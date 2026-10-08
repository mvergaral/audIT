#!/usr/bin/env python3
"""Íconos propios de equipos de red y de sitio, vehículos y piezas lógicas.

Ningún set abierto trae router, switch, firewall, rack, UPS, generador, clima de
precisión, lector de tarjeta o gabinete en el estilo plano de Fluent Emoji, así que
se dibujan aquí con la misma paleta. Todos usan un lienzo de 48 x 48 y no llevan
marca ni logo de fabricante: el modelo va como nombre bajo el ícono.

  python3 propios.py      escribe iconos/pr-*.svg
"""
import os

AQUI = os.path.dirname(os.path.abspath(__file__))
ICONOS = os.path.join(AQUI, "..", "iconos")

# Paleta de Fluent Emoji, estilo plano
D1, D2, D3 = "#321B41", "#433B6B", "#533566"
G1, G2, G3, G4, G5 = "#9B9B9B", "#B4ACBC", "#D3D3D3", "#E1D8EC", "#F3EEF8"
W = "#FFFFFF"
B1, B2, B3 = "#00A6ED", "#26C9FC", "#0074BA"
R1 = "#F8312F"
Y1, O1 = "#FFB02E", "#FF822D"
V1 = "#00D26A"


def r(x, y, w, h, rx=0, f=D2):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{f}"/>'


def c(cx, cy, rr, f):
    return f'<circle cx="{cx}" cy="{cy}" r="{rr}" fill="{f}"/>'


def p(d, s, w=2.0, f="none", extra=""):
    return (f'<path d="{d}" fill="{f}" stroke="{s}" stroke-width="{w}" stroke-linecap="round" '
            f'stroke-linejoin="round"{extra}/>')


def pf(d, f):
    return f'<path d="{d}" fill="{f}"/>'


I = {}

I["pr-router"] = "".join([
    r(10, 5, 3.2, 19, 1.6, G1), r(34.8, 5, 3.2, 19, 1.6, G1),
    r(5, 21, 38, 18, 3.5, D2), r(5, 35, 38, 4, 2, D1),
    c(12, 29, 1.8, V1), c(17, 29, 1.8, V1), c(22, 29, 1.8, B2),
    r(29, 27, 4, 4, 0.6, G3), r(35, 27, 4, 4, 0.6, G3),
])

I["pr-switch"] = (r(2.5, 15, 43, 18, 3, D2)
                  + "".join(r(6 + i * 4.4, 19.5, 3.2, 3.4, 0.5, G3) for i in range(8))
                  + "".join(r(6 + i * 4.4, 25, 3.2, 3.4, 0.5, G3) for i in range(8))
                  + c(42.3, 21, 1.2, V1) + c(42.3, 26.5, 1.2, V1))

I["pr-firewall"] = "".join([
    r(4, 11, 40, 27, 3.5, R1),
    p("M4 20 H44 M4 29 H44 M17 11 V20 M31 11 V20 M10.5 20 V29 M24 20 V29 M37.5 20 V29 "
      "M17 29 V38 M31 29 V38", W, 1.6),
])

I["pr-servidor"] = "".join(
    r(3, y, 42, 11, 2.5, D2) + "".join(r(6 + i * 6.5, y + 3, 5, 5, 0.8, G2) for i in range(4))
    + c(37.5, y + 5.5, 1.4, V1) + c(41.3, y + 5.5, 1.4, B2) for y in (12, 25))

I["pr-rack"] = (r(11, 3, 26, 41, 2.5, D1) + r(14, 6, 20, 35, 1, D2)
                + "".join(r(15.5, 7.5 + i * 5.6, 17, 4.2, 0.8, G2 if i % 2 else G3)
                          + c(30.2, 9.6 + i * 5.6, 0.9, V1) for i in range(6))
                + r(13, 44, 4, 2, 0.5, D1) + r(31, 44, 4, 2, 0.5, D1))

I["pr-ups"] = (r(12, 4, 24, 40, 3, D2) + r(16, 9, 16, 7, 1.2, B2)
               + pf("M26.5 20 L18 31.5 H23.4 L21.4 40 L30 28 H24.6 Z", Y1))

I["pr-generador"] = "".join([
    r(36, 5, 3.5, 9, 1, G1), r(5, 12, 38, 27, 3, Y1),
    p("M9.5 18 H25 M9.5 22.5 H25 M9.5 27 H25 M9.5 31.5 H25", O1, 2.2),
    r(29.5, 17, 10, 12, 1.6, D2), r(31, 19, 7, 3.6, 0.8, B2),
    pf("M35.5 30.5 L32 35.5 H34.5 L33.5 38.5 L37.5 33.5 H35 Z", D2),
    r(3, 38, 42, 4.5, 1.2, D1),
])

I["pr-clima"] = "".join([
    r(11, 3, 26, 42, 2.5, G3), r(14, 6, 20, 10, 1.5, G2),
    p("M15.5 9 H32.5 M15.5 11.5 H32.5 M15.5 14 H32.5", G3, 1.0),
    p("M24 22 V36 M17.9 25.5 L30.1 32.5 M17.9 32.5 L30.1 25.5", B1, 2.4),
    r(15, 39.5, 7, 3, 0.6, D2),
])

I["pr-camara"] = "".join([
    r(4, 9, 6, 15, 1.5, G1), p("M9 16.5 L16 20", G1, 3.2),
    '<g transform="rotate(14 28 22)">', r(14, 15.5, 26, 13, 4, G3), r(13, 12.5, 30, 5.5, 2.5, G2),
    c(39.5, 22, 4.2, D1), c(38.4, 20.9, 1.3, B2), "</g>",
])

I["pr-lector-tarjeta"] = "".join([
    r(14, 5, 20, 38, 4, D2),
    p("M19.5 18 Q22.5 22 19.5 26 M23 15.5 Q28 22 23 28.5 M26.5 13 Q33 22 26.5 31", W, 2.0),
    c(24, 37.5, 1.7, V1),
])

I["pr-lector-facial"] = "".join([
    r(13, 3, 22, 42, 4, D1), r(15.5, 8, 17, 24, 2, B2),
    c(24, 17, 4.2, W), pf("M17 30.5 Q24 20.5 31 30.5 Z", W), c(24, 5.6, 0.9, G2),
    r(19.5, 36, 9, 4.5, 2.2, D2),
])

I["pr-antena"] = "".join([
    p("M24 9 L15.5 45 M24 9 L32.5 45", D2, 2.4),
    p("M20.8 22.5 H27.2 L18.6 31.5 H29.4 L16.8 39.5 H31.2", D2, 1.5),
    c(24, 8, 2.8, R1),
    p("M16.5 3.5 Q12.5 8 16.5 12.5 M12.8 0.8 Q6.5 8 12.8 15.2", B1, 2.0),
    p("M31.5 3.5 Q35.5 8 31.5 12.5 M35.2 0.8 Q41.5 8 35.2 15.2", B1, 2.0),
])

I["pr-wifi"] = "".join([
    r(10, 25, 28, 17, 5, G3), c(24, 33.5, 1.9, B1),
    p("M17.5 17.5 Q24 11.5 30.5 17.5 M13 13 Q24 3 35 13", B1, 2.6), c(24, 21.2, 2.1, B1),
])

I["pr-ble"] = "".join([
    r(9, 12, 30, 25, 6, G3),
    p("M19.5 19 L28.5 28 L24 32 V16 L28.5 20 L19.5 29", B3, 2.4),
    c(34.5, 16.5, 1.3, V1),
])

I["pr-pc-industrial"] = (r(4, 15, 40, 22, 2.5, D2)
                         + "".join(r(6.2 + i * 3.9, 10, 2.2, 6.5, 0.8, G1) for i in range(10))
                         + r(8, 27.5, 4.5, 3.5, 0.6, G3) + r(14.5, 27.5, 4.5, 3.5, 0.6, G3)
                         + r(21, 27.5, 6, 3.5, 0.6, G3) + c(38.5, 29.2, 1.4, V1))

I["pr-g26i"] = "".join([
    r(3, 31, 6, 4.5, 1, G1), r(39, 31, 6, 4.5, 1, G1),
    r(12, 9.5, 4.6, 6.5, 1, Y1), r(21.7, 9.5, 4.6, 6.5, 1, Y1), r(31.4, 9.5, 4.6, 6.5, 1, Y1),
    r(7, 15, 34, 23, 4.5, D1), c(13.5, 26.5, 1.7, V1), c(18.5, 26.5, 1.7, B2),
    r(24, 23.5, 12.5, 6, 1, D3),
])

I["pr-can"] = "".join([
    p("M2 30 H46", G1, 5.5), p("M2 30 H46", G3, 1.4),
    r(14, 18, 20, 21, 5, D2), p("M14 30 H34", D1, 1.4), c(28.8, 23.3, 1.5, V1),
    p("M24 39 V46", D2, 2.6),
])

I["pr-iridium"] = "".join([
    r(8, 30, 32, 10, 3, D1), pf("M10.5 31 Q24 12 37.5 31 Z", G3),
    p("M17 10.5 Q24 5.5 31 10.5 M12.8 7 Q24 -1 35.2 7", B1, 2.2),
])

I["pr-baliza"] = "".join([
    r(14, 14, 20, 20, 6, G2), c(24, 24, 5.2, W), c(24, 24, 2.2, B1),
    p("M10 16.5 Q6.2 24 10 31.5 M5.8 12.8 Q0.8 24 5.8 35.2", B1, 2.1),
    p("M38 16.5 Q41.8 24 38 31.5 M42.2 12.8 Q47.2 24 42.2 35.2", B1, 2.1),
])

I["pr-gabinete"] = "".join([
    r(9, 3, 30, 42, 2.5, G2), r(12, 6, 24, 36, 1.5, G4), r(31, 20, 2.4, 8, 1, D2),
    p("M16 10.5 H27 M16 13.5 H27 M16 16.5 H27", G2, 1.4),
])

I["pr-vesda"] = "".join([
    p("M5 6.5 H43", R1, 3.2), p("M24 6.5 V16", R1, 3.2),
    c(11, 6.5, 0.9, W), c(18, 6.5, 0.9, W), c(31, 6.5, 0.9, W), c(38, 6.5, 0.9, W),
    r(9, 16, 30, 24, 3, G3), r(13, 20.5, 22, 8, 1.2, D2),
    r(15, 25, 3, 2, 0.4, V1), r(19.5, 24, 3, 3, 0.4, Y1), r(24, 23, 3, 4, 0.4, O1), r(28.5, 22, 3, 5, 0.4, R1),
    c(17, 34.5, 1.5, V1),
])

I["pr-transferencia"] = "".join([
    r(11, 4, 26, 40, 2, G2), r(14, 8, 20, 32, 1.5, G4), r(19, 15, 10, 18, 2, D2),
    r(21.5, 12, 5, 11, 1.8, Y1), c(24, 37, 1.3, V1),
])

I["pr-cola"] = "".join([
    p("M5 12 H43 M5 36 H43", D2, 2.2),
    r(8, 16, 9, 16, 2, B3), r(19.5, 16, 9, 16, 2, B1), r(31, 16, 9, 16, 2, B2),
])

I["pr-cortacircuito"] = "".join([
    r(12, 5, 24, 38, 3, D2), r(18.5, 12, 11, 22, 2, D1), r(19.5, 23, 9, 10, 1.6, W),
    pf("M25.5 36.5 L22.5 40.5 H24.6 L23.8 43 L27 39 H24.9 Z", Y1),
])

I["pr-semirremolque"] = "".join([
    r(3, 15, 6.5, 12, 1, B1), r(9, 11, 37, 21, 1.5, G3), r(9, 25.5, 37, 2.2, 0, B1),
    r(9, 32, 37, 2.6, 0, D2), r(16, 34, 2.2, 7.5, 0.4, D2),
    c(33, 38, 3.8, D1), c(33, 38, 1.3, G2), c(41, 38, 3.8, D1), c(41, 38, 1.3, G2),
])

I["pr-tracto"] = "".join([
    r(17.5, 4, 2.4, 17, 0.8, G1), r(24, 9, 18, 22, 3.5, B1), r(32, 12.5, 8, 8, 1.2, B2),
    r(3, 29, 41, 4.5, 1, D2), r(7, 26, 13, 3.2, 0.8, G1),
    c(12, 37.5, 4.6, D1), c(12, 37.5, 1.6, G2), c(35, 37.5, 4.6, D1), c(35, 37.5, 1.6, G2),
])

I["pr-servicio"] = "".join([
    pf("M24 4 L41.3 14 V34 L24 44 L6.7 34 V14 Z", B3),
    p("M24 14 L32.7 19 V29 L24 34 L15.3 29 V19 Z", W, 2.2),
])

I["pr-adaptador"] = "".join([
    r(4, 15, 15, 18, 2.5, B3), r(19, 19, 7.5, 2.8, 0.6, G1), r(19, 26.2, 7.5, 2.8, 0.6, G1),
    r(29, 15, 15, 18, 2.5, B1), r(27.5, 18.5, 2, 11, 0.5, D2),
])

I["pr-transformador"] = "".join([
    p("M8 17 H38 M32 11 L38 17 L32 23", B3, 3.0),
    p("M40 31 H10 M16 25 L10 31 L16 37", B1, 3.0),
])

I["pr-reconciliador"] = "".join([
    r(11, 5, 26, 38, 2.5, G3), r(18, 3, 12, 5, 1.5, D2),
    p("M16.5 25 L21.5 30 L32 19.5", V1, 3.6),
])

I["pr-memoria"] = "".join([
    r(9, 9, 30, 30, 3, D2), r(15, 15, 18, 18, 1.5, D3),
    "".join(r(13 + i * 6, 3.5, 2.5, 6, 0.5, G1) + r(13 + i * 6, 38.5, 2.5, 6, 0.5, G1) for i in range(4)),
    "".join(r(3.5, 13 + i * 6, 6, 2.5, 0.5, G1) + r(38.5, 13 + i * 6, 6, 2.5, 0.5, G1) for i in range(4)),
])

import math as _m


def _arco(cx, cy, rr, a0, a1):
    x0, y0 = cx + rr * _m.cos(_m.radians(a0)), cy - rr * _m.sin(_m.radians(a0))
    x1, y1 = cx + rr * _m.cos(_m.radians(a1)), cy - rr * _m.sin(_m.radians(a1))
    return f"M{x0:.2f} {y0:.2f} A{rr} {rr} 0 0 1 {x1:.2f} {y1:.2f}"


I["pr-rastreador"] = "".join([
    r(7, 17, 30, 25, 5, D2),
    pf("M22 21.5 a6 6 0 0 1 6 6 c0 4.6 -6 10 -6 10 s-6 -5.4 -6 -10 a6 6 0 0 1 6 -6 z", R1),
    c(22, 27.4, 2.2, W),
    p("M34 12.5 Q38.5 13.5 39.5 18 M34 7 Q43.5 8.5 45 18", B1, 2.1),
])

I["pr-pod"] = "".join([
    pf("M24 5 L41 14.5 L24 24 L7 14.5 Z", B2), pf("M7 14.5 L24 24 V43 L7 33.5 Z", B3),
    pf("M41 14.5 V33.5 L24 43 V24 Z", B1),
])

I["pr-barrera"] = "".join([
    r(7, 14, 9, 28, 1.5, D2), r(4, 41, 15, 4, 1, D1),
    r(15, 17, 31, 6, 1, W), r(15, 17, 6, 6, 0, R1), r(27, 17, 6, 6, 0, R1), r(39, 17, 6, 6, 0, R1),
    p("M15 17 H46 V23 H15", G1, 0.8),
])

I["pr-medidor"] = "".join([
    p(_arco(24, 32, 16, 180, 0), G3, 6.5), p(_arco(24, 32, 16, 180, 55), B1, 6.5),
    p("M24 32 L33.5 21", D2, 3), c(24, 32, 3.4, D2), r(6, 37, 36, 4, 2, G2),
])

I["pr-aleta"] = "".join([
    pf("M9 38 C12 25 22 13 37 11 C33 20 34 30 39 38 Z", D2), r(5, 37, 38, 4.5, 2, G1),
    p("M37 3.5 Q42.5 5 43.5 10.5", B1, 2.1),
])

I["pr-volante"] = "".join([
    f'<circle cx="24" cy="24" r="14" fill="{W}" stroke="{D2}" stroke-width="4.2"/>',
    p("M10.5 26 H19.5 M28.5 26 H37.5 M24 29 V37.5", D2, 3.6), c(24, 25.5, 4.6, D2),
])


CREDITO = ("Dibujo propio de esta entrega en la paleta de Fluent Emoji, sin elementos de terceros "
           "ni marcas. Uso libre para el equipo audIT")


def main():
    os.makedirs(ICONOS, exist_ok=True)
    for k, cuerpo in I.items():
        with open(os.path.join(ICONOS, k + ".svg"), "w", encoding="utf-8") as f:
            f.write('<svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 48 48">'
                    + cuerpo + "</svg>\n")
    print(len(I), "íconos propios")


if __name__ == "__main__":
    main()
