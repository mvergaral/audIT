"""Fase A de la Entrega 3.2: cambios de costos sobre la planilla 3.1.

Uso: /usr/bin/python3 aplicar_costos.py ENTRADA.xlsx SALIDA.xlsx
Requiere LibreOffice con UNO. Las fórmulas se escriben en sintaxis de Calc.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lo  # noqa: E402

PC = "$'Parámetros corrección'"
PERFILES = 19  # filas por mes en «Dotación por perfil»
IDX = {'SRE': 5, 'Software': 8, 'Técnico de campo': 14}


def fila_dotacion(mes, perfil):
    return 2 + (mes - 1) * PERFILES + IDX[perfil]


def mes_hito(h):
    return f"SUMIF($'Hitos E25'.$A$2:$A$13;\"{h}\";$'Hitos E25'.$C$2:$C$13)"


def main(entrada, salida):
    desk = lo.connect()
    doc = lo.open_doc(desk, entrada)
    sh = doc.Sheets
    for i in range(sh.Count):
        sh.getByIndex(i).unprotect('')

    def c(hoja, ref):
        return sh.getByName(hoja).getCellRangeByName(ref)

    def put(hoja, ref, v):
        cell = c(hoja, ref)
        if isinstance(v, str) and v.startswith('='):
            cell.setFormula(v)
        elif isinstance(v, str):
            cell.setString(v)
        else:
            cell.setValue(v)

    p = 'Parámetros corrección'
    # P4: escalones de madurez en la base.
    put(p, 'B70', 1)
    put(p, 'C70', 'Base 3.2: escalones B13:B15 activos desde M25, M33 y M45 sobre la carga variable, '
        'sujetos a dos meses sin P1, backlog <10 y demanda dentro de capacidad (Art. 78.2).')
    # P5: el montaje externo sustituye las horas internas del técnico.
    put(p, 'B59', 1)
    put(p, 'C59', 'Base 3.2: el proveedor ejecuta el montaje M7-M9 y el técnico interno no se carga en esas horas; '
        'audIT conserva banco y analista.')

    # Nuevos parámetros de la 3.2 (filas 78-87).
    nuevos = [
        ('Horas internas de campo en operación', 80,
         'Supuesto 3.2: 0,5 FTE interno (80 h) para supervisión, recepción en terminal, stock y coordinación de urgencias SLA 4h; '
         'el resto del ciclo de vida se externaliza por visita y rondas.'),
        ('Reposiciones a bordo del contrato (unidades)', 19, 'D4 4.1: iWave G26I, 172 más 19 de reposición.'),
        ('Reposiciones de balizas del contrato (unidades)', 21, 'D4 4.1: Teltonika EYE, 210 más 21 de reposición.'),
        ('Visitas correctivas sin reemplazo por mes', 3,
         'Supuesto 3.2: 3 visitas/mes para diagnóstico, correctivas presenciales SLA 4h, crecimiento M24/M36/M48 y renovación M36.'),
        ('Rondas regionales del proveedor por mes', 2,
         'Supuesto 3.2: 2 rondas regionales por mes; incluye revisiones preventivas periódicas en terminales y traslados según B10.'),
        ('Mes de salida del técnico de campo interno', 19,
         'Cubre montaje de etapas 1 y 2 (M7-M9 y M16-M18 según T-14 y S4); desde M19 campo 100% externo por visita.'),
        ('Amortización por calendario (1) o saldo sobre piso desde B5 (0)', 1,
         'Base 3.2: cuotas de la hoja Amortización, pagadas tras los cobros de hitos y sujetas al piso B3.'),
        ('Refuerzo SRE por puesta en producción (h)', 160,
         'Supuesto 3.2: guardia adicional en H6, H7, H11 (Dotación) y H12 (Soporte).'),
        ('Refuerzo Software por puesta en producción (h)', 80,
         'Supuesto 3.2: corrección en caliente durante la puesta en producción.'),
        ('Prepago anual de soporte de fabricantes (1/0)', 1,
         'Base 3.2: contratos de soporte D4 4.3 pagados por año anticipado en M13, M25, M37 y M49.'),
    ]
    for i, (a, b, cc) in enumerate(nuevos, start=78):
        put(p, f'A{i}', a)
        put(p, f'B{i}', b)
        put(p, f'C{i}', cc)

    # Técnico de campo interno: sin dotación base desde M10 (columnas M10-12 a M19-20).
    for col in 'FGHI':
        put('Tarifas por perfil', f'{col}16', 0)
    put('Tarifas por perfil', 'J16', 'Rol adicional; referencia costo mínimo Ingeniero Junior, EDT4/11. '
        '3.2: sale en M10 (Parámetros corrección B83); campo externo por visita.')

    # Demanda del técnico: las balizas se montan solo en los B54 meses posteriores al piloto.
    for mes in range(1, 21):
        r = fila_dotacion(mes, 'Técnico de campo')
        put('Dotación por perfil', f'F{r}',
            f"=SUMIF($'Instalación por lote'.$A$2:$A$21;A{r};$'Instalación por lote'.$E$2:$E$21)"
            f"+SUMIF($'Instalación por lote'.$A$2:$A$21;A{r};$'Instalación por lote'.$F$2:$F$21)"
            f"+IF(A{r}={PC}.$B$37;{PC}.$B$38*{PC}.$B$6/60;"
            f"IF(AND(A{r}>{PC}.$B$37;A{r}<={PC}.$B$37+{PC}.$B$54);{PC}.$B$52*{PC}.$B$53/60/{PC}.$B$54;0))")

    # Refuerzo de puesta en producción en H6, H7 y H11 (implementación).
    for mes in range(1, 21):
        for perfil, prow in (('SRE', 85), ('Software', 86)):
            r = fila_dotacion(mes, perfil)
            put('Dotación por perfil', f'G{r}',
                f"=MAX(0;F{r}-E{r})+IF(OR(A{r}={mes_hito('H6')};A{r}={mes_hito('H7')};"
                f"A{r}={mes_hito('H11')});{PC}.$B${prow};0)")
    # H12 (operación): refuerzo en «Soporte por perfil».
    sp = sh.getByName('Soporte por perfil')
    for r in range(2, 434):
        perfil = sp.getCellByPosition(1, r - 1).getString()
        prow = 85 if perfil.startswith('SRE') else 86 if perfil.startswith('Software') else None
        if prow:
            put('Soporte por perfil', f'F{r}', f"=IF(A{r}={mes_hito('H12')};{PC}.$B${prow};0)")

    # Campo en operación: horas internas reducidas.
    put('Contrato de soporte', 'B7', f"={PC}.$B$78")
    put('Contrato de soporte', 'E7', '3.2: 0,5 FTE interno (recepción, stock, coordinación); '
        'reposiciones y visitas externas en Detalle proveedores D4.')

    # Servicio de campo externo M10-M56 en «Detalle proveedores D4», filas 380-426.
    for k, mes in enumerate(range(10, 57)):
        r = 380 + k
        put('Detalle proveedores D4', f'A{r}', mes)
        put('Detalle proveedores D4', f'B{r}', 'audIT')
        put('Detalle proveedores D4', f'C{r}', 'Servicio técnico de campo externo')
        put('Detalle proveedores D4', f'D{r}', 'Proveedor de montaje, tarifa de Instalación por lote')
        put('Detalle proveedores D4', f'E{r}',
            f"=IF(A{r}<{PC}.$B$83;0;(({PC}.$B$79+{PC}.$B$80)/({PC}.$B$45-{PC}.$B$83+1)+{PC}.$B$81)"
            f"*{PC}.$B$6/60*$'Tarifas por perfil'.$B$16*(1+{PC}.$B$9)+{PC}.$B$82*{PC}.$B$10)")
        put('Detalle proveedores D4', f'F{r}', 'tasa_presupuestaria_E24')
        put('Detalle proveedores D4', f'G{r}', f"=E{r}*$'Parámetros D2'.$B$11")
        put('Detalle proveedores D4', f'J{r}', 'Supuesto 3.2: reposiciones D4 4.1 y visitas correctivas, B79-B83')
    prov = sh.getByName('Proveedores')
    rd = prov.createReplaceDescriptor()
    rd.SearchString = '$379'
    rd.ReplaceString = '$426'
    print('referencias ampliadas en Proveedores:', prov.replaceAll(rd))

    # Soporte y mantención: prepago anual (mismo total).
    det = sh.getByName('Detalle proveedores D4')
    filas = [r for r in range(2, 380) if det.getCellByPosition(2, r - 1).getString() == 'Soporte y mantención']
    mensual = det.getCellByPosition(4, filas[0] - 1).getValue()
    put(p, 'A88', 'Soporte de fabricantes mensual de referencia CLP')
    put(p, 'B88', mensual)
    put(p, 'C88', 'D4 4.3, valor mensual del calendario_46.py; se paga anual anticipado si B87=1.')
    for r in filas:
        put('Detalle proveedores D4', f'E{r}',
            f"=IF({PC}.$B$87=1;IF(MOD(A{r}-13;12)=0;{PC}.$B$88*MIN(12;{PC}.$B$45-A{r}+1);0);{PC}.$B$88)")
    print('filas de soporte reprogramadas:', len(filas))

    doc.calculateAll()
    for i in range(sh.Count):
        sh.getByIndex(i).protect('')
    lo.save_xlsx(doc, salida)
    doc.close(True)
    lo.close(desk)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
