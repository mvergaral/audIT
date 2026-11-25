"""Incorpora las curvas que el exportador Markdown del repo deja como texto."""
from pathlib import Path
from docx import Document
from docx.shared import Inches
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
import re
OUT=Path(__file__).resolve().parent
p=OUT/'documentos/AUDIT_AnalisisFinanciero_2_20261125.docx';d=Document(p)
if len(d.inline_shapes)<2:
    for label,name in [('Figura 2.1.','curva-s'),('Figura 2.2.','solvencia-3.2')]:
        anchor=next(p for p in d.paragraphs if p.text.lstrip('*').startswith(label))
        picture=d.add_paragraph();picture.add_run().add_picture(str(OUT/'revision'/(name+'.png')),width=Inches(6.0));anchor._p.addprevious(picture._p)
for paragraph in list(d.paragraphs):
    if paragraph.text.startswith('!['):paragraph._p.getparent().remove(paragraph._p)
d.save(p)
for p in (OUT/'documentos').glob('*.docx'):
    doc=Document(p)
    for paragraph in doc.paragraphs:
        if re.match(r'^Tabla \d',paragraph.text):paragraph.paragraph_format.keep_with_next=True
    for table in doc.tables:
        headers=[c.text for c in table.rows[0].cells]
        widths=None
        if headers==['N.º','Concepto','Moneda','Valor neto','IVA (19 %)','Total']:
            widths=[.3,1.81,.49,1.31,1.31,1.31]
        elif len(headers)==7 and headers[0]=='Hito':
            widths=[.45,1.93,.45,.5,1.1,1.0,1.1]
        if widths:
            table.autofit=False
            for column,width in zip(table.columns,widths):column.width=Inches(width)
            for row in table.rows:
                for cell,width in zip(row.cells,widths):cell.width=Inches(width)
    for node in doc.element.iter(qn('w:t')):
        if node.text:
            node.text=node.text.replace(r'\noindent',' ')
            node.text=re.sub(r'(?<=[a-záéíóúñ])(?=CLP|UF|USD)',' ',node.text)
            node.text=re.sub(r'\b(CLP|UF|USD) +(?=-?\d)',lambda m:m[1]+'\u00a0',node.text)
    doc.save(p)
for path in (OUT/'documentos').glob('AUDIT_*.md'):
    path.write_text(path.read_text(encoding='utf-8').replace(r'\noindent',''),encoding='utf-8')
print('DOCX con dos figuras y sin sintaxis Markdown de imagen sin convertir.')
