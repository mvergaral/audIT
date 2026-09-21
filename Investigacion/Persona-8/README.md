# Persona 8 — Matías V.

## Auditor de Calidad, Verificación de Vigencia y Custodio del Formulario A-6

**Nivel de uso de IA: 0 estricto.** El auditor es la barrera de control humano imparcial
que valida la probidad del trabajo completo. Cualquier uso de IA en esta función
comprometería la credibilidad de toda la declaración.

---

## Qué hay en esta carpeta

| Archivo | Qué es | Estado |
| :--- | :--- | :---: |
| [`Auditoria_C9_Preentrega.md`](Auditoria_C9_Preentrega.md) | Barrido de los seis capítulos contra los cuatro indicios del Comunicado 9. 12 hallazgos con archivo y línea | Cerrado |
| [`Fact_Checking_Referencias.md`](Fact_Checking_Referencias.md) | Inventario de las 92 URL y de las referencias bibliográficas del corpus, clasificadas por prioridad de verificación. Incluye seis referencias de Persona 4 con forma de fuente no verificada | **Por verificar** |
| [`Verificacion_Vigencia_Normativa.md`](Verificacion_Vigencia_Normativa.md) | Entregable exigido por nombre en la ficha TI-12: 38 filas de norma, estado, fuente oficial y fecha de consulta | **En blanco, por llenar a mano** |
| [`Formulario_A6_Consolidado.md`](Formulario_A6_Consolidado.md) | Anexo de declaración de IA de los ocho integrantes | 3 de 8 recibidas |

---

## Criterio de intervención

> Si hay que elegir entre dos opciones válidas, el auditor lo pide.
> Si solo hay una respuesta correcta y ya está verificada, el auditor la aplica.

El auditor **no reescribe capítulos ajenos**. La razón no es jerárquica: el Formulario
A-6 se firma individualmente, y el Comunicado 9 sanciona «*cualquier capítulo, sección o
figura que el grupo sea incapaz de explicar*». Si el auditor corrige una cifra de otro
integrante, esa persona firma una declaración que dejó de ser cierta y no podrá defender
oralmente un número que no calculó.

### Correcciones que sí aplica el auditor

Erratas ya verificadas contra fuente oficial, sin criterio de contenido de por medio:

| Corrección | Alcance | Verificada por |
| :--- | :--- | :--- |
| `Art. 14` Ley 21.663 → `Art. 9` + `Art. 27` + `D.S. 295/2024` | 7 puntos en `Persona-4/` | P2, `Entregable_2`, §2 |
| `13/12/2026` → `01/12/2026` | 12 en `Entregable_1_Matriz_Obligaciones`, 10 en `Subdocumento_P4_Consolidado` | P2, Art. primero transitorio |
| Voz en segunda persona | `Persona-3/Subdocumento…md` líneas 153, 156, 159 | Comunicado 9, letra d) |
| Párrafo sobre el «docente evaluador» | `Subdocumento_P4…Definitivo.md` §8 | Comunicado 9, letra d) |

Cada una va en su propio commit, con el autor mencionado, para que quede trazable.

### Lo que el auditor no toca

Cifras, elección de herramienta o de arquitectura, y todo numeral que Persona 2 dejó
marcado `[NV]` —señaladamente el artículo del DPO, donde las fuentes discrepan entre el
49 y el 50 y Persona 4 cita el 48. Eso se verifica en fuente primaria, no se reemplaza.

---

## Verificaciones heredadas

Persona 2 dejó trabajo explícitamente derivado a Persona 8:

- Las 9 leyes con fecha de Diario Oficial sin confirmar (`Entregable_6`).
- El estado de Chile ante el **Convenio 108+ (CETS 223)** en el Treaty Office del Consejo
  de Europa.
- Los `[NV]` de la sección §7.2 del `Entregable_1`.
- La errata del **D.S. N° 285/2024** en la fila 18 del cuadro comparativo: verificarlo o
  retirarlo.

Todas están incorporadas como filas de `Verificacion_Vigencia_Normativa.md`.

---

## Verificación de límites formales

| Requisito | Fuente | Estado |
| :--- | :--- | :---: |
| Informe de 10 a 15 páginas | Indicaciones §2 | ☐ |
| Nombre del archivo: `10 - AUDIT - TI-12.pdf` | Indicaciones §2 | ☐ |
| Asunto del correo: `[ICI544] - 10 - AUDIT - TI-12` | Indicaciones §2 | ☐ |
| Entrega impresa **y** electrónica en PDF | Indicaciones §2 | ☐ |
| Presentación en PowerPoint o PDF | Indicaciones §2 | ☐ |
| Cuestionario de 30 preguntas con índice temático | Indicaciones §3 | ☑ |
| Párrafo de aporte propio al cierre de la introducción | Indicaciones §4 | ☐ |
| Verificación documentada de vigencia | Ficha TI-12 | ☐ |
| Anexo A-6 con las ocho firmas | Indicaciones §6.3 | ☐ |
