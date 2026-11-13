# Modelo editable de trabajo D2

`D2_MODELO_TRABAJO.xlsx` actualiza el escenario de f9ce7b0 con el aporte D3 de 4070a7e. Las hojas conectan costos, precios, facturación, cobros, caja financiada, Curva S y VAN/TIR. M57 se usa para conciliar el cobro de la última mensualidad. El CSV de Fila A de 262ead9 corresponde a la versión anterior.

| Entrada | Ubicación y uso |
|---|---|
| Proveedores | Bloques mensuales de D4, licencias y calidad/capacitación, con ID y fuente. Las compras del mandante aparecen como informativas. El control detecta IDs duplicados; la conciliación detallada por factura se hace al desglosar los bloques. |
| Personal | Escenario mensual, ajuste editable y cruce de CP-SEC-05. La reserva de prueba se documenta y su costo atribuible se presenta por separado de la caja. |
| Innovaciones | Referencias conocidas de INN-1 e INN-4. Cuando se confirme un importe incremental, cargarlo en Costos, «Otros confirmados», en el mes correspondiente. |
| IVA | Registrar IVA pagado y crédito fiscal por separado, en el mes aplicable. El interruptor de IVA está apagado en el escenario publicado. La estructura supone liquidación del IVA débito neto al mes siguiente. |
| H5 | Cambiar el mes de cobro a M13 en Parámetros para probar la sensibilidad. La facturación sigue en M12. |
| Capital inicial | Entrada de escenario. Tras cambiar costos o cobros, revisar caja mínima y uso de línea y volver a dimensionar el financiamiento si corresponde. |

La demanda D3 se incorpora como hoja de planificación. Las 6.008 h sustituyen las 17.600 h como estimación de A09. La diferencia no se descuenta de la nómina. El costo atribuible de INN-1 de CLP 14.816.000 de implementación y CLP 16.072.000 de soporte se mantiene separado de la caja hasta conciliar su cobertura. Se carga CLP 24.856.290 netos de firma automática, con CLP 4.722.710 de IVA referencial. La asignación Azure de CLP 132.000 se individualiza dentro del presupuesto D4 sin sumar una nueva salida.

Para D4 se registran CLP 21.828.338 de IVA referencial de equipos y SIM 5G. Equipos se toman del calendario de la planilla anterior y SIM de 4.2 de D4 (M4–M56). Se conserva el crédito fiscal vacío hasta validar documentos y el interruptor global se mantiene desactivado. Azure, LTE a bordo, Iridium y los demás servicios requieren conciliación de factura y pagador. En INN-4 se conserva el alcance de 182 instalaciones base, incluidas 34 de terceros. El cupo incremental se deja editable y fuera del flujo base hasta acreditar capacidad con visitas y turnos. Los costos unitarios de hardware, alta y soporte pueden simularse en Innovaciones.

Se probó el cambio de fecha de H5, la propagación de un ajuste de personal al VAN y la separación entre IVA pagado y crédito fiscal. También se verificaron el total de firma, la demanda D3 de M9 y el control de duplicados.

Para regenerar desde la versión publicada, configurar `D2_NODE_MODULES` con la carpeta que contiene `@oai/artifact-tool` y ejecutar `node generar_planilla_trabajo.mjs D2_MODELO_TRABAJO.xlsx`. La generación reconstruye el escenario inicial desde los CSV versionados.

Para el cierre quedan la hoja Resumen del mandante, el IVA de las partidas pendientes, la capacidad que cubre las horas D3 y el cupo adicional de comodato. La dotación total sigue siendo de escenario. Con esos datos se actualizarán precios, caja e indicadores y se emitirá la Fila A definitiva a D1.
