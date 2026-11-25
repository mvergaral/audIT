# Registro de consultas D2 - Ignacio C. y Matías V.

## Informe 1 - Caso 10: Transporte de Carga

**Responsables de preparación:** Ignacio C. y Matías V.  
**Área:** D2 - Esquema de solución y alcance  
**Fecha objetivo de revisión interna:** 31-08-2026  
**Cierre oficial del período de consultas:** 01-09-2026  
**Estado:** Borrador para revisión del equipo  
**Nombre de la empresa proponente:** AudIT

---

## 1. Reglas aplicables

De acuerdo con el Artículo 43 de las Bases Administrativas:

- Las consultas deben enviarse por escrito y a través del canal oficial.
- Deben ser concretas, precisas y pertinentes al proceso.
- No deben solicitar información confidencial.
- No deben pedir al CLIENTE que diseñe la solución en lugar del PROPONENTE.
- Deben presentarse en una planilla con número correlativo, empresa, fecha, tipo, referencia, consulta y propuesta de interpretación.
- El archivo oficial debe nombrarse `CONSULTAS_[EMPRESA]_AAAAMMDD.XLSX`.

Las consultas de este documento están orientadas a aclarar contradicciones, precisar el alcance documental y conocer la disponibilidad de información o interfaces existentes. No buscan trasladar al CLIENTE las decisiones del numeral 16.1.

---

## 2. Consultas recomendadas para envío

### Prioridad crítica

| N.º | Empresa | Fecha | Tipo | Documento, sección y página | Consulta detallada | Propuesta de interpretación del proponente |
|---:|---|---|---|---|---|---|
| 1 | AudIT | 31-08-2026 | Administrativa | Bases Administrativas, Formulario T-20, pág. 65; Formulario T-22, pág. 68 | El Formulario T-20 establece la publicación del Acta de Respuestas a Consultas y la entrega del Informe 1 para el 07-09-2026. Sírvase aclarar el horario y orden relativo de ambos hitos, e indicar si las respuestas publicadas ese día deben incorporarse obligatoriamente en el Informe 1. | Se entiende que el Acta será publicada con antelación suficiente para incorporarla al Informe 1 o, en su defecto, que las respuestas se considerarán obligatorias desde la instancia siguiente. |
| 2 | AudIT | 31-08-2026 | Administrativa/Técnica | Bases Administrativas, Formulario T-12, pág. 62; Formulario T-22, pág. 68 | El Formulario T-12 solicita declarar el cumplimiento de cada requerimiento de las Bases Técnicas del caso y de los requisitos transversales del “Capítulo 3”. Sírvase aclarar si, para el Informe 1, la matriz debe incluir la totalidad de los requisitos RT-01 a RT-26 aplicables o solamente los requisitos vinculados con los subdocumentos 1, 2, 3, 4, 5 y 13 exigidos en esta instancia. | Se propone incluir en el Informe 1 todos los requisitos del caso y los requisitos transversales que afectan alcance, arquitectura, datos e innovaciones, incorporando el resto de manera incremental en los informes siguientes. |
| 3 | AudIT | 31-08-2026 | Administrativa | Bases Administrativas, artículos 28 y 29, pág. 19; Formularios T-19 y T-22, págs. 64 y 68-69 | El Artículo 29 y el Formulario T-19 exigen inversión, efecto en costo operacional y beneficio esperado para cada innovación, mientras el Formulario T-22 sitúa la valorización de las innovaciones en el Informe 3. Sírvase aclarar el nivel de cuantificación económica requerido en el Informe 1. | Se entiende que el Informe 1 debe incluir una estimación preliminar y sus supuestos, reservándose la valorización definitiva y su incorporación al flujo de caja para el Informe 3. |
| 4 | AudIT | 31-08-2026 | Técnica | Bases Técnicas Caso 10, capítulos 5, 16.1 y 17.4, págs. 12-13 y 34-40 | Para evaluar las alternativas de conservación, integración, envolvimiento o sustitución del sistema de gestión de transporte de 2013, sírvase indicar si el sistema dispone de API, acceso documentado a base de datos, exportaciones masivas, documentación de su modelo de datos y soporte vigente del proveedor. | De no existir antecedentes adicionales, se asumirá acceso de lectura mediante mecanismos de exportación o base de datos, sujeto a validación durante el levantamiento inicial. |
| 5 | AudIT | 31-08-2026 | Técnica | Bases Técnicas Caso 10, capítulos 5, 15 y 17.4, págs. 12-13, 31-33 y 39-40 | Respecto de las tres plataformas de posicionamiento actualmente utilizadas, sírvase precisar para cada una si existen API o mecanismos de exportación, derechos contractuales de integración, documentación técnica disponible, límites de consumo y acceso a datos históricos. | Se asumirá que la integración estará condicionada por los derechos y capacidades vigentes de cada proveedor, y que cualquier plataforma sin interfaz requerirá un mecanismo alternativo expresamente declarado. |
| 6 | AudIT | 31-08-2026 | Técnica/Contractual | Bases Técnicas Caso 10, capítulos 10, 12, 16.1 y 17.1, págs. 23-25 y 34-38 | Sin solicitar el contenido confidencial de los contratos, sírvase indicar si los acuerdos vigentes con los 148 transportistas contienen cláusulas relativas a instalación de dispositivos, acceso o intercambio de telemetría, entrega de jornada, tratamiento de datos personales, consentimiento y niveles de servicio. | Se asumirá que las condiciones requeridas deberán incorporarse mediante anexos o nuevos acuerdos como parte del plan de adhesión, sin que puedan imponerse unilateralmente. |

### Prioridad alta

| N.º | Empresa | Fecha | Tipo | Documento, sección y página | Consulta detallada | Propuesta de interpretación del proponente |
|---:|---|---|---|---|---|---|
| 7 | AudIT | 31-08-2026 | Técnica | Bases Técnicas Caso 10, capítulos 5, 15 y 16.1, págs. 12-13 y 31-36 | Respecto de los 61 tractocamiones con telemetría de fábrica y los tacógrafos digitales instalados, sírvase indicar si existen suscripciones activas, autorizaciones de acceso, interfaces documentadas y mecanismos actuales de descarga o exportación. | Se asumirá que la factibilidad y los costos de acceso deben verificarse con cada fabricante, sin considerar disponible un dato hasta confirmar autorización e interfaz. |
| 8 | AudIT | 31-08-2026 | Técnica | Bases Técnicas Caso 10, capítulos 5, 14, 15 y Anexo A, págs. 12-13, 29-33 y 45-46 | Para dimensionar la migración, sírvase indicar si estarán disponibles inventarios o muestras anonimizadas de las cuatro planillas de vigencias, maestros de flota, conductores, transportistas, clientes, viajes y liquidaciones, incluyendo campos, formatos, identificadores y volumen aproximado por fuente. | Se asumirá que la Etapa 1 contempla levantamiento, perfilamiento y conciliación de todas las fuentes, y que la calidad definitiva se determinará durante esa actividad. |
| 9 | AudIT | 31-08-2026 | Técnica | Bases Técnicas Caso 10, capítulos 5, 9.10, 11 y 16.1, págs. 12-13, 23-25 y 34-36 | Respecto del sistema contable que se mantiene como único emisor de documentos tributarios, sírvase indicar si dispone de API, integración por archivos, acceso a ambientes de prueba y mecanismo de contingencia oficialmente soportado para la emisión del documento electrónico de transporte sin conectividad. | Se asumirá integración con el sistema contable sin reemplazarlo; la modalidad concreta y el procedimiento sin conexión quedarán sujetos a las interfaces oficialmente disponibles. |
| 10 | AudIT | 31-08-2026 | Técnica/Operacional | Bases Técnicas Caso 10, capítulos 15, 16.1 y 18, págs. 31-36 y 41-43 | El caso exige alertar el agotamiento de jornada con tiempo para alcanzar un lugar seguro. Sírvase indicar si el CLIENTE dispone actualmente de un catastro georreferenciado, validado y mantenido de terminales, áreas de descanso o lugares seguros de detención en sus rutas habituales. | De no existir dicho catastro, se considerará su levantamiento y validación operacional como una actividad de la Etapa 1. |
| 11 | AudIT | 31-08-2026 | Técnica/Operacional | Bases Técnicas Caso 10, capítulos 9.5, 10, 11 y 16.1, págs. 22-25 y 34-36 | Para registrar automáticamente llegada y salida en instalaciones de terceros sin instalar equipamiento en ellas, sírvase indicar si existen geocercas, agendas de cita, mensajes EDI, API de clientes, registros de barrera u otras fuentes digitales disponibles en alguno de los 84 clientes. | Se asumirá una estrategia por capacidades disponibles en cada cliente, complementada por mecanismos de geocerca y evidencia a bordo donde no exista integración. |
| 12 | AudIT | 31-08-2026 | Técnica/Operacional | Bases Técnicas Caso 10, capítulos 9.1, 10 y 16.1, págs. 22-24 y 34-36 | Sírvase indicar si actualmente existe una autoridad, rol o procedimiento formal para autorizar excepcionalmente un viaje cuando una validación de jornada, habilitación o aptitud del equipo no se satisface, y si dichas excepciones dejan evidencia auditable. | De no existir un procedimiento vigente, se propondrá una regla de excepción restrictiva, con doble autorización, fundamento obligatorio, caducidad y auditoría inalterable. |

---

## 3. Consultas de reserva

Estas consultas pueden incorporarse si el equipo considera que no están suficientemente respondidas por las bases o por su propio levantamiento.

| N.º | Tipo | Referencia | Consulta | Motivo para mantenerla en reserva |
|---:|---|---|---|---|
| R1 | Técnica | Caso 10, Cap. 15, RT-12.11 | ¿Qué medios de identificación utilizan hoy los conductores propios y externos al iniciar un viaje o un turno, y existe un identificador único común entre los sistemas actuales? | Puede tratarse como información a levantar durante la Etapa 1. |
| R2 | Técnica | Caso 10, Cap. 9.9 y Cap. 15 | ¿Existen obligaciones contractuales vigentes con clientes respecto de frecuencia, precisión, retención o disponibilidad de la posición compartida? | Podría involucrar información contractual sensible; conviene solicitar sólo parámetros generales. |
| R3 | Técnica | Caso 10, Cap. 9.7 y Cap. 16.1 | ¿Qué fuentes actuales entregan combustible, peajes, neumáticos, mantenimiento y pagos a terceros, y cuáles poseen identificadores que permitan asociarlas automáticamente a viaje, vehículo y contrato? | Parte de esta información puede inferirse del capítulo de sistemas actuales. |
| R4 | Administrativa | Formulario T-12 | ¿Se admite declarar un cumplimiento condicionado a una aclaración, supuesto o dependencia externa, o la columna “Cumple” debe contener únicamente una respuesta binaria? | Puede resolverse utilizando observaciones o referencias en la propuesta, si el formato entregado permite campos adicionales. |

---

## 4. Preguntas que no deben enviarse al CLIENTE

Las siguientes materias corresponden expresamente al trabajo profesional del PROPONENTE. Deben resolverse como decisiones o supuestos y no formularse como solicitudes para que el CLIENTE diseñe la solución.

| Materia | Razón para no preguntar | Tratamiento interno |
|---|---|---|
| Cómo obtener y acreditar la jornada de un conductor externo | Decisión 1 del numeral 16.1 | Proponer fuente, consentimiento, integridad, corrección y contingencia |
| Qué ofrecer a los 148 transportistas | Decisión 2 del numeral 16.1 | Diseñar plan de adhesión e incentivos |
| Reemplazar o conservar el sistema de 2013 | Decisión 3 del numeral 16.1 | Evaluar alternativas usando la respuesta sobre interfaces disponibles |
| Quién paga o administra el dispositivo | Decisión 5 del numeral 16.1 | Definir modelo contractual y económico |
| Quién puede autorizar una excepción al bloqueo | Decisión 6 del numeral 16.1 | Proponer regla y usar como entrada la estructura actual de autoridad |
| Anticipación de la alerta de jornada | Debe justificarla el PROPONENTE | Derivar de distancia a lugares seguros y condiciones de ruta |
| Método para emitir el documento sin cobertura | Decisión pendiente explícita | Diseñar conforme a la interfaz y contingencia admitida por la autoridad |
| Frecuencia de muestreo de posición | Decisión pendiente explícita | Balancear precisión, costo de datos y almacenamiento |
| Criterio de asignación del retorno | Decisión pendiente explícita | Definir regla de negocio y método de optimización |
| Reparto entre Etapa 1 y Etapa 2 | Obligación del Subdocumento 3 | Justificar según dependencias, riesgos e hitos externos |
| Metas no fijadas de los criterios de aceptación | El Capítulo 18 exige proponerlas | Establecer línea base, meta, fecha y medición |
| Forma de operar durante el período de flota mixta | Decisión de implantación | Diseñar convivencia, reversión y criterio de avance |

---

## 5. Priorización para la reunión del lunes

Si el equipo debe reducir la cantidad de preguntas, se recomienda conservar como mínimo:

1. Orden entre Acta de Respuestas y entrega del Informe 1.
2. Alcance del Formulario T-12 en el Informe 1.
3. Nivel económico exigido para las innovaciones en el Informe 1.
4. Interfaces y derechos de acceso del sistema de gestión de 2013.
5. Interfaces y derechos de las plataformas de posicionamiento.
6. Condiciones contractuales existentes con transportistas.
7. Integración y contingencia del sistema contable.
8. Existencia de un catastro de lugares seguros de detención.

---

## 6. Lista de control antes del envío

- [x] Completar el nombre de la empresa proponente: AudIT.
- [ ] Confirmar con el equipo la fecha interna y el canal oficial.
- [ ] Revisar si alguna consulta ya fue respondida en una aclaración formal.
- [ ] Eliminar preguntas duplicadas aportadas por otras duplas.
- [ ] Confirmar referencias de documento, sección y página en los PDF originales.
- [ ] Verificar que ninguna consulta pida al CLIENTE diseñar la solución.
- [ ] Mantener una única materia concreta por fila.
- [ ] Revisar y acordar cada propuesta de interpretación.
- [ ] Pasar las consultas aprobadas a la planilla oficial.
- [x] Nombrar el archivo `CONSULTAS_AudIT_20260901.XLSX`.
- [ ] Enviar por el canal oficial antes del cierre.

---

## 7. Registro de revisión del equipo

| N.º | Decisión | Observación del equipo | Responsable | Estado |
|---:|---|---|---|---|
| 1 | Enviar / ajustar / eliminar |  |  | Pendiente |
| 2 | Enviar / ajustar / eliminar |  |  | Pendiente |
| 3 | Enviar / ajustar / eliminar |  |  | Pendiente |
| 4 | Enviar / ajustar / eliminar |  |  | Pendiente |
| 5 | Enviar / ajustar / eliminar |  |  | Pendiente |
| 6 | Enviar / ajustar / eliminar |  |  | Pendiente |
| 7 | Enviar / ajustar / eliminar |  |  | Pendiente |
| 8 | Enviar / ajustar / eliminar |  |  | Pendiente |
| 9 | Enviar / ajustar / eliminar |  |  | Pendiente |
| 10 | Enviar / ajustar / eliminar |  |  | Pendiente |
| 11 | Enviar / ajustar / eliminar |  |  | Pendiente |
| 12 | Enviar / ajustar / eliminar |  |  | Pendiente |
