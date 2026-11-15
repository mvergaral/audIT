# Acreditación de fondos y cobro de H5

**Informe 3 · audIT / Transportes Curimón · TFEP-01/2026 · 14 de noviembre de 2026**

## Decisión propuesta por D1 y verificación D2

D1 propone solicitar acreditación para **CLP 332.814.380 en M1** y un compromiso contingente adicional de **hasta CLP 387.240.185**. El compromiso adicional se distribuye entre M9 y M12 según cuándo se pague la reserva D4. Esta estructura deja 56 cierres mensuales de al menos CLP 10 millones con la línea en cero en ambos escenarios de estrés a 30 días. La cobertura dentro del mes requiere fechas de cobro y pago acreditadas o fondos adicionales disponibles antes del primer déficit.

| Concepto | Neto a recibir CLP | Banco CLP | Socios CLP | Fecha objetivo de disponibilidad |
|---|---:|---:|---:|---|
| Capital inicial para el caso base | 332.814.380 | 266.251.504 | 66.562.876 | Inicio de M1, febrero de 2027. Acreditar abono antes del primer egreso. |
| Compromiso contingente máximo, escenario con reserva anticipada | 387.240.185 | 309.792.148 | 77.448.037 | Disponible por tramos desde el inicio de M9, octubre de 2027, y M12, enero de 2028, antes de los egresos que los gatillan. |
| Total máximo del esquema por tramos | **720.054.565** | **576.043.652** | **144.010.913** | Se solicita disponibilidad para el máximo de los caminos excluyentes. |

**Cronograma exacto del refuerzo.** Si la reserva D4 sale en M12, el tramo total de M9 es CLP 2.016.000 (banco 1.612.800 y socios 403.200) y en M12, CLP 381.901.950 (banco 305.521.560 y socios 76.380.390). Si la reserva se paga en M9, ese mes se necesitan CLP 154.715.775 (banco 123.772.620 y socios 30.943.155) y en M12, CLP 232.524.410 (banco 186.019.528 y socios 46.504.882). Cada vía suma lo que ella misma requiere. El calendario de desembolsos debe permitir ambos caminos.

La propuesta usa 80 % de banco y 20 % de socios en cada tramo, 0,9 % mensual sobre saldo bancario de apertura y una comisión ilustrativa de CLP 250.000 pagada en M12 para el estrés. Se deben obtener tasas y comisiones efectivas de la oferta de crédito. Los montos del cuadro expresan abonos netos de retenciones. Si el banco descuenta cargos al transferir, habrá que dimensionar el nominal y el costo desde el monto efectivamente abonado y revisar el reparto E-24. No se modela restitución de aportes.

El préstamo inicial se amortiza en M21. El tramo bancario contingente se paga íntegramente en M16 en la simulación, después de H5 y con el cobro de H7 del escenario. Solicitar que su vencimiento permita esa secuencia y que se documenten las condiciones si H7 se desplaza. El banco y los socios deben respaldar el compromiso. La aprobación previa de D1 se refiere a un supuesto de modelación de CLP 400 millones.

## Tareas ejecutadas y respaldo requerido

| Tarea | Trabajo hecho | Evidencia pendiente y responsable |
|---|---|---|
| Capital inicial | D2 reprodujo el modelo y calculó CLP 332.814.380 como primer múltiplo íntegro de cinco pesos que cubre los 56 cierres con la meta y proporciones exactas. Frente a CLP 274.452.748 versionados, el aumento es CLP 58.361.632. En M9 cierra en CLP 10.000.002,46. | D1 obtiene carta vinculante o contrato con monto neto disponible, calendario, tasa y base, comisiones, garantías y condiciones de giro. Los socios acreditan autorización, monto, fecha y fuente. Tesorería registra el abono cuando ocurra. |
| H5 | D1 dejó calendario y texto de confirmación. D2 verificó que H5 conserva M12 y 10 % del precio de implementación, CLP 461.880.281,50 netos. Si la factura válida se recibe el 31-01-2028, 15 días vencen el 15-02-2028 y 30 días el 01-03-2028. | Curimón confirma plazo y día previsto de acta/recepción. Conforme al Art. 18, el acta suscrita acredita la aceptación y existe un plazo de revisión de diez días hábiles. D1 incorpora luego la fecha efectiva del acta, recepción y abono. Si se desplaza el acta fuera de M12, D2 revisa también el mes de factura y el entero de IVA. |
| Cobertura de atraso | D2 dimensionó el puente por tramos, comparó desembolso único y probó reserva en M9 o M12. El expediente registra repago y costo, manteniendo la factura H5 y la venta del caso base. | Banco y socios acreditan el monto neto de cada tramo y la condición de pago por H5/H7. La línea de CLP 50 millones queda fuera del financiamiento requerido en estos escenarios. Si se decide invocarla como contingencia, D1 obtiene contrato y prueba cupo, tiempos de giro, tasa y vigencia. |
| Caja dentro del mes | D2 desglosó anticipos, abonos, IVA, costos, intereses, reserva, comisión y amortización de los meses críticos. Se probó el orden adverso con los pagos antes de los cobros del mes. | D2/D4 obtienen vencimientos por orden, proveedor, nómina, garantías e IVA. D1/Tesorería obtienen fechas valor del banco y Curimón. Completar el registro, ordenar los movimientos y conciliar con la serie mensual antes de acreditar cobertura. |

**Evidencia revisada.** Git `c9a6515652c3357ea684bf0bb9338b7c4ec028fd`, la revisión local 2.1 y los tickets AUD-5, 17, 18, 20, 22 y 38 con 29 comentarios. El cierre de AUD-20 concierne a la integración de supuestos. En el material revisado no apareció una carta bancaria ejecutable, un compromiso de socios por los montos recalculados ni una aceptación de Curimón del plazo de H5. Los adjuntos con evidencia de cálculo de AUD-22 están representados por el paquete versionado. [AUD-5][aud5] · [AUD-18][aud18] · [AUD-20][aud20] · [AUD-22][aud22] · [AUD-38][aud38]

## Prueba de los 56 cierres mensuales

| Escenario | Capital total CLP | Caja M12 CLP | Caja M13 CLP | Interés bancario CLP | Reembolso del puente CLP |
|---|---:|---:|---:|---:|---|
| Base profesor con H5 en M12 | 332.814.380 | 398.979.765 | 333.607.118 | 47.925.271 | — |
| Tesorería con H5 en M13, sin reserva ni cargos de estrés | 493.472.150 | 10.000.000 | 364.581.936 | 49.082.007 | 128.526.216 en M13 |
| H5 en M13, reserva M12, tramos | 648.481.475 | 10.000.005 | 491.878.089 | 57.060.029 | 252.533.676 en M16 |
| H5 en M14, reserva M12, tramos | 716.732.330 | 78.250.860 | 10.000.003 | 59.025.653 | 307.134.360 en M16 |
| H5 en M14, reserva M9, tramos | 720.054.565 | 78.274.780 | 10.000.003 | 62.419.649 | 309.792.148 en M16 |
| H5 en M14, reserva M12, reembolso inmediato tras H5 | 865.033.195 | 226.551.725 | 157.233.102 | 55.632.767 | 425.775.052 en M14 |
| H5 en M14, reserva M9 o M12, desembolso completo M1 | 749.966.520 | 78.490.146 | 10.000.003 | 107.995.179 | — |

Todos los casos del cuadro mantienen cero giros y cero saldo de línea. La prueba combinada incluye reserva D4 de CLP 152.699.775, compra condicional de 72 h por CLP 2.016.000 en M6–M9, comisión ilustrativa y CLP 114.000 mensuales de IVA de calibración en M13–M15. El escenario de desembolso único exige CLP 599.973.216 bancarios y CLP 149.993.304 de socios en M1. El desembolso por tramos permite pagar menos intereses que girar todo en M1. Pagar el puente en cuanto entre H5 reduce intereses y exige un tramo mayor en M12, porque M15 vuelve a estrechar la caja.

D2 reprodujo dos referencias de la revisión 2.1 con CLP 400 millones sobre el capital anterior y línea disponible. Con pago a 15 días M12 cierra en CLP 8.957.065. Con pago a 30 días M13 llega a **−CLP 8.989.379** tras usar el tope de la línea. Las pruebas nuevas mantienen CLP 10 millones como piso. En el atraso aislado hasta M14, la Fila A a precio fijo da VAN de CLP 1.226.784.192 y TIR de 82,6294 % mensual. El aumento de deuda se refleja en caja financiada. [Bases, Art. 18 y E-24/E-25][bases] · [Cotejo versionado][cotejo]

## Prueba de fechas y criterio de cierre

Para la alternativa por tramos con H5 en M14, ordenar todos los egresos operativos y tributarios antes de los cobros de cada mes arroja un mínimo de **−CLP 264.818.765 en M13**. Alcanzar CLP 10 millones bajo ese orden exigiría adelantar cobros, diferir pagos o disponer de **CLP 274.818.765 adicionales en ese momento**, antes de su costo financiero. Esta cifra mide el faltante bajo un orden adverso al aplicar los tramos y sirve para revisar facturas y fechas. El modelo también calcula una cota si se financia desde M1 todo el orden adverso: **CLP 1.052.310.610** para H5 en M14 y reserva en M12, con 80/20 y el costo simulado desde M1. Los cierres mensuales del cuadro principal validan el monto por mes. La fecha valor de cada movimiento determina si se necesita refuerzo adicional.

Con el [registro de fechas](tesoreria-fechas-por-acreditar.csv), D2 debe separar cada grupo de egresos en partidas documentadas que sumen su monto de control. Registrar fecha valor, importe con signo, documento y orden dentro del día. En cada mes, partir del saldo de apertura de la serie D1/D2, sumar cobros y abonos y restar egresos, impuestos, intereses y amortizaciones en el orden acreditado. El saldo tras el último evento debe coincidir con el cierre mensual. D1 verifica que cada partida de financiamiento tenga respaldo, que el saldo diario permanezca cubierto y que M9/M12/M13 conserven la holgura acordada. Todo cambio de fecha, cotización o comisión exige una nueva corrida. [Serie D1/D2](flujo-mensual-d1-d2.csv)

## Textos para solicitar los respaldos

**Banco y tesorería.** «Solicitamos una propuesta de financiamiento para el proyecto TFEP-01/2026 de Transportes Curimón, con un desembolso bancario inicial neto de CLP 266.251.504 antes del primer egreso de febrero de 2027 y una facilidad contingente de hasta CLP 309.792.148 netos, con giros alternativos en octubre de 2027 y enero de 2028 según el cuadro adjunto. El modelo prevé amortizar el préstamo inicial en M21 y el tramo contingente desde M16 según el cobro de H5 y H7. Agradecemos indicar monto desembolsable, disponibilidad, fecha valor, plazo y condiciones de giro, tasa y base de devengo, todas las comisiones, garantías y calendario de amortización.»

**Socios.** «Se solicita formalizar un aporte de CLP 66.562.876 antes del primer egreso contractual y un compromiso contingente de hasta CLP 77.448.037, conforme a los tramos alternativos de octubre de 2027 y enero de 2028. El acuerdo debe indicar monto, responsables, fecha y mecanismo de abono.»

**Curimón.** «Para planificar la tesorería de TFEP-01/2026, solicitamos confirmar la fecha prevista de revisión y suscripción del acta de H5, el procedimiento de recepción de la factura válida y el plazo de abono. Proponemos emitir la factura al suscribirse el acta y recibir el pago dentro de 15 días corridos desde su recepción. Agradecemos confirmar el plazo, la fecha estimada de recepción y el vencimiento previsto.»

## Verificación y archivos

- [Flujo mensual reproducido](flujo-mensual-d1-d2.csv). Diez escenarios, M1–M56 más M57, saldos de deuda, intereses, abonos y montos antes de cobros.
- [Calendario para acreditar fechas](tesoreria-fechas-por-acreditar.csv). Incluye vencimiento provisional de H5 y fechas objetivo para tener fondos disponibles. Las columnas de confirmación quedan para el respaldo documental.
- [Importes y supuestos del cálculo](dimensionamiento.json) y [script de reproducción](../acreditar_fondos.py). El script toma los valores del Excel versionado, conserva el precio y contrasta el resultado contra el escenario previo. Se ejecuta desde el repositorio con `python -B -X utf8 outputs/informe3-integral/acreditar_fondos.py` y el entorno con openpyxl y Pillow.
- Registro de uso de IA para A-6: auditoría de fuentes, dimensionamiento de capital y deuda, reconstrucción de flujos, pruebas de caja y redacción de borradores. La puesta en producción en Excel y la revisión humana quedan para el responsable una vez que haya evidencia. Los respaldos externos, los abonos y el acuerdo de Curimón están pendientes.

[bases]: https://github.com/mvergaral/audIT/blob/c9a6515/texto/FEP01_26_Bases_Administrativas_TFEP_01_2026_3.md
[cotejo]: https://github.com/mvergaral/audIT/blob/c9a6515/Informe-3/COTEJO-CIERRE.md
[aud5]: https://linear.app/audit-fep/issue/AUD-5
[aud18]: https://linear.app/audit-fep/issue/AUD-18
[aud20]: https://linear.app/audit-fep/issue/AUD-20
[aud22]: https://linear.app/audit-fep/issue/AUD-22
[aud38]: https://linear.app/audit-fep/issue/AUD-38
