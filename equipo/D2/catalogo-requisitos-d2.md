# Catálogo preliminar de requisitos - D2

**Subdocumento 3 · Esquema de solución y alcance**\
**Estado:** versión ratificada por D2 el 06-09-2026, comprometida para el Informe 1\
**Fuentes:** FEP03 · Capítulo 10 · p.23; Capítulo 18 · p.41;
`registro-decisiones-d2.md`

## 1. Convenciones

- `CA-01` a `CA-29`: criterios de aceptación del caso.
- `R-01` a `R-14`: restricciones no negociables del caso.
- `D-01` a `D-26`: decisiones del registro D2.
- **Propuesto:** formulación de solución D2 para atender la fuente citada; no implica aprobación ni cumplimiento.
- **Condicionado:** depende de una validación jurídica, tributaria, comercial o técnica todavía pendiente.
- Las consultas se consideran propuestas de interpretación, no respuestas del CLIENTE.
- Cuando las Bases no fijan un umbral, el requisito remite a la meta comprometida en
  `criterios-aceptacion-d2.md`, que distingue resultado obligatorio, meta del PROPONENTE
  y parámetro a fijar en la Etapa 1.
- La exigencia normativa reside en la fuente; los mecanismos, etapas y metas D2 son
  decisiones de alcance de D2. Ningún estado de esta tabla acredita cumplimiento.

## 2. Requisitos funcionales

| ID | Requisito verificable | Origen | Prioridad | Etapa | Verificación | Estado |
|---|---|---|---|---|---|---|
| RF-001 | Antes de autorizar un viaje, comprobar jornada disponible, habilitaciones del conductor y equipos, y aptitud y compatibilidad del tractocamión y semirremolque. Todo incumplimiento legal o de seguridad deberá bloquear la asignación. | CA-01; R-07; D-06 | Must | E1 | Casos válidos, vencidos, incompatibles y sin evidencia; bitácora de bloqueos. | Propuesto |
| RF-002 | Obtener, asociar al viaje y presentar evidencia de jornada efectiva de los 454 conductores, incluidos externos, distinguiendo dato declarado, tacógrafo y otras fuentes. | CA-02; R-02; R-07; D-01; D-13 | Must | E1 | Piloto propio/externo, conciliación y revisión legal. | Condicionado |
| RF-003 | Al asignar un viaje a un conductor externo, disponer de evidencia identificada y sellada de su jornada previa relevante, incluida la realizada para otros clientes cuando sea legal y contractualmente accesible. | CA-03; R-02; R-07; D-01 | Must | E1 | Casos con jornada suficiente, insuficiente, ausente y corregida. | Condicionado |
| RF-004 | Conservar evidencia de jornada con origen, sello temporal, integridad verificable e historial de correcciones sin sobrescritura. | CA-04; D-13; D-24 | Must | E1 | Prueba de alteración, cadena de custodia y auditoría. | Condicionado |
| RF-005 | Consolidar las aproximadamente 6.000 vigencias en un registro único con titular, responsable de renovación, custodio, vencimiento, respaldo, alertas y efecto sobre la asignación. Umbrales: meta por ratificar. | CA-05; D-18 | Must | E1 | Conciliación con las cuatro planillas y pruebas de alerta/bloqueo. | Condicionado |
| RF-006 | Antes del despacho de carga peligrosa, verificar que la carga efectiva corresponda al manifiesto y vincular carga, vehículo, conductor, habilitaciones y evidencia del punto de carga. | CA-06; R-09; D-19 | Must | E1 | Casos con coincidencia, discrepancia y evidencia ausente. | Condicionado |
| RF-007 | Descargar la información disponible de tacógrafos, asociarla con conductor y vehículo, conservar el original y permitir su consulta. Periodicidad: meta por ratificar. | CA-07; R-02; R-03; D-13 | Must | E1 | Piloto por modelo y prueba de contingencia física. | Condicionado |
| RF-008 | Entregar a la torre una vista única con posición, fuente, antigüedad y nivel de evidencia de los 374 camiones, explicitando unidades sin señal o sin adhesión. | CA-08; R-02; R-03; D-04; D-26 | Must | E1 | Conciliación del padrón y simulación de pérdida de señal/no adhesión. | Condicionado |
| RF-009 | Cada unidad intervenida deberá registrar localmente al menos 72 horas de posición, eventos, jornada, permanencias y documentos, sin pérdida, y sincronizarlos después. | CA-09; R-03; R-04; D-11; D-26 | Must | E1 | Ensayo desconectado de 72 horas y reconciliación extremo a extremo. | Condicionado |
| RF-010 | Registrar automáticamente llegada y salida en instalaciones de clientes, sin interacción del conductor ni equipos instalados allí, conservando fuente, precisión y sello temporal. | CA-10; R-01; R-09; D-08 | Must | E1 | Prueba en terreno con falsos cruces y ausencia de cobertura. | Propuesto |
| RF-011 | Generar evidencia consultable de tiempos de espera y relacionarla con viaje, reglas contractuales y cobro de sobreestadía. Meta D2 ratificada: objeciones ≤20 % de cobros respaldados en E2. | CA-11; D-08 | Must | E1 | Muestreo de cobros y medición de tasa de objeción. | Condicionado |
| RF-012 | Obtener conformidad mediante firma y OTP del receptor identificado, con sello temporal, ubicación y evidencia; operar offline y sincronizar después. Meta D2 ratificada: cero pérdidas y ≥99 % disponible el mismo día. | CA-12; R-04; R-09; D-10 | Must | E1 | Casos de aceptación, rechazo, ausencia y operación offline. | Condicionado |
| RF-013 | Generar desde la orden la información requerida para el documento electrónico de transporte, sin redigitación y manteniendo al sistema contable como único emisor tributario. | CA-13; R-08; D-03; D-09 | Must | E1 | Comparación campo a campo y prueba de integración. | Propuesto |
| RF-014 | Disponer del documento electrónico de transporte conforme antes de iniciar el movimiento, incluso en puntos de carga sin cobertura, mediante un mecanismo declarado, validado y soportado por el sistema contable como único emisor. Una solicitud en cola para emisión posterior no satisface el requisito; sin documento conforme se bloquea la salida. | CA-14; R-04; R-08; D-09 | Must | E1 | Documento conforme anterior al movimiento en escenario sin cobertura; bloqueo si falta; validación tributaria, reintentos sin duplicación ni redigitación. | Condicionado |
| RF-015 | Recomendar retornos que maximicen el margen esperado después de respetar ubicación, jornada, habilitaciones, compatibilidad, plazo, nivel de servicio y aceptación. Meta D2 ratificada: kilómetros vacíos ≤18 % en población comparable. | CA-15; R-02; D-14 | Should | E2 | Piloto antes/después y registro de recomendaciones. | Condicionado |
| RF-016 | Conocer sistemáticamente el costo real por kilómetro y viaje, ruta y contrato; publicar el costo consolidado por viaje dentro de 24 horas de su cierre, con componentes disponibles y faltantes explícitos, y disponer del costo real por ruta antes de la renegociación de 2027. D2 ratifica versionado inicial/consolidado sin sobrescritura y meta E1 de ≥95 % de viajes trazables y 100 % de rutas y contratos modelados; debe validarse su equivalencia con RT-05.29. | CA-16; CA-17; CA-19; FEP03 cap.15 RT-05.29; D-15; D-16; D-17 | Must | E1 | Medir cierre-publicación ≤24 h, componentes disponibles/pendientes, costo por km y conciliación posterior sin sobrescritura; validar tratamiento de estimaciones. | Condicionado |
| RF-017 | Distinguir costo interno de flota propia y costo contractual de usar flota subcontratada; incorporar costos internos del tercero solo con información open-book autorizada. | CA-16; R-02; D-16 | Must | E1 | Revisión con Finanzas y tres escenarios de flota. | Condicionado |
| RF-018 | Relacionar kilometraje, consumo, ruta, vehículo, conductor y condiciones para explicar la dispersión de rendimiento entre camiones comparables. Meta D2 ratificada: explicar ≥80 % de la variación comparable. | CA-18; D-12; D-15 | Should | E2 | Análisis reproducible sobre muestra comparable. | Condicionado |
| RF-019 | Calcular la liquidación del transportista desde viajes, tarifas, anticipos, peajes, sobreestadías y ajustes, dejando la intervención manual como excepción auditable. Meta D2 ratificada: ≤1 día hábil y ≤2 % de correcciones en E1. | CA-20; D-03; D-16 | Must | E1 | Ejecución paralela y conciliación con proceso actual. | Condicionado |
| RF-020 | Permitir a cada transportista autenticado consultar sus viajes, estados, evidencias y liquidación en curso, restringidos a su operación. | CA-21; CA-29; D-02; D-23 | Must | E1 | Aceptación y pruebas de segregación de datos. | Propuesto |
| RF-021 | Permitir al cliente autorizado consultar posición y estado de su carga solo durante el servicio y dentro de lo autorizado por el titular de los datos. | CA-22; R-02; R-03; D-23 | Must | E1 | Acceso antes, durante y después del viaje. | Condicionado |
| RF-022 | Permitir al dueño otorgar, consultar y revocar permisos por camión, viaje, dato, destinatario y periodo, manteniendo bitácora y distinguiendo captura futura, visibilidad y retención obligatoria. Meta D2 ratificada: revocación de datos futuros efectiva en ≤5 min. | CA-23; CA-29; R-02; R-03; D-23 | Must | E1 | Casos de consentimiento/revocación y auditoría de accesos. | Condicionado |
| RF-023 | Calcular emisiones de CO2e por tonelada-kilómetro con metodología ISO 14083/GLEC declarada y verificable, incluidos terceros, y consolidación mensual. Decisión D2 ratificada: base, línea base y método en E1; cálculo productivo completo en E2, con consumo real donde exista y factores documentados y versionados. | CA-24; FEP03 cap.15 RT-05.29; R-02; D-22 | Must | E1 base/metodología; E2 productivo completo | E1: revisar fuentes, línea base y método; E2: reproducción independiente del cálculo y consolidación mensual, incluidos terceros. | Condicionado |
| RF-024 | Permitir que un taller externo registre una intervención, incluso offline, identificando taller, técnico, activo, fecha, kilometraje, trabajo, repuestos y evidencia, con validación previa a la hoja de vida. Meta D2 ratificada: ≥95 % recibidas y 100 % de las validadas incorporadas. | CA-25; R-04; R-09; D-21 | Should | E2 | Prueba con taller, aprobación, corrección y sincronización. | Condicionado |
| RF-025 | Gatillar mantenimiento preventivo con kilometraje real trazable y mostrar explícitamente el nivel de estimación cuando no exista telemetría. | CA-26; R-03; R-06; D-12; D-21 | Must | E1 | Comparación con odómetro y prueba de órdenes. | Condicionado |
| RF-026 | Administrar adhesión de los 148 transportistas, registrando invitación, condiciones, consentimiento, estado, fecha, equipos y capacidades habilitadas. Meta D2 ratificada: ≥70 % (104/148) al cierre E1 y ≥90 % (134/148) al cierre E2. | CA-27; R-02; R-03; D-02; D-05 | Must | E1-E2 | Reporte periódico y muestreo contractual. | Condicionado |
| RF-027 | Calcular a bordo una alerta anticipada según jornada restante, ubicación, ruta y tiempo hasta un lugar seguro. Margen mínimo: meta por ratificar. | CA-28; R-01; R-04; D-07 | Must | E1 | Prueba en rutas piloto, incluido caso sin lugar alcanzable. | Condicionado |
| RF-028 | Durante la transición, distinguir validación telemática completa y documental controlada, sin presentar el modo degradado como equivalente ni reducir controles legales o de seguridad. | CA-01; CA-02; CA-08; CA-27; R-02; R-03; R-07; D-26 | Must | E1 | Operación mixta y auditoría de bloqueos. | Condicionado |

## 3. Requisitos no funcionales

| ID | Requisito verificable | Origen | Prioridad | Etapa | Verificación | Estado |
|---|---|---|---|---|---|---|
| RNF-001 | Ninguna función exigirá interacción del conductor con un dispositivo mientras el vehículo esté en movimiento; toda captura y alerta en marcha será automática. | R-01; CA-10; CA-28 | Must | E1 | Prueba en vehículo y revisión de interfaces. | Propuesto |
| RNF-002 | La operación esencial a bordo no dependerá de cobertura y conservará integridad, orden, sello temporal y ausencia de duplicados al sincronizar. | R-04; CA-09; D-11 | Must | E1 | Desconexión de 72 horas y reconciliación. | Propuesto |
| RNF-003 | No se intervendrán equipos de terceros sin acuerdo expreso; las capacidades no autorizadas permanecerán deshabilitadas y visibles como tales. | R-02; R-03; D-02; D-04 | Must | E1 | Revisión contractual y caso no adherido. | Propuesto |
| RNF-004 | Toda intervención física a bordo ocurrirá durante el paso normal por terminal, sin inmovilización adicional no declarada. Duración y despliegue: metas por ratificar. | R-05; R-10; R-11; D-25 | Must | E1 | Pilotos cronometrados por familia. | Condicionado |
| RNF-005 | La integración vehicular será de solo lectura, no interferirá con seguridad y tendrá autorización del fabricante cuando pueda afectar la garantía. | R-06; D-12 | Must | E1 | Autorización por modelo y prueba de no escritura. | Condicionado |
| RNF-006 | El sistema contable seguirá como único emisor tributario; la integración evitará emisiones paralelas y será idempotente ante reintentos. | R-08; D-03; D-09 | Must | E1 | Prueba de emisión única y reintentos. | Propuesto |
| RNF-007 | La solución no requerirá equipamiento propio ni impondrá procedimientos en puntos de carga o descarga de terceros. | R-09; CA-10; CA-12 | Must | E1 | Inspección y piloto en instalaciones externas. | Propuesto |
| RNF-008 | La continuidad absorberá cierres de Los Libertadores de hasta 12 días, preservando evidencia y sincronizando al recuperarse la operación. | R-04; R-12; D-20 | Must | E1 | Simulación de cierre y revisión del protocolo. | Condicionado |
| RNF-009 | La solución será administrable por el área TI de nueve personas; toda especialidad dedicada no disponible se entregará como servicio con responsabilidades y niveles explícitos. | R-13 | Must | E1 | Revisión RACI y prueba operativa. | Propuesto |
| RNF-010 | Se declarará y evaluará el costo total de operación de 36 meses: suscripciones, conectividad, nube, soporte, mantención, reposición y retiro. | R-14; D-05; D-11 | Must | E1 | Revisión del TCO y trazabilidad económica. | Condicionado |
| RNF-011 | Los despliegues no detendrán globalmente la flota y permitirán convivencia controlada entre unidades equipadas, homologadas y no adheridas. | R-05; R-10; R-11; D-25; D-26 | Must | E1 | Ensayo de despliegue progresivo. | Condicionado |
| RNF-012 | Los registros probatorios mostrarán autor, origen, fecha, valores anteriores/posteriores y cadena de custodia, sin sobrescribir el historial. | CA-04; D-24 | Must | E1 | Pruebas de modificación/borrado y auditoría. | Condicionado |
| RNF-013 | Los datos personales y comerciales aplicarán minimización, acceso por rol y atributo, cifrado en tránsito/reposo y protección reforzada de geolocalización, jornada y tarifas. | CA-23; CA-29; D-23; D-24 | Must | E1 | Pruebas de autorización y revisión criptográfica. | Condicionado |
| RNF-014 | La conservación y eliminación respetarán plazos por dominio; la revocación no eliminará evidencia cuya retención sea legal o contractualmente obligatoria. | CA-04; CA-23; D-13; D-23; D-24 | Must | E1 | Pruebas de archivo, eliminación y excepción legal. | Condicionado |

## 4. Cobertura de criterios de aceptación

Los enlaces de esta sección y de la siguiente indican cobertura documental propuesta,
no satisfacción demostrada de los criterios o restricciones.

| Criterio | Requisitos |
|---|---|
| CA-01 | RF-001, RF-028 |
| CA-02 | RF-002, RF-028 |
| CA-03 | RF-003 |
| CA-04 | RF-004, RNF-012, RNF-014 |
| CA-05 | RF-005 |
| CA-06 | RF-006 |
| CA-07 | RF-007 |
| CA-08 | RF-008, RF-028 |
| CA-09 | RF-009, RNF-002 |
| CA-10 | RF-010, RNF-001, RNF-007 |
| CA-11 | RF-011 |
| CA-12 | RF-012, RNF-007 |
| CA-13 | RF-013 |
| CA-14 | RF-014 |
| CA-15 | RF-015 |
| CA-16 | RF-016, RF-017 |
| CA-17 | RF-016 |
| CA-18 | RF-018 |
| CA-19 | RF-016 |
| CA-20 | RF-019 |
| CA-21 | RF-020 |
| CA-22 | RF-021 |
| CA-23 | RF-022, RNF-013, RNF-014 |
| CA-24 | RF-023 |
| CA-25 | RF-024 |
| CA-26 | RF-025 |
| CA-27 | RF-026, RF-028 |
| CA-28 | RF-027, RNF-001 |
| CA-29 | RF-020, RF-022, RNF-013 |

## 5. Cobertura de restricciones no negociables

| Restricción | Requisitos |
|---|---|
| R-01 | RF-010, RF-027, RNF-001 |
| R-02 | RF-002, RF-003, RF-007, RF-008, RF-015, RF-017, RF-021, RF-022, RF-023, RF-026, RF-028, RNF-003 |
| R-03 | RF-007, RF-008, RF-009, RF-021, RF-022, RF-025, RF-026, RF-028, RNF-003 |
| R-04 | RF-009, RF-012, RF-014, RF-024, RF-027, RNF-002, RNF-008 |
| R-05 | RNF-004, RNF-011 |
| R-06 | RF-025, RNF-005 |
| R-07 | RF-001, RF-002, RF-003, RF-028 |
| R-08 | RF-013, RF-014, RNF-006 |
| R-09 | RF-006, RF-010, RF-012, RF-024, RNF-007 |
| R-10 | RNF-004, RNF-011 |
| R-11 | RNF-004, RNF-011 |
| R-12 | RNF-008 |
| R-13 | RNF-009 |
| R-14 | RNF-010 |

## 6. Validaciones pendientes después de la ratificación D2

1. Confirmar con D3/D4 la viabilidad de la cobertura sobre 374 camiones y los componentes propuestos.
2. Validar jurídicamente jornada externa, tacógrafos, firma/OTP y valor probatorio de la evidencia.
3. Confirmar un mecanismo soportado por el sistema contable que entregue el documento conforme antes del movimiento aun sin cobertura; no aceptar solo emisión diferida.
4. Costear y formalizar el ciclo de vida contractual del dispositivo financiado por AUDIT.
5. Levantar el catálogo de lugares seguros y fijar la anticipación de alertas.
6. Conciliar revocación de datos futuros, visibilidad y retención legal de geolocalización.
7. Resuelto. Son 3 los contratos servidos bajo costo, equivalentes al 31 % del ingreso, y 2 de ellos se renegocian en 2027 (FEP03 · Sección 7.3 · p.15 y Sección 13.2 · p.27).
8. Fijar las metas que continúan pendientes y validar la viabilidad de las ya ratificadas por D2.
9. Validar ISO 14083/GLEC, factores y cobertura sin presentar E1 como cumplimiento completo de CA-24.
10. Validar el diseño de costeo frente a CA-16/17/19 y FEP03 RT-05.29; una versión llamada inicial no acredita por sí sola el costo consolidado exigido.
