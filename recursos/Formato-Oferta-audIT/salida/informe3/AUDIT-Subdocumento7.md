# Subdocumento 7. Plan de trabajo, EDT, cronograma e implantación

audIT, Empresa N.º 10. Licitación TFEP-01/2026, Caso 10 Transporte de Carga. Oferta Técnica, Sobre N.º 2. Propuesta final. Archivo AUDIT-Subdocumento7.pdf. Anexos: Formulario T-14 en el archivo AUDIT-Formulario-T-14.pdf, Formulario T-15 en el archivo AUDIT-Formulario-T-15.pdf, Formulario T-18 en el archivo AUDIT-Formulario-T-18.pdf.

## 7 Introducción al Plan de Trabajo

> **Resumen de apertura.**
>
> Este capítulo convierte el alcance del Subdocumento 3 en trabajo con fecha, dueño y holgura. La
> implementación dura 21 meses y la operación 36, como fija el Artículo 17. El plan se ordena por lo que
> no controla audIT: el paso de cada camión por un terminal, la firma de 148 transportistas y la
> temporada de fruta, que con el inicio en febrero de 2027 cae en los meses 1 a 3, 11 a 15 y 23 a 27.
>
> **Qué recibe Transportes Curimón S.A.**
> - Una EDT de 13 elementos y 54 paquetes de trabajo que cubre el 100 % del alcance, con su diccionario en el Formulario T-14.
> - La ruta crítica calculada con PERT y CPM y una carta Gantt de 56 meses con los doce hitos del Formulario E-25.
> - La dotación mes a mes, con 37 personas en el peak de los meses 13 a 17, y su esfuerzo por etapa en el Formulario T-15.
> - El plan de implantación por proceso y por terminal, la cobertura a bordo mes a mes y los umbrales de cierre de cada marcha blanca.

Este capítulo presenta la estructura de descomposición del trabajo, el plan de trabajo con sus
frentes paralelos y el cronograma con la ruta crítica, la implantación y las dos marchas blancas.
Sigue el cronograma contractual del FEP01, Artículo 17.1, p. 12, que fija la Etapa 1 entre los meses 1 y 16, la
Etapa 2 entre los meses 13 y 21 y la operación entre los meses 21 y 56. Toma el alcance, las
capacidades y los supuestos del Subdocumento 3, en particular el inicio del contrato en febrero de 2027
(sección 3.2.6), y aplica el marco de gestión del Subdocumento 6: los paquetes que
dependen de terceros, del terreno o de un hito contractual se planifican de forma predictiva, y los
paquetes de software se construyen en iteraciones de dos semanas. El Subdocumento 8 toma de este
capítulo las actividades y holguras sobre las que calcula sus riesgos, y el Subdocumento 9 las ventanas
de prueba.

Los formularios T-14, T-15 y T-18 acompañan este capítulo como archivos propios, conforme al
Comunicado 10, sección 1. El Formulario T-14 trae el diccionario de la EDT paquete por paquete. El
Formulario T-15 trae el esfuerzo por etapa, la curva de dotación, la asignación de capacidad por rol en
los meses 13 a 15 y la malla completa de precedencias con sus holguras. El Formulario T-18 trae la
propuesta de implantación de cada etapa, la convivencia entre ambas y la reversión.

## 7.1 EDT

La EDT está orientada a entregables y no a fases: cada paquete termina en algo que el mandante puede
recibir y verificar. Sigue la regla del 100 %, según la cual la suma del trabajo de los elementos
hijos es igual al trabajo del padre, y nada queda fuera ni se cuenta dos veces
(Project Management Institute, 2019). Tiene 13 elementos de primer nivel y 54 paquetes de trabajo. La
Figura 7.3 la muestra completa.

La descomposición de segundo nivel se presenta en Figura 7.4, Figura 7.5, Figura 7.6, Figura 7.7, Figura 7.8. La ficha de aceptación de 11.2 está en Figura 7.9; la lectura de cobertura y los 42 vínculos requisito--paquete están en Figura 7.10 y Figura 7.11.

![Figura 7.3. Árbol general de la EDT: raíz y trece elementos](../../subdocumentos/07-plan-trabajo/graficos/edt-revisada/01-arbol.pdf)

*Figura 7.3. Árbol general de la EDT: raíz y trece elementos*

Fuente: Elaboración propia.

![Figura 7.4. Paquetes 1 a 3: gestión, diseño y plataforma](../../subdocumentos/07-plan-trabajo/graficos/edt-revisada/02-paquetes-1.pdf)

*Figura 7.4. Paquetes 1 a 3: gestión, diseño y plataforma*

Fuente: Elaboración propia.

![Figura 7.5. Paquetes 4 y 5: equipo y servicios Etapa 1](../../subdocumentos/07-plan-trabajo/graficos/edt-revisada/03-paquetes-2.pdf)

*Figura 7.5. Paquetes 4 y 5: equipo y servicios Etapa 1*

Fuente: Elaboración propia.

![Figura 7.6. Paquetes 6 a 8: integraciones, datos y Etapa 2](../../subdocumentos/07-plan-trabajo/graficos/edt-revisada/04-paquetes-3.pdf)

*Figura 7.6. Paquetes 6 a 8: integraciones, datos y Etapa 2*

Fuente: Elaboración propia.

![Figura 7.7. Paquetes 9 a 11: adhesión, calidad e implantación](../../subdocumentos/07-plan-trabajo/graficos/edt-revisada/05-paquetes-4.pdf)

*Figura 7.7. Paquetes 9 a 11: adhesión, calidad e implantación*

Fuente: Elaboración propia.

![Figura 7.8. Paquetes 12 y 13: innovaciones y operación](../../subdocumentos/07-plan-trabajo/graficos/edt-revisada/06-paquetes-5.pdf)

*Figura 7.8. Paquetes 12 y 13: innovaciones y operación*

Fuente: Elaboración propia.

![Figura 7.9. Ejemplo del diccionario: paquete 11.2](../../subdocumentos/07-plan-trabajo/graficos/edt-revisada/07-ejemplo.pdf)

*Figura 7.9. Ejemplo del diccionario: paquete 11.2*

Fuente: Elaboración propia.

![Figura 7.10. Trazabilidad de alcance, paquetes y evidencia](../../subdocumentos/07-plan-trabajo/graficos/edt-revisada/08-trazabilidad.pdf)

*Figura 7.10. Trazabilidad de alcance, paquetes y evidencia*

Fuente: Elaboración propia.

![Figura 7.11. Matriz de los 42 requisitos y sus paquetes asignados](../../subdocumentos/07-plan-trabajo/graficos/edt-revisada/09-matriz-requisitos.pdf)

*Figura 7.11. Matriz de los 42 requisitos y sus paquetes asignados*

Fuente: Elaboración propia.

La vista general muestra la raíz y los trece elementos de primer nivel. Las cinco láminas de detalle distribuyen los 54 paquetes sin repetir el diccionario; el entregable, la aceptación, el responsable y los meses de cada uno permanecen en el Formulario T-14. La
organización distingue gestión, diseño, plataforma, equipo a bordo, servicios, integraciones,
datos, adhesión, calidad, implantación, innovaciones y operación de 36 meses. Los paquetes 5.1 a 5.6 llevan el
nombre de los seis contextos del Subdocumento 4, de modo que cada componente de la arquitectura tiene
un solo paquete que lo construye. La adhesión es un elemento propio, con duración, responsable y riesgo,
porque el Caso exige tratarla como actividad y no como supuesto (Caso, numeral 17.5, p. 40).

La descomposición contiene los 54 paquetes del diccionario T-14, sin duplicar códigos. Los 42
códigos de T-12 tienen al menos un paquete asignado en la matriz de la Figura 7.11;
esta correspondencia de códigos no sustituye la comprobación del entregable y de su prueba de
aceptación. La Tabla 7.1 resume las demás fuentes del alcance.

**Tabla 7.1.** Fuentes de alcance y puntos de trazabilidad de la EDT

| Fuente del alcance | Elementos | Paquetes | Revisión |
|---|---|---|---|
| Requerimientos del Formulario T-12 | 42 | Matriz de la EDT | 42 vinculados |
| Contextos de la arquitectura lógica | 6 | 5.1 a 5.6 | Códigos cotejados |
| Innovaciones del Subdocumento 13 | 5 | 12.1 a 12.5 | Códigos cotejados |
| Exigencias del numeral 17.5 del Caso | 11 | Tabla siguiente | Correspondencia explícita |

*Fuente: Formulario T-12, sección 4.1.4, Subdocumento 13 y Caso, numeral 17.5, p. 40.*

La tabla resume la cobertura por familias; la correspondencia individual de cada requisito se debe verificar con el catálogo T-12 y el diccionario T-14. Algunas exigencias del Caso se desarrollan además de los requisitos del catálogo: la caracterización de la cobertura móvil en terreno (2.2), que el
Caso, RT-03.24, p. 31 prohíbe suponer, la factibilidad con proveedores y fabricantes (2.3), que no depende
de audIT, la migración con verificación documental de las vigencias (7.1) y el estudio de costo por
ruta del mes 6 (2.5), que llega antes de la renegociación de 2027.

La Tabla 7.2 desglosa las once exigencias del numeral 17.5 y localiza el trabajo que las materializa. Los paquetes comparten evidencia cuando la restricción afecta a varios frentes.

**Tabla 7.2.** Exigencias de planificación del Caso y paquetes que las desarrollan

| Exigencia | Paquetes | Evidencia planificada |
|---|---|---|
| Horizonte de 56 meses | 1.1, 13.1 a 13.4 | Gantt M1--M56 |
| Despliegue a bordo y cobertura acumulada | 4.1 a 4.3 | Curva mensual de implantación |
| Adhesión con duración, responsable y riesgo | 9.1 a 9.3 | Campaña, metas y refuerzo |
| Congelamiento, restricciones y cierre mensual | 4.2, 6.1, 11.2, 11.3 | Ventanas de implantación y Gantt |
| Cierres fronterizos por nieve | 4.1, 4.2 | Holguras A11 y A18 en la red CPM |
| Cobertura móvil medida en terreno | 2.2 | Mapa por tramo y punto de carga |
| Factibilidad con proveedores y fabricantes | 2.3 | Actas escritas de factibilidad |
| Migración documental de vigencias | 7.1 | Acta de conciliación de vigencias |
| Costo real por ruta antes de renegociar | 2.5, 5.6 | Estudio entregado a finanzas en M6 |
| Capacitación distribuida y por turnos | 11.1 | G13, capacitación y certificación |
| Solapamientos M13--M15 y M19--M20 | 1.1, 8.1 a 8.5, 11.2, 11.3 | Dotación y partición de capacidad |

*Fuente: Caso, numeral 17.5, p. 40, diccionario T-14, red T-15 y plan T-18.*

La correspondencia incorpora las restricciones operacionales al alcance asignado. La cobertura mensual, las reservas y la dotación se justifican en las secciones de implantación, ruta crítica y solapamientos de este capítulo.

El diccionario de la EDT, en el Formulario T-14, declara para cada uno de los 54 paquetes su
entregable, su criterio de aceptación, el rol responsable, la actividad de la red de la
sección 7.3.1 a la que pertenece y sus meses. La Tabla 7.3 resume el primer
nivel.

**Tabla 7.3.** Resumen del diccionario de la EDT por elemento de primer nivel

| Elemento | Entregable principal | Responsable | Hito |
|---|---|---|---|
| 1 Gestión | Plan de dirección e informes | Jefe de Proyecto | H1 |
| 2 Levantamiento | Línea base y arquitectura | Arquitecto de Solución | H1, H2 |
| 3 Plataforma | Cinco ambientes con observabilidad | Líder de Operación | H3 |
| 4 Equipo a bordo | 182 equipos montados | Líder de Implantación | H6 |
| 5 Servicios Etapa 1 | Software de los seis contextos | Líder de Desarrollo | H4 |
| 6 Integraciones | Contratos de interfaz en producción | Líder de Integración | H4 |
| 7 Datos y migración | Actas de conciliación | Líder de Datos | H5 |
| 8 Servicios Etapa 2 | Software de la Etapa 2 | Líder de Desarrollo | H9 |
| 9 Adhesión | Anexos firmados | Líder Funcional | H7, H12 |
| 10 Calidad | Certificación de cada etapa | Líder de Calidad | H5, H10 |
| 11 Implantación | Actas de marcha blanca | Líder de Implantación | H7, H12 |
| 12 Innovaciones | Cinco innovaciones operando | Arquitecto de Solución | H12 |
| 13 Operación | Niveles de servicio mensuales | Líder de Operación | Mensual |

*Fuente: Formulario T-14 y FEP01, Formulario E-25, p. 74.*

La tabla identifica el rol que coordina cada elemento; los responsables de los paquetes se
detallan en T-14 y pueden ser distintos. Cada hito del Formulario E-25 tiene al menos un elemento que lo gatilla. El hito
H7 depende de dos elementos que no son software, la adhesión y la implantación, y por eso sus
responsables participan del Comité de Proyecto desde el mes 1.

## 7.2 Plan de trabajo

El plan de trabajo ordena los 54 paquetes en el tiempo y les asigna personas. Esta sección explica cómo
se alinea con las metodologías del Subdocumento 6, cómo se secuenció y estimó el trabajo, cómo se divide
la capacidad en el solapamiento de los meses 13 a 15 y cómo se trabaja en los meses 19 y 20.

### 7.2.1 Alineación con las metodologías

El Subdocumento 6 combina una capa predictiva para los compromisos contractuales con una capa adaptativa
para el software (sección 6.1.1). El plan aplica esa división paquete por paquete. Los
elementos 1, 2, 3, 4, 7, 9 y 11 son predictivos: tienen fecha fija en la red, dependen del terreno, de
terceros o de un hito del Formulario E-25, y se controlan contra la línea base. Los elementos 5, 6 y 8 son
adaptativos: se construyen en iteraciones de dos semanas, ocho en la Etapa 1 (actividad A09, 80 días
hábiles) y cinco en la Etapa 2 (actividad A20, 50 días hábiles), y su contenido se prioriza con el orden
de prioridad del Formulario T-12. El elemento 13 trabaja en flujo continuo, que es la forma en que el
Subdocumento 6 atiende incidentes y solicitudes durante la operación.

Las dos capas se encuentran en la red. Cada actividad adaptativa tiene una duración fija en la red, de modo
que lo que varía dentro de ella es el contenido de cada iteración y no su fecha de término. Las
instancias de gobierno son las del Subdocumento 6: el Comité de Proyecto quincenal revisa el avance de
la EDT y el consumo de las reservas de la ruta crítica, el Comité Ejecutivo mensual revisa los
indicadores de adhesión y aprueba los cambios de alcance, y el Comité de Operación sigue la marcha
blanca desde el mes 13 (sección 6.1.4).

### 7.2.2 Secuenciamiento y estimación del esfuerzo

La secuencia sale de tres clases de dependencia. Las técnicas son las de la cadena de capacidades del
Subdocumento 3: sin registro de vigencias y expediente de jornada no hay asignación con bloqueo, y sin
asignación no hay documento ni costo (sección 3.2.2). Las físicas son las del terreno: un
equipo sólo se monta cuando el camión pasa por un terminal y nunca entre diciembre y abril
(Caso, numeral 13.2, p. 27). Las contractuales son los hitos del FEP01, Formulario E-25, p. 74, que fijan qué debe estar
aceptado en cada mes. La red de 25 actividades de la sección 7.3.1 combina las tres.

La estimación usa el método que corresponde a cada clase de trabajo. Las actividades de la red se estiman
con tres valores y se combinan con PERT, como explica la sección 7.3.1. El contenido de las
iteraciones se estima por analogía con la velocidad de equipos de igual composición, con el factor de foco
del 70 % que usa la sección 7.2.3. El montaje a bordo se estima por capacidad, porque su
límite es físico. Los 148 camiones propios se montan en la actividad A11, de 60 días hábiles, entre los
meses 6 y 9: son 2,5 camiones por día hábil repartidos en cinco terminales. Cada camión pasa por un
terminal cada seis días (Caso, capítulo 10, restricción 5, p. 23), es decir unas catorce veces en los 60
días hábiles de la actividad, así que la frecuencia de paso no es la restricción. La restricción es la dotación de
montaje en el horario de relevo, y por eso cuatro de los siete analistas de implantación entran en el mes 6
y no en el 10.

La Tabla 7.4 resume cuántas personas trabajan en cada tramo y en qué. El Formulario T-15 trae
el esfuerzo de cada etapa, que resulta de multiplicar esta dotación por los meses de cada tramo.

**Tabla 7.4.** Dotación del proyecto por tramo de meses

| Meses | Personas | Trabajo principal |
|---|---|---|
| 1 y 2 | 14 | Levantamiento, terreno, factibilidad y campaña de adhesión |
| 3 a 5 | 24 | Arquitectura, ambientes y diseño detallado |
| 6 a 9 | 30 | Construcción, integraciones, migración y montaje de la flota propia |
| 10 a 12 | 33 | Pruebas, certificación y capacitación |
| 13 a 17 | 37 | Marcha blanca y estabilización de la Etapa 1, y desarrollo de la Etapa 2 |
| 18 | 30 | Certificación de la Etapa 2 y Etapa 1 en producción |
| 19 y 20 | 26 | Marcha blanca de la Etapa 2 y Etapa 1 en producción |
| 21 a 56 | 16 | Operación |

*Fuente: Formulario T-15.*

La dotación crece hasta el peak de 37 personas en los meses 13 a 17, que es el período con dos frentes
abiertos, y baja a 16 en la operación. En la Etapa 1 el trabajo se reparte en seis frentes: gestión y
adhesión, levantamiento en terreno, plataforma y seguridad, software de los seis contextos, integraciones y
datos, y equipo a bordo. Los frentes se sincronizan en los hitos del Formulario E-25 y en la reunión
semanal de seguimiento del Subdocumento 6. La holgura que el plan reserva para los cierres del paso Los
Libertadores está en las actividades de terreno y se calcula en la sección 7.3.1.

### 7.2.3 Partición de la capacidad de ingeniería en el solapamiento de los meses 13 a 15

Entre los meses 13 y 15 ocurren a la vez la marcha blanca de la Etapa 1 y el desarrollo de la
Etapa 2 (FEP01, Artículo 17.1, p. 12). El FEP01, Artículo 17.2, p. 13 pide demostrar en el Formulario T-15 que la
dotación y los frentes de trabajo alcanzan para ambos esfuerzos. audIT divide el equipo en dos
escuadras de composición fija durante los tres meses. La Escuadra de Estabilización E1 sostiene la
marcha blanca y la Escuadra de Construcción E2 desarrolla la Etapa 2. Cada escuadra tiene su líder,
su tablero de trabajo y su reunión diaria. Se forman con personas de las células Alfa, Beta y Gamma
descritas en el Subdocumento 1 y con el refuerzo del proyecto que declara el Formulario T-15. La
Tabla 7.5 resume las dos escuadras y la capacidad que queda para coordinarlas.

**Tabla 7.5.** Escuadras del solapamiento de los meses 13 a 15

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
los cinco terminales. Cuatro analistas se incorporan en el mes 6 para el montaje a bordo de la flota propia (actividad A11)
y los siete están desde el mes 10 para capacitar a los conductores (actividad A13 de la red). Siguen en E1 hasta el fin de la estabilización posterior al paso a
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

En los meses 19 y 20 la Etapa 1 está en producción y la Etapa 2 en marcha blanca (FEP01, Artículo 17.2, p. 13). El
riesgo ya no es la capacidad, como en los meses 13 a 15, sino la integridad: dos alcances que comparten
datos no pueden producir dos versiones del mismo viaje. La Tabla 7.6 muestra los frentes y
su dotación.

**Tabla 7.6.** Frentes de trabajo de los meses 19 y 20

| Frente | Personas | Responde por |
|---|---|---|
| Etapa 1 en producción | 12 | Mesa de servicio 24x7, guardia y correcciones |
| Marcha blanca de la Etapa 2 | 11 | Portal del cliente, retornos, emisiones y talleres |
| Coordinación y datos compartidos | 3 | Conciliación diaria entre ambos alcances |

*Fuente: Formulario T-15.*

Las 26 personas se reparten así porque la Etapa 1 ya opera con el equipo que seguirá en la operación: la
mesa de servicio existe desde el mes 16, ya que desde ese mes un incidente que impida asignar es de
severidad máxima (Caso, RT-21.06, p. 34). La única fuente de verdad se garantiza por diseño. Los procesos de
la Etapa 2 no tienen datos propios de viaje, conductor ni camión: los leen de los contextos de la Etapa 1
por eventos, de modo que no existe una segunda digitación que conciliar. Lo que se concilia cada día es el
resultado, por ejemplo que cada retorno propuesto corresponda a un viaje real y que cada posición mostrada
a un cliente tenga autorización vigente. Las 12 personas del primer frente y 4 de los otros dos forman el
equipo de operación de 16 personas que sigue desde el mes 21.

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

![Figura 7.1. Red PERT de la Etapa 1 hasta el inicio de la marcha blanca, con la ruta crítica en rojo](../../subdocumentos/07-plan-trabajo/graficos/pert-etapa1.pdf)

*Figura 7.1. Red PERT de la Etapa 1 hasta el inicio de la marcha blanca, con la ruta crítica en rojo*

Fuente: Elaboración propia.

La fila central de la figura es la ruta crítica. Arriba y abajo corren las actividades que dependen
del terreno y de terceros: la cobertura móvil, la factibilidad con los proveedores de posicionamiento,
la adhesión de los transportistas y el piloto a bordo.

![Figura 7.2. Red PERT del solapamiento de los meses 13 a 15 y de la Etapa 2, con la ruta crítica en rojo](../../subdocumentos/07-plan-trabajo/graficos/pert-etapa2.pdf)

*Figura 7.2. Red PERT del solapamiento de los meses 13 a 15 y de la Etapa 2, con la ruta crítica en rojo*

Fuente: Elaboración propia.

La ruta sigue por la fila central. En la fila superior van la marcha blanca, la transferencia y la
estabilización de la Etapa 1, y en la inferior la instalación progresiva a bordo. Las actividades con
borde punteado vienen de la Figura 7.1.

Las dos reservas de contingencia de la ruta, A14 y A23, se calculan con la varianza de la cadena que
protegen. Cada una mide dos desviaciones estándar, redondeado al entero más cercano. La
Tabla 7.7 da el resultado, y el Formulario T-15 trae las estimaciones de tres puntos de cada
actividad.

**Tabla 7.7.** Reservas de contingencia de la ruta crítica

| Cadena | Actividades | Desviación estándar | Reserva | Probabilidad de cumplir |
|---|---|---|---|---|
| Etapa 1, hasta el inicio de la marcha blanca (día 240) | A01, A02, A05, A07, A09 y A12 | 6,89 | A14, 14 días | 97,9 % |
| Etapa 2, hasta el inicio de su marcha blanca (día 360) | A17, A20 y A22 | 5,04 | A23, 10 días | 97,6 % |

*Fuente: elaboración propia, con distribución normal sobre la suma de las actividades de cada cadena.*

La probabilidad de cumplir las dos fechas a la vez es 95,6 %. Cada ruta no crítica que converge en
A12 tiene una holgura de al menos 3,5 veces la desviación estándar de su tramo propio, así que el sesgo
por convergencia de rutas paralelas no cambia estas cifras de forma apreciable.

La Tabla 7.8 compara cada hito del FEP01, Formulario E-25, p. 74 con el día en que la red lo alcanza.

**Tabla 7.8.** Hitos del Formulario E-25 frente a la red

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
hito H7 del mes 16 tiene además su propio margen de 10 días hábiles, según la Tabla 7.8. Las
demás actividades no críticas absorben las restricciones físicas del Caso. El piloto a bordo (A11)
tiene 20 días hábiles de holgura y la instalación progresiva (A18) tiene 40. Un cierre del paso Los
Libertadores por nieve dura hasta 12 días corridos (Caso, numeral 13.2, p. 27), unos 9 días hábiles, de
modo que un cierre completo cabe en la holgura de ambas actividades. La adhesión de los 148
transportistas (A06) tiene 24 días hábiles de holgura libre antes de la capacitación (A13). A13
conserva 40 días hábiles y comienza en el día 182, diez días antes del término de A09;
termina en el día 222, con 38 días de holgura total y 18 de holgura libre. El hito G13,
incluido en la construcción A09, exige la versión de entrenamiento probada y congelada
en PREPROD, datos ficticios y material por perfil antes de iniciar. Los primeros diez días
cubren familiarización con roles, permisos, jornada y bloqueo, privacidad, identificación,
alertas y falta de conexión. Los treinta restantes cubren práctica de flujos completos
y evaluación, después de terminar A09. La capacitación se organiza por turnos y relevos
sin afectar la operación. La falta de G13 retrasa el inicio real y obliga a registrar
el atraso y actualizar el riesgo; el desfase no acredita disponibilidad. La
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

La planificación se lee desde el horizonte contractual hasta el control de la implementación. La Figura 7.12 muestra las ventanas agregadas de los trece elementos de la EDT en M1-M56. La Figura 7.13 presenta las 25 actividades y G13 en días hábiles, con ruta crítica, holgura total y enlaces principales; las precedencias completas se consultan en T-15 y en los PERT de la sección 7.3.1.

Los detalles se agrupan por frentes y cubren los 54 paquetes una sola vez, incluyendo los cuatro de operación. Las barras representan ventanas mensuales del T-14; los rombos muestran posiciones planificadas de hitos relacionados con la red. La tabla de hitos distingue estas posiciones de los límites contractuales y de los inicios fijos H6/H11. La probabilidad de cumplir plazos se analiza por separado en S8.

Las vistas del anexo se presentan en Figura 7.12, Figura 7.13, Figura 7.14, Figura 7.15, Figura 7.16, Figura 7.17, Figura 7.18, Figura 7.19, Figura 7.20, Figura 7.21, Figura 7.22, Figura 7.23.

![Figura 7.12. Horizonte contractual M1-M56](../../subdocumentos/07-plan-trabajo/graficos/revisada/gantt-panorama.pdf)

*Figura 7.12. Horizonte contractual M1-M56*

Fuente: Elaboración propia.

![Figura 7.13. Red CPM de 25 actividades y G13](../../subdocumentos/07-plan-trabajo/graficos/revisada/gantt-cpm.pdf)

*Figura 7.13. Red CPM de 25 actividades y G13*

Fuente: Elaboración propia.

![Figura 7.14. Gestión y levantamiento](../../subdocumentos/07-plan-trabajo/graficos/revisada/gantt-gestion.pdf)

*Figura 7.14. Gestión y levantamiento*

Fuente: Elaboración propia.

![Figura 7.15. Plataforma y equipo a bordo](../../subdocumentos/07-plan-trabajo/graficos/revisada/gantt-plataforma.pdf)

*Figura 7.15. Plataforma y equipo a bordo*

Fuente: Elaboración propia.

![Figura 7.16. Construcción de la Etapa 1](../../subdocumentos/07-plan-trabajo/graficos/revisada/gantt-e1.pdf)

*Figura 7.16. Construcción de la Etapa 1*

Fuente: Elaboración propia.

![Figura 7.17. Integraciones y migración](../../subdocumentos/07-plan-trabajo/graficos/revisada/gantt-datos.pdf)

*Figura 7.17. Integraciones y migración*

Fuente: Elaboración propia.

![Figura 7.18. Etapa 2 y adhesión](../../subdocumentos/07-plan-trabajo/graficos/revisada/gantt-e2.pdf)

*Figura 7.18. Etapa 2 y adhesión*

Fuente: Elaboración propia.

![Figura 7.19. Calidad, capacitación e implantación](../../subdocumentos/07-plan-trabajo/graficos/revisada/gantt-implantacion.pdf)

*Figura 7.19. Calidad, capacitación e implantación*

Fuente: Elaboración propia.

![Figura 7.20. Ventanas de las innovaciones](../../subdocumentos/07-plan-trabajo/graficos/revisada/gantt-innovaciones.pdf)

*Figura 7.20. Ventanas de las innovaciones*

Fuente: Elaboración propia.

![Figura 7.21. Fechas planificadas y límites de H1-H12](../../subdocumentos/07-plan-trabajo/graficos/revisada/gantt-hitos.pdf)

*Figura 7.21. Fechas planificadas y límites de H1-H12*

Fuente: Elaboración propia.

![Figura 7.22. G13, reservas y control de fechas](../../subdocumentos/07-plan-trabajo/graficos/revisada/gantt-control.pdf)

*Figura 7.22. G13, reservas y control de fechas*

Fuente: Elaboración propia.

![Figura 7.23. Continuidad operacional M21-M56](../../subdocumentos/07-plan-trabajo/graficos/revisada/gantt-operacion.pdf)

*Figura 7.23. Continuidad operacional M21-M56*

Fuente: Elaboración propia.

La figura muestra tres cosas que el plan no puede cambiar y que ordenan todo lo demás. La primera es que
ningún montaje a bordo cae en gris: el elemento 4 trabaja en los meses 6 a 10 y vuelve en los meses 16 a 18,
y en los meses 13 a 15 su actividad es la integración por plataforma, que no toca camiones. La segunda es
que los dos pasos a producción, mayo y octubre de 2028, quedan fuera de diciembre a abril, fuera de
Fiestas Patrias y en la segunda quincena del mes, después del cierre mensual de nueve días
(Caso, numeral 13.2, p. 27). La tercera es que la marcha blanca de la Etapa 1 queda dentro de la temporada de
fruta, lo que el plan acepta porque el Artículo 17 no deja otra posición y porque la marcha blanca no
interviene camiones. Durante la operación, las dos pruebas anuales de recuperación ante desastres
(FEP02, RT-07.07, p. 17) se programan en junio y en noviembre: separadas por cinco meses, fuera de la temporada de fruta, de
Fiestas Patrias y del cierre mensual. El Formulario T-14 trae la carta Gantt a nivel de paquete.

### 7.3.3 Implantación y puesta en marcha

La implantación respeta las condiciones del Caso, numeral 13.3, pp. 27 y 28: nada entra en producción sin
convivir con la forma actual de trabajar, ninguna actividad inmoviliza camiones y el despliegue avanza
por proceso. El Formulario T-18 la detalla por etapa. Esta sección resume el patrón de despliegue, las
pruebas, las métricas de éxito y la reversión.

**Patrón de despliegue.**
Cada componente se despliega con el patrón que su naturaleza permite. Los servicios en la nube usan
despliegue azul-verde: la versión nueva corre junto a la anterior y la puerta de enlace cambia el tráfico
de una a otra, de modo que volver atrás es cambiar el tráfico de vuelta. El firmware a bordo usa
despliegue canario: una versión nueva va primero a diez camiones propios de San Bernardo, luego a un
terminal y luego al resto, y sólo se instala cuando el camión pasa por un terminal. Los procesos se
habilitan en forma progresiva, uno a la vez y terminal por terminal, empezando por San Bernardo.

En la Etapa 1 los procesos entran en este orden: vigencias y jornada, que sólo registran, viaje y
posición, documento de transporte, asignación con bloqueo, costo y liquidación, y portal del
transportista. El orden sigue la cadena de dependencias del Subdocumento 3 y deja para el final los
procesos que necesitan datos acumulados. Se empieza por la flota propia porque el mandante puede
instruir a sus conductores y el equipo es suyo, y se sigue con los transportistas que adhirieron en la
cohorte inicial de la campaña.

**Cobertura a bordo mes a mes.**
El Caso exige declarar la cobertura acumulada mes a mes (Caso, numeral 13.3, p. 27). La
Tabla 7.9 la muestra para los 182 equipos audIT.

**Tabla 7.9.** Equipos audIT montados al cierre de cada mes

| Mes | Calendario | Flota propia | Terceros sin equipo | Total |
|---|---|---|---|---|
| 6 | Julio 2027 | 10 | 0 | 10 |
| 7 | Agosto 2027 | 55 | 4 | 59 |
| 8 | Septiembre 2027 | 105 | 10 | 115 |
| 9 | Octubre 2027 | 148 | 16 | 164 |
| 10 | Noviembre 2027 | 148 | 20 | 168 |
| 11 a 15 | Diciembre a abril | 148 | 20 | 168 |
| 16 | Mayo 2028 | 148 | 24 | 172 |
| 17 | Junio 2028 | 148 | 28 | 176 |
| 18 | Julio 2028 | 148 | 31 | 179 |

*Fuente: elaboración propia sobre el Caso, numeral 2.2, p. 6 y las metas de adhesión del Subdocumento 3.*

La flota propia queda completa en el mes 9, antes de la temporada de fruta. Los 34 camiones de terceros
sin equipo dependen de que su dueño firme la modalidad completa, y por eso su curva sigue la meta de
adhesión: 24 en el mes 16 y 31 en el mes 18, el 70 % y el 90 % de 34. Los tres restantes y el 22 % de la
flota subcontratada que pasa menos de una vez al mes por un terminal, unos 50 camiones, operan mientras
tanto en modalidad de datos o documental, con su nivel de evidencia visible en la torre. Los 192 camiones
de terceros con equipo propio entran a la vista única cuando se integra su plataforma, en el mes 10.

**Pruebas.**
Antes de cada marcha blanca la solución pasa cuatro clases de prueba, que el Subdocumento 9 detalla. La
prueba de aceptación la ejecutan usuarios reales de cada perfil: torre, conductores propios y de
terceros, terminal, taller, finanzas y transportistas. La prueba de desempeño verifica la asignación en
30 segundos y el documento en 90 segundos en el percentil 95, como mide el FEP01, Artículo 78.3, p. 40, con la
volumetría proyectada a tres años: 430 camiones y 118.000 viajes al año (Caso, numeral 14.1, p. 29). La
prueba de estrés lleva la carga al triple de la volumetría inicial, que es lo que la solución debe
soportar sin rediseño (FEP02, RT-09.03, p. 21), y repite la reconexión simultánea de 300 camiones que
dimensiona la sección 4.2.8. La prueba de resiliencia corta el enlace de un terminal
durante 24 horas (FEP01, Artículo 16.4, p. 12) y el de un camión durante 72.

**Métricas de éxito.**
Un paso a producción es exitoso si en sus primeros 30 días hábiles no hay incidentes críticos atribuibles
a la solución, la disponibilidad de las funciones críticas es de al menos 99,9 % en el mes, la tasa de
cambios fallidos no supera el 5 % (FEP01, Artículo 78.2 y 78.3, p. 40) y la conciliación diaria con el registro vigente no
muestra diferencias sin explicar. Son los mismos indicadores que cierran la marcha blanca, medidos ahora
con la solución como sistema de registro.

**Reversión.**
Durante la marcha blanca se aplica el procedimiento de reversión del T-18, conservando la forma actual de trabajar en paralelo y conciliando los registros antes de restituir el tráfico. Después del paso a producción, la reversión de un servicio en la nube es el cambio
de tráfico del despliegue azul-verde y la autoriza el Jefe de Proyecto con el Líder de Operación. Nada se
pierde al revertir. Los documentos de transporte ya emitidos son del sistema contable y no dependen de la
plataforma, y los equipos a bordo conservan lo enviado durante 72 horas para reenviarlo. La reversión de
un firmware usa la imagen anterior que guarda el gabinete del terminal (sección 4.3.2).

> **Compromiso C-02.** audIT ensaya la reversión de cada servicio antes de cada paso a producción y la mantiene disponible durante la estabilización posterior.
>
> Métrica: Reversión de un servicio en la nube en no más de 15 minutos, sin pérdida de eventos. Se verifica en: Ensayo de reversión en preproducción antes de cada paso a producción. Fuente: Caso, numeral 13.3, p. 27 y FEP01, Artículo 17.1, p. 12.

### 7.3.4 Marcha blanca de la Etapa 1 y de la Etapa 2

Cada marcha blanca termina sólo cuando se cumplen a la vez las seis condiciones del FEP01, Artículo 17.3, p. 13. El
plan las convierte en indicadores con umbral, medidos cada día y evaluados sobre las cuatro últimas
semanas. La Tabla 7.10 los declara para las dos etapas.

**Tabla 7.10.** Condiciones de cierre de cada marcha blanca y su umbral

| Condición del Art. 17.3 | Indicador | Etapa 1 | Etapa 2 |
|---|---|---|---|
| Sin incidentes críticos ni altos | Incidentes abiertos | Cero | Cero |
| Volumen real comprometido | Viajes por la plataforma | 100 % de flota propia y adheridos | 100 % de clientes con autorización |
| Disponibilidad y respuesta | Funciones críticas y percentil 95 | 99,9 %, 30 s y 90 s | 99,9 % y 2 min |
| Conciliación | Diferencias sin explicar | Cero | Cero |
| Personal capacitado | Usuarios certificados | Torre y terminales al 100 % | Comercial y talleres al 100 % |
| Acta de aceptación | Firma de la contraparte | Mes 15 | Mes 20 |

*Fuente: FEP01, Artículo 17.3, p. 13 y FEP01, Artículo 78.2, p. 40.*

Los umbrales de disponibilidad son los que el FEP01, Artículo 78.2, p. 40 exige en la operación para las funciones
críticas, de modo que la marcha blanca prueba lo mismo que después se cobra. La conciliación de la Etapa 1
compara cada día la plataforma con los registros vigentes: el sistema de 2013 para los viajes, las
planillas para las vigencias y el papel para la jornada de los conductores propios. Toda diferencia queda
explicada o corregida antes del día siguiente.

**Marcha blanca de la Etapa 1.**
Entre febrero y abril de 2028 la Etapa 1 opera con datos y usuarios reales, en plena temporada de fruta.
Lo aprovecha en dos pruebas que no podrían hacerse en un mes tranquilo. La verificación bloqueante corre en
paralelo en los meses 13 y 14 sobre todas las asignaciones, sin detener ninguna, y registra cuántos viajes
habría detenido, por qué motivo y con qué cliente comprometido. En el mes 15 bloquea en la flota propia con
la regla de excepción activa. La liquidación de febrero y de marzo se calcula por las dos vías, la actual y
la nueva, y se concilia transportista por transportista. Un analista de implantación está en cada
terminal en el horario de relevo, como compromete la sección 7.2.3.

**Marcha blanca de la Etapa 2.**
En agosto y septiembre de 2028 la Etapa 2 convive con la Etapa 1 en producción. El portal del cliente
muestra posición sólo de los camiones con autorización vigente, los retornos se proponen sin asignarse
automáticamente y el cálculo de emisiones se ejecuta sobre los dos meses completos. La marcha blanca
incluye la semana de Fiestas Patrias, que pone a prueba la operación con restricción vehicular sin que
ocurra ningún paso a producción.

Si una marcha blanca no cumple las seis condiciones, se extiende por cuenta de audIT sin mover las fechas
siguientes (FEP01, Artículo 17.3, p. 13). La de la Etapa 1 tiene 20 días hábiles de holgura antes de afectar la marcha
blanca de la Etapa 2, según la sección 7.3.1. La de la Etapa 2 no tiene holgura y por eso está
protegida por la reserva A23.

## Referencias

Beyer, B., Jones, C., Petoff, J. y Murphy, N. R. (Eds.). (2016). *Site Reliability Engineering: How Google Runs Production Systems*. O'Reilly Media. https://sre.google/sre-book/being-on-call/

Brooks, F. P. (1975). *The Mythical Man-Month: Essays on Software Engineering*. Addison-Wesley.

Kniberg, H. (2015). *Scrum and XP from the Trenches* (2.ª ed.). C4Media.

Malcolm, D. G., Roseboom, J. H., Clark, C. E. y Fazar, W. (1959). Application of a Technique for Research and Development Program Evaluation. *Operations Research*, *7*(5), 646-669. https://doi.org/10.1287/opre.7.5.646

Project Management Institute. (2019). *Practice Standard for Scheduling* (3.ª ed.).

Project Management Institute. (2019). *Practice Standard for Work Breakdown Structures* (3.ª ed.).

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
| Introducción | Claude Opus 5.5 en Claude Code | Redacción inicial de los dos párrafos de apertura desde el Artículo 17 y el Comunicado 10 | Alto | Ninguno | D2, Analista de Requerimientos: revisión del propósito del plan y su correspondencia con las fases y obligaciones de la oferta. |
| 7.2.3 | Claude Opus 5.5 en Claude Code | Cálculo de la dotación y de la asignación por rol con un guion, búsqueda de fuentes y redacción inicial del texto desde las decisiones de diseño del equipo | Alto | Ninguno | D2, Analista de Requerimientos: revisión de la dotación, asignación por rol y cobertura durante los solapamientos. |
| 7.3.1 | Claude Opus 5.5 en Claude Code y conector de Lucid | Cálculo de la red PERT y CPM con un guion, redacción inicial del análisis y dos diagramas escritos como código para Lucid | Alto | Medio | D2, Analista de Requerimientos: revisión de la secuencia PERT/CPM, precedencias, ruta crítica y reservas. |
| Formulario T-15 | Claude Opus 5.5 en Claude Code | Tablas de dotación, asignación, estimaciones de tres puntos y malla generadas desde el mismo cálculo | Alto | Ninguno | D2, Analista de Requerimientos: revisión de la dotación, esfuerzo, estimaciones de tres puntos y malla del T-15. |
| Resumen de apertura, 7.1, 7.2, 7.2.1, 7.2.2, 7.2.4 y 7.3.2 a 7.3.4 | Claude Opus 5.5 en Claude Code y OpenAI Codex | Redacción inicial sobre las decisiones del equipo, cálculo de la dotación por tramo y de la cobertura a bordo, y figuras de la EDT y de la carta Gantt escritas como código TikZ con un guion | Alto | Medio | D2, Analista de Planificación y Calidad: revisión de cobertura de la EDT, partición del trabajo, cronograma, implantación y correspondencia de las figuras con el plan. |
| Formularios T-14 y T-18, y esfuerzo del T-15 | Claude Opus 5.5 en Claude Code | Diccionario de los 54 paquetes, secuencias de implantación, procedimiento de reversión y curvas de esfuerzo | Alto | Ninguno | D2, Analista de Planificación y Calidad: revisión del diccionario de los 54 paquetes, secuencias de implantación, reversión y esfuerzo de T-14, T-15 y T-18. |
| 7.1 y 7.3.3 | OpenAI Codex | Actualización de descripción de EDT y generación de vistas generales y detalles legibles de EDT/Gantt; recuperación de PERT conservando el alcance de los paquetes | Alto | Alto | D2, Analista de Planificación y Calidad: revisión de las vistas generales y detalles de EDT/Gantt, sus códigos, leyendas y referencias PERT. |
| 7.3.1, T-15 y T-18 | OpenAI Codex | Precedencia A09 FS-10 de A13 y puerta G13; recálculo de holguras y actualización de PERT y gráficos; sprint 7 y complemento de sprint 8 dentro de 40 días | Alto | Ninguno | D2, Analista de Planificación y Calidad: revisión del adelanto condicionado de A13, entrega G13, holguras, duración y complemento del sprint 8 dentro de los 40 días. |
| Carta Gantt y anexos de planificación | OpenAI Codex | Conciliación de 26 filas de T-15 y 54 paquetes de T-14; reorganización por frentes; generación de ruta crítica, holguras, hitos, reservas y operación; revisión visual de los PDF | Medio | Alto | D2, Analista de Requerimientos: revisión humana de Gantt v3, su contenido, formato e integración en el Subdocumento 7. |
| EDT y anexos de alcance | OpenAI Codex | Conciliación de 13 elementos y 54 paquetes con T-14; reorganización del árbol, vistas de paquetes, ejemplo de diccionario y trazabilidad; integración y revisión visual de PDF | Medio | Alto | D2, Analista de Requerimientos: revisión humana de la EDT v2, su contenido, formato e integración en el Subdocumento 7. |
