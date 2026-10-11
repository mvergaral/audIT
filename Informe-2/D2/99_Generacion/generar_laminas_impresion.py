"""Láminas vectoriales para anexos de 257,4 x 167 mm, letra mínima 10 pt."""
from pathlib import Path
import json
import re
import math
from xml.etree import ElementTree as ET
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, white
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from fontTools.ttLib import TTFont as VariableFont
from fontTools.varLib.instancer import instantiateVariableFont
from xml.sax.saxutils import escape
import fitz

ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT / 'recursos/Formato-Oferta-audIT'
OUT = BASE / 'subdocumentos/07-plan-trabajo/graficos'
OUT.mkdir(exist_ok=True)
DATA = json.loads((ROOT / 'Informe-2/d2/99_Generacion/plan_detallado.json').read_text(encoding='utf-8'))
PACKAGES = DATA['paquetes']
GROUPS = ['Gestión del proyecto', 'Levantamiento y diseño', 'Plataforma', 'Equipo a bordo',
          'Servicios Etapa 1', 'Integraciones', 'Datos y migración', 'Servicios Etapa 2',
          'Adhesión de transportistas', 'Calidad y pruebas', 'Implantación', 'Innovaciones', 'Operación']
font_source = Path('C:/Users/mvergara/AppData/Local/Microsoft/Windows/Fonts/IBMPlexSans-VariableFont_wdth,wght.ttf')
font_output = Path(__file__).resolve().parent / 'salida_temporal/fuentes'
font_output.mkdir(parents=True, exist_ok=True)
for name, weight in [('Diagrama',400),('DiagramaBold',600)]:
    target=font_output/f'Plex-{weight}.ttf'
    if not target.exists():
        font=instantiateVariableFont(VariableFont(str(font_source)),{'wght':weight,'wdth':100},inplace=True)
        font.save(str(target))
    pdfmetrics.registerFont(TTFont(name,str(target)))
pdfmetrics.registerFontFamily('Diagrama', normal='Diagrama', bold='DiagramaBold', italic='Diagrama', boldItalic='DiagramaBold')
NAVY = HexColor('#0F2A43')
BLUE = HexColor('#256B87')
PALE = HexColor('#E6EDF2')
W, H = 720, 450
STYLE = ParagraphStyle('texto', fontName='Diagrama', fontSize=10, leading=12, textColor=NAVY)

def text(c, value, x, y, width, bold=False):
    p = Paragraph(('<b>' + escape(value) + '</b>') if bold else escape(value), STYLE)
    _, h = p.wrap(width, H)
    p.drawOn(c, x, y-h)
    return h

def page(filename, title, subtitle):
    c = canvas.Canvas(str(OUT / filename), pagesize=(W,H))
    c.setTitle(title)
    c.setFillColor(NAVY)
    c.setFont('DiagramaBold', 16)
    c.drawString(18, H-26, title)
    text(c, subtitle, 18, H-39, W-36)
    c.setStrokeColor(BLUE)
    c.line(18, H-66, W-18, H-66)
    text(c, 'Fuente: elaboración propia a partir de los Formularios T-14, T-15, T-18 y T-19.', 18, 27, W-36)
    return c

edt_files = []
gantt_files = []
c = page('edt-general.pdf', 'EDT - vista general', '13 elementos de primer nivel; 54 paquetes desarrollados en las láminas de detalle.')
for i, name in enumerate(GROUPS):
    col, row = i//7, i%7
    x, y = 30+col*350, 364-row*43
    c.setFillColor(PALE)
    c.roundRect(x,y-31,330,33,4,stroke=0,fill=1)
    count = sum(p['codigo'].split('.')[0] == str(i+1) for p in PACKAGES)
    text(c, f'{i+1}. {name} ({count} paquetes)', x+9, y-5, 312, True)
c.save()
edt_files.append(('edt-general.pdf','EDT general: trece elementos','7-edt'))

for i, name in enumerate(GROUPS, 1):
    rows = [p for p in PACKAGES if p['codigo'].split('.')[0] == str(i)]
    for start in range(0, len(rows), 3):
        n = start//3+1
        filename = f'edt-detalle-{i:02}-{n}.pdf'
        c = page(filename, f'EDT {i} - {name} ({n})', 'Mismos códigos y alcance que T-14; detalle de entregable, aceptación y responsable.')
        y = 372
        for p in rows[start:start+3]:
            h = text(c, f"{p['codigo']}  {p['nombre']}", 22, y, 674, True)
            y -= h+3
            for label, key in [('Entregable','entregable'),('Aceptación','aceptacion'),('Responsable','responsable')]:
                h = text(c, f"{label}: {p[key]}", 32, y, 662)
                y -= h+2
            c.setStrokeColor(PALE)
            c.line(22,y,698,y)
            y -= 9
        if y < 42:
            raise RuntimeError(f'Detalle EDT {i} excede la página: {y}')
        c.save()
        edt_files.append((filename,f'EDT {i}: {name}, detalle {n}',f'7-edt-detalle-{i:02}-{n}'))

def gantt(filename, title, rows, months, summary=False):
    c = page(filename, title, 'Mes 1: febrero de 2027 (supuesto SA-01). Barras por paquete; no sustituyen la red CPM de T-15.')
    left, right, top, bottom = 232, 698, 326, 100
    unit = (right-left)/months
    # Temporada de fruta según el calendario supuesto, diciembre a abril.
    for m in range(1, months+1):
        actual_month = ((m+0)%12)+1
        if actual_month in (12,1,2,3,4):
            c.setFillColor(PALE)
            c.rect(left+(m-1)*unit,bottom,unit,top-bottom,fill=1,stroke=0)
    tick = 4 if months == 56 else 2
    c.setFillColor(NAVY)
    c.setFont('Diagrama',10)
    for m in range(1,months+1,tick):
        x = left+(m-1)*unit
        c.setStrokeColor(HexColor('#CAD6DF'))
        c.line(x,bottom,x,top)
        c.drawString(x,top+10,f'M{m}')
    c.drawRightString(right,top+26,f'M{months}')
    dy = (top-bottom)/max(len(rows),1)
    for j,p in enumerate(rows):
        y = top-(j+.5)*dy
        label = f"{p['codigo']} {p['nombre']}"
        text(c,label,20,y+9,left-28)
        c.setFillColor(BLUE)
        for a,b in p['ventanas']:
            if a <= months:
                c.rect(left+(a-1)*unit,y-5,(min(b,months)-a+1)*unit,10,fill=1,stroke=0)
    # Hitos contractuales y leyenda, separados de las barras.
    c.setFillColor(NAVY)
    c.setFont('Diagrama',10)
    for code,m,_ in DATA['hitos']:
        if m <= months:
            x = left+(m-.5)*unit
            c.line(x,75,x,85)
            # Alternar tres filas evita solapamiento de los hitos próximos.
            c.drawCentredString(x,55-(int(code[1:])%3)*12,code)
    text(c,'Gris: temporada de fruta. Barras: ventanas mensuales. H1-H12: hitos de E-25 descritos en S7.',20,top+44,W-40)
    c.save()

overview=[]
for i,name in enumerate(GROUPS,1):
    months = sorted({m for p in PACKAGES if p['codigo'].split('.')[0]==str(i) for a,b in p['ventanas'] for m in range(a,b+1)})
    windows=[]
    for m in months:
        if windows and m==windows[-1][1]+1:
            windows[-1][1]=m
        else:
            windows.append([m,m])
    overview.append({'codigo':str(i),'nombre':name,'ventanas':windows})
gantt('gantt-general.pdf','Gantt - vista general M1-M56',overview,56,True)
gantt_files.append(('gantt-general.pdf','Gantt general M1-M56','7-gantt'))
for months in (24,56):
    rows=[p for p in PACKAGES if any(a<=months for a,b in p['ventanas'])]
    for start in range(0,len(rows),6):
        n=start//6+1
        filename=f'gantt-m{months}-detalle-{n:02}.pdf'
        gantt(filename,f'Gantt M1-M{months} - detalle {n}',rows[start:start+6],months)
        gantt_files.append((filename,f'Gantt M1-M{months}: detalle {n}',f'7-gantt-{months}-{n:02}'))

# Recuperar archivos PERT requeridos sin cambiar actividades ni precedencias.
for n in (1,2):
    source=BASE/f'figuras/07-plan-trabajo/pert-etapa{n}.svg'
    root=ET.parse(source).getroot()
    _,_,vw,vh=map(float,root.attrib['viewBox'].split())
    pw=float(root.attrib['width'].replace('mm',''))*72/25.4
    ph=float(root.attrib['height'].replace('mm',''))*72/25.4
    scale=pw/vw
    c=canvas.Canvas(str(OUT/f'pert-etapa{n}.pdf'),pagesize=(pw,ph))
    for node in root:
        tag=node.tag.split('}')[-1]
        a=node.attrib
        if tag=='defs':
            continue
        stroke=a.get('stroke','none')
        fill=a.get('fill','none')
        if stroke!='none':
            c.setStrokeColor(HexColor(stroke))
        if fill!='none':
            c.setFillColor(HexColor(fill))
        c.setLineWidth(float(a.get('stroke-width',1))*scale)
        dash=a.get('stroke-dasharray','')
        c.setDash([float(v)*scale for v in re.split(r'[, ]+',dash) if v] if dash else [])
        if tag=='rect':
            x,y,w,h=[float(a.get(k,0))*scale for k in ('x','y','width','height')]
            c.roundRect(x,ph-y-h,w,h,float(a.get('rx',0))*scale,stroke=int(stroke!='none'),fill=int(fill!='none'))
        elif tag=='polyline':
            pts=[tuple(map(float,p.split(','))) for p in a['points'].split()]
            path=c.beginPath()
            path.moveTo(pts[0][0]*scale,ph-pts[0][1]*scale)
            for x,y in pts[1:]:
                path.lineTo(x*scale,ph-y*scale)
            c.drawPath(path,stroke=1,fill=0)
            if a.get('marker-end'):
                x,y=pts[-1]; px,py=pts[-2]
                angle=math.atan2(y-py,x-px)
                arrow=c.beginPath()
                arrow.moveTo(x*scale,ph-y*scale)
                for sign in (-1,1):
                    ax=x-11*math.cos(angle)+sign*5*math.sin(angle)
                    ay=y-11*math.sin(angle)-sign*5*math.cos(angle)
                    arrow.lineTo(ax*scale,ph-ay*scale)
                arrow.close()
                c.setFillColor(HexColor(stroke))
                c.drawPath(arrow,fill=1,stroke=0)
        elif tag=='text':
            font='DiagramaBold' if a.get('font-weight') in ('600','700','bold') else 'Diagrama'
            c.setFont(font,float(a['font-size'])*scale)
            x,y=float(a['x'])*scale,ph-float(a['y'])*scale
            value=''.join(node.itertext())
            draw={'middle':c.drawCentredString,'end':c.drawRightString}.get(a.get('text-anchor'),c.drawString)
            draw(x,y,value)
        else:
            raise RuntimeError(f'Elemento PERT no soportado: {tag}')
    c.save()

def annexes(entries):
    return '\n'.join(r'\anexoGrafico{subdocumentos/07-plan-trabajo/graficos/'+f'{filename}}}{{{title}}}{{{label}}}' for filename,title,label in entries)

content=BASE/'subdocumentos/07-plan-trabajo/contenido.tex'
s=content.read_text(encoding='utf-8')
s=re.sub(r'\\figuraHorizontal\{\.\./\.\./Informe-2/D2/01_EDT/01_Completa/EDT_Completa.png\}[^\n]*',
         lambda _:annexes(edt_files),s)
s=re.sub(r'\\figura\[ancho=completo,alto=0.92,lugar=p\]\{\.\./\.\./Informe-2/D2/02_Gantt/01_Graficos/Gantt_Completa_M01-M56.png\}[^\n]*',
         lambda _:annexes(gantt_files),s)
s=s.replace('figuras/07-plan-trabajo/pert-etapa','subdocumentos/07-plan-trabajo/graficos/pert-etapa')
for entries, anchor in [(edt_files[1:],r'\anexoGrafico{subdocumentos/07-plan-trabajo/graficos/edt-general.pdf}'),
                        (gantt_files[1:],r'\anexoGrafico{subdocumentos/07-plan-trabajo/graficos/gantt-general.pdf}')]:
    references='Los detalles se presentan en '+', '.join(r'\figref{'+label+'}' for _,_,label in entries)+'.\n\n'
    if references not in s:
        s=s.replace(anchor,references+anchor)
content.write_text(s,encoding='utf-8')

# Una regeneración sustituye únicamente los anexos y referencias de estas láminas.
for section,entries in [('edt',edt_files),('gantt',gantt_files)]:
    marker_start=f'% INICIO LAMINAS {section.upper()}'
    marker_end=f'% FIN LAMINAS {section.upper()}'
    block=marker_start+'\n'+'Los detalles se presentan en '+', '.join(r'\figref{'+label+'}' for _,_,label in entries[1:])+'.\n\n'+annexes(entries)+'\n'+marker_end
    # Retirar versiones generadas previamente, evitando duplicar etiquetas.
    s=re.sub(r'Los detalles se presentan en \\figref\{7-'+section+r'[^\n]+\.\n\n','',s)
    s=re.sub(r'\\anexoGrafico\{subdocumentos/07-plan-trabajo/graficos/'+section+r'[^\n]+\n?','',s)
    s=re.sub(re.escape(marker_start)+r'.*?'+re.escape(marker_end),'',s,flags=re.S)
    anchor=r'\section{EDT}' if section=='edt' else r'\subsection{Carta Gantt}'
    pos=s.index('\n\n',s.index(anchor))+2
    # Insertar tras el primer párrafo para conservar la regla estructural.
    pos=s.index('\n\n',pos)+2
    s=s[:pos]+block+'\n\n'+s[pos:]
content.write_text(s,encoding='utf-8')

merged=fitz.open()
records=[]
for filename,title,label in edt_files+gantt_files+[(f'pert-etapa{n}.pdf',f'PERT Etapa {n}',f'7-pert{n}') for n in (1,2)]:
    doc=fitz.open(OUT/filename)
    sizes=[span['size'] for p in doc for block in p.get_text('dict')['blocks'] if 'lines' in block for line in block['lines'] for span in line['spans'] if span['text'].strip()]
    records.append({'archivo':filename,'minimo_pt':round(min(sizes),2) if sizes else None})
    merged.insert_pdf(doc)
merged.save(str(ROOT/'Informe-2/d2/03_Apoyo/Laminas_EDT_Gantt_PERT.pdf'))
(OUT/'verificacion_letra.json').write_text(json.dumps(records,ensure_ascii=False,indent=2),encoding='utf-8')
print(f'{len(records)} láminas generadas; mínimos de letra:',records)

portal=ROOT/'Informe-2/d2/00_ABRIR_ENTREGABLES.html'
s=portal.read_text(encoding='utf-8')
if '03_Apoyo/Laminas_EDT_Gantt_PERT.pdf' not in s:
    link='<p><a href="03_Apoyo/Laminas_EDT_Gantt_PERT.pdf">Vistas para impresión: EDT, Gantt y PERT (11-10-2026)</a></p>'
    s=s.replace('<body>','<body>'+link,1)
    portal.write_text(s,encoding='utf-8')
