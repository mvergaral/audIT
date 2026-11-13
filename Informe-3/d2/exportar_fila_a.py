"""Extrae la Fila A calculada del Excel de trabajo para el contraste de D1."""

import csv
import math
from pathlib import Path

from openpyxl import load_workbook


def exportar(directorio):
    libro = load_workbook(directorio / "D2_MODELO_TRABAJO.xlsx", data_only=True)
    flujo = libro["Flujo de Caja"]
    tasa = libro["Parámetros"]["B10"].value
    van = libro["Indicadores"]["B2"].value
    filas = []
    for mes in range(1, 58):
        fila = mes + 1
        periodo, facturacion, cobros, costos, neto = (
            flujo[f"{columna}{fila}"].value for columna in ("A", "E", "F", "G", "H")
        )
        if periodo != mes or not all(
            isinstance(valor, (int, float)) and math.isfinite(valor)
            for valor in (facturacion, cobros, costos, neto)
        ):
            raise ValueError(f"Mes {mes} sin valores calculados válidos")
        if not math.isclose(cobros - costos, neto, abs_tol=0.01):
            raise ValueError(f"La Fila A no cuadra en M{mes}")
        filas.append((mes, facturacion, cobros, costos, neto, mes <= 56))
    contraste = sum(fila[4] / (1 + tasa) ** fila[0] for fila in filas[:56])
    if not math.isclose(contraste, van, abs_tol=0.01):
        raise ValueError("El VAN exportado no coincide con el Excel")
    if not math.isclose(filas[-1][2], filas[-2][1], abs_tol=0.01):
        raise ValueError("M57 no concilia con la mensualidad facturada en M56")
    salida = directorio / "AUD-22_FILA_A_MODELO_TRABAJO.csv"
    with salida.open("w", encoding="utf-8", newline="") as archivo:
        writer = csv.writer(archivo, lineterminator="\n")
        writer.writerow(("mes", "facturacion_clp", "cobros_clp", "costos_clp", "fila_a_clp", "incluido_van_base"))
        writer.writerow((0, 0, 0, 0, 0, True))
        writer.writerows(filas)
    print(f"M0–M56, M57 auxiliar, tasa {tasa:.10%}, VAN {van:.2f} CLP")


if __name__ == "__main__":
    exportar(Path(__file__).resolve().parent)
