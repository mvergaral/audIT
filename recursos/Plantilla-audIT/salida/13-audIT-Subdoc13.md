# Innovaciones

**Subdocumento N.º 13**

| | |
|---|---|
| Empresa | audIT, Empresa N.º 10 |
| Licitación | Licitación Pública Internacional N.º TFEP-01/2026. Caso 10 Transporte de Carga |
| Proyecto | Plataforma Digital de Misión Crítica para Transporte de Carga |
| Cliente | Transportes Curimón S.A. |
| Instancia | Informe Preparatorio 1. Oferta Técnica Sobre N.º 2 |
| Contenido | Cartera de cinco innovaciones, una por cada tipo obligatorio del Artículo 28. |
| Versión | 1.0 |
| Fecha | 7 de septiembre de 2026 |
| Lugar | Viña del Mar, Chile |

---

## Innovaciones


El Artículo 28 exige una cartera de cinco innovaciones, una por cada tipo obligatorio y sin repetir
tipo. En esta instancia cada innovación se nombra y se explica en su alcance, con su idea, la
tecnología que la sustenta y el resultado esperado. El refinamiento trazable con la arquitectura y
la estructura de desglose corresponde al Informe 2, la valorización al Informe 3 y el Formulario
T-19 con los siete elementos del Artículo 29 a la propuesta final.

El Artículo 30.2 establece que se valora la pertinencia al caso por sobre la novedad tecnológica en
abstracto, y que una innovación sofisticada que no resuelve un problema real del caso obtiene menor
puntaje que una sencilla, bien justificada y con impacto verificable. Las cinco propuestas que
siguen se eligieron con ese criterio.


**Tabla. Cartera de innovaciones y responsables**

| **Tipo** | **Categoría del Artículo 28** | **Innovación** | **Responsable** |
|---|---|---|---|
| 1 | Producto o servicio | Portal del transportista con liquidación en curso | Ignacio C. |
| 2 | Proceso | Despliegue sin detener la flota | Ignacio V. y Alonso |
| 3 | Tecnológica o de arquitectura | Operación desconectada y vista única de flota | Marcel y Martín |
| 4 | Modelo de negocio o contratación | Esquema de adhesión y propiedad del dispositivo | Matías V. |
| 5 | Experiencia de usuario, sostenibilidad o impacto social | Bienestar del conductor y descanso en parador seguro | Carlos y Naomi |


### Tipo 1. Portal del transportista con liquidación en curso


**Idea.** Hoy el transportista subcontratado espera nueve días a que ocho personas calculen su
liquidación, y el once por ciento de esos cálculos se corrige después. Durante ese tiempo no tiene
forma de saber cuánto va a cobrar ni por qué. La innovación consiste en mostrarle su liquidación
mientras se construye, viaje a viaje, en lugar de entregársela cerrada al final del mes.

**Tecnología que la sustenta.** Portal segregado por identidad con vista propia de cada
transportista, alimentado por el mismo motor de costeo que produce la liquidación oficial. Cada
viaje aparece con su tarifa aplicada, sus tiempos de espera certificados por geocerca y sus
descuentos, en el momento en que el dato entra al sistema y no cuando el mes cierra.

**Resultado esperado.** Reducción del tiempo de cierre mensual y del porcentaje de
liquidaciones corregidas. Y un efecto que importa más que ambos, porque el portal es la primera
razón concreta que un dueño de camión tiene para adherir. La transparencia del pago es el
argumento comercial del plan de adhesión que mide el criterio 27.

**Lo que agrega sobre lo que las bases ya exigen.** Los criterios 21 y 29 obligan a que el
transportista autenticado consulte sus viajes, evidencias y liquidación en curso dentro del portal
del mandante. Eso está comprometido en el alcance y no se presenta como innovación. Lo que agrega
esta ficha es que la evidencia salga del portal como un documento del transportista, verificable
por un tercero que no tiene acceso al sistema del mandante. Un expediente exportable con la jornada
acreditada de sus conductores, la vigencia de sus habilitaciones y la hoja de vida de sus equipos,
que él presenta a sus otros clientes, a la autoridad o a su aseguradora. Las bases no lo piden, y
tampoco cae en la exclusión del Capítulo 11 sobre administrar la contabilidad de los
transportistas, porque no administra nada. Devuelve a su titular una evidencia ya producida.

**Madurez.** Escala de niveles de madurez tecnológica de uno a nueve
(ISO, 2013). La firma electrónica avanzada con verificación en línea está en nivel nueve,
en operación productiva y regulada en Chile desde 2002 (Congreso Nacional de Chile, 2002), y es la línea base
comprometida. La credencial verificable alcanzó el estado de recomendación en mayo de 2025
(World Wide Web Consortium, 2025) y se sitúa entre siete y ocho por su adopción todavía acotada en el
ecosistema logístico local. El modelo de datos se diseña para incorporarla sin rehacer la emisión.
La composición del expediente sobre datos de jornada y mantenimiento está en nivel seis, porque el
componente es convencional y lo nuevo es su uso probatorio por el titular.

**Incorporación en la arquitectura y en el cronograma.** Un servicio de emisión de expediente
en la capa de servicios de negocio, que consume control de jornada, gestión documental y gestión de
flota. Un servicio público de verificación sin autenticación, que recibe un código y responde
válido o inválido sin revelar contenido. La firma la provee la bóveda de claves de la capa de
seguridad. El portal expone la solicitud y la descarga. La decisión entre firma avanzada y
credencial verificable se documenta en el mes cuatro con el levantamiento de destinatarios reales,
la emisión se construye entre los meses diez y doce, y el expediente queda disponible durante la
marcha blanca de la Etapa 1.

**Impacto económico.** La inversión es incremental sobre el portal, que ya está presupuestado
por los criterios 21 y 29 con independencia de esta ficha. Agrega el desarrollo de los dos
servicios y la suscripción anual de certificados de firma del emisor, partidas por cotizar cuyo
valor definitivo se incorpora al flujo de caja del Informe 3. El efecto en costo operacional es
marginal y positivo, porque el expediente se compone de evidencia que el sistema ya produce y
conserva por obligación del criterio 4. El beneficio principal no se realiza en esta línea sino en
la adhesión, de la que depende el sesenta coma cuatro por ciento de la capacidad, y así se declara
en lugar de atribuirle un ahorro directo que no tiene.

**Indicador de verificación.** Línea base cero, porque la capacidad no existe. Meta de
cuarenta por ciento de los transportistas adheridos emitiendo al menos un expediente, medida al
cierre de la marcha blanca en el mes quince. Meta secundaria de reducir a menos del dos por ciento
las liquidaciones corregidas después de emitidas, desde el once por ciento actual, medida en el
tercer cierre mensual posterior al paso a producción.

**Riesgo de adopción.** El riesgo principal es que el transportista no perciba utilidad y no
emita el expediente, con probabilidad media e impacto alto, porque desaparece el argumento central
de la adhesión. Se mitiga asistiendo la primera emisión en el terminal durante el enrolamiento. El
riesgo secundario es que los destinatarios no acepten el documento como prueba, que se mitiga
levantando destinatarios reales en el mes cuatro antes de construir. La contingencia general es que
el portal obligatorio se entrega igual, porque esta ficha es una capa sobre él y no una condición
de su funcionamiento. Lo que se pierde es el argumento de reciprocidad, que se compensa con los
incentivos económicos de la ficha tipo 4.

**Investigación adicional requerida.** La elección entre firma electrónica avanzada y
credencial verificable requiere el levantamiento de destinatarios del mes cuatro. El motor de
costeo del que depende la liquidación en curso ya forma parte del alcance de la Etapa 1.


### Tipo 2. Despliegue sin detener la flota


**Idea.** Un camión detenido no produce, la intervención a bordo solo puede hacerse cuando el
camión pasa por un terminal, y ese paso ocurre cada seis días en promedio mientras el 22 por ciento
de la flota subcontratada pasa menos de una vez al mes. La innovación convierte ese paso fortuito
en una ventana de intervención planificada y de duración acotada.

**Tecnología que la sustenta.** Anticipación de la llegada al terminal a partir de la posición
de la propia flota, equipo preconfigurado en el stock de reemplazo antes de que el camión llegue, y
gestión remota del parque para que todo el ciclo de vida posterior ocurra por aire. La intervención
física se reduce a sustituir y salir.

**Resultado esperado.** Unidades intervenidas por mes y tiempo de inmovilización por unidad.
El techo del ritmo lo fija el 22 por ciento que pasa menos de una vez al mes, y esa limitación se
declara en lugar de ocultarse.

**Investigación adicional requerida.** Ninguna en el concepto. El tiempo real de intervención
por familia de vehículo se mide en el piloto de la Etapa 1.


### Tipo 3. Operación desconectada y vista única de flota


**Idea.** Cuarenta y un millones de kilómetros al año con tramos de más de 80 kilómetros sin
cobertura, 34 camiones sin dispositivo y 340 repartidos en tres plataformas incompatibles, una de
las cuales no permite exportar. La innovación hace que el registro exista en el vehículo antes de
que exista cualquier enlace, garantizando operatividad total durante desconexiones extremas, y que
las tres plataformas se vean como una sola interfaz unificada.

**Tecnología que la sustenta.** Arquitectura híbrida Edge-to-Cloud con almacenamiento local no
volátil en cabina sobre memoria flash industrial ($\ge 8\text{ GB}$) con algoritmos de nivelación de
desgaste (\textit{wear-leveling}) resistentes a choques térmicos ($-20^\circ\text{C}$ a $+70^\circ\text{C}$)
y vibraciones severas (RT-08.11). Motor embebido SQLite en modo WAL (\textit{Write-Ahead Logging}) con
serialización binaria ultracompacta en Protocol Buffers (Protobuf) sobre MQTT v5.0 / Kafka, requiriendo
menos de 10 MB para 72 horas continuas y soportando hasta 288 horas (12 días) de aislamiento en el Paso
Los Libertadores (RT-10.05). Capa de ingestión telemática unificada que normaliza eventos de las tres
plataformas comerciales vía adaptadores API/Webhooks sin intervenir físicamente equipos de terceros
(Restricción 3, Decisión D-02). Emisión tributaria offline de Documentos Electrónicos de Transporte (DET)
con folios CAF pre-asignados y Timbre Electrónico DTE (TED) en memoria criptográfica antes del rodado (RF-014).

**Madurez.** Nivel de Madurez Tecnológica TRL 8/9 (\cite{iso16290}), sustentado en componentes
comerciales y estándares industriales maduros (MQTT v5.0, SAE J1939-71, OCI Runtime). La consistencia
eventual y reconciliación determinista de estados tras particiones prolongadas se apoya formalmente en
estructuras de datos replicadas libres de conflictos (CRDT) y modelos de replicación distribuida
(Kleppmann, 2017).

**Incorporación en la arquitectura y en el cronograma.** Se articula en la Capa 1 (Borde Terrestre:
dispositivo con flash $\ge 8\text{ GB}$, SQLite WAL y acopladores inductivos FMS J1939 en 61 unidades
propias sin alterar garantías), Capa 3 (APIM con mTLS y limitación elástica de tasa a 60 req/min por
dispositivo para ráfagas de reconexión), Capa 5 (Event Ingestion Kafka con búfer de hasta 1.500 pings/min)
y Capa 6 (TimescaleDB para series temporales y deduplicación en PostgreSQL 16 por \texttt{idempotency_key}).
Su trazabilidad contractual con la EDT comprende los paquetes EDT 3.4 (Conector de Ingestión Telemática,
Meses 3--6), EDT 4.2 (Homologación e Instalación de Búfer a Bordo $\ge 8\text{ GB}$, Meses 4--8) y EDT 4.5
(Acopladores Inductivos FMS J1939 en 61 camiones, Meses 6--9).

**Resultado esperado.** Los indicadores parten de una línea base medida:


**Tabla. Indicadores de la innovación tipo 3**

| **Indicador** | **Línea base** | **Meta** |
|---|---|---|
| Pérdida de registros en desconexión de 72 horas | Pérdida total en sombras de más de dos horas | Cero pérdida |
| Resistencia al cierre de Los Libertadores | Ceguera tras 24 a 48 horas | Preservación hasta 288 horas (12 días) |
| Visibilidad unificada de la flota | Tres plataformas separadas y 34 unidades ciegas | Totalidad de unidades en vista única |
| Latencia de reconciliación tras la sombra | No existe sincronización | Supera el umbral de 20 minutos del Capítulo 15 |
| Emisión del documento sin señal | Rezagada o inexistente | Emitido conforme antes de que el vehículo se mueva |


**Investigación adicional requerida.** La factibilidad técnica y SLA de los adaptadores de
exportación de la plataforma que hoy no permite salida directa debe verificarse con ese proveedor
durante la actividad EDT 3.4 en la Etapa 1.


### Tipo 4. Esquema de adhesión y propiedad del dispositivo


**Idea.** Financiamiento del dispositivo, incentivos de adhesión, consentimiento granular y
beneficios verificables. La primera pregunta que hace un dueño de camión es de quién es el equipo, quién lo
paga y qué pasa con él si deja de trabajar con la compañía. La segunda es si el aparato va a
delatar cuándo trabaja para la competencia. Mientras esas dos preguntas no tengan respuesta, ningún
diseño técnico se despliega. La innovación separa la propiedad del equipo de la propiedad del dato,
y le entrega la segunda al dueño del camión.

**Tecnología que la sustenta.** Figura de comodato sobre el equipamiento, con condiciones de
retiro y de traspaso definidas desde el inicio. Modo de privacidad implementado en el firmware del
dispositivo y no en configuración de servidor, de modo que la posición deja de emitirse hacia el
mandante cuando el camión trabaja para otro cliente, y esa garantía sea verificable por el dueño en
lugar de prometida. Consentimiento granular y revocable administrado desde el portal, con registro
auditable de cada acceso a la información de localización.

**Lo que agrega sobre lo que las bases ya exigen.** El Capítulo 11 resuelve quién compra el
hardware, y presentar esa regla como innovación sería presentar como propia una decisión que ya
está en las bases. Lo que el Caso deja abierto es la decisión quinta del numeral 16.1, sobre el
dispositivo instalado en un camión de un tercero, y la restricción 2, que obliga a conseguir por
contrato, por incentivo o por diseño lo que dependa de terceros. Esta ficha agrega tres cosas que
las bases no piden. La ventana de transmisión gobernada en el firmware, que convierte una promesa
de privacidad en una propiedad verificable. El comodato con retiro sin costo, que elimina el riesgo
patrimonial del transportista sobre un activo que es suyo, y que según el levantamiento del Caso
alcanza los doscientos millones de pesos en el caso de un dueño de dos camiones
(Escuela de Informática PUCV, 2026c). Y el
financiamiento del incentivo con el recupero de un ingreso que hoy se pierde, de modo que la
adhesión no compita con el margen operacional de nueve por ciento del mandante.

**Madurez.** Los componentes técnicos se evalúan en la escala de niveles de madurez
tecnológica (ISO, 2013). El control de transmisión por ventana en el dispositivo está en
nivel ocho, porque la gestión remota de configuración de equipos conectados es tecnología
productiva y lo específico es la regla de negocio que la gobierna. El registro de consentimiento
granular y revocable está en nivel ocho y su exigencia es normativa (Congreso Nacional de Chile, 2024). El
componente contractual no se califica en esta escala porque no es una tecnología. El comodato de
equipamiento a proveedores de servicio es figura de uso corriente y no requiere desarrollo. El
reparto de recupero sobre evidencia aportada tiene precedente acotado y poca documentación pública
en el sector nacional.

**Incorporación en la arquitectura y en el cronograma.** La ventana se aplica en la unidad
telemática y en el búfer local, que almacenan fuera de ella y no transmiten. El concentrador de
dispositivos distribuye la configuración de ventana a cada equipo. Un servicio de consentimiento y
un servicio de adhesión, ambos nuevos, definen la ventana desde la asignación del viaje y registran
la revocación. El portal expone la consola de permisos con bitácora. La adhesión comienza en el mes
uno, antes que cualquier construcción, porque el numeral 13.1 advierte que hay decisiones cuyo
plazo no lo fija la tecnología sino una negociación con terceros, y las negociaciones no se
paralelizan. La cohorte piloto va entre los meses seis y nueve, la consola entre el nueve y el
doce, y el resultado se mide en la marcha blanca.

**Impacto económico.** La adquisición del equipamiento es del mandante conforme al Capítulo
11, y audIT especifica y dimensiona la cantidad sobre la adhesión efectiva y no sobre los
doscientos veintiséis camiones de terceros. Las partidas propias son el diseño y la validación
jurídica del anexo, la campaña de enrolamiento en cinco terminales con presencia en horario de
relevo, y la consola de consentimiento. Todas por cotizar, con valorización en el flujo de caja del
Informe 3. En costo operacional aumenta la conectividad, el soporte y la reposición del parque en
comodato, y disminuyen el costo de la liquidación mensual y el de gestionar las objeciones de
cobro. El beneficio se apoya en base verificada. En 2025 se facturaron trescientos cuarenta
millones de pesos por tiempos de espera y el setenta y uno por ciento fue objetado, es decir
doscientos cuarenta y un coma cuatro millones, porque la hora de llegada se anota en papel. La meta
de reducir la objeción bajo el veinte por ciento implica un recupero anual del orden de ciento
setenta y tres millones, cifra derivada de la meta y no comprometida como ingreso. Ese recupero es
el que financia el incentivo, y su reparto concreto se fija en el anexo contractual.

**Indicador de verificación.** Línea base cero de ciento cuarenta y ocho transportistas
adheridos. Meta de setenta por ciento al cierre de la Etapa 1 y noventa por ciento al cierre de la
Etapa 2. La primera medición de anexos firmados ocurre desde el mes tres, muy antes del paso a
producción, lo que satisface con holgura el requisito deseable de que al menos una innovación sea
verificable durante la marcha blanca. Indicadores complementarios, tasa de revocación del
consentimiento bajo el diez por ciento de los adheridos, y objeción sobre cobros de espera
respaldados bajo el veinte por ciento desde el setenta y uno actual.

**Riesgo de adopción.** Que la adhesión no alcance el setenta por ciento en la Etapa 1, con
probabilidad media e impacto alto, porque limita jornada, posición y emisiones sobre el sesenta
coma cuatro por ciento de la capacidad. Se mitiga comenzando en el mes uno y mostrando beneficio
verificable antes de pedir el equipo, y la contingencia es escalonar el incentivo y extender la
modalidad de datos, que no requiere instalar nada. Que el transportista desconfíe de la ventana de
transmisión, que se mitiga haciéndola auditable por él mismo desde su consola de permisos. Que los
clientes no acepten la evidencia telemática como respaldo del cobro, lo que eliminaría la fuente de
financiamiento del incentivo, con contingencia de financiarlo con la reducción del costo de
liquidación, que no depende del cliente. Y que el anexo no resista revisión jurídica, con
probabilidad baja e impacto alto, mitigado por la validación entre los meses uno y tres, antes de
construir.

**Investigación adicional requerida.** El tratamiento contable del comodato y el reparto
concreto del recupero de sobreestadía requieren definición conjunta con el mandante. La adquisición
del equipamiento no está abierta, la resuelve el Capítulo 11 del Caso.


### Tipo 5. Bienestar del conductor y descanso en parador seguro


**Idea.** Una alerta que avisa al conductor cuando su cuota de cinco horas continuas está por agotarse, entregada en medio de una cuesta sin bermas o en un tramo desértico sin paraderos habilitados para combinaciones de 18,6 metros y 45 toneladas, no soluciona nada: lo fuerza a detenerse en bermas peligrosas o a seguir rodando en infracción. La innovación abandona el temporizador pasivo e implementa un sistema socio-técnico de acompañamiento predictivo del descanso, que cruza la cinemática del camión con la curva biológica de alerta circadiana y un catálogo georreferenciado y calificado de paradores de carga pesada.

**Tecnología que la sustenta.** Motor predictivo embebido a bordo en \textit{audIT EdgeHub} (RT-06.01), que evalúa en tiempo real el tiempo de conducción acumulado, la topografía del tramo siguiente y la ventana de mínima alerta circadiana (\textit{Window of Circadian Low}, 02:00 a 06:00 h). Catálogo georreferenciado local estructurado en SQLite WAL sobre memoria flash industrial ($\ge 8\text{ GB}$, RT-08.11), que califica capacidad geométrica de estacionamiento, servicios de higiene, duchas, agua potable y seguridad perimetral. Enclavamiento cinético estricto de pantalla ante cualquier movimiento ($v > 0\text{ km/h}$ o freno de mano liberado, conforme a la Ley N.º 21.377), con entrega de sugerencias mediante síntesis vocal local pasiva (TTS offline en español por altavoz vehicular, RT-16.21) sin exigir desviar la mirada ni admitir interacción táctil en marcha (RT-13.08). En modo detenido, interfaz ergonómica con guantes pesados (botones $\ge 60\times 60\text{ mm}$ e iluminación ámbar de alto contraste).

**Lo que agrega sobre lo que las bases ya exigen.** El cálculo reactivo de distancia al lugar seguro de detención (RT-09.01, RF-027), la autenticación sin manipulación (RT-12.11), la interfaz para guantes sin interacción en marcha (RT-13.08) y la resiliencia desconectada de 72 horas (RT-17.01) constituyen el alcance base comprometido y no se presentan como innovación. Lo que agrega esta ficha son tres elementos: (1) la anticipación predictiva circadiana, que sugiere pausas preventivas antes de que el conductor ingrese a tramos críticos sin infraestructura o enfrente el valle biológico de microsueño de madrugada (disparador del accidente del 14 de febrero de 2026), (2) la ontología, gobernanza y sincronización OTA en terminales de un catálogo calificado para camiones de 45 toneladas con servicios dignos de descanso, y (3) un modelo social y ergonómico no punitivo para los 258 conductores externos subcontratados (Restricciones 1 y 2, Ley N.º 20.123), transformando una herramienta de control patronal en un asistente de seguridad y bienestar.

**Madurez.** Escala de madurez tecnológica de uno a nueve (ISO, 2013). El hardware telemático de borde, almacenamiento SQLite WAL, TTS local y enclavamiento cinético están en nivel ocho, con componentes comerciales de uso maduro en flotas pesadas. El modelo predictivo circadiano y la ontología de paradores adaptada a la red vial chilena se sitúan en nivel siete, demostrados en entorno operacional representativo de la Ruta 5 y pasos cordilleranos, apoyados en estándares de ergonomía vehicular (ISO, 2017; ISO, 2019), investigación de fatiga en transporte de carga (FMCSA, 2020) y normativa vial nacional (Congreso Nacional de Chile, 2021; Ministerio del Trabajo, 2003).

**Incorporación en la arquitectura y en el cronograma.** Se articula en la Capa 1 (Borde Terrestre: motor predictivo a bordo, catálogo local SQLite y síntesis TTS), Capa 4 (Servicio de Gobernanza de Paradores y Seguridad Vial en la Torre de Control) y Capa 7 (Portal para consulta pasiva). Su trazabilidad comprende los paquetes EDT 2.4 (Diseño Ergonómico UI/UX y Protocolo Guantes, Meses 4 a 7), EDT 3.7 (Catálogo de Paradores en Campaña de Cobertura RT-03.24, Meses 3 a 6), EDT 4.6 (Software de Enclavamiento Cinético y Alerta Circadiana, Meses 7 a 10) y EDT 7.2 (Validación Operacional en Marcha Blanca con Conductores Reales, Meses 13 a 15). El beneficio es verificable antes del mes 16, cumpliendo RT-26.08.

**Impacto económico.** La inversión requerida es incremental sobre el software de borde (280 horas-hombre de desarrollo) y talleres ergonómicos participativos, mientras que el levantamiento del catálogo se absorbe dentro del recorrido de la campaña de medición de cobertura (RT-03.24) sin costo logístico adicional. En costo operacional genera un ahorro estimado de 1,2 % en combustible nocturno de larga distancia al eliminar la búsqueda errática de estacionamiento en ruta. El beneficio central radica en la mitigación del riesgo de siniestros graves por microsueño (cuyo costo supera \$150 millones por evento e induce paralización de clientes) y la supresión de multas por Ley No Chat y Art. 25 bis.

**Indicador de verificación.** Línea base cero de alertas con parador calificado garantizado, con meta de $\ge 98\text{ %}$ de efectividad en ruta nacional medida mensualmente en marcha blanca. Cero eventos de interacción táctil con vehículo en movimiento ($v > 0\text{ km/h}$, meta 100 % de bloqueo cinético). Carga cognitiva NASA-TLX con guantes reducida a $< 35$ puntos (desde 68 puntos de línea base). Y adherencia voluntaria de paradas seguras en conductores externos de $\ge 85\text{ %}$ (frente al 22 % actual).

**Riesgo de adopción.** Que los 258 conductores externos perciban el sistema como vigilancia patronal encubierta, con probabilidad media-alta e impacto alto. Se mitiga mediante diseño ergonómico participativo en horario de relevo en los cinco terminales y orientando la herramienta al bienestar (recomendación de sitios con duchas, seguridad y convenios comerciales). La contingencia es que la unidad a bordo conmuta a notificación puramente acústica pasiva por altavoz ambiental, sin requerir teléfonos personales ni botones adicionales en cabina, manteniendo la seguridad activa sin fricción sindical.

**Investigación adicional requerida.** La validación de los paradores seguros y sus atributos geométricos y sanitarios se consolida durante la campaña de cobertura de la Etapa 1. La calibración fina de la ventana circadiana con las familias de turnos reales de Curimón se ajusta en los talleres de diseño ergonómico del mes cuatro.


### Estado de elaboración y responsables


El reparto de responsabilidades quedó ratificado el 6 de septiembre de 2026. Las fichas tipo 1 y
tipo 4 corresponden a la dupla del subdocumento 3, la tipo 2 a la dupla del subdocumento 4, la tipo
3 a la dupla de los subdocumentos 4.1 y 5, y la tipo 5 a la dupla de los subdocumentos 1 y 2.


### Trazabilidad con el resto de la propuesta


Ninguna de las cinco es una funcionalidad que las bases ya exijan. Las tipo 2, 3 y 5 se apoyan en
componentes de la arquitectura descritos en el subdocumento 4. La tipo 1 se apoya en el motor de
costeo del subdocumento 5. La tipo 4 es contractual antes que técnica, y su viabilidad determina
cuántas unidades del parque llegan a intervenirse.

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
