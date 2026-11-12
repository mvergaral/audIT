#!/usr/bin/env python3
"""Calendario mensual de compras y contrataciones de D4 (tarea 4.6), meses 1 a 56, en pesos netos.

Usa los mismos datos de presupuesto_41.py y nube_42.py. Uso: python3 calendario_46.py > calendario_46.out
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import presupuesto_41 as p41  # noqa: E402
import nube_42 as n42  # noqa: E402

MESES = range(1, 57)
col = {k: {m: 0.0 for m in MESES} for k in
       ["inversion", "azure", "conectividad", "soporte", "otros", "mandante"]}

# inversión de audIT y unidades de prueba
for lineas, es_prueba in ((p41.M, False), (p41.PRUEBA, True)):
    for g, k, q, mes, nota in lineas:
        precio, mon = p41.P[k][2], p41.P[k][3]
        if precio is None:
            continue
        destino = "inversion" if (es_prueba or k in p41.AUDIT) else "mandante"
        col[destino][mes] += precio * p41.TC[mon] * q

# Azure por ambiente y meses activos, más herramientas, datos y Entra ID (D4-148)
for m in MESES:
    col["azure"][m] += n42.azure_mes(m) * n42.TC

# conectividad
for m in MESES:
    eq = n42.equipos_activos(m)
    col["conectividad"][m] += eq * n42.IRIDIUM_MES * n42.TC + eq * 3000
    if m >= 4:
        col["conectividad"][m] += 8 * n42.ENTEL_13GB + 1000 * n42.TC
act = {6: 10, 7: 60, 8: 60, 9: 52, 24: 8, 36: 7, 48: 7}
for m, n in act.items():
    col["conectividad"][m] += n * n42.IRIDIUM_ACT * n42.TC

# soporte y mantención, baterías, disposición y asesoría legal (mantencion_contingencia.py)
valor_hw = sum(col["inversion"].values()) - sum(
    p41.P[k][2] * p41.TC[p41.P[k][3]] * q for _, k, q, _, _ in p41.PRUEBA) + sum(col["mandante"].values())
for m in range(13, 57):
    col["soporte"][m] += valor_hw * 0.01
col["otros"][36] += (4 * 300 + 2 * 600 + 2 * 1447.99) * 900
col["otros"][56] += 1_000_000
col["otros"][3] += 3_000_000


def fmt(x):
    return f"{x:,.0f}".replace(",", ".")


if __name__ == "__main__":
    print("| Mes | Inversión audIT | Azure | Conectividad | Soporte y mantención | Otros | Total audIT | Acumulado audIT | Compras del mandante (informativo) |")
    print("|---|---|---|---|---|---|---|---|---|")
    acum = 0
    tot = {k: 0 for k in col}
    for m in MESES:
        audit = sum(col[k][m] for k in ["inversion", "azure", "conectividad", "soporte", "otros"])
        acum += audit
        for k in col:
            tot[k] += col[k][m]
        print(f"| {m} | {fmt(col['inversion'][m])} | {fmt(col['azure'][m])} | {fmt(col['conectividad'][m])} | "
              f"{fmt(col['soporte'][m])} | {fmt(col['otros'][m])} | {fmt(audit)} | {fmt(acum)} | {fmt(col['mandante'][m])} |")
    t_audit = sum(round(tot[k]) for k in ["inversion", "azure", "conectividad", "soporte", "otros"])
    print(f"| Total | {fmt(tot['inversion'])} | {fmt(tot['azure'])} | {fmt(tot['conectividad'])} | {fmt(tot['soporte'])} | "
          f"{fmt(tot['otros'])} | {fmt(t_audit)} | | {fmt(tot['mandante'])} |")
