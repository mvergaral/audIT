# AUD-20 · Decisiones del modelo financiero D1/D2

Decisiones adoptadas para la integración de la Entrega 3 bajo delegación de D1. Las cifras que dependen de cantidades aún en conciliación se calculan a partir de esas entradas cuando se completen.

| Decisión | Implementación |
|---|---|
| Margen comercial | 18,5 % como objetivo de modelación y 19,0 % como sensibilidad, sobre ventas netas. Controlar EBITDA consolidado sobre ingresos netos ≤ 20 %. Separar costos operativos, inversión y gastos financieros antes de comprobar el margen. |
| Precios | Mostrar costos y precios por implementación y operación en CLP, UF y USD. Calcular el precio por fase desde sus costos económicos y el margen seleccionado. Contrastar el resultado con el EBITDA consolidado. |
| Cobros de implementación | El caso de oferta conserva el cobro en el mes del hito E-25 como supuesto de comparación. Para tesorería se propone cobrar H5 a 15 días corridos desde la recepción de la factura válida y se prueba un plazo de 30 días corridos. Cada escenario registra el cobro una vez y conserva el mes contractual del hito. |
| Operación | Base con mensualidad fija y ajuste variable neto cero como supuesto. Mantener variables y multas como entradas por servicio. Devengar de M21 a M56, cobrar de M22 a M57. |
| Financiamiento | Estructura inicial 80 % banco y 20 % socios. Dimensionar el monto con los flujos completos y exigir que la caja de cierre permanezca cubierta bajo el tope de línea de CLP 50.000.000. Interés banco 0,9 % mensual e interés línea 3,0 % mensual sobre saldos de apertura. Evaluar capacidad de pago antes de fijar amortizaciones. |
| Evaluación | Tasa mensual antes de impuestos = 0,80 × 0,9 % + 0,20 × [(1 + 20 %)^(1/12) − 1] = 1,0261894 %. VAN y TIR sobre Fila A, M1–M56 y M0 = 0. Usar Fila C para liquidez. |
| Cierre | Pagar CLP 13.800.000 en M56 por extensión de garantía y cola de seguro. Reconocer el cobro M57 en la conciliación posterior. Sensibilizar el VAN con el valor equivalente en M56 de la cuenta por cobrar, una sola vez. |
| Reserva D4 | Presupuestar CLP 152.699.775 como contingencia identificada. El estrés publicado concentra el desembolso en M12 junto al atraso de H5. Probar además M9, cuando la base usa más línea. La base conserva los costos calendarizados. |
| Garantía de correcto funcionamiento | Calcular la comisión con 5 % del precio de implementación × 1,5 % anual × 2 años. Si se incluye en la base que determina ese mismo precio, despejar algebraicamente la fórmula para evitar circularidad. |
| Innovaciones | Llevar a costos solo desembolsos incrementales atribuibles a audIT. Mantener el beneficio de Curimón en el registro de innovaciones y mostrar el recupero de INN-4 como bruto hasta conocer el reparto. |
| CP-SEC-05 | Conservar 16 h condicionales, incluidas las 7 h estimadas de D4. Usar las 9 h restantes como límite provisional de planificación para conducción, validación y aportes adicionales sujetos al desglose. Mantener las 72 h de preparación en 4.1/A11 y verificar su cobertura antes de cargar un adicional. |

## Disponibilidad de fondos y aceptación de H5

| Concepto | Escenario de cálculo | Evidencia para pasar a comprometido |
|---|---|---|
| H5, M12, 10 % del precio de implementación | CLP 461.880.281,50 netos. El comparador de oferta factura y cobra en M12. La referencia de tesorería cobra en M13 y la sensibilidad de 30 días, en M14 bajo las fechas provisionales indicadas abajo. | E-25 fija mes y porcentaje. El Art. 18 exige el acta de aceptación y contempla diez días hábiles de revisión y diez para subsanar observaciones. Confirmar el plazo de pago y acreditar entrega, acta, recepción de la factura válida y fecha efectiva de abono. |
| Capital inicial M1 | CLP 274.452.748: banco CLP 219.562.198,40 y socios CLP 54.890.549,60. | Carta o contrato, monto desembolsable, vigencia, condiciones de giro, garantías, costo y calendario. Para socios, acuerdo y comprobante o fecha del aporte. |
| Refuerzo hipotético M1 | CLP 400.000.000: banco CLP 320.000.000 y socios CLP 80.000.000. Comisión incremental base del estrés CLP 0. | Acreditar la disponibilidad adicional y las condiciones, además de la fecha, importe y tratamiento de la comisión. La comisión de CLP 250.000 que se prueba abajo es ilustrativa. |
| Línea | Tope de CLP 50.000.000 y tasa mensual de 3,0 % según E-24. | Confirmar instrumento, fecha de habilitación, monto utilizable, tiempos de giro y condiciones de restitución. |

### Plazo propuesto para H5

> Curimón pagará H5 dentro de 15 días corridos desde la recepción de la factura válida. audIT emitirá la factura el día en que la Contraparte Técnica suscriba el acta de aceptación de H5.

Para dimensionar la caja se supone que el acta se suscribe y la factura válida se emite y recibe el **31-01-2028**, último día de M12 según el calendario de períodos AUD-18. El plazo de revisión del Art. 18 se aplica antes del acta. El vencimiento se calcula sumando días corridos a la fecha de recepción de la factura.

| Escenario | Recepción de la factura | Vencimiento de pago | Mes de cobro |
|---|---|---|---|
| Comparador de oferta | M12 | Supuesto de cobro en el mes del hito | M12 |
| Referencia de tesorería · 15 días | 31-01-2028 | 15-02-2028 | M13 |
| Sensibilidad · 30 días | 31-01-2028 | 01-03-2028 | M14 |

La contraparte debe confirmar el plazo propuesto. Una aceptación posterior o una recepción de factura en otra fecha desplaza el vencimiento y puede cambiar el mes de cobro. Al registrar las fechas confirmadas, recalcular el vencimiento y repetir las pruebas de caja mensual e intramensual. [Calendario AUD-18](AUD-18_CALENDARIO_INGRESOS_E25.csv)

En Excel, `Parámetros D2!B49:B51` contiene la recepción de la factura y ambos plazos. `B54` selecciona el plazo alternativo. `Sensibilidad!A72:C75` muestra los saldos de cierre del escenario activo. La prueba mantiene el devengo en M12 para medir el efecto del cobro. Si cambia el mes del acta, también se revisan la facturación y el IVA.

### Pruebas de caja con H5 cobrado en M13

| Caso H5 en M13 | Reserva | Refuerzo M1 | Compra CP-SEC-05 | Comisión ilustrativa M12 | Caja M9 CLP | Caja M12 CLP |
|---|---|---:|---:|---:|---:|---:|
| Atraso aislado | — | 0 | 0 | 0 | 0 | −155.747.160 |
| Estrés sin refuerzo | M12 | 0 | 0 | 0 | 0 | −308.446.935 |
| Reserva anticipada | M9 | 0 | 0 | 0 | −147.699.775 | −310.096.935 |
| Refuerzo de referencia | M12 | 400.000.000 | 0 | 0 | 331.960.000 | 11.223.065 |
| Refuerzo con 72 h | M12 | 400.000.000 | 2.016.000 | 0 | 329.944.000 | 9.207.065 |
| Refuerzo con 72 h y comisión | M12 | 400.000.000 | 2.016.000 | 250.000 | 329.944.000 | 8.957.065 |

### Sensibilidad de 30 días con H5 cobrado en M14

| Escenario | Caja M12 CLP | Caja M13 CLP | Uso máximo de línea CLP |
|---|---:|---:|---:|
| Solo cambio de cobro | −155.747.160 | −222.199.604 | 50.000.000 |
| Reserva en M12 y refuerzo de CLP 400 millones | 11.223.065 | −6.723.379 | 50.000.000 |
| Reserva, refuerzo, compra de 72 h y comisión ilustrativa de CLP 250.000 en M12 | 8.957.065 | −8.989.379 | 50.000.000 |

El VAN de la Fila A con cobro en M14 es CLP 1.226.784.192 y la TIR es 82,63 % mensual. Con el refuerzo y la compra de horas, el saldo negativo de M13 exige cobertura adicional antes del abono de H5.

La reserva en M9 adelanta el uso de la línea y sus intereses. Las 72 h se valorizan en M6–M9 por CLP 576.000, 608.000, 432.000 y 400.000, respectivamente. Con compra completa, comisión y reserva de M12, el incremento marginal de caja por peso de refuerzo M1 es 0,9208 hasta M12, por once meses de interés sobre la fracción bancaria de 80 %. El refuerzo teórico mínimo para llegar a CLP 10.000.000 es CLP 401.132.641 en ese escenario mensual. La cifra presupone el giro de M1 y las demás condiciones simuladas. [Preparación y evidencia de horas](../CRUCE-CP-SEC-05-D2.md)

D1 admitió estudiar un puente con giro en M12 y devolución después del cobro de H5 en M13. En este corte, si se utiliza la línea hasta su tope, el atraso aislado requiere recibir al menos CLP 155.747.161 netos para evitar déficit o CLP 165.747.161 para cerrar M12 con CLP 10.000.000. Si se añade la reserva completa en M12, el umbral para esa meta pasa a CLP 318.446.936, antes de compra de horas y comisiones. Si se retiene comisión del puente, el giro bruto debe cubrir tanto el abono neto objetivo como el cargo. Contrastar costo y calendario con el refuerzo en M1. Acreditar fecha y condiciones antes de considerar el puente disponible. [Alternativa revisada por D1](https://linear.app/audit-fep/issue/AUD-20#comment-8bb96c87-7712-4afe-8ace-a391e17ba1c4)

La prueba de orden adverso concentra los pagos de cada mes antes de sus cobros. Parte de caja de apertura, más fondos del escenario y saldo utilizable de línea, y resta egresos netos, IVA de compras, entero de IVA anterior, intereses y los cargos de estrés. En M13, con el refuerzo de referencia, compra completa, comisión y CLP 114.000 de IVA hipotético de calibración, esa secuencia produce una brecha potencial de CLP 283.808.147 aun con la línea completa. Es una cota de orden de eventos. Para reemplazarla, ordenar diariamente las fechas de abono de hitos, aportes y giros junto con nómina, pagos a proveedores, garantías, tributos e intereses. El control de cierre debe comprobar que el mínimo intramensual esté cubierto y repetir la prueba de caja M12.

Fuentes: FEP01 · Formularios E-21, E-24 y E-25 · pp. 70–74. Aclaraciones · estructura de planilla, financiamiento, Curva S y rentabilidad. Paquete D1 en main desde b8935c4. [AUD-5](https://linear.app/audit-fep/issue/AUD-5) · [AUD-7](https://linear.app/audit-fep/issue/AUD-7) · [AUD-38](https://linear.app/audit-fep/issue/AUD-38).
