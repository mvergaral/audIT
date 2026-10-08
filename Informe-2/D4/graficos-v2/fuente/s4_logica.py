"""Subdocumento 4, sección 4.1: figuras lógicas (segunda vuelta).

Contenido tomado del texto de la 4.1, de la 3.2.4, 3.3.1 y 3.4.2 del S3, del
Formulario T-12 y del stack de la sección 4.1.1. Los seis contextos usan sus
nombres canónicos. El origen de cada dato nuevo está en INFORME.md.
"""
from lienzo import Figura, ancho, GRIS_CLARO

C = "04-arquitectura"
CONTEXTOS = ["Planificación y tráfico", "Flota y activos", "Personas y cumplimiento",
             "Telemetría y geocercas", "Operación de fletes", "Liquidación y costeo"]
PARTIDOS = {"Planificación y tráfico": ["Planificación", "y tráfico"],
            "Flota y activos": ["Flota", "y activos"],
            "Personas y cumplimiento": ["Personas y", "cumplimiento"],
            "Telemetría y geocercas": ["Telemetría", "y geocercas"],
            "Operación de fletes": ["Operación", "de fletes"],
            "Liquidación y costeo": ["Liquidación", "y costeo"]}
# Lo que decide cada contexto (S3 3.3.1 y T-12)
DECIDE = {"Planificación y tráfico": [["Asignación con", "verificación"], "Retorno con carga"],
          "Flota y activos": ["Aptitud del equipo", "Mantención por km", ["Semirremolque", "acoplado"]],
          "Personas y cumplimiento": ["Jornada y evidencia", "Habilitaciones", "Consentimientos"],
          "Telemetría y geocercas": ["Vista única de flota", "Llegada y salida"],
          "Operación de fletes": [["Documento de", "transporte"], ["Conformidad", "de entrega"], "Carga peligrosa"],
          "Liquidación y costeo": ["Costo por viaje", ["Liquidación a", "transportistas"]]}
PREGUNTA = {"Planificación y tráfico": "¿Qué carga y hacia dónde?",
            "Flota y activos": "¿Puede salir el equipo hoy?",
            "Personas y cumplimiento": "¿Puede conducir hoy?",
            "Telemetría y geocercas": "¿Dónde está y cuándo llegó?",
            "Operación de fletes": "¿Qué viaje ocurrió?",
            "Liquidación y costeo": "¿Cuánto costó y a quién se paga?"}


def panel_tec(f, x, y, w, h, titulo, iconos, filas=1):
    """Panel de tecnologías de una capa, como la columna izquierda del ejemplo."""
    f.grupo(x, y, w, h, titulo, rx=6)
    if not iconos:
        return
    por_fila = -(-len(iconos) // filas)
    for i, (ic, nombre) in enumerate(iconos):
        fila, col = divmod(i, por_fila)
        n = min(por_fila, len(iconos) - fila * por_fila)
        cx = x + w * (col + 0.5) / n
        cy = y + 25 + fila * 30
        f.icono(ic, cx, cy, 16)
        f.texto(cx, cy + 16.5, nombre, 9, anc="middle")


def contexto(f, x, y, w, h, nombre, fichas, pregunta=False):
    f.rect(x, y, w, h, rx=5)
    lineas = PARTIDOS[nombre] if ancho(nombre, 10) > w - 10 else [nombre]
    for j, l in enumerate(lineas):
        f.texto(x + w / 2, y + 13 + j * 11.5, l, 10, anc="middle")
    yy = y + 13 + len(lineas) * 11.5
    for s in fichas:
        n = len(s) if isinstance(s, list) else 1
        hh = 14 + (n - 1) * 10.6
        f.ficha(x + w / 2, yy + hh / 2, s, w=w - 8)
        yy += hh + 3
    return yy


def logica_capas():
    f = Figura("LogicaCapas", C, "H")
    LX, LW = 8, 126
    SX0, SX1 = 142, 452
    filas = {"L1": (50, 98), "L2": (106, 126), "L3": (134, 154), "L4": (162, 364), "L5": (372, 418),
             "L6": (426, 470)}
    # personas, cada una unida a su canal
    canales = {"portal": 194, "app": 298, "vistas": 400}
    personas = [("rol-operador", "Operador de torre", 54, ["portal"]), ("rol-cliente", "Cliente", 150, ["portal"]),
                ("rol-transportista", "Transportista", 246, ["portal", "app"]), ("rol-conductor", "Conductor", 336, ["app"]),
                ("rol-taller", "Terminal y taller", 424, ["vistas"])]
    for ic, n, x, destinos in personas:
        f.icono(ic, x, 13, 20)
        f.texto(x, 35, n, 10, anc="middle")
        for d in destinos:
            dx = 0 if len(destinos) == 1 else (-6 if d == "portal" else 6)
            yj = 44 if d != "vistas" else 44
            f.linea([(x + dx, 38), (x + dx, yj), (canales[d], yj), (canales[d], 50)])
    # columna izquierda: capa y tecnologías
    panel_tec(f, LX, 50, LW, 48, "Presentación",
              [("dev-flutter", "Flutter"), ("dev-react", "React"), ("dev-nextjs", "Next.js")])
    f.grupo(LX, 106, LW, 48, "Borde y puerta", rx=6)
    for (ic, n), yy in zip([("az-frontdoor", "Front Door"), ("az-apim", "API Management")], (128, 144)):
        f.icono(ic, LX + 18, yy, 13)
        f.texto(LX + 30, yy + 3.2, n, 9)
    panel_tec(f, LX, 162, LW, 202, "Servicios", [("dev-dotnet", ".NET"), ("dev-go", "Go"), ("az-aks", "AKS")])
    panel_tec(f, LX, 372, LW, 46, "Integración", [("az-iothub", "IoT Hub"), ("az-eventhubs", "Event Hubs")])
    panel_tec(f, LX, 426, LW, 44, "Datos", [("dev-postgresql", "PostgreSQL"), ("si-timescale", "TimescaleDB")])
    # presentación
    f.grupo(SX0, 50, SX1 - SX0, 48, None)
    for (ic, n), x in zip([("flu-portal", "Portal web"), ("flu-movil", "App móvil"),
                           ("flu-consola", ["Vistas de portería", "y taller"])], canales.values()):
        f.nodo(ic, x, 61, 14, n)
    # borde y puerta de enlace
    cx = (SX0 + SX1) / 2
    f.grupo(SX0, 106, SX1 - SX0, 20, None, rx=4)
    f.icono("az-frontdoor", cx - 62, 116, 14)
    f.texto(cx - 50, 120, "Front Door Premium", 10)
    f.grupo(SX0, 134, SX1 - SX0, 20, None, rx=4)
    f.icono("az-apim", cx - 52, 144, 14)
    f.texto(cx - 40, 148, "API Management", 10)
    # seis contextos con lo que decide cada uno
    f.grupo(SX0, 162, SX1 - SX0, 202, None)
    w = (SX1 - SX0 - 16) / 3
    orden = [["Planificación y tráfico", "Operación de fletes", "Personas y cumplimiento"],
             ["Telemetría y geocercas", "Flota y activos", "Liquidación y costeo"]]
    y = 166
    for fila, h in zip(orden, (100, 90)):
        for i, n in enumerate(fila):
            contexto(f, SX0 + 4 + i * (w + 4), y, w, h, n, DECIDE[n])
        y += h + 4
    # integración y eventos
    f.grupo(SX0, 372, SX1 - SX0, 46, None)
    for i, (ic, n) in enumerate([("pr-adaptador", ["Capa", "anticorrupción"]), ("pr-cola", ["Mensajes", "fallidos"]),
                                 ("az-eventhubs", "Event Hubs"), ("az-iothub", "IoT Hub")]):
        f.nodo(ic, SX0 + (SX1 - SX0) * (i + 0.5) / 4, 385, 16, n, "Protocolo Kafka" if ic == "az-eventhubs" else None)
    # datos
    f.grupo(SX0, 426, SX1 - SX0, 44, None)
    for i, (ic, n) in enumerate([("az-postgres", "Transaccional"), ("az-postgres", ["Series", "de tiempo"]),
                                 ("az-redis", "Caché"), ("az-storage", "Inmutable"), ("az-datalake", "Lakehouse")]):
        f.nodo(ic, SX0 + 8 + (SX1 - SX0 - 16) * (i + 0.5) / 5, 436, 14, n)
    # la petición baja y la respuesta sube por el mismo camino
    for a_, b_ in [(98, 106), (126, 134), (154, 162), (364, 372), (418, 426)]:
        f.linea([(cx + 104, a_), (cx + 104, b_)])
        f.linea([(cx + 114, b_), (cx + 114, a_)])

    # bandas transversales
    f.grupo(458, 50, 62, 420, "Seguridad")
    f.nodo("entra-id", 489, 104, 24, "Entra ID")
    f.nodo("az-keyvault", 489, 176, 24, "Key Vault")
    f.grupo(526, 50, 86, 420, "Observabilidad")
    f.nodo("az-monitor", 569, 104, 24, ["Azure", "Monitor"], ["Trazas,", "métricas y", "registros"])

    # servicios externos, unidos a la capa de integración
    f.grupo(618, 50, 104, 288, "Servicios externos")
    externos = [("flu-gestion2013", ["Sistema de", "gestión de", "transporte 2013"]),
                ("flu-contable", ["Sistema contable", "y de facturación"]),
                ("pr-rastreador", ["Plataformas", "de terceros"]), ("flu-fabrica", ["Telemetría", "de fábrica"]),
                ("flu-edificio-publico", ["Autoridad", "tributaria"]), ("flu-edificio-publico", ["Dirección", "del Trabajo"]),
                ("flu-edificio-publico", ["Aduana"]), ("flu-combustible", ["Estaciones de", "servicio y peajes"])]
    y = 80
    for ic, n in externos:
        alto = max(16, 10.4 * len(n))
        yc = y + alto / 2
        f.icono(ic, 634, yc, 16)
        for j, l in enumerate(n):
            f.texto(647, yc + 3.2 + (j - (len(n) - 1) / 2) * 10.4, l, 9)
        y += alto + 9
    f.linea([(618, 320), (615, 320), (615, 405), (452, 405)], flecha="ambas")
    # el camión, con su versión reducida de servicios y datos, unido a IoT Hub
    f.grupo(618, 344, 104, 126, "Camión")
    for (ic, n, d), (x, yy) in zip([("pr-g26i", "iWave G26I", "Linux"), ("pr-servicio", "Geocercas", "Motor"),
                                    ("dev-sqlite", "SQLite", "Modo WAL"), ("pr-memoria", "Búfer", "288 h")],
                                   [(645, 376), (697, 376), (645, 428), (697, 428)]):
        f.icono(ic, x, yy, 18)
        f.texto(x, yy + 19, n, 9, anc="middle")
        f.texto(x, yy + 29.5, d, 9, anc="middle")
    f.linea([(618, 385), (421, 385)], flecha="ambas")
    return f.guardar()


PREGUNTA_LINEAS = {"Planificación y tráfico": ["¿Qué carga", "y hacia dónde?"],
                   "Flota y activos": ["¿Puede salir", "el equipo hoy?"],
                   "Personas y cumplimiento": ["¿Puede conducir", "hoy?"],
                   "Telemetría y geocercas": ["¿Dónde está y", "cuándo llegó?"],
                   "Operación de fletes": ["¿Qué viaje", "ocurrió?"],
                   "Liquidación y costeo": ["¿Cuánto costó y", "a quién se paga?"]}


def logica_contextos():
    f = Figura("LogicaContextos", C, "V", alto=408)
    w, h = 100, 98
    xs = [8, 158, 308]
    filas = [(14, ["Personas y cumplimiento", "Planificación y tráfico", "Flota y activos"]),
             (176, ["Telemetría y geocercas", "Operación de fletes", "Liquidación y costeo"])]
    for y, nombres in filas:
        for x, n in zip(xs, nombres):
            f.rect(x, y, w, h, rx=6)
            for j, l in enumerate(PARTIDOS[n]):
                f.texto(x + w / 2, y + 15 + j * 12, l, 10, anc="middle")
            f.ficha(x + w / 2, y + 51, PREGUNTA_LINEAS[n], w=w - 10)
            f.icono("az-postgres", x + w / 2, y + h - 15, 18)
    # Planificación y tráfico pregunta a Personas y a Flota
    f.linea([(158, 44), (108, 44)])
    f.rotulo(133, 47, "pregunta")
    f.linea([(258, 44), (308, 44)])
    f.rotulo(283, 47, "pregunta")
    # eventos entre contextos, los mismos del modelo táctico
    f.linea([(208, 112), (208, 176)], disc=True)
    f.rotulo(208, 155, "Viaje asignado")
    f.linea([(58, 176), (58, 130), (346, 130), (346, 112)], disc=True)
    f.rotulo(120, 133, "Semirremolque acoplado")
    f.linea([(108, 222), (158, 222)], disc=True)
    f.rotulo(133, 219, ["Llegada", "y salida"])
    f.linea([(258, 222), (308, 222)], disc=True)
    f.rotulo(283, 219, ["Viaje", "cerrado"])
    # fuentes de terreno de la telemetría
    f.nodo("pr-rastreador", 32, 330, 22, ["Plataformas", "de terceros"])
    f.nodo("flu-fabrica", 98, 330, 22, ["Telemetría", "de fábrica"])
    f.linea([(32, 319), (32, 274)])
    f.linea([(98, 319), (98, 274)])
    f.rotulo(98, 298, "Solo lectura")
    # capa anticorrupción y sistemas que se conservan
    f.grupo(158, 292, 250, 24, None, rx=4)
    f.icono("pr-adaptador", 174, 304, 14)
    f.texto(290, 308, "Capa anticorrupción", 10, anc="middle")
    for x in (208, 358):
        f.linea([(x, 274), (x, 292)], flecha="ambas")
    f.nodo("flu-gestion2013", 208, 348, 24, ["Sistema de gestión", "de transporte 2013"], "Se sustituye por funciones")
    f.nodo("flu-contable", 358, 348, 24, ["Sistema contable", "y de facturación"], "Único emisor")
    f.linea([(208, 316), (208, 336)], flecha="ambas")
    f.linea([(358, 316), (358, 336)], flecha="ambas")
    return f.guardar()


def resiliencia():
    f = Figura("D3-diagrama11_patrones_resiliencia_despacho", C, "V", alto=556)
    cx = 180
    f.nodo("rol-operador", cx, 22, 24, "Operador de torre")
    f.linea([(cx, 50), (cx, 73)])
    f.nodo("az-apim", cx, 86, 26, "API Management", "Contrato de entrada")
    f.marcador(cx + 22, 74, 1)
    f.linea([(cx, 124), (cx, 153)])
    # mamparo de la verificación bloqueante
    f.grupo(56, 136, 236, 262, "Mamparo")
    f.nodo("pr-servicio", cx, 166, 26, ["Servicio de", "verificación"])
    f.nodo("az-redis", 106, 166, 24, ["Caché en", "memoria"], "Clave: 10 ms")
    f.marcador(126, 152, 2)
    f.linea([(167, 166), (118, 166)])
    # tres invariantes en paralelo, con sus datos desde la caché
    xs = [112, 180, 252]
    f.linea([(cx, 206), (cx, 226)], flecha=None)
    f.linea([(xs[0], 226), (xs[2], 226)], flecha=None)
    for x in xs:
        f.linea([(x, 226), (x, 241)])
    f.nodo("rol-conductor", xs[0], 254, 24, "Conductor")
    f.nodo("pr-tracto", xs[1], 254, 26, "Tractocamión")
    f.marcador(xs[1] + 22, 242, 3)
    f.nodo("pr-semirremolque", xs[2], 254, 26, ["Semirremolque y", "carga peligrosa"])
    for x in xs:
        f.linea([(x, 290 if x != xs[2] else 300), (x, 308)], flecha=None)
    f.linea([(xs[0], 308), (xs[2], 308)], flecha=None)
    f.rotulo(146, 311, "En paralelo: 450 ms")
    f.linea([(cx, 308), (cx, 327)])
    f.nodo("az-postgres", cx, 340, 26, "Motor transaccional", "Persistencia: 200 ms")
    f.marcador(cx + 22, 328, 4)
    f.linea([(167, 340), (66, 340), (66, 172), (94, 172)], disc=True)
    f.rotulo(66, 262, "Respaldo")
    f.ficha(174, 388, "Hilos y conexiones propios")
    # rechazo: documento de error que vuelve al operador
    f.linea([(252, 308), (298, 308), (298, 62), (345, 62)])
    f.nodo("flu-documento", 356, 62, 22, "Rechazo")
    f.ficha(356, 100, ["Error estructurado", "< 1 s"])
    f.linea([(356, 51), (356, 22), (193, 22)])
    # efectos fuera del camino bloqueante
    f.linea([(cx, 398), (cx, 416)])
    f.nodo("az-eventhubs", cx, 430, 26, "Bus transaccional", "Fuera del camino bloqueante")
    f.marcador(cx + 22, 418, 5)
    # cortacircuito hacia las integraciones externas
    f.grupo(304, 148, 112, 318, "Externos")
    f.nodo("pr-cortacircuito", 356, 180, 24, "Cortacircuito")
    f.ficha(356, 222, ["Abre con más", "de la mitad de", "10 fallidas · 30 s"], w=88)
    f.linea([(193, 166), (316, 166), (316, 180), (344, 180)])
    f.nodo("pr-adaptador", 356, 284, 24, ["Capa", "anticorrupción"])
    f.linea([(368, 180), (404, 180), (404, 284), (368, 284)])
    f.rotulo(404, 254, "10 s")
    f.nodo("flu-contable", 356, 356, 22, ["Sistema", "contable"])
    f.linea([(344, 284), (316, 284), (316, 356), (345, 356)])
    f.nodo("flu-edificio-publico", 356, 426, 22, ["Autoridad", "tributaria"])
    f.linea([(367, 356), (400, 356), (400, 426), (367, 426)])
    f.rotulo(400, 386, ["Emisión", "90 s"])
    # presupuesto de tiempo, en proporción hasta 2 s, y el tope de 30 s
    x0, x2, yb = 30, 330, 514
    def xs_(ms):
        return x0 + (x2 - x0) * ms / 2000
    for a_, b_, c in [(0, 10, "#9B9B9B"), (10, 460, "#C8C8C8"), (460, 660, GRIS_CLARO)]:
        f.rect(xs_(a_), yb - 7, xs_(b_) - xs_(a_), 14, relleno=c, borde="#404040", grosor=0.5)
    f.linea([(x0, yb), (396, yb)], flecha=None, saltos=False)
    f.texto(xs_(235), yb - 12, "450 ms", 9, anc="middle")
    f.texto(xs_(560), yb - 12, "200 ms", 9, anc="middle")
    f.texto(x0, yb + 22, "10 ms", 9)
    f.linea([(x2, yb - 12), (x2, yb + 12)], flecha=None, saltos=False)
    f.texto(x2, yb + 22, "< 2 s", 9, anc="middle")
    f.crudo(f'<path d="M357,{yb - 6} l-5,12 M363,{yb - 6} l-5,12" stroke="#2B2B2B" stroke-width="1"/>')
    f.linea([(396, yb - 12), (396, yb + 12)], flecha=None, saltos=False)
    f.texto(396, yb + 22, "30 s", 9, anc="end")
    return f.guardar()


def integraciones():
    f = Figura("LogicaIntegraciones", C, "H")
    # plataforma al centro
    f.grupo(240, 168, 280, 124, "Plataforma audIT")
    f.nodo("az-apim", 310, 222, 28, "API Management")
    f.nodo("az-iothub", 390, 222, 28, "IoT Hub")
    f.nodo("az-eventhubs", 466, 222, 28, "Event Hubs")
    # sistemas internos a la izquierda, detrás de la capa anticorrupción
    f.grupo(14, 120, 136, 214, "Sistemas internos")
    f.nodo("flu-gestion2013", 82, 166, 26, ["Sistema de gestión", "de transporte 2013"], "Se sustituye por funciones")
    f.nodo("flu-contable", 82, 262, 26, ["Sistema contable", "y de facturación"], "Único emisor")
    f.linea([(150, 190), (240, 190)], flecha="ambas")
    f.rotulo(195, 193, ["Capa", "anticorrupción"])
    f.linea([(150, 262), (240, 262)], flecha="ambas")
    f.ficha(195, 262, ["Asíncrono", "96.000 viajes/año"])
    f.nodo("flu-edificio-publico", 82, 404, 26, ["Autoridad", "tributaria"])
    f.linea([(82, 334), (82, 390)], flecha="ambas")
    f.ficha(82, 360, ["128.000", "documentos/año"])
    # contrapartes en línea, arriba
    f.grupo(240, 10, 280, 112, "Contrapartes en línea")
    f.nodo("flu-empresa", 300, 56, 26, "Clientes")
    f.nodo("flu-edificio-publico", 390, 56, 26, "Aduana")
    f.nodo("flu-edificio-publico", 470, 56, 26, ["Dirección", "del Trabajo"])
    for x in (300, 390):
        f.linea([(x, 122), (x, 136), (345, 136)], flecha=None)
    f.linea([(345, 136), (345, 168)], flecha="ambas")
    f.ficha(345, 148, "Síncrono y asíncrono")
    f.linea([(470, 122), (470, 168)], flecha="ambas")
    # contrapartes por lotes, a la derecha
    f.grupo(610, 150, 106, 160, "Por lotes")
    f.nodo("flu-combustible", 663, 196, 26, ["Estaciones", "de servicio"])
    f.nodo("flu-peaje", 663, 268, 26, "Peajes")
    f.linea([(650, 196), (520, 196)], disc=True)
    f.ficha(565, 196, ["Lotes · 74.000/año", "hasta 40 días"])
    f.linea([(650, 268), (520, 268)], disc=True)
    f.ficha(565, 268, ["Lotes", "620.000/año"])
    # fuentes de terreno, abajo
    f.grupo(240, 350, 330, 116, "Terreno")
    fuentes = [("pr-g26i", ["Equipos audIT"], "182 camiones", 302, None, 0),
               ("pr-rastreador", ["Plataformas", "de terceros"], "192 camiones", 380,
                ["Asíncrono", "solo consulta"], 312),
               ("flu-fabrica", ["Telemetría", "de fábrica"], "61 tractocamiones", 464,
                ["Asíncrono · 61", "solo lectura"], 330),
               ("pr-ble", ["Portería", "y terminal"], None, 538, None, 0)]
    for ic, n, d, x, ficha, yf in fuentes:
        f.nodo(ic, x, 394, 26, n, d)
        if x < 520:
            f.linea([(x, 381), (x, 292)], flecha="ambas" if x == 302 else "fin")
        else:
            f.linea([(x, 381), (x, 336), (506, 336), (506, 292)])
        if ficha:
            f.ficha(x, yf, ficha)
    return f.guardar()


def acl():
    f = Figura("D3-diagrama12_integracion_acl_erp2013", C, "H")
    # contextos a la izquierda
    f.grupo(14, 20, 136, 238, "Contextos")
    for i, c in enumerate(CONTEXTOS):
        f.caja(22, 42 + i * 35, 120, 29, [c] if ancho(c, 9) < 110 else PARTIDOS[c], tam=9, rx=4, alto_linea=10.6)
    f.linea([(150, 104), (248, 104)])
    f.rotulo(182, 96, ["Viaje cerrado,", "liquidación", "aprobada"])
    # capa anticorrupción: cuatro piezas en cadena
    f.grupo(214, 20, 330, 238, "Capa anticorrupción")
    f.nodo("pr-adaptador", 262, 104, 26, ["Adaptador", "de dominio"])
    f.nodo("pr-transformador", 362, 104, 26, ["Transformador", "de esquemas"])
    f.linea([(275, 104), (349, 104)])
    f.icono("pr-cortacircuito", 450, 104, 24)
    f.icono("pr-cola", 486, 104, 24)
    f.texto(468, 128, "Protector de", 10, anc="middle")
    f.texto(468, 140, "resiliencia", 10, anc="middle")
    f.texto(468, 151, "Cortacircuito y cola", 9, anc="middle")
    f.linea([(375, 104), (438, 104)])
    f.nodo("pr-reconciliador", 380, 196, 26, "Reconciliador", "Expone lo pendiente")
    f.linea([(393, 196), (520, 196), (520, 112), (498, 112)], disc=True)
    f.rotulo(468, 199, "Vigila la cola")
    # sistemas que se conservan o se sustituyen
    f.nodo("flu-gestion2013", 640, 44, 26, ["Sistema de gestión", "de transporte 2013"])
    f.linea([(544, 40), (627, 40)], flecha="ambas")
    f.nodo("flu-contable", 640, 132, 26, ["Sistema contable", "y de facturación"], "Único emisor")
    f.linea([(498, 98), (580, 98), (580, 126), (627, 126)])
    f.rotulo(580, 112, ["Eventos", "traducidos"])
    f.nodo("flu-edificio-publico", 640, 220, 24, ["Autoridad", "tributaria"])
    f.linea([(653, 132), (690, 132), (690, 220), (652, 220)])
    f.rotulo(690, 176, "Emite")
    # la confirmación vuelve traducida a los contextos
    f.linea([(627, 138), (596, 138), (596, 240), (200, 240), (200, 170), (150, 170)])
    f.rotulo(330, 243, "Confirmación traducida")
    # sustitución del sistema de 2013, función por función
    f.grupo(14, 268, 702, 198, "Retiro del sistema de 2013 función por función")
    x16, x21, x24 = 240, 500, 650
    f.linea([(60, 306), (700, 306)], flecha=None, saltos=False)
    for x, m in ((x16, 16), (x21, 21), (x24, 24)):
        f.linea([(x, 300), (x, 312)], flecha=None, saltos=False)
        f.texto(x, 297, f"Mes {m}", 9, 600, "middle")
    f.rect(x21, 303, x24 - x21, 6, relleno=GRIS_CLARO, borde="#9B9B9B", grosor=0.5)
    f.rotulo((x21 + x24) / 2, 309, "Solo lectura")

    def par(x, y, funcion, contexto_):
        n = len(funcion) if isinstance(funcion, list) else 1
        hh = 14 + (n - 1) * 10.6
        f.ficha(x, y + hh / 2, funcion)
        f.linea([(x, y + hh), (x, y + hh + 10)])
        f.ficha(x, y + hh + 17, contexto_, peso=600)
        return y + hh + 24 + 5

    y = 322
    for fun, ctx in [("Asignación de viajes", "Planificación y tráfico"), ("Control de viajes", "Operación de fletes"),
                     (["Base de la liquidación y", "tarifas de transportistas"], "Liquidación y costeo")]:
        y = par(x16, y, fun, ctx)
    y = 322
    for fun, ctx in [("Órdenes de transporte", "Planificación y tráfico"), ("Tarifas a clientes", "Liquidación y costeo"),
                     ("Consulta histórica", "Repositorio analítico")]:
        y = par(x21, y, fun, ctx)
    f.ficha(x24, 338, ["Retiro del", "sistema de 2013"])
    return f.guardar()


def analitica():
    f = Figura("D3-diagrama13_arquitectura_analitica_lakehouse_bi", C, "H")
    # fuentes
    f.grupo(14, 20, 102, 380, "Fuentes")
    f.nodo("az-postgres", 65, 70, 26, ["Motor", "transaccional"])
    f.nodo("az-eventhubs", 65, 196, 26, "Telemetría")
    f.ficha(65, 232, "Posición: 2 min")
    f.nodo("flu-documento", 65, 318, 26, ["Archivos de", "combustible", "y peaje"])
    # la captura de cambios lee la bitácora, no las tablas
    f.linea([(78, 70), (141, 70)])
    f.nodo("flu-bitacora", 152, 70, 22, "Bitácora")
    f.ficha(152, 106, "RT-05.05")
    f.linea([(163, 70), (210, 70)])
    f.rotulo(188, 66, ["Captura", "de cambios"])
    f.linea([(78, 196), (196, 196), (196, 92), (210, 92)])
    f.linea([(78, 318), (202, 318), (202, 106), (210, 106)], disc=True)
    # repositorio en capas
    f.grupo(200, 20, 320, 380, "Repositorio analítico", "az-datalake", sub="Delta Lake en ADLS Gen2")
    capas = [("Cruda", ["Tal como llegó"], 210), ("Depurada", ["Deduplicada", "y validada"], 316),
             ("De negocio", ["Modelo", "dimensional"], 422)]
    for n, d, x in capas:
        f.caja(x, 42, 86, 76, [(n, 10, 600)] + [(l, 9, 400) for l in d], rx=6)
    f.linea([(296, 80), (316, 80)])
    f.linea([(402, 80), (422, 80)])
    f.ficha(486, 138, ["Emisiones:", "mensual"])
    # costo por viaje: flota propia y subcontratada (tabla 4-costo)
    f.linea([(440, 118), (440, 158)])
    f.grupo(208, 158, 304, 234, "Costo por viaje")
    f.texto(354, 194, "Flota propia", 9, 600, "middle")
    f.texto(460, 194, "Flota subcontratada", 9, 600, "middle")
    filas = [("flu-combustible", "Combustible", "Medido por telemetría", "No observable"),
             ("flu-peaje", "Peajes", "Pasada efectiva", "Igual, si lo asume"),
             ("rol-conductor", "Conductor", "Jornada imputada", "En la tarifa pactada"),
             ("rol-taller", "Mantenimiento", "Cuota por km", "No observable"),
             ("flu-reloj", "Sobreestadía", "Horas por geocerca", "Igual"),
             ("rol-transportista", ["Tarifa a", "terceros"], "No aplica", "Costo directo"),
             ("pr-medidor", "Kilómetro", "Odómetro telemático", "Traza de posición")]
    y = 212
    for ic, n, a_, b_ in filas:
        f.icono(ic, 222, y, 15)
        nl = n if isinstance(n, list) else [n]
        for j, l in enumerate(nl):
            f.texto(234, y + 3.2 + (j - (len(nl) - 1) / 2) * 10.4, l, 9)
        f.ficha(354, y, a_, w=100)
        f.ficha(460, y, b_, w=100)
        y += 19 if len(nl) == 1 else 24
    f.ficha(300, 370, "Preliminar: 24 h")
    f.ficha(430, 370, ["Definitiva: con", "combustible y peajes"])
    # explotación
    f.grupo(530, 20, 192, 380, "Explotación")
    herramientas = [("flu-tablero", "Tableros", None, 584, 70), ("flu-autoservicio", "Autoservicio", None, 668, 70),
                    ("flu-repuestos", "Exportación", "Formatos abiertos", 584, 156),
                    ("flu-reloj", ["Envío", "programado"], "Por calendario", 668, 156)]
    for ic, n, d, x, yy in herramientas:
        f.nodo(ic, x, yy, 24, n, d)
    f.linea([(508, 60), (530, 60)])
    f.ficha(626, 214, "RT-05.28")
    f.linea([(626, 222), (626, 252)], flecha=None)
    f.linea([(562, 252), (690, 252)], flecha=None)
    for x, ic, n in [(562, "rol-gerencia", "Gerencia"), (626, "rol-finanzas", "Finanzas"),
                     (690, "rol-operaciones", "Operaciones")]:
        f.linea([(x, 252), (x, 272)])
        f.nodo(ic, x, 284, 22, n)
    return f.guardar()


def tactico():
    f = Figura("D3-diagrama2_arquitectura_tactica_ddd", C, "V", alto=560)
    L, R, w = 8, 248, 166
    filas = [8, 186, 364]

    def contexto_(x, y, n):
        f.grupo(x, y, w, 136, n, discontinuo=True, borde="#404040")

    def caja(x, y, nombre, miembros=(), raiz=False):
        ww = w - 20
        hh = 22 + 11 * len(miembros)
        f.rect(x, y, ww, hh, rx=4)
        f.texto(x + 8, y + 15, nombre, 10, 600)
        if raiz:
            f.icono("flu-corona", x + ww - 12, y + 11, 12)
        else:
            f.texto(x + ww - 6, y + 15, "entidad", 9, anc="end")
        for i, (m, tipo) in enumerate(miembros):
            f.texto(x + 8, y + 27 + i * 11, f"{m}, {tipo}", 9)
        return y + hh

    def caja2(x, y, lineas):
        ww = w - 20
        hh = 14 + 11.5 * len(lineas)
        f.rect(x, y, ww, hh, rx=4)
        for i, l in enumerate(lineas):
            f.texto(x + 8, y + 15 + i * 11.5, l, 10, 600)
        f.texto(x + ww - 6, y + 15, "entidad", 9, anc="end")

    contexto_(L, filas[0], "Planificación y tráfico")
    caja(L + 10, filas[0] + 30, "Orden de transporte")
    caja(L + 10, filas[0] + 60, "Asignación")
    contexto_(R, filas[0], "Flota y activos")
    caja(R + 10, filas[0] + 26, "Tractocamión", [("Vigencia", "entidad")], raiz=True)
    caja(R + 10, filas[0] + 72, "Semirremolque", [("Vigencia", "entidad")], raiz=True)
    contexto_(L, filas[1], "Operación de fletes")
    caja(L + 10, filas[1] + 30, "Viaje", [("Sobreestadía", "entidad"), ("Gasto operacional", "valor")], raiz=True)
    contexto_(R, filas[1], "Telemetría y geocercas")
    caja(R + 10, filas[1] + 30, "Posición")
    caja2(R + 10, filas[1] + 60, ["Geocerca de", "punto de carga"])
    contexto_(L, filas[2], "Liquidación y costeo")
    caja(L + 10, filas[2] + 30, "Costo del viaje")
    caja2(L + 10, filas[2] + 60, ["Liquidación del", "transportista"])
    contexto_(R, filas[2], "Personas y cumplimiento")
    caja(R + 10, filas[2] + 30, "Conductor",
         [("Vigencia", "entidad"), ("Jornada del conductor", "entidad"), ("Consentimiento de datos", "valor")], raiz=True)

    # eventos de dominio entre contextos
    f.linea([(L + 100, filas[0] + 136), (L + 100, filas[1])], disc=True)
    f.rotulo(L + 100, filas[0] + 160, "Viaje asignado")
    f.linea([(R + 83, filas[1]), (R + 83, filas[0] + 136)], disc=True)
    f.rotulo(R + 83, filas[0] + 160, "Semirremolque acoplado")
    f.linea([(R, filas[1] + 100), (L + w, filas[1] + 100)], disc=True)
    f.rotulo((L + w + R) / 2, filas[1] + 97, ["Llegada y salida", "en un punto"])
    f.linea([(R + 83, filas[2]), (R + 83, filas[1] + 136)], disc=True)
    f.rotulo(R + 83, filas[1] + 160, "Consentimiento revocado")
    f.linea([(L + 40, filas[1] + 136), (L + 40, filas[2])], disc=True)
    f.rotulo(L + 40, filas[1] + 152, ["Viaje", "cerrado"])
    f.linea([(L + 130, filas[1] + 136), (L + 130, filas[2])], disc=True)
    f.rotulo(L + 130, filas[1] + 152, ["Documento", "emitido"])
    # la liquidación aprobada sale hacia la capa anticorrupción
    f.linea([(L + 83, filas[2] + 136), (L + 83, 516)], disc=True)
    f.rotulo(L + 83, filas[2] + 156, "Liquidación aprobada")
    f.nodo("pr-adaptador", L + 83, 530, 24, "Capa anticorrupción")
    return f.guardar()


FIGURAS = [logica_capas, logica_contextos, resiliencia, integraciones, acl, analitica, tactico]
