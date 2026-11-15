"""Fase C de la Entrega 3.2: hoja «Feedback 3.2» con la respuesta trazable a la revisión.

Uso: /usr/bin/python3 aplicar_registro.py ENTRADA.xlsx SALIDA.xlsx
Los resultados se escriben como fórmulas para que sigan al modelo.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lo  # noqa: E402

FILAS = [
    ('P1', 'Flujo sin línea de crédito; la línea solo ante riesgo',
     'Base sin giros; prepago bancario M17-M18 tras H9 y H10; línea corregida en escenarios',
     "=SUM($'Flujo de Caja'.R2:R57)", 'Giros de línea en la base (CLP)',
     "Flujo de Caja R; Amortización; Parámetros corrección B84, B89"),
    ('P2', 'La caja no debe quedar bajo la línea de flotación',
     'Caja de cierre y cota previa a cobros sobre el piso todos los meses',
     "=MIN($'Flujo de Caja'.W2:W57)", 'Caja de cierre mínima (CLP)',
     "Flujo de Caja W y AG; Control de entrega B2, B21"),
    ('P2', '', '', "=MIN($'Flujo de Caja'.AG2:AG57)", 'Cota mínima antes de cobros (CLP)', 'Piso: Parámetros corrección B3'),
    ('P3', 'Costos con adquisiciones, instalación y puesta en producción visibles',
     'Prepago anual de soporte de fabricantes; montaje por lote M7-M9; refuerzo en H6, H7, H11 y H12',
     "=MAX($Costos.K2:K57)-MIN($Costos.K22:K57)", 'Amplitud mensual del costo (CLP)',
     'Detalle proveedores D4; Instalación por lote; Dotación por perfil G; Soporte por perfil F; B85-B88'),
    ('P4', 'Bajar soporte con la madurez',
     'Escalones 75/50/25 % de la carga variable en la base desde M25, M33 y M45',
     "=$Personal.D23-$Personal.D57", 'Baja de personal M22 a M56 (CLP/mes)',
     'Parámetros corrección B70, B12-B15; Soporte por perfil E'),
    ('P5', 'Externalizar lo operativo y dar de baja al personal que termina',
     'Montaje externo sustituye horas internas; técnico interno sale en M10; campo en operación por visita',
     "=SUM($'Detalle proveedores D4'.E380:E426)", 'Servicio de campo externo M10-M56 (CLP)',
     'Parámetros corrección B59, B78-B83; Tarifas por perfil F16:I16; Contrato de soporte B7'),
    ('P5', '', '', "=(320-$'Parámetros corrección'.B78)*$'Contrato de soporte'.D7*36", 'Nómina interna de campo evitada en operación (CLP)',
     'Contrato de soporte B7 y D7'),
    ('Precio', 'Margen bajo el tope de 20 %',
     'Precio por fase desde costo y margen objetivo 18,5 %', '=$Indicadores.B10', 'Margen EBITDA sobre ventas',
     'Parámetros D2 B2, B14, B15; Parámetros corrección B62'),
    ('Interés', 'Menor costo financiero', 'Crédito pagado en M17-M18 en vez de M21',
     "=SUM($'Flujo de Caja'.P2:P63)", 'Interés bancario total (CLP)', 'Control de entrega B33'),
]


def main(entrada, salida):
    desk = lo.connect()
    doc = lo.open_doc(desk, entrada)
    sh = doc.Sheets
    if not sh.hasByName('Feedback 3.2'):
        sh.insertNewByName('Feedback 3.2', 0)
    ws = sh.getByName('Feedback 3.2')
    for j, t in enumerate(['Punto', 'Observación de la revisión', 'Cambio 3.2', 'Resultado', 'Medida', 'Respaldo']):
        ws.getCellByPosition(j, 0).setString(t)
    for i, fila in enumerate(FILAS, start=1):
        for j, v in enumerate(fila):
            cell = ws.getCellByPosition(j, i)
            if v.startswith('='):
                cell.setFormula(v)
            else:
                cell.setString(v)
    ws.getCellByPosition(0, len(FILAS) + 2).setString(
        'Supuestos 3.2 sin cotización recibida: horas internas de campo, visitas y rondas del proveedor, '
        'refuerzos de puesta en producción. Se rotulan en Parámetros corrección C78-C89.')
    doc.calculateAll()
    ws.protect('')
    lo.save_xlsx(doc, salida)
    doc.close(True)
    lo.close(desk)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
