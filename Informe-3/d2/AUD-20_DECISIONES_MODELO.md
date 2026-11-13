# AUD-20 · Decisiones del modelo financiero D1/D2

Decisiones adoptadas para la integración de la Entrega 3 bajo delegación de D1. Las cifras que dependen de cantidades aún en conciliación se calculan a partir de esas entradas cuando se completen.

| Decisión | Implementación |
|---|---|
| Margen comercial | 18,5 % como objetivo de modelación y 19,0 % como sensibilidad, sobre ventas netas. Controlar EBITDA consolidado sobre ingresos netos ≤ 20 %. Separar costos operativos, inversión y gastos financieros antes de comprobar el margen. |
| Precios | Mostrar costos y precios por implementación y operación en CLP, UF y USD. Calcular el precio por fase desde sus costos económicos y el margen seleccionado. Contrastar el resultado con el EBITDA consolidado. |
| Cobros de implementación | Base en el mes del hito E-25, condicionada a aceptación. Sensibilidad de H5 un mes después. Desplazar caja sin cambiar el mes del hito ni sumar el cobro dos veces. |
| Operación | Base con mensualidad fija y ajuste variable neto cero como supuesto. Mantener variables y multas como entradas por servicio. Devengar de M21 a M56, cobrar de M22 a M57. |
| Financiamiento | Estructura inicial 80 % banco y 20 % socios. Dimensionar el monto con los flujos completos y exigir que la caja de cierre permanezca cubierta bajo el tope de línea de CLP 50.000.000. Interés banco 0,9 % mensual e interés línea 3,0 % mensual sobre saldos de apertura. Evaluar capacidad de pago antes de fijar amortizaciones. |
| Evaluación | Tasa mensual antes de impuestos = 0,80 × 0,9 % + 0,20 × [(1 + 20 %)^(1/12) − 1] = 1,0261894 %. VAN y TIR sobre Fila A, M1–M56 y M0 = 0. Usar Fila C para liquidez. |
| Cierre | Pagar CLP 13.800.000 en M56 por extensión de garantía y cola de seguro. Reconocer el cobro M57 en la conciliación posterior. Sensibilizar el VAN con el valor equivalente en M56 de la cuenta por cobrar, una sola vez. |
| Reserva D4 | Presupuestar CLP 152.699.775 como contingencia identificada. Simular un desembolso en el mes de mayor necesidad de financiamiento de la base y recalcular la liquidez. La base efectiva conserva los costos calendarizados. |
| Garantía de correcto funcionamiento | Calcular la comisión con 5 % del precio de implementación × 1,5 % anual × 2 años. Si se incluye en la base que determina ese mismo precio, despejar algebraicamente la fórmula para evitar circularidad. |
| Innovaciones | Llevar a costos solo desembolsos incrementales atribuibles a audIT. Mantener el beneficio de Curimón en el registro de innovaciones y mostrar el recupero de INN-4 como bruto hasta conocer el reparto. |
| CP-SEC-05 | Conservar 16 h condicionales, incluidas las 7 h estimadas de D4. Usar las 9 h restantes como límite provisional de planificación para conducción, validación y aportes adicionales sujetos al desglose. Mantener las 72 h de preparación en 4.1/A11 y verificar su cobertura antes de cargar un adicional. |

Fuentes: FEP01 · Formularios E-21, E-24 y E-25 · pp. 70–74. Aclaraciones · estructura de planilla, financiamiento, Curva S y rentabilidad. Paquete D1 en main desde b8935c4. [AUD-5](https://linear.app/audit-fep/issue/AUD-5) · [AUD-7](https://linear.app/audit-fep/issue/AUD-7) · [AUD-38](https://linear.app/audit-fep/issue/AUD-38).
