# Cotejo de cierre · Informe 3

## Revisión 2.1 · 13 de noviembre de 2026

La revisión parte del commit auditado `c9a6515`. Los importes de oferta, el costo neto, el VAN y la TIR de la base conservan la conciliación del corte de origen. La disponibilidad de financiamiento, las asignaciones de personal y los antecedentes comerciales siguen condicionando el cierre de la entrega.

| Prioridad de auditoría | Corrección y comprobación | Evidencia pendiente |
|---|---|---|
| 1. Liquidez | El plazo propuesto para H5 es de 15 días corridos desde la recepción de la factura válida emitida con el acta. Con recepción provisional el 31-01-2028, tesorería proyecta el 15-02-2028 (M13). Con 30 días, proyecta el 01-03-2028 (M14). Con reserva, CLP 400 millones de refuerzo, 72 h compradas y comisión ilustrativa de CLP 250.000, M12 cierra con CLP 8.957.065 en ambos casos. Con pago a 30 días, M13 cierra con déficit de CLP 8.989.379 aun con la línea al tope. | Confirmar plazo con la contraparte, acta, recepción de la factura y abono. Acreditar crédito, aporte, línea y calendario diario de tesorería. [Decisiones y pruebas de caja](d2/AUD-20_DECISIONES_MODELO.md) |
| 2. Costos, horas e IVA | Clasificación mensual por naturaleza T-22 y cruce de los cierres M21–M24. IVA estimado de caja de CLP 14.432.400 imputado a ExpressRoute y LTE, con crédito fiscal base de CLP 0. Referencias de firma, licencias y hardware por pagador. | Ejecutores y horas acreditadas, bases de pólizas y overhead, facturas y crédito fiscal, consumo y pagador de energía y combustible. [Conciliación de respaldos](CONCILIACION-RESPALDOS.md). |
| 3. Coherencia del modelo | Se preserva RESUMEN. El Cuadro maestro concilia contra la facturación efectiva y muestra la diferencia respecto de la oferta. Se protegieron las fórmulas y se agregaron controles de entradas y de ajustes mensuales. | La aplicación del modelo en tesorería depende de completar los parámetros con evidencia efectiva. |
| 4. Innovaciones | Se documentaron los componentes de inversión, operación, cobertura y beneficio para Curimón de las cinco fichas, con fórmulas de escenario y solapes identificados. | Línea base y validación causal para monetizar, cobertura de ejecutores, cupo, altas y reparto aprobados para INN-4. [Conciliación de respaldos](CONCILIACION-RESPALDOS.md). |
| 5. Artículo 46 | El anexo del Informe 3 registra 68 filas, con 17 incorporadas, 13 parciales y 38 sin cierre acreditado. Se cotejaron los identificadores de las 100 observaciones históricas del Informe 1 y los cruces con las observaciones vigentes. | Cerrar las filas con evidencia pendiente y conciliar las referencias con los folios definitivos del sobre. [Matriz Art. 46](AUDIT-Anexo-Art46-Informe3-Revision-Independiente.md). |
| 6. Adquisiciones | Se distinguen orden, pago, recepción y puesta en servicio. Se actualizaron dependencias de grupo electrógeno, G26I y ExpressRoute antes de H3 o del piloto, con alternativas condicionadas. | Cotizaciones, stock, plazos puestos en destino, factibilidad de enlace y aceptación de alternativas. [Matriz de adquisiciones](d4/4.5-matriz-adquisiciones.md). |
| 7. PDF y exposición | Informe v2.1, ficha de lectura ampliada y rótulo de firma gráfica. Curva S de la presentación con segmentos rectos y meses críticos en el eje. Las siete notas de exposición distribuyen 15 minutos entre dos roles. Se abrió el enlace y se verificaron retención de paquetes y reconciliación en el simulador. | El representante debe acreditar las firmas según el Art. 40.2. El equipo debe efectuar el ensayo oral y registrar la revisión humana y el A-6. [Registro de asistencia](../Investigacion/Persona-8/Registro_A6_Revision_Informe_3_20261113.md). |

### Comprobaciones de la revisión 2.1

- **Excel de escritorio.** Se regeneró desde OFERTA_D2 por COM y se volvió a aplicar el postproceso mediante `d2/aplicar_controles_modelo.mjs`. Se probaron el atraso de H5, el variable de M21, el descuento M56 y su cobro M57, los 36 descuentos por CLP 500.000 y el rechazo cruzado de una combinación inválida. La venta de escenario cae CLP 18 millones con los 36 descuentos y el control de facturación queda en cero. Se verificaron la compra de horas, comisión, giro desplazado, costos adicionales y los meses independientes de pago y crédito de IVA.
- **PDF.** Se recompiló con LuaLaTeX y Biber y se verificaron 23 folios carta, hoja resumen, índice, las 68 filas del anexo, legibilidad y enlace de la demostración. Se compilaron ejemplares de control de T-14, T-15, T-17, T-18 y T-19. [Figura 2.1, S2 folio 10](d1/control-art46/S2-NEC-03-folio10.pdf).
- **Presentación.** Se renderizaron las siete láminas. El gráfico conserva 56 observaciones por serie en una planilla incrustada y las tres series se cotejaron con el CSV de Curva S. Se verificaron el enlace y la agenda de 15 minutos con dos roles.

## Aplicación del plan de corrección · corte auditado

- **Modelo.** El cuadro maestro concilia a costo y venta de RESUMEN y el puente mensual de IVA reproduce CLP 69.374.046 de referencia y CLP 14.432.400 pagados en la caja base. Se incorporan ajustes de operación por mes, comisión de crédito de estrés, criterios de administración formulados y escenarios de beneficios de Curimón con entradas y evidencia.
- **Prueba de regresión.** El recálculo en LibreOffice conservó el VAN, la TIR, la caja mínima y el uso de línea de base. En una copia, CLP 1.000.000 variables de M21 pasan a la factura M21 y al cobro M22. El descuento de CLP 500.000 de M56 pasa a la factura M56 y al cobro M57. H5 desplazado a M13 conserva la factura de M12. Una comisión de CLP 250.000 en el estrés reduce la caja M12 en ese importe bajo las mismas condiciones. Queda la comprobación equivalente en Excel de escritorio.
- **Informe y exposición.** El PDF presenta compras vinculadas a hitos, costos directos e indirectos, sensibilidad y valorización. El anexo se ubica después del cuerpo económico. El recuento es 19 incorporadas, 6 parciales y 43 sin cierre acreditado. La presentación incorpora el déficit previo al financiamiento y los hitos de la Curva S.
- **Demostración.** Se ejecutó el recorrido publicado Portal Clientes → Simulador Operativo en Vivo → pérdida de cobertura → restablecimiento. La interfaz mostró la retención en el búfer y el mensaje de reconciliación exitosa. El ensayo oral de 15 minutos corresponde al equipo expositor.

### Evidencia pendiente

| Frente | Evidencia para cerrar |
|---|---|
| Horas, nómina y M21–M24 | Confirmar ejecutores, reservas y posibles horas compartidas de CP-SEC-05 y G13. Conciliar las actividades 6.5 y 7.2 con T-15, E-26 y sus filas de nómina. |
| H5 y caja | Acreditar fecha de cobro, crédito y aporte, giros y comisiones. Recalcular con los datos confirmados y comprobar la meta M12. |
| Proveedores y pagadores | Acreditar ofertas, IVA, crédito fiscal, bases asegurables, overhead, energía y combustible. Contrastar la suficiencia de la reserva por riesgo y mes. |
| Innovaciones | Conciliar horas e imputación incremental por mes, acreditar cupo adicional y reparto de INN-4 y obtener evidencia para monetizar beneficios. |
| Art. 46 | Verificar el cambio y localizador de cada observación parcial o abierta. Revisar GEN-05 en S6 y S8. |

La edición del modelo usa el consolidado generado por Excel como insumo para `d2/aplicar_controles_modelo.mjs`. El script incorpora las hojas y fórmulas de revisión. En la edición publicada se restituyeron las protecciones y hojas ocultas que el exportador no conserva, y se incorporaron resultados recalculados sin reemplazar las fórmulas. La ruta COM se actualizó para el calendario de cobros y la comisión de estrés y queda por validar en Windows.

La planilla consolidada toma como base el paquete OFERTA_D2 del commit c601503. El corte de insumos es 8c950fa. El escenario conserva los precios y el calendario base publicados.

## Controles del comparador de oferta con H5 cobrado en M12

| Control | Resultado |
|---|---:|
| Costo neto | CLP 7.984.400.845 |
| Precio neto | CLP 9.796.810.853 |
| Margen sobre ventas | 18,50 % |
| VAN M0–M56 | CLP 1.235.043.316 |
| TIR mensual | 83,6613 % |
| Cobro en M57 | CLP 143.833.557 |
| Equilibrio nominal con costos fijos del caso | CLP 7.984.400.845 |
| Venta de equilibrio a VAN cero con calendario base y escala uniforme | CLP 8.175.218.018 |
| Recuperación descontada sostenida | M16 |
| Déficit en M12 con H5 en M13, sin reserva ni refuerzo | CLP 155.747.160 |
| Déficit en M12 con H5 en M13 y reserva D4, antes del financiamiento adicional | CLP 308.446.935 |

Se conservaron los rótulos, las fórmulas y las celdas combinadas de RESUMEN. El Resumen Ejecutivo explica las referencias invertidas de costo y venta de la plantilla y su métrica de utilidad sobre costo. La Fila A y la Curva S de base se cotejan con los CSV de OFERTA_D2.

## Decisión de financiamiento H5 · 13-11-2026

H5 conserva su mes contractual M12 según E-25. Para tesorería se propone pagar dentro de 15 días corridos desde la recepción de la factura válida, emitida el día en que se suscribe el acta de aceptación. La fecha provisional de acta y recepción es el 31-01-2028. El plazo de 15 días vence el 15-02-2028 (M13) y el de 30 días, el 01-03-2028 (M14). Las fechas deben recalcularse con el acta y la recepción efectivas. [Plazo propuesto para H5](d2/AUD-20_DECISIONES_MODELO.md#plazo-propuesto-para-h5)

D1 aprobó modelar el atraso del cobro de H5 a M13 junto con el desembolso de la reserva D4 en M12. El supuesto aprobado incorpora CLP 400.000.000 adicionales desde M1: CLP 320.000.000 de crédito y CLP 80.000.000 de socios. Se aplica 0,9 % mensual al saldo bancario de apertura y amortización desde M21, según la caja disponible. La meta es mantener CLP 10.000.000 de caja en M12. El recálculo en Excel dejó CLP 11.223.065 de caja mínima en M12 y cero giros de línea en el escenario combinado. Se mantienen los precios y el cálculo del VAN sobre la Fila A.

La aprobación corresponde a la modelación de la licitación. La disponibilidad de los fondos, los términos de giro y las comisiones requieren respaldo. El escenario actual no incluye comisiones adicionales de este crédito. Si se confirman, se incorporan en la Fila C y se vuelve a comprobar la holgura.

### Respaldo revisado

- **Bases del modelo.** El Formulario E-24, FEP01 p. 73, fija 0,9 % mensual para el crédito de consumo de referencia y los topes de 80 % bancario, 20 % propio y CLP 50 millones para la línea. El [dimensionamiento anterior de D2](https://github.com/mvergaral/audIT/commit/a89084b) y el [paquete OFERTA_D2](https://github.com/mvergaral/audIT/commit/c601503) respaldan la metodología de caja.
- **Disponibilidad.** En las ramas remotas revisadas al 13-11-2026, con main en 8c950fa, no se encontró una aprobación de crédito por CLP 320 millones ni un compromiso de socios por CLP 80 millones. La [guía pública de BancoEstado](https://www.bancoestado.cl/content/dam/bancoestado-public/pdf/microempresas/guia-de-uso-emprendedor.pdf) sirve de referencia para el uso de crédito comercial como capital de trabajo. El monto, la tasa contractual y las condiciones de giro requieren confirmación específica.
- **Estado de entrega.** Escenario de financiamiento aprobado por D1 para la licitación y verificado en la Fila C. Disponibilidad, condiciones de giro y comisiones pendientes de respaldo.

## Responsables de la evidencia pendiente

[Conciliación de personal, gastos e infraestructura](CONCILIACION-RESPALDOS.md).

| Responsable | Pendiente | Evidencia para cerrarlo |
|---|---|---|
| D1 y D2 | Plazo de pago de H5 y disponibilidad de financiamiento | Confirmación del plazo por la contraparte, acta, recepción de factura y fecha de abono. Acreditar monto, fecha, instrumento y costo de los fondos. Recalcular el saldo diario y el cierre M12. |
| D1 y D2 | IVA de proveedores, seguros y overhead | Condiciones tributarias por proveedor, términos de las pólizas y conciliación de overhead con RRHH y R-24. |
| D1 y D2 | Horas de calidad, PCU y personal | T-15 y E-26 conciliados con ejecutores y disponibilidad. Identificar las 72 h de preparación de CP-SEC-05. |
| D1 y D2 | Innovación 5 | Los montos concilian con talleres, calibración, desarrollo y soporte. Sigue pendiente acreditar cobertura por ejecutor e IVA de calibración. |
| D2 y D3 | Innovaciones 1 y 2, licencias y firma | Acreditar cobertura de horas, condición comercial de Sonar y firma, y base de medición del beneficio para Curimón. |
| D2 y D4 | Innovaciones 3 y 4, suministros y reserva | Relacionar costos con partidas, confirmar energía y combustible, validar reparto de recuperos y calendario de uso de la reserva. |
| D1–D4 | Anexo Art. 46 | Completar la evidencia y cotejar los folios del juego técnico final. |
| Equipo | Prototipo navegable y validación de entrega | [Acceso al sitio audIT](https://carlosabarza.github.io/PaginaAudIT/#equipo). El sitio ofrece «Simulador Operativo en Vivo». Recorrido verificado el 13-11-2026: Portal Clientes → Simulador Operativo en Vivo → Simular Pérdida de Cobertura Celular → Restablecer Cobertura Móvil. La interfaz mostró el búfer local y la confirmación de reconciliación. Queda la validación humana y el ensayo completo de exposición. |

Regeneración de la planilla desde la raíz del repositorio con PowerShell 7 y Excel de escritorio:

    pwsh -NoProfile -File Informe-3/d2/consolidar_informe3.ps1

Los insumos OFERTA_D2 están versionados en Informe-3/d2. El archivo generado se guarda en Informe-3.
