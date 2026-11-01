"""Construye escenas vectoriales, manifiesto y notas sin modificar el informe."""
from pathlib import Path
import base64
import csv
import html
import json
import math
import textwrap

BASE = Path(__file__).resolve().parent
# Repositorio audIT: la presentación vive dentro de él (o, en copias antiguas, a su lado).
AUDIT = next(p for p in (BASE.parent, BASE.parent / 'audIT') if (p / 'recursos/Formato-Oferta-audIT').is_dir())
INF2 = AUDIT / 'recursos/Formato-Oferta-audIT/salida/informe2'
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
NAVY = '#102d3e'


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
    out = f'<rect data-card="1" x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="2"/>'
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
        f'<g data-badge="1"><rect x="{x}" y="{y}" width="{bw}" height="{h}" rx="{h // 2}" fill="{bg}" stroke="{color}" stroke-width="1.8"/>'
        + text(x + bw / 2, ty, label, size, color, weight, 'middle')
        + '</g>'
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


def item(content, extra=''):
    ext = f' {extra}' if extra else ''
    return f'<g data-item="1"{ext}>{content}</g>'


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


def icon(kind, x, y, scale=1, color=C, slide_from_x=None, pulse=False, center=None):
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
        'server': '<rect x="20" y="14" width="120" height="36" rx="6"/><rect x="20" y="62" width="120" height="36" rx="6"/><rect x="20" y="110" width="120" height="36" rx="6"/><path d="M40 32h40 M40 80h40 M40 128h40"/><circle cx="118" cy="32" r="5"/><circle cx="118" cy="80" r="5"/><circle cx="118" cy="128" r="5"/>',
        'router': '<rect x="14" y="80" width="132" height="48" rx="10"/><path d="M50 80V44 M110 80V44 M36 104h8 M60 104h8 M84 104h8"/><path d="M36 34q14-16 28 0 M96 34q14-16 28 0"/>',
        'satellite': '<rect x="62" y="62" width="36" height="36" rx="5"/><rect x="8" y="66" width="44" height="28" rx="3"/><rect x="108" y="66" width="44" height="28" rx="3"/><path d="M52 80h10 M98 80h10 M80 98v22 M62 136q18-18 36 0"/>',
        'card': '<rect x="14" y="36" width="132" height="88" rx="12"/><path d="M14 62h132 M34 100h40"/>',
        'beacon': '<circle cx="80" cy="104" r="20"/><path d="M48 72q32-32 64 0 M26 50q54-54 108 0"/>',
        'phone': '<rect x="48" y="10" width="64" height="140" rx="12"/><path d="M70 128h20"/>',
        'trailer': '<path d="M8 40h124v60H8z M132 88h20"/><circle cx="38" cy="112" r="12"/><circle cx="70" cy="112" r="12"/>',
        'ups': '<rect x="40" y="14" width="80" height="132" rx="10"/><path d="M86 44l-16 28h20l-16 30"/>',
    }
    attrs = ''
    if slide_from_x is not None:
        attrs += f' data-slide-from-x="{slide_from_x}"'
    if pulse:
        attrs += ' data-pulse="1"'
    if center:
        # El navegador mide la forma real y la centra en (cx, cy).
        attrs += f' data-center="{center[0]} {center[1]}" data-scale="{scale}"'
    return f'<g transform="translate({x} {y}) scale({scale})" fill="none" stroke="{color}" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"{attrs}>{shapes[kind]}</g>'


ICONOS = BASE / 'assets/iconos'
_TECH = {}


def tech(key, x, y, size=40):
    # Íconos oficiales sin modificar: Azure Architecture Icons y Simple Icons (CC0). Ver assets/iconos/LICENCIAS.md.
    if key not in _TECH:
        _TECH[key] = base64.b64encode((ICONOS / f'{key}.svg').read_bytes()).decode()
    return f'<image href="data:image/svg+xml;base64,{_TECH[key]}" x="{x}" y="{y}" width="{size}" height="{size}"/>'


def tchip(x, y, label, key=None, colr=C, size=15, h=32):
    # Pastilla con el logo de la tecnología a la izquierda; devuelve (svg, ancho).
    w = int(len(label) * size * 0.6) + (h + 14 if key else 22)
    out = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{h // 2}" fill="#ffffff" stroke="{colr}" stroke-width="1.5"/>'
    if key:
        out += tech(key, x + 6, y + 4, h - 8)
    out += text(x + (h + 4 if key else 11), y + h * 0.68, label, size, colr, 600)
    return out, w


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
    + '<g data-slide-from-x="-700">' + icon('truck', 1100, 320, 2.1, C) + '</g>',
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
    + '<g data-slide-from-x="-880">' + icon('truck', 1235, 268, 1.55, C) + '</g>'
    + badge(1515, 325, 'RUTA ACTIVA', AMBER, '#fff0d7', 180, 38, 21),
    0,
)
for i, (code, a, b, sub) in enumerate([
    ('01 · CONDUCTOR', 'Conductor', 'Aptitud y jornada vigente', 'Tarjeta MIFARE, licencia y descanso'),
    ('02 · VEHÍCULO', 'Vehículo', 'Vigencias y telemetría CAN', 'Estado técnico y bus J1939'),
    ('03 · DOCUMENTO', 'Documento', 'Disponibilidad y conformidad', 'Guía/DTE íntegro en cabina'),
]):
    x = 30 + i * 565
    cx = x + 265
    v += group(
        line(cx, 430, cx, 468, C, 3, draw=True)
        + circle(cx, 430, 11, C, C, pulse=True)
        + card(x, 468, 530, 168, CARD_BG, STROKE, 14, C)
        + badge(x + 26, 480, code, C, '#e7f3f6', None, 28, 16)
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
    'La salida requiere conductor habilitado, vehículo conforme y documento íntegro en cabina. La identificación del conductor utiliza tarjeta MIFARE con el camión detenido; no se propone biometría de conductores. La biometría del T-11 corresponde a la sala de datos. Una asignación de recursos no sustituye la autorización de salida: la condición documental se verifica antes del traslado.',
    30,
    3,
    kind='operational',
)

# 2. s02 — Recorrido Operacional Cabina → Terminal → Torre (45 s · S3 §3.3 · S3 §3.2.4)
v = ''
nodes_s02 = [
    ('truck', '01 · BORDE', 'Cabina', 'Identidad del conductor por tarjeta', 'Gateway + app del conductor + búfer', 30),
    ('terminal', '02 · CONTROL', 'Terminal', 'Validación y sincronización', 'Inspección y despacho local', 625),
    ('tower', '03 · NÚCLEO', 'Torre de control', 'Asignación y seguimiento', 'Monitoreo de flota 24/7', 1220),
]
for i, (ic, tag, lab, desc1, desc2, x) in enumerate(nodes_s02):
    v += group(
        card(x, 30, 475, 360, CARD_BG, STROKE, 16, C, accent_top=True)
        + badge(x + 28, 56, tag, C, '#e7f3f6', 165, 34, 20)
        + icon(ic, x + 182, 82, 0.96, C, center=(x + 237, 168))
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
    + text(155, 356, 'Lectura J1939 no invasiva', 23, MUTED)
    + line(48, 390, 525, 390, STROKE, 1.5)
    + text(48, 462, '8 GB', 54, C, 700, count_to=8, count_suffix=' GB')
    + text(198, 444, 'Buffer local eMMC', 28, WHITE, 600)
    + text(198, 478, 'Store & forward sin cobertura', 23, MUTED)
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
    + text(648, 216, 'Ingesta asíncrona', 27, C, 600)
    + text(648, 256, 'Colas desacopladas · TLS 1.3', 23, WHITE)
    + card(624, 306, 478, 118, CARD_ALT, STROKE, 12, AMBER)
    + text(648, 354, 'Persistencia políglota', 27, AMBER, 600)
    + text(648, 394, 'Transaccional + series + caché', 23, WHITE)
    + card(624, 444, 478, 154, CARD_ALT, STROKE, 12, C)
    + text(648, 492, 'Continuidad San Bernardo', 27, WHITE, 600)
    + text(648, 532, 'Fibra + LTE + grupo electrógeno', 23, WHITE)
    + text(648, 570, 'Contingencia regional en S4', 22, AMBER),
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
    + text(1418, 202, 'viajes por año', 27, WHITE, 600)
    + text(1418, 236, 'histórico a migrar', 23, MUTED)
    + line(1200, 268, 1678, 268, STROKE, 1.5)
    + card(1200, 290, 478, 148, CARD_ALT, STROKE, 12, C)
    + text(1224, 338, 'EvidenciaJornada', 28, C, 600)
    + text(1224, 378, 'Conductor + vehículo + DTE + hash', 23, WHITE)
    + text(1224, 414, 'Autorización trazable e inmutable', 21, MUTED)
    + card(1200, 458, 478, 140, CARD_ALT, STROKE, 12, AMBER)
    + text(1224, 502, 'ETL y reconciliación', 27, AMBER, 600)
    + text(1224, 540, 'Maestros saneados antes de E1', 23, WHITE)
    + text(1224, 576, 'Consulta histórica hasta M24', 21, MUTED),
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
    + badge(48, 548, 'OBSERVACIÓN 48', AMBER, '#fff0d7', None, 34, 19)
    + text(290, 574, 'Cadena íntegra entre requisito, paquete EDT y protocolo de pruebas.', 30, WHITE, 600)
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
    + text(72, 202, 'Sprints de 2 semanas', 25, C, 600)
    + text(72, 238, 'Integración continua con compuertas', 21, WHITE)
    + text(72, 268, 'DEV → QA → PREPROD → PROD', 20, MUTED)
    + card(48, 310, 478, 130, CARD_ALT, STROKE, 12, AMBER)
    + text(72, 352, 'Control de cambios (T-10)', 25, AMBER, 600)
    + text(72, 388, 'Impacto en plazo, red y seguridad', 21, WHITE)
    + text(72, 418, 'Comité aprueba antes de liberar', 20, MUTED)
    + card(48, 460, 478, 142, CARD_ALT, STROKE, 12, C)
    + text(72, 514, '≤ 5 %', 48, C, 700)
    + text(225, 498, 'Cambios fallidos', 25, WHITE, 600)
    + text(225, 530, 'Umbral mensual', 21, MUTED)
    + text(72, 578, 'Rollback automatizado', 21, C),
    0,
)
# Centro: S9 / T-13 Estándares y Quality Gates Hardware/Software
v += group(
    card(585, 26, 535, 602, CARD_BG, STROKE, 16, C, accent_top=True)
    + badge(613, 54, 'S9 · ESTÁNDARES · FORMULARIO T-13', C, '#e7f3f6', 355, 34, 19)
    + text(613, 130, 'Quality Gates Técnicos', 38, WHITE, 600)
    + card(613, 160, 478, 140, CARD_ALT, STROKE, 12, C)
    + text(637, 202, 'Hardware a bordo', 26, C, 600)
    + text(637, 238, 'SAE J1455 · IP67: conjunto expuesto', 22, WHITE)
    + text(637, 274, 'Pérdida CAN < 0,1 % en banco', 21, AMBER)
    + card(613, 320, 478, 140, CARD_ALT, STROKE, 12, C)
    + text(637, 362, 'Software y seguridad', 26, C, 600)
    + text(637, 398, 'SAST/DAST sin críticos abiertos', 22, WHITE)
    + text(637, 434, 'Reglas RN-01 a RN-04 cubiertas', 21, MUTED)
    + card(613, 480, 478, 122, CARD_ALT, STROKE, 12, AMBER)
    + text(637, 522, 'Montaje por flota', 26, AMBER, 600)
    + text(637, 558, 'Recepción unitaria por camión', 22, WHITE)
    + text(637, 588, 'Checklist firmado antes de torre', 21, MUTED),
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
    + rect_bar(1196, 285, 64, 175, C, 6, grow_y=True)
    + text(1228, 275, '25', 24, C, 700, 'middle')
    + text(1228, 490, 'Unit.', 17, WHITE, 600, 'middle')
    + rect_bar(1278, 285, 64, 175, C, 6, grow_y=True)
    + text(1310, 275, '25', 24, C, 700, 'middle')
    + text(1310, 490, 'Integr.', 17, WHITE, 600, 'middle')
    + rect_bar(1360, 320, 64, 140, C, 6, grow_y=True)
    + text(1392, 310, '20', 24, C, 700, 'middle')
    + text(1392, 490, 'Sistema', 17, WHITE, 600, 'middle')
    + rect_bar(1442, 320, 64, 140, AMBER, 6, grow_y=True)
    + text(1474, 310, '20', 24, AMBER, 700, 'middle')
    + text(1474, 490, 'No func.', 17, WHITE, 600, 'middle')
    + rect_bar(1524, 355, 64, 105, AMBER, 6, grow_y=True)
    + text(1556, 345, '15', 24, AMBER, 700, 'middle')
    + text(1556, 490, 'HIL', 17, WHITE, 600, 'middle')
    + rect_bar(1606, 355, 64, 105, AMBER, 6, grow_y=True)
    + text(1638, 345, '15', 24, AMBER, 700, 'middle')
    + text(1638, 490, 'UAT', 17, WHITE, 600, 'middle')
    + line(1185, 460, 1685, 460, '#bdced6', 2)
    + card(1178, 538, 502, 68, CARD_ALT, STROKE, 10, C)
    + text(1196, 580, 'Críticos: 100 % sin defectos S1/S2', 22, WHITE, 600),
    2,
)
add(
    'La calidad se controla desde el código hasta terreno.',
    'METODOLOGÍA Y CALIDAD / S6 · S9 · T-9 · T-10 · T-13 · T-17',
    v,
    'S6 / T-9 / T-10: metodología y control de cambios · S9 / T-13 / T-17: aseguramiento de calidad y 120 casos de prueba',
    'S6 combina sprints de dos semanas con control de cambios y umbral mensual ≤5 % de cambios fallidos. T-13 aplica SAE J1455 al perfil de montaje e IP67 al conjunto exterior expuesto, no uniformemente a todos los periféricos de cabina: el lector MIFARE del T-11 es IP66. La lectura CAN exige pérdida <0,1 % y cero tramas transmitidas por audIT. Los 120 casos del T-17 son 25 unitarios, 25 integración, 20 sistema, 12 rendimiento, ocho seguridad, 15 hardware/HIL y 15 UAT. Rendimiento y seguridad se agrupan como veinte no funcionales en la gráfica. Son casos diseñados, cuya ejecución y actas corresponden a la fase contractual.',
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
    + text(312, 406, '¿La operación adopta el cambio?', 20, WHITE)
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

# Registro de riesgos críticos: un solo cuadro con dueño, disparador y respuesta (datos ya presentes en T-16 y S7).
RISKS = [
    ('R-28', 'SOLUCIÓN', 'Documento sin cobertura en ruta', 'Líder de Integración', ('12', '8'),
     'Retorno > 90 s o pérdida de fragmentos', 'en pruebas de sombra',
     'Pre-emisión en planta, documento firmado', 'en cabina y bloqueo preventivo', C),
    ('R-16', 'DESARROLLO', 'Ruta crítica o capacitación atrasan M13', 'Jefe de Proyecto', ('8', '4'),
     'Entrega G13 incompleta el día 182 o', 'consumo > 50 % de la reserva A14',
     'PREPROD anticipado, cápsulas por perfil', 'y uso controlado de A14', AMBER),
    ('R-11', 'IMPLANTACIÓN', 'Baja adhesión de transportistas', 'Líder Funcional', ('12', '8'),
     '59 o menos anexos firmados', 'de 148 al cierre del mes 9',
     'Mesa jurídica y operativa; enrolamiento', 'asistido en los terminales', NAVY),
    ('R-19', 'IMPLANTACIÓN', 'Montaje a bordo atrasado', 'Líder de Implantación', ('6', '3'),
     'Cobertura mensual acumulada por', 'camión bajo lo planificado',
     'Cuadrillas paralelas en terminales;', 'A18 tiene 40 días hábiles de holgura', NAVY),
    ('R-18', 'IMPLANTACIÓN', 'Marcha blanca inestable', 'Líder de Operación', ('12', '8'),
     'Condiciones del Art. 17.3 no', 'cumplidas al revisar el mes 14',
     'Reversión según T-18; producción sólo', 'con acta (20 d de holgura en A15)', NAVY),
]
COLS = [(0, 'RIESGO'), (560, 'EXPOSICIÓN'), (800, 'DISPARADOR'), (1270, 'RESPUESTA')]
v = group(
    card(0, 0, 1728, 46, '#e7f3f6', STROKE, 10)
    + ''.join(text(x + 24, 31, lab, 17, C, 700, extra='letter-spacing="2"') for x, lab in COLS),
    0,
)
for k, (rid, amb, name, owner, expo, t1, t2, r1, r2, colr) in enumerate(RISKS):
    y = 58 + k * 116
    row = (
        card(0, y, 1728, 104, CARD_BG if k % 2 == 0 else CARD_ALT, STROKE, 12, colr)
        + text(28, y + 42, rid, 30, colr, 700)
        + badge(126, y + 16, amb, colr, '#e7f3f6' if colr == C else '#fff0d7' if colr == AMBER else '#edf1f4', None, 28, 15)
        + text(28, y + 80, name, 23, WHITE, 600)
        + text(352, y + 42, owner, 18, MUTED, 600)
    )
    if isinstance(expo, tuple):
        ini, res = expo
        row += (
            badge(584, y + 34, ini, AMBER, '#fff0d7', 52, 36, 20, 700)
            + arrow(642, y + 52, 690, y + 52, C, 3)
            + badge(698, y + 34, res, C, '#e7f3f6', 52, 36, 20, 700)
        )
    else:
        row += badge(584, y + 34, expo, MUTED, '#ffffff', None, 36, 18, 600)
    row += (
        text(824, y + 44, t1, 21, WHITE) + text(824, y + 74, t2, 21, WHITE)
        + text(1294, y + 44, r1, 21, C, 500) + text(1294, y + 74, r2, 21, C, 500)
    )
    v += group(item(row), 0 if k == 0 else 1 if k == 1 else 2)
add(
    'Cada riesgo crítico tiene dueño, disparador y respuesta.',
    'RIESGOS / REGISTRO DE RIESGOS CRÍTICOS · S8 · T-16 · S7 §7.3.1',
    v,
    'T-16: R-28, R-16, R-11, R-19 y R-18 · exposición en escala ordinal 1–25, residual estimada · S7 §7.3.1: holguras de A15 y A18',
    'Leer la tabla por columnas, no fila por fila. Cada riesgo tiene un único dueño, un disparador medible que activa la respuesta y una respuesta definida de antemano. [Revelar R-16.] El riesgo del proyecto se vigila con la reserva A14: si se consume más de la mitad, se escala. [Revelar implantación.] En implantación, la adhesión tiene una meta al mes 9; el montaje y la marcha blanca no se reducen con exposición sino con colchón de cronograma: 40 días de holgura en A18 y 20 en A15. La exposición residual es una estimación ordinal, no una probabilidad.',
    60,
    3,
)

# 7. s07 — Riesgo de la Solución en Ruta: R-28 y SLA de 90 s (60 s · T-16: R-28 · S8 §8.2)
v = ''
r28_nodes = [
    ('doc', '01 · ORIGEN', 'ERP emite DTE', 'Guía electrónica timbrada', 'Pre-emisión si la carga se conoce', 0),
    ('tower', '02 · ENLACE', 'Retorno satelital', 'Conmutación LTE / satélite', 'Fragmentación y acuse de recibo', 402),
    ('truck', '03 · CABINA', 'Bloqueo en cabina', ('Representación conforme', 'disponible en cabina'), 'Sin conformidad no sale', 804),
]
for i, (ic, tag, title_n, sub1, sub2, x) in enumerate(r28_nodes):
    v += group(
        card(x, 28, 352, 365, CARD_BG, STROKE, 16, C, accent_top=True)
        + badge(x + 22, 50, tag, C, '#e7f3f6', None, 30, 17)
        + icon(ic, x, 0, 0.78, C, center=(x + 176, 164))
        + text(x + 176, 282, title_n, 28, WHITE, 600, 'middle')
        + (''.join(text(x + 176, 310 + j * 24, line, 21, C, 500, 'middle') for j, line in enumerate(sub1))
           if isinstance(sub1, tuple) else text(x + 176, 318, sub1, 21, C, 500, 'middle'))
        + text(x + 176, 374 if isinstance(sub1, tuple) else 352, sub2, 20, MUTED, 400, 'middle'),
        i,
    )
    if i < 2:
        v += group(arrow(x + 358, 164, x + 396, 164, C, 3.5, draw=True, flow=True), i + 1)

# Panel derecho dedicado al SLA de 90 s con anillo medidor (cero colisión con la antena)
v += group(
    card(1206, 28, 522, 365, CARD_BG, STROKE, 16, AMBER, accent_top=True)
    + badge(1230, 50, 'CASO RT-09.01 · SLA OBJETIVO', AMBER, '#fff0d7', 310, 32, 18)
    + progress_ring(1467, 182, 80, 0.78, AMBER)
    + text(1467, 198, '90 s', 48, AMBER, 700, 'middle', count_to=90, count_suffix=' s')
    + text(1467, 318, 'Presupuesto extremo a extremo', 26, WHITE, 600, 'middle')
    + text(1467, 352, 'Exigencia sujeta a protocolo de ensayo', 22, AMBER, 400, 'middle'),
    3,
)
# Panel inferior de controles y gobierno de R-28
v += group(
    card(0, 418, 1728, 212, CARD_ALT, STROKE, 16, C)
    + badge(28, 442, 'GOBIERNO DE R-28', C, '#e7f3f6', None, 34, 19)
    + text(1700, 468, 'Exposición 12 (P3 × I4)  →  8 (P2 × I4) estimada', 25, AMBER, 700, 'end')
    + text(28, 524, 'Prevención', 22, C, 700) + text(200, 524, 'Pre-emisión documental cuando la carga se conoce en planta.', 25, WHITE)
    + text(28, 564, 'Control', 22, C, 700) + text(200, 564, 'Ensayo del documento completo en zonas de sombra; bloqueo sin conformidad.', 25, WHITE)
    + text(28, 604, 'Disparador', 22, AMBER, 700) + text(200, 604, 'Retorno > 90 s o pérdida de fragmentos en pruebas de ruta · dueño: Líder de Integración', 23, MUTED),
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
    + badge(48, 44, 'T-16 · AMFE', C, '#e7f3f6', None, 34, 19)
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
    + icon('check', 1442, 216, 0.72, C, center=(1495, 268))
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

# ACTO 1 · Arquitectura física, lógica y de datos (S4 y S5 vigentes, T-11).
# Un color por plano en todo el deck: nube, sitio y flota. Cada tecnología lleva su ícono oficial.
NUBE, SITIO, FLOTA = C, '#3e5c9a', '#2f7d5b'
TINT = {NUBE: '#e7f3f6', SITIO: '#e9edf6', FLOTA: '#e6f2ec'}


def chip(x, y, label, colr=NUBE, size=19, h=34, w=None):
    return badge(x, y, label, colr, TINT.get(colr, '#ffffff'), w, h, size, 600)


def obs(x, y, label):
    # Marca de observación del Informe 1 resuelta en esta vista.
    return badge(x, y, f'✓ {label}', CORAL, '#fbeaea', None, 30, 15, 700)


def plane(x, y, w, h, colr, title, sub='', ic=None):
    out = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="16" fill="{TINT[colr]}" stroke="{colr}" stroke-width="2"/>'
    tx = x + 22
    if ic:
        out += icon(ic, x + 16, y + 10, 0.19, colr)
        tx = x + 58
    out += text(tx, y + 34, title, 22, colr, 700)
    if sub:
        out += text(x + w - 22, y + 34, sub, 17, MUTED, 600, 'end')
    return out


def tile(x, y, key, name, sub, w=158, h=112):
    # Servicio de nube: ícono oficial arriba y nombre completo debajo.
    return (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="#ffffff" stroke="{STROKE}" stroke-width="1.5"/>'
        + tech(key, x + w / 2 - 22, y + 10, 44)
        + text(x + w / 2, y + 76, name, 16, WHITE, 700, 'middle')
        + text(x + w / 2, y + 98, sub, 14, MUTED, 500, 'middle')
    )


def iline(x, y, keys, label, size=18, colr=WHITE, weight=400, isz=24):
    # Línea de texto precedida por íconos (tecnología 'azure-…'/'si-…' o de línea).
    out, cx = '', x
    for k in keys:
        if k.startswith(('azure-', 'si-')):
            out += tech(k, cx, y - isz + 5, isz)
        else:
            out += icon(k, cx, y - isz + 4, isz / 160, colr if colr != WHITE else MUTED)
        cx += isz + 6
    return out + text(cx + 2, y, label, size, colr, weight)


def link(x1, y1, x2, y2, label, colr=MUTED, dashed=False, anchor='start', lx=None, ly=None):
    lx = (x1 + x2) / 2 + 12 if lx is None else lx
    ly = (y1 + y2) / 2 + 6 if ly is None else ly
    return arrow(x1, y1, x2, y2, colr, 3, dashed=dashed) + text(lx, ly, label, 17, colr, 600, anchor)


# A1 · Contexto y tres planos
SERV = [('azure-frontdoor', 'Front Door', 'borde y WAF'), ('azure-apim', 'API Management', 'puerta de enlace'),
        ('azure-aks', 'AKS', '6 contextos'), ('azure-iothub', 'IoT Hub', 'camiones'),
        ('azure-eventhubs', 'Event Hubs', 'protocolo Kafka'), ('azure-postgresql', 'PostgreSQL', '+ TimescaleDB'),
        ('azure-managedredis', 'Managed Redis', 'caché'), ('azure-storage', 'Storage', 'Blob · ADLS Gen2')]
v = group(
    plane(0, 0, 1340, 182, NUBE, 'NUBE · Azure Chile Central, tres zonas', '24 componentes', ic='cloud')
    + ''.join(tile(20 + k * 164, 52, *s) for k, s in enumerate(SERV))
    + plane(1376, 0, 352, 182, NUBE, 'Brazil South', '1', ic='cloud')
    + tech('azure-postgresql', 1398, 56, 34) + tech('azure-eventhubs', 1440, 56, 34) + tech('azure-storage', 1482, 56, 34)
    + text(1398, 124, 'Recuperación en espera', 19, WHITE, 700)
    + text(1398, 152, 'réplicas asíncronas', 17, NUBE, 600)
    + arrow(1340, 120, 1376, 120, NUBE, 3, dashed=True)
    + obs(560, 8, 'Obs. 71 · conteo'),
    0,
)
v += group(
    plane(0, 240, 860, 168, SITIO, 'SITIO · San Bernardo, sala de 26 m²', '4 componentes', ic='server')
    + iline(22, 306, ['si-dell', 'si-fortinet'], '2 Dell R360 · 2 FortiGate 90G · nodo de la torre', 18, WHITE, 600)
    + iline(22, 340, ['server'], 'Capa anticorrupción junto al sistema contable', 18)
    + chip(22, 360, 'Contable: único emisor', SITIO, 16, 30)
    + chip(300, 360, 'Sistema 2013: consulta hasta M24', SITIO, 16, 30)
    + plane(900, 240, 828, 168, SITIO, 'SITIO · 4 terminales regionales', '3 por gabinete', ic='router')
    + iline(922, 306, ['server'], '2 OnLogic Karbon 430 en activo y espera', 18, WHITE, 600)
    + iline(922, 340, ['router'], 'Router 5G Teltonika RUTX50 · switch · UPS', 18)
    + text(922, 380, 'Operan 24 h sin enlace', 18, SITIO, 700)
    + arrow(300, 240, 300, 184, SITIO, 3.5) + tech('azure-expressroute', 312, 196, 26)
    + text(344, 216, 'ExpressRoute 100 Mbit/s + VPN', 17, SITIO, 700)
    + arrow(1200, 240, 1200, 184, SITIO, 3.5) + tech('azure-vpngateway', 1212, 196, 26)
    + text(1244, 216, 'Fijo ≥ 10 Mbit/s + 5G', 17, SITIO, 700),
    1,
)
v += group(
    plane(0, 464, 560, 122, FLOTA, 'FLOTA · 182 camiones audIT', '5 a bordo', ic='truck')
    + iline(22, 528, ['si-linux', 'satellite'], 'iWave G26I · Iridium Edge · CANCrocodile', 17, WHITE, 600)
    + iline(22, 562, ['card'], 'MIFARE · LTE y satélite · búfer 288 h', 17)
    + plane(590, 464, 560, 122, FLOTA, 'FLOTA · 192 de terceros', 'no se intervienen', ic='truck')
    + text(612, 528, 'Conservan su equipo; acceso autorizado', 17, WHITE, 600)
    + text(612, 562, 'según factibilidad de cada proveedor', 17, WHITE)
    + plane(1180, 464, 548, 122, FLOTA, 'FLOTA · 210 semirremolques', '1 + 1', ic='trailer')
    + iline(1202, 528, ['si-bluetooth'], 'Baliza Teltonika EYE por Bluetooth', 17, WHITE, 600)
    + iline(1202, 562, ['phone'], 'Teléfono del conductor: app de 4 perfiles', 17)
    + link(868, 464, 868, 184, '', FLOTA)
    + text(856, 448, 'LTE · Iridium SBD', 17, FLOTA, 600, 'end')
    + link(892, 464, 892, 184, '', FLOTA, dashed=True)
    + text(906, 448, 'Interfaces autorizadas', 17, FLOTA, 600),
    2,
)
v += group(
    text(0, 628, '39 componentes', 22, WHITE, 700)
    + rect_bar(190, 610, round(1100 * 24 / 39), 24, NUBE, 6, grow_x=True)
    + rect_bar(190 + round(1100 * 24 / 39), 610, round(1100 / 39), 24, '#7fb3bf', 0, grow_x=True)
    + rect_bar(190 + round(1100 * 25 / 39), 610, round(1100 * 7 / 39), 24, SITIO, 0, grow_x=True)
    + rect_bar(190 + round(1100 * 32 / 39), 610, round(1100 * 7 / 39), 24, FLOTA, 6, grow_x=True)
    + text(1310, 628, '24 nube · 1 recuperación · 7 sitio · 7 flota', 18, MUTED, 600),
    3,
)
add(
    'La solución es híbrida: nube, sitio y flota.',
    'ARQUITECTURA · CONTEXTO Y TRES PLANOS / S4 §4.2 · §4.2.3 · T-11 · FEP01 Art. 16',
    v,
    'S4 §4.2, Tabla de planos y §4.2.3: 39 componentes (24 + 1 + 14) · T-11 · FEP01 Art. 16.1 a 16.4 · Caso RT-06.01 · íconos: Azure Architecture Icons y Simple Icons',
    '[Nube.] Azure Chile Central en tres zonas; Brazil South es la región de recuperación prevista. [Sitios.] San Bernardo sostiene la torre y aloja la capa anticorrupción junto al contable, único emisor tributario; cuatro terminales tienen nodos activo y espera y respaldo 5G. [Flota.] Se instalan equipos audIT en 182 camiones. Los 192 de terceros conservan sus equipos: el acceso por interfaz o exportación se sujeta a autorización y factibilidad por proveedor, sin prometer una API disponible para todos. La cobertura efectiva y antigüedad se muestran por unidad. [Componentes.] El catálogo arquitectónico tiene 39: 24 primarios, uno de recuperación y 14 fuera de la nube. R24 exige base de licitud, aprobación del mandante y cláusulas firmadas antes de H2; si falta esa condición no se autoriza producción, según S4.',
    45,
    4,
)

# A2 · Lógica: ocho capas con producto y seis contextos
LAYERS = [
    ('Presentación', [('Next.js', 'si-nextjs'), ('React', 'si-react'), ('Flutter · 4 perfiles', 'si-flutter'), ('Portería y taller', None)]),
    ('Borde y exposición', [('Azure Front Door Premium', 'azure-frontdoor'), ('WAF · protección volumétrica', None)]),
    ('Puerta de enlace', [('API Management Premium', 'azure-apim'), ('mTLS · cuotas · versionado', None)]),
    ('Servicios de negocio', [('AKS en 3 zonas', 'azure-aks'), ('Kubernetes', 'si-kubernetes'), ('.NET 10 LTS', 'si-dotnet'), ('6 contextos', None)]),
    ('Integración y eventos', [('IoT Hub S1', 'azure-iothub'), ('Event Hubs Premium', 'azure-eventhubs'), ('Kafka', 'si-kafka'), ('Go 1.27', 'si-go')]),
    ('Datos', [('PostgreSQL 16', 'azure-postgresql'), ('TimescaleDB', 'si-timescale'), ('Managed Redis', 'azure-managedredis'), ('Blob WORM', 'azure-storage'), ('Delta · ADLS Gen2', 'azure-storage')]),
]
LY0, LH2 = 0, 92
v = ''
rows = ''
for k, (lab, comps) in enumerate(LAYERS):
    y = LY0 + k * LH2
    body = (
        f'<rect x="0" y="{y}" width="1120" height="{LH2 - 12}" rx="12" fill="{"#ffffff" if k != 3 else TINT[NUBE]}" stroke="{STROKE if k != 3 else NUBE}" stroke-width="2"/>'
        + text(22, y + 48, lab, 21, NUBE if k == 3 else WHITE, 700)
    )
    x = 252
    for cpt, key in comps:
        svg_c, w = tchip(x, y + 22, cpt, key, NUBE, 15, 36)
        body += svg_c
        x += w + 10
    if k < 5:
        body += arrow(1100, y + LH2 - 18, 1100, y + LH2 + 4, MUTED, 2.5)
    rows += item(body)
v += group(rows, 0)
v += group(
    f'<rect x="1140" y="0" width="60" height="{6 * LH2 - 12}" rx="12" fill="{TINT[SITIO]}" stroke="{SITIO}" stroke-width="2"/>'
    + tech('azure-entra', 1152, 10, 36) + tech('azure-keyvault', 1152, 54, 36)
    + text(1170, 320, 'SEGURIDAD · Entra ID · Key Vault · RBAC/ABAC', 17, SITIO, 700, 'middle', extra='transform="rotate(-90 1170 320)"')
    + f'<rect x="1212" y="0" width="60" height="{6 * LH2 - 12}" rx="12" fill="#f1f3f5" stroke="{MUTED}" stroke-width="2"/>'
    + tech('azure-monitor', 1224, 10, 36)
    + text(1242, 320, 'OBSERVABILIDAD · Azure Monitor · trazas', 17, MUTED, 700, 'middle', extra='transform="rotate(-90 1242 320)"'),
    1,
)
CTX = [
    ('5.1', 'Personas y cumplimiento', '¿la persona puede conducir hoy?'),
    ('5.2', 'Flota y activos', '¿el equipo puede salir hoy?'),
    ('5.3', 'Planificación y tráfico', 'qué mover y hacia dónde'),
    ('5.4', 'Telemetría y geocercas', 'dónde está y cuándo llegó'),
    ('5.5', 'Operación de fletes', 'el viaje que realmente ocurrió'),
    ('5.6', 'Liquidación y costeo', 'cuánto costó y a quién se paga'),
]
CTX_IC = ['people', 'truck', 'tower', 'satellite', 'doc', 'db']
ctx = text(1300, 22, 'SEIS CONTEXTOS · QUÉ DECIDE CADA UNO', 15, NUBE, 700, extra='letter-spacing="1.5"')
for k, (codigo_edt, name, q) in enumerate(CTX):
    y = 44 + k * 84
    ctx += item(
        f'<rect x="1300" y="{y}" width="428" height="74" rx="10" fill="#ffffff" stroke="{NUBE}" stroke-width="1.5"/>'
        + icon(CTX_IC[k], 1312, y + 17, 0.25, NUBE)
        + text(1364, y + 32, f'{codigo_edt}  {name}', 19, NUBE, 700)
        + text(1364, y + 58, q, 17, WHITE)
    )
v += group(ctx + line(1120, 3 * LH2 + 40, 1300, 300, NUBE, 2, dash='5 4'), 2)
v += group(
    text(0, 6 * LH2 + 30, 'Ninguna interfaz toca la base: la petición baja por la pila y la respuesta sube. El camión replica servicios y datos en versión reducida.', 18, MUTED)
    + obs(1330, 6 * LH2 + 10, 'Obs. 53 · 58 · 63 · 65'),
    3,
)
add(
    'Ocho capas, cada una con su producto.',
    'ARQUITECTURA LÓGICA / S4 §4.1.1 · §4.1.3 · §4.1.4 · FEP02 numeral 2.1',
    v,
    'S4 §4.1.1: productos y soporte · §4.1.3: las ocho capas (FEP02 2.1, RT-02.01) · §4.1.4: seis contextos delimitados · ISO/IEC/IEEE 42010',
    'Recorrer la pila de arriba abajo, nombrando el producto, no el concepto. [Capas.] Portales en Next.js y React, app Flutter; Front Door con cortafuegos como único punto público; API Management con certificado mutuo; los servicios de negocio en AKS en tres zonas sobre .NET 10 LTS; IoT Hub y Event Hubs con protocolo Kafka para la ingesta, escrita en Go; y una capa de datos políglota. [Transversales.] Seguridad, con Entra ID y Key Vault, y observabilidad, con Azure Monitor, no son un piso más: atraviesan todos. [Contextos.] El negocio son seis contextos; cada uno decide una sola cosa y tiene sus propios datos: Planificación pregunta a Personas y a Flota, no lee sus bases. Son los mismos nombres de los paquetes 5.1 a 5.6 de la EDT.',
    50,
    4,
)

# A2b · Verificación bloqueante del despacho: presupuesto de 30 s
v = group(
    card(0, 0, 330, 200, '#ffffff', STROKE, 14, NUBE)
    + icon('tower', 24, 18, 0.24, NUBE)
    + text(70, 46, 'Solicitud', 22, WHITE, 700)
    + text(24, 84, 'Torre o terminal pide', 18, MUTED)
    + text(24, 110, 'conductor + tracto +', 18, MUTED)
    + text(24, 136, 'semirremolque + carga', 18, MUTED)
    + chip(24, 152, 'Planificación y tráfico', NUBE, 16, 32),
    0,
)
inv = [
    ('people', 'Persona y jornada', 'Identidad, descanso, Art. 25 bis, licencia · RN-01 a RN-04', 'Personas y cumplimiento'),
    ('truck', 'Equipo', 'Vigencias del tracto y del semirremolque, compatibilidad', 'Flota y activos'),
    ('doc', 'Carga y documento', 'Documento conforme; DS 298 en carga peligrosa', 'Planificación + contable'),
]
invs = ''
for k, (ic, t1, t2, owner) in enumerate(inv):
    y = k * 70
    invs += item(
        arrow(336, 100, 410, y + 34, NUBE, 2.5)
        + f'<rect x="414" y="{y}" width="760" height="62" rx="10" fill="#ffffff" stroke="{NUBE}" stroke-width="1.5"/>'
        + icon(ic, 426, y + 13, 0.23, NUBE)
        + text(474, y + 28, t1, 20, NUBE, 700) + text(474, y + 52, t2, 16.5, WHITE)
        + text(1158, y + 28, owner, 15, MUTED, 600, 'end')
        + arrow(1176, y + 31, 1250, 100, NUBE, 2.5)
    )
v += group(invs, 1)
v += group(
    card(1254, 0, 474, 200, '#ffffff', STROKE, 14, CORAL)
    + icon('shield', 1276, 16, 0.25, CORAL)
    + text(1322, 46, 'Veredicto', 22, WHITE, 700)
    + text(1278, 84, 'Una causa legal bloquea siempre.', 18, CORAL, 700)
    + text(1278, 112, 'El rechazo informa causa, umbral,', 17, WHITE)
    + text(1278, 136, 'dato evaluado y versión de la regla.', 17, WHITE)
    + text(1278, 172, 'Petición repetida: mismo resultado', 16, MUTED),
    1,
)
BUD = [('Identidad e idempotencia', 2, '#7fb3bf'), ('Jornada, vigencias y aptitud', 8, NUBE), ('Reserva y confirmación', 8, SITIO),
       ('Veredicto y auditoría', 4, '#7a8fbf'), ('Respuesta', 3, MUTED), ('Margen', 5, '#d9e3e8')]
bx, bw = 0, 1728 / 30
bars = text(0, 268, 'PRESUPUESTO DE EXTREMO A EXTREMO · RT-09.01 · TABLA 4.3 DEL S4', 16, NUBE, 700, extra='letter-spacing="1.5"')
for lab, s, colr in BUD:
    w = s * bw
    bars += item(
        rect_bar(round(bx, 1), 288, round(w - 4, 1), 64, colr, 8, grow_x=True)
        + text(round(bx + w / 2 - 2, 1), 328, f'{s} s', 22, '#ffffff' if colr not in ('#d9e3e8',) else MUTED, 700, 'middle')
        + text(round(bx + 4, 1), 384 + (BUD.index((lab, s, colr)) % 2) * 26, lab, 16, WHITE, 600)
    )
    bx += w
v += group(bars + text(1728, 268, '25 + 5 = 30 s', 22, CORAL, 700, 'end'), 2)
v += group(
    card(0, 430, 1728, 200, CARD_BG, STROKE, 14, NUBE)
    + text(28, 476, 'Por qué no basta con leer y después confirmar', 22, WHITE, 700)
    + text(28, 512, 'Planificación registra el intento, serializa la reserva y confirma sólo si las evaluaciones', 20, WHITE)
    + text(28, 540, 'de Personas y de Flota siguen vigentes. Un cambio incompatible invalida el intento.', 20, WHITE)
    + text(28, 584, 'Reparto de diseño, aún sin medición: los 660 ms del caso favorable no acreditan el extremo a extremo.', 18, MUTED)
    + obs(1370, 452, 'Obs. 57 · secuencia citada'),
    3,
)
add(
    'Un viaje se autoriza o se bloquea en 30 segundos.',
    'ARQUITECTURA LÓGICA · VERIFICACIÓN BLOQUEANTE / S4 §4.1.9 · Caso RT-09.01',
    v,
    'S4 §4.1.9 y Tabla 4.3: presupuesto de diseño de la asignación · Caso RT-09.01, p. 32 · S3: RN-01 a RN-04',
    'Seguir una petición real por la pila. [Solicitud.] La torre pide asignar conductor, tracto, semirremolque y carga. [Invariantes.] Planificación evalúa en paralelo tres condiciones y pregunta a quien es dueño de cada dato: Personas, Flota y el documento del contable. Una causa legal bloquea siempre, y el rechazo explica por qué. [Presupuesto.] El Caso da 30 segundos: dos para identidad, ocho para las tres evaluaciones en paralelo, ocho para reservar y confirmar, cuatro para veredicto y auditoría, tres para responder, y cinco de margen. [Cierre.] Ojo: es un reparto de diseño, todavía sin medición.',
    40,
    4,
)

# A3 · Física: nodos con hardware exacto y enlaces
v = group(
    plane(0, 0, 1340, 244, NUBE, 'Azure Chile Central · producción en 3 zonas', 'catálogo §4.2.4', ic='cloud')
    + text(22, 78, 'Borde', 16, NUBE, 700) + iline(140, 78, ['azure-frontdoor', 'azure-apim'], 'Front Door Premium · API Management Premium (3 zonas)', 17)
    + text(22, 110, 'Integración', 16, NUBE, 700) + iline(140, 110, ['azure-iothub', 'azure-dps', 'azure-eventhubs'], 'IoT Hub S1 ×2 (800.000 msg/día) · DPS X.509 · Event Hubs Premium', 17)
    + tech('azure-iothub', 1210, 94, 28) + text(1248, 116, 'IoT Hub', 17, NUBE, 700)
    + text(22, 142, 'Aplicación', 16, NUBE, 700) + iline(140, 142, ['azure-aks', 'si-kubernetes'], 'AKS con nodos en 3 zonas y escalado automático', 17)
    + text(22, 174, 'Datos', 16, NUBE, 700) + iline(140, 174, ['azure-postgresql', 'azure-storage', 'azure-keyvault'], 'PostgreSQL Flexible HA zonal · Blob ZRS inmutable · Key Vault HSM', 17)
    + text(22, 206, 'Red central', 16, NUBE, 700) + iline(140, 206, ['azure-firewall', 'azure-expressroute', 'azure-vpngateway', 'azure-bastion'], 'Firewall Premium · ExpressRoute · VPN · Bastion', 17)
    + text(22, 232, 'Red central: 10.10.0.0/22 · Red de producción: 10.11.0.0/20', 17, NUBE, 600)
    + plane(1376, 0, 352, 218, NUBE, 'Brazil South', 'espera', ic='cloud')
    + tech('azure-postgresql', 1398, 54, 32) + tech('azure-eventhubs', 1436, 54, 32) + tech('azure-storage', 1474, 54, 32)
    + text(1398, 120, 'Réplicas de PostgreSQL,', 17, WHITE) + text(1398, 144, 'Timescale y Event Hubs', 17, WHITE)
    + text(1398, 180, 'RPO 15 min · RTO 4 h', 19, NUBE, 700)
    + text(1398, 206, '10.20.0.0/22 · 10.21.0.0/20', 15, MUTED),
    0,
)
v += group(
    plane(0, 292, 640, 248, SITIO, 'San Bernardo · sala de sitio', 'pares A/B', ic='server')
    + iline(22, 354, ['si-dell'], '2 Dell PowerEdge R360', 18, WHITE, 600)
    + iline(22, 382, ['si-fortinet'], '2 FortiGate 90G · 2 FortiSwitch 124F-POE', 18)
    + iline(22, 410, ['ups'], '2 UPS APC SRT3000 · UPS de 66 min', 18)
    + iline(22, 438, ['server'], '2 Liebert Mini-Mate2 (N+1) · VESDA · Kidde', 18)
    + iline(22, 466, ['ups'], 'Grupo electrógeno Himoinsa HYW-8', 18, SITIO, 700)
    + iline(22, 494, ['ups'], 'Por R360: 2 fuentes · Por FortiGate: 2 adaptadores', 18)
    + text(54, 522, 'Alimentaciones A/B en circuitos distintos', 18, SITIO, 600)
    + plane(680, 292, 600, 248, SITIO, 'Cada terminal (×4)', 'gabinete', ic='router')
    + iline(702, 354, ['server'], '2 OnLogic Karbon 430, activo y espera', 18, WHITE, 600)
    + iline(702, 382, ['router'], 'Teltonika RUTX50 5G (2 SIM) · TSW202', 18)
    + iline(702, 410, ['ups'], 'UPS APC SRT1000XLI', 18)
    + iline(702, 438, ['si-fortinet', 'card'], 'FortiAP 234G + Minew G1 en los 5 terminales', 18)
    + text(734, 466, '24 V: cómputo/router · 48 V: TSW202 y PoE', 18, SITIO, 600)
    + iline(702, 494, ['ups'], '2 fuentes DIN + módulo de redundancia por bus', 18)
    + text(734, 522, 'A: UPS · B: otro circuito del tablero', 18, SITIO, 600)
    + plane(1320, 292, 408, 206, FLOTA, 'Camión (182 + 19)', 'a bordo', ic='truck')
    + iline(1342, 358, ['si-linux'], 'iWave G26I · 8 GB eMMC', 18, WHITE, 600)
    + iline(1342, 388, ['satellite'], 'Iridium Edge (SBD)', 18)
    + iline(1342, 418, ['chip'], 'Technoton CANCrocodile', 18)
    + iline(1342, 448, ['card'], 'Lector MIFARE · 572 tarjetas', 18)
    + iline(1342, 478, ['si-bluetooth'], 'Baliza EYE en 210 + 21', 18, FLOTA, 700),
    1,
)
v += group(
    arrow(320, 292, 320, 246, SITIO, 3.5) + tech('azure-expressroute', 334, 248, 24) + text(366, 264, 'ExpressRoute 100 Mbit/s', 16, SITIO, 700)
    + text(366, 284, '+ VPN 2.º proveedor · ≤ 1 min', 16, SITIO, 600)
    + arrow(980, 292, 980, 246, SITIO, 3.5) + tech('azure-vpngateway', 994, 248, 24) + text(1026, 264, 'Fijo ≥ 10 Mbit/s', 16, SITIO, 700)
    + text(1026, 284, '+ 5G con 2 SIM · < 1 min', 16, SITIO, 600)
    + f'<path d="M1524 292 V280 H1360 V110" fill="none" stroke="{FLOTA}" stroke-width="3.5" stroke-linejoin="round" data-draw="346"/>'
    + arrow(1360, 110, 1326, 110, FLOTA, 3.5)
    + text(1540, 262, 'LTE 13–16 MB/mes', 16, FLOTA, 700)
    + text(1540, 284, '+ Iridium SBD 340 B', 16, FLOTA, 600)
    + arrow(1340, 60, 1376, 60, NUBE, 3, dashed=True),
    2,
)
v += group(
    card(0, 564, 1728, 66, CARD_BG, STROKE, 14, NUBE)
    + text(28, 592, 'Cinco ambientes, cada uno en su suscripción y desde el mismo código: DEV · QA · PREPROD · PROD · recuperación.', 20, WHITE, 600)
    + text(28, 620, 'Respaldos 3-2-1-1-0 · restauración mensual · dos conmutaciones reales al año (RT-07.07).', 18, MUTED)
    + obs(1330, 600, 'Obs. 64 · 65 · 70 · 72'),
    3,
)
add(
    'Cada nodo declara su hardware y su enlace.',
    'ARQUITECTURA FÍSICA / S4 §4.2.1 · §4.2.4 · §4.2.6 · §4.2.7 · T-11',
    v,
    'S4 §4.2.1: hardware · §4.2.5: redes · §4.2.6: ambientes · §4.2.7: enlaces y alimentación redundante · T-11 · FEP02 RT-08.04, p. 18',
    '[Nube.] Chile Central es la región primaria: red central 10.10.0.0/22 y red de producción 10.11.0.0/20. Brazil South recibe réplicas para recuperación, con RPO de 15 minutos y RTO de 4 horas. [Enlaces.] El camión llega por LTE o Iridium a IoT Hub en Chile Central. San Bernardo usa ExpressRoute de 100 Mbit/s y VPN de respaldo; cada terminal, enlace fijo y 5G. [Energía.] San Bernardo mantiene equipos A/B en circuitos distintos: cada R360 tiene dos fuentes y cada FortiGate 90G, dos adaptadores. En cada terminal hay un bus de 24 V para cómputo y router y otro de 48 V para el TSW202, que alimenta el punto de acceso y el lector por PoE. Cada bus tiene dos fuentes DIN y un módulo de redundancia: una fuente desde la UPS y otra desde un circuito distinto del tablero, según RT-08.04 y T-11. [Cierre.] Cinco ambientes desde el mismo código. El mandante compra el hardware detallado en T-11.',
    45,
    4,
)

# A3a2 · Vista física completa con acercamiento por partes (versión extendida de la Figura 4.13 del S4)
FIS_W, FIS_H = 6251, 3667            # assets/fisica-completa.png
FIS_K = FIS_W / 2000                 # las zonas se midieron sobre la figura reducida a 2000 px de ancho
FIS_VP = (0, -74, 1330, 740)         # ventana del acercamiento, en coordenadas de la lámina
FIS_ZONAS = [                        # (título, línea 1, línea 2, zona x0 y0 x1 y1 o None para la vista completa)
    ('Vista completa', 'Nube, sitio, terminales y flota,', 'con contrapartes y enlaces', None),
    ('1 · Nube', 'Chile Central en 3 zonas', 'Brazil South: RTO 4 h · RPO 15 min', (790, 0, 1570, 505)),
    ('2 · San Bernardo', 'Racks A/B · 66 min de UPS', 'Grupo electrógeno: 24 h', (10, 95, 770, 700)),
    ('3 · Terminales ×4', 'Karbon 430 activo y en espera', 'Opera 24 h sin enlace', (795, 685, 1255, 1168)),
    ('4 · Flota', '182 iWave G26I · búfer 288 h', '210 semirremolques con baliza', (1268, 685, 1995, 1168)),
]


def fis_vista(zona):
    # viewBox con la proporción de la ventana, centrado en la zona y sin salir de la figura
    if zona is None:
        return f'0 0 {FIS_W} {FIS_H}'
    x0, y0, x1, y1 = (c * FIS_K for c in zona)
    asp = FIS_VP[2] / FIS_VP[3]
    w, h = max(x1 - x0, (y1 - y0) * asp), max(y1 - y0, (x1 - x0) / asp)
    x = min(max((x0 + x1 - w) / 2, 0), FIS_W - w)
    y = min(max((y0 + y1 - h) / 2, 0), FIS_H - h)
    return f'{x:.0f} {y:.0f} {w:.0f} {h:.0f}'


fis_marcos = ''
for k, (_t, _a, _b, zona) in enumerate(FIS_ZONAS[1:], 1):
    x0, y0, x1, y1 = (c * FIS_K for c in zona)
    fis_marcos += (
        f'<rect x="{x0:.0f}" y="{y0:.0f}" width="{x1 - x0:.0f}" height="{y1 - y0:.0f}" rx="40" fill="none" stroke="{C}" stroke-width="16"/>'
        f'<circle cx="{x0 + 95:.0f}" cy="{y0 + 95:.0f}" r="72" fill="{C}"/>'
        f'<text x="{x0 + 95:.0f}" y="{y0 + 127:.0f}" fill="#ffffff" font-size="92" font-weight="700" text-anchor="middle">{k}</text>'
    )
vx, vy, vw, vh = FIS_VP
vistas = json.dumps([fis_vista(z) for *_r, z in FIS_ZONAS])
v = (
    f'<rect x="{vx}" y="{vy}" width="{vw}" height="{vh}" rx="14" fill="#ffffff" stroke="{STROKE}" stroke-width="2"/>'
    f'<svg x="{vx}" y="{vy}" width="{vw}" height="{vh}" viewBox="{fis_vista(None)}" preserveAspectRatio="xMidYMid meet" data-zoom=\'{vistas}\'>'
    f'<image href="assets/fisica-completa.png" x="0" y="0" width="{FIS_W}" height="{FIS_H}"/>'
    f'<g data-show-at="0" data-hide-at="1">{fis_marcos}</g></svg>'
)
for k, (titulo, l1, l2, _z) in enumerate(FIS_ZONAS):
    y = vy + k * 150
    v += (
        f'<rect x="1360" y="{y}" width="368" height="140" rx="14" fill="{CARD_BG}" stroke="{STROKE}" stroke-width="2"/>'
        f'<g data-show-at="{k}"' + (f' data-hide-at="{k + 1}"' if k < len(FIS_ZONAS) - 1 else '') + '>'
        f'<rect x="1360" y="{y}" width="368" height="140" rx="14" fill="#e7f3f6" stroke="{C}" stroke-width="3"/>'
        f'<rect x="1360" y="{y}" width="7" height="140" rx="3.5" fill="{C}"/></g>'
        + text(1386, y + 46, titulo, 25, WHITE, 600)
        + text(1386, y + 84, l1, 18, MUTED)
        + text(1386, y + 112, l2, 18, MUTED)
    )
add(
    'La arquitectura física completa, parte por parte.',
    'ARQUITECTURA FÍSICA · VISTA COMPLETA / S4 §4.2.1 · §4.2.3 · §4.2.7 · T-11',
    group(v, 0),
    'S4 §4.2.1: implementos · §4.2.3: emplazamiento · §4.2.5: redes · §4.2.7: enlaces · T-11 · versión extendida de la Figura 4.13 del S4',
    '[Completa.] La misma arquitectura de la lámina anterior, en una sola vista: nube, San Bernardo, cuatro terminales, flota y contrapartes, con cada enlace y su capacidad. '
    '[Nube.] Chile Central, en tres zonas, separa borde, aplicación, integración, gestión y datos dentro de la red de producción 10.11.0.0/20. IoT Hub recibe a los camiones y Event Hubs, con protocolo Kafka, reparte los eventos. Brazil South recibe la réplica asíncrona y queda en espera, con RTO de 4 horas y RPO de 15 minutos. '
    '[San Bernardo.] Dos racks de 24 U: servidores R360 A y B, dos FortiGate 90G en alta disponibilidad, FortiSwitch A y B y dos UPS SRT3000, con 66 minutos. El grupo electrógeno Himoinsa de 8,8 kVA sostiene 24 horas con 64,3 litros. La capa anticorrupción une el sistema contable, único emisor tributario, con el sistema de 2013. ExpressRoute de 100 Mbit/s y la VPN de respaldo la conectan con Azure. '
    '[Terminales.] Cada gabinete tiene dos Karbon 430, uno activo y otro en espera, el router RUTX50 con enlace fijo de al menos 10 Mbit/s y 5G con dos SIM, y el switch TSW202. La portería lee la baliza del semirremolque con el Minew G1 y el patio tiene un FortiAP 234G. El terminal opera 24 horas sin enlace. '
    '[Flota.] Los 182 tractocamiones con equipo audIT, 148 propios y 34 de terceros, llevan el iWave G26I con Iridium Edge, el lector CAN sin contacto y el lector de tarjeta. De los 8 GB de memoria se usan 2,4 GB, con el búfer de 288 horas. Los 192 camiones de terceros conservan su equipo.',
    45,
    5,
)

# A3b · El camión como nodo on-premise distribuido
v = group(
    card(560, 150, 520, 300, '#ffffff', FLOTA, 18, FLOTA, accent_top=True)
    + icon('chip', 590, 176, 0.32, FLOTA)
    + text(820, 206, 'iWave G26I', 34, FLOTA, 700, 'middle')
    + tech('si-linux', 980, 178, 34) + tech('si-sqlite', 1024, 178, 34)
    + text(820, 240, 'Linux embebido · elemento seguro TA100', 18, WHITE, 600, 'middle')
    + text(820, 276, '3 CAN J1939 · RS232 · RS485', 18, WHITE, 400, 'middle')
    + text(820, 306, 'LTE Cat 4/M1 · GNSS · Wi-Fi · BT 5.0', 18, WHITE, 400, 'middle')
    + text(820, 342, '9–32 V · −40 a +70 °C · IP67', 18, WHITE, 400, 'middle')
    + text(820, 392, 'SQLite WAL con bandeja de salida', 18, FLOTA, 700, 'middle')
    + text(820, 420, 'actualización A/B sólo en el terminal', 17, MUTED, 400, 'middle'),
    0,
)
PER = [
    (0, 40, 'chip', None, 'Technoton CANCrocodile', 'CAN 2.0B · J1939 sin cortar el arnés', 'Restricción 6: garantía del vehículo', (440, 96), (560, 230)),
    (0, 330, 'card', None, 'Lector MIFARE DESFire', 'RS485 · IP66 · tarjeta con camión detenido', 'RT-12.11', (440, 386), (560, 370)),
    (1200, 40, 'satellite', None, 'Iridium Edge', 'RS232 · SBD 340 B de subida', 'Tramos > 80 km sin señal', (1200, 96), (1080, 230)),
    (1200, 330, 'beacon', 'si-bluetooth', 'Baliza Teltonika EYE', 'Bluetooth en el semirremolque', 'Acople verificable', (1200, 386), (1080, 370)),
]
per = ''
for x, y, ic, logo, t1, t2, t3, a, b in PER:
    w = 440 if x == 0 else 528
    per += item(
        card(x, y, w, 112, CARD_BG, STROKE, 12, FLOTA)
        + icon(ic, x + 20, y + 24, 0.36, FLOTA)
        + (tech(logo, x + w - 46, y + 14, 30) if logo else '')
        + text(x + 90, y + 38, t1, 21, FLOTA, 700) + text(x + 90, y + 68, t2, 17, WHITE) + text(x + 90, y + 94, t3, 16, MUTED)
        + line(a[0], a[1], b[0], b[1], FLOTA, 2.5, dash='6 4')
    )
v += group(per, 1)
MEM = [('Arranque', 16), ('Sistema A + B', 2048), ('Búfer 288 h', 38.4), ('Diagnóstico', 256), ('Geocercas y maestros', 16)]
mx, mscale = 0, 1728 / 8192
mem = text(0, 500, 'MEMORIA DERIVADA · 8 GB eMMC', 16, FLOTA, 700, extra='letter-spacing="1.5"') + rect_bar(0, 516, 1728, 46, '#eef2f4', 8)
for k, (lab, mb) in enumerate(MEM):
    w = max(mb * mscale, 6)
    mem += rect_bar(round(mx, 1), 516, round(w, 1), 46, [MUTED, FLOTA, CORAL, '#7a8fbf', SITIO][k], 0, grow_x=True)
    mx += w
mem += (
    text(round(mx) + 16, 546, '2.374 MB requeridos · margen de más de 3 veces', 20, WHITE, 700)
    + text(0, 600, 'El búfer de 288 h cubre los 12 días de cierre de Los Libertadores y pesa 38,4 MB: menos del 2 % de lo requerido.', 18, MUTED)
    + text(0, 628, 'Las dos particiones de sistema ocupan casi todo: permiten volver a la versión anterior si una actualización falla.', 18, MUTED)
    + obs(1480, 584, 'Obs. 73 · 78')
)
v += group(mem, 2)
add(
    'El camión es un nodo que opera sin red.',
    'ARQUITECTURA FÍSICA · EQUIPO A BORDO / S4 §4.2.2 · T-11 · Caso RT-06.01',
    v,
    'S4 §4.2.2: equipo a bordo y Tabla de capacidad derivada (2.374 MB) · Caso RT-03.10, RT-06.01, RT-10.05, RT-12.11 · restricciones 5 y 6',
    'El Caso pide tratar el equipo a bordo como un componente on-premise distribuido. [Equipo.] Es un iWave G26I: Linux, tres buses CAN, LTE, GNSS y un elemento seguro para arranque y claves; guarda los datos en SQLite y aguanta la cabina. [Periféricos.] Cada uno responde a una restricción: el CANCrocodile lee el bus sin cortar cables, para no tocar la garantía; el lector MIFARE identifica al conductor con el camión detenido; el Iridium cubre los tramos sin señal; y la baliza Bluetooth comprueba qué semirremolque va acoplado. [Memoria.] La observación 73 pidió derivar los 8 GB: se necesitan 2.374 MB, y el búfer de 288 horas para el cierre de Los Libertadores pesa menos del 2 %.',
    35,
    3,
)

# A4 · Datos: persistencia por dominio y conducta ante partición
DATA = [
    ('Asignación y vigencias', ['azure-postgresql', 'si-postgresql'], 'PostgreSQL 16 Flexible · ACID', 'Sin estado autoritativo no confirma una reserva', NUBE),
    ('Captura a bordo', ['si-sqlite'], 'SQLite 3 WAL + bandeja de salida', 'Sigue capturando y sincroniza después', FLOTA),
    ('Telemetría', ['azure-eventhubs', 'si-timescale'], 'Event Hubs → TimescaleDB', 'Acumula localmente y deduplica al reconectar', NUBE),
    ('Caché y sesiones', ['azure-managedredis', 'si-redis'], 'Azure Managed Redis', 'Si falla, consulta la fuente; nunca habilita con copia vieja', NUBE),
    ('Documentos y auditoría', ['azure-storage'], 'Blob Storage inmutable (WORM)', 'Original local cifrado hasta confirmar custodia', SITIO),
    ('Analítica', ['azure-storage'], 'Delta Lake en ADLS Gen2', 'Actualización diferida sin tocar el despacho', MUTED),
]
v = group(
    text(0, 18, 'DOMINIO', 15, NUBE, 700, extra='letter-spacing="1.5"')
    + text(290, 18, 'MOTOR', 15, NUBE, 700, extra='letter-spacing="1.5"')
    + text(760, 18, 'SI SE CORTA EL ENLACE', 15, NUBE, 700, extra='letter-spacing="1.5"'),
    0,
)
rows = ''
for k, (dom, keys, eng, part, colr) in enumerate(DATA):
    y = 32 + k * 70
    rows += item(
        f'<rect x="0" y="{y}" width="1190" height="60" rx="10" fill="{CARD_BG}" stroke="{STROKE}" stroke-width="1.5"/>'
        + f'<rect x="0" y="{y}" width="7" height="60" rx="3.5" fill="{colr}"/>'
        + text(22, y + 38, dom, 20, WHITE, 700)
        + iline(290, y + 40, keys, eng, 18, colr, 700, 30)
        + text(760, y + 38, part, 17, WHITE)
    )
v += group(rows, 0)
v += group(
    card(1222, 0, 506, 452, '#ffffff', STROKE, 14, NUBE, accent_top=True)
    + icon('db', 1244, 18, 0.22, NUBE)
    + text(1290, 46, 'Volumen y retención', 22, WHITE, 700)
    + text(1246, 94, '96.000', 36, NUBE, 700) + text(1402, 94, 'viajes al año', 19, WHITE)
    + text(1246, 142, '≈120 M', 36, NUBE, 700) + text(1402, 142, 'posiciones al año', 19, WHITE)
    + text(1246, 190, '128.000', 36, NUBE, 700) + text(1402, 190, 'documentos al año', 19, WHITE)
    + line(1246, 214, 1704, 214, STROKE, 1.5)
    + text(1246, 250, 'Jornada y evidencia', 18, WHITE) + text(1704, 250, '5 años', 18, NUBE, 700, 'end')
    + text(1246, 282, 'Documento del viaje', 18, WHITE) + text(1704, 282, '6 años', 18, NUBE, 700, 'end')
    + text(1246, 314, 'Siniestros', 18, WHITE) + text(1704, 314, '10 años', 18, NUBE, 700, 'end')
    + text(1246, 346, 'Habilitaciones', 18, WHITE) + text(1704, 346, 'vigencia + 5', 18, NUBE, 700, 'end')
    + text(1246, 378, 'Posición y telemetría', 18, WHITE) + text(1704, 378, '2 años en línea', 18, NUBE, 700, 'end')
    + text(1246, 426, 'Auditoría append-only anclada en WORM', 17, MUTED),
    1,
)
MIG = [('Extracción y perfil', 'copia y hash del origen'), ('Homologación', 'deduplicación y mapeos'),
       ('Acreditación documental', '≈6.000 vigencias: respaldo verificado'), ('Ensayo y corte', 'conciliación y acta')]
mig = text(0, 488, 'MIGRACIÓN · S5 §5.3', 15, NUBE, 700, extra='letter-spacing="1.5"')
for k, (a, b) in enumerate(MIG):
    x = k * 432
    mig += item(
        f'<rect x="{x}" y="502" width="410" height="80" rx="10" fill="{TINT[NUBE]}" stroke="{NUBE}" stroke-width="1.5"/>'
        + text(x + 18, 534, f'{k + 1}. {a}', 19, NUBE, 700) + text(x + 18, 564, b, 17, WHITE)
        + (arrow(x + 412, 542, x + 430, 542, NUBE, 2.5) if k < 3 else '')
    )
mig += text(0, 618, 'Histórico: 5 años de viajes (≈480.000, estimación) y 6 de liquidaciones. Un registro en cuarentena no habilita despacho.', 17, MUTED)
v += group(mig, 2)
add(
    'Cada dato vive en el motor que su uso exige.',
    'ARQUITECTURA DE DATOS / S5 §5.2 · §5.3 · S4 §4.1.20 · Caso RT-05.10',
    v,
    'S5 Tabla 5.3: persistencia y conducta ante partición · Tabla 5.5: retención · Tabla 5.6: migración · S4 §4.1.20: volumen declarado',
    '[Dominios.] PostgreSQL confirma las asignaciones; SQLite captura a bordo; TimescaleDB conserva telemetría. La caché no habilita con una copia desactualizada. Documentos y auditoría conservan integridad y la analítica se separa del despacho. [Volumen.] 96.000 viajes y cerca de 120 millones de posiciones anuales. [Migración.] Las aproximadamente 6.000 vigencias requieren verificación documental individual, respaldo custodiado y acta de conciliación. El hash SHA-256 comprueba integridad y no sustituye la verificación documental. Nada en cuarentena habilita despacho.',
    45,
    3,
)

# A5 · Sin enlace: qué sigue operando
v = group(
    plane(0, 0, 1728, 110, NUBE, 'Autoridad de asignación y emisión', 'Azure + San Bernardo', ic='cloud')
    + tech('azure-aks', 1568, 50, 40) + tech('azure-postgresql', 1618, 50, 40) + tech('azure-iothub', 1668, 50, 40)
    + text(22, 82, 'Asignación nueva: Azure. Documento tributario: solo el contable de San Bernardo, mediante integración.', 20, WHITE, 600),
    0,
)
AUT = [
    (0, 'San Bernardo', SITIO, 'server', '24 h', 'FEP01 Art. 16.4', ['Torre de control en continuidad', 'Recepción de emergencias', 'Registro de lo que ocurre']),
    (590, 'Terminales', SITIO, 'router', '24 h', 'mayor de 12 h (Caso) y 24 h', ['Consulta de vigencias en portería', 'Nodo en activo y espera', 'Procedimiento supletorio']),
    (1180, 'Camión', FLOTA, 'truck', '72 h → 288 h', 'RT-03.10 · diseño', ['Posición, jornada y llegadas', 'Documentos ya recibidos', 'Bloqueo sin documento conforme']),
]
nodes = ''
for x, name, colr, ic, hrs, src, items in AUT:
    nodes += item(
        f'<line x1="{x + 274}" y1="110" x2="{x + 274}" y2="190" stroke="{CORAL}" stroke-width="3" stroke-dasharray="7 6"/>'
        + text(x + 290, 158, '✕', 26, CORAL, 700)
        + plane(x, 190, 548, 290, colr, name, src, ic=ic)
        + text(x + 22, 270, hrs, 46, colr, 700)
        + text(x + 22, 300, 'de autonomía', 17, MUTED)
        + ''.join(text(x + 22, 350 + j * 36, f'• {it}', 19, WHITE) for j, it in enumerate(items))
    )
v += group(nodes, 1)
v += group(
    card(0, 512, 1728, 118, CARD_BG, STROKE, 14, CORAL)
    + text(28, 554, 'Al volver la señal: lotes numerados, deduplicación y acuse duradero; sólo el acuse libera el búfer.', 20, WHITE, 600)
    + text(28, 592, 'CP-PERF-02: 300 camiones tras 72 h sin cobertura dejan sus datos conciliados en 20 minutos.', 19, CORAL, 600)
    + obs(1500, 576, 'Obs. 74'),
    2,
)
add(
    'Si se corta el enlace, la operación sigue.',
    'ARQUITECTURA · OPERACIÓN DESCONECTADA / S4 §4.1.26 · §4.2.3 · §4.3',
    v,
    'S4 §4.1.26: operación desconectada y reconexión · §4.2.3: funciones on-premise · §4.3: plazos sin enlace · FEP01 Art. 16.4 · Caso RT-03.10 y RT-03.13',
    '[Autoridad.] Una asignación nueva requiere el estado autoritativo de Azure. El sistema contable de San Bernardo permanece como único emisor tributario, integrado a través de la capa anticorrupción. [Autonomía.] Los sitios mantienen 24 horas de funciones locales y el camión conserva un mínimo contractual de 72 horas, con diseño para 288. Una copia local no permite inventar vigencias ni confirmar asignaciones globales. [Reconexión.] Se sincroniza por lotes con deduplicación y acuse duradero. CP-PERF-02 diseña la comprobación con 300 camiones tras 72 horas, incluyendo transferencia, persistencia y conciliación. Es un criterio de ensayo, no una medición ya realizada.',
    30,
    3,
)

# ACTO 3 · Riesgos desde el T-16 y el S8 vigentes, separadores de acto y simulación de atraso.
import re
_t16 = (INF2 / 'AUDIT-Formulario-T-16.md').read_text(encoding='utf-8')
RISK = {}
for m in re.finditer(r'id=(R-\d+), riesgo=\{([^}]*)\}, categoria=\{([^}]*)\}, probabilidad=(\d), impacto=(\d), exposicion=(\d+)', _t16):
    rid, desc, cat, p, i, e = m.groups()
    RISK[rid] = dict(desc=desc, cat=cat, p=int(p), i=int(i), e=int(e))
for row in _t16.splitlines():
    cells = [c.strip() for c in row.strip().strip('|').split('|')]
    if len(cells) == 5 and cells[0] in RISK:
        a, b = cells[4].split(' a ')
        RISK[cells[0]].update(resp=cells[1], trig=cells[2], when=cells[3], e0=int(a), e1=int(b))
assert len(RISK) == 28 and all('e1' in r for r in RISK.values()), len(RISK)
AMFE = []
for row in _t16.splitlines():
    cells = [c.strip() for c in row.strip().strip('|').split('|')]
    if len(cells) == 8 and cells[3].isdigit() and cells[5].isdigit():
        AMFE.append(cells)
MC = {}
for row in (INF2 / 'AUDIT-Subdocumento8.md').read_text(encoding='utf-8').splitlines():
    cells = [c.strip() for c in row.strip().strip('|').split('|')]
    if len(cells) == 5 and re.fullmatch(r'H\d+', cells[0]) and cells[4].endswith('%'):
        MC[cells[0]] = cells[4]


def level(e):
    return 'Alta' if e >= 12 else 'Media' if e >= 6 else 'Baja'


LEVEL_FILL = {'Alta': '#f4d6d6', 'Media': '#fbe9d2', 'Baja': '#e2f0e8'}
LEVEL_INK = {'Alta': CORAL, 'Media': '#8a5a12', 'Baja': FLOTA}


def separador(num, title, sub, items):
    body = (
        text(0, 150, num, 150, '#7fb3bf', 700)
        + text(0, 300, title, 76, '#ffffff', 700)
        + text(0, 362, sub, 30, '#cfe3e8', 400)
        + ''.join(text(0 + k * 430, 470, it, 24, '#ffffff', 600) + line(k * 430, 490, k * 430 + 380, 490, '#7fb3bf', 3)
                  for k, it in enumerate(items))
    )
    return group(body, 0)


# Síntesis Art. 46: brechas del Informe 1 y cambios documentados en el repo vigente.
# La matriz completa permanece en recursos/Formato-Oferta-audIT/anexos/observaciones-informe1.tex.
cambios = [
    ('01 · 38 · 45 · 48', 'Requisitos sin trazabilidad', '42 requisitos trazados', 'hasta pruebas diseñadas', 'S3 §3.2.8', 'T-12 / T-17', 'doc', 0),
    ('37 · 53 · 64 · 65', 'Arquitectura incompleta', 'Esquema, capas y equipos', 'definidos', 'S3 §3.3 · S4 §4.1.3', 'S4 §4.2 / T-11', 'cloud', 0),
    ('43', 'Sistema de 2013 sin decisión', 'Sustitución gradual', 'consulta hasta M24', 'S3 §3.2.4', '', 'server', 1),
    ('73 · 74', 'Capacidad sin justificar', 'Memoria y reconexión', 'dimensionadas', 'S4 §§4.2.2 / 4.2.8', 'T-17 · CP-PERF-02', 'db', 1),
    ('88–91', 'Innovaciones y fichas insuficientes', 'Tipos 2 y 3 reformulados', 'cinco fichas completas', 'S13 §§13.2–13.3', 'T-19', 'chip', 2),
]
estructura = (
    text(105, 28, 'OBSERVACIÓN', 20, MUTED, 700)
    + text(654, 28, 'CAMBIO INCORPORADO', 20, C, 700)
    + text(1342, 28, 'UBICACIÓN', 20, MUTED, 700)
    + line(20, 45, 1710, 45, C, 2)
)
filas = {0: '', 1: '', 2: ''}
for i, (obs, brecha, cambio, detalle, ref1, ref2, pictograma, paso) in enumerate(cambios):
    y = 58 + i * 100
    estructura += f'<rect x="20" y="{y}" width="1690" height="92" rx="10" fill="{CARD_BG if i % 2 == 0 else CARD_ALT}"/>'
    estructura += line(630, y + 14, 630, y + 78, STROKE, 1)
    estructura += line(1320, y + 14, 1320, y + 78, STROKE, 1)
    filas[paso] += item(
        icon(pictograma, 42, y + 22, .30, C)
        + text(105, y + 30, obs, 21, AMBER, 700)
        + text(105, y + 65, brecha, 27, WHITE, 600)
        + text(654, y + 36, cambio, 33, C, 700)
        + text(654, y + 70, detalle, 27, WHITE)
        + text(1342, y + 36, ref1, 23, MUTED, 600)
        + text(1342, y + 70, ref2, 23, MUTED)
    )
v = group(
    estructura
    + line(20, 580, 1710, 580, STROKE, 1)
    + text(20, 621, 'Selección de cambios · Detalle en matriz Art. 46 · Pruebas pendientes de ejecución', 23, MUTED),
    0,
)
v += ''.join(group(filas[paso], paso) for paso in range(3))
add(
    'Cambios principales del Informe 2',
    'CORRECCIONES DEL INFORME 1 / ART. 46 · T-22',
    v,
    'Matriz Art. 46 · S3 · S4 · S13 · T-11 / T-12 / T-17 / T-19',
    'Síntesis de 40 segundos. [Vista inicial: requisitos y arquitectura.] El Informe 2 incorpora el catálogo T-12 de 42 requerimientos trazados a componentes, paquetes y pruebas diseñadas; S3 §3.2.8 y T-17 responden a las observaciones 01, 38, 45 y 48. El esquema conceptual de S3 §3.3 y las capas, interfaces y arquitectura física de S4 §§4.1.3 y 4.2 responden a 37, 53, 64 y 65, con el catálogo T-11. [Revelar legado y capacidad.] S3 §3.2.4 resuelve la observación 43 con sustitución por funciones en M16 y M21, consulta hasta M24 y conservación del ERP contable como único emisor tributario. S4 §§4.2.2 y 4.2.8 deriva memoria y reconexión para 73 y 74; T-17 CP-PERF-02 define el ensayo del proceso completo. [Revelar innovaciones.] Para 88–91, S13 §§13.2–13.3 reformula la programación por oportunidad de patio y el semirremolque conectado; T-19 entrega cinco fichas con los elementos exigidos. Se priorizan cambios que definen el alcance, la viabilidad y la verificación de la propuesta. Las correcciones editoriales permanecen en la matriz completa y las novedades de EDT y riesgos se explican en sus bloques. La selección no acredita cierre integral de las 100 observaciones ni ejecución de las pruebas. El respaldo de correcciones amplía 37, 43 y 48.',
    40,
    3,
)

add('Qué construimos', 'ACTO 1 DE 3', separador('01', 'Qué construimos', 'Arquitectura física, lógica y de datos', ['Tres planos', 'Ocho capas', 'Datos y desconexión', 'Correcciones']),
    'S4 y S5', 'Separador de acto; el expositor 1 continúa con la arquitectura.', 3, 1, kind='section')
add('Cómo lo ejecutamos', 'ACTO 2 DE 3', separador('02', 'Cómo lo ejecutamos', 'EDT, carta Gantt y compuertas', ['EDT en 3 niveles', 'Red y ruta crítica', 'Qué pasa si', 'Transición']),
    'S7 · T-14 · T-15', 'Separador. Cambio de voz al expositor de la EDT.', 3, 1, kind='section')
add('Cómo lo protegemos', 'ACTO 3 DE 3', separador('03', 'Cómo lo protegemos', 'Plan de riesgos del S8 y del T-16', ['28 riesgos', 'Los que más pesan', 'R-28 y AMFE', 'Reservas']),
    'S8 · T-16', 'Separador. Cambio de voz al expositor de riesgos.', 3, 1, kind='section')

# Mapa de calor P×I con los 28 riesgos y distribución antes/después.
GX, GY, CS = 90, 10, 104
v = ''
grid = ''
for p in range(1, 6):
    for i in range(1, 6):
        lv = level(p * i)
        x, y = GX + (i - 1) * CS, GY + (5 - p) * CS
        grid += f'<rect x="{x}" y="{y}" width="{CS - 4}" height="{CS - 4}" rx="8" fill="{LEVEL_FILL[lv]}"/>'
        grid += text(x + CS - 12, y + 22, str(p * i), 14, LEVEL_INK[lv], 700, 'end')
for k in range(1, 6):
    grid += text(GX - 18, GY + (5 - k) * CS + 58, str(k), 20, WHITE, 700, 'end')
    grid += text(GX + (k - 1) * CS + 50, GY + 5 * CS + 28, str(k), 20, WHITE, 700, 'middle')
grid += text(GX + 250, GY + 5 * CS + 62, 'IMPACTO', 16, MUTED, 700, 'middle', extra='letter-spacing="2"')
grid += text(26, GY + 260, 'PROBABILIDAD', 16, MUTED, 700, 'middle', extra='letter-spacing="2" transform="rotate(-90 26 270)"')
v += group(grid, 0)
cells = {}
for rid, r in RISK.items():
    cells.setdefault((r['p'], r['i']), []).append(rid)
chips = ''
for (p, i), ids in cells.items():
    x0, y0 = GX + (i - 1) * CS + 6, GY + (5 - p) * CS + 30
    for k, rid in enumerate(sorted(ids)):
        cx, cy = x0 + (k % 2) * 46, y0 + (k // 2) * 17
        chips += item(text(cx, cy + 12, rid.replace('R-', 'R'), 14, LEVEL_INK[level(p * i)], 700))
v += group(chips, 1)
before = {lv: sum(level(r['e0']) == lv for r in RISK.values()) for lv in ('Alta', 'Media', 'Baja')}
after = {lv: sum(level(r['e1']) == lv for r in RISK.values()) for lv in ('Alta', 'Media', 'Baja')}
dist = (
    text(720, 40, 'Antes y después de mitigar', 30, WHITE, 700)
    + text(720, 76, 'Escala del S8: baja 1–5 · media 6–11 · alta 12–25', 19, MUTED)
)
for k, lv in enumerate(('Alta', 'Media', 'Baja')):
    y = 120 + k * 110
    dist += (
        text(720, y + 30, lv, 24, LEVEL_INK[lv], 700)
        + rect_bar(860, y + 6, before[lv] * 30, 30, '#ffffff', 6, stroke=LEVEL_INK[lv])
        + text(860 + before[lv] * 30 + 12, y + 30, f'{before[lv]} antes', 19, MUTED, 600)
        + rect_bar(860, y + 46, max(after[lv] * 30, 3), 30, LEVEL_INK[lv], 6, grow_x=True)
        + text(860 + max(after[lv] * 30, 3) + 12, y + 70, f'{after[lv]} después', 19, LEVEL_INK[lv], 700)
    )
v += group(dist, 2)
cats = {}
for r in RISK.values():
    cats[r['cat']] = cats.get(r['cat'], 0) + 1
v += group(
    card(720, 460, 1008, 170, CARD_BG, STROKE, 14, CORAL)
    + text(744, 504, f'Ningún riesgo queda alto: los {before["Alta"]} de exposición alta tienen además plan de contingencia.', 21, WHITE, 700)
    + ''.join(text(744 + (k % 3) * 330, 548 + (k // 3) * 34, f'{n}  {c}', 18, MUTED, 600) for k, (c, n) in enumerate(sorted(cats.items(), key=lambda kv: -kv[1])))
    + text(744, 616, 'Exposición residual estimada, no medida.', 17, MUTED),
    3,
)
add(
    'Veintiocho riesgos evaluados; ninguno queda alto.',
    'RIESGOS · MAPA P×I / S8 §8.1–8.2 · T-16',
    v,
    'T-16: 28 riesgos con probabilidad, impacto, exposición inicial y residual · S8 §8.1: escalas y umbrales',
    'Partir por el panorama completo. [Mapa.] Probabilidad por impacto, de 1 a 5; el color sigue la escala del S8. [Riesgos.] Los 28 riesgos del T-16 en su celda inicial: la mayoría se concentra en exposición media; siete quedan en alta, y uno, el R-06, llega a 15. [Antes y después.] Después de mitigar, ninguno queda en alta. [Cierre.] Las categorías: técnicos, contrapartes, gestión, ciberseguridad y continuidad. Lo residual es una estimación, no una medición.',
    50,
    4,
)

# Los riesgos que más pesan: exposición alta (≥ 12).
SHORT = {
    'R-06': ('Retiro de Azure Cache for Redis en el mes 20', 'Diseñar desde el inicio sobre Azure Managed Redis'),
    'R-11': ('Adhesión bajo 104 en el mes 16 y 134 en el 21', '≤ 59 de 148 con anexo al cierre del mes 9'),
    'R-18': ('Marcha blanca E1 en temporada de fruta', 'Condición de cierre bajo umbral en el mes 14'),
    'R-23': ('Ataque al portal expone a conductores externos', 'Vulnerabilidad crítica abierta o acceso anómalo'),
    'R-24': ('Réplica en Brazil South sin base de licitud', 'H2 sin base de licitud, aprobación o cláusulas'),
    'R-27': ('Bloqueo indebido de un viaje que debía salir', 'Prueba en paralelo de los meses 13 a 15'),
    'R-28': ('Documento no vuelve a la cabina en 90 s', 'Ensayo con retorno > 90 s (mes 3)'),
}
top = sorted([k for k, r in RISK.items() if r['e0'] >= 12], key=lambda k: (-RISK[k]['e0'], k))
v = group(
    card(0, 0, 1728, 44, '#fbeaea', STROKE, 10)
    + ''.join(text(x, 29, lab, 16, CORAL, 700, extra='letter-spacing="1.5"') for x, lab in
              [(24, 'RIESGO'), (730, 'P × I'), (900, 'RESPUESTA'), (1080, 'DISPARADOR'), (1560, 'EXPOSICIÓN')]),
    0,
)
for k, rid in enumerate(top):
    r = RISK[rid]
    y = 54 + k * 82
    name, trig = SHORT.get(rid, (r['desc'][:48], r['trig'][:48]))
    v += group(item(
        f'<rect x="0" y="{y}" width="1728" height="74" rx="10" fill="{CARD_BG if k % 2 == 0 else "#ffffff"}" stroke="{STROKE}" stroke-width="1.5"/>'
        + text(24, y + 46, rid, 24, CORAL, 700)
        + text(118, y + 34, name, 20, WHITE, 700)
        + text(118, y + 60, r['cat'], 15, MUTED, 600)
        + text(730, y + 46, f"{r['p']} × {r['i']}", 22, WHITE, 700)
        + badge(900, y + 20, r['resp'], C if r['resp'] == 'Mitigar' else SITIO, '#ffffff', 130, 34, 17, 700)
        + text(1080, y + 46, trig, 18, WHITE)
        + badge(1560, y + 20, str(r['e0']), CORAL, '#fbeaea', 46, 34, 18, 700)
        + arrow(1612, y + 37, 1650, y + 37, MUTED, 2.5)
        + badge(1656, y + 20, str(r['e1']), FLOTA, TINT[FLOTA], 46, 34, 18, 700)
    ), 0 if k < 2 else 1 if k < 5 else 2)
add(
    'Siete riesgos altos, cada uno con su disparador.',
    'RIESGOS · EXPOSICIÓN ALTA / T-16 · S8 §8.3',
    v,
    'T-16: riesgos con exposición ≥ 12, respuesta, disparador, plazo y exposición residual · S8 §8.3: plan de acción',
    'Seleccionar los siete riesgos de exposición alta inicial. R06 se evita usando Managed Redis desde el diseño; R11 se vigila con al menos 60 de los 148 transportistas al corte M9 y refuerzo con 59 o menos. R23 protege el portal. R24 exige base de licitud, aprobación del mandante y cláusulas firmadas antes de H2; la región secundaria no se considera autorizada por el solo calendario. Completar con marcha blanca en temporada, bloqueo indebido y retorno documental R28. Las exposiciones residuales son estimaciones de diseño.',
    50,
    3,
)

# Corbatín de R-28 con barreras del S4 §4.1.13 y AMFE del T-16.
EVX = 864
v = group(
    f'<circle cx="{EVX}" cy="230" r="118" fill="#fbeaea" stroke="{CORAL}" stroke-width="3"/>'
    + text(EVX, 186, 'R-28', 30, CORAL, 700, 'middle')
    + text(EVX, 222, 'El documento completo', 19, WHITE, 700, 'middle')
    + text(EVX, 248, 'no vuelve a la cabina', 19, WHITE, 700, 'middle')
    + text(EVX, 274, 'en 90 segundos', 19, WHITE, 700, 'middle')
    + text(EVX, 312, f"P{RISK['R-28']['p']} × I{RISK['R-28']['i']} = {RISK['R-28']['e0']} → {RISK['R-28']['e1']}", 17, CORAL, 700, 'middle'),
    0,
)
CAUSES = [('Punto de carga sin LTE', 'Iridium Edge en cabina'), ('Carga conocida solo al cargar', 'Solicitud satelital al ERP'),
          ('Documento > 1 mensaje SBD', 'Fragmentación y reensamblado'), ('Pérdida de fragmentos', 'Acuse íntegro y reintentos')]
causes, bars_p = '', ''
for k, (cause, barrier) in enumerate(CAUSES):
    y = 40 + k * 116
    causes += item(
        card(0, y, 300, 70, '#ffffff', STROKE, 10, MUTED) + text(20, y + 43, cause, 18, WHITE, 600)
        + line(300, y + 35, EVX - 116, 230 + (k - 1.5) * 40, MUTED, 2.5)
    )
    bars_p += item(
        f'<rect x="340" y="{y + 12}" width="250" height="46" rx="8" fill="{NUBE}"/>'
        + text(465, y + 41, barrier, 15.5, '#ffffff', 700, 'middle')
    )
v += group(causes, 1)
v += group(bars_p + text(465, 26, 'BARRERAS PREVENTIVAS', 15, NUBE, 700, 'middle', extra='letter-spacing="1.5"'), 2)
CONS = [('Camión detenido en la carga', 'Ensayo > 90 s: revisar diseño'),
        ('Salida sin documento', 'Bloqueo de salida (RF-013/014)')]
cons = ''
for k, (c1, barrier) in enumerate(CONS):
    y = 80 + k * 220
    cons += item(
        line(EVX + 116, 230 + (k - 0.5) * 60, 1428, y + 35, MUTED, 2.5)
        + f'<rect x="1100" y="{y + 30 + (k - 0.5) * 20}" width="290" height="46" rx="8" fill="{SITIO}"/>'
        + text(1245, y + 59 + (k - 0.5) * 20, barrier, 15, '#ffffff', 700, 'middle')
        + card(1428, y, 300, 70, '#ffffff', STROKE, 10, CORAL) + text(1448, y + 43, c1, 17, WHITE, 600)
    )
v += group(cons + text(1245, 26, 'RESPUESTA Y REVISIÓN', 15, SITIO, 700, 'middle', extra='letter-spacing="1.5"'), 3)
amfe_top = sorted(AMFE, key=lambda c: -int(c[5]))[:2]
v += group(
    card(0, 520, 1728, 110, CARD_BG, STROKE, 14, CORAL)
    + text(28, 560, f'AMFE del T-16: {len(AMFE)} modos de falla, ninguno llega a NPR 50.', 21, WHITE, 700)
    + ''.join(text(28 + k * 860, 598, f'{c[0]}: NPR {c[5]} (S{c[2]} · O{c[3]} · D{c[4]})', 18, CORAL, 600) for k, c in enumerate(amfe_top))
    + text(28, 622, 'Preemisión solo si la carga ya se conoce. Ensayo M3: documento mayor, pérdidas y reintentos; NPR estimado.', 16, MUTED),
    4,
)
add(
    'R-28: cuatro causas, cuatro barreras antes del evento.',
    'RIESGOS · CORBATÍN DE R-28 / S4 §4.1.13 · S8 · T-16',
    v,
    'S4 §4.1.13: emisión del documento sin cobertura · T-16: R-28 y análisis de modos de falla · Caso RT-09.01 (90 s) · restricción 8',
    '[Evento.] El documento completo no vuelve a cabina dentro de 90 segundos. [Causas y controles.] Sin LTE se utiliza Iridium. Si la carga definitiva se conoce solo en terreno, se solicita por satélite al contable; la preemisión únicamente sirve cuando se conoce antes. Un documento mayor que un mensaje requiere fragmentación y reensamblado; las pérdidas requieren acuse de integridad y reintentos dentro del presupuesto total. El ensayo M3 utiliza el documento mayor, con pérdidas y reintentos, para validar estas barreras; no es una barrera operativa por sí solo. [Respuesta.] Sin documento conforme no se permite salir; si el ensayo falla se revisan diseño y T-11 según R28, sin asumir resuelto el camino de carga desconocida. [AMFE.] Diez modos, todos bajo NPR 50 estimado; no son mediciones de terreno.',
    50,
    5,
)

# Qué pasa si A09 se atrasa 10 días (aritmética sobre la red del T-15).
D0, D1, X0, X1 = 60, 290, 290, 1728
dx = lambda d: round(X0 + (d - D0) * (X1 - X0) / (D1 - D0), 1)
CH = [('A07', 'Infraestructura y ambientes', 76, 112), ('A09', 'Construcción Etapa 1', 112, 192),
      ('A12', 'Certificación Etapa 1', 192, 226), ('A14', 'Reserva Etapa 1', 226, 240), ('A15', 'Marcha blanca E1', 240, 290)]
DELAY = 10
v = ''
axis = ''
for d in range(60, 300, 20):
    axis += f'<line x1="{dx(d)}" y1="30" x2="{dx(d)}" y2="420" stroke="#e3ebef" stroke-width="1"/>' + text(dx(d), 22, f'día {d}', 14, MUTED, 500, 'middle')
for d, lab in ((200, 'límite H4'), (240, 'límite H5 · H6 fijo')):
    axis += f'<line x1="{dx(d)}" y1="30" x2="{dx(d)}" y2="420" stroke="{AMBER}" stroke-width="2" stroke-dasharray="6 5"/>' + text(dx(d) + 6, 440, lab, 15, AMBER, 700)
plan = ''
for k, (aid, name, s, e) in enumerate(CH):
    y = 50 + k * 72
    colr = '#f6dede' if aid == 'A14' else (CORAL if aid != 'A15' else C)
    plan += text(0, y + 30, aid, 18, CORAL if aid != 'A15' else C, 700) + text(54, y + 30, name, 17, WHITE, 600)
    ghost = ' data-dim-at="1"' if aid in ('A12', 'A14') else ''
    plan += f'<rect x="{dx(s)}" y="{y + 10}" width="{dx(e) - dx(s)}" height="30" rx="6" fill="{colr}"' + (f' stroke="{CORAL}" stroke-dasharray="5 4"' if aid == 'A14' else '') + ghost + '/>'
plan += text(dx(192) + 8, 50 + 72 + 60, 'H4', 15, AMBER, 700) + text(dx(226) + 8, 50 + 144 + 60, 'H5', 15, AMBER, 700)
v += group(axis + plan + text(dx(240) - 8, 50 + 288 + 60, 'H6', 15, AMBER, 700, 'end'), 0)
y9, y12, y14 = 50 + 72, 50 + 144, 50 + 216
shift = dx(192 + DELAY) - dx(192)
v += group(
    rect_bar(dx(192), y9 + 10, shift, 30, '#e8a3a3', 0, grow_x=True)
    + text(dx(192 + DELAY) + 8, y9 + 31, f'+{DELAY} días', 17, CORAL, 700)
    + f'<g data-slide-from-x="{-shift}"><rect x="{dx(192 + DELAY)}" y="{y12 + 10}" width="{dx(226) - dx(192)}" height="30" rx="6" fill="{CORAL}" stroke="#ffffff" stroke-width="2"/></g>'
    + f'<rect x="{dx(226 + DELAY)}" y="{y14 + 10}" width="{dx(240) - dx(226 + DELAY)}" height="30" rx="6" fill="{CORAL}"/>'
    + text(dx(226) - 8, y14 + 31, 'A14: 14 → 4 días', 17, CORAL, 700, 'end'),
    1,
)
v += group(
    card(0, 470, 560, 160, '#e2f0e8', FLOTA, 14, FLOTA)
    + text(24, 512, 'H5 y H6 se mantienen', 24, FLOTA, 700)
    + text(24, 548, f'A12 termina el día {226 + DELAY}, antes del 240.', 18, WHITE)
    + text(24, 576, 'La reserva A14 absorbe 10 de sus 14 días.', 18, WHITE)
    + text(24, 604, 'Escenario determinista; no nueva simulación.', 16, MUTED)
    + card(584, 470, 560, 160, '#fbeaea', CORAL, 14, CORAL)
    + text(608, 512, 'H4 queda 2 días tarde', 24, CORAL, 700)
    + text(608, 548, f'A09 termina el día {192 + DELAY}; su límite es el 200.', 18, WHITE)
    + text(608, 576, 'La reserva protege H6, no los hitos de pago.', 18, WHITE)
    + text(608, 604, 'R-17: incumplimiento del hito intermedio.', 16, MUTED)
    + card(1168, 470, 560, 160, CARD_BG, STROKE, 14, SITIO)
    + text(1192, 512, 'Se activa R-16', 24, SITIO, 700)
    + text(1192, 548, 'Consumo > 50 % de A14: revisión', 18, WHITE)
    + text(1192, 576, 'quincenal hasta el día 240.', 18, WHITE)
    + text(1192, 604, 'A13 termina el día 232: quedan 8 días antes de H6.', 16, MUTED),
    2,
)
add(
    '¿Y si la construcción de la Etapa 1 se atrasa 10 días?',
    'CARTA GANTT · ESCENARIO DETERMINISTA / T-15 · S7 §7.3.1 · T-16',
    v,
    'T-15 y S7 §7.3.1: A09 +10 días hábiles y consumo de A14 · T-16: R-16 y R-17 · No se recalcula Monte Carlo',
    'Este es un escenario determinista sobre la red del T-15, sin nueva simulación. A09 termina el día 202 y supera el límite 200 de H4. A12 se desplaza hasta el 236 y la reserva A14 baja de 14 a 4 días, conservando el inicio fijo de H6 en el día 240. G13 y A13 se desplazan: A13 acaba el día 232 y conserva ocho días antes de H6. Los 38 días de holgura total de la red no autorizan a mover esa fecha fija. Se activa R16 por consumo superior al 50 % de A14 y permanece R17 por incumplimiento del hito intermedio. Los porcentajes Monte Carlo de S8 pertenecen a la línea base; no se atribuyen a este escenario.',
    35,
    3,
)

# Respaldo: registro completo de los 28 riesgos (dos páginas) y AMFE completo.
ordered = sorted(RISK)
for page, chunk in enumerate((ordered[:14], ordered[14:])):
    v = card(0, 0, 1728, 40, '#fbeaea', STROKE, 8) + ''.join(
        text(x, 27, lab, 15, CORAL, 700, extra='letter-spacing="1.5"') for x, lab in
        [(16, 'ID'), (96, 'RIESGO'), (1010, 'P×I'), (1090, 'RESP.'), (1200, 'DISPARADOR'), (1650, 'EXP.')])
    for k, rid in enumerate(chunk):
        r = RISK[rid]
        y = 46 + k * 43
        v += f'<rect x="0" y="{y}" width="1728" height="39" rx="6" fill="{CARD_BG if k % 2 == 0 else "#ffffff"}"/>'
        v += text(16, y + 26, rid, 16, LEVEL_INK[level(r['e0'])], 700)
        v += text(96, y + 26, textwrap.shorten(r['desc'], 98, placeholder='…'), 15, WHITE)
        v += text(1010, y + 26, f"{r['p']}×{r['i']}", 16, WHITE, 700)
        v += text(1090, y + 26, r['resp'], 15, MUTED, 600)
        v += text(1200, y + 26, textwrap.shorten(r['trig'], 50, placeholder='…'), 14, WHITE)
        v += text(1650, y + 26, f"{r['e0']} → {r['e1']}", 15, LEVEL_INK[level(r['e0'])], 700)
    add(f'Registro de riesgos · {chunk[0]} a {chunk[-1]}.', 'RESPALDO / T-16 · REGISTRO COMPLETO', group(v, 0),
        'T-16: identificación, evaluación P×I, respuesta, disparador y exposición residual', 'Respaldo para preguntas sobre cualquier riesgo del registro.', 30, 1, backup=True)
v = card(0, 0, 1728, 44, '#fbeaea', STROKE, 8) + ''.join(
    text(x, 29, lab, 15, CORAL, 700, extra='letter-spacing="1.5"') for x, lab in
    [(16, 'MODO DE FALLA'), (620, 'S · O · D'), (780, 'NPR'), (900, 'DETECCIÓN'), (1640, 'RIESGO')])
for k, c in enumerate(sorted(AMFE, key=lambda c: -int(c[5]))):
    y = 52 + k * 58
    npr = int(c[5])
    v += f'<rect x="0" y="{y}" width="1728" height="50" rx="8" fill="{CARD_BG if k % 2 == 0 else "#ffffff"}"/>'
    v += text(16, y + 32, c[0], 18, WHITE, 600) + text(620, y + 32, f'{c[2]} · {c[3]} · {c[4]}', 18, MUTED, 600)
    v += rect_bar(780, y + 14, npr * 1.6, 22, CORAL if npr >= 30 else C, 5) + text(790 + npr * 1.6, y + 32, str(npr), 17, WHITE, 700)
    v += text(900, y + 32, c[6], 16, WHITE) + text(1640, y + 32, c[7], 17, CORAL, 700)
v += f'<line x1="{780 + 50 * 1.6}" y1="44" x2="{780 + 50 * 1.6}" y2="{52 + len(AMFE) * 58}" stroke="{CORAL}" stroke-width="2" stroke-dasharray="6 4"/>'
add('El AMFE completo: diez modos bajo NPR 50.', 'RESPALDO / T-16 · ANÁLISIS DE MODOS DE FALLA', group(v, 0),
    'T-16: análisis de modos de falla y efectos (S × O × D = NPR, umbral 50)', 'Respaldo del AMFE con los diez modos.', 30, 1, backup=True)

# 10–12. Bloque EDT (S7 §7.1 · T-14): árbol nivel 0–1, árbol completo nivel 2 y anatomía del diccionario.
# Fuente única: S7 Figura 7.1 (nombres cortos), Tabla 7.2 (responsables e hitos) y T-14 (diccionario).
EDT = [
    (1, 'Gestión del proyecto', 'Jefe de Proyecto', ['Dirección y control', 'Interesados y comunicaciones', 'Hardware del mandante']),
    (2, 'Levantamiento y diseño', 'Arquitecto de Solución', ['Línea base y catálogo', 'Cobertura móvil en terreno', 'Factibilidad con terceros', 'Arquitectura y datos', 'Estudio de costo por ruta']),
    (3, 'Plataforma', 'Líder de Operación', ['Ambientes y despliegue', 'Seguridad e identidad', 'Observabilidad', 'San Bernardo y gabinetes']),
    (4, 'Equipo a bordo', 'Líder de Implantación', ['Firmware y gestión remota', 'Montaje camión por camión', 'Integración de terceros']),
    (5, 'Servicios de la Etapa 1', 'Líder de Desarrollo', ['Personas y cumplimiento', 'Flota y activos', 'Planificación y tráfico', 'Telemetría y geocercas', 'Operación de fletes', 'Liquidación y costeo', 'Portal del transportista']),
    (6, 'Integraciones', 'Líder de Integración', ['Sistema contable', 'Plataformas de posición', 'Telemetría y tacógrafo', 'Combustible, peaje y taller', 'Sistema de 2013 y su retiro']),
    (7, 'Datos y migración', 'Líder de Datos', ['Migración de vigencias', 'Migración histórica', 'Repositorio analítico']),
    (8, 'Servicios de la Etapa 2', 'Líder de Desarrollo', ['Portal del cliente', 'Asignación de retornos', 'Emisiones', 'Talleres y mantenimiento', 'Dispersión de rendimiento']),
    (9, 'Adhesión de transportistas', 'Líder Funcional', ['Anexo de adhesión', 'Campaña y enrolamiento', 'Medición y refuerzo']),
    (10, 'Calidad y pruebas', 'Líder de Calidad', ['Sistema e integración', 'Desempeño y seguridad', 'Aceptación de usuario']),
    (11, 'Implantación', 'Líder de Implantación', ['Capacitación', 'Marcha blanca, Etapa 1', 'Marcha blanca, Etapa 2', 'Estabilización y traspaso']),
    (12, 'Innovaciones', 'Arquitecto de Solución', ['Expediente del transportista', 'Intervenciones en patio', 'Semirremolque conectado', 'Esquema de adhesión', 'Bienestar del conductor']),
    (13, 'Operación de 36 meses', 'Líder de Operación', ['Mesa de servicio 24x7', 'Operación de la plataforma', 'Ciclo de vida a bordo', 'Mantención evolutiva']),
]
assert sum(len(e[3]) for e in EDT) == 54



def edt_color(n):
    return C if n <= 6 else NAVY


# 10. EDT nivel 0 y 1: árbol descendente con conteo de paquetes y regla del 100 %.
NW = 124
NGAP = (1728 - 13 * NW) / 12
cxs = [round(i * (NW + NGAP) + NW / 2, 1) for i in range(13)]
v = group(
    card(404, 0, 920, 86, '#e7f3f6', C, 16)
    + text(864, 34, 'NIVEL 0 · PROYECTO', 17, C, 700, 'middle', extra='letter-spacing="3"')
    + text(864, 70, 'Plataforma de control de jornada, flota y viaje', 30, NAVY, 700, 'middle'),
    0,
)
nodes = ''
for i, (n, name, _, pk) in enumerate(EDT):
    cx = cxs[i]
    x = cx - NW / 2
    col = edt_color(n)
    lines = textwrap.wrap(name, 13, break_long_words=False)
    body = (
        line(cx, 118, cx, 150, col, 2.5)
        + card(x, 150, NW, 172, '#ffffff', STROKE, 12, col, accent_top=True)
        + text(cx, 204, str(n), 40, col, 700, 'middle')
    )
    for k, ln_ in enumerate(lines):
        body += text(cx, 240 + k * 22, ln_, 15.5, NAVY, 600, 'middle')
    nodes += item(body)
v += group(
    line(864, 86, 864, 118, C, 3, draw=True)
    + line(cxs[0], 118, cxs[-1], 118, C, 3, draw=True)
    + nodes
    + card(0, 486, 560, 152, CARD_BG, STROKE, 14, C)
    + text(30, 568, '13', 72, C, 700, count_to=13)
    + text(150, 548, 'elementos de primer nivel', 26, NAVY, 600)
    + text(150, 584, 'orientados a entregables, no a fases', 21, MUTED),
    1,
)
squares = ''
for i, (n, _, _, pk) in enumerate(EDT):
    cx = cxs[i]
    k = len(pk)
    tw = k * 13 + (k - 1) * 4
    sx = cx - tw / 2
    body = ''.join(f'<rect x="{sx + j * 17:.1f}" y="336" width="13" height="13" rx="3" fill="{edt_color(n)}"/>' for j in range(k))
    body += text(cx, 378, f'{k} paquetes', 16, MUTED, 600, 'middle')
    squares += item(body)
v += group(
    squares
    + card(584, 486, 560, 152, CARD_BG, STROKE, 14, C)
    + text(614, 568, '54', 72, C, 700, count_to=54)
    + text(734, 548, 'paquetes de trabajo', 26, NAVY, 600)
    + text(734, 584, 'estimables y asignables (T-14)', 21, MUTED),
    2,
)
x16 = cxs[5] + NW / 2
x713 = cxs[6] - NW / 2
v += group(
    '<path d="M0 400 v12 H{0} v-12" fill="none" stroke="{1}" stroke-width="3" stroke-linecap="round" data-draw="900"/>'.format(round(x16, 1), C)
    + text(x16 / 2, 446, 'Construye la Etapa 1 · elementos 1 a 6', 22, C, 700, 'middle')
    + '<path d="M{0} 400 v12 H1728 v-12" fill="none" stroke="{1}" stroke-width="3" stroke-linecap="round" data-draw="1000"/>'.format(round(x713, 1), NAVY)
    + text((x713 + 1728) / 2, 446, 'Acompaña, certifica y opera · elementos 7 a 13', 22, NAVY, 700, 'middle')
    + card(1168, 486, 560, 152, '#fff6e8', AMBER, 14, AMBER)
    + text(1198, 568, '100 %', 60, AMBER, 700)
    + text(1384, 548, 'del alcance cubierto', 26, NAVY, 600)
    + text(1384, 584, 'hijos = padre · sin vacíos', 21, MUTED)
    + text(1384, 612, 'ni dobles conteos', 21, MUTED),
    3,
)
add(
    'La EDT cubre todo el alcance en 13 elementos.',
    'EDT · NIVELES 0 Y 1 / S7 §7.1 · T-14',
    v,
    'S7 §7.1, Figura 7.1 y Tabla 7.2 · T-14: diccionario de 54 paquetes · PMI (2019): regla del 100 %',
    'Construir el árbol en voz alta. Nivel 0: el proyecto completo. Nivel 1: trece elementos orientados a entregables, no a fases. [Revelar paquetes.] Cada elemento baja a paquetes estimables y asignables: 54 en total; el elemento 5 es el más grande porque replica los contextos de la arquitectura. [Revelar agrupación.] Los elementos 1 a 6 construyen la Etapa 1; los 7 a 13 la acompañan, certifican y operan. La regla del 100 %: la suma de los hijos es el padre, sin vacíos ni dobles conteos.',
    50,
    4,
)

# 11. EDT nivel 2: árbol indentado completo (54 paquetes) y trazabilidad.
cols = [[1, 2, 3], [4, 5, 6], [7, 8, 9, 10], [11, 12, 13]]
CW = 420
LH = 30
v = group(
    text(0, 16, 'CONSTRUYE LA ETAPA 1', 16, C, 700, extra='letter-spacing="3"')
    + line(0, 30, 2 * CW + 16, 30, C, 2.5, draw=True)
    + text(2 * (CW + 16), 16, 'ACOMPAÑA, CERTIFICA Y OPERA', 16, NAVY, 700, extra='letter-spacing="3"')
    + line(2 * (CW + 16), 30, 1728, 30, NAVY, 2.5, draw=True),
    0,
)
focus = {5: 'S4', 9: 'Caso', 11: 'Hitos', 12: 'T-19'}
col_groups = ['', '']
for ci, col in enumerate(cols):
    x = ci * (CW + 16)
    y = 66
    for n in col:
        _, name, _, pk = EDT[n - 1]
        colr = edt_color(n)
        dim = '' if n in focus else 'data-dim-at="2"'
        body = (
            f'<rect x="{x}" y="{y - 24}" width="{CW}" height="34" rx="8" fill="{"#e7f3f6" if n <= 6 else "#edf1f4"}"/>'
            + text(x + 14, y, str(n), 21, colr, 700)
            + text(x + 52, y, name, 21, NAVY, 700)
        )
        last = y + len(pk) * LH
        body += line(x + 20, y + 12, x + 20, last - 6, STROKE, 2)
        for j, p in enumerate(pk):
            py = y + (j + 1) * LH
            body += line(x + 20, py - 6, x + 32, py - 6, STROKE, 2)
            body += text(x + 38, py, f'{n}.{j + 1}', 18, colr, 700) + text(x + 92, py, p, 18, NAVY, 400)
        col_groups[0 if ci < 2 else 1] += item(body, dim)
        y = last + LH + 10
v += group(col_groups[0], 0)
v += group(col_groups[1], 1)
tags = ''
for n, label in focus.items():
    ci = next(i for i, c in enumerate(cols) if n in c)
    x = ci * (CW + 16)
    y = 66
    for m in cols[ci]:
        if m == n:
            break
        y += (len(EDT[m - 1][3]) + 1) * LH + 10
    tags += item(badge(x + CW - 84, y - 20, label, AMBER, '#fff0d7', 76, 26, 15, 700))
legend = (
    card(0, 508, CW, 142, '#fff6e8', AMBER, 12, AMBER)
    + text(22, 534, 'TRAZABILIDAD DE LA EDT', 15, AMBER, 700, extra='letter-spacing="2"')
    + text(22, 560, 'S4 · 5.1 a 5.6 = los seis contextos', 17, NAVY, 600)
    + text(22, 583, 'T-19 · 12.1 a 12.5 = las cinco fichas', 17, NAVY, 600)
    + text(22, 606, 'Caso · 9 es entregable, no supuesto', 17, NAVY, 600)
    + text(22, 629, 'Hitos · 11 acredita H6, H7, H11 y H12', 17, NAVY, 600)
)
v += group(tags + item(legend), 2)
add(
    'Cada elemento baja a paquetes que se pueden aceptar.',
    'EDT · NIVEL 2: 54 PAQUETES / S7 §7.1 · T-14 · T-19',
    v,
    'S7 Figura 7.1 · T-14: 54 paquetes · S4: seis contextos · T-19: cinco innovaciones · Caso §17.5, p. 40',
    'Recorrer de izquierda a derecha sin leer paquete por paquete. Columnas 1 y 2: lo que construye la Etapa 1, con el elemento 5 nombrado igual que los contextos de la arquitectura. [Revelar columnas 3 y 4.] Datos, Etapa 2, adhesión, calidad, implantación, innovaciones y operación. [Revelar trazabilidad.] Destacar tres decisiones de diseño: 5.1 a 5.6 son los seis contextos de S4, por lo que cada componente tiene un único paquete que lo construye; 12.1 a 12.5 son las fichas del T-19; y la adhesión es un elemento propio con responsable, porque el Caso exige tratarla como actividad. El elemento 11 produce las actas de los hitos de marcha blanca.',
    70,
    3,
)

# 12. Diccionario: anatomía del paquete 11.2 y comprobación de la regla del 100 %.
v = group(
    card(0, 0, 1010, 650, CARD_BG, STROKE, 16, C, accent_top=True)
    + badge(28, 26, 'DICCIONARIO DE LA EDT · FORMULARIO T-14', C, '#e7f3f6', None, 34, 17)
    + text(982, 50, '0 Proyecto  ›  11 Implantación  ›  11.2', 18, MUTED, 600, 'end')
    + text(28, 140, '11.2', 64, C, 700)
    + text(196, 112, 'Marcha blanca, Etapa 1', 34, NAVY, 700)
    + text(196, 146, 'Paquete de trabajo de nivel 2 · elemento 11 Implantación', 20, MUTED),
    0,
)
fields = [
    ('ENTREGABLE', '¿Qué recibe el mandante?', 'Marcha blanca y paso a producción de la Etapa 1', C),
    ('CRITERIO DE ACEPTACIÓN', '¿Cómo se acepta o rechaza?', 'Seis condiciones del Art. 17.3 · hitos H6 y H7', C),
    ('RESPONSABLE', '¿Quién responde?', 'Líder de Implantación · un único rol del T-15', NAVY),
    ('RED Y MESES', '¿Cuándo y dónde en la red?', 'Actividades A15 y A19 · meses 13 a 16', NAVY),
]
for fi, (lab, q, val, colr) in enumerate(fields):
    y = 178 + fi * 88
    v += group(
        card(28, y, 954, 76, '#ffffff', STROKE, 12, colr)
        + text(52, y + 32, lab, 17, colr, 700, extra='letter-spacing="1.5"')
        + text(52, y + 58, q, 17, MUTED, 400)
        + text(340, y + 47, val, 25, NAVY, 600),
        1 if fi < 2 else 2,
    )
chain = (
    text(28, 556, 'TRAZA DE LA OBSERVACIÓN 48', 16, AMBER, 700, extra='letter-spacing="2"')
    + badge(28, 576, 'RNF-011 · T-12', C, '#e7f3f6', 196, 44, 19)
    + arrow(232, 598, 282, 598, C, 3)
    + badge(290, 576, 'Paquete 11.2 · T-14', AMBER, '#fff0d7', 240, 44, 19)
    + arrow(538, 598, 588, 598, C, 3)
    + badge(596, 576, 'CP-INT-05 · CP-SYS-05 · T-17', C, '#e7f3f6', 360, 44, 19)
)
v += group(chain, 2)
checks = [
    ('42', 'Requerimientos del T-12', 'Paquetes 1.1 a 13.1'),
    ('6', 'Contextos de la arquitectura', 'Paquetes 5.1 a 5.6'),
    ('5', 'Innovaciones del S13', 'Paquetes 12.1 a 12.5'),
    ('11', 'Exigencias del Caso §17.5', '2.2, 2.3, 4.2, 7.1, 9.2, 11.1 y otros'),
]
right = (
    card(1036, 0, 692, 650, '#ffffff', STROKE, 16, AMBER, accent_top=True)
    + badge(1064, 26, 'REGLA DEL 100 % · S7 TABLA 7.1', AMBER, '#fff0d7', None, 34, 17)
    + text(1064, 112, 'Ningún elemento del alcance', 30, NAVY, 700)
    + text(1064, 148, 'queda sin paquete.', 30, NAVY, 700)
)
rows = ''
for k, (num, lab, pk) in enumerate(checks):
    y = 180 + k * 92
    rows += item(
        card(1064, y, 636, 80, CARD_BG, STROKE, 12)
        + text(1120, y + 54, num, 40, C, 700, 'middle')
        + text(1176, y + 36, lab, 22, NAVY, 600)
        + text(1176, y + 63, pk, 17, MUTED)
        + circle(1662, y + 40, 20, C, '#e7f3f6', 2.5)
        + f'<path d="M1652 {y + 41} l7 7 l13 -14" fill="none" stroke="{C}" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/>'
    )
rows += item(
    card(1064, 556, 636, 66, '#fff6e8', AMBER, 12, AMBER)
    + text(1088, 597, 'Σ trabajo de los hijos = trabajo del padre', 23, AMBER, 700)
)
v += group(right + rows, 3)
add(
    'El diccionario hace verificable cada paquete.',
    'EDT · DICCIONARIO Y REGLA DEL 100 % / S7 §7.1 · T-12 · T-14 · T-17',
    v,
    'T-14: paquete 11.2 · S7 Tabla 7.1: cobertura contra el alcance · T-12: RNF-011 · T-17: CP-INT-05 y CP-SYS-05',
    'Tomar un paquete real, el 11.2, y leerlo como lo leería el mandante. [Revelar.] Entregable: lo que se recibe. Criterio: las seis condiciones del Art. 17.3, que se acreditan en los hitos H6 y H7. [Revelar.] Un solo responsable, el Líder de Implantación, y su lugar en la red: A15 y A19, meses 13 a 16. Es el mismo paquete al que llega la traza de la observación 48. [Revelar.] Cerrar con la regla del 100 %: se contrastó contra los 42 requerimientos, los seis contextos, las cinco innovaciones y las once exigencias del Caso; ninguno quedó sin paquete.',
    60,
    4,
)

# 11. s11 — Del Alcance al Control: Paquete 11.1 y Compuerta G13→A13 (60 s · T-14: 11.1 · T-15: G13/A13 · R-16)
v = ''
# Izquierda: Ficha de control del paquete 11.1 (T-14)
v += group(
    card(20, 24, 770, 604, CARD_BG, STROKE, 16, C, accent_top=True)
    + badge(48, 46, 'DICCIONARIO EDT · FORMULARIO T-14', C, '#e7f3f6', None, 30, 16)
    + text(48, 142, '11.1', 56, C, 700)
    + text(202, 114, 'Capacitación Operacional', 36, WHITE, 600)
    + text(202, 152, 'Torre de control · 5 terminales · conductores', 23, MUTED)
    + line(48, 180, 760, 180, STROKE, 1.5)
    + card(48, 202, 714, 92, CARD_ALT, STROKE, 12, C)
    + text(72, 238, 'ENTREGABLE', 21, C, 700)
    + text(72, 272, 'Capacitación de torre, terminales y conductores', 24, WHITE)
    + card(48, 308, 714, 92, CARD_ALT, STROKE, 12, C)
    + text(72, 344, 'RESPONSABLE Y VENTANA EN RED (T-15)', 21, C, 700)
    + text(72, 378, 'Líder de Implantación  ·  Actividad A13 (Día 182 al 222 · M10–M12)', 21, WHITE)
    + card(48, 414, 714, 92, CARD_ALT, STROKE, 12, AMBER)
    + text(72, 450, 'CRITERIO DE ACEPTACIÓN', 21, AMBER, 700)
    + text(72, 484, 'G13 disponible antes de A13 · usuarios certificados', 24, WHITE)
    + card(48, 522, 714, 82, '#f9f2e7', STROKE, 12, AMBER)
    + text(72, 572, 'T-14 define aceptación · T-15 fija precedencia', 22, AMBER, 600),
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
    + text(972, 211, 'G13', 18, C, 700, 'middle')
    + text(972, 266, 'Versión lista', 27, WHITE, 600, 'middle')
    + text(972, 300, 'PREPROD congelado', 21, MUTED, 400, 'middle')
    + text(972, 326, 'Datos + material', 21, C, 500, 'middle')
    + arrow(1100, 248, 1134, 248, C, 3.5, draw=True)
    + card(1138, 156, 258, 185, CARD_ALT, STROKE, 14, AMBER, accent_top=True)
    + circle(1267, 204, 24, AMBER, '#ffffff', 3)
    + text(1267, 211, 'A13', 18, AMBER, 700, 'middle')
    + text(1267, 266, 'Capacitación', 27, WHITE, 600, 'middle')
    + text(1267, 300, '40 días hábiles', 22, AMBER, 600, 'middle')
    + text(1267, 326, '10d + 30d prácticos', 21, MUTED, 400, 'middle')
    + arrow(1400, 248, 1434, 248, C, 3.5, draw=True)
    + card(1438, 156, 242, 185, CARD_ALT, STROKE, 14, C, accent_top=True)
    + circle(1559, 204, 24, C, '#ffffff', 3)
    + text(1559, 211, 'H6', 18, C, 700, 'middle')
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
    + text(872, 518, 'Regla de control (R-16): Sin G13 aceptado, A13 no comienza.', 25, AMBER, 700)
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

# Carta Gantt de la red (T-15, Tabla 7.7): 25 actividades, precedencias fin-inicio, holguras y ruta crítica.
T15 = INF2 / 'AUDIT-Formulario-T-15.md'
ACTS = {}
for row in T15.read_text(encoding='utf-8').splitlines():
    cells = [c.strip() for c in row.strip().strip('|').split('|')]
    if len(cells) == 11 and cells[0][:1] in 'AG' and cells[0][1:].isdigit():
        aid, desc, preds, dur, es, ef, ls, lf, ht, hl, crit = cells
        links_in = []
        for p in ([] if preds == 'Ninguna' else preds.split(',')):
            # Precedencia fin-inicio, con adelanto opcional: «A09 FS−10».
            parts = p.strip().replace('−', '-').split()
            links_in.append((parts[0], int(parts[1][2:]) if len(parts) > 1 else 0))
        ACTS[aid] = dict(
            preds=links_in, dur=int(dur), row=len(ACTS),
            es=int(es), ef=int(ef), lf=int(lf), ht=int(ht), crit=crit == 'Sí',
        )
assert sum(a[0] == 'A' for a in ACTS) == 25, len(ACTS)
GANTT_NAMES = {
    'A01': 'Inicio del proyecto', 'A02': 'Levantamiento y línea base', 'A03': 'Cobertura móvil en terreno',
    'A04': 'Factibilidad con terceros', 'A05': 'Arquitectura y datos', 'A06': 'Adhesión de transportistas',
    'A07': 'Infraestructura y ambientes', 'A08': 'Migración de vigencias', 'A09': 'Construcción Etapa 1',
    'A10': 'Integraciones', 'A11': 'Piloto a bordo', 'A12': 'Certificación Etapa 1',
    'A13': 'Capacitación', 'A14': 'Reserva Etapa 1', 'A15': 'Marcha blanca E1',
    'A16': 'Transferencia tecnológica', 'A17': 'Diseño Etapa 2', 'A18': 'Instalación progresiva',
    'A19': 'Paso a producción E1', 'A20': 'Construcción Etapa 2', 'A21': 'Estabilización E1',
    'A22': 'Certificación Etapa 2', 'A23': 'Reserva Etapa 2', 'A24': 'Marcha blanca E2',
    'A25': 'Producción Etapa 2', 'G13': 'Entrega G13 a capacitación',
}
# Hitos del Formulario E-25 frente a la red (S7 Tabla 7.7): (actividad, al inicio o al final)
GANTT_HITOS = {'H1': ('A02', 'ef'), 'H2': ('A05', 'ef'), 'H3': ('A07', 'ef'), 'H4': ('A09', 'ef'), 'H5': ('A12', 'ef'),
               'H6': ('A15', 'es'), 'H8': ('A17', 'ef'), 'H7': ('A19', 'ef'), 'H9': ('A20', 'ef'), 'H10': ('A22', 'ef'),
               'H11': ('A24', 'es'), 'H12': ('A25', 'ef')}
GX0, GX1, GY0, RH = 330, 1716, 58, 540 / len(ACTS)
gx = lambda d: round(GX0 + d * (GX1 - GX0) / 420, 1)
gy = lambda aid: round(GY0 + ACTS[aid]['row'] * RH, 1)
CRIT = CORAL
DASH = ' stroke-dasharray="6 5"'
DIM2 = ' data-dim-at="2"'
grid = ''
for m in range(0, 22):
    x = gx(m * 20)
    strong = m in (12, 18)
    grid += f'<line x1="{x}" y1="40" x2="{x}" y2="{GY0 + len(ACTS) * RH}" stroke="{AMBER if strong else "#dbe6eb"}" stroke-width="{2 if strong else 1}"{DASH if strong else ""}/>'
    if m < 21 and (m % 2 == 0 or m in (12, 18)):
        grid += text(gx(m * 20 + 10), 30, f'M{m + 1}', 15, AMBER if m in (12, 18) else MUTED, 700 if m in (12, 18) else 500, 'middle')
labels = ''
bars = ''
for aid, a in ACTS.items():
    y = gy(aid)
    reserve = aid in ('A14', 'A23')
    colr = CRIT if a['crit'] else C
    labels += text(0, y + 15, aid, 15, colr, 700) + text(44, y + 15, GANTT_NAMES[aid], 15, WHITE, 600 if a['crit'] else 400)
    w = max(gx(a['ef']) - gx(a['es']), 4)
    fill = '#f6dede' if reserve else colr
    stroke = f' stroke="{CRIT}" stroke-width="1.5" stroke-dasharray="4 3"' if reserve else ''
    dim = '' if a['crit'] else ' data-dim-at="2"'
    if a['dur'] == 0:
        x = gx(a['es'])
        bars += f'<g data-item="1"{dim}><rect x="{x - 7}" y="{y + 4}" width="14" height="14" transform="rotate(45 {x} {y + 11})" fill="{C}" stroke="#ffffff" stroke-width="2"/></g>'
        continue
    bars += f'<g data-item="1"{dim}><rect x="{gx(a["es"])}" y="{y + 4}" width="{w}" height="14" rx="4" fill="{fill}"{stroke}/></g>'
links = ''
for aid, a in ACTS.items():
    for p, lag in a['preds']:
        pa = ACTS[p]
        x1, y1 = gx(pa['ef'] + lag), gy(p) + 18
        x2, y2 = gx(a['es']), gy(aid) + 4
        both = pa['crit'] and a['crit']
        colr = CRIT if both else '#93a9b4'
        d = f'M{x1} {y1} V{y2 - 4}' + (f' H{x2}' if x2 - x1 > 2 else '')
        ln = int(abs(y2 - y1) + abs(x2 - x1)) + 8
        links += (
            f'<g{"" if both else DIM2}><path d="{d}" fill="none" stroke="{colr}" stroke-width="{2.2 if both else 1.3}" data-draw="{ln}"/>'
            f'<circle cx="{x2 if x2 - x1 > 2 else x1}" cy="{y2 - 4}" r="2.6" fill="{colr}"/></g>'
        )
floats = ''
for aid, a in ACTS.items():
    if a['ht'] > 0:
        y = gy(aid) + 11
        floats += (
            f'<line x1="{gx(a["ef"])}" y1="{y}" x2="{gx(a["lf"])}" y2="{y}" stroke="{MUTED}" stroke-width="1.5" stroke-dasharray="2 3"/>'
            f'<line x1="{gx(a["lf"])}" y1="{y - 5}" x2="{gx(a["lf"])}" y2="{y + 5}" stroke="{MUTED}" stroke-width="1.5"/>'
        )
hitos = ''
for h, (aid, edge) in GANTT_HITOS.items():
    x = gx(ACTS[aid][edge])
    y = gy(aid) + 11
    h = f"{h} · ≈{round(float(MC[h].rstrip(' %').replace(',', '.')))} %" if h in MC else h
    hitos += item(
        f'<rect x="{x - 7}" y="{y - 7}" width="14" height="14" transform="rotate(45 {x} {y})" fill="{AMBER}" stroke="#ffffff" stroke-width="2"/>'
        + (text(x - 14, y + 5, h, 15, AMBER, 700, 'end') if edge == 'es'
           else text(x - 10, y - 10, h, 15, AMBER, 700, 'end') if h.startswith('H12')
           else text(x + 10, y - 9, h, 15, AMBER, 700))
    )
legend_y = GY0 + len(ACTS) * RH + 22
legend = (
    f'<rect x="0" y="{legend_y - 12}" width="26" height="12" rx="3" fill="{CRIT}"/>' + text(34, legend_y, 'Ruta crítica · 13 actividades sin holgura', 17, WHITE, 600)
    + f'<rect x="420" y="{legend_y - 12}" width="26" height="12" rx="3" fill="{C}"/>' + text(454, legend_y, 'Con holgura', 17, WHITE)
    + f'<line x1="600" y1="{legend_y - 6}" x2="640" y2="{legend_y - 6}" stroke="{MUTED}" stroke-width="1.5" stroke-dasharray="2 3"/>' + text(648, legend_y, 'Holgura total', 17, WHITE)
    + f'<rect x="800" y="{legend_y - 12}" width="26" height="12" rx="3" fill="#f6dede" stroke="{CRIT}" stroke-dasharray="4 3"/>' + text(834, legend_y, 'Reserva', 17, WHITE)
    + f'<rect x="950" y="{legend_y - 13}" width="12" height="12" transform="rotate(45 956 {legend_y - 7})" fill="{AMBER}"/>' + text(972, legend_y, 'Hito E-25', 17, WHITE)
    + text(1716, legend_y, 'Días hábiles 0 a 420 · 20 días = 1 mes', 17, MUTED, 400, 'end')
)
v = group(grid + labels + bars, 0)
v += group(links, 1)
v += group(floats + legend, 2)
v += group(hitos + text(0, 644, 'Rombos: posición planificada · %: Monte Carlo al límite contractual (S8), redondeado · A09 → G13/A13: FS−10', 17, MUTED), 3)
add(
    'La red de 25 actividades define la ruta crítica.',
    'CARTA GANTT Y DEPENDENCIAS / S7 §7.3.1 · T-15 · FEP01 E-25',
    v,
    'T-15: precedencias y holguras · S7 §7.3.1, Tabla 7.7: posición planificada · S8: Monte Carlo al límite contractual (10.000 corridas)',
    '[Barras.] Veinticinco actividades y la compuerta G13, del día 0 al 420, fin M21. [Dependencias.] Se muestran precedencias fin a inicio; A09 hacia G13 y A13 incluye adelanto FS−10. A12 depende de migración, construcción, integraciones y piloto. [Ruta.] Trece actividades críticas; las reservas A14 y A23 son explícitas. Un atraso se propaga si se mantienen todas las duraciones; consumir una reserva modifica ese escenario. [Hitos.] Los rombos muestran la posición planificada y los porcentajes, redondeados, la probabilidad Monte Carlo de cumplir el límite contractual de S8. No son probabilidades de terminar en la fecha temprana: A12 se planifica al día 226, pero el 96,2 % corresponde al límite 240. Redondear un resultado a 100 % no constituye una garantía.',
    90,
    4,
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
    + text(46, 548, 'Retiro funcional del legado en M16 y M21', 26, WHITE, 600)
    + text(46, 582, '• E1 produce desde M16; E2 inicia marcha blanca en M19.', 20, MUTED)
    + text(46, 612, '• Consulta histórica hasta M24; el contable conserva la emisión.', 20, C)
    + card(865, 466, 843, 164, CARD_ALT, STROKE, 14, AMBER)
    + badge(891, 486, 'S7 §7.2 · T-15: NIVELACIÓN DE CAPACIDAD (M13–M15)', AMBER, '#fff0d7', 495, 32, 18)
    + text(891, 542, '37 FTE = 21,5 E1 + 14,1 E2 + 1,4 coordinación', 25, WHITE, 600)
    + text(891, 570, '37 personas: 21 de planta + 16 de refuerzo; sin sobreasignación.', 20, AMBER)
    + text(891, 598, 'Seguridad e Integración: dos roles distintos de 1 FTE cada uno.', 20, MUTED)
    + text(891, 623, 'Cada rol: 0,4 E1 + 0,4 E2 + 0,2 coordinación.', 19, MUTED),
    2,
)
add(
    'La transición se ejecuta en dos etapas niveladas.',
    'CRONOGRAMA Y CAPACIDAD / S3 §3.2.4 · S7 §§7.2–7.3 · T-15 · T-18',
    v,
    'S3 §3.2.4 · S7 §§7.2–7.3 · T-15: nivelación Células Alfa/Beta · T-18: etapas E1/E2 y legado hasta M24',
    '[Etapas.] Marcha blanca E1 M13–M15 y producción M16; marcha blanca E2 M19–M20 y aceptación M21; operación hasta M56. [Legado.] Retiro funcional del sistema de 2013 en M16 y M21, consulta histórica hasta M24; el contable permanece como emisor. [Capacidad M13–M15.] Son 37 personas, 21 de planta y 16 de refuerzo. Los 37 FTE se distribuyen en 21,5 para E1, 14,1 para E2 y 1,4 de coordinación. Seguridad de la Información y Líder de Integración son dos roles distintos, cada uno de un FTE: 0,4 E1, 0,4 E2 y 0,2 coordinación. No hay un especialista combinado. La tabla T-15 desglosa el resto de roles sin sobreasignación. En M19–M20 S7 prevé 26 personas; 16 integran la operación desde M21.',
    90,
    3,
)

# Reservas por cadenas (S7) y simulación de la red completa (S8).
v = group(
    card(0, 0, 840, 650, CARD_BG, STROKE, 16, CORAL, accent_top=True)
    + badge(28, 26, 'RESERVAS DE CONTINGENCIA · S7 TABLA 7.6', CORAL, '#fbeaea', None, 34, 17)
    + text(28, 104, 'Dos reservas protegen la ruta crítica', 30, WHITE, 700)
    + text(28, 134, 'Aproximación PERT normal por cadenas; no simula toda la red.', 19, MUTED),
    0,
)
for k, (rid, chain, acts_txt, sigma, days, prob, end_txt) in enumerate([
    ('A14', 'Etapa 1', 'A01 · A02 · A05 · A07 · A09 · A12', '6,89', 14, 0.979, 'día 240 / inicio M13'),
    ('A23', 'Etapa 2', 'A17 · A20 · A22', '5,04', 10, 0.976, 'día 360 / inicio M19'),
]):
    y = 150 + k * 170
    v += group(
        card(28, y, 784, 160, '#ffffff', STROKE, 12, CORAL)
        + text(52, y + 36, f'Reserva {rid} · {days} días hábiles', 26, CORAL, 700)
        + text(52, y + 68, f'Cadena {chain}: {acts_txt}', 20, WHITE, 600)
        + text(52, y + 94, f'σ = {sigma} días · {end_txt}', 19, MUTED)
        + rect_bar(52, y + 113, 520, 22, '#e7eef1', 8)
        + rect_bar(52, y + 113, round(520 * prob), 22, C, 8, grow_x=True)
        + text(590, y + 132, f'{prob * 100:.1f} %'.replace('.', ','), 26, C, 700)
        + text(700, y + 132, 'por cadena', 17, MUTED),
        1,
    )
v += group(
    card(28, 494, 784, 140, '#fff6e8', AMBER, 12, AMBER)
    + text(52, 522, 'PERT por cadenas: ambas a tiempo, 95,6 %', 21, AMBER, 700)
    + text(52, 554, 'Monte Carlo, red completa: 92,1 % conjunta', 24, C, 700)
    + text(52, 584, 'H6: 96,2 % · H11: 95,5 % · 10.000 corridas (S8)', 20, WHITE)
    + text(52, 614, 'Reserva < 50 % y cadena pendiente > 50 %: elevar al Comité Ejecutivo.', 17, MUTED),
    1,
)

slack = [
    ('A04', 'Factibilidad con terceros', 61, 'No depende de audIT', None),
    ('A18', 'Instalación progresiva', 40, 'Cierre Los Libertadores', 9),
    ('A06', 'Adhesión (holgura libre)', 24, 'Antes de la capacitación', None),
    ('A11', 'Piloto a bordo', 20, 'Cierre Los Libertadores', 9),
    ('A15', 'Marcha blanca E1', 20, 'Extensión por Art. 17.3', None),
]
right = (
    card(868, 0, 860, 650, CARD_BG, STROKE, 16, C, accent_top=True)
    + badge(896, 26, 'HOLGURAS QUE ABSORBEN RIESGOS · S7 §7.3.1', C, '#e7f3f6', None, 34, 17)
    + text(896, 108, 'Holguras de actividades fuera de la ruta', 28, WHITE, 700)
    + text(896, 142, 'Holguras internas en días hábiles; los hitos conservan su límite.', 19, MUTED)
)
rows = ''
scale = 6.2
for k, (aid, name, ht, why, event) in enumerate(slack):
    y = 182 + k * 88
    body = (
        text(896, y + 26, aid, 20, C, 700) + text(950, y + 26, name, 21, WHITE, 600)
        + text(1700, y + 26, why, 17, MUTED, 400, 'end')
        + rect_bar(896, y + 40, round(ht * scale), 22, C, 6, grow_x=True)
        + text(896 + round(ht * scale) + 10, y + 58, f'{ht} d', 19, C, 700)
    )
    if event:
        body += (
            rect_bar(896, y + 66, round(event * scale), 10, CORAL, 4, grow_x=True)
            + text(896 + round(event * scale) + 8, y + 76, f'cierre del paso: {event} d hábiles (Caso §13.2)', 16, CORAL, 600)
        )
    rows += item(body)
v += group(right + rows, 2)
add(
    'Las reservas y holguras absorben el riesgo del plan.',
    'RIESGOS DEL CRONOGRAMA / S7 §7.3.1 · T-15 · S8: MONTE CARLO',
    v,
    'S7 Tabla 7.6: PERT por cadenas (97,9 %, 97,6 %; conjunta 95,6 %) · S8: red completa (96,2 %, 95,5 %; conjunta 92,1 %) · T-15',
    '[Reservas.] A14 aporta 14 días y A23 diez. S7 usa una aproximación normal por cadenas: probabilidades 97,9 % y 97,6 %, con producto conjunto 95,6 %. [Red completa.] S8 simula 10.000 corridas con semilla 2026 y Beta-PERT sobre el T-15: H6 96,2 %, H11 95,5 % y ambas marchas blancas a tiempo 92,1 %. La diferencia recoge las rutas convergentes y la capacitación condicionada a G13; no se presentan ambos resultados como equivalentes. Si la reserva baja del 50 % con más de la mitad de cadena pendiente, se eleva al Comité Ejecutivo. [Holguras.] A04 tiene 61 días totales; A18 cuarenta, A11 y A15 veinte, y A06 veinticuatro libres. Son holguras internas; no permiten desplazar hitos ni condiciones contractuales.',
    60,
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
    ('H12', 'M21', 'Aceptación Final', 'Producción completa E1+E2', 'Operación M21–M56', 1575, True, AMBER, 1),
]
for code, m_lbl, title_g, sub1, sub2, xg, is_top, col_g, st_g in gates_s13:
    cy_card = 28 if is_top else 272
    line_y1 = 188 if is_top else 225
    line_y2 = 225 if is_top else 272
    gw = 310
    gx = min(max(xg - gw / 2, 0), 1728 - gw)
    v += group(
        line(xg, line_y1, xg, line_y2, col_g, 3, draw=True)
        + circle(xg, 225, 18, col_g, col_g, pulse=True)
        + card(gx, cy_card, gw, 158, CARD_BG, STROKE, 14, col_g, accent_top=True)
        + text(gx + 22, cy_card + 48, code, 34, col_g, 700)
        + badge(gx + gw - 120, cy_card + 20, m_lbl, col_g, '#e7f3f6' if col_g == C else '#fff0d7', 98, 34, 19)
        + text(gx + 22, cy_card + 88, title_g, 23, WHITE, 600)
        + text(gx + 22, cy_card + 118, sub1, 20, MUTED)
        + text(gx + 22, cy_card + 144, sub2, 20, col_g, 500),
        st_g,
    )

# Amortiguadores / Reservas de red (A14 y A23) y Regla de Gobierno
v += group(
    rect_bar(240, 208, 185, 34, '#e7f0f3', 10, grow_x=True, stroke=C)
    + text(332, 231, 'Reserva A14: 14 d', 19, C, 700, 'middle')
    + rect_bar(950, 208, 185, 34, '#e7f0f3', 10, grow_x=True, stroke=C)
    + text(1042, 231, 'Reserva A23: 10 d', 19, C, 700, 'middle')
    + card(20, 456, 1688, 174, CARD_ALT, STROKE, 16, AMBER)
    + badge(48, 480, 'S7 §7.3.1 · REGLA DE GOBIERNO', AMBER, '#fff0d7', None, 34, 19)
    + text(540, 505, 'Fecha contractual de hito  ≠  Holgura interna de la red', 34, AMBER, 700)
    + text(48, 558, '• Una holgura en actividades internas o el uso de las reservas A14 (14 d) y A23 (10 d) no autoriza desplazar H7 (M16) ni H12 (M21).', 25, WHITE)
    + text(48, 598, '• S8: Monte Carlo de 10.000 corridas sobre la red del T-15; H12 se cumple en el 95,5 % de las corridas.', 23, MUTED),
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
COMPROMISOS = [
    ('01', 'Qué construimos', 'Una arquitectura híbrida de 39 componentes', 'que sigue operando sin enlace.',
     '182 G26I · 8 capas con producto · 24 h en sitio, 288 h a bordo', NUBE),
    ('02', 'Cómo lo ejecutamos', '54 paquetes aceptables y una ruta', 'crítica protegida por reservas.',
     f"13 actividades críticas · A14 y A23 · H12 al {MC.get('H12', '')} en Monte Carlo", SITIO),
    ('03', 'Cómo lo protegemos', '28 riesgos con disparador;', 'ninguno queda alto.',
     'R-06 evitado desde el diseño · AMFE bajo 50 · sin documento no hay salida', CORAL),
]
for k, (num, act, l1, l2, sub, colr) in enumerate(COMPROMISOS):
    y = k * 168
    v += group(
        f'<rect x="0" y="{y}" width="10" height="140" rx="5" fill="{colr}"/>'
        + text(40, y + 52, num, 44, colr, 700) + text(130, y + 44, act.upper(), 17, colr, 700, extra='letter-spacing="2"')
        + text(130, y + 86, l1 + ' ' + l2, 34, WHITE, 700)
        + text(130, y + 124, sub, 21, MUTED),
        k,
    )
v += group(text(0, 610, 'Calidad: 120 casos de prueba diseñados (ISO/IEC/IEEE 29119); su ejecución y actas corresponden a la fase contractual.', 19, MUTED), 2)
add(
    'Tres compromisos que se pueden verificar.',
    'CIERRE / UNA PROPUESTA EN TRES ACTOS',
    v,
    'Síntesis del Informe 2: S4, S5, S7, S8 y formularios T-11 a T-19',
    'Cerrar con tres frases, una por acto, sin repetir las láminas. Qué construimos: una arquitectura híbrida que sigue operando sin enlace. Cómo lo ejecutamos: 54 paquetes y una ruta crítica protegida por reservas. Cómo lo protegemos: 28 riesgos con disparador, ninguno alto después de mitigar. Mencionar que la calidad tiene 120 casos diseñados y abrir las preguntas.',
    45,
    3,
)

# Cierre de la exposición, después de la síntesis técnica.
v = group(
    text(24, 200, 'Preguntas y discusión', 96, WHITE, 700)
    + text(28, 270, 'Gracias.', 40, C, 600)
    + line(28, 320, 1660, 320, STROKE, 3, draw=True)
    + text(28, 400, 'Transportes Curimón · Licitación TFEP-01/2026 · Caso 10, Transporte de Carga', 26, MUTED)
    + badge(28, 450, 'audIT · Soluciones Tecnológicas SpA', C, '#e7f3f6', 550, 48, 24),
    0,
)
add(
    'Preguntas y discusión',
    'CIERRE / REVISIÓN 2',
    v,
    'Transportes Curimón · TFEP-01/2026 · audIT Soluciones Tecnológicas SpA',
    'Abrir los 15 minutos de preguntas. Si hace falta mostrar un detalle, la tecla B abre el respaldo técnico y Escape vuelve.',
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
    ('03 · MODELO DE CRONOGRAMA (T-15)', 'Red determinista con reservas explícitas', 'Incorpora reservas A14 (14 d), A23 (10 d) y Células Alfa y Beta.', 'Monte Carlo del S8: probabilidad por hito en 10.000 corridas.', 20, 336, C, 1),
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

# Portafolio de innovaciones: metas y calendario propios de cada ficha T-19.
v = group(
    text(48, 30, 'EDT · INNOVACIÓN Y MADUREZ', 19, C, 700)
    + text(720, 30, 'META PROPUESTA', 19, C, 700)
    + text(1280, 30, 'CALENDARIO DE LA FICHA', 19, C, 700),
    0,
)
inno_rows = [
    ('12.1', 'Expediente verificable del transportista',
     ['Firma TRL 9 · credencial TRL 7–8', 'Credencial alternativa sujeta a aceptación'],
     ['50 % de adheridos con expediente en M21.', 'Verificación ≤5 s en el 99 % desde M16.'],
     ['Entrevistas M4; construcción M8–M10.', 'Cohorte inicial en marcha blanca E1.'], 0),
    ('12.2', 'Intervenciones por oportunidad de patio',
     ['TRL 2 propuesto; sin prueba de concepto'],
     ['Preparación inútil: reducción ≥20 %', 'respecto de la línea base homologada.'],
     ['Piloto M6; propios M6–M9.', 'Terceros desde M7; pausa M11–M15.', 'Continuación M16–M18.'], 0),
    ('12.3', 'Semirremolque conectado',
     ['Balizas TRL 9 · acople TRL 6→7 en MB'],
     ['≥95 % de asignaciones con', 'semirremolque propio verificado', 'por medición.'],
     ['Montaje M6–M10 y M16–M18.', 'Validación en MB, antes de M16.'], 1),
    ('12.4', 'Esquema de adhesión y propiedad',
     ['Ventana y consentimiento TRL 8', 'El contrato no se califica en TRL'],
     ['0 posiciones fuera de la ventana', 'de transmisión acordada.'],
     ['Anexo M2–M3; cohorte M6–M9.', 'Ventana y consola M6–M10.', 'Medición desde marcha blanca E1.'], 1),
    ('12.5', 'Bienestar y descanso en parador seguro',
     ['TRL 2 conceptual; sin prueba de concepto', 'Metas TRL 6/7 sujetas a evidencia'],
     ['≥98 % de episodios que exigen parada', 'con recomendación válida y oportuna.', 'Omisión o aviso tardío cuentan como fallo.'],
     ['Ensayos M10–M12; piloto M13–M15.', 'Producción E1 en M16.'], 2),
]
for idx, (code_i, name_i, trl_lines, metric_lines, calendar_lines, st_i) in enumerate(inno_rows):
    y = 48 + idx * 116
    col_i = AMBER if idx in (1, 2) else C
    v += group(
        card(20, y, 1688, 108, CARD_BG, STROKE, 12, col_i)
        + text(48, y + 59, code_i, 34, col_i, 700)
        + text(155, y + 30, name_i, 24, WHITE, 600)
        + ''.join(text(155, y + 60 + k * 25, t, 19, col_i) for k, t in enumerate(trl_lines))
        + ''.join(text(720, y + 30 + k * 27, t, 21, WHITE) for k, t in enumerate(metric_lines))
        + ''.join(text(1280, y + 30 + k * 27, t, 19, MUTED) for k, t in enumerate(calendar_lines)),
        st_i,
    )
v += group(text(20, 642, 'Metas propuestas, no resultados · Hitos seleccionados; calendario completo en T-19 · Fichas 1–5 / EDT 12.1–12.5', 17, MUTED), 2)
add(
    'Las cinco innovaciones distinguen TRL y condiciones.',
    'RESPALDO / INNOVACIONES · S13 · FORMULARIO T-19, FICHAS 1–5',
    v,
    'S13 §§13.1–13.5 · T-19: madurez, calendarios e indicadores por ficha · EDT 12.1–12.5',
    'Cada innovación conserva su propio calendario y meta. Son propuestas: no se declara medición ni piloto ejecutados. Expediente: 50 % de adheridos con al menos una emisión en M21, y respuesta ≤5 s en 99 % de verificaciones desde M16; el formato alternativo depende de aceptación. Proceso: concepto TRL 2, piloto de 10 camiones M6, flota propia completa M9, terceros desde M7, pausa M11–M15 y continuación M16–M18; la mejora de 20 % exige línea base homologada. Semirremolque: el 95 % se refiere a asignaciones con semirremolque propio verificado por medición; montaje M6–M10 y M16–M18, validación antes de M16. Adhesión: ventana y consentimiento TRL 8; el contrato no recibe TRL. Bienestar: TRL 2 conceptual; objetivos TRL 6 tras ensayos M10–M12 y TRL 7 tras piloto M13–M15, sujetos a evidencia. Su efectividad divide episodios con recomendación válida y oportuna por episodios en que el oráculo exige parada; falta de parador, aviso omitido o tardío son fallos, y con denominador cero no se informa tasa. Talleres M4, catálogo M3–M6 y software M4–M9 preceden a esa validación.',
    60,
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
    + text(48, 574, 'Cada camino requiere una falla técnica y una falla de control (AND); no se supone independencia estadística.', 26, WHITE, 600)
    + text(48, 610, 'Rigor S8 §8.2: análisis lógico cualitativo para diseñar pruebas en paralelo; no se inventan probabilidades empíricas sin historial.', 22, MUTED),
    2,
)
add(
    'El árbol de fallas modela compuertas OR y AND.',
    'RESPALDO 04 / ÁRBOL DE FALLAS DE VERIFICACIÓN BLOQUEANTE · S8 §8.2',
    v,
    'S8 §8.2: árbol de fallas con compuerta OR superior y cuatro compuertas AND inferiores',
    'El evento tope se alimenta por OR de cuatro ramas. Cada AND expresa una conjunción de falla técnica y falla de control. Se utiliza como análisis lógico cualitativo para diseñar pruebas; dibujar AND no acredita independencia estadística ni autoriza multiplicar probabilidades sin datos.',
    45,
    3,
    backup=True,
)

# Procedimiento de reversión: las seis acciones y responsables del T-18.
v = group(
    text(40, 30, 'PASO', 18, C, 700)
    + text(150, 30, 'ACCIÓN', 18, C, 700)
    + text(900, 30, 'RESPONSABLE', 18, C, 700)
    + text(1440, 30, 'TIEMPO MÁXIMO', 18, C, 700),
    0,
)
rev_steps = [
    ('01', 'Detectar incidente crítico de la versión o diferencia de conciliación sin explicar.', 'Guardia de la mesa de servicio', '15 minutos', 0),
    ('02', 'Decidir la reversión con la contraparte técnica informada.', 'Jefe de Proyecto y Líder de Operación', '30 minutos', 0),
    ('03', 'Cambiar el tráfico a la versión anterior del servicio afectado.', 'Ingeniero SRE de guardia', '15 minutos', 1),
    ('04', 'Recibir los eventos reenviados desde la copia de 72 horas a bordo.', 'Líder de Operación', '20 min por camión', 1),
    ('05', 'Conciliar viajes y documentos del período con el sistema contable.', 'Líder de Datos', '24 horas', 2),
    ('06', 'Informar la causa raíz al mandante.', 'Jefe de Proyecto', '5 días hábiles', 2),
]
for j, (num_r, action_r, role_r, limit_r, step_r) in enumerate(rev_steps):
    y = 50 + j * 78
    v += group(
        card(20, y, 1688, 70, CARD_BG if j % 2 == 0 else CARD_ALT, STROKE, 10, C)
        + text(40, y + 45, num_r, 30, C, 700)
        + ''.join(text(150, y + 29 + k * 27, t, 24, WHITE) for k, t in enumerate(textwrap.wrap(action_r, 55)))
        + ''.join(text(900, y + 29 + k * 27, t, 23, MUTED, 600) for k, t in enumerate(textwrap.wrap(role_r, 36)))
        + text(1440, y + 43, limit_r, 23, C, 700),
        step_r,
    )
v += group(
    card(20, 532, 1688, 102, CARD_ALT, STROKE, 14, AMBER)
    + text(48, 568, 'Ventanas por acción; no se suman como RTO único. Procedimiento previsto y pendiente de ensayo.', 24, WHITE, 600)
    + text(48, 608, 'El sistema contable conserva los documentos emitidos; el reenvío se concilia sin duplicar folios.', 23, MUTED),
    2,
)
add(
    'La reversión opera con tiempos y roles definidos.',
    'RESPALDO / PROCEDIMIENTO DE REVERSIÓN · FORMULARIO T-18',
    v,
    'T-18: procedimiento de reversión, seis acciones con sus responsables y tiempos máximos',
    'Recorrer las seis acciones del T-18. Detecta la guardia de la mesa de servicio en 15 minutos. Deciden Jefe de Proyecto y Líder de Operación en 30 minutos, con contraparte técnica informada. El SRE de guardia conmuta en 15 minutos. El Líder de Operación recibe los eventos reenviados en 20 minutos por camión. El Líder de Datos concilia en 24 horas. El Jefe de Proyecto informa la causa raíz en cinco días hábiles. Las ventanas no constituyen un RTO sumado; el procedimiento se ensaya en PREPROD antes de cada paso a producción. Un firmware vuelve a la imagen anterior en el siguiente paso por terminal, sin borrar eventos pendientes.',
    45,
    3,
    backup=True,
)

# s20 a s28 (Respaldos 06 a 14) — Diccionario Completo EDT (Paquetes 1 al 54, sin colisiones)
# Fuente vigente: tabla del diccionario exportada del Formulario T-14 (repositorio audIT).
T14 = INF2 / 'AUDIT-Formulario-T-14.md'
packages = []
for row in T14.read_text(encoding='utf-8').splitlines():
    cells = [c.strip() for c in row.strip().strip('|').split('|')]
    if len(cells) == 5 and cells[0][:1].isdigit():
        packages.append(dict(codigo=cells[0], nombre=cells[1], criterio=cells[2], responsable=cells[3], red=cells[4]))
assert len(packages) == 54, len(packages)

for page_idx, offset in enumerate(range(0, len(packages), 6)):
    v = (
        card(0, 0, 1728, 50, '#e7f3f6', STROKE, 10)
        + text(24, 33, 'PAQUETE', 18, C, 700, extra='letter-spacing="1.5"')
        + text(150, 33, 'ENTREGABLE', 18, C, 700, extra='letter-spacing="1.5"')
        + text(760, 33, 'CRITERIO DE ACEPTACIÓN', 18, C, 700, extra='letter-spacing="1.5"')
        + text(1360, 33, 'RESPONSABLE · RED Y MESES', 18, C, 700, extra='letter-spacing="1.5"')
    )
    row_top = 60
    for j, p in enumerate(packages[offset:offset + 6]):
        name_lines = textwrap.wrap(p['nombre'], 46, break_long_words=False, break_on_hyphens=False)
        criterion_lines = textwrap.wrap(p['criterio'], 56, break_long_words=False, break_on_hyphens=False)
        role_lines = textwrap.wrap(p['responsable'], 36, break_long_words=False)
        network_lines = textwrap.wrap(p['red'], 40, break_long_words=False, break_on_hyphens=False)
        row_height = max(80, 26 + max(len(name_lines) * 24, len(criterion_lines) * 22,
                                      (len(role_lines) + len(network_lines)) * 21))
        v += card(0, row_top, 1728, row_height, CARD_BG if j % 2 == 0 else CARD_ALT, STROKE, 10, C)
        v += text(24, row_top + row_height / 2 + 10, p['codigo'], 30, C, 700)
        for col_x, wrapped, size, line_height in (
            (150, name_lines, 22, 24),
            (760, criterion_lines, 20, 22),
        ):
            first_baseline = row_top + (row_height - (len(wrapped) - 1) * line_height) / 2 + size * 0.35
            for k, value_line in enumerate(wrapped):
                v += text(col_x, first_baseline + k * line_height, value_line, size, WHITE, 500)
        for k, value_line in enumerate(role_lines):
            v += text(1360, row_top + 24 + k * 21, value_line, 18, WHITE, 600)
        for k, value_line in enumerate(network_lines):
            v += text(1360, row_top + 24 + (len(role_lines) + k) * 21, value_line, 18, MUTED)
        row_top += row_height + 8
    v = group(v, 0)
    add(
        f'Diccionario EDT · paquetes {packages[offset]["codigo"]} a {packages[min(offset + 5, len(packages) - 1)]["codigo"]}.',
        f'RESPALDO {page_idx + 6:02} / DICCIONARIO EDT · T-14',
        v,
        'T-14: diccionario de la EDT, entregable, criterio, responsable, red y meses por paquete',
        'Vista paginada del diccionario vigente del T-14 para localizar cualquier paquete durante las preguntas de la comisión.',
        seconds=30,
        steps=1,
        backup=True,
    )

# Tiempos de la versión con bloque EDT ampliado (tres láminas): se recortan láminas de apoyo para volver a 15:00.
# Recorrido principal en tres actos (título, segundos). Lo que no está aquí va al respaldo, salvo DESCARTE.
RECORRIDO = [
    ('Revisión 2 · Caso Transporte de Carga', 15),
    ('Una salida segura exige información confiable.', 25),
    ('Cambios principales del Informe 2', 40),
    ('Qué construimos', 3),
    ('La solución es híbrida: nube, sitio y flota.', 40),
    ('Ocho capas, cada una con su producto.', 45),
    ('Un viaje se autoriza o se bloquea en 30 segundos.', 40),
    ('Cada nodo declara su hardware y su enlace.', 40),
    ('La arquitectura física completa, parte por parte.', 45),
    ('El camión es un nodo que opera sin red.', 35),
    ('Cada dato vive en el motor que su uso exige.', 35),
    ('Si se corta el enlace, la operación sigue.', 35),
    ('Cómo lo ejecutamos', 3),
    ('La EDT cubre todo el alcance en 13 elementos.', 35),
    ('Cada elemento baja a paquetes que se pueden aceptar.', 40),
    ('El diccionario hace verificable cada paquete.', 40),
    ('La red de 25 actividades define la ruta crítica.', 65),
    ('¿Y si la construcción de la Etapa 1 se atrasa 10 días?', 40),
    ('El paquete 11.1 se controla con la compuerta G13.', 35),
    ('La transición se ejecuta en dos etapas niveladas.', 45),
    ('Cómo lo protegemos', 3),
    ('Veintiocho riesgos evaluados; ninguno queda alto.', 45),
    ('Siete riesgos altos, cada uno con su disparador.', 45),
    ('R-28: cuatro causas, cuatro barreras antes del evento.', 45),
    ('Las reservas y holguras absorben el riesgo del plan.', 50),
    ('Tres compromisos que se pueden verificar.', 20),
    ('Preguntas y discusión', 5),
]
RESPALDO_ORDEN = [
    'Registro de riesgos · R-01 a R-14.',
    'Registro de riesgos · R-15 a R-28.',
    'El AMFE completo: diez modos bajo NPR 50.',
    'El árbol de fallas modela compuertas OR y AND.',
    'Sin documento conforme, el viaje no puede salir.',
    'La implantación converge en producción aceptada.',
    'Los hitos avanzan por evidencia y protegen fechas.',
    'La reversión opera con tiempos y roles definidos.',
    'La calidad se controla desde el código hasta terreno.',
    'Las correcciones vinculan decisiones y pruebas.',
    'Las cinco innovaciones distinguen TRL y condiciones.',
    'La evidencia mantiene límites metodológicos explícitos.',
]
# Superadas por el rediseño o con datos que ya no coinciden con el S4/T-16 vigentes.
DESCARTE = {
    'La solución conecta cabina, terminal y torre.',
    'La arquitectura integra borde, nube y trazabilidad.',
    'El método P×I evalúa y reduce la exposición.',
    'Cada riesgo crítico tiene dueño, disparador y respuesta.',
    'El AMFE prioriza controles de detección temprana.',
    'Cada riesgo crítico tiene dueño, umbral y respuesta.',
}
by_title = {s['title']: s for s in SLIDES}
missing = [ti for ti, _ in RECORRIDO if ti not in by_title] + [ti for ti in RESPALDO_ORDEN if ti not in by_title]
assert not missing, missing
main = []
for ti, sec in RECORRIDO:
    s = by_title[ti]
    s['seconds'], s['backup'] = sec, False
    main.append(s)
rest = [s for s in SLIDES if s['title'] not in DESCARTE and s not in main]
for s in rest:
    s['backup'] = True
rest.sort(key=lambda s: RESPALDO_ORDEN.index(s['title']) if s['title'] in RESPALDO_ORDEN else len(RESPALDO_ORDEN))
SLIDES[:] = main + rest
EXPOSICION_SEGUNDOS = sum(s['seconds'] for s in main)
MARGEN_SEGUNDOS = 15 * 60 - EXPOSICION_SEGUNDOS
for n, s in enumerate(SLIDES, 1):
    s['id'] = f's{n:02}'
    if s['backup']:
        s['eyebrow'] = re.sub(r'^RESPALDO(?:\s+\d+)?\s*/',
                              f'RESPALDO R{n - len(main)} /', s['eyebrow'])
import base64
FONT_FACES = ''.join(
    "@font-face{font-family:'AuditSans';font-style:normal;font-weight:%s;font-display:block;src:url(data:font/woff2;base64,%s) format('woff2')}"
    % (weight, base64.b64encode((BASE / 'assets/fonts' / f'AuditSans-{name}.woff2').read_bytes()).decode())
    for name, weight in (('Regular', '100 500'), ('Bold', '600 900'))
)
css = FONT_FACES + '''*{box-sizing:border-box}html,body{margin:0;width:100%;height:100%;overflow:hidden;background:#ffffff;color:#102d3e;font-family:'AuditSans','Liberation Sans',Arial,sans-serif}body{position:relative}#stage{width:1920px;height:1080px;position:absolute;transform-origin:0 0}.scene{position:absolute;inset:0;width:100%;height:100%;overflow:hidden;background:#ffffff;opacity:0;visibility:hidden;pointer-events:none}.clip{position:absolute;inset:0}.scene::after{content:"";position:absolute;left:96px;right:96px;bottom:104px;height:1px;background:#bdced6}.eyebrow{position:absolute;left:96px;top:62px;font-size:23px;letter-spacing:.15em;color:#006b7d;font-weight:600}.brand{position:absolute;right:96px;top:49px;width:142px;height:54px;object-fit:contain}.headline{position:absolute;left:96px;top:132px;width:1710px;font-size:68px;line-height:1.1;font-weight:600;letter-spacing:-.035em;margin:0}.visual{position:absolute;left:96px;top:296px;width:1728px;height:650px;overflow:visible;font-family:'AuditSans','Liberation Sans',Arial,sans-serif}.source{position:absolute;left:96px;bottom:54px;font-size:19px;color:#48606e;max-width:1540px}.folio{position:absolute;right:96px;bottom:52px;font-size:23px;color:#48606e}.scene.cover .headline,.scene.operational .headline,.scene.closing .headline,.scene.section .headline{display:none}.scene.section{background:#102d3e}.scene.section .brand,.scene.section .folio,.scene.section .source,.scene.section::after{display:none}.scene.section .eyebrow{color:#7fb3bf;top:118px}.scene.section .visual{top:215px}.scene.cover .visual,.scene.operational .visual,.scene.closing .visual{top:215px}.scene.cover .eyebrow,.scene.operational .eyebrow,.scene.closing .eyebrow{top:118px}.scene.cover .brand,.scene.operational .brand,.scene.closing .brand{top:100px;width:220px;height:80px}@media(prefers-reduced-motion:reduce){*{scroll-behavior:auto}}'''

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
function fitCards(){
scenes.forEach(sc=>{
  const svg=sc.querySelector('svg.visual');
  if(!svg)return;
  const cards=[...svg.querySelectorAll('rect[data-card]')].map(r=>({x:+r.getAttribute('x'),y:+r.getAttribute('y'),w:+r.getAttribute('width'),h:+r.getAttribute('height')}));
  svg.querySelectorAll('text').forEach(t=>{
    if(t.closest('[data-badge]')||t.closest('g[transform]'))return;
    const b=t.getBBox();
    if(!b.width)return;
    const px=b.x+b.width/2,py=b.y+b.height/2;
    const c=cards.filter(r=>px>=r.x&&px<=r.x+r.w&&py>=r.y&&py<=r.y+r.h).sort((m,n)=>m.w*m.h-n.w*n.h)[0];
    if(!c)return;
    const anchor=t.getAttribute('text-anchor')||'start';
    const room=anchor==='middle'?c.w-32:anchor==='end'?b.x+b.width-c.x-16:c.x+c.w-16-b.x;
    if(!t.dataset.fs)t.dataset.fs=t.getAttribute('font-size');
    if(b.width>room){const fs=parseFloat(t.getAttribute('font-size'));t.setAttribute('font-size',(fs*Math.max(.78,room/b.width)).toFixed(1));}
  });
});
}
function fitBadges(){
document.querySelectorAll('g[data-badge]').forEach(g=>{
  const r=g.querySelector('rect'),t=g.querySelector('text');
  if(!r||!t)return;
  if(!r.dataset.w){r.dataset.w=r.getAttribute('width');t.dataset.fs=t.getAttribute('font-size');}
  const w=Number(r.dataset.w),h=Number(r.getAttribute('height')),x=Number(r.getAttribute('x'));
  r.setAttribute('width',w);t.setAttribute('font-size',t.dataset.fs);t.setAttribute('x',(x+w/2).toFixed(1));
  const need=t.getComputedTextLength()+h*.9;
  if(need<=w)return;
  // Primero se reduce la letra para no invadir lo vecino; sólo si no basta se ensancha la pastilla.
  const k=Math.max(.8,(w-h*.9)/(need-h*.9));
  t.setAttribute('font-size',(parseFloat(t.dataset.fs)*k).toFixed(1));
  const need2=t.getComputedTextLength()+h*.9;
  if(need2>w){r.setAttribute('width',need2.toFixed(1));t.setAttribute('x',(x+need2/2).toFixed(1));}
});
}
function centerIcons(){
  document.querySelectorAll('g[data-center]').forEach(g=>{
    const [cx,cy]=g.dataset.center.split(' ').map(Number),s=Number(g.dataset.scale)||1,b=g.getBBox();
    g.setAttribute('transform',`translate(${(cx-s*(b.x+b.width/2)).toFixed(1)} ${(cy-s*(b.y+b.height/2)).toFixed(1)}) scale(${s})`);
  });
}
centerIcons();
function fitText(){
  document.querySelectorAll('svg.visual text').forEach(t=>{if(t.dataset.fs&&!t.closest('[data-badge]'))t.setAttribute('font-size',t.dataset.fs);});
  fitBadges();fitCards();
}
fitText();
if(document.fonts)Promise.all(['400 20px AuditSans','700 20px AuditSans'].map(f=>document.fonts.load(f))).then(()=>{fitText();document.documentElement.dataset.fontsReady='true';});
const master=gsap.timeline({paused:true});
const flowLoops=[];
const truckLoops=[];
scenes.forEach((scene,i)=>{
  const tl=gsap.timeline({paused:true});
  const head=scene.querySelector('.headline');
  const eyebrow=scene.querySelector('.eyebrow');
  if(head)tl.fromTo(head,{opacity:0,y:26},{opacity:1,y:0,duration:.7,ease:'power3.out'},0);
  if(eyebrow)tl.fromTo(eyebrow,{opacity:0,x:-18},{opacity:1,x:0,duration:.6,ease:'power2.out'},0);
  scene.querySelectorAll('[data-step]').forEach(el=>{
    const at=Number(el.dataset.step)*2;
    const items=el.querySelectorAll('[data-item]');
    if(items.length){
      tl.fromTo(el,{opacity:0},{opacity:1,duration:.01},at);
      tl.fromTo(items,{opacity:0,y:18},{opacity:1,y:0,duration:.55,ease:'power2.out',stagger:Math.min(.07,.9/items.length)},at);
    }else{
      tl.fromTo(el,{opacity:0,y:22},{opacity:1,y:0,duration:.78,ease:'power2.out'},at);
    }
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
  scene.querySelectorAll('[data-dim-at]').forEach(d=>{
    tl.to(d,{opacity:.2,duration:.5,ease:'power1.out'},Number(d.dataset.dimAt)*2);
  });
  scene.querySelectorAll('svg[data-zoom]').forEach(z=>{
    const views=JSON.parse(z.dataset.zoom);
    views.slice(1).forEach((v,k)=>{
      tl.fromTo(z,{attr:{viewBox:views[k]}},{attr:{viewBox:v},duration:.95,ease:'power2.inOut',immediateRender:false},(k+1)*2);
    });
  });
  scene.querySelectorAll('[data-show-at]').forEach(el=>{
    tl.fromTo(el,{opacity:0},{opacity:1,duration:.45,ease:'power1.out'},Number(el.dataset.showAt)*2+.3);
    if(el.dataset.hideAt)tl.fromTo(el,{opacity:1},{opacity:0,duration:.3,ease:'power1.in',immediateRender:false},Number(el.dataset.hideAt)*2);
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
let shown=-1;
function visibility(t){
  const index=Math.min(scenes.length-1,Math.max(0,Math.floor(t/10)));
  const isQa=document.documentElement.dataset.qa==='true'|| window.parent?.document?.documentElement?.dataset?.qa==='true';
  if(index!==shown){
    const prev=shown;
    shown=index;
    scenes.forEach((s,i)=>{
      if(i===index||i===prev)return;
      gsap.killTweensOf(s);
      s.style.opacity='0';s.style.visibility='hidden';s.style.pointerEvents='none';
    });
    const inc=scenes[index];
    const clip=inc.querySelector('.clip');
    gsap.killTweensOf(inc);
    inc.style.visibility='visible';inc.style.pointerEvents='auto';
    if(prev>=0&&!isQa&&!matchMedia('(prefers-reduced-motion: reduce)').matches){
      const out=scenes[prev];
      const dir=index>prev?1:-1;
      out.style.pointerEvents='none';
      gsap.killTweensOf(out);
      gsap.to(out,{opacity:0,duration:.32,ease:'power1.in',onComplete:()=>{if(shown!==prev)out.style.visibility='hidden';}});
      gsap.fromTo(inc,{opacity:0},{opacity:1,duration:.5,delay:.1,ease:'power1.out'});
      if(clip)gsap.fromTo(clip,{x:40*dir},{x:0,duration:.75,delay:.1,ease:'power3.out'});
    }else{
      if(prev>=0){const out=scenes[prev];out.style.opacity='0';out.style.visibility='hidden';out.style.pointerEvents='none';}
      inc.style.opacity='1';
      if(clip)gsap.set(clip,{x:0});
    }
  }
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
wrapper = '''<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>audIT · Revisión 2 · Transportes Curimón</title><script src="assets/hyperframes-player.global.js"></script><script src="assets/hyperframes-slideshow.global.js"></script><style>*{box-sizing:border-box}html,body{margin:0;width:100%;height:100%;overflow:hidden;background:#ffffff}hyperframes-slideshow{display:block;position:relative;width:100vw;height:100vh;outline:none}hyperframes-player{position:absolute;inset:0} [data-hf-chrome]{display:none!important}#surface{position:absolute;inset:0;z-index:8;background:transparent;cursor:default}#surface.idle{cursor:none}[data-hf-presenting="true"]~#surface{display:none}body:has([data-hf-presenting="true"]) #surface{display:none}body:has([data-hf-presenting="true"]) [data-hf-chrome]{display:block!important}</style></head><body><hyperframes-slideshow tabindex="0" notes-storage-key="audit-curimon-revision2"><hyperframes-player interactive src="composition/index.html"></hyperframes-player><script type="application/hyperframes-slideshow+json">''' + island + '''</script></hyperframes-slideshow><div id="surface" aria-hidden="true"></div><script src="harness.js"></script></body></html>'''
(BASE / 'index.html').write_text(wrapper, encoding='utf-8')
embedded = json.dumps(raw, ensure_ascii=False).replace('</', '<\\/')
wrapper = wrapper.replace('<title>', '<link rel="icon" href="data:,"><title>')
wrapper = wrapper.replace(' interactive src="composition/index.html"', ' interactive')
wrapper = wrapper.replace('<script src="harness.js">', '<script type="application/json" id="embedded-composition">' + embedded + '</script><script src="harness.js">')
(BASE / 'index.html').write_text(wrapper, encoding='utf-8')
(BASE / 'escenas.json').write_text(json.dumps([{k: v for k, v in s.items() if k != 'content'} for s in SLIDES], ensure_ascii=False, indent=2), encoding='utf-8')
(BASE / 'NOTAS-EXPOSICION.md').write_text(
    f'# Guion de exposición\n\nObjetivo: {EXPOSICION_SEGUNDOS // 60} minutos y {EXPOSICION_SEGUNDOS % 60} segundos + {MARGEN_SEGUNDOS} segundos de margen. No hay asignación ficticia de expositores.\n\n'
    + '\n\n'.join(
        f"## {i + 1}. {s['title']}\n\nTiempo: {s['seconds']} s.{' Respaldo.' if s['backup'] else ''}\n\n{s['notes']}\n\nFuente: {s['source']}"
        for i, s in enumerate(SLIDES)
    ),
    encoding='utf-8',
)
print(f'{len(manifest["slides"])} escenas principales; {len(manifest["slideSequences"][0]["slides"])} de respaldo; {sum(s["seconds"] for s in SLIDES if not s["backup"])} segundos objetivo.')
