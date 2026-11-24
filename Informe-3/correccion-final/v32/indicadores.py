"""Resume indicadores y controles de una planilla recalculada (valores en caché).

Uso: python indicadores.py PLANILLA.xlsx [--meses]
"""
import sys

import openpyxl


def leer(path):
    wb = openpyxl.load_workbook(path, data_only=True)
    fc = [r for r in wb['Flujo de Caja'].iter_rows(min_row=2, values_only=True) if isinstance(r[0], int)]
    co = {r[0]: r for r in wb['Costos'].iter_rows(min_row=2, values_only=True) if isinstance(r[0], int)}
    return wb, fc, co


def resumen(path, meses=False):
    wb, fc, co = leer(path)
    base = [r for r in fc if r[0] <= 56]
    venta = sum(r[4] or 0 for r in base)
    costo = sum(r[6] or 0 for r in base)
    out = {
        'venta': venta, 'costo': costo, 'ebitda': venta - costo,
        'margen': (venta - costo) / venta,
        'capital': wb['Parámetros D2']['B4'].value,
        'giros_linea': sum(r[17] or 0 for r in fc),
        'interes_banco': sum(r[15] or 0 for r in fc),
        'interes_linea': sum(r[16] or 0 for r in fc),
        'caja_min': min(r[22] for r in base), 'mes_caja_min': min(base, key=lambda r: r[22])[0],
        'cota_min': min(r[32] for r in base), 'mes_cota_min': min(base, key=lambda r: r[32])[0],
        'identidad_max': max(abs(r[33] or 0) for r in fc),
        'caja_m56': base[-1][22],
        'van': wb['Indicadores']['B2'].value, 'tir': wb['Indicadores']['B3'].value,
    }
    errores = sum(1 for ws in wb for row in ws.iter_rows(values_only=True) for v in row
                  if isinstance(v, str) and (v.startswith('#') or v.startswith('Err:')))
    out['celdas_error'] = errores
    m = lambda x: f'{x / 1e6:,.2f}'
    print(f"venta {m(out['venta'])} | costo {m(out['costo'])} | EBITDA {m(out['ebitda'])} | margen {out['margen']:.4%}")
    print(f"capital {m(out['capital'])} | giros línea {m(out['giros_linea'])} | interés banco {m(out['interes_banco'])}"
          f" | interés línea {m(out['interes_linea'])}")
    print(f"caja mín {m(out['caja_min'])} (M{out['mes_caja_min']}) | cota mín {m(out['cota_min'])} (M{out['mes_cota_min']})"
          f" | caja M56 {m(out['caja_m56'])}")
    print(f"VAN {out['van']} | TIR {out['tir']} | |identidad| máx {out['identidad_max']:.3g} | celdas con error {errores}")
    if meses:
        print(' M  cobros  costos  D4    pers  pagoB  saldoB   caja   cota')
        for r in base:
            c = co[r[0]]
            print(f"{r[0]:>2} {m(r[5]):>7} {m(r[6]):>7} {m(c[1]):>6} {m(c[6]):>6} {m(r[20] or 0):>6} {m(r[21] or 0):>7}"
                  f" {m(r[22]):>7} {m(r[32]):>7}")
    sens = wb['Sensibilidad']
    hdr = [c.value for c in sens[1]]
    print('escenario | caja mín | línea máx | déficit | cota | faltante piso | VAN')
    for r in sens.iter_rows(min_row=2, max_row=16, values_only=True):
        if r[0]:
            d = dict(zip(hdr, r))
            g = lambda k: m(d[k]) if isinstance(d.get(k), (int, float)) else d.get(k)
            print(f"{r[0]:32} {g('Caja mínima CLP'):>9} {g('Línea máxima CLP'):>7} {g('Déficit residual CLP'):>8}"
                  f" {g('Cota antes de cobros CLP'):>9} {g('Faltante frente a piso CLP'):>8} {g('VAN Fila A CLP'):>9}")
    return out


if __name__ == '__main__':
    resumen(sys.argv[1], '--meses' in sys.argv)
