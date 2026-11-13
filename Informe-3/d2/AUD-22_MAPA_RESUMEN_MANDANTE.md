# Mapa para integrar la hoja Resumen del mandante

Se integró «FLUJO DE CAJA - VACIO.xlsx», con SHA-256 `07a9b45003d04e4b161cde07a6839bb89627bf566490da90e21c21da0a154a2c`. Se comparó con el ejemplo con datos. El archivo vacío comparte su estructura y usa las conversiones de E-24. La copia [D2_RESUMEN_MANDANTE.xlsx](D2_RESUMEN_MANDANTE.xlsx) conserva las fórmulas, celdas combinadas, rótulos y orden de «RESUMEN».

La hoja «PUENTE D2» carga los subtotales del modelo de trabajo. El puente asigna las tarifas de implementación en proporción al costo y conserva la tarifa de servicios de soporte igual al costo, conforme a la fórmula de la plantilla. El diferencial de la tarifa de soporte se refleja en RRHH para cuadrar con el precio de operación. Esta distribución es de presentación para el escenario y no cambia los precios de fase.

«Rentabilidad Nominal» conserva la fórmula original de utilidad sobre costo. El control de margen del escenario usa ventas como denominador. Las filas de PCU mantienen sus referencias de origen y quedan pendientes de insumo. Las celdas G21 y G22 esperan los indicadores validados por D1.

La copia integra el resumen económico. Para calendario mensual, Curva S y Fila A se usa el modelo de trabajo D2. Para volver a cargar el resumen desde una versión nueva, ejecutar `node integrar_resumen_mandante.mjs plantilla.xlsx modelo.xlsx salida.xlsx` con `D2_NODE_MODULES` configurada como indica la guía del modelo.

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

Verificar B12:G20 como detalle de costos y tarifas, y C6:C8 y H6:H8 como totales en CLP. Regenerar la copia de integración cuando se cierre el presupuesto.
