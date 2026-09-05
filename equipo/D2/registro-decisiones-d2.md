# Registro de decisiones de diseño - D2

**Ignacio C. y Matías V. · Esquema de solución y alcance**

**Caso 10 · Transporte de Carga · Transportes Curimón S.A.**

**Estado:** borrador de trabajo para ratificación del equipo

**Fuente principal:** FEP03 · sección 16.1 · p.34

## 1. Cómo usar este registro

Este documento convierte las 26 decisiones pendientes de las Bases en propuestas de
trabajo trazables. Una propuesta no se considera acordada hasta que D2 la ratifique y,
cuando corresponda, la coordine con D1, D3 o D4.

No existe en el repositorio un Acta de Respuestas a Consultas. Por ello, las propuestas
de interpretación incluidas en las consultas no se tratan como respuestas ni como
acuerdos del CLIENTE.

### Estados

- **Propuesta:** existe una solución suficientemente concreta para revisarla.
- **Propuesta parcial:** existe una dirección, pero faltan elementos relevantes.
- **Abierta:** no existe una solución suficiente y requiere diseño inmediato.
- **Ratificada:** acordada por el equipo y apta para alimentar requisitos y alcance.

## 2. Decisiones críticas para ratificación inmediata

Desarrollo de D-01: `decision-01-jornada-externa.md`. Incluye alternativas,
recomendación, bloqueo ante evidencia insuficiente, contingencias y verificación
por grupo. Sigue pendiente de ratificación y validación jurídica.

Antes de cerrar el catálogo RF/RNF deben resolverse estas materias:

1. **Alcance del equipamiento:** D3 supone capacidad de borde en los 374 camiones,
   mientras D4 limita la intervención a unidades propias y terceros adheridos.
2. **Telemetría de fábrica:** escoger rFMS/API del fabricante como vía primaria y dejar
   el lector físico CAN/FMS sujeto a autorización expresa por modelo y garantía.
3. **Costeo:** separar costeo operacional básico en Etapa 1 de analítica avanzada en
   Etapa 2, asegurando información útil antes de la renegociación de 2027.
4. **Propiedad del dispositivo:** definir financiamiento, administración, mantención y
   salida contractual; no basta con declarar que el CLIENTE compra el hardware.
5. **Privacidad:** distinguir captura futura, visibilidad para clientes, conservación
   histórica y eliminación legalmente procedente.
6. **Excepciones al bloqueo:** definir qué incumplimientos nunca admiten excepción y
   cuáles pueden someterse a autorización extraordinaria auditable.

## 3. Registro maestro

| N° | Estado | Decisión propuesta | Validación o trabajo pendiente | Coordinación |
|---:|---|---|---|---|
| 1 | Propuesta parcial | Acreditar la jornada externa mediante declaración digital identificada antes del despacho, contraste con tacógrafo cuando esté disponible y acceso contractual a registros del transportista. La consulta de jornada será bloqueante y la evidencia tendrá sello de tiempo y protección contra alteraciones. | Validar valor probatorio, identificación del conductor, correcciones, contingencia y fuente de jornada previa para otros clientes. | D1, D3 y revisión legal |
| 2 | Propuesta parcial | Ofrecer adhesión contractual que agrupe dispositivo, intercambio de datos, consentimiento y acceso al portal de viajes, evidencias y liquidación. Mantener una modalidad operacional degradada para quien no adhiera, sin prometer capacidades que dependan de sus datos. | Definir incentivo económico, metas por periodo, instrumento contractual, consecuencia del rechazo y criterio de permanencia. | Matías lidera; D1 y D4 |
| 3 | Propuesta | Sustituir progresivamente los módulos operacionales del TMS 2013 mediante una capa de transición, manteniendo el sistema contable como único emisor tributario. | Confirmar interfaces, exportaciones, soporte y separación real entre TMS y sistema contable. Preparar alternativa si solo existe acceso por archivos o base de datos. | D3 |
| 4 | Propuesta parcial | Unificar los tres proveedores GPS mediante una capa de ingestión multicanal. Homologar equipos de terceros sin intervenirlos y usar una alternativa móvil o equipo acordado para unidades sin dispositivo. | Resolver la diferencia entre cobertura de 374 unidades y solo unidades intervenibles; confirmar API, derechos, históricos y límites de cada proveedor. | D3 y D4 |
| 5 | Propuesta parcial | El CLIENTE financia y mantiene en inventario el equipo adicional que instala; en camiones de terceros se requiere adhesión expresa. El contrato debe regular uso, administración, soporte, retiro, devolución o transferencia al terminar la relación. | Definir quién paga instalación, conectividad, suscripciones, mantención y retiro; fijar tratamiento de equipos propios preexistentes del transportista. | Matías lidera; D1 y D4 |
| 6 | Propuesta parcial | Aplicar bloqueo automático ante jornada insuficiente, habilitación vencida o equipo no apto. Solo condiciones no legales y previamente clasificadas podrían admitir una excepción temporal con autoridad nominada, motivo, doble control, caducidad y auditoría. | Clasificar causales excepcionables y no excepcionables; acordar autoridad, escalamiento y operación cuando un viaje comprometido queda bloqueado. | D1, D3 y operación |
| 7 | Propuesta parcial | Calcular la alerta a bordo según jornada restante y tiempo hasta el próximo lugar seguro, considerando ruta y condiciones vigentes, en vez de usar un umbral fijo aislado. | Levantar y validar el catastro de lugares seguros; definir márgenes mínimos y contingencia cuando no exista detención segura alcanzable. | D4 y conductores |
| 8 | Propuesta parcial | Registrar llegada y salida automáticamente con geocercas y sello temporal; complementar con EDI, API, agenda o barrera cuando el cliente disponga de esas fuentes. Conservar evidencia de precisión y eventos de entrada/salida. | Definir tratamiento de falsos cruces, precisión aceptable, resolución de disputas y aceptación contractual de la evidencia por los clientes. | D3, D4 y área comercial |
| 9 | Propuesta parcial | Generar la orden y preparar localmente la información necesaria para la emisión sin redigitación. Usar el mecanismo offline oficialmente soportado por el sistema contable y transmitir al recuperar conectividad, manteniéndolo como único emisor tributario. | No comprometer CAF, firma o prefoliado hasta validar su vigencia con el sistema contable y la normativa aplicable. | D3 y proveedor contable |
| 10 | Abierta | Diseñar una conformidad de entrega digital disponible el mismo día, identificada, sellada temporalmente y operable sin cobertura, con sincronización posterior. | Elegir mecanismo de aceptación, identidad y facultades del receptor, rechazo o ausencia, evidencia complementaria, momento que habilita facturación y tratamiento de controversias. | Ignacio lidera; D1 y D3 |
| 11 | Propuesta | Usar muestreo adaptativo: mayor frecuencia en maniobras, geocercas y eventos; frecuencia media en ruta estable; frecuencia baja detenido. Conservar detalle local sin cobertura y transmitirlo posteriormente. | Ratificar valores iniciales de 10 s, 30 s y 5 min mediante piloto; dimensionar fotos, eventos, datos móviles y almacenamiento. | D3 y D4 |
| 12 | Propuesta parcial | Priorizar acceso remoto rFMS/API del fabricante en modo de solo lectura. Considerar lectura física CAN/FMS únicamente donde no exista acceso remoto y haya autorización del fabricante sin afectar garantía ni seguridad. | Levantar marca, modelo, año, suscripción e interfaces de los 61 tractocamiones; eliminar afirmaciones de garantía no confirmadas. | D3 y D4 |
| 13 | Propuesta parcial | Descargar el tacógrafo de forma remota cuando el modelo lo permita; usar descarga física controlada como contingencia. Conservar archivos originales, identidad, sello temporal, integridad y trazabilidad de descarga. | Confirmar modelos, interfaces, periodicidad legal, responsable, asociación conductor-vehículo y plazo de conservación. | D3, D4 y revisión legal |
| 14 | Abierta | Incorporar optimización de retorno en Etapa 2, respetando jornada, habilitaciones, ubicación, plazo, compatibilidad de carga y aceptación del transportista. | Definir función objetivo y ponderaciones: margen, kilómetros vacíos, nivel de servicio, jornada, riesgo y prioridad contractual. Definir adjudicación entre flota propia y terceros. | Matías lidera; D1 y D3 |
| 15 | Propuesta | Mantener un costo preliminar del viaje dentro de 24 horas, con componentes disponibles y estimaciones identificadas, y una versión consolidada posterior sin sobrescribir el historial. | Definir reglas de estimación, fuentes, identificadores comunes, responsables de conciliación y señal visible de costo provisional. | D3 y finanzas |
| 16 | Propuesta parcial | Distinguir el costo para Curimón de contratar a un tercero de su costo operacional interno. Para gestión contractual usar tarifa, anticipos, peajes y sobreestadía; usar datos open-book solo con adhesión expresa para comparaciones económicas ampliadas. | Acordar cuál costo exige cada indicador y qué datos aceptarán compartir los transportistas; evitar presentar la tarifa como costo real del tercero. | Matías lidera; D1 y D3 |
| 17 | Propuesta parcial | Entregar en Etapa 1 costeo básico por viaje, ruta y contrato para sustentar la renegociación de 2027; dejar modelos avanzados de rentabilidad y optimización para Etapa 2. | Identificar los tres contratos, fecha de corte, información mínima, escenarios y responsable de la decisión comercial. | D1, D3 y finanzas |
| 18 | Propuesta parcial | Consolidar las aproximadamente 6.000 vigencias en un registro único con propietario, titular, responsable de renovación, custodio, alertas y efecto bloqueante sobre la asignación. | Definir responsables y escalamiento por tipo documental, especialmente cuando el titular sea externo; ratificar umbrales de alerta y reglas de bloqueo. | D1 y D3 |
| 19 | Abierta | Verificar que la carga peligrosa efectivamente cargada corresponda al manifiesto antes del despacho, vinculando identidad de carga, vehículo, conductor, documentación y evidencia del punto de carga. | Elegir evidencia viable sin instalar equipos ni imponer procesos al cliente: integración disponible, lectura de código/UN, manifiesto firmado, fotografía sellada o doble validación. Definir excepción y auditoría. | Ignacio lidera; D1, D3 y operación |
| 20 | Propuesta parcial | Mantener operación y evidencia local durante cierres fronterizos, suspender o clasificar correctamente tiempos según regla contractual y sincronizar en orden al recuperar conectividad. | Diseñar protocolo operacional: jornada y relevo, reprogramación, comunicación al cliente, custodia de carga, trámites y autorización para modificar sobreestadías. | Matías lidera; D3 y D4 |
| 21 | Abierta | Permitir que el taller externo registre una intervención mediante canal web o móvil, incluso offline, adjuntando identidad, fecha, kilometraje, trabajo, repuestos y evidencia; someterla a validación antes de incorporarla a la hoja de vida. | Definir usuario, datos mínimos, aprobación, plazo, evidencia, correcciones, efecto en garantía y mantenimiento preventivo. | Ignacio lidera; D3 y D4 |
| 22 | Propuesta parcial | Calcular emisiones por tonelada-kilómetro con metodología declarada basada en ISO 14083/GLEC: consumo real donde esté disponible y factores estándar documentados para terceros, migrando a datos reales según adhesión. | Validar estándar aceptado, factores, tratamiento de vacío, límites, datos de masa y mecanismo de verificación externa. | D1 y D3 |
| 23 | Propuesta parcial | Aplicar consentimiento granular y revocable por transportista, camión, viaje, dato y destinatario. Compartir posición con clientes solo durante el servicio autorizado y auditar accesos desde el portal del transportista. | Separar revocación de captura futura, visibilidad, retención histórica y obligaciones legales. Considerar derechos del conductor además del dueño del camión. | Ignacio lidera; D3 y revisión legal |
| 24 | Propuesta parcial | Proteger la evidencia de jornada con identidad fuerte, sello temporal, registro append-only, hash encadenado y almacenamiento inmutable; conservar historial de correcciones sin sobrescritura. | Validar autoría, fuente original, cadena de custodia, sello de tiempo, auditor independiente y valor probatorio. Corregir la inconsistencia técnica del trigger descrito por D3. | D3 y revisión legal |
| 25 | Propuesta parcial | Desplegar kits preconfigurados camión por camión durante pasos normales por terminal, con piloto por familia de vehículo, instalación acotada, verificación y actualización remota posterior. En terceros, intervenir solo con adhesión y autorización. | Calcular cronograma desde frecuencia real de paso, tiempos de piloto, stock y capacidad de talleres. Sustituir metas 80/95/100 si no se sostienen con esos datos. | D4; Matías revisa adhesión |
| 26 | Propuesta parcial | Operar en modo mixto: validación telemática completa para equipados y validación documental controlada para no equipados, identificando visiblemente el nivel de evidencia. Avanzar por cobertura y calidad, no solo por fecha. | Definir criterio de avance, reversión, carga operacional, riesgo aceptable y tratamiento permanente del transportista que no adhiere. Verificar si el modo degradado satisface la acreditación de jornada. | Matías lidera; D3 y D4 |

## 4. Acuerdos de alcance que propone D2

Estas reglas permiten que el catálogo de requisitos avance aunque existan validaciones
externas pendientes:

1. Toda dependencia no confirmada se declara como supuesto y tiene contingencia.
2. Ninguna consulta enviada se cita como respuesta del CLIENTE mientras no exista acta.
3. Ningún requisito obliga a intervenir equipos de terceros sin acuerdo expreso.
4. La operación esencial debe funcionar sin cobertura y sincronizarse después.
5. La ausencia de adhesión no puede ocultarse: reduce capacidades y debe tener un modo
   operacional explícito, medible y seguro.
6. Los incumplimientos legales o de seguridad no se transforman en excepciones por una
   autorización operacional.
7. El sistema contable se conserva como único emisor de documentos tributarios.
8. La arquitectura implementa las decisiones de alcance de D2; no debe inventarlas ni
   contradecirlas.

## 5. Validación mínima para cerrar D2-01

- [ ] Las 26 propuestas fueron revisadas por Ignacio y Matías.
- [ ] Las decisiones 1, 2, 5 y 25 quedaron ratificadas y fundamentadas.
- [ ] Las decisiones abiertas 10, 14, 19 y 21 tienen solución acordada.
- [ ] Se resolvió el alcance real de equipamiento en flota propia y de terceros.
- [ ] Se acordó la estrategia primaria para telemetría de fábrica.
- [ ] Se resolvió la división del costeo entre Etapa 1 y Etapa 2.
- [ ] Se definió el modelo contractual y económico del dispositivo.
- [ ] Se acordaron reglas de retención y revocación de geolocalización.
- [ ] D3 y D4 confirmaron que pueden implementar las decisiones sin supuestos nuevos.
- [ ] Cada decisión ratificada alimenta al menos un RF, RNF, supuesto o exclusión.

## 6. Fuentes internas consultadas

- `equipo/D1/subdoc2-problema.md`
- `equipo/D1/consultas-d1.md`
- `equipo/D2/plan-trabajo-d2-v2.md`
- `equipo/D2/consultas-d2-v2.md`
- `equipo/D3/plan-de-trabajo.md`
- `equipo/D3/subdoc4.1-arquitectura-logica.md`
- `equipo/D3/subdoc5-datos.md`
- `equipo/D4/D4-MATERIAL-INFORME1.md`
- `equipo/consultas-consolidadas-audit.md`
