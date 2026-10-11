#!/usr/bin/env python3
"""Red PERT/CPM del Subdocumento 7 en dos vistas (D4-61, D4-66).

Una sola fuente para tres salidas con la misma geometría:
  - JSON de Standard Import para Lucid (d11_pert_e1.json y d11_pert_e2.json)
  - SVG y PDF vectorial para el formato (figuras/07-plan-trabajo/pert-etapa1.*)
  - Mermaid para revisarla rápido (D4/mermaid/10-pert-etapa1.mmd y 11-pert-etapa2.mmd)

Marco horizontal de 1700 x 1104 unidades, que en la página ocupa 257,4 x 167,2 mm.
La letra del SVG es de 23,3 unidades, 10 pt impresos. En Lucid es de 10 pt.
Duraciones en días hábiles (FEP01, Art. 10.1), mes contractual de 20 días hábiles.
"""
import html
import json
import math
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(__file__))
from lucidgen import Diagrama, html_texto, ROJO, SECUNDARIO, TINTA, BLANCO, MARINO  # noqa: E402

RAIZ = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))  # carpeta que contiene D4
# El S7 se sacó del formato local (D4-108): las figuras ya no se escriben ahí
FIG = os.path.join(RAIZ, "D4/lucid/salida-pert")
MMD = os.path.join(RAIZ, "D4/mermaid")
AQUI = os.path.dirname(os.path.abspath(__file__))

# ----------------------------------------------------------------------------
# Red: id -> (predecesoras, a, m, b). None en las reservas: se calculan.
# ----------------------------------------------------------------------------
RED = {
    "A01": ([], 4, 5, 6),
    "A02": (["A01"], 28, 32, 42),
    "A03": (["A01"], 38, 44, 56),
    "A04": (["A01"], 45, 58, 83),
    "A05": (["A02"], 32, 37, 48),
    "A06": (["A02"], 95, 118, 153),
    "A07": (["A05"], 29, 35, 47),
    "A08": (["A05", "A07"], 50, 59, 74),
    "A09": (["A07"], 70, 78, 98),
    "A10": (["A04", "A07"], 56, 65, 80),
    "A11": (["A03", "A07"], 50, 59, 74),
    "A12": (["A08", "A09", "A10", "A11"], 30, 33, 42),
    "A13": (["A06", "A09"], 36, 40, 44),
    "A14": (["A12"], None, None, None),
    "A15": (["A13", "A14"], 60, 60, 60),
    "A16": (["A14"], 42, 50, 58),
    "A17": (["A14"], 31, 35, 45),
    "A18": (["A06", "A11", "A14"], 100, 118, 148),
    "A19": (["A15", "A16"], 10, 10, 10),
    "A20": (["A17"], 42, 48, 66),
    "A21": (["A19"], 30, 30, 30),
    "A22": (["A20"], 20, 23, 32),
    "A23": (["A22"], None, None, None),
    "A24": (["A21", "A23"], 40, 40, 40),
    "A25": (["A18", "A24"], 20, 20, 20),
}
# La A13 empieza 10 días hábiles antes de que termine la A09, con el último sprint en preproducción (D4-104)
DESFASE = {("A09", "A13"): -10}
CADENA_E1 = ["A01", "A02", "A05", "A07", "A09", "A12"]
CADENA_E2 = ["A17", "A20", "A22"]


def cpm():
    te, var = {}, {}
    for k, (_, a, m, b) in RED.items():
        if a is None:
            continue
        assert (a + 4 * m + b) % 6 == 0, k
        te[k] = (a + 4 * m + b) // 6
        var[k] = ((b - a) / 6) ** 2
    s1 = math.sqrt(sum(var[k] for k in CADENA_E1))
    s2 = math.sqrt(sum(var[k] for k in CADENA_E2))
    te["A14"], te["A23"] = round(2 * s1), round(2 * s2)
    es, ef = {}, {}
    for k in RED:
        es[k] = max([ef[p] + DESFASE.get((p, k), 0) for p in RED[k][0]], default=0)
        ef[k] = es[k] + te[k]
    fin = max(ef.values())
    suc = {k: [j for j in RED if k in RED[j][0]] for k in RED}
    ls, lf = {}, {}
    for k in reversed(list(RED)):
        lf[k] = min([ls[s] - DESFASE.get((k, s), 0) for s in suc[k]], default=fin)
        ls[k] = lf[k] - te[k]
    ht = {k: ls[k] - es[k] for k in RED}
    hl = {k: min([es[s] - DESFASE.get((k, s), 0) for s in suc[k]], default=fin) - ef[k] for k in RED}
    for k in RED:
        if ht[k] == 0:
            assert hl[k] == 0, k
    return te, es, ef, ls, lf, ht, hl, fin


TE, ES, EF, LS, LF, HT, HL, FIN = cpm()
assert FIN == 420
CRIT = {k for k in RED if HT[k] == 0}

NOMBRE = {
    "A01": ["Inicio", ""], "A02": ["Levantamiento", "y línea base"],
    "A03": ["Cobertura móvil", "en terreno"], "A04": ["Factibilidad", "proveedores"],
    "A05": ["Arquitectura", "y seguridad"], "A06": ["Adhesión de", "transportistas"],
    "A07": ["Infraestructura", "y ambientes"], "A08": ["Migración", "de vigencias"],
    "A09": ["Construcción", "Etapa 1"], "A10": ["Integraciones", ""],
    "A11": ["Piloto a bordo", "por familia"], "A12": ["Certificación", "Etapa 1"],
    "A13": ["Capacitación", "conductores"], "A14": ["Reserva de", "cronograma E1"],
    "A15": ["Marcha blanca", "Etapa 1"], "A16": ["Transferencia", "a TI mandante"],
    "A17": ["Diseño", "Etapa 2"], "A18": ["Instalación", "progresiva"],
    "A19": ["Producción", "Etapa 1"], "A20": ["Construcción", "Etapa 2"],
    "A21": ["Estabilización", "Etapa 1"], "A22": ["Certificación", "Etapa 2"],
    "A23": ["Reserva de", "cronograma E2"], "A24": ["Marcha blanca", "Etapa 2"],
    "A25": ["Producción", "Etapa 2"],
}
HITO = {"A02": "H1", "A05": "H2", "A07": "H3", "A09": "H4", "A12": "H5", "A15": "H6",
        "A17": "H8", "A19": "H7", "A20": "H9", "A22": "H10", "A24": "H11", "A25": "H12"}


def rotulo(k, externo=False):
    cab = f"{k} ({HITO[k]})" if k in HITO else k
    nom = [n for n in NOMBRE[k] if n]
    if externo:
        return [cab] + nom + ["(vista Etapa 1)"]
    return [cab] + nom + [f"{TE[k]} d, ES {ES[k]}", f"HT {HT[k]}, HL {HL[k]}"]


# ----------------------------------------------------------------------------
# Geometría: 7 columnas por ES y 5 carriles. W x H por actividad.
# ----------------------------------------------------------------------------
ANCHO, ALTO = 1700, 1104
W, H, G = 220, 170, 23
X0 = (ANCHO - 7 * W - 6 * G) / 2
FILAS = [30, 210, 390, 570, 750]
LETRA_SVG = 23.3          # 10 pt impresos con el marco a 257,4 mm
LINEA_SVG = 28


def caja(col, fila):
    return (X0 + col * (W + G), FILAS[fila], W, H)


# vista: lista de (id, columna, fila, externo) y aristas con su ruta
VISTAS = {
    "etapa1": {
        "titulo": "Red PERT, Etapa 1 hasta el inicio de la marcha blanca",
        "nodos": [("A01", 0, 2, False), ("A02", 1, 2, False), ("A03", 1, 3, False),
                  ("A04", 1, 4, False), ("A06", 2, 0, False), ("A05", 2, 2, False),
                  ("A07", 3, 2, False), ("A08", 4, 1, False), ("A09", 4, 2, False),
                  ("A11", 4, 3, False), ("A10", 4, 4, False), ("A13", 5, 0, False),
                  ("A12", 5, 2, False), ("A14", 6, 2, False)],
        "nota": "A06, A11, A13 y A14 siguen en la vista del solapamiento y la Etapa 2.",
        # aristas cuyo tramo vertical va junto al origen (el carril del origen está ocupado)
        "junto_origen": {("A05", "A08")},
    },
    "etapa2": {
        "titulo": "Red PERT, solapamiento de los meses 13 a 15 y Etapa 2",
        "nodos": [("A13", 0, 0, True), ("A14", 0, 2, False), ("A06", 0, 3, True),
                  ("A11", 0, 4, True), ("A15", 1, 0, False), ("A16", 1, 1, False),
                  ("A17", 1, 2, False), ("A18", 1, 4, False), ("A19", 2, 0, False),
                  ("A20", 2, 2, False), ("A21", 3, 0, False), ("A22", 3, 2, False),
                  ("A23", 4, 2, False), ("A24", 5, 2, False), ("A25", 6, 2, False)],
        "nota": None,
        "junto_origen": set(),
    },
}
LEYENDA = [
    "Rojo y trazo grueso: ruta crítica, con holgura total y libre igual a cero. Borde punteado: actividad dibujada en la otra vista.",
    "d: días hábiles. ES: inicio temprano. HT: holgura total. HL: holgura libre. Entre paréntesis, el hito del Formulario E-25.",
]


def aristas(vista):
    ids = {n[0] for n in vista["nodos"]}
    ext = {n[0] for n in vista["nodos"] if n[3]}
    out = []
    for k in RED:
        if k not in ids or k in ext:
            continue
        for p in RED[k][0]:
            if p in ids:
                out.append((p, k))
    return out


def geometria(vista):
    pos = {n[0]: caja(n[1], n[2]) for n in vista["nodos"]}
    eds = aristas(vista)
    # puntos de entrada repartidos en el lado izquierdo del destino
    entrada = {}
    for d in {e[1] for e in eds}:
        ins = sorted([e for e in eds if e[1] == d], key=lambda e: pos[e[0]][1])
        rect = [e for e in ins if pos[e[0]][1] == pos[d][1]]
        arriba = [e for e in ins if pos[e[0]][1] < pos[d][1]]
        abajo = [e for e in ins if pos[e[0]][1] > pos[d][1]]
        for e in rect:
            entrada[e] = 0.5
        for i, e in enumerate(arriba):
            entrada[e] = 0.18 + 0.22 * i / max(1, len(arriba))
        for i, e in enumerate(abajo):
            entrada[e] = 0.62 + 0.22 * (i + 1) / max(1, len(abajo))
        if not rect and len(ins) == 1:
            entrada[ins[0]] = 0.5
    # tramo vertical de cada arista: en el hueco junto al destino, o junto al origen
    vert = {}
    for (a, b) in eds:
        xa, ya, wa, ha = pos[a]
        y1, y2 = ya + ha / 2, pos[b][1] + pos[b][3] * entrada[(a, b)]
        if abs(y1 - y2) >= 0.5:
            vert[(a, b)] = xa + wa + G / 2 if (a, b) in vista["junto_origen"] else pos[b][0] - G / 2
    # los destinos que comparten un hueco reciben tramos verticales separados
    desplaza = {}
    for xv in set(vert.values()):
        destinos = sorted({b for e, x in vert.items() if x == xv for b in [e[1]]},
                          key=lambda b: pos[b][1])
        for i, b in enumerate(destinos):
            desplaza[(xv, b)] = (i - (len(destinos) - 1) / 2) * 9
    rutas = []
    for (a, b) in eds:
        xa, ya, wa, ha = pos[a]
        xb, yb, wb, hb = pos[b]
        x1, y1 = xa + wa, ya + ha / 2
        x2, y2 = xb, yb + hb * entrada[(a, b)]
        if (a, b) not in vert:
            pts = [(x1, y1), (x2, y2)]
        else:
            xv = vert[(a, b)] + desplaza[(vert[(a, b)], b)]
            pts = [(x1, y1), (xv, y1), (xv, y2), (x2, y2)]
        rutas.append((a, b, pts, a in CRIT and b in CRIT))
    return pos, rutas, entrada


# ----------------------------------------------------------------------------
# SVG
# ----------------------------------------------------------------------------
def svg(nombre, vista):
    pos, rutas, _ = geometria(vista)
    ext = {n[0] for n in vista["nodos"] if n[3]}
    mm_w = 257.4
    mm_h = mm_w * ALTO / ANCHO
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{mm_w}mm" height="{mm_h:.1f}mm" '
         f'viewBox="0 0 {ANCHO} {ALTO}" font-family="IBM Plex Sans">',
         '<defs>'
         f'<marker id="fr" viewBox="0 0 10 10" refX="10" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="{ROJO}"/></marker>'
         f'<marker id="fg" viewBox="0 0 10 10" refX="10" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="{SECUNDARIO}"/></marker>'
         '</defs>',
         f'<rect x="0" y="0" width="{ANCHO}" height="{ALTO}" fill="{BLANCO}"/>']
    # líneas no críticas debajo, críticas encima
    for critica in (False, True):
        for (a, b, pts, c) in rutas:
            if c != critica:
                continue
            d = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
            color, ancho, m = (ROJO, 4, "fr") if c else (SECUNDARIO, 1.8, "fg")
            o.append(f'<polyline points="{d}" fill="none" stroke="{color}" stroke-width="{ancho}" '
                     f'stroke-linejoin="round" marker-end="url(#{m})"/>')
    for k, (x, y, w, h) in pos.items():
        c = k in CRIT and k not in ext
        if k in ext:
            borde, rell, gros, guion = SECUNDARIO, "#F6F8FB", 1.8, ' stroke-dasharray="8,6"'
        elif c:
            borde, rell, gros, guion = ROJO, "#FBECEC", 4, ""
        else:
            borde, rell, gros, guion = SECUNDARIO, BLANCO, 1.8, ""
        o.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{w}" height="{h}" rx="6" fill="{rell}" '
                 f'stroke="{borde}" stroke-width="{gros}"{guion}/>')
        lineas = rotulo(k, k in ext)
        y0 = y + h / 2 - (len(lineas) - 1) * LINEA_SVG / 2 + LETRA_SVG * 0.35
        for i, t in enumerate(lineas):
            peso = ' font-weight="600"' if i == 0 else ""
            o.append(f'<text x="{x + w / 2:.1f}" y="{y0 + i * LINEA_SVG:.1f}" font-size="{LETRA_SVG}" '
                     f'text-anchor="middle" fill="{TINTA}"{peso}>{html.escape(t)}</text>')
    ley = LEYENDA + ([vista["nota"]] if vista["nota"] else [])
    for i, t in enumerate(ley):
        o.append(f'<text x="{X0:.1f}" y="{ALTO - 30 - (len(ley) - 1 - i) * 34:.1f}" font-size="{LETRA_SVG}" '
                 f'fill="{SECUNDARIO}">{html.escape(t)}</text>')
    o.append("</svg>")
    ruta = os.path.join(FIG, f"pert-{nombre}.svg")
    with open(ruta, "w") as f:
        f.write("\n".join(o) + "\n")
    subprocess.run(["rsvg-convert", "-f", "pdf", "-o", ruta[:-4] + ".pdf", ruta], check=True)
    return ruta


# ----------------------------------------------------------------------------
# Lucid (Standard Import)
# ----------------------------------------------------------------------------
def lucid(nombre, vista):
    pos, rutas, entrada = geometria(vista)
    ext = {n[0] for n in vista["nodos"] if n[3]}
    d = Diagrama(vista["titulo"], ANCHO, ALTO, marco=False)
    ids = {}
    for k, (x, y, w, h) in pos.items():
        c = k in CRIT and k not in ext
        borde = ROJO if c else SECUNDARIO
        rell = "#FBECEC" if c else ("#F6F8FB" if k in ext else BLANCO)
        ids[k] = d.caja(x, y, w, h, rotulo(k, k in ext), borde=borde, relleno=rell,
                        dashed=k in ext)
        if c:
            d.formas[-1]["style"]["stroke"]["width"] = 3
    for (a, b, pts, c) in rutas:
        color, ancho = (ROJO, 3) if c else (SECUNDARIO, 1.5)
        salta = pos[b][0] - (pos[a][0] + pos[a][2]) > G + 1
        if len(pts) > 2 and ((a, b) in vista["junto_origen"] or salta):
            # tramos fijos: el codo automático de Lucid cruzaría las actividades del medio
            for i in range(len(pts) - 1):
                d.lineas.append({"id": d._id("l"), "lineType": "straight",
                                 "endpoint1": {"type": "positionEndpoint", "style": "none",
                                               "position": {"x": pts[i][0], "y": pts[i][1]}},
                                 "endpoint2": {"type": "positionEndpoint",
                                               "style": "arrow" if i == len(pts) - 2 else "none",
                                               "position": {"x": pts[i + 1][0], "y": pts[i + 1][1]}},
                                 "stroke": {"color": color, "width": ancho, "style": "solid"}})
        else:
            d.linea(ids[a], ids[b], pa=(1, 0.5), pb=(0, round(entrada[(a, b)], 3)), color=color,
                    ancho=ancho, tipo="straight" if len(pts) == 2 else "elbow")
    ley = LEYENDA + ([vista["nota"]] if vista["nota"] else [])
    d.texto(X0, ALTO - 20 - 30 * len(ley), ley, color=SECUNDARIO, w=ANCHO - 2 * X0)
    ruta = os.path.join(AQUI, f"d11_pert_{nombre}.json")
    with open(ruta, "w") as f:
        f.write(d.json())
    return ruta


# ----------------------------------------------------------------------------
# Mermaid
# ----------------------------------------------------------------------------
def mermaid(nombre, vista, numero):
    ext = {n[0] for n in vista["nodos"] if n[3]}
    o = [f"%% {vista['titulo']}. Generado por D4/lucid/d11_pert.py, misma red que la figura del S7.",
         "flowchart LR"]
    for k, _, _, e in vista["nodos"]:
        o.append(f'    {k}["{"<br/>".join(html.escape(t) for t in rotulo(k, e))}"]')
    eds = aristas(vista)
    for a, b in eds:
        o.append(f"    {a} --> {b}")
    o.append(f"    classDef critica fill:#FBECEC,stroke:{ROJO},stroke-width:3px,color:{TINTA}")
    o.append(f"    classDef normal fill:#FFFFFF,stroke:{SECUNDARIO},stroke-width:1px,color:{TINTA}")
    o.append(f"    classDef externa fill:#F6F8FB,stroke:{SECUNDARIO},stroke-dasharray:6 4,color:{TINTA}")
    nodos = [n[0] for n in vista["nodos"]]
    crit = [k for k in nodos if k in CRIT and k not in ext]
    norm = [k for k in nodos if k not in CRIT and k not in ext]
    for cls, grupo in (("critica", crit), ("normal", norm), ("externa", sorted(ext))):
        if grupo:
            o.append(f"    class {','.join(grupo)} {cls}")
    idx = [str(i) for i, (a, b) in enumerate(eds) if a in CRIT and b in CRIT]
    if idx:
        o.append(f"    linkStyle {','.join(idx)} stroke:{ROJO},stroke-width:4px")
    ruta = os.path.join(MMD, f"{numero}-pert-{nombre}.mmd")
    with open(ruta, "w") as f:
        f.write("\n".join(o) + "\n")
    return ruta


if __name__ == "__main__":
    os.makedirs(FIG, exist_ok=True)
    for n, (nombre, vista) in enumerate(VISTAS.items()):
        print(svg(nombre, vista))
        print(lucid(nombre, vista))
        print(mermaid(nombre, vista, 10 + n))
    print("ruta crítica:", " ".join(k for k in RED if k in CRIT), "fin", FIN)
