# FORMULACIÓN DE PROYECTOS

# BASES TÉCNICAS TRANSVERSALES PARA LA PREPARACIÓN DE LA PROPUESTA Versión 1.0 Fecha Documento: 18-08-2026

# Bases Técnicas Transversales

Requisitos técnicos comunes a las trece industrias del llamado

Asignatura Ámbito Versión Objeto Unidad Profesor Documento Documento académica complementario base Taller Antonio Escuela Requisitos Las Bases Bases 1.0 trece - Técnicas de Administrativas agosto de Moya Formulación industrias de Informática, de amuitoctura, Villegas del 2026 caso del de TFEP-01/2026 - llamado, Pontificia asignado Proyectos antonio.moya infraestructura, sin a Universidad cada Informáticos excepción (FEPO1.26) O empresa pucv.cl calidad, Católica - proponente IC1-5444 operación de Valparaíso y presentación exigibles a toda solución ofertada

Este documento fija el piso técnico común del llamado. Todo lo que aquí se exige es exigible en las trece

industrias; Los requisitos lo que están cada codificados industria tiene como de RT-CC.NN propio -su y deben proceso responderse de negocio, uno sus a volúmenes, uno en el Formulario sus integraciones T-12 de y las su Bases regulación Administrativas. sectorial - se establece en las Bases Técnicas de cada caso.

Bases Técnicas Transversales TFEP-01/2026 1/51

# CONTENIDO

Objeto, ámbito, relación con los demás documentos, régimen de

HI \| II - - Disposiciones - Arquitectura Infraestructura de del la documento solución desastres, premise,. ambientes hardware, y puestos entrega de continua, trabajo datos, y equipamiento integración de y 2-5 6-8 1 cumplimiento analítica. y forma de responder. Site Modelo principal multicapa on-premise, de referencia, site secundario modelo híbrido y recuperación de nube ante y on- terreno.

Desempeño y capacidad, disponibilidad y resiliencia, seguridad, IV - Requisitos no funcionales identidad, usabilidad y accesibilidad, observabilidad, sostenibilidad 9-15 y certificaciones.

Módulos obligatorios en toda industria, canales digitales y

V - Capacidades transversales. NA, N. ns 16-18 movilidad, inteligencia artificial y automatización. VI - Proyecto, implantación y Gobierno del proyecto, pruebas y criterios de aceptación, modelo 19-22 operación de operación, mesa de ayuda, mantención y capacitación... e Presencia digital del proponente, video de presentación, prototipo VII - Exigencias de presentación E prop h h h 23-26 interactivo de interfaz e innovaciones.

Índice de requisitos, plantilla de volumetría, checklist de VII - Anexos q \>, A-D entregables y glosario. Cómo se articula este documento con los demás

| LasBasesAdministrativasgobiernanelprocesoyelcontrato:quiénparticipa,quégarantíasrinde,cómose | evalúa,quéplazosrigenyquésepenaliza.SuCapítulo4enuncialosrequisitostransversalesenelnivelde | exigenciacontractual. |
|:--- |:--- |:--- |
| EstedocumentodesarrollatécnicamenteeseCapítulo4ylollevaalnivelderequisitoverificable.Dondelas | BasesAdministrativasdicen«lasolucióndeberáteneraltadisponibilidad»,aquísedicecuál,medidacómo, | probadacuándoyacreditadaconquéevidencia. |
| LasBasesTécnicasdecadacaso,quesepublicanporseparado,aportanelcontextodelaindustria,elproceso | denegocio,losrequerimientosfuncionales,lavolumetríarealylosvaloresconcretosdetodorequisito | marcado«Segúncaso»enestedocumento. |

Este documento desarrolla técnicamente ese Capítulo 4 y lo lleva al nivel de requisito verificable. Donde las Bases Administrativas dicen «la solución deberá tener alta disponibilidad», aquí se dice cuál, medida cómo, probada cuándo y acreditada con qué evidencia.

Las Bases Técnicas de cada caso, que se publican por separado, aportan el contexto de la industria, el proceso de negocio, los requerimientos funcionales, la volumetría real y los valores concretos de todo requisito marcado «Según caso» en este documento.

Sobre Este pliego el nivel describe de exigencia. una plataforma de misión crítica, no un sistema de gestión convencional. Los umbrales, los estándares y los controles que contiene son los que hoy se exigen en el mercado a un proveedor que opera la infraestructura digital de una empresa. Una propuesta que los trate como formalidades a declarar, en lugar de como decisiones de ingeniería a resolver, quedará en evidencia en la matriz de cumplimiento y en la defensa técnica.

Bases Técnicas Transversales TFEP-01/2026 2/51

# DISPOSICIONES DEL DOCUMENTO

# CAPÍTULO 1 - OBJETO, ÁMBITO Y RÉGIMEN DE CUMPLIMIENTO

1.1 Objeto Las presentes Bases Técnicas Transversales establecen los requisitos técnicos, de infraestructura, de calidad, de operación y de presentación que toda solución ofertada en la Licitación N\* TFEP-01/2026 debe satisfacer,

con independencia de la industria y del caso asignado a cada empresa proponente.

El propósito de este documento es doble. Primero, fijar un piso técnico común y exigente que impida que la comparación entre ofertas se distorsione por diferencias de interpretación sobre qué es una plataforma de misión crítica. Segundo, liberar a las Bases Técnicas de cada caso de repetir aquello que es común, permitiéndoles concentrarse en lo que efectivamente distingue a una industria de otra: su proceso de negocio,

sus volúmenes, sus integraciones, sus regulaciones sectoriales y sus criterios de aceptación propios.

## 1.2 Ámbito de aplicación

Este documento aplica íntegramente a los trece casos del llamado:

Minería - extracción de recursos Sala de cine - entretenimiento 2 Logística - empresa distribuidora 9 Cadena multitienda - retail 3 Servicios de agua potable - utilities 10 \| Transporte de carga 4 Consultas médicas - salud y bienestar 11 \| Servicios financieros - banca, seguros y cambio 5 Cadena de hoteles - turismo y hospitalidad 12 \| Agroindustria 6 Portuaria - operación marítima comercial 13 \| Telecomunicaciones

Servicio de puerto deportivo - recreación marítima

1.3 Relación con los demás documentos del proceso

Este documento se lee conjuntamente con las Bases Administrativas y con las Bases Técnicas del caso,

conforme al orden de precedencia del Artículo 5\* de las Bases Administrativas.

Reglas del proceso, participación, garantías, evaluación, adjudicación, contrato, niveles de servicio contractuales, penalidades y exigencia de innovación. Incluye el cronograma obligatorio de 56 meses (Art. 17") y los requisitos transversales de nivel contractual (Capítulo 4).

Prevalecen sobre este documento en materias administrativas y contractuales. Bases Administrativas TFEP-01/2026 Desarrolla técnicamente el

Bases Técnicas Cómo debe estar construida, desplegada, protegida,, » E. uu Capítulo 4 de las Bases Transversales (este operada y presentada la solución, en términos técnicos -. e.. Administrativas. No lo documento) verificables y comunes a las trece industrias. contradice ni lo rebaja.

Bases Técnicas Transversales TFEP-01/2026 3/51 Puede endurecer cualquier

Contexto de la industria, proceso de negocio, requisito de este. requerimientos funcionales, volúmenes reales, documento; nunca Bases Técnicas del caso,,,,,, integraciones, normativa sectorial, ventana operacional y rebajarlo. Aporta los valores criterios de aceptación propios del caso. de los requisitos marcados «Según caso». 1.4 Régimen de cumplimiento

Los requisitos de este documento se identifican con un código de la forma RT-CC.NN, donde CC es el número del capítulo y NN el correlativo dentro de él. Cada requisito tiene un carácter: Significado Efecto en la evaluación

Su incumplimiento o su omisión producen puntaje cero en el ítem afectado. El incumplimiento de un requisito obligatorio de seguridad, continuidad o arquitectura habilita la exclusión conforme al Artículo 58\* de las Bases Administrativas. Requisito de cumplimiento forzoso. La

Obligatorio " o la 2 solución no es admisible sin él.

Requisito que el CLIENTE valora pero no Deseable exige. Diferencia una oferta buena de una oferta destacada.

Su cumplimiento acreditado otorga puntaje adicional dentro del ítem. Su ausencia no penaliza.

| Sefija,evalúarigeelcontravalorporelvalordefectodelcaso.queesteSieldocumentocasonolo | indiquey,ensudefecto,elcriteriodelaComisión | Evaluadora. |
|:--- |:--- |:--- |
| Requisitoobligatoriocuyovalornumérico, | SegúncasoumbraloalcanceconcretolofijanlasBases | Técnicasdelcaso. |
| 1.51.CómoSicumple,debecumpleresponderseparcialmenteestedocumentoonocumple. | ElPROPONENTEdeberáacreditarelcumplimientodelatotalidaddelosrequisitosenelFormularioT-12,Matriz | deCumplimientoTécnicoyTrazabilidad,indicandoporcadacódigoRT: |

Requisito obligatorio cuyo valor numérico, Según caso umbral o alcance concreto lo fijan las Bases Técnicas del caso.

1.5 1. Cómo Si cumple, debe cumple responderse parcialmente este documento o no cumple. El PROPONENTE deberá acreditar el cumplimiento de la totalidad de los requisitos en el Formulario T-12, Matriz de Cumplimiento Técnico y Trazabilidad, indicando por cada código RT:

2. El componente, servicio, producto o práctica concreta con que lo satisface, individualizado por nombre y versión.

3. La sección y página de la Oferta Técnica donde se desarrolla.

4. La evidencia con que se verificará durante la ejecución: entregable, prueba, informe o certificado.

Declarar «cumple» sin individualizar el componente ni indicar dónde se desarrolla equivale a no declarar.

La Comisión Evaluadora no buscará en la propuesta la respuesta que el PROPONENTE no señaló, y calificará el requisito como no acreditado.

1.6 Neutralidad tecnológica y criterio de vigencia

Este documento no impone marcas, productos ni proveedores determinados. Cuando menciona un producto lo hace a título de referencia y admite equivalentes de prestaciones iguales o superiores, lo que el PROPONENTE deberá acreditar.

SÍ impone, en cambio, un criterio de vigencia. Todo componente ofertado - lenguaje, marco de trabajo, motor de base de datos, sistema operativo, biblioteca, dispositivo - deberá contar con soporte vigente del fabricante o de su comunidad al momento de la oferta, y con hoja de ruta de soporte que cubra, como mínimo, la totalidad

Bases Técnicas Transversales TFEP-01/2026 4/51

del período contractual de 56 meses. El PROPONENTE deberá declarar, por cada componente principal, su versión, su fecha de fin de soporte y su plan de actualización.

La obsolescencia programada de un componente durante la vigencia del Contrato no es un riesgo del

CLIENTE. Si un componente alcanza su fin de soporte antes del mes 56, la actualización o la sustitución es de cargo del ADJUDICATARIO y debe estar prevista y costeada en la oferta. 1.7 Interpretación de los umbrales

Todo umbral expresado en este documento es un mínimo exigido, salvo que se indique expresamente que constituye un máximo. Los tiempos de respuesta se entienden medidos en el percentil 95 sobre la experiencia

real del usuario final, y no como promedio ni como medición sintética de laboratorio, salvo indicación expresa.

Las mediciones de disponibilidad se calculan sobre la transacción de negocio completa de extremo a extremo.

La disponibilidad de la infraestructura subyacente no es un sustituto válido: un componente activo que devuelve errores no cuenta como disponible.

Bases Técnicas Transversales TFEP-01/2026 5/51

# ARQUITECTURA DE LA SOLUCIÓN

# CAPÍTULO 2 - MODELO DE ARQUITECTURA DE REFERENCIA

## 2.1 Modelo multicapa exigido

La solución deberá organizarse en las capas que se describen a continuación. Las capas son de existencia obligatoria; la tecnología con que se materializa cada una es decisión del PROPONENTE, que deberá justificarla. Presentación Borde y exposición

| Puertadeenlace | deservicios |
|:--- |:--- |
| Serviciosde | negocio |
| Integracióny | eventos | Servicios de negocio Integración y eventos Datos Seguridad transversal Observabilidad transversal

Interfaces de las personas usuarias: portal web, aplicación móvil, terminales operacionales y pantallas de terreno.

Único punto de entrada público: distribución de contenidos, balanceo, protección perimetral y terminación de cifrado.

Publicación, autenticación, autorización, cuotas, límites de tasa, versionado y observabilidad de las interfaces de programación.

| Lógicadelprocesodenegociodelcaso, | organizadaenmódulosconlímitesdecontexto | explícitos. |
|:--- |:--- |:--- |
| Comunicaciónasíncrona,desacoplamiento, | orquestaciónycoreografíadeprocesosentre | módulosyconsistemasexternos. |
| Persistenciatransaccional,analítica, | documental,deseriesdetiempoydearchivos, | segúnlorequieraelcaso. |

Comunicación asíncrona, desacoplamiento, orquestación y coreografía de procesos entre módulos y con sistemas externos.

Persistencia transaccional, analítica, documental, de series de tiempo y de archivos, según lo requiera el caso.

## Identidad, autorización, gestión de secretos, cifrado, registro de auditoría y detección.

Métricas, registros y trazas distribuidas correlacionadas.

## 2.2 Requisitos de arquitectura

La solución se organizará en las ocho capas del numeral 2.1. El PROPONENTE

| Diseñoadaptativo,accesibleysinlógicade | negocio.Ningunainterfazpodráacceder | directamentealabasededatos. |
|:--- |:--- |:--- |
| CDN,WAFgestionado,proteccióncontra | denegacióndeservicioencapas3,4y7,y | terminaciónTLS1.3. |
| Validacióndeesquema,inspeccióndecarga | útil,trazabilidadportransacciónycatálogo | deservicios. |
| Sinestado,desplegablesdeforma | independiente,concontratosversionadosy | compatibilidadhaciaatrás. |
| Busointermediariodemensajeríacon | persistencia,colademensajesfallidos, | reintentoydeduplicación. |
| Separaciónentrelotransaccionalylo | analítico.Cifradoenreposo.Respaldoy | retencióndeclarados. |

CDN, WAF gestionado, protección contra denegación de servicio en capas 3, 4 y 7, y terminación TLS 1.3.

Validación de esquema, inspección de carga útil, trazabilidad por transacción y catálogo de servicios.

Sin estado, desplegables de forma independiente, con contratos versionados y compatibilidad hacia atrás.

Bus o intermediario de mensajería con persistencia, cola de mensajes fallidos, reintento y deduplicación.

Separación entre lo transaccional y lo analítico. Cifrado en reposo. Respaldo y retención declarados.

Aplicada a todas las capas, no como capa perimetral única.

Instrumentación conforme a OpenTelemetry, cobertura de nube y onpremise sin puntos ciegos.

RT-02.01 RT-02.02 Se presentará rechazará el toda diagrama arquitectura de la arquitectura monolítica lógica que no identificando permita desplegar cada capa, de forma sus Obligatorio Obligatorio componentes y las interfaces entre ellas. La arquitectura será modular, con límites de contexto explícitos y acoplamiento débil. independiente sus componentes críticos.

Bases Técnicas Transversales TFEP-01/2026 6/51

La descripción de la arquitectura se ajustará a ISO/IEC/IEEE 42010, con vistas lógica,

REO de procesos, de despliegue, de datos y de seguridad.

RT-02.04 con la alternativa escogida, las alternativas descartadas y el criterio de decisión. El Obligatorio Obligatorio El registro PROPONENTE es entregable mantendrá contractual un registro y se actualizará de decisiones durante de arquitectura toda la ejecución. (ADR) fechado,

La capa de servicios de negocio será sin estado. El estado de sesión y el estado de

RT-02.05;. add proceso residirán en almacenes externos con alta disponibilidad.

Obligatorio Toda operación de escritura expuesta a reintentos será idempotente, con clave de

RT-02.06 s idempotencia declarada por el cliente y ventana de deduplicación documentada.

RT-02.07 consumidor y orden garantizado dentro de la partición o del agregado cuando el Obligatorio Obligatorio Los proceso flujos lo de exija. eventos garantizarán entrega al menos una vez, con deduplicación en el

La solución implementará patrones de resiliencia demostrables: reintento con retroceso exponencial y variación aleatoria, cortacircuitos, mamparos de aislamiento, límites de tasa y tiempo de espera explícito en toda llamada remota. No se admiten llamadas remotas sin tiempo de espera. RT-02.08 Obligatorio

| Lasolucióndegradarádeformaelegante:antelaindisponibilidaddeuncomponente | RT-02.09nocríticodeberácontinuaroperandoenmodoreducido,informandoladegradaciónObligatorio | alapersonausuaria,ynuncafallardeformatotal. |
|:--- |:--- |:--- |
| Lascapasdeaplicacióneintegraciónescalaránhorizontalmentedeforma | RT-02.10automática,conumbrales,límitessuperioresycostoasociadodeclaradosenlaObligatorio | oferta. |
| ElPROPONENTEdeclararáexplícitamentelospuntosúnicosdefallaquesubsistanen | RT-02.11suarquitecturayjustificaráporquésonaceptables.OmitirestadeclaracióncuandoObligatorio | existanpuntosúnicosdefallaseevaluarácomoobservacióngrave. |

Las capas de aplicación e integración escalarán horizontalmente de forma RT-02.10 automática, con umbrales, límites superiores y costo asociado declarados en la Obligatorio oferta.

El PROPONENTE declarará explícitamente los puntos únicos de falla que subsistan en RT-02.11 su arquitectura y justificará por qué son aceptables. Omitir esta declaración cuando Obligatorio existan puntos únicos de falla se evaluará como observación grave.

La solución admitirá su replicación a nuevas unidades, sitios, sucursales o filiales del

RT-02.12.: uu.. Según caso CLIENTE sin rediseño arquitectónico, mediante parametrización o multi-tenencia. 5 El PROPONENTE presentará un modelo de dominio del negocio del caso, con las.. RT-02.13 y NU. ú, E, e Obligatorio entidades principales, sus relaciones y los eventos de negocio que las modifican. Se valorará la aplicación documentada de patrones de arquitectura evolutiva que permitan sustituir un componente sin reescribir la solución: capa anticorrupción RT-02.14 Deseable

frente a sistemas heredados, estrangulamiento progresivo y abstracción de proveedores. 2.3 Estilo arquitectónico y su justificación

El CLIENTE no impone un estilo arquitectónico. Sí exige que el escogido sea explícito, coherente con la escala del caso y justificado. El PROPONENTE deberá comparar al menos dos alternativas y explicar por qué descarta la no elegida, considerando la complejidad operacional que introduce, el tamaño y las competencias del equipo, el costo de infraestructura y la capacidad del CLIENTE de operarla al término del Contrato.

Adoptar una arquitectura de microservicios para un caso cuyo volumen no la justifica es un error de

ingeniería y se evaluará como tal. La sofisticación no reemplaza a la pertinencia.

Bases Técnicas Transversales TFEP-01/2026 7/51

# CAPÍTULO 3 - MODELO HÍBRIDO: NUBE Y ON-PREMISE 3.1 Distribución de cargas

Conforme al Artículo 16% de las Bases Administrativas, la solución será obligatoriamente híbrida. El PROPONENTE deberá presentar una tabla de emplazamiento que asigne cada componente a nube o a onpremise y justifique la decisión.

Latencia tolerada por el proceso Superior a 100 ms Inferior a 50 ms o determinista El proceso debe continuar sin excepción Consecuencia de la pérdida de.. El proceso puede esperar conectividad P P P

Volumen y costo de transferencia de Alto volumen generado localmente Volumen moderado., datos (video, telemetría, sensores)

## Acoplamiento con equipamiento Directo: balanzas, PLC, lectores, Nulo o mediado por servicios

físico o Elasticidad Restricción custodia de regulatoria la demanda de residencia Muy. variable E. o estacional Constante Con en barreras, el restricción caso cámaras, y predecible sectorial básculas declarada i Sin restricción 3.2 Requisitos del componente en nube

El PROPONENTE declarará el proveedor de nube pública, la región primaria y la RT-03.01 región secundaria utilizadas. El proveedor deberá contar con presencia de región o Obligatorio zona en Chile o en Sudamérica.

Todos los componentes con requisito de alta disponibilidad se desplegarán en al

RT-03.02 Ñ E Obligatorio menos dos zonas de disponibilidad. No se aceptará un diseño en una sola zona. 5 La totalidad de la infraestructura se definirá como código, versionada en el repositorio del CLIENTE, revisable y reproducible. No se admite infraestructura.. RT-03.03 P y rep Obligatorio

creada manualmente por consola, salvo la cuenta raíz inicial, cuya creación deberá documentarse.

| Laredsesegmentaráporcapas,consubredesprivadasparaaplicaciónydatos,y | RT-03.04exposiciónpúblicarestringidaalacapadeborde.NingúncomponentededatosseráObligatorio | alcanzabledesdeInternet. |
|:--- |:--- |:--- |
| ElPROPONENTEprivilegiaráserviciosadministradosporsobreservicios | RT-03.05autoadministradoscuandoelloreduzcaelriesgooperacional,yjustificarácadaObligatorio | excepción. |
| SeaplicaránprácticasFinOps:etiquetadoobligatoriodetodoslosrecursospor | RT-03.06ambiente,móduloycentrodecosto;presupuestosconalertasdedesviación;yObligatorio | reportemensualdeconsumodesglosadoentregadoalCLIENTE. |
| ElPROPONENTEdeclararásuestrategiadereversibilidadydemitigacióndelbloqueo | RT-03.07porproveedor,identificandoquécomponentessonportables,cuálesnolosonycuálObligatorio | seríaelesfuerzoestimadodeunamigración. |
| Lasoluciónemplearáinstanciasreservadas,planesdeahorroocapacidad | RT-03.08comprometidacuandoelperfildecargalojustifique,yloreflejaráenlaestructuradeDeseable | costos. |

El PROPONENTE privilegiará servicios administrados por sobre servicios RT-03.05 autoadministrados cuando ello reduzca el riesgo operacional, y justificará cada Obligatorio excepción.

Se aplicarán prácticas FinOps: etiquetado obligatorio de todos los recursos por RT-03.06 ambiente, módulo y centro de costo; presupuestos con alertas de desviación; y Obligatorio reporte mensual de consumo desglosado entregado al CLIENTE.

El PROPONENTE declarará su estrategia de reversibilidad y de mitigación del bloqueo RT-03.07 por proveedor, identificando qué componentes son portables, cuáles no lo son y cuál Obligatorio sería el esfuerzo estimado de una migración.

La solución empleará instancias reservadas, planes de ahorro o capacidad RT-03.08 comprometida cuando el perfil de carga lo justifique, y lo reflejará en la estructura de Deseable costos.

Bases Técnicas Transversales TFEP-01/2026 8/51

Se valorará el uso de cómputo sin servidor o de contenedores administrados para las RT-03.09 cargas de perfil variable, con el análisis comparativo de costo frente a instancias Deseable permanentes.

3.3 Requisitos del componente on-premise y del borde operacional

| Elcomponenteon-premiseoperarádeformaautónomaydegradadaantelapérdida | RT-03.10totaldelenlaceconlanube,duranteunperíodomínimode24horascontinuasoelObligatorio | mayorquefijeelcaso. |
|:--- |:--- |:--- |
| Durantelaoperacióndesconectada,lasolucióncontinuaráregistrandolas | RT-03.11transaccionesoperacionalescríticasdeformalocal,conintegridadgarantizadaysinObligatorio | pérdidadedatos. |
| Restablecidoelenlace,lasincronizaciónseráautomática,conreconciliación | RT-03.12deterministadeconflictos,regladeresolucióndocumentadaybitácoraauditabledeObligatorio | lasdecisionesaplicadas. |
| ElPROPONENTEdeclararáquéfuncionesNOestarándisponiblesenmodo | RT-03.13desconectadoyquéprocedimientomanuallassuple.LaausenciadeestadeclaraciónObligatorio | seevaluarácomoobservacióngrave. |
| Losequiposon-premisecríticosseránredundantes.Elalmacenamientolocaltolerará | RT-03.14lafalladealmenosundisco;elPROPONENTEdeclararáelnivelRAIDescogidoyloObligatorio | justificaráfrentealasalternativas. |

Durante la operación desconectada, la solución continuará registrando las RT-03.11 transacciones operacionales críticas de forma local, con integridad garantizada y sin Obligatorio pérdida de datos.

Restablecido el enlace, la sincronización será automática, con reconciliación RT-03.12 determinista de conflictos, regla de resolución documentada y bitácora auditable de Obligatorio las decisiones aplicadas.

El PROPONENTE declarará qué funciones NO estarán disponibles en modo RT-03.13 desconectado y qué procedimiento manual las suple. La ausencia de esta declaración Obligatorio se evaluará como observación grave.

Los equipos on-premise críticos serán redundantes. El almacenamiento local tolerará RT-03.14 la falla de al menos un disco; el PROPONENTE declarará el nivel RAID escogido y lo Obligatorio justificará frente alas alternativas.

Los sistemas on-premise se endurecerán conforme a los CIS Benchmarks aplicables,

RT-03.15 e, E. Obligatorio con gestión centralizada de parches y ventana de aplicación acordada con el CLIENTE. El monitoreo del componente on-premise se integrará a la misma plataforma de +: RT-03.16... - Obligatorio observabilidad que la nube, con alertamiento unificado. El enlace entre el sitio on-premise y la nube será redundante, con caminos físicos y RT-03.17 proveedores distintos, y conmutación automática con tiempo de conmutación Obligatorio declarado.

Los dispositivos de borde y de terreno se administrarán de forma remota y RT-03.18 centralizada: inventario, configuración, actualización de firmware y de aplicación, Obligatorio bloqueo y borrado remoto.

Se valorará el procesamiento en el borde de las cargas que lo admitan -filtrado, RT-03.19 agregación previa, inferencia local- reduciendo el volumen transferido y la Deseable dependencia del enlace. 3.4 Conectividad y redes

El PROPONENTE dimensionará el ancho de banda requerido por sitio, en régimen RT-03.20 normal y en peak, y lo justificará con el cálculo de volumen de transacciones y de Obligatorio datos.

La conexión entre la red del CLIENTE y la nube se establecerá mediante enlace RT-03.21 privado dedicado o red privada virtual con cifrado, según lo que el volumen y la Obligatorio criticidad justifiquen.

Bases Técnicas Transversales TFEP-01/2026 9/51

El acceso remoto de las personas trabajadoras del CLIENTE, incluido el trabajo desde el hogar, se resolverá con acceso a la red de confianza cero, con verificación de postura del dispositivo. No se admite exponer servicios internos directamente a Internet. RT-03.22 Obligatorio

La red inalámbrica de los sitios operacionales, cuando el caso la requiera, contará con RT-03.23 segmentación por tipo de dispositivo, autenticación por certificado o credencial de Según caso empresa y cobertura verificada mediante estudio de sitio.

El PROPONENTE declarará la calidad de servicio y la priorización de tráfico aplicada a

RT-03.24.; " ". "E, las transacciones operacionales críticas frente al tráfico administrativo. Deseable

# CAPÍTULO 4 - AMBIENTES, ENTREGA CONTINUA Y GESTIÓN DE LA CONFIGURACIÓN 4.1 Ambientes obligatorios

Construcción y prueba unitaria por parte del Aislado. Datos sintéticos o anonimizados. Desarrollo:: ds equipo de desarrollo. Reconstruible desde código. QA Pruebas funcionales, de integración, de Aislado. Datos de prueba controlados y regresión y automatizadas. versionados. Reinicio a estado conocido. E Equivalente a producción en topología, e Pruebas de aceptación, de carga, de resiliencia. e. Preproducción » configuración y versiones. Volumen de y ensayo del paso a producción.. datos representativo. e » Acceso restringido y auditado. Sin acceso Producción Operación real. Í.. interactivo directo de desarrolladores. Recuperación ante Continuidad ante indisponibilidad de la región Replicación continua. Conmutación desastres o del sitio primario. probada semestralmente. 4.2 Requisitos de entrega continua

Los cinco ambientes del numeral 4.1 estarán habilitados y operativos como condición REDAOL del hito H3 del Formulario E-25.

## Obligatorio

Preproducción será equivalente a producción en topología, versiones de RT-04.02 componentes y configuración. Las diferencias que subsistan por costo se declararán Obligatorio expresamente y se justificarán.

El código residirá en un sistema de control de versiones con ramas protegidas,

RT-04.03 revisión obligatoria por pares y prohibición de escritura directa sobre la rama Obligatorio principal. Existirá trazabilidad completa entre requerimiento, incidencia, cambio de código + d RT-04.04. b,,, 50, Obligatorio prueba ejecutada y despliegue realizado. El flujo de integración continua ejecutará, como mínimo: compilación, pruebas unitarias, análisis estático de código, análisis de composición de software, escaneo de.. RT-04.05, \<o, h, Obligatorio

secretos y escaneo de imágenes de contenedor, con criterios de bloqueo automático del despliegue.

Bases Técnicas Transversales TFEP-01/2026 10/51

Los despliegues serán automatizados y reproducibles, con reversión automatizada y

RT-04.06 A e sin intervención manual en el paso a producción.

RT-04.07 canario o despliegue progresivo. Se declarará cuál se emplea y se demostrará en Obligatorio Obligatorio La Preproducción estrategia de antes despliegue de cada permitirá paso a producción. liberar sin interrupción del servicio: azul-verde,

| Todaconfiguraciónestaráexternalizadadelartefactoygestionadaporambiente.Un | RT-04.08mismoartefactodeberápoderpromoversedeQAaPreproducciónyaProducciónsinObligatorio | recompilación. |
|:--- |:--- |:--- |
| Lossecretosresidiránenungestordesecretosconrotaciónautomáticayauditoría | RT-04.09deacceso.Quedaprohibidatodacredencialembebidaencódigo,imágenesoObligatorio | archivosdeconfiguración. |
| Lasmigracionesdeesquemadebasededatosseránversionadas,reversiblesy | RT-04.10ejecutadasdeformaautomatizada,conestrategiadecompatibilidadquepermitaObligatorio | convivirdosversionesdelaaplicaciónduranteeldespliegue. |

Los secretos residirán en un gestor de secretos con rotación automática y auditoría RT-04.09 de acceso. Queda prohibida toda credencial embebida en código, imágenes o Obligatorio archivos de configuración.

Las migraciones de esquema de base de datos serán versionadas, reversibles y RT-04.10 ejecutadas de forma automatizada, con estrategia de compatibilidad que permita Obligatorio convivir dos versiones de la aplicación durante el despliegue.

La cobertura de pruebas automatizadas del código de lógica de negocio será de al

RT-04.11., menos 70 %, con umbral bloqueante en el flujo de integración continua.

RT-04.12 compromiso de código hasta producción, su tasa de cambios fallidos y su tiempo de Obligatorio Obligatorio El restauración, PROPONENTE y los declarará medirá durante su frecuencia la Operación. de despliegue objetivo, su tiempo desde el

Los ambientes no productivos se apagarán o reducirán fuera del horario de uso, con. Deseable el ahorro reflejado en la estructura de costos.

# RT-04.13

Se valorará la existencia de ambientes efímeros por rama o por incidencia, creados y RT-04.14 í des Deseable destruidos automáticamente.

# CAPÍTULO 5 - DATOS, INTEGRACIÓN E INTEROPERABILIDAD 5.1 Modelo y gestión de datos

| ElPROPONENTEentregaráelmodelodedatosdocumentadoyundiccionariode | RT-05.01datosconelnombre,eltipo,eldominiodevalores,laobligatoriedad,elpropietarioyObligatorio | lasensibilidaddecadaatributo. |
|:--- |:--- |:--- |
| ElPROPONENTEjustificarálaseleccióndelparadigmaydelmotordepersistencia: | RT-05.02relacionalonorelacional,garantíastransaccionales,ylaposiciónescogidaentreObligatorio | consistenciaydisponibilidadconformealteoremaCAP,paracadadominiodedatos. |
| Todaoperacióndenegocioserátrazable:lasoluciónpermitiráreconstruirquién, | RT-05.03qué,cuándo,desdequédispositivoyconquévaloresanterioresyposteriores,paraObligatorio | cualquierregistroyencualquiermomentodelperíododeretención. |
| RT-05.04Lapuntocalidaddecaptura,dedatosindicadoressegestionarádeconformecompletitud,aISO/IECexactitud25012,yconsistencia,convalidaciónytableroeneldeObligatorio | calidaddisponibleparaelCLIENTE. | Elalmacenamientotransaccionalyelanalíticoestaránseparados.Ningunaconsulta |

El PROPONENTE justificará la selección del paradigma y del motor de persistencia: RT-05.02 relacional o no relacional, garantías transaccionales, y la posición escogida entre Obligatorio consistencia y disponibilidad conforme al teorema CAP, para cada dominio de datos.

Toda operación de negocio será trazable: la solución permitirá reconstruir quién, RT-05.03 qué, cuándo, desde qué dispositivo y con qué valores anteriores y posteriores, para Obligatorio cualquier registro y en cualquier momento del período de retención.

RT-05.04 La punto calidad de captura, de datos indicadores se gestionará de conforme completitud, a ISO/IEC exactitud 25012, y consistencia, con validación y tablero en el de Obligatorio calidad disponible para el CLIENTE. El almacenamiento transaccional y el analítico estarán separados. Ninguna consulta

RT-05.05, - » Obligatori analítica podrá degradar el desempeño de la operación. igarono

Bases Técnicas Transversales TFEP-01/2026 11/51

La solución permitirá exportar la totalidad de la información del CLIENTE en formatos RT-05.06 abiertos y documentados, en cualquier momento del Contrato, sin costo adicional y Obligatorio sin intervención del ADJUDICATARIO.

El PROPONENTE declarará la política de retención, archivado y eliminación por cada RT-05.07 dominio de datos, coherente con la normativa aplicable al caso, e implementará un Obligatorio procedimiento verificable de eliminación segura.

sensibles Los El PROPONENTE datos que personales el caso presentará se identifique. tratarán una estrategia conforme al de Artículo gestión 85\* de datos de las maestros Bases que evite la.. RT-05.08 RT-05.09 Administrativas, Tu" con. seudonimización. o cifrado, a nivel de campo. para las categorías Obligatorio Obligatorio duplicación de entidades compartidas entre módulos y con sistemas externos. Se valorará la implementación de un catálogo de datos con linaje automatizado, que

- i Adi: Deseable permita rastrear el origen de cada indicador de negocio hasta su fuente.

# RT-05.10 5.2 Migración de datos

| ElPROPONENTEpresentaráunplandemigraciónconalcance,origen,volumen, | RT-05.11reglasdetransformación,criteriosdecalidad,estrategiadeejecuciónyplandeObligatorio | reversión. |
|:--- |:--- |:--- |
| Lamigraciónincluiráunaetapadeperfiladoysaneamientoprevio,coninformede | RT-05.12losdefectosdetectadosenlosdatosdeorigenyladecisiónadoptadasobrecadaObligatorio | uno. |
| SeejecutaránalmenosdosensayoscompletosdemigraciónsobrePreproducción | RT-05.13antesdelamigracióndefinitiva,conmedicióndeltiempototalydelresultadodelaObligatorio | conciliación. |

La migración incluirá una etapa de perfilado y saneamiento previo, con informe de RT-05.12 los defectos detectados en los datos de origen y la decisión adoptada sobre cada Obligatorio uno.

Se ejecutarán al menos dos ensayos completos de migración sobre Preproducción RT-05.13 antes de la migración definitiva, con medición del tiempo total y del resultado de la Obligatorio conciliación.

La conciliación posterior a la migración será cuantitativa y verificable: recuentos,

RT-05.14 sumas de control y muestreo dirigido. Toda diferencia deberá quedar explicada.

## Obligatorio

Los datos históricos que no se migren quedarán accesibles en un repositorio de RT-05.15 q,: q.. e Según caso consulta durante el período de retención que fije el caso.

## 5.3 Integración e interoperabilidad

Los servicios síncronos se documentarán en OpenAPI 3.1 y los flujos dirigidos por RT-05.16 eventos en AsyncAPI 2.6 o superior. La documentación se generará desde el código y Obligatorio se mantendrá actualizada automáticamente.

Los contratos de interfaz se versionarán semánticamente, con compatibilidad hacia

RT-05.17: e,, 7, atrás y política de obsolescencia con preaviso mínimo de seis meses.

RT-05.18 autenticación mutua TLS. Queda prohibida la autenticación por clave estática en la Obligatorio Obligatorio La ruta autenticación de la dirección entre web. sistemas empleará OAuth 2.1 con credenciales de cliente o

Toda integración registrará la transacción de entrada y de salida, con identificador de RT-05.19 correlación común que permita seguir una operación de negocio a través de todos Obligatorio los sistemas involucrados.

Bases Técnicas Transversales TFEP-01/2026 12/51

Las integraciones con sistemas heredados o de terceros se aislarán mediante una RT-05.20 capa anticorrupción, de modo que un cambio en el sistema externo no propague su Obligatorio modelo al núcleo de la solución.

El PROPONENTE declarará, por cada integración, el modo (síncrono o asíncrono), el RT-05.21 volumen esperado, la ventana de disponibilidad del sistema contraparte y el Obligatorio comportamiento de la solución cuando ese sistema no responde.

La solución soportará la carga y descarga masiva de información en formatos RT-05.22 abiertos, con validación previa, informe de errores por registro y procesamiento Obligatorio parcial. Se emplearán los estándares sectoriales de intercambio que las Bases Técnicas del, RT-05.23. " Según caso caso identifiquen. Se valorará la publicación de un portal de servicios para desarrolladores con RT-05.24 documentación navegable, ambiente de pruebas y credenciales de prueba Deseable autoservidas. 5.4 Analítica e inteligencia de negocio

La solución proveerá una capa analítica con tableros operacionales y de gestión,

RT-05.25 RT-05.26 RT-05.27 propias El CLIENTE del podrá caso, y construir profundizar sus propios desde el informes indicador sin.-- agregado intervención hasta del la transacción ADJUDICATARIO,, de Obligatorio Obligatorio Obligatorio construidos origen. sobre los indicadores que las Bases Técnicas del caso definan. 5 Los tableros permitirán filtrar por período, unidad organizacional y dimensiones

mediante una herramienta de autoservicio con modelo semántico documentado.

Todo informe será exportable en formatos abiertos y programable para envío,, RT-05.28 e. Obligatorio automático por calendario.

La latencia máxima entre la ocurrencia de una transacción y su disponibilidad en la

RT-05.29 RT-05.30 con el modelo,.". sus ¿ variables, " su métrica de desempeño y su plan: de reentrenamiento Según Deseable caso capa analítica será la que fije el caso y, en su defecto, no superará las 4 horas. Se valorará la incorporación de analítica predictiva pertinente al proceso del caso, documentados.

Bases Técnicas Transversales TFEP-01/2026 13/51

# INFRAESTRUCTURA

# CAPÍTULO 6 - SITE PRINCIPAL ON-PREMISE

6.1 El PROPONENTE Alcance y dimensionamiento deberá habilitar un proporcional recinto técnico para el alojamiento de los servidores, el almacenamiento y los equipos de telecomunicaciones que soportan la operación on-premise del CLIENTE, con un nivel de disponibilidad de infraestructura de 99,95 %. El recinto se emplazará en el espacio físico que proporcione el CLIENTE, cuya ubicación y superficie se establecen en las Bases Técnicas del caso.

Las exigencias de este capítulo se aplican de manera proporcional a la escala del componente on-premise que el caso requiera:

El caso requiere cómputo, almacenamiento y o Se aplican integramente los

Sala técnica principal rocesamiento sustantivos en las instalaciones del princi " requisitos RT-06.01 a RT-06.24. CUENTE. Se aplican los requisitos de energía, Sala técnica Sitios operacionales que requieren cómputo local climatización, control de acceso, secundaria o de sitio para continuidad, pero no albergan el núcleo. detección de incendio y monitoreo, dimensionados al sitio. Se aplican los requisitos de. -.. " protección eléctrica, control de Gabinete o borde Puntos de operación con equipamiento mínimo: na. ' De o acceso físico, monitoreo remoto y operacional pórtico, muelle, sala de máquinas, sucursal, faena. condiciones ambientales del equipo.

El PROPONENTE deberá declarar expresamente qué tipología adopta en cada sitio del caso y justificar el

dimensionamiento. Sobredimensionar el recinto es tan penalizado como subdimensionarlo: ambos revelan que el cálculo de capacidad no se hizo. 6.2 Requisitos de obra y habilitación

El espacio asignado será de uso exclusivo de la solución y estará aislado de otras

RT-06.01 dependencias del CLIENTE, con acceso independiente.

## Obligatorio

RT-06.02 Los muros no estructurales del recinto contarán con blindaje perimetral; el Obligatorio - PROPONENTE especificará el material y la resistencia. E El PROPONENTE entregará el plano de distribución interna del recinto, con la RT-06.03 separación de las zonas de generadores, baterías, climatización, servidores, Obligatorio comunicaciones, trabajo y respaldo.

El piso técnico, la canalización, el cableado estructurado y el etiquetado se ejecutarán

RT-06.04 e conforme a norma, con documentación de la certificación de cada enlace.

## Obligatorio

Bases Técnicas Transversales TFEP-01/2026 14/51

Los racks de servidores serán independientes de los racks de equipos de

RT-06.05 comunicación. Se declarará la ocupación proyectada de cada rack y su margen de Obligatorio crecimiento. La obra civil de separación de las instalaciones es de cargo del CLIENTE; su RT-06.06 A UD - Obligatorio especificación técnica y su coordinación son de cargo del PROPONENTE. E 6.3 Energía

| Elsuministroeléctricodelosequiposseráininterrumpido,consistemade | RT-06.07alimentaciónininterrumpidadimensionadoparaunaautonomíamínimade30Obligatorio | minutosaplenacarga. |
|:--- |:--- |:--- |
| Lacapacidaddegeneraciónautónomaaseguraráunrangomínimode24horas | RT-06.08continuasdeoperación,conestanquedecombustibledimensionadoycontratodeObligatorio | reabastecimientodeclarado. |
| Lainstalacióneléctricadelrecintoseráindependientedeladelrestodeledificioy | RT-06.09cumplirálanormativaeléctricachilenavigente,incluidalaNChElec.2777sobreObligatorio | sistemasdepuestaatierra. |

La capacidad de generación autónoma asegurará un rango mínimo de 24 horas RT-06.08 continuas de operación, con estanque de combustible dimensionado y contrato de Obligatorio reabastecimiento declarado.

La instalación eléctrica del recinto será independiente de la del resto del edificio y RT-06.09 cumplirá la normativa eléctrica chilena vigente, incluida la NCh Elec. 2777 sobre Obligatorio sistemas de puesta a tierra.

Se efectuará revisión y medición semestral de las instalaciones eléctricas del recinto, RT-06.10 con informe entregable al CLIENTE.

## Obligatorio

El PROPONENTE declarará la carga eléctrica proyectada en kW, el factor de potencia.. RT-06.11 en,:. Obligatorio y la eficiencia en el uso de la energía (PUE) estimada del recinto.

Se valorará la redundancia de alimentación en configuración 2N o N+1 con doble RT-06.12 - "e td Deseable acometida y transferencia automática. 6.4 Climatización y condiciones ambientales

Se dentro El recinto monitorearán de contará los rangos en con línea que climatización recomienda la temperatura, de el precisión fabricante la humedad para del operación y equipamiento. la presencia continua, de agua, con.. RT-06.13 RT-06.14 redundante N en i configuración N+1,: con control de temperatura le. y de humedad: relativa Obligatorio Obligatorio alertamiento integrado a la plataforma de observabilidad. El PROPONENTE declarará la estrategia de contención de pasillo frío o caliente y su

lr "" Deseable efecto en la eficiencia energética.

# RT-06.15 6.5 Detección y extinción de incendios

El recinto contará con detección temprana por aspiración de aire con tecnología RT-06.16 Mo - proa porasa el Obligatorio láser, tipo AnaLASER o equivalente de prestaciones iguales o superiores.

La extinción será automática mediante agente limpio tipo FM-200 o equivalente, con

RT-06.17 e, A aprobación UL e instalación conforme a norma NFPA.

## Obligatorio

Se proveerá un sistema secundario de extintores portátiles habilitados, con.. RT-06.18 » e Obligatorio mantención y certificación vigentes.

Bases Técnicas Transversales TFEP-01/2026 15/51

El sistema de detección y extinción se integrará al monitoreo en línea y notificará al RT-06.19 NOC y a la contraparte del CLIENTE.

## Obligatorio 6.6 Seguridad física y control de acceso

El ingreso al recinto se controlará mediante seguridad física y control de acceso RT-06.20 biométrico basado principalmente en biometría facial, con AFIS como respaldo. Se Obligatorio admite proponer sistemas de mayor seguridad.

Todo ingreso y egreso quedará registrado en una bitácora auditable, con RT-06.21 identificación de la persona, fecha, hora y motivo, conservada por el período de Obligatorio retención declarado.

Entre el acceso principal y el término del pasillo de la zona de control se dispondrá un espacio para la atención de personas en proceso de enrolamiento. Se evaluará mejor

RT-06.22,, ».,,, Obligatorio la existencia de una estación de enrolamiento fuera de las instalaciones del recinto técnico. Al término del pasillo se instalará un acceso que impida el paso de más de una, i RT-06.23 Obligatorio

persona a la vez, con nueva verificación de identidad previa al ingreso.

El recinto contará con videovigilancia y monitoreo IP, con imágenes en línea y RT-06.24 disponibles para visualización de al menos los últimos 30 días. Las grabaciones Obligatorio anteriores se respaldarán en un medio secundario recuperable y auditable.

El PROPONENTE declarará el procedimiento de acceso de terceros -fabricantes,

RT-06.25, Pai;: 1 mantenedores, auditores- con acompañamiento obligatorio y registro.

## Obligatorio 6.7 Respaldo y custodia de medios

Se habilitará un servicio de custodia de medios de respaldo para el sitio primario, en RT-06.26 un medio físico transportable a otro lugar cuando el CLIENTE lo determine. Se admite Obligatorio proponer una solución más segura y eficiente, debidamente justificada.

El recinto de custodia cumplirá exigencias de luminosidad, humedad, ventilación y

RT-06.27 cualquier otro factor que pueda afectar la calidad y la disponibilidad de los medios.

## Obligatorio

Se llevará un inventario de medios con rotación, verificación periódica de legibilidad.. RT-06.28. E. Obligatorio Y registro de todo movimiento de entrada y de salida.

## 6.8 Espacio de operación del personal

El PROPONENTE habilitará el espacio físico necesario para el personal encargado de la operación y administración de la plataforma, con estaciones de trabajo, telefonía,

RT-06.29 RT-06.30 b " o - i: MUpos Narea tu Obligatorio Obligatorio conexión a Internet y todo elemento que permita realizar la labor en condiciones adecuadas. El espacio de operación estará separado de la sala de equipos y no requerirá el

ingreso al recinto técnico para las labores habituales de operación.

Las instalaciones sanitarias, las zonas de seguridad ante emergencia y las áreas RT-06.31 exteriores existentes en el edificio del CLIENTE podrán utilizarse y no deben Obligatorio implementarse nuevamente. El PROPONENTE declarará de cuáles hará uso.

Bases Técnicas Transversales TFEP-01/2026 16/51 6.9 Rutas de comunicaciones

RT-06.32 El El N acceso PROPONENTE a las. redes proveerá de comunicaciones toda N. la conectividad, estará provisto la seguridad a través y las de canalizaciones, rutas físicas Obligatorio.. distintas, con ingreso al edificio por puntos separados.

| RT-06.33Ud.,,, | cañeríasoductosrequeridosparacumplirlosnivelesdeserviciocomprometidos. |
|:--- |:--- |
| Obligatorio | SeprivilegiaráalPROPONENTEqueofrezcaoproveaespecificacionesnuevaso |
|::;Deseable | mejoresquelasaquíestablecidas,debidamentefundamentadas. |

Obligatorio Se privilegiará al PROPONENTE que ofrezca o provea especificaciones nuevas o::; Deseable mejores que las aquí establecidas, debidamente fundamentadas.

# RT-06.34

# CAPÍTULO 7 - SITE SECUNDARIO Y RECUPERACIÓN ANTE DESASTRES

## 7.1 Configuración exigida

Complementariamente al sitio principal, el PROPONENTE deberá habilitar un sitio secundario en dependencias distintas, en modalidad activo-activo o activo-pasivo, con replicación de datos en línea para el ambiente de producción y características tecnológicas equivalentes a las del sitio principal en lo que respecta a los servicios críticos.

El PROPONENTE declarará la modalidad escogida -activo-activo o activo-pasivo- y RT-07.01 la justificará frente al costo, al RTO comprometido y a la complejidad operacional que Obligatorio introduce.

El sitio secundario estará emplazado a una distancia suficiente del principal para no RT-07.02 verse afectado por el mismo evento de fuerza mayor. El PROPONENTE declarará la Obligatorio distancia y el análisis de amenazas comunes considerado. La replicación de datos será continua, con medición y alertamiento del retraso de.. RT-07.03 A Obligatorio replicación. El objetivo de tiempo de recuperación (RTO) no superará 4 horas y el objetivo de RT-07.04 punto de recuperación (RPO) no superará 15 minutos para los servicios críticos, salvo Obligatorio exigencia superior del caso.

El procedimiento de conmutación estará documentado, automatizado en la mayor RT-07.05 medida posible y ejecutable por el personal del CLIENTE tras la transferencia de Obligatorio conocimiento.

Existirá un procedimiento de retorno al sitio principal igualmente documentado y

RT-07.06,:: probado, con reconciliación de los datos generados durante la contingencia.

## Obligatorio

El plan de recuperación ante desastres se probará al menos dos veces al año RT-07.07 mediante conmutación real, con informe de resultados, medición del RTO y del RPO Obligatorio efectivamente alcanzados y plan de corrección de las brechas detectadas.

Se valorará que la conmutación sea automática ante la detección de indisponibilidad, RT-07.08 i A. Deseable con criterio de disparo declarado y protección contra conmutación innecesaria. 7.2 Niveles de servicio de infraestructura Energía del recinto 99,95% Climatización 99,95%

Bases Técnicas Transversales TFEP-01/2026 17/51

Red y comunicaciones 99,95% Servidores y cómputo 99,95% Motor de base de datos 99,95% Portal y canales de atención 99,95% Transacción de negocio crítica de extremo a extremo 99,9 % (Artículo 78\* de las Bases Administrativas)

Los niveles de disponibilidad de infraestructura son un medio, no un fin. El compromiso contractual que se mide y se penaliza es el del Artículo 78" de las Bases Administrativas, sobre la transacción de negocio de extremo a extremo.

## 7.3 Respaldos

La política de respaldo seguirá el esquema 3-2-1-1-0: tres copias, en dos medios RT-07.09 distintos, una fuera de sitio, una inmutable o fuera de línea y cero errores de Obligatorio verificación de restauración.

Los respaldos estarán cifrados en reposo y en tránsito, con clave gestionada de forma

RT-07.10 independiente de la infraestructura respaldada.

RT-07.11 durante su período de retención, incluso frente a credenciales administrativas Obligatorio Obligatorio comprometidas. Las copias inmutables estarán protegidas contra borrado y contra modificación

Se ejecutará y documentará una prueba de restauración al menos mensual, sobre

RT-07.12. ie:: LA una muestra representativa, con medición del tiempo efectivo de restauración.

## Obligatorio

El PROPONENTE declarará, por cada dominio de datos, la frecuencia de respaldo, el: S RT-07.13, ». » Obligatorio período de retención y el tiempo estimado de restauración completa. Los respaldos permitirán la restauración granular: un registro, una tabla, un módulo o el sistema completo. RT-07.14 Deseable

# CAPÍTULO 8 - HARDWARE, PUESTOS DE TRABAJO Y EQUIPAMIENTO DE TERRENO

8.1 Infraestructura de cómputo, almacenamiento y red

RT-08.01 El referencia, PROPONENTE procesador, especificará memoria, el equipamiento almacenamiento de cómputo local, interfaces con su marca, y consumo, modelo junto de Obligatorio con el cálculo de dimensionamiento que lo sustenta. El almacenamiento será redundante, con tolerancia declarada a la falla de discos,

RT-08.02 Obligatorio control de errores y monitoreo predictivo de salud de los medios.:

Los conmutadores de núcleo, los cortafuegos y los balanceadores de carga estarán en.. RT-08.03: e: e:: d: 5 Obligatorio configuración de alta disponibilidad, sin punto único de falla.

Todo el equipamiento contará con fuentes de poder redundantes y conexión a

RT-08.04 ME. A. as circuitos eléctricos distintos.

## Obligatorio

Bases Técnicas Transversales TFEP-01/2026 18/51

# RT-08.05

# RT-08.06

El PROPONENTE declarará el margen de crecimiento del dimensionamiento propuesto, expresado como porcentaje sobre la carga proyectada del caso, y el Obligatorio procedimiento de ampliación.

El equipamiento será nuevo, sin uso previo, con garantía de fábrica vigente desde la E Obligatorio recepción conforme.

8.2 Puestos de trabajo de operación y de back office

# RT-08.07

# RT-08.08

# RT-08.09

El PROPONENTE especificará las estaciones de trabajo requeridas para la operación y la administración de la plataforma, en la cantidad que determine el Obligatorio dimensionamiento del caso, con monitores duales.

Los puestos de trabajo cumplirán las condiciones ergonómicas de la NCh 2527 y los;, E a Obligatorio equipos contarán con certificación de eficiencia energética.

Las estaciones estarán gestionadas de forma centralizada, con cifrado de disco, control de dispositivos extraíbles, antivirus con detección y respuesta y actualización Obligatorio automatizada.

8.3 Equipamiento de terreno y dispositivos operacionales

Conforme al Artículo 14.2 de las Bases Administrativas, la especificación técnica del hardware de terreno es de

cargo del PROPONENTE aunque su adquisición corresponda al CLIENTE.

# RT-08.10

# RT-08.11

# RT-08.12

# RT-08.13

# RT-08.14

# RT-08.15

El PROPONENTE especificará cada dispositivo de terreno con marca, modelo de referencia, cantidad, características mínimas, accesorios, consumibles y costo Obligatorio unitario estimado, aun cuando su compra sea de cargo del CLIENTE.

La especificación considerará las condiciones reales de uso del caso: intemperie, humedad, polvo, vibración, temperatura, uso con guantes, luminosidad y autonomía Obligatorio de batería requerida por turno.

Los dispositivos declararán su grado de protección contra polvo y agua y su.. y, proveerá una unidad de cada tipo de dispositivo especificado para Obligatorio Deseable resistencia a caídas, coherentes con el entorno de operación. El PROPONENTE indicará el ciclo de vida esperado de cada dispositivo, la disponibilidad de repuestos y el plan de reposición durante los 56 meses del Obligatorio Contrato. Los dispositivos se integrarán a la gestión centralizada de flota exigida en RT-03.18. Obligatorio El PROPONENTE a idad d da tipo de di ¡ti ificad

pruebas de aceptación por parte del CLIENTE, antes de la compra masiva.

8.4 Garantías, repuestos y niveles de reemplazo Hardware crítico

Soporte 24x7 con atención en sitio y compromiso de resolución en 4

horas. Hardware no crítico Soporte en horario hábil con compromiso de resolución en 24 horas. Software de base y de plataforma Soporte continuo del fabricante durante todo el período contractual.

Bases Técnicas Transversales TFEP-01/2026 19/51 Stock de repuestos Reemplazo de componente crítico en falla Dispositivos de terreno

Al menos 10 % del parque instalado por tipo de componente crítico, disponible en Chile.

Máximo 4 horas desde la confirmación del diagnóstico.

Stock de reemplazo en sitio equivalente al 10 % del parque, con configuración precargada. 8.5 Ciclo de vida y disposición final

# RT-08.16

# RT-08.17

# RT-08.18

# RT-08.19

El PROPONENTE presentará el plan de ciclo de vida del equipamiento: recepción,

e E.;: on Obligatorio puesta en servicio, mantención, actualización, retiro y disposición final.

Todo medio de almacenamiento que salga de servicio será borrado de forma segura, e Obligatorio y verificable, con certificado de destrucción o de sanitización entregado al CLIENTE. 5

La disposición final de equipamiento electrónico se realizará con gestor autorizado,. h M.. A o PeÉ Obligatorio conforme a la normativa de residuos aplicable, con certificado de disposición.

Se valorará una estrategia de reacondicionamiento o de extensión de vida útil que

i i dr Deseable reduzca el impacto ambiental, cuantificada en la propuesta.

Bases Técnicas Transversales TFEP-01/2026 20/51

# REQUISITOS NO FUNCIONALES

# CAPÍTULO 9 - DESEMPEÑO, CAPACIDAD Y ESCALABILIDAD 9.1 Umbrales de desempeño

Los siguientes umbrales son exigibles en producción, medidos en el percentil 95 sobre la experiencia real de la persona usuaria y bajo la carga de peak declarada en las Bases Técnicas del caso.

Carga inicial de una página del portal 2 segundos Navegación entre vistas ya cargadas 1 segundo Respuesta de una interfaz de programación de consulta simple 500 ms Respuesta de una interfaz de programación de escritura transaccional 800 ms

pu; eS Definido por el caso; en su defecto, 3 Transacción operacional crítica de terreno, de extremo a extremo

segundos Búsqueda con criterios compuestos 3 segundos Generación de un informe estándar en línea 30 segundos Procesamiento por lotes 10.000 registros por minuto Carga de un archivo de 100 MB 60 segundos Tiempo de arranque en frío de un servicio 60 segundos 9.2 Requisitos de capacidad y escalabilidad

segundo, El La PROPONENTE solución volumen soportará presentará de la datos concurrencia y el crecimiento cálculo y de el capacidad volumen anual, tomados de que transacciones sustenta de la volumetría su que fije del el caso. caso, RT-09.01 RT-09.02 dimensionamiento,. con los supuestos de usuarios. concurrentes, transacciones por Obligatorio Según caso y mantendrá los umbrales del numeral 9.1 bajo esa carga. La solución soportará, sin rediseño, un crecimiento de al menos tres veces la

RT-09.03 E. tias, volumetría inicial del caso en un horizonte de tres años.

## Obligatorio

RT-09.04 El El escalamiento PROPONENTE. de identificará las » capas el de componente aplicación o e integración que primero será se. convertirá horizontal en y automático, cuello de Obligatorio s con tiempo de reacción declarado y sin pérdida de transacciones en curso.

RT-09.05.., botella al crecer la carga y explicará cómo lo detectará y cómo lo resolverá.

RT-09.06 1,5 veces el peak declarado, y pruebas de estrés hasta identificar el punto de quiebre Obligatorio Obligatorio Se de ejecutarán la solución. pruebas de carga sobre Preproducción con un volumen equivalente a

El informe de pruebas de carga incluirá la curva de tiempo de respuesta frente a RT-09.07 carga, el punto de saturación, el consumo de recursos y el comportamiento durante y Obligatorio después del peak.

Bases Técnicas Transversales TFEP-01/2026 21/51

# RT-09.08

# RT-09.09

# RT-09.10

| Lasolucióndegradarádeformacontroladaalsuperarselacapacidad:encolamiento, | limitacióndetasaymensajeexplícitoalapersonausuaria,nuncaerrorgenériconiObligatorio | pérdidasilenciosadetransacciones. |
|:--- |:--- |:--- |
| SegestionarálacapacidaddurantelaOperaciónconproyeccióntrimestralde | crecimiento,alertasanticipadasdeagotamientoypropuestadeajustedeObligatorio | dimensionamientoydecosto. |
| Sevalorarálaexistenciadepruebasdecargaautomatizadasejecutadasdeforma | periódicaenelflujodeintegracióncontinua,condetecciónderegresionesdeDeseable | desempeño. |

Se gestionará la capacidad durante la Operación con proyección trimestral de crecimiento, alertas anticipadas de agotamiento y propuesta de ajuste de Obligatorio dimensionamiento y de costo.

Se valorará la existencia de pruebas de carga automatizadas ejecutadas de forma periódica en el flujo de integración continua, con detección de regresiones de Deseable desempeño.

# CAPÍTULO 10 - DISPONIBILIDAD, CONTINUIDAD Y RESILIENCIA

# RT-10.01

# RT-10.02

# RT-10.03

# RT-10.04

# RT-10.05

# RT-10.06

# RT-10.07

# RT-10.08

# RT-10.09

La solución alcanzará una disponibilidad mensual mínima de 99,9 % para los servicios clasificados como críticos, medida sobre la transacción de negocio de extremo a Obligatorio extremo.

El PROPONENTE clasificará cada servicio de la solución en crítico, alto, medio o bajo, justificando la clasificación con el impacto operacional de su indisponibilidad, y aplicará a cada uno el nivel de servicio correspondiente del Artículo 78\* de las Bases Administrativas.

## Obligatorio

El plan de continuidad del negocio se elaborará conforme a ISO 22301, con análisis de impacto en el negocio, escenarios de contingencia, procedimientos manuales de Obligatorio respaldo y criterios de activación.

La continuidad TIC se estructurará conforme a ISO/IEC 27031, articulada con el plan

», Obligatorio Deseable de recuperación ante desastres del Capítulo 7. 5 Los mantenimientos programados se ejecutarán fuera de la ventana operacional Serán caso crítica que defina el caso, con aviso previo mínimo de diez días hábiles.: La solución permitirá desplegar cambios sin interrupción del servicio. Las ventanas de obligatorio indisponibilidad programada serán excepcionales y deberán justificarse caso a caso. E Se ejecutarán pruebas de resiliencia mediante inyección controlada de fallas -caída de instancia, de zona, de dependencia externa, latencia elevada, saturación de oblizatorio disco- antes de cada paso a producción y al menos una vez por semestre durante la 5 Operación. El PROPONENTE documentará, por cada dependencia externa, el comportamiento de la solución cuando esa dependencia no responde, responde con error o responde Obligatorio con lentitud. Se declarará un presupuesto de error por servicio crítico y su vinculación con el ritmo de despliegue de cambios.

Bases Técnicas Transversales TFEP-01/2026 22/51

# CAPÍTULO 11 - SEGURIDAD DE LA INFORMACIÓN 11.1 Gobierno y modelo de seguridad

# RT-11.01

# RT-11.02

# RT-11.03

# RT-11.04

# RT-11.05

# RT-11.06

La arquitectura de seguridad se basará en el modelo Zero Trust conforme a NIST SP 800-207: verificación explícita de cada solicitud, privilegio mínimo y presunción de Obligatorio compromiso.

El PROPONENTE entregará un modelado de amenazas documentado por cada componente y por cada integración externa, con metodología declarada (STRIDE U Obligatorio otra), y lo actualizará ante cada cambio arquitectónico relevante.

La información del CLIENTE se clasificará por nivel de sensibilidad, con controles

Obligatorio diferenciados por nivel documentados en una matriz.:

Existirá un programa de gestión de vulnerabilidades con escaneo continuo y plazos máximos de remediación de 7 días corridos para vulnerabilidades críticas, 15 días Obligatorio para altas y 30 días para medias, contados desde su publicación o detección.

El PROPONENTE mantendrá una matriz de controles de seguridad trazable a ISO/IEC 27001 e ISO/IEC 27002, indicando el control, su implementación concreta en la Obligatorio solución y la evidencia que lo acredita.

Se aplicarán los controles de ISO/IEC 27017 para los servicios en nube y de ISO/IEC

Obligatorio 27018 para el tratamiento de datos personales en nube. 5 11.2 Protección de la capa expuesta

# RT-11.07

# RT-11.08

# RT-11.09

# RT-11.10

# RT-11.11

# RT-11.12

# RT-11.13

La publicación de servicios se realizará exclusivamente a través de la capa de borde, con red de distribución de contenidos, cortafuegos de aplicaciones web con reglas gestionadas y personalizadas, y protección contra denegación de servicio distribuida en capas 3, 4 y 7.

## Obligatorio

El cifrado en tránsito empleará TLS 1.3, con prohibición expresa de TLS 1.0 y 1.1, conjuntos de cifrado modernos, HSTS con precarga y gestión automatizada de Obligatorio certificados con rotación y alerta anticipada de vencimiento.

La totalidad de los datos en reposo estará cifrada, con claves gestionadas en un servicio de gestión de claves o en un módulo de seguridad de hardware, política de Obligatorio rotación declarada y separación de funciones en la custodia de claves.

Los datos de categoría sensible que el caso identifique se cifrarán adicionalmente a,, Según caso nivel de campo, de modo que el acceso a la base de datos no revele su contenido.

La puerta de enlace de servicios aplicará autenticación, autorización, cuotas, límites

PE; e.- Obligatorio de tasa, validación de esquema e inspección de carga Útil. 5

Los puntos de entrada públicos contarán con protección contra bots y abuso automatizado, con reto progresivo que no degrade la accesibilidad ni bloquee a Obligatorio personas usuarias legítimas.

El PROPONENTE declarará la superficie de exposición completa de la solución: cada

Obligatori nombre de dominio, puerto y servicio alcanzable desde fuera de la red del CLIENTE. li

Bases Técnicas Transversales TFEP-01/2026 23/51 11.3 Detección, respuesta y evidencia

Los eventos de seguridad se registrarán de forma centralizada e inalterable, con RT-11.14 retención mínima de doce meses en línea y veinticuatro meses adicionales en archivo Obligatorio recuperable.

Los eventos se correlacionarán en una plataforma SIEM, con casos de uso de RT-11.15 detección definidos específicamente para el proceso de negocio del caso, y no sólo Obligatorio genéricos de infraestructura.

Se implementará detección y respuesta en puntos finales y en cargas de trabajo, RT-11.16; tanto en nube como on-premise.

Obligatorio El PROPONENTE dispondrá de un centro de operaciones de seguridad con cobertura

RT-11.17, AA A E 24x7, propio o subcontratado, y declarará su ubicación, dotación y procedimientos.

RT-11.18 escalamiento, plazos, responsables y protocolo de comunicación al CLIENTE dentro Obligatorio Obligatorio de El plan las dos de respuesta horas de detectado a incidentes un de incidente seguridad de severidad definirá clasificación, crítica. cadena de

Toda brecha de seguridad o de datos personales se notificará al CLIENTE dentro de RT-11.19 las 24 horas de su detección, con informe preliminar, y el análisis de causa raíz se Obligatorio entregará dentro de los cinco días hábiles siguientes.

RT-11.20 Se ADJUDICATARIO, ejecutarán pruebas anualmente de intrusión y antes por de un cada tercero paso independiente a producción, del con entrega íntegra Obligatorio del informe al CLIENTE y plan de remediación con plazos. Se realizarán ejercicios de simulación de incidente con participación del CLIENTE al

RT-11.21 - Deseable menos una vez al año durante la Operación.

11.4 Seguridad del ciclo de desarrollo y de la cadena de suministro

El flujo de integración continua incorporará análisis estático de código, análisis de RT-11.22 composición de software, análisis dinámico y escaneo de imágenes de contenedor, Obligatorio con criterios de bloqueo automático del despliegue ante hallazgos críticos.

Cada versión liberada se acompañará de su inventario de componentes de software

RT-11.23 Obligatori en formato CycloneDX o SPDX, entregado al CLIENTE. lemon Los artefactos se firmarán y su procedencia se verificará conforme a SLSA nivel 3 0 RT-11.24; Obligatorio superior. RT-11.25 - Quedap P P Obligatorio ueda prohibido el uso de datos productivos reales en ambientes no productivos sin e anonimización o seudonimización verificable.

El PROPONENTE declarará el proceso de aprobación de nuevas dependencias de RT-11.26 terceros, incluyendo criterios de licencia, mantención activa y ausencia de Obligatorio vulnerabilidades conocidas.

## Las personas desarrolladoras no tendrán acceso interactivo directo al ambiente de

RT-11.27 producción. Todo acceso excepcional será temporal, aprobado, registrado y con Obligatorio sesión grabada.

Se aplicará el marco OWASP SAMM o equivalente para medir y mejorar la madurez

ea Nu Deseable del proceso de desarrollo seguro, con evaluación inicial y reevaluación anual.

# RT-11.28

Bases Técnicas Transversales TFEP-01/2026 24/51

11.5 Certificaciones y estándares de seguridad exigidos

Sistema Marco Datos personales de de ciberseguridad gestión en de nube seguridad 1ISO/1EC 1ISO/IEC NIST Cybersecurity 27001 27018 e ISO/IEC Framework 27002 2.0 Servicios Arquitectura en nube de confianza cero 1ISO/IEC NIST SP 27017 800-207

OWASP ASVS 4.0 nivel 2 como mínimo; OWASP Top 10 y OWASP API Security

eguridad de aplicaciones Top 10 S idad d licaci

Endurecimiento de sistemas CIS Benchmarks del producto correspondiente Cadena de suministro de software SLSA nivel 3 o superior Continuidad ISO 22301 e ISO/IEC 27031

Normativa nacional Leyes N\* 21.719, N\* 21.663, N\* 21.459 y N\* 19.799, según aplicabilidad al caso

# CAPÍTULO 12 - IDENTIDAD, ACCESO Y GESTIÓN DE SESIONES

La gestión de identidad será centralizada, con federación mediante OpenID Connect y RT-12.01 OAuth 2.1, o SAML 2.0 cuando la integración con el CLIENTE lo requiera, e integración Obligatorio con el directorio corporativo del CLIENTE por LDAP o su equivalente en la nube.

Existirá inicio de sesión único para todos los módulos de la solución, con cierre de RT-12.02 A sesión propagado a todos ellos.

RT-12.03 para todo acceso privilegiado y para todo acceso originado fuera de la red Obligatorio Obligatorio corporativa. La autenticación multifactor será obligatoria para personas usuarias administradoras,

Se soportarán factores resistentes a la suplantación de identidad, tipo FIDO2 o claves

- LaS Deseable de acceso, al menos para los perfiles administradores.

RT-12.04 RT-12.05 atributos donde el proceso lo exija, con matriz de segregación de funciones Obligatorio documentada El control de acceso y verificable. será basado en roles, complementado con control basado en

Los accesos privilegiados se gestionarán con elevación temporal a demanda,

RT-12.06 - i ie de;, aprobación previa y grabación de sesión para las operaciones de mayor riesgo.

RT-12.07 renovación de la credencial de sesión tras la autenticación, revocación inmediata y Obligatorio Obligatorio control La política de de sesiones sesión concurrentes. declarará duración máxima, caducidad por inactividad,

Las credenciales de sesión serán firmadas y de vida breve, con credencial de refresco RT-12.08 rotatoria. Queda prohibido transportar identificadores de sesión en la ruta de la Obligatorio dirección web.

Se registrará auditoría completa del ciclo de vida de la identidad: creación, RT-12.09 modificación, elevación, bloqueo y baja de cuentas, con no repudio y retención Obligatorio declarada.

Bases Técnicas Transversales TFEP-01/2026 25/51

| Elaprovisionamientoyeldesaprovisionamientoestaránautomatizadosyligadosal | RT-12.10ciclodevidalaboral,conbajaefectivaenunplazonosuperiora24horasdesdelaObligatorio | desvinculación. |
|:--- |:--- |:--- |
| Elmecanismodeautenticaciónseadecuaráalperfiloperacionalrealdescritoenel | RT-12.11caso:entornosdeterreno,usoconguantes,bajaalfabetizacióndigital,dispositivosSegúncaso | compartidosporturnoyausenciadecorreoelectrónicopersonal. |
| LaspersonasusuariasexternasdelCLIENTE-clientes,proveedores,pacientes, | RT-12.12productores,segúnelcaso-dispondrándeunmecanismoderegistro,verificaciónSegúncaso | deidentidadyrecuperacióndeaccesoautoservidoyseguro. |

El mecanismo de autenticación se adecuará al perfil operacional real descrito en el RT-12.11 caso: entornos de terreno, uso con guantes, baja alfabetización digital, dispositivos Según caso compartidos por turno y ausencia de correo electrónico personal.

Las personas usuarias externas del CLIENTE -clientes, proveedores, pacientes, RT-12.12 productores, según el caso- dispondrán de un mecanismo de registro, verificación Según caso de identidad y recuperación de acceso autoservido y seguro.

El PROPONENTE declarará el procedimiento de acceso de emergencia (cuenta de

RT-12.13 e: K último recurso), su custodia, su control y su auditoría.

## Obligatorio

# CAPÍTULO 13 - USABILIDAD, ACCESIBILIDAD Y EXPERIENCIA DE USUARIO

| TodaslasinterfacesdestinadasapersonasusuariascumpliránWCAG2.2nivelAA, | RT-13.01verificadoconherramientasautomatizadasyconpruebasmanuales,coninformedeObligatorio | conformidadentregable. |
|:--- |:--- |:--- |
| Eldiseñoseráresponsivoyfuncionarácorrectamenteenescritorio,tabletay | RT-13.02teléfono,conpuntosdequiebrecoherentesyadaptacióninteligentedelcontenido,Obligatorio | nosimplereducción. |
| ElPROPONENTEejecutaráinvestigaciónconpersonasusuariasrealesdelCLIENTE, | RT-13.03prototipadoypruebasdeusabilidadantesdelaconstruccióndefinitiva,yObligatorio | documentaráloshallazgosyloscambiosdediseñoqueprodujeron. |
| Secomprometeránindicadoresdeusabilidadmedibles:tiempomáximodela | RT-13.04transacciónoperacionalcrítica,númeromáximodepasos,tasadeerrortoleradayObligatorio | tiempodeaprendizajeesperadoporperfil. |

El diseño será responsivo y funcionará correctamente en escritorio, tableta y RT-13.02 teléfono, con puntos de quiebre coherentes y adaptación inteligente del contenido, Obligatorio no simple reducción.

El PROPONENTE ejecutará investigación con personas usuarias reales del CLIENTE, RT-13.03 prototipado y pruebas de usabilidad antes de la construcción definitiva, y Obligatorio documentará los hallazgos y los cambios de diseño que produjeron.

Se comprometerán indicadores de usabilidad medibles: tiempo máximo de la RT-13.04 transacción operacional crítica, número máximo de pasos, tasa de error tolerada y Obligatorio tiempo de aprendizaje esperado por perfil.

Ninguna funcionalidad principal requerirá más de tres interacciones desde la pantalla RE13:05 de inicio del perfil correspondiente.

RT-13.06 errores de forma comprensible -indicando qué ocurrió y qué hacer- y evitará Obligatorio Obligatorio La mensajes solución técnicos entregará dirigidos retroalimentación a la persona visual usuaria clara final. ante cada acción, manejará los

La solución soportará a personas usuarias con baja alfabetización digital: alto RT-13.07 contraste, objetivos táctiles de al menos 44 x 44 píxeles, iconografía acompañada de Obligatorio texto, y flujos guiados paso a paso.

Cuando el caso lo requiera, las interfaces de terreno operarán con guantes, a la

RT-13.08.. ED.. » Según caso intemperie, con luminosidad variable y sin conexión. Existirá un sistema de diseño documentado con paleta de colores acotada, jerarquía RT-13.09 tipográfica de a lo más dos familias, iconografía coherente, retícula y componentes Obligatorio reutilizables. El PROPONENTE declarará la matriz de navegadores y de versiones soportadas y su,, RT-13.10 E. Obligatorio política de actualización. La solución será navegable íntegramente por teclado, con orden de foco lógico A; RT-13.11 E E h, gico y Obligatorio atajos para las operaciones frecuentes.

Bases Técnicas Transversales TFEP-01/2026 26/51

Se valorará el soporte de modo oscuro, de personalización de la interfaz por persona RT-13.12. M. o Deseable usuaria y de múltiples idiomas cuando el caso lo justifique.

# CAPÍTULO 14 - OBSERVABILIDAD Y GESTIÓN DEL SERVICIO

La observabilidad será unificada para nube y on-premise, con métricas, registros y RT-14.01 trazas distribuidas correlacionadas por un identificador único de transacción, Obligatorio instrumentadas conforme a OpenTelemetry.

El CLIENTE dispondrá de acceso propio y permanente a los tableros operacionales y

RT-14.02.., A de negocio, con datos en tiempo real y capacidad de exportación.

RT-14.03 persona usuaria y no sobre pruebas sintéticas, sin perjuicio de que estas se empleen Obligatorio Obligatorio como Los indicadores complemento. de nivel de servicio se medirán sobre la experiencia real de la

El alertamiento se basará en síntomas de negocio y no sólo en umbrales de RT-14.04 infraestructura, con supresión de ruido, agrupación, escalamiento automático y Obligatorio turnos de disponibilidad declarados.

Existirá un libro de operación y una guía de resolución documentados para cada

RT-14.05. N\_ ADA, "e escenario de falla previsible, con automatización progresiva de las tareas repetitivas.

RT-14.06 entregable dentro de cinco días hábiles y seguimiento de las acciones correctivas Obligatorio Obligatorio Todo hasta incidente su cierre. crítico dará lugar a un análisis de causa raíz obligatorio, con informe

Los registros de la solución no contendrán datos personales sensibles ni credenciales,

RT-14.07,: Y su acceso estará controlado y auditado.

## Obligatorio

El PROPONENTE declarará la retención de métricas, registros y trazas, y su costo.. RT-14.08. o.,. Obligatorio asociado, distinguiendo el almacenamiento en línea del archivado.

Se valorará la detección proactiva de anomalías mediante análisis del RT-14.09. o NE - Deseable comportamiento histórico, con alerta antes de que el incidente afecte a la operación.

# CAPÍTULO 15 - SOSTENIBILIDAD, EFICIENCIA Y CERTIFICACIONES 15.1 Sostenibilidad y eficiencia energética

El PROPONENTE dimensionará la infraestructura ajustada a la demanda real,

RT-15.01 evitando capacidad ociosa permanente, y declarará el factor de utilización Obligatorio proyectado. RT-15.02 Los ambientes no productivos se apagarán o reducirán fuera del horario de uso. Obligatorio

El PROPONENTE estimará la huella de carbono anual de la operación de la solución y

RT-15.03 Y, declarará la metodología empleada.

## Obligatorio

Se declarará la eficiencia en el uso de la energía (PUE) del recinto on-premise y la., RT-15.04.. ». Obligatorio intensidad de carbono de la región de nube escogida.

Bases Técnicas Transversales TFEP-01/2026 27/51

Pontificia Universidad Católica de Valparaíso - Escuela de Informática

Licitación N\* TFEP-01/2026 - Bases Técnicas Transversales

# RT-15.05

Se valorará la elección de regiones de nube con menor intensidad de carbono cuando Deseable

la latencia y la regulación lo permitan, con el análisis comparativo correspondiente.

# RT-15.06

Se valorará la definición de metas de reducción del consumo durante la Operación, con medición y reporte anual. 15.2 Certificaciones institucionales exigidas

# \[ión tte ISO/IEC 27001 - Seguridad de la información ISO 9001 - Gestión de la calidad ISO/IEC 20000-1 - Gestión de servicios de TI 1SO 22301 - Continuidad del negocio

ISO/IEC 42001 - Gestión de inteligencia artificial Certificación sectorial específica 15.3 Certificaciones del personal

## Obligatoria Obligatoria Deseable Deseable Deseable Según caso Deseable

Vigente a la fecha de la oferta o plan de certificación con hitos verificables dentro de los primeros 12 meses del Contrato.

Vigente Vigente Vigente Exigible sólo a o o la plan plan fecha si declarado. declarado. la solución de la oferta. incorpora componentes de IA.

La que identifiquen las Bases Técnicas del caso.

El equipo propuesto acreditará, como mínimo, las siguientes certificaciones individuales vigentes. Una misma

persona puede acreditar más de una, pero no puede contarse dos veces para el mismo requisito. Certificación o competencia Cantidad mínima

Gestión arquitecto de proyectos (PMP, PRINCE2 o equivalente) 2 asma personas Gestión Seguridad de de servicios la información (ITIL 4 Foundation (CISSP, CISM, o superior) CEH, OSCP o equivalente) 5 2 personas personas Gobierno Bases de datos de TI (COBIT del motor o equivalente) ofertado 2 2 personas personas Arquitectura Calidad y pruebas de nube de software del proveedor (ISTQB ofertado, o equivalente) nivel profesional o de 2 personas

Las certificaciones se acreditarán con copia del certificado vigente y con el código de

RT-15.07 RT-15.08 RT-15.09 contractual PROYECTO, e y con las dedicación repondrá, ante declarada.: la salida No de se una, aceptará persona acreditar certificada, personal conforme que no al Obligatorio Obligatorio Obligatorio verificación participe. del organismo emisor cuando exista. Las El ADJUDICATARIO personas certificadas mantendrá formarán vigentes parte estas del equipo certificaciones efectivamente durante asignado todo el período al Artículo 76\* de las Bases Administrativas.

Bases Técnicas Transversales TFEP-01/2026 28/51

# CAPACIDADES TRANSVERSALES DE LA SOLUCIÓN

Los módulos y capacidades de este Título son exigibles en las trece industrias. No son el negocio del caso -eso lo definen las Bases Técnicas respectivas - sino la infraestructura funcional sin la cual ninguna plataforma de

misión crítica es operable, auditable ni administrable.

# CAPÍTULO 16 - MÓDULOS TRANSVERSALES OBLIGATORIOS 16.1 Administración y parametrización

La solución dispondrá de un módulo de administración que permita al CLIENTE, sin RT-16.01 intervención del ADJUDICATARIO, gestionar personas usuarias, roles, permisos, Obligatorio unidades organizacionales y sus jerarquías.

catálogos, Las interfaz reglas de de listas administración, negocio de valores, parametrizables con textos control de notificación -umbrales, de versiones - plazos, serán y registro configurables montos, de quién tolerancias, cambió desde la qué y.. RT-16.02. ».. a T\_ Obligatorio cuándo.

Todo cambio de parámetro con impacto operacional requerirá aprobación de un

RT-16.03. N, LE sei segundo perfil y quedará registrado con su justificación.

RT-16.04 cuáles requieren desarrollo. Presentar como parametrizable lo que exige desarrollo Obligatorio Obligatorio se El PROPONENTE evaluará como declarará observación expresamente grave. qué elementos son parametrizables y Existirá un ambiente de simulación que permita probar el efecto de un cambio de

RT-16.05;: e Deseable parámetro antes de aplicarlo a producción. 16.2 Auditoría y trazabilidad

Toda operación que cree, modifique o elimine información quedará registrada con RT-16.06 identificación de la persona o del sistema que la ejecutó, fecha y hora con zona Obligatorio horaria, origen, valores anteriores y valores posteriores.

El registro de auditoría será inalterable y no podrá ser modificado ni eliminado por

RT-16.07 ningún perfil, incluido el administrador de la plataforma.

## Obligatorio

El CLIENTE podrá consultar y exportar la auditoría desde la interfaz, con filtros por.. RT-16.08,;. E.. Obligatorio persona, período, entidad y tipo de operación, sin requerir acceso a la base de datos.

Las consultas a información sensible quedarán registradas, no sólo las, RT-16.09 NE. a 5, Según caso modificaciones.

El período de retención de la auditoría será el que fije el caso y, en su defecto, no RT-16.10... AN inferior a cinco años. Según caso

Bases Técnicas Transversales TFEP-01/2026 29/51 16.3 Flujos de trabajo y motor de reglas

# RT-16.11

# RT-16.12

# RT-16.13

# RT-16.14

## La solución soportará flujos de trabajo con estados, transiciones, responsables,, LA o E.. Obligatorio Deseable plazos, escalamiento automático por vencimiento y delegación por ausencia. Los flujos serán configurables por el CLIENTE sin desarrollo, al menos en lo relativo a Obliestorio responsables, plazos y niveles de aprobación. Toda solicitud pendiente será visible para su responsable en una bandeja de tareas Obiiestorio unificada, con priorización y alerta de vencimiento. 5 El motor de reglas permitirá definir condiciones de negocio evaluables sin

recompilación, con trazabilidad de qué regla se aplicó a cada transacción. 16.4 Gestión documental y firma electrónica

# RT-16.15

# RT-16.16

# RT-16.17

# RT-16.18

# RT-16.19

La solución gestionará documentos con versionado, metadatos, control de acceso,,;; onaldn Obligatorio búsqueda por contenido y por metadato, y previsualización sin descarga.

Los documentos se almacenarán cifrados, con verificación de integridad y retención

L Obligatorio conforme a la política del caso.:

La solución soportará firma electrónica conforme a la Ley N\* 19.799, con firma avanzada para los actos que el caso lo requiera, y verificación de validez del Según caso certificado al momento de la firma.

Se generará el sello de tiempo y se conservará la evidencia de firma que permita

E is mi Ei Según caso verificar el documento con posterioridad al vencimiento del certificado. =

La solución generará documentos a partir de plantillas administrables por el CLIENTE,

N.: Obligatorio con datos de la transacción y salida en formato abierto. 5 16.5 Notificaciones y mensajería multicanal

# RT-16.20

# RT-16.21

# RT-16.22

# RT-16.23

# RT-16.24

# RT-16.25

# RT-16.26

La solución enviará notificaciones por al menos tres canales: correo electrónico, notificación en la aplicación y mensajería instantánea o SMS, según lo que el caso Obligatorio requiera.

Las plantillas de notificación serán administrables por el CLIENTE, con variables de la e i Obligatorio transacción, y versionadas.

Cada persona usuaria podrá configurar sus preferencias de canal y de frecuencia,

\_, i í Obligatorio respetando las notificaciones que el CLIENTE defina como obligatorias. 5 El envío será asíncrono, con reintento ante falla, control de duplicados y registro de Obligatorio entrega, apertura y error por cada mensaje. si El PROPONENTE declarará el proveedor de cada canal, su costo unitario, su volumen Obligatorio proyectado y el tratamiento del costo variable en la Oferta Económica.: Las notificaciones respetarán la normativa de comunicaciones comerciales y. a Td, Obligatorio permitirán la baja cuando corresponda. Se valorará la integración con canales conversacionales que permitan a la persona Deseable

usuaria responder y ejecutar acciones desde el propio canal.

Bases Técnicas Transversales TFEP-01/2026 30/51

## 16.6 Búsqueda, reportería y exportación

La solución dispondrá de búsqueda global con indexación de texto completo, RT-16.27 tolerancia a errores de escritura, filtros facetados y respeto del control de acceso de Obligatorio la persona que busca.

Los listados serán ordenables, filtrables, paginados y exportables en formatos

RT-16.28: Obligatorio abiertos, con el filtro aplicado reflejado en la exportación. 5 Las exportaciones de gran volumen se procesarán de forma asíncrona, con:; RT-16.29 TT. » Obligatorio notificación al completarse y sin bloquear la sesión. Toda exportación de información sensible quedará registrada en la auditoría, con.. RT-16.30 u q s, Obligatorio identificación de quién exportó qué y cuándo. 16.7 Portal público y canales de autoatención

La solución dispondrá de un portal público con la información que el caso determine, RT-16.31 accesible sin autenticación, con los mismos estándares de accesibilidad y desempeño Según caso que el resto de la plataforma.

Las personas usuarias externas dispondrán de autoatención para las consultas de

RT-16.32 RT-16.33 RT-16.34 El PROPONENTE P P. estimar! p la reducción esperada au E del volumen de, atención: asistida por Obligatorio Obligatorio Obligatorio efecto mayor de frecuencia, la autoatención evitando y comprometerá el contacto telefónico el indicador. para operaciones simples. El portal público resistirá picos de tráfico sin degradar los servicios transaccionales,;

internos, mediante aislamiento de recursos y caché.

# CAPÍTULO 17 - CANALES DIGITALES Y MOVILIDAD

La solución proveerá una aplicación móvil para los perfiles operacionales que el caso RT-17.01 identifique, con funcionamiento sin conexión y sincronización diferida cuando la Según caso operación en terreno lo requiera.

El PROPONENTE declarará si la aplicación es nativa, híbrida o web progresiva, y RT-17.02 justificará la decisión frente al requisito de operación desconectada, al acceso a Obligatorio periféricos y al costo de mantención.

La aplicación soportará las versiones de sistema operativo móvil vigentes y las dos

RT-17.03, A MD. Obligatorio anteriores, con política de actualización declarada. La aplicación se distribuirá por las tiendas oficiales o mediante gestión de flota s RT-17.04 h N, p E. E.,, E Obligatorio corporativa, con firma de la aplicación y verificación de integridad. La información almacenada en el dispositivo estará cifrada, con borrado remoto y o RT-17.05 MU. ne. Obligatorio bloqueo ante pérdida o desvinculación de la persona usuaria. La aplicación integrará los periféricos que el caso requiera: cámara, lector de códigos RT-17.06 h, E P a, ú, =os, Según caso NFC, GPS, impresora de etiquetas, balanza o báscula. El consumo de datos móviles y de batería se optimizará y se declarará el consumo.. RT-17.07 y h Y Obligatorio estimado por turno de trabajo.

Bases Técnicas Transversales TFEP-01/2026 31/51

Se valorará la disponibilidad de una versión de la interfaz para dispositivos de bajo

RT-17.08.,: i costo o de generaciones anteriores, ampliando la cobertura de personas usuarias. Deseable

# CAPÍTULO 18 - INTELIGENCIA ARTIFICIAL Y AUTOMATIZACIÓN

La incorporación de inteligencia artificial no es obligatoria. Sí lo es, cuando el PROPONENTE la incorpore, cumplir íntegramente los requisitos de este capítulo. Una capacidad de inteligencia artificial mal gobernada es un riesgo, no una ventaja competitiva.

El PROPONENTE declarará cada componente de inteligencia artificial: propósito,

RT-18.01 modelo o servicio empleado, proveedor, versión y ubicación de procesamiento de los Obligatorio datos. Se garantizará contractualmente que los datos del CLIENTE no serán utilizados para RT-18.02 E a ns N h Obligatorio entrenar modelos de terceros, salvo autorización expresa y escrita. Se documentarán los límites de uso, los casos en que el resultado requiere validación Ss RT-18.03, a a Obligatorio

humana previa y el procedimiento de supervisión.

| Losriesgosdesesgo,alucinación,fugadeinformaciónyusoindebidoseevaluarány | RT-18.04mitigaránconformealNISTAlRiskManagementFramework1.0yalanormaISO/IECObligatorio | 42001. |
|:--- |:--- |:--- |
| Todainteracciónrelevanteconuncomponentedeinteligenciaartificialquedará | RT-18.05registradaparaefectosdeauditoríaytrazabilidad,incluyendolaentrada,lasalidayObligatorio | ladecisiónhumanaposterior. |
| Elcomponentepodrádesactivarsesincomprometerlaoperacióndelrestodela | RT-18.06solución,yexistiráunprocedimientomanualderespaldoparalafunciónqueObligatorio | automatiza. |

Toda interacción relevante con un componente de inteligencia artificial quedará RT-18.05 registrada para efectos de auditoría y trazabilidad, incluyendo la entrada, la salida y Obligatorio la decisión humana posterior.

El componente podrá desactivarse sin comprometer la operación del resto de la RT-18.06 solución, y existirá un procedimiento manual de respaldo para la función que Obligatorio automatiza.

Cuando el resultado se presente a una persona usuaria, se indicará expresamente RT-18.07 que fue generado o sugerido de forma automática, y su nivel de confianza cuando el Obligatorio modelo lo provea. Los modelos predictivos declararán sus variables de entrada, su métrica de.. RT-18.08. í, e. Obligatorio desempeño, su línea base y su plan de reentrenamiento y de detección de deriva. La responsabilidad por los resultados de los componentes de inteligencia artificial RT-18.09 recae íntegramente en el ADJUDICATARIO, conforme al Artículo 86? de las Bases Obligatorio Administrativas.

Se valorará el uso de automatización robótica de procesos o de agentes para tareas RT-18.10 repetitivas de back office, con el ahorro de horas cuantificado y reflejado en la Oferta Deseable Económica.

Incorporar un modelo de lenguaje a la solución sin declarar dónde se procesan los datos, sin control de acceso a la información que consulta y sin validación humana de sus resultados será evaluado como incumplimiento de los requisitos de seguridad, no como innovación.

Bases Técnicas Transversales TFEP-01/2026 32/51

# PROYECTO, IMPLANTACIÓN Y OPERACIÓN

# CAPÍTULO 19 - ESTRUCTURA Y GOBIERNO DEL PROYECTO 19.1 Oficina de gestión y metodología

| ElADJUDICATARIOconstituiráunaoficinadegestióndelproyectoconmetodología | RT-19.01declarada,basadaenelPMBOKdelProjectManagementInstituteeintegrandoObligatorio | prácticaságilesdondeelPROPONENTElojustifique. |
|:--- |:--- |:--- |
| ElJefedeProyectotendrádedicaciónexclusivadurantetodalafasede | RT-19.02implementaciónyfacultadesparacomprometeralADJUDICATARIOenmateriasdeObligatorio | ejecución. |
| ExistiráunprocedimientoformaldecontroldecambiosconformealArtículo72\*de | RT-19.03lasBasesAdministrativas,conregistrodecambios,análisisdeimpactoyaprobaciónObligatorio | previaalaejecución. |
| LagestióndelriesgoseguirálanormaISO31000,conregistroderiesgosvivo, | RT-19.04revisiónencadaComitédeProyectoyplanesdemitigaciónconresponsable,plazoyObligatorio | disparador. |
| ElADJUDICATARIOhabilitaráunespaciocolaborativoaccesiblealCLIENTE,conla | RT-19.05documentacióndelproyecto,losentregables,lasactas,elregistroderiesgosyelObligatorio | registrodecambiossiempreactualizados. |

El Jefe de Proyecto tendrá dedicación exclusiva durante toda la fase de RT-19.02 implementación y facultades para comprometer al ADJUDICATARIO en materias de Obligatorio ejecución.

Existirá un procedimiento formal de control de cambios conforme al Artículo 72\* de RT-19.03 las Bases Administrativas, con registro de cambios, análisis de impacto y aprobación Obligatorio previa a la ejecución.

La gestión del riesgo seguirá la norma ISO 31000, con registro de riesgos vivo, RT-19.04 revisión en cada Comité de Proyecto y planes de mitigación con responsable, plazo y Obligatorio disparador.

El ADJUDICATARIO habilitará un espacio colaborativo accesible al CLIENTE, con la RT-19.05 documentación del proyecto, los entregables, las actas, el registro de riesgos y el Obligatorio registro de cambios siempre actualizados. 19.2 Roles mínimos del equipo

# \[0 Pasción nin gusto

Certificación en gestión de proyectos y Jefe de Proyecto 100 % en implementación experiencia comprobable en proyectos de escala equivalente.

Arquitecto Encargado Líder,. 5 de Desarrollo e de de Seguridad Solución E.. de la Alta Permanente 100 % en en o diseño, implementación permanente,, en Certificación Certificación Experiencia Experiencia e en en de en modelado la arquitectura seguridad tecnología. y vigente. migración. ofertada. del proveedor de Información Líder Líder de Funcional Datos el Permanente 100 Comité % en implementación de en Arquitectura implementación de Experiencia nube ofertado. en la industria del caso. Líder de Calidad y Pruebas Permanente datos. Certificación en pruebas de software. Experiencia en integración de sistemas

Líder de Integración Permanente en implementación heredados. Desde el mes 6, permanente en

íder de Operación / Oparación Líder de O ión / SRE, Certificación en gestión de servicios.

Bases Técnicas Transversales TFEP-01/2026 33/51

# \[rg Pasación mim quo

Líder de Implantación y Gestión del Experiencia en implantación con usuarios. Desde el mes 8. Cambio operacionales.

El PROPONENTE podrá agregar los roles que su propuesta requiera. La dotación total del equipo deberá ser coherente con las horas hombre del Formulario T-15 y con la curva de recursos de la Oferta Económica. 19.3 Control y reporte del proyecto

El ADJUDICATARIO entregará un informe mensual de avance con estado del RT-19.06 cronograma, avance físico y financiero, entregables del período, desviaciones, Obligatorio riesgos, incidencias y compromisos del período siguiente.

El avance se medirá con valor ganado, reportando el índice de desempeño del RT-19.07 cronograma y del costo, y no mediante declaración cualitativa de porcentaje de Obligatorio avance.

El CLIENTE dispondrá de un tablero de estado del proyecto actualizado, accesible en RT-19.08, cualquier momento.

RT-19.09 levantarán dentro de los dos días hábiles siguientes y registrarán acuerdos, Obligatorio Obligatorio Las responsables actas de todos y plazos. los comités del Artículo 71\* de las Bases Administrativas se Toda desviación superior al 10 % en un hito se comunicará dentro de los cinco días

RT-19.10 e " Obligatorio hábiles de detectada, con plan de recuperación.;

# CAPÍTULO 20 - IMPLANTACIÓN, PRUEBAS Y CRITERIOS DE ACEPTACIÓN

## 20.1 Estrategia de pruebas Cobertura mínima de 70 % en lógica de

Unitarias y de componente \| Continuo, en el flujo de integración e negocio; sin pruebas en falla. Todos los flujos de integración del caso

Integración Continuo, tras cada despliegue a QA. " ejecutados sin error.... Antes de cada promoción a Batería de regresión automatizada Sistema y regresión ";; Preproducción completa sin regresiones. -, --- Casos de aceptación del caso aprobados Aceptación de usuario Antes de cada certificación de etapa. h.. y firmados por la Contraparte Técnica., " Umbrales del Capítulo 9 cumplidos a 1,5 Carga y estrés Antes de cada paso a producción h h veces el peak declarado. Resiliencia Antes de cada paso a producción y La solución degrada de forma controlada y semestral en Operación se recupera sin intervención.

Recuperación ante RTO y RPO comprometidos alcanzados en Antes del paso a producción y semestral

desastres Seguridad Accesibilidad ofensiva Antes Antes de de cada cada paso paso a a producción producción y anual \| Sin conmutación hallazgos críticos real. ni altos abiertos. y an e Conformidad WCAG 2.2 AA verificada documentada.

Bases Técnicas Transversales TFEP-01/2026 34/51 Dos ensayos previos a la migración Migración de datos definitiva Conciliación sin diferencias no explicadas.

## 20.2 Requisitos de implantación

El PROPONENTE presentará un plan de implantación por sitio y por perfil, coherente

RT-20.01 A ""; Obligatorio con el cronograma obligatorio del Artículo 17" de las Bases Administrativas. 5 La estrategia de paso a producción será gradual y reversible. Se declarará el criterio.. RT-20.02 E ».. » Obligatorio de avance entre olas y el procedimiento de reversión, con su tiempo de ejecución. Durante la marcha blanca, la solución convivirá con la operación vigente del CLIENTE,, RT-20.03, h td, Obligatorio

con conciliación diaria y sin doble digitación no declarada.

El PROPONENTE definirá los indicadores diarios que se medirán durante la marcha RT-20.04 blanca y sus umbrales de avance, conforme al Artículo 17.3 de las Bases Obligatorio Administrativas.

Se dispondrá de acompañamiento en terreno durante las primeras semanas de cada

RT-20.05 RT-20.06 Ri:20.07 RT-20.08 Existirá una e Aciinición, ELO de temminado.; acordada, con el! CUENTE, a aplicable e a Eada p Obligatorio Obligatorio obligatorio Obligatorio ola, entregable, producción, con dotación que con incluya dotación declarada código, y duración y decreciente pruebas, declaradas documentación, según y la sin curva costo de seguridad adicional. adopción. y despliegue. 5 Se El protocolo establecerá de un aceptación período de de estabilización cada hito se formalizará con atención conforme reforzada al tras Formulario cada paso T-17, a " o con criterios objetivos y verificables.

# CAPÍTULO 21 - MODELO DE OPERACIÓN, MANTENCIÓN Y SOPORTE 21.1 Estructura operativa

El ADJUDICATARIO dispondrá de un centro de operaciones de red con cobertura RT-21.01 24x7x365, propio o subcontratado, y declarará su ubicación, dotación por turno y Obligatorio procedimientos.

Se designará un gerente de servicio dedicado como contraparte permanente del

RT-21.02, Obligatorio CLIENTE durante la fase de Operación. E RT-21.03 El equipo de operación contará con especialistas por tecnología, nominados y con oblisstorio dedicación declarada. Los procedimientos de operación estarán documentados y serán ejecutables por el. RT-21.04 Obligatorio

personal del CLIENTE tras la transferencia de conocimiento.

Bases Técnicas Transversales TFEP-01/2026 35/51 21.2 Centro de atención telefónica

Este ámbito es central para dar continuidad y seguimiento al esfuerzo de incorporación y adopción de la solución.

# RT-21.05

# RT-21.06

# RT-21.07

# RT-21.08

# RT-21.09

# RT-21.10

# RT-21.11

# RT-21.12

# RT-21.13

# RT-21.14

| ElPROPONENTEdispondrádeuncentrodeatenciónadecuadoparasoportar | integralmentelasconsultas,propioosubcontratadoconunoperadordenivelObligatorio | acreditado. |
|:--- |:--- |:--- |
| Elcentrodeatencióncumpliráuntiempodeatenciónalusuariofinalde80%antes | de20segundosyunaresoluciónalprimercontactodealmenos70%.LatasadeObligatorio | abandononosuperaráel5%. |
| Elhorariomínimodeatenciónseráde8:00a20:00endíashábiles,ampliadoa24x7 | paralosincidentesdeseveridadcríticayparalaventanaoperacionalquedefinaelSegúncaso | caso. |
| Laatencióncubriráorientaciónfuncionaldedistintosgradosdecomplejidad,desde | preguntassimpleshastasituacionescomplejas,ylaspreguntastécnicasmásObligatorio | frecuentessobrelaaplicaciónysuentornodeuso. |
| Semantendráunregistrohistóricodelasactividadesdesoportequepermita | monitorearygestionarlosprincipalesrequerimientos,conanálisisdetendenciaObligatorio | mensual. |
| Existiráunprocesodeaprendizajedelcentrodesoportequeacumuleconocimiento | sobrelascomplejidadesdelaoperaciónylasnecesidadesdelaspersonasusuarias,Obligatorio | reflejadoenlabasedeconocimiento. |

El centro de atención cumplirá un tiempo de atención al usuario final de 80 % antes de 20 segundos y una resolución al primer contacto de al menos 70 %. La tasa de Obligatorio abandono no superará el 5 %.

El horario mínimo de atención será de 8:00 a 20:00 en días hábiles, ampliado a 24x7 para los incidentes de severidad crítica y para la ventana operacional que defina el Según caso caso.

La atención cubrirá orientación funcional de distintos grados de complejidad, desde preguntas simples hasta situaciones complejas, y las preguntas técnicas más Obligatorio frecuentes sobre la aplicación y su entorno de uso.

Se mantendrá un registro histórico de las actividades de soporte que permita monitorear y gestionar los principales requerimientos, con análisis de tendencia Obligatorio mensual.

Existirá un proceso de aprendizaje del centro de soporte que acumule conocimiento sobre las complejidades de la operación y las necesidades de las personas usuarias, Obligatorio reflejado en la base de conocimiento.

Se proveerán servicios de capacitación en línea en modalidad de autoformación, con

i, Obligatorio registro de avance para efectos de monitoreo. Se habilitarán espacios de interacción entre las entidades y personas usuarias del Deseable sistema, que permitan compartir experiencias de uso. Los indicadores clave del proceso de soporte estarán abiertos al CLIENTE, y los.. Obligatorio

indicadores específicos serán accesibles según nivel de autorización.

El PROPONENTE dimensionará la dotación del centro de atención con fundamento cuantitativo, empleando teoría de colas o el modelo Erlang C, a partir del volumen de Obligatorio contactos proyectado del caso. 21.3 Mesa de ayuda por niveles

# \[at ess Nivel 1 Nivel 2

Recibe los contactos de las personas usuarias internas y externas sobre cualquier requerimiento de la plataforma.

Recepción, registro del ticket, clasificación, soluciones básicas y derivación.

Soporte especializado, configuraciones y Agentes con mayores conocimientos o especialistas diagnóstico. Los incidentes relativos a

en el sistema y en las aplicaciones provistas por el procedimientos propios de la operación o a ADJUDICATARIO. Resuelven los incidentes derivados \| aplicaciones del CLIENTE no provistas por el del nivel 1 apoyándose en manuales y guías. ADJUDICATARIO son de responsabilidad del CLIENTE y no se derivan a la mesa.

Bases Técnicas Transversales TFEP-01/2026 36/51

Pontificia Universidad Católica de Valparaíso - Escuela de Informática

Licitación N\* TFEP-01/2026 - Bases Técnicas Transversales

# Gm e tu

Métodos de solución a nivel experto y análisis Nivel 3 avanzado de la solución y de las aplicaciones

## provistas. Nivel 4 software o hardware utilizados. Soporte del fabricante de los componentes de

Resolución de problemas nuevos o desconocidos, apoyo a los niveles 1 y 2, e investigación y desarrollo de soluciones. Incluye el traslado a sitio cuando el problema lo requiera.

Es responsabilidad del ADJUDICATARIO gestionar y obtener este soporte cuando se requiera, sin que ello lo exima de responsabilidad frente al CLIENTE.

# RT-21.15

# RT-21.16

# RT-21.17

# RT-21.18

Existirá un canal único de registro de incidentes y solicitudes, con número de ticket, clasificación por severidad y seguimiento del ciclo de vida completo hasta el cierre Obligatorio conforme.

Cuando el caso comprenda sitios alejados, los especialistas de niveles 2 y 3 deberán trasladarse cuando la resolución lo requiera, por el medio más rápido disponible y

i dsd i e i e Según caso con disponibilidad de tiempo suficiente, sin alterar la atención normal del resto de 5 los sitios. El costo del traslado está incluido en la oferta. El cierre de un ticket requerirá confirmación de la persona usuaria o transcurso del.. y » e Obligatorio plazo de confirmación automática declarado. El ADJUDICATARIO reportará mensualmente el cumplimiento de los niveles de o. Obligatorio

servicio de atención, con el detalle por severidad y el análisis de los incumplimientos. 21.4 Mantención

# \[0 Preventiva Correctiva Evolutiva Normativa

| Revisionesprogramadas,actualizacionesCalendarioanualacordadoconelCLIENTE. | planificadas,optimizacióncontinuayauditoríasAuditoríasalmenostrimestrales,con | técnicas.informe. |
|:--- |:--- |:--- |
| Sincostoadicional.Sujetaalostiemposde | Correccióndedefectosdelasolución.resolucióndelArtículo78"delasBases | Administrativas. |
| Bolsaanualdehorascomprometidaenla | oferta,contarifadeclaradaparael | excedente.Labolsanoutilizadaenunaño |

Sin costo adicional. Sujeta a los tiempos de Corrección de defectos de la solución. resolución del Artículo 78" de las Bases Administrativas.

Bolsa anual de horas comprometida en la oferta, con tarifa declarada para el excedente. La bolsa no utilizada en un año

Mejoras funcionales, nuevas características y optimización del desempeño solicitadas por el

CLIENTE. í \_ no se pierde y se acumula al siguiente. Incluida en el valor de la Operación, sin Adecuación de la solución ante cambios legales o costo adicional. Plazo de adecuación regulatorios aplicables al caso. coherente con la entrada en vigencia de la norma.

# RT-21.19

## El PROPONENTE declarará el tamaño de la bolsa anual de horas de mantención

evolutiva, su composición por perfil y el procedimiento de solicitud, estimación, Obligatorio aprobación y liquidación.

Bases Técnicas Transversales TFEP-01/2026 37/51

# RT-21.20

# RT-21.21

# RT-21.22

La mantención evolutiva se someterá al mismo estándar de calidad, pruebas y

", Ta, Obligatori Obligatorio Obligatorio seguridad una fracción que declarada el desarrollo de la original. capacidad de la Operación a reducirla. ió El Las PROPONENTE actualizaciones mantendrá de versión un de registro los componentes de deuda técnica de base cuantificado se planificarán y destinará S. A.

anualmente, con ventana acordada y plan de reversión.

# CAPÍTULO 22 - CAPACITACIÓN Y TRANSFERENCIA DE CONOCIMIENTO

# RT-22.01

# RT-22.02

# RT-22.03

# RT-22.04

# RT-22.05

# RT-22.06

# RT-22.07

# RT-22.08

# RT-22.09

El plan de capacitación se estructurará por perfil: personas usuarias finales, usuarias

-. Obligatorio avanzadas, administradoras, equipo técnico y soporte de niveles 1 y 2. 5

Las modalidades incluirán capacitación presencial en cada sitio de operación, sesiones en línea sincrónicas, autoformación y acompañamiento en puesto de Obligatorio trabajo durante la marcha blanca.

Todo el material de capacitación se entregará en español, en formato editable y de propiedad del CLIENTE: manuales por perfil, guías rápidas, preguntas frecuentes, Obligatorio videos tutoriales y base de conocimiento consultable.

La capacitación no podrá afectar la operación del CLIENTE: se programará por turnos

y en horarios acordados, considerando la estacionalidad y la ventana operacional del Según caso caso. Las personas usuarias administradoras y el equipo técnico del CLIENTE serán, " e E, Obligatorio evaluados y certificados como condición para el cierre de cada marcha blanca. Durante la Operación se ejecutarán al menos dos jornadas anuales de actualización y Oblizatorio se capacitará al personal nuevo del CLIENTE sin costo adicional. E El ADJUDICATARIO proveerá acompañamiento y mentoría al equipo técnico del oblisatorio CLIENTE durante al menos seis meses posteriores al paso a producción de la Etapa 2. 5 La base de conocimiento será mantenida y actualizada durante todo el Contrato, con N. E lt Sis Obligatorio métricas de uso y de utilidad percibida. Se valorará la existencia de un ambiente permanente de entrenamiento, con datos Deseable

## ficticios, disponible para la práctica sin riesgo.

Bases Técnicas Transversales TFEP-01/2026 38/51

# EXIGENCIAS DE PRESENTACIÓN DE LA PROPUESTA

Este Título establece entregables de la propuesta que no son documentos escritos: la presencia digital del proponente, un video de presentación y un prototipo interactivo. Los tres se evalúan y los tres tienen causales de descalificación propias.

# CAPÍTULO 23 - INFORMACIÓN CORPORATIVA Y PRESENCIA DIGITAL

## 23.1 Página web corporativa

El PROPONENTE deberá disponer de una página web corporativa activa y actualizada que contenga, como

mínimo, la siguiente información claramente identificable y de fácil acceso.

Información institucional: descripción detallada del giro principal, historia y trayectoria de la empresa con al menos tres años de antigúiedad comprobable, misión, visión y valores, certificaciones y acreditaciones vigentes, y presencia geográfica y oficinas. RT-23.01 Obligatorio

Experiencia y casos de éxito: portafolio de proyectos similares de los últimos cinco años, casos documentados con métricas verificables, testimonios de clientes con autorización de publicación, industrias atendidas con énfasis en la del caso asignado, y volumen de transacciones o de personas usuarias gestionadas. RT-23.02 Obligatorio

## Equipo profesional: organigrama del equipo directivo, perfiles de socios y directores,

RT-23.03 currículos resumidos del equipo técnico clave y certificaciones profesionales del Obligatorio personal.

Capacidades técnicas: servicios y soluciones ofrecidas, conjunto tecnológico RT-23.04 dominado, alianzas tecnológicas con proveedores de nube y de plataforma, Obligatorio metodologías de trabajo certificadas, e infraestructura y capacidad instalada.

El sitio será accesible conforme a WCAG 2.2 nivel AA, responsivo y con certificado TLS RT-23.05 ", válido y vigente.

## Obligatorio

El sitio se mantendrá activo y disponible durante todo el proceso de licitación, desde.. RT-23.06: Un Obligatorio el registro del participante hasta la adjudicación.

Material educativo digital: seminarios en línea, artículos técnicos o centro de

RT-23.07 RT-23.08 RT-23.09 Métricas N de disponibilidad e y desempeño de los servicios del proponente publicadas Deseable Deseable Deseable clientes. recursos y documentación. Demostración en línea, recorrido virtual de la solución o portal de soporte para en tiempo real.

Calculadora de retorno de la inversión o herramienta de estimación pertinente a la RT-23.10.. P Deseable industria del caso. 23.2 Verificación y validación

El CLIENTE verificará el sitio durante el proceso de evaluación. Constituyen causal de descalificación:

\* Sitio web no disponible o con caídas recurrentes durante el período de evaluación.

Bases Técnicas Transversales TFEP-01/2026 39/51

Pontificia Universidad Católica de Valparaíso - Escuela de Informática

Licitación N\* TFEP-01/2026 - Bases Técnicas Transversales \* Información falsa o engañosa comprobada.

\* Ausencia de la información crítica exigida en el numeral 23.1.

\* Casos de éxito no verificables o cuyas contrapartes desmientan lo declarado. \* Plagio de contenido de otros sitios. 23.3 Declaración de veracidad

El PROPONENTE deberá incluir en el Sobre N\* 1 una declaración jurada simple que indique: e A e NE

Que La La dirección autorización toda la información oficial para del que sitio publicada la web Comisión de en la Evaluadora empresa. el sitio es verídica contacte y se a las encuentra referencias actualizada. declaradas. El compromiso de mantener el sitio activo durante todo el proceso.

La aceptación de la descalificación en caso de información falsa.

# CAPÍTULO 24 - VIDEO DE PRESENTACIÓN DE LA PROPUESTA 24.1 Especificaciones técnicas

Audio Música Duración Resolución Formato de archivo Cuadros por segundo Tasa de bits de video Tamaño máximo del archivo Orientación Aspectos visuales 24.2 Estructura y contenido

44,1 30 5 500 Opcional, Máximo MP4 Mbps fps MB. kHz con como como 5 y códec con minutos 16 mínimo. bits mínimo. licencia H.264. como (300 acreditable. mínimo, segundos). en Excederlo AAC o MP3, produce con niveles descalificación normalizados, automática. sin distorsión Full HD, 1920 ni ruido x 1080 de píxeles fondo excesivo. como mínimo. Horizontal (apaisada).

Iluminación profesional adecuada, fondo neutro o corporativo, sin efectos que distraigan del mensaje y con transiciones suaves.

El video deberá contener los siguientes segmentos, en este orden:

1. Introducción corporativa: logotipo animado, nombre del proyecto y del caso, fecha de la propuesta y nombre del proponente.

2. Comprensión del problema: análisis de la problemática actual, impacto en las personas afectadas, riesgos de no implementar la solución, métricas del problema identificado y demostración de comprensión del sector.

3. Solución propuesta: visión general, beneficios para cada grupo de interés, diferenciadores clave,

innovaciones incluidas y resultados esperados con métricas.

Bases Técnicas Transversales TFEP-01/2026 40/51

# O.

## Propuesta tecnológica: conjunto tecnológico completo, arquitectura de alto nivel, servicios de nube

## utilizados, y seguridad y cumplimiento normativo.

## relevantes, garantías y compromisos, y valor agregado único.. Ventajas competitivas: por qué el proponente es la mejor opción, experiencia específica, casos de éxito

Cierre y compromiso: compromiso con el proyecto, datos de contacto e identidad corporativa final.

## 24.3 Participación del equipo

Todos los integrantes clave del equipo deberán aparecer individualmente

presentándose, en toma de medio cuerpo, mirando directamente a la cámara, con

RT-24.01, N e - E Obligatorio vestimenta formal o de negocio informal, y con una duración mínima de aparición de 10 segundos por persona. Cada vez que aparezca un integrante deberá mostrarse en pantalla su nombre RT-24.02 completo, su cargo en el proyecto, sus años de experiencia y su especialización Obligatorio relevante. RT-24.03 Las certificaciones principales de cada integrante podrán mostrarse en pantalla. Deseable El fondo será el mismo para todas las tomas de personas, con iluminación.. RT-24.04. N \_ Obligatorio consistente y encuadre similar para todos los participantes. La paleta de colores corporativa, la tipografía y el uso de la marca serán consistentes RT-24.05 en todo el video, con logotipo visible en todas las escenas y datos de contacto en el Obligatorio encabezado o pie. Los niveles de volumen estarán normalizados, con la misma calidad de grabación.. RT-24.06 td Y Obligatorio sin variaciones bruscas de sonido.

24.4 Evaluación, penalizaciones y descalificación

# je -.é--\].\]\]\]\]\] Audio con problemas menores Iluminación deficiente Transiciones bruscas Información poco clara Falta de un rol no crítico del equipo Duración superior a 5 minutos No aparición del equipo clave completo

Calidad técnica inferior a la especificada en el numeral 24.1 Información falsa o engañosa

Uso de material con derechos de autor sin licencia No entrega del video junto con la propuesta 24.5 Entrega, derechos y autorizaciones

-5 puntos -5 puntos -5 puntos -5 puntos -5 puntos Descalificación automática Descalificación automática Descalificación automática Descalificación automática Descalificación automática Descalificación automática

\* Entrega física: unidad de almacenamiento USB junto con la propuesta, etiquetada con el nombre de la

empresa y del proyecto, incluyendo archivo de respaldo.

Bases Técnicas Transversales TFEP-01/2026 41/51

\* Entrega digital: enlace de descarga con vigencia mínima de 60 días, sin restricciones de descarga y con la contraseña de acceso en documento separado.

\* El PROPONENTE autoriza el uso del video para fines de evaluación y su proyección en las sesiones de evaluación.

\* El PROPONENTE garantiza que posee todos los derechos necesarios sobre el material utilizado.

\* La Comisión Evaluadora mantendrá la confidencialidad del contenido, no lo distribuirá sin autorización y eliminará las copias posteriores a la evaluación de las propuestas no seleccionadas.

# CAPÍTULO 25 - PROTOTIPO INTERACTIVO DE INTERFAZ Y DISEÑO UX/UI 25.1 Objetivo y momento de entrega

El PROPONENTE deberá presentar, junto con el Informe 3, un prototipo interactivo de alta fidelidad que demuestre de manera clara y tangible la visión de diseño de interfaz propuesta para la solución del caso. El prototipo permite evaluar la comprensión del proponente sobre las necesidades reales de las personas

usuarias y su capacidad de traducirlas en una experiencia de uso adecuada.

El prototipo no requiere conexión con servicios de fondo ni con base de datos, pero debe simular de manera realista la navegación y los flujos de trabajo principales, permitiendo a los evaluadores experimentar la solución desde la perspectiva de los distintos perfiles de personas usuarias. 25.2 Alcance mínimo

El prototipo deberá incluir, como mínimo, las siguientes vistas y funcionalidades navegables:

Página de inicio pública; página de inicio con sesión iniciada y personalizada por perfil; Portal principal tablero principal con componentes configurables; menú de navegación completo y funcional; rastro de navegación y navegación contextual.

Pantalla de inicio de sesión unificada; registro de una nueva persona usuaria externa en al menos cinco pasos; recuperación de acceso; segundo factor de autenticación; y tablero de primer ingreso con recorrido guiado. Autenticación e incorporación

El flujo de negocio central de la industria asignada, de extremo a extremo, en al menos seis pasos, desde su inicio hasta su cierre, incluyendo los estados intermedios y el manejo de la excepción más frecuente. Proceso operacional principal del caso

Proceso Perfil de operacional terreno o de Un La vista segundo que utilizará flujo relevante, la persona con usuaria su listado, operacional su vista de en detalle, su puesto su creación real, incluida y su flujo su de secundario operación del caso versión aprobación móvil visual. y su comportamiento sin conexión, cuando el caso lo requiera.

Directorio de la contraparte externa del caso -clientes, proveedores, productores,

Gestión de terceros.., un E. pacientes, pasajeros-, su ficha completa, su evaluación y su historial.

Indicadores principales con visualizaciones; al menos seis tipos de gráfico distintos; Tablero analítico filtros por período y categoría; profundización desde el indicador hasta el detalle; y exportación de informes.

Gestión de personas usuarias, roles y permisos; parametrización; y consulta de Administración o auditoría.

Dos módulos adicionales A elección del PROPONENTE, pertinentes al caso.

Bases Técnicas Transversales TFEP-01/2026 42/51 25.3 Principios de diseño exigidos

# RT-25.01

# RT-25.02

# RT-25.03

# RT-25.04

# RT-25.05

Navegación intuitiva sin necesidad de manual, con un máximo de tres interacciones

Obligatorio para alcanzar cualquier funcionalidad principal. E

Retroalimentación visual clara ante cada acción, estados de carga y transición fluidos,

Obligatorio y manejo elegante de los errores. E

| CumplimientodeWCAG2.2nivelAA:contrasteadecuado,tamañosdefuente | legibles,objetivostáctilesdealmenos44x44píxeles,navegacióncompletaporObligatorio | teclado,ytextosalternativosyetiquetasdeaccesibilidad. |
|:--- |:--- |:--- |
| Diseñoresponsivodemostradoenescritorio(1920x1080y1366x768),tableta(768 | x1024enverticalyhorizontal)yteléfono(375x812),conpuntosdequiebreObligatorio | coherentes. |
| Sistemadediseñodocumentado:paletadealomáscincocoloresprincipales,alo | másdosfamiliastipográficasjerarquizadas,iconografíacoherente,retículayObligatorio | espaciadoconsistentes,ycomponentesreutilizables. |

Diseño responsivo demostrado en escritorio (1920 x 1080 y 1366 x 768), tableta (768 x 1024 en vertical y horizontal) y teléfono (375 x 812), con puntos de quiebre Obligatorio coherentes.

Sistema de diseño documentado: paleta de a lo más cinco colores principales, a lo más dos familias tipográficas jerarquizadas, iconografía coherente, retícula y Obligatorio espaciado consistentes, y componentes reutilizables. 25.4 Componentes de interfaz obligatorios Componentes que el prototipo debe demostrar

## Navegación Formularios

Menú principal, menú secundario contextual, rastro de navegación, paginación, pestañas y acordeones, navegación por pasos y menú de acciones rápidas.

Campos de texto con validación en tiempo real, selectores y desplegables, casillas y botones de opción, selectores de fecha y hora, carga de archivos con arrastrar y soltar, autocompletado y formularios de múltiples pasos.

Tablas con ordenamiento y filtrado, gráficos de barras, de líneas y circulares, tarjetas de

Visualización de datos información, líneas de tiempo, indicadores de progreso, distintivos y etiquetas, e información contextual emergente.

Mensajes de éxito, error, advertencia e información; ventanas modales y diálogos;

Retroalimentación notificaciones emergentes; esqueletos de carga; indicadores de progreso; y estados vacíos Acción ilustrados.

Botones primarios, secundarios y terciarios; botón de acción flotante; acciones en línea; menús contextuales; acciones masivas; y confirmación de acciones críticas. 25.5 Entrega y nivel de interactividad

# RT-25.06

# RT-25.07

# RT-25.08

# RT-25.09

El prototipo se entregará como enlace navegable en línea, sin instalación ni,, Obligatorio complementos, compatible con los navegadores modernos vigentes.

El acceso al prototipo estará garantizado por un mínimo de seis meses desde su

## Obligatorio entrega.

El prototipo permitirá navegación completa entre pantallas, simulación de ingreso de datos, transiciones y animaciones básicas, estados de posado y activo, simulación de Obligatorio carga de archivos, elementos desplegables funcionales y simulación de validaciones.

Se entregará la arquitectura de información del prototipo: mapa del sitio completo, diagrama de navegación, taxonomía y nomenclatura, estructura de menús y jerarquía Obligatorio de la información.

Bases Técnicas Transversales TFEP-01/2026 43/51

Se valorará la posibilidad de exportar el prototipo a un documento interactivo para RT-25.10 ietAn ai A revisión sin conexión. Deseable 25.6 Restricciones y penalizaciones No se requiere Se penalizará

Conexión Funcionalidad Persistencia a base de real la de información de datos. servicios ingresada. de fondo. Prototipos Diseños Falta de genéricos responsividad estáticos, sin no personalización en navegables. los tamaños al exigidos. caso. Procesamiento real de datos. Incumplimiento de los estándares de accesibilidad. Integración con servicios externos. Navegación confusa o enlaces rotos. Autenticación real. Inconsistencias visuales evidentes. 25.7 Propiedad intelectual del diseño

\* El diseño propuesto será de propiedad del CLIENTE si la propuesta resulta adjudicada, conforme al Artículo 84\* de las Bases Administrativas.

## \* El PROPONENTE mantiene los derechos sobre sus componentes genéricos y sobre su sistema de diseño preexistente.

\* Se autoriza el uso del prototipo para fines de evaluación y para su proyección en las sesiones de evaluación.

e El CLIENTE mantendrá la confidencialidad de los diseños no seleccionados.

# CAPÍTULO 26 - INNOVACIONES

La exigencia de innovación se establece en el Capítulo 5 de las Bases Administrativas: cinco innovaciones obligatorias, una por cada tipo, con los siete elementos del Artículo 29\* documentados en el Formulario T-19. Este capítulo agrega las exigencias técnicas de su formulación.

Cada innovación se ubicará explícitamente en la arquitectura: qué capa la contiene,

RT-26.01, A 25 Obligatorio qué componentes la implementan y qué interfaces consume o expone. Cada innovación identificará los paquetes de la estructura de descomposición del:: RT-26.02.: paq T: Obligatorio trabajo que la ejecutan y el mes del cronograma en que se materializa. Las innovaciones de base tecnológica declararán el nivel de madurez de la tecnología.. RT-26.03 " e Obligatorio con la escala utilizada y citarán las fuentes en norma APA 7.2 edición. Cada innovación declarará su riesgo de adopción, su probabilidad, su impacto, la RT-26.04 '.- E Sopcion, su pro! y pacto, Obligatorio estrategia de mitigación y el plan de contingencia si no rinde lo esperado. Cada innovación declarará su indicador de verificación con línea base, meta y RT-26.05 momento de medición, y su impacto en inversión, costo operacional y beneficio Obligatorio esperado. Las innovaciones que incorporen inteligencia artificial cumplirán íntegramente el Y RT-26.06 q h E h 5 Obligatorio Capítulo 18 de este documento.

Bases Técnicas Transversales TFEP-01/2026 44/51

| LasinnovacionesquemodifiquenlaarquitecturadeseguridadrequeriránsupropiosA | RT-26.07Obligatorio | modeladodeamenazas. |
|:--- |:--- |:--- |
| Sevaloraráquealmenosunainnovaciónseaverificabledurantelamarchablancade | RT-26.08.\_.Deseable | laEtapa1,esdecir,quesubeneficiopuedamedirseantesdelmes16. |
| Noseaceptarácomoinnovaciónlasolaadopcióndeunatecnologíaqueyaconstituyeestándardela | industria,lamencióndeunatendenciasindiseñodeincorporación,niunafuncionalidadexigidaporlas | BasesTécnicaspresentadacomoinnovación.Lapertinenciaalcasopesamásquelanovedadtecnológica |

Se valorará que al menos una innovación sea verificable durante la marcha blanca de RT-26.08. \_. Deseable la Etapa 1, es decir, que su beneficio pueda medirse antes del mes 16.

No se aceptará como innovación la sola adopción de una tecnología que ya constituye estándar de la industria, la mención de una tendencia sin diseño de incorporación, ni una funcionalidad exigida por las Bases Técnicas presentada como innovación. La pertinencia al caso pesa más que la novedad tecnológica en abstracto.

Bases Técnicas Transversales TFEP-01/2026 45/51

Pontificia Universidad Católica de Valparaíso - Escuela de Informática

# CAPÍTULO A

# ÍNDICE DE REQUISITOS TRANSVERSALES

Licitación N\* TFEP-01/2026 - Bases Técnicas Transversales

Resumen de los requisitos codificados de este documento. El PROPONENTE deberá pronunciarse sobre la totalidad de ellos en el Formulario T-12.

A estos requisitos se suman los del Capítulo 4 de las Bases Administrativas y la totalidad de los

requerimientos funcionales, volúmenes y criterios de aceptación de las Bases Técnicas del caso asignado.

Site Site Modelo secundario principal de arquitectura on-premise y recuperación de referencia ante desastres Modelo Hardware, híbrido: puestos nube de y trabajo on-premise y terreno Ambientes, Desempeño, entrega capacidad continua y escalabilidad y configuración Datos, Disponibilidad, integración continuidad e interoperabilidad y resiliencia Seguridad de la información Identidad, acceso y sesiones

Usabilidad, accesibilidad y experiencia de usuario

Observabilidad Inteligencia artificial y gestión y automatización del servicio Sostenibilidad, Estructura y gobierno eficiencia del y proyecto certificaciones Módulos Implantación, transversales pruebas y obligatorios aceptación Canales Operación, digitales mantención y movilidad y soporte Capacitación y transferencia de conocimiento Información corporativa y presencia digital Video de presentación de la propuesta Prototipo interactivo y diseño UX/UI

# RT-02.01 -RT-02.14

# RT-03.01 -RT-03.24 24

RT-04.01 -RT-04.14 14 RT-05.01 - RT-05.30 30 RT-06.01 - RT-06.34 34 RT-07.01 -RT-07.14 14 RT-08.01 -RT-08.19 19 RT-09.01 -RT-09.10 10 RT-10.01 -RT-10.09 9 RT-11.01- RT-11.28 28 RT-12.01-RT-12.13 13 RT-13.01--RT-13.12 12 RT-14.01 -RT-14.09 9 RT-15.01 -RT-15.09 9 RT-16.01 -RT-16.34 34 RT-17.01-RT-17.08 8 RT-18.01-RT-18.10 10 RT-19.01 - RT-19.10 10 RT-20.01 - RT-20.08 8 RT-21.01 - RT-21.22 22 RT-22.01.- RT-22.09 9 RT-23.01 - RT-23.10 10 RT-24.01 -RT-24.06 6 RT-25.01-RT-25.10 10

Bases Técnicas Transversales TFEP-01/2026 46/51 Innovaciones RT-26.01 - RT-26.08

# TOTAL DE REQUISITOS CODIFICADOS 374

# CAPÍTULO B - PLANTILLA DE VOLUMETRÍA

Las Bases Técnicas de cada caso entregan la volumetría real de la industria correspondiente, completando la siguiente plantilla. El PROPONENTE deberá dimensionar su solución sobre esos valores y declarar el margen de crecimiento considerado.

Transacciones Volumen Contrapartes Personas Personas Documentos de usuarias usuarias almacenamiento procesados externas de negocio concurrentes registradas activas al anuales año transaccional Transacciones por segundo en régimen normal Transacciones por segundo en peak

Volumen de almacenamiento documental y multimedia

Volumen Integraciones de datos con sistemas históricos internos a migrar Integraciones Dispositivos de con terreno sistemas en operación externos Sitios Contactos u operaciones mensuales a al cubrir centro de atención

## Ventana operacional crítica (horario y estacionalidad)

# CAPÍTULO C - CHECKLIST DE ENTREGABLES DE LA OFERTA TÉCNICA

Lista de verificación para el PROPONENTE. No reemplaza a los formularios del Anexo B de las Bases Administrativas ni altera sus exigencias. Documento de arquitectura conforme a

RT-02.03 Sobre N\* 2 ISO/IEC/IEEE 42010, con las cinco vistas

2 Registro de decisiones de arquitectura (ADR) RT-02.04 Sobre N\* 2

Bases Técnicas Transversales TFEP-01/2026 47/51

Pontificia Universidad Católica de Valparaíso - Escuela de Informática

| Tabladeemplazamientodecomponentesennube | yon-premise,justificada |
|:--- |:--- |
| Declaracióndefuncionesnodisponiblesenmodo | desconectado |
| Modelodedatosydiccionariodedatos | Plandemigracióndedatos |
| DocumentacióndeinterfacesenOpenAPIy | AsyncAPI |
| Especificacióndelsiteprincipalydelsite | secundario,conplanos |
| Planderecuperaciónantedesastresypolíticade | respaldo |
| Especificacióndelhardwareydelosdispositivos | deterreno |

Declaración de funciones no disponibles en modo desconectado

Modelo de datos y diccionario de datos Plan de migración de datos

Documentación de interfaces en OpenAPI y AsyncAPI

Especificación del site principal y del site secundario, con planos

Plan de recuperación ante desastres y política de respaldo

Especificación del hardware y de los dispositivos de terreno Cálculo de capacidad y dimensionamiento

Plan de continuidad del negocio conforme a ISO

Modelado de amenazas y matriz de controles de seguridad

Declaración de la superficie de exposición de la solución Plan de respuesta a incidentes de seguridad

Modelo de identidad, matriz de roles y segregación de funciones

| Sistemadediseñoeinformedeconformidadde | accesibilidad |
|:--- |:--- |
| Estrategiadeobservabilidadycatálogodealertas | Certificadosinstitucionalesydelpersonal |
| Estrategiadepruebasyplandepruebas | (FormularioT-13) |
| Plandeimplantaciónydemarchablanca | (FormularioT-18) |
| Modelodeoperación,soportey | dimensionamientodelcentrodeatención |
| Plandecapacitaciónydetransferenciade | conocimiento |
| Matrizdecumplimientotécnico(FormularioT-12) | sobretodosloscódigosRT |
| Sitiowebcorporativoactivoydeclaraciónjurada | deveracidad |

Estrategia de observabilidad y catálogo de alertas Certificados institucionales y del personal

## Estrategia de pruebas y plan de pruebas (Formulario T-13)

Plan de implantación y de marcha blanca (Formulario T-18)

Modelo de operación, soporte y dimensionamiento del centro de atención

Plan de capacitación y de transferencia de conocimiento

Matriz de cumplimiento técnico (Formulario T-12) sobre todos los códigos RT

Sitio web corporativo activo y declaración jurada de veracidad Video de presentación de la propuesta

Licitación N\* TFEP-01/2026 - Bases Técnicas Transversales

Cap. 3 Sobre N\* 2 RT-03.13 Sobre N\*2 RT-05.01 Sobre N\* 2 RT-05.11 Sobre N\* 2 RT-05.16 Sobre N\* 2 Caps. 6 y 7 Sobre N\* 2 Cap. 7 Sobre N\* 2 Cap. 8 Sobre N\* 2 RT-09.01 Sobre N\* 2 RT-10.03 Sobre N\* 2 RT-11.02 y RT-11.05 Sobre N\* 2 RT-11.13 Sobre N\* 2 RT-11.18 Sobre N\* 2 Cap. 12 Sobre N\* 2 Cap. 13 Sobre N\* 2 Cap. 14 Sobre N\* 2 Cap. 15 SobreN\* 1 y N\*2 Cap. 20 Sobre N\* 2 RT-20.01 Sobre N\* 2 Cap. 21 Sobre N\* 2 Cap. 22 Sobre N\* 2 Numeral 1.5 Sobre N\* 2 Cap. 23 SobreN\* 1 Cap. 24 Con la propuesta final

Bases Técnicas Transversales TFEP-01/2026 48/51

Prototipo interactivo y arquitectura de información \|» Cap. 25 Con el Informe 3

28 \| Fichas de las cinco innovaciones (Formulario T-19) Cap.26 Sobre N\* 2

# CAPÍTULO D - GLOSARIO Y DEFINICIONES

Complementa el Artículo 3\* de las Bases Administrativas. Ante discrepancia, prevalece la definición de dicho artículo. Término Definición

Architecture Decision Record. Registro fechado de una decisión de arquitectura, sus

ADR AFIS API ASVS Automated Application Application; Security Fingerprint Programming Verification Identification Interface. Standard, Interfaz System. de de Sistema OWASP. programación automatizado Estándar que de expone verificación de identificación capacidades de por de alternativas huella un sistema dactilar. a y otro. su fundamento.

## seguridad de aplicaciones.

Capa CDN CIS Benchmarks anticorrupción. yu Componente Content Guías de Delivery configuración que Network. traduce. segura el Red modelo publicadas de distribución de un por sistema el de Center contenidos. externo for Internet al modelo Security. propio, impidiendo que aquel contamine este.

Patrón que interrumpe las llamadas a una dependencia en falla para evitar la propagación Cortacircuitos del error.

Despliegue azul-verde Estrategia que mantiene dos entornos productivos y conmuta el tráfico entre ellos.

Despliegue DevSecOps Erlang FCR FM-200 C canario Agente Estrategia Integración Modelo First Call limpio de Resolution. que teoría de de expone las extinción de prácticas colas Resolución la nueva empleado de de incendios, seguridad versión en el para primer a apto en una dimensionar el contacto. fracción para ciclo recintos de creciente desarrollo centros con de equipamiento del y atención. operación. tráfico. electrónico. laC Infrastructure as Code. Infraestructura definida como código versionado.. Propiedad de una operación que produce el mismo resultado aunque se ejecute varias Idempotencia

OpenTelemetry MITTR NOC NCh veces. Mean Network Norma Estándar Time Chilena Operations abierto To Restore. Oficial, de instrumentación Center. emitida Tiempo Centro por medio el de para Instituto de operaciones restauración métricas, Nacional de registros del red. de servicio. Normalización. y trazas. ITIL Marco de buenas prácticas para la gestión de servicios de tecnologías de información. Mamparo de Patrón que separa recursos por grupo de consumo para que la falla de uno no agote los del aislamiento resto.

Bases Técnicas Transversales TFEP-01/2026 49/51

Pontificia Universidad Católica de Valparaíso - Escuela de Informática

Licitación N\* TFEP-01/2026 - Bases Técnicas Transversales Término Definición OWASP Percentil 95

# PMBOK

# PMO Presupuesto de error

# PUE

# RAID RPO RTO

# sBOM SIEM SLA / SLO / SLI SLSA Soc SRE

# STRIDE

# TPS UAT WAF

# WCAG Zero Trust

## Open Worldwide Application Security Project.

Valor bajo el cual se encuentra el 95 % de las mediciones. Refleja la experiencia de la cola lenta, no el promedio.

Guía de fundamentos para la dirección de proyectos, del Project Management Institute. Project Management Office. Oficina de gestión de proyectos.

Fracción de indisponibilidad admitida por el objetivo de nivel de servicio, empleada para regular el ritmo de cambios.

Power Usage Effectiveness. Relación entre la energía total consumida por un recinto y la consumida por el equipamiento de Til.

Software Redundant Recovery Bill Point Array of Objective. Materials. of Independent Máxima Inventario Disks. pérdida de Arreglo los de componentes datos redundante tolerada, de de un expresada discos. artefacto en de tiempo. software. Recovery Time Objective. Máximo tiempo tolerado para restituir el servicio.

Security Information and Event Management. Plataforma de correlación de eventos de seguridad.

Acuerdo, objetivo e indicador de nivel de servicio.

Supply-chain Levels for Software Artifacts. Marco de niveles de seguridad de la cadena de suministro de software.

Security Operations Center. Centro de operaciones de seguridad. Site Reliability Engineering. Disciplina de operación de sistemas basada en ingeniería.

Metodología de modelado de amenazas: suplantación, manipulación, repudio, divulgación, denegación y elevación de privilegios.

Transactions Web Web User Acceptance Application Content Per Accessibility Second. Testing. Firewall. Transacciones Pruebas Cortafuegos Guidelines. de aceptación Pautas de por aplicaciones segundo. de accesibilidad de usuario. web. para el contenido web.

Modelo de seguridad en que ninguna red, dispositivo, identidad o carga de trabajo es confiable por defecto.

Bases Técnicas Transversales TFEP-01/2026 50/51