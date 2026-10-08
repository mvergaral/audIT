"""Lienzo común de las figuras de los Subdocumentos 4, 7 y 13 (segunda vuelta).

El viewBox está en puntos, así que font-size es el tamaño impreso. Vertical:
148,9 mm de ancho (422 pt). Horizontal: 257,4 x 167 mm (729,6 x 473,4 pt).
Cada <text> lleva sus propios x, y, font-size, font-family y font-weight, que es
lo que lee herramientas/letra_diagramas.py.

Novedades de la segunda vuelta: fichas (cajas blancas chicas de 9 pt), rótulos
sobre su línea con fondo blanco, saltos donde una línea cruza a otra y una
revisión de líneas que pasan sobre íconos, fichas o textos.
"""
import html
import os
import re
import subprocess

import pymupdf

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.normpath(os.path.join(AQUI, ".."))
ICONOS = os.path.join(RAIZ, "iconos")
PLEX = "/usr/share/texmf-dist/fonts/opentype/ibm/plex/"
_F = {400: pymupdf.Font(fontfile=PLEX + "IBMPlexSans-Regular.otf"),
      600: pymupdf.Font(fontfile=PLEX + "IBMPlexSans-SemiBold.otf")}

MM = 72 / 25.4
TINTA = "#000000"
LINEA = "#2B2B2B"
BORDE = "#404040"
BORDE_AZ = "#7A7A7A"
BORDE_FICHA = "#8C8C8C"
SUBRED = "#F7F8FA"
GRIS_CLARO = "#E6E6E6"
ROJO = "#C0392B"
GUION = "3.5 2.5"
FAMILIA = "IBM Plex Sans"
SALTO = 3.0
REVISION = {}   # nombre de figura -> líneas que pasan sobre íconos, fichas o textos


def ancho(s, tam=10, peso=400):
    return _F[600 if peso >= 600 else 400].text_length(s, fontsize=tam)


def _limpiar_icono(clave, crudo):
    t = re.sub(r"<\?xml.*?\?>|<!DOCTYPE.*?>|<!--.*?-->|<title>.*?</title>|<desc>.*?</desc>", "",
               crudo, flags=re.S)
    m = re.search(r"<svg\b([^>]*)>(.*)</svg>", t, re.S)
    attrs, cuerpo = m.group(1), m.group(2)
    vb = re.search(r'viewBox="([^"]+)"', attrs)
    if vb:
        vb = vb.group(1)
    else:
        w = float(re.search(r'width="([\d.]+)', attrs).group(1))
        h = float(re.search(r'height="([\d.]+)', attrs).group(1))
        vb = f"0 0 {w} {h}"
    pre = clave + "-"
    ids = set(re.findall(r'\bid="([^"]+)"', cuerpo))
    for i in sorted(ids, key=len, reverse=True):
        e = re.escape(i)
        cuerpo = re.sub(rf'\bid="{e}"', f'id="{pre}{i}"', cuerpo)
        cuerpo = re.sub(rf"url\(\s*#{e}\s*\)", f"url(#{pre}{i})", cuerpo)
        cuerpo = re.sub(rf'href="#{e}"', f'href="#{pre}{i}"', cuerpo)
    clases = set()
    for cl in re.findall(r'\bclass="([^"]+)"', cuerpo):
        clases.update(cl.split())
    for cl in sorted(clases, key=len, reverse=True):
        cuerpo = re.sub(rf"\.{re.escape(cl)}(?![\w-])", f".{pre}{cl}", cuerpo)
    cuerpo = re.sub(r'\bclass="([^"]+)"',
                    lambda m: 'class="' + " ".join(pre + x for x in m.group(1).split()) + '"', cuerpo)
    fill = re.search(r'\sfill="([^"]+)"', attrs)
    extra = f' fill="{fill.group(1)}"' if fill else ""
    return f'<symbol id="ic-{clave}" viewBox="{vb}"{extra}>{cuerpo}</symbol>'


def _cruce(a, b):
    """Punto donde el segmento a (de la línea nueva) cruza al b, si son perpendiculares y
    el cruce cae en el interior de ambos."""
    (ax0, ay0), (ax1, ay1) = a
    (bx0, by0), (bx1, by1) = b
    ah, bh = abs(ay0 - ay1) < 0.01, abs(bx0 - bx1) < 0.01
    av, bv = abs(ax0 - ax1) < 0.01, abs(by0 - by1) < 0.01
    m = SALTO + 1.0
    if ah and bh:      # a horizontal, b vertical
        x, y = bx0, ay0
        if min(ax0, ax1) + m < x < max(ax0, ax1) - m and min(by0, by1) + 0.5 < y < max(by0, by1) - 0.5:
            return (x, y)
    if av and bv:      # a vertical, b horizontal
        x, y = ax0, by0
        if min(ay0, ay1) + m < y < max(ay0, ay1) - m and min(bx0, bx1) + 0.5 < x < max(bx0, bx1) - 0.5:
            return (x, y)
    return None


class Figura:
    def __init__(self, nombre, carpeta, tipo, alto=None):
        self.nombre, self.carpeta, self.tipo = nombre, carpeta, tipo
        if tipo == "H":
            self.W, self.H = 729.6, 473.4
            self.mm = (257.4, 167.0)
        else:
            self.W = 422.0
            self.H = alto or 567.0
            assert self.H <= 567.0
            self.mm = (148.9, round(self.H / MM, 1))
        self.simbolos = {}
        self.fondo, self.lineas, self.frente, self.textos = [], [], [], []
        self.trazos = []          # (pts, attrs) de cada línea, para los saltos
        self.cajas_icono = []     # rectángulos que ninguna línea debe atravesar
        self.cajas_texto = []
        self.usados = set()

    # ------------------------------------------------------------- texto
    def texto(self, x, y, s, tam=10, peso=400, anc="start", capa=None, revisar=True):
        assert tam >= 9, (self.nombre, s, tam)
        p = f' font-weight="{peso}"' if peso != 400 else ""
        (capa if capa is not None else self.textos).append(
            f'<text x="{x:.2f}" y="{y:.2f}" font-size="{tam}" font-family="{FAMILIA}"{p} '
            f'text-anchor="{anc}" fill="{TINTA}">{html.escape(s)}</text>')
        w = ancho(s, tam, peso)
        x0 = {"start": x, "middle": x - w / 2, "end": x - w}[anc]
        if revisar:
            self.cajas_texto.append((x0, y - 0.72 * tam, x0 + w, y + 0.2 * tam, s))
        return w

    def fondo_texto(self, x, y, s, tam=9, peso=400, anc="start", pad=1.6):
        w = ancho(s, tam, peso)
        x0 = {"start": x, "middle": x - w / 2, "end": x - w}[anc]
        self.frente.append(f'<rect x="{x0 - pad:.2f}" y="{y - tam * 0.8:.2f}" width="{w + 2 * pad:.2f}" '
                           f'height="{tam * 1.1:.2f}" fill="#FFFFFF"/>')

    def rotulo(self, x, y, s, tam=9, anc="middle", fondo=True, peso=400):
        """Rótulo de línea: 9 pt, sobre la línea y con fondo blanco."""
        lineas = s if isinstance(s, (list, tuple)) else [s]
        for i, l in enumerate(lineas):
            yy = y + i * (tam + 1.6)
            if fondo:
                self.fondo_texto(x, yy, l, tam, peso, anc)
            self.texto(x, yy, l, tam, peso, anc, revisar=not fondo)

    def ficha(self, x, y, s, anc="middle", tam=9, peso=400, alto=14, pad=4.5, w=None):
        """Ficha: caja blanca chica con un texto de 9 pt. (x, y) es el centro vertical
        de la caja y el punto de anclaje horizontal. Devuelve (x0, y0, x1, y1)."""
        lineas = s if isinstance(s, (list, tuple)) else [s]
        ww = w or max(ancho(l, tam, peso) for l in lineas) + 2 * pad
        hh = alto + (len(lineas) - 1) * (tam + 1.6)
        x0 = {"start": x, "middle": x - ww / 2, "end": x - ww}[anc]
        y0 = y - hh / 2
        self.frente.append(f'<rect x="{x0:.2f}" y="{y0:.2f}" width="{ww:.2f}" height="{hh:.2f}" rx="3" '
                           f'fill="#FFFFFF" stroke="{BORDE_FICHA}" stroke-width="0.6"/>')
        for i, l in enumerate(lineas):
            self.texto(x0 + ww / 2, y0 + 10 + i * (tam + 1.6) + (alto - 14) / 2, l, tam, peso, "middle",
                       capa=self.frente, revisar=False)
        self.cajas_icono.append((x0, y0, x0 + ww, y0 + hh, "ficha " + lineas[0]))
        return (x0, y0, x0 + ww, y0 + hh)

    def marcador(self, cx, cy, n, r=6.8):
        """Número en un círculo blanco de borde negro."""
        self.frente.append(f'<circle cx="{cx:.2f}" cy="{cy:.2f}" r="{r}" fill="#FFFFFF" stroke="#000000" '
                           f'stroke-width="0.9"/>')
        self.texto(cx, cy + 3.2, str(n), 9, 600, "middle", capa=self.frente, revisar=False)
        self.cajas_icono.append((cx - r, cy - r, cx + r, cy + r, f"marcador {n}"))

    def rombo(self, cx, cy, r=4.5, relleno="#000000"):
        self.frente.append(f'<path d="M{cx:.2f} {cy - r:.2f} L{cx + r:.2f} {cy:.2f} L{cx:.2f} {cy + r:.2f} '
                           f'L{cx - r:.2f} {cy:.2f} Z" fill="{relleno}"/>')

    # ------------------------------------------------------------- íconos
    def _simbolo(self, clave):
        if clave not in self.simbolos:
            with open(os.path.join(ICONOS, clave + ".svg"), encoding="utf-8") as f:
                self.simbolos[clave] = _limpiar_icono(clave, f.read())
        self.usados.add(clave)

    def icono(self, clave, cx, cy, s, revisar=True):
        self._simbolo(clave)
        self.frente.append(f'<use href="#ic-{clave}" x="{cx - s / 2:.2f}" y="{cy - s / 2:.2f}" '
                           f'width="{s:.2f}" height="{s:.2f}"/>')
        if revisar:
            self.cajas_icono.append((cx - s / 2, cy - s / 2, cx + s / 2, cy + s / 2, clave))

    def nodo(self, clave, cx, cy, s, nombre, dato=None, tam=10):
        """Ícono con su nombre debajo (10 pt) y un dato técnico opcional (9 pt).
        Devuelve la y de la última línea escrita."""
        if clave:
            self.icono(clave, cx, cy, s)
        y = cy + s / 2 + tam + 1
        for l in (nombre if isinstance(nombre, (list, tuple)) else [nombre]):
            if l:
                self.texto(cx, y, l, tam, 400, "middle")
                y += tam + 2
        for l in (dato if isinstance(dato, (list, tuple)) else ([dato] if dato else [])):
            self.texto(cx, y - 0.5, l, 9, 400, "middle")
            y += 10.5
        return y - (tam + 2)

    # ------------------------------------------------------------- grupos
    def grupo(self, x, y, w, h, titulo=None, icono=None, rx=10, borde=BORDE, grosor=0.75,
              relleno="#FFFFFF", discontinuo=False, tam=10, peso=600, sub=None):
        guion = f' stroke-dasharray="{GUION}"' if discontinuo else ""
        self.fondo.append(f'<rect x="{x:.2f}" y="{y:.2f}" width="{w:.2f}" height="{h:.2f}" rx="{rx}" '
                          f'fill="{relleno}" stroke="{borde}" stroke-width="{grosor}"{guion}/>')
        if titulo:
            tx = x + 8
            if icono:
                self.icono(icono, x + 8 + 6.5, y + 11, 13, revisar=False)
                tx = x + 8 + 13 + 4
            wt = self.texto(tx, y + 15, titulo, tam, peso)
            if sub:
                self.texto(tx + wt + 6, y + 15, sub, 9)

    def grupo_az(self, x, y, w, h, titulo, icono, subred=False, sub=None, discontinuo=False):
        self.grupo(x, y, w, h, titulo, icono, rx=3, borde=BORDE_AZ, grosor=0.6,
                   relleno=SUBRED if subred else "#FFFFFF", sub=sub, discontinuo=discontinuo)

    def caja(self, x, y, w, h, lineas, tam=10, peso=400, rx=6, discontinuo=False, borde=BORDE,
             grosor=0.75, color_borde=None, alto_linea=None):
        guion = f' stroke-dasharray="{GUION}"' if discontinuo else ""
        self.fondo.append(f'<rect x="{x:.2f}" y="{y:.2f}" width="{w:.2f}" height="{h:.2f}" rx="{rx}" '
                          f'fill="#FFFFFF" stroke="{color_borde or borde}" stroke-width="{grosor}"{guion}/>')
        n = len(lineas)
        al = alto_linea or tam + 2
        y0 = y + h / 2 - (n - 1) * al / 2 + tam * 0.35
        for i, l in enumerate(lineas):
            txt, t2, p2 = l if isinstance(l, tuple) else (l, tam, peso)
            self.texto(x + w / 2, y0 + i * al, txt, t2, p2, "middle")

    # ------------------------------------------------------------- líneas
    def linea(self, pts, disc=False, flecha="fin", color=LINEA, grosor=1.0, saltos=True):
        self.trazos.append((list(pts), dict(disc=disc, flecha=flecha, color=color, grosor=grosor,
                                            saltos=saltos)))

    def _path(self, pts, cruces):
        d = [f"M{pts[0][0]:.2f},{pts[0][1]:.2f}"]
        for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
            cs = [c for c in cruces if c[0] == ((x0, y0), (x1, y1))]
            if abs(y0 - y1) < 0.01:          # horizontal
                s = 1 if x1 > x0 else -1
                for _, (xc, yc) in sorted(cs, key=lambda c: s * c[1][0]):
                    d.append(f"L{xc - s * SALTO:.2f},{y0:.2f}")
                    d.append(f"A{SALTO},{SALTO} 0 0 {1 if s > 0 else 0} {xc + s * SALTO:.2f},{y0:.2f}")
            elif abs(x0 - x1) < 0.01:        # vertical
                s = 1 if y1 > y0 else -1
                for _, (xc, yc) in sorted(cs, key=lambda c: s * c[1][1]):
                    d.append(f"L{x0:.2f},{yc - s * SALTO:.2f}")
                    d.append(f"A{SALTO},{SALTO} 0 0 {0 if s > 0 else 1} {x0:.2f},{yc + s * SALTO:.2f}")
            d.append(f"L{x1:.2f},{y1:.2f}")
        return " ".join(d)

    def _dibujar_lineas(self):
        hechos = []
        for pts, a in self.trazos:
            segs = list(zip(pts, pts[1:]))
            cruces = []
            if a["saltos"]:
                for s in segs:
                    for otro in hechos:
                        for t in otro:
                            p = _cruce(s, t)
                            if p:
                                cruces.append((s, p))
            hechos.append(segs)
            guion = f' stroke-dasharray="{GUION}"' if a["disc"] else ""
            mid = "r" if a["color"] == ROJO else "n"
            m = ""
            if a["flecha"] in ("fin", "ambas"):
                m += f' marker-end="url(#fin-{mid})"'
            if a["flecha"] in ("ini", "ambas"):
                m += f' marker-start="url(#ini-{mid})"'
            self.lineas.append(f'<path d="{self._path(pts, cruces)}" fill="none" stroke="{a["color"]}" '
                               f'stroke-width="{a["grosor"]}" stroke-linejoin="miter"{guion}{m}/>')

    def rect(self, x, y, w, h, relleno="#FFFFFF", borde=BORDE, grosor=0.75, rx=0, disc=False, capa="fondo",
             guion=None):
        g = f' stroke-dasharray="{guion or GUION}"' if disc else ""
        b = f' stroke="{borde}" stroke-width="{grosor}"' if borde else ""
        getattr(self, capa).append(f'<rect x="{x:.2f}" y="{y:.2f}" width="{w:.2f}" height="{h:.2f}" '
                                   f'rx="{rx}" fill="{relleno}"{b}{g}/>')

    def crudo(self, s, capa="frente"):
        getattr(self, capa).append(s)

    # ------------------------------------------------------------- revisión
    def revisar(self):
        """Líneas que atraviesan un ícono, una ficha o un texto (no cuentan los extremos
        que llegan al borde). Devuelve la lista de problemas."""
        malos = []
        cajas = [(x0 + 1.5, y0 + 1.5, x1 - 1.5, y1 - 1.5, n) for x0, y0, x1, y1, n in self.cajas_icono]
        cajas += [(x0 + 0.5, y0 + 0.5, x1 - 0.5, y1 - 0.5, "texto «" + n + "»") for x0, y0, x1, y1, n in self.cajas_texto]
        for pts, _ in self.trazos:
            for (ax, ay), (bx, by) in zip(pts, pts[1:]):
                for x0, y0, x1, y1, n in cajas:
                    if x1 <= x0 or y1 <= y0:
                        continue
                    if abs(ay - by) < 0.01 and y0 < ay < y1:
                        if min(ax, bx) < x1 and max(ax, bx) > x0:
                            malos.append(n)
                    elif abs(ax - bx) < 0.01 and x0 < ax < x1:
                        if min(ay, by) < y1 and max(ay, by) > y0:
                            malos.append(n)
        return sorted(set(malos))

    # ------------------------------------------------------------- salida
    def svg(self):
        def marcadores(mid, color):
            return (f'<marker id="fin-{mid}" viewBox="0 0 10 10" refX="9.5" refY="5" markerWidth="5.5" '
                    f'markerHeight="5.5" markerUnits="userSpaceOnUse" orient="auto">'
                    f'<path d="M0,0.8 L10,5 L0,9.2 z" fill="{color}"/></marker>'
                    f'<marker id="ini-{mid}" viewBox="0 0 10 10" refX="0.5" refY="5" markerWidth="5.5" '
                    f'markerHeight="5.5" markerUnits="userSpaceOnUse" orient="auto">'
                    f'<path d="M10,0.8 L0,5 L10,9.2 z" fill="{color}"/></marker>')
        self.lineas = []
        self._dibujar_lineas()
        o = [f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" '
             f'width="{self.mm[0]}mm" height="{self.mm[1]}mm" viewBox="0 0 {self.W:g} {self.H:g}">',
             "<defs>" + marcadores("n", LINEA) + marcadores("r", ROJO)
             + "".join(self.simbolos[k] for k in sorted(self.simbolos)) + "</defs>",
             f'<rect x="0" y="0" width="{self.W:g}" height="{self.H:g}" fill="#FFFFFF"/>',
             '<g id="grupos">', *self.fondo, "</g>",
             '<g id="flechas">', *self.lineas, "</g>",
             '<g id="iconos">', *self.frente, "</g>",
             '<g id="textos">', *self.textos, "</g>", "</svg>"]
        return "\n".join(o) + "\n"

    def guardar(self, salida_raiz=RAIZ):
        d = os.path.join(salida_raiz, self.carpeta)
        os.makedirs(d, exist_ok=True)
        base = os.path.join(d, self.nombre)
        with open(base + ".svg", "w", encoding="utf-8") as f:
            f.write(self.svg())
        subprocess.run(["rsvg-convert", "-f", "pdf", "-o", base + ".pdf", base + ".svg"], check=True)
        subprocess.run(["rsvg-convert", "-f", "png", "--dpi-x", "300", "--dpi-y", "300",
                        "-b", "white", "-o", base + ".png", base + ".svg"], check=True)
        REVISION[self.nombre] = self.revisar()
        return base
