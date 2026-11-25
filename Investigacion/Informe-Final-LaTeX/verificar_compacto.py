"""Verificación auxiliar de PDF y aritmética de la tabla del maestro (IA nivel 2)."""
from pathlib import Path
import json
import re
import fitz
from PIL import Image, ImageOps, ImageDraw

ROOT = Path(__file__).resolve().parent
pdf = ROOT / 'build' / '10-AUDIT-TI-12.pdf'
doc = fitz.open(pdf)
report = {'paginas': len(doc), 'archivo': str(pdf), 'detalle': [], 'fuera_de_pagina': []}
sheet = Image.new('RGB', (1260, ((len(doc) + 2) // 3) * 615), '#d8dde1')
for i, page in enumerate(doc):
    words = page.get_text('words')
    report['detalle'].append({'pagina': i + 1, 'palabras': len(words), 'inicio': page.get_text()[:180]})
    for x0, y0, x1, y1, word, *_ in words:
        if x0 < 0 or y0 < 0 or x1 > page.rect.width or y1 > page.rect.height:
            report['fuera_de_pagina'].append({'pagina': i + 1, 'texto': word})
    pix = page.get_pixmap(matrix=fitz.Matrix(0.67, 0.67), alpha=False)
    image = Image.frombytes('RGB', (pix.width, pix.height), pix.samples)
    sheet.paste(image, ((i % 3) * 420 + 10, (i // 3) * 615 + 25))
    ImageDraw.Draw(sheet).text(((i % 3) * 420 + 10, (i // 3) * 615 + 5), f'Pagina {i+1}', fill='black')
sheet.save(ROOT / 'build' / 'revision-contacto.png')
for p in (6, 7, 8, 10, 15):
    if p <= len(doc):
        doc[p-1].get_pixmap(matrix=fitz.Matrix(1.4, 1.4)).save(ROOT / 'build' / f'revision-{p:02}.png')

# Reconstrucción independiente de los flujos por período de la tabla 3.2.
rows = [
    [375, 0, 0, 0, 0], [0, 387.5, 0, 0, 0],
    [432, 288, 576, 432, 288], [576, 384, 768, 576, 384],
    [27, 178, 280, 240, 166], [60, 40, 80, 60, 40],
    [108, 123.5, 246.96, 185.2, 123.5], [0, 0, 112.5, 112.5, 112.5],
    [90, 60, 120, 90, 60], [15, 70, 85, 85, 55],
]
periods = [(1,12),(13,20),(21,36),(37,48),(49,56)]
flow = []
for m in range(1,57):
    k = next(k for k, (a,b) in enumerate(periods) if a <= m <= b)
    n = periods[k][1] - periods[k][0] + 1
    cost = sum(row[k] / n for j,row in enumerate(rows) if j != 6)
    cost += (0 if m < 6 else 108 / 7) if k == 0 else rows[6][k] / n
    flow.append(cost)
report['aritmetica'] = {
    'tco_uf': round(sum(flow), 2),
    'van_uf': round(sum(v / 1.009**m for m,v in enumerate(flow,1)), 2),
    'purview_recalculado': sum(v*w for v,w in zip([5,1,5,5,4],[.25,.20,.25,.20,.10])),
    'rosi_condicional_pct': (55000*.85-sum(flow))/sum(flow)*100,
    'umbral_sin_eficacia_56_meses_pct': sum(flow)/55000*100,
}
log = (ROOT / 'build' / '10-AUDIT-TI-12.log').read_text(encoding='utf-8', errors='replace')
report['advertencias'] = re.findall(r'(?:Overfull[^\n]*|Missing character[^\n]*|LaTeX Warning:[^\n]*)', log)
(ROOT / 'build' / 'verificacion.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps(report, ensure_ascii=True, indent=2))
assert 10 <= len(doc) <= 15, f'Extensión fuera de rango: {len(doc)}'
assert not report['fuera_de_pagina'], 'Hay texto fuera de los bordes del PDF'
assert abs(report['aritmetica']['tco_uf'] - 8492.16) < .01
