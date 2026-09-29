# Subdocumento 6: Metodologías de Gestión y Desarrollo
**Licitación Pública TFEP-01/2026 — Solución Integral de Transporte de Carga Terrestre**  
**Cliente:** Transportes Curimón S.A.  
**Proponente:** audIT Soluciones Tecnológicas SpA  
**Ponderación Técnica Informe 2:** 8 % (FEP01 p. 66)  
**Formularios Asociados:** Formulario T-9 y Formulario T-10 (FEP01 p. 61)  
**Dupla Responsable:** D3 (Arquitectura DevSecOps, Ingeniería de Software y Plataforma de Datos)

---

## 1. Resumen de Apertura e Inserción Metodológica

El presente subdocumento formaliza el marco metodológico integrado de audIT para la dirección, construcción, aseguramiento y despliegue del sistema de gestión operacional y logística de Transportes Curimón S.A. Se establece un modelo de gestión híbrido que conjuga la previsibilidad y rigor de control del estándar PMBOK con la flexibilidad iterativa de Scrum y la eficiencia operativa de Kanban, asegurando el cumplimiento estricto del cronograma de 56 meses y los 42 requerimientos normalizados en el Formulario T-12. Asimismo, se institucionaliza una práctica de ingeniería DevSecOps unificada en GitLab CI Enterprise con certificación de procedencia SLSA Nivel 3 y puertas de calidad automáticas.

### Entregables Recibidos por el Mandante
* **Estructura formal de gobernanza** organizada en cinco comités mandantes con cadencias quincenales y mensuales (FEP01, Artículo 71°, p. 37).
* **Procedimiento formal de control de cambios** con análisis de impacto multidimensional y tope contractual del 20 % (FEP01, Artículo 72°, p. 38).
* **Pipeline integral DevSecOps automatizado** con análisis estático (SAST), escaneo de contenedores (Trivy), validación IaC y pruebas dinámicas (DAST).
* **Cadena de suministro de software protegida** mediante firmas criptográficas Cosign y atestaciones SBOM CycloneDX (FEP01, Artículo 4.3, p. 5).
* **Matrices estandarizadas de criterios de salida** para Definición de Preparado (DoR) y Definición de Terminado (DoD).

La naturaleza multidimensional de la licitación TFEP-01/2026 exige articular actividades de distinta naturaleza: adquisiciones masivas de equipamiento de telemetría vehicular, obras civiles menores en terminales, configuraciones de infraestructura cloud de misión crítica, e ingeniería de software para componentes transaccionales, móviles y analíticos. Un enfoque metodológico homogéneo resultaría insuficiente. Por ello, la estrategia metodológica de audIT se articula como el núcleo operativo que conecta los requerimientos del Formulario T-12 con el Plan de Trabajo del Capítulo 7, el Plan de Riesgos del Capítulo 8 y el Sistema de Calidad del Capítulo 9.

---

## 2. Sección 6.1: Metodología de Gestión del Proyecto

La gestión del proyecto adopta las directrices de la guía PMBOK (PMI, 7.ª edición), adaptada específicamente a las restricciones operativas y contractuales del transporte de carga por carretera y la logística interurbana (FEP01, Artículo 4.3, p. 5; FEP02, RT-19.01, p. 33). Este marco garantiza trazabilidad absoluta sobre la línea base de alcance, tiempo y costo, articulando la relación contractual con Transportes Curimón S.A. mediante canales formales de rendición de cuentas.

### 6.1.1 Marco Híbrido de Gestión: PMBOK y Enfoques Ágiles

La administración del contrato se fundamenta en un modelo de ciclo de vida híbrido, el cual combina procesos predictivos para los compromisos contractuales vinculantes con ciclos adaptativos para la construcción de los módulos de software:

* **Capa Predictiva (PMBOK 7):** Aplica a la gestión de la Ruta Crítica contractual del Artículo 17°, la entrega de hitos del Formulario E-25, la logística de abastecimiento e instalación física del hardware vehicular en el parque de 374 camiones (148 tractos propios, 34 terceros sin GPS equipados por audIT con pinzas CANclick inductivas, y 192 terceros homologados por API), las adecuaciones de salas técnicas y la obtención de recepciones provisorias y definitivas.
* **Capa Adaptativa (Scrum):** Aplica al diseño y programación de los módulos aplicativos (torre de control, despacho, portal de transportistas, aplicación de conductores y analítica). Se estructura en iteraciones cortas (sprints de 2 semanas) con entregables potencialmente desplegables, lo que permite retroalimentación temprana de las contrapartes operativas de Curimón sin comprometer los plazos mayores de entrega.
* **Capa de Flujo Continuo (Kanban):** Aplica a la atención de incidencias en etapa de marcha blanca (60 días para Etapa 1 y 60 días para Etapa 2, FEP01, Artículo 17.3, p. 12), gestión de parches de seguridad y solicitudes de servicio menores durante los 36 meses de operación continuada.

> **Decisión Técnica D-01: Adopción de marco de gestión híbrido predictivo-ágil**  
> * **Decisión:** Implementar gobernanza predictiva PMBOK para control contractual e hitos combinada con Scrum en iteraciones de dos semanas para software.  
> * **Alternativa descartada:** Enfoque puramente predictivo tipo cascada y enfoque puramente ágil sin línea base.  
> * **Criterio:** El transporte crítico exige certidumbre contractual de plazos de implantación junto con flexibilidad en diseño de interfaces y analítica.  
> * **Fuente:** FEP01, Artículo 4.3, p. 5; FEP02, RT-19.01, p. 33.

### 6.1.2 Gobernanza de Interesados y Plan de Comunicaciones

La gestión eficaz de los grupos de interés resulta determinante debido a la dispersión geográfica de las faenas y la multiplicidad de actores involucrados en la cadena logística:

1. **Patrocinador Ejecutivo y Dirección de Transporte Curimón:** Enfocados en retorno de inversión, continuidad operacional del negocio y cumplimiento de contratos de flete minero, vitivinícola y retail.
2. **Supervisores de Tráfico y Operadores de Torre de Control:** Usuarios intensivos de la plataforma, orientados a la visibilidad en tiempo real, alertas de desvío y cumplimiento de itinerarios.
3. **Conductores de Flota Propia y Terceros:** 454 conductores que interactúan directamente con la aplicación móvil y los sensores de cabina, priorizando la ergonomía, simplicidad y registro certero de jornadas laborales conforme al Artículo 25 bis del Código del Trabajo.
4. **Transportistas Terceros y Dueños de Camiones:** Propietarios de los 226 camiones subcontratados, interesados en la liquidación expedita de servicios y visibilidad telemática homologada.
5. **Organismos Fiscalizadores (Dirección del Trabajo, MTT, SEC):** Entidades que auditan la legalidad del transporte, pesos por eje, transporte de sustancias peligrosas y registros de jornada.

Conforme a la exigencia técnica de las bases (FEP02, RT-19.05, p. 33), audIT implementará desde el primer mes del contrato un **Espacio Colaborativo Digital** unificado en la nube de acceso seguro 24/7 para el equipo del proyecto y la contraparte técnica de Curimón. Este repositorio centralizado alojará la documentación formal, especificaciones de diseño, minutas firmadas, registro vivo de riesgos conforme a la norma ISO 31000 (FEP02, RT-19.04, p. 33) y el catálogo de solicitudes de cambio.

### 6.1.3 Gestión de Adquisiciones e Integración Contractual

La gestión de adquisiciones se estructura para mitigar riesgos de desabastecimiento en la cadena de suministros tecnológicos que pudieran afectar la Ruta Crítica:

* **Adquisición Temprana de Componentes Vehiculares:** Compra y resguardo inicial de los 148 computadores de a bordo industriales, 34 interfaces inductivas CANclick para terceros y antenas satelitales auxiliares durante los meses 1 y 2 de la Etapa 1, neutralizando fluctuaciones de comercio exterior y plazos de internación aduanera.
* **Acuerdos de Nivel de Servicio con Nube Pública:** Contratación bajo régimen Enterprise Agreement con Microsoft Azure para la provisión garantizada de capacidad de cómputo en la región principal Chile Central y zona secundaria Brazil South, asegurando el SLA contractual de 99,5 % (FEP01, Artículo 78°, p. 40).
* **Conectividad Celular Multicarrier:** Contratos de conectividad telemática con SIM card industriales en modalidad APN privada sobre redes de telecomunicaciones de cobertura nacional, con conmutación automática entre operadores para minimizar zonas de silencio.

### 6.1.4 Comités de Gobernanza, Cadencias y Mecanismos de Decisión

El control directivo y operacional del contrato se estructura en estricto apego al marco de gobernanza mandatado por las bases de licitación (FEP01, Artículo 71°, p. 37). La interacción formal entre audIT y Transportes Curimón S.A. se canaliza a través de cinco instancias formales:

| Instancia | Frecuencia | Participantes Obligatorios | Propósito y Alcance Decisional |
| :--- | :--- | :--- | :--- |
| **Comité Ejecutivo** | Mensual | Patrocinador de Curimón, Gerencia de audIT, Administrador del Contrato. | Dirección estratégica, resolución de bloqueos contractuales, aprobación de modificaciones de alcance y evaluación de riesgos mayores. |
| **Comité de Proyecto** | Quincenal | Contraparte Técnica de Curimón, Jefe de Proyecto de audIT. | Seguimiento riguroso de la Carta Gantt, estado de paquetes de trabajo EDT, control de hitos y acuerdos de ejecución técnica. |
| **Comité de Arquitectura** | Mensual | Arquitecto de Solución, Oficial de Ciberseguridad, referentes de TI de Curimón. | Aprobación formal de decisiones técnicas (ADR), control de deuda técnica, revisión de estándares de interoperabilidad y seguridad. |
| **Comité de Operación** | Mensual (desde M13) | Líder de Operación, Jefatura de Mesa de Ayuda, Contraparte Técnica de Curimón. | Verificación del cumplimiento de acuerdos SLA, gestión de problemas recurrentes, indicadores de marcha blanca y mejora continua. |
| **Reunión de Seguimiento** | Semanal | Equipos de ingeniería y especialistas de ambas partes. | Coordinación táctica operativa, revisión de impedimentos inmediatos y compromisos semanales de avance. |

```mermaid
flowchart LR
    sem["Reunión Semanal\n(Impedimentos)"] -->|Escalamiento| proy["Comité de Proyecto\n(Desviaciones <= 5d)"]
    proy -->|Impacto contractual| ejec["Comité Ejecutivo\n(Cambios y SLA)"]
    proy -->|Consulta técnica| arq["Comité de Arquitectura\n(Decisiones ADR)"]
    arq --> ejec
    ejec -->|Sin acuerdo 30d| res["Resolución Controversias\n(CAM Santiago, Art. 87)"]
```

#### Procedimiento Formal de Control de Cambios (Artículo 72°)
Toda modificación o requerimiento emergente debe tramitarse obligatoriamente mediante el procedimiento de control de cambios regido por el Artículo 72° de las Bases Administrativas:

| Paso | Acción Requerida | Responsable Formal | Criterio y Resultado Verificable |
| :--- | :--- | :--- | :--- |
| **1. Registro** | Solicitud Formal de Cambio (RFC) en espacio colaborativo. | Parte solicitante (Curimón o audIT). | Formulario normalizado con descripción técnica, justificación operativa y urgencia asignada. |
| **2. Análisis** | Evaluación técnica y multidimensional de impactos. | Jefe de Proyecto y Arquitecto de Solución. | Informe de impacto en alcance, cronograma de Ruta Crítica, matriz de riesgos y disponibilidad. |
| **3. Revisión** | Dictamen técnico del Comité de Arquitectura. | Contraparte Técnica y Líder Técnico de audIT. | Validación de viabilidad arquitectónica, compatibilidad con microservicios y seguridad. |
| **4. Decisión** | Aprobación o rechazo formal en acta. | Comité Ejecutivo (unanimidad de representantes). | Aprobación expresa previa a cualquier ejecución física o lógica. Límite acumulado del 20 %. |
| **5. Ejecución** | Actualización de línea base y despliegue controlado. | Equipos de ingeniería y PMO. | Incorporación a sprint de desarrollo o ventana de mantenimiento programada. |

> **Compromiso C-01:** audIT formalizará las decisiones y acuerdos de cada sesión de comité en un plazo máximo de veinticuatro horas hábiles en el espacio colaborativo digital.  
> * **Métrica:** Emisión de minuta formal y registro en espacio digital en menos de 24 horas hábiles tras cada sesión de comité.  
> * **Verificación:** Registro de auditoría del repositorio colaborativo.  
> * **Fuente:** FEP01, Artículo 71°, p. 37; FEP02, RT-19.05, p. 33.

---

## 3. Sección 6.2: Metodología de Desarrollo Software

El desarrollo de la solución tecnológica se estructura bajo un ciclo de vida evolutivo basado en ingeniería de software guiada por el dominio (Domain-Driven Design, DDD) y prácticas DevSecOps. Se garantiza la prevención sistemática de deuda técnica y un tiempo de salida al mercado optimizado para los frentes operativos del transporte.

### 6.2.1 Ciclo de Vida Adaptado y Evolución Arquitectónica

Para conciliar la alta disponibilidad exigida con la continua evolución logística de Transportes Curimón, el desarrollo de software se organiza en torno a los límites de contexto definidos en el Subdocumento 4.1:

* **Gestión Evolutiva de Requerimientos:** Cada uno de los 42 requerimientos del Formulario T-12 se desglosa en Historias de Usuario documentadas en el repositorio colaborativo. Cada historia incluye criterios de aceptación redactados en formato estructurado (Gherkin: Dado, Cuando, Entonces), sirviendo de especificación viva ejecutable.
* **Diseño de Interfaces API-First:** Todo intercambio de datos entre módulos internos y con sistemas legados del cliente se realiza mediante contratos formales: especificación OpenAPI 3.1 para servicios síncronos REST y especificación AsyncAPI 2.6 para eventos telemáticos sobre Apache Kafka (FEP01, Artículo 4.3, p. 5).
* **Prevención y Mitigación de Deuda Técnica:** Cada sprint de construcción reserva un 15 % de la capacidad de desarrollo para refactorización, optimización de consultas en base de datos y actualización de librerías base. Se prohíbe la acumulación de advertencias de compilación y se somete el código a inspección estática continua.

### 6.2.2 Ecosistema DevSecOps Unificado en GitLab CI Enterprise

audIT descarta configuraciones fragmentadas o herramientas dispersas, adoptando como estándar corporativo exclusivo la plataforma **GitLab CI Enterprise** para la orquestación íntegra del ciclo DevSecOps (FEP01, Artículo 4.3, p. 5).

> **Decisión Técnica D-02: Ecosistema integral DevSecOps sobre GitLab CI Enterprise**  
> * **Decisión:** Unificar todo el control de versiones, pipeline de CI/CD, escaneo SAST, gestión de artefactos y políticas de despliegue en GitLab CI Enterprise.  
> * **Alternativa descartada:** Arquitecturas mixtas compuestas por herramientas independientes (Jenkins, SonarQube standalone sin integración nativa, scripts de despliegue aislados).  
> * **Criterio:** Reducir vectores de falla, garantizar trazabilidad auditable de la cadena de suministro de software y automatizar la aplicación de políticas SLSA Nivel 3.  
> * **Fuente:** FEP01, Artículo 4.3, p. 5.

```mermaid
flowchart LR
    f1["1. Build & Unit\n(PyTest / Jest >=80%)"] --> f2["2. SAST & Secrets\n(SonarQube Quality Gate)"]
    f2 --> f3["3. Container Scan\n(Trivy 0 CVEs)"]
    f3 --> f4["4. Supply Chain\n(SLSA 3, SBOM, Cosign)"]
    f4 --> f5["5. IaC Deploy\n(Terraform en AKS)"]
    f5 --> f6["6. DAST\n(OWASP ZAP Staging)"]
```

| Fase del Pipeline | Herramienta Ejecutora | Métrica Evaluada | Umbral Bloqueante de Paso a Producción |
| :--- | :--- | :--- | :--- |
| **1. Pruebas** | GitLab Runner / PyTest | Cobertura de código | $\ge 80\,\%$ de cobertura de ramas (branch coverage). Cero pruebas unitarias fallidas. |
| **2. Análisis estático** | SonarQube Enterprise | Calidad y seguridad | Quality Gate «A» en mantenibilidad, deuda técnica $<5\,\%$, cero vulnerabilidades críticas o altas. |
| **3. Contenedores** | Trivy Container Scanner | Vulnerabilidades CVE | Cero vulnerabilidades críticas o altas en dependencias y capas base (imágenes Distroless / Alpine). |
| **4. Cadena de valor** | Cosign / Syft (Anchore) | Integridad de artefactos | Generación mandatoria de SBOM en formato CycloneDX. Firma criptográfica con clave corporativa HSM (SLSA Nivel 3). |
| **5. Infraestructura** | HashiCorp Terraform | Drift y seguridad IaC | Ejecución de `tfsec` y `checkov`. Cero configuraciones inseguras en templates de Azure. |
| **6. Análisis dinámico** | OWASP ZAP | Vulnerabilidades web | Cobertura OWASP ASVS 4.0 Nivel 2 (Art. 4.3). Cero hallazgos en Top 10 web y API. |

### 6.2.3 Infraestructura como Código y Gestión de Configuración

Toda la infraestructura cloud alojada en Microsoft Azure se gestiona bajo el paradigma de Infraestructura como Código (IaC) mediante scripts de Terraform versionados en Git (FEP02, RT-10.02, p. 24):

* **Segregación de Ambientes:** Suscripciones independientes de Azure para Desarrollo, Pruebas/Staging y Producción, impidiendo cualquier cruce accidental de accesos o datos operacionales.
* **Aprovisionamiento Inmutable:** Los servidores y clusters de Azure Kubernetes Service (AKS) no admiten modificaciones manuales en caliente vía consola. Cualquier cambio de configuración o escalamiento debe registrarse como código, someterse a revisión por pares y desplegarse mediante pipeline.
* **Gestión Centralizada de Secretos:** Ninguna credencial, clave privada o cadena de conexión se almacena en el código fuente. Se utiliza Azure Key Vault integrado con identidades administradas (Managed Identities) y rotación programada automática.

### 6.2.4 Ceremonias Técnicas, Artefactos y Criterios de Salida

El trabajo colaborativo del equipo de desarrollo se organiza en torno a un flujo de trabajo de control de versiones GitFlow adaptado:

* **Rama `main`:** Refleja exclusivamente el código en producción verificado. Es una rama protegida que requiere firma criptográfica de commits y aprobación de dos líderes técnicos.
* **Rama `develop`:** Rama de integración continua donde convergen las nuevas funcionalidades validadas mediante pruebas unitarias.
* **Ramas temáticas (`feature/*`, `bugfix/*`, `hotfix/*`):** Ramas de trabajo de corta duración, sujetas obligatoriamente a revisión por pares (Peer Review) mediante Merge Requests.

| Nivel de Control | Artefacto / Fase Evaluada | Criterios de Aceptación Obligatorios |
| :--- | :--- | :--- |
| **Definición de Preparado (DoR)** | Historia de Usuario / Requerimiento funcional | Requerimiento trazado unívocamente al Formulario T-12. Criterios de aceptación definidos en Gherkin. Dependencias técnicas resueltas. Mockups de interfaz aprobados. |
| **Revisión por Pares** | Merge Request (MR) en GitLab | Aprobación obligatoria de al menos un revisor senior. Verificación de adherencia a guías de estilo, comentarios arquitectónicos y ausencia de duplicidad de código. |
| **Definición de Terminado (DoD)** | Incremento de Software / Release Candidate | Código fusionado en rama objetivo. Cobertura $\ge 80\,\%$. Quality Gate SonarQube superado. Contenedor firmado con Cosign y registrado en Azure Container Registry con SBOM. Documentación OpenAPI actualizada. Despliegue exitoso en staging sin regresiones operativas. |

> **Compromiso C-02:** audIT mantendrá un tiempo de despliegue continuo en ambiente de pruebas inferior a quince minutos para incrementos de software validados.  
> * **Métrica:** Despliegue automatizado en staging en menos de 15 minutos tras aprobación de Merge Request.  
> * **Verificación:** Métricas de ejecución del pipeline en GitLab CI Enterprise.  
> * **Fuente:** FEP01, Artículo 4.3, p. 5; FEP02, RT-10.02, p. 24.

---

## 4. Anexos Oficiales del Subdocumento 6

### Formulario T-9: Metodología para la Administración y Gestión del Proyecto
*(FEP01 p. 61 · Formulario T-7 letra a)*

| Contenido Exigido por las Bases | Dónde se Presenta en la Oferta Técnica |
| :--- | :--- |
| **Metodología de gestión del proyecto:** aplicación del PMBOK adaptada a la complejidad del proyecto, integrando enfoques ágiles donde corresponda. | Sección 6.1.1 (Marco híbrido de gestión: PMBOK y enfoques ágiles) |
| **Gestión de interesados, comunicaciones, adquisiciones e integración contractual.** | Sección 6.1.2 (Gobernanza de interesados y plan de comunicaciones) y Sección 6.1.3 (Gestión de adquisiciones e integración contractual) |
| **Ceremonias, artefactos, cadencias y mecanismos formales de decisión.** | Sección 6.1.4 (Comités de gobernanza, cadencias y mecanismos de decisión) |

### Formulario T-10: Metodología para el Desarrollo
*(FEP01 p. 61 · Formulario T-7 letra b)*

| Contenido Exigido por las Bases | Dónde se Presenta en la Oferta Técnica |
| :--- | :--- |
| **Metodología de desarrollo coherente con la naturaleza del proyecto,** con sus implicancias en gestión de requerimientos, arquitectura evolutiva, refactorización, deuda técnica y tiempo de salida al mercado. | Sección 6.2.1 (Ciclo de vida adaptado y evolución arquitectónica) |
| **Prácticas de DevSecOps, integración y entrega continuas,** infraestructura como código y automatización de pruebas en pipeline. | Sección 6.2.2 (Ecosistema DevSecOps unificado en GitLab CI Enterprise) y Sección 6.2.3 (Infraestructura como código y gestión de configuración) |
| **Ceremonias técnicas, artefactos de ingeniería y criterios de aceptación (DoR y DoD).** | Sección 6.2.4 (Ceremonias técnicas, artefactos y criterios de salida) |
