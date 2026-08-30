
<!-- ===== página 1 / 49 ===== -->

### FORMULACIÓN DE PROYECTOS

### BASES TÉCNICAS

PARA LA PREPARACIÓN

DE LA PROPUESTA

Versión 1.0

Fecha Documento: 18-08-2026
<!-- ===== página 2 / 49 ===== -->

### Bases Técnicas Transporte de Carga

Transportes Curimón S.A. — cuando la responsabilidad y el control no coinciden

| Asignatura | Taller de Formulación de Proyectos Informáticos — ICI-5444 |
| --- | --- |
| Unidad académica | Escuela de Informática, Pontificia Universidad Católica de Valparaíso |
| Profesor | Antonio Moya Villegas — antonio.moya@pucv.cl |
| Industria | Transporte terrestre de carga por carretera, con flota propia y transportistas subcontratados |
| Mandante | Transportes Curimón S.A. (empresa ficticia) |
| Operación | 374 camiones, 454 conductores, 96.000 viajes y 41 millones de kilómetros al año, entre Antofagasta y Puerto Montt, más cruce fronterizo a Mendoza |
| Condición especial | El 60 % de la capacidad no pertenece a la compañía y sus 258 conductores no son sus trabajadores. La empresa responde por viajes que no controla |
| Documentos que rigen | Bases Administrativas FEP01.26 y Bases Técnicas Transversales FEP02.26 |
| Duración del contrato | 56 meses: implementación en dos etapas y 36 meses de operación |
| Versión | 1.0 — agosto de 2026 |

> Este documento no es una especificación de requerimientos. Es la descripción de una operación real, con sus datos, sus dolores, sus contradicciones internas y sus vacíos. Identificar qué es funcional y qué no lo es, completar lo que falta con supuestos declarados y con reglas de negocio propias de la industria, investigar aquello que el documento no explica, y traducir todo ello en un alcance, una arquitectura, un plan y una estrategia de puesta en producción, es exactamente el trabajo que se está licitando y lo que será evaluado.
<!-- ===== página 3 / 49 ===== -->

CONTENIDO

| Título | Contenido | Capítulos |
| --- | --- | --- |
| I- El mandante y el encargo | Cómo llegamos a esta licitación, la compañía, su flota propia y subcontratada, sus cifras, sus personas y los nodos de su red. | 1-3 |
| II - La operación tal como es hoy | El ciclo del viaje, la jornada del conductor, los documentos, el costo, los sistemas existentes, la conectividad y los indicadores del problema. | 4-7 |
| III - Lo que dicen quienes operan | Diez entrevistas de levantamiento, incluidas las de una conductora, un dueño de camión y una clienta, con sus contradicciones intactas. | 8 |
| IV - Lo que el mandante espera | Expectativas de negocio, restricciones no negociables, exclusiones, marco normativo y prioridades. | 9-13 |
| V - Antecedentes para el dimensionamiento | Volumetría entregada y volumetría a estimar, parámetros del caso y decisiones deliberadamente no resueltas. | 14-16 |
| VI - Lo que debe producir el proponente | El trabajo de traducción exigido, los criterios de aceptación y cómo se evaluará este caso. | 17-19 |
| VII: Anexos del caso | Mapa de sistemas y flujos actuales, perfil del viaje y calendario operacional, y glosario de la industria. | A-C |

Cómo leer este documento

Los Títulos | y II describen la operación. Se entregan con detalle porque de ellos dependen todas las decisiones de diseño: no hay atajo que permita saltarlos.

El Título III recoge las voces de quienes operan y también las de tres personas que están fuera de la estructura de la compañía: una conductora, un dueño de camión subcontratado y la gerenta de logística del cliente mayor. No están de acuerdo entre sí, y esa discrepancia es información, no ruido: revela dónde el proyecto va a encontrar resistencia y qué tensiones habrá que arbitrar.

El Título IV expresa lo que el mandante espera, deliberadamente en lenguaje de negocio y no de requerimientos. El Título V entrega los datos duros que la compañía conoce, señala cuáles debe estimar el proponente, fija los parámetros de los requisitos que las Bases Técnicas Transversales dejaron abiertos al caso, y enumera veintiséis decisiones que el cliente no ha tomado.

El Título VI describe el trabajo exigido y los criterios con que se juzgará. Conviene leerlo primero y volver a él al final.
<!-- ===== página 4 / 49 ===== -->

> Tres particularidades de este caso. La primera es que la responsabilidad y el control no coinciden. El 60 % de los camiones no son de la compañía y las 258 personas que los conducen no son sus trabajadores, pero la compañía responde ante el cliente por la carga, ante la autoridad por las condiciones del viaje que despacha y ante su seguro por el siniestro. Todo lo que dependa de esos terceros deberá conseguirse por contrato, por incentivo o por diseño, nunca por instrucción. La segunda es que el dato más importante está fuera de la empresa. El accidente que originó esta licitación ocurrió porque un conductor había manejado antes para otro cliente, algo que la compañía no tenía forma de saber. El cliente mayor exige, para 2029, acreditar la jornada de cada viaje incluidos los camiones subcontratados. Ése es el problema central y no tiene una solución evidente. La tercera es que el cronograma no lo decide el proveedor: lo decide la física de la operación. Todo equipamiento a bordo sólo puede instalarse cuando el camión pasa por un terminal, y un camión pasa cada seis días en promedio, con un 22 % de la flota subcontratada que aparece menos de una vez al mes. Durante buena parte del proyecto convivirán camiones equipados y camiones sin equipar.
<!-- ===== página 5 / 49 ===== -->

### EL MANDANTE Y EL ENCARGO

### CAPÍTULO 1 CÓMO LLEGAMOS A ESTA LICITACIÓN

El 14 de febrero de 2026, a las 04:40, un camión salió de la calzada en el kilómetro 312 de la Ruta 5 Sur. El conductor fue rescatado, estuvo hospitalizado tres semanas y se recuperó. No hubo terceros involucrados. El camión no era de la compañía. Era de un transportista subcontratado que trabaja con ella desde hace nueve años.

La investigación estableció que el conductor había manejado el día anterior para otra empresa y no había completado su período de descanso antes de tomar el viaje que la compañía le asignó a las 22:00.

Los registros de la compañía estaban impecables. Mostraban que ese conductor llevaba once horas sin conducir para ella. Lo que no mostraban —lo que la compañía no tenía forma de saber— es qué había hecho ese conductor durante esas once horas.

«Nosotros cumplimos», dijo Enrique Valdebenito Rioseco, gerente general, en el directorio del 3 de marzo. «Y eso es exactamente lo que me asusta. Cumplimos con todo lo que estaba a nuestro alcance y aun así despachamos a una persona que no estaba en condiciones de manejar. El dato que hacía falta no estaba en ninguno de nuestros sistemas porque no es nuestro.»

La autoridad laboral abrió una investigación. El principal cliente suspendió el contrato durante seis semanas mientras auditaba. La compañía aseguradora subió la prima en la renovación.

En abril llegó el segundo golpe, más pequeño y más humillante.

Una fiscalización en ruta detuvo a un camión de la compañía que transportaba sustancias peligrosas. La documentación no calzaba con la carga que efectivamente llevaba, y el certificado del curso obligatorio del conductor había vencido tres semanas antes.

El camión quedó inmovilizado catorce horas, hubo multa, y el cliente minero al que servía abrió una investigación propia sobre el proveedor.

El vencimiento del certificado estaba en una planilla que se actualiza cuando alguien se acuerda. Nadie se acordó.

Y en junio llegó la tercera noticia, que no vino de afuera sino de adentro.

Gabriela Ossandón Prieto, que asumió como gerenta de administración y finanzas en enero, construyó por primera vez en la historia de la compañía un modelo de costo por kilómetro que separaba las rutas en lugar de prorratear por ingreso.

El resultado fue que tres de los ocho contratos principales —que en conjunto son el treinta y uno por ciento de los ingresos — se estaban sirviendo por debajo del costo. Uno de ellos con un margen de menos catorce por ciento, sostenido durante cuatro años.

«No es que alguien se haya equivocado», explicó en el mismo directorio. «Es que las tarifas se negociaron el 2021 sobre una estructura de costos que ya no existe, y como repartimos los costos por ingreso, las rutas buenas venían pagando las malas. Nadie podía verlo porque el dato para verlo nunca se juntó.»
<!-- ===== página 6 / 49 ===== -->

La semana siguiente, la exportadora que representa el diecinueve por ciento de los ingresos comunicó por escrito sus condiciones para la renovación de 2029. Son cuatro: documento electrónico de transporte integrado de extremo a extremo; posición de la carga disponible para el cliente en tiempo real; reporte verificado de emisiones por tonelada-kilómetro; y acreditación del cumplimiento de la jornada del conductor en cada viaje, incluidos los camiones subcontratados.

El directorio aprobó licitar el proyecto. En el acta quedó consignada una advertencia que el gerente general pidió incorporar: «el sesenta por ciento de nuestra capacidad no nos pertenece y esas personas no son nuestros trabajadores. Cualquier solución que suponga que podemos darles una orden va a fracasar el primer día».

> Este documento es el resultado de seis meses de levantamiento en los cinco terminales, en los dos talleres, en la torre de programación, en puntos de carga de clientes y arriba de camiones en ruta, y de treinta y siete entrevistas, de las cuales once fueron a transportistas subcontratados. No es una especificación. Es la descripción, lo más honesta que el CLIENTE ha sido capaz de hacer, de una operación real con sus datos, sus dolores, sus contradicciones internas y sus vacíos. Traducir esto en requerimientos es el trabajo del PROPONENTE, y es precisamente lo que se evalúa.

### CAPÍTULO 2 LA COMPAÑÍA

### 2.1 Identificación

| Antecedente | Detalle |
| --- | --- |
| Razón social | Transportes Curimón S.A. |
| Giro | Transporte terrestre de carga por carretera: carga general paletizada, carga refrigerada, carga a granel, sustancias peligrosas y contenedores desde y hacia puerto, |
| Condición | Sociedad anónima cerrada. Opera con flota propia y con transportistas subcontratados, que son personas naturales o empresas de uno a cuatro camiones. |
| Cobertura | Ruta 5 entre Antofagasta y Puerto Montt, rutas transversales asociadas, y cruce fronterizo hacia Mendoza por el paso Los Libertadores. |
| Casa matriz y terminal principal | San Bernardo, Región Metropolitana. |
| Inicio de operaciones | 1989. Incorporación de transportistas subcontratados a partir de 2004; hoy son la mayoría de la capacidad. |
| Ingresos anuales | $ 78.000 millones. |
| Propiedad | Sociedad anónima cerrada. 78 % de la familia fundadora en segunda generación; 22 % de un fondo de inversión incorporado en 2019. |
<!-- ===== página 7 / 49 ===== -->

> El dato que define este caso está en la tabla anterior y conviene subrayarlo: el 60 % de la capacidad de transporte de esta compañía no le pertenece, y las personas que conducen esos camiones no son sus trabajadores. La compañía responde ante el cliente por la carga, responde ante la autoridad por las condiciones del viaje que despacha, y responde ante su seguro por el siniestro; pero no manda sobre el equipo ni sobre la persona, En este caso la responsabilidad y el control no coinciden, y esa brecha es el problema.

### 2.2 La flota

| Componente | Cantidad | Observación |
| --- | --- | --- |
| Tractocamiones propios | 148 | Antiguedad promedio 6,4 años. 61 con telemetría de fábrica que hoy no se descarga. |
| Semirremolques propios | 210 | Rampla plana, furgón seco, furgón refrigerado, tolva y portacontenedores. |
| Camiones de transportistas subcontratados | 226 | Pertenecientes a 148 personas naturales o empresas de uno a cuatro camiones. |
| Capacidad total gestionada | 374 camiones | El 60,4 % no es propiedad de la compañía. |
| Camiones habilitados para sustancias peligrosas | 18 | Con señalización, equipamiento y conductores con curso específico vigente exigible. |
| Equipos refrigerados | 44 | 12 % de la flota. Concentran su actividad entre diciembre y abril. |
| Camiones con dispositivo de posicionamiento | 340 de 374 | 34 camiones subcontratados no tienen ninguno. Los que tienen se reparten entre tres proveedores distintos. |
| Talleres propios | 2 | San Bernardo y Los Ángeles. El resto de la mantención se subcontrata en ruta. |
| Estanque de combustible propio | 1 | En San Bernardo. El resto del abastecimiento es con tarjeta en una red de estaciones de servicio. |

### 2.3 Cifras de la operación

| Indicador | Valor |
| --- | --- |
| Viajes al año | = 96.000 |
| Kilómetros recorridos al año | = 41.000.000 |
| Toneladas transportadas al año | = 2.400.000 |
| Conductores que operan bajo la programación de la compañía | = 454: 196 propios y 258 de transportistas subcontratados |
| Clientes activos | 84; ocho contratos principales concentran el 71 % del ingreso |
| Cliente mayor | Una exportadora que representa el 19 % de los ingresos |
| Cruces fronterizos al año por Los Libertadores | = 1.900 |
| Terminales | 5: San Bernardo, Antofagasta, Talca, Los Ángeles y Puerto Montt |
| Estructura de costo | Pago a transportistas subcontratados 38 %, combustible de flota propia 14 %, conductores propios 12 %, administración y otros 11 %, mantenimiento 5 %, neumáticos 4 %, peajes 4 %, seguros 3 % |
<!-- ===== página 8 / 49 ===== -->

| Indicador | Valor |
| --- | --- |
| Margen operacional consolidado | 9 %, con tres contratos principales bajo costo |
| Frecuencia con que un camión pasa por un terminal | cada 6 días en promedio; el 22 % de la flota subcontratada pasa menos de una vez al mes |

### 2.4 Las personas

| Categoría | Dotación | Régimen |
| --- | --- | --- |
| Personal propio | 336 | Jornada ordinaria, salvo conductores y torre de programación. |
| Conductores propios | 196 | Jornada de conductor sujeta al régimen especial de la normativa laboral: límites de conducción continua, descansos y horas mensuales. |
| Torre de programación y operaciones | 22 | Turnos 24x7. Asignan viajes, siguen la ruta y resuelven contingencias. |
| Mantenimiento y taller | 46 | Dos talleres propios, con turnos. |
| Administración de transportistas subcontratados | 8 | Contratos, liquidaciones, documentación y acreditación de 148 terceros. |
| Prevención de riesgos y seguridad | 11 | Jornada, siniestralidad, carga peligrosa y seguridad de la carga en ruta. |
| Control de flota | 6 | Operan tres plataformas distintas de posicionamiento satelital. |
| Comercial | 9 | 84 clientes activos y ocho contratos principales. |
| Administración y finanzas | 24 | Incluye liquidación a terceros, peajes, combustible y facturación. |
| Gerencia | 5 | Jornada ordinaria. |
| Área de tecnologías de información | 9 | Para 5 terminales, 2 talleres y una flota que no está en ninguna parte fija. |
| Conductores de transportistas subcontratados | 258 personas | No son trabajadores de la compañía. Conducen bajo su programación y, en muchos casos, también para otros clientes. |

> Los 258 conductores de transportistas subcontratados son el punto ciego de toda la operación. La compañía les asigna viajes, depende de ellos para cumplir con sus clientes y responde por lo que ocurra durante esos viajes, pero no los contrata, no los remunera, no los capacita por obligación laboral y no conoce lo que hacen cuando no están conduciendo para ella. El accidente del 14 de febrero ocurrió exactamente en ese punto ciego.
<!-- ===== página 9 / 49 ===== -->

### CAPÍTULO 3 EL TERRITORIO Y SUS NODOS

Esta compañía no tiene un recinto: tiene una red. Su operación ocurre a lo largo de tres mil kilómetros de ruta, en instalaciones que en su mayoría no le pertenecen, y su unidad productiva —el camión— pasa la mayor parte del tiempo lejos de cualquier lugar donde la empresa tenga presencia.

| Nodo | Qué ocurre allí | Condiciones relevantes |
| --- | --- | --- |
| Terminal San Bernardo | Casa matriz, torre de programación 24x7, taller principal, estanque de combustible y patio de maniobras. | Único punto donde converge todo. Es donde se instala y se mantiene cualquier equipamiento a bordo. |
| Terminales regionales | Antofagasta, Talca, Los Ángeles y Puerto Montt. Relevo de conductores, descanso, apoyo mecánico y estacionamiento. | Enlace propio de un proveedor, sin respaldo en tres de los cuatro. |
| La cabina del camión | El lugar de trabajo real. Conducción, descanso, comunicación con la torre y registro de la jornada. | En movimiento, con cobertura intermitente, con el conductor solo y sin posibilidad de manipular un dispositivo mientras conduce. |
| La ruta | 3.000 km de carretera, con tramos de cobertura móvil nula que superan los 80 km continuos en el norte y en zonas cordilleranas. | Es donde ocurre el 100 % del riesgo y donde la empresa tiene la menor visibilidad. |
| Puntos de carga del cliente | Recepción del camión, carga, emisión de documentos y salida. | No son instalaciones de la compañía. Sus tiempos, sus reglas y sus sistemas los define el cliente. |
| Puntos de descarga | Entrega de la carga, conformidad del destinatario y devolución de documentos. | Igual que los anteriores: la compañía es visita. La conformidad se obtiene en papel. |
| Plazas de pesaje | Control de peso por eje de la autoridad vial. | El camión lo carga el cliente y lo pesan a la compañía. Un sobrepeso es multa e inmovilización. |
| Paso fronterizo Los Libertadores | Cruce hacia Mendoza, con control aduanero y migratorio de dos países. | Cierra por nieve entre junio y septiembre, en episodios impredecibles que han llegado a 12 días continuos. |
| Talleres en ruta | Mantención correctiva subcontratada cuando un camión falla lejos de un terminal. | Proveedores externos cuya intervención hoy no queda registrada en la hoja de vida del equipo. |
| Estaciones de servicio de la red | Abastecimiento de combustible con tarjeta fuera de San Bernardo. | El consumo se conoce por la liquidación mensual de la red, no en el momento de la carga. |
<!-- ===== página 10 / 49 ===== -->

### LA OPERACIÓN TAL COMO ES HOY

CAPÍTULO 4 EL CICLO DEL VIAJE

Lo que sigue es la descripción del proceso tal como ocurre, no como debería ocurrir. Se entrega con este nivel de detalle porque de él dependen las decisiones de alcance, de arquitectura y de trazabilidad que el PROPONENTE deberá tomar.

La unidad de esta operación es el viaje: una carga que sale de un punto y llega a otro, con un camión, un conductor y un documento. Ocurre noventa y seis mil veces al año y casi siempre lejos de cualquier lugar donde la compañía tenga presencia física.

### 4.1 La tarifa y el contrato

Los ocho contratos principales concentran el setenta y uno por ciento del ingreso y se negocian por tramo: un valor por viaje o por tonelada entre un origen y un destino, con condiciones de frecuencia, de tipo de equipo y de tiempo de tránsito.

Esas tarifas se negociaron en distintos momentos, la más antigua en 2021, sobre una estructura de costos que ya no existe. El combustible, los neumáticos, la remuneración del conductor y el seguro subieron de forma desigual, y el reajuste que contemplan los contratos no sigue esa canasta.

Hasta junio de 2026 la compañía no sabía si un contrato ganaba o perdía, porque asignaba los costos a los contratos en proporción a su ingreso. Con esa regla, todo contrato grande parecía razonable.

### 4.2 La programación y la asignación del viaje

La torre de programación opera veinticuatro horas al día. Recibe los requerimientos de los clientes, arma la carga de trabajo del día siguiente y asigna cada viaje a un camión.

Asignar un viaje significa decidir simultáneamente varias cosas: qué camión está o estará disponible en el origen, si el equipo es el adecuado para esa carga, si el conductor tiene jornada suficiente para completar el tramo, si sus habilitaciones están vigentes, y qué hará ese camión después de descargar.

Todo eso lo resuelven veintidós personas mirando una pizarra, tres pantallas de posicionamiento satelital de proveedores distintos y una planilla, y hablando por teléfono con conductores y con dueños de camión.

La decisión sobre qué hará el camión después de descargar es la más importante del negocio y la menos sistematizada. El veintiséis por ciento de los kilómetros recorridos al año son con el camión vacío.

### 4.3 La jornada del conductor, y por qué no se conoce

La normativa laboral chilena somete a los conductores de carga a un régimen especial: límites a las horas de conducción continua, descansos mínimos obligatorios y un tope de horas mensuales. No es una recomendación: es una obligación cuyo cumplimiento la empresa debe poder acreditar.

Para los ciento noventa y seis conductores propios, la compañía lleva ese control con un registro que el conductor completa y firma, complementado con el libro de asistencia del terminal. Los camiones nuevos tienen tacógrafo digital, pero su información no se descarga: nadie definió quién lo hace ni con qué frecuencia.
<!-- ===== página 11 / 49 ===== -->

Para los doscientos cincuenta y ocho conductores de transportistas subcontratados, la compañía no lleva control alguno. Lo que sabe es cuándo les asignó un viaje y cuándo lo terminaron.

Y ahí está el vacío que produjo el accidente del 14 de febrero. Un conductor de un tercero puede haber conducido ocho horas para otro cliente esa mañana. Cuando la compañía le asigna un viaje esa noche, ve un conductor que lleva once horas sin trabajar para ella, y despacha.

El cliente mayor exige, para 2029, acreditación del cumplimiento de jornada en cada viaje, incluidos los camiones subcontratados. La compañía no tiene hoy ninguna forma de producir esa acreditación.

### 4.4 Las habilitaciones del conductor y del equipo

Un viaje sólo puede ejecutarse si concurren varias vigencias: la licencia de conducir del conductor, su examen médico cuando corresponde, el curso específico si la carga es peligrosa, la revisión técnica del tractocamión y del semirremo!que, el permiso de circulación, el seguro obligatorio y la póliza de responsabilidad.

Son siete u ocho fechas de vencimiento por cada uno de los cuatrocientos cincuenta y cuatro conductores y de los trescientos setenta y cuatro camiones. Del orden de seis mil fechas vivas.

Todas están en planillas. Una para conductores propios, otra para conductores de terceros, otra para equipos propios y otra para equipos de terceros, mantenidas por personas distintas y actualizadas cuando alguien se acuerda.

Nada en el momento de asignar un viaje verifica que esas vigencias estén al día. Eso fue lo que ocurrió en abril con el certificado de carga peligrosa vencido tres semanas antes.

### 4.5 La carga y el documento de transporte

El camión llega al punto de carga del cliente, espera su turno, se carga y recibe la documentación. El documento electrónico de transporte debe estar emitido antes de que el vehículo se mueva.

Hoy ese documento se emite desde el sistema contable de la compañía, redigitando la información desde la orden de transporte que ya existe en el sistema de gestión. Cuando el punto de carga no tiene cobertura móvil —yY varios no la tienen— el documento se emite antes o después, y el camión circula en una situación que la compañía prefiere no describir con precisión.

El peso lo determina el cliente al cargar. Si en una plaza de pesaje resulta que el camión excede el peso por eje permitido, la multa y la inmovilización recaen sobre la compañía, no sobre quien cargó. En 2025 hubo ciento cuarenta y dos detenciones por sobrepeso, con dieciocho horas de inmovilización promedio.

### 4.6 La ruta, la posición y la cobertura

Trescientos cuarenta de los trescientos setenta y cuatro camiones tienen dispositivo de posicionamiento satelital. Los treinta y cuatro restantes, todos de transportistas subcontratados, no tienen ninguno: se sabe dónde están porque el conductor llama.

Los que tienen se reparten entre tres proveedores distintos, porque el dueño de camión contrata el suyo. Control de flota opera tres pantallas simultáneas con tres formas distintas de representar lo mismo, y no existe una vista única de la flota.

Hay tramos de ruta con más de ochenta kilómetros continuos sin cobertura móvil, en el norte y en zonas cordilleranas. Durante esos tramos no hay posición, no hay comunicación y no hay registro, salvo el que el propio dispositivo almacene y envíe después.
<!-- ===== página 12 / 49 ===== -->

El cliente mayor exige, para 2029, posición de la carga en tiempo real disponible para él. Eso supone resolver simultáneamente los tres proveedores, los treinta y cuatro camiones sin equipo, los tramos sin cobertura y — la parte que nadie ha discutido— si el dueño de un camión está dispuesto a que su posición se comparta con un tercero.

### 4.7 La espera en los puntos de carga y descarga

Un camión que espera es un camión que no produce. En 2025 el tiempo medio de espera en un punto de carga fue de tres horas y diez minutos, con casos de más de ocho horas en temporada de fruta.

Los contratos contemplan un tiempo libre de espera y un cobro a partir de allí. La compañía facturó por ese concepto trescientos cuarenta millones de pesos y los clientes objetaron el setenta y uno por ciento.

La razón es siempre la misma: la hora de llegada y la de salida las anota el conductor en un papel, a veces de memoria al terminar el día. Frente a un cliente que dispone de su propio registro de portería, ese papel no sostiene nada.

### 4.8 La descarga y la conformidad

En el destino se entrega la carga y se obtiene la conformidad del destinatario, que es la prueba de que la compañía cumplió. Esa conformidad se firma en un papel que el conductor guarda y entrega en el terminal cuando pasa por uno, lo que puede tardar días.

El cuatro coma dos por ciento de los documentos de respaldo llega incompleto, ilegible o no llega. Cada uno de esos casos es una factura que se demora o que se objeta, y en caso de un reclamo por faltante o daño, es una defensa que no existe.

### 4.9 El combustible, los peajes y los neumáticos

El combustible es el catorce por ciento del ingreso y el mayor costo controlable de la flota propia. Se abastece en el estanque de San Bernardo, donde se registra en una planilla, y con tarjeta en una red de estaciones, cuyo consumo se conoce en la liquidación mensual.

Eso significa que la compañía sabe cuánto combustible consumió un camión con hasta cuarenta días de desfase, y no puede relacionar el consumo con el viaje, con la ruta ni con el conductor.

El rendimiento declarado promedio de la flota propia es de dos coma tres kilómetros por litro. La dispersión entre camiones del mismo modelo y la misma ruta llega al diecinueve por ciento, y nadie ha investigado por qué.

Los peajes se pagan con dispositivo y se liquidan mensualmente. Los neumáticos se compran, se montan y se recapan, y su vida se controla en una planilla del taller que no distingue por posición ni por equipo.

### 4.10 El mantenimiento

La flota propia tiene un plan de mantenimiento preventivo por kilometraje. El kilometraje se toma del odómetro cuando el camión pasa por el taller, de modo que la fecha de la próxima mantención es una estimación.

Sesenta y un tractocamiones tienen telemetría de fábrica capaz de reportar kilometraje, consumo, códigos de falla y hábitos de conducción. Esa información no se descarga desde que se compraron los equipos.

Cuando un camión falla en ruta se recurre a un taller externo. Esa intervención se paga con una factura y no queda registrada en la hoja de vida del equipo, de modo que el historia! de mantenimiento de un camión está incompleto por diseño.
<!-- ===== página 13 / 49 ===== -->

De los camiones subcontratados la compañía no sabe nada: el mantenimiento es responsabilidad de su dueño y la única verificación es la revisión técnica vigente.

### 4.11 La liquidación al transportista subcontratado

Cada mes hay que liquidar a ciento cuarenta y ocho transportistas: cuántos viajes hizo cada camión, con qué tarifa, con qué descuentos por combustible anticipado, peajes, siniestros o incumplimientos, y con qué bonificaciones.

El proceso toma nueve días y lo ejecutan ocho personas. El once por ciento de las liquidaciones se corrige después de emitida, casi siempre porque el transportista reclama un viaje que no aparece o un descuento que no reconoce.

Los transportistas no tienen forma de ver sus viajes ni su liquidación en curso. Se enteran cuando les llega el documento, y si no están de acuerdo, llaman.

### 4.12 La carga peligrosa y el cruce fronterizo

Dieciocho camiones están habilitados para transportar sustancias peligrosas. Esa operación tiene reglas propias: documentación específica que debe acompañar a la carga, hoja de datos de seguridad, señalización del vehículo, equipamiento de emergencia, conductor con curso vigente y un plan de respuesta ante incidentes.

Tedo eso se verifica hoy con una lista de chequeo en papel que se completa en el terminal. La fiscalización de abril encontró que la documentación no correspondía a la carga que efectivamente llevaba el camión.

El cruce fronterizo hacia Mendoza suma mil novecientas operaciones al año, con documentación aduanera de dos países y con un paso que cierra por nieve entre junio y septiembre en episodios que han llegado a doce días continuos. Cuando el paso cierra, la compañía tiene camiones detenidos en ruta, carga comprometida y conductores en jornada que hay que resolver.

### CAPÍTULO 5 LOS SISTEMAS QUE EXISTEN HOY

El PROPONENTE deberá integrarse a este panorama. La columna de destino indica la decisión ya tomada por el CLIENTE; donde dice «decisión del proponente», la decisión no está tomada y debe fundamentarse en la propuesta.

| Sistema | Función | Destino |
| --- | --- | --- |
| Sistema de gestión de transporte, implantado en 2013 | Órdenes de transporte, asignación de viajes, tarifas, control de viajes y base de la liquidación a transportistas. | Decisión del PROPONENTE. Es el núcleo de la operación y la decisión de arquitectura más importante del caso, y debe resolverse con fundamento técnico y económico explícito. |
| Plataformas de posicionamiento satelital | Ubicación y eventos de los camiones. Tres proveedores distintos: uno contratado por la compañía y dos por los dueños de camión, | Se mantienen los equipos instalados. Unificar la vista es parte del alcance y su factibilidad debe verificarse con cada proveedor. 34 camiones no tienen ninguno. |
| Telemetría de fábrica de los tractocamiones | Kilometraje, consumo, códigos de falla y conducción, en 61 equipos propios. | No se interviene el vehículo. Su aprovechamiento como integración de solo lectura debe evaluarse y su factibilidad verificarse con cada fabricante. |
<!-- ===== página 14 / 49 ===== -->

| Sistema | Función | Destino |
| --- | --- | --- |
| Sistema de mantenimiento del taller, 2017 | Órdenes de trabajo, repuestos y plan preventivo de la flota propia. | Se mantiene o se reemplaza, con justificación. No recibe las intervenciones hechas en talleres externos en ruta. |
| Sistema contable y de facturación | Contabilidad, cuentas por pagar, remuneraciones y emisión de documentos tributarios, incluido el documento electrónico de transporte. | Se mantiene. Es el único emisor de documentos tributarios. Hoy recibe por redigitación lo que ya existe en el sistema de gestión. |
| Portal de la red de estaciones de servicio | Consumo de combustible con tarjeta, liquidado mensualmente. | Se integra. Es la única fuente del consumo fuera de San Bernardo y hoy llega con hasta 40 días de desfase. |
| Sistema del dispositivo de peaje | Pasadas y montos, liquidados mensualmente. | Se integra. |
| Planillas de cálculo | Vigencias de conductores y equipos, control de jornada, vida de neumáticos, tiempos de espera, siniestros, combustible del estanque propio, kilómetros vacíos y control de la carga peligrosa. | Deben desaparecer como sistema de registro. Ese es, en buena medida, el objeto de esta licitación. |
| Papel | Registro de jornada firmado por el conductor, conformidad de entrega del destinatario, lista de chequeo de carga peligrosa y anotación de horas de llegada y salida en los puntos del cliente. | Debe desaparecer como soporte probatorio. Es el origen del 71 % de objeciones a los cobros por espera y de la imposibilidad de acreditar la jornada. |

> El sistema de gestión de transporte de 2013 conoce el viaje que la compañía encargó, pero no conoce el viaje que efectivamente ocurrió. No sabe a qué hora llegó realmente el camión al punto de carga, cuántas horas condujo el conductor, cuánto combustible consumió, qué ruta tomó ni qué le pasó en el camino. Toda esa información existe —en tres plataformas de posicionamiento, en una telemetría que nadie descarga, en una liquidación de combustible que llega con cuarenta días de atraso y en papeles que viajan en la cabina— y nunca se junta.

### CAPÍTULO 6 CONECTIVIDAD, SEGURIDAD Y CONDICIONES DEL SITIO

| Elemento | Situación actual |
| --- | --- |
| Cobertura móvil en ruta | Discontinua. Hay tramos de más de 80 km continuos sín cobertura en el norte y en zonas cordilleranas, y la calidad varía por operador. Es la condición más determinante del diseño. |
| Enlace de los terminales | San Bernardo con dos proveedores. Los cuatro terminales regionales con un proveedor y sin respaldo en tres de ellos. |
| Sala de equipos | Recinto de 26 m? en San Bernardo, habilitado en 2013, con climatización tipo split, alimentación ininterrumpida de 20 minutos y acceso por credencial. No cumple los estándares del Capítulo 6 de las Bases Técnicas Transversales. |
<!-- ===== página 15 / 49 ===== -->

| Elemento | Situación actual |
| --- | --- |
| Equipamiento a bordo | Sólo puede instalarse, actualizarse o reemplazarse cuando el camión pasa por un terminal. Un camión pasa cada 6 días en promedio, y el 22 % de la flota subcontratada pasa menos de una vez al mes. |
| Condiciones de la cabina | Vibración, temperatura extrema en el norte, polvo, y alimentación eléctrica del vehículo. Todo equipamiento debe acreditar su comportamiento en esas condiciones y su instalación no puede afectar la garantía del vehículo. |
| El conductor conduciendo | No puede manipular ningún dispositivo mientras el vehículo está en movimiento. Cualquier interacción debe ocurrir con el camión detenido, y toda captura durante la marcha debe ser automática. |
| Puntos de carga y descarga del cliente | Instalaciones de terceros, con reglas, horarios y sistemas propios. Varios sin cobertura móvil. La compañía no puede instalar equipamiento en ellos. |
| Dispositivos de los transportistas subcontratados | Pertenecen a sus dueños. La compañía no puede intervenirlos, configurarlos ni exigir su reemplazo por la vía laboral. |
| Seguridad de la carga en ruta | Rutas y horarios con riesgo conocido de asalto. Existe un protocolo de comunicación con la torre y un botón de emergencia en parte de la flota, con cobertura desigual. |
| Talleres | San Bernardo y Los Ángeles, con red propia. Los talleres externos en ruta no tienen ninguna conexión con la compañía. |
| Paso fronterizo | Cobertura y sistemas de dos países. Los cierres por nieve se comunican por los canales oficiales y no están integrados a ningún sistema de la compañía. |

> La compañía ha sido explícita en cinco puntos. Primero: nada de lo que se proponga puede exigir al conductor una interacción mientras el vehículo está en movimiento. Segundo: el 60 % de la capacidad pertenece a terceros y la compañía no puede imponerles equipamiento, configuraciones ni herramientas por la vía laboral; todo lo que dependa de ellos debe conseguirse por contrato, por incentivo o por diseño, y su viabilidad debe estar argumentada. Tercero: la operación no puede depender de la cobertura móvil, que es discontinua por definición. Cuarto: el equipamiento a bordo sólo puede intervenirse cuando el camión pasa por un terminal, lo que impone un ritmo de despliegue que no se puede acelerar. Quinto: la compañía responde por la jornada del conductor que despacha y debe poder acreditarla, sea propio o de un tercero.

### CAPÍTULO 7 LO QUE DUELE: INDICADORES DEL PROBLEMA

Los siguientes datos corresponden al ejercicio 2025 y al primer semestre de 2026, y provienen de los registros de la compañía. Se entregan porque dimensionan el problema y porque el PROPONENTE deberá comprometer mejoras verificables sobre ellos.

### 7.1 Seguridad, jornada y habilitaciones

| Indicador | Valor | Referencia |
| --- | --- | --- |
| Conductores sobre los que existe control de jornada | 196 de 454 | 454 |
| Conocimiento de la jornada previa de un conductor de un tercero | inexistente | acreditable por viaje |
| Tacógrafos digitales cuya información se descarga | o) | todos |
<!-- ===== página 16 / 49 ===== -->

| Indicador | Valor | Referencia |
| --- | --- | --- |
| Verificación de vigencias en el momento de asignar un viaje | inexistente | bloqueante |
| Fechas de vencimiento vivas de conductores y equipos | = 6.000, en cuatro planillas separadas | en un solo registro |
| Siniestros con lesiones en los últimos 3 años | 4, uno de ellos grave | cero |
| Detenciones en ruta por sobrepeso | 142, con 18 horas de inmovilización promedio | bajo 10 |
| Detenciones por documentación de carga peligrosa | 1, con multa e inmovilización de 14 horas | cero |

### 7.2 El viaje, la posición y el cumplimiento al cliente

| Indicador | Valor 2025 |
| --- | --- |
| Viajes al año | = 96.000 |
| Kilómetros recorridos con el camión vacío | 26 % del total |
| Camiones sin dispositivo de posicionamiento | 34 de 374 |
| Plataformas de posicionamiento en uso simultáneo | 3, sin vista unificada |
| Tramos de ruta sin cobertura móvil | superiores a 80 km continuos en el norte y en zonas cordilleranas |
| Tiempo medio de espera en un punto de carga | 3 h 10 min; sobre 8 horas en temporada de fruta |
| Cobros por tiempo de espera facturados y objetados | 5 340 millones facturados; 71 % objetado |
| Registro de la hora de llegada y salida en el punto del cliente | anotación del conductor en papel |
| Documentos de respaldo de entrega que llegan incompletos, ¡legibles o no llegan | 4,2% |
| Tiempo entre la entrega y la disponibilidad del respaldo en el terminal | hasta varios días |
| Posición de la carga disponible al cliente | inexistente |
| Emisiones por tonelada-kilómetro | no se mide |

### 7.3 Costo, tarifa y liquidación

| Indicador | Valor | Referencia |
| --- | --- | --- |
| Contratos principales servidos bajo costo | 3 de 8, equivalentes al 31 % del ingreso | cero |
| Margen del peor de ellos | —-14 %, sostenido durante 4 años |  |
| Método de asignación de costos a contratos hasta junio de 2026 | prorrateo por ingreso | por ruta y por viaje |
| Desfase con que se conoce el consumo de combustible de un camión | hasta 40 días | por viaje |
| Dispersión de rendimiento entre camiones del mismo modelo y ruta | 19 %, sin investigar | explicada |
<!-- ===== página 17 / 49 ===== -->

| Indicador | Valor | Referencia |
| --- | --- | --- |
| Duración de la liquidación mensual a 148 transportistas | 9 días, 8 personas | automática |
| Liquidaciones corregidas después de emitidas | 11% | bajo 1% |
| Visibilidad del transportista sobre sus viajes y su liquidación en curso | inexistente | en línea |
| Conocimiento del costo real por kilómetro por ruta | desde junio de 2026, en una planilla | sistemático |

### 7.4 Mantenimiento, equipo y tecnología

| Indicador | Valor |
| --- | --- |
| Tractocamiones con telemetría de fábrica sin utilizar | [3 |
| Origen del kilometraje para el plan preventivo | odómetro leído cuando el camión pasa por el taller |
| Intervenciones de talleres externos registradas en la hoja de vida del equipo | ninguna |
| Conocimiento del estado de mantenimiento de los camiones subcontratados | sólo la revisión técnica vigente |
| Control de vida de neumáticos | planilla del taller, sin distinguir posición ni equipo |
| Frecuencia con que un camión pasa por un terminal | cada 6 días en promedio; 22 % de los subcontratados, menos de una vez al mes |
| Personal del área de tecnologías de información | 9, para 5 terminales, 2 talleres y una flota en movimiento |
| Sistemas que deben consultarse para reconstruir un viaje completo | 5, más dos planillas y un papel |

> Ninguno de estos indicadores se resuelve comprando software. Esta compañía responde por viajes que ocurren a mil kilómetros de distancia, ejecutados en su mayoría por camiones que no son suyos y por personas que no son sus trabajadoras, en tramos donde no hay cobertura y con un dato crítico —cuántas horas lleva conduciendo esa persona— que sencillamente está fuera de su alcance. El PROPONENTE que entienda que el problema de este caso es que la responsabilidad y el control no coinciden, y que diseñe para conseguir información de quien no está obligado a dársela, tendrá una ventaja evidente sobre quien ofrezca módulos.
<!-- ===== página 18 / 49 ===== -->

### LO QUE DICEN QUIENES OPERAN

### CAPÍTULO 8 ENTREVISTAS DE LEVANTAMIENTO

Las siguientes son transcripciones editadas de las entrevistas de levantamiento sostenidas entre marzo y agosto de 2026, en los cinco terminales, en los dos talleres, en puntos de carga de clientes y arriba de camiones en ruta. Once de ellas fueron a transportistas subcontratados. Se entregan con sus contradicciones intactas, porque las contradicciones son parte del problema.

El PROPONENTE debe leerlas como lo que son: la palabra de personas que conocen muy bien su parte de la operación y que no tienen por qué conocer la de los demás, ni tienen por qué saber de sistemas. Distinguir el hecho de la opinión, la necesidad del capricho y el problema de la solución que la persona ya se imaginó es parte del trabajo profesional que se está licitando.

> Enrigue Valdebenito Rioseco Gerente General

> Voy a partir por el accidente porque todo lo demás sale de ahí. Nosotros cumplimos con todo lo que estaba a nuestro alcance y aun así despachamos a una persona que no estaba en condiciones de manejar. Eso me quita el sueño más que cualquier número.

> El dato que faltaba no estaba en ninguno de nuestros sistemas porque no es nuestro. Ese conductor había manejado para otro cliente esa mañana. Nosotros vimos a alguien que llevaba once horas sin conducir para nosotros y lo despachamos.

> El sesenta por ciento de mi capacidad no me pertenece y esas personas no son mis trabajadores. Yo no les puedo dar una orden. Les puedo poner condiciones en el contrato, les puedo pagar más o menos, y les puedo dejar de dar viajes. Nada más.

> Entonces cuando alguien me diga «instalamos un dispositivo en toda la flota», le voy a preguntar quién le va a pedir permiso a ciento cuarenta y ocho dueños de camión, y qué les vamos a ofrecer a cambio. Si esa parte no está en la propuesta, la propuesta no sirve.

> Y lo del costo por kilómetro me pegó de otra manera. Cuatro años sirviendo un contrato a menos catorce por ciento sin saberlo. Yo llevo veintiún años en esta empresa. Eso no es un error de alguien: es que nunca juntamos el dato.

> Ricardo Mansilla Oyarzo —- Gerente de Operaciones

> Mi torre son veintidós personas en turnos, veinticuatro por siete, asignando viajes a trescientos setenta y cuatro camiones.

> Para asignar un viaje tengo que saber cuatro cosas al mismo tiempo: dónde está el camión, si el equipo sirve para esa carga, si el conductor tiene jornada, y si los papeles están al día. De esas cuatro, hoy sé una y media. La posición la veo en tres pantallas distintas porque hay tres proveedores de GPS, y hay treinta y cuatro camiones que no tienen ninguno: a esos los ubico llamando por teléfono.
<!-- ===== página 19 / 49 ===== -->

La jornada de un conductor propio la sé más o menos. La de un conductor de un tercero no la sé. Eso hay que decirlo con todas sus letras, porque es la pregunta que nos hizo la autoridad después del accidente. Y lo que más plata cuesta es lo que menos sistematizado tengo: qué hace el camión después de descargar. El veintiséis por ciento de los kilómetros los hacemos vacíos. Eso lo resolvemos a punta de teléfono y de memoria de la gente de la torre.

Lo que necesito es simple de decir: que cuando yo vaya a asignar un viaje, el sistema me diga que no puedo, y por qué. Prefiero que me bloquee a que me deje pasar.

Yasna Colipán Marín Conductora, 7 años, ruta norte

Yo hago Santiago—Antofagasta y a veces Calama. Son dos días largos y me conozco cada tramo.

La regla de las horas de conducción está bien y yo la respeto. El problema no es la regla: es dónde. Hay tramos donde a mí se me cumple el tiempo y no hay dónde parar. No hay banquina, no hay servicentro, no hay nada por sesenta kilómetros. Si me van a poner una alarma, que me avise antes, con tiempo para llegar a un lugar donde se pueda estar.

El registro de la jornada lo lleno yo, en una hoja. A veces lo lleno al final del día porque durante el día no se puede. Y sí, cuando lo lleno al final me acuerdo aproximado.

Manejando no puedo tocar nada. Eso lo tienen que entender: si me ponen algo que hay que apretar en ruta, o no lo aprieto, o lo aprieto mal, o lo aprieto en un momento en que no debería estar mirando.

Las esperas son lo peor del trabajo. Llego a un punto de carga a las siete y salgo a la una de la tarde. Seis horas sentada, y esas horas cuentan en mi jornada aunque no esté manejando. Anoto la hora en un papel y después alguien dice que no fue así.

Y en el norte hay tramos donde no hay señal por más de una hora. Si algo pasa ahí, estás sola. Por eso el botón sirve, cuando anda.

Nolberto Sandoval Pinto —- Transportista subcontratado. Dueño de dos camiones

Yo tengo dos camiones y trabajo con Curimón hace nueve años. También le hago viajes a otras dos empresas. Eso lo saben y nunca ha sido un problema.

Le voy a hablar claro porque para eso me invitaron. Mis camiones valen más de doscientos millones entre los dos y son míos. Los pago yo, los mantengo yo y los arriesgo yo. Curimón me paga por viaje.

Cuando me dicen que me van a instalar un aparato, yo pregunto tres cosas: quién lo paga, quién ve esa información, y qué pasa con ella cuando yo estoy trabajando para otro cliente. Porque si el aparato es de ellos y anda prendido siempre, ellos van a saber cuándo trabajo para la competencia. Eso no se lo voy a dar. Ahora, sobre el accidente: yo conozco al colega y a mí también me dio vueltas. Es verdad que hay gente que agarra un viaje encima de otro porque necesita la plata. Yo no lo hago, pero pasa. Y también es verdad que nadie tiene cómo saberlo.

Si me preguntan qué me haría cambiar de opinión: que yo controle qué se comparte y cuándo. Si el aparato registra mis horas y eso me sirve a mÍ para demostrar que estoy en regla, lo acepto. Si el aparato es para que ellos me vigilen, no.
<!-- ===== página 20 / 49 ===== -->

Y una cosa práctica que a mí me duele todos los meses: yo no veo mi liquidación hasta que llega. Nueve días después del cierre. Si falta un viaje, tengo que llamar y esperar. Si yo pudiera ver mis viajes en el momento, me ahorraría la mitad de los problemas del año.

Gabriela Ossandón Prieto Gerenta de Administración y Finanzas

Yo llegué en enero y lo primero que pedí fue el costo por kilómetro por ruta. Nadie lo tenía. Repartíamos los costos por ingreso, que es la manera más elegante de no saber nada.

Cuando lo armé, salieron tres contratos bajo costo, uno a menos catorce por ciento. Y no es que estuvieran perdiendo desde ayer: llevaban cuatro años. Las rutas buenas venían subsidiando a las malas y nadie podía verlo.

El problema de fondo es que los datos existen y están todos separados. El combustible me llega de la red de estaciones cuarenta días después. Los peajes vienen en ctra liquidación. Los neumáticos están en una planilla del taller. Las horas del conductor están en un papel que viaja en la cabina. Y el viaje está en el sistema de transporte. Cinco fuentes que nunca se juntan.

Del pago a terceros: es el treinta y ocho por ciento de mis costos y son ciento cuarenta y ocho liquidaciones al mes que arman ocho personas en nueve días. El once por ciento hay que corregirlo después. Eso es mucha gente haciendo mucho trabajo manual para llegar tarde y con errores.

Y quiero adelantar algo que va a aparecer: no conozco el costo de un camión subcontratado, sólo la tarifa que le pago. Así que cuando comparo flota propia con flota de terceros, estoy comparando cosas distintas. Eso también hay que resolverlo.

Última cosa. Voy a mirar la propuesta económica con lupa, y en particular el costo de operar esto durante los treinta y seis meses. Esta empresa gana nueve por ciento.

Hugo Trincado Bahamonde — - Jefe de Taller y Mantenimiento

Tengo dos talleres y cuarenta y seis personas para ciento cuarenta y ocho tractocamiones y doscientos diez semirremolques.

El plan preventivo es por kilometraje y el kilometraje lo leo del odómetro cuando el camión pasa por el taller. O sea, la fecha de la próxima mantención es una adivinanza informada.

Y aquí viene lo que me tiene molesto hace años: sesenta y un camiones traen telemetría de fábrica. Ese camión me puede decir el kilometraje, el consumo, los códigos de falla y hasta cómo lo están manejando. Desde que los compramos, nadie ha bajado ese dato. Está ahí y no lo usamos.

Cuando un camión se rompe en ruta lo arregla un taller externo. Llega la factura y se paga. Esa reparación no queda en la hoja de vida del equipo. Después yo miro el historial de un camión y tiene hoyos de años. De los camiones de terceros no sé nada y no me corresponde saber. Pero cuando uno de ellos se queda en pana con carga de un cliente mío, el problema es mío igual.

Y ojo con una cosa de la que nadie habla: yo sólo puedo tocar un camión cuando pasa por un terminal. Si me dicen que hay que instalar algo en trescientos setenta y cuatro camiones, eso no es un proyecto de un mes: es un proyecto de meses, y hay camiones que aparecen por acá dos veces al año.
<!-- ===== página 21 / 49 ===== -->

Denisse Aguayo Lillo —- Jefa de Prevención de Riesgos y Seguridad

Somos once personas y respondemos por la seguridad de cuatrocientos cincuenta y cuatro conductores, de los cuales sólo ciento noventa y seis son nuestros.

Después del accidente de febrero me tocó explicarle a la autoridad cómo controlamos la jornada. Mostré los registros de nuestros conductores, que están bien. Y después me preguntaron por los conductores de terceros y no tuve nada que mostrar.

Yo llevo tres años pidiendo que el tacógrafo se descargue. Los camiones nuevos lo traen. Nadie definió quién lo baja, cada cuánto ni dónde se guarda. Es información que la ley nos va a pedir y que hoy se pierde sola. Los vencimientos son mi otro dolor. Son como seis mil fechas vivas entre licencias, exámenes, cursos, revisiones técnicas, permisos y seguros. Están en cuatro planillas distintas que mantienen personas distintas. Lo de abril, el curso de carga peligrosa vencido tres semanas antes, era absolutamente predecible.

Y sobre la carga peligrosa: la lista de chequeo se llena en el terminal, en papel. El fiscalizador encontró que el papel no correspondía a lo que llevaba el camión. Ese papel lo llenó alguien apurado.

Lo que yo quiero es que el sistema no deje salir un camión que no puede salir. No una alerta, no un correo: que no deje. Sé que operaciones va a decir que eso frena viajes. Prefiero frenar un viaje.

Patricio Kast Fuentealba Jefe de Control de Flota

Somos seis personas mirando tres pantallas distintas. Cada proveedor de GPS dibuja el mapa a su manera, define los eventos a su manera y guarda el histórico a su manera.

El proveedor de nuestra flota propia lo contratamos nosotros. Los otros dos los contrataron los dueños de camión, cada uno por su cuenta, y a nosotros nos dan un acceso de visita. En uno de ellos ni siquiera podemos exportar.

Y hay treinta y cuatro camiones sin nada. Cuando la torre me pregunta dónde está uno de esos, la respuesta es que llamemos al conductor.

Los tramos sin cobertura son otra cosa que la gente de oficina subestima. En el norte hay más de ochenta kilómetros seguidos sin señal. Ahí el camión desaparece del mapa. Cuando reaparece, algunos equipos mandan lo que guardaron y otros no mandan nada: simplemente hay un hoyo.

El cliente grande quiere ver la posición de su carga en tiempo real. Yo entiendo la exigencia, pero eso significa resolver tres proveedores, treinta y cuatro camiones sin equipo, los hoyos de cobertura, y además convencer a ciento cuarenta y ocho dueños de camión de que su posición se comparta con un tercero. Lo último es lo más difícil y nadie lo ha planteado todavía.

Marcelo Riquelme Ibáñez —- Jefe de Tecnologías de Información

Somos nueve personas para cinco terminales, dos talleres y una flota que por definición no está en ninguna parte fija.

El sistema de gestión de transporte es del 2013 y hace bien una cosa: sabe qué viaje encargamos. No sabe qué viaje ocurrió. No sabe a qué hora llegó el camión, cuánto manejó el conductor, cuánto combustible gastó ni qué ruta tomó.
<!-- ===== página 22 / 49 ===== -->

Toda esa información existe. Está en tres plataformas de GPS, en una telemetría que nunca bajamos, en una liquidación de combustible que llega a los cuarenta días y en papeles que andan en la cabina. Nunca se junta, y ése es literalmente el proyecto.

Después está el documento electrónico de transporte, que hoy lo emitimos redigitando desde la orden de transporte al sistema contable. Eso es trabajo manual y es fuente de error, pero hay algo peor y prefiero decirlo: hay puntos de carga sin cobertura donde el documento no se puede emitir en el momento. Alguien tiene que resolver eso y no soy yo.

Y una advertencia sobre el despliegue: cualquier cosa que vaya arriba de un camión se instala cuando el camión pasa por un terminal. No hay otra. Con trescientos setenta y cuatro camiones y un promedio de seis días, y con un veintidós por ciento de la flota subcontratada que aparece menos de una vez al mes, eso define el cronograma. No lo define el proveedor: lo define la física.

Andrea Lecaros Vives - Gerenta de Logística de la exportadora que representa el 19 % de los ingresos

Trabajamos con Curimón hace catorce años y son buenos. Esta conversación no es una amenaza, es una exigencia con plazo, que no es lo mismo.

Pedimos cuatro cosas para 2029. La primera es el documento de transporte electrónico integrado de punta a punta, sin que nadie redigite nada. Hoy recibimos documentos con errores que se originan en una transcripción.

La segunda es posición de la carga en tiempo real, disponible para nosotros. Nuestros propios clientes nos la piden a nosotros. No es un capricho: es una condición que nos trasladan.

La tercera es emisiones por tonelada-kilómetro, verificadas por un tercero. Va en nuestro reporte y necesitamos que el dato sea auditable, no una estimación.

Y la cuarta es la que sé que les va a costar, y la pedimos justamente por lo que pasó en febrero: acreditación del cumplimiento de la jornada del conductor en cada viaje, incluidos los camiones subcontratados. Nosotros también respondemos por lo que pasa con nuestra carga en la ruta.

Les dijimos que entendemos que la cuarta es difícil. Lo que no vamos a aceptar es que nos digan que es imposible, porque el problema no es nuestro y el riesgo tampoco lo es sólo de ellos.

Sobre las contradicciones.

El PROPONENTE habrá advertido que estas entrevistas no son consistentes entre sí. Operaciones quiere asignar al camión más cercano y no sabe cuánta jornada le queda al conductor si es de un tercero. Prevención quiere que el sistema bloquee la salida y operaciones sabe que eso frena viajes. El cliente exige la posición de la carga en tiempo real y el dueño del camión responde que su posición es información suya, sobre todo cuando trabaja para otro. Finanzas quiere costo por kilómetro real y no conoce el costo de un camión que no es suyo. Taller quiere mantenimiento con telemetría y el 60 % de la flota no le pertenece. La conductora respeta la regla de las horas y explica que hay tramos donde no existe un lugar donde detenerse. Y el gerente general recuerda que a ciento cuarenta y ocho dueños de camión no se les puede dar una orden: hay que ofrecerles algo.

Estas tensiones son reales y no se resolverán antes de la adjudicación. Resolverlas —o, cuando no sea posible, proponer una arquitectura que permita convivir con ellas y dejar constancia de la decisión y de su costo— es parte de lo que se está licitando.
<!-- ===== página 23 / 49 ===== -->

### LO QUE EL MANDANTE ESPERA

### CAPÍTULO 9 EXPECTATIVAS DE NEGOCIO

Las siguientes son las expectativas del CLIENTE expresadas como resultados de negocio. Deliberadamente no están escritas como requerimientos. Traducirlas en requerimientos funcionales y no funcionales, priorizarlos, asignarlos a una etapa y hacerlos verificables es trabajo del PROPONENTE.

### 9.1 Que ningún camión salga si no puede salir

El CLIENTE espera que, en el momento de asignar un viaje, se verifique de forma bloqueante que el conductor dispone de jornada suficiente, que sus habilitaciones están vigentes, que el equipo tiene su documentación al día y que la combinación es apta para la carga que va a transportar.

Espera que esa verificación cubra también a los conductores y camiones de transportistas subcontratados, que son la mayoría, y que el sistema impida la asignación en lugar de limitarse a advertirla.

Esta es la primera expectativa y es la que originó la licitación.

### 9.2 Que la jornada del conductor sea un dato y no una declaración

El CLIENTE espera conocer y poder acreditar la jornada efectiva de conducción de cada persona que despacha, propia o de un tercero, con evidencia oponible ante la autoridad, ante el cliente y ante el seguro.

Espera hacerlo sabiendo que una parte de esa jornada ocurre fuera de la compañía y que no puede obtenerse por la vía laboral. Cómo conseguirla es precisamente la primera de las decisiones que este documento no resuelve.

### 9.3 Que las vigencias no dependan de que alguien se acuerde

El CLIENTE espera un registro único de las aproximadamente seis mil fechas de vencimiento de conductores y equipos, con aviso anticipado a quien corresponda y con efecto directo sobre la posibilidad de asignar un viaje.

### 9.4 Que se sepa qué viaje ocurrió, y no sólo cuál se encargó

El CLIENTE espera reconstruir cada viaje con la información real: horas de llegada y salida en los puntos de carga y descarga, ruta seguida, tiempo de conducción, combustible consumido, peajes, incidentes y conformidad de entrega.

Espera que esa reconstrucción sea automática y que no dependa de un papel que viaja en la cabina durante días.

### 9.5 Que el tiempo de espera se pueda cobrar

El CLIENTE espera que la hora de llegada y la de salida en las instalaciones de un cliente se registren sin intervención del conductor, con evidencia suficiente para sostener el cobro que hoy se objeta en un setenta y uno por ciento.
<!-- ===== página 24 / 49 ===== -->

### 9.6 Que el camión vuelva cargado

El CLIENTE espera reducir de forma medible el veintiséis por ciento de kilómetros recorridos en vacío, y espera que la decisión de qué hace un camión después de descargar deje de depender del teléfono y de la memoria de la torre.

### 9.7 Que se conozca el costo real de cada ruta y de cada contrato

El CLIENTE espera un costo por kilómetro y por viaje construido con datos reales —combustible, peajes, neumáticos, mantenimiento, jornada, pago a terceros— y no con un prorrateo, y espera poder decir si un contrato gana o pierde antes de renovarlo y no cuatro años después.

9.8 Que la liquidación a los transportistas sea automática y transparente

El CLIENTE espera liquidar a ciento cuarenta y ocho transportistas sin nueve días de trabajo manual y sin un once por ciento de correcciones, y espera que cada transportista pueda ver sus viajes y su liquidación en curso en cualquier momento.

### 9.9 Que el cliente vea su carga

El CLIENTE espera entregar a sus clientes la posición de la carga y el estado del viaje, con la información que corresponda a cada uno y respetando lo que los dueños de camión estén dispuestos a compartir.

### 9.10 Que el documento de transporte no se redigite

El CLIENTE espera que el documento electrónico de transporte se emita desde la misma información con que se planificó el viaje, sin transcripción intermedia, y espera una solución declarada para los puntos de carga sin cobertura móvil.

### 9.11 Que las emisiones se midan con método

El CLIENTE espera reportar emisiones por tonelada-kilómetro con una metodología declarada, con datos trazables hasta el consumo real de cada viaje y en condiciones de ser verificada por un tercero.

### CAPÍTULO 10 RESTRICCIONES NO NEGOCIABLES

Las siguientes condiciones no están en discusión. Una propuesta que no las respete será evaluada como falta de comprensión del caso.

| N° | Restricción |
| --- | --- |
| 1 | Ninguna solución puede exigir al conductor una interacción con un dispositivo mientras el vehículo está en movimiento. Toda captura durante la marcha debe ser automática. |
| 2 | El 60 % de la capacidad pertenece a 148 transportistas subcontratados y sus 258 conductores no son trabajadores de la compañía. Nada puede imponérseles por la vía laboral: lo que dependa de ellos debe conseguirse por contrato, por incentivo o por diseño, y su viabilidad debe estar argumentada en la propuesta. |
| 3 | Los dispositivos instalados en camiones de terceros pertenecen a sus dueños. No pueden intervenirse, reconfigurarse ni reemplazarse sin su acuerdo expreso. |
| 4 | La operación no puede depender de la cobertura móvil. Existen tramos de más de 80 km continuos sin señal y son parte permanente de la operación, no una excepción. |
| 5 | Todo equipamiento a bordo sólo puede instalarse, actualizarse o reemplazarse cuando el camión pasa por un terminal. Un camión pasa cada 6 días en promedio y el 22 % de la flota subcontratada pasa menos de una vez al mes. |
<!-- ===== página 25 / 49 ===== -->

| N° | Restricción |
| --- | --- |
| 6 | Ningún equipamiento a bordo puede afectar la garantía del vehículo ni interferir con sus sistemas de seguridad. |
| 7 | La compañía responde por la jornada del conductor que despacha, sea propio o de un tercero, y debe poder acreditarla ante la autoridad, ante el cliente y ante el seguro. |
| 8 | El sistema contable se mantiene y sigue siendo el único emisor de documentos tributarios, incluido el documento electrónico de transporte. |
| 9 | Los puntos de carga y descarga son instalaciones de terceros. La compañía no puede instalar equipamiento en ellas ni imponer procedimientos a sus operadores. |
| 10 | Un camión detenido no produce. Ninguna actividad del proyecto puede inmovilizar unidades más allá del tiempo que ya pasan en el terminal, salvo que su costo esté declarado y costeado en la propuesta económica. |
| 11 | La flota rueda 24x7x365, No existe una ventana de detención de la operación: la intervención es camión por camión y terminal por terminal. |
| 12 | El paso fronterizo Los Libertadores cierra por nieve entre junio y septiembre en episodios impredecibles que han llegado a 12 días continuos. El plan debe absorberlos. |
| 13 | El área de tecnologías de información son 9 personas. Toda función que requiera un especialista dedicado que la compañía no tiene debe ofrecerse como servicio y estar costeada. |
| 14 | La compañía opera con un margen operacional del 9 %. La propuesta económica será evaluada con especial atención al costo de operación de los 36 meses. |

### CAPÍTULO 11 EXCLUSIONES EXPLÍCITAS

Para evitar sorpresas, el CLIENTE declara expresamente qué NO está pidiendo:

- No se pide reemplazar el sistema contable ni la emisión de documentos tributarios.
- No se pide intervenir los sistemas del vehículo ni modificar su electrónica de fábrica.
- No se pide reemplazar las plataformas de posicionamiento satelital instaladas en camiones de terceros, aunque sí unificar la vista y especificar qué se requeriría si hubiera que homologarlas.
- No se pide gestión de remuneraciones ni administración de personal, aunque sí el registro de jornada con valor probatorio y la información que alimente el cálculo de la remuneración variable del conductor.
- Nose pide administrar la contabilidad de los transportistas subcontratados; sí liquidar lo que la compañía les debe y darles visibilidad de sus viajes.
- No se pide desarrollar un mercado de cargas ni intermediar carga de terceros, aunque sí resolver la asignación del retorno con la carga que la propia compañía gestiona.
- No se pide operar los talleres externos en ruta; sí incorporar su intervención a la hoja de vida del equipo.
- Nose pide sustituir los sistemas de la autoridad aduanera ni los de los clientes; sí integrarse a ellos donde exista interfaz disponible.
- No se pide instalar infraestructura en los puntos de carga y descarga de los clientes, que son instalaciones de terceros.
- El hardware — dispositivos a bordo, terminales de terminal y taller, lectores y equipamiento de red— lo adquiere el CLIENTE; el PROPONENTE debe especificar exactamente qué comprar, cuánto y con qué características, conforme al Capítulo 8 de las Bases Técnicas Transversales.
<!-- ===== página 26 / 49 ===== -->

> Que algo esté excluido del alcance no significa que pueda ignorarse en el diseño. La solución debe convivir con todo lo excluido, y las dependencias que ello genera deben estar identificadas, documentadas y consideradas en el plan y enel riesgo.

### CAPÍTULO 12 MARCO NORMATIVO Y COMPROMISOS CON TERCEROS

El PROPONENTE deberá identificar, investigar y considerar en su propuesta el marco que aplica a esta industria. El CLIENTE entrega la orientación inicial; la profundización es parte del trabajo.

| Ámbito | Referencia | Por qué importa aquí |
| --- | --- | --- |
| Jornada del conductor de carga | Régimen especial de jornada del personal que se desempeña como conductor de vehículos de carga terrestre interurbana: conducción continua máxima, descansos mínimos y tope de horas. | Es la obligación cuyo incumplimiento está detrás del accidente de febrero y cuya acreditación exige el cliente mayor para 2029. |
| Registro de la jornada | Obligación de llevar registro de las horas trabajadas y de conducción, y medios admitidos para hacerlo. | Hoy se lleva en papel firmado por el conductor y no existe para los 258 conductores de terceros. |
| Licencias de conducir profesionales | Requisitos, clases, exámenes y vigencia de las licencias necesarias para conducir vehículos de carga. | Forma parte de las = 6.000 fechas de vencimiento que hoy viven en planillas. |
| Transporte de sustancias peligrosas | Reglamento de transporte de cargas peligrosas por calles y caminos: documentación, señalización, equipamiento, capacitación específica del conductor y plan de emergencia. | Es el origen de la detención de abril, con documentación que no correspondía y curso vencido. |
| Pesos y dimensiones | Normativa sobre pesos máximos por eje y dimensiones de vehículos de carga, y fiscalización en plazas de pesaje. | 142 detenciones en 2025. El cliente carga y la compañía responde. |
| Documento electrónico de transporte | Normativa de la autoridad tributaria sobre emisión electrónica del documento que ampara el traslado de mercaderías. | Debe emitirse antes de que el vehículo se mueva, incluso en puntos de carga sin cobertura móvil. |
| Contrato de transporte terrestre | Régimen del contrato de transporte de carga, responsabilidad del porteador por pérdida, daño y retraso, y plazos de reclamo. | Define qué debe acreditar la compañía cuando un cliente reclama, y hoy esa prueba viaja en papel. |
| Subcontratación | Normativa sobre trabajo en régimen de subcontratación y responsabilidad de la empresa principal. | Involucra a 148 transportistas y 258 conductores que no son trabajadores de la compañía. |
| Seguridad y salud en el trabajo | Obligaciones de prevención de riesgos, investigación de accidentes y gestión de la fatiga en la conducción profesional. | Es el marco de la investigación abierta tras el accidente del 14 de febrero. |
| Revisión técnica y emisiones vehiculares | Régimen de revisión técnica, certificación de emisiones y permisos de circulación. | Aplica a 374 camiones y 210 semirremolques, propios y de terceros. |
| Tránsito y seguridad vial | Ley de tránsito y normativa sobre uso de dispositivos, velocidad y condiciones de conducción. | Fundamenta la restricción no negociable N° 1. |
| Cruce fronterizo y aduanas | Documentación de tránsito internacional, control aduanero y migratorio de dos países. | = 1.900 cruces al año por Los Libertadores. |
<!-- ===== página 27 / 49 ===== -->

| Ámbito | Referencia | Por qué importa aquí |
| --- | --- | --- |
| Protección de datos personales | Ley N° 21.719, con atención a los datos de conductores que no son trabajadores de la compañía y a la información de localización. | La posición de un camión de un tercero y las horas de un conductor externo son datos cuyo tratamiento requiere base y consentimiento. |
| Reporte de emisiones | Marcos de cuantificación y reporte de gases de efecto invernadero aplicables al transporte de carga y a la cadena logística de los clientes. | Es la tercera condición del cliente mayor para 2029 y exige metodología verificable. |

> Este listado es orientador, no exhaustivo. El PROPONENTE es responsable de identificar la normativa aplicable completa y de acreditar en su propuesta cómo la solución la satisface. En este caso, además, la propuesta debe distinguir con precisión qué obligaciones recaen sobre la compañía respecto de sus propios trabajadores y cuáles respecto de los conductores de transportistas subcontratados, porque no son las mismas y su tratamiento técnico tampoco puede serlo.

### CAPÍTULO 13 HORIZONTE, PRIORIDADES Y ETAPAS

### 13.1 Lo que el comité quiere primero

El comité expresó, sin transformarlo en instrucción técnica, un orden de urgencia: primero la seguridad — jornada, vigencias y bloqueo de la asignación—, porque de ahí salieron el accidente y la detención de abril; luego el viaje real, la posición y la evidencia de los tiempos; y por último el costo por kilómetro, la liquidación a terceros y las emisiones.

La gerenta de administración y finanzas dejó una objeción registrada que conviene tomar en serio: «tres contratos están perdiendo plata hoy y dos de ellos se renegocian el próximo año. Si el costo por kilómetro real queda para la Etapa 2, vamos a renegociar otra vez a ciegas».

El jefe de control de flota dejó otra: «no se puede prometer posición en tiempo real al cliente sin haber resuelto antes qué están dispuestos a compartir los dueños de camión. Esa conversación con ciento cuarenta y ocho personas toma meses y no la puede hacer un sistema».

Las dos objeciones apuntan a lo mismo desde ángulos distintos: hay decisiones de este proyecto cuyo plazo no lo fija la tecnología sino una negociación con terceros, y las negociaciones no se paralelizan.

Ese orden es una preferencia del mandante, no una definición de alcance. La distribución concreta entre la Etapa 1 y la Etapa 2 la propone el PROPONENTE y debe justificarla en función de las dependencias técnicas, del riesgo, de los hitos externos del numeral 13.2 y de la capacidad de absorción del CLIENTE, que en este caso incluye la disposición de ciento cuarenta y ocho transportistas que no dependen de él.

> Una propuesta que se limite a repetir el orden de preferencia del comité sin analizarlo será evaluada como falta de criterio profesional. Si el PROPONENTE considera que hay una dependencia técnica que obliga a alterar ese orden, debe decirlo y fundamentarlo. El CLIENTE contrata ingeniería, no obediencia.
<!-- ===== página 28 / 49 ===== -->

### 13.2 Hitos externos que condicionan el proyecto

Ninguno de los siguientes hitos lo controla la compañía, y tres de ellos ni siquiera tienen fecha. El plan debe incorporarlos como restricciones y no como riesgos a monitorear.

| Fecha | Hito externo | Consecuencia |
| --- | --- | --- |
| Diciembre a abril | Temporada de fruta. Máxima demanda de equipo refrigerado, esperas de más de 8 horas en puntos de carga y peak de actividad de toda la flota. | Ventana de congelamiento. La operación no admite intervenciones y los camiones pasan aún menos por los terminales. |
| Junio a septiembre | Cierres del paso Los Libertadores por nieve, en episodios impredecibles de hasta 12 días continuos. | Camiones detenidos en ruta, carga comprometida y conductores en jornada. El plan debe absorberlo y no puede planificarse. |
| Semana Santa y Fiestas Patrias | Restricciones de circulación de vehículos de carga decretadas por la autoridad y peaks de tránsito. | Congelamientos cortos con fecha conocida. |
| Cierre de cada mes | Liquidación a 148 transportistas y facturación a 84 clientes. | Nueve días de trabajo manual que no admiten interrupción. |
| Permanente | Un camión pasa por un terminal cada 6 días en promedio; el 22 % de la flota subcontratada pasa menos de una vez al mes. | Determina fisicamente el ritmo de cualquier despliegue a bordo. No lo define el proveedor. |
| 2029 | Condiciones de renovación del cliente que representa el 19 % de los ingresos: documento electrónico integrado, posición en tiempo real, emisiones verificadas y acreditación de jornada incluidos los camiones subcontratados. | La cuarta condición exige negociar con 148 transportistas y no se resuelve con tecnología sola. |
| 2027 | Renegociación de dos de los tres contratos que hoy se sirven bajo costo. | Si el costo real por ruta no está disponible antes, se renegocia sin información. |
| En curso | Investigación de la autoridad laboral tras el accidente del 14 de febrero y auditoría del principal cliente. | Puede imponer obligaciones adicionales durante la ejecución del proyecto. |
| 2030 — 2032 | Evaluación de incorporar un sexto terminal en el norte y de renovar 40 tractocamiones. | No es seguro. Si ocurre, el CLIENTE espera incorporarlos sin rehacer la solución. |

### 13.3 Estrategia de puesta en producción esperada

El CLIENTE no impone una estrategia de implantación, pero sí declara las condiciones que cualquier estrategia debe respetar:

1. Nada entra en producción sin haber convivido con la forma actual de trabajar durante la marcha blanca correspondiente, con conciliación entre ambas y con la posibilidad de volver atrás.

2. Ninguna actividad puede detener la flota ni inmovilizar unidades más allá del tiempo que ya pasan en el terminal, salvo que su costo esté declarado y costeado.

3. El despliegue de equipamiento a bordo se hace camión por camión, cuando cada uno pasa por un

terminal. El plan debe declarar la cobertura acumulada esperada mes a mes y qué se hace con el 22 % de la flota subcontratada que aparece con menos frecuencia.
<!-- ===== página 29 / 49 ===== -->

El paso a producción no puede ocurrir entre diciembre y abril, ni en las ventanas de restricción

vehicular, ni durante el cierre mensual de liquidaciones.

El despliegue debe poder hacerse por proceso — asignación y bloqueo, jornada, viaje y posición,

documentos, costos, liquidación, portal de clientes y portal de transportistas— y no como un único evento.

Toda función que dependa de los transportistas subcontratados debe desplegarse con un plan de

adhesión declarado: qué se les pide, qué se les ofrece, en qué plazo y qué ocurre con quien no adhiere. La verificación bloqueante de la asignación debe probarse en paralelo antes de bloquear efectivamente, midiendo cuántos viajes habría detenido y por qué motivo.

La capacitación debe considerar que los conductores no están en ningún lugar fijo, que 258 de ellos no son trabajadores de la compañía y que la torre opera en turnos 24x7.

La estabilización posterior a cada paso a producción debe tener dotación y duración declaradas, y

contemplar presencia en los terminales en horario de relevo, que es de madrugada.

10. El plan debe declarar qué ocurre con los camiones que quedan sin equipar al término de cada etapa y cómo opera la solución en modo mixto durante ese período, que será largo.

> El CUENTE despacha viajes que ocurren a mil kilómetros de distancia, ejecutados en su mayoría por camiones que no son suyos y por personas que no son sus trabajadoras. Un error durante la marcha blanca no se traduce en un dato mal registrado: se traduce en un camión que sale cuando no debía salir. La estrategia de puesta en producción, y el plan de adhesión de los ciento cuarenta y ocho transportistas subcontratados, pesan en la evaluación de este caso tanto como la arquitectura.
<!-- ===== página 30 / 49 ===== -->

### ANTECEDENTES PARA EL DIMENSIONAMIENTO

### CAPÍTULO 14 VOLUMETRÍA: LO QUE SE ENTREGA Y LO QUE SE DEBE ESTIMAR

El CLIENTE entrega los volúmenes que efectivamente conoce, porque son los que gobierna su operación. Los volúmenes propios del dimensionamiento de un sistema —concurrencia, transacciones por segundo, almacenamiento, telemetría, integraciones— no los conoce, y no tiene por qué conocerlos: derivarlos es trabajo de ingeniería del PROPONENTE.

> Las celdas marcadas como «a estimar» deben completarse en la propuesta con el valor estimado, el método de estimación y los supuestos empleados. Entregar la propuesta con esas celdas vacías, o con valores sin derivación, se evaluará como dimensionamiento no realizado.

### 14.1 Volumetría operacional entregada por el CLIENTE

| Dimensión | Valor actual | Proyección a 3 años |
| --- | --- | --- |
| Camiones gestionados | 374: 148 propios y 226 de terceros | = 430: 170 y 260 |
| Transportistas subcontratados | 148 | =175 |
| Conductores que operan bajo la programación | 454: 196 propios y 258 de terceros | = 520 |
| Semirremolques propios | 210 | 245 |
| Viajes al año | = 96.000 | = 118.000 |
| Kilómetros recorridos al año | = 41.000.000 | = 50.000.000 |
| Toneladas transportadas al año | = 2.400.000 | = 2.900.000 |
| Documentos electrónicos de transporte emitidos al año | = 128.000 | = 157.000 |
| Clientes activos | 84 | = 100 |
| Puntos distintos de carga y descarga | = 1.400 | = 1.700 |
| Cruces fronterizos al año | = 1.900 | =2.400 |
| Camiones con dispositivo de posicionamiento | 340 de 374, en 3 plataformas distintas | 430 de 430 |
| Tractocamiones con telemetría de fábrica disponible | 61 | =110 |
| Fechas de vencimiento vivas de conductores y equipos | = 6.000 | = 7.000 |
| Liquidaciones mensuales a transportistas | 148 | =175 |
| Órdenes de trabajo de taller al año | = 5.200 | = 6.100 |
| Posiciones de neumático gestionadas | = 8.200 | = 9.500 |
| Abastecimientos de combustible al año | = 74.000 | = 90.000 |
| Pasadas de peaje al año | = 620.000 | = 760.000 |
| Personal propio con acceso a sistemas | 336 | 390 |
<!-- ===== página 31 / 49 ===== -->

| Dimensión | Valor actual | Proyección a 3 años |
| --- | --- | --- |
| Conductores externos que deberían acceder a alguna función | 258 | = 300 |

### 14.2 Volumetría de sistema que el proponente debe estimar

| Dimensión | Valor |
| --- | --- |
| Frecuencia de muestreo justificada para posición, eventos de conducción y telemetría del motor | A estimar y declarar como supuesto |
| Eventos por segundo generados por la flota completa según esa frecuencia | A estimar y declarar como supuesto |
| Volumen que debe almacenar el dispositivo a bordo durante 72 horas sin cobertura | A estimar y declarar como supuesto |
| Tiempo de sincronización de un camión al recuperar cobertura tras 72 horas | A estimar y declarar como supuesto |
| Consumo mensual de datos móviles por camión y su costo agregado para la flota | A estimar y declarar como supuesto |
| Transacciones por segundo en el peak de asignación de la torre | A estimar y declarar como supuesto |
| Personas usuarias internas concurrentes, considerando turnos 24x7 | A estimar y declarar como supuesto |
| Personas usuarias externas concurrentes: clientes y transportistas subcontratados | A estimar y declarar como supuesto |
| Volumen anual de almacenamiento transaccional | A estimar y declarar como supuesto |
| Volumen anual de almacenamiento de series de posición y de telemetría, con su política de agregación | A estimar y declarar como supuesto |
| Volumen de almacenamiento de la evidencia de jornada por el plazo de retención exigido | A estimar y declarar como supuesto |
| Volumen total de datos históricos a migrar desde el sistema de gestión de transporte de 2013 | A estimar y declarar como supuesto |
| Número de integraciones y volumen por integración, distinguiendo plataformas de posicionamiento, telemetría de fabricantes, red de combustible, peajes, sistema contable, clientes y autoridad aduanera | A estimar y declarar como supuesto |
| Ancho de banda por terminal | A estimar y declarar como supuesto |
| Contactos mensuales a la mesa de ayuda, distinguiendo personal interno, conductores y transportistas | A estimar y declarar como supuesto |
| Dotación de la mesa de ayuda y del equipo de operación para cobertura 24x7x365 | A estimar y declarar como supuesto |
<!-- ===== página 32 / 49 ===== -->

> Preste atención a tres particularidades del perfil de carga de este caso. La primera es que la fuente principal de datos está en movimiento y desconectada buena parte del tiempo: el dimensionamiento no depende sólo de cuántos eventos se generan sino de cuántos se acumulan a bordo y de qué ocurre cuando trescientos camiones recuperan cobertura al mismo tiempo al salir de una zona de sombra. La segunda es que la frecuencia de muestreo es una decisión de diseño con consecuencia directa en el costo de datos móviles de la flota, que es un costo recurrente y no despreciable para una empresa con margen del 9 %. La tercera es que hay dos poblaciones de usuarios externos —84 clientes y 148 transportistas con 258 conductores— cuyos perfiles, derechos sobre los datos y capacidad tecnológica son completamente distintos.

### CAPÍTULO 15 PARÁMETROS DEL CASO PARA LOS REQUISITOS «SEGÚN CASO»

Las Bases Técnicas Transversales marcan un conjunto de requisitos como «Según caso»: son obligatorios, pero su valor concreto lo fija cada industria. Los valores para el Caso 10 son los siguientes. Cuando este capítulo endurece un umbral del documento transversal, prevalece el más exigente.

| Código | Materia | Valor para el Caso 10 |
| --- | --- | --- |
| RT-02.12 | Replicación a nuevas unidades | Exigible. La compañía evalúa un sexto terminal en el norte y la renovación de 40 tractocamiones entre 2030 y 2032. La solución debe admitir un terminal nuevo, camiones nuevos y transportistas nuevos por parametrización, y el alta de un transportista subcontratado con sus camiones y conductores debe poder completarse en el plazo en que hoy se firma un contrato. |
| RT-03.10 | Operación desconectada del componente on- premise | El dispositivo a bordo debe operar 72 horas continuas sin cobertura móvil, registrando posición, eventos de conducción y jornada, tiempos en puntos de carga y descarga, y documentos asociados al viaje, sin pérdida de ningún registro. Los terminales deben operar 12 horas sin enlace hacia el exterior. La emisión del documento electrónico de transporte en un punto de carga sin cobertura es una decisión pendiente del numeral 16.1 y debe resolverse, no omitirse. |
| RT-03.13 | Sincronización tras la reconexión | No debe superar 20 minutos por camión tras 72 horas sin cobertura, sin pérdida de ningún evento de jornada ni de ningún registro de tiempo en instalaciones de cliente, y con un diseño que soporte la reconexión simultánea de varios cientos de unidades al salir de una zona de sombra. |
| RT-03.24 | Red de los sitios operacionales | Exigible el respaldo de enlace en los cuatro terminales regionales, tres de los cuales hoy no lo tienen. Y, con carácter propio de este caso, se exige caracterizar la cobertura móvil real de las rutas que la compañía opera mediante mediciones en terreno, y no suponerla: la disponibilidad declarada por los operadores no es un antecedente aceptable para el diseño. |
| RT-05.10 | Retención de datos históricos y de auditoría | Registro de jornada de conducción y su evidencia: mínimo 5 años, conforme a la normativa laboral aplicable. Documento electrónico de transporte y antecedentes del viaje: 6 años. Antecedentes de siniestros: 10 años. Habilitaciones de conductores y equipos: su vigencia y 5 años más. Registros de carga peligrosa: 5 años. Evidencia de tiempos de llegada y salida en instalaciones de cliente: 3 años. Liquidaciones a transportistas: 6 años. Series de posición y telemetría: 2 años en línea, con política de agregación declarada para el resto. |
| RT-05.15 | Datos históricos a migrar | Maestros de flota, semirremolques, conductores, transportistas y clientes: la totalidad. Viajes: 5 años. Liquidaciones a transportistas: 6 años. Siniestros: la totalidad. Las = 6.000 vigencias, con verificación documental de cada una durante la migración, por tratarse de datos hoy dispersos en cuatro planillas mantenidas por personas distintas. |
<!-- ===== página 33 / 49 ===== -->

| Código | Materia | Valor para el Caso 10 |
| --- | --- | --- |
| RT-05.23 | Estándares sectoriales de intercambio | Formato del documento electrónico de transporte definido por la autoridad tributaria. Estándares de telemetría vehicular y de intercambio con las plataformas de posicionamiento. Estándares de descarga y conservación de datos de tacógrafo digital. Estándares de intercambio logístico con clientes para aviso de despacho, estado del viaje y conformidad de entrega. Formatos de la autoridad aduanera para el tránsito internacional. El PROPONENTE deberá identificar cada uno por su denominación y verificar con cada proveedor y fabricante qué es efectivamente accesible. |
| RT-05.29 | Latencia de la capa analítica | Posición de un camión con cobertura: no superior a 2 minutos. Jornada acumulada de un conductor: en tiempo real, con el dato disponible en el momento de asignar. Tiempos de llegada y salida en un punto de cliente: registrados en el momento del evento. Costo consolidado de un viaje: no superior a 24 horas tras su cierre, con los componentes que a esa fecha estén disponibles y con indicación explícita de los que aún no lo están. Emisiones: consolidación mensual. |
| RT-06.01 | Tipología del emplazamiento on- premise | Sala de equipos de San Bernardo, de 26 m? habilitada en 2013, que debe remediarse o reemplazarse por no cumplir el Capítulo 6 del documento transversal. Gabinete en cada terminal regional dimensionado para RT-03.10. Y, con carácter propio de este caso, el dispositivo a bordo debe tratarse como un componente on-premise distribuido en 374 unidades, con su propio ciclo de vida, su mecanismo de actualización remota, su gestión de seguridad y su plan de reposición, todo ello sujeto ala restricción de que sólo puede intervenirse físicamente cuando el camión pasa por un terminal. |
| RT-09.01 | Transacción operacional crítica | Asignación de un viaje con verificación bloqueante de jornada, habilitaciones y aptitud del equipo: no superior a 30 segundos. Emisión del documento electrónico de transporte: no superior a 90 segundos. Registro de llegada y de salida en un punto de carga o descarga: automático, sin intervención del conductor y sin equipamiento instalado en las instalaciones del cliente. Transmisión de un evento de botón de emergencia a la torre: no superior a 15 segundos con cobertura. Publicación de la posición al cliente: no superior a 2 minutos. Alerta de jornada próxima a agotarse: con la anticipación que el PROPONENTE justifique en función de la distancia al lugar seguro de detención más cercano, criterio que debe declararse y fundamentarse. |
| RT-09.02 | Concurrencia y volumen de transacciones | El PROPONENTE lo deriva de la volumetría del numeral 14.1, considerando la reconexión simultánea de unidades al salir de zonas de sombra, y lo declara conforme al numeral 14.2. |
| RT-10.05 | Ventana operacional protegida | La flota rueda 24x7x365 y no existe ventana de detención: la intervención es camión por camión y terminal por terminal. Congelamiento de diciembre a abril por temporada de fruta. Congelamiento en las ventanas de restricción vehicular de Semana Santa y Fiestas Patrias. Congelamiento durante los nueve días del cierre mensual de liquidaciones. Los cierres del paso fronterizo por nieve, de hasta 12 días continuos, deben absorberse sin desplazar hitos. |
| RT-11.10 | Cifrado a nivel de campo | Exigible para los datos personales de los 258 conductores que no son trabajadores de la compañía, para toda información de localización asociada a una persona identificable, para los antecedentes de jornada y para las tarifas y condiciones pactadas con cada uno de los 148 transportistas subcontratados. |
| RT-12.11 | Autenticación en el perfil operacional | Torre en turnos 24x7. Conductores sin dispositivo asignado propio en una parte relevante de los casos y con camiones que rotan entre conductores. 258 conductores que no son trabajadores de la compañía y que en muchos casos trabajan también para otros. La identificación del conductor al inicio de un viaje debe resolverse sin exigir manipulación de un dispositivo con el vehículo en movimiento y sin depender de que el conductor recuerde una credencial. |
<!-- ===== página 34 / 49 ===== -->

| Código | Materia | Valor para el Caso 10 |
| --- | --- | --- |
| RT-12.12 | Personas usuarias externas | Los 84 clientes; los 148 transportistas subcontratados y sus 258 conductores; los talleres externos que intervienen equipos en ruta; la red de estaciones de servicio; y las autoridades laboral, de transporte y aduanera en lo que la normativa disponga. |
| RT-13.08 | Interfaces de terreno y de atención | Cabina en movimiento, con vibración, temperatura extrema y luz solar directa, donde ninguna interacción es admisible durante la marcha. Terminal en horario de relevo, que es de madrugada. Taller con guantes y manos sucias. Punto de carga de un cliente donde el conductor es visita y no controla nada. Ruta sin cobertura durante horas. Toda interfaz destinada al conductor debe ser operable con una sola mano, con guantes, y debe validarse con conductores reales antes de su despliegue. |
| RT-13.12 | Idioma y diseño de las interfaces del conductor | Español obligatorio. La documentación y las interfaces asociadas al cruce fronterizo deben considerar el intercambio con la autoridad del país vecino. Y, con carácter obligatorio y por sobre lo que exige el documento transversal, las interfaces destinadas al conductor deben acreditar criterios verificables de carga cognitiva mínima, validados con conductores en condiciones reales de operación. |
| RT-15.02 | Certificaciones sectoriales del adjudicatario | Conocimiento acreditado del régimen especial de jornada del conductor de carga y del reglamento de transporte de sustancias peligrosas. Experiencia comprobable en telemática de flotas y en soluciones con operación desconectada prolongada. |
| RT-16.09 | Registro de consultas a información sensible | Exigible sobre el acceso a la localización de camiones de terceros, a los antecedentes de jornada de conductores externos y a las tarifas y condiciones pactadas con cada transportista. Debe registrarse además todo acceso de un cliente a información de posición, indicando qué se le mostró y bajo qué autorización del dueño del camión. |
| RT-16.14 | Firma electrónica | Exigible en la conformidad de entrega del destinatario, en el registro de jornada del conductor, enla lista de verificación de carga peligrosa previa a la salida y en la aceptación de la liquidación mensual por parte del transportista subcontratado, en la modalidad que la normativa admita para cada caso. |
| RT-16.21 | Canales de notificación | Alerta de jornada próxima a agotarse, al conductor y a la torre, con la anticipación fundamentada de RT-09.01. Alerta de vencimiento de habilitaciones con escalonamiento a 60, 30 y 7 días, al titular y a quien deba actuar. Alerta de desvío de ruta y evento de botón de emergencia a la torre, con confirmación de recepción por una persona identificada. Aviso al cliente ante eventos relevantes del viaje. Aviso al transportista subcontratado ante cada viaje liquidado. |
| RT-16.30 | Portal público | Sin autenticación: seguimiento del estado de un envío mediante su número de documento. Autenticado, portal del cliente: posición de la carga, estado del viaje, documentos, conformidades, tiempos en sus instalaciones y emisiones asociadas. Autenticado, portal del transportista subcontratado: sus viajes, su liquidación en curso y su detalle, sus vencimientos, su evaluación y —con carácter obligatorio— el control de qué datos de sus camiones y conductores autoriza compartir y con quién, con posibilidad de revocación. |
| RT-17.01 | Aplicación móvil | Exigible en cuatro perfiles: conductor, operable con una sola mano y con guantes, sin ninguna interacción exigible en marcha y con operación desconectada de 72 horas; torre de programación; terminal y taller; y transportista subcontratado, con la gestión de sus viajes, su liquidación y sus autorizaciones de datos. |
<!-- ===== página 35 / 49 ===== -->

| Código | Materia | Valor para el Caso 10 |
| --- | --- | --- |
| RT-17.06 | Periféricos a integrar | Dispositivos a bordo en 374 camiones; las tres plataformas de posicionamiento satelital existentes; la telemetría de fábrica de 61 tractocamiones, como integración de solo lectura sujeta a la autorización de cada fabricante; los tacógrafos digitales instalados; lectores y terminales de los cinco terminales y los dos talleres; y el dispositivo de peaje. |
| RT-21.06 | Horario del centro de atención | 24x7x365 sin excepción. La flota rueda a toda hora y todo incidente que impida asignar un viaje, emitir un documento de transporte o recibir un evento de emergencia se clasifica en la severidad máxima. |
| RT-21.16 | Traslado a sitios alejados | Exigible. Cinco terminales entre Antofagasta y Puerto Montt, con más de 2.500 km entre los extremos. Debe considerarse además que una parte de la intervención ocurre sobre camiones que están en ruta y cuya llegada a un terminal no es programable con precisión. |
| RT-22.04 | Restricción de la capacitación | Los conductores no están en ningún lugar fijo y pasan por un terminal cada 6 días en promedio. 258 de ellos no son trabajadores de la compañía y su capacitación no puede imponerse por la vía laboral. La torre opera en turnos 24x7. El congelamiento de diciembre a abril coincide con el período de mayor actividad y menor disponibilidad de las personas. |

### CAPÍTULO 16 LO QUE ESTE DOCUMENTO DELIBERADAMENTE NO RESUELVE

Las decisiones que siguen son necesarias para que la solución sea coherente. El CLIENTE no las ha tomado, y no las va a tomar por el PROPONENTE. Resolverlas, dejarlas escritas como supuesto y hacerse cargo de sus consecuencias en la arquitectura, en el alcance y en el costo forma parte del trabajo profesional que se licita.

### 16.1 Decisiones de diseño pendientes

| N° | Decisión no tomada | Por qué importa |
| --- | --- | --- |
| 1 | Cómo se obtiene y se acredita la jornada de conducción de un conductor que no es trabajador de la compañía y que puede haber conducido antes para otro cliente. | Es la decisión más importante del caso. Es la causa del accidente del 14 de febrero y la cuarta condición del cliente mayor para 2029, y el dato está fuera del alcance de la empresa. |
| 2 | Qué se les ofrece a los 148 transportistas subcontratados a cambio de compartir sus datos, y qué ocurre con quien no adhiere. | Sin un plan de adhesión viable, toda la arquitectura que dependa de ellos es un dibujo. El gerente general lo advirtió expresamente. |
| 3 | Qué se hace con el sistema de gestión de transporte de 2013: se reemplaza, se conserva y se integra, o se envuelve mientras se sustituye por partes. | Sabe qué viaje se encargó y no sabe qué viaje ocurrió. Por él pasa toda la operación y toda la liquidación. |
| 4 | Cómo se unifica la posición de la flota con tres proveedores distintos, accesos de solo consulta en dos de ellos y 34 camiones sin dispositivo alguno. | Es la base de la posición en tiempo real que exige el cliente, y una de las tres plataformas ni siquiera permite exportar. |
| 5 | De quién es el dispositivo a bordo en un camión de un tercero, quién lo paga, quién lo administra y qué ocurre con él si el transportista deja de trabajar con la compañía. | Define el modelo económico y contractual de todo el despliegue, y es la primera pregunta que hacen los dueños de camión. |
| 6 | Qué ocurre cuando la verificación bloqueante impide un viaje ya comprometido con un cliente, quién puede autorizar una excepción y con qué registro. | Prevención quiere que el sistema no deje salir; operaciones sabe que eso detiene viajes. Sin regla de excepción, la primera vez que ocurra alguien la saltará por fuera. |
<!-- ===== página 36 / 49 ===== -->

| N° | Decisión no tomada | Por qué importa |
| --- | --- | --- |
| 7 | Con cuánta anticipación se alerta el agotamiento de la jornada, considerando que hay tramos donde no existe un lugar seguro donde detenerse. | La conductora entrevistada lo planteó con claridad: la alerta que llega tarde no sirve, y la que llega en un tramo sin dónde parar tampoco. |
| 8 | Cómo se registran la llegada y la salida en un punto de carga que es instalación de un tercero, sin intervención del conductor y sin instalar equipamiento allí. | Es el 71 % de los cobros por espera que hoy se objetan, y las dos soluciones evidentes están excluidas por la restricción no negociable N° 9. |
| 9 | Cómo se emite el documento electrónico de transporte en un punto de carga sin cobertura móvil, cumpliendo la exigencia de que exista antes de que el vehículo se mueva. | Ocurre hoy y la compañía reconoce que la práctica actual no resiste un examen. |
| 10 | Cómo se obtiene la conformidad de entrega del destinatario y en qué momento queda disponible para facturar y para defenderse de un reclamo. | Hoy viaja en papel en la cabina durante días y el 4,2 % nunca llega en condiciones. |
| 11 | Qué frecuencia de muestreo se adopta para posición y telemetría, qué se transmite en cobertura y qué se guarda a bordo para después. | Determina el costo mensual de datos móviles de toda la flota, que es recurrente en una empresa con 9 % de margen. |
| 12 | Qué se hace con la telemetría de fábrica de los 61 tractocamiones que hoy no se descarga. | El dato existe, es gratuito y permitiría mantenimiento por condición, consumo real y hábitos de conducción. Su acceso depende de cada fabricante. |
| 13 | Quién descarga la información del tacógrafo digital, con qué frecuencia, dónde se conserva y con qué garantía de integridad. | Es información que la autoridad puede exigir y que hoy se pierde sola. |
| 14 | Cómo y con qué criterio se asigna el retorno de un camión que va a quedar vacío. | El 26 % de los kilómetros son en vacío y hoy se resuelve por teléfono y por memoria de la torre. |
| 15 | Cómo se construye el costo de un viaje con componentes que llegan con desfases muy distintos: combustible a 40 días, peajes mensuales, neumáticos por planilla y jornada en papel. | Determina si el costo por viaje es un dato operacional o un cierre contable tardío. |
| 16 | Cómo se estima el costo real de un camión subcontratado si la compañía sólo conoce la tarifa que le paga. | Sin eso, comparar flota propia con flota de terceros es comparar cosas distintas, y esa comparación gobierna la decisión de crecer con una u otra. |
| 17 | Qué se hace con los tres contratos que hoy se sirven bajo costo y qué información debe estar disponible antes de la renegociación de 2027. | Son el 31 % del ingreso y dos de ellos se renegocian el próximo año. |
| 18 | Cómo se controlan las = 6.000 vigencias y quién es el responsable de cada una cuando el titular del documento es un tercero. | La compañía responde por el viaje que despacha, pero no puede renovar la licencia de alguien que no es su trabajador. |
| 19 | Cómo se verifica que la documentación de carga peligrosa corresponde efectivamente a lo que se cargó, y no alo que se planificó cargar. | Es exactamente el hallazgo de la fiscalización de abril. |
| 20 | Qué hace la solución cuando el paso fronterizo cierra doce días con camiones detenidos, carga comprometida y conductores en jornada. | Ocurre todos los inviernos y hoy se administra por teléfono. |
| 21 | Cómo se incorpora a la hoja de vida del equipo la intervención de un taller externo en ruta. | Hoy no se incorpora, y por eso el historial de mantenimiento de cada camión tiene hoyos de años. |
<!-- ===== página 37 / 49 ===== -->

| N° | Decisión no tomada | Por qué importa |
| --- | --- | --- |
| 22 | Cómo se calculan las emisiones por tonelada- kilómetro y con qué dato de consumo se hace para los camiones de terceros, cuyo combustible la compañía no compra. | Es la tercera condición del cliente para 2029 y exige verificación por un tercero. |
| 23 | Qué información del viaje y de la posición se comparte con el cliente, y cómo se concilia con lo que cada dueño de camión autoriza compartir. | El cliente exige tiempo real y el dueño de camión considera su posición información propia, sobre todo cuando trabaja para otros. |
| 24 | Cómo se protege la evidencia de jornada frente a la posibilidad de que se alegue manipulación, por parte de la compañía o del conductor. | Un registro que puede editarse no sirve como prueba ante la autoridad, ante el seguro ni ante el cliente. |
| 25 | Cómo se despliega el equipamiento a bordo en 374 camiones que pasan por un terminal cada 6 días, y qué se hace con el 22 % de la flota subcontratada que aparece menos de una vez al mes. | Define el cronograma real del proyecto. No lo define el proveedor: lo define la física de la operación. |
| 26 | Cómo opera la solución durante el largo período en que una parte de la flota estará equipada y otra no. | Ese período no es una transición breve: puede durar la mayor parte de una etapa, y durante él conviven dos formas de trabajar. |

Esta lista no es exhaustiva. Encontrar los demás vacíos es parte del ejercicio, y el PROPONENTE que identifique vacíos no listados aquí será evaluado favorablemente por ello.

### 16.2 Materias que el proponente deberá investigar

El CLIENTE no espera que el PROPONENTE conozca el transporte de carga por carretera. Sí espera que lo estudie. Las siguientes materias no se explican en este documento:

- Régimen especial de jornada del conductor de carga terrestre interurbana en Chile: conducción continua, descansos y tope de horas.
- Registro de la jornada: medios admitidos, valor probatorio, y estándares de tacógrafo digital y de descarga y conservación de sus datos.
- Telemática de flotas: arquitecturas, protocolos, estándares de telemetría vehicular y almacenamiento a bordo.
- Telemetría de fábrica de los fabricantes de camiones: qué exponen, en qué condiciones y con qué autorización.
- Diseño para operación prolongada sin conectividad: almacenamiento local, sincronización diferida, resolución de conflictos y reconexión masiva.
- Gestión de la fatiga en la conducción profesional: modelos, indicadores y prácticas de la industria.

### Reglamento de transporte de cargas peligrosas: documentación, señalización, equipamiento,

capacitación del conductor y plan de emergencia.

- Normativa de pesos y dimensiones por eje, y distribución de responsabilidad por sobrepeso entre quien carga y quien transporta.
- Documento electrónico de transporte: contenido, oportunidad de emisión y mecanismos de contingencia sin conectividad.
- Contrato de transporte terrestre de carga: responsabilidad del porteador por pérdida, daño y retraso, prueba de la entrega y plazos de reclamo.
- Régimen de subcontratación y responsabilidad de la empresa principal respecto de trabajadores de terceros.
<!-- ===== página 38 / 49 ===== -->

Modelos de relación con transportistas subcontratados: esquemas contractuales, incentivos, evaluación y programas de adhesión tecnológica.

Costeo en transporte de carga: costo por kilómetro y por viaje, costos fijos y variables, y punto de

equilibrio de una unidad.

Asignación de flota y de carga de retorno: modelos de optimización y reducción de kilómetros en vacío. Gestión de neumáticos y mantenimiento preventivo y por condición en flotas de carga.

Cuantificación y reporte de emisiones en transporte de carga: métodos por tonelada-kilómetro y

esquemas de verificación por tercero.

Seguridad de la carga en ruta: gestión de riesgo por ruta y horario, y protocolos de emergencia.

Protección de datos personales aplicada a información de localización y a personas que no son

trabajadores de quien trata el dato.

Tránsito internacional de carga por pasos fronterizos y documentación aduanera aplicable.

> Una propuesta que ofrezca «control de flota» sin haber entendido que el sesenta por ciento de esa flota no le pertenece al mandante, o que prometa acreditación de jornada sin explicar qué se le va a ofrecer a ciento cuarenta y ocho dueños de camión para que la entreguen, quedará en evidencia frente a la Comisión de Expertos.
<!-- ===== página 39 / 49 ===== -->

### LO QUE DEBE PRODUCIR EL PROPONENTE

### CAPÍTULO 17 EL TRABAJO DE TRADUCCIÓN EXIGIDO

Este documento describe una operación y sus problemas. No contiene un catálogo de requerimientos. Construirlo es la primera tarea del PROPONENTE y la que condiciona todas las demás.

### 17.1 De la necesidad al requerimiento

El PROPONENTE deberá recorrer este documento y producir un catálogo de requerimientos trazable a su origen. Cada requerimiento debe indicar de qué párrafo, entrevista, indicador o restricción proviene, de modo que el CLIENTE pueda verificar que nada quedó fuera y que nada se inventó.

| Producto | Contenido esperado |
| --- | --- |
| Catálogo de requerimientos funcionales | Qué debe hacer la solución, expresado en términos verificables, con identificador, descripción, actor, precondición, resultado esperado, prioridad y origen en este documento. |
| Catálogo de requerimientos no funcionales | Desempeño, disponibilidad, seguridad, usabilidad, operabilidad, mantenibilidad, portabilidad y cumplimiento, con umbral numérico y método de verificación. Deben incorporar los parámetros del Capítulo 15 y distinguir lo exigible a la compañía de lo exigible a terceros. |
| Registro de supuestos | Toda decisión que el PROPONENTE tomó por el CLIENTE, con su fundamento, su impacto si resulta equivocada y la instancia en que se validará. Incluye obligatoriamente las veintiséis decisiones del numeral 16.1, y en particular la primera, la segunda y la vigesimoquinta. |
| Plan de adhesión de los transportistas subcontratados | Documento propio de este caso: qué se les pide alos 148 transportistas, qué se les ofrece a cambio, en qué plazo, con qué instrumento contractual, cómo se mide la adhesión y qué ocurre con quien no adhiere. Sin este producto, toda función que dependa de ellos carece de sustento. |
| Registro de reglas de negocio | Las reglas propias del transporte que la solución debe respetar y que este documento no explicita: cómputo de la jornada, criterio de aptitud del equipo para una carga, prelación en la asignación, regla de excepción al bloqueo, cálculo del tiempo libre de espera y base de la liquidación a terceros, entre otras. |
| Matriz de trazabilidad | Correspondencia entre orígen, requerimiento, componente de la arquitectura, paquete de la EDT, prueba de verificación y criterio de aceptación. |
| Registro de vacíos y consultas | Aquello que el PROPONENTE no puede resolver por sí solo y que someterá al CLIENTE durante el período de consultas. |

> Un requerimiento no es una frase copiada de este documento. «Debe controlarse la jornada del conductor» no es un requerimiento: es un resultado esperado. El requerimiento indica de qué fuente se obtiene el tiempo de conducción, cómo se distingue conducir de esperar, qué ocurre con las horas que esa persona trabajó para otro, cómo se acredita el dato ante un tercero que puede impugnarlo, quién puede corregirlo y con qué registro, cuánto tiempo se conserva y cómo se demuestra que no fue alterado.
<!-- ===== página 40 / 49 ===== -->

### 17.2 Distinguir lo funcional de lo no funcional

Buena parte de lo que este documento describe puede leerse de las dos maneras, y la clasificación no es indiferente: determina quién lo verifica, cómo se prueba y en qué momento del proyecto se comprueba. Se ofrecen deliberadamente sin resolver algunos casos limítrofes:

- «El dispositivo debe operar setenta y dos horas sin cobertura»: ¿es disponibilidad, es una decisión de arquitectura, o es un conjunto de requerimientos funcionales sobre qué puede hacerse y qué no en modo desconectado?
- «La asignación debe verificar la jornada de forma bloqueante»: ¿es un control de seguridad, un requerimiento funcional de la asignación, o cumplimiento normativo con evidencia conservada?
- «El conductor no puede interactuar en marcha»: ¿es usabilidad, es seguridad de las personas, o es una restricción de diseño que condiciona cada pantalla y cada captura de dato?
- «La evidencia de jornada debe resistir una alegación de manipulación»: ¿es integridad de datos, es trazabilidad, o es un requerimiento funcional sobre quién puede editar qué y con qué registro?
- «La alerta debe llegar con tiempo para detenerse en un lugar seguro»: ¿es desempeño, es un requerimiento funcional que exige conocer dónde están esos lugares, o es una regla de negocio que alguien debe definir?
- «El transportista debe poder ver su liquidación en curso»: ¿es una funcionalidad del portal, un requerimiento de transparencia contractual, o parte del plan de adhesión sin el cual nada de lo demás ocurre?

Se evaluará el criterio con que el PROPONENTE resuelve estos casos y la consistencia con que aplica su propio criterio a lo largo de la propuesta, no la coincidencia con una respuesta preestablecida.

### 17.3 Definir el alcance y su reparto entre etapas

A partir del catálogo, el PROPONENTE deberá delimitar el alcance de la Etapa 1 y de la Etapa 2, declarar las exclusiones y justificar el reparto en función de las dependencias técnicas, del riesgo, de los hitos externos del numeral 13.2 y de la capacidad de absorción del CLIENTE.

La justificación debe hacerse cargo explícitamente de la preferencia del comité del numeral 13.1 y de las dos objeciones registradas allí mismo: que dos de los tres contratos bajo costo se renegocian en 2027 y sin costo real por ruta se renegociarán a ciegas, y que la posición en tiempo real para el cliente no puede prometerse antes de resolver qué están dispuestos a compartir los dueños de camión, conversación que toma meses y que no la hace un sistema.

### 17.4 Diseñar la arquitectura

La arquitectura lógica y física debe ser propia de este caso y reconocible como tal. Debe hacerse cargo, como mínimo, de los siguientes asuntos, todos ellos derivados de lo descrito en este documento:

1. De qué fuente se obtiene el tiempo de conducción de cada persona, incluidas las que no son

trabajadores de la compañía, y cómo se convierte en evidencia oponible.

2. Cómo se construye la verificación bloqueante de la asignación: qué se comprueba, contra qué fuentes, en treinta segundos y con qué comportamiento cuando una fuente no está disponible.

3. Cómo opera el dispositivo a bordo durante setenta y dos horas sin cobertura y cómo se comporta el

sistema cuando cientos de unidades recuperan señal a la vez.

4. Cómo se unifica la posición con tres plataformas de proveedores distintos, dos de ellas con acceso de solo consulta, y treinta y cuatro camiones sin dispositivo.
<!-- ===== página 41 / 49 ===== -->

5. Cómo se registran la llegada y la salida en instalaciones de terceros sin intervención del conductor y sin

instalar equipamiento allí.

6. Cómo se emite el documento electrónico de transporte en un punto de carga sin cobertura, cumpliendo

la exigencia de que exista antes del movimiento del vehículo.

7. Cómo se obtiene y se transmite la conformidad de entrega del destinatario en el momento en que

ocurre.

8. Qué frecuencia de muestreo se adopta, qué se transmite y qué se acumula a bordo, y cuál es el costo

mensual de datos móviles resultante para toda la flota.

9. Cómo se accede a la telemetría de fábrica de sesenta y un tractocamiones y a los tacógrafos digitales,

sin intervenir el vehículo.

10. Cómo se protege la integridad de la evidencia de jornada frente a una alegación de manipulación por

cualquiera de las partes.

11. Cómo se gestiona el consentimiento de cada dueño de camión sobre qué datos se comparten, con

quién y hasta cuándo, con posibilidad de revocación.

12. Cómo se construye el costo por viaje con componentes que llegan con desfases de hasta cuarenta días,

y qué se muestra mientras faltan.

13. Cómo se administra el ciclo de vida del dispositivo a bordo —actualización remota, seguridad,

reposición — en 374 unidades que sólo se tocan en un terminal.

14. Qué crecimiento admite el diseño ante un sexto terminal y una flota de 430 camiones, y qué

componente se satura primero.

### 17.5 Planificar de forma realista

El plan de trabajo debe ser específico de esta compañía. Un cronograma que podría servir para cualquier proyecto será evaluado como deficiente. En particular deberá reflejar:

- El cronograma contractual obligatorio de 56 meses del Artículo 17° de las Bases Administrativas, sin proponer plazos alternativos.
- El ritmo físico del despliegue a bordo: 374 camiones que pasan por un terminal cada 6 días en promedio, con un 22 % de la flota subcontratada que aparece menos de una vez al mes. El plan debe declarar la cobertura acumulada esperada mes a mes.
- El plan de adhesión de 148 transportistas subcontratados como una actividad con duración, responsable y riesgo propios, y no como un supuesto.
- El congelamiento de diciembre a abril, las ventanas de restricción vehicular y los nueve días del cierre mensual de liquidaciones.
- Los cierres imprevistos del paso fronterizo por nieve, de hasta 12 días continuos. El plan debe declarar cuánta holgura reserva y sobre qué base.
- La caracterización en terreno de la cobertura móvil de las rutas, que es una actividad de levantamiento con costo y plazo, no un supuesto de diseño.
- La verificación de factibilidad con tres proveedores de posicionamiento y con los fabricantes de camiones, que no depende del ADJUDICATARIO.
- La migración y verificación documental de las = 6.000 vigencias hoy dispersas en cuatro planillas.
- La disponibilidad del costo real por ruta antes de la renegociación de 2027 de dos de los contratos bajo costo.
<!-- ===== página 42 / 49 ===== -->

- La capacitación de conductores que no están en ningún lugar fijo, de los cuales 258 no son trabajadores de la compañía, y de una torre que opera en turnos 24x7.
- El solapamiento de los meses 13 a 15 y 19 a 20, con la dotación efectivamente necesaria para sostener dos frentes en cinco terminales y en ruta.

### 17.6 Proponer una estrategia de puesta en producción y de operación

El C LIENTE despacha viajes que ocurren lejos y que en su mayoría ejecutan terceros. La propuesta deberá contener una estrategia explícita y no una declaración de intenciones:

1. Qué entra en producción primero, en qué terminal y sobre qué subconjunto de flota, y con qué criterio de avance. Se espera fundamento sobre si conviene empezar por la flota propia o por un grupo de

transportistas dispuestos.

- Cómo se prueba la verificación bloqueante en paralelo antes de bloquear efectivamente, midiendo cuántos viajes habría detenido, por qué motivo y con qué impacto comercial.
- Cómo se define y se comunica la regla de excepción al bloqueo, quién la autoriza y cómo se audita su uso.
- Cómo se ejecuta el plan de adhesión: qué se les presenta a los transportistas, en qué instancia, con qué instrumento contractual y cómo se mide.
- Qué indicadores se medirán durante la marcha blanca y con qué umbral se declara cerrada, conforme al

## Artículo 17.3 de las Bases Administrativas.

- Cómo se revierte un paso a producción fallido con doscientos camiones en ruta y con documentos de transporte ya emitidos.
- Cómo opera la solución en modo mixto durante el período —largo— en que parte de la flota estará equipada y parte no, y cómo se evita que ese período genere dos formas paralelas de trabajar que después no se puedan unificar.
- Qué dotación de acompañamiento habrá en los terminales, en horario de relevo, que es de madrugada, y en cinco regiones simultáneamente.
- Cómo se capacita a conductores que pasan por un terminal cada seis días y que en su mayoría no son trabajadores de la compañía. 10. Cómo se logra la adopción de una conductora con siete años de experiencia que hoy llena su registro en papel, y de un dueño de camión que pregunta quién paga el aparato y quién ve sus datos. 11. Cómo se transfiere la operación a un equipo de 9 personas y qué queda como servicio permanente del ADJUDICATARIO durante los 36 meses, con cobertura 24x7 y con un costo compatible con un margen operacional del 9 %.

### CAPÍTULO 18 CRITERIOS DE ACEPTACIÓN DEL CASO

Los siguientes resultados de negocio son los que el CLIENTE utilizará para juzgar si el PROYECTO fue exitoso. El PROPONENTE deberá comprometerse con ellos, proponer la meta cuando este documento no la fije, indicar en qué momento del cronograma se alcanzará cada uno y cómo se medirá.

| N° | Resultado esperado | Situación actual |
| --- | --- | --- |
| 1 | Ningún camión sale con un conductor sin jornada disponible, con una habilitación vencida o con un equipo no apto. | No se verifica nada al asignar. |
<!-- ===== página 43 / 49 ===== -->

| N° | Resultado esperado | Situación actual |
| --- | --- | --- |
| 2 | La jornada efectiva de conducción se conoce y se acredita para los 454 conductores, no sólo para los 196 propios. | 196 de 454, en papel. |
| 3 | La jornada previa de un conductor de un tercero es un dato disponible en el momento de asignar. | Inexistente. Fue la causa del accidente de febrero. |
| 4 | La evidencia de jornada resiste una alegación de manipulación y es oponible ante la autoridad, el cliente y el seguro. | Un registro en papel que el conductor completa a veces al final del día. |
| 5 | Las = 6.000 vigencias están en un registro único, con aviso anticipado y con efecto sobre la asignación. | Cuatro planillas mantenidas por personas distintas. |
| 6 | No vuelve a salir un camión con documentación de carga peligrosa que no corresponde a la carga. | Lista de chequeo en papel; una detención en abril. |
| 7 | La información del tacógrafo digital se descarga, se conserva y está disponible. | Nunca se ha descargado. |
| 8 | Existe una vista única de la flota, con posición de los 374 camiones. | Tres pantallas y 34 camiones sin dispositivo. |
| 9 | El dispositivo a bordo registra 72 horas sin cobertura y no se pierde ningún evento. | Los tramos sin señal dejan hoyos en el registro. |
| 10 | Las horas de llegada y salida en instalaciones de clientes se registran sin intervención del conductor. | Anotación en papel, a veces de memoria. |
| 11 | Los cobros por tiempo de espera se sostienen con evidencia y dejan de objetarse masivamente. | $ 340 millones facturados, 71 % objetado. |
| 12 | La conformidad de entrega está disponible el mismo día de la entrega. | Viaja en papel en la cabina durante días; 4,2 % no llega. |
| 13 | El documento electrónico de transporte se emite desde la orden de transporte, sin redigitación. | Se redigita al sistema contable. |
| 14 | Existe una solución declarada y conforme para emitir el documento en puntos de carga sin cobertura. | La práctica actual no resiste un examen. |
| 15 | Los kilómetros recorridos en vacío bajan de forma medible. | 26 % del total, resuelto por teléfono. |
| 16 | Se conoce el costo real por kilómetro y por viaje, por ruta y por contrato, de forma sistemática. | Una planilla construida en junio de 2026. |
| 17 | El costo por viaje está disponible dentro de las 24 horas de cerrado el viaje. | El combustible llega a los 40 días. |
| 18 | Se explica la dispersión del 19 % de rendimiento entre camiones del mismo modelo y ruta. | No se ha investigado. |
| 19 | Se dispone del costo real por ruta antes de la renegociación de 2027. | Dos contratos bajo costo se renegocian ese año. |
| 20 | La liquidación a 148 transportistas es automática y se corrige por excepción. | 9 días, 8 personas, 11 % corregido. |
| 21 | Cada transportista ve sus viajes y su liquidación en curso en cualquier momento. | Se entera cuando le llega el documento. |
| 22 | El cliente ve la posición y el estado de su carga, con lo que el dueño del camión haya autorizado. | Inexistente. |
| 23 | Cada dueño de camión controla qué datos comparte, con quién y hasta cuándo, y puede revocarlo. | No existe ningún mecanismo. |
<!-- ===== página 44 / 49 ===== -->

| N° | Resultado esperado | Situación actual |
| --- | --- | --- |
| 24 | Las emisiones por tonelada-kilómetro se calculan con metodología declarada y verificable, incluidos los camiones de terceros. | No se mide. |
| 25 | La intervención de un taller externo queda en la hoja de vida del equipo. | No queda registrada. |
| 26 | El mantenimiento preventivo se gatilla con kilometraje real y no con una estimación. | Odómetro leído cuando el camión pasa por el taller. |
| 27 | Existe un plan de adhesión con resultados medibles: cuántos de los 148 transportistas adhirieron y en qué plazo. | No existe la conversación. |
| 28 | Doña Yasna recibe la alerta de jornada con tiempo suficiente para llegar a un lugar donde efectivamente se pueda detener. | La regla existe; el lugar donde parar, a veces no. |
| 29 | Don Nolberto ve sus dos camiones, sus viajes y su liquidación en curso, y decide él qué información comparte y con quién. | Se entera nueve días después y no controla nada. |

> Los criterios 27, 28 y 29 son los tres que deciden este caso. El 27 mide si el PROPONENTE entendió que la mayor parte de la solución depende de personas a las que no se les puede dar una orden. El 28 mide si entendió que una alerta correcta entregada donde no hay dónde detenerse es una alerta inútil, y que eso obliga a saber algo que hoy nadie tiene: dónde están los lugares seguros de detención. Y el 29 es el más difícil de todos, porque exige diseñar para que quien entrega el dato conserve el control sobre él, que es exactamente la condición que don Nolberto puso y sin la cual no habrá dato.

### CAPÍTULO 19 CÓMO SE EVALUARÁ ESTE CASO

La evaluación se rige por el Título V de las Bases Administrativas y por la ponderación del Formulario T-21. Este capítulo precisa qué se buscará específicamente en el Caso 10 al aplicar esos criterios.

| ftem | Qué se buscará en este caso |
| --- | --- |
| Comprensión del problema | Que el PROPONENTE entienda que en esta compañía la responsabilidad y el control no coinciden: responde por viajes que ejecutan camiones ajenos conducidos por personas que no son sus trabajadores, y el dato crítico —cuántas horas lleva conduciendo esa persona— está fuera de su alcance. Que entienda además que el sistema actual sabe qué viaje se encargó y no sabe qué viaje ocurrió. |
| Esquema de solución y alcance | Que la decisión sobre cómo se obtiene la jornada de un conductor externo esté tomada, fundada y costeada, y que exista un plan de adhesión concreto para los 148 transportistas. Que la decisión sobre el sistema de gestión de 2013 no se resuelva por omisión. Que las exclusiones sean explícitas. |
| Arquitectura lógica y física | Que resuelva de forma verificable la operación de 72 horas sin cobertura, la reconexión masiva al salir de zonas de sombra, la unificación de tres plataformas de posicionamiento, el registro de tiempos en instalaciones de terceros sin instalar nada, la emisión del documento sin cobertura y el ciclo de vida de un componente distribuido en 374 vehículos. Que sea propia de esta operación y no un diagrama de referencia con el nombre cambiado. |
| Modelo y gestión de datos | Que la evidencia de jornada esté diseñada para resistir una impugnación. Que el consentimiento de cada dueño de camión sea gestionable y revocable, y que su ejercicio esté registrado. Que las veintiséis decisiones pendientes del numeral 16.1 estén resueltas y declaradas como supuesto. |
<!-- ===== página 45 / 49 ===== -->

| ítem | Qué se buscará en este caso |
| --- | --- |
| Plan de trabajo, EDT y cronograma | Que el ritmo de despliegue a bordo esté derivado de la frecuencia real con que los camiones pasan por un terminal, con cobertura acumulada declarada mes a mes. Que el plan de adhesión de los transportistas figure como actividad con duración y riesgo. Que la caracterización en terreno de la cobertura móvil esté costeada, Que la holgura por cierres del paso fronterizo esté declarada. |
| Plan de riesgos | Que los riesgos sean de este proyecto: transportistas que no adhieren, proveedores de posicionamiento que no exponen sus datos, fabricantes que no autorizan el acceso a la telemetría, un despliegue a bordo que avanza más lento que lo planificado, un bloqueo que detiene viajes comprometidos, y un período mixto que se prolonga más de lo previsto. |
| Servicios de operación y niveles de servicio | Que el modelo de soporte cubra 24x7x365 porque la flota rueda a toda hora, que clasifique en severidad máxima todo incidente que impida asignar, despachar o recibir una emergencia, y que su costo sea compatible con una empresa de margen operacional del 9 %. |
| Innovaciones | Que las cinco innovaciones sean pertinentes al transporte de carga y a los problemas de esta compañía, y no un catálogo de tecnologías de moda. Que la innovación de modelo de negocio o de contratación se haga cargo, específicamente, de la relación con los transportistas subcontratados, que es donde está el problema y donde está la oportunidad. |
| Consolidación | Que la propuesta sea internamente coherente: que la arquitectura sostenga el alcance, que la EDT contenga la arquitectura, que el cronograma refleje la EDT y que el costo derive de todo lo anterior. |

> Una advertencia final del mandante. Enelacta del directorio quedó consignada la advertencia que el gerente general pidió incorporar: el sesenta por ciento de la capacidad de esta compañía no le pertenece y esas personas no son sus trabajadores; cualquier solución que suponga que se les puede dar una orden va a fracasar el primer día. Una propuesta técnicamente impecable que instale un dispositivo en toda la flota sin explicar quién se lo pide a ciento cuarenta y ocho dueños de camión, quién lo paga y qué se les ofrece a cambio, será superada por una propuesta más modesta que traiga esa conversación resuelta. Y detrás de todo lo demás está la frase con que empezó este documento: la compañía cumplió con todo lo que estaba a su alcance, y aun así despachó a una persona que no estaba en condiciones de manejar.
<!-- ===== página 46 / 49 ===== -->

### ANEXOS DEL CASO

CAPÍTULO A MAPA DE SISTEMAS Y FLUJOS DE INFORMACIÓN ACTUALES

Descripción de los flujos de información tal como ocurren hoy. La columna «cómo viaja» es la que explica buena parte de los problemas descritos en el Capítulo 7.

| Origen | Destino | Qué información | Cómo viaja hoy |
| --- | --- | --- | --- |
| Cliente | Torre de programación | Requerimiento de transporte | Correo, teléfono y, en dos clientes, interfaz propia |
| Torre | Sistema de gestión de transporte | Orden de transporte y asignación de camión | Digitación; sin verificación de jornada ni de vigencias |
| Torre | Conductor o dueño de camión | Asignación del viaje | Teléfono y mensajería |
| Sistema de gestión | Sistema contable | Datos para el documento electrónico de transporte | Redigitación manual |
| Cliente Conductor | Camión Papel | Carga y peso efectivamente cargado Hora de llegada y de salida en el punto del cliente | Lo determina el cliente; la compañía responde por el sobrepeso Anotación manual, a veces al final del día |
| Conductor | Papel | Registro de jornada de conducción | Formulario firmado que viaja en la cabina |
| Tacógrafo digital | Nadie | Registro electrónico de conducción | El equipo lo genera; nunca se descarga |
| Camión | Plataforma de posicionamiento | Posición y eventos | Tres proveedores distintos; 34 camiones sin dispositivo |
| Telemetría de fábrica | Nadie | Kilometraje, consumo, códigos de falla y conducción de 61 tractocamiones | El equipo lo genera; nunca se descarga |
| Destinatario | Papel | Conformidad de entrega | Firma en papel que el conductor entrega al pasar por un terminal |
| Red de estaciones de servicio | Administración | Consumo de combustible con tarjeta | Liquidación mensual, con hasta 40 días de desfase |
| Estanque de San Bernardo | Administración | Combustible cargado en el terminal | Planilla |
| Dispositivo de peaje | Administración | Pasadas y montos | Liquidación mensual |
| Taller propio | Sistema de mantenimiento | Órdenes de trabajo y plan preventivo | Sistema de 2017, con kilometraje leído del odómetro en el taller |
| Taller externo en ruta | Nadie | Intervención sobre un equipo | Llega una factura; no queda en la hoja de vida del equipo |
| Prevención | Planillas | = 6.000 vigencias de conductores y equipos | Cuatro planillas separadas, mantenidas por personas distintas |
<!-- ===== página 47 / 49 ===== -->

| Origen | Destino | Qué información | Cómo viaja hoy |
| --- | --- | --- | --- |
| Terminal | Papel | Lista de verificación de carga peligrosa | Se completa antes de la salida; no se contrasta con lo cargado |
| Sistema de gestión | Administración de terceros | Viajes ejecutados por cada transportista | Extracción mensual, con ajustes manuales |
| Administración de terceros | 148 transportistas | Liquidación mensual | 9 días de proceso; 11 % se corrige después |
| Torre | Cliente | Estado del viaje | Teléfono y correo, a solicitud |
| Autoridad | Compañía | Cierre del paso fronterizo por nieve | Canales oficiales; sin integración con ningún sistema |

### CAPÍTULO B CALENDARIO Y PERFIL OPERACIONAL DE REFERENCIA

B.1 Perfil de un viaje típico de larga distancia

| Etapa | Qué ocurre | Carga sobre la solución |
| --- | --- | --- |
| Asignación | La torre decide qué camión toma el viaje, considerando ubicación, equipo, jornada y vigencias. | Es el único momento en que la solución puede impedir que algo salga mal. Debe resolverse en 30 segundos y de forma bloqueante. |
| Presentación en el origen | El camión llega al punto de carga del cliente y espera su turno. | 3 h 10 min de espera promedio. La hora de llegada debe registrarse sin intervención del conductor. |
| Carga y documentación | El cliente carga, se determina el peso y se emite el documento de transporte. | El documento debe existir antes de que el vehículo se mueva, incluso sin cobertura móvil. |
| Tramo en ruta | Conducción, con descansos obligatorios y tramos sin cobertura de más de 80 km. | Registro autónomo a bordo. Alerta de jornada con anticipación suficiente para llegar a un lugar seguro. |
| Relevo o descanso en terminal | En viajes largos, cambio de conductor o descanso reglamentario en un terminal regional. | Es el momento en que se puede intervenir el equipamiento a bordo y donde se descargan los respaldos. |
| Llegada al destino | Descarga y obtención de la conformidad del destinatario. | La conformidad debe quedar disponible el mismo día, no cuando el conductor pase por un terminal. |
| Decisión de retorno | Se define si el camión vuelve cargado o vacío. | Es la decisión de mayor impacto económico del ciclo y hoy la menos sistematizada. 26 % de los kilómetros son en vacío. |
| Cierre del viaje | Se consolidan tiempos, kilómetros, combustible, peajes e incidentes. | El costo del viaje debe estar disponible en 24 horas, indicando qué componentes aún faltan. |
<!-- ===== página 48 / 49 ===== -->

B.2 Calendario operacional y ventanas

| Período | Efecto | Consecuencia para el proyecto |
| --- | --- | --- |
| Diciembre a abril | Temporada de fruta. Máxima demanda de equipo refrigerado, esperas de más de 8 horas y peak de toda la flota. | Congelamiento. Los camiones pasan aún menos por los terminales, lo que frena cualquier despliegue a bordo. |
| Junio a septiembre | Cierres del paso Los Libertadores por nieve, en episodios impredecibles de hasta 12 días continuos. | Camiones detenidos, carga comprometida y conductores en jornada. No se puede planificar; sólo absorber. |
| Semana Santa y Fiestas Patrias | Restricciones de circulación de vehículos de carga y peaks de tránsito. | Congelamientos cortos con fecha conocida. |
| Últimos días de cada mes | Cierre de facturación a 84 clientes y liquidación a 148 transportistas. | Nueve días de proceso manual que no admiten interrupción. |
| Mayo a agosto | Menor actividad relativa de la flota refrigerada y clima adverso en el sur. | Mejor ventana para intervención mayor, siempre camión por camión. |
| Permanente | Un camión pasa por un terminal cada 6 días en promedio; el 22 % de la flota subcontratada, menos de una vez al mes. | Define físicamente el ritmo del despliegue a bordo y por lo tanto el cronograma del proyecto. |
| Permanente | La flota rueda 24x7x365. | No existe una ventana de detención de la operación. Toda intervención es por unidad y por terminal. |
| Anual | Renovación de contratos con clientes y con transportistas subcontratados. | Única oportunidad natural para incorporar obligaciones de datos, niveles de servicio y condiciones de adhesión. |

### CAPÍTULO C GLOSARIO DE LA INDUSTRIA

Vocabulario mínimo para leer este documento. No sustituye la investigación exigida en el numeral 16.2.

| Término | Significado |
| --- | --- |
| Carga peligrosa | Mercancía clasificada por su riesgo, sujeta a reglas propias de documentación, señalización, equipamiento, capacitación del conductor y plan de emergencia. |
| Conducción continua | Tiempo máximo que un conductor puede manejar sin interrumpir para descansar, fijado por la normativa laboral aplicable al transporte de carga. |
| Conformidad de entrega | Constancia firmada por el destinatario de que recibió la carga en las condiciones convenidas. Es la prueba de cumplimiento del porteador. |
| Costo por kilómetro | Costo total de operar una unidad dividido por los kilómetros recorridos. Es el indicador central para saber si una tarifa cubre o no lo que cuesta el viaje. |
| Documento electrónico de transporte | Documento tributario que ampara el traslado de mercaderías y que debe estar emitido antes de que el vehículo se mueva. |
| Dueño de camión | Persona natural o empresa pequeña propietaria de uno o pocos camiones, que presta servicio a un transportista mayor sin ser su trabajador. Es el 60 % de la capacidad de este caso. |
| Hoja de vida del equipo | Historial completo de intervenciones, mantenciones y fallas de un vehículo. En este caso está incompleta porque los talleres externos no reportan. |
<!-- ===== página 49 / 49 ===== -->

| Término | Significado |
| --- | --- |
| Jornada del conductor | Tiempo total de trabajo del conductor, que incluye la conducción y también la espera, la carga y la descarga. Está sujeta a límites legales y su registro es obligatorio. |
| Kilómetro en vacío | Kilómetro recorrido sin carga. No genera ingreso y consume combustible, neumáticos y jornada. Es la principal ineficiencia estructural del transporte de carga. |
| Peso por eje | Distribución del peso total del vehículo entre sus ejes. Su exceso es infracción y se controla en plazas de pesaje, aunque quien carga es el cliente. |
| Plaza de pesaje | Instalación de la autoridad vial donde se controla el peso de los vehículos de carga y se cursan infracciones por sobrepeso. |
| Porteador | Quien se obliga a transportar la carga y responde por su pérdida, daño o retraso conforme al contrato de transporte. |
| Recapado | Reacondicionamiento de un neumático usado para extender su vida útil. Es una práctica habitual de control de costos en flotas de carga. |
| Relevo | Cambio de conductor en un punto intermedio del viaje, para cumplir con los límites de jornada sin detener la unidad. |
| Semirremolque | Unidad de carga sin motor que se acopla al tractocamión. Rampla plana, furgón seco, furgón refrigerado, tolva o portacontenedores. |
| Tacógrafo | Dispositivo que registra la velocidad, la distancia y los tiempos de conducción y descanso de un vehículo. En su versión digital, genera un registro descargable. |
| Telemetría de fábrica | Información que el propio vehículo genera y transmite: kilometraje, consumo, códigos de falla y patrones de conducción. Su acceso depende de cada fabricante. |
| Tiempo de espera | Tiempo que el camión permanece en las instalaciones del cliente sin operar. Los contratos contemplan un tiempo libre y un cobro a partir de allí. |
| Tonelada-kilómetro | Unidad que combina peso transportado y distancia recorrida. Es la base habitual para expresar productividad y emisiones en transporte de carga. |
| Tractocamión | Unidad motriz que arrastra uno o más semirremolques. Es el activo principal y el que porta la mayor parte del equipamiento tecnológico. |
| Transportista subcontratado | Empresa o persona que ejecuta viajes por cuenta de otra, con vehículos y conductores propios. Ejecuta la operación sin pertenecer a la organización que la programa. |
| Viaje | Unidad de la operación: una carga que se traslada desde un origen a un destino, con un camión, un conductor y su documentación. |
| Zona de sombra | Tramo de ruta sin cobertura de red móvil. En este caso los hay de más de 80 km continuos y son parte permanente de la operación. |