#!/usr/bin/env python3
"""Incorpora diagramas y carta Gantt vigentes a la presentación Ruta Curimón.

Reemplaza las láminas «arquitectura» y «plan» del recorrido principal, agrega
láminas de respaldo (infraestructura física, ruta crítica y mapa de riesgos),
renumera los pies de página y actualiza el índice. Es idempotente: se puede
volver a ejecutar después de cambiar los formularios del informe.

Fuentes (propuesta final):
- Infraestructura física: recursos/Formato-Oferta-audIT/figuras/04-arquitectura/fisica-lamina-*.png (D4, S4.2/T-11)
- Ventanas por elemento EDT: subdocumentos/07-plan-trabajo/graficos/conciliacion-3.2/puente.json (T-14/T-18)
- Red y holguras: salida/final/AUDIT-Formulario-T-15.md, Tabla 7.5
- Riesgos: salida/final/AUDIT-Formulario-T-16.md
- Meses de hitos de pago: configuracion/economico.tex (E-25)

Uso: python3 tools/ruta_curimon_graficos.py
"""
from pathlib import Path
from io import BytesIO
import base64
import html
import json
import re

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / 'Presentacion-N3-Ruta-Curimon.html'
OFERTA = ROOT / 'recursos/Formato-Oferta-audIT'
FIG = OFERTA / 'figuras/04-arquitectura'
ICONOS = ROOT / 'Presentacion-Revision(FINAL)Test/assets/iconos'
PUENTE = OFERTA / 'subdocumentos/07-plan-trabajo/graficos/conciliacion-3.2/puente.json'
T15 = OFERTA / 'salida/final/AUDIT-Formulario-T-15.md'
T16 = OFERTA / 'salida/final/AUDIT-Formulario-T-16.md'
ECON = OFERTA / 'configuracion/economico.tex'

INK = '#182a24'
GREEN = '#235842'
SAGE = '#dce7d7'
LINE = '#a7bbab'
MUTED = '#4d6257'
AMBER = '#795020'
WARM = '#f6ecd9'
PAPER = '#fffef9'
PALE = '#e8eee4'
FONT = 'DM,sans-serif'
TITLE = 'Barlow,sans-serif'
DIA_MES = 20  # T-15: 20 días hábiles por mes contractual

# Láminas que genera este script, en el orden en que se insertan tras «continuidad».
NUEVAS_RESPALDO = ['infra-nube', 'infra-sala', 'infra-terminales', 'infra-flota', 'ruta-critica', 'riesgos']


def esc(s):
    return html.escape(str(s), quote=True)


def icono(nombre):
    data = (ICONOS / f'{nombre}.svg').read_bytes()
    return 'data:image/svg+xml;base64,' + base64.b64encode(data).decode()


def png(nombre, ancho=2100):
    img = Image.open(FIG / f'{nombre}.png').convert('RGB')
    img = img.resize((ancho, round(img.height * ancho / img.width)), Image.LANCZOS)
    buf = BytesIO()
    img.save(buf, 'PNG', optimize=True)
    return 'data:image/png;base64,' + base64.b64encode(buf.getvalue()).decode()


def t(x, y, s, size=24, color=INK, weight=400, anchor='start', family=FONT):
    return (f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" font-weight="{weight}" '
            f'fill="{color}" text-anchor="{anchor}">{esc(s)}</text>')


def caja(x, y, w, h, fill=PAPER, stroke=LINE, width=2, rx=6, dash=''):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{width}"{d}/>'


def flecha(x1, y1, x2, y2, color=GREEN, width=3.5, dash='', marker='fin'):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    if color == AMBER:
        marker = 'finA'
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{width}"{d} '
            f'marker-end="url(#{marker})"/>')


def ruta(d, color=GREEN, width=3.5, dash='', marker='fin'):
    da = f' stroke-dasharray="{dash}"' if dash else ''
    return f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{width}"{da} marker-end="url(#{marker})"/>'


def img(x, y, size, href):
    return f'<image x="{x}" y="{y}" width="{size}" height="{size}" href="{href}"/>'


def defs():
    return ''.join(['<defs>'] + [
        f'<marker id="{i}" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto">'
        f'<path d="M0,0 L10,5 L0,10 z" fill="{c}"/></marker>' for i, c in (('fin', GREEN), ('finA', AMBER))] + ['</defs>'])


def lista(x, y, items, size=24, gap=40, color=INK):
    """Líneas con viñeta cuadrada; devuelve el SVG."""
    out = []
    for i, s in enumerate(items):
        yy = y + i * gap
        out.append(f'<rect x="{x}" y="{yy - size * .42}" width="9" height="9" fill="{GREEN}"/>')
        out.append(t(x + 22, yy, s, size, color))
    return ''.join(out)


def chip(x, y, w, s, size=22, fill=SAGE, color=GREEN):
    return caja(x, y, w, 40, fill, fill, 0, 20) + t(x + w / 2, y + 28, s, size, color, 700, 'middle')


# ---------------------------------------------------------------- Arquitectura

def svg_arquitectura():
    W, H = 1712, 612
    o = [f'<svg class="diagram" viewBox="0 0 {W} {H}" role="img" aria-label="Arquitectura híbrida: flota, terminales, sala de San Bernardo, Azure Chile Central y Brazil South">', defs()]

    # Fondo de Azure primero, para que las puntas de los enlaces queden visibles
    o.append(caja(910, 48, 600, 560, '#f4f7f1', GREEN, 3))
    # Flota
    o.append(caja(0, 0, 420, 292, PAPER, GREEN, 3))
    o.append(t(24, 44, 'Flota · 182 kits audIT', 31, GREEN, 700, family=TITLE))
    o.append(lista(28, 96, ['Equipo iWave G26I a bordo', 'SQLite WAL · búfer 288 h', 'CAN J1939 y lector DESFire', 'LTE con GNSS e Iridium'], 24, 40))
    o.append(chip(24, 236, 372, '148 propios + 34 de terceros', 22))

    # Terminales
    o.append(caja(0, 322, 420, 230, PAPER, GREEN, 3))
    o.append(t(24, 366, '4 terminales', 31, GREEN, 700, family=TITLE))
    o.append(lista(28, 406, ['ICS-6280 activo y en espera', 'Router 5G con doble SIM', 'Portería y patio con balizas'], 24, 36))
    o.append(chip(24, 498, 372, 'Opera 24 h sin enlace', 22, WARM, AMBER))

    # Enlaces de la flota hacia IoT Hub
    o.append(flecha(420, 128, 932, 128))
    o.append(t(676, 112, 'LTE · operador móvil', 24, INK, 700, 'middle'))
    o.append(flecha(420, 232, 932, 232, dash='12 9'))
    o.append(t(676, 216, 'Satélite Iridium · mensajes críticos', 24, INK, 700, 'middle'))
    o.append(t(676, 262, 'hasta 340 bytes por mensaje', 21, MUTED, 400, 'middle'))

    # Sala San Bernardo
    o.append(caja(466, 322, 384, 230, PAPER, GREEN, 3))
    o.append(t(488, 366, 'Sala San Bernardo', 31, GREEN, 700, family=TITLE))
    o.append(img(488, 390, 32, icono('si-dell')) + t(530, 415, '2 servidores R360', 23))
    o.append(img(488, 430, 32, icono('si-fortinet')) + t(530, 455, 'FortiGate 90G en HA', 23))
    o.append(lista(496, 495, ['UPS A/B · generador 24 h'], 23))
    o.append(t(488, 532, 'Anticorrupción: SGT 2013 y contable', 19, MUTED))
    # Sala -> red central (ExpressRoute y VPN de respaldo)
    o.append(flecha(850, 500, 932, 500))
    o.append(flecha(850, 540, 932, 540, dash='12 9'))
    # Terminales -> VPN Gateway
    o.append(ruta('M420,540 L450,540 L450,584 L932,584'))
    o.append(t(660, 608, 'VPN IPsec por 5G desde cada terminal', 21, MUTED, 400, 'middle'))

    # Azure Chile Central (los recuadros internos van después de los enlaces)
    o.append(t(932, 88, 'Azure Chile Central', 31, GREEN, 700, family=TITLE))
    o.append(t(1180, 88, '· región primaria, 3 zonas', 21, MUTED))
    # Usuarios -> borde
    o.append(t(1500, 22, 'Torre, clientes y transportistas', 21, INK, 700, 'end'))
    o.append(flecha(1470, 30, 1470, 106))

    def bloque(x, y, w, h, titulo, items):
        s = [caja(x, y, w, h, PAPER, LINE, 2), t(x + 14, y + 30, titulo, 21, GREEN, 700)]
        n = len(items)
        for i, (ic, l1, l2) in enumerate(items):
            cx = x + w * (i + .5) / n
            s.append(img(cx - 26, y + 44, 52, icono(ic)))
            s.append(t(cx, y + 122, l1, 20, INK, 700, 'middle'))
            if l2:
                s.append(t(cx, y + 146, l2, 18, MUTED, 400, 'middle'))
        return ''.join(s)

    o.append(bloque(926, 108, 164, 160, 'Integración', [('azure-iothub', 'IoT Hub', 'Event Hubs')]))
    o.append(img(1036, 152, 40, icono('azure-eventhubs')))
    o.append(bloque(1122, 108, 164, 160, 'Aplicación', [('azure-aks', 'AKS', 'nodos en 3 zonas')]))
    o.append(bloque(1318, 108, 178, 160, 'Borde', [('azure-apim', 'Front Door', 'y API Management')]))
    o.append(img(1411, 152, 40, icono('azure-frontdoor')))
    o.append(flecha(1090, 188, 1120, 188))
    o.append(flecha(1318, 188, 1288, 188))
    o.append(flecha(1204, 268, 1204, 296))
    o.append(bloque(926, 298, 570, 160, 'Datos', [
        ('azure-postgresql', 'PostgreSQL', 'transaccional'),
        ('azure-postgresql', 'PostgreSQL', 'series Timescale'),
        ('azure-storage', 'Blob', 'inmutable ZRS'),
        ('azure-keyvault', 'Key Vault', 'Premium'),
    ]))
    o.append(bloque(926, 446 + 22, 570, 128, 'Red central', []))
    for i, (ic, l1, l2) in enumerate([('azure-expressroute', 'ExpressRoute', '100 Mbit/s'), ('azure-vpngateway', 'Puerta VPN', 'respaldo y terminales'), ('azure-firewall', 'Firewall', 'Premium')]):
        cx = 926 + 570 * (i + .5) / 3
        o.append(img(cx - 20, 500, 40, icono(ic)))
        o.append(t(cx, 562, l1, 20, INK, 700, 'middle'))
        o.append(t(cx, 584, l2, 18, MUTED, 400, 'middle'))

    # Brazil South
    o.append(caja(1556, 48, 156, 560, PAPER, AMBER, 3, dash='10 7'))
    o.append(t(1634, 90, 'Brazil South', 23, AMBER, 700, 'middle', TITLE))
    o.append(t(1634, 122, 'en espera', 20, MUTED, 400, 'middle'))
    o.append(img(1608, 160, 52, icono('azure-postgresql')))
    o.append(img(1608, 228, 52, icono('azure-aks')))
    o.append(t(1634, 330, 'RTO', 22, MUTED, 400, 'middle'))
    o.append(t(1634, 372, '4 h', 40, AMBER, 700, 'middle', TITLE))
    o.append(t(1634, 430, 'RPO', 22, MUTED, 400, 'middle'))
    o.append(t(1634, 472, '15 min', 40, AMBER, 700, 'middle', TITLE))
    o.append(t(1634, 540, 'réplica', 20, MUTED, 400, 'middle'))
    o.append(t(1634, 564, 'asíncrona', 20, MUTED, 400, 'middle'))
    o.append(flecha(1496, 378, 1554, 378, AMBER, 3.5, '10 7'))
    o.append('</svg>')
    return ''.join(o)


# ---------------------------------------------------------------- Calendario

def hitos_e25():
    meses = {h: int(m) for h, m in re.findall(r'\\HitoPago\{(H\d+)\}\{\d+\}\{(\d+)\}', ECON.read_text(encoding='utf-8'))}
    assert len(meses) == 12, meses
    return meses


def red_t15():
    filas = {}
    txt = T15.read_text(encoding='utf-8')
    bloque = txt.split('**Tabla 7.5.**', 1)[1]
    for linea in bloque.splitlines()[1:]:
        if not linea.startswith('|'):
            if filas:
                break
            continue
        c = [x.strip() for x in linea.strip('|').split('|')]
        if c[0] in ('ID', '---'):
            continue
        filas[c[0]] = dict(id=c[0], nombre=c[1], es=int(c[4]), ef=int(c[5]), ht=int(c[8]))
    assert 'H12' in filas and filas['H12']['ef'] == 21 * DIA_MES, 'T-15 sin H12 en el día 420'
    return filas


def dia_hito(red, h):
    return red[h]['es']


def x_mes(m, x0, w):
    """Escala con quiebre: M1–M24 ocupan el 82 % del ancho; M25–M56, el resto."""
    corte = 24
    a = w * .82
    if m <= corte:
        return x0 + a * m / corte
    return x0 + a + (w - a) * (m - corte) / (56 - corte)


def svg_calendario():
    P = json.loads(PUENTE.read_text(encoding='utf-8'))['paquetes'].values()
    grupos = ['Gestión', 'Levantamiento y diseño', 'Plataforma', 'Equipo a bordo', 'Capacidades E1',
              'Integraciones', 'Datos y migración', 'Capacidades E2', 'Adhesión de transportistas',
              'Calidad y pruebas', 'Implantación y estabilización', 'Innovaciones', 'Operación']
    filas = []
    for i, nombre in enumerate(grupos, 1):
        meses = sorted({m for p in P if p['codigo'].split('.')[0] == str(i) for a, b in p['ventanas'] for m in range(a, b + 1)})
        ventanas = []
        for m in meses:
            if ventanas and ventanas[-1][1] + 1 == m:
                ventanas[-1][1] = m
            else:
                ventanas.append([m, m])
        filas.append((str(i), nombre, ventanas))
    red = red_t15()
    meses = hitos_e25()
    for h, m in meses.items():  # el día del hito cae dentro de su mes contractual
        assert (m - 1) * DIA_MES <= dia_hito(red, h) <= m * DIA_MES, (h, m, dia_hito(red, h))

    W, H = 1712, 612
    x0, w = 418, 1280
    top = 120
    rh = 34
    o = [f'<svg class="diagram" viewBox="0 0 {W} {H}" role="img" aria-label="Carta Gantt M1 a M56 con los doce hitos de pago">', defs()]
    bottom = top + rh * len(filas)
    # Temporada de fruta (diciembre a abril; M1 = febrero de 2027)
    for m in range(1, 57):
        if (m % 12) + 1 in (12, 1, 2, 3, 4):
            xa, xb = x_mes(m - 1, x0, w), x_mes(m, x0, w)
            o.append(f'<rect x="{xa:.1f}" y="{top - 8}" width="{xb - xa:.1f}" height="{bottom - top + 8}" fill="{WARM}"/>')
    # Eje
    for m in [1, 3, 6, 9, 12, 15, 18, 21, 24, 40, 56]:
        xa = x_mes(m - 1, x0, w) if m <= 24 else x_mes(m, x0, w)
        o.append(f'<line x1="{xa:.1f}" y1="{top - 8}" x2="{xa:.1f}" y2="{bottom}" stroke="{LINE}" stroke-width="1.5"/>')
        o.append(t(xa + (-4 if m == 56 else 4), top - 14, f'M{m}', 19, MUTED, 400, 'end' if m == 56 else 'start'))
    xq = x_mes(24, x0, w)
    o.append(f'<line x1="{xq:.1f}" y1="{top - 8}" x2="{xq:.1f}" y2="{bottom + 6}" stroke="{INK}" stroke-width="2" stroke-dasharray="4 6"/>')
    # Hitos
    o.append(t(0, 70, 'Hitos de pago E-25', 24, AMBER, 700))
    for i, h in enumerate(sorted(meses, key=lambda k: dia_hito(red, k))):
        d = dia_hito(red, h)
        x = x_mes(d / DIA_MES, x0, w)
        y = 66
        o.append(f'<path d="M{x:.1f},{y - 10} L{x + 10:.1f},{y} L{x:.1f},{y + 10} L{x - 10:.1f},{y} z" fill="{AMBER}"/>')
        o.append(f'<line x1="{x:.1f}" y1="{y + 10}" x2="{x:.1f}" y2="{top - 30}" stroke="{AMBER}" stroke-width="1.5"/>')
        ly = 18 if i % 2 == 0 else 44
        o.append(t(x, ly, h, 20, AMBER, 700, 'middle'))
    # Producción E1 y E2
    for m, label in [(16, 'Producción E1'), (21, 'Producción E2')]:
        x = x_mes(m, x0, w)
        o.append(f'<line x1="{x:.1f}" y1="{top - 8}" x2="{x:.1f}" y2="{bottom}" stroke="{GREEN}" stroke-width="3"/>')
    # Filas
    for i, (cod, nombre, ventanas) in enumerate(filas):
        y = top + i * rh
        if i % 2 == 0:
            o.append(f'<rect x="0" y="{y}" width="{x0 - 10}" height="{rh}" fill="{PALE}"/>')
        o.append(t(10, y + 26, cod, 21, GREEN, 700))
        o.append(t(50, y + 26, nombre, 22, INK))
        for a, b in ventanas:
            xa, xb = x_mes(a - 1, x0, w), x_mes(b, x0, w)
            color = AMBER if cod == '13' else GREEN
            o.append(f'<rect x="{xa:.1f}" y="{y + 9}" width="{max(xb - xa, 6):.1f}" height="{rh - 18}" rx="4" fill="{color}"/>')
    # Leyenda
    ly = bottom + 44
    o.append(f'<rect x="0" y="{ly - 18}" width="34" height="18" fill="{WARM}" stroke="{LINE}"/>' + t(44, ly - 2, 'Temporada de fruta, dic.–abr.', 21, MUTED))
    o.append(f'<line x1="380" y1="{ly - 9}" x2="414" y2="{ly - 9}" stroke="{GREEN}" stroke-width="3"/>' + t(424, ly - 2, 'Paso a producción: M16 (E1) y M21 (E2)', 21, MUTED))
    o.append(f'<line x1="890" y1="{ly - 9}" x2="924" y2="{ly - 9}" stroke="{INK}" stroke-width="2" stroke-dasharray="4 6"/>' + t(934, ly - 2, 'Desde M24 la escala se comprime: solo operación', 21, MUTED))
    o.append('</svg>')
    return ''.join(o)


GRUPOS_RED = [
    ('Levantamiento y diseño', ['A01', 'A02', 'R-H1', 'A05', 'R-H2']),
    ('Ambientes y sala', ['A07', 'R-H3', 'A07-SALA']),
    ('Equipo a bordo y montaje', ['A04-HW', 'A11-LECT', 'A11-HOM', 'A11-PIL', 'M7-KIT', 'M8-KIT', 'M9-KIT', 'A11-INN3']),
    ('Adhesión de transportistas', ['A06-ANEXO', 'A06-LOTE', 'A06-CAMP', 'A06-H12']),
    ('Construcción E1 · 8 sprints', ['A09-1', 'A09-2', 'A09-3', 'A09-4', 'A09-5', 'A09-6', 'A09-7', 'A09-8', 'R-H4']),
    ('Integraciones y migración', ['A08-VIG', 'A08-HIST1', 'A08-BI1', 'A10-CONT', 'A10-POS', 'A10-OEM', 'A10-TALLER', 'A10-LEG', 'HIST-VALID']),
    ('Certificación E1 y reserva', ['A12-SIS', 'A12-SEC', 'A12-UAT', 'R-H5', 'A14']),
    ('Capacitación (G13)', ['G13-Q', 'A13-FAM', 'A13-PRA']),
    ('Marcha blanca y producción E1', ['R-H6', 'A15', 'A18-INT', 'A19', 'R-H7']),
    ('Diseño y construcción E2', ['A17', 'R-H8', 'A20-1', 'A20-2', 'A20-3', 'A20-4', 'A20-5']),
    ('Certificación y marcha blanca E2', ['A22-SIS', 'A22-SEC', 'R-H9', 'R-H10', 'A23', 'R-H11', 'A24']),
    ('Producción E2', ['A25', 'R-H12']),
]


def svg_ruta_critica():
    red = red_t15()
    W, H = 1712, 640
    x0, w = 470, 1230
    top, rh = 50, 40
    xd = lambda d: x0 + w * d / (21 * DIA_MES)
    o = [f'<svg class="diagram" viewBox="0 0 {W} {H}" role="img" aria-label="Red T-15 agrupada, M1 a M21, con actividades críticas resaltadas">', defs()]
    bottom = top + rh * len(GRUPOS_RED)
    for m in range(1, 22):
        xa = xd((m - 1) * DIA_MES)
        if m % 2 == 1:
            o.append(f'<rect x="{xa:.1f}" y="{top - 6}" width="{w / 21:.1f}" height="{bottom - top + 6}" fill="{PALE}"/>')
        o.append(t(xa + w / 42, top - 16, f'M{m}', 19, MUTED, 400, 'middle'))
    for i, (nombre, ids) in enumerate(GRUPOS_RED):
        y = top + i * rh
        o.append(t(0, y + 28, nombre, 22, INK))
        for a in sorted(ids, key=lambda a: (red[a]['ht'] == 0, a.startswith('R-H'))):
            r = red[a]
            if r['ef'] <= r['es']:
                continue
            critica = r['ht'] == 0
            revision = a.startswith('R-H')
            fill = '#ffffff' if revision else (GREEN if critica else '#8fb39f')
            stroke = GREEN if critica else '#8fb39f'
            o.append(f'<rect x="{xd(r["es"]):.1f}" y="{y + 10}" width="{max(xd(r["ef"]) - xd(r["es"]) - 1, 3):.1f}" height="{rh - 20}" '
                     f'rx="3" fill="{fill}" stroke="{stroke}" stroke-width="2"/>')
    meses = hitos_e25()
    for h in meses:
        d = red[h]['es']
        x = xd(d)
        o.append(f'<line x1="{x:.1f}" y1="{top - 6}" x2="{x:.1f}" y2="{bottom}" stroke="{AMBER}" stroke-width="1.5" stroke-dasharray="3 5"/>')
        o.append(f'<path d="M{x:.1f},{bottom + 6} L{x + 10:.1f},{bottom + 16} L{x:.1f},{bottom + 26} L{x - 10:.1f},{bottom + 16} z" fill="{AMBER}"/>')
    for i, h in enumerate(sorted(meses, key=lambda k: red[k]['es'])):
        o.append(t(xd(red[h]['es']), bottom + 46 + (24 if i % 2 else 0), h, 18, AMBER, 700, 'middle'))
    for i, (fill, stroke, label) in enumerate([(GREEN, GREEN, 'Holgura total 0 (crítica)'), ('#8fb39f', '#8fb39f', 'Con holgura'), ('#fff', GREEN, 'Revisión de la contraparte')]):
        ly = bottom + 30 + i * 28
        o.append(f'<rect x="0" y="{ly - 16}" width="30" height="16" fill="{fill}" stroke="{stroke}" stroke-width="2"/>' + t(42, ly, label, 20, MUTED))
    o.append('</svg>')
    criticas = sum(1 for r in red.values() if r['ht'] == 0)
    return ''.join(o), len(red), criticas


# ---------------------------------------------------------------- Riesgos

def riesgos_t16():
    txt = T16.read_text(encoding='utf-8')
    R = {}
    for m in re.finditer(r'\\riesgoTDieciseis\{id=(R-\d+),.*?probabilidad=(\d), impacto=(\d), exposicion=(\d+)', txt):
        rid, p, i, e = m.group(1), int(m.group(2)), int(m.group(3)), int(m.group(4))
        assert p * i == e, rid
        R[rid] = dict(p=p, i=i, e=e)
    for linea in txt.split('**Tabla 8.1.**', 1)[1].splitlines():
        m = re.match(r'\| (R-\d+) \| ([^|]+)\|.*\| (\d+) a (\d+) \|$', linea.strip())
        if m:
            R[m.group(1)].update(origen=m.group(2).strip(), inicial=int(m.group(3)), residual=int(m.group(4)))
    assert len(R) == 36 and all('residual' in r for r in R.values()), len(R)
    assert all(r['inicial'] == r['e'] for r in R.values())
    return R


def svg_riesgos(R):
    W, H = 900, 660
    c = 110
    x0, y0 = 150, 20
    o = [f'<svg class="diagram" viewBox="0 0 {W} {H}" role="img" aria-label="Matriz de probabilidad e impacto de los 36 riesgos del T-16">']
    for p in range(1, 6):
        for i in range(1, 6):
            e = p * i
            fill = '#e9c9a0' if e >= 12 else (WARM if e >= 6 else SAGE)
            x, y = x0 + (i - 1) * c, y0 + (5 - p) * c
            o.append(f'<rect x="{x}" y="{y}" width="{c - 4}" height="{c - 4}" fill="{fill}"/>')
            ids = [k[2:] for k, r in sorted(R.items()) if r['p'] == p and r['i'] == i]
            for j in range(0, len(ids), 4):
                o.append(t(x + (c - 4) / 2, y + 30 + (j // 4) * 24, ' '.join(ids[j:j + 4]), 18, INK, 700, 'middle'))
            if not ids:
                o.append(t(x + c - 12, y + c - 14, str(e), 16, MUTED, 400, 'end'))
    for k in range(1, 6):
        o.append(t(x0 + (k - .5) * c - 2, y0 + 5 * c + 28, str(k), 22, MUTED, 700, 'middle'))
        o.append(t(x0 - 18, y0 + (5 - k) * c + c / 2 + 6, str(k), 22, MUTED, 700, 'end'))
    o.append(t(x0 + 2.5 * c, y0 + 5 * c + 62, 'Impacto', 24, INK, 700, 'middle'))
    o.append(f'<text x="70" y="{y0 + 2.5 * c}" font-family="{FONT}" font-size="24" font-weight="700" fill="{INK}" text-anchor="middle" transform="rotate(-90 70 {y0 + 2.5 * c})">Probabilidad</text>')
    o.append('</svg>')
    return ''.join(o)


# ---------------------------------------------------------------- Láminas

HEADER = '<header><span class="audit-logo" role="img" aria-label="audIT Soluciones Tecnológicas"></span><span>TFEP-01/2026 · Caso 10</span></header>'


def seccion(sid, kicker, titulo, cuerpo, fuente, notas, clase='slide'):
    return (f'<section id="{sid}" class="{clase}" aria-label="{esc(titulo)}">{HEADER}<div class="wrap">'
            f'<div class="kicker enter">{esc(kicker)}</div><h2 class="enter">{esc(titulo)}</h2>'
            f'<div class="body enter" style="--delay:.09s">{cuerpo}</div></div>'
            f'<footer><span>{esc(fuente)}</span><span>00</span></footer><p class="notes">{esc(notas)}</p></section>')


def lamina_figura(sid, titulo, figura, alt, puntos, fuente, notas):
    cuerpo = (f'<div class="figwrap"><img class="fisica" src="{png(figura)}" alt="{esc(alt)}">'
              f'<div class="figside">' + ''.join(f'<p>{esc(p)}</p>' for p in puntos) +
              '<p class="hint">Clic en la figura para ampliarla; Esc o cualquier tecla la cierra.</p></div></div>')
    return seccion(sid, 'Respaldo técnico · infraestructura física', titulo, cuerpo, fuente, notas, 'slide figslide')


def construir():
    s = {}
    s['arquitectura'] = seccion(
        'arquitectura', 'Propuesta técnica', 'Arquitectura híbrida', svg_arquitectura(),
        'FEP02 · §§2.1 y 3.1–3.4 · Oferta técnica S4.2, S5 y T-11',
        '2:45–3:45 · D3. Recorrer de izquierda a derecha. El equipo a bordo guarda los eventos en SQLite '
        'con 288 h de búfer y los envía al IoT Hub por LTE; los mensajes críticos usan Iridium. Cada terminal '
        'opera 24 h sin enlace y se conecta por VPN IPsec. La sala de San Bernardo llega a Azure por '
        'ExpressRoute de 100 Mbit/s, con VPN de respaldo, y aloja la capa anticorrupción hacia el sistema de '
        '2013 y el contable. En Azure, el registro transaccional mantiene la autoridad de asignación y las '
        'series de telemetría viven aparte. Los portales entran por Front Door y API Management, nunca directo '
        'a la base. Brazil South queda en espera con RTO 4 h y RPO 15 min. El detalle por nodo está en el respaldo.')
    s['plan'] = seccion(
        'plan', 'Implementación', 'Hitos que condicionan la entrega', svg_calendario(),
        'FEP01 · E-25, pp. 74–75 · Oferta técnica S7, T-14, T-15 y T-18',
        '5:55–6:45 · D4. Las barras son las ventanas de los 13 elementos de la EDT y los rombos, los doce hitos '
        'de pago de E-25. H3 en M6 habilita la infraestructura y el piloto de 10 kits; los lotes de montaje van de '
        'M7 a M9. H5 en M12 certifica la Etapa 1, H6 en M13 inicia su marcha blanca y H7 la pasa a producción '
        'en M16. La Etapa 2 fija su línea base en M14 con H8 y llega a producción en M21 con H12, cuando empieza '
        'la operación facturable. La banda ocre marca la temporada de fruta: la marcha blanca E1 cae en ella y por '
        'eso tiene reserva. E-25 asigna 60 % del precio de implementación a E1 y 40 % a E2.')
    s['infra-nube'] = lamina_figura(
        'infra-nube', 'Nube primaria y región de recuperación', 'fisica-lamina-c',
        'Azure Chile Central con redes de borde, aplicación, integración, gestión y datos; Brazil South en espera',
        ['Cinco subredes en Azure Chile Central, con AKS en 3 zonas.',
         'PostgreSQL transaccional y de series por separado.',
         'Brazil South en espera: RTO 4 h y RPO 15 min.',
         'Preproducción, QA y desarrollo con el mismo código de infraestructura.'],
        'Oferta técnica S4.2 y T-11 · lámina C', 'Respaldo. Usar si preguntan por zonas, segmentación o recuperación. '
        'Los números en círculo enlazan con las otras láminas: 1 y 2 San Bernardo, 5 terminales, 6 y 7 flota.')
    s['infra-sala'] = lamina_figura(
        'infra-sala', 'Sala de sitio en San Bernardo', 'fisica-lamina-a',
        'Sala de San Bernardo con rack de servidores, rack de comunicaciones, energía y capa anticorrupción',
        ['Dos Dell R360 y dos FortiGate 90G en alta disponibilidad.',
         'Circuitos A y B; 66 min con una UPS y 24 h de generador.',
         'ExpressRoute a Azure y VPN de respaldo por otro proveedor.',
         'La capa anticorrupción aísla el sistema de 2013 y el contable.'],
        'Oferta técnica S4.2 y T-11 · lámina A', 'Respaldo. La energía tiene un punto único declarado: el tablero de transferencia. '
        'La emisión tributaria sigue en el sistema contable del mandante.')
    s['infra-terminales'] = lamina_figura(
        'infra-terminales', 'Terminales y contrapartes', 'fisica-lamina-d',
        'Gabinete de terminal, portería y patio, y contrapartes por lotes y en línea',
        ['Gabinete con ICS-6280 activo y en espera, y router 5G con dos SIM.',
         'La terminal opera 24 h sin enlace.',
         'Portería con lectores; patio con FortiAP y Wi-Fi al equipo a bordo.',
         'Contrapartes por lotes o en línea, según su interfaz.'],
        'Oferta técnica S4.2 y T-11 · lámina D', 'Respaldo. Dos de las tres plataformas de terceros son solo de consulta y una no exporta: '
        'ese riesgo es R-08 en el T-16.')
    s['infra-flota'] = lamina_figura(
        'infra-flota', 'Flota y equipo a bordo', 'fisica-lamina-e',
        'Equipo iWave G26I en la cabina con LTE, Iridium, CAN, lector DESFire y memoria particionada',
        ['182 tractocamiones con equipo audIT: 148 propios y 34 de terceros.',
         'iWave G26I con elemento seguro, SQLite WAL y búfer de 288 h.',
         'LTE y GNSS; Iridium hasta 340 bytes por mensaje.',
         '192 tractocamiones de terceros se integran por sus plataformas.'],
        'Oferta técnica S4.2 y T-11 · lámina E', 'Respaldo. El mínimo del Caso son 72 h a bordo; dimensionamos 288 h. '
        'La memoria usa 2,4 de 8 GB y se actualiza con sistemas A y B.')
    svg_red, n_red, n_crit = svg_ruta_critica()
    s['ruta-critica'] = seccion(
        'ruta-critica', 'Respaldo de planificación', 'Ruta crítica hasta H12', svg_red,
        'Oferta técnica S7 · T-15, Tabla 7.5 · E-25',
        f'Respaldo. La red del T-15 tiene {n_red} nodos y {n_crit} con holgura total cero. Cada fila agrupa actividades; '
        'las barras verdes oscuras son críticas y las blancas, revisiones de la contraparte. H4, H7 y H12 terminan en su '
        'límite contractual; A14 y A23 son las reservas que protegen las marchas blancas (R-16 y R-17 del T-16).')
    R = riesgos_t16()
    altos = sum(r['inicial'] >= 12 for r in R.values())
    altos_res = sum(r['residual'] >= 12 for r in R.values())
    origen = {k: sum(r['origen'] == k for r in R.values()) for k in ('Mandante', 'Terceros', 'audIT')}
    lado = (f'<div class="riskside"><div class="stat warning"><strong>{altos} → {altos_res}</strong><b>riesgos de exposición alta</b>'
            f'<p>Iniciales con exposición 12 o más frente a los residuales tras mitigar.</p></div>'
            f'<div class="stat"><strong>{len(R)}</strong><b>riesgos evaluados</b><p>{origen["Terceros"]} de terceros, '
            f'{origen["audIT"]} de audIT y {origen["Mandante"]} del mandante.</p></div>'
            f'<p class="callout">Cada riesgo alto tiene disparador, responsable y plan de contingencia en S8.</p></div>')
    s['riesgos'] = seccion(
        'riesgos', 'Respaldo de riesgos', 'Mapa de los 36 riesgos', f'<div class="riskgrid">{svg_riesgos(R)}{lado}</div>',
        'Oferta técnica S8 · T-16, registro y Tabla 8.1',
        'Respaldo. La matriz ubica cada riesgo por su exposición inicial: probabilidad por impacto, de 1 a 5. '
        'Las celdas ocres son exposición alta. Los más citados: R-11 adhesión de transportistas, R-18 marcha blanca en '
        'temporada, R-23 ataque al portal, R-24 réplica en Brazil South y R-35 desconexión del equipo a bordo. '
        'R-06 salió del registro y su número no se reutiliza.')
    return s


CSS = '''
/* === Diagramas generados por tools/ruta_curimon_graficos.py === */
.diagram{width:100%;height:auto;display:block;overflow:visible;max-height:none}
#arquitectura .body,#plan .body,#ruta-critica .body{justify-content:flex-start}
.figslide .wrap{gap:12px}
.figslide .kicker{font-size:24px}
.figslide h2{font-size:56px}
.figwrap{display:grid;grid-template-columns:1036px 1fr;gap:40px;align-items:center}
.figwrap img.fisica{width:1036px;height:672px;max-width:none;max-height:none;background:#fff;border:2px solid var(--line);cursor:zoom-in}
.figwrap img.fisica.zoomed{position:fixed;left:128px;top:0;width:1664px;height:1080px;z-index:20;border:0;cursor:zoom-out;box-shadow:0 0 0 200px #182a24b0}
.figside .hint{font-size:24px;border:0;padding:0;color:var(--muted)}
.figside{display:grid;gap:22px}
.figside p{font-size:31px;line-height:1.2;border-left:6px solid var(--green);padding-left:18px}
.riskgrid{display:grid;grid-template-columns:900px 1fr;gap:56px;align-items:center}
.riskside{display:grid;gap:30px}
#ruta-critica h2,#riesgos h2{font-size:72px}
'''


JS = '''<script id="ruta-graficos">
/* === Ampliación de las figuras de infraestructura física (tools/ruta_curimon_graficos.py) === */
document.querySelector('.deck-stage').addEventListener('click',e=>{
  const f=e.target.closest('img.fisica');
  if(f) f.classList.toggle('zoomed');
});
addEventListener('keydown',()=>document.querySelectorAll('img.fisica.zoomed').forEach(f=>f.classList.remove('zoomed')),true);
</script>
'''


def main():
    doc = HTML.read_text(encoding='utf-8')
    nuevas = construir()
    # Reemplazos en el recorrido principal
    for sid in ('arquitectura', 'plan'):
        doc, n = re.subn(rf'<section id="{sid}" .*?</section>', lambda m: nuevas[sid], doc, count=1, flags=re.S)
        assert n == 1, sid
    # Respaldo: elimina versiones previas y las inserta después de «continuidad»
    for sid in NUEVAS_RESPALDO:
        doc = re.sub(rf'<section id="{sid}" .*?</section>\n?', '', doc, flags=re.S)
    bloque = '\n'.join(nuevas[sid] for sid in NUEVAS_RESPALDO)
    doc, n = re.subn(r'(<section id="continuidad" .*?</section>)', lambda m: m.group(1) + '\n' + bloque, doc, count=1, flags=re.S)
    assert n == 1
    # Estilos
    doc = re.sub(r'\n/\* === Diagramas generados por tools/ruta_curimon_graficos\.py === \*/.*?(?=</style>)', '', doc, flags=re.S)
    doc = doc.replace('</style>', CSS + '</style>', 1)
    doc = re.sub(r'<script id="ruta-graficos">.*?</script>\n?', '', doc, flags=re.S)
    doc = doc.replace('</body>', JS + '</body>', 1)
    # Numeración de pies de página según el orden real
    ids = re.findall(r'<section id="([^"]+)"', doc)
    num = {sid: i for i, sid in enumerate(ids, 1)}

    def pie(m):
        sid = m.group(1)
        return re.sub(r'(<footer><span>.*?</span><span>)\d+(</span></footer>)', rf'\g<1>{num[sid]:02}\g<2>', m.group(0), count=1, flags=re.S)
    doc = re.sub(r'<section id="([^"]+)".*?</section>', pie, doc, flags=re.S)
    # Índice
    toc = [('problema', 'La escala del despacho'), ('arquitectura', 'Arquitectura híbrida'),
           ('demo', 'Qué ocurre cuando se pierde la señal'), ('plan', 'Hitos que condicionan la entrega'),
           ('precio', 'Precio, costo y margen'), ('curva', 'Curva S de costos y facturación'),
           ('caja', 'El atraso de H5 exige liquidez'), ('innovaciones', 'Cinco innovaciones y sus costos'),
           ('condiciones', 'Condiciones y monedas de la oferta'), ('sensibilidad', 'Sensibilidad de rentabilidad y caja'),
           ('hitos', 'Doce pagos contra aceptación'), ('proveedores', 'Proveedores, plazos y pagadores'),
           ('infra-nube', 'Infraestructura física, nube a flota'), ('ruta-critica', 'Ruta crítica hasta H12'),
           ('riesgos', 'Mapa de los 36 riesgos'), ('trazabilidad', 'Evidencia para revisión')]
    botones = ''.join(f'<button type="button" data-jump="{sid}"><b>{num[sid]:02}</b>{esc(txt)}</button>' for sid, txt in toc)
    doc, n = re.subn(r'<div class="toc">.*?</div>', f'<div class="toc">{botones}</div>', doc, count=1, flags=re.S)
    assert n == 1
    # Los textos editados se guardan por posición; al cambiar las láminas se invalida lo guardado.
    doc = re.sub(r"const savedKey='ruta-curimon-texto-v\d+';", "const savedKey='ruta-curimon-texto-v2';", doc)
    HTML.write_text(doc, encoding='utf-8')
    print(f'{HTML.name}: {len(ids)} láminas · {HTML.stat().st_size / 1e6:.1f} MB')


if __name__ == '__main__':
    main()
