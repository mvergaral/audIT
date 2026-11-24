"""Publica las cachés recalculadas por el generador y protege las hojas OOXML."""
import json
from copy import deepcopy
from pathlib import Path
from zipfile import ZipFile

import openpyxl
from lxml import etree
from openpyxl.utils.cell import range_boundaries

D = Path(__file__).resolve().parent
O = D.parents[1] / 'outputs/informe3-mejora'
source = O / 'revision/modelo-borrador-v4.xlsx'
target = O / 'entrega/INFORME3_AUDIT_PLANILLA_20261115.xlsx'
book = openpyxl.load_workbook(source, data_only=True)
formulas = openpyxl.load_workbook(source, data_only=False)
v = lambda sheet, address: book[sheet][address].value
rows = lambda sheet, columns, first, last: [
    [v(sheet, f'{c}{r}') for c in columns] for r in range(first, last + 1)
]
errors = [(s.title, c.coordinate, c.value) for s in book for row in s for c in row if c.data_type == 'e']
assert not errors, errors
assert all(isinstance(v(sheet, cell), (int, float)) for sheet, cell in [('RESUMEN','C8'),('RESUMEN','H8'),('Indicadores','B2'),('Indicadores','B3'),('Control de entrega','B8')]), 'Caché crítica vacía'
controls = rows('Control de entrega', ['A', 'B'], 2, 31)
assert v('Control de entrega', 'B8') == 36
assert v('Indicadores', 'B8') == v('Ingresos', 'J58')
assert abs(v('RESUMEN', 'C8') - sum(x[0] for x in rows('Costos', 'K', 2, 57))) < .01
assert abs(v('RESUMEN', 'H8') - sum(x[0] for x in rows('Ingresos', 'E', 2, 57))) < .01
assert abs(v('Control de entrega', 'B28')) < .01, controls
editable = {
    'Parámetros corrección': ['B3:B10', 'B12:B36', 'B38:B41', 'B43', 'B46:B50', 'B53',
                             'B57:B59', 'B62', 'B64:B77'],
    'Parámetros D2': ['B2:B3', 'B5:B9', 'B11:B13', 'B16:B17', 'B19:B21'],
    'Tarifas por perfil': ['B2:I20'],
    'Contrato de soporte': ['B2:D13'],
    'Ajustes de operación': ['B2:C57'],
    'Mesa de ayuda': ['C7:D11'],
}
ns = 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'
def tag(name):
    return f'{{{ns}}}{name}'

temporary = target.with_suffix('.tmp')
with ZipFile(source) as incoming, ZipFile(temporary, 'w') as outgoing:
    styles = etree.fromstring(incoming.read('xl/styles.xml'))
    cell_xfs = styles.find(tag('cellXfs'))
    fonts = styles.find(tag('fonts'))
    changed_style = {}
    def style_id(original, unlock):
        key = (int(original), unlock)
        if key in changed_style:
            return str(changed_style[key])
        local = deepcopy(cell_xfs[key[0]])
        protection = local.find(tag('protection'))
        if protection is None:
            protection = etree.Element(tag('protection'))
            extension = local.find(tag('extLst'))
            if extension is None:
                local.append(protection)
            else:
                extension.addprevious(protection)
        protection.set('locked', '0' if unlock else '1')
        local.set('applyProtection', '1')
        if unlock:
            font = deepcopy(fonts[int(local.get('fontId', '0'))])
            color = font.find(tag('color'))
            if color is None:
                color = etree.SubElement(font, tag('color'))
            color.attrib.clear()
            color.set('rgb', 'FF0000FF')
            local.set('fontId', str(len(fonts)))
            local.set('applyFont', '1')
            fonts.append(font)
        changed_style[key] = len(cell_xfs)
        cell_xfs.append(local)
        return str(changed_style[key])

    replacements = {}
    # Resolve sheet parts through relationships rather than assuming worksheet numbering.
    wb = etree.fromstring(incoming.read('xl/workbook.xml'))
    rels = etree.fromstring(incoming.read('xl/_rels/workbook.xml.rels'))
    destinations = {r.get('Id'): r.get('Target') for r in rels}
    for sheet in wb.find(tag('sheets')):
        name = sheet.get('name')
        rid = next(value for key, value in sheet.attrib.items() if key.endswith('}id'))
        rel = destinations[rid]
        member = rel.lstrip('/') if rel.startswith('/') else 'xl/' + rel
        tree = etree.fromstring(incoming.read(member))
        existing = tree.find(tag('sheetProtection'))
        if existing is not None:
            tree.remove(existing)
        protection = etree.Element(tag('sheetProtection'), sheet='1', objects='1', scenarios='1')
        ordered = {'sheetCalcPr', 'sheetData'}
        preceding = [c for c in tree if etree.QName(c).localname in ordered]
        preceding[-1].addnext(protection)
        cells = {c.get('r'): c for c in tree.findall(f'{tag("sheetData")}/{tag("row")}/{tag("c")}')}
        for address, c in cells.items():
            item = formulas[name][address]
            unlock = False
            # Keep a formula protected even if a future revision adds one within an input range.
            if item.data_type != 'f':
                for rng in editable.get(name, []):
                    x1, y1, x2, y2 = range_boundaries(rng)
                    if x1 <= item.column <= x2 and y1 <= item.row <= y2:
                        unlock = True
                        break
            c.set('s', style_id(c.get('s', '0'), unlock))
        # A quoted option has no base-case amount. Create empty editable cells where the exporter omitted them.
        if name == 'Mesa de ayuda':
            for row in tree.findall(f'{tag("sheetData")}/{tag("row")}'):
                if not 7 <= int(row.get('r')) <= 11:
                    continue
                for column in 'CD':
                    address = column + row.get('r')
                    if address not in cells:
                        cell = etree.Element(tag('c'), r=address, s=style_id('0', True))
                        next_cell = next((c for c in row if c.get('r', '')[0:1] > column), None)
                        if next_cell is None:
                            row.append(cell)
                        else:
                            next_cell.addprevious(cell)
        validation = tree.find(tag('dataValidations'))
        if validation is not None:
            for rule in validation:
                rule.set('showErrorMessage', '1')
            hard_limits = {
                'Parámetros corrección': ('B38:B41', 'AND(ISNUMBER(B38),B38=INT(B38),B38>=0,SUM($B$38:$B$41)<=$B$63)',
                                          'El total de kits no puede superar B63. Reduzca primero el lote de origen.'),
                'Parámetros D2': ('B16:B17', 'AND(ISNUMBER(B16),ISNUMBER(B17),B16=INT(B16),B17=INT(B17),B16>=1,B17>=1,B16+B17-1<=56)',
                                 'El inicio y la duración deben ser meses enteros y terminar a más tardar en M56.'),
            }
            if name in hard_limits:
                region, condition, error = hard_limits[name]
                for rule in list(validation):
                    if rule.get('sqref') == region:
                        validation.remove(rule)
                rule = etree.SubElement(validation, tag('dataValidation'), type='custom',
                                        sqref=region, showErrorMessage='1', errorStyle='stop', error=error)
                etree.SubElement(rule, tag('formula1')).text = condition
                validation.set('count', str(len(validation)))
        replacements[member] = etree.tostring(tree)
    fonts.set('count', str(len(fonts)))
    cell_xfs.set('count', str(len(cell_xfs)))
    replacements['xl/styles.xml'] = etree.tostring(styles)
    for item in incoming.infolist():
        outgoing.writestr(item, replacements.get(item.filename, incoming.read(item)))

temporary.replace(target)

metrics = {
    'capital_inicial_clp': v('Parámetros corrección', 'B4'),
    'facilidad_contingente_clp': v('Parámetros corrección', 'B28'),
    'costo_clp': v('RESUMEN', 'C8'), 'venta_clp': v('RESUMEN', 'H8'),
    'implementacion_clp': v('Parámetros D2', 'B14'), 'mensualidad_clp': v('Parámetros D2', 'B15'),
    'van_clp': v('Indicadores', 'B2'), 'tir_mensual': v('Indicadores', 'B3'),
    'margen': v('Indicadores', 'B10'), 'tasa_mensual': v('Parámetros D2', 'B10'),
    'caja_minima_tesoreria': v('Control de entrega', 'B2'),
    'caja_minima_neta': v('Control de entrega', 'B3'),
    'linea_base_maxima': v('Control de entrega', 'B5'), 'controles': controls,
    'escenarios': rows('Sensibilidad', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 2, 16),
    'flujo': rows('Flujo de Caja', ['A','E','F','G','H','O','P','Q','R','S','T','U','V','W','AA','AB','AC','AD'], 2, 63),
    'costos': rows('Costos', 'ABCDEFGHIJKL', 2, 57),
    'soporte_mensual': rows('Personal', 'AD', 22, 57),
    'instalacion': rows('Instalación por lote', 'BACDEFGHIJK', 2, 21),
    'errores': errors,
}
(O/'revision/resultados.json').write_text(json.dumps(metrics, ensure_ascii=False, indent=2)+'\n')
print({k: value for k, value in metrics.items() if not isinstance(value, list)})
