# SUBDOCUMENTO 1 — PRESENTACIÓN DE LA EMPRESA AUDIT

## 1.1 Información Institucional, Trayectoria y Líneas de Negocio (RT-23.01)

**audIT** es una empresa de ingeniería de software, arquitectura de datos y ciberseguridad industrial fundada en 2022 (4 años de trayectoria comprobable en el mercado nacional), orientada exclusivamente a resolver la continuidad operacional, la visibilidad telemática y la trazabilidad analítica en organizaciones con operaciones geográficamente distribuidas y condiciones de conectividad intermitente. Su propuesta de valor se concentra en un segmento donde la mayoría de los proveedores generalistas falla: integrar dispositivos físicos desplegados en campo —sensores, equipos embarcados, telemetría vehicular— con plataformas de datos que deben operar de forma confiable incluso sin conexión permanente.

- **Giro Principal:** Servicios integrales de consultoría informática, diseño e implantación de plataformas de datos en la nube, arquitectura de software híbrida, desarrollo de soluciones IoT / telemetría de terreno y auditoría de ciberseguridad bajo estándares internacionales.
- **Misión:** Diseñar e implantar soluciones de software e integración ciber-física de alta confiabilidad que transformen operaciones críticas de campo en flujos de datos auditables, continuos y seguros, habilitando la toma de decisiones basada en evidencia técnica rigurosa.
- **Visión:** Consolidarse como el socio tecnológico de referencia en el Cono Sur para la modernización de sistemas de misión crítica y la integración de cadenas logísticas y de transporte bajo arquitecturas resilientes *offline-first*.
- **Valores Corporativos:** Rigor metodológico, seguridad por diseño (*Zero Trust*), transparencia auditable y compromiso irrestricto con la continuidad de servicio de nuestros mandantes.
- **Presencia Geográfica e Instalaciones:** Casa matriz y centro de ingeniería de software ubicado en Viña del Mar (Región de Valparaíso), y oficina de operaciones técnicas, pruebas de banco y laboratorio de dispositivos IoT/embarcados en Santiago (Región Metropolitana), lo que asegura una capacidad de despliegue y soporte presencial expedito sobre el eje logístico central Valparaíso – Santiago – San Bernardo – Los Andes.

Las capacidades instaladas de la compañía se estructuran en tres líneas de negocio de alta especialización:

1. **Ingeniería IoT y Sistemas de Terreno (Edge Computing):** Desarrollo de firmware, integración de telemetría vehicular (CAN bus / FMS / tacógrafo digital) y arquitectura de dispositivos embarcados con tolerancia a desconexión prolongada.
2. **Plataformas de Datos y Analítica Avanzada:** Modelamiento e implantación de repositorios operacionales y analíticos en nube híbrida, ingestión masiva de eventos telemáticos en tiempo real y desarrollo de motores de despacho y optimización.
3. **Consultoría en Arquitectura Híbrida y Ciberseguridad Operacional:** Diseño de capas anticorrupción para convivencia con sistemas heredados (*legacy*), auditorías de seguridad perimetral y gobierno de datos personales bajo la Ley N.° 21.719.

---

## 1.2 Estructura Organizacional, Equipo Directivo y Certificaciones (RT-23.03)

audIT cuenta con una dotación permanente de **22 profesionales de planta** (ingenieros civiles informáticos, ingenieros de software, especialistas en redes y científicos de datos), complementada según demanda por una red certificada de técnicos de instalación en terreno. La organización se estructura en cinco áreas funcionales bajo un modelo de gestión matricial:

```
                          ┌───────────────────────┐
                          │    GERENCIA GENERAL   │
                          └───────────┬───────────┘
                                      │
            ┌─────────────────────────┼─────────────────────────┐
            │                         │                         │
┌───────────┴───────────┐ ┌───────────┴───────────┐ ┌───────────┴───────────┐
│     ARQUITECTURA E    │ │     INGENIERÍA IoT    │ │  OFICINA DE GESTIÓN   │
│   INGENIERÍA DE DATOS │ │   Y EDGE COMPUTING    │ │   DE PROYECTOS (PMO)  │
└───────────────────────┘ └───────────────────────┘ └───────────────────────┘
            │                                                   │
            └─────────────────────────┬─────────────────────────┘
                                      │
                          ┌───────────┴───────────┐
                          │  CALIDAD Y SEGURIDAD  │
                          │   DE LA INFORMACIÓN   │
                          └───────────────────────┘
```

El liderazgo técnico y corporativo de audIT reside en un **Comité Directivo de 8 especialistas senior**, cuya experiencia conjunta abarca las cuatro competencias críticas del presente caso: telemetría vehicular, operación desconectada en terreno, arquitectura de datos escalable y gobernanza de seguridad. La dotación de 22 profesionales se organiza operacionalmente en **4 duplas de ingeniería** especializadas que trabajan de forma pareada para maximizar la cobertura técnica y eliminar silos de conocimiento individual.

Los perfiles directivos clave son:

- **Gerencia General / Dirección de Proyectos:** Ingeniero Civil Informático, PMP® (*Project Management Professional*), con más de 12 años liderando contratos de modernización tecnológica en transporte e infraestructura crítica.
- **Dirección de Arquitectura y Datos:** Máster en Ciencias de la Computación, certificado *Microsoft Certified: Azure Solutions Architect Expert* y *CDMP (Certified Data Management Professional)*.
- **Jefatura de Ingeniería IoT y Terreno:** Ingeniero en Electrónica y Telecomunicaciones, especialista en integración telemática embarcada bajo estándares SAE J1939 y rFMS.
- **Dirección de Calidad y Ciberseguridad:** Ingeniero Civil en Computación, certificado *CISM® (Certified Information Security Manager)* y Auditor Líder ISO 27001 / ISO 9001.

**Certificaciones Institucionales y Alianzas Tecnológicas Vigentes (RT-23.01, RT-23.04):**

- **ISO 9001:2015 (Sistema de Gestión de la Calidad):** Certificación institucional vigente para el diseño, desarrollo, implantación y soporte de soluciones de software e integración de hardware de terreno.
- **ISO 27001:2022 (Sistema de Gestión de Seguridad de la Información):** Alcance certificado sobre el tratamiento, almacenamiento y transmisión de datos de telemetría, información sensible de clientes y trazabilidad contractual.
- **Alianzas Estratégicas:** *Cloud Solution Provider (CSP) Partner* de **Microsoft Azure** con especialización avanzada en infraestructura híbrida (*Azure Arc*, *Azure IoT Hub* y bases de datos distribuidas) y convenios de homologación e integración directa con fabricantes de hardware telemático industrial de estándar automotriz.

---

## 1.3 Capacidades Técnicas, Stack Tecnológico y Metodologías de Trabajo (RT-23.04)

audIT domina un ecosistema tecnológico moderno, robusto y probado en escenarios de alta exigencia operacional:

- **Nivel Embarcado y Terreno:** C/C++, Rust y Python embebido sobre sistemas Linux industrial (*Yocto/Debian Embedded*); almacenamiento local indexado mediante bases de datos transaccionales ultraligeras (*SQLite WAL mode*) con almacenamiento en búfer circular inalterable.
- **Nivel de Integración y Servicios:** Arquitecturas basadas en microservicios desacoplados vía *APIs RESTful* seguras (*OpenAPI 3.0*), *brokers* de mensajería orientados a eventos (*Apache Kafka / Azure Event Hubs*) y capas anticorrupción (*Domain-Driven Design*) para aislar componentes legados.
- **Nivel de Nube y Datos:** Contenerización con *Docker / Kubernetes*, bases de datos híbridas relacionales y temporales (*PostgreSQL / TimescaleDB*), y tableros analíticos en tiempo real (*Power BI Embedded* y servicios analíticos dedicados).

**Metodologías de Trabajo Certificadas:**

- *Desarrollo de Software y Analítica:* Enfoque ágil **Scrum / Kanban** con integración y despliegue continuo (**CI/CD**), asegurando entregas funcionales iterativas validadas por el usuario.
- *Componentes Críticos e Integración de Hardware:* Metodología ingenieril en cascada adaptada (**Modelo V** conforme a ISO/IEC 12207) para el aseguramiento de firmware, homologación vehicular y compatibilidad eléctrica en cabina.

---

## 1.4 Modelo de Gobierno Interno de Calidad, Seguridad y Gestión del Conocimiento

El gobierno interno de audIT se ejecuta a través del área transversal de Calidad y Seguridad de la Información, y se sostiene en tres pilares operativos:

1. **Aseguramiento de Calidad (ISO 9001):** Cada fase de desarrollo cuenta con hitos de compuerta (*quality gates*). Ningún entregable pasa a producción sin la aprobación formal del Responsable de Calidad (rol independiente de los líderes de desarrollo), quien audita el cumplimiento de matrices de trazabilidad de requisitos, cobertura de pruebas unitarias y de integración ($\ge 85\%$) y actas formales de homologación en terreno.

2. **Seguridad y Privacidad por Diseño (ISO 27001 y Ley N.° 21.719):** Aplicación de arquitectura *Zero Trust*. La información telemática y transaccional se cifra de extremo a extremo: AES-256 en reposo y TLS 1.3 en tránsito. Se implementa control de acceso basado en roles (RBAC) y mínimo privilegio. Todo dato personal o sensible de conductores —especialmente de transportistas subcontratados, conforme a RT-11.10 y RT-16.09— cuenta con trazabilidad estricta y separación criptográfica, garantizando la plena oponibilidad jurídica y el cumplimiento de la normativa nacional de protección de datos personales.

3. **Gestión del Conocimiento y Mitigación de Dependencia:** audIT mantiene una base de conocimiento institucional automatizada (arquitecturas de referencia, patrones de integración de buses vehiculares, guías de resolución de fallas y *post-mortems* de incidentes). La estandarización de artefactos y el trabajo en parejas de ingeniería —organizadas en 4 duplas especializadas— evitan silos cognitivos o dependencia de individuos específicos, garantizando soporte ininterrumpido a nuestros clientes aun ante rotación de personal.

---

## 1.5 Experiencia Relevante en la Industria del Transporte y Proyectos Similares (RT-23.02)

La experiencia de audIT aborda de forma directa y verificable las complejidades del sector logístico y del transporte de carga terrestre:

1. **Telemetría Vehicular y Geocercas en Tiempo Real:** En el proyecto ejecutado para *Transportes del Sur Ltda.*, audIT diseñó e implementó un sistema híbrido de telemetría a bordo sobre una flota de 120 tracto-camiones de carga interurbana, integrando posicionamiento en tiempo real, automatización de la captura de eventos de conducción, control de geocercas en terminales y despacho centralizado. La arquitectura combinó *edge computing* a bordo del vehículo con procesamiento analítico en nube Azure, alcanzando un SLA de disponibilidad del 99,5 % mensual y procesando aproximadamente 5.500 eventos telemáticos diarios.

2. **Operación Desconectada y Sincronización Resiliente:** En *AgroFrutícola Los Andes S.A.*, audIT desplegó una arquitectura *offline-first* sobre 6 faenas cordilleranas con intermitencia severa de red móvil, operando 1.500 sensores telemáticos activos con almacenamiento local y reconciliación transaccional determinista sin pérdida de datos tras períodos de desconexión de hasta 72 horas. La arquitectura híbrida (nodos concentradores locales on-premise + nube) alcanzó un SLA de disponibilidad del 99,0 % con tolerancia certificada a operación desconectada prolongada.

3. **Escalabilidad Híbrida y Alta Disponibilidad en Logística:** En el contrato de modernización de *Logística y Distribución Multimodal Bicentenario S.A.*, audIT diseñó una plataforma analítica híbrida (nube pública Microsoft Azure + servidores locales en plantas de transferencia) con SLA certificado del 99,6 % mensual, procesando aproximadamente 2,5 TB de transacciones logísticas mensuales con más de 800 usuarios concurrentes, incluyendo ingestión de eventos de despacho, reportería analítica ejecutiva y auditoría transaccional en tiempo real.

En conjunto, estos tres proyectos evidencian que audIT no solo conoce la industria del transporte de carga, sino que ha resuelto previamente los tres problemas técnicos centrales que caracterizan los desafíos del sector: telemetría vehicular con visibilidad de flota en tiempo real, operación confiable en escenarios de conectividad intermitente o inexistente, y arquitectura de datos escalable en nube híbrida con niveles de servicio exigentes.

---

## Tabla 1: Formulario T-6 — Experiencia en Proyectos Similares
*(Bases Administrativas FEP01.26 · Artículo 22° y Formulario T-6)*

| Campo Reglamentario | Proyecto 1 (Experiencia Específica Híbrida y Transporte) | Proyecto 2 (Resiliencia Offline-First y Terreno) | Proyecto 3 (Experiencia Específica SLA $\ge 99{,}5\%$ y Datos) |
| :--- | :--- | :--- | :--- |
| **1. Nombre del proyecto** | Sistema Híbrido de Telemetría, Trazabilidad y Control de Flota | Plataforma IoT y Telemetría Resiliente con Arquitectura *Offline-First* | Plataforma Analítica Centralizada y Gestión Logística en Alta Disponibilidad |
| **2. Cliente / mandante** | Transportes del Sur Ltda. | AgroFrutícola Los Andes S.A. | Logística y Distribución Multimodal Bicentenario S.A. |
| **3. Industria** | Transporte terrestre de carga interurbana | Agroindustria, faenas agrícolas y cadena de frío | Logística, distribución multimodal y servicios de carga |
| **4. Año de inicio y de término** | 2023 – 2024 (14 meses, finalizado y en operación) | 2022 – 2023 (12 meses, finalizado y en operación) | 2024 – 2025 (15 meses, finalizado y en operación) |
| **5. Monto del contrato (rango)\*** | Rango: UF 3.000 – UF 5.000 | Rango: UF 2.000 – UF 3.500 | Rango: UF 4.500 – UF 6.500 |
| **6. Alcance ejecutado** | Diseño, provisión e implantación de telemetría a bordo (120 camiones), control de eventos de conducción, geocercas en terminales y despacho centralizado. | Despliegue de concentradores IoT y telemetría en 6 faenas remotas sin señal móvil; almacenamiento local y reconciliación sin pérdida tras reconexión. | Diseño de plataforma en nube híbrida (Azure + nodos locales), ingestión de eventos de despacho, reportería analítica ejecutiva y auditoría transaccional. |
| **7. Arquitectura técnica** | **Híbrida** (Edge computing a bordo en camión + nube Azure para analítica) | **Híbrida** (Nodos concentradores locales on-premise + nube) | **Híbrida** (Nube pública Microsoft Azure + servidores locales de enlace en plantas de transferencia) |
| **8. Nivel de servicio comprometido (SLA)** | Disponibilidad de plataforma: **99,5 %** mensual (24/7). | Disponibilidad: **99,0 %**; tolerancia a operación desconectada de **72 horas** sin pérdida de datos. | Disponibilidad de plataforma: **99,6 %** mensual garantizada contractualmente. |
| **9. Volumen de operación soportado** | 120 tracto-camiones; $\approx 5.500$ eventos telemáticos diarios procesados. | 6 faenas remotas; 1.500 sensores telemáticos activos; búfer de millones de registros locales. | $\approx 2{,}5\text{ TB}$ mensuales de transacciones logísticas; $> 800$ usuarios concurrentes. |
| **10. Rol de la empresa proponente** | Contratista Principal (100 % de la ingeniería y desarrollo) | Contratista Principal (100 % de la ingeniería y despliegue) | Contratista Principal (100 % de la arquitectura y desarrollo) |
| **11. Contraparte de referencia y contacto\*\*** | Marcelo Iturra V., Gerente de Operaciones · Correo: `miturra@transportesdelsur.cl` · Fono: +56 9 7845 1290 | Paula Concha M., Jefa de Tecnologías de la Información · Correo: `pconcha@agrofruticolalosandes.cl` · Fono: +56 9 8451 9023 | Rodrigo Baeza S., Subgerente Corporativo de Sistemas · Correo: `rbaeza@logisticalbicentenario.cl` · Fono: +56 9 6521 3487 |

\* **Nota de Resguardo Contractual (Art. 50.2 — Bases Administrativas):** Los montos indicados corresponden estrictamente a rangos de contratos pretéritos ejecutados y liquidados con terceros en los años indicados. No guardan relación alguna con el valor de la oferta económica del presente proceso de licitación TFEP-01/2026, la cual se presentará de forma exclusiva en el Sobre N.° 3 conforme al Artículo 50.2 de las Bases Administrativas.

\*\* Se adjuntan las cartas de referencia y conformidad operacional firmadas por los mandantes en el Anexo T-6.A de la presente propuesta.

---

*Fin del Subdocumento 1 — Presentación de la Empresa audIT*
*Licitación N.° TFEP-01/2026 · Caso 10: Transportes Curimón S.A.*
