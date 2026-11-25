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
> - La ruta crítica determinista calculada con CPM, las condiciones para el análisis PERT y una carta Gantt de 56 meses con los doce hitos del Formulario E-25.
> - La capacidad interna mes a mes, con un máximo de 39,2306 FTE equivalentes en M7, el servicio externo y el esfuerzo por paquete en el Formulario T-15.
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
Figura 7.1 la muestra completa.

La descomposición de segundo nivel se presenta en Figura 7.2, Figura 7.3, Figura 7.4, Figura 7.5, Figura 7.6. La ficha de aceptación de 11.2 está en Figura 7.7; la lectura de cobertura y los 42 vínculos requisito--paquete están en Figura 7.8 y Figura 7.9.

![Figura 7.1. Árbol general de la EDT: raíz y trece elementos](../../subdocumentos/07-plan-trabajo/graficos/edt-revisada/01-arbol.pdf)

*Figura 7.1. Árbol general de la EDT: raíz y trece elementos*

Fuente: Elaboración propia.

![Figura 7.2. Paquetes 1 a 3: gestión, diseño y plataforma](../../subdocumentos/07-plan-trabajo/graficos/edt-revisada/02-paquetes-1.pdf)

*Figura 7.2. Paquetes 1 a 3: gestión, diseño y plataforma*

Fuente: Elaboración propia.

![Figura 7.3. Paquetes 4 y 5: equipo y servicios Etapa 1](../../subdocumentos/07-plan-trabajo/graficos/edt-revisada/03-paquetes-2.pdf)

*Figura 7.3. Paquetes 4 y 5: equipo y servicios Etapa 1*

Fuente: Elaboración propia.

![Figura 7.4. Paquetes 6 a 8: integraciones, datos y Etapa 2](../../subdocumentos/07-plan-trabajo/graficos/edt-revisada/04-paquetes-3.pdf)

*Figura 7.4. Paquetes 6 a 8: integraciones, datos y Etapa 2*

Fuente: Elaboración propia.

![Figura 7.5. Paquetes 9 a 11: adhesión, calidad e implantación](../../subdocumentos/07-plan-trabajo/graficos/edt-revisada/05-paquetes-4.pdf)

*Figura 7.5. Paquetes 9 a 11: adhesión, calidad e implantación*

Fuente: Elaboración propia.

![Figura 7.6. Paquetes 12 y 13: innovaciones y operación](../../subdocumentos/07-plan-trabajo/graficos/edt-revisada/06-paquetes-5.pdf)

*Figura 7.6. Paquetes 12 y 13: innovaciones y operación*

Fuente: Elaboración propia.

![Figura 7.7. Ejemplo del diccionario: paquete 11.2](../../subdocumentos/07-plan-trabajo/graficos/edt-revisada/07-ejemplo.pdf)

*Figura 7.7. Ejemplo del diccionario: paquete 11.2*

Fuente: Elaboración propia.

![Figura 7.8. Trazabilidad de alcance, paquetes y evidencia](../../subdocumentos/07-plan-trabajo/graficos/edt-revisada/08-trazabilidad.pdf)

*Figura 7.8. Trazabilidad de alcance, paquetes y evidencia*

Fuente: Elaboración propia.

![Figura 7.9. Matriz de los 42 requisitos y sus paquetes asignados](../../subdocumentos/07-plan-trabajo/graficos/edt-revisada/09-matriz-requisitos.pdf)

*Figura 7.9. Matriz de los 42 requisitos y sus paquetes asignados*

Fuente: Elaboración propia.

La vista general muestra la raíz y los trece elementos de primer nivel. Las cinco láminas de detalle distribuyen los 54 paquetes sin repetir el diccionario; el entregable, la aceptación, el responsable y los meses de cada uno permanecen en el Formulario T-14. La
organización distingue gestión, diseño, plataforma, equipo a bordo, servicios, integraciones,
datos, adhesión, calidad, implantación, innovaciones y operación de 36 meses. Los paquetes 5.1 a 5.6 llevan el
nombre de los seis contextos del Subdocumento 4. La lectura por capacidades de la Tabla 7.1
relaciona entregables de ambos cortes con las actividades de su primera entrega y conserva la codificación
del T-14 para el seguimiento de pruebas, cronograma y costos. La adhesión es un elemento propio, con duración, responsable y riesgo,
porque el Caso exige tratarla como actividad y no como supuesto (Caso, numeral 17.5, p. 40).

**Tabla 7.1.** Capacidades de software, paquetes y actividades de control

| Capacidad verificable | Paquetes del T-14 | Enlace con T-15 |
|---|---|---|
| Personas, asignación y permisos | 5.1 Personas y cumplimiento, 5.3 Planificación y tráfico, 5.7 Portal del transportista | A09 entrega H4 y A12 certificación H5 |
| Flota, posición y mantenimiento | 5.2 Flota y activos, 5.4 Telemetría y geocercas, 8.1 Portal del cliente, 8.4 Mantenimiento | A09/A12 y A17/A20/A22 |
| Flete y retorno | 5.5 Operación de fletes, 8.2 Asignación de retornos | A09/A12 y A17/A20/A22 |
| Costeo, liquidación y analítica | 5.6 Liquidación y costeo, 8.3 Emisiones, 8.5 Rendimiento | A09/A12 y A17/A20/A22 |

Esta lectura identifica los productos y su actividad de control. La descomposición de la red por
contexto requiere estimaciones de duración y precedencias de sus paquetes, además del enlace al hito.

La descomposición contiene los 54 paquetes del diccionario T-14, sin duplicar códigos. Los 42
códigos de T-12 tienen al menos un paquete asignado en la matriz de la Figura 7.9;
esta correspondencia de códigos no sustituye la comprobación del entregable y de su prueba de
aceptación. La Tabla 7.2 resume las demás fuentes del alcance.

**Tabla 7.2.** Fuentes de alcance y puntos de trazabilidad de la EDT

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

La Tabla 7.3 desglosa las once exigencias del numeral 17.5 y localiza el trabajo que las materializa. Los paquetes comparten evidencia cuando la restricción afecta a varios frentes.

**Tabla 7.3.** Exigencias de planificación del Caso y paquetes que las desarrollan

| Exigencia | Paquetes | Evidencia planificada |
|---|---|---|
| Horizonte de 56 meses | 1.1, 13.1 a 13.4 | Gantt M1--M56 |
| Despliegue a bordo y cobertura acumulada | 4.1 a 4.3 | Curva mensual de implantación |
| Adhesión con duración, responsable y riesgo | 9.1 a 9.3 | Campaña, metas y refuerzo |
| Congelamiento, restricciones y cierre mensual | 4.2, 6.1, 11.2, 11.3 | Ventanas de implantación y Gantt |
| Cierres fronterizos por nieve | 4.1, 4.2 | Ventanas de piloto y lotes, rutas alternativas y control de cambios |
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
sección 7.3.1 a la que pertenece y sus meses. La Tabla 7.4 resume el primer
nivel.

**Tabla 7.4.** Resumen del diccionario de la EDT por elemento de primer nivel

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

La estimación separa capacidad de ingeniería, atención y servicio externo. Las actividades tienen
entregable y dependencia identificables en T-14/T-15. Las duraciones son ventanas de planificación;
la capacidad mensual contratada procede de la conciliación de perfiles y demanda de desarrollo.
El montaje utiliza 140 minutos de puesto por kit, 20 minutos de banco y 140 minutos de analista,
como hipótesis a validar en el piloto; no se presentan como tiempos ya medidos.

### 7.2.3 Capacidad interna y servicio externo

La capacidad de implementación alcanza 39,2306 FTE equivalentes en M7. Un FTE equivale a 160 horas
mensuales; la fracción expresa contratación de capacidad y no un número nominal de personas.
La curva detallada por mes, tarea, rol y paquete está en T-15. Se presupuestan 99.626,67 horas
internas en M1--M20 y 84.606 en M21--M56, incluido el cierre de integraciones y migración.
Los refuerzos SRE y Software de H6, H7, H11 y H12 están dentro de esa contratación.

El montaje externo de M7--M9 sustituye las horas de puesto internas; audIT conserva banco,
analista, prueba y recepción. El técnico de implementación se mantiene antes de M19 y sale
desde ese mes. En operación hay 0,5 FTE interno de coordinación de campo, más visitas externas,
reposiciones y rondas. No se compromete una cuadrilla permanente de dos personas.

### 7.2.4 Partición de capacidad en M13 a M15

En M13--M15 conviven la estabilización E1 y la construcción E2. El equipo base de referencia
es 37,0 FTE, dividido en 21,5 para E1, 14,1 para E2 y 1,4 de coordinación. Esa partición
es una regla de control del equipo base, no el máximo de contratación de toda la implementación.
M13 añade 160 horas SRE y 80 horas Software para la puesta en producción: total 38,5 FTE
equivalentes. M14 y M15 conservan 37,0. Los refuerzos no se cuentan simultáneamente en ambos frentes.

Los siete roles de dirección comparten su jornada al 80 por ciento entre los frentes y reservan
el resto a coordinación. El resto de los puestos mantiene frente primario y una única reserva
semanal. El líder de cada frente asigna la tarea del diccionario a su ejecutor y descuenta
guardia, atención, revisión y ausencia antes de fijar capacidad neta de sprint. No se identifica
capacidad bruta con horas netas de programación.

En terreno se programan los 35 relevos semanales de los cinco terminales con los siete analistas
de implantación presupuestados en este tramo. La agenda se confirma con cada terminal y
reserva capacitación por turno sin retirar usuarios críticos de la operación. El Jefe de Proyecto
revisa semanalmente cupos, ausencias y reemplazos. Si un cupo no se confirma se usa simulación
en PREPROD y se reasigna la práctica; no se certifica un usuario que no completó la evaluación.

> **Compromiso C-01.** audIT mantiene presencia de implantación en el relevo y protege la atención de la operación vigente.
>
> Métrica: 35 turnos de relevo semanales en los cinco terminales durante marcha blanca y estabilización E1. Se verifica en: registro semanal de turno, ejecutor y suplencia. Fuente: Caso, numeral 13.3, p. 27.

### 7.2.5 Solapamiento de M19 y M20

La contratación interna equivale a 26,5 FTE en M19 y 25,0 en M20. El técnico de campo ya no
forma parte de esa nómina; la atención física se ejecuta por visita externa. La Etapa 1 en
producción y la Etapa 2 en marcha blanca comparten los registros de viaje, conductor, camión y
transportista. Cada contexto conserva un único dueño y la conciliación diaria contrasta el
resultado con el registro vigente. El refuerzo de H11 pertenece a M19 y no se extiende por
defecto a M20. T-15 contiene el presupuesto por perfil; el Líder de Operación protege primero
la continuidad E1 y el de Desarrollo ejecuta el alcance E2 sin usar dos veces la misma jornada.

### 7.2.6 Continuidad y madurez del soporte

La mesa N1 dispone de seis agentes regulares y un FTE de suplencias y picos: 1.120 horas por mes.
La coordinación interna de campo dispone de 80 horas mensuales; el proveedor atiende tres visitas
correctivas y dos rondas regionales mensuales presupuestadas, además de las reposiciones incluidas
en el contrato. Los tiempos de respuesta y resolución se mantienen conforme al FEP01, Artículo 78.2, p. 40.
Las tarifas de servicio de campo son provisiones de presupuesto y requieren orden de servicio
y cobertura confirmada por sitio antes de su activación.

La carga variable de Software, Datos y QA utiliza factores 100, 75, 50 y 25 por ciento desde
M21, M25, M33 y M45. La cobertura fija permanece. Cada reducción exige dos meses sin P1,
backlog menor que diez y demanda dentro de capacidad; si no se cumple, se mantiene el factor
anterior y se activa el escenario sin reducción. La supervisión conserva los SLA y no convierte
una hipótesis de madurez en una reducción automática de la obligación de servicio.

El cierre M21--M24 de EDT6.5 y EDT7.2 reserva 1.669 horas ya incluidas en la contratación.
La conducción técnica de cierre utiliza 18, 17, 17 y 17 horas de la capacidad de Gestión de Servicio
en M21, M22, M23 y M24: ese puesto debe acreditar competencia de liderazgo de desarrollo para
asumir esta responsabilidad. La reserva deja 62 o 63 horas para su gestión ordinaria dentro de
las 80 contratadas. En H1 se asigna un titular que cumpla ambos cometidos o un sustituto de igual
capacidad y tarifa, conservando la cobertura de servicio y sin declarar una equivalencia ya acreditada.
El presupuesto identifica esa asignación como propuesta de ejecución, no como nombramiento confirmado.

El cierre tiene recursos de Arquitectura, Frontend, Datos y QA
en T-15, y una actividad formal de estabilización E2 posterior a H12. La aceptación contractual
no elimina ese trabajo ni lo duplica dentro de la mantención evolutiva.

## 7.3 Cronograma e implantación

Esta sección determina la ruta crítica de la implementación con sus holguras y presenta la carta
Gantt, el plan de implantación y el plan de las dos marchas blancas.

### 7.3.1 Ruta crítica y holguras

La red detallada del Formulario T-15 conecta entregables, revisiones, hitos y operación.
A09 y A20 son grupos de ocho y cinco sprints, respectivamente; los nodos individuales de diez
días identifican la entrega de cada contexto. G13 es una entrega probada de PREPROD al cierre
del séptimo sprint y habilita capacitación; su disponibilidad real es condición de inicio.

La red incorpora los lotes M6--M9, el escalamiento lógico M13--M15 sin intervención física,
el estudio EDT2.5 entregado durante M6, la migración histórica y la estabilización E2 hasta M24.
Cada relación declara FS o SS y su desfase. Se calculan ES, EF, LS, LF, HT y HL con cotas
propias de liberación y límite; la criticidad se interpreta contra esas fechas. La secuencia de
control que fija la aceptación H12 recorre A01, A02, R-H1, H1, A05, INN5-D, INN5-C, INN5-Q, R-H6, H6, A17, R-H8, H8, los sprints A20-1 a A20-5, A22-SIS, R-H10, H10, A23, H11, A24, A25, R-H12 y H12. Sus
enlaces sin margen gobiernan las transiciones H6, H11 y H12 y se distinguen de las restricciones
locales de lote (M7/8/9-KIT) y de las ventanas de revisión de contraparte. H6 queda condicionado
por la certificación de la innovación circadiana INN5-Q y por la reserva A14; H11 por la reserva
A23 y la certificación E2; H12 por la marcha blanca A24 y el corte A25. Pueden solaparse la
familiarización A13-FAM con el sprint A09-8, la marcha blanca A24 con la migración histórica
A24-HIST2 y la estabilización CE2 con el saneamiento posterior al acta H12. La lámina de control
del anexo traza esta cadena; el resto de la red con HT cero es restricción local y no se suma a
una única ruta crítica.

La Tabla 7.5 presenta las fechas de aceptación planificadas, incluidas las ventanas de
revisión de contraparte. Los inicios de marcha blanca H6 y H11 se fijan al comienzo de M13 y M19.
Las fechas civiles son una visualización de SA-01; al fijar el inicio contractual se contrastan
contra temporada de fruta, cierres y relevos sin desplazar los hitos del E-25.

\input{subdocumentos/07-plan-trabajo/graficos/conciliacion-3.2/hitos-resumen.tex}

H4, H7 y H12 no tienen margen al límite contractual. H11 tiene fecha fija al inicio de M19:
su margen se controla en la reserva A23 y no adelantando el acta. En particular, la marcha blanca
E2 ocupa los días 360 a 400, el corte A25 los días 400 a 410 y la revisión R-H12 los días 410 a 420.
Esta secuencia consume el plazo hasta H12. La contratación mensual de T-15 no acredita por sí
sola capacidad neta para acortar actividades ni disponibilidad simultánea por turno.
Antes de fijar la línea base en H1, el Jefe de Proyecto y los ejecutores deben validar capacidad,
ventanas de terceros y estimaciones de tres puntos. Cualquier adelanto o solapamiento debe
conservar los criterios de aceptación y demostrar su efecto en recursos, pruebas y costo.
Hasta esa validación se mantiene la exposición alta de R-17 de S8/T-16, sin declarar recuperada
una holgura ni una probabilidad de cumplimiento que la red actual no respalda.

Las reservas A14 y A23 son ventanas de contingencia de planificación y no una probabilidad
calculada de cumplimiento. Si se reciben observaciones se evalúa la subsanación y se registra
el consumo de reserva. La malla presentada es CPM determinista con duraciones de ventana y no
sustituye el análisis PERT: las estimaciones de tres puntos que el Formulario T-14 exige quedan
pendientes de la validación de los ejecutores, y las probabilidades de la red anterior deben
recalcularse sobre esta malla antes de volver a publicarse, sin trasladar probabilidades
históricas a los nodos nuevos. Las duraciones nuevas deben contrastarse en H1 con el ejecutor
y el calendario real; esa revisión no autoriza mover las fechas obligatorias.

### 7.3.2 Carta Gantt

La carta Gantt muestra las ventanas de los 54 paquetes, los hitos y la red de control.
La descomposición por contexto permite distinguir una dependencia técnica de la espera de un
acta. El Formulario T-14 incorpora directamente la carta, sin depender de una remisión al cuerpo.
T-15 presenta la red detallada y sus holguras; el presupuesto de capacidad se verifica por mes y perfil.

Las vistas se presentan en Figura 7.10, Figura 7.11, Figura 7.12, Figura 7.13, Figura 7.14, Figura 7.15, Figura 7.16, Figura 7.17, Figura 7.18, Figura 7.19, Figura 7.20, Figura 7.21.

![Figura 7.10. Horizonte contractual M1--M56](../../subdocumentos/07-plan-trabajo/graficos/revisada/gantt-panorama.pdf)

*Figura 7.10. Horizonte contractual M1--M56*

Fuente: Elaboración propia.

![Figura 7.11. Cadena de control hasta H12](../../subdocumentos/07-plan-trabajo/graficos/revisada/gantt-cpm.pdf)

*Figura 7.11. Cadena de control hasta H12*

Fuente: Elaboración propia.

![Figura 7.12. Gestión y levantamiento](../../subdocumentos/07-plan-trabajo/graficos/revisada/gantt-gestion.pdf)

*Figura 7.12. Gestión y levantamiento*

Fuente: Elaboración propia.

![Figura 7.13. Plataforma y equipo a bordo](../../subdocumentos/07-plan-trabajo/graficos/revisada/gantt-plataforma.pdf)

*Figura 7.13. Plataforma y equipo a bordo*

Fuente: Elaboración propia.

![Figura 7.14. Construcción por capacidades E1](../../subdocumentos/07-plan-trabajo/graficos/revisada/gantt-e1.pdf)

*Figura 7.14. Construcción por capacidades E1*

Fuente: Elaboración propia.

![Figura 7.15. Integraciones y migración](../../subdocumentos/07-plan-trabajo/graficos/revisada/gantt-datos.pdf)

*Figura 7.15. Integraciones y migración*

Fuente: Elaboración propia.

![Figura 7.16. Capacidades E2 y adhesión](../../subdocumentos/07-plan-trabajo/graficos/revisada/gantt-e2.pdf)

*Figura 7.16. Capacidades E2 y adhesión*

Fuente: Elaboración propia.

![Figura 7.17. Calidad e implantación](../../subdocumentos/07-plan-trabajo/graficos/revisada/gantt-implantacion.pdf)

*Figura 7.17. Calidad e implantación*

Fuente: Elaboración propia.

![Figura 7.18. Ventanas de innovaciones](../../subdocumentos/07-plan-trabajo/graficos/revisada/gantt-innovaciones.pdf)

*Figura 7.18. Ventanas de innovaciones*

Fuente: Elaboración propia.

![Figura 7.19. Lotes de montaje y condiciones](../../subdocumentos/07-plan-trabajo/graficos/revisada/gantt-hitos.pdf)

*Figura 7.19. Lotes de montaje y condiciones*

Fuente: Elaboración propia.

![Figura 7.20. G13 reservas y cierre técnico](../../subdocumentos/07-plan-trabajo/graficos/revisada/gantt-control.pdf)

*Figura 7.20. G13 reservas y cierre técnico*

Fuente: Elaboración propia.

![Figura 7.21. Continuidad operacional M21--M56](../../subdocumentos/07-plan-trabajo/graficos/revisada/gantt-operacion.pdf)

*Figura 7.21. Continuidad operacional M21--M56*

Fuente: Elaboración propia.

El montaje se concentra en el piloto M6 y los lotes externos M7--M9, sin trabajos físicos
programados durante diciembre--abril bajo SA-01. El escalamiento de plataformas de terceros
M13--M15 es lógico. Las órdenes de montaje requieren firma de adhesión aplicable, stock recibido,
ventana normal de paso y reserva del proveedor por terminal. Una condición incumplida se trata
como desviación del escenario y exige reprogramación técnica y financiera, sin declarar equipos
instalados ni activar servicios de una unidad que aún no fue recibida.

Para los cierres invernales sucesivos del paso Los Libertadores se verifica semanalmente
la posición de los camiones y la disponibilidad de cada terminal; el cronograma no supone
que un único cierre de doce días represente toda la exposición. Los kits deben estar recibidos
antes de liberar cada lote. Se atiende primero en un terminal nacional disponible durante el
paso normal del camión y se utiliza la reserva de agenda del proveedor para reagrupar unidades.
Si los cierres consumen la ventana del lote, el Jefe de Proyecto registra la desviación,
actualiza el riesgo y contrasta reprogramación, activación y caja; no utiliza una holgura
agregada de integración para justificar montaje fuera de su ventana ni desplaza automáticamente
los hitos de aceptación.

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
Tabla 7.6 la muestra para los 182 equipos audIT.

**Tabla 7.5.** Equipos audIT montados al cierre de cada mes

| Mes | Modalidad de ejecución | Nuevos | Acumulados |
|---|---|---|---|
| M6 | Piloto interno San Bernardo | 10 | 10 |
| M7 | Cinco terminales, proveedor externo | 60 | 70 |
| M8 | Cinco terminales, proveedor externo | 60 | 130 |
| M9 | Cinco terminales, proveedor externo | 52 | 182 |
| M10--M56 | Operación, reposición y crecimiento según orden | 0 de alta inicial | 182 de configuración inicial |

*Fuente: calendario de instalación del escenario económico de referencia; piloto incluido en los 182 equipos, sin duplicarlo.*

La curva es el escenario de contratación, no evidencia de montaje ejecutado. Incluye 148 camiones
propios y 34 de terceros sin equipo; la distribución de los 34 entre lotes exige adhesión y paso
confirmados. La firma por RUT, el consentimiento de cada conductor, el montaje y la activación
se miden por separado. Para quien no haya completado esas condiciones se mantiene modalidad
de datos o documental y se registra la diferencia frente al presupuesto. No se transforma la meta
de adhesión M16/M21 en una instalación retroactiva.

Los cinco terminales reciben 12 kits cada uno en M7 y M8. En M9 San Bernardo recibe 12 y cada
terminal regional diez. audIT conserva banco y recepción; el proveedor aporta 401,33 horas
de puesto para los 172 montajes externos. Las 210 balizas iniciales se montan M7--M9, a razón
de 70 por mes y 15 minutos presupuestados cada una; las 21 de reposición son stock. Los cinco
lectores de portería se prueban M5--M6, dos horas por lector. Los 19 equipos a bordo de reserva
no se cuentan como altas iniciales. El criterio de montaje exige permanecer dentro de la
estadía normal; los 140 minutos son hipótesis a validar, no una ampliación de la estadía.

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
de tráfico del despliegue azul-verde y la autoriza el Jefe de Proyecto con el Líder de Operación. Se preservan los registros transaccionales y se cotejan viajes, documentos y eventos por identificador. El ensayo CP-SYS-20 comprueba reenvío y deduplicación antes del paso. El firmware retorna por A/B ante fallo de arranque; la imagen del terminal respalda la recuperación presencial en una visita posterior si resulta necesaria (sección 4.3.2).

> **Compromiso C-02.** audIT ensaya la reversión de cada servicio antes de cada paso a producción y la mantiene disponible durante la estabilización posterior.
>
> Métrica: Reversión de un servicio en la nube en no más de 15 minutos, sin pérdida de eventos. Se verifica en: Ensayo de reversión en preproducción antes de cada paso a producción. Fuente: Caso, numeral 13.3, p. 27 y FEP01, Artículo 17.1, p. 12.

### 7.3.4 Marcha blanca de la Etapa 1 y de la Etapa 2

Cada marcha blanca termina sólo cuando se cumplen a la vez las seis condiciones del FEP01, Artículo 17.3, p. 13. El
plan las convierte en indicadores con umbral, medidos cada día y evaluados sobre las cuatro últimas
semanas. La Tabla 7.7 los declara para las dos etapas.

**Tabla 7.6.** Condiciones de cierre de cada marcha blanca y su umbral

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
terminal en el horario de relevo, como compromete la sección 7.2.4.

**Marcha blanca de la Etapa 2.**
En agosto y septiembre de 2028 la Etapa 2 convive con la Etapa 1 en producción. El portal del cliente
muestra posición sólo de los camiones con autorización vigente, los retornos se proponen sin asignarse
automáticamente y el cálculo de emisiones se ejecuta sobre los dos meses completos. La marcha blanca
incluye la semana de Fiestas Patrias, que pone a prueba la operación con restricción vehicular sin que
ocurra ningún paso a producción.

Si una marcha blanca no cumple las seis condiciones, se extiende por cuenta de audIT sin mover las fechas
siguientes (FEP01, Artículo 17.3, p. 13). La red de T-15 calcula el margen por actividad y límite contractual; una extensión requiere revisar la fecha de aceptación, capacidad y reserva consumida. La Etapa 2 mantiene la reserva A23 y la fecha de H12.

## Referencias

Project Management Institute. (2019). *Practice Standard for Work Breakdown Structures* (3.ª ed.).

Transportes Curimón S.A. (2026). *Bases administrativas para la preparación de la propuesta: Licitación Pública Internacional N.º TFEP-01/2026* (Documento FEP01).

Transportes Curimón S.A. (2026). *Bases técnicas del Caso 10, Transporte de Carga: Licitación Pública Internacional N.º TFEP-01/2026* (Documento FEP03).

Transportes Curimón S.A. (2026). *Bases técnicas transversales para la preparación de la propuesta: Licitación Pública Internacional N.º TFEP-01/2026* (Documento FEP02).

Transportes Curimón S.A. (2026). *Comunicado 10: Estructura obligatoria de las propuestas preparatorias y técnica final* (Comunicado de la licitación TFEP-01/2026).

## Declaración de uso de IA

Conforme al Comunicado 10, sección 7.2, cada sección de este subdocumento y cada formulario asociado declara la herramienta de inteligencia artificial generativa usada, su finalidad, el nivel de uso en texto y en diagramas según la escala oficial de esa sección, y quién revisó y qué verificó. Esta declaración se consolida en el Formulario A-6.

| Sección | Herramienta | Finalidad del uso | Nivel en texto | Nivel en diagramas | Revisión humana (quién y qué verificó) |
|---|---|---|---|---|---|
| S7, T-14, T-15, T-18, EDT y Gantt | OpenAI Codex | Conciliación con la entrega económica 3.2, generación de fuentes y salidas, cálculo y comprobación documental | Alto | Alto | D2, Analista de Planificación y Calidad: revisión humana de esta corrección por realizar antes de emitir. Las revisiones de versiones previas no se extienden automáticamente a esta edición. |
