# REGISTRO DE REVISIÓN HUMANA Y CONTROL DE CALIDAD — GEN-05
**audIT Soluciones Tecnológicas SpA — Licitación TFEP-01/2026**
**Proyecto:** Sistema de Gestión Telemática, Monitoreo de Flota y Control de Jornada — Transportes Curimón S.A.
**Revisor Técnico Responsable:** Carlos Abarza (audIT / Dupla D1)
**Fecha de Emisión y Cierre:** Noviembre de 2026
**Normativa Aplicable:** Comunicado 10 (§7.1 y §7.2), Bases Administrativas (Arts. 40, 46 y 47.1), Observaciones GEN-05, CAL-03, CAL-06, INN-04 e INN-05.

---

## 1. Propósito y Alcance del Registro

El presente documento constituye el **Registro Formal de Verificación y Supervisión Humana** exigido por la observación oficial **GEN-05** y los lineamientos del Comunicado 10 (§7). Certifica la revisión exhaustiva, modificación manual, validación técnica y verificación de consistencia realizada por el revisor humano sobre los artefactos técnicos generados o asistidos por modelos de lenguaje (LLM / Codex) en el ámbito de responsabilidad de la Dupla D1 (Subdocumentos S1, S2, S9 y Formularios T-6, T-13, T-17, T-19 y económicos asociados).

El alcance de la supervisión humana cubre detalladamente:
1. **Catálogo de 120 casos de prueba** del Formulario T-17 (`catalogo-T-17.tex`), validando caso a caso las precondiciones, entradas sintéticas, pasos de ejecución, oráculos de salida y severidades P1/P2/P3.
2. **Matriz de trazabilidad de los 29 criterios de aceptación del Caso** (`trazabilidad-T-17.tex`, Tabla `9-rtm-29`), asegurando la correspondencia unívoca con el Formulario T-12 y la asignación expresa de responsables de verificación entre audIT y Transportes Curimón S.A.
3. **Matriz de trazabilidad de los 42 requerimientos de software (RF/RNF)** (`trazabilidad-T-17.tex`, Tabla `9-rtm`).
4. **Trece fichas de protocolo de aceptación vinculante** (Hitos H1 a H12 y Ficha Consolidadora de Producto Final en `protocolos-hitos-T-17.tex`), verificando plazos perentorios (Art. 18), paquetes EDT y la base de cobro preceptiva del Formulario E-25.
5. **Cartera de Innovaciones (Formulario T-19)**, específicamente la Ficha 5 (anticipación circadiana), conciliando la matriz de riesgo residual con la escala S8 y declarando como hipótesis paramétricas de ingeniería los supuestos de beneficio físico.

---

## 2. Metodología de Revisión y Criterios de Aceptación Humana

Cada artefacto asistido por IA fue sometido a un protocolo de revisión estructurado en cuatro fases:

```
[Borrador Asistido por IA] 
         ↓
(Fase 1: Análisis Semántico y Cruce Normativo) 
         ↓
(Fase 2: Verificación de Oráculos, Fixtures y Fórmulas) 
         ↓
(Fase 3: Rectificación Manual y Desacoplamiento) 
         ↓
[Aprobación Humana y Firma en Registro]
```

* **Fase 1 (Cruce Normativo y Contractual):** Cotejo directo contra Bases Administrativas (FEP01.26), Bases Técnicas Transversales (FEP02.26), Bases Técnicas del Caso (FEP03.26), Comunicado 10 y Aclaraciones oficiales. Se descartó cualquier intento de sobreajuste a ejemplos de aula o parámetros no fundamentados.
* **Fase 2 (Verificación de Oráculos y Fixtures):** Comprobación matemática y lógica de valores sintéticos, cadenas hash de integridad, tolerancias de latencia (p95, p99), matrices de compatibilidad química (NCh 382/2190) y reglas de descanso (Art. 25 bis Código del Trabajo).
* **Fase 3 (Rectificación Manual y Desacoplamiento):** Eliminación de alucinaciones, remoción de dependencias erróneas, corrección de cruces indebidos de casos de prueba y separación estricta entre obligaciones base e innovaciones incrementales.
* **Fase 4 (Aprobación y Certificación):** Consolidación en el código fuente LaTeX y registro de trazabilidad en el Anexo de Art. 46.

---

## 3. Detalle de Sesiones de Auditoría y Hallazgos Subsanados

| Sesión / Fecha | Componente Auditado | Hallazgo Inicial de IA | Acción Correctiva Humana Aplicada (Carlos Abarza) | Estado / Impacto |
| :--- | :--- | :--- | :--- | :--- |
| **Sesión 1**<br>28-Oct-2026 | Catálogo T-17:<br>120 Casos de Prueba | Fichas generadas con oráculos genéricos ("el sistema funciona correctamente") en 14 casos. | Redacción manual de oráculos deterministas: código de error HTTP/gRPC, mensajes textuales exactos, estados en BD PostgreSQL/Redis y tiempos límites de respuesta. | **Aprobado**<br>100% de los 120 casos con veredicto binario Pass/Fail. |
| **Sesión 2**<br>30-Oct-2026 | Catálogo T-17:<br>CP-HW-06 y CP-HW-08 | `CP-HW-08` aludía a polvo minero no aplicable al caso. `CP-HW-06` mezclaba activación SOS con alertas de descanso vial. | Corrección de `CP-HW-08` a estanqueidad IP67 en transporte de carga. Desacoplamiento de `CP-HW-06` (SOS) restringiéndolo a RNF-001. | **Aprobado**<br>Resuelve observación oficial CAL-02. |
| **Sesión 3**<br>02-Nov-2026 | Matriz T-17:<br>Tabla `9-rtm-29`<br>(Criterio 28) | El Criterio 28 citaba erróneamente `CP-HW-06` (ensayo SOS de hardware) para verificar paraderos seguros. Faltaban responsables de verificación. | Reemplazo de `CP-HW-06` por la terna `CP-UNIT-18`, `CP-SYS-07` y `CP-UAT-07`. Incorporación de columna con responsables técnicos de audIT y Curimón en los 29 criterios. | **Aprobado**<br>Resuelve observación oficial CAL-03. |
| **Sesión 4**<br>04-Nov-2026 | Protocolos Hitos:<br>Fichas H1 a H12 y Producto Final | Los efectos económicos de los hitos calculaban cobros sobre el "precio contractual total" con porcentajes arbitrarios (10%, 5%, etc.). | Alineación estricta contra Formulario E-25: base de cálculo fijada en el "valor total de la fase de implementación", 60% Etapa 1, 40% Etapa 2 y 36 pagos mensuales separados para operación (M21–M56). | **Aprobado**<br>Resuelve observación oficial CAL-06. |
| **Sesión 5**<br>06-Nov-2026 | Ficha 5 Innovación:<br>Formulario T-19 | Beneficios físicos expresados como hechos consumados sin respaldo empírico de flota. Matriz de riesgo residual ambigua. | Etiquetado formal de los beneficios físicos como **"hipótesis paramétricas de ingeniería"** a calibrar en marcha blanca (M13–M15). Alineación de severidad inherente 3x4 (Alta) y residual 1x3 (Baja/Aceptable) bajo escala S8. | **Aprobado**<br>Resuelve observaciones INN-04 e INN-05. |
| **Sesión 6**<br>08-Nov-2026 | Calidad S9 y T-13:<br>Quality Gates | Quality Gates sin articulación explícita con las 6 condiciones contractuales acumulativas del Art. 17.3. | Incorporación de matriz de puertas de calidad vinculadas a ambientes, branch policies (SLSA Nivel 3) y criterios perentorios de subsanación de 10 días hábiles. | **Aprobado**<br>Resuelve observación CAL-05. |

---

## 4. Auditoría Sistemática de las 7 Baterías de Ensayos (120 Casos T-17)

A continuación se certifica la revisión manual caso a caso realizada sobre cada familia de pruebas del Formulario T-17:

### 4.1 Ensayos Unitarios Automatizados (CP-UNIT-01 a CP-UNIT-25)
* **Revisión Humana:** Se verificó que los 25 casos utilicen fixtures sintéticos aislados, mocking de dependencias externas (APIs de terceros y base de datos) y ejecución determinista en runner Go Test / PyTest.
* **Casos Clave Auditados:**
  * `CP-UNIT-01` a `CP-UNIT-04`: Lógica de validación laboral de jornada según Art. 25 bis CT (límites de 5 horas continuas, descanso de 2 horas y descanso diario de 8 horas).
  * `CP-UNIT-06`: Sellado inmutable con cadenas SHA-256 de eventos de jornada.
  * `CP-UNIT-18`: Algoritmo predictivo de estimación de fatiga y proximidad a área segura (RF-027). Verificado el desacoplamiento de dispositivos físicos en la prueba unitaria.
  * `CP-UNIT-19`: Matriz de incompatibilidad química de sustancias peligrosas (D.S. 298 / NCh 2190).

### 4.2 Ensayos de Integración y Servicios (CP-INT-01 a CP-INT-25)
* **Revisión Humana:** Se validaron los contratos de datos, idempotencia de APIs, colas de mensajería asíncrona (RabbitMQ/Kafka) y manejo de fallos de red.
* **Casos Clave Auditados:**
  * `CP-INT-02` y `CP-INT-03`: Integración con padrón de conductores propios y externos, clasificando niveles de evidencia probatoria 1 a 5.
  * `CP-INT-11` y `CP-INT-12`: Integración bidireccional con TMS 2013 y ERP corporativo vía webhooks autenticados.
  * `CP-INT-21`: Protocolo de descarga remota DSRC de tacógrafos digitales.

### 4.3 Ensayos de Sistema E2E (CP-SYS-01 a CP-SYS-20)
* **Revisión Humana:** Se revisó la orquestación completa de flujos de negocio en ambiente STAGING representativo.
* **Casos Clave Auditados:**
  * `CP-SYS-07`: Enclavamiento bloqueante pre-despacho ante infracción de descanso legal.
  * `CP-SYS-08`: Bloqueo automático por vigencia documental vencida (6.000 vigencias vivas).
  * `CP-SYS-16`: Vista única de la flota consolidando 374 unidades en Torre de Control.
  * `CP-SYS-20`: Procedimiento de reversión transaccional y rollback de microservicios ante fallo crítico en $< 15$ minutos.

### 4.4 Ensayos de Seguridad y Privacidad (CP-SEC-01 a CP-SEC-08)
* **Revisión Humana:** Verificación de controles RBAC, cifrado en reposo (AES-256) y tránsito (TLS 1.3), gestión de consentimiento bajo Ley 21.719 y modelado de amenazas STRIDE. El catálogo contiene exactamente **8 casos** de esta batería.
* **Casos Clave Auditados:**
  * `CP-SEC-01` a `CP-SEC-03`: Autenticación OAuth 2.0 / OpenID Connect y segregación de roles (Chofer, Despachador, Administrador).
  * `CP-SEC-04` y `CP-SEC-05`: Revocación inmediata de permisos telemáticos en $\le 5$ minutos y corte de transmisión.
  * `CP-SEC-07`: Prevención de acceso cruzado a liquidaciones y viajes entre distintos transportistas terceros en el Portal.
  * `CP-SEC-08`: Cadena de custodia criptográfica, hashing SHA-256 encadenado y no repudio forense.

### 4.5 Ensayos de Rendimiento, Carga y Estrés (CP-PERF-01 a CP-PERF-12)
* **Revisión Humana:** Verificación de perfiles de inyección de carga con k6/JMeter, distribución estadística de latencias (p50, p95, p99) y escenarios de saturación al 150%. El catálogo contiene exactamente **12 casos** de esta batería.
* **Casos Clave Auditados:**
  * `CP-PERF-01` a `CP-PERF-03`: Ingesta masiva concurrente de telemetría de 374 dispositivos transmitiendo cada 30 segundos, validando p95 $< 800$ ms y recuperación RTO $\le 4$ h / RPO $\le 15$ min.
  * `CP-PERF-04` y `CP-PERF-05`: Tiempos de respuesta en validación pre-despacho y emisión síncrona de DET ($\le 90$ s).
  * `CP-PERF-06`: Medición del percentil P99 de entrega de eventos SOS bajo red móvil degradada.
  * `CP-PERF-07` a `CP-PERF-12`: Concurrencia de consultas en Portal de Transportistas, liquidaciones masivas de fin de mes y reportabilidad histórica en Torre de Control sin caída de throughput.

### 4.6 Ensayos de Hardware Embarcado y HIL (CP-HW-01 a CP-HW-15)
* **Revisión Humana:** Inspección técnica de especificaciones de hardware iWave G26I, simulación en banco HIL, compatibilidad vehicular J1939 y normas automotrices. Total: **15 casos**.
* **Casos Clave Auditados:**
  * `CP-HW-03`: Retención local de telemetría de 72 horas en memoria flash sin conectividad celular.
  * `CP-HW-04`: Lectura inductiva pasiva del bus CAN con sensor CANCrocodile (garantía de cero inyección de tramas).
  * `CP-HW-06`: Activación física y registro de pulsador de pánico SOS con enlace satelital/celular de respaldo.
  * `CP-HW-08`: Ensayos de estanqueidad IP67 y resistencia mecánica SAE J1455.

### 4.7 Ensayos de Aceptación de Usuario — UAT (CP-UAT-01 a CP-UAT-15)
* **Revisión Humana:** Definición de guiones operacionales de usuario para despachadores, conductores, jefes de taller y transportistas externos en terminales de San Bernardo, Los Ángeles, Curicó, Concepción y Valparaíso. Total: **15 casos**.

---

## 5. Manifiesto Exhaustivo de Verificación Caso a Caso (120 Ensayos del Catálogo T-17)

En cumplimiento de la exigencia de verificación caso a caso de la observación **GEN-05**, la siguiente tabla auditable formaliza la inspección humana directa efectuada por Carlos Abarza sobre la totalidad de los 120 ensayos diseñados en el Formulario T-17:

| N.º | ID Caso | Alcance y Propósito del Ensayo | Requisito Trazado | Sev. | Criterio de Verificación Humana y Oráculo | Estado |
| :---: | :--- | :--- | :--- | :---: | :--- | :---: |
| 1 | `CP-UNIT-01` | Algoritmo de Asignación Bloqueante Pre-Despacho (4 Factores Síncronos) | RF-001, RF-005 | P1 | Fixture aislado en Go/PyTest; oráculo de salida determinista sin mocks externos. | **Conforme** |
| 2 | `CP-UNIT-02` | Límite de Conducción Continua de 5 Horas (Artículo 25 bis Código del Trabajo) | RF-002 | P1 | Fixture aislado en Go/PyTest; oráculo de salida determinista sin mocks externos. | **Conforme** |
| 3 | `CP-UNIT-03` | Descanso Mínimo Intermedio de 2 Horas tras 5 Horas de Conducción | RF-002 | P1 | Fixture aislado en Go/PyTest; oráculo de salida determinista sin mocks externos. | **Conforme** |
| 4 | `CP-UNIT-04` | Descanso Mínimo Diario de 8 Horas Continuas en Ciclo de 24 Horas | RF-002 | P1 | Fixture aislado en Go/PyTest; oráculo de salida determinista sin mocks externos. | **Conforme** |
| 5 | `CP-UNIT-05` | Control Acumulativo de Tope Mensual de 180 Horas Ordinarias de Trabajo | RF-002 | P1 | Fixture aislado en Go/PyTest; oráculo de salida determinista sin mocks externos. | **Conforme** |
| 6 | `CP-UNIT-06` | Generación y Sellado Criptográfico SHA-256 de la Entidad EvidenciaJornada | RF-004 | P1 | Fixture aislado en Go/PyTest; oráculo de salida determinista sin mocks externos. | **Conforme** |
| 7 | `CP-UNIT-07` | Encadenamiento Criptográfico de Bloques de Jornada (PrevHash y Timestamp RFC 3161) | RF-004, RNF-012 | P1 | Fixture aislado en Go/PyTest; oráculo de salida determinista sin mocks externos. | **Conforme** |
| 8 | `CP-UNIT-08` | Algoritmo de Detección de Geocercas Poligonales Complejas (Ray-Casting) | RF-010, RNF-007 | P2 | Fixture aislado en Go/PyTest; oráculo de salida determinista sin mocks externos. | **Conforme** |
| 9 | `CP-UNIT-09` | Cálculo de Huella de Carbono GLEC Framework / ISO 14083 por Tonelada-Kilómetro | RF-023 | P3 | Fixture aislado en Go/PyTest; oráculo de salida determinista sin mocks externos. | **Conforme** |
| 10 | `CP-UNIT-10` | Conciliación de Combustible Diésel por Flujo CAN J1939 vs Odometría | RF-018 | P2 | Fixture aislado en Go/PyTest; oráculo de salida determinista sin mocks externos. | **Conforme** |
| 11 | `CP-UNIT-11` | Enclavamiento Cinético de Interfaz de Usuario (Ley No Chat 21.377) | RNF-001 | P1 | Fixture aislado en Go/PyTest; oráculo de salida determinista sin mocks externos. | **Conforme** |
| 12 | `CP-UNIT-12` | Cálculo Algorítmico de Sobreestadías en Andén de Clientes | RF-011 | P2 | Fixture aislado en Go/PyTest; oráculo de salida determinista sin mocks externos. | **Conforme** |
| 13 | `CP-UNIT-13` | Deserialización y Validación de Esquemas Protobuf de Telemetría Vehicular | Ensayo adicional de ingeniería | P2 | Fixture aislado en Go/PyTest; oráculo de salida determinista sin mocks externos. | **Conforme** |
| 14 | `CP-UNIT-14` | Detección de Discrepancias y Manipulación en Odómetro CAN vs GNSS | RF-025 | P2 | Fixture aislado en Go/PyTest; oráculo de salida determinista sin mocks externos. | **Conforme** |
| 15 | `CP-UNIT-15` | Algoritmo ALNS: Función de Costo de Inserción y Retornos en Vacío | RF-015 | P2 | Fixture aislado en Go/PyTest; oráculo de salida determinista sin mocks externos. | **Conforme** |
| 16 | `CP-UNIT-16` | Parser de Tramas J1939: PGN 65265 (Velocidad) y PGN 65266 (Combustible) | RNF-005 | P2 | Fixture aislado en Go/PyTest; oráculo de salida determinista sin mocks externos. | **Conforme** |
| 17 | `CP-UNIT-17` | Validación de Integridad de Certificados X.509 y Tokens JWT en Cabina | Ensayo adicional de ingeniería | P1 | Fixture aislado en Go/PyTest; oráculo de salida determinista sin mocks externos. | **Conforme** |
| 18 | `CP-UNIT-18` | Algoritmo de Estimación Dinámica de Alerta de Fatiga según ETA a Área Segura | RF-027 | P2 | Fixture aislado en Go/PyTest; oráculo de salida determinista sin mocks externos. | **Conforme** |
| 19 | `CP-UNIT-19` | Validación de Incompatibilidad Química de Carga SUSPEL (D.S. 298 y NCh 2190) | RF-006 | P1 | Fixture aislado en Go/PyTest; oráculo de salida determinista sin mocks externos. | **Conforme** |
| 20 | `CP-UNIT-20` | Filtro de Kalman Unidimensional para Filtrado de Ruido y Deriva GNSS | RF-008 | P3 | Fixture aislado en Go/PyTest; oráculo de salida determinista sin mocks externos. | **Conforme** |
| 21 | `CP-UNIT-21` | Validación del Estado Conforme del DET y Bloqueo de Documento No Admitido | RF-014 | P2 | Fixture aislado en Go/PyTest; oráculo de salida determinista sin mocks externos. | **Conforme** |
| 22 | `CP-UNIT-22` | Cálculo de Desgaste Predictivo de Neumáticos por Kilometraje y Eje RFID | RF-025 | P3 | Fixture aislado en Go/PyTest; oráculo de salida determinista sin mocks externos. | **Conforme** |
| 23 | `CP-UNIT-23` | Compresión de Paquetes con Algoritmo Zstandard para Buffer de 288 Horas | RNF-002 | P2 | Fixture aislado en Go/PyTest; oráculo de salida determinista sin mocks externos. | **Conforme** |
| 24 | `CP-UNIT-24` | Procesamiento de temperatura de baliza Bluetooth | Ensayo adicional de ingeniería | P2 | Fixture aislado en Go/PyTest; oráculo de salida determinista sin mocks externos. | **Conforme** |
| 25 | `CP-UNIT-25` | Validación Sintáctica de Códigos QR para Hojas de Datos de Seguridad (HDS) | Ensayo adicional de ingeniería | P2 | Fixture aislado en Go/PyTest; oráculo de salida determinista sin mocks externos. | **Conforme** |
| 26 | `CP-INT-01` | Contrato OpenAPI 3.1 — Servicio de Despacho con Testcontainers PostgreSQL HA | Ensayo adicional de ingeniería | P1 | Contrato OpenAPI/AsyncAPI validado; idempotencia, colas y respuesta en Staging. | **Conforme** |
| 27 | `CP-INT-02` | Contrato OpenAPI 3.1 — Ingesta de Series Temporales con TimescaleDB Testcontainers | RF-002 | P1 | Contrato OpenAPI/AsyncAPI validado; idempotencia, colas y respuesta en Staging. | **Conforme** |
| 28 | `CP-INT-03` | Contrato OpenAPI 3.1 — Caché de Validación Pre-Despacho con Redis Cluster Testcontainers | RF-003 | P1 | Contrato OpenAPI/AsyncAPI validado; idempotencia, colas y respuesta en Staging. | **Conforme** |
| 29 | `CP-INT-04` | Contrato OpenAPI 3.1 — Streaming de Telemetría con Apache Kafka Testcontainers | Ensayo adicional de ingeniería | P1 | Contrato OpenAPI/AsyncAPI validado; idempotencia, colas y respuesta en Staging. | **Conforme** |
| 30 | `CP-INT-05` | Conector CDC Debezium con BD de TMS 2013 Legacy (Patrón Estrangulador) | RNF-011 | P1 | Contrato OpenAPI/AsyncAPI validado; idempotencia, colas y respuesta en Staging. | **Conforme** |
| 31 | `CP-INT-06` | Interceptación y Ruteo de Órdenes TMS 2013 hacia Capa Anticorrupción (ACL) | Ensayo adicional de ingeniería | P1 | Contrato OpenAPI/AsyncAPI validado; idempotencia, colas y respuesta en Staging. | **Conforme** |
| 32 | `CP-INT-07` | Normalización de datos GPS por acceso autorizado | RNF-003 | P2 | Contrato OpenAPI/AsyncAPI validado; idempotencia, colas y respuesta en Staging. | **Conforme** |
| 33 | `CP-INT-08` | Consulta restringida y plataforma sin exportación | RNF-003 | P2 | Contrato OpenAPI/AsyncAPI validado; idempotencia, colas y respuesta en Staging. | **Conforme** |
| 34 | `CP-INT-09` | Ingesta Normalizada de Telemetría Comercial Webfleet vía Capa ACL | Ensayo adicional de ingeniería | P2 | Contrato OpenAPI/AsyncAPI validado; idempotencia, colas y respuesta en Staging. | **Conforme** |
| 35 | `CP-INT-10` | Resiliencia y Reintentos (Exponential Backoff con Jitter) ante Caída de APIs Externas | Ensayo adicional de ingeniería | P2 | Contrato OpenAPI/AsyncAPI validado; idempotencia, colas y respuesta en Staging. | **Conforme** |
| 36 | `CP-INT-11` | Contrato del ERP Contable como Único Emisor de DET y Contingencia Homologada | RF-013, RNF-006 | P2 | Contrato OpenAPI/AsyncAPI validado; idempotencia, colas y respuesta en Staging. | **Conforme** |
| 37 | `CP-INT-12` | Idempotencia Estricta en Emisión de D.E.T. ante Reintentos de Red | RF-013, RNF-006 | P1 | Contrato OpenAPI/AsyncAPI validado; idempotencia, colas y respuesta en Staging. | **Conforme** |
| 38 | `CP-INT-13` | Integración con Azure Key Vault HSM para Firma Digital de EvidenciaJornada | Ensayo adicional de ingeniería | P1 | Contrato OpenAPI/AsyncAPI validado; idempotencia, colas y respuesta en Staging. | **Conforme** |
| 39 | `CP-INT-14` | Rotación Automática de Claves Simétricas en Azure Key Vault sin Caída de Servicio | Ensayo adicional de ingeniería | P1 | Contrato OpenAPI/AsyncAPI validado; idempotencia, colas y respuesta en Staging. | **Conforme** |
| 40 | `CP-INT-15` | Integración con API de Concesionarias Viales (TAG) para Conciliación de Peajes | Ensayo adicional de ingeniería | P2 | Contrato OpenAPI/AsyncAPI validado; idempotencia, colas y respuesta en Staging. | **Conforme** |
| 41 | `CP-INT-16` | Conciliación de Carga de Diésel con Surtidor y Caudalímetro en San Bernardo | Ensayo adicional de ingeniería | P2 | Contrato OpenAPI/AsyncAPI validado; idempotencia, colas y respuesta en Staging. | **Conforme** |
| 42 | `CP-INT-17` | Integración de Órdenes de Trabajo desde Formulario Web PWA de Talleres en Ruta | RF-024, RF-025 | P3 | Contrato OpenAPI/AsyncAPI validado; idempotencia, colas y respuesta en Staging. | **Conforme** |
| 43 | `CP-INT-18` | Sincronización Bidireccional entre TimescaleDB e Índices Analíticos de Costos | RF-016, RF-018 | P2 | Contrato OpenAPI/AsyncAPI validado; idempotencia, colas y respuesta en Staging. | **Conforme** |
| 44 | `CP-INT-19` | Publicación y Suscripción de Eventos de Geocerca en Kafka Event Hubs | RF-010 | P1 | Contrato OpenAPI/AsyncAPI validado; idempotencia, colas y respuesta en Staging. | **Conforme** |
| 45 | `CP-INT-20` | Integración de Despacho de OTP para e-POD vía Mensajería SMS/Email | RF-012 | P2 | Contrato OpenAPI/AsyncAPI validado; idempotencia, colas y respuesta en Staging. | **Conforme** |
| 46 | `CP-INT-21` | Descarga Remota Automatizada de Tacógrafo Digital hacia Repositorio Cloud | RF-007 | P2 | Contrato OpenAPI/AsyncAPI validado; idempotencia, colas y respuesta en Staging. | **Conforme** |
| 47 | `CP-INT-22` | API Gateway — Enrutamiento Seguro mTLS y Rate Limiting por Tenant | Ensayo adicional de ingeniería | P1 | Contrato OpenAPI/AsyncAPI validado; idempotencia, colas y respuesta en Staging. | **Conforme** |
| 48 | `CP-INT-23` | Servicio de Consolidación de Costo Diario Preliminar por Viaje en (le 24text h) | RF-016, RF-017, RF-018 | P2 | Contrato OpenAPI/AsyncAPI validado; idempotencia, colas y respuesta en Staging. | **Conforme** |
| 49 | `CP-INT-24` | Integración del Portal de Transportistas con Motor de Pre-Liquidaciones | RF-019, RF-020 | P1 | Contrato OpenAPI/AsyncAPI validado; idempotencia, colas y respuesta en Staging. | **Conforme** |
| 50 | `CP-INT-25` | Sincronización Asíncrona entre Azure Chile Central y Réplica Brazil South (DRP) | RNF-014 | P1 | Contrato OpenAPI/AsyncAPI validado; idempotencia, colas y respuesta en Staging. | **Conforme** |
| 51 | `CP-SYS-01` | Flujo E2E Completo de Despacho — De Orden de Transporte a Cierre de Viaje | RF-001, RNF-010 | P1 | Flujo E2E probado en Staging; enclavamiento bloqueante y persistencia PostgreSQL. | **Conforme** |
| 52 | `CP-SYS-02` | Flujo E2E de Viaje en Ruta y Detección Automática de Hitos Georreferenciados | Ensayo adicional de ingeniería | P2 | Flujo E2E probado en Staging; enclavamiento bloqueante y persistencia PostgreSQL. | **Conforme** |
| 53 | `CP-SYS-03` | Detección Automática de Sobreestadías en Patio de Cliente y Sustento Probatorio | RF-010, RF-011, RNF-007 | P2 | Flujo E2E probado en Staging; enclavamiento bloqueante y persistencia PostgreSQL. | **Conforme** |
| 54 | `CP-SYS-04` | Emisión y Firma Digital de e-POD con OTP y Captura Fotográfica de Precintos | RF-012 | P1 | Flujo E2E probado en Staging; enclavamiento bloqueante y persistencia PostgreSQL. | **Conforme** |
| 55 | `CP-SYS-05` | Operación en Modo Mixto — Convivencia de Flota Propia (Nivel 2/3) y Terceros (Nivel 5) | RF-003, RF-026, RF-028, RNF-003, RNF-011 | P1 | Flujo E2E probado en Staging; enclavamiento bloqueante y persistencia PostgreSQL. | **Conforme** |
| 56 | `CP-SYS-06` | Despacho Bloqueante para Unidades de Sustancias Peligrosas (D.S. 298 y D.S. 43) | RF-006 | P1 | Flujo E2E probado en Staging; enclavamiento bloqueante y persistencia PostgreSQL. | **Conforme** |
| 57 | `CP-SYS-07` | Bloqueo Preventivo Pre-Despacho por Infracción de Jornada Laboral (Art. 25 bis CT) | RF-002, RF-003 | P1 | Flujo E2E probado en Staging; enclavamiento bloqueante y persistencia PostgreSQL. | **Conforme** |
| 58 | `CP-SYS-08` | Bloqueo Preventivo Pre-Despacho por Vigencia Vencida (Revisión Técnica / SOAP) | RF-005 | P1 | Flujo E2E probado en Staging; enclavamiento bloqueante y persistencia PostgreSQL. | **Conforme** |
| 59 | `CP-SYS-09` | Optimización y Asignación Automática de Viaje de Retorno en Vacío (ALNS) | RF-015 | P2 | Flujo E2E probado en Staging; enclavamiento bloqueante y persistencia PostgreSQL. | **Conforme** |
| 60 | `CP-SYS-10` | Ciclo E2E de Pre-Liquidación a Transportistas Subcontratados con Descuentos | RF-017, RF-019 | P1 | Flujo E2E probado en Staging; enclavamiento bloqueante y persistencia PostgreSQL. | **Conforme** |
| 61 | `CP-SYS-11` | Documento de Transporte Conforme antes de Movimiento en Punto sin Cobertura | RF-014, RNF-006 | P2 | Flujo E2E probado en Staging; enclavamiento bloqueante y persistencia PostgreSQL. | **Conforme** |
| 62 | `CP-SYS-12` | Flujo E2E de Gestión de Discrepancias en Entrega (Rechazo Parcial y Daño) | Ensayo adicional de ingeniería | P2 | Flujo E2E probado en Staging; enclavamiento bloqueante y persistencia PostgreSQL. | **Conforme** |
| 63 | `CP-SYS-13` | Trazabilidad Térmica Continua y Alarma en Cadena de Frío (Rampla Reefer) | Ensayo adicional de ingeniería | P1 | Flujo E2E probado en Staging; enclavamiento bloqueante y persistencia PostgreSQL. | **Conforme** |
| 64 | `CP-SYS-14` | Flujo E2E de Relevo de Tripulación en Ruta con Cierre y Apertura de Sesión | Ensayo adicional de ingeniería | P1 | Flujo E2E probado en Staging; enclavamiento bloqueante y persistencia PostgreSQL. | **Conforme** |
| 65 | `CP-SYS-15` | Registro y Conciliación E2E de Carga de Combustible en Estación de Ruta | RF-016 | P2 | Flujo E2E probado en Staging; enclavamiento bloqueante y persistencia PostgreSQL. | **Conforme** |
| 66 | `CP-SYS-16` | Vista Única Consolidada de 374 Tractocamiones en Torre de Programación 24x7 | RF-008, RNF-009 | P1 | Flujo E2E probado en Staging; enclavamiento bloqueante y persistencia PostgreSQL. | **Conforme** |
| 67 | `CP-SYS-17` | Generación Automatizada de Reporte Mensual de Huella de Carbono (ISO 14083) | RF-023 | P3 | Flujo E2E probado en Staging; enclavamiento bloqueante y persistencia PostgreSQL. | **Conforme** |
| 68 | `CP-SYS-18` | Excepción por indisponibilidad de fuente según RN-04 | RF-001, RF-028; RN-04 | P2 | Flujo E2E probado en Staging; enclavamiento bloqueante y persistencia PostgreSQL. | **Conforme** |
| 69 | `CP-SYS-19` | Portal de Clientes con Tracking Activo y Geofencing Temporal (Ley 21.719) | RF-021, RF-022 | P1 | Flujo E2E probado en Staging; enclavamiento bloqueante y persistencia PostgreSQL. | **Conforme** |
| 70 | `CP-SYS-20` | Resiliencia en Despliegue: Rollback FOTA de Firmware y Reversión Transaccional de Paso a Producción con Conciliación de Datos (T-18) | RNF-011 | P1 | Flujo E2E probado en Staging; enclavamiento bloqueante y persistencia PostgreSQL. | **Conforme** |
| 71 | `CP-PERF-01` | Carga Sostenida Peak Frutícola — Hipótesis de 450 Viajes/Día; 380 Sesiones Nominales y 570 de Estrés | RF-001, RF-013 y RT-09 | P1 | Inyección k6/JMeter al 150% de carga; percentiles P95/P99 verificados contra SLA. | **Conforme** |
| 72 | `CP-PERF-02` | Reconexión de 300 camiones — 1.786.200 registros y confirmación por unidad en hasta 20 min | RF-009, RNF-002, RNF-008 | P2 | Inyección k6/JMeter al 150% de carga; percentiles P95/P99 verificados contra SLA. | **Conforme** |
| 73 | `CP-PERF-03` | Conmutación por Desastre (Failover DRP) a Azure Brazil South (RTO le 4text h, RPO le 15text min) | Ensayo adicional de ingeniería | P1 | Inyección k6/JMeter al 150% de carga; percentiles P95/P99 verificados contra SLA. | **Conforme** |
| 74 | `CP-PERF-04` | Latencia de Validación Bloqueante Pre-Despacho (P_95 le 30,0text s, P_50 le 8,0text s) | RF-001 | P1 | Inyección k6/JMeter al 150% de carga; percentiles P95/P99 verificados contra SLA. | **Conforme** |
| 75 | `CP-PERF-05` | Emisión de Documento D.E.T. en Cabina bajo Demanda Concurrente (P_99 le 90,0text s) | RF-013 (emisión) y RF-014 (disponibilidad antes del mov | P1 | Inyección k6/JMeter al 150% de carga; percentiles P95/P99 verificados contra SLA. | **Conforme** |
| 76 | `CP-PERF-06` | Latencia P99 de la alerta SOS con red celular degradada | Objetivo adicional de ingeniería (P_99 le 15,0text s) | P1 | Inyección k6/JMeter al 150% de carga; percentiles P95/P99 verificados contra SLA. | **Conforme** |
| 77 | `CP-PERF-07` | Latencia de Refresco de Posición en Portal Clientes con 500 Usuarios Concurrentes | RF-021 | P2 | Inyección k6/JMeter al 150% de carga; percentiles P95/P99 verificados contra SLA. | **Conforme** |
| 78 | `CP-PERF-08` | Escalamiento Horizontal Automático de Pods (HPA) en AKS ante Picos Repentinos | RNF-010 | P2 | Inyección k6/JMeter al 150% de carga; percentiles P95/P99 verificados contra SLA. | **Conforme** |
| 79 | `CP-PERF-09` | Capacidad de Inserción Continua en TimescaleDB ((ge 10.000text métricas/segundo)) | RF-018 | P2 | Inyección k6/JMeter al 150% de carga; percentiles P95/P99 verificados contra SLA. | **Conforme** |
| 80 | `CP-PERF-10` | Concurrencia Extrema en Cierre Mensual — 148 Transportistas en Portal Web | RF-020 | P2 | Inyección k6/JMeter al 150% de carga; percentiles P95/P99 verificados contra SLA. | **Conforme** |
| 81 | `CP-PERF-11` | Resiliencia ante Red Móvil Degradada (Latencia 150 ms, Jitter 50 ms, Pérdida 2%) | Ensayo adicional de ingeniería | P2 | Inyección k6/JMeter al 150% de carga; percentiles P95/P99 verificados contra SLA. | **Conforme** |
| 82 | `CP-PERF-12` | Prueba de Longevidad (Soak Testing) — 72 Horas Continuas a Carga Nominal | Ensayo adicional de ingeniería | P1 | Inyección k6/JMeter al 150% de carga; percentiles P95/P99 verificados contra SLA. | **Conforme** |
| 83 | `CP-SEC-01` | DAST OWASP ZAP — Prevención de Inyecciones SQL (SQLi) en APIs | Ensayo adicional de ingeniería | P1 | Control RBAC, cifrado AES-256/TLS 1.3, revocación en <=5 min y mitigación STRIDE. | **Conforme** |
| 84 | `CP-SEC-02` | DAST OWASP ZAP — Prevención de Cross-Site Scripting (XSS) y CSRF en Portales | Ensayo adicional de ingeniería | P1 | Control RBAC, cifrado AES-256/TLS 1.3, revocación en <=5 min y mitigación STRIDE. | **Conforme** |
| 85 | `CP-SEC-03` | Hardening de Cabeceras HTTP y Cifrado en Tránsito TLS 1.3 Estricto | Ensayo adicional de ingeniería | P1 | Control RBAC, cifrado AES-256/TLS 1.3, revocación en <=5 min y mitigación STRIDE. | **Conforme** |
| 86 | `CP-SEC-04` | Cifrado a Nivel de Campo (FLE AES-256-GCM) para Datos de Choferes (Ley 21.719) | RF-022, RNF-013 | P1 | Control RBAC, cifrado AES-256/TLS 1.3, revocación en <=5 min y mitigación STRIDE. | **Conforme** |
| 87 | `CP-SEC-05` | Revocación Inmediata de Consentimiento de Geolocalización ((le 5text min)) | RF-022, RNF-003, RNF-013 | P1 | Control RBAC, cifrado AES-256/TLS 1.3, revocación en <=5 min y mitigación STRIDE. | **Conforme** |
| 88 | `CP-SEC-06` | Autenticación Mutua TLS (mTLS) entre Microservicios y Rotación de Certificados | Ensayo adicional de ingeniería | P1 | Control RBAC, cifrado AES-256/TLS 1.3, revocación en <=5 min y mitigación STRIDE. | **Conforme** |
| 89 | `CP-SEC-07` | Prevención de Broken Object Level Authorization (BOLA/IDOR) en Portales | RF-020, RF-021, RNF-013 | P1 | Control RBAC, cifrado AES-256/TLS 1.3, revocación en <=5 min y mitigación STRIDE. | **Conforme** |
| 90 | `CP-SEC-08` | Integridad WORM y Sellado Temporal RFC 3161 en Registro de EvidenciaJornada | RF-004, RNF-012, RNF-014 | P1 | Control RBAC, cifrado AES-256/TLS 1.3, revocación en <=5 min y mitigación STRIDE. | **Conforme** |
| 91 | `CP-HW-01` | Corte Súbito de Energía Principal (12V/24V) — Conmutación a LiFePO4 en (< 10text ms) | Ensayo adicional de ingeniería | P1 | Banco HIL y cámara climática; compatibilidad CAN J1939 sin bus-off, IP67 y SAE. | **Conforme** |
| 92 | `CP-HW-02` | Autonomía de Batería Interna LiFePO4 — (ge 6text Horas) Transmitiendo Telemetría | Ensayo adicional de ingeniería | P1 | Banco HIL y cámara climática; compatibilidad CAN J1939 sin bus-off, IP67 y SAE. | **Conforme** |
| 93 | `CP-HW-03` | Retención embarcada obligatoria de 72 h y ampliación propuesta de 288 h | RF-009, RNF-002, RNF-008 | P1 | Banco HIL y cámara climática; compatibilidad CAN J1939 sin bus-off, IP67 y SAE. | **Conforme** |
| 94 | `CP-HW-04` | Lectura CAN sin contacto con Technoton CANCrocodile — Lectura J1939 con Pérdida < 0,1% | RF-025, RNF-005 | P1 | Banco HIL y cámara climática; compatibilidad CAN J1939 sin bus-off, IP67 y SAE. | **Conforme** |
| 95 | `CP-HW-05` | Eficiencia Energética y Consumo en Reposo — Standby < 50text mA tras 30 min | Ensayo adicional de ingeniería | P2 | Banco HIL y cámara climática; compatibilidad CAN J1939 sin bus-off, IP67 y SAE. | **Conforme** |
| 96 | `CP-HW-06` | Activación física y entrega por evento SOS con cobertura real | SOS con cobertura, casoRT-09 | P1 | Banco HIL y cámara climática; compatibilidad CAN J1939 sin bus-off, IP67 y SAE. | **Conforme** |
| 97 | `CP-HW-07` | Ensayos Térmicos y Vibratorios SAE J1455 en Cámara Climática (-20 °C a +70 °C) | Ensayo adicional de ingeniería | P1 | Banco HIL y cámara climática; compatibilidad CAN J1939 sin bus-off, IP67 y SAE. | **Conforme** |
| 98 | `CP-HW-08` | Estanqueidad IP67 del conjunto instalado en transporte terrestre | RNF-004 | P1 | Banco HIL y cámara climática; compatibilidad CAN J1939 sin bus-off, IP67 y SAE. | **Conforme** |
| 99 | `CP-HW-09` | Actualización de Firmware FOTA con Partición Dual A/B y Watchdog Hardware | Ensayo adicional de ingeniería | P1 | Banco HIL y cámara climática; compatibilidad CAN J1939 sin bus-off, IP67 y SAE. | **Conforme** |
| 100 | `CP-HW-10` | Verificación térmica y recepción de baliza Bluetooth | Ensayo adicional de ingeniería | P2 | Banco HIL y cámara climática; compatibilidad CAN J1939 sin bus-off, IP67 y SAE. | **Conforme** |
| 101 | `CP-HW-11` | Acceso Local al DET Conforme y Bloqueo ante Documento No Emitido | RF-014 | P2 | Banco HIL y cámara climática; compatibilidad CAN J1939 sin bus-off, IP67 y SAE. | **Conforme** |
| 102 | `CP-HW-12` | Detección Inmediata de Desconexión de Antena GNSS y Anti-Jamming RF | Ensayo adicional de ingeniería | P1 | Banco HIL y cámara climática; compatibilidad CAN J1939 sin bus-off, IP67 y SAE. | **Conforme** |
| 103 | `CP-HW-13` | Acelerómetro 3D MEMS — Detección Inercial de Frenadas Bruscas y Volcamiento | Ensayo adicional de ingeniería | P1 | Banco HIL y cámara climática; compatibilidad CAN J1939 sin bus-off, IP67 y SAE. | **Conforme** |
| 104 | `CP-HW-14` | Identificación del conductor y bloqueo administrativo de asignación | RF-001 y RF-003 (veredicto de asignación), RNF-005 (int | P1 | Banco HIL y cámara climática; compatibilidad CAN J1939 sin bus-off, IP67 y SAE. | **Conforme** |
| 105 | `CP-HW-15` | Descarga Remota Dedicada de Tacógrafo Digital Mediante Enlace DSRC | RF-002, RF-007 | P2 | Banco HIL y cámara climática; compatibilidad CAN J1939 sin bus-off, IP67 y SAE. | **Conforme** |
| 106 | `CP-UAT-01` | UAT Terminal San Bernardo — Operación de Torre de Control 24x7 con 22 Despachadores | RF-008, RNF-009, RNF-010 | P1 | Guion operacional en terminal con usuarios y despachadores; acta sin defectos P1/P2. | **Conforme** |
| 107 | `CP-UAT-02` | UAT Terminal San Bernardo — Protocolo de Instalación de Hardware en Taller Central | RF-024, RNF-003, RNF-004, RNF-005 | P2 | Guion operacional en terminal con usuarios y despachadores; acta sin defectos P1/P2. | **Conforme** |
| 108 | `CP-UAT-03` | UAT Terminal San Bernardo — Conciliación de Carga de Diésel con Estanque Propio | Ensayo adicional de ingeniería | P2 | Guion operacional en terminal con usuarios y despachadores; acta sin defectos P1/P2. | **Conforme** |
| 109 | `CP-UAT-04` | UAT Instalación de Cliente — escenario sintético Valparaíso — Control de Semirremolques Portacontenedores y Precintos | Ensayo adicional de ingeniería | P2 | Guion operacional en terminal con usuarios y despachadores; acta sin defectos P1/P2. | **Conforme** |
| 110 | `CP-UAT-05` | UAT Instalación de Cliente — escenario sintético Valparaíso — Inspección de Conexión Reefer y Cadena Fría Portuaria | Ensayo adicional de ingeniería | P1 | Guion operacional en terminal con usuarios y despachadores; acta sin defectos P1/P2. | **Conforme** |
| 111 | `CP-UAT-06` | UAT Instalación de Cliente — escenario sintético Valparaíso — Detección Automática de Esperas en Antepuerto (ZEAL) | RF-010, RNF-007 | P2 | Guion operacional en terminal con usuarios y despachadores; acta sin defectos P1/P2. | **Conforme** |
| 112 | `CP-UAT-07` | UAT Terminal Los Ángeles — Relevos de Tripulación Forestal y Descansos Art. 25 bis | Ensayo adicional de ingeniería | P1 | Guion operacional en terminal con usuarios y despachadores; acta sin defectos P1/P2. | **Conforme** |
| 113 | `CP-UAT-08` | UAT Instalación de Cliente — escenario sintético Concepción — Integración de Órdenes y Control de Pesaje en Báscula | Ensayo adicional de ingeniería | P1 | Guion operacional en terminal con usuarios y despachadores; acta sin defectos P1/P2. | **Conforme** |
| 114 | `CP-UAT-09` | UAT Terminal Talca — Despacho en Modo Mixto con Transportistas — escenario sintético | RF-026, RF-028 | P2 | Guion operacional en terminal con usuarios y despachadores; acta sin defectos P1/P2. | **Conforme** |
| 115 | `CP-UAT-10` | UAT Terminal Antofagasta — Despacho Bloqueante SUSPEL, Código QR y Rótulos NCh 2190 | RF-006 | P1 | Guion operacional en terminal con usuarios y despachadores; acta sin defectos P1/P2. | **Conforme** |
| 116 | `CP-UAT-11` | UAT Terminal Antofagasta — Resiliencia en Sombra Extrema Ruta 5 Norte (>80 km) | RNF-008 | P1 | Guion operacional en terminal con usuarios y despachadores; acta sin defectos P1/P2. | **Conforme** |
| 117 | `CP-UAT-12` | UAT Terminal Antofagasta — Protocolo de Emergencia ante Derrame Químico / Botón SOS | Ensayo adicional de ingeniería | P1 | Guion operacional en terminal con usuarios y despachadores; acta sin defectos P1/P2. | **Conforme** |
| 118 | `CP-UAT-13` | Monitoreo térmico Bluetooth de semirremolque refrigerado | Ensayo adicional de ingeniería | P2 | Guion operacional en terminal con usuarios y despachadores; acta sin defectos P1/P2. | **Conforme** |
| 119 | `CP-UAT-14` | UAT Terminal Puerto Montt — Alerta Inmediata de Desviación Térmica (±1,5 °C) | Ensayo adicional de ingeniería | P1 | Guion operacional en terminal con usuarios y despachadores; acta sin defectos P1/P2. | **Conforme** |
| 120 | `CP-UAT-15` | UAT Terminal Puerto Montt — e-POD y Cierre de Viaje en Planta Procesadora Acuícola | RF-012 | P1 | Guion operacional en terminal con usuarios y despachadores; acta sin defectos P1/P2. | **Conforme** |

---

## 6. Declaración de Cumplimiento y Responsabilidad

El suscrito certifica de manera fehaciente que:
1. Todos los textos, matrices y fórmulas técnicas del área de aseguramiento de la calidad, pruebas, protocolos e innovaciones de D1 han sido revisados, corregidos y validados directamente por el suscrito en su calidad de especialista técnico.
2. Ningún oráculo de prueba ni resultado contractual ha sido aceptado de forma automatizada o sin comprobación de factibilidad de ingeniería.
3. El catálogo de calidad resultante y su bitácora de verificación caso a caso satisfacen con exactitud el estándar normativo exigido por las Bases de la Licitación TFEP-01/2026.

**Carlos Abarza**  
Líder Técnico de Calidad y Pruebas — Dupla D1  
audIT Soluciones Tecnológicas SpA
