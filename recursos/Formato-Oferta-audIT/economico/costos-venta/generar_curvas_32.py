"""Dibuja las dos curvas con los resultados almacenados en el respaldo 3.2."""
import json
from pathlib import Path

from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen.canvas import Canvas


HERE = Path(__file__).resolve().parent
NAVY = HexColor('#102D3E')
TEAL = HexColor('#007582')
GRID = HexColor('#D7E2E7')


def render(rows, filename, title, series):
    chart = Canvas(str(HERE / filename), pagesize=(420, 219))
    chart.setTitle(title)
    chart.setFillColor(NAVY)
    chart.setFont('Arial', 14)
    chart.drawString(12, 201, title)
    chart.setFont('Arial', 10)
    chart.drawString(12, 184, 'Base 3.2 · Millones de CLP · M1–M56')

    left, bottom, width, height = 51, 47, 354, 122
    upper = max(row[col] for row in rows for col, _, _ in series) * 1.05
    for i in range(6):
        y = bottom + i * height / 5
        chart.setStrokeColor(GRID)
        chart.setLineWidth(0.55)
        chart.line(left, y, left + width, y)
        chart.setFillColor(NAVY)
        chart.drawRightString(left - 6, y - 3, f'{upper * i / 5e6:,.0f}'.replace(',', '.'))

    for month in (1, 8, 16, 24, 32, 40, 48, 56):
        x = left + (month - 1) * width / 55
        chart.drawCentredString(x, bottom - 15, f'M{month}')

    for index, (col, label, color) in enumerate(series):
        chart.setStrokeColor(color)
        chart.setFillColor(color)
        chart.setLineWidth(1.7)
        points = [(left + (row[0] - 1) * width / 55, bottom + row[col] / upper * height) for row in rows]
        path = chart.beginPath()
        path.moveTo(*points[0])
        for point in points[1:]:
            path.lineTo(*point)
        chart.drawPath(path)
        key_x = left + index * 175
        chart.line(key_x, 14, key_x + 16, 14)
        chart.drawString(key_x + 22, 11, label)
    chart.save()


if __name__ == '__main__':
    pdfmetrics.registerFont(TTFont('Arial', 'C:/Windows/Fonts/arial.ttf'))
    data = json.loads((HERE.parent / 'datos/respaldo-3.2.json').read_text(encoding='utf-8'))
    rows = [row for row in data['curva'][1:] if isinstance(row[0], int)]
    if [row[0] for row in rows] != list(range(1, 57)):
        raise ValueError('La curva debe cubrir los 56 meses de evaluación')
    render(rows, 'curva-s.pdf', 'Costo y facturación acumulada', ((1, 'Costo con intereses', TEAL), (2, 'Facturación', NAVY)))
    render(rows, 'solvencia-3.2.pdf', 'Caja financiada del caso base', ((3, 'Saldo de caja', TEAL),))
