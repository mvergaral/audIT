#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verifica las exigencias formales de las bases sobre los PDF y los fuentes.

  python3 herramientas/verificar.py                 todo lo que haya en salida/
  python3 herramientas/verificar.py salida/muestra-continua/manifiesto.json

Cada punto sale como CUMPLE, NO CUMPLE o AVISO, con su detalle. El informe
queda además en salida/verificacion-<grupo>.md. Sale con código 1 si algún
punto no cumple.

Mide el PDF final, no el fuente: el tamaño de cada fragmento de texto (con
PyMuPDF, ver herramientas/preparar.sh), la posición del folio en la hoja
física, las fuentes incrustadas y el texto extraíble. Del fuente revisa las
citas a figuras y tablas, los títulos seguidos de tabla o figura, los
residuos prohibidos y las reglas de escritura del equipo.
"""
import glob
import json
import math
import os
import re
import subprocess
import sys
import unicodedata

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
from comun import RAIZ, SALIDA, Config  # noqa: E402

try:
    import pymupdf
except ImportError:  # usa el entorno virtual si existe
    venv = os.path.join(AQUI, ".venv")
    if os.path.exists(os.path.join(venv, "bin", "python")) and \
            os.path.realpath(sys.prefix) != os.path.realpath(venv):
        py = os.path.join(venv, "bin", "python")
        os.execv(py, [py] + sys.argv)
    pymupdf = None

MM = 72 / 25.4
CUERPO_MIN = 11.0      # FEP01, Artículo 40.4
TABLA_MIN = 9.0
TOLERANCIA = 0.02      # redondeo de la medición

CUMPLE, NO, AVISO, NA = "CUMPLE", "NO CUMPLE", "AVISO", "NO APLICA"


# ----------------------------------------------------------------------------
class Informe:
    def __init__(self, grupo):
        self.grupo = grupo
        self.puntos = []

    def agregar(self, codigo, titulo, estado, detalle=()):
        self.puntos.append((codigo, titulo, estado, list(detalle)))

    def imprimir(self):
        print(f"\nVerificación de {self.grupo}")
        print("-" * 78)
        for codigo, titulo, estado, detalle in self.puntos:
            print(f"{estado:10s} {codigo:4s} {titulo}")
            for d in detalle[:8]:
                print(f"{'':16s}{d}")
            if len(detalle) > 8:
                print(f"{'':16s}... y {len(detalle) - 8} más (ver el informe .md)")
        n = sum(1 for p in self.puntos if p[2] == NO)
        a = sum(1 for p in self.puntos if p[2] == AVISO)
        print("-" * 78)
        print(f"{len(self.puntos)} puntos, {n} no cumplen, {a} avisos")
        return n

    def markdown(self, ruta):
        lin = [f"# Verificación de {self.grupo}", "",
               "| Estado | Punto | Detalle |", "|---|---|---|"]
        for codigo, titulo, estado, detalle in self.puntos:
            d = "<br>".join(x.replace("|", "\\|") for x in detalle[:40]) or ""
            lin.append(f"| {estado} | {codigo}. {titulo} | {d} |")
        with open(ruta, "w", encoding="utf-8") as f:
            f.write("\n".join(lin) + "\n")


# ----------------------------------------------------------------------------
#  Utilidades
# ----------------------------------------------------------------------------
def norm(s):
    s = unicodedata.normalize("NFKC", s).casefold()
    return re.sub(r"\s+", " ", s).strip()


def sin_comentarios(texto):
    return "\n".join(re.sub(r"(?<!\\)%.*$", "", l) for l in texto.split("\n"))


def fuentes_de(log_o_aux):
    """Archivos .tex del proyecto que entraron en la compilación (del .fls)."""
    fls = re.sub(r"\.(log|aux)$", ".fls", log_o_aux)
    salida = []
    try:
        for l in open(os.path.join(RAIZ, fls), encoding="utf-8", errors="replace"):
            if l.startswith("INPUT "):
                ruta = l[6:].strip()
                if not os.path.isabs(ruta):
                    ruta = os.path.join(RAIZ, ruta)
                ruta = os.path.normpath(ruta)
                if ruta.startswith(RAIZ) and ruta.endswith(".tex") and "/salida/" not in ruta:
                    salida.append(ruta)
    except OSError:
        pass
    return sorted(set(salida))


def es_contenido(ruta):
    rel = os.path.relpath(ruta, RAIZ)
    return rel.startswith(("subdocumentos/", "muestra/", "anexos/", "economico/"))


def leer(ruta):
    return open(ruta, encoding="utf-8", errors="replace").read()


def figuras_medidas(aux):
    """(archivo, escala, folio, modo, etiqueta) de cada figura, desde el .aux."""
    try:
        t = leer(os.path.join(RAIZ, aux))
    except OSError:
        return []
    return [(m.group(1), float(m.group(2)), int(m.group(3)), m.group(4), m.group(5))
            for m in re.finditer(r"\\figuraMedida\{([^}]*)\}\{([\d.]+)\}\{(\d+)\}\{([^}]*)\}\{([^}]*)\}", t)]


def cajas_figura(aux, pdfs_folio):
    """Rectángulo de cada figura en su página, en coordenadas de PyMuPDF
    (hoja física, origen arriba a la izquierda), desde \\figuraCaja y
    \\figuraMedida del .aux: {folio: [rect, ...]}."""
    try:
        t = leer(os.path.join(RAIZ, aux))
    except OSError:
        return {}
    folio = {m[4]: m[2] for m in figuras_medidas(aux)}
    salida = {}
    for m in re.finditer(r"\\figuraCaja\{([^}]*)\}\{(-?\d+)\}\{(-?\d+)\}\{([\d.]+)\}\{([\d.]+)\}", t):
        et, x, y, w, h = m.group(1), int(m.group(2)), int(m.group(3)), float(m.group(4)), float(m.group(5))
        if et not in folio:
            continue
        f = folio[et]
        alto = pdfs_folio(f)
        if alto is None:
            continue
        x0, yb = x / 65536 * 72 / 72.27, y / 65536 * 72 / 72.27
        salida.setdefault(f, []).append(pymupdf.Rect(x0, alto - yb - h, x0 + w, alto - yb))
    return salida


def en_figura(bbox, rects):
    r = pymupdf.Rect(bbox)
    c = pymupdf.Point((r.x0 + r.x1) / 2, (r.y0 + r.y1) / 2)
    return any(c in q for q in rects)


def entradas_folio(texto):
    return [m.groups() for m in re.finditer(
        r"\\entradaFolio\{([^{}]*)\}\{((?:[^{}]|\{[^{}]*\})*)\}\{(\d+)\}\{([^{}]*)\}", texto)]


# ----------------------------------------------------------------------------
#  Verificaciones sobre el PDF
# ----------------------------------------------------------------------------
class Pdf:
    def __init__(self, entrada, grupo_dir):
        self.e = entrada
        self.nombre = entrada["nombre"]
        self.ruta = os.path.join(grupo_dir, self.nombre)
        self.folio0 = entrada["folio_inicial"]
        self.doc = pymupdf.open(self.ruta) if pymupdf else None
        self.n = self.doc.page_count if self.doc else entrada.get("paginas", 0)

    def folio(self, i):
        return self.folio0 + i


def zona_folio(pagina):
    """Palabras del extremo inferior derecho de la hoja física."""
    w, h = pagina.mediabox.width, pagina.mediabox.height
    palabras = pagina.get_text("words")
    return [p for p in palabras if p[0] > w - 25 * MM and p[1] > h - 15 * MM]


def textos_visibles(pagina):
    """Fragmentos de texto con su posición y su sentido tal como se ve la
    página en pantalla, aplicando el giro (/Rotate) que declara el PDF.
    PyMuPDF entrega las coordenadas de la hoja física. Una página girada con
    pdflscape se ve apaisada, y lo que en la hoja física está abajo a la
    derecha en pantalla queda abajo a la izquierda y de costado."""
    m = pagina.rotation_matrix
    lineal = pymupdf.Matrix(m.a, m.b, m.c, m.d, 0, 0)
    salida = []
    for b in pagina.get_text("dict")["blocks"]:
        for l in b.get("lines", []):
            d = pymupdf.Point(l["dir"]) * lineal
            derecho = abs(d.x - 1) < 0.01 and abs(d.y) < 0.01
            for s in l["spans"]:
                if s["text"].strip():
                    salida.append((s["text"].strip(), pymupdf.Rect(s["bbox"]) * m, derecho))
    return salida


def folio_visible(pagina, esperado):
    """Dónde se ve el folio: abajo a la derecha y derecho, o dónde está."""
    w, h = pagina.rect.width, pagina.rect.height
    donde = []
    for texto, r, derecho in textos_visibles(pagina):
        if texto != esperado:
            continue
        abajo, derecha = r.y0 > h - 20 * MM, r.x0 > w - 25 * MM
        if r.y0 > h - 15 * MM and derecha and derecho:
            return True, []
        if abajo or r.y0 > h - 40 * MM:
            donde.append(("abajo" if abajo else "cerca del pie") + " a la "
                         + ("derecha" if derecha else "izquierda")
                         + ("" if derecho else ", de costado"))
    return False, donde


def folio_en_cabeza(pagina):
    """«Folio N» repetido en la cabeza de la página tal como se ve."""
    m = pagina.rotation_matrix
    for b in pagina.get_text("dict")["blocks"]:
        for l in b.get("lines", []):
            r = pymupdf.Rect(l["bbox"]) * m
            texto = " ".join(s["text"] for s in l["spans"])
            if r.y0 < 25 * MM and re.search(r"\bFolio\s+\d+", texto):
                return True
    return False


def verificar_pdfs(inf, pdfs, anexos, modo, cfg, con_figura=frozenset()):
    # 1. Papel y orientación
    malos, horizontales = [], []
    for p in pdfs:
        if not p.doc:
            continue
        for i, pg in enumerate(p.doc):
            w, h = round(pg.mediabox.width), round(pg.mediabox.height)
            giro = pg.rotation % 180 == 90
            apaisada = (w, h) == (792, 612)
            if (w, h) not in ((612, 792), (792, 612)):
                malos.append(f"{p.nombre} folio {p.folio(i)}: {w} x {h} pt, no es carta")
            elif giro or apaisada:
                horizontales.append((p.nombre, p.folio(i)))
                if (p.nombre, p.folio(i)) not in anexos:
                    malos.append(f"{p.nombre} folio {p.folio(i)}: horizontal sin ser anexo gráfico declarado")
    det = [f"{len(horizontales)} páginas horizontales, todas anexos gráficos declarados"] if horizontales and not malos else []
    inf.agregar("1", "Papel carta y vertical, salvo anexos gráficos declarados",
                NO if malos else CUMPLE, malos or det)

    # 2. Folio presente, abajo a la derecha y correlativo. Se mide la página
    # como se ve en pantalla (el Sobre N.º 2 es electrónico, Artículo 48.1):
    # una página girada deja el folio de la hoja física abajo a la izquierda.
    malos = []
    for p in pdfs:
        if not p.doc:
            continue
        for i, pg in enumerate(p.doc):
            esperado = str(p.folio(i))
            ok, donde = folio_visible(pg, esperado)
            if not ok:
                if donde:
                    malos.append(f"{p.nombre}, página {i + 1}: el folio {esperado} se ve "
                                 f"{' y '.join(donde)}, no abajo a la derecha"
                                 + (f" (página girada {pg.rotation} grados)" if pg.rotation else ""))
                else:
                    numeros = [w[4] for w in zona_folio(pg) if w[4].isdigit()]
                    malos.append(f"{p.nombre}, página {i + 1}: se esperaba el folio {esperado} "
                                 f"abajo a la derecha, hay {numeros or 'nada'}")
            if folio_en_cabeza(pg):
                malos.append(f"{p.nombre}, página {i + 1}: la cabeza repite «Folio», "
                             "la página muestra dos números")
    inf.agregar("2", "Folio en todas las páginas, extremo inferior derecho tal como se ve, correlativo",
                NO if malos else CUMPLE,
                malos or [f"{sum(p.n for p in pdfs)} páginas revisadas en {len(pdfs)} archivo(s), "
                          "medidas como se ven en pantalla"])

    # 3. Continuidad entre archivos
    if len(pdfs) > 1:
        det, mal = [], False
        for a, b in zip(pdfs, pdfs[1:]):
            if modo == "continuo":
                ok = b.folio0 == a.folio0 + a.n
                mal |= not ok
                det.append(f"{a.nombre} termina en {a.folio0 + a.n - 1}, "
                           f"{b.nombre} empieza en {b.folio0}" + ("" if ok else "  <- salto"))
            else:
                ok = b.folio0 == 1
                mal |= not ok
        inf.agregar("3", "Folio continuo entre archivos" if modo == "continuo"
                    else "Folio por subdocumento: cada archivo empieza en 1",
                    NO if mal else CUMPLE, det)
    else:
        inf.agregar("3", "Continuidad del folio entre archivos", NA, ["documento único"])

    # 4. Media firma y folio no se tocan entre sí ni con el texto
    malos, revisadas = [], 0
    for p in pdfs:
        if not p.doc:
            continue
        for i, pg in enumerate(p.doc):
            w, h = pg.mediabox.width, pg.mediabox.height
            fol = [x for x in zona_folio(pg) if x[4] == str(p.folio(i))]
            firma = [x for x in pg.get_text("words")
                     if x[4] in ("Media", "firma") and x[1] > h - 15 * MM]
            imgs = [pymupdf.Rect(b["bbox"]) for b in pg.get_image_info()
                    if b["bbox"][1] > h - 30 * MM and b["bbox"][2] - b["bbox"][0] < 40 * MM]
            if not fol or not firma:
                continue
            revisadas += 1
            rf = pymupdf.Rect(fol[0][:4])
            zona = pymupdf.Rect(min(x[0] for x in firma), min(x[1] for x in firma),
                                max(x[2] for x in firma), max(x[3] for x in firma))
            for r in [zona] + imgs:
                if r.x1 + 2 * MM > rf.x0 and r.y1 > rf.y0 - 2 * MM:
                    malos.append(f"{p.nombre} folio {p.folio(i)}: media firma a menos de 2 mm del folio")
                    break
            # texto del cuerpo que baje hasta la zona del pie (19 mm)
            pie = h - 19 * MM
            for b in pg.get_text("dict")["blocks"]:
                for l in b.get("lines", []):
                    for s in l["spans"]:
                        if s["text"].strip() and s["bbox"][3] > pie and s["bbox"][1] < pie - 1:
                            malos.append(f"{p.nombre} folio {p.folio(i)}: texto cruza el filete del pie: "
                                         f"«{s['text'][:30]}»")
                        elif s["text"].strip() and s["bbox"][1] > pie and \
                                not s["font"].startswith("IBMPlex"):
                            malos.append(f"{p.nombre} folio {p.folio(i)}: texto de figura en la zona "
                                         f"del pie: «{s['text'][:30]}»")
            # en páginas con figura, ningún trazo del diagrama entra en la zona
            # del pie. Se excluyen los filetes propios del pie: el que lo separa
            # del texto (19 mm) y la línea de la media firma (7,4 mm).
            if (p.nombre, p.folio(i)) in con_figura:
                for dib in pg.get_drawings():
                    r = dib["rect"]
                    if r.y1 <= pie + 1:
                        continue
                    if r.height <= 1.5 and abs(r.y1 - (h - 7.4 * MM)) < 1.5:
                        continue
                    malos.append(f"{p.nombre} folio {p.folio(i)}: el diagrama entra en la zona del "
                                 f"pie ({(h - r.y1) / MM:.1f} mm del borde inferior)")
                    break
    inf.agregar("4", "Media firma y folio separados entre sí, del texto y de los diagramas",
                NO if malos else CUMPLE, malos or [f"{revisadas} páginas con media firma y folio"])

    # 5. Tamaño de letra
    if not pymupdf:
        inf.agregar("5", "Cuerpo 11 pt o más, tablas y leyendas 9 pt o más", NA,
                    ["falta PyMuPDF: correr herramientas/preparar.sh"])
    else:
        cuerpo, resto, minimos = [], [], {}
        for p in pdfs:
            figs = cajas_figura(p.e["aux"], lambda f, p=p: p.doc[f - p.folio0].mediabox.height
                                if 0 <= f - p.folio0 < p.n else None)
            for i, pg in enumerate(p.doc):
                rects = figs.get(p.folio(i), [])
                for b in pg.get_text("dict")["blocks"]:
                    for l in b.get("lines", []):
                        for s in l["spans"]:
                            t = s["text"].strip()
                            if not t:
                                continue
                            f, z = s["font"], s["size"]
                            if not f.startswith("IBMPlex") or en_figura(s["bbox"], rects):
                                continue          # texto de figuras importadas, punto 6
                            clase = "cuerpo" if f.startswith("IBMPlexSerif") else "otros"
                            minimos[clase] = min(minimos.get(clase, 99), z)
                            if clase == "cuerpo" and z < CUERPO_MIN - TOLERANCIA:
                                cuerpo.append(f"{p.nombre} folio {p.folio(i)}: {z:.2f} pt «{t[:40]}»")
                            if clase == "otros" and z < TABLA_MIN - TOLERANCIA:
                                resto.append(f"{p.nombre} folio {p.folio(i)}: {f} {z:.2f} pt «{t[:40]}»")
        det = [f"cuerpo (IBM Plex Serif): mínimo {minimos.get('cuerpo', 0):.2f} pt",
               f"tablas, leyendas, títulos, encabezado y pie (Plex Sans y Mono): "
               f"mínimo {minimos.get('otros', 0):.2f} pt"]
        inf.agregar("5", "Cuerpo 11 pt o más, tablas y leyendas 9 pt o más (medido en el PDF)",
                    NO if cuerpo or resto else CUMPLE, cuerpo + resto + det)

    # 7. Fuentes incrustadas y texto extraíble
    malos = []
    for p in pdfs:
        out = subprocess.run(["pdffonts", p.ruta], capture_output=True, text=True).stdout
        for l in out.split("\n")[2:]:
            campos = l.split()
            if len(campos) >= 5 and "no" in campos[-5:-3]:
                malos.append(f"{p.nombre}: fuente no incrustada {campos[0]}")
        texto = subprocess.run(["pdftotext", p.ruta, "-"], capture_output=True, text=True).stdout
        vacias = [str(p.folio(i)) for i, t in enumerate(texto.split("\f")[:p.n]) if not t.strip()]
        if vacias:
            malos.append(f"{p.nombre}: páginas sin texto extraíble, folios {', '.join(vacias)}")
        if "\ufb01" in texto or "\ufb02" in texto:
            malos.append(f"{p.nombre}: ligaduras fi/fl sin separar, la búsqueda falla")
    muestra_texto = subprocess.run(["pdftotext", pdfs[0].ruta, "-"], capture_output=True,
                                   text=True).stdout if pdfs else ""
    prueba = [w for w in ("Técnica", "Ficha", "Folio") if w not in muestra_texto]
    if prueba:
        malos.append("búsqueda con tildes o ligaduras falla para: " + ", ".join(prueba))
    inf.agregar("7", "Fuentes incrustadas y texto seleccionable y buscable (tildes, ligaduras)",
                NO if malos else CUMPLE, malos or ["todas las fuentes incrustadas, «Técnica», "
                                                   "«Ficha» y «Folio» se encuentran en el texto"])


def verificar_figuras(inf, pdfs, medidas):
    """6. Texto dentro de las figuras: letra mínima del origen por la escala."""
    if not medidas:
        inf.agregar("6", "Texto dentro de las figuras 9 pt o más", NA, ["sin figuras importadas"])
        return
    det, mal = [], False
    por_nombre = {}
    for (archivo, escala, folio, modo, etiqueta) in medidas:
        if archivo == "nativa":
            continue
        clave = (archivo, modo, etiqueta)
        if clave in por_nombre:
            continue
        por_nombre[clave] = (escala, folio)
    for (archivo, modo, etiqueta), (escala, folio) in por_nombre.items():
        ruta = archivo if os.path.isabs(archivo) else os.path.join(RAIZ, archivo)
        if not os.path.exists(ruta) and os.path.exists(os.path.join(RAIZ, "figuras", archivo)):
            ruta = os.path.join(RAIZ, "figuras", archivo)
        minimo_pdf, ancho = None, None
        if pymupdf and ruta.lower().endswith(".pdf") and os.path.exists(ruta):
            d = pymupdf.open(ruta)
            ancho = d[0].rect.width
            for b in d[0].get_text("dict")["blocks"]:
                for l in b.get("lines", []):
                    for s in l["spans"]:
                        if s["text"].strip():
                            minimo_pdf = min(minimo_pdf or 99, s["size"])
        svg = os.path.splitext(ruta)[0] + ".svg"
        minimo_svg = None
        if os.path.exists(svg):
            t = leer(svg)
            tams = [float(x) for x in re.findall(r'font-size="([\d.]+)"', t)]
            vb = re.search(r'viewBox="[\d.]+ [\d.]+ ([\d.]+) [\d.]+"', t)
            if tams and vb and ancho:
                minimo_svg = min(tams) * ancho / float(vb.group(1))
        minimo = minimo_pdf or minimo_svg
        if minimo is None:
            det.append(f"{os.path.basename(archivo)} ({modo}, folio {folio}): escala {escala:.2f}, "
                       "no se pudo medir la letra de origen")
            continue
        efectiva = minimo * escala
        ok = efectiva >= TABLA_MIN - TOLERANCIA
        mal |= not ok
        linea = (f"{os.path.basename(archivo)} ({modo}, folio {folio}): letra mínima de origen "
                 f"{minimo:.2f} pt, escala {escala:.2f}, efectiva {efectiva:.2f} pt")
        if not ok:
            necesaria = TABLA_MIN / escala
            linea += (f"  <- bajo 9 pt. En esta disposición el diagrama necesita letra mínima "
                      f"{necesaria:.1f} pt a tamaño natural")
            if minimo_svg and ancho:
                vb_ancho = float(re.search(r'viewBox="[\d.]+ [\d.]+ ([\d.]+)', leer(svg)).group(1))
                linea += f", es decir font-size {necesaria * vb_ancho / ancho:.1f} en el SVG"
        det.append(linea)
    # medición directa en la página, como control
    if pymupdf:
        for p in pdfs:
            figs = cajas_figura(p.e["aux"], lambda f, p=p: p.doc[f - p.folio0].mediabox.height
                                if 0 <= f - p.folio0 < p.n else None)
            for i, pg in enumerate(p.doc):
                rects = figs.get(p.folio(i), [])
                tam = [s["size"] for b in pg.get_text("dict")["blocks"] for l in b.get("lines", [])
                       for s in l["spans"] if s["text"].strip() and
                       (en_figura(s["bbox"], rects) or not s["font"].startswith("IBMPlex"))]
                if tam:
                    det.append(f"  control en el PDF, {p.nombre} folio {p.folio(i)}: texto de figura "
                               f"entre {min(tam):.2f} y {max(tam):.2f} pt")
    inf.agregar("6", "Texto dentro de las figuras 9 pt o más", NO if mal else CUMPLE, det)


# ----------------------------------------------------------------------------
#  Registro de compilación
# ----------------------------------------------------------------------------
def verificar_registros(inf, entradas, ajenos):
    malos, avisos, marcadores = [], [], set()
    for e in entradas:
        try:
            log = leer(os.path.join(RAIZ, e["log"]))
        except OSError:
            malos.append(f"{e['nombre']}: sin registro de compilación")
            continue
        n = len(re.findall(r"^Overfull \\[hv]box", log, re.M))
        if n:
            malos.append(f"{e['nombre']}: {n} cajas desbordadas")
        und = set(re.findall(r"(?:Reference|Citation) `([^']*)' on page \d+ undefined", log))
        if und:
            malos.append(f"{e['nombre']}: referencias sin resolver: {', '.join(sorted(und))[:120]}")
        if re.search(r"There were undefined references", log):
            malos.append(f"{e['nombre']}: LaTeX informa referencias sin resolver")
        if re.search(r"Table widths have changed", log):
            malos.append(f"{e['nombre']}: longtable no estabilizó los anchos de una tabla "
                         "(el PDF puede tener una tabla fuera de margen)")
        elif re.search(r"Rerun to get|Label\(s\) may have changed", log):
            avisos.append(f"{e['nombre']}: el registro pide otra compilación")
        marcadores |= set(re.findall(r"AUDIT-MARCADOR: (.*)", log))
        for m in re.finditer(r"AUDIT-FORMULARIO-AJENO: (\S+) (T-\d+)", log):
            ajenos.add(f"{e['nombre']}: la tabla {m.group(1)} se llama «Formulario {m.group(2)}» "
                       "y no es ese formulario")
    inf.agregar("8", "Sin cajas desbordadas ni referencias sin resolver",
                NO if malos else (AVISO if avisos else CUMPLE), malos + avisos)
    return marcadores


# ----------------------------------------------------------------------------
#  Verificaciones sobre los fuentes
# ----------------------------------------------------------------------------
TITULO = re.compile(r"^\s*\\(section|subsection|subsubsection|paragraph)\*?\{")
OBJETO = re.compile(r"^\s*\\(begin\{(tabla|tablaAudit|figure|figuraNativa|longtable|tabular|xltabular)\}"
                    r"|figura\b|figura\[|figuraAncha|anexoGrafico|TablaAcumulada)")
SALTAR = re.compile(r"^\s*(\\label\{[^}]*\}|\\needspace\{[^}]*\}|\\FloatBarrier|%.*)?\s*$")


def verificar_fuentes(inf, fuentes, aux_labels, cfg, final, economico=False):
    contenido = [f for f in fuentes if es_contenido(f)]

    # 9. Figuras y tablas citadas desde el texto
    textos = {f: sin_comentarios(leer(f)) for f in contenido}
    todo = "\n".join(textos.values())
    citadas = set()
    for m in re.finditer(r"\\(figref|tabref)\{([^}]*)\}", todo):
        citadas.add(("fig:" if m.group(1) == "figref" else "tab:") + m.group(2))
    for m in re.finditer(r"\\(figrefs|tabrefs)\{([^}]*)\}\{([^}]*)\}", todo):
        pre = "fig:" if m.group(1) == "figrefs" else "tab:"
        citadas |= {pre + m.group(2), pre + m.group(3)}
    for m in re.finditer(r"\\(?:ref|refx|pageref|folio|verSeccion|verSeccionFolio)\{([^}]*)\}", todo):
        citadas.add(m.group(1))
    faltan, formularios = [], []
    for et in sorted(aux_labels):
        if not et.startswith(("fig:", "tab:")) or et in citadas:
            continue
        if re.match(r"tab:(t\d|T-|t8|t19|art46|hoja-resumen)", et):
            formularios.append(et)
        else:
            faltan.append(et)
    det = [f"no se cita: {x}" for x in faltan]
    if formularios:
        det.append("tablas de formulario sin cita desde el texto (aviso): " + ", ".join(formularios))
    inf.agregar("9", "Cada figura y cada tabla se cita desde el texto",
                NO if faltan else (AVISO if formularios else CUMPLE),
                det or [f"{len([x for x in aux_labels if x.startswith(('fig:', 'tab:'))])} "
                        "figuras y tablas, todas citadas"])

    # 10. Ningún título seguido directamente de una tabla o figura
    malos = []
    for f in contenido:
        lineas = leer(f).split("\n")
        for i, l in enumerate(lineas):
            if TITULO.match(l):
                j = i + 1
                while j < len(lineas) and SALTAR.match(lineas[j]):
                    j += 1
                if j < len(lineas) and OBJETO.match(lineas[j]):
                    malos.append(f"{os.path.relpath(f, RAIZ)}:{i + 1}: título seguido de "
                                 f"{lineas[j].strip()[:40]}")
    inf.agregar("10", "Ningún título va seguido directamente de una tabla o una figura",
                NO if malos else CUMPLE, malos or [f"{len(contenido)} archivos de contenido revisados"])

    # 11. Residuos prohibidos en el fuente
    malos = residuos("fuente", {os.path.relpath(f, RAIZ): sin_comentarios(leer(f))
                                for f in fuentes if not f.endswith(".bib")}, economico=economico)
    return malos


ROTULO_FORM = re.compile(r"\\(section|subsection|subsubsection|paragraph)\*?(?:\[[^\]]*\])?"
                         r"\{([^{}]*(?:\{[^{}]*\}[^{}]*)*)\}")


def rotulos_formulario(fuentes):
    """Títulos del contenido que nombran un «Formulario T-NN». Los
    formularios reales los imprime formularios/ con su propio título, así que
    un título del contenido con ese nombre anuncia algo que no es el
    formulario (la revisión del Informe 1 lo objetó en el Subdocumento 4)."""
    salida = []
    for f in fuentes:
        rel = os.path.relpath(f, RAIZ)
        if not es_contenido(f) or "/formularios/" in rel:
            continue
        t = sin_comentarios(leer(f))
        for m in ROTULO_FORM.finditer(t):
            n = re.search(r"Formulario[\s~]+(T-\d+)", m.group(2))
            if n:
                linea = t.count("\n", 0, m.start()) + 1
                salida.append(f"{rel}:{linea}: el título «{m.group(2)[:50]}» nombra el "
                              f"Formulario {n.group(1)}, que no es este apartado")
    return salida


RESIDUOS = [
    (r"Escuela de Inform", "Escuela de Informática"),
    (r"\bduplas?\b", "dupla"),
    (r"\b(Carlos|Naomi|Ignacio|Matías|Martín|Marcel|Alonso)\b", "nombre de integrante"),
    (r"Proyecto Semestral", "Proyecto Semestral"),
    (r"\b(January|February|March|April|June|July|August|September|October|November|December)\b",
     "mes en inglés"),
    (r"\bMay \d{4}\b", "mes en inglés"),
    (r"horas?[\s-]+hombres?", "horas hombre"),
    (r"(?<![\\\w])\$\s?\d", "cifra con signo de pesos"),
    (r"\\\$\s?\d", "cifra con signo de pesos"),
    (r"millones de pesos", "millones de pesos"),
    (r"\b(CLP|USD)\s?\$?\s?\d", "cifra en moneda"),
    (r"\bUF\s?\d", "cifra en UF"),
]


# Etiquetas que el Artículo 50.2 prohíbe solo en la oferta técnica. En los
# documentos económicos las cifras en dinero son lo que se pide (Artículo
# 51.2) y las horas hombre son la base del costeo por perfil (Formulario E-26).
SOLO_TECNICOS = {"horas hombre", "cifra con signo de pesos", "millones de pesos",
                 "cifra en moneda", "cifra en UF"}


def residuos(donde, textos, excepciones_hh=(), economico=False):
    malos = []
    for nombre, t in textos.items():
        es_t15 = "T-15" in nombre or nombre in excepciones_hh
        for patron, etiqueta in RESIDUOS:
            if etiqueta == "horas hombre" and es_t15:
                continue
            if economico and etiqueta in SOLO_TECNICOS:
                continue
            for m in re.finditer(patron, t, re.I if etiqueta != "nombre de integrante" else 0):
                linea = t.count("\n", 0, m.start()) + 1
                malos.append(f"{donde} {nombre}:{linea}: {etiqueta} «{m.group(0)}»")
        for m in re.finditer(r"\b192\b", t):
            cerca = t[max(0, m.start() - 60):m.end() + 60].lower()
            if "cami" in cerca or "tercer" in cerca:
                malos.append(f"{donde} {nombre}: 192 usado como cantidad de camiones")
    return malos


def residuos_pdf(pdfs, paginas_t15, economico=False):
    textos = {}
    for p in pdfs:
        if not p.doc:
            continue
        for i, pg in enumerate(p.doc):
            clave = f"{p.nombre} folio {p.folio(i)}"
            textos[clave] = pg.get_text()
    return residuos("PDF", textos, excepciones_hh=paginas_t15, economico=economico)


def verificar_escritura(fuentes):
    """Reglas de escritura del equipo: aviso, no error."""
    det = []
    for f in fuentes:
        if not es_contenido(f):
            continue
        t = sin_comentarios(leer(f))
        t = re.sub(r"\$[^$]*\$", "", t)              # matemáticas
        for patron, etiqueta in ((r";", "punto y coma"), (r"—|–", "raya"), (r"(?<!-)--(?!-)", "guion doble")):
            n = len(re.findall(patron, t))
            if n:
                det.append(f"{os.path.relpath(f, RAIZ)}: {n} {etiqueta}")
    return det


def verificar_hoja_resumen(inf, pdfs, entradas):
    """12. La hoja resumen coincide con los folios reales."""
    if not entradas:
        inf.agregar("12", "Hoja resumen coincide con la foliación", NA, ["no hay hoja resumen"])
        return
    por_nombre = {p.nombre[:-4]: p for p in pdfs}
    malos, ok = [], 0
    for clave, titulo, folio, archivo in entradas:
        p = por_nombre.get(archivo) or (pdfs[0] if len(pdfs) == 1 else None)
        if not p or not p.doc:
            malos.append(f"{titulo}: no se encontró {archivo}.pdf")
            continue
        i = int(folio) - p.folio0
        if not 0 <= i < p.n:
            malos.append(f"{titulo}: folio {folio} fuera de {p.nombre}")
            continue
        pg = p.doc[i]
        texto = norm(pg.get_text()).replace("[", " ").replace("]", " ")
        texto = re.sub(r"\s+", " ", texto)
        if str(folio) not in [w[4] for w in zona_folio(pg)]:
            malos.append(f"{titulo}: la página no lleva impreso el folio {folio}")
            continue
        clave_texto = re.sub(r"^(subdocumento \d+\.|formulario t-\d+\.|anexo gráfico [\w.]+\.|"
                             r"entregable \d+\.|informe preparatorio \d+\.|\d+(\.\d+)*\s)\s*", "",
                             norm(re.sub(r"\\[a-zA-Z]+|[{}~]", " ", titulo)))
        muestra = clave_texto[:24].strip()
        if clave.startswith("portada") or muestra in texto:
            ok += 1
        else:
            malos.append(f"{titulo}: el folio {folio} no muestra «{muestra}»")
    inf.agregar("12", "Hoja resumen: cada sección empieza en el folio que declara",
                NO if malos else CUMPLE, malos or [f"{ok} entradas comprobadas contra el PDF"])


def verificar_titulos_pdf(inf, pdfs, entradas):
    """17. Aperturas arriba de página nueva. 18. Títulos que no quedan al pie."""
    if not pymupdf:
        return
    por_nombre = {p.nombre[:-4]: p for p in pdfs}
    malos = []
    for clave, titulo, folio, archivo in entradas:
        if not clave.startswith("sd-"):
            continue
        p = por_nombre.get(archivo) or (pdfs[0] if len(pdfs) == 1 else None)
        if not p:
            continue
        pg = p.doc[int(folio) - p.folio0]
        palabra = norm(re.sub(r"^Subdocumento \d+\.\s*", "", titulo)).split(" ")[0]
        ys = [w[1] for w in pg.get_text("words") if norm(w[4]) == palabra]
        if not ys or min(ys) > pg.mediabox.height * 0.35:
            malos.append(f"{titulo}: no abre arriba de la página (folio {folio})")
    inf.agregar("17", "Cada subdocumento empieza en página nueva, arriba",
                NO if malos else CUMPLE, malos or ["todas las aperturas en la parte superior de página nueva"])
    # títulos en las últimas cinco líneas del área de texto
    huerfanos = []
    for p in pdfs:
        for i, pg in enumerate(p.doc):
            h = pg.mediabox.height
            limite = h - 25.3 * MM - 5 * 14.5
            for b in pg.get_text("dict")["blocks"]:
                for l in b.get("lines", []):
                    for sp in l["spans"]:
                        if ("SmBld" in sp["font"] or "SemiBold" in sp["font"]) and \
                                round(sp["size"]) in (12, 14, 17) and sp["bbox"][1] > limite and \
                                sp["bbox"][3] < h - 20 * MM and sp["text"].strip():
                            huerfanos.append(f"{p.nombre} folio {p.folio(i)}: «{sp['text'][:40]}»")
    inf.agregar("18", "Ningún título queda en las cinco últimas líneas de la página",
                AVISO if huerfanos else CUMPLE, huerfanos or ["ningún título al pie"])

    # 19. Ninguna tabla deja su cabecera sola al pie. Si la leyenda inicial de
    # una tabla aparece en la misma página que su propia continuación, la
    # página anterior quedó solo con el pie de la tabla.
    malas = []
    for p in pdfs:
        for i, pg in enumerate(p.doc):
            t = pg.get_text()
            cont = set(re.findall(r"Tabla (\d+\.\d+)\s*\(continuación\)", t))
            inicio = set(re.findall(r"Tabla (\d+\.\d+)\s+(?!\(continuación\))\S", t))
            for n in sorted(cont & inicio):
                malas.append(f"{p.nombre} folio {p.folio(i) - 1}: la Tabla {n} dejó la página solo con su pie")
    inf.agregar("19", "Ninguna tabla deja su cabecera o su leyenda sola al pie",
                NO if malas else CUMPLE, malas or ["todas las tablas empiezan con filas en su primera página"])


def pertenencia(entradas, archivo, folio0, n):
    """Subdocumento al que pertenece cada página de un archivo, según los
    folios de inicio que registra el .aux: una apertura (sd-N) abre el
    subdocumento N, sus formularios y anexos le pertenecen, y cualquier otra
    entrada (portada, ficha, índice, observaciones, referencias) es una página
    preliminar que no pertenece a ninguno."""
    marcas = []
    for clave, _, folio, arch in entradas:
        if arch != archivo:
            continue
        if clave.startswith("sd-"):
            marcas.append((int(folio), int(clave[3:]), True))
        elif not clave.startswith(("form-", "anexo-")):
            marcas.append((int(folio), None, False))
    marcas.sort(key=lambda x: x[0])
    salida = {}
    for i in range(n):
        folio, actual, apertura = folio0 + i, None, False
        for f, sd, es_apertura in marcas:
            if f <= folio:
                actual, apertura = sd, es_apertura and f == folio
        salida[folio] = (actual, apertura)
    return salida


def subdoc_encabezado(pagina):
    """Subdocumento que declara el encabezado de la página tal como se ve:
    el título corriente o la cabeza de un anexo gráfico. None si el
    encabezado no nombra ninguno, False si la página no tiene encabezado."""
    m = pagina.rotation_matrix
    textos = []
    for b in pagina.get_text("dict")["blocks"]:
        for l in b.get("lines", []):
            r = pymupdf.Rect(l["bbox"]) * m
            texto = " ".join(s["text"] for s in l["spans"])
            if r.y0 < 16 * MM or (r.y0 < 25 * MM and "ANEXO GRÁFICO" in texto):
                textos.append(texto)
    if not textos:
        return False
    m = re.search(r"\bSubdocumento (\d+)", " ".join(textos))
    return int(m.group(1)) if m else None


def verificar_encabezados(inf, pdfs, entradas):
    """20. El encabezado de cada página nombra el subdocumento al que la página
    pertenece, y las páginas preliminares no nombran ninguno."""
    if not pymupdf:
        return
    malos, revisadas = [], 0
    for p in pdfs:
        if not p.doc:
            continue
        duenos = pertenencia(entradas, p.nombre[:-4], p.folio0, p.n)
        for i, pg in enumerate(p.doc):
            folio = p.folio(i)
            dueno, apertura = duenos.get(folio, (None, False))
            declara = subdoc_encabezado(pg)
            if declara is False or apertura:
                continue              # portada, apertura o contraportada sin encabezado
            revisadas += 1
            if declara != dueno:
                malos.append(f"{p.nombre} folio {folio}: el encabezado dice "
                             + (f"Subdocumento {declara}" if declara else "una página preliminar")
                             + ", la página es "
                             + (f"del Subdocumento {dueno}" if dueno else "preliminar"))
    inf.agregar("20", "El encabezado nombra el subdocumento al que pertenece cada página",
                NO if malos else CUMPLE,
                malos or [f"{revisadas} encabezados comparados con los folios de inicio del .aux"])


NOMBRE_TECNICO = re.compile(r"^(INFORME[123]|SOBRE2)_[A-Z0-9]+_(SUBDOC\d\d|OFERTA_TECNICA)_\d{8}\.pdf$")
# Formulario E-21 (FEP01 p.72), «sin excepción». La fecha va como AAAAMMDD,
# igual que en los Artículos 49 a 51 (el E-21 no fija su formato).
NOMBRE_E21 = {
    "oferta": re.compile(r"^[A-Z0-9]+_OfertaEconomica_1_\d{8}\.(pdf|docx)$"),
    "analisis": re.compile(r"^[A-Z0-9]+_AnalisisFinanciero_2_\d{8}\.(pdf|docx)$"),
    "planilla": re.compile(r"^[A-Z0-9]+_ModeloFinanciero_3_\d{8}\.xlsx$"),
    "zip": re.compile(r"^SOBRE3_[A-Z0-9]+_OFERTA_ECONOMICA_\d{8}\.ZIP$"),
}
# Informe 3 (supuesto: el patrón de los informes)
NOMBRE_INFORME3 = {
    "costos": re.compile(r"^INFORME3_[A-Z0-9]+_COSTOS_VENTA_\d{8}\.pdf$"),
    "planilla": re.compile(r"^INFORME3_[A-Z0-9]+_PLANILLA_\d{8}\.xlsx$"),
}


def verificar_nombres(inf, entradas, cfg, grupo, man=None):
    if man and man.get("tipo") == "economico":
        return verificar_nombres_economicos(inf, man)
    malos = [e["nombre"] for e in entradas
             if not NOMBRE_TECNICO.match(e["nombre"]) and e["nombre"] != "muestra.pdf"]
    det = [f"{e['nombre']}" for e in entradas]
    inf.agregar("13", "Nombres de archivo conforme a los Artículos 49 a 51",
                NO if malos else CUMPLE, [f"mal nombrado: {m}" for m in malos] or det)


def verificar_nombres_economicos(inf, man):
    """13. Nombres del Formulario E-21 y entregables completos del sobre."""
    final = man["instancia"] == "final"
    patrones = NOMBRE_E21 if final else NOMBRE_INFORME3
    malos, avisos, det = [], [], []
    for e in man["archivos"]:
        for nombre in [e["nombre"]] + ([e["docx"]] if e.get("docx") else []):
            det.append(nombre)
            if not patrones.get(e["clave"], re.compile("^$")).match(nombre):
                malos.append(f"mal nombrado según el Formulario E-21: {nombre}")
        if final and not e.get("docx"):
            malos.append(f"falta el DOCX de {e['nombre']} (Formulario E-21 y Artículo 40.4)")
    if final:
        claves = {e["clave"] for e in man["archivos"]}
        for c in ("oferta", "analisis"):
            if c not in claves:
                malos.append(f"falta el entregable {'1' if c == 'oferta' else '2'} del Formulario E-21")
    if man.get("planilla"):
        det.append(man["planilla"])
        if not patrones["planilla"].match(man["planilla"]):
            malos.append(f"mal nombrada: {man['planilla']}")
    else:
        avisos.append("falta la planilla del mandante (" + ("modelo financiero, entregable 3 del "
                      "Formulario E-21" if final else "Formulario T-22") + "): el formato no la "
                      "genera, se copia de economico/planilla/")
    if man.get("zip"):
        det.append(man["zip"])
        if not NOMBRE_E21["zip"].match(man["zip"]):
            malos.append(f"mal nombrado según el Artículo 51.3: {man['zip']}")
    inf.agregar("13", "Nombres de archivo conforme al Formulario E-21 y al Artículo 51.3"
                if final else "Nombres de archivo del Informe 3",
                NO if malos else (AVISO if avisos else CUMPLE), malos + avisos + det)


# ----------------------------------------------------------------------------
#  Documentos económicos (Artículo 51.2 y Formularios E-21 y E-24)
# ----------------------------------------------------------------------------
E24 = {"USD": 900, "EUR": 1000, "UF": 40000}     # FEP01, Formulario E-24, p. 73
IVA_E24 = 19
DINERO = re.compile(r"(?<![\w])(CLP|UF|USD|US\$|\$)\s?(\d{1,3}(?:\.\d{3})+(?:,\d+)?|\d+(?:,\d+)?)")


def div_red(a, b):
    if a >= 0:
        return (2 * a + b) // (2 * b)
    return -((2 * (-a) + b) // (2 * b))


def fmt_entero(n):
    return f"{n:,}".replace(",", ".")


def fmt_cent(c):
    s = "-" if c < 0 else ""
    c = abs(c)
    return s + f"{c // 100:,}".replace(",", ".") + f",{c % 100:02d}"


def cifras_aux(texto):
    return [m.groups() for m in re.finditer(
        r"\\audit@cifraeco\{([^{}]*)\}\{([^{}]*)\}\{([^{}]*)\}\{([^{}]*)\}\{([^{}]*)\}", texto)]


def ivas_aux(texto):
    return [m.groups() for m in re.finditer(
        r"\\audit@ivaeco\{([^{}]*)\}\{(-?\d+)\}\{(-?\d+)\}\{(-?\d+)\}\{([^{}]*)\}", texto)]


def texto_plano(doc):
    return re.sub(r"\s+", " ", " ".join(pg.get_text() for pg in doc).replace("\xa0", " "))


def cifras_dinero(doc):
    """Cifras en dinero, leídas línea por línea: en una tabla, la moneda de
    una fila y el número de la siguiente no forman una cifra."""
    salida = []
    for pg in doc:
        for b in pg.get_text("dict")["blocks"]:
            for l in b.get("lines", []):
                texto = " ".join(s["text"] for s in l["spans"]).replace("\xa0", " ")
                salida += [f"{a} {n}" for a, n in DINERO.findall(re.sub(r"\s+", " ", texto))]
    return salida


def verificar_economico(inf, man, pdfs, cfg, grupo_dir):
    """22. Tres monedas con el tipo de cambio del E-24. 23. IVA desglosado.
    24. Valores idénticos en PDF, DOCX y planilla."""
    # 22 ---------------------------------------------------------------------
    malos, det = [], []
    for k, v in E24.items():
        if cfg.tipos_cambio.get(k) != v:
            malos.append(f"configuracion/economico.tex fija 1 {k} = CLP {cfg.tipos_cambio.get(k)}, "
                         f"el Formulario E-24 dice CLP {fmt_entero(v)}")
    if cfg.iva != IVA_E24:
        malos.append(f"configuracion/economico.tex fija IVA {cfg.iva} %, el E-24 dice {IVA_E24} %")
    tc = cfg.tipos_cambio
    permitidas = set()
    montos = 0
    for p, e in zip(pdfs, man["archivos"]):
        aux = leer(os.path.join(RAIZ, e["aux"]))
        for clave, clp, uf, usd, pesos in cifras_aux(aux):
            permitidas |= {x for x in (clp, uf, usd) if x}
            if clp and uf and usd and pesos.lstrip("-").isdigit():
                montos += 1
                n = int(pesos)
                esperado = (f"CLP {fmt_entero(n)}", f"UF {fmt_cent(div_red(n * 100, tc['UF']))}",
                            f"USD {fmt_cent(div_red(n * 100, tc['USD']))}")
                if (clp, uf, usd) != esperado:
                    malos.append(f"{p.nombre}: {clave} impreso como {clp} · {uf} · {usd}, con el "
                                 f"tipo de cambio del E-24 corresponde {' · '.join(esperado)}")
            elif (uf or usd) and not clp:
                pass                              # rangos del E-26 en UF
        if not p.doc:
            continue
        texto = texto_plano(p.doc)
        for k in ("USD", "UF"):
            if f"1 {k} = CLP {fmt_entero(tc[k])}" not in texto:
                malos.append(f"{p.nombre}: no indica el tipo de cambio «1 {k} = CLP "
                             f"{fmt_entero(tc[k])}» (Formulario E-21)")
        for cifra in cifras_dinero(p.doc):
            if cifra not in permitidas:
                malos.append(f"{p.nombre}: la cifra «{cifra}» no sale de partidas.csv ni de los "
                             "comandos de montos: puede discrepar con los otros documentos")
    det.append(f"{montos} montos en CLP, UF y USD recalculados con 1 USD = CLP {fmt_entero(tc['USD'])} "
               f"y 1 UF = CLP {fmt_entero(tc['UF'])} (Formulario E-24)")
    det.append("ninguna cifra en dinero escrita a mano" if not any("no sale de" in x for x in malos)
               else "")
    inf.agregar("22", "Montos en CLP, UF y USD con el tipo de cambio del Formulario E-24",
                NO if malos else CUMPLE, malos + [d for d in det if d])

    # 23 ---------------------------------------------------------------------
    malos, n_iva = [], 0
    for p, e in zip(pdfs, man["archivos"]):
        aux = leer(os.path.join(RAIZ, e["aux"]))
        for clave, neto, iva, total, afecto in ivas_aux(aux):
            n_iva += 1
            neto, iva, total = int(neto), int(iva), int(total)
            if afecto == "si" and iva != div_red(neto * cfg.iva, 100):
                malos.append(f"{p.nombre}: IVA de {clave} es {iva}, el {cfg.iva} % de {neto} es "
                             f"{div_red(neto * cfg.iva, 100)}")
            if total != neto + iva:
                malos.append(f"{p.nombre}: total de {clave} {total} distinto de neto más IVA")
        if p.doc and f"IVA ({cfg.iva} %)" not in texto_plano(p.doc):
            malos.append(f"{p.nombre}: ninguna tabla desglosa el IVA (Artículo 51.2)")
    inf.agregar("23", "Valores netos, IVA desglosado y total general (Artículo 51.2)",
                NO if malos else CUMPLE,
                malos or [f"{n_iva} partidas y totales con neto, IVA y total comprobados"
                          if n_iva else "tablas de montos con columnas de neto, IVA y total, "
                          "sin partidas completas todavía"])

    # 24 ---------------------------------------------------------------------
    malos, avisos, det = [], [], []
    por_clave = {}
    for p, e in zip(pdfs, man["archivos"]):
        aux = leer(os.path.join(RAIZ, e["aux"]))
        for clave, clp, uf, usd, pesos in cifras_aux(aux):
            if clave.startswith(("partida ", "neto ", "total ", "iva ")) and "total general" not in clave:
                por_clave.setdefault(clave, set()).add((clp, uf, usd))
        # el DOCX trae las mismas cifras que el PDF
        if e.get("docx"):
            ruta = os.path.join(grupo_dir, e["docx"])
            try:
                docx = texto_plano(pymupdf.open(ruta))
            except Exception as ex:                # noqa: BLE001
                malos.append(f"{e['docx']}: no se pudo abrir ({ex})")
                continue
            en_pdf = set(cifras_dinero(p.doc))
            en_docx = set(cifras_dinero(pymupdf.open(ruta)))
            eco = json.load(open(os.path.join(RAIZ, e["eco"]), encoding="utf-8")) if e.get("eco") else {}
            celdas = {c.strip("*") for tb in eco.get("tablas", {}).values() for f in tb["filas"]
                      for c in f if re.fullmatch(r"\**-?[\d.]+(,\d+)?\**", c)}
            faltan = sorted((en_pdf - en_docx) | {c for c in celdas if c not in docx})
            sobran = sorted(en_docx - en_pdf)
            if faltan or sobran:
                malos.append(f"{e['docx']}: cifras distintas del PDF. Faltan {faltan[:6]}, "
                             f"sobran {sobran[:6]}")
            else:
                det.append(f"{e['docx']}: abre y trae las mismas {len(en_pdf)} cifras en moneda y "
                           f"{len(celdas)} valores de tabla que el PDF")
    for clave, variantes in por_clave.items():
        if len(variantes) > 1:
            malos.append(f"{clave} se imprime distinto entre documentos: {sorted(variantes)}")
    # la planilla del mandante contra partidas.csv
    if man.get("planilla"):
        import planilla as pl
        raices = man["archivos"][0]["fuentes"][0]
        partidas = pl.leer_partidas(raices)
        resultado = pl.comparar(os.path.join(grupo_dir, man["planilla"]), partidas, cfg.tipos_cambio)
        for clave, ref, esperado, v, ok in resultado:
            if not ok:
                malos.append(f"{man['planilla']} {ref}: {clave} vale {v}, partidas.csv dice {esperado}")
        if not resultado:
            avisos.append("ninguna partida declara su celda en la planilla (columna planilla de "
                          "partidas.csv): no se puede comparar")
        else:
            det.append(f"{len(resultado)} celdas de la planilla comparadas con partidas.csv")
    else:
        avisos.append("sin planilla del mandante en la salida: la comparación con el modelo "
                      "financiero queda pendiente")
    det.append(f"{len(por_clave)} cifras de partidas iguales en todos los documentos"
               if por_clave else "sin partidas completas todavía")
    inf.agregar("24", "Valores idénticos en los PDF, los DOCX y la planilla (Formulario E-21)",
                NO if malos else (AVISO if avisos else CUMPLE), malos + avisos + det)


def verificar_paleta(inf):
    t = leer(os.path.join(RAIZ, "temas", "marca.tex"))
    colores = dict(re.findall(r"\\definecolor\{([^}]*)\}\{HTML\}\{([0-9A-Fa-f]{6})\}", t))

    def lum(h):
        c = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
        c = [x / 12.92 if x <= 0.03928 else ((x + 0.055) / 1.055) ** 2.4 for x in c]
        return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]

    def contraste(a, b):
        la, lb = sorted([lum(a), lum(b)], reverse=True)
        return (la + 0.05) / (lb + 0.05)
    det, mal = [], False
    for c in ("audit-marino", "audit-tinta", "audit-secundario"):
        r = contraste(colores[c], "FFFFFF")
        mal |= r < 4.5
        det.append(f"{c} sobre blanco {r:.2f}:1")
    det.append(f"audit-turquesa sobre blanco {contraste(colores['audit-turquesa'], 'FFFFFF'):.2f}:1, "
               "solo para filetes y nodos, nunca texto chico")
    inf.agregar("14", "Colores de texto legibles (contraste 4,5:1 o más)", NO if mal else CUMPLE, det)


# ----------------------------------------------------------------------------
def verificar_grupo(ruta_manifiesto, cfg):
    man = json.load(open(ruta_manifiesto, encoding="utf-8"))
    grupo = man["grupo"]
    if man.get("instancia") and man["instancia"] != cfg.instancia:
        cfg = Config(man["instancia"])
    economico = man.get("tipo") == "economico"
    grupo_dir = os.path.dirname(ruta_manifiesto)
    if grupo == "muestra":
        grupo_dir = SALIDA
    inf = Informe(grupo)
    pdfs = [Pdf(e, grupo_dir) for e in man["archivos"]]
    modo = man.get("modo_folio", "unico")

    # anexos declarados y medidas de figuras
    anexos, medidas, aux_labels, fuentes, entradas_hoja = set(), [], set(), set(), []
    entradas_todas = []          # folios de inicio de cada archivo, haya o no hoja resumen
    for p, e in zip(pdfs, man["archivos"]):
        try:
            entradas_todas += [(a, b, c, e["nombre"][:-4])
                               for a, b, c, _ in entradas_folio(leer(os.path.join(RAIZ, e["aux"])))]
        except OSError:
            pass
        for m in figuras_medidas(e["aux"]):
            medidas.append(m)
            if m[3] == "horizontal":
                anexos.add((p.nombre, m[2]))
        try:
            aux = leer(os.path.join(RAIZ, e["aux"]))
            aux_labels |= set(re.findall(r"\\newlabel\{([^}]*)\}", aux))
            if not entradas_hoja and len(pdfs) == 1:
                entradas_hoja = [(a, b, c, e["nombre"][:-4]) for a, b, c, _ in entradas_folio(aux)]
        except OSError:
            pass
        fuentes |= set(fuentes_de(e["aux"]))
    hoja = os.path.join(RAIZ, "salida", "aux", grupo, "folios-sobre.tex")
    if len(pdfs) > 1 and os.path.exists(hoja):
        entradas_hoja = entradas_folio(leer(hoja))

    con_figura = {(p.nombre, m[2]) for p, e in zip(pdfs, man["archivos"])
                  for m in figuras_medidas(e["aux"])}
    verificar_pdfs(inf, pdfs, anexos, modo, cfg, con_figura)
    verificar_figuras(inf, pdfs, medidas)
    ajenos = set()
    marcadores = verificar_registros(inf, man["archivos"], ajenos)
    malos_fuente = verificar_fuentes(inf, sorted(fuentes), aux_labels, cfg, cfg.instancia == "final",
                                     economico)

    # páginas del T-15, donde las bases piden horas hombre
    t15 = set()
    for i, (clave, titulo, folio, archivo) in enumerate(entradas_todas):
        if clave == "form-T-15":
            sig = entradas_todas[i + 1] if i + 1 < len(entradas_todas) else None
            # el formulario siguiente puede empezar en la misma página en que
            # termina el T-15: esa página también queda exenta
            fin = int(sig[2]) + 1 if sig and sig[3] == archivo else int(folio) + 3
            t15 |= {f"{archivo}.pdf folio {x}" for x in range(int(folio), fin)}
    malos_pdf = residuos_pdf(pdfs, t15, economico) if pymupdf else []
    inf.agregar("11", "Sin residuos: Escuela, dupla, nombres, Proyecto Semestral, meses en inglés, "
                "192 camiones (documento económico: el Artículo 50.2 no se aplica)" if economico else
                "Sin residuos: Escuela, dupla, nombres, Proyecto Semestral, meses en inglés, "
                "horas hombre, cifras en dinero (Artículo 50.2), 192 camiones",
                NO if malos_fuente or malos_pdf else CUMPLE,
                malos_fuente + malos_pdf or [f"{len(fuentes)} fuentes y {sum(p.n for p in pdfs)} "
                                              "páginas revisadas"])
    rotulos = sorted(ajenos) + rotulos_formulario(sorted(fuentes))
    inf.agregar("21", "Ninguna tabla ni título se llama «Formulario T-NN» sin ser el formulario",
                AVISO if rotulos else CUMPLE,
                rotulos or ["las tablas y títulos que nombran un formulario son los de formularios/"])
    verificar_hoja_resumen(inf, pdfs, entradas_hoja)
    verificar_titulos_pdf(inf, pdfs, entradas_todas)
    verificar_encabezados(inf, pdfs, entradas_todas)
    verificar_nombres(inf, man["archivos"], cfg, grupo, man)
    if economico and pymupdf:
        verificar_economico(inf, man, pdfs, cfg, grupo_dir)
    verificar_paleta(inf)
    escritura = verificar_escritura(sorted(fuentes))
    inf.agregar("15", "Reglas de escritura: sin punto y coma, raya ni guion doble (aviso)",
                AVISO if escritura else CUMPLE, escritura or ["ninguno en los archivos de contenido"])
    final = cfg.instancia == "final" and grupo.startswith("final")
    inf.agregar("16", "Marcadores por completar", (NO if final else AVISO) if marcadores else CUMPLE,
                [f"{len(marcadores)} marcadores distintos pendientes: "
                 + "; ".join(sorted(marcadores)[:6]).replace(";", " |")] if marcadores else [])
    n = inf.imprimir()
    inf.markdown(os.path.join(SALIDA, f"verificacion-{grupo}.md"))
    return n


def main():
    cfg = Config()
    if len(sys.argv) > 1:
        manifiestos = sys.argv[1:]
    else:
        manifiestos = sorted(glob.glob(os.path.join(SALIDA, "manifiesto*.json"))
                             + glob.glob(os.path.join(SALIDA, "*", "manifiesto*.json")))
    if not manifiestos:
        print("No hay nada compilado en salida/. Correr antes herramientas/compilar.py")
        return 2
    if not pymupdf:
        print("Aviso: sin PyMuPDF no se miden tamaños de letra. Correr herramientas/preparar.sh")
    total = sum(verificar_grupo(m, cfg) for m in manifiestos)
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main())
