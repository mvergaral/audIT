from pathlib import Path
import json
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor

R=Path(__file__).resolve().parents[2]/'tmp/cierre-entrega-3/recursos/Formato-Oferta-audIT'
D=json.loads((R/'economico/datos/respaldo-3.2.json').read_text(encoding='utf-8'))
pdfmetrics.registerFont(TTFont('Audit32',r'C:/Windows/Fonts/arial.ttf'))
rows=[r for r in D['curva'][1:] if isinstance(r[0],int)]
for name,title,series in [('curva-s.pdf','Costo y facturación acumulada',[(1,'Costo con intereses','#007582'),(2,'Facturación','#102D3E')]),('solvencia-3.2.pdf','Caja financiada del caso base',[(3,'Saldo de caja','#007582')])]:
    c=canvas.Canvas(str(R/'economico/costos-venta'/name),pagesize=(720,420))
    c.setTitle(title);c.setFont('Audit32',18);c.drawString(58,385,title)
    c.setFont('Audit32',12);c.drawString(58,362,'Referencia 3.2 · Millones de CLP · M1--M56')
    ymax=max(r[col] for r in rows for col,_,_ in series)*1.05
    for i in range(6):
        y=70+i*50;v=ymax*i/5
        c.setStrokeColor(HexColor('#D7E2E7'));c.line(80,y,690,y)
        c.setFillColor(HexColor('#102D3E'));c.drawRightString(72,y-4,f'{v/1e6:,.0f}'.replace(',','.'))
    for m in [1,8,16,24,32,40,48,56]:c.drawCentredString(80+(m-1)*610/55,48,f'M{m}')
    for k,(col,label,color) in enumerate(series):
        c.setStrokeColor(HexColor(color));c.setLineWidth(2);path=c.beginPath()
        for i,row in enumerate(rows):
            x=80+(row[0]-1)*610/55;y=70+row[col]/ymax*250
            if i:path.lineTo(x,y)
            else:path.moveTo(x,y)
        c.drawPath(path);c.setFillColor(HexColor(color));c.drawString(80+k*250,25,label)
    c.save()
print('Curvas contractuales y saldo de caja generados por separado.')
