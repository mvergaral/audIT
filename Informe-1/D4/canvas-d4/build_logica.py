# -*- coding: utf-8 -*-
"""Tres artboards de arquitectura lógica (subdoc. 4.1 — insumo para D3)."""
from build import (icon, box, path, elabel, page, emit, esc, G,
                   INK, MUTED, HAIR, FONT, MONO,
                   C_CLOUD, C_SITE, C_EDGE, C_FLEET, C_NET, W, H)

GRAY = "#41506A"

def band(o, y, h, title, comps, color):
    o.append(box(150, y, 826, h, title, color))
    for i, (g, t) in enumerate(comps):
        o.append(icon(352 + i * 152, y + 24, g, t, color, 28))

# ═════════════════════════════════════════════════ L1 · las ocho capas
def l1():
    o = []
    for x, t in [(44, "Seguridad"), (988, "Observabilidad")]:
        o.append(box(x, 92, 92, 578, "", GRAY, dashed=True))
        cx, cy = x + 46, 381
        o.append(f'<text x="{cx}" y="{cy}" font-family="{FONT}" font-size="12.5" '
                 f'font-weight="600" fill="{GRAY}" text-anchor="middle" '
                 f'transform="rotate(-90 {cx} {cy})">{esc(t)}</text>')

    band(o, 92, 88, "Presentación", [("person", "Portal web"), ("sim", "App móvil"),
         ("chip", "Terminal"), ("gauge", "Pantalla terreno")], C_CLOUD)
    band(o, 190, 88, "Borde y exposición", [("cloud", "CDN"), ("firewall", "WAF"),
         ("switch", "Balanceo"), ("key", "TLS 1.3")], C_CLOUD)
    band(o, 288, 88, "Puerta de enlace", [("key", "Autenticación"), ("gauge", "Cuotas"),
         ("box", "Versionado"), ("archive", "Catálogo")], C_CLOUD)
    o.append(box(150, 386, 826, 88, "Servicios de negocio", C_NET))
    o.append(f'<rect x="352" y="404" width="598" height="52" rx="6" fill="#FFFFFF" '
             f'stroke="{C_NET}" stroke-width="1.2" stroke-dasharray="5 4"/>')
    o.append(f'<text x="651" y="428" font-family="{MONO}" font-size="12" font-weight="600" '
             f'fill="{C_NET}" text-anchor="middle">[ POR DEFINIR — D3 ]</text>')
    o.append(f'<text x="651" y="445" font-family="{FONT}" font-size="9.5" fill="{MUTED}" '
             f'text-anchor="middle">módulos con límites de contexto explícitos</text>')
    band(o, 484, 88, "Integración y eventos", [("stream", "Bus"), ("queue", "Cola fallidos"),
         ("flow", "Reintento"), ("check", "Deduplicación")], C_EDGE)
    band(o, 582, 88, "Datos", [("db", "Transaccional"), ("chart", "Analítico"),
         ("archive", "Documental"), ("clock", "Series")], C_SITE)
    for y in (180, 278, 376, 474, 572):
        o.append(path([(300, y), (300, y + 10)]))
    o.append(f'<text x="563" y="700" font-family="{FONT}" font-size="10.5" fill="{MUTED}" '
             f'text-anchor="middle">Ninguna interfaz accede directamente a la base de datos</text>')
    return page("".join(o), "Arquitectura lógica — las ocho capas obligatorias", "4.1 · A",
                "RT-02.01 · RT-02.02 · numeral 2.1 Bases Técnicas Transversales, pág. 6/51")

# ═════════════════════════════════════════════════ L2 · integraciones
def l2():
    o = []
    o.append(box(392, 300, 340, 176, "Plataforma", C_CLOUD, "cloud"))
    o.append(icon(478, 352, "stream", "Integración", C_CLOUD, 38))
    o.append(icon(646, 352, "db", "Datos", C_CLOUD, 38))
    izq = [("rack", "Gestión 2013"), ("gauge", "Mantenimiento 2017"),
           ("box", "Contable"), ("bolt", "Combustible"), ("switch", "Peaje")]
    o.append(box(44, 92, 300, 612, "Sistemas internos", C_SITE, "server"))
    ys = []
    for i, (g, t) in enumerate(izq):
        y = 140 + i * 116
        o.append(icon(194, y, g, t, C_SITE, 38))
        o.append(path([(213, y + 19), (370, y + 19)], arrow="none"))
        ys.append(y + 19)
    o.append(path([(370, ys[0]), (370, ys[-1])], arrow="none"))
    o.append(path([(370, 388), (388, 388)], arrow="both"))
    der = [("gps", "3 plataformas GPS"), ("cloud", "Telemetría rFMS"), ("gauge", "Tacógrafos")]
    o.append(box(780, 92, 300, 380, "Terreno", C_FLEET, "truck"))
    yd = []
    for i, (g, t) in enumerate(der):
        y = 140 + i * 116
        o.append(icon(930, y, g, t, C_FLEET, 38))
        o.append(path([(911, y + 19), (754, y + 19)], arrow="none"))
        yd.append(y + 19)
    ext = [("person", "84 clientes"), ("firewall", "Autoridad aduanera")]
    o.append(box(780, 508, 300, 220, "Externos", C_NET, "cloud"))
    for i, (g, t) in enumerate(ext):
        y = 550 + i * 88
        o.append(icon(930, y, g, t, C_NET, 38))
        o.append(path([(911, y + 19), (754, y + 19)], arrow="none"))
        yd.append(y + 19)
    o.append(path([(754, yd[0]), (754, yd[-1])], arrow="none"))
    o.append(path([(754, 388), (736, 388)], arrow="both"))
    o.append(elabel(832, 294, "solo lectura", C_FLEET))
    o.append(f'<text x="562" y="512" font-family="{FONT}" font-size="10.5" fill="{MUTED}" '
             f'text-anchor="middle">Capa anticorrupción en cada integración</text>')
    return page("".join(o), "Mapa de integraciones", "4.1 · B",
                "RT-05.20 · RT-05.21 · RT-17.06 del Caso, pág. 34/49 · Cap. 5 del Caso, pág. 12/49")

# ═════════════════════════════════════════════════ L3 · capa → emplazamiento
def l3():
    o = []
    capas = ["Presentación", "Borde y exposición", "Puerta de enlace", "Servicios de negocio",
             "Integración y eventos", "Datos", "Seguridad", "Observabilidad"]
    cols = [("Nube", C_CLOUD, 470), ("San Bernardo", C_SITE, 640),
            ("Gabinete", C_EDGE, 810), ("Camión", C_FLEET, 980)]
    marca = [[1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 1, 1, 1],
             [1, 1, 0, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
    y0, rh = 208, 60
    for t, c, x in cols:
        o.append(f'<text x="{x}" y="{y0-16}" font-family="{FONT}" font-size="11" '
                 f'font-weight="600" fill="{c}" text-anchor="middle">{esc(t)}</text>')
    o.append(f'<line x1="150" y1="{y0-6}" x2="1060" y2="{y0-6}" stroke="{HAIR}" stroke-width="1"/>')
    for r, capa in enumerate(capas):
        y = y0 + r * rh
        o.append(f'<text x="160" y="{y+26}" font-family="{FONT}" font-size="11.5" '
                 f'fill="{INK}">{esc(capa)}</text>')
        o.append(f'<line x1="150" y1="{y+40}" x2="1060" y2="{y+40}" stroke="{HAIR}" '
                 f'stroke-width="0.6"/>')
        for (t, c, x), on in zip(cols, marca[r]):
            if on:
                o.append(f'<circle cx="{x}" cy="{y+21}" r="7.5" fill="{c}"/>')
            else:
                o.append(f'<circle cx="{x}" cy="{y+21}" r="7.5" fill="none" stroke="{HAIR}" '
                         f'stroke-width="1.2"/>')
    o.append(f'<text x="160" y="{y0+8*rh+34}" font-family="{FONT}" font-size="10.5" '
             f'fill="{MUTED}">Propuesta de D4 · se cierra con D3 en la sincronización del 04-09</text>')
    o.append(box(44, 90, 1035, 44, "", C_CLOUD))
    o.append(f'<text x="62" y="118" font-family="{FONT}" font-size="11.5" fill="{INK}">'
             f'El Artículo 16.2 califica como observación grave asignar un componente sin justificar.</text>')
    return page("".join(o), "De la capa lógica al emplazamiento físico", "4.1 → 4.2",
                "Artículo 16° y 16.2 Bases Administrativas · RT-03.10 · RT-06.01 del Caso, pág. 32/49")

def f41(fn):
    return lambda: fn().replace("Dupla 4 · Subdoc. 4.2 · TFEP-01/2026",
                                "Subdoc. 4.1 · insumo de D4 para D3 · TFEP-01/2026")

emit([("LogicaCapas", f41(l1)), ("LogicaIntegraciones", f41(l2)),
      ("LogicaEmplazamiento", f41(l3))])
