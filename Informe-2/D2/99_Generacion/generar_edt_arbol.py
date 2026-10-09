from pathlib import Path
import json,html,textwrap
from xml.etree import ElementTree as E
P=Path(__file__).resolve().parent / "salida_temporal"
data=json.loads((P/'plan_detallado.json').read_text(encoding='utf-8'))['paquetes']
names=['Gestión del proyecto','Levantamiento y diseño','Plataforma','Equipo a bordo','Servicios de la Etapa 1','Integraciones','Datos y migración','Servicios de la Etapa 2','Adhesión de transportistas','Calidad y pruebas','Implantación','Innovaciones','Operación de 36 meses']
W=4940;H=2260;COL=375;M=35;BW=335;BH=238;STEP=265
svg=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}"><rect width="100%" height="100%" fill="#f6f8fb"/><text x="35" y="43" font-family="Arial" font-size="27" fill="#17324d" font-weight="bold">Estructura de Descomposición del Trabajo · Proyecto completo</text><text x="35" y="75" font-family="Arial" font-size="17" fill="#536779">Transportes Curimón · 13 áreas · 54 paquetes del T-14 oficial · Elaboración D2</text>']
mx=E.Element('mxfile',host='app.diagrams.net',type='device',version='25.0.3');d=E.SubElement(mx,'diagram',id='edt-completa',name='EDT completa · árbol de 54 paquetes');model=E.SubElement(d,'mxGraphModel',page='1',pageWidth=str(W),pageHeight=str(H),grid='1',gridSize='10');r=E.SubElement(model,'root');E.SubElement(r,'mxCell',id='0');E.SubElement(r,'mxCell',id='1',parent='0')
def box(cid,title,lines,x,y,w,h,dark=False):
 fill='#17324d' if dark else '#ffffff';color='#ffffff' if dark else '#17324d'
 label='<b>'+html.escape(title)+'</b><br><br>'+html.escape('\n'.join(lines)).replace('\n','<br>')
 c=E.SubElement(r,'mxCell',id=cid,value=label,vertex='1',parent='1',style=f'rounded=1;whiteSpace=wrap;html=1;fillColor={fill};strokeColor=#a7bccd;fontColor={color};fontSize=15;align=left;verticalAlign=top;spacing=15;')
 E.SubElement(c,'mxGeometry',x=str(x),y=str(y),width=str(w),height=str(h),attrib={'as':'geometry'})
 svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="9" fill="{fill}" stroke="#a7bccd"/>')
 yy=y+26
 for text,bold in [(t,True) for t in textwrap.wrap(title,int((w-30)/8.5))]+[(t,False) for line in lines for t in (textwrap.wrap(line,int((w-30)/7.8)) or [''])]:
  svg.append(f'<text x="{x+15}" y="{yy}" font-family="Arial" font-size="15" font-weight="{ "bold" if bold else "normal"}" fill="{color}">{html.escape(text)}</text>'); yy+=20
 assert yy-20<=y+h-10,(cid,yy,y+h)
def edge(cid,source,target,points):
 c=E.SubElement(r,'mxCell',id=cid,edge='1',parent='1',source=source,target=target,style='edgeStyle=orthogonalEdgeStyle;endArrow=none;rounded=0;strokeColor=#7e99ad;strokeWidth=2;exitX=0.5;exitY=1;entryX=0;entryY=0.5;')
 geo=E.SubElement(c,'mxGeometry',relative='1',attrib={'as':'geometry'})
 arr=E.SubElement(geo,'Array',attrib={'as':'points'})
 for x,y in points[1:-1]:E.SubElement(arr,'mxPoint',x=str(x),y=str(y))
 svg.append('<polyline points="'+' '.join(f'{x},{y}' for x,y in points)+'" fill="none" stroke="#7e99ad" stroke-width="2"/>')
rx=W/2-450
box('project','0 · Plataforma de control de jornada, flota y viaje',['Implementación de dos etapas y operación hasta el mes 56'],rx,105,900,85,True)
# Troncales del proyecto y cada área. Los paquetes son hermanos, nunca una secuencia de actividades.
svg.append(f'<path d="M{W/2},190 V220 H{M+(12*COL)+BW/2} M{W/2},220 H{M+BW/2}" fill="none" stroke="#7e99ad" stroke-width="2"/>')
for g,name in enumerate(names,1):
 x=M+(g-1)*COL;cx=x+BW/2
 box('a'+str(g),f'{g} · {name}',[],x,250,BW,85,True)
 c=E.SubElement(r,'mxCell',id='root-'+str(g),edge='1',parent='1',source='project',target='a'+str(g),style='edgeStyle=orthogonalEdgeStyle;endArrow=none;strokeColor=#7e99ad;strokeWidth=2;exitX=0.5;exitY=1;entryX=0.5;entryY=0;')
 ge=E.SubElement(c,'mxGeometry',relative='1',attrib={'as':'geometry'});ar=E.SubElement(ge,'Array',attrib={'as':'points'});E.SubElement(ar,'mxPoint',x=str(W/2),y='220');E.SubElement(ar,'mxPoint',x=str(cx),y='220')
 svg.append(f'<path d="M{cx},220 V250" fill="none" stroke="#7e99ad" stroke-width="2"/>')
 ps=[p for p in data if p['codigo'].startswith(str(g)+'.')]
 for j,p in enumerate(ps):
  y=375+j*STEP; windows=' / '.join(f'M{a}–M{b}' for a,b in p['ventanas'])
  # Un nodo por paquete, identificado con el código oficial. El diccionario conserva la aceptación extensa.
  lines=[p['entregable'],'', 'Responsable: '+p['responsable'],'Ventana: '+windows]
  box('p'+p['codigo'],p['codigo']+' · '+p['nombre'],lines,x,y,BW,BH)
  spine=x-14;points=[(cx,335),(cx,352),(spine,352),(spine,y+BH/2),(x,y+BH/2)]
  edge('e'+p['codigo'],'a'+str(g),'p'+p['codigo'],points)
svg.append(f'<text x="35" y="{H-55}" font-family="Arial" font-size="16" fill="#536779">Fuentes: T-14 oficial (alcance, aceptación y roles), T-18 (implantación), T-19 (innovaciones). Ventanas sujetas a las conciliaciones documentadas en la vista del proyecto.</text><text x="35" y="{H-25}" font-family="Arial" font-size="16" fill="#536779">Lectura: raíz → área de alcance → paquete de trabajo. La posición vertical de los paquetes no expresa una secuencia temporal.</text></svg>')
(P/'EDT_Proyecto_Completo.svg').write_text(''.join(svg),encoding='utf-8')
E.indent(mx);E.ElementTree(mx).write(P/'EDT_Completa.drawio',encoding='utf-8',xml_declaration=True)
view='''<!doctype html><html lang="es"><meta charset="utf-8"><title>EDT completa · Transportes Curimón</title><style>body{margin:0;background:#f6f8fb;font:16px Arial;color:#17324d}header{padding:20px 30px;background:#17324d;color:white;position:sticky;top:0;z-index:2}button,a{margin-right:12px;padding:9px 14px;border:0;border-radius:6px;cursor:pointer}a{color:white}main{overflow:auto;height:calc(100vh - 120px)}img{display:block;max-width:none}</style><header><b>EDT del proyecto completo · 54 paquetes en un único árbol</b><p><button onclick="document.querySelector('img').style.width='100%'">Ajustar al ancho</button><button onclick="document.querySelector('img').style.width='4940px'">Tamaño legible · desplazar</button><a href="EDT_Proyecto_Completo.svg">Abrir SVG</a><a href="EDT_D2.drawio">Editable diagrams.net</a></p></header><main><img src="EDT_Proyecto_Completo.svg" style="width:4940px" alt="Árbol completo de la EDT con 13 áreas y 54 paquetes"></main></html>'''
(P/'EDT_Proyecto_Completo.html').write_text(view,encoding='utf-8')
print('Árbol completo generado: 4940 × 2260, 13 áreas y 54 paquetes.')
