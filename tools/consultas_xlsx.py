#!/usr/bin/env python3
"""Genera la planilla de consultas en XLSX desde el registro en Markdown.

Se escribe el XLSX a mano con zipfile porque openpyxl no está instalado y esto
no justifica una dependencia: son siete columnas de texto y ninguna fórmula.
El formato exigido está en el Artículo 43.2 de las Bases Administrativas.
"""

import html
import re
import sys
import zipfile
from datetime import date
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
CABECERAS = ["Número correlativo", "Nombre de la empresa proponente",
             "Fecha de la consulta", "Tipo de consulta",
             "Documento, sección, artículo o anexo y página",
             "Consulta detallada, formulada de manera concreta y precisa",
             "Propuesta de interpretación del proponente"]
TIPOS = {"Administrativa", "Técnica", "Anexo"}
ANCHOS = [10, 16, 14, 16, 46, 90, 80]


def filas_del_md(path, empresa, fecha):
    """Lee las tablas de consultas del registro; ignora reserva y descartes."""
    filas, dentro = [], False
    for linea in path.read_text().split("\n"):
        if linea.startswith("## "):
            dentro = linea.startswith("## Consultas para envío")
        if not dentro or not linea.startswith("|"):
            continue
        c = [x.strip() for x in linea.strip("|").split("|")]
        if len(c) != 5 or not c[0].isdigit():
            continue
        filas.append([c[0], empresa, fecha, c[1], c[2], c[3], c[4]])
    return filas


def celda(ref, valor):
    return (f'<c r="{ref}" t="inlineStr" s="1"><is><t xml:space="preserve">'
            f'{html.escape(str(valor))}</t></is></c>')


def escribir(destino, filas):
    cols = "".join(f'<col min="{i+1}" max="{i+1}" width="{w}" customWidth="1"/>'
                   for i, w in enumerate(ANCHOS))
    xml = ['<?xml version="1.0" encoding="UTF-8" standalone="yes"?>',
           '<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">',
           f'<cols>{cols}</cols><sheetData>']
    for n, fila in enumerate([CABECERAS] + filas, start=1):
        cs = "".join(celda(f"{chr(65+i)}{n}", v) for i, v in enumerate(fila))
        xml.append(f'<row r="{n}">{cs}</row>')
    xml.append('</sheetData></worksheet>')

    estilos = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
               '<styleSheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">'
               '<fonts count="1"><font><sz val="11"/><name val="Calibri"/></font></fonts>'
               '<fills count="1"><fill><patternFill patternType="none"/></fill></fills>'
               '<borders count="1"><border/></borders>'
               '<cellStyleXfs count="1"><xf/></cellStyleXfs>'
               '<cellXfs count="2"><xf xfId="0"/>'
               '<xf xfId="0" applyAlignment="1">'
               '<alignment vertical="top" wrapText="1"/></xf></cellXfs>'
               '</styleSheet>')

    with zipfile.ZipFile(destino, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml",
                   '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
                   '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
                   '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
                   '<Default Extension="xml" ContentType="application/xml"/>'
                   '<Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>'
                   '<Override PartName="/xl/worksheets/sheet1.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>'
                   '<Override PartName="/xl/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.styles+xml"/>'
                   '</Types>')
        z.writestr("_rels/.rels",
                   '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
                   '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
                   '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="xl/workbook.xml"/>'
                   '</Relationships>')
        z.writestr("xl/workbook.xml",
                   '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
                   '<workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" '
                   'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">'
                   '<sheets><sheet name="Consultas" sheetId="1" r:id="rId1"/></sheets></workbook>')
        z.writestr("xl/_rels/workbook.xml.rels",
                   '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
                   '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
                   '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet1.xml"/>'
                   '<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>'
                   '</Relationships>')
        z.writestr("xl/styles.xml", estilos)
        z.writestr("xl/worksheets/sheet1.xml", "".join(xml))


if __name__ == "__main__":
    empresa = sys.argv[1] if len(sys.argv) > 1 else "AUDIT"
    envio = sys.argv[2] if len(sys.argv) > 2 else date.today().strftime("%Y%m%d")
    fecha = f"{envio[6:8]}-{envio[4:6]}-{envio[0:4]}"

    origen = RAIZ / "equipo/D2/consultas-d2-v2.md"
    filas = filas_del_md(origen, empresa, fecha)
    malos = [f[0] for f in filas if f[3] not in TIPOS]
    if malos:
        sys.exit(f"tipo no permitido por el Art. 43.2 en las consultas: {malos}")

    destino = RAIZ / f"equipo/D2/CONSULTAS_{empresa}_{envio}.XLSX"
    escribir(destino, filas)
    print(f"{len(filas)} consultas -> {destino.relative_to(RAIZ)}")
