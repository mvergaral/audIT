# Informe 3 · Comparación de 3.0 y 3.1

**Decisión recomendada: usar 3.1 como base de trabajo y defensa de la oferta.** 3.1 reconoce el costo de personal que audIT todavía debe cubrir y muestra el ahorro de madurez como una sensibilidad verificable. A igual venta, baja el margen EBITDA del 18,50 % al 16,59 %, pero sigue cumpliendo el tope del 20 %. La cota previa a cobros queda CLP 4,50 millones por debajo del piso interno, por lo que la versión sirve como base económica y requiere cerrar la tesorería antes de liberar la oferta.

La comparación toma como referencia el paquete de [Entrega 3.0 del 14 de noviembre de 2026](Entrega-3.0/) y usa el paquete vigente de [Entrega 3.1 del 15 de noviembre de 2026](Entrega-3.1/), con las curvas en vertical. Se contrastaron valores y fórmulas de ambos Excel y se cotejaron informe, presentación y manifiestos. Los importes se expresan en millones de CLP salvo indicación contraria. Las diferencias se calculan como 3.1 menos 3.0, antes del redondeo.

## Gráficos locales

| Gráfico | Cómo se lee |
|---|---|
| [01 · Quiebres de costo y financiamiento](Graficos-locales/01-quiebres-costo-y-financiamiento.png) | Costo del proyecto por mes, interés y principal del préstamo. El costo distingue personal, montaje externo, otra infraestructura y servicios y otras partidas netas. |
| [02 · Implementación, M0–M21](Graficos-locales/02-curva-implementacion-M0-M21.png) | Facturación ajustada y caja neta de IVA desde CLP 730 millones en M0. Incluye el mes de transición M21, con H12, primera factura de operación y pago del préstamo. El panel inferior muestra el costo mensual y el interés. |
| [03 · Operación, M21–M56](Graficos-locales/03-curva-operacion-M21-M56.png) | Acumulados atribuibles al servicio desde el cierre de M20. Se emplean facturas y cobros de operación y se imputa la garantía de M21 a implementación. La línea naranja es el flujo neto acumulado generado por el servicio, sin saldo inicial del proyecto, H12, deuda ni IVA. En el panel mensual, 3.1 con madurez reproduce el costo de operación de 3.0. |

### Quiebres que explican los gráficos

| Mes | Qué se mueve en 3.1 | Respaldo en la planilla |
|---|---|---|
| M3 | De M2 a M3 el costo neto sube de 77,28 a 205,61. Aumentan nómina en 41,60 y D4, montaje y energía en 85,90, principalmente por adquisiciones D4. | `Costos!B3:K4`, `Detalle proveedores D4` en M3 |
| M7–M10 | Se presupuestan 60, 60 y 52 montajes externos en M7, M8 y M9 por 3,78, 3,78 y 3,43, en total 10,98. Desde M10 este proveedor deja de sumar un cargo. El costo total baja 30,29 entre M9 y M10. De esa baja, 26,85 son de nómina del proyecto y 3,43 son el pago de montaje que termina. Hay otros movimientos netos por aproximadamente 0,01. audIT conserva trabajo interno de integración y recepción y el modelo mantiene personal técnico para la marcha blanca. | `Instalación por lote!A7:J21`, `Costos!B10:K11`, `Conciliación técnica!A17:E18` |
| M13 | Mayor costo neto mensual, 226,21. El salto frente a M12 combina nómina, licencias por 11,59, seguros y garantías periódicas por 11,00 y desembolsos D4. | `Costos!B13:K14`, `Gastos Administrativos` en M13 |
| M18–M21 | La nómina baja de 168,64 en M17 a 143,26 en M18, 125,44 en M19–M20 y 65,84 en M21. El costo neto total pasa de 156,69 en M20 a 102,52 en M21, incluidos 6,66 de comisión de garantía imputada a implementación. | `Costos!G18:K22`, `Costos!M22`, `Dotación por perfil` |
| M21–M22 | M21 tiene **584,00 de principal más 5,256 del último interés**. Desde M22 ambos cargos bancarios quedan en cero. En M21 entran 443,74 de H12 y la primera factura de servicio se cobra en M22. Por eso la caja neta cae 248,03 entre el cierre M20 y M21, mientras el costo neto del proyecto baja. El principal figura en el flujo de financiamiento. | `Flujo de Caja!E22:F23,P22:Q23,U22:V23,AA21:AA23`, `Financiamiento!E22:K23` |
| M25, M37 y M49 | Picos del costo operativo de 109,37, 109,63 y 109,88. Coinciden 5,01 de licencias con 11,00 de seguros y garantías periódicas, además de variaciones de infraestructura. La nómina base queda en 61,92 al mes desde M25. | `Costos!B26:K26,B38:K38,B50:K50`, `Gastos Administrativos`, `Proveedores` |
| M25, M33 y M45 | El escenario por madurez reduce software, datos y QA. La diferencia mensual con la base, incluido overhead, es 2,28, 4,57 y 6,85 respectivamente a partir de cada escalón. El piso de cobertura y N1 internalizado siguen en el escenario. | `Contrato de soporte!C8:D10`, `Escenarios corregidos!E808:F863` |
| M52–M56 | En M52 hay 0,215 de licencias. Calidad suma 2,00 en M53 y 3,50 en M54. En M56 el costo llega a 107,46, con 13,80 por cierre de coberturas y 1,00 por borrado y disposición final dentro de D4. Se factura el último mes de servicio en M56 y se cobra en M57. | `Costos!B53:K57`, `Gastos Administrativos`, `Detalle proveedores D4`, `Indicadores!B8` |

## Diferencias económicas

| Indicador | 3.0, base de comparación | 3.1, caso base | Diferencia |
|---|---:|---:|---:|
| Venta neta de implementación | 4.437,41 | 4.437,41 | 0,00 |
| Venta neta de operación | 4.036,55 | 4.036,55 | 0,00 |
| Venta neta total | 8.473,96 | 8.473,96 | 0,00 |
| Costo neto de implementación | 3.616,49 | 3.623,04 | +6,55 |
| Costo neto de operación | 3.289,79 | 3.445,16 | +155,37 |
| Costo neto total | 6.906,28 | 7.068,20 | +161,92 |
| EBITDA | 1.567,68 | 1.405,77 | −161,92 |
| Margen EBITDA sobre ventas netas | 18,50 % | 16,59 % | −1,91 pp |
| Utilidad sobre costo en `RESUMEN!M9` | 22,70 % | 19,89 % | −2,81 pp |
| VAN de Fila A, M1–M56 | 1.076,60 | 970,71 | −105,89 |
| VAN con cobro M57 | 1.139,26 | 1.033,37 | −105,89 |
| TIR mensual de Fila A | 71,5500 % | 70,9938 % | −0,5562 pp |
| Tasa mensual de descuento | 1,0262 % | 1,0262 % | 0 pp |
| Recuperación descontada sostenida | M17 | M17 | 0 |
| Venta neta de equilibrio para VAN cero | 7.081,70 | 7.218,64 | +136,94 |
| Capital inicial, banco y socios | 730,00 | 730,00 | 0,00 |
| Interés bancario total | 105,12 | 105,12 | 0,00 |
| Giro de línea en base | 0,00 | 0,00 | 0,00 |
| Caja mínima al cierre de mes, M9 con IVA | 216,96 | 210,41 | −6,55 |
| Caja mínima al cierre de mes, M9 neta de IVA | 280,45 | 273,90 | −6,55 |
| Cota mínima antes de cobros, M10 | 22,05 | 15,50 | −6,55 |
| Caja de tesorería al cierre de M56 | 1.410,29 | 1.248,38 | −161,92 |
| Cobro pendiente en M57 | 112,13 | 112,13 | 0,00 |

Fuentes en ambos libros: `RESUMEN!C6:C8,H6:H8,M8:M9`, `Indicadores!B2:B15`, `Control de entrega!B2:B21`, `Financiamiento!B2:L58` y `Flujo de Caja!W57`. La inyección de M1 son 584,00 de deuda y 146,00 de socios. El interés de 5,256 se carga en M2–M21, y la comisión bancaria de 0,25 se registra en M1. Los tipos presupuestarios del E-24 son CLP 40.000 por UF y CLP 900 por USD.

### Costo mensual y origen de la caída del EBITDA

La venta queda fija para comparar los dos paquetes. Cambian únicamente el costo de personal y su overhead del 2 % dentro de administración. El gasto del proveedor de montaje es el mismo en las dos versiones. La diferencia por montaje es la nómina que 3.0 descontaba y que 3.1 mantiene mientras falte respaldo de un egreso evitable.

| Meses | Cambio de 3.1 | Diferencia neta por mes | Total del grupo |
|---|---|---:|---:|
| M1–M6, M10–M24 | Mismo costo mensual | 0,00000 | 0,00000 |
| M7 y M8 | Restituye nómina atribuida al montaje físico y overhead | +2,28480 cada mes | +4,56960 |
| M9 | Restituye nómina para 52 kits y overhead | +1,98016 | +1,98016 |
| M25–M32 | Base al 100 % frente al 75 % de 3.0 en el bloque variable | +2,28480 | +18,27840 |
| M33–M44 | Base al 100 % frente al 50 % de 3.0 en el bloque variable | +4,56960 | +54,83520 |
| M45–M56 | Base al 100 % frente al 25 % de 3.0 en el bloque variable | +6,85440 | +82,25280 |
| Total | Nómina y overhead | | **+161,91616** |

- Montaje: 172 kits × 140 minutos corresponden a 401 h 20 min. A CLP 16.000/h más overhead, explican **CLP 6.549.760**.
- Madurez: el bloque variable a carga completa cuesta CLP 8.960.000 por mes, antes de overhead. Sustituir las rebajas automáticas por carga completa en la base explica **CLP 155.366.400**. El escenario por madurez de 3.1 conserva el costo de montaje de 3.1. A igual precio llega a un EBITDA de **CLP 1.561,13 millones**, un margen de **18,42 %** y un VAN de **CLP 1.070,56 millones**. La brecha restante frente a 3.0 se explica por montaje.

El detalle íntegro para los 56 meses está en [Variación mensual de Entrega 3.1](Entrega-3.1/Variacion-mensual.csv). Las fórmulas de origen están en `Costos!E:K`, `Parámetros corrección!B16,B59,B70`, `Instalación por lote!E:K` y `Contrato de soporte!C8:D10`.

## Cambios de modelo y trazabilidad

| Tema | 3.0 | Cambio en 3.1 |
|---|---|---|
| Precio de implementación y operación | Precio calculado desde costo y margen objetivo. | Conserva CLP 4.437,41 millones de implementación y CLP 112,13 millones por mensualidad como referencia. El selector `Parámetros corrección!B62` permite probar el recálculo. |
| Hitos y mensualidades | Hitos y lógica de servicio incorporados al flujo. `Control de entrega!B8` contenía el número 36 fijo. | `Calendario E25` alimenta `Ingresos!G:K`. Se calculan facturas y cobros por separado. Los 12 hitos y los 36 meses se concilian con inicios y desfases editables, 36 facturas emitidas y último cobro M57. H12 y la primera factura de operación ocurren ambos en M21. |
| Garantía de M21 | La garantía ya estaba presupuestada e imputada a implementación. | Explicita el mes y la fase en `Costos!M22` y los vincula a `RESUMEN`. Se mantiene su pago en M21. |
| Flujo e indicadores | Caja y VAN base más M57. | Amplía la planilla de M57 a M62. `Flujo de Caja!AH` verifica la identidad de caja e `Indicadores!B8` suma los cobros posteriores a M56. Se prueban M58, cambios de duración e inicio y ajustes sobre la última factura. |
| Dotación y EDT | Consigna dotación y brechas por perfil. Imputa las horas evitables de montaje. | `Conciliación técnica` explicita la brecha entre 17.600 h de T-15 y 6.008 h de A09, y deja pendientes la nivelación semanal, M18–M20 y las tarifas de Funcional e Implantación. `Dotación por perfil` aplica solo la fracción demostrable de sustitución. |
| Montaje y altas satelitales | Calendario de 182 kits, 10 piloto y 172 externos, con compras y altas valorizadas. | `Instalación por lote` permite mover lotes y concilia inventario. `Activaciones` deriva altas, equipos activos, Iridium y LTE. Se documenta la diferencia entre 182 previstos en M9 y 164 de S7. El proveedor termina en M9 en ambos casos. |
| Infraestructura y administración | Tarifas y montos por proveedor y pagador. | Enlaza más partidas de conectividad a los equipos activados y hace explícito el overhead sobre personal. Los presupuestos de hardware del mandante, licencias, calidad, cierre y proveedores conservan su magnitud. |
| Operación y madurez | Factores 75 %, 50 % y 25 % aplicados desde M25, M33 y M45 en base. | La base conserva el 100 % del bloque variable. `Soporte por perfil` permite aplicar los escalones mediante `Parámetros corrección!B70`. Se muestran condiciones de demanda, concurrencia, incidentes y SLA. |
| Mesa N1 | Mesa interna y suplencias en `Contrato de soporte`. | Mismo costo interno de CLP 17,92 millones mensuales antes de overhead. Se agrega `Mesa de ayuda` para comparar una cola compartida y una mesa dedicada con egreso evitable, abono, excedencias, herramientas, supervisión y transición. Los valores de comparación comercial siguen pendientes. |
| Sensibilidad | Siete pruebas publicadas de H5, reserva, facilidad y choques. | Quince pruebas. Se agregan H4 con y sin línea, facilidad M9, atraso de acta H4, atraso de H12, soporte a carga completa, madurez y amortización en cuotas. Incluye faltante frente al piso, comisiones, caja al cierre M56 y cobros posteriores. |
| Curva S | Vista contractual del costo con intereses, facturación y caja. | Agrega series auxiliares M0–M56 en `Gráficos UF!P:S` y presenta en el informe y las láminas el presupuesto base y la madurez con capital inicial. Se conserva la vista contractual en la Figura 3 y Excel. |
| Controles y formato | 40 hojas. Hojas críticas protegidas. | 44 hojas, sin eliminar hojas de 3.0. Se agregan `Calendario E25`, `Activaciones`, `Conciliación técnica` y `Mesa de ayuda`. Se amplían validaciones y los controles de facturación, cobro, inventario, saldo de deuda e identidad de caja. Persisten entradas editables sin validación en `Contrato de soporte!D2:D13` y `Parámetros D2!B5:B9`. |

Los siete escenarios comunes también cambian de resultado. La comparación siguiente usa la **cota antes de cobros**, que captura el riesgo de secuencia de pagos bajo el supuesto conservador de la planilla.

| Prueba | Cota 3.0 | Cota 3.1 |
|---|---:|---:|
| H5 cobrado M13 | −233,42 | −239,97 |
| H5 cobrado M14 | −233,42 | −239,97 |
| H5 M14 + reserva M12 | −337,62 | −344,17 |
| H5 M14 + reserva + facilidad | 22,05 | 15,50 |
| Costos +5 % | −63,25 | −70,13 |
| Cobros −5 % | −43,96 | −39,97 |
| Reserva anticipada M9 | 21,54 | 14,99 |

En 3.1, retrasar H4 a M11 deja una cota de **−261,08**. El caso con línea habilitada arroja el mismo mínimo porque el giro depende del saldo mensual del modelo y no cubre automáticamente ese faltante previo a cobros. Si también se atrasa el acta y la factura, la cota es **−176,76**. Una facilidad adicional de 420,00 en M9 eleva la cota de H4 a **152,63** en el escenario. Esa facilidad está condicionada a disponibilidad y desembolso previo a los pagos. Para las cuotas desde M21 el interés total pasa de 105,12 a **113,00**. [Planilla 3.1, `Sensibilidad!A2:AE16`](Entrega-3.1/INFORME3_AUDIT_PLANILLA_20261115.xlsx)

### Inventario de hojas comunes

La revisión por coordenada detectó cambios de fórmulas o contenido en **19 de las 40 hojas de 3.0**. Los resultados recalculados pueden cambiar en hojas con fórmulas iguales. La enumeración cubre cambios de contenido y resultados del modelo, y omite estilos, representación interna del archivo y redondeos de caché.

| Grupo | Hojas con cambios de contenido y ámbito |
|---|---|
| Ventas, parámetros y costos | `RESUMEN`, `Parámetros D2`, `Costos`, `Ingresos`, `Hitos E25`, `Parámetros corrección`. Cambian los vínculos a precio, garantía, calendario, escenarios e inventario. |
| Tesorería y control | `Flujo de Caja`, `Indicadores`, `Financiamiento`, `Sensibilidad`, `Escenarios corregidos`, `Control de entrega`, `Resumen Ejecutivo`. Cambian la cola, los escenarios, los indicadores referenciados o sus controles. |
| Personal, compras y gastos | `Detalle proveedores D4`, `Gastos Administrativos`, `Dotación por perfil`, `Instalación por lote`, `Soporte por perfil`. Cambian enlaces, criterios de cálculo o glosas de presupuesto. |
| Visualización | `Gráficos UF`. Se agregan el desglose mensual y las columnas de curvas con apertura en M0. |

## Cambios de informes y paquete

| Entregable | Cambio de 3.0 a 3.1 |
|---|---|
| PDF económico | Pasa de 27 a 28 páginas. La resolución de observaciones del Art. 46 se mueve del folio 7 al 19, después del cuerpo económico. Los estados técnicos abiertos quedan explícitos. Se actualizan los totales, el cuadro de personal, las pruebas de tesorería y las referencias. La Figura 1 superpone el punto de partida de facturación ajustada y caja en cada caso en dos paneles verticales. La Figura 3 muestra las series contractuales. |
| Presentación PDF y PPTX | Pasa de 10 a 11 láminas y de 4 a 5 gráficos editables. La lámina 2 toma las nuevas magnitudes. La 3 explicita la nómina conservada con el proveedor de montaje. La 4 desglosa costos. Las láminas 5 y 6 muestran base y madurez, cada una con apertura común. La lámina 7 compara H4 y H5, la 8 separa amortización, la 9 muestra el caso base de soporte, la 10 mantiene costo y valor de innovaciones y la 11 mantiene la demostración. |
| Prototipo | 3.1 hace explícito que la URL pública corresponde al despliegue previo. Los cambios locales de razón social y rótulos requieren reflejarse en el sitio público. La revisión humana sustantiva y el registro A-6 se declaran pendientes. |
| LEEME, manifiesto y ZIP | 3.1 incorpora un registro de mejoras, el CSV mensual, sumas SHA-256 para los archivos y para la línea base, resultados de verificación y un ZIP con el juego de entrega. Los gráficos de este análisis se guardan en `Graficos-locales`. |

Fuentes: [Informe 3.0](Entrega-3.0/INFORME3_AUDIT_COSTOS_VENTA_20261114.pdf), [Informe 3.1](Entrega-3.1/INFORME3_AUDIT_COSTOS_VENTA_20261115.pdf), [presentación 3.0](Entrega-3.0/INFORME3_AUDIT_PRESENTACION_20261114.pdf), [presentación 3.1](Entrega-3.1/INFORME3_AUDIT_PRESENTACION_20261115.pdf) y [registro de entrega](Entrega-3.1/Registro-de-mejora.md).

## Decisión para la oferta

**Quedarse con 3.1 y usar 3.0 como referencia de costo.** El menor EBITDA de 3.1 reconoce dos ahorros que 3.0 daba por disponibles. El primero exige demostrar que el proveedor de montaje evita un egreso interno. El segundo exige evidencia de demanda y capacidad para retirar horas contratadas sin afectar la cobertura. Si esas condiciones se cumplen, la planilla 3.1 ya permite incorporar el ahorro de forma trazable. El escenario de madurez, cuyo ahorro arranca en M25, deja intacta la cota de M10.

La prioridad para cerrar la oferta es acreditar las fechas de H4/H5, los fondos y el orden de los pagos. Para alcanzar el piso interno en el caso base se requieren **CLP 4,50 millones adicionales de caja disponible antes de cobrar en M10**, o cambiar pagos por el mismo efecto neto. Ese monto cubre el desfase del caso base y debe evaluarse aparte de la contingencia de atraso H4. También faltan respaldar la ejecución de los lotes, resolver las validaciones de entrada y cerrar la revisión humana y del prototipo.

Mantener el N1 interno como costo base mientras las referencias públicas carezcan del precio para el alcance completo. La opción externa puede incorporarse si demuestra cobertura, SLA y ahorro sobre el gasto interno efectivamente evitable. [Análisis de externalización N1](Analisis-externalizacion-N1.md)
