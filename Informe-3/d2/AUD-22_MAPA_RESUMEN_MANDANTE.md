# Mapa para integrar la hoja Resumen del mandante

Este mapa identifica las celdas fuente del modelo actual. Las celdas destino se identifican cuando llegue el original, conservando filas, rótulos, orden y fórmulas de «Resumen».

| Concepto | Origen en D2 | Control |
|---|---|---|
| Precio neto de implementación | Parámetros B14 | Cuadra con los doce hitos E-25 y con el reparto 60/40. |
| Precio neto de operación | Parámetros B15 × B16, más variables si se incorporan | Cuadra con 36 servicios. La última mensualidad se factura M56 y se cobra M57. |
| Costos netos | Costos K2:K57 | Verificar clasificación por fase y componentes. Mantener compras del mandante fuera del costo audIT. |
| Facturación y cobros | Flujo de Caja E2:F57 y F58 para conciliación | Conciliar la diferencia con el cobro pendiente M57. |
| Caja y línea | Flujo de Caja W57 e Indicadores B5:B6 | Verificar tope, déficit y saldo al cierre. |
| Curva S | Curva S A2:D57 | Conciliar costos con intereses, facturación y caja financiada. |
| Fila A para D1 | Flujo de Caja H2:H57 y M0 = 0 | Exportar desde el mismo Excel. M57 es auxiliar. |
| VAN, TIR y sensibilidad | Resultados validados por D1 sobre la Fila A entregada | Registrar versión del flujo y devolver las cifras validadas a Indicadores. |

Con el original disponible, identificar celdas y nombres definidos, enlazar las cifras sin sobrescribir rótulos, verificar las conversiones a UF y USD con E-24 y regenerar el paquete de D2.
