#!/usr/bin/env python3
"""Tareas 4.3 (soporte y mantención) y 4.7 (contingencia) con el método simplificado de D4-145.

Toma los totales de presupuesto_41.out y nube_42.out. Tipo de cambio del E-24: USD $900.
Uso: python3 mantencion_contingencia.py > mantencion_contingencia.out
"""
import os
import re

AQUI = os.path.dirname(os.path.abspath(__file__))
TC = 900


def total(archivo, rotulo):
    t = open(os.path.join(AQUI, archivo), encoding="utf-8").read()
    return int(re.search(rotulo + r": ([\d.]+)", t).group(1).replace(".", ""))


def fmt(x):
    return f"{x:,.0f}".replace(",", ".")


inv = total("presupuesto_41.out", "TOTAL AUDIT_INVERSION")
prueba = total("presupuesto_41.out", "TOTAL AUDIT_PRUEBA")
mand = total("presupuesto_41.out", "TOTAL MANDANTE_INFORMATIVA")
nube = total("nube_42.out", "TOTAL NUBE Y CONECTIVIDAD")

# ---------------------------------------------------------------- 4.3
valor_hw = inv + mand                      # todo el hardware, del mandante y de audIT
meses_soporte = 56 - 13 + 1                # desde el mes 13, tras el primer año de garantía
soporte = valor_hw * 0.12 / 12 * meses_soporte
baterias = [("Batería de UPS SRT1000XLI (estimado USD 300)", 4, 300 * TC),
            ("Batería interna de UPS SRT3000RMXLI (estimado USD 600)", 2, 600 * TC),
            ("Paquete de baterías SRT96RMBP (USD 1.447,99, CDW)", 2, 1447.99 * TC)]
bat = sum(q * p for _, q, p in baterias)
dispo = 1_000_000                          # borrado seguro y disposición final, estimado
mant = soporte + bat + dispo

print("## 4.3 Soporte y mantención")
print("| Partida | Supuesto | Mes | Total neto en pesos |\n|---|---|---|---|")
print(f"| Soporte del fabricante y mantención preventiva y correctiva | 12 % anual de {fmt(valor_hw)} de hardware, {meses_soporte} meses | 13 a 56, mensual de {fmt(valor_hw * 0.01)} | {fmt(soporte)} |")
for n, q, p in baterias:
    print(f"| {n} | {q} unidades | 36 | {fmt(q * p)} |")
print(f"| Borrado seguro y disposición final (estimado) | Gestor autorizado y certificados (FEP02, RT-08.17 y RT-08.18) | 56 | {fmt(dispo)} |")
print(f"| Total 4.3 | | | {fmt(mant)} |")
print(f"TOTAL 4.3: {fmt(mant)}\n")

# ---------------------------------------------------------------- 4.7
legal_r24 = 3_000_000                      # asesoría legal de las cláusulas tipo, estimado
base = inv + prueba + nube + mant + legal_r24
reserva = base * 0.10
print("## 4.7 Contingencia")
print("| Partida | Supuesto | Total neto en pesos |\n|---|---|---|")
print(f"| Respuesta a R-24: asesoría legal de las cláusulas contractuales tipo antes del H2 (estimado) | Mes 3 | {fmt(legal_r24)} |")
print(f"| Reserva de contingencia | 10 % de los costos de D4 ({fmt(base)}) | {fmt(reserva)} |")
print(f"| Total 4.7 | | {fmt(legal_r24 + reserva)} |")
print(f"TOTAL 4.7: {fmt(legal_r24 + reserva)}\n")

print("## Resumen de costos de D4 para audIT")
print("| Concepto | Total neto en pesos |\n|---|---|")
for n, v in [("Inversión en infraestructura on-premise (4.1)", inv), ("Unidades de prueba (4.1)", prueba),
             ("Nube y conectividad (4.2)", nube), ("Soporte y mantención (4.3)", mant),
             ("Respuesta a R-24 (4.7)", legal_r24), ("Reserva de contingencia (4.7)", reserva)]:
    print(f"| {n} | {fmt(v)} |")
print(f"| Total costos de D4 en el flujo de audIT | {fmt(base + reserva)} |")
print(f"| Hoja informativa del mandante, fuera del flujo (4.1) | {fmt(mand)} |")
