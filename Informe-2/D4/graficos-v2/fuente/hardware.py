#!/usr/bin/env python3
"""Ilustraciones de hardware: vista frontal de cada equipo del T-11, dibujada en
vector a partir de la forma real del modelo (proporciones, puertos, luces,
antenas), sin marca ni logo del fabricante. El modelo va como nombre junto al
equipo.

Openclipart (dominio público) no trae estos modelos y las fotos de los
fabricantes tienen derechos, así que se dibujan aquí. Cada lienzo usa la
proporción del equipo: un equipo de 1 U de rack mide 483 x 44, como el frente
real en milímetros, y se coloca con Figura.equipo(), que respeta esa proporción.

  python3 hardware.py      escribe iconos/hw-*.svg
"""
import os

AQUI = os.path.dirname(os.path.abspath(__file__))
ICONOS = os.path.join(AQUI, "..", "iconos")

# chasis oscuro, metal claro, carcasa blanca, puertos y luces
CH0, CH1, CH2, CH3 = "#16181B", "#2B2E33", "#3A3F46", "#555B64"
ME0, ME1, ME2, ME3 = "#8A9099", "#A7ADB5", "#C9CDD3", "#E4E7EB"
BL0, BL1, BL2 = "#C3C8CF", "#E2E5E9", "#F6F7F9"
PUERTO, PUERTO_IN = "#0B0C0E", "#40464E"
VERDE, AMBAR, AZUL, ROJO = "#3DDC84", "#FFB02E", "#33A1FD", "#E8423F"
PANTALLA0, PANTALLA1 = "#1E5A85", "#5BB4E5"

H = {}      # clave -> (ancho, alto, cuerpo)


def grad(gid, c0, c1, vertical=True):
    x2, y2 = ("0", "1") if vertical else ("1", "0")
    return (f'<linearGradient id="{gid}" x1="0" y1="0" x2="{x2}" y2="{y2}">'
            f'<stop offset="0" stop-color="{c0}"/><stop offset="1" stop-color="{c1}"/></linearGradient>')


def r(x, y, w, h, f, rx=0, s=None, sw=0.6):
    b = f' stroke="{s}" stroke-width="{sw}"' if s else ""
    return f'<rect x="{x:g}" y="{y:g}" width="{w:g}" height="{h:g}" rx="{rx:g}" fill="{f}"{b}/>'


def c(cx, cy, rr, f, s=None, sw=0.6):
    b = f' stroke="{s}" stroke-width="{sw}"' if s else ""
    return f'<circle cx="{cx:g}" cy="{cy:g}" r="{rr:g}" fill="{f}"{b}/>'


def p(d, f="none", s=None, sw=1.0, extra=""):
    b = f' stroke="{s}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"' if s else ""
    return f'<path d="{d}" fill="{f}"{b}{extra}/>'


def rj45(x, y, w=11, h=9, abajo=False):
    """Puerto RJ45 visto de frente, con la muesca de la traba."""
    m = w * 0.36
    if abajo:
        return (r(x, y, w, h, PUERTO, 0.6) + r(x + (w - m) / 2, y + h - 2.2, m, 2.2, PUERTO_IN)
                + r(x + 1.4, y + 1.2, w - 2.8, 1.2, PUERTO_IN))
    return (r(x, y, w, h, PUERTO, 0.6) + r(x + (w - m) / 2, y, m, 2.2, PUERTO_IN)
            + r(x + 1.4, y + h - 2.4, w - 2.8, 1.2, PUERTO_IN))


def sfp(x, y, w=13, h=8):
    return r(x, y, w, h, ME1, 0.4, ME0, 0.5) + r(x + 1.2, y + 1.6, w - 2.4, h - 3.2, PUERTO)


def orejas(w, h, color=CH1):
    """Orejas de montaje de un equipo de rack de 19 pulgadas, con sus agujeros."""
    o = ""
    for x in (0, w - 17):
        o += r(x, 0, 17, h, color, 1.2)
        for yy in ((h * 0.5,) if h < 60 else (h * 0.25, h * 0.75)):
            o += r(x + 4.5, yy - 3, 8, 6, CH0, 3)
    return o


def ventila(x, y, w, h, paso=4.2, color=CH0):
    """Rejilla de ventilación de ranuras verticales."""
    o = ""
    n = int(w // paso)
    for i in range(n):
        o += r(x + i * paso + paso * 0.25, y, paso * 0.5, h, color, paso * 0.25)
    return o


def panal(x, y, w, h, paso=5.0):
    """Frente perforado: filas de agujeros redondos desfasadas."""
    o = ""
    fila = 0
    yy = y + paso / 2
    while yy < y + h:
        xx = x + paso / 2 + (paso / 2 if fila % 2 else 0)
        while xx < x + w:
            o += c(xx, yy, paso * 0.28, CH0)
            xx += paso
        yy += paso * 0.86
        fila += 1
    return o


# ---------------------------------------------------------------- San Bernardo, rack
def rack_1u(cuerpo, gid="g", c0=CH3, c1=CH1):
    w, h = 483, 44
    return (w, h, f"<defs>{grad(gid, c0, c1)}</defs>" + r(0, 1, w, h - 2, f"url(#{gid})", 2, CH0, 0.8)
            + orejas(w, h) + cuerpo)


def fortiswitch():
    o = ""
    o += c(30, 15, 2.2, VERDE) + c(30, 25, 2.2, VERDE) + c(38, 15, 2.2, AMBAR)
    o += rj45(44, 24, 12, 9)                                            # consola
    for b in range(4):                                                  # 24 RJ45 en bloques de 6
        for i in range(6):
            x = 80 + b * 84 + i * 13
            o += rj45(x, 8, 12, 10) + rj45(x, 21, 12, 10, abajo=True)
            o += r(x + 1, 6, 2.2, 1.4, VERDE) + r(x + 8.8, 6, 2.2, 1.4, AMBAR)
    for i in range(4):                                                  # 4 SFP+
        o += sfp(420 + (i % 2) * 18, 9 + (i // 2) * 14, 15, 10)
    return rack_1u(o)


def r360():
    o = ""
    o += r(20, 6, 30, 32, CH2, 2) + c(28, 14, 2.4, AZUL) + c(28, 24, 1.8, VERDE) + c(40, 31, 3.2, ME2, CH0)
    for i in range(4):                                                  # 4 bahías de 3,5"
        x = 60 + i * 74
        o += r(x, 6, 70, 32, ME2, 1.5, ME0, 0.6) + r(x + 3, 9, 46, 26, ME1, 1)
        o += panal(x + 4, 10, 44, 24, 4.0)
        o += r(x + 52, 9, 14, 26, ME3, 1.5, ME0, 0.5) + c(x + 59, 31, 1.6, VERDE)
    o += panal(360, 7, 80, 30, 5.0)
    o += r(448, 8, 16, 28, CH2, 2) + c(456, 15, 3.4, ME2, CH0) + r(451, 24, 10, 6, PUERTO, 1)
    return rack_1u(o, c0="#4A5059", c1="#24272B")


def proveedor():
    o = r(140, 10, 200, 24, CH2, 3, CH0)
    for i in range(4):
        o += c(155 + i * 9, 22, 2.2, VERDE if i < 3 else AMBAR)
    for i in range(4):
        o += rj45(200 + i * 15, 17, 12, 10)
    o += sfp(268, 18, 16, 10) + r(296, 18, 8, 10, PUERTO, 1) + c(322, 22, 3.2, ME2, CH0)
    return rack_1u(o, c0="#3B4048", c1="#1F2226")


def patch():
    o = ""
    for i in range(24):
        x = 46 + i * 16.5 + (i // 6) * 6
        o += r(x, 16, 13, 14, BL1, 1) + r(x + 2, 18.5, 9, 8, PUERTO, 0.8) + r(x + 3.5, 18.5, 6, 2, PUERTO_IN)
        o += r(x + 3, 9, 7, 4.2, BL2, 0.6)
    return rack_1u(o)


def bandeja(*equipos):
    """Bandeja de 1 U con equipos de escritorio encima."""
    o = r(17, 34, 449, 9, ME0, 1) + r(17, 34, 449, 2.5, ME2)
    for x, w, cuerpo in equipos:
        o += cuerpo(x, w)
    return (483, 44, orejas(483, 44, ME0) + o)


def fortigate_escritorio(x, w):
    """FortiGate 90G de escritorio, visto de frente sobre la bandeja."""
    h, y = 24, 9
    s = w / 216
    o = r(x, y, w, h, CH2, 3, CH0, 0.8) + r(x, y, w, 4, CH3, 2)
    o += c(x + 9 * s, y + 9, 1.8, VERDE) + c(x + 9 * s, y + 16, 1.8, VERDE) + c(x + 16 * s, y + 9, 1.8, AMBAR)
    for i in range(10):
        o += rj45(x + 26 * s + i * 15.2 * s, y + 8, 12.4 * s, 10)
    for i in range(2):
        o += sfp(x + 182 * s + i * 16 * s, y + 9, 13 * s, 8)
    return o


def grabador_escritorio(x, w):
    """Grabador de video de escritorio con 8 puertos PoE al frente."""
    h, y = 26, 7
    s = w / 200
    o = r(x, y, w, h, CH1, 3, CH0, 0.8) + r(x, y, w, 4, CH3, 2)
    o += c(x + 12 * s, y + 13, 2.2, VERDE) + c(x + 22 * s, y + 13, 2.2, AZUL)
    for i in range(8):
        o += rj45(x + 40 * s + i * 17 * s, y + 9, 14 * s, 11)
    o += ventila(x + 182 * s, y + 7, 14 * s, 14, 3.2)
    return o


def fortigate():
    """FortiGate 90G suelto, de escritorio."""
    o = fortigate_escritorio(2, 212)
    return (216, 42, o.replace('y="9"', 'y="9"'))


def ups_2u(con_pantalla=True):
    w, h = 483, 88
    o = f"<defs>{grad('g', '#4A5059', '#22252A')}</defs>" + r(0, 1, w, h - 2, "url(#g)", 2, CH0, 0.8)
    o += orejas(w, h)
    if con_pantalla:
        o += r(30, 8, 132, 72, CH3, 4, CH0, 0.8)
        o += f"<defs>{grad('p', PANTALLA1, PANTALLA0)}</defs>" + r(42, 16, 70, 34, "url(#p)", 2, CH0, 0.8)
        for i in range(3):
            o += r(48, 22 + i * 9, 38 + (i % 2) * 14, 3, "#D8F0FF", 1)
        for i in range(4):
            o += c(124 + (i % 2) * 18, 24 + (i // 2) * 16, 5, ME2, CH0, 0.6)
        o += c(77, 64, 7, ME2, CH0, 0.8) + c(77, 64, 3, VERDE)
        o += r(124, 58, 26, 12, CH1, 2) + c(131, 64, 2, VERDE) + c(143, 64, 2, AMBAR)
        o += ventila(176, 10, 272, 68, 6.0)
    else:
        o += ventila(30, 10, 418, 68, 6.0) + r(220, 36, 40, 16, CH2, 3, CH0) + c(240, 44, 2.4, VERDE)
    return (w, h, o)


# ---------------------------------------------------------------- terminales
def rutx50():
    """Router 5G de carcasa de aluminio, con cuatro antenas de látigo arriba."""
    w, h = 140, 120
    o = f"<defs>{grad('g', '#5A6069', '#2E3238')}</defs>"
    for x, alto in ((20, 64), (44, 70), (96, 70), (120, 64)):           # antenas
        o += r(x - 3.4, 56 - alto, 6.8, alto, CH1, 3.4) + r(x - 5, 52, 10, 8, ME1, 1.5)
        o += r(x - 3.4, 56 - alto + alto * 0.62, 6.8, 2.4, CH3)
    o += r(70 - 3, 46, 6, 10, ME1, 1.5) + r(70 - 5, 42, 10, 6, CH1, 2)  # conector GNSS
    o += r(4, 58, 132, 56, "url(#g)", 6, CH0, 1)
    o += r(4, 58, 132, 7, "#6A717B", 4)
    for i in range(6):
        o += c(16 + i * 8, 74, 2.2, VERDE if i < 4 else AZUL)
    for i in range(5):
        o += rj45(14 + i * 17, 86, 14, 13)
    o += r(104, 86, 10, 13, PUERTO, 1.5) + r(120, 86, 10, 13, CH0, 5)  # SIM y energía
    return (w, h, o)


def tsw202():
    """Switch de riel DIN: 8 RJ45 con PoE y 2 SFP, con el riel por detrás."""
    w, h = 150, 74
    o = r(0, 30, w, 14, ME1, 1, ME0, 0.6) + r(0, 34, w, 2, ME0)       # riel DIN
    o += f"<defs>{grad('g', '#575D66', '#2A2E33')}</defs>" + r(8, 6, 134, 62, "url(#g)", 5, CH0, 1)
    o += r(8, 6, 134, 8, "#686F79", 4)
    for i in range(4):
        o += c(18 + i * 8, 22, 2, VERDE)
    for i in range(8):
        o += rj45(16 + (i % 4) * 22, 32 + (i // 4) * 17, 15, 12)
        o += r(16 + (i % 4) * 22 + 15.6, 33 + (i // 4) * 17, 2.4, 2.4, AMBAR, 0.5)
    o += sfp(110, 33, 22, 11) + sfp(110, 50, 22, 11)
    return (w, h, o)


def karbon():
    """Computador industrial sin ventilador: aletas de disipación arriba y puertos al frente."""
    w, h = 150, 90
    o = f"<defs>{grad('g', '#3F444B', '#1B1D20')}</defs>"
    for i in range(17):                                                 # aletas
        o += r(8 + i * 8, 2, 5, 30, "#2D3136", 1.2, CH0, 0.4)
    o += r(4, 28, 142, 58, "url(#g)", 5, CH0, 1)
    o += c(18, 44, 4.5, ME2, CH0, 0.6) + c(18, 44, 1.8, AZUL)
    o += r(30, 40, 22, 10, ME1, 2, ME0, 0.5) + r(33, 43, 16, 4, PUERTO)  # USB
    o += r(56, 40, 22, 10, ME1, 2, ME0, 0.5) + r(59, 43, 16, 4, PUERTO)
    o += rj45(86, 38, 15, 13) + rj45(106, 38, 15, 13)
    o += p("M30,60 h34 l-3,12 h-28 z", PUERTO, ME0, 0.6)               # puerto serie
    for i in range(5):
        o += c(36 + i * 5.5, 65, 1.1, ME2)
    o += r(74, 60, 34, 12, PUERTO, 2) + r(116, 60, 20, 12, CH3, 3) + c(126, 66, 2.6, VERDE)
    return (w, h, o)


def ups_torre():
    """UPS de torre con pantalla y botones arriba."""
    w, h = 64, 140
    o = f"<defs>{grad('g', '#4A5059', '#1E2125', False)}</defs>" + r(2, 2, 60, 136, "url(#g)", 5, CH0, 1)
    o += f"<defs>{grad('p', PANTALLA1, PANTALLA0)}</defs>" + r(12, 14, 40, 24, "url(#p)", 2, CH0, 0.6)
    for i in range(3):
        o += r(16, 19 + i * 6, 24 + (i % 2) * 6, 2, "#D8F0FF", 1)
    for i in range(3):
        o += c(18 + i * 14, 48, 4, ME2, CH0, 0.6)
    o += c(32, 62, 5.5, ME2, CH0, 0.6) + c(32, 62, 2.2, VERDE)
    o += ventila(12, 76, 40, 54, 5.0)
    return (w, h, o)


def inyector():
    w, h = 80, 40
    o = r(2, 6, 76, 30, BL1, 4, BL0, 1) + r(2, 6, 76, 5, BL2, 3)
    o += rj45(12, 18, 14, 12) + rj45(34, 18, 14, 12) + c(62, 24, 3, VERDE)
    return (w, h, o)


def fortiap():
    """Punto de acceso de exterior: carcasa blanca IP67 con prensaestopa abajo."""
    w, h = 80, 110
    o = f"<defs>{grad('g', BL2, BL0, False)}</defs>" + r(8, 4, 64, 88, "url(#g)", 10, "#A9AEB5", 1)
    o += r(14, 10, 52, 76, BL2, 7)
    o += c(40, 30, 3.2, AZUL)
    o += r(34, 92, 12, 8, ME1, 1.5) + r(37, 100, 6, 10, CH1, 2)
    return (w, h, o)


def minew_g1():
    """Lector de balizas: caja blanca chica con luz y un puerto de red abajo."""
    w, h = 100, 70
    o = f"<defs>{grad('g', BL2, BL0)}</defs>" + r(4, 4, 92, 54, "url(#g)", 9, "#A9AEB5", 1)
    o += r(30, 20, 40, 4, AZUL, 2) + c(50, 38, 2.6, VERDE)
    o += r(40, 58, 20, 10, CH1, 2)
    return (w, h, o)


# ---------------------------------------------------------------- camión
def g26i():
    """Computador vehicular en caja de aluminio, con conectores coaxiales y de bus al frente."""
    w, h = 160, 96
    o = f"<defs>{grad('g', ME3, ME0)}</defs>"
    for i in range(10):
        o += r(14 + i * 13.5, 2, 8, 20, ME1, 1.5, ME0, 0.5)
    o += r(4, 16, 152, 76, "url(#g)", 7, ME0, 1)
    o += r(10, 22, 140, 64, "#3A3F46", 4)
    for i, col in enumerate(("#2F6FD6", "#7B3FC4", "#1E1E1E")):          # FAKRA: LTE, GNSS, Wi-Fi
        o += r(18 + i * 22, 30, 16, 16, col, 2) + c(26 + i * 22, 38, 3.4, ME2)
    o += r(86, 28, 56, 22, CH0, 4) + r(90, 32, 48, 14, "#20242A", 2)    # conector de bus
    for i in range(8):
        o += c(95 + i * 5.6, 36, 1.2, ME2) + c(95 + i * 5.6, 42, 1.2, ME2)
    o += c(22, 66, 3, VERDE) + c(34, 66, 3, AZUL) + c(46, 66, 3, AMBAR)
    o += r(70, 58, 30, 16, CH0, 3) + r(110, 58, 30, 16, CH0, 3)
    return (w, h, o)


def iridium_edge():
    """Módem satelital: domo blanco sobre base oscura, con su cable."""
    w, h = 120, 80
    o = f"<defs>{grad('g', '#FFFFFF', BL0)}</defs>"
    o += p("M14,52 Q14,8 60,8 Q106,8 106,52 Z", "url(#g)", "#A9AEB5", 1)
    o += r(6, 50, 108, 14, CH1, 4) + r(6, 50, 108, 4, CH3, 2)
    o += p("M60,64 V72 Q60,78 70,78 H112", s=CH1, sw=4)
    return (w, h, o)


def aleta():
    """Antena de techo LTE y GNSS en forma de aleta."""
    w, h = 130, 70
    o = f"<defs>{grad('g', '#4A5059', '#16181B')}</defs>"
    o += p("M8,56 C30,54 56,40 74,14 Q80,6 88,10 C98,22 112,40 122,56 Z", "url(#g)", CH0, 1)
    o += p("M74,16 C82,26 92,38 100,52", s="#6A717B", sw=1.4)
    o += r(4, 54, 122, 10, CH0, 4)
    return (w, h, o)


def cancrocodile():
    """Lector CAN sin contacto: pinza negra sobre el par de cables del arnés."""
    w, h = 140, 70
    o = ""
    for dy, col in ((-3.5, "#F2C200"), (3.5, "#2C6FD1")):              # par trenzado del arnés
        o += p(f"M2,{35 + dy} C24,{35 - dy} 40,{35 + dy} 60,{35 - dy} S100,{35 + dy} 138,{35 - dy}", s=col, sw=4)
    o += f"<defs>{grad('g', '#4A5059', '#16181B')}</defs>"
    o += r(42, 14, 56, 42, "url(#g)", 8, CH0, 1)
    o += p("M42,30 h-8 v10 h8 M98,30 h8 v10 h-8", "#1F2226", CH0, 0.8)
    o += r(48, 18, 44, 8, "#5A6069", 3) + c(86, 46, 2.6, VERDE)
    o += p("M70,56 V66 H40", s=CH1, sw=3)
    return (w, h, o)


def lector_desfire():
    """Lector de tarjetas sin contacto: placa negra con el símbolo de lectura."""
    w, h = 64, 100
    o = f"<defs>{grad('g', '#3F444B', '#16181B', False)}</defs>" + r(4, 4, 56, 92, "url(#g)", 8, CH0, 1)
    o += r(10, 10, 44, 64, "#2A2E33", 5)
    for i, rr in enumerate((6, 11, 16)):
        o += p(f"M{28 + rr * 0.7},{42 - rr * 0.7} A{rr},{rr} 0 0 1 {28 + rr * 0.7},{42 + rr * 0.7}",
               s="#E6E9ED", sw=2.4)
    o += c(26, 42, 2.4, "#E6E9ED") + r(22, 82, 20, 5, VERDE, 2.5)
    return (w, h, o)


def baliza():
    """Baliza de semirremolque: cuerpo cuadrado redondeado, sellado, con una luz."""
    w, h = 80, 80
    o = f"<defs>{grad('g', '#5A6069', '#22252A')}</defs>" + r(4, 4, 72, 72, "url(#g)", 16, CH0, 1)
    o += c(40, 40, 22, "#2E3238", "#6A717B", 1.4) + c(40, 40, 8, "#3F444B") + c(58, 22, 2.6, AZUL)
    return (w, h, o)


def bateria_camion():
    w, h = 110, 80
    o = f"<defs>{grad('g', '#3F444B', '#16181B')}</defs>"
    o += r(18, 4, 16, 10, ME1, 2) + r(76, 4, 16, 10, ME1, 2)
    o += r(4, 12, 102, 64, "url(#g)", 5, CH0, 1) + r(4, 12, 102, 10, "#555B64", 4)
    o += p("M20,40 h12 M26,34 v12", s=ROJO, sw=3) + p("M78,40 h12", s="#E6E9ED", sw=3)
    return (w, h, o)


# ---------------------------------------------------------------- sala y patio
def generador():
    """Grupo electrógeno insonorizado: cabina con celosías, panel de control y escape."""
    w, h = 200, 120
    o = f"<defs>{grad('g', '#D9DDE2', '#9BA2AB')}</defs>"
    o += r(150, 2, 10, 18, CH1, 2)                                      # escape
    o += r(6, 14, 188, 92, "url(#g)", 5, "#6E747D", 1)
    o += r(6, 14, 188, 8, "#EEF0F3", 4)
    for x0 in (16, 106):                                                # dos puertas con celosía
        o += r(x0, 30, 78, 64, "#C2C7CE", 3, "#7D838C", 0.8)
        for i in range(9):
            o += r(x0 + 8, 36 + i * 6.2, 62, 3, "#8A9099", 1.5)
    o += r(64, 36, 22, 22, CH1, 2) + r(67, 39, 16, 9, "#9FE3B2", 1) + c(71, 53, 2, VERDE) + c(79, 53, 2, ROJO)
    o += r(2, 106, 196, 12, CH1, 2)                                     # base con estanque
    return (w, h, o)


def tablero():
    """Tablero de transferencia: gabinete metálico con visor de interruptores."""
    w, h = 80, 120
    o = f"<defs>{grad('g', '#D9DDE2', '#A3AAB3', False)}</defs>" + r(4, 4, 72, 112, "url(#g)", 4, "#6E747D", 1)
    o += r(14, 16, 52, 40, CH2, 2)
    for i in range(6):
        o += r(18 + i * 8, 24, 6, 24, BL1, 1) + r(19 + i * 8, 30 + (i % 2) * 8, 4, 6, CH1)
    o += r(64, 66, 6, 22, CH1, 2)
    o += p("M40,72 l12,22 h-24 z", AMBAR, CH0, 0.8) + p("M42,78 l-4,6 h5 l-3,6", s=CH0, sw=1.4)
    return (w, h, o)


def clima_cielo():
    """Unidad de clima de precisión de cielo: caja metálica con rejillas abajo."""
    w, h = 170, 70
    o = f"<defs>{grad('g', BL2, BL0)}</defs>" + r(4, 4, 162, 54, "url(#g)", 4, "#8A9099", 1)
    o += r(14, 12, 60, 38, "#D3D7DC", 2)
    for i in range(7):
        o += r(18, 16 + i * 5, 52, 2.4, "#9BA2AB", 1)
    o += r(84, 12, 72, 38, "#D3D7DC", 2)
    for i in range(7):
        o += r(88, 16 + i * 5, 64, 2.4, "#9BA2AB", 1)
    o += r(4, 58, 162, 8, "#8A9099", 2)
    return (w, h, o)


def camara_domo():
    """Cámara de mini domo: base blanca y domo oscuro."""
    w, h = 90, 60
    o = f"<defs>{grad('g', '#5A6069', '#0E1013')}</defs>"
    o += r(6, 6, 78, 14, BL1, 6, BL0, 1)
    o += p("M16,20 Q16,56 45,56 Q74,56 74,20 Z", "url(#g)", CH0, 1)
    o += c(45, 34, 7, "#20252C", "#6A717B", 1) + c(47, 32, 2.2, "#9FC9EA")
    return (w, h, o)


def lector_facial():
    """Terminal de rostro: placa alta con pantalla, cámara arriba y huella abajo."""
    w, h = 60, 120
    o = f"<defs>{grad('g', '#3F444B', '#121417', False)}</defs>" + r(4, 4, 52, 112, "url(#g)", 8, CH0, 1)
    o += c(30, 13, 3, "#1C3D5A", "#6A717B", 0.8)
    o += f"<defs>{grad('p', '#2B6FA8', '#0F2E4A')}</defs>" + r(10, 22, 40, 56, "url(#p)", 3)
    o += p("M30,36 a9,11 0 1,0 0.01,0 Z", s="#9FD8FF", sw=1.6) + p("M20,74 q10,-12 20,0", s="#9FD8FF", sw=1.6)
    o += r(20, 86, 20, 22, "#2A2E33", 4, "#6A717B", 0.8) + p("M25,92 q5,-4 10,0 M24,97 q6,-5 12,0 M25,102 q5,-4 10,0",
                                                              s="#8A9099", sw=1)
    return (w, h, o)


def vesda():
    """Detector por aspiración: caja clara con su barra de luces y la tubería que entra arriba."""
    w, h = 110, 90
    o = r(24, 0, 12, 20, "#E8423F", 1) + r(74, 0, 12, 20, "#E8423F", 1)
    o += f"<defs>{grad('g', BL2, BL0)}</defs>" + r(4, 16, 102, 70, "url(#g)", 6, "#8A9099", 1)
    o += r(14, 26, 82, 50, CH2, 4)
    for i, col in enumerate((VERDE, VERDE, AMBAR, AMBAR, ROJO, ROJO)):
        o += r(22 + i * 11, 36, 8, 12, col, 1.5)
    o += r(22, 56, 64, 10, "#20252C", 2) + c(30, 61, 2, VERDE)
    return (w, h, o)


def cilindro_fk():
    """Cilindro del agente de extinción, con válvula y manómetro."""
    w, h = 50, 120
    o = f"<defs>{grad('g', '#F0605D', '#A3201E', False)}</defs>"
    o += r(18, 2, 14, 10, ME1, 2) + r(12, 10, 26, 8, ME0, 2) + c(38, 14, 6, BL2, CH0, 1) + p("M38,14 l3,-3", s=CH0, sw=1)
    o += r(6, 18, 38, 98, "url(#g)", 16, "#7E1716", 1)
    o += r(10, 50, 30, 30, BL2, 2) + r(14, 56, 22, 3, CH1) + r(14, 63, 16, 3, CH1) + r(14, 70, 20, 3, CH1)
    return (w, h, o)


def rack_cerrado():
    """Rack cerrado de 24 U visto de frente: marco negro y puerta perforada con manilla."""
    w, h = 60, 120
    o = r(0, 0, 60, 120, CH1, 2, CH0, 1) + r(4, 4, 52, 108, CH2, 1)
    o += panal(7, 8, 46, 98, 4.2)
    o += r(48, 50, 4, 18, ME2, 1.5) + r(2, 112, 8, 8, CH0, 1) + r(50, 112, 8, 8, CH0, 1)
    return (w, h, o)


def torre_celular():
    """Torre de telefonía de celosía con tres antenas de panel."""
    w, h = 80, 140
    o = p("M40,30 L18,136 M40,30 L62,136", s=CH2, sw=2.4)
    for y0 in range(40, 136, 16):
        k0 = (y0 - 30) / 106
        k1 = (y0 + 16 - 30) / 106
        xl0, xr0 = 40 - 22 * k0, 40 + 22 * k0
        xl1, xr1 = 40 - 22 * min(k1, 1), 40 + 22 * min(k1, 1)
        o += p(f"M{xl0:.1f},{y0} L{xr1:.1f},{min(y0 + 16, 136)} M{xr0:.1f},{y0} L{xl1:.1f},{min(y0 + 16, 136)}",
               s=CH3, sw=1.2)
    o += p("M40,8 V32", s=CH2, sw=2.4)
    for x in (22, 40, 58):
        o += r(x - 5, 12, 10, 26, BL1, 2, "#8A9099", 1)
    o += r(12, 134, 56, 5, CH1, 1)
    return (w, h, o)


def main():
    piezas = {
        "hw-fortiswitch": fortiswitch(), "hw-r360": r360(), "hw-proveedor": proveedor(), "hw-patch": patch(),
        "hw-bandeja-fortigate": bandeja((26, 212, fortigate_escritorio), (245, 212, fortigate_escritorio)),
        "hw-bandeja-grabador": bandeja((140, 200, grabador_escritorio)),
        "hw-ups-rack": ups_2u(True), "hw-bateria-rack": ups_2u(False),
        "hw-rutx50": rutx50(), "hw-tsw202": tsw202(), "hw-karbon": karbon(), "hw-ups-torre": ups_torre(),
        "hw-inyector": inyector(), "hw-fortiap": fortiap(), "hw-minew": minew_g1(),
        "hw-g26i": g26i(), "hw-iridium": iridium_edge(), "hw-aleta": aleta(), "hw-can": cancrocodile(),
        "hw-desfire": lector_desfire(), "hw-baliza": baliza(), "hw-bateria": bateria_camion(),
        "hw-generador": generador(), "hw-tablero": tablero(), "hw-clima": clima_cielo(),
        "hw-camara": camara_domo(), "hw-facial": lector_facial(), "hw-vesda": vesda(), "hw-cilindro": cilindro_fk(),
        "hw-torre": torre_celular(), "hw-rack": rack_cerrado(), "hw-fortigate": fortigate(),
    }
    for k, (w, h, cuerpo) in piezas.items():
        with open(os.path.join(ICONOS, k + ".svg"), "w", encoding="utf-8") as f:
            f.write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:g} {h:g}">{cuerpo}</svg>\n')
    print(len(piezas), "ilustraciones de hardware")


if __name__ == "__main__":
    main()
