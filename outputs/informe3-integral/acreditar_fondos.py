"""Dimensiona compromisos de fondos AUD-5/17/18/20 y separa caja mensual e intramensual."""

import csv
import json
from dataclasses import dataclass
from datetime import date, timedelta
from pathlib import Path

from reproducir import CUT, bank_fraction, bank_rate, debt_start, flux, h5, initial
from reproducir import inputs, irr, limit, npv, simulate, target, vat_rate


OUT = Path(__file__).resolve().parent / "cierre-liquidez"
START = date(2027, 2, 1)  # AUD-18
RECEIPT = date(2028, 1, 31)  # AUD-20, fecha de trabajo
RESERVE = inputs["B22"].value
REFILL = 400_000_000  # AUD-20, aprobado para modelación
FEE = 250_000  # AUD-20, ilustrativa
HOURS = {6: 576_000, 7: 608_000, 8: 432_000, 9: 400_000}
CALIBRATION = {month: inputs["B26"].value for month in (13, 14, 15)}


@dataclass(frozen=True)
class Stress:
    collection: int
    reserve: int = 0


def period(month):
    year, month_index = divmod(START.month - 1 + month - 1, 12)
    return date(START.year + year, month_index + 1, 1)


def contract_month(day):
    return (day.year - START.year) * 12 + day.month - START.month + 1


def costs(month, stress):
    if not stress.reserve:
        return 0, 0, 0, 0
    return (
        RESERVE if month == stress.reserve else 0,
        HOURS.get(month, 0),
        CALIBRATION.get(month, 0),
        FEE if month == 12 else 0,
    )


def model(stress, draws, repay_from=None):
    """Initial bank capital amortizes from M21. The bridge cannot be repaid before H5."""
    cash = bank = short_debt = prior_vat = 0.0
    rows = []
    for row in flux:
        month, _, _, _, invoice, receipt, net_cost = row[:7]
        moved = h5[5] * ((month == stress.collection) - (month == 12))
        receipt += moved
        vat_received = row[9] + moved * vat_rate
        vat_purchase = row[10] * inputs["B12"].value
        vat_payment = prior_vat * inputs["B12"].value
        prior_vat = row[12]
        reserve, hours, extra_vat, fee = costs(month, stress)
        opening = cash
        new_capital = draws.get(month, 0)
        credit = new_capital * bank_fraction
        equity = new_capital - credit
        interest = (bank + short_debt) * bank_rate
        payments = net_cost + vat_purchase + vat_payment + reserve + hours + extra_vat + fee + interest
        before_collections = opening + new_capital - payments
        cash = before_collections + receipt + vat_received
        if month != 1 and repay_from is not None:
            short_debt += credit
        else:
            bank += credit
        short_repaid = 0
        if repay_from is not None and month >= max(repay_from, stress.collection):
            short_repaid = min(short_debt, max(0, cash - target))
            short_debt -= short_repaid
            cash -= short_repaid
        bank_repaid = 0
        if month >= debt_start:
            bank_repaid = min(bank, max(0, cash))
            cash -= bank_repaid
            bank -= bank_repaid
        rows.append(dict(
            mes=month, periodo=period(month).isoformat(), caja_apertura=opening,
            factura_neta=invoice, cobro_neto=receipt, iva_cobrado=vat_received,
            egreso_neto=net_cost, iva_compra=vat_purchase, entero_iva=vat_payment,
            reserva_d4=reserve, compra_horas=hours, iva_calibracion=extra_vat,
            comision=fee, banco_abonado=credit, socios_abonado=equity,
            interes=interest, caja_antes_de_cobros=before_collections,
            repago_puente=short_repaid, principal_banco=bank_repaid,
            saldo_puente=short_debt, saldo_banco=bank,
            giro_linea=0, saldo_linea=0, caja_cierre=cash,
        ))
    return rows


def low(rows, field="caja_cierre", start=1, end=56):
    return min(rows[start - 1:end], key=lambda row: row[field])


def size(stress, draws, month, end=56, field="caja_cierre", floor=target, repay_from=None):
    """A multiple of CLP 5 keeps both 80/20 commitments whole in pesos."""
    left, right = 0, 400_000_000
    while left < right:
        middle = (left + right) // 2
        rows = model(stress, {**draws, month: middle * 5}, repay_from)
        if low(rows, field, month, end)[field] >= floor:
            right = middle
        else:
            left = middle + 1
    funded = {**draws, month: left * 5}
    assert low(model(stress, funded, repay_from), field, month, end)[field] >= floor
    if left:
        below = {**draws, month: (left - 1) * 5}
        assert low(model(stress, below, repay_from), field, month, end)[field] < floor
    return {key: value for key, value in funded.items() if value}


def stage(stress, base, repay_from):
    draws = dict(base)
    # Include the conditional preparation expense when testing the pre-H5 cash floor.
    if stress.reserve:
        draws = size(stress, draws, 9, 11, repay_from=repay_from)
    return size(stress, draws, 12, repay_from=repay_from)


def summary(rows, draws, stress):
    floor = low(rows)
    worst = low(rows, "caja_antes_de_cobros")
    h5_row = rows[stress.collection - 1]
    return dict(
        mes_cobro_h5=stress.collection, mes_reserva=stress.reserve or None,
        tramos_clp=draws, capital_total_clp=sum(draws.values()),
        banco_clp=sum(row["banco_abonado"] for row in rows),
        socios_clp=sum(row["socios_abonado"] for row in rows),
        caja_minima_clp=floor["caja_cierre"], mes_minimo=floor["mes"],
        caja_m9_clp=rows[8]["caja_cierre"], caja_m12_clp=rows[11]["caja_cierre"],
        caja_m13_clp=rows[12]["caja_cierre"], caja_m14_clp=rows[13]["caja_cierre"],
        peor_caja_antes_de_cobros_clp=min(worst["caja_antes_de_cobros"], floor["caja_cierre"]),
        mes_peor_orden=worst["mes"],
        intereses_clp=sum(row["interes"] for row in rows),
        comisiones_clp=sum(row["comision"] for row in rows),
        amortizacion_cobro_h5_clp=h5_row["repago_puente"],
        saldo_puente_tras_h5_clp=h5_row["saldo_puente"],
        pagos_puente_clp={row["mes"]: row["repago_puente"] for row in rows if row["repago_puente"]},
        amortizacion_banco_clp=sum(row["principal_banco"] for row in rows),
    )


def save_csv(path, rows):
    with path.open("w", newline="", encoding="utf-8-sig") as file:
        writer = csv.DictWriter(file, fieldnames=list(rows[0]), delimiter=";")
        writer.writeheader()
        writer.writerows({key: f"{value:.2f}".replace(".", ",") if isinstance(value, float) else value
                          for key, value in row.items()} for row in rows)


def calendar(rows, due):
    """Monthly control amounts to be split and dated against invoices and bank dates."""
    events = []
    for row in rows:
        month = row["mes"]
        if month not in (1, 9, 10, 12, 13, 14, 15, 16, 21):
            continue
        moved = h5[5] if month == contract_month(due) else 0
        flows = [
            ("crédito abonado", row["banco_abonado"], "Banco / D1", "", row["periodo"]),
            ("aporte abonado", row["socios_abonado"], "Socios / D1", "", row["periodo"]),
            ("abono H5 con IVA", moved * (1 + vat_rate), "Curimón / D1", due.isoformat(), ""),
            ("otros cobros con IVA", row["cobro_neto"] + row["iva_cobrado"] - moved * (1 + vat_rate), "Curimón / D1", "", ""),
            ("egresos netos, desglosar", -row["egreso_neto"], "D2/D4", "", ""),
            ("IVA compras", -row["iva_compra"], "D2/D4", "", ""),
            ("entero IVA previo", -row["entero_iva"], "D2/Tesorería", "", ""),
            ("reserva D4", -row["reserva_d4"], "D4", "", ""),
            ("horas a comprar", -row["compra_horas"], "D2", "", ""),
            ("IVA calibración", -row["iva_calibracion"], "D2", "", ""),
            ("comisión ilustrativa", -row["comision"], "Banco / D1", "", ""),
            ("intereses", -row["interes"], "Banco / D1", "", ""),
            ("repago puente tras H5", -row["repago_puente"], "Banco / D1", "", ""),
            ("amortización préstamo inicial", -row["principal_banco"], "Banco / D1", "", ""),
        ]
        assert abs(sum(item[1] for item in flows) - (row["caja_cierre"] - row["caja_apertura"])) < 0.01
        for concept, amount, owner, proposed, availability in flows:
            if abs(amount) > 0.01:
                events.append(dict(mes=month, periodo=row["periodo"], concepto=concept,
                                   control_clp=amount, responsable=owner, fecha_sup_borrador=proposed,
                                   disponible_desde_fecha_objetivo=availability, fecha_confirmada="",
                                   hora_u_orden_confirmado="", monto_confirmado_clp="", respaldo=""))
    return events


def main():
    due_15, due_30 = (RECEIPT + timedelta(days=days) for days in (15, 30))
    assert (due_15.isoformat(), due_30.isoformat()) == ("2028-02-15", "2028-03-01")
    m15, m30 = contract_month(due_15), contract_month(due_30)
    base = Stress(12)
    m13, m14, early = Stress(m15, 12), Stress(m30, 12), Stress(m30, 9)
    base_draw = size(base, {}, 1)
    cases = [("base_profesor", base, base_draw, None)]
    for name, stress, repayment in (
        ("tesoreria_h5_m13", Stress(m15), m15),
        ("h5_m13_reserva_m12_tramos_repago_m16", m13, 16),
        ("h5_m14_reserva_m12_tramos_repago_m16", m14, 16),
        ("h5_m14_reserva_m9_tramos_repago_m16", early, 16),
        ("h5_m14_reserva_m12_tramos_repago_h5", m14, m30),
    ):
        cases.append((name, stress, stage(stress, base_draw, repayment), repayment))
    for name, stress in (
        ("h5_m13_reserva_m12_todo_m1", m13),
        ("h5_m14_reserva_m12_todo_m1", m14),
        ("h5_m14_reserva_m9_todo_m1", early),
    ):
        cases.append((name, stress, size(stress, {}, 1), None))
    cases.append(("h5_m14_reserva_m12_cota_orden_todo_m1", m14,
                  size(m14, {}, 1, field="caja_antes_de_cobros"), None))
    reference_costs = {**HOURS, 12: RESERVE + FEE, **CALIBRATION}
    ref_h5_m13 = simulate(initial + REFILL, limit, m15, reference_costs)
    ref_h5_m14 = simulate(initial + REFILL, limit, m30, reference_costs)
    assert abs(ref_h5_m13[11]["caja"] - 8_957_065) < 1
    assert abs(ref_h5_m14[12]["caja"] - (-8_989_379)) < 1
    official = simulate(base_draw[1], 0)
    assert max(abs(row["caja"] - test["caja_cierre"])
               for row, test in zip(official, model(base, base_draw))) < 0.01
    serial = {}
    all_rows = []
    for name, stress, draws, repay_from in cases:
        rows = model(stress, draws, repay_from)
        assert len(rows) == 57
        assert low(rows)["caja_cierre"] >= target
        assert all(row["giro_linea"] == row["saldo_linea"] == 0 for row in rows)
        assert rows[-1]["saldo_banco"] == rows[-1]["saldo_puente"] == 0
        payment_month = max(repay_from or 0, stress.collection)
        assert rows[payment_month - 1]["saldo_puente"] == 0
        assert not any(row["repago_puente"] for row in rows[:payment_month - 1])
        assert all(row["factura_neta"] == source[4] for row, source in zip(rows, flux))
        assert abs(sum(row["cobro_neto"] for row in rows) - sum(row[5] for row in flux)) < 0.01
        serial[name] = summary(rows, draws, stress)
        all_rows.extend(dict(escenario=name, **row) for row in rows)
    delayed_values = [row["cobro_neto"] - row["egreso_neto"] for row in model(Stress(m30), base_draw)[:56]]
    assert abs(npv(inputs["B10"].value, delayed_values) - 1_226_784_192) < 1
    chosen = next((stress, draws, repayment) for name, stress, draws, repayment in cases
                  if name == "h5_m14_reserva_m12_tramos_repago_m16")
    OUT.mkdir(exist_ok=True)
    save_csv(OUT / "flujo-mensual-d1-d2.csv", all_rows)
    save_csv(OUT / "tesoreria-fechas-por-acreditar.csv", calendar(model(*chosen), due_30))
    (OUT / "dimensionamiento.json").write_text(json.dumps(
        {"sha": CUT, "caja_objetivo_clp": target, "h5_neto_clp": h5[5],
         "h5_factura_provisional": RECEIPT.isoformat(), "vencimiento_15": due_15.isoformat(),
         "vencimiento_30": due_30.isoformat(), "reserva_clp": RESERVE, "horas_compra_clp": HOURS,
         "comision_estrés_clp": FEE, "iva_calibracion_clp": CALIBRATION,
         "m14_solo_atraso_van_clp": npv(inputs["B10"].value, delayed_values),
         "m14_solo_atraso_tir": irr(delayed_values),
         "referencia_refuerzo_400": {"m13_caja_m12": ref_h5_m13[11]["caja"],
                                    "m14_caja_m13": ref_h5_m14[12]["caja"]},
         "escenarios": serial}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"{len(cases)} escenarios verificados, 56 cierres más M57, deuda conciliada y factura H5 fija.")


if __name__ == "__main__":
    main()
