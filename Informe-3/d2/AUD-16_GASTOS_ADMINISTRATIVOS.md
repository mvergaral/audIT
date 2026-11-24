# AUD-16 · Calendario administrativo D1

El CSV adjunto contiene **CLP 85.400.000** de egresos netos calendarizados adicionales al insumo conciliado D2. La suma parcial de ambos insumos es **CLP 1.717.980.351**. Los importes son referencias de presupuesto del paquete D1.

| Partida | Total CLP | Tratamiento |
|---|---:|---|
| Fiel cumplimiento, M1–M56 | 50.400.000 | Nueve períodos semestrales anticipados desde M1 a M49, y tramo M55–M56 prorrateado. Este último tramo supone que el banco permite el prorrateo. |
| Responsabilidad civil | 13.000.000 | Cinco primas anuales. |
| Ciberriesgo regular | 15.000.000 | Cinco primas anuales. |
| Notaría | 1.200.000 | Pago único en M1. |
| Custodia de fuentes | 5.800.000 | Alta en M6 y ocho cánones desde M12. |

La extensión de fiel cumplimiento y el endoso de cola ya están en el insumo D2 de M56 por CLP 13.800.000. El nuevo calendario conserva esa imputación. Las primas regulares y la cola se presupuestan según D1. El prorrateo de la última prima anual y cualquier crédito por superposición requieren revisar los términos de la póliza. Hasta contar con ellos se conserva el importe de D1 como presupuesto prudente.

## Partidas que requieren fórmula o base de imputación

- **Seriedad de la oferta.** Comisión referencial CLP 2.812.500 por 150 días. Registrar como costo preoperacional recuperable en precio. El escenario base mantiene M0 = 0 y muestra el efecto de asumir el pago como salida previa en una sensibilidad.
- **Correcto funcionamiento.** Comisión total de 0,15 % del precio de implementación. Se provisiona en el costo de implementación, con pago estimado en M21 al constituir la garantía.
- **Todo riesgo.** Aplicar 0,8 % anual al valor de reposición de los activos cubiertos, desde que se instalan. La base asegurable requiere identificar los activos y su cobertura.
- **Accidentes del trabajo.** Aplicar el supuesto D1 de 0,93 % a la remuneración imponible. Descontar lo ya incluido en la tarifa integral al conciliar el presupuesto de RRHH.
- **Overhead.** Imputar gerencia, administración, contabilidad y legal solo en la medida en que no estén incluidos en la dotación base o en la asesoría R-24. Identificar afectación y recuperabilidad de IVA por partida antes de cerrar caja.

## Conciliación por naturaleza para T-22

El [detalle mensual](AUD-16_CONCILIACION_NATURALEZA_T22.csv) reproduce el caso base auditado `c9a6515` contra `Costos!K2:K57`. Clasifica el gasto de audIT por naturaleza y conserva el mes de pago o cargo presupuestado. El registro de Proveedores permite seguir los gastos de terceros hasta Costos y su naturaleza. El hardware de campo y red de Curimón se informa aparte.

| Mes de caja | Inversión CLP | Operación CLP | Administración CLP | RRHH CLP | Total neto CLP |
|---|---:|---:|---:|---:|---:|
| M1–M20 | 111.326.621,00 | 462.041.469,00 | 39.200.000,00 | 3.144.828.000,00 | 3.757.396.090,00 |
| M21–M56 | 0,00 | 1.071.268.551,00 | 69.928.204,22 | 3.085.808.000,00 | 4.227.004.755,22 |
| **Total** | **111.326.621,00** | **1.533.310.020,00** | **109.128.204,22** | **6.230.636.000,00** | **7.984.400.845,22** |

Para reproducir cada fila, partir de `Costos` columnas B a H, J y L. En el detalle D4, inversión es la suma de `Equipos` y `Unidades de prueba` del pagador audIT. Reclasificar `Asesoría legal R-24` a administración en M3. En operación quedan el resto de D4 (incluido el ajuste de CLP −1 en M56 del calendario) y las columnas C, D, H y L. En administración se suman E, F, J y R-24. La columna G contiene RRHH. El control es la suma de las cuatro naturalezas menos la columna K y concilia los 56 meses al centavo.

La columna de fase presupuestaria del CSV sigue el corte M20/M21 del calendario de caja. La comisión de correcto funcionamiento se paga en M21 y pertenece al precio de implementación. Al reasignarla para el cuadro por fase comercial, implementación suma CLP 3.764.324.294,22 y operación CLP 4.220.076.551,00. Las horas de cierre de implementación 6.5 y 7.2 que se ejecutan M21–M24 se identifican por alcance, paquete de ejecución y mes, con costo incremental sujeto al cruce de capacidad. [Conciliación de capacidad](AUD-15_CONCILIACION_CAPACIDAD.md)

## Criterios para completar la cobertura

| Partida | Fórmula por mes y pagador audIT | Fuente de imputación y control |
|---|---|---|
| Gerencia y administración | Horas dedicadas × costo horario integral, más servicios externos directos | Obtener matriz de cargos y remuneraciones de AUD-17; separar dedicación directa a EDT de funciones corporativas. Descontar lo incluido en RRHH. |
| Contabilidad y legal | Horas internas no incluidas × tarifa, más honorarios externos imputables | Identificar asesoría, contrato, proveedor, documento y mes. R-24 ya contiene CLP 3.000.000 y se imputa una vez en M3. |
| Todo riesgo | Base de reposición cubierta × 0,8 % anual × meses de exposición/12, ajustado a la forma de pago cotizada | Art. 38 exige cubrir equipos provistos u operados en instalaciones del cliente. Identificar activo, valor de reposición, titular, aceptación, inicio de cobertura y prima. El 0,8 % es referencia D1. |
| Accidentes y responsabilidad patronal | Remuneración imponible por persona y mes × tasa aplicable, menos la cotización incluida en tarifa integral | Conciliar liquidaciones, tasa aplicable y póliza. El 0,93 % del paquete D1 es un supuesto de cálculo. |
| Garantías y seguros | Aplicar el calendario y las bases de la tabla anterior, con fecha de emisión y pago | Confirmar comisiones, prorrateos y endosos. En M56 hay una sola salida de CLP 13.800.000; cotejar su composición con la cobertura de la prima de M49. |

Los importes pendientes de evidenciar se controlan como brechas, con costo adicional por determinar. La comisión de seriedad se prueba en M0 por separado. Los intereses de deuda y línea se tratan como financiamiento.

Fuentes: paquete económico D1 integrado en main, FEP01 artículos 35–38, 68 y 84.6 y aclaraciones de gastos administrativos. [AUD-16](https://linear.app/audit-fep/issue/AUD-16) · [AUD-20](https://linear.app/audit-fep/issue/AUD-20).
