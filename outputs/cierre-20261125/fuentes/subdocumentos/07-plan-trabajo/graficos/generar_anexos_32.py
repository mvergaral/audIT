"""Dibuja anexos activos desde la conciliación mensual y la red calculada."""
from pathlib import Path
import json,re
import fitz
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor,white
from xml.sax.saxutils import escape

HERE=Path(__file__).resolve().parent; BASE=HERE.parent
OUT=HERE/'revisada';OUT.mkdir(exist_ok=True)
D=json.loads((HERE/'conciliacion-3.2/puente.json').read_text(encoding='utf-8'))
P=list(D['paquetes'].values());R=json.loads((HERE/'conciliacion-3.2/red-calculada.json').read_text(encoding='utf-8'))
FONT=Path('C:/Windows/Fonts')
pdfmetrics.registerFont(TTFont('Audit32',str(FONT/'arial.ttf')))
pdfmetrics.registerFont(TTFont('Audit32Bold',str(FONT/'arialbd.ttf')))
N=HexColor('#102D3E');T=HexColor('#007582');G=HexColor('#D7E2E7');A=HexColor('#9B5A00')
W,H=840,525; manifests=[]
STYLE=ParagraphStyle('texto',fontName='Audit32',fontSize=12,leading=14,textColor=N)

def text(c,s,x,y,w=760,bold=False,size=12):
    st=ParagraphStyle('t',parent=STYLE,fontName='Audit32Bold' if bold else 'Audit32',fontSize=size,leading=size+2)
    p=Paragraph(escape(s.replace(r'\%','%')),st);_,h=p.wrap(w,1000);p.drawOn(c,x,y-h);return h

def page(slug,title,caption,subtitle):
    c=canvas.Canvas(str(OUT/(slug+'.pdf')),pagesize=(W,H))
    c.setTitle(title);c.setAuthor('audIT Soluciones Tecnológicas SpA')
    c.setFillColor(T);c.setFont('Audit32Bold',12);c.drawString(34,495,'PLANIFICACIÓN / S7 · T-14 · T-15 · T-18')
    text(c,title,34,472,772,True,22);text(c,subtitle,34,435,772)
    manifests.append(dict(file=slug+'.pdf',caption=caption,label='7-'+slug));return c

def finish(c,note):
    c.setStrokeColor(G);c.line(34,48,806,48);text(c,note,34,43,772,size=11.5)
    c.setFillColor(N);c.setFont('Audit32',11.5);c.drawRightString(806,12,'Conciliación 3.2 · 24-11-2026')
    c.save()

def gantt(slug,title,rows,start=1,end=24):
    c=page(slug,title,title,'Ventanas contractuales de trabajo. La aceptación depende de evidencia y acta; las barras no acreditan ejecución.')
    left=278;u=526/(end-start+1);top=392;bottom=100
    for m in range(start,end+1):
        x=left+(m-start)*u
        if ((m%12)+1) in (12,1,2,3,4):c.setFillColor(HexColor('#F0F4F6'));c.rect(x,bottom,u,top-bottom,fill=1,stroke=0)
        if (m-start)%(4 if end>24 else 2)==0:
            c.setFillColor(N);c.setFont('Audit32',12);c.drawString(x,top+8,f'M{m}')
            c.setStrokeColor(G);c.line(x,bottom,x,top)
    for i,p in enumerate(rows):
        y=380-i*min(23,270/max(1,len(rows)-1))
        text(c,p['codigo'],34,y+8,40,True);text(c,p['nombre'],77,y+8,194,size=11.5)
        for a,b in p['ventanas']:
            a=max(start,a);b=min(end,b)
            if a<=b:
                c.setFillColor(T);c.roundRect(left+(a-start)*u,y-5,(b-a+1)*u,8,2,fill=1,stroke=0)
    finish(c,'Gris: temporada de fruta bajo SA-01. La operación conserva SLA, atención fija y refuerzos; las horas se detallan en T-15.')

def main():
    groups=['Gestión','Levantamiento y diseño','Plataforma','Equipo a bordo','Capacidades E1','Integraciones','Datos y migración','Capacidades E2','Adhesión','Calidad y pruebas','Implantación y estabilización','Innovaciones','Operación']
    rows=[]
    for i,name in enumerate(groups,1):
        months=sorted({m for p in P if p['codigo'].startswith(str(i)+'.') for a,b in p['ventanas'] for m in range(a,b+1)})
        windows=[]
        for m in months:
            if windows and windows[-1][1]+1==m:windows[-1][1]=m
            else:windows.append([m,m])
        rows.append(dict(codigo=str(i),nombre=name,ventanas=windows))
    gantt('gantt-panorama','Horizonte contractual M1--M56',rows,end=56)
    c=page('gantt-cpm','Dependencias que gobiernan H12','Cadena de control hasta H12','Se muestra la predecesora que fija el inicio de cada nodo; T-15 conserva todas las ramas, restricciones y holguras.')
    by={n['id']:n for n in R};chain=[];node=by['H12']
    while True:
        chain.append(node)
        if not node['predecesoras']:break
        controlling=max(node['predecesoras'],key=lambda p:by[p['id']]['EF' if p['tipo']=='FS' else 'ES']+p.get('lag',0))
        node=by[controlling['id']]
    chain.reverse();assert len(chain)<=36,'La cadena debe dividirse para conservar tamaño de letra'
    positions=[]
    for i,n in enumerate(chain):
        row=i//6;column=i%6 if row%2==0 else 5-i%6
        x=34+column*130;y=391-row*48;positions.append((x,y))
        if i:
            px,py=positions[-2];c.setStrokeColor(T);c.setLineWidth(1)
            if py==y:
                a=px+116 if x>px else px;b=x if x>px else x+116
                c.line(a,y-16,b,y-16);tip=b;direction=1 if x>px else -1
                c.line(tip-4*direction,y-13,tip,y-16);c.line(tip-4*direction,y-19,tip,y-16)
            else:
                c.line(x+58,py-36,x+58,y);c.line(x+55,y+4,x+58,y);c.line(x+61,y+4,x+58,y)
        c.setStrokeColor(T);c.setFillColor(HexColor('#F0F4F6'));c.roundRect(x,y-36,116,36,3,fill=1,stroke=1)
        text(c,n['id'],x+5,y-2,106,True,11.5);text(c,f"d{n['ES']}--{n['EF']} / HT {n['HT']}",x+5,y-18,106,size=11.5)
    finish(c,'Flechas = dependencia de control; FS por defecto, desfases y SS en T-15. Las cotas de liberación pueden fijar el inicio aunque exista predecesora.')
    fronts=[('gestion','Gestión y levantamiento',{'1','2'}),('plataforma','Plataforma y equipo a bordo',{'3','4'}),('e1','Construcción por capacidades E1',{'5'}),('datos','Integraciones y migración',{'6','7'}),('e2','Capacidades E2 y adhesión',{'8','9'}),('implantacion','Calidad e implantación',{'10','11'}),('innovaciones','Ventanas de innovaciones',{'12'})]
    for slug,title,ids in fronts:gantt('gantt-'+slug,title,[p for p in P if p['codigo'].split('.')[0] in ids])
    c=page('gantt-hitos','Montaje inicial por terminal','Lotes de montaje y condiciones','Diez pilotos en M6; 172 montajes externos M7--M9. Total de configuración inicial: 182 kits.')
    text(c,'Mes',34,395,45,True);text(c,'Terminal',105,395,175,True);text(c,'Kits',305,395,55,True);text(c,'Responsabilidad',390,395,390,True)
    for i,row in enumerate(D['montaje']):
        y=371-i*16
        for value,x,w in [(row['mes'],34,45),(row['terminal'],105,175),(row['kits'],305,55),('Piloto interno' if row['mes']==6 else 'Externo; banco y recepción audIT',390,390)]:text(c,str(value),x,y,w,size=11.5)
    finish(c,'Condiciones: firma y consentimiento aplicables, stock recibido, paso normal por terminal, proveedor reservado y acta por unidad.')
    c=page('gantt-control','Compuertas y capacidad de atención','G13 reservas y cierre técnico','Las duraciones son estimaciones de planificación y no evidencias de disponibilidad de terceros.')
    blocks=[('G13 / capacitación','PREPROD y material por perfil listos día 182; diez días de familiarización y treinta de práctica y evaluación. CP-SEC-05 no se suma otra vez a la demanda.'),('Montaje / integración','A11-PIL, M7-KIT, M8-KIT y M9-KIT: M6--M9. A18-INT: M13--M15, solo lógico. Balizas A11-BAL7/8/9 M7--M9 y lectores A11-LECT M5--M6. Los stocks de 21 balizas y 19 equipos no son altas iniciales.'),('Solapamientos / guardias','M13 y M16: 38,5 FTE equivalentes por refuerzo. M19: 26,5; M20: 25. La asignación por tarea y perfil descuenta atención y coordinación.'),('Cierre / operación','H12 M21; estabilización y cierre EDT6.5/7.2 hasta M24. Mesa 6+1; campo interno 80 h/mes y servicio externo. Madurez condicionada, sin bajar SLA.')]
    for i,(title,body) in enumerate(blocks):text(c,title,34,395-i*73,772,True);text(c,body,34,374-i*73,772)
    finish(c,'La validación en H1 contrasta tarea, ejecutor, turno y capacidad neta; una desviación requiere control de cambios y actualización de caja.')
    gantt('gantt-operacion','Continuidad operacional M21--M56',[p for p in P if p['codigo'].startswith('13.')],21,56)
    combined=fitz.open()
    for e in manifests:
        with fitz.open(OUT/e['file']) as pdf:combined.insert_pdf(pdf)
    combined.save(HERE/'Gantt_Completa_Revisada.pdf')
    (OUT/'manifiesto.json').write_text(json.dumps(manifests,ensure_ascii=False,indent=2),encoding='utf-8')
    refs='Las vistas se presentan en '+', '.join(r'\figref{'+e['label']+'}' for e in manifests)+'.\n\n'
    annex='\n'.join(r'\anexoGrafico{subdocumentos/07-plan-trabajo/graficos/revisada/'+e['file']+'}{'+e['caption']+'}{'+e['label']+'}' for e in manifests)
    p=BASE/'contenido.tex';s=p.read_text(encoding='utf-8');s=re.sub(r'% INICIO LAMINAS GANTT.*?% FIN LAMINAS GANTT',lambda _: '% INICIO LAMINAS GANTT\n'+refs+annex+'\n% FIN LAMINAS GANTT',s,flags=re.S);p.write_text(s,encoding='utf-8')
    # Rótulos propios evitan colisión entre el anexo S7 y el archivo autónomo T-14.
    refs='Las láminas de la carta se citan como '+', '.join(r'\figref{7-t14-'+e['file'][:-4]+'}' for e in manifests)+'.\n\n'
    annex='\n'.join(r'\anexoGrafico{subdocumentos/07-plan-trabajo/graficos/revisada/'+e['file']+'}{'+e['caption']+'}{7-t14-'+e['file'][:-4]+'}' for e in manifests)
    (HERE/'conciliacion-3.2/gantt-formulario.tex').write_text(refs+annex+'\n',encoding='utf-8')
    print('Gantt activa:',len(manifests),'láminas; 54 paquetes; referencia 3.2')

if __name__=='__main__':main()
