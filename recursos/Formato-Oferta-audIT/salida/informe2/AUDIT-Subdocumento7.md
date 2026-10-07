# Subdocumento 7. Plan de trabajo, EDT, cronograma e implantación

audIT, Empresa N.º 10. Licitación TFEP-01/2026, Caso 10 Transporte de Carga. Oferta Técnica, Sobre N.º 2. Informe Preparatorio 2. Archivo AUDIT-Subdocumento7.pdf. Anexos: Formulario T-14 en el archivo AUDIT-Formulario-T-14.pdf, Formulario T-15 en el archivo AUDIT-Formulario-T-15.pdf, Formulario T-18 en el archivo AUDIT-Formulario-T-18.pdf.

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
(sección ?), y aplica el marco de gestión del Subdocumento 6: los paquetes que
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
Figura 7.1 la muestra completa.

\begin{figuraNativa}[!htbp]{Estructura de descomposición del trabajo con sus 13 elementos y 54 paquetes}{7-edt}
\begin{tikzpicture}[
  t/.style={font=\sffamily\fontsize{9.5bp}{11bp}\selectfont\color{audit-tinta},anchor=west,inner sep=0.6mm},
  n1/.style={font=\sffamily\bfseries\fontsize{9.5bp}{11bp}\selectfont\color{audit-marino},anchor=west,inner sep=0.6mm},
  ln/.style={draw=audit-filete,line width=0.6pt}]
  \node[draw=audit-marino,line width=0.7pt,fill=audit-gris-claro,font=\sffamily\bfseries\fontsize{9.5bp}{11bp}\selectfont\color{audit-marino},minimum width=146mm,minimum height=8mm] (raiz) at (73mm,6mm) {Plataforma de control de jornada, flota y viaje para Transportes Curimón};
  \draw[ln] (2mm,-4.0mm) -- (5mm,-4.0mm);
  \node[n1] at (5mm,-4.0mm) {1 Gestión del proyecto};
  \draw[ln] (8mm,-8.3mm) -- (10mm,-8.3mm);
  \node[t] at (10mm,-8.3mm) {1.1 Dirección y control};
  \draw[ln] (8mm,-12.6mm) -- (10mm,-12.6mm);
  \node[t] at (10mm,-12.6mm) {1.2 Interesados y comunicaciones};
  \draw[ln] (8mm,-16.9mm) -- (10mm,-16.9mm);
  \node[t] at (10mm,-16.9mm) {1.3 Hardware del mandante};
  \draw[ln] (8mm,-6.0mm) -- (8mm,-16.9mm);
  \draw[ln] (2mm,-23.4mm) -- (5mm,-23.4mm);
  \node[n1] at (5mm,-23.4mm) {2 Levantamiento y diseño};
  \draw[ln] (8mm,-27.7mm) -- (10mm,-27.7mm);
  \node[t] at (10mm,-27.7mm) {2.1 Línea base y catálogo};
  \draw[ln] (8mm,-32.0mm) -- (10mm,-32.0mm);
  \node[t] at (10mm,-32.0mm) {2.2 Cobertura móvil en terreno};
  \draw[ln] (8mm,-36.3mm) -- (10mm,-36.3mm);
  \node[t] at (10mm,-36.3mm) {2.3 Factibilidad con terceros};
  \draw[ln] (8mm,-40.6mm) -- (10mm,-40.6mm);
  \node[t] at (10mm,-40.6mm) {2.4 Arquitectura y datos};
  \draw[ln] (8mm,-44.9mm) -- (10mm,-44.9mm);
  \node[t] at (10mm,-44.9mm) {2.5 Estudio de costo por ruta};
  \draw[ln] (8mm,-25.4mm) -- (8mm,-44.9mm);
  \draw[ln] (2mm,-51.4mm) -- (5mm,-51.4mm);
  \node[n1] at (5mm,-51.4mm) {3 Plataforma};
  \draw[ln] (8mm,-55.7mm) -- (10mm,-55.7mm);
  \node[t] at (10mm,-55.7mm) {3.1 Ambientes y despliegue};
  \draw[ln] (8mm,-60.0mm) -- (10mm,-60.0mm);
  \node[t] at (10mm,-60.0mm) {3.2 Seguridad e identidad};
  \draw[ln] (8mm,-64.3mm) -- (10mm,-64.3mm);
  \node[t] at (10mm,-64.3mm) {3.3 Observabilidad};
  \draw[ln] (8mm,-68.6mm) -- (10mm,-68.6mm);
  \node[t] at (10mm,-68.6mm) {3.4 San Bernardo y gabinetes};
  \draw[ln] (8mm,-53.4mm) -- (8mm,-68.6mm);
  \draw[ln] (2mm,-75.1mm) -- (5mm,-75.1mm);
  \node[n1] at (5mm,-75.1mm) {4 Equipo a bordo};
  \draw[ln] (8mm,-79.4mm) -- (10mm,-79.4mm);
  \node[t] at (10mm,-79.4mm) {4.1 Firmware y gestión remota};
  \draw[ln] (8mm,-83.7mm) -- (10mm,-83.7mm);
  \node[t] at (10mm,-83.7mm) {4.2 Montaje camión por camión};
  \draw[ln] (8mm,-88.0mm) -- (10mm,-88.0mm);
  \node[t] at (10mm,-88.0mm) {4.3 Integración de terceros};
  \draw[ln] (8mm,-77.1mm) -- (8mm,-88.0mm);
  \draw[ln] (2mm,-94.5mm) -- (5mm,-94.5mm);
  \node[n1] at (5mm,-94.5mm) {5 Servicios de la Etapa 1};
  \draw[ln] (8mm,-98.8mm) -- (10mm,-98.8mm);
  \node[t] at (10mm,-98.8mm) {5.1 Personas y cumplimiento};
  \draw[ln] (8mm,-103.1mm) -- (10mm,-103.1mm);
  \node[t] at (10mm,-103.1mm) {5.2 Flota y activos};
  \draw[ln] (8mm,-107.4mm) -- (10mm,-107.4mm);
  \node[t] at (10mm,-107.4mm) {5.3 Planificación y tráfico};
  \draw[ln] (8mm,-111.7mm) -- (10mm,-111.7mm);
  \node[t] at (10mm,-111.7mm) {5.4 Telemetría y geocercas};
  \draw[ln] (8mm,-116.0mm) -- (10mm,-116.0mm);
  \node[t] at (10mm,-116.0mm) {5.5 Operación de fletes};
  \draw[ln] (8mm,-120.3mm) -- (10mm,-120.3mm);
  \node[t] at (10mm,-120.3mm) {5.6 Liquidación y costeo};
  \draw[ln] (8mm,-124.6mm) -- (10mm,-124.6mm);
  \node[t] at (10mm,-124.6mm) {5.7 Portal del transportista};
  \draw[ln] (8mm,-96.5mm) -- (8mm,-124.6mm);
  \draw[ln] (2mm,-131.1mm) -- (5mm,-131.1mm);
  \node[n1] at (5mm,-131.1mm) {6 Integraciones};
  \draw[ln] (8mm,-135.4mm) -- (10mm,-135.4mm);
  \node[t] at (10mm,-135.4mm) {6.1 Sistema contable};
  \draw[ln] (8mm,-139.7mm) -- (10mm,-139.7mm);
  \node[t] at (10mm,-139.7mm) {6.2 Plataformas de posición};
  \draw[ln] (8mm,-144.0mm) -- (10mm,-144.0mm);
  \node[t] at (10mm,-144.0mm) {6.3 Telemetría y tacógrafo};
  \draw[ln] (8mm,-148.3mm) -- (10mm,-148.3mm);
  \node[t] at (10mm,-148.3mm) {6.4 Combustible, peaje y taller};
  \draw[ln] (8mm,-152.6mm) -- (10mm,-152.6mm);
  \node[t] at (10mm,-152.6mm) {6.5 Sistema de 2013 y su retiro};
  \draw[ln] (8mm,-133.1mm) -- (8mm,-152.6mm);
  \draw[ln] (2mm,2mm) -- (2mm,-131.1mm);
  \draw[ln] (77mm,-4.0mm) -- (80mm,-4.0mm);
  \node[n1] at (80mm,-4.0mm) {7 Datos y migración};
  \draw[ln] (83mm,-8.3mm) -- (85mm,-8.3mm);
  \node[t] at (85mm,-8.3mm) {7.1 Migración de vigencias};
  \draw[ln] (83mm,-12.6mm) -- (85mm,-12.6mm);
  \node[t] at (85mm,-12.6mm) {7.2 Migración histórica};
  \draw[ln] (83mm,-16.9mm) -- (85mm,-16.9mm);
  \node[t] at (85mm,-16.9mm) {7.3 Repositorio analítico};
  \draw[ln] (83mm,-6.0mm) -- (83mm,-16.9mm);
  \draw[ln] (77mm,-23.4mm) -- (80mm,-23.4mm);
  \node[n1] at (80mm,-23.4mm) {8 Servicios de la Etapa 2};
  \draw[ln] (83mm,-27.7mm) -- (85mm,-27.7mm);
  \node[t] at (85mm,-27.7mm) {8.1 Portal del cliente};
  \draw[ln] (83mm,-32.0mm) -- (85mm,-32.0mm);
  \node[t] at (85mm,-32.0mm) {8.2 Asignación de retornos};
  \draw[ln] (83mm,-36.3mm) -- (85mm,-36.3mm);
  \node[t] at (85mm,-36.3mm) {8.3 Emisiones};
  \draw[ln] (83mm,-40.6mm) -- (85mm,-40.6mm);
  \node[t] at (85mm,-40.6mm) {8.4 Talleres y mantenimiento};
  \draw[ln] (83mm,-44.9mm) -- (85mm,-44.9mm);
  \node[t] at (85mm,-44.9mm) {8.5 Dispersión de rendimiento};
  \draw[ln] (83mm,-25.4mm) -- (83mm,-44.9mm);
  \draw[ln] (77mm,-51.4mm) -- (80mm,-51.4mm);
  \node[n1] at (80mm,-51.4mm) {9 Adhesión de transportistas};
  \draw[ln] (83mm,-55.7mm) -- (85mm,-55.7mm);
  \node[t] at (85mm,-55.7mm) {9.1 Anexo de adhesión};
  \draw[ln] (83mm,-60.0mm) -- (85mm,-60.0mm);
  \node[t] at (85mm,-60.0mm) {9.2 Campaña y enrolamiento};
  \draw[ln] (83mm,-64.3mm) -- (85mm,-64.3mm);
  \node[t] at (85mm,-64.3mm) {9.3 Medición y refuerzo};
  \draw[ln] (83mm,-53.4mm) -- (83mm,-64.3mm);
  \draw[ln] (77mm,-70.8mm) -- (80mm,-70.8mm);
  \node[n1] at (80mm,-70.8mm) {10 Calidad y pruebas};
  \draw[ln] (83mm,-75.1mm) -- (85mm,-75.1mm);
  \node[t] at (85mm,-75.1mm) {10.1 Sistema e integración};
  \draw[ln] (83mm,-79.4mm) -- (85mm,-79.4mm);
  \node[t] at (85mm,-79.4mm) {10.2 Desempeño y seguridad};
  \draw[ln] (83mm,-83.7mm) -- (85mm,-83.7mm);
  \node[t] at (85mm,-83.7mm) {10.3 Aceptación de usuario};
  \draw[ln] (83mm,-72.8mm) -- (83mm,-83.7mm);
  \draw[ln] (77mm,-90.2mm) -- (80mm,-90.2mm);
  \node[n1] at (80mm,-90.2mm) {11 Implantación};
  \draw[ln] (83mm,-94.5mm) -- (85mm,-94.5mm);
  \node[t] at (85mm,-94.5mm) {11.1 Capacitación};
  \draw[ln] (83mm,-98.8mm) -- (85mm,-98.8mm);
  \node[t] at (85mm,-98.8mm) {11.2 Marcha blanca, Etapa 1};
  \draw[ln] (83mm,-103.1mm) -- (85mm,-103.1mm);
  \node[t] at (85mm,-103.1mm) {11.3 Marcha blanca, Etapa 2};
  \draw[ln] (83mm,-107.4mm) -- (85mm,-107.4mm);
  \node[t] at (85mm,-107.4mm) {11.4 Estabilización y traspaso};
  \draw[ln] (83mm,-92.2mm) -- (83mm,-107.4mm);
  \draw[ln] (77mm,-113.9mm) -- (80mm,-113.9mm);
  \node[n1] at (80mm,-113.9mm) {12 Innovaciones};
  \draw[ln] (83mm,-118.2mm) -- (85mm,-118.2mm);
  \node[t] at (85mm,-118.2mm) {12.1 a 12.5, una por innovación};
  \draw[ln] (83mm,-115.9mm) -- (83mm,-118.2mm);
  \draw[ln] (77mm,-124.7mm) -- (80mm,-124.7mm);
  \node[n1] at (80mm,-124.7mm) {13 Operación de 36 meses};
  \draw[ln] (83mm,-129.0mm) -- (85mm,-129.0mm);
  \node[t] at (85mm,-129.0mm) {13.1 Mesa de servicio 24x7};
  \draw[ln] (83mm,-133.3mm) -- (85mm,-133.3mm);
  \node[t] at (85mm,-133.3mm) {13.2 Operación de la plataforma};
  \draw[ln] (83mm,-137.6mm) -- (85mm,-137.6mm);
  \node[t] at (85mm,-137.6mm) {13.3 Ciclo de vida del equipo a bordo};
  \draw[ln] (83mm,-141.9mm) -- (85mm,-141.9mm);
  \node[t] at (85mm,-141.9mm) {13.4 Mantención evolutiva};
  \draw[ln] (83mm,-126.7mm) -- (83mm,-141.9mm);
  \draw[ln] (77mm,2mm) -- (77mm,-124.7mm);
\end{tikzpicture}
\end{figuraNativa}

La columna izquierda reúne lo que construye la Etapa 1: gestión, levantamiento, plataforma, equipo a
bordo, los seis contextos de la arquitectura lógica y sus integraciones. La columna derecha reúne lo
que la acompaña o la sigue: datos y migración, la Etapa 2, la adhesión de los transportistas, la
calidad, la implantación, las innovaciones y la operación de 36 meses. Los paquetes 5.1 a 5.6 llevan el
nombre de los seis contextos del Subdocumento 4, de modo que cada componente de la arquitectura tiene
un solo paquete que lo construye. La adhesión es un elemento propio, con duración, responsable y riesgo,
porque el Caso exige tratarla como actividad y no como supuesto (Caso, numeral 17.5, p. 40).

La regla del 100 % se comprobó contra las tres fuentes del alcance. La Tabla 7.1
muestra el resultado.

**Tabla 7.1.** Comprobación de la cobertura de la EDT contra el alcance

| Fuente del alcance | Elementos | Paquetes | Sin paquete |
|---|---|---|---|
| Requerimientos del Formulario T-12 | 42 | 1.1 a 13.1 | Ninguno |
| Contextos de la arquitectura lógica | 6 | 5.1 a 5.6 | Ninguno |
| Innovaciones del Subdocumento 13 | 5 | 12.1 a 12.5 | Ninguna |
| Exigencias del numeral 17.5 del Caso | 11 | 2.2, 2.3, 4.2, 7.1, 9.2, 11.1 y otros | Ninguna |

*Fuente: Formulario T-12, sección ?, Subdocumento 13 y Caso, numeral 17.5, p. 40.*

Ningún elemento del alcance queda sin paquete. Cuatro paquetes no nacen de un requerimiento sino de una
exigencia del Caso sobre el plan: la caracterización de la cobertura móvil en terreno (2.2), que el
Caso, RT-03.24, p. 31 prohíbe suponer, la factibilidad con proveedores y fabricantes (2.3), que no depende
de audIT, la migración con verificación documental de las vigencias (7.1) y el estudio de costo por
ruta del mes 6 (2.5), que llega antes de la renegociación de 2027.

El diccionario de la EDT, en el Formulario T-14, declara para cada uno de los 54 paquetes su
entregable, su criterio de aceptación, el rol responsable, la actividad de la red de la
sección 7.3.1 a la que pertenece y sus meses. La Tabla 7.2 resume el primer
nivel.

**Tabla 7.2.** Resumen del diccionario de la EDT por elemento de primer nivel

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

Cada elemento tiene un único responsable, que es un rol del equipo del Formulario T-15 y no una
persona sin cargo, y cada hito del Formulario E-25 tiene al menos un elemento que lo gatilla. El hito
H7 depende de dos elementos que no son software, la adhesión y la implantación, y por eso sus
responsables participan del Comité de Proyecto desde el mes 1.

## 7.2 Plan de trabajo

El plan de trabajo ordena los 54 paquetes en el tiempo y les asigna personas. Esta sección explica cómo
se alinea con las metodologías del Subdocumento 6, cómo se secuenció y estimó el trabajo, cómo se divide
la capacidad en el solapamiento de los meses 13 a 15 y cómo se trabaja en los meses 19 y 20.

### 7.2.1 Alineación con las metodologías

El Subdocumento 6 combina una capa predictiva para los compromisos contractuales con una capa adaptativa
para el software (sección ?). El plan aplica esa división paquete por paquete. Los
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
blanca desde el mes 13 (sección ?).

### 7.2.2 Secuenciamiento y estimación del esfuerzo

La secuencia sale de tres clases de dependencia. Las técnicas son las de la cadena de capacidades del
Subdocumento 3: sin registro de vigencias y expediente de jornada no hay asignación con bloqueo, y sin
asignación no hay documento ni costo (sección ?). Las físicas son las del terreno: un
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

La Tabla 7.3 resume cuántas personas trabajan en cada tramo y en qué. El Formulario T-15 trae
el esfuerzo de cada etapa, que resulta de multiplicar esta dotación por los meses de cada tramo.

**Tabla 7.3.** Dotación del proyecto por tramo de meses

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
Tabla 7.4 resume las dos escuadras y la capacidad que queda para coordinarlas.

**Tabla 7.4.** Escuadras del solapamiento de los meses 13 a 15

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
datos no pueden producir dos versiones del mismo viaje. La Tabla 7.5 muestra los frentes y
su dotación.

**Tabla 7.5.** Frentes de trabajo de los meses 19 y 20

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

La Figura 7.2 muestra la red de la Etapa 1 hasta el inicio de la marcha blanca, y la
Figura 7.3 el solapamiento de los meses 13 a 15 y la Etapa 2.

![Figura 7.2. Red PERT de la Etapa 1 hasta el inicio de la marcha blanca, con la ruta crítica en rojo](../../figuras/07-plan-trabajo/pert-etapa1.pdf)

*Figura 7.2. Red PERT de la Etapa 1 hasta el inicio de la marcha blanca, con la ruta crítica en rojo*

Fuente: Elaboración propia.

La fila central de la figura es la ruta crítica. Arriba y abajo corren las actividades que dependen
del terreno y de terceros: la cobertura móvil, la factibilidad con los proveedores de posicionamiento,
la adhesión de los transportistas y el piloto a bordo.

![Figura 7.3. Red PERT del solapamiento de los meses 13 a 15 y de la Etapa 2, con la ruta crítica en rojo](../../figuras/07-plan-trabajo/pert-etapa2.pdf)

*Figura 7.3. Red PERT del solapamiento de los meses 13 a 15 y de la Etapa 2, con la ruta crítica en rojo*

Fuente: Elaboración propia.

La ruta sigue por la fila central. En la fila superior van la marcha blanca, la transferencia y la
estabilización de la Etapa 1, y en la inferior la instalación progresiva a bordo. Las actividades con
borde punteado vienen de la Figura 7.2.

Las dos reservas de contingencia de la ruta, A14 y A23, se calculan con la varianza de la cadena que
protegen. Cada una mide dos desviaciones estándar, redondeado al entero más cercano. La
Tabla 7.6 da el resultado, y el Formulario T-15 trae las estimaciones de tres puntos de cada
actividad.

**Tabla 7.6.** Reservas de contingencia de la ruta crítica

| Cadena | Actividades | Desviación estándar | Reserva | Probabilidad de cumplir |
|---|---|---|---|---|
| Etapa 1, hasta el inicio de la marcha blanca (día 240) | A01, A02, A05, A07, A09 y A12 | 6,89 | A14, 14 días | 97,9 % |
| Etapa 2, hasta el inicio de su marcha blanca (día 360) | A17, A20 y A22 | 5,04 | A23, 10 días | 97,6 % |

*Fuente: elaboración propia, con distribución normal sobre la suma de las actividades de cada cadena.*

La probabilidad de cumplir las dos fechas a la vez es 95,6 %. Cada ruta no crítica que converge en
A12 tiene una holgura de al menos 3,5 veces la desviación estándar de su tramo propio, así que el sesgo
por convergencia de rutas paralelas no cambia estas cifras de forma apreciable.

La Tabla 7.7 compara cada hito del FEP01, Formulario E-25, p. 74 con el día en que la red lo alcanza.

**Tabla 7.7.** Hitos del Formulario E-25 frente a la red

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
hito H7 del mes 16 tiene además su propio margen de 10 días hábiles, según la Tabla 7.7. Las
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

La carta Gantt cubre los 56 meses del contrato sobre el calendario real, con el inicio en febrero de
2027. Muestra los 13 elementos de la EDT, las dos marchas blancas, los dos pasos a producción, el inicio
de la operación y los doce hitos del Formulario E-25. La Figura 7.4 la presenta con la temporada de
fruta en gris.

\begin{figuraNativa}[!htbp]{Carta Gantt de los 56 meses por elemento de la EDT, con inicio en febrero de 2027}{7-gantt}
\begin{tikzpicture}[
  t/.style={font=\sffamily\fontsize{9.5bp}{11bp}\selectfont\color{audit-tinta}},
  lab/.style={t,anchor=west,inner sep=0pt}]
  \fill[audit-gris-claro] (40.00mm,9.0mm) rectangle (45.70mm,-78.4mm);
  \fill[audit-gris-claro] (59.00mm,9.0mm) rectangle (68.50mm,-78.4mm);
  \fill[audit-gris-claro] (81.80mm,9.0mm) rectangle (91.30mm,-78.4mm);
  \fill[audit-gris-claro] (104.60mm,9.0mm) rectangle (114.10mm,-78.4mm);
  \fill[audit-gris-claro] (127.40mm,9.0mm) rectangle (136.90mm,-78.4mm);
  \node[t] at (50.45mm,6.5mm) {2027};
  \draw[audit-filete] (40.00mm,9.0mm) -- (40.00mm,4.5mm);
  \node[t] at (72.30mm,6.5mm) {2028};
  \draw[audit-filete] (60.90mm,9.0mm) -- (60.90mm,4.5mm);
  \node[t] at (95.10mm,6.5mm) {2029};
  \draw[audit-filete] (83.70mm,9.0mm) -- (83.70mm,4.5mm);
  \node[t] at (117.90mm,6.5mm) {2030};
  \draw[audit-filete] (106.50mm,9.0mm) -- (106.50mm,4.5mm);
  \node[t] at (137.85mm,6.5mm) {2031};
  \draw[audit-filete] (129.30mm,9.0mm) -- (129.30mm,4.5mm);
  \node[t] at (40.95mm,2.2mm) {1};
  \node[t] at (63.75mm,2.2mm) {13};
  \node[t] at (69.45mm,2.2mm) {16};
  \node[t] at (78.95mm,2.2mm) {21};
  \node[t] at (101.75mm,2.2mm) {33};
  \node[t] at (124.55mm,2.2mm) {45};
  \node[t] at (145.45mm,2.2mm) {56};
  \node[lab] at (0mm,6.5mm) {Año};
  \node[lab] at (0mm,2.2mm) {Mes del contrato};
  \node[lab] at (0mm,-2.80mm) {1 Gestión};
  \draw[fill=audit-marino!55,draw=audit-marino,line width=0.4pt] (40.00mm,-4.40mm) rectangle (79.90mm,-1.20mm);
  \node[lab] at (0mm,-8.40mm) {2 Levantamiento};
  \draw[fill=audit-marino!55,draw=audit-marino,line width=0.4pt] (40.00mm,-10.00mm) rectangle (51.40mm,-6.80mm);
  \draw[fill=audit-marino!55,draw=audit-marino,line width=0.4pt] (62.80mm,-10.00mm) rectangle (66.60mm,-6.80mm);
  \node[lab] at (0mm,-14.00mm) {3 Plataforma};
  \draw[fill=audit-marino!55,draw=audit-marino,line width=0.4pt] (45.70mm,-15.60mm) rectangle (62.80mm,-12.40mm);
  \node[lab] at (0mm,-19.60mm) {4 Equipo a bordo};
  \draw[fill=audit-marino!55,draw=audit-marino,line width=0.4pt] (49.50mm,-21.20mm) rectangle (59.00mm,-18.00mm);
  \draw[fill=audit-marino!55,draw=audit-marino,line width=0.4pt] (62.80mm,-21.20mm) rectangle (74.20mm,-18.00mm);
  \node[lab] at (0mm,-25.20mm) {5 Servicios Etapa 1};
  \draw[fill=audit-marino!55,draw=audit-marino,line width=0.4pt] (49.50mm,-26.80mm) rectangle (59.00mm,-23.60mm);
  \node[lab] at (0mm,-30.80mm) {6 Integraciones};
  \draw[fill=audit-marino!55,draw=audit-marino,line width=0.4pt] (49.50mm,-32.40mm) rectangle (59.00mm,-29.20mm);
  \draw[fill=audit-marino!55,draw=audit-marino,line width=0.4pt] (68.50mm,-32.40mm) rectangle (79.90mm,-29.20mm);
  \node[lab] at (0mm,-36.40mm) {7 Datos y migración};
  \draw[fill=audit-marino!55,draw=audit-marino,line width=0.4pt] (49.50mm,-38.00mm) rectangle (62.80mm,-34.80mm);
  \draw[fill=audit-marino!55,draw=audit-marino,line width=0.4pt] (74.20mm,-38.00mm) rectangle (85.60mm,-34.80mm);
  \node[lab] at (0mm,-42.00mm) {8 Servicios Etapa 2};
  \draw[fill=audit-marino!55,draw=audit-marino,line width=0.4pt] (62.80mm,-43.60mm) rectangle (74.20mm,-40.40mm);
  \node[lab] at (0mm,-47.60mm) {9 Adhesión};
  \draw[fill=audit-marino!55,draw=audit-marino,line width=0.4pt] (40.00mm,-49.20mm) rectangle (79.90mm,-46.00mm);
  \node[lab] at (0mm,-53.20mm) {10 Calidad y pruebas};
  \draw[fill=audit-marino!55,draw=audit-marino,line width=0.4pt] (57.10mm,-54.80mm) rectangle (62.80mm,-51.60mm);
  \draw[fill=audit-marino!55,draw=audit-marino,line width=0.4pt] (70.40mm,-54.80mm) rectangle (74.20mm,-51.60mm);
  \node[lab] at (0mm,-58.80mm) {11 Implantación};
  \draw[fill=audit-marino!55,draw=audit-marino,line width=0.4pt] (57.10mm,-60.40mm) rectangle (62.80mm,-57.20mm);
  \draw[fill=audit-turquesa!45,draw=audit-marino,line width=0.4pt] (62.80mm,-60.40mm) rectangle (68.50mm,-57.20mm);
  \draw[fill=audit-marino,draw=audit-marino,line width=0.4pt] (68.50mm,-60.40mm) rectangle (70.40mm,-57.20mm);
  \draw[fill=audit-marino!55,draw=audit-marino,line width=0.4pt] (70.40mm,-60.40mm) rectangle (74.20mm,-57.20mm);
  \draw[fill=audit-turquesa!45,draw=audit-marino,line width=0.4pt] (74.20mm,-60.40mm) rectangle (78.00mm,-57.20mm);
  \draw[fill=audit-marino,draw=audit-marino,line width=0.4pt] (78.00mm,-60.40mm) rectangle (79.90mm,-57.20mm);
  \node[lab] at (0mm,-64.40mm) {12 Innovaciones};
  \draw[fill=audit-marino!55,draw=audit-marino,line width=0.4pt] (45.70mm,-66.00mm) rectangle (68.50mm,-62.80mm);
  \node[lab] at (0mm,-70.00mm) {13 Operación};
  \draw[fill=audit-gris-claro!60!audit-marino!25,draw=audit-marino,line width=0.4pt] (78.00mm,-71.60mm) rectangle (146.40mm,-68.40mm);
  \node[lab] at (0mm,-75.60mm) {Hitos del E-25};
  \fill[audit-marino] (42.85mm,-74.00mm) -- (41.75mm,-76.80mm) -- (43.95mm,-76.80mm) -- cycle;
  \fill[audit-marino] (46.65mm,-74.00mm) -- (45.55mm,-76.80mm) -- (47.75mm,-76.80mm) -- cycle;
  \fill[audit-marino] (50.45mm,-74.00mm) -- (49.35mm,-76.80mm) -- (51.55mm,-76.80mm) -- cycle;
  \fill[audit-marino] (58.05mm,-74.00mm) -- (56.95mm,-76.80mm) -- (59.15mm,-76.80mm) -- cycle;
  \fill[audit-marino] (61.85mm,-74.00mm) -- (60.75mm,-76.80mm) -- (62.95mm,-76.80mm) -- cycle;
  \fill[audit-marino] (63.75mm,-74.00mm) -- (62.65mm,-76.80mm) -- (64.85mm,-76.80mm) -- cycle;
  \fill[audit-marino] (65.65mm,-74.00mm) -- (64.55mm,-76.80mm) -- (66.75mm,-76.80mm) -- cycle;
  \fill[audit-marino] (69.45mm,-74.00mm) -- (68.35mm,-76.80mm) -- (70.55mm,-76.80mm) -- cycle;
  \fill[audit-marino] (71.35mm,-74.00mm) -- (70.25mm,-76.80mm) -- (72.45mm,-76.80mm) -- cycle;
  \fill[audit-marino] (73.25mm,-74.00mm) -- (72.15mm,-76.80mm) -- (74.35mm,-76.80mm) -- cycle;
  \fill[audit-marino] (75.15mm,-74.00mm) -- (74.05mm,-76.80mm) -- (76.25mm,-76.80mm) -- cycle;
  \fill[audit-marino] (78.95mm,-74.00mm) -- (77.85mm,-76.80mm) -- (80.05mm,-76.80mm) -- cycle;
  \draw[fill=audit-turquesa!45,draw=audit-marino] (0mm,-84.8mm) rectangle (4mm,-82.0mm); \node[lab] at (5mm,-83.4mm) {Marcha blanca};
  \draw[fill=audit-marino,draw=audit-marino] (36mm,-84.8mm) rectangle (40mm,-82.0mm); \node[lab] at (41mm,-83.4mm) {Paso a producción};
  \fill[audit-gris-claro] (78mm,-84.8mm) rectangle (82mm,-82.0mm); \node[lab] at (83mm,-83.4mm) {Diciembre a abril};
\end{tikzpicture}
\end{figuraNativa}

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
Tabla 7.8 la muestra para los 182 equipos audIT.

**Tabla 7.8.** Equipos audIT montados al cierre de cada mes

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
dimensiona la sección ?. La prueba de resiliencia corta el enlace de un terminal
durante doce horas y el de un camión durante 72.

**Métricas de éxito.**
Un paso a producción es exitoso si en sus primeros 30 días hábiles no hay incidentes críticos atribuibles
a la solución, la disponibilidad de las funciones críticas es de al menos 99,9 % en el mes, la tasa de
cambios fallidos no supera el 5 % (FEP01, Artículo 78.2 y 78.3, p. 40) y la conciliación diaria con el registro vigente no
muestra diferencias sin explicar. Son los mismos indicadores que cierran la marcha blanca, medidos ahora
con la solución como sistema de registro.

**Reversión.**
Durante la marcha blanca la reversión no requiere procedimiento: la forma actual de trabajar sigue
operando en paralelo. Después del paso a producción, la reversión de un servicio en la nube es el cambio
de tráfico del despliegue azul-verde y la autoriza el Jefe de Proyecto con el Líder de Operación. Nada se
pierde al revertir. Los documentos de transporte ya emitidos son del sistema contable y no dependen de la
plataforma, y los equipos a bordo conservan lo enviado durante 72 horas para reenviarlo. La reversión de
un firmware usa la imagen anterior que guarda el gabinete del terminal (sección ?).

> **Compromiso C-02.** audIT ensaya la reversión de cada servicio antes de cada paso a producción y la mantiene disponible durante la estabilización posterior.
>
> Métrica: Reversión de un servicio en la nube en no más de 15 minutos, sin pérdida de eventos. Se verifica en: Ensayo de reversión en preproducción antes de cada paso a producción. Fuente: Caso, numeral 13.3, p. 27 y FEP01, Artículo 17.1, p. 12.

### 7.3.4 Marcha blanca de la Etapa 1 y de la Etapa 2

Cada marcha blanca termina sólo cuando se cumplen a la vez las seis condiciones del FEP01, Artículo 17.3, p. 13. El
plan las convierte en indicadores con umbral, medidos cada día y evaluados sobre las cuatro últimas
semanas. La Tabla 7.9 los declara para las dos etapas.

**Tabla 7.9.** Condiciones de cierre de cada marcha blanca y su umbral

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
| Introducción | Claude Opus 5.5 en Claude Code | Redacción inicial de los dos párrafos de apertura desde el Artículo 17 y el Comunicado 10 | Alto | Ninguno | [nombre y cargo de quien revisó, y qué verificó] |
| 7.2.3 | Claude Opus 5.5 en Claude Code | Cálculo de la dotación y de la asignación por rol con un guion, búsqueda de fuentes y redacción inicial del texto desde las decisiones D4-61 a D4-67 | Alto | Ninguno | [nombre y cargo de quien revisó, y qué verificó] |
| 7.3.1 | Claude Opus 5.5 en Claude Code y conector de Lucid | Cálculo de la red PERT y CPM con un guion, redacción inicial del análisis y dos diagramas escritos como código para Lucid | Alto | Medio | [nombre y cargo de quien revisó, y qué verificó] |
| Formulario T-15 | Claude Opus 5.5 en Claude Code | Tablas de dotación, asignación, estimaciones de tres puntos y malla generadas desde el mismo cálculo | Alto | Ninguno | [nombre y cargo de quien revisó, y qué verificó] |
| Resumen de apertura, 7.1, 7.2, 7.2.1, 7.2.2, 7.2.4 y 7.3.2 a 7.3.4 | Claude Opus 5.5 en Claude Code | Redacción inicial sobre las decisiones del equipo, cálculo de la dotación por tramo y de la cobertura a bordo, y figuras de la EDT y de la carta Gantt escritas como código TikZ con un guion | Alto | Medio | [nombre y cargo de quien revisó, y qué verificó] |
| Formularios T-14 y T-18, y esfuerzo del T-15 | Claude Opus 5.5 en Claude Code | Diccionario de los 54 paquetes, secuencias de implantación, procedimiento de reversión y curvas de esfuerzo | Alto | Ninguno | [nombre y cargo de quien revisó, y qué verificó] |
