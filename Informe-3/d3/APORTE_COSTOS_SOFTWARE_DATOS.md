# 3.8 · Explicación del presupuesto de software y datos

**Tarea:** AUD-31. **Destinatario:** D1/AUD-12, con integración D2. **Fecha:** 12-11-2026. **Estado:** texto preparado; cierre económico sujeto a las conciliaciones identificadas. Es un aporte del Informe 3, no una nueva presentación de capítulos técnicos.

## Texto para integrar

El presupuesto separa trabajo propio, licencias y ejecución de servicios. Las reglas de jornada, asignación, documentos, liquidación y convivencia justifican construir el software de negocio y sus adaptadores ya diseñados en S4.1/S5. Se contratan plataformas administradas y se incorporan bibliotecas compatibles; no se supone una compra adicional de TMS ni se presenta un motor de terceros como desarrollo de audIT.

T-15 ya contiene 36.800 h de servicios E1, integración, datos/migración y servicios E2, más 2.560 h para las cinco innovaciones. El reparto por perfil propuesto por D3 desagrega ese presupuesto y no lo incrementa. La nivelación y elección de costos corresponden a la integración de D2, usando E-26 y E-24 sin confundir costo interno con tarifa de venta. Los cierres de integración/migración hasta M24 deben ubicarse en recursos de operación o reprogramarse expresamente: no se cuentan también en implementación cuya curva termina en M20.

Para la implementación del expediente se adopta la referencia provisional de D2 de $30.000/h para las 160 h de Software y 64 h de Frontend/Móvil: $6.720.000 entre ambos perfiles. Con las referencias de los demás perfiles, las 480 h tienen un costo atribuido de $14.816.000. Esa selección no se extiende a operación ni a la innovación 2 y solo genera gasto adicional por la parte que no esté ya cubierta en T-15. Fuente: respaldo D2 de AUD-21, commit 93477ab, apartado «Costo interno de las 480 horas de implementación».

GitLab Premium Self-Managed concreta la plataforma de S6. Con 33, 37, 16, 16 y 16 usuarios en las anualidades M1/13/25/37/49, la referencia pública USD 29/usuario/mes exige USD 41.064, equivalentes a $36.957.600 netos a E-24. Se pagan doce meses en M49 aunque la anualidad termine en M60. No se presume devolución, descuento ni precio congelado; el alojamiento y los runners son costos distintos.

SonarQube Developer se conserva como partida pendiente de cotización por instancia/LOC. Una edición gratuita no se presenta como equivalente para todos los lenguajes y ramas sin verificarlo. Las herramientas abiertas tienen canon nulo en las ediciones identificadas, pero requieren cómputo, actualización, revisión de dependencias y operación interna. ZAP no reemplaza el pentest externo de D1; respaldar GitLab tampoco sustituye el escrow independiente.

D4 consolida nube y D3 entrega carga, modelo, retención y ejecución: el reparto ya consta en ambos aportes. Las facturas externas se registran una vez en Proveedores y alimentan Operación según T-22, conservando su mes real de pago. El suplemento de VM para GitLab/Sonar/runners tiene una referencia de $36.078.804 netos, todavía fuera del total Azure de D4; faltan discos, copias, ACR y completar identidad/analítica. No constituye el total final de herramientas.

El mantenimiento incluye prevención, corrección, actualización y mejora continua. Las innovaciones requieren nominalmente 12 h/mes para expediente y 16 h/mes para programación; el costo interno atribuido conjunto es $864.000 mensuales de referencia. El adicional de caja depende de la capacidad reservable del mismo perfil en 13.2/13.4. Si ya está en dotación, no se vuelve a sumar. En M21 se conserva la carga nominal E1 durante H12 de E2; el traspaso debe identificarse sin duplicar personas.

La innovación 2 propone 560 h dentro de EDT 12, con costo interno atribuido de referencia de $16.576.000. Su ejecución cloud, operación y beneficio se separan. Sin base para visitas y minutos evitados, el escenario prudente no acredita ahorro monetario. Los $30 millones anuales de patio incluidos por D1 requieren cantidades, costos y sensibilidad explícitos. Los beneficios pertenecen a Curimón y no incrementan ingresos de audIT.

## Entregables y condiciones de cierre

| Tarea | Archivo preparado | Pendiente |
|---|---|---|
| AUD-24 · Esfuerzo | 3.1-esfuerzo-perfiles.md | Nivelación por perfil/mes, cierres M21–M24 y capacidad operativa |
| AUD-25 · Licencias | 3.2-licencias-herramientas.md | Cotización Sonar/LOC y ejecución |
| AUD-26 · Recurrentes | 3.3-costos-recurrentes.md | Terminar AUD-25 y conciliar incrementos |
| AUD-27 · Hacer/comprar | 3.4-desarrollar-comprar-contratar.md | Decisiones entregadas; compras concretas continúan en sus tareas |
| AUD-28 · Proveedores | 3.5-proveedores-software.md | Fichas entregadas, con precio Sonar pendiente identificado |
| AUD-29 · Reparto nube | 3.6-reparto-nube.md | Propietarios documentados; suplemento por dimensionar |
| AUD-30 · Innovación 2 | APORTE_ECONOMICO_INNOVACION_2.md | Capacidad/nube, beneficio D1 e integración D2 |
| AUD-31 · Texto económico | Este archivo | Antecedentes FF abiertos impiden declarar presupuesto completo |

D2 mantiene cantidad, unidad, precio, frecuencia, mes e IVA como entradas de la planilla; los resultados se calculan con fórmulas. calculo/calcular_d3.py comprueba los insumos D3 y no sustituye la hoja del mandante ni permite pegar resultados como constantes. Un null significa faltante, nunca costo cero.

**Fuentes:** S4.1/S5/S6/S13, T-14/T-15/T-19, E-24 p.73/E-26 p.76, FEP01 T-22 p.69 y Aclaraciones Informe 3 §§1/5. Precios/licencias y fechas: 3.2/3.5 y datos/fuentes_licencias.json. VM: instantánea oficial Azure de D4 del 11-11-2026. Revisión base examinada: main 8ae8c27. Los archivos permanecen locales hasta autorización expresa de push.
