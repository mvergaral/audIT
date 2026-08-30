#!/usr/bin/env python3
"""Convierte una página escaneada en Markdown conservando la estructura de tablas.

Las tablas de estas bases están completamente enrejadas, así que la estructura se
recupera de los propios filetes en vez de adivinarla desde la posición del texto.

Detalle importante: se trabajan DOS binarizaciones de la misma página.

  - `grid` (umbral suave, 200): conserva los filetes gris claro de las tablas, que
    el umbral duro borraría junto con la marca de agua. La marca "CONFIDENCIAL" es
    diagonal, así que nunca produce corridas horizontales o verticales largas y no
    contamina la detección de rejilla.
  - `ocr` (umbral duro, 153 sobre el canal mínimo): elimina la marca de agua por
    completo y es la imagen que se le pasa a tesseract.

El canal mínimo de RGB (en vez del gris de luminancia) es lo que permite que el
umbral duro conserve los títulos dorados: para el dorado el canal azul es casi
negro, mientras que la marca de agua es gris neutro y desaparece entera.

Flujo: se ubican los filetes, se clasifican las franjas entre ellos en tabla /
banda rellena / prosa, se recorre la página de arriba abajo y se emite cada bloque
en orden de lectura. Se llama a tesseract UNA vez por bloque (no por celda),
pidiendo TSV, y cada palabra se asigna a su celda por el centroide de su bbox:
es ~40x más rápido que recortar celda por celda y da el mismo resultado.
"""

import csv
import io
import re
import subprocess
import sys

import numpy as np
from PIL import Image

GRID_TH = 200         # umbral suave: detección de filetes
OCR_TH = 153          # umbral duro (60%): borra la marca de agua
RULE_MAX_THICK = 10   # px: más grueso que esto no es filete sino banda rellena
H_RULE_FRAC = 0.62    # cobertura mínima del ancho para un filete horizontal
V_RULE_FRAC = 0.75    # cobertura mínima del alto de la franja para uno vertical
MIN_STRIP = 15        # px: altura mínima de una fila de tabla
MARGIN_FRAC = 0.045   # se descartan las cornisas (encabezado y pie de página)


def runs(mask):
    """[(inicio, fin_exclusivo)] de las corridas de True en un vector booleano."""
    out, start = [], None
    for i, v in enumerate(mask):
        if v and start is None:
            start = i
        elif not v and start is not None:
            out.append((start, i))
            start = None
    if start is not None:
        out.append((start, len(mask)))
    return out


def find_rules(profile, need):
    """Filetes a partir de un perfil de proyección.

    Una corrida delgada aporta un filete en su centro. Una gruesa es una banda
    rellena (la cabecera oscura de la tabla) y aporta un filete en cada borde, para
    que su texto blanco sobre fondo oscuro quede en una celda propia y no se pierda.
    """
    # Se cierran los huecos pequeños antes de clasificar: en la cabecera oscura de
    # una tabla, las letras blancas recortan la banda a la altura de la equis y la
    # cobertura cae bajo el umbral, partiendo una sola banda en varias corridas.
    merged = []
    for a, b in runs(profile > need):
        if merged and a - merged[-1][1] <= 15:
            merged[-1][1] = b
        else:
            merged.append([a, b])

    out = []
    for a, b in merged:
        if b - a <= RULE_MAX_THICK:
            out.append((a + b) // 2)
        else:
            out.extend((a, b))
    return sorted(set(out))


def vrules(grid, y0, y1):
    """Filetes verticales de una franja. None si la franja está rellena de tinta."""
    band = grid[y0:y1, :]
    h, w = band.shape
    if h < MIN_STRIP:
        return None
    if band.mean() > 0.5:
        # Banda rellena de tinta (la cabecera oscura): los huecos entre las letras
        # blancas simularían filetes verticales, así que aquí no se decide nada.
        return None
    return find_rules(band.sum(axis=0), V_RULE_FRAC * h)


def consensus(lists, tol=12, frac=0.55):
    """Columnas presentes en al menos `frac` de las franjas.

    Se cuentan franjas distintas y no posiciones sueltas: una franja ruidosa puede
    aportar varios filetes falsos muy juntos, y contarlos por separado los haría
    pasar el corte como si fueran una columna real.
    """
    flat = sorted((p, i) for i, lst in enumerate(lists) for p in lst)
    clusters, cur = [], []
    for p, i in flat:
        if cur and p - cur[-1][0] > tol:
            clusters.append(cur)
            cur = []
        cur.append((p, i))
    if cur:
        clusters.append(cur)
    need = max(1, frac * len(lists))
    return sorted({int(np.median([p for p, _ in c])) for c in clusters
                   if len({i for _, i in c}) >= need})


def ocr_tsv(arr, lang, psm, pad=0):
    """Corre tesseract sobre un recorte y devuelve las palabras con su bbox.

    `pad` agrega margen blanco: sin él tesseract descarta los recortes muy anchos
    y bajos, como la banda de cabecera de una tabla.
    """
    if pad:
        p = np.full((arr.shape[0] + 2 * pad, arr.shape[1] + 2 * pad), 255, np.uint8)
        p[pad:-pad, pad:-pad] = arr
        arr = p
    buf = io.BytesIO()
    Image.fromarray(arr).save(buf, format="PNG")
    res = subprocess.run(
        ["tesseract", "stdin", "stdout", "-l", lang, "--oem", "1",
         "--psm", str(psm), "tsv"],
        input=buf.getvalue(), capture_output=True,
    )
    words = []
    for r in csv.DictReader(io.StringIO(res.stdout.decode("utf-8", "replace")),
                            delimiter="\t", quoting=csv.QUOTE_NONE):
        try:
            if int(r["level"]) != 5:
                continue
            txt = (r["text"] or "").strip()
            if not txt or float(r["conf"]) < 0:
                continue
            words.append({"text": txt, "x": int(r["left"]), "y": int(r["top"]),
                          "w": int(r["width"]), "h": int(r["height"]),
                          "par": (int(r["block_num"]), int(r["par_num"])),
                          "line": int(r["line_num"]),
                          "conf": float(r["conf"])})
        except (ValueError, TypeError, KeyError):
            continue
    return words


def in_reading_order(words):
    """Ordena palabras en orden de lectura agrupándolas primero en renglones.

    Ordenar por `y` crudo entrelaza palabras del mismo renglón, porque sus cajas
    diferen en unos pocos píxeles; hay que agrupar por banda antes de ordenar por x.
    """
    if not words:
        return ""
    hh = float(np.median([w["h"] for w in words])) or 1.0
    lines, cur, base = [], [], None
    for w in sorted(words, key=lambda w: w["y"]):
        if base is None or abs(w["y"] - base) <= hh * 0.6:
            base = w["y"] if base is None else base
            cur.append(w)
        else:
            lines.append(cur)
            cur, base = [w], w["y"]
    if cur:
        lines.append(cur)
    return " ".join(" ".join(w["text"] for w in sorted(ln, key=lambda w: w["x"]))
                    for ln in lines)


# El signo ordinal de "Artículo 32°" es diminuto y tesseract lo lee como comilla,
# asterisco o porcentaje. Subir la resolución no ayuda: el modelo de lenguaje no
# espera un grado tras un dígito. Se corrige después, con reglas verificadas
# contra el corpus completo para no tocar los porcentajes reales (los pesos de
# evaluación se escriben "17%" y son legítimos).
ORD_MARK = re.compile(r"(\d)[*\"\u201d\u201c'\u2019]")
# re.I porque los títulos van en mayúscula ("ARTÍCULO 2%."): son la mitad
# de los casos y son justamente los que sirven para indexar el documento.
ORD_ART = re.compile(r"\b(Art\.|Art[íi]culos?)(\s+\d+)%", re.I)
ORD_RANGE = re.compile(r"(\d)([%\u00b0])(\s*[\u2014\u2013-]\s*\d+)([%\u00b0])")

# La arroba se lee como "E" suelta entre el usuario y el dominio.
# La sigla del ramo, ICI-5444, sale como "1C1-5444" o "1CI1-5444": la I y el 1
# son casi idénticos en esta tipografía. Comprobado sobre el corpus completo,
# el patrón no coincide con ningún otro código de los documentos (TFEP-01-2026,
# FEP01.26, T-22, A-6 tienen otra forma).
# El mismo signo tras la "N" de "Ley N°", "Sobre N°", "Licitación N°". Sin
# condición sobre lo que sigue: las 96 apariciones del corpus son todas el signo
# de número, y una "N" seguida de comilla no ocurre de otra forma.
NUM_SIGN = re.compile(r"\bN[*\"\u201d\u201c'\u2019]")

COURSE = re.compile(r"\b[1Il|]\s?[CGO]\s?[1IlL|]{1,2}\s?-\s?(\d{4})\b")

AT_SIGN = re.compile(r"(\w)\s+E\s+(\w+\.(?:cl|com|org|net))\b")

# La misma confusión I/1 en las referencias a normas: "ISO/IEC 27017" sale como
# "ISO/1EC", y "ISO 22301" como "1SO 22301".
NORMA = re.compile(r"\b1SO\b|[!¡]?1EC\b")

# El ordinal femenino de "APA 7.ª edición" se lee como un 2: "APA 7.2 edición".
ORD_FEM = re.compile(r"\b(\d)\.2(\s+(?:ed\.|edici[óo]n))", re.I)

ROMAN = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X",
         "XI", "XII", "XIII", "XIV", "XV", "XVI", "XVII", "XVIII", "XIX", "XX"]
# El separador es un punto medio en el original, y el OCR lo devuelve como '-',
# ':', '+', '.' o casi cualquier signo, así que se acepta cualquier puntuación.
CELL_ROMAN = re.compile(r"^\s*([IVXlL|]{1,6})\s*[^\w\s]\s*\S")
ART_COL = re.compile(r"^\s*art[ií]culos?\s*$", re.I)


def normalize(text):
    """Reglas de corrección de OCR verificadas contra todo el corpus."""
    text = ORD_MARK.sub(r"\1°", text)
    text = ORD_ART.sub(r"\1\2°", text)
    text = AT_SIGN.sub(r"\1@\2", text)
    text = COURSE.sub(r"ICI-\1", text)
    text = NUM_SIGN.sub("N°", text)
    text = NORMA.sub(lambda m: "ISO" if "S" in m.group(0) else "IEC", text)
    text = ORD_FEM.sub(r"\1.ª\2", text)
    # En un rango, si un extremo quedó como grado el otro también lo es.
    for _ in range(2):
        text = ORD_RANGE.sub(
            lambda m: m.group(1) + "\u00b0" + m.group(3) + "\u00b0"
            if "\u00b0" in (m.group(2), m.group(4)) else m.group(0), text)
    return text


def fix_columns(grid):
    """Repara la columna de romanos y la de artículos de un índice de contenidos.

    El OCR confunde 'I' con '|', 'l' o 'L', y pierde trazos ('VIII' sale 'VII').
    Cuando una columna entera es la secuencia I, II, III..., la propia secuencia
    dice cuál debía ser cada valor, y se repara contra ella. Solo se aplica si la
    mayoría de los valores ya coincide, para no inventar numeración donde no la hay.
    """
    for c in range(len(grid[0])):
        body = [r for r in grid[1:] if c < len(r)]
        if ART_COL.match(grid[0][c]):
            for r in body:
                r[c] = ORD_MARK.sub("\\1°",
                                    re.sub(r"(\d)%", "\\1°", r[c]))
            continue
        ms = [CELL_ROMAN.match(r[c]) for r in body]
        if len(body) < 3 or not all(ms):
            continue
        got = [m.group(1).upper().replace("|", "I").replace("L", "I") for m in ms]
        want = ROMAN[1:len(body) + 1]
        if sum(g == w for g, w in zip(got, want)) < 0.6 * len(body):
            continue
        for r, m, w in zip(body, ms, want):
            r[c] = w + r[c][m.end(1):]
    return grid


def cell_text(ocr, y0, y1, x0, x1, lang):
    """OCR de una celda aislada.

    Se recorta celda por celda en vez de leer la banda entera de una vez porque
    tesseract, sobre la tabla completa, o inventa caracteres sueltos entre las
    columnas (psm 6) o descarta las celdas de un solo dígito (psm 11). Aislada,
    cada celda se lee limpia. Cuesta una invocación por celda, pero solo en las
    páginas que traen tablas.
    """
    crop = ocr[y0 + 3:y1 - 3, x0 + 3:x1 - 3]
    if crop.size == 0:
        return ""
    ink = (crop < 128).mean()
    if ink < 0.002:
        return ""                       # celda vacía: no vale la pena invocar OCR
    if ink > 0.5:
        crop = 255 - crop               # cabecera oscura: texto blanco sobre tinta
    for psm in (6, 11, 7):
        words = ocr_tsv(crop, lang, psm, pad=25)
        if words:
            return in_reading_order(words)
    return ""


def render_table(ocr, hr, vr, lang):
    nrow, ncol = len(hr) - 1, len(vr) - 1
    grid = [[cell_text(ocr, hr[r], hr[r + 1], vr[c], vr[c + 1], lang)
             for c in range(ncol)] for r in range(nrow)]
    grid = [[normalize(c) for c in row] for row in grid
            if any(c.strip() for c in row)]
    if not grid:
        return ""
    if len(grid) > 1:
        grid = fix_columns(grid)
    # El escape de la barra va al final: antes, un 'I' romano leído como '|' se
    # convertiría en '\\|' y fix_columns ya no lo reconocería.
    grid = [[c.replace("|", "\\|") for c in row] for row in grid]

    # Una sola columna no es una tabla: es un recuadro destacado.
    if ncol == 1:
        body = " ".join(r[0] for r in grid).strip()
        # Un recuadro de una sola columna es el título de un formulario o sección,
        # no una cita destacada, cuando el texto es corto o cuando se identifica
        # como encabezado por sí mismo (el de un formulario puede pasar de 80
        # caracteres y aun así ser un título).
        titulo = (CAP.match(body) and body == body.upper()) or (
            len(body) < 80 and not body.endswith("."))
        return f"### {body}\n" if titulo else f"> {body}\n"

    out = ["| " + " | ".join(grid[0]) + " |",
           "| " + " | ".join("---" for _ in grid[0]) + " |"]
    out += ["| " + " | ".join(row) + " |" for row in grid[1:]]
    return "\n".join(out) + "\n"


ART = re.compile(r"^(ART[IÍ]CULO|ANEXO|AP[EÉ]NDICE)\s", re.I)
SUBSEC = re.compile(r"^\d+(\.\d+)+\s+\S")
CAP = re.compile(r"^(?:CAP[IÍ]TULO\s+[0-9IVX]+|FORMULARIO\s+[A-Z]+-?\d+)\b", re.I)


def group_lines(words):
    """Agrupa palabras en renglones por su posición vertical.

    No se usa la numeración de bloques y párrafos de tesseract: sobre estas
    páginas parte un mismo listado en bloques distintos y junta viñetas que no
    tienen relación. La geometría es más fiable.
    """
    if not words:
        return []
    hh = float(np.median([w["h"] for w in words])) or 1.0
    out, cur, base = [], [], None
    for w in sorted(words, key=lambda w: w["y"]):
        if base is not None and w["y"] - base > hh * 0.6:
            out.append(cur)
            cur = []
            base = None
        if base is None:
            base = w["y"]
        cur.append(w)
    if cur:
        out.append(cur)

    lines = []
    for ws in out:
        ws = sorted(ws, key=lambda w: w["x"])
        lines.append({
            "words": ws,
            "text": " ".join(w["text"] for w in ws).strip(),
            "left": ws[0]["x"],
            "right": max(w["x"] + w["w"] for w in ws),
            "top": min(w["y"] for w in ws),
            "h": float(np.median([w["h"] for w in ws])),
        })
    return [ln for ln in lines if ln["text"]]


def render_prose(ocr, y0, y1, lang):
    lines = group_lines(ocr_tsv(ocr[y0:y1, :], lang, 3))
    if not lines:
        return ""

    body_h = float(np.median([ln["h"] for ln in lines]))
    lines = [ln for ln in lines if ln["h"] > body_h * 0.45]   # descarta fragmentos
    if not lines:
        return ""

    # Márgenes reales del cuerpo de texto, medidos sobre la propia página.
    body_left = float(np.percentile([ln["left"] for ln in lines], 10))
    right_edge = float(np.percentile([ln["right"] for ln in lines], 90))
    gaps = [b["top"] - a["top"] for a, b in zip(lines, lines[1:])]
    pitch = float(np.median(gaps)) if gaps else body_h * 1.6

    # Barras verticales decorativas del margen (los bloques de entrevistas las
    # llevan). Sin descontarlas, la sonda de viñetas encuentra tinta en el margen
    # de TODOS los renglones y parte el bloque en un ítem por línea.
    gut0, gut1 = max(int(body_left) - 12, 0), int(body_left + body_h * 2.6)
    bar_cols = set()
    for x in range(gut0, min(gut1, ocr.shape[1])):
        col = ocr[y0:y1, x] < 128
        if any(b - a > body_h * 4 for a, b in runs(col)):
            bar_cols.add(x)

    def has_marker(ln):
        """¿Hay tinta en el margen, a la izquierda del texto de este renglón?

        La viñeta casi nunca sobrevive al OCR, pero sí está en la imagen. Como el
        ítem y sus renglones de continuación arrancan exactamente en la misma
        sangría, el glifo en el margen es la única señal de dónde empieza un ítem
        nuevo: sin él, un ítem de un solo renglón que llega al margen derecho es
        indistinguible de la continuación del anterior.
        """
        x0, x1 = int(body_left) - 4, ln["left"] - 6
        cols = [x for x in range(max(x0, 0), max(x1, 0)) if x not in bar_cols]
        if len(cols) < 4:
            return False
        a = y0 + ln["top"] - int(body_h * 0.3)
        b = y0 + ln["top"] + int(body_h * 1.2)
        return int((ocr[max(a, 0):b, cols] < 128).sum()) > body_h * 0.4

    def in_bar(ln):
        """¿Este renglón va junto a una barra vertical de margen?"""
        if not bar_cols:
            return False
        a = y0 + ln["top"]
        b = a + int(body_h)
        return int((ocr[a:b, sorted(bar_cols)] < 128).sum()) > body_h * 0.5

    def marker_word(ln):
        """¿El primer token del renglón es un glifo de viñeta leído como palabra?"""
        ws = ln["words"]
        if len(ws) < 2 or len(ws[0]["text"]) > 2:
            return False
        # Hacen falta las dos condiciones. El hueco solo no basta: el texto
        # justificado estira los espacios y un "El" inicial llega a separarse
        # tanto como una viñeta. Pero el glifo además es bajo (mide medio cuerpo
        # de texto), y ninguna palabra real lo es.
        gap = ws[1]["x"] - (ws[0]["x"] + ws[0]["w"])
        return ws[0]["h"] < body_h * 0.6 and gap > body_h * 0.75

    def kind_of(ln):
        t = ln["text"]
        # Los encabezados de capítulo y de formulario no siempre se componen
        # más grandes que el cuerpo, así que la prueba de altura se le escapa a
        # la mitad de ellos. El texto sí es inequívoco, siempre que se exija
        # además la caja alta: en prosa aparecen menciones como "Formulario A-1:
        # Identificación del Proponente", que no son encabezados.
        if CAP.match(t) and t == t.upper():
            return "h3"
        if ART.match(t):
            return "h2"
        short = len(t) < 90 and not t.endswith(".")
        if ln["h"] > body_h * 1.15 and short:
            return "h3"
        if SUBSEC.match(t) and len(t) < 70 and not t.endswith("."):
            return "h3"
        # Hay dos estilos de lista en estos documentos. Uno con sangría francesa,
        # donde el glifo cae en el margen y el OCR lo descarta: ahí la viñeta se
        # detecta buscando tinta en el margen. Otro sin sangría, donde el glifo
        # queda dentro del renglón y el OCR sí lo lee, mal, como "e", "*" o "©":
        # ahí se reconoce por ser un token muy corto separado del texto por un
        # hueco mayor que un espacio normal.
        if marker_word(ln):
            return "item"
        # La sangría sola no basta: los bloques de entrevistas también van
        # sangrados y no son listas.
        if ln["left"] > body_left + body_h * 0.7:
            return "item" if has_marker(ln) else "quote"
        return "body"

    blocks, cur = [], []
    for i, ln in enumerate(lines):
        k = kind_of(ln)
        prev = lines[i - 1] if i else None
        # Un párrafo justificado llega siempre al margen derecho: si el renglón
        # anterior quedó corto, es que ahí terminaba el párrafo. La holgura es
        # amplia porque el justificado deja el margen irregular en varias decenas
        # de píxeles, y un corte estrecho parte los ítems largos en dos.
        was_item = cur[0][0] == "item" if cur else False
        if k == "quote" and was_item:
            k = "item"                      # continuación de la viñeta anterior
        if k == "item" and was_item:
            # Manda el glifo, esté en el margen (lista con sangría francesa) o
            # dentro del renglón (lista sin sangría).
            broke = has_marker(ln) or marker_word(ln)
        else:
            broke = (prev is None
                     or k in ("h2", "h3")
                     or (cur and cur[0][0] in ("h2", "h3"))
                     or prev["right"] < right_edge - body_h * 2.5
                     or ln["top"] - prev["top"] > pitch * 1.55
                     or (k in ("item", "quote")) != (was_item or
                         (cur[0][0] == "quote" if cur else False)))
        if broke and cur:
            blocks.append(cur)
            cur = []
        cur.append((k, ln))
    if cur:
        blocks.append(cur)

    def strip_marker(ln):
        """Quita el glifo de viñeta cuando el OCR sí lo leyó (como '*', 'e', 'EP').

        Se reconoce por geometría y no por el carácter: es un token muy corto,
        separado del texto por un hueco mayor que el espacio entre palabras.
        """
        if marker_word(ln):
            return " ".join(w["text"] for w in ln["words"][1:]).strip()
        return ln["text"]

    out = []
    for blk in blocks:
        k = blk[0][0]
        parts = [strip_marker(ln) if k == "item" and i == 0 else ln["text"]
                 for i, (_, ln) in enumerate(blk)]
        text = " ".join(parts).strip()
        text = normalize(text)
        if k == "h2":
            out.append("## " + text)
        elif k == "h3":
            out.append("### " + text)
        elif k == "item":
            out.append("- " + text)
        elif k == "quote":
            out.append(("> " if in_bar(blk[0][1]) else "") + text)
        else:
            out.append(text)
    text = ""
    for i, chunk in enumerate(x for x in out if x):
        if i and not (text.endswith("\n") and chunk.startswith("- ")
                      and text.rstrip("\n").split("\n")[-1].startswith("- ")):
            text += "\n"
        text += chunk + "\n"
    return text


PIE = re.compile(r"(\d+)\s*/\s*(\d+)")


def pagina_impresa(ocr, lang):
    """Número de página impreso en el pie, que es el que se cita.

    No coincide con el número de página del PDF: en estos tres documentos la
    portada no va numerada, así que el impreso es siempre uno menos. Se lee del
    pie en vez de asumir el desfase, para que la cita sea verificable.
    Se toma la ÚLTIMA fracción del renglón: antes viene "TFEP-01/2026".
    """
    pie = ocr[int(ocr.shape[0] * (1 - MARGIN_FRAC)):, :]
    txt = " ".join(w["text"] for w in ocr_tsv(pie, lang, 11, pad=25))
    ms = PIE.findall(txt)
    return f"{ms[-1][0]}/{ms[-1][1]}" if ms else ""


def page_to_md(path, lang="spa"):
    mn = np.array(Image.open(path).convert("RGB")).min(axis=2)
    H, W = mn.shape
    grid = mn < GRID_TH
    ocr = np.where(mn < OCR_TH, 0, 255).astype(np.uint8)

    top, bot = int(H * MARGIN_FRAC), int(H * (1 - MARGIN_FRAC))
    hr = [y for y in find_rules(grid.sum(axis=1), H_RULE_FRAC * W) if top < y < bot]

    # Cada franja entre dos filetes se clasifica: tabla, banda rellena o prosa.
    strips = []
    for a, b in zip(hr, hr[1:]):
        vr = vrules(grid, a + 2, b - 2)
        strips.append((a, b, "fill" if vr is None else
                       ("table" if len(vr) >= 2 else "prose"), vr))

    # Franjas contiguas de tabla/relleno que contengan al menos una tabla real.
    tables, i = [], 0
    while i < len(strips):
        if strips[i][2] == "table":
            j = i
            while j + 1 < len(strips) and strips[j + 1][2] in ("table", "fill"):
                j += 1
            while strips[j][2] != "table":
                j -= 1
            # hacia atrás: la cabecera oscura queda clasificada como banda rellena
            # y es una fila más de la tabla, no prosa que la precede.
            k = i
            while k - 1 >= 0 and strips[k - 1][2] == "fill":
                k -= 1
            cols = consensus([s[3] for s in strips[k:j + 1] if s[2] == "table"])
            if len(cols) >= 2:
                tables.append((strips[k][0], strips[j][1],
                               [strips[k][0]] + [s[1] for s in strips[k:j + 1]], cols))
            i = j + 1
        else:
            i += 1

    chunks, cursor = [], top
    for y0, y1, rows, cols in tables:
        if y0 - cursor > MIN_STRIP:
            chunks.append(("prose", cursor, y0, None, None))
        chunks.append(("table", y0, y1, sorted(set(rows)), cols))
        cursor = y1
    if bot - cursor > MIN_STRIP:
        chunks.append(("prose", cursor, bot, None, None))

    marca = pagina_impresa(ocr, lang)
    out = [f"<!--pag:{marca}-->"] if marca else ["<!--pag:-->"]
    for kind, y0, y1, rows, cols in chunks:
        md = (render_prose(ocr, y0, y1, lang) if kind == "prose"
              else render_table(ocr, rows, cols, lang))
        if md.strip():
            out.append(md.strip())
    return "\n\n".join(out)


if __name__ == "__main__":
    sys.stdout.write(page_to_md(sys.argv[1],
                                sys.argv[2] if len(sys.argv) > 2 else "spa"))
