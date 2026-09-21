# Plan de Recorte Editorial del Informe Maestro

## TI-12 · audIT (Empresa N.º 10) · para Persona 1

**Origen:** ensamblaje del 21-09-2026 (`Investigacion/INFORME-MAESTRO.md`).
**Problema:** el cuerpo mide **23,9 páginas** contra un presupuesto de **10 a 15**.
Hay que recortar **~4.450 palabras, unas 9 páginas**.

> El §2 de las Indicaciones fija la extensión como requisito formal, y el §4 advierte que
> **«no se valora la extensión: un informe largo sin aporte propio se evalúa peor que uno
> breve con análisis genuino»**. El recorte no es opcional.

---

## Estado actual por capítulo

| Capítulo | Autor | Actual | Presupuesto | Exceso |
| :--- | :---: | ---: | ---: | ---: |
| Apertura: resumen ejecutivo, introducción y aporte propio | P1 | 1,6 p | 1,5 p | — |
| **1. Marco legal chileno** | P2 | **5,2 p** | 2,0–2,5 p | **−2,7 p** |
| **2. Marco internacional, normas técnicas y GRC** | P3 | **6,7 p** | 3,0–4,0 p | **−2,7 p** |
| **3. Matriz de obligaciones e impacto económico** | P4 | **5,4 p** | 1,5–2,0 p | **−3,4 p** |
| **4. Arquitectura y aplicación al Caso 10** | P5 | **4,5 p** | 1,5–2,0 p | **−2,5 p** |
| Síntesis, conclusiones y recomendaciones | P1 | 0,9 p | 1,0 p | — |
| Referencias | — | 0,5 p | — | — |

Los dos capítulos de Persona 1 están dentro de presupuesto. El exceso está íntegramente en
los cuatro capítulos técnicos.

---

## Recortes ya aplicados en el ensamblaje

| Qué | Dónde va |
| :--- | :--- |
| §6 de Persona 4, memoria metodológica y ficha de precios | Anexo D, por indicación de su propio encabezado |
| §7 de Persona 4, script `modelo_costos.py` | Anexo D |
| Cabeceras de asignatura, notas editoriales internas y bloques de metadatos de cada subdocumento | Eliminados |

---

## Recortes autorizados por sus autores, pendientes de aplicar

**Persona 2** dejó por escrito su orden de prioridad de eliminación:

1. El detalle del régimen sancionatorio del §2 — íntegro en su Entregable 1.
2. El desglose de etapas de calificación de OIV del §3 — íntegro en su Entregable 2.
3. Los ítems 3 y 4 del §6 — aplicaciones derivadas, no hallazgos.

Y marcó como **no recortables**: la asimetría del §1, el Artículo 14 sexies del §2, el
esquema 3/72/15 del §3 y la figura del §5, por sostener los capítulos de P4 y P5.

---

## Candidatos para los otros tres capítulos

Ninguno de estos autores dejó instrucciones de recorte. Son propuestas del auditor y
**requieren su visto bueno**, porque cada uno debe poder defender oralmente lo que quede.

| Capítulo | Candidato | Por qué | Ahorro aprox. |
| :--- | :--- | :--- | ---: |
| **P3** | §3.2, ficha objetiva de las ocho herramientas | Es una tabla de datos crudos; la matriz del §3.3.2 ya la resume y el análisis del §3.3.3 la interpreta | 0,8 p |
| **P3** | §2.3, costo de certificación | Cuatro componentes de costo que P4 ya incorpora al modelo | 0,6 p |
| **P3** | §1.2 y §1.3, tablas de vigencias y lectura comparada | Solapan con el **Anexo B** de verificación de vigencia | 1,0 p |
| **P4** | §2, matriz de las 13 obligaciones | Reemplazable por una síntesis de 5 filas remitiendo al **Anexo A**, que la contiene completa | 1,5 p |
| **P4** | §4.2, matriz de sensibilidad 3×3 y cuadrantes asimétricos | El §4.1 ya establece la banda de variación | 0,8 p |
| **P5** | §3, trazabilidad EDT, hitos y calce E-26 | Detalle de gestión del proyecto, no de cumplimiento normativo | 1,2 p |
| **P5** | Diagramas ASCII extensos del §1 | Conservar uno, remitir el resto a sus entregables | 0,8 p |

Aplicando los tres de Persona 2 y estos siete, el cuerpo queda en torno a **14 páginas**.

---

## Regla que no debe romperse al recortar

El Comunicado 9, letra a), sanciona el capítulo cuyas figuras y tablas **aparezcan sin que
el texto las cite, las explique ni derive conclusiones de ellas**. Al quitar una tabla hay
que quitar también su párrafo de análisis, o al revés: **nunca dejar el análisis sin la
tabla ni la tabla sin el análisis**. Es el error más fácil de cometer recortando contra
reloj y el más caro.

Del mismo modo, si una tabla se traslada a un anexo, el cuerpo debe conservar la frase que
la cita y la conclusión que de ella se deriva.
