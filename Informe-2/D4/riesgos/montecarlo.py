"""Simulación Monte Carlo del cronograma de la oferta (S7, red PERT del T-15).

Datos: estimaciones de tres puntos (tabla 7-tres-puntos) y malla de precedencias (tabla 7-malla)
del Formulario T-15, leídas del archivo. Distribución Beta-PERT. Las reservas A14 y A23 se modelan
como fechas fijas: la marcha blanca de la Etapa 1 empieza en el día 240 (H6) y la de la Etapa 2 en
el día 360 (H11), salvo que algo llegue tarde. Los límites de los hitos salen de la tabla 7-hitos
del S7. Uso: python3 montecarlo.py
"""
import re, json, pathlib, sys
import numpy as np
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "graficos-v2" / "fuente"))
import rutas  # noqa: E402

# El S7 es de la dupla 2 (D4-108). Se leen las duraciones de su T-15 vigente en el repositorio.
# A13 sigue el acuerdo con D2 (D4-127): empieza 10 días hábiles antes del fin de A09, día 182 en la
# línea base, y solo si están las funciones de entrenamiento probadas y congeladas en PREPROD, los datos
# ficticios y el material por perfil. La versión congelada es la del sprint 7 de los ocho de A09, así que
# su disponibilidad se simula como el cierre de ese sprint. Se supone que datos y material llegan con
# ella: si no, el inicio real se atrasa y se registra. «python3 montecarlo.py sin» simula A13 después
# de A09, para comparar.
T15 = pathlib.Path(rutas.T15).read_text(encoding="utf-8")
MODO = sys.argv[1] if len(sys.argv) > 1 else "acuerdo"
assert MODO in ("acuerdo", "sin"), MODO
tres = {m.group(1): tuple(int(x) for x in m.groups()[1:4])
        for m in re.finditer(r"^(A\d\d) & (\d+) & (\d+) & (\d+) & \d+ & [\d,]+ \\\\", T15, re.M)}
malla = {}
for m in re.finditer(r"^(A\d\d) & .*? & ([A\d, ]+|Ninguna) & (\d+) & (\d+) & (\d+) & (\d+) & (\d+) & (\d+) & (\d+) & (Sí|No) \\\\", T15, re.M):
    pre = [] if m.group(2) == "Ninguna" else [p.strip() for p in m.group(2).split(",")]
    malla[m.group(1)] = dict(pre=pre, dur=int(m.group(3)), es=int(m.group(4)), critica=m.group(10) == "Sí")
assert len(malla) == 25 and len(tres) == 18, (len(malla), len(tres))

N, rng = 10_000, np.random.default_rng(2026)
def dur(a):
    if a in tres:
        lo, mo, hi = tres[a]
        al = 1 + 4 * (mo - lo) / (hi - lo); be = 1 + 4 * (hi - mo) / (hi - lo)
        return lo + rng.beta(al, be, N) * (hi - lo)
    return np.full(N, float(malla[a]["dur"]))
D = {a: dur(a) for a in malla}
EF, S = {}, {}
def fin(a, inicio):
    S[a] = inicio; EF[a] = inicio + D[a]; return EF[a]
mx = np.maximum
fin("A01", np.zeros(N))
for a in ["A02", "A03", "A04"]: fin(a, EF["A01"])
fin("A05", EF["A02"]); fin("A06", EF["A02"]); fin("A07", EF["A05"])
fin("A08", mx(EF["A05"], EF["A07"])); fin("A09", EF["A07"])
fin("A10", mx(EF["A04"], EF["A07"])); fin("A11", mx(EF["A03"], EF["A07"]))
fin("A12", mx.reduce([EF["A08"], EF["A09"], EF["A10"], EF["A11"]]))
entrenamiento = S["A09"] + D["A09"] * 7 / 8       # cierre del sprint 7: versión congelada en PREPROD
fin("A13", mx(EF["A06"], entrenamiento if MODO == "acuerdo" else EF["A09"]))
fin_a14 = mx(240, EF["A12"])                      # reserva A14: hasta el día 240
fin("A15", mx(fin_a14, EF["A13"]))                # H6: inicio de la marcha blanca 1
fin("A16", fin_a14); fin("A17", fin_a14)
fin("A18", mx.reduce([EF["A06"], EF["A11"], fin_a14]))
fin("A19", mx(EF["A15"], EF["A16"])); fin("A20", EF["A17"]); fin("A21", EF["A19"]); fin("A22", EF["A20"])
fin("A24", mx.reduce([np.full(N, 360.0), EF["A22"], EF["A21"]]))   # reserva A23 y H11
fin("A25", mx(EF["A24"], EF["A18"]))

hitos = [("H1", EF["A02"], 40), ("H2", EF["A05"], 80), ("H3", EF["A07"], 120), ("H4", EF["A09"], 200),
         ("H5", EF["A12"], 240), ("H6", S["A15"], 240), ("H8", EF["A17"], 280), ("H7", EF["A19"], 320),
         ("H9", EF["A20"], 340), ("H10", EF["A22"], 360), ("H11", S["A24"], 360), ("H12", EF["A25"], 420)]
res = {"corridas": N, "semilla": 2026, "modo_A13": MODO, "hitos": {h: round(float((v <= lim).mean()) * 100, 1) for h, v, lim in hitos}}
res["sin_reserva"] = {"A12 en el día 226": round(float((EF["A12"] <= 226).mean()) * 100, 1),
                      "A22 en el día 350": round(float((EF["A22"] <= 350).mean()) * 100, 1)}
res["percentiles_fin_A12"] = {p: round(float(np.percentile(EF["A12"], p)), 1) for p in (50, 80, 95)}
res["percentiles_inicio_A15"] = {p: round(float(np.percentile(S["A15"], p)), 1) for p in (50, 80, 95)}
pred = np.argmax(np.vstack([EF["A08"], EF["A09"], EF["A10"], EF["A11"]]), axis=0)
res["define_inicio_A12"] = {a: round(float((pred == i).mean()) * 100, 1) for i, a in enumerate(["A08", "A09", "A10", "A11"])}
res["A13_retrasa_marcha_blanca"] = round(float((EF["A13"] > fin_a14).mean()) * 100, 1)
res["A13_empieza_despues_del_dia_182"] = round(float((S["A13"] > 182).mean()) * 100, 1)
res["percentiles_inicio_A13"] = {p: round(float(np.percentile(S["A13"], p)), 1) for p in (50, 80, 95)}
res["holgura_A13_a_marcha_blanca"] = {p: round(float(np.percentile(fin_a14 - EF["A13"], p)), 1) for p in (5, 50)}
res["A18_define_H12"] = round(float((EF["A18"] > EF["A24"]).mean()) * 100, 1)
res["ambas_marchas_blancas_a_tiempo"] = round(float(((S["A15"] <= 240) & (S["A24"] <= 360)).mean()) * 100, 1)
pathlib.Path(__file__).with_name("montecarlo.json" if MODO == "acuerdo" else "montecarlo-sin-adelanto.json").write_text(json.dumps(res, ensure_ascii=False, indent=2))
print(json.dumps(res, ensure_ascii=False, indent=2))
