# Modelo y Gestión de Datos

**Subdocumento N.º 5**

| | |
|---|---|
| Empresa | audIT, Empresa N.º 10 |
| Licitación | Licitación Pública Internacional N.º TFEP-01/2026. Caso 10 Transporte de Carga |
| Proyecto | Plataforma Digital de Misión Crítica para Transporte de Carga |
| Cliente | Transportes Curimón S.A. |
| Instancia | Informe Preparatorio 1. Oferta Técnica Sobre N.º 2 |
| Contenido | Modelo de dominio, persistencia, auditoría, retención, respaldo, migración y protección de datos personales. |
| Versión | 1.0 |
| Fecha | 7 de septiembre de 2026 |
| Lugar | Viña del Mar, Chile |

---

## Modelo y gestión de datos


### Control de versiones y diagnóstico de evolución técnica


#### Diagnóstico del modelo inicial y deficiencias superadas


En la auditoría técnica de arquitectura se identificaron cuatro vulnerabilidades estructurales en las aproximaciones iniciales frente a las exigencias de las Bases Técnicas del Caso 10 (Escuela de Informática PUCV, 2026c):


- **Modelo anémico monolítico:** Las entidades se concebían como simples esquemas de tablas pasivas con claves foráneas, sin encapsulamiento de invariantes de negocio ni validaciones previas a la persistencia (vulnerando el control bloqueante del Código del Trabajo, Artículo 25 bis (Ministerio del Trabajo, 2003), antes de autorizar despachos en $\le 30$ segundos según RT-09.01).
- **Antipatrón de saturación por telemetría:** Acoplar tablas relacionales estándar al flujo continuo de los $\approx 41.000.000$ km/año y 374 unidades generaba contención de bloqueos e indisponibilidad transaccional en la torre de programación 24/7.
- **Omisión de la asimetría tracto-rampla:** No se disociaba el tractocamión (148 propios, 226 subcontratados) del semirremolque (210 equipos propios y ramplas de terceros), impidiendo controlar vigencias técnicas y habilitaciones químicas independientes bajo el D.S. N.º 298 para sustancias peligrosas (Ministerio de Transportes, 1995).
- **Ausencia de Gobierno de Datos Maestros (MDM) y omisión en plazos legales de retención:** No existía una estrategia para evitar duplicación de entidades entre la nueva plataforma y el ERP contable legado de 2013 (RT-05.09), omitiéndose además el plazo legal de habilitaciones (vigencia más 5 años) fijado en el Capítulo 15 del Caso.


#### Cuadro comparativo de innovaciones técnicas


**Tabla. Evolución técnica del modelo de datos audIT**

| **Dimensión** | **Enfoque Anterior** | **Enfoque Definitivo audIT** | **Impacto en Curimón** |
|---|---|---|---|
| Paradigma de Modelado | Esquema ERD relacional plano. | Domain-Driven Design (DDD): contextos delimitados e invariantes (RT-02.13). | Valida en memoria y previene despachos ilegales en $\le 30$ s. |
| Ingesta Telemática | Tablas relacionales sobrecargadas. | Arquitectura Fast-Data desacoplada: TimescaleDB / Kafka y búfer offline 72 h. | Aísla pings GPS del motor central y resiste sombras $> 80$ km. |
| Gobernanza de Activos | Entidad única CAMION. | Disociación estricta TRACTOCAMION y SEMIRREMOLQUE. | Controla vencimientos cruzados y compatibilidad química (DS 298). |
| Datos Maestros (MDM) | Entidades dispersas sin sincronización. | MDM de Registro Maestro Único (\textit{Golden Record}) con Capa Anticorrupción. | Evita duplicidad de 454 choferes, 374 camiones y 84 clientes vs ERP 2013. |
| Estrategia de Desempeño | Índices genéricos sin partición. | Particionamiento mensual, índices GiST y BRIN, y caché L2 Redis Cluster. | Geocercas en $< 5$ ms y almacenamiento telemático optimizado 95 %. |
| Saneamiento Vigencias | Carga masiva sin contrastación. | Verificación documental individual obligatoria con hash SHA-256 en WORM. | Sanea 4 planillas ($\approx 6.000$ vigencias) y erradica multas por atraso. |
| Seguridad y Privacidad | Cifrado de disco estándar. | Cifrado a nivel de campo (FLE AES-256-GCM) y anonimización en Dev/QA. | Cumplimiento irrestricto Ley N.º 21.719 en 258 choferes externos. |
| Retención Legal | Plazos genéricos sin norma. | Matriz ajustada a Cap. 15 del Caso (10a, 6a, 5a, vigencia+5a, 3a, 2a). | Certeza probatoria laboral, tributaria (SII) y sobreestadías. |


### Modelo de dominio y fronteras transaccionales (DDD)


Para gobernar una operación anual de 96.000 viajes, 374 camiones (148 propios, 226 subcontratados), 210 semirremolques propios y 454 conductores, el sistema se estructura bajo principios de \textit{Domain-Driven Design} (DDD) en seis contextos delimitados interconectados mediante eventos de dominio asíncronos y una Capa Anticorrupción (ACL) que aísla el ERP Contable de 2013 (RT-02.13, RT-05.09):


- **Agregado Viaje (Core Domain):** Orquesta la máquina de estados finita (\texttt{PROGRAMADO} $\to$ \texttt{EN_CARGA} $\to$ \texttt{EN_RUTA} $\to$ \texttt{EN_DESCARGA} $\to$ \texttt{CERRADO} / \texttt{CANCELADO}). Ejecuta el método bloqueante \texttt{asignarRecursos()} validando en memoria y de forma atómica: (i) aptitud técnica y vigencia del tracto, (ii) compatibilidad y habilitación de la rampla (D.S. N.º 298), y (iii) jornada disponible del conductor bajo el Artículo 25 bis del Código del Trabajo (Ministerio del Trabajo, 2003). Dispone del método \texttt{suspenderPorTramiteAduanero()} para congelar el cómputo de sobreestadías ante cierres invernales en Los Libertadores (hasta 12 días por nieve o 14 horas de cola aduanera).
- **Agregado Tractocamion:** Custodia las vigencias técnicas y mecánicas del vehículo motor (revisión técnica, SOAP, permiso de circulación) y administra el estado de telemetría CANbus/FMS (SAE J1939 activo en 61 unidades propias).
- **Agregado Semirremolque:** Modela los 210 equipos de arrastre propios y los de terceros. Implementa la regla \texttt{cumpleNormaEstanqueDS298()} para asegurar que ninguna carga ácida o combustible sea despachada en carrocerías sin prueba de estanqueidad vigente.
- **Agregado Conductor:** Gobierna el control estricto de la jornada laboral bajo el Artículo 25 bis (máximo 5 horas continuas de conducción, descanso mínimo de 2 horas intermedias y verificación de descanso semanal previo). Custodia la entidad de consentimiento de datos bajo la Ley N.º 21.719 (Congreso Nacional de Chile, 2024).
- **Agregado Transportista:** Modela la relación comercial con los 148 dueños de camiones independientes, sus contratos marco, tarifas pactadas y reglas de pre-liquidación mensual.
- **Agregado OrdenTransporte:** Representa la relación contractual con los 84 clientes generadores de carga, tarifas acordadas, geocercas de origen/destino y especificaciones de carga peligrosa.


### Estrategia de Gestión de Datos Maestros (MDM)


En cumplimiento de RT-05.09, la solución implementa un marco centralizado de Master Data Management (MDM) estructurado bajo el principio de Registro Maestro Único (\textit{Golden Record}), erradicando la duplicación entre la nueva plataforma y el sistema legado:


- \textbf{Definición de Fuentes de Verdad (\textit{Source of Truth}):}

- \textit{Maestro de Conductores y Habilitaciones:} La plataforma audIT es la fuente exclusiva de verdad. Ningún conductor puede ser dado de alta o modificado directamente en el ERP.
- \textit{Maestro de Flota (Tractos y Semirremolques):} Administrado exclusivamente en el módulo de flota de audIT, sincronizando la PPU y estado operativo.
- \textit{Maestro de Clientes y Proveedores (Transportistas):} El ERP contable mantiene la tuición de la razón social y datos bancarios/tributarios, mientras que audIT extiende la entidad con los atributos operacionales (geocercas, tarifas de flete, contratos de adhesión).

- **Reglas de desduplicación y limpieza:**

- \textit{Conductores:} Llave unívoca normalizada por RUT chileno validado algorítmicamente (Módulo 11). Prohibición de registros duplicados por variaciones de nombre o espacios.
- \textit{Flota:} Llave primaria natural basada en la Placa Patente Única (PPU) en formato estándar del Registro Civil e Identificación.

- **Propagación y consistencia eventual:** Toda actualización en un maestro dispara un evento de integración a través de Azure Service Bus / Kafka, asegurando que todos los servicios mantengan el mismo estado en menos de 2 segundos.


### Calidad de datos bajo ISO/IEC 25012 y catálogo con linaje


En cumplimiento de RT-05.04, la gestión de la información se rige formalmente por el estándar internacional ISO/IEC 25012 (\textit{Data Quality Model}) (ISO, 2008):


**Tabla. Métricas de calidad de datos bajo ISO/IEC 25012**

| **Dimensión ISO 25012** | **Métrica Comprometida** | **Mecanismo de Control en la Solución** |
|---|---|---|
| Completitud (\textit{Completeness}) | $\ge 99{,}8$% de campos obligatorios en despachos. | Validación bloqueante web y móvil, impidiendo viajes con conductor o activo nulo. |
| Exactitud (\textit{Accuracy}) | 100 % RUT válidos con DV y 100 % patentes verificadas. | Validación sintáctica Módulo 11 y cotejo con padrón oficial autorizado. |
| Consistencia (\textit{Consistency}) | 100 % correspondencia tracto, rampla y carga. | Reglas de negocio que impiden asignar ramplas estándar a órdenes DS 298. |
| Credibilidad (\textit{Credibility}) | 100 % marcas temporales sincronizadas. | NTP estrato 1 y reloj GPS satelital con descarte de reloj manipulable del SO local. |
| Accesibilidad (\textit{Accessibility}) | Disponibilidad $\ge 99{,}9$% para 22 despachadores 24/7. | Réplicas de lectura transaccionales distribuidas en zonas Multi-AZ. |


Se provee un tablero operacional en tiempo real que reporta el \textit{Data Quality Index}, alertando anomalías y vigencias antes de que se traduzcan en fallas de servicio. Asimismo, se incorpora un catálogo de metadatos (OpenMetadata / Azure Purview) que traza visualmente el linaje automatizado de extremo a extremo: desde el dato crudo en el sensor CANbus o ticket de peaje hasta el indicador financiero de «Costo por Kilómetro por Ruta» expuesto a la Gerencia de Finanzas.


### Persistencia políglota y justificación frente al Teorema CAP


En estricta conformidad con RT-05.02, la solución adopta una Arquitectura Políglota Híbrida gobernada por el Teorema CAP para cada dominio operacional:


**Tabla. Persistencia políglota y clasificación CAP**

| **Capa / Dominio** | **Clase CAP** | **Motor Tecnológico** | **Justificación Operacional** |
|---|---|---|---|
| Transaccional Maestra | Sistema CP | PostgreSQL 16 Enterprise + PostGIS | Consistencia estricta (ACID) irrenunciable en asignación, vigencias y DTE. Preferible encolar a autorizar chofer fatigado. |
| Telemetría y Streaming | Sistema AP | TimescaleDB / Kafka / Event Hubs | Disponibilidad extrema y tolerancia a particiones bajo consistencia eventual (BASE) para absorber 41M km/año. |
| Búfer a Bordo en Cabina | Sistema AP local | SQLite 3 embebido con WAL | Persistencia local atómica en flash industrial ($\ge 8\text{ GB}$) con 72 h a 288 h de autonomía ante cortes eléctricos o sombras. |
| Caché y Baja Latencia | En memoria | Redis 7.2 Cluster | Evaluación de geocercas para 1.400 puntos de clientes y terminales en $< 5$ ms sin golpear disco. |
| Documentos y Evidencia | Inmutable | Object Storage WORM (Compliance) | Custodia inalterable de firmas, e-Docs y actas con retención bloqueada frente a administradores. |


![Persistencia políglota. Consistencia estricta, disponibilidad extrema y capa transitoria](Persistencia.pdf)

*Figura. Persistencia políglota. Consistencia estricta, disponibilidad extrema y capa transitoria*


### Estrategia de desempeño de base de datos


Para garantizar que la validación bloqueante de despacho responda en $\le 30$ segundos (RT-09.01) sin contención de bloqueos frente a los 96.000 viajes anuales, se implementa una estrategia cuádruple de optimización:


- **Indexación especializada:** Índices B-Tree en claves foráneas (\texttt{id_tracto}, \texttt{id_conductor}, \texttt{id_semirremolque}) y RUTs, índices espaciales GiST y SP-GiST (PostGIS) en polígonos de geocercas para optimizar \texttt{ST_Contains()} y \texttt{ST_DWithin()}, además de índices BRIN (\textit{Block Range Indexes}) en marcas temporales de telemetría y auditoría, ocupando un 95 % menos de espacio en disco y memoria RAM que un B-Tree tradicional.
- **Particionamiento horizontal declarativo:** La tabla transaccional central \texttt{viaje} se particiona por rango de fechas en segmentos **mensuales**, concentrando el 90 % de las consultas en la partición activa. Las tablas históricas de telemetría y auditoría se particionan automáticamente, facilitando su desacople hacia almacenamiento en frío (\textit{Detached Partitions}).
- **Caché multinivel de baja latencia:** Nivel 1 en memoria de microservicios para catálogos estáticos y Nivel 2 en Redis Cluster para sesiones, estados de vigencia precalculados y coordenadas de las 1.400 instalaciones de clientes ($< 5$ ms).
- **Vistas materializadas concurrentes:** Actualizadas de forma asíncrona (\texttt{REFRESH MATERIALIZED VIEW CONCURRENTLY}) para saldos de pre-liquidación y consumos de combustible, evitando escaneos masivos sobre tablas en caliente durante la jornada diurna.


### Modelo lógico de persistencia y diccionario de datos


El esquema relacional en PostgreSQL 16 implementa claves primarias UUIDv4 generadas criptográficamente, restricciones de integridad referencial estricta y cascada restringida.


#### Criterios de clasificación de sensibilidad (Ley N.º 21.719 y RT-11.10)


- **Pública / Operacional Interna:** Identificadores del sistema, códigos de viaje, patentes PPU.
- **Personal:** Datos que identifican directamente a personas naturales (RUT, nombre, teléfono de conductores).
- **Sensible / Laboral:** Trazas de geolocalización continua, sellos de tiempo de descanso y jornada, infracciones viales $\to$ **Cifrado a nivel de campo (FLE AES-256-GCM) obligatorio**.
- **Confidencial Comercial:** Tarifas unitarias pactadas con cada uno de los 148 transportistas subcontratados y pre-liquidaciones de flete $\to$ **Cifrado a nivel de campo (FLE AES-256-GCM) obligatorio**.


#### Diccionario de datos de las entidades centrales


**Tabla. Entidad CONDUCTOR (196 propios y 258 externos)**

| **Atributo** | **Tipo de Dato** | **Dominio / Formato** | **Req.** | **Sensibilidad y Tratamiento** |
|---|---|---|---|---|
| id_conductor | UUIDv4 | Identificador global | Sí | Operacional. Clave primaria B-Tree. |
| id_transportista | UUIDv4 | FK hacia TRANSPORTISTA | No | Operacional. Nulo si es conductor propio Curimón. |
| rut_conductor | VARCHAR(12) | Formato nacional con DV | Sí | **Personal**. Cifrado FLE (AES-256-GCM). |
| nombre_completo | VARCHAR(120) | Texto alfabético | Sí | **Personal**. Cifrado FLE (AES-256-GCM). |
| clase_licencia | VARCHAR(5) | 'A5', 'A4', 'A2' | Sí | Operacional. Validación aptitud de conducción. |
| estado_operativo | ENUM | 'HABILITADO', 'BLOQUEADO' | Sí | Operacional. Control despacho bloqueante (RT-09.01). |


**Tabla. Entidades TRACTOCAMION y SEMIRREMOLQUE (374 tractos y 210 ramplas)**

| **Atributo** | **Tipo de Dato** | **Dominio / Formato** | **Req.** | **Sensibilidad y Tratamiento** |
|---|---|---|---|---|
| id_tracto | UUIDv4 | Identificador global | Sí | Operacional. Clave primaria. |
| patente | VARCHAR(8) | Formato PPU nacional | Sí | Operacional. Índice B-Tree único. |
| tipo_propiedad | ENUM | 'PROPIO', 'TERCERO' | Sí | Operacional. Filtro auditoría y liquidación. |
| canbus_activo | BOOLEAN | TRUE, FALSE | Sí | Operacional. TRUE en 61 unidades iniciales. |
| id_semirremolque | UUIDv4 | Identificador global | Sí | Operacional. Clave primaria. |
| tipo_carroceria | ENUM | 'RAMPLA', 'ESTANQUE', 'TOLVA' | Sí | Operacional. Compatibilidad química DS 298. |
| capacidad_ton | NUMERIC(5,2) | 1.00 a 45.00 ton | Sí | Operacional. Restricción física de carga. |


**Tabla. Entidad VIGENCIA_HABILITACION (Núcleo de las $\approx 6.000$ fechas vivas)**

| **Atributo** | **Tipo de Dato** | **Dominio / Formato** | **Req.** | **Sensibilidad y Tratamiento** |
|---|---|---|---|---|
| id_vigencia | UUIDv4 | Identificador global | Sí | Operacional. Clave primaria. |
| id_sujeto | UUIDv4 | FK polimórfica (Tracto/Rampla/Chofer) | Sí | Operacional. Índice compuesto con tipo documento. |
| tipo_sujeto | ENUM | 'TRACTO', 'RAMPLA', 'CONDUCTOR' | Sí | Operacional. Discriminador de activo. |
| tipo_documento | ENUM | Catálogo oficial de 12 tipos | Sí | Operacional. Rev. Técnica, SOAP, Licencia, DS 298. |
| fecha_vencimiento | DATE | Fecha calendario | Sí | Operacional. Disparador de alertas preventivas. |
| estado_verificacion | ENUM | 'VERIFICADO', 'PENDIENTE' | Sí | **Solo 'VERIFICADO' autoriza flete**. |
| id_documento | UUIDv4 | FK hacia DOCUMENTO_RESPALDO | Sí | Operacional. Evidencia documental obligatoria. |


**Tabla. Entidad DOCUMENTO_RESPALDO (Custodia Criptográfica)**

| **Atributo** | **Tipo de Dato** | **Dominio / Formato** | **Req.** | **Sensibilidad y Tratamiento** |
|---|---|---|---|---|
| id_documento | UUIDv4 | Identificador global | Sí | Operacional. Clave primaria. |
| hash_sha256 | CHAR(64) | Hash criptográfico hexadecimal | Sí | **Firma inalterabilidad probatoria**. |
| uri_almacenamiento | VARCHAR(500) | URI Object Storage WORM | Sí | Operacional. Almacenamiento inmutable. |
| fecha_carga | TIMESTAMPTZ | Sello UTC de subida | Sí | Operacional. Trazabilidad temporal auditada. |


**Tabla. Entidad CONSENTIMIENTO_DATOS (Soberanía y Ley N.º 21.719)**

| **Atributo** | **Tipo de Dato** | **Dominio / Formato** | **Req.** | **Sensibilidad y Tratamiento** |
|---|---|---|---|---|
| id_consentimiento | UUIDv4 | Identificador global | Sí | Operacional. Clave primaria. |
| id_transportista | UUIDv4 | FK hacia TRANSPORTISTA | Sí | Operacional. Titular del camión subcontratado. |
| comparte_posicion | BOOLEAN | TRUE, FALSE | Sí | **Sensible**. Permiso streaming GPS en flete activo. |
| comparte_telemetria | BOOLEAN | TRUE, FALSE | Sí | **Sensible**. Permiso lectura odómetro y CANbus. |
| autoriza_clientes | JSONB | Lista de IDs de mandantes | Sí | **Sensible**. Whitelist mandantes autorizados. |
| fecha_otorgamiento | TIMESTAMPTZ | Sello UTC de autorización | Sí | Operacional. Trazabilidad legal probatoria. |
| fecha_revocacion | TIMESTAMPTZ | Sello UTC (nullable) | No | Operacional. Cese inmediato de transmisión. |


**Tabla. Entidad VIAJE (Transacción Central, 96.000 viajes/año)**

| **Atributo** | **Tipo de Dato** | **Dominio / Formato** | **Req.** | **Sensibilidad y Tratamiento** |
|---|---|---|---|---|
| id_viaje | UUIDv4 | Identificador global | Sí | Operacional. Clave primaria. |
| codigo_viaje | VARCHAR(20) | Formato VJ-YYYYMM-XXXXXX | Sí | Operacional. Identificador unívoco de flete. |
| id_tracto | UUIDv4 | FK hacia TRACTOCAMION | Sí | Operacional. Validación técnica bloqueante. |
| id_semirremolque | UUIDv4 | FK hacia SEMIRREMOLQUE | No | Operacional. Exigido en cargas con rampla. |
| id_conductor | UUIDv4 | FK hacia CONDUCTOR | Sí | Operacional. Validación jornada Art. 25 bis. |
| peso_origen_kg | NUMERIC(8,2) | Peso báscula / ticket | Sí | Operacional. Mitigación de 142 sobrepesos/año. |
| estado_viaje | ENUM | 6 estados operacionales | Sí | Operacional. Máquina de estados finita. |


### Auditoría inalterable de modificaciones (Append-Only CDC)


Para satisfacer RT-05.03, RT-16.06, RT-16.07 y el Criterio de Aceptación 4 de las Bases Técnicas:


- **Trigger de auditoría transaccional:** Toda sentencia \texttt{INSERT}, \texttt{UPDATE} o \texttt{DELETE} sobre entidades maestras, viajes y habilitaciones dispara un trigger a nivel de fila (\texttt{AFTER INSERT OR UPDATE OR DELETE ... FOR EACH ROW}) que inserta un registro en la tabla particionada \texttt{auditoria_evento}, capturando atómicamente los estados \texttt{OLD} y \texttt{NEW} en formato JSONB.
- **Estructura forense del registro:** Captura identificador de operador (\texttt{usuario_id}), IP de origen, dispositivo, sello UTC sincronizado por NTP estrato 1, tabla intervenida, UUID y estados anterior y posterior.
- **Inalterabilidad y blindaje frente a administradores (RT-16.07):** Se revocan formalmente los permisos de modificación o borrado a nivel de base de datos:
    \begin{quote}
    \small\texttt{REVOKE UPDATE, DELETE, TRUNCATE ON TABLE auditoria_evento FROM PUBLIC, dba_admin, audit_app;}
    \end{quote}
    Cada registro incorpora un hash encadenado SHA-256 (\textit{Hash Chain}) que vincula criptográficamente el evento actual con el hash del evento anterior. Los segmentos mensuales cerrados se replican en caliente hacia un bucket de almacenamiento inmutable WORM con retención bloqueada (\textit{Object Lock Compliance}).


### Esquema de respaldo 3-2-1-1-0 y continuidad operacional


Para garantizar la continuidad de servicio con un RTO $\le 4$ horas y un RPO $\le 15$ minutos conforme a RT-07.02, RT-07.04, RT-07.09 y RT-07.13, se implementa la política 3-2-1-1-0:


- **3 Copias de la Información:** 1 base productiva viva en Azure Chile Central (Multi-AZ), 1 réplica síncrona en zona secundaria, y 1 respaldo binario diario consolidado.
- **2 Medios Diferentes:** Almacenamiento NVMe local de alta velocidad para la base viva y Azure Blob Storage con redundancia geográfica (GZRS) para los respaldos binarios.
- \textbf{1 Copia Fuera de Sitio (\textit{Off-site}):} Replicación asíncrona continua de logs de transacciones (\textit{WAL-G archiving}) hacia una región secundaria a más de 100 km (Azure East US 2 o región equivalente).
- \textbf{1 Copia Desconectada e Inmutable (\textit{Immutable Air-Gapped}):} Snapshots semanales con retención bloqueada WORM (\textit{Object Lock Compliance}) que impiden cualquier alteración, incluso ante secuestro de credenciales maestras.
- **0 Errores en Ensayos de Restauración:** Pipeline semanal automatizado que levanta una instancia efímera de PostgreSQL, restaura el último backup binario, aplica los WALs hasta el punto en el tiempo (PITR) y ejecuta pruebas automáticas de consistencia referencial (\texttt{pg_amcheck}).
- **Cifrado Integral:** Datos en tránsito con TLS 1.3 y datos en reposo cifrados con AES-256 (TDE / LUKS) con llaves en Azure Key Vault gestionado (HSM FIPS 140-2 Nivel 3) con rotación anual.


**Tabla. Matriz de respaldo, retención y RTO por dominio**

| **Dominio de Datos** | **Retención Exigida** | **Frecuencia y Estrategia** | **RTO** |
|---|---|---|---|
| Jornada de conducción y evidencia | Mínimo 5 años | Continua (WAL Streaming) + Diaria consolidada | $\le 2$ horas |
| DET y antecedentes del viaje | 6 años | Continua (WAL Streaming) + Diaria consolidada | $\le 2$ horas |
| Antecedentes de siniestros | 10 años | Diaria consolidada + WORM mensual | $\le 4$ horas |
| Habilitaciones conductores y flota | Vigencia + 5 años | Diaria consolidada | $\le 2$ horas |
| Registros de carga peligrosa (DS 298) | 5 años | Diaria consolidada + WORM mensual | $\le 2$ horas |
| Tiempos en recintos de clientes | 3 años | Diaria consolidada | $\le 4$ horas |
| Liquidaciones a transportistas | 6 años | Diaria + pre y post cierre mensual | $\le 2$ horas |
| Series de posición y telemetría | 2 años en línea | Continua (Micro-batch / TimescaleDB chunks) | $\le 4$ horas |


Cuarta copia distribuida en el borde: las unidades intervenidas de la flota (148 tractocamiones propios y los 34 camiones de terceros incorporados por adhesión voluntaria) conservan en la memoria flash industrial ($\ge 8\text{ GB}$) de su dispositivo embarcado el registro operacional íntegro de al menos 72 horas y hasta 288 horas continuas durante aislamientos por nieve en Los Libertadores, mientras que los 192 terceros homologados mantienen el búfer local exigido por el estándar de interoperabilidad sin intervenir su equipamiento privado. Si bien no sustituye al respaldo centralizado, constituye una fuente distribuida de reconciliación determinista ante caídas de red.


### Migración de datos y saneamiento histórico


#### Acreditación documental individual de las $\approx 6.000$ vigencias


Transportes Curimón S.A. administra aproximadamente 6.000 fechas de vencimiento vivas dispersas en cuatro planillas de cálculo independientes sin integridad referencial. En conformidad con RT-05.15 del Capítulo 15:


- **Regla probatoria de habilitación:** Ningún registro de vigencia migrado se considerará habilitante para despachar si no cuenta con su respectiva **verificación documental individual**.
- **Custodia criptográfica:** Cada documento de respaldo (licencia, revisión técnica, SOAP, curso DS 298) se almacena en el repositorio inmutable WORM y se sella con su huella SHA-256 vinculada en base de datos.
- **Régimen de excepción gobernado:** Registros sin documento digital ingresan como \texttt{'PENDIENTE_DOCUMENTACION'}. Se otorga una ventana perentoria de 30 días en marcha blanca. Cumplido el plazo, el sistema bloquea automáticamente la asignación del activo o chofer hasta cargar el respaldo verificado.


#### Alcance cuantitativo y plan de migración en 4 fases


**Tabla. Alcance de migración histórica del Caso 10**

| **Dominio Histórico a Migrar** | **Volumen del Caso 10** | **Criterio de Aceptación y Conciliación** |
|---|---|---|
| Maestros de Flota y Semirremolques | 100 % (374 tractos y 210 ramplas) | Conciliación 1:1 contra padrón oficial del Registro Civil. |
| Maestros Conductores y Transportistas | 100 % (454 choferes y 148 dueños) | Conciliación de RUTs y contratos marco vigentes. |
| Maestro de Clientes y Geocercas | 100 % (84 clientes y 1.400 puntos) | Validación de direcciones y polígonos geoespaciales. |
| Vigencias de Habilitación Vivas | $\approx 6.000$ registros en 4 planillas | Verificación documental individual con hash SHA-256. |
| Histórico de Viajes Operacionales | 5 años ($\approx 480.000$ viajes) | Conciliación de totales, códigos de flete y fechas. |
| Histórico de Liquidaciones | 6 años ($\approx 10.656$ liquidaciones) | Cuadre financiero al peso contra libros del ERP 2013. |
| Histórico de Siniestros | 100 % de antecedentes disponibles | Integridad de expedientes legales y peritajes de seguros. |


- **Fase 1: Perfilamiento y Extracción (Días 1 a 15):** Scripts de perfilamiento sobre las 4 planillas de vigencias y bases del ERP 2013, identificando inconsistencias, RUTs erróneos y fechas caducadas.
- **Fase 2: Homologación y Normalización (Días 16 a 35):** Limpieza algorítmica, resolución de discrepancias junto a Prevención de Riesgos y Tráfico, y homologación al catálogo de enums.
- **Fase 3: Acreditación Documental y Hash Criptográfico (Días 36 a 50):** Carga masiva de documentos digitalizados, generación de hashes SHA-256 y segregación de pendientes.
- \textbf{Fase 4: Ensayos de Migración (\textit{Mock Runs}) y Transición Final (\textit{Cutover}):}

- \textit{Primer Ensayo Completo (Día 45, RT-05.13):} Ensayo en seco (\textit{Dry-Run}) en Preproducción con el 100 % de los datos para medir tiempos de ingestión, latencias y tasa de excepciones.
- \textit{Segundo Ensayo Completo (Día 60, RT-05.13):} Simulación integral de corte operacional (\textit{Cutover Rehearsal}) y prueba de estrés de validación bloqueante de despacho sobre el volumen total migrado.
- \textit{Conciliación Cuantitativa y Firma de Acta (RT-05.14):} Verificación matemática del 100 % de patentes, conductores y saldos contables. El paso a Producción requiere la firma formal de un Acta de Conciliación sin discrepancias.


### Protección de datos personales y soberanía (Ley N.º 21.719)


RT-11.10 exige cifrado a nivel de campo para los datos personales de los 258 conductores que no son trabajadores de la compañía, para toda información de localización asociada a una persona identificable, para los antecedentes de jornada y para las tarifas pactadas con cada transportista. La Ley N.º 21.719 (Congreso Nacional de Chile, 2024) gobierna ese tratamiento:


- **Soberanía y minimización del dato:** La solución no sabe dónde está una persona, sino dónde está un camión durante la ejecución de un flete contratado, con autorización expresa y revocable de su dueño (RT-16.30). Fuera de la ventana temporal del viaje, el streaming de posición se suspende a nivel de firmware en cabina.
- **Anonimización verificable en desarrollo y pruebas (RT-04.14):** Prohibición total de clonar bases productivas a entornos de desarrollo o QA sin anonimización previa. Se aplican RUTs sintéticos vía Módulo 11 pseudoaleatorio, enmascaramiento irreversible de nombres y adición de ruido gaussiano ($\mu = 1.0, \sigma = 0.05$) sobre tarifas y liquidaciones para preservar distribuciones estadísticas destruyendo los valores nominales.
- **Revocación de consentimiento vs. retención legal mandatoria:** Ante la revocación de consentimiento de un transportista, cesa de inmediato la captura telemática futura. Sin embargo, para cumplir con las obligaciones legales de conservación del Estado de Chile (Art. 25 bis por 5 años, Código Tributario por 6 años y responsabilidad civil por 10 años), los datos históricos precedentes se bloquean en cuarentena criptográfica de solo lectura, accesibles únicamente ante requerimiento judicial.
- \textbf{Destrucción criptográfica definitiva (\textit{Crypto-shredding}):} Cumplidos íntegramente los plazos estatutarios de retención, se gatilla automáticamente la purga mediante \textit{crypto-shredding}, destruyendo las llaves FLE en Azure Key Vault asociadas al titular, renderizando los datos matemáticamente irrecuperables en disco y respaldos sin alterar la integridad estructural de la base de datos (NIST, 2014).
- \textbf{Garantía de reversibilidad contractual sin \textit{vendor lock-in} (RT-05.06):} Al cierre contractual (mes 36 o 56), audIT garantiza formalmente la entrega del patrimonio completo de datos en formatos abiertos y documentados sin costo adicional: volcado SQL estándar (\texttt{pg_dump}), series telemáticas en Apache Parquet columnar, y repositorio e-Docs en ZIP estructurado con manifiesto JSON Schema y catálogo de hashes SHA-256.


### Analítica y costo real por kilómetro en $\le 24$ horas


Para dar cumplimiento a RT-05.05 y soportar la analítica financiera:


- **Aislamiento total de cargas transaccionales y analíticas:** Ninguna consulta analítica impacta la base transaccional de producción. La propagación ocurre en tiempo casi real ($< 60$ s) mediante Debezium Change Data Capture (CDC) y Apache Kafka hacia el repositorio analítico (Delta Lake / réplica analítica).
- **Soporte al modelo de costeo con desfase de combustible (40 días):** La entidad \texttt{costo_viaje} implementa versionamiento semántico auditable:

- \textit{Versión 1 ($\le 24$ h tras cierre del viaje):} Costo preliminar trazable que consolida costos directos conocidos (tarifa del flete, peajes estimados, combustible inferido por odómetro/CANbus) e identifica explícitamente los componentes pendientes de liquidación.
- \textit{Versión 2 (Conciliación a 40 días):} Actualización automática al ingresar el archivo de liquidación mensual de estaciones de servicio (Enex/Copec) y peajes, generando una nueva versión auditada sin sobreescribir la historia previa.


![Construcción del costo real por kilómetro con fuentes de distinto desfase](Costo.pdf)

*Figura. Construcción del costo real por kilómetro con fuentes de distinto desfase*


Ese diseño responde a la razón por la que el problema existe. El combustible llega con 40 días de desfase, los peajes se liquidan mensualmente y las tarifas de terceros son contractuales. Esperar a que todo esté disponible convierte el costo por viaje en un cierre contable tardío, y esa demora es la que permitió que un contrato operara cuatro años a menos 14 por ciento sin que nadie lo advirtiera.

## Bibliografía

Dirección del Trabajo. (2009). *Resolución Exenta N.º 1213. Sistema obligatorio de control de asistencia, horas de trabajo y descanso para conductores de vehículos de carga terrestre interurbana*.

Ministerio del Trabajo. (2003). *Decreto con Fuerza de Ley N.º 1. Texto refundido del Código del Trabajo. Artículo 25 bis*. Biblioteca del Congreso Nacional de Chile. https://www.bcn.cl/leychile/navegar?idNorma=207436

Escuela de Informática PUCV. (2026a). *Bases Administrativas. Licitación Pública Internacional N.º TFEP-01/2026* (FEP01.26).

Escuela de Informática PUCV. (2026b). *Bases Técnicas Transversales* (FEP02.26).

Escuela de Informática PUCV. (2026c). *Bases Técnicas del Caso 10. Transporte de Carga* (FEP03.10.26).

FMS Standard. (2025). *Technical Specification rFMS vehicle data version 5.0.0*. https://www.fms-standard.com

Iridium Communications. (2024). *Iridium Short Burst Data Service Developers Guide*.

ISO. (2011). *ISO/IEC 27031*. ISO. (2013). *ISO 16290. Definition of the Technology Readiness Levels (TRLs) and their criteria of assessment*. ISO. (2017). *ISO 15005. Road vehicles — Ergonomic aspects of transport and information and control systems*. ISO. (2019). *ISO 9241-210. Ergonomics of human-system interaction*. ISO. (2019). *ISO 22301*. ISO. (2022). *ISO/IEC/IEEE 42010*. ISO. (2023). *ISO 14083*.

Federal Motor Carrier Safety Administration [FMCSA]. (2020). *Commercial Motor Vehicle Driver Fatigue, Long-Term Health, and Highway Safety: Research Needs*. The National Academies Press. https://doi.org/10.17226/21921

Microsoft. (2025). *Azure geographies. Chile Central region*.

Congreso Nacional de Chile. (2002). *Ley N.º 19.799 sobre documentos electrónicos, firma electrónica y servicios de certificación de dicha firma*. https://www.bcn.cl/leychile/navegar?idNorma=196640

Congreso Nacional de Chile. (2021). *Ley N.º 21.377 que sanciona como infracción gravísima la conducción de vehículos manipulando dispositivos de telefonía móvil o cualquier otro artefacto electrónico («Ley No Chat»)*. https://www.bcn.cl/leychile/navegar?idNorma=1166014

Congreso Nacional de Chile. (2024). *Ley N.º 21.719 que regula la protección y el tratamiento de los datos personales y crea la Agencia de Protección de Datos Personales*. Diario Oficial de 13 de diciembre de 2024. https://www.bcn.cl/leychile/navegar?i=1209272

Ministerio de Transportes. (1995). *Decreto Supremo N.º 298*.

Ministerio del Trabajo. (2006). *Ley N.º 20.123 sobre trabajo en régimen de subcontratación*.

NFPA. (2022). *NFPA 2001*. NIST. (2014). *NIST SP 800-88 Rev. 1*.

Smart Freight Centre. (2023). *GLEC Framework, version 3.0*.

Webfleet Solutions. (2025). *WEBFLEET SAT. Ficha técnica del producto*.

World Wide Web Consortium. (2025). *Verifiable credentials data model v2.0*. W3C Recommendation de 15 de mayo de 2025. https://www.w3.org/TR/vc-data-model-2.0/
