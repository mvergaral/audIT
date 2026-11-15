"""Conciliación y publicación del corte 3.1 a partir de los cuatro entregables."""
import csv
import hashlib
import json
import re
import shutil
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

import openpyxl
import pymupdf
from lxml import etree

D = Path(__file__).resolve().parent
mejora = D.parents[3]
O = D.parents[1] / 'outputs/informe3-mejora'
E = O / 'entrega'
base = mejora / 'Entrega-3.0'
cut = mejora / 'Entrega-3.1'
report, workbook, deck, reading = [
    f'INFORME3_AUDIT_{suffix}_20261115.{ext}'
    for suffix, ext in [('COSTOS_VENTA', 'pdf'), ('PLANILLA', 'xlsx'),
                        ('PRESENTACION', 'pptx'), ('PRESENTACION', 'pdf')]
]
base_book = openpyxl.load_workbook(base / 'INFORME3_AUDIT_PLANILLA_20261114.xlsx')
base_values = openpyxl.load_workbook(base / 'INFORME3_AUDIT_PLANILLA_20261114.xlsx', data_only=True)
formulas = openpyxl.load_workbook(E / workbook)
values = openpyxl.load_workbook(E / workbook, data_only=True)
assert set(base_book.sheetnames) <= set(formulas.sheetnames)
assert not formulas._external_links
def labels(sheet):
    return [(c.coordinate, c.value) for row in sheet for c in row if c.data_type == 's']

assert labels(base_book['RESUMEN']) == labels(formulas['RESUMEN'])
assert base_book['RESUMEN'].merged_cells == formulas['RESUMEN'].merged_cells
assert all(s.protection.sheet for s in formulas)
assert not [(s.title, c.coordinate, c.value) for s in values for row in s for c in row if c.data_type == 'e']
for s, a in [('Parámetros corrección', 'B36'), ('Parámetros corrección', 'B39'),
             ('Parámetros D2', 'B16'), ('Ajustes de operación', 'B57'), ('Mesa de ayuda', 'C8')]:
    assert not formulas[s][a].protection.locked
    assert any(a in r for r in formulas[s].data_validations.dataValidation)
for s, a in [('Calendario E25', 'E22'), ('Control de entrega', 'B8'), ('Parámetros D2', 'B32')]:
    assert formulas[s][a].protection.locked
for a, expected in {'B7': 12, 'B8': 36, 'B22': 36, 'B23': 57, 'B24': 0, 'B25': 0, 'B28': 0}.items():
    assert abs(values['Control de entrega'][a].value - expected) < .01
assert values['Ingresos']['H22'].value > 0 and values['Ingresos']['G22'].value > 0
assert values['Ingresos']['J58'].value > 0
assert len(formulas['Gráficos UF']._charts) == 5
series = json.loads((O / 'revision/series.json').read_text())
expected = [
    [series[k] for k in ['personal', 'infra', 'otros']],
    [series[k] for k in ['ajustada', 'operativo', 'cajaApertura']],
    [series[k] for k in ['ajustada', 'madurezOperativo', 'madurezCajaApertura']],
    [series[k] for k in ['cajaBase', 'cajaEstres', 'cajaCubierta', 'cajaH4']],
    [series['banco'], series['socios'], [-x for x in series['amort']]],
]
ns = {'c': 'http://schemas.openxmlformats.org/drawingml/2006/chart'}
uf = values['Parámetros D2']['B21'].value
assert values['Gráficos UF']['Q2'].value == values['Gráficos UF']['S2'].value
assert values['Gráficos UF']['Q2'].value == values['Parámetros D2']['B4'].value / uf
assert values['Gráficos UF']['R2'].value == 0
assert all(
    abs(a - b) < .01 for a, b in zip(series['cajaApertura'][1:], series['curvaCaja'])
)
with ZipFile(E / deck) as z:
    charts = sorted(n for n in z.namelist() if re.fullmatch(r'ppt/slides/charts/chart\d+.xml', n))
    assert len(charts) == len(expected)
    for part, data in zip(charts, expected):
        root = etree.fromstring(z.read(part))
        outputs = root.findall('.//c:ser', ns)
        assert len(outputs) == len(data), part
        for output, model in zip(outputs, data):
            points = output.findall('./c:val/c:numRef/c:numCache/c:pt', ns)
            points.sort(key=lambda pt: int(pt.get('idx')))
            got = [float(pt.find('c:v', ns).text) for pt in points]
            assert len(got) == len(model)
            assert all(abs(a - b / uf) <= .00501 for a, b in zip(got, model)), part

with (D / 'economico/datos/partidas.csv').open() as file:
    partidas = list(csv.DictReader(file, delimiter=';'))
checked = 0
for item in partidas:
    if item['planilla']:
        sheet, cell = item['planilla'].rsplit('!', 1)
        assert abs(values[sheet][cell].value - int(item['valor'])) <= .5000001, item
        checked += 1

with pymupdf.open(E / report) as pdf:
    text = [p.get_text() for p in pdf]
    first_annex = next(i + 1 for i, p in enumerate(text) if 'GEN-01.' in p)
    first_body = next(i + 1 for i, p in enumerate(text) if 'Adquisiciones clave o relevantes' in p and 'primer' not in p and i > 5)
    assert first_annex > first_body and f'folio {first_annex}' in re.sub(r'\s+', ' ', text[first_annex - 1]).lower()
    assert not any('??' in p for p in text)
    pages = len(pdf)
with pymupdf.open(E / reading) as pdf:
    slides = len(pdf)
    assert slides == 11 and any(link.get('uri') for link in pdf[-1].get_links())
    assert 'Magnitudes de la oferta' in pdf[1].get_text()

cut.mkdir(exist_ok=True)
for name in [report, workbook, deck, reading]:
    shutil.copyfile(E / name, cut / name)
with (cut / 'Variacion-mensual.csv').open('w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(['mes', 'costo_3.0_clp', 'costo_3.1_clp', 'variacion_clp',
                     'personal_variacion_clp', 'administracion_variacion_clp',
                     'caja_3.0_clp', 'caja_3.1_clp', 'cota_3.0_clp', 'cota_3.1_clp'])
    for month in range(1, 57):
        r = month + 1
        old, new = [b['Costos'][f'K{r}'].value for b in (base_values, values)]
        num = lambda x: f'{x:.2f}'.replace('.', ',')
        costs = lambda c: values['Costos'][f'{c}{r}'].value - base_values['Costos'][f'{c}{r}'].value
        balances = [b['Flujo de Caja'][f'{col}{r}'].value for col in ('W', 'AG') for b in (base_values, values)]
        writer.writerow([month, *map(num, [old, new, new - old, costs('G'), costs('E'), *balances])])

def metadata(path):
    return {'nombre': path.name, 'bytes': path.stat().st_size, 'sha256': hashlib.sha256(path.read_bytes()).hexdigest()}

package_names = [report, workbook, deck, reading, 'LEEME.txt', 'Registro-de-mejora.md', 'Variacion-mensual.csv']
manifest = {
    'licitacion': 'TFEP-01/2026', 'version': '3.1', 'fecha': '2026-11-15',
    'estado': 'Corte para revisión. Pendientes condiciones de ejecución y validación sustantiva.',
    'archivos': [metadata(cut / n) for n in package_names],
    'linea_base': {'version': '3.0', 'fecha': '2026-11-14',
                   'archivos': [metadata(p) for p in sorted(base.iterdir()) if p.is_file()]},
    'prototipo': {'url': 'https://carlosabarza.github.io/PaginaAudIT/',
                  'ruta': 'Portal Clientes > Simulador Operativo en Vivo',
                  'validacion': 'Ruta pública anterior verificada. Cambios de razón social y rótulos compilados localmente.'},
    'comprobaciones': {'paginas_informe': pages, 'folio_anexo_art46': first_annex, 'laminas': slides,
                        'graficos_editables_pptx': len(expected), 'hojas': len(formulas.sheetnames),
                        'celdas_conciliadas': checked, 'pruebas_propagacion': 5, 'vinculos_externos_excel': 0}
}
manifest_name = 'manifiesto.json'
(cut / manifest_name).write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
zip_path = cut / 'INFORME3_AUDIT_3.1_20261115.zip'
with ZipFile(zip_path, 'w', compression=ZIP_DEFLATED, compresslevel=9) as z:
    for name in [*package_names, manifest_name]:
        z.write(cut / name, name)
with ZipFile(zip_path) as z:
    assert z.testzip() is None
    assert z.namelist() == [*package_names, manifest_name]
    for file in manifest['archivos']:
        assert hashlib.sha256(z.read(file['nombre'])).hexdigest() == file['sha256']
print(json.dumps(manifest['comprobaciones'], ensure_ascii=False))
