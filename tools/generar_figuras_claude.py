#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generador fiel de diagramas audIT basado 100% en el motor original de Claude
(Informe-1/D4/canvas-d4/build.py y build_logica.py).

Preserva:
- Los 35 glifos vectoriales exactos (G)
- El estilo de cajitas redondeadas con glifos blancos (icon)
- Las cajas de contorno con glifo en la esquina (box)
- Los conectores y etiquetas (path, elabel)
- La paleta cromática oficial (C_CLOUD, C_SITE, C_EDGE, C_FLEET, C_NET)

Ajusta:
- Tipografía mínima a >= 15.0 px (Art. 40.4 de las bases)
- Coordenadas espaciadas para garantizar 0 choques y máxima legibilidad
"""

import os, html, sys
import pymupdf

# Importar constantes y glifos del motor original de Claude
sys.path.append(os.path.abspath("Informe-1/D4/canvas-d4"))
import build

W, H = 1123, 794
INK, MUTED, HAIR = build.INK, build.MUTED, build.HAIR
C_CLOUD, C_SITE, C_EDGE, C_FLEET, C_NET = (
    build.C_CLOUD, build.C_SITE, build.C_EDGE, build.C_FLEET, build.C_NET
)
GRAY = "#41506A"
FONT = build.FONT
MONO = build.MONO
G = build.G

def esc(s):
    return html.escape(str(s), quote=False)

def icon(x, y, key, label, color, s=34, sub=None):
    """Caja original de Claude con glifo blanco + textos >= 15 px."""
    o = [f'<rect x="{x-s/2:.1f}" y="{y}" width="{s}" height="{s}" rx="6" fill="{color}"/>']
    k = s / 24 * 0.74
    o.append(f'<g transform="translate({x-s/2+s*0.13:.1f},{y+s*0.13:.1f}) scale({k:.3f})" '
             f'fill="none" stroke="#fff" stroke-width="1.7" stroke-linecap="round" '
             f'stroke-linejoin="round"><path d="{G[key]}"/></g>')
    o.append(f'<text x="{x}" y="{y+s+16}" font-family="{FONT}" font-size="15" font-weight="600" fill="{INK}" '
             f'text-anchor="middle">{esc(label)}</text>')
    if sub:
        o.append(f'<text x="{x}" y="{y+s+32}" font-family="{FONT}" font-size="15" fill="{MUTED}" '
                 f'text-anchor="middle">{esc(sub)}</text>')
    return "".join(o)

def box(x, y, w, h, title, color, gl=None, dashed=False, sub=None):
    """Contenedor original de Claude con textos >= 15 px."""
    d = ' stroke-dasharray="4 3"' if dashed else ""
    o = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="4" fill="#FFFFFF" '
         f'stroke="{color}" stroke-width="1.2"{d}/>']
    tx = x + 10
    if gl:
        o.append(f'<g transform="translate({x+8},{y+6}) scale(0.68)" fill="none" stroke="{color}" '
                 f'stroke-width="2" stroke-linecap="round" stroke-linejoin="round">'
                 f'<path d="{G[gl]}"/></g>')
        tx = x + 28
    fs = 15 if dashed else 16
    o.append(f'<text x="{tx}" y="{y+19}" font-family="{FONT}" font-size="{fs}" '
             f'font-weight="600" fill="{color}">{esc(title)}</text>')
    if sub:
        o.append(f'<text x="{x+w-10}" y="{y+19}" font-family="{FONT}" font-size="15" '
                 f'fill="{MUTED}" text-anchor="end">{esc(sub)}</text>')
    return "".join(o)

def path(pts, dashed=False, arrow="end", color=None):
    c = color or MUTED
    d = "M" + " L".join(f"{p[0]},{p[1]}" for p in pts)
    da = ' stroke-dasharray="5 4"' if dashed else ""
    m = ""
    if arrow in ("end", "both"): m += f' marker-end="url(#a{c[1:]})"'
    if arrow in ("start", "both"): m += f' marker-start="url(#b{c[1:]})"'
    return f'<path d="{d}" fill="none" stroke="{c}" stroke-width="1.2"{da}{m}/>'

def elabel(x, y, t, color=None):
    w = len(t) * 8.5 + 20
    return (f'<rect x="{x-w/2:.1f}" y="{y-10}" width="{w:.1f}" height="20" rx="3" fill="#FFFFFF"/>'
            f'<text x="{x}" y="{y+4}" font-family="{FONT}" font-size="15" font-weight="600" '
            f'fill="{color or MUTED}" text-anchor="middle">{esc(t)}</text>')

def page(inner, title, num, foot):
    mk = "".join(
        f'<marker id="a{c[1:]}" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5.5" '
        f'markerHeight="5.5" orient="auto-start-reverse"><path d="M0,1.5 L8.5,5 L0,8.5 z" fill="{c}"/></marker>'
        f'<marker id="b{c[1:]}" viewBox="0 0 10 10" refX="2" refY="5" markerWidth="5.5" '
        f'markerHeight="5.5" orient="auto"><path d="M8.5,1.5 L0,5 L8.5,8.5 z" fill="{c}"/></marker>'
        for c in {MUTED, C_NET, C_CLOUD, C_SITE, C_EDGE, C_FLEET})
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
            f'viewBox="0 0 {W} {H}"><defs>{mk}</defs>'
            f'<rect width="{W}" height="{H}" fill="#FFFFFF"/>'
            f'<text x="44" y="46" font-family="{FONT}" font-size="20" font-weight="600" '
            f'fill="{INK}">{esc(title)}</text>'
            f'<text x="{W-44}" y="46" font-family="{FONT}" font-size="15" fill="{MUTED}" '
            f'text-anchor="end">Diagrama {num}</text>'
            f'<line x1="44" y1="58" x2="{W-44}" y2="58" stroke="{HAIR}" stroke-width="1.2"/>'
            + inner +
            f'<line x1="44" y1="{H-42}" x2="{W-44}" y2="{H-42}" stroke="{HAIR}" stroke-width="1.2"/>'
            f'<text x="44" y="{H-24}" font-family="{MONO}" font-size="15" fill="{MUTED}">{esc(foot)}</text>'
            f'<text x="{W-44}" y="{H-24}" font-family="{FONT}" font-size="15" fill="{MUTED}" '
            f'text-anchor="end">audIT · TFEP-01/2026</text>'
            + '</svg>')

# =============================================================================
# 1. Main: Arquitectura Física General (Adaptada a 15 px)
# =============================================================================
def build_main():
    o = []
    # Torre 24x7
    o.append(icon(105, 140, "person", "Torre 24×7", MUTED, 34))
    
    # Nube Azure Chile Central
    o.append(box(210, 80, 600, 195, "Azure Chile Central", C_CLOUD, "cloud", sub="3 zonas"))
    o.append(box(224, 108, 176, 154, "Ingesta", C_CLOUD, dashed=True))
    o.append(icon(268, 142, "hub", "IoT Hub", C_CLOUD, 32))
    o.append(icon(356, 142, "stream", "Event Hubs", C_CLOUD, 32))
    
    o.append(box(412, 108, 136, 154, "Cómputo", C_CLOUD, dashed=True))
    o.append(icon(480, 142, "k8s", "AKS", C_CLOUD, 32))
    
    o.append(box(560, 108, 238, 154, "Datos", C_CLOUD, dashed=True))
    o.append(icon(618, 138, "db", "PostgreSQL", C_CLOUD, 30))
    o.append(icon(738, 138, "chart", "Data Explorer", C_CLOUD, 30))
    o.append(icon(618, 196, "box", "Blob", C_CLOUD, 30))
    o.append(icon(738, 196, "key", "Key Vault", C_CLOUD, 30))

    # Azure Brazil South (DR)
    o.append(box(844, 80, 235, 195, "Azure — 2.ª región", C_CLOUD, "cloud"))
    o.append(icon(961, 145, "db", "Réplica", C_CLOUD, 34))
    o.append(path([(810, 175), (844, 175)], dashed=True, arrow="both"))
    o.append(elabel(827, 175, "DR"))
    o.append(path([(122, 175), (210, 175)]))

    # San Bernardo
    o.append(box(44, 335, 556, 185, "San Bernardo", C_SITE, "rack", sub="26 m²"))
    o.append(box(58, 362, 312, 145, "Sala técnica", C_SITE, dashed=True))
    o.append(icon(96, 396, "server", "Servidores", C_SITE, 32))
    o.append(icon(170, 396, "switch", "Switches", C_SITE, 32))
    o.append(icon(244, 396, "firewall", "Firewalls", C_SITE, 32))
    o.append(icon(324, 396, "archive", "Custodia", C_SITE, 32))
    
    o.append(box(382, 362, 206, 145, "Planta", C_SITE, dashed=True))
    o.append(icon(428, 390, "bolt", "UPS", C_SITE, 28))
    o.append(icon(536, 390, "gen", "Generador", C_SITE, 28))
    o.append(icon(428, 446, "snow", "Clima N+1", C_SITE, 28))
    o.append(icon(536, 446, "flame", "Extinción", C_SITE, 28))
    
    # Enlaces San Bernardo -> Nube
    o.append(path([(290, 275), (290, 305), (250, 305), (250, 335)], arrow="both"))
    o.append(path([(440, 275), (440, 305), (475, 305), (475, 335)], dashed=True, arrow="both"))
    o.append(elabel(270, 305, "ExpressRoute"))
    o.append(elabel(458, 305, "VPN"))

    # Terminales regionales
    o.append(box(632, 335, 447, 185, "Terminales regionales", C_EDGE, "rack", sub="×4"))
    terms = ["Antofagasta", "Talca", "Los Ángeles", "Puerto Montt"]
    for i, t in enumerate(terms):
        x = 646 + i * 105
        o.append(box(x, 362, 98, 145, "", C_EDGE))
        o.append(icon(x + 49, 396, "rack", t, C_EDGE, 30))
    
    o.append(path([(855, 275), (855, 335)], arrow="both"))
    o.append(elabel(855, 305, "Enlace + respaldo"))

    # Flota
    o.append(box(44, 545, 1035, 185, "Flota", C_FLEET, "truck", sub="374 camiones"))
    for i, (t, sb) in enumerate([("Propios", "148"), ("Terceros", "226"), ("Sin GPS", "34 de 374")]):
        o.append(icon(120 + i * 115, 595, "truck", t, C_FLEET, 36, sb))
    
    # Dispositivo a bordo
    o.append(box(475, 570, 590, 145, "Dispositivo a bordo", C_FLEET, dashed=True))
    devs = [("chip", "Unidad"), ("sim", "Celular"), ("sat", "SBD"), ("nfc", "ID conductor")]
    for i, (g, t) in enumerate(devs):
        o.append(icon(545 + i * 140, 605, g, t, C_FLEET, 32))
    
    # Enlaces flota
    o.append(path([(755, 570), (755, 528), (612, 528), (612, 275)]))
    o.append(elabel(612, 305, "Celular / satelital", C_FLEET))
    o.append(path([(850, 520), (850, 545)], dashed=True))
    o.append(elabel(850, 532, "Instalación"))

    return page("".join(o), "Arquitectura física general", 1,
                "RT-03.01 · RT-03.02 · RT-03.17 · RT-06.01 · RT-07.02 · RT-21.06")

# =============================================================================
# 2. LogicaCapas: Las 8 Capas Obligatorias (Adaptada a 15 px)
# =============================================================================
def build_logica_capas():
    o = []
    
    # Capas transversales verticales
    for x, t in [(44, "Seguridad"), (979, "Observabilidad")]:
        o.append(box(x, 80, 100, 596, "", GRAY, dashed=True))
        cx, cy = x + 50, 378
        o.append(f'<text x="{cx}" y="{cy}" font-family="{FONT}" font-size="16" '
                 f'font-weight="600" fill="{GRAY}" text-anchor="middle" '
                 f'transform="rotate(-90 {cx} {cy})">{esc(t)}</text>')

    def band(y, h, title, comps, color):
        o.append(box(160, y, 803, h, title, color))
        for i, comp in enumerate(comps):
            g, t = comp[0], comp[1]
            sub = comp[2] if len(comp) > 2 else None
            o.append(icon(260 + i * 200, y + 26, g, t, color, 30, sub))

    # Capa 1: Presentación
    band(80, 88, "1. Presentación", [
        ("person", "Portal web", "Clientes y transp."),
        ("sim", "App móvil", "Conductor Flutter"),
        ("chip", "Terminal", "Torre 24×7"),
        ("gauge", "Terreno", "Pantalla patio")
    ], C_CLOUD)

    # Capa 2: Borde y exposición
    band(180, 88, "2. Borde y exposición", [
        ("cloud", "CDN", "Front Door"),
        ("firewall", "WAF", "Anti-DDoS L7"),
        ("switch", "Balanceo", "Carga multizona"),
        ("key", "TLS 1.3", "Cifrado estricto")
    ], C_CLOUD)

    # Capa 3: Puerta de enlace
    band(280, 88, "3. Puerta de enlace", [
        ("key", "Autenticación", "OAuth2 / OIDC"),
        ("gauge", "Cuotas", "Rate limiting"),
        ("box", "Versionado", "Semántico /v1"),
        ("archive", "Catálogo", "OpenAPI 3.1")
    ], C_CLOUD)

    # Capa 4: Servicios de negocio (6 contextos DDD)
    o.append(box(160, 380, 803, 98, "4. Servicios de negocio (6 Contextos Delimitados DDD)", C_NET))
    ctxs = [
        ("flow", "Planificación"),
        ("truck", "Flota"),
        ("person", "Personas"),
        ("gps", "Telemetría"),
        ("bus", "Operación"),
        ("chart", "Liquidación")
    ]
    for i, (g, t) in enumerate(ctxs):
        o.append(icon(226 + i * 134, 404, g, t, C_NET, 30))

    # Capa 5: Integración y eventos
    band(490, 88, "5. Integración y eventos", [
        ("stream", "Bus eventos", "Event Hubs"),
        ("queue", "Cola fallidos", "DLQ sin pérdida"),
        ("flow", "Reintento", "Backoff exponencial"),
        ("check", "Capa ACL", "Adaptador ERP")
    ], C_EDGE)

    # Capa 6: Datos
    band(590, 88, "6. Datos", [
        ("db", "Transaccional", "PostgreSQL Flexible"),
        ("clock", "Series GPS", "TimescaleDB"),
        ("archive", "Documental", "ADLS Gen2"),
        ("chart", "Lakehouse", "Delta / Costo km")
    ], C_SITE)

    # Conectores verticales entre capas
    for y in (168, 268, 368, 478, 578):
        o.append(path([(260, y), (260, y + 12)]))
        o.append(path([(860, y), (860, y + 12)]))

    # Pie explicativo
    o.append(f'<text x="561" y="694" font-family="{FONT}" font-size="15" font-weight="600" fill="{INK}" '
             f'text-anchor="middle">Una petición desciende atravesando las seis capas y la respuesta asciende por el mismo camino.</text>')
    o.append(f'<text x="561" y="714" font-family="{FONT}" font-size="15" fill="{MUTED}" '
             f'text-anchor="middle">Seguridad y observabilidad no están en la pila: la cruzan de forma transversal.</text>')
    o.append(f'<text x="561" y="734" font-family="{FONT}" font-size="15" fill="{MUTED}" '
             f'text-anchor="middle">Servicios y Datos operan de forma liviana a bordo del camión para soportar 72h sin cobertura.</text>')

    return page("".join(o), "Arquitectura lógica — las ocho capas obligatorias", "4.1 · A",
                "Num. 2.1 transversal · RT-02.01 a RT-02.13 · RT-17.01 · RT-21.01")

# =============================================================================
# Generación y compilación
# =============================================================================
def main():
    import subprocess
    fig_dir = "recursos/Formato-Oferta-audIT/figuras/04-arquitectura"

    diagrams = [
        ("Main", build_main()),
        ("LogicaCapas", build_logica_capas())
    ]

    for name, svg_content in diagrams:
        svg_path = os.path.join(fig_dir, f"{name}.svg")
        pdf_path = os.path.join(fig_dir, f"{name}.pdf")
        png_path = os.path.join(fig_dir, f"{name}.png")

        # 1. Guardar SVG
        with open(svg_path, "w", encoding="utf-8") as f:
            f.write(svg_content)
        print(f"SVG guardado: {svg_path}")

        # 2. PNG con rsvg-convert (soporta <marker> y stroke-dasharray correctamente)
        # PyMuPDF no renderiza flechas ni líneas punteadas SVG.
        subprocess.run(
            ["rsvg-convert", "-d", "150", "-p", "150", svg_path, "-o", png_path],
            check=True
        )
        print(f"PNG generado: {png_path}")

        # 3. PDF vectorial con rsvg-convert (para LaTeX)
        subprocess.run(
            ["rsvg-convert", "--format=pdf", svg_path, "-o", pdf_path],
            check=True
        )
        print(f"PDF generado: {pdf_path}")

if __name__ == "__main__":
    main()
