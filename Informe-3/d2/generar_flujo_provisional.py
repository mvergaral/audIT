"""Genera el flujo provisional para revisión de D1 con los insumos publicados."""

import csv
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
MARGEN = 0.185
TASA_BANCO = 0.009
TASA_LINEA = 0.03
TOPE_LINEA = 50_000_000
TASA_VAN = 0.8 * TASA_BANCO + 0.2 * (1.2 ** (1 / 12) - 1)
COMISION_GARANTIA = 0.05 * 0.015 * 2
PERSONAL_M1_M20 = (
    [78_400_000] * 2 + [129_600_000] * 3 + [160_320_000] * 4
    + [175_680_000] * 3 + [196_160_000] * 5 + [160_320_000] + [139_840_000] * 2
)
CALIDAD = {
    4: 3_000_000, 5: 4_750_000, 6: 4_000_000, 7: 2_250_000,
    8: 500_000, 9: 500_000, 10: 2_500_000, 11: 6_875_000,
    12: 4_875_000, 17: 2_250_000, 18: 4_000_000, 19: 1_750_000,
    29: 2_000_000, 30: 3_500_000, 41: 2_000_000, 42: 3_500_000,
    53: 2_000_000, 54: 3_500_000,
}


def read_csv(name):
    with (HERE / name).open(encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream))


def calcular_van(flows, rate):
    return sum(value / (1 + rate) ** month for month, value in enumerate(flows, 1))


def generar():
    source = read_csv("AUD-17_EGRESOS_D4_2026-11-12.csv")
    events = read_csv("AUD-18_CALENDARIO_INGRESOS_E25.csv")
    admin = {month: 0 for month in range(1, 57)}
    for entry in read_csv("AUD-16_CALENDARIO_ADMIN_D1.csv"):
        admin[int(entry["mes_caja"])] += int(entry["importe_clp_neto"])
    hits = {
        int(e["mes_hito_o_servicio"]): float(e["porcentaje_valor_implementacion"]) / 100
        for e in events if e["fase"] == "implementacion"
    }
    assert len(hits) == 12 and abs(sum(hits.values()) - 1) < 1e-12
    assert sum(admin.values()) == 85_400_000 and sum(CALIDAD.values()) == 53_750_000
    rows = []
    for entry, rrhh in zip(source, PERSONAL_M1_M20 + [85_120_000] * 36, strict=True):
        month = int(entry["mes"])
        d4 = int(entry["total_audit_segun_d4_clp_neto"]) - (month == 56)
        licenses = int(entry["gitlab_licencia_referencial_clp_neto"]) + int(
            entry["sonarqube_licencia_anualidad_supuesta_clp_neto"]
        )
        rows.append(dict(
            mes=month, periodo=entry["periodo"], d4=d4, licencias=licenses,
            calidad=CALIDAD.get(month, 0), administracion=admin[month],
            cierre=int(entry["salida_cierre_m56_propuesta_d1_clp"]),
            rrhh_escenario=rrhh, mandante=int(entry["compras_mandante_informativas_clp_neto"]),
        ))
    assert [row["mes"] for row in rows] == list(range(1, 57))
    assert sum(row["d4"] for row in rows) == 1_526_997_751
    assert sum(row["mandante"] for row in rows) == 225_384_199
    cost_fields = ("d4", "licencias", "calidad", "administracion", "cierre", "rrhh_escenario")
    for row in rows:
        row["egresos"] = sum(row[field] for field in cost_fields)
    impl_cost = sum(r["egresos"] for r in rows[:20])
    op_cost = sum(r["egresos"] for r in rows[20:])
    impl_price = impl_cost / (1 - MARGEN - COMISION_GARANTIA)
    monthly_price = op_cost / (1 - MARGEN) / 36
    rows[20]["egresos"] += impl_price * COMISION_GARANTIA

    def forecast(initial, h5_delay=False, reserve_month=None):
        cash = bank = line = cumulative_cost = cumulative_billing = 0
        result = []
        for row in rows:
            month = row["mes"]
            billing = hits.get(month, 0) * impl_price + (monthly_price if month >= 21 else 0)
            receipt = hits.get(month, 0) * impl_price + (monthly_price if month >= 22 else 0)
            if h5_delay:
                receipt += (int(month == 13) - int(month == 12)) * hits[12] * impl_price
            cost = row["egresos"] + (152_699_775 if month == reserve_month else 0)
            project = receipt - cost
            bank_interest, line_interest = bank * TASA_BANCO, line * TASA_LINEA
            debt_draw = initial * 0.8 if month == 1 else 0
            equity = initial * 0.2 if month == 1 else 0
            bank += debt_draw
            before_line = cash + project + debt_draw + equity - bank_interest - line_interest
            draw = max(0, min(TOPE_LINEA - line, -before_line))
            line_payment = min(line, max(0, before_line))
            line += draw - line_payment
            before_amortization = before_line + draw - line_payment
            bank_payment = min(bank, max(0, before_amortization)) if month >= 21 else 0
            bank -= bank_payment
            new_cash = before_amortization - bank_payment
            cumulative_cost += cost + bank_interest + line_interest
            cumulative_billing += billing
            result.append({
                **row, "egresos": cost, "facturacion": billing, "cobros": receipt,
                "fila_a": project, "aporte_socios": equity, "giro_banco": debt_draw,
                "interes_banco": bank_interest, "interes_linea": line_interest,
                "giro_linea": draw, "pago_linea": line_payment, "pago_banco": bank_payment,
                "fila_c": new_cash - cash, "caja_acumulada": new_cash, "saldo_banco": bank,
                "saldo_linea": line, "costos_acumulados_con_interes": cumulative_cost,
                "facturacion_acumulada": cumulative_billing,
            })
            cash = new_cash
        return result

    def funded(**scenario):
        def covers(amount):
            return min(row["caja_acumulada"] for row in forecast(amount, **scenario)) >= -0.001

        low, high = 0, 1_000_000
        while not covers(high):
            high *= 2
            if high > 100_000_000_000:
                raise ValueError("No se encontró financiamiento viable en el rango evaluado")
        while low < high:
            middle = (low + high) // 2
            if covers(middle):
                high = middle
            else:
                low = middle + 1
        return high, forecast(high, **scenario)

    initial, base = funded()
    peak = max(base, key=lambda r: (round(r["saldo_linea"], 2), -r["caja_acumulada"]))
    reserve_month = peak["mes"]
    h5_initial, _ = funded(h5_delay=True)
    reserve_initial, _ = funded(reserve_month=reserve_month)
    flows = [row["fila_a"] for row in base]
    assert len(flows) == 56 and abs(sum(r["fila_c"] for r in base) - base[-1]["caja_acumulada"]) < 0.01
    assert abs(sum(r["facturacion"] - r["cobros"] for r in base) - monthly_price) < 0.01
    assert max(r["saldo_linea"] for r in base) <= TOPE_LINEA + 0.001
    assert abs(sum(row["egresos"] - row["rrhh_escenario"] for row in base)
               - impl_price * COMISION_GARANTIA - 1_717_980_351) < 0.01
    assert abs((sum(r["facturacion"] for r in base) - sum(r["egresos"] for r in base))
               / sum(r["facturacion"] for r in base) - MARGEN) < 1e-12
    result = dict(
        horizonte=56, m0=0, tasa_mensual=TASA_VAN, precio_impl_escenario=impl_price,
        mensualidad_escenario=monthly_price, cobro_m57=monthly_price,
        valor_en_m56_del_cobro_m57=monthly_price / (1 + TASA_VAN),
        van_referencial=calcular_van(flows, TASA_VAN),
        van_referencial_con_m57=calcular_van(flows + [monthly_price], TASA_VAN),
        capital_inicial_escenario=initial, capital_inicial_h5_m13=h5_initial,
        mes_estres_reserva=reserve_month, capital_inicial_estres_reserva=reserve_initial,
        caja_m56=base[-1]["caja_acumulada"], saldo_banco_m56=base[-1]["saldo_banco"],
        saldo_linea_m56=base[-1]["saldo_linea"], tope_linea=TOPE_LINEA,
    )
    for filename, data in [
        ("AUD-22_FILA_A_PROVISIONAL.csv", [{k:r[k] for k in ("mes","periodo","facturacion","cobros","egresos","fila_a")} for r in base]),
        ("AUD-17_FLUJO_INTEGRADO_PROVISIONAL.csv", base),
    ]:
        with (HERE / filename).open("w", encoding="utf-8", newline="") as stream:
            writer = csv.DictWriter(stream, fieldnames=data[0].keys(), lineterminator="\n")
            writer.writeheader()
            writer.writerows(data)
    (HERE / "AUD-22_PARAMETROS_PROVISIONALES.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    generar()
