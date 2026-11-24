"""Sincroniza respaldos y corrige rótulos en copia, sin alterar el cálculo 3.2."""
from decimal import Decimal
from pathlib import Path
from xml.sax.saxutils import escape
import hashlib
import json
import xml.etree.ElementTree as ET
import zipfile
import openpyxl

ROOT=Path(__file__).resolve().parents[2]
BASE=ROOT/'recursos/Formato-Oferta-audIT'
SOURCE=ROOT/'outputs/3.2/Entrega-3.2/INFORME3_AUDIT_PLANILLA_3.2_20261115.xlsx'
OUT=ROOT/'outputs/3.2/Conciliacion-D2-20261124';OUT.mkdir(parents=True,exist_ok=True)
W=openpyxl.load_workbook(SOURCE,data_only=True)
replacements={
 'Montaje externo sustituye horas internas; técnico interno sale en M10; campo en operación por visita':'Montaje externo sustituye horas internas; técnico interno de implementación sale en M19; campo en operación con coordinación interna y visitas externas',
 'Servicio de campo externo M10-M56 (CLP)':'Servicio de campo externo: base M19–M56 (CLP)',
 'Corte en M19 para cubrir con técnico interno la instalación de etapas 1 y 2 (M7-M9 y M16-M18 según T-14 y S4); desde M19 las atenciones de campo son 100% externas por visita.':'Base M19: sale el técnico interno de implementación. Piloto M6 y montaje por lotes M7–M9. Desde M19 se presupuesta servicio externo por visita; en operación audIT mantiene 80 h/mes de recepción, stock y coordinación.',
 'S7 tabla 7-cobertura (propios y terceros); activación presupuestada ligada a instalación. Ventanas de terceros por acreditar.':'Comparación del S7 anterior con el presupuesto 3.2. Para la base conciliada, consultar Instalación por lote y Activaciones. Ventanas de terceros por acreditar.',
 'Técnico M18–M20 (HH/mes)':'Técnico interno M18 (HH/mes)',
 'Campo: marcha blanca, sustituciones y asistencia a recepción. Falta cuadrante y demanda por terminal.':'M18: 160 h internas. Desde M19 el técnico de implementación sale; M19–M20: cero horas de ese perfil. En M21–M56: 80 h/mes de coordinación interna y servicio externo.',
 'Dos perfiles: ciclo de vida, reposiciones y recepción en terminal.':'0,5 FTE interno: recepción, stock y coordinación. Las reposiciones y visitas se ejecutan con proveedor externo.',
 'Precio 3.0 para el cotejo. Recálculo opcional con margen explícito.':'Precio 3.2 por costo de fase y margen objetivo; referencia histórica separada en Parámetros corrección B60.',
 'Mensualidad 3.0 para el cotejo. Recálculo opcional con el calendario de servicio.':'Mensualidad 3.2 por costo de operación y margen objetivo; referencia histórica separada en B61.',
}
NS={'m':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
def signature(path):
    out=[]
    with zipfile.ZipFile(path) as z:
        for name in sorted(n for n in z.namelist() if n.startswith('xl/worksheets/') and n.endswith('.xml')):
            tree=ET.fromstring(z.read(name))
            for c in tree.findall('.//m:c',NS):
                f=c.find('m:f',NS);v=c.find('m:v',NS)
                # Fórmulas, números y referencias a cadenas permanecen intactos.
                out.append((name,c.get('r'),c.get('t'),ET.tostring(f) if f is not None else None,v.text if v is not None else None))
    return out

dest=OUT/'INFORME3_AUDIT_PLANILLA_3.2_CONCILIADA_D2.xlsx'
staged=dest.with_suffix('.tmp')
with zipfile.ZipFile(SOURCE) as zin,zipfile.ZipFile(staged,'w') as zout:
    for entry in zin.infolist():
        data=zin.read(entry.filename)
        if entry.filename=='xl/sharedStrings.xml':
            for before, after in replacements.items():
                old = escape(before).encode('utf-8')
                new = escape(after).encode('utf-8')
                if data.count(old) != 1:
                    raise ValueError(f'No se encontró un rótulo único para {before!r}')
                data = data.replace(old, new, 1)
        zout.writestr(entry,data)
if signature(SOURCE) != signature(staged):
    raise ValueError('Cambió una fórmula o un valor; no se libera la copia')
with zipfile.ZipFile(SOURCE) as zin, zipfile.ZipFile(staged) as zout:
    changed_entries = [name for name in zin.namelist() if zin.read(name) != zout.read(name)]
    if changed_entries != ['xl/sharedStrings.xml']:
        raise ValueError(f'Se alteraron partes inesperadas del libro: {changed_entries}')
with staged.open('rb') as stream:
    checked = openpyxl.load_workbook(stream, data_only=True, read_only=True)
    changes = []
    for sheet in W:
        for row in checked[sheet.title].iter_rows():
            for cell in row:
                if cell.value is None:
                    continue
                previous = sheet[cell.coordinate].value
                if cell.value == previous:
                    continue
                expected = previous
                if isinstance(previous, str):
                    for before, after in replacements.items():
                        expected = expected.replace(before, after)
                if cell.value != expected:
                    raise ValueError(f'Valor no previsto en {sheet.title}!{cell.coordinate}')
                changes.append(f'{sheet.title}!{cell.coordinate}')
    checked.close()
staged.replace(dest)
cw=W['Cuadro maestro']
def su(rows,col):return sum(cw.cell(i,col).value or 0 for i in rows)
vals={'implementacion':W['RESUMEN']['H6'].value,'operacion':W['RESUMEN']['H7'].value,
 'firma-inn1':W['Innovaciones']['D2'].value,'recupero-inn4':W['Beneficios Curimón']['B4'].value,
 'egreso-inn5':W['Innovaciones']['D6'].value,'capital-inicial':W['Parámetros corrección']['B4'].value,
 'hardware-mandante':W['Hardware del mandante']['H40'].value,'licencias-d3':su([4,13],3),
 'costo-fase-implementacion':W['RESUMEN']['C6'].value,'costo-fase-operacion':W['RESUMEN']['C7'].value,
 'van':W['Indicadores']['B2'].value,'equilibrio-nominal':W['Indicadores']['B12'].value,'equilibrio-van':W['Indicadores']['B13'].value,
 'cobro-m57':W['Indicadores']['B8'].value,'capital-adicional-h5':W['Parámetros corrección']['B28'].value,
 'reserva-d4':W['Parámetros corrección']['B26'].value,'deficit-h5':W['Sensibilidad']['J2'].value,
 'deficit-h5-reserva':W['Sensibilidad']['J4'].value,'caja-estres-h5':W['Sensibilidad']['G5'].value,
 'gasto-rrhh':su([2,11],3),'gasto-administracion':su([8,17],3),
 'gasto-inversion':cw['C3'].value,'gasto-operacion-directo':su([4,5,6,7,9,10,13,14,15,16,18],3),
 'gasto-proveedores':cw['C12'].value,
 'costo-directo-implementacion':su(range(2,8),3),'costo-directo-operacion':su(range(11,17),3),
 'costo-indirecto':su([8,9,10,17,18],3),
 'cuadro-impl-directo-costo':su(range(2,8),3),'cuadro-impl-directo-venta':su(range(2,8),4),
 'cuadro-impl-indirecto-costo':su(range(8,11),3),'cuadro-impl-indirecto-venta':su(range(8,11),4),
 'cuadro-op-directo-costo':su(range(11,17),3),'cuadro-op-directo-venta':su(range(11,17),4),
 'cuadro-op-indirecto-costo':su(range(17,19),3),'cuadro-op-indirecto-venta':su(range(17,19),4)}
for inn in range(1,6):
    rows=[r for r in W['Atribución innovaciones'].iter_rows(min_row=2,values_only=True) if r[0]==f'INN-{inn}']
    vals[f'innovacion-{inn}-inversion']=sum(r[6] or 0 for r in rows if isinstance(r[2],int) and r[2]<=20)
    vals[f'innovacion-{inn}-costo']=sum(r[6] or 0 for r in rows if isinstance(r[2],int) and r[2]>=21)
    vals[f'innovacion-{inn}-beneficio']=W['Innovaciones'][f'E{inn + 1}'].value
source_cells = {
    'proyecto': 'RESUMEN!H8',
    'gasto-total': 'RESUMEN!C8',
    'costo-total': 'Cuadro maestro!C19',
    'gasto-inversion': 'Cuadro maestro!C3',
    'gasto-proveedores': 'Cuadro maestro!C12',
    'capital-adicional-h5': 'Parámetros corrección!B28',
    'reserva-d4': 'Parámetros corrección!B26',
    'caja-estres-h5': 'Sensibilidad!G5',
    'deficit-h5': 'Sensibilidad!J2',
    'deficit-h5-reserva': 'Sensibilidad!J4',
    'van': 'Indicadores!B2',
    'firma-inn1': 'Innovaciones!D2',
    'recupero-inn4': 'Beneficios Curimón!B4',
    'hardware-mandante': 'Hardware del mandante!H40',
    'egreso-inn5': 'Innovaciones!D6',
    'capital-inicial': 'Parámetros corrección!B4',
}
source_ranges = {'licencias-d3': 'Cuadro maestro!C4+C13; Costos!C2:C57'}
source_cells.update({f'innovacion-{inn}-beneficio': f'Innovaciones!E{inn + 1}' for inn in range(1, 6)})


def csv_amount(value):
    # El lector Lua convierte el numerador a un entero y lo duplica al redondear.
    # Se publica CLP entero. Seis decimales retienen precisión de la planilla
    # sin desbordar el entero con montos del orden de miles de millones.
    return format(Decimal(str(value)).quantize(Decimal('0.000001')).normalize(), 'f')


csvpath=BASE/'economico/datos/partidas.csv';lines=[]
obsolete={'caja-estres-horas','deficit-h5-30-dias'}
concepts = {
    'deficit-h5': 'Déficit antes de cobros en atraso de H5 a M13',
    'reserva-d4': 'Reserva de sensibilidad D4',
    'hardware-mandante': 'Hardware a cargo del mandante, total referencial',
    'cobro-m57': 'Mensualidad neta de operación, último cobro en M57',
    'firma-inn1': 'Egreso directo por firma automática INN-1',
    'recupero-inn4': 'Recupero bruto referencial del mandante en 36 meses, INN-4',
    'licencias-d3': 'Licencias de implementación y operación',
    'egreso-inn5': 'Egreso directo de INN-5',
    'capital-inicial': 'Capital inicial del caso base',
}
seen = set()
for line in csvpath.read_text(encoding='utf-8').splitlines():
    if not line or line.startswith('#'):lines.append(line);continue
    cells=line.split(';');key=cells[0]
    if key in obsolete:continue
    seen.add(key)
    if key in concepts:cells[1]=concepts[key]
    if key.startswith('innovacion-'):
        cells[1] = cells[1].replace('costo operacional incremental','personal atribuido en operación').replace('inversión','personal atribuido en implementación').replace('beneficio esperado','beneficio monetario reconocido en el caso base')
    if key in vals:cells[3]=csv_amount(vals[key])
    if key in source_cells:cells[5]=source_cells[key]
    lines.append(';'.join(cells))
for key in ('egreso-inn5', 'capital-inicial'):
    if key not in seen:
        lines.append(';'.join([key, concepts[key], 'CLP', csv_amount(vals[key]), 'no', source_cells[key]]))
csvpath.write_text('\n'.join(lines)+'\n',encoding='utf-8')
sens=[]
for row in W['Sensibilidad'].iter_rows(min_row=2,max_row=16,values_only=True):
    if row[0]:sens.append(dict(zip([c.value for c in W['Sensibilidad'][1]],row)))
report={'origen_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),'copia_sha256':hashlib.sha256(dest.read_bytes()).hexdigest(),'celdas_texto_corregidas':len(changes),'referencias_texto_corregidas':changes,'cadenas_compartidas_corregidas':len(replacements),'partes_ooxml_modificadas':changed_entries,'formulas_valores_y_caches_identicos':True,'partidas':vals,'rangos_fuente':source_ranges,'sensibilidad':sens,'curva':[[c.value for c in row[:4]] for row in W['Curva S']],'tir':W['Indicadores']['B3'].value,'recuperacion':W['Indicadores']['B14'].value}
(BASE/'economico/datos/respaldo-3.2.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
(OUT/'verificacion-copia.json').write_text(json.dumps({k:v for k,v in report.items() if k not in ['sensibilidad','curva']},ensure_ascii=False,indent=2),encoding='utf-8')
print('Copia de rótulos:',len(changes),'celdas; fórmulas, números y cachés idénticos.')
print('Partidas numéricas sincronizadas:',len(vals))
