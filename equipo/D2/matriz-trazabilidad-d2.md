# Matriz de trazabilidad - D2

**Subdocumento 3 · Esquema de solución y alcance**\
**Estado:** borrador derivado de `catalogo-requisitos-d2.md`\
**Regla:** un componente ausente se marca **por definir**; no se inventa como parte de
la arquitectura acordada.

Los componentes y pruebas son candidatos para revisión con D3/D4, no evidencia de
cumplimiento. `Decisión` referencia el registro sin ratificarlo; `Verifica` identifica
la fuente que la prueba deberá contrastar, no una verificación ya realizada. Las
brechas son observaciones documentales pendientes de validación por sus responsables.

## 1. Requisitos funcionales

| ID | Decisión | Capacidad | Componente lógico/físico | Verifica | Prueba | Brecha |
|---|---|---|---|---|---|---|
| RF-001 | D-06 | Despacho seguro | Servicios de Despacho, Jornada, Flota y Gestión Documental | CA-01; R-07 | Bloqueos válidos/inválidos y auditoría | Clasificar excepciones |
| RF-002 | D-01, D-13 | Jornada propia y externa | Servicio de Control de Jornada; Conductor; Búfer a Bordo | CA-02; R-02; R-07 | Conciliación de fuentes y autoría | Modelo de fuentes por definir |
| RF-003 | D-01 | Jornada previa externa | Servicio de Control de Jornada; Conductor; CONSENTIMIENTO_DATOS | CA-03; R-02; R-07 | Casos suficiente, insuficiente, ausente y corregido | Fuente intercliente por definir |
| RF-004 | D-13, D-24 | Evidencia inalterable | Gestión Documental; Auditoría Append-Only; Repositorio WORM | CA-04 | Alteración, corrección, borrado y cadena de custodia | Corregir trigger; validar autoría |
| RF-005 | D-18 | Registro único de vigencias | Gestión Documental; VIGENCIA_HABILITACION; MDM; WORM | CA-05 | Conciliación, alerta y bloqueo | Responsables y umbrales pendientes |
| RF-006 | D-19 | Verificación de carga peligrosa | OrdenTransporte; Semirremolque; Despacho y Asignación | CA-06; R-09 | Coincidencia, discrepancia y ausencia | Captura de carga efectiva por definir |
| RF-007 | D-13 | Descarga de tacógrafos | Unidad telemática; CAN/FMS; Gestión Documental; WORM | CA-07; R-02; R-03 | Piloto por modelo y contingencia física | Parque, periodicidad e identidad pendientes |
| RF-008 | D-04, D-26 | Vista única de flota | Portal Unificado; Broker Streaming; Base de Telemetría | CA-08; R-02; R-03 | Conciliación de padrón y pérdida de señal | Ingestión multicarrier por definir |
| RF-009 | D-11, D-26 | Operación offline 72 h | Búfer a Bordo; Unidad telemática; IoT Hub; Event Hubs | CA-09; R-03; R-04 | Desconexión, corte, reconexión y deduplicación | Cobertura real de terceros pendiente |
| RF-010 | D-08 | Llegada/salida automática | Unidad telemática; caché; Base de Telemetría | CA-10; R-01; R-09 | Geocercas, falsos cruces y offline | Servicio de geocercas no individualizado |
| RF-011 | D-08 | Evidencia de sobreestadía | Liquidaciones y Peajes; Tarifas y Contratos; Portal; WORM | CA-11 | Reconstrucción y muestreo de cobros | Permanencia contractual por definir |
| RF-012 | D-10 | Conformidad de entrega | Aplicación Móvil; Búfer a Bordo; WORM | CA-12; R-04; R-09 | Aceptación, rechazo, ausencia y offline | Identidad/aceptación por definir |
| RF-013 | D-03, D-09 | DET sin redigitación | OrdenTransporte; ACL; Adaptador ERP 2013; Transformador | CA-13; R-08 | Comparación campo a campo y emisión única | Interfaz ERP no confirmada |
| RF-014 | D-09 | DET conforme antes del movimiento sin cobertura | Búfer a Bordo; ACL; Broker Transaccional; DLQ; **mecanismo de emisión conforme por definir** | CA-14; R-04; R-08 | Documento conforme previo al movimiento, bloqueo si falta, offline, reintento y cero duplicados | Interfaz y mecanismo tributario sin validar; una cola de emisión posterior no satisface el requisito |
| RF-015 | D-14 | Optimización de retornos | Lakehouse; Capa Semántica; **optimizador por definir** | CA-15; R-02 | Piloto antes/después y restricciones | Función objetivo abierta |
| RF-016 | D-15, D-16, D-17 | Costo real por km, viaje, ruta y contrato | ETL; Conciliación GPS; Lakehouse; FACT_COSTO_VIAJE | CA-16; CA-17; CA-19; FEP03 RT-05.29 | Costo consolidado ≤24 h con componentes disponibles/faltantes explícitos; conciliación y costo real antes de renegociar | Validar fuentes y versionado propuesto; preliminar no equivale automáticamente al consolidado exigido |
| RF-017 | D-16 | Separación de costos | FACT_COSTO_VIAJE; DIM_PROPIEDAD_FLOTA; Tarifas y Contratos | CA-16; R-02 | Propia, tercero cerrado y open-book | Consentimiento open-book pendiente |
| RF-018 | D-12, D-15 | Rendimiento comparable | Lakehouse; Capa Semántica; Conciliación GPS | CA-18 | Cohorte comparable y repetibilidad | Depende de consumo real |
| RF-019 | D-03, D-16 | Liquidación automática | Liquidaciones y Peajes; Transportista; ACL | CA-20 | Ejecución paralela y cuadre | Workflow de excepción incompleto |
| RF-020 | D-02, D-23 | Portal del transportista | Portal Unificado; Entra ID; Transportista | CA-21; CA-29 | Aceptación y segregación | ABAC y auditoría visible pendientes |
| RF-021 | D-23 | Seguimiento para clientes | Portal; Entra ID; CONSENTIMIENTO_DATOS; Telemetría | CA-22; R-02; R-03 | Acceso antes/durante/después | Modelo de permiso insuficiente |
| RF-022 | D-23 | Consentimiento granular | CONSENTIMIENTO_DATOS; Portal; Auditoría; Entra ID | CA-23; CA-29; R-02; R-03 | Otorgar/revocar y auditar | Granularidad y derechos del conductor |
| RF-023 | D-22 | Emisiones: base/metodología E1; productivo completo E2 (propuesta no ratificada) | Lakehouse; Capa Semántica; **motor CO2e por definir** | CA-24; FEP03 RT-05.29; R-02 | E1: fuentes, línea base y método; E2: reproducción independiente y consolidación mensual, incluidos terceros | Método, factores, cobertura y distribución E1/E2 pendientes; E1 no acredita cumplimiento completo |
| RF-024 | D-21 | Taller externo | Interfaces de Taller; Aplicación Móvil; Gestión de Flota | CA-25; R-04; R-09 | Offline, aprobación y sincronización | Workflow de taller por definir |
| RF-025 | D-12, D-21 | Mantenimiento por kilometraje | Gestión de Flota; Tractocamion; rFMS; Telemetría | CA-26; R-03; R-06 | Comparación con odómetro y orden | Acceso OEM pendiente |
| RF-026 | D-02, D-05 | Adhesión de transportistas | Portal; Transportista; CONSENTIMIENTO_DATOS | CA-27; R-02; R-03 | Flujo de adhesión y muestreo contractual | Workflow contractual por definir |
| RF-027 | D-07 | Alerta de jornada segura | Unidad telemática; Búfer; Control de Jornada | CA-28; R-01; R-04 | Rutas piloto y caso sin lugar alcanzable | Catálogo/algoritmo por definir |
| RF-028 | D-26 | Operación mixta | Despacho; Portal; Unidad telemática; Gestión Documental | CA-01; CA-02; CA-08; CA-27; R-02; R-03; R-07 | Flota mixta, etiquetas y bloqueos | Gobierno de modos por definir |

## 2. Requisitos no funcionales

| ID | Decisión | Capacidad | Componente lógico/físico | Verifica | Prueba | Brecha |
|---|---|---|---|---|---|---|
| RNF-001 | D-07, D-08 | Cero interacción en movimiento | Unidad telemática; Identificación; Aplicación Móvil | R-01; CA-10; CA-28 | Bloqueo de controles en movimiento | Bloqueo no especificado |
| RNF-002 | D-11 | Offline íntegro e idempotente | Búfer; SQLite WAL; Event Hubs; caché | R-04; CA-09 | 72 h, corte y reconciliación | Idempotencia de 24 h insuficiente |
| RNF-003 | D-02, D-04 | No intervenir terceros | CONSENTIMIENTO_DATOS; IoT Hub; Portal | R-02; R-03 | Adherido/no adherido | Autorización contractual no modelada |
| RNF-004 | D-25 | Intervención durante paso normal | Despliegue sin detener flota; kits; IoT Update | R-05; R-10; R-11 | Piloto cronometrado | Meta de 30 min no validada |
| RNF-005 | D-12 | Lectura vehicular segura | rFMS; acoplador inductivo; CAN/FMS | R-06 | Autorización OEM y no escritura | Garantía no confirmada |
| RNF-006 | D-03, D-09 | Emisor tributario único | ACL; Adaptador ERP; Broker; DLQ | R-08 | Emisión única y reintentos | Interfaz y ventana pendientes |
| RNF-007 | D-08, D-10, D-19 | Sin equipos en clientes | Unidad telemática; geocercas; Aplicación Móvil | R-09; CA-10; CA-12 | Piloto sin instalación externa | Evidencias D-10/D-19 abiertas |
| RNF-008 | D-20 | Continuidad 12 días | Búfer ≥8 GB; Unidad telemática; sala secundaria | R-04; R-12 | Simulación de cierre prolongado | Energía y terceros no demostrados |
| RNF-009 | — | Operación por TI reducido | Azure administrado; Monitor; Log Analytics; Grafana; Arc | R-13 | Runbook y prueba por TI | RACI/NOC por definir |
| RNF-010 | D-05, D-11 | TCO de 36 meses | Cost Management; FinOps; modelo D4 | R-14 | Trazabilidad de costos por escenario | Cantidades reales pendientes |
| RNF-011 | D-25, D-26 | Despliegue progresivo | Despliegue sin detener flota; IoT Device Twins/Update | R-05; R-10; R-11 | Convivencia, actualización y reversión | Cronograma y reversión pendientes |
| RNF-012 | D-24 | Auditoría probatoria | Auditoría Append-Only; auditoria_evento; WORM | CA-04 | Intentos INSERT/UPDATE/DELETE y hashes | Trigger inconsistente |
| RNF-013 | D-23, D-24 | Privacidad y cifrado | Entra ID; Key Vault; APIM; AES-256-GCM | CA-23; CA-29 | Accesos negativos y cifrado | ABAC granular no materializado |
| RNF-014 | D-13, D-23, D-24 | Retención por dominio | Matriz de retención; WORM; crypto-shredding | CA-04; CA-23 | Archivo, purga y excepción legal | Revocación contradice retención |

## 3. Componentes que D3/D4 deben incorporar o precisar

1. Ingestión y homologación de los tres proveedores GPS.
2. Captura y validación de carga peligrosa efectivamente cargada.
3. Conformidad digital e identificación del receptor.
4. Motor de optimización de retornos.
5. Motor versionado para cálculo de CO2e.
6. Workflow móvil y de aprobación para talleres externos.
7. Workflow contractual de adhesión de transportistas.
8. Catálogo y cálculo de lugares seguros alcanzables.
9. Gobierno explícito de los modos completo, homologado y documental.
10. Modelo de consentimiento por camión, viaje, dato, destinatario y periodo.

## 4. Controles de cierre

- [ ] Cada requisito conserva el mismo ID y etapa que el catálogo.
- [ ] Cada requisito tiene al menos una capacidad y una prueba.
- [ ] Toda brecha de componente tiene responsable y tratamiento.
- [ ] D3 valida los componentes lógicos y D4 los físicos.
- [ ] Ninguna consulta sin respuesta se presenta como confirmación.
- [ ] Se corrigen las contradicciones de auditoría, retención e idempotencia.
