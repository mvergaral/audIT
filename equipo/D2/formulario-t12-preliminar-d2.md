# Formulario T-12 preliminar - D2

**Matriz de cumplimiento técnico y trazabilidad**\
**Fuente del formato:** FEP01 · Formulario T-12 · p.62\
**Estado:** matriz interna de trabajo, no formato final aprobado

Esta matriz conserva los nombres de las cinco columnas del T-12 y cubre los 42 IDs
internos `RF-001..RF-028` y `RNF-001..RNF-014`. No sustituye la declaración de cada
requisito aplicable de las Bases que exige FEP01 · Formulario T-12 · p.62.
**Pendiente de verificación** es un estado de uso interno, no un valor del formato final
aprobado. Todas las filas tienen brechas o validaciones abiertas en la matriz de
trazabilidad; ni el compromiso de atender una exigencia ni un componente propuesto
justifican declarar cumplimiento. Los componentes son candidatos por revisar con
D3/D4 y las referencias SD3 no acreditan aún una sección definitiva de la propuesta.

| ID requerimiento | Descripción | Cumple | Componente que lo satisface | Sección de la propuesta |
|---|---|---|---|---|
| RF-001 | Validación bloqueante de jornada, habilitaciones y aptitud. | Pendiente de verificación | Servicios de Despacho, Jornada, Flota y Gestión Documental | SD3 · Despacho seguro |
| RF-002 | Jornada acreditada de conductores propios y externos. | Pendiente de verificación | Control de Jornada; Conductor; Búfer a Bordo | SD3 · Jornada propia y externa |
| RF-003 | Jornada previa externa disponible al asignar. | Pendiente de verificación | Control de Jornada; Conductor; Consentimiento | SD3 · Jornada externa y adhesión |
| RF-004 | Evidencia de jornada íntegra y sin sobrescritura. | Pendiente de verificación | Gestión Documental; Auditoría Append-Only; WORM | SD3 · Cadena de custodia |
| RF-005 | Registro único de vigencias con alerta y bloqueo. | Pendiente de verificación | Gestión Documental; MDM; Vigencias; WORM | SD3 · Registro de vigencias |
| RF-006 | Carga peligrosa efectiva verificada contra manifiesto. | Pendiente de verificación | Orden de Transporte; Semirremolque; Despacho | SD3 · Carga peligrosa |
| RF-007 | Descarga, asociación y conservación de tacógrafos. | Pendiente de verificación | Unidad Telemática; CAN/FMS; Gestión Documental | SD3 · Jornada y tacógrafos |
| RF-008 | Vista única de posición de los 374 camiones. | Pendiente de verificación | Portal; Broker Streaming; Base de Telemetría | SD3 · Vista única de flota |
| RF-009 | Registro local de 72 h y sincronización posterior. | Pendiente de verificación | Búfer a Bordo; Unidad Telemática; IoT Hub | SD3 · Operación desconectada |
| RF-010 | Llegada y salida automáticas en clientes. | Pendiente de verificación | Unidad Telemática; Geocercas; Telemetría | SD3 · Tiempos en clientes |
| RF-011 | Evidencia de espera y respaldo de sobreestadía. | Pendiente de verificación | Liquidaciones; Tarifas; Portal; WORM | SD3 · Evidencia comercial |
| RF-012 | Conformidad digital disponible el mismo día. | Pendiente de verificación | Aplicación Móvil; Búfer; WORM | SD3 · Conformidad de entrega |
| RF-013 | DET generado desde la orden sin redigitación. | Pendiente de verificación | Orden; ACL; Adaptador ERP; Transformador | SD3 · Integración tributaria |
| RF-014 | DET conforme antes del movimiento, incluso sin cobertura, con emisor contable único; bloqueo si falta. La emisión diferida no basta. | Pendiente de verificación | Búfer; ACL; Broker; DLQ; mecanismo conforme por definir y validar | SD3 · Contingencia tributaria |
| RF-015 | Recomendación de retornos y reducción de vacío. | Pendiente de verificación | Lakehouse; Capa Semántica; optimizador por definir | SD3 · Retornos E2 |
| RF-016 | Costo real por km/viaje/ruta/contrato y costo consolidado por viaje en 24 h con faltantes explícitos (FEP03 RT-05.29); versionado propuesto por validar. | Pendiente de verificación | ETL; Conciliación; Lakehouse; FACT_COSTO_VIAJE | SD3 · Costeo operacional |
| RF-017 | Separación de costos propios y de terceros. | Pendiente de verificación | FACT_COSTO_VIAJE; DIM_PROPIEDAD_FLOTA; Tarifas | SD3 · Modelo de costos |
| RF-018 | Explicación de dispersión de rendimiento. | Pendiente de verificación | Lakehouse; Capa Semántica; Conciliación GPS | SD3 · Rendimiento E2 |
| RF-019 | Liquidación automática por excepción. | Pendiente de verificación | Liquidaciones; Transportista; ACL | SD3 · Liquidación |
| RF-020 | Portal segregado de viajes y liquidación. | Pendiente de verificación | Portal; Entra ID; Transportista | SD3 · Portal transportista |
| RF-021 | Seguimiento del cliente sujeto a autorización. | Pendiente de verificación | Portal; Entra ID; Consentimiento; Telemetría | SD3 · Portal cliente |
| RF-022 | Consentimiento granular, revocable y auditable. | Pendiente de verificación | Consentimiento; Portal; Auditoría; Entra ID | SD3 · Soberanía de datos |
| RF-023 | CO2e verificable por tonelada-kilómetro, incluidos terceros, con consolidación mensual; base/metodología E1 y productivo completo E2, propuesta no ratificada. | Pendiente de verificación | Lakehouse; Capa Semántica; motor por definir | SD3 · Emisiones E1/E2 |
| RF-024 | Intervenciones de talleres externos registradas offline. | Pendiente de verificación | Interfaz Taller; Aplicación Móvil; Gestión de Flota | SD3 · Talleres E2 |
| RF-025 | Mantenimiento por kilometraje real trazable. | Pendiente de verificación | Gestión de Flota; rFMS; Telemetría | SD3 · Mantenimiento |
| RF-026 | Adhesión de transportistas gestionada y medible. | Pendiente de verificación | Portal; Transportista; Consentimiento | SD3 · Plan de adhesión |
| RF-027 | Alerta de jornada según lugar seguro alcanzable. | Pendiente de verificación | Unidad Telemática; Búfer; Control de Jornada | SD3 · Lugares seguros |
| RF-028 | Convivencia de validación telemática y documental. | Pendiente de verificación | Despacho; Portal; Unidad; Gestión Documental | SD3 · Operación mixta |
| RNF-001 | Cero interacción del conductor durante la marcha. | Pendiente de verificación | Unidad Telemática; Identificación; Aplicación Móvil | SD3 · Seguridad de interfaz |
| RNF-002 | Operación offline íntegra e idempotente. | Pendiente de verificación | Búfer; SQLite WAL; Event Hubs; caché | SD3 · Resiliencia |
| RNF-003 | Sin intervención de terceros sin acuerdo expreso. | Pendiente de verificación | Consentimiento; IoT Hub; Portal | SD3 · Límites de intervención |
| RNF-004 | Intervención durante paso normal por terminal. | Pendiente de verificación | Kits; IoT Update; despliegue progresivo | SD3 · Despliegue |
| RNF-005 | Integración vehicular de solo lectura y autorizada. | Pendiente de verificación | rFMS; acoplador; CAN/FMS | SD3 · Integración vehicular |
| RNF-006 | ERP como emisor único e integración idempotente. | Pendiente de verificación | ACL; Adaptador ERP; Broker; DLQ | SD3 · Integración tributaria |
| RNF-007 | Sin equipos ni procedimientos impuestos en clientes. | Pendiente de verificación | Unidad Telemática; Geocercas; Aplicación Móvil | SD3 · Instalaciones externas |
| RNF-008 | Continuidad ante cierre fronterizo de 12 días. | Pendiente de verificación | Búfer; Unidad Telemática; sala secundaria | SD3 · Continuidad |
| RNF-009 | Administrable por el equipo TI de nueve personas. | Pendiente de verificación | Azure administrado; Monitor; Grafana; Arc | SD3 · Modelo operativo |
| RNF-010 | TCO completo de 36 meses. | Pendiente de verificación | Cost Management; FinOps; modelo D4 | SD3 · TCO |
| RNF-011 | Despliegue sin detención global y reversible. | Pendiente de verificación | Device Twins; IoT Update; despliegue progresivo | SD3 · Implantación |
| RNF-012 | Auditoría probatoria sin sobrescritura. | Pendiente de verificación | Auditoría Append-Only; auditoria_evento; WORM | SD3 · Auditoría |
| RNF-013 | Minimización, segregación y cifrado de datos. | Pendiente de verificación | Entra ID; Key Vault; APIM; AES-256-GCM | SD3 · Seguridad y privacidad |
| RNF-014 | Retención y eliminación diferenciadas por dominio. | Pendiente de verificación | Matriz de Retención; WORM; crypto-shredding | SD3 · Ciclo de vida de datos |

## Controles pendientes

- [ ] Incorporar cada requisito textual aplicable de FEP02 y FEP03.
- [ ] Confirmar los valores admitidos en `Cumple` para la entrega; el estado interno no implica aprobación del formato final.
- [ ] Reemplazar las secciones `SD3` por numeración definitiva del informe.
- [ ] Ratificar componentes con D3 y D4.
- [ ] Eliminar todo “por definir” antes de la entrega final.
- [ ] Confirmar que cada fila coincide con catálogo y trazabilidad.
- [ ] Cerrar brechas con evidencia localizada antes de declarar cumplimiento; no trasladar compromisos o hipótesis como resultados verificados.
- [ ] Validar documento conforme previo al movimiento, costeo conforme en 24 h y distribución propuesta de emisiones E1/E2.
