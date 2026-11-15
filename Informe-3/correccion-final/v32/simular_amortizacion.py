"""Calcula un calendario de amortización anticipada que respeta el piso de caja.

Replica el flujo financiado base de «Flujo de Caja» (sin línea) y, mes a mes, paga el
máximo principal que mantiene la caja de cierre y la cota previa a cobros sobre el piso en
todos los meses siguientes. Redondea las cuotas hacia abajo al múltiplo indicado.
Uso: python simular_amortizacion.py PLANILLA.xlsx [redondeo_CLP]
"""
import math
import sys

import openpyxl


def cargar(path):
    wb = openpyxl.load_workbook(path, data_only=True)
    pc, d2 = wb['Parámetros corrección'], wb['Parámetros D2']
    fc = [r for r in wb['Flujo de Caja'].iter_rows(min_row=2, values_only=True) if isinstance(r[0], int)]
    par = dict(piso=pc['B3'].value, comision=pc['B29'].value, capital=d2['B4'].value,
               banco=d2['B5'].value, tasa=d2['B6'].value)
    # H Fila A, O IVA neto caja, F cobros, J IVA cobrado
    flujos = [(r[0], r[7] or 0, r[14] or 0, r[5] or 0, r[9] or 0) for r in fc]
    return par, flujos


def simular(par, flujos, cuotas):
    caja, saldo, interes, filas = 0.0, 0.0, 0.0, []
    for mes, filaA, iva, cobro, ivac in flujos:
        ini = par['capital'] if mes == 1 else 0.0
        i = saldo * par['tasa']
        y = caja + filaA + iva + ini - i - (par['comision'] if mes == 1 else 0)
        saldo += ini * par['banco']
        pago = min(saldo, cuotas.get(mes, 0.0))
        caja, saldo, interes = y - pago, saldo - pago, interes + i
        filas.append((mes, y - cobro - ivac, caja, saldo))
    return filas, interes


def calendario(par, flujos, redondeo):
    cuotas = {}
    for mes, *_ in flujos:
        if mes == 1:
            continue
        filas, _ = simular(par, flujos, cuotas)
        if filas[mes - 1][3] <= 0:
            break
        holgura = min(min(c, w) for m, c, w, _ in filas if m > mes) if mes < len(filas) else math.inf
        holgura = min(holgura, filas[mes - 1][2]) - par['piso']
        pago = min(filas[mes - 1][3], max(0.0, holgura))
        pago = math.floor(pago / redondeo) * redondeo if pago < filas[mes - 1][3] else filas[mes - 1][3]
        if pago > 0:
            cuotas[mes] = pago
    return cuotas


if __name__ == '__main__':
    par, flujos = cargar(sys.argv[1])
    redondeo = float(sys.argv[2]) if len(sys.argv) > 2 else 1e6
    _, int_bullet = simular(par, flujos, {21: 1e12})
    cuotas = calendario(par, flujos, redondeo)
    filas, interes = simular(par, flujos, cuotas)
    print(f"interés bullet M21: {int_bullet/1e6:.2f} M | interés calendario: {interes/1e6:.2f} M")
    for m, v in cuotas.items():
        print(f"M{m}: {v/1e6:.2f} M")
    peor = min(min(c, w) for _, c, w, _ in filas[:56])
    print(f"mínimo de caja/cota con calendario: {peor/1e6:.2f} M | saldo final {filas[55][3]:.0f}")


def calendario_colchon(par, flujos, colchon, meses_pago, redondeo):
    """Paga solo en meses de cobro de hitos y deja caja de cierre >= piso + colchón."""
    cuotas = {}
    for mes in meses_pago:
        filas, _ = simular(par, flujos, cuotas)
        saldo = filas[mes - 1][3]
        if saldo <= 0:
            continue
        fut = [(c, w) for m, c, w, _ in filas if m >= mes]
        h = min(min(c - par['piso'], w - par['piso'] - colchon) for c, w in fut)
        pago = min(saldo, max(0.0, h))
        if pago < saldo:
            pago = math.floor(pago / redondeo) * redondeo
        if pago > 0:
            cuotas[mes] = pago
    return cuotas
