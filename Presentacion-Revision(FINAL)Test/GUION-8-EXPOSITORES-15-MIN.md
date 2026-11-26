# Guion oral · Propuesta final audIT

**Transportes Curimón · TFEP-01/2026 · 8 expositores · máximo 15 minutos**

La pauta reserva **14:05 para la exposición, incluidos los relevos, y 0:55 para absorber demoras**. Los tiempos son acumulados desde la portada. Cada encabezado indica cuándo cambiar de lámina. Una sola persona maneja las flechas y acompaña la explicación con las revelaciones. Las referencias y las indicaciones entre corchetes son para el equipo.

| Expositor | Tiempo acumulado | Láminas | Tema |
|---|---|---|---|
| 1 | 0:00–1:45 | 1–3 | Problema y alcance de la oferta |
| 2 | 1:45–3:15 | 4–5 | Arquitectura híbrida y capas |
| 3 | 3:15–4:40 | 6–7 | Asignación segura y continuidad a bordo |
| 4 | 4:40–6:55 | 8–10 | EDT, cronograma y capacitación |
| 5 | 6:55–8:30 | 11–12 | Riesgos, reservas y control de plazo |
| 6 | 8:30–10:15 | 13–14 | Adquisiciones, facturación y caja |
| 7 | 10:15–12:25 | 15–16 | Costos, rentabilidad y sensibilidad |
| 8 | 12:25–14:05 | 17–19 | Condiciones comerciales, compromisos y cierre |

## Expositor 1 · Problema y oferta

### 0:00 · Lámina 1 — Propuesta final

Buenos días. Somos audIT. Presentamos nuestra propuesta para que Transportes Curimón pueda decidir, con evidencia verificable, si un viaje está en condiciones de salir.

### 0:10 · Lámina 2 — Una salida segura

[Revelar conductor, vehículo y documento en ese orden.]

Antes de autorizar una salida, la torre necesita responder tres preguntas. ¿El conductor cumple las condiciones de jornada y habilitación? ¿El tractor y el semirremolque son aptos para ese viaje? ¿Está disponible y conforme el documento de transporte? Si alguna condición obligatoria falla, el sistema bloquea la asignación, explica la causa y registra la decisión. La operación puede identificar qué falta y la supervisión puede reconstruir qué evidencia se usó.

### 0:55 · Lámina 3 — Resumen de la oferta

La propuesta combina 47 componentes desplegados entre nube, instalaciones y flota. Incluye equipamiento audIT para 182 camiones, dos etapas de implementación con aceptación final en el mes 21 y 36 meses de operación. El precio neto de ambas fases es de aproximadamente ocho mil trescientos sesenta y ocho millones de pesos.

El alcance se organiza en 54 paquetes de trabajo. También entregamos cinco propuestas de innovación con condiciones de validación, un registro de 36 riesgos con disparadores y un catálogo de 120 pruebas diseñadas. Esas pruebas servirán para verificar la solución durante la ejecución. Veamos cómo se distribuye la arquitectura.

*Referencias para el equipo · S2, S3, S4 §4.2.3, S7, S8, S9, S13, T‑17, T‑19 y oferta económica E‑21.*

## Expositor 2 · Arquitectura

### 1:45 · Lámina 4 — Nube, sitio y flota

[Señalar nube, San Bernardo, terminales y flota.]

El núcleo funciona en Azure Chile Central. Allí están 32 componentes y se concentran los servicios de negocio, la recepción de telemetría y los datos centrales. La región de recuperación prevista es Brazil South. Su uso con datos personales depende de la habilitación y aprobación correspondientes.

Otros 14 componentes están fuera de la nube. San Bernardo conserva funciones de continuidad para la torre, y los terminales regionales cuentan con cómputo en activo y en espera. La propuesta instala equipos audIT en 182 camiones. Los 192 vehículos de terceros que ya cuentan con equipo conservan sus dispositivos y se integran a través de plataformas cuyos accesos deben homologarse.

### 2:35 · Lámina 5 — Ocho capas

Las ocho capas organizan la solución desde los portales y la aplicación móvil hasta los servicios y los datos. Front Door protege la entrada pública, API Management administra el acceso y los servicios de negocio se ejecutan en Azure Kubernetes Service. Identidad y observabilidad atraviesan esas capas.

Los servicios tienen responsabilidades definidas. Planificación consulta a Personas por la habilitación del conductor y a Flota por la aptitud del vehículo. Esa separación permite rastrear el origen de cada decisión. Ahora veremos cómo ocurre en una asignación real.

*Referencias para el equipo · S4 §§4.1.3–4.1.4, 4.2.3 y 4.3, S5, T‑11 y T‑16, riesgo R‑24.*

## Expositor 3 · Asignación y continuidad

### 3:15 · Lámina 6 — Verificación en 30 segundos

[Seguir la solicitud desde la torre hasta el veredicto.]

Cuando la torre solicita un viaje, el servicio consulta en paralelo las condiciones de jornada, vehículo y documento. Si la evidencia cumple, confirma la asignación y deja el veredicto registrado. Si existe una causa obligatoria de bloqueo, devuelve la razón a la torre para que pueda resolverla.

El diseño distribuye los 30 segundos en 25 de procesamiento y 5 de margen. Ese presupuesto se comprobará con pruebas. El retorno del documento a cabina tiene su propio límite de 90 segundos y el emisor sigue siendo el sistema contable.

### 3:55 · Lámina 7 — El camión sin red

El equipo a bordo registra localmente la posición, la identificación del conductor y los eventos disponibles. El lector CAN sin contacto evita intervenir el arnés, y el enlace satelital se reserva para mensajes críticos. El diseño prevé hasta 288 horas de almacenamiento a bordo y 24 horas de continuidad en sitio para las funciones previstas. Al recuperar el enlace, el equipo reenvía la evidencia y confirma su recepción.

La asignación de viajes nuevos y la emisión documental siguen pasando por los servicios centrales. Esa diferencia delimita qué puede continuar durante un corte. Pasemos al plan para implantar y aceptar estas capacidades.

*Referencias para el equipo · S3, S4 §§4.1.9, 4.1.13 y 4.2.2, S5, T‑11, T‑17 y Caso RT‑09.01.*

## Expositor 4 · Ejecución y aceptación

### 4:40 · Lámina 8 — Estructura de desglose del trabajo

La estructura de desglose del trabajo, o EDT, organiza el alcance en 13 elementos y 54 paquetes. Cada paquete identifica un entregable, un responsable y un criterio de aceptación. Eso nos permite vincular lo que se construye con la evidencia que debe revisar la contraparte.

Por ejemplo, el montaje a bordo se acepta con un acta por camión. La capacitación, en cambio, se comprueba con la práctica por turnos y la certificación de los usuarios. Ambos forman parte del mismo proyecto, con criterios de recepción distintos.

### 5:20 · Lámina 9 — Carta Gantt

[Señalar las barras, las precedencias y los rombos de aceptación.]

La carta resume la malla final de 122 nodos hasta el día hábil 420. Las barras representan las ventanas de trabajo, las líneas muestran dependencias y los rombos indican cuándo se prevé emitir las actas. El punteado indica holgura total. Una ventana en rojo señala ausencia de holgura, que también puede deberse a una restricción local.

H4, H7 y H12 llegan a su límite contractual. Para H12, por ejemplo, la marcha blanca de la segunda etapa termina en el día 400, el corte llega al 410 y la revisión de la contraparte ocupa los diez días restantes. La aceptación, por tanto, depende tanto del trabajo técnico como de que la revisión se complete a tiempo.

### 6:15 · Lámina 10 — Capacitación y compuerta G13

Para capacitar a torre, terminales y conductores, G13 libera una versión de preproducción probada con datos y materiales. La familiarización dura diez días y empieza ocho días hábiles antes del cierre del último sprint. Le siguen treinta días de práctica y evaluación por turnos. La capacitación aporta evidencia a la revisión del dossier antes del acta de arranque.

[Avanzar una vez para mostrar la reserva A14.]

En paralelo a la revisión corre la reserva de catorce días que parte en H5. Ambas ramas convergen en el acta H6, que habilita la marcha blanca. Esa fecha es la que protege el control del riesgo R‑16.

*Referencias para el equipo · S6, S7 §§7.1–7.3, T‑14, T‑15, T‑16 R‑16 y R‑17, y E‑25.*

## Expositor 5 · Riesgos y reservas

### 6:55 · Lámina 11 — Matriz de riesgos

[Señalar los ejes y ubicar R‑17 entre los riesgos de exposición alta.]

El T‑16 registra 36 riesgos. La matriz ubica sus códigos según la probabilidad y el impacto iniciales. Desde 12 puntos, la exposición se clasifica como alta y exige contingencia. Cada riesgo tiene un responsable, un disparador y una respuesta prevista.

R‑17 sigue alto porque tres hitos de pago llegan sin margen. R‑28 ilustra otro tipo de riesgo: si el documento completo no vuelve a cabina en el tiempo exigido, se ensaya ese canal, se anticipa la emisión cuando la carga se conoce y se conserva el bloqueo si falta el documento conforme.

### 7:45 · Lámina 12 — Reservas y escalamiento

La reserva A14 dispone de 14 días hábiles para proteger el inicio de la primera marcha blanca. A23 dispone de 10 para la segunda. Ambas protegen fechas concretas del plan. Para R‑17, un día hábil de atraso activa una alerta. Si el atraso proyectado supera el margen del hito, el caso se escala al Comité Ejecutivo.

Antes de fijar la línea base en H1 se validarán capacidad, ventanas de terceros y estimaciones con los ejecutores. Un atraso de aceptación también puede trasladar un cobro. Por eso el bloque siguiente muestra cómo se financia la operación entre hitos.

*Referencias para el equipo · S7 §7.3.1, S8 §§8.1–8.3 y T‑16.*

## Expositor 6 · Adquisiciones y tesorería

### 8:30 · Lámina 13 — Quién provee y quién paga

Las adquisiciones responden a los tres entornos de la arquitectura. Microsoft Azure aporta los servicios de nube. audIT asume, entre otros equipos, los servidores de continuidad en San Bernardo, el cómputo de los terminales regionales y el respaldo eléctrico. El mandante compra los equipos de red y de campo que le asigna el T‑11, incluido el equipamiento previsto para la flota. El hardware a cargo del mandante está valorizado por separado en alrededor de 225 millones de pesos, como referencia presupuestaria.

### 9:25 · Lámina 14 — Curva S y caja mensual

[Señalar primero la gráfica superior y luego el saldo inferior.]

La curva superior compara facturación acumulada y costos con intereses. En el mes 56, la facturación llega a 8.368 millones de pesos y los costos con intereses a 6.907 millones, aproximadamente. La operación empieza a facturarse en el mes 21 y a cobrarse en el 22. El último cobro queda programado para el mes 57.

Abajo vemos el saldo de caja financiada con IVA. Su mínimo de cierre en el caso base es de unos 227 millones de pesos en el mes 9. Como el orden de pagos y cobros puede crear un faltante dentro del mes, la siguiente lámina financiera examina ese efecto bajo estrés.

*Referencias para el equipo · S4, T‑11, T‑22, E‑21, E‑25 y hojas «Curva S», «Flujo de Caja» y «Hardware del mandante» del modelo del Sobre 3.*

## Expositor 7 · Costos y evaluación financiera

### 10:15 · Lámina 15 — Costo neto y precio

[Señalar el gráfico por categoría y después el precio por fase.]

El costo neto del proyecto asciende a aproximadamente 6.820 millones de pesos. Recursos humanos es la partida principal. El resto se distribuye entre inversión, administración y operación. En la lámina, la operación aparece desglosada entre costos propios y servicios de proveedores.

El precio neto ofertado es de aproximadamente 4.478 millones para implementación y 3.891 millones para 36 meses de operación. Sobre el total de venta neta, el margen consolidado es de 18,50 por ciento. La Curva S incluye intereses en su serie de costos, por lo que el total de esa gráfica y el costo neto de esta lámina responden a bases distintas.

### 11:15 · Lámina 16 — VAN, TIR y sensibilidad

Para evaluar el proyecto usamos 56 meses de flujo y una tasa de descuento mensual de 1,0262 por ciento. El caso base arroja un valor actual neto de 1.064,66 millones de pesos. La TIR mensual reportada es de 79,19 por ciento y la unicidad de esa raíz queda por validar.

El VAN sigue positivo en los escenarios mostrados. Con costos cinco por ciento mayores, baja a 793 millones. Con cobros cinco por ciento menores, baja a 740 millones. Si el cobro de H5 se atrasa al mes 14 y se usa la reserva en el mes 12, el VAN queda en unos 922 millones, pero antes de recibir los cobros aparece un déficit de casi 369 millones. El modelo muestra que una facilidad contingente de 420 millones cubriría ese faltante si está disponible. Pasemos a las condiciones contractuales y a la evidencia de aceptación.

*Referencias para el equipo · T‑22, E‑21, E‑24 y Sobre 3, hojas «Parámetros D2», «Indicadores» y «Sensibilidad».*

## Expositor 8 · Compromisos y cierre

### 12:25 · Lámina 17 — Garantías y pagos

La oferta contempla una garantía de seriedad de 500 mil dólares, con vigencia mínima de 150 días corridos, y una garantía de fiel cumplimiento de un millón de dólares, vigente hasta doce meses después del término de la operación. Los pagos de implementación se distribuyen en un 60 por ciento para la primera etapa y un 40 por ciento para la segunda, a través de doce hitos asociados a entregables aceptados.

### 13:05 · Lámina 18 — Tres compromisos verificables

Nuestro primer compromiso es demostrar la decisión de salida y las funciones que la operación conserva durante un corte de enlace. El segundo es entregar el alcance mediante paquetes con criterios de aceptación y actas acordadas con la contraparte. El tercero es gestionar los riesgos con disparadores explícitos y evidencia de pruebas.

El catálogo de calidad contiene 120 casos diseñados que se vinculan con 42 requerimientos. Durante el proyecto, su ejecución y sus resultados respaldarán la aceptación junto con las verificaciones documentales que correspondan. Así podrá revisarse qué se entregó, cómo se comprobó y qué condiciones quedan abiertas en cada hito.

### 13:55 · Lámina 19 — Preguntas

Gracias por su atención. Quedamos disponibles para sus preguntas sobre la solución, el plan de ejecución o la oferta económica.

*Referencias para el equipo · FEP01, artículos 35 y 36 y Formulario E‑25. S9, S13, T‑13, T‑17 y T‑19.*

## Consultas de la comisión

| Si preguntan por… | Referencia de respaldo |
|---|---|
| Qué funciones se mantienen durante un corte | Lámina de respaldo «Si se corta el enlace, la operación sigue» y S4 §4.2.3. |
| Qué hacer si se atrasa un hito | Láminas 9 y 12, T‑15 y S8 §8.2. Para el efecto de H5 en caja, lámina 16. |
| Cómo se acredita la calidad | T‑13 y T‑17. Distinguir catálogo diseñado, ejecución contractual y acta de aceptación. |
| Cuáles son las cinco innovaciones | Lámina de respaldo de innovaciones y S13/T‑19. Expediente verificable, intervenciones por oportunidad de patio, semirremolque conectado, esquema de adhesión y propiedad, y bienestar del conductor y parador seguro. |
| Por qué el VAN sigue positivo si falta caja | Lámina 16 y Sobre 3. El VAN mide el valor descontado de los flujos del proyecto. El faltante se mide antes de los cobros en el escenario de tesorería. |

Para abrir las láminas de respaldo, pulsa **B**. Usa **Escape** para volver al recorrido principal.
