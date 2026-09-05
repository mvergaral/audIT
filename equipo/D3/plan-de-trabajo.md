# Plan de Trabajo de Dupla D3 — Versión 2.0 Definitiva

**Marcel. y Martín. · Arquitectura Lógica y Datos**
Empresa Proponente: **audIT**
Licitación N.º TFEP-01/2026 · Caso 10: Transporte de Carga (Transportes Curimón S.A.)
Taller de Formulación de Proyectos Informáticos (ICI-5444) · Escuela de Informática · PUCV

---

## Ficha del Proceso y Alcance D3

| Parámetro                                | Definición Contractual y Académica                                                                                                                                                                                                  |
| ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Empresa Proponente**              | **audIT** (escrito según asignación oficial)                                                                                                                                                                                  |
| **Integrantes Dupla 3**             | **Martín .** (Arquitectura Lógica, Integración, BI/Analítica)**Marcel.** (Modelo de Dominio, Persistencia, Migración, Retención)                                                                                    |
| **Subdocumentos Asignados**         | **Subdoc. 4.1**: Arquitectura lógica (**16 %**)**Subdoc. 5**: Modelo y gestión de datos (**11 %**)**Subdoc. 13**: Innovación Tipo 3 (Tecnológica / Arquitectura, **17 %** cartera compartida) |
| **Ponderación Total Directa**      | **27 %** de la Oferta Técnica en el Informe 1 (la dupla con mayor peso técnico relativo) + 1 Ficha T-19                                                                                                                       |
| **Hito Entrega Simulación (T-20)** | **Lunes 07-09-2026** (Cierre formal según Formulario T-20 de las Bases Administrativas)                                                                                                                                        |
| **Hito Entrega Académica (Curso)** | **Lunes 21-09-2026** (Entrega informe 10 a 15 páginas y presentación, según programa ICI-5444)                                                                                                                               |
| **Presentación Preparatoria 1**    | Entre el**14-09-2026** y el **25-09-2026** (15 min de exposición + 15 min de preguntas, Art. 45°)                                                                                                                       |
| **Regla de Oro Interna**            | **Reparto explícito para que Martín no toque una base de datos** (`asignacion-duplas.md`). Co-responsabilidad y revisión cruzada obligatoria en todos los entregables.                                                     |

---

## 1. Objetivos del Trabajo de D3

1. Desarrollar íntegramente el **Subdocumento 4.1 (Arquitectura Lógica y Esquema de Solución)** conforme a la norma **ISO/IEC/IEEE 42010**, garantizando una arquitectura híbrida desacoplada, sin estado (*stateless*) en servicios de negocio, modular y altamente resiliente, con su respectivo Registro de Decisiones de Arquitectura (**ADR**, RT-02.04).
2. Diseñar la **Capa de Integración e Interoperabilidad** mediante estándares abiertos (**OpenAPI 3.1** para síncronos y **AsyncAPI 2.6** para eventos, RT-05.16), autenticación M2M robusta (**OAuth 2.1 / mTLS**, RT-05.18), e implementando una **Capa Anticorrupción (ACL)** que aísle el ERP contable de 2013 (RT-02.14, RT-05.20 y Consulta Oficial N.° 13).
3. Estructurar la **Capa Analítica e Inteligencia de Negocio (BI)** resolviendo la separación física/lógica con el almacenamiento transaccional (RT-05.05), habilitando autoservicio para Finanzas (RT-05.27) y entregando el modelo para calcular el **Costo Real por Kilómetro por Ruta en ≤ 24 horas**, manejando componentes desfasados (combustible a 40 días, peajes mensuales) para la **Etapa 1** (RT-05.29, Consulta Oficial N.° 18 y Decisión 17).
4. Desarrollar íntegramente el **Subdocumento 5 (Modelo y Gestión de Datos)**: modelo de dominio (RT-02.13), diccionario de datos con clasificación de sensibilidades (RT-05.01), gestión de datos maestros (**MDM**, RT-05.09), justificación de persistencia bajo el **Teorema CAP** (RT-05.02) y auditoría inalterable con valores antes/después (RT-05.03, RT-16.06).
5. Planificar el **Saneamiento y Migración de Datos Históricos**: estrategia integral para las **~6.000 vigencias vivas** distribuidas en cuatro planillas heredadas con **verificación documental individual**, maestros de flota/clientes y 2 ensayos completos en Preproducción (RT-05.11 a RT-05.15, Consulta Oficial N.° 21).
6. Formalizar la **Política de Retención, Archivado y Eliminación Segura** por dominios conforme a los plazos legales del caso (siniestros 10a, DTE/liquidaciones 6a, jornada 5a, tiempos en cliente 3a, telemetría 2a en línea, RT-05.10) y la seguridad de datos personales con **cifrado a nivel de campo** bajo la Ley N.° 21.719 (RT-11.10).
7. Formular la **Ficha T-19 de Innovación Tipo 3 (Tecnológica / Arquitectura)**: *"Operación desconectada 72 h y unificación de las tres plataformas GPS"*, cumpliendo los 7 elementos del Artículo 29° con fuentes citadas en **norma APA 7.ª ed.**, y coordinando con D4 el buffer de almacenamiento y la tolerancia a fallos RAID (RT-03.14).

---

## 2. Matriz Maestra de Entregables D3

| Código         | Entregable / Artefacto                                              | Subdoc.       | Requisitos Base                              | Líder  | Revisor        | Cierre | Estado        |
| --------------- | ------------------------------------------------------------------- | ------------- | -------------------------------------------- | ------- | -------------- | ------ | ------------- |
| **D3-01** | Diagrama y Memoria de Arquitectura Lógica (8 Capas)                | 4.1           | RT-02.01, RT-02.02, ISO/IEC/IEEE 42010       | Martín | Marcel         | 04-09  | En curso      |
| **D3-02** | Registro de Decisiones de Arquitectura (ADR inicial)                | 4.1           | RT-02.04, Art. 19°                          | Martín | Marcel         | 04-09  | En curso      |
| **D3-03** | Diseño de Resiliencia y Servicios de Negocio Stateless             | 4.1           | RT-02.05, RT-02.08, RT-09.01                 | Martín | Marcel         | 05-09  | Pendiente     |
| **D3-04** | Especificación de Integración, APIs y Capa Anticorrupción        | 4.1           | RT-05.16–21, RT-02.14, Consultas 13, 17     | Martín | Marcel         | 05-09  | Pendiente     |
| **D3-05** | Modelo de Capa Analítica y Costeo por Km/Ruta (BI)                 | 4.1 / 5       | RT-05.25–30, Consulta 18, Decisiones 15, 16 | Martín | Marcel         | 05-09  | Pendiente     |
| **D3-06** | Inventario de Componentes Lógicos (para Emplazamiento D4)          | 4.1 / 4.2     | RT-03.01–24, Art. 16°, Formulario T-11     | Martín | Alonso (D4)    | 04-09  | Bloqueante D4 |
| **D3-07** | Modelo de Dominio del Negocio y Entidades Principales               | 5             | RT-02.13, FEP03 Cap. 4 y 14                  | Marcel  | Martín        | 04-09  | En curso      |
| **D3-08** | Diccionario de Datos, Sensibilidades y Datos Maestros (MDM)         | 5             | RT-05.01, RT-05.09, ISO 25012                | Marcel  | Martín        | 05-09  | Pendiente     |
| **D3-09** | Matriz de Persistencia y Justificación Teorema CAP                 | 5             | RT-05.02, T-7 Subdoc. 5                      | Marcel  | Martín        | 04-09  | En curso      |
| **D3-10** | Modelo Transaccional, Trazabilidad y Auditoría Inalterable         | 5             | RT-05.03, RT-16.06, RT-16.07                 | Marcel  | Martín        | 05-09  | Pendiente     |
| **D3-11** | Estrategia de Desempeño: Indexación, Partición y Caché          | 5             | T-7 Subdoc. 5, RT-09.02                      | Marcel  | Martín        | 05-09  | Pendiente     |
| **D3-12** | Plan de Migración, Saneamiento y Ensayos de Preproducción         | 5             | RT-05.11–15, Consulta 21, Decisión 18      | Marcel  | Martín        | 05-09  | Pendiente     |
| **D3-13** | Política de Retención, Cifrado Ley 21.719 y Reversibilidad        | 5             | RT-05.06–10, RT-11.10, Art. 85°            | Marcel  | Martín        | 05-09  | Pendiente     |
| **D3-14** | Ficha T-19 Innovación Tipo 3 (Desconexión 72h / Unificación GPS) | 13            | Art. 28°, 29°, RT-26.01–08, APA 7         | Ambos   | Ambos          | 06-09  | Pendiente     |
| **D3-15** | Tablas de Coordinación RT-03.13 (Offline) y RT-07.13 (Backup)      | 4.1 / 5 / 4.2 | RT-03.13, RT-07.13, RT-03.14                 | Ambos   | Ignacio V (D4) | 05-09  | En curso      |
| **D3-16** | Guión de Exposición y Preparación de Defensa (Art. 45°)         | Presentación | Art. 45°, Formulario T-22                   | Ambos   | Ambos          | 06-09  | Pendiente     |

---

## 3. Asignación Detallada por Integrante

### Martín. — Arquitectura Lógica, Integración y BI (Subdocumento 4.1)

*Foco: Definir cómo se organizan y comunican los componentes de software, cómo interactúan con sistemas legados y externos, y cómo se extrae valor analítico operativo en tiempo y forma.*

1. **Arquitectura Lógica Multicapa (RT-02.01 a RT-02.04):**

   - Diseñar el diagrama de arquitectura lógica propio del caso cubriendo las **8 capas de referencia**:
     1. *Presentación*: Portal Web (React/Next), App Móvil Flutter (operable con guantes en cabina), Terminales de torre y taller.
     2. *Borde y Exposición*: Azure Front Door / WAF gestionado, protección anti-DDoS L3-L7, terminación TLS 1.3.
     3. *Puerta de Enlace (API Gateway)*: Azure API Management para cuotas, límites de tasa, versionado semántico y validación de esquemas JSON/OpenAPI.
     4. *Servicios de Negocio*: Microservicios en contenedores (Azure Kubernetes Service o Azure Container Apps) organizados por límites de contexto (*bounded contexts*): Despacho/Tráfico, Gestión de Flota, Monitoreo de Jornada, Gestión Documental, Liquidaciones, Contratos/Tarifas.
     5. *Integración y Eventos*: Event-driven architecture con Azure Event Hubs / Kafka para ingestión masiva de telemetría y Azure Service Bus para mensajería transaccional empresarial con colas de mensajes fallidos (*Dead-Letter Queues*).
     6. *Capa de Datos*: Políglota (SQL para transaccional, Time-series para GPS, Blob Storage para e-Docs, Lakehouse para BI).
     7. *Seguridad Transversal*: Azure Key Vault, Azure Entra ID (OAuth 2.1 / OIDC), auditoría criptográfica.
     8. *Observabilidad Transversal*: OpenTelemetry con Azure Monitor y Application Insights sin puntos ciegos en nube ni terminales.
   - Formalizar la descripción arquitectónica bajo el estándar **ISO/IEC/IEEE 42010** en sus vistas: lógica, de procesos, de datos, de integración y de seguridad.
   - Elaborar el **Registro de Decisiones de Arquitectura (ADR)** con las alternativas evaluadas, descartadas y criterios de selección para cada elección técnica.
2. **Resiliencia Extrema y Servicios Sin Estado (RT-02.05 a RT-02.10):**

   - Garantizar que la capa de servicios de negocio sea **100 % sin estado (stateless)**, delegando estados de sesión y workflow a almacenes externos distribuidos de alta disponibilidad (Redis Enterprise / Azure Cache).
   - Diseñar los patrones de resiliencia obligatorios (RT-02.08):
     * **Time-outs explícitos**: Prohibida taxativamente cualquier llamada remota sin tiempo límite declarado.
     * **Cortacircuitos (Circuit Breakers)** y mamparos (*bulkheads*) para aislar fallas en integraciones externas.
     * **Reintento exponencial con variación aleatoria (*jitter*)**.
     * **Idempotencia estricta en escrituras** con claves de idempotencia y ventana de deduplicación documentada (RT-02.06).
3. **Capa de Integración e Interoperabilidad (RT-05.16 a RT-05.24):**

   - Documentar contratos síncronos en **OpenAPI 3.1** y flujos dirigidos por eventos en **AsyncAPI 2.6+**, generados automáticamente desde el código.
   - Diseñar la seguridad M2M mediante **OAuth 2.1** (Client Credentials Grant) o autenticación mutua TLS (**mTLS**). Prohibición absoluta de API keys en URL.
   - **Capa Anticorrupción (ACL, RT-02.14, RT-05.20 y Consulta N.° 13)**: Sustituir los módulos operativos de 2013 (tráfico, despacho, tarifas, liquidación) y encapsular el ERP contable existente, interactuando únicamente vía API para la emisión de DTE tributario y asientos contables.
   - Diseñar la ingestión desacoplada de fuentes externas desfasadas (Consulta N.° 17): portal de combustible (archivos mensuales) y dispositivos de peaje/TAG (archivos mensuales), preparados para evolucionar a APIs diarias.
   - Integración con la telemetría CANbus/FMS inactiva de los 61 tractocamiones propios mediante conectores de solo lectura en protocolo estándar SAE J1939 sin vulnerar garantías de fábrica (Restricción 6 y Consulta N.° 14).
4. **Capa Analítica e Inteligencia de Negocio (RT-05.25 a RT-05.30):**

   - **Separación absoluta** entre procesamiento transaccional (OLTP) y analítico (OLAP) mediante réplicas de lectura y arquitectura Lakehouse / Data Warehouse para evitar cualquier degradación operacional (RT-05.05).
   - **Modelo de Costeo Real por Kilómetro y por Ruta (Decisiones 15, 16, 17 y Consulta N.° 18)**:
     * Resolver la latencia de negocio: emitir el **costo consolidado preliminar del viaje en ≤ 24 horas** tras su cierre, indicando explícitamente los componentes pendientes y actualizándose automáticamente con historial de versiones a medida que ingresan peajes y combustible a 40 días.
     * Diseñar el algoritmo de costeo para camiones subcontratados donde solo se dispone de la tarifa pactada y anticipos de combustible.
     * Asegurar que el costeo analítico esté disponible en la **Etapa 1**, previo a la renegociación contractual de 2027 donde dos contratos pierden plata sistemáticamente.
   - Proveer herramienta de autoservicio con **modelo semántico documentado** (Power BI Embedded / Semantic Layer) para que Finanzas cree tableros con *drill-down* hasta la transacción individual sin requerir soporte TI (RT-05.27).
5. **Inventario Lógico para la Dupla D4 (RT-03 / Formulario T-11):**

   - Entregar a D4 la lista exhaustiva de componentes lógicos clasificados por latencia, criticidad, volumen, regulación, conectividad y justificación de emplazamiento (Nube vs. San Bernardo vs. Terminales Regionales vs. Camiones On-Premise).

---

### Marcel. — Modelo de Dominio, Persistencia y Migración (Subdocumento 5)

*Foco: Diseñar dónde y cómo residen los datos, su consistencia y transaccionalidad, la limpieza de los datos heredados y el cumplimiento normativo estricto.*

1. **Modelo de Dominio y Datos Maestros (RT-02.13, RT-05.01, RT-05.09):**

   - Modelar el dominio del negocio (DDD): Agregados y entidades principales (*Viaje, Tramo, OrdenDeTransporte, Conductor, Tractocamion, Semirremolque, PropietarioTransportista, Tarifa, EventoJornada, Geocerca, Liquidacion, Siniestro*).
   - Elaborar el **Diccionario de Datos** exhaustivo con tipo, rango de valores, obligatoriedad, propietario del dominio y nivel de sensibilidad (RT-05.01).
   - Diseñar la estrategia de **Gestión de Datos Maestros (MDM)** para unificar y evitar duplicidad de conductores, camiones y clientes entre la nueva solución y el ERP legado (RT-05.09).
2. **Matriz de Persistencia Políglota y Teorema CAP (RT-05.02):**

   - Justificar formalmente la posición en el Teorema CAP y el motor seleccionado para cada dominio:
     * *Transaccional Crítico (Despacho, Asignación, Viajes, DTE, Liquidaciones)*: **RDBMS Relacional** (Azure Database for PostgreSQL Flexible Server o SQL Server). Enfoque **CP/CA** (Consistencia estricta, ACID, transaccionalidad total).
     * *Series Temporales de Telemetría y Posición GPS*: **Time-Series / NoSQL Distribuido** (Azure Cosmos DB o TimescaleDB / Azure Data Explorer). Enfoque **AP** (Alta disponibilidad, particionamiento masivo horizontal, consistencia eventual).
     * *Buffer Local a Bordo (Dispositivo 374 camiones)*: **SQLite embebido / Realm / RocksDB**. Tolerancia a 72h offline con almacenamiento local cifrado en disco.
     * *Repositorio Documental (e-Docs, guías firmadas, fotos de siniestros)*: **Object Storage** (Azure Blob Storage con inmutabilidad WORM).
3. **Auditoría Inalterable y Trazabilidad (RT-05.03, RT-16.06, RT-16.07):**

   - Diseñar bitácora de auditoría inmutable que capture para cada operación de escritura: identificador de transacción, usuario/dispositivo, marca de tiempo, dirección IP, valores anteriores y valores posteriores (*CDC - Change Data Capture*).
   - Garantizar inalterabilidad absoluta de los registros de jornada y asignación frente a administradores mediante almacenamiento protegido contra borrado o encadenamiento criptográfico (*Append-only Ledger*), blindando a Curimón ante juicios laborales o reclamos de seguros (Criterio de Aceptación 4).
4. **Estrategia de Desempeño de Base de Datos (Formulario T-7 Subdoc. 5):**

   - Definir estrategia de indexación B-Tree para claves foráneas y búsquedas transaccionales, índices GiST/SP-GiST para consultas geoespaciales de geocercas (PostGIS).
   - Particionamiento horizontal de tablas históricas de viajes y telemetría por rango de fecha (mensual/anual).
   - Estrategia de caché de baja latencia con Redis para sesiones operacionales, datos maestros de lectura intensiva y validación de vigencias en portería.
5. **Plan de Saneamiento y Migración de Datos Históricos (RT-05.11 a RT-05.15 y Consulta N.° 21):**

   - Planificar el perfilamiento, limpieza y migración de las **~6.000 vigencias vivas** (licencias, revisiones técnicas, certificados de gases, seguros, cursos de cargas peligrosas) dispersas en 4 planillas Excel independientes.
   - Diseñar el protocolo de **verificación documental individual obligatoria** (contrastar cada fila de planilla contra el documento digital/físico escaneado durante la migración, RT-05.15).
   - Definir las reglas de transformación ETL/ELT, reportes de excepciones y plan de reversión (*rollback*).
   - Comprometer formalmente **al menos 2 ensayos completos de migración** en ambiente de Preproducción antes de la salida en vivo (RT-05.13) con conciliación cuantitativa verificable mediante sumas de control (*checksums*) y recuentos (RT-05.14).
   - Migración histórica completa de maestros de flota/clientes, 5 años de viajes, 6 años de liquidaciones y 100 % de antecedentes de siniestros.
6. **Política de Retención Legal y Cifrado Ley 21.719 (RT-05.07, RT-05.10, RT-11.10):**

   - Codificar en base de datos las políticas automáticas de retención y purga segura:
     * *10 años*: Antecedentes de siniestros.
     * *6 años*: Documentos tributarios (DTE) y liquidaciones a transportistas.
     * *5 años*: Registros y evidencia de jornada de conducción (normativa laboral) y cargas peligrosas.
     * *Vigencia + 5 años*: Habilitaciones de conductores y tractocamiones/semirremolques.
     * *3 años*: Tiempos de permanencia en instalaciones de clientes (respaldo de sobreestadías).
     * *2 años en línea*: Series de posición y telemetría (posteriormente agregadas y archivadas en frío).
   - **Cifrado a nivel de campo obligatorio (RT-11.10)**: Aplicar llaves gestionadas en HSM para datos sensibles de los 258 conductores subcontratados (RUT, teléfonos, antecedentes médicos/licencias), coordenadas GPS asociadas a personas identificables y tarifas individuales pactadas con los 148 dueños de camiones.
   - **Reversibilidad y Formatos Abiertos (RT-05.06)**: Asegurar mecanismos nativos de exportación completa en formatos abiertos (JSON, CSV, Parquet) sin costo ni dependencia de proveedor al término del contrato.

---

## 4. Trabajo Conjunto: Innovación Tipo 3 (Subdocumento 13 / Ficha T-19)

**Responsables:** Marcel . y Martín.
**Tema Asignado:** *"Operación desconectada 72 h y unificación de las tres plataformas GPS"*
**Ponderación:** 17 % de la cartera de 5 innovaciones en el Informe 1 (Formulario T-21 y Consulta N.° 2).

### Desarrollo de los 7 Elementos Obligatorios del Artículo 29°:

1. **Problema y Oportunidad Concreta:**

   - *Dimensión real del problema*: 41 millones de km anuales con tramos de más de 80 km sin cobertura celular en la Ruta 5 Norte/Sur y pasos cordilleranos (Paso Los Libertadores con cierres por nieve de hasta 12 días continuos, ~1.900 cruces anuales).
   - *Fragmentación telemática*: Flota de 374 camiones donde 34 no tienen GPS, y los 340 restantes se dividen en 3 plataformas comerciales incompatibles contratadas por terceros (dos de ellas con acceso exclusivo de consulta web y una que no permite exportación por API).
   - *Impacto*: Ceguera operativa, pérdida de eventos de jornada y sobreestadías no cobradas por falta de sellos de tiempo continuos.
2. **Tecnología que la Sustenta:**

   - *Arquitectura Edge-to-Cloud con Store-and-Forward tolerante a partición de red*: Almacenamiento local estructurado a bordo (SQLite embebido cifrado con SQLCipher / AES-256) con capacidad de retención de hasta 120 horas de series de tiempo comprimidas en protocolo Protocol Buffers (Protobuf).
   - *Capa de Ingestión Telemática Unificada*: Conectores adaptadores multifuente en la nube (API scraping gobernado, ingestión síncrona/asíncrona y webhooks) combinados con una App Móvil con geolocalización autónoma para los 34 camiones sin GPS hardware, normalizando todo evento bajo el estándar sectorial telemático.
   - *Emisión de DTE Tributario en Sombra*: Pre-asignación de folios CAF autorizados por el SII en memoria protegida del dispositivo a bordo, permitiendo emitir la guía de despacho electrónica firmada localmente en puntos de carga sin señal y sincronizando al ERP contable tras la reconexión (Consulta N.° 15).
3. **Nivel de Madurez Tecnológica (TRL) y Citas APA 7.ª Edición:**

   - Nivel de Madurez **TRL 8/9** (tecnologías probadas en entornos operacionales reales de transporte y minería).
   - Justificación teórica rigurosa citando marcos de sincronización distribuida (Conflict-free Replicated Data Types - CRDTs), protocolos de transporte IoT (MQTT v5.0 / CoAP) y estándares de bases de datos embebidas resilientes conforme a fuentes académicas e industriales en formato APA 7.
4. **Diseño de Incorporación y Trazabilidad en Arquitectura:**

   - *Ubicación en la Arquitectura*: Inserta en la Capa 1 (Dispositivo embarcado / App móvil), Capa 5 (Event Ingestion / Broker) y Capa 6 (Time-series Storage).
   - *Procedimiento de Sincronización Determinista (RT-03.12 y RT-03.13)*: Reconciliación basada en marcas temporales de reloj GPS confiable (*monotonic clock*), resolución determinista de conflictos sin pérdida de integridad y tiempo de sincronización total ≤ 20 minutos por camión.
   - *Capacidad ante Reconexión Simultánea*: Diseño de cola elástica en Azure Event Hubs capaz de absorber la ráfaga concurrente de más de 300 camiones saliendo simultáneamente de zonas de sombra sin degradar la torre.
   - *Declaración Explícita de Funciones NO Disponibles en Modo Desconectado (RT-03.13)*:
     * No disponible: Notificaciones en tiempo real al cliente final, asignación de nuevos viajes no pre-cargados, consulta interactiva de liquidaciones.
     * Procedimiento manual supletorio documentado para evitar observaciones graves.
   - *Hardware On-Premise y RAID (RT-03.14)*: Declaración de tolerancia a falla de al menos 1 disco (RAID-1 en nodos de borde de terminales y flash industrial con wear-leveling en cabina).
5. **Impacto Económico Preliminar (Informe 1):**

   - Estimación paramétrica de inversión en licencias/desarrollo de conectores vs. ahorro en penalizaciones contractuales por pérdida de señal, reducción de horas-hombre en torre de control y recupero de sobreestadías (Consulta Oficial N.° 5: estimación conceptual en Informe 1; flujo de caja valorizado en Informe 3).
6. **Indicadores de Verificación del Beneficio:**

   - *Línea Base*: 0 % de camiones con trazabilidad continua en zonas de sombra; 3 plataformas aisladas; 34 camiones sin visibilidad.
   - *Meta*: 100 % de eventos de viaje y jornada recuperados tras 72 h sin pérdida de paquetes; 100 % de la flota visible en una única torre de control; latencia de sincronización < 15 min. Momento de medición: Marcha blanca Etapa 1 (Mes 12 a 15).
7. **Riesgos de Adopción, Probabilidad, Impacto y Mitigación:**

   - *Riesgo*: Negativa de un proveedor GPS externo a facilitar acceso de scraping/datos. (Probabilidad: Media, Impacto: Alto).
   - *Mitigación / Contingencia*: Activación del tracking telemático de respaldo mediante la App móvil del conductor (desarrollada con geocercas automáticas) durante el viaje activo de Curimón, independizándose del proveedor del transportista.

---

## 5. Mapeo y Resolución de las 26 Decisiones del Caso (Numeral 16.1)

D3 asume la fundamentación técnica y formalización de supuestos para las **16 decisiones** que impactan arquitectura, datos e integraciones:

| N.°         | Decisión Pendiente del Caso 10                                            | Tratamiento y Supuesto Arquitectónico / Persistencia en D3                                                                                                                                       |
| ------------ | -------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1**  | Obtención y acreditación de jornada de conductores externos              | Registro inalterable con sellos de tiempo criptográficos, firma electrónica en App móvil y consulta bloqueante previa al despacho (RT-02.13, RT-05.01, RT-16.14).                              |
| **3**  | Destino del sistema de gestión de transporte de 2013                      | Sustitución integral de módulos operativos de 2013 mediante Capa Anticorrupción (ACL); ERP contable se preserva vía API para facturación/DTE (RT-02.14, Consulta 13).                        |
| **4**  | Unificación de 3 GPS externos y 34 camiones sin hardware                  | Capa de ingestión telemática multicanal en la nube + App móvil con geolocalización de respaldo en viajes activos para unidades sin dispositivo (Innovación Tipo 3).                          |
| **8**  | Registro de llegada/salida en porterías de clientes sin instalar hardware | Geocercas virtuales telemáticas de alta precisión (±15 m) con marca temporal GPS certificada y registro automático de entrada/salida sin intervención humana (Restricción 9).               |
| **9**  | Emisión de DTE tributario en puntos de carga sin cobertura celular        | Pre-foliado de contingencia autorizado por SII (Res. Ex. N.° 107/2014) con stock de folios CAF en memoria segura de cabina y sincronización diferida (Consulta 15).                             |
| **11** | Frecuencia de muestreo de posición y telemetría a bordo                  | Frecuencia adaptativa: 30 s en movimiento con cobertura, 5 min en ralentí/detención, compresión y almacenamiento en buffer local ante pérdida de enlace (Decisión conjunta con D4).          |
| **12** | Telemetría de fábrica inactiva en 61 tractocamiones propios              | Integración de solo lectura mediante lector inductivo en puerto FMS/CANbus (SAE J1939) sin vulnerar garantías de motor (Restricción 6, Consulta 14).                                           |
| **13** | Descarga y conservación de datos de tacógrafo digital                    | Protocolo de descarga física/remota periódica en terminales con almacenamiento inmutable por 5 años conforme a normativa de transporte (RT-05.10).                                             |
| **15** | Construcción del costo del viaje con desfases extremos                    | Capa analítica con costo preliminar trazable en ≤ 24 h, declarando componentes pendientes y actualizando automáticamente con historial de versiones ante combustible a 40 días (Consulta 18). |
| **16** | Estimación del costo real de camiones subcontratados                      | Algoritmo analítico de imputación basado en tarifa contractual, incentivos por tramo, peajes reales e imputación de combustible anticipado.                                                    |
| **17** | Información de los 3 contratos bajo costo antes de 2027                   | Despliegue prioritario de la capa analítica de rentabilidad de rutas en la**Etapa 1** para respaldar la renegociación contractual temprana.                                               |
| **18** | Control y vigencia de las ~6.000 fechas de vencimiento                     | Módulo de vigencias con motor de alertas escalonadas (60, 30, 7 días) y verificación documental individual durante la migración (RT-05.15, RT-16.21, Consulta 21).                            |
| **20** | Gestión ante cierre de 12 días por nieve en Los Libertadores             | Buffer local extendido a bordo, preservación de estados en repositorios locales y sincronización determinista masiva al habilitarse el paso sin saturar enlaces.                                |
| **22** | Cálculo de emisiones CO2e/ton-km para flota propia y terceros             | Motor analítico bajo estándar GLEC Framework / ISO 14083 con datos directos CANbus en flota propia y factores ponderados en terceros con consolidación mensual (RT-05.29, Consulta 12).        |
| **23** | Consentimiento granular y revocable sobre datos compartidos                | Portal del transportista con matriz de permisos por camión/viaje, registro de auditoría de accesos a datos de localización y cumplimiento Ley 21.719 (RT-16.09, RT-16.30).                     |
| **24** | Inalterabilidad y protección de la evidencia de jornada                   | Base de datos relacional con firmas hash encadenadas y almacenamiento inmutable (WORM) para impedir manipulación por parte de la empresa o conductores (RT-05.03).                               |

---

## 6. Sincronizaciones e Interfaces Inter-Duplas

```
               ┌────────────────────────────────────────────────────────┐
               │              D1: Empresa y Problema                    │
               │  Dolores priorizados · Magnitud cuantitativa del caso  │
               └──────────────────────────┬─────────────────────────────┘
                                          │ Entregables D1
                                          ▼
┌───────────────────────────────────────────────────────────────────────────────────────┐
│                           D2: Esquema de Solución y Alcance                           │
│  Catálogo RF/RNF (D2-02) · Alcance por Etapas (D2-05) · Plan de Adhesión (D2-06)       │
└──────────────────┬─────────────────────────────────────────────────┬──────────────────┘
                   │ Requisitos y Alcance                            │ Requisitos
                   ▼                                                 ▼
┌──────────────────────────────────────┐          ┌─────────────────────────────────────┐
│    D3: Arquitectura Lógica y Datos   │          │  D4: Arquitectura Física e Infraest.│
│  (Martín y Marcel · 27 % + Ficha T19)│◄────────►│  (Ignacio V y Alonso · 16 % + T19)  │
│  · Diagrama Lógico 8 Capas (D3-01)   │ Emplaza- │  · Emplazamiento Componentes (T-11) │
│  · Capa de Integración & ACL (D3-04) │ miento y │  · Dispositivo a Bordo 374 Camiones │
│  · Capa Analítica BI & Costos (D3-05)│ Offline  │  · Redes, Enlaces y Data Centers    │
│  · Modelo Datos & Persistencia(D3-07)│ S4 04-09 │  · Costo Datos Móviles & Ancho Banda│
└──────────────────────────────────────┘          └─────────────────────────────────────┘
```

### Protocolo de Intercambio con las demás Duplas:

1. **Lo que D3 recibe de D1 y D2:**

   - De D1: Matriz de actores afectados, datos cuantitativos consolidados (los 3 contratos bajo costo, los $340M en esperas con 71 % objetado, los 142 pesajes viales).
   - De D2: Catálogo de requerimientos RF/RNF versión 1, delimitación de alcance Etapa 1 vs. Etapa 2, y el plan de adhesión de los 148 transportistas.
2. **Lo que D3 entrega a D4 (Hito Crítico de Sincronización S4 — Viernes 04-09):**

   - **Inventario de Componentes Lógicos (D3-06)**: Lista normalizada de módulos, microservicios, bases de datos y brokers requeridos para que D4 pueda completar la **Tabla de Emplazamiento del Formulario T-11**.
   - **Tabla Conjunta RT-03.13**: Definición acordada de las funciones que NO estarán disponibles en modo desconectado y el procedimiento manual de respaldo.
   - **Tabla Conjunta RT-07.13**: Definición de frecuencia de respaldo, retención, RPO y RTO por cada dominio de datos.
   - **Parámetros de Telemetría**: Definición del tamaño del paquete de datos comprimido y volumen acumulado a bordo en 72 horas para el cálculo de memoria física y costo de SIMs de D4.

---

## 7. Criterios de Aceptación del Caso que D3 Resuelve

D3 es responsable directo de garantizar la viabilidad técnica y contractual de los siguientes criterios del Capítulo 18 (FEP03 p.41):

- **Criterio 1**: Ningún camión sale sin conductor con jornada disponible, habilitación vigente o equipo apto (Validación lógica bloqueante en ≤ 30 s, RT-09.01).
- **Criterio 3**: Jornada previa de conductor de tercero disponible al asignar viaje (Modelo de datos unificado).
- **Criterio 4**: Evidencia de jornada inalterable y oponible ante autoridad laboral y seguros (Auditoría inmutable RT-05.03).
- **Criterio 5**: Las ~6.000 vigencias en registro único con alertas preventivas (Modelo de datos maestros y migración saneada).
- **Criterio 8**: Vista única de la flota de 374 camiones (Capa de ingestión telemática unificada).
- **Criterio 9**: Registro continuo de 72 horas sin cobertura sin pérdida de eventos (Innovación Tipo 3, RT-03.10).
- **Criterio 10 y 11**: Registro automático de llegada/salida en clientes y respaldo fehaciente de cobro de esperas (Geocercas criptográficas).
- **Criterio 13 y 14**: DTE emitido sin redigitación y solución conforme para emisión en puntos de carga sin cobertura (Integración ERP y contingencia CAF).
- **Criterio 16, 17 y 19**: Costo real por km/ruta disponible en ≤ 24 h tras cierre, con componentes pendientes declarados, antes de la renegociación de 2027 (Capa analítica en Etapa 1).
- **Criterio 22 y 23**: Monitoreo de carga con autorización granular y revocable por dueño de camión (Control de datos y Ley 21.719).
- **Criterio 24**: Emisiones CO2e/ton-km calculadas con metodología auditable GLEC / ISO 14083 (Módulo analítico).
- **Criterio 28 y 29**: Alerta oportuna a conductores considerando lugares de descanso seguros y portal del transportista con soberanía de datos (Decisiones que deciden el caso).

---

## 8. Estrategia de Presentación y Defensa (Art. 45° y Formulario T-22)

Las presentaciones preparatorias tienen una duración estricta de **15 minutos de exposición y 15 minutos de preguntas**, con agenda cerrada (Formulario T-22) y la regla crítica de que **el CLIENTE puede designar aleatoriamente quién expone cada sección**.

### Bloques de Exposición de D3:

1. **Bloque 1: Arquitectura Lógica y Esquema de Solución (3 min 30 s):**
   - *Mensaje central*: Demostrar cómo las 8 capas de la arquitectura resuelven la operación híbrida, el aislamiento del ERP 2013 mediante Capa Anticorrupción y la resiliencia en terreno sin llamadas remotas desprotegidas.
2. **Bloque 2: Modelo de Datos, Persistencia y Migración (3 min 00 s):**
   - *Mensaje central*: Demostrar la solidez del almacenamiento políglota (CAP), la inalterabilidad de la evidencia de jornada y la estrategia de saneamiento documental de las 6.000 vigencias heredadas.
3. **Bloque 3: Innovación Tipo 3 — Desconexión 72 h y GPS (Junto con D2/D4 en bloque de innovación, 2 min 00 s):**
   - *Mensaje central*: Demostrar que las 72h offline no son un slogan sino una arquitectura de sincronización determinista validada en APA 7, tolerante a fallos y capaz de unificar las 3 plataformas existentes.

### Preparación Cruzada Anti-Riesgo:

- Martín y Marcel realizarán ensayos cronometrados con intercambio de roles: Martín debe poder defender el Teorema CAP, los plazos de retención y la migración de vigencias; Marcel debe poder defender las 8 capas lógicas, los patrones de resiliencia y el modelo analítico de costos.

---

## 9. Criterios de Término (Definition of Done D3)

- [ ] Diagrama de arquitectura lógica elaborado según ISO/IEC/IEEE 42010 cubriendo las 8 capas sin elementos genéricos.
- [ ] Registro de Decisiones de Arquitectura (ADR) con justificación técnica de alternativas escogidas y descartadas.
- [ ] Especificación de contratos OpenAPI 3.1 y AsyncAPI 2.6 con diseño de Capa Anticorrupción para ERP 2013.
- [ ] Modelo semántico analítico con resolución del costo preliminar en ≤ 24 h y soporte a desfase de combustible a 40 días.
- [ ] Inventario de componentes lógicos entregado y consensuado con D4 para la Tabla de Emplazamiento (T-11).
- [ ] Modelo de dominio (DDD) y diccionario de datos completo con sensibilidades bajo la Ley N.° 21.719.
- [ ] Matriz de persistencia con justificación del Teorema CAP por cada dominio de información.
- [ ] Plan de migración de datos con protocolo de verificación documental individual para las ~6.000 vigencias y 2 ensayos en Preproducción.
- [ ] Tabla de retención con plazos normativos (10a, 6a, 5a, 3a, 2a) y procedimiento de eliminación segura.
- [ ] Ficha T-19 de Innovación Tipo 3 completa con los 7 elementos del Art. 29°, citas APA 7.ª ed. y tabla RT-03.13.
- [ ] Coherencia cruzada absoluta con los requerimientos de D2 y la infraestructura física de D4.
- [ ] Guión de presentación ensayado por ambos integrantes dentro de los tiempos estipulados.

---

## 10. Tabla de Fuentes y Verificación Normativa

Todas las citas corresponden a la **numeración impresa al pie** de los documentos oficiales:

| Documento       | Sección / Artículo   | Pág. | Materia Clave para D3                                                                   |
| --------------- | ---------------------- | ----: | --------------------------------------------------------------------------------------- |
| **FEP01** | Artículo 16°         |    12 | Exigencias del componente on-premise y coherencia lógica-física                       |
| **FEP01** | Artículo 19°         |    14 | Arquitectura conforme a ISO/IEC/IEEE 42010                                              |
| **FEP01** | Artículos 28° y 29° |    19 | Cartera de 5 innovaciones y 7 elementos obligatorios de la Ficha T-19                   |
| **FEP01** | Artículo 45°         |    28 | Reglas de la presentación (15 min, selección aleatoria de expositores)                |
| **FEP01** | Artículo 50.2         |    29 | Prohibición absoluta de cifras de precio en Oferta Técnica (Sobre N.° 2)             |
| **FEP01** | Formulario T-7         |    57 | Índice oficial: Subdoc. 4 (Arquitectura) y Subdoc. 5 (Modelo de Datos)                 |
| **FEP01** | Formulario T-20        |    65 | Calendario oficial de actividades del proceso                                           |
| **FEP01** | Formulario T-21        |    66 | Tabla de ponderación técnica: Subdoc 4.1 (16 %), Subdoc 5 (11 %), Innovaciones (17 %) |
| **FEP01** | Formulario T-22        |    68 | Contenido específico exigido para el Informe y Presentación 1                         |
| **FEP02** | Capítulo 2 (RT-02)    |     6 | Modelo de 8 capas (2.1), resiliencia, stateless, ADR y Capa Anticorrupción             |
| **FEP02** | Capítulo 3 (RT-03)    |     8 | Operación desconectada on-premise, reconciliación y tabla RT-03.13                    |
| **FEP02** | Capítulo 5 (RT-05)    |    11 | Datos, diccionario, Teorema CAP, migración, OpenAPI/AsyncAPI y BI                      |
| **FEP02** | Capítulo 11 (RT-11)   |    21 | Cifrado a nivel de campo (RT-11.10) y seguridad de datos personales                     |
| **FEP02** | Capítulo 16 (RT-16)   |    29 | Auditoría con valores antes/después (RT-16.06) y control de accesos                   |
| **FEP02** | Capítulo 17 (RT-17)   |    31 | Aplicación móvil, periféricos (GPS) y optimización de datos móviles                |
| **FEP02** | Capítulo 26 (RT-26)   |    44 | Exigencias técnicas de las innovaciones y trazabilidad arquitectónica                 |
| **FEP03** | Capítulo 5            |    12 | Sistemas legados actuales (gestión 2013, ERP contable, portal combustible)             |
| **FEP03** | Capítulo 10           |    23 | Las 14 restricciones no negociables                                                     |
| **FEP03** | Capítulo 13           |    26 | Horizonte, prioridades y ventanas protegidas (temporada de fruta, Los Libertadores)     |
| **FEP03** | Capítulo 14           |    29 | Volumetría operacional entregada (14.1) y volumetría técnica a estimar (14.2)        |
| **FEP03** | Capítulo 15           |    31 | Parámetros del caso para requisitos "según caso" (RT-05.10, RT-05.15, RT-05.29)       |
| **FEP03** | Capítulo 16           |    34 | Las 26 decisiones de diseño pendientes                                                 |
| **FEP03** | Capítulo 18           |    41 | Los 29 criterios de aceptación del caso                                                |
| **FEP03** | Capítulo 19           |    43 | Criterios específicos de evaluación del Caso 10                                       |
