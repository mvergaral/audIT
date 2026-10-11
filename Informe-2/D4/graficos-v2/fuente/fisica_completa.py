"""Subdocumento 4: estructura física completa en una sola figura (tercera vuelta).

Junta fisica-general, region-primaria y equipo-a-bordo sin quitar nada, con los
equipos dibujados (hardware.py) y las conexiones de cada uno. Base: contenido.tex
del S4 (4.2.1, 4.2.2, 4.2.8, 4.3.1) y el Formulario T-11. Va a tamaño natural y
en una versión reducida a oficio apaisado para ver cómo queda.

Las posiciones de los equipos dentro de cada rack son supuestos (el T-11 solo dice
qué rack lleva cada equipo y cuántas unidades ocupa cada rack).
"""
from lienzo import Figura, ancho, GRIS_CLARO

C = "04-arquitectura"
ENERGIA = "#8C8C8C"
OFICIO = (308.0, 167.0)       # área útil de una página oficio apaisada, en mm


def eq(f, clave, cx, cy, nombre=None, dato=None, w=None, h=None, tam=10):
    """Equipo dibujado con su nombre (10 pt) y dato (9 pt) debajo. Devuelve la caja del dibujo."""
    b = f.equipo(clave, cx, cy, w=w, h=h)
    y = b[3] + tam + 1
    for l in (nombre if isinstance(nombre, (list, tuple)) else ([nombre] if nombre else [])):
        f.texto(cx, y, l, tam, anc="middle")
        y += tam + 2
    for l in (dato if isinstance(dato, (list, tuple)) else ([dato] if dato else [])):
        f.texto(cx, y - 0.5, l, 9, anc="middle")
        y += 10.5
    return b


def subred(f, x, y, w, h, nombre, rango):
    f.grupo_az(x, y, w, h, nombre, "az-subnet", subred=True)
    f.texto(x + 25, y + 26.5, rango, 9)
    f.icono("az-nsg", x + w - 10, y + 10, 11)


def lineas_texto(f, x, y, lineas, tam=9, anc="start", paso=10.6):
    for i, l in enumerate(lineas):
        f.texto(x, y + i * paso, l, tam, anc=anc)


def energia(f, pts):
    f.linea(pts, flecha=None, color=ENERGIA, grosor=1.8, saltos=False)


def fisica_completa():
    W, H = 1500, 880
    f = Figura("fisica-completa", C, "L", alto=H, ancho_pt=W)

    # ================================================================ fuera de San Bernardo, arriba
    f.icono("flu-edificio-publico", 206, 30, 22)
    f.texto(222, 34, "Autoridad tributaria", 10)

    # ================================================================ San Bernardo
    f.grupo(8, 72, 568, 800, "San Bernardo", sub="Sala de sitio")
    # -- capa anticorrupción: sistemas existentes
    f.grupo(16, 96, 260, 100, "Capa anticorrupción", "pr-adaptador", rx=6)
    f.nodo("flu-gestion2013", 70, 140, 24, ["Sistema de gestión", "de transporte 2013"])
    f.nodo("flu-contable", 206, 140, 24, ["Sistema contable", "y de facturación"])
    f.linea([(206, 127), (206, 42)])
    f.rotulo(206, 60, "Documentos tributarios")
    # -- energía: grupo electrógeno y tablero de transferencia
    f.grupo(16, 204, 260, 136, "Energía", rx=6, sub="Punto único declarado")
    ge = eq(f, "hw-generador", 80, 256, ["Grupo electrógeno"], ["Himoinsa HYW-8, 8,8 kVA", "estanque de 100 L"], w=70)
    tb = eq(f, "hw-tablero", 222, 256, ["Tablero de", "transferencia"], None, h=40)
    energia(f, [(ge[2], 256), (tb[0], 256)])
    f.rotulo(152, 259, "Energía")
    f.ficha(222, 322, "24 h con 64,3 L")
    # -- sala: clima, detección y extinción
    f.grupo(16, 348, 260, 516, "Sala: clima y protección", rx=6)
    cl = eq(f, "hw-clima", 80, 400, "2 climas", ["Liebert Mini-Mate2", "de cielo, 3,55 kW", "N+1, muros opuestos"], w=64)
    ag = f.nodo("flu-agua", 80, 540, 22, "Detector de agua", ["Liebert LT460, cable", "bajo los climas"])
    f.linea([(80, 529), (80, 466)])
    f.rotulo(80, 498, "Aviso al clima")
    fk = f.nodo("flu-extintor", 210, 400, 26, "Cilindro", ["FK-5-1-12, Kidde", "Fluoro-K, junto", "a la esclusa"])
    ve = eq(f, "hw-vesda", 210, 540, "VESDA VLF-250", ["(detección temprana", "de humo por", "aspiración)"], w=40)
    f.nodo("flu-extintor", 80, 660, 22, "2 extintores", ["de CO₂, esclusa y", "zona de trabajo"])
    f.ficha(146, 836, ["Las medidas de detalle se", "confirman en la Etapa 1"])

    # -- racks: servidores (izquierda) y comunicaciones (derecha)
    RS, RC = (300, 112, 120, 328), (436, 112, 120, 412)
    f.grupo(*RS, "Rack de servidores", rx=3, grosor=1.6)
    f.grupo(*RC, "Rack de comunicaciones", rx=3, grosor=1.6)
    xs, xc = RS[0] + RS[2] / 2, RC[0] + RC[2] / 2
    wi = 96

    def unidad(x, y, clave, nombre):
        b = f.equipo(clave, x, y, w=wi)
        lineas_texto(f, x, b[3] + 10, nombre if isinstance(nombre, list) else [nombre], anc="middle")
        return b

    def libres(x, y0, y1, lineas):
        f.rect(x - wi / 2, y0, wi, y1 - y0, relleno="#FFFFFF", borde="#9B9B9B", grosor=0.6, rx=1.5, disc=True)
        lineas_texto(f, x, (y0 + y1) / 2 + 3.2 - (len(lineas) - 1) * 5.3, lineas, anc="middle")

    libres(xs, 132, 236, ["24 U, cerca", "de 12 ocupadas", "", "Espacio libre"])
    r360b = unidad(xs, 252, "hw-r360", "R360 B, circuitos A y B")
    r360a = unidad(xs, 278, "hw-r360", "R360 A, circuitos A y B")
    batb = unidad(xs, 312, "hw-bateria-rack", "Batería externa B")
    upsb = unidad(xs, 348, "hw-ups-rack", "UPS SRT3000 B, circuito B")
    bata = unidad(xs, 384, "hw-bateria-rack", "Batería externa A")
    upsa = unidad(xs, 420, "hw-ups-rack", "UPS SRT3000 A, circuito A")
    f.ficha(xs, 456, "66 min con una UPS")

    libres(xc, 132, 272, ["24 U, cerca", "de 8 ocupadas", "", "Espacio libre"])
    fg = unidad(xc, 290, "hw-bandeja-fortigate", ["2 FortiGate 90G en HA", "circuitos A y B"])
    fsb = unidad(xc, 334, "hw-fortiswitch", "FortiSwitch B, circuito B")
    fsa = unidad(xc, 360, "hw-fortiswitch", "FortiSwitch A, circuito A")
    p1 = unidad(xc, 418, "hw-proveedor", "Proveedor ExpressRoute")
    p2 = unidad(xc, 462, "hw-proveedor", "Proveedor de la VPN")
    grab = unidad(xc, 498, "hw-bandeja-grabador", "Grabador Axis S3008")
    # proveedores al par de FortiGate, por la izquierda del rack
    xl = RC[0] + 6
    f.linea([(p2[0], 462), (xl, 462), (xl, 418)], flecha=None)
    f.linea([(p1[0], 418), (xl, 418), (xl, 290), (fg[0], 290)])
    f.rotulo(xl, 392, "WAN")
    # FortiGate a los dos switches, por la derecha
    xr = RC[0] + RC[2] - 6
    f.linea([(fg[2], 290), (xr, 290), (xr, 360), (fsa[2], 360)])
    f.linea([(xr, 334), (fsb[2], 334)])
    # switches a los servidores, entre los racks
    f.linea([(fsb[0], 342), (428, 342), (428, 264), (r360b[2], 264)], flecha="ambas")
    # sistema contable a los servidores: la pasarela de la capa anticorrupción corre en los R360
    f.linea([(219, 140), (284, 140), (284, 264), (r360b[0], 264)], flecha="ambas")
    # energía: tablero de transferencia a las dos UPS
    energia(f, [(tb[2], 256), (294, 256), (294, 420), (upsa[0], 420)])
    energia(f, [(294, 348), (upsb[0], 348)])
    f.rotulo(294, 306, "Energía")

    # -- red de sala, desde los switches por el costado derecho
    BUS = 566
    f.linea([(fsa[2], 366), (BUS, 366), (BUS, 812)], flecha=None)
    # acceso y vigilancia
    f.grupo(300, 532, 256, 104, "Sala: acceso y vigilancia", rx=6)
    cm = eq(f, "hw-camara", xc, 590, "4 cámaras", "Axis M3215-LVE", w=32)
    f.linea([(xc, cm[1]), (xc, RC[1] + RC[3])])
    f.rotulo(xc, 556, "PoE")
    lf = eq(f, "hw-facial", 360, 588, "2 lectores", "faciales, esclusa", h=30)
    f.linea([(BUS, 562), (360, 562), (360, lf[1])])
    # torre de control
    f.grupo(300, 644, 256, 70, "Torre 24x7", rx=6)
    lineas_texto(f, 310, 680, ["22 personas en turnos;", "usan el enlace a Azure"])
    f.icono("rol-operador", 530, 680, 30)
    f.linea([(BUS, 680), (545, 680)])
    # patio y portería
    f.grupo(300, 722, 256, 142, "Patio y portería", rx=6)
    ap = eq(f, "hw-fortiap", 344, 780, "FortiAP 234G", None, h=34)
    inj = eq(f, "hw-inyector", 430, 780, "Inyector", "PoE 802.3bt", w=32)
    mn = eq(f, "hw-minew", 512, 800, "Minew G1", None, w=32)
    f.linea([(BUS, 772), (inj[2], 772)])
    f.linea([(inj[0], 780), (ap[2], 780)])
    f.linea([(BUS, 800), (mn[2], 800)])
    f.rotulo(BUS, 840, "PoE") if False else None

    # ================================================================ Azure
    xa = 740
    f.icono("rol-usuarios", xa, 20, 20)
    f.texto(xa + 16, 24, "Usuarios", 10)
    f.icono("az-frontdoor", xa, 54, 24)
    f.texto(xa + 18, 52, "Front Door", 10)
    f.texto(xa + 18, 63, "Premium, global", 9)
    f.linea([(xa, 30), (xa, 42)])
    # Brazil South, en espera
    f.grupo_az(830, 4, 336, 62, "Brazil South", "az-region", sub="Recuperación en espera, RTO 4 h y RPO 15 min")
    f.caja(838, 30, 84, 26, [("Red central", 10, 400), ("10.20.0.0/22", 9, 400)], rx=3, borde="#7A7A7A",
           grosor=0.6, alto_linea=10.5)
    f.caja(928, 30, 84, 26, [("En espera", 10, 400), ("10.21.0.0/20", 9, 400)], rx=3, borde="#7A7A7A",
           grosor=0.6, alto_linea=10.5)
    # servicios con réplica activa y el AKS en espera (detalle en region-secundaria)
    for i, ic in enumerate(["az-postgres", "az-postgres", "az-storage", "az-eventhubs", "az-keyvault"]):
        f.icono(ic, 1028 + i * 22, 38, 16)
    f.linea([(1020, 50), (1020, 53), (1124, 53), (1124, 50)], flecha=None, saltos=False)
    f.texto(1072, 63, "Réplica activa", 9, anc="middle")
    f.icono("az-aks", 1142, 38, 16)
    f.texto(1142, 63, "En espera", 9, anc="middle")
    f.linea([(930, 84), (930, 66)], disc=True)
    f.texto(936, 79, "Réplica asíncrona", 9)

    f.grupo_az(596, 84, 574, 420, "Azure Chile Central", "az-region")
    f.texto(1040, 99, "Región primaria, 3 zonas", 9, anc="end")
    f.grupo_az(606, 108, 554, 272, "Red de producción", "az-vnet")
    f.texto(1040, 123, "10.11.0.0/20", 9, anc="end")
    subred(f, 616, 132, 174, 112, "Borde", "10.11.1.0/24")
    f.nodo("az-apim", xa, 186, 26, "API Management", "Premium")
    f.linea([(xa, 66), (xa, 173)])
    subred(f, 798, 132, 166, 112, "Aplicación", "10.11.4.0/22")
    f.nodo("az-aks", 881, 180, 26, "AKS", "Nodos en 3 zonas")
    for i in range(3):
        f.ficha(839 + i * 42, 230, f"Zona {i + 1}")
    subred(f, 972, 132, 178, 112, "Integración", "10.11.2.0/24")
    f.nodo("az-eventhubs", 1006, 180, 26, "Event Hubs", ["Premium,", "Kafka"])
    f.nodo("az-iothub", 1066, 180, 26, "IoT Hub", "S1 × 2")
    f.ficha(1066, 232, "Certificado mutuo")
    f.nodo("az-dps", 1120, 180, 26, "Provisioning", "DPS")
    f.linea([(xa + 13, 180), (868, 180)])
    f.linea([(993, 180), (894, 180)])
    f.linea([(1053, 180), (1019, 180)])
    f.linea([(1107, 180), (1079, 180)], disc=True)
    subred(f, 616, 252, 174, 120, "Gestión", "10.11.8.0/24")
    f.nodo("az-monitor", 703, 314, 26, ["Monitor y", "Log Analytics"])
    subred(f, 798, 252, 352, 120, "Datos", "10.11.3.0/24")
    datos = [("az-postgres", "PostgreSQL", "Transaccional", 840), ("az-postgres", "PostgreSQL", "Series, TimescaleDB", 930),
             ("az-storage", "Blob inmutable", "ZRS", 1022), ("az-keyvault", "Key Vault", "Premium", 1104)]
    for ic, n, d, x in datos:
        f.nodo(ic, x, 312, 26, n, d)
        f.icono("az-privateendpoint", x + 16, 301, 11)
    f.ficha(840, 362, "Primaria y espera")
    # AKS escribe en los datos por un bus
    f.linea([(894, 188), (968, 188), (968, 288)], flecha=None)
    f.linea([(840, 288), (1104, 288)], flecha=None)
    for x in [d[3] for d in datos]:
        f.linea([(x, 288), (x, 299)])
    # todo se registra en Monitor
    for x in (660, 820, 994):
        f.linea([(x, 244), (x, 248), (794, 248), (794, 314), (716, 314)], disc=True)
    # red central
    f.grupo_az(606, 388, 334, 108, "Red central", "az-vnet", sub="10.10.0.0/22")
    f.icono("az-expressroute", 630, 418, 20)
    f.texto(644, 416, "ExpressRoute", 10)
    f.texto(644, 427, "ErGw1AZ", 9)
    f.texto(644, 439, "Circuito de 100 Mbit/s", 9)
    f.texto(644, 449.6, "EdgeConnex SCL", 9)
    f.icono("az-vpngw", 740, 466, 20)
    f.texto(754, 464, "Puerta VPN", 10)
    f.texto(754, 475, "VpnGw1AZ", 9)
    f.nodo("az-firewall", 832, 440, 26, "Firewall", "Premium")
    f.icono("az-routetable", 832, 403, 14)
    f.linea([(832, 427), (832, 410)], flecha=None)
    f.linea([(832, 396), (832, 380)])
    f.texto(822, 407, "Tabla de rutas", 9, anc="end")
    f.nodo("az-bastion", 892, 440, 26, "Bastion", ["Acceso", "administrativo"])
    f.linea([(892, 427), (892, 380)], disc=True)
    f.grupo_az(948, 388, 212, 108, "Otros ambientes", "az-subscription")
    for i, (n, r) in enumerate([("Preproducción", "10.12.0.0/20"), ("QA", "10.13.0.0/20"),
                                ("Desarrollo", "10.14.0.0/20")]):
        f.texto(958 + i * 70, 432, n, 10)
        f.texto(958 + i * 70, 443, r, 9)
    f.texto(958, 476, "Mismo código de infraestructura", 9)
    f.linea([(940, 458), (948, 458)], disc=True, flecha="ambas")
    # San Bernardo a la red central: ExpressRoute y VPN de respaldo, por ductos distintos
    f.linea([(p1[2], 418), (620, 418)], flecha="ambas")
    f.linea([(p2[2], 462), (730, 462)], disc=True, flecha="ambas")
    f.rotulo(672, 465, "VPN de respaldo")

    # ================================================================ enlaces de la flota
    # LTE: antena del camión, operador móvil, IoT Hub
    XL, XI = 1200, 1262
    to = f.equipo("hw-torre", XL, 400, h=56)
    f.linea([(XL, to[1]), (XL, 100), (1072, 100), (1072, 167)])
    f.rotulo(XL, 150, "LTE")
    f.rotulo(XL, to[3] + 16, ["Operador", "móvil"], tam=10)
    # Iridium: módem, satélite, puerta Iridium, IoT Hub
    sa = f.equipo("oc-satelite", XI, 330, w=40)
    pi = f.equipo("flu-antena-tierra", XI, 230, w=26)
    f.linea([(XI, sa[1]), (XI, pi[3])], disc=True, flecha=None)
    f.linea([(XI, pi[1]), (XI, 92), (1060, 92), (1060, 167)], disc=True)
    f.rotulo(XI, sa[3] + 14, "Satélite", tam=10)
    f.rotulo(XI, pi[3] + 14, ["Puerta", "Iridium"], tam=10)
    f.rotulo(XI, 150, "≤ 340 bytes")

    # ================================================================ contrapartes
    f.grupo(1300, 8, 192, 496, "Contrapartes")
    f.grupo(1308, 30, 176, 96, "Por lotes", rx=6)
    f.nodo("flu-combustible", 1352, 64, 20, ["Estaciones", "de servicio"])
    f.nodo("flu-peaje", 1440, 64, 20, "Peajes")
    f.grupo(1308, 134, 176, 200, "En línea", rx=6)
    f.nodo("flu-empresa", 1352, 172, 20, "Clientes")
    f.nodo("flu-edificio-publico", 1440, 172, 20, "Aduana")
    f.nodo("flu-edificio-publico", 1352, 254, 20, ["Dirección", "del Trabajo"])
    pl = f.nodo("pr-rastreador", 1432, 254, 22, ["Plataformas de", "3 proveedores"],
                ["2 solo consulta,", "1 sin exportación"])
    # los fabricantes autorizan la lectura a bordo; la telemetría no llega por aquí
    f.nodo("flu-fabrica", 1380, 410, 22, "Fabricantes", ["Autorización", "de lectura"])
    f.linea([(1308, 110), (1170, 110)], disc=True)
    f.rotulo(1240, 113, "Archivos") if False else None
    f.linea([(1308, 210), (1170, 210)], flecha="ambas")
    f.linea([(1396, 351), (1396, 496)], flecha=None) if False else None

    # ================================================================ terminales
    f.grupo(596, 516, 344, 356, "Terminales", sub="× 4")
    f.grupo(604, 540, 180, 324, "Gabinete", "pr-gabinete", rx=6)
    ka = eq(f, "hw-karbon", 650, 600, "Karbon 430 A", "Activo", w=54)
    kb = eq(f, "hw-karbon", 650, 690, "Karbon 430 B", "En espera", w=54)
    up = eq(f, "hw-ups-torre", 650, 790, "UPS SRT1000XLI", "83 min con 152 W", h=40)
    rt = eq(f, "hw-rutx50", 740, 600, "RUTX50", ["Fijo ≥ 10 Mbit/s", "y 5G, dos SIM"], w=58)
    ts = eq(f, "hw-tsw202", 740, 712, "TSW202", "Switch PoE", w=66)
    f.ficha(740, 826, ["Opera 24 h", "sin enlace"])
    f.linea([(rt[2], 606), (778, 606), (778, 706), (ts[2], 706)], flecha="ambas")
    f.linea([(ts[0], 712), (700, 712), (700, 600), (ka[2], 600)])
    f.linea([(700, 690), (kb[2], 690)])
    f.linea([(ka[0], 606), (614, 606), (614, 696), (kb[0], 696)], disc=True, flecha="ambas")
    # uplinks del RUTX50 a la puerta VPN de Azure
    f.linea([(736, rt[1]), (736, 476)], flecha="ambas")
    f.linea([(744, rt[1]), (744, 476)], disc=True, flecha="ambas")
    f.rotulo(740, 492, "VPN IPsec")
    # portería y patio del terminal
    f.grupo(804, 540, 128, 140, "Portería", rx=6)
    mt = eq(f, "hw-minew", 840, 592, "Minew G1", None, w=32)
    f.nodo("pr-semirremolque", 902, 590, 26, "Semirremolque", ["Baliza,", "Bluetooth"])
    f.linea([(889, 590), (mt[2], 590)])
    f.nodo("pr-barrera", 840, 646, 20, "Barrera")
    f.grupo(804, 688, 128, 176, "Patio", rx=6)
    it = eq(f, "hw-inyector", 836, 730, "Inyector", "PoE 802.3bt", w=30)
    at = eq(f, "hw-fortiap", 884, 734, "FortiAP", "234G", h=34)
    f.linea([(ts[2], 718), (790, 718), (790, 596), (mt[0], 596)])
    f.rotulo(790, 650, "PoE")
    f.linea([(ts[2], 726), (it[0], 726)])
    f.linea([(it[2], 730), (at[0], 730)])

    # ================================================================ flota
    f.grupo(952, 516, 540, 356, "Flota con equipo audIT", sub="182 tractocamiones")
    # tractocamiones
    f.grupo(960, 540, 84, 66, None, rx=6)
    f.nodo("flu-camion", 1002, 562, 24, "148 propios", "y 34 de terceros")
    # techo: los dos enlaces del camión
    f.grupo(1052, 540, 116, 66, None, rx=6)
    ir = eq(f, "hw-iridium", 1082, 566, "Iridium Edge", None, w=34)
    al = eq(f, "hw-aleta", 1140, 568, "LTE y GNSS", None, w=36)
    f.texto(1060, 552, "Techo", 9) if False else None
    # cadenas desde la nube hasta el techo
    f.linea([(XL, to[3]), (XL, 568), (al[2], 568)], flecha="ambas")
    f.linea([(XI, sa[3]), (XI, 548), (1082, 548), (1082, ir[1])], disc=True, flecha="ambas")
    # equipo a bordo
    GB = (960, 624, 200, 172)
    f.grupo(*GB, "iWave G26I", rx=6, grosor=1.2, sub="en la cabina")
    f.equipo("hw-g26i", 1128, 645, w=40)
    # lo que corre dentro del equipo, con su ícono
    partes = [("dev-linux", 994, 680, "Linux", None),
              ("cmp-elemento-seguro", 1060, 680, ["Elemento", "seguro TA100"], ["Arranque", "seguro y claves"]),
              ("fui-codigo", 1126, 680, ["audIT", "EdgeHub"], None),
              ("flu-ubicacion", 994, 752, ["Motor de", "geocercas"], None),
              ("flu-espera", 1060, 752, ["Búfer de", "288 h"], None),
              ("dev-sqlite", 1126, 752, ["SQLite en", "modo WAL"], None)]
    for ic, cx, cy, n, d in partes:
        f.nodo(ic, cx, cy, 18, n, d)
    f.linea([(1082, 606), (1082, GB[1])], flecha="ambas")
    f.rotulo(1082, 616, "RS232")
    f.linea([(1140, 606), (1140, GB[1])], flecha="ambas")
    f.rotulo(1140, 616, "Coaxial")
    # Wi-Fi del patio del terminal
    f.linea([(at[2], 734), (GB[0], 734)], flecha="ambas")
    f.rotulo(921, 737, "Wi-Fi")
    # periféricos en la cabina
    f.grupo(1168, 624, 144, 240, None, rx=6)
    def periferico(clave, y, w=None, h=None, lineas=()):
        b = f.equipo(clave, 1192, y, w=w, h=h)
        f.texto(1214, y - 2, lineas[0], 10)
        lineas_texto(f, 1214, y + 9, lineas[1:])
        return b
    cn = periferico("hw-can", 664, w=40, lineas=["CANCrocodile", "CAN J1939, sin", "cortar el arnés"])
    f.ficha(1240, 703, ["61 con telemetría", "de fábrica, solo lectura"])
    f.linea([(cn[0], 664), (GB[0] + GB[2], 664)])
    ld = periferico("hw-desfire", 736, h=30, lineas=["Lector DESFire", "GAO MIFARE", "RS485"])
    f.linea([(ld[0], 736), (GB[0] + GB[2], 736)])
    bt = periferico("hw-bateria", 816, w=32, lineas=["Batería", "9 a 32 V"])
    energia(f, [(bt[0], 816), (1164, 816), (1164, 788), (GB[0] + GB[2], 788)])
    # semirremolques con su baliza
    f.grupo(960, 804, 200, 60, None, rx=6)
    f.icono("pr-semirremolque", 984, 834, 28)
    f.texto(1002, 832, "210 semirremolques", 10)
    f.texto(1002, 843, "44 refrigerados", 9)
    bz = f.equipo("hw-baliza", 1134, 828, w=18)
    f.texto(1134, 853, "Baliza", 9, anc="middle")
    f.linea([(1134, bz[1]), (1134, GB[1] + GB[3])])
    f.rotulo(1134, 812, "Bluetooth") if False else None
    # flota de terceros, por las plataformas de sus proveedores
    f.grupo(1320, 540, 164, 66, "Flota de terceros", rx=6)
    f.icono("flu-camion", 1342, 584, 24)
    f.texto(1360, 582, "192 tractocamiones", 10)
    f.texto(1360, 593, "con equipo propio", 9)
    f.linea([(1476, 540), (1476, 254), (1443, 254)])
    # memoria del G26I
    f.grupo(1320, 614, 164, 250, "Memoria del G26I", "pr-memoria", rx=6, sub="eMMC 8 GB")
    celdas = [("Arranque", "16 MB"), ("Sistema A", "1 GB"), ("Sistema B", "1 GB"), ("Búfer 288 h", "38,4 MB"),
              ("Registros", "256 MB"), ("Geocercas y maestros", "16 MB")]
    for i, (n, tam) in enumerate(celdas):
        yy = 640 + i * 30
        f.rect(1350, yy, 126, 26, borde="#404040", grosor=0.75)
        f.texto(1356, yy + 11, n, 10 if len(n) < 14 else 9)
        f.texto(1356, yy + 21.5, tam, 9)
    f.linea([(1350, 683), (1338, 683), (1338, 713), (1350, 713)], flecha="ambas")
    f.texto(1413, 838, "Total 2,4 GB de 8 GB", 10, anc="middle")
    f.texto(1413, 851, "Actualización A y B", 9, anc="middle")
    base = f.guardar()
    f.guardar_escala("-oficio", *OFICIO)
    return base


FIGURAS = [fisica_completa]
