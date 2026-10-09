# Subdocumento 7. Plan de trabajo, EDT y cronograma

audIT, Empresa N.º 10. Licitación TFEP-01/2026, Caso 10 Transporte de Carga. Oferta Técnica, Sobre N.º 2. Informe 2. Anexos: Formularios T-14, T-15 y T-18.

## 7 Plan de trabajo, EDT y cronograma

Este subdocumento organiza los entregables, dependencias, recursos y mecanismos de control para implantar la solución descrita en el Subdocumento 3. La planificación se expresará en meses relativos al inicio contractual. Las fechas calendario y la línea base quedan sujetas a validación contra el plazo de las Bases, el acta de inicio y las dependencias que confirmen D1, D3 y D4.

### 7.1 Estructura de Desglose del Trabajo (EDT)

La EDT descompone el alcance contractual en entregables verificables y paquetes de trabajo estimables. Cada paquete deberá contar con código único, responsable corporativo, prerrequisitos, salida documentada, criterio de aceptación y relación trazable con los requisitos de T-12. El detalle de paquetes y reglas de control se presenta en T-14.

#### 7.1.1 Criterios de descomposición y control

La descomposición se realiza por entregable y resultado, no por actividad interna aislada. Las cuentas de control agrupan arquitectura, plataforma, datos, hardware, seguridad, pruebas, adopción y transición. Los paquetes que dependan de decisiones del mandante, sistemas legados o adhesión de terceros se identifican con una dependencia y una condición de entrada explícitas. Ningún paquete se considera terminado solo por haber consumido esfuerzo: debe satisfacer sus criterios de aceptación y aportar evidencia al repositorio controlado.

La cobertura de T-12, las cinco innovaciones, la migración histórica del TMS, la flota, los terminales y las pruebas se trazará a paquetes EDT en el Formulario T-14. Las cantidades y alcances de equipamiento se conciliarán con T-11 de D4; la arquitectura y el stack, con D3; y los criterios de calidad, con D1.

#### 7.1.2 Cuentas de control

| Código EDT | Cuenta de control | Resultado verificable |
|:---|:---|:---|
| 1.1 | Dirección, gestión y control integrado | Línea base, decisiones, riesgos, cambios, informes y cierre documentados. |
| 1.2 | Requisitos, arquitectura y diseño | Requisitos trazados, arquitectura aprobada e interfaces especificadas. |
| 1.3 | Plataforma, seguridad e integración | Ambientes, controles, servicios comunes e integraciones habilitados. |
| 1.4 | Capacidades funcionales de Etapa 1 | Capacidades de despacho, jornada, flota, documentos, ERP y costeo aceptadas para producción. |
| 1.5 | Hardware, conectividad y operación de borde | Unidades y terminales habilitados conforme al alcance aprobado por D4. |
| 1.6 | Datos, migración e interoperabilidad | Datos migrados, reconciliados y aceptados con trazabilidad. |
| 1.7 | Verificación, validación y aceptación | Evidencias de prueba y actas conforme a los criterios acordados con D1 y Curimón. |
| 1.8 | Adopción, despliegue y transición | Usuarios y transportistas preparados; transición y soporte documentados. |
| 1.9 | Capacidades de Etapa 2 | Innovaciones y capacidades diferidas implementadas y aceptadas conforme a su alcance. |
| 1.10 | Operación, transferencia y cierre | Transferencia, soporte, documentación y cierre contractual aceptados. |

#### 7.1.3 Trazabilidad de alcance

Cada requisito funcional y no funcional del T-12 se asociará a uno o más paquetes EDT. Las cinco innovaciones, el volumen de migración del TMS 2013, las actividades de hardware para flota propia y terceros, y las pruebas UAT en San Bernardo, Valparaíso, Concepción, Antofagasta y Puerto Montt también deberán quedar cubiertos. La asignación detallada se mantiene en T-14 y no se declara completa hasta que D3/D4 confirmen sus dependencias y entregables.

### 7.2 Plan de trabajo

El trabajo se ejecutará mediante líneas coordinadas de requisitos y diseño, construcción e integración, habilitación de hardware y datos, y verificación/adopción. La secuencia detallada se ajustará a las precedencias de T-18. Las iteraciones de desarrollo y sus ventanas de liberación se confirmarán con D3 antes de establecer calendarios de sprint.

#### 7.2.1 Estrategia de ejecución

1. **Preparación y línea base:** confirmar alcance, requisitos, arquitectura, EDT, calendario, recursos, riesgos y criterios de aceptación.
2. **Diseño y habilitación:** cerrar interfaces, ambientes, seguridad, aprovisionamiento, datos de prueba, logística de equipos y coordinación con el ERP.
3. **Construcción e integración:** implementar entregables priorizados, realizar revisiones y mantener trazabilidad requisito-código-prueba.
4. **Migración y habilitación de flota:** preparar, ejecutar y reconciliar migraciones y despliegues graduales con criterios de reversa y continuidad.
5. **Verificación y aceptación:** completar pruebas funcionales, integración, seguridad, carga, resiliencia, recuperación y UAT; registrar hallazgos y actas.
6. **Transición y operación:** realizar la marcha blanca prevista en el plan contractual validado, estabilizar el servicio y transferir procedimientos y conocimiento.

#### 7.2.2 Coordinación de recursos y dependencias

La asignación mensual de recursos y la curva de utilización se documentarán en T-15. El solapamiento entre estabilización/marcha blanca y construcción de la siguiente etapa se representará sin doble contabilizar personas ni superar la capacidad confirmada. La partición de células Alfa y Beta descrita en el Plan Maestro es una propuesta de organización que debe cotejarse con la dotación aprobada y el cronograma contractual antes de comprometerla.

Las dependencias clave comprenden: decisiones y especificaciones de D3 para arquitectura, APIs y pipeline; cantidades, instalación y modos de falla de D4; ventanas y criterios QA de D1; disponibilidad de contrapartes y sistemas del mandante; y adhesión/participación de los transportistas. Toda dependencia que afecte ruta crítica deberá tener responsable y fecha de resolución en T-18.

### 7.3 Cronograma e implantación

El cronograma maestro y su red de precedencias se documentan en T-18. Se informarán hitos, duración, predecesoras, holgura total y libre, ruta crítica, responsables y criterios de aceptación. Las fechas calendario se incorporarán después de verificar el plazo total establecido en las Bases y la fecha de inicio contractual; los meses de producción mencionados en S3/T-12 deben armonizarse con esa línea base.

La planificación debe contemplar pruebas de integración, carga, resiliencia, recuperación ante desastres y seguridad; UAT en los cinco terminales definidos; liberaciones controladas; y la marcha blanca de 60 días indicada por el Plan Maestro, una vez confirmada su ubicación en el plazo contractual. D1 recibirá mediante H4 las ventanas aprobadas para alinear S9, T-13 y T-17.

#### 7.3.1 Hitos de planificación

| Hito | Criterio de salida | Fecha / mes base |
|:---|:---|:---|
| Aprobación de línea base | Alcance, EDT, recursos, calendario y criterios aceptados. | Pendiente de conciliación con Bases y acta de inicio. |
| Diseño e interfaces aprobados | Arquitectura, contratos de integración y seguridad revisados. | Pendiente de dependencias D3/mandante. |
| Entorno integrado disponible | Ambientes, accesos, observabilidad y pipeline listos. | Pendiente de secuencia T-18 y handoff D3. |
| Pruebas de sistema y resiliencia | Criterios de entrada/salida y evidencias aprobados. | Ventanas a fijar en H4. |
| UAT en cinco terminales | Casos ejecutados, hallazgos tratados y actas por terminal. | Ventanas a fijar en H4. |
| Producción Etapa 1 | Requisitos obligatorios y aceptación de etapa satisfechos. | Mes contractual por confirmar. |
| Marcha blanca | Operación acompañada durante 60 días y criterios de salida cumplidos. | Ubicación en cronograma por confirmar. |
| Producción Etapa 2 | Capacidades diferidas verificadas y aceptadas. | Mes contractual por confirmar. |
| Transferencia y cierre | Documentación, soporte y responsabilidades transferidos. | Conforme al plazo contractual validado. |

La versión actual es un borrador estructural. T-14, T-15 y T-18 deben completarse y conciliarse antes de afirmar que existe una línea base aprobada o emitir H4 como calendario definitivo.
