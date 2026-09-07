# Arquitectura Lógica y Física de la Solución

**Subdocumento N.º 4**

| | |
|---|---|
| Empresa | audIT, Empresa N.º 10 |
| Licitación | Licitación Pública Internacional N.º TFEP-01/2026. Caso 10 Transporte de Carga |
| Proyecto | Plataforma Digital de Misión Crítica para Transporte de Carga |
| Cliente | Transportes Curimón S.A. |
| Instancia | Informe Preparatorio 1. Oferta Técnica Sobre N.º 2 |
| Contenido | Arquitectura lógica, física, de integración, de seguridad y de despliegue, con dimensionamiento y decisiones registradas. |
| Versión | 1.0 |
| Fecha | 7 de septiembre de 2026 |
| Lugar | Viña del Mar, Chile |

---

## Arquitectura de la solución


### Arquitectura lógica


#### Punto de partida


El Capítulo 5 del Caso resume el problema en una frase. El sistema de gestión de transporte de 2013
conoce el viaje que la compañía encargó y no conoce el viaje que efectivamente ocurrió, página 13.
El dato existe repartido en tres plataformas de posicionamiento, en una telemetría que nadie
descarga, en una liquidación de combustible que llega con cuarenta días de atraso y en papeles que
viajan en la cabina, y nunca se junta. Esa dispersión no se corrige configurando el sistema
existente, porque nace de cómo está construido.


**Tabla. Rasgos del sistema de 2013 y respuesta de esta arquitectura**

| **Rasgo** | **Efecto que produce hoy** | **Respuesta de esta arquitectura** |
|---|---|---|
| Base única compartida por tráfico, facturación y contabilidad | La consulta de gestión compite con la operación de la torre por el mismo motor | Separación del almacenamiento transaccional y del analítico, obligatoria por RT-05.05 |
| Integración con el sistema contable por consultas y tablas compartidas | Todo cambio contable alcanza el núcleo operacional sin traducción | Capa anticorrupción, obligatoria por RT-05.20 |
| Ausencia de costo por kilómetro por ruta | Tres de los ocho contratos principales se sirven bajo costo, el peor a menos catorce por ciento sostenido durante cuatro años, numeral 7.3 página 15 | Costo por viaje en doble versión, preliminar y consolidada |
| Puerto de telemetría de fábrica inactivo | La lectura del motor de 61 tractocamiones no se aprovecha por temor a la garantía | Acoplamiento sin contacto sobre el arnés original |
| Módulos operativos acoplados entre sí | El sistema no distingue el viaje encargado del viaje ocurrido | Seis contextos delimitados, cada uno con sus propios datos |


#### Las ocho capas


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


**Tabla. Componentes declarados por capa**

| **Capa** | **Componentes** |
|---|---|
| Presentación | Portal web con representación en servidor, aplicación móvil en los cuatro perfiles que exige RT-17.01 del Caso, conductor, torre, terminal y taller, y transportista subcontratado, y vistas de portería y de taller de alto contraste |
| Borde y exposición | Distribución de contenidos con presencia global, cortafuegos de aplicación y protección volumétrica en las capas de red, transporte y aplicación |
| Puerta de enlace | Gestión de interfaces con identidad federada, certificado mutuo entre máquinas, límites de tasa por perfil y catálogo publicado |
| Servicios de negocio | Contenedores orquestados sobre nodos repartidos en tres zonas de disponibilidad, con un despliegue independiente por contexto delimitado |
| Integración y eventos | Flujo de telemetría para la ingesta masiva, bus transaccional con orden garantizado dentro de la partición y cola de mensajes fallidos, y capa anticorrupción frente al sistema contable |
| Datos | Motor relacional multizona, base de series de tiempo, caché en memoria, almacenamiento inmutable y repositorio analítico. El diseño detallado es materia del Subdocumento 5 |
| Seguridad | Bóveda de claves en módulo criptográfico, identidad federada con control por rol y por atributo, y bitácora que permite reconstruir quién, qué, cuándo y con qué valores anteriores, según RT-05.03 |
| Observabilidad | Instrumentación única con trazas, métricas y registros correlacionados por el identificador común que RT-05.19 exige a toda integración |


![Las ocho capas obligatorias del numeral 2.1 transversal, con sus componentes e interfaces, conforme a RT-02.01](LogicaCapas.pdf)

*Figura. Las ocho capas obligatorias del numeral 2.1 transversal, con sus componentes e interfaces, conforme a RT-02.01*


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


#### Registro de decisiones de arquitectura


RT-02.04 y el Artículo 19 convierten el registro de decisiones en entregable contractual, con la
alternativa escogida, las descartadas y el criterio de selección. Se registran cuatro decisiones
estructurales de la arquitectura lógica.


**Tabla. Decisiones de arquitectura lógica registradas**

| **ADR** | **Contexto** | **Decisión** | **Alternativa descartada** | **Criterio** |
|---|---|---|---|---|
| 01 | Cientos de unidades salen a la vez de una misma zona de sombra y vuelcan su registro acumulado mientras la torre despacha | Contenedores orquestados con despliegue independiente por contexto | Monolito modular con escalado vertical | Aislamiento de fallas y escalado independiente. La ingesta no compite por recursos con el despacho |
| 02 | Asignar un viaje dispara notificación, geocerca, costeo preliminar y aviso al cliente | Publicación de eventos de dominio | Cadena síncrona de llamadas entre servicios | Desacoplamiento temporal. El despacho confirma y libera al operador sin esperar los efectos derivados |
| 03 | Finanzas necesita costo por ruta sobre los mismos datos que la torre usa para operar | Captura de cambios hacia el repositorio analítico | Consultas analíticas sobre réplicas de lectura | RT-05.05 prohíbe que la consulta analítica degrade la operación |
| 04 | Conviven 84 clientes, 148 transportistas, terminales y el sistema contable de 2013 | Identidad federada y certificado mutuo entre servicios | Claves de interfaz de larga duración | RT-05.18 prohíbe la clave estática en la ruta de la dirección web |


Estas cuatro son las decisiones estructurales de la capa lógica. El registro completo es entregable
contractual y se actualiza durante toda la ejecución, según ordena el mismo RT-02.04.


#### Degradación, escalamiento y puntos únicos de falla


Tres requisitos obligatorios de la misma sección exigen declaraciones que conviene no dejar
implícitas. RT-02.09 obliga a degradar de forma elegante, de modo que la caída de un componente no
crítico deje la solución operando en modo reducido y avisando de la degradación, y nunca falle de
forma total. La aplicación de esa regla en esta operación es directa. Si el repositorio analítico
no responde, la torre sigue despachando. Si el sistema contable no responde, la operación sigue y
la emisión tributaria se encola. Si el enlace satelital no está disponible, el registro sigue
acumulándose a bordo.

RT-02.10 exige que las capas de aplicación e integración escalen horizontalmente de forma
automática, con umbrales, límites superiores y costo asociado declarados en la oferta. Los umbrales
y los límites se declaran en esta sección. El costo asociado se remite al Sobre N.º
3, porque el Artículo 50.2 excluye toda cifra de precio de la Oferta Técnica.

RT-02.11 evalúa como observación grave omitir la declaración de los puntos únicos de falla que
subsistan. Esta oferta declara dos.


**Tabla. Puntos únicos de falla declarados**

| **Punto** | **Por qué subsiste** | **Por qué es aceptable** |
|---|---|---|
| El sistema contable de 2013 como emisor único de documentos tributarios | La restricción 8 lo fija y no es negociable | La capa anticorrupción aísla su indisponibilidad. La operación no se detiene y la emisión se recupera al restablecerse |
| El dispositivo a bordo de cada camión | Hay uno por unidad y solo puede intervenirse cuando el camión pasa por un terminal, según RT-06.01 del Caso | La falla afecta a una unidad y no a la flota. Se mitiga con repuestos precargados y con el procedimiento supletorio declarado más adelante |


#### Resiliencia


Los servicios de negocio son sin estado, con el estado de sesión y de proceso en almacenes externos
de alta disponibilidad. Los patrones de RT-02.08 son obligatorios y esta oferta los adopta. Tiempos
límite explícitos en toda llamada remota, cortacircuitos y mamparos para aislar fallas de
integraciones externas, y reintento exponencial con variación aleatoria. La escritura es
idempotente con ventana de deduplicación dimensionada para tolerar la desconexión prolongada en
ruta.

El estado de sesión y el estado de proceso residen en almacenes externos de alta disponibilidad,
como exige RT-02.05. Allí viven las sesiones concurrentes de los 22 operadores de la torre, las
credenciales activas y las geocercas de los 1.400 puntos distintos de carga y descarga que declara
el numeral 14.1. Cualquier instancia puede destruirse y reemplazarse sin pérdida de transacciones
en curso.

Los parámetros que siguen son de diseño de audIT y se ajustan con la medición de la Etapa 1.


**Tabla. Parámetros de los patrones de resiliencia**

| **Patrón** | **Parámetro declarado** |
|---|---|
| Cortacircuito | Se abre al superarse la mitad de las llamadas fallidas en una ventana deslizante de diez peticiones, permanece abierto 30 segundos y admite tres llamadas de prueba antes de restablecer el tráfico |
| Mamparo | La verificación bloqueante del despacho tiene su propio conjunto de hilos y de conexiones. La saturación de la consulta de liquidaciones o de reportes no le quita capacidad |
| Tiempo de espera | Validación en memoria, 800 milisegundos. Consulta transaccional del despacho, 5 segundos. Llamada al sistema contable a través de la capa anticorrupción, 10 segundos. Emisión del documento electrónico de transporte, 90 segundos, que es el techo que fija RT-09.01 del Caso |
| Reintento | Tres intentos sobre operaciones idempotentes, con retroceso exponencial y variación aleatoria. La variación evita que cientos de unidades que recuperan cobertura a la vez reintenten sincronizadas |
| Límite de tasa | Declarado por perfil en la puerta de enlace, según se detalla en la gobernanza de interfaces |


#### Verificación bloqueante del despacho


RT-09.01 del Caso fija en 30 segundos el tope para asignar un viaje con verificación de jornada,
habilitaciones y aptitud del equipo. El servicio evalúa tres invariantes en paralelo y ninguna
admite excepción automática.


**Tabla. Invariantes de la verificación bloqueante**

| **Invariante** | **Qué comprueba** | **Fundamento** |
|---|---|---|
| Conductor | Horas conducidas en el día, continuidad sin descanso y acumulado del período | Artículo 25 bis del Código del Trabajo (Ministerio del Trabajo, 2003) |
| Tractocamión | Revisión técnica aprobada, seguro obligatorio vigente y permiso de circulación al día | Numeral 4.4 del Caso |
| Semirremolque y carga peligrosa | Curso vigente del conductor y correspondencia entre la documentación y lo efectivamente cargado | Decreto Supremo N.º 298 (Ministerio de Transportes, 1995) |


La secuencia bloquea la clave de idempotencia, evalúa las tres invariantes en paralelo, persiste en
una única transacción y responde.


**Tabla. Reparto del presupuesto de 30 segundos**

| **Paso** | **Presupuesto** | **Dónde se resuelve** |
|---|---|---|
| Validación del contrato de entrada y bloqueo de la clave de idempotencia | 10 milisegundos | Puerta de enlace y caché en memoria |
| Evaluación paralela de las tres invariantes | 450 milisegundos | Caché en memoria, con respaldo en el motor transaccional |
| Persistencia atómica del viaje asignado | 200 milisegundos | Motor transaccional, aislamiento serializable |
| Publicación de los efectos derivados | Fuera del camino bloqueante | Bus transaccional |
| Total comprometido | Por debajo de 2 segundos | Frente al techo de 30 segundos de RT-09.01 del Caso |


Ante rechazo el sistema responde en menos de un segundo con un documento de error estructurado que
nombra la invariante incumplida, de modo que el operador sepa qué falta y no reintente a ciegas.


**Tabla. Contenido del documento de error ante un despacho rechazado**

| **Campo** | **Contenido** |
|---|---|
| Tipo | Identificador estable de la causal, resoluble a su documentación |
| Título | Enunciado breve de la invariante incumplida |
| Estado | Código que distingue el rechazo por regla de negocio del error técnico |
| Detalle | Valor medido y umbral aplicado, para que el operador sepa cuánto falta |
| Instancia | Identificador del viaje y del intento de asignación, correlacionable con la bitácora |


El presupuesto se cumple con holgura porque la evaluación ocurre sobre datos en memoria. Esa
holgura es deliberada. RT-09.03 obliga a soportar tres veces la volumetría inicial sin rediseño, y
un margen estrecho hoy sería un rediseño mañana.


#### Idempotencia y ventana de deduplicación


RT-02.06 exige escrituras idempotentes. Cada operación lleva una clave única que se retiene durante
siete días, plazo dimensionado para cubrir las 72 horas de desconexión más el margen de los cierres
prolongados del paso fronterizo. La clave se bloquea en el almacén en memoria y se respalda con una
restricción de unicidad duradera en el motor transaccional, de modo que un reintento tras la
reconexión masiva no duplica un viaje ni un documento.

La ventana opera en dos niveles con propósitos distintos. El nivel en memoria resuelve la
concurrencia inmediata. Si la clave ya está tomada y la operación sigue en curso, la petición se
rechaza como conflicto. Si ya se completó, se devuelve la respuesta guardada en lugar de repetir la
escritura. El nivel duradero resuelve el caso que importa aquí, el mensaje que llega desde el búfer
de un camión después de días sin cobertura, cuando la clave ya expiró en memoria. La restricción de
unicidad lo descarta sin importar cuánto tiempo pasó. RT-02.07 exige además deduplicación en el
consumidor y orden garantizado dentro de la partición, y ambos se aplican al flujo de telemetría.


#### Gobernanza de interfaces y contratos


RT-05.16 obliga a documentar los servicios síncronos en OpenAPI 3.1 y los flujos dirigidos por
eventos en AsyncAPI 2.6 o superior, y exige que esa documentación se genere desde el código y se
mantenga actualizada de forma automática. La consecuencia práctica es que no se admite discrepancia
entre el contrato publicado y la implementación viva, porque el contrato no se escribe aparte.

RT-05.17 obliga a versionar semánticamente los contratos, con compatibilidad hacia atrás y política
de obsolescencia con preaviso mínimo de seis meses. RT-05.18 fija el mecanismo de autenticación
entre sistemas y prohíbe la clave estática en la ruta de la dirección web. RT-05.19 exige registrar
la transacción de entrada y la de salida de toda integración con un identificador de correlación
común, que es lo que permite seguir una operación de negocio a través de todos los sistemas que
toca. Ese identificador es el mismo que usa la capa de observabilidad.

RT-05.21 obliga a declarar, por cada integración, el modo, el volumen esperado, la ventana de
disponibilidad de la contraparte y el comportamiento de la solución cuando esa contraparte no
responde. Esa declaración se entrega a continuación.


**Tabla. Declaración por integración conforme a RT-05.21**

| **Contraparte** | **Modo** | **Volumen esperado** | **Ventana de la contraparte** | **Si no responde** |
|---|---|---|---|---|
| Sistema contable de 2013 | Asíncrono | Documentos y asientos de 96.000 viajes al año | Horario administrativo, sin compromiso 24x7 | Cortacircuito y encolado. La operación no se detiene |
| Plataformas de posicionamiento de terceros | Asíncrono | Posición de los camiones de terceros con dispositivo | No declarada por el Caso | Última posición conocida con su antigüedad visible, nunca una posición sin fecha |
| Telemetría de fábrica | Asíncrono | 61 tractocamiones, solo lectura | Sujeta a la autorización de cada fabricante | El viaje se registra igual con el dispositivo a bordo |
| Red de estaciones de servicio | Por lotes | 74.000 abastecimientos al año | Mensual, con hasta 40 días de desfase | El costo se emite preliminar y se marca como pendiente |
| Concesionarias de peaje | Por lotes | 620.000 pasadas al año | Mensual | Peaje estimado por la traza, marcado como estimado |
| Autoridad tributaria | Síncrono | 128.000 documentos al año | Según disponibilidad del servicio | Emisión de contingencia y envío diferido |
| Clientes y autoridad aduanera | Ambos | Según contrato y cruce | Variable | Reintento con retroceso y aviso a la torre |


Los volúmenes de esta tabla provienen del numeral 14.1 del Caso, página 29. La ventana de
disponibilidad de las plataformas de terceros y de la autoridad tributaria no está declarada en las
bases y se consulta al mandante.

RT-05.22 exige además carga y descarga masiva en formatos abiertos, con validación previa, informe
de errores por registro y procesamiento parcial. Esa capacidad es la que sostiene la migración de
las cerca de 6.000 vigencias y la ingesta mensual de combustible y peajes.


#### Convivencia con el sistema contable heredado


La capa anticorrupción sustituye los módulos operativos de 2013, tráfico, despacho, tarifas y
liquidación, y encapsula el sistema contable, que se conserva como único emisor de documentos
tributarios. El aislamiento es bidireccional. Un cambio en el sistema externo no propaga su modelo
al núcleo, y el núcleo no escribe directamente sobre el legado.

RT-02.14 valora la aplicación documentada de patrones de arquitectura evolutiva que permitan
sustituir un componente sin reescribir la solución, y nombra tres. Esta oferta aplica los tres. La
capa anticorrupción frente al sistema heredado, el estrangulamiento progresivo con que los módulos
operativos de 2013 se van sustituyendo función por función en lugar de en un corte único, y la
abstracción de proveedores, que es lo que permite declarar la estrategia de reversibilidad que exige
RT-03.07.


**Tabla. Piezas de la capa anticorrupción**

| **Pieza** | **Función** |
|---|---|
| Adaptador de dominio | Traduce el evento de negocio, viaje cerrado o liquidación aprobada, a la estructura plana que el sistema contable espera |
| Transformador de esquemas | Homologa formatos en ambos sentidos, de modo que las convenciones de 2013 no lleguen al modelo nuevo |
| Protector de resiliencia | Cortacircuito y cola de mensajes fallidos. Si el sistema contable no responde, las transacciones se acumulan y la operación 24x7 continúa |
| Reconciliador | Verifica que todo evento encolado terminó registrado, y expone el pendiente en lugar de dejarlo silencioso |


RT-03.10 del Caso dejan expresamente abierta la emisión del documento electrónico de transporte en
un punto de carga sin cobertura, y advierten que debe resolverse y no omitirse. La solución no puede
ser diferir la emisión, porque el camión no puede rodar sin el documento. Esta oferta la resuelve
adelantando el acto de emisión, no posponiéndolo. El dispositivo a bordo o el terminal de despacho
de faena recibe por anticipado un lote de folios autorizados y el certificado de contingencia, y
genera y firma el documento localmente antes de que el camión se mueva. Al recuperarse el enlace, el
evento viaja por la capa anticorrupción hacia el sistema contable y hacia la autoridad tributaria,
con la misma clave de idempotencia que impide duplicar el folio. La factibilidad de este mecanismo
depende de una gestión que corresponde al mandante ante la autoridad tributaria, y está consultada
en el pliego del Artículo 43 bajo el número 15.


![Integración con el sistema contable heredado a través de la capa anticorrupción](D3-diagrama12_integracion_acl_erp2013.png)

*Figura. Integración con el sistema contable heredado a través de la capa anticorrupción*


#### Fuentes con desfase y telemetría del vehículo


Dos integraciones no entregan datos en el momento en que ocurren y la arquitectura las trata como
tales. El consumo de combustible llega con hasta 40 días de desfase, numeral 7.3 página 15, y los
peajes se liquidan mensualmente. Ambas se ingieren por lotes desde un depósito seguro, con
validación sintáctica y verificación de totales, y ambas quedan detrás de un adaptador, de modo que
el día en que una de esas contrapartes publique una interfaz en línea baste conectar el adaptador
nuevo sin tocar el modelo de costeo.

Ingerir el archivo no basta. Cada carga de combustible se cruza contra la posición del camión en
ese instante y cada pasada de peaje contra la traza del viaje. Ese cruce es lo que convierte un
archivo de cobros en costo imputable a un viaje, y es también lo que deja a la vista la carga que
se registró en una estación por la que el camión no pasó. Son 74.000 abastecimientos y 620.000
pasadas de peaje al año según el numeral 14.1, volumen que no admite revisión manual.

Un tercer frente es la posición de la flota de terceros. El Caso declara 340 de 374 camiones con
dispositivo repartidos en tres plataformas distintas, numeral 14.1 página 29, dos de ellas con
acceso de solo consulta y una que ni siquiera permite exportar, página 34. Unificar esa vista es
obligación de esta oferta y reemplazar esos equipos está excluido, página 24. Lo que se entrega es
la vista unificada y el estándar de homologación contra el cual clasificar cada equipo, no un
inventario de un parque que el Caso no describe.

La telemetría de fábrica de los 61 tractocamiones se lee por acoplamiento sin contacto sobre la
interfaz del vehículo, en modo de solo lectura y sujeta a la autorización de cada fabricante que
exige RT-17.06 del Caso. Esa elección no es de conveniencia técnica. La restricción 6 prohíbe que el
equipamiento a bordo afecte la garantía del vehículo o interfiera con sus sistemas de seguridad, y
el Capítulo 11 excluye intervenir la electrónica de fábrica. Una conexión que no corta ni empalma
el arnés original es lo que permite cumplir ambas.


**Tabla. Parámetros leídos de la telemetría de fábrica**

| **Parámetro** | **Para qué se usa** |
|---|---|
| Consumo instantáneo y acumulado | Componente medido del costo por kilómetro de la flota propia |
| Nivel de estanque | Contraste con el abastecimiento facturado por la red de estaciones |
| Revoluciones y aceleraciones bruscas | Conducción eficiente y explicación de la dispersión de rendimiento de 19 por ciento entre camiones del mismo modelo y ruta |
| Odómetro del vehículo | Kilómetro efectivo del viaje, denominador del costo |
| Horas de funcionamiento y de ralentí | Consumo que no produce kilómetro |
| Uso de freno de servicio y freno motor | Insumo del mantenimiento por condición |


Todos son parámetros de lectura. Ninguno escribe sobre el bus del vehículo, y esa restricción es de
diseño y no de configuración.


#### Capa analítica y costo real por kilómetro


La segregación entre lo transaccional y lo analítico se resuelve por captura de cambios hacia un
repositorio organizado en capas sucesivas de refinamiento, desde el dato crudo hasta el modelo
dimensional que consume la gerencia. La replicación lee la bitácora del motor transaccional y no
consulta sus tablas, que es la única forma de cumplir RT-05.05 sin que la analítica toque la
operación.


**Tabla. Capas del repositorio analítico**

| **Capa** | **Qué contiene** | **Qué garantiza** |
|---|---|---|
| Cruda | El registro tal como llegó, replicación transaccional, posición telemática y archivos mensuales de combustible y peaje | Reproceso completo sin volver a la fuente y trazabilidad del origen de cada indicador |
| Depurada | Deduplicación, validación de coordenadas, corrección de marcas de tiempo y cruce de la telemetría con el tramo de la orden | Un mismo hecho con una sola representación |
| De negocio | Modelo dimensional con el hecho de costo por viaje y por tramo, y las dimensiones de ruta, cliente, tracto, conductor, régimen de propiedad y tiempo | Consulta de gerencia sin conocimiento del modelo transaccional |


![Capa analítica por niveles de refinamiento y explotación del costo por kilómetro](D3-diagrama13_arquitectura_analitica_lakehouse_bi.png)

*Figura. Capa analítica por niveles de refinamiento y explotación del costo por kilómetro*


El costo por kilómetro se calcula distinto según el régimen de propiedad del equipo. Para la flota
propia se compone de combustible medido por telemetría, peajes efectivamente transitados,
neumáticos, mantenimiento, jornada del conductor y depreciación. Para la flota subcontratada el
mandante solo conoce la tarifa pactada y los anticipos de combustible, de modo que el resto se
imputa. Esa diferencia hay que declararla, porque comparar flota propia con flota de terceros sin
declararla es comparar cosas distintas, y esa comparación gobierna la decisión de crecer con una u
otra.


**Tabla. Componentes del costo por viaje y su origen**

| **Componente** | **Flota propia** | **Flota subcontratada** |
|---|---|---|
| Combustible | Medido por telemetría y valorizado con la liquidación mensual | No observable. La compañía solo conoce el anticipo que otorga |
| Peajes | Pasada efectiva cruzada con la traza | Igual, cuando el peaje lo asume la compañía |
| Conductor | Jornada imputada al tramo | Incluida en la tarifa pactada, no descomponible |
| Mantenimiento y neumáticos | Cuota por kilómetro sobre la orden de taller y la posición de neumático | No observable |
| Sobreestadía | Horas de espera acreditadas por geocerca | Igual |
| Tarifa a terceros | No aplica | Costo directo contractual |
| Denominador | Kilómetro del odómetro telemático | Kilómetro de la traza de posición |


El mecanismo es dual y no es una elección de diseño, es lo que el propio Caso fija. RT-05.29,
Capítulo 15 página 31, exige el costo consolidado de un viaje en no más de 24 horas tras su cierre,
con los componentes que a esa fecha estén disponibles y con indicación explícita de los que aún no
lo están. Se emite entonces una versión preliminar dentro de esas 24 horas, marcada como tal y
enumerando qué falta, y una versión definitiva cuando llegan el combustible y los peajes. La
primera no se sobrescribe. Ambas coexisten, y la desviación entre una y otra mide la calidad de la
estimación. Sin ese doble paso el costo por viaje se convierte en un cierre contable tardío, que es
exactamente la condición que permitió servir tres contratos bajo costo, el peor durante cuatro años.

El mismo RT-05.29 fija el resto de las latencias analíticas, y conviene tenerlas juntas porque
gobiernan el diseño de la capa.


**Tabla. Latencias de la capa analítica fijadas por RT-05.29 del Caso**

| **Dato** | **Latencia máxima** |
|---|---|
| Posición de un camión con cobertura | 2 minutos |
| Jornada acumulada de un conductor | Tiempo real, disponible en el momento de asignar |
| Tiempo de llegada y de salida en un punto de cliente | Registrado en el momento del evento |
| Costo consolidado de un viaje | 24 horas tras su cierre, con indicación de los componentes pendientes |
| Emisiones | Consolidación mensual |


La jornada acumulada es la fila que condiciona la arquitectura. Exigirla en tiempo real en el
momento de asignar significa que no puede leerse del repositorio analítico, y por eso vive en la
caché en memoria que evalúa la invariante del despacho.


#### Explotación analítica y autoservicio


RT-05.25 obliga a proveer tableros operacionales y de gestión sobre los indicadores que el Caso
define. RT-05.26 exige poder filtrar por período y por dimensión propia del caso y profundizar
desde el indicador agregado hasta la transacción de origen. Esa navegación termina en el viaje
individual con su traza, su documento de transporte y su respaldo de entrega, y no en un subtotal.

RT-05.27 obliga a que el cliente construya sus propios informes sin intervención del adjudicatario,
mediante una herramienta de autoservicio con modelo semántico documentado. El modelo semántico se
entrega validado con la gerencia de administración y finanzas, con las métricas nombradas y
definidas una sola vez, de modo que margen por ruta signifique lo mismo en todos los tableros.
RT-05.28 exige que todo informe sea exportable en formatos abiertos y programable para envío
automático por calendario.

RT-05.30 valora la analítica predictiva con el modelo, sus variables, su métrica de desempeño y su
plan de reentrenamiento documentados. Es un requisito deseable y esta oferta lo aborda en el
Subdocumento 13.


#### Modelo táctico del dominio


RT-02.13 exige presentar el modelo de dominio del negocio con las entidades principales, sus
relaciones y los eventos de negocio que las modifican. El modelo táctico que sigue lo entrega
organizado por contexto delimitado, de modo que cada agregado quede bajo el contexto que lo posee.


![Modelo táctico del dominio. Agregados, entidades y servicios por contexto](D3-diagrama2_arquitectura_tactica_ddd.png)

*Figura. Modelo táctico del dominio. Agregados, entidades y servicios por contexto*


#### Inventario de componentes lógicos


El Artículo 16.2 obliga a justificar el emplazamiento componente por componente. El inventario
lógico clasifica cada componente por capa, latencia exigida, criticidad operacional y volumen. El
servicio de Personas y cumplimiento gobierna la jornada y custodia la matriz general de vigencias,
mientras que el modelo polimórfico del Subdocumento 5 desagrega las vigencias mecánicas hacia el
contexto de Flota y activos y las habilitaciones hacia los conductores. Es el insumo directo de la
tabla de emplazamiento, que se desarrolla en la sección física y se detalla componente por
componente en el Anexo A.


**Tabla. Inventario de componentes lógicos**

| **Componente** | **Capa** | **Latencia** | **Criticidad** | **Volumen** |
|---|---|---|---|---|
| Distribución de contenidos y cortafuegos | Borde | 50 ms | Crítica | Todo el tráfico web entrante |
| Puerta de enlace | Borde | 30 ms | Crítica | Toda petición de portal, aplicación e integración |
| Despacho y asignación | Negocio | 500 ms | Máxima, bloqueante | 96.000 viajes al año |
| Flota y activos | Negocio | 1 s | Alta | 374 tractocamiones, 210 semirremolques y vigencias mecánicas |
| Personas y cumplimiento | Negocio | 500 ms | Máxima | 454 conductores, jornada y matriz de cumplimiento |
| Gestión documental | Negocio | 2 s | Alta | 128.000 documentos de transporte al año |
| Tarifas y liquidación | Negocio | 3 s | Media alta | 148 transportistas y 84 clientes |
| Bus de telemetría | Eventos | 100 ms | Crítica | Ingesta continua con peak de reconexión masiva |
| Bus transaccional | Eventos | 200 ms | Crítica | Eventos de negocio del ciclo del viaje |
| Capa anticorrupción | Integración | 500 ms | Alta | Asientos y documentos tributarios |
| Motor transaccional | Datos | 15 ms | Máxima | 96.000 viajes al año, particionado |
| Series de tiempo | Datos | 20 ms | Alta | Cerca de 120 millones de registros al año |
| Caché en memoria | Datos | 5 ms | Crítica | Geocercas de 1.400 puntos, sesiones y vigencias |
| Almacenamiento inmutable | Datos | 1 s | Alta | Conformidades, certificados y siniestros |
| Repositorio analítico | Analítica | Segundos | Media | Retención de RT-05.10 del Caso |
| Capa semántica y tableros | Analítica | 2 s | Media | Gerencia, finanzas y operaciones |
| Búfer a bordo | Terreno | Inmediata | Máxima | 182 unidades con flash industrial $\ge 8$ GB y 192 homologadas |
| Ingesta de plataformas de terceros | Integración | 500 ms | Alta | Tres plataformas existentes |
| Aplicación móvil | Presentación | 1 s | Media alta | Cuatro perfiles de RT-17.01 del Caso |
| Lector de portería y terminal | Terreno | 2 s | Alta | Cinco terminales y dos talleres |
| Sistema contable de 2013 | Heredado | No aplica | Externa | Contabilidad y documentos tributarios |


Las latencias de esta tabla son objetivos de diseño de audIT derivados de los umbrales del numeral
9.1 transversal y de RT-09.01 del Caso, salvo las que esos requisitos fijan de manera expresa.


#### Concurrencia y volumen declarados


RT-09.02 del Caso no fija un número. Ordena derivarlo de la volumetría del numeral 14.1 y
declararlo conforme al numeral 14.2, considerando de manera expresa la reconexión simultánea de
unidades al salir de zonas de sombra. La derivación es la siguiente.


**Tabla. Concurrencia derivada de la volumetría del Caso**

| **Población** | **En hora punta** | **Base de la derivación** |
|---|---|---|
| Personal interno con acceso a sistemas | 50 a 80 | Torre de 22 personas en turno, despacho de terminal, finanzas, facturación y taller, sobre los 336 con acceso del numeral 14.1 |
| Conductores en aplicación móvil | 100 a 150 | Accesos breves de inicio y cierre de turno sobre 454 conductores |
| Transportistas subcontratados en portal | 30 a 50 | Consulta de viajes y de liquidación sobre 148 |
| Clientes en seguimiento | 50 a 100 | Sesiones de seguimiento sobre 84 clientes activos |
| Suma aritmética de los rangos | 230 a 380 | Extremo inferior y superior de las cuatro filas |
| Concurrencia de dimensionamiento | 350 | Se dimensiona sobre el extremo superior redondeado, y la prueba de carga de RT-09.06 se ejecuta sobre 1,5 veces ese valor |


**Tabla. Volumen anual de telemetría derivado**

| **Magnitud** | **Valor** | **Derivación** |
|---|---|---|
| Kilómetros recorridos al año | 41.000.000 | Numeral 14.1, dato del Caso |
| Horas de marcha al año | Cerca de 745.000 | Kilómetros sobre la velocidad comercial del supuesto S-01 |
| Registros de posición en marcha | Cerca de 89 millones al año | Muestreo de 30 segundos sobre las horas de marcha |
| Registros de posición en detención | Cerca de 30 millones al año | Muestreo de 5 minutos sobre el resto de las horas del año |
| Volumen de posición en crudo | Cerca de 8 GB al año | 64 bytes por registro, supuesto S-03 |
| Volumen de telemetría de motor en crudo | Cerca de 7 GB al año | 160 bytes por muestra, una por minuto en marcha |
| Volumen almacenado | 30 a 40 GB al año | Con índices y tablas de estado sobre los dos anteriores |


RT-05.10 del Caso fija dos años en línea para las series de posición y telemetría, con política de
agregación declarada para el resto. Ese requisito es el que dimensiona la capa caliente. Conviene
dejar constancia de que el mismo código, en las Bases Técnicas Transversales, corresponde a una
materia distinta y de carácter deseable, y que esta oferta se rige por el texto del Caso.


![Patrones de resiliencia y flujo de la asignación bloqueante](D3-diagrama11_patrones_resiliencia_despacho.png)

*Figura. Patrones de resiliencia y flujo de la asignación bloqueante*


### Arquitectura física


#### Cumplimiento del modelo híbrido


El Artículo 16.1 no admite propuestas exclusivamente en nube ni exclusivamente on-premise. Esta
solución es híbrida en tres planos simultáneos, y la parte on-premise no es decorativa.


**Tabla. Los tres planos de emplazamiento**

| **Plano** | **Contenido** | **Por qué no puede estar en otro lugar** |
|---|---|---|
| Nube | Núcleo transaccional, analítica, portales e integración | Elasticidad hacia 430 camiones y absorción del peak de reconexión |
| On-premise de sitio | Continuidad de la torre en San Bernardo y gabinetes en los cuatro terminales regionales | RT-06.01 del Caso exige gabinete por terminal dimensionado para RT-03.10 |
| On-premise distribuido | Nodos a bordo de 374 camiones | La operación no puede depender de la cobertura móvil. Equipamiento físico en 148 propios y 34 por adhesión, e integración lógica en 192 de terceros |


#### El dispositivo a bordo es infraestructura


RT-06.01 del Caso ordena tratar el componente a bordo como un sistema on-premise distribuido que
cubre la operación de los 374 tractocamiones. Conforme a la restricción 3 de las bases, el
equipamiento físico provisto por el mandante con memoria flash industrial de 8 GB se despliega
directamente en las 148 unidades propias y en las 34 unidades sin equipo que adhieran al programa.
Los 192 camiones de terceros con dispositivo preexistente se integran como terminales lógicos
mediante adaptadores de interoperabilidad, exigiendo el estándar de homologación pero sin
intervenir su hardware privado. Todo el parque intervenido cuenta con su propio ciclo de vida, su
mecanismo de actualización remota, su gestión de seguridad y su plan de reposición, sujeto a que
solo puede intervenirse físicamente cuando el camión pasa por un terminal.


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


**Tabla. Tecnologías de software, versiones y soporte ofertado**

| **Componente** | **Producto y versión** | **Fin de soporte** | **Plan a 56 meses y justificación** |
|---|---|---|---|
| Orquestación y cómputo | Azure Kubernetes Service (AKS) 1.30+ | Ciclo continuo N-2 | Servicio administrado PaaS con actualización programada fuera de horas punta |
| Motor transaccional | PostgreSQL 16 Flexible Server con PostGIS | Noviembre 2028 | Alta disponibilidad zonal con conmutación automática y soporte extendido |
| Series temporales y streaming | TimescaleDB 2.15 / Event Hubs Kafka | Mayo 2029 | Particionamiento mensual y compresión columnar para 120 millones de eventos anuales |
| Caché en memoria | Azure Cache for Redis 7.2 | Octubre 2028 | Réplicas en memoria RAM con latencia menor a 5 ms para geocercas y sesiones |
| Almacenamiento a bordo | SQLite 3 con WAL | Indefinido (LTS) | Motor embebido en flash industrial de 8 GB con nivelación de desgaste |
| Repositorio analítico | Delta Lake en ADLS Gen2 | Soporte activo | Arquitectura de tres capas con captura de cambios desacoplada |
| Seguridad e identidad | Microsoft Entra ID y Key Vault HSM | Continuo | Autenticación federada y custodia de claves FIPS 140-2 Nivel 3 |


El diseño detallado del modelo de persistencia, particionamiento y consultas transaccionales de
estos motores se acompaña en el Subdocumento 5.


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


RT-03.13 transversal obliga a declarar qué funciones no estarán disponibles sin enlace y qué
procedimiento manual las suple, y evalúa como observación grave la ausencia de esta declaración. El
mismo código en el Capítulo 15 del Caso, página 31, regula otra materia y fija un compromiso
adicional que esta oferta asume. La sincronización tras la reconexión no debe superar 20 minutos por
camión después de 72 horas sin cobertura, sin perder ningún evento de jornada ni ningún registro de
tiempo en instalaciones de cliente, y con un diseño que soporte la reconexión simultánea de varios
cientos de unidades al salir de una zona de sombra. Ese es el requisito que obliga a la ventana de
sincronización escalonada y al retroceso aleatorizado descritos más arriba, y la razón por la que la
ingesta se dimensiona sobre el peak de reconexión y no sobre el promedio.


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
| S-13 | Concurrencia simultánea en hora punta | 300 a 350 sesiones | Derivada del numeral 14.1 y medida en la Etapa 1 |
| S-14 | Registros de posición al año | Cerca de 120 millones, de los cuales 89 millones en marcha | Derivada de S-01 y de la frecuencia adaptativa. Supone el dispositivo muestreando también con el camión detenido |
| S-15 | Volumen almacenado de series de tiempo | 30 a 40 GB al año | Ajuste con el modelo de datos del Subdocumento 5 |
| S-16 | Parámetros de cortacircuito, mamparo y tiempo de espera | Declarados en la Sección 4 | Ajuste con la prueba de carga de RT-09.06 |
| S-17 | Ventana de disponibilidad de las plataformas de terceros y de la autoridad tributaria | No declarada por las bases | Consulta al mandante |


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
- **Las consultas del Artículo 43 están enviadas y no respondidas.** Las
    interpretaciones que esta oferta adopta sobre la sustitución de los módulos operativos de 2013,
    la autorización de los fabricantes para leer la telemetría, el mecanismo digital de la red de
    estaciones de servicio y el alcance del costo consolidado en 24 horas son propuestas de audIT
    consignadas en el pliego, no respuestas del mandante. Si el Acta de Respuestas las modifica,
    esta arquitectura se ajusta en el Informe 2.
- **El producto satelital evaluado declara 40 horas de almacenamiento**
    (Webfleet Solutions, 2025) frente a las 72 horas exigidas. La especificación de esta oferta fija
    la capacidad mínima en 8 GB precisamente para no depender de ese límite.


### Diagramas de arquitectura


Los diagramas que siguen se presentan en orientación horizontal a página completa. Sus versiones a resolución de trabajo acompañan esta oferta como archivos independientes.


![Contextos delimitados del dominio y sistemas con los que convive la solución](Contextos.pdf)

*Figura. Contextos delimitados del dominio y sistemas con los que convive la solución*


![Mapa de integraciones. Sistemas internos, fuentes de terreno y contrapartes externas](LogicaIntegraciones.pdf)

*Figura. Mapa de integraciones. Sistemas internos, fuentes de terreno y contrapartes externas*


![Arquitectura física general. Nube, sitio de continuidad, gabinetes de terminal y flota](Main.pdf)

*Figura. Arquitectura física general. Nube, sitio de continuidad, gabinetes de terminal y flota*


![El camión como componente on-premise distribuido](Camion.pdf)

*Figura. El camión como componente on-premise distribuido*


![Separación entre recuperación ante desastres y continuidad operacional en el borde](DosEjes.pdf)

*Figura. Separación entre recuperación ante desastres y continuidad operacional en el borde*


![Flujo de un evento de jornada registrado sin cobertura](Flujo.pdf)

*Figura. Flujo de un evento de jornada registrado sin cobertura*


![Correspondencia entre capa lógica y emplazamiento físico](LogicaEmplazamiento.pdf)

*Figura. Correspondencia entre capa lógica y emplazamiento físico*


## Anexo A. Tabla de emplazamiento de componentes


El Artículo 16.2 obliga a justificar, componente por componente, la decisión de emplazamiento en
función de latencia, criticidad operacional, volumen de datos, restricciones regulatorias,
disponibilidad de conectividad y costo total de propiedad, y califica como observación grave toda
asignación no justificada. El numeral 1.5 añade que declarar cumplimiento sin individualizar el
componente equivale a no declarar. Por eso cada fila lleva su justificación propia.


### Emplazamientos declarados


**Tabla. Emplazamientos y tipología declarada por sitio**

| **Código** | **Emplazamiento** | **Tipología declarada** | **Fundamento** |
|---|---|---|---|
| N | Nube, Azure Chile Central, tres zonas | No aplica | RT-03.01 y RT-03.02 |
| N2 | Nube, segunda región Azure | No aplica | RT-07.02 y Artículo 16.3 |
| SB | San Bernardo, 26 metros cuadrados | Sala técnica secundaria o de sitio | Numeral 6.1 transversal |
| GT | Gabinete de terminal, cuatro unidades | Gabinete o borde operacional | RT-06.01 del Caso |
| DB | Dispositivo a bordo, 374 unidades | On-premise distribuido | RT-06.01 del Caso |
| BM | Borde móvil | No aplica | RT-17.01 |


### Decisión de emplazamiento componente por componente


**Tabla. Tabla de emplazamiento de componentes. Formulario T-11**

| **N.º** | **Componente lógico** | **Capa** | **Empl.** | **Justificación de la decisión** |
|---|---|---|---|---|
| 1 | CDN y protección perimetral | Borde | N | Punto de presencia distribuido. no tiene sentido físico fuera de la nube |
| 2 | Puerta de enlace de servicios | Borde | N | Autenticación y enrutamiento centralizados. escala con el peak de reconexión |
| 3 | Servicio de despacho y asignación | Negocio | N | Orquesta recursos de toda la red. requiere la vista completa de flota y jornada |
| 4 | Nodo de continuidad operacional | Negocio | SB | RT-21.06: asignar viaje, emitir DET y recibir pánico son severidad máxima. No pueden depender del enlace a la nube |
| 5 | Servicio de flota y mantenimiento | Negocio | N | Administración centralizada de activos. tolera latencia de segundos |
| 6 | Servicio de jornada | Negocio | N | Validación bloqueante ≤ 30 s (RT-09.01) contra el dato consolidado |
| 7 | Servicio de gestión documental | Negocio | N | Sellado y control de retención centralizados |
| 8 | Servicio de tarifas y liquidación | Negocio | N | Proceso por lotes mensual. sin exigencia de latencia operacional |
| 9 | Bus de eventos de telemetría | Eventos | N | Absorbe la ráfaga de cientos de unidades saliendo de la misma sombra |
| 10 | Bus transaccional | Eventos | N | Entrega garantizada con cola de mensajes fallidos |
| 11 | Pasarela de la capa anticorrupción | Integración | SB | Debe alcanzar el ERP heredado, que está físicamente en San Bernardo |
| 12 | Integración telemática de terceros | Integración | N | Consume APIs de los dos proveedores externos. cero intervención física (restricción 3) |
| 13 | Integración rFMS de fábrica | Integración | N | API del fabricante, solo lectura, autorización por OEM (RT-17.06) |
| 14 | Base transaccional | Datos | N | Consistencia estricta con alta disponibilidad multizona |
| 15 | Base de series de tiempo | Datos | N | Volumen y patrón de escritura masiva. 2 años en línea (RT-05.10 del Caso) |
| 16 | Caché distribuida | Datos | N | Sesiones, vigencias y geocercas de consulta. no sustituye la evaluación a bordo |
| 17 | Repositorio documental inmutable | Datos | N | Evidencia probatoria con retención de 5 a 10 años (RT-07.11, RT-05.10) |
| 18 | Lakehouse analítico | Analítica | N | Aislamiento OLTP/OLAP. costo por km en ≤ 24 h (RT-05.29) |
| 19 | Capa semántica de autoservicio | Analítica | N | Explotación por Finanzas sin intervención de TI (RT-05.27) |
| 20 | Gestión del parque de dispositivos | Terreno | N | Inventario, configuración, firmware, bloqueo y borrado remotos (RT-03.18) |
| 21 | Identidad, secretos y cifrado de campo | Seguridad | N | Clave gestionada independiente de la infraestructura respaldada (RT-07.10, RT-11.10) |
| 22 | Observabilidad | Observab. | N | Cobertura unificada de nube y on-premise, sin puntos ciegos (RT-03.16) |
| 23 | Réplica de recuperación ante desastres | Todas | N2 | RT-07.02: distancia suficiente para no compartir el evento de fuerza mayor |
| 24 | ERP contable heredado 2013 | Legado | SB | Sistema existente no reemplazable y único emisor de documentos tributarios (Cap. 11) |
| 25 | Terminación de enlaces y borde de red | Red | SB | Punto de entrada de ExpressRoute y VPN por rutas físicas distintas (RT-03.17, RT-06.32) |
| 26 | Custodia de medios de respaldo | Datos | SB | Medio físico transportable fuera de sitio (RT-06.26, esquema 3-2-1-1-0 de RT-07.09) |
| 27 | Nodo de terminal | Negocio | GT | RT-03.10 del Caso: «Los terminales deben operar 12 horas sin enlace hacia el exterior» |
| 28 | Lector de portería y enrolamiento | Terreno | GT + SB | Verificación local de vigencias en los 5 terminales. el enrolamiento biométrico se centraliza (RT-06.22) |
| 29 | Buffer no volátil ≥ 8 GB | Terreno | DB | RT-03.10: 72 h sin cobertura sin pérdida de registro. RT-10.05: hasta 12 días (288 h) de cierre fronterizo |
| 30 | Motor de geocercas a bordo | Terreno | DB | RT-09.01: registro de llegada y salida automático, sin intervención del conductor y sin equipamiento en instalaciones del cliente |
| 31 | Cálculo de alerta de jornada a bordo | Terreno | DB | Criterio 28: la alerta debe llegar aunque no haya enlace, con anticipación al lugar seguro |
| 32 | Identificación del conductor | Terreno | DB | RT-12.11: sin manipular un dispositivo y sin recordar una credencial |
| 33 | Módulo satelital de ráfaga corta | Terreno | DB | Subconjunto por riesgo. Población no estimable hasta la medición de RT-03.24 |
| 34 | App móvil del conductor | Borde | BM | RT-17.01. Canal voluntario e incentivado. la trazabilidad obligatoria no depende de él (restricciones 1 y 2) |


**Tabla. Matriz de los seis criterios del Artículo 16.2**

| **N.º** | **Componente** | **Latencia** | **Criticidad** | **Volumen** | **Regulación** | **Conectividad** | **TCO** |
|---|---|---|---|---|---|---|---|
| 3 | Despacho y asignación | ≤ 30 s extremo a extremo | Máxima | 96.000 viajes/año | Sin exigencia específica | Requiere enlace | Elástico |
| 4 | Nodo de continuidad | ≤ 30 s local | Máxima | Ventana de 12 h | Sin exigencia específica | Opera sin enlace | Fijo, dos nodos |
| 6 | Servicio de jornada | ≤ 30 s | Máxima | 454 conductores | Datos personales de 258 externos | Requiere enlace | Elástico |
| 9 | Bus de telemetría | ≤ 100 ms | Crítica | Peak de reconexión masiva | Sin exigencia específica | Requiere enlace | Elástico por partición |
| 14 | Base transaccional | ≤ 15 ms | Máxima | Particionado mensual | Retención 5-10 años | Requiere enlace | Reservado |
| 15 | Series de tiempo | ≤ 20 ms | Alta | 2 años en línea + agregación | Sin exigencia específica | Requiere enlace | Por capa hot/cold |
| 17 | Repositorio inmutable | ≤ 1 s | Alta | Evidencia probatoria | WORM, 10 años siniestros | Requiere enlace | Por capa de acceso |
| 21 | Identidad y cifrado | ≤ 50 ms | Crítica | Sin exigencia específica | RT-11.10 cifrado a nivel de campo . Ley 21.719 | Requiere enlace | Fijo por HSM |
| 23 | Réplica de DR | RPO ≤ 15 min | Crítica | Espejo de producción | Sin exigencia específica | Enlace entre regiones | Activo-pasivo |
| 24 | ERP heredado | N/A | Externa | Contabilidad y DTE | Único emisor tributario | Local | Existente |
| 27 | Nodo de terminal | Local | Alta | 12 h de operación autónoma | Sin exigencia específica | Opera sin enlace 12 h | 4 gabinetes |
| 29 | Buffer a bordo | Inmediata | Máxima | $\approx$ 0,8 MB en 72 h . ≥ 8 GB de capacidad | Evidencia de jornada | Opera sin cobertura | Por unidad |
| 30 | Geocercas a bordo | Inmediata | Alta | Eventos discretos | Sin exigencia específica | Opera sin cobertura | Sin costo marginal |
| 33 | Módulo satelital | ≤ decenas de s | Alta | Ráfagas cortas | Sin exigencia específica | Sin cobertura celular | Por mensaje |
| 34 | App móvil | ≤ 1 s | Media, no bloqueante | 454 potenciales | Consentimiento revocable | Requiere enlace | Por desarrollo |


### Reparto resultante


Dieciocho componentes en la región primaria de nube, uno en la segunda región, cinco en San
Bernardo, dos en gabinete de terminal, cinco en el dispositivo a bordo y uno en borde móvil. La
propuesta cumple el Artículo 16.1, porque no es exclusivamente en nube ni exclusivamente
on-premise, y la parte on-premise sostiene las tres funciones que RT-21.06 clasifica en severidad
máxima cuando cae el enlace.


### Celdas que no se pueden cerrar en esta instancia


**Tabla. Materias abiertas de la tabla de emplazamiento**

| **Materia** | **Por qué y cómo se cierra** |
|---|---|
| Población del módulo satelital | RT-03.24 del Caso prohíbe suponer la cobertura y exige medirla en terreno. Se cierra con la campaña de medición de la Etapa 1 |
| Unidades totales con almacenamiento local | Depende de cuántos transportistas adhieran. Se cierra con el plan de adhesión |
| Dimensionamiento del nodo de continuidad | Requiere el peak de asignación de la torre, derivado de RT-09.02 y del numeral 14.2 |


## Bibliografía

Dirección del Trabajo. (2009). *Resolución Exenta N.º 1213. Sistema obligatorio de control de asistencia, horas de trabajo y descanso para conductores de vehículos de carga terrestre interurbana*.

Ministerio del Trabajo. (2003). *Decreto con Fuerza de Ley N.º 1. Texto refundido del Código del Trabajo. Artículo 25 bis*. Biblioteca del Congreso Nacional de Chile. https://www.bcn.cl/leychile/navegar?idNorma=207436

Escuela de Informática PUCV. (2026a). *Bases Administrativas. Licitación Pública Internacional N.º TFEP-01/2026* (FEP01.26).

Escuela de Informática PUCV. (2026b). *Bases Técnicas Transversales* (FEP02.26).

Escuela de Informática PUCV. (2026c). *Bases Técnicas del Caso 10. Transporte de Carga* (FEP03.10.26).

FMS Standard. (2025). *Technical Specification rFMS vehicle data version 5.0.0*. https://www.fms-standard.com

Iridium Communications. (2024). *Iridium Short Burst Data Service Developers Guide*.

ISO. (2011). *ISO/IEC 27031*. ISO. (2013). *ISO 16290. Definition of the Technology Readiness Levels (TRLs) and their criteria of assessment*. ISO. (2017). *ISO 15005. Road vehicles — Ergonomic aspects of transport and information and control systems*. ISO. (2019). *ISO 9241-210. Ergonomics of human-system interaction*. ISO. (2019). *ISO 22301*. ISO. (2022). *ISO/IEC/IEEE 42010*. ISO. (2023). *ISO 14083*.

Federal Motor Carrier Safety Administration [FMCSA]. (2020). *Commercial Motor Vehicle Driver Fatigue, Long-Term Health, and Highway Safety: Research Needs*. The National Academies Press. https://doi.org/10.17226/21921

Microsoft. (2025). *Azure geographies. Chile Central region*.

Congreso Nacional de Chile. (2002). *Ley N.º 19.799 sobre documentos electrónicos, firma electrónica y servicios de certificación de dicha firma*. https://www.bcn.cl/leychile/navegar?idNorma=196640

Congreso Nacional de Chile. (2021). *Ley N.º 21.377 que sanciona como infracción gravísima la conducción de vehículos manipulando dispositivos de telefonía móvil o cualquier otro artefacto electrónico («Ley No Chat»)*. https://www.bcn.cl/leychile/navegar?idNorma=1166014

Congreso Nacional de Chile. (2024). *Ley N.º 21.719 que regula la protección y el tratamiento de los datos personales y crea la Agencia de Protección de Datos Personales*. Diario Oficial de 13 de diciembre de 2024. https://www.bcn.cl/leychile/navegar?i=1209272

Ministerio de Transportes. (1995). *Decreto Supremo N.º 298*.

Ministerio del Trabajo. (2006). *Ley N.º 20.123 sobre trabajo en régimen de subcontratación*.

NFPA. (2022). *NFPA 2001*. NIST. (2014). *NIST SP 800-88 Rev. 1*.

Smart Freight Centre. (2023). *GLEC Framework, version 3.0*.

Webfleet Solutions. (2025). *WEBFLEET SAT. Ficha técnica del producto*.

World Wide Web Consortium. (2025). *Verifiable credentials data model v2.0*. W3C Recommendation de 15 de mayo de 2025. https://www.w3.org/TR/vc-data-model-2.0/
