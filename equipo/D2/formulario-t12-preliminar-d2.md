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
D3/D4. La columna de sección apunta a los capítulos internos del Subdocumento 3
consolidado, en `subdoc3-esquema-solucion.md`, de modo que la referencia se mantiene
válida cualquiera sea la foliación global que adopte el informe impreso.

| ID requerimiento | Descripción | Cumple | Componente que lo satisface | Sección de la propuesta |
|---|---|---|---|---|
| RF-001 | Validación bloqueante de jornada, habilitaciones y aptitud. | Pendiente de verificación | Servicios de Despacho, Jornada, Flota y Gestión Documental | Cap. 3, Despacho seguro |
| RF-002 | Jornada acreditada de conductores propios y externos. | Pendiente de verificación | Control de Jornada; Conductor; Búfer a Bordo | Cap. 3, Expediente de jornada |
| RF-003 | Jornada previa externa disponible al asignar. | Pendiente de verificación | Control de Jornada; Conductor; Consentimiento | Cap. 3, Expediente de jornada y cap. 5.1 |
| RF-004 | Evidencia de jornada íntegra y sin sobrescritura. | Pendiente de verificación | Gestión Documental; Auditoría Append-Only; WORM | Cap. 3, Expediente de jornada |
| RF-005 | Registro único de vigencias con alerta y bloqueo. | Pendiente de verificación | Gestión Documental; MDM; Vigencias; WORM | Cap. 3, Registro único de vigencias |
| RF-006 | Carga peligrosa efectiva verificada contra manifiesto. | Pendiente de verificación | Orden de Transporte; Semirremolque; Despacho | Cap. 3, Despacho seguro |
| RF-007 | Descarga, asociación y conservación de tacógrafos. | Pendiente de verificación | Unidad Telemática; CAN/FMS; Gestión Documental | Cap. 3, Expediente de jornada |
| RF-008 | Vista única de posición de los 374 camiones. | Pendiente de verificación | Portal; Broker Streaming; Base de Telemetría | Cap. 3, Viaje y evidencia y cap. 5.6 |
| RF-009 | Registro local de 72 h y sincronización posterior. | Pendiente de verificación | Búfer a Bordo; Unidad Telemática; IoT Hub | Cap. 3, Operación desconectada |
| RF-010 | Llegada y salida automáticas en clientes. | Pendiente de verificación | Unidad Telemática; Geocercas; Telemetría | Cap. 3, Viaje y evidencia |
| RF-011 | Evidencia de espera y respaldo de sobreestadía. | Pendiente de verificación | Liquidaciones; Tarifas; Portal; WORM | Cap. 3, Viaje y evidencia y cap. 5.2 |
| RF-012 | Conformidad digital disponible el mismo día. | Pendiente de verificación | Aplicación Móvil; Búfer; WORM | Cap. 3, Viaje y evidencia |
| RF-013 | DET generado desde la orden sin redigitación. | Pendiente de verificación | Orden; ACL; Adaptador ERP; Transformador | Cap. 3, Integración tributaria |
| RF-014 | DET conforme antes del movimiento, incluso sin cobertura, con emisor contable único; bloqueo si falta. La emisión diferida no basta. | Pendiente de verificación | Búfer; ACL; Broker; DLQ; mecanismo conforme por definir y validar | Cap. 3, Integración tributaria y cap. 6 |
| RF-015 | Recomendación de retornos y reducción de vacío. | Pendiente de verificación | Lakehouse; Capa Semántica; optimizador por definir | Cap. 4.3, Etapa 2 |
| RF-016 | Costo real por km/viaje/ruta/contrato y costo consolidado por viaje en 24 h con faltantes explícitos, conforme a FEP03 RT-05.29, con historial de versiones. | Pendiente de verificación | ETL; Conciliación; Lakehouse; FACT_COSTO_VIAJE | Cap. 3, Costeo y liquidación y cap. 4.1 |
| RF-017 | Separación de costos propios y de terceros. | Pendiente de verificación | FACT_COSTO_VIAJE; DIM_PROPIEDAD_FLOTA; Tarifas | Cap. 3, Costeo y liquidación |
| RF-018 | Explicación de dispersión de rendimiento. | Pendiente de verificación | Lakehouse; Capa Semántica; Conciliación GPS | Cap. 4.3, Etapa 2 |
| RF-019 | Liquidación automática por excepción. | Pendiente de verificación | Liquidaciones; Transportista; ACL | Cap. 3, Costeo y liquidación y cap. 5.2 |
| RF-020 | Portal segregado de viajes y liquidación. | Pendiente de verificación | Portal; Entra ID; Transportista | Cap. 3, Portales y consentimiento y cap. 5.2 |
| RF-021 | Seguimiento del cliente sujeto a autorización. | Pendiente de verificación | Portal; Entra ID; Consentimiento; Telemetría | Cap. 3, Portales y consentimiento |
| RF-022 | Consentimiento granular, revocable y auditable. | Pendiente de verificación | Consentimiento; Portal; Auditoría; Entra ID | Cap. 3, Portales y consentimiento y cap. 5.3 |
| RF-023 | CO2e verificable por tonelada-kilómetro, incluidos terceros, con consolidación mensual; base y metodología en E1, cálculo productivo completo en E2. | Pendiente de verificación | Lakehouse; Capa Semántica; motor por definir | Cap. 4.1, reparto de emisiones |
| RF-024 | Intervenciones de talleres externos registradas offline. | Pendiente de verificación | Interfaz Taller; Aplicación Móvil; Gestión de Flota | Cap. 4.3, Etapa 2 |
| RF-025 | Mantenimiento por kilometraje real trazable. | Pendiente de verificación | Gestión de Flota; rFMS; Telemetría | Cap. 2, Coherencia problema-solución |
| RF-026 | Adhesión de transportistas gestionada y medible. | Pendiente de verificación | Portal; Transportista; Consentimiento | Cap. 5, Plan de adhesión |
| RF-027 | Alerta de jornada según lugar seguro alcanzable. | Pendiente de verificación | Unidad Telemática; Búfer; Control de Jornada | Cap. 3, Despacho seguro |
| RF-028 | Convivencia de validación telemática y documental. | Pendiente de verificación | Despacho; Portal; Unidad; Gestión Documental | Cap. 5.6, Modalidades de adhesión |
| RNF-001 | Cero interacción del conductor durante la marcha. | Pendiente de verificación | Unidad Telemática; Identificación; Aplicación Móvil | Cap. 1, Reglas de diseño |
| RNF-002 | Operación offline íntegra e idempotente. | Pendiente de verificación | Búfer; SQLite WAL; Event Hubs; caché | Cap. 3, Operación desconectada |
| RNF-003 | Sin intervención de terceros sin acuerdo expreso. | Pendiente de verificación | Consentimiento; IoT Hub; Portal | Cap. 5.3, Comodato y no intervención |
| RNF-004 | Intervención durante paso normal por terminal. | Pendiente de verificación | Kits; IoT Update; despliegue progresivo | Cap. 3, Implantación progresiva |
| RNF-005 | Integración vehicular de solo lectura y autorizada. | Pendiente de verificación | rFMS; acoplador; CAN/FMS | Cap. 6, Supuestos D-12 y D-13 |
| RNF-006 | ERP como emisor único e integración idempotente. | Pendiente de verificación | ACL; Adaptador ERP; Broker; DLQ | Cap. 3, Integración tributaria |
| RNF-007 | Sin equipos ni procedimientos impuestos en clientes. | Pendiente de verificación | Unidad Telemática; Geocercas; Aplicación Móvil | Cap. 7, Exclusiones |
| RNF-008 | Continuidad ante cierre fronterizo de 12 días. | Pendiente de verificación | Búfer; Unidad Telemática; sala secundaria | Cap. 3, Operación desconectada |
| RNF-009 | Administrable por el equipo TI de nueve personas. | Pendiente de verificación | Azure administrado; Monitor; Grafana; Arc | Cap. 3, Implantación progresiva |
| RNF-010 | TCO completo de 36 meses. | Pendiente de verificación | Cost Management; FinOps; modelo D4 | Cap. 5.3, Costos del comodato |
| RNF-011 | Despliegue sin detención global y reversible. | Pendiente de verificación | Device Twins; IoT Update; despliegue progresivo | Cap. 3, Implantación progresiva |
| RNF-012 | Auditoría probatoria sin sobrescritura. | Pendiente de verificación | Auditoría Append-Only; auditoria_evento; WORM | Cap. 3, Expediente de jornada |
| RNF-013 | Minimización, segregación y cifrado de datos. | Pendiente de verificación | Entra ID; Key Vault; APIM; AES-256-GCM | Cap. 3, Portales y consentimiento |
| RNF-014 | Retención y eliminación diferenciadas por dominio. | Pendiente de verificación | Matriz de Retención; WORM; crypto-shredding | Cap. 8, Criterios y verificación |

## Controles

Cerrados para el Informe 1.

- [x] Cada fila coincide con el catálogo y con la matriz de trazabilidad. Los 42
      identificadores cuadran en los tres documentos.
- [x] Cada fila apunta a un capítulo existente del Subdocumento 3 consolidado.

Abiertos, con su hito propio.

- [ ] Incorporar cada requisito textual aplicable de FEP02 y FEP03, en el alcance que
      determine la respuesta a la consulta sobre el Capítulo 3 transversal. Hito, Informe 2.
- [ ] Confirmar los valores admitidos en la columna `Cumple` del formato oficial. Hito,
      Acta de Respuestas a Consultas.
- [ ] Ratificar componentes con D3 y D4. Hito, lectura cruzada previa al Informe 2.
- [ ] Cerrar cada brecha con evidencia localizada antes de declarar cumplimiento, sin
      trasladar compromisos ni hipótesis como resultados verificados. Hito, oferta final
      del 25 de noviembre de 2026, cuando desaparece todo «por definir».
- [ ] Validar documento conforme previo al movimiento, costeo consolidado en 24 horas y
      distribución de emisiones entre E1 y E2. Hito, levantamiento de la Etapa 1.
