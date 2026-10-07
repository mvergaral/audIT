# Formulario T-6. Experiencia en proyectos similares

audIT, Empresa N.º 10. Licitación TFEP-01/2026, Caso 10 Transporte de Carga. Oferta Técnica, Sobre N.º 2. Informe Preparatorio 2. Archivo AUDIT-Formulario-T-6.pdf. Anexo del Subdocumento N.º 1, Presentación de la empresa. Las fuentes están en las Referencias de ese subdocumento.

\makeatletter
\audit@iniciarpartes
\makeatother
{\renewcommand\textoEncabezado{\color{audit-marino}Índice}\indiceDetallado}

\makeatletter
\audit@marcasubdoc{Subdocumento 1}
\makeatother
\markboth{Formulario T-6}{}
\registrarFolio{formsd-1}{Formulario T-6: catálogo de experiencia}
\phantomsection
\addcontentsline{toc}{section}{Formulario T-6: catálogo de experiencia}
\begin{formulario}{T-6}
Las tres fichas y sus instrumentos asociados representan la experiencia declarada por audIT y se cotejan con el expediente del Sobre N.º 1; este registro documental no acredita una revisión externa de los originales. Los once campos, tres proyectos y sus períodos se mantienen. Los SLA contractuales históricos son mensuales: 99,5 %, 99,2 % y 99,6 %; cualquier promedio medido informado en un acta es una magnitud distinta. Los rangos monetarios corresponden a esos contratos históricos, no al precio de la oferta para Curimón.
\begingroup\emergencystretch=3em
  \begin{formularioTSeis}

    \proyectoTSeis{
      nombre       = Sistema Híbrido de Telemetría  Trazabilidad y Control de Flota,
      cliente      = Transportes del Sur Ltda.,
      industria    = Transporte terrestre interurbano de carga pesada y distribución troncal,
      periodo      = 2023--2024 (14 meses de implementación; en operación continuada),
      monto        = Rango histórico superior a 50.000 Unidades de Fomento,
      alcance      = Provisión e instalación de pasarelas embarcadas CANbus J1939; desarrollo de plataforma cloud de despacho  control de geocercas dinámicas y monitoreo en tiempo real.,
      arquitectura = Híbrida: Edge computing en cabina + nube pública Microsoft Azure,
      servicio     = 99{,}5 % mensual en disponibilidad de plataforma 24/7/365,
      volumen      = 340 tractocamiones activos; $≈ 88.000 viajes anuales; > 6{,}8$ millones de eventos/día,
      rol          = Contratista Principal (100 % ingeniería  desarrollo y soporte),
      contacto     = Marcelo Iturra Valenzuela  Gerente de Operaciones (miturra@transportesdelsur.cl  +56 9 7845 1290)
    }

    \proyectoTSeis{
      nombre       = Plataforma IoT y Telemetría Resiliente con Arquitectura Offline-First,
      cliente      = AgroFrutícola Los Andes S.A.,
      industria    = Agroindustria  faenas remotas y logística de exportación en frío,
      periodo      = 2022--2023 (12 meses de implementación; en operación continuada),
      monto        = Rango histórico entre 30.000 y 45.000 Unidades de Fomento,
      alcance      = Despliegue de concentradores telemáticos locales on-premise  integración de 1.500 sensores de frío PT100 y sincronización bidireccional offline-first.,
      arquitectura = Híbrida: Concentradores locales on-premise en plantas + nube Microsoft Azure,
      servicio     = 99{,}2 % mensual; tolerancia a operación desconectada de 72 horas,
      volumen      = 310 unidades de transporte y frío; 12 faenas remotas; $≈ 82.000$ despachos/año,
      rol          = Contratista Principal (100 % ingeniería  integración y despliegue),
      contacto     = Paula Concha Morales  Jefa de Tecnologías de Información (pconcha@agrofruticolalosandes.cl  +56 9 8451 9023)
    }

    \proyectoTSeis{
      nombre       = Plataforma Analítica Centralizada y Gestión Logística en Alta Disponibilidad,
      cliente      = Logística y Distribución Multimodal Bicentenario S.A.,
      industria    = Logística portuaria  distribución multimodal y transferencia de carga,
      periodo      = 2024--2025 (15 meses de implementación; en operación continuada),
      monto        = Rango histórico superior a 60.000 Unidades de Fomento,
      alcance      = Arquitectura cloud escalable en Azure con microservicios e ingesta de eventos de alta velocidad; reportería analítica y despacho automatizado.,
      arquitectura = Híbrida: Nube Microsoft Azure articulada con servidores de borde en terminales,
      servicio     = 99{,}6 % mensual garantizado contractualmente con monitoreo continuo,
      volumen      = 390 tractocamiones y portacontenedores; $≈ 98.000 viajes anuales; > 12$ millones de eventos/día,
      rol          = Contratista Principal (100 % arquitectura  software e implantación),
      contacto     = Rodrigo Baeza Santander  Subgerente Corporativo de Sistemas (rbaeza@logisticabicentenario.cl  +56 9 6521 3487)
    }

  \end{formularioTSeis}

  \providecommand\tituloBloqueFormulario[1]{
    \phantomsection\addcontentsline{toc}{section}{#1}{\sffamily\bfseries\fontsize{13bp}{16bp}\selectfont\color{audit-marino}#1}}
  \providecommand\subtituloBloqueFormulario[1]{
    \phantomsection\addcontentsline{toc}{subsection}{#1}{\sffamily\bfseries\fontsize{11bp}{14bp}\selectfont\color{audit-marino}#1}}

  \tituloBloqueFormulario{Fichas de detalle técnico por proyecto}

Las fichas explican el contexto, la solución y los resultados de los tres proyectos resumidos en el catálogo.

  \subtituloBloqueFormulario{Ficha Técnica 1: Sistema Híbrido de Telemetría, Trazabilidad y Control de Flota}
  La ficha desarrolla los antecedentes técnicos y los resultados de operación del proyecto.
- **Mandante:** Transportes del Sur Ltda. (RUT: 77.412.980-4).
- **Contexto Operacional y Desafío de Ingeniería:** Control telemático en ruta sobre un parque de 340 tractocamiones en transporte troncal interurbano (Ruta 5 Sur entre Región Metropolitana y Región de Los Lagos). Flota heterogénea multimarca que requería lectura no intrusiva de bus CAN SAE J1939 sin alterar el cableado original ni vulnerar garantías de fabricante.
- **Solución Implementada por audIT SpA:** Despliegue de pasarelas ARM Cortex-A7 con Linux embebido; acopladores inductivos *CANclick*; motor de borde con búfer SQLite en modo WAL para persistencia en zonas de sombra celular en Ruta 5 Sur; plataforma cloud en *Azure Kubernetes Service* (AKS), ingestión continua con *Azure Event Hubs* y base de datos distribuida PostgreSQL / TimescaleDB.
- **Resultados Verificables:** Reducción auditada de 7,4% en consumo de combustible mediante control de ralentí y alertas pasivas; cumplimiento del SLA contractual de disponibilidad mensual de 99,5% durante el período de operación posterior a la recepción de mayo de 2024; procesamiento íntegro de > 6{,}8 millones de eventos telemáticos diarios.

  \subtituloBloqueFormulario{Ficha Técnica 2: Plataforma IoT y Telemetría Resiliente con Arquitectura Offline-First}
  La ficha desarrolla los antecedentes técnicos y los resultados de operación del proyecto.
- **Mandante:** AgroFrutícola Los Andes S.A. (RUT: 96.834.120-0).
- **Contexto Operacional y Desafío de Ingeniería:** Logística de exportación agrícola distribuida en 12 faenas y centrales de empaque precordilleranas (Valparaíso, O'Higgins y Maule) con zonas de sombra celular de hasta 72 horas continuas, requiriendo trazabilidad térmica ininterrumpida sobre 310 unidades refrigeradas.
- **Solución Implementada por audIT SpA:** Servidores industriales de borde (*edge servers*) locales en plantas de empaque y pasarelas a bordo con sondas PT100; protocolo de sincronización determinista *offline-first* con marcas de tiempo monotónicas y firmas SHA-256; reconciliación en lote comprimido con algoritmo Zstandard (*zstd*) al retornar a red industrial o celular, garantizando cero pérdida de transacciones y cero colisiones; consolidación en Azure para certificación fitosanitaria de exportación.
- **Resultados Verificables:** Trazabilidad térmica continua del 100% de despachos de exportación en frío; resiliencia operativa demostrada ante 72 horas continuas sin cobertura celular sin pérdida de datos; disponibilidad mensual de plataforma del 99,2%.

  \subtituloBloqueFormulario{Ficha Técnica 3: Plataforma Analítica Centralizada y Gestión Logística en Alta Disponibilidad}
  La ficha desarrolla los antecedentes técnicos y los resultados de operación del proyecto.
- **Mandante:** Logística y Distribución Multimodal Bicentenario S.A. (RUT: 76.305.440-3).
- **Contexto Operacional y Desafío de Ingeniería:** Transporte intermodal y transferencia de carga entre puertos (San Antonio y Valparaíso) y terminales intermodales en Santiago, administrando una flota de 390 tractocamiones y portacontenedores con > 98.000 viajes anuales y ventanas de alta congestión portuaria.
- **Solución Implementada por audIT SpA:** Capa Anticorrupción (ACL) con APIs RESTful seguras (OpenAPI 3.1) para absorber tres proveedores GPS comerciales previos y sistemas SAP empresariales; arquitectura cloud en Microsoft Azure con replicación geográfica multi-zona y bus de eventos asíncrono para > 800 usuarios concurrentes y latencia API percentil 95 (P95) $< 120\text{ ms}$; despacho automatizado de viajes y atestación de servicios prestados.
- **Resultados Verificables:** SLA auditado de 99,6% mensual garantizado contractualmente; ingestión estable de > 12 millones de eventos diarios; visibilidad de carga en tiempo real para empresas navieras e importadores.

  \tituloBloqueFormulario{Acreditación documental y cartas de referencia de mandantes}

  En conformidad con lo prescrito en el FEP01, Artículo 34.1, p. 22 de las Bases Administrativas (*«Acreditación: Formulario T-6 y carta de referencia del mandante»*), a continuación se presentan transcripciones de las actas formales de recepción final conforme y certificaciones de servicio emitidas por los mandantes de los tres proyectos declarados.

  \subtituloBloqueFormulario{Anexo T6.A: Acta formal de recepción final conforme y certificado de servicio — Transportes del Sur Ltda.}
  **Folio Oficial:** ACTA-REC-2024-088 · **Contrato:** CT-2023-TSUR-041 · **Resolución:** Res. Directorio TSUR N.° 2024/05-R
  **Fecha de Emisión:** 14 de enero de 2026 · **Fecha de Cierre Definitivo:** 31 de mayo de 2024
  **Mandante:** Transportes del Sur Ltda. · RUT: 77.412.980-4 · Av. Presidente Jorge Alessandri 11200, San Bernardo, Región Metropolitana.
  **Contratista Principal:** audIT Soluciones Tecnológicas SpA · RUT: 76.924.310-0 [4pt]
  Por medio del presente instrumento, don **Marcelo Iturra Valenzuela**, C.I. N.° 11.654.892-5, en su calidad de Gerente de Operaciones y Representante Técnico Facultado de Transportes del Sur Ltda., certifica bajo fe de juramento institucional que la empresa **audIT Soluciones Tecnológicas SpA** ejecutó en calidad de **Contratista Principal (100% de responsabilidad técnica)** el proyecto individualizado entre el 15 de marzo de 2023 y el 31 de mayo de 2024 (14 meses de ejecución), manteniéndose a la fecha bajo régimen de soporte y operación continuada.
  Se deja constancia fehaciente de las siguientes especificaciones técnicas y operacionales auditadas:
- **Alcance y Parque Administrado:** Provisión e instalación de pasarelas telemáticas CANbus J1939 y plataforma central de control sobre una flota activa de **340 tractocamiones interurbanos** en Ruta 5 Sur, con volumetría anual sostenida de 88.000 viajes y > 6{,}8 millones de eventos telemáticos diarios.
- **Arquitectura Técnica:** Arquitectura híbrida de alta disponibilidad (*edge computing* en cabina vehicular y microservicios en Microsoft Azure) con persistencia local y operación desacoplada garantizada en zonas de sombra celular.
- **Disponibilidad Demostrada (SLA):** Disponibilidad mensual promedio de **99,55%**, superando el compromiso contractual mínimo del 99,5%.
- **Conformidad Final y Ausencia de Contingencias:** Entregables recepcionados a entera conformidad y satisfacción, sin reservas técnicas ni vicios pendientes. Se certifica que el contratista no fue objeto de multas, penalizaciones, litigios ni contingencias laborales o previsionales.

  *Contraparte suscriptora de la carta de referencia*
  **Marcelo Iturra Valenzuela** · Gerente de Operaciones · Transportes del Sur Ltda.
  Contacto: `miturra@transportesdelsur.cl` · Teléfono: +56 9 7845 1290

  \subtituloBloqueFormulario{Anexo T6.B: Acta formal de recepción final conforme y certificado de servicio — AgroFrutícola Los Andes S.A.}
  **Folio Oficial:** ACTA-REC-2023-014 · **Contrato:** CT-2022-AFLA-019 · **Resolución:** Res. Gerencial AFLA N.° 2023/01-TI
  **Fecha de Emisión:** 02 de febrero de 2026 · **Fecha de Cierre Definitivo:** 25 de enero de 2023
  **Mandante:** AgroFrutícola Los Andes S.A. · RUT: 96.834.120-0 · Camino Internacional Km 12, San Esteban, Región de Valparaíso.
  **Contratista Principal:** audIT Soluciones Tecnológicas SpA · RUT: 76.924.310-0 [4pt]
  Por medio del presente instrumento, doña **Paula Concha Morales**, C.I. N.° 13.921.405-6, en su calidad de Jefa de Tecnologías de Información de AgroFrutícola Los Andes S.A., certifica bajo fe de juramento institucional que **audIT Soluciones Tecnológicas SpA** ejecutó en calidad de **Contratista Principal (100% de ingeniería y desarrollo)** el proyecto entre el 10 de enero de 2022 y el 25 de enero de 2023 (12 meses de duración), prestando soporte continuo hasta la actualidad.
  Se certifica el cumplimiento pleno de:
- **Alcance y Parque Administrado:** Despliegue telemático en **310 unidades de transporte y furgones refrigerados**, integrando 1.500 sensores de temperatura digital PT100 y concentradores en 12 plantas de empaque precordilleranas.
- **Arquitectura Híbrida y Resiliencia Desconectada:** Arquitectura híbrida con diseño *offline-first*, garantizando tolerancia absoluta a operación desconectada de hasta **72 horas continuas** en faenas rurales, con reconciliación determinista de datos y cero pérdida de registros térmicos.
- **Disponibilidad Demostrada (SLA):** Disponibilidad auditada del **99,2% mensual**, habilitando auditorías fitosanitarias internacionales de exportación.
- **Conformidad Final y Ausencia de Contingencias:** Recepción conforme sin observaciones técnicas pendientes, con cuenta corriente contractual liquidada sin reclamos ni controversias de ningún orden.

  *Contraparte suscriptora de la carta de referencia*
  **Paula Concha Morales** · Jefa de Tecnologías de Información · AgroFrutícola Los Andes S.A.
  Contacto: `pconcha@agrofruticolalosandes.cl` · Teléfono: +56 9 8451 9023

  \subtituloBloqueFormulario{Anexo T6.C: Acta formal de recepción final conforme y certificado de servicio — Logística Bicentenario S.A.}
  **Folio Oficial:** ACTA-REC-2025-102 · **Contrato:** CT-2024-BIC-077 · **Resolución:** Res. Directorio BIC N.° 2025/03-SIS
  **Fecha de Emisión:** 20 de marzo de 2026 · **Fecha de Cierre Definitivo:** 28 de marzo de 2025
  **Mandante:** Logística y Distribución Multimodal Bicentenario S.A. · RUT: 76.305.440-3 · Av. Puerto Central 450, San Antonio, Región de Valparaíso.
  **Contratista Principal:** audIT Soluciones Tecnológicas SpA · RUT: 76.924.310-0 [4pt]
  Por medio del presente instrumento, don **Rodrigo Baeza Santander**, C.I. N.° 12.433.871-9, en su calidad de Subgerente Corporativo de Sistemas de Logística y Distribución Multimodal Bicentenario S.A., certifica bajo fe de juramento institucional que **audIT Soluciones Tecnológicas SpA** desarrolló e implementó en calidad de **Contratista Principal** la plataforma corporativa entre el 02 de enero de 2024 y el 28 de marzo de 2025 (15 meses), prestando soporte continuo a la fecha.
  Se deja constancia fehaciente de:
- **Volumen Operacional y Escala:** Monitoreo en tiempo real de **390 tractocamiones y portacontenedores**, con demanda anual > 98.000 viajes e ingestión sobre 12 millones de eventos diarios en ventanas de alta congestión portuaria.
- **Arquitectura y Concurrencia:** Solución híbrida basada en Microsoft Azure y terminales locales de transferencia, soportando > 800 usuarios concurrentes y latencia API P95 inferior a 120 ms.
- **Disponibilidad Demostrada (SLA):** Cumplimiento continuo auditado de un SLA mensual de **99,6%**, con redundancia multi-zona y conmutación automática por falla (*failover*).
- **Conformidad Final y Ausencia de Contingencias:** Recepción definitiva conforme sin observaciones, sin multas contractuales y sin litigios de ninguna especie.

  *Contraparte suscriptora de la carta de referencia*
  **Rodrigo Baeza Santander** · Subgerente Corporativo de Sistemas · Logística Bicentenario S.A.
  Contacto: `rbaeza@logisticabicentenario.cl` · Teléfono: +56 9 6521 3487

  \tituloBloqueFormulario{Declaración del representante y localización del expediente}

  El representante legal identifica las cartas de referencia y actas que sustentan la experiencia declarada en este formulario, conforme al FEP01, Artículo 34.1, p. 22. La transcripción técnica permite cotejar sus datos; la autenticidad y la modalidad de firma se comprueban sobre los instrumentos originales.
- Transportes del Sur Ltda.: ACTA-REC-2024-088, contrato CT-2023-TSUR-041.
- AgroFrutícola Los Andes S.A.: ACTA-REC-2023-014, contrato CT-2022-AFLA-019.
- Logística y Distribución Multimodal Bicentenario S.A.: ACTA-REC-2025-102, contrato CT-2024-BIC-077.

  Estos antecedentes se individualizan en el expediente `EXP-T6-AUDIT-2026`, dentro del Sobre N.º 1. Sus contactos, fechas, alcance, volúmenes y disponibilidad deben coincidir con las fichas y con las cartas de referencia. Los rangos monetarios del catálogo son históricos y no corresponden al precio de la oferta actual. Las disponibilidades declaradas son mensuales: 99,5%, 99,2% y 99,6%, respectivamente.

  \begin{center}
    \includegraphics[height=1.4cm]{portadas/activos/media-firma.png} [4pt]
    **Alejandro Hermosilla Díaz**
    Representante Legal · audIT Soluciones Tecnológicas SpA
    RUT: 14.892.341-8
  \end{center}
\endgroup
\end{formulario}

