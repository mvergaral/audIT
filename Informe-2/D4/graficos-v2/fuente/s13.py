"""Subdocumento 13: cartera de innovaciones y semirremolque conectado (segunda vuelta)."""
from lienzo import Figura, ancho, SUBRED

C13 = "13-innovaciones"

INNOVACIONES = [(1, "inn-expediente", ["Expediente verificable", "del transportista"]),
                (2, "az-deviceupdate", ["Programación por", "oportunidad de patio"]),
                (3, "pr-semirremolque", ["Semirremolque", "conectado"]),
                (4, "flu-acuerdo", ["Esquema de adhesión y", "propiedad del dispositivo"]),
                (5, "flu-parador", ["Bienestar del conductor y", "descanso en parador seguro"])]


def nodo_marcado(f, ic, cx, cy, s, nombre, numeros):
    f.nodo(ic, cx, cy, s, nombre)
    x0 = cx + s / 2 + 4
    for i, n in enumerate(numeros):
        f.marcador(x0 + i * 15, cy - s / 2 + 1, n)


def cartera():
    f = Figura("cartera", C13, "V", alto=498)
    # nombres completos de las cinco innovaciones, con su ícono
    for i, (n, ic, nombre) in enumerate(INNOVACIONES):
        col, fila = (0, i) if i < 3 else (1, i - 3)
        x, y = 16 + col * 210, 18 + fila * 30
        f.marcador(x, y, n)
        f.icono(ic, x + 20, y, 18)
        for j, l in enumerate(nombre):
            f.texto(x + 34, y - 2 + j * 11.5, l, 10)
    capas = [("Presentación", 104, [("flu-portal", ["Portal del", "transportista"], [1, 4]),
                                    ("flu-movil", "App móvil", []),
                                    ("flu-consola", ["Vistas de", "portería y taller"], [])]),
             ("Servicios", 182, [("pr-servicio", ["Servicio de", "verificación"], [1]),
                                 ("pr-servicio", ["Planificación", "de patio"], [2]),
                                 ("flu-candado", ["Verificación", "bloqueante"], [3]),
                                 ("flu-documento", "Consentimiento", [4]),
                                 ("flu-parador", ["Gobernanza", "de paradores"], [5])]),
             ("Integración", 260, [("az-iothub", "IoT Hub", []), ("az-deviceupdate", ["Actualización", "remota"], [2]),
                                   ("az-eventhubs", "Event Hubs", [])]),
             ("Borde", 338, [("pr-pc-industrial", "Terminales", [2]), ("pr-ble", "Portería", [3]),
                             ("pr-wifi", ["Patio", "con Wi-Fi"], [])]),
             ("Equipo a bordo", 416, [("pr-g26i", "iWave G26I", [2, 3, 4, 5]), ("pr-servicio", ["Motor de", "geocercas"], []),
                                      ("rol-conductor", ["Alerta de", "jornada"], [])])]
    for titulo, y, nodos in capas:
        f.grupo(8, y, 406, 74, titulo)
        n = len(nodos)
        for i, (ic, nombre, nums) in enumerate(nodos):
            cx = 30 + 376 * (i + 0.5) / n
            nodo_marcado(f, ic, cx, y + 31, 22, nombre, nums)
    return f.guardar()


def semirremolque():
    f = Figura("semirremolque", C13, "H")
    f.grupo(10, 10, 392, 454, "Borde")
    f.grupo(412, 32, 106, 432, "Integración")
    f.grupo(528, 10, 192, 454, "Servicios")

    # ------------------------------------------------ en ruta: la baliza y el G26I que la lee
    f.grupo(20, 32, 372, 260, "En ruta", rx=8)
    g = f.equipo("hw-g26i", 84, 92, w=64)
    f.texto(84, g[3] + 12, "iWave G26I", 10, anc="middle")
    b = f.equipo("hw-baliza", 204, 92, w=32)
    f.texto(204, b[3] + 12, "Baliza EYE Sensor", 10, anc="middle")
    f.linea([(b[0], 92), (g[2], 92)])
    f.rotulo(152, 95, "Bluetooth")
    f.texto(146, 152, "Acople: señal estable y", 9, anc="middle")
    f.texto(146, 162.6, "movimiento junto al camión", 9, anc="middle")
    # tractocamión con el semirremolque acoplado
    f.icono("pr-tracto", 86, 232, 64)
    f.icono("pr-semirremolque", 166, 232, 74)
    f.texto(74, 280, "Tractocamión", 10, anc="middle")
    f.texto(186, 280, "Semirremolque", 10, anc="middle")
    f.linea([(84, g[3] + 16), (84, 196)], flecha=None, grosor=0.6, saltos=False)
    f.rotulo(84, 186, "Cabina")
    f.linea([(204, b[3] + 16), (204, 194)], flecha=None, grosor=0.6, saltos=False)
    f.rotulo(204, 186, "Chasis delantero")
    # lo que trae y mide la baliza, en íconos
    f.grupo(258, 42, 126, 242, "La baliza", rx=6)
    datos = [("flu-termometro", "Temperatura"), ("flu-agua", "Humedad"),
             ("flu-puerta", "Puerta"), ("flu-vibracion", "Acelerómetro"),
             ("flu-bateria", "Batería 5 años"), ("flu-reloj", "Cada 10 s"),
             ("flu-copo", "44 refrigerados"), ("hw-baliza", "210 + 21")]
    for i, (ic, n) in enumerate(datos):
        x, y = 290 + (i % 2) * 64, 80 + (i // 2) * 54
        if ic.startswith("hw-"):
            f.equipo(ic, x, y, w=19)
        else:
            f.icono(ic, x, y, 20)
        f.texto(x, y + 23, n, 9, anc="middle")

    # ------------------------------------------------ portería: el lector registra el que sale
    f.grupo(20, 302, 372, 152, "Portería", rx=8)
    m = f.equipo("hw-minew", 84, 362, w=44)
    f.texto(84, m[3] + 12, "Minew G1", 10, anc="middle")
    f.texto(84, m[3] + 23, "Lector de portería", 9, anc="middle")
    f.nodo("pr-barrera", 200, 360, 30, "Barrera")
    f.icono("pr-tracto", 290, 356, 46)
    f.icono("pr-semirremolque", 346, 356, 54)
    f.texto(330, 394, "Semirremolque que sale", 10, anc="middle")
    f.texto(330, 405.5, "aunque el camión no", 9, anc="middle")
    f.texto(330, 416, "tenga equipo audIT", 9, anc="middle")
    f.linea([(346, 329), (346, 322), (84, 322), (84, m[1])])
    f.rotulo(215, 325, "Bluetooth")

    # ------------------------------------------------ integración: dos redes a IoT Hub
    f.nodo("az-iothub", 465, 156, 26, "IoT Hub")
    f.linea([(84, g[1]), (84, 22), (504, 22), (504, 156), (478, 156)])
    f.rotulo(290, 25, "Red celular")
    f.linea([(m[0], 362), (30, 362), (30, 446), (426, 446), (426, 156), (452, 156)])
    f.rotulo(220, 449, "Red del terminal")
    f.linea([(465, 184), (465, 282)])
    f.nodo("az-eventhubs", 465, 296, 26, "Event Hubs", ["Reparte el", "evento"])

    # ------------------------------------------------ servicios: tres usos del acople
    filas = [(32, 128, "pr-servicio", "Flota y activos", None,
              "flu-llave", ["Kilómetros para el", "plan preventivo"]),
             (170, 128, "flu-candado", "Verificación", "bloqueante",
              "pr-semirremolque", ["Sale el asignado,", "no el declarado"]),
             (308, 146, "pr-servicio", "Telemetría", "y geocercas",
              "si-timescale", ["Series de tiempo", "TimescaleDB"])]
    f.linea([(478, 296), (524, 296)], flecha=None)
    ys = [y + 46 for y, *_ in filas]
    f.linea([(524, ys[0]), (524, ys[-1])], flecha=None)
    for (y, h, ic, n1, n2, ic2, res), yc in zip(filas, ys):
        f.rect(536, y, 176, h, rx=6)
        f.linea([(524, yc), (557, yc)])
        f.nodo(ic, 570, yc, 26, [n1, n2] if n2 else n1)
        f.linea([(583, yc), (644, yc)])
        f.nodo(ic2, 662, yc, 28 if ic2.startswith("si-") else 30, res[0])
        f.texto(662, yc + 15 + 11 + 12 - 0.5, res[1], 9 if ic2.startswith("si-") else 10, anc="middle")
    # lo que guarda la base de series de tiempo
    yt = ys[-1] + 66
    f.icono("flu-termometro", 646, yt, 16)
    f.icono("flu-puerta", 668, yt, 16)
    f.texto(657, yt + 20, "Temperatura y puerta", 9, anc="middle")
    return f.guardar()



def intervenciones():
    """Copia de la figura 13-2-intervenciones de la dupla 3 (generadores_graficos/s13_proceso.py,
    commit f86e240), sin título interno y sin punto y coma. Todo sube 45 puntos y el lienzo se acorta
    en lo mismo, porque el título ya no ocupa la parte de arriba."""
    dy = 45
    f = Figura("intervenciones", "13-innovaciones", "L", alto=473.4 - dy, ancho_pt=729.6)
    pasos = [(122, 65, "1. Observar", "flu-ubicacion", ["ETA y paso por terminal", "Permiso y actualidad"]),
             (365, 65, "2. Preparar", "flu-documento", ["Familia de equipo / kit", "Versión y pruebas previas"]),
             (608, 65, "3. Programar", "pr-servicio", ["Ventana, técnico y stock", "Prioridad + plan manual"]),
             (122, 249, "4. Autorizar", "flu-candado", ["Vehículo detenido en terminal", "Ventana y kit confirmados"]),
             (365, 249, "5. Intervenir", "pr-g26i", ["Configurar / instalar", "Validar antes de liberar"]),
             (608, 249, "6. Aprender", "pr-reconciliador", ["Acta y tiempos reales", "Recalibrar el próximo plan"])]
    for x, y, t, ic, ls in pasos:
        f.grupo(x - 105, y - dy, 210, 122, t, rx=6)
        f.nodo(ic, x, y + 48 - dy, 28, ls)
    for y in (126, 310):
        f.linea([(227, y - dy), (260, y - dy)])
        f.linea([(470, y - dy), (503, y - dy)])
    f.linea([(608, 187 - dy), (608, 216 - dy), (122, 216 - dy), (122, 249 - dy)])
    f.rotulo(365, 211 - dy, "Plan factible → confirmar ventana, y si no existe, reprogramar")
    lineas = ["La instalación por unidad en terminal es obligatoria. El aporte es la planificación dinámica verificable.",
              "Piloto: 10 unidades en M6 y flota propia de M6 a M9. Metas y línea base se miden, sin inventar resultados.",
              "El twin conserva el estado deseado y el reportado. Eventos y actas guardan el historial de cada intervención."]
    y0 = 405 - dy
    f.grupo(14, y0, f.W - 28, 22 + 13 * len(lineas), None, rx=6, relleno=SUBRED)
    for i, t in enumerate(lineas):
        f.texto(24, y0 + 18 + i * 13, t, 9)
    return f.guardar()


FIGURAS = [cartera, semirremolque, intervenciones]
