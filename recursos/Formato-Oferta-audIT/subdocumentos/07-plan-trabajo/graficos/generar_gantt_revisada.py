"""Anexo Gantt revisado: datos conciliados, frentes, hitos y operación."""
from pathlib import Path
import json, re, hashlib
import fitz
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, white
from reportlab.lib.utils import ImageReader
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from xml.sax.saxutils import escape
HERE=Path(__file__).resolve().parent
BASE=HERE.parent
ROOT=HERE.parents[4]
OUT=HERE/'revisada';OUT.mkdir(exist_ok=True)
SOURCE=ROOT/'Informe-2/d2/99_Generacion/plan_detallado.json'
D=json.loads(SOURCE.read_text(encoding='utf-8'))
P=D['paquetes'];R=D['red'];BY={r['id']:r for r in R}
N=HexColor('#102D3E');T=HexColor('#007582');RED=HexColor('#B3343C');A=HexColor('#9B5A00');G=HexColor('#D7E2E7');PALE=HexColor('#F0F4F6')
W,H=840,525
LOGO=ROOT/'recursos/Formato-Oferta-audIT/portadas/activos/logo-audit.png'
STYLE=ParagraphStyle('body',fontName='Helvetica',fontSize=12,leading=14,textColor=N)
def txt(c,s,x,y,w,bold=False):
 p=Paragraph(('<b>'+escape(s)+'</b>') if bold else escape(s),STYLE);_,h=p.wrap(w,1000);p.drawOn(c,x,y-h);return h
# Reconcile every numeric and precedence field against the current T-15.
t15=(BASE/'formularios/T-15.tex').read_text(encoding='utf-8')
fields=['duracion','inicio_temprano','fin_temprano','inicio_tardio','fin_tardio','holgura_total','holgura_libre']
checked=[]
for line in t15.splitlines():
 if not re.match(r'^(A\d{2}|G13) &',line):continue
 cells=[x.strip() for x in line.removesuffix('\\\\').split('&')]
 if len(cells)!=11:continue
 r=BY[cells[0]]
 assert [int(x) for x in cells[3:10]]==[int(r[f]) for f in fields],cells[0]
 assert cells[2].replace('$','')==r['predecesoras'],cells[0]
 assert cells[10]==r['critica'],cells[0]
 checked.append(cells[0])
assert len(checked)==26
# Independent generalized CPM calculation (FS relationships, including FS-10).
preds={r['id']:[(m.group(1),int(m.group(2) or 0)) for m in re.finditer(r'(A\d{2}|G13)(?: FS(-?\d+))?',r['predecesoras'])] for r in R}
es={};ef={};succ={r['id']:[] for r in R}
for r in R:
 id=r['id'];es[id]=max([ef[pr]+lag for pr,lag in preds[id]] or [0]);ef[id]=es[id]+int(r['duracion'])
 for pr,lag in preds[id]:succ[pr].append((id,lag))
ls={};lf={}
for r in reversed(R):
 id=r['id'];lf[id]=min([ls[ss]-lag for ss,lag in succ[id]] or [420]);ls[id]=lf[id]-int(r['duracion'])
for r in R:
 id=r['id'];hl=min([es[ss]-lag-ef[id] for ss,lag in succ[id]] or [420-ef[id]])
 assert [es[id],ef[id],ls[id],lf[id],ls[id]-es[id],hl]==[int(r[f]) for f in fields[1:]],id
ids=set(re.findall(r'^(\d+\.\d+) &',(BASE/'formularios/T-14.tex').read_text(encoding='utf-8'),re.M))
assert ids=={p['codigo'] for p in P} and len(ids)==54
months={x[0]:x[1] for x in D['hitos']}
econ=(ROOT/'recursos/Formato-Oferta-audIT/configuracion/economico.tex').read_text(encoding='utf-8')
assert {h:int(m) for h,m in re.findall(r'\\HitoPago\{(H\d+)\}\{\d+\}\{(\d+)\}',econ)}==months
# Fixed starts are exceptions to the end-of-month contractual deadlines.
HITS=[('H1','A02','Línea base de alcance',38,40),('H2','A05','Arquitectura, seguridad y datos',76,80),('H3','A07','Ambientes habilitados',112,120),('H4','A09','Etapa 1 para pruebas',192,200),('H5','A12','Certificación E1',226,240),('H6','A15','Inicio marcha blanca E1',240,240),('H8','A17','Línea base E2',276,280),('H7','A19','Producción E1',310,320),('H9','A20','Etapa 2 para pruebas',326,340),('H10','A22','Certificación E2',350,360),('H11','A24','Inicio marcha blanca E2',360,360),('H12','A25','Aceptación final E2',420,420)]
for h,task,_,day,limit in HITS:
 assert day==int(BY[task]['inicio_temprano' if h in ('H6','H11') else 'fin_temprano'])
 assert limit==((months[h]-1)*20 if h in ('H6','H11') else months[h]*20)
LABELS={'A01': 'Inicio del proyecto', 'A02': 'Levantamiento y línea base', 'A03': 'Cobertura móvil en terreno', 'A04': 'Factibilidad con terceros', 'A05': 'Arquitectura y datos', 'A06': 'Adhesión de transportistas', 'A07': 'Infraestructura y ambientes', 'A08': 'Migración de vigencias', 'A09': 'Construcción Etapa 1', 'A10': 'Integraciones', 'A11': 'Piloto a bordo', 'A12': 'Certificación Etapa 1', 'G13': 'Entrega G13 a capacitación', 'A13': 'Capacitación', 'A14': 'Reserva Etapa 1', 'A15': 'Marcha blanca E1', 'A16': 'Transferencia tecnológica', 'A17': 'Diseño Etapa 2', 'A18': 'Instalación progresiva', 'A19': 'Paso a producción E1', 'A20': 'Construcción Etapa 2', 'A21': 'Estabilización E1', 'A22': 'Certificación Etapa 2', 'A23': 'Reserva Etapa 2', 'A24': 'Marcha blanca E2', 'A25': 'Producción Etapa 2'}
manifest=[]
def new(slug,title,caption,subtitle):
 c=canvas.Canvas(str(OUT/(slug+'.pdf')),pagesize=(W,H));c.setTitle(title);c.setAuthor('audIT Soluciones Tecnológicas SpA')
 c.setFillColor(T);c.setFont('Helvetica-Bold',12);c.drawString(34,496,'PLANIFICACIÓN / S7 · T-14 · T-15 · T-18')
 c.drawImage(ImageReader(str(LOGO)),746,477,width=62,height=21,mask='auto',preserveAspectRatio=True)
 c.setFillColor(N);c.setFont('Helvetica-Bold',23);c.drawString(34,459,title)
 txt(c,subtitle,34,440,770)
 manifest.append(dict(file=slug+'.pdf',caption=caption,label='7-'+slug))
 return c

def finish(c,note):
 c.setStrokeColor(G);c.line(34,46,806,46);txt(c,note,34,39,772)
 c.setFillColor(N);c.setFont('Helvetica',12);c.drawRightString(806,12,f'v3 · 02-11-2026 · {len(manifest):02}')
 c.save()

def diamond(c,x,y,color=T,size=4):
 c.setFillColor(color);p=c.beginPath();p.moveTo(x,y+size);p.lineTo(x+size,y);p.lineTo(x,y-size);p.lineTo(x-size,y);p.close();c.drawPath(p,fill=1,stroke=0)

def axis(c,first,last,top=390,bottom=115):
 left,right=260,810;u=(right-left)/(last-first+1)
 for m in range(first,last+1):
  x=left+(m-first)*u
  if (m%12)+1 in (12,1,2,3,4):c.setFillColor(PALE);c.rect(x,bottom,u,top-bottom,stroke=0,fill=1)
  if (m-first)%(4 if last>24 else 2)==0:
   c.setStrokeColor(G);c.setLineWidth(.6);c.line(x,bottom,x,top);c.setFillColor(N);c.setFont('Helvetica',12);c.drawString(x+1,top+10,f'M{m}')
 c.setFillColor(N);c.drawRightString(right,top+27,f'Fin M{last}')
 return left,u

def rows_page(slug,title,rows,first=1,last=24,summary=False):
 c=new(slug,title,title,'Ventanas mensuales del T-14. M1 = febrero de 2027 (SA-01); cada mes ocupa su intervalo completo.')
 left,u=axis(c,first,last);step=270/len(rows)
 for i,p in enumerate(rows):
  y=380-(i+.5)*step
  c.setFillColor(T);c.setFont('Helvetica-Bold',12);c.drawString(35,y-4,p['codigo']);txt(c,p['nombre'],76,y+8,178)
  for j,(a,b) in enumerate(p['ventanas']):
   a=max(a,first);b=min(b,last)
   if a>b:continue
   if p['codigo'] in ('11.2','11.3') and j==1:
    h=next(x for x in HITS if x[0]==('H7' if p['codigo']=='11.2' else 'H12'))
    diamond(c,left+(h[3]/20-(first-1))*u,y,A)
   else:
    c.setFillColor(A if p['codigo'] in ('11.2','11.3') else T)
    c.roundRect(left+(a-first)*u,y-4,(b-a+1)*u,8,2,fill=1,stroke=0)
    if p['codigo'].startswith('12.'):
     c.setFillColor(N);c.setFont('Helvetica',12);c.drawCentredString(left+((a+b)/2-first+.5)*u,y+9,f'V{j+1}')
  if summary and p['codigo']=='11':
   for hh,tt,nn,dd,ll in HITS:
    if hh in ('H6','H7','H11','H12'):
     xx=left+(dd/20)*u;diamond(c,xx,y,A);c.setFillColor(N);c.setFont('Helvetica',12);c.drawCentredString(xx,y+9,hh)
  if not summary:
   tasks=set(re.findall(r'A\d{2}',p.get('red_meses','')))
   for h,task,name,day,limit in HITS:
    if task in tasks and p['codigo'] not in ('11.2','11.3'):
     x=left+(day/20-(first-1))*u
     if left<=x<=810:
      diamond(c,x,y,T,3);c.setFillColor(N);c.setFont('Helvetica',12);c.drawCentredString(x,y+9,h)
      xl=left+(limit/20-(first-1))*u
      c.setStrokeColor(A);c.setLineWidth(.8);c.line(xl,y-7,xl,y+7)
      if x!=xl:c.line(x,y,xl,y)
  if p['codigo'] in ('11.2','11.3'):
   c.setFillColor(A);c.setFont('Helvetica',12);c.drawString(left+(p['ventanas'][0][0]-first)*u,y+10,'Marcha blanca')
   stageh=next(v for v in HITS if v[0]==('H7' if p['codigo']=='11.2' else 'H12'))
   c.drawString(left+(stageh[3]/20-(first-1))*u-8,y-19,stageh[0])
   xl=left+(stageh[4]/20-(first-1))*u;c.setStrokeColor(A);c.line(xl,y-7,xl,y+7)
 txt(c,'Gris: temporada de fruta · Rombo: plan · Trazo ocre: límite · Barra ocre: marcha blanca · Turquesa: ventana EDT.',34,91,772)
 if any(p['codigo'].startswith('12.') for p in rows):
  finish(c,'V1, V2, V3 numeran ventanas previstas; los intervalos sin barra no acreditan una suspensión aprobada.')
 elif first==21:finish(c,'36 meses de operación, M21-M56. El inicio de M21 es el día 400; H12 se planifica al fin de M21, día 420.')
 else:finish(c,'Las barras agregan paquetes; las precedencias y holguras se consultan en la red CPM y T-15.')

# 1. Broad contract overview: aggregate windows of all 13 EDT elements.
groups=['Gestión del proyecto','Levantamiento y diseño','Plataforma','Equipo a bordo','Servicios E1','Integraciones','Datos y migración','Servicios E2','Adhesión de transportistas','Calidad y pruebas','Implantación','Innovaciones','Operación']
overview=[]
for i,name in enumerate(groups,1):
 mm=sorted({m for p in P if p['codigo'].split('.')[0]==str(i) for a,b in p['ventanas'] for m in range(a,b+1)});windows=[]
 for m in mm:
  if windows and windows[-1][1]+1==m:windows[-1][1]=m
  else:windows.append([m,m])
 overview.append(dict(codigo=str(i),nombre=name,ventanas=windows))
rows_page('gantt-panorama','Horizonte contractual M1-M56',overview,last=56,summary=True)
# 2. CPM with total float and selected precedence arrows.
c=new('gantt-cpm','Red CPM: ruta crítica y holguras','Red CPM de 25 actividades y G13','Línea base T-15 · 25 actividades + compuerta G13 · HT: holgura total en días hábiles.')
left,right=270,768;u=(right-left)/420;ys={r['id']:386-i*10.8 for i,r in enumerate(R)}
for m in range(1,22,2):
 x=left+(m-1)*20*u;c.setStrokeColor(G);c.line(x,102,x,400);c.setFillColor(N);c.setFont('Helvetica',12);c.drawString(x,407,f'M{m}')
c.setFont('Helvetica-Bold',12);c.drawString(787,407,'HT')
critical=[r for r in R if r['critica']=='Sí']
for prev,nxt in zip(critical,critical[1:]):
 x=left+int(prev['fin_temprano'])*u;y0=ys[prev['id']];y1=ys[nxt['id']]
 c.setStrokeColor(RED);c.setLineWidth(.6);c.line(x,y0,x,y1);c.line(x-2,y1+3,x,y1);c.line(x+2,y1+3,x,y1)
# FS-10 is an advance from the end of A09, not a normal finish-start arrow.
x0=left+192*u;x1=left+182*u;y=ys['G13']
c.setStrokeColor(T);c.setDash(2,2);c.line(x0,ys['A09'],x0,y);c.line(x0,y,x1,y);c.setDash();c.line(x1+3,y+2,x1,y);c.line(x1+3,y-2,x1,y)
xg=left+182*u;c.setStrokeColor(T);c.line(xg,ys['G13'],xg,ys['A13']);c.line(xg-2,ys['A13']+3,xg,ys['A13']);c.line(xg+2,ys['A13']+3,xg,ys['A13'])
for r in R:
 id=r['id'];y=ys[id];color=RED if r['critica']=='Sí' else T
 c.setFillColor(color);c.setFont('Helvetica-Bold' if r['critica']=='Sí' else 'Helvetica',12);c.drawString(34,y-3,id)
 c.setFillColor(N);c.setFont('Helvetica',12);c.drawString(72,y-3,LABELS[id]);c.drawRightString(812,y-3,r['holgura_total'])
 x=left+int(r['inicio_temprano'])*u;w=int(r['duracion'])*u
 if id=='G13':diamond(c,x,y,T)
 elif id in ('A14','A23'):
  c.setStrokeColor(RED);c.setFillColor(white);c.setDash(2,2);c.roundRect(x,y-3.3,w,6.6,2,fill=1,stroke=1);c.setDash()
 else:c.setFillColor(color);c.roundRect(x,y-3.3,w,6.6,2,fill=1,stroke=0)
for day,h in [(240,'H6 / M13'),(360,'H11 / M19')]:
 x=left+day*u;c.setStrokeColor(A);c.setDash(3,3);c.line(x,102,x,400);c.setDash();c.setFillColor(A);c.setFont('Helvetica',12);c.drawCentredString(x,83,h)
finish(c,'Rojo: ruta crítica y enlaces críticos · Turquesa: no crítica · Reserva: discontinua · FS-10: adelanto G13/A13. Fin M21 = día 420. Resto de precedencias: PERT y T-15.')
# 3-9. Seven fronts preserve all 50 non-operation packages, exactly once.
fronts=[('gantt-gestion','Gestión y levantamiento',{'1','2'}),('gantt-plataforma','Plataforma y equipo a bordo',{'3','4'}),('gantt-e1','Construcción de la Etapa 1',{'5'}),('gantt-datos','Integraciones y migración',{'6','7'}),('gantt-e2','Etapa 2 y adhesión',{'8','9'}),('gantt-implantacion','Calidad, capacitación e implantación',{'10','11'}),('gantt-innovaciones','Ventanas de las innovaciones',{'12'})]
covered=[]
for slug,title,areas in fronts:
 rows=[p for p in P if p['codigo'].split('.')[0] in areas];covered.extend(p['codigo'] for p in rows);rows_page(slug,title,rows)
# 10. All milestones with explicit meanings.
c=new('gantt-hitos','Hitos: planificación y compromiso','Fechas planificadas y límites de H1-H12','Días hábiles desde el inicio. Rombo = posición planificada; límite = fecha contractual, con H6/H11 como inicios fijos.')
headers=[('Hito',34),('Nombre',78),('Actividad',345),('Plan',435),('Límite',500),('Mes',565),('Margen',680)]
for text,x in headers:c.setFillColor(T);c.setFont('Helvetica-Bold',12);c.drawString(x,391,text)
for i,(h,task,name,day,limit) in enumerate(HITS):
 y=366-i*23
 if i%2==0:c.setFillColor(PALE);c.rect(30,y-6,780,22,fill=1,stroke=0)
 values=[h,name,task,str(day),str(limit),('Inicio ' if h in ('H6','H11') else 'Fin ')+f'M{months[h]}', 'Fijo' if h in ('H6','H11') else str(limit-day)+' d']
 for value,(_,x) in zip(values,headers):c.setFillColor(N);c.setFont('Helvetica',12);c.drawString(x,y,value)
txt(c,'El margen del hito es límite menos fecha planificada; no equivale a la HT de la actividad. H12 tiene margen cero en la línea base con A23 incluida.',34,77,770)
finish(c,'Fuente: tabla de hitos de S7, malla T-15 y catálogo económico del proyecto basado en E-25. H6 y H11 se fijan al inicio del mes.')
# 11. Distinguish gates, fixed dates, and reserves.
c=new('gantt-control','Compuertas y reservas del cronograma','G13, reservas y control de fechas','El calendario por sí solo no acredita la disponibilidad de G13 ni el cumplimiento de una aceptación.')
blocks=[('G13 habilita A13','Día 182: entrega probada y congelada en PREPROD, datos ficticios y material por perfil. A13 conserva 40 días: 10 de familiarización y 30 de práctica/evaluación. El adelanto A09 FS-10 exige disponibilidad real de G13.'),('A14 protege el inicio de E1','Reserva explícita: 14 días, del 226 al 240. H6 fija el inicio de marcha blanca al día 240, comienzo de M13. Consumir la reserva exige registrar el cambio; no desplaza esa fecha fija.'),('A23 protege el inicio de E2','Reserva explícita: 10 días, del 350 al 360. H11 fija el inicio de marcha blanca al día 360, comienzo de M19. La reserva forma parte de la línea base CPM.'),('Holgura, margen y probabilidad','La HT mide flexibilidad de una actividad en la red; el margen de un hito se mide contra su límite contractual. La probabilidad de cumplir un límite se analiza en S8 y no se deduce del color o la longitud de una barra.')]
for i,(title,body) in enumerate(blocks):
 y=394-i*75;txt(c,title,34,y,770,True);txt(c,body,34,y-20,770)
finish(c,'Fuente: S7, T-15 y T-18. Reservas e hitos se muestran en la línea base; esta lámina no introduce un escenario de atraso.')
# 12. Operation, without duplicating 50 implementation packages.
ops=[p for p in P if p['codigo'].startswith('13.')];covered.extend(p['codigo'] for p in ops)
assert len(covered)==54 and set(covered)==ids
rows_page('gantt-operacion','Continuidad operacional M21-M56',ops,first=21,last=56)
# Output and traceability.
combined=fitz.open()
for entry in manifest:
 doc=fitz.open(OUT/entry['file']);combined.insert_pdf(doc)
combined.save(HERE/'Gantt_Completa_Revisada.pdf')
(OUT/'manifiesto.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
# Only replace the controlled Gantt block. Keep all other S7 content and labels intact.
content=BASE/'contenido.tex';s=content.read_text(encoding='utf-8')
intro=r'''La planificación se lee desde el horizonte contractual hasta el control de la implementación. La \figref{7-gantt-panorama} muestra las ventanas agregadas de los trece elementos de la EDT en M1-M56. La \figref{7-gantt-cpm} presenta las 25 actividades y G13 en días hábiles, con ruta crítica, holgura total y enlaces principales; las precedencias completas se consultan en T-15 y en los PERT de la \verSeccion{sec:7-ruta}.

Los detalles se agrupan por frentes y cubren los 54 paquetes una sola vez, incluyendo los cuatro de operación. Las barras representan ventanas mensuales del T-14; los rombos muestran posiciones planificadas de hitos relacionados con la red. La tabla de hitos distingue estas posiciones de los límites contractuales y de los inicios fijos H6/H11. La probabilidad de cumplir plazos se analiza por separado en S8.

'''
start=s.index('\\subsection{Carta Gantt}')
a=s.index('\n\n',start)+2;b=s.index('% INICIO LAMINAS GANTT',a)
s=s[:a]+intro+s[b:]
refs='Las vistas del anexo se presentan en '+', '.join('\\figref{'+e['label']+'}' for e in manifest)+'.\n\n'
annex='\n'.join('\\anexoGrafico{subdocumentos/07-plan-trabajo/graficos/revisada/'+e['file']+'}{'+e['caption']+'}{'+e['label']+'}' for e in manifest)
block='% INICIO LAMINAS GANTT\n'+refs+annex+'\n% FIN LAMINAS GANTT'
s=re.sub(r'% INICIO LAMINAS GANTT.*?% FIN LAMINAS GANTT',lambda _:block,s,flags=re.S);content.write_text(s,encoding='utf-8')
fontfile=HERE/'verificacion_letra.json';f=json.loads(fontfile.read_text(encoding='utf-8'));f=[x for x in f if not x['archivo'].startswith('revisada/')]
f.extend({'archivo':'revisada/'+e['file'],'minimo_pt':12.0} for e in manifest);fontfile.write_text(json.dumps(f,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
report={'CPM_recalculada_y_coincidente':True,'actividades_conciliadas_T15':len(checked),'paquetes_conciliados_T14':len(ids),'paquetes_cubiertos_sin_duplicar':len(covered),'hitos_conciliados_catalogo':len(HITS),'paginas':len(manifest),'fuente_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),'integracion':'Ver revisada/verificacion-integracion.json; recompilar si se regeneran las figuras.','pendientes':['Cotejo directo de tabla E-25: extracción textual vacía.','Revisión humana y asociación a bitácora A-6 del responsable.']}
(OUT/'conciliacion.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,ensure_ascii=True))
