"""Cartera original de D4 con la innovación de proceso de D3 actualizada."""
from comun import Figura

INNOVACIONES = [
    (1, 'inn-expediente', ['Expediente verificable', 'del transportista']),
    (2, 'az-deviceupdate', ['Programación por', 'oportunidad de patio']),
    (3, 'pr-semirremolque', ['Semirremolque', 'conectado']),
    (4, 'flu-acuerdo', ['Esquema de adhesión y', 'propiedad del dispositivo']),
    (5, 'flu-parador', ['Bienestar del conductor y', 'descanso en parador seguro']),
]

def nodo_marcado(f, icono, cx, cy, s, nombre, numeros):
    f.nodo(icono, cx, cy, s, nombre)
    x0 = cx + s / 2 + 4
    for i, n in enumerate(numeros):
        f.marcador(x0 + i * 15, cy - s / 2 + 1, n)

def figura_13_cartera():
    f = Figura('13-cartera', 'V', alto=498)
    for i, (n, icono, nombre) in enumerate(INNOVACIONES):
        col, fila = (0, i) if i < 3 else (1, i - 3)
        x, y = 16 + col * 210, 18 + fila * 30
        f.marcador(x, y, n)
        f.icono(icono, x + 20, y, 18)
        for j, linea in enumerate(nombre):
            f.texto(x + 34, y - 2 + j * 11.5, linea, 10)
    capas = [
        ('Presentación', 104, [
            ('flu-portal', ['Portal del', 'transportista'], [1, 4]),
            ('flu-movil', 'App móvil', []),
            ('flu-consola', ['Vistas de', 'portería y taller'], []),
        ]),
        ('Servicios', 182, [
            ('pr-servicio', ['Servicio de', 'verificación'], [1]),
            ('pr-servicio', ['Planificación', 'de patio'], [2]),
            ('flu-candado', ['Verificación', 'bloqueante'], [3]),
            ('flu-documento', 'Consentimiento', [4]),
            ('flu-parador', ['Gobernanza', 'de paradores'], [5]),
        ]),
        ('Integración', 260, [
            ('az-iothub', 'IoT Hub', []),
            ('az-deviceupdate', ['Actualización', 'remota'], [2]),
            ('az-eventhubs', 'Event Hubs', []),
        ]),
        ('Borde', 338, [
            ('pr-pc-industrial', 'Terminales', [2]),
            ('pr-ble', 'Portería', [3]),
            ('pr-wifi', ['Patio', 'con Wi-Fi'], []),
        ]),
        ('Equipo a bordo', 416, [
            ('pr-g26i', 'iWave G26I', [2, 3, 4, 5]),
            ('pr-servicio', ['Motor de', 'geocercas'], []),
            ('rol-conductor', ['Alerta de', 'jornada'], []),
        ]),
    ]
    for titulo, y, nodos in capas:
        f.grupo(8, y, 406, 74, titulo)
        for i, (icono, nombre, numeros) in enumerate(nodos):
            cx = 30 + 376 * (i + 0.5) / len(nodos)
            nodo_marcado(f, icono, cx, y + 31, 22, nombre, numeros)
    return f.guardar()

FIGURAS = [figura_13_cartera]
