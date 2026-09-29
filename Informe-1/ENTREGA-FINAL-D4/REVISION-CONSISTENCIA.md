# Revisión de consistencia del Informe 1 y del repositorio audIT

Fecha de corte 06-09-2026, actualizada tras los cambios de D1, D2 y D3 de las 18:45. Verificado contra los tres documentos de la licitación con
`audIT/tools/buscar.py` y por contraste cruzado entre los archivos de las cuatro duplas.

---

## 1. Lo que quedó consistente

| Materia | Estado |
|---|---|
| Cifras de volumetría del numeral 14.1 | Coinciden en las cuatro duplas y en el informe |
| Partición de la flota en 148, 192 y 34 | Alineada tras la corrección enviada a D3 |
| Buffer a bordo de 8 GB en lugar de 120 horas | Aceptado por D3 y reflejado en ambos documentos |
| Frecuencia de muestreo 30 s en marcha y 5 min detenido | Idéntica en D3 y D4 |
| Capa anticorrupción anclada a RT-05.20 | Corregido por D3 |
| App móvil como canal voluntario | Corregido por D3 |
| Plazos de retención por dominio | Idénticos en D3 y D4 |
| Proveedor de nube y región | Azure Chile Central en ambas duplas |
| Reglas de escritura del informe | Cero punto y coma, cero raya em, cero guion doble |
| Reparto de las cinco innovaciones | Ratificado por D2 el 06-09 y reflejado en el subdocumento 13 |
| Cita del Código del Trabajo | Alineada con la corrección APA de D1. Decreto con Fuerza de Ley N.º 1 de 2003, no 2001 ni 2024 |
| Metodología de emisiones | ISO 14083 y marco GLEC, ratificados por D2 en RF-023 |
| Indicadores de la innovación tipo 3 | Línea base y meta tomadas de la ficha de D3 |

## 2. Lo que sigue abierto y afecta la entrega

### 2.1 Innovaciones tipo 4 y tipo 5. RESUELTO el 06-09-2026

D2 zanjó el conflicto en su plan de trabajo y dejó constancia del acuerdo.

> Una nota anterior de reparto daba a D2 los tipos 1 y 5, y el tipo 4 a D1. Se resolvió mantener el
> reparto del plan general: D2 toma 1 y 4, y D1 queda con el tipo 5.

| Tipo | Dupla | Responsable |
|---|---|---|
| 1 Producto o servicio | D2 | Ignacio C. |
| 2 Proceso | D4 | Ignacio V. y Alonso |
| 3 Tecnológica o de arquitectura | D3 | Marcel y Martín |
| 4 Modelo de negocio o contratación | D2 | Matías V. |
| 5 Experiencia de usuario, sostenibilidad o impacto social | D1 | Carlos y Naomi |

Los marcadores de responsable pendiente ya no existen en el subdocumento 13. Queda una tarea
menor. `equipo/asignacion-duplas.md` sigue diciendo que el tipo 4 es de D1 y el tipo 5 de D2, que
es lo contrario del acuerdo. Ese archivo debe corregirse para que exista una sola fuente.

### 2.2 Las 6.000 vigencias están asignadas al contexto equivocado

El modelo de dominio sitúa la matriz completa en el contexto de Flota y activos. La mitad de esas
fechas son de personas, es decir licencia de conducir, examen médico y curso de sustancias
peligrosas. Con el reparto actual, el servicio que valida la jornada tiene que salir de su contexto
para verificar una licencia. Lo defendible es llevarla íntegra al contexto de Personas y
cumplimiento, o crear un contexto propio de Cumplimiento que sirva a los otros dos.

### 2.3 Supuestos de D3 que no aparecen en ninguna base

Verificado por búsqueda sobre los tres documentos.

| Dato | Dónde aparece | Situación |
|---|---|---|
| Precisión de geocerca de más menos 15 metros | `D3/plan-de-trabajo.md` | No está en las bases. Es supuesto y debe declararse |
| Retención de 120 horas del buffer | `D3/plan-de-trabajo.md` | Retirada en `Para_D4.md`, pero sigue en el plan |
| Resolución Exenta 107 de 2014 del SII | `D3/plan-de-trabajo.md` | Sin verificar |
| Latencia de sincronización menor a 15 minutos | `D3/plan-de-trabajo.md` | Más estricta que el umbral del Capítulo 15. Conviene redactarla como superación del umbral exigido |

### 2.4 Errores puntuales en `Para_D4.md`

| Punto | Dice | Corresponde |
|---|---|---|
| Código del buffer | Las 72 horas de desconexión, RT-03.13 | Las 72 horas son RT-03.10. RT-03.13 es la declaración de funciones no disponibles |
| Terminales con descarga por red inalámbrica | Los 5 terminales regionales | Son 4 regionales más San Bernardo, cinco en total |
| Notación del cálculo | 374 tractocamiones por 41 millones de kilómetros | Los 41 millones son el total de la flota. El resultado de 745.000 horas es correcto, la fórmula no |
| Pings anuales | 89,4 millones | Cuenta solo horas de marcha. Sumando el muestreo en detención son cerca de 120 millones |
| Concurrencia | 300 a 350 sesiones pico | El desglose propio suma 230 a 380 |
| Marcado | Repeticiones de mayor o igual a 8 GB y del signo de multiplicación | Duplicación de formato |

### 2.5 El archivo `audIT/CLAUDE.md` describe otro entregable

Ese archivo describe el trabajo como un informe de investigación de 10 a 15 páginas con
cuestionario de 30 preguntas y anexo de declaración de uso de inteligencia artificial, con entrega
el 21 de septiembre. Eso corresponde al Trabajo de Investigación 2026, documento FEP00.3.26, que es
una evaluación distinta de la simulación de licitación.

Lo que las cuatro duplas están construyendo es la Oferta Técnica del Sobre N.º 2, cuyo contenido lo
fija el Formulario T-22, cuya forma la fija el Artículo 40 y cuya fecha la fija el Formulario T-20.
Son dos entregas con reglas y fechas distintas. Conviene separarlas en el archivo de notas para que
nadie aplique el límite de 15 páginas a la oferta ni el Artículo 40 al informe de investigación.

## 3. Verificaciones normativas hechas sobre el texto de las bases

| Referencia | Estado |
|---|---|
| Artículo 16.1, prohibición de solución exclusivamente en nube o en on-premise | Verificado |
| Artículo 16.2, justificación componente por componente | Verificado |
| Artículo 16.3, obligación de declarar región primaria y secundaria | Verificado |
| Artículo 40.1, foliación correlativa como requisito excluyente | Verificado |
| Artículo 50.2, prohibición de cifras de precio | Verificado |
| RT-03.10, 72 horas del dispositivo y 12 horas de los terminales | Verificado |
| RT-06.01 del Caso, dispositivo a bordo como componente distribuido | Verificado |
| RT-07.02, distancia del sitio secundario | Verificado |
| RT-09.03, crecimiento de tres veces la volumetría | Verificado |
| RT-10.05, cierres de 12 días del paso fronterizo | Verificado en dos secciones |
| Numeral 2.1, las ocho capas obligatorias | Verificado |
| Numeral 6.1, las tres tipologías de recinto | Verificado |

## 4. Cumplimiento del Artículo 40 en el documento generado

| Exigencia | Estado |
|---|---|
| Foliación correlativa sin saltos | Cumple desde el índice. La portada no lleva número |
| Media firma en cada página | Marca de posición incorporada en el pie. Requiere la firma real |
| Índice detallado | Cumple, con índices de figuras y tablas |
| PDF con texto seleccionable | Cumple |
| Cuerpo de al menos 11 puntos | Cumple, cuerpo a 12 puntos |
| Tablas de al menos 9 puntos | Cumple, tablas a 10 puntos |
| Referencias en norma APA séptima edición | Cumple, con 18 fuentes |
| Ausencia de cifras de precio de la oferta | Cumple. Las cifras en pesos son del mandante y provienen del Caso |

## 5. Materias pendientes antes de la entrega

1. Resolver la asignación de las innovaciones tipo 4 y tipo 5, y actualizar `asignacion-duplas.md`
   para que exista una sola fuente.
2. Reasignar la matriz de vigencias al contexto de Personas y cumplimiento.
3. Corregir los seis puntos de `Para_D4.md`.
4. Declarar o eliminar los cuatro supuestos de D3 que no están en las bases.
5. Verificar las dos normas chilenas citadas y las referencias laborales de jornada.
6. Estimar personas usuarias concurrentes, internas y externas, para RT-09.01.
7. Incorporar la firma real en el pie de página.
8. Separar en `audIT/CLAUDE.md` los dos entregables del curso.
