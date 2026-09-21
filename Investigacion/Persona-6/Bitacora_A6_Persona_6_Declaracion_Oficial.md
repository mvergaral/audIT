# Declaración Oficial de Uso de Inteligencia Artificial (Formulario A-6)
## Persona 6: Diseñador Pedagógico del Cuestionario de Evaluación (30 Preguntas)

**Asignatura:** Taller de Formulación de Proyectos Informáticos (ICI-5444) · Escuela de Informática, PUCV  
**Empresa Asignada:** AudIT (Empresa 10)  
**Tema de Investigación:** TI-12 · *Cumplimiento normativo en proyectos TIC: Ley 21.719, Ley 21.663 (ANCI) y marco internacional*  
**Caso de Aplicación:** Caso 10 — *Transportes Curimón S.A.* (Licitación TFEP-01/2026)  
**Responsable:** Marcel (Persona 6 — *Assessment & Knowledge Verification Lead*)  
**Marco Normativo:** Bases Administrativas FEP01.26 (Art. 13.5 y Formulario A-6), Indicaciones FEP00.3.26 (Sección 6.1) y Comunicado 9.  
**Fecha de Emisión:** 21 de septiembre de 2026  

---

## 1. Declaración Formal de Autoría y Criterio de Uso (Nivel 0 y Nivel 1)

En cumplimiento estricto del Artículo 13.5 de las Bases Administrativas, las directrices de la Sección 6.1 de las Indicaciones del Trabajo y el Comunicado 9 de la Escuela de Informática:

1. **Autoría Intelectual, Pedagógica y Legal (Nivel 0 - 100% Humano):**
   * **Prohibición Taxativa de IA en Redacción:** En estricta conformidad con el Punto 6.1 de las Indicaciones, declaro bajo fe de juramento académico que la totalidad de los **30 enunciados**, las **opciones y distractores plausibles**, las **respuestas clave** y las **justificaciones técnicas y fundamentos jurídicos** que integran el Anexo E fueron conceptualizadas, redactadas, resueltas y calibradas directamente por el estudiante sin delegación a inteligencias artificiales generativas.
   * **Diseño Pedagógico bajo Taxonomía de Bloom:** La calibración del banco en tres niveles cognitivos —12 preguntas Básicas (40%), 12 preguntas Intermedias (40%) y 6 preguntas Avanzadas (20%)—, así como la distribución equilibrada en 4 formatos (8 Selección múltiple, 8 Verdadero/Falso con justificación, 7 Oraciones para completar y 7 Respuestas de desarrollo corto), fue diseñada íntegramente por el estudiante para asegurar una evaluación rigurosa.
   * **Extracción y Validación en Fuentes Primarias:** Todas las disposiciones legales citadas (Ley 21.719 sobre Protección de Datos, Ley 21.663 Marco de Ciberseguridad / ANCI, Ley 21.459 de Delitos Informáticos, Código del Trabajo, Dictamen DT 569/2018), reglamentos internacionales (RGPD de la UE, EU AI Act 2024/1689), estándares técnicos (ISO/IEC 27001:2022, ISO/IEC 42001:2023) y antecedentes operativos del Caso Curimón (374 camiones, 454 choferes —196 de planta vs. 258 subcontratados—, topología de Azure Chile Central sin *paired region*, modelo Gordon-Loeb con cota $\le 37\%$ y *crypto-shredding* de 686 llaves HSM) fueron analizados, cotejados y extraídos manualmente desde las fuentes primarias oficiales (BCN, Diario Oficial, EUR-Lex y Bases FEP01/FEP02/FEP03).
   * **Solvencia para Interrogación Oral Individual (Comunicado 9):** El estudiante asume el dominio pleno para responder oralmente y sin titubeos ante la comisión docente sobre el fundamento normativo, la plausibilidad de los distractores y las decisiones de diseño de cualquiera de las 30 preguntas formuladas al azar.

2. **Alcance del Apoyo Técnico de IA (Nivel 1 - Asistencia de Formato y Diagramación):**
   * El uso de asistentes de inteligencia artificial se autorizó y limitó estrictamente a labores mecánicas y superficiales de formato: tabulación de estructuras en Markdown, estructuración de las llamadas a la macro `\pregunta` en sintaxis LaTeX de `informe-ti12.sty`, verificación de caracteres reservados de compilación (escapes de `\%`, comillas tipográficas, guiones dobles `--`) y cuadratura visual de la tabla del índice temático multidimensional.
   * Ninguna pregunta, respuesta, análisis pedagógico ni justificación legal fue delegada a generación algorítmica.

---

## 2. Matriz Resumen de Declaración por Sección (Formulario A-6)

| Entregable / Componente | Archivo Fuente | Nivel Declarado | Descripción del Aporte Humano (Nivel 0) | Alcance del Apoyo de IA (Nivel 1) |
| :--- | :--- | :---: | :--- | :--- |
| **Banco de Preguntas Básicas (40%)** | `Entregables/P_Basicas.md` | **Nivel 0 + 1** | Redacción manual de P01 a P12: plazos CSIRT (3 h), DPO voluntario, multas UTM, vacancia legal de 24 meses, ISO 27001, delitos informáticos, RGPD, OIV, CISO Assistant, transferencias EE.UU., ISO 42001 y datos biométricos. | Alineación y tabulación de opciones en Markdown y separación de campos. |
| **Banco de Preguntas Intermedias (40%)** | `Entregables/P_Intermedias.md` | **Nivel 0 + 1** | Redacción manual de P13 a P24: roles DPA Curimón/audIT, Azure Chile Central sin paired region, Dictamen DT 569/2018 (GPS), Art. 8 bis explicabilidad, EIPD preventiva, reporte OIV en 24 h, SLA contractual de 2 h y cross-mapping GRC. | Formateo de tablas Markdown y verificación de consistencia visual en justificaciones. |
| **Banco de Preguntas Avanzadas (20%)** | `Entregables/P_Avanzadas.md` | **Nivel 0 + 1** | Redacción manual de P25 a P30: US CLOUD Act vs BYOK/HYOK, análisis de sensibilidad del TCO, borrado criptográfico (*crypto-shredding*), resiliencia contractual, perfilamiento y cota 37% de Gordon-Loeb. | Formateo de expresiones matemáticas KaTeX/LaTeX ($1/e \approx 36,79\%$). |
| **Índice Temático y Matriz Multidimensional** | `Entregables/P_Indice_Tematico.md` | **Nivel 0 + 1** | Mapeo biunívoco de las 30 preguntas contra las 14 secciones del informe final y los 6 subtemas obligatorios de la Ficha TI-12. | Tabulación de la matriz cruzada de 5 columnas en Markdown. |
| **Subdocumento Consolidado en LaTeX** | `Subdocumento_Persona_6_Consolidado.tex` | **Nivel 0 + 1** | Definición de los 6 argumentos de cada macro `\pregunta` `{formato}{dificultad}{sección}{enunciado}{respuesta}{justificación}`. | Verificación de sintaxis de cierre de llaves, comillas tipográficas y escape de `\%`. |

---

## 3. Registro Cronológico de Prompts e Interacciones (Nivel 1)

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ REGISTRO DE INTERACCIONES DE APOYO FORMULARIO A-6 — MARCEL (PERSONA 6)                  │
├────┬────────────┬──────────────────────────────────────────┬──────────────┬────────────┤
│ ID │ Fecha/Hora │ Tarea de Apoyo Solicitada                │ Nivel de Uso │ Finalidad  │
├────┼────────────┼──────────────────────────────────────────┼──────────────┼────────────┤
│ 01 │ 17-09 10:15│ Formateo y tabulación de P_Basicas.md    │ Nivel 1      │ Maquetación│
│ 02 │ 17-09 14:30│ Tabulación Markdown de P_Intermedias.md  │ Nivel 1      │ Diagramación│
│ 03 │ 18-09 09:40│ Formateo de P_Avanzadas y fórmulas KaTeX │ Nivel 1      │ Formato    │
│ 04 │ 18-09 15:20│ Diagramación de matriz de Índice Temático│ Nivel 1      │ Tabulación │
│ 05 │ 19-09 11:10│ Conversión a macros LaTeX \pregunta      │ Nivel 1      │ LaTeX      │
│ 06 │ 19-09 16:45│ Depuración de escapes de % y caracteres  │ Nivel 1      │ Sintaxis   │
│ 07 │ 20-09 12:00│ Verificación de contadores (30 preguntas)│ Nivel 1      │ Cuadratura │
│ 08 │ 20-09 17:30│ Revisión de directrices de integración   │ Nivel 1      │ Edición    │
└────┴────────────┴──────────────────────────────────────────┴──────────────┴────────────┘
```

---

### Registro A6-01: Formateo y Tabulación de Preguntas Básicas en Markdown
* **Fecha y Hora:** 17-09-2026 10:15 hrs.
* **Integrante:** Marcel (Persona 6).
* **Sección / Entregable:** `Entregables/P_Basicas.md` (Preguntas P01 a P12).
* **Herramienta y Versión:** Asistente IA (Motor Claude / Gemini 3.8).
* **Nivel de Uso:** Nivel 1 (Formato y tabulación Markdown).
* **Prompt Empleado:**
  > *"Tengo redactadas manualmente las 12 preguntas básicas del Anexo E con sus enunciados, opciones a/b/c/d, respuestas y justificaciones legales (Ley 21.663 Art. 9, Ley 21.719 Art. 50, multas UTM, ISO 27001). Dale formato de bloques Markdown estandarizados con subtítulos para Enunciado, Opciones, Respuesta Correcta y Justificación Legal, sin alterar el texto ni las alternativas."*
* **Uso del Resultado:** Se estructuró el archivo modular [P_Basicas.md](file:///home/marcelx7/Desktop/Ramos%20U,%202026,%202do%20Sem/Fep%28Local%29%20%281%29/Investigacion/audIT/Investigacion/Persona-6/Entregables/P_Basicas.md) con jerarquía visual uniforme.
* **Verificación Humana:** El estudiante leyó y cotejó cada pregunta asegurando que las alternativas, respuestas y artículos legales permanecieran exactamente como fueron formulados.

---

### Registro A6-02: Tabulación Markdown de Preguntas Intermedias del Caso Curimón
* **Fecha y Hora:** 17-09-2026 14:30 hrs.
* **Integrante:** Marcel (Persona 6).
* **Sección / Entregable:** `Entregables/P_Intermedias.md` (Preguntas P13 a P24).
* **Herramienta y Versión:** Asistente IA (Motor Claude / Gemini 3.8).
* **Nivel de Uso:** Nivel 1 (Diagramación y alineación de datos).
* **Prompt Empleado:**
  > *"Organiza en formato Markdown homogéneo estas 12 preguntas intermedias aplicadas al Caso Curimón que redacté (roles Curimón/audIT, 374 camiones, Dictamen DT 569/2018 sobre GPS, Azure Chile Central sin paired region, SLA de 2 horas). Mantén intactos los textos, los distractores y las citas técnicas."*
* **Uso del Resultado:** Se maquetó el documento [P_Intermedias.md](file:///home/marcelx7/Desktop/Ramos%20U,%202026,%202do%20Sem/Fep%28Local%29%20%281%29/Investigacion/audIT/Investigacion/Persona-6/Entregables/P_Intermedias.md).
* **Verificación Humana:** Confirmación manual de los datos del caso: flota de 374 camiones, 454 choferes y parámetros del contrato.

---

### Registro A6-03: Formateo de Preguntas Avanzadas y Ecuaciones KaTeX
* **Fecha y Hora:** 18-09-2026 09:40 hrs.
* **Integrante:** Marcel (Persona 6).
* **Sección / Entregable:** `Entregables/P_Avanzadas.md` (Preguntas P25 a P30).
* **Herramienta y Versión:** Asistente IA (Motor Claude / Gemini 3.8).
* **Nivel de Uso:** Nivel 1 (Formateo tipográfico de expresiones matemáticas).
* **Prompt Empleado:**
  > *"En estas 6 preguntas avanzadas de análisis crítico (CLOUD Act, TCO del proyecto, borrado criptográfico y modelo Gordon-Loeb), formatea la cota matemática 1/e ≈ 36,79% en sintaxis KaTeX inline ($...$) y revisa que las tablas de compensaciones queden bien alineadas."*
* **Uso del Resultado:** Se aplicó la sintaxis matemática en [P_Avanzadas.md](file:///home/marcelx7/Desktop/Ramos%20U,%202026,%202do%20Sem/Fep%28Local%29%20%281%29/Investigacion/audIT/Investigacion/Persona-6/Entregables/P_Avanzadas.md).
* **Verificación Humana:** El estudiante comprobó el renderizado visual de los símbolos matemáticos y la consistencia con el modelo económico del informe.

---

### Registro A6-04: Diagramación de la Matriz de Índice Temático Multidimensional
* **Fecha y Hora:** 18-09-2026 15:20 hrs.
* **Integrante:** Marcel (Persona 6).
* **Sección / Entregable:** `Entregables/P_Indice_Tematico.md` (Matriz de cobertura).
* **Herramienta y Versión:** Asistente IA (Motor Claude / Gemini 3.8).
* **Nivel de Uso:** Nivel 1 (Tabulación y estructuración de matriz).
* **Prompt Empleado:**
  > *"Tengo el listado del mapeo de las 30 preguntas frente a las 14 secciones del informe final y los 6 subtemas de la Ficha TI-12. Dale formato de tabla Markdown limpia con 5 columnas: N.º Pregunta, Sección del Informe, Dificultad, Formato y Subtema TI-12 Evaluado, agregando al final una tabla resumen de cobertura por subtema."*
* **Uso del Resultado:** Se generó la tabla cruzada en [P_Indice_Tematico.md](file:///home/marcelx7/Desktop/Ramos%20U,%202026,%202do%20Sem/Fep%28Local%29%20%281%29/Investigacion/audIT/Investigacion/Persona-6/Entregables/P_Indice_Tematico.md).
* **Verificación Humana:** Verificación manual de que cada uno de los 6 subtemas de la Ficha TI-12 tuviese al menos 1 pregunta asignada (se certificaron entre 3 y 8 preguntas por subtema).

---

### Registro A6-05: Conversión a Macros LaTeX `\pregunta` en `informe-ti12.sty`
* **Fecha y Hora:** 19-09-2026 11:10 hrs.
* **Integrante:** Marcel (Persona 6).
* **Sección / Entregable:** `Subdocumento_Persona_6_Consolidado.tex`.
* **Herramienta y Versión:** Asistente IA (Motor Claude / Gemini 3.8).
* **Nivel de Uso:** Nivel 1 (Conversión de sintaxis a macro LaTeX).
* **Prompt Empleado:**
  > *"Toma el texto de mis 30 preguntas estructuradas y conviértelas al llamado exacto de la macro LaTeX oficial: \pregunta{formato}{dificultad}{sección}{enunciado}{respuesta}{justificación}, respetando estrictamente los valores válidos: formato (seleccion, vf, completar, corta), dificultad (basica, intermedia, avanzada) y el nombre de la sección correspondiente."*
* **Uso del Resultado:** Se construyó el bloque de 30 macros compilables en [Subdocumento_Persona_6_Consolidado.tex](file:///home/marcelx7/Desktop/Ramos%20U,%202026,%202do%20Sem/Fep%28Local%29%20%281%29/Investigacion/audIT/Investigacion/Persona-6/Subdocumento_Persona_6_Consolidado.tex).
* **Verificación Humana:** El estudiante revisó que no faltara ningún argumento entre llaves y que los textos coincidieran exactamente con los archivos Markdown originales.

---

### Registro A6-06: Depuración de Caracteres Especiales y Escapes en LaTeX
* **Fecha y Hora:** 19-09-2026 16:45 hrs.
* **Integrante:** Marcel (Persona 6).
* **Sección / Entregable:** `Subdocumento_Persona_6_Consolidado.tex` (Control de compilación).
* **Herramienta y Versión:** Asistente IA (Motor Claude / Gemini 3.8).
* **Nivel de Uso:** Nivel 1 (Depuración sintáctica LaTeX).
* **Prompt Empleado:**
  > *"Revisa este código .tex con las 30 preguntas para asegurar que todos los signos de porcentaje estén escapados como \%, las comillas dobles utilicen comillas latinas tipográficas (« » o `` ''), las alternativas de selección usen \\ como separador y los espacios de completar usen \rule{3cm}{0.4pt}."*
* **Uso del Resultado:** Se blindó el archivo contra errores de compilación con XeLaTeX.
* **Verificación Humana:** Inspección visual de líneas y búsqueda de `%` sin barra para evitar líneas comentadas accidentalmente.

---

### Registro A6-07: Verificación de Contadores Automáticos y Cuadratura del Anexo E
* **Fecha y Hora:** 20-09-2026 12:00 hrs.
* **Integrante:** Marcel (Persona 6).
* **Sección / Entregable:** Anexo E y control de rúbrica.
* **Herramienta y Versión:** Asistente IA (Motor Claude / Gemini 3.8).
* **Nivel de Uso:** Nivel 1 (Control de calidad y verificación aritmética).
* **Prompt Empleado:**
  > *"Calcula el recuento total de las preguntas en el archivo .tex según sus argumentos: verifica que la suma total sea exactamente 30, que las básicas sean 12 (40%), intermedias 12 (40%), avanzadas 6 (20%) y que los formatos se distribuyan en 8 selección, 8 vf, 7 completar y 7 corta."*
* **Uso del Resultado:** Confirmación de cuadratura exacta antes de enviar las directrices a Persona 1.
* **Verificación Humana:** Comprobación directa contra la rúbrica oficial de la asignatura.

---

### Registro A6-08: Maquetación de Directrices de Integración para Persona 1 y Persona 8
* **Fecha y Hora:** 20-09-2026 17:30 hrs.
* **Integrante:** Marcel (Persona 6).
* **Sección / Entregable:** `Directrices_Integracion_Anexo_E_LaTeX.md`.
* **Herramienta y Versión:** Asistente IA (Motor Claude / Gemini 3.8).
* **Nivel de Uso:** Nivel 1 (Formato de instructivo técnico).
* **Prompt Empleado:**
  > *"Estructura un instructivo técnico en Markdown dirigido a Persona 1 (Editor Líder) y Persona 8 (Auditor de Calidad) explicando paso a paso cómo reemplazar el comando \pendienteHumano en content/(7)-anexos.tex con las macros del Anexo E, y cómo funcionan los contadores automáticos \controlCuestionario e \indiceTematico."*
* **Uso del Resultado:** Se redactó el documento [Directrices_Integracion_Anexo_E_LaTeX.md](file:///home/marcelx7/Desktop/Ramos%20U,%202026,%202do%20Sem/Fep%28Local%29%20%281%29/Investigacion/audIT/Investigacion/Persona-6/Directrices_Integracion_Anexo_E_LaTeX.md).
* **Verificación Humana:** El estudiante validó la ruta del archivo maestro y el comando de compilación (`./compilar.sh`).

---

## 4. Certificación para Integración Consolidada

El presente documento oficial se remite a:
* **Persona 8 (Matías — Auditor de Calidad, Fact-Checking & Custodio del Formulario A-6):** para la acreditación de cumplimiento en la planilla unificada de todo el equipo audIT.
* **Persona 1 (Ignacio C. — Editor Líder):** como constancia de conformidad de autoría para la compilación del Anexo de Declaración de IA en el documento maestro `10 - AUDIT - TI-12.pdf`.

---

## 5. Firma y Compromiso de Responsabilidad

El suscrito declara bajo juramento académico que el presente registro refleja con fidelidad y transparencia absoluta la totalidad de las interacciones realizadas con herramientas de inteligencia artificial durante el desarrollo de las tareas de la Persona 6. 

Todo el contenido sustantivo, las 30 preguntas, alternativas, respuestas clave, interpretaciones normativas (Leyes 21.719 y 21.663) y justificaciones del Caso Curimón son de responsabilidad intelectual y autoría exclusiva del estudiante.

\
**Marcel**  
Persona 6 — *Assessment & Knowledge Verification Lead*  
audIT Soluciones de Software SpA (Empresa N.º 10)  
Taller de Formulación de Proyectos Informáticos (ICI-5444)  
Pontificia Universidad Católica de Valparaíso  
