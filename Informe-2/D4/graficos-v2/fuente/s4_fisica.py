"""Subdocumento 4, secciones 4.2 y 4.3: figuras físicas (segunda vuelta).

Base: message.txt, contenido.tex del S4 y el Formulario T-11. Cada dato nuevo
tiene su origen anotado en INFORME.md.
"""
from lienzo import Figura, ancho, GRIS_CLARO, BORDE

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
    f.nodo("pr-generador", 120, 172, 26, ["Grupo", "electrógeno"], "Himoinsa")
    f.grupo(22, 256, 128, 58, "Patio", rx=6)
    f.icono("pr-wifi", 52, 286, 18)
    f.texto(52, 305, "FortiAP 234G", 9, anc="middle")
    f.icono("pr-ble", 120, 286, 18)
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
    f.icono("pr-wifi", 516, 278, 18)
    f.texto(516, 297, "FortiAP", 9, anc="middle")
    f.texto(516, 307.5, "234G", 9, anc="middle")
    f.icono("pr-ble", 568, 278, 18)
    f.texto(568, 297, "Minew G1", 9, anc="middle")
    f.linea([(506, 124), (506, 96)], flecha="ambas")
    f.rotulo(506, 106, ["Fijo", "≥ 10 Mbit/s"])
    f.linea([(566, 124), (566, 96)], disc=True, flecha="ambas")
    f.rotulo(566, 106, ["5G de", "respaldo"])

    # ---------------------------------------------------------------- enlaces de la flota
    cadena(f, 392, 368, 96, [("pr-antena", 236, 24)])
    f.rotulo(392, 260, ["Operador", "móvil"], tam=10)
    f.rotulo(392, 106, "LTE")
    cadena(f, 444, 368, 96, [("flu-satelite", 300, 24), ("flu-antena-tierra", 176, 24)], disc=True)
    f.rotulo(444, 324, "Satélite", tam=10)
    f.rotulo(444, 200, ["Puerta", "Iridium"], tam=10)
    f.rotulo(444, 106, "≤ 340 bytes")

    # ---------------------------------------------------------------- flota
    f.grupo(84, 368, 368, 98, "Flota con equipo audIT")
    f.nodo("flu-camion", 154, 410, 28, "182 tractocamiones", "148 propios y 34 de terceros")
    f.nodo("pr-g26i", 250, 410, 26, "iWave G26I")
    f.nodo("pr-baliza", 336, 410, 24, "Baliza", "EYE Sensor")
    f.nodo("pr-semirremolque", 412, 410, 28, ["210", "semirremolques"], "44 refrigerados")
    f.linea([(324, 410), (263, 410)])
    f.rotulo(293, 413, "Bluetooth")
    f.grupo(480, 334, 120, 132, "Flota de terceros")
    f.nodo("flu-camion", 540, 390, 28, "192", ["tractocamiones", "con equipo propio"])

    # ---------------------------------------------------------------- contrapartes
    f.grupo(622, 86, 98, 380, "Contrapartes")
    f.grupo(628, 106, 86, 112, "Por lotes", rx=6)
    f.nodo("flu-combustible", 671, 136, 18, ["Estaciones", "de servicio"])
    f.nodo("flu-peaje", 671, 186, 18, "Peajes")
    f.grupo(628, 224, 86, 236, "En línea", rx=6)
    f.nodo("flu-empresa", 671, 254, 18, "Clientes")
    f.nodo("flu-edificio-publico", 671, 292, 18, "Aduana")
    f.nodo("flu-edificio-publico", 671, 330, 18, ["Dirección", "del Trabajo"])
    f.nodo("flu-fabrica", 671, 378, 18, ["Telemetría", "de fábrica"])
    f.nodo("pr-rastreador", 671, 424, 18, ["Plataformas de", "2 proveedores"])
    f.linea([(600, 424), (660, 424)])
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
    f.nodo("pr-firewall", 50, 380, 24, "San Bernardo", "FortiGate 90G")
    f.linea([(62, 380), (238, 380)], flecha="ambas")
    f.rotulo(150, 376, ["ExpressRoute 100 Mbit/s", "EdgeConnex SCL"])
    f.linea([(62, 388), (118, 388), (118, 428), (238, 428)], disc=True, flecha="ambas")
    f.rotulo(160, 431, "VPN de respaldo")
    f.nodo("pr-router", 50, 440, 22, "Terminales")
    f.linea([(61, 438), (238, 438)], flecha="ambas")
    f.rotulo(160, 441, "VPN")
    return f.guardar()


def equipo_a_bordo():
    f = Figura("equipo-a-bordo", C, "V", alto=482)
    # techo con las dos antenas
    f.grupo(118, 8, 196, 70, "Techo", rx=6)
    f.nodo("pr-iridium", 168, 40, 22, "Iridium Edge")
    f.nodo("pr-aleta", 262, 40, 22, "Antena LTE y GNSS")
    # afuera: satélite, red celular, baliza y patio
    f.nodo("flu-satelite", 380, 26, 22, "Satélite")
    f.linea([(168, 29), (168, 14), (350, 14), (350, 26), (369, 26)], disc=True, flecha="ambas")
    f.rotulo(258, 17, "≤ 340 bytes")
    f.nodo("pr-antena", 380, 104, 22, "Red celular")
    f.linea([(273, 40), (330, 40), (330, 104), (369, 104)], flecha="ambas")
    f.rotulo(330, 74, "LTE")
    f.nodo("pr-baliza", 380, 196, 22, "Baliza", "EYE Sensor")
    f.nodo("pr-wifi", 380, 276, 22, ["Patio del", "terminal"], "FortiAP 234G")

    # cabina
    f.grupo(8, 88, 318, 248, "Cabina")
    f.grupo(140, 110, 166, 168, "iWave G26I", "pr-g26i", rx=6, grosor=1.2)
    fichas = ["Linux", ["Elemento seguro TA100", "arranque seguro y claves"], "audIT EdgeHub",
              "Motor de geocercas", "Búfer de 288 h", "SQLite en modo WAL"]
    y = 140
    for s in fichas:
        n = len(s) if isinstance(s, list) else 1
        hh = 14 + (n - 1) * 10.6
        f.ficha(223, y + hh / 2, s, w=150)
        y += hh + 4
    # antenas al equipo
    f.linea([(168, 78), (168, 110)], flecha="ambas")
    f.rotulo(168, 98, "RS232")
    f.linea([(262, 78), (262, 110)], flecha="ambas")
    f.rotulo(262, 98, "Coaxial")
    # arnés CAN del camión con el lector pinzado, sin cortarlo
    f.linea([(46, 112), (46, 206)], flecha=None, grosor=3.2, color="#9B9B9B", saltos=False)
    f.linea([(53, 112), (53, 206)], flecha=None, grosor=3.2, color="#9B9B9B", saltos=False)
    f.icono("pr-can", 50, 140, 26, revisar=False)
    f.rotulo(50, 167, "CANCrocodile", tam=10)
    f.rotulo(50, 194, "Arnés CAN")
    f.linea([(63, 140), (140, 140)])
    f.rotulo(102, 143, "CAN J1939")
    f.nodo("pr-lector-tarjeta", 70, 232, 24, "Lector DESFire", "GAO MIFARE")
    f.linea([(82, 228), (140, 228)])
    f.rotulo(112, 231, "RS485")
    f.nodo("flu-bateria", 70, 296, 22, "Batería del camión", "9 a 32 V")
    f.linea([(81, 296), (180, 296), (180, 278)])
    f.rotulo(130, 299, "Energía")
    # periféricos externos
    f.linea([(369, 196), (306, 196)])
    f.rotulo(338, 199, "Bluetooth")
    f.linea([(369, 270), (306, 270)])
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


def ambientes():
    f = Figura("ambientes", C, "V", alto=512)
    cajas = [("Desarrollo", "10.14.0.0/20", ["Chile Central", "Niveles menores"], 10, False),
             ("QA", "10.13.0.0/20", ["Chile Central", "Niveles menores"], 108, False),
             ("Preproducción", "10.12.0.0/20", ["Chile Central", "Pruebas de carga 1,5 × peak"], 206, False),
             ("Producción", "10.11.0.0/20", ["Zona 1", "Zona 2", "Zona 3"], 304, False),
             ("Recuperación", "10.21.0.0/20", ["Brazil South", "En espera"], 426, True)]
    x, w, h = 116, 256, 80
    contenido = [("az-aks", "AKS"), ("az-postgres", "PostgreSQL"), ("az-iothub", "IoT Hub"),
                 ("az-eventhubs", "Event Hubs")]
    for n, rango, fichas, y, disc in cajas:
        f.grupo_az(x, y, w, h, n, "az-subscription", sub=rango, discontinuo=disc)
        for i, (ic, nom) in enumerate(contenido):
            cx = x + w * (i + 0.5) / 4
            f.icono(ic, cx, y + 34, 16)
            f.texto(cx, y + 53, nom, 9, anc="middle")
        anchos = [ancho(s, 9) + 9 for s in fichas]
        total = sum(anchos) + 6 * (len(fichas) - 1)
        cx = x + (w - total) / 2
        for s, a in zip(fichas, anchos):
            f.ficha(cx + a / 2, y + 68, s)
            cx += a + 6
    # el repositorio alimenta los cinco ambientes
    f.nodo("dev-git", 46, 230, 28, ["Repositorio", "del mandante"], ["Código de", "infraestructura"])
    f.linea([(60, 230), (96, 230)], flecha=None)
    ys = [y + h / 2 for _, _, _, y, _ in cajas]
    f.linea([(96, ys[0]), (96, ys[-1])], flecha=None)
    for y in ys:
        f.linea([(96, y), (x, y)])
    # promoción, de un ambiente al siguiente
    for (_, _, _, y1, _), (_, _, _, y2, _) in zip(cajas[:3], cajas[1:4]):
        f.linea([(x + w, y1 + 56), (x + w + 24, y1 + 56), (x + w + 24, y2 + 22), (x + w, y2 + 22)])
        f.rotulo(x + w + 24, (y1 + 56 + y2 + 22) / 2 + 3, "Promoción")
    # réplica a recuperación
    f.linea([(x + w / 2, 304 + h), (x + w / 2, 426)], disc=True)
    f.rotulo(x + w / 2, 408, "Réplica asíncrona")
    return f.guardar()


def reconexion():
    f = Figura("reconexion", C, "V", alto=556)
    cx = 180
    # tramo 1: los 300 camiones salen de la sombra con 192 mensajes cada uno
    f.marcador(18, 30, 1)
    for x in (100, 172, 244):
        f.icono("flu-camion", x, 24, 24)
        f.texto(x, 50, "192 mensajes", 9, anc="middle")
        f.linea([(x, 56), (x, 66), (cx, 66)], flecha=None)
    f.ficha(344, 24, "× 300")
    f.ficha(344, 44, "57.600 mensajes")
    f.linea([(cx, 66), (cx, 92)])
    # tramo 2: red celular, con espera aleatoria y reintento
    f.marcador(18, 112, 2)
    f.nodo("pr-antena", cx, 106, 26, "Red celular")
    f.icono("flu-espera", 260, 100, 18)
    f.icono("flu-reintento", 284, 100, 18)
    f.texto(272, 124, "Espera aleatoria", 9, anc="middle")
    f.texto(272, 134.5, "y reintento", 9, anc="middle")
    f.linea([(cx, 132), (cx, 172)])
    f.rotulo(cx, 156, "Conexiones en 3 s")
    # tramo 3: IoT Hub
    f.marcador(18, 192, 3)
    f.nodo("az-iothub", cx, 186, 26, "IoT Hub S1 × 2")
    f.icono("pr-medidor", 268, 182, 22)
    f.texto(268, 204, "100 envíos/s", 9, anc="middle")
    f.linea([(cx, 212), (cx, 252)])
    f.rotulo(cx, 236, "57.600 en 9,6 min")
    # tramo 4: Event Hubs como cola
    f.marcador(18, 272, 4)
    f.nodo("az-eventhubs", 120, 266, 26, "Event Hubs")
    f.rect(152, 254, 112, 26, relleno="#FFFFFF", borde="#404040", grosor=0.75, rx=4)
    for i in range(8):
        f.rect(158 + i * 13, 259, 8, 16, relleno=GRIS_CLARO, borde="#9B9B9B", grosor=0.5, rx=1.5)
    f.texto(208, 294, "Cola retenida", 9, anc="middle")
    f.linea([(cx, 280), (cx, 286)], flecha=None)
    f.linea([(133, 266), (152, 266)], flecha=None)
    f.linea([(264, 266), (318, 266)], disc=True)
    f.linea([(cx, 300), (cx, 334)])
    # tramo 5: consumidores en AKS, por lotes
    f.marcador(18, 352, 5)
    for i in range(4):
        f.icono("pr-pod", 138 + i * 28, 348, 18)
    f.texto(cx, 371, "Consumidores en AKS", 10, anc="middle")
    f.ficha(cx, 386, "Por lotes")
    f.linea([(cx, 393), (cx, 420)])
    f.nodo("az-postgres", cx, 434, 26, "PostgreSQL de series")
    # indicador en la columna derecha
    f.grupo(318, 232, 96, 104, "Indicador")
    f.nodo("az-monitor", 366, 276, 24, ["Profundidad", "de la cola"], "Retraso de proceso")
    # barra de tiempo, en proporción: 0 a 20 minutos
    x0, x1, yb = 30, 396, 494
    def xt(minutos):
        return x0 + (x1 - x0) * minutos / 20
    f.rect(x0, yb - 5, xt(9.6) - x0, 10, relleno=GRIS_CLARO, borde="#9B9B9B", grosor=0.5)
    f.linea([(x0, yb), (x1, yb)], flecha=None, saltos=False)
    for m in (0.05, 1.5, 9.6, 20):
        f.linea([(xt(m), yb - 9), (xt(m), yb + 9)], flecha=None, saltos=False)
    f.texto(x0, yb + 21, "3 s, conexiones", 9)
    f.texto(xt(1.5), yb - 14, "1,5 min, fotos", 9, anc="middle")
    f.texto(xt(9.6), yb - 14, "9,6 min, mensajes", 9, anc="middle")
    f.texto(x1, yb - 14, "20 min, límite RT-03.13", 9, anc="end")
    return f.guardar()


def sala_san_bernardo():
    import math
    f = Figura("sala-san-bernardo", C, "V", alto=420)
    m = 50                     # puntos por metro: 6,5 m = 325 pt
    X, Y, W, H = 48, 46, 6.5 * m, 4 * m

    def P(xm, ym):
        return X + xm * m, Y + ym * m

    def cono(xm, ym, ang, largo=1.3, abre=28):
        x0, y0 = P(xm, ym)
        pts = [(x0, y0)]
        for a in (ang - abre, ang + abre):
            pts.append((x0 + largo * m * math.cos(math.radians(a)), y0 + largo * m * math.sin(math.radians(a))))
        f.crudo('<path d="M{:.2f},{:.2f} L{:.2f},{:.2f} L{:.2f},{:.2f} Z" fill="#ECECEC"/>'.format(
            *pts[0], *pts[1], *pts[2]), capa="fondo")

    # conos de las cuatro cámaras (debajo de todo)
    for xm, ym, ang in [(0.15, 0.15, 45), (6.35, 0.15, 135), (6.35, 3.85, 225), (0.15, 2.55, 45)]:
        cono(xm, ym, ang)
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
    f.icono("pr-lector-facial", *P(1.35, 4.3), 14)
    f.texto(*P(1.35, 4.64), "Lector", 9, anc="middle")
    f.icono("pr-lector-facial", *P(1.15, 2.68), 14)
    f.texto(*P(1.15, 3.02), "Lector", 9, anc="middle")
    # entrada
    f.linea([P(0.7, 5.0), P(0.7, 4.08)])
    f.rotulo(*P(0.7, 4.98), "Entrada")
    # cilindro de FK-5-1-12 junto a la esclusa
    cx, cy = P(1.7, 3.62)
    f.crudo(f'<circle cx="{cx:.2f}" cy="{cy:.2f}" r="{0.16 * m:.2f}" fill="#E6E6E6" stroke="#404040" stroke-width="0.9"/>')
    f.texto(*P(1.5, 3.3), "FK-5-1-12", 9)
    # climas en muros opuestos, con el cable detector de agua delante
    f.rect(*P(0, 0.35), 0.35 * m, 1.0 * m, relleno="#FFFFFF", borde="#404040", grosor=1.2)
    f.texto(*P(0.5, 0.65), "Clima A", 10)
    f.rect(*P(6.15, 2.0), 0.35 * m, 1.0 * m, relleno="#FFFFFF", borde="#404040", grosor=1.2)
    f.texto(*P(6.05, 2.25), "Clima B", 10, anc="end")
    f.linea([P(0.45, 0.85), P(0.45, 1.2)], flecha=None, saltos=False)
    f.icono("flu-agua", *P(0.45, 1.32), 10)
    f.texto(*P(0.45, 1.6), "Agua", 9, anc="middle")
    f.linea([P(6.05, 2.5), P(6.05, 2.95)], flecha=None, saltos=False)
    f.icono("flu-agua", *P(6.05, 3.07), 10)
    f.texto(*P(6.05, 3.35), "Agua", 9, anc="middle")
    # racks a escala, con el frente hacia el pasillo
    for x0, nombre in ((2.0, "Servidores"), (3.6, "Comunicaciones")):
        f.rect(*P(x0, 0.35), 0.6 * m, 1.0 * m, relleno="#FFFFFF", borde="#404040", grosor=1.2)
        xa, ya = P(x0, 1.35)
        f.crudo(f'<path d="M{xa:.2f},{ya:.2f} h{0.6 * m:.2f}" stroke="#2B2B2B" stroke-width="3"/>')
        f.texto(*P(x0 + 0.3, 0.92), "24 U", 9, anc="middle")
        f.texto(*P(x0 + 0.3, 0.28), nombre, 10, anc="middle")
    f.rect(*P(1.8, 1.5), 2.6 * m, 0.7 * m, relleno="none", borde="#9B9B9B", grosor=0.6, disc=True, rx=3)
    f.texto(*P(3.1, 1.92), "Pasillo de trabajo", 9, anc="middle")
    # VESDA: detector en el muro y tubería por el cielo con sus puntos de muestreo
    f.icono("pr-vesda", *P(6.22, 1.15), 16)
    f.texto(*P(6.22, 1.52), "VESDA", 9, anc="middle")
    f.linea([P(6.06, 1.15), P(5.15, 1.15), P(5.15, 2.45), P(1.6, 2.45)], disc=True, flecha=None, saltos=False)
    for xm in (2.0, 3.0, 4.0, 5.0):
        x, y = P(xm, 2.45)
        f.crudo(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="2.2" fill="#FFFFFF" stroke="#2B2B2B" stroke-width="0.9"/>')
    # cámaras
    for xm, ym in [(0.15, 0.15), (6.35, 0.15), (6.35, 3.85), (0.15, 2.55)]:
        f.icono("pr-camara", *P(xm, ym), 12)
    # trabajo, respaldo y tablero
    f.rect(*P(4.3, 3.45), 1.4 * m, 0.45 * m, relleno="#FFFFFF", borde="#404040", grosor=0.9)
    f.icono("flu-consola", *P(5.0, 3.67), 14)
    f.texto(*P(5.0, 3.3), "Trabajo", 10, anc="middle")
    f.rect(*P(2.7, 3.65), 1.5 * m, 0.3 * m, relleno="#FFFFFF", borde="#404040", grosor=0.9)
    f.icono("flu-repuestos", *P(3.45, 3.8), 12)
    f.texto(*P(3.45, 3.5), "Respaldo", 10, anc="middle")
    f.rect(*P(2.05, 3.8), 0.4 * m, 0.15 * m, relleno="#FFFFFF", borde="#404040", grosor=0.9)
    f.texto(*P(2.25, 3.65), "Tablero", 9, anc="middle")
    # ductos de los dos enlaces, por muros distintos
    xd, yd = P(4.9, 0)
    f.rect(xd - 4, yd - 14, 8, 16, relleno="#FFFFFF", borde="#2B2B2B", grosor=0.9)
    f.texto(xd, yd - 18, "Ducto ExpressRoute", 9, anc="middle")
    xd, yd = P(6.5, 0.6)
    f.rect(xd - 2, yd - 4, 16, 8, relleno="#FFFFFF", borde="#2B2B2B", grosor=0.9)
    f.texto(xd + 18, yd - 2, "Ducto", 9)
    f.texto(xd + 18, yd + 8.6, "VPN", 9)
    # cotas y escala
    f.linea([(X, 14), (X + W, 14)], flecha="ambas", saltos=False)
    f.rotulo(X + W / 2, 17, "6,5 m")
    f.linea([(24, Y), (24, Y + H)], flecha="ambas", saltos=False)
    f.rotulo(24, Y + H / 2 + 3, "4 m")
    f.linea([(X + W - m, Y + H + 26), (X + W, Y + H + 26)], flecha=None, grosor=2.2, saltos=False)
    for xx in (X + W - m, X + W):
        f.linea([(xx, Y + H + 22), (xx, Y + H + 30)], flecha=None, saltos=False)
    f.texto(X + W - m / 2, Y + H + 41, "1 m", 9, anc="middle")
    # patio: grupo electrógeno y tablero de transferencia, con la línea de energía a la sala
    f.grupo(X, Y + H + 52, 230, 112, "Patio, fuera de la sala")
    f.nodo("pr-generador", X + 50, Y + H + 104, 26, ["Grupo", "electrógeno"], "Himoinsa 8,8 kVA")
    f.nodo("pr-transferencia", X + 160, Y + H + 104, 24, ["Tablero de", "transferencia"])
    f.linea([(X + 63, Y + H + 104), (X + 148, Y + H + 104)])
    tx, ty = P(2.25, 3.95)
    f.linea([(X + 160, Y + H + 92), (X + 160, Y + H + 40), (tx, Y + H + 40), (tx, ty)])
    f.rotulo(X + 160, Y + H + 74, "Energía")
    return f.guardar()


def gabinete_terminal():
    f = Figura("gabinete-terminal", C, "V", alto=456)
    f.grupo(14, 60, 200, 390, "Gabinete", "pr-gabinete", sub="Una /24 de 172.16.4.0/22")
    # riel DIN detrás de los equipos
    for y in (110, 180, 250, 320, 390):
        f.rect(24, y + 4, 80, 4, relleno="#C8C8C8", borde=None)
    equipos = [("pr-router", "RUTX50", "Router 5G", 110), ("pr-switch", "TSW202", "Switch", 180),
               ("pr-pc-industrial", "Karbon 430 A", "Activo", 250), ("pr-pc-industrial", "Karbon 430 B", "En espera", 320),
               ("pr-ups", "UPS SRT1000XLI", None, 390)]
    for ic, n, d, y in equipos:
        f.nodo(ic, 64, y, 26, n, d)
    f.ficha(64, 432, "83 min")
    f.ficha(160, 432, "24 h sin enlace")
    # conexiones internas
    f.linea([(51, 110), (30, 110), (30, 180), (51, 180)], flecha="ambas")
    for y in (250, 320):
        f.linea([(77, 184), (118, 184), (118, y - 4), (77, y - 4)], flecha="ambas")
    f.linea([(51, 254), (30, 254), (30, 324), (51, 324)], disc=True, flecha="ambas")
    # la UPS alimenta a todos
    f.linea([(77, 394), (111, 394)], flecha=None, grosor=0.75)
    f.icono("flu-enchufe", 118, 394, 14)
    for y in (118, 188, 258, 328):
        f.linea([(125, 394), (160, 394), (160, y), (77, y)], grosor=0.75)
    f.rotulo(160, 366, "Energía")
    # enlaces hacia Azure
    f.nodo("az-region", 370, 40, 26, "Azure Chile Central", "Red central, VPN")
    f.linea([(77, 102), (250, 102), (250, 36), (357, 36)], flecha="ambas")
    f.rotulo(304, 39, "Fijo ≥ 10 Mbit/s")
    f.linea([(77, 112), (262, 112), (262, 46), (357, 46)], disc=True, flecha="ambas")
    f.rotulo(310, 49, "5G de respaldo")
    # patio: el punto de acceso actualiza un camión
    f.grupo(240, 150, 174, 104, "Patio")
    f.nodo("pr-wifi", 296, 200, 26, "FortiAP 234G")
    f.nodo("flu-camion", 380, 200, 26, "Camión")
    f.linea([(309, 200), (367, 200)], disc=True)
    f.rotulo(338, 203, "Wi-Fi")
    f.linea([(77, 176), (200, 176), (200, 200), (283, 200)])
    # portería: el lector lee la baliza del semirremolque que pasa
    f.grupo(240, 282, 174, 108, "Portería")
    f.nodo("pr-barrera", 322, 312, 22, "Barrera")
    f.nodo("pr-ble", 272, 340, 26, "Minew G1")
    f.nodo("pr-semirremolque", 374, 340, 26, "Semirremolque", "Baliza EYE Sensor")
    f.linea([(361, 346), (285, 346)])
    f.rotulo(323, 349, "Bluetooth")
    f.linea([(77, 184), (118, 184), (118, 300), (220, 300), (220, 340), (259, 340)])
    return f.guardar()


def recuperacion():
    f = Figura("recuperacion", C, "H")
    # pasos de la conmutación
    f.grupo(14, 8, 702, 110, "Conmutación")
    pasos = [("az-monitor", "1. Detección", "15 min sin respuesta"),
             ("flu-operador", "2. Confirmación", "De la guardia"),
             ("flu-engranaje", "3. Promoción", "Automatizada"),
             ("az-region", "4. Operación", "En Brazil South")]
    xs = [110, 290, 470, 650]
    for (ic, n, d), x in zip(pasos, xs):
        f.nodo(ic, x, 48, 26, n, d)
    for a, b in zip(xs, xs[1:]):
        f.linea([(a + 50, 48), (b - 50, 48)])
    f.ficha(470, 104, "2 pruebas al año")
    # regiones y réplicas
    serv = [("az-postgres", "PostgreSQL", "Transaccional", "Réplica asíncrona"),
            ("az-postgres", "PostgreSQL", "Series", "Réplica asíncrona"),
            ("az-eventhubs", "Event Hubs", None, ["Réplica geográfica,", "≤ 10 min"]),
            ("az-storage", "Blob inmutable", None, "Replicación de objetos"),
            ("az-aks", "AKS y Key Vault", None, "Mismo código")]
    xs = [138, 250, 362, 474, 586]
    f.grupo_az(82, 130, 560, 88, "Azure Chile Central", "az-region", sub="Región primaria")
    f.grupo_az(82, 278, 560, 92, "Azure Brazil South", "az-region", sub="En espera, RTO 4 h, RPO 15 min")
    for (ic, n, d, rot), x in zip(serv, xs):
        f.nodo(ic, x, 170, 26, n, d)
        f.nodo(ic, x, 318, 26, n, d)
        f.linea([(x, 218), (x, 278)], disc=True)
        f.rotulo(x, 246 if isinstance(rot, str) else 241, rot)
    # vuelta a Chile Central, con conciliación
    f.linea([(82, 330), (46, 330), (46, 258)], disc=True, flecha=None)
    f.linea([(46, 242), (46, 176), (82, 176)], disc=True)
    f.ficha(46, 250, "Conciliación")
    # sin redundancia geográfica: la pareja de Brazil South no se usa
    f.icono("az-region", 682, 312, 22)
    f.crudo('<path d="M669,299 L695,325 M695,299 L669,325" stroke="#2B2B2B" stroke-width="1.6"/>')
    f.texto(682, 336, "South Central", 9, anc="middle")
    f.texto(682, 346.5, "US", 9, anc="middle")
    f.ficha(682, 368, ["Sin redundancia", "geográfica"])
    # eje de continuidad
    f.grupo(14, 386, 702, 80, "Continuidad si cae el enlace", sub="Eje separado de la recuperación")
    for ic, n, d, x in [("pr-servidor", "San Bernardo", "24 h sin enlace", 160),
                        ("pr-pc-industrial", "Terminales", "24 h sin enlace", 366),
                        ("flu-camion", "Camiones", "Búfer de 288 h", 572)]:
        f.nodo(ic, x, 420, 26, n, d)
    f.linea([(572, 407), (572, 370)], disc=True)
    f.rotulo(572, 381, "Reenvío de 72 h")
    return f.guardar()


FIGURAS = [fisica_general, region_primaria, equipo_a_bordo, ambientes, reconexion, sala_san_bernardo,
           gabinete_terminal, recuperacion]
