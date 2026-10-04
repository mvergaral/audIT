# Subdocumento 7. Plan de trabajo, EDT, cronograma e implantación

audIT, Empresa N.º 10. Licitación TFEP-01/2026, Caso 10 Transporte de Carga. Oferta Técnica, Sobre N.º 2. Informe Preparatorio 2. Archivo AUDIT-Subdocumento7.pdf. Anexos: Formulario T-14 en el archivo AUDIT-Formulario-T-14.pdf, Formulario T-15 en el archivo AUDIT-Formulario-T-15.pdf, Formulario T-18 en el archivo AUDIT-Formulario-T-18.pdf.

## 7 Introducción al Plan de Trabajo

Este capítulo presenta la estructura de descomposición del trabajo, el plan de trabajo con sus
frentes paralelos y el cronograma con la ruta crítica, la implantación y las dos marchas blancas.
Sigue el cronograma contractual del FEP01, Artículo 17.1, p. 12, que fija la Etapa 1 entre los meses 1 y 16, la
Etapa 2 entre los meses 13 y 21 y la operación entre los meses 21 y 56.
**[Información requerida por dupla 2: resumen del capítulo y coherencia con el marco metodológico del Subdocumento 6]**

Los formularios T-14, T-15 y T-18 acompañan este capítulo como archivos propios, conforme al
Comunicado 10, sección 1. El Formulario T-15 trae la asignación de capacidad por rol en los meses
13 a 15 y la malla completa de precedencias con sus holguras.

## 7.1 EDT

**[Información requerida por dupla 2: estructura de descomposición del trabajo con el 100 % del alcance y resumen
analítico del Diccionario de la EDT del Formulario T-14]**

## 7.2 Plan de trabajo

**[Información requerida por dupla 2: párrafo de apertura del plan de trabajo]**

### 7.2.1 Alineación con las metodologías

**[Información requerida por dupla 2: alineación con las metodologías del Subdocumento 6]**

### 7.2.2 Secuenciamiento y estimación del esfuerzo

**[Información requerida por dupla 2: secuenciamiento y estimación del esfuerzo]**

### 7.2.3 Partición de la capacidad de ingeniería en el solapamiento de los meses 13 a 15

Entre los meses 13 y 15 ocurren a la vez la marcha blanca de la Etapa 1 y el desarrollo de la
Etapa 2 (FEP01, Artículo 17.1, p. 12). El FEP01, Artículo 17.2, p. 13 pide demostrar en el Formulario T-15 que la
dotación y los frentes de trabajo alcanzan para ambos esfuerzos. audIT divide el equipo en dos
escuadras de composición fija durante los tres meses. La Escuadra de Estabilización E1 sostiene la
marcha blanca y la Escuadra de Construcción E2 desarrolla la Etapa 2. Cada escuadra tiene su líder,
su tablero de trabajo y su reunión diaria. Se forman con personas de las células Alfa, Beta y Gamma
descritas en el Subdocumento 1 y con el refuerzo del proyecto que declara el Formulario T-15. La
Tabla 7.1 resume las dos escuadras y la capacidad que queda para coordinarlas.

**Tabla 7.1.** Escuadras del solapamiento de los meses 13 a 15

| Escuadra | Conduce | Capacidad | Responde por |
|---|---|---|---|
| Estabilización E1 | Líder de Operación / SRE | 21,5 FTE: 19 personas dedicadas y parte de siete roles de dirección | Marcha blanca, incidentes de nivel 3, conciliación diaria, presencia en terminales y transferencia al mandante |
| Construcción E2 | Líder de Desarrollo | 14,1 FTE: 11 personas dedicadas y parte de siete roles de dirección | Diseño detallado, construcción en sprints y entrega para pruebas de la Etapa 2 |
| Coordinación | Jefe de Proyecto | 1,4 FTE: el 20 % de siete roles de dirección | Dependencias y datos que comparten las dos escuadras |

*Fuente: elaboración propia. El detalle por rol está en el Formulario T-15.*

Las 37 personas del equipo suman 37,0 FTE: 21,5 en E1, 14,1 en E2 y 1,4 de coordinación. E1 tiene
7,4 FTE más que E2 porque la marcha blanca se sostiene en cinco terminales a la vez, de madrugada y
con guardia 24x7.

**Regla de asignación.**
Quien reparte su jornada entre dos frentes pierde tiempo en cada cambio de contexto.
Weinberg (1992) estima esa pérdida en 20 % del tiempo productivo cuando una persona pasa de
uno a dos proyectos simultáneos. Rubinstein et al. (2001) midieron que el costo de cambiar de tarea
crece con la complejidad de las reglas de cada tarea. Por eso los ingenieros, analistas y
desarrolladores pertenecen a una sola escuadra durante el solapamiento. Solo se reparten siete roles
de dirección que responden por las dos etapas: Jefe de Proyecto, Arquitecto de Solución, Encargado de
Seguridad de la Información, Líder de Calidad y Pruebas, Líder de Datos, Líder Funcional y Líder de
Integración. Cada uno asigna 80 % de su jornada a las escuadras y deja el 20 % restante sin trabajo
planificado para coordinar entre ellas, así que nadie supera el 100 % de su jornada.

**Decisión D-01. Dos escuadras de composición fija en los meses 13 a 15**

| Se decide | Se descarta | Criterio | Fuente |
|---|---|---|---|
| Cada ingeniero, analista y desarrollador trabaja en una sola escuadra. Solo siete roles de dirección se reparten, al 80 % | Repartir a los mismos ingenieros entre la marcha blanca y el desarrollo según la urgencia de cada semana | Pérdida por cambio de contexto y ninguna persona sobre el 100 % de su jornada | FEP01, Artículo 17.2, p. 13 |

**Escuadra de Estabilización E1.**
La conduce el Líder de Operación / SRE, que las bases exigen desde el mes 6 y en forma permanente en
la Operación (FEP02, numeral 19.2, p. 33). Responde por la marcha blanca con datos y usuarios reales,
medición diaria de indicadores y plan de reversión activo (FEP01, Artículo 17.1, p. 12). Corrige los incidentes de
nivel 3 sobre el software de la Etapa 1 con ingenieros que participaron en su construcción. Lleva la
conciliación diaria con los registros vigentes, que es condición de cierre de la marcha blanca
(FEP01, Artículo 17.3, p. 13). Mantiene presencia en los cinco terminales en el horario de relevo, que es de
madrugada (Caso, numeral 13.3, p. 27). También transfiere la operación al equipo de tecnologías de información
del mandante, que tiene 9 personas para 5 terminales y 2 talleres (Caso, numeral 7.4, p. 16).

El tamaño de E1 sale de dos cálculos, uno para la guardia y otro para el terreno. La torre de
programación opera en turnos 24x7 con 22 personas (Caso, numeral 2.4, p. 7), así que un incidente de la
Etapa 1 puede ocurrir a cualquier hora. Ocho ingenieros de E1 forman la rotación de guardia: el Líder
de Operación / SRE, los dos ingenieros SRE / DevOps y los ingenieros de software, frontend, datos,
firmware y telecomunicaciones. Ocho es el mínimo que Beyer et al. (2016) indican para una rotación
24x7 de un solo sitio con turnos semanales de guardia primaria y secundaria. Así cada ingeniero queda
de guardia una semana al mes, el 25 % de su tiempo. En terreno, cinco terminales por siete días
suman 35 turnos de relevo por semana. Un analista cubre cinco turnos semanales, de modo que se
necesitan 7 analistas de implantación en terreno. El cálculo supone que hay relevos todos los días en
los cinco terminales. Los analistas se incorporan en el mes 10 para capacitar a los conductores
(actividad A13 de la red) y siguen en E1 hasta el fin de la estabilización posterior al paso a
producción (actividad A21, 30 días hábiles, meses 16 y 17), que el Caso pide declarar con dotación y
duración (Caso, numeral 13.3, p. 27).

> **Compromiso C-01.** audIT mantiene un analista de implantación en cada terminal en el horario de relevo, todos los días, durante la marcha blanca y la estabilización de la Etapa 1.
>
> Métrica: 35 turnos de relevo por semana cubiertos en los cinco terminales, de la capacitación previa a la marcha blanca hasta el fin de la estabilización de la Etapa 1. Se verifica en: registro semanal de turnos firmado por el jefe de cada terminal. Fuente: Caso, numeral 13.3, p. 27.

**Escuadra de Construcción E2.**
La conduce el Líder de Desarrollo, con dedicación de 100 % en la implementación
(FEP02, numeral 19.2, p. 33). Responde por el levantamiento y el diseño detallado de la Etapa 2 (hito H8,
mes 14), la construcción en sprints de dos semanas definida en el Subdocumento 6 y la entrega del
software para pruebas (hito H9, mes 17). Tiene dos equipos. El de software suma ocho personas: el Líder
de Desarrollo, un ingeniero de software sénior, un ingeniero frontend y móvil, dos desarrolladores
full-stack, un ingeniero de datos y analítica, un analista de QA y un analista PMO que actúa como Scrum
Master. Son menos de las diez personas que la Guía de Scrum indica como tamaño habitual de un equipo
(Schwaber y Sutherland, 2020). El de firmware lo forman dos ingenieros de firmware y un ingeniero
electrónico, a cargo del escalamiento telemático. E2 planifica cada sprint con un factor de foco de
70 % sobre los días-persona disponibles, el valor por defecto que Kniberg (2015) usa para
equipos nuevos. El 15 % de cada sprint que el Subdocumento 6 reserva para deuda técnica se descuenta
de esa capacidad. Los cuatro integrantes del refuerzo de E2 entran al inicio del mes 13 y usan como
inducción los 36 días hábiles del diseño detallado (actividad A17), antes del primer sprint.

**Interfaz entre escuadras.**
Las dos escuadras trabajan sobre un solo repositorio y un solo pipeline con las mismas puertas de
calidad. Una corrección de E1 tiene prioridad de despliegue sobre una funcionalidad de E2. En la
reunión semanal de impedimentos del Subdocumento 6, el Jefe de Proyecto, el Arquitecto de Solución y
los dos líderes de escuadra revisan todo cambio que toque datos compartidos por las dos etapas. Si el
cambio es de arquitectura, pasa al Comité de Arquitectura. El objetivo es llegar a los meses 19 y 20
con una única fuente de verdad (FEP01, Artículo 17.2, p. 13). Si la Etapa 2 se atrasa, no se trasladan personas de
E1 a E2 durante el solapamiento, porque sumar gente a un desarrollo atrasado lo atrasa más
(Brooks, 1975). El atraso se absorbe con la reserva de cronograma de la Etapa 2 (actividad
A23, sección 7.3.1) y con la prioridad del alcance.

### 7.2.4 Solapamiento de los meses 19 y 20

**[Información requerida por dupla 2: frentes de trabajo y dotación de los meses 19 y 20, con la Etapa 1 en producción y la
Etapa 2 en marcha blanca]**

## 7.3 Cronograma e implantación

Esta sección determina la ruta crítica de la implementación con sus holguras y presenta la carta
Gantt, el plan de implantación y el plan de las dos marchas blancas.

### 7.3.1 Ruta crítica y holguras

La red de la implementación tiene 25 actividades, desde el inicio del contrato hasta la aceptación
final del mes 21, y el Formulario T-15 trae su malla completa. Las duraciones están en días hábiles,
que es la unidad por defecto de las bases (FEP01, Artículo 10.1, p. 8). Un mes contractual equivale a 20 días
hábiles: 260 días de lunes a viernes al año, menos los feriados legales, redondeado hacia abajo. El
día 0 es el inicio del mes 1, de modo que el hito de un mes m vence el día 20 × m.

Las duraciones son estimaciones PERT de tres puntos. La duración esperada es (a + 4m + b) / 6 y la
varianza es ((b − a) / 6)² (Malcolm et al., 1959). Las dos marchas blancas y los dos pasos a
producción tienen duración fija porque la fija el FEP01, Artículo 17.1, p. 12. Las actividades que cierran un hito
incluyen los 10 días hábiles que el mandante tiene para revisar el entregable (FEP01, Artículo 18.3, p. 13). La
holgura total es el inicio tardío menos el inicio temprano. La holgura libre es el menor inicio
temprano de los sucesores menos el término temprano (Project Management Institute, 2019).

La Figura 7.1 muestra la red de la Etapa 1 hasta el inicio de la marcha blanca, y la
Figura 7.2 el solapamiento de los meses 13 a 15 y la Etapa 2.

![Figura 7.1. Red PERT de la Etapa 1 hasta el inicio de la marcha blanca, con la ruta crítica en rojo](../../figuras/07-plan-trabajo/pert-etapa1.pdf)

*Figura 7.1. Red PERT de la Etapa 1 hasta el inicio de la marcha blanca, con la ruta crítica en rojo*

Fuente: Elaboración propia.

La fila central de la figura es la ruta crítica. Arriba y abajo corren las actividades que dependen
del terreno y de terceros: la cobertura móvil, la factibilidad con los proveedores de posicionamiento,
la adhesión de los transportistas y el piloto a bordo.

![Figura 7.2. Red PERT del solapamiento de los meses 13 a 15 y de la Etapa 2, con la ruta crítica en rojo](../../figuras/07-plan-trabajo/pert-etapa2.pdf)

*Figura 7.2. Red PERT del solapamiento de los meses 13 a 15 y de la Etapa 2, con la ruta crítica en rojo*

Fuente: Elaboración propia.

La ruta sigue por la fila central. En la fila superior van la marcha blanca, la transferencia y la
estabilización de la Etapa 1, y en la inferior la instalación progresiva a bordo. Las actividades con
borde punteado vienen de la Figura 7.1.

Las dos reservas de contingencia de la ruta, A14 y A23, se calculan con la varianza de la cadena que
protegen. Cada una mide dos desviaciones estándar, redondeado al entero más cercano. La
Tabla 7.2 da el resultado, y el Formulario T-15 trae las estimaciones de tres puntos de cada
actividad.

**Tabla 7.2.** Reservas de contingencia de la ruta crítica

| Cadena | Actividades | Desviación estándar | Reserva | Probabilidad de cumplir |
|---|---|---|---|---|
| Etapa 1, hasta el inicio de la marcha blanca (día 240) | A01, A02, A05, A07, A09 y A12 | 6,89 | A14, 14 días | 97,9 % |
| Etapa 2, hasta el inicio de su marcha blanca (día 360) | A17, A20 y A22 | 5,04 | A23, 10 días | 97,6 % |

*Fuente: elaboración propia, con distribución normal sobre la suma de las actividades de cada cadena.*

La probabilidad de cumplir las dos fechas a la vez es 95,6 %. Cada ruta no crítica que converge en
A12 tiene una holgura de al menos 3,5 veces la desviación estándar de su tramo propio, así que el sesgo
por convergencia de rutas paralelas no cambia estas cifras de forma apreciable.

La Tabla 7.3 compara cada hito del FEP01, Formulario E-25, p. 74 con el día en que la red lo alcanza.

**Tabla 7.3.** Hitos del Formulario E-25 frente a la red

| Hito | Actividad | Día hábil planificado | Límite contractual | Margen |
|---|---|---|---|---|
| H1 | Fin de A02 | 38 | 40 (mes 2) | 2 |
| H2 | Fin de A05 | 76 | 80 (mes 4) | 4 |
| H3 | Fin de A07 | 112 | 120 (mes 6) | 8 |
| H4 | Fin de A09 | 192 | 200 (mes 10) | 8 |
| H5 | Fin de A12 | 226 | 240 (mes 12) | 14 |
| H6 | Inicio de A15 | 240 | 240 (inicio del mes 13) | Fecha fija |
| H8 | Fin de A17 | 276 | 280 (mes 14) | 4 |
| H7 | Fin de A19 | 310 | 320 (mes 16) | 10 |
| H9 | Fin de A20 | 326 | 340 (mes 17) | 14 |
| H10 | Fin de A22 | 350 | 360 (mes 18) | 10 |
| H11 | Inicio de A24 | 360 | 360 (inicio del mes 19) | Fecha fija |
| H12 | Fin de A25 | 420 | 420 (mes 21) | Protegido por A23 |

*Fuente: elaboración propia a partir del Formulario E-25, p. 74.*

Todos los hitos se alcanzan dentro de su mes contractual. Los inicios de las dos marchas blancas no
tienen margen porque el FEP01, Artículo 17.1, p. 12 los fija.

**Trazado de la ruta crítica.**
La ruta crítica es A01, A02, A05, A07, A09, A12, A14, A17, A20, A22, A23, A24 y A25. Sus 13
actividades tienen holgura total y libre igual a cero, y cada una tiene un solo predecesor crítico y un
solo sucesor crítico, de modo que hay una sola ruta crítica. Hasta el mes 12 recorre la cadena de la
Etapa 1 que gatilla los hitos H1 a H5. Desde el mes 13 pasa al desarrollo de la Etapa 2, que tiene seis
meses para levantar, diseñar, construir y certificar un alcance nuevo. La marcha blanca de la Etapa 1
queda fuera de la ruta porque dura tres meses fijos y después le quedan 20 días hábiles de holgura
antes de la marcha blanca de la Etapa 2. Un atraso en A09 o en A12 desplaza el inicio de A17. Como A17,
A20 y A22 no tienen holgura, ese atraso llega intacto a la marcha blanca de la Etapa 2 y al paso a
producción del mes 21. La reserva A14 absorbe hasta 14 días hábiles de atraso en la Etapa 1 antes de
afectar el mes 13. La reserva A23 absorbe hasta 10 días hábiles en la Etapa 2 antes de afectar el
mes 19.

**Holguras de las actividades no críticas.**
El FEP01, Artículo 17.1, p. 12 fija el inicio de la marcha blanca de la Etapa 1 en el mes 13, de modo que la holgura
de 20 días hábiles de A15, A19 y A21 se aplica a su cierre. Es lo que puede extenderse esa marcha
blanca, si no se cumplen las condiciones del FEP01, Artículo 17.3, p. 13, sin afectar el inicio de la marcha blanca
de la Etapa 2. La extensión corre por cuenta de audIT y no mueve las fechas de las fases siguientes. El
hito H7 del mes 16 tiene además su propio margen de 10 días hábiles, según la Tabla 7.3. Las
demás actividades no críticas absorben las restricciones físicas del Caso. El piloto a bordo (A11)
tiene 20 días hábiles de holgura y la instalación progresiva (A18) tiene 40. Un cierre del paso Los
Libertadores por nieve dura hasta 12 días corridos (Caso, numeral 13.2, p. 27), unos 9 días hábiles, de
modo que un cierre completo cabe en la holgura de ambas actividades. La adhesión de los 148
transportistas (A06) tiene 34 días hábiles de holgura libre antes de la capacitación (A13). La
verificación con los proveedores de posicionamiento (A04), que no depende de audIT, puede atrasarse 61
días hábiles sin atrasar el fin del proyecto.

**Control de la ruta.**
Reforzar la marcha blanca de la Etapa 1 no acorta el proyecto, porque no está en la ruta crítica. La
regla de asignación de la sección 7.2.3 descarta mover personas de la Etapa 1 a la
Etapa 2 durante el solapamiento. El control se ejerce sobre la ruta: el avance de cada sprint de A09 y
A20 contra su línea base y el consumo de las reservas A14 y A23. El Jefe de Proyecto informa el consumo
de cada reserva en el Comité de Proyecto quincenal del Subdocumento 6. Si una reserva baja de la mitad
cuando a su cadena le queda más de la mitad de su duración, el caso sube al Comité Ejecutivo con un
plan de recuperación.

### 7.3.2 Carta Gantt

**[Información requerida por dupla 2: carta Gantt de los 56 meses articulada con el Artículo 17 y los hitos del Formulario
E-25, con las ventanas de marcha blanca, los pasos a producción y el inicio de la Operación]**

### 7.3.3 Implantación y puesta en marcha

**[Información requerida por dupla 2: patrón de despliegue, pruebas de aceptación, pruebas de estrés y rendimiento,
métricas de éxito y protocolo de reversión]**

### 7.3.4 Marcha blanca de la Etapa 1 y de la Etapa 2

**[Información requerida por dupla 2: plan de marcha blanca de cada etapa con los criterios e indicadores de cierre del
Artículo 17.3]**

## Referencias

Beyer, B., Jones, C., Petoff, J. y Murphy, N. R. (Eds.). (2016). *Site Reliability Engineering: How Google Runs Production Systems*. O'Reilly Media. https://sre.google/sre-book/being-on-call/

Brooks, F. P. (1975). *The Mythical Man-Month: Essays on Software Engineering*. Addison-Wesley.

Kniberg, H. (2015). *Scrum and XP from the Trenches* (2.ª ed.). C4Media.

Malcolm, D. G., Roseboom, J. H., Clark, C. E. y Fazar, W. (1959). Application of a Technique for Research and Development Program Evaluation. *Operations Research*, *7*(5), 646-669. https://doi.org/10.1287/opre.7.5.646

Project Management Institute. (2019). *Practice Standard for Scheduling* (3.ª ed.).

Rubinstein, J. S., Meyer, D. E. y Evans, J. E. (2001). Executive Control of Cognitive Processes in Task Switching. *Journal of Experimental Psychology: Human Perception and Performance*, *27*(4), 763-797. https://doi.org/10.1037/0096-1523.27.4.763

Schwaber, K. y Sutherland, J. (2020). *The Scrum Guide: The Definitive Guide to Scrum: The Rules of the Game*. https://scrumguides.org/docs/scrumguide/v2020/2020-Scrum-Guide-US.pdf

Transportes Curimón S.A. (2026). *Bases administrativas para la preparación de la propuesta: Licitación Pública Internacional N.º TFEP-01/2026* (Documento FEP01).

Transportes Curimón S.A. (2026). *Bases técnicas del Caso 10, Transporte de Carga: Licitación Pública Internacional N.º TFEP-01/2026* (Documento FEP03).

Transportes Curimón S.A. (2026). *Bases técnicas transversales para la preparación de la propuesta: Licitación Pública Internacional N.º TFEP-01/2026* (Documento FEP02).

Transportes Curimón S.A. (2026). *Comunicado 10: Estructura obligatoria de las propuestas preparatorias y técnica final* (Comunicado de la licitación TFEP-01/2026).

Weinberg, G. M. (1992). *Quality Software Management. Volume 1: Systems Thinking*. Dorset House.

## Declaración de uso de IA

Conforme al Comunicado 10, sección 7.2, cada sección de este subdocumento y cada formulario asociado declara la herramienta de inteligencia artificial generativa usada, su finalidad, el nivel de uso en texto y en diagramas según la escala oficial de esa sección, y quién revisó y qué verificó. Esta declaración se consolida en el Formulario A-6.

| Sección | Herramienta | Finalidad del uso | Nivel en texto | Nivel en diagramas | Revisión humana (quién y qué verificó) |
|---|---|---|---|---|---|
| Introducción | Claude Opus 5.5 en Claude Code | Borrador de los dos párrafos de apertura desde el Artículo 17 y el Comunicado 10 | Alto | Ninguno | **[Información requerida por dupla 4: nombre, cargo y qué verificó]** |
| 7.2.3 | Claude Opus 5.5 en Claude Code | Cálculo de la dotación y de la asignación por rol con un guion, búsqueda de fuentes y borrador del texto desde las decisiones D4-61 a D4-67 | Alto | Ninguno | **[Información requerida por dupla 4: nombre, cargo y qué verificó]** |
| 7.3.1 | Claude Opus 5.5 en Claude Code y conector de Lucid | Cálculo de la red PERT y CPM con un guion, borrador del análisis y dos diagramas escritos como código para Lucid | Alto | Medio | **[Información requerida por dupla 4: nombre, cargo y qué verificó]** |
| Formulario T-15 | Claude Opus 5.5 en Claude Code | Tablas de dotación, asignación, estimaciones de tres puntos y malla generadas desde el mismo cálculo | Alto | Ninguno | **[Información requerida por dupla 4: nombre, cargo y qué verificó]** |
| 7.1, 7.2.1, 7.2.2, 7.2.4 y 7.3.2 a 7.3.4 | **[Información requerida por dupla 2: herramienta]** | **[Información requerida por dupla 2: finalidad]** | **[Información requerida por dupla 2: nivel]** | **[Información requerida por dupla 2: nivel]** | **[Información requerida por dupla 2: nombre, cargo y qué verificó]** |
| Formularios T-14 y T-18 | **[Información requerida por dupla 2: herramienta]** | **[Información requerida por dupla 2: finalidad]** | **[Información requerida por dupla 2: nivel]** | **[Información requerida por dupla 2: nivel]** | **[Información requerida por dupla 2: nombre, cargo y qué verificó]** |
