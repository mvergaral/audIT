# Modelo editable de trabajo D2

`D2_MODELO_TRABAJO.xlsx` reproduce el escenario publicado en f9ce7b0. Las hojas conectan costos, precios, facturación, cobros, caja financiada, Curva S y VAN/TIR. M57 se usa para conciliar el cobro de la última mensualidad.

| Entrada | Ubicación y uso |
|---|---|
| Proveedores | Bloques mensuales de D4, licencias y calidad/capacitación, con ID y fuente. Las compras del mandante aparecen como informativas. El control detecta IDs duplicados; la conciliación detallada por factura se hace al desglosar los bloques. |
| Personal | Escenario mensual, ajuste editable y cruce de CP-SEC-05. La reserva de prueba se documenta y su costo atribuible se presenta por separado de la caja. |
| Innovaciones | Referencias conocidas de INN-1 e INN-4. Cuando se confirme un importe incremental, cargarlo en Costos, «Otros confirmados», en el mes correspondiente. |
| IVA | Registrar IVA pagado y crédito fiscal por separado, en el mes aplicable. El interruptor de IVA está apagado en el escenario publicado. La estructura supone liquidación del IVA débito neto al mes siguiente. |
| H5 | Cambiar el mes de cobro a M13 en Parámetros para probar la sensibilidad. La facturación sigue en M12. |
| Capital inicial | Entrada de escenario. Tras cambiar costos o cobros, revisar caja mínima y uso de línea y volver a dimensionar el financiamiento si corresponde. |

Se verificó la coincidencia de VAN, TIR, caja final y M57 con el escenario previo. También se probó el cambio de fecha de H5, la propagación de un ajuste de personal al VAN y la separación entre IVA pagado y crédito fiscal. El Excel exportado contiene ocho hojas, un gráfico vinculado al flujo y resultados calculados sin errores de fórmula.

Para regenerar desde la versión publicada, configurar `D2_NODE_MODULES` con la carpeta que contiene `@oai/artifact-tool` y ejecutar `node generar_planilla_trabajo.mjs D2_MODELO_TRABAJO.xlsx`. La generación reconstruye el escenario inicial desde los CSV versionados.

Para el cierre quedan la hoja Resumen del mandante, el detalle de proveedores e IVA, las cantidades y costos incrementales de innovaciones, y la conciliación de personal. Con esos datos se actualizarán precios, caja e indicadores y se emitirá la Fila A definitiva a D1.
