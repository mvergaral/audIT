#!/usr/bin/env python3
"""Generador de diagramas de Lucid (Standard Import) para la dupla 4.

Lucid trabaja a 160 DPI: 1 pt = 2,22 px. Cada diagrama se dibuja dentro de un
marco de tamaño fijo, que es lo que exporta el PNG, para que la escala en la
página sea casi 1:1 y la letra de 10 pt llegue impresa a 10 pt.

  Figura horizontal: marco de 1600 x 1040 px, área de 257,4 x 167 mm.
  Figura vertical:   marco de 930 px de ancho, 148,9 mm de ancho de texto.

Paleta del manual de marca de audIT (Formato-Oferta-audIT/temas/marca.tex).
"""
import html
import json

MARINO = "#0F2A43"
TURQUESA = "#18B7C7"
TINTA = "#1B2430"
SECUNDARIO = "#5B6675"
FILETE = "#C6D0DC"
NUBE, NUBE_F = "#1B4FA8", "#EEF3FC"
SITIO, SITIO_F = "#96600B", "#FBF4E8"
TERM, TERM_F = "#0A6B45", "#E9F6EF"
FLOTA, FLOTA_F = "#5B3BB5", "#F2EEFB"
ROJO = "#A32222"
BLANCO = "#FFFFFF"

PX_POR_CAR = 12.5   # ancho medio de un carácter a 10 pt (22,2 px de cuerpo)
HOLGURA = 36        # relleno interno de las formas de texto de Lucid
ALTO_LINEA = 27     # alto de línea a 10 pt


def ancho_texto(lineas, pt=10):
    return max(len(l) for l in lineas) * PX_POR_CAR * pt / 10


def html_texto(lineas, pt=10, bold_primera=False, color=TINTA, align="center"):
    partes = []
    for i, l in enumerate(lineas):
        e = html.escape(l)
        if i == 0 and bold_primera:
            e = f"<b>{e}</b>"
        partes.append(e)
    return (f'<p style="font-size:{pt}pt;text-align:{align};color:{color}">'
            + "<br>".join(partes) + "</p>")


class Diagrama:
    def __init__(self, titulo, ancho, alto, marco=False):
        self.titulo = titulo
        self.ancho, self.alto = ancho, alto
        self.formas = []
        self.lineas = []
        self.n = 0
        # marco de fondo opcional: fija el área que exporta el PNG
        if marco:
          self.formas.append({"id": "marco", "type": "rectangle",
                            "boundingBox": {"x": 0, "y": 0, "w": ancho, "h": alto},
                            "style": {"fill": {"type": "color", "color": BLANCO},
                                      "stroke": {"color": BLANCO, "width": 1, "style": "solid"}}})

    def _id(self, pref):
        self.n += 1
        return f"{pref}{self.n}"

    def zona(self, x, y, w, h, titulo, color, relleno, pt=11, dashed=False, trazo=None):
        """Contenedor redondeado con título en la esquina. trazo: color del borde si difiere del título."""
        i = self._id("z")
        self.formas.append({"id": i, "type": "roundedRectangleContainer",
                            "boundingBox": {"x": x, "y": y, "w": w, "h": h},
                            "style": {"fill": {"type": "color", "color": relleno},
                                      "stroke": {"color": trazo or color, "width": 2,
                                                 "style": "dashed" if dashed else "solid"}}})
        if titulo:
            lineas = titulo if isinstance(titulo, list) else [titulo]
            tw = ancho_texto(lineas, pt) + HOLGURA
            self.formas.append({"id": self._id("t"), "type": "text",
                                "boundingBox": {"x": x + 12, "y": y + 6, "w": tw,
                                                "h": ALTO_LINEA * pt / 10 * len(lineas) + 8},
                                "text": html_texto(lineas, pt, bold_primera=True, color=color,
                                                   align="left")})
        return i

    def icono(self, clase, cx, y, lineas, tam=56, pt=10, color=TINTA, arriba=False):
        """Ícono centrado en cx con su rótulo debajo, o encima si arriba=True. Devuelve el id del ícono."""
        i = self._id("i")
        # un espacio como texto: sin él Lucid imprime el nombre del servicio bajo el ícono
        self.formas.append({"id": i, "type": "namedShape", "className": clase, "text": " ",
                            "boundingBox": {"x": cx - tam / 2, "y": y, "w": tam, "h": tam}})
        tw = ancho_texto(lineas, pt) + HOLGURA
        th = ALTO_LINEA * pt / 10 * len(lineas) + 6
        ry = y - th - 4 if arriba else y + tam + 4
        self.formas.append({"id": self._id("r"), "type": "text",
                            "boundingBox": {"x": cx - tw / 2, "y": ry, "w": tw, "h": th},
                            "text": html_texto(lineas, pt, bold_primera=True, color=color)})
        return i

    def caja(self, x, y, w, h, lineas, borde=MARINO, relleno=BLANCO, pt=10, bold=True,
             color=TINTA, dashed=False, align="center"):
        i = self._id("c")
        self.formas.append({"id": i, "type": "rectangle",
                            "boundingBox": {"x": x, "y": y, "w": w, "h": h},
                            "text": html_texto(lineas, pt, bold_primera=bold, color=color, align=align),
                            "style": {"fill": {"type": "color", "color": relleno},
                                      "stroke": {"color": borde, "width": 1.5,
                                                 "style": "dashed" if dashed else "solid"}}})
        return i

    def texto(self, x, y, lineas, pt=10, color=TINTA, bold=False, align="left", w=None):
        tw = w or ancho_texto(lineas, pt) + HOLGURA
        th = ALTO_LINEA * pt / 10 * len(lineas) + 6
        i = self._id("x")
        self.formas.append({"id": i, "type": "text",
                            "boundingBox": {"x": x, "y": y, "w": tw, "h": th},
                            "text": html_texto(lineas, pt, bold_primera=bold, color=color, align=align)})
        return i

    def linea(self, a, b, pa=None, pb=None, rotulo=None, pos=0.5, lado="top", color=MARINO,
              estilo="solid", ancho=2, flecha="arrow", origen="none", tipo="elbow", pt=10):
        ep1 = {"type": "shapeEndpoint", "style": origen, "shapeId": a}
        ep2 = {"type": "shapeEndpoint", "style": flecha, "shapeId": b}
        if pa and pb:
            ep1["position"] = {"x": pa[0], "y": pa[1]}
            ep2["position"] = {"x": pb[0], "y": pb[1]}
        l = {"id": self._id("l"), "lineType": tipo, "endpoint1": ep1, "endpoint2": ep2,
             "stroke": {"color": color, "width": ancho, "style": estilo}}
        if rotulo:
            lineas = rotulo if isinstance(rotulo, list) else [rotulo]
            l["text"] = [{"text": html_texto(lineas, pt, color=color), "position": pos, "side": lado}]
        self.lineas.append(l)
        return l["id"]

    def json(self):
        # Lucid imprime «Text» en las formas básicas sin texto
        for f in self.formas:
            if f["type"] in ("rectangle", "circle") and "text" not in f:
                f["text"] = " "
        return json.dumps({"version": 1, "pages": [{"id": "p1", "title": self.titulo,
                                                    "shapes": self.formas, "lines": self.lineas}]},
                          ensure_ascii=False, separators=(",", ":"))
