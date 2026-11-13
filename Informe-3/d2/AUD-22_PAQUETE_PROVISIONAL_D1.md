# AUD-22 · Paquete provisional para D1

## Datos para VAN y TIR

- [Fila A de M1 a M56](AUD-22_FILA_A_PROVISIONAL.csv). CLP netos, cobros y egresos por mes. M0 = 0 en el escenario.
- [Parámetros y conciliación de M57](AUD-22_PARAMETROS_PROVISIONALES.json). WACC mensual 1,0261894 %. Para el VAN usar la Fila A de M1 a M56. Para la TIR incluir M0 = 0 y usar periodicidad mensual. Si se informa anual, convertir mediante (1 + TIR mensual)^12 − 1.
- [Flujo detallado](AUD-17_FLUJO_INTEGRADO_PROVISIONAL.csv). Incluye Fila C, deuda y las tres series de Curva S. La facturación final de operación queda por cobrar en M56. La sensibilidad incorpora ese cobro en M57 una sola vez.
- Reproducción: ejecutar `python generar_flujo_provisional.py` desde este directorio. Los montos están sin redondear en los CSV para preservar la conciliación.

## Escenario y límites de uso

La ejecución integra D4, licencias, calidad/capacitación, cierre, el calendario administrativo aprobado como provisional y la dotación de escenario del Excel previo. Incluye una comisión estimada de correcto funcionamiento en M21, atribuida a implementación para fijar el precio. Usa M1–M20 como regla provisional de clasificación de los demás costos, aunque H12 se factura en M21. Se mantienen variables y multas en cero en este escenario.

Los flujos están **sin IVA de caja**. El presupuesto definitivo requiere horas/tarifas respaldadas y verificar la cobertura de CP-SEC-05. D1 ya desglosó 8 h y D4 7 h, dentro de las 16 h condicionales. La cobertura por perfil sigue pendiente. También faltan los incrementos de las innovaciones y completar el overhead y las bases de seguros. Estos conceptos abiertos se excluyen de la cifra de escenario. La hoja Resumen del mandante sigue pendiente.

El financiamiento supone un desembolso en M1 (80 % banco, 20 % socios), intereses sobre apertura, pago prioritario de la línea y amortización bancaria con excedentes desde M21. El tamaño calculado cubre los cierres de mes en el escenario. La disponibilidad bancaria y la liquidez dentro de cada mes requieren evidencia separada.

Este paquete permite a D1 reproducir y revisar el cálculo sobre cifras de escenario. AUD-22 queda abierto hasta emitir la versión completa para cierre y AUD-23 hasta incorporar y validar sus resultados definitivos.
