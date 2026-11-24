"""Fase B de la Entrega 3.2: precio por margen objetivo, amortización por calendario y línea.

Uso: /usr/bin/python3 aplicar_financiamiento.py ENTRADA.xlsx SALIDA.xlsx
1. Vuelve al precio desde costo y margen objetivo (B62 = 0).
2. Calcula con simular_amortizacion.py el calendario que paga en meses de cobro de hitos sin
   romper el piso, lo escribe en la hoja «Amortización» y conecta el pago bancario.
3. Corrige la línea de los escenarios: gira ante el faltante previo a cobros y reporta el
   déficit residual contra cero.
"""
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lo  # noqa: E402

PC = "$'Parámetros corrección'"
D2 = "$'Parámetros D2'"
AM = "$'Amortización'"
PY = os.environ.get('AUDIT_PYTHON', 'python3')


def main(entrada, salida):
    tmp = salida.replace('.xlsx', '-precio.xlsx')
    desk = lo.connect()
    doc = lo.open_doc(desk, entrada)
    sh = doc.Sheets
    for i in range(sh.Count):
        sh.getByIndex(i).unprotect('')
    pcs = sh.getByName('Parámetros corrección')
    pcs.getCellRangeByName('B62').setValue(0)
    pcs.getCellRangeByName('C62').setString(
        'Base 3.2: precio por fase desde costo y margen objetivo (Parámetros D2 B2). '
        'B60:B61 quedan como referencia de la 3.1 para comparar.')
    pcs.getCellRangeByName('A89').setString('Primer mes de prepago bancario')
    pcs.getCellRangeByName('B89').setValue(17)
    pcs.getCellRangeByName('C89').setString(
        'Base 3.2: después de H7 (paso a producción Etapa 1) y del valle de H5; prepago voluntario, '
        'en escenarios solo si los cobros van al día.')
    doc.calculateAll()
    lo.save_xlsx(doc, tmp)

    # Calendario calculado sobre los flujos ya repreciados (no dependen de la amortización).
    he = sh.getByName('Hitos E25')
    primero = pcs.getCellRangeByName('B89').getValue()
    meses = sorted({int(he.getCellRangeByName(f'E{r}').getValue()) for r in range(2, 14)})
    hitos = ','.join(str(m) for m in meses if m >= primero)
    out = subprocess.run([PY, '-I', '-c', (
        'import sys,json; sys.path.insert(0, %r)\n'
        'from simular_amortizacion import cargar, calendario_colchon\n'
        'par, fl = cargar(%r)\n'
        'print(json.dumps(calendario_colchon(par, fl, 0.0, [%s], 1e7)))'
    ) % (os.path.dirname(os.path.abspath(__file__)), tmp, hitos)], capture_output=True, text=True, check=True)
    import json
    cuotas = {int(k): v for k, v in json.loads(out.stdout).items()}
    print('cuotas:', {k: round(v / 1e6, 2) for k, v in cuotas.items()})

    if not sh.hasByName('Amortización'):
        sh.insertNewByName('Amortización', sh.Count)
    am = sh.getByName('Amortización')
    for j, t in enumerate(['Mes', 'Cuota de principal CLP', 'Criterio']):
        am.getCellByPosition(j, 0).setString(t)
    for mes in range(1, 63):
        am.getCellByPosition(0, mes).setValue(mes)
        am.getCellByPosition(1, mes).setValue(round(cuotas.get(mes, 0.0)))
        if mes in cuotas:
            am.getCellByPosition(2, mes).setString(
                'Prepago tras el cobro del hito del mes; mantiene caja de cierre y cota previa a cobros '
                'sobre el piso en todos los meses siguientes (simular_amortizacion.py).')
    am.getCellByPosition(0, 64).setString('Total')
    am.getCellByPosition(1, 64).setFormula('=SUM(B2:B63)')
    am.getCellByPosition(0, 65).setString('Diferencia con crédito')
    am.getCellByPosition(1, 65).setFormula(f"=B65-{D2}.$B$4*{D2}.$B$5")

    fc = sh.getByName('Flujo de Caja')
    for r in range(3, 64):
        u = fc.getCellRangeByName(f'U{r}')
        viejo = u.getFormula()[1:]
        u.setFormula(f"=IF({PC}.$B$84=1;MIN(V{r-1};MAX(0;SUMIF({AM}.$A$2:$A$63;\"<=\"&A{r};{AM}.$B$2:$B$63)"
                     f"-SUM(U$2:U{r-1}));MAX(0;Y{r}+R{r}-S{r}-{PC}.$B$3));{viejo})")
        # Línea base coherente con los escenarios (inactiva mientras B43 = 0).
        fc.getCellRangeByName(f'R{r}').setFormula(
            f"=IF({PC}.$B$43=1;MIN(MAX(0;{D2}.$B$8-T{r-1});MAX(0;{PC}.$B$3-(Y{r}-F{r}-J{r})));0)")
        fc.getCellRangeByName(f'AG{r}').setFormula(f'=Y{r}+R{r}-F{r}-J{r}')
    fc.getCellRangeByName('R2').setFormula(
        f"=IF({PC}.$B$43=1;MIN({D2}.$B$8;MAX(0;{PC}.$B$3-(Y2-F2-J2)));0)")
    fc.getCellRangeByName('AG2').setFormula('=Y2+R2-F2-J2')

    es = sh.getByName('Escenarios corregidos')
    sens = sh.getByName('Sensibilidad')
    inicios = [r for r in range(2, 1200) if es.getCellRangeByName(f'B{r}').getValue() == 1
               and es.getCellRangeByName(f'A{r}').getString()]
    for k, ini in enumerate(inicios):
        srow = k + 2
        for r in range(ini, ini + 62):
            prev_p = f'P{r-1}' if r > ini else '0'
            prev_r = f'R{r-1}' if r > ini else '0'
            q = es.getCellRangeByName(f'Q{r}')
            viejo = q.getFormula()[1:]
            pagado = f'SUM(Q${ini}:Q{r-1})' if r > ini else '0'
            fr = r - ini + 2  # fila del mismo mes en «Flujo de Caja»
            al_dia = f"SUM(D${ini}:D{r})>=SUM($'Flujo de Caja'.$F$2:$F${fr})*(1-$Sensibilidad.$F${srow})-1"
            debido = (f"MAX(0;IF(OR({al_dia};B{r}>={PC}.$B$5);SUMIF({AM}.$A$2:$A$63;\"<=\"&B{r};{AM}.$B$2:$B$63);0)"
                      f"+IF(B{r}>={PC}.$B$32;SUM(I${ini}:I{r})*{D2}.$B$5;0)-{pagado})")
            q.setFormula(
                f"=IF(AND({PC}.$B$84=1;$Sensibilidad.$Y${srow}=0);MIN({prev_r};MAX(0;M{r}+N{r}-O{r}-{PC}.$B$3);"
                f"{debido});{viejo})")
            es.getCellRangeByName(f'N{r}').setFormula(
                f"=IF($Sensibilidad.$V${srow}=1;MIN(MAX(0;{D2}.$B$8-{prev_p});"
                f"MAX(0;{PC}.$B$3-M{r}+D{r}*(1+{D2}.$B$11*{D2}.$B$12)));0)")
            es.getCellRangeByName(f'V{r}').setFormula(
                f"=M{r}+N{r}-D{r}*(1+{D2}.$B$11*{D2}.$B$12)")
        sens.getCellRangeByName(f'J{srow}').setFormula(f'=MAX(0;-MIN(G{srow};S{srow}))')
    print('bloques de escenarios:', len(inicios))
    sens.getCellRangeByName('A16').setString('Amortización 3.1 en cuotas desde M21')

    ce = sh.getByName('Control de entrega')
    ce.getCellRangeByName('B20').setString('3.2 / 15-11-2026')
    ce.getCellRangeByName('A32').setString('Calendario de amortización menos crédito')
    ce.getCellRangeByName('B32').setFormula(f"={AM}.B66")
    ce.getCellRangeByName('C32').setString('Debe ser cero: las cuotas cubren el crédito bancario inicial.')
    ce.getCellRangeByName('A33').setString('Interés bancario total')
    ce.getCellRangeByName('B33').setFormula("=SUM($'Flujo de Caja'.P2:P63)")
    ce.getCellRangeByName('C33').setString('Prepago desde B89 tras cobros de hitos; comparar con 105,12 M de la 3.1.')

    # Rótulos de versión y textos del resumen.
    sh.getByName('Indicadores').getCellRangeByName('B9').setString(
        'Base presupuestaria 3.2; ver condiciones y controles')
    rex = sh.getByName('Resumen Ejecutivo')
    rex.getCellRangeByName('B1').setString('Informe 3 · versión 3.2')
    rex.getCellRangeByName('B17').setString(
        'Escalones de madurez en la base desde M25, M33 y M45; cobertura fija y guardia se conservan. '
        'Campo en operación externalizado por visita.')
    rex.getCellRangeByName('B18').setString(
        'E-24: 80% banco, 20% socios. Prepago del crédito en M17-M18 tras H9 y H10; línea solo para contingencias.')
    sh.getByName('Conciliación técnica').getCellRangeByName('C1').setString('Presupuesto 3.2')

    doc.calculateAll()
    for i in range(sh.Count):
        sh.getByIndex(i).protect('')
    lo.save_xlsx(doc, salida)
    doc.close(True)
    lo.close(desk)
    os.remove(tmp)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
