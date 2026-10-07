# Subdocumento 3. Esquema de solución y alcance

audIT, Empresa N.º 10. Licitación TFEP-01/2026, Caso 10 Transporte de Carga. Oferta Técnica, Sobre N.º 2. Informe Preparatorio 2. Archivo AUDIT-Subdocumento3.pdf. Anexos: Formulario T-12 en el archivo AUDIT-Formulario-T-12.pdf.

## Resolución de observaciones del Informe 1

El FEP01, Artículo 46, p. 28 pide resolver en cada informe las observaciones de la instancia anterior, con trazabilidad entre observación, respuesta y sección modificada. La tabla reúne las observaciones del Informe 1 que corresponden a este documento y la sección donde se resuelve cada una.

**Resolución de las observaciones del Informe 1, conforme a FEP01, Artículo 46, p. 28**

| N.º | Observación | Respuesta | Sección modificada |
|---|---|---|---|
| 01 | Formulario T-12 ausente pese a que el Subdocumento 3 pág. 6 indica que acompaña la oferta técnica. | Se acepta. Existe T-12 en archivo propio con 42 requerimientos: 28 funcionales y 14 no funcionales. Se cotejaron sus identificadores, campos, contextos, paquetes EDT y referencias con los 120 casos de T-17; la matriz de pruebas conserva cobertura diseñada y no declara ejecución. | S3 3.2.8; T-12; T-17, matriz de requisitos, casos y alcance de verificación. |
| 12 | Nombres de integrantes y equipos internos de trabajo dentro de la oferta técnica en S13 y S3. | Se acepta. El cotejo de las fuentes de S1/S2/S9 y del cuerpo de S3/T-12 verifica voz corporativa sin delegación interna. Las declaraciones de uso de IA se conservan como obligación del formato y su revisión humana permanece pendiente; no se acredita purga integral de S13 ni de otros capítulos. | S1/S2/S9; cuerpo S3/T-12; declaraciones de uso de IA. |
| 37 | No existe esquema de solución, cero figuras en 18 páginas | Se acepta. La sección 3.3 dibuja el esquema conceptual con usuarios, canales, los seis contextos, integración, borde y sistemas que se conservan, y lo recorre por partes. El capítulo trae cinco figuras propias, cada una citada antes y explicada después | 3.1, 3.2.8, 3.3 y 3.4.2 |
| 38 | No hay modelo conceptual, componentes ni trazabilidad de requerimiento a componente | Se acepta. S3 describe seis contextos y T-12 vincula los 42 requerimientos con contexto, paquete EDT y casos. T-17 incorpora variantes específicas para esas referencias, distinguiendo el ensayo unitario de la verificación de integración, sistema y hardware. No se declara ejecución ni cobertura de los 54 paquetes por el solo conteo. | S3 3.2.8 y 3.3.1; T-12; T-17, matriz de trazabilidad. |
| 39 | El capítulo abre sin explicar su objetivo ni su relación con el Subdocumento 2 | Se acepta. El capítulo abre con su resumen y una introducción que lo conecta con los subdocumentos 2, 4, 7 y 9 y con el Formulario T-12. La sección 3.4.1 cruza cada problema del Capítulo 2 con su capacidad, sus requerimientos y su criterio | Introducción y 3.4.1 |
| 40 | La sección 1.4 remite a una sección 4 que no existe en el documento | Se acepta. Las referencias a otros subdocumentos se generan desde sus etiquetas y apuntan a la sección exacta del Subdocumento 4 | Subdocumento 3 completo |
| 41 | La Etapa 1 es una tabla de capacidades sin identificador y la Etapa 2 un párrafo, sin dependencias, hitos externos ni capacidad de absorción del mandante | Se acepta. Diez capacidades E1-01 a E1-10 y seis E2-01 a E2-06 con contexto, dependencia e hito. El reparto se justifica por dependencias, riesgo, hitos del numeral 13.2, incluido el de 2029, y la capacidad de absorción de un área de tecnología de nueve personas | 3.2.1, 3.2.2 y 3.2.3 |
| 42 | Exclusiones copiadas en parte, supuestos sin lista y restricciones no recogidas | Se acepta. Las diez exclusiones del Capítulo 11 con la dependencia que generan, ocho supuestos del alcance con su efecto y su validación, y las catorce restricciones agrupadas por lo que condicionan | 3.2.5, 3.2.6 y 3.2.7 |
| 43 | La decisión sobre el sistema de gestión de 2013 no se menciona, y el Capítulo 5 del Caso la llama la decisión de arquitectura más importante | Se acepta. S3 decide sustitución por funciones detrás de capa anticorrupción: asignación, seguimiento y liquidación en M16, órdenes y tarifas cliente en M21, conservación de solo lectura hasta M24. El ERP contable permanece como único emisor tributario; T-17 incorpora convivencia y reintentos sin duplicación. | S3 3.2.4; T-17 CP-INT-05 y CP-SYS-05, variante RNF-011. |
| 44 | Sin visión de arquitectura empresarial ni análisis de interoperabilidad, escalabilidad, seguridad o desempeño | Se acepta. El esquema parte de las capacidades del negocio y sus seis contextos, y analiza cinco atributos de calidad con el dato del Caso que dimensiona cada uno | 3.3 y 3.3.3 |
| 45 | Se declaran 42 requisitos, se muestran 12 y el Formulario T-12 no se entregó | Se acepta. El Formulario T-12 va en archivo propio con los 42 requerimientos, y el capítulo resume su distribución por contexto, etapa y prioridad | 3.2.8 y Formulario T-12 |
| 46 | Los requisitos mostrados no tienen actor, precondición, resultado esperado ni prioridad, que exige el numeral 17.1 del Caso | Se acepta. Cada requerimiento funcional trae actor, precondición, resultado esperado, prioridad y origen, y cada no funcional su categoría, umbral, método de verificación y a quién es exigible | Formulario T-12 |
| 47 | No hay registro de reglas de negocio: cómputo de jornada, excepción al bloqueo, tiempo libre de espera ni asignación del retorno | Se acepta. Doce reglas de negocio con su fuente y quién puede cambiarlas, entre ellas el cómputo de jornada, la excepción al bloqueo, el tiempo libre de espera, la base de la liquidación y la asignación del retorno | 3.2.9 y Formulario T-12 |
| 48 | No hay matriz de trazabilidad de origen a requerimiento, componente y prueba | Se acepta. Se cotejaron los 42 códigos y todas sus referencias a casos existentes. La matriz de T-17 registra paquetes EDT y comprobaciones diseñadas, con límites de simulación y homologación. La correspondencia documental no acredita pruebas ejecutadas ni aprobación contractual. | S3 3.2.8; T-12; T-17, matriz de requisitos y variantes por caso. |
| 49 | No existen implementación, implantación ni operación: ingeniería de software, integración continua, migración, corte, reversión, observabilidad ni recuperación | Se acepta y se aclara. Se incorporan las tres secciones con el ciclo de desarrollo, el montaje camión por camión, la prueba en paralelo del bloqueo, la reversión y la operación 24x7. Se aclara que el Formulario T-7 (p. 57) no las asigna al Subdocumento 3, y que su detalle está en los subdocumentos 6 y 7, que esta instancia entrega | 3.4.4, 3.4.5 y 3.4.6 |
| 50 | La modalidad de datos promete jornada acreditada con un equipo que no identifica al conductor, cuando su evidencia real es la atestación del transportista | Se acepta. S3 distingue fuente de posición y prueba de jornada; T-17 corrige la atribución de atestación a una API GPS. La atestación debe ser firmada por el transportista y genera marca; ausencia de fuente e incumplimiento legal bloquean. La modalidad de datos no identifica por sí sola al conductor. | S3 3.3.2 y 3.4.3; T-17 CP-INT-07, CP-SYS-05 y CP-UAT-09. |
| 51 | Se dice que los 29 criterios están comprometidos y sólo ocho tienen meta, hito y medición | Se acepta. Los 29 criterios tienen meta, mes y medición en el Formulario T-12, clasificados en resultado del Caso, meta propuesta por audIT y parámetro fijado en la Etapa 1 | 3.2.10 y Formulario T-12 |
| 52 | Códigos sin definir, como la decisión D-02 y el supuesto S-09 | Se acepta. Cada código se define en su primera mención y en el glosario del Formulario T-12. Las decisiones del numeral 16.1 se citan como DP para no confundirlas con las decisiones propias de la oferta | Subdocumento 3 y Formulario T-12 |
| 76 | La restricción 8 fija al sistema contable como único emisor del DET y la consulta citada (15) no aparece en tabla de S3. | Se acepta y se aclara. S3/T-12 mantiene el ERP contable como único emisor y prevé DET anticipado desde la orden o solicitud por enlace satelital con folio de vuelta. T-17 incorpora ambas variantes, idempotencia, acceso local antes del movimiento y bloqueo ante documento no conforme. La prueba diseñada no acredita interfaz homologada ni conformidad tributaria obtenida. | S3 3.4.2; T-12 RF-013/RF-014/RNF-006; T-17 CP-UNIT-21, CP-INT-11/12, CP-SYS-11 y CP-HW-11. |

## 3 Esquema de solución y alcance

> **Resumen de apertura.**
>
> Este capítulo define qué construye audIT para Transportes Curimón, en qué orden y con qué resultado
> medible. La solución hace coincidir la responsabilidad con el control: la compañía responde por la
> jornada de 454 conductores y hoy sólo controla, en papel, la de 196. Las cuatro decisiones de fondo
> están tomadas en este capítulo: quién acredita la jornada de un conductor externo, qué ocurre con el
> sistema de gestión de 2013, cómo se emite el documento de transporte sin cobertura y qué entra en
> cada etapa.
>
> **Qué recibe Transportes Curimón S.A.**
> - El alcance de la Etapa 1 y de la Etapa 2 con su criterio de reparto y sus hitos en el calendario real.
> - El catálogo de 42 requerimientos, doce reglas de negocio y los 29 criterios de aceptación con meta, mes y medición.
> - El esquema de la solución y su correspondencia uno a uno con los seis contextos de la arquitectura lógica.
> - El plan de adhesión de los 148 transportistas y la estrategia con cada grupo de interés.

El capítulo parte de la comprensión del problema del Subdocumento 2 y entrega lo que los capítulos
siguientes desarrollan. La sección 3.1 resume el ciclo completo del contrato. La sección 3.2 delimita
el alcance: reparto entre etapas, decisión sobre el sistema de 2013, exclusiones, supuestos,
restricciones, catálogo, reglas de negocio y criterios de aceptación. La sección 3.3 dibuja el esquema
de la solución, y la sección 3.4 explica cómo funciona un viaje, cómo se consigue la adhesión de los
transportistas y cómo se implementa, se implanta y se opera. Los nombres de los componentes son los
mismos de la arquitectura lógica del Subdocumento 4 (sección ?), el plan de trabajo
del Subdocumento 7 usa los paquetes de trabajo que aquí se citan y el Subdocumento 9 prueba cada
requerimiento con los casos que el Formulario T-12 le asigna.

El Formulario T-12 acompaña este capítulo como archivo propio, conforme al Comunicado 10, sección 1. Contiene el catálogo completo con los campos que exige el
Caso, numeral 17.1, p. 38, la matriz de trazabilidad de cada requerimiento hasta su componente, su
paquete de trabajo y su prueba, el registro de reglas de negocio, el registro de supuestos con las
veintiséis decisiones del Caso, numeral 16.1, p. 34, los 29 criterios de aceptación y el registro de
consultas.

## 3.1 Resumen Ejecutivo de la Solución

Transportes Curimón responde ante la autoridad, ante sus clientes y ante su aseguradora por viajes que
en un 60,4 % ejecutan camiones ajenos, conducidos por 258 personas que no son sus trabajadoras
(Caso, numeral 2.2, p. 6). El dato que decide si un viaje puede salir, cuántas horas lleva conduciendo esa
persona, está fuera de su alcance, y el sistema de gestión de 2013 sabe qué viaje se encargó pero no
qué viaje ocurrió (Caso, capítulo 5, p. 12). La solución de audIT cierra esa brecha con tres piezas que no
funcionan por separado.

La primera es la evidencia. Cada viaje se asigna con un veredicto de jornada, habilitaciones y aptitud
del equipo, calculado en no más de 30 segundos (Caso, RT-09.01, p. 32), y cada veredicto queda con su
fuente y su nivel de prueba. La segunda es la adhesión: lo que depende de 148 transportistas se obtiene
por contrato y por incentivo, nunca por orden (Caso, capítulo 10, restricción 2, p. 23). La tercera es la
operación desconectada: el registro del viaje vive a bordo del camión durante los tramos sin señal y se
consolida en la nube al reconectarse, de modo que la cobertura móvil no condiciona la prueba.

La necesidad de compatibilizar fuentes heterogéneas y autonomía del transportista, diagnosticada en la sección 2.4 del Subdocumento 2, se atiende mediante ingesta por cada plataforma y homologación progresiva de compatibilidad. La adhesión se apoya en el expediente verificable y la transparencia de liquidaciones como incentivos, sin imponer el reemplazo de sistemas de terceros. Estos mecanismos son decisiones de solución: su cobertura depende de validar acceso, permisos y aptitud de los equipos, conforme a SUP-01 y SUP-02 del diagnóstico y al estándar de homologación recogido en la sección 3.2.5.

El contrato dura 56 meses y su cronograma es el del FEP01, Artículo 17.1, p. 12, sin alteración. La Etapa 1 se
desarrolla entre los meses 1 y 12, convive con la operación vigente en marcha blanca entre los meses 13
y 15 y pasa a producción en el mes 16. La Etapa 2 se desarrolla entre los meses 13 y 18, en paralelo
con la marcha blanca de la Etapa 1, tiene marcha blanca en los meses 19 y 20 y pasa a producción en el
mes 21, que es también la aceptación final de la implementación. La operación cubre los meses 21 a 56,
36 meses continuos con atención 24x7x365.

El calendario real importa tanto como los meses contractuales, porque el Caso prohíbe pasos a
producción entre diciembre y abril (Caso, numeral 13.3, p. 28). Los meses 16 y 21 están separados por cinco
meses, que es también la duración de esa ventana. Por eso el mes 16 sólo puede caer en mayo o junio y
el 21 en octubre o noviembre. Con el inicio del contrato en febrero de 2027 (supuesto SA-01 de la
sección 3.2.6), la Etapa 1 pasa a producción en mayo de 2028, después de la temporada de fruta, y la
Etapa 2 en octubre de 2028, después de Fiestas Patrias y antes del congelamiento siguiente. La
Figura 3.1 muestra los primeros 24 meses sobre el calendario.

**Figura 3.1. Ciclo contractual de los primeros 24 meses sobre el calendario, con inicio en febrero de 2027. En gris, la temporada de fruta de diciembre a abril**

Fuente: elaboración propia sobre el Artículo 17 de las Bases Administrativas y las restricciones estacionales del Caso, capítulos 4 y 10. Febrero de 2027 es el supuesto de inicio declarado en esta propuesta.

[Consultar diagrama en el PDF](AUDIT-Subdocumento3.pdf).

La figura deja a la vista la consecuencia que el cronograma obligatorio impone y que el plan no puede
eludir: la marcha blanca de la Etapa 1 cae entera en la temporada de fruta, entre febrero y abril de
2028. La marcha blanca no es un paso a producción ni interviene camiones, y la solución la usa a su
favor: la verificación bloqueante corre en paralelo durante el peak de actividad, que es la condición
más exigente para medir cuántos viajes habría detenido. Todo el montaje a bordo termina antes de
diciembre de 2027 y se reanuda en mayo de 2028, según la sección 3.4.5.

Tres resultados resumen lo que el mandante recibe al cierre de la implementación. Desde el mes 16
ningún viaje asignado por la plataforma sale sin veredicto de jornada, habilitaciones y aptitud. Desde
el mes 16 el costo de cada viaje está disponible dentro de las 24 horas de su cierre y la liquidación a
los transportistas toma un día hábil. Y desde el mes 21 el cliente ve la posición de su carga dentro de
lo que cada dueño de camión autoriza, con las cuatro condiciones de renovación del cliente mayor para
2029 cubiertas un año antes de ese plazo (Caso, numeral 13.2, p. 27).

> **Compromiso C-01.** Ningún viaje asignado por la plataforma sale sin un veredicto favorable o una excepción autorizada y registrada conforme a la regla RN-04.
>
> Métrica: Cero salidas con jornada, habilitación o equipo no apto desde el mes 16. Se verifica en: Criterio de aceptación 1 del Caso, auditoría mensual del total de asignaciones. Fuente: Caso, capítulo 18, p. 41.

## 3.2 Alcance

El alcance se descompone en capacidades asignadas a los seis contextos de la arquitectura lógica. Esta
sección explica primero con qué criterio se reparten entre las dos etapas, después toma la decisión
sobre el sistema de 2013, y luego declara exclusiones, supuestos, restricciones, el catálogo de
requerimientos, las reglas de negocio y los criterios de aceptación. Cada código que aparece aquí se
define en su primera mención y en el glosario del Formulario T-12.

### 3.2.1 Criterio de reparto entre la Etapa 1 y la Etapa 2

El comité expresó un orden de urgencia: primero la seguridad, luego el viaje real y la evidencia de los
tiempos, y al final el costo por kilómetro, la liquidación y las emisiones (Caso, numeral 13.1, p. 26). El
mismo numeral advierte que ese orden es una preferencia y no una definición de alcance, y pide
justificar el reparto por dependencias técnicas, riesgo, hitos externos y capacidad de absorción del
mandante. audIT aplica esos cuatro criterios en ese orden y el resultado coincide con el comité en tres
puntos y lo altera en dos.

Coincide en que la seguridad va primero, y no por deferencia. La verificación bloqueante de la
asignación necesita dos insumos que no existen hoy: el registro único de las cerca de 6.000 vigencias y
el expediente de jornada de cada conductor (Caso, capítulo 18, pp. 41 y 42). Los dos son también entrada del
viaje real, del costo y de la liquidación. Construirlos primero no es una preferencia: sin ellos, nada
de lo demás tiene sobre qué apoyarse.

Coincide también en que la posición en tiempo real al cliente no se adelanta, y acoge la objeción del
jefe de control de flota: no puede prometerse posición al cliente antes de saber qué están dispuestos a
compartir los dueños de camión, y esa conversación toma meses (Caso, numeral 13.1, p. 26). La adhesión
avanza durante toda la Etapa 1 y el portal de clientes con posición entra en la Etapa 2, cuando la base
de consentimientos ya existe. Y coincide en dejar el cálculo productivo de emisiones para la Etapa 2:
la exigencia del cliente mayor es para 2029, y lo que no admite espera es fijar el método, no producir
el número.

Lo altera en el costo. La objeción de la gerenta de administración y finanzas es un hito externo con
fecha: dos de los tres contratos que hoy se sirven bajo costo se renegocian en 2027 (Caso, numeral
13.2, p. 27). Con el inicio en febrero de 2027, incluso la producción de la Etapa 1 llega en mayo de 2028,
después de esa renegociación. Adelantar el costeo a la Etapa 1, como planteó el Informe 1, no alcanza.
audIT lo resuelve en dos tiempos. En el mes 6, julio de 2027, entrega un estudio de costo real por ruta
y por contrato construido con los datos históricos que ya existen (liquidaciones de combustible,
peajes, neumáticos, remuneraciones y la planilla de junio de 2026) cargados en el repositorio
analítico. En el mes 16, el costeo por viaje entra en producción como dato operacional de cada viaje.

**Decisión D-01. Costo real por ruta antes de la renegociación de 2027**

| Se decide | Se descarta | Criterio | Fuente |
|---|---|---|---|
| Estudio de costo por ruta y contrato con datos históricos en el mes 6 y costeo por viaje en producción en el mes 16 | Dejar el costo para la Etapa 2, como sugiere el orden del comité, o sólo adelantarlo a la Etapa 1 | La renegociación ocurre en 2027 y la Etapa 1 pasa a producción en mayo de 2028. Sólo un entregable analítico anterior llega a tiempo | Caso, numeral 13.2, p. 27 y criterio 19 del Caso, capítulo 18, p. 42 |

Lo altera también en la jornada del conductor externo, que el comité ubica dentro de la seguridad pero
cuyo plazo no lo fija la tecnología. La acreditación de esa jornada depende de que el transportista
firme el anexo de adhesión, y esa negociación con 148 contrapartes no se paraleliza. Por eso la
campaña de adhesión empieza en el mes 1, como actividad con duración, responsable y riesgo propios, y
no espera a que el software esté listo. La capacidad de absorción del mandante cierra el reparto: un
área de tecnología de nueve personas (Caso, capítulo 10, restricción 13, p. 24) no puede recibir los dos
alcances a la vez, y la Etapa 2 sólo agrega procesos que no cambian la forma de despachar.

### 3.2.2 Alcance de la Etapa 1

La Etapa 1 controla lo que puede producir un despacho ilegal, una pérdida de prueba, una duplicación
tributaria o un tratamiento indebido de datos personales. La Tabla 3.1 identifica sus diez
capacidades con el contexto de la arquitectura que las sostiene y la capacidad de la que dependen. El
paquete de trabajo de cada una está en el Formulario T-12.

**Tabla 3.1.** Capacidades de la Etapa 1, contexto responsable y dependencias

| ID | Capacidad | Contexto | Depende de |
|---|---|---|---|
| E1-01 | Registro único de vigencias con alertas | Personas y cumplimiento, y Flota y activos | Migración verificada |
| E1-02 | Expediente de jornada con nivel de evidencia | Personas y cumplimiento | E1-07 y adhesión |
| E1-03 | Asignación con verificación bloqueante | Planificación y tráfico | E1-01 y E1-02 |
| E1-04 | Lista de verificación de carga peligrosa | Operación de fletes | E1-01 |
| E1-05 | Documento de transporte desde la orden | Operación de fletes | E1-03 |
| E1-06 | Llegada, salida, espera y conformidad | Telemetría y geocercas, y Operación de fletes | E1-07 |
| E1-07 | Vista única de flota y operación sin enlace | Telemetría y geocercas | Montaje y plataformas |
| E1-08 | Costo por viaje y liquidación | Liquidación y costeo | E1-06 |
| E1-09 | Portal del transportista y consentimiento | Personas y cumplimiento | Adhesión |
| E1-10 | Método de emisiones y retiro parcial del sistema de 2013 | Liquidación y costeo, y capa anticorrupción | E1-08 |

*Fuente: elaboración propia sobre el Caso, capítulo 18, p. 41 y la sección ?.*

La tabla muestra una cadena y no una lista: E1-01 y E1-02 alimentan la asignación, la asignación
alimenta el documento, y el registro de tiempos alimenta el costo y la liquidación. Dos dependencias
quedan fuera del software y gobiernan el plazo real: el montaje a bordo, que sigue el paso de los
camiones por los terminales, y la adhesión, que sigue la negociación con los transportistas. Por eso
el Subdocumento 7 las trata como actividades de la red, con duración y holgura propias.

### 3.2.3 Alcance de la Etapa 2

La Etapa 2 agrega procesos que se apoyan en datos que la Etapa 1 ya produce y que no cambian la forma de
despachar. La Tabla 3.2 identifica sus seis capacidades.

**Tabla 3.2.** Capacidades de la Etapa 2, contexto responsable y hito que atienden

| ID | Capacidad | Contexto | Hito o criterio |
|---|---|---|---|
| E2-01 | Posición y estado de la carga para el cliente | Telemetría y geocercas | Criterio 22 y hito de 2029 |
| E2-02 | Asignación de retornos | Planificación y tráfico | Criterio 15 |
| E2-03 | Cálculo mensual de emisiones por tonelada-kilómetro | Liquidación y costeo | Criterio 24 y hito de 2029 |
| E2-04 | Intervenciones de talleres externos y mantenimiento por kilometraje real | Flota y activos | Criterios 25 y 26 |
| E2-05 | Explicación de la dispersión de rendimiento | Liquidación y costeo | Criterio 18 |
| E2-06 | Retiro completo del sistema de 2013 | Planificación y tráfico, y capa anticorrupción | Decisión 3 del numeral 16.1 |

*Fuente: elaboración propia sobre el Caso, numeral 13.2, p. 27 y el Caso, capítulo 18, p. 42.*

Dos de las seis capacidades responden al hito de 2029, cuando el cliente que representa el 19 % de los
ingresos renueva exigiendo documento integrado, posición en tiempo real, emisiones verificadas y
jornada acreditada también en los camiones subcontratados (Caso, numeral 13.2, p. 27). La Etapa 1 cubre la
primera y la cuarta. La Etapa 2 cubre las otras dos en octubre de 2028, lo que deja un año de
operación con evidencia acumulada antes de la renovación. El diseño admite además el sexto terminal
y los 430 camiones proyectados por parametrización, sin rehacer la solución (Caso, RT-02.12, p. 31).

### 3.2.4 Decisión sobre el sistema de gestión de transporte de 2013

El sistema de gestión de transporte implantado en 2013 maneja las órdenes de transporte, la asignación
de viajes, las tarifas, el control de viajes y la base de la liquidación a transportistas. El Caso lo
llama la decisión de arquitectura más importante y exige resolverla con fundamento técnico y económico
(Caso, capítulo 5, p. 12). No debe confundirse con el sistema contable y de facturación, que se mantiene
como único emisor de documentos tributarios (Caso, capítulo 10, restricción 8, p. 24). audIT evaluó las
cuatro alternativas que el Caso, numeral 16.1, p. 34 enumera, más un paquete de mercado, con los criterios
de la Tabla 3.3.

**Tabla 3.3.** Alternativas evaluadas para el sistema de gestión de 2013

| Alternativa | Riesgo de corte | Conoce el viaje real | Costo recurrente |
|---|---|---|---|
| Reemplazo en un solo evento | Alto | Sí | Bajo, propio |
| Conservar e integrar | Bajo | No | Medio, dos sistemas |
| Paquete de mercado | Alto | Parcial | Alto, por camión |
| Sustitución por funciones | Bajo | Sí | Bajo, propio |

*Fuente: elaboración propia sobre el Caso, capítulo 5, p. 12, el Caso, numeral 16.1, p. 34 y la Caso, restricción 11, p. 24.*

El reemplazo en un solo evento queda descartado por la operación: la flota rueda 24x7x365 sin ventana
de detención (Caso, capítulo 10, restricción 11, p. 24), y un corte único exigiría que órdenes, asignación,
tarifas y liquidación cambien la misma noche, con 200 camiones en ruta y un cierre mensual de nueve
días que no admite interrupción. Conservar e integrar deja intacto el problema que el Caso describe: el
sistema seguiría sin conocer el viaje que ocurrió, y la verificación bloqueante y el costo por viaje
tendrían que vivir fuera de él, con dos registros del mismo viaje que nadie concilia. El paquete de
mercado resuelve órdenes y tarifas, pero ninguno de los evaluados trae la cascada de evidencia de
jornada, el consentimiento revocable por dueño de camión ni la liquidación desde la evidencia, de modo
que habría que construir esas piezas igual, y su licencia por unidad crece con la flota hacia 430
camiones, en una compañía con 9 % de margen operacional (Caso, numeral 2.3, p. 7).

**Decisión D-02. Sistema de gestión de transporte de 2013**

| Se decide | Se descarta | Criterio | Fuente |
|---|---|---|---|
| Sustitución función por función detrás de una capa anticorrupción, con retiro completo en el mes 21 | Reemplazo en un solo evento, conservar e integrar, y paquete de mercado | Único camino que conoce el viaje real sin corte único. El costo recurrente queda en una sola plataforma propia del mandante | Caso, capítulo 5, p. 12, decisión 3 del Caso, numeral 16.1, p. 34 y fowler2004_strangler () |

La sustitución por funciones aplica el patrón de estrangulamiento: la plataforma nueva crece alrededor
del sistema existente y le quita funciones una a una hasta que deja de usarse
(fowler2004_strangler, ). La capa anticorrupción que exige RT-05.20 traduce entre los dos
modelos mientras conviven (sección ?). La Tabla 3.4 fija qué función
pasa a qué contexto y cuándo.

**Tabla 3.4.** Retiro del sistema de 2013 función por función

| Función del sistema de 2013 | Contexto que la asume | Mes en producción |
|---|---|---|
| Asignación de viajes | Planificación y tráfico | 16 |
| Control de viajes | Operación de fletes | 16 |
| Base de la liquidación y tarifas de transportistas | Liquidación y costeo | 16 |
| Órdenes de transporte | Planificación y tráfico | 21 |
| Tarifas a clientes | Liquidación y costeo | 21 |
| Consulta histórica | Repositorio analítico | 21, solo lectura hasta el 24 |

*Fuente: elaboración propia.*

Entre los meses 16 y 21 el sistema de 2013 sigue recibiendo las órdenes y la capa anticorrupción las
publica como eventos hacia la plataforma, que asigna, controla y liquida. En el mes 21 las órdenes y las
tarifas a clientes pasan a la plataforma y el sistema de 2013 queda sólo para consulta. Su retiro
definitivo ocurre en el mes 24, cuando la migración de cinco años de viajes y seis de liquidaciones que
exige RT-05.15 está conciliada (Caso, RT-05.15, p. 31). El fundamento económico se expresa sin montos, por
el FEP01, Artículo 50.2, p. 29: la alternativa elegida evita la licencia por unidad, evita mantener dos sistemas
durante 36 meses de operación y concentra el costo en la construcción, que es propiedad del mandante.
La valorización comparada va en la Oferta Económica. El Subdocumento 4 registra la misma decisión como
registro de decisión de arquitectura.

### 3.2.5 Exclusiones explícitas

El Caso declara diez materias que no pide y advierte que lo excluido no puede ignorarse en el diseño:
la solución debe convivir con todo ello y sus dependencias deben quedar identificadas
(Caso, capítulo 11, p. 24). La Tabla 3.5 recoge las diez y la dependencia que cada una genera.

**Tabla 3.5.** Exclusiones del Caso y dependencia que generan en la solución

| N.º | Lo que no se pide | Con qué convive la solución |
|---|---|---|
| 1 | Reemplazar el sistema contable y la emisión tributaria | Capa anticorrupción y regla RN-11 |
| 2 | Intervenir los sistemas o la electrónica del vehículo | Lectura sin contacto y de solo lectura |
| 3 | Reemplazar las plataformas de posicionamiento de terceros | Ingesta de las tres plataformas y estándar de homologación |
| 4 | Remuneraciones y administración de personal | Jornada con valor probatorio como insumo de la remuneración |
| 5 | Contabilidad de los transportistas | Liquidación de lo que la compañía les debe |
| 6 | Mercado de cargas o intermediación | Retornos sólo con carga propia, regla RN-09 |
| 7 | Operar talleres externos | Registro de su intervención en la hoja de vida |
| 8 | Sustituir sistemas de aduana o de clientes | Integración donde exista interfaz |
| 9 | Infraestructura en puntos de carga y descarga | Geocercas virtuales, regla RN-07 |
| 10 | Adquirir el hardware | Especificación exacta en el Formulario T-11 |

*Fuente: Caso, capítulo 11, p. 24.*

Cada exclusión deja una obligación de diseño. Las exclusiones 1, 3 y 8 se traducen en integraciones de
la capa anticorrupción con su propio contrato de interfaz, y las 2 y 9 restringen dónde puede capturarse
el dato. La exclusión 10 traslada al mandante la compra y a audIT la responsabilidad de que lo comprado
sea exactamente lo necesario, que el Subdocumento 4 resuelve en 182 equipos a bordo más repuestos.

### 3.2.6 Supuestos del alcance

Los supuestos del entorno, sobre la disposición de terceros a compartir información, están en la
sección 2.5 del Subdocumento 2 con los códigos SUP-01 a SUP-06. Esta sección declara los supuestos de la
propuesta: decisiones que audIT toma por el mandante para poder fijar plazos y metas. Cada uno lleva su
efecto si resulta falso y la instancia en que se valida, como pide el Caso, numeral 17.1, p. 38. La
Tabla 3.6 los resume y el Formulario T-12 los completa con las veintiséis decisiones del
numeral 16.1.

**Tabla 3.6.** Supuestos del alcance, efecto si fallan y validación

| ID | Supuesto | Efecto si es falso | Se valida |
|---|---|---|---|
| SA-01 | El mes 1 es febrero de 2027 | Con enero, el mes 16 cae en abril, prohibido | Firma del contrato |
| SA-02 | Paso por terminal cada 6 días y 22 % de terceros bajo una vez al mes | Se recalcula la cobertura mensual | Registro de portería, meses 1 a 3 |
| SA-03 | Dos de las tres plataformas entregan datos por interfaz | Esos camiones se tratan como sin equipo | Factibilidad, meses 1 a 4 |
| SA-04 | El sistema contable recibe datos por interfaz | Se usa intercambio de archivos con conciliación | Prueba técnica, mes 3 |
| SA-05 | La renegociación de 2027 es posterior a julio | El estudio se entrega por contrato, primero los tres bajo costo | Gerencia de finanzas, mes 1 |
| SA-06 | La autoridad admite el registro electrónico de jornada | Se mantiene el respaldo en papel firmado | Consulta C-10, mes 2 |
| SA-07 | El mandante firma los anexos de adhesión | La adhesión no avanza y se activa el gatillo | Comité Ejecutivo, mes 1 |
| SA-08 | Los terceros con equipo conservan su contrato con su proveedor | Pierden posición y pasan a modalidad documental | Seguimiento mensual de adhesión |

*Fuente: elaboración propia. SA: supuesto del alcance.*

El supuesto SA-01 es el único que audIT pide fijar en el contrato. El FEP01, Artículo 10.2, p. 8 cuenta los meses
desde la fecha de inicio, con el mes 1 como el primer mes completo de ejecución. Con la adjudicación el
1 de diciembre de 2026 FEP01, Formulario T-20, p. 65, una firma en enero de 2027 deja febrero como primer mes
completo. Si el inicio fuera enero, el mes 16 caería en abril de 2028 y ninguna estrategia lo
corregiría sin alterar el Artículo 17. El supuesto SA-08 nace de un riesgo que el Subdocumento 8 trata:
el apagado de las redes 2G y 3G puede dejar sin señal equipos de terceros que hoy reportan posición.

### 3.2.7 Restricciones del alcance

Las catorce restricciones del Caso no se discuten (Caso, capítulo 10, p. 23). Lo que esta sección hace es
mostrar qué parte del alcance condiciona cada una, porque varias se cumplen sólo si el diseño las
tiene en cuenta desde el principio. La Tabla 3.7 las agrupa por el componente que
restringen.

**Tabla 3.7.** Restricciones del Caso agrupadas por lo que condicionan

| Restricción | Condiciona | Respuesta en el alcance |
|---|---|---|
| 1 y 6 | Equipo a bordo | Captura automática, cero interacción en marcha, lectura sin contacto |
| 2, 3 y 7 | Jornada de terceros | Sujeto obligado al dueño del camión y cascada de evidencia |
| 4 y 12 | Operación sin enlace | 72 horas a bordo y absorción de 12 días de cierre |
| 5, 10 y 11 | Montaje y despliegue | Sólo en terminal, camión por camión, sin inmovilizar |
| 8 | Documento de transporte | Sistema contable como único emisor |
| 9 | Puntos de cliente | Geocercas virtuales, nada instalado |
| 13 y 14 | Operación de 36 meses | Servicios administrados y costo de operación declarado |

*Fuente: Caso, capítulo 10, pp. 23 y 24.*

La agrupación muestra que tres restricciones, la 2, la 3 y la 7, juntas producen la decisión más
importante del caso: la compañía responde por una jornada que no controla, sobre conductores a los que
no puede dar órdenes y en camiones cuyos equipos no puede tocar. La sección 3.3.2
desarrolla esa decisión. Las restricciones 5, 10 y 11 fijan el ritmo físico del proyecto y no se pueden acelerar con
más personas.

### 3.2.8 Catálogo priorizado de requerimientos

El Caso no trae requerimientos y exige construirlos desde el texto, con su origen verificable
(Caso, numeral 17.1, p. 38). audIT recorrió los capítulos 4 a 18 del Caso y produjo 42 requerimientos: 28
funcionales, RF-001 a RF-028, y 14 no funcionales, RNF-001 a RNF-014. Cada uno lleva en el Formulario
T-12 su descripción, actor, precondición, resultado esperado, prioridad, origen, componente, paquete de
trabajo y prueba de verificación, y los no funcionales además su categoría, umbral numérico, método de
verificación y a quién son exigibles. La Tabla 3.8 resume el catálogo por contexto.

**Tabla 3.8.** Requerimientos por contexto de la arquitectura y por etapa

| Contexto | RF | RNF | Etapa 1 | Etapa 2 |
|---|---|---|---|---|
| Personas y cumplimiento | 7 | 2 | 9 | 0 |
| Flota y activos | 3 | 2 | 3 | 2 |
| Planificación y tráfico | 3 | 0 | 2 | 1 |
| Telemetría y geocercas | 4 | 5 | 8 | 1 |
| Operación de fletes | 5 | 1 | 6 | 0 |
| Liquidación y costeo | 6 | 0 | 4 | 2 |
| Plataforma transversal | 0 | 4 | 4 | 0 |
| Total | 28 | 14 | 36 | 6 |

*Fuente: Formulario T-12. Plataforma transversal agrupa la capa anticorrupción y la operación del servicio.*

La concentración en Personas y cumplimiento, Telemetría y geocercas, y Operación de fletes refleja dónde
está el problema: la jornada, el viaje real y la evidencia. Los catorce no funcionales se concentran en
Telemetría y geocercas porque el equipo a bordo carga con las restricciones más duras: cero interacción en
marcha, 72 horas sin enlace y ninguna intervención sobre equipos ajenos. La prioridad tiene tres niveles
con un criterio declarado. Prioridad 1 es todo requerimiento cuya falla deja salir un camión que no debía
o pierde una prueba: 16 de los 42. Prioridad 2 es todo el que sostiene un criterio de aceptación o una
restricción del Caso: 24. Prioridad 3 es el que optimiza sobre datos que ya existen: la asignación de
retornos y la explicación de la dispersión de rendimiento. La prioridad ordena la construcción y la
prueba, no la opcionalidad: los 42 están comprometidos.

La clasificación entre funcional y no funcional no es indiferente, porque decide quién verifica, cómo
y cuándo (Caso, numeral 17.2, p. 39). audIT aplica un criterio único. Es funcional lo que cambia el
resultado de una transacción que una persona puede observar: la asignación se bloquea, el documento se
emite, la alerta llega. Es no funcional lo que restringe a todas las transacciones por igual y se
verifica con un umbral medido: cero interacción en marcha, 72 horas sin pérdida, integridad de la
evidencia. Con ese criterio, la verificación bloqueante es funcional (RF-001) y su tiempo de 30
segundos es un umbral de desempeño, la operación de 72 horas es no funcional (RNF-002) y su contenido,
qué se registra sin enlace, es funcional (RF-009). El Formulario T-12 aplica el mismo criterio a los
seis casos limítrofes que plantea el Caso.

La Figura 3.2 sigue un requerimiento de extremo a extremo para mostrar cómo se lee la cadena que
el Caso, numeral 17.1, p. 38 exige: origen, requerimiento, componente, paquete de trabajo, prueba y
criterio de aceptación.

**Figura 3.2. Cadena de trazabilidad del requerimiento RF-003, jornada previa del conductor externo**

Fuente: elaboración propia sobre el Caso, numeral 4.3 y capítulo 18, y la trazabilidad RF-003 del Formulario T-12.

[Consultar diagrama en el PDF](AUDIT-Subdocumento3.pdf).

La cadena se lee en el sentido de las flechas. Arriba, el requerimiento nace de un párrafo del Caso y de
una de las decisiones que el Caso deja abiertas, y se asigna a un único contexto de la arquitectura. Abajo, el contexto se
construye en un paquete de trabajo del Subdocumento 7, se prueba con los casos del Subdocumento 9 y se
acepta contra el criterio 3. El paquete EDT 9.2 aparece porque este requerimiento no se cumple sólo con
software: sin el anexo de adhesión firmado no hay acceso a la jornada previa. El Formulario T-12 trae
la misma cadena para los 42 requerimientos, y cuatro reglas la controlan: todo problema del Capítulo 2
tiene requerimiento, exclusión o supuesto, todo requerimiento tiene origen, componente, paquete y
prueba, todo criterio de aceptación tiene al menos un requerimiento, y ningún contexto carece de un
requerimiento que lo justifique.

### 3.2.9 Reglas de negocio

El Caso pide registrar las reglas propias del transporte que la solución debe respetar y que el
documento no explicita (Caso, numeral 17.1, p. 38). audIT registra doce. Una regla no es un requerimiento:
el requerimiento dice qué hace la solución, la regla dice con qué criterio lo decide y quién puede
cambiar ese criterio. La Tabla 3.9 resume las doce y el Formulario T-12 trae su enunciado
completo.

**Tabla 3.9.** Reglas de negocio, fuente y responsable de su cambio

| ID | Regla | Fuente | Cambia |
|---|---|---|---|
| RN-01 | Cómputo de la jornada | Art. 25 bis | Prevención |
| RN-02 | Distinción entre conducir, esperar y descansar | Diseño audIT | Prevención |
| RN-03 | Veredicto según nivel de evidencia | Decisión 1 del 16.1 | Comité Ejecutivo |
| RN-04 | Excepción al bloqueo | Decisión 6 del 16.1 | Comité Ejecutivo |
| RN-05 | Aptitud del equipo para la carga | DS 298 y contratos | Control de flota |
| RN-06 | Prelación en la asignación | Diseño audIT | Operaciones |
| RN-07 | Tiempo libre de espera | Contrato de cada cliente | Comercial |
| RN-08 | Base de la liquidación a terceros | Anexo de adhesión | Finanzas |
| RN-09 | Asignación del retorno | Decisión 14 del 16.1 | Operaciones |
| RN-10 | Ventana de transmisión y revocación | Ley 21.719 | Comité Ejecutivo |
| RN-11 | Documento de transporte antes del movimiento | Restricción 8 | Finanzas |
| RN-12 | Escalonamiento de vencimientos | RT-16.21 del Caso | Prevención |

*Fuente: elaboración propia. Art. 25 bis del Código del Trabajo, DS 298 y Ley 21.719, citados en el texto.*

Tres reglas merecen explicación en el cuerpo porque deciden si un camión sale. La regla RN-01 aplica el
régimen especial del conductor de carga interurbana: no más de cinco horas de conducción continua,
seguidas de un descanso de al menos dos horas, un descanso de ocho horas ininterrumpidas en cada
veinticuatro y un tope de 180 horas mensuales (Ministerio del Trabajo, 2003). Lo que la ley no dice, y
la regla RN-02 fija, es cómo se distingue conducir de esperar: el equipo a bordo cuenta conducción cuando
el camión se mueve fuera de una geocerca de punto de cliente, y espera cuando está detenido dentro de
ella. Los umbrales de velocidad y de tiempo que separan ambos estados se calibran en la marcha blanca
contra el tacógrafo de los camiones que lo tienen.

La regla RN-04 responde a la decisión 6 del numeral 16.1: qué pasa cuando el bloqueo detiene un viaje
comprometido. Ninguna causa legal admite excepción: jornada agotada, licencia vencida o carga peligrosa
mal documentada bloquean siempre. La excepción existe sólo cuando el bloqueo se debe a que una fuente de
dato no responde, la autorizan dos personas con rol nominado, el jefe de turno de la torre y prevención
de riesgos, vale para un viaje, queda registrada con motivo y se revisa en el comité mensual. Sin regla
de excepción, la primera vez que el bloqueo detenga un viaje alguien lo saltará por fuera
(Caso, numeral 16.1, p. 34). La regla RN-10 decide qué ve el mandante de un camión ajeno, y la sección 3.4.3
la explica junto con el plan de adhesión.

### 3.2.10 Criterios formales de aceptación del alcance

El Caso fija 29 resultados de negocio y pide comprometerse con ellos, proponer la meta cuando el Caso no
la fija, indicar en qué mes se alcanza cada uno y cómo se mide (Caso, capítulo 18, p. 41). Los 29 tienen
meta, mes y medición en el Formulario T-12. audIT los clasifica en tres clases, porque un umbral
ofrecido como si fuera exigencia del Caso confunde la evaluación, y uno fijado sin línea base se
incumple después. La Tabla 3.10 muestra la distribución.

**Tabla 3.10.** Clases de criterios de aceptación y mes en que se alcanzan

| Clase | Criterios | Total | Mes |
|---|---|---|---|
| Resultado del Caso | 1, 2, 3, 4, 5, 6, 8, 9, 12, 13, 14, 17, 19, 21, 22, 25, 26, 29 | 18 | 6 a 21 |
| Meta propuesta por audIT | 11, 15, 16, 18, 20, 23, 24, 27 | 8 | 16 a 33 |
| Parámetro fijado en la Etapa 1 | 7, 10, 28 | 3 | 12 |

*Fuente: Caso, capítulo 18, pp. 41 a 43 y Formulario T-12.*

La primera clase reúne los resultados que el Caso ya define y que se cumplen o no, como que ningún camión
salga sin jornada disponible. La segunda reúne los que el Caso deja sin cifra y audIT la fija: las
objeciones a los cobros por espera bajan del 71 % a menos del 20 % de los cobros respaldados, la
liquidación pasa de nueve días a uno con menos del 1 % corregido, que es la referencia del
Caso, numeral 7.3, p. 16, y la revocación de un consentimiento surte efecto en no más de cinco minutos. La
tercera reúne tres valores que no pueden fijarse antes de medir, como la anticipación de la alerta de
jornada, que depende de la distancia a los lugares seguros de detención que la Etapa 1 levanta: para
ellos audIT compromete el mes y el método con que quedan fijados, no un número inventado.

Los criterios 27, 28 y 29 son los que el Caso declara decisivos (Caso, capítulo 18, p. 43). El criterio 27,
adhesión, tiene metas de 104 de los 148 transportistas al cierre de la Etapa 1, el 70 %, y de 134 al
cierre de la Etapa 2, el 90 %. El 28, alerta con lugar seguro, se cumple cuando toda alerta indica un
lugar de detención alcanzable antes de agotar la jornada. El 29, que el dueño del camión vea y decida,
está en producción desde el mes 16 porque el consentimiento debe existir antes de capturar un solo dato
de un camión ajeno.

> **Compromiso C-02.** audIT conduce con el mandante la campaña de adhesión desde el mes 1 y aplica las medidas de refuerzo de la sección 3.4.3 si en el mes 9 la adhesión firmada es inferior al 40 %.
>
> Métrica: 104 de 148 transportistas con anexo firmado en el mes 16 y 134 en el mes 21. Se verifica en: Criterio de aceptación 27, registro de adhesión del contexto Flota y activos. Fuente: Caso, capítulo 18, p. 43.

## 3.3 Esquema de solución

El esquema muestra la solución como la verá quien la usa: quién entra por qué canal, qué decide cada
parte y con qué sistemas existentes convive. Es el modelo conceptual que la arquitectura lógica del
Subdocumento 4 desarrolla capa por capa, y usa sus mismos nombres. La Figura 3.3 presenta la vista
general y las secciones siguientes la recorren por partes.

**Figura 3.3. Esquema conceptual de la solución: usuarios, canales, los seis contextos, integración, borde y sistemas que se conservan**

Fuente: elaboración propia sobre las necesidades y restricciones del Caso, capítulos 4, 5 y 10, y los contextos de la sección 4.1 del Subdocumento 4.

[Consultar diagrama en el PDF](AUDIT-Subdocumento3.pdf).

La figura se lee de arriba hacia abajo. Arriba están los cinco grupos de usuarios con su volumen. Los
conductores y los transportistas son la mayoría y no son trabajadores de la compañía, y por eso su canal
es una aplicación que no exige interacción en marcha y un portal donde el transportista controla sus
datos. Al centro están los seis contextos, cada uno con la pregunta que responde. Abajo están el borde,
que mantiene la operación cuando cae el enlace, y los sistemas que la solución no reemplaza o retira
gradualmente. Seguridad y observabilidad no se dibujan como caja porque atraviesan todas las capas, como
explica la sección ?.

### 3.3.1 Los seis contextos y lo que decide cada uno

Los servicios de negocio se dividen en seis contextos delimitados, cada uno con su lenguaje y sus datos.
Un contexto no consulta la base de otro, le pregunta. La división sigue las decisiones del negocio y no
las pantallas, y por eso reproduce la separación que el sistema de 2013 no tiene. Planificación y
tráfico decide qué carga se mueve, hacia dónde y con qué camión, y es quien emite la asignación.
Flota y activos decide si un tractocamión y un semirremolque pueden salir hoy: revisión técnica,
permisos, mantenimiento y aptitud para la carga, y además registra en qué modalidad adhirió cada camión
de un tercero. Personas y cumplimiento decide si una persona puede conducir hoy: licencia, cursos,
expediente de jornada, nivel de evidencia y consentimientos.

Los otros tres miran el viaje en curso y su cierre. Telemetría y geocercas sabe dónde está cada camión y
cuándo llegó a cada punto, unificando los 182 equipos audIT y las plataformas de terceros. Operación de
fletes reconstruye el viaje que realmente ocurrió: documento de transporte, tiempos, conformidad de
entrega y carga peligrosa. Liquidación y costeo calcula cuánto costó cada viaje y cuánto se paga a cada
transportista. Al asignar, Planificación y tráfico pregunta a Personas y cumplimiento y a Flota y activos,
y si cualquiera responde que no, el viaje no sale. Ese diálogo cabe en el presupuesto de 30 segundos que
la sección ? reparte paso a paso.

### 3.3.2 Evidencia de jornada y veredicto de asignación

La pieza más delicada del esquema es cómo se obtiene la jornada de un conductor que no es trabajador de
la compañía. El mandante no necesita saber dónde estuvo ni para quién manejó. Necesita un veredicto al
asignar, apto o no apto, y poder acreditar después que lo verificó. La Figura 3.4 muestra las
seis fuentes ordenadas por su valor probatorio y cómo se convierten en uno de tres resultados.

**Figura 3.4. Cascada de fuentes de jornada y veredicto de la asignación**

Fuente: elaboración propia sobre el Caso, numeral 4.3, restricciones de jornada del capítulo 10 y criterio 2 del capítulo 18. Los niveles probatorios son decisiones de esta propuesta.

[Consultar diagrama en el PDF](AUDIT-Subdocumento3.pdf).

La figura se recorre de arriba hacia abajo y de izquierda a derecha. Los niveles 1 a 4 son evidencia
instrumental: un tacógrafo descargado, el equipo a bordo que identifica al conductor con su tarjeta, la
telemetría de fábrica o la señal de reposo del camión, que dice que el vehículo no se movió sin decir
dónde estuvo. Con cualquiera de ellos se asigna. El nivel 5 es la atestación: al aceptar el viaje, el
transportista firma electrónicamente que el conductor designado cumplió su descanso
(Congreso Nacional de Chile, 2002). Con ella se asigna, pero el viaje queda marcado y la responsabilidad registrada.
Sin ninguna fuente, la ausencia de dato se trata como evidencia negativa y no como dato neutro: el
viaje se bloquea.

La brecha que queda se declara en lugar de disimularla. Un conductor que manejó otro camión, de otra
empresa y sin equipo, no deja rastro instrumental. Esa situación se cierra por responsabilidad
contractual del dueño del camión, que es quien tiene contrato con el mandante, y no por tecnología. Ése
es el fundamento de trasladar la obligación de acreditar la jornada desde el conductor, a quien nada
puede exigírsele por la vía laboral, al transportista (Caso, capítulo 10, restricción 2, p. 23).

### 3.3.3 Atributos de calidad que el esquema resuelve

El esquema responde a cinco atributos que el Informe 1 no analizó: interoperabilidad, escalabilidad,
seguridad, desempeño y disponibilidad. La Tabla 3.11 muestra, para cada uno, el dato del Caso
que lo dimensiona y la parte del esquema que lo atiende.

**Tabla 3.11.** Atributos de calidad, dato que los dimensiona y respuesta del esquema

| Atributo | Dato del Caso | Respuesta del esquema |
|---|---|---|
| Interoperabilidad | Tres plataformas de posicionamiento, una sin exportación | Ingesta por plataforma y estándar de homologación |
| Escalabilidad | De 374 a 430 camiones y un sexto terminal | Contextos con despliegue independiente y alta por parámetro |
| Seguridad | 258 conductores externos con datos de localización | Cifrado de campo, consentimiento y registro de cada consulta |
| Desempeño | Asignación en 30 s y documento en 90 s | Diálogo entre tres contextos con datos en memoria |
| Disponibilidad | Tramos de más de 80 km sin señal y cierres de 12 días | Borde autónomo y sincronización en 20 minutos |

*Fuente: Caso, numeral 14.1, p. 29, Caso, capítulo 15, pp. 31 y 32 y Caso, capítulo 10, p. 23.*

Ninguno de los cinco se resuelve agregando capacidad de nube. La interoperabilidad depende de lo que
cada proveedor acepte exponer, y por eso su factibilidad es una actividad de los meses 1 a 4 y no un
supuesto. La disponibilidad depende del borde: el camión, el terminal y San Bernardo siguen operando
cuando cae el enlace, y la nube recibe todo al volver. La seguridad depende del consentimiento, que es
la condición que puso el dueño de camión entrevistado y sin la cual no habrá dato (Caso, capítulo
18, p. 43).

## 3.4 Explicación de la Solución

Esta sección explica la solución desde el negocio. Muestra que responde a cada problema del Capítulo 2,
recorre un viaje completo, explica la estrategia con los grupos de interés de la sección 2.4 y resume
cómo se implementa, se implanta y se opera. Termina con la correspondencia uno a uno entre el esquema y la
arquitectura lógica.

### 3.4.1 Coherencia con el problema del Capítulo 2

El Subdocumento 2 identificó los problemas que el Caso describe y los dimensionó. La Tabla 3.12
cruza los ocho principales con la capacidad que los resuelve y el criterio que lo verifica.

**Tabla 3.12.** Problema del Capítulo 2, capacidad que lo resuelve y criterio que lo verifica

| Problema | Capacidad | Requerimientos | Criterio |
|---|---|---|---|
| Jornada de 258 conductores externos sin control | E1-02 | RF-002, RF-003 | 2 y 3 |
| Asignación sin verificación previa | E1-03 | RF-001 | 1 |
| 6.000 vigencias en cuatro planillas | E1-01 | RF-005 | 5 |
| 71 % de los cobros por espera objetados | E1-06 | RF-010, RF-011 | 10 y 11 |
| Documento de transporte redigitado | E1-05 | RF-013, RF-014 | 13 y 14 |
| Costo asignado por ingreso y no por ruta | E1-08 | RF-016, RF-017 | 16, 17 y 19 |
| Liquidación de nueve días con 11 % corregido | E1-08 | RF-019, RF-020 | 20 y 21 |
| 26 % de kilómetros en vacío | E2-02 | RF-015 | 15 |

*Fuente: Subdocumento 2, sección 2.3, y Caso, numeral 7.3, pp. 15 y 16.*

Siete de los ocho problemas se resuelven en la Etapa 1. El que queda para la Etapa 2, los kilómetros en
vacío, depende de conocer primero dónde termina realmente cada viaje, que es un dato de la Etapa 1. La
tabla confirma el orden de la sección 3.2.1 desde el lado del problema: lo que la Etapa 1 no resuelve
no puede resolverse antes.

### 3.4.2 Funcionamiento de un viaje

Un viaje recorre los seis contextos en ocho pasos. La Figura 3.5 los muestra con el contexto que
actúa en cada uno y el umbral que lo gobierna.

**Figura 3.5. Ocho pasos de un viaje con el contexto que actúa y su umbral**

Fuente: elaboración propia sobre el Caso, capítulos 4 y 10, y el catálogo de requerimientos del Formulario T-12.

[Consultar diagrama en el PDF](AUDIT-Subdocumento3.pdf).

La fila superior es el despacho y la inferior el cierre. En el paso 1 la orden nace en Planificación y
tráfico, que hasta el mes 21 la recibe del sistema de 2013 a través de la capa anticorrupción. En el paso
2 la asignación pregunta a Personas y cumplimiento por la jornada y las habilitaciones del conductor, y a
Flota y activos por la aptitud del tractocamión y del semirremolque. Si alguno responde que no, el viaje
no sale. En el paso 3 Operación de fletes arma los datos del documento de transporte desde la orden y el
sistema contable lo emite, sin redigitar `RF-013`. El camión no inicia el movimiento sin el folio
emitido, regla RN-11.

En el paso 4 el equipo a bordo registra posición, conducción y eventos, y los transmite con cobertura o
los guarda hasta 72 horas sin ella `RF-009`. En el paso 5 la llegada y la salida en el punto del
cliente se registran por geocerca virtual, sin que el conductor haga nada y sin instalar equipos en un
recinto ajeno `RF-010`. Ese registro sellado es la evidencia que sostiene el cobro por espera según
la regla RN-07. En el paso 6 el destinatario firma la conformidad en la aplicación, y el documento queda
disponible el mismo día `RF-012`. En los pasos 7 y 8 el viaje cerrado entra al costo con los
componentes disponibles y la indicación de los que faltan, como el combustible que llega con hasta 40 días
de desfase (Caso, RT-05.29, p. 32), y alimenta la liquidación mensual del transportista `RF-019`.

La emisión del documento en un punto de carga sin cobertura es la decisión 9 del numeral 16.1 y la
restricción 8 no deja margen: el sistema contable es el único emisor. La solución lo resuelve sin que
ningún equipo emita. Si los datos de la carga se conocen al asignar, el documento se emite antes de que
el camión entre a la zona sin señal y viaja con su folio en el equipo. Si sólo se conocen en el punto, el
equipo audIT envía el conjunto mínimo de datos por su enlace satelital de mensajes cortos, de hasta 340
bytes (Iridium Communications, 2024), el sistema contable emite y el folio vuelve por el mismo canal. Los
puntos de carga sin cobertura los identifica la caracterización en terreno de los meses 1 a 3, y la regla
RN-06 asigna esos viajes a camiones con equipo audIT cuando los datos de la carga no se conocen antes.

**Decisión D-03. Documento de transporte en un punto de carga sin cobertura**

| Se decide | Se descarta | Criterio | Fuente |
|---|---|---|---|
| Emisión anticipada desde la orden, o emisión por el sistema contable con datos enviados por enlace satelital, con el folio de vuelta antes del movimiento | Folios preasignados al equipo a bordo o al terminal, que convierten a ese equipo en emisor | Restricción 8: el sistema contable es el único emisor. Ningún equipo del Formulario T-11 emite documentos | Caso, capítulo 10, restricción 8, p. 24 y decisión 9 del Caso, numeral 16.1, p. 35 |

### 3.4.3 Estrategia con los grupos de interés y plan de adhesión

El Subdocumento 2 mapeó trece actores con su influencia e interés. El Caso advierte que una propuesta que
instale un dispositivo en toda la flota sin explicar quién se lo pide a 148 dueños de camión, quién lo
paga y qué se les ofrece a cambio, será superada por una más modesta que traiga esa conversación resuelta
(Caso, capítulo 19, p. 44). Por eso el plan de adhesión es el centro de la estrategia, y los demás actores se
abordan después.

A los transportistas se les piden tres cosas, y el equipo no es la primera: autorización de acceso a la
jornada de sus conductores para los viajes de la compañía, consentimiento de tratamiento de posición
acotado a la ventana del viaje asignado, y aceptación del equipo en comodato sólo para quien elige la
modalidad completa. A cambio se les ofrece lo que ellos mismos reclamaron en el levantamiento: ver su
liquidación en curso en vez de enterarse nueve días después del cierre, una liquidación calculada desde
la evidencia del viaje que deja la corrección como excepción, una participación declarada en el cobro
por espera que su propia evidencia permita sostener, preferencia en la asignación de retornos dentro de
lo que permita el contrato vigente, y un expediente verificable de su propio cumplimiento que puede
presentar a sus otros clientes, que es la innovación 1 del Subdocumento 13.

El instrumento es un anexo al contrato de transporte vigente y no un contrato nuevo, para no reabrir la
negociación comercial con 148 contrapartes. Regula el acceso a la jornada, el alcance y la revocación del
consentimiento, el comodato, el reparto de la espera recuperada y las causales de término. El equipo lo
adquiere el mandante (Caso, capítulo 11, p. 24), queda en comodato mientras dure la relación comercial, se
instala y se retira en el paso normal por terminal sin costo para el transportista, y su régimen de daño
distingue uso normal de negligencia. Lo que hace viable la adhesión no es quién paga el equipo sino de
quién son los datos: según la regla RN-10, el equipo sólo transmite dentro de la ventana del viaje
asignado por la compañía, y fuera de ella el firmware no emite posición. La innovación 4 del Subdocumento
13 desarrolla ese diseño.

La Tabla 3.13 corrige un punto que el Informe 1 dejó implícito: el nivel de evidencia real
que habilita cada modalidad.

**Tabla 3.13.** Modalidades de adhesión y nivel de evidencia de jornada que habilitan

| Modalidad | Qué aporta el transportista | Camiones | Evidencia de jornada |
|---|---|---|---|
| Completa | Anexo, consentimiento y equipo audIT en comodato | 34 sin equipo y quien lo pida | Nivel 2 |
| De datos | Anexo, consentimiento y acceso a su plataforma | 192 con equipo propio | Nivel 4 o 5 |
| Sin adhesión | Nada | Quien no firma | Ninguna, bloquea |

*Fuente: elaboración propia sobre la Caso, restricción 3, p. 23 y el Caso, numeral 2.2, p. 6.*

En la modalidad de datos, el equipo del tercero entrega posición pero no identifica al conductor ni sella
el tiempo con integridad. Su aporte es el reposo del camión, nivel 4, y el resto lo cubre la atestación,
nivel 5. Esa modalidad acredita jornada con marca, no con evidencia instrumental, y la torre lo ve así.
Quien quiera subir de nivel pasa a la modalidad completa. Quien no adhiere sigue operando con validación
documental, pero sin atestación firmada su conductor no obtiene veredicto y el viaje no se asigna.

La adhesión se mide cada mes con ocho indicadores: transportistas contactados, anexos firmados, camiones
por modalidad, conductores capacitados, viajes por nivel de evidencia, consultas a la liquidación en curso,
revocaciones y tiempo entre firma y activación. Las metas son 104 transportistas al mes 16 y 134 al mes 21.
Si en el mes 9 la adhesión firmada no llega al 40 %, se activan tres medidas en orden: ampliar el reparto
de la espera recuperada, priorizar los retornos para la flota adherida y extender la modalidad de datos,
que no requiere instalar nada. Lo que no se hace es rebajar el estándar de prueba, porque la compañía
responde por la jornada del conductor que despacha cualquiera sea la tasa de adhesión
(Caso, capítulo 10, restricción 7, p. 24).

Con los demás actores la estrategia sigue la matriz de la sección 2.4 del Subdocumento 2. A los
conductores propios se les capacita en el terminal durante el relevo, que es de madrugada, sin aula y
sobre una interfaz que no exige interacción en marcha (Congreso Nacional de Chile, 2021). A prevención de riesgos se le
entrega la regla de excepción y su revisión mensual, que le da control sin detener la operación. A la
gerencia de finanzas se le entrega el estudio de costo del mes 6. A la autoridad laboral, que investiga el
accidente de febrero, se le ofrece el expediente de jornada como evidencia oponible, y la consulta C-10
sobre el registro electrónico se resuelve en el mes 2. A la aseguradora y al cliente mayor se les entrega
la acreditación de jornada por viaje desde el mes 16. El fondo de inversión recibe los indicadores del
Comité Ejecutivo cada mes.

### 3.4.4 Implementación

La implementación sigue el ciclo de vida del Subdocumento 6: gestión del proyecto con el marco del PMBOK
adaptado y desarrollo con iteraciones de dos semanas. Cada contexto es un servicio que se construye,
prueba y despliega por separado, como exige RT-02.02, de modo que un cambio en la liquidación no obliga a
redesplegar la asignación. El código y la infraestructura viven en un solo repositorio con integración
continua en GitLab, la infraestructura se declara como código con Terraform, y el análisis estático corre
en cada integración. Los cinco ambientes, desarrollo, calidad, preproducción, producción y recuperación,
se levantan desde el mismo código sección ?.

El firmware del equipo a bordo sigue un ciclo propio, porque sólo puede actualizarse cuando el camión pasa
por un terminal (Caso, RT-06.01, p. 32). Cada versión se prueba en un banco con equipos reales y se libera
primero en diez camiones propios de San Bernardo. La telemetría de fábrica y las tres plataformas de
posicionamiento se integran después de su verificación de factibilidad, de modo que una plataforma que
no exporta no bloquea la construcción del resto.

### 3.4.5 Implantación

La implantación respeta las condiciones del Caso, numeral 13.3, p. 27. Nada entra en producción sin haber
convivido con la forma actual de trabajar, ninguna actividad inmoviliza camiones y el despliegue avanza
por proceso, no como un evento único. El montaje a bordo empieza por la flota propia, porque la compañía
puede instruir a sus conductores y el equipo es suyo sin negociación: un piloto de diez camiones en San
Bernardo en el mes 6, julio de 2027, y la flota propia completa en el mes 9. Cada camión pasa por un
terminal cada seis días, unas cinco veces al mes, de modo que el límite no es la frecuencia de paso sino
la dotación de técnicos en el horario de relevo. Los 34 camiones de terceros sin equipo se montan desde el
mes 7, a medida que sus dueños firman la modalidad completa.

El montaje se detiene entre diciembre de 2027 y abril de 2028, los meses 11 a 15, y se reanuda en mayo de
2028. Las metas de planificación son 24 de esos 34 camiones montados al mes 16 y 31 al mes 21, que
corresponden al 70 % y al 90 % de adhesión. De los 226 camiones de terceros, el 22 % pasa por un
terminal menos de una vez al mes, unos 50 camiones (Caso, capítulo 10, restricción 5, p. 23). Para ellos el
plan no supone un paso: mientras no se monten operan en modalidad de datos o documental, y la torre ve su
nivel de evidencia. El Subdocumento 7 declara la cobertura acumulada mes a mes.

La verificación bloqueante se prueba en paralelo antes de bloquear. En los meses 13 y 14 corre sobre todas
las asignaciones sin detener ninguna y registra cuántos viajes habría detenido, por qué motivo y con qué
cliente comprometido. En el mes 15 bloquea efectivamente en la flota propia, con la regla de excepción
activa. En el mes 16 bloquea en toda la flota. Si la marcha blanca muestra un motivo de bloqueo que la
operación no puede absorber, se corrige el dato o la regla antes del paso a producción, nunca se apaga el
bloqueo.

Cada paso a producción ocurre en la segunda quincena del mes, después del cierre mensual de nueve días. La
reversión es posible porque nada se pierde: los documentos de transporte ya emitidos son del sistema
contable y no dependen de la plataforma, y los equipos a bordo conservan lo enviado durante 72 horas para
reenviarlo tras una conmutación (sección ?). La estabilización posterior a cada
paso tiene dotación en los cinco terminales en el horario de relevo, que el Subdocumento 7 dimensiona.

### 3.4.6 Operación

La operación de 36 meses empieza en el mes 21 con atención 24x7x365, porque la flota rueda a toda hora y
todo incidente que impida asignar, emitir un documento o recibir una emergencia tiene severidad máxima
(Caso, RT-21.06, p. 34). El área de tecnología del mandante tiene nueve personas y no puede sostener sola una
plataforma con 182 equipos distribuidos (Caso, capítulo 10, restricción 13, p. 24). audIT opera como servicio
la plataforma, el ciclo de vida del equipo a bordo y la mesa de ayuda, y transfiere al área del mandante la
administración funcional y la primera línea de atención a usuarios internos.

La continuidad tiene dos ejes separados. Si cae la región primaria de nube, la recuperación conmuta a la
región secundaria con un tiempo de recuperación de cuatro horas y una pérdida máxima de quince minutos de
datos. Si cae el enlace, los camiones, los terminales y San Bernardo siguen operando sin la nube
sección ?. La observabilidad correlaciona cada transacción de punta a punta, desde
la asignación en la torre hasta el evento en el camión. El Subdocumento 10 detalla los niveles de
servicio y el Subdocumento 11 los planes de operación.

### 3.4.7 Correspondencia con la arquitectura lógica

El Comunicado 10, capítulo 3 exige que el esquema corresponda al ciento por ciento con la arquitectura
lógica y con los mismos nombres. La Tabla 3.14 cruza cada elemento del esquema con su lugar en el
Subdocumento 4.

**Tabla 3.14.** Correspondencia entre el esquema de solución y la arquitectura lógica

| Elemento del esquema | Capa en 4.1 | Sección del Subdocumento 4 |
|---|---|---|
| Canales de los cinco grupos de usuarios | Presentación | sección ? |
| Los seis contextos | Servicios de negocio | sección ? |
| Capa anticorrupción y sistemas que se conservan | Integración y eventos | sección ? |
| Datos transaccionales, series, evidencia y analítica | Datos | sección ? |
| 182 equipos a bordo y 192 de terceros | Borde, on-premise distribuido | sección ? |
| San Bernardo y gabinetes de terminal | On-premise de sitio | sección ? |

*Fuente: elaboración propia sobre el Subdocumento 4.*

Cada elemento del esquema tiene un lugar en la arquitectura y ninguno queda sin él. Los seis contextos
llevan en ambos subdocumentos el mismo nombre y la misma pregunta. El Formulario T-12 completa la
correspondencia en el detalle: cada uno de los 42 requerimientos nombra el contexto que lo atiende.

## Referencias

Congreso Nacional de Chile. (2002). *Ley N.º 19.799 sobre documentos electrónicos, firma electrónica y servicios de certificación de dicha firma*. Biblioteca del Congreso Nacional de Chile. https://www.bcn.cl/leychile/navegar?idNorma=196640

Congreso Nacional de Chile. (2021). *Ley N.º 21.377 que modifica la Ley de Tránsito para sancionar la conducción manipulando dispositivos de telefonía móvil u otro artefacto electrónico*. Biblioteca del Congreso Nacional de Chile. https://www.bcn.cl/leychile/navegar?idNorma=1166014

Fowler, M. (2004, 29 de junio). *Strangler Fig Application*. https://martinfowler.com/bliki/StranglerFigApplication.html

Iridium Communications. (2024). *Iridium Short Burst Data Service Developers Guide*.

Ministerio del Trabajo. (2003). *Decreto con Fuerza de Ley N.º 1. Texto refundido, coordinado y sistematizado del Código del Trabajo. Artículo 25 bis sobre jornada de choferes de vehículos de carga terrestre interurbana*. Biblioteca del Congreso Nacional de Chile. https://www.bcn.cl/leychile/navegar?idNorma=207436

Transportes Curimón S.A. (2026). *Bases administrativas para la preparación de la propuesta: Licitación Pública Internacional N.º TFEP-01/2026* (Documento FEP01).

Transportes Curimón S.A. (2026). *Bases técnicas del Caso 10, Transporte de Carga: Licitación Pública Internacional N.º TFEP-01/2026* (Documento FEP03).

Transportes Curimón S.A. (2026). *Comunicado 10: Estructura obligatoria de las propuestas preparatorias y técnica final* (Comunicado de la licitación TFEP-01/2026).

## Declaración de uso de IA

Conforme al Comunicado 10, sección 7.2, cada sección de este subdocumento y cada formulario asociado declara la herramienta de inteligencia artificial generativa usada, su finalidad, el nivel de uso en texto y en diagramas según la escala oficial de esa sección, y quién revisó y qué verificó. Esta declaración se consolida en el Formulario A-6.

| Sección | Herramienta | Finalidad del uso | Nivel en texto | Nivel en diagramas | Revisión humana (quién y qué verificó) |
|---|---|---|---|---|---|
| Artículo 46, filas 37 a 52 | Claude Opus 5.5 en Claude Code | Redacción de las respuestas a partir de la revisión del Informe 1 y ubicación de la sección que resuelve cada una | Alto | Ninguno | [nombre y cargo de quien revisó, y qué verificó] |
| Introducción y 3.1 | Claude Opus 5.5 en Claude Code | Redacción inicial del resumen y cálculo de la ubicación de los meses 16 y 21 en el calendario | Alto | Medio | [nombre y cargo de quien revisó, y qué verificó] |
| 3.2 | Claude Opus 5.5 en Claude Code | Redacción inicial del reparto entre etapas, la decisión sobre el sistema de 2013, exclusiones, supuestos, restricciones, catálogo, reglas y criterios, sobre las decisiones tomadas por el equipo | Alto | Medio | [nombre y cargo de quien revisó, y qué verificó] |
| 3.3 | Claude Opus 5.5 en Claude Code | Redacción inicial del texto y diagramas escritos como código TikZ a partir del modelo de seis contextos del Subdocumento 4 | Alto | Medio | [nombre y cargo de quien revisó, y qué verificó] |
| 3.4 | Claude Opus 5.5 en Claude Code | Redacción inicial del funcionamiento del viaje, el plan de adhesión traído del Informe 1, la implementación, la implantación y la operación | Alto | Medio | [nombre y cargo de quien revisó, y qué verificó] |
| Formulario T-12 | Claude Opus 5.5 en Claude Code y Codex | Reescritura del catálogo de 42 requerimientos y conciliación de RF-028 y RN-03 con las modalidades y evidencia de jornada definidas en S3 | Alto | Ninguno | Conciliación y controles documentales automatizados realizados; revisión humana final pendiente. |
