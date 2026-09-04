# -*- coding: utf-8 -*-
"""Genera los 4 artboards .dc.html + copias .svg para revision visual."""
import os, html
OUT = os.path.dirname(os.path.abspath(__file__))
W, H = 1123, 794

INK, MUTED, HAIR = "#1B2430", "#5B6675", "#C6D0DC"
C_CLOUD, C_SITE, C_EDGE, C_FLEET, C_NET = "#1B4FA8", "#96600B", "#0A6B45", "#5B3BB5", "#A32222"
FONT = "'IBM Plex Sans','Noto Sans',system-ui,sans-serif"
MONO = "'IBM Plex Mono','DejaVu Sans Mono',monospace"

def esc(s): return html.escape(str(s), quote=False)

# ───────────────────────────────────────────────────────── glifos 24×24
G = {
 "cloud":"M5 17.5a3.6 3.6 0 0 1 .7-7.1 5 5 0 0 1 9.5-1.6 3.9 3.9 0 0 1 3.6 3.9 3.4 3.4 0 0 1-2 3.1z",
 "server":"M4 5.5h16v5H4zM4 13.5h16v5H4zM7 8h.01M7 16h.01",
 "switch":"M4 8h16M4 16h16M8 5.5 4.5 8 8 10.5M16 13.5l3.5 2.5-3.5 2.5",
 "firewall":"M3.5 6h17v12h-17zM3.5 12h17M9 6v6M15 12v6M9 18v-6",
 "db":"M12 4.5c4 0 7 1 7 2.3v10.4c0 1.3-3 2.3-7 2.3s-7-1-7-2.3V6.8C5 5.5 8 4.5 12 4.5zM5 9.6c0 1.3 3 2.3 7 2.3s7-1 7-2.3M5 14.4c0 1.3 3 2.3 7 2.3s7-1 7-2.3",
 "chart":"M4 19h16M7 16V9M12 16V5M17 16v-4",
 "box":"M12 3.5 20 7v10l-8 3.5L4 17V7zM4 7l8 3.5L20 7M12 10.5V20",
 "key":"M14.5 6.5a4 4 0 1 1-3.4 6.1L4.5 19.2v-3h3v-3h3l.6-.6A4 4 0 0 1 14.5 6.5zM15.5 9.5h.01",
 "hub":"M12 4.5v5M12 14.5v5M4.5 12h5M14.5 12h5M12 9.5a2.5 2.5 0 1 0 0 5 2.5 2.5 0 0 0 0-5",
 "stream":"M4 7h13M4 12h16M4 17h10M20 7l-3-2.5M20 7l-3 2.5",
 "k8s":"M12 3.5 19 7v10l-7 3.5L5 17V7zM12 9a3 3 0 1 0 0 6 3 3 0 0 0 0-6",
 "bolt":"M13.5 3.5 6 13h5l-1.5 7.5L18 11h-5z",
 "gen":"M4.5 8.5h15v9h-15zM8 8.5V6h8v2.5M8 12h8M12 12v5.5",
 "snow":"M12 3.5v17M4.5 7.8l15 8.4M19.5 7.8l-15 8.4",
 "flame":"M12 3.5c3 4 5 5.5 5 9a5 5 0 0 1-10 0c0-1.6.8-2.8 2-4 .3 1.2 1 1.8 1.8 2C11 8.5 11 5.6 12 3.5z",
 "archive":"M4 5.5h16v4H4zM5.5 9.5v9h13v-9M10 13h4",
 "rack":"M6 3.5h12v17H6zM8.5 7h7M8.5 11h7M8.5 15h4",
 "truck":"M2.5 6.5h11v9h-11zM13.5 9.5h4l3 3.5v2.5h-7zM6.5 15.5a1.8 1.8 0 1 0 0 3.6 1.8 1.8 0 0 0 0-3.6M17 15.5a1.8 1.8 0 1 0 0 3.6 1.8 1.8 0 0 0 0-3.6",
 "ant":"M12 8.5v11M7.5 4.5a7 7 0 0 0 0 8M16.5 4.5a7 7 0 0 1 0 8M9.8 6.5a3.4 3.4 0 0 0 0 4M14.2 6.5a3.4 3.4 0 0 1 0 4M8.5 19.5h7",
 "sat":"M6 12 12 6M4 14l6 6M14 4l6 6M9.5 8.5 15.5 14.5M13 17c2.5 0 4.5-2 4.5-4.5",
 "person":"M12 4.5a3.2 3.2 0 1 0 0 6.4 3.2 3.2 0 0 0 0-6.4M5.5 20c0-3.6 2.9-6 6.5-6s6.5 2.4 6.5 6",
 "chip":"M7.5 7.5h9v9h-9zM10 3.5v4M14 3.5v4M10 16.5v4M14 16.5v4M3.5 10h4M3.5 14h4M16.5 10h4M16.5 14h4",
 "gps":"M12 3.5c-3.3 0-6 2.6-6 5.9 0 4.4 6 11.1 6 11.1s6-6.7 6-11.1c0-3.3-2.7-5.9-6-5.9zM12 7.2a2.4 2.4 0 1 0 0 4.8 2.4 2.4 0 0 0 0-4.8",
 "sim":"M6 3.5h8l4 4v13H6zM9.5 11h5v6h-5z",
 "nfc":"M8 5.5a9 9 0 0 1 0 13M11.5 8a5 5 0 0 1 0 8M15 10.5a1.8 1.8 0 0 1 0 3",
 "gauge":"M4.5 17a7.5 7.5 0 1 1 15 0M12 17l4-5M12 17h.01",
 "bus":"M4 12h4M16 12h4M8 8.5h8v7H8zM11 5.5v3M13 15.5v3",
 "ecu":"M4.5 7h15v10h-15zM8 11h8M8 14h5M4.5 12H2M21.5 12h-2",
 "flow":"M12 3.5 21 12l-9 8.5L3 12z",
 "clock":"M12 4a8 8 0 1 0 0 16 8 8 0 0 0 0-16M12 7.5V12l3 2",
 "check":"M5 12.5l4.5 4.5L19 7.5",
 "queue":"M4 6.5h16M4 12h16M4 17.5h16M7 4v5M12 9.5v5M17 15v5",
}

def icon(x, y, key, label, color, s=34, sub=None):
    """Cuadrado redondeado con glifo blanco + nombre debajo, centrado en x."""
    o = [f'<rect x="{x-s/2:.1f}" y="{y}" width="{s}" height="{s}" rx="6" fill="{color}"/>']
    k = s / 24 * 0.74
    o.append(f'<g transform="translate({x-s/2+s*0.13:.1f},{y+s*0.13:.1f}) scale({k:.3f})" '
             f'fill="none" stroke="#fff" stroke-width="1.7" stroke-linecap="round" '
             f'stroke-linejoin="round"><path d="{G[key]}"/></g>')
    o.append(f'<text x="{x}" y="{y+s+13}" font-family="{FONT}" font-size="9.5" fill="{INK}" '
             f'text-anchor="middle">{esc(label)}</text>')
    if sub:
        o.append(f'<text x="{x}" y="{y+s+24}" font-family="{FONT}" font-size="8.5" fill="{MUTED}" '
                 f'text-anchor="middle">{esc(sub)}</text>')
    return "".join(o)

def box(x, y, w, h, title, color, gl=None, dashed=False, sub=None):
    """Contenedor blanco con borde de color, icono + nombre arriba a la izquierda."""
    d = ' stroke-dasharray="4 3"' if dashed else ""
    o = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="4" fill="#FFFFFF" '
         f'stroke="{color}" stroke-width="1"{d}/>']
    tx = x + 10
    if gl:
        o.append(f'<g transform="translate({x+8},{y+7}) scale(0.62)" fill="none" stroke="{color}" '
                 f'stroke-width="2" stroke-linecap="round" stroke-linejoin="round">'
                 f'<path d="{G[gl]}"/></g>')
        tx = x + 26
    fs = 10 if dashed else 11
    o.append(f'<text x="{tx}" y="{y+17}" font-family="{FONT}" font-size="{fs}" '
             f'font-weight="600" fill="{color}">{esc(title)}</text>')
    if sub:
        o.append(f'<text x="{x+w-10}" y="{y+17}" font-family="{FONT}" font-size="9.5" '
                 f'fill="{MUTED}" text-anchor="end">{esc(sub)}</text>')
    return "".join(o)

def path(pts, dashed=False, arrow="end", color=None):
    c = color or MUTED
    d = "M" + " L".join(f"{p[0]},{p[1]}" for p in pts)
    da = ' stroke-dasharray="5 4"' if dashed else ""
    m = ""
    if arrow in ("end", "both"): m += f' marker-end="url(#a{c[1:]})"'
    if arrow in ("start", "both"): m += f' marker-start="url(#b{c[1:]})"'
    return f'<path d="{d}" fill="none" stroke="{c}" stroke-width="1"{da}{m}/>'

def elabel(x, y, t, color=None):
    w = len(t) * 4.95 + 18
    return (f'<rect x="{x-w/2:.1f}" y="{y-7}" width="{w:.1f}" height="14" fill="#FFFFFF"/>'
            f'<text x="{x}" y="{y+3}" font-family="{FONT}" font-size="9" '
            f'fill="{color or MUTED}" text-anchor="middle">{esc(t)}</text>')

def page(inner, title, num, foot):
    mk = "".join(
        f'<marker id="a{c[1:]}" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5.5" '
        f'markerHeight="5.5" orient="auto-start-reverse"><path d="M0,1.5 L8.5,5 L0,8.5 z" fill="{c}"/></marker>'
        f'<marker id="b{c[1:]}" viewBox="0 0 10 10" refX="2" refY="5" markerWidth="5.5" '
        f'markerHeight="5.5" orient="auto"><path d="M8.5,1.5 L0,5 L8.5,8.5 z" fill="{c}"/></marker>'
        for c in {MUTED, C_NET, C_CLOUD})
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
            f'viewBox="0 0 {W} {H}"><defs>{mk}</defs>'
            f'<rect width="{W}" height="{H}" fill="#FFFFFF"/>'
            f'<text x="44" y="46" font-family="{FONT}" font-size="17" font-weight="600" '
            f'fill="{INK}">{esc(title)}</text>'
            f'<text x="{W-44}" y="46" font-family="{FONT}" font-size="11" fill="{MUTED}" '
            f'text-anchor="end">Diagrama {num}</text>'
            f'<line x1="44" y1="60" x2="{W-44}" y2="60" stroke="{HAIR}" stroke-width="1"/>'
            + inner +
            f'<line x1="44" y1="{H-42}" x2="{W-44}" y2="{H-42}" stroke="{HAIR}" stroke-width="1"/>'
            f'<text x="44" y="{H-26}" font-family="{MONO}" font-size="9" fill="{MUTED}">{esc(foot)}</text>'
            f'<text x="{W-44}" y="{H-26}" font-family="{FONT}" font-size="9" fill="{MUTED}" '
            f'text-anchor="end">Dupla 4 · Subdoc. 4.2 · TFEP-01/2026</text></svg>')

# ══════════════════════════════════════════════════════════ 1 · general
def d1():
    o = []
    o.append(icon(110, 160, "person", "Torre 24×7", MUTED, 30))
    # nube
    o.append(box(230, 92, 560, 176, "Azure Chile Central", C_CLOUD, "cloud", sub="3 zonas"))
    o.append(box(246, 112, 168, 142, "Ingesta", C_CLOUD, dashed=True))
    o.append(icon(288, 150, "hub", "IoT Hub", C_CLOUD))
    o.append(icon(372, 150, "stream", "Event Hubs", C_CLOUD))
    o.append(box(426, 112, 132, 142, "Cómputo", C_CLOUD, dashed=True))
    o.append(icon(492, 150, "k8s", "AKS", C_CLOUD))
    o.append(box(570, 112, 204, 142, "Datos", C_CLOUD, dashed=True))
    o.append(icon(622, 148, "db", "PostgreSQL", C_CLOUD))
    o.append(icon(722, 148, "chart", "Data Explorer", C_CLOUD))
    o.append(icon(622, 204, "box", "Blob", C_CLOUD))
    o.append(icon(722, 204, "key", "Key Vault", C_CLOUD))
    # DR
    o.append(box(848, 92, 190, 176, "Azure — 2.ª región", C_CLOUD, "cloud"))
    o.append(icon(943, 160, "db", "Réplica", C_CLOUD))
    o.append(path([(790, 180), (846, 180)], dashed=True, arrow="both"))
    o.append(elabel(818, 173, "DR"))
    o.append(path([(127, 177), (228, 177)]))
    # San Bernardo
    o.append(box(44, 330, 546, 176, "San Bernardo", C_SITE, "rack", sub="26 m²"))
    o.append(box(60, 352, 300, 140, "Sala técnica", C_SITE, dashed=True))
    o.append(icon(105, 390, "server", "Servidor ×2", C_SITE))
    o.append(icon(180, 390, "switch", "Switch ×2", C_SITE))
    o.append(icon(255, 390, "firewall", "Firewall ×2", C_SITE))
    o.append(icon(325, 390, "archive", "Custodia", C_SITE))
    o.append(box(374, 352, 200, 140, "Planta", C_SITE, dashed=True))
    o.append(icon(422, 386, "bolt", "UPS", C_SITE, 30))
    o.append(icon(524, 386, "gen", "Generador", C_SITE, 30))
    o.append(icon(422, 442, "snow", "Clima N+1", C_SITE, 30))
    o.append(icon(524, 442, "flame", "Extinción", C_SITE, 30))
    o.append(path([(300, 268), (300, 300), (250, 300), (250, 328)], arrow="both"))
    o.append(path([(430, 268), (430, 300), (470, 300), (470, 328)], dashed=True, arrow="both"))
    o.append(elabel(275, 300, "ExpressRoute"))
    o.append(elabel(450, 300, "VPN"))
    # terminales
    o.append(box(636, 330, 402, 176, "Terminales regionales", C_EDGE, "rack", sub="×4"))
    for i, t in enumerate(["Antofagasta", "Talca", "Los Ángeles", "Puerto Montt"]):
        x = 654 + i * 96
        o.append(box(x, 356, 84, 132, "", C_EDGE))
        o.append(icon(x + 42, 386, "rack", t, C_EDGE, 30))
    o.append(path([(840, 268), (840, 328)], arrow="both"))
    o.append(elabel(840, 300, "Enlace + respaldo"))
    # flota
    o.append(box(44, 556, 994, 152, "Flota", C_FLEET, "truck", sub="374 camiones"))
    for i, (t, sb) in enumerate([("Propios", "148"), ("Terceros", "192"), ("Sin equipo", "34")]):
        o.append(icon(140 + i * 120, 600, "truck", t, C_FLEET, 38, sb))
    o.append(box(470, 580, 550, 108, "Dispositivo a bordo", C_FLEET, dashed=True))
    for i, (g, t) in enumerate([("chip", "Unidad"), ("sim", "Celular"),
                                ("sat", "SBD"), ("nfc", "ID conductor")]):
        o.append(icon(560 + i * 130, 614, g, t, C_FLEET, 30))
    o.append(path([(745, 578), (745, 528), (612, 528), (612, 272)]))
    o.append(elabel(612, 300, "Celular / satelital", C_FLEET))
    o.append(path([(838, 506), (838, 554)], dashed=True))
    o.append(elabel(838, 532, "Instalación"))
    return page("".join(o), "Arquitectura física general", 1,
                "RT-03.01 · RT-03.02 · RT-03.17 · RT-06.01 · RT-07.02 · RT-07.04 · RT-21.06 · num. 6.1 transversal")

# ══════════════════════════════════════════════════════════ 2 · camion
def d2():
    o = []
    o.append(box(44, 92, 560, 362, "Cabina del camión", C_FLEET, "truck", sub="×374"))
    o.append(box(62, 118, 300, 296, "Unidad telemática", C_FLEET, dashed=True))
    o.append(icon(212, 152, "gps", "GNSS", C_FLEET))
    o.append(icon(212, 250, "archive", "Buffer 8 GB", C_FLEET))
    o.append(icon(212, 348, "chip", "Procesador", C_FLEET))
    o.append(icon(500, 152, "sim", "Módem 4G", C_FLEET))
    o.append(icon(500, 250, "sat", "Módulo SBD", C_FLEET))
    o.append(icon(500, 348, "nfc", "Lector NFC", C_FLEET))
    for y in (169, 267, 365):
        o.append(path([(364, y), (481, y)]))
    o.append(f'<text x="324" y="438" font-family="{FONT}" font-size="10.5" fill="{MUTED}" '
             f'text-anchor="middle">Sin interacción en marcha</text>')
    o.append(box(44, 486, 560, 150, "Vehículo", C_SITE, "ecu"))
    o.append(icon(160, 524, "gauge", "Tacógrafo", C_SITE))
    o.append(icon(324, 524, "bus", "Bus CAN", C_SITE))
    o.append(icon(488, 524, "ecu", "ECU", C_SITE))
    o.append(path([(160, 520), (160, 418)], arrow="end"))
    o.append(elabel(160, 468, "DDD", C_SITE))
    o.append(box(680, 92, 358, 544, "Fuera del vehículo", C_CLOUD, "cloud"))
    o.append(icon(800, 152, "ant", "Red celular", C_NET, 38))
    o.append(icon(800, 300, "sat", "Iridium", C_NET, 38))
    o.append(icon(800, 452, "cloud", "Nube del fabricante", C_NET, 38))
    o.append(f'<text x="800" y="518" font-family="{FONT}" font-size="9" fill="{MUTED}" '
             f'text-anchor="middle">61 tractocamiones</text>')
    o.append(path([(519, 169), (777, 169)]))
    o.append(elabel(640, 169, "LTE"))
    o.append(path([(519, 267), (640, 267), (640, 319), (777, 319)]))
    o.append(elabel(640, 240, "SBD"))
    o.append(path([(507, 541), (640, 541), (640, 471), (777, 471)]))
    o.append(elabel(640, 508, "rFMS"))
    return page("".join(o), "El camión como componente on-premise distribuido", 2,
                "RT-03.10 · RT-03.18 · RT-06.01 · RT-12.11 · RT-17.06 · restricciones 1, 5 y 6")

# ══════════════════════════════════════════════════════════ 3 · dos ejes
def d3():
    o = []
    o.append(box(330, 84, 424, 150, "No es un par de respaldo", C_NET, "firewall"))
    o.append(icon(430, 122, "cloud", "Quilicura", C_NET, 34))
    o.append(icon(654, 122, "rack", "San Bernardo", C_NET, 34))
    o.append(path([(450, 139), (634, 139)], arrow="none", color=C_NET))
    o.append(f'<line x1="532" y1="128" x2="552" y2="150" stroke="{C_NET}" stroke-width="1.8"/>')
    o.append(f'<line x1="552" y1="128" x2="532" y2="150" stroke="{C_NET}" stroke-width="1.8"/>')
    o.append(elabel(542, 200, "≈ 20 km", C_NET))
    o.append(box(44, 268, 994, 190, "Eje 1 — Recuperación ante desastres", C_CLOUD, "cloud"))
    o.append(icon(360, 322, "cloud", "Azure Chile Central", C_CLOUD, 44))
    o.append(icon(722, 322, "cloud", "Azure 2.ª región", C_CLOUD, 44))
    o.append(path([(400, 344), (690, 344)], arrow="both", color=C_CLOUD))
    o.append(elabel(541, 344, "replicación continua", C_CLOUD))
    o.append(f'<text x="541" y="418" font-family="{FONT}" font-size="11" fill="{INK}" '
             f'text-anchor="middle">RTO 4 h · RPO 15 min</text>')
    o.append(box(44, 494, 994, 200, "Eje 2 — Continuidad operacional en el borde", C_SITE, "rack"))
    xs = [180, 440, 700, 940]
    lb = [("cloud", "Azure", C_CLOUD), ("rack", "San Bernardo", C_SITE),
          ("rack", "Terminal", C_EDGE), ("truck", "Camión", C_FLEET)]
    for x, (g, t, c) in zip(xs, lb):
        o.append(icon(x, 556, g, t, c, 44))
    for a, b in zip(xs, xs[1:]):
        o.append(path([(a + 40, 578), (b - 40, 578)], arrow="both", color=MUTED))
    o.append(elabel(820, 578, "72 h autónomas", C_FLEET))
    o.append(elabel(310, 578, "ExpressRoute"))
    o.append(elabel(570, 578, "enlace + respaldo"))
    o.append(f'<text x="541" y="656" font-family="{FONT}" font-size="11" fill="{INK}" '
             f'text-anchor="middle">Opera con el enlace caído</text>')
    return page("".join(o), "Por qué el sitio de borde no es el secundario de la nube", 3,
                "RT-07.01 a RT-07.08 · RT-03.10 · RT-21.06 · Artículo 16° Bases Administrativas")

# ══════════════════════════════════════════════════════════ 4 · flujo
def d4():
    o = []
    def node(x, y, w, h, t, c, gl=None):
        r = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="#FFFFFF" '
             f'stroke="{c}" stroke-width="1.2"/>']
        ty = y + h / 2 + 4
        if gl:
            r.append(f'<g transform="translate({x+12},{y+h/2-9}) scale(0.75)" fill="none" '
                     f'stroke="{c}" stroke-width="1.8" stroke-linecap="round" '
                     f'stroke-linejoin="round"><path d="{G[gl]}"/></g>')
            r.append(f'<text x="{x+38}" y="{ty}" font-family="{FONT}" font-size="11" '
                     f'fill="{INK}">{esc(t)}</text>')
        else:
            r.append(f'<text x="{x+w/2}" y="{ty}" font-family="{FONT}" font-size="11" '
                     f'fill="{INK}" text-anchor="middle">{esc(t)}</text>')
        return "".join(r)
    o.append(node(60, 108, 230, 54, "Zona de sombra", C_FLEET, "ant"))
    o.append(node(60, 206, 230, 54, "Registro en buffer", C_EDGE, "archive"))
    o.append(path([(175, 162), (175, 202)]))
    cx, cy = 175, 348
    o.append(f'<path d="M{cx},{cy-46} L{cx+110},{cy} L{cx},{cy+46} L{cx-110},{cy} z" '
             f'fill="#FFFFFF" stroke="{C_CLOUD}" stroke-width="1.2"/>')
    o.append(f'<text x="{cx}" y="{cy+4}" font-family="{FONT}" font-size="11" fill="{INK}" '
             f'text-anchor="middle">¿Evento crítico?</text>')
    o.append(path([(175, 260), (175, 298)]))
    o.append(node(430, 321, 210, 54, "Envío por SBD", C_NET, "sat"))
    o.append(path([(285, 348), (426, 348)], arrow="end", color=C_NET))
    o.append(elabel(352, 330, "Sí", C_NET))
    o.append(node(60, 428, 230, 54, "Cola local", C_EDGE, "queue"))
    o.append(path([(175, 394), (175, 424)]))
    o.append(elabel(206, 410, "No"))
    o.append(node(60, 526, 230, 54, "Recupera cobertura", C_FLEET, "sim"))
    o.append(path([(175, 482), (175, 522)]))
    o.append(node(430, 526, 210, 54, "Sincronización diferida", C_CLOUD, "stream"))
    o.append(path([(294, 553), (426, 553)]))
    o.append(node(430, 624, 210, 54, "Reconciliación", C_CLOUD, "check"))
    o.append(path([(535, 580), (535, 620)]))
    o.append(elabel(535, 602, "≤ 20 min", C_CLOUD))
    o.append(node(790, 624, 220, 54, "Registro consolidado", C_EDGE, "db"))
    o.append(path([(640, 651), (786, 651)]))
    o.append(box(756, 118, 282, 286, "Sólo estos eventos", C_NET, "sat", dashed=True))
    o.append(icon(836, 172, "flame", "Pánico", C_NET, 32))
    o.append(icon(958, 172, "gps", "Geocerca", C_NET, 32))
    o.append(icon(836, 292, "ant", "Frontera", C_NET, 32))
    o.append(icon(958, 292, "clock", "Jornada", C_NET, 32))
    o.append(path([(640, 348), (752, 348)], color=C_NET))
    return page("".join(o), "Flujo de un evento de jornada sin cobertura", 4,
                "RT-03.10 · RT-03.12 · RT-09.01 · Cap. 14.2 volumetría del caso")

DC = """<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;600&family=IBM+Plex+Mono:wght@400&display=swap">
  <style>
    body { margin: 0; background: #FFFFFF; }
    a { color: #1B4FA8; } a:hover { color: #12356F; }
  </style>
</helmet>
<div style="width: 1123px; height: 794px; background: #FFFFFF;">
%s
</div>
</x-dc>
</body>
</html>
"""

ART = [("Main", d1), ("Camion", d2), ("DosEjes", d3), ("Flujo", d4)]

def emit(pairs):
  for name, fn in pairs:
    svg = fn()
    open(os.path.join(OUT, f"{name}.dc.html"), "w", encoding="utf-8").write(DC % svg)
    open(os.path.join(OUT, f"_{name}.svg"), "w", encoding="utf-8").write(svg)
    import re
    labels = [t for t in re.findall(r">([^<>]+)</text>", svg) if t.strip()]
    print(f"{name:9s} etiquetas={len(labels):3d}  caracteres={sum(len(t) for t in labels):4d}")

if __name__ == "__main__":
    emit(ART)
