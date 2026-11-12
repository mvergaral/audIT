#!/usr/bin/env python3
"""Costo mensual de Azure de la tarea 4.2 (AUD-33), con dimensionamiento de referencia.

Precios: API pública de precios minoristas de Azure, pago por uso, consultados el 2026-11-11
(azure_precios/*.json). Tamaños: referencia propia declarada (D4-144), ajustable tras la prueba de
carga de 1,5 veces el peak antes del H5 (S4 §4.1, RT-09.06). Región de recuperación en espera tibia.
Incluye la conectividad que paga audIT (D4-143 b y D4-144).
Uso: python3 nube_42.py > nube_42.out
"""
H = 730  # horas por mes
TC = 900  # USD a pesos, Formulario E-24

# Precios unitarios en USD (fuente: archivo de la API y medidor)
P = {
    "aks_sla": 0.10,          # aks_cc: Standard Uptime SLA, por hora
    "d2_cc": 0.158, "d4_cc": 0.316,   # vm_cc: D2ds v5 y D4ds v5, por hora
    "d2_bs": 0.18, "d4_bs": 0.36,     # vm_bs
    "apim_prem": 3.829,       # apim_cc: Premium Unit, por hora
    "apim_dev": 0.0658,       # apim_cc: Developer Unit, por hora
    "afd_base": 330.0,        # afd: Premium Base Fees, por mes
    "afd_gb": 0.0825,         # afd: Premium Data Transfer Out, primer tramo
    "iot_s1": 34.925,         # iothub_cc: S1 Unit, por mes
    "eh_prem_cc": 1.434719, "eh_prem_bs": 2.055,   # eh_cc / eh_bs: Premium Processing Unit, por hora
    "eh_std_tu": 0.04191,     # eh_cc: Standard Throughput Unit, por hora
    "pg_gp_vcore_cc": 0.1246, "pg_gp_vcore_bs": 0.12,   # pg_cc / pg_bs: Ddsv5 por vCore y hora
    "pg_b1ms": 0.0238, "pg_b2ms": 0.1904,               # pg_cc: Burstable, por hora
    "pg_gb_cc": 0.161, "pg_gb_bs": 0.2185,              # Storage Data Stored, por GB y mes
    "redis_b0": 0.0224, "redis_b3": 0.091,              # redis_cc: Managed Redis Balanced, por hora
    "fw_prem": 1.75, "fw_gb": 0.016,                    # fw_cc / fw_bs: Premium Deployment y Data Processed
    "vpn_gw1az": 0.21,        # vpn_cc: VpnGw1AZ, por hora (incluye 10 túneles S2S)
    "er_gw1az": 0.361,        # er_cc: ErGw1AZ Gateway, por hora
    "er_100_std": 100.0, "er_gb": 0.1,                  # er_circ: Standard Metered 100 Mbps y salida
    "bastion_basic": 0.19,    # bastion_cc: Basic Gateway, por hora
    "kv_hsm_key": 1.0, "kv_ops_10k": 0.03,              # kv_cc / kv_bs
    "blob_zrs_cc": 0.0322, "blob_lrs_bs": 0.0326,       # blob_cc / blob_bs: Hot, por GB y mes
    "la_gb": 3.2131, "la_ret_gb": 0.1397,               # la_cc: ingesta sobre 5 GB y retención
    "salida_gb": 0.087,       # bw_cc: salida a Internet, usado como referencia para la réplica entre regiones
}

# (ambiente, servicio, supuesto de tamaño, costo mensual en USD)
L = []
def a(amb, serv, sup, usd):
    L.append((amb, serv, sup, usd))

# ---------------------------------------------------------------- Producción, Chile Central
a("PROD", "AKS, plano de control", "Nivel Standard con SLA de disponibilidad", P["aks_sla"] * H)
a("PROD", "AKS, nodos", "3 D2ds v5 de sistema y 3 D4ds v5 de aplicación, uno por zona", (3 * P["d2_cc"] + 3 * P["d4_cc"]) * H)
a("PROD", "API Management", "Premium, 2 unidades en dos zonas (D4-144, corrige la fila 33 del T-11)", 2 * P["apim_prem"] * H)
a("PROD", "Front Door", "Premium, 100 GB de salida al mes", P["afd_base"] + 100 * P["afd_gb"])
a("PROD", "IoT Hub", "S1, 2 unidades (T-11, fila 34)", 2 * P["iot_s1"])
a("PROD", "Event Hubs", "Premium, 1 unidad de procesamiento (T-11, fila 35)", P["eh_prem_cc"] * H)
a("PROD", "PostgreSQL transaccional", "4 vCore de propósito general, alta disponibilidad entre zonas, 256 GB por nodo", (2 * 4 * P["pg_gp_vcore_cc"]) * H + 2 * 256 * P["pg_gb_cc"])
a("PROD", "PostgreSQL de series (TimescaleDB)", "2 vCore de propósito general, 128 GB", (2 * P["pg_gp_vcore_cc"]) * H + 128 * P["pg_gb_cc"])
a("PROD", "Azure Managed Redis", "Balanced B3", P["redis_b3"] * H)
a("PROD", "Azure Firewall", "Premium, 300 GB procesados al mes", P["fw_prem"] * H + 300 * P["fw_gb"])
a("PROD", "Puerta VPN", "VpnGw1AZ, túneles de los 4 terminales y respaldo de San Bernardo", P["vpn_gw1az"] * H)
a("PROD", "Puerta ExpressRoute", "ErGw1AZ", P["er_gw1az"] * H)
a("PROD", "Circuito ExpressRoute, lado Microsoft", "Standard medido 100 Mbit/s, 50 GB de salida", P["er_100_std"] + 50 * P["er_gb"])
a("PROD", "Azure Bastion", "Basic", P["bastion_basic"] * H)
a("PROD", "Key Vault", "Premium, 20 claves HSM y 1 millón de operaciones", 20 * P["kv_hsm_key"] + 100 * P["kv_ops_10k"])
a("PROD", "Almacenamiento de objetos y Data Lake", "500 GB Hot ZRS en promedio", 500 * P["blob_zrs_cc"])
a("PROD", "Log Analytics", "3 GB al día, 12 meses en línea", (90 - 5) * P["la_gb"] + 990 * P["la_ret_gb"])
a("PROD", "Réplica hacia Brazil South", "50 GB al mes de tráfico entre regiones", 50 * P["salida_gb"])
# ---------------------------------------------------------------- Recuperación, Brazil South, espera tibia
a("DR", "Event Hubs, réplica", "Premium, 1 unidad de procesamiento", P["eh_prem_bs"] * H)
a("DR", "PostgreSQL transaccional, réplica", "2 vCore, 256 GB", (2 * P["pg_gp_vcore_bs"]) * H + 256 * P["pg_gb_bs"])
a("DR", "PostgreSQL de series, réplica", "2 vCore, 128 GB", (2 * P["pg_gp_vcore_bs"]) * H + 128 * P["pg_gb_bs"])
a("DR", "Azure Firewall", "Premium, siempre activo", P["fw_prem"] * H + 10 * P["fw_gb"])
a("DR", "Key Vault", "Premium, 20 claves HSM", 20 * P["kv_hsm_key"] + 10 * P["kv_ops_10k"])
a("DR", "Almacenamiento replicado", "500 GB Hot LRS", 500 * P["blob_lrs_bs"])
a("DR", "AKS en las pruebas de conmutación", "2 pruebas al año de 8 horas con el tamaño de producción", 2 * 8 * (P["aks_sla"] + 3 * P["d2_bs"] + 3 * P["d4_bs"]) / 12)
# ---------------------------------------------------------------- Preproducción
a("PREPROD", "AKS, nodos", "3 D2ds v5, nivel gratuito", 3 * P["d2_cc"] * H)
a("PREPROD", "API Management", "Developer, 1 unidad", P["apim_dev"] * H)
a("PREPROD", "IoT Hub", "S1, 1 unidad", P["iot_s1"])
a("PREPROD", "Event Hubs", "Standard, 2 unidades de capacidad", 2 * P["eh_std_tu"] * H)
a("PREPROD", "PostgreSQL", "2 vCore de propósito general, 128 GB, más series en B2ms con 64 GB", (2 * P["pg_gp_vcore_cc"]) * H + 128 * P["pg_gb_cc"] + P["pg_b2ms"] * H + 64 * P["pg_gb_cc"])
a("PREPROD", "Azure Managed Redis", "Balanced B0", P["redis_b0"] * H)
a("PREPROD", "Log Analytics", "1 GB al día", 30 * P["la_gb"])
a("PREPROD", "Prueba de carga antes del H5", "Un mes con el tamaño de producción (AKS y PostgreSQL), repartido en 51 meses", ((3 * P["d2_cc"] + 3 * P["d4_cc"]) + 2 * 4 * P["pg_gp_vcore_cc"]) * H / 51)
# ---------------------------------------------------------------- QA
a("QA", "AKS, nodos", "2 D2ds v5, nivel gratuito", 2 * P["d2_cc"] * H)
a("QA", "API Management", "Developer, 1 unidad", P["apim_dev"] * H)
a("QA", "IoT Hub", "S1, 1 unidad", P["iot_s1"])
a("QA", "Event Hubs", "Standard, 1 unidad de capacidad", P["eh_std_tu"] * H)
a("QA", "PostgreSQL", "B2ms, 64 GB", P["pg_b2ms"] * H + 64 * P["pg_gb_cc"])
a("QA", "Azure Managed Redis", "Balanced B0", P["redis_b0"] * H)
a("QA", "Log Analytics", "0,5 GB al día", 15 * P["la_gb"])
# ---------------------------------------------------------------- DEV
a("DEV", "AKS, nodos", "1 D2ds v5, nivel gratuito", P["d2_cc"] * H)
a("DEV", "API Management", "Developer, 1 unidad", P["apim_dev"] * H)
a("DEV", "Event Hubs", "Standard, 1 unidad de capacidad", P["eh_std_tu"] * H)
a("DEV", "PostgreSQL", "B1ms, 32 GB", P["pg_b1ms"] * H + 32 * P["pg_gb_cc"])
a("DEV", "Azure Managed Redis", "Balanced B0", P["redis_b0"] * H)
a("DEV", "Log Analytics", "0,3 GB al día", 9 * P["la_gb"])

# Meses activos de cada ambiente (contrato de 56 meses, mes 1 = febrero de 2027)
MESES = {"DEV": (4, 56), "QA": (4, 56), "PREPROD": (6, 56), "PROD": (6, 56), "DR": (12, 56)}


# ---------------------------------------------------------------- Conectividad que paga audIT
IRIDIUM_MES, IRIDIUM_ACT = 36.75, 31.50   # Ground Control GC-SBD-25KB-1, USD, contrato de 12 meses
ENTEL_13GB = 9990 / 1.19                  # Entel Plan 13 GB, $9.990 al mes con IVA, neto
# Equipos a bordo activos por mes, según el montaje del S4 §4.2.2 (supuesto de reparto):
# piloto de 10 en el mes 6, flota propia y terceros hasta 182 en el mes 9, crecimiento en los meses 24, 36 y 48.
def equipos_activos(m):
    base = {6: 10, 7: 70, 8: 130}.get(m, 182 if m >= 9 else 0)
    return base + (8 if m >= 24 else 0) + (7 if m >= 36 else 0) + (7 if m >= 48 else 0)


def conectividad(total_azure):
    iri = sum(equipos_activos(m) for m in range(1, 57)) * IRIDIUM_MES * TC
    act = (182 + 22) * IRIDIUM_ACT * TC
    sim = 8 * ENTEL_13GB * (56 - 4 + 1)
    print("\n| Conectividad | Supuesto | Pesos al mes en régimen | Total neto 56 meses |\n|---|---|---|---|")
    print(f"| Tiempo de aire Iridium | Plan de 25 KB a USD 36,75 por equipo activo, 182 desde el mes 9 más el crecimiento | {fmt(182 * IRIDIUM_MES * TC)} | {fmt(iri)} |")
    print(f"| Activación Iridium | USD 31,50 por equipo, 204 equipos | | {fmt(act)} |")
    print(f"| SIM 5G de los terminales | 8 líneas, referencia Entel 13 GB a $9.990 con IVA, meses 4 a 56 | {fmt(8 * ENTEL_13GB)} | {fmt(sim)} |")
    lte = sum(equipos_activos(m) for m in range(1, 57)) * 3000
    er = 1000 * TC * (56 - 4 + 1)
    print(f"| Planes LTE de los equipos a bordo | Estimado $3.000 netos por línea activa al mes (D4-145) | {fmt(182 * 3000)} | {fmt(lte)} |")
    print(f"| Circuito del proveedor de ExpressRoute | Estimado USD 1.000 al mes, meses 4 a 56 (D4-145) | {fmt(1000 * TC)} | {fmt(er)} |")
    print(f"| Total conectividad | | | {fmt(iri + act + sim + lte + er)} |")
    print(f"\nTOTAL NUBE Y CONECTIVIDAD: {fmt(total_azure + iri + act + sim + lte + er)}")


def fmt(x, d=0):
    return f"{x:,.{d}f}".replace(",", "X").replace(".", ",").replace("X", ".")


if __name__ == "__main__":
    print("| Ambiente | Servicio | Supuesto de tamaño | USD al mes | Pesos al mes |\n|---|---|---|---|---|")
    tot_amb = {}
    for amb, serv, sup, usd in L:
        tot_amb[amb] = tot_amb.get(amb, 0) + usd
        print(f"| {amb} | {serv} | {sup} | {fmt(usd, 2)} | {fmt(usd * TC)} |")
    print("\n| Ambiente | Meses | USD al mes | Pesos al mes | Meses activos | Total neto en pesos |\n|---|---|---|---|---|---|")
    total = 0
    for amb, usd in tot_amb.items():
        m0, m1 = MESES[amb]
        n = m1 - m0 + 1
        total += usd * TC * n
        print(f"| {amb} | {m0} a {m1} | {fmt(usd, 2)} | {fmt(usd * TC)} | {n} | {fmt(usd * TC * n)} |")
    print(f"| Total 56 meses | | | | | {fmt(total)} |")
    apim = 2 * P["apim_prem"] * H
    print(f"\nAPIM Premium: {fmt(apim, 2)} USD al mes, {apim / tot_amb['PROD']:.0%} de producción")
    conectividad(total)
