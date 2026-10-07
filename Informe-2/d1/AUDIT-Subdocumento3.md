# Subdocumento 3. Esquema de solución y alcance

audIT, Empresa N.º 10. Licitación TFEP-01/2026, Caso 10 Transporte de Carga. Oferta Técnica, Sobre N.º 2. Informe Preparatorio 2. Archivo AUDIT-Subdocumento3.pdf. Anexos: Formulario T-12 en el archivo AUDIT-Formulario-T-12.pdf.

## 3 Esquema de solución y alcance

El presente capítulo formaliza el esquema integral de solución y la delimitación contractual del
alcance para la modernización de los sistemas operacionales de Transportes Curimón S.A.
La propuesta de audIT Soluciones Tecnológicas SpA establece el principio de correspondencia entre
responsabilidad y control, dotando a la compañía de medios probatorios verificables, integración
contractual no traumática con los transportistas terceros y resiliencia ante contingencias en ruta.
La sección 3.1 sintetiza el ciclo integral de la solución en sus fases de desarrollo, marchas blancas,
pasos a producción y operación continuada de 36 meses. La sección 3.2 descompone modularmente el alcance,
fijando los criterios de corte entre Etapa 1 y Etapa 2, las exclusiones explícitas, el catálogo de los 42
requerimientos canónicos y los criterios formales de aceptación. La sección 3.3 presenta el modelo conceptual
y los diagramas de arquitectura de solución. Finalmente, la sección 3.4 desarrolla la explicación
operacional y de negocio de la solución, demostrando plena coherencia con la problemática descrita en el
Capítulo 2, estableciendo la estrategia de adopción con los 148 transportistas terceros y garantizando el
mapeo unívoco con la arquitectura lógica del Capítulo 4.

El capítulo se articula directamente con el Formulario T-12, que acompaña esta entrega como archivo
independiente (`AUDIT-Formulario-T-12.pdf`), conforme al Comunicado 10, sección 1.

## 3.1 Resumen Ejecutivo de la Solución

La necesidad de compatibilizar fuentes heterogéneas y autonomía del transportista, diagnosticada en la sección 2.4 del Subdocumento 2, se atiende mediante ingesta por cada plataforma y homologación progresiva de compatibilidad. La adhesión se apoya en el expediente verificable y la transparencia de liquidaciones como incentivos, sin imponer el reemplazo de sistemas de terceros. Estos mecanismos son decisiones de solución: su cobertura depende de validar acceso, permisos y aptitud de los equipos, conforme a SUP-01 y SUP-02 del diagnóstico.

La solución diseñada por audIT Soluciones Tecnológicas SpA para Transportes Curimón S.A.
resuelve la brecha estructural de control identificada en el diagnóstico del negocio: la compañía
responde solidariamente ante clientes, fiscalizadores y tribunales por una operación en la cual el
60,4 % de la capacidad de transporte pertenece a 148 transportistas subcontratados y 258 de los 454
conductores no poseen vínculo de subordinación directa.
Frente a este escenario, la solución hace coincidir la responsabilidad con el control operacional
mediante evidencia probatoria auditable, adhesión contractual basada en beneficios compartidos y una
arquitectura tecnológica tolerante a desconexión prolongada.

El ciclo de vida del proyecto comprende tres fases claramente delimitadas en el tiempo contractual:
- **Fase de Implementación de la Etapa 1 (Meses 1 a 15):** Construcción del núcleo operacional
  seguro, saneamiento de las 6.000 vigencias en un registro único, consolidación del expediente digital de
  jornada, módulo de pre-despacho con validación bloqueante, telemetría inicial y conector con el sistema
  contable como único emisor tributario. Finaliza con una marcha blanca de 30 días continuos durante el mes 15.
- **Paso a Producción de la Etapa 1 e Inicio de Operación Continuada (Mes 16):** Entrada en
  régimen productivo de las capacidades de seguridad, despacho, viaje, facturación y costeo básico por viaje,
  iniciando el cómputo de los 36 meses de operación comprometidos FEP01, Artículo 17, p. 12.
- **Fase de Implementación y Paso a Producción de la Etapa 2 (Meses 17 a 21):** Desarrollo y
  despliegue de capacidades analíticas avanzadas, optimización heurística de retornos en vacío (ALNS),
  cálculo productivo integral de emisiones CO2e bajo norma ISO 14083 / GLEC y portal para talleres externos.
  Su paso a producción se formaliza en el mes 21 tras superar las pruebas de carga y aceptación de usuarios.

La operación continuada se extiende por 36 meses a contar de la recepción provisoria de la Etapa 1,
garantizando la estabilidad de la plataforma, el soporte a los 148 transportistas terceros y el cumplimiento
de los Acuerdos de Nivel de Servicio (SLA) de disponibilidad igual o superior al 99,5 % comprometidos en el Formulario T-6.

## 3.2 Alcance

El alcance del proyecto se estructura como una descomposición modular rigurosa que prioriza la mitigación de
riesgos regulatorios, laborales y tributarios en la primera etapa, postergando la optimización analítica y
el escalamiento masivo para la segunda etapa. A continuación se detallan los componentes, criterios de corte,
supuestos, requerimientos y criterios de aceptación.

### 3.2.1 Alcance diferenciado de Etapa 1 y Etapa 2

La distribución del trabajo responde a cinco principios rectores de ingeniería: primacía del riesgo legal
y operacional, resolución previa de dependencias de interfaces, validación temprana de adopción de terceros,
continuidad operacional sin detención de flota y generación de valor medible desde el primer hito productivo.

En la Tabla 3.1 se detalla la asignación de capacidades entre ambas etapas contractuales.

**Tabla 3.1.** Distribución de capacidades y alcance entre Etapa 1 y Etapa 2

| Capacidad | Etapa 1 (Producción Mes 16) | Etapa 2 (Producción Mes 21) |
|---|---|---|
| Gestión de Despacho | Pre-despacho con validación bloqueante en en 30 segundos o menos s de jornada, habilitaciones y vigencias. | Integración de asignación dinámica multivariable y turnos rotativos complejos. |
| Expediente de Jornada | Expediente multifuente por conductor, sellos de tiempo inalterables y validación de descansos. | Trazabilidad histórica consolidada y predicción de disponibilidad laboral. |
| Control de Flota y Viaje | Vista unificada en torre, detección automática de geocercas en 1.400 clientes y buffer local de 288 h. | Consolidación de telemetría de motor CAN/FMS para flota tractiva compatible. |
| Integración Tributaria | Generación de datos de la orden hacia el ERP contable sin redigitación; contingencia offline. | Auditoría automatizada de cruce fiscal y conciliación tributaria en línea. |
| Costeo y Liquidación | Costeo por viaje dentro de 24 h post-cierre y liquidación automática a transportistas terceros. | Modelos de costeo marginal, rentabilidad de clientes y mantenimiento por condición. |
| Optimización de Flota | Registro de viajes en vacío y análisis de patrones de retorno en rutas troncales. | Algoritmo ALNS de asignación de cargas de retorno para reducción de kilómetros vacíos. |
| Gobernanza y Privacidad | Módulo de consentimientos conforme a Ley N.º 21.719 con revocación en tiempo real. | Portal avanzado de autoservicio para transportistas y clientes corporativos. |
| Sostenibilidad y ESG | Base de datos, factores de emisión y metodología ISO 14083 / GLEC verificable. | Cálculo productivo mensual automatizado de huella de carbono por cliente y contrato. |
| Talleres y Mantenimiento | Registro de mantenciones internas y odometría de flota propia. | Portal web/móvil para registro y homologación de intervenciones en talleres externos. |
|  |

El criterio de corte adelanta deliberadamente el módulo de costeo por viaje a la Etapa 1, difiriendo del orden
original del comité de Curimón. Este ajuste responde a un hecho económico ineludible: dos de los tres contratos
principales servidos actualmente bajo costo se renegocian durante 2027 (Caso, Sección 13.2, p. 27). Postergar el
costeo real hasta el mes 21 obligaría a la compañía a renegociar a ciegas por un nuevo ciclo comercial.

### 3.2.2 Exclusiones explícitas, supuestos y restricciones

El límite del alcance establece con exactitud qué obligaciones asume audIT SpA y cuáles permanecen en la esfera
exclusiva del mandante o de terceros.

**Exclusiones taxativas (Bases Técnicas, Capítulo 11, p. 24):.**
- No se reemplaza el software ERP contable heredado ni se asume la emisión directa de documentos tributarios.
- No se interviene físicamente la computadora de a bordo (ECU) ni se transmiten comandos sobre el bus vehicular CAN.
- No se sustituyen las plataformas GPS preexistentes de los 148 transportistas terceros que cuenten con monitoreo.
- No se administra la contabilidad ni la gestión tributaria interna de los transportistas independientes.
- No se instala equipamiento físico ni infraestructura de comunicaciones en las instalaciones de clientes.

**Supuestos declarados:.**
- El mandante adquiere la totalidad del hardware a bordo (182 equipos principales y 19 de reposición) conforme al Capítulo 11 de las Bases Técnicas y el Formulario T-11.
- El mandante gestiona la suscripción del anexo contractual de adhesión con los 148 transportistas terceros con el apoyo técnico de audIT SpA.
- El sistema contable existente dispone o implementará una interfaz oficial para emitir documentos de transporte en modo de contingencia desconectada.

**Restricciones no negociables:.**
Cumplimiento estricto del descanso de choferes según el Artículo 25 bis del Código del Trabajo, cero distracción al
conducir conforme a la Ley N.º 21.377 (Ley No Chat), protección rigurosa de datos personales según la Ley N.º 21.719
y tolerancia obligatoria a 12 días de incomunicación (288 horas) por cierres estacionales del Paso Los Libertadores.

### 3.2.3 Catálogo priorizado de requerimientos

El catálogo maestro comprende 42 requerimientos normalizados: 28 funcionales (`RF-001` a `RF-028`)
y 14 no funcionales (`RNF-001` a `RNF-014`), trazados de extremo a extremo contra los dolores del
negocio, la arquitectura lógica y los casos de prueba. En la Tabla 3.2 se sintetiza la
distribución por dominio, mientras que el detalle exhaustivo con todos los campos normativos del numeral 17.1 del
Caso se presenta en el Formulario T-12 adjunto.

**Tabla 3.2.** Síntesis del catálogo de 42 requerimientos del proyecto

| Dominio de Solución | Requisitos RF | Requisitos RNF | Total | Alcance Contractual |
|---|---|---|---|---|
| Despacho y Jornada | 7 | 3 | 10 | Etapa 1 (Mes 16) |
| Telemetría y Resiliencia Offline | 6 | 4 | 10 | Etapa 1 (Mes 16) / Etapa 2 |
| Facturación e Integración ERP | 4 | 2 | 6 | Etapa 1 (Mes 16) |
| Costos, Tarifas y Liquidaciones | 4 | 1 | 5 | Etapa 1 (Mes 16) / Etapa 2 |
| Portales y Privacidad de Datos | 4 | 2 | 6 | Etapa 1 (Mes 16) / Etapa 2 |
| Optimización, ESG y Mantenimiento | 3 | 2 | 5 | Etapa 2 (Mes 21) |
| **Total Consolidado** | **28** | **14** | **42** | **Etapa 1: 32 / Etapa 2: 10** |
|  |

### 3.2.4 Criterios formales de aceptación del alcance

El cumplimiento del alcance se evalúa mediante 29 Criterios de Aceptación (CA-01 a CA-29) definidos en el
Capítulo 18 del Caso. La oferta técnica clasifica cada criterio según su naturaleza contractual:
- **Criterios Obligatorios de Cumplimiento Irrestricto:** Cero salidas con infracción legal o de
  seguridad (`CA-01`), jornada acreditable en el 100 % de los despachos (`CA-02`), documento
  tributario conforme previo a la iniciación del movimiento (`CA-14`) y resiliencia offline de al menos
  72 horas sin pérdida de datos (`CA-09`).
- **Metas Comprometidas por audIT SpA:** Reducción de sobreestadías objetadas a al 20 % o menos en
  Etapa 2 (`CA-11`), reducción de kilómetros en vacío a al 18 % o menos (`CA-15`), disponibilidad
  del costo consolidado dentro de las 24 horas del cierre de viaje (`CA-17`), pre-liquidación mensual
  en en un día hábil o menos día hábil con al 2 % o menos de ajustes (`CA-20`), adhesión de transportistas igual o superior al 70 % en
  Etapa 1 y igual o superior al 90 % en Etapa 2 (`CA-27`), y tiempo de revocación de datos en 5 minutos o menos minutos (`CA-23`).
- **Parámetros a Fijar en la Etapa 1:** Periodicidad de descarga física de tacógrafos (`CA-07`),
  precisión geométrica de geocercas en faenas (`CA-10`), y márgenes dinámicos de anticipación para alertas de
  lugar seguro de descanso en ruta (`CA-28`).

## 3.3 Esquema de solución

El esquema de solución propuesto por audIT SpA articula una arquitectura desacoplada basada en microservicios,
nube híbrida y computación de borde (Edge Computing) en cada vehículo.
En la Figura 3.1 se ilustra el modelo conceptual de la solución, estructurado en ocho capas
desacopladas y seis contextos delimitados, conforme al modelo de referencia mandatado en las Bases Técnicas
Transversales FEP02, numeral 2.1, p. 6.

![Figura 3.1. Diagrama conceptual del esquema de solución](../../03-solucion/esquema_conceptual_solucion.png)

*Figura 3.1. Diagrama conceptual del esquema de solución*

Fuente: Elaboración propia.

Como se aprecia en la Figura 3.1, la solución se organiza de abajo hacia arriba en las
siguientes capas operacionales:
- **Capa de Borde Vehicular (On-Premise Móvil):** Dispositivo telemático instalado en cabina con
  almacenamiento no volátil de 8 GB (eMMC), firmware con motor de persistencia local SQLite en modo WAL y
  conexión no invasiva mediante pinzas inductivas al bus CAN/FMS. Garantiza autonomía de hasta 288 horas sin señal.
- **Capa de Ingesta y Mensajería Asíncrona:** Servicios de ingesta masiva en la nube pública
  (Azure Event Hubs) capaces de absorber ráfagas de reconexión tras pérdidas de cobertura en la cordillera,
  garantizando orden temporal e idempotencia en la recepción de telemetría.
- **Capa de Servicios de Negocio y Microservicios (AKS):** Conjunto de seis microservicios aislados
  que ejecutan la lógica esencial: Servicio de Despacho (validación bloqueante sub-30s), Servicio de Control de
  Jornada (expediente unificado), Servicio de Gestión de Flota, Servicio de Viajes y Evidencia, Servicio de
  Costeo y Liquidación, y Servicio de Privacidad y Consentimiento.
- **Capa de Integración y Adaptadores (ACL):** Capa Anticorrupción que aísla el nuevo ecosistema del
  software ERP contable heredado de 2013, transformando eventos asíncronos en peticiones transaccionales seguras.
- **Capa de Persistencia Políglota y Almacenamiento Inmutable:** Base relacional transaccional
  (PostgreSQL HA), motor de series de tiempo para telemetría (TimescaleDB) y repositorio inmutable WORM
  (Azure Blob con políticas de inmutabilidad) para resguardar la evidencia con valor probatorio legal.
- **Capa de Exposición y Seguridad Perimetral:** API Gateway gobernado con autenticación federada,
  control de acceso basado en atributos (ABAC) y cortafuegos de aplicaciones web (WAF).
- **Capa de Presentación y Portales Web/Móviles:** Aplicación web responsiva para la torre de control,
  portal seguro para 148 transportistas, portal de seguimiento controlado para clientes y aplicación móvil para choferes.
- **Capa de Observabilidad Integral:** Pila unificada de métricas, trazas distribuidas y bitácoras
  auditables para asegurar la monitorización continua del rendimiento y los SLA comprometidos.

## 3.4 Explicación de la Solución

La explicación operacional y de negocio detalla el funcionamiento dinámico de la solución a través de sus flujos
principales, demostrando su coherencia con la problemática de Transportes Curimón S.A. y el mapeo exacto con los
componentes de software especificados en el Capítulo 4.
En la Figura 3.2 se presenta el flujo operacional de extremo a extremo que gobierna desde la
creación de la orden de transporte hasta el cierre de la liquidación mensual.

![Figura 3.2. Flujo operacional de extremo a extremo de la solución](../../03-solucion/flujo_operacional_solucion.png)

*Figura 3.2. Flujo operacional de extremo a extremo de la solución*

Fuente: Elaboración propia.

### 3.4.1 Dinámica operacional de las nueve capacidades esenciales

A partir del flujo ilustrado en la Figura 3.2, las nueve capacidades de la solución operan
de manera coordinada para garantizar la seguridad, la legalidad y la eficiencia del negocio:
- **Despacho Seguro con Validación Bloqueante (`RF-001`, `RF-005`, `RF-006`):** Al momento
  en que el despachador asigna un viaje, el microservicio consulta en memoria Redis y base PostgreSQL las habilitaciones
  del chofer, el descanso efectivo previo, la compatibilidad del tractocamión y semirremolque y las 6.000 vigencias vivas.
  Si se detecta cualquier incumplimiento legal o de seguridad, el sistema genera un bloqueo estricto en menos de 2
  segundos, impidiendo la emisión de la orden de carga. Solo una autorización dual documentada puede levantar excepciones
  operacionales no críticas.
- **Expediente de Jornada e Integridad Probatoria (`RF-002`, `RF-003`, `RF-004`):** El sistema
  consolida los registros de jornada de choferes propios y subcontratados. Los datos de conducción y descanso se sellan
  criptográficamente con hash SHA-256 encadenado y se depositan en almacenamiento inmutable WORM, garantizando su
  pleno valor probatorio ante la Dirección del Trabajo y tribunales laborales.
- **Registro Único de Vigencias Saneado (`RF-005`):** Sustituye las cuatro planillas dispersas actuales
  por un repositorio centralizado con alertas preventivas automatizadas a 30, 15 y 5 días antes del vencimiento de licencias,
  revisiones técnicas, seguros obligatorios y pases a faenas mineras.
- **Viaje y Evidencia Operacional (`RF-008`, `RF-010`, `RF-011`, `RF-012`):** Registro automático
  de arribos y partidas en recintos de clientes mediante geocercas poligonales basadas en algoritmos de ray-casting,
  eliminando la manipulación humana. Los tiempos de espera se registran con sello temporal inalterable, generando la prueba
  irrefutable para facturar el 100 % de las sobreestadías legítimas y reducir las objeciones a menos del 20 %. La
  conformidad de entrega (POD) se obtiene en destino mediante firma digital y código OTP transmitido al receptor.
- **Operación Desconectada y Resiliencia en Frontera (`RF-009`, `RNF-002`, `RNF-008`):** El firmware
  embarcado almacena hasta 288 horas de eventos en memoria no volátil local, permitiendo operar sin pérdida de datos en zonas
  sin cobertura celular y absorbiendo cierres de hasta 12 días en el Paso Los Libertadores. Al recuperar señal, la
  sincronización se realiza de forma ordenada, idempotente y sin duplicados.
- **Integración Tributaria sin Fricción (`RF-013`, `RF-014`, `RNF-006`):** La orden de transporte
  aprobada genera la estructura de datos requerida por el software ERP contable de Curimón, el cual actúa como único emisor
  autorizado ante el Servicio de Impuestos Internos. Para salidas en faenas remotas sin señal, se utiliza el mecanismo
  offline certificado del ERP con folios preasignados, bloqueando la salida si el documento no está emitido conforme.
- **Costeo por Viaje y Liquidación Automatizada (`RF-016`, `RF-017`, `RF-019`):** El motor de costos
  calcula el gasto real por kilómetro, tramo y ruta, publicando una versión preliminar en menos de 24 horas tras el cierre
  del viaje y consolidando mensualmente los ajustes de combustible y peajes. La liquidación mensual de los 148 transportistas
  se automatiza sobre evidencia objetiva de viaje, acortando el proceso de 9 días a 24 horas y reduciendo las disputas a menos del 2 %.
- **Portales Web Seguros y Gobernanza de Privacidad (`RF-020`, `RF-021`, `RF-022`, `RNF-013`):**
  Portal de autoservicio para transportistas terceros con visibilidad de sus viajes y pre-liquidaciones en curso. Portal para
  clientes corporativos con seguimiento en tiempo real limitado estrictamente a la ventana horaria del viaje asignado. Módulo
  de privacidad que implementa la Ley N.º 21.719, permitiendo al transportista otorgar o revocar consentimientos telemáticos
  con efecto en menos de 5 minutos.
- **Implantación Gradual y Flota Mixta (`RF-026`, `RF-028`, `RNF-004`, `RNF-011`):**
  Despliegue gradual que respeta el ritmo físico de la flota (montaje en terminal en un tiempo inferior a 45 minutos).
  La torre de control opera en modo mixto, identificando con claridad visual el nivel de evidencia disponible (telemática
  completa, homologada o documental reforzada), sin degradar nunca las reglas de bloqueo legal.

### 3.4.2 Estrategia de adopción y enrolamiento de los 148 transportistas

La viabilidad práctica de la solución radica en su plan de adhesión para los 148 empresarios subcontratados. En lugar de
imponer exigencias unilaterales, audIT SpA propone un modelo contractual de comodato e incentivos verificables:
- **Régimen de Propiedad y Comodato:** El equipamiento a bordo es adquirido en su totalidad por Curimón
  FEP01, Artículo 11, p. 24 y se entrega en comodato gratuito al transportista mientras mantenga contrato activo. audIT SpA asume la
  instalación, configuración, mantenimiento y retiro en terminal, sin costo patrimonial para el dueño del camión.
- **Soberanía y Protección del Dato Privado:** El dispositivo telemático solo captura y transmite datos cuando
  existe una orden de viaje activa asignada por Curimón. Fuera de esa ventana operacional, la captura cesa o se anonimiza,
  resguardando la privacidad del chofer y la confidencialidad de los viajes que el transportista ejecute para terceros.
- **Incentivos Económicos:** El transportista consulta su pre-liquidación en tiempo real en el
  portal web, eliminando la incertidumbre de fin de mes; participa en la recaudación efectiva de las sobreestadías demostradas
  por su propia telemetría; y dispone de un expediente electrónico portable con su historial de cumplimiento técnico.
- **Modalidades de Adhesión Flexibles:** Se definen tres niveles: *Adhesión Completa* (comodato de hardware
  y telemetría integral), *Adhesión de Datos* (integración API de su GPS preexistente sin intervenir el vehículo) y
  *Modo Transición* (validación documental reforzada mientras se completa el enrolamiento).

Esta estrategia asegura alcanzar contractualmente las metas de adhesión del 70 % al cierre de la Etapa 1 (Mes 16) y del
90 % al cierre de la Etapa 2 (Mes 21), garantizando la viabilidad social y técnica de la modernización de Transportes Curimón S.A.

## Referencias

Transportes Curimón S.A. (2026). *Bases administrativas para la preparación de la propuesta: Licitación Pública Internacional N.º TFEP-01/2026* (Documento FEP01).

Transportes Curimón S.A. (2026). *Bases técnicas del Caso 10, Transporte de Carga: Licitación Pública Internacional N.º TFEP-01/2026* (Documento FEP03).

Transportes Curimón S.A. (2026). *Bases técnicas transversales para la preparación de la propuesta: Licitación Pública Internacional N.º TFEP-01/2026* (Documento FEP02).

Transportes Curimón S.A. (2026). *Comunicado 10: Estructura obligatoria de las propuestas preparatorias y técnica final* (Comunicado de la licitación TFEP-01/2026).

## Declaración de uso de IA

Conforme al Comunicado 10, sección 7.2, cada sección de este subdocumento y cada formulario asociado declara la herramienta de inteligencia artificial generativa usada, su finalidad, el nivel de uso en texto y en diagramas según la escala oficial de esa sección, y quién revisó y qué verificó. Esta declaración se consolida en el Formulario A-6.

| Sección | Herramienta | Finalidad del uso | Nivel en texto | Nivel en diagramas | Revisión humana (quién y qué verificó) |
|---|---|---|---|---|---|
| Introducción | Claude Opus 5.5 en Claude Code | Redacción introductoria y síntesis de articulación técnica | Bajo | Ninguno | Carlos Jesús Abarza Suazo, Director de Auditoría y Aseguramiento Tecnológico: Verificación de coherencia con pliego de licitación |
| 3.1 | Claude Opus 5.5 en Claude Code | Síntesis del ciclo de vida, etapas contractuales y modelo operacional | Medio | Ninguno | Carlos Jesús Abarza Suazo, Director de Auditoría y Aseguramiento Tecnológico: Verificación de plazos Art. 17 y 36 meses de operación |
| 3.2 | Claude Opus 5.5 en Claude Code | Estructuración del alcance, corte E1/E2, catálogo de 42 requerimientos y criterios de aceptación | Medio | Ninguno | Carlos Jesús Abarza Suazo, Director de Auditoría y Aseguramiento Tecnológico: Auditoría de 42 requerimientos y coherencia con FEP01/FEP03 |
| 3.3 | Claude Opus 5.5 en Claude Code y conector visual | Estructuración de diagramas conceptuales y descripción analítica de capas | Medio | Bajo | Carlos Jesús Abarza Suazo, Director de Auditoría y Aseguramiento Tecnológico: Validación de mapeo unívoco con arquitectura de S4 |
| 3.4 | Claude Opus 5.5 en Claude Code | Articulación operacional de las 9 capacidades y estrategia de adopción de transportistas | Medio | Ninguno | Carlos Jesús Abarza Suazo, Director de Auditoría y Aseguramiento Tecnológico: Verificación de Ley 21.719 y reglas de comodato |
| Formulario T-12 | Claude Opus 5.5 en Claude Code y Codex | Reescritura del catálogo de 42 requerimientos y conciliación de RF-028 y RN-03 con las modalidades y evidencia de jornada definidas en S3 | Alto | Ninguno | Conciliación y controles documentales automatizados realizados; revisión humana final pendiente. |
