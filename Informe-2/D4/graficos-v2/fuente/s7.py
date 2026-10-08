"""Subdocumento 7: las dos redes PERT.

Actividades, precedencias, duraciones, tiempos y ruta crítica se leen de la malla
del Formulario T-15 (tabla 7-malla). De D4/lucid/d11_pert.py solo se toma la
ubicación de cada actividad en la grilla (columna y fila), que no es un dato.
"""
import importlib.util
import os
import re

from lienzo import Figura, ROJO, BORDE, ancho

C7 = "07-plan-trabajo"
T15 = "/mnt/NuevoVol/FEP/Formato-Oferta-audIT/subdocumentos/07-plan-trabajo/formularios/T-15.tex"
PERT_PY = "/mnt/NuevoVol/FEP/D4/lucid/d11_pert.py"

# Nombre corto de cada actividad, con palabras de su descripción en el T-15. La
# descripción completa no cabe en un nodo a 10 pt; la equivalencia va en el informe.
CORTO = {
    "A01": ["Inicio del", "proyecto"], "A02": ["Levantamiento", "y línea base"],
    "A03": ["Cobertura móvil", "en terreno"], "A04": ["Factibilidad con", "proveedores"],
    "A05": ["Arquitectura", "y seguridad"], "A06": ["Plan de adhesión", "de transportistas"],
    "A07": ["Infraestructura", "y ambientes"], "A08": ["Migración de", "las vigencias"],
    "A09": ["Construcción", "de la Etapa 1"], "A10": ["Integraciones", "y plataformas"],
    "A11": ["Piloto de 10 y", "flota propia"], "A12": ["Certificación", "de la Etapa 1"],
    "A13": ["Capacitación de", "conductores"], "A14": ["Reserva de la", "Etapa 1"],
    "A15": ["Marcha blanca", "de la Etapa 1"], "A16": ["Transferencia", "tecnológica"],
    "A17": ["Diseño detallado", "de la Etapa 2"], "A18": ["Terceros y", "montaje restante"],
    "A19": ["Paso a producción", "de la Etapa 1"], "A20": ["Construcción", "de la Etapa 2"],
    "A21": ["Estabilización", "de la Etapa 1"], "A22": ["Certificación", "de la Etapa 2"],
    "A23": ["Reserva de la", "Etapa 2"], "A24": ["Marcha blanca", "de la Etapa 2"],
    "A25": ["Paso a producción", "de la Etapa 2"],
}


def leer_t15():
    t = open(T15, encoding="utf-8").read()
    filas = {}
    patron = re.compile(r"^(A\d\d) & (.+?) & (.+?) & (\d+) & (\d+) & (\d+) & (\d+) & (\d+) & (\d+) & (\d+) & (Sí|No) \\\\",
                        re.M)
    num = {m.start(): t.count("\n", 0, m.start()) + 1 for m in patron.finditer(t)}
    for m in patron.finditer(t):
        k, desc, pred = m.group(1), m.group(2), m.group(3)
        hito = re.search(r"\((H\d+)", desc)
        filas[k] = dict(desc=desc, pred=[] if pred == "Ninguna" else [p.strip() for p in pred.split(",")],
                        dur=int(m.group(4)), ES=int(m.group(5)), EF=int(m.group(6)), LS=int(m.group(7)),
                        LF=int(m.group(8)), HT=int(m.group(9)), HL=int(m.group(10)), crit=m.group(11) == "Sí",
                        hito=hito.group(1) if hito else None, linea=num[m.start()])
    return filas


def _d11():
    spec = importlib.util.spec_from_file_location("d11_pert", PERT_PY)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def diferencias():
    """Lo que no coincide entre el T-15 y d11_pert.py."""
    t, m = leer_t15(), _d11()
    out = []
    for k, f in t.items():
        pred_d = sorted(m.RED[k][0])
        if sorted(f["pred"]) != pred_d:
            out.append(f"{k}: precedentes {', '.join(f['pred']) or 'ninguno'} en el T-15 y {', '.join(pred_d)} en d11_pert.py")
        for c in ("ES", "EF", "LS", "LF"):
            if getattr(m, c)[k] != f[c]:
                out.append(f"{k}: {c} {f[c]} en el T-15 y {getattr(m, c)[k]} en d11_pert.py")
        if m.TE[k] != f["dur"]:
            out.append(f"{k}: duración {f['dur']} en el T-15 y {m.TE[k]} en d11_pert.py")
        nd = " ".join(n for n in m.NOMBRE[k] if n)
        out.append(f"{k}: nombre «{nd}» en d11_pert.py; en el T-15 «{f['desc']}»")
    return out


def pert(nombre):
    t, m = leer_t15(), _d11()
    f = Figura(f"pert-{nombre}", C7, "H")
    vista = m.VISTAS[nombre]
    W, G, H, P = 92.0, 11.6, 70.0, 89.0
    X0 = (f.W - 7 * W - 6 * G) / 2
    Y0 = 26.0
    celda = {(c, r): k for k, c, r, _ in vista["nodos"]}
    ext = {k for k, _, _, e in vista["nodos"] if e}
    pos = {k: (X0 + c * (W + G), Y0 + r * P, c, r) for k, c, r, _ in vista["nodos"]}
    critico = {k for k in pos if t[k]["crit"] and k not in ext}

    # eje de meses: mes de inicio de cada columna (20 días hábiles por mes)
    f.linea([(X0, 17), (X0 + 7 * W + 6 * G, 17)], flecha=None, saltos=False)
    for c in range(7):
        ks = [k for k, (_, _, cc, _) in pos.items() if cc == c and k not in ext] or \
             [k for k, (_, _, cc, _) in pos.items() if cc == c]
        mes = 1 + min(t[k]["ES"] for k in ks) // 20
        xc = X0 + c * (W + G) + W / 2
        f.linea([(xc, 14), (xc, 20)], flecha=None, saltos=False)
        f.texto(xc, 10.5, f"Mes {mes}", 9, anc="middle")

    # aristas
    aristas = []
    for b in pos:
        if b in ext:
            continue
        for a in t[b]["pred"]:
            if a in pos:
                aristas.append((a, b))

    def libre(fila, c0, c1):
        return all((c, fila) not in celda for c in range(c0, c1 + 1))

    plan = []
    for a, b in aristas:
        xa, ya, ca, ra = pos[a]
        xb, yb, cb, rb = pos[b]
        crit = a in critico and b in critico
        if ra == rb and libre(ra, ca + 1, cb - 1):
            plan.append((a, b, None, crit))
        elif cb == ca + 1 or libre(ra, ca + 1, cb - 1):
            plan.append((a, b, ("dest", cb - 1), crit))
        else:
            plan.append((a, b, ("orig", ca), crit))
    # verticales por hueco: bus común si varias aristas comparten destino u origen
    por_hueco = {}
    for a, b, v, crit in plan:
        if v:
            g = v[1]
            por_hueco.setdefault(g, []).append((a, b, crit))
    clave, xv = {}, {}
    for g, lst in por_hueco.items():
        nd = {}
        ns = {}
        for a, b, crit in lst:
            if not crit:
                nd[b] = nd.get(b, 0) + 1
                ns[a] = ns.get(a, 0) + 1
        claves = []
        for a, b, crit in lst:
            if not crit and nd[b] >= 2:
                k = ("d", b)
            elif not crit and ns[a] >= 2:
                k = ("s", a)
            else:
                k = ("e", a, b)
            clave[(a, b)] = (g, k)
            if k not in claves:
                claves.append(k)
        claves.sort(key=lambda k: min(pos[x][1] for x in k[1:]))
        for i, k in enumerate(claves):
            xv[(g, k)] = X0 + (g + 1) * (W + G) - G / 2 + (i - (len(claves) - 1) / 2) * 3.6
    # puntos de entrada en el destino
    entradas = {}
    for b in pos:
        llegan = [(a, b, v, c) for a, b2, v, c in plan if b2 == b for a in [a]]
    for a, b, v, crit in plan:
        _, yb = pos[b][0], pos[b][1]
        ya = pos[a][1]
        if crit or ya == yb:
            entradas[(a, b)] = yb + H / 2
        else:
            g, k = clave[(a, b)]
            if k[0] == "d":
                entradas[(a, b)] = yb + H / 2 + 16
            else:
                entradas[(a, b)] = yb + H / 2 + (-16 if ya < yb else 16)
    # separa entradas distintas que caen en el mismo punto
    vistos = {}
    for (a, b), y in sorted(entradas.items(), key=lambda e: pos[e[0][0]][1]):
        g = clave.get((a, b))
        k = (b, round(y, 1))
        if k in vistos and vistos[k] != (g[1] if g else None):
            entradas[(a, b)] = y + 9
        vistos.setdefault(k, g[1] if g else None)

    for crit_pase in (False, True):
        for a, b, v, crit in plan:
            if crit != crit_pase:
                continue
            xa, ya, _, _ = pos[a]
            xb, yb, _, _ = pos[b]
            y1 = ya + H / 2
            y2 = entradas[(a, b)]
            if v is None:
                pts = [(xa + W, y1), (xb, y1)]
            else:
                x = xv[clave[(a, b)]]
                if v[0] == "orig" and len(range(pos[a][2] + 1, pos[b][2])) > 0:
                    pts = [(xa + W, y1), (x, y1), (x, y2), (xb, y2)]
                else:
                    pts = [(xa + W, y1), (x, y1), (x, y2), (xb, y2)]
            f.linea(pts, color=ROJO if crit else "#2B2B2B", grosor=1.5 if crit else 1.0)

    # nodos
    for k, (x, y, _, _) in pos.items():
        d = t[k]
        es_ext = k in ext
        crit = k in critico
        f.rect(x, y, W, H, relleno="#FFFFFF", borde=ROJO if crit else BORDE, grosor=1.5 if crit else 0.75,
               rx=6, disc=es_ext)
        f.cajas_icono.append((x, y, x + W, y + H, k))
        nom = CORTO[k]
        for l in nom:
            assert ancho(l, 10) <= W - 8, (k, l, ancho(l, 10))
        if es_ext:
            f.texto(x + W / 2, y + 24, k, 10, 600, "middle")
            for i, l in enumerate(nom):
                f.texto(x + W / 2, y + 38 + i * 12, l, 10, anc="middle")
            continue
        f.texto(x + 6, y + 13, k, 10, 600)
        f.texto(x + 6 + ancho(k, 10, 600) + 5, y + 13, f"{d['dur']} días", 9)
        if d["hito"]:
            wh = ancho(d["hito"], 9, 600)
            f.texto(x + W - 6, y + 13, d["hito"], 9, 600, "end")
            f.rombo(x + W - 6 - wh - 7, y + 9.8, 4)
        for i, l in enumerate(nom):
            f.texto(x + W / 2, y + 27 + i * 11.5, l, 10, anc="middle")
        f.texto(x + W / 2, y + 52, f"ES {d['ES']} · EF {d['EF']}", 9, anc="middle")
        f.texto(x + W / 2, y + 63, f"LS {d['LS']} · LF {d['LF']}", 9, anc="middle")
        if not crit:
            f.ficha(x + W / 2, y + H + 9, f"Holgura {d['HT']}")
    return f.guardar()


def pert_etapa1():
    return pert("etapa1")


def pert_etapa2():
    return pert("etapa2")


FIGURAS = [pert_etapa1, pert_etapa2]


# ---------------------------------------------------------------------------- EDT y Gantt (dupla 2)
S7TEX = "/mnt/NuevoVol/FEP/Formato-Oferta-audIT/subdocumentos/07-plan-trabajo/contenido.tex"


def _tikz(etiqueta):
    t = open(S7TEX, encoding="utf-8").read()
    i = t.index("{" + etiqueta + "}")
    return t[i:t.index(r"\end{tikzpicture}", i)]


def edt():
    t = _tikz("7-edt")
    raiz = re.search(r"\(raiz\) at \([^)]*\) \{([^}]*)\}", t).group(1)
    nodos = re.findall(r"\\node\[(n1|t)\] at \(([\d.]+)mm,[-\d.]+mm\) \{([^}]*)\}", t)
    cols = {}
    for tipo, x, s in nodos:
        col = 0 if float(x) < 50 else 1
        if tipo == "n1":
            cols.setdefault(col, []).append([s, []])
        else:
            cols[col][-1][1].append(s)
    f = Figura("edt", C7, "V", alto=560)
    f.caja(8, 6, 406, 24, [(raiz, 10, 600)], rx=4)
    f.linea([(211, 30), (211, 40)], flecha=None)
    f.linea([(110, 40), (312, 40)], flecha=None)
    for col, elementos in cols.items():
        x = 8 + col * 208
        f.linea([(x + 102, 40), (x + 102, 46)])
        y = 48
        for nombre, paquetes in elementos:
            h = 21 + 13.2 * len(paquetes) + 2
            f.grupo(x, y, 198, h, nombre, rx=6)
            for i, p in enumerate(paquetes):
                f.ficha(x + 10, y + 27.5 + i * 13.2, p, anc="start", alto=12, w=178)
            y += h + 3
    return f.guardar()


def gantt():
    t = _tikz("7-gantt")
    mm0, mmmes = 40.0, 1.9
    def mes(xmm):
        return (float(xmm) - mm0) / mmmes
    f = Figura("gantt", C7, "H")
    X0, X1 = 150.0, 716.0
    pm = (X1 - X0) / 56
    def X(m):
        return X0 + m * pm
    filas = re.findall(r"\\node\[lab\] at \(0mm,(-[\d.]+)mm\) \{(\d+ [^}]*)\}", t)
    y0, paso = 58, 28.0
    yfila = {}
    # temporada de diciembre a abril, en gris muy claro
    for a, b in re.findall(r"\\fill\[audit-gris-claro\] \(([\d.]+)mm,9\.0mm\) rectangle \(([\d.]+)mm,-78\.4mm\)", t):
        f.rect(X(mes(a)), 40, X(mes(b)) - X(mes(a)), y0 + paso * 14 - 40, relleno="#EFEFEF", borde=None)
    # años y meses del contrato
    for xa, anio in re.findall(r"\\node\[t\] at \(([\d.]+)mm,6\.5mm\) \{(\d{4})\}", t):
        f.texto(X(mes(xa)), 18, anio, 9, 600, "middle")
    for xl in re.findall(r"\\draw\[audit-filete\] \(([\d.]+)mm,9\.0mm\) -- \([\d.]+mm,4\.5mm\)", t):
        f.linea([(X(mes(xl)), 8), (X(mes(xl)), 22)], flecha=None, saltos=False)
    for xm, m in re.findall(r"\\node\[t\] at \(([\d.]+)mm,2\.2mm\) \{(\d+)\}", t):
        f.texto(X(int(m) - 0.5), 34, m, 9, anc="middle")
        f.linea([(X(int(m) - 1), 38), (X(int(m) - 1), 42)], flecha=None, saltos=False)
    f.texto(8, 18, "Año", 9, 600)
    f.texto(8, 34, "Mes del contrato", 9, 600)
    f.linea([(X0, 40), (X1, 40)], flecha=None, saltos=False)
    for i, (ymm, nombre) in enumerate(filas):
        y = y0 + i * paso
        yfila[ymm] = y
        f.texto(8, y + 3.5, nombre, 10)
        if i < len(filas) - 1:
            f.linea([(X0, y + paso / 2), (X1, y + paso / 2)], flecha=None, color="#E0E0E0", grosor=0.5, saltos=False)
    # barras
    patron = re.compile(r"\\draw\[fill=([^,]+),draw=audit-marino,line width=0\.4pt\] \(([\d.]+)mm,(-[\d.]+)mm\) "
                        r"rectangle \(([\d.]+)mm,(-[\d.]+)mm\)")
    for relleno, xa, ya, xb, yb in patron.findall(t):
        ycen = (float(ya) + float(yb)) / 2
        fila = min(yfila, key=lambda k: abs(float(k) - ycen))
        y = yfila[fila]
        a, b = X(mes(xa)), X(mes(xb))
        if relleno == "audit-turquesa!45":       # marcha blanca
            f.rect(a, y - 6, b - a, 12, relleno="#C8C8C8", borde="#404040", grosor=0.6)
        elif relleno == "audit-marino":          # paso a producción
            f.rect(a, y - 6, b - a, 12, relleno="#404040", borde="#404040", grosor=0.6)
        elif relleno.startswith("audit-gris"):   # operación
            f.rect(a, y - 6, b - a, 12, relleno="#FFFFFF", borde="#404040", grosor=0.75, disc=True)
        else:
            f.rect(a, y - 6, b - a, 12, relleno="#FFFFFF", borde="#404040", grosor=0.75)
    # hitos del E-25
    yh = y0 + len(filas) * paso
    f.texto(8, yh + 3.5, "Hitos del E-25", 10)
    hitos = sorted(float(x) for x in re.findall(r"\\fill\[audit-marino\] \(([\d.]+)mm,-74\.00mm\)", t))
    t15 = leer_t15()
    orden = sorted([(d["ES"] if "al inicio" in d["desc"] else d["EF"], d["hito"]) for d in t15.values() if d["hito"]])
    for i, (xmm, (_, h)) in enumerate(zip(hitos, orden)):
        x = X(mes(xmm))
        f.rombo(x, yh, 4.2)
        f.texto(x, yh + (16 if i % 2 == 0 else -9), h, 9, anc="middle")
    return f.guardar()


FIGURAS = [pert_etapa1, pert_etapa2, edt, gantt]
