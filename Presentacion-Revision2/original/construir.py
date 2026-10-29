"""Construye escenas vectoriales, manifiesto y notas sin modificar el informe."""
from pathlib import Path
import csv
import html
import json
import math
import textwrap

BASE = Path(__file__).resolve().parent
ROOT = BASE.parents[1]
OUT = BASE / 'composition'
C = '#006b7d'
WHITE = '#102d3e'
MUTED = '#48606e'
AMBER = '#8a5100'
CORAL = '#a13437'
CARD_BG = '#f4f8fa'
CARD_ALT = '#ffffff'
STROKE = '#c4d3dc'
SLIDES = []


def text(x, y, value, size=42, color=WHITE, weight=400, anchor='start', count_to=None, count_prefix='', count_suffix='', extra=''):
    attrs = ''
    if count_to is not None:
        attrs += f' data-count-to="{count_to}" data-count-prefix="{html.escape(str(count_prefix))}" data-count-suffix="{html.escape(str(count_suffix))}"'
    if extra:
        attrs += f' {extra}'
    return f'<text x="{x}" y="{y}" fill="{color}" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}"{attrs}>{html.escape(str(value))}</text>'


def line(x1, y1, x2, y2, color=C, width=3, dash='', draw=False):
    length = int(math.hypot(x2 - x1, y2 - y1)) + 10
    d_attr = f' data-draw="{length}"' if draw else ''
    dash_attr = f' stroke-dasharray="{dash}"' if dash else ''
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{width}" stroke-linecap="round"{dash_attr}{d_attr}/>'


def circle(x, y, r=12, color=C, fill=None, width=3, pulse=False, slide_from_x=None):
    attrs = ''
    if pulse:
        attrs += ' data-pulse="1"'
    if slide_from_x is not None:
        attrs += f' data-slide-from-x="{slide_from_x}"'
    return f'<circle cx="{x}" cy="{y}" r="{r}" stroke="{color}" stroke-width="{width}" fill="{fill or "#ffffff"}"{attrs}/>'


def card(x, y, w, h, fill=CARD_BG, stroke=STROKE, rx=14, accent=None, accent_top=False):
    out = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="2"/>'
    if accent:
        if accent_top:
            out += f'<rect x="{x}" y="{y}" width="{w}" height="6" rx="3" fill="{accent}"/>'
        else:
            out += f'<rect x="{x}" y="{y}" width="7" height="{h}" rx="3.5" fill="{accent}"/>'
    return out


def badge(x, y, label, color=C, bg='#e7f3f6', w=None, h=40, size=23, weight=600):
    bw = w or max(84, int(len(str(label)) * (size * 0.62) + 34))
    ty = y + int(h * 0.68)
    return (
        f'<rect x="{x}" y="{y}" width="{bw}" height="{h}" rx="{h // 2}" fill="{bg}" stroke="{color}" stroke-width="1.8"/>'
        + text(x + bw / 2, ty, label, size, color, weight, 'middle')
    )


def arrow(x1, y1, x2, y2, color=C, width=3.5, dashed=False, draw=True, flow=False):
    length = int(math.hypot(x2 - x1, y2 - y1)) + 12
    d_attr = f' data-draw="{length}"' if draw and not dashed else ''
    dash_attr = ' stroke-dasharray="9 7"' if dashed else ''
    angle = math.atan2(y2 - y1, x2 - x1)
    hl = 13
    hw = 6.5
    lx2 = x2 - math.cos(angle) * 4
    ly2 = y2 - math.sin(angle) * 4
    p1x = x2
    p1y = y2
    p2x = x2 - hl * math.cos(angle) + hw * math.sin(angle)
    p2y = y2 - hl * math.sin(angle) - hw * math.cos(angle)
    p3x = x2 - hl * math.cos(angle) - hw * math.sin(angle)
    p3y = y2 - hl * math.sin(angle) + hw * math.cos(angle)
    out = (
        f'<line x1="{x1}" y1="{y1}" x2="{lx2:.1f}" y2="{ly2:.1f}" stroke="{color}" stroke-width="{width}" stroke-linecap="round"{dash_attr}{d_attr}/>'
        f'<polygon points="{p1x:.1f},{p1y:.1f} {p2x:.1f},{p2y:.1f} {p3x:.1f},{p3y:.1f}" fill="{color}"/>'
    )
    if flow:
        out += f'<path d="M{x1} {y1} L{x2} {y2}" fill="none" stroke="none" data-flow-path="1" data-flow-color="{color}"/>'
    return out


def curve_arrow(d, color=C, width=3.5, draw=True, length=520, marker=True, flow=False, end_xy=None):
    d_attr = f' data-draw="{length}"' if draw else ''
    out = f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{width}" stroke-linecap="round"{d_attr}/>'
    if marker and end_xy:
        ex, ey = end_xy
        out += f'<polygon points="{ex},{ey} {ex-13},{ey-6.5} {ex-13},{ey+6.5}" fill="{color}"/>'
    if flow:
        out += f'<path d="{d}" fill="none" stroke="none" data-flow-path="1" data-flow-color="{color}"/>'
    return out


def rect_bar(x, y, w, h, fill=C, rx=8, grow_x=False, grow_y=False, opacity=1.0, stroke=None):
    attrs = ''
    if grow_x:
        attrs += ' data-grow-x="1"'
    if grow_y:
        attrs += ' data-grow-y="1"'
    if opacity < 1.0:
        attrs += f' fill-opacity="{opacity}"'
    s_attr = f' stroke="{stroke}" stroke-width="1.5"' if stroke else ''
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}"{s_attr}{attrs}/>'


def progress_ring(cx, cy, r, pct, color=AMBER, track='#d7e4e9', width=13):
    circ = round(2 * math.pi * r, 1)
    offset = round(circ * (1.0 - pct), 1)
    return (
        f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#ffffff" stroke="{track}" stroke-width="{width}"/>'
        f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{color}" stroke-width="{width}" stroke-linecap="round" '
        f'transform="rotate(-90 {cx} {cy})" stroke-dasharray="{circ}" stroke-dashoffset="{offset}" data-ring-circ="{circ}" data-ring-offset="{offset}"/>'
    )


def group(content, step=0, extra=''):
    ext = f' {extra}' if extra else ''
    return f'<g data-step="{step}"{ext}>{content}</g>'


def svg(content):
    defs = (
        '<defs>'
        f'<marker id="arrow-cyan" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6.5" markerHeight="6.5" orient="auto-start-reverse">'
        f'<path d="M 0 1.5 L 9 5 L 0 8.5 z" fill="{C}"/></marker>'
        f'<marker id="arrow-amber" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6.5" markerHeight="6.5" orient="auto-start-reverse">'
        f'<path d="M 0 1.5 L 9 5 L 0 8.5 z" fill="{AMBER}"/></marker>'
        f'<marker id="arrow-muted" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6.5" markerHeight="6.5" orient="auto-start-reverse">'
        f'<path d="M 0 1.5 L 9 5 L 0 8.5 z" fill="{MUTED}"/></marker>'
        '</defs>'
    )
    return '<svg class="visual" viewBox="0 0 1728 650" xmlns="http://www.w3.org/2000/svg" role="img">' + defs + content + '</svg>'


def icon(kind, x, y, scale=1, color=C, slide_from_x=None, pulse=False):
    shapes = {
        'truck': '<path d="M8 30h92v64H8z M100 51h34l25 25v18h-59 M113 58h16l16 19h-32"/><circle cx="38" cy="99" r="13"/><circle cx="130" cy="99" r="13"/>',
        'doc': '<path d="M35 7h65l28 28v100H35z M100 7v30h28 M53 57h56 M53 77h56 M53 97h36"/>',
        'tower': '<path d="M80 15v116 M47 132h66 M80 28L52 132 M80 28l28 104 M65 78h30 M38 54Q5 26 38 0 M122 54q33-28 0-54 M51 40Q31 23 51 10 M109 40q20-17 0-30"/><circle cx="80" cy="18" r="7"/>',
        'check': '<path d="M28 70l32 30 75-75" data-draw="180"/>',
        'people': '<circle cx="65" cy="35" r="23"/><path d="M16 121v-17q0-34 49-34t49 34v17 M119 20q35-5 35 26t-35 29 M130 82q35 5 35 39"/>',
        'terminal': '<path d="M10 62l70-48 70 48v73H10z M38 135V76h84v59 M65 78v57 M95 78v57"/>',
        'shield': '<path d="M80 6l60 22v45q0 40-60 68Q20 113 20 73V28z M47 71l25 25 44-48"/>',
        'chip': '<rect x="32" y="32" width="76" height="76" rx="10"/><rect x="52" y="52" width="36" height="36" rx="4"/><path d="M50 14v18 M70 14v18 M90 14v18 M50 108v18 M70 108v18 M90 108v18 M14 50h18 M14 70h18 M14 90h18 M108 50h18 M108 70h18 M108 90h18"/>',
        'cloud': '<path d="M42 104h68a28 28 0 0 0 4-55 38 38 0 0 0-73-11A26 26 0 0 0 42 104z"/><path d="M52 122h56 M80 104v18"/>',
        'db': '<ellipse cx="75" cy="32" rx="46" ry="16"/><path d="M29 32v68c0 9 21 16 46 16s46-7 46-16V32"/><path d="M29 66c0 9 21 16 46 16s46-7 46-16"/>',
    }
    attrs = ''
    if slide_from_x is not None:
        attrs += f' data-slide-from-x="{slide_from_x}"'
    if pulse:
        attrs += ' data-pulse="1"'
    return f'<g transform="translate({x} {y}) scale({scale})" fill="none" stroke="{color}" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"{attrs}>{shapes[kind]}</g>'


def add(title, eyebrow, content, source, notes, seconds=45, steps=3, backup=False, kind=''):
    n = len(SLIDES) + 1
    SLIDES.append(dict(
        id=f's{n:02}',
        title=title,
        eyebrow=eyebrow,
        content=svg(content),
        source=source,
        notes=notes,
        seconds=seconds,
        steps=steps,
        backup=backup,
        kind=kind,
    ))


# Portada formal, separada de la apertura operacional.
v = group(
    badge(20, 52, 'TRANSPORTES CURIMÓN · TFEP-01/2026', C, '#e7f3f6', 520, 44, 22)
    + text(20, 184, 'REVISIÓN 2', 94, WHITE, 700)
    + text(20, 266, 'Informe y presentación', 53, C, 600)
    + text(20, 322, 'Correcciones · riesgos · EDT · planificación', 29, MUTED)
    + line(20, 368, 1660, 368, STROKE, 3, draw=True)
    + text(20, 435, 'audIT Soluciones Tecnológicas SpA', 35, WHITE, 600)
    + text(20, 482, 'Propuesta técnica para transporte de carga', 28, MUTED)
    + '<g data-slide-from-x="-700"><g data-moving-truck="1">' + icon('truck', 1100, 320, 2.1, C) + '</g></g>',
    0,
)
add(
    'Revisión 2 · Caso Transporte de Carga',
    'PRESENTACIÓN TÉCNICA / INFORME 2',
    v,
    'Transportes Curimón · TFEP-01/2026 · audIT Soluciones Tecnológicas SpA',
    'Presentar el alcance de la revisión: correcciones del Informe 1, riesgos de solución, proyecto e implantación, EDT, planificación e hitos. La exposición dura 15 minutos y deja 15 minutos para preguntas.',
    15,
    1,
    kind='cover',
)

# ==============================================================================
# BLOQUE 1: SOLUCIÓN, ARQUITECTURA Y CORRECCIONES (S2 · S3 · S4 · S5)
# ==============================================================================

# 1. s01 — Apertura Operacional (30 s · S2 / S3 §3.3)
v = group(
    badge(0, 26, 'TRANSPORTES CURIMÓN · TFEP-01/2026', C, '#e7f3f6', 475, 42, 22)
    + text(0, 148, 'Una salida segura exige', 76, WHITE, 650)
    + text(0, 236, 'información confiable.', 76, C, 650)
    + card(1085, 32, 625, 220, CARD_BG, STROKE, 16, AMBER)
    + text(1120, 88, 'REGLA DE SALIDA BLOQUEANTE', 24, AMBER, 700)
    + text(1120, 140, '3 verificaciones en línea', 38, WHITE, 600)
    + text(1120, 188, 'Sin conformidad documental y técnica,', 27, MUTED)
    + text(1120, 224, 'la orden de viaje no se libera en cabina.', 27, MUTED),
    0,
)
v += group(
    line(30, 430, 1690, 430, '#bdced6', 5, draw=True)
    + line(30, 430, 1280, 430, C, 5, draw=True)
    + '<g data-slide-from-x="-880"><g data-moving-truck="1">' + icon('truck', 1235, 268, 1.55, C) + '</g></g>'
    + badge(1515, 325, 'RUTA ACTIVA', AMBER, '#fff0d7', 180, 38, 21),
    0,
)
for i, (code, a, b, sub) in enumerate([
    ('01 · CONDUCTOR', 'Conductor', 'Aptitud y jornada vigente', 'Licencia, biometría y descanso'),
    ('02 · VEHÍCULO', 'Vehículo', 'Vigencias y telemetría CAN', 'Estado técnico y bus J1939'),
    ('03 · DOCUMENTO', 'Documento', 'Disponibilidad y conformidad', 'Guía/DTE íntegro en cabina'),
]):
    x = 30 + i * 565
    cx = x + 265
    v += group(
        line(cx, 430, cx, 468, C, 3, draw=True)
        + circle(cx, 430, 11, C, C, pulse=True)
        + card(x, 468, 530, 168, CARD_BG, STROKE, 14, C)
        + badge(x + 26, 484, code, C, '#e7f3f6', 195, 30, 18)
        + text(x + 26, 544, a, 36, WHITE, 600)
        + text(x + 26, 580, b, 25, C, 500)
        + text(x + 26, 614, sub, 22, MUTED),
        i,
    )
add(
    'Una salida segura exige información confiable.',
    'REVISIÓN 2 / TFEP-01/2026',
    v,
    'S2 · S3 §3.3 · S8: verificación bloqueante de salida',
    'Abrir desde la operación real. El camión se desplaza sobre un carril dedicado mientras se activan los tres controles bloqueantes inferiores: conductor, vehículo y documento deben aportar evidencia válida antes de autorizar la salida.',
    30,
    3,
    kind='operational',
)

# 2. s02 — Recorrido Operacional Cabina → Terminal → Torre (45 s · S3 §3.3 · S3 §3.2.4)
v = ''
nodes_s02 = [
    ('truck', '01 · BORDE', 'Cabina', 'Evidencia a bordo y biometría', 'Gateway + tablet + buffer local', 30),
    ('terminal', '02 · CONTROL', 'Terminal', 'Validación y sincronización', 'Inspección y despacho local', 625),
    ('tower', '03 · NÚCLEO', 'Torre de control', 'Asignación y seguimiento', 'Monitoreo de flota 24/7', 1220),
]
for i, (ic, tag, lab, desc1, desc2, x) in enumerate(nodes_s02):
    v += group(
        card(x, 30, 475, 360, CARD_BG, STROKE, 16, C, accent_top=True)
        + badge(x + 28, 56, tag, C, '#e7f3f6', 165, 34, 20)
        + icon(ic, x + 182, 82, 0.96, C)
        + text(x + 237, 282, lab, 40, WHITE, 600, 'middle')
        + text(x + 237, 326, desc1, 26, C, 500, 'middle')
        + text(x + 237, 364, desc2, 23, MUTED, 400, 'middle'),
        i,
    )
    if i < 2:
        v += group(
            arrow(x + 483, 210, x + 587, 210, C, 4, draw=True, flow=True)
            + text(x + 535, 188, 'Telemetría' if i == 0 else 'Eventos', 19, MUTED, 500, 'middle'),
            i + 1,
        )
v += group(
    arrow(1457, 392, 1457, 458, C, 3.5, draw=True, flow=True)
    + line(265, 462, 1460, 462, C, 4, draw=True)
    + line(265, 462, 265, 498, C, 3, draw=True)
    + line(862, 462, 862, 498, C, 3, draw=True)
    + line(1457, 462, 1457, 498, C, 3, draw=True)
    + circle(265, 462, 7, C, C)
    + circle(862, 462, 7, C, C)
    + circle(1457, 462, 7, C, C)
    + card(30, 498, 475, 134, CARD_ALT, STROKE, 12, AMBER)
    + text(58, 548, 'ERP contable', 33, AMBER, 600)
    + text(58, 594, 'Conservado como emisor tributario DTE', 24, MUTED)
    + card(625, 498, 475, 134, CARD_ALT, STROKE, 12, C)
    + text(653, 548, 'Posicionamiento GPS', 33, C, 600)
    + text(653, 594, 'Integración de rastro y geocercas', 24, MUTED)
    + card(1220, 498, 475, 134, CARD_ALT, STROKE, 12, C)
    + text(1248, 548, 'Portal Transportistas', 33, C, 600)
    + text(1248, 594, 'Vigencias documentales y flota externa', 24, MUTED),
    2,
)
add(
    'La solución conecta cabina, terminal y torre.',
    'SOLUCIÓN / RECORRIDO DE UN VIAJE',
    v,
    'S3 §3.3 · S3 §3.2.4: recorrido operacional e integraciones externas',
    'Recorrer el viaje del dato desde la cabina hasta la torre de control. El terminal aporta validación y sincronización. La torre coordina la operación y se integra mediante bus con el ERP contable (emisor tributario), posicionamiento y transportistas.',
    45,
    3,
)

# 3. s03 — [NUEVA] Arquitectura Física, Lógica y Resiliencia de Datos (60 s · S4.1 · S4.2 · S5 · T-11)
v = ''
# Columna 1: Borde Embarcado (S4.2 / T-11)
v += group(
    card(20, 28, 535, 598, CARD_BG, STROKE, 16, C, accent_top=True)
    + badge(48, 52, 'S4.2 · FORMULARIO T-11', C, '#e7f3f6', 275, 34, 20)
    + icon('chip', 455, 36, 0.54, C)
    + text(48, 138, 'Borde Embarcado IoT', 37, WHITE, 600)
    + text(48, 222, '374', 66, C, 700, count_to=374)
    + text(195, 202, 'Gateways telemáticos', 28, WHITE, 600)
    + text(195, 236, 'Flota total objetivo equipada', 23, MUTED)
    + line(48, 268, 525, 268, STROKE, 1.5)
    + text(48, 340, '61', 58, AMBER, 700, count_to=61)
    + text(155, 322, 'Interfaces CANclick', 28, WHITE, 600)
    + text(155, 356, 'Lectura J1939 no invasiva sin corte', 23, MUTED)
    + line(48, 390, 525, 390, STROKE, 1.5)
    + text(48, 462, '8 GB', 54, C, 700, count_to=8, count_suffix=' GB')
    + text(198, 444, 'Buffer local eMMC', 28, WHITE, 600)
    + text(198, 478, 'Store & Forward en zonas oscuras', 23, MUTED)
    + rect_bar(48, 518, 475, 16, '#dce9ed', 8)
    + rect_bar(48, 518, 415, 16, C, 8, grow_x=True)
    + text(48, 568, 'Protección IP67 · Norma SAE J1455', 24, MUTED)
    + text(48, 600, '350 kits huella + 225 cámaras DMS', 23, C, 500),
    0,
)
# Columna 2: Arquitectura Lógica Cloud (S4.1)
v += group(
    arrow(560, 320, 591, 320, C, 3.5, draw=True, flow=True)
    + card(596, 28, 535, 598, CARD_BG, STROKE, 16, C, accent_top=True)
    + badge(624, 52, 'S4.1 · ARQUITECTURA LÓGICA', C, '#e7f3f6', 310, 34, 20)
    + icon('cloud', 1030, 36, 0.54, C)
    + text(624, 138, 'Núcleo Cloud y Eventos', 37, WHITE, 600)
    + card(624, 168, 478, 118, CARD_ALT, STROKE, 12, C)
    + text(648, 212, 'Ingesta Asíncrona y Telemetría', 27, C, 600)
    + text(648, 248, 'Colas de eventos desacopladas · TLS 1.3', 23, MUTED)
    + text(648, 274, 'Idempotencia ante reconexión satelital/LTE', 22, WHITE)
    + card(624, 306, 478, 118, CARD_ALT, STROKE, 12, AMBER)
    + text(648, 350, 'Persistencia Políglota', 27, AMBER, 600)
    + text(648, 386, 'Transaccional + Series de Tiempo + Caché', 23, MUTED)
    + text(648, 412, 'Reglas RN-01..RN-04 auditables por viaje', 22, WHITE)
    + card(624, 444, 478, 154, CARD_ALT, STROKE, 12, C)
    + text(648, 488, 'Continuidad en San Bernardo', 27, WHITE, 600)
    + text(648, 524, 'Doble enlace fibra/LTE + grupo electrógeno', 23, MUTED)
    + text(648, 558, 'Contingencia regional documentada en S4', 22, AMBER)
    + text(648, 584, '(mitigación activa ante corte zonal)', 21, MUTED),
    1,
)
# Columna 3: Modelo de Datos y Migración (S5)
v += group(
    arrow(1136, 320, 1167, 320, C, 3.5, draw=True, flow=True)
    + card(1172, 28, 535, 598, CARD_BG, STROKE, 16, AMBER, accent_top=True)
    + badge(1200, 52, 'S5 · DATOS Y MIGRACIÓN', AMBER, '#fff0d7', 285, 34, 20)
    + icon('db', 1605, 36, 0.54, AMBER)
    + text(1200, 138, 'Gobierno y Evidencia', 37, WHITE, 600)
    + text(1200, 222, '96.000', 60, AMBER, 700, count_to=96, count_suffix='.000')
    + text(1418, 202, 'Viajes/año históricos', 27, WHITE, 600)
    + text(1418, 236, 'Migración progresiva 2013', 23, MUTED)
    + line(1200, 268, 1678, 268, STROKE, 1.5)
    + card(1200, 290, 478, 148, CARD_ALT, STROKE, 12, C)
    + text(1224, 334, 'Entidad: EvidenciaJornada', 28, C, 600)
    + text(1224, 372, 'Vincula Conductor + Vehículo + DTE + Hash', 23, WHITE)
    + text(1224, 408, 'Trazabilidad inmutable de autorización', 23, MUTED)
    + card(1200, 458, 478, 140, CARD_ALT, STROKE, 12, AMBER)
    + text(1224, 502, 'Estrategia ETL y Reconciliación', 27, AMBER, 600)
    + text(1224, 538, 'Catálogos maestros saneados antes de E1', 23, WHITE)
    + text(1224, 574, 'Consulta histórica garantizada hasta M24', 23, MUTED),
    2,
)
add(
    'La arquitectura integra borde, nube y trazabilidad.',
    'ARQUITECTURA FÍSICA, LÓGICA Y DATOS / S4.1 · S4.2 · S5',
    v,
    'S4.1: arquitectura lógica · S4.2 / T-11: equipamiento a bordo · S5: modelo de datos y migración',
    'Explicar las tres capas técnicas del Informe 2: en el borde (S4.2/T-11), 374 gateways, 61 interfaces CANclick no invasivas y buffer local de 8 GB; en la nube (S4.1), ingesta asíncrona y continuidad en San Bernardo advirtiendo su condición de contingencia regional; en datos (S5), la entidad EvidenciaJornada y la migración de 96.000 viajes/año.',
    60,
    3,
)

# 4. s04 — Decisiones de Solución y Cadena de Evidencia (60 s · Obs. 37, 43 y 48 — S3 / T-12 / T-14 / T-17)
v = ''
# Fila superior: Observaciones 37 y 43 en dos tarjetas comparativas
v += group(
    card(20, 22, 825, 255, CARD_BG, STROKE, 16, C)
    + badge(48, 44, 'OBSERVACIÓN 37 · INFORME 1', C, '#e7f3f6', 310, 34, 19)
    + text(695, 67, 'S3 §3.3', 25, C, 700)
    + text(48, 122, 'Brecha: Faltaba esquema conceptual integrador.', 28, MUTED)
    + text(48, 172, 'Decisión: Recorrido extremo a extremo documentado', 31, WHITE, 600)
    + text(48, 214, 'con fronteras claras entre cabina, terminal, torre y ERP.', 26, C)
    + text(48, 252, 'Estado: Incorporado en S3 §3.3 (síntesis funcional).', 23, MUTED)
    + card(875, 22, 835, 255, CARD_BG, STROKE, 16, C)
    + badge(903, 44, 'OBSERVACIÓN 43 · INFORME 1', C, '#e7f3f6', 310, 34, 19)
    + text(1535, 67, 'S3 §3.2.4', 25, C, 700)
    + text(903, 122, 'Brecha: Faltaba definir el futuro del sistema 2013.', 28, MUTED)
    + text(903, 172, 'Decisión: Sustitución progresiva por funciones;', 31, WHITE, 600)
    + text(903, 214, 'ERP contable se conserva como emisor tributario.', 26, C)
    + text(903, 252, 'Producción E1 M16 / E2 M21 · Consulta legado hasta M24.', 23, MUTED),
    0,
)
# Fila central: Cadena de cierre de Observación 48 (4 tarjetas conectadas)
chain_s04 = [
    ('RNF-011', 'Requisito de convivencia', 'Sin detenciones por despliegue', 'S3 §3.4.5 · T-12'),
    ('EDT 11.2', 'Paquete de trabajo', 'Despliegue gradual Etapa 1', 'Formulario T-14'),
    ('CP-INT-05', 'Prueba de integración', 'Intercambio con sistema legado', 'Formulario T-17'),
    ('CP-SYS-05', 'Prueba de sistema', 'Verificación de no regresión', 'Formulario T-17'),
]
for i, (code, title_c, desc_c, loc_c) in enumerate(chain_s04):
    x = 20 + i * 432
    v += group(
        card(x, 305, 392, 198, CARD_ALT, STROKE, 14, AMBER if i >= 2 else C, accent_top=True)
        + text(x + 24, 360, code, 38, AMBER if i >= 2 else C, 700)
        + text(x + 24, 404, title_c, 27, WHITE, 600)
        + text(x + 24, 442, desc_c, 23, MUTED)
        + badge(x + 24, 456, loc_c, C if i < 2 else AMBER, '#e7f3f6', 205, 32, 18),
        1,
    )
    if i < 3:
        v += group(arrow(x + 396, 404, x + 428, 404, C, 3.5, draw=True), 1)
# Fila inferior: Banner de rigor metodológico
v += group(
    card(20, 526, 1690, 106, CARD_BG, STROKE, 14, AMBER)
    + badge(48, 548, 'OBSERVACIÓN 48 · TRAZABILIDAD DOCUMENTAL', AMBER, '#fff0d7', 435, 34, 19)
    + text(510, 572, 'Cadena íntegra verificada entre requisito, paquete EDT y protocolo de pruebas.', 30, WHITE, 600)
    + text(48, 612, 'Alcance actual: T-17 acredita el diseño y cobertura documental de los casos; su ejecución y actas corresponden a la fase contractual.', 25, AMBER),
    2,
)
add(
    'Las correcciones vinculan decisiones y pruebas.',
    'CORRECCIONES / OBSERVACIONES 37, 43 Y 48 · S3 · T-12 · T-14 · T-17',
    v,
    'S3 §§3.2.4 y 3.3 · T-12: RNF-011 · T-14: 11.2 · T-17: CP-INT-05 y CP-SYS-05',
    'Unificar las tres correcciones estructurales del Informe 1: las observaciones 37 y 43 quedan resueltas en S3 con el esquema conceptual y el calendario de retiro del legado 2013. Para la observación 48, mostrar la cadena completa RNF-011 → 11.2 → CP-INT-05 → CP-SYS-05 advirtiendo que las pruebas están diseñadas, no ejecutadas.',
    60,
    3,
)

# ==============================================================================
# BLOQUE 2: METODOLOGÍA Y ASEGURAMIENTO DE CALIDAD (S6 · S9)
# ==============================================================================

# 5. s05 — [NUEVA] Metodología DevSecOps y Aseguramiento de Calidad (60 s · S6 · S9 · T-9 · T-10 · T-13 · T-17)
v = ''
# Izquierda: S6 Metodología de Desarrollo y Gestión del Cambio
v += group(
    card(20, 26, 535, 602, CARD_BG, STROKE, 16, C, accent_top=True)
    + badge(48, 54, 'S6 · METODOLOGÍA · T-9 / T-10', C, '#e7f3f6', 310, 34, 19)
    + text(48, 130, 'Gobierno DevSecOps', 38, WHITE, 600)
    + card(48, 160, 478, 130, CARD_ALT, STROKE, 12, C)
    + text(72, 202, 'Ciclo Híbrido con Sprints de 2 Semanas', 25, C, 600)
    + text(72, 238, 'Compuertas de arquitectura e integración continua', 19.5, WHITE)
    + text(72, 268, 'Entornos segregados: DEV → QA → PREPROD → PROD', 18.5, MUTED)
    + card(48, 310, 478, 130, CARD_ALT, STROKE, 12, AMBER)
    + text(72, 352, 'Control de Cambios (T-10)', 25, AMBER, 600)
    + text(72, 388, 'Evaluación de impacto en plazo, red y seguridad', 20, WHITE)
    + text(72, 418, 'Aprobación formal en Comité antes de liberación', 19.5, MUTED)
    + card(48, 460, 478, 142, CARD_ALT, STROKE, 12, C)
    + text(72, 514, '≤ 5 %', 48, C, 700)
    + text(225, 498, 'Tasa de cambio fallido', 25, WHITE, 600)
    + text(225, 530, 'Umbral mensual en producción', 21, MUTED)
    + text(72, 578, 'Rollback automatizado y telemetría post-despliegue', 19.5, C),
    0,
)
# Centro: S9 / T-13 Estándares y Quality Gates Hardware/Software
v += group(
    card(585, 26, 535, 602, CARD_BG, STROKE, 16, C, accent_top=True)
    + badge(613, 54, 'S9 · ESTÁNDARES · FORMULARIO T-13', C, '#e7f3f6', 355, 34, 19)
    + text(613, 130, 'Quality Gates Técnicos', 38, WHITE, 600)
    + card(613, 160, 478, 140, CARD_ALT, STROKE, 12, C)
    + text(637, 202, 'Hardware Embarcado y Telemetría', 26, C, 600)
    + text(637, 238, 'Vibración SAE J1455 · Sellado IP67 en cabina', 22, WHITE)
    + text(637, 274, 'Pérdida de tramas CAN J1939 < 0,1 % en banco', 21, AMBER)
    + card(613, 320, 478, 140, CARD_ALT, STROKE, 12, C)
    + text(637, 362, 'Calidad de Software y Seguridad', 26, C, 600)
    + text(637, 398, 'Análisis estático SAST/DAST sin críticos abiertos', 20.5, WHITE)
    + text(637, 434, 'Cobertura de reglas de negocio RN-01..RN-04', 21, MUTED)
    + card(613, 480, 478, 122, CARD_ALT, STROKE, 12, AMBER)
    + text(637, 522, 'Inspección de Montaje por Flota', 26, AMBER, 600)
    + text(637, 558, 'Protocolo de recepción unitaria por camión', 23, WHITE)
    + text(637, 588, 'Checklist firmado antes de habilitar en torre', 21, MUTED),
    1,
)
# Derecha: S9 / T-17 Matriz de 120 Casos de Prueba (Barras verticales crecientes)
v += group(
    card(1150, 26, 558, 602, CARD_BG, STROKE, 16, AMBER, accent_top=True)
    + badge(1178, 54, 'S9 · PLAN DE PRUEBAS · T-17', AMBER, '#fff0d7', 310, 34, 19)
    + text(1178, 150, '120', 60, AMBER, 700, count_to=120)
    + text(1336, 122, 'Casos de prueba diseñados', 26, WHITE, 600)
    + text(1336, 154, 'Norma ISO/IEC/IEEE 29119', 22, MUTED)
    + line(1178, 174, 1680, 174, STROKE, 1.5)
    # Gráfico de barras verticales por nivel de prueba
    + rect_bar(1200, 270, 95, 190, C, 8, grow_y=True)
    + text(1247, 252, '38', 28, C, 700, 'middle')
    + text(1247, 492, 'Unitarias', 21, WHITE, 600, 'middle')
    + text(1247, 518, 'Reglas RN', 19, MUTED, 400, 'middle')
    + rect_bar(1325, 295, 95, 165, C, 8, grow_y=True)
    + text(1372, 277, '32', 28, C, 700, 'middle')
    + text(1372, 492, 'Integración', 21, WHITE, 600, 'middle')
    + text(1372, 518, 'CP-INT-05', 19, C, 500, 'middle')
    + rect_bar(1450, 315, 95, 145, AMBER, 8, grow_y=True)
    + text(1497, 297, '28', 28, AMBER, 700, 'middle')
    + text(1497, 492, 'Sistema', 21, WHITE, 600, 'middle')
    + text(1497, 518, 'CP-SYS-05', 19, AMBER, 500, 'middle')
    + rect_bar(1575, 345, 95, 115, AMBER, 8, grow_y=True)
    + text(1622, 327, '22', 28, AMBER, 700, 'middle')
    + text(1622, 492, 'UAT Terreno', 21, WHITE, 600, 'middle')
    + text(1622, 518, '5 Terminales', 19, MUTED, 400, 'middle')
    + line(1185, 460, 1685, 460, '#bdced6', 2)
    + card(1178, 538, 502, 68, CARD_ALT, STROKE, 10, C)
    + text(1196, 580, 'Criterio: 100 % casos críticos sin defectos S1/S2', 20, WHITE, 500),
    2,
)
add(
    'La calidad se controla desde el código hasta terreno.',
    'METODOLOGÍA Y CALIDAD / S6 · S9 · T-9 · T-10 · T-13 · T-17',
    v,
    'S6 / T-9 / T-10: metodología y control de cambios · S9 / T-13 / T-17: aseguramiento de calidad y 120 casos de prueba',
    'Cubrir los capítulos S6 y S9 del Informe 2: ciclo iterativo con control de cambios formal y umbral de <=5% de cambios fallidos en producción; compuertas de calidad para hardware (SAE J1455, IP67, pérdida CAN <0,1%) y 120 casos de prueba diseñados en T-17 bajo ISO 29119.',
    60,
    3,
)

# ==============================================================================
# BLOQUE 3: GESTIÓN DE RIESGOS Y AMFE (S8 · T-16)
# ==============================================================================

# 6. s06 — Método Común P×I y Reducción Inicial→Residual (60 s · S8 §8.1 · T-16)
v = ''
# Panel izquierdo: 3 Ámbitos y Escala P x I
v += group(
    card(20, 24, 650, 604, CARD_BG, STROKE, 16, C, accent_top=True)
    + badge(48, 52, 'S8 §8.1 · METODOLOGÍA P × I', C, '#e7f3f6', 295, 34, 19)
    + text(48, 124, 'Tres Ámbitos de Exposición', 36, WHITE, 600)
    + card(48, 150, 594, 92, CARD_ALT, STROKE, 12, C)
    + text(70, 194, '01 · Solución', 27, C, 700)
    + text(312, 194, '¿La tecnología cumple en ruta?', 22, WHITE)
    + text(312, 224, 'Ej.: R-28 retorno satelital DTE', 20, MUTED)
    + card(48, 256, 594, 92, CARD_ALT, STROKE, 12, C)
    + text(70, 300, '02 · Desarrollo', 27, C, 700)
    + text(312, 300, '¿El proyecto llega a tiempo?', 22, WHITE)
    + text(312, 330, 'Ej.: R-16 compuerta G13 y A13', 20, MUTED)
    + card(48, 362, 594, 92, CARD_ALT, STROKE, 12, C)
    + text(70, 406, '03 · Implantación', 27, C, 700)
    + text(312, 406, '¿La operación adopta el cambio?', 22, WHITE)
    + text(312, 436, 'Ej.: R-11 adhesión y R-18 MB', 20, MUTED)
    + text(48, 496, 'Escala Ordinal Probabilidad (1–5) × Impacto (1–5)', 24, WHITE, 600)
    + rect_bar(48, 516, 185, 22, C, 6, grow_x=True)
    + rect_bar(242, 516, 195, 22, AMBER, 6, grow_x=True)
    + rect_bar(446, 516, 196, 22, CORAL, 6, grow_x=True)
    + text(48, 568, 'Baja 1–5', 25, C, 600)
    + text(242, 568, 'Media 6–11', 25, AMBER, 600)
    + text(446, 568, 'Alta 12–25', 25, CORAL, 600)
    + text(48, 606, 'Escala ordinal para priorizar; no equivale a porcentaje.', 21, MUTED),
    0,
)
# Panel derecho: Gráfico Dumbbell Conectado (Reducción Inicial -> Residual)
def rx_pos(val):
    return 1110 + int(val * 22)

v += group(
    card(700, 24, 1008, 604, CARD_BG, STROKE, 16, AMBER, accent_top=True)
    + badge(728, 52, 'T-16 · REDUCCIÓN DE EXPOSICIÓN ESTIMADA', AMBER, '#fff0d7', 415, 34, 19)
    + text(728, 124, 'Efecto del Plan de Mitigación (Inicial → Residual)', 34, WHITE, 600)
    # Bandas de fondo por nivel de exposición
    + rect_bar(rx_pos(0), 155, rx_pos(5.5) - rx_pos(0), 340, C, 6, opacity=0.07)
    + rect_bar(rx_pos(5.5), 155, rx_pos(11.5) - rx_pos(5.5), 340, AMBER, 6, opacity=0.07)
    + rect_bar(rx_pos(11.5), 155, rx_pos(25) - rx_pos(11.5), 340, CORAL, 6, opacity=0.07),
    1,
)
for val in [0, 4, 8, 12, 16, 20, 25]:
    xp = rx_pos(val)
    v += group(
        line(xp, 155, xp, 495, '#cbdce2', 1.5)
        + text(xp, 530, str(val), 23, MUTED, 500, 'middle'),
        1,
    )
dumbbell_rows = [
    ('R-28', 'Documento en ruta', 'Pre-emisión + bloqueo cabina', 12, 8),
    ('R-16', 'Capacitación A13', 'Compuerta G13 + reserva A14', 8, 4),
    ('R-11', 'Adhesión flota', 'Meta M9 ≥60/148 + mesa apoyo', 12, 8),
]
for i, (rcode, rname, rmit, ini, res) in enumerate(dumbbell_rows):
    y = 212 + i * 108
    x_ini = rx_pos(ini)
    x_res = rx_pos(res)
    dx = x_ini - x_res
    v += group(
        text(728, y - 6, rcode, 31, C, 700)
        + text(822, y - 6, rname, 25, WHITE, 600)
        + text(728, y + 26, rmit, 21, MUTED)
        + circle(x_ini, y, 14, AMBER, AMBER),
        1,
    )
    v += group(
        arrow(x_ini - 16, y, x_res + 16, y, C, 4, draw=True)
        + circle(x_res, y, 14, C, C, slide_from_x=dx)
        + badge(x_res - 50, y - 48, f'{res} (Res.)', C, '#e7f3f6', 86, 28, 16)
        + badge(x_ini - 34, y - 48, f'{ini} (Ini.)', AMBER, '#fff0d7', 86, 28, 16),
        2,
    )
v += group(
    text(728, 576, '● Exposición Inicial', 24, AMBER, 600)
    + text(1015, 576, '← ● Exposición Residual Estimada', 24, C, 600)
    + text(728, 610, 'Nota: R-28 y R-11 mantienen impacto 4; el control reduce probabilidad pero exige contingencia.', 20, WHITE),
    2,
)
add(
    'El método P×I evalúa y reduce la exposición.',
    'RIESGOS / MÉTODO Y REDUCCIÓN ESTIMADA · S8 §8.1 · T-16',
    v,
    'S8 §8.1 · T-16: matriz de exposición inicial y residual en escala ordinal 1–25',
    'Presentar los tres ámbitos de riesgo y la escala ordinal P×I a la izquierda. A la derecha, mostrar cómo los controles reducen la exposición estimada de R-28 (12→8), R-16 (8→4) y R-11 (12→8), recalcando que no son porcentajes y que el impacto sigue exigiendo contingencia.',
    60,
    3,
)

# 7. s07 — Riesgo de la Solución en Ruta: R-28 y SLA de 90 s (60 s · T-16: R-28 · S8 §8.2)
v = ''
r28_nodes = [
    ('doc', '01 · ORIGEN', 'ERP emite DTE', 'Guía electrónica timbrada', 'Pre-emisión cuando carga se conoce', 20),
    ('tower', '02 · ENLACE', 'Retorno satelital', 'Conmutación LTE / Satélite', 'Fragmentación y acuse de recibo', 415),
    ('truck', '03 · CABINA', 'Verificación bloqueante', 'Documento íntegro en tablet', 'Sin conformidad el viaje no sale', 810),
]
for i, (ic, tag, title_n, sub1, sub2, x) in enumerate(r28_nodes):
    v += group(
        card(x, 28, 365, 365, CARD_BG, STROKE, 16, C, accent_top=True)
        + badge(x + 24, 54, tag, C, '#e7f3f6', 165, 32, 18)
        + icon(ic, x + 122, 82, 0.94, C)
        + text(x + 182, 276, title_n, 30, WHITE, 600, 'middle')
        + text(x + 182, 314, sub1, 22, C, 500, 'middle')
        + text(x + 182, 350, sub2, 20, MUTED, 400, 'middle'),
        i,
    )
    if i < 2:
        v += group(arrow(x + 370, 210, x + 410, 210, C, 3.5, draw=True, flow=True), i + 1)

# Panel derecho dedicado al SLA de 90 s con anillo medidor (cero colisión con la antena)
v += group(
    card(1210, 28, 498, 365, CARD_BG, STROKE, 16, AMBER, accent_top=True)
    + badge(1238, 54, 'CASO RT-09.01 · SLA OBJETIVO', AMBER, '#fff0d7', 310, 32, 18)
    + progress_ring(1459, 198, 86, 0.78, AMBER)
    + text(1459, 212, '90 s', 48, AMBER, 700, 'middle', count_to=90, count_suffix=' s')
    + text(1459, 318, 'Presupuesto extremo a extremo', 26, WHITE, 600, 'middle')
    + text(1459, 352, 'Exigencia sujeta a protocolo de ensayo', 22, AMBER, 400, 'middle'),
    3,
)
# Panel inferior de controles y gobierno de R-28
v += group(
    card(20, 418, 1688, 210, CARD_ALT, STROKE, 16, C)
    + badge(48, 444, 'TRATAMIENTO Y GOBIERNO · RIESGO R-28', C, '#e7f3f6', 395, 34, 19)
    + text(470, 468, 'Exposición Inicial: 12 (P3 × I4)  →  Residual Estimada: 8 (P2 × I4)', 26, AMBER, 600)
    + text(48, 520, '1. Mitigación preventiva: Pre-emisión documental cuando la asignación de carga se conoce en planta.', 27, WHITE)
    + text(48, 562, '2. Control técnico: Ensayo del documento completo en zonas de sombra y bloqueo en cabina sin conformidad.', 27, C, 500)
    + text(48, 604, 'Responsable: Líder de Integración  ·  Disparador: Retorno > 90 s o pérdida de fragmentos en pruebas de ruta.', 24, MUTED),
    4,
)
add(
    'Sin documento conforme, el viaje no puede salir.',
    'RIESGOS DE LA SOLUCIÓN / R-28 · S8 §8.2 · CASO RT-09.01',
    v,
    'T-16: R-28 · S8 §8.2 · Caso RT-09.01: presupuesto de retorno documental en 90 s',
    'Explicar que se exige el retorno del documento íntegro a la cabina dentro de 90 segundos, separado en un medidor dedicado. La pre-emisión aplica cuando la carga se conoce. El ensayo extremo a extremo sigue pendiente de acreditación en terreno.',
    60,
    5,
)

# 8. s08 — [PROMOVIDA Y ENRIQUECIDA] AMFE de Equipamiento e Infraestructura (60 s · T-16)
v = ''
v += group(
    card(20, 24, 1688, 92, CARD_ALT, STROKE, 14, C)
    + badge(48, 44, 'FORMULARIO T-16 · ANÁLISIS AMFE', C, '#e7f3f6', 335, 34, 19)
    + text(410, 68, 'Evaluación Severidad (S) × Ocurrencia (O) × Detección (D) = NPR', 30, WHITE, 600)
    + text(410, 98, 'Escala técnica de priorización preventiva (10 modos registrados; ninguno alcanza el umbral crítico NPR = 50).', 23, MUTED),
    0,
)
# Línea vertical de umbral NPR = 50
# Escala de barras: x_start = 945, 1 unidad NPR = 11 px -> NPR 50 = 945 + 550 = 1495
x_bar0 = 945
x_umbral = x_bar0 + int(50 * 11)  # 1495
amfe_rows = [
    ('01 · Borde', 'Equipo a bordo deja de registrar', 'Watchdog local + alerta latido en torre', '4 × 3 × 3', 36, C, 0),
    ('02 · Enlace', 'Módem satelital sin servicio', 'Buffer eMMC 8 GB + conmutación dual', '4 × 2 × 4', 32, C, 1),
    ('03 · Energía', 'Grupo electrógeno no arranca', 'Prueba semanal automatizada + UPS', '3 × 2 × 3', 18, AMBER, 2),
]
for idx, (tag, mode, ctrl, sod, npr, col, st) in enumerate(amfe_rows):
    y = 142 + idx * 125
    bw = int(npr * 11)
    v += group(
        card(20, y, 1688, 108, CARD_BG, STROKE, 14, col)
        + badge(46, y + 18, tag, col, '#e7f3f6' if col == C else '#fff0d7', 145, 30, 18)
        + text(210, y + 42, mode, 29, WHITE, 600)
        + text(210, y + 80, 'Control: ' + ctrl, 21, MUTED)
        + badge(705, y + 32, f'S×O×D: {sod}', WHITE, '#e7f0f3', 210, 42, 20)
        + rect_bar(x_bar0, y + 35, 600, 36, '#e7f0f3', 10)
        + rect_bar(x_bar0, y + 35, bw, 36, col, 10, grow_x=True)
        + text(x_bar0 + bw + 20, y + 64, f'NPR {npr}', 31, col, 700, count_to=npr, count_prefix='NPR '),
        st,
    )
v += group(
    line(x_umbral, 132, x_umbral, 515, CORAL, 3.5, dash='8 6', draw=True)
    + badge(x_umbral - 88, 522, 'UMBRAL NPR = 50', CORAL, '#f9e8e8', 185, 34, 19)
    + card(20, 530, 1340, 96, CARD_ALT, STROKE, 14, AMBER)
    + text(48, 572, 'Prioridad en detección temprana (D): instrumentar telemetría de autodiagnóstico antes de salir a ruta.', 26, WHITE, 600)
    + text(48, 608, 'Nota metodológica: el NPR jerarquiza controles físicos y de enlace; no representa probabilidad porcentual de falla.', 22, AMBER),
    2,
)
add(
    'El AMFE prioriza controles de detección temprana.',
    'RIESGOS TÉCNICOS / AMFE DE EQUIPAMIENTO E INFRAESTRUCTURA · T-16',
    v,
    'T-16: Análisis de Modos y Efectos de Falla (AMFE) · S8 §8.2',
    'Presentar el AMFE promovido al recorrido principal: severidad, ocurrencia y detección para equipo a bordo (NPR 36), módem satelital (NPR 32) y respaldo eléctrico (NPR 18). Todos quedan bajo el umbral 50 gracias a controles de detección anticipada.',
    60,
    3,
)

# 9. s09 — Riesgos de Implantación y Convergencia a Producción (60 s · R-11 · R-19 · R-18)
v = ''
imp_rows = [
    ('R-11 · ADHESIÓN', 'Adhesión de transportistas', 'Meta: ≥ 60 de 148 anexos firmados al corte M9', 'Dueño: Líder Funcional · Activa mesa legal/comercial si ≤ 59', 36, 98),
    ('R-19 · MONTAJE', 'Montaje en flota operativa', 'Control de cobertura mensual acumulada por camión', 'Dueño: Líder de Implantación · Cuadrillas paralelas en terminales', 236, 298),
    ('R-18 · MARCHA BLANCA', 'Estabilidad en marcha blanca', 'Verificación de criterios en M14 y reversión T-18', 'Dueño: Líder de Operación · Paso a producción solo con acta', 436, 498),
]
for i, (tag, title_r, sub1, sub2, y_card, y_Port) in enumerate(imp_rows):
    v += group(
        card(20, y_card, 845, 168, CARD_BG, STROKE, 16, C if i < 2 else AMBER)
        + badge(48, y_card + 20, tag, C if i < 2 else AMBER, '#e7f3f6' if i < 2 else '#fff0d7', 235, 32, 18)
        + text(305, y_card + 44, title_r, 33, WHITE, 600)
        + text(48, y_card + 98, sub1, 26, C if i < 2 else AMBER, 500)
        + text(48, y_card + 138, sub2, 22, MUTED)
        + circle(865, y_Port, 9, C if i < 2 else AMBER, C if i < 2 else AMBER),
        i,
    )
# Nodo derecho de convergencia y aceptación
v += group(
    card(1285, 105, 420, 390, CARD_BG, STROKE, 20, C, accent_top=True)
    + badge(1365, 135, 'CONVERGENCIA E1 / E2', C, '#e7f3f6', 260, 34, 19)
    + circle(1495, 268, 72, C, '#ffffff', 4, pulse=True)
    + icon('check', 1442, 216, 0.72, C)
    + text(1495, 388, 'Producción', 40, WHITE, 700, 'middle')
    + text(1495, 430, 'con aceptación formal', 28, C, 600, 'middle')
    + text(1495, 468, 'Hito H7 (M16) · Hito H12 (M21)', 22, MUTED, 400, 'middle'),
    2,
)
v += group(
    ''.join(
        curve_arrow(f'M 874 {port} C 1060 {port}, 1120 298, 1272 298', C if idx < 2 else AMBER,
                    4, draw=True, length=480, marker=True, flow=True, end_xy=(1282, 298))
        for idx, (_, _, _, _, _, port) in enumerate(imp_rows)
    ),
    3,
)
add(
    'La implantación converge en producción aceptada.',
    'RIESGOS DE IMPLANTACIÓN / R-11 · R-19 · R-18 · T-16 · T-18',
    v,
    'T-16: R-11 (adhesión), R-19 (montaje), R-18 (marcha blanca) · T-18: criterios de salida y reversión',
    'Mostrar cómo las tres corrientes operativas (adhesión de al menos 60 de 148 transportistas en M9, montaje mensual por flota y marcha blanca con reversión disponible) convergen directamente en el nodo de producción con aceptación formal.',
    60,
    4,
)

# ==============================================================================
# BLOQUE 4: PLAN DE TRABAJO, EDT E INNOVACIONES (S7 · S13)
# ==============================================================================

# 10. s10 — EDT (54 Paquetes en 13 Áreas) e Innovaciones T-19 (60 s · S7 §7.1 · S13 · T-14 · T-19)
areas_s10 = [
    ('01', 'Gestión', '4 paq.'),
    ('02', 'Levantamiento', '4 paq.'),
    ('03', 'Plataforma', '5 paq.'),
    ('04', 'Equipo a bordo', '4 paq.'),
    ('05', 'Servicios E1', '5 paq.'),
    ('06', 'Integraciones', '4 paq.'),
    ('07', 'Datos y migración', '4 paq.'),
    ('08', 'Servicios E2', '4 paq.'),
    ('09', 'Adhesión', '3 paq.'),
    ('10', 'Calidad y pruebas', '4 paq.'),
    ('11', 'Implantación', '4 paq.'),
    ('12', 'Innovaciones', '5 paq.'),
    ('13', 'Operación', '4 paq.'),
]
v = group(
    card(20, 18, 1688, 108, CARD_BG, STROKE, 16, C)
    + text(48, 96, '54', 76, C, 700, count_to=54)
    + text(168, 66, 'paquetes de trabajo en 13 áreas de nivel 1 (Diccionario T-14)', 33, WHITE, 600)
    + text(168, 104, 'Cada paquete define entregable verificable, criterio de aceptación y rol responsable único.', 24, MUTED)
    + badge(1425, 46, 'DESCOMPOSICIÓN EDT', C, '#e7f3f6', 255, 40, 20),
    0,
)
# Barra horizontal de distribución de árbol en y = 144
v += group(line(140, 144, 1580, 144, '#bdced6', 3, draw=True), 0)
for col_i in range(4):
    cx = 215 + col_i * 430
    v += group(line(cx, 126, cx, 162, C, 2.5, draw=True), 0)

for i, (num, name, cnt) in enumerate(areas_s10):
    if i < 12:
        col = i % 4
        row = i // 4
        x = 20 + col * 430
        y = 162 + row * 94
        w_card = 398
    else:
        # Área 13 a la izquierda de la fila inferior para dejar spotlight de 11 y 12 a la derecha
        x = 20
        y = 452
        w_card = 398
    highlight = i in (10, 11)
    stroke_c = AMBER if i == 11 else (C if i == 10 else STROKE)
    accent_c = AMBER if i == 11 else (C if i == 10 else None)
    step_idx = 0 if i < 8 else 1
    v += group(
        card(x, y, w_card, 78, CARD_BG if highlight else CARD_ALT, stroke_c, 12, accent_c)
        + badge(x + 16, y + 20, num, AMBER if i == 11 else C, '#e7f3f6', 58, 36, 20)
        + text(x + 88, y + 48, name, 26, WHITE, 600 if highlight else 500)
        + text(x + w_card - 20, y + 48, cnt, 21, AMBER if i == 11 else MUTED, 600, 'end'),
        step_idx,
    )

# Panel inferior derecho (Spotlight S13 / T-19 Innovaciones y conexión con 11 Implantación)
v += group(
    card(450, 452, 1258, 176, CARD_BG, STROKE, 16, AMBER, accent_top=True)
    + badge(478, 476, 'FOCO S13 · ÁREA 12: 5 FICHAS DE INNOVACIÓN (T-19)', AMBER, '#fff0d7', 495, 34, 19)
    + badge(995, 476, 'FOCO S7 · ÁREA 11: IMPLANTACIÓN →', C, '#e7f3f6', 365, 34, 19)
    + text(478, 540, '• 12.1 Analítica Predictiva  ·  12.2 Gemelo Digital de Red  ·  12.3 Visión DMS en Cabina', 25, WHITE, 600)
    + text(478, 576, '• 12.4 Asistente Operacional IA  ·  12.5 Red de Paradores Seguros (piloto controlado M13–M15)', 25, C, 500)
    + text(478, 610, 'Rigor T-19: TRL de componentes distinguido de TRL de integración; beneficios sujetos a línea base en terreno.', 21, MUTED),
    2,
)
add(
    'La EDT estructura 54 paquetes e integra innovaciones.',
    'EDT E INNOVACIONES / S7 §7.1 · S13 · T-14 · T-19',
    v,
    'S7 §7.1 · T-14: 54 paquetes en 13 áreas · S13 / T-19: 5 fichas de innovación (área 12)',
    'Presentar la descomposición de 54 paquetes en 13 áreas. Destacar el área 11 (Implantación) que conectaremos en la lámina siguiente y el área 12 (S13/T-19) con las 5 innovaciones propuestas y su piloto entre M13 y M15.',
    60,
    3,
)

# 11. s11 — Del Alcance al Control: Paquete 11.1 y Compuerta G13→A13 (60 s · T-14: 11.1 · T-15: G13/A13 · R-16)
v = ''
# Izquierda: Ficha de control del paquete 11.1 (T-14)
v += group(
    card(20, 24, 770, 604, CARD_BG, STROKE, 16, C, accent_top=True)
    + badge(48, 52, 'DICCIONARIO EDT · FORMULARIO T-14', C, '#e7f3f6', 360, 34, 19)
    + text(48, 142, '11.1', 56, C, 700)
    + text(202, 114, 'Capacitación Operacional', 36, WHITE, 600)
    + text(202, 152, 'Torre de control · 5 terminales · conductores', 23, MUTED)
    + line(48, 180, 760, 180, STROKE, 1.5)
    + card(48, 202, 714, 92, CARD_ALT, STROKE, 12, C)
    + text(72, 238, 'ENTREGABLE', 21, C, 700)
    + text(72, 272, 'Manuales por perfil, entorno de práctica y registro de asistencia', 24, WHITE)
    + card(48, 308, 714, 92, CARD_ALT, STROKE, 12, C)
    + text(72, 344, 'RESPONSABLE Y VENTANA EN RED (T-15)', 21, C, 700)
    + text(72, 378, 'Líder de Implantación  ·  Actividad A13 (Día 182 al 222 · M10–M12)', 24, WHITE)
    + card(48, 414, 714, 92, CARD_ALT, STROKE, 12, AMBER)
    + text(72, 450, 'CRITERIO DE ACEPTACIÓN', 21, AMBER, 700)
    + text(72, 484, 'Compuerta G13 aprobada + evaluación práctica ≥ 80 % por rol', 24, WHITE)
    + card(48, 522, 714, 82, '#f9f2e7', STROKE, 12, AMBER)
    + text(72, 558, 'Trazabilidad: T-14 define aceptación; T-15 fija precedencia.', 21, AMBER, 600)
    + text(72, 588, 'Las fechas de línea base requieren control de ejecución real.', 20, MUTED),
    0,
)
# Derecha: Flujo bloqueante G13 -> A13 (40d) -> Marcha Blanca y control de R-16
v += group(
    card(820, 24, 888, 604, CARD_BG, STROKE, 16, AMBER, accent_top=True)
    + badge(848, 52, 'RED DE PRECEDENCIAS · T-15 Y RIESGO R-16', AMBER, '#fff0d7', 415, 34, 19)
    + text(848, 124, 'Secuencia Bloqueante de Preparación', 36, WHITE, 600)
    # 3 nodos horizontales dentro del panel derecho
    + card(848, 156, 248, 185, CARD_ALT, STROKE, 14, C, accent_top=True)
    + circle(972, 204, 24, C, '#ffffff', 3, pulse=True)
    + text(972, 213, 'G13', 24, C, 700, 'middle')
    + text(972, 266, 'Versión lista', 27, WHITE, 600, 'middle')
    + text(972, 300, 'PREPROD congelado', 21, MUTED, 400, 'middle')
    + text(972, 326, 'Datos + material', 21, C, 500, 'middle')
    + arrow(1100, 248, 1134, 248, C, 3.5, draw=True)
    + card(1138, 156, 258, 185, CARD_ALT, STROKE, 14, AMBER, accent_top=True)
    + circle(1267, 204, 24, AMBER, '#ffffff', 3)
    + text(1267, 213, 'A13', 24, AMBER, 700, 'middle')
    + text(1267, 266, 'Capacitación', 27, WHITE, 600, 'middle')
    + text(1267, 300, '40 días hábiles', 22, AMBER, 600, 'middle')
    + text(1267, 326, '10d + 30d prácticos', 21, MUTED, 400, 'middle')
    + arrow(1400, 248, 1434, 248, C, 3.5, draw=True)
    + card(1438, 156, 242, 185, CARD_ALT, STROKE, 14, C, accent_top=True)
    + circle(1559, 204, 24, C, '#ffffff', 3)
    + text(1559, 213, 'H6', 24, C, 700, 'middle')
    + text(1559, 266, 'Marcha Blanca', 27, WHITE, 600, 'middle')
    + text(1559, 300, 'Inicio en M13', 21, C, 500, 'middle')
    + text(1559, 326, 'Usuarios acreditados', 21, MUTED, 400, 'middle'),
    1,
)
v += group(
    # Barra segmentada de A13 (10 días familiarización + 30 días práctica + reserva A14)
    text(848, 384, 'Desglose de Actividad A13 (40 días hábiles) y Amortiguador A14:', 25, WHITE, 600)
    + rect_bar(848, 404, 205, 42, C, 8, grow_x=True)
    + text(950, 432, '10 d Familiarización', 18, '#ffffff', 700, 'middle')
    + rect_bar(1061, 404, 395, 42, AMBER, 8, grow_x=True)
    + text(1258, 432, '30 d Práctica y Evaluación por Rol', 19, '#ffffff', 700, 'middle')
    + rect_bar(1464, 404, 216, 42, '#e0ebef', 8, grow_x=True, stroke=C)
    + text(1572, 432, 'Reserva A14 (14 d)', 19, C, 700, 'middle')
    + card(848, 474, 832, 130, CARD_ALT, STROKE, 12, AMBER)
    + text(872, 518, 'Regla de control (R-16): Sin G13 aceptado, A13 no comienza.', 28, AMBER, 700)
    + text(872, 556, 'El adelanto de 10 días está condicionado a entorno PREPROD estable.', 23, WHITE)
    + text(872, 588, 'Dueño: Jefe de Proyecto · Disparador: G13 incompleto o consumo > 50 % de A14.', 21, MUTED),
    2,
)
add(
    'El paquete 11.1 se controla con la compuerta G13.',
    'DEL ALCANCE AL CONTROL / T-14: 11.1 · T-15: G13/A13 · T-16: R-16',
    v,
    'T-14: paquete 11.1 · T-15: compuerta G13, actividad A13 (40 d) y reserva A14 · T-16: riesgo R-16',
    'Conectar la ficha del paquete 11.1 con su control en el cronograma: G13 exige versión probada en PREPROD, datos ficticios y material antes de iniciar los 40 días hábiles de A13 (10 de familiarización y 30 prácticos). Sin G13 disponible, A13 no comienza.',
    60,
    3,
)

# 12. s12 — Cronograma E1/E2 y Nivelación de Recursos (90 s · S3 §3.2.4 · S7 §7.2–7.3 · T-15 · T-18)
v = ''
# Escala 100% proporcional M1..M24: x = 290 + (m - 1) * 48 (M1=290, M24=1394), más bloque M25->M56 (1420..1690)
def m_x(m):
    return 290 + int((m - 1) * 48)

v += group(
    card(20, 18, 1688, 432, CARD_BG, STROKE, 16, C)
    + text(45, 58, 'PISTA / ETAPA', 22, C, 700)
    + badge(1425, 32, 'OPERACIÓN → M56', C, '#e7f3f6', 255, 34, 19),
    0,
)
for m in [1, 4, 7, 10, 13, 16, 19, 21, 24]:
    xm = m_x(m)
    is_prod = m in (16, 21)
    v += group(
        line(xm, 72, xm, 432, AMBER if is_prod else '#cadbe1', 2 if is_prod else 1, dash='5 5' if is_prod else '')
        + text(xm, 58, f'M{m}', 21, AMBER if is_prod else MUTED, 700 if is_prod else 500, 'middle'),
        0,
    )

gantt_tracks = [
    ('01 · Construcción E1', 1, 12, 92, C, 'Diseño, borde y core E1', '', 0),
    ('02 · Marcha Blanca E1', 13, 15, 148, AMBER, 'M13–M15', '3 m validación (H6)', 0),
    ('03 · Producción E1', 16, 24, 204, C, 'Aceptación H7 en M16', '', 1),
    ('04 · Construcción E2', 13, 18, 260, '#087d70', 'Analítica e integraciones E2', '', 1),
    ('05 · Marcha Blanca E2', 19, 20, 316, AMBER, 'M19–20', '2 m validación (H11)', 1),
    ('06 · Producción E2', 21, 24, 372, C, 'Aceptación H12', '', 1),
]
for label_t, m_ini, m_fin, y_t, col_t, bar_txt, out_txt, st_t in gantt_tracks:
    x1 = m_x(m_ini)
    x2 = m_x(m_fin) + 42
    bw = x2 - x1
    v += group(
        text(45, y_t + 25, label_t, 23, WHITE, 600)
        + rect_bar(x1, y_t, bw, 34, col_t, 10, grow_x=True)
        + text(x1 + bw / 2 if out_txt else x1 + 14, y_t + 24, bar_txt, 18 if out_txt else 19, '#ffffff', 700, 'middle' if out_txt else 'start')
        + (text(x2 + 14, y_t + 24, out_txt, 19, col_t, 600) if out_txt else ''),
        st_t,
    )
    if m_fin == 24:
        # Cola hacia M56 para las pistas de producción
        v += group(
            rect_bar(1445, y_t, 235, 34, '#e7f0f3', 10, grow_x=True, stroke=C)
            + text(1562, y_t + 24, 'Continúa → M56', 19, C, 600, 'middle'),
            2,
        )

# Panel inferior: Convivencia del Legado (M1-M24) y Nivelación de Recursos en el solapamiento M13-M15 (T-15)
v += group(
    card(20, 466, 820, 164, CARD_ALT, STROKE, 14, C)
    + badge(46, 486, 'S3 §3.2.4 · CONVIVENCIA DEL LEGADO 2013', C, '#e7f3f6', 415, 32, 18)
    + text(46, 548, 'Sustitución progresiva por funciones (M1 a M21)', 26, WHITE, 600)
    + text(46, 582, '• M16–M20: E1 opera en producción mientras E2 entra en marcha blanca.', 20, MUTED)
    + text(46, 612, '• Hasta M24: Sistema 2013 en consulta histórica; ERP sigue como emisor.', 20, C)
    + card(865, 466, 843, 164, CARD_ALT, STROKE, 14, AMBER)
    + badge(891, 486, 'S7 §7.2 · T-15: NIVELACIÓN DE CAPACIDAD (M13–M15)', AMBER, '#fff0d7', 495, 32, 18)
    + text(891, 548, 'Partición de equipos sin sobreasignación en solapamiento:', 26, WHITE, 600)
    + text(891, 582, '• Célula Alfa: Marcha blanca y soporte E1  |  Célula Beta: Construcción E2.', 20, AMBER)
    + text(891, 612, '• Especialista de Seguridad e Integración: 1,0 FTE dedicado sin doble cómputo.', 20, MUTED),
    2,
)
add(
    'La transición se ejecuta en dos etapas niveladas.',
    'CRONOGRAMA Y CAPACIDAD / S3 §3.2.4 · S7 §§7.2–7.3 · T-15 · T-18',
    v,
    'S3 §3.2.4 · S7 §§7.2–7.3 · T-15: nivelación Células Alfa/Beta · T-18: etapas E1/E2 y legado hasta M24',
    'Explicar el cronograma en escala proporcional M1–M24 con extensión a M56: E1 entra a marcha blanca en M13–M15 y producción en M16; E2 hace marcha blanca en M19–M20 y producción en M21. Destacar la partición en Células Alfa y Beta durante M13–M15 para evitar sobreasignación.',
    90,
    3,
)

# 13. s13 — Compuertas de Aceptación, Hitos y Reservas de Red (90 s · S7 §7.3.1 · T-15 · T-18)
v = ''
# Línea de tiempo central en y = 225
v += group(
    line(110, 225, 1610, 225, '#bdced6', 6)
    + line(110, 225, 1610, 225, C, 6, draw=True),
    0,
)
gates_s13 = [
    ('G13', 'M10*', 'Compuerta Pre-A13', 'PREPROD + datos + material', 'Día 182 línea base', 155, True, C, 0),
    ('H6', 'M13', 'Inicio MB Etapa 1', '40d capacitación cumplidos', 'Apertura controlada E1', 510, False, C, 0),
    ('H7', 'M16', 'Aceptación Etapa 1', 'Producción E1 autorizada', 'Cierre formal MB E1', 865, True, AMBER, 1),
    ('H11', 'M19', 'Inicio MB Etapa 2', 'E1 estable en producción', 'Apertura controlada E2', 1220, False, C, 1),
    ('H12', 'M21', 'Aceptación Final', 'Producción completa E1+E2', 'Paso a operación M56', 1575, True, AMBER, 1),
]
for code, m_lbl, title_g, sub1, sub2, xg, is_top, col_g, st_g in gates_s13:
    cy_card = 28 if is_top else 272
    line_y1 = 188 if is_top else 225
    line_y2 = 225 if is_top else 272
    v += group(
        line(xg, line_y1, xg, line_y2, col_g, 3, draw=True)
        + circle(xg, 225, 18, col_g, col_g, pulse=True)
        + card(xg - 135, cy_card, 270, 158, CARD_BG, STROKE, 14, col_g, accent_top=True)
        + text(xg - 112, cy_card + 48, code, 34, col_g, 700)
        + badge(xg + 15, cy_card + 20, m_lbl, col_g, '#e7f3f6' if col_g == C else '#fff0d7', 98, 34, 19)
        + text(xg - 112, cy_card + 88, title_g, 23, WHITE, 600)
        + text(xg - 112, cy_card + 118, sub1, 17.5, MUTED)
        + text(xg - 112, cy_card + 144, sub2, 18, col_g, 500),
        st_g,
    )

# Amortiguadores / Reservas de red (A14 y A23) y Regla de Gobierno
v += group(
    rect_bar(240, 208, 185, 34, '#e7f0f3', 10, grow_x=True, stroke=C)
    + text(332, 231, 'Reserva A14: 14 d', 19, C, 700, 'middle')
    + rect_bar(950, 208, 185, 34, '#e7f0f3', 10, grow_x=True, stroke=C)
    + text(1042, 231, 'Reserva A23: 10 d', 19, C, 700, 'middle')
    + card(20, 456, 1688, 174, CARD_ALT, STROKE, 16, AMBER)
    + badge(48, 480, 'S7 §7.3.1 · REGLA DE GOBIERNO DEL CRONOGRAMA', AMBER, '#fff0d7', 465, 34, 19)
    + text(540, 505, 'Fecha contractual de hito  ≠  Holgura interna de la red', 34, AMBER, 700)
    + text(48, 558, '• Una holgura en actividades internas o el uso de las reservas A14 (14 d) y A23 (10 d) no autoriza desplazar H7 (M16) ni H12 (M21).', 25, WHITE)
    + text(48, 598, '• Rigor documental: las reservas están modeladas en la red determinista T-15; no se reclama validación probabilística Monte Carlo.', 23, MUTED),
    2,
)
add(
    'Los hitos avanzan por evidencia y protegen fechas.',
    'PLANIFICACIÓN / COMPUERTAS, HITOS Y RESERVAS · S7 §7.3.1 · T-15 · T-18',
    v,
    'S7 §7.3.1 · T-15: G13 y reservas A14 (14 d) / A23 (10 d) · T-18: hitos H6, H7, H11 y H12',
    'Explicar la cadena de compuertas e hitos: G13 habilita capacitación, H6 y H11 abren las marchas blancas, y H7/H12 formalizan la aceptación. Distinguir claramente entre fecha contractual de hito, holgura de actividad y las reservas explícitas A14 (14 días) y A23 (10 días).',
    90,
    3,
)

# 14. s14 — Cierre: Compromisos Verificables de la Propuesta (45 s · Síntesis Integral)
v = ''
pillars_s14 = [
    (
        '01',
        'SOLUCIÓN Y TRAZABILIDAD',
        'Arquitectura y Correcciones',
        'S3 · S4 · S5 · T-11 · T-12',
        [
            ('Salida bloqueante', 'Conductor + Vehículo + DTE verificados'),
            ('Borde y nube', '374 gateways, 61 CANclick, buffer 8 GB'),
            ('Legado 2013', 'Sustitución funcional; consulta a M24'),
            ('Evidencia', 'Cadena RNF-011 → 11.2 → CP-INT/SYS-05'),
        ],
        C,
        20,
    ),
    (
        '02',
        'RIESGOS Y CALIDAD',
        'Mitigación y Umbrales',
        'S6 · S8 · S9 · T-13 · T-16 · T-17',
        [
            ('Método P×I', 'Reducción 12→8 (R-28/R-11) y 8→4 (R-16)'),
            ('Ruta R-28', 'Presupuesto 90 s bajo protocolo de ensayo'),
            ('AMFE técnico', 'NPR ≤ 36 (< umbral 50) con autodetección'),
            ('Calidad S6/S9', '120 casos ISO 29119 · ≤ 5 % cambio fallido'),
        ],
        C,
        596,
    ),
    (
        '03',
        'EJECUCIÓN CONTROLADA',
        'EDT, Cronograma y Compuertas',
        'S7 · S13 · T-14 · T-15 · T-18 · T-19',
        [
            ('Alcance EDT', '54 paquetes en 13 áreas + 5 fichas T-19'),
            ('Compuerta G13', 'Requisito bloqueante para 40 d de A13'),
            ('Dos etapas', 'Producción E1 en M16 y E2 en M21 → M56'),
            ('Capacidad', 'Células Alfa/Beta + reservas A14 y A23'),
        ],
        AMBER,
        1172,
    ),
]
for idx, (num, badge_t, title_p, forms_p, bullets, col_p, xp) in enumerate(pillars_s14):
    card_content = (
        card(xp, 24, 535, 515, CARD_BG, STROKE, 16, col_p, accent_top=True)
        + text(xp + 28, 98, num, 58, col_p, 700)
        + badge(xp + 125, 52, badge_t, col_p, '#e7f3f6' if col_p == C else '#fff0d7', 380, 34, 18)
        + text(xp + 28, 152, title_p, 34, WHITE, 600)
        + text(xp + 28, 186, forms_p, 21, col_p, 600)
        + line(xp + 28, 206, xp + 505, 206, STROKE, 1.5)
    )
    for b_i, (b_head, b_desc) in enumerate(bullets):
        by = 252 + b_i * 70
        card_content += (
            circle(xp + 42, by - 8, 6, col_p, col_p)
            + text(xp + 64, by, b_head + ':', 24, WHITE, 600)
            + text(xp + 64, by + 30, b_desc, 21, MUTED)
        )
    v += group(card_content, idx)
    if idx < 2:
        v += group(arrow(xp + 539, 275, xp + 592, 275, C, 3.5, draw=True), idx + 1)

v += group(
    card(20, 556, 1688, 74, CARD_ALT, STROKE, 14, C)
    + text(48, 601, 'Compromiso de defensa técnica: trazabilidad documental íntegra, sin promesas fuera de los formularios T-9 a T-19.', 23.5, WHITE, 600)
    + badge(1448, 574, '14:25 + 0:35 MARGEN', AMBER, '#fff0d7', 240, 36, 18),
    2,
)
add(
    'La propuesta vincula arquitectura, riesgos y control.',
    'CIERRE / COMPROMISOS VERIFICABLES DE LA PROPUESTA',
    v,
    'Síntesis integral Informe 2: S2–S9 y S13 · Formularios T-9 a T-19',
    'Cerrar sintetizando los tres pilares verificables de la propuesta: arquitectura y correcciones trazables, riesgos y calidad con umbrales explícitos, y ejecución controlada por compuertas y reservas. Queda abierta la sesión de preguntas con apoyo del respaldo técnico.',
    45,
    3,
)

# Cierre de la exposición, después de la síntesis técnica.
v = group(
    text(24, 192, 'Preguntas y discusión', 82, WHITE, 700)
    + text(28, 278, '15 minutos para revisar decisiones, riesgos e hitos.', 38, C, 500)
    + line(28, 330, 1660, 330, STROKE, 3, draw=True)
    + text(28, 416, 'Riesgos', 32, AMBER, 600)
    + text(28, 459, 'Solución · desarrollo · implantación', 27, MUTED)
    + text(600, 416, 'Planificación', 32, AMBER, 600)
    + text(600, 459, 'EDT · compuertas · hitos', 27, MUTED)
    + text(1130, 416, 'Evidencia', 32, AMBER, 600)
    + text(1130, 459, 'Formularios y pruebas trazables', 27, MUTED)
    + badge(28, 540, 'audIT · Soluciones Tecnológicas SpA', C, '#e7f3f6', 550, 44, 22),
    0,
)
add(
    'Preguntas y discusión',
    'CIERRE / REVISIÓN 2',
    v,
    'Transportes Curimón · TFEP-01/2026 · audIT Soluciones Tecnológicas SpA',
    'Abrir los 15 minutos de preguntas. Usar el respaldo técnico para profundizar en riesgos, trazabilidad, cronograma y criterios de aceptación.',
    10,
    1,
    kind='closing',
)

# ==============================================================================
# RESPALDO TÉCNICO (14 DIAPOSITIVAS: s15 a s28 — ACCESO CON TECLA 'B')
# ==============================================================================

# s15 (Respaldo 01) — Alcance y fronteras de la verificación (Grilla 2x2)
v = ''
limits_s15 = [
    ('01 · VERIFICACIÓN DOCUMENTAL', 'Cotejo de observaciones y trazabilidad', 'Se verificó Obs. 37, 43 y cadena RNF-011 en S3, T-12, T-14 y T-17.', 'No equivale a una auditoría de cumplimiento total de pliego.', 20, 26, C, 0),
    ('02 · PROTOCOLOS DE PRUEBA (T-17)', 'Diseño acreditado vs. ejecución futura', '120 casos (incluidos CP-INT-05 y CP-SYS-05) con diseño y criterios.', 'La ejecución y actas de resultado ocurren en etapa contractual.', 874, 26, AMBER, 1),
    ('03 · MODELO DE CRONOGRAMA (T-15)', 'Red determinista con reservas explícitas', 'Incorpora reservas A14 (14 d), A23 (10 d) y Células Alfa y Beta.', 'No se reclama validación probabilística Monte Carlo en esta vista.', 20, 336, C, 1),
    ('04 · CALENDARIO CONTRACTUAL (T-18)', 'Meses relativos al hito de inicio', 'Los hitos M10, M13, M16, M19, M21, M24 y M56 son meses relativos.', 'Las fechas calendario definitivas se fijan al firmar el inicio.', 874, 336, AMBER, 2),
]
for tag, title_l, desc1, desc2, xl, yl, col_l, st_l in limits_s15:
    v += group(
        card(xl, yl, 834, 286, CARD_BG, STROKE, 16, col_l, accent_top=True)
        + badge(xl + 28, yl + 30, tag, col_l, '#e7f3f6' if col_l == C else '#fff0d7', 360, 34, 19)
        + text(xl + 28, yl + 114, title_l, 33, WHITE, 600)
        + text(xl + 28, yl + 168, desc1, 23, MUTED)
        + line(xl + 28, yl + 204, xl + 800, yl + 204, STROKE, 1.5)
        + text(xl + 28, yl + 248, 'Límite: ' + desc2, 22, col_l, 600),
        st_l,
    )
add(
    'La evidencia mantiene límites metodológicos explícitos.',
    'RESPALDO 01 / ALCANCE Y FRONTERAS DE VERIFICACIÓN',
    v,
    'S3 · S7 · S8 · T-12 / T-15 / T-17 / T-18',
    'Usar ante preguntas sobre el alcance de las afirmaciones: distinguimos con rigor entre diseño documental verificado y resultados de ejecución en terreno.',
    45,
    3,
    backup=True,
)

# s16 (Respaldo 02) — Gobierno del riesgo: dueños, disparadores y contingencias (3 columnas)
v = ''
gov_s16 = [
    ('R-28', 'Solución en Ruta', 'Documento sin cobertura', 'Líder de Integración', '12 → 8', 'Retorno DTE > 90 s o pérdida de fragmentos en pruebas de sombra.', 'Pre-emisión en planta + buffer firmado en cabina + bloqueo preventivo.', 20, C, 0),
    ('R-16', 'Desarrollo y Red', 'Capacitación y plazo A13', 'Jefe de Proyecto', '8 → 4', 'Compuerta G13 incompleta al día 182 o consumo > 50 % de reserva A14.', 'Congelamiento PREPROD anticipado + cápsulas por perfil + uso controlado A14.', 596, AMBER, 1),
    ('R-11', 'Implantación E1', 'Adhesión transportistas', 'Líder Funcional', '12 → 8', '59 o menos anexos firmados y validados (sobre 148) al cierre de M9.', 'Mesa de soporte jurídico/operativo + enrolamiento asistido en terminales.', 1172, C, 2),
]
for rcode, ambito, rtitle, owner, exp_s, trig, cont, xg, col_g, st_g in gov_s16:
    trig_lines = textwrap.wrap(trig, width=38)
    cont_lines = textwrap.wrap(cont, width=38)
    v += group(
        card(xg, 24, 535, 602, CARD_BG, STROKE, 16, col_g, accent_top=True)
        + text(xg + 28, 96, rcode, 54, col_g, 700)
        + badge(xg + 175, 52, ambito.upper(), col_g, '#e7f3f6' if col_g == C else '#fff0d7', 235, 34, 18)
        + badge(xg + 420, 52, exp_s, WHITE, '#e7f0f3', 90, 34, 18)
        + text(xg + 28, 148, rtitle, 33, WHITE, 600)
        + card(xg + 28, 178, 478, 86, CARD_ALT, STROKE, 12, col_g)
        + text(xg + 48, 212, 'DUEÑO DEL RIESGO', 19, col_g, 700)
        + text(xg + 48, 244, owner, 26, WHITE, 600)
        + card(xg + 28, 282, 478, 145, CARD_ALT, STROKE, 12, AMBER)
        + text(xg + 48, 318, 'DISPARADOR DE ACTIVACIÓN (TRIGGER)', 19, AMBER, 700)
        + ''.join(text(xg + 48, 356 + k * 32, l_str, 22, WHITE) for k, l_str in enumerate(trig_lines[:2]))
        + card(xg + 28, 445, 478, 152, CARD_ALT, STROKE, 12, C)
        + text(xg + 48, 481, 'PLAN DE RESPUESTA Y CONTINGENCIA', 19, C, 700)
        + ''.join(text(xg + 48, 519 + k * 32, l_str, 22, MUTED) for k, l_str in enumerate(cont_lines[:2])),
        st_g,
    )
add(
    'Cada riesgo crítico tiene dueño, umbral y respuesta.',
    'RESPALDO 02 / GOBIERNO OPERACIONAL DEL RIESGO · T-16',
    v,
    'T-16: registro de riesgos R-28, R-16 y R-11 con responsables y disparadores cuantitativos',
    'Respaldo directo para preguntas de gobernanza de riesgos: muestra quién responde, qué umbral numérico dispara la alerta y qué contingencia se activa en cada ámbito.',
    45,
    3,
    backup=True,
)

# s17 (Respaldo 03) — Portafolio de 5 Innovaciones (S13 / T-19) y Madurez TRL
v = ''
v += group(
    card(20, 18, 1688, 78, CARD_ALT, STROKE, 12, C)
    + badge(44, 36, 'SECCIÓN 13 · FORMULARIO T-19', C, '#e7f3f6', 320, 34, 19)
    + text(390, 66, '5 Paquetes de Innovación (EDT 12.1 a 12.5) · Piloto M13–M15 · Despliegue M16', 29, WHITE, 600),
    0,
)
inno_rows = [
    ('12.1', 'Analítica Predictiva de Mantenimiento', 'TRL 8 Comp. / TRL 6 Integ.', 'Modelos sobre telemetría CAN J1939 para anticipar fallas.', 'Sujeto a historial limpio de 6 meses', 0),
    ('12.2', 'Gemelo Digital de Red Logística', 'TRL 7 Comp. / TRL 6 Integ.', 'Simulación de cuellos de botella en 5 terminales.', 'Calibración durante marcha blanca E1', 0),
    ('12.3', 'Visión Artificial DMS en Cabina', 'TRL 8 Comp. / TRL 7 Integ.', '225 cámaras de fatiga y distracción con alerta local.', 'Validación de falsos positivos en ruta', 1),
    ('12.4', 'Asistente Operacional IA Generativa', 'TRL 7 Comp. / TRL 6 Integ.', 'Consulta rápida de procedimientos y anomalías en torre.', 'Modo asistido; no toma decisiones autónomas', 1),
    ('12.5', 'Red Conectada de Paradores Seguros', 'TRL 8 Comp. / TRL 6 Integ.', 'Reserva y control de descanso en ruta (RN-03).', 'Dependiente de convenios con paradores', 2),
]
for idx, (code_i, name_i, trl_i, desc_i, cond_i, st_i) in enumerate(inno_rows):
    y = 112 + idx * 102
    col_i = AMBER if idx in (1, 2) else C
    v += group(
        card(20, y, 1688, 88, CARD_BG, STROKE, 12, col_i)
        + text(48, y + 54, code_i, 34, col_i, 700)
        + text(155, y + 42, name_i, 27, WHITE, 600)
        + text(155, y + 72, desc_i, 22, MUTED)
        + badge(885, y + 24, trl_i, col_i, '#e7f3f6' if col_i == C else '#fff0d7', 295, 38, 19)
        + text(1210, y + 52, cond_i, 22, WHITE, 500),
        st_i,
    )
add(
    'Las cinco innovaciones distinguen TRL y condiciones.',
    'RESPALDO 03 / DETALLE DE INNOVACIONES S13 · FORMULARIO T-19',
    v,
    'S13 · T-19: fichas de innovación 12.1 a 12.5, niveles TRL y supuestos de validación',
    'Usar ante consultas sobre la Sección 13 (Innovaciones): detalla los 5 paquetes del área 12 de la EDT, diferenciando la madurez comercial del componente respecto del TRL de integración en Curimón.',
    45,
    3,
    backup=True,
)

# s18 (Respaldo 04) — Árbol de Fallas de Verificación Bloqueante (Compuertas OR y AND vectoriales)
v = ''
# Evento Tope + Compuerta Lógica OR en (864, 175)
v += group(
    card(404, 18, 920, 88, CARD_BG, STROKE, 14, AMBER, accent_top=True)
    + badge(432, 42, 'EVENTO TOPE NO DESEADO', AMBER, '#fff0d7', 275, 34, 18)
    + text(730, 68, 'Viaje asignado a conductor no apto', 31, WHITE, 700)
    + line(864, 106, 864, 138, AMBER, 3.5)
    # Compuerta OR vectorial
    + f'<path d="M 824 138 Q 864 122 904 138 Q 904 178 864 202 Q 824 178 824 138 Z" fill="#fff0d7" stroke="{AMBER}" stroke-width="3"/>'
    + text(864, 172, 'OR', 20, AMBER, 700, 'middle')
    + line(864, 202, 864, 226, '#bdced6', 3.5)
    + line(215, 226, 1513, 226, '#bdced6', 3.5, draw=True),
    0,
)
fault_branches = [
    ('CAMINO 01', 'Registro incompleto', 'aceptado como válido', 'Falla validación + sin alerta', 20, 215, 0),
    ('CAMINO 02', 'Excepción RN-04', 'aplicada sin respaldo', 'Override manual + falta auditoría', 452, 647, 1),
    ('CAMINO 03', 'Terminal sin enlace', 'asigna localmente', 'Corte WAN + caché desactualizado', 884, 1079, 1),
    ('CAMINO 04', 'Conductor externo', 'sin evidencia vigente', 'Portal desincronizado + control omitido', 1316, 1511, 2),
]
for tag_f, l1, l2, and_desc, xf, cxf, st_f in fault_branches:
    v += group(
        line(cxf, 226, cxf, 256, C, 3)
        # Compuerta AND vectorial en cada rama
        + f'<path d="M {cxf - 32} 256 L {cxf + 32} 256 L {cxf + 32} 282 A 32 24 0 0 1 {cxf - 32} 282 Z" fill="#e7f3f6" stroke="{C}" stroke-width="2.5"/>'
        + text(cxf, 284, 'AND', 17, C, 700, 'middle')
        + line(cxf, 306, cxf, 330, C, 3)
        + card(xf, 330, 392, 182, CARD_BG, STROKE, 14, C, accent_top=True)
        + badge(xf + 22, 352, tag_f, C, '#e7f3f6', 148, 30, 17)
        + text(xf + 22, 412, l1, 28, WHITE, 600)
        + text(xf + 22, 446, l2, 25, C, 500)
        + text(xf + 22, 488, and_desc, 20, MUTED),
        st_f,
    )
v += group(
    card(20, 534, 1688, 94, CARD_ALT, STROKE, 14, C)
    + text(48, 574, 'Defensa en profundidad: cada camino exige que fallen simultáneamente dos barreras independientes (compuerta AND).', 26, WHITE, 600)
    + text(48, 610, 'Rigor S8 §8.2: análisis lógico cualitativo para diseñar pruebas en paralelo; no se inventan probabilidades empíricas sin historial.', 22, MUTED),
    2,
)
add(
    'El árbol de fallas modela compuertas OR y AND.',
    'RESPALDO 04 / ÁRBOL DE FALLAS DE VERIFICACIÓN BLOQUEANTE · S8 §8.2',
    v,
    'S8 §8.2: árbol de fallas con compuerta OR superior y cuatro compuertas AND inferiores',
    'Explicar la estructura lógica del árbol de fallas de S8 §8.2: el evento tope ocurre por una compuerta OR superior alimentada por cuatro ramas, donde cada rama requiere la conjunción (compuerta AND) de una falla técnica y una falla de control.',
    45,
    3,
    backup=True,
)

# s19 (Respaldo 05) — Procedimiento de Reversión en 4 Pasos (T-18)
v = ''
rev_steps = [
    ('01', 'Detectar', '15 min', 'Incidente crítico S1 o discrepancia de datos en marcha blanca.', 'Guardia SRE / Monitoreo Torre', C, 20, 0),
    ('02', 'Decidir', '30 min', 'Evaluación en comité operativo con contraparte Curimón informada.', 'Jefe de Proyecto + Líder Operación', AMBER, 448, 1),
    ('03', 'Revertir', '15m + 20m/camión', 'Conmutación de tráfico a versión previa y resincronización.', 'Ingeniero SRE + Soporte Terreno', C, 876, 1),
    ('04', 'Conciliar', '24 h / 5 días', 'Cuadratura de viajes y DTE en 24 h; informe causal en 5 días hábiles.', 'Líder de Datos + Operación', AMBER, 1304, 2),
]
for num_r, title_r, sla_r, desc_r, role_r, col_r, xr, st_r in rev_steps:
    w_lines = textwrap.wrap(desc_r, width=30)
    v += group(
        card(xr, 36, 404, 465, CARD_BG, STROKE, 16, col_r, accent_top=True)
        + text(xr + 26, 108, num_r, 56, col_r, 700)
        + badge(xr + 125, 64, sla_r, col_r, '#e7f3f6' if col_r == C else '#fff0d7', 252, 38, 19)
        + text(xr + 26, 168, title_r, 38, WHITE, 600)
        + line(xr + 26, 194, xr + 378, 194, STROKE, 1.5)
        + ''.join(text(xr + 26, 244 + k * 34, line_s, 24, WHITE) for k, line_s in enumerate(w_lines))
        + card(xr + 24, 378, 356, 98, CARD_ALT, STROKE, 12, col_r)
        + text(xr + 44, 414, 'RESPONSABLE', 19, col_r, 700)
        + text(xr + 44, 450, role_r, 19.5, MUTED, 600),
        st_r,
    )
    if xr < 1300:
        v += group(arrow(xr + 408, 268, xr + 444, 268, C, 3.5, draw=True), st_r)

v += group(
    card(20, 526, 1688, 102, CARD_ALT, STROKE, 14, AMBER)
    + badge(48, 548, 'NOTA METODOLÓGICA T-18', AMBER, '#fff0d7', 280, 34, 18)
    + text(350, 572, 'Ventanas operativas de procedimiento; no deben sumarse como RTO único ni declararse como prueba ya ejecutada.', 23, WHITE, 600)
    + text(48, 610, 'Durante la reversión, el ERP contable mantiene la continuidad de emisión tributaria sin pérdida de folios.', 23, MUTED),
    2,
)
add(
    'La reversión opera con tiempos y roles definidos.',
    'RESPALDO 05 / PROCEDIMIENTO DE REVERSIÓN · FORMULARIO T-18',
    v,
    'T-18: procedimiento de reversión en 4 fases (15 min, 30 min, 15 min + 20 min/camión, 24 h / 5 d)',
    'Detallar el protocolo de reversión de T-18 en cuatro pasos con sus ventanas operativas y responsables, advirtiendo que no deben sumarse como un RTO único.',
    45,
    3,
    backup=True,
)

# s20 a s28 (Respaldos 06 a 14) — Diccionario Completo EDT (Paquetes 1 al 54, sin colisiones)
with (ROOT / 'Informe-2/d2/03_Apoyo/Diccionario_EDT.csv').open(encoding='utf-8-sig', newline='') as f:
    packages = list(csv.DictReader(f))

for page_idx, offset in enumerate(range(0, len(packages), 6)):
    v = (
        card(10, 8, 1708, 52, '#e7f3f6', STROKE, 10)
        + text(34, 43, 'CÓDIGO', 24, C, 700)
        + text(195, 43, 'PAQUETE DE TRABAJO (T-14)', 24, C, 700)
        + text(1135, 43, 'ROL RESPONSABLE', 24, C, 700)
    )
    for j, p in enumerate(packages[offset:offset + 6]):
        row_top = 70 + j * 94
        row_bg = CARD_BG if j % 2 == 0 else CARD_ALT
        v += card(10, row_top, 1708, 86, row_bg, STROKE, 10, C if j % 2 == 0 else None)
        v += badge(30, row_top + 24, p['codigo'], C, '#e7f3f6', 110, 38, 22)
        name_lines = textwrap.wrap(p['nombre'], width=42)
        role_lines = textwrap.wrap(p['responsable'], width=32)
        for k, value in enumerate(name_lines[:2]):
            ty = (row_top + 52) if len(name_lines) == 1 else (row_top + 38 + k * 30)
            v += text(195, ty, value, 27, WHITE, 500)
        for k, value in enumerate(role_lines[:2]):
            ty = (row_top + 52) if len(role_lines) == 1 else (row_top + 38 + k * 30)
            v += text(1135, ty, value, 25, MUTED, 500)
    v = group(v, 0)
    add(
        f'La EDT detalla sus paquetes ({offset + 1}–{min(offset + 6, len(packages))}).',
        f'RESPALDO {page_idx + 6:02} / DICCIONARIO EDT · T-14',
        v,
        'T-14 · Diccionario_EDT.csv: catálogo completo de paquetes de trabajo',
        'Los criterios de aceptación completos permanecen en T-14 y en el diccionario CSV. Esta vista paginada permite localizar cualquier paquete durante las preguntas de la comisión.',
        seconds=30,
        steps=1,
        backup=True,
    )

css = '''*{box-sizing:border-box}html,body{margin:0;width:100%;height:100%;overflow:hidden;background:#ffffff;color:#102d3e;font-family:system-ui,sans-serif}body{position:relative}#stage{width:1920px;height:1080px;position:absolute;transform-origin:0 0}.scene{position:absolute;inset:0;width:100%;height:100%;overflow:hidden;background:#ffffff;opacity:0;visibility:hidden;pointer-events:none}.scene::after{content:"";position:absolute;left:96px;right:96px;bottom:104px;height:1px;background:#bdced6}.eyebrow{position:absolute;left:96px;top:62px;font-size:23px;letter-spacing:.15em;color:#006b7d;font-weight:600}.brand{position:absolute;right:96px;top:49px;width:142px;height:54px;object-fit:contain}.headline{position:absolute;left:96px;top:132px;width:1710px;font-size:68px;line-height:1.1;font-weight:600;letter-spacing:-.035em;margin:0}.visual{position:absolute;left:96px;top:296px;width:1728px;height:650px;overflow:visible;font-family:system-ui,sans-serif}.source{position:absolute;left:96px;bottom:54px;font-size:19px;color:#48606e;max-width:1540px}.folio{position:absolute;right:96px;bottom:52px;font-size:23px;color:#48606e}.scene.cover .headline,.scene.operational .headline,.scene.closing .headline{display:none}.scene.cover .visual,.scene.operational .visual,.scene.closing .visual{top:215px}.scene.cover .eyebrow,.scene.operational .eyebrow,.scene.closing .eyebrow{top:118px}.scene.cover .brand,.scene.operational .brand,.scene.closing .brand{top:100px;width:220px;height:80px}@media(prefers-reduced-motion:reduce){*{scroll-behavior:auto}}'''

manifest = {'slides': [], 'slideSequences': [{'id': 'respaldo', 'label': 'Respaldo técnico', 'slides': []}]}
sections = []
for i, s in enumerate(SLIDES):
    start = i * 10
    ref = dict(sceneId=s['id'], notes=s['notes'], fragments=[start + 1 + 2 * j for j in range(s['steps'])])
    (manifest['slideSequences'][0]['slides'] if s['backup'] else manifest['slides']).append(ref)
    sections.append(
        f'''<div id="{s['id']}" class="scene {s['kind']}" data-composition-id="{s['id']}" data-start="{start}" data-duration="10" data-width="1920" data-height="1080"><section class="clip" data-start="0" data-duration="10" data-track-index="1"><div class="eyebrow">{s['eyebrow']}</div><img class="brand" src="../assets/logo-audit.png" alt="audIT"><h1 class="headline">{s['title']}</h1>{s['content']}<div class="source">{s['source']}</div><div class="folio">{('R' + str(i - sum(not x['backup'] for x in SLIDES) + 1)) if s['backup'] else str(i + 1).zfill(2)}</div></section></div>'''
    )

js = '''window.__timelines=window.__timelines||{};
const scenes=Array.from(document.querySelectorAll('.scene'));
const master=gsap.timeline({paused:true});
const flowLoops=[];
const truckLoops=[];
scenes.forEach((scene,i)=>{
  const tl=gsap.timeline({paused:true});
  scene.querySelectorAll('[data-step]').forEach(el=>{
    const at=Number(el.dataset.step)*2;
    tl.fromTo(el,{opacity:0,y:22},{opacity:1,y:0,duration:.78,ease:'power2.out'},at);
    el.querySelectorAll('[data-draw]').forEach(d=>{
      const len=Number(d.dataset.draw)||600;
      d.style.strokeDasharray=String(len);
      tl.fromTo(d,{strokeDashoffset:len},{strokeDashoffset:0,duration:.72,ease:'power2.inOut'},at+.04);
    });
    el.querySelectorAll('[data-grow-x]').forEach(bar=>{
      const bx=Number(bar.getAttribute('x'))||0;
      const by=Number(bar.getAttribute('y'))||0;
      const bh=Number(bar.getAttribute('height'))||0;
      gsap.set(bar,{svgOrigin:`${bx} ${by+bh/2}`});
      tl.fromTo(bar,{scaleX:0},{scaleX:1,duration:.72,ease:'expo.out'},at+.05);
    });
    el.querySelectorAll('[data-grow-y]').forEach(bar=>{
      const bx=Number(bar.getAttribute('x'))||0;
      const by=Number(bar.getAttribute('y'))||0;
      const bw=Number(bar.getAttribute('width'))||0;
      const bh=Number(bar.getAttribute('height'))||0;
      gsap.set(bar,{svgOrigin:`${bx+bw/2} ${by+bh}`});
      tl.fromTo(bar,{scaleY:0},{scaleY:1,duration:.72,ease:'power3.out'},at+.05);
    });
    el.querySelectorAll('[data-slide-from-x]').forEach(node=>{
      const dx=Number(node.dataset.slideFromX)||0;
      tl.fromTo(node,{x:dx},{x:0,duration:.74,ease:'power3.inOut'},at+.04);
    });
    el.querySelectorAll('[data-pulse]').forEach(p=>{
      const cx=Number(p.getAttribute('cx'))||0;
      const cy=Number(p.getAttribute('cy'))||0;
      if(cx||cy)gsap.set(p,{svgOrigin:`${cx} ${cy}`});
      tl.fromTo(p,{scale:0.25},{scale:1,duration:.68,ease:'back.out(2.1)'},at+.06);
    });
    el.querySelectorAll('[data-ring-circ]').forEach(ring=>{
      const circ=Number(ring.dataset.ringCirc)||540;
      const target=Number(ring.dataset.ringOffset)||120;
      tl.fromTo(ring,{strokeDashoffset:circ},{strokeDashoffset:target,duration:.74,ease:'power2.out'},at+.04);
    });
    el.querySelectorAll('[data-count-to]').forEach(cnt=>{
      const target=Number(cnt.dataset.countTo)||0;
      const prefix=cnt.dataset.countPrefix||'';
      const suffix=cnt.dataset.countSuffix||'';
      const proxy={v:0};
      tl.fromTo(proxy,{v:0},{v:target,duration:.72,ease:'power2.out',onUpdate:()=>{
        cnt.textContent=prefix+Math.round(proxy.v)+suffix;
      }},at+.04);
    });
  });
  scene.querySelectorAll('path[data-flow-path]').forEach((p,idx)=>{
    const svgRoot=scene.querySelector('svg');
    if(!svgRoot||typeof p.getTotalLength!=='function')return;
    const len=p.getTotalLength();
    if(!len)return;
    const dot=document.createElementNS('http://www.w3.org/2000/svg','circle');
    dot.setAttribute('r','4.5');
    dot.setAttribute('fill',p.dataset.flowColor||'#006b7d');
    dot.setAttribute('opacity','0');
    svgRoot.appendChild(dot);
    const proxy={t:0};
    const loop=gsap.to(proxy,{t:1,duration:2.2,repeat:-1,ease:'none',paused:true,delay:idx*0.45,onUpdate:()=>{
      if(document.documentElement.dataset.qa==='true'){dot.setAttribute('opacity','0');return;}
      const pt=p.getPointAtLength(proxy.t*len);
      dot.setAttribute('cx',pt.x.toFixed(1));
      dot.setAttribute('cy',pt.y.toFixed(1));
      dot.setAttribute('opacity',String(Math.sin(proxy.t*Math.PI)*0.85));
    }});
    flowLoops.push({sceneIndex:i,loop,dot});
  });
  scene.querySelectorAll('[data-moving-truck]').forEach(truck=>{
    const loop=gsap.to(truck,{x:28,y:-3,duration:1.65,repeat:-1,yoyo:true,ease:'sine.inOut',paused:true});
    truckLoops.push({sceneIndex:i,loop});
  });
  window.__timelines[scene.id]=tl;
  master.add(tl,i*10);
  tl.paused(false);
});
window.__timelines.root=master;
function fit(){
  const s=Math.min(innerWidth/1920,innerHeight/1080);
  const stage=document.getElementById('stage');
  stage.style.transform='scale('+s+')';
  stage.style.left=(innerWidth-1920*s)/2+'px';
  stage.style.top=(innerHeight-1080*s)/2+'px';
}
function visibility(t){
  const index=Math.min(scenes.length-1,Math.max(0,Math.floor(t/10)));
  const isQa=document.documentElement.dataset.qa==='true'|| window.parent?.document?.documentElement?.dataset?.qa==='true';
  scenes.forEach((s,i)=>{
    const active=i===index;
    s.style.opacity=active?'1':'0';
    s.style.visibility=active?'visible':'hidden';
    s.style.pointerEvents=active?'auto':'none';
  });
  flowLoops.forEach(f=>{
    if(f.sceneIndex===index&&!isQa){
      if(f.loop.paused())f.loop.play();
    }else{
      f.loop.pause();
      f.dot.setAttribute('opacity','0');
    }
  });
  truckLoops.forEach(f=>{
    if(f.sceneIndex===index&&!isQa){if(f.loop.paused())f.loop.play();}
    else{f.loop.pause(0);}
  });
  document.body.dataset.scene=scenes[index].id;
}
master.eventCallback('onUpdate',()=>visibility(master.time()));
window.__hfSetTime=t=>{master.seek(t,false);visibility(t)};
window.addEventListener('resize',fit);
fit();
window.__hfSetTime(1);
const timelineMessage={source:'hf-preview',type:'timeline',durationInFrames:scenes.length*300,scenes:scenes.map((s,i)=>({id:s.id,start:i*10,duration:10}))};
function postTimeline(){parent.postMessage(timelineMessage,'*')}
window.addEventListener('load',postTimeline);
postTimeline();'''

island = json.dumps(manifest, ensure_ascii=False)
raw = '<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>audIT · Revisión 2</title><script src="../assets/gsap.min.js"></script><style>' + css + '</style></head><body><script type="application/hyperframes-slideshow+json">' + island + '</script><main id="stage">' + ''.join(sections) + '</main><script>' + js + '</script></body></html>'
OUT.mkdir(exist_ok=True)
raw = raw.replace('src="../assets/', 'src="assets/')
raw = raw.replace('<main id="stage">', '').replace('</main>', '')
raw = raw.replace('window.__timelines.root=master', 'window.__hfMasterTimeline=master')
raw = raw.replace(
    "const stage=document.getElementById('stage');\n  stage.style.transform='scale('+s+')';\n  stage.style.left=(innerWidth-1920*s)/2+'px';\n  stage.style.top=(innerHeight-1080*s)/2+'px';",
    "scenes.forEach(stage=>{stage.style.width='1920px';stage.style.height='1080px';stage.style.transformOrigin='0 0';stage.style.transform='scale('+s+')';stage.style.left=(innerWidth-1920*s)/2+'px';stage.style.top=(innerHeight-1080*s)/2+'px'})",
)
(OUT / 'index.html').write_text(raw, encoding='utf-8')
import shutil
shutil.copytree(BASE / 'assets', OUT / 'assets', dirs_exist_ok=True)
(BASE / 'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding='utf-8')
wrapper = '''<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>audIT · Revisión 2 · Transportes Curimón</title><script src="assets/hyperframes-player.global.js"></script><script src="assets/hyperframes-slideshow.global.js"></script><style>*{box-sizing:border-box}html,body{margin:0;width:100%;height:100%;overflow:hidden;background:#ffffff}hyperframes-slideshow{display:block;position:relative;width:100vw;height:100vh;outline:none}hyperframes-player{position:absolute;inset:0} [data-hf-chrome]{display:none!important}#surface{position:absolute;inset:0;z-index:8;background:transparent;cursor:none}[data-hf-presenting="true"]~#surface{display:none}body:has([data-hf-presenting="true"]) #surface{display:none}body:has([data-hf-presenting="true"]) [data-hf-chrome]{display:block!important}</style></head><body><hyperframes-slideshow tabindex="0" notes-storage-key="audit-curimon-revision2"><hyperframes-player interactive src="composition/index.html"></hyperframes-player><script type="application/hyperframes-slideshow+json">''' + island + '''</script></hyperframes-slideshow><div id="surface" aria-hidden="true"></div><script src="harness.js"></script></body></html>'''
(BASE / 'index.html').write_text(wrapper, encoding='utf-8')
embedded = json.dumps(raw, ensure_ascii=False).replace('</', '<\\/')
wrapper = wrapper.replace('<title>', '<link rel="icon" href="data:,"><title>')
wrapper = wrapper.replace(' interactive src="composition/index.html"', ' interactive')
wrapper = wrapper.replace('<script src="harness.js">', '<script type="application/json" id="embedded-composition">' + embedded + '</script><script src="harness.js">')
(BASE / 'index.html').write_text(wrapper, encoding='utf-8')
(BASE / 'escenas.json').write_text(json.dumps([{k: v for k, v in s.items() if k != 'content'} for s in SLIDES], ensure_ascii=False, indent=2), encoding='utf-8')
(BASE / 'NOTAS-EXPOSICION.md').write_text(
    '# Guion de exposición\n\nObjetivo: 14 minutos y 25 segundos + 35 segundos de margen. No hay asignación ficticia de expositores.\n\n'
    + '\n\n'.join(
        f"## {i + 1}. {s['title']}\n\nTiempo: {s['seconds']} s. {'Respaldo.' if s['backup'] else ''}\n\n{s['notes']}\n\nFuente: {s['source']}"
        for i, s in enumerate(SLIDES)
    ),
    encoding='utf-8',
)
print(f'{len(manifest["slides"])} escenas principales; {len(manifest["slideSequences"][0]["slides"])} de respaldo; {sum(s["seconds"] for s in SLIDES if not s["backup"])} segundos objetivo.')
