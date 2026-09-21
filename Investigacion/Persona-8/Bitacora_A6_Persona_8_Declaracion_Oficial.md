# Declaración Oficial de Uso de Inteligencia Artificial (Formulario A-6)
## Persona 8: Auditoría de Calidad, Verificación de Vigencia y Custodia del Formulario A-6

**Asignatura:** Taller de Formulación de Proyectos Informáticos (ICI-5444) · Escuela de Informática, PUCV
**Empresa Asignada:** AudIT (Empresa N.º 10)
**Tema de Investigación:** TI-12 · *Cumplimiento normativo en proyectos TIC*
**Caso de Aplicación:** Caso 10 — *Transportes Curimón S.A.*
**Responsable:** Matías Vergara (Persona 8)
**Marco Normativo:** Bases Administrativas FEP01.26 (Art. 13.5 y Formulario A-6), Indicaciones FEP00.3.26 (Secciones 6.1 a 6.4) y Comunicado 9.
**Fecha de Emisión:** 21 de septiembre de 2026

---

## 1. Alcance de lo que aporta Persona 8 al informe

El rol de auditoría produce dos piezas que forman parte del informe y un conjunto de
artefactos internos que no se despachan:

| Pieza | ¿Va en el informe? |
| :--- | :--- |
| **Anexo B** — Verificación documentada del estado de vigencia normativa | Sí. Exigido por nombre en la ficha TI-12 |
| **Anexo F** — Formulario A-6 consolidado | Sí. Exigido por el §6.3 |
| Informe de auditoría del Comunicado 9, fact-checking de referencias y verificación aritmética | No. Instrumentos internos de control previo al despacho |
| Correcciones aplicadas sobre capítulos de otros integrantes | Sí, indirectamente: su resultado queda en los capítulos de sus autores |

---

## 2. Matriz de declaración por sección

| Actividad | Nivel | Alcance declarado |
| :--- | :---: | :--- |
| **Verificación del estado de vigencia de cada norma en su fuente oficial** (Anexo B) | **0** | Cada fila se cierra abriendo la fuente —BCN, Diario Oficial, EUR-Lex, Treaty Office, iso.org— y anotando la fecha de consulta. El §6.1 es taxativo: las cifras, citas y referencias se obtienen de la fuente, no del modelo |
| **Fact-checking de las 92 URL y de las referencias bibliográficas** | **0** | Misma razón. La clasificación previa por indicios estructurales fue asistida; **la confirmación de que una fuente existe es humana y no se delega** |
| **Consolidación del Formulario A-6 y custodia de las firmas** (Anexo F) | **0** | Recopilación de las declaraciones individuales, verificación de que el nivel declarado sea coherente con lo observado y constancia de las no recibidas |
| **Barrido de coherencia cruzada sobre el corpus** (contradicciones entre capítulos, marcadores residuales, figuras huérfanas) | **2** | Se emplearon búsquedas y comparaciones automatizadas sobre los archivos del repositorio para localizar los puntos a revisar. **La calificación de cada hallazgo y la decisión de qué corregir y qué elevar a su autor son juicio propio** |
| **Verificación aritmética del modelo económico de Persona 4** | **2** | Scripts de recálculo generados con asistencia, identificados como código auxiliar conforme al §6.1. Los resultados son reproducibles y verificables por cualquiera: la tabla cuadra o no cuadra |
| **Procesamiento de las ocho firmas digitalizadas** (recorte, fondo transparente, rotación) | **2** | Código auxiliar de tratamiento de imagen, identificado como tal |
| **Redacción de los informes internos de auditoría** (`Auditoria_C9_Preentrega`, `Fact_Checking_Referencias`, `Verificacion_Aritmetica_P4`) | **3** | Redactados con asistencia de IA a partir de los hallazgos del barrido. **No forman parte del informe despachado**; son instrumentos de control interno |
| **Redacción de §3.3.3, §3.3.4 y cierre del §4 del capítulo de Persona 3** | **3** | Generados con asistencia de IA sobre datos ya presentes en ese capítulo, para subsanar el hallazgo H-04. Declarado también en la declaración de Persona 3 |

---

## 3. Herramientas y versiones

| Actividad | Herramienta y versión |
| :--- | :--- |
| Barrido de coherencia, verificación aritmética, procesamiento de firmas y redacción de los informes de auditoría | Claude Opus 5 (`claude-opus-5`), vía Claude Code |
| Consulta del corpus de las bases de licitación | `tools/buscar.py` del repositorio (índice FTS5 propio, sin IA) |
| Verificación de fuentes oficiales | Navegador, sin asistencia |

---

## 4. Correcciones aplicadas sobre capítulos de otros integrantes

En calidad de auditor se aplicaron correcciones **sobre erratas ya verificadas en fuente
oficial por otro integrante**, sin decidir contenido. Cada una quedó en su propio commit,
nominando al autor afectado:

| Commit | Corrección |
| :--- | :--- |
| `390d3fd` | Deber de reporte de incidentes: Art. 14 → Art. 9 de la Ley 21.663, más Art. 27 y D.S. 295/2024. Verificado por Persona 2 |
| `96102d0` | Vigencia de la Ley 21.719: 13/12/2026 → 01/12/2026, por el Artículo primero transitorio. Verificado por Persona 2 |
| `7bf605b` | Retiro de la voz del asistente en el capítulo de Persona 3 |
| `9c08e87` | Traslado de la guía de defensa oral desde el subdocumento al manual operativo |
| `84d4e3e` | RoSI, VAN, reancla de la matriz de sensibilidad, rutas de disco en bibliografías, defectos de forma de Persona 3, plan de anexos |
| `4be6e90` | Tramo 3 de 16 meses y TCO 8.375,40 → 8.492,16 UF; herramienta GRC unificada |
| `1e42fc0` | Custodia de claves unificada en Azure Key Vault Premium, por decisión de Persona 5 |

**No se modificó ninguna cifra, elección de herramienta ni numeral marcado `[NV]` sin
decisión expresa de su autor.**

---

## 5. Declaración de cierre

Declaro que las verificaciones en fuente oficial que constan en el Anexo B y en el
fact-checking de referencias fueron realizadas personalmente, que las cifras y citas del
informe se obtuvieron de su fuente y no de un modelo, y que puedo explicar oralmente cada
hallazgo de la auditoría, la aritmética del modelo económico y el criterio con que se
distinguió entre corrección aplicable y decisión reservada a su autor.

Declaro asimismo, conforme al §6.4, el uso de asistencia de inteligencia artificial en los
niveles consignados en el §2, incluidos los de nivel 3, por ser preferible la declaración
exacta a la omisión.

---

## 6. Firma

<img src="firmas/P8_Matias_Vergara.png" alt="Firma de Matías Vergara" height="80">

**Matías Vergara**
Persona 8 — Auditoría de calidad, verificación de vigencia y custodia del Formulario A-6
AudIT (Empresa N.º 10) · TI-12 · 21 de septiembre de 2026
