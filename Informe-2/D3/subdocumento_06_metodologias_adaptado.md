# 6. Introducción a las metodologías

Para el proyecto de modernización tecnológica de Transportes Curimón S.A. (licitación TFEP-01/2026, Caso 10 Transporte de Carga), audIT Soluciones Tecnológicas SpA aplica un esquema de trabajo híbrido. La gobernanza contractual, adquisiciones y control formal de cambios se administran bajo los estándares de PMBOK 7.ª Edición. En paralelo, el ciclo de construcción y entrega de software opera con Scrum, Kanban y un pipeline DevSecOps sobre GitLab CI Enterprise.

Este diseño responde a las restricciones operativas de Curimón: una flota de 374 camiones (61 con telemetría de fábrica), 96.000 viajes al año, servicio ininterrumpido 24x7 y un plazo contractual de 56 meses organizado en dos etapas con despliegue concurrente.

> **Resumen ejecutivo**
>
> El modelo de gestión compatibiliza compromisos contractuales de precio cerrado con el desarrollo iterativo del software. La Etapa 1 concluye y se estabiliza en el mes 15 tras tres meses de marcha blanca. La Etapa 2 finaliza su marcha blanca de dos meses en el mes 20; el mes 21 se establece como hito de aceptación final y de inicio formal de los 36 meses de operación y soporte continuo bajo los SLA vinculantes de las Bases (FEP01 · Artículo 20° · p. 14 y FEP01 · Artículo 78.2° · p. 40), correspondiente a un 99,9% de disponibilidad para servicios Críticos (despacho, telemetría y jornada) y 99,5% para servicios Altos.
>
> Entre los meses 16 y 20, durante la coexistencia de la producción de Etapa 1 con el desarrollo y marcha blanca de Etapa 2, la operación en vivo de Etapa 1 está plenamente cubierta bajo un régimen de **Garantía Técnica e Hiperatención Operativa (Hypercare)** con los mismos SLA vinculantes de producción (99,9% crítico, 99,5% alto), célula de soporte técnico 24/7 y la matriz contractual de tiempos de respuesta de incidentes del Artículo 78°.
>
> **Régimen de adquisiciones y hardware (Formulario T-11):** conforme al pliego de licitación (Caso 10, capítulo 11, p. 24), **todo el equipamiento físico (computadores a bordo, módems satelitales, lectores CAN, servidores y gabinetes) es adquirido directamente por el CLIENTE (Transportes Curimón S.A.)**. audIT provee la especificación técnica rigurosa de compra (Formulario T-11), supervisión, kits de instalación y despliegue técnico. La plataforma vehicular unificada corresponde al **iWave G26I con SoC NXP i.MX 6ULL, 512 MB de RAM y 8 GB de almacenamiento eMMC**.
>
> **Cronograma riguroso de instalación a bordo (alineado con S7):** el montaje físico en la flota vehicular se ejecuta de forma modular sin detención de operaciones: piloto de 10 camiones propios en el mes 6; instalación en el resto de los 148 camiones propios entre los meses 6 y 9; instalación en 34 camiones de terceros en comodato entre los meses 7 y 10; **pausa contractual estricta de no intervención de camiones entre los meses 11 y 15 (temporada alta de fruta de Curimón, prohibición absoluta de inmovilizar flota)**; y reanudación de montaje de flota remanente entre los meses 16 y 18.
>
> **Entregables y compromisos principales:**
> - Gestión híbrida: PMBOK para gobernanza, contratos y control de cambios (Art. 72°), con sprints quincenales Scrum y flujo visual Kanban para desarrollo de software.
> - Cumplimiento del Artículo 17°: Etapa 1 con 12 meses de desarrollo y 3 meses de marcha blanca (M13 a M15); Etapa 2 concurrente (M13 a M18) con 2 meses de marcha blanca (M19 a M20); paso a producción definitivo en el mes 21.
> - Soporte ininterrumpido en producción: régimen de Garantía Técnica y Hypercare en meses 16 a 20 con SLA de 99,9% crítico, empalmando sin discontinuidad con los 36 meses de operación formal (M21 a M56).
> - Métrica unificada de asignación: validación interna en memoria en menos de 2 segundos (camino nominal ~660 ms); presupuesto transaccional de extremo a extremo de 25 segundos (RT-09.01).
> - Pipeline DevSecOps: integración y entrega continua en GitLab CI con runners efímeros, análisis SAST, escaneo de dependencias (SCA) y pruebas dinámicas DAST.
> - Cuatro ambientes del ciclo de vida del software (DEV, QA, PREPROD y PROD) más DR como entorno operativo de recuperación en Azure Brazil South, promoviendo contenedores inmutables validados mediante firmas criptográficas (Cosign) y atestaciones SLSA Build L3.
> - Gobierno del proyecto: cinco instancias formales de gobernanza (cuatro comités de gestión de proyecto y una mesa operativa diaria de terreno), emisión de actas en menos de 24 horas y control de cambios formal con tope del 20% del valor del contrato.

Este documento sintetiza la propuesta técnica para el Formulario T-9 (Metodología para la Administración y Gestión del Proyecto) y el Formulario T-10 (Metodología para el Desarrollo), en coordinación con el Subdocumento 4 (Arquitectura), Subdocumento 5 (Datos), Subdocumento 7 (Plan de Trabajo) y Subdocumento 9 (Calidad y Pruebas).

## 6.1 Metodología de gestión de proyectos

### 6.1.1 Gobierno, hitos y solapamiento contractual

La planificación cumple las restricciones de calendario del Artículo 17° de las Bases Administrativas (FEP01 p. 12) y las condiciones del Caso 10. La Figura 6.1 muestra la secuencia de etapas, los periodos de desarrollo y las ventanas de marcha blanca.

![Figura 6.1. Hitos, solapamiento de etapas y marcha blanca](./figuras/6-1-hitos.png)

Fuente: elaboración propia.

#### Cronograma de etapas y marcha blanca (Art. 17°)

El plan se organiza en dos etapas secuenciales y concurrentes:

- **Etapa 1 (meses 1 a 15):**
  - *Desarrollo e implantación (meses 1 a 12):* levantamiento de procesos, arquitectura base e integración con el sistema de transporte de 2013 y sistema contable mediante la Capa Anticorrupción.
  - *Montaje físico a bordo (meses 6 a 10):* piloto de 10 camiones propios en el mes 6; montaje en los 138 camiones propios restantes entre los meses 6 y 9; instalación en 34 camiones de terceros en comodato entre los meses 7 y 10.
  - *Pausa obligatoria de montaje (meses 11 a 15):* **prohibición contractual absoluta de intervenir camiones durante la temporada alta de fruta (diciembre a abril)**. Durante esta ventana, las actividades sobre flota se limitan exclusivamente a integración de software y telemetría por plataforma sin tocar vehículos físicamente.
  - *Marcha blanca de Etapa 1 (meses 13 a 15, 90 días):* operación en faena en paralelo al sistema legado, calibración de validaciones de despacho en memoria interna en menos de 2 segundos, estabilización de ingesta telemática y verificación documental.
  - *Paso a producción de Etapa 1:* inicio del mes 16.
- **Etapa 2 (meses 13 a 20):**
  - *Desarrollo concurrente (meses 13 a 18):* se ejecuta en paralelo con la marcha blanca de la Etapa 1. Desarrolla el portal de liquidación y sobreestadías, optimización de retornos (RF-015), explicabilidad de dispersión de combustible (RF-018), mantenimiento por odómetro real y cálculo de CO2e (ISO 14083).
  - *Reanudación de montaje físico remanente (meses 16 a 18):* instalación a bordo para transportistas terceros adheridos de forma rezagada al plan de comodato.
  - *Marcha blanca de Etapa 2 (meses 19 a 20, 60 días):* pruebas de liquidación de fletes con transportistas externos y conciliación contable peso a peso con el sistema contable.
  - *Paso a producción formal y aceptación final definitiva:* mes 21.

#### Operación en producción de Etapa 1 durante los meses 16 a 20

Entre los meses 16 y 20, el núcleo de despacho, telemetría y evidencia de jornada de la Etapa 1 se encuentra operando en producción comercial activa en faenas reales de Curimón, coexistiendo con el desarrollo y la marcha blanca de la Etapa 2. Para garantizar continuidad operacional absoluta sin vacíos de cobertura contractual, este período se rige formalmente bajo el siguiente marco:

1. **Régimen de Garantía Técnica e Hiperatención Operativa (Hypercare):** el servicio en producción de la Etapa 1 está completamente respaldado por audIT bajo régimen de garantía técnica y soporte de estabilización, financiado dentro de la partida de implantación sin costos adicionales para Curimón.
2. **SLA vinculantes de producción (FEP01, Art. 20° y Art. 78.2°):**
   - **Servicios Críticos (99,9 % de disponibilidad mensual):** verificación bloqueante de despacho, ingesta telemática en tiempo real, registro de evidencia de jornada y enlace con el sistema contable para el DET.
   - **Servicios Altos (99,5 % de disponibilidad mensual):** visualización en torre de control, consultas de geocercas y reportes operacionales diurnos.
3. **Célula de Soporte de Producción 24/7:** equipo dedicado integrado por 4 ingenieros de soporte (Nivel 2 y Nivel 3) con cobertura ininterrumpida 24x7, monitoreo proactivo mediante Azure Monitor / Grafana y mesa de ayuda operativa para operadores de romana, despachadores y conductores.
4. **Matriz de Severidad y Tiempos de Respuesta (Artículo 78°):**
   - **Severidad 1 (Crítica - bloqueo de despacho o caída de ingesta telemática):** tiempo de respuesta inicial ≤ 15 minutos; tiempo de solución técnica o workaround seguro ≤ 2 horas.
   - **Severidad 2 (Alta - degradación de servicios sin detención de romana):** tiempo de respuesta ≤ 30 minutos; resolución ≤ 4 horas.
   - **Severidad 3 (Media - fallas parciales en reportes o pantallas secundarias):** tiempo de respuesta ≤ 2 horas; resolución ≤ 24 horas.
   - **Severidad 4 (Baja - consultas operativas o ajustes menores de interfaz):** tiempo de respuesta ≤ 4 horas; resolución coordinada en el siguiente sprint programado.
5. **Empalme con el Soporte Contractual Formal de 36 meses (meses 21 a 56):** al finalizar el mes 20 y obtenerse el acta de aceptación final conjunta de la solución integral (Etapas 1 y 2), el servicio empalma de forma inmediata e ininterrumpida con el período contractual de 36 meses de operación continua, soporte técnico y mantenimiento correctivo/evolutivo bajo los mismos SLA vinculantes del Artículo 78°.

#### Hito de renegociación contractual de 2027 (mes 21)

De acuerdo con el Caso 10 (numerales 13.2 y 17.5), dos de los tres principales contratos de clientes de Curimón operan con tarifas bajo costo por falta de trazabilidad en rutas y sobreestadías. Su renovación contractual debe realizarse durante 2027 (mes 21 del proyecto).

Para esa fecha, el módulo de costeo por viaje (iniciado en Etapa 1 y consolidado en Etapa 2) proporcionará a la Gerencia de Curimón una estimación preliminar de costo por viaje y kilómetro en ≤ 24 h (RT-05.29), con faltantes identificados (`AUSENTE = NULL`), junto con el historial de versiones consolidadas después de conciliar peajes y combustible, proporcionando datos objetivos e inmutables para renegociar tarifas sobre servicios que representan el 31% de los ingresos de la compañía.

#### Estructura de comités y cadencias de gobierno

El modelo de gobernanza articula cinco instancias formales de coordinación y toma de decisiones: cuatro comités de gestión de proyecto orientados a la supervisión estratégica, seguimiento operativo, control contractual de cambios y calidad técnica, complementados por una mesa operativa diaria de terreno para la coordinación ágil en faena y romana:

1. **Comité Directivo:** Gerencia General de Curimón, Director de Proyecto audIT y sponsor; mensual. Supervisa estrategia, hitos contractuales y escalamientos mayores.
2. **Comité de Seguimiento Operacional:** Jefe de Proyecto Curimón, Project Manager audIT y Líder QA; quincenal. Revisa EDT, costos, riesgos y asignación de recursos.
3. **Comité de Control de Cambios (CCB):** PM audIT, contraparte técnica Curimón y asesor legal; ordinario quincenal y, ante emergencia operativa, convocatoria dentro de 48 h. Resuelve RFC conforme al Art. 72°.
4. **Comité Técnico y de Arquitectura:** arquitecto audIT, líder TI Curimón y DevSecOps; semanal. Revisa interfaces, contratos de integración, seguridad y pases a PREPROD.
5. **Mesa de Operaciones y Romana:** despachadores Curimón y soporte de terreno audIT; diaria, 15 min. Coordina incidencias de terreno, enrolamiento de choferes y disponibilidad de dispositivos.

Todas las sesiones de comités formales generan un acta de acuerdos distribuida en un plazo máximo de 24 horas hábiles.

### 6.1.2 Interesados y plan de comunicaciones

El plan de gestión de interesados atiende los requerimientos operativos del proyecto: la adopción voluntaria del comodato por parte de transportistas subcontratados, la claridad de los descansos para conductores según la normativa laboral y la continuidad operativa requerida por la administración de Curimón:

- **Directorio y Gerencia General:** informe ejecutivo y reunión mensual del Director de Proyecto audIT sobre hitos, presupuesto y riesgos.
- **Transportistas subcontratados:** portal web y talleres quincenales a cargo del Gestor de Adopción; difusión de ventajas del comodato, liquidación transparente y derechos de privacidad bajo Ley 21.719.
- **Conductores:** aplicación móvil y charlas de inducción semanales o por enrolamiento, a cargo del Monitor de Terreno; uso de interfaz táctil, verificación de jornada y botón de modo privado.
- **Equipo TI Curimón (9 personas):** repositorio y wiki técnica con transferencia continua de conocimiento y reuniones semanales; capacitación en runbooks, infraestructura como código y monitoreo.
- **Jefes de Terminal y Romana:** consola operativa y coordinación diaria con el Líder de Despliegue; programación de ventanas de instalación y planes de contingencia.

### 6.1.3 Adquisiciones y control de cambios

#### Plan de adquisiciones de hardware físico (Formulario T-11)

**Régimen de adquisición de hardware:**
Conforme al pliego de licitación (Caso 10, capítulo 11, p. 24), **todo el hardware físico vehicular, de terminales y de sala técnica es adquirido directamente por el CLIENTE (Transportes Curimón S.A.)**. audIT especifica exactamente qué comprar, cuánto y con qué características en el Formulario T-11, además de ejecutar la homologación técnica, control de recepción, kits de montaje y puesta en servicio.

Lista de materiales formal concordante con el Formulario T-11:
1. **Equipos nuevos en flota (182 camiones):** 148 computadores a bordo industriales **iWave G26I (SoC NXP i.MX 6ULL, 512 MB RAM, 8 GB eMMC)** para la flota propia y 34 para transportistas terceros que ingresen al plan de comodato. Adquiere: CLIENTE.
2. **Repuestos en pañol (19 unidades):** reserva en frío en los talleres de San Bernardo y terminales regionales, calculada como el 10% del parque instalado (182 × 0,10 ≈ 19 unidades). El total de computadores a bordo adquiridos corresponde a 201 unidades. Adquiere: CLIENTE.
3. **Módems satelitales de contingencia (201 unidades):** 182 módems **Iridium Edge (SBD)** para cabina vehicular y 19 repuestos, conectados por RS232 al computador a bordo. Adquiere: CLIENTE.
4. **Lectores CAN sin contacto (201 unidades):** 182 kits inductivos **Technoton CANCrocodile** (SAE J1939) y 19 repuestos para lectura no invasiva. Adquiere: CLIENTE.
5. **Lectores de identificación del chofer (201 unidades):** 182 lectores **GAO RFID MIFARE DESFire 13,56 MHz** (RS485) y 19 repuestos. Adquiere: CLIENTE.
6. **Flota homologada por software (192 camiones):** vehículos subcontratados con GPS operativo de las tres plataformas de mercado existentes. Se integran mediante conectores y APIs de software, sin intervenir hardware vehicular (Restricción 3).

#### Procedimiento de control de cambios (Artículo 72°)

Cualquier ajuste a requerimientos, cronograma, arquitectura o especificaciones técnicas sigue el flujo establecido en el Artículo 72° de las Bases Administrativas (FEP01 p. 38), formalizado en la Tabla 6.1.

**Tabla 6.1.** Procedimiento de control de cambios (Artículo 72°)

| Fase del proceso | Responsable | Plazo máximo | Actividad y criterio técnico |
|---|---|---|---|
| 1. Solicitud Formal (RFC) | Curimón o audIT | Día 1 | Ingreso de solicitud formal justificando necesidad operativa, técnica o legal en plataforma GitLab. |
| 2. Evaluación de impacto | Equipo técnico audIT | Hasta 5 días hábiles | Análisis exhaustivo de impacto en alcance, cronograma (EDT), costos, SLA contractual (Art. 78°), seguridad y Ley 21.719. |
| 3. Dictamen del CCB | Comité de Cambios (CCB) | Hasta 3 días hábiles | Sesión ordinaria con resolución fundada de aprobación, rechazo o solicitud de aclaraciones. |
| 4. Aprobación del mandante | Representante Curimón | Hasta 5 días hábiles | Pronunciamiento formal, firma de la orden de cambio contractual e incorporación a la línea base. |
| 5. Implementación y cierre | PM y líder técnico audIT | Según plan aprobado | Despliegue en ambientes DEV/QA, pase controlado a producción y actualización de la línea base en la EDT. |

Fuente: elaboración propia.

#### Diferenciación de circuitos: Trámite Ordinario versus Emergencia Operativa

1. **Circuito Ordinario (hasta 13 días hábiles en total):** aplica a modificaciones de alcance, mejoras funcionales o ajustes de cronograma no urgentes. Suma la evaluación técnica (5 días), el dictamen del CCB (3 días) y la aprobación del mandante (5 días).
2. **Procedimiento Acelerado de Emergencia (máximo 48 horas):** ante incidentes críticos de producción (P1), detenciones imprevistas en romana o requerimientos normativos sobrevinientes con amenaza inminente a la continuidad del despacho, el CCB se autoconvoca en un plazo máximo de 48 horas, emitiendo una resolución preliminar de mitigación en menos de 24 horas y regularizando la orden de cambio administrativa en los 5 días subsiguientes.

Criterios contractuales aplicables:
- El valor acumulado de las órdenes de cambio no puede superar el 20% del valor total original del contrato (Artículo 72°).
- Las políticas de escalamiento automático en Azure (HPA en AKS y particiones en Event Hubs) constituyen parámetros operativos y no requieren orden de cambio contractual.
- Disponibilidad contractual del servicio: compromiso vinculante con los niveles de servicio de las Bases (FEP01 · Artículo 20° y Artículo 78.2°): **99,9% de disponibilidad para servicios Críticos** y **99,5% para servicios Altos**.

### 6.1.4 Cadencias, ceremonias y artefactos ágiles

El equipo de desarrollo trabaja bajo Scrum con iteraciones de dos semanas:
- **Sprint Planning (lunes de inicio, 4 horas):** el Product Owner y el equipo seleccionan ítems del Product Backlog priorizados por valor y riesgo, acordando el objetivo del sprint (*Sprint Goal*).
- **Daily Standup (diario, 15 minutos):** reunión breve para coordinar el trabajo del día, detectar bloqueos y comprobar el estado de las ramas de desarrollo.
- **Backlog Refinement (semanal, 2 horas):** partición de épicas en historias de usuario, estimación de esfuerzo y validación del criterio de preparación (*Definition of Ready*).
- **Sprint Review (viernes de cierre, 2 horas):** demostración del incremento desplegado en Preproducción (PREPROD) ante el equipo técnico de Curimón.
- **Sprint Retrospective (viernes de cierre, 1 hora):** revisión interna del proceso de trabajo y acuerdos de mejora técnica.
- **Artefactos del marco:** Product Backlog en GitLab Issues, Sprint Backlog en tablero Kanban e Incremento de Software validado según la *Definition of Done* (cobertura unitaria ≥ 80%, escaneo SAST limpio de fallas críticas y contratos OpenAPI al día).

## 6.2 Metodología de desarrollo de software

### 6.2.1 Pipeline DevSecOps y separación de cuatro ambientes SDLC y DR

El ciclo de desarrollo utiliza un pipeline de integración y despliegue continuo implementado en GitLab CI Enterprise, según el flujo de la Figura 6.2.

![Figura 6.2. Pipeline DevSecOps y promoción entre ambientes](./figuras/6-2-pipeline.png)

Fuente: elaboración propia.

#### Ambientes del ciclo de desarrollo (SDLC) y entorno operativo de recuperación (DR)

El sistema opera con cuatro ambientes segregados para el ciclo de vida del software (DEV, QA, PREPROD y PROD), complementados por un entorno operativo de contingencia y recuperación ante desastres (DR) en Azure Brazil South que replica la configuración inmutable de producción:

1. **DEV (Desarrollo):** pruebas unitarias y trabajo sobre ramas de características. Utiliza bases de datos locales con datos sintéticos; no tiene acceso a datos de producción.
2. **QA (Pruebas de calidad):** pruebas de integración, contratos OpenAPI/AsyncAPI y reglas de dominio. Utiliza datos sintéticos o bases anonimizadas.
3. **PREPROD (Preproducción / Staging):** réplica exacta de Producción en capacidad de cómputo, red y topología. Alberga pruebas dinámicas DAST, pruebas de carga con k6 y ensayos previos de migración (*Mock Runs*).
4. **PROD (Producción):** entorno activo en Azure Chile Central. Los pases a producción promueven la imagen validada en PREPROD y verifican su digest criptográfico SHA-256.
5. **DR (Disaster Recovery):** entorno operativo espejo de contingencia y recuperación en Azure Brazil South (objetivos RTO ≤ 4 horas y RPO ≤ 15 minutos, sujetos a simulacro cronometrado). No recibe despliegues directos desde desarrollo, sino que replica la infraestructura inmutable mediante plantillas Terraform e imágenes firmadas de PROD, con claves maestras gestionadas bajo protocolo Break-Glass.

#### Cadena de suministro de software y SLSA Build L3

Para proteger la integridad de las aplicaciones frente a vulnerabilidades en dependencias y compilación, el pipeline adopta los lineamientos de SLSA Build v1.1 Nivel 3:
- **Runners efímeros:** las compilaciones corren en contenedores temporales con privilegios mínimos, destruidos automáticamente tras finalizar cada tarea.
- **Atestaciones de procedencia:** cada compilación genera un registro inmutable que certifica el repositorio de origen, commit SHA, parámetros y ambiente de construcción.
- **Inventario de dependencias (SBOM):** generación automática de SBOM en formato CycloneDX v1.5 para catalogar librerías directas y transitivas.
- **Firma con Cosign:** las imágenes de contenedor se firman criptográficamente mediante Cosign con llaves custodiadas en Azure Key Vault HSM. Los clústeres de AKS implementan políticas de admisión (Kyverno) que bloquean la ejecución de imágenes sin firma válida o sin atestación de origen.

### 6.2.2 Despliegue con reducción de interrupciones, canary y reversión automática

Para reducir el riesgo de interrupción durante las actualizaciones productivas, se aplican tres mecanismos:
- **Despliegues canary:** las versiones nuevas se dirigen primero al 10% del tráfico o a un terminal específico. Durante 60 minutos se supervisan tasas de error y latencia antes de extender el despliegue al resto del sistema.
- **Migraciones de base de datos con patrón Expand-Contract:** las modificaciones de esquema en PostgreSQL se dividen en adición de columnas, migración asíncrona de datos y retiro posterior de campos antiguos, permitiendo la coexistencia de versiones consecutivas de la aplicación.
- **Reversión automática:** el controlador de despliegue en AKS revierte los pods a la versión previa si los errores HTTP 5xx superan el 1% o si la latencia transaccional del despacho excede los 25 segundos.

### 6.2.3 Criterios de entrada, salida y métricas DORA

El avance entre ambientes está regido por compuertas de calidad:
- **Entrada a QA:** pruebas unitarias con cobertura de código ≥ 80%, análisis estático en SonarQube sin observaciones críticas o bloqueantes, y escaneo de vulnerabilidades en dependencias (Trivy) sin CVEs críticos.
- **Entrada a PREPROD:** pruebas de integración completadas, contratos de interfaces verificados y compatibilidad de esquema de base de datos validada.
- **Entrada a PROD:** escaneo dinámico DAST (OWASP ZAP) sin hallazgos altos o críticos, pruebas de rendimiento con k6 validando respuestas en memoria interna en menos de 2 segundos para 350 usuarios simultáneos, aprobación del Comité de Cambios y verificación de firma digital en el contenedor.

#### Métricas de desempeño de ingeniería (DORA)

La gestión de ingeniería se evalúa mediante cuatro indicadores:
- **Frecuencia de despliegue (Deployment Frequency):** quincenal a producción (al cierre de cada iteración) y continua en entornos de prueba.
- **Tiempo de entrega de cambios (Lead Time for Changes):** inferior a 5 días hábiles desde el commit hasta su disponibilidad en PREPROD.
- **Tasa de fallos en cambios (Change Failure Rate):** menor al 10% de las publicaciones a producción.
- **Tiempo medio de recuperación (MTTR):** inferior a 60 minutos ante incidentes productivos mediante reversión automatizada de versiones.

## 6.3 Correspondencia con los formularios T-9 y T-10

La siguiente correspondencia permite ubicar los contenidos de los Formularios T-9 y T-10 en este subdocumento (FEP01, p. 61).

- **T-9 — Gobernanza, instancias y cadencias:** §6.1.1.
- **T-9 — Interesados y comunicaciones:** §6.1.2.
- **T-9 — Adquisiciones y control de cambios:** §6.1.3.
- **T-9 — Ceremonias y artefactos ágiles:** §6.1.4.
- **T-10 — Ciclo de vida, pipeline DevSecOps e infraestructura como código:** §6.2 y §6.2.1.
- **T-10 — Ambientes segregados:** cuatro ambientes SDLC (DEV, QA, PREPROD y PROD), más DR como entorno operativo de contingencia; §6.2.1.
- **T-10 — Despliegue canary, reversión, compuertas de calidad y métricas DORA:** §§6.2.2–6.2.3.

## Referencias

- Google. (2025). *Supply-chain Levels for Software Artifacts (SLSA)* (Build Track v1.1). OpenSSF. https://slsa.dev/spec/v1.1/
- OWASP Foundation. (2021). *OWASP Application Security Verification Standard* (ASVS Version 4.0.3). OWASP. https://owasp.org/www-project-application-security-verification-standard/
- Project Management Institute. (2021). *A Guide to the Project Management Body of Knowledge (PMBOK Guide)* (7.ª ed.). Project Management Institute.
- Schwaber, K., & Sutherland, J. (2020). *The Scrum Guide: The Definitive Guide to Scrum: The Rules of the Game*. Scrum.org.
- Forsgren, N., Humble, J., & Kim, G. (2018). *Accelerate: The Science of Lean Software and DevOps: Building and Scaling High Performing Technology Organizations*. IT Revolution Press.

## Declaración de uso de IA

En conformidad con el Comunicado 09 y el Comunicado 10 (§7.2), se declara el uso asistido de herramientas de inteligencia artificial generativa durante la estructuración metodológica de este subdocumento. La definición de los marcos de gobierno, el cronograma de etapas alineado con las restricciones del Caso, el régimen de operación y soporte de Etapa 1, la especificación de compras del Formulario T-11 y los parámetros DevSecOps fueron realizados y aprobados por la Dupla 3 (DevSecOps & Software/Datos) en coordinación con la Dupla 2 (PMO) y la Dupla 4 (Infraestructura).
