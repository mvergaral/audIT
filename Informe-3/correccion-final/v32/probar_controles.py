"""Regresiones de parámetros, protección y pagos en copias abiertas en memoria.

Uso: /usr/bin/python3 probar_controles.py PLANILLA.xlsx
No guarda ni modifica el archivo examinado.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lo  # noqa: E402
import uno  # noqa: E402


def main(path):
    desk = lo.connect()
    doc = None
    try:
        def c(sheet, ref):
            return doc.Sheets.getByName(sheet).getCellRangeByName(ref)

        def v(sheet, ref):
            return c(sheet, ref).getValue()

        def cargar(ref=None, valor=None):
            nonlocal doc
            if doc:
                doc.close(True)
            doc = lo.open_doc(desk, path)
            if ref:
                doc.Sheets.getByName('Parámetros corrección').unprotect('')
                c('Parámetros corrección', ref).setValue(valor)
            doc.calculateAll()

        def pagos():
            return [(int(v('Flujo de Caja', f'A{r}')), v('Flujo de Caja', f'U{r}'))
                    for r in range(2, 64) if v('Flujo de Caja', f'U{r}') > 1]

        def cero(ref):
            assert abs(v('Control de entrega', ref)) < 1, (ref, v('Control de entrega', ref))

        cargar()
        base = v('Indicadores', 'B12')
        assert abs(base - 6801216450.621594) < 1, 'Cambió el presupuesto base publicado de la 3.2'
        assert abs(v('Indicadores', 'B10') - .185) < 1e-8
        assert pagos()[0][0] == 17 and pagos()[-1][0] == 18
        for ref in ['B4', 'B5', 'B11', 'B12', 'B13', 'B15', 'B16', 'B18', 'B24', 'B25', 'B26', 'B28', 'B29', 'B31', 'B32', 'B34', 'B35']:
            cero(ref)
        assert v('Control de entrega', 'B21') >= v('Parámetros corrección', 'B3')
        for row in range(78, 93):
            cell = c('Parámetros corrección', f'B{row}')
            assert not cell.getPropertyValue('CellProtection').IsLocked, row
            assert cell.getPropertyValue('Validation').Type != uno.Enum('com.sun.star.sheet.ValidationType', 'ANY'), row
        assert doc.Sheets.getByName('Amortización').isProtected()
        assert c('Amortización', 'B18').getPropertyValue('CellProtection').IsLocked
        charts = doc.Sheets.getByName('Gráficos UF').Charts
        assert charts.Count == 5
        for i in range(charts.Count):
            chart = charts.getByIndex(i).EmbeddedObject
            names = []
            for coord in chart.getFirstDiagram().getCoordinateSystems():
                for tipo in coord.getChartTypes():
                    for serie in tipo.getDataSeries():
                        for seq in serie.getDataSequences():
                            if seq.getValues().getPropertyValue('Role') == 'values-y':
                                names.append(tuple(seq.getLabel().getData()))
            assert len(names) == 3 and len(set(names)) == 3, (i, names)
        print('OK base conservada, controles, entradas editables/validadas y fórmulas protegidas')
        print('OK cinco gráficos con leyendas distintas vinculadas a sus cabeceras')

        cargar('B89', 18)
        assert pagos()[0][0] >= 18, pagos()
        cero('B32'); cero('B34')
        print('OK B89=18: el primer pago se desplaza y no se anticipa a la fecha propuesta')

        cargar('B4', 740000000)
        assert abs(v('Amortización', 'B65') - 592000000) < 1
        cero('B32')
        print('OK capital 740 M: calendario de 592 M, sin diferencia de principal')

        cargar('B83', 11)
        assert v('Dotación por perfil', 'E187') == 160
        assert v('Dotación por perfil', 'E206') == 0
        assert v('Detalle proveedores D4', 'E380') == 0
        assert v('Detalle proveedores D4', 'E381') > 0
        assert v('Indicadores', 'B12') > base
        cero('B35')
        print('OK salida M11: se pagan 160 h internas M10 y el servicio externo comienza M11')

        cargar('B91', 20)
        assert pagos()[-1][0] >= 20, pagos()
        cero('B32'); cero('B34')
        print('OK B91=20: la liquidación del remanente cambia de mes')
    finally:
        if doc:
            doc.close(True)
        lo.close(desk)


if __name__ == '__main__':
    main(sys.argv[1])
