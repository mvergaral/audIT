# AUD-16 · Conciliación de IVA de proveedores D4

El calendario D4 sustenta CLP **1.526.997.751 netos** a cargo de audIT y CLP **225.384.199 netos** a cargo de Curimón. Para audIT se reproducen CLP **21.828.338 de IVA referencial** en equipos y SIM 5G. Los antecedentes disponibles son presupuestos, precios de lista y estimaciones. La factura, el pago y la procedencia del crédito fiscal quedan pendientes de respaldo. [Calendario D4 4.6](../d4/4.6-calendario-compras.md) · [Asignación de compras D4 4.8](../d4/4.8-compras-audit-y-mandante.md)

## IVA referencial a cargo de audIT

| Mes contractual | Equipos y unidades de prueba (CLP) | SIM 5G (CLP) | Total referencial (CLP) |
|---|---:|---:|---:|
| M1 | 1.852.500 | | 1.852.500 |
| M3 | 15.751.217 | | 15.751.217 |
| M4 | 3.548.341 | 12.760 | 3.561.101 |
| M5–M56 | | 12.760 por mes | 663.520 |
| **Total** | **21.152.058** | **676.280** | **21.828.338** |

D4 estima el IVA de equipos al 19 % del neto, según E-24. Los precios incluyen listas extranjeras y equivalentes presupuestarios. El IVA de caja requiere conocer el canal, la base aplicable, el documento de compra o de internación y la fecha de pago. Las SIM 5G usan un precio público de referencia de CLP 9.990 bruto por línea y ocho líneas desde M4. La diferencia mensual entre el bruto de CLP 79.920 y el neto calculado de CLP 67.159,66 da CLP 12.760 al redondear. D4 prevé dos operadores por gabinete y Entel solo identifica el precio de referencia. [E-24, FEP01 p. 73](../../texto/FEP01_26_Bases_Administrativas_TFEP_01_2026_3.md#L2400) · [Equipos D4 4.1](../d4/4.1-presupuesto-equipos.md) · [Conectividad D4 4.2](../d4/4.2-nube-conectividad.md)

## IVA modelado en la caja base

El flujo consolidado aplica la tasa E-24 a las siguientes partidas de audIT en el mes presupuestado del servicio. Es un supuesto conservador de caja, sujeto a verificar factura, emisor, receptor y fecha de pago. El crédito fiscal acreditado en el corte es CLP 0.

| Partida de origen en el CSV D4 | Canal | Meses | Base neta CLP | IVA de caja supuesto CLP |
|---|---|---|---:|---:|
| Circuito de operador ExpressRoute | Operador de circuito por seleccionar | M4–M56 | 47.700.000 | 9.063.000 |
| LTE a bordo | Operador móvil por seleccionar | M6–M56 | 28.260.000 | 5.369.400 |
| **Total audIT** | | | **75.960.000** | **14.432.400** |

Por mes y proveedor, multiplicar el neto de la fila por 19 % y redondear a pesos. ExpressRoute suma CLP 171.000 cada mes. LTE suma CLP 5.700 en M6 y CLP 103.740 en M12. El control de caja da CLP 171.000 en M4 y CLP 274.740 en M12. El puerto Azure de ExpressRoute pertenece al bloque Microsoft/CSP. La firma automática se controla en su propio bloque, con IVA referencial y sin cargo en la caja base.

## Partidas con tratamiento tributario por acreditar

| Proveedor o canal presupuestado | Partida | Meses | Neto (CLP, redondeado) | Evidencia por obtener |
|---|---|---|---:|---|
| Microsoft / canal CSP | Azure e identidad Entra | M1–M56; Entra M1, M13, M25, M37 y M49 | 863.430.586 | Entidad que factura, destinatario y desglose de impuestos. D4 indica que audIT paga el consumo y la suscripción queda a nombre del mandante. |
| Ground Control | Tiempo de aire Iridium | M6–M56 | 311.566.500 | Canal de contratación, entidad que factura y tratamiento del servicio. |
| Ground Control | Activación Iridium | M6–M9, M24, M36 y M48 | 5.783.400 | Facturación de las altas y tratamiento del cargo. |
| Operador móvil por seleccionar | LTE a bordo | M6–M56 | 28.260.000 | Cotización del plan M2M con precio neto, impuesto y destinatario. |
| Operador de circuito por seleccionar | Circuito ExpressRoute | M4–M56 | 47.700.000 | Cotización del operador. El puerto de Microsoft se incluye en Azure. |
| Fabricantes y mantenedores por desglosar | Soporte y mantención | M13–M56 | 146.604.800 | Contratos y desglose por emisor y concepto. D4 usa una estimación agregada de 12 % anual sobre el hardware. |
| Canales por confirmar; CDW para el precio de referencia de los paquetes | Reposición de baterías UPS | M36 | 4.766.382 | Cotización, canal y documento de compra o internación. |
| Proveedor por confirmar | Asesoría legal R-24 | M3 | 3.000.000 | Identidad y régimen del prestador, tipo de documento y monto afecto si corresponde. |
| Gestor autorizado por seleccionar | Borrado y disposición final | M56 | 1.000.000 | Cotización y factura con desglose. |

El neto de estas partidas suma **CLP 1.412.111.668**, redondeado. Incluye los CLP 75.960.000 de conectividad con IVA supuesto en caja. Las baterías de reposición de M36 figuran en operación 4.3, fuera del IVA referencial de inversión inicial. La reserva de contingencia se controla en sensibilidad. [Proveedores D4 4.4](../d4/4.4-proveedores-clave.md) · [Operación D4 4.3](../d4/4.3-mantencion-operacion.md) · [Calendario D4 4.6](../d4/4.6-calendario-compras.md)

## Uso del respaldo mensual

El [CSV de proveedores](AUD-16_IVA_PROVEEDORES_D4.csv) contiene una fila por mes, pagador, partida y proveedor o canal referencial. Las filas de hardware conservan la fuente de precio de 4.1. Cuando D4 no identifica un canal adjudicado, el CSV conserva el canal de referencia o el proveedor pendiente. Los meses corresponden a la compra o al servicio presupuestado, con M1 en febrero de 2027. Se muestran netos con dos decimales y el IVA referencial en pesos enteros. Para equipos se redondea el total mensual al 19 % y se distribuye el residuo por los mayores restos entre sus filas. El total de netos redondeado por cada mes reproduce el calendario D4.

En M56 el flujo provisional registra CLP 29.303.129 para D4, un peso menos que el calendario, que muestra CLP 29.303.130. AUD-17 asigna a M56 el ajuste de redondeo para cuadrar el total contractual de D4. [Flujo AUD-17](AUD-17_FLUJO_INTEGRADO_PROVISIONAL.csv)

Los equipos de Curimón se muestran en la hoja informativa. Para ese pagador el CSV contiene CLP 42.822.998 de IVA referencial, calculado y redondeado por mes. Las unidades de prueba corresponden a audIT incluso cuando el mismo proveedor figura en las compras de Curimón. [Presupuesto D4 4.1](../d4/4.1-presupuesto-equipos.md) · [Asignación D4 4.8](../d4/4.8-compras-audit-y-mandante.md)

El CSV conserva separados el IVA referencial, el pago efectivo y el crédito fiscal. Los campos `iva_pagado_clp` y `credito_fiscal_clp` se completan contra emisor, receptor, documento, base y mes efectivo. En el modelo, reemplazar el supuesto de conectividad por el pago confirmado correspondiente para evitar duplicar el cargo. [Modelo D2](D2_MODELO_TRABAJO.md)

## Conciliación por cobertura

| Universo presupuestario | Pagador | IVA referencial CLP | Tratamiento |
|---|---|---:|---|
| Equipos iniciales, unidades de prueba y SIM 5G | audIT | 21.828.338 | Referencia D4; requiere factura o internación y pago. |
| Firma automática | audIT | 4.722.710 | Piloto M13–M15: 14.050/mes. Desde M16: 114.160/mes. Referencia D3. |
| GitLab | audIT | 7.021.944 | 19 % de CLP 36.957.600, por renovación M1/M13/M25/M37/M49. |
| SonarQube | audIT | 204.250 | 19 % de CLP 1.075.000, por renovación M4/M16/M28/M40/M52. |
| Calibración INN-5 | audIT | 342.000 | Sensibilidad de CLP 114.000 en M13/M14/M15, condicionada al documento. |
| Hardware de campo y red | Curimón | 42.822.998 | Referencia D4 en la hoja informativa de Curimón. |

El subtotal histórico de CLP 69.374.046 comprende equipos/SIM de audIT, firma y hardware de Curimón. Las licencias aportan CLP 7.226.194 de referencia adicional; la calibración tiene un escenario separado. La resta entre la referencia histórica y los CLP 14.432.400 de conectividad combina partidas distintas y carece de significado como saldo fiscal. El modelo es antes de impuesto a la renta. Una proyección tributaria adicional requiere determinar régimen, base y calendario aplicables a audIT. [Licencias D3](../d3/3.2-licencias-herramientas.md) · [Firma D3](../d3/APORTE_COSTOS_SOFTWARE_DATOS.md) · [Cierre de caja](AUD-20_CIERRE_CAJA_M56_M57.md)
