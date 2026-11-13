# Plan de cierre D2 · Entrega 3

El objetivo es entregar a D1 una Fila A definitiva que cuadre con el presupuesto, la caja y el Resumen original del mandante. Este plan parte del modelo vigente y del alcance aprobado de 182 montajes base. Las altas adicionales se mantienen como sensibilidad.

## 1. Completar los insumos en paralelo

| Tarea | Acción | Evidencia para cerrar |
|---|---|---|
| [AUD-14](https://linear.app/audit-fep/issue/AUD-14) | En «Capacidad por perfil», registrar ejecutor por código, horas reservadas y fuente. Priorizar Seguridad/SRE en M9 y Datos/QA en M21–M24. Descontar guardias y otras tareas. Conciliar las 15 h de campaña de CP-SEC-05 dentro de su reserva de 16 h y las 72 h de preparación dentro de 4.1/A11. Aplicar tarifas E-26 respaldadas. | Matriz perfil/mes con demanda, capacidad efectiva, brecha, tarifa y fuente. |
| [AUD-15](https://linear.app/audit-fep/issue/AUD-15) | Reasignar horas cuando haya disponibilidad acreditada. Si queda una brecha, presentar monto y efecto en caja antes de comprometer refuerzo. Cargar el ajuste aprobado una sola vez y revisar personal M1–M56. | Nómina mensual conciliada con T-15 por implementación, operación y soporte. CLP 12.516.000 es una sensibilidad focalizada. |
| [AUD-21](https://linear.app/audit-fep/issue/AUD-21) | Para INN-1, mantener el costo de firma como estimación hasta fijar su importe y registrar solo el soporte incremental que resulte de AUD-14/15. Para INN-4, conciliar los costos de los 182 montajes con la base y separar el recupero bruto del beneficio neto para Curimón. Documentar el reparto o dejar el beneficio neto identificado como pendiente. | Matriz por innovación, mes y pagador, con inversión, operación, beneficio y supuestos. Sensibilidad de comodato fuera de la caja base. |
| [AUD-16](https://linear.app/audit-fep/issue/AUD-16) | En «Detalle proveedores D4» y «Proveedores», registrar base afecta, pagador, IVA, fecha de pago y crédito fiscal por proveedor. Para el presupuesto, identificar expresamente las estimaciones y su respaldo. Completar indirectos y bases de seguros y garantías. Conciliar la reserva y los costos informativos del mandante. | Registro mensual por partida, con fuente, IVA referencial separado y conciliación entre proveedores, Costos y Resumen. |

Los datos de capacidad y tratamiento de IVA son insumos de cierre. Si falta respaldo, elevar el supuesto concreto y su impacto para decisión antes de convertirlo en base. La plantilla original ya está disponible y su hoja Resumen ya fue integrada en una copia.

## 2. Congelar y verificar la planilla

| Tarea | Acción | Evidencia para cerrar |
|---|---|---|
| [AUD-20](https://linear.app/audit-fep/issue/AUD-20) | Recalcular precios por fase con costos cerrados. Comprobar margen sobre ventas netas y dimensionar el capital inicial y la línea. | Cuadro de precio, costo y margen por fase. Financiamiento coherente con E-24. |
| [AUD-18](https://linear.app/audit-fep/issue/AUD-18) | Aplicar precios a los 12 hitos y 36 mensualidades, incorporar variables y multas con sus supuestos, y probar el atraso de H5. | Cobros conciliados con E-25, reparto 60/40 y mensualidad M56 por cobrar en M57. |
| [AUD-17](https://linear.app/audit-fep/issue/AUD-17) | Regenerar el flujo libre y financiado. Cerrar IVA de caja, intereses, deuda y conciliación M56–M57. Probar liquidez con precios cerrados y crédito fiscal diferido. | 56 meses conciliados, M57 auxiliar, caja sin déficit en la base y línea dentro de CLP 50 millones. Si falla, resolver financiamiento o calendario antes de emitir. |
| [AUD-19](https://linear.app/audit-fep/issue/AUD-19) | Regenerar la Curva S con las series del flujo final. Actualizar la copia del Resumen conservando estructura y fórmulas. | Costos con intereses, facturación y caja cuadran con el modelo. Totales en CLP, UF y USD verificados. |

Actualizar `D2_MODELO_TRABAJO.xlsx` desde el generador, exportar la Fila A con `exportar_fila_a.py` y regenerar `D2_RESUMEN_MANDANTE.xlsx` usando `integrar_resumen_mandante.mjs`. Verificar fórmulas, reconciliación de precios y caja, y preservación de rótulos, orden y celdas combinadas de Resumen.

## 3. Entregar y cerrar

| Tarea | Acción | Evidencia para cerrar |
|---|---|---|
| [AUD-22](https://linear.app/audit-fep/issue/AUD-22) | Publicar el Excel, Resumen, Curva S y Fila A de M0 a M56 con M57 auxiliar. Adjuntar versión, tasa, supuestos y controles para D1. | Paquete versionado en main y enlace en Linear. Fila A verificada contra el mismo Excel. |
| [AUD-23](https://linear.app/audit-fep/issue/AUD-23) | Recibir de D1 VAN, TIR, sensibilidad y punto de equilibrio validados sobre esa versión. Incorporar los resultados y comprobar sus referencias y unidades. | Indicadores incorporados al mismo paquete y respaldo de la versión validada por D1. |

Publicar cada avance verificable en main y enlazarlo en las incidencias D2 correspondientes. La validación financiera y el cierre de las incidencias propias de D1 corresponden a D1.
