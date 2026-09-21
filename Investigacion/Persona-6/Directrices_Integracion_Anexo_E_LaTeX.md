# Directrices de Integración Técnica: Anexo E en LaTeX
## Procedimiento de Ensamblaje y Validación Automatizada
**Emisor:** Persona 6 (*Assessment & Knowledge Verification Lead*)  
**Receptores:** Persona 1 (*Lead Editor*) & Persona 8 (*QA Auditor*)  
**Asignatura:** ICI-5444 · Taller de Formulación de Proyectos Informáticos (PUCV)  

---

## 1. Archivos Involucrados en el Proyecto LaTeX

El cuestionario se integra en la estructura del informe compilable ubicado en:
`.../Informe_Investigacion/Formato_INF_PUCV__4_/`

* **Archivo fuente de las preguntas:** `Persona-6/Subdocumento_Persona_6_Consolidado.tex`
* **Archivo de destino en el informe:** `content/(7)-anexos.tex`
* **Archivo de macros del cuestionario:** `informe-ti12.sty`
* **Script de compilación:** `./compilar.sh`

---

## 2. Procedimiento Paso a Paso de Integración

### Paso 1: Localización del bloque en `content/(7)-anexos.tex`
Abrir `content/(7)-anexos.tex` y descender hasta la subsección `Anexo E`:

```latex
\clearpage
% ===========================================================================
\phantomsection
\addcontentsline{toc}{subsection}{Anexo E. Cuestionario de 30 preguntas}
\subsection*{Anexo E. Cuestionario de evaluación de conocimientos}

\pendienteHumano{Cuestionario de 30 preguntas}{0.25}{...}

\subsubsection*{Control de distribución}
\controlCuestionario

\subsubsection*{Índice temático}
\indiceTematico
```

### Paso 2: Reemplazo del recuadro pendiente
Eliminar la línea:
```latex
\pendienteHumano{Cuestionario de 30 preguntas}{0.25}{Redacción de preguntas, respuestas y justificaciones de autoría del grupo. Usar el comando \texttt{\textbackslash pregunta\{formato\}\{dificultad\}\{sección\}\{enunciado\}\{respuesta\}\{justificación\}} con formato \texttt{seleccion}, \texttt{vf}, \texttt{completar} o \texttt{corta}, y dificultad \texttt{basica}, \texttt{intermedia} o \texttt{avanzada}. Las tablas de control y de índice temático de abajo se llenan solas.}
```

Y en su lugar, insertar el contenido completo de `Persona-6/Subdocumento_Persona_6_Consolidado.tex` (las 30 llamadas `\pregunta{...}{...}{...}{...}{...}{...}`).

> [!IMPORTANT]
> **No eliminar** las llamadas `\controlCuestionario` ni `\indiceTematico`. Estas dos macros deben quedar inmediatamente después de la Pregunta 30.

---

## 3. Comportamiento Automatizado de las Macros en LaTeX

Al compilar con `xelatex` o `./compilar.sh`:

1. **La macro `\pregunta` ejecuta:**
   * Incrementa el contador global `preguntaN`.
   * Incrementa el contador específico de dificultad (`preguntaBasica`, `preguntaIntermedia`, `preguntaAvanzada`).
   * Incrementa el contador específico de formato (`fmtSeleccion`, `fmtVF`, `fmtCompletar`, `fmtCorta`).
   * Acumula una nueva fila en el token `\filasIndiceTematico` con el formato:  
     `N.º & Sección & Dificultad & Formato \\ \hline`
   * Imprime el encabezado en negrita con el número de pregunta, formato, dificultad y sección.
   * Imprime el enunciado, la respuesta y la justificación.

2. **La macro `\controlCuestionario` genera:**
   Una tabla resumen que compara los contadores actuales contra la exigencia del curso:
   * Total actual (debe marcar **30**).
   * Básicas (debe marcar **12**).
   * Intermedias (debe marcar **12**).
   * Avanzadas (debe marcar **6**).
   * Formatos presentes (debe marcar **8 / 8 / 7 / 7**).

3. **La macro `\indiceTematico` genera:**
   Una tabla estructurada con las 30 filas ordenadas cronológicamente, mapeando cada pregunta con su sección respectiva del informe.

---

## 4. Verificación de Compilación y Control de Errores

Ejecutar desde el directorio del informe:
```bash
./compilar.sh
```

### Reglas para evitar errores de compilación comunes:
* **Símbolo de porcentaje:** Todo porcentaje en texto debe ir escapado como `\%` (ej. `2\% o 4\%`, `37\%`). Un `%` sin barra comenta el resto de la línea en LaTeX.
* **Comillas dobles:** Usar comillas latinas o tipográficas de LaTeX (``texto'' o comillas angulares « »), no comillas rectas dobles sueltas `"`.
* **Saltos de línea en enunciados de selección:** Utilizar estrictamente `\\` para separar las alternativas (ej. `a) Opción 1.\\ b) Opción 2.\\ c) Opción 3.\\ d) Opción 4.`).
* **Espacio para completar:** Emplear la macro tipográfica `\rule{3cm}{0.4pt}` o `\rule{4cm}{0.4pt}`.
