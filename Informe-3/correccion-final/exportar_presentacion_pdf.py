"""Genera la copia de lectura desde las láminas renderizadas por el generador PPTX."""
from pathlib import Path
from zipfile import ZipFile

from lxml import etree
import pymupdf

root = Path(__file__).resolve().parents[2] / 'outputs/informe3-mejora'
output = root / 'entrega'
pptx = output / 'INFORME3_AUDIT_PRESENTACION_20261115.pptx'
ns = {'a': 'http://schemas.openxmlformats.org/drawingml/2006/main'}
images = sorted((root / 'revision/slides').glob('slide-*.png'))
assert images
with ZipFile(pptx) as presentation, pymupdf.open() as pdf:
    for i, image in enumerate(images, 1):
        slide = etree.fromstring(presentation.read(f'ppt/slides/slide{i}.xml'))
        page = pdf.new_page(width=960, height=540)
        page.insert_image(page.rect, filename=image)
        # Text from the same slide supplies the search layer for the rendered copy.
        text = '\n'.join(slide.xpath('.//a:t/text()', namespaces=ns))
        page.insert_textbox(pymupdf.Rect(35, 32, 920, 510), text, fontsize=12, render_mode=3)
        if 'Abrir prototipo audIT' in text:
            page.insert_link({
                'kind': pymupdf.LINK_URI, 'from': pymupdf.Rect(45, 421, 265, 457),
                'uri': 'https://carlosabarza.github.io/PaginaAudIT/',
            })
    pdf.set_metadata({'title': 'audIT – Informe 3.1 · Presentación',
                      'author': 'audIT Soluciones Tecnológicas SpA'})
    pdf.save(output / 'INFORME3_AUDIT_PRESENTACION_20261115.pdf', garbage=4, deflate=True)
