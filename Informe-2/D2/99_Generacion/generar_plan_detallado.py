from pathlib import Path
import re,json,csv,html,textwrap,calendar
from datetime import date
from xml.etree import ElementTree as E
ROOT=Path(__file__).resolve().parents[3]
OUT=Path(__file__).resolve().parent / "salida_temporal"
OUT.mkdir(parents=True,exist_ok=True)
BASE=ROOT/'recursos/Formato-Oferta-audIT/subdocumentos'
def clean(s):
 s=s.replace(r'\%', '%').replace(r'\midrule','').replace('\\\\','').strip()
 return s
rows=[]
for line in (BASE/'07-plan-trabajo/formularios/T-14.tex').read_text(encoding='utf-8').splitlines():
 if re.match(r'^\d+\.\d+ &',line):
  v=[clean(x) for x in line.split('&')]
  rows.append(dict(zip(['codigo','entregable','aceptacion','responsable','red_meses'],v)))
groups=['Gestión del proyecto','Levantamiento y diseño','Plataforma','Equipo a bordo','Servicios de la Etapa 1','Integraciones','Datos y migración','Servicios de la Etapa 2','Adhesión de transportistas','Calidad y pruebas','Implantación','Innovaciones','Operación de 36 meses']
short={}
s=(BASE/'07-plan-trabajo/contenido.tex').read_text(encoding='utf-8')
for code,name in re.findall(r'\{(\d+\.\d+) ([^{}]+)\};',s): short.setdefault(code,name)
inn=(BASE/'13-innovaciones/formularios/T-19.tex').read_text(encoding='utf-8')
for i,n in enumerate(re.findall(r'  nombre = \{([^\n]+)\},',inn),1): short[f'12.{i}']=n
for p in rows:p['nombre']=short.get(p['codigo'],p['entregable'])
network=[]
for line in (BASE/'07-plan-trabajo/formularios/T-15.tex').read_text(encoding='utf-8').splitlines():
 if re.match(r'^A\d\d &',line):
  v=[clean(x) for x in line.split('&')]
  if len(v)==11:
   network.append(dict(zip(['id','actividad','predecesoras','duracion','inicio_temprano','fin_temprano','inicio_tardio','fin_tardio','holgura_total','holgura_libre','critica'],v[:11])))
requirements=[]
reqtext=(BASE/'03-solucion/formularios/T-12.md').read_text(encoding='utf-8')
for match in re.finditer(r'### ((?:RF|RNF)-\d+)\n(.*?)(?=\n### |\n## |\Z)',reqtext,re.S):
 block=match.group(2); desc=re.search(r'\| Descripción \| (.*?) \|',block); trace=re.search(r'\| Componente y trazabilidad \| (.*?) \|',block)
 codes=re.findall(r'EDT (\d+\.\d+)',trace.group(1) if trace else '')
 requirements.append({'requisito':match.group(1),'descripcion':desc.group(1) if desc else '', 'paquetes':', '.join(codes),'trazabilidad':trace.group(1) if trace else ''})
for p in rows:p['requisitos']=', '.join(q['requisito'] for q in requirements if p['codigo'] in q['paquetes'].split(', '))
# Ventanas mensuales del T-14. Segmentos distintos conservan un único paquete EDT.
spans={
'1.1':[(1,21)],'1.2':[(1,21)],'1.3':[(1,5)],'2.1':[(1,2)],'2.2':[(1,3)],'2.3':[(1,4)],'2.4':[(2,4)],'2.5':[(4,6)],
'3.1':[(4,6)],'3.2':[(4,12)],'3.3':[(4,6)],'3.4':[(4,12)],'4.1':[(4,9)],'4.2':[(6,10),(16,18)],'4.3':[(6,10),(13,15)],
'6.5':[(6,9),(16,24)],'7.1':[(6,9)],'7.2':[(6,12),(19,24)],'7.3':[(4,10)],'9.1':[(2,3)],'9.2':[(2,21)],'9.3':[(2,21)],
'10.1':[(6,10),(15,17)],'10.2':[(10,12),(17,18)],'10.3':[(10,12),(17,18)],'11.1':[(10,12)],'11.2':[(13,15),(16,16)],'11.3':[(19,20),(21,21)],'11.4':[(13,15),(16,17)],
'12.1':[(4,4),(8,10),(13,15)],'12.2':[(4,4),(5,8)],'12.3':[(4,9),(13,15)],'12.4':[(2,3),(6,10),(13,21)],'12.5':[(3,6),(7,10),(13,15)]}
for p in rows:
 c=p['codigo'];g=int(c.split('.')[0])
 if g==5:spans[c]=[(6,10)]
 if g==6 and c not in spans:spans[c]=[(6,9)]
 if g==8:spans[c]=[(13,18)]
 if g==13:spans[c]=[(21,56)]
 p['ventanas']=spans[c]
 p['origen_ventana']='T-19' if g==12 else ('Propuesta mensual derivada de T-15' if g==10 else 'T-14 / T-18')
hits=[('H1',2,'Línea base de alcance'),('H2',4,'Arquitectura, seguridad y datos'),('H3',6,'Ambientes habilitados'),('H4',10,'Etapa 1 para pruebas'),('H5',12,'Certificación Etapa 1'),('H6',13,'Inicio marcha blanca Etapa 1'),('H7',16,'Producción Etapa 1'),('H8',14,'Línea base Etapa 2'),('H9',17,'Etapa 2 para pruebas'),('H10',18,'Certificación Etapa 2'),('H11',19,'Inicio marcha blanca Etapa 2'),('H12',21,'Producción E2 / aceptación final')]
# XML nativo diagrams.net: una vista completa y una lámina por área con diccionario visible.
mx=E.Element('mxfile',host='app.diagrams.net',type='device',version='25.0.3')
NAVY='#17324d';TEAL='#0f766e'
def page(name,w,h):
 d=E.SubElement(mx,'diagram',id='p'+str(len(mx)),name=name);m=E.SubElement(d,'mxGraphModel',page='1',pageWidth=str(w),pageHeight=str(h),grid='1',gridSize='10');r=E.SubElement(m,'root');E.SubElement(r,'mxCell',id='0');E.SubElement(r,'mxCell',id='1',parent='0');return r
svgs=[]
def svgstart(w,h,title,subtitle):
 return [f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}"><rect width="100%" height="100%" fill="#f5f7fa"/>',f'<text x="35" y="45" font-family="Arial" font-size="25" font-weight="bold" fill="{NAVY}">{html.escape(title)}</text>',f'<text x="35" y="73" font-family="Arial" font-size="13" fill="#576b7d">{html.escape(subtitle)}</text>']
def card(r,svg,cid,title,body,x,y,w,h,dark=False):
 fill=NAVY if dark else '#ffffff';font='#ffffff' if dark else NAVY
 val=html.escape(title)+'<br><br>'+html.escape(body).replace('\n','<br>')
 cell=E.SubElement(r,'mxCell',id=cid,value=val,parent='1',vertex='1',style=f'rounded=1;whiteSpace=wrap;html=1;fillColor={fill};strokeColor=#b9cbd7;fontColor={font};fontSize=13;align=left;spacing=14;')
 E.SubElement(cell,'mxGeometry',x=str(x),y=str(y),width=str(w),height=str(h),attrib={'as':'geometry'})
 svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{fill}" stroke="#b9cbd7"/>')
 yy=y+26
 for txt,bold in [(t,True) for t in textwrap.wrap(title,max(20,int(w/8)))]+[(t,False) for para in body.split('\n') for t in (textwrap.wrap(para,max(20,int(w/7.2))) or [''])]:
  svg.append(f'<text x="{x+16}" y="{yy}" font-family="Arial" font-size="13" fill="{font}" font-weight="{ "bold" if bold else "normal"}">{html.escape(txt)}</text>');yy+=19
r=page('00 · EDT completa',1900,1450);svg=svgstart(1900,1450,'EDT · Proyecto completo Transportes Curimón','13 áreas · 54 paquetes oficiales · Códigos del T-14 · Detalle de aceptación y responsable en las láminas siguientes')
card(r,svg,'root','0 · Plataforma de control de jornada, flota y viaje','Implementación de dos etapas y operación hasta el mes 56',580,100,740,82,True)
for g,n in enumerate(groups,1):
 ps=[p for p in rows if p['codigo'].startswith(str(g)+'.')];col=(g-1)%4;rr=(g-1)//4;x=35+col*465;y=230+rr*280
 card(r,svg,'g'+str(g),f'{g} · {n}','\n'.join(p['codigo']+' '+p['nombre'] for p in ps),x,y,440,255)
 edge=E.SubElement(r,'mxCell',id='edge'+str(g),parent='1',edge='1',source='root',target='g'+str(g),style='edgeStyle=orthogonalEdgeStyle;endArrow=none;strokeColor=#b9cbd7;');E.SubElement(edge,'mxGeometry',relative='1',attrib={'as':'geometry'})
svg.append('</svg>');svgs.append(('EDT_00_completa.svg',''.join(svg)))
for g,n in enumerate(groups,1):
 ps=[p for p in rows if p['codigo'].startswith(str(g)+'.')];h=190+((len(ps)+2)//3)*350;r=page(f'{g:02} · {n}',1560,h);svg=svgstart(1560,h,f'EDT {g} · {n}','Paquetes oficiales · Entregable, aceptación, rol responsable y ventana contractual')
 for j,p in enumerate(ps):
  x=35+(j%3)*510;y=110+(j//3)*350
  months=' / '.join(f'M{a}–M{b}' for a,b in p['ventanas'])
  body=f"Entregable: {p['entregable']}\n\nAceptación: {p['aceptacion']}\n\nResponsable: {p['responsable']}\nVentana: {months}\nRed: {p['red_meses']}\nRequisitos: {p['requisitos'] or 'Alcance transversal / T-14 / T-19'}"
  card(r,svg,'p'+p['codigo'],p['codigo']+' · '+p['nombre'],body,x,y,490,330)
 svg.append('</svg>');svgs.append((f'EDT_{g:02}_detalle.svg',''.join(svg)))
E.indent(mx);E.ElementTree(mx).write(OUT/'EDT_Seccionada.drawio',encoding='utf-8',xml_declaration=True)
for name,svg in svgs:(OUT/name).write_text(svg,encoding='utf-8')
# Gantt visual con eje contractual; cada fila usa un paquete, no repite alcance.
def gantt(maxmonth,filename):
 relevant=[p for p in rows if min(a for a,b in p['ventanas'])<=maxmonth]
 left=570;unit=50 if maxmonth<=24 else 27;w=left+unit*maxmonth+50;h=150+len(relevant)*36+13*34+12*29+95
 svg=svgstart(w,h,f'Carta Gantt detallada · M1–M{maxmonth}','Eje relativo contractual · Segmentos por paquete · Ventanas de T-14/T-18/T-19 · Meses de pruebas derivados de T-15')
 for m in range(1,maxmonth+1):
  x=left+(m-1)*unit;svg.append(f'<line x1="{x}" y1="115" x2="{x}" y2="{h-50}" stroke="#dce4eb"/><text x="{x+unit/2}" y="105" text-anchor="middle" font-family="Arial" font-size="11" fill="{NAVY}">M{m}</text>')
 y=128
 for g,n in enumerate(groups,1):
  ps=[p for p in relevant if p['codigo'].startswith(str(g)+'.')]
  if not ps:continue
  svg.append(f'<rect x="25" y="{y-16}" width="{w-50}" height="29" rx="4" fill="{NAVY}"/><text x="35" y="{y+4}" font-family="Arial" font-size="14" font-weight="bold" fill="white">{g} · {html.escape(n)}</text>');y+=34
  for p in ps:
   svg.append(f'<text x="35" y="{y+5}" font-family="Arial" font-size="13" fill="{NAVY}">{html.escape(p["codigo"]+" · "+p["nombre"])}</text>')
   for a,b in p['ventanas']:
    if a>maxmonth:continue
    b=min(b,maxmonth);x=left+(a-1)*unit;wid=(b-a+1)*unit-4;color=TEAL if g not in (10,11,12,13) else {10:'#6579a5',11:'#b26d20',12:'#8464a6',13:'#336e94'}[g]
    svg.append(f'<rect x="{x+2}" y="{y-13}" width="{wid}" height="25" rx="4" fill="{color}"><title>{html.escape(p["entregable"]+" · "+p["origen_ventana"])}</title></rect>')
   y+=36
 svg.append(f'<text x="35" y="{y+6}" font-family="Arial" font-size="16" font-weight="bold" fill="{NAVY}">Hitos contractuales · E-25</text>');y+=32
 for code,m,label in sorted(hits,key=lambda t:t[1]):
  x=left+(m-.5)*unit;svg.append(f'<text x="35" y="{y+4}" font-family="Arial" font-size="13" fill="{NAVY}">{code} · {html.escape(label)} · M{m}</text><path d="M{x},{y-8} l8,8 l-8,8 l-8,-8 Z" fill="#bd5439"/>');y+=29
 svg.append(f'<text x="35" y="{y+30}" font-family="Arial" font-size="12" fill="#576b7d">Ventanas mensuales; la malla CPM y sus días hábiles se consultan por separado. Revisar discrepancias del T-19 antes de aprobar.</text></svg>')
 (OUT/filename).write_text(''.join(svg),encoding='utf-8')
gantt(56,'Gantt_D2_56_meses.svg');gantt(24,'Gantt_D2_implementacion.svg')
def cal(m):
 n=2027*12+1+m-1;return f'{n//12:04}-{n%12+1:02}-01'
def mermaid(maxmonth,fn):
 lines=['%%{init: {"theme":"base","gantt":{"leftPadding":420,"barHeight":22,"barGap":7,"fontSize":13}}}%%','gantt',f'    title Proyecto completo · M1–M{maxmonth} · Calendario provisional M1 febrero 2027','    dateFormat YYYY-MM-DD','    axisFormat %b %Y','    tickInterval 1month' if maxmonth<=24 else '    tickInterval 3month','    todayMarker off']
 for g,n in enumerate(groups,1):
  ps=[p for p in rows if int(p['codigo'].split('.')[0])==g and min(a for a,b in p['ventanas'])<=maxmonth]
  if not ps:continue
  lines.append('    section '+str(g)+' '+n)
  for p in ps:
   for j,(a,b) in enumerate(p['ventanas']):
    if a>maxmonth:continue
    b=min(b,maxmonth);label=p['codigo']+' '+p['nombre']+f' [M{a}–M{b}]'
    lines.append(f'    {label.replace(":"," ")} :p{p["codigo"].replace(".","_")}_{j}, {cal(a)}, {cal(b+1)}')
 lines.append('    section Hitos E-25')
 for code,m,label in sorted(hits,key=lambda t:t[1]):lines.append(f'    {code} {label} M{m} :milestone, {code.lower()}, {cal(m)}, 0d')
 lines+=['    %% Ancla calendario provisional; el compromiso es en meses contractuales.','    %% Fuentes oficiales locales: T-14, T-15, T-18 y T-19.','    %% Los segmentos de pruebas son propuesta mensual; validar fechas de innovaciones e IDs EDT.']
 (OUT/fn).write_text('\n'.join(lines)+'\n',encoding='utf-8')
mermaid(56,'Gantt_D2.mmd');mermaid(24,'Gantt_Implementacion_D2.mmd')
with (OUT/'Diccionario_EDT_D2.csv').open('w',newline='',encoding='utf-8-sig') as f:
 w=csv.DictWriter(f,fieldnames=['codigo','nombre','entregable','aceptacion','responsable','red_meses','origen_ventana','requisitos']);w.writeheader();w.writerows({k:p[k] for k in w.fieldnames} for p in rows)
with (OUT/'Red_actividades_T15.csv').open('w',newline='',encoding='utf-8-sig') as f:
 w=csv.DictWriter(f,fieldnames=list(network[0]));w.writeheader();w.writerows(network)
(OUT/'plan_detallado.json').write_text(json.dumps({'paquetes':rows,'red':network,'hitos':hits},ensure_ascii=False,indent=2),encoding='utf-8')
# Documento visual autónomo, se abre sin cuenta ni conexión.
def table(items,keys):return '<table><thead><tr>'+''.join('<th>'+html.escape(k.replace('_',' ').title())+'</th>' for k in keys)+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+html.escape(str(p[k]))+'</td>' for k in keys)+'</tr>' for p in items)+'</tbody></table>'
notes=['T-19 innovación 2 fija piloto en M4 y montaje propio al cierre de M8; T-14/T-15 habilitan plataforma en M6 y montaje entre M6–M10. Conciliar prerrequisitos y fecha final antes de aprobar la línea base.','T-19 innovaciones 2, 3 y 5 cita códigos 4.5, 4.4, 3.7 y 4.6 que no existen en el T-14 oficial. La EDT conserva los 54 códigos del T-14 y muestra las cinco innovaciones por su nombre vigente.','T-14 sitúa firmware en M4–M9 y pruebas de 72 horas, mientras T-12 contempla escenarios de cierre de hasta 288 horas. Conciliar el criterio de aceptación; se preserva el texto oficial en el diccionario.','La instalación física A18 del T-15 ocupa M13–M18, incluyendo la ventana diciembre–abril del calendario asumido. T-18 divide montaje en M6–M10 y M16–M18. La Gantt usa la separación del T-18 y no declara resuelta esta incompatibilidad.','El inicio febrero de 2027 es un supuesto de los documentos oficiales. Los SVG usan M1–M56 para evitar confundir el calendario supuesto con una fecha de acta confirmada.','Los 25 registros CPM se transcriben del T-15 con su escala convencional de 20 días hábiles/mes. Sus holguras no se aplican automáticamente a los 54 paquetes ni se recalculan como fechas calendario.','Los paquetes 10.1–10.3 se muestran en ventanas mensuales derivadas de la red T-15; requieren validación del responsable de calidad.','El T-14 no presenta un paquete independiente de cierre al mes 56. Confirmar alcance de transferencia final y cierre contractual antes de afirmar cobertura completa de esos entregables.']
body='''<!doctype html><html lang="es"><meta charset="utf-8"><title>EDT y Gantt · Proyecto completo</title><style>body{margin:0;background:#f1f4f7;color:#17324d;font:15px Arial}header{padding:32px 40px;background:#17324d;color:white}main{max-width:1500px;margin:auto;padding:28px}h1{margin:0 0 12px}h2{margin-top:36px}nav{display:flex;gap:18px;flex-wrap:wrap;padding:18px;background:white;position:sticky;top:0}a{color:#0f766e}.view{overflow:auto;border:1px solid #ccd8e0;border-radius:12px;background:white;margin:18px 0}img{display:block;max-width:none}.overview img{width:100%;max-width:1900px}details{background:white;padding:18px;border-radius:8px;margin:12px 0}summary{font-weight:bold;cursor:pointer}table{border-collapse:collapse;width:100%;font-size:13px}th,td{border:1px solid #d7e0e7;padding:10px;text-align:left;vertical-align:top}th{background:#e8eff4}.note{background:#fff3df;padding:20px;border-radius:10px;line-height:1.6}p{line-height:1.6}@media print{nav{display:none}header{background:white;color:#17324d}.view{overflow:visible}img{width:100%!important}details{break-inside:avoid}details> *{display:block}table{font-size:9px}}</style><header><h1>EDT y Carta Gantt</h1><p>Proyecto completo · Transportes Curimón · 13 áreas · 54 paquetes · 25 actividades de la red oficial · 56 meses</p></header><nav><a href="#edt">EDT completa</a><a href="#detalle">Detalle por área</a><a href="#gantt">Gantt de implementación</a><a href="#operacion">Gantt 56 meses</a><a href="#red">Precedencias y holguras</a><a href="#revision">Puntos de revisión</a></nav><main>'''
body+='<p>Versión detallada basada en los formularios oficiales del repositorio. La EDT representa entregables; la Gantt muestra sus ventanas mensuales y la tabla de red conserva el secuenciamiento del T-15. Preparación D2 · propuesta pendiente de conciliación de las discrepancias señaladas al final.</p><h2 id="edt">EDT del proyecto completo</h2><div class="view overview"><img src="EDT_00_completa.svg" alt="EDT completa"></div><h2 id="detalle">Diccionario visual por área</h2>'
for g,n in enumerate(groups,1):body+=f'<details open><summary>{g} · {html.escape(n)}</summary><div class="view"><img src="EDT_{g:02}_detalle.svg" alt="Detalle EDT {g}" style="width:100%;max-width:1560px"></div></details>'
body+='<h2>Trazabilidad del alcance funcional y transversal</h2><p>Requisitos del T-12 oficial con su descripción y referencia a paquetes. Una ausencia de código explícito debe revisarse con la contraparte.</p><div class="view">'+table(requirements,['requisito','descripcion','paquetes'])+'</div><h2 id="gantt">Implementación y retiro del legado · M1–M24</h2><p>Desplaza horizontalmente para consultar cada mes. Las actividades de migración y retiro continúan hasta M24, en convivencia con la operación desde M21.</p><div class="view"><img src="Gantt_D2_implementacion.svg" alt="Gantt implementación"></div><h2 id="operacion">Horizonte completo · M1–M56</h2><div class="view"><img src="Gantt_D2_56_meses.svg" alt="Gantt completo"></div><h2 id="red">Red oficial de actividades · T-15</h2><p>Predecesoras y duraciones en días hábiles según el T-15. La condición crítica pertenece a esta red agregada; no se atribuye a cada paquete. Los meses contractuales de E-25 prevalecen para los compromisos.</p><div class="view">'+table(network,list(network[0]))+'</div><h2 id="revision">Conciliaciones necesarias para aprobar</h2><div class="note"><ul>'+''.join('<li>'+html.escape(n)+'</li>' for n in notes)+'</ul></div><h2>Fuentes y archivos editables</h2><p>Formulario T-14 (54 paquetes), T-15 (red A01–A25), T-18 (implantación) y T-19 (cinco innovaciones), en recursos/Formato-Oferta-audIT/subdocumentos. Fechas contractuales: FEP01 · Artículos 17.1–17.3 · pp.12–13; Formulario E-25 · p.74. Restricciones: FEP03 · numeral 17.5 · p.40.</p><p><a href="EDT_D2.drawio">Fuente diagrams.net</a> · <a href="Gantt_D2.mmd">Fuente Mermaid completa</a> · <a href="Gantt_Implementacion_D2.mmd">Fuente Mermaid implementación</a> · <a href="Diccionario_EDT_D2.csv">Diccionario CSV</a> · <a href="Red_actividades_T15.csv">Red CSV</a></p></main></html>'
(OUT/'EDT_Gantt_Proyecto_Completo.html').write_text(body,encoding='utf-8')
print(f'Generado: {len(rows)} paquetes, {len(network)} actividades de red, {len(svgs)} láminas EDT y 2 Gantt SVG.')

