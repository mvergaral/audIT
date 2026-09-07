# Esquema de Solución y Alcance

**Subdocumento N.º 3**

| | |
|---|---|
| Empresa | audIT, Empresa N.º 10 |
| Licitación | Licitación Pública Internacional N.º TFEP-01/2026. Caso 10 Transporte de Carga |
| Proyecto | Plataforma Digital de Misión Crítica para Transporte de Carga |
| Cliente | Transportes Curimón S.A. |
| Instancia | Informe Preparatorio 1. Oferta Técnica Sobre N.º 2 |
| Contenido | Solución propuesta, alcance de las etapas, exclusiones, catálogo de requerimientos y criterios de aceptación. |
| Versión | 1.0 |
| Fecha | 7 de septiembre de 2026 |
| Lugar | Viña del Mar, Chile |

---

## Esquema de solución y alcance


### Principio rector


El registro operacional de esta empresa no vive en un servidor. Vive en 374 camiones, y la nube es
donde se consolida. De ese enunciado se desprenden las tres decisiones que ordenan la propuesta.


### Decisión primera. El sujeto obligado de la acreditación de jornada


El mandante no necesita saber dónde estuvo un conductor externo ni para quién manejó. Necesita un
veredicto en el momento de asignar, apto o no apto, y necesita poder acreditar después que lo
verificó. Es un dato derivado, no un historial.

La obligación se traslada del conductor, a quien nada puede exigírsele por la vía laboral, al dueño
del camión, que sí mantiene contrato comercial con el mandante. Al aceptar el viaje, el
transportista firma electrónicamente que el conductor designado cuenta con descanso reglamentario.
El dispositivo aporta la evidencia instrumental que contrasta esa declaración, y la identificación
del conductor ocurre sin acción suya.


**Tabla. Cascada de fuentes para el veredicto de jornada**

| **Nivel** | **Fuente** | **Valor probatorio** |
|---|---|---|
| 1 | Tacógrafo digital descargado por la central | Máximo, donde exista |
| 2 | Dispositivo a bordo con identificación del conductor | Evidencia instrumental |
| 3 | Telemetría de fábrica en solo lectura | Complementa |
| 4 | Señal de reposo del activo, sin coordenadas | Contrasta la atestación |
| 5 | Atestación firmada del transportista | Piso contractual universal |
| 0 | Registro portable del conductor, voluntario e incentivado | Beneficio, nunca requisito |


La regla de bloqueo depende de la calidad de la evidencia y no solo de las horas. Con evidencia
instrumental se asigna. Solo con atestación se asigna con marca y responsabilidad registrada. Sin
ninguna fuente se bloquea. La ausencia de datos se trata como evidencia negativa y no como dato
neutro. La excepción la autoriza un rol nominado, con motivo, vigencia y registro auditable.

Queda una brecha que esta oferta declara en lugar de disimularla. El conductor que manejó otro
camión, de otra empresa, sin dispositivo, no deja rastro instrumental alguno. Esa situación se
cierra por responsabilidad contractual y no por tecnología.


### Decisión segunda. La operación no depende de la cobertura móvil


La conectividad se resuelve por capas y no con una única opción para toda la flota.


- **Almacenamiento local en toda unidad intervenida.** El requisito RT-03.10 del Caso
    exige que el dispositivo opere 72 horas continuas sin cobertura móvil registrando posición,
    eventos de conducción y jornada, tiempos en puntos de carga y descarga, y documentos asociados
    al viaje, sin pérdida de ningún registro. Ese requisito está escrito sobre la cobertura móvil,
    de modo que la disponibilidad de enlace satelital no releva de cumplirlo.
- **Celular como portador primario en toda unidad intervenida**, a tasa completa, con
    sincronización diferida y reconciliación determinista al recuperar enlace.
- **Satelital de ráfaga corta en un subconjunto acotado por riesgo**, para posición a
    tasa reducida, botón de emergencia y eventos críticos. La carga útil de esta operación se mide
    en kilobytes por minuto, no en megabits (Iridium Communications, 2024).


La banda ancha satelital para toda la flota se evaluó y se descarta. Cobra ancho de banda que la
operación no usa, consume energía del vehículo y exige montar una antena sobre la cabina, lo que
compromete la restricción que prohíbe afectar la garantía del vehículo. La alternativa descartada
queda registrada en el registro de decisiones de arquitectura conforme a RT-02.04.


### Decisión tercera. Continuidad y recuperación son problemas distintos


El sitio de borde y el sitio secundario de nube no resuelven lo mismo, y confundirlos incumple
RT-07.02, que exige que el secundario esté a distancia suficiente para no verse afectado por el
mismo evento de fuerza mayor. La Sección 4 desarrolla los dos ejes por separado.


### Catálogo de requisitos


El alcance funcional se expresa en 42 requisitos trazables al origen, 28 funcionales y 14 no
funcionales. La tabla siguiente recoge los que definen la solución. El catálogo completo acompaña
esta oferta en el Formulario T-12.


**Tabla. Requisitos que estructuran la solución**

| **ID** | **Exigencia** | **Criterio que satisface** |
|---|---|---|
| RF-001 | Validación bloqueante de jornada, habilitaciones y aptitud antes de asignar | Ningún camión sale sin poder salir |
| RF-003 | Jornada previa del conductor externo disponible al asignar | Decisión primera del Caso |
| RF-008 | Vista única de posición de los 374 camiones | Unifica tres plataformas |
| RF-009 | Registro local de 72 horas y sincronización posterior | Independencia de la cobertura |
| RF-010 | Llegada y salida automáticas en instalaciones de cliente | Origen del 71 por ciento objetado |
| RF-014 | Documento de transporte conforme antes del movimiento, incluso sin cobertura | La emisión diferida no basta |
| RF-022 | Consentimiento granular, revocable y auditable | Criterio 29 |
| RF-026 | Adhesión de transportistas gestionada y medible | Criterio 27 |
| RF-027 | Alerta de jornada según lugar seguro alcanzable | Criterio 28 |
| RNF-001 | Cero interacción del conductor durante la marcha | Restricción 1 |
| RNF-002 | Operación desconectada íntegra e idempotente | RT-03.10 y RT-03.11 |
| RNF-003 | Sin intervención de equipos de terceros sin acuerdo expreso | Restricción 3 |


### Alcance por etapas


El criterio de partición no es de tamaño sino de riesgo. La Etapa 1 controla lo que puede producir
un despacho ilegal, una pérdida probatoria, una duplicación tributaria o un tratamiento indebido de
datos personales, y valida las dependencias técnicas y contractuales antes de comprometer un
despliegue masivo.

El comité expresó un orden de urgencia. Primero seguridad, luego viaje y evidencia, y por último
costo, liquidación y emisiones. El numeral 13.1 del Caso advierte que repetir ese orden sin
analizarlo se evalúa como falta de criterio profesional, y que el mandante contrata ingeniería y no
obediencia (Escuela de Informática PUCV, 2026c). Esta oferta lo altera en un punto y lo mantiene en el
resto.

El costeo por ruta y contrato se adelanta a la Etapa 1, en contra de la tercera prioridad del
comité. El fundamento es un hito externo con fecha, no una preferencia. Dos de los tres contratos
servidos bajo costo se renegocian en 2027, y la Etapa 2 no entra en producción antes del mes
veintiuno según el cronograma obligatorio del Artículo 17 (Escuela de Informática PUCV, 2026a). Dejar el
costo real para la Etapa 2 significa renegociar a ciegas por segunda vez, que es la objeción que la
gerenta de administración y finanzas dejó registrada en el levantamiento. Un contrato servido a
menos catorce por ciento durante cuatro años cuesta más que adelantar el módulo de costeo.

El resto del orden se mantiene por dependencia técnica y no por deferencia. La seguridad va primero
porque el bloqueo de la asignación necesita el registro de vigencias saneado y el expediente de
jornada, y ambos son entradas de todo lo demás. La posición en tiempo real para el cliente no se
adelanta, pese a ser atractiva comercialmente, porque el jefe de control de flota dejó la objeción
correcta. No se puede prometer posición en tiempo real sin resolver antes qué están dispuestos a
compartir ciento cuarenta y ocho dueños de camión, y esa conversación toma meses. Prometerla antes
de la adhesión sería comprometer un dato que no se tiene derecho a capturar. Las emisiones quedan
repartidas, con base metodológica en la Etapa 1 y cálculo productivo en la Etapa 2, porque la
exigencia del cliente exportador es para 2029 y lo que no admite espera es fijar el método, no
producir el número.


**Tabla. Capacidades comprometidas en la Etapa 1**

| **Capacidad** | **Resultado comprometido** |
|---|---|
| Despacho seguro | Validación de jornada, vigencias, aptitud y nivel de evidencia antes de asignar |
| Evidencia y documentos | Registro maestro, trazabilidad e integridad, con pilotos de carga peligrosa y de tacógrafo |
| Posición y operación desconectada | Vista única piloto, geocercas y almacenamiento mínimo de 72 horas |
| Viaje y facturación | Documento conforme antes del movimiento aun sin cobertura, con emisor contable único |
| Costos y liquidación | Costo consolidado dentro de 24 horas con faltantes explícitos, y liquidación por excepción |
| Base de emisiones | Fuentes, línea base y metodología declarada conforme a ISO 14083 y al marco GLEC. No cálculo productivo completo |
| Portales y consentimiento | Portal mínimo, segregación, adhesión y permisos granulares |
| Flota y mantenimiento | Pilotos de kilometraje real y de alerta de lugar seguro |
| Implantación y operación | Pilotos por familia de vehículo, matriz de responsabilidades y despliegue progresivo |


La Etapa 2 escala el despliegue al resto del parque adherido, incorpora la optimización de retornos
para atacar el 26 por ciento de kilómetros en vacío, lleva el cálculo de emisiones a régimen
productivo completo y consolida la adopción de los transportistas.


### Tres poblaciones de camiones, tres tratamientos


La flota no admite un tratamiento único. La restricción 3 establece que los dispositivos instalados
en camiones de terceros pertenecen a sus dueños y no pueden intervenirse, reconfigurarse ni
reemplazarse sin acuerdo expreso.


**Tabla. Tratamiento por población de la flota**

| **Población** | **Unidades** | **Tratamiento** |
|---|---|---|
| Flota propia | 148 | Especificación completa y despliegue directo |
| Terceros con dispositivo | 192 | No se reemplaza nada. Estándar mínimo de homologación y unificación de la vista |
| Terceros sin dispositivo | 34 | Únicos candidatos a equipamiento nuevo, y solo por adhesión |


El entregable para la población intermedia no es un inventario, que el mandante no entregó, sino un
estándar mínimo de homologación contra el cual clasificar después cada equipo. Almacenamiento local
de 72 horas, sincronización diferida, formato de evento, identificación del conductor y sello de
tiempo con garantía de integridad.


### Lo que queda fuera del alcance


El Capítulo 11 del Caso declara con precisión qué no se pide, y esta oferta lo respeta.


- No se reemplaza el sistema contable ni la emisión de documentos tributarios.
- No se interviene la electrónica de fábrica del vehículo.
- No se reemplazan las plataformas de posicionamiento instaladas en camiones de terceros.
    Sí se unifica la vista y se especifica qué se requeriría para homologarlas.
- No se instala infraestructura en los puntos de carga y descarga de los clientes.
- El hardware lo adquiere el mandante. audIT especifica qué comprar, cuánto y con qué
    características.


### Plan de adhesión


El criterio 27 mide si el proponente entendió que la mayor parte de la solución depende de personas
a las que no se les puede dar una orden. El gerente general lo dijo con la pregunta que anunció que
haría a cada oferta. Quién le va a pedir permiso a ciento cuarenta y ocho dueños de camión, y qué
se les va a ofrecer a cambio (Escuela de Informática PUCV, 2026c).


#### Qué se les pide y qué se les ofrece


Se les piden tres cosas, y la instalación del aparato no es la primera. Autorización de acceso a
los registros de jornada de sus conductores, en la medida y por el período necesarios para
acreditar los viajes que ejecuten para el mandante. Consentimiento de tratamiento de posición y
actividad, acotado a la ventana del viaje asignado. Y aceptación del equipamiento a bordo en
régimen de comodato, solo para quienes adhieran en la modalidad completa.

La contraprestación es verificable por el propio transportista, y tres de sus cuatro componentes
resuelven un dolor que él mismo declaró en el levantamiento.


**Tabla. Contraprestación comprometida en el plan de adhesión**

| **Beneficio** | **Situación actual** | **Compromiso** |
|---|---|---|
| Liquidación visible en curso | La conoce nueve días después del cierre | Viajes y liquidación consultables en cualquier momento |
| Menos correcciones posteriores | El once por ciento se corrige tras emitirse | Cálculo desde la evidencia del viaje, con corrección como excepción auditable |
| Reparto de la sobreestadía recuperada | El setenta y uno por ciento de los cobros es objetado por falta de prueba | Participación declarada en el cobro que su propia evidencia permita sostener |
| Prioridad en la asignación de retorno | No existe criterio explícito | Preferencia para la flota adherida dentro de lo que permita el contrato vigente |


#### Régimen del dispositivo


El Capítulo 11 del Caso resuelve la primera mitad de la pregunta y no admite lectura alternativa.
Todo el hardware lo adquiere el mandante, y audIT especifica qué comprar, cuánto y con qué
características. Lo que el Caso deja abierto, en la decisión quinta del numeral 16.1, es de quién
es el dispositivo instalado en un camión de un tercero, quién lo administra y qué ocurre con él si
el transportista deja de trabajar con la compañía (Escuela de Informática PUCV, 2026c).


**Tabla. Régimen del equipo instalado en un camión de tercero**

| **Materia** | **Propuesta** |
|---|---|
| Adquisición y propiedad | Del mandante, conforme al Capítulo 11, para toda la flota |
| Tenencia | Del transportista adherido, en comodato, mientras dure la relación comercial |
| Configuración, instalación y soporte | De audIT, como parte del servicio, durante el paso normal por terminal |
| Retiro | En el primer paso por terminal al término de la relación, sin costo para el transportista |
| Daño o pérdida | Régimen declarado en el anexo de adhesión, que distingue uso normal de negligencia |
| Equipos preexistentes del transportista | No se intervienen. Se homologa la vista, conforme al Capítulo 11 |


Lo que hace viable la adhesión no es quién paga el aparato, sino de quién son los datos. El
transportista entrevistado hizo tres preguntas. Quién lo paga, quién ve esa información y qué pasa
con ella cuando trabaja para otro cliente. La primera la responden las bases. Las otras dos las
responde el diseño, y son las que deciden si adhiere. Por eso la propuesta separa la propiedad del
equipo de la propiedad del dato. El equipo es del mandante, la actividad del transportista sigue
siendo suya, y el dispositivo solo transmite dentro de la ventana del viaje asignado.


#### Instrumento contractual, enrolamiento y capacitación


Un anexo al contrato de transporte vigente, no un contrato nuevo, para no reabrir la negociación
comercial completa con ciento cuarenta y ocho contrapartes. El anexo regula el acceso a registros
de jornada, el alcance y la revocación del consentimiento, el comodato del equipo, el reparto de la
sobreestadía recuperada y las causales de término. Su redacción corresponde al mandante con apoyo
de audIT y requiere validación jurídica antes de su uso.

El enrolamiento sigue el ritmo físico de la operación y no un calendario de escritorio. Un camión
pasa por un terminal cada seis días en promedio, y el veintidós por ciento de la flota
subcontratada pasa menos de una vez al mes, lo que equivale a unas cincuenta unidades sobre las
doscientas veintiséis de terceros. Ese subconjunto fija el límite físico de cualquier meta de
cobertura. La capacitación considera que los conductores no están en un lugar fijo, que doscientos
cincuenta y ocho de ellos no son trabajadores de la compañía y que el relevo en terminal ocurre de
madrugada. Se diseña como instrucción breve en el punto de paso, sin aula y sin material que el
conductor deba conservar, apoyada en que la interfaz a bordo no exige interacción en marcha.


#### Modalidades y tratamiento de quien no adhiere


**Tabla. Modalidades de adhesión**

| **Modalidad** | **Qué aporta el transportista** | **Qué capacidades habilita** |
|---|---|---|
| Completa | Consentimiento, acceso a jornada y equipo en comodato | Todas, incluidas posición durante el servicio y evidencia telemática |
| De datos | Consentimiento y acceso a jornada, homologando su equipo actual | Posición homologada, jornada acreditada, portal y liquidación |
| Sin adhesión | Nada | Validación documental controlada, sin posición ni jornada telemática |


Quien no adhiere sigue operando. Lo que no ocurre es que su nivel de evidencia se presente como
equivalente al de un camión adherido. La vista de la torre distingue de manera visible la cobertura
completa, la homologada, la documental y la no disponible. Esa distinción es lo que impide que el
período de flota mixta genere dos formas paralelas de trabajar que después no se puedan unificar.


#### Cómo se mide y qué ocurre si no alcanza


Ocho indicadores medidos mensualmente desde el primer mes. Transportistas contactados, con anexo
firmado, vehículos enrolados por modalidad, conductores capacitados, viajes con jornada acreditada
por fuente, transportistas que consultan su liquidación en curso, tasa de revocación del
consentimiento y tiempo entre la firma y la activación efectiva.

Las metas comprometidas son setenta por ciento de adhesión al cierre de la Etapa 1, es decir ciento
cuatro de ciento cuarenta y ocho, y noventa por ciento al cierre de la Etapa 2, es decir ciento
treinta y cuatro. La cobertura telemática de la flota es un indicador distinto y no debe
confundirse con el porcentaje de transportistas adheridos, porque cada transportista tiene entre
uno y cuatro camiones.

Si al noveno mes la adhesión firmada es inferior al cuarenta por ciento, se activan tres medidas en
este orden, y las tres están costeadas. Ampliar el reparto de la sobreestadía recuperada, que es el
incentivo con mejor relación entre costo para el mandante y valor percibido por el transportista.
Priorizar la asignación de retornos a la flota adherida. Y extender la modalidad de datos, que no
requiere instalar nada. Lo que no se hace es rebajar el estándar probatorio ni presentar la
validación documental como equivalente a la telemática. La compañía responde por la jornada del
conductor que despacha, sea propio o de un tercero, y esa responsabilidad no cambia con la tasa de
adhesión.


### Criterios de aceptación comprometidos


El Capítulo 18 del Caso fija veintinueve resultados y exige comprometerlos, proponer meta donde no
esté fijada, indicar el hito y declarar cómo se medirá. Los veintinueve están comprometidos. La
oferta distingue tres situaciones y la distinción es deliberada, porque un umbral ofrecido como si
fuera exigencia de las bases confunde la evaluación, y un umbral fijado sin línea base se incumple
después.


- **Resultado obligatorio.** Lo exige el texto de las bases. Se compromete sin condición.
- **Meta de audIT.** El umbral queda a propuesta del oferente. Es oferta comprometida y se declara como propia.
- **Parámetro de la Etapa 1.** El valor no puede fijarse sin levantamiento previo. Se compromete el hito y el método con que quedará fijado, no un número anterior a la medición.


**Tabla. Metas propias de audIT sobre línea base medida**

| **Crit.** | **Línea base** | **Meta comprometida** |
|---|---|---|
| 11 | Setenta y uno por ciento de los cobros por espera objetado | Objeciones bajo el veinte por ciento de los cobros respaldados, en la Etapa 2 |
| 12 | Cuatro coma dos por ciento de respaldos de entrega no llega | Disponible el mismo día, cero conformidades perdidas, en la Etapa 1 |
| 15 | Veintiséis por ciento de kilómetros en vacío | Bajo el dieciocho por ciento en población comparable, en la Etapa 2 |
| 16 | Una planilla construida en junio de 2026 | Noventa y cinco por ciento de viajes con costo trazable, en la Etapa 1 |
| 18 | Diecinueve por ciento de dispersión sin investigar | Modelo reproducible que explique el ochenta por ciento de la variación comparable |
| 20 | Liquidación de nueve días con ocho personas y once por ciento corregido | Un día hábil y bajo dos por ciento de correcciones, en la Etapa 1 |
| 23 | No existe control de datos compartidos | Permisos granulares y revocación efectiva en cinco minutos |
| 27 | No existe conversación de adhesión | Setenta por ciento de adhesión al cierre de la Etapa 1 y noventa por ciento al cierre de la Etapa 2 |


Estas metas se comprometen bajo supuestos que conviene declarar ahora y no ajustar durante la
ejecución. Las de cobertura telemática suponen la frecuencia de paso por terminal declarada en las
bases, y si la frecuencia real es menor se recalculan sobre el ritmo medido. Las de costeo suponen
que un costo consolidado con componentes pendientes explícitos satisface el parámetro RT-05.29,
punto que audIT consultó formalmente. Las de jornada externa y documento tributario suponen valor
probatorio de la evidencia propuesta y existencia de un mecanismo de contingencia soportado por el
sistema contable. Las de vacío y rendimiento se miden sobre población comparable definida en la
Etapa 1. Y todas están dentro del costo total de operación de treinta y seis meses, sin gasto no
presupuestado.


### Trazabilidad y matriz de cumplimiento


La propuesta sostiene una cadena verificable que va del problema al criterio de aceptación. Origen,
requisito, prioridad, etapa, capacidad, componente, método de verificación y criterio. Cuatro
reglas de control gobiernan esa cadena. Todo problema relevante tiene requisito, exclusión o
supuesto asociado. Todo requisito tiene origen, etapa, componente y método de verificación. Todo
criterio de aceptación tiene al menos un requisito. Y ningún componente de la arquitectura carece
de un requisito que lo justifique.

El Formulario T-12 exige declarar el cumplimiento de cada requerimiento de las Bases Técnicas del
Caso y de los requisitos transversales del Capítulo 3 (Escuela de Informática PUCV, 2026a). El Capítulo 3
de las Bases Técnicas Transversales trata del modelo híbrido de nube y on-premise, uno de
veintinueve capítulos, lo que es incompatible con el propósito de una matriz integral de
cumplimiento. audIT consultó esa contradicción dentro del período del Artículo 43 y el Acta de
Respuestas se publica el mismo día de entrega de este informe. Mientras esa respuesta no exista, la
matriz cubre los requisitos del Caso y los requisitos transversales que afectan alcance,
arquitectura, datos e innovaciones, y ninguna de sus filas declara cumplimiento acreditado en esta
instancia. Un compromiso de atender una exigencia y un componente propuesto no son evidencia de
cumplimiento.


### Consultas formuladas al mandante


**Tabla. Consultas presentadas durante el período del Artículo 43**

| **ID** | **Materia** | **Qué desbloquea** |
|---|---|---|
| C-01 | RT-08.10 exige declarar el costo unitario estimado de cada dispositivo dentro de la especificación técnica, y el Artículo 50.2 prohíbe toda cifra de precio en la Oferta Técnica bajo causal de exclusión | Formato de la especificación de implementos |
| C-02 | RT-03.10 exige 72 horas de operación desconectada del dispositivo a bordo, y la restricción 3 impide intervenir los equipos de camiones de terceros sin acuerdo expreso | Alcance real del requisito sobre la flota |
| C-03 | RT-06.01 ordena remediar o reemplazar la sala de San Bernardo sin indicar a qué tipología del numeral 6.1 debe llevarse | Dimensionamiento y costo del recinto |
| C-04 | Instalaciones distintas de San Bernardo con espacio apto para un sitio secundario que satisfaga RT-07.02 | Emplazamiento del sitio secundario |
| C-05 | Posibilidad de ampliar el espacio más allá de los 26 metros cuadrados | Dimensionamiento del recinto |
| C-06 | Existencia de mediciones previas de cobertura móvil | Costo y plazo de la campaña de Etapa 1 |
| C-07 | Composición del parque telemático de los 226 camiones de terceros por proveedor | Estándar de homologación |
| C-08 | Proporción de camiones de terceros con tacógrafo digital | Alcance del programa de tacógrafo |
| C-09 | Identificación de los 18 camiones de carga peligrosa entre propios y de terceros | Población prioritaria de capa satelital |
| C-10 | Existencia de autorización de la Dirección del Trabajo para sustituir la libreta de registro por un medio electrónico (Dirección del Trabajo, 2009) | Hito regulatorio del registro de jornada |
| C-11 | Códigos de requisito citados en el Capítulo 15 del Caso que corresponden a materias distintas en las Bases Técnicas Transversales | Trazabilidad de toda la oferta |


### Contradicciones detectadas entre los documentos de la licitación


El Artículo 43 registra qué proponentes identifican vacíos, contradicciones y riesgos. audIT
consigna las siguientes.


- **RT-08.10 contra Artículo 50.2.** El primero obliga a declarar el costo unitario
    estimado de cada dispositivo de terreno dentro de la especificación técnica. El segundo prohíbe
    toda cifra de precio en la Oferta Técnica bajo causal de exclusión inmediata. Esta oferta
    entrega la especificación sin valorización y remite los costos al Sobre N.º
    3, a la espera de la respuesta a C-01.
- **RT-03.10 contra la restricción 3.** Si las 72 horas de operación desconectada se
    entienden exigibles sobre las 374 unidades, el requisito resulta incumplible por diseño sobre
    el 51 por ciento de la flota, cuyos equipos no pueden intervenirse. Esta oferta lo interpreta
    exigible sobre las unidades intervenidas y somete el resto al estándar de homologación.
- **Códigos del Capítulo 15 del Caso.** Varios códigos citados allí corresponden en
    las Bases Técnicas Transversales a materias distintas de las que el Caso les atribuye, y en
    tres casos el Caso convierte en exigible un requisito que transversalmente es solo deseable.
    Esta oferta cita cada requisito por su texto y su página además de su código.
- **RT-09.03 contra la proyección del propio Caso.** El requisito transversal obliga a
    soportar tres veces la volumetría inicial en tres años. La proyección del Caso llega a 1,2
    veces. Esta oferta dimensiona sobre el umbral más exigente.
- **RT-07.07 contra la ventana operacional protegida.** El primero exige dos
    conmutaciones reales al año para probar el plan de recuperación. RT-10.05 congela diciembre a
    abril, Semana Santa, Fiestas Patrias y los nueve días del cierre mensual. La ventana disponible
    es estrecha y esta oferta la calendariza de manera explícita.


### Materias pendientes al cierre de esta instancia


Esta oferta declara con la misma claridad lo que aún no está cerrado.


**Tabla. Materias pendientes al cierre del Informe 1**

| **Materia** | **Condición de cierre** |
|---|---|
| Fichas T-19 de los tipos 4 y 5 | Requiere resolver la asignación interna de responsabilidad, hoy consignada de forma distinta en dos documentos de trabajo del proponente |
| Estimación de personas usuarias concurrentes internas y externas | Insumo de RT-09.01, derivado de la volumetría del numeral 14.2 |
| Volumen anual de series de posición y de evidencia de jornada | Requiere la política de agregación definitiva |
| Justificación comparada del nivel de redundancia de almacenamiento | RT-03.14 exige compararlo con las alternativas y no solo declararlo |
| Verificación de dos normas chilenas citadas en las bases | Confirmación ante el organismo normalizador antes de citarlas en la oferta definitiva |
| Verificación de las referencias laborales de jornada y registro | Lectura directa de la norma antes de su cita definitiva |


## Bibliografía

Dirección del Trabajo. (2009). *Resolución Exenta N.º 1213. Sistema obligatorio de control de asistencia, horas de trabajo y descanso para conductores de vehículos de carga terrestre interurbana*.

Ministerio del Trabajo. (2003). *Decreto con Fuerza de Ley N.º 1. Texto refundido del Código del Trabajo. Artículo 25 bis*. Biblioteca del Congreso Nacional de Chile. https://www.bcn.cl/leychile/navegar?idNorma=207436

Escuela de Informática PUCV. (2026a). *Bases Administrativas. Licitación Pública Internacional N.º TFEP-01/2026* (FEP01.26).

Escuela de Informática PUCV. (2026b). *Bases Técnicas Transversales* (FEP02.26).

Escuela de Informática PUCV. (2026c). *Bases Técnicas del Caso 10. Transporte de Carga* (FEP03.10.26).

FMS Standard. (2025). *Technical Specification rFMS vehicle data version 5.0.0*. https://www.fms-standard.com

Iridium Communications. (2024). *Iridium Short Burst Data Service Developers Guide*.

ISO. (2011). *ISO/IEC 27031*. ISO. (2013). *ISO 16290. Definition of the Technology Readiness Levels (TRLs) and their criteria of assessment*. ISO. (2019). *ISO 22301*. ISO. (2022). *ISO/IEC/IEEE 42010*. ISO. (2023). *ISO 14083*.

Microsoft. (2025). *Azure geographies. Chile Central region*.

Congreso Nacional de Chile. (2002). *Ley N.º 19.799 sobre documentos electrónicos, firma electrónica y servicios de certificación de dicha firma*. https://www.bcn.cl/leychile/navegar?idNorma=196640

Congreso Nacional de Chile. (2024). *Ley N.º 21.719 que regula la protección y el tratamiento de los datos personales y crea la Agencia de Protección de Datos Personales*. Diario Oficial de 13 de diciembre de 2024. https://www.bcn.cl/leychile/navegar?i=1209272

Ministerio de Transportes. (1995). *Decreto Supremo N.º 298*.

Ministerio del Trabajo. (2006). *Ley N.º 20.123 sobre trabajo en régimen de subcontratación*.

NFPA. (2022). *NFPA 2001*. NIST. (2014). *NIST SP 800-88 Rev. 1*.

Smart Freight Centre. (2023). *GLEC Framework, version 3.0*.

Webfleet Solutions. (2025). *WEBFLEET SAT. Ficha técnica del producto*.

World Wide Web Consortium. (2025). *Verifiable credentials data model v2.0*. W3C Recommendation de 15 de mayo de 2025. https://www.w3.org/TR/vc-data-model-2.0/
