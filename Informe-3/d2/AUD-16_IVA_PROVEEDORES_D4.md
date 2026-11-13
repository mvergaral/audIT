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

## Partidas con IVA pendiente de determinar

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

El neto con IVA pendiente suma **CLP 1.412.111.668**, redondeado. Las baterías de reposición de M36 figuran en operación 4.3, por lo que el IVA referencial de la inversión inicial 4.1 no las cubre. La reserva de contingencia se controla en el escenario de sensibilidad. El personal y las licencias de GitLab y SonarQube se concilian en sus partidas de D2 y D3. [Proveedores D4 4.4](../d4/4.4-proveedores-clave.md) · [Operación D4 4.3](../d4/4.3-mantencion-operacion.md) · [Calendario D4 4.6](../d4/4.6-calendario-compras.md)

## Uso del respaldo mensual

El [CSV de proveedores](AUD-16_IVA_PROVEEDORES_D4.csv) contiene una fila por mes, pagador, partida y proveedor o canal referencial. Las filas de hardware conservan la fuente de precio de 4.1. Cuando D4 no identifica un canal adjudicado, el CSV conserva el canal de referencia o el proveedor pendiente. Los meses corresponden a la compra o al servicio presupuestado, con M1 en febrero de 2027. Se muestran netos con dos decimales y el IVA referencial en pesos enteros. Para equipos se redondea el total mensual al 19 % y se distribuye el residuo por los mayores restos entre sus filas. El total de netos redondeado por cada mes reproduce el calendario D4.

En M56 el flujo provisional registra CLP 29.303.129 para D4, un peso menos que el calendario, que muestra CLP 29.303.130. AUD-17 asigna a M56 el ajuste de redondeo para cuadrar el total contractual de D4. [Flujo AUD-17](AUD-17_FLUJO_INTEGRADO_PROVISIONAL.csv)

Los equipos de Curimón se muestran en la hoja informativa. Para ese pagador el CSV contiene CLP 42.822.998 de IVA referencial, calculado y redondeado por mes. Las unidades de prueba corresponden a audIT incluso cuando el mismo proveedor figura en las compras de Curimón. [Presupuesto D4 4.1](../d4/4.1-presupuesto-equipos.md) · [Asignación D4 4.8](../d4/4.8-compras-audit-y-mandante.md)

Mantener el interruptor de IVA de caja desactivado en el modelo de trabajo. Usar `iva_referencial_clp` para cotejar el bloque mensual D4 ya cargado y evitar sumar dos veces los mismos netos o su IVA. Completar `iva_pagado_clp` con respaldo y mes efectivo de pago. Completar `credito_fiscal_clp` cuando se verifique la procedencia y el mes aplicable, identificando emisor, receptor, documento y base. Las celdas vacías representan importes pendientes de verificar. [Modelo D2](D2_MODELO_TRABAJO.md)
