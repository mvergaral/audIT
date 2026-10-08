"""Subdocumento 13: cartera de innovaciones y semirremolque conectado (segunda vuelta)."""
from lienzo import Figura, ancho

C13 = "13-innovaciones"

INNOVACIONES = [(1, "inn-expediente", ["Expediente verificable", "del transportista"]),
                (2, "az-deviceupdate", ["Despliegue sin detener", "la flota"]),
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
    f.grupo(14, 20, 328, 446, "Borde")
    f.grupo(360, 20, 128, 446, "Integración")
    f.grupo(506, 20, 210, 446, "Servicios")
    # tractocamión con el semirremolque acoplado
    f.nodo("pr-g26i", 84, 82, 22, "iWave G26I")
    f.nodo("pr-baliza", 150, 82, 22, "Baliza")
    f.linea([(139, 82), (96, 82)])
    f.rotulo(118, 85, "Bluetooth")
    f.linea([(84, 108), (84, 150)], flecha=None)
    f.rotulo(84, 130, "Cabina")
    f.linea([(150, 108), (150, 148)], flecha=None)
    f.rotulo(150, 130, "Chasis")
    f.icono("pr-tracto", 92, 172, 46)
    f.icono("pr-semirremolque", 140, 172, 50)
    f.texto(80, 212, "Tractocamión", 10, anc="middle")
    f.texto(160, 226, "Semirremolque", 10, anc="middle")
    for i, s in enumerate(["Temperatura", "Puerta", "Acelerómetro", "44 refrigerados", "210 + 21"]):
        f.ficha(268, 64 + i * 19, s, w=86)
    # portería: barrera y lector
    f.grupo(24, 252, 308, 168, "Portería", rx=8)
    f.nodo("pr-ble", 150, 296, 24, "Minew G1")
    f.nodo("pr-barrera", 150, 356, 34, "Barrera")
    f.nodo("pr-semirremolque", 262, 356, 40, ["Semirremolque", "que sale"])
    f.linea([(262, 336), (262, 296), (162, 296)])
    f.rotulo(214, 299, "Bluetooth")
    # al IoT Hub por dos redes
    f.linea([(84, 71), (84, 40), (424, 40), (424, 167)])
    f.rotulo(250, 43, "Red celular")
    f.linea([(138, 296), (36, 296), (36, 440), (372, 440), (372, 186), (411, 186)])
    f.rotulo(220, 443, "Red del terminal")
    f.nodo("az-iothub", 424, 180, 26, "IoT Hub")
    f.linea([(424, 214), (424, 262)])
    f.nodo("az-eventhubs", 424, 276, 26, "Event Hubs", "Reparte el evento")
    # tres servicios
    f.linea([(437, 276), (494, 276)], flecha=None)
    f.linea([(494, 96), (494, 380)], flecha=None)
    for y in (96, 236, 380):
        f.linea([(494, y), (550, y)])
    f.nodo("pr-servicio", 564, 96, 26, "Flota y activos")
    f.ficha(608, 138, "Kilómetros → plan preventivo")
    f.nodo("flu-candado", 564, 236, 26, ["Verificación", "bloqueante"])
    f.ficha(608, 288, ["Semirremolque que sale", "= asignado"])
    f.nodo("pr-servicio", 564, 380, 26, ["Telemetría", "y geocercas"])
    f.linea([(577, 380), (650, 380)])
    f.nodo("az-postgres", 664, 380, 26, ["Series", "de tiempo"])
    f.ficha(664, 438, "Temperatura y puerta")
    return f.guardar()


FIGURAS = [cartera, semirremolque]
