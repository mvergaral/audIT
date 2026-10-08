"""Tres figuras propuestas al equipo (segunda vuelta). Van en propuestas/.

Las alturas en unidades de rack de cada equipo, salvo el Dell R360 (1 U, T-11), no
están en las fuentes: son supuestos que suman lo que dice el S4 y quedan anotados
en INFORME.md.
"""
from lienzo import Figura, ancho, GRIS_CLARO

CP = "propuestas"


def racks_san_bernardo():
    f = Figura("racks-san-bernardo", CP, "V", alto=452)
    u = 15.0                       # puntos por unidad de rack
    base = 412                     # borde inferior de la unidad 1
    racks = [("Rack de servidores", 46, [(1, 2, "UPS SRT3000 A"), (3, 2, "Batería SRT96RMBP A"),
                                           (5, 2, "UPS SRT3000 B"), (7, 2, "Batería SRT96RMBP B"),
                                           (10, 1, "Dell R360 A"), (11, 1, "Dell R360 B")], (12, 24)),
             ("Rack de comunicaciones", 256, [(1, 1, "Proveedor 1"), (2, 1, "Proveedor 2"),
                                              (4, 1, "Panel de conexión"), (5, 1, "FortiSwitch 124F-POE A"),
                                              (6, 1, "FortiSwitch 124F-POE B"), (7, 1, "Panel de conexión"),
                                              (8, 1, "2 × FortiGate 90G, bandeja")], (9, 24))]
    w = 150
    for titulo, x, equipos, (l0, l1) in racks:
        f.texto(x + w / 2, 18, titulo, 10, 600, "middle")
        f.texto(x + w / 2, 30, "24 U", 9, anc="middle")
        f.rect(x - 6, base - 24 * u - 6, w + 12, 24 * u + 12, relleno="#FFFFFF", borde="#2B2B2B", grosor=2.2, rx=2)
        for i in range(1, 25):
            y = base - i * u
            f.rect(x, y, w, u, relleno="#FFFFFF", borde="#D3D3D3", grosor=0.4)
            f.texto(x - 10, y + u / 2 + 3.2, str(i), 9, anc="end")
        for ui, alto, nombre in equipos:
            y = base - (ui - 1 + alto) * u
            f.rect(x + 2, y + 1, w - 4, alto * u - 2, relleno="#FFFFFF", borde="#404040", grosor=0.9, rx=1.5)
            f.texto(x + w / 2, y + alto * u / 2 + 3.4, nombre, 9, anc="middle")
        y0 = base - l1 * u
        f.rect(x + 2, y0 + 1, w - 4, (l1 - l0 + 1) * u - 2, relleno="#FFFFFF", borde="#9B9B9B", grosor=0.6,
               rx=1.5, disc=True)
        f.texto(x + w / 2, y0 + (l1 - l0 + 1) * u / 2 + 3.4, f"Libre, unidades {l0} a {l1}", 9, anc="middle")
    f.ficha(46 + w / 2, 438, "Cerca de 12 U ocupadas")
    f.ficha(256 + w / 2, 438, "Cerca de 8 U ocupadas")
    return f.guardar()


def instalacion_a_bordo():
    f = Figura("instalacion-a-bordo", CP, "H")
    tinta, gris, gris2 = "#433B6B", "#D3D3D3", "#E1D8EC"
    suelo = 352
    # semirremolque
    f.rect(60, 150, 400, 150, relleno=gris2, borde="#9B9B9B", grosor=1, rx=3)
    f.rect(60, 300, 400, 10, relleno=tinta, borde=None)
    f.rect(386, 310, 8, 34, relleno=tinta, borde=None)
    for x in (120, 182):
        f.crudo(f'<circle cx="{x}" cy="330" r="22" fill="#321B41"/><circle cx="{x}" cy="330" r="8" fill="#B4ACBC"/>')
    # tractocamión
    f.rect(452, 296, 214, 16, relleno=tinta, borde=None)
    f.rect(452, 286, 62, 10, relleno="#9B9B9B", borde=None)
    f.crudo('<path d="M528,296 V176 Q528,150 556,150 H632 Q660,150 666,178 L676,232 V296 Z" fill="#00A6ED"/>')
    f.crudo('<path d="M600,164 H640 Q652,164 656,180 L664,222 H600 Z" fill="#26C9FC"/>')
    f.rect(515, 160, 8, 120, relleno="#9B9B9B", borde=None, rx=2)
    for x in (560, 636):
        f.crudo(f'<circle cx="{x}" cy="330" r="22" fill="#321B41"/><circle cx="{x}" cy="330" r="8" fill="#B4ACBC"/>')
    f.linea([(40, suelo), (700, suelo)], flecha=None, color="#9B9B9B", saltos=False)
    # arnés CAN del camión, a lo largo del chasis
    f.linea([(540, 290), (660, 290)], flecha=None, grosor=3, color="#9B9B9B", saltos=False)
    # piezas instaladas
    piezas = [("pr-aleta", 568, 140, 18, ["Antena LTE y GNSS", "Techo de la cabina"], 470, 60),
              ("pr-iridium", 618, 140, 18, ["Iridium Edge", "Techo de la cabina"], 640, 60),
              ("pr-g26i", 572, 220, 18, ["iWave G26I", "Cabina"], 720, 160),
              ("pr-lector-tarjeta", 612, 244, 16, ["Lector DESFire", "Al alcance del", "conductor detenido"], 720, 236),
              ("pr-can", 608, 290, 20, ["CANCrocodile", "Sobre el arnés original,", "sin cortarlo"], 720, 400),
              ("pr-baliza", 428, 318, 18, ["Baliza EYE Sensor", "Chasis delantero,", "a la sombra"], 330, 420)]
    for ic, x, y, s, texto, fx, fy in piezas:
        f.rect(x - s / 2 - 2, y - s / 2 - 2, s + 4, s + 4, relleno="#FFFFFF", borde=None, rx=3, capa="frente")
        f.icono(ic, x, y, s)
        derecha = fx > 700
        x0, y0, x1, y1 = f.ficha(fx, fy, texto, anc="end" if derecha else "middle")
        if derecha:
            yc = (y0 + y1) / 2
            f.linea([(x + s / 2 + 2, y), (x0 - 10, y), (x0 - 10, yc), (x0, yc)], flecha=None, grosor=0.6, saltos=False)
        else:
            borde = y1 if fy < y else y0
            f.linea([(x, y - s / 2 - 2 if fy < y else y + s / 2 + 2), (x, borde)] if x0 < x < x1 else
                    [(x, y - s / 2 - 2 if fy < y else y + s / 2 + 2), (x, (borde + y) / 2), ((x0 + x1) / 2, (borde + y) / 2),
                     ((x0 + x1) / 2, borde)], flecha=None, grosor=0.6, saltos=False)
    f.texto(260, 230, "Semirremolque", 10, anc="middle")
    f.texto(596, 268, "Tractocamión", 10, anc="middle")
    return f.guardar()


def documento_sin_cobertura():
    f = Figura("documento-sin-cobertura", CP, "V", alto=560)
    # alternativa: emisión anticipada
    f.grupo(8, 8, 406, 112, "Si los datos se conocen al asignar")
    f.nodo("flu-portapapeles", 70, 58, 24, "Orden")
    f.nodo("flu-contable", 210, 58, 24, ["Sistema contable"], "Emite antes")
    f.nodo("flu-camion", 350, 58, 24, ["Entra con", "su folio"])
    f.linea([(83, 58), (197, 58)])
    f.linea([(223, 58), (337, 58)])
    f.rotulo(280, 61, "Folio")
    # en el punto, sin cobertura
    f.grupo(8, 132, 406, 420, "Si solo se conocen en el punto sin cobertura")
    cx = 80
    f.marcador(36, 176, 1)
    f.nodo("flu-camion", cx, 176, 26, "Punto sin señal")
    f.marcador(36, 252, 2)
    f.nodo("pr-g26i", cx, 252, 24, "iWave G26I", "Datos mínimos")
    f.nodo("flu-satelite", cx, 336, 24, "Iridium")
    f.marcador(36, 420, 3)
    f.nodo("az-iothub", cx, 420, 24, "IoT Hub")
    f.linea([(cx, 205), (cx, 239)], flecha=None)
    f.linea([(cx, 290), (cx, 323)], flecha="ambas")
    f.rotulo(cx, 309, "≤ 340 bytes")
    f.linea([(cx, 366), (cx, 407)], flecha="ambas")
    f.nodo("pr-servicio", 200, 420, 24, ["Operación", "de fletes"])
    f.linea([(93, 420), (187, 420)], flecha="ambas")
    f.nodo("pr-adaptador", 310, 420, 24, ["Capa", "anticorrupción"])
    f.linea([(213, 420), (297, 420)], flecha="ambas")
    f.marcador(286, 316, 4)
    f.nodo("flu-contable", 310, 316, 26, "Sistema contable", "Único emisor")
    f.linea([(310, 407), (310, 360)], flecha="ambas")
    # el folio vuelve por el mismo canal y el camión sale
    f.ficha(310, 250, ["El folio vuelve", "por el mismo canal"])
    f.linea([(310, 303), (310, 258)], flecha=None, disc=True)
    f.marcador(250, 250, 5)
    f.linea([(310, 242), (310, 206)], disc=True)
    f.nodo("flu-camion", 310, 176, 26, "Sale con su folio")
    f.marcador(286, 162, 6)
    f.linea([(94, 176), (296, 176)])
    f.rotulo(196, 179, "Con el folio emitido")
    return f.guardar()


FIGURAS = [racks_san_bernardo, instalacion_a_bordo, documento_sin_cobertura]
