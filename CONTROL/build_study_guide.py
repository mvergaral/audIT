from pathlib import Path
import re
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_CELL_VERTICAL_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

ROOT = Path.cwd()
SRC = ROOT / 'plan_estudio_control_2' / 'definitivo_FEP26'
OUT = ROOT / 'Guia_exhaustiva_estudio_certamen_FEP26.docx'

doc = Document()
sec = doc.sections[0]
sec.top_margin = Inches(.7)
sec.bottom_margin = Inches(.7)
sec.left_margin = Inches(.78)
sec.right_margin = Inches(.78)

styles = doc.styles
normal = styles['Normal']
normal.font.name = 'Aptos'
normal.font.size = Pt(9.5)
normal.font.color.rgb = RGBColor(35, 42, 50)
normal.paragraph_format.space_after = Pt(5)
normal.paragraph_format.line_spacing = 1.12
for nm, size in [('Title', 28), ('Subtitle', 13), ('Heading 1', 19), ('Heading 2', 14), ('Heading 3', 11)]:
    st = styles[nm]
    st.font.name = 'Aptos Display' if nm != 'Subtitle' else 'Aptos'
    st.font.size = Pt(size)
    st.font.bold = nm != 'Subtitle'
    st.font.color.rgb = RGBColor(0, 0, 0)
    st.paragraph_format.keep_with_next = True
    st.paragraph_format.space_before = Pt(13 if nm != 'Title' else 0)
    st.paragraph_format.space_after = Pt(6)

def shade(cell, fill):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd'); shd.set(qn('w:fill'), fill); tcPr.append(shd)

def set_repeat_table_header(row):
    trPr = row._tr.get_or_add_trPr()
    tblHeader = OxmlElement('w:tblHeader'); tblHeader.set(qn('w:val'), 'true'); trPr.append(tblHeader)

def add_page_number(paragraph):
    paragraph.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    run = paragraph.add_run('FEP26  |  Guía de estudio  •  ')
    run.font.size = Pt(8); run.font.color.rgb = RGBColor(90, 100, 110)
    fld = OxmlElement('w:fldSimple'); fld.set(qn('w:instr'), 'PAGE')
    paragraph._p.append(fld)

add_page_number(sec.footer.paragraphs[0])

def inline(p, text):
    # Minimal Markdown emphasis/code handling while keeping readable text.
    tokens = re.split(r'(\*\*.*?\*\*|`[^`]+`|\*[^*]+\*)', text)
    for t in tokens:
        if not t: continue
        if t.startswith('**') and t.endswith('**'):
            r=p.add_run(t[2:-2]); r.bold=True
        elif t.startswith('`') and t.endswith('`'):
            r=p.add_run(t[1:-1]); r.font.name='Consolas'; r.font.size=Pt(8.7); r.font.color.rgb=RGBColor(24, 82, 112)
        elif t.startswith('*') and t.endswith('*'):
            r=p.add_run(t[1:-1]); r.italic=True
        else:
            p.add_run(t)

def add_md(text, first_title_as_heading=True):
    lines=text.splitlines(); i=0; in_code=False; code=[]
    while i < len(lines):
        raw=lines[i]; s=raw.strip()
        if s.startswith('```'):
            if in_code:
                p=doc.add_paragraph(); p.paragraph_format.left_indent=Inches(.22); p.paragraph_format.right_indent=Inches(.12)
                p.paragraph_format.space_before=Pt(2); p.paragraph_format.space_after=Pt(7)
                r=p.add_run('\n'.join(code)); r.font.name='Consolas'; r.font.size=Pt(8.2); r.font.color.rgb=RGBColor(28,61,78)
                in_code=False; code=[]
            else: in_code=True
            i+=1; continue
        if in_code:
            code.append(raw); i+=1; continue
        if not s or s in ('---','***'):
            i+=1; continue
        # Markdown table
        if s.startswith('|') and i+1 < len(lines) and re.match(r'^\s*\|?\s*:?-{2,}', lines[i+1]):
            rows=[]
            while i < len(lines) and lines[i].strip().startswith('|'):
                cells=[c.strip() for c in lines[i].strip().strip('|').split('|')]
                if not all(re.fullmatch(r':?-{2,}:?', c or '-') for c in cells): rows.append(cells)
                i+=1
            if rows:
                n=max(map(len, rows)); tab=doc.add_table(rows=0, cols=n); tab.alignment=WD_TABLE_ALIGNMENT.CENTER; tab.style='Table Grid'
                for ri, vals in enumerate(rows):
                    cells=tab.add_row().cells
                    for ci in range(n):
                        cell=cells[ci]; cell.vertical_alignment=WD_CELL_VERTICAL_ALIGNMENT.CENTER
                        p=cell.paragraphs[0]; p.paragraph_format.space_after=Pt(1); p.paragraph_format.line_spacing=1.0
                        inline(p, vals[ci] if ci < len(vals) else '')
                        for rr in p.runs: rr.font.size=Pt(8)
                        if ri==0:
                            shade(cell,'DCE8EE')
                            for rr in p.runs: rr.bold=True; rr.font.color.rgb=RGBColor(0,0,0)
                    if ri==0: set_repeat_table_header(tab.rows[0])
                doc.add_paragraph().paragraph_format.space_after=Pt(1)
            continue
        hm=re.match(r'^(#{1,4})\s+(.*)',s)
        if hm:
            level=len(hm.group(1)); title=hm.group(2).strip()
            if level==1 and title.startswith(('Capítulo ', 'PMBOK ', 'Parte ', 'Pauta ', 'Banco ', 'Caso integrador')):
                doc.add_page_break()
            p=doc.add_paragraph(style=f'Heading {min(level,3)}'); inline(p,title)
            i+=1; continue
        if s.startswith('>'):
            p=doc.add_paragraph(); p.paragraph_format.left_indent=Inches(.22); p.paragraph_format.right_indent=Inches(.18)
            p.paragraph_format.space_before=Pt(4); p.paragraph_format.space_after=Pt(7)
            inline(p,s.lstrip('> ').strip())
            for r in p.runs: r.italic=True; r.font.color.rgb=RGBColor(52,83,98)
            i+=1; continue
        if re.match(r'^[-*+]\s+',s):
            p=doc.add_paragraph(style='List Bullet'); inline(p,re.sub(r'^[-*+]\s+','',s)); p.paragraph_format.space_after=Pt(2)
            i+=1; continue
        if re.match(r'^\d+[.)]\s+',s):
            p=doc.add_paragraph(style='List Number'); inline(p,re.sub(r'^\d+[.)]\s+','',s)); p.paragraph_format.space_after=Pt(2)
            i+=1; continue
        p=doc.add_paragraph(); inline(p,s)
        i+=1

# Cover
p=doc.add_paragraph(style='Title'); p.alignment=WD_ALIGN_PARAGRAPH.LEFT
p.add_run('Guía exhaustiva de estudio')
p=doc.add_paragraph(style='Subtitle'); p.add_run('Certamen de Formulación de Proyectos Informáticos  |  FEP26')
p=doc.add_paragraph(); p.paragraph_format.space_before=Pt(24)
r=p.add_run('Materia explicada, fórmulas paso a paso y dos controles de práctica con pauta razonada'); r.bold=True; r.font.size=Pt(12)
p=doc.add_paragraph('Arquitectura · requisitos y alcance · planificación · estimación · riesgos · adquisiciones · calidad · sala de servidores')
p.paragraph_format.space_before=Pt(6)
p=doc.add_paragraph('Guía de trabajo personal'); p.paragraph_format.space_before=Pt(48)
for r in p.runs: r.font.size=Pt(10); r.font.color.rgb=RGBColor(80,90,100)
doc.add_page_break()

intro='''# Cómo estudiar con esta guía

Esta guía reúne las clases FEP01–FEP06, los capítulos PMBOK 5, 6, 8 y 11, lecturas de estimación y WBS, y la forma de preguntar observada en las pautas de los dos controles publicados. El recorrido conecta los conceptos con una licitación de software y termina con dos simulacros originales, uno amplio y otro de alta dificultad.

## Un método para aprender y responder

1. Lee un bloque breve y cierra el documento.
2. Explica el concepto en voz alta usando un ejemplo propio.
3. Resuelve un ejercicio sin mirar la fórmula; luego comprueba unidades y resultado.
4. En preguntas de caso, escribe concepto, evidencia del enunciado, decisión y consecuencia.
5. Mantén una lista de errores: qué confundiste, por qué y qué señal del enunciado debiste notar.

Para cada cálculo usa la secuencia **datos → fórmula → reemplazo con unidades → resultado → interpretación**. Una alternativa correcta sin desarrollo suele perder puntos. En desarrollo, responde exactamente lo preguntado antes de agregar contexto.

## Mapa de materia

| Bloque | Pregunta que responde |
|---|---|
| Proyecto y requisitos | ¿Qué necesidad se atenderá y quién define que está resuelta? |
| Alcance y EDT | ¿Qué trabajo está incluido y cómo se descompone? |
| Cronograma | ¿Qué depende de qué, cuánto dura y qué controla la fecha final? |
| Arquitectura e infraestructura | ¿Cómo se organiza y despliega una solución que satisface los requisitos? |
| Estimación y precio | ¿Cuánto trabajo, tiempo y dinero requiere y con qué incertidumbre? |
| Riesgos | ¿Qué incertidumbre puede afectar objetivos y qué respuesta conviene? |
| Adquisiciones y contratos | ¿Qué conviene hacer, comprar o arrendar y quién asume cada riesgo? |
| Calidad | ¿Cómo se previene, mide y acepta la conformidad? |
| Sala de servidores | ¿Qué espacio, energía, refrigeración, red y continuidad requiere la infraestructura? |

'''
add_md(intro)

files=[
 '01_caso_transversal.md',
 '02_proyecto_interesados_y_requisitos.md',
 '03_alcance_y_EDT_PMBOK05.md',
 '04_cronograma_PMBOK06.md',
 '05_arquitectura_logica.md',
 '06_arquitectura_fisica_nube_y_continuidad.md',
 '07_sala_de_servidores.md',
 '08_estimacion_software_UCP.md',
 '09_costos_tarifas_y_precio.md',
 '10_riesgos_PMBOK11_y_licitacion.md',
 '11_adquisiciones_contratos_y_TCO.md',
 '12_calidad_PMBOK08.md',
 '13_caso_integrador_resuelto.md',
 '15_formulas_comparaciones_y_glosario.md',
 '16_mapa_ITTO_PMBOK.md',
]
for name in files:
    add_md((SRC/name).read_text(encoding='utf-8'))

# The two practice exams and their reasoned keys.
bank1=(SRC/'14_banco_de_preguntas.md').read_text(encoding='utf-8')
bank1=bank1.replace('# Banco de preguntas para el Control 2', '# Simulacro 1 - Control integral de FEP26', 1)
add_md(bank1)
bank2=(SRC/'18_banco_acotado_profesor_sin_respuestas.md').read_text(encoding='utf-8')
bank2=bank2.replace('# Banco acotado de alta dificultad - Control 2', '# Simulacro 2 - Nivel avanzado', 1)
add_md(bank2)
key2=(SRC/'19_pauta_banco_acotado_profesor.md').read_text(encoding='utf-8')
key2=key2.replace('# Pauta razonada - Banco acotado de alta dificultad', '# Pauta razonada del Simulacro 2', 1)
add_md(key2)

# Closing high-yield review tailored to patterns visible in the published controls.
add_md((SRC/'20_anexo_produccion_costos.md').read_text(encoding='utf-8'))
add_md('''# Repaso final y estrategia de examen

## Señales que conviene reconocer

- **EDT:** es jerarquía del alcance; no dibujes precedencias dentro de ella. El primer nivel puede organizarse por entregables, fases, subproyectos o disciplinas si el conjunto cubre el alcance total. Descompón hasta que el trabajo se pueda estimar, asignar y controlar; aplica también el período de reporte.
- **Cronograma:** en una relación FS la sucesora espera al fin; en SS depende del inicio; en FF se ancla al fin. Para una unión usa el máximo de los finales tempranos; al retroceder, el mínimo de los inicios tardíos. Puede haber varias rutas críticas.
- **Disponibilidad:** componentes en serie se multiplican. En redundancia activa-activa independiente, la disponibilidad del conjunto redundado es `1 − (1−A1)(1−A2)`. Incluye los componentes comunes en serie.
- **Estimación:** separa tamaño, esfuerzo, duración, costo y precio. Distingue horas nominales de productivas. Declara granularidad de casos de uso, supuestos, rangos e incertidumbre.
- **Riesgos:** formula causa–evento incierto–efecto. Riesgo materializado pasa a problema. EMV ayuda a comparar alternativas; no reemplaza el costo base ni el análisis de apetito al riesgo.
- **Sala:** PUE = energía total del recinto / energía TI; DCiE es el inverso. El clima se estima sobre la carga TI. Dimensiona en cadena y no confundas redundancia aparente con caminos independientes.
- **Calidad:** Gestionar la Calidad mira cómo se trabaja y mejora procesos; Controlar la Calidad verifica entregables; Validar el Alcance obtiene aceptación formal.
- **Adquisiciones:** RFI explora; RFQ pide precio comparable para algo especificado; IFB licita con especificación cerrada; RFP pide una solución propuesta cuando aún se evalúan método y equipo.

## Gestión del tiempo durante el certamen

1. Recorre el control y marca cálculos, conceptos y casos.
2. En cálculos, anota primero datos y unidad solicitada. Evita redondear hasta el final.
3. En alternativas, descarta opciones que cambian unidades, invierten una razón o confunden proceso con entregable.
4. Reserva tiempo para revisar signos, porcentajes, suma de etapas y conclusiones.
5. Si una pregunta parece ambigua, declara la convención usada y continúa con una solución consistente.

## Referencias utilizadas

Clases FEP01.26–FEP06.26; PMBOK sexta edición, capítulos 5, 6, 8 y 11; WBS Second Edition; lecturas de métodos de estimación, estimación basada en casos de uso y puntos de función; resumen de producción y costos; hoja de fórmulas; pautas publicadas de Control 1 y Control 2. Las preguntas de los simulacros de esta guía son material de práctica y su pauta se incluye para autocorrección.
''')

# Core properties and save
doc.core_properties.title='Guía exhaustiva de estudio para el certamen FEP26'
doc.core_properties.subject='Formulación de Proyectos Informáticos: resumen pedagógico y controles de práctica'
doc.core_properties.author=''
doc.save(OUT)
print(OUT)
