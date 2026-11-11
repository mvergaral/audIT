# Subdocumento 4. Arquitectura lógica y física de la solución

audIT, Empresa N.º 10. Licitación TFEP-01/2026, Caso 10 Transporte de Carga. Oferta Técnica, Sobre N.º 2. Informe Preparatorio 2. Archivo AUDIT-Subdocumento4.pdf. Anexos: Formulario T-11 en el archivo AUDIT-Formulario-T-11.pdf.

## Resolución de observaciones del Informe 1

El FEP01, Artículo 46, p. 28 pide resolver en cada informe las observaciones de la instancia anterior, con trazabilidad entre observación, respuesta y sección modificada. La tabla reúne las observaciones del Informe 1 que corresponden a este documento y la sección donde se resuelve cada una.

**Resolución de las observaciones del Informe 1, conforme a FEP01, Artículo 46, p. 28**

| N.º | Observación | Respuesta | Sección modificada |
|---|---|---|---|
| 03 | El Anexo A del Subdocumento 4 no es el Formulario T-11, es una tabla de emplazamiento sin cantidades ni configuración. | Se acepta. Existe una fuente formal del T-11 con fichas de componentes, cantidades y configuración. La respuesta de almacenamiento y reconexión se reconcilia con S4; disponer del archivo no acredita por sí solo conformidad de todas las fichas. | S4, formularios/T-11.tex; dimensionamiento de S4. |
| 53 | Diagrama de las 8 capas no muestra interfaces ni explica qué contiene cada capa ni cómo se conectan. | Se acepta. Se acoge la observación. La respuesta de trabajo propone la siguiente medida, cuya implementación no se acredita en este lote: «Se rediseña el diagrama de arquitectura lógica en capas con interfaces explícitas (REST, gRPC, Kafka, CDC Debezium) y descripción técnica componente a componente.». Su cierre requiere examen de la fuente y de la evidencia correspondiente; no se declara realizada esa revisión para capítulos ajenos al lote S1/S2/S9 y al cálculo de S4. | Sección 4.1.2 (Figura 4.1). |
| 54 | Componentes representados solo como íconos genéricos (terminal de torre y pantalla de terreno sin especificar). | Se acepta. Se acoge la observación. La respuesta de trabajo propone la siguiente medida, cuya implementación no se acredita en este lote: «Se individualiza cada componente: sistema operativo, software ejecutado, protocolos de enlace, roles de usuario y hardware de soporte.». Su cierre requiere examen de la fuente y de la evidencia correspondiente; no se declara realizada esa revisión para capítulos ajenos al lote S1/S2/S9 y al cálculo de S4. | Sección 4.1.2. |
| 55 | No hay matriz de requerimiento a componente; ningún RF del Subdocumento 3 se ubica en un componente. | Se acepta. T-12 asigna contexto y paquete EDT a cada uno de los 42 requerimientos, cotejados con S3. T-17 vincula esa matriz con casos y variantes verificables. No se acredita aquí la correspondencia física completa de cada componente de S4, que requiere revisión propia. | T-12, campo componente; S3 3.2.8 y 3.4.7; T-17, matriz de trazabilidad. S4 pendiente de examen integral. |
| 56 | No se mencionan los principios SOLID, la referencia se reduce a ISO 42010 y los ambientes SDLC están ausentes. | Se acepta. Se acoge la observación. La respuesta de trabajo propone la siguiente medida, cuya implementación no se acredita en este lote: «Se fundamenta el diseño bajo principios SOLID, se estructura la vista lógica bajo ISO/IEC/IEEE 42010 y se documentan formalmente los ambientes del SDLC (Dev, QA, Staging, Producción, DR).». Su cierre requiere examen de la fuente y de la evidencia correspondiente; no se declara realizada esa revisión para capítulos ajenos al lote S1/S2/S9 y al cálculo de S4. | Sección 4.1.1 y Sección 4.1.6. |
| 57 | Diagrama de secuencia de asignación bloqueante huérfano y faltan secuencias de reconexión, emisión y liquidación. | Se acepta. Se acoge la observación. La respuesta de trabajo propone la siguiente medida, cuya implementación no se acredita en este lote: «Se vincula el diagrama al texto analítico y se agregan las secuencias de reconexión masiva tras 288 h de sombra, emisión sin cobertura y liquidación a 148 transportistas.». Su cierre requiere examen de la fuente y de la evidencia correspondiente; no se declara realizada esa revisión para capítulos ajenos al lote S1/S2/S9 y al cálculo de S4. | Sección 4.1.8. |
| 58 | Frameworks y tecnologías viven solo en las figuras; el texto no las decide ni las justifica técnicamente. | Se acepta. Se acoge la observación. La respuesta de trabajo propone la siguiente medida, cuya implementación no se acredita en este lote: «Se justifica la adopción de cada tecnología (C++/Go en borde, .NET Core/Node.js en backend, PostgreSQL/TimescaleDB) evaluando rendimiento, soporte y compatibilidad.». Su cierre requiere examen de la fuente y de la evidencia correspondiente; no se declara realizada esa revisión para capítulos ajenos al lote S1/S2/S9 y al cálculo de S4. | Sección 4.1.7. |
| 59 | El modelo táctico DDD no trae límites de contexto (*Bounded Contexts*) ni eventos de dominio. | Se acepta. Se acoge la observación. La respuesta de trabajo propone la siguiente medida, cuya implementación no se acredita en este lote: «Se formaliza el diseño táctico DDD con especificación rigurosa de Bounded Contexts, agregados, comandos de negocio y eventos de dominio transmitidos por Kafka.». Su cierre requiere examen de la fuente y de la evidencia correspondiente; no se declara realizada esa revisión para capítulos ajenos al lote S1/S2/S9 y al cálculo de S4. | Sección 4.1.5. |
| 60 | Estrangulamiento del sistema 2013 sin ADR ni comparación de alternativas ni fundamento económico. | Se acepta. Se acoge la observación. La respuesta de trabajo propone la siguiente medida, cuya implementación no se acredita en este lote: «Se formaliza el ADR-01 evaluando alternativas (Big Bang, Retiro total vs Strangler Fig) con justificación técnica de riesgos y preservación de continuidad operacional.». Su cierre requiere examen de la fuente y de la evidencia correspondiente; no se declara realizada esa revisión para capítulos ajenos al lote S1/S2/S9 y al cálculo de S4. | Sección 4.1.5 (ADR-01). |
| 61 | El descarte de la banda ancha satelital queda registrado pero no aparece como ADR formal. | Se acepta. Se acoge la observación. La respuesta de trabajo propone la siguiente medida, cuya implementación no se acredita en este lote: «Se documenta el ADR-02 justificando el descarte de terminales satelitales de alta velocidad frente al computador de borde con buffer local eMMC de 8 GB y persistencia offline.». Su cierre requiere examen de la fuente y de la evidencia correspondiente; no se declara realizada esa revisión para capítulos ajenos al lote S1/S2/S9 y al cálculo de S4. | Sección 4.1.5 (ADR-02). |
| 62 | Se afirma que el estilo arquitectónico se justifica con la volumetría sin justificarlo ni comparar estilos. | Se acepta. Se acoge la observación. La respuesta de trabajo propone la siguiente medida, cuya implementación no se acredita en este lote: «Se realiza análisis comparativo de estilos (Monolito, Microservicios, Event-Driven, SOA), fundamentando la adopción del estilo híbrido Event-Driven según la volumetría del Caso 10.». Su cierre requiere examen de la fuente y de la evidencia correspondiente; no se declara realizada esa revisión para capítulos ajenos al lote S1/S2/S9 y al cálculo de S4. | Sección 4.1.3. |
| 63 | El stack tecnológico no ha sido validado formalmente. | Se acepta. Se acoge la observación. La respuesta de trabajo propone la siguiente medida, cuya implementación no se acredita en este lote: «Se presenta la matriz del stack tecnológico validando versiones estables LTS, fechas de fin de soporte (EOL) del fabricante y pruebas de concepto de laboratorio.». Su cierre requiere examen de la fuente y de la evidencia correspondiente; no se declara realizada esa revisión para capítulos ajenos al lote S1/S2/S9 y al cálculo de S4. | Sección 4.1.7. |
| 64 | Falta diagrama de arquitectura física; la figura 1.8 son íconos y cajas sin SKU, vNets, subredes ni enlaces. | Se acepta. Se acoge la observación. La respuesta de trabajo propone la siguiente medida, cuya implementación no se acredita en este lote: «Se incorpora el diagrama de arquitectura física exhaustivo con servicios Azure, SKUs exactos, topología vNet/subredes, enlaces redundantes y dimensionamiento de ancho de banda.». Su cierre requiere examen de la fuente y de la evidencia correspondiente; no se declara realizada esa revisión para capítulos ajenos al lote S1/S2/S9 y al cálculo de S4. | Sección 4.2.1 (Figura 4.2). |
| 65 | Contradicciones en componentes Azure (Data Explorer vs Timescale/Cosmos, Kafka vs Event Hubs). | Se acepta. Se acoge la observación. La respuesta de trabajo propone la siguiente medida, cuya implementación no se acredita en este lote: «Se unifica y congela la arquitectura: Apache Kafka en clúster Strimzi sobre AKS, TimescaleDB para telemetría de series temporales y PostgreSQL para datos transaccionales.». Su cierre requiere examen de la fuente y de la evidencia correspondiente; no se declara realizada esa revisión para capítulos ajenos al lote S1/S2/S9 y al cálculo de S4. | S4 §4.2.8 y S5 §5.5. |
| 66 | La sala de servidores de 26 m² se compara ítem por ítem pero falta plano, carga eléctrica y balance térmico. | Se acepta. Se acoge la observación. La respuesta de trabajo propone la siguiente medida, cuya implementación no se acredita en este lote: «Se incorpora memoria técnica con plano de distribución en planta, consumo eléctrico estimado (kW) y balance térmico de disipación (BTU/h) de la sala técnica de Curimón S.A.». Su cierre requiere examen de la fuente y de la evidencia correspondiente; no se declara realizada esa revisión para capítulos ajenos al lote S1/S2/S9 y al cálculo de S4. | Sección 4.2.6. |
| 67 | Ningún diagrama físico se cita desde el texto analítico. | Se acepta. Se acoge la observación. La respuesta de trabajo propone la siguiente medida, cuya implementación no se acredita en este lote: «Se referencian y recorren en profundidad todos los diagramas de arquitectura física desde el texto analítico del documento.». Su cierre requiere examen de la fuente y de la evidencia correspondiente; no se declara realizada esa revisión para capítulos ajenos al lote S1/S2/S9 y al cálculo de S4. | Subdocumento 4 completo. |
| 68 | La sección 1.2.8 promete declarar cada producto con versión, fin de soporte y parches y no declara ninguno. | Se acepta. Se acoge la observación. La respuesta de trabajo propone la siguiente medida, cuya implementación no se acredita en este lote: «Se formaliza la matriz completa de hardware y software base con versión, ciclo de vida, soporte oficial y plan de actualización y parches de seguridad.». Su cierre requiere examen de la fuente y de la evidencia correspondiente; no se declara realizada esa revisión para capítulos ajenos al lote S1/S2/S9 y al cálculo de S4. | Sección 4.2.8. |
| 70 | Sin cantidades, el parque oscila entre 374 y «según adhesión» y no se explicita el no reemplazo de terceros. | Se acepta. Se acoge la observación. La respuesta de trabajo propone la siguiente medida, cuya implementación no se acredita en este lote: «Se congelan las cantidades del parque: 374 camiones (148 propios retrofiteados con audIT EdgeHub v2.4, 192 terceros homologados por API y 34 terceros sin GPS equipados por audIT con pinzas CANclick).». Su cierre requiere examen de la fuente y de la evidencia correspondiente; no se declara realizada esa revisión para capítulos ajenos al lote S1/S2/S9 y al cálculo de S4. | Sección 4.2.2 y Anexo A. |
| 71 | Se afirma que hay 18 componentes en la región primaria y la tabla suma 20; la matriz cubre 14 de 34. | Se acepta. Se acoge la observación. La respuesta de trabajo propone la siguiente medida, cuya implementación no se acredita en este lote: «Se corrigen los conteos de componentes cloud y se cuadra al 100 % la matriz de infraestructura y servicios de la región primaria.». Su cierre requiere examen de la fuente y de la evidencia correspondiente; no se declara realizada esa revisión para capítulos ajenos al lote S1/S2/S9 y al cálculo de S4. | Sección 4.2.4 y Anexo A. |
| 72 | La región secundaria no tiene nombre y el Artículo 16.3 exige declararla formalmente. | Se acepta. Se acoge la observación. La respuesta de trabajo propone la siguiente medida, cuya implementación no se acredita en este lote: «Se formaliza a Brazil South (São Paulo) como la región secundaria de contingencia y réplica de datos de audIT SpA, en estricto cumplimiento del Art. 16.3.». Su cierre requiere examen de la fuente y de la evidencia correspondiente; no se declara realizada esa revisión para capítulos ajenos al lote S1/S2/S9 y al cálculo de S4. | S4 §4.2.5 y S5 §5.9. |
| 73 | Los 8 GB del dispositivo embarcado no tienen cálculo; la derivación da 10 MB y 288 h dan cerca de 40 MB. | Se acepta. Se deriva el perfil de 72 h: 4.104 posiciones, 1.800 muestras de motor, 45 eventos y cinco documentos, 777.656 bytes sin fotos y 3.237.656 con ocho fotos. La ampliación propuesta 288 h suma 12.950.624 bytes brutos; overhead físico y reserva elevan el presupuesto a 38.851.872 bytes y se asignan 64 MiB. Sistemas A/B, arranque, diagnóstico y maestros llevan el total a 2.400 MiB (2,52 GB decimales). Capacidad útil, ocupación e integridad se verifican en HIL, sin presuponer compresión o equiparar cierre vial con desconexión. | S4, capacidad de almacenamiento y dimensionamiento; T-11; T-17 CP-HW-03. |
| 74 | La sincronización en 20 min por camión se repite como requisito y no se dimensiona ante reconexión masiva. | Se acepta. El perfil simultáneo usa 300 camiones, 1.786.200 registros y 971.296.800 bytes con fotos. Se calculan 6,48 Mbit/s útiles mínimos; con 25 % de transporte y 20 % de reserva temporal, 10,12 Mbit/s. Dos unidades S1 permiten estimar admisión de 71.400 paquetes en 11,9 min; no demuestra transferencia/persistencia. CP-PERF-02 mide confirmación completa y conciliación por camión en hasta veinte minutos. | S4, dimensionamiento y figura de reconexión; T-11; T-17 CP-PERF-02. |
| 75 | Ausentes eventos/segundo, TPS peak de asignación, volumen anual, datos a migrar y ancho de banda. | Se acepta. El perfil de carga mantiene hipótesis explícitas y no confunde concurrencia con viajes diarios. T-17 coteja con T-12 los 42 requisitos y separa ensayo de 72 h de ampliación propuesta de 288 h. La cantidad histórica a migrar y la medición operacional siguen sujetas al levantamiento; no se afirma disponer de 480.000 registros. | S2, supuestos; S3/T-12; T-17 CP-PERF-01, CP-PERF-02 y CP-HW-03. Volumetría integral de S4 pendiente. |
| 77 | El equipo de TI de 9 personas no se menciona y el RT-03.05 se cita sin listar los servicios administrados. | Se acepta. Se acoge la observación. La respuesta de trabajo propone la siguiente medida, cuya implementación no se acredita en este lote: «Se modela la interacción operativa con el equipo de TI de 9 personas de Curimón S.A. y se detallan los servicios administrados provistos por audIT SpA bajo RT-03.05.». Su cierre requiere examen de la fuente y de la evidencia correspondiente; no se declara realizada esa revisión para capítulos ajenos al lote S1/S2/S9 y al cálculo de S4. | Sección 4.2.8. |
| 78 | Se tratan los 3 proveedores GPS y 34 camiones sin equipo pero no se dice qué se instala ni cómo conviven. | Se acepta. Se acoge la observación. La respuesta de trabajo propone la siguiente medida, cuya implementación no se acredita en este lote: «Se especifica la arquitectura de coexistencia: capa de integración API (ACL) para Wialon/Wisetrack, e instalación de audIT EdgeHub v2.4 con pinzas CANclick en los 34 tractos desprovistos.». Su cierre requiere examen de la fuente y de la evidencia correspondiente; no se declara realizada esa revisión para capítulos ajenos al lote S1/S2/S9 y al cálculo de S4. | Sección 4.2.2. |
| 79 | La recuperación ante desastres y continuidad se separan con argumento sísmico sin justificar factibilidad. | Se acepta. Se acoge la observación. La respuesta de trabajo propone la siguiente medida, cuya implementación no se acredita en este lote: «Se fundamenta la factibilidad técnica y latencia ($<50\text{ ms}$) del enlace hacia Brazil South, garantizando el cumplimiento estricto del RTO $\le 4\text{ h} y RPO \le 15\text{ min}$.». Su cierre requiere examen de la fuente y de la evidencia correspondiente; no se declara realizada esa revisión para capítulos ajenos al lote S1/S2/S9 y al cálculo de S4. | Sección 4.2.5. |
| 80 | Los respaldos aparecen en una sola fila y no hay modelo Zero Trust explícito ni superficie de exposición. | Se acepta. Se acoge la observación. La respuesta de trabajo propone la siguiente medida, cuya implementación no se acredita en este lote: «Se diseña la arquitectura de ciberseguridad: modelo Zero Trust, microsegmentación de subredes, Azure Bastion, WAF y almacenamiento inmutable WORM.». Su cierre requiere examen de la fuente y de la evidencia correspondiente; no se declara realizada esa revisión para capítulos ajenos al lote S1/S2/S9 y al cálculo de S4. | Sección 4.2.7. |

## 4 Introducción a la Arquitectura Lógica y Física de la Solución

Este capítulo describe cómo se construye la Plataforma Digital de Misión Crítica para Transporte de Carga: con qué piezas de software se organiza
la solución y en qué equipos, sitios y regiones de nube corre cada una. La sección 4.1 presenta la
arquitectura lógica, sus ocho capas, sus seis contextos delimitados y sus decisiones registradas, y la
4.1.1 las tecnologías de software. La sección 4.2 ubica cada componente en la nube, en San Bernardo,
en los cuatro terminales regionales y en los camiones, declara los enlaces y los puntos únicos de
falla, y dimensiona la ingesta de datos y la reconexión masiva. La sección 4.3 declara los dos
centros de datos: Azure Chile Central como región primaria, con la sala de San Bernardo como sitio de
continuidad, y Azure Brazil South como región secundaria.

El capítulo parte del esquema de solución del Subdocumento 3 y del catálogo de requerimientos de su
Formulario T-12. Se apoya en el modelo de datos del Subdocumento 5, que define dónde reside cada dato
y cómo se respalda. Los riesgos que abre la infraestructura, como el apagado de las redes 2G y 3G o el
retraso de una réplica, se tratan en el Subdocumento 8, y el ritmo de instalación a bordo en el plan
de trabajo del Subdocumento 7. La innovación tecnológica del Subdocumento 13 usa el Bluetooth del
equipo a bordo que se especifica aquí. Lo que el mandante compra, con cantidades y características, se
detalla en el Formulario T-11, que acompaña este capítulo como archivo propio
(`AUDIT-Formulario-T-11.pdf`), conforme al Comunicado 10, sección 1.

## 4.1 Arquitectura lógica

El Capítulo 5 del Caso resume el problema en una frase. El sistema de gestión de transporte de 2013
conoce el viaje que la compañía encargó y no conoce el viaje que efectivamente ocurrió
(Caso, capítulo 5, p. 13). El dato existe repartido en tres plataformas de posicionamiento, en una
telemetría que nadie descarga, en una liquidación de combustible que llega con cuarenta días de
atraso y en papeles que viajan en la cabina, y nunca se junta. Esa dispersión no se corrige
configurando el sistema existente, porque nace de cómo está construido.

### 4.1.1 Especificaciones Tecnologías de Software a utilizar

La selección sigue FEP02, RT-03.05, p. 8, que pide servicios administrados cuando reducen el riesgo
operacional, y separa los datos de negocio, las series de tiempo y el análisis en almacenes
distintos. El contrato dura 56 meses y obliga a actualizar, de modo que ninguna versión inicial se
presenta como soportada hasta el mes 56. La Tabla 4.1 fija los productos y la forma de
mantener su soporte.

**Tabla 4.1.** Tecnologías seleccionadas y mantenimiento de su soporte

| Componente | Producto | Soporte del fabricante | Actualización dentro del contrato |
|---|---|---|---|
| Aplicación móvil de cuatro perfiles | Flutter 3.47.0 estable, Dart compatible y SQLite local | Canal estable; el fabricante no publica una fecha fija de fin para esa versión | Fijar SDK, Dart, plataformas mínimas y dependencias en el manifiesto; actualizar con regresión por perfil |
| Portales y torre de control | React 19.3.0 y Next.js 16.x | React estable con política de versiones; Next.js 16 en soporte activo LTS al 10-11-2026 | Fijar parche compatible y SBOM antes de construir; actualizar dentro del ciclo LTS con prueba de regresión |
| Servicios de negocio | .NET 10 LTS | Hasta el 14 de noviembre de 2028 | Paso a la versión LTS siguiente antes de esa fecha |
| Ingesta y borde | Go 1.27.3 | Cada versión mayor tiene soporte hasta que salen dos versiones mayores posteriores | Actualizar revisiones de seguridad y pasar a una versión mayor con soporte antes de su retiro |
| Orquestación | Azure Kubernetes Service | Versiones de Kubernetes que AKS soporta en cada liberación | Actualización por grupos de nodos con prueba de reversa |
| Motor transaccional | PostgreSQL 16 Flexible Server con PostGIS | Hasta el 9 de noviembre de 2028 | Actualización mayor ensayada antes de esa fecha, con extensiones y captura de cambios compatibles |
| Series de tiempo | TimescaleDB, edición Apache-2, en una instancia Flexible Server separada | Versión que Azure publica para cada versión de PostgreSQL | Actualización junto con la versión mayor de PostgreSQL |
| Eventos | Azure Event Hubs Premium con protocolo Kafka | Servicio administrado | Sin clúster Kafka propio que mantener |
| Caché | Azure Managed Redis | Servicio administrado | Provisionado desde la Etapa 1, sin migración desde Azure Cache for Redis |
| Persistencia a bordo | SQLite 3 en modo WAL | Biblioteca fijada en la imagen Linux del equipo | Actualización probada ante cortes de energía y sin borrar registros no confirmados |
| Repositorio analítico | Delta Lake en ADLS Gen2 | Motor, conectores y biblioteca declarados en un manifiesto de versiones | Datos exportables en formatos abiertos |
| Identidad y secretos | Entra ID, identidades administradas y Key Vault | Servicio administrado | Edición y capacidades fijadas en el Formulario T-11 |

*Fuentes: políticas de soporte de los fabricantes (Microsoft, 2026; The Go Authors, 2026; PostgreSQL Global Development Group, 2026; Microsoft, 2026; Microsoft, 2026; Microsoft, 2026); versiones web y móvil verificadas el 10-11-2026 en \url{https://docs.flutter.dev/release/release-notes}, \url{https://react.dev/versions} y \url{https://nextjs.org/support-policy}.*

La tabla decide los productos y evita dos buses alternativos o dos motores intercambiables. Las
versiones base de los canales móviles y web se muestran con su estado a la fecha de esta revisión. El
parche compatible de Next.js y las versiones de Dart y SQLite se fijan en el hito de diseño, cada una con su SBOM, su
licencia, su prueba de compatibilidad, su política de soporte y su responsable. La tabla especifica el
mantenimiento, y las pruebas de compatibilidad todavía no se ejecutan.

Tres productos deben actualizarse dentro del contrato, porque su soporte termina antes del mes 56.
.NET 10 y PostgreSQL 16 terminan en noviembre de 2028, que es el mes 22 si el contrato parte en
febrero de 2027, y cada versión de Go pierde el soporte cuando salen las dos siguientes, cerca de un año
después. .NET 8 termina el 10 de noviembre de 2026 y por eso no es la base del proyecto. El
FEP02, numeral 1.6, p. 5 deja esa actualización de cargo del adjudicatario, y el plan la hace dentro de
la mantención evolutiva, probada en preproducción y sin detener la operación. Las series usan
TimescaleDB en la edición Apache-2 que ofrece Azure, y el diseño no supone funciones comerciales de
compresión que esa edición no trae (Microsoft, 2026). El bus es Event Hubs con clientes del
protocolo Kafka, y no un clúster Kafka propio sobre Strimzi (Microsoft, 2026). Entrega cada
evento al menos una vez y conserva el orden dentro de la partición, así que la idempotencia la pone la
aplicación, sin depender de transacciones Kafka en vista previa.

La caché nace en Azure Managed Redis porque Microsoft retira Azure Cache for Redis Enterprise el 31 de
marzo de 2027 y las ediciones Basic, Standard y Premium el 30 de septiembre de 2028
(Microsoft, 2026). En una implantación nueva se provisiona directamente el servicio de
reemplazo, y así se evita una migración durante la marcha blanca de la Etapa 2, que es el riesgo R-06
del Subdocumento 8. La caché guarda datos derivados y sesiones, y nunca es la única prueba que habilita
un despacho.

Microsoft declara tres zonas de disponibilidad en Chile Central y no le asigna región emparejada
(Microsoft, s. f.). Brazil South es la región secundaria que elige esta oferta, y Azure Managed
Redis está disponible en las dos (Microsoft, 2026). Que una región exista no prueba la
disponibilidad de cada SKU, extensión, modalidad de alta disponibilidad o cuota. Esa matriz por
servicio y región se fija en el diseño detallado, y el aprovisionamiento y la recuperación se validan
antes de activar producción.

### 4.1.2 Punto de partida

Cinco rasgos del sistema de 2013 explican esa dispersión, y cada uno tiene en esta arquitectura una
respuesta estructural propia (Caso, capítulos 5 y 7). La base operativa del sistema de gestión está
acoplada a las consultas de gestión, que compiten con la operación de la torre por el mismo motor, y se
responde separando el almacenamiento transaccional del analítico, como obliga RT-05.05. La integración
con el sistema contable por consultas y tablas compartidas lleva todo cambio contable al núcleo
operacional sin traducción, y se responde con la capa anticorrupción que obliga RT-05.20. La falta de
costo por kilómetro por ruta explica que tres de los ocho contratos principales se sirvan bajo costo,
el peor a menos catorce por ciento durante cuatro años (Caso, numeral 7.3, p. 15), y se responde con un
costo por viaje en doble versión, preliminar y consolidada. El puerto de telemetría de fábrica está
inactivo y la lectura del motor de 61 tractocamiones no se aprovecha por temor a la garantía, y se
responde con una lectura de fábrica autorizada, con protocolo y equipo homologados con cada fabricante.
Los módulos operativos acoplados entre sí no distinguen el viaje encargado del viaje ocurrido, y se
responden con seis contextos delimitados, cada uno con sus propios datos. Ninguno de los cinco se
resuelve configurando el sistema existente.

### 4.1.3 Las ocho capas

La solución se organiza en las ocho capas del modelo de referencia, cuya existencia es obligatoria
conforme al FEP02, numeral 2.1, p. 6. RT-02.01 exige el diagrama que identifica cada capa, sus
componentes y las interfaces entre ellas, y la descripción se ajusta a ISO/IEC/IEEE 42010
(ISO, 2022). La capa de presentación reúne el portal web con representación en servidor para
84 clientes y 148 transportistas, la aplicación móvil en los cuatro perfiles que exige RT-17.01 del Caso
(conductor, torre, terminal y taller, y transportista subcontratado) y las vistas de portería y de
taller, de alto contraste y operables con guantes. La de borde y exposición es el único punto de entrada
público, con distribución de contenidos de presencia global, cortafuegos de aplicación, protección
volumétrica en las capas de red, transporte y aplicación, balanceo y terminación de cifrado. La puerta
de enlace gestiona las interfaces con identidad federada, certificado mutuo entre máquinas,
autorización, cuotas y límites de tasa por perfil, versionado semántico y catálogo publicado. Los
servicios de negocio son seis contextos delimitados, sin estado, en contenedores orquestados sobre
nodos de tres zonas de disponibilidad y con un despliegue independiente por contexto.

La capa de integración y eventos tiene un flujo de telemetría para la ingesta masiva, un bus
transaccional con orden garantizado dentro de la partición, una cola de mensajes fallidos con reintento
y deduplicación, y la capa anticorrupción frente al sistema contable. La de datos es políglota y separa
el motor relacional multizona, la base de series de tiempo, la caché en memoria, el almacenamiento
documental inmutable y el repositorio analítico, cuyo diseño detallado es materia del Subdocumento 5. La
seguridad atraviesa todas las capas con una bóveda de claves, identidad federada con control por rol y
por atributo, cifrado y una bitácora que permite reconstruir quién, qué, cuándo y con qué valores
anteriores, según RT-05.03. La observabilidad usa una instrumentación única con trazas, métricas y
registros correlacionados por el identificador común que RT-05.19 exige a toda integración, sin puntos
ciegos entre nube y terreno.

Ninguna interfaz accede directamente a la base de datos. Una petición entra por la presentación, el
borde y la puerta de enlace, y el servicio invoca su repositorio o publica en su bandeja de salida
cuando corresponde. No toda consulta pasa por el bus de eventos. La respuesta vuelve por la puerta de
enlace y el canal de presentación. Seguridad y observabilidad no ocupan un lugar en esa pila, la
atraviesan entera. La Figura 4.1 dibuja las ocho capas con sus componentes.

![Figura 4.1. Las ocho capas obligatorias del numeral 2.1 transversal, con sus componentes e interfaces, conforme a RT-02.01](../../figuras/04-arquitectura/LogicaCapas.pdf)

*Figura 4.1. Las ocho capas obligatorias del numeral 2.1 transversal, con sus componentes e interfaces, conforme a RT-02.01*

Fuente: Elaboración propia.

Arriba están los cinco tipos de usuario y el canal que usa cada uno. A la derecha quedan los servicios
externos y el camión, que conserva una versión reducida de las capas de servicios y de datos para
operar sin enlace, con un búfer de al menos 72 horas.

### 4.1.4 Los seis contextos delimitados

RT-02.02 rechaza toda arquitectura monolítica que no permita desplegar de forma independiente sus
componentes críticos. Los servicios de negocio se organizan en seis contextos, cada uno con su propio
lenguaje y sus propios datos. Un contexto no consulta la base de datos de otro, le pregunta.
Planificación y tráfico decide qué carga hay que mover y hacia dónde. Flota y activos decide si el
equipo puede salir hoy, y Personas y cumplimiento, si la persona puede conducir hoy. Telemetría y
geocercas sabe dónde está el camión y cuándo llegó, Operación de fletes reconstruye el viaje que
realmente ocurrió y Liquidación y costeo calcula cuánto costó y a quién se paga.

La descomposición separa responsabilidades que hoy están dispersas entre el sistema de gestión, las
planillas, los papeles y las plataformas de posicionamiento. La Figura 4.2 muestra los seis
contextos y los sistemas con los que conviven.

![Figura 4.10. Contextos delimitados del dominio y sistemas con los que convive la solución](../../figuras/04-arquitectura/audit-figura-4.2-contextos.png)

*Figura 4.10. Contextos delimitados del dominio y sistemas con los que convive la solución*

Fuente: Elaboración propia.

En la figura, cada contexto tiene su propio lenguaje y sus propios datos. Planificación y tráfico puede
bloquear un viaje sin conocer por dentro a Personas y cumplimiento ni a Flota y activos, porque les
pregunta.

### 4.1.5 Convivencia con lo que ya existe

El sistema de gestión de transporte de 2013 (Caso, capítulo 5, p. 12) y el sistema contable
(Caso, capítulo 5, p. 13) son contrapartes distintas. RT-05.20 obliga a aislar mediante una capa
anticorrupción las integraciones con sistemas heredados o de terceros, y esa capa traduce sus
contratos, pero no sustituye por sí sola sus módulos. Los servicios nuevos reemplazan la asignación, el
control de viaje y la liquidación en el mes 16, y las órdenes y las tarifas a clientes en el mes 21. El
sistema de gestión queda solo para consulta hasta el mes 24, con conciliación y reversa según los
Subdocumentos 3 y 7. El sistema contable sigue como único emisor tributario, como fija la
restricción 8.

### 4.1.6 Registro de decisiones de arquitectura

FEP02, RT-02.04, p. 7 exige un registro de decisiones fechado, con la alternativa escogida, las
descartadas y el criterio, que es entregable contractual y se actualiza durante toda la ejecución, y el
FEP01, Artículo 19, p. 14 lo pide también en la oferta. La Tabla 4.2 registra ocho propuestas documentadas el 11 de octubre
de 2026. Esa fecha es la del registro en la oferta, no una aprobación contractual ni una fecha efectiva de implantación. Cada ADR adquiere estado aprobado y fecha efectiva sólo con el acta del Comité de Arquitectura, que aún no existe; mientras tanto su estado es *propuesto*. Las cuatro primeras conservan su número para no romper las referencias de la arquitectura
física, y las cuatro nuevas completan el análisis que pidió el Informe 1.

**Tabla 4.2.** Registro de decisiones de arquitectura

| ADR | Decisión | Alternativas evaluadas | Criterio | Consecuencia y verificación |
|---|---|---|---|---|
| 01 | Seis contextos desplegables por separado en AKS | Monolito modular, arquitectura orientada a servicios con orquestador central o servicios independientes | RT-02.02 exige desplegar por separado los componentes críticos | La ingesta queda aislada del despacho a cambio de más operación, observabilidad y pruebas de contratos, y el aislamiento se mide bajo carga |
| 02 | Event Hubs Premium con protocolo Kafka y bandeja de salida transaccional | Cadena síncrona de llamadas HTTP o Kafka autoadministrado sobre Strimzi | Las ráfagas quedan aisladas y los efectos derivados no alargan el despacho | La entrega al menos una vez obliga a deduplicar y conciliar en el consumidor |
| 03 | Captura de cambios hacia ADLS y Delta Lake, con modelo dimensional | Inteligencia de negocios sobre la base transaccional o sobre una réplica operacional | RT-05.05 exige separar la analítica de la operación | La captura también consume recursos, por lo que se vigilan los slots y el WAL y se mide su impacto |
| 04 | Identidad federada, certificado por equipo y acceso por rol y atributo | Claves compartidas o secretos en la dirección web | RT-05.18 y el modelo Zero Trust exigen revocación, mínima exposición y secretos fuera del código | Se prueba el acceso cruzado entre transportistas |
| 05 | Reemplazar el sistema de gestión de 2013 función por función y conservar el contable | Corte único, conservarlo solo integrado o un paquete de mercado sin integración demostrada | Los cortes de los meses 16, 21 y 24 evitan interrumpir la operación y el doble registro definitivo | La coexistencia, los adaptadores y la conciliación se presupuestan en el plan de trabajo y en el Sobre N.º 3, sin suponer ahorros |
| 06 | Captura local y mensajería satelital corta, con el documento emitido por el sistema contable | Banda ancha satelital en toda la flota o emisión fiscal en la cabina | Contiene el costo recurrente y los equipos del T-11, y la emisión en cabina infringe la restricción 8 | Se ensaya la entrega completa del documento en 90 segundos y la decisión se revisa si el ensayo falla |
| 07 | PostgreSQL transaccional y TimescaleDB en instancias separadas | Motor único, Cosmos DB o un motor temporal autoadministrado | La integridad referencial queda en el negocio y las series quedan aisladas con SQL conocido | Se verifican la extensión Apache-2, sus funciones efectivas, su actualización y su alta disponibilidad en Azure |
| 08 | SQLite local con bandeja de salida, acuses y conciliación determinista | Depender del enlace para cada evento o un búfer solo en memoria | El Caso exige 72 horas a bordo y conciliación en 20 minutos, y el transversal 24 horas en terminal | Las 288 horas propuestas tienen su propio ensayo y su propia capacidad |

*Fuente: elaboración propia sobre FEP02, RT-02.04, p. 7.*

El registro de ejecución mantendrá para cada ADR los campos `estado`, `fecha_propuesta`, `fecha_aprobación`, `fecha_efectiva`, versión, acta y responsable. En esta entrega, ADR 01–08 tienen fecha de propuesta 11-10-2026, estado propuesto y fecha de aprobación/efectiva pendientes. La evidencia que permite cambiar cada estado es el acta que aprueba la alternativa correspondiente; no se presenta la fecha común de redacción como ocho decisiones ya aprobadas. El Comité revisará en particular ADR 06 contra el ensayo de entrega del documento y ADR 07 contra las capacidades de la extensión en Azure.

La tabla permite revisar cada elección con sus costos de operación. Un cambio de proveedor, de protocolo o de estrategia de continuidad actualiza el ADR, los
contratos, la EDT y los casos de aceptación. La mensajería satelital de la decisión 06 se dimensiona
en la sección 4.2.2.

### 4.1.7 Degradación, escalamiento y puntos únicos de falla

Tres requisitos obligatorios de la misma sección exigen declaraciones que conviene no dejar
implícitas. RT-02.09 obliga a degradar de forma elegante, de modo que la caída de un componente no
crítico deje la solución operando en modo reducido y avisando de la degradación, y nunca falle de
forma total. Si el repositorio analítico no responde, la torre sigue despachando. Si el sistema contable
no responde, siguen la captura, el seguimiento y los viajes que ya tienen su documentación conforme. La
solicitud pendiente se encola, pero se bloquea la salida del viaje que todavía necesita su documento. Si
el enlace satelital no está disponible, el registro sigue acumulándose a bordo.

RT-02.10 exige que las capas de aplicación e integración escalen horizontalmente de forma automática,
con umbrales, límites superiores y costo asociado declarados en la oferta. Los umbrales y los límites
se declaran en la sección 4.1.26. El costo asociado se remite al Sobre N.º 3, porque
el FEP01, Artículo 50.2, p. 29 excluye toda cifra de precio de la Oferta Técnica.

RT-02.11 evalúa como observación grave omitir la declaración de los puntos únicos de falla que
subsistan. Esta oferta declara dos en la capa lógica. El primero es el sistema contable como emisor
único de documentos tributarios. Subsiste porque la restricción 8 lo fija, y es aceptable porque la
captura y el seguimiento continúan. Una salida sin documento conforme queda bloqueada, la cola se vigila
y su atasco se escala como incidente crítico. El segundo es el dispositivo a bordo de cada camión. Hay
uno por unidad y solo puede intervenirse cuando el camión pasa por un terminal, según
Caso, RT-06.01, p. 32. Su falla afecta a una unidad y no a la flota, y se mitiga con repuestos
precargados y con el procedimiento de contingencia aprobado de la sección 4.3.2, que nunca levanta un
bloqueo legal.

Los puntos únicos de falla de la infraestructura física se analizan en la sección 4.2.7.

### 4.1.8 Resiliencia

Los servicios de negocio son sin estado, con el estado de sesión y de proceso en almacenes externos de
alta disponibilidad. Los patrones de RT-02.08 son obligatorios y esta oferta los adopta. Tiempos
límite explícitos en toda llamada remota, cortacircuitos y mamparos para aislar fallas de
integraciones externas, y reintento exponencial con variación aleatoria. La escritura es idempotente
con ventana de deduplicación dimensionada para tolerar la desconexión prolongada en ruta.

El estado de sesión y el estado de proceso residen en almacenes externos de alta disponibilidad, como
exige RT-02.05. Allí viven las sesiones concurrentes de los 22 operadores de la torre, las credenciales
activas y las geocercas de los 1.400 puntos distintos de carga y descarga que declara el
Caso, numeral 14.1, p. 29. Cualquier instancia puede destruirse y reemplazarse sin pérdida de
transacciones en curso. Los parámetros que siguen son de diseño de audIT y se ajustan con la
medición de la Etapa 1. El cortacircuito se abre cuando falla más de la mitad de las llamadas en una
ventana deslizante de diez peticiones, queda abierto 30 segundos y admite tres llamadas de prueba antes
de restablecer el tráfico. El mamparo le da a la verificación bloqueante del despacho su propio conjunto
de hilos y de conexiones, de modo que la saturación de la consulta de liquidaciones o de reportes no le
quita capacidad. Los tiempos de espera son de 800 milisegundos para la validación en memoria, 5 segundos
para la consulta transaccional del despacho, 10 segundos para la llamada al sistema contable a través
de la capa anticorrupción y 90 segundos para la emisión del documento electrónico de transporte, que es
el techo que fija RT-09.01 del Caso. El reintento hace hasta tres intentos sobre operaciones
idempotentes, solo si caben en el plazo total, con retroceso exponencial y variación aleatoria, para que
cientos de unidades que recuperan cobertura a la vez no reintenten sincronizadas. El límite de tasa se
declara por perfil en la puerta de enlace, como se detalla en la gobernanza de interfaces.

Los tiempos de espera escalonan desde la validación en memoria hasta el techo de 90 segundos del Caso,
de modo que ninguna llamada lenta consume el presupuesto de la verificación bloqueante.

### 4.1.9 Verificación bloqueante del despacho

Caso, RT-09.01, p. 32 fija en 30 segundos el tope para asignar un viaje con verificación de jornada,
habilitaciones y aptitud del equipo. El servicio evalúa en paralelo tres invariantes, y una causa legal
bloquea siempre. La de persona y jornada comprueba la identidad del conductor, el descanso, la jornada
acumulada según el artículo 25 bis del Código del Trabajo (Ministerio del Trabajo, 2003), la
evidencia previa relevante y la licencia vigente, conforme a las reglas RN-01 a RN-04 del
Subdocumento 3. La de equipo comprueba las vigencias acreditadas del tractocamión y del semirremolque
(Caso, numeral 4.4, p. 10), su disponibilidad y su compatibilidad con la carga, y sin respaldo vigente no
habilita. La de carga y documentación comprueba el documento de transporte conforme y, en la carga
peligrosa, los requisitos del Decreto Supremo N.º 298 (Ministerio de Transportes, 1995) y la lista de verificación
firmada, según RF-006, RF-013 y RF-014. Asignar recursos no reemplaza la autorización de salida.

El conductor, el tractocamión y el semirremolque no pueden tener asignaciones activas superpuestas.
Planificación obtiene evaluaciones versionadas de Personas y cumplimiento y de Flota y activos, y
confirma solo si esas versiones siguen vigentes. Cada evaluación lleva sujeto, versión, instante y
vencimiento. No basta leer una versión remota y después confirmar en otra base, porque la habilitación
puede cambiar entre los dos pasos. Por eso Planificación serializa las reservas de recursos y registra
el intento antes de consultar. Un cambio incompatible invalida los intentos afectados, y si la vigencia
no se puede confirmar, la asignación se rechaza dentro del plazo. El plan de pruebas del
Subdocumento 9 ensaya en especial una revocación concurrente, dos solicitudes sobre el mismo recurso y
el vencimiento del token. La transacción es local a Planificación, sin atomicidad global entre
contextos.

La Tabla 4.3 reparte el tiempo máximo de la decisión, con la confirmación, la auditoría y
la respuesta incluidas.

**Tabla 4.3.** Presupuesto de diseño de la asignación, de extremo a extremo

| Paso | Máximo de diseño | Control |
|---|---|---|
| Identidad, contrato y clave de idempotencia | 2 segundos | Autorización y unicidad duradera |
| Jornada, vigencias y aptitud, en paralelo | 8 segundos | Evidencia vigente, con retorno a la fuente autoritativa si la caché está desactualizada |
| Reserva y confirmación atómica | 8 segundos | Restricciones de exclusión y de unicidad, con control de versión y de conflicto |
| Veredicto y auditoría | 4 segundos | Causal, evidencia, regla y correlación |
| Respuesta al operador | 3 segundos | Incluye el tránsito de red y la puerta de enlace |
| Total con margen | 25 más 5, igual a 30 segundos | Ningún reintento rebasa el plazo total |

*Fuente: elaboración propia sobre Caso, RT-09.01, p. 32.*

El reparto es de diseño y todavía no tiene medición. Los 660 milisegundos nominales de la
Figura 4.3 corresponden a un caso favorable, con la caché vigente, y no acreditan el
tiempo de extremo a extremo. Un objetivo interno bajo 2 segundos se conserva como hipótesis de
optimización que se mide en las pruebas, sin presentarlo como resultado.

Ante un rechazo, la respuesta identifica la causa y su categoría, que puede ser una regla, un dato
insuficiente, un conflicto o un error técnico. Trae el umbral, el dato evaluado y el motivo, sin mostrar
antecedentes personales a un rol que no puede verlos. Lleva el viaje, el intento y las operaciones
relacionadas con su identificador de correlación, y también la versión de la regla aplicada y las
evidencias que sostienen el veredicto. Una petición repetida devuelve el resultado ya confirmado, y una
operación todavía en curso devuelve conflicto, sin emitir una segunda asignación. La regla RN-04 admite
una excepción solo cuando una fuente de evidencia no está disponible. La aprueban el jefe de turno y
prevención de riesgos, con motivo, para un solo viaje y con revisión mensual, y nunca cubre una jornada
agotada ni un documento legal faltante.

La Figura 4.3 muestra los patrones que aíslan el despacho de las integraciones externas.

![Figura 4.11. Patrones de resiliencia y presupuesto nominal de diseño](../../figuras/04-arquitectura/audit-figura-4.3-resiliencia.png)

*Figura 4.11. Patrones de resiliencia y presupuesto nominal de diseño*

Fuente: Elaboración propia.

La figura sigue la asignación desde la puerta de enlace hasta la persistencia, con los mamparos y
cortacircuitos que la separan de las integraciones externas. Sus tiempos son hipótesis de diseño y no
mediciones. La Figura 4.4 detalla los mensajes de la asignación.

![Figura 4.2. Secuencia de la asignación bloqueante y publicación desde la bandeja de salida](../../figuras/04-arquitectura/4-3-asignacion.pdf)

*Figura 4.2. Secuencia de la asignación bloqueante y publicación desde la bandeja de salida*

Fuente: Elaboración propia.

La transacción reúne la reserva, la asignación y la bandeja de salida, y la confirmación se devuelve solo
después del commit. La publicación se reintenta desde la bandeja y el consumidor deduplica, lo que cierra
la ventana en que un viaje podía quedar confirmado sin su evento. La rama de rechazo mantiene el bloqueo
ante un incumplimiento o un plazo agotado, porque el sistema impide la asignación y no se limita a
advertirla (Caso, numeral 9.1, p. 22). La excepción de RN-04 es un procedimiento aparte y aprobado, nunca
un reintento que cambie el veredicto en silencio.

### 4.1.10 Idempotencia y ventana de deduplicación

RT-02.06 exige escrituras idempotentes, y cada operación lleva una clave única. La caché puede retenerla
siete días para acelerar los reintentos frecuentes, pero siete días no cubren un cierre de doce. Por eso
la unicidad duradera y la respuesta registrada se conservan mientras se retiene el registro de negocio,
también en una reconexión tras 288 horas. La clave se bloquea en el almacén en memoria y se respalda con
una restricción de unicidad duradera en el motor transaccional, de modo que un reintento tras la
reconexión masiva no duplica un viaje ni un documento.

La ventana opera en dos niveles con propósitos distintos. El nivel en memoria resuelve la concurrencia
inmediata. Si la clave ya está tomada y la operación sigue en curso, la petición se rechaza como
conflicto. Si ya se completó, se devuelve la respuesta guardada en lugar de repetir la escritura. El
nivel duradero resuelve el caso que importa aquí, el mensaje que llega desde el búfer de un camión
después de días sin cobertura, cuando la clave ya expiró en memoria. La restricción de unicidad lo
descarta sin importar cuánto tiempo pasó. RT-02.07 exige además deduplicación en el consumidor y orden
garantizado dentro de la partición, y ambos se aplican al flujo de telemetría.

### 4.1.11 Gobernanza de interfaces y contratos

FEP02, RT-05.16, p. 12 obliga a documentar los servicios síncronos en OpenAPI 3.1 y los flujos dirigidos
por eventos en AsyncAPI 2.6 o superior, y exige que esa documentación se genere desde el código y se
mantenga actualizada de forma automática. La consecuencia práctica es que no se admite discrepancia
entre el contrato publicado y la implementación viva, porque el contrato no se escribe aparte. Como
ejemplo, el servicio síncrono de verificación previa al despacho expone `POST
/api/v1/despacho/validar` bajo OpenAPI 3.1. Recibe los identificadores del viaje, del conductor, del
tractocamión, del semirremolque y de la carga, y devuelve el veredicto, la latencia de la validación y la
bitácora auditable de los factores evaluados. El evento asíncrono de salida se describe bajo
AsyncAPI 2.6 en el canal de eventos de operación, en formato CloudEvents, con identificador único,
agregado, secuencia, versión de esquema y correlación. El transporte autenticado y el sellado de las
evidencias se definen según el tipo de evento, y un código HMAC no se presenta como firma tributaria.

RT-05.17 obliga a versionar semánticamente los contratos, con compatibilidad hacia atrás y política de
obsolescencia con preaviso mínimo de seis meses. RT-05.18 fija el mecanismo de autenticación entre
sistemas y prohíbe la clave estática en la ruta de la dirección web. RT-05.19 exige registrar la
transacción de entrada y la de salida de toda integración con un identificador de correlación común,
que es lo que permite seguir una operación de negocio a través de todos los sistemas que toca. Ese
identificador es el mismo que usa la capa de observabilidad.

RT-05.21 obliga a declarar, por cada integración, el modo, el volumen esperado, la ventana de
disponibilidad de la contraparte y el comportamiento de la solución cuando esa contraparte no
responde. Esa declaración se entrega en la Tabla 4.4.

**Tabla 4.4.** Declaración por integración conforme a RT-05.21

| Contraparte | Modo | Volumen esperado | Ventana de la contraparte | Si no responde |
|---|---|---|---|---|
| Sistema contable y de facturación | Solicitud y respuesta para emitir, asíncrono para asientos | Hasta 128.000 documentos y los eventos de 96.000 viajes al año | Emisión continua por acordar y probar, porque el Caso no la declara | Se encola la solicitud y se bloquea la salida sin documento conforme |
| Plataformas de posicionamiento de terceros | Asíncrono | Posición de los camiones de terceros con dispositivo | No declarada por el Caso | Última posición conocida con su antigüedad visible, nunca una posición sin fecha |
| Telemetría de fábrica | Asíncrono | 61 tractocamiones, solo lectura | Sujeta a la autorización de cada fabricante | El viaje se registra igual con el dispositivo a bordo |
| Red de estaciones de servicio | Por lotes | 74.000 abastecimientos al año | Mensual, con hasta 40 días de desfase | El costo se emite preliminar y se marca como pendiente |
| Concesionarias de peaje | Por lotes | 620.000 pasadas al año | Mensual | Peaje estimado por la traza, marcado como estimado |
| Autoridad tributaria, a través del sistema contable | Según el contrato fiscal del emisor | 128.000 documentos al año | Según el servicio de la autoridad | Contingencia fiscal admitida y documentada, sin que audIT emita |
| Clientes y autoridad aduanera | Ambos | Según contrato y cruce | Variable | Reintento con retroceso y aviso a la torre |

*Fuente: Caso, numeral 14.1, p. 29, y elaboración propia.*

Los volúmenes de esta tabla provienen del Caso, numeral 14.1, p. 29. La ventana de disponibilidad de las
plataformas de terceros, de la autoridad tributaria y de la emisión continua del sistema contable no
está declarada en las bases y se consulta al mandante. RT-05.22 exige además carga y descarga masiva en
formatos abiertos, con validación previa, informe de errores por registro y procesamiento parcial. Esa
capacidad es la que sostiene la migración de las cerca de 6.000 vigencias y la ingesta mensual de
combustible y peajes. La Figura 4.5 dibuja el mapa de integraciones.

![Figura 4.3. Mapa de integraciones. Sistemas internos, fuentes de terreno y contrapartes externas](../../figuras/04-arquitectura/LogicaIntegraciones.png)

*Figura 4.3. Mapa de integraciones. Sistemas internos, fuentes de terreno y contrapartes externas*

Fuente: Elaboración propia.

La figura distingue el sistema de gestión de 2013, que se sustituye, del sistema contable, que se
conserva como único emisor tributario detrás de la capa anticorrupción. Los 192 camiones de terceros
con equipo son la población de referencia, y el dibujo no acredita un acceso automático a las tres
plataformas. La cobertura efectiva y su antigüedad se muestran por unidad, y los equipos del vehículo
se leen solo en modo lectura.

### 4.1.12 Convivencia con el sistema contable heredado

Los servicios de negocio sustituyen los módulos operativos del sistema de gestión de 2013. La capa
anticorrupción traduce los contratos y encapsula el sistema contable, que se conserva como único
emisor de documentos tributarios. El aislamiento es bidireccional. Un cambio en el sistema externo no
propaga su modelo al núcleo, y el núcleo no escribe directamente sobre el legado.

RT-02.14 valora la aplicación documentada de patrones de arquitectura evolutiva que permitan
sustituir un componente sin reescribir la solución, y nombra tres. Esta oferta aplica los tres. La capa
anticorrupción frente al sistema heredado, el estrangulamiento progresivo con que los módulos
operativos de 2013 se van sustituyendo función por función en lugar de en un corte único, y la
abstracción de proveedores, que es lo que permite declarar la estrategia de reversibilidad que exige
RT-03.07. La capa tiene cuatro piezas. El adaptador de dominio traduce el evento de negocio, viaje
cerrado o liquidación aprobada, a la estructura plana que espera el sistema contable. El transformador
de esquemas homologa los formatos en ambos sentidos, para que las convenciones de 2013 no lleguen al
modelo nuevo. El protector de resiliencia combina cortacircuito y cola de mensajes fallidos: si el
sistema contable no responde, las solicitudes quedan pendientes y las salidas sin documento conforme se
bloquean. El reconciliador verifica que todo evento encolado terminó registrado y expone lo pendiente en
lugar de dejarlo en silencio.

La Figura 4.6 muestra la integración con el sistema contable a través de esa capa.

![Figura 4.4. Integración con el sistema contable heredado a través de la capa anticorrupción](../../figuras/04-arquitectura/audit-figura-4.4-acl.png)

*Figura 4.4. Integración con el sistema contable heredado a través de la capa anticorrupción*

Fuente: Elaboración propia.

El sistema contable queda detrás de la capa y solo recibe eventos ya traducidos.

### 4.1.13 Emisión del documento de transporte sin cobertura

La restricción 8 del Caso fija que el sistema contable y de facturación es el único emisor del
documento tributario de transporte (Caso, capítulo 10, p. 24). La cabina y el terminal no generan folios
ni firman documentos tributarios. Los requerimientos RF-013 y RF-014 del Formulario T-12 piden el
documento conforme antes de iniciar el traslado, también en un punto de carga sin cobertura, y asignar
recursos no habilita la salida por sí solo. La Figura 4.7 muestra los dos caminos del
Subdocumento 3. La emisión anticipada sirve cuando la carga definitiva se conoce al programar el
despacho, y la solicitud satelital, cuando solo se conoce en el punto sin cobertura. En los dos el
sistema contable emite y la cabina recibe el contenido íntegro que necesita para portar una
representación conforme, porque un folio o una huella no bastan.

![Figura 4.5. Emisión del documento de transporte sin cobertura: emisión anticipada o solicitud satelital al único emisor](../../figuras/04-arquitectura/documento-sin-cobertura.pdf)

*Figura 4.5. Emisión del documento de transporte sin cobertura: emisión anticipada o solicitud satelital al único emisor*

Fuente: Elaboración propia.

Con la mensajería SBD de la familia 9603, Iridium permite hasta 340 bytes de subida y 270 de bajada por
mensaje (Iridium Communications, 2026). Un documento completo puede necesitar varios mensajes. El protocolo propuesto usa una solicitud correlacionada con versión, longitud, número de
fragmento e integridad, y un reensamblado verificable. El original XML firmado se conserva en el
sistema contable y en su custodia. La cabina recibe todos los datos y el timbre que necesita para
portar la representación válida, o el archivo de representación completo. No hace falta transmitir todo
el XML si esa representación no lo requiere, pero tampoco se acepta una representación incompleta armada
con el folio o con una huella. La pasarela satelital necesita un adaptador autorizado hacia la
plataforma, porque Iridium no habla directamente el protocolo de IoT Hub.

El límite total de la emisión es de 90 segundos (Caso, RT-09.01, p. 32). Se mide la solicitud, la emisión,
el retorno en fragmentos, la verificación y la disponibilidad portable, con el documento de mayor tamaño
previsto. Si el documento comprimido pesa \(B\) bytes y cada mensaje lleva una cabecera de \(h\) bytes, con
\(0 \le h < 270\), la bajada necesita al menos \(\lceil B/(270-h) \rceil\) mensajes. El ensayo incluye
pérdidas, reintentos y el tiempo propio del satélite, y no supone que un timbre completo quepa en un
solo mensaje.

La contingencia por falta de cobertura que describe el Servicio de Impuestos Internos permite emitir la
guía fuera de línea y enviarla al recuperar la conexión (Servicio de Impuestos Internos, 2026; Servicio de Impuestos Internos, 2019),
pero no autoriza a audIT a emitir desde la cabina, porque la restricción 8 mantiene al sistema contable
como emisor. La representación y el envío fiscal siguen el régimen que aplique al contribuyente. Medir que el
retorno satelital completo quepa en 90 segundos es condición previa para aceptar ese camino. Si no se logra, se revisan la decisión 06 de la Tabla 4.2 y el Formulario T-11, y
mientras tanto la regla es bloquear la salida sin documento conforme. Ese riesgo se trata en el
Subdocumento 8. La Figura 4.8 detalla el intercambio y el cotejo previo al movimiento.

![Figura 4.6. Secuencia de emisión, entrega y comprobación previa a la salida](../../figuras/04-arquitectura/4-4-documento.pdf)

*Figura 4.6. Secuencia de emisión, entrega y comprobación previa a la salida*

Fuente: Elaboración propia.

La salida se habilita solo con la carga coincidente, el documento válido y la representación portable
disponible. Un cambio posterior de la carga obliga a corregir con el emisor y a evaluar de nuevo, y la
cabina no modifica la copia firmada ni reutiliza un folio para otro viaje.

### 4.1.14 Fuentes con desfase y telemetría del vehículo

Dos integraciones no entregan datos en el momento en que ocurren y la arquitectura las trata como
tales. El consumo de combustible llega con hasta 40 días de desfase (Caso, numeral 7.3, p. 15), y los
peajes se liquidan mensualmente. Ambas se ingieren por lotes desde un depósito seguro, con validación
sintáctica y verificación de totales, y ambas quedan detrás de un adaptador, de modo que el día en que
una de esas contrapartes publique una interfaz en línea baste conectar el adaptador nuevo sin tocar el
modelo de costeo.

Ingerir el archivo no basta. Cada carga de combustible se cruza contra la posición del camión en ese
instante y cada pasada de peaje contra la traza del viaje. Ese cruce es lo que convierte un archivo de
cobros en costo imputable a un viaje, y es también lo que deja a la vista la carga que se registró en
una estación por la que el camión no pasó. Son 74.000 abastecimientos y 620.000 pasadas de peaje al año
según el Caso, numeral 14.1, p. 29, volumen que no admite revisión manual.

Un tercer frente es la posición de la flota de terceros. El Caso declara 340 de 374 camiones con
dispositivo repartidos en tres plataformas distintas (Caso, numeral 14.1, p. 29), dos de ellas con acceso
de solo consulta y una que ni siquiera permite exportar (Caso, numeral 16.1, p. 34). Unificar esa vista es
obligación de esta oferta y reemplazar esos equipos está excluido (Caso, capítulo 11, p. 24). Lo que se
entrega es la vista unificada y el estándar de homologación contra el cual clasificar cada equipo, no
un inventario de un parque que el Caso no describe.

La telemetría de fábrica de los 61 tractocamiones se lee en modo de solo lectura, sujeta a la
autorización de cada fabricante que exige Caso, RT-17.06, p. 34. Que el acoplamiento no tenga contacto
eléctrico no prueba por sí solo la autorización ni la disponibilidad de las señales, y cada lectura
necesita protocolo, parámetros, licencia de acceso y homologación del fabricante. La restricción 6
prohíbe que el equipamiento a bordo afecte la garantía del vehículo o interfiera con sus sistemas de
seguridad, y el Capítulo 11 excluye intervenir la electrónica de fábrica. No cortar ni empalmar el arnés
reduce la intervención, pero la conformidad con la garantía y la seguridad se verifica por modelo de
vehículo, y los 182 lectores previstos no implican 182 fuentes CAN disponibles. Se leen el consumo
instantáneo y acumulado, que es el componente medido del costo por kilómetro de la flota propia, y el
nivel de estanque, que se contrasta con el abastecimiento facturado por la red de estaciones. Las
revoluciones y las aceleraciones bruscas sirven a la conducción eficiente y explican la dispersión de
rendimiento de 19 por ciento entre camiones del mismo modelo y ruta. El odómetro da el kilómetro
efectivo del viaje, que es el denominador del costo. Las horas de funcionamiento y de ralentí miden el
consumo que no produce kilómetro, y el uso del freno de servicio y del freno motor alimenta el
mantenimiento por condición, según el criterio 18 del Caso.

Todos son parámetros de lectura. Ninguno escribe sobre el bus del vehículo, y esa restricción es de
diseño y no de configuración.

### 4.1.15 Capa analítica y costo real por kilómetro

La segregación entre lo transaccional y lo analítico se resuelve por captura de cambios hacia un
repositorio organizado en capas sucesivas de refinamiento, desde el dato crudo hasta el modelo
dimensional que consume la gerencia. La replicación lee la bitácora del motor transaccional y no
consulta sus tablas, para que la analítica no consulte la base de la operación, como pide RT-05.05. La
lectura del WAL y sus slots consumen recursos, se vigilan, y la separación se comprueba bajo carga. El
repositorio tiene tres capas. La cruda guarda el registro tal como llegó, desde la replicación
transaccional, la posición telemática y los archivos mensuales de combustible y peaje, lo que permite
reprocesar todo sin volver a la fuente y trazar el origen de cada indicador. La depurada deduplica,
valida coordenadas, corrige marcas de tiempo y cruza la telemetría con el tramo de la orden, de modo que
un mismo hecho tenga una sola representación. La de negocio es un modelo dimensional con el hecho de
costo por viaje y por tramo y las dimensiones de ruta, cliente, tracto, conductor, régimen de propiedad
y tiempo, que la gerencia consulta sin conocer el modelo transaccional.

La Figura 4.9 muestra la capa analítica y la explotación del costo por kilómetro.

![Figura 4.7. Capa analítica por niveles de refinamiento y explotación del costo por kilómetro](../../figuras/04-arquitectura/audit-figura-4.5-analitica.png)

*Figura 4.7. Capa analítica por niveles de refinamiento y explotación del costo por kilómetro*

Fuente: Elaboración propia.

El costo por kilómetro se calcula distinto según el régimen de propiedad del equipo. Para la flota
propia se compone de combustible medido por telemetría, peajes efectivamente transitados, neumáticos,
mantenimiento, jornada del conductor y depreciación. Para la flota subcontratada el mandante solo
conoce la tarifa pactada y los anticipos de combustible, de modo que el resto se imputa. Esa diferencia
hay que declararla, porque comparar flota propia con flota de terceros sin declararla es comparar cosas
distintas, y esa comparación gobierna la decisión de crecer con una u otra. La Tabla 4.5
muestra el origen de cada componente.

**Tabla 4.5.** Componentes del costo por viaje y su origen

| Componente | Flota propia | Flota subcontratada |
|---|---|---|
| Combustible | Medido por telemetría y valorizado con la liquidación mensual | No observable, porque la compañía solo conoce el anticipo que otorga |
| Peajes | Pasada efectiva cruzada con la traza | Igual, cuando el peaje lo asume la compañía |
| Conductor | Jornada imputada al tramo | Incluida en la tarifa pactada, no descomponible |
| Mantenimiento y neumáticos | Cuota por kilómetro sobre la orden de taller y la posición de neumático | No observable |
| Sobreestadía | Horas de espera acreditadas por geocerca | Igual |
| Tarifa a terceros | No aplica | Costo directo contractual |
| Denominador | Kilómetro del odómetro telemático | Kilómetro de la traza de posición |

*Fuente: elaboración propia.*

El mecanismo es dual y no es una elección de diseño, es lo que el propio Caso fija.
Caso, RT-05.29, p. 32 exige el costo consolidado de un viaje en no más de 24 horas tras su cierre, con los
componentes que a esa fecha estén disponibles y con indicación explícita de los que aún no lo están. Se
emite entonces una versión preliminar dentro de esas 24 horas, marcada como tal y enumerando qué falta,
y una versión definitiva cuando llegan el combustible y los peajes. La primera no se sobrescribe. Ambas
coexisten, y la desviación entre una y otra mide la calidad de la estimación. Sin ese doble paso el
costo por viaje se convierte en un cierre contable tardío, que es exactamente la condición que permitió
servir tres contratos bajo costo, el peor durante cuatro años.

El mismo RT-05.29 fija el resto de las latencias analíticas, que gobiernan el diseño de la capa. La
posición de un camión con cobertura debe estar disponible en 2 minutos, la jornada acumulada de un
conductor en tiempo real al momento de asignar, y el tiempo de llegada y de salida en un punto de
cliente en el momento del evento. El costo consolidado de un viaje tiene 24 horas tras su cierre, con
indicación de los componentes pendientes, y las emisiones se consolidan cada mes
(Caso, RT-05.29, p. 32).

La jornada acumulada es la que condiciona la arquitectura. Exigirla en tiempo real en el momento de
asignar significa que no puede leerse del repositorio analítico. Por eso la evaluación usa el estado
autoritativo o una proyección cuya versión y actualidad se comprueban antes del commit, y una caché
antigua no habilita al conductor.

### 4.1.16 Explotación analítica y autoservicio

RT-05.25 obliga a proveer tableros operacionales y de gestión sobre los indicadores que el Caso define.
RT-05.26 exige poder filtrar por período y por dimensión propia del caso y profundizar desde el
indicador agregado hasta la transacción de origen. Esa navegación termina en el viaje individual con su
traza, su documento de transporte y su respaldo de entrega, y no en un subtotal.

RT-05.27 obliga a que el cliente construya sus propios informes sin intervención del adjudicatario,
mediante una herramienta de autoservicio con modelo semántico documentado. El modelo semántico se
entrega validado con la gerencia de administración y finanzas, con las métricas nombradas y definidas
una sola vez, de modo que margen por ruta signifique lo mismo en todos los tableros. RT-05.28 exige que
todo informe sea exportable en formatos abiertos y programable para envío automático por calendario.

RT-05.30 valora la analítica predictiva con el modelo, sus variables, su métrica de desempeño y su plan
de reentrenamiento documentados. Es un requisito deseable y esta oferta lo aborda en el
Subdocumento 13.

### 4.1.17 Secuencia de liquidación y costeo por viaje

La consolidación del costo de un viaje y la liquidación a los transportistas siguen la secuencia de la
Figura 4.10, desde el cierre del viaje hasta el acuse del sistema contable.

![Figura 4.8. Secuencia del costeo por viaje, la conciliación de insumos y la liquidación en el sistema contable](../../figuras/04-arquitectura/4-6-liquidacion.pdf)

*Figura 4.8. Secuencia del costeo por viaje, la conciliación de insumos y la liquidación en el sistema contable*

Fuente: Elaboración propia.

Al cerrar el viaje, Liquidación y costeo emite la versión preliminar del costo en menos de 24 horas
(Caso, RT-05.29, p. 32). Cada vez que llega una cartola de combustible o de peaje se registra una versión
auditada nueva, sin sobrescribir la anterior, hasta la definitiva. El costo preliminar de un viaje y la
liquidación mensual son registros distintos. La liquidación se propone al transportista con el detalle
por viaje, y su aceptación o su discrepancia quedan trazadas antes de enviarla al sistema contable. Una
evidencia insuficiente deja el componente sin valor y abre una excepción para revisión, en lugar de
registrarlo como cero. Sin el acuse contable la liquidación queda pendiente, y los reintentos son
idempotentes, así que ningún pago se duplica.

### 4.1.18 Modelo táctico del dominio

RT-02.13 exige presentar el modelo de dominio del negocio con las entidades principales, sus relaciones
y los eventos de negocio que las modifican. El modelo táctico de la Figura 4.11 lo entrega
organizado por contexto delimitado, de modo que cada agregado quede bajo el contexto que lo posee.

![Figura 4.12. Modelo táctico del dominio. Agregados, entidades y objetos de valor por contexto, con los eventos de dominio entre contextos](../../figuras/04-arquitectura/audit-figura-4.6-tactico.png)

*Figura 4.12. Modelo táctico del dominio. Agregados, entidades y objetos de valor por contexto, con los eventos de dominio entre contextos*

Fuente: Elaboración propia.

Cada agregado de la figura pertenece a un solo contexto delimitado. Los eventos de dominio van en línea
discontinua, desde el contexto que los publica hasta el que los recibe. Los comandos y los eventos de
cada contexto se detallan en la sección 4.1.22.

### 4.1.19 Responsabilidad y emplazamiento de componentes lógicos

La Tabla 4.6 resume la responsabilidad y el emplazamiento de cada componente lógico, y las
cantidades y configuraciones completas están en el Formulario T-11. Cada contexto guarda sus datos bajo
un solo propietario y expone contratos, sin acceder a las tablas de otro. El FEP01, Artículo 16.2, p. 11 obliga a
justificar el emplazamiento componente por componente.

**Tabla 4.6.** Componentes lógicos y fundamento de su emplazamiento

| Componente | Responsabilidad | Emplazamiento y motivo |
|---|---|---|
| Planificación y tráfico | Orden, asignación y retornos | Servicios en AKS, con estado coherente de todos los recursos dentro del plazo de 30 segundos |
| Flota y activos | Aptitud, semirremolque y taller | AKS con maestros acreditados y lectura autorizada, mientras la captura instrumental reside a bordo |
| Personas y cumplimiento | Evidencia, jornada, habilitaciones y permisos | AKS con registro local, para decidir con identidad y evidencia conservadas y no con datos analíticos |
| Telemetría y geocercas | Captura, posición, llegada, salida y reconexión | Captura y evaluación de geocerca a bordo, con ingesta y vista unificada en la nube |
| Operación de fletes | Viaje ocurrido, documento, conformidad y carga peligrosa | AKS y aplicación de terreno, con el emisor tributario fuera de la solución y detrás de la capa anticorrupción |
| Liquidación y costeo | Versiones de costo y liquidación | Servicio con repositorio analítico separado, que entrega al sistema contable solo registros aprobados y traducidos |
| PostgreSQL, TimescaleDB y Redis | Negocio, series y caché | Instancias separadas según el Subdocumento 5 y el T-11, sin que Redis sea autoridad única del despacho |
| IoT Hub, Event Hubs y bandeja de salida | Admisión, eventos y publicación duradera | Nube, con identidad por dispositivo, cuotas, partición, reintento y deduplicación |
| Búfer, aplicación móvil y terminal | Captura sin enlace y copia documental | Equipo local y aplicación por perfil, con la autonomía de la sección 4.1.26 |

*Fuente: elaboración propia sobre el FEP01, Artículo 16.2, p. 11.*

La tabla usa los seis nombres de contexto del Subdocumento 3. Los objetivos de latencia son los del
Caso, y una estimación en milisegundos de un componente es una hipótesis y no una prueba de
cumplimiento de extremo a extremo.

### 4.1.20 Concurrencia y volumen declarados

Caso, RT-09.02, p. 32 no fija un número. Ordena derivarlo de la volumetría del numeral 14.1 y declararlo
conforme al numeral 14.2, considerando de manera expresa la reconexión simultánea de unidades al salir
de zonas de sombra. La derivación de la concurrencia está en la Tabla 4.7.

**Tabla 4.7.** Concurrencia derivada de la volumetría del Caso

| Población | En hora punta | Base de la derivación |
|---|---|---|
| Personal interno con acceso a sistemas | 50 a 80 | Torre de 22 personas en turno, despacho de terminal, finanzas, facturación y taller, sobre los 336 con acceso del numeral 14.1 |
| Conductores en aplicación móvil | 100 a 150 | Accesos breves de inicio y cierre de turno sobre 454 conductores |
| Transportistas subcontratados en portal | 30 a 50 | Consulta de viajes y de liquidación sobre 148 |
| Clientes en seguimiento | 50 a 100 | Sesiones de seguimiento sobre 84 clientes activos |
| Suma aritmética de los rangos | 230 a 380 | Extremo inferior y superior de las cuatro filas |
| Concurrencia de dimensionamiento | 380 | Hipótesis de diseño que suma los extremos superiores y se ensaya con 570 sesiones |

*Fuente: elaboración propia sobre el Caso, numeral 14.1, p. 29.*

Las 380 sesiones son una hipótesis de diseño, que el Caso no fija y el contrato no compromete. La prueba
de carga de RT-09.06 las ensaya con 1,5 veces ese valor, 570 sesiones, y la misma cifra rige en la
arquitectura física y en el plan de pruebas. El volumen anual y los perfiles de ráfaga se derivan en la
Tabla 4.8. Son supuestos de capacidad que pide el Caso, numeral 14.2, p. 30, y se reemplazan por
mediciones en el levantamiento.

**Tabla 4.8.** Derivación reproducible de la carga de datos

| Magnitud | Fórmula y resultado | Alcance del supuesto |
|---|---|---|
| Horas anuales en marcha | 41.000.000 km / 55 km/h = 745.455 h | El kilometraje es dato del Caso y la velocidad es el supuesto S-01 |
| Posición en marcha | 745.455 h \(\times\) 120 muestras/h \(≈\) 89,45 millones | Una muestra cada 30 s, con la vista completa futura de 374 unidades y no con el acceso actual |
| Posición detenida | (374 \(\times\) 8.760 \(-\) 745.455) h \(\times\) 12 muestras/h \(≈\) 30,37 millones | Una muestra cada 5 min en un año de 365 días |
| Posición total en bytes crudos | 119,82 millones \(\times\) 64 bytes \(≈\) 7,67 GB al año | Registro binario del supuesto S-03, sin JSON, índices, transporte ni réplicas |
| Motor, escenario inicial de 61 unidades | (745.455 \(\times\) 61 / 374) h \(\times\) 60 \(\times\) 160 bytes \(≈\) 1,17 GB al año | Reparto proporcional de la marcha, sin suponer CAN activo en toda la flota |
| Admisión normal máxima | 374/30 + 182/60 \(≈\) 15,5 eventos/s | Escenario simultáneo de diseño, al que se suman los eventos de negocio |
| Asignación en punta | 22 puestos \(\times\) 1 asignación/30 s \(≈\) 0,73 TPS, y 7,33 TPS en una ráfaga de 10 veces | Hipótesis de carga que no divide viajes anuales por usuarios |
| Reconexión de 300 unidades tras 72 h | 1.786.200 registros y 971.296.800 bytes con fotos, a no menos de 1.861 registros/s en 960 s útiles | Los 20 minutos menos 20 % de reserva, con unos 10,12 Mbit/s útiles |
| Series en línea por dos años | Posición cruda \(≈\) 15,34 GB y motor inicial \(≈\) 2,34 GB | Factor físico provisional de 3 para índices, WAL y réplicas, sujeto a medición |

*Fuente: elaboración propia sobre el Caso, numerales 14.1 y 14.2, pp. 29 y 30.*

La tabla cubre las series de posición y de motor, con supuestos de muestreo, de población y de tamaño
de registro. Los volúmenes transaccionales e históricos se estiman en el
Subdocumento 5 y en la sección 4.2.8. El perfil de 72 horas por camión y la
reserva de búfer propuesta de 288 horas se tratan aparte del volumen anual, y el cierre vial de doce
días no equivale por sí solo a doce días sin enlace. Caso, RT-05.10, p. 31 exige dos años en línea para
posición y telemetría, con agregación declarada para el resto. El crecimiento a tres veces la
volumetría inicial se prueba según FEP02, RT-09.03, p. 21, aparte del estrés con 570 sesiones y de la
ráfaga de 300 reconexiones, porque son ensayos distintos.

### 4.1.21 Modelado de amenazas de la arquitectura

FEP02, RT-26.07, p. 45 exige un modelado de amenazas propio para toda innovación que modifique la
arquitectura de seguridad. La baliza Bluetooth del semirremolque, de la innovación 3 del
Subdocumento 13, es una fuente nueva de datos, y la Tabla 4.9 modela sus amenazas con la
clasificación STRIDE. Son controles propuestos de diseño y no evidencia de pruebas de seguridad
ejecutadas. Se prueban en la Etapa 1, y si cambia el protocolo o el alcance de la baliza, el modelo se
actualiza antes de su aprobación.

**Tabla 4.9.** Amenazas de la baliza y controles de diseño

| Categoría | Amenaza | Control de diseño |
|---|---|---|
| Suplantación | Baliza desconocida o asociada a otro semirremolque o viaje | El identificador se vincula al activo y al viaje vigente, y un evento desconocido se excluye de la evidencia |
| Manipulación | Evento alterado, repetido o fuera de secuencia | Se validan esquema y vigencia, se conserva la procedencia y se aplican deduplicación e idempotencia |
| Repudio | Disputa sobre el origen o el tratamiento del evento | Se registran la fuente, la hora de recepción, el viaje y las acciones posteriores, con cada rectificación enlazada al registro original |
| Divulgación | Exposición de la ubicación o de la asociación entre conductor y semirremolque | La consulta se limita a los roles y al viaje habilitados, con los datos mínimos |
| Denegación de servicio | Pérdida, retraso o ráfaga de eventos | Se controla la tasa, se muestra la antigüedad de la última señal y la vista se degrada sin inventar posiciones |
| Elevación de privilegios | Evento usado para alterar el despacho o actuar sobre el vehículo | La ingesta es de solo lectura y la baliza no cambia el estado del viaje ni actúa sobre el bus del vehículo |

*Fuente: elaboración propia sobre FEP02, RT-26.07, p. 45.*

La baliza queda como fuente auxiliar. Su señal sola no acredita jornada ni descanso, la operación
conserva la procedencia de cada evento, y las reglas de despacho y de jornada se evalúan con
independencia de ella. Las demás amenazas de la arquitectura se tratan en la
sección 4.1.24.

### 4.1.22 Estilo, principios de diseño y contratos de dominio

El estilo combina servicios independientes, transacciones locales y eventos. Un monolito modular cuesta
menos de operar, pero no permite el despliegue independiente que FEP02, RT-02.02, p. 6 exige a los
componentes críticos. Una cadena síncrona de servicios multiplica los tiempos de espera, y una
arquitectura orientada a servicios con orquestación central concentra las fallas. Los seis contextos,
con interfaces para las decisiones inmediatas y eventos para los efectos derivados, separan la carga
normal de unos 15,5 eventos por segundo de la ráfaga de reconexión de al menos 1.861 registros por
segundo.

Los principios SOLID se aplican así. Cada servicio tiene la responsabilidad de un solo contexto, que es
el principio de responsabilidad única. Un proveedor nuevo entra mediante un adaptador del mismo
contrato, sin modificar el núcleo, que es el principio de abierto y cerrado. Todo adaptador debe pasar
las pruebas comunes de ese contrato, que es la sustitución de Liskov. Las interfaces de jornada, de
permisos y de liquidación se separan según quién las consume, que es la segregación de interfaces. El
dominio depende de puertos de repositorio y de mensajería y no del SDK de la nube, que es la inversión
de dependencias. La descripción de vistas y preocupaciones sigue ISO/IEC/IEEE 42010
(ISO, 2022), y el gobierno arquitectónico, equivalente a TOGAF, se ejerce con los ADR, el
comité de arquitectura y la revisión mensual, como pide el FEP01, Artículo 4.3, p. 6.

La Tabla 4.10 completa la Figura 4.11 con los comandos y los eventos de cada
contexto. Los nombres de los contratos son propuestas para la implementación. Cada evento lleva
identificador, agregado, versión, secuencia y correlación, con su esquema en AsyncAPI y su política de
compatibilidad.

**Tabla 4.10.** Comandos y eventos por contexto

| Contexto | Comando principal | Evento derivado y consumidor |
|---|---|---|
| Planificación y tráfico | AsignarRecursos y ReprogramarViaje | ViajeAsignado hacia Operación y Telemetría, con el rechazo conservado en auditoría |
| Flota y activos | AcreditarVigencia y RegistrarIntervencion | AptitudEquipoActualizada hacia Planificación, que invalida la proyección afectada |
| Personas y cumplimiento | EvaluarAsignacion y RevocarPermiso | JornadaActualizada y PermisoRevocado hacia Planificación y los canales autorizados |
| Telemetría y geocercas | IngerirLote y EvaluarGeocerca | LlegadaRegistrada y SalidaRegistrada hacia Operación, con la posición autorizada hacia el portal |
| Operación de fletes | SolicitarDocumento y CerrarViaje | DocumentoDisponible y ViajeCerrado hacia Planificación y Liquidación |
| Liquidación y costeo | CalcularCosto y AprobarLiquidacion | CostoVersionado y LiquidacionAprobada hacia el portal y la capa anticorrupción |

*Fuente: elaboración propia.*

La tabla no requiere una transacción distribuida entre seis bases. Planificación valida versiones y
reservas en su propia transacción, y cada contexto conserva sus agregados y publica sus efectos desde su
bandeja de salida. Un cambio concurrente que invalida una habilitación obliga a evaluar de nuevo antes
de confirmar.

### 4.1.23 Trazabilidad del alcance

El Formulario T-12 vigente mantiene 28 requerimientos funcionales y 14 no funcionales, con sus paquetes
de la EDT y sus casos de prueba. Los contratos de esta sección corresponden a ese catálogo, y los
componentes se ubican en la Tabla 4.6 y en la Figura 4.1. RF-001 atraviesa
Planificación, Personas y Flota. RF-013 y RF-014 terminan en la capa anticorrupción y en el sistema
contable. RNF-008 atraviesa el borde, la ingesta y la persistencia. Con esa relación se comprueba la
cobertura del alcance sin convertir el cuerpo en un inventario de formularios.

### 4.1.24 Seguridad lógica y superficie de exposición

El acceso público termina en Front Door, con su cortafuegos de aplicación, y en API Management. Las
bases, el bus, los secretos y los servicios internos quedan en red privada, conforme a
FEP02, RT-03.04, p. 8. El seguimiento sin autenticación muestra solo el estado del envío con el número
de documento, sin posición personal ni historial del transportista (Caso, RT-16.30, p. 33). Los portales
autenticados evalúan en cada petición el rol, el transportista, el recurso, el cliente, el viaje activo,
la finalidad y el permiso vigente.

Entra ID autentica a las personas, y cada equipo usa una identidad con certificado propio y revocable.
El conductor se identifica con el camión detenido, con la tarjeta o el token asignado y su vínculo a la
persona y al viaje, sin contraseña que recordar ni interacción en marcha, como piden
Caso, RT-12.11, p. 32 y Caso, RT-13.08, p. 33. La prueba con guantes y con conductores que rotan pertenece
al plan de pruebas del Subdocumento 9. Las identidades administradas acceden a Key Vault, y las claves y
los secretos no aparecen en el código ni en la dirección web. Se cifran el transporte y los campos que
exige Caso, RT-11.10, p. 32, con claves y roles separados. Cada acceso sensible registra qué se mostró y
con qué autorización (Caso, RT-16.09, p. 33).

Se verifican como mínimo la suplantación de un equipo o de la baliza, la alteración o repetición de
eventos, el repudio de una firma, la consulta entre transportistas, la saturación por reconexiones y la
elevación a administración. La Tabla 4.9 cubre la baliza, y las pruebas del resto se trazan al
Formulario T-17. La huella y el cifrado no bastan por sí solos para acreditar el cumplimiento legal. La segmentación de red que sostiene este modelo Zero Trust está en la
sección 4.2.5.

### 4.1.25 Ambientes y liberación

Desarrollo usa datos sintéticos. Calidad contiene escenarios y simuladores reproducibles.
Preproducción reproduce las integraciones y la configuración sin accesos de producción. Producción
contiene los datos autorizados y los cambios aprobados, y recuperación replica los componentes críticos
con el mecanismo jurídico y de continuidad del Subdocumento 5 y de la sección 4.3.2. Cada ambiente tiene
identidades, secretos, redes, almacenes y permisos separados, y su emplazamiento físico está en la
sección 4.2.6. La configuración se versiona como código y se promueve el mismo artefacto
firmado, según el Subdocumento 6.

La aceptación incluye pruebas de contratos, de carga, de reconexión, de evidencia, de permisos y de
reversa. Activar la réplica en Brazil South con datos personales exige un mecanismo de transferencia
documentado, y deshabilitarla sin otro sitio secundario operativo tampoco acredita un RPO de 15 minutos
ni un RTO de 4 horas. La vía prevista son las cláusulas contractuales tipo del artículo 27 de la Ley
N.º 21.719, que el mandante firma con el proveedor de nube antes del hito H2
(sección 4.3.2). La revisión jurídica y la conmutación probada son, juntas,
condiciones para entrar en producción.

### 4.1.26 Operación desconectada, reconexión y escalamiento

A bordo se conservan la posición, los eventos de jornada, la llegada y la salida y los documentos
durante al menos 72 horas (Caso, RT-03.10, p. 31). En el terminal rige el mayor de los dos mínimos, las 24
horas de FEP02, RT-03.10, p. 9 frente a las 12 horas del Caso. La captura local usa SQLite en modo WAL
con bandeja de salida, y la aplicación comparte la identidad y los catálogos vigentes con el nodo
autorizado. La operación local no inventa vigencias, permisos ni asignaciones globales, y toda
asignación nueva necesita acceso al servicio autoritativo de reserva. RN-04 solo exceptúa una fuente de
evidencia no disponible, bajo sus controles, y no reemplaza la reserva, la legalidad ni el documento
conforme que el movimiento necesita.

La Figura 4.12 muestra la reconexión: autenticación, lotes numerados, admisión,
deduplicación, commit y acuse duradero. Solo el último acuse permite depurar el búfer.

![Figura 4.9. Secuencia de la reconexión, con el acuse posterior a la persistencia y la conciliación por camión](../../figuras/04-arquitectura/4-7-reconexion.pdf)

*Figura 4.9. Secuencia de la reconexión, con el acuse posterior a la persistencia y la conciliación por camión*

Fuente: Elaboración propia.

La conciliación conserva el original y la resolución de cada conflicto, y la hora de recepción no
reemplaza la hora del evento. La prueba CP-PERF-02 debe demostrar que cada camión, después de 72 horas
sin cobertura, deja en 20 minutos todos sus datos transferidos, persistidos y conciliados, fotos
incluidas (Caso, RT-03.13, p. 31), con 300 unidades simultáneas y sin perder jornada ni tiempos de
cliente. Que IoT Hub admita los mensajes no prueba su entrega final. Las
288 horas propuestas y la capacidad del búfer de la sección 4.2.2 requieren otro ensayo y no
reemplazan esta prueba contractual. Los límites de cada tramo de la reconexión se dimensionan en la
sección 4.2.8.

El escalamiento automático que exige FEP02, RT-02.10, p. 7 parte con dos réplicas por contexto. Aumenta
cuando la CPU supera el 65 % o el retraso de consumo pasa de 30 segundos durante dos minutos, y se
reduce solo después de diez minutos estables. El máximo inicial es de ocho réplicas de ingesta y cuatro
por servicio de negocio, sujeto al perfil y a las cuotas del Formulario T-11. Los mamparos reservan
recursos para el despacho, el documento y las emergencias. Al llegar al máximo se alerta a la operación y
se limita la carga no crítica, y la capacidad y el costo no crecen sin registro. El costo de esos
límites va en el Sobre N.º 3, y el plan de pruebas mide la latencia completa, la saturación, el consumo
de recursos y la recuperación antes de aceptar el perfil.

## 4.2 Arquitectura física

El FEP01, Artículo 16.1, p. 11 exige una solución híbrida: la carga principal en nube pública y componentes
desplegados en las instalaciones u operaciones del mandante. Esta solución reparte sus componentes en
los tres planos de la Tabla 4.21. Cada componente lógico de la sección 4.1 queda en uno de ellos
por una razón que se declara en la sección 4.2.3.

**Tabla 4.21.** Los tres planos de emplazamiento

| Plano | Contenido | Por qué no puede estar en otro lugar |
|---|---|---|
| Nube | Núcleo transaccional, analítica, portales, ingesta e integración, en Azure Chile Central con recuperación en Brazil South | Elasticidad hacia 430 camiones y absorción del peak de reconexión |
| On-premise de sitio | Nodo de continuidad de la torre en San Bernardo y gabinetes en los cuatro terminales regionales | RT-06.01 del Caso exige gabinete por terminal y el Art. 16.4 pide operar al menos 24 horas sin enlace |
| On-premise distribuido | 182 equipos audIT a bordo, más la lectura de los equipos que ya tienen 192 camiones de terceros | La operación no puede depender de la cobertura móvil (restricción 4) |

*Fuente: FEP01, Artículo 16, pp. 11 y 12, y Caso, RT-06.01, p. 32, y capítulo 10, p. 23.*

El reparto de la flota sale del Caso, numeral 2.2, p. 6: 340 de los 374 camiones tienen dispositivo y
«34 camiones subcontratados no tienen ninguno». Entonces 226 menos 34 da 192 camiones de terceros con
equipo, y 340 menos 192 da 148 propios, todos equipados. Los 148 propios y los 34 de terceros sin
equipo llevan el equipo de audIT, 182 en total. Los 192 de terceros que ya tienen equipo lo conservan,
porque la restricción 3 impide intervenirlo sin acuerdo de su dueño (Caso, capítulo 10, p. 23), y sus
datos llegan por las plataformas de sus proveedores. La Figura 4.8 muestra los tres planos y
los enlaces que los unen.

![Figura 4.8. Vista general de la arquitectura física: nube primaria y secundaria, San Bernardo, terminales regionales y flota, con los enlaces y su capacidad](../../figuras/04-arquitectura/fisica-general.png)

*Figura 4.8. Vista general de la arquitectura física: nube primaria y secundaria, San Bernardo, terminales regionales y flota, con los enlaces y su capacidad*

Fuente: Elaboración propia.

La figura se lee de arriba hacia abajo. Arriba está la nube, con Azure Chile Central como región
primaria en tres zonas y Brazil South en espera. Al medio está San Bernardo, conectado a la red central
de Azure por ExpressRoute de 100 Mbit/s y por una VPN de respaldo a través de otro proveedor. A su
lado están los cuatro terminales regionales, cada uno con un enlace fijo de al menos 10 Mbit/s y un
router 5G de respaldo. Abajo está la flota: los 182 equipos audIT transmiten por la red celular y,
donde no hay señal, por la red satelital Iridium, mientras que los 192 equipos de terceros entregan su
posición a través de las plataformas de sus proveedores. Las secciones que siguen desarrollan cada
parte con su propio diagrama, como pide el Comunicado 10, sección 4.4.

### 4.2.1 Especificaciones Implementos a proveer (Hardware y Software)

El hardware lo adquiere el mandante, y audIT debe especificar exactamente qué comprar, cuánto y con
qué características (Caso, capítulo 11, p. 24). FEP02, RT-08.10, p. 19 pide para cada dispositivo marca,
modelo de referencia, cantidad, características mínimas y costo unitario estimado. El costo va en el
Sobre N.º 3, porque el FEP01, Artículo 50.2, p. 29 no admite en la Oferta Técnica cifras que permitan inferir el
monto. La Tabla 4.22 resume los implementos por sitio. El detalle, con características,
ubicación, ciclo de vida y justificación de cada uno, está en el Formulario T-11.

**Tabla 4.22.** Implementos que compra el mandante, por sitio

| Sitio | Implemento | Modelo de referencia | Cantidad |
|---|---|---|---|
| Cabina | Equipo a bordo | iWave G26I con eMMC de 8 GB | 182 + 19 |
| Cabina | Módem satelital | Iridium Edge | 182 + 19 |
| Cabina | Lector CAN sin contacto | Technoton CANCrocodile | 182 + 19 |
| Cabina | Lector de tarjeta | GAO RFID MIFARE DESFire | 182 + 19 |
| Conductores | Tarjeta de identificación | MIFARE DESFire | 572 |
| Semirremolques | Baliza Bluetooth | Teltonika EYE Sensor BTSMP1 | 210 + 21 |
| Terminales | Computador de terminal | OnLogic Karbon 430 | 8 |
| Terminales | Router 5G de respaldo | Teltonika RUTX50 | 4 |
| Terminales | Switch de gabinete | Teltonika TSW202 | 4 |
| Terminales | UPS de gabinete | APC SRT1000XLI | 4 |
| Cinco terminales | Punto de acceso de patio | Fortinet FortiAP 234G | 5 |
| Cinco terminales | Lector de portería | Minew G1 | 5 |
| San Bernardo | Servidor | Dell PowerEdge R360 | 2 |
| San Bernardo | Firewall | Fortinet FortiGate 90G | 2 |
| San Bernardo | Switch | Fortinet FortiSwitch 124F-POE | 2 |
| San Bernardo | UPS | APC SRT3000RMXLI con SRT96RMBP | 2 |
| San Bernardo | Clima de precisión | Vertiv Liebert Mini-Mate2 MMD12E | 2 |
| San Bernardo | Detección y extinción | VESDA VLF-250 y Kidde Fluoro-K | 1 y 1 |
| San Bernardo | Control de acceso | Suprema FaceStation F2 | 2 |
| San Bernardo | Videovigilancia | Axis M3215-LVE y grabador S3008 Mk II | 4 y 1 |
| San Bernardo | Detección de agua | Vertiv Liebert LT460 | 1 |
| San Bernardo | Grupo electrógeno | Himoinsa HYW-8 T5 S5 con estanque de 100 L | 1 |

*Fuente: elaboración propia. Detalle en el Formulario T-11 (AUDIT-Formulario-T-11.pdf). Los servicios de nube se declaran en la sección 4.2.4.*

Las cantidades salen de las poblaciones del Caso y no de la adhesión. El equipo a bordo y sus tres
periféricos se compran para 182 camiones, más 19 de reposición, que son el 10 % del parque
redondeado hacia arriba. Las 572 tarjetas cubren a los 520 conductores que el Caso, numeral 14.1, p. 29
proyecta a tres años, más el mismo 10 %. Las balizas cubren los 210 semirremolques propios más 21 de
reposición. El T-11 declara además, en filas aparte, los equipos que la flota suma a tres años según el
mismo numeral: 22 equipos a bordo para los camiones propios que pasan de 148 a 170, y 35 balizas para
los semirremolques que pasan de 210 a 245. Los 192 equipos de terceros no figuran porque no se
reemplazan.

**Estándar de homologación de los equipos de terceros.**  El Caso no pide reemplazar las
plataformas de posicionamiento instaladas en camiones de terceros, pero sí «especificar qué se
requeriría si hubiera que homologarlas» (Caso, capítulo 11, p. 24). La Tabla 4.23 fija ese
estándar mínimo. Contra él se clasifica cada equipo durante la Etapa 1, porque el Caso no entrega
marca, modelo ni capacidad de esos equipos y esta oferta no los supone.

**Tabla 4.23.** Estándar mínimo para homologar un equipo de terceros

| Exigencia | Valor mínimo | Fuente |
|---|---|---|
| Operación sin cobertura | 72 horas continuas sin pérdida de registros de posición y jornada | Caso, RT-03.10, p. 31 |
| Salida de datos | Interfaz programática con autenticación entre sistemas y sin clave estática en la dirección web | FEP02, RT-05.18, p. 12 |
| Frecuencia de posición | Cada 30 segundos en marcha y cada 5 minutos detenido | Supuestos de la sección 4.2.9 |
| Red móvil | LTE en las bandas que usan los operadores en Chile, sin depender de 2G ni de 3G | SUBTEL (2026) y Diario Financiero (2026) |
| Identificación del conductor | Sin manipular un dispositivo en marcha ni recordar una credencial | Caso, RT-12.11, p. 32 |
| Instalación | Sin cortar ni empalmar el arnés del vehículo | Restricción 6, Caso, p. 24 |

*Fuente: elaboración propia sobre las bases citadas y Subsecretaría de Telecomunicaciones (2026), Diario Financiero (s. f.).*

Las plataformas de los proveedores preexistentes de los 192 camiones subcontratados se integran mediante conectores y adaptadores API REST/Webhook hacia la capa de ingesta cloud de audIT SpA. Para aquellas unidades cuyo equipamiento preexistente no cumpla con los requisitos mínimos de almacenamiento desconectado de 72 horas (RT-03.10) o presente obsolescencia por el apagado de redes 2G/3G, el plan de adhesión del Subdocumento 3 contempla una opción de actualización tecnológica (retrofit) mediante la entrega en comodato de unidades audIT homologadas durante el paso normal por terminal, asegurando la cobertura integral de la flota sin fricción patrimonial para los transportistas.

### 4.2.2 Equipo a bordo y almacenamiento derivado

Caso, RT-06.01, p. 32 ordena tratar el dispositivo a bordo como un componente on-premise distribuido,
con su propio ciclo de vida, su mecanismo de actualización remota, su gestión de seguridad y su plan
de reposición, todo ello sujeto a que solo puede intervenirse físicamente cuando el camión pasa por un
terminal. El equipo elegido es el iWave G26I, un computador vehicular con Linux embebido, tres puertos
CAN con J1939, RS232 y RS485, red celular LTE Cat 4 o Cat M1, GNSS, Wi-Fi, Bluetooth 5.0 y el elemento
seguro Microchip TA100 para arranque seguro y almacenamiento de claves. Funciona de 9 a 32 V, de
−40 a +70 °C y con protección IP67 (iWave Global, 2026), lo que responde a la vibración, el polvo
y la temperatura de cabina que piden FEP02, RT-08.11, p. 19 y FEP02, RT-08.12, p. 19. La
Figura 4.9 muestra el equipo con sus periféricos.

![Figura 4.9. Equipo a bordo: iWave G26I, periféricos, interfaces y particiones de la memoria](../../figuras/04-arquitectura/equipo-a-bordo.png)

*Figura 4.9. Equipo a bordo: iWave G26I, periféricos, interfaces y particiones de la memoria*

Fuente: Elaboración propia.

Cada periférico de la figura responde a una restricción del Caso. El CANCrocodile lee el bus del camión
a través del aislamiento de los cables, sin cortarlos, y entrega la señal en CAN 2.0B según SAE J1939
(Technoton, 2026), con lo que se cumple la restricción 6 sobre la garantía del
vehículo (Caso, capítulo 10, p. 24). El lector de tarjetas MIFARE DESFire, IP66 y conectado por RS485
(GAO RFID, 2026), identifica al conductor cuando acerca su tarjeta con el camión detenido, como
pide Caso, RT-12.11, p. 32. El Iridium Edge, conectado por RS232, manda mensajes de hasta 340 bytes por
la red satelital (Ground Control, 2026) en los tramos de más de 80 km sin señal de la
restricción 4 (Caso, capítulo 10, p. 23). Es el mismo módem que Webfleet vende en Chile dentro de su
producto satelital (Webfleet, 2026), lo que hace factible su homologación local. Ese
producto guarda hasta 40 horas de registro y exige su propio rastreador, y por eso el módem se conecta
al G26I, que sí guarda 288 horas. El Wi-Fi del equipo solo se usa en el patio del terminal para las
actualizaciones, que se aplican en dos particiones de sistema para volver a la anterior si la nueva
falla (Northern.tech, 2026), y la restricción 5 queda cumplida porque nada se instala ni se
actualiza fuera de un terminal. El Bluetooth lee la baliza del semirremolque acoplado, que es la base
de la innovación tecnológica del Subdocumento 13.

La compra exige que el modelo cubra las bandas LTE que usan los operadores en Chile, de 700, 850,
1.700, 1.900 y 2.600 MHz (Subsecretaría de Telecomunicaciones, 2026), y que cuente con la homologación de SUBTEL. La ficha
del G26I declara certificaciones CE, FCC, ISED, PTCRB y AT&T, y no declara E-Mark ni SUBTEL, de modo
que ambas quedan como condición de compra. El equipo a bordo no emite documentos tributarios: la
restricción 8 deja al sistema contable como único emisor (Caso, capítulo 10, p. 24).

**Capacidad de almacenamiento.**  La observación 73 exige derivar la memoria sin ajustar el cálculo a los 8 GB del producto. Se distingue volumen serializado, sobrecarga física, reserva y particiones del sistema. El perfil de 72 h se calcula en sección 4.2.8; 288 h es ampliación propuesta por audIT, independiente de la duración del cierre fronterizo.

La carga serializada del perfil suma 3.237.656 bytes por 72 h; cuatro repeticiones suman 12.950.624 bytes. Se presupuesta otro tanto para índices, WAL, cifrado y metadatos, y otro tanto como reserva: 38.851.872 bytes. Son presupuestos de ingeniería, no ocupación medida ni compresión conseguida. Una partición de 64 MiB aporta 67.108.864 bytes y deja 28.256.992 bytes adicionales sobre ese presupuesto; HIL debe comprobar ocupación, reinicio e integridad del perfil completo. Si la sobrecarga real supera el presupuesto, se recalcula antes de homologar.

La Tabla 4.24 suma asignaciones físicas en MiB ($1 \mathrm{MiB}=1.048.576$ bytes); GB comercial se expresa en decimal. Así se evita sumar MB y MiB como si fueran equivalentes.

**Tabla 4.24.** Asignación de almacenamiento a bordo por componente

| Componente | Asignación | Base de diseño |
|---|---|---|
| Partición de arranque | 16 MiB | Gestor de actualización |
| Sistema A y sistema B | 2.048 MiB | Hasta 1 GiB por imagen |
| Búfer propuesto de 288 h | 64 MiB | 38.851.872 bytes presupuestados |
| Diagnóstico | 256 MiB | Tope rotativo independiente |
| Geocercas y maestros | 16 MiB | Catálogo y vigencias |
| Total asignado | 2.400 MiB | 2.516.582.400 bytes |

*Fuente: elaboración propia; mínimo de 72 h en Caso RT-03.10, p. 31. Hipótesis y reserva verificables mediante T-17.*

La asignación suma aproximadamente 2,52 GB decimales. Los 8 GB nominales del G26I (iWave Global, 2026) son una configuración de producto; la capacidad útil después de formateo y las reservas del controlador se verifican antes de compra. No se toma la capacidad nominal como toda la memoria disponible. El presupuesto contiene las dos imágenes y no se limita a los bytes de telemetría. La reserva para almacenamiento no demuestra vida útil de escritura: se contrastan escrituras, amplificación y resistencia del fabricante durante los 56 meses. Los plazos legales de conservación corresponden al repositorio central por dominio; el búfer local no reemplaza esos plazos.

### 4.2.3 Emplazamiento de componentes

El FEP01, Artículo 16.2, p. 11 obliga a justificar el emplazamiento componente por componente en función de
latencia, criticidad operacional, volumen de datos, restricciones regulatorias, disponibilidad de
conectividad y costo total de propiedad, y califica como observación grave una asignación no
justificada. La justificación de cada componente, con esos seis criterios, está en el Formulario T-11.
La Tabla 4.25 resume dónde queda cada uno.

**Tabla 4.25.** Reparto de los componentes por emplazamiento

| Código | Emplazamiento | Tipología | Componentes |
|---|---|---|---|
| N | Azure Chile Central, tres zonas | No aplica | 23 |
| N2 | Azure Brazil South, en espera | No aplica | 1 |
| SB | San Bernardo, sala de 26 m² | Sala técnica secundaria o de sitio | 4 |
| GT | Gabinete de cada terminal regional | Gabinete o borde operacional | 3 |
| DB | Equipo a bordo de 182 camiones | On-premise distribuido | 5 |
| SR | Baliza en 210 semirremolques | On-premise distribuido | 1 |
| BM | Teléfono del conductor | No aplica | 1 |

*Fuente: elaboración propia. Detalle por componente en el Formulario T-11.*

De 38 componentes, 23 quedan en la región primaria de nube, uno en la secundaria y 14 fuera de la
nube, repartidos entre San Bernardo, los gabinetes, los camiones, los semirremolques y el teléfono del
conductor. La propuesta cumple el FEP01, Artículo 16.1, p. 11, porque no es exclusivamente en nube ni
exclusivamente on-premise, y la parte on-premise sostiene las tres funciones que Caso, RT-21.06, p. 34
clasifica en severidad máxima cuando cae el enlace: asignar un viaje, emitir un documento de transporte
y recibir un evento de emergencia. El Informe 1 declaraba 18 componentes en nube y su tabla sumaba 20
(observación 71). La cuenta actual sale de la lista del T-11.

**Trazabilidad entre la arquitectura lógica y la física.**  El Comunicado 10, sección 11
recomienda una matriz que cruce cada componente con su lugar en el esquema de solución, en la
arquitectura lógica y en el nodo físico. La Tabla 4.26 la presenta para los componentes
críticos.

**Tabla 4.26.** Trazabilidad de los componentes críticos entre la sección 4.1 y el nodo físico

| Componente | Capa lógica (4.1) | Nodo físico (4.2) | T-11 |
|---|---|---|---|
| Despacho y asignación | Servicios de negocio | AKS en tres zonas de Chile Central, con copia local en el nodo de San Bernardo | N y SB |
| Personas y cumplimiento | Servicios de negocio | AKS en tres zonas de Chile Central | N |
| Bus de telemetría | Integración y eventos | IoT Hub S1 y Event Hubs Premium en la subred de integración | N |
| Motor transaccional | Datos | PostgreSQL Flexible con alta disponibilidad entre zonas | N |
| Series de tiempo | Datos | PostgreSQL Flexible con TimescaleDB, servidor propio | N |
| Almacenamiento inmutable | Datos | Almacenamiento con redundancia de zona e inmutabilidad | N |
| Capa anticorrupción | Integración y eventos | Pasarela en el nodo de San Bernardo, junto al sistema contable | SB |
| Nodo de terminal | Servicios de negocio | Dos Karbon 430 en activo y en espera | GT |
| Búfer a bordo | Datos, versión reducida | eMMC del iWave G26I | DB |
| Réplica de recuperación | Todas | Brazil South, en espera | N2 |

*Fuente: elaboración propia.*

La matriz muestra que las capas de servicios y de datos existen en tres lugares, nube, terminal y
camión, porque son las que deben seguir funcionando sin enlace.

### 4.2.4 Catálogo de servicios contratados en la nube

Todos los servicios del catálogo están disponibles en Chile Central y en Brazil South. Se verificó en
la interfaz pública de precios de Azure, que solo lista un servicio en una región cuando está
desplegado ahí (Microsoft, 2026). FEP02, RT-03.05, p. 8 y el FEP01, Artículo 16.3, p. 11 piden privilegiar
servicios administrados cuando reducen el riesgo operacional, y el catálogo los usa en todas las capas.
En este caso la preferencia tiene una razón concreta. El área de tecnología del mandante son nueve
personas para cinco terminales, dos talleres y una flota que no está en ningún lugar fijo
(Caso, capítulo 8, p. 20). Con servicios administrados, los parches, la alta disponibilidad y los
respaldos de la plataforma los opera el proveedor de nube, y en San Bernardo y los terminales quedan
solo los equipos que el FEP01, Artículo 16.4, p. 12 exige para operar sin enlace. La Tabla 4.27 declara
el nivel, la configuración y la subred de cada uno.

**Tabla 4.27.** Servicios de Azure en la región primaria, con nivel y configuración

| Servicio | Nivel y configuración | Subred |
|---|---|---|
| Front Door | Premium, con cortafuegos de aplicación y protección volumétrica | Global, borde |
| API Management | Premium, con unidades en las tres zonas | Borde |
| IoT Hub | S1 con 2 unidades: 800.000 mensajes de 4 KB al día | Integración |
| Device Provisioning Service | Enrolamiento con certificado X.509 del elemento seguro | Integración |
| Event Hubs | Premium, protocolo Kafka, réplica geográfica asíncrona a Brazil South | Integración |
| Kubernetes Service (AKS) | Nodos en las tres zonas, con escalado automático | Aplicación |
| PostgreSQL Flexible transaccional | Alta disponibilidad entre zonas y réplica de lectura en Brazil South | Datos |
| PostgreSQL Flexible de series | Servidor propio con TimescaleDB, réplica en Brazil South | Datos |
| Almacenamiento de objetos | Redundancia de zona, inmutabilidad para evidencia y documentos | Datos |
| Key Vault | Premium, claves en módulo criptográfico | Datos |
| Azure Firewall | Premium, en la red central | Red central |
| Puerta de ExpressRoute | ErGw1AZ, redundante entre zonas | Red central |
| Puerta de VPN | VpnGw1AZ, redundante entre zonas | Red central |
| Bastion | Acceso administrativo sin dirección pública | Red central |
| Monitor y Log Analytics | Registros de todos los ambientes, 12 meses en línea y 24 en archivo | Gestión |

*Fuente: elaboración propia sobre Microsoft (s. f.), Microsoft (s. f.) y Microsoft (s. f.).*

IoT Hub S1 con dos unidades admite 800.000 mensajes de 4 KB al día (Microsoft, s. f.), y la
sección 4.2.8 muestra que la operación normal con 430 camiones usa unos 330.000. La réplica asíncrona de
Event Hubs se configura con un retraso máximo, y el servicio frena la entrada si ese retraso se supera
(Microsoft, s. f.), lo que acota la pérdida de telemetría ante un desastre. La retención de
Monitor sigue el FEP01, Artículo 21.3, p. 15, que exige doce meses en línea y veinticuatro en archivo para los
eventos de seguridad. Las series de tiempo van en un servidor separado del transaccional, de modo que
el peak de escritura de la reconexión masiva no atrase la réplica de los datos del despacho.

La infraestructura se define como código, versionada en el repositorio del mandante, porque
FEP02, RT-03.03, p. 8 no admite infraestructura creada manualmente por consola. Todo recurso lleva
etiquetas de ambiente, centro de costo y responsable, con presupuestos y alertas de desviación, como
pide el FEP01, Artículo 16.3, p. 11. FEP02, RT-03.07, p. 8 exige declarar la estrategia de reversibilidad. Los
contenedores y el motor relacional son portables. Los servicios de ingesta, mensajería y analítica no lo
son sin reescritura, aunque Event Hubs expone el protocolo Kafka y eso reduce el esfuerzo de migrar el
bus.

### 4.2.5 Topología de red y segmentación

La red en Azure es de tipo central y radial. Una red central por región concentra el cortafuegos de
Azure y las puertas de ExpressRoute y de VPN. Cada ambiente tiene su propia red, conectada a la
central, con cinco subredes: borde, integración, aplicación, datos y gestión. Solo la subred de borde se
expone a Internet, y las de aplicación y datos son privadas, como exige el FEP01, Artículo 16.3, p. 11. Los servicios
administrados se alcanzan por puntos de conexión privados dentro de su subred. La Tabla 4.28
declara el plan de direcciones.

**Tabla 4.28.** Plan de direcciones de la red

| Red | Rango | Contenido |
|---|---|---|
| Central de Chile Central | 10.10.0.0/22 | Cortafuegos, puertas de ExpressRoute y VPN, Bastion |
| Producción | 10.11.0.0/20 | Borde, integración, aplicación, datos y gestión, una /24 cada una, salvo aplicación con /22 para los nodos de AKS |
| Preproducción | 10.12.0.0/20 | Misma división que producción |
| QA | 10.13.0.0/20 | Misma división, con menos nodos |
| Desarrollo | 10.14.0.0/20 | Misma división, con menos nodos |
| Central de Brazil South | 10.20.0.0/22 | Cortafuegos y puerta de VPN |
| Recuperación en Brazil South | 10.21.0.0/20 | Misma división que producción |
| San Bernardo | 172.16.0.0/22 | Servidores, gestión, videovigilancia y acceso, en redes virtuales locales separadas |
| Terminales regionales | 172.16.4.0/22 | Una /24 por terminal |

*Fuente: elaboración propia. Rangos privados que no se superponen entre sí.*

Los rangos no se superponen, de modo que cualquier sitio puede enrutar a cualquier red de Azure sin
traducción de direcciones. La Figura 4.10 muestra la región primaria con sus redes, subredes y
servicios.

![Figura 4.10. Región primaria Azure Chile Central: red central, red de producción, subredes, servicios con su nivel y conexiones con San Bernardo y los terminales](../../figuras/04-arquitectura/region-primaria.png)

*Figura 4.10. Región primaria Azure Chile Central: red central, red de producción, subredes, servicios con su nivel y conexiones con San Bernardo y los terminales*

Fuente: Elaboración propia.

Todo el tráfico entre redes pasa por el cortafuegos de la red central, y cada subred tiene su grupo de
seguridad con reglas de denegación por defecto. Los camiones entran por IoT Hub con certificado mutuo,
los portales por Front Door y la puerta de enlace, y San Bernardo y los terminales por la red central.
Ningún componente de datos es alcanzable desde Internet. La administración entra por Bastion, sin
dirección pública en las máquinas.

### 4.2.6 Ambientes, alta disponibilidad y respaldos

La solución tiene cinco ambientes y cada uno vive en su propia suscripción, como muestra la
Figura 4.11.

![Figura 4.11. Ambientes de la solución, cada uno en su suscripción, y promoción desde desarrollo hasta producción](../../figuras/04-arquitectura/ambientes.png)

*Figura 4.11. Ambientes de la solución, cada uno en su suscripción, y promoción desde desarrollo hasta producción*

Fuente: Elaboración propia.

Desarrollo y QA están en Chile Central con niveles de servicio menores y menos nodos. Preproducción
repite la arquitectura de producción a escala reducida, y ahí se ejecutan las pruebas de carga que
FEP02, RT-09.06, p. 21 fija en 1,5 veces el peak declarado. Producción corre en las tres zonas de Chile
Central. El ambiente de recuperación está en Brazil South, en espera, y se describe en la
sección 4.3.2. Los cinco se levantan desde el mismo código de infraestructura, de modo que el de
recuperación es idéntico a producción por construcción.

FEP02, RT-03.02, p. 8 exige al menos dos zonas para todo componente con requisito de alta
disponibilidad. En producción, AKS reparte sus nodos en tres zonas, PostgreSQL mantiene una copia en
espera en otra zona, el almacenamiento es de redundancia de zona y API Management tiene unidades en las
tres. En San Bernardo, los servidores, los firewalls y los switches van en pares, y en cada terminal los
dos Karbon 430 funcionan en activo y en espera.

Los respaldos siguen el esquema 3-2-1-1-0 de FEP02, RT-07.09, p. 18. Las tres copias son la base en
producción, su respaldo diario en Chile Central y la réplica en Brazil South. Los dos medios son el
motor de base de datos y el almacenamiento de objetos. La copia fuera de sitio es la de Brazil South.
La copia inmutable es el respaldo en almacenamiento con bloqueo de escritura por el período de
retención. Cero errores se verifica con una restauración de prueba mensual y con las dos conmutaciones
reales al año que pide FEP02, RT-07.07, p. 17. La custodia en medio físico de FEP02, RT-06.26, p. 16 se
cubre con esa copia inmutable fuera de sitio, que el mismo requisito admite como solución más segura y
eficiente, porque la sala de San Bernardo es de sitio y no aloja el núcleo.

### 4.2.7 Enlaces, puntos únicos de falla y conmutación

FEP02, RT-03.17, p. 9 exige que el enlace entre el sitio on-premise y la nube sea redundante, con
caminos físicos y proveedores distintos, y con tiempo de conmutación declarado. La Tabla 4.29
declara cada enlace.

**Tabla 4.29.** Enlaces de la solución

| Enlace | Medio principal | Capacidad | Respaldo | Conmutación |
|---|---|---|---|---|
| San Bernardo y Azure | ExpressRoute en Santiago | 100 Mbit/s | VPN por el segundo proveedor, con otra ruta física | Hasta 1 minuto |
| Terminal y Azure | Enlace fijo con VPN | 10 Mbit/s o más | Router 5G con dos SIM | Bajo 1 minuto |
| Camión y Azure | LTE | 13 a 16 MB al mes | Iridium, mensajes de hasta 340 bytes | Inmediata para eventos críticos |
| Terceros y Azure | Plataformas de dos proveedores | Según cada proveedor | Ninguno | No aplica |

*Fuente: elaboración propia sobre Microsoft (s. f.), Microsoft (2026) y Ground Control (2026).*

ExpressRoute tiene punto de conexión en Santiago, en EdgeConnex SCL, con Cirion Technologies, Equinix y
PitChile como proveedores (Microsoft, s. f.). Santiago no ofrece la modalidad Metro ni la Local
de ExpressRoute, así que la redundancia la da la VPN por el segundo proveedor que San Bernardo ya tiene
(Caso, capítulo 5, p. 13). Con detección bidireccional de fallas en el enlace privado, la caída se detecta
en menos de un segundo y la convergencia hacia la ruta de respaldo toma hasta un minuto
(Microsoft, 2026). La tabla de regiones de Microsoft asocia Santiago solo a Brazil South dentro de
Sudamérica, por lo que el proveedor debe confirmar que el circuito alcanza Chile Central con el nivel
Estándar. Los terminales conmutan en el propio RUTX50, que vigila el enlace fijo y pasa a la red 5G
(Teltonika Networks, 2026). Se configura con sondeos cada 10 segundos, de modo que la conmutación
ocurre en menos de un minuto. El enlace de los terceros no tiene respaldo porque depende de plataformas
que audIT no controla.

La cobertura móvil real de las rutas se caracteriza con mediciones en terreno, porque
Caso, RT-03.24, p. 31 declara que la disponibilidad informada por los operadores no es un antecedente
aceptable para el diseño. Esa campaña es una actividad de la Etapa 1 con costo y plazo, y produce dos
entregables con un solo recorrido: el mapa de sombras georreferenciado y el catálogo de lugares seguros
de detención que el criterio 28 necesita y que hoy nadie posee. La Tabla 4.30 recorre los puntos
únicos de falla de la infraestructura y cómo se cubre cada uno.

**Tabla 4.30.** Puntos únicos de falla de la infraestructura y su mitigación

| Punto de falla | Mitigación |
|---|---|
| Enlace de San Bernardo | VPN por otro proveedor y otra ruta física |
| Enlace de un terminal | Router 5G con dos SIM |
| Nodo de un terminal | Segundo Karbon 430 en espera |
| Servidor de San Bernardo | Segundo R360 en alta disponibilidad |
| Firewall o switch de San Bernardo | Segundo equipo del par, en otro circuito |
| UPS de San Bernardo | Segunda UPS en la alimentación B |
| Grupo electrógeno | 66 minutos de UPS y reabastecimiento desde el estanque propio |
| Clima de San Bernardo | Segunda unidad, N+1 |
| Zona de Azure | Servicios en las tres zonas de Chile Central |
| Región de Azure | Brazil South en espera (sección 4.3.2) |
| Cobertura celular | Búfer de 288 horas y mensajería Iridium |
| Equipo a bordo | Reposición del 10 % cambiada en el terminal |

*Fuente: elaboración propia.*

Ningún punto de la tabla deja la operación detenida por sí solo. Subsisten dos puntos únicos que se
declaran como exige RT-02.11: el grupo electrógeno, que es uno solo porque la sala es de sitio y la
redundancia de generación es deseable y no obligatoria (FEP02, RT-06.12, p. 15), y el equipo a bordo,
que solo se cambia cuando el camión pasa por un terminal, cada seis días en promedio
(Caso, capítulo 10, p. 23). Mientras tanto, el búfer guarda lo registrado.

FEP02, RT-08.04, p. 18 pide fuentes de poder redundantes conectadas a circuitos distintos. Los servidores
R360 tienen dos fuentes, una en cada alimentación, y el FortiGate 90G admite un segundo adaptador, que
se compra (Fortinet, 2026). El FortiSwitch 124F-POE y los equipos de gabinete tienen una sola
fuente, y en ellos la redundancia la da el par: cada equipo del par va en un circuito distinto.

### 4.2.8 Dimensionamiento y capacidad

El Caso, numeral 14.2, p. 30 exige estimar la volumetría del sistema y advierte que todo valor entregado
sin su derivación se evalúa como dimensionamiento no realizado. Advierte también que el problema de
esta operación es qué ocurre cuando trescientos camiones recuperan cobertura al mismo tiempo. La
estimación usa los supuestos de muestreo de la sección 4.2.9: posición cada 30 segundos en marcha y
cada 5 minutos detenido, telemetría del motor cada 60 segundos y 30 horas de marcha en 72 horas. La
Tabla 4.31 muestra lo que acumula un camión en 72 horas sin cobertura.

El perfil de ensayo es explícito y sintético: 30 h en marcha con posición cada 30 s y 42 h detenido cada 300 s producen 3.600+504=4.104 posiciones de 64 bytes; 30 h de motor cada 60 s producen 1.800 muestras de 160 bytes. Se propone un fixture de 45 eventos de jornada/conducción/esperas de 600 bytes, cinco documentos de 40.000 bytes y ocho fotos de 307.500 bytes. Los tamaños incluyen la serialización del fixture y se contrastan con firmware y documentos homologados; no son mediciones ni cantidades universales del caso. No se presupone compresión.

La Tabla 4.31 separa los componentes. Los eventos/documentos suman $45\times600+5\times40.000=227.000$ bytes; todo el lote sin fotos suma 777.656 bytes.

**Tabla 4.31.** Perfil sintético serializado de un camión tras 72 h

| Componente | Cantidad | Bytes |
|---|---|---|
| Posiciones | 4.104 | 262.656 |
| Motor | 1.800 | 288.000 |
| Eventos y documentos | 45 + 5 | 227.000 |
| Total sin fotos | 5.954 | 777.656 |
| Fotos adjuntas | 8 | 2.460.000 |
| Total de datos y fotos | Un lote | 3.237.656 |

*Fuente: hipótesis analíticas y fixture de audIT; frecuencias S-02/S-03 y variantes CP-PERF-02/CP-HW-03 de T-17.*

Trescientos camiones producen 1.786.200 registros y 971.296.800 bytes incluidos adjuntos. Dividir ese volumen por veinte minutos requiere 6,48 Mbit/s útiles agregados, antes de overhead. Como presupuesto adicional se incorpora 25 % de transporte/metadatos y se reserva 20 % de la ventana para reconexión, reintentos, persistencia y conciliación: $971.296.800\times1,25\times8/960=10,12$ Mbit/s. El porcentaje es una hipótesis declarada que se contrasta en pruebas; la garantía contractual solo se comprueba midiendo la confirmación íntegra de cada camión en hasta veinte minutos.

La Tabla 4.32 distingue tasas de operaciones y cuotas. Los bloques de 4 KiB son una elección de empaquetado del ensayo y unidad de cuota diaria, no el tamaño máximo de un mensaje ni la tasa de operaciones (Microsoft, s. f.).

**Tabla 4.32.** Reconexión de 300 camiones: estimación y límites

| Cálculo | Resultado | Alcance |
|---|---|---|
| Paquetes de 4 KiB sin fotos | 57.000 | 300 por $\lceil777.656/4.096\rceil$ |
| Con presupuesto de 25 % | 71.400 | 238 paquetes por camión |
| Envíos a 100 operaciones/s | 11,9 min | Límite de dos unidades S1 |
| Nuevas conexiones a 100/s | Al menos 3 s | Solo admisión, sin reintentos |
| Inicio de 300 archivos agrupados | Al menos 90 s | 100/min por unidad; dos unidades |

*Fuente: elaboración propia y documentación de Microsoft IoT Hub consultada el 7 de octubre de 2026.*

Estas estimaciones no prueban el tiempo final: admitir un archivo no lo transfiere, y aceptar un mensaje no confirma escritura ni conciliación. La transferencia de fotos comparte presupuesto de enlace; sus huellas deben compararse antes de cerrar el cronómetro. Colas, escritura, reintentos y carga normal se incluyen en CP-PERF-02. El ensayo aplica a cada camión y falla si uno excede veinte minutos o pierde registros; 288 h se ensaya separadamente como ampliación de ingeniería.

![Figura 4.12. Reconexión masiva: del búfer del camión a la base de datos, con los límites de cada tramo](../../figuras/04-arquitectura/reconexion.png)

*Figura 4.12. Reconexión masiva: del búfer del camión a la base de datos, con los límites de cada tramo*

Fuente: Elaboración propia.

La figura sigue los cinco tramos. Cada equipo espera un tiempo aleatorio antes de reconectarse y
reintenta con retroceso exponencial, de modo que los 300 no golpean la puerta en el mismo segundo. Del
IoT Hub los mensajes pasan a Event Hubs, que desacopla la llegada del procesamiento: los consumidores en
AKS escriben en lotes a la base de series a su propio ritmo, y el mensaje queda retenido en el bus
aunque la base se atrase. La admisión de ingesta es el cuello de botella previsto por el cálculo de cuotas;
el ensayo debe contrastarlo con transferencia de fotos, procesamiento y escritura.
La figura identifica profundidad de cola y conciliación como indicadores, sin declarar una saturación medida.

En operación normal cada camión manda 768 mensajes diarios, uno por minuto en marcha y uno cada cinco
minutos detenido. Con los 430 camiones proyectados son unos 330.000 mensajes diarios, más 71.400 paquetes presupuestados de una
reconexión, dentro de los 800.000 de las dos unidades. El resto de lo que pide el numeral 14.2 está en
la Tabla 4.33.

**Tabla 4.33.** Otras estimaciones del numeral 14.2

| Estimación | Valor | Cómo sale |
|---|---|---|
| Eventos por segundo, promedio | 8,5 | 374 camiones con 1.968 registros diarios cada uno |
| Eventos por segundo en la reconexión | Cerca de 3.000 | 300 camiones con 5.954 registros en 10 minutos |
| Transacciones por segundo en la asignación | Cerca de 1 | Cota con los 374 camiones asignados en una hora y 10 consultas por asignación |
| Datos móviles por camión | 13 a 16 MB al mes | Muestreo de 30 segundos con sobrecarga de protocolo |
| Datos móviles de los equipos audIT | 2,4 a 2,9 GB al mes | 182 equipos por el valor anterior |
| Ancho de banda por terminal | 10 Mbit/s | 12,5 visitas diarias con imagen de 1 GB |
| Ancho de banda de San Bernardo | 52 Mbit/s | 80 usuarios internos a 0,5 Mbit/s, más continuidad, por el crecimiento a 390 usuarios |

*Fuente: elaboración propia basada en la memoria de cálculo de ancho de banda y balance de cargas de San Bernardo.*

La carga fuerte de esta operación es la ingesta en la reconexión, unas 350 veces el promedio. La
asignación, que es la transacción crítica de Caso, RT-09.01, p. 32, pesa poco en volumen: los 96.000
viajes al año son 263 al día. El ancho de banda de los terminales lo fija la actualización del equipo a
bordo. Con 62 visitas diarias a terminal en toda la red, calculadas con la flota completa como cota,
12,5 por terminal, y una imagen de 1 GB, se necesitan 3,5 Mbit/s repartidos en 8 horas y unos 9 Mbit/s
si cuatro camiones se actualizan en la misma hora de relevo. El ancho de banda de San Bernardo lo fijan
los usuarios de la casa matriz y de la torre, y por eso el circuito ExpressRoute es de 100 Mbit/s, el
siguiente escalón comercial sobre 52 Mbit/s.

La observación 75 pidió además el volumen transaccional anual y el de la evidencia que se almacena. La
Tabla 4.34 los reúne.

**Tabla 4.34.** Volumen transaccional y de evidencia al año

| Transacción | Hoy | A tres años |
|---|---|---|
| Viajes | 96.000 | 118.000 |
| Documentos electrónicos de transporte | 128.000 | 157.000 |
| Abastecimientos de combustible | 74.000 | 90.000 |
| Pasadas de peaje | 620.000 | 760.000 |
| Órdenes de trabajo de taller | 5.200 | 6.100 |
| Liquidaciones a transportistas | 1.776 | 2.100 |
| Evidencia en almacenamiento inmutable | Cerca de 59 GB | Cerca de 67 GB |

*Fuente: Caso, numeral 14.1, p. 29. Liquidaciones: 148 y 175 al mes por 12. Evidencia: documentos de transporte a 40 KB (5,1 GB hoy) más 2,46 MB de fotos cada 72 horas por equipo audIT (54 GB con 182 equipos y 61 GB con 204).*

La evidencia se retiene cinco años para la jornada y seis para los documentos de transporte
(Caso, RT-05.10, p. 31), de modo que en los 56 meses del contrato se acumulan cerca de 290 GB, con lo que el
almacenamiento inmutable no condiciona el diseño. Los umbrales del numeral 9.1 transversal son exigibles
en producción medidos en el percentil 95 sobre la experiencia real de la persona usuaria, y en cada
fila prevalece el umbral más exigente entre ese numeral y el Caso. FEP02, RT-09.03, p. 21 obliga a
soportar sin rediseño un crecimiento de tres veces la volumetría inicial, y la proyección del Caso llega
a 1,2 veces, de modo que esta oferta dimensiona sobre el requisito transversal. FEP02, RT-09.05, p. 21
pide identificar el primer cuello de botella. El modelo propone la admisión de ingesta durante
la reconexión masiva como limitación inicial; CP-PERF-02 debe verificarlo frente al enlace,
las fotos y la persistencia, midiendo profundidad de cola y retraso de procesamiento.
La ampliación de unidades de IoT Hub y de procesamiento se evalúa según el tramo medido, sin presuponer que elimine otro cuello de botella. La disponibilidad comprometida es de 99,9 % mensual para los servicios
críticos, medida sobre la transacción de negocio de extremo a extremo (FEP01, Artículo 20, p. 14).

### 4.2.9 Supuestos declarados y brechas

El Caso, numeral 14.2, p. 30 advierte que todo valor entregado sin su derivación se evalúa como
dimensionamiento no realizado. Los supuestos que sostienen las cifras de esta sección se declaran en la
Tabla 4.35 con la forma en que se cierran.

**Tabla 4.35.** Supuestos de audIT con su valor y su cierre

| ID | Supuesto | Valor | Cómo se cierra |
|---|---|---|---|
| S-01 | Velocidad comercial media | 55 km/h | Medición en la Etapa 1 |
| S-02 | Horas de marcha dentro de 72 horas | 30 horas | Régimen de descansos del artículo 25 bis |
| S-03 | Tamaño del registro de posición | 64 bytes | Ajuste con el firmware del G26I |
| S-04 | Volumen acumulado a bordo tras 72 horas | 0,78 MB sin fotos y 2,46 MB de fotos | Derivado en la sección 4.2.8 |
| S-05 | Capacidad de almacenamiento a bordo | 2,52 GB asignados sobre 8 GB nominales | Derivada en la sección 4.2.2 |
| S-06 | Consumo mensual de datos por camión | 13 a 16 MB | Campaña de medición |
| S-07 | Imagen de actualización del equipo a bordo | 1 GB | Medición con el primer firmware |
| S-08 | Población con módem satelital | Los 182 equipos audIT | Decisión de diseño, no depende de la medición |
| S-09 | Parque telemático de los 192 camiones de terceros | Marca y modelo desconocidos | Clasificación contra el estándar de la sección 4.2.1 |
| S-10 | Consumo de cada servidor de San Bernardo | 300 W | Herramienta de planificación del fabricante |
| S-11 | Coeficiente del clima de precisión | 3,27 | Ficha del equipo a 50 Hz al comprar |
| S-12 | Tipología del recinto de San Bernardo | Sala técnica de sitio | Consulta al mandante |
| S-13 | Concurrencia simultánea en hora punta | 380 sesiones | Prueba de carga de RT-09.06 |
| S-14 | Registros de posición al año | Cerca de 120 millones | Derivada de S-01 y del muestreo |
| S-15 | Volumen almacenado de series | 30 a 40 GB al año | Modelo de datos del Subdocumento 5 |
| S-16 | Tráfico por usuario interno | 0,5 Mbit/s | Medición en la Etapa 1 |
| S-17 | Ventana de disponibilidad de las plataformas de terceros y de la autoridad tributaria | No declarada por las bases | Consulta al mandante |
| S-18 | Suscripción de Azure | A nombre del mandante | Reversibilidad de RT-03.07 |

*Fuente: elaboración propia. S-01 a S-17 vienen del Informe 1 y se actualizaron con las decisiones de esta instancia.*

Cada supuesto tiene un mecanismo de cierre en la Etapa 1 o en la compra. Ninguno fija un valor que las
bases entreguen de otra forma.

Esta oferta reconoce cinco brechas que la ingeniería no cierra por sí sola.
- La cobertura móvil no se supone. El Caso declara que la disponibilidad informada por los
operadores no es un antecedente aceptable para el diseño, y cualquier cifra sobre la calidad de la
señal en cada tramo antes de la medición en terreno sería una invención.
- El parque telemático de los 192 camiones de terceros tampoco se supone. El Caso no entrega marca,
modelo, protocolo ni capacidad de almacenamiento de esos equipos. El entregable correcto es el
estándar mínimo de homologación de la sección 4.2.1, y el levantamiento es una actividad de la Etapa 1
con costo, plazo y dependencia de terceros.
- El conductor que manejó otro camión sin dispositivo no deja rastro instrumental. Esa brecha se
cierra con responsabilidad contractual.
- Las consultas del Artículo 43 están enviadas y no respondidas. Las interpretaciones que esta
oferta adopta sobre la sustitución de los módulos operativos de 2013, la autorización de los
fabricantes para leer la telemetría, el mecanismo digital de la red de estaciones de servicio y el
alcance del costo consolidado en 24 horas son propuestas de audIT, no respuestas del mandante.
- El producto satelital evaluado en el Informe 1 guarda 40 horas de registro (Webfleet, 2026),
frente a las 72 exigidas. Por eso esta oferta integra el mismo módem al G26I, que guarda 288 horas.

## 4.3 Data center

La solución usa dos regiones de Azure y dos tipos de sitio propio del mandante. El FEP02, numeral
6.1, p. 14 obliga a declarar la tipología de cada sitio, advierte que sobredimensionar se castiga igual
que quedarse corto y fija para el recinto una disponibilidad de infraestructura de 99,95 %. La
Tabla 4.36 declara la tipología de cada sitio.

**Tabla 4.36.** Tipología declarada por sitio

| Sitio | Tipología | Fundamento |
|---|---|---|
| San Bernardo, 26 m² | Sala técnica secundaria o de sitio | Continuidad de la torre, no aloja el núcleo |
| Cuatro terminales regionales | Gabinete o borde operacional | Caso, RT-06.01, p. 32 |
| 182 camiones con equipo audIT | On-premise distribuido | Caso, RT-06.01, p. 32 |

*Fuente: FEP02, numeral 6.1, p. 14, y Caso, RT-06.01, p. 32.*

San Bernardo no aloja el núcleo, que está en la nube. Aloja lo que mantiene viva la operación cuando
cae el enlace, y por eso es una sala de sitio. A esa tipología el numeral 6.1 le aplica los requisitos
de energía, climatización, control de acceso, detección de incendio y monitoreo, dimensionados al sitio.

Las bases fijan dos plazos distintos para operar sin enlace. Caso, RT-03.10, p. 31 pide que los
terminales operen 12 horas sin enlace hacia el exterior, y el FEP01, Artículo 16.4, p. 12 exige que el componente
on-premise opere de forma autónoma degradada al menos 24 horas continuas, «en ningún caso inferior». Esta
oferta diseña San Bernardo y los terminales para 24 horas, que cumple ambos textos, y deja la diferencia
declarada para que el mandante la aclare.

### 4.3.1 Especificaciones Data Center Primaria

La región primaria es Azure Chile Central, en Santiago, con tres zonas de disponibilidad
(Microsoft, s. f.). El proveedor cumple FEP02, RT-03.01, p. 8, que exige región en Chile o en
Sudamérica, y los componentes con alta disponibilidad se reparten en las tres zonas, como pide
FEP02, RT-03.02, p. 8. La residencia de los datos queda en el país y sujeta a la aprobación del mandante,
como dispone el FEP01, Artículo 23, p. 17. Chile Central no tiene región pareja (Microsoft, s. f.). Eso importa
para la recuperación: los servicios que Azure replica solos hacia la región pareja no tienen adónde
replicar, y la copia a Brazil South se diseña servicio por servicio en la sección 4.3.2.

La infraestructura on-premise asociada está en la sala de San Bernardo, que es casa matriz, sede de la
torre 24x7 y terminal principal (Caso, capítulo 3, p. 8). Hoy la sala mide 26 m², se habilitó en 2013,
tiene climatización split, 20 minutos de alimentación ininterrumpida y acceso por credencial, y el Caso
declara que no cumple el capítulo 6 de las Transversales (Caso, capítulo 5, p. 13). La
Tabla 4.37 compara cada exigencia con lo que hay y con lo que se instala.

**Tabla 4.37.** Habilitación de la sala de San Bernardo

| Ámbito | Exigencia | Hoy | Solución | Fuente |
|---|---|---|---|---|
| Energía | UPS de 30 minutos a plena carga | 20 minutos | Dos APC SRT3000 en alimentación A y B con batería externa | RT-06.07 |
| Energía | Generación de 24 horas con estanque y contrato | No existe | Himoinsa HYW-8 T5 S5 con estanque de 100 L | RT-06.08 |
| Energía | Instalación propia y puesta a tierra según NCh Elec. 2777 | Por verificar | Tablero propio con transferencia automática | RT-06.09 |
| Energía | Carga, factor de potencia y PUE declarados | No declarados | 1,94 kW, factor 0,95 y PUE de 1,95 | RT-06.11 |
| Clima | Precisión en N+1 | Split | Dos Liebert Mini-Mate2 de 3,55 kW | RT-06.13 |
| Clima | Temperatura, humedad y agua en línea | No existe | Controlador del clima y Liebert LT460 | RT-06.14 |
| Incendio | Detección por aspiración láser | No existe | VESDA VLF-250 | RT-06.16 |
| Incendio | Extinción con agente limpio aprobado por UL | No existe | Kidde Fluoro-K, FK-5-1-12 | RT-06.17 |
| Acceso | Biometría facial con AFIS de respaldo | Credencial | Dos Suprema FaceStation F2 en esclusa | RT-06.20 |
| Acceso | Videovigilancia de 30 días | No existe | Cuatro cámaras Axis y grabador de 4 TB | RT-06.24 |
| Redes | Rutas físicas distintas | Dos proveedores | ExpressRoute y VPN por ductos separados | RT-06.32 |

*Fuente: FEP02, capítulo 6, pp. 14 a 17, y Caso, capítulo 5, p. 13.*

La brecha está en energía, clima, incendio y acceso, que son los ámbitos que el numeral 6.1 exige para
una sala de sitio. El agente de extinción es el FK-5-1-12. El Informe 1 proponía el Novec 1230, que es
ese mismo compuesto, pero 3M dejó de fabricarlo a fines de 2025 (Fike, 2025). Kidde lo
ofrece como Fluoro-K, con aprobación UL y FM (Kidde Fire Systems, 2026), lo que cumple
FEP02, RT-06.17, p. 15. La detección y la extinción se integran al monitoreo, que avisa al centro de
operación y a la contraparte del mandante (FEP02, RT-06.19, p. 16), y la sala suma dos extintores
portátiles de dióxido de carbono (FEP02, RT-06.18, p. 15).

**Balance eléctrico y térmico.**  FEP02, RT-06.11, p. 15 pide declarar la carga proyectada en kW,
el factor de potencia y el PUE. La Tabla 4.38 suma la carga con los consumos de ficha de cada
equipo y los supuestos declarados.

**Tabla 4.38.** Balance eléctrico de la sala de San Bernardo

| Concepto | W | Base |
|---|---|---|
| Dos servidores Dell R360 | 600 | 300 W cada uno, supuesto S-10 |
| Dos firewalls FortiGate 90G | 40 | 19,9 W cada uno, ficha del fabricante |
| Dos switches FortiSwitch 124F-POE | 105 | 237,4 W máximo menos 185 W de PoE, ficha |
| Cuatro cámaras de videovigilancia | 52 | 12,95 W de la clase 3 de PoE cada una |
| Acceso, grabador, detección y sensores | 150 | Supuesto de diseño |
| Equipos de los dos proveedores de enlace | 50 | 25 W cada uno, supuesto de diseño |
| Carga de TI | 996 | Suma de las filas anteriores |
| Pérdidas de las dos UPS | 100 | 7,6 % a plena carga según la ficha |
| Iluminación | 208 | 8 W/m² en 26 m² |
| Clima, una unidad en servicio | 640 | 1,6 kW de calor con COP 3,27, más 149 W de ventilador |
| Carga total | 1.944 | PUE de 1,95 |

*Fuente: Fortinet (2026), Fortinet (2026), Schneider Electric (2023), Stulz (2024), Vertiv (2026). Memoria de cálculo térmico y eléctrico según estándares ASHRAE TC 9.9 y TIA-942.*

La carga de TI es de cerca de 1 kW y la total de 1,94 kW, con un PUE estimado de 1,95. El PUE es alto
porque en una sala de 26 m² el clima y la iluminación pesan mucho frente a una carga de TI chica. El
calor a retirar, 1,6 kW, cabe en una sola unidad de 3,55 kW, y la segunda queda en reserva para cumplir
el N+1 de FEP02, RT-06.13, p. 15. El coeficiente de 3,27 sale de la ficha de una unidad de precisión de
Stulz, 6,6 kW de capacidad con 2.020 W de compresor (Stulz, 2024), y se reemplaza por el del
equipo comprado. El factor de potencia de diseño es 0,95, porque los servidores y las UPS de doble
conversión corrigen el factor en su entrada, y se mide en la revisión semestral de
FEP02, RT-06.10, p. 15.

La UPS se dimensiona con la carga de TI. Cada APC SRT3000 tiene 505 VAh internos, y con una batería
externa llega a 1.515 VAh (Schneider Electric, 2023). Con un rendimiento del inversor de 0,9 y la batería al
80 % de su capacidad al final de su vida, una sola UPS sostiene toda la carga de TI durante 66 minutos
(1.515 × 0,9 × 0,8 / 996 W), el doble de los 30 que pide FEP02, RT-06.07, p. 15. Sin la batería externa
serían 22 minutos, y por eso se compra.

El grupo electrógeno toma la carga total más la recarga de las dos UPS, 168 W cada una: 2,28 kW, o
2,85 kVA a factor 0,8. El Himoinsa HYW-8 T5 S5 entrega 8,8 kVA y queda al 32 % (Himoinsa, 2026).
Un grupo de 15 kVA quedaría bajo el 30 %, carga con la que un motor diésel acumula combustible sin
quemar. A plena carga consume 2,68 litros por hora, 64,3 litros en 24 horas, y el estanque opcional de
100 litros cumple las 24 horas de FEP02, RT-06.08, p. 15 con margen. El reabastecimiento se hace desde el
estanque de combustible propio que la compañía tiene en San Bernardo (Caso, numeral 2.2, p. 6), con un
contrato de respaldo con el proveedor de combustible.

La videovigilancia guarda 30 días en línea, como pide FEP02, RT-06.24, p. 16. Cuatro cámaras Axis
M3215-LVE a 2 Mbit/s en H.265 generan 2,59 TB en 30 días, y el grabador Axis S3008 Mk II de 4 TB los
cubre (Axis Communications, 2026; Axis Communications, 2026). Las grabaciones anteriores se copian al almacenamiento inmutable
de Azure, lo que suma 8 Mbit/s al enlace de San Bernardo, dentro de su capacidad de 100 Mbit/s.

**Plano de la sala.**  FEP02, RT-06.03, p. 14 pide el plano de distribución con las zonas de
generadores, baterías, climatización, servidores, comunicaciones, trabajo y respaldo. El numeral 6.1 lo
exige a la sala principal, y esta oferta lo entrega igual porque la revisión del Informe 1 lo pidió. La
Figura 4.13 lo muestra sobre una planta supuesta de 6,5 por 4 metros, que suma los 26 m²
del Caso.

![Figura 4.13. Plano de la sala de San Bernardo con sus zonas, a proporción de 26 m²](../../figuras/04-arquitectura/sala-san-bernardo.png)

*Figura 4.13. Plano de la sala de San Bernardo con sus zonas, a proporción de 26 m²*

Fuente: Elaboración propia.

Se entra por una esclusa con dos lectores biométricos, uno en cada puerta, que no deja pasar a más de
una persona a la vez (FEP02, RT-06.23, p. 16). El rack de servidores y el de comunicaciones van separados,
como pide FEP02, RT-06.05, p. 15, y cada uno es de 24 unidades. El de servidores ocupa cerca de 12
unidades con los dos R360, las dos UPS y sus baterías externas, y el de comunicaciones cerca de 8 con
los firewalls, los switches, los paneles de conexión y los equipos de los proveedores, de modo que ambos
quedan con la mitad o más libre para crecer. Las dos unidades de clima van en muros opuestos, el cilindro
de FK-5-1-12 junto a la esclusa, el puesto de trabajo con la consola en la zona de trabajo y los
repuestos de sala en la zona de respaldo. El grupo electrógeno y su tablero de transferencia quedan en
el patio, fuera de la sala, y los dos enlaces entran por ductos separados, como pide
FEP02, RT-06.32, p. 17. Las medidas de detalle se confirman en el levantamiento de la Etapa 1, porque el
Caso solo entrega la superficie.

**Gabinetes de los terminales regionales.**  Cada terminal regional lleva el gabinete de la
Figura 4.14.

![Figura 4.14. Gabinete de un terminal regional, con sus enlaces, el punto de acceso de patio y el lector de portería](../../figuras/04-arquitectura/gabinete-terminal.png)

*Figura 4.14. Gabinete de un terminal regional, con sus enlaces, el punto de acceso de patio y el lector de portería*

Fuente: Elaboración propia.

Dentro del gabinete van dos OnLogic Karbon 430 en activo y en espera, que funcionan sin ventilador de
−40 a +70 °C con alimentación de 9 a 48 V y consumen cerca de 35 W cada uno (OnLogic, 2026).
Con dos equipos el terminal no queda con un punto único de falla. El router Teltonika RUTX50, 5G con dos
SIM y conmutación automática, opera de −40 a +75 °C y consume menos de 18 W
(Teltonika Networks, 2026). El switch Teltonika TSW202, de riel DIN y con PoE, conecta los equipos
(Teltonika Networks, 2026). Fuera del gabinete, el FortiAP 234G, IP67 y de −50 a +70 °C, cubre el
patio con Wi-Fi para actualizar los camiones (Fortinet, 2026), y el Minew G1 lee en la portería
las balizas de los semirremolques (Minew, 2023). El gabinete suma 152 W, y la UPS APC SRT1000XLI,
con 293 VAh (Schneider Electric, 2024), lo sostiene 83 minutos al final de la vida de su batería. Sin enlace,
el terminal sigue registrando salidas y llegadas, verifica la aptitud contra la copia local de vigencias
y jornada, y actualiza los camiones con la imagen que guarda, durante las 24 horas que fija el
FEP01, Artículo 16.4, p. 12.

El monitoreo de San Bernardo y de los terminales se integra a la misma plataforma de observabilidad que
la nube, con alertas unificadas, como pide FEP02, RT-03.16, p. 9.

### 4.3.2 Especificaciones Data Center Secundario

La región secundaria corresponde a Azure Brazil South (São Paulo), provista con tres zonas
de disponibilidad (Microsoft, s. f.). Santiago y São Paulo están a unos 2.586 km en línea recta, en
otro país, con otro sistema eléctrico y lejos de la zona de subducción que concentra los grandes
sismos de Chile, lo que responde a FEP02, RT-07.02, p. 17. San Bernardo, en la misma área metropolitana
que la región primaria, no puede ser el sitio de recuperación porque comparte con ella el riesgo
sísmico y la red eléctrica. Microsoft no publica la latencia entre las dos regiones
(Microsoft, s. f.). El mínimo físico de ida y vuelta por fibra es de unos 26 ms (2.586 km × 2 /
200.000 km/s), y la latencia real se mide en la Etapa 1.

La modalidad es activo-pasivo, como permite FEP02, RT-07.01, p. 17. Una copia activa en Brazil South
duplicaría el costo de operación para mejorar un RTO que el activo-pasivo ya cumple, y agregaría la
complejidad de escribir en dos regiones a la vez. Brazil South queda en espera con réplicas asíncronas y
se promueve ante un desastre. Los objetivos son los de FEP02, RT-07.04, p. 17: 4 horas para recuperar el
servicio y no más de 15 minutos de datos perdidos. La Tabla 4.39 declara cómo se copia cada
servicio.

**Tabla 4.39.** Cómo llega cada servicio a Brazil South

| Servicio | Mecanismo | Redundancia allí | Efecto en el RPO |
|---|---|---|---|
| PostgreSQL transaccional | Réplica de lectura asíncrona que se promueve a primaria | Local o de zona | Retraso de segundos a minutos, con alerta bajo 15 minutos |
| PostgreSQL de series | Réplica de lectura asíncrona propia | Local o de zona | El peak de la reconexión no atrasa la transaccional |
| Event Hubs | Réplica geográfica asíncrona con retraso máximo de 10 minutos | Premium | Pérdida acotada a 10 minutos, que el búfer a bordo repone |
| Almacenamiento de objetos | Replicación de objetos a una cuenta de Brazil South | Local o de zona | Documentos copiados en minutos |
| AKS y servicios | Mismo código de infraestructura, clúster en espera | Tres zonas | Afecta el RTO, no el RPO |
| Key Vault | Bóveda propia con las claves respaldadas | Del servicio | Afecta el RTO, no el RPO |

*Fuente: elaboración propia sobre Microsoft (s. f.), Microsoft (s. f.) y Microsoft (s. f.).*

Ninguna copia en Brazil South usa redundancia geográfica. La pareja de Brazil South es South Central US,
en Texas (Microsoft, s. f.), y una redundancia geográfica llevaría los datos fuera de Sudamérica.
Microsoft advierte que el retraso de una réplica asíncrona de PostgreSQL suele ser de segundos a minutos
y puede llegar a horas con escritura intensa (Microsoft, s. f.). Por eso la telemetría tiene tres
defensas. Va a un servidor propio, de modo que su peak no atrasa la réplica transaccional. Pasa antes por
Event Hubs, cuya réplica frena la entrada si el retraso supera los 10 minutos (Microsoft, s. f.). Y
el equipo a bordo conserva lo enviado durante 72 horas, así que tras una conmutación reenvía el tramo que
la réplica pudo no alcanzar, y la clave de idempotencia de siete días descarta los duplicados.

La Figura 4.15 muestra la recuperación entre regiones y el eje separado de continuidad.

![Figura 4.15. Recuperación ante desastres entre Chile Central y Brazil South, y eje separado de continuidad en San Bernardo, los terminales y los camiones](../../figuras/04-arquitectura/recuperacion.png)

*Figura 4.15. Recuperación ante desastres entre Chile Central y Brazil South, y eje separado de continuidad en San Bernardo, los terminales y los camiones*

Fuente: Elaboración propia.

La conmutación sigue los cuatro pasos de la parte superior de la figura. El monitoreo detecta la caída y
alerta con un criterio declarado: la región primaria no responde durante 15 minutos, el plazo que
Microsoft sugiere como referencia para promover una región secundaria (Microsoft, s. f.). La guardia
confirma que es un desastre y no una falla pasajera. Un procedimiento automatizado promueve las
réplicas y despliega los servicios en Brazil South. La operación pasa a la región secundaria. La
confirmación humana protege contra una conmutación innecesaria, como valora FEP02, RT-07.08, p. 17, y el
procedimiento queda documentado y automatizado como exige FEP02, RT-07.05, p. 17. La vuelta a Chile
Central sigue un procedimiento igual, con conciliación de lo generado durante la contingencia
(FEP02, RT-07.06, p. 17), y la conmutación se prueba de verdad dos veces al año
(FEP02, RT-07.07, p. 17).

La parte inferior de la figura es el otro eje. La recuperación y la continuidad son ejes separados:
Brazil South recupera la nube si cae la región primaria, y San Bernardo, los terminales y los camiones
mantienen la operación cuando lo que cae es el enlace con la nube. La Tabla 4.40 los separa.

**Tabla 4.40.** Los dos ejes de continuidad

| Eje | Primario y secundario | Fundamento |
|---|---|---|
| Recuperación ante desastres | Azure Chile Central y Azure Brazil South | Distancia que evita compartir el evento (RT-07.02), con RTO de 4 horas y RPO de 15 minutos (RT-07.04) |
| Continuidad operacional | Nube, San Bernardo, terminales y camiones | RT-21.06 del Caso clasifica en severidad máxima todo incidente que impida asignar un viaje, emitir un documento de transporte o recibir un evento de emergencia |

*Fuente: FEP02, RT-07.02 y RT-07.04, p. 17, y Caso, RT-21.06, p. 34.*

FEP02, RT-03.13, p. 9 obliga a declarar qué funciones no estarán disponibles sin enlace y qué
procedimiento manual las suple, y evalúa como observación grave la ausencia de esta declaración. El
mismo código en el Caso regula otra materia, la sincronización en 20 minutos tras la reconexión, que la
sección 4.2.8 dimensiona. La Tabla 4.41 declara las funciones.

**Tabla 4.41.** Disponibilidad de funciones sin enlace y procedimiento supletorio

| Función | Sin enlace | Procedimiento supletorio |
|---|---|---|
| Registro de posición, jornada y eventos | Disponible | No aplica |
| Evaluación de geocerca de llegada y salida | Disponible | No aplica |
| Alerta de jornada próxima a agotarse | Disponible | No aplica |
| Botón de emergencia | Disponible por satélite en los 182 equipos audIT | Protocolo telefónico con la torre para los camiones de terceros |
| Asignación de un viaje no precargado | No disponible | Autorización de la torre, registrada y reconciliada al recuperar enlace |
| Verificación bloqueante con dato fresco | Parcial, contra copia local | Regla de excepción con rol nominado y registro auditable |
| Consulta de liquidación por el transportista | No disponible | Portal, al recuperar enlace |
| Notificación en tiempo real al cliente | No disponible | Aviso diferido |
| Actualización del equipo a bordo | Solo en terminal | Con la imagen que guarda el gabinete |

*Fuente: elaboración propia sobre FEP02, RT-03.13, p. 9.*

La emisión del documento electrónico de transporte sin cobertura no está en la tabla porque su mecanismo
lo define la sección 4.1, con el sistema contable como único emisor.

Los formularios de este subdocumento van en archivo propio: Formulario T-11 (`AUDIT-Formulario-T-11.pdf`).

## Referencias

Axis Communications. (2026). *AXIS M3215-LVE dome camera. Datasheet*. https://www.axis.com/products/axis-m3215-lve

Axis Communications. (2026). *AXIS S3008 Mk II recorder. Datasheet*. https://www.axis.com/products/axis-s3008-mk-ii

Diario Financiero. (2026, 2 de febrero). *¿Fin del 3G? La nueva estrategia de Entel para el uso eficiente de su espectro pone en alerta a las empresas de GPS*. https://www.df.cl/empresas/telecom-tecnologia/fin-del-3g-la-nueva-estrategia-de-entel-para-el-uso-eficiente-de-su

Fike. (2025). *3M Novec 1230 discontinued: what now?*. https://www.fike.com/knowledge-center/3m-novec-1230-discontinued-what-now/

Fortinet. (2026). *FortiAP series data sheet*. https://www.fortinet.com/resources/data-sheets/fortiap-series

Fortinet. (2026). *FortiGate 90G series data sheet*. https://www.fortinet.com/resources/data-sheets/fortigate-90g-series

Fortinet. (2026). *FortiSwitch 124F-POE data sheet*. https://www.router-switch.com/pdf/ft-fs-124f-poe-datasheet.pdf

GAO RFID. (2026). *13.56 MHz MIFARE DESFire RFID reader*. https://gaorfid.com/product/reader-mifare-desfire-13-56-mhz-rfid/

Ground Control. (2026). *Iridium Edge satellite IoT terminal*. https://www.groundcontrol.com/product/iridium-edge-9602-satellite-modem/

Himoinsa. (2026). *Grupo electrógeno diésel HYW-8 T5 S5 insonorizado, 8,8 kVA*. https://www.himoinsa.com/esp/generadores-electricos/15843/grupo-electrogeno--8,8kva--insonorizado.html

ISO. (2022). *ISO/IEC/IEEE 42010. Systems and software engineering. Architecture description*.

iWave Global. (2026). *Rugged telematics device G26I*. https://iwave-global.com/product/rugged-telematics-device/

Kidde Fire Systems. (2026). *Fluoro-K clean agent fire suppression*. https://kiddefenwal.com/solutions/engineered-fire-suppression/clean-agent-systems-land/fluoro-k/

Microsoft. (2026). *Azure Retail Prices REST API*. https://prices.azure.com/api/retail/prices

Microsoft. (2026). *Configure BFD over ExpressRoute*. Microsoft Learn. https://learn.microsoft.com/en-us/azure/expressroute/expressroute-bfd

Microsoft. (2026, 10 de julio). *Azure Event Hubs geo-replication*. Microsoft Learn. https://learn.microsoft.com/en-us/azure/event-hubs/geo-replication

Microsoft. (2026, 16 de julio). *Read replicas in Azure Database for PostgreSQL flexible server*. Microsoft Learn. https://learn.microsoft.com/en-us/azure/postgresql/read-replica/concepts-read-replicas

Microsoft. (2026, 16 de septiembre). *Locations and connectivity providers for Azure ExpressRoute*. Microsoft Learn. https://learn.microsoft.com/en-us/azure/expressroute/expressroute-locations-providers

Microsoft. (2026, 23 de septiembre). *List of Azure regions*. Microsoft Learn. https://learn.microsoft.com/en-us/azure/reliability/regions-list

Microsoft. (2026, 30 de julio). *Azure network round-trip latency statistics*. Microsoft Learn. https://learn.microsoft.com/en-us/azure/networking/azure-network-latency

Microsoft. (2026, 5 de septiembre). *What is Azure Database for PostgreSQL flexible server?*. Microsoft Learn. https://learn.microsoft.com/en-us/azure/postgresql/flexible-server/overview

Microsoft. (2026, 6 de mayo). *Understand Azure IoT Hub quotas and throttling*. Microsoft Learn. https://learn.microsoft.com/en-us/azure/iot-hub/iot-hub-devguide-quotas-throttling

Minew. (2023). *G1 IoT Bluetooth gateway*. https://www.minew.com/wp-content/uploads/2023/12/G1-IoT-Bluetooth%C2%AE-Gateway.pdf

Ministerio de Transportes. (1995). *Decreto Supremo N.º 298. Reglamento de transporte de cargas peligrosas por calles y caminos*.

Ministerio del Trabajo. (2003). *Decreto con Fuerza de Ley N.º 1. Texto refundido, coordinado y sistematizado del Código del Trabajo. Artículo 25 bis sobre jornada de choferes de vehículos de carga terrestre interurbana*. Biblioteca del Congreso Nacional de Chile. https://www.bcn.cl/leychile/navegar?idNorma=207436

Northern.tech. (2026). *Variables. Mender documentation*. https://docs.mender.io/operating-system-updates-yocto-project/variables

OnLogic. (2026). *Karbon 430. Compact rugged computer with expansion*. https://static.onlogic.com/resources/spec-sheets/OnLogic-K430-Spec-Sheet-V5.pdf

Schneider Electric. (2023). *APC Smart-UPS On-Line SRT3000XLI. Product datasheet*. https://media.distrelec.com/Web/Downloads/_t/ds/SRT3000XLI_eng_tds.pdf

Schneider Electric. (2024). *APC Smart-UPS SRT 1000VA 230V SRT1000XLI. Product datasheet*. https://docs.rs-online.com/8440/A700000007481704.pdf

Stulz. (2024). *MiniSpace EC. Precision air conditioning for small heat loads*. https://www.stulz.com/en-us/products/detail/minispaceec/

Subsecretaría de Telecomunicaciones. (2026). *Bandas en las que operan los teléfonos celulares en Chile*. https://www.subtel.gob.cl/bandas-en-las-que-operan-los-telefonos-celulares-en-chile/

Technoton. (2026). *CANCrocodile: contactless CAN bus reader*. https://e-shop.jv-technoton.com/product/cancrocodile/

Teltonika Networks. (2026). *RUTX50 industrial 5G router*. https://www.teltonika-networks.com/products/routers/rutx50

Teltonika Networks. (2026). *TSW202 PoE+ managed Ethernet switch*. https://www.teltonika-networks.com/products/ethernet-switches/tsw202

Transportes Curimón S.A. (2026). *Bases administrativas para la preparación de la propuesta: Licitación Pública Internacional N.º TFEP-01/2026* (Documento FEP01).

Transportes Curimón S.A. (2026). *Bases técnicas del Caso 10, Transporte de Carga: Licitación Pública Internacional N.º TFEP-01/2026* (Documento FEP03).

Transportes Curimón S.A. (2026). *Bases técnicas transversales para la preparación de la propuesta: Licitación Pública Internacional N.º TFEP-01/2026* (Documento FEP02).

Transportes Curimón S.A. (2026). *Comunicado 10: Estructura obligatoria de las propuestas preparatorias y técnica final* (Comunicado de la licitación TFEP-01/2026).

Vertiv. (2026). *Liebert Mini-Mate2, MMD12E, 3.55 kW*. https://www.vertiv.com/en-us/products-catalog/thermal-management/room-cooling/mmd12e-3.55kw/

Webfleet. (2026). *Webfleet SAT. Ficha técnica para Chile*. https://www.webfleet.com/es_cl/webfleet/products/link/webfleet-sat/

## Declaración de uso de IA

Conforme al Comunicado 10, sección 7.2, cada sección de este subdocumento y cada formulario asociado declara la herramienta de inteligencia artificial generativa usada, su finalidad, el nivel de uso en texto y en diagramas según la escala oficial de esa sección, y quién revisó y qué verificó. Esta declaración se consolida en el Formulario A-6.

| Sección | Herramienta | Finalidad del uso | Nivel en texto | Nivel en diagramas | Revisión humana (quién y qué verificó) |
|---|---|---|---|---|---|
| Artículo 46 | Claude Opus 5.5 en Claude Code | Redacción de las respuestas normativas y trazabilidad de secciones técnicas | Alto | Ninguno | Carlos Jesús Abarza Suazo, Director de Auditoría y Aseguramiento Tecnológico: Validación de ingeniería |
| Introducción | Claude Opus 5.5 en Claude Code | Síntesis del capítulo, articulación de 8 capas y alineamiento con el pliego | Alto | Ninguno | Carlos Jesús Abarza Suazo, Director de Auditoría y Aseguramiento Tecnológico: Validación de ingeniería |
| 4.1 y 4.1.1 | Claude Opus 5.5 en Claude Code | Estructuración de arquitectura lógica, contextos delimitados y tecnologías de software | Medio | Bajo | Carlos Jesús Abarza Suazo, Director de Auditoría y Aseguramiento Tecnológico: Verificación de contratos OpenAPI y ADRs |
| 4.2 y 4.2.1 | Claude Opus 5.5 en Claude Code | Estructuración de arquitectura física híbrida, dimensionamiento de hardware y memoria eMMC | Medio | Bajo | Carlos Jesús Abarza Suazo, Director de Auditoría y Aseguramiento Tecnológico: Verificación de cálculos de concurrencia y T-11 |
| 4.3, 4.3.1 y 4.3.2 | Claude Opus 5.5 en Claude Code | Estrategia de data center primaria y secundaria, balance de cargas y alta disponibilidad | Medio | Bajo | Carlos Jesús Abarza Suazo, Director de Auditoría y Aseguramiento Tecnológico: Certificación de estándares TIA-942 y ASHRAE |
| Formulario T-11 | Claude Opus 5.5 en Claude Code | Consolidación tabular de las 68 partidas de hardware y software del Formulario T-11 | Alto | Ninguno | Carlos Jesús Abarza Suazo, Director de Auditoría y Aseguramiento Tecnológico: Auditoría de partidas industriales y ciclo de vida |
| 4.2.2, 4.2.8 y Formulario T-11 — Conciliación incremental H | Codex; generación asistida de imágenes | Reconciliación de perfil, memoria en bytes/MiB, cuotas de reconexión, particiones y figura de reconexión | Alto | Medio | Revisión humana de estos cambios pendiente |
