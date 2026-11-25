# Simulacro 2 - Alta dificultad

Este banco cubre exclusivamente lo indicado por el profesor:

- Capítulo 5: procesos, salidas centrales, EDT, Validar el Alcance y Controlar la Calidad.
- Capítulo 6: relaciones lógicas, ruta crítica, holguras, compresión y optimización de recursos.
- Capítulo 8: calidad frente a grado, procesos y costo de la calidad.
- Capítulo 11: procesos, respuestas, valor esperado, árbol de decisión y reservas.

## Instrucciones

1. En las preguntas 1 a 24 marca una alternativa entre A y E.
2. Justifica cada respuesta en dos a cuatro líneas. Marcar sin desarrollar no entrena el formato anunciado por el profesor.
3. En las preguntas 25 a 32 muestra fórmulas, reemplazo, resultado con unidad y conclusión.
4. Algunas preguntas contienen alternativas combinadas. No supongas que “todas las anteriores” o “ninguna de las anteriores” son automáticamente correctas o falsas.
5. No revises la pauta hasta terminar una sección completa.

---

# Parte A - Selección múltiple aplicada

## Capítulo 5 - Gestión del Alcance

### 1

Durante talleres y entrevistas, el equipo documenta necesidades detalladas y registra vínculos bidireccionales entre cada necesidad, su entregable y la prueba que demostrará su cumplimiento. ¿Qué combinación proceso-salidas describe mejor el trabajo?

A. Planificar la Gestión del Alcance - plan de gestión del alcance y plan de gestión de los requisitos.  
B. Recopilar Requisitos - documentación de requisitos y matriz de trazabilidad de requisitos.  
C. Definir el Alcance - enunciado del alcance y matriz de trazabilidad de requisitos.  
D. Crear la EDT - línea base del alcance y documentación detallada de requisitos.  
E. Todas las combinaciones anteriores describen salidas centrales del proceso señalado.

### 2

Después de aprobarse el alcance, el director solicita identificar exactamente los componentes de la línea base del alcance. ¿Cuál lista es correcta?

A. Enunciado del alcance, documentación de requisitos y matriz de trazabilidad.  
B. Acta de constitución, EDT y diccionario de la EDT.  
C. Plan de gestión del alcance, enunciado del alcance y EDT.  
D. Enunciado del alcance aprobado, EDT y diccionario de la EDT.  
E. EDT, línea base del cronograma y línea base de costos.

### 3

Dentro de una cuenta de control se conoce que habrá una migración histórica, pero todavía no existe información suficiente para descomponerla y estimarla como trabajo ejecutable. ¿Cómo debe nombrarse ese componente mientras se detalla progresivamente?

A. Actividad de duración indeterminada.  
B. Paquete de trabajo provisional.  
C. Paquete de planificación.  
D. Entregable aceptado condicionalmente.  
E. Cuenta de control subordinada.

### 4

Evalúa las afirmaciones sobre la regla del 100 %:

I. La EDT debe representar todo el trabajo del producto y de gestión necesario para completar el proyecto.  
II. Los componentes hijos deben representar el 100 % del trabajo contenido en su componente padre.  
III. La EDT no debe incorporar trabajo ajeno al alcance aprobado.

A. Solo I es correcta.  
B. Solo I y II son correctas.  
C. Solo II y III son correctas.  
D. Solo I y III son correctas.  
E. I, II y III son correctas.

### 5

Un módulo supera las pruebas técnicas definidas, pero el usuario rechaza su recepción porque omite un flujo clínico incluido en los requisitos aprobados. ¿Cuál interpretación es más precisa?

A. Controlar la Calidad pudo verificar criterios técnicos, pero Validar el Alcance no debe aceptar el módulo; corresponde rastrear el requisito y corregir la no conformidad antes de presentarlo nuevamente.  
B. Validar el Alcance debe aceptar el módulo porque un entregable verificado se convierte automáticamente en entregable aceptado, aunque falte un flujo aprobado.  
C. Controlar la Calidad solo puede ejecutarse después de la aceptación, porque la inspección técnica depende de que el usuario confirme primero la utilidad operacional.  
D. Controlar el Alcance debe modificar inmediatamente la línea base para eliminar el flujo omitido, porque las pruebas técnicas ya demostraron la conformidad del producto.  
E. Gestionar la Calidad debe emitir la aceptación formal del módulo, porque ese proceso integra las auditorías internas con la aprobación de los interesados.

### 6

Con la línea base vigente, un patrocinador solicita una función adicional y afirma que “no debería tomar mucho”. ¿Cuál actuación mantiene correctamente el control del alcance?

A. Incorporar la función a la EDT y después calcular si el incremento requiere autorización formal.  
B. Rechazar la función, porque una línea base aprobada no puede modificarse durante la ejecución.  
C. Registrar y analizar la solicitud; solo después de su aprobación actualizar las líneas base y documentos afectados.  
D. Tratar la función como paquete de planificación hasta que el equipo determine su esfuerzo definitivo.  
E. Pedir a Controlar la Calidad que verifique la función antes de decidir si pertenece al alcance aprobado.

---

## Capítulo 6 - Gestión del Cronograma

### 7

La capacitación puede comenzar tres días después de iniciado el despliegue, sin importar si este ha terminado. ¿Cómo se representa la relación?

A. FS+3: la capacitación comienza tres días después del término del despliegue.  
B. SS+3: la capacitación comienza tres días después del inicio del despliegue.  
C. FF+3: la capacitación termina tres días después del término del despliegue.  
D. SF-3: la capacitación termina tres días antes del inicio del despliegue.  
E. Todas las relaciones anteriores expresan la misma restricción con distinta notación.

### 8

Una actividad B estaba vinculada con A mediante `FS+5`. Después de revisar la necesidad real de espera, el equipo utiliza `FS+2`, sin alterar las duraciones. ¿Qué modificación realizó?

A. Redujo la duración de B en tres unidades y conservó intacta la dependencia.  
B. Incorporó un adelanto de tres unidades y convirtió la relación en Inicio-Inicio.  
C. Aplicó intensificación, porque toda reducción del plazo supone aumentar recursos.  
D. Eliminó una dependencia obligatoria y la reemplazó por una dependencia externa.  
E. Redujo el retraso asociado a la relación en tres unidades, siempre que la lógica del trabajo lo permita.

### 9

Una actividad presenta ES = 8, EF = 14, LS = 11 y LF = 17. ¿Cuál conclusión es correcta?

A. Tiene seis días de holgura porque su duración es `14-8`.  
B. Tiene nueve días de holgura porque su término tardío es 17.  
C. Tiene cero días de holgura porque `EF-ES` coincide con `LF-LS`.  
D. Tiene tres días de holgura y, bajo las condiciones actuales, no es crítica.  
E. Ninguna es correcta porque la holgura solo puede calcularse con la ruta completa.

### 10

El gerente necesita reducir la fecha final sin incorporar recursos. El equipo descubre que parte del diseño y la construcción se mantenían secuenciales por preferencia, no por una restricción técnica. ¿Qué acción es más coherente?

A. Nivelar recursos sobre actividades no críticas hasta que desaparezca toda holgura disponible.  
B. Intensificar actividades críticas reemplazando recursos actuales por otros de igual costo.  
C. Aplicar ejecución rápida sobre la dependencia discrecional crítica, aceptando mayor riesgo de retrabajo.  
D. Suavizar recursos sobre actividades críticas, aunque con ello se exceda la holgura total disponible.  
E. Todas las anteriores reducen necesariamente la duración sin agregar recursos.

### 11

Dos actividades requieren a la misma especialista durante la misma semana. Una de ellas posee cuatro días de holgura y puede desplazarse tres días sin cambiar la ruta crítica ni la fecha final. ¿Qué técnica se está aplicando?

A. Suavizamiento de recursos, porque el ajuste permanece dentro de la holgura disponible.  
B. Nivelación de recursos, porque toda reasignación de una persona modifica necesariamente la línea base.  
C. Ejecución rápida, porque las actividades dejan de ejecutarse simultáneamente.  
D. Intensificación, porque el conflicto se resuelve modificando la disponibilidad del recurso.  
E. Ninguna de las anteriores, porque optimizar recursos exige recalcular primero el presupuesto.

### 12

Un proyecto tiene dos rutas críticas de igual duración. El director propone reducir dos días una actividad que pertenece exclusivamente a una de ellas. ¿Qué conclusión es más rigurosa?

A. El proyecto se acorta dos días porque toda actividad crítica determina por sí sola la fecha final.  
B. El proyecto se acorta un día porque la reducción se reparte entre las dos rutas críticas existentes.  
C. La segunda ruta adquiere dos días de holgura porque no recibió ninguna intervención directa.  
D. La fecha puede permanecer igual porque la otra ruta crítica continúa determinando el término.  
E. Todas las conclusiones son posibles sin necesidad de recalcular la red.

---

## Capítulo 8 - Gestión de la Calidad

### 13

Una clínica compra un monitor básico, con pocas funciones, que satisface consistentemente todas las especificaciones contratadas. Otro monitor tiene más funciones, pero falla repetidamente en precisión. ¿Qué afirmación es correcta?

A. El primer monitor tiene bajo grado y baja calidad; el segundo tiene alto grado y alta calidad.  
B. El primer monitor tiene alta calidad y alto grado; el segundo tiene baja calidad y bajo grado.  
C. El primer monitor puede tener bajo grado y alta calidad; el segundo puede tener alto grado y baja calidad.  
D. Ambos tienen igual calidad, porque el grado determina únicamente el precio y no el cumplimiento.  
E. Todas las afirmaciones anteriores pueden ser correctas según la percepción del comprador.

### 14

Durante la ejecución se audita el proceso de revisión de código, se detectan prácticas inconsistentes y se propone una mejora para evitar recurrencias. ¿Qué proceso describe mejor la situación?

A. Planificar la Gestión de la Calidad, porque se están definiendo métricas antes de iniciar el proyecto.  
B. Gestionar la Calidad, porque se examina y mejora el proceso utilizado para producir resultados.  
C. Controlar la Calidad, porque se inspecciona un entregable terminado contra sus especificaciones.  
D. Validar el Alcance, porque se busca la aceptación formal de una mejora de proceso.  
E. Controlar el Alcance, porque una práctica inconsistente equivale a una variación de la línea base.

### 15

Una organización incurre en los siguientes costos: capacitación preventiva, inspección de entregables, retrabajo antes de liberar y garantía por fallas en producción. ¿Cuál secuencia de clasificación es correcta?

A. Evaluación - prevención - falla externa - falla interna.  
B. Prevención - falla interna - evaluación - falla externa.  
C. Prevención - evaluación - falla externa - falla interna.  
D. Evaluación - prevención - falla interna - falla externa.  
E. Prevención - evaluación - falla interna - falla externa.

### 16

El equipo propone eliminar las revisiones preventivas y conservar únicamente las pruebas finales para reducir costos. ¿Cuál evaluación es más adecuada?

A. Prevención y evaluación son costos de conformidad; reducir prevención puede aumentar defectos y costos de falla, aunque las pruebas finales continúen siendo necesarias.  
B. Prevención es costo de no conformidad y evaluación es costo de conformidad; eliminar prevención reduce directamente el costo total esperado.  
C. Prevención y evaluación son costos de falla interna; mantener solo pruebas finales traslada todas las fallas al proveedor.  
D. Prevención es costo de conformidad y evaluación es falla externa; eliminar revisiones evita pagar dos veces por la misma actividad.  
E. Ninguna es correcta, porque el costo de la calidad incluye únicamente fallas detectadas después de la entrega.

### 17

Un proceso permanece estable durante varias semanas: ningún punto supera sus límites de control. Sin embargo, todas las mediciones exceden el máximo contractual aceptado por el cliente. ¿Cuál conclusión corresponde?

A. El proceso es capaz, porque mantenerse dentro de los límites demuestra cumplimiento contractual.  
B. El proceso está fuera de control, porque los límites de especificación sustituyen a los límites estadísticos.  
C. El producto debe aceptarse, porque una causa común no puede producir una no conformidad contractual.  
D. El proceso puede estar estable, pero no ser capaz de cumplir la especificación del cliente.  
E. Todas son correctas si el promedio permanece constante durante el período observado.

### 18

Una inspección detecta doce defectos en un módulo antes de entregarlo. El equipo los corrige y una nueva inspección confirma conformidad. ¿Qué combinación es más precisa?

A. Gestionar la Calidad - entregable aceptado - costo de evaluación por toda la corrección.  
B. Validar el Alcance - entregable verificado - costo de falla externa por los defectos.  
C. Controlar la Calidad - entregable verificado - evaluación por inspeccionar y falla interna por retrabajar.  
D. Planificar la Calidad - entregable aceptado - prevención por corregir antes de liberar.  
E. Controlar el Alcance - entregable validado - falla externa porque el módulo ya estaba construido.

---

## Capítulo 11 - Gestión de los Riesgos

### 19

¿Cuál secuencia representa correctamente los siete procesos de Gestión de los Riesgos del Proyecto?

A. Planificar la gestión; identificar; análisis cualitativo; análisis cuantitativo; planificar respuestas; implementar respuestas; monitorear riesgos.  
B. Identificar; planificar la gestión; análisis cuantitativo; análisis cualitativo; implementar respuestas; planificar respuestas; monitorear riesgos.  
C. Planificar la gestión; identificar; análisis cuantitativo; análisis cualitativo; planificar respuestas; monitorear riesgos; implementar respuestas.  
D. Planificar la gestión; análisis cualitativo; identificar; análisis cuantitativo; implementar respuestas; planificar respuestas; monitorear riesgos.  
E. Todas son aceptables porque los siete procesos carecen de una relación lógica definida.

### 20

Para una amenaza de daño financiero, la empresa compra una póliza. La póliza no reduce la probabilidad del incidente, pero obliga a un tercero a cubrir la pérdida económica definida. ¿Qué estrategia predomina?

A. Evitar, porque la empresa elimina completamente la causa que originaba la amenaza.  
B. Mitigar, porque la probabilidad se mantiene y la empresa reduce internamente el impacto técnico.  
C. Aceptar activamente, porque se reserva dinero propio para responder cuando ocurra el incidente.  
D. Transferir, porque un tercero asume contractualmente parte del impacto financiero.  
E. Todas las estrategias anteriores describen por igual la contratación de una póliza.

### 21

Existe una oportunidad de automatización que podría reducir considerablemente el plazo. El director asigna al mejor equipo y prioridad absoluta con el propósito explícito de asegurar que ocurra. ¿Qué estrategia aplica?

A. Mejorar, porque solo aumenta la probabilidad sin intentar asegurar el resultado.  
B. Explotar, porque busca garantizar la materialización de la oportunidad.  
C. Compartir, porque entrega la responsabilidad completa a un tercero especializado.  
D. Transferir, porque desplaza a otro equipo las consecuencias favorables del evento.  
E. Escalar, porque toda oportunidad importante debe administrarse fuera del proyecto.

### 22

Después de mitigar una amenaza permanece una exposición menor. Además, la solución de mitigación introduce la posibilidad de incompatibilidad con otro sistema. ¿Cómo se clasifican ambas exposiciones?

A. La exposición menor es secundaria y la incompatibilidad es residual.  
B. Ambas son residuales porque aparecen después de ejecutar la respuesta.  
C. Ambas son secundarias porque no estaban en la evaluación inicial.  
D. La exposición menor es aceptada y la incompatibilidad queda fuera del registro.  
E. La exposición menor es residual y la incompatibilidad es un riesgo secundario.

### 23

¿Qué afirmación distingue correctamente las reservas?

A. Contingencia cubre desconocidos y queda fuera de la línea base; gestión cubre identificados y queda dentro.  
B. Ambas cubren riesgos identificados, pero gestión se asigna únicamente a actividades críticas.  
C. Contingencia cubre riesgos identificados y pertenece a la línea base; gestión cubre trabajo imprevisto y queda fuera de ella, aunque integra el presupuesto.  
D. Contingencia es utilidad del proveedor y gestión es presupuesto reservado para control de calidad.  
E. Ninguna es correcta porque las reservas solo se calculan después de materializarse el riesgo.

### 24

Los resultados indicados ya son netos. La alternativa X ofrece 60 % de probabilidad de ganar $18 millones y 40 % de perder $6 millones. La alternativa Y ofrece 80 % de ganar $12 millones y 20 % de perder $3 millones. Según el valor monetario esperado, ¿qué corresponde?

A. Elegir Y: su EMV es $9,0 millones, superior en $0,6 millones al de X.  
B. Elegir X: su EMV es $10,8 millones, superior en $1,8 millones al de Y.  
C. Elegir Y: su EMV es $9,6 millones, superior en $1,2 millones al de X.  
D. Elegir X: su EMV es $8,4 millones, superior en $0,6 millones al de Y.  
E. Ninguna: ambas alternativas tienen un EMV de $8,4 millones.

---

# Parte B - Desarrollo y cálculo

## Capítulo 5

### 25. Procesos, salidas y aceptación

Un hospital inicia un proyecto para incorporar una plataforma de telemedicina. Durante el proyecto ocurren estos hechos:

- Se define cómo se documentará, aprobará y controlará el alcance.
- Se realizan entrevistas y se vinculan requisitos con pruebas.
- Se establecen inclusiones, exclusiones y criterios de aceptación.
- El trabajo se descompone hasta paquetes gestionables.
- Un módulo supera las pruebas técnicas y luego se presenta al representante clínico.
- Después de aprobar la línea base, se solicita agregar grabación de consultas.

Responde:

a. Escribe los seis procesos del capítulo 5 en orden y la salida central de cada uno.  
b. Explica el recorrido desde entregable terminado hasta entregable aceptado, distinguiendo Controlar la Calidad de Validar el Alcance.  
c. Indica cómo debe gestionarse la grabación solicitada y qué no debería modificarse antes de su aprobación.

### 26. Diagnóstico de una EDT

Un equipo construye una EDT cuyo primer nivel son las fases del ciclo de vida. Dentro de ella dibuja flechas de precedencia entre paquetes, denomina “actividad” a todo componente inferior y detiene automáticamente la descomposición en 200 horas. El avance se informa cada dos semanas. Además, deja fuera el trabajo de gestión porque “no produce software”.

Analiza cada decisión indicando:

a. Qué elementos pueden ser válidos y bajo qué condición.  
b. Qué elementos son incorrectos y por qué.  
c. Cómo deberían utilizarse los términos cuenta de control, paquete de planificación, paquete de trabajo y actividad.  
d. Qué regla de la EDT se vulnera al excluir la gestión.

---

## Capítulo 6

### 27. Red con relaciones mixtas

Considera la siguiente red, medida en semanas:

| Actividad | Duración | Relación |
|---|---:|---|
| A | 4 | Inicio del proyecto |
| B | 6 | FS con A |
| C | 7 | SS+2 con B |
| D | 5 | FS con B |
| E | 4 | FS con C y FS+1 con D |
| F | 3 | FF con E |
| G | 2 | FS con E |

Responde:

a. Calcula inicio y término tempranos de todas las actividades.  
b. Determina la duración del proyecto y la secuencia que controla su término.  
c. Durante la ejecución, B aumenta de 6 a 8 semanas sin cambiar su fecha de inicio. Recalcula la fecha final.  
d. Explica por qué el aumento de B afecta de manera diferente a C y D.  
e. Concluye en qué semana termina el proyecto después del cambio.

### 28. Holguras y optimización de recursos

| Actividad | Duración | Predecesora |
|---|---:|---|
| A | 3 días | - |
| B | 6 días | A |
| C | 5 días | A |
| D | 4 días | B |
| E | 7 días | C |
| F | 2 días | D y E |

Responde:

a. Calcula la duración, rutas y holguras totales.  
b. Una misma especialista debe ejecutar B y C, por lo que no pueden superponerse. Calcula la fecha final si se ejecuta primero C y luego B.  
c. Calcula la fecha final si se ejecuta primero B y luego C.  
d. Elige el orden de nivelación menos perjudicial y explica por qué esto no es suavizamiento.  
e. Diferencia fast tracking de crashing e indica sobre qué actividades tendría sentido evaluarlos.

---

## Capítulo 8

### 29. Costo de la calidad y grado

Un proyecto registra:

- $2 millones en capacitación preventiva.
- $3 millones en inspecciones y pruebas.
- $4 millones en retrabajo antes de liberar.
- $6 millones en garantías por fallas detectadas en producción.

Responde:

a. Clasifica cada costo.  
b. Calcula costo de conformidad, costo de no conformidad y costo total de la calidad.  
c. Explica cuál habría sido potencialmente más conveniente reducir y mediante qué tipo de inversión.  
d. El producto pertenece a una categoría básica, pero cumple todos sus requisitos. Determina si eso implica baja calidad y justifica.

### 30. Los tres procesos y la aceptación

Durante un proyecto ocurren los siguientes eventos:

1. Se determinan métricas de disponibilidad, tiempos de respuesta y tolerancias.
2. Una auditoría detecta que los equipos aplican criterios distintos para revisar código.
3. Una prueba mide 4,8 segundos cuando el máximo aceptable es 3 segundos.
4. Tras corregir el defecto, una nueva prueba confirma 2,7 segundos.
5. El cliente revisa el flujo completo y firma la recepción.

Responde:

a. Asocia cada evento con Planificar, Gestionar o Controlar la Calidad; si corresponde a otro capítulo, indícalo.  
b. Identifica cuándo existe un entregable verificado y cuándo uno aceptado.  
c. Explica por qué un proceso podría estar estadísticamente estable y aun así no cumplir los 3 segundos.  
d. Clasifica el retrabajo realizado antes de la recepción dentro del costo de la calidad.

---

## Capítulo 11

### 31. Árbol de decisión

Una empresa debe elegir una estrategia cuyos resultados ya están expresados como beneficios o pérdidas netas:

- **Alternativa A:** 65 % de probabilidad de obtener $18 millones y 35 % de probabilidad de perder $12 millones.
- **Alternativa B:** 85 % de probabilidad de obtener $11 millones y 15 % de probabilidad de perder $5 millones.

Responde:

a. Dibuja el árbol de decisión.  
b. Calcula el EMV de cada alternativa.  
c. Selecciona una alternativa según EMV e indica la diferencia monetaria esperada.  
d. Explica por qué la decisión final podría considerar también la tolerancia al riesgo, aunque el EMV favorezca una alternativa.

### 32. Respuestas y reservas

La estimación base, sin reservas, es de $100 millones. Después de aplicar respuestas, permanecen estos riesgos:

- R1: 25 % de probabilidad de perder $12 millones.
- R2: 10 % de probabilidad de perder $20 millones.
- O1: 40 % de probabilidad de ahorrar $5 millones.

La política de la organización establece:

- La contingencia se calcula sumando los EMV negativos residuales, sin descontar oportunidades.
- La reserva de gestión equivale al 10 % de la línea base de costos resultante.

Además, una póliza transfiere parte de R2; permanece una exposición menor y aparece el riesgo de que la aseguradora rechace el siniestro por documentación incompleta.

Responde:

a. Calcula el EMV individual y el EMV neto de los tres riesgos.  
b. Calcula la reserva de contingencia, la línea base de costos, la reserva de gestión y el presupuesto total.  
c. Clasifica la exposición que permanece después de transferir R2 y el riesgo introducido por la póliza.  
d. Indica a qué procesos pertenecen la planificación, ejecución y seguimiento de estas respuestas.  
e. Concluye por qué contingencia y gestión no deben tratarse como una única reserva.

