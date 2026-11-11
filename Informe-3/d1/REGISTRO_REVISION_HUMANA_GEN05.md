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

### 4.4 Ensayos de Seguridad y Privacidad (CP-SEC-01 a CP-SEC-10)
* **Revisión Humana:** Verificación de controles RBAC, cifrado en reposo (AES-256) y tránsito (TLS 1.3), gestión de consentimiento bajo Ley 21.719 y modelado STRIDE.
* **Casos Clave Auditados:**
  * `CP-SEC-04` y `CP-SEC-05`: Revocación inmediata de permisos telemáticos en $\le 5$ minutos.
  * `CP-SEC-08`: Cadena de custodia criptográfica y no repudio forense.

### 4.5 Ensayos de Rendimiento, Carga y Estrés (CP-PERF-01 a CP-PERF-10)
* **Revisión Humana:** Verificación de perfiles de inyección de carga con k6/JMeter, distribución estadística de latencias (p50, p95, p99) y escenarios de saturación al 150%.
* **Casos Clave Auditados:**
  * `CP-PERF-01` a `CP-PERF-03`: Ingesta masiva concurrente de 374 dispositivos transmitiendo cada 30 segundos.
  * `CP-PERF-06`: Medición del percentil P99 de entrega de eventos SOS bajo red móvil degradada.

### 4.6 Ensayos de Hardware Embarcado y HIL (CP-HW-01 a CP-HW-15)
* **Revisión Humana:** Inspección técnica de especificaciones de hardware iWave G26I, simulación en banco HIL, compatibilidad vehicular J1939 y normas automotrices.
* **Casos Clave Auditados:**
  * `CP-HW-03`: Retención local de telemetría de 72 horas en memoria flash sin conectividad celular.
  * `CP-HW-04`: Lectura inductiva pasiva del bus CAN con sensor CANCrocodile (garantía de cero inyección de tramas).
  * `CP-HW-06`: Activación y registro de pulsador de pánico SOS con enlace satelital/celular de respaldo.
  * `CP-HW-08`: Ensayos de estanqueidad IP67 y resistencia mecánica SAE J1455.

### 4.7 Ensayos de Aceptación de Usuario — UAT (CP-UAT-01 a CP-UAT-15)
* **Revisión Humana:** Definición de guiones operacionales de usuario para despachadores, conductores, jefes de taller y transportistas externos en terminales de San Bernardo, Los Ángeles, Curicó, Concepción y Valparaíso.

---

## 5. Declaración de Cumplimiento y Responsabilidad

El suscrito certifica de manera fehaciente que:
1. Todos los textos, matrices y fórmulas técnicas del área de aseguramiento de la calidad, pruebas, protocolos e innovaciones de D1 han sido revisados, corregidos y validados directamente por el suscrito en su calidad de especialista técnico.
2. Ningún oráculo de prueba ni resultado contractual ha sido aceptado de forma automatizada o sin comprobación de factibilidad de ingeniería.
3. El catálogo de calidad resultante satisface con exactitud el estándar normativo exigido por las Bases de la Licitación TFEP-01/2026.

**Carlos Abarza**  
Líder Técnico de Calidad y Pruebas — Dupla D1  
audIT Soluciones Tecnológicas SpA
