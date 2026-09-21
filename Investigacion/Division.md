# Plan Operativo — AudIT · TI-12

## Cumplimiento normativo en proyectos TIC: Ley 21.719, Ley 21.663 (ANCI) y marco internacional

**Documento interno de coordinación · Versión Opus · 15 de septiembre de 2026**

> **Contexto de ejecución.** El equipo AudIT (8 integrantes) dispone de **6 días calendario** (miércoles 16 → lunes 21 de septiembre de 2026, considerando los feriados patrios del 18 y 19) para entregar: (a) informe escrito de 10-15 páginas, (b) presentación ejecutiva en PowerPoint/PDF, (c) cuestionario de 30 preguntas con justificaciones e índice temático y (d) anexo de declaración de uso de IA firmado individualmente. La entrega electrónica e impresa se realiza el **lunes 21 de septiembre de 2026**.

> [!CAUTION]
> Este plan opera bajo las restricciones del **Comunicado 9**: toda sección cuyo texto no evidencie trabajo de ingeniería propio del grupo (figuras huérfanas, cifras sin cálculo mostrado, contradicciones entre capítulos, marcadores residuales de IA) puede derivar en puntaje 0 del subdocumento completo a partir del Informe 2, sin posibilidad de subsanación.

---

## Mapa de Organización del Equipo

```
                    ┌──────────────────────────────────────────────────────────────┐
                    │   Persona 1: LIDERAZGO EDITORIAL, COHERENCIA & APORTE PROPIO│
                    └────────────────────────────┬─────────────────────────────────┘
                                                 │ Supervisa & Ensambla
           ┌─────────────────────────────────────┼─────────────────────────────────────┐
           ▼                                     ▼                                     ▼
  ┌────────────────────┐              ┌─────────────────────────┐              ┌────────────────────┐
  │   INVESTIGACIÓN    │              │   INGENIERÍA LEGAL &    │              │  EVALUACIÓN &      │
  │   NORMATIVA &      │              │   MODELADO ECONÓMICO    │              │  COMUNICACIÓN      │
  │   COMPARATIVA      │              │                         │              │                    │
  ├────────────────────┤              ├─────────────────────────┤              ├────────────────────┤
  │ P2: Marco Legal    │              │ P4: Impacto Económico   │              │ P6: Cuestionario   │
  │     Chile          │              │     & TCO Cumplimiento  │              │     30 Preguntas   │
  │ P3: Marco          │              │ P5: Arquitectura de     │              │ P7: Presentación   │
  │     Internacional  │              │     Cumplimiento &      │              │     Ejecutiva &    │
  │     & Herramientas │              │     Caso de Licitación  │              │     Defensa Oral   │
  └────────┬───────────┘              └──────────┬──────────────┘              └─────────┬──────────┘
           │                                     │                                      │
           └─────────────────┬───────────────────┘                                      │
                             ▼                                                          ▼
  ┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
  │ Persona 8: AUDITOR DE CALIDAD, VERIFICACIÓN DE VIGENCIA (2025/2026) & FORMULARIO A-6 (ANTI-C9) │
  └──────────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 1. Perfiles y Asignación de Roles (Persona 1 a 8)

### Persona 1 — Líder de Integración Editorial, Introducción/Aporte Propio y Coherencia Global

* **Rol funcional:** Technical Lead, Lead Editor & System Integrator.
* **Características / habilidades ideales:**
  - Redacción académica de nivel de licitación profesional; capacidad de discriminar entre texto sustantivo y relleno.
  - Visión sistémica del documento: puede detectar contradicciones cruzadas entre capítulos de distintos autores.
  - Firmeza editorial para rechazar y devolver secciones que violen las 10-15 páginas o que contengan figuras sin análisis.
  - Dominio sólido del vocabulario jurídico-técnico chileno (datos personales, servicios esenciales, operadores de importancia vital).
* **Tareas entregables concretas:**
  1. Definición del **índice oficial del informe**, asignación de presupuesto de páginas por capítulo (distribución sugerida más abajo) y plantilla de maquetación con formato unificado.
  2. Redacción de la **Introducción**, incluyendo el párrafo obligatorio de delimitación de **Aporte Propio** (conforme a la Sección 4 de las indicaciones: qué proviene de la ficha y qué es aporte genuino del grupo).
  3. Redacción del **Resumen Ejecutivo** (máx. ½ página) y del capítulo de **Conclusiones y Recomendaciones Estratégicas**.
  4. **Control de coherencia narrativa global:** verificar que los mismos términos legales se usen de manera consistente (ej. «responsable del tratamiento» vs. «encargado»), que las fechas de vigencia citadas por P2 y P3 coincidan entre sí, y que la terminología técnica sea homogénea.
  5. Consolidación final del documento maestro y exportación a **PDF con la nomenclatura estricta del curso**: `10 - AUDIT - TI-12` (archivo) y `[ICI544] - 10 - AUDIT - TI-12` (asunto del correo).
* **Nivel de uso de IA previsto y registro A-6:**
  - **Nivel 0** en Introducción (delimitación del aporte propio), Conclusiones y Recomendaciones (restricción mandatoria del punto 6.1 de las indicaciones).
  - **Nivel 1** en tareas de maquetación, revisión ortotipográfica y normalización de estilo.
  - **Evidencia:** Historial de versiones en Google Docs o historial de commits del repositorio Git mostrando las iteraciones humanas sobre estos capítulos.

> [!TIP]
> **Distribución de páginas sugerida (sobre un objetivo de ~13 páginas):**
>
> | Sección | Páginas |
> | :--- | :---: |
> | Resumen Ejecutivo + Introducción (con párrafo de Aporte Propio) | 1,5 |
> | Marco Legal Chileno (P2) | 2,5 |
> | Marco Internacional y Normas Técnicas (P3) | 2,5 |
> | Cuadro Comparativo de Herramientas GRC y Normativas (P2+P3) | 1,5 |
> | Impacto Económico del Cumplimiento y Matriz de Obligaciones (P4) | 2,0 |
> | Arquitectura de Cumplimiento y Vínculo con el Caso (P5) | 2,0 |
> | Conclusiones y Recomendaciones Estratégicas (P1) | 1,0 |
> | **Total estimado** | **~13,0** |
>
> *El cuestionario de 30 preguntas, el anexo A-6 y las referencias bibliográficas NO cuentan dentro de las 10-15 páginas del cuerpo.*

---

### Persona 2 — Especialista en Marco Legal Chileno y Normativa Nacional

* **Rol funcional:** Chilean Regulatory Research Specialist.
* **Características / habilidades ideales:**
  - Capacidad de lectura y síntesis de textos legales chilenos (Biblioteca del Congreso Nacional, Diario Oficial).
  - Comprensión de la estructura institucional del Estado chileno en materia de datos y ciberseguridad.
  - Rigor para citar artículos, incisos y fechas de vigencia con precisión jurídica.
  - Familiaridad con el ecosistema de protección de datos personales y la transición desde la Ley 19.628 hacia la Ley 21.719.
* **Tareas entregables concretas:**
  1. **Análisis profundo de la Ley 21.719** (protección y tratamiento de datos personales): fecha de entrada en vigencia, Agencia de Protección de Datos, distinción responsable vs. encargado del tratamiento, bases de licitud, datos sensibles, derechos de los titulares (ARCO + portabilidad), régimen de sanciones (montos, infracciones leves/graves/gravísimas).
  2. **Análisis profundo de la Ley 21.663** (marco de ciberseguridad): ANCI y CSIRT Nacional, distinción entre servicios esenciales y operadores de importancia vital, deberes de seguridad, plazos de reporte de incidentes según su reglamento.
  3. Investigación de la **Ley 21.180** (Transformación Digital del Estado), la **Ley 19.628** (antecedente) y **al menos 2 normativas chilenas adicionales** no listadas en la ficha (ej. Ley 20.285 de Transparencia, normativa sectorial de la CMF, instrucciones de la Contraloría sobre datos, Política Nacional de Ciberseguridad 2023-2028, o decreto reglamentario de la ANCI), justificando por qué merecen entrar en la comparativa.
  4. **Mapa de organismos chilenos relevantes** con sus competencias, fechas de constitución efectiva y estado operacional verificado a septiembre de 2026 (Agencia PDP, ANCI, CSIRT Nacional, + otros que identifique).
  5. Contribución a la **columna nacional** del cuadro comparativo multicriterio conjunto con P3.
  6. Si tras investigar concluye que no existen más normativas chilenas relevantes, **declaración expresa de exhaustividad negativa** con bitácora de búsqueda (fuentes, criterios de descarte, fecha).
* **Nivel de uso de IA previsto y registro A-6:**
  - **Nivel 2** para síntesis inicial de cuerpos legales extensos y estructuración de esquemas de análisis.
  - **Nivel 0** en la interpretación jurídica final, el análisis comparativo y la ponderación de criterios (restricción del punto 6.1).
  - **Evidencia:** Exportación de chats usados para estructurar el esquema de análisis; enlace directo a cada ley en BCN (Biblioteca del Congreso Nacional) como fuente primaria verificada.

---

### Persona 3 — Especialista en Marco Internacional, Normas Técnicas y Herramientas de Apoyo

* **Rol funcional:** International Regulatory & GRC Tooling Specialist.
* **Características / habilidades ideales:**
  - Lectura fluida en inglés técnico-jurídico (los textos fuente del RGPD, NIS2, NIST y Reglamento IA están en inglés).
  - Conocimiento del ecosistema de estándares internacionales (ISO/IEC, NIST, ENISA).
  - Capacidad de evaluar herramientas de software GRC (Governance, Risk, Compliance) y de gestión de consentimiento.
  - Espíritu crítico para identificar el «techo de complejidad» de las plataformas y su real aplicabilidad en el contexto chileno.
* **Tareas entregables concretas:**
  1. **Análisis del marco internacional obligatorio:** RGPD (UE 2016/679), Directiva NIS2, Reglamento Europeo de IA (UE 2024/1689) y Reglamento de Ciberresiliencia (CRA), verificando plazos de aplicación vigentes a septiembre de 2026.
  2. **Normas técnicas certificables:** ISO/IEC 27001:2022 (SGSI), ISO/IEC 27701 (extensión de privacidad), ISO/IEC 42001:2023 (SGAIA), NIST Cybersecurity Framework 2.0 — con análisis del **costo de certificación** (auditoría, consultora, mantenimiento anual).
  3. Investigación e incorporación de **al menos 2 marcos normativos o estándares adicionales** no listados en la ficha (ej. SOC 2 Type II, ISO 22301 (continuidad de negocio), NIST AI RMF 1.0, estándar PCI-DSS v4.0, Convenio 108+ del Consejo de Europa, o legislación LATAM como la LGPD brasileña), justificando su relevancia para un proyecto TIC operado desde Chile.
  4. **Comparativa de herramientas GRC y de apoyo al cumplimiento** (mínimo 6 + 2 de aporte propio):
     - Herramientas listadas en la ficha: plataformas de GRC, gestión de consentimiento, descubrimiento y clasificación de datos personales.
     - Deberá mapear: OneTrust, Vanta, Drata, ServiceNow GRC, BigID, Microsoft Purview Compliance Manager, y al menos 2 adicionales (ej. Securiti.ai, TrustArc, Osano, WireWheel, Transcend, Collibra Privacy, Palqee, u open-source como OpenDPIA).
  5. Confección del **cuadro comparativo multicriterio** conjunto con P2 (≥ 6 herramientas/normativas), con criterios explícitos y ponderados.
* **Nivel de uso de IA previsto y registro A-6:**
  - **Nivel 2** para prospección de herramientas de mercado y traducción/síntesis de documentos en inglés.
  - **Nivel 0** en el análisis comparativo, la ponderación de criterios y la justificación de selección.
  - **Evidencia:** Registro de prompts de prospección, capturas de pantalla de la documentación oficial de cada herramienta con fecha visible, enlace a páginas oficiales de ISO, NIST y EUR-Lex.

---

### Persona 4 — Modelado Económico del Cumplimiento, Dimensionamiento e Impacto Financiero

* **Rol funcional:** Compliance Cost Modeler & Financial Impact Analyst.
* **Características / habilidades ideales:**
  - Rigor numérico absoluto: toda cifra debe ser rastreable hasta su fuente oficial (precio de lista del proveedor, tarifa del organismo certificador, cotización de mercado laboral).
  - Manejo avanzado de planillas de cálculo y modelado de escenarios (Excel/Google Sheets).
  - Comprensión de estructuras de costos de cumplimiento: roles dedicados (DPO, CISO, equipo legal), licencias de herramientas GRC, costos de auditoría y certificación, y seguros de ciberriesgo.
  - Capacidad de integrar el impacto del cumplimiento en el **flujo de caja, VAN y TIR** de la propuesta técnico-económica.
* **Tareas entregables concretas:**
  1. **Matriz de obligaciones aplicables al caso** (entregable obligatorio de la ficha TI-12): tabla que vincule cada obligación legal con su actividad de cumplimiento, el rol responsable, el plazo normativo y la **partida de costo asociada** (formato: Obligación → Actividad → Rol → Plazo → Costo estimado).
  2. **Estimación del impacto económico del cumplimiento** sobre el proyecto, desglosado en:
     - Roles dedicados: DPO, CISO, analista de cumplimiento, asesor legal externo (con salarios/honorarios de mercado chileno, fuente: encuestas salariales 2025/2026 verificadas).
     - Herramientas GRC: licencias anuales de las plataformas evaluadas por P3 (fuente: pricing oficial del proveedor, fecha de consulta).
     - Auditorías y certificaciones: costo de certificación ISO 27001 inicial + mantenimiento anual (fuente: cotización de organismos como BSI, Bureau Veritas, SGS u otros, con fecha).
     - Seguros de ciberriesgo y multas potenciales: órdenes de magnitud del régimen sancionatorio de la Ley 21.719.
  3. **Reflejo en el flujo de caja:** Modelar cómo las partidas de cumplimiento alteran el flujo de caja del proyecto a 5 años, con análisis de sensibilidad sobre las 2 variables de mayor impacto (ej. costo del DPO + costo de herramienta GRC, o costo de auditoría + prima de seguro).
  4. **Tabla de precios con metadatos completos:** Cada cifra incluye producto, moneda (CLP o USD), región (Chile), fecha de consulta (2025/2026) y régimen (precio de lista, cotización, o «solo por cotización»).
* **Nivel de uso de IA previsto y registro A-6:**
  - **Nivel 0 estricto** en toda cifra, fórmula, cálculo y fuente numérica (las cifras inventadas por IA son falta grave conforme al punto 6 de las indicaciones).
  - **Nivel 1** para pulir la redacción de la memoria de cálculo.
  - **Evidencia:** Planilla de cálculo versionada (Google Sheets con historial de ediciones) y capturas de pantalla de las calculadoras/páginas de pricing con fecha visible.

---

### Persona 5 — Arquitecto de Cumplimiento y Vinculación con el Caso de Licitación

* **Rol funcional:** Compliance Architecture Designer & Case Integrator.
* **Características / habilidades ideales:**
  - Pensamiento arquitectónico: capacidad de modelar flujos de datos, puntos de decisión regulatoria y fronteras de cumplimiento.
  - Destreza en diagramación formal (Mermaid, Draw.io, C4 Model) para crear artefactos visuales que se integren argumentativamente en el texto.
  - Comprensión del ciclo de vida de un proyecto informático y de la licitación del caso asignado al grupo.
  - Capacidad de traducir obligaciones legales abstractas en actividades concretas dentro de una EDT (Estructura de Desglose de Trabajo) y carta Gantt.
* **Tareas entregables concretas:**
  1. **Diseño del diagrama de arquitectura de cumplimiento** para el caso del grupo: mapa visual que muestre los flujos de datos personales, los puntos de tratamiento, las fronteras de responsabilidad (responsable vs. encargado), los controles de seguridad exigidos y los flujos de reporte de incidentes al CSIRT/ANCI.
  2. Diseño del diagrama de **Privacidad y Seguridad desde el diseño y por defecto** (Privacy by Design): cómo se inserta el registro de actividades de tratamiento, la evaluación de impacto (EIPD) y los controles técnicos en el ciclo de vida del proyecto.
  3. **Análisis de transferencias internacionales de datos** y su efecto sobre la elección de región cloud y de proveedores: mapa de decisión que evalúe si el caso requiere residencia de datos en Chile, si existen cláusulas contractuales tipo, y cuáles proveedores cloud ofrecen regiones en Chile o LATAM.
  4. Redacción del capítulo de **Vínculo con la propuesta técnico-económica:** cómo las obligaciones de cumplimiento se traducen en partidas presupuestarias, roles en la EDT, hitos en la Gantt y criterios de aceptación en las bases técnicas.
  5. **Integración explicativa de toda figura en el cuerpo del texto:** cada diagrama debe ser citado, descrito paso a paso y vinculado con conclusiones. Cero figuras huérfanas (Comunicado 9, punto a).
* **Nivel de uso de IA previsto y registro A-6:**
  - **Nivel 2** para generar código base de diagramas Mermaid a partir de especificaciones humanas.
  - **Nivel 0** en el diseño de ingeniería, las decisiones arquitectónicas y la vinculación con el caso.
  - **Evidencia:** Commits del repositorio mostrando la evolución manual de los diagramas; prompts de generación de código Mermaid declarados en el A-6.

---

### Persona 6 — Diseñador Pedagógico del Cuestionario de 30 Preguntas

* **Rol funcional:** Assessment & Knowledge Verification Lead.
* **Características / habilidades ideales:**
  - Capacidad pedagógica: saber formular preguntas que evalúen comprensión, aplicación y análisis crítico, no solo memorización.
  - Precisión conceptual en terminología legal-técnica (no confundir «responsable» con «encargado», ni «ANCI» con «CSIRT»).
  - Redacción quirúrgica: preguntas sin ambigüedad, distractores plausibles y justificaciones que aporten valor.
  - Atención extrema al detalle normativo de la Sección 3 de las indicaciones.
* **Tareas entregables concretas:**
  1. Redacción de **30 preguntas originales** (autoría 100% humana, restricción mandatoria del punto 6.1) sobre los conceptos investigados.
  2. **Distribución estricta de dificultad:**
     - **12 preguntas básicas (40%):** Definiciones, conceptos fundamentales, identificación de organismos y marcos.
     - **12 preguntas intermedias (40%):** Aplicación práctica, comparación entre normativas, escenarios de cumplimiento.
     - **6 preguntas avanzadas (20%):** Análisis crítico, trade-offs entre marcos, resolución de casos con conflicto entre normativas.
  3. **Combinación obligatoria de formatos:** Selección múltiple, verdadero/falso con justificación, completar términos técnicos y respuesta corta.
  4. **Clave de respuestas:** Cada pregunta acompañada de su respuesta correcta y una **justificación técnica** que explique por qué es correcta y por qué las alternativas incorrectas no lo son.
  5. **Índice temático cruzado:** Tabla que vincule cada pregunta con la sección y el subtema del informe que cubre.
  6. **Calibración de cobertura:** Debe existir al menos 1 pregunta por cada subtema obligatorio de la ficha TI-12 (6 subtemas → mínimo 6 preguntas distribuidas), con distribución proporcional al peso del subtema.

> [!IMPORTANT]
> **Distribución mínima de cobertura temática sugerida:**
>
> | Subtema TI-12 | Preguntas mínimas | Ejemplo de enfoque |
> | :--- | :---: | :--- |
> | Ley 21.719 (datos personales) | 6 | Bases de licitud, derechos ARCO, régimen de sanciones |
> | Ley 21.663 (ANCI/ciberseguridad) | 5 | Servicios esenciales vs. OIV, plazos de reporte |
> | Privacidad desde el diseño | 4 | EIPD, registro de tratamiento, controles técnicos |
> | Transferencias internacionales | 3 | Regiones cloud, cláusulas contractuales, residencia |
> | Marco internacional (RGPD, NIS2, Reg. IA) | 7 | Comparación Chile-UE, plazos, extraterritorialidad |
> | Normas certificables (ISO 27001, 42001) | 5 | Costo certificación, alcance, relación con cumplimiento legal |
> | **Total** | **30** | |

* **Nivel de uso de IA previsto y registro A-6:**
  - **Nivel 0 estricto e innegociable.** La Sección 6.1 prohíbe taxativamente la redacción de preguntas, respuestas y justificaciones con IA. El grupo debe poder reconstruir el razonamiento oralmente.
  - **Evidencia:** Declaración explícita de autoría humana en el A-6. Borrador manuscrito o historial de ediciones en Google Docs como respaldo.

---

### Persona 7 — Director de Presentación Ejecutiva y Preparador de Defensa Oral

* **Rol funcional:** Executive Presentation Lead & Defense Coach.
* **Características / habilidades ideales:**
  - Diseño visual ejecutivo de alto impacto (PowerPoint/Google Slides): dominio de jerarquía visual, paletas cromáticas corporativas y síntesis gráfica.
  - Capacidad de condensar 13 páginas de informe en 12-15 diapositivas sin perder la estructura argumental.
  - Oratoria y estructuración de presentaciones técnicas bajo presión de tiempo.
  - Empatía pedagógica: capacidad de anticipar qué preguntará el docente y preparar al equipo.
* **Tareas entregables concretas:**
  1. Elaboración del **mazo de diapositivas ejecutivas** (12-15 láminas), con diseño limpio y corporativo.
  2. **Adaptación visual de los artefactos** del informe para exposición: diagramas de P5 (simplificados para pantalla), tablas de P2-P3 (destacando hallazgos clave) y gráficos financieros de P4 (con barras de sensibilidad).
  3. Redacción del **libreto de defensa oral:** distribución de minutos por integrante (ej. ~3 min/persona para ~24 min total), orden de intervención y puntos de transición.
  4. Creación de una **matriz de «Preguntas Difíciles»** con al menos 15 preguntas que el docente podría formular, con sus respuestas técnicas preparadas y asignadas al integrante que debe responder.
  5. Organización y moderación del **ensayo general** de exposición (Día 5), con cronómetro y retroalimentación.
* **Nivel de uso de IA previsto y registro A-6:**
  - **Nivel 1** para sugerencias de layout y estructura visual de diapositivas.
  - **Nivel 0** en los argumentos de defensa, el libreto y la matriz de preguntas difíciles (el grupo debe poder reconstruir el razonamiento oralmente).
  - **Evidencia:** Historial de versiones de la presentación en Google Slides/PowerPoint.

---

### Persona 8 — Auditor de Calidad, Verificación de Vigencia y Formulario A-6

* **Rol funcional:** QA Auditor, Legal Fact-Checker & Compliance Officer del equipo.
* **Características / habilidades ideales:**
  - Mentalidad de auditor legal: escrupulosidad extrema, tolerancia cero a datos sin respaldo.
  - Capacidad de verificar el estado de vigencia de leyes y reglamentos en fuentes oficiales (BCN, Diario Oficial, EUR-Lex, ISO.org).
  - Conocimiento de las normas de citación y referenciación (APA 7 o norma del curso).
  - Dominio de las reglas del Comunicado 9 para actuar como **última línea de defensa** antes de la entrega.
* **Tareas entregables concretas:**
  1. **Verificación documentada del estado de vigencia de cada norma citada** (entregable obligatorio de la ficha TI-12): tabla con norma, estado (vigente / con vacatio legis / en tramitación / derogada), fuente oficial (URL), y fecha de verificación.
  2. **Fact-checking del 100% de las fuentes:** verificar que cada URL citada esté viva, que cada cifra tenga respaldo oficial (2025/2026), y que ninguna fuente caiga en la categoría de «no admisible» (comparativas de proveedor sobre su propia categoría, contenido de agregadores sin fuente original).
  3. **Auditoría preventiva del Comunicado 9:** barrido línea por línea del informe buscando:
     - Marcadores residuales de IA: `[cite: n]`, `[INSERTAR DIAGRAMA]`, `Anexo ??`, `borrador`, `pendiente de validar`, `por indicación del usuario`, `Fuente: elaboración propia` sin análisis.
     - Figuras huérfanas: diagramas o tablas que aparezcan sin ser citados, explicados ni analizados en el texto.
     - Cifras no rastreables: números sin fórmula mostrada, sin fuente, o que contradigan otro capítulo.
     - Rupturas de ficción: menciones a «curso», «docente», «tarea», «propuesta académica» en un contexto que simula licitación.
     - Contradicciones cruzadas: que P2 diga que la Ley 21.719 entra en vigencia en una fecha y P5 asuma otra distinta; que P4 costee una herramienta que P3 no analizó.
  4. **Consolidación del Formulario A-6 (Anexo de Declaración de IA):**
     - Recopilar la declaración **individual** de cada uno de los 8 integrantes.
     - Verificar que el nivel declarado por sección sea coherente con lo observado en el texto.
     - Compilar prompts, enlaces a conversaciones y evidencia trazable de quienes declaren niveles 2 o 3.
     - Asegurar que el formulario incluya todas las secciones del informe (no un nivel global único) y que esté firmado por los 8 integrantes.
  5. **Verificación de límites formales:** conteo de páginas (10-15), nomenclatura de archivos, asunto del correo, y que todos los anexos obligatorios estén presentes.
* **Nivel de uso de IA previsto y registro A-6:**
  - **Nivel 0 estricto.** El auditor actúa como la barrera de control humano imparcial que valida la probidad del trabajo completo. Cualquier uso de IA en esta función comprometería la credibilidad de toda la declaración.

---

## 2. Cronograma de 6 Días (Checkpoints y Mitigación de Riesgos)

El plan abarca desde el **Día 1 (miércoles 16 de septiembre)** hasta el **Día 6 (lunes 21 de septiembre de 2026)**, fecha oficial de entrega de la asignatura. Cada día incluye un hito, entregables por rol, revisión cruzada obligatoria y alertas del Comunicado 9.

> [!WARNING]
> **Contingencia Fiestas Patrias (Viernes 18 y Sábado 19):** El **viernes 18** (Independencia Nacional) y el **sábado 19 de septiembre** (Glorias del Ejército) son feriados nacionales irrenunciables en Chile. El cronograma aplica una rigurosa estrategia de ***front-loading***: se concentra la toma de decisiones y la coordinación sincrónica en los Días 1 y 2 (miércoles 16 y jueves 17 pre-feriado), se reservan los Días 3 y 4 (viernes 18 y sábado 19) para avance asíncrono individual sin reuniones obligatorias, se programa la sesión sincrónica de ensamblaje, auditoría y ensayo oral para el Día 5 (domingo 20), y se ejecuta el despacho formal el Día 6 (lunes 21).

```
[Mié 16] Día 1 · Arranque, fuentes verificadas y kick-off sincrónico
   │
[Jue 17] Día 2 · CONGELAMIENTO BASELINE + Borradores y modelo económico preliminar
   │
[Vie 18] Día 3 · 🇨🇱 FERIADO (Fiestas Patrias) — Redacción individual asíncrona (P2, P3, P4, P5)
   │
[Sáb 19] Día 4 · 🇨🇱 FERIADO (Glorias del Ejército) — Cuestionario, comparativas y diagramas
   │
[Dom 20] Día 5 · Ensamblaje V1 + Auditoría C9 + Ensayo oral solidario (sincrónico)
   │
[Lun 21] Día 6 · Día de Entrega: Firma A-6, exportación final y despacho oficial
```

### Día 1 — Miércoles 16/09 · «Alineación, Alcance y Fuentes Primarias»

| Aspecto | Detalle |
| :--- | :--- |
| **Hito** | Índice oficial aprobado, fuentes primarias identificadas, supuestos de volumetría del caso acordados. Bitácora A-6 habilitada. |
| **P1** | Distribuye plantilla con índice, presupuesto de páginas, y estilo de citación. Coordina la reunión de arranque (kick-off). |
| **P2** | Identifica y descarga los textos oficiales de la Ley 21.719, Ley 21.663, Ley 21.180, Ley 19.628 desde BCN. Propone las 2 normativas chilenas adicionales. Inicia investigación de dictámenes de la Dirección del Trabajo sobre monitoreo GPS de conductores (línea de aporte propio). |
| **P3** | Identifica fuentes primarias del RGPD (EUR-Lex), NIS2, Reg. IA, Reg. Ciberresiliencia, ISO 27001, NIST CSF 2.0. Propone las 2 normativas/estándares internacionales adicionales. Comienza lista de herramientas GRC (≥8). |
| **P4** | Ancla los supuestos al Caso 10 Curimón (ver Sección 3.1 — Datos del Caso). Propone la estructura de la matriz de obligaciones. |
| **P5** | Revisa las Bases Técnicas del Caso 10 (Cap. 12 Marco Normativo). Identifica los flujos de datos personales (conductores propios, conductores subcontratados, clientes, localización GPS) y las fronteras de cumplimiento responsable/encargado. |
| **P6** | Estudia la ficha TI-12 y las Bases Técnicas del Caso 10. Comienza la planificación de la distribución de las 30 preguntas por subtema. |
| **P7** | Define la estructura de la presentación (12-15 láminas) y el estilo visual. Prepara la plantilla de diapositivas. |
| **P8** | Crea el repositorio de evidencias: carpeta compartida para capturas de fuentes, planilla de verificación de vigencia, plantilla del Formulario A-6, y **bitácora continua de prompts** (ver Sección 4.4). |
| **Revisión cruzada** | **P1 y P8** revisan la lista de fuentes propuesta por P2 y P3 (¿son fuentes preferentes o admisibles? ¿alguna es inadmisible?). **P4 y P5** contrastan los supuestos de volumetría contra las Bases Técnicas del Caso 10. |
| **🚩 Alertas C9** | No iniciar redacción de texto antes de tener fuentes primarias verificadas. No incluir herramientas GRC que solo aparezcan en blogs de comparación sin documentación oficial propia. |

---

### Día 2 — Jueves 17/09 · «Congelamiento de Baseline, Borradores y Modelo Económico Preliminar»

> **Última sesión sincrónica antes del feriado patrio.** Todo lo que requiera coordinación presencial o decisión conjunta debe resolverse hoy.

| Aspecto | Detalle |
| :--- | :--- |
| **Hito** | **Firma del Acta de Congelamiento de Datos** (Baseline numérico y normativo). Primeros borradores de análisis entregados. Cada integrante sale con su asignación clara para los 2 días de trabajo asíncrono. |
| **P1** | Modera la sesión de congelamiento. Documenta los datos base en el **Acta de Baseline** (ver Sección 3 — Matriz de Coherencia). Distribuye las asignaciones individuales para Días 3-4 (feriado asíncrono). |
| **P2** | Entrega borrador del análisis de la Ley 21.719 (artículos clave, fechas, sanciones). Confirma las fechas de vigencia oficiales. Reporta hallazgos de la investigación sobre dictámenes de la DT (aporte propio). |
| **P3** | Entrega borrador del análisis del RGPD y NIS2 (comparativa inicial Chile-UE). Define criterios de evaluación para las herramientas GRC. |
| **P4** | Entrega primera versión de la **matriz de obligaciones** con al menos 10 obligaciones mapeadas. Comienza a levantar precios de herramientas GRC y costos de roles usando el Formulario E-26 como referencia de tarifas (ver Sección 3.2). |
| **P5** | Entrega primer borrador del **diagrama de arquitectura de cumplimiento** (flujos de datos, puntos de control, frontera responsable/encargado). |
| **P6** | Redacta las primeras **10 preguntas básicas** con respuestas y justificaciones. |
| **P7** | Comienza a maquetar las láminas de contexto y marco conceptual con los insumos disponibles de P2. |
| **P8** | Primera ronda de verificación: confirma el estado de vigencia de las leyes y normas citadas por P2 y P3 (¿están vigentes, en vacatio legis, o en tramitación a septiembre 2026?). |
| **Revisión cruzada** | **P4 ↔ P5:** La arquitectura de cumplimiento de P5 no puede incluir componentes (herramientas, roles) que P4 no haya contemplado en la estructura de costos. **P2 ↔ P3:** Que las fechas de vigencia y la terminología sean consistentes entre el marco chileno y el internacional. |
| **🚩 Alertas C9** | No comenzar a redactar capítulos sin haber congelado: (a) las fechas de vigencia de cada norma, (b) la moneda y tasa de conversión, (c) los supuestos del caso. Las cifras desalineadas entre capítulos son señal directa de texto generado por separado sin integración humana. |

> [!WARNING]
> **Acta de Congelamiento (Día 2, cierre):** A partir de este momento, ningún integrante puede modificar unilateralmente los datos base (fechas de vigencia, supuestos del caso, moneda, herramientas seleccionadas) sin autorización formal de P1 y P8. Toda modificación posterior se documenta como «enmienda al baseline» con justificación.

---

### Día 3 — Viernes 18/09 · 🇨🇱 FERIADO (Fiestas Patrias) · «Redacción Asíncrona Individual — Investigación Profunda»

> **Feriado nacional irrenunciable: No hay reuniones sincrónicas.** Cada integrante trabaja a su ritmo de forma asíncrona sobre su asignación. Se comunican hallazgos y dudas por el canal de mensajería (WhatsApp/Discord). Standup asíncrono breve a las 20:00 hrs.

| Aspecto | Detalle |
| :--- | :--- |
| **Hito** | Capítulos de análisis normativo en borrador avanzado, modelo de costos con fuentes verificadas en progreso, cuestionario al 50%. |
| **P1** | Revisa los borradores de P2 y P3 por coherencia terminológica y narrativa. Detecta redundancias o vacíos. Envía observaciones por el canal asíncrono. |
| **P2** | Completa el análisis de la Ley 21.663 y los organismos chilenos. Integra las 2 normativas adicionales con su justificación. |
| **P3** | Avanza en el **cuadro comparativo de herramientas GRC** (≥6 analizadas + 2 de aporte propio). Completa el análisis de normas certificables con costos de certificación. |
| **P4** | Avanza en el **modelo de costos del cumplimiento** con estimación a 5 años. Levanta precios de herramientas GRC y costos de roles. Toda cifra con metadatos completos (producto, moneda, región, fecha, régimen). |
| **P5** | Avanza en los diagramas (arquitectura de cumplimiento + Privacy by Design) con texto explicativo integrado. |
| **P6** | Redacta las preguntas **11 a 20 (intermedias)** con respuestas y justificaciones. |
| **P7** | Integra los artefactos gráficos preliminares de P5 en las diapositivas. |
| **P8** | Verifica fuentes de P4 (precios con URL oficial y fecha). Inicia barrido de marcadores residuales en los borradores disponibles. |
| **Revisión cruzada** | Asíncrona: cada integrante revisa si su trabajo es coherente con el baseline congelado. P8 envía observaciones por escrito. |
| **🚩 Alertas C9** | Uso de «Fuente: elaboración propia» como leyenda de una figura sin que el texto la cite, la explique ni derive conclusiones de ella. Presencia de cifras que no se deriven de un cálculo mostrado o de una fuente con fecha. |

---

### Día 4 — Sábado 19/09 · 🇨🇱 FERIADO (Glorias del Ejército) · «Cierre de Comparativas, Diagramas y Cuestionario»

> **Feriado nacional: No hay reuniones sincrónicas.** Todos los artefactos de contenido deben quedar subidos al repositorio al cierre de este día para permitir el ensamblaje conjunto del Día 5.

| Aspecto | Detalle |
| :--- | :--- |
| **Hito** | Cuadro comparativo GRC cerrado, modelo de costos completo con sensibilidad, diagramas finales entregados, cuestionario de 30 preguntas terminado. |
| **P2 y P3** | Cierran y pulen sus capítulos respectivos. Entregan texto final a P1 para ensamblaje. |
| **P4** | Entrega el **modelo de costos** terminado con análisis de sensibilidad sobre las 2 variables de mayor impacto. Entrega la **matriz de obligaciones** completa. |
| **P5** | Entrega los **diagramas finales** (arquitectura de cumplimiento + Privacy by Design + mapa de transferencias internacionales) con texto explicativo paso a paso. |
| **P6** | Entrega las preguntas **21 a 30 (avanzadas)** con justificaciones. Completa el **índice temático cruzado** (pregunta → sección → subtema). |
| **P7** | Completa el borrador de la presentación ejecutiva (12-15 láminas). Comienza el libreto de defensa oral. |
| **P8** | Audita a P4: fact-checking de cifras finales. Audita a P5: que ningún diagrama sea una «figura huérfana». |
| **Revisión cruzada** | Asíncrona: **P8 → P4** (fact-checking de cifras), **P3 → P2** (coherencia Chile-UE). Todos entregan su capítulo final al repositorio compartido antes de las 22:00 hrs. |
| **🚩 Alertas C9** | Contradicciones cruzadas entre capítulos (ej. P2 fecha la vigencia de la Ley 21.719 distinto a lo que P4 asume en su modelo de costos). Cifras sin fuente con fecha. |

---

### Día 5 — Domingo 20/09 · «Ensamblaje V1, Auditoría Anti-C9 y Ensayo Oral Solidario»

> **Día clave: Sesión sincrónica obligatoria del equipo.** Ensamblaje del documento completo, auditoría integral anti-Comunicado 9 y ensayo oral general.

| Aspecto | Detalle |
| :--- | :--- |
| **Hito** | Documento V1 ensamblado y auditado → V2 corregida. Presentación final lista. Formulario A-6 completado. Ensayo oral realizado. |
| **P1** | Redacta la **Introducción** (con párrafo de Aporte Propio) y las **Conclusiones y Recomendaciones** (Nivel 0 IA). Ensambla todos los capítulos en el documento maestro unificado. Verifica el conteo de páginas (10-15). |
| **P1 y P8** | **Auditoría cruzada total:** revisión línea por línea del informe V1 contra la checklist del Comunicado 9. Generación de la lista definitiva de correcciones. |
| **P2, P3, P4, P5** | Incorporan las correcciones señaladas por la auditoría. Resuelven toda inconsistencia detectada. |
| **P6** | Ajusta preguntas cuyas referencias cambiaron tras la edición del documento. Entrega cuestionario final con índice temático actualizado a las páginas del V2. |
| **P7** | Entrega la **presentación ejecutiva final** (PPT/PDF). Entrega el **libreto de defensa oral** con distribución de minutos y la **matriz de preguntas difíciles** (≥15 preguntas anticipadas con respuestas asignadas). Verifica que los datos en las diapositivas coincidan exactamente con el informe V2. |
| **P8** | Completa y consolida el **Formulario A-6**: recopila las 8 declaraciones individuales, verifica niveles por sección, adjunta evidencia trazable de la bitácora de prompts. Verifica que el formulario esté firmado por los 8 integrantes. |
| **Todo el equipo** | **Ensayo general de exposición oral** con cronómetro. P7 modera. Cada integrante presenta su parte y responde preguntas del resto del grupo. |
| **Revisión cruzada** | **P6 → Informe V2:** Que cada pregunta del cuestionario apunte a contenido existente. **P7 interroga al equipo:** Simulación de preguntas del docente a cada integrante sobre cualquier parte del trabajo. |
| **🚩 Alertas C9** | **Barrido final de marcadores:** `[cite: n]`, `[INSERTAR...]`, `Anexo ??`, `borrador`, `pendiente de validar`, `Fuente: elaboración propia` sin análisis. Cualquier integrante que no pueda explicar oralmente una cifra o un diagrama debe estudiarlo esa misma noche. |

> [!CAUTION]
> **Regla de Oro del Día 5:** Conforme al Comunicado 9, el docente puede interrogar a cualquier miembro sobre cualquier tabla, diagrama o cifra. **Ningún integrante se desconecta** hasta que los 8 hayan demostrado capacidad de explicar: (a) las 3 leyes chilenas clave, (b) la lógica de la matriz de obligaciones, (c) la procedencia de al menos 2 cifras del modelo de costos, y (d) el significado de cada componente del diagrama de arquitectura de cumplimiento.

---

### Día 6 — Lunes 21/09 · «Día Oficial de Entrega: Firma, Exportación y Despacho Formal»

| Aspecto | Detalle |
| :--- | :--- |
| **Hito** | Documentos finales exportados, nomenclatura verificada, correo oficial enviado, impresión entregada en la sesión fijada. |
| **P1** | Incorpora las últimas correcciones menores del ensayo. Exporta el informe final a **PDF de alta calidad**. Verifica nomenclatura de archivos: `10 - AUDIT - TI-12`. |
| **P8** | Verificación final del checklist de entrega: (a) informe PDF, (b) presentación PPT/PDF, (c) cuestionario de 30 preguntas, (d) Formulario A-6 firmado. Verifica que el conteo de páginas esté en rango [10, 15]. |
| **P7** | Exportación final de la presentación (PPT y PDF). Última verificación de coherencia diapositivas ↔ informe final. |
| **P1** | Envío del correo electrónico oficial antes del plazo límite con asunto: `[ICI544] - 10 - AUDIT - TI-12`. Coordina la entrega impresa en la sesión fijada por el calendario del curso. |
| **Revisión cruzada** | **P1 y P8** realizan la revisión final de despacho: nomenclatura de archivos, asunto del correo, firmas en el A-6, completitud de anexos. |
| **🚩 Alertas C9** | Entrega sin Formulario A-6 firmado = entrega incompleta = no se recibe conforme. Discrepancia entre el nombre del archivo y el asunto del correo. Envío sin adjuntar la presentación. |

---

## 3. Matriz de Coherencia Cruzada (Control de Calidad)

Para cumplir estrictamente el Comunicado 9 y erradicar contradicciones entre capítulos, los siguientes datos se declaran **congelados al cierre del Día 2**. Ningún integrante puede modificarlos sin autorización formal de P1 y P8.

### 3.1 Datos del Caso 10 — Transportes Curimón S.A.

Los siguientes datos provienen directamente de las [Bases Técnicas del Caso 10](file:///home/carlosa/Documentos/Universidad/Actual/FEP/Proyecto/Informe/repo/texto/FEP03_10_26_Caso_10_Transporte_de_Carga_Bases_Tecnicas_del_Caso.md) y constituyen la volumetría oficial del caso. **No son estimaciones**: son cifras del documento fuente.

| Parámetro del Caso | Dato Verificado | Fuente (línea del documento) | Implicancia para TI-12 |
| :--- | :--- | :---: | :--- |
| Flota total gestionada | **374 camiones** (60,4% subcontratados) | L29, L131 | Cada camión transmite localización GPS = dato personal bajo Ley 21.719. |
| Conductores totales | **454** (196 propios + 258 subcontratados) | L29, L164 | Los 258 conductores externos NO son trabajadores de la empresa. El tratamiento de sus datos requiere base de licitud y consentimiento diferenciado. |
| Transportistas subcontratados | **148 empresas** externas | L708 | Relación responsable/encargado del tratamiento: Curimón es responsable, cada transportista tiene conductores cuyos datos se tratan. |
| Clientes | **84 empresas** cliente | L889 | Datos de contacto, direcciones de entrega, firmas digitales de recepción. |
| Operación geográfica | Antofagasta a Puerto Montt + **cruce fronterizo a Mendoza (Argentina)** | L29 | Transferencia internacional de datos personales: requiere evaluación bajo Ley 21.719 y potencialmente marco argentino (Ley 25.326). |
| Cifrado obligatorio (RT-11.10) | Cifrado a nivel de campo para datos personales de los 258 conductores externos, localización asociada a persona identificable, y tarifas de los 148 transportistas. | L882 | Requisito técnico explícito en las Bases que debe reflejarse en la arquitectura de cumplimiento de P5. |
| Retención de datos | Jornada de conducción: 5 años. Telemetría: 2 años en línea. Siniestros: 10 años. | L869 | Implicancias directas para el registro de actividades de tratamiento y la política de retención/eliminación. |
| Protección de datos personales | Ley N° 21.719, con atención a conductores que no son trabajadores de la compañía y a la información de localización. | L718 | **Mención explícita en las Bases Técnicas:** «La posición de un camión de un tercero y las horas de un conductor externo son datos cuyo tratamiento requiere base y consentimiento.» |
| Duración del contrato | 56 meses: implementación en 2 etapas + 36 meses de operación | L33 | Base temporal para el TCO a 5 años de P4. |

### 3.2 Referencia de Tarifas — Formulario E-26 (Bases Administrativas)

Para el costeo de roles de cumplimiento, P4 debe usar como referencia los rangos del [Formulario E-26](file:///home/carlosa/Documentos/Universidad/Actual/FEP/Proyecto/Informe/repo/texto/FEP01_26_Bases_Administrativas_TFEP_01_2026_3.md#L2458-L2488) de las Bases Administrativas del curso (FEP01.26). Esto garantiza coherencia entre el trabajo de investigación y la propuesta de licitación.

| Rol requerido en TI-12 | Perfil homólogo en E-26 | Costo (UF/h) | Tarifa (UF/h) | Nota |
| :--- | :--- | :---: | :---: | :--- |
| **CISO / Oficial de Seguridad** | Encargado de Seguridad TI | 0,8–1,4 | 1,5–2,5 | Perfil directo del E-26. |
| **DPO / Delegado de Protección de Datos** | Jefe de Proyecto (proxy) | 0,8–2,1 | 1,5–3,0 | El E-26 no tiene perfil DPO. Se usa Jefe de Proyecto como proxy más cercano. Declarar el criterio en la memoria de cálculo. |
| **Analista de Cumplimiento** | Analista QA Experto | 0,5–0,7 | 0,8–1,0 | Perfil de control de calidad como proxy para control de cumplimiento. |
| **Asesor Legal Externo** | *Perfil no listado en E-26* | Declarar | Declarar | El E-26 permite perfiles adicionales «no contenidos en la lista» con rangos coherentes. P4 debe declarar fuente y justificación del rango usado. |

> [!NOTE]
> El Formulario E-26 indica: «Pueden existir otros roles no contenidos en la lista. Deberán declararse en la hoja de tarifas del modelo financiero y respetar rangos coherentes con los aquí indicados.» El Asesor Legal Externo cae en esta categoría.

### 3.3 Baseline congelado (Día 2)

```
       ┌──────────────────────────────────────────────────────────────────────┐
       │               BASELINE NORMATIVO-ECONÓMICO (DÍA 2)                  │
       │                                                                     │
       │  Caso: Transportes Curimón S.A. (Caso 10)                          │
       │  Flota: 374 camiones · 454 conductores (258 externos)              │
       │  Clientes: 84 · Transportistas: 148                                │
       │  Normas base: Ley 21.719 + Ley 21.663 + RGPD (referencia)         │
       │  Moneda: UF y CLP (con conversión a USD si aplica)                 │
       │  Contrato: 56 meses (implementación + 36 meses operación)          │
       │  Fecha de consulta de precios: septiembre 2026                      │
       └───────────────┬────────────────────────────────┬─────────────────────┘
                       │                                │
            ┌──────────▼──────────┐          ┌──────────▼──────────┐
            │ Persona 5           │          │ Persona 4           │
            │ (Arquitectura de    │          │ (Impacto Económico) │
            │  Cumplimiento)      │          │                     │
            ├─────────────────────┤          ├─────────────────────┤
            │ • Flujo de datos    │◄────────►│ • Costo DPO (E-26)  │
            │   personales        │          │ • Licencia GRC      │
            │ • Puntos de control │          │ • Auditoría ISO     │
            │ • Frontera resp/enc │          │ • Seguro ciberriesgo│
            │ • Región cloud      │          │ • Multas Ley 21.719 │
            │ • Cifrado RT-11.10  │          │ • TCO 56 meses      │
            └─────────────────────┘          └─────────────────────┘
                       ▲                                ▲
                       └────────────┬───────────────────┘
                                    │ Valida normativas
                                    │ y herramientas
                       ┌────────────┴────────────┐
                       │ Personas 2 & 3          │
                       │ (Normativa + GRC)        │
                       ├─────────────────────────┤
                       │ • Fechas de vigencia    │
                       │ • Obligaciones legales  │
                       │ • Herramientas evaluadas│
                       │ • Costos de licencia    │
                       └─────────────────────────┘
```

### 3.4 Tabla de variables críticas congeladas

| Variable / Parámetro Crítico | Dueño del Dato | Dato Congelado (Baseline Oficial) | Dónde Impacta | Regla de Consistencia |
| :--- | :---: | :--- | :--- | :--- |
| **Fechas de vigencia de normas chilenas** | **P2** | Ley 21.719: *[verificar fecha exacta en BCN — promulgada 2024, vacatio legis de 24 meses]*. Ley 21.663: publicada en Diario Oficial el 8 de abril de 2024. Ley 21.180: *[verificar]*. Estado de reglamentos: *[verificar si publicados o en tramitación a septiembre 2026]*. | • Análisis P2 (marco chileno)  • Matriz de obligaciones (P4, columna «plazo»)  • Diagrama PbD (P5, hitos de cumplimiento)  • Cuestionario (P6)  • Diapositivas (P7) | Prohibido que P4 calcule costos de cumplimiento asumiendo una fecha de entrada en vigencia distinta a la documentada por P2. |
| **Fechas de aplicación de normativa internacional** | **P3** | RGPD: vigente desde 2018. NIS2: *[verificar fecha de transposición]*. Reg. IA: *[verificar fecha escalonada por categoría de riesgo]*. Reg. Ciberresiliencia: *[verificar]*. | • Análisis P3 (marco internacional)  • Comparativa Chile-UE (P2+P3)  • Cuestionario (P6) | Las preguntas del cuestionario de P6 sobre plazos deben usar exactamente las fechas congeladas por P3. |
| **Volumetría del Caso 10** | **P4 + P5** | 374 camiones, 454 conductores (196 propios + 258 subcontratados), 148 transportistas, 84 clientes, 96.000 viajes/año, cruce fronterizo a Mendoza. Contrato de 56 meses. | • Matriz de obligaciones (P4)  • Diagrama de arquitectura (P5)  • Vínculo con propuesta (P5)  • Análisis de transferencias internacionales (P5) | La arquitectura de P5 debe reflejar exactamente los mismos actores y flujos de datos que P4 usa para dimensionar los costos de cumplimiento. |
| **Moneda y tasa de conversión** | **P4** | Moneda base: **UF y CLP**. Conversión: 1 UF = *[valor congelado, fuente SII o CMF, fecha]* CLP. 1 USD = *[valor congelado, fuente Banco Central, fecha]* CLP. Tarifas de roles: Formulario E-26 en UF/hora. | • Tablas de costos de herramientas GRC (P3+P4)  • Planilla de impacto económico (P4)  • Costos de certificación (P3) | No se admiten tablas que mezclen CLP, USD y EUR sin factor de conversión explícito y fecha de fijación. |
| **Herramientas GRC seleccionadas** | **P3** | Lista definitiva de ≥8 herramientas (6 base + 2 aporte propio) con nombre exacto, versión (si aplica) y URL de documentación oficial. | • Cuadro comparativo (P2+P3)  • Diagrama de arquitectura (P5, si integra herramienta GRC)  • Modelo de costos (P4, licencias)  • Cuestionario (P6)  • Diapositivas (P7) | P5 solo puede dibujar herramientas que P3 haya analizado. P4 solo puede cotizar herramientas que P3 haya seleccionado. P6 solo puede preguntar sobre herramientas que aparezcan en el informe. |
| **Costos de roles de cumplimiento** | **P4** | DPO: rango de Jefe de Proyecto E-26 (0,8–2,1 UF/h costo, 1,5–3,0 UF/h tarifa). CISO: Encargado de Seguridad TI E-26 (0,8–1,4 UF/h costo, 1,5–2,5 UF/h tarifa). Analista de Cumplimiento: Analista QA Experto E-26 (0,5–0,7 UF/h costo). Asesor Legal Externo: perfil declarado con rango justificado. | • Matriz de obligaciones (P4, columna «costo»)  • Flujo de caja (P4)  • Vínculo con propuesta (P5) | Todas las tarifas deben ser coherentes con los rangos del Formulario E-26. El proxy utilizado debe declararse en la memoria de cálculo. |

---

## 4. Protocolo de Blindaje contra el Comunicado 9

### 4.1 Standup diario asíncrono (20:00 hrs)

Cada persona reporta en **máximo 3 líneas** por un canal compartido (WhatsApp, Discord o Slack):

1. **Qué entregué hoy** (artefacto concreto).
2. **Qué inconsistencia detecté** en el trabajo de otro integrante (o «ninguna detectada»).
3. **Qué completaré mañana** y si necesito un insumo de alguien.

### 4.2 Checklist Anti-Comunicado 9 (para uso de P8)

Antes de dar el visto bueno final, P8 debe verificar **cada uno** de estos puntos:

- [ ] ¿Cada diagrama y tabla está citado, explicado y analizado en el texto? (No hay figuras huérfanas.)
- [ ] ¿Cada cifra de costo tiene: producto, moneda, región, fecha de consulta y tipo de precio?
- [ ] ¿Las fechas de vigencia de las leyes son consistentes en todos los capítulos?
- [ ] ¿La herramienta GRC recomendada en las conclusiones fue analizada en la comparativa?
- [ ] ¿El diagrama de arquitectura refleja exactamente los componentes costeados?
- [ ] ¿Las preguntas del cuestionario apuntan a contenido existente en el informe?
- [ ] ¿Se eliminaron todos los marcadores residuales de IA?
- [ ] ¿No hay menciones a «curso», «tarea», «profesor» en contexto de licitación?
- [ ] ¿El párrafo de aporte propio distingue claramente qué viene de la ficha y qué es del grupo?
- [ ] ¿El Formulario A-6 tiene las 8 firmas y los niveles por sección (no un nivel global)?
- [ ] ¿El informe tiene entre 10 y 15 páginas (sin contar anexos)?
- [ ] ¿El nombre del archivo y el asunto del correo siguen la nomenclatura exigida?
- [ ] ¿Las cifras del modelo de costos se derivan de la volumetría del Caso 10 (374 camiones, 454 conductores)?
- [ ] ¿Las tarifas de roles son coherentes con los rangos del Formulario E-26?

### 4.3 Defensa oral solidaria

Conforme al Comunicado 9, el docente puede interrogar a **cualquier** miembro sobre **cualquier** parte del trabajo. El Día 5, durante el ensayo general, cada integrante debe demostrar capacidad de explicar:

1. Los **3 pilares normativos chilenos** (Ley 21.719, Ley 21.663, Ley 21.180) y su estado de vigencia.
2. La **diferencia entre responsable y encargado del tratamiento** y por qué importa para Curimón (empresa que opera con 258 conductores que no son sus trabajadores).
3. La **lógica de la matriz de obligaciones** (cómo se pasa de una obligación legal a una partida de costo).
4. La **procedencia de al menos 2 cifras** del modelo de costos (fuente, fecha, moneda, rango E-26 si aplica).
5. El **significado de cada componente** del diagrama de arquitectura de cumplimiento y su relación con los flujos de datos del Caso 10.
6. Por qué el grupo **recomienda** la estrategia de cumplimiento que recomienda (y qué alternativas descartó y por qué).

### 4.4 Bitácora continua de prompts para el Formulario A-6

> [!IMPORTANT]
> P8 habilita este archivo compartido el Día 1. Todo integrante que use herramientas de IA (Nivel 1, 2 o 3) debe registrar cada interacción **en el momento de uso**, no al final. Esto elimina la deuda de registro que se acumularía para el Día 5.

Cada entrada de la bitácora sigue este formato:

```
### Registro de Interacción con IA — Formulario A-6
* **Fecha y Hora:** [DD-MM-AAAA HH:MM]
* **Integrante:** Persona [N]
* **Sección del Informe:** [Nombre de la sección]
* **Herramienta y Versión:** [Ej. Claude 4.5 Sonnet / ChatGPT Plus (GPT-4o)]
* **Nivel de Uso:** [0, 1, 2 o 3]
* **Prompt Empleado:**
  > "[Transcripción exacta del prompt]"
* **Uso del Resultado:** [Cómo se usó: esquema, traducción, revisión, etc. Qué se verificó manualmente.]
* **Enlace de Evidencia:** [URL al chat o captura en carpeta compartida]
```

### 4.5 Líneas de investigación para el Aporte Propio (Sección 4 de las indicaciones)

> [!WARNING]
> Las siguientes líneas son **direcciones de investigación**, no afirmaciones verificadas. Cada una requiere confirmación con fuentes primarias oficiales antes de incluirse en el informe. Si la investigación no confirma la premisa, se documenta la búsqueda realizada y se descarta con transparencia.

**Línea de investigación 1 — Tensión entre monitoreo GPS de conductores y protección de datos personales:**

- *Premisa:* El monitoreo satelital continuo de la flota (exigencia de seguridad en transporte) colisiona con el derecho a la intimidad del conductor, especialmente de los 258 conductores subcontratados.
- *Tarea de P2:* Investigar si existen dictámenes específicos de la **Dirección del Trabajo** de Chile sobre control de localización fuera de la jornada laboral. Contrastar con los principios de proporcionalidad y minimización de la Ley 21.719.
- *Condición para inclusión:* Solo se incluye si P2 encuentra respaldo documental verificable (dictámenes, jurisprudencia judicial o pronunciamientos de la Agencia PDP). Si no existe, se declara el vacío normativo como hallazgo.

**Línea de investigación 2 — Gobernanza de algoritmos de IA en transporte bajo ISO/IEC 42001 y Ley 21.719:**

- *Premisa:* Los sistemas modernos de transporte pueden usar algoritmos para asignar viajes, optimizar rutas o evaluar la conducción. Si el sistema del Caso 10 incorpora funcionalidades algorítmicas, podrían existir obligaciones respecto a decisiones automatizadas.
- *Tarea de P2 y P5:* Verificar si la Ley 21.719 contiene disposiciones sobre decisiones automatizadas (análogo al Art. 22 del RGPD). P5 debe identificar qué funcionalidades del Caso 10 involucran procesamiento algorítmico.
- *Condición para inclusión:* Solo si se confirma el articulado relevante en el texto legal y si el Caso 10 efectivamente contempla funcionalidades algorítmicas en sus requisitos.

---

## 5. Resumen de Entregables Finales y Responsables

| Entregable | Responsable principal | Revisores | Formato |
| :--- | :---: | :---: | :--- |
| Informe escrito (10-15 págs.) | P1 (ensamblaje) | P8 (auditoría), todo el equipo | PDF, nomenclatura `10 - AUDIT - TI-12` |
| Cuadro comparativo ≥6 herramientas GRC | P3 (elaboración) | P2, P8 | Tabla dentro del informe |
| Matriz de obligaciones aplicables al caso | P4 (elaboración) | P2, P5, P8 | Tabla dentro del informe |
| Modelo de impacto económico (TCO 56 meses) | P4 (elaboración) | P8 (fact-check) | Tabla + análisis de sensibilidad |
| Verificación de vigencia de normas | P8 (elaboración) | P2, P3 | Tabla dentro del informe |
| Diagramas de arquitectura de cumplimiento | P5 (elaboración) | P1, P4 | Figuras integradas en el informe |
| Cuestionario de 30 preguntas | P6 (elaboración) | P1 (coherencia), P8 (formato) | Documento anexo |
| Presentación ejecutiva | P7 (elaboración) | P1, todo el equipo | PPT/PDF, 12-15 láminas |
| Libreto de defensa oral | P7 (elaboración) | Todo el equipo | Documento interno |
| Formulario A-6 (Declaración de IA) | P8 (consolidación) | P1 (revisión final) | Formulario anexo, firmado ×8 |

---

> [!NOTE]
> **Sobre el «Vínculo con la propuesta técnico-económica»** (aclaración de la Sección 8 de las indicaciones): El grupo debe relacionar las conclusiones del trabajo de investigación con el **Caso 10 — Transportes Curimón S.A.** El tema TI-12 es el que más directamente convierte exigencias legales en partidas presupuestarias: sin este análisis, las propuestas subestiman roles de cumplimiento (DPO, CISO), auditorías de certificación y capacidades de respuesta a incidentes. La mención explícita de la Ley 21.719 en las Bases Técnicas del caso (L718) y el requisito de cifrado a nivel de campo (RT-11.10, L882) hacen que la vinculación sea no solo conveniente, sino **exigida por las propias bases del mandante**.

