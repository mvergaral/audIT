# Arquitectura Lógica y Física

**Subdocumento N.º 4**

| | |
|---|---|
| Empresa | audIT, Empresa N.º 10 |
| Licitación | Licitación Pública Internacional N.º TFEP-01/2026, Caso 10 Transporte de Carga |
| Proyecto | Plataforma Digital de Misión Crítica para Transporte de Carga |
| Cliente | Transportes Curimón S.A. |
| Instancia | Informe Preparatorio 1, Oferta Técnica Sobre N.º 2 |
| Contenido | Ocho capas, contextos delimitados, emplazamiento, dispositivo a bordo, dimensionamiento, supuestos y diagramas. |
| Fecha | 7 de septiembre de 2026 |

---

## Arquitectura de la solución


### Arquitectura lógica


La solución se organiza en las ocho capas del modelo de referencia, cuya existencia es obligatoria
conforme al numeral 2.1 de las Bases Técnicas Transversales. RT-02.01 exige el diagrama que
identifica cada capa, sus componentes y las interfaces entre ellas, y la descripción se ajusta a
ISO/IEC/IEEE 42010 (ISO, 2022).


**Tabla. Las ocho capas y su contenido en esta solución**

| **Capa** | **Contenido** |
|---|---|
| Presentación | Portal web para 84 clientes y 148 transportistas, aplicación móvil, terminales de torre y taller, pantallas de terreno operables con guantes |
| Borde y exposición | Distribución de contenidos, cortafuegos de aplicación, balanceo y terminación de cifrado. Único punto de entrada público |
| Puerta de enlace | Autenticación, autorización, cuotas, límites de tasa, versionado semántico y catálogo de servicios |
| Servicios de negocio | Seis contextos delimitados con límites explícitos, sin estado y desplegables de forma independiente |
| Integración y eventos | Bus de telemetría, bus transaccional, cola de mensajes fallidos, reintento y deduplicación |
| Datos | Persistencia políglota. Transaccional, series de tiempo, documental inmutable y analítica separadas |
| Seguridad | Identidad, autorización, gestión de secretos, cifrado y auditoría. Transversal a todas las capas |
| Observabilidad | Métricas, registros y trazas correlacionadas, sin puntos ciegos entre nube y terreno |


Ninguna interfaz accede directamente a la base de datos. Una petición desciende atravesando las
seis capas de la pila y la respuesta asciende por el mismo camino. Seguridad y observabilidad no
ocupan un lugar en esa pila, la atraviesan entera.


#### Los seis contextos delimitados


RT-02.02 rechaza toda arquitectura monolítica que no permita desplegar de forma independiente sus
componentes críticos. Los servicios de negocio se organizan en seis contextos, cada uno con su
propio lenguaje y sus propios datos. Un contexto no consulta la base de datos de otro, le pregunta.


**Tabla. Contextos delimitados y la decisión que sostiene cada uno**

| **Contexto** | **Qué decide** |
|---|---|
| Planificación y tráfico | Qué carga hay que mover y hacia dónde |
| Flota y activos | Si el equipo puede salir hoy |
| Personas y cumplimiento | Si la persona puede conducir hoy |
| Telemetría y geocercas | Dónde está el camión y cuándo llegó |
| Operación de fletes | El viaje que realmente ocurrió |
| Liquidación y costeo | Cuánto costó y a quién se paga |


El sistema de gestión de 2013 mezcla los seis, y esa es la razón de fondo por la que conoce el
viaje que se encargó y no conoce el viaje que ocurrió.


#### Convivencia con lo que ya existe


RT-05.20 obliga a aislar mediante una capa anticorrupción las integraciones con sistemas heredados
o de terceros, de modo que un cambio en el sistema externo no propague su modelo al núcleo. Esa
capa sustituye los módulos operativos de 2013, tráfico, despacho, tarifas y liquidación, y
encapsula el sistema contable, que se conserva como único emisor de documentos tributarios.


#### Resiliencia


Los servicios de negocio son sin estado, con el estado de sesión y de proceso en almacenes externos
de alta disponibilidad. Los patrones de RT-02.08 son obligatorios y esta oferta los adopta. Tiempos
límite explícitos en toda llamada remota, cortacircuitos y mamparos para aislar fallas de
integraciones externas, y reintento exponencial con variación aleatoria. La escritura es
idempotente con ventana de deduplicación dimensionada para tolerar la desconexión prolongada en
ruta.


### Arquitectura física


#### Cumplimiento del modelo híbrido


El Artículo 16.1 no admite propuestas exclusivamente en nube ni exclusivamente on-premise. Esta
solución es híbrida en tres planos simultáneos, y la parte on-premise no es decorativa.


**Tabla. Los tres planos de emplazamiento**

| **Plano** | **Contenido** | **Por qué no puede estar en otro lugar** |
|---|---|---|
| Nube | Núcleo transaccional, analítica, portales e integración | Elasticidad hacia 430 camiones y absorción del peak de reconexión |
| On-premise de sitio | Continuidad de la torre en San Bernardo y gabinetes en los cuatro terminales regionales | RT-06.01 del Caso exige gabinete por terminal dimensionado para RT-03.10 |
| On-premise distribuido | 374 dispositivos a bordo | La operación no puede depender de la cobertura móvil |


#### El dispositivo a bordo es infraestructura


RT-06.01 del Caso ordena tratar el dispositivo a bordo como un componente on-premise distribuido en
374 unidades, con su propio ciclo de vida, su mecanismo de actualización remota, su gestión de
seguridad y su plan de reposición, todo ello sujeto a que solo puede intervenirse físicamente
cuando el camión pasa por un terminal.


**Tabla. Especificación del componente a bordo**

| **Elemento** | **Especificación** |
|---|---|
| Almacenamiento no volátil | Mínimo 8 GB en memoria flash industrial con nivelación de desgaste |
| Alimentación | 9 a 32 V desde el sistema del vehículo, con protección de sobretensión y polaridad inversa |
| Condiciones de cabina | Vibración, temperatura extrema del norte, polvo y luz solar directa |
| Grado de protección | Declarado y coherente con el entorno, conforme a RT-08.12 |
| Interfaces de vehículo | CAN y FMS en modo lectura, con descarga remota de tacógrafo |
| Identificación del conductor | Sin manipulación de dispositivo y sin depender de que recuerde una credencial |
| Gestión remota | Inventario, configuración, actualización de firmware, bloqueo y borrado, conforme a RT-03.18 |
| Modo de privacidad | Implementado en el firmware del equipo, no en configuración de servidor |
| Ciclo de vida | Declarado para los 56 meses del contrato, con disponibilidad de repuestos y plan de reposición |
| Repuestos | Diez por ciento del parque instalado, con configuración precargada |


La capacidad de 8 GB no se deriva solo de las 72 horas de RT-03.10. RT-10.05 declara que los
cierres del paso Los Libertadores alcanzan 12 días continuos, es decir 288 horas, y deben
absorberse sin desplazar hitos. Un camión detenido allí sigue obligado a no perder ningún registro.
Especificar capacidad en lugar de duración evita rehacer el cálculo cada vez que cambia la
frecuencia de muestreo o se incorpora un tipo nuevo de evidencia.


#### Dimensionamiento derivado


El numeral 14.2 del Caso exige estimar estos valores y advierte que todo valor entregado sin su
derivación se evalúa como dimensionamiento no realizado.


**Tabla. Volumen acumulado a bordo tras 72 horas sin cobertura**

| **Componente** | **Sin imágenes** | **Con evidencia fotográfica** |
|---|---|---|
| Posición a 30 s en marcha y 5 min detenido | 263 KB | 263 KB |
| Telemetría de motor a una muestra por minuto | 288 KB | 288 KB |
| Eventos discretos | 32 KB | 32 KB |
| Documentos del viaje | 195 KB | 2,6 MB |
| Subtotal | 0,8 MB | 3,2 MB |
| Con factor de seguridad de tres | 2,5 MB | 10 MB |


Los supuestos de esta derivación son propios de audIT y se declaran en la Sección 7. Velocidad
comercial media de 55 kilómetros por hora, 64 bytes por registro de posición, 160 bytes por muestra
de telemetría, 40 KB por documento electrónico de transporte y 300 KB por fotografía comprimida.


**Tabla. Consumo mensual de datos móviles por camión y para la flota**

| **Concepto** | **Cada 10 s** | **Cada 30 s** | **Cada 60 s** |
|---|---|---|---|
| Carga útil por camión | 7,9 MB | 5,3 MB | 4,7 MB |
| Con sobrecarga de protocolo | 20 a 24 MB | 13 a 16 MB | 12 a 14 MB |
| Flota completa de 374 unidades | 8,2 GB | 5,6 GB | 5,0 GB |


De este cálculo se desprende una conclusión que conviene declarar. El costo de datos móviles de
esta flota es marginal. Lo que pesa en un horizonte de 36 meses son los cargos fijos por unidad,
suscripción de plataforma, tarjeta de comunicación, servicio satelital y suscripción por
fabricante, porque todos escalan con las 374 unidades y luego con las 430. La frecuencia de
muestreo recomendada es adaptativa, con diez segundos en maniobra y evento, treinta segundos en
ruta estable y cinco minutos en detención.


#### Emplazamiento en nube


La región primaria es Azure Chile Central, con tres zonas de disponibilidad y residencia de datos
en el país (Microsoft, 2025), lo que satisface RT-03.01 y RT-03.02. El Artículo 16.3 obliga
además a declarar expresamente la región primaria y la región secundaria utilizadas, y esta oferta
lo hace en el eje de recuperación descrito más adelante.

La infraestructura se define como código, versionada en el repositorio del mandante. RT-03.03 no
admite infraestructura creada manualmente por consola. RT-03.07 exige declarar la estrategia de
reversibilidad, y esta oferta la declara. Los contenedores y el motor relacional son portables. Los
servicios de ingesta, mensajería y analítica no lo son sin reescritura, y su esfuerzo de migración
se estima en el registro de decisiones.


#### Emplazamiento on-premise y tipología declarada


El numeral 6.1 transversal define tres tipologías de recinto y obliga a declarar cuál se adopta en
cada sitio, advirtiendo que sobredimensionar se penaliza igual que subdimensionar.


**Tabla. Tipología declarada por sitio**

| **Sitio** | **Tipología** | **Justificación** |
|---|---|---|
| San Bernardo, 26 metros cuadrados | Sala técnica secundaria o de sitio | El núcleo está en nube. Aquí residen la continuidad de la torre, la terminación de enlaces y la custodia de medios |
| Cuatro terminales regionales | Gabinete o borde operacional | Texto expreso de RT-06.01 del Caso |
| 374 camiones | On-premise distribuido | Texto expreso de RT-06.01 del Caso |


La sala actual mide 26 metros cuadrados, se habilitó en 2013, tiene climatización de tipo split,
veinte minutos de alimentación ininterrumpida y acceso por credencial. El propio Caso declara que
no cumple el Capítulo 6 transversal y ordena remediarla o reemplazarla.


**Tabla. Habilitación del recinto de San Bernardo y brecha respecto de la situación actual**

| **Ámbito** | **Especificación** | **Brecha actual** |
|---|---|---|
| Energía | Alimentación ininterrumpida con autonomía mínima de 30 minutos a plena carga | Hoy 20 minutos |
| Energía | Generación autónoma de al menos 24 horas continuas, con estanque dimensionado y contrato de reabastecimiento | No existe |
| Energía | Instalación eléctrica independiente del resto del edificio y puesta a tierra conforme a la normativa chilena vigente | Por verificar |
| Energía | Revisión y medición semestral con informe entregable | No existe |
| Clima | Climatización de precisión redundante en configuración N más uno | Hoy split |
| Clima | Monitoreo en línea de temperatura, humedad y presencia de agua | No existe |
| Incendio | Detección temprana por aspiración de aire con tecnología láser | No existe |
| Incendio | Extinción automática por agente limpio con aprobación UL e instalación conforme a norma (NFPA, 2022) | No existe |
| Acceso | Control biométrico facial con respaldo dactilar y bitácora auditable | Hoy credencial |
| Acceso | Videovigilancia con treinta días en línea | No existe |
| Medios | Custodia en medio físico transportable, con inventario, rotación y verificación de legibilidad | No existe |
| Redes | Acceso a comunicaciones por rutas físicas distintas con ingreso por puntos separados | Por verificar |


RT-06.34 privilegia al proponente que ofrezca especificaciones mejores que las establecidas,
debidamente fundamentadas. audIT propone un agente de extinción de bajo potencial de calentamiento
global en lugar del agente de referencia, y vincula esa elección con la estimación de huella de
carbono que exige RT-15.03.


#### Continuidad y recuperación como ejes separados


**Tabla. Los dos ejes de continuidad**

| **Eje** | **Primario y secundario** | **Fundamento** |
|---|---|---|
| Recuperación ante desastres | Azure Chile Central y una segunda región Azure | RT-07.02 exige distancia suficiente para no compartir el evento de fuerza mayor. Objetivo de recuperación de 4 horas y punto de recuperación de 15 minutos |
| Continuidad operacional | Nube y San Bernardo | RT-21.06 clasifica en severidad máxima todo incidente que impida asignar un viaje, emitir un documento de transporte o recibir un evento de emergencia |


San Bernardo no es el respaldo de la nube. Es el nodo que mantiene viva la operación cuando el
enlace cae. Situar allí el sitio secundario de recuperación incumpliría RT-07.02, porque la sala y
la región primaria comparten cuenca sísmica y sistema eléctrico.


#### Red y enlaces


El enlace entre San Bernardo y la nube es redundante, con caminos físicos y proveedores distintos y
conmutación automática con tiempo declarado, conforme a RT-03.17. Los cuatro terminales regionales
reciben respaldo de enlace, que tres de los cuatro no tienen hoy. Ningún componente de datos es
alcanzable desde internet y el acceso remoto del personal se resuelve con verificación de postura
del dispositivo, sin exponer servicios internos.

La caracterización de la cobertura móvil real de las rutas se ejecuta mediante mediciones en
terreno. El Caso declara de manera expresa que la disponibilidad informada por los operadores no es
un antecedente aceptable para el diseño. Esa campaña es una actividad de la Etapa 1 con costo y
plazo, y produce dos entregables con un solo recorrido. El mapa de sombras georreferenciado y el
catálogo de lugares seguros de detención que el criterio 28 necesita y que hoy nadie posee.


#### Tecnologías de software


Cada producto ofertado se declara con su versión, su fecha de fin de soporte del fabricante y su
plan de actualización para los 56 meses del contrato. RT-03.05 obliga a privilegiar servicios
administrados sobre autoadministrados cuando ello reduzca el riesgo operacional y a justificar cada
excepción. El estilo arquitectónico se justifica con la volumetría del caso y no con la tendencia
del mercado, tal como advierte el numeral 2.3.


#### Desempeño, capacidad y disponibilidad


Los umbrales del numeral 9.1 transversal son exigibles en producción medidos en el percentil 95
sobre la experiencia real de la persona usuaria. El Caso endurece la fila crítica, y en cada fila
prevalece el umbral más exigente. Asignación de un viaje con verificación bloqueante en no más de
30 segundos. Emisión del documento electrónico de transporte en no más de 90 segundos. Transmisión
del evento de botón de emergencia a la torre en no más de 15 segundos con cobertura. Publicación de
la posición al cliente en no más de dos minutos.

RT-09.03 obliga a soportar sin rediseño un crecimiento de al menos tres veces la volumetría inicial
en un horizonte de tres años. La proyección del propio Caso llega a 1,2 veces, de modo que el
requisito transversal es más exigente y esta oferta dimensiona sobre él.

RT-09.05 exige identificar el componente que primero se convertirá en cuello de botella. En esta
operación es la ingesta durante la reconexión masiva. Cientos de unidades que salen de la misma
zona de sombra vuelcan simultáneamente hasta 72 horas de registro contra el mismo punto de entrada.
Se detecta por profundidad de cola y retraso de procesamiento, y se resuelve con particionado,
retroceso aleatorizado y ventana de sincronización escalonada.

La disponibilidad comprometida es de 99,9 por ciento mensual para los servicios críticos, medida
sobre la transacción de negocio de extremo a extremo. Los planes de continuidad y de continuidad de
las tecnologías de información se elaboran conforme a ISO 22301 (ISO, 2019) e ISO/IEC
27031 (ISO, 2011).


#### Funciones no disponibles en modo desconectado


RT-03.13 obliga a declarar qué funciones no estarán disponibles sin enlace y qué procedimiento
manual las suple, y evalúa como observación grave la ausencia de esta declaración.


**Tabla. Disponibilidad de funciones sin enlace y procedimiento supletorio**

| **Función** | **Sin enlace** | **Procedimiento supletorio** |
|---|---|---|
| Registro de posición, jornada y eventos | Disponible | No aplica |
| Evaluación de geocerca de llegada y salida | Disponible | No aplica |
| Alerta de jornada próxima a agotarse | Disponible | No aplica |
| Emisión del documento de transporte | Disponible | No aplica |
| Botón de emergencia | Disponible por satélite en la población de capa 2 | Protocolo telefónico con la torre donde no hay enlace satelital |
| Asignación de un viaje no precargado | No disponible | Autorización de la torre, registrada y reconciliada al recuperar enlace |
| Verificación bloqueante con dato fresco | Parcial, contra copia local | Regla de excepción con rol nominado y registro auditable |
| Consulta de liquidación por el transportista | No disponible | Portal, al recuperar enlace |
| Notificación en tiempo real al cliente | No disponible | Aviso diferido |
| Actualización de firmware del dispositivo | No disponible | Solo en terminal |


### Supuestos y brechas declaradas


El numeral 14.2 del Caso advierte que todo valor entregado sin su derivación se evalúa como
dimensionamiento no realizado. Los supuestos que sostienen las cifras de esta sección se
declaran aquí con su cierre.


#### Supuestos declarados


**Tabla. Supuestos de audIT con su derivación y su cierre**

| **ID** | **Supuesto** | **Valor** | **Cómo se cierra** |
|---|---|---|---|
| S-01 | Velocidad comercial media | 55 km/h | Medición en Etapa 1 |
| S-02 | Horas de marcha dentro de 72 horas calendario | 30 horas | Régimen de descansos del Artículo 25 bis |
| S-03 | Tamaño del registro de posición | 64 bytes | Ajuste con el fabricante seleccionado |
| S-04 | Volumen acumulado a bordo tras 72 horas | 0,8 MB sin imágenes y 3,2 MB con evidencia fotográfica | Derivado en la Sección 4 |
| S-05 | Capacidad de almacenamiento a bordo | Mínimo 8 GB no volátil | Cubre 72 horas y los 12 días de cierre fronterizo |
| S-06 | Consumo mensual de datos por camión | 13 a 16 MB | Campaña de medición |
| S-07 | Consumo agregado de la flota | 5,6 GB mensuales | Derivado de S-06 |
| S-08 | Población que requiere enlace satelital | No estimable hoy | Campaña de medición de cobertura, Etapa 1 |
| S-09 | Composición del parque telemático de terceros | Desconocida | Levantamiento en Etapa 1 y consulta al mandante |
| S-10 | Tarificación satelital por mensaje y no por byte | Modelo de ráfaga corta | Cotización |
| S-11 | Umbral de latencia del botón de emergencia en modo satelital | Por declarar y fundamentar | El requisito limita los 15 segundos al caso con cobertura |
| S-12 | Tipología del recinto de San Bernardo | Sala técnica de sitio | Consulta C-03 |


#### Brechas que esta oferta reconoce


- **La cobertura móvil no se supone.** El Caso declara que la disponibilidad informada
    por los operadores no es un antecedente aceptable para el diseño. Cualquier cifra sobre cuántas
    unidades requieren enlace satelital antes de la medición en terreno sería una invención.
- **El parque telemático de los 226 camiones de terceros no se inventaría.** El Caso
    no entrega marca, modelo, protocolo ni capacidad de almacenamiento de esos equipos. El
    entregable correcto es un estándar mínimo de homologación contra el cual clasificar después
    cada equipo, y el levantamiento es una actividad de Etapa 1 con costo, plazo y dependencia de
    terceros.
- **El conductor que manejó otro camión sin dispositivo no deja rastro
    instrumental.** Esa brecha se cierra por responsabilidad contractual y no por tecnología.
- **El producto satelital evaluado declara 40 horas de almacenamiento**
    (Webfleet Solutions, 2025) frente a las 72 horas exigidas. La especificación de esta oferta fija
    la capacidad mínima en 8 GB precisamente para no depender de ese límite.


### Diagramas de arquitectura


Los diagramas que siguen se presentan en orientación horizontal a página completa. Sus versiones a resolución de trabajo acompañan esta oferta como archivos independientes.


![Arquitectura lógica. Las ocho capas obligatorias del numeral 2.1 transversal](assets/images/LogicaCapas.pdf)

*Figura. Arquitectura lógica. Las ocho capas obligatorias del numeral 2.1 transversal*


![Contextos delimitados del dominio y sistemas con los que convive la solución](assets/images/Contextos.pdf)

*Figura. Contextos delimitados del dominio y sistemas con los que convive la solución*


![Mapa de integraciones. Sistemas internos, fuentes de terreno y contrapartes externas](assets/images/LogicaIntegraciones.pdf)

*Figura. Mapa de integraciones. Sistemas internos, fuentes de terreno y contrapartes externas*


![Arquitectura física general. Nube, sitio de continuidad, gabinetes de terminal y flota](assets/images/Main.pdf)

*Figura. Arquitectura física general. Nube, sitio de continuidad, gabinetes de terminal y flota*


![El camión como componente on-premise distribuido](assets/images/Camion.pdf)

*Figura. El camión como componente on-premise distribuido*


![Separación entre recuperación ante desastres y continuidad operacional en el borde](assets/images/DosEjes.pdf)

*Figura. Separación entre recuperación ante desastres y continuidad operacional en el borde*


![Flujo de un evento de jornada registrado sin cobertura](assets/images/Flujo.pdf)

*Figura. Flujo de un evento de jornada registrado sin cobertura*


![Correspondencia entre capa lógica y emplazamiento físico](assets/images/LogicaEmplazamiento.pdf)

*Figura. Correspondencia entre capa lógica y emplazamiento físico*


## Bibliografía

Dirección del Trabajo. (2009). *Resolución Exenta N.º 1213. Sistema obligatorio de control de asistencia, horas de trabajo y descanso para conductores de vehículos de carga terrestre interurbana*.

Ministerio del Trabajo. (2003). *Decreto con Fuerza de Ley N.º 1. Texto refundido del Código del Trabajo. Artículo 25 bis*. Biblioteca del Congreso Nacional de Chile. https://www.bcn.cl/leychile/navegar?idNorma=207436

Escuela de Informática PUCV. (2026a). *Bases Administrativas. Licitación Pública Internacional N.º TFEP-01/2026* (FEP01.26).

Escuela de Informática PUCV. (2026b). *Bases Técnicas Transversales* (FEP02.26).

Escuela de Informática PUCV. (2026c). *Bases Técnicas del Caso 10. Transporte de Carga* (FEP03.10.26).

FMS Standard. (2025). *Technical Specification rFMS vehicle data version 5.0.0*. https://www.fms-standard.com

Iridium Communications. (2024). *Iridium Short Burst Data Service Developers Guide*.

ISO. (2011). *ISO/IEC 27031*. ISO. (2019). *ISO 22301*. ISO. (2022). *ISO/IEC/IEEE 42010*. ISO. (2023). *ISO 14083*.

Microsoft. (2025). *Azure geographies. Chile Central region*.

Ministerio de Hacienda. (2024). *Ley N.º 21.719 sobre protección y tratamiento de datos personales*.

Ministerio de Transportes. (1995). *Decreto Supremo N.º 298*.

Ministerio del Trabajo. (2006). *Ley N.º 20.123 sobre trabajo en régimen de subcontratación*.

NFPA. (2022). *NFPA 2001*. NIST. (2014). *NIST SP 800-88 Rev. 1*.

Smart Freight Centre. (2023). *GLEC Framework, version 3.0*.

Webfleet Solutions. (2025). *WEBFLEET SAT. Ficha técnica del producto*.
