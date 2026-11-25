# Auditoría de la entrega

## 1. Alcance de la revisión

Esta auditoría considera exclusivamente los siguientes documentos:

1. `TFEP03.26_Plantillas.docx.md`, versión disponible de la plantilla `TFEP03.26_Plantillas.docx`.
2. `TFEP03.26_Taller_de_Riesgos_Enunciado_4046881d734894bcf889733d9dbfc778.pdf`.

No se revisaron otros archivos de la carpeta.

La auditoría registra información encontrada, cumplimiento observado, inconsistencias y riesgos de evaluación. No incorpora una versión corregida de la plantilla.

## 2. Resultado general

El documento presenta una estructura bastante completa y desarrolla todos los bloques principales de la Parte A y de la Parte B. La mayoría de los cálculos aritméticos son consistentes con los valores escritos.

El material todavía presenta hallazgos relevantes que impiden considerarlo completamente cerrado:

- Falta el entregable B.6, correspondiente a la lámina final.
- La tabla principal de respuestas no contiene todos los campos exigidos para B.2.
- Existen diferencias de costos entre secciones.
- Hay probabilidades y reglas de acción que no coinciden con ejemplos y reglas explícitas del enunciado.
- Algunos hechos utilizados en los riesgos no aparecen expresamente sustentados en el PDF.

## 3. Revisión por entregable

### A.1 - Diez frases de las bases

**Estado observado:** Cumplido en cantidad y estructura general.

- Se presentan exactamente diez cláusulas: BT-1, BT-2, BT-3, BT-5, BT-6, BT-7, BT-8, BA-1, BA-2 y BA-3.
- La selección no incluye BA-4, que el enunciado entrega como ejemplo resuelto y excluye expresamente del entregable A.1.
- La columna `Qué no está dicho` identifica silencios contractuales concretos.
- La columna adicional `Riesgo que produce` amplía la tabla mínima solicitada. No contiene una solución, por lo que no contradice directamente la prohibición de proponer soluciones en A.1.

### A.2 - RBS del proyecto

**Estado observado:** Cumplido en contenido mínimo.

- Están presentes las siete ramas de la RBS.
- Todas las ramas tienen al menos dos categorías de nivel 2, como exige el enunciado.
- Las categorías están adaptadas al caso de retail y no se limitan a nombres genéricos.
- La distribución de categorías por rama es 4, 4, 4, 2, 2, 2 y 2.

### A.3 - Registro de riesgos

**Estado observado:** Cumplido en cantidad y forma general, con observaciones de trazabilidad y calibración.

- Se presentan exactamente quince riesgos.
- Los enunciados siguen la forma `Dado que... entonces puede que... teniendo como consecuencia...`.
- Los riesgos tienen dueño, probabilidad, impacto y zona.
- Los impactos monetarios escritos posteriormente son coherentes con los rangos de la escala del enunciado.
- En la tabla principal de la sección 3 aparece la zona, pero no una columna numérica explícita para la exposición `P × I`. La exposición sí aparece posteriormente en la sección 4.3.

### A.4 - Priorización

**Estado observado:** Cumplido bajo las probabilidades actualmente asignadas.

- Se ordenan los quince riesgos.
- Se aplican los desempates por valor esperado cuando la exposición es igual.
- Se identifican los cinco riesgos de mayor exposición.
- Las observaciones de acción están presentes para los cinco primeros.

Existe una dependencia con la clasificación de R-03 y R-14: si se modifican sus probabilidades conforme a los ejemplos del enunciado, la priorización debe volver a evaluarse.

### B.1 - Registro cuantificado y reserva

**Estado observado:** Cumplido aritméticamente, con supuestos económicos poco documentados.

Se verifican los siguientes resultados bajo los valores actualmente escritos:

| Concepto | Valor registrado |
|---|---:|
| Suma de impactos | $161.261.300 |
| Reserva bruta / suma de valores esperados | $105.193.490 |
| Reserva como porcentaje de costos directos | 14,82 % |
| Reserva correspondiente al 5 % | $35.500.000 |
| Brecha frente al 5 % | $69.693.490 |
| Valor esperado eliminado por respuestas | $66.896.740 |
| Reserva residual | $38.296.750 |
| Costos directos con acciones | $726.500.000 |
| Oferta neta gestionada | $917.071.150 |

Los cálculos anteriores son internamente consistentes. Sin embargo, varios precios de compras, servicios externos, licencias, fletes y consultorías aparecen como supuestos sin una fuente o criterio de estimación visible en el documento.

### B.2 - Respuestas con etapa declarada

**Estado observado:** Parcialmente cumplido.

El enunciado exige ocho campos por respuesta. La tabla de la sección 6.1 presenta solamente:

- ID.
- Estrategia.
- Acción concreta.
- Dueño.
- Costo.
- Disparador.
- Etapa.

No presenta en esa tabla el riesgo residual ni el retorno. La sección 9 agrega valor esperado residual y retorno, pero no explicita la probabilidad residual ni el impacto residual.

También se observan estrategias combinadas como `Evitar / Mitigar`, `Evitar / Alcance` y `Evitar / Contrato`, mientras que el enunciado presenta las estrategias como categorías individuales.

### B.3 - Consulta, supuesto y exclusión

**Estado observado:** Cumplido en estructura, con una omisión en el supuesto y una referencia no verificable en la exclusión.

- Se incluye una consulta vinculada a R-03 y BT-1.
- Se incluye un supuesto vinculado a R-01 y BT-3.
- Se incluye una exclusión vinculada a R-06 y BT-6.
- La consulta identifica la decisión que depende de la respuesta.
- La exclusión incluye razón técnica y una vía de incorporación.
- El supuesto indica una tarifa horaria, pero no registra un monto total estimado para el escenario en que el supuesto resulte falso, pese a que el enunciado solicita una cifra.
- La exclusión menciona un `Catálogo de Obras Civiles Opcionales` y un `Anexo Económico N° 4`, referencias que no aparecen en el PDF revisado.

### B.4 - Matriz de riesgo a solución

**Estado observado:** Cumplido estructuralmente bajo el ranking actual.

- Se incluyen cinco riesgos.
- Cada fila modifica alcance, requisitos, arquitectura, plan/EDT o precio.
- No hay filas completamente vacías.
- La matriz hace visible que los riesgos producen cambios concretos en la oferta.

Su contenido depende de que el ranking de A.4 permanezca sin cambios.

### B.5 - Recálculo

**Estado observado:** Cumplido en aritmética general, con inconsistencias heredadas de B.2.

- Se calcula el retorno de las ocho respuestas.
- Se calcula la reserva residual.
- Se calcula la oferta gestionada y se compara con la oferta basada en el 5 %.
- La suma de los ahorros registrados es $66.896.740.
- El costo total de las acciones registradas es $16.500.000.

El recálculo debe considerarse dependiente de las probabilidades, costos y riesgos seleccionados actualmente.

### B.6 - Una lámina

**Estado observado:** No encontrado.

El enunciado exige una lámina final con tres riesgos, el cambio producido en la oferta y el costo de cada cambio. No existe una sección equivalente en la plantilla disponible.

## 4. Hallazgos prioritarios

### F-01 - Falta B.6

**Severidad:** Alta  
**Ubicación:** Plantilla, después de la sección 9; enunciado, sección 8.6.

El entregable final solicitado por el enunciado no está representado en la plantilla.

### F-02 - Campos incompletos en B.2

**Severidad:** Alta  
**Ubicación:** Plantilla, secciones 6.1 y 9; enunciado, sección 8.2.

No se registra de forma completa la probabilidad residual, el impacto residual, el valor esperado residual y el retorno dentro de cada respuesta. La información está repartida entre tablas y sigue faltando el detalle de probabilidad e impacto residuales.

### F-03 - Probabilidad de R-03

**Severidad:** Alta  
**Ubicación:** Plantilla, R-03 y sección 4.1; enunciado, sección 6.1, página 8.

R-03 se califica como `Muy alta · 0,90`. El propio enunciado utiliza como ejemplo el motor de promociones construido en 2013 sin documentación y lo califica como `Alta · 0,70`. La calificación registrada no coincide con el ejemplo explícito del método.

### F-04 - Probabilidad y regla de acción de R-14

**Severidad:** Alta  
**Ubicación:** Plantilla, R-14, sección 5 y sección 6.1; enunciado, secciones 5.3 y 6.1.

R-14 se clasifica como `Crítica · 0,40`, pero su respuesta se presenta como mitigación logística. La regla del enunciado para la zona crítica exige cambiar el diseño, eliminar la causa o no ofertar. Además, el ejemplo del enunciado sobre proveedor único y equipos importados usa probabilidad `Baja · 0,30`.

### F-05 - Costos inconsistentes

**Severidad:** Alta  
**Ubicación:** Plantilla, secciones 6.1 y 9.1.

- R-07 registra costo `$0` en la respuesta y `$2.800.000` en el retorno.
- R-04 registra costo `$5.000.000` en la respuesta y `$2.200.000` en el retorno.

La diferencia no altera el costo total declarado, pero sí afecta la trazabilidad de cada respuesta.

### F-06 - Hechos no expresamente sustentados

**Severidad:** Media-Alta  
**Ubicación:** Plantilla, enunciados y justificaciones de R-02, R-06, R-07, R-09, R-11 y R-15.

El PDF no declara expresamente algunos elementos usados como causas o evidencias:

- R-02: uso de LLM y ausencia de arquitectura determinista.
- R-06: parque de salas con quince años de operación.
- R-07: ventanas nocturnas de cuatro a cinco horas.
- R-09: baja familiaridad con IA y ausencia de protocolos de consulta.
- R-11: demora habitual de la gerencia comercial por contingencias.
- R-15: escasez estructural demostrada de perfiles MLOps/Data.

El enunciado permite justificar probabilidades con antecedentes del rubro, pero dicha evidencia no queda identificada en el documento.

### F-07 - Alcance de R-01

**Severidad:** Media  
**Ubicación:** Plantilla, R-01, supuesto de la sección 7 y matriz de la sección 8.

El caso informa 38.000 SKU activos y, por separado, define C1 para 40 categorías del surtido base. El documento usa 38.000 SKU como si fueran directamente el alcance del pronóstico. La relación entre ambos universos no queda explícita.

### F-08 - Supuestos de costos sin base visible

**Severidad:** Media  
**Ubicación:** Plantilla, sección 4.2.

Los desgloses muestran operaciones y montos, pero no siempre indican el criterio de estimación de servicios, licencias, hardware, fletes, consultorías o sanciones provisionadas. El enunciado indica que, cuando no exista un precio, debe declararse el supuesto.

### F-09 - Exposición numérica separada del registro principal

**Severidad:** Baja-Media  
**Ubicación:** Plantilla, sección 3 y sección 4.3; enunciado, sección 7.4.

La tabla principal de riesgos no incluye una columna numérica de exposición junto a la zona. La cifra sí aparece después, por lo que la información existe, pero queda separada del registro cualitativo original.

### F-10 - Artefactos de formato en la versión disponible

**Severidad:** Baja  
**Ubicación:** Plantilla Markdown disponible.

Se observan caracteres de salto internos, un `s.` aislado, un `.` aislado y un paréntesis escapado sobrante. Estos artefactos podrían provenir de la conversión desde DOCX; no se puede confirmar si aparecen en el archivo DOCX original.

## 5. Fortalezas observadas

- La cantidad de riesgos cumple con el mínimo exacto de quince.
- La RBS cubre las siete ramas y respeta el mínimo de categorías por rama.
- La estructura causal de los riesgos está bien aplicada.
- La mayoría de los impactos monetarios se encuentran dentro del rango de su nivel de impacto.
- La priorización está correctamente ordenada considerando exposición y valor esperado bajo los valores actuales.
- Los cálculos de reserva, ahorro, costos directos y oferta final son aritméticamente consistentes bajo los supuestos registrados.
- La matriz B.4 demuestra que los riesgos modifican la oferta en alcance, requisitos, arquitectura, planificación y precio.
- La consulta, el supuesto y la exclusión están identificados con riesgo y cláusula de origen.
- Las respuestas se concentran principalmente en propuesta e implementación, tal como recomienda el enunciado.

## 6. Limitaciones de la auditoría

- La carpeta contiene la versión `TFEP03.26_Plantillas.docx.md`, no el archivo binario `TFEP03.26_Plantillas.docx`; por ello no se pudo verificar visualmente el formato original, orientación de páginas, tamaño de fuentes, saltos de página o configuración de tablas.
- No se evaluaron documentos distintos de la plantilla disponible y el PDF del enunciado.
- La consistencia de los valores de probabilidad se evaluó contra las reglas y ejemplos contenidos en el propio PDF.

## 7. Estado final de auditoría

**Resultado:** avance sólido, pero con hallazgos abiertos.

**Condición observada:** no completamente listo para entrega debido principalmente a la ausencia de B.6, los campos incompletos de B.2, las diferencias de costos y las inconsistencias de R-03 y R-14 frente al método del enunciado.

## 8. Revisión de posibles trampas en el PDF del profesor

### 8.1 Trampas pedagógicas explícitas

Estas situaciones están anunciadas o demostradas directamente por el enunciado y, por tanto, deben considerarse intencionales:

| ID | Ubicación | Información encontrada | Efecto esperado |
|---|---|---|---|
| T-01 | Enunciado, sección 3.2 y sección 6.5 | BA-4 está resuelta como ejemplo y se indica expresamente que no cuenta para A.1 ni debe aparecer en el registro. | Evitar incluir BA-4 entre las diez cláusulas o entre los quince riesgos. |
| T-02 | Enunciado, secciones 7.2 y 7.4 | A.1 exige exactamente diez cláusulas y A.3 exactamente quince riesgos. | No marcar las dieciséis cláusulas ni entregar más de quince riesgos. |
| T-03 | Enunciado, sección 7.2 | A.1 pide identificar lo que no está dicho y prohíbe proponer soluciones en esa etapa. | Separar la lectura adversarial de la respuesta al riesgo. |
| T-04 | Enunciado, secciones 5.1 y 5.2 | Las probabilidades solo pueden usar los cinco niveles indicados y los impactos deben medirse contra la utilidad esperada, no contra el monto del contrato. | No usar probabilidades intermedias ni comparar impactos con el presupuesto total. |
| T-05 | Enunciado, sección 6.2 | El impacto solo considera retrabajo, compras/servicios adicionales y multas/penalidades. Se excluyen imagen y lucro cesante. | No agregar componentes económicos que el método excluye. |
| T-06 | Enunciado, sección 6.4 | Los empates se resuelven por exposición, valor esperado, etapa de respuesta y, finalmente, decisión declarada del grupo. | No ordenar empates arbitrariamente. |
| T-07 | Enunciado, sección 8.2 | La Parte B solicita los ocho riesgos de mayor exposición, no únicamente los cinco de A.4. | No limitar las respuestas de B.2 a los cinco primeros de A.4. |
| T-08 | Enunciado, sección 8.5 | La reserva se recalcula con las respuestas de zonas crítica y alta; los riesgos medios permanecen en la reserva salvo que se declare otra decisión. | No restar automáticamente todos los valores esperados. |
| T-09 | Enunciado, sección 8.6 | B.6 debe cerrarse con una sola lámina que muestre tres riesgos, sus cambios y sus costos. | No omitir la lámina final. |
| T-10 | Enunciado, sección 5.3 | El límite `0,40` pertenece a la zona crítica porque la regla crítica usa `>= 0,40`, aunque la fila de zona alta también muestra `0,40`. | El valor exacto `0,40` debe tratarse como crítico. |

### 8.2 Contradicciones o posibles errores intencionales del PDF

Estas situaciones no están presentadas como ejemplos pedagógicos, pero son contradicciones internas del documento y podrían ser trampas colocadas deliberadamente. No deben resolverse silenciosamente como si no existieran.

| ID | Ubicación | Contradicción encontrada | Evaluación |
|---|---|---|---|
| T-11 | Página 1, tabla inicial, y sección 1.1 | La entrega de la Parte B aparece primero como envío por el `aula virtual` y luego como un PDF enviado por `correo`. | Contradicción formal del canal de entrega. |
| T-12 | Sección 2.4 y sección 4 | Se indica que las consultas cierran el día 10, el acta se publica el día 17 y la oferta se entrega el día 30. Sin embargo, después se afirma que faltan trece días para entregar y ocho días para cerrar consultas. Esas referencias temporales no pueden ser simultáneamente verdaderas. | Contradicción cronológica. |
| T-13 | Sección 7.1 | El bloque dura 90 minutos, pero la tabla asigna 1, 2, 3, 4 y 5 minutos a sus cinco actividades y deja vacío el total. Los valores suman 15 minutos, no 90. | Inconsistencia evidente de planificación. |
| T-14 | Página 1 y encabezados/pies del documento | El nombre del archivo utiliza `TFEP03.26`, mientras el documento identifica el material como `FEP04.1.26`. | Inconsistencia de identificación documental; no se puede confirmar si es deliberada. |

## 9. Contradicciones nuevas detectadas en la plantilla

### T-15 - Distribución de etapas inconsistente

**Ubicación:** Plantilla, secciones 6.1, 6.2 y 6.3.

Las etapas declaradas en las respuestas detalladas no coinciden con el resumen de distribución:

- R-12 figura como `Implementación` en la respuesta detallada, pero aparece como `Propuesta` en el resumen.
- R-14 figura como `Propuesta`, pero aparece como `Implementación` en el resumen.
- R-04 figura como `Implementación`, pero aparece como `Propuesta` en el resumen.
- R-06 figura como `Implementación`, pero aparece como `Propuesta` en el resumen.
- R-15 figura como `Propuesta`, pero aparece como `Implementación` en el resumen.

Por esta diferencia, el resumen declara 9 acciones en propuesta y 5 en implementación, mientras que las filas detalladas contabilizan 8 en propuesta y 6 en implementación, además de 1 en implantación.

### T-16 - Desempate entre R-08 y R-15

**Ubicación:** Plantilla, sección 5; enunciado, sección 6.4.

R-08 y R-15 tienen la misma exposición y el mismo valor esperado. La plantilla ubica R-08 antes que R-15, pero sus etapas detalladas son respectivamente `Implementación` y `Propuesta`. Según la regla de desempate del enunciado, la acción en etapa de propuesta debe preceder a la de implementación.

### T-17 - Estrategia de R-12 frente a su zona

**Ubicación:** Plantilla, R-12 en las secciones 5 y 6.1; enunciado, sección 5.3.

R-12 es crítico, pero la respuesta lo rotula como `Mitigar / EDT`. La regla de zona crítica exige cambio de diseño, eliminación de la causa o decisión de no ofertar. El contenido de la acción modifica hardware y layouts, pero la etiqueta de estrategia no coincide con la regla aplicada.

## 10. Conclusión sobre las trampas

Sí existen trampas claramente intencionales en el PDF: BA-4 como ejemplo excluido, cantidades exactas de entregables, escalas cerradas, diferencia entre cinco y ocho riesgos, regla de recálculo, tratamiento del valor `0,40` y exigencia de B.6.

También existen al menos tres contradicciones internas no resueltas por el documento: el canal de entrega de la Parte B, las fechas relativas de consultas y el reparto de los 90 minutos. El PDF no declara que esas contradicciones sean ejercicios de análisis, por lo que su intencionalidad no puede confirmarse; objetivamente deben tratarse como ambigüedades formales del material.

La plantilla reproduce algunas de esas zonas sensibles y agrega inconsistencias propias en las etapas, los desempates y las estrategias de zona crítica.
