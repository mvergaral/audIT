# Plan de Anexos del Informe Final

## TI-12 · audIT (Empresa N.º 10) · Caso 10, Transportes Curimón S.A.

**Origen:** auditoría de Persona 8, hallazgo H-08. Hasta ahora cada capítulo remitía a un
anexo con una letra propia y sin plan común, lo que produce «referencias a secciones o
anexos inexistentes» (Comunicado 9, letra d).

**Criterio:** se conservan las letras que los capítulos **ya venían usando** —C, D, E y
F— y se añaden A y B, que no estaban asignadas. Así ninguna referencia existente queda
obsoleta.

| Anexo | Contenido | Responsable | Estado |
| :---: | :--- | :---: | :---: |
| **A** | Matriz de obligaciones completa (las 13 obligaciones con actividad, rol, plazo y partida) | P4 | Listo — `Entregable_1_Matriz_Obligaciones.md` |
| **B** | Verificación documentada del estado de vigencia normativa | P8 | Por completar — `Persona-8/Verificacion_Vigencia_Normativa.md` |
| **C** | Bitácora de búsqueda y descarte de herramientas GRC y marcos técnicos | P3 | **Falta el archivo** |
| **D** | Memoria metodológica, homologación E-26 y ficha de precios | P4 | Listo — `Subdocumento_…_Definitivo.md`, §6 |
| **E** | Cuestionario de 30 preguntas, clave de respuestas e índice temático | P6 | Listo — `Persona-6/` |
| **F** | Formulario A-6, declaración de uso de IA con las ocho firmas | P8 | 3 de 8 declaraciones |

---

## Referencias que NO son anexos del informe

Durante la auditoría se verificó que estas menciones remiten a anexos **de normas
externas** y son correctas. No deben renumerarse:

| Mención | Dónde | Qué es |
| :--- | :--- | :--- |
| «Anexo A» | `Entregable_2_Modelo_TCO.md:230`, `Justificacion_Proxys_E26_Mercado.md:82` | Anexo A de la **ISO/IEC 27001:2022** (lista de controles) |
| «Anexo I» y «Anexo III» | `Subdocumento_Persona_3_Consolidado.md`, tabla de vigencias | Anexos I y III del **Reglamento (UE) 2024/1689** de IA |
| «Anexo A-6» | `Persona-4/README.md:38` | El **Formulario A-6**, no una letra de anexo |

---

## Pendiente crítico: el Anexo C

El §4 de las Indicaciones exige, cuando el grupo concluye que no hay más alternativas
relevantes, «*declararlo expresamente y documentar la búsqueda realizada: fuentes
consultadas, criterios de descarte y fecha*», y advierte que «*omitir el punto sin
declararlo se evalúa como ficha incompleta*».

`Persona-3/README.md` anuncia el archivo `Bitacora_Alternativas_GRC_P3.md` como soporte
de ese anexo, pero **el archivo no existe en el repositorio**. Solo Persona 3 puede
escribirlo: es el registro de qué buscó, qué descartó y por qué.

Contenido mínimo: las herramientas y marcos evaluados y no incorporados, el criterio de
descarte de cada uno, las fuentes consultadas y la fecha. Persona 3 ya tiene el material
—el §2.2 y el §3.1 del subdocumento explican por qué entraron Osano, Eramba, la Ley
25.326 y el SOC 2 Type II—; falta el reverso, es decir, los cinco marcos que dice haber
evaluado y descartado.
