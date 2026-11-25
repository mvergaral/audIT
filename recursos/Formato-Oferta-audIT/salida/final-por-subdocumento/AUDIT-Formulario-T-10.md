# Formulario T-10. Metodología para el desarrollo

Oferta final de audIT. Anexo del Subdocumento 6.

| Contenido exigido | Desarrollo en S6 |
|---|---|
| Ciclo de vida, requerimientos, arquitectura evolutiva y deuda técnica | sección 6.2.1 |
| DevSecOps y automatización de pruebas | sección 6.2.2 |
| Infraestructura y configuración como código | sección 6.2.3 |
| Criterios de ingeniería, Definición de Preparado y Definición de Terminado | sección 6.2.4 |
| Cadencias, promoción, reversión y métricas de entrega | sección 6.2.5 |

La Tabla 6.2 propone una secuencia verificable de incrementos. Cada fila es una línea base de planificación que se ratifica con la contraparte en el refinamiento; no afirma pruebas ya ejecutadas. Los requisitos y prioridades proceden de T-12, las duraciones de A09/A20 de T-15 y las pruebas de S9/T-17.

**Tabla 6.2.** Incrementos iniciales de A09 y A20 por sprint

| Sprint | Requisitos T-12 | Incremento y dependencia principal | Prueba, revisor y salida |
|---|---|---|---|
| A09-1 | RF-005, RF-022 | Maestros con propietario, permisos y roles; depende de contratos de identidad | CP-SYS-08 y CP-SEC-04; TI y Prevención; sin permisos cruzados |
| A09-2 | RF-002, RF-003, RF-004 | Evidencia de jornada, origen y custodia; depende de maestros | CP-SYS-05 y CP-SEC-08; Prevención; evidencia reconstruible |
| A09-3 | RF-001, RF-028 | Veredicto de asignación por modalidad; depende de jornada y activos | CP-SYS-01 y CP-UAT-09; torre; veredicto y motivo registrados |
| A09-4 | RF-007, RF-008, RF-009 | Captura a bordo y vista de flota; depende de equipos homologados | CP-SYS-16 y CP-PERF-02; torre y TI; sin pérdida/duplicación |
| A09-5 | RF-010, RF-011, RF-012 | Geocerca, espera y entrega; depende de puntos y contratos | CP-SYS-03 y CP-SYS-04; Operaciones; eventos conciliados |
| A09-6 | RF-006, RF-013, RF-014 | Carga peligrosa y documento emitido por contable; depende de su interfaz | CP-SYS-06 y CP-HW-11; torre; emisor correcto |
| A09-7 | RF-026, RF-027; G13 | Adhesión, alerta y versión de entrenamiento con cinco flujos | CP-UAT-09 y CP-UNIT-18; conductor y transportista; candidato para G13-Q |
| A09-8 | RF-016, RF-017, RF-019, RF-020 | Costeo inicial, liquidación y portal; integración de E1 | CP-INT-23, CP-SYS-10 y CP-SEC-07; Finanzas y torre; candidato H4 |
| A20-1 | RF-015, RF-018 | Retorno y análisis de rendimiento; datos E1 conciliados | CP-SYS-09 y CP-PERF-09; Operaciones; cálculo explicable |
| A20-2 | RF-021, RF-023 | Vista del cliente y emisiones con método declarado | CP-SYS-19 y CP-SYS-17; cliente y Finanzas; acceso limitado |
| A20-3 | RF-024, RF-025 | Taller externo y mantenimiento por kilometraje | CP-INT-17 y CP-UNIT-14; Mantenimiento; intervención auditable |
| A20-4 | RF-015 a RF-025 | Integración entre analítica, talleres y portales | Regresión T-17 de RF-015 a RF-025; TI y usuarios; defectos bloqueantes cerrados |
| A20-5 | RF-015 a RF-025 | Candidato E2, reversa y evidencias para H9 | Regresión T-17 y reversión; QA y titular funcional; acta de candidato |

A09-7 entrega el candidato el día hábil 180. Tras los dos días de G13-Q, se libera G13 en d182 y la práctica completa empieza en d192. A09-8 y A20-5 entregan candidatos para las revisiones de H4 y H9 previstas en T-15 y S9. Para cada sprint se registra por perfil la disponibilidad del T-15, las ausencias y guardias, y la capacidad neta: días-persona disponibles por foco acordado por 0,85. Para E2 se propone un foco inicial de 0,70, equivalente a 0,595 de la disponibilidad previa con la reserva de deuda. El Jefe de Proyecto y el titular funcional aprueban la carga al planificar el sprint. Si no cabe, registran el impacto y reordenan historias según criticidad y dependencias.

Cada incremento conserva ID T-12, contrato OpenAPI/AsyncAPI cuando corresponda, commit, revisión independiente, pruebas con resultado, SBOM, firma, digest y decisión de promoción. El pipeline en GitLab Premium Self-Managed revisa dependencias e infraestructura como código, pruebas y análisis estático con SonarQube Developer desde M4. Una historia comienza con dependencias, revisor y criterios definidos. QA bloquea promoción ante defectos de seguridad, integridad o cumplimiento. Se promueve el mismo artefacto firmado y se ensaya retorno al digest previo, conservando los datos.

En M21 a M56 el paquete 13.4 destina 160, 120, 80 y 40 horas variables de software por mes desde M21, M25, M33 y M45. La deuda técnica y las mejoras comparten esas horas. El Comité de Operación asigna capacidad mensual y conserva el factor anterior si hay incidentes P1, exceso de pendientes o demanda que no cabe en el tramo reducido. Antes de asignar deuda y mejoras se descuentan las reservas de cierre imputadas a la misma bolsa de T-15. La guardia, la corrección fija y los refuerzos específicos conservan su imputación.

En M21 a M24 se reservan 1.669 horas de cierre ya incluidas en la contratación: 879 para EDT 6.5 y 790 para EDT 7.2. La propuesta asigna 18, 17, 17 y 17 horas mensuales de conducción técnica a Gestión de Servicio. En H1 se debe acreditar su competencia de liderazgo de desarrollo y la cobertura del servicio restante, o designar un sustituto de igual capacidad y tarifa, según S7 y T-15.
