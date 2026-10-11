# Subdocumento 5. Modelo y gestión de datos

audIT, Empresa N.º 10. Licitación TFEP-01/2026, Caso 10 Transporte de Carga. Oferta Técnica, Sobre N.º 2. Informe Preparatorio 2. Archivo AUDIT-Subdocumento5.pdf.

## Resolución de observaciones del Informe 1

La tabla de resolución registra los cambios de diseño para el Informe 2 y su evidencia documental (FEP01 · Artículo 46° · p.28). La aceptación de implementación requiere S9/T-17 y revisión humana.

| N.º | Observación | Respuesta de diseño | Evidencia |
|---|---|---|---|
| 13, 85 | Bitácora interna en el cuerpo | Apertura con dominio y gobierno; el registro de IA se entrega por separado | 5.1 y declaración final |
| 81 | Evidencia de jornada ausente | Original, fuente, nivel, estado, identidad, sellos, rectificación y veredicto separados | 5.1.5, Figura 5.4 y anexo de diccionario |
| 82 | Falta diagrama entidad-relación | Dos modelos legibles por dominio con PK, referencias y multiplicidades | Figuras 5.1 y 5.4 |
| 83 | Residencia contradictoria | Chile Central primario y Brazil South secundario con mecanismo jurídico y DR probado antes de activación | 5.1.6 y 5.2.3 |
| 84 | Motor temporal y bus abiertos | TimescaleDB en servidor separado; Event Hubs Premium mediante protocolo Kafka | 5.2.1 y S4.1.1 |
| 86 | Prosa y figuras sin análisis | Gráficos de relaciones, custodia, permisos, persistencia, CDC, migración y desempeño recorridos en el texto | Figuras 5.1–5.9 |
| 87 | Revocación y retención no validadas | Cesar la compartición, separar base de tratamiento y conservar obligaciones; sanitización verificable al vencer plazos | 5.1.6; CP-SEC-05/08 y CP-INT-25 |

Estos cambios resuelven las diferencias de especificación. Los resultados de ensayos, acreditación documental y revisión jurídica no se presentan como ejecutados.

## 5 Modelo y gestión de datos

El modelo conserva el viaje ocurrido y sus respaldos sin mezclarlo con el costo estimado, el documento fiscal o el permiso de compartir datos. S3 fija reglas y alcance; S4.1 define servicios y contratos; S6/S7 organizan su construcción y migración; S9 comprueba que una decisión pueda reconstruirse a partir de la evidencia original. El CLIENTE recibe modelos por dominio, diccionario de atributos, gobierno de maestros, plazos de conservación y criterios de conciliación.

## 5.1 Modelo

Los seis contextos canónicos tienen propietarios explícitos. Compartir una identidad o referenciar un viaje no autoriza a un servicio a escribir en la base de otro. Las claves globales facilitan correlación y deduplicación; las restricciones de negocio se implementan en el contexto responsable.

### 5.1.1 Decisiones del modelo

La Tabla 5.1 vincula cada decisión con una necesidad del Caso, sin atribuir al legado un esquema que no se ha levantado.

**Tabla 5.1.** Decisiones de modelado y efecto operacional

| Decisión | Necesidad | Consecuencia verificable |
|---|---|---|
| Separar orden, viaje y asignación | Distinguir servicio solicitado, recursos reservados y recorrido efectivo | Reasignar recursos no borra la historia ni cancela automáticamente el viaje |
| Distinguir tracto y semirremolque | Aptitud y combinaciones de carga | Vigencias y compatibilidad por activo, no por una entidad genérica de camión |
| Evidencia, evaluación y permisos separados | Jornada impugnable y control del dato de terceros | Reconstruir qué fuentes se usaron, con qué regla y quién autorizó una excepción |
| Maestros con propietario único | Cuatro planillas de ≈6.000 vigencias y sistemas existentes | Identidad, respaldo y discrepancias conciliados antes de habilitar |
| Separar negocio, series y análisis | Asignación ≤30 s y ráfagas de reconexión | Ensayar cargas simultáneas y consultas de BI aisladas del OLTP |
| Versionar costo y liquidación | Combustible tardío y liquidación mensual | v1 ≤24 h con faltantes; posteriores versiones sin sobrescritura |

La Tabla 5.1 fija la estructura que se comprueba en S9. El cifrado y los índices son controles complementarios; ninguno acredita por sí solo cumplimiento legal, exactitud documental o latencia.

### 5.1.2 Dominios de información y modelo conceptual

La arquitectura de datos se estructura en seis contextos delimitados con límites explícitos. En la Figura 5.1 se despliega el modelo conceptual y relacional de persistencia de datos.

![Figura 5.1. Modelo lógico de las relaciones críticas del viaje](./graficos/audit-figura-5.1-erd.png)

*Figura 5.1. Modelo lógico de las relaciones críticas del viaje*

Fuente: elaboración D3 con el lienzo de D4.

La Figura 5.1 separa el ciclo del viaje de las asignaciones: una orden genera cero o varios viajes y cada viaje conserva cero o varias asignaciones históricas. Cada asignación confirmada identifica conductor, tracto y, cuando la carga lo exige, semirremolque; no puede solaparse con otra activa para esos recursos. Documento, costo y evaluación mantienen su identificador y relación con el viaje o la asignación. En el gráfico, EVAL_ASIGNACION abrevia EVALUACION_ASIGNACION y DOCUMENTO_TRANSP. abrevia DOCUMENTO_TRANSPORTE.

Los contextos gobiernan estos agregados: Planificación conserva OrdenTransporte y la reserva de Asignación; Operación conserva Viaje y su ejecución; Flota conserva Tractocamion y Semirremolque; Personas conserva Conductor, EvidenciaJornada y EvaluacionAsignacion; Liquidación conserva CostoVersion y Liquidacion. Transportista y Cliente tienen identidad compartida con un propietario de atributo declarado en MDM.

El ciclo propuesto del viaje es `PROGRAMADO → EN_CARGA → EN_RUTA → EN_DESCARGA → CERRADO`, con `CANCELADO` como excepción trazable. `BLOQUEADA` es resultado de una evaluación de asignación, no un sexto estado que termine el viaje por fatiga: puede buscarse otro recurso y volver a evaluar. El rechazo de carga en destino conserva evento, motivo y resolución; no elimina recorrido ni costos ya incurridos. Un cierre de frontera registra demora y causa; su efecto sobre cobros depende de la regla contractual, sin congelar sobreestadías automáticamente por RT-10.05.

### 5.1.3 Estrategia de Gestión de Datos Maestros (MDM)

En cumplimiento de FEP02, RT-05.09, p. 11, se implementa un marco centralizado de Master Data Management (MDM) con principio de Registro Maestro Único (*Golden Record*), visualizado en la Figura 5.2.

![Figura 5.2. Gestión de Datos Maestros (MDM) y Capa Anticorrupción](./graficos/audit-figura-5.2-mdm.png)

*Figura 5.2. Gestión de Datos Maestros (MDM) y Capa Anticorrupción*

Fuente: elaboración D3 con el lienzo de D4.

La Figura 5.2 identifica propietarios y conciliación: Personas gobierna conductor/evidencia/habilitación; Flota, activos y taller; Planificación, órdenes y puntos de servicio; el contable conserva identidad comercial y de facturación según el contrato de integración. Las tarifas operacionales cambian de autoridad por función en M16/M21 según S3; no existe doble escritura maestra.

Cada registro mantiene ID global y clave natural validada. El RUT usa validación sintáctica de dígito verificador y contraste documental; la patente se normaliza y contrasta con antecedentes autorizados. No se promete una API del Registro Civil ni una consulta oficial automática sin acceso acreditado. Los duplicados o fuentes contradictorias quedan en cuarentena con resolución del propietario y trazabilidad del origen.

### 5.1.4 Diccionario de datos y restricciones

El [anexo de diccionario](./subdocumento_05_anexos_diccionario.md) entrega por atributo nombre, tipo, dominio, obligatoriedad, propietario y sensibilidad, conforme a FEP02 · RT-05.01 · p.11 y Comunicado 10 · capítulo 5. Las Figuras 5.1/5.4 muestran relaciones legibles; el cuerpo analiza las restricciones que determinan la operación.

Una vigencia referencia exactamente un conductor, un tracto o un semirremolque mediante tres FK nullable y un `CHECK` de un único sujeto. Se evita una FK polimórfica que PostgreSQL no pueda comprobar. El estado `VERIFICADO` requiere respaldo y fecha de verificación; también se comprueba vencimiento, tipo requerido y eventual revocación. Una fecha futura en una planilla no equivale a aptitud acreditada.

El viaje puede programarse sin recursos ni peso definitivo. La asignación sólo se confirma con recursos y evaluación válida; pasar a `EN_RUTA` requiere además carga definitiva y documento conforme. La posición se almacena con latitud y longitud ambas presentes o ambas ausentes. Identidad, velocidad, odómetro y hora del evento se dejan nulos cuando la fuente no los proporciona; la hora de recepción y la procedencia siempre quedan registradas. No se generan ceros para representar desconocimiento.

### 5.1.5 Evidencia de jornada, cascada y cadena de custodia

La evidencia se clasifica conforme al contrato de S3 y a la corrección de D1: fuente instrumental, nivel, estado, modalidad y veredicto son dimensiones distintas. La Tabla 5.2 conserva la correspondencia canónica.

**Tabla 5.2.** Niveles de evidencia de jornada y uso en la validación

| **Origen o código conservado** | **Nivel canónico** | **Condición de interpretación** | **Modalidad y veredicto esperado** |
|---|---|---|---|
| Tacógrafo digital descargado (`TACO_DIG`) | 1 | Conservar original, identidad y vínculo a vehículo/viaje; validar integridad antes de asignar | Se evalúa con los demás controles de asignación; un incumplimiento legal siempre bloquea |
| Equipo a bordo con conductor identificado (p. ej., código de origen CAN o GPS) | 2 | Solo se asigna este nivel si la identidad del conductor y el vínculo al evento están verificados; el código instrumental no basta | En modalidad completa, el nivel 2 es la evidencia prevista por S3; el veredicto sigue sujeto a los controles legales y operacionales |
| Telemetría de fábrica (`TEL_FAB`) | 3 | Lectura autorizada, de solo lectura, con origen, cobertura y hora de recepción trazables | Se evalúa como nivel 3; no se infiere identidad personal ni descanso únicamente desde telemetría del vehículo |
| Reposo del camión (`REPOSO_CAM`) | 4 | Sin coordenadas; acredita estado del vehículo, no descanso personal | En modalidad de datos requiere atestación firmada de nivel 5 para asignar con marca; sin ella bloquea |
| Atestación firmada del transportista (`ATEST_TRAN`) | 5 | Firma, responsable, fecha y viaje identificados y validados | Asignación con marca y responsabilidad registrada; en modalidad sin adhesión habilita solo la validación documental acompañada de atestación válida |
| Registro voluntario del conductor (`REG_COND`) | 0 | Captura identificada y trazable, sin elevar su valor probatorio | Informativo; nunca es requisito ni cambia el veredicto |
| Evento de portería | — | Puede complementar la trazabilidad de entrada o salida; no acredita por sí mismo jornada o descanso | No crea un nivel ni habilita asignación por sí solo |
| Sin evidencia (`SIN_EVIDENCIA`) | `NULL` | No existe una fuente válida asociada | Bloquea, salvo la excepción acotada de RN-04; nunca levanta un bloqueo legal |
| Código fuente desconocido (`CODIGO_FUENTE_DESCONOCIDO`) | `NULL` | Conservar el código original sin asignarle nivel hasta homologarlo | Rechaza la integración y bloquea el veredicto habilitante |
| Evidencia inválida (`EVIDENCIA_INVALIDA`) | `NULL` | Conservar el artefacto y el motivo de rechazo para auditoría, sin tratarlo como nivel 0 | Bloquea el veredicto habilitante |

El nivel clasifica la evidencia y no certifica por sí solo su valor judicial. Los códigos de origen (CAN, GPS, portería u otro) se conservan sin convertirlos en niveles: CAN instalado en un equipo a bordo no equivale a telemetría de fábrica. Las plataformas de terceros se integran únicamente mediante lectura o exportación autorizada; no se presume API ni webhook.

La evaluación de asignación vinculada conserva por separado `modalidad_adhesion`, `veredicto_asignacion`, versión de regla y marca temporal, junto con las referencias a conductor, viaje y evidencia. La modalidad completa aplica la evidencia de nivel 2 prevista por S3; la modalidad de datos requiere reposo de nivel 4 complementado por atestación firmada de nivel 5 y produce asignación con marca; sin adhesión, la validación documental solo habilita con atestación válida y también deja marca. La falta de fuente bloquea, salvo la excepción acotada de RN-04. Un incumplimiento legal bloquea en todas las modalidades y el nivel 0 nunca modifica el resultado. Estos casos se cotejan con T-17, CP-SYS-05 y CP-UAT-09.


El origen recibido se conserva sin renumeración silenciosa. Una descarga de tacógrafo, un evento de equipo o una atestación mantiene original, emisor/dispositivo, versión de esquema, ID, marca temporal si existe, hora de recepción, hash y resultado de validación. `id_conductor` puede ser nulo en un artefacto no identificado; ese artefacto se conserva para auditoría y no se convierte por sí solo en jornada personal habilitante. La vinculación exige identidad acreditada y período coherente.

`EVIDENCIA_JORNADA` conserva artefactos válidos, desconocidos o inválidos; la ausencia se expresa en `EVALUACION_ASIGNACION` como `SIN_EVIDENCIA`, sin inventar una fila de evidencia. `nivel_cascada` es NULL para origen desconocido/inválido; 0 sólo para `REG_COND`; 1–5 según la fuente válida y la condición canónica. Un nivel válido no elimina un incumplimiento legal. La hora GNSS/NTP se compara con la de recepción y se registra deriva o calidad del reloj; no se llama reloj atómico ni se reemplaza la hora original para aparentar exactitud.

La Figura 5.3 recorre recepción, validación, sellado, conservación y rectificación.

![Figura 5.3. Cadena de custodia de evidencias y tratamiento de fuentes inválidas](./graficos/5-2-custodia.png)

*Figura 5.3. Custodia de jornada. Fuente: elaboración D3 con el lienzo de D4.*

El hash permite detectar alteración; no es firma electrónica ni vuelve inmutable una fila por sí solo. Se conserva el original firmado cuando procede, se encadenan registros con identificador de cadena y secuencia, y se anclan segmentos y manifiestos en almacenamiento WORM con retención bloqueada, bajo administración separada. Las cuentas de aplicación carecen de UPDATE/DELETE/TRUNCATE sobre evidencia. La protección frente al administrador se acredita en el almacenamiento inmutable y con verificación independiente; revocar permisos SQL al usuario aplicativo no restringe por sí solo a un superusuario.

Las rectificaciones generan un registro nuevo que referencia el original, sin sobrescribirlo. El primer hash previo es NULL y existe un único inicio por cadena; el orden es secuencia de custodia, distinto del orden de ocurrencia de eventos tardíos. Un acuse de sincronización requiere commit duradero. La confirmación probatoria incorpora el sellado y respaldo exigidos por el dominio; su falta se muestra y se ensaya, sin declarar evidencia plenamente custodiada cuando sólo fue admitida por el bus.

La Figura 5.4 separa evaluación y evidencia mediante `EVALUACION_EVIDENCIA`: una evaluación puede usar reposo de nivel 4 y atestación de nivel 5 simultáneamente. El veredicto siempre se registra, aun sin evidencia válida. Una excepción RN-04 conserva dos aprobadores, motivo, un viaje y revisión mensual; no levanta una causa legal. Las restricciones y nulabilidad se detallan en el anexo.

![Figura 5.4. Modelo lógico de evidencia, evaluación, excepción y permiso](./graficos/5-7-evidencia.png)

*Figura 5.4. Relaciones de la evaluación de asignación. Fuente: elaboración D3 con el lienzo de D4.*

La Tabla 5.2 y la Figura 5.4 se cotejan con CP-SYS-05/CP-UAT-09: nivel 0, nivel 5, modalidad de datos, atestación ausente, fuente desconocida y bloqueo legal. Una base migrada conserva los códigos anteriores, su tabla de correspondencia y la versión del mapeo; no altera la evidencia original para hacerla coincidir con el nuevo esquema.

### 5.1.6 Soberanía, permisos y bases de tratamiento

El permiso del transportista controla qué datos de sus recursos comparte, con quién, para qué finalidad y durante qué servicio (FEP03 · RT-16.30 · p.33). No sustituye la base de tratamiento de datos personales del conductor. El modelo distingue permiso comercial, adhesión contractual y base jurídica; la localización es dato personal cuando identifica o permite identificar a una persona, sin clasificar automáticamente toda localización como categoría legal de dato sensible.

La Figura 5.5 muestra concesión, evaluación por petición, revocación y decisión de conservación. `PERMISO_COMPARTIR` mantiene recurso, destinatario, alcance, finalidad, vigencia, versión y respaldo; `ACCESO_DATO` conserva qué se mostró y bajo qué versión. Una lista JSON de clientes no reemplaza relaciones verificables ni la auditoría de cada acceso.

![Figura 5.5. Compartición autorizada, revocación y conservación](./graficos/5-3-permisos.png)

*Figura 5.5. Ciclo de permisos. Fuente: elaboración D3 con el lienzo de D4.*

La revocación cesa nuevas consultas y emisiones cubiertas por el permiso, invalida caché/credenciales de acceso y propaga una versión al dispositivo. Durante falta de enlace no puede recibir una revocación nueva: el permiso local tiene vencimiento y sólo se transmiten datos tras comprobar la versión al reconectar. La transmisión de emergencia y los registros obligatorios siguen su base específica y minimización; revocar compartición comercial no borra evidencia de jornada ni elimina obligaciones de seguridad.

FEP01 · Artículo 4.2° · p.5 exige Ley 21.719 y, mientras esté vigente, Ley 19.628. La Ley 21.719 entra en vigor el 01-12-2026; el inicio supuesto de febrero de 2027 cae bajo el régimen nuevo. Curimón debe documentar finalidad, base, derechos, encargos, plazos y transferencias. El cifrado de campo exigido por RT-11.10 no reemplaza esos deberes ([BCN, Ley 21.719](https://www.bcn.cl/leychile/navegar?i=1209272)).

Chile Central es primario y Brazil South es secundario propuesto en S4.3. Una réplica de datos personales es transferencia internacional: requiere identificar responsable y destinatario y documentar una vía aplicable del artículo 27 y las salvaguardias del artículo 28. Ubicación sudamericana y cifrado no acreditan por sí solos licitud. Si no se documenta el mecanismo, no se activa esa réplica; tampoco se declara satisfecho el DR hasta disponer de un sitio secundario admisible que supere RPO ≤15 min y RTO ≤4 h. La revisión jurídica y la prueba de recuperación son condiciones de puesta en operación.

Una supresión solicitada se resuelve por dato y finalidad: conservar protegido lo sujeto a retención o litigio, cesar usos no autorizados y eliminar cuando proceda. El procedimiento incluye BD, originales, índices, cachés, exportaciones autorizadas, réplicas y respaldos; registra alcance, retenciones vigentes y fecha efectiva. NIST SP 800-88 Rev. 2 sustituye la revisión 1 desde septiembre de 2025. La destrucción criptográfica sólo se usa cuando el diseño de claves y todas sus copias lo permite; no se promete irrecuperabilidad absoluta ni purga instantánea de Key Vault ([NIST, SP 800-88 Rev. 2](https://csrc.nist.gov/pubs/sp/800/88/r2/final)).

## 5.2 Gestión de datos

La gestión de datos de audIT define la gobernanza operacional del dato, los motores de persistencia justificados frente a los compromisos de disponibilidad y latencia, y las políticas de retención, respaldo y seguridad.

### 5.2.1 Motores, transacciones y decisión ante partición

FEP02 · RT-05.02 · p.11 exige justificar por dominio consistencia y disponibilidad. CAP se aplica al comportamiento de un sistema distribuido durante una partición; ACID describe transacciones y no clasifica automáticamente un producto como CP/AP. La Tabla 5.3 y la Figura 5.6 concretan la decisión operacional.

**Tabla 5.3.** Persistencia y conducta ante pérdida de enlace

| Dominio | Motor y transacción | Decisión ante partición |
|---|---|---|
| Asignación, vigencias y datos de negocio | PostgreSQL 16 Flexible; transacciones ACID y restricciones | Priorizar consistencia: sin estado autoritativo no confirmar una nueva reserva. RN-04 sólo cubre la fuente de evidencia indisponible; no habilita una reserva global sin conexión |
| Captura de jornada/operación a bordo | SQLite 3 con WAL y outbox local | Continuar captura local y sincronizar después. Consistencia eventual entre copia local y nube; no disponibilidad universal de todas las funciones |
| Telemetría en nube | TimescaleDB sobre PostgreSQL en servidor separado; Event Hubs Premium en ingesta | Acumular localmente si nube no accesible; deduplicar al reconectar. TimescaleDB conserva semántica relacional; no se etiqueta como AP por usar eventos |
| Caché y sesiones | Azure Managed Redis | Dato derivado con versión/expiración. Falla o desactualización conduce a consulta autoritativa; no habilita con una copia obsoleta |
| Documentos y auditoría | Blob Storage con retención inmutable y manifiestos | Conservar original local cifrado hasta confirmar custodia; estado pendiente visible. No afirmar inmutabilidad sólo por un hash |
| Analítica | ADLS Gen2 / Delta y modelo dimensional | Aceptar actualización diferida sin degradar el despacho; publicar antigüedad, faltantes y versiones |

La Tabla 5.3 mantiene una base de negocio consistente y una captura local que resiste particiones. El documento fiscal permanece en el contable y requiere entrega conforme antes del movimiento; el búfer local no habilita emisión propia.

![Figura 5.6. Consistencia del despacho y continuidad de captura durante una partición](./graficos/audit-figura-5.3-cap.png)

*Figura 5.6. Decisiones de persistencia ante partición. Fuente: elaboración D3 con el lienzo de D4.*

El protocolo Kafka de Event Hubs no implica un segundo clúster Apache Kafka ni transacciones exactamente una vez. Se usan outbox, entrega al menos una vez, orden por agregado y deduplicación duradera, conforme a S4.1.

### 5.2.2 Segregación arquitectónica OLTP versus analítica (Lakehouse)

Para dar cumplimiento a FEP02, RT-05.05, p. 11, se separa la base transaccional de producción respecto del consumo analítico de reportería y cálculo de costo por kilómetro. La propagación usa captura de cambios (CDC Debezium) y Event Hubs Premium mediante protocolo Kafka. El objetivo propuesto de retraso CDC <60 s se verifica bajo carga antes de aceptarse; el flujo avanza hacia el repositorio analítico (Delta Lake), como esquematiza la Figura 5.7.

![Figura 5.7. Segregación transaccional OLTP y analítica OLAP mediante CDC](./graficos/audit-figura-5.4-cdc.png)

*Figura 5.7. Segregación transaccional OLTP y analítica OLAP mediante CDC*

Fuente: elaboración D3 con el lienzo de D4.

El modelo de costeo por viaje (Caso, RT-05.29, p. 31) administra el desfase inherente de las liquidaciones de combustible (hasta 40 días) y peajes mensuales, emitiendo una versión preliminar en no más de 24 horas y una versión consolidada definitiva post-cierre sin sobrescribir los registros originales.

### 5.2.3 Políticas de gobernanza, calidad y retención histórica

La calidad se mide en captura y migración según FEP02 · RT-05.04 · p.11 e ISO/IEC 25012. La Tabla 5.4 distingue los atributos que habilitan una transacción de los campos opcionales de una fuente.

**Tabla 5.4.** Calidad y método de comprobación

| Dimensión | Objetivo de aceptación | Comprobación |
|---|---|---|
| Completitud | 100 % de campos exigidos para confirmar asignación/salida; reportar faltantes del resto | Numerador y denominador por entidad y fuente; no convertir NULL en cero |
| Exactitud | Identificadores válidos y documentos cotejados antes de habilitar | Validación sintáctica más respaldo autorizado; una API oficial no se presume |
| Consistencia | Sin asignaciones activas superpuestas ni vigencias sin sujeto/respaldo | FK, CHECK, unicidad/exclusión y ensayos concurrentes |
| Credibilidad | Origen, versión y horas de evento/recepción conservados; deriva visible | Contraste de reloj y orden de secuencia; cuarentena cuando no hay interpretación fiable |
| Accesibilidad | 99,9 % mensual en servicios críticos durante operación | Indicadores de servicio extremo a extremo; HA del motor sola no acredita SLA |

La Tabla 5.4 produce un tablero con errores por fuente, antigüedad, registros en cuarentena y resolución responsable. Las modificaciones y consultas sensibles conservan actor, dispositivo, valores anteriores/posteriores, motivo y correlación (RT-05.03 transversal y RT-16.09 del Caso).

La auditoría es append-only, encadenada y anclada en WORM bajo administración separada. La cuenta de negocio no modifica ni elimina registros de evidencia; una cuenta de administración de BD no puede modificar el original WORM. Los ensayos de integridad comprueban también omisión de eventos y eliminación de segmentos, con manifiestos firmados; el hash de una fila aislada no detecta por sí solo que esa fila desapareció.

La Tabla 5.5 recoge los mínimos de FEP03 · RT-05.10 · p.31. No se atribuye a la ley tributaria una retención que aquí procede del contrato. El punto inicial del cómputo y las retenciones por litigio se documentan por dominio.

**Tabla 5.5.** Retención y recuperación por dominio

| Dominio | Mínimo contractual | Preservación y objetivo |
|---|---|---|
| Jornada y evidencia | 5 años | Original, evaluación y rectificaciones; WAL continuo y segmentos sellados; RTO de diseño ≤2 h |
| Documento y antecedentes del viaje | 6 años | Original fiscal y representación asociados al viaje; RTO de diseño ≤2 h |
| Siniestros | 10 años | Expediente completo y retención por litigio cuando corresponda; RTO ≤4 h |
| Habilitaciones | Vigencia +5 años | Versiones y respaldos, incluidas revocaciones; RTO de diseño ≤2 h |
| Carga peligrosa | 5 años | Documento y lista firmada; RTO de diseño ≤2 h |
| Llegada y salida en cliente | 3 años | Evento y origen preservados; RTO ≤4 h |
| Liquidaciones | 6 años | Versiones, aceptación y acuse contable; RTO de diseño ≤2 h |
| Posición y telemetría | 2 años en línea | Después, agregado diario por unidad/viaje para distancia y consumo según finalidad; sin destruir evidencia sujeta a otros plazos; RTO ≤4 h |

La Tabla 5.5 conserva mínimos y diferencia objetivos internos de los contractuales. Para servicios críticos, RPO ≤15 min y RTO ≤4 h (FEP02 · RT-07.04 · p.17). El desfase real de WAL, objetos y eventos debe medirse conjuntamente; un respaldo diario aislado no cumple RPO de quince minutos.

La política 3-2-1-1-0 incluye producción, copia recuperable localmente segregada y copia fuera de sitio, con almacenamiento de BD y objetos, al menos una copia inmutable y restauración sin errores verificada. Replicación continua no sustituye respaldo recuperable frente a corrupción. Se prueban restauración, conmutación y retorno al menos dos veces al año; el 0 es criterio de aceptación del ensayo, no resultado ya obtenido. La copia extranjera queda sujeta a 5.1.6 y S4.3. Al vencer retenciones y ausentes litigios, la sanitización se documenta con eliminación efectiva de todas las copias o expiración controlada de respaldos, sin reintroducir datos suprimidos al restaurar.

## 5.3 Estrategia de migración

Transportes Curimón S.A. administra cerca de 6.000 vigencias dispersas en cuatro planillas sin validación referencial. En cumplimiento de Caso, RT-05.15, p. 31, ningún registro migrado se considerará habilitante para despachar sin su correspondiente verificación documental individual. En la Tabla 5.6 se detalla el alcance cuantitativo y en la Figura 5.8 el flujo metodológico en cuatro fases.

**Tabla 5.6.** Alcance de migración histórica del Caso 10

| **Dominio Histórico a Migrar** | **Volumen del Caso 10** | **Criterio de Aceptación y Conciliación** |
|---|---|---|
| Maestros de flota y semirremolques | 100 % (374 tractos y 210 semirremolques propios; terceros según inventario) | Conciliación 1:1 contra inventario y respaldos autorizados del CLIENTE |
| Maestros conductores y transportistas | 100 % (454 choferes y 148 dueños) | Validación RUT Módulo 11 y contratos marco vigentes |
| Maestro de clientes y geocercas | 100 % (84 clientes y 1.400 puntos) | Validación de direcciones y polígonos geoespaciales |
| Vigencias de habilitación vivas | ≈ 6.000 registros en 4 planillas | Verificación documental individual con hash SHA-256 |
| Histórico de viajes operacionales | 5 años; ≈480.000 si se mantuvo la tasa actual, estimación | Conciliación de totales, códigos de flete y fechas |
| Histórico de liquidaciones | 6 años; ≈10.656 si hubo 148/mes, estimación | Cuadre de importes, moneda y redondeo contra registros del sistema fuente y contable |
| Histórico de siniestros | 100 % de antecedentes disponibles | Integridad de expedientes legales y peritajes |

La Tabla 5.6 distingue alcance obligatorio de estimaciones derivadas: el Caso aporta una tasa anual actual, no el número real de filas de los últimos cinco/seis años. En el levantamiento se cuentan registros, adjuntos y bytes, incluidos históricos sin persona/vehículo homologado; el archivo original se conserva en cuarentena hasta resolverlos.

La Figura 5.8 muestra cuatro fases: extracción/perfilamiento con copia y hash del origen; homologación y deduplicación con mapeos aprobados; acreditación de cada vigencia y custodia del respaldo; ensayos en PREPROD, conciliación y carga final de diferencias. La ventana se estima con conteos/bytes reales y tasas de los ensayos; se concilia con S7 antes del corte. Los paquetes de datos EDT 7.x y cortes por función M16/M21 gobiernan la ejecución.

La aceptación exige conciliación de totales, referencias y documentos, ausencia de vigencias habilitantes sin respaldo y cuadratura de liquidaciones con diferencias justificadas. Toda inconsistencia se identifica por registro, propietario y resolución, sin afirmar que una carga masiva elimina errores. Se prueban reversa, delta final e idempotencia; nunca se borran documentos fiscales ya emitidos ni evidencias válidas generadas durante la convivencia. Los cortes respetan los congelamientos y la implantación por terminal/unidad de S7 (FEP03 · RT-10.05 · p.32).

![Figura 5.8. Metodología de extracción, saneamiento, carga y conciliación histórica](./graficos/audit-figura-5.5-migracion.png)

*Figura 5.8. Metodología de extracción, saneamiento, carga y conciliación histórica*

Fuente: elaboración D3 con el lienzo de D4.

La Figura 5.8 muestra las puertas de acreditación y conciliación. Un registro en cuarentena no habilita despacho; el corte requiere acta y aceptación de los casos vinculados en T-17, con discrepancias resueltas o excluidas explícitamente del uso habilitante.

## 5.4 Estrategia de desempeño

La meta contractual de asignación es ≤30 s extremo a extremo (FEP03 · RT-09.01 · p.32). Menos de 2 s es objetivo interno de un caso nominal, no medición ni garantía derivada de usar caché. La Figura 5.9 muestra que una proyección sólo habilita cuando su versión y actualidad se validan contra el estado autoritativo; si hay conflicto se reevalúa o rechaza dentro del plazo total.

![Figura 5.9. Estado autoritativo, caché e índices especializados](./graficos/audit-figura-5.6-desempeno.png)

*Figura 5.9. Desempeño y validación de actualidad. Fuente: elaboración D3 con el lienzo de D4.*

La Figura 5.9 separa consultas puntuales del histórico y la analítica. Se proponen B-tree sobre IDs/FK y rangos de asignación, GiST en geocercas y BRIN sólo donde el orden físico temporal lo justifique. Un RUT cifrado no se indexa como texto en claro: la deduplicación usa un índice ciego HMAC con clave separada, alcance documentado y acceso restringido; se evalúa el riesgo de correlación. Las búsquedas parciales no se ofrecen sobre ciphertext como si fueran equivalentes a texto.

Con ≈96.000 viajes/año, `VIAJE` se mantiene sin partición inicialmente para conservar PK/FK simples. Se particionan series, eventos y auditoría por tiempo; si luego se particiona negocio, PostgreSQL exige incluir la clave de partición en la restricción única aplicable y propagarla a las referencias. No se propone una PK global por UUID incompatible con la partición mensual. La extensión TimescaleDB en Azure es Apache-2; particionado y agregaciones usan sólo funciones verificadas en esa edición, sin asumir compresión comercial.

Redis conserva versiones, vencimiento y permisos. Revocar una habilitación o autorización invalida la proyección; un TTL aislado no asegura actualidad. El caché no es el único registro de idempotencia. Vistas y consultas de preliquidación/BI residen en la capa analítica, con refresco y marca de antigüedad; no compiten con la base de despacho.

S4.1.20 deriva ~119,82 millones de posiciones/año en el escenario completo y distingue las 61 fuentes iniciales de motor del resto. El anexo de S5 estima bytes de negocio, evidencia y migración con tamaños supuestos. La aceptación mide máximos y percentiles del despacho, retraso de CDC, consumo de WAL, CPU/IO, reconstrucción de evidencia y confirmación de cada camión. Se separan 380 sesiones provisionales, 570 en estrés, crecimiento 3× y 300 reconexiones: no son la misma prueba ni equivalen a TPS. La línea base concurrente se concilia con D4 antes de congelar dimensionamiento.

## Referencias

Biblioteca del Congreso Nacional. (2024). *Ley N.º 21.719*. https://www.bcn.cl/leychile/navegar?i=1209272

Chandramouli, R., y Hibbard, E. (2025). *Guidelines for Media Sanitization (NIST SP 800-88 Rev. 2)*. https://csrc.nist.gov/pubs/sp/800/88/r2/final

ISO. (2008). *ISO/IEC 25012: Data quality model*. https://www.iso.org/standard/35736.html

Microsoft. (s.f.). *Consideraciones de extensiones de PostgreSQL Flexible Server*. https://learn.microsoft.com/en-us/azure/postgresql/extensions/concepts-extensions-considerations

## Declaración de uso de IA

Los cambios del 11-10-2026 se declaran en la tabla siguiente; la revisión humana de ingeniería no se declara ejecutada por el asistente. La declaración de herramientas previas permanece en la versión Git de origen, sin atribuir nombres de modelos o validaciones no comprobadas.

| Sección | Herramienta | Finalidad | Nivel en texto | Nivel en diagramas | Revisión humana |
|---|---|---|---|---|---|
| 5 y 5.1 | OpenAI Codex (GPT-6), sobre diseño previo y corrección D1 | Separar dominios, evidencia, evaluación, custodia y permisos | Alto | Alto | Pendiente: D3 coteja el modelo con S3; D1 comprueba CP-SYS-05/CP-UAT-09 |
| 5.2 | OpenAI Codex (GPT-6) | Corregir CAP, motores, retención y respaldo | Alto | Alto | Pendiente: D3/D4 validan productos, edición, recuperación y base de transferencia |
| 5.3 | OpenAI Codex (GPT-6) | Distinguir volumen estimado, cuarentena y criterios de corte | Alto | Alto | Pendiente: D3/D2 concilian ventana y paquetes EDT |
| 5.4 | OpenAI Codex (GPT-6) | Revisar índices, partición y actualidad de caché | Alto | Alto | Pendiente: D3/D1 validan restricciones y ensayos |
| Anexo de diccionario | OpenAI Codex (GPT-6) | Especificar atributos, relaciones, restricciones y supuestos de capacidad | Alto | Ninguno | Pendiente: D3 verifica cada atributo y su propietario |
