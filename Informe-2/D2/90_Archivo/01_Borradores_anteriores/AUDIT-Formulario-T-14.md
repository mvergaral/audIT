# Formulario T-14. Diccionario de la Estructura de Desglose del Trabajo

**Estado:** borrador para conciliación; no constituye línea base aprobada.  
**Vínculo:** Subdocumento 7, secciones 7.1–7.3.

El diccionario define los principales paquetes de trabajo. Los responsables se expresan por función corporativa y deben confirmarse al aprobar la línea base. Duraciones, fechas y asignaciones detalladas se completarán contra las Bases, T-11/T-12 y las confirmaciones de D3/D4.

| EDT | Paquete de trabajo | Resultado / evidencia | Dependencias principales | Criterio de aceptación |
|:---|:---|:---|:---|:---|
| 1.1.1 | Gobierno y control integrado | Planes, minutas, decisiones, cambios e informes versionados. | Acta de inicio y contraparte. | Decisiones, cambios y estado trazables; aprobaciones registradas. |
| 1.1.2 | Gestión de alcance y requisitos | Baseline T-12 y matriz de trazabilidad. | D2; aclaraciones del mandante. | 42 IDs únicos y cobertura confirmada; sin requisitos huérfanos. |
| 1.1.3 | Gestión de riesgos, calidad y configuración | Registros de riesgos, calidad, versiones y control documental. | D1/D3/D4. | Controles, responsables y evidencias definidos y revisados. |
| 1.2.1 | Arquitectura y decisiones de diseño | Arquitectura aprobada, decisiones y contratos. | S4.1/S4.2 de D3/D4. | Interfaces, límites y decisiones aprobados por las partes designadas. |
| 1.2.2 | Diseño funcional y experiencia de usuario | Flujos, reglas, prototipos y criterios de aceptación. | T-12 y usuarios clave. | Trazabilidad con requisitos y aprobación funcional documentada. |
| 1.3.1 | Ambientes e infraestructura base | Desarrollo, pruebas y producción configurados. | D4 y seguridad. | Acceso, monitoreo, respaldo y configuración verificados. |
| 1.3.2 | Identidad, seguridad y privacidad | Roles, controles, registros y procedimientos. | D3; revisión legal. | Pruebas de controles y excepciones aprobadas; evidencia archivada. |
| 1.3.3 | Integración y mensajería | Adaptadores, APIs/eventos, manejo de errores y reintentos. | Contratos D3 y sistemas del mandante. | Pruebas de integración/idempotencia aceptadas. |
| 1.4.1 | Despacho, jornada y habilitaciones | Reglas de predespacho y expediente de jornada. | RF-001–RF-007; interfaces fuente. | Casos obligatorios de bloqueo y autorización aprobados. |
| 1.4.2 | Flota, viajes y evidencia | Registro de estados de viaje, eventos y documentos. | RF-008–RF-012; datos de flota. | Escenarios funcionales y trazabilidad aceptados. |
| 1.4.3 | Integración tributaria/ERP | Adaptador hacia sistema contable emisor. | RF-013/RF-014; contraparte ERP. | Emisión única, idempotencia y contingencias probadas. |
| 1.4.4 | Costos, tarifas y liquidaciones | Cálculo de costos y liquidación según reglas aprobadas. | Requisitos de dominio y datos maestros. | Conciliación con casos de referencia aprobados. |
| 1.5.1 | Suministro y preparación de hardware | Equipos configurados y serializados. | T-11 y decisión de compra/entrega. | BOM, configuración, trazabilidad y prueba de recepción aceptados. |
| 1.5.2 | Instalación y homologación de flota | Registro por unidad y estado de instalación/homologación. | D4, transportistas y ventanas de terminal. | Inspección y prueba por unidad; no afectar operación ni garantía. |
| 1.5.3 | Conectividad y operación de borde | Captura, almacenamiento local y sincronización. | Hardware, D3 y requisito RT-03.10. | Retención mínima 72 h verificada; capacidad mayor solo tras validación. |
| 1.6.1 | Calidad y preparación de datos | Perfil, limpieza, mapeo y reglas de conciliación. | Acceso a fuentes históricas. | Reglas, excepciones y conteos aprobados antes de migrar. |
| 1.6.2 | Migración histórica TMS 2013 | Lotes migrados, reconciliación e informe de excepciones. | Datos fuente y estrategia de corte. | Totales y muestras conciliados; aceptación del dueño de datos. |
| 1.7.1 | Pruebas funcionales e integración | Casos, resultados, defectos y evidencias. | S9/T-17 y ambientes. | Criterios de salida y defectos bloqueantes resueltos. |
| 1.7.2 | Pruebas de carga, resiliencia y recuperación | Informes de pruebas reproducibles. | Dimensionamiento D4/D3 y umbrales D1. | SLA 99,9 %, RTO 4 h, RPO 15 min y 72 h offline verificados según protocolo aprobado. |
| 1.7.3 | UAT en terminales | Actas y hallazgos por terminal. | Usuarios, ambientes y ventanas H4. | Aprobación documentada en cada terminal dentro del alcance. |
| 1.8.1 | Formación y adopción | Materiales, sesiones y registros de asistencia. | Perfiles y plan de adopción. | Cobertura y evaluación según umbrales aprobados. |
| 1.8.2 | Despliegue y marcha blanca | Liberaciones, monitoreo, incidencias y acta de salida. | Aceptación Etapa 1 y calendario contractual. | 60 días solo si se confirma en línea base; criterios de salida satisfechos. |
| 1.9.1 | Innovación: ALNS | Paquete de algoritmo, integración y evaluación. | T-19, datos y objetivos aprobados. | Métricas de aceptación acordadas, medidas y revisadas. |
| 1.9.2 | Innovación: TwinMaker | Modelo/visualización y fuentes de datos acordadas. | Ficha de innovación D3 y arquitectura. | Demostración funcional y criterios de T-19 aceptados. |
| 1.9.3 | Innovación: DMS visión artificial | Componente, integración y protocolo de prueba. | Ficha D4, hardware y privacidad. | Pruebas de seguridad y desempeño aprobadas. |
| 1.9.4 | Innovación: PWA offline | Aplicación, sincronización y estados de conflicto. | Diseño y política de datos. | Pruebas offline/sync y accesibilidad aprobadas. |
| 1.9.5 | Innovación: monitoreo IoT de frío | Captura, alertas e informes de temperatura. | Sensores e integración D4. | Calibración, alarmas y trazabilidad aceptadas. |
| 1.10.1 | Transferencia y soporte | Manuales, operación, capacitación y escalamiento. | Criterios de aceptación y equipo Curimón. | Actas de transferencia y responsabilidades aprobadas. |
| 1.10.2 | Cierre contractual | Acta final, pendientes y archivo de evidencias. | Aceptación de entregables. | Cierre formal documentado por las partes. |

## Cobertura requerida por confirmar

La matriz de trazabilidad detallada que vincule los 42 requisitos RF/RNF a los paquetes se completa desde T-12 y se adjunta como anexo de control de la EDT. Los cinco terminales considerados son San Bernardo, Valparaíso, Concepción, Antofagasta y Puerto Montt. Cantidades de equipos, camiones, dispositivos, volumen/retención de datos y cronología de las innovaciones deben cotejarse con T-11, T-12, T-19 y las respuestas de D3/D4 antes de congelar el formulario.
