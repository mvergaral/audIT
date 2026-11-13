# AUD-20 · Conciliación de caja y última mensualidad

E-25 establece que la operación se paga en los primeros días del mes siguiente al servicio vencido. Para el cierre, **la mensualidad del servicio M55 se cobra en M56 y la de M56 se cobra en M57**, sujeto a los ajustes contractuales. El horizonte de evaluación de E-24 termina en M56. Se usa M57 como conciliación posterior al horizonte para seguir la cuenta por cobrar y cualquier deuda de cierre.

| Registro | M56 · septiembre de 2031 | M57 · octubre de 2031 |
| --- | --- | --- |
| Facturación de operación | Registrar la mensualidad del servicio M56 en la curva de facturación. | Cierre de la cuenta por cobrar al percibir el pago. |
| Cobros efectivos | Registrar el pago de M55 y cualquier otro cobro que efectivamente entre en M56. | Registrar el cobro de la mensualidad M56, neto de multas aplicables. |
| Garantía y seguro de cierre | Registrar la salida propuesta por D1 una sola vez: **CLP 13.800.000**, compuestos por CLP 10.800.000 de garantía y CLP 3.000.000 de seguro. | Conciliar el pago ya registrado en M56. |
| Evaluación de 56 meses | Escenario base de VAN/TIR con flujos efectivos de M1–M56. Mostrar la cuenta por cobrar como saldo de cierre y calcular por separado la sensibilidad de VAN con ajuste terminal. | Mostrar el cobro real en el calendario auxiliar y conciliarlo con la cuenta por cobrar de M56. |

## Control de liquidez

1. **Caja antes del pago extraordinario** = saldo inicial M56 + cobros efectivos de M56 − pagos ordinarios de M56. La caja se mide con importes efectivamente pagados, incluido el tratamiento de IVA que corresponda.
2. **Caja antes de financiamiento** = caja antes del pago extraordinario − CLP 13.800.000.
3. **Financiamiento puente requerido** = máximo entre cero y el déficit de caja. Verificar el mínimo de caja dentro del mes según el orden real de cobros y pagos, además del saldo al cierre.
4. **Capacidad de la línea** = CLP 50.000.000 menos el saldo ya utilizado. Si se usa la línea, calcular intereses al 3,0 % mensual sobre la utilización según su calendario y conciliar la amortización con la caja disponible en M57.

Si la caja después de cobros y pagos ordinarios fuera cero, se necesitarían **CLP 13.800.000** de puente. Un mes completo a 3,0 % supondría **CLP 414.000** de interés. Es una prueba de sensibilidad. El desembolso real depende de la caja, del orden de pagos y del saldo disponible de la línea.

El [CSV de egresos](AUD-17_EGRESOS_D4_2026-11-12.csv) contiene en M56 **CLP 29.303.130** del calendario D4 y **CLP 13.800.000** del escenario de D1. Suman **CLP 43.103.130** como egreso parcial de ese mes. Faltan los demás egresos, el cobro de M55, el monto de la última mensualidad y el saldo de apertura para determinar la caja y el puente.

Para la sensibilidad de VAN, el ajuste en M56 es **cobro esperado de M57 ÷ (1 + tasa mensual de evaluación)**, usando la misma base del flujo libre y los descuentos contractuales aplicables. El ajuste se agrega al último período únicamente en la evaluación de sensibilidad. El flujo financiado conserva las fechas efectivas. Si se incorpora M57 como flujo explícito en una conciliación ampliada, se usa el cobro de M57 una sola vez.

Fuentes: FEP01 · Formularios E-24 y E-25 · pp. 73–74. [D1, supuestos de cierre y financiamiento](https://github.com/mvergaral/audIT/blob/0712c7f/Informe-3/d1/ECONOMICO_SUPUESTOS_Y_PARAMETROS_D1.md) · [AUD-5](https://linear.app/audit-fep/issue/AUD-5) · [AUD-20](https://linear.app/audit-fep/issue/AUD-20).
