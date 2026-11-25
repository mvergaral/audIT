"""Simulación Monte Carlo del cronograma sobre la malla conciliada con la entrega 3.2 (D4-161).

La red es la de D2 en subdocumentos/07-plan-trabajo/graficos/conciliacion-3.2/red-calculada.json:
122 nodos con duración única, precedencias FS y SS con desfase, liberación y límite. El S7 deja
pendientes las estimaciones de tres puntos hasta validarlas con los ejecutores en H1, así que esta
corrida usa una regla declarada y provisional:

  * Duración fija: hitos, revisiones contractuales de 10 días hábiles (R-H*, Art. 18.3) y
    ventanas cuya liberación y límite fijan la duración (piloto, lotes, marchas blancas, operación).
  * Reservas A14 y A23: absorben el atraso hasta el día 240 y el 360, como en la red anterior.
  * Resto del trabajo: Beta-PERT con optimista 0,85, más probable 1 y pesimista 1,4 veces la
    duración de la malla.

Uso: python3 montecarlo32.py
"""
import json
import pathlib
import sys

import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "graficos-v2" / "fuente"))
import rutas  # noqa: E402

RED = pathlib.Path(rutas.REPO) / "recursos/Formato-Oferta-audIT/subdocumentos/07-plan-trabajo/graficos/conciliacion-3.2/red-calculada.json"
NODOS = json.loads(RED.read_text(encoding="utf-8"))
OPT, PES = 0.85, 1.4
N, rng = 10_000, np.random.default_rng(2026)
RESERVAS = {"A14": 240.0, "A23": 360.0}


def fija(n):
    if n["duracion"] == 0 or n["id"].startswith("R-") or n["id"] in RESERVAS:
        return True
    return "liberacion" in n and "limite" in n and n["limite"] - n["liberacion"] == n["duracion"]


def duracion(n):
    d = float(n["duracion"])
    if fija(n):
        return np.full(N, d)
    lo, mo, hi = OPT * d, d, PES * d
    al, be = 1 + 4 * (mo - lo) / (hi - lo), 1 + 4 * (hi - mo) / (hi - lo)
    return lo + rng.beta(al, be, N) * (hi - lo)


def simular():
    ES, EF = {}, {}
    for n in NODOS:                      # la lista ya viene en orden topológico
        i = n["id"]
        ini = np.full(N, float(n.get("liberacion", 0)))
        for p in n["predecesoras"]:
            base = EF[p["id"]] if p["tipo"] == "FS" else ES[p["id"]]
            ini = np.maximum(ini, base + p["lag"])
        ES[i] = ini
        if i in RESERVAS:
            EF[i] = np.maximum(ini, RESERVAS[i])
        else:
            EF[i] = ini + duracion(n)
    return ES, EF


ES, EF = simular()
hitos = [n for n in NODOS if n["id"].startswith("H") and n["duracion"] == 0]
res = {"corridas": N, "semilla": 2026, "regla": f"Beta-PERT {OPT}/1/{PES}", "nodos": len(NODOS),
       "hitos": {n["id"]: round(float(np.mean(EF[n["id"]] <= n["limite"] + 1e-9)) * 100, 1) for n in hitos},
       "atraso_medio_dias": {n["id"]: round(float(np.mean(np.maximum(0, EF[n["id"]] - n["limite"]))), 1) for n in hitos}}
ambas = (EF["H6"] <= 240 + 1e-9) & (EF["H11"] <= 360 + 1e-9)
res["ambas_marchas_blancas"] = round(float(np.mean(ambas)) * 100, 1)
res["H12_p90"] = round(float(np.percentile(EF["H12"], 90)), 1)
# consumo de las reservas: cuánto del margen de A14 y A23 se usa
for r in RESERVAS:
    holgura = RESERVAS[r] - ES[r]
    res[f"{r}_probabilidad_agotada"] = round(float(np.mean(holgura < 0)) * 100, 1)
    res[f"{r}_holgura_mediana"] = round(float(np.median(holgura)), 1)
pathlib.Path(__file__).with_name("montecarlo32.json").write_text(json.dumps(res, ensure_ascii=False, indent=2) + "\n")
print(json.dumps(res, ensure_ascii=False, indent=1))
