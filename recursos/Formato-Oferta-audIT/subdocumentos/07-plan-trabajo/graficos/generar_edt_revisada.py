"""Genera las vistas sintéticas de la EDT desde el diccionario T-14."""
from pathlib import Path
import json, re
import fitz
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, white
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from xml.sax.saxutils import escape

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
# Arial conserva las métricas de la composición y queda incrustada en el PDF.
FONTDIR=Path('C:/Windows/Fonts')
pdfmetrics.registerFont(TTFont('Helvetica',str(FONTDIR/'arial.ttf')))
pdfmetrics.registerFont(TTFont('Helvetica-Bold',str(FONTDIR/'arialbd.ttf')))
pdfmetrics.registerFontFamily('Helvetica',normal='Helvetica',bold='Helvetica-Bold',italic='Helvetica',boldItalic='Helvetica-Bold')
HERE=Path(__file__).resolve().parent
BASE=HERE.parent
ROOT=HERE.parents[4]
OUT=HERE/'edt-revisada'; OUT.mkdir(exist_ok=True)
P=json.loads((ROOT/'Informe-2/d2/99_Generacion/plan_detallado.json').read_text(encoding='utf-8'))['paquetes']
# Ajustes conciliados con las fichas T-19 vigentes.
AJ=json.loads((HERE/'ajustes-paquetes.json').read_text(encoding='utf-8'))
for paquete in P:
 if paquete['codigo'] in AJ:paquete.update(AJ[paquete['codigo']])
T14=(BASE/'formularios/T-14.tex').read_text(encoding='utf-8')
ids=re.findall(r'^(\d+\.\d+) &',T14,re.M)
assert len(P)==len(ids)==54 and set(ids)=={p['codigo'] for p in P}
assert len({p['codigo'].split('.')[0] for p in P})==13
N=HexColor('#102D3E'); T=HexColor('#007582'); A=HexColor('#9B5A00'); G=HexColor('#D7E2E7'); PALE=HexColor('#F0F4F6')
W,H=840,525
NAMES=['Gestión del proyecto','Levantamiento y diseño','Plataforma','Equipo a bordo','Servicios Etapa 1','Integraciones','Datos y migración','Servicios Etapa 2','Adhesión de transportistas','Calidad y pruebas','Implantación','Innovaciones','Operación']
STYLE=ParagraphStyle('p',fontName='Helvetica',fontSize=11.5,leading=13.5,textColor=N)
def para(c,s,x,top,w,bold=False,color=None):
 st=ParagraphStyle('x',parent=STYLE,textColor=color or N)
 q=Paragraph(('<b>'+escape(s)+'</b>') if bold else escape(s),st)
 _,h=q.wrap(w,1000);q.drawOn(c,x,top-h);return h
def page(slug,title,kicker,sub):
 c=canvas.Canvas(str(OUT/(slug+'.pdf')),pagesize=(W,H));c.setTitle(title);c.setAuthor('audIT Soluciones Tecnológicas SpA')
 c.setFillColor(T);c.setFont('Helvetica-Bold',12);c.drawString(34,496,kicker)
 c.setFillColor(N);c.setFont('Helvetica-Bold',23);c.drawString(34,458,title)
 para(c,sub,34,441,770)
 return c
def foot(c,n):
 c.setStrokeColor(G);c.line(34,47,806,47);para(c,n,34,40,770)
 c.setFillColor(N);c.setFont('Helvetica',11.5);c.drawRightString(806,12,'EDT · 02-11-2026');c.save()

# Árbol explícito de tres niveles; las conexiones representan pertenencia, no precedencia.
c=page('01-arbol','13 elementos · 54 paquetes','EDT / S7 §7.1 · T-14','La raíz contiene trece elementos de alcance; cada código de paquete aparece en las vistas siguientes.')
c.setFillColor(N);c.roundRect(286,355,268,46,7,fill=1,stroke=0)
para(c,'0  Plataforma de control de jornada, flota y viaje',300,389,240,True,white)
c.setStrokeColor(T);c.setLineWidth(1.2)
# Conexiones dibujadas una vez y antes de los nodos. La segunda fila
# deriva por el margen, sin atravesar ningún elemento de la primera.
c.line(420,355,420,340)
c.line(24,340,748,340)
c.line(24,340,24,225)
c.line(24,225,637,225)
for i in range(13):
 cx=82+(i%7)*111
 c.line(cx,340 if i<7 else 225,cx,333 if i<7 else 212)
for i,name in enumerate(NAMES):
 col=i%7;row=i//7;x=34+col*111;y=265-row*121
 c.setFillColor(PALE);c.setStrokeColor(G);c.roundRect(x,y,98,68,5,fill=1,stroke=1)
 c.setFillColor(T);c.setFont('Helvetica-Bold',12);c.drawString(x+7,y+51,f'{i+1:02d}')
 para(c,name,x+7,y+48,85,True)
 c.setFillColor(A);c.setFont('Helvetica-Bold',11.5);c.drawString(x+7,y+7,f"{sum(p['codigo'].startswith(str(i+1)+'.') for p in P)} paquetes")
foot(c,'Conexión = descomposición del alcance. La posición no representa fechas ni dependencias.')

PANELS=[([1,2],[3],'02-paquetes-1','Gestión, diseño y plataforma'),([4],[5],'03-paquetes-2','Equipo a bordo y servicios Etapa 1'),([6,7],[8],'04-paquetes-3','Integraciones, datos y Etapa 2'),([9,10],[11],'05-paquetes-4','Adhesión, calidad e implantación'),([12],[13],'06-paquetes-5','Innovaciones y operación')]
for left,right,slug,title in PANELS:
 c=page(slug,title,'EDT / DESCOMPOSICIÓN · T-14','Un nodo por paquete oficial. El código identifica su elemento padre; T-14 conserva entregable, aceptación y responsable.')
 for groups,x in ((left,34),(right,426)):
  y=390
  for g in groups:
   c.setFillColor(N);c.roundRect(x,y-24,374,25,3,fill=1,stroke=0)
   para(c,f'{g:02d}   {NAMES[g-1]}',x+8,y-4,350,True,white);y-=34
   for p in (p for p in P if p['codigo'].startswith(str(g)+'.')):
    c.setStrokeColor(G);c.line(x,y-21,x+374,y-21)
    c.setFillColor(T);c.setFont('Helvetica-Bold',11.5);c.drawString(x+5,y-12,p['codigo'])
    h=para(c,p['nombre'],x+42,y,325)
    y-=max(27,h+7)
   y-=9
  assert y>56,(slug,y)
 foot(c,'Los 54 códigos se muestran una vez en estas cinco láminas. Fuente: diccionario T-14.')

p=next(p for p in P if p['codigo']=='11.2')
c=page('07-ejemplo','Cómo se verifica un paquete','EDT / DICCIONARIO · EJEMPLO 11.2','La ficha conecta el paquete con su entregable, aceptación, responsable y ventana declarados en T-14.')
items=[('PAQUETE','11.2 · Marcha blanca y paso a producción, Etapa 1'),('ENTREGABLE',p['entregable']),('ACEPTACIÓN',p['aceptacion']),('RESPONSABLE',p['responsable']),('RED Y MESES',p['red_meses'])]
y=389
for label,value in items:
 c.setFillColor(PALE);c.roundRect(34,y-53,772,58,4,fill=1,stroke=0)
 c.setFillColor(T);c.setFont('Helvetica-Bold',11.5);c.drawString(48,y-15,label)
 para(c,value,187,y-9,602,True if label=='PAQUETE' else False)
 y-=66
foot(c,'Ejemplo del T-14. La evidencia y el procedimiento de prueba se consultan en T-17.')

c=page('08-trazabilidad','Cobertura y evidencia','EDT / TRAZABILIDAD · T-12 · T-14 · T-17','La codificación permite seguir alcance, paquete y entregable; la lámina siguiente presenta los 42 vínculos requisito--paquete.')
rows=[('42 requisitos T-12','Relación por código en T-14','Revisar requisito a requisito'),('6 contextos lógicos','5.1–5.6','5.7 es portal adicional'),('5 innovaciones','12.1–12.5','Ficha y métrica en T-19'),('Exigencias del Caso','Paquetes 2.2, 2.3, 7.1, 9.2, 11.1','Cotejar numeral 17.5')]
for i,(source,packages,note) in enumerate(rows):
 y=377-i*72;c.setFillColor(PALE if i%2==0 else white);c.rect(34,y-48,772,59,fill=1,stroke=0)
 para(c,source,45,y,220,True);para(c,packages,283,y,260);para(c,note,558,y,233)
foot(c,'Cobertura declarada: 13 elementos y 54 paquetes. Las asociaciones individuales requieren validación documental.')

t12=(ROOT/'recursos/Formato-Oferta-audIT/subdocumentos/03-solucion/formularios/T-12.tex').read_text(encoding='utf-8')
reqs=set(re.findall(r'\b(?:RF|RNF)-\d{3}\b',t12))
mapping={q:[p['codigo'] for p in P if q in re.findall(r'\b(?:RF|RNF)-\d{3}\b',p['requisitos'])] for q in sorted(reqs)}
assert len(reqs)==42 and all(mapping.values())
c=page('09-matriz-requisitos','42 requisitos con paquete','EDT / COBERTURA INDIVIDUAL · T-12 → T-14','Cada código de T-12 tiene al menos un paquete asignado; un paquete puede cubrir varios requisitos.')
for i,(req,codes) in enumerate(mapping.items()):
 col=i//21;row=i%21;x=34+col*393;y=390-row*15
 c.setFillColor(T);c.setFont('Helvetica-Bold',11.5);c.drawString(x,y,req)
 c.setFillColor(N);c.setFont('Helvetica',11.5);c.drawString(x+88,y,', '.join(codes))
foot(c,'Fuente: códigos T-12 y asociaciones del plan detallado D2; validar entregable y prueba en T-14/T-17.')
(OUT/'matriz-requisitos.json').write_text(json.dumps(mapping,ensure_ascii=False,indent=2),encoding='utf-8')

doc=fitz.open()
for f in sorted(f for f in OUT.glob('*.pdf') if f.name!='EDT_Completa_Revisada.pdf'):
 with fitz.open(f) as d:doc.insert_pdf(d)
doc.save(OUT/'EDT_Completa_Revisada.pdf',garbage=4,deflate=True)
print(json.dumps({'paginas':len(doc),'paquetes':len(P),'archivos':[f.name for f in sorted(OUT.glob('*.pdf'))]},ensure_ascii=False))
