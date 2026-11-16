"""Fase D: entradas editables y calendario de pagos parametrizado de la planilla 3.2.

Mantiene los importes del caso base. Las cuotas propuestas son decisiones de
planificación explícitas, no el resultado de un optimizador ejecutado por Excel.
Uso: /usr/bin/python3 aplicar_controles.py ENTRADA.xlsx SALIDA.xlsx
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lo  # noqa: E402
import uno  # noqa: E402

PC = "$'Parámetros corrección'"
D2 = "$'Parámetros D2'"


def main(entrada, salida):
    desk = lo.connect()
    doc = None
    try:
        doc = lo.open_doc(desk, entrada)
        sh = doc.Sheets
        for i in range(sh.Count):
            sh.getByIndex(i).unprotect('')

        def cell(hoja, ref):
            return sh.getByName(hoja).getCellRangeByName(ref)

        def put(hoja, ref, value):
            c = cell(hoja, ref)
            if isinstance(value, str):
                if value.startswith('='):
                    c.setFormula(value)
                else:
                    c.setString(value)
            else:
                c.setValue(value)

        p = 'Parámetros corrección'
        am = sh.getByName('Amortización')
        # La fase B calcula una propuesta de dos prepagos para la base 3.2.
        # Se expone como entradas y se deriva el remanente del principal vigente.
        cuotas = [(int(am.getCellRangeByName(f'A{r}').getValue()),
                   am.getCellRangeByName(f'B{r}').getValue())
                  for r in range(2, 64)
                  if am.getCellRangeByName(f'B{r}').getValue() > 0]
        if len(cuotas) != 2:
            raise ValueError('La fase D espera la propuesta de dos prepagos de la base 3.2; revisar el calendario antes de regenerar.')
        put(p, 'A90', 'Primer prepago programado CLP')
        put(p, 'B90', cuotas[0][1])
        put(p, 'C90', 'Decisión presupuestaria editable: propuesta calculada para la base 3.2. '
            'No se reoptimiza al cambiar costos; comprobar los controles de liquidez.')
        put(p, 'A91', 'Mes programado de liquidación del remanente')
        put(p, 'B91', cuotas[-1][0])
        put(p, 'C91', 'Se usa el mayor entre B89 y B91. Si coinciden, ambas cuotas se programan en ese mes; '
            'el flujo limita el pago por saldo y piso de caja.')
        put(p, 'A92', 'FTE de referencia del técnico antes de su salida')
        put(p, 'B92', cell('Tarifas por perfil', 'E16').getValue())
        put(p, 'C92', 'Referencia del técnico del tramo M6–M9. Desde M10 se reserva este FTE solo antes de B83. '
            'B83 admite M10–M21: salida durante o al final de implementación.')
        put(p, 'C89', 'Primer mes programado de prepago. Junto a B90 y B91 alimenta Amortización; '
            'las fechas e importes son una propuesta de planificación, sujeta a cobros y piso de caja.')

        principal = f'{D2}.$B$4*{D2}.$B$5'
        for r in range(2, 64):
            put('Amortización', f'B{r}',
                f'=IF(A{r}={PC}.$B$89;MIN({principal};{PC}.$B$90);0)'
                f'+IF(A{r}=MAX({PC}.$B$89;{PC}.$B$91);MAX(0;{principal}-{PC}.$B$90);0)')
            put('Amortización', f'C{r}', 'Cuotas propuestas en B89:B91; remanente calculado desde el principal vigente.')

        # Promedio por tramo visible en Tarifas; reserva mensual exacta en Dotación.
        for col, inicio, fin in [('F', 10, 13), ('G', 13, 16), ('H', 16, 19), ('I', 19, 21)]:
            put('Tarifas por perfil', f'{col}16',
                f'={PC}.$B$92*MAX(0;MIN({PC}.$B$83;{fin})-{inicio})/({fin}-{inicio})')
        put('Tarifas por perfil', 'J16',
            'Promedio FTE del tramo antes de B83; Dotación por perfil aplica el corte exacto por mes. '
            'Montaje sustituible separado; campo externo desde B83.')
        for mes in range(10, 21):
            r = 2 + (mes - 1) * 19 + 14
            put('Dotación por perfil', f'D{r}', f'=IF(A{r}<{PC}.$B$83;{PC}.$B$92;0)')

        # Entradas nuevas: desbloqueo y validación, conservando las fórmulas protegidas.
        for row in range(78, 93):
            c = cell(p, f'B{row}')
            protection = c.getPropertyValue('CellProtection')
            protection.IsLocked = False
            c.setPropertyValue('CellProtection', protection)
            v = c.getPropertyValue('Validation')
            v.Type = uno.Enum('com.sun.star.sheet.ValidationType', 'DECIMAL')
            v.Operator = uno.Enum('com.sun.star.sheet.ConditionOperator', 'GREATER_EQUAL')
            v.Formula1 = '0'
            if row in (79, 80, 81, 82):
                v.Type = uno.Enum('com.sun.star.sheet.ValidationType', 'WHOLE')
            if row in (84, 87, 83, 89, 91):
                v.Type = uno.Enum('com.sun.star.sheet.ValidationType', 'WHOLE')
                v.Operator = uno.Enum('com.sun.star.sheet.ConditionOperator', 'BETWEEN')
                v.Formula1, v.Formula2 = '0', '1'
                if row == 83:
                    v.Formula1, v.Formula2 = '10', '21'
                elif row in (89, 91):
                    v.Formula1, v.Formula2 = '1', '$B$45'
            v.ShowErrorMessage = True
            v.ErrorMessage = 'Usar un número válido para esta entrada. Meses enteros; interruptores 0 o 1; cantidades no negativas.'
            c.setPropertyValue('Validation', v)

        locale = uno.createUnoStruct('com.sun.star.lang.Locale')
        locale.Language, locale.Country = 'en', 'US'
        pct = doc.NumberFormats.queryKey('0.0000%', locale, True)
        if pct == -1:
            pct = doc.NumberFormats.addNew('0.0000%', locale)
        for ref in ['B3', 'B10']:
            cell('Indicadores', ref).setPropertyValue('NumberFormat', pct)
        cell('Feedback 3.2', 'D9').setPropertyValue('NumberFormat', pct)

        ce = 'Control de entrega'
        put(ce, 'A34', 'Principal programado antes del primer mes de prepago')
        put(ce, 'B34', f'=SUMIF($Amortización.$A$2:$A$63;"<"&{PC}.$B$89;$Amortización.$B$2:$B$63)')
        put(ce, 'C34', 'Debe ser cero; el calendario respeta B89.')
        put(ce, 'A35', 'FTE del técnico interno desde su salida')
        put(ce, 'B35', f'=SUMIFS($\'Dotación por perfil\'.$D$2:$D$381;'
            f'$\'Dotación por perfil\'.$A$2:$A$381;">="&{PC}.$B$83;'
            '$\'Dotación por perfil\'.$B$2:$B$381;"Técnico de campo")')
        put(ce, 'C35', 'Debe ser cero; las horas previas se mantienen en su mes.')
        put(ce, 'B20', '3.2 / revisión de controles 15-11-2026')
        put('Resumen Ejecutivo', 'B18',
            f'="E-24: 80% banco y 20% socios. Prepagos propuestos en M"&{PC}.$B$89&'
            f'" y M"&MAX({PC}.$B$89;{PC}.$B$91)&"; pagos sujetos a cobros y piso de caja. Línea para contingencias."')
        for r, texto, formula, unidad in [
            (14, 'Amortización vinculada a B89:B91 y al principal', '=$\'Control de entrega\'.B32', 'Diferencia calendario/principal: cero'),
            (15, 'Salida del técnico vinculada a B83', '=$\'Control de entrega\'.B35', 'FTE después de salida: cero')]:
            for col, val in zip('ABCDEF', ['Control', texto, 'Verificación de entradas y propagación', formula, unidad, 'Revisión de parámetros 3.2']):
                put('Feedback 3.2', f'{col}{r}', val)

        # Los cinco gráficos conservaban todas sus leyendas ligadas a RESUMEN!A1.
        # Cada serie debe tomar su nombre de la cabecera real de sus valores.
        charts = sh.getByName('Gráficos UF').Charts
        for i in range(charts.Count):
            chart = charts.getByIndex(i).EmbeddedObject
            provider = chart.getDataProvider()
            for coord in chart.getFirstDiagram().getCoordinateSystems():
                for tipo in coord.getChartTypes():
                    for serie in tipo.getDataSeries():
                        for seq in serie.getDataSequences():
                            values = seq.getValues()
                            if values.getPropertyValue('Role') != 'values-y':
                                continue
                            source = values.getSourceRangeRepresentation()
                            match = re.fullmatch(r'(.*[.!])(\$?[A-Z]+)\$?\d+(?::.*)?', source)
                            if not match:
                                raise ValueError(f'Rango no reconocido para el nombre de la serie: {source}')
                            seq.setLabel(provider.createDataSequenceByRangeRepresentation(match[1] + match[2] + '$1'))

        doc.calculateAll()
        for i in range(sh.Count):
            sh.getByIndex(i).protect('')
        lo.save_xlsx(doc, salida)
    finally:
        if doc:
            doc.close(True)
        lo.close(desk)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
