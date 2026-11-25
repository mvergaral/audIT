"""Subdocumento 4: la vista física completa en cinco láminas legibles (D4-163).

fisica_completa.py dibuja todo en un lienzo de 1500 x 880 pt, que en una página horizontal
queda con letra de 4,4 pt. Aquí el mismo dibujo se reparte en cinco láminas del tamaño útil
de una página horizontal (729,6 x 473,4 pt), así que la letra queda a su tamaño de origen,
9 pt o más:

  A. San Bernardo: sistemas existentes, energía y racks
  B. San Bernardo: clima, protección, acceso, torre y patio
  C. Nube: Azure Chile Central y Brazil South
  D. Terminales regionales y contrapartes
  E. Flota con equipo audIT y sus enlaces

Cada bloque conserva el código y las coordenadas de fisica_completa.py y se dibuja a través
de Mover, que lo desplaza dentro de la lámina. Lo que cambia de lugar o de tamaño está
comentado. Una conexión que sigue en otra lámina termina en un número dentro de un círculo,
el mismo en las dos láminas, y cada lámina trae la lista de esos números.
"""
from lienzo import Figura, ancho
from fisica_completa import C, ENERGIA, eq, subred, lineas_texto, energia


class Mover:
    """Dibuja sobre la figura f con las coordenadas desplazadas en (dx, dy). Las cajas que
    devuelven equipo y ficha vuelven a las coordenadas del bloque, para que el código del
    bloque siga igual."""

    def __init__(self, f, dx, dy):
        self.f, self.dx, self.dy = f, dx, dy

    def _caja(self, b):
        return (b[0] - self.dx, b[1] - self.dy, b[2] - self.dx, b[3] - self.dy)

    def texto(self, x, y, *a, **k):
        return self.f.texto(x + self.dx, y + self.dy, *a, **k)

    def rotulo(self, x, y, *a, **k):
        return self.f.rotulo(x + self.dx, y + self.dy, *a, **k)

    def ficha(self, x, y, *a, **k):
        return self._caja(self.f.ficha(x + self.dx, y + self.dy, *a, **k))

    def marcador(self, cx, cy, *a, **k):
        return self.f.marcador(cx + self.dx, cy + self.dy, *a, **k)

    def icono(self, clave, cx, cy, *a, **k):
        return self.f.icono(clave, cx + self.dx, cy + self.dy, *a, **k)

    def equipo(self, clave, cx, cy, *a, **k):
        return self._caja(self.f.equipo(clave, cx + self.dx, cy + self.dy, *a, **k))

    def nodo(self, clave, cx, cy, *a, **k):
        return self.f.nodo(clave, cx + self.dx, cy + self.dy, *a, **k) - self.dy

    def grupo(self, x, y, *a, **k):
        return self.f.grupo(x + self.dx, y + self.dy, *a, **k)

    def grupo_az(self, x, y, *a, **k):
        return self.f.grupo_az(x + self.dx, y + self.dy, *a, **k)

    def caja(self, x, y, *a, **k):
        return self.f.caja(x + self.dx, y + self.dy, *a, **k)

    def rect(self, x, y, *a, **k):
        return self.f.rect(x + self.dx, y + self.dy, *a, **k)

    def linea(self, pts, *a, **k):
        return self.f.linea([(x + self.dx, y + self.dy) for x, y in pts], *a, **k)


def cortar(s, ancho_max, tam=9):
    lineas, actual = [], ""
    for p in s.split():
        prueba = (actual + " " + p).strip()
        if actual and ancho(prueba, tam) > ancho_max:
            lineas.append(actual)
            actual = p
        else:
            actual = prueba
    return lineas + [actual]


def leyenda(f, x, y, titulo, filas, x_max=726):
    """Lista de las conexiones que siguen en otra lámina: número en círculo y texto de 9 pt,
    cortado para no pasar de x_max."""
    for i, l in enumerate(cortar(titulo, x_max - x, 10)):
        f.texto(x, y + i * 12, l, 10, 600)
    y += 12 * len(cortar(titulo, x_max - x, 10)) + 8
    for n, texto in filas:
        f.marcador(x + 7, y - 3, n)
        lineas = cortar(texto, x_max - x - 19)
        for i, l in enumerate(lineas):
            f.texto(x + 19, y + i * 10.6, l, 9)
        y += 10.6 * len(lineas) + 8
    return y


# ---------------------------------------------------------------------------- lámina A
def lamina_a():
    f = Figura("fisica-lamina-a", C, "H")
    g = Mover(f, 4, -12)

    # autoridad tributaria, fuera del sitio; el emisor llega por su propio enlace (ARQ-08)
    g.icono("flu-edificio-publico", 206, 30, 22)
    g.texto(222, 34, "Autoridad tributaria", 10)
    g.grupo(8, 72, 568, 368, "San Bernardo", sub="Sala de sitio")
    g.grupo(16, 96, 260, 100, "Capa anticorrupción", "pr-adaptador", rx=6)
    g.nodo("flu-gestion2013", 70, 140, 24, ["Sistema de gestión", "de transporte 2013"])
    g.nodo("flu-contable", 206, 140, 24, ["Sistema contable", "y de facturación"])
    g.linea([(206, 127), (206, 42)])
    g.rotulo(206, 56, ["Documentos tributarios", "por internet del emisor"])
    # energía
    g.grupo(16, 204, 260, 136, "Energía", rx=6, sub="Punto único declarado")
    ge = eq(g, "hw-generador", 80, 256, ["Grupo electrógeno"], ["Himoinsa HYW-8, 8,8 kVA", "estanque de 100 L"], w=70)
    tb = eq(g, "hw-tablero", 222, 256, ["Tablero de", "transferencia"], None, h=40)
    energia(g, [(ge[2], 256), (tb[0], 256)])
    g.rotulo(152, 259, "Energía")
    g.ficha(222, 322, "24 h con 64,3 L")

    # racks: el espacio libre se dibuja más corto que en la vista completa (66 y 96 pt menos)
    # para que la lámina quepa a tamaño natural; los equipos y sus conexiones son los mismos
    RS, RC = (300, 112, 120, 262), (436, 112, 120, 316)
    g.grupo(*RS, "Rack de servidores", rx=3, grosor=1.6)
    g.grupo(*RC, "Rack de comunicaciones", rx=3, grosor=1.6)
    xs, xc = RS[0] + RS[2] / 2, RC[0] + RC[2] / 2
    wi = 96

    def unidad(x, y, clave, nombre):
        b = g.equipo(clave, x, y, w=wi)
        lineas_texto(g, x, b[3] + 10, nombre if isinstance(nombre, list) else [nombre], anc="middle")
        return b

    def libres(x, y0, y1, lineas):
        g.rect(x - wi / 2, y0, wi, y1 - y0, relleno="#FFFFFF", borde="#9B9B9B", grosor=0.6, rx=1.5, disc=True)
        lineas_texto(g, x, (y0 + y1) / 2 + 3.2 - (len(lineas) - 1) * 5.3, lineas, anc="middle")

    libres(xs, 132, 170, ["24 U, cerca de 12", "ocupadas"])
    r360b = unidad(xs, 186, "hw-r360", "R360 B, circuitos A y B")
    unidad(xs, 212, "hw-r360", "R360 A, circuitos A y B")
    unidad(xs, 246, "hw-bateria-rack", "Batería externa B")
    upsb = unidad(xs, 282, "hw-ups-rack", "UPS SRT3000 B, circuito B")
    unidad(xs, 318, "hw-bateria-rack", "Batería externa A")
    upsa = unidad(xs, 354, "hw-ups-rack", "UPS SRT3000 A, circuito A")

    libres(xc, 132, 176, ["24 U, cerca de 8", "ocupadas"])
    fg = unidad(xc, 194, "hw-bandeja-fortigate", ["2 FortiGate 90G en HA", "circuitos A y B"])
    fsb = unidad(xc, 238, "hw-fortiswitch", "FortiSwitch B, circuito B")
    fsa = unidad(xc, 264, "hw-fortiswitch", "FortiSwitch A, circuito A")
    p1 = unidad(xc, 322, "hw-proveedor", "Proveedor ExpressRoute")
    p2 = unidad(xc, 366, "hw-proveedor", "Proveedor de la VPN")
    unidad(xc, 402, "hw-bandeja-grabador", "Grabador Axis S3008")
    g.ficha(xs, 400, "66 min con una UPS")
    xl = RC[0] + 6
    g.linea([(p2[0], 366), (xl, 366), (xl, 322)], flecha=None)
    g.linea([(p1[0], 322), (xl, 322), (xl, 194), (fg[0], 194)])
    g.rotulo(xl, 296, "WAN")
    xr = RC[0] + RC[2] - 6
    g.linea([(fg[2], 194), (xr, 194), (xr, 264), (fsa[2], 264)])
    g.linea([(xr, 238), (fsb[2], 238)])
    g.linea([(fsb[0], 246), (428, 246), (428, 198), (r360b[2], 198)], flecha="ambas")
    g.linea([(219, 140), (284, 140), (284, 198), (r360b[0], 198)], flecha="ambas")
    energia(g, [(tb[2], 256), (294, 256), (294, 354), (upsa[0], 354)])
    energia(g, [(294, 282), (upsb[0], 282)])
    g.rotulo(294, 320, "Energía")
    # salidas a otras láminas: enlaces a Azure (1 y 2), red de sala (3) y cámaras (4)
    g.linea([(p1[2], 322), (596, 322)], flecha="ambas")
    g.marcador(604, 322, 1)
    g.linea([(p2[2], 366), (596, 366)], disc=True, flecha="ambas")
    g.marcador(604, 366, 2)
    BUS = 566
    g.linea([(fsa[2], 270), (BUS, 270), (BUS, 446)], flecha=None)
    g.marcador(BUS, 453, 3)
    g.linea([(xc, 460), (xc, RC[1] + RC[3])])
    g.marcador(xc, 467, 4)
    leyenda(f, 626, 40, "Sigue en otra lámina", [
        (1, "ExpressRoute a la red central de Azure (C)"),
        (2, "VPN de respaldo por otro proveedor (C)"),
        (3, "Red de sala a lectores, torre y patio (B)"),
        (4, "Cámaras al grabador (B)"),
    ])
    return f.guardar()


# ---------------------------------------------------------------------------- lámina B
def lamina_b():
    f = Figura("fisica-lamina-b", C, "H")
    g = Mover(f, 4, -316)
    g.grupo(8, 320, 568, 412, "San Bernardo", sub="Sala de sitio")
    # clima, detección y extinción: la ficha de medidas sube y el grupo se acorta
    g.grupo(16, 348, 260, 372, "Sala: clima y protección", rx=6)
    eq(g, "hw-clima", 80, 400, "2 climas", ["Liebert Mini-Mate2", "de cielo, 3,55 kW", "N+1, muros opuestos"], w=64)
    g.nodo("flu-agua", 80, 540, 22, "Detector de agua", ["Liebert LT460, cable", "bajo los climas"])
    g.linea([(80, 529), (80, 466)])
    g.rotulo(80, 498, "Aviso al clima")
    g.nodo("flu-extintor", 210, 400, 26, "Cilindro", ["FK-5-1-12, Kidde", "Fluoro-K, junto", "a la esclusa"])
    eq(g, "hw-vesda", 210, 540, "VESDA VLF-250", ["(detección temprana", "de humo por", "aspiración)"], w=40)
    g.nodo("flu-extintor", 80, 660, 22, "2 extintores", ["de CO₂, esclusa y", "zona de trabajo"])
    g.ficha(210, 690, ["Las medidas de detalle se", "confirman en la Etapa 1"])

    # acceso, torre y patio: suben 184 pt respecto de la vista completa
    h = Mover(f, 4, -316 - 184)
    xc = 496
    BUS = 566
    h.grupo(300, 532, 256, 104, "Sala: acceso y vigilancia", rx=6)
    cm = eq(h, "hw-camara", xc, 590, "4 cámaras", "Axis M3215-LVE", w=32)
    h.linea([(xc, cm[1]), (xc, 520)])
    h.marcador(xc, 513, 4)
    h.rotulo(xc, 556, "PoE")
    lf = eq(h, "hw-facial", 360, 588, "2 lectores", "faciales, esclusa", h=30)
    h.linea([(BUS, 562), (360, 562), (360, lf[1])])
    h.grupo(300, 644, 256, 70, "Torre 24x7", rx=6)
    lineas_texto(h, 310, 680, ["22 personas en turnos;", "usan el enlace a Azure"])
    h.icono("rol-operador", 530, 680, 30)
    h.linea([(BUS, 680), (545, 680)])
    h.grupo(300, 722, 256, 142, "Patio y portería", rx=6)
    ap = eq(h, "hw-fortiap", 344, 780, "FortiAP 234G", None, h=34)
    inj = eq(h, "hw-inyector", 430, 780, "Inyector", "PoE 802.3bt", w=32)
    mn = eq(h, "hw-minew", 512, 800, "Minew G1", None, w=32)
    h.marcador(BUS, 513, 3)
    h.linea([(BUS, 520), (BUS, 800)], flecha=None)
    h.linea([(BUS, 772), (inj[2], 772)])
    h.linea([(inj[0], 780), (ap[2], 780)])
    h.linea([(BUS, 800), (mn[2], 800)])
    leyenda(f, 600, 40, "Sigue en otra lámina", [
        (3, "Red de sala desde los FortiSwitch del rack (A)"),
        (4, "Cámaras al grabador del rack (A)"),
    ])
    return f.guardar()


# ---------------------------------------------------------------------------- lámina C
def lamina_c():
    f = Figura("fisica-lamina-c", C, "H")
    g = Mover(f, -578, -38)
    xa = 740
    # usuarios y Front Door en una franja más baja que en la vista completa
    g.icono("rol-usuarios", 652, 60, 20)
    g.texto(666, 64, "Usuarios", 10)
    g.linea([(712, 60), (727, 60)])
    g.icono("az-frontdoor", xa, 60, 22)
    g.texto(xa + 16, 58, "Front Door", 10)
    g.texto(xa + 16, 69, "Premium, global", 9)
    g.linea([(xa, 72), (xa, 173)])

    g.grupo_az(596, 84, 574, 420, "Azure Chile Central", "az-region")
    g.texto(1040, 99, "Región primaria, 3 zonas", 9, anc="end")
    g.grupo_az(606, 108, 554, 272, "Red de producción", "az-vnet")
    g.texto(1040, 123, "10.11.0.0/20", 9, anc="end")
    subred(g, 616, 132, 174, 112, "Borde", "10.11.1.0/24")
    g.nodo("az-apim", xa, 186, 26, "API Management", "Premium")
    subred(g, 798, 132, 166, 112, "Aplicación", "10.11.4.0/22")
    g.nodo("az-aks", 881, 180, 26, "AKS", "Nodos en 3 zonas")
    for i in range(3):
        g.ficha(839 + i * 42, 230, f"Zona {i + 1}")
    subred(g, 972, 132, 178, 112, "Integración", "10.11.2.0/24")
    g.nodo("az-eventhubs", 1006, 180, 26, "Event Hubs", ["Premium,", "Kafka"])
    g.nodo("az-iothub", 1066, 180, 26, "IoT Hub", "S1 × 2")
    g.ficha(1066, 232, "Certificado mutuo")
    g.nodo("az-dps", 1120, 180, 26, "Provisioning", "DPS")
    g.linea([(xa + 13, 180), (868, 180)])
    g.linea([(993, 180), (894, 180)])
    g.linea([(1053, 180), (1019, 180)])
    g.linea([(1107, 180), (1079, 180)], disc=True)
    subred(g, 616, 252, 174, 120, "Gestión", "10.11.8.0/24")
    g.nodo("az-monitor", 703, 314, 26, ["Monitor y", "Log Analytics"])
    subred(g, 798, 252, 352, 120, "Datos", "10.11.3.0/24")
    datos = [("az-postgres", "PostgreSQL", "Transaccional", 840), ("az-postgres", "PostgreSQL", "Series, TimescaleDB", 930),
             ("az-storage", "Blob inmutable", "ZRS", 1022), ("az-keyvault", "Key Vault", "Premium", 1104)]
    for ic, n, d, x in datos:
        g.nodo(ic, x, 312, 26, n, d)
        g.icono("az-privateendpoint", x + 16, 301, 11)
    g.ficha(840, 362, "Primaria y espera")
    g.linea([(894, 188), (968, 188), (968, 288)], flecha=None)
    g.linea([(840, 288), (1104, 288)], flecha=None)
    for x in [d[3] for d in datos]:
        g.linea([(x, 288), (x, 299)])
    for x in (660, 820, 994):
        g.linea([(x, 244), (x, 248), (794, 248), (794, 314), (716, 314)], disc=True)
    g.grupo_az(606, 388, 334, 108, "Red central", "az-vnet", sub="10.10.0.0/22")
    g.icono("az-expressroute", 630, 418, 20)
    g.texto(644, 416, "ExpressRoute", 10)
    g.texto(644, 427, "ErGw1AZ", 9)
    g.texto(644, 439, "Circuito de 100 Mbit/s", 9)
    g.texto(644, 449.6, "EdgeConnex SCL", 9)
    g.icono("az-vpngw", 740, 466, 20)
    g.texto(754, 464, "Puerta VPN", 10)
    g.texto(754, 475, "VpnGw1AZ", 9)
    g.nodo("az-firewall", 832, 440, 26, "Firewall", "Premium")
    g.icono("az-routetable", 832, 403, 14)
    g.linea([(832, 427), (832, 410)], flecha=None)
    g.linea([(832, 396), (832, 380)])
    g.texto(822, 407, "Tabla de rutas", 9, anc="end")
    g.nodo("az-bastion", 892, 440, 26, "Bastion", ["Acceso", "administrativo"])
    g.linea([(892, 427), (892, 380)], disc=True)
    g.grupo_az(948, 388, 212, 108, "Otros ambientes", "az-subscription")
    for i, (n, r) in enumerate([("Preproducción", "10.12.0.0/20"), ("QA", "10.13.0.0/20"),
                                ("Desarrollo", "10.14.0.0/20")]):
        g.texto(958 + i * 70, 432, n, 10)
        g.texto(958 + i * 70, 443, r, 9)
    g.texto(958, 476, "Mismo código de infraestructura", 9)
    g.linea([(940, 458), (948, 458)], disc=True, flecha="ambas")
    # entradas desde otras láminas
    g.marcador(587, 418, 1)
    g.linea([(594, 418), (620, 418)], flecha="ambas")
    g.marcador(587, 462, 2)
    g.linea([(594, 462), (730, 462)], disc=True, flecha="ambas")
    g.rotulo(672, 465, "VPN de respaldo")
    g.linea([(736, 497), (736, 476)], flecha="ambas")
    g.linea([(744, 497), (744, 476)], disc=True, flecha="ambas")
    g.marcador(740, 504, 5)
    # la flota llega al IoT Hub por LTE y por Iridium
    g.linea([(1186, 100), (1072, 100), (1072, 167)])
    g.marcador(1193, 100, 6)
    g.linea([(1186, 80), (1060, 80), (1060, 167)], disc=True)
    g.marcador(1193, 80, 7)
    # contrapartes
    g.linea([(1186, 130), (1170, 130)], disc=True)
    g.marcador(1193, 130, 8)
    g.linea([(1186, 210), (1170, 210)], flecha="ambas")
    g.marcador(1193, 210, 9)

    # Brazil South: en la vista completa va arriba; aquí va en una columna a la derecha
    BX, BY, BW, BH = 1178, 250, 128, 210
    g.grupo_az(BX, BY, BW, BH, "Brazil South", "az-region")
    lineas_texto(g, BX + 8, BY + 30, ["Recuperación", "en espera, RTO 4 h", "y RPO 15 min"])
    g.caja(BX + 8, BY + 64, BW - 16, 26, [("Red central", 10, 400), ("10.20.0.0/22", 9, 400)], rx=3,
           borde="#7A7A7A", grosor=0.6, alto_linea=10.5)
    g.caja(BX + 8, BY + 96, BW - 16, 26, [("En espera", 10, 400), ("10.21.0.0/20", 9, 400)], rx=3,
           borde="#7A7A7A", grosor=0.6, alto_linea=10.5)
    for i, ic in enumerate(["az-postgres", "az-postgres", "az-storage", "az-eventhubs", "az-keyvault"]):
        g.icono(ic, BX + 20 + i * 22, BY + 140, 16)
    g.linea([(BX + 10, BY + 152), (BX + 10, BY + 155), (BX + 118, BY + 155), (BX + 118, BY + 152)],
            flecha=None, saltos=False)
    g.texto(BX + BW / 2, BY + 166, "Réplica activa", 9, anc="middle")
    g.icono("az-aks", BX + 20, BY + 190, 16)
    g.texto(BX + 34, BY + 194, "AKS en espera", 9)
    g.linea([(1150, 300), (BX, 300)], disc=True)
    filas = ["1 y 2, San Bernardo (A). 5, terminales (D).", "6, LTE, y 7, Iridium, flota (E). 8 y 9, contrapartes (D)."]
    f.texto(290, 11, "Conexiones que siguen en otra lámina", 10, 600)
    for i, l in enumerate(filas):
        f.texto(290, 22 + i * 10.6, l, 9)
    return f.guardar()


# ---------------------------------------------------------------------------- lámina D
def lamina_d():
    f = Figura("fisica-lamina-d", C, "H")
    g = Mover(f, -588, -500)
    g.grupo(596, 516, 344, 356, "Terminales", sub="× 4")
    g.grupo(604, 540, 180, 324, "Gabinete", "pr-gabinete", rx=6)
    ka = eq(g, "hw-karbon", 650, 600, "ICS-6280 A", "Activo · 24 V", w=54)
    kb = eq(g, "hw-karbon", 650, 690, "ICS-6280 B", "En espera · 24 V", w=54)
    eq(g, "hw-ups-torre", 650, 790, "UPS SRT1000XLI", "78 min con 162 W", h=40)
    rt = eq(g, "hw-rutx50", 740, 600, "RUTX50", ["Fijo ≥ 10 Mbit/s", "y 5G, dos SIM", "24 V"], w=58)
    ts = eq(g, "hw-tsw202", 740, 712, "TSW202", "Switch PoE · 48 V", w=66)
    g.ficha(740, 790, ["Opera 24 h", "sin enlace"])
    g.ficha(694, 849, ["2 fuentes DIN + módulo por bus", "A: UPS · B: otro circuito"])
    g.linea([(rt[2], 606), (778, 606), (778, 706), (ts[2], 706)], flecha="ambas")
    g.linea([(ts[0], 712), (700, 712), (700, 600), (ka[2], 600)])
    g.linea([(700, 690), (kb[2], 690)])
    g.linea([(ka[0], 606), (614, 606), (614, 696), (kb[0], 696)], disc=True, flecha="ambas")
    # uplinks del RUTX50 a la puerta VPN de Azure (lámina C)
    g.linea([(736, rt[1]), (736, 523)], flecha="ambas")
    g.linea([(744, rt[1]), (744, 523)], disc=True, flecha="ambas")
    g.marcador(740, 516, 5)
    g.rotulo(740, 533, "VPN IPsec")
    g.grupo(804, 540, 128, 140, "Portería", rx=6)
    mt = eq(g, "hw-minew", 840, 592, "Minew G1", None, w=32)
    g.nodo("pr-semirremolque", 902, 590, 26, "Semirremolque", ["Baliza,", "Bluetooth"])
    g.linea([(889, 590), (mt[2], 590)])
    g.nodo("pr-barrera", 840, 646, 20, "Barrera")
    g.grupo(804, 688, 128, 176, "Patio", rx=6)
    it = eq(g, "hw-inyector", 836, 730, "Inyector", "PoE 802.3bt", w=30)
    at = eq(g, "hw-fortiap", 884, 734, "FortiAP", "234G", h=34)
    g.linea([(ts[2], 718), (790, 718), (790, 596), (mt[0], 596)])
    g.rotulo(790, 650, "PoE")
    g.linea([(ts[2], 726), (it[0], 726)])
    g.linea([(it[2], 730), (at[0], 730)])
    # Wi-Fi del patio al equipo a bordo (lámina E)
    g.linea([(at[2], 734), (947, 734)], flecha="ambas")
    g.marcador(954, 734, 11)

    # contrapartes: los fabricantes suben 40 pt y el grupo se acorta
    h = Mover(f, -924, 0)
    h.grupo(1300, 8, 192, 420, "Contrapartes")
    h.grupo(1308, 30, 176, 96, "Por lotes", rx=6)
    h.nodo("flu-combustible", 1352, 64, 20, ["Estaciones", "de servicio"])
    h.nodo("flu-peaje", 1440, 64, 20, "Peajes")
    h.grupo(1308, 134, 176, 200, "En línea", rx=6)
    h.nodo("flu-empresa", 1352, 172, 20, "Clientes")
    h.nodo("flu-edificio-publico", 1440, 172, 20, "Aduana")
    h.nodo("flu-edificio-publico", 1352, 254, 20, ["Dirección", "del Trabajo"])
    h.nodo("pr-rastreador", 1432, 254, 22, ["Plataformas de", "3 proveedores"],
           ["2 solo consulta,", "1 sin exportación"])
    h.nodo("flu-fabrica", 1380, 370, 22, "Fabricantes", ["Autorización", "de lectura"])
    h.linea([(1308, 110), (1290, 110)], disc=True)
    h.marcador(1283, 110, 8)
    h.linea([(1308, 210), (1290, 210)], flecha="ambas")
    h.marcador(1283, 210, 9)
    h.linea([(1443, 254), (1476, 254), (1476, 421)], flecha=None)
    h.marcador(1476, 428, 12)
    leyenda(f, 584, 40, "Sigue en otra lámina", [
        (5, "VPN IPsec a la puerta VPN de Azure (C)"),
        (8, "Archivos por lotes a Azure (C)"),
        (9, "Servicios en línea con Azure (C)"),
        (11, "Wi-Fi del patio al equipo a bordo (E)"),
        (12, "Flota de terceros por sus plataformas (E)"),
    ])
    return f.guardar()


# ---------------------------------------------------------------------------- lámina E
def lamina_e():
    f = Figura("fisica-lamina-e", C, "H")
    g = Mover(f, -930, -404)
    # enlaces de la flota: en la vista completa bajan desde el IoT Hub; aquí van en una franja
    # sobre la flota y suben a la lámina C
    XL, XI, XP = 1200, 1268, 1340
    to = g.equipo("hw-torre", XL, 466, h=40)
    g.rotulo(XL, to[3] + 14, ["Operador", "móvil"], tam=9)
    g.linea([(XL, to[1]), (XL, 427)])
    g.marcador(XL, 420, 6)
    sa = g.equipo("oc-satelite", XI, 466, w=36)
    pi = g.equipo("flu-antena-tierra", XP, 466, w=24)
    g.linea([(sa[2], 466), (pi[0], 466)], disc=True, flecha=None)
    g.linea([(XP, pi[1]), (XP, 427)], disc=True)
    g.marcador(XP, 420, 7)
    g.rotulo(XI, sa[3] + 12, "Satélite", tam=9)
    g.rotulo(XP, pi[3] + 12, ["Puerta", "Iridium"], tam=9)

    g.grupo(952, 516, 540, 356, "Flota con equipo audIT", sub="182 tractocamiones")
    g.grupo(960, 540, 84, 66, None, rx=6)
    g.nodo("flu-camion", 1002, 562, 24, "148 propios", "y 34 de terceros")
    g.grupo(1052, 540, 116, 66, None, rx=6)
    ir = eq(g, "hw-iridium", 1082, 566, "Iridium Edge", None, w=34)
    al = eq(g, "hw-aleta", 1140, 568, "LTE y GNSS", None, w=36)
    g.linea([(XL, to[3]), (XL, 568), (al[2], 568)], flecha="ambas")
    g.linea([(XI, sa[3]), (XI, 548), (1082, 548), (1082, ir[1])], disc=True, flecha="ambas")
    GB = (960, 624, 200, 172)
    g.grupo(*GB, "iWave G26I", rx=6, grosor=1.2, sub="en la cabina")
    g.equipo("hw-g26i", 1128, 645, w=40)
    partes = [("dev-linux", 994, 680, "Linux", None),
              ("cmp-elemento-seguro", 1060, 680, ["Elemento", "seguro TA100"], ["Arranque", "seguro y claves"]),
              ("fui-codigo", 1126, 680, ["audIT", "EdgeHub"], None),
              ("flu-ubicacion", 994, 752, ["Motor de", "geocercas"], None),
              ("flu-espera", 1060, 752, ["Búfer de", "288 h"], None),
              ("dev-sqlite", 1126, 752, ["SQLite en", "modo WAL"], None)]
    for ic, cx, cy, n, d in partes:
        g.nodo(ic, cx, cy, 18, n, d)
    g.linea([(1082, 606), (1082, GB[1])], flecha="ambas")
    g.rotulo(1082, 616, "RS232")
    g.linea([(1140, 606), (1140, GB[1])], flecha="ambas")
    g.rotulo(1140, 616, "Coaxial")
    # Wi-Fi del patio del terminal (lámina D)
    g.marcador(943, 734, 11)
    g.linea([(950, 734), (GB[0], 734)], flecha="ambas")
    g.grupo(1168, 624, 144, 240, None, rx=6)

    def periferico(clave, y, w=None, h=None, lineas=()):
        b = g.equipo(clave, 1192, y, w=w, h=h)
        g.texto(1214, y - 2, lineas[0], 10)
        lineas_texto(g, 1214, y + 9, lineas[1:])
        return b
    cn = periferico("hw-can", 664, w=40, lineas=["CANCrocodile", "CAN J1939, sin", "cortar el arnés"])
    g.ficha(1240, 703, ["61 con telemetría", "de fábrica, solo lectura"])
    g.linea([(cn[0], 664), (GB[0] + GB[2], 664)])
    ld = periferico("hw-desfire", 736, h=30, lineas=["Lector DESFire", "GAO MIFARE", "RS485"])
    g.linea([(ld[0], 736), (GB[0] + GB[2], 736)])
    bt = periferico("hw-bateria", 816, w=32, lineas=["Batería", "9 a 32 V"])
    energia(g, [(bt[0], 816), (1164, 816), (1164, 788), (GB[0] + GB[2], 788)])
    g.grupo(960, 804, 200, 60, None, rx=6)
    g.icono("pr-semirremolque", 984, 834, 28)
    g.texto(1002, 832, "210 semirremolques", 10)
    g.texto(1002, 843, "44 refrigerados", 9)
    bz = g.equipo("hw-baliza", 1134, 828, w=18)
    g.texto(1134, 853, "Baliza", 9, anc="middle")
    g.linea([(1134, bz[1]), (1134, GB[1] + GB[3])])
    g.grupo(1320, 540, 164, 66, "Flota de terceros", rx=6)
    g.icono("flu-camion", 1342, 584, 24)
    g.texto(1360, 582, "192 tractocamiones", 10)
    g.texto(1360, 593, "con equipo propio", 9)
    g.linea([(1476, 540), (1476, 523)])
    g.marcador(1476, 516, 12)
    g.grupo(1320, 614, 164, 250, "Memoria del G26I", "pr-memoria", rx=6, sub="eMMC 8 GB")
    celdas = [("Arranque", "16 MB"), ("Sistema A", "1 GB"), ("Sistema B", "1 GB"), ("Búfer 288 h", "38,4 MB"),
              ("Registros", "256 MB"), ("Geocercas y maestros", "16 MB")]
    for i, (n, tam) in enumerate(celdas):
        yy = 640 + i * 30
        g.rect(1350, yy, 126, 26, borde="#404040", grosor=0.75)
        g.texto(1356, yy + 11, n, 10 if len(n) < 14 else 9)
        g.texto(1356, yy + 21.5, tam, 9)
    g.linea([(1350, 683), (1338, 683), (1338, 713), (1350, 713)], flecha="ambas")
    g.texto(1413, 838, "Total 2,4 GB de 8 GB", 10, anc="middle")
    g.texto(1413, 851, "Actualización A y B", 9, anc="middle")
    leyenda(f, 576, 140, "Sigue en otra lámina", [
        (6, "LTE al IoT Hub de Azure (C)"),
        (7, "Iridium al IoT Hub de Azure, hasta 340 bytes por mensaje (C)"),
        (11, "Wi-Fi del patio del terminal (D)"),
        (12, "Plataformas de sus proveedores (D)"),
    ])
    return f.guardar()


FIGURAS = [lamina_a, lamina_b, lamina_c, lamina_d, lamina_e]
