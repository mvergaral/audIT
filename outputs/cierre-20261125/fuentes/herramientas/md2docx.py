#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Markdown -> DOCX sin dependencias (OOXML escrito directamente).

  python3 herramientas/md2docx.py entrada.md salida.docx "Título" "Pie" [folio]

Adaptado de D4/tools-md2docx.py para los entregables 1 y 2 del Sobre N.º 3,
que el Formulario E-21 y el Artículo 40.4 piden además en DOCX. El Markdown
lo escribe herramientas/tex2md.py con las cifras que imprimió el PDF, así que
el DOCX trae las mismas cifras.

Lo que cumple del Artículo 40: carta vertical, cuerpo en IBM Plex Serif de
11 pt, tablas en IBM Plex Sans de 9,5 pt, folio en el extremo inferior
derecho que empieza en el mismo número que el PDF, e índice detallado (campo
de índice que Word actualiza al abrir el archivo). La media firma va en el
PDF: el DOCX es la versión editable.
"""
import html
import re
import sys
import zipfile

NS = ('xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" '
      'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"')
SERIF, SANS, MONO = "IBM Plex Serif", "IBM Plex Sans", "IBM Plex Mono"
MARINO, SECUNDARIO, TINTA, GRIS, FILETE, TURQUESA = \
    "0F2A43", "4A5D70", "1B2733", "E6EDF2", "C8D2DE", "18B7C7"
ANCHO_TEXTO = 12240 - 1701 - 1134        # carta menos márgenes, en veinteavos de punto


def E(t):
    return html.escape(t, quote=False).replace('"', "&quot;")


def run(t, b=False, i=False, code=False, color=None, sz=None, fuente=None):
    if not t:
        return ""
    rpr = []
    f = MONO if code else fuente
    if f:
        rpr.append(f'<w:rFonts w:ascii="{f}" w:hAnsi="{f}" w:cs="{f}"/>')
    if b:
        rpr.append("<w:b/>")
    if i:
        rpr.append("<w:i/>")
    if color:
        rpr.append(f'<w:color w:val="{color}"/>')
    if sz:
        rpr.append(f'<w:sz w:val="{int(sz * 2)}"/><w:szCs w:val="{int(sz * 2)}"/>')
    p = f"<w:rPr>{''.join(rpr)}</w:rPr>" if rpr else ""
    return f'<w:r>{p}<w:t xml:space="preserve">{E(t)}</w:t></w:r>'


TOK = re.compile(r"(\*\*.+?\*\*|`[^`]+`|(?<![*\w])\*[^*\n]+\*(?![*\w])|\[[^\]]+\])")


def runs(texto, sz=None, negrita=False, fuente=None):
    """Negrita, código, cursiva y marcadores [por completar] en gris."""
    out = []
    for parte in TOK.split(texto):
        if not parte:
            continue
        if parte.startswith("**") and parte.endswith("**"):
            out.append(run(parte[2:-2], b=True, sz=sz, fuente=fuente))
        elif parte.startswith("`") and parte.endswith("`"):
            out.append(run(parte[1:-1], code=True, sz=sz))
        elif parte.startswith("[") and parte.endswith("]"):
            out.append(run(parte, color=SECUNDARIO, sz=sz, fuente=SANS))
        elif len(parte) > 2 and parte[0] == "*" and parte[-1] == "*":
            out.append(run(parte[1:-1], i=True, sz=sz, fuente=fuente))
        else:
            out.append(run(parte, b=negrita, sz=sz, fuente=fuente))
    return "".join(out)


def para(contenido, estilo=None, antes=0, despues=120, fondo=None, borde=None, jc=None,
         seguir=False, sangria=0):
    pr = []
    if estilo:
        pr.append(f'<w:pStyle w:val="{estilo}"/>')
    if seguir:
        pr.append("<w:keepNext/>")
    # orden del esquema OOXML (CT_PPr): pStyle, keepNext, pBdr, shd, spacing, ind, jc
    if borde:
        pr.append(f'<w:pBdr><w:left w:val="single" w:sz="18" w:space="8" w:color="{borde}"/></w:pBdr>')
    if fondo:
        pr.append(f'<w:shd w:val="clear" w:fill="{fondo}"/>')
    pr.append(f'<w:spacing w:before="{antes}" w:after="{despues}"/>')
    if sangria:
        pr.append(f'<w:ind w:left="{sangria}"/>')
    if jc:
        pr.append(f'<w:jc w:val="{jc}"/>')
    return f'<w:p><w:pPr>{"".join(pr)}</w:pPr>{contenido}</w:p>'


NUMERO = re.compile(r"^\**-?[\d.]+(,\d+)?( %)?\**$")


def tabla(filas):
    ncol = max(len(f) for f in filas)
    # ancho de cada columna según su texto más largo, con un mínimo
    largo = [max(4, max(len(re.sub(r"\*\*", "", f[c])) if c < len(f) else 0 for f in filas))
             for c in range(ncol)]
    largo = [min(x, 60) for x in largo]
    total = sum(largo)
    anchos = [max(700, int(ANCHO_TEXTO * x / total)) for x in largo]
    ajuste = ANCHO_TEXTO - sum(anchos)
    anchos[max(range(ncol), key=lambda c: anchos[c])] += ajuste
    bordes = "<w:tblBorders>" + "".join(
        f'<w:{x} w:val="single" w:sz="4" w:space="0" w:color="{FILETE}"/>'
        for x in ("top", "bottom", "insideH")) + "</w:tblBorders>"
    # orden del esquema (CT_TblPr): tblW, tblBorders, tblLayout, tblCellMar
    out = [f'<w:tbl><w:tblPr><w:tblW w:w="{ANCHO_TEXTO}" w:type="dxa"/>'
           f'{bordes}<w:tblLayout w:type="fixed"/><w:tblCellMar><w:top w:w="40" w:type="dxa"/><w:left w:w="80" w:type="dxa"/>'
           '<w:bottom w:w="40" w:type="dxa"/><w:right w:w="80" w:type="dxa"/></w:tblCellMar></w:tblPr>'
           "<w:tblGrid>" + "".join(f'<w:gridCol w:w="{a}"/>' for a in anchos) + "</w:tblGrid>"]
    for n, fila in enumerate(filas):
        cab = n == 0
        trpr = "<w:trPr><w:tblHeader/><w:cantSplit/></w:trPr>" if cab else "<w:trPr><w:cantSplit/></w:trPr>"
        celdas = []
        for c in range(ncol):
            texto = fila[c] if c < len(fila) else ""
            fondo = f'<w:shd w:val="clear" w:fill="{GRIS}"/>' if cab else ""
            jc = "right" if (not cab and NUMERO.match(texto.strip())) else None
            cuerpo = runs(texto, sz=9.5, negrita=cab, fuente=SANS) or run(" ", sz=9.5)
            celdas.append(f'<w:tc><w:tcPr><w:tcW w:w="{anchos[c]}" w:type="dxa"/>{fondo}</w:tcPr>'
                          f"{para(cuerpo, antes=0, despues=0, jc=jc)}</w:tc>")
        out.append(f"<w:tr>{trpr}{''.join(celdas)}</w:tr>")
    return "".join(out) + "</w:tbl>" + para("", despues=120)


def indice(titulos):
    """Campo de índice (TOC) con los títulos ya escritos. Word lo actualiza
    con los números de página al abrir el archivo (updateFields)."""
    inicio = ('<w:p><w:pPr><w:pStyle w:val="TDC1"/></w:pPr>'
              '<w:r><w:fldChar w:fldCharType="begin"/></w:r>'
              '<w:r><w:instrText xml:space="preserve"> TOC \\o "1-3" \\h \\z \\u </w:instrText></w:r>'
              '<w:r><w:fldChar w:fldCharType="separate"/></w:r>')
    lineas = []
    for k, (nivel, texto) in enumerate(titulos):
        cont = run(texto)
        if k == 0:
            lineas.append(inicio + cont + "</w:p>")
        else:
            lineas.append(f'<w:p><w:pPr><w:pStyle w:val="TDC{nivel}"/></w:pPr>{cont}</w:p>')
    if not lineas:
        lineas.append(inicio + "</w:p>")
    lineas.append('<w:p><w:r><w:fldChar w:fldCharType="end"/></w:r></w:p>')
    return "".join(lineas)


def convertir(md):
    lineas = md.split("\n")
    cuerpo, titulos, i = [], [], 0
    for l in lineas:
        m = re.match(r"^(#{2,4})\s+(.*)", l.strip())
        if m:
            titulos.append((len(m.group(1)) - 1, re.sub(r"\*\*", "", m.group(2))))
    indice_puesto = False
    while i < len(lineas):
        ln = lineas[i]
        st = ln.strip()
        if st.startswith("|") and st.endswith("|"):
            buf = []
            while i < len(lineas) and lineas[i].strip().startswith("|"):
                buf.append(lineas[i])
                i += 1
            filas = []
            for x in buf:
                cs = [c.strip().replace("\\|", "|") for c in re.split(r"(?<!\\)\|", x.strip()[1:-1])]
                if all(re.fullmatch(r":?-{2,}:?", c) for c in cs if c):
                    continue
                filas.append(cs)
            if filas:
                cuerpo.append(tabla(filas))
            continue
        if st.startswith(">"):
            buf = []
            while i < len(lineas) and lineas[i].strip().startswith(">"):
                buf.append(re.sub(r"^\s*>\s?", "", lineas[i]))
                i += 1
            parrafos = " ".join(x.strip() if x.strip() else "\n" for x in buf).split("\n")
            for p in parrafos:
                if p.strip():
                    txt = re.sub(r"^- ", "• ", p.strip())
                    cuerpo.append(para(runs(txt, sz=10.5, fuente=SANS), fondo="F4F7FA",
                                       borde=TURQUESA, antes=0, despues=60, sangria=160))
            cuerpo.append(para("", despues=60))
            continue
        if not st:
            i += 1
            continue
        m = re.match(r"^(#{1,4})\s+(.*)", st)
        if m:
            nivel, texto = len(m.group(1)), m.group(2)
            if nivel == 1:
                cuerpo.append(para(runs(texto), estilo="Titulo", despues=160, seguir=True))
            else:
                if not indice_puesto:
                    cuerpo.append(para(run("Índice"), estilo="Titulo2", despues=120))
                    cuerpo.append(indice(titulos))
                    cuerpo.append('<w:p><w:r><w:br w:type="page"/></w:r></w:p>')
                    indice_puesto = True
                cuerpo.append(para(runs(texto), estilo=f"Titulo{nivel - 1}N", seguir=True,
                                   antes=[0, 0, 280, 220, 180][nivel], despues=[0, 0, 120, 100, 80][nivel]))
            i += 1
            continue
        m = re.match(r"^(\s*)([-*+]|\d+\.)\s+(.*)", ln)
        if m:
            marca = "•  " if not m.group(2)[0].isdigit() else m.group(2) + "  "
            cuerpo.append(para(run(marca) + runs(m.group(3)), sangria=340, despues=60))
            i += 1
            continue
        buf = [st]
        i += 1
        while i < len(lineas) and lineas[i].strip() and \
                not re.match(r"^\s*([#>|]|[-*+]\s|\d+\.\s)", lineas[i]):
            buf.append(lineas[i].strip())
            i += 1
        cuerpo.append(para(runs(" ".join(buf)), despues=120))
    return "".join(cuerpo)


def estilos():
    def titulo(id_, nombre, nivel, sz, color):
        return (f'<w:style w:type="paragraph" w:styleId="{id_}"><w:name w:val="{nombre}"/>'
                f'<w:basedOn w:val="Normal"/><w:next w:val="Normal"/><w:qFormat/>'
                f'<w:pPr><w:keepNext/><w:outlineLvl w:val="{nivel}"/></w:pPr>'
                f'<w:rPr><w:rFonts w:ascii="{SANS}" w:hAnsi="{SANS}" w:cs="{SANS}"/><w:b/>'
                f'<w:sz w:val="{sz}"/><w:color w:val="{color}"/></w:rPr></w:style>')

    def tdc(n):
        return (f'<w:style w:type="paragraph" w:styleId="TDC{n}"><w:name w:val="toc {n}"/>'
                f'<w:basedOn w:val="Normal"/><w:pPr><w:spacing w:after="40"/>'
                f'<w:ind w:left="{(n - 1) * 360}"/></w:pPr>'
                f'<w:rPr><w:rFonts w:ascii="{SANS}" w:hAnsi="{SANS}"/><w:sz w:val="20"/></w:rPr></w:style>')
    return ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            f'<w:styles {NS}><w:docDefaults><w:rPrDefault><w:rPr>'
            f'<w:rFonts w:ascii="{SERIF}" w:hAnsi="{SERIF}" w:cs="{SERIF}"/>'
            f'<w:color w:val="{TINTA}"/><w:sz w:val="22"/><w:szCs w:val="22"/><w:lang w:val="es-CL"/>'
            '</w:rPr></w:rPrDefault><w:pPrDefault><w:pPr><w:spacing w:after="120" w:line="290" '
            'w:lineRule="auto"/></w:pPr></w:pPrDefault></w:docDefaults>'
            '<w:style w:type="paragraph" w:default="1" w:styleId="Normal"><w:name w:val="Normal"/></w:style>'
            + titulo("Titulo", "Title", 0, 40, MARINO)
            + titulo("Titulo2", "Subtitle", 9, 28, MARINO)
            + titulo("Titulo1N", "heading 1", 0, 34, MARINO)
            + titulo("Titulo2N", "heading 2", 1, 27, MARINO)
            + titulo("Titulo3N", "heading 3", 2, 23, TINTA)
            + tdc(1) + tdc(2) + tdc(3) + "</w:styles>")


def pie(texto):
    return (f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?><w:ftr {NS}>'
            f'<w:p><w:pPr><w:pBdr><w:top w:val="single" w:sz="4" w:space="6" w:color="{FILETE}"/></w:pBdr>'
            f'<w:tabs><w:tab w:val="right" w:pos="{ANCHO_TEXTO}"/></w:tabs><w:spacing w:after="0"/></w:pPr>'
            + run(texto, sz=9, color=SECUNDARIO, fuente=SANS)
            + f'<w:r><w:rPr><w:rFonts w:ascii="{SANS}" w:hAnsi="{SANS}"/><w:sz w:val="18"/></w:rPr><w:tab/>'
              '<w:t xml:space="preserve">Folio </w:t></w:r>'
            + f'<w:r><w:rPr><w:rFonts w:ascii="{SANS}" w:hAnsi="{SANS}"/><w:b/>'
              f'<w:color w:val="{MARINO}"/><w:sz w:val="24"/></w:rPr><w:fldChar w:fldCharType="begin"/></w:r>'
              '<w:r><w:instrText xml:space="preserve"> PAGE </w:instrText></w:r>'
              '<w:r><w:fldChar w:fldCharType="separate"/></w:r>'
            + f'<w:r><w:rPr><w:b/><w:color w:val="{MARINO}"/><w:sz w:val="24"/></w:rPr><w:t>1</w:t></w:r>'
              '<w:r><w:fldChar w:fldCharType="end"/></w:r></w:p></w:ftr>')


def construir(md, salida, titulo, texto_pie, folio=1):
    md = md.replace("️", "")
    sect = ('<w:sectPr><w:footerReference w:type="default" r:id="rId3"/>'
            '<w:pgSz w:w="12240" w:h="15840"/>'
            '<w:pgMar w:top="1134" w:right="1134" w:bottom="1134" w:left="1701" '
            'w:header="567" w:footer="454" w:gutter="0"/>'
            f'<w:pgNumType w:start="{int(folio)}"/></w:sectPr>')
    doc = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
           f'<w:document {NS}><w:body>{convertir(md)}{sect}</w:body></w:document>')
    R = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
    P = "http://schemas.openxmlformats.org/package/2006/relationships"
    partes = {
        "[Content_Types].xml": '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
        '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
        '<Default Extension="xml" ContentType="application/xml"/>'
        '<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>'
        '<Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>'
        '<Override PartName="/word/settings.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.settings+xml"/>'
        '<Override PartName="/word/footer1.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.footer+xml"/>'
        '<Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/></Types>',
        "_rels/.rels": '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        f'<Relationships xmlns="{P}">'
        f'<Relationship Id="rId1" Type="{R}/officeDocument" Target="word/document.xml"/>'
        '<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/></Relationships>',
        "word/_rels/document.xml.rels": '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        f'<Relationships xmlns="{P}">'
        f'<Relationship Id="rId1" Type="{R}/styles" Target="styles.xml"/>'
        f'<Relationship Id="rId2" Type="{R}/settings" Target="settings.xml"/>'
        f'<Relationship Id="rId3" Type="{R}/footer" Target="footer1.xml"/></Relationships>',
        "word/document.xml": doc,
        "word/styles.xml": estilos(),
        "word/settings.xml": '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        f'<w:settings {NS}><w:defaultTabStop w:val="708"/>'
        '<w:characterSpacingControl w:val="doNotCompress"/><w:updateFields w:val="true"/></w:settings>',
        "word/footer1.xml": pie(texto_pie),
        "docProps/core.xml": '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" '
        'xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" '
        'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">'
        f'<dc:title>{E(titulo)}</dc:title><dc:creator>audIT</dc:creator>'
        '<cp:revision>1</cp:revision></cp:coreProperties>',
    }
    with zipfile.ZipFile(salida, "w", zipfile.ZIP_DEFLATED) as z:
        for nombre, contenido in partes.items():
            z.writestr(nombre, contenido)
    return salida


if __name__ == "__main__":
    if len(sys.argv) < 5:
        print(__doc__)
        sys.exit(2)
    md = open(sys.argv[1], encoding="utf-8").read()
    folio = int(sys.argv[5]) if len(sys.argv) > 5 else 1
    print(construir(md, sys.argv[2], sys.argv[3], sys.argv[4], folio))
