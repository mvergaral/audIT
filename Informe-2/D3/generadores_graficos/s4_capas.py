"""Adaptación de LogicaCapas de D4 (9fb9d19): cuatro perfiles móviles y autonomía exigida.
Se preservan distribución, iconos y estilo; la fuente D4 permanece intacta.
"""
from comun import Figura, ancho, GRIS_CLARO
from s4_logica import panel_tec, contexto, DECIDE

def logica_capas():
    f = Figura("LogicaCapas", "H")
    LX, LW = 8, 126
    SX0, SX1 = 142, 452
    filas = {"L1": (50, 98), "L2": (106, 126), "L3": (134, 154), "L4": (162, 364), "L5": (372, 418),
             "L6": (426, 470)}
    # personas, cada una unida a su canal
    canales = {"portal": 194, "app": 298, "vistas": 400}
    personas = [("rol-operador", "Operador de torre", 54, ["portal", "app"]), ("rol-cliente", "Cliente", 150, ["portal"]),
                ("rol-transportista", "Transportista", 246, ["portal", "app"]), ("rol-conductor", "Conductor", 336, ["app"]),
                ("rol-taller", "Terminal y taller", 424, ["app", "vistas"])]
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
                                    ("dev-sqlite", "SQLite", "Modo WAL"), ("pr-memoria", "Búfer", "72 h mín.")],
                                   [(645, 376), (697, 376), (645, 428), (697, 428)]):
        f.icono(ic, x, yy, 18)
        f.texto(x, yy + 19, n, 9, anc="middle")
        f.texto(x, yy + 29.5, d, 9, anc="middle")
    f.linea([(618, 385), (421, 385)], flecha="ambas")
    return f.guardar()

FIGURAS=[logica_capas]
