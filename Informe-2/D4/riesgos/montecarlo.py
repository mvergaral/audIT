"""Simulación Monte Carlo del cronograma de la oferta (S7, red PERT del T-15).

La red se lee completa del Formulario T-15: actividades, hitos (G13), precedencias con desfase
(«A09 FS$-10$») y duraciones (tabla 7-malla), y las estimaciones de tres puntos (tabla 7-tres-puntos).
Distribución Beta-PERT. Las reservas A14 y A23 se modelan como fechas fijas: la marcha blanca de la
Etapa 1 empieza en el día 240 (H6) y la de la Etapa 2 en el día 360 (H11), salvo que algo llegue tarde.

G13 es la entrega probada y congelada de PREPROD, con datos ficticios y material por perfil, al cierre
del sprint 7 de los ocho de A09. Su disponibilidad no se da por cierta por el solo adelanto: se simula
como el cierre de ese sprint, que depende de cómo avance A09, y A13 empieza cuando se cumplen a la vez
A06, A09 FS-10 y G13 (acuerdo del T-15, D4-127). Datos y material se suponen listos con esa versión.

Uso: python3 montecarlo.py        red del T-15
     python3 montecarlo.py sin    A13 después del fin de A09, solo para comparar
"""
import json
import pathlib
import re
import sys

import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "graficos-v2" / "fuente"))
import rutas  # noqa: E402

MODO = sys.argv[1] if len(sys.argv) > 1 else "acuerdo"
assert MODO in ("acuerdo", "sin"), MODO
T15 = pathlib.Path(rutas.T15).read_text(encoding="utf-8")

tres = {m.group(1): tuple(int(x) for x in m.groups()[1:4])
        for m in re.finditer(r"^(A\d\d) & (\d+) & (\d+) & (\d+) & \d+ & [\d,]+ \\\\", T15, re.M)}
malla = {}
for m in re.finditer(r"^([AG]\d\d) & (.+?) & (.+?) & (\d+) & (\d+) & (\d+) & (\d+) & (\d+) & (\d+) & (\d+) & (Sí|No) \\\\",
                     T15, re.M):
    pre = []
    if m.group(3) != "Ninguna":
        for p in m.group(3).split(","):
            d = re.match(r"\s*([AG]\d\d)(?:\s*FS\$?([-−+]\d+)\$?)?\s*$", p)
            assert d, p
            pre.append((d.group(1), int(d.group(2).replace("−", "-")) if d.group(2) else 0))
    malla[m.group(1)] = dict(pre=pre, dur=int(m.group(4)), es=int(m.group(5)), ef=int(m.group(6)))
assert len(malla) == 26 and "G13" in malla and len(tres) == 18, (len(malla), len(tres))

N, rng = 10_000, np.random.default_rng(2026)


def duracion(a):
    if a in tres:
        lo, mo, hi = tres[a]
        al, be = 1 + 4 * (mo - lo) / (hi - lo), 1 + 4 * (hi - mo) / (hi - lo)
        return lo + rng.beta(al, be, N) * (hi - lo)
    return np.full(N, float(malla[a]["dur"]))


D = {a: duracion(a) for a in sorted(malla)}
S, EF = {}, {}
FIJAS = {"A14": 240.0, "A23": 360.0}           # reservas: el hito que protegen queda en esa fecha


def calcular(a):
    if a in EF:
        return EF[a]
    pre = malla[a]["pre"]
    if MODO == "sin" and a == "A13":
        pre = [("A06", 0), ("A09", 0)]
    inicio = np.zeros(N)
    for p, desfase in pre:
        inicio = np.maximum(inicio, calcular(p) + desfase)
    if a == "G13":                              # cierre del sprint 7 de los ocho de A09
        inicio = np.maximum(inicio, S["A09"] + D["A09"] * 7 / 8)
    S[a] = inicio
    EF[a] = np.maximum(FIJAS[a], inicio) if a in FIJAS else inicio + D[a]
    return EF[a]


for a in sorted(malla):
    calcular(a)
# comprobación: sin incertidumbre, la red reproduce los tiempos tempranos del T-15
for a, f in malla.items():
    assert a in FIJAS or a == "G13" or abs(f["es"] + f["dur"] - f["ef"]) < 1e-9, a

hitos = [("H1", EF["A02"], 40), ("H2", EF["A05"], 80), ("H3", EF["A07"], 120), ("H4", EF["A09"], 200),
         ("H5", EF["A12"], 240), ("H6", S["A15"], 240), ("H8", EF["A17"], 280), ("H7", EF["A19"], 320),
         ("H9", EF["A20"], 340), ("H10", EF["A22"], 360), ("H11", S["A24"], 360), ("H12", EF["A25"], 420)]
p = lambda x: round(float(np.mean(x)) * 100, 1)  # noqa: E731
res = {"corridas": N, "semilla": 2026, "modo_A13": MODO, "hitos": {h: p(v <= lim) for h, v, lim in hitos}}
res["sin_reserva"] = {"A12 en el día 226": p(EF["A12"] <= 226), "A22 en el día 350": p(EF["A22"] <= 350)}
res["percentiles_fin_A12"] = {q: round(float(np.percentile(EF["A12"], q)), 1) for q in (50, 80, 95)}
res["percentiles_inicio_A15"] = {q: round(float(np.percentile(S["A15"], q)), 1) for q in (50, 80, 95)}
pred = np.argmax(np.vstack([EF["A08"], EF["A09"], EF["A10"], EF["A11"]]), axis=0)
res["define_inicio_A12"] = {a: p(pred == i) for i, a in enumerate(["A08", "A09", "A10", "A11"])}
res["A13_retrasa_marcha_blanca"] = p(EF["A13"] > EF["A14"])
res["A13_empieza_despues_del_dia_182"] = p(S["A13"] > 182)
res["percentiles_inicio_A13"] = {q: round(float(np.percentile(S["A13"], q)), 1) for q in (50, 80, 95)}
res["G13_despues_del_dia_182"] = p(EF["G13"] > 182)
res["percentiles_G13"] = {q: round(float(np.percentile(EF["G13"], q)), 1) for q in (50, 80, 95)}
res["holgura_A13_a_marcha_blanca"] = {q: round(float(np.percentile(EF["A14"] - EF["A13"], q)), 1) for q in (5, 50)}
res["A18_define_H12"] = p(EF["A18"] > EF["A24"])
res["ambas_marchas_blancas_a_tiempo"] = p((S["A15"] <= 240) & (S["A24"] <= 360))
nombre = "montecarlo.json" if MODO == "acuerdo" else "montecarlo-sin-adelanto.json"
pathlib.Path(__file__).with_name(nombre).write_text(json.dumps(res, ensure_ascii=False, indent=2) + "\n")
print(json.dumps(res, ensure_ascii=False))
