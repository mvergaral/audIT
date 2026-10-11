"""Subdocumento 4, secciones 4.2 y 4.3: figuras físicas (segunda vuelta).

Base: message.txt, contenido.tex del S4 y el Formulario T-11. Cada dato nuevo
tiene su origen anotado en INFORME.md.
"""
from lienzo import Figura, ancho, GRIS_CLARO, BORDE
from fisica_completa import eq

C = "04-arquitectura"


def rack(f, x, y, w, h, titulo, fichas, grosor=1.4):
    """Minirrack o gabinete: marco oscuro con su nombre y un equipo por ficha."""
    f.grupo(x, y, w, h, titulo, rx=2, grosor=grosor)
    for i, s in enumerate(fichas):
        f.ficha(x + w / 2, y + 30 + i * 17, s, w=w - 12)


def bloque(f, x, y, w, h, icono, nombre, rango):
    """Red de Azure como bloque compacto: ícono, nombre y rango en una línea."""
    f.rect(x, y, w, h, relleno="#FFFFFF", borde="#7A7A7A", grosor=0.6, rx=3)
    wn = ancho(nombre, 10)
    wr = ancho(rango, 9)
    total = 18 + wn + 5 + wr
    x0 = x + (w - total) / 2
    f.icono(icono, x0 + 7, y + h / 2, 14)
    f.texto(x0 + 18, y + h / 2 + 3.5, nombre, 10)
    f.texto(x0 + 18 + wn + 5, y + h / 2 + 3.5, rango, 9)


def cadena(f, x, y0, y1, saltos, disc=False):
    """Enlace vertical de y0 (abajo) a y1 (arriba) que pasa por íconos intermedios: la
    línea se corta en cada ícono, el nombre va sobre la línea con fondo blanco y las
    puntas quedan solo en los extremos."""
    tramos = []
    y = y0
    for ic, cy, s in sorted(saltos, key=lambda h: -h[1]):
        tramos.append((y, cy + s / 2))
        y = cy - s / 2
        f.icono(ic, x, cy, s)
    tramos.append((y, y1))
    for i, (a, b) in enumerate(tramos):
        fl = "ambas" if len(tramos) == 1 else ("ini" if i == 0 else ("fin" if i == len(tramos) - 1 else None))
        f.linea([(x, a), (x, b)], disc=disc, flecha=fl)


def fisica_general():
    f = Figura("fisica-general", C, "H")
    # ---------------------------------------------------------------- nube
    f.grupo_az(14, 10, 112, 86, "Brazil South", "az-region")
    f.caja(22, 34, 96, 26, [("Red central", 10, 400), ("10.20.0.0/22", 9, 400)], rx=3, borde="#7A7A7A",
           grosor=0.6, alto_linea=10.5)
    f.caja(22, 64, 96, 26, [("En espera", 10, 400), ("10.21.0.0/20", 9, 400)], rx=3, borde="#7A7A7A",
           grosor=0.6, alto_linea=10.5)
    f.grupo_az(160, 10, 446, 86, "Azure Chile Central", "az-region", sub="Región primaria")
    for i in range(3):
        f.ficha(470 + i * 46, 21, f"Zona {i + 1}")
    bloque(f, 172, 42, 172, 40, "az-vnet", "Red central", "10.10.0.0/22")
    bloque(f, 372, 42, 222, 40, "az-vnet", "Red de producción", "10.11.0.0/20")
    f.linea([(344, 62), (372, 62)], flecha="ambas")
    f.linea([(160, 53), (126, 53)], disc=True)
    f.rotulo(143, 56, "Réplica")
    # Front Door global y usuarios
    f.nodo("az-frontdoor", 640, 30, 26, "Front Door", ["Premium,", "global"])
    f.nodo("rol-usuarios", 700, 30, 26, "Usuarios")
    f.linea([(687, 30), (653, 30)])
    f.linea([(627, 30), (606, 30)])

    # ---------------------------------------------------------------- San Bernardo
    f.grupo(14, 124, 352, 228, "San Bernardo", sub="Sala de sitio")
    f.nodo("rol-operador", 52, 172, 26, "Torre 24x7", ["22 personas", "en turnos"])
    eq(f, "hw-generador", 120, 172, ["Grupo", "electrógeno"], "Himoinsa", w=44)
    f.grupo(22, 256, 128, 58, "Patio", rx=6)
    f.equipo("hw-fortiap", 52, 285, h=20)
    f.texto(52, 305, "FortiAP 234G", 9, anc="middle")
    f.equipo("hw-minew", 120, 286, w=26)
    f.texto(120, 305, "Minew G1", 9, anc="middle")
    rack(f, 158, 146, 104, 76, "Comunicaciones", ["FortiGate 90G ×2", "FortiSwitch 124F ×2"])
    rack(f, 266, 146, 96, 76, "Servidores", ["Dell R360 ×2", "UPS SRT3000 ×2"])
    f.grupo(158, 236, 204, 108, "Capa anticorrupción", "pr-adaptador", rx=6)
    f.nodo("flu-contable", 210, 280, 24, ["Sistema contable", "y de facturación"])
    f.nodo("flu-gestion2013", 312, 280, 24, ["Sistema de gestión", "de transporte 2013"])
    f.linea([(314, 222), (314, 236)], flecha="ambas")
    # autoridad tributaria, colgada del sistema contable
    f.linea([(198, 280), (162, 280), (162, 362), (50, 362), (50, 380)], flecha="ambas")
    f.nodo("flu-edificio-publico", 50, 394, 24, ["Autoridad", "tributaria"])
    # enlaces a Chile Central
    f.linea([(186, 146), (186, 96)], flecha="ambas")
    f.rotulo(186, 106, ["ExpressRoute", "100 Mbit/s"])
    f.linea([(246, 146), (246, 96)], disc=True, flecha="ambas")
    f.rotulo(246, 106, ["VPN de", "respaldo"])

    # ---------------------------------------------------------------- terminales
    f.grupo(480, 124, 120, 196, "Terminales", sub="× 4")
    rack(f, 488, 146, 104, 94, "Gabinete", ["RUTX50", "TSW202", "Karbon 430 ×2", "UPS SRT1000XLI"])
    f.linea([(516, 240), (516, 268)])
    f.linea([(568, 240), (568, 268)])
    f.equipo("hw-fortiap", 516, 277, h=20)
    f.texto(516, 297, "FortiAP", 9, anc="middle")
    f.texto(516, 307.5, "234G", 9, anc="middle")
    f.equipo("hw-minew", 568, 278, w=26)
    f.texto(568, 297, "Minew G1", 9, anc="middle")
    f.linea([(506, 124), (506, 96)], flecha="ambas")
    f.rotulo(506, 106, ["Fijo", "≥ 10 Mbit/s"])
    f.linea([(566, 124), (566, 96)], disc=True, flecha="ambas")
    f.rotulo(566, 106, ["5G de", "respaldo"])

    # ---------------------------------------------------------------- enlaces de la flota
    cadena(f, 392, 368, 96, [("hw-torre", 236, 30)])
    f.rotulo(392, 260, ["Operador", "móvil"], tam=10)
    f.rotulo(392, 106, "LTE")
    cadena(f, 444, 368, 96, [("flu-satelite", 300, 24), ("flu-antena-tierra", 176, 24)], disc=True)
    f.rotulo(444, 324, "Satélite", tam=10)
    f.rotulo(444, 200, ["Puerta", "Iridium"], tam=10)
    f.rotulo(444, 106, "≤ 340 bytes")

    # ---------------------------------------------------------------- flota
    f.grupo(84, 368, 368, 98, "Flota con equipo audIT")
    f.nodo("flu-camion", 154, 410, 28, "182 tractocamiones", "148 propios y 34 de terceros")
    eq(f, "hw-g26i", 250, 410, "iWave G26I", w=40)
    eq(f, "hw-baliza", 336, 410, "Baliza", "EYE Sensor", w=22)
    f.nodo("pr-semirremolque", 412, 410, 28, ["210", "semirremolques"], "44 refrigerados")
    f.linea([(325, 410), (270, 410)])
    f.rotulo(293, 413, "Bluetooth")
    f.grupo(480, 334, 120, 132, "Flota de terceros")
    f.nodo("flu-camion", 540, 390, 28, "192", ["tractocamiones", "con equipo propio"])

    # ---------------------------------------------------------------- contrapartes
    f.grupo(622, 86, 98, 380, "Contrapartes")
    f.grupo(628, 106, 86, 112, "Por lotes", rx=6)
    f.nodo("flu-combustible", 671, 136, 18, ["Estaciones", "de servicio"])
    f.nodo("flu-peaje", 671, 186, 18, "Peajes")
    f.grupo(628, 224, 86, 236, "En línea", rx=6)
    f.nodo("flu-empresa", 671, 240, 18, "Clientes")
    f.nodo("flu-edificio-publico", 671, 272, 18, "Aduana")
    f.nodo("flu-edificio-publico", 671, 302, 18, ["Dirección", "del Trabajo"])
    # la telemetría de fábrica se lee a bordo con el CANCrocodile (S4 406-408): el fabricante solo autoriza
    f.nodo("flu-fabrica", 671, 345, 18, "Fabricantes", ["Autorizan", "la lectura"])
    # tres plataformas: dos de solo consulta y una que no exporta (Caso, numeral 16.1, p.34, y S4 679)
    f.nodo("pr-rastreador", 671, 404, 18, ["Plataformas de", "3 proveedores"], ["2 de consulta,", "1 sin exportar"])
    f.linea([(600, 404), (660, 404)])
    f.linea([(628, 150), (618, 150), (618, 70), (606, 70)], disc=True)
    f.linea([(628, 340), (614, 340), (614, 84), (606, 84)], flecha="ambas")
    return f.guardar()


def subred(f, x, y, w, h, nombre, rango):
    """Subred de Azure: ícono y nombre arriba a la izquierda, rango debajo y el grupo de
    seguridad de red como ícono chico en la esquina."""
    f.grupo_az(x, y, w, h, nombre, "az-subnet", subred=True)
    f.texto(x + 25, y + 26.5, rango, 9)
    f.icono("az-nsg", x + w - 10, y + 10, 11)


def region_primaria():
    f = Figura("region-primaria", C, "H")
    # usuarios y Front Door, global, fuera de la región
    f.nodo("rol-usuarios", 150, 24, 24, "Usuarios")
    f.linea([(138, 24), (52, 24), (52, 149)])
    f.nodo("az-frontdoor", 52, 162, 26, "Front Door", ["Premium,", "global"])
    f.linea([(65, 162), (256, 162)])
    # camiones por IoT Hub
    f.nodo("flu-camion", 652, 24, 26, "Camiones", "182 equipos audIT")
    f.linea([(638, 20), (566, 20), (566, 149)], flecha="ambas")
    f.rotulo(600, 23, "LTE")
    f.linea([(638, 30), (578, 30), (578, 149)], disc=True, flecha="ambas")
    f.rotulo(608, 33, "Iridium")

    f.grupo_az(204, 66, 482, 404, "Azure Chile Central", "az-region", sub="3 zonas de disponibilidad")
    # red de producción
    f.grupo_az(214, 90, 462, 254, "Red de producción", "az-vnet", sub="10.11.0.0/20")
    subred(f, 224, 114, 90, 108, "Borde", "10.11.1.0/24")
    f.nodo("az-apim", 269, 162, 26, "API Management", "Premium")
    subred(f, 322, 114, 132, 108, "Aplicación", "10.11.4.0/22")
    f.nodo("az-aks", 388, 162, 26, "AKS", "Nodos en 3 zonas")
    for i in range(3):
        f.ficha(346 + i * 42, 210, f"Zona {i + 1}")
    subred(f, 462, 114, 206, 108, "Integración", "10.11.2.0/24")
    f.nodo("az-eventhubs", 502, 162, 26, "Event Hubs", "Premium, Kafka")
    f.nodo("az-iothub", 572, 162, 26, "IoT Hub", "S1 × 2")
    f.ficha(572, 210, "Certificado mutuo")
    f.nodo("az-dps", 636, 162, 26, "Provisioning", "DPS")
    # flujos internos
    f.linea([(282, 158), (375, 158)])
    f.linea([(489, 158), (401, 158)])
    f.linea([(559, 158), (515, 158)])
    f.linea([(623, 158), (585, 158)], disc=True)
    subred(f, 224, 230, 90, 108, "Gestión", "10.11.8.0/24")
    f.nodo("az-monitor", 262, 284, 26, ["Monitor y", "Log Analytics"])
    subred(f, 322, 230, 346, 108, "Datos", "10.11.3.0/24")
    datos = [("az-postgres", "PostgreSQL", "Transaccional", 372), ("az-postgres", "PostgreSQL", "Series, TimescaleDB", 460),
             ("az-storage", "Blob inmutable", "ZRS", 552), ("az-keyvault", "Key Vault", "Premium", 630)]
    for ic, n, d, x in datos:
        f.nodo(ic, x, 284, 26, n, d)
        f.icono("az-privateendpoint", x + 16, 273, 11)
    f.ficha(372, 332, "Primaria y espera")
    # AKS escribe en los datos por un bus
    for x in [d[3] for d in datos]:
        f.linea([(401, 168), (458, 168), (458, 262), (x, 262), (x, 271)])
    # todo se registra en Monitor
    for x in (300, 388, 565):
        f.linea([(x, 222), (x, 226), (318, 226), (318, 284), (275, 284)], disc=True)
    f.linea([(322, 284), (275, 284)], disc=True)
    # réplica a Brazil South
    f.linea([(668, 300), (727, 300)], disc=True)
    f.rotulo(698, 303, ["Réplica a", "Brazil South"])

    # red central
    f.grupo_az(214, 350, 300, 116, "Red central", "az-vnet", sub="10.10.0.0/22")
    f.nodo("az-expressroute", 248, 380, 20, "ExpressRoute", "ErGw1AZ")
    f.nodo("az-vpngw", 248, 432, 20, "Puerta VPN", "VpnGw1AZ")
    f.nodo("az-firewall", 382, 414, 26, "Firewall", "Premium")
    cadena(f, 382, 401, 344, [("az-routetable", 366, 16)])
    f.rotulo(382, 387, "Tabla de rutas")
    f.nodo("az-bastion", 466, 414, 26, "Bastion", ["Acceso", "administrativo"])
    f.linea([(466, 401), (466, 344)], disc=True)
    f.rotulo(466, 368, "Subredes")
    # otros ambientes
    f.grupo_az(524, 350, 152, 116, "Otros ambientes", "az-subscription")
    for i, (n, r) in enumerate([("Preproducción", "10.12.0.0/20"), ("QA", "10.13.0.0/20"),
                                ("Desarrollo", "10.14.0.0/20")]):
        f.texto(534, 386 + i * 24, n, 10)
        f.texto(534, 397 + i * 24, r, 9)
    f.linea([(514, 440), (524, 440)], disc=True, flecha="ambas")

    # entradas desde San Bernardo y los terminales
    eq(f, "hw-fortigate", 46, 380, "San Bernardo", "FortiGate 90G", w=52)
    f.linea([(72, 380), (238, 380)], flecha="ambas")
    f.rotulo(150, 376, ["ExpressRoute 100 Mbit/s", "EdgeConnex SCL"])
    f.linea([(72, 384), (118, 384), (118, 428), (238, 428)], disc=True, flecha="ambas")
    f.rotulo(160, 431, "VPN de respaldo")
    eq(f, "hw-rutx50", 46, 436, "Terminales", "RUTX50", w=30)
    f.linea([(61, 440), (238, 440)], flecha="ambas")
    f.rotulo(160, 441, "VPN")
    return f.guardar()


# software y funciones del iWave G26I: (ícono, x, y, nombre, dato)
G26I_PARTES = [("dev-linux", 178, 142, "Linux", None),
               ("cmp-elemento-seguro", 268, 142, ["Elemento seguro", "TA100"], ["Arranque seguro", "y claves"]),
               ("fui-codigo", 178, 212, "audIT EdgeHub", None),
               ("flu-ubicacion", 268, 212, ["Motor de", "geocercas"], None),
               ("flu-espera", 178, 260, "Búfer de 288 h", None),
               ("dev-sqlite", 268, 260, ["SQLite en", "modo WAL"], None)]


def equipo_a_bordo():
    f = Figura("equipo-a-bordo", C, "V", alto=482)
    # techo con las dos antenas
    f.grupo(118, 8, 196, 70, "Techo", rx=6)
    eq(f, "hw-iridium", 168, 40, "Iridium Edge", w=34)
    eq(f, "hw-aleta", 262, 41, "Antena LTE y GNSS", w=38)
    # afuera: satélite, red celular, baliza y patio
    f.nodo("flu-satelite", 380, 26, 22, "Satélite")
    f.linea([(168, 29), (168, 14), (350, 14), (350, 26), (369, 26)], disc=True, flecha="ambas")
    f.rotulo(258, 17, "≤ 340 bytes")
    eq(f, "hw-torre", 380, 104, "Red celular", h=30)
    f.linea([(281, 40), (330, 40), (330, 104), (369, 104)], flecha="ambas")
    f.rotulo(330, 74, "LTE")
    eq(f, "hw-baliza", 380, 196, "Baliza", "EYE Sensor", w=22)
    eq(f, "hw-fortiap", 380, 276, ["Patio del", "terminal"], "FortiAP 234G", h=26)

    # cabina
    f.grupo(8, 88, 318, 248, "Cabina")
    f.grupo(132, 108, 182, 194, "iWave G26I", "pr-g26i", rx=6, grosor=1.2)
    # lo que corre dentro del equipo, con su ícono
    for ic, cx, cy, n, d in G26I_PARTES:
        f.nodo(ic, cx, cy, 20, n, d)
    # antenas al equipo
    f.linea([(168, 78), (168, 108)], flecha="ambas")
    f.rotulo(168, 98, "RS232")
    f.linea([(262, 78), (262, 108)], flecha="ambas")
    f.rotulo(262, 98, "Coaxial")
    # arnés CAN del camión con el lector pinzado, sin cortarlo
    f.linea([(46, 112), (46, 206)], flecha=None, grosor=3.2, color="#9B9B9B", saltos=False)
    f.linea([(53, 112), (53, 206)], flecha=None, grosor=3.2, color="#9B9B9B", saltos=False)
    f.equipo("hw-can", 50, 140, w=40, revisar=False)
    f.rotulo(50, 167, "CANCrocodile", tam=10)
    f.rotulo(50, 194, "Arnés CAN")
    f.linea([(70, 140), (132, 140)])
    f.rotulo(101, 143, "CAN J1939")
    eq(f, "hw-desfire", 70, 232, "Lector DESFire", "GAO MIFARE", h=26)
    f.linea([(82, 228), (132, 228)])
    f.rotulo(107, 231, "RS485")
    eq(f, "hw-bateria", 70, 296, "Batería del camión", "9 a 32 V", w=30)
    f.linea([(85, 296), (132, 296)])
    f.rotulo(108, 299, "Energía")
    # periféricos externos
    f.linea([(369, 196), (314, 196)])
    f.rotulo(338, 199, "Bluetooth")
    f.linea([(369, 270), (314, 270)])
    f.rotulo(338, 273, "Wi-Fi")

    # memoria
    f.grupo(8, 352, 406, 122, "Memoria del G26I", "pr-memoria", sub="eMMC de 8 GB")
    celdas = [("Arranque", "16 MB"), ("Sistema A", "1 GB"), ("Sistema B", "1 GB"),
              ("Búfer 288 h", "38,4 MB"), ("Registros", "256 MB"), (["Geocercas", "y maestros"], "16 MB")]
    x0, w, y0, h = 20, 382 / 6, 398, 46
    for i, (n, tam) in enumerate(celdas):
        x = x0 + i * w
        f.rect(x, y0, w, h, borde="#404040", grosor=0.75)
        nl = n if isinstance(n, list) else [n]
        for j, l in enumerate(nl):
            f.texto(x + w / 2, y0 + 15 + j * 11.5, l, 10, anc="middle")
        f.texto(x + w / 2, y0 + h - 6, tam, 9, anc="middle")
    xa, xb = x0 + 1.5 * w, x0 + 2.5 * w
    f.linea([(xa, y0), (xa, y0 - 12), (xb, y0 - 12), (xb, y0)], flecha="ambas")
    f.rotulo((xa + xb) / 2, y0 - 9, "Actualización")
    f.linea([(x0, y0 + h + 6), (x0, y0 + h + 10), (x0 + 382, y0 + h + 10), (x0 + 382, y0 + h + 6)], flecha=None)
    f.rotulo(211, y0 + h + 14, "Total 2,4 GB de 8 GB", tam=10)
    return f.guardar()


# color del borde de cada ambiente, el mismo en ambientes y ambientes-promocion
# (paleta de Okabe e Ito, distinguible con daltonismo; el rojo queda reservado para el PERT)
COLOR_AMBIENTE = {"Desarrollo": "#0072B2", "QA": "#009E73", "Preproducción": "#E69F00",
                  "Producción": "#8E44AD", "Recuperación": "#5D6D7E"}
BORDE_AMBIENTE = 1.6

AMBIENTES = [("Desarrollo", "10.14.0.0/20", ["Chile Central", "Niveles menores y menos nodos"]),
             ("QA", "10.13.0.0/20", ["Chile Central", "Niveles menores y menos nodos"]),
             ("Preproducción", "10.12.0.0/20", ["Producción a escala reducida", "Pruebas de carga 1,5 × peak"]),
             ("Producción", "10.11.0.0/20", ["3 zonas de Chile Central"]),
             ("Recuperación", "10.21.0.0/20", ["Brazil South, en espera", "Idéntica a producción"])]


def ambientes():
    """Vista general (quinta vuelta): cómo nacen los cinco ambientes y en qué se diferencian.
    S4 815-816, 829-832, 846-850 y 871-881."""
    f = Figura("ambientes", C, "V", alto=430)
    f.ficha(118, 16, "Cada ambiente en su propia suscripción", anc="start")
    f.ficha(118, 42, ["Etiquetas de ambiente, centro de costo y", "responsable, con presupuesto y alertas"], anc="start")
    x, w, h = 118, 200, 58
    ys = [64, 130, 196, 262, 358]
    for (n, rango, fichas), y in zip(AMBIENTES, ys):
        f.grupo(x, y, w, h, n, "az-subscription", rx=3, borde=COLOR_AMBIENTE[n], grosor=BORDE_AMBIENTE,
                discontinuo=(n == "Recuperación"), sub=rango)
        for j, s in enumerate(fichas):
            f.ficha(x + 10, y + 31 + j * 17, s, anc="start")
    # el código de infraestructura crea los cinco
    f.nodo("dev-git", 46, 216, 26, ["Repositorio", "del mandante"], ["Código de", "infraestructura"])
    f.ficha(46, 300, ["Sin creación", "por consola"])
    cys = [y + h / 2 for y in ys]
    f.linea([(59, 216), (88, 216)], flecha=None)
    f.linea([(88, cys[0]), (88, cys[-1])], flecha=None)
    for cy in cys:
        f.linea([(88, cy), (x, cy)])
    f.rotulo(88, 343, "Despliega")
    # la recuperación va aparte: no recibe versiones, recibe la réplica de producción
    f.texto(x, 350, "Aparte: no recibe versiones", 9)
    f.linea([(290, ys[3] + h), (290, ys[4])], disc=True)
    f.rotulo(290, 342, "Réplica")
    # registros de todos los ambientes
    f.grupo(334, 64, 80, 352, None, rx=6)
    f.nodo("az-monitor", 374, 170, 26, ["Monitor y", "Log Analytics"], ["Registros de", "todos los", "ambientes"])
    f.ficha(374, 268, ["12 meses", "en línea"])
    f.ficha(374, 300, ["24 en", "archivo"])
    for cy in cys:
        f.linea([(x + w, cy), (334, cy)], disc=True)
    return f.guardar()


def ambientes_promocion():
    """Paso a paso (quinta vuelta): qué le pasa a una versión, de izquierda a derecha.
    S4 871-893; pipeline del S6 de la dupla 3, tabla 6.3 (líneas 132-139)."""
    f = Figura("ambientes-promocion", C, "H")
    YP, HP, YF = 132, 208, 312
    pasos = {"cod": (8, 76), "des": (134, 92), "qa": (276, 92), "pre": (418, 92), "prod": (560, 162)}
    cx = {k: x + w / 2 for k, (x, w) in pasos.items()}
    nombre = {"des": "Desarrollo", "qa": "QA", "pre": "Preproducción", "prod": "Producción"}
    for k, (x, w) in pasos.items():
        if k in nombre:
            f.rect(x, YP, w, HP, rx=6, borde=COLOR_AMBIENTE[nombre[k]], grosor=BORDE_AMBIENTE)
        else:
            f.rect(x, YP, w, HP, rx=6)

    def titulo(k, s, rango=None):
        f.texto(cx[k], YP + 16, s, 10, 600, "middle")
        if rango:
            f.texto(cx[k], YP + 28, rango, 9, anc="middle")

    # 1. código
    titulo("cod", "1. Código")
    f.nodo("dev-git", cx["cod"], 186, 24, ["Repositorio", "del mandante"], ["Aplicación e", "infraestructura"])
    # 2 a 4: desarrollo, QA y preproducción, con las fichas de la vista general
    for k, (n, rango, fichas), num in zip(["des", "qa"], AMBIENTES[:2], (2, 3)):
        titulo(k, f"{num}. {n}", rango)
        f.nodo("az-subscription", cx[k], 186, 22, "Suscripción", "propia")
        f.ficha(cx[k], 240, fichas[0])
        f.ficha(cx[k], 268, ["Niveles menores", "y menos nodos"])
    titulo("pre", "4. Preproducción", "10.12.0.0/20")
    f.nodo("az-subscription", cx["pre"], 186, 22, "Suscripción", "propia")
    f.ficha(cx["pre"], 244, ["Producción a", "escala reducida"])
    f.nodo("pr-medidor", cx["pre"], 282, 20, "Prueba de carga", "1,5 × peak")
    # 5. producción
    titulo("prod", "5. Producción", "10.11.0.0/20")
    c1, c2 = cx["prod"] - 41, cx["prod"] + 41
    f.nodo("az-aks", c1, 182, 22, "AKS", "Nodos en 3 zonas")
    f.nodo("az-postgres", c2, 182, 22, "PostgreSQL", ["Copia en espera", "en otra zona"])
    f.nodo("az-storage", c1, 244, 22, "Almacenamiento", ["Redundancia", "de zona"])
    f.nodo("az-apim", c2, 244, 22, "API Management", ["Unidades en", "las 3 zonas"])
    f.ficha(cx["prod"], 308, "Respaldo diario en Chile Central")
    f.ficha(cx["prod"], 328, "Restauración de prueba mensual")
    # flechas entre pasos
    orden = ["cod", "des", "qa", "pre", "prod"]
    for a, b in zip(orden, orden[1:]):
        xa = pasos[a][0] + pasos[a][1]
        f.linea([(xa, YF), (pasos[b][0], YF)])
        f.rotulo((xa + pasos[b][0]) / 2, YF + 3, "Despliega" if a == "cod" else "Promoción")

    # pipeline de la dupla 3: seis etapas antes de producción, sin asignarlas a un ambiente
    xb0, xb1 = pasos["des"][0], pasos["pre"][0] + pasos["pre"][1]
    f.grupo(xb0, 24, xb1 - xb0, 96, "Pipeline DevSecOps", rx=6)
    f.ficha(xb1 - 8, 39, "Antes de producción", anc="end")
    etapas = [("Pruebas", "Cobertura ≥ 80 %"), ("Análisis estático", "SonarQube"), ("Contenedores", "Trivy"),
              ("SBOM y firma", "Cosign"), ("Infraestructura", "tfsec y checkov"), ("Análisis dinámico", "OWASP ZAP")]
    cw, cg = 106, 20
    xs = [xb0 + 9 + i * (cw + cg) for i in range(3)]
    # dos filas que se leen de izquierda a derecha: 1 a 3 arriba y 4 a 6 abajo, numeradas
    celdas = [(xs[0], 50), (xs[1], 50), (xs[2], 50), (xs[0], 88), (xs[1], 88), (xs[2], 88)]
    for i, ((n, herr), (x, y)) in enumerate(zip(etapas, celdas), 1):
        f.rect(x, y, cw, 26, rx=4, borde="#7A7A7A", grosor=0.6)
        f.texto(x + cw / 2, y + 11, f"{i}. {n}", 10, anc="middle")
        f.texto(x + cw / 2, y + 22, herr, 9, anc="middle")
    for (xa, ya), (xb, yb) in zip(celdas, celdas[1:]):
        if ya == yb:
            f.linea([(xa + cw, ya + 13), (xb, yb + 13)])
        else:
            # de la etapa 3 a la 4: baja y vuelve al inicio de la segunda fila
            f.linea([(xa + cw / 2, ya + 26), (xa + cw / 2, 82), (xb - 5, 82), (xb - 5, yb + 13), (xb, yb + 13)])
    f.linea([(cx["cod"], YP), (cx["cod"], 63), (xb0, 63)])
    # la etapa 6 desemboca en la promoción de preproducción a producción: es la puerta antes de producción
    xg = (pasos["pre"][0] + pasos["pre"][1] + pasos["prod"][0]) / 2
    f.linea([(xs[2] + cw, 101), (xg, 101), (xg, YF - 1)])

    # recuperación, aparte: no recibe versiones
    YR = 372
    f.grupo(8, YR, 714, 68, "Recuperación", borde=COLOR_AMBIENTE["Recuperación"], grosor=BORDE_AMBIENTE,
            discontinuo=True, sub="No recibe versiones: recibe la réplica de producción y se levanta desde el mismo código")
    f.icono("az-region", 30, YR + 42, 22)
    f.texto(48, YR + 40, "Brazil South, en espera", 10)
    f.texto(48, YR + 51, "10.21.0.0/20", 9)
    f.ficha(250, YR + 42, "Idéntica a producción")
    f.linea([(cx["cod"], YP + HP), (cx["cod"], YR)], disc=True)
    f.linea([(cx["prod"], YP + HP), (cx["prod"], YR)], disc=True)
    f.texto(cx["cod"] + 8, YR - 9, "Mismo código", 9)
    f.texto(cx["prod"] - 8, YR - 9, "Réplica de producción", 9, anc="end")
    return f.guardar()


def reconexion():
    """Reconexión de 300 camiones tras 72 h (quinta vuelta): qué es un mensaje, de dónde salen
    los números y los cinco tramos, con mensajes y fotos en carriles separados.
    S4 962-999; cálculo en D4/investigacion/dimensionamiento.py."""
    f = Figura("reconexion", C, "V", alto=567)
    X = 196                                   # carril de los mensajes
    # ------------------------------------------------ 1. un camión, abierto
    f.marcador(14, 22, 1)
    f.nodo("flu-camion", 52, 34, 24, "Un camión", "72 h sin cobertura")
    partes = [("Posiciones", None, "4.104 registros", "263 KB", 262656, "#C8C8C8"),
              ("Telemetría", "del motor", "1.800 registros", "288 KB", 288000, "#DCDCDC"),
              ("Eventos y", "documentos", "Cerca de 50", "232 KB", 232448, "#EFEFEF")]
    total = sum(p[4] for p in partes)
    x, x0b, wb = 100, 100, 200
    for n1, n2, reg, kb, by, gris in partes:
        w = wb * by / total
        f.rect(x, 26, w, 18, relleno=gris, borde="#FFFFFF", grosor=1)
        lineas = [(n1, 10)] + ([(n2, 10)] if n2 else []) + [(reg, 9), (kb, 9)]
        y = 57
        for s, tam in lineas:
            f.texto(x + w / 2, y, s, tam, anc="middle")
            y += 12 if tam == 10 else 10.5
        x += w
    f.rect(x0b, 26, wb, 18, relleno="none", borde="#404040", grosor=0.75)
    f.texto(310, 33, "0,78 MB", 10)
    f.texto(310, 44, "Cerca de 6.000", 9)
    f.texto(310, 54.5, "registros", 9)
    f.linea([(344, 60), (344, 75)])
    f.ficha(364, 88, ["192 mensajes de 4 KB", "(4 KB = 4.096 bytes)"])
    # las fotos, aparte, en un paquete
    for i in range(8):
        f.icono("flu-foto", 106 + i * 14, 118, 12)
    f.texto(216, 115, "8 fotos,", 9)
    f.texto(216, 125.5, "2,46 MB", 9)
    f.linea([(256, 118), (281, 118)])
    f.nodo("flu-repuestos", 292, 118, 18, None, "En 1 paquete")
    # por 300 camiones que salen a la vez de una sombra
    for i in range(3):
        f.icono("flu-camion", 28 + i * 24, 166, 20)
    f.ficha(52, 190, "300 camiones")
    f.texto(96, 163, "× 300 camiones que", 9)
    f.texto(96, 173.5, "salen a la vez de", 9)
    f.texto(96, 184, "una sombra", 9)
    f.linea([(364, 100.3), (364, 172)])
    f.rotulo(364, 139, "× 300")
    f.linea([(292, 141), (292, 168)])
    f.rotulo(292, 157, "× 300")
    f.ficha(364, 180, "57.600 mensajes")
    f.ficha(292, 182, ["300 paquetes", "de fotos"])
    # ------------------------------------------------ 2. red celular: las conexiones
    f.linea([(364, 187), (364, 207), (X + 6, 207), (X + 6, 215)])
    f.linea([(292, 194.3), (292, 201), (X - 6, 201), (X - 6, 215)])
    f.marcador(14, 230, 2)
    f.equipo("hw-torre", X, 230, h=30)
    f.texto(X - 18, 234, "Red celular", 10, anc="end")
    f.icono("flu-espera", 262, 226, 16)
    f.icono("flu-reintento", 282, 226, 16)
    f.texto(272, 245, "Espera aleatoria", 9, anc="middle")
    f.texto(272, 255.5, "y reintento", 9, anc="middle")
    f.ficha(368, 232, ["300 conexiones a 100", "por segundo: 3 s"])
    # ------------------------------------------------ 3. IoT Hub: los envíos y la carga de fotos
    f.linea([(X, 245), (X, 273)])
    f.marcador(14, 286, 3)
    f.icono("az-iothub", X, 286, 26)
    f.texto(X - 18, 284, "IoT Hub", 10, anc="end")
    f.texto(X - 18, 295, "S1 × 2", 9, anc="end")
    f.ficha(70, 332, ["800.000 mensajes al día", "con 2 unidades: 330.000", "de la operación normal y",
                      "57.600 de esta reconexión"])
    # carril de las fotos: carga de archivos al almacenamiento inmutable
    f.linea([(X + 13, 286), (367, 286)])
    f.rotulo(290, 289, "Carga de archivos")
    f.nodo("az-storage", 380, 286, 26, "Blob inmutable", "Evidencia")
    f.ficha(364, 344, ["Inicio de 300 cargas:", "1,67 por segundo por", "unidad, × 2: 1,5 min"])
    # carril de los mensajes
    f.linea([(X, 299), (X, 371)])
    f.ficha(258, 330, ["Admisión estimada:", "57.600 mensajes a 100", "por segundo, 9,6 min"])
    # ------------------------------------------------ 4. Event Hubs: la cola y su indicador
    f.marcador(14, 384, 4)
    f.icono("az-eventhubs", X, 384, 26)
    f.texto(X - 18, 388, "Event Hubs", 10, anc="end")
    f.rect(214, 374, 86, 20, relleno="#FFFFFF", borde="#404040", grosor=0.75, rx=3)
    for i in range(6):
        f.rect(219 + i * 13.5, 378, 8, 12, relleno=GRIS_CLARO, borde="#9B9B9B", grosor=0.5, rx=1.5)
    f.linea([(X + 13, 384), (214, 384)], flecha=None)
    f.texto(257, 406, "Cola retenida", 9, anc="middle")
    f.grupo(316, 370, 98, 76, "Indicador", rx=6)
    f.icono("az-monitor", 330, 398, 16)
    f.texto(342, 396, "Profundidad", 9)
    f.texto(342, 406.5, "de la cola", 9)
    f.ficha(365, 428, ["Alerta sobre 10", "min de retraso"])
    f.linea([(300, 384), (316, 384)], disc=True)
    # ------------------------------------------------ 5. consumidores en AKS, por lotes
    f.linea([(X, 397), (X, 435)])
    f.marcador(14, 448, 5)
    f.nodo("az-aks", X, 448, 26, ["Consumidores", "por lotes"])
    f.ficha(110, 448, "Escalado automático")
    f.linea([(X + 13, 448), (287, 448)])
    f.nodo("az-postgres", 300, 448, 26, ["PostgreSQL", "de series"])

    # ------------------------------------------------ regla de tiempo proporcional, de 0 a 20 minutos
    x0, x1, yb = 40, 370, 546

    def xt(minutos):
        return x0 + (x1 - x0) * minutos / 20
    filas = [(0.05, "Conexiones, 3 s", 512), (1.5, "Inicio de cargas de fotos, 1,5 min", 523),
             (9.6, "Admisión de mensajes, 9,6 min", 534)]
    f.texto(x0, 502, "Admisión estimada. Fin del proceso: CP-PERF-02", 9)
    for m, s, y in filas:
        f.rect(x0, y - 4, xt(m) - x0, 8, relleno="#C8C8C8", borde="#404040", grosor=0.5)
        f.texto(xt(m) + 5, y + 3.2, s, 9)
    f.linea([(x0, yb), (x1, yb)], flecha=None, saltos=False)
    for m in (0, 5, 10, 15, 20):
        f.linea([(xt(m), yb - 3), (xt(m), yb + 3)], flecha=None, saltos=False)
        f.texto(xt(m), yb + 13, str(m), 9, anc="middle")
    f.texto(x1 + 8, yb + 13, "minutos", 9)
    f.linea([(x1, 497), (x1, yb)], flecha=None, grosor=1.6, saltos=False)
    f.texto(x1 - 5, 502, "20 min, límite RT-03.13", 9, anc="end")
    return f.guardar()


def sala_san_bernardo():
    import math
    f = Figura("sala-san-bernardo", C, "V", alto=420)
    m = 46                     # puntos por metro: 6,5 m = 299 pt
    X, Y, W, H = 40, 60, 6.5 * m, 4 * m
    AGUA = "#2C6FD1"

    def P(xm, ym):
        return X + xm * m, Y + ym * m

    def cono(x0, y0, ang, largo=1.3 * m, abre=28):
        pts = [(x0, y0)]
        for a in (ang - abre, ang + abre):
            pts.append((x0 + largo * math.cos(math.radians(a)), y0 + largo * math.sin(math.radians(a))))
        f.crudo('<path d="M{:.2f},{:.2f} L{:.2f},{:.2f} L{:.2f},{:.2f} Z" fill="#ECECEC"/>'.format(
            *pts[0], *pts[1], *pts[2]), capa="fondo")

    # conos de las cuatro cámaras (debajo de todo)
    camaras = [(0.15, 0.15, 45), (6.35, 0.15, 135), (6.35, 3.85, 225), (0.15, 2.55, 45)]
    for xm, ym, ang in camaras:
        cono(*P(xm, ym), ang)
    # muros
    f.rect(X, Y, W, H, relleno="none", borde="#2B2B2B", grosor=4)
    # esclusa: muro interior y dos puertas con su giro
    f.crudo('<path d="M{:.2f},{:.2f} H{:.2f} V{:.2f}" fill="none" stroke="#2B2B2B" stroke-width="3"/>'.format(
        *P(0, 2.4), P(1.4, 0)[0], P(0, 4)[1]), capa="fondo")
    for ym, sentido, barrido in ((4.0, 1, 0), (2.4, -1, 1)):
        xh, yh = P(0.3, ym)
        xa, _ = P(1.1, ym)
        f.rect(xh, yh - 2.5, 0.8 * m, 5, relleno="#FFFFFF", borde=None)
        f.crudo(f'<path d="M{xh:.2f},{yh:.2f} V{yh + sentido * 0.8 * m:.2f} A{0.8 * m},{0.8 * m} 0 0 {barrido} {xa:.2f},{yh:.2f}" '
                f'fill="none" stroke="#7A7A7A" stroke-width="0.75"/>', capa="fondo")
    f.texto(*P(0.72, 3.62), "Esclusa", 10, anc="middle")
    f.equipo("hw-facial", *P(1.3, 4.36), h=17)
    f.texto(*P(1.3, 4.72), "Lector facial", 9, anc="middle")
    f.equipo("hw-facial", *P(1.15, 2.72), h=17)
    f.texto(*P(1.04, 3.08), "Lector", 9, anc="middle")
    f.icono("flu-extintor", *P(0.22, 3.25), 11)                 # extintor portátil de la esclusa
    f.texto(*P(0.36, 3.33), "CO₂", 9)
    # entrada
    f.linea([P(0.7, 5.0), P(0.7, 4.08)])
    f.rotulo(*P(0.7, 4.98), "Entrada")
    # cilindro de FK-5-1-12 junto a la esclusa
    f.icono("flu-extintor", *P(1.68, 3.12), 17)
    f.texto(*P(1.9, 3.06), "Cilindro", 9)
    f.texto(*P(1.9, 3.29), "FK-5-1-12", 9)
    # climas en muros opuestos, con el cable detector de agua por el piso bajo cada uno
    f.rect(*P(0, 0.35), 0.35 * m, 1.0 * m, relleno="#FFFFFF", borde="#404040", grosor=1.2)
    f.texto(*P(0.55, 0.62), "Clima A", 10)
    f.rect(*P(6.15, 2.0), 0.35 * m, 1.0 * m, relleno="#FFFFFF", borde="#404040", grosor=1.2)
    f.texto(*P(5.95, 2.3), "Clima B", 10, anc="end")
    f.linea([P(0.0, 0.27), P(0.45, 0.27), P(0.45, 1.43), P(0.0, 1.43)], disc=True, flecha=None, color=AGUA,
            grosor=1.4, saltos=False)
    f.linea([P(6.5, 1.92), P(6.05, 1.92), P(6.05, 3.08), P(6.5, 3.08)], disc=True, flecha=None, color=AGUA,
            grosor=1.4, saltos=False)
    f.icono("flu-agua", *P(0.62, 1.12), 10)
    f.texto(*P(0.75, 1.0), "Cable detector", 9)
    f.texto(*P(0.75, 1.23), "de agua", 9)
    f.icono("flu-agua", *P(5.88, 2.78), 10)
    f.texto(*P(5.75, 2.72), "Cable detector", 9, anc="end")
    f.texto(*P(5.75, 2.95), "de agua", 9, anc="end")
    # racks a escala, con el frente hacia el pasillo
    for x0, nombre in ((2.0, "Servidores"), (3.6, "Comunicaciones")):
        f.rect(*P(x0, 0.35), 0.6 * m, 1.0 * m, relleno="#FFFFFF", borde="#404040", grosor=1.2)
        xa, ya = P(x0, 1.35)
        f.crudo(f'<path d="M{xa:.2f},{ya:.2f} h{0.6 * m:.2f}" stroke="#2B2B2B" stroke-width="3"/>')
        f.equipo("hw-rack", *P(x0 + 0.3, 0.76), h=31)
        f.texto(*P(x0 + 0.3, 1.29), "24 U", 9, anc="middle")
        f.texto(*P(x0 + 0.3, 0.27), nombre, 10, anc="middle")
    f.rect(*P(1.8, 1.5), 2.6 * m, 0.7 * m, relleno="none", borde="#9B9B9B", grosor=0.6, disc=True, rx=3)
    f.texto(*P(3.1, 1.92), "Pasillo de trabajo", 9, anc="middle")
    # VESDA: detector en el muro y tubería por el cielo con sus puntos de muestreo
    f.equipo("hw-vesda", *P(6.24, 1.15), w=19)
    f.linea([P(6.02, 1.15), P(5.15, 1.15), P(5.15, 2.45), P(1.6, 2.45)], disc=True, flecha=None, saltos=False)
    for xm in (2.0, 3.0, 4.0, 5.0):
        x, y = P(xm, 2.45)
        f.crudo(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="2.2" fill="#FFFFFF" stroke="#2B2B2B" stroke-width="0.9"/>')
    xv = X + W + 8
    for i, s in enumerate(["VESDA", "(detección", "temprana", "de humo por", "aspiración)"]):
        f.texto(xv, Y + 59 + i * 10.6, s, 9)
    f.linea([(X + W + 6, Y + 1.15 * m), (X + W - 1, Y + 1.15 * m)], flecha=None, grosor=0.6, saltos=False)
    # cámaras de mini domo
    for xm, ym, _ in camaras:
        f.equipo("hw-camara", *P(xm, ym), w=13)
    # trabajo, respaldo y tablero
    f.rect(*P(4.3, 3.45), 1.4 * m, 0.45 * m, relleno="#FFFFFF", borde="#404040", grosor=0.9)
    f.icono("flu-consola", *P(5.0, 3.67), 14)
    f.texto(*P(5.0, 3.3), "Trabajo", 10, anc="middle")
    f.icono("flu-extintor", *P(5.95, 3.62), 11)                 # extintor portátil de la zona de trabajo
    f.texto(*P(5.95, 3.36), "CO₂", 9, anc="middle")
    f.rect(*P(2.7, 3.65), 1.5 * m, 0.3 * m, relleno="#FFFFFF", borde="#404040", grosor=0.9)
    f.icono("flu-repuestos", *P(3.45, 3.8), 12)
    f.texto(*P(3.45, 3.5), "Respaldo", 10, anc="middle")
    f.rect(*P(2.05, 3.8), 0.4 * m, 0.15 * m, relleno="#FFFFFF", borde="#404040", grosor=0.9)
    f.texto(*P(2.25, 3.66), "Tablero", 9, anc="middle")
    # ductos de los dos enlaces, por muros distintos, con lo que lleva cada uno
    xd, yd = P(4.9, 0)
    f.rect(xd - 4, yd - 14, 8, 16, relleno="#FFFFFF", borde="#2B2B2B", grosor=0.9)
    f.texto(xd, yd - 30, "Ducto ExpressRoute", 9, anc="middle")
    f.texto(xd, yd - 19.4, "(enlace dedicado a Azure, 100 Mbit/s)", 9, anc="middle")
    xd, yd = P(6.5, 0.6)
    f.rect(xd - 2, yd - 4, 16, 8, relleno="#FFFFFF", borde="#2B2B2B", grosor=0.9)
    for i, s in enumerate(["Ducto VPN", "(respaldo por", "el segundo", "proveedor)"]):
        f.texto(xd + 18, yd - 14 + i * 10.6, s, 9)
    # cotas y escala
    f.linea([(X, 14), (X + W, 14)], flecha="ambas", saltos=False)
    f.rotulo(X + W / 2, 17, "6,5 m")
    f.linea([(22, Y), (22, Y + H)], flecha="ambas", saltos=False)
    f.rotulo(22, Y + H / 2 + 3, "4 m")
    f.linea([(X + W - m, Y + H + 26), (X + W, Y + H + 26)], flecha=None, grosor=2.2, saltos=False)
    for xx in (X + W - m, X + W):
        f.linea([(xx, Y + H + 22), (xx, Y + H + 30)], flecha=None, saltos=False)
    f.texto(X + W - m / 2, Y + H + 41, "1 m", 9, anc="middle")
    # patio: grupo electrógeno y tablero de transferencia, con la línea de energía a la sala
    yp = Y + H + 54
    f.grupo(X, yp, 374, 110, "Patio, fuera de la sala")
    f.equipo("hw-generador", X + 80, yp + 50, w=62)
    f.texto(X + 80, yp + 82, "Grupo electrógeno", 10, anc="middle")
    f.texto(X + 80, yp + 93, "Himoinsa 8,8 kVA", 9, anc="middle")
    f.equipo("hw-tablero", X + 210, yp + 50, h=40)
    f.texto(X + 210, yp + 82, "Tablero de", 10, anc="middle")
    f.texto(X + 210, yp + 94, "transferencia", 10, anc="middle")
    f.linea([(X + 112, yp + 50), (X + 196, yp + 50)])
    tx, ty = P(2.25, 3.95)
    f.linea([(X + 210, yp + 30), (X + 210, Y + H + 14), (tx, Y + H + 14), (tx, ty)])
    f.rotulo(X + 210, yp + 2, "Energía")
    return f.guardar()


def gabinete_terminal():
    f = Figura("gabinete-terminal", C, "V", alto=530)
    f.grupo(14, 70, 200, 452, "Gabinete", "pr-gabinete", sub="Una /24 de 172.16.4.0/22")
    cx = 100
    # equipos, centrados, con su nombre debajo: (ilustración, ancho, alto, nombre, dato, y del centro)
    equipos = [("hw-rutx50", 66, None, "RUTX50", "Router 5G, dos SIM", 128),
               ("hw-tsw202", 78, None, "TSW202", "Switch PoE, riel DIN", 212),
               ("hw-karbon", 66, None, "Karbon 430 A", "Activo", 290),
               ("hw-karbon", 66, None, "Karbon 430 B", "En espera", 368),
               ("hw-ups-torre", None, 54, "UPS SRT1000XLI", "83 min con 152 W", 448)]
    caja = {}
    for ic, w, h, n, d, cy in equipos:
        x0, y0, x1, y1 = f.equipo(ic, cx, cy, w=w, h=h)
        caja[n] = (x0, y0, x1, y1)
        f.texto(cx, y1 + 11, n, 10, anc="middle")
        f.texto(cx, y1 + 22, d, 9, anc="middle")
    rt, sw, ka, kb, ups = (caja[k] for k in ("RUTX50", "TSW202", "Karbon 430 A", "Karbon 430 B", "UPS SRT1000XLI"))
    ym = lambda b, d=0: (b[1] + b[3]) / 2 + d
    # datos, por el costado izquierdo: router al switch y switch a los dos computadores
    f.linea([(rt[0], ym(rt, 16)), (54, ym(rt, 16)), (54, ym(sw, -6)), (sw[0], ym(sw, -6))], flecha="ambas")
    f.linea([(sw[0], ym(sw, 6)), (40, ym(sw, 6)), (40, ym(ka)), (ka[0], ym(ka))], flecha="ambas")
    f.linea([(40, ym(ka)), (40, ym(kb)), (kb[0], ym(kb))], flecha="fin")
    f.linea([(ka[0], ym(ka, 10)), (26, ym(ka, 10)), (26, ym(kb, 10)), (kb[0], ym(kb, 10))], disc=True, flecha="ambas")
    # la UPS alimenta a todos, por el costado derecho
    xe = 166
    f.linea([(ups[2], ym(ups)), (130, ym(ups))], flecha=None, grosor=0.75)
    f.icono("flu-enchufe", 137, ym(ups), 13)
    f.linea([(144, ym(ups)), (xe, ym(ups)), (xe, ym(rt, 22))], flecha=None, grosor=0.75)
    for b in (rt, sw, ka, kb):
        yy = ym(b, 22) if b is rt else ym(b, 10)
        f.linea([(xe, yy), (b[2], yy)], grosor=0.75)
    f.rotulo(xe, ym(kb) + 36, "Energía")
    f.ficha(cx, 508, "El terminal opera 24 h sin enlace")
    # enlaces a Azure: el fijo entra al RUTX50, que conmuta solo a 5G
    f.nodo("dev-azure", 372, 36, 26, "Azure Chile Central", "Red central, VPN IPsec")
    f.linea([(rt[2], ym(rt, 6)), (236, ym(rt, 6)), (236, 30), (359, 30)], flecha="ambas")
    f.rotulo(236, 50, ["Fijo ≥ 10 Mbit/s,", "proveedor local"])
    f.linea([(rt[2], ym(rt, 14)), (318, ym(rt, 14)), (318, 42), (359, 42)], disc=True, flecha="ambas")
    f.rotulo(318, 96, ["5G,", "dos SIM"])
    # patio: el switch alimenta el punto de acceso por un inyector y el punto actualiza un camión
    f.grupo(232, 150, 182, 140, "Patio")
    yp = ym(sw, -6)
    xi0, yi0, xi1, yi1 = f.equipo("hw-inyector", 262, 196, w=34)
    f.texto(262, yi1 + 10, "Inyector", 9, anc="middle")
    f.texto(262, yi1 + 20.5, "PoE 802.3bt", 9, anc="middle")
    f.linea([(sw[2], yp), (196, yp), (196, 196), (xi0, 196)])
    f.rotulo(214, 199, "PoE+")
    xa0, ya0, xa1, ya1 = f.equipo("hw-fortiap", 326, 196, h=40)
    f.texto(326, 228, "FortiAP 234G", 10, anc="middle")
    f.linea([(xi1, 196), (xa0, 196)])
    f.nodo("flu-camion", 378, 250, 24, "Camión", "Actualización")
    f.linea([(xa1, 186), (378, 186), (378, 237)], disc=True, flecha="ambas")
    f.rotulo(378, 214, ["Wi-Fi", "6E"])
    # portería: el lector lee la baliza del semirremolque que pasa
    f.grupo(232, 306, 182, 128, "Portería")
    f.nodo("pr-barrera", 322, 336, 22, "Barrera")
    f.equipo("hw-minew", 266, 378, w=34)
    f.texto(266, 402, "Minew G1", 10, anc="middle")
    f.nodo("pr-semirremolque", 376, 378, 28, "Semirremolque", "Baliza EYE Sensor")
    f.linea([(362, 378), (283, 378)])
    f.rotulo(322, 381, "Bluetooth")
    f.linea([(sw[2], ym(sw, 6)), (184, ym(sw, 6)), (184, 378), (249, 378)])
    f.rotulo(216, 381, "PoE")
    return f.guardar()


def recuperacion():
    """Recuperación ante desastres como procedimiento (cuarta vuelta): regla de tiempo arriba,
    pasos de izquierda a derecha y el eje de continuidad aparte, abajo. S4 1273-1315."""
    f = Figura("recuperacion", C, "H")
    YP, HP = 56, 272               # caja de los pasos
    YF = 180                       # altura de las flechas entre pasos
    pasos = {"normal": (8, 172), "det": (192, 76), "conf": (280, 84), "prom": (376, 166),
             "oper": (554, 86), "vuelta": (652, 70)}
    cx = {k: x + w / 2 for k, (x, w) in pasos.items()}
    for k, (x, w) in pasos.items():
        f.rect(x, YP, w, HP, rx=6)

    def titulo(k, lineas, y=72):
        for i, s in enumerate(lineas):
            f.texto(cx[k], y + i * 12, s, 10, 600, "middle")

    # ------------------------------------------------ regla de tiempo: solo los cuatro tiempos con fuente
    marcas = [(130, "−15 min", "RPO"), (pasos["det"][0] - 6, "0", "Caída"), (cx["det"], "15 min", "Alerta"),
              (cx["oper"], "≤ 4 h", "RTO: servicio en Brazil South")]
    f.linea([(14, 30), (716, 30)], saltos=False)
    for x, s, d in marcas:
        f.linea([(x, 25), (x, 35)], flecha=None, saltos=False)
        f.texto(x, 20, s, 9, anc="middle")
        f.texto(x, 46, d, 9, anc="middle")
    f.crudo('<path d="M413,36 L419,24 M419,36 L425,24" stroke="#2B2B2B" stroke-width="1"/>')
    f.rect(414, 28, 10, 4, relleno="#FFFFFF", borde=None, capa="frente")
    f.crudo('<path d="M413,36 L419,24 M419,36 L425,24" stroke="#2B2B2B" stroke-width="1"/>')

    # ------------------------------------------------ operación normal: las réplicas corren hacia Brazil South
    x0 = pasos["normal"][0]
    titulo("normal", ["Operación normal"])
    f.icono("az-region", x0 + 16, 94, 20)
    f.texto(x0 + 32, 92, "Chile Central", 10)
    f.texto(x0 + 32, 102.5, "Región primaria,", 9)
    f.texto(x0 + 32, 113, "activa en 3 zonas", 9)
    filas = [("az-postgres", "PostgreSQL", ["Transaccional, asíncrona"]),
             ("az-postgres", "PostgreSQL", ["Series, asíncrona"]),
             ("az-eventhubs", "Event Hubs", ["Frena la entrada si el", "retraso pasa de 10 min"]),
             ("az-storage", "Blob inmutable", ["Objetos, en minutos"]),
             ("az-keyvault", "Key Vault", ["Claves respaldadas"])]
    y = 134
    for ic, n, datos in filas:
        f.icono(ic, x0 + 40, y, 16)
        f.texto(x0 + 54, y - 1, n, 10)
        for j, d in enumerate(datos):
            f.texto(x0 + 54, y + 9.5 + j * 10.5, d, 9)
        y += 26 + 10.5 * (len(datos) - 1)
    yb = y + 6
    f.linea([(x0 + 16, 104), (x0 + 16, yb - 10)], disc=True)
    f.icono("az-region", x0 + 16, yb, 20)
    f.texto(x0 + 32, yb - 2, "Brazil South", 10)
    f.texto(x0 + 32, yb + 8.5, "En espera, RTO 4 h", 9)
    f.texto(x0 + 32, yb + 19, "y RPO 15 min", 9)
    ys = yb + 36
    f.icono("az-region", x0 + 16, ys, 14)
    f.crudo(f'<path d="M{x0 + 8},{ys - 8} L{x0 + 24},{ys + 8} M{x0 + 24},{ys - 8} L{x0 + 8},{ys + 8}" '
            f'stroke="#2B2B2B" stroke-width="1.4"/>')
    f.texto(x0 + 32, ys - 2, "South Central US", 9)
    f.texto(x0 + 32, ys + 8.5, "Sin redundancia geográfica", 9)

    # ------------------------------------------------ 1. detección
    titulo("det", ["1. Detección"])
    f.nodo("az-monitor", cx["det"], 108, 26, ["Monitor y", "Log Analytics"])
    f.ficha(cx["det"], 228, ["Sin respuesta", "durante 15 min"])

    # ------------------------------------------------ 2. confirmación, con su salida «no»
    titulo("conf", ["2. Confirmación"])
    f.nodo("flu-operador", cx["conf"], 108, 26, "La guardia", ["Desastre y no", "falla pasajera"])
    f.linea([(cx["conf"], 160), (cx["conf"], YF - 4.5)], flecha=None)
    f.rombo(cx["conf"], YF)
    f.linea([(cx["conf"], YF + 4.5), (cx["conf"], 220)])
    f.ficha(cx["conf"], 235, ["No: sin", "conmutación"])
    f.texto(cx["conf"] + 30, YF - 4, "Sí", 9, anc="middle")

    # ------------------------------------------------ 3. promoción automatizada y documentada
    xp = pasos["prom"][0]
    titulo("prom", ["3. Promoción"])
    f.texto(cx["prom"], 85, "Automatizada y documentada", 9, anc="middle")
    f.grupo(xp + 8, 94, 150, 136, "Datos:", rx=6, sub="se promueven")
    celdas = [("az-postgres", "PostgreSQL", "Pasa a primaria"), ("az-postgres", "PostgreSQL", "Series"),
              ("az-eventhubs", "Event Hubs", None), ("az-storage", "Blob inmutable", None)]
    for i, (ic, n, d) in enumerate(celdas):
        f.nodo(ic, xp + 44 + (i % 2) * 78, 130 + (i // 2) * 50, 18, n, d)
    f.texto(cx["prom"], 224, "Afectan el RPO", 9, anc="middle")
    f.grupo(xp + 8, 238, 150, 84, "Cómputo y claves:", rx=6, sub="se levantan")
    f.nodo("az-aks", xp + 44, 272, 18, "AKS", "Mismo código")
    f.nodo("az-keyvault", xp + 118, 272, 18, "Key Vault", "Claves respaldadas")
    f.texto(cx["prom"], 316, "Afectan el RTO, no el RPO", 9, anc="middle")

    # ------------------------------------------------ 4. operación en Brazil South
    titulo("oper", ["4. Operación en", "Brazil South"])
    f.icono("az-region", cx["oper"], 112, 24)
    f.ficha(cx["oper"], 142, "Servicio en ≤ 4 h")
    f.nodo("flu-camion", cx["oper"], 218, 24, "Camiones", ["Reenvían sus", "últimas 72 h"])
    lineas = ["Idempotencia de", "7 días: descarta", "duplicados"]
    for i, s in enumerate(lineas):
        f.texto(cx["oper"], 276 + i * 10.5, s, 9, anc="middle")

    # ------------------------------------------------ vuelta a Chile Central
    titulo("vuelta", ["Vuelta a", "Chile Central"])
    f.icono("az-region", cx["vuelta"], 112, 24)
    f.texto(cx["vuelta"], 138, "Procedimiento", 9, anc="middle")
    f.texto(cx["vuelta"], 148.5, "igual", 9, anc="middle")
    f.ficha(cx["vuelta"], 228, "Conciliación")

    # flechas entre pasos
    orden = ["normal", "det", "conf", "prom", "oper", "vuelta"]
    for a, b in zip(orden, orden[1:]):
        xa = pasos[a][0] + pasos[a][1]
        if a == "conf":
            f.linea([(cx["conf"] + 4.5, YF), (pasos[b][0], YF)])
        else:
            f.linea([(xa, YF), (pasos[b][0], YF)])

    # llave bajo los pasos 1 a 4
    xa, xb, yl = pasos["det"][0], pasos["oper"][0] + pasos["oper"][1], 336
    f.linea([(xa, YP + HP + 2), (xa, yl), (xb, yl), (xb, YP + HP + 2)], flecha=None, saltos=False)
    f.linea([((xa + xb) / 2, yl), ((xa + xb) / 2, yl + 5)], flecha=None, saltos=False)
    f.texto((xa + xb) / 2, yl + 17, "Se prueba de verdad 2 veces al año", 9, anc="middle")

    # ------------------------------------------------ eje separado: continuidad si cae el enlace
    f.grupo(14, 368, 702, 98, "Continuidad si cae el enlace", sub="Eje separado: no hay conmutación")
    for i, (ic, n, fichas) in enumerate([("flu-camion", "Camiones", ["Búfer de 288 h", "Reconexión tras 72 h"]),
                                         ("pr-pc-industrial", "Terminales", ["24 h sin enlace"]),
                                         ("pr-servidor", "San Bernardo", ["24 h sin enlace"])]):
        x = 24 + i * 232
        f.rect(x, 390, 218, 68, rx=6)
        f.nodo(ic, x + 60, 414, 24, n)
        for j, s in enumerate(fichas):
            f.ficha(x + 150, 424 + (j - (len(fichas) - 1) / 2) * 19, s, w=110)
    return f.guardar()


def _region_secundaria(nombre, carpeta, conexiones):
    """Azure Brazil South con la diagramación de region_primaria: mismas posiciones, íconos,
    niveles, grupos de seguridad y puntos de conexión privados. Cambian el estado de cada
    servicio y las conexiones. S4 841-850, 880-881 y 1261-1291; T-11 366-410 y 557-563."""
    f = Figura(nombre, carpeta, "H")
    # fichas de la región, arriba
    f.ficha(214, 16, "Suscripción del mandante", anc="start")
    f.ficha(338, 16, "Idéntica a producción, mismo código", anc="start")
    f.ficha(214, 42, "Activo-pasivo, RTO 4 h y RPO 15 min", anc="start")
    f.ficha(376, 42, ["2.586 km de Santiago, ≥ 26 ms ida", "y vuelta, se mide en la Etapa 1"], anc="start")

    f.grupo_az(204, 60, 482, 410, "Azure Brazil South", "az-region", sub="São Paulo, 3 zonas de disponibilidad, en espera")
    # red de recuperación
    f.grupo_az(214, 84, 462, 268, "Red de recuperación", "az-vnet", sub="10.21.0.0/20")
    YS = 154          # fila de íconos de las subredes de arriba
    subred(f, 224, 108, 90, 114, "Borde", "10.21.1.0/24")
    f.nodo("az-apim", 269, YS, 26, "API Management", "Premium")
    f.ficha(269, 206, ["Se despliega", "al promover"])
    subred(f, 322, 108, 132, 114, "Aplicación", "10.21.4.0/22")
    f.nodo("az-aks", 388, YS, 26, "AKS")
    f.ficha(388, 206, "Clúster en espera")
    subred(f, 462, 108, 206, 114, "Integración", "10.21.2.0/24")
    f.nodo("az-eventhubs", 506, YS, 26, "Event Hubs", ["Premium, Kafka,", "≤ 10 min"])
    f.ficha(506, 211, "Réplica activa")
    f.nodo("az-iothub", 576, YS, 26, "IoT Hub", "S1 × 2")
    f.nodo("az-dps", 636, YS, 26, "Provisioning", "DPS")
    f.ficha(606, 206, ["IoT Hub y DPS: se", "despliegan al promover"])
    YD = 276          # fila de íconos de las subredes de abajo
    subred(f, 224, 230, 90, 116, "Gestión", "10.21.8.0/24")
    f.nodo("az-monitor", 262, YD, 26, ["Monitor y", "Log Analytics"])
    f.ficha(262, 330, ["Se despliega", "al promover"])
    subred(f, 322, 230, 346, 116, "Datos", "10.21.3.0/24")
    datos = [("az-postgres", "PostgreSQL", ["Transaccional,", "réplica de lectura"], 372),
             ("az-postgres", "PostgreSQL", ["Series, TimescaleDB,", "réplica propia"], 460),
             ("az-storage", "Blob inmutable", ["Local o de zona,", "objetos en minutos"], 552),
             ("az-keyvault", "Key Vault", ["Premium, claves", "respaldadas"], 630)]
    for ic, n, d, x in datos:
        f.nodo(ic, x, YD, 26, n, d)
        f.icono("az-privateendpoint", x + 16, YD - 11, 11)
        f.ficha(x, 336, "Réplica activa")

    # réplicas desde Chile Central: entran por el borde izquierdo, en discontinua
    f.icono("az-region", 46, 226, 24)
    f.texto(46, 252, "Azure", 10, anc="middle")
    f.texto(46, 264, "Chile Central", 10, anc="middle")
    f.texto(46, 275, "Región primaria", 9, anc="middle")
    f.linea([(59, 226), (630, 226)], disc=True, flecha=None)
    f.rotulo(132, 229, "Réplicas")
    f.linea([(340, 226), (340, YD), (359, YD)], disc=True)
    for x in (460, 552, 630):
        f.linea([(x, 226), (x, YD - 13)], disc=True)
    f.linea([(466, 226), (466, YS), (493, YS)], disc=True)
    # el código de infraestructura llega desde el repositorio del mandante
    f.nodo("dev-git", 140, 80, 24, ["Repositorio", "del mandante"], ["Código de", "infraestructura"])
    f.linea([(153, 80), (204, 80)], disc=True)
    f.rotulo(178, 83, "Despliega")
    # pareja de la región, que no se usa
    f.icono("az-region", 24, 302, 18)
    f.crudo('<path d="M14,292 L34,312 M34,292 L14,312" stroke="#2B2B2B" stroke-width="1.5"/>')
    f.texto(40, 300, "South Central US", 10)
    f.texto(40, 310.5, "Pareja de la región, no se usa:", 9)
    f.texto(40, 321, "llevaría los datos fuera", 9)
    f.texto(40, 331.5, "de Sudamérica", 9)

    # red central, con los mismos componentes que la de Chile Central
    f.grupo_az(214, 358, 300, 108, "Red central", "az-vnet", sub="10.20.0.0/22")
    f.icono("az-expressroute", 234, 392, 20)
    f.texto(248, 390, "ExpressRoute", 10)
    f.texto(248, 401, "ErGw1AZ", 9)
    f.icono("az-vpngw", 234, 440, 20)
    f.texto(248, 438, "Puerta VPN", 10)
    f.texto(248, 449, "VpnGw1AZ", 9)
    f.nodo("az-firewall", 382, 414, 26, "Firewall", "Premium")
    cadena(f, 382, 401, 352, [("az-routetable", 374, 16)])
    f.rotulo(382, 392, "Tabla de rutas")
    f.nodo("az-bastion", 466, 414, 26, "Bastion", ["Acceso", "administrativo"])
    f.linea([(466, 401), (466, 352)], disc=True)
    f.rotulo(466, 378, "Subredes")
    # un solo ambiente
    f.grupo_az(524, 358, 152, 108, "Un solo ambiente", "az-subscription")
    f.texto(534, 394, "Recuperación de", 10)
    f.texto(534, 406, "producción", 10)
    f.texto(534, 424, "Desarrollo, QA y", 9)
    f.texto(534, 434.5, "preproducción, solo", 9)
    f.texto(534, 445, "en Chile Central", 9)

    if conexiones:
        # propuesta: cómo llegarían los actores externos tras la promoción (el S4 no lo dice)
        f.nodo("rol-usuarios", 150, 22, 24, "Usuarios")
        f.linea([(138, 22), (52, 22), (52, 141)], disc=True)
        f.nodo("az-frontdoor", 52, YS, 26, "Front Door", ["Premium,", "global"])
        f.linea([(65, YS), (256, YS)], disc=True)
        f.rotulo(160, YS + 3, "Tras la promoción")
        f.nodo("flu-camion", 690, 22, 26, "Camiones", "182 equipos audIT")
        f.linea([(676, 18), (568, 18), (568, 141)], disc=True, flecha="ambas")
        f.linea([(676, 28), (582, 28), (582, 141)], disc=True, flecha="ambas")
        f.rotulo(624, 21, "Tras la promoción")
        eq(f, "hw-fortigate", 46, 380, "San Bernardo", "FortiGate 90G", w=52)
        f.linea([(72, 380), (196, 380), (196, 392), (224, 392)], disc=True, flecha="ambas")
        f.rotulo(134, 383, "Tras la promoción")
        eq(f, "hw-rutx50", 46, 436, "Terminales", "RUTX50", w=30)
        f.linea([(61, 446), (118, 446), (224, 446)], disc=True, flecha="ambas")
        f.rotulo(160, 449, "Tras la promoción")
    return f.guardar()


def region_secundaria():
    return _region_secundaria("region-secundaria", C, conexiones=False)


def region_secundaria_conexiones():
    return _region_secundaria("region-secundaria-conexiones", "propuestas", conexiones=True)


FIGURAS = [fisica_general, region_primaria, region_secundaria, region_secundaria_conexiones, equipo_a_bordo, ambientes, ambientes_promocion, reconexion, sala_san_bernardo,
           gabinete_terminal, recuperacion]
