"""Verifica la Fila A y genera indicadores y la Curva S del escenario D2."""

import csv
import json
import math
from pathlib import Path

import numpy as np
from reportlab.lib import colors
from reportlab.pdfgen import canvas

from generar_flujo_provisional import calcular_van

ROOT = Path(__file__).resolve().parent


def cargar(nombre):
    with (ROOT / nombre).open(encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream))


def dibujar(series):
    pdf = canvas.Canvas(str(ROOT / "AUD-19_CURVA_S_PROVISIONAL.pdf"), pagesize=(820, 480))
    pdf.setTitle("Curva S provisional · D2")
    pdf.setFont("Helvetica-Bold", 20)
    pdf.drawString(62, 434, "Curva S provisional · D2")
    pdf.setFont("Helvetica", 11)
    pdf.drawString(62, 413, "M1–M56 · Millones de CLP · Escenario sin IVA de caja")
    left, bottom, width, height = 78, 100, 685, 275
    maximum = math.ceil(max(max(values) for _, values, _ in series) / 2000) * 2000
    pdf.setFont("Helvetica", 9)
    for tick in range(0, maximum + 1, 2000):
        y = bottom + height * tick / maximum
        pdf.setStrokeColor(colors.HexColor("#DAE1E8"))
        pdf.line(left, y, left + width, y)
        pdf.setFillColor(colors.HexColor("#34465A"))
        pdf.drawRightString(left - 9, y - 3, f"{tick:,}".replace(",", "."))
    for month in (1, 8, 16, 24, 32, 40, 48, 56):
        pdf.drawCentredString(left + width * (month - 1) / 55, bottom - 16, f"M{month}")
    for index, (label, values, color) in enumerate(series):
        pdf.setStrokeColor(colors.HexColor(color))
        pdf.setLineWidth(2.1)
        line = pdf.beginPath()
        line.moveTo(left, bottom + height * values[0] / maximum)
        for i, value in enumerate(values[1:], 1):
            line.lineTo(left + width * i / 55, bottom + height * value / maximum)
        pdf.drawPath(line)
        x = left + index * 240
        pdf.line(x, 49, x + 18, 49)
        pdf.setFillColor(colors.HexColor("#233548"))
        pdf.drawString(x + 24, 46, label)
    pdf.save()


def main():
    rows = cargar("AUD-17_FLUJO_INTEGRADO_PROVISIONAL.csv")
    fila_a = cargar("AUD-22_FILA_A_PROVISIONAL.csv")
    params = json.loads((ROOT / "AUD-22_PARAMETROS_PROVISIONALES.json").read_text(encoding="utf-8"))
    assert [int(r["mes"]) for r in rows] == list(range(1, 57))
    assert [r["fila_a"] for r in fila_a] == [r["fila_a"] for r in rows]
    flows = [float(r["fila_a"]) for r in rows]
    rate = params["tasa_mensual"]
    van = calcular_van(flows, rate)
    assert math.isclose(van, params["van_referencial"], abs_tol=0.01)
    # La raíz positiva del factor de descuento da una TIR mensual real.
    roots = np.polynomial.polynomial.polyroots([params["m0"], *flows])
    rates = sorted(1 / root.real - 1 for root in roots if abs(root.imag) < 1e-8 and root.real > 0)
    assert rates and all(abs(calcular_van(flows, candidate)) < 1 for candidate in rates)
    recovery = [
        i for i in range(1, len(flows) + 1)
        if all(sum(flows[:j]) >= 0 for j in range(i, len(flows) + 1))
    ]
    costs = sum(float(r["egresos"]) for r in rows)
    billings = sum(float(r["facturacion"]) for r in rows)
    h5 = float(rows[11]["cobros"])
    delayed_h5 = flows.copy()
    delayed_h5[11] -= h5
    delayed_h5[12] += h5
    expected_costs = costs + sum(float(r["interes_banco"]) + float(r["interes_linea"]) for r in rows)
    assert math.isclose(float(rows[-1]["costos_acumulados_con_interes"]), expected_costs)
    assert math.isclose(float(rows[-1]["facturacion_acumulada"]), billings)
    assert math.isclose(float(rows[-1]["caja_acumulada"]), sum(float(r["fila_c"]) for r in rows))
    output = {
        "escenario": "Provisional, sin IVA de caja",
        "tasa_mensual": rate,
        "van": van,
        "van_con_cobro_m57": calcular_van([*flows, params["cobro_m57"]], rate),
        "van_con_h5_cobrado_en_m13": calcular_van(delayed_h5, rate),
        "tir_mensual_raices_reales": rates,
        "tir_anual_equivalente": [(1 + candidate) ** 12 - 1 for candidate in rates],
        "mes_recuperacion_simple_sostenida": recovery[0] if recovery else None,
        "facturacion_equilibrio_costos_fijos_escenario_clp": costs,
        "fraccion_facturacion_de_equilibrio": costs / billings,
        "sensibilidad_van_por_tasa_mensual": [
            {"tasa": rate + delta, "van": calcular_van(flows, rate + delta)}
            for delta in (-0.0025, 0, 0.0025)
        ],
    }
    (ROOT / "AUD-23_INDICADORES_PROVISIONALES.json").write_text(
        json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    dibujar([
        (label, [float(r[field]) / 1_000_000 for r in rows], color)
        for label, field, color in (
            ("Costos acumulados con intereses", "costos_acumulados_con_interes", "#A54B1B"),
            ("Facturación acumulada", "facturacion_acumulada", "#184A80"),
            ("Saldo de caja financiado", "caja_acumulada", "#18765E"),
        )
    ])
    print(json.dumps(output, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
