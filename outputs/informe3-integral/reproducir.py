"""Reproduce la caja del paquete versionado y genera escenarios separados."""

import csv
import json
from io import BytesIO
from pathlib import Path
from subprocess import check_output

from openpyxl import load_workbook
from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
CUT = "c9a6515652c3357ea684bf0bb9338b7c4ec028fd"
BOOK = "Informe-3/AUDIT-Informe3-Modelo-Economico.xlsx"
RAW = check_output(["git", "show", f"{CUT}:{BOOK}"], cwd=ROOT)
book = load_workbook(BytesIO(RAW), data_only=True)
inputs = book["Parámetros D2"]
flux = list(book["Flujo de Caja"].values)[1:]
initial, bank_fraction, bank_rate, line_rate, limit = [
    inputs[f"B{i}"].value for i in range(4, 9)
]
uf = inputs["B21"].value
debt_start = inputs["B17"].value
vat_rate = inputs["B11"].value * inputs["B12"].value
h5 = next(row for row in flux if row[1] == "H5")
target = 10_000_000


def simulate(capital, line_limit, h5_month=12, extra_costs=None):
    cash = bank = line = 0
    result = []
    for row in flux:
        month, _, _, _, invoice, collection, cost = row[:7]
        if h5_month != 12:
            collection += h5[5] * ((month == h5_month) - (month == 12))
        extra = (extra_costs or {}).get(month, 0)
        vat_cash = row[14] + vat_rate * (collection - row[5])
        bank_interest = bank * bank_rate
        line_interest = line * line_rate
        paid_capital = capital if month == 1 else 0
        before = cash + paid_capital + collection - cost + vat_cash
        before -= bank_interest + line_interest + extra
        draw = min(line_limit - line, max(0, -before))
        repay = min(line, max(0, before))
        line += draw - repay
        debt_payment = min(bank, max(0, before + draw - repay)) if month >= debt_start else 0
        bank += paid_capital * bank_fraction - debt_payment
        closing = before + draw - repay - debt_payment
        result.append(dict(mes=month, factura=invoice, cobro=collection, costo=cost,
                           iva_caja=vat_cash, egreso_adicional=extra,
                           prestamo=paid_capital * bank_fraction,
                           aporte=paid_capital * (1 - bank_fraction),
                           interes_banco=bank_interest, interes_linea=line_interest,
                           antes_de_giro=before, giro=draw, pago_linea=repay,
                           saldo_linea=line, amortizacion=debt_payment, saldo_banco=bank,
                           caja=closing, fila_c=closing-cash))
        cash = closing
    return result


def minimum(rows):
    return min(rows[:56], key=lambda row: row["caja"])


def dimension(h5_month=12, extra_costs=None):
    low, high = int(initial), 2_000_000_000
    assert minimum(simulate(high, 0, h5_month, extra_costs))["caja"] >= target
    while low < high:
        probe = (low + high) // 2
        if minimum(simulate(probe, 0, h5_month, extra_costs))["caja"] >= target:
            high = probe
        else:
            low = probe + 1
    return low


def summarize(rows):
    floor = minimum(rows)
    fields = ("prestamo", "aporte", "giro", "pago_linea", "interes_linea", "interes_banco")
    return {
        "caja_minima": floor["caja"], "mes_minimo": floor["mes"],
        "antes_de_giro_en_minimo": floor["antes_de_giro"],
        "saldo_linea_max": max(row["saldo_linea"] for row in rows),
        "meses_giro": [row["mes"] for row in rows if row["giro"] > 0.01],
        "meses_pago_linea": [row["mes"] for row in rows if row["pago_linea"] > 0.01],
        "pagos_banco": [[row["mes"], row["amortizacion"]] for row in rows if row["amortizacion"] > 0.01],
        "deficit_residual": max(0, -floor["caja"]),
        **{field: sum(row[field] for row in rows) for field in fields},
    }


def npv(rate, values):
    return sum(value / (1 + rate) ** month for month, value in enumerate(values, 1))


def irr(values):
    low, high = 0, 2
    assert npv(low, values) > 0 > npv(high, values)
    for _ in range(70):
        mid = (low + high) / 2
        if npv(mid, values) > 0:
            low = mid
        else:
            high = mid
    return (low + high) / 2


def chart(filename, title, series, ticks, notes, bars=False):
    image = Image.new("RGB", (1260, 640), "#ffffff")
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("arial.ttf", 18)
    title_font = ImageFont.truetype("arialbd.ttf", 32)
    draw.text((62, 37), title, font=title_font, fill="#132238")
    draw.text((62, 86), "UF de 40.000 CLP  |  Corte c9a6515  |  M1–M56", font=font, fill="#4b5c70")
    left, top, right, bottom = 122, 147, 1190, 490
    x = lambda month: left + 10 + (right-left-20) * (month-1)/55
    y = lambda value: bottom - (bottom-top) * (value-ticks[0])/(ticks[-1]-ticks[0])
    for tick in ticks:
        draw.line((left, y(tick), right, y(tick)), fill="#93a4b8" if tick == 0 else "#e3eaf1", width=2)
        draw.text((left-12, y(tick)), f"{tick:,}".replace(",", "."), font=font, anchor="rm", fill="#4b5c70")
    for month in (1, 9, 12, 16, 21, 32, 40, 48, 56):
        draw.line((x(month), top, x(month), bottom), fill="#edf1f5")
        draw.text((x(month), bottom+12), f"M{month}", font=font, anchor="mt", fill="#4b5c70")
    for index, (label, color, values) in enumerate(series):
        points = [(x(i), y(v/uf)) for i, v in enumerate(values[:56], 1)]
        if bars:
            for i, (a, b) in enumerate(points, 1):
                draw.rectangle((a-6, b, a+6, y(0)), fill="#b65b33" if i in (13, 16, 17) else color)
        else:
            draw.line(points, fill=color, width=4)
        offset = 122 + index * 350
        draw.line((offset, 552, offset+24, 552), fill=color, width=5)
        draw.text((offset+34, 552), label, font=font, anchor="lm", fill="#132238")
    draw.text((122, 590), notes, font=font, fill="#4b5c70")
    image.save(OUT / filename)


def main():
    base = simulate(initial, limit)
    assert max(abs(row["caja"] - cached[22]) for row, cached in zip(base, flux)) < 0.01
    assert max(abs(row["saldo_linea"] - cached[19]) for row, cached in zip(base, flux)) < 0.01
    assert max(abs(row["saldo_banco"] - cached[21]) for row, cached in zip(base, flux)) < 0.01
    assert len(flux) == 57 and sum(bool(row[1]) for row in flux) == 12
    scenarios = {
        "base_publicada": base,
        "base_sin_linea": simulate(initial, 0),
        "base_condicionada": simulate(dimension(), 0),
        "h5_m13_sin_linea": simulate(initial, 0, 13),
        "h5_m13_capital_base_condicionado": simulate(dimension(), limit, 13),
        "h5_m13_con_linea": simulate(initial, limit, 13),
        "h5_m13_reserva_sin_refuerzo": simulate(initial, limit, 13, {12: inputs["B22"].value}),
        "h5_m13_reserva_sin_linea_condicionado": simulate(
            dimension(13, {12: inputs["B22"].value}), 0, 13, {12: inputs["B22"].value}),
    }
    assert abs(minimum(scenarios["h5_m13_con_linea"])["caja"] - book["Sensibilidad"]["D5"].value) < 0.01
    assert all(row["giro"] == row["saldo_linea"] == 0 for row in scenarios["base_condicionada"])
    assert minimum(scenarios["base_condicionada"])["caja"] >= target
    assert minimum(simulate(dimension() - 1, 0))["caja"] < target
    assert all(row["factura"] == cached[4] for rows in scenarios.values() for row, cached in zip(rows, flux))
    values = [row[7] for row in flux[:56]]
    rate = bank_fraction * bank_rate + (1-bank_fraction) * ((1+inputs["B9"].value)**(1/12)-1)
    cost = sum(row[6] for row in flux[:56])
    sale = sum(row[4] for row in flux[:56])
    metrics = dict(tasa_mensual=rate, van=npv(rate, values), tir_mensual=irr(values),
                   costo=cost, venta=sale, margen=(sale-cost)/sale, cobro_m57=flux[56][5],
                   picos_costo=sorted(((row[0], row[6]) for row in flux), key=lambda pair: -pair[1])[:5])
    for key, cell in (("van", "B2"), ("tir_mensual", "B3"), ("margen", "B10")):
        assert abs(metrics[key] - book["Indicadores"][cell].value) < 0.01
    with (OUT / "series-mensuales.csv").open("w", newline="", encoding="utf-8-sig") as file:
        columns = list(base[0])[1:]
        writer = csv.writer(file)
        writer.writerow(["escenario", "mes", *[f"{field}_uf" for field in columns],
                         "costo_mas_intereses_acumulado_uf", "facturacion_acumulada_uf"])
        for name, rows in scenarios.items():
            costs = invoices = 0
            for row in rows:
                costs += row["costo"] + row["interes_banco"] + row["interes_linea"] + row["egreso_adicional"]
                invoices += row["factura"]
                writer.writerow([name, row["mes"], *[row[field]/uf for field in columns], costs/uf, invoices/uf])
    (OUT / "controles.json").write_text(json.dumps(
        {"corte": CUT, "clp_por_uf": uf, "meta_clp": target,
         "modelo": metrics, "escenarios": {name: summarize(rows) for name, rows in scenarios.items()}},
        ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    curve = list(book["Curva S"].values)[1:]
    chart("curva-s-uf.png", "Curva S del paquete versionado", [
        ("Costos con intereses", "#25589a", [row[1] for row in curve]),
        ("Facturación acumulada", "#167a62", [row[2] for row in curve]),
        ("Caja financiada", "#b65b33", [row[3] for row in curve]),
    ], [0, 50_000, 100_000, 150_000, 200_000, 250_000], "Fuente · Curva S!B2:D57. Giro en M9; H5 en M12; amortización en M21.")
    chart("costos-mensuales-uf.png", "Egresos netos por mes", [
        ("Egreso neto del proyecto", "#25589a", [row["costo"] for row in base]),
    ], [0, 2000, 4000, 6000, 7000], "Fuente · Costos!K2:K57. Mayores egresos en M13, M17 y M16.", bars=True)
    chart("caja-uf.png", "Caja financiada y atraso de H5", [
        ("Base versionada", "#25589a", [row["caja"] for row in base]),
        ("Base condicionada sin línea", "#167a62", [row["caja"] for row in scenarios["base_condicionada"]]),
        ("H5 M13 con capital condicionado", "#b65b33", [row["caja"] for row in scenarios["h5_m13_capital_base_condicionado"]]),
    ], [-5000, 0, 10_000, 20_000, 30_000, 45_000], "M9 · giro base. M12 · déficit por atraso de H5. M21 · amortización bancaria.")
    print("Caja, deuda y línea cotejadas en 57 meses. VAN, TIR, margen y estrés H5 reproducidos.")


if __name__ == "__main__":
    main()
