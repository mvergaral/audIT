# CAPÍTULO II: COMPRENSIÓN DEL PROBLEMA Y DE LA NECESIDAD

**Licitación N.º TFEP-01/2026 — Caso 10: Transportes Curimón S.A.**
**Dupla 1 (D1) — Subdocumento 2**

---

## 2.1 Contexto Estratégico y Territorial de Transportes Curimón S.A.

### 2.1.1 El Territorio Operacional: 3.000 km, Nodos Críticos y Zonas de Sombra

Transportes Curimón S.A. despliega su operación de carga terrestre a lo largo de un corredor logístico de aproximadamente **3.000 kilómetros lineales**, extendido desde Antofagasta por el norte hasta Puerto Montt por el sur, con un ramal internacional que cruza la Cordillera de los Andes a través del **Paso Los Libertadores**. Este último constituye un nodo de altísima criticidad operacional: el paso acumula un promedio histórico de **1.900 cortes y cierres** por condiciones climáticas invernales, con episodios de interrupción que alcanzan hasta **12 días consecutivos** de inoperabilidad. La materialización de estos cierres no solo detiene los vehículos en tránsito, sino que genera un efecto cascada sobre la programación completa de la flota, las obligaciones contractuales con exportadores y la capacidad de reasignación de recursos en la torre de despacho.

La infraestructura fija de Curimón se articula en torno a una red de **5 terminales operacionales** distribuidos a lo largo del corredor: **Antofagasta**, **Coquimbo**, **San Bernardo (Santiago)**, **Concepción** y **Puerto Montt**. Complementariamente, la empresa opera **2 talleres principales de mantención** localizados en **San Bernardo** y **Concepción**, que concentran las capacidades de mantenimiento preventivo y correctivo de la flota propia. Esta disposición geográfica de nodos fijos —cinco puntos de contacto en 3.000 km— implica que los tramos entre terminales superan ampliamente las distancias que permiten una supervisión presencial periódica, y que extensas franjas del corredor quedan fuera del alcance directo de cualquier instalación de la empresa.

La extensión territorial plantea, por tanto, un primer problema estructural de naturaleza geográfica: la dispersión espacial de los activos móviles impide cualquier forma de supervisión presencial continua. Los **374 tractocamiones** que gestiona la empresa transitan simultáneamente por una red vial donde conviven tramos de autopista concesionada con segmentos de ruta interurbana sin bermas adecuadas, zonas desérticas del norte grande con extensiones superiores a **60-80 km sin infraestructura de detención segura**, y corredores de alta congestión en la zona central vinculados a la industria frutícola y portuaria.

La consecuencia directa de esta configuración territorial es la existencia de lo que operacionalmente puede denominarse **"zonas de sombra"**: franjas geográficas donde la empresa carece de visibilidad sobre la posición, el estado mecánico y la condición del conductor que opera el vehículo. Esta opacidad territorial se agrava por un dato estructural del caso: **34 camiones carecen por completo de dispositivo GPS**, y los restantes **340 camiones con GPS** están distribuidos en **3 plataformas de rastreo distintas e incompatibles entre sí**, lo que obliga a la torre de despacho a operar con tres pantallas simultáneas sin capacidad de correlación automática de datos.

Desde la perspectiva de la gobernanza del dato posicional, Curimón enfrenta un problema de **fragmentación de la fuente de verdad territorial**. No existe una visión única y consolidada de dónde se encuentra cada activo en un momento dado. La torre de despacho —compuesta por **22 operadores en turnos 24/7**— recurre a la **memoria humana y llamadas telefónicas** como mecanismo primario de asignación y seguimiento, lo cual introduce latencia, errores de juicio y una dependencia crítica del conocimiento tácito individual de cada operador.

### 2.1.2 La Dinámica de Negocio: Redundancia, Subcontratación y Margen Operacional del 9%

Transportes Curimón S.A. opera bajo un modelo de negocio mixto que combina flota propia con subcontratación extensiva de capacidad de transporte. La empresa gestiona **374 tractocamiones**: **148 camiones propios** (39,6% de la flota) y **226 camiones subcontratados** (60,4%) pertenecientes a **148 dueños independientes**. Complementariamente, la empresa posee **210 semirremolques propios** que se acoplan indistintamente a tractocamiones propios y de terceros.

Este modelo de negocio genera una dinámica de redundancia operacional necesaria pero costosa: la empresa debe mantener una base de activos propios suficiente para honrar compromisos contractuales mínimos, mientras que recurre masivamente a la subcontratación para absorber peaks de demanda, cubrir rutas de baja rentabilidad y compensar la indisponibilidad de vehículos propios por mantenimiento o siniestralidad.

La escala de la operación es significativa: aproximadamente **96.000 viajes anuales** que totalizan cerca de **41.000.000 de kilómetros recorridos por año**. Sin embargo, una cifra revela una ineficiencia logística de primer orden: el **26% de los kilómetros totales se recorren en vacío**, lo que equivale a aproximadamente **10,66 millones de kilómetros anuales sin carga**. Esta redundancia kilométrica no solo representa un costo directo de combustible, peajes, desgaste de neumáticos y depreciación acelerada, sino que evidencia una incapacidad estructural de la torre de despacho para optimizar la triangulación de cargas de retorno.

El margen operacional consolidado de la empresa es de apenas un **9%**, una cifra que por sí sola revela la fragilidad financiera de la operación. Más preocupante aún es la composición interna de dicho margen: **3 de los 8 contratos principales operan bajo costo**, y estos tres contratos representan el **31% del ingreso total de la compañía**. El caso más extremo corresponde a un contrato que ha operado a un **margen negativo del −14%** durante **4 años consecutivos**. Esta situación configura un patrón de **subsidios cruzados ocultos**, donde los contratos rentables financian la pérdida sostenida de los deficitarios sin que exista un mecanismo analítico que permita a la gerencia identificar, cuantificar y corregir esta distorsión de forma oportuna.

La causa raíz de esta opacidad financiera reside en el método de **asignación histórica de costos prorrateada por volumen de ingreso**: un criterio que distribuye los costos operacionales proporcionalmente a la facturación de cada contrato, en lugar de imputarlos analíticamente al consumo real de recursos (kilómetros recorridos, horas de conducción, combustible consumido, peajes pagados, mantenciones efectuadas) de cada ruta, viaje y contrato específico. Esta metodología enmascara sistemáticamente la verdadera rentabilidad de cada operación y priva a la gerencia de la información necesaria para tomar decisiones de negociación tarifaria, abandono de contratos deficitarios o reestructuración de rutas.

---

## 2.2 La Fractura Estructural: La Brecha entre Responsabilidad Legal y Control Operacional

> [!IMPORTANT]
> **Declaración formal del problema raíz:** Transportes Curimón S.A. soporta la **totalidad de la responsabilidad civil, comercial, regulatoria y reputacional** derivada de cada viaje que gestiona ante clientes, autoridades fiscalizadoras y terceros afectados, pero carece de **tuición operacional directa** sobre el **60,4% de los vehículos** (226 camiones subcontratados) y el **56,8% de los conductores** (258 choferes externos) que ejecutan materialmente dichos viajes.

Esta fractura estructural constituye el **problema central** que atraviesa transversalmente todos los dominios operacionales de la compañía: seguridad vial, cumplimiento normativo, eficiencia logística, control financiero y gestión comercial. No se trata de un problema funcional aislado ni de una deficiencia de un proceso particular, sino de un **desacople sistémico** entre la arquitectura jurídico-comercial del negocio y la arquitectura de control operacional de la empresa.

La magnitud de este desacople se manifiesta en datos concretos:

- **Control de jornada:** Curimón posee un control precario de la jornada de sus **196 conductores propios** (limitado a los momentos de presencia en terminal), y tiene **cero visibilidad** sobre la jornada previa de los **258 conductores externos** al momento de asignarles un flete. Este punto ciego quedó trágicamente expuesto en el siniestro del **km 312**, donde se determinó que el conductor externo involucrado tenía **11 horas de descanso simulado** en sus registros, habiendo en realidad conducido para otro cliente inmediatamente antes de tomar el flete de Curimón.

- **Retorno a terminales:** Los camiones propios retornan a un terminal de Curimón en promedio cada **6 días**, lo que ya limita la frecuencia de inspecciones presenciales, verificación documental y descarga de datos. Pero el problema se agudiza dramáticamente con la flota subcontratada: el **22% de los camiones de terceros** pasa menos de **1 vez al mes** por un terminal de la empresa. Esto significa que para una fracción significativa de su capacidad operativa, Curimón opera esencialmente "a ciegas" respecto del estado mecánico del vehículo, la vigencia documental del conductor y las condiciones reales de prestación del servicio.

- **Datos de operación:** **61 tractocamiones propios** cuentan con telemetría de fábrica CANbus que transmite datos de motor, consumo, frenado y velocidad, pero esta capacidad está **completamente inactiva**: los datos nunca han sido descargados ni analizados. De forma análoga, la empresa tiene **0 descargas de tacógrafos digitales** a pesar de que estos instrumentos son **obligatorios por ley**. Esta doble inactividad configura una paradoja: la empresa posee hardware instalado capaz de generar evidencia objetiva del comportamiento operacional de sus vehículos y conductores, pero no ha establecido los procesos, competencias ni rutinas organizacionales necesarios para transformar esos datos en información de gestión y cumplimiento.

La fractura entre responsabilidad y control no es una condición estática: se está agravando progresivamente por la convergencia de presiones regulatorias crecientes (fiscalización de jornada, normativa hazmat, control de emisiones), exigencias contractuales del cliente exportador clave (trazabilidad del 100% de los viajes para la renovación de contrato en 2029) y la propia inercia de crecimiento de la flota subcontratada como mecanismo de flexibilidad comercial.

---

## 2.3 Diagnóstico Cuantitativo del Dolor Operacional (Los 7 Bloques de Datos Duros)

### Bloque 1: Estructura de Flota y Asimetría de Tenencia

La configuración de activos de Curimón revela una **asimetría estructural de tenencia** que condiciona todo el modelo de control:

| Indicador | Valor | Implicancia |
|:---|:---|:---|
| Tractocamiones gestionados | 374 | Escala operacional que excede la capacidad de control manual |
| Camiones propios | 148 (39,6%) | Minoría de la flota bajo tuición directa |
| Camiones subcontratados | 226 (60,4%) | Mayoría de la flota sin tuición directa |
| Dueños independientes | 148 | Alta fragmentación de la propiedad; 148 interlocutores con intereses divergentes |
| Semirremolques propios | 210 | Acople con tractocamiones propios y de terceros: punto de contacto físico entre ambas flotas |
| Retorno a terminal (propios) | Cada 6 días | Ventana limitada para inspección, verificación y descarga de datos |
| Retorno a terminal (subcontratados) | 22% pasa < 1 vez/mes | Punto ciego operacional: fracción de la flota virtualmente invisible |

La asimetría de tenencia implica que Curimón ha externalizado la propiedad del activo principal (el tractocamión) pero no ha podido externalizar la **responsabilidad** que le es jurídicamente imputable como operador logístico mandante. Los 148 dueños independientes mantienen soberanía sobre sus vehículos: deciden a qué otros operadores prestan servicio, cuándo llevan sus camiones a mantención, qué conductores contratan y qué información comparten o retienen. La empresa, por su parte, carece de mecanismos contractuales, operacionales o informativos que le permitan verificar de forma independiente el cumplimiento de estándares mínimos cuando el activo no está físicamente presente en sus terminales.

### Bloque 2: Fuerza Laboral y Brecha de Control de Jornada

| Indicador | Valor | Implicancia |
|:---|:---|:---|
| Conductores programados | 454 | Fuerza laboral distribuida en territorio extenso |
| Conductores propios | 196 (43,2%) | Control de jornada precario, limitado a presencia en terminal |
| Conductores externos | 258 (56,8%) | Control de jornada **inexistente** por parte de Curimón |
| Descargas de tacógrafo digital | 0 | Incumplimiento normativo total; ausencia de evidencia objetiva de jornada |
| Caso km 312 | 11 h de descanso simulado | Evidencia de riesgo sistémico: el conductor había operado para otro cliente sin descanso real |

La **brecha de control de jornada** es quizás la vulnerabilidad más grave del modelo operacional de Curimón, tanto por sus implicancias de seguridad vial como por su exposición legal. La normativa vigente (Art. 25 bis del Código del Trabajo) establece límites estrictos de jornada de conducción y descanso obligatorio para conductores de transporte de carga interurbana. Sin embargo, Curimón no tiene forma de conocer qué actividad realizó un conductor externo **antes** de tomar un flete de la empresa. El siniestro del km 312 no es un evento aislado sino la manifestación tangible de un riesgo latente en cada uno de los aproximadamente **96.000 viajes anuales** donde participan conductores externos: la empresa despacha vehículos confiando en la declaración verbal del conductor sobre su estado de descanso, sin contar con ningún registro objetivo que respalde o contradiga dicha declaración.

La absoluta ausencia de descargas de tacógrafo digital agrava esta situación: incluso para los conductores propios, la empresa carece de registros instrumentales que permitan verificar el cumplimiento de jornada, establecer patrones de fatiga o generar evidencia de descargo ante un eventual proceso judicial o fiscalización laboral.

### Bloque 3: Eficiencia y Dinámica de Rutas

| Indicador | Valor | Implicancia |
|:---|:---|:---|
| Viajes anuales | ≈ 96.000 | Alta frecuencia de despacho; presión sobre la torre de control |
| Kilómetros anuales | ≈ 41.000.000 | Escala que amplifica cualquier ineficiencia porcentual |
| Extensión territorial | 3.000 km | Dispersión que impide supervisión presencial |
| Kilómetros en vacío | 26% (≈ 10,66 M km/año) | Redundancia logística masiva; costo operacional sin contraprestación de ingreso |
| Operadores de torre | 22 (turnos 24/7) | Asignación por memoria humana y llamadas telefónicas |
| Paso Los Libertadores | 1.900 cierres; hasta 12 días | Nodo de alta volatilidad que desestabiliza la programación |

El dato de **10,66 millones de kilómetros recorridos en vacío** por año merece un análisis particular. Cada kilómetro en vacío consume combustible (el rubro representa el **14% del ingreso total** de la compañía), desgasta neumáticos, acumula peajes, genera depreciación del activo y ocupa horas de conducción que podrían destinarse a viajes productivos. En una operación con margen del 9%, la reducción de incluso una fracción de este porcentaje de vacío tendría un impacto directo y mensurable en la rentabilidad consolidada.

La causa raíz de esta ineficiencia se localiza en el método de asignación de la torre de despacho: **22 operadores humanos** que programan **96.000 viajes anuales** apoyándose en su memoria individual, conocimiento tácito de la disponibilidad de conductores y comunicación telefónica. Este esquema de asignación carece de visibilidad sobre la posición actual de todos los vehículos disponibles, las cargas de retorno potencialmente triangulables y las ventanas de tiempo óptimas para minimizar el recorrido sin carga. La asignación por memoria humana no solo es subóptima desde el punto de vista logístico, sino que es además **irrepetible y no auditable**: no existe registro de por qué se asignó un determinado camión a un determinado viaje, ni es posible evaluar retrospectivamente si existía una alternativa más eficiente.

### Bloque 4: Desgobierno de Datos, Vigencias y Hardware Ocioso

| Indicador | Valor | Implicancia |
|:---|:---|:---|
| Fechas de vencimiento vivas | ≈ 6.000 | Licencias, revisiones, seguros, cursos en vigilancia simultánea |
| Soporte de gestión | 4 planillas Excel aisladas | Sin integridad referencial, sin alertas automatizadas, sin auditoría de cambios |
| Descargas de tacógrafo | 0 | Incumplimiento legal; dato de jornada inutilizado |
| Tractocamiones con CANbus inactivo | 61 propios | Hardware de telemetría instalado de fábrica, nunca descargado |
| Camiones sin GPS | 34 | Invisibilidad posicional total |
| Camiones con GPS | 340 en 3 plataformas incompatibles | Fragmentación de la visibilidad; 3 pantallas en torre sin integración |

Este bloque revela un patrón de **desgobierno de datos** que opera en tres niveles simultáneos:

**Nivel 1 — Datos existentes pero no gestionados:** Las **≈ 6.000 fechas de vencimiento** constituyen un corpus de información crítica para el cumplimiento normativo (un curso vencido puede derivar en una infracción grave, como ocurrió en abril 2026 con la carga hazmat), pero su gestión está dispersa en **4 planillas Excel aisladas**. Estas planillas carecen de integridad referencial cruzada, no generan alertas proactivas de próximo vencimiento, no registran quién modificó qué dato ni cuándo, y son susceptibles a errores de digitación, duplicación y omisión. La consecuencia práctica es que el vencimiento de un documento crítico solo se detecta cuando ya se ha materializado la infracción.

**Nivel 2 — Datos generados pero no capturados:** Los **61 tractocamiones propios con telemetría CANbus** y los tacógrafos digitales de la flota generan datos continuamente durante cada viaje: velocidad, RPM, consumo instantáneo, temperatura de motor, eventos de frenado brusco, tiempos de conducción y descanso. Sin embargo, estos datos **nunca se descargan**. La empresa posee el hardware pero no ejecuta el proceso de extracción, almacenamiento y análisis. El resultado es una pérdida sistemática de información que podría fundamentar decisiones de mantenimiento predictivo, cumplimiento de jornada y optimización de consumo.

**Nivel 3 — Datos capturados pero no integrados:** Los **340 camiones con GPS** generan datos de posición, pero la distribución en **3 plataformas incompatibles** obliga a los operadores de torre a alternar entre tres interfaces distintas sin posibilidad de correlacionar la información en una vista unificada. Esta fragmentación reduce la utilidad operacional del dato posicional y aumenta la probabilidad de error humano en la coordinación de flota.

### Bloque 5: Fricción Comercial, Esperas y Liquidación a Terceros

| Indicador | Valor | Implicancia |
|:---|:---|:---|
| Espera promedio en clientes | 3 h 10 min | Tiempo improductivo del activo y del conductor |
| Espera máxima (temporada fruta) | Hasta 8 h | Pico estacional que multiplica la ineficiencia |
| Sobreestadías facturadas | $340 M CLP/año | Ingreso potencial por compensación del tiempo de espera |
| Cobros objetados por clientes | 71% ($241,4 M CLP) | Pérdida cuasi-cierta por falta de prueba fehaciente |
| Respaldos ilegibles/incompletos | 4,2% | Documentación manual que no soporta disputa comercial |
| Proceso de liquidación mensual | 9 días hábiles, 8 personas | Alto consumo de recursos administrativos |
| Notas de corrección post-emisión | 11% | Indicador de error sistemático en el cálculo de liquidación |

Este bloque cuantifica una **hemorragia financiera crónica** directamente atribuible a la incapacidad de la empresa para generar prueba fehaciente de los tiempos de espera en instalaciones de clientes. Curimón factura anualmente **$340 millones CLP** por concepto de sobreestadías, pero el **71% de estos cobros** —equivalente a **$241,4 millones CLP**— es objetado y no percibido porque la empresa no puede demostrar de forma incontrovertible la hora de ingreso y la hora de salida del vehículo en las instalaciones del cliente.

En el contexto de un margen operacional del 9%, la no percepción de $241,4 millones CLP anuales representa una erosión directa de la rentabilidad que es enteramente atribuible a una deficiencia de registro y documentación, no a una condición intrínseca del mercado o de la operación física. La causa raíz es la dependencia de **respaldos documentales manuales** (guías, timbres, anotaciones) que resultan ilegibles, incompletos o insuficientes como prueba ante la objeción del cliente.

Paralelamente, el **proceso de liquidación mensual a los 148 transportistas subcontratados** consume **9 días hábiles** y la dedicación de **8 personas** del área administrativa. El **11% de notas de corrección post-emisión** indica que más de 1 de cada 10 liquidaciones contiene errores que deben ser detectados, reclamados por el transportista, corregidos, re-emitidos y re-aprobados. Este ciclo de corrección no solo consume recursos adicionales sino que deteriora la relación comercial con los dueños de camiones subcontratados, quienes perciben la liquidación como un proceso opaco, tardío y propenso a errores en su perjuicio.

### Bloque 6: Estructura Financiera y Distorsión de Costos

| Indicador | Valor | Implicancia |
|:---|:---|:---|
| Margen operacional consolidado | 9% | Fragilidad ante cualquier incremento de costos o pérdida de ingresos |
| Contratos bajo costo | 3 de 8 principales | Subsidios cruzados ocultos; rentabilidad aparente distorsionada |
| Peor contrato | −14% de margen, 4 años consecutivos | Destrucción sostenida de valor no corregida |
| Peso de contratos deficitarios | 31% del ingreso | Magnitud significativa del ingreso proveniente de operaciones no rentables |
| Costo de combustible | 14% del ingreso | Segundo rubro de costo más relevante |
| Desfase de registro de combustible | Hasta 40 días | Información de costos disponible con rezago que impide gestión oportuna |
| Método de costeo | Prorrateo por volumen de ingreso | Enmascara subsidios cruzados; impide costeo analítico por viaje/ruta/contrato |

La **distorsión de costos** constituye un problema de gobernanza financiera de primer orden. El método de prorrateo por volumen de ingreso asigna costos a cada contrato en proporción a lo que factura, no en proporción a lo que consume. Esto genera una ilusión óptica contable: los contratos de mayor facturación absorben proporcionalmente más costos aunque sus rutas sean más eficientes, mientras que los contratos de menor facturación parecen menos costosos aunque sus rutas sean más largas, más complejas o más intensivas en combustible.

El resultado práctico es que la gerencia no dispone de la información necesaria para responder preguntas fundamentales de gestión: ¿Cuál es el costo real por kilómetro de cada ruta? ¿Cuánto cuesta servir a cada cliente por tonelada transportada? ¿Qué contratos generan valor y cuáles destruyen valor? La persistencia de un contrato a **−14% de margen durante 4 años consecutivos** es evidencia directa de esta ceguera analítica: si el dato estuviera visible, cuantificado y atribuido correctamente, la decisión de renegociar o abandonar ese contrato debería haberse tomado años antes.

El **desfase de hasta 40 días en el registro de combustible** agrava la distorsión: el rubro que representa el **14% del ingreso** total se contabiliza con un rezago que impide cualquier forma de control de gestión en tiempo operacional. La gerencia conoce el costo real de combustible de un viaje solo semanas después de que el viaje se completó, cuando la oportunidad de corrección o ajuste ya ha caducado.

### Bloque 7: Seguridad Operacional, Sobrepeso e Incumplimiento Normativo

| Indicador | Valor | Implicancia |
|:---|:---|:---|
| Detenciones por sobrepeso (2025) | 142 | Frecuencia inaceptable; patrón recurrente, no incidental |
| Inmovilización promedio por evento | 18 h | Pérdida de productividad directa del activo y el conductor |
| Horas-camión perdidas por sobrepeso | 2.556 h/año | Equivalente a más de 106 días-camión completos inoperativos |
| Infracción hazmat (abril 2026) | 1 grave; 14 h inmovilización | Curso vencido 3 semanas atrás; falla de vigilancia documental |
| Siniestros con lesiones (3 años) | 4 (1 grave en febrero 2026) | Riesgo de vida, costo humano, exposición judicial y reputacional |
| Exigencia del exportador clave | Trazabilidad 100%, posición real, e-Docs, CO₂e | Condición no negociable para renovación de contrato 2029 |
| Peso del exportador clave en ingresos | 19% | Pérdida de este contrato comprometería la viabilidad del negocio |

Las **142 detenciones por sobrepeso** en 2025 no pueden interpretarse como eventos aislados o accidentales: su frecuencia configura un **patrón de incumplimiento recurrente** que sugiere una falla estructural en el proceso de carga, verificación de peso y despacho. Cada detención genera un promedio de **18 horas de inmovilización**, lo que totaliza **2.556 horas-camión perdidas** en el año. Este dato debe leerse en el contexto de una operación que lucha por optimizar cada hora productiva de sus activos: las 2.556 horas equivalen a más de **106 jornadas completas de 24 horas** donde un tractocamión y su conductor están detenidos sin generar ingreso alguno, además de las multas, costos de descarga parcial y daño reputacional asociados.

La infracción por transporte de carga peligrosa (hazmat) de **abril 2026** es un caso emblemático del fracaso en la vigilancia de vigencias documentales: el curso obligatorio del conductor estaba **vencido 3 semanas atrás**, un lapso que se sitúa dentro del horizonte normal de cualquier mecanismo de alerta proactivo razonablemente diseñado. El hecho de que esta expiración no haya sido detectada hasta que se materializó la fiscalización en ruta confirma que las **4 planillas Excel aisladas** que gestionan las ≈ 6.000 fechas de vencimiento no constituyen un mecanismo efectivo de control.

Los **4 siniestros con lesiones en los últimos 3 años**, incluyendo **1 siniestro grave en febrero 2026**, configuran una tendencia de siniestralidad que, además de su costo humano primario, expone a la empresa a consecuencias judiciales, regulatorias y comerciales de magnitud potencialmente existencial.

Finalmente, la **exigencia del cliente exportador clave** —que representa el **19% de los ingresos** de Curimón— establece un horizonte temporal no negociable: para la **renovación de contrato en 2029**, la empresa debe demostrar capacidad de trazabilidad de jornada en el **100% de los viajes** (incluyendo los operados por terceros), posición en tiempo real, documentación electrónica (e-Docs) y reporte auditado de emisiones de **CO₂e por tonelada-kilómetro**. El incumplimiento de estas condiciones no implicará una penalización dentro del contrato, sino la **no renovación del contrato mismo**, con la consiguiente pérdida del 19% de los ingresos de la compañía —un impacto que, sobre un margen del 9%, podría comprometer la viabilidad financiera de la empresa.

---

### Tabla Maestra de Síntomas, Causas Raíz e Impactos Económicos/Legales

| N.º | Síntoma Observable | Causa Raíz | Impacto Económico / Legal |
|:---:|:---|:---|:---|
| S1 | 0 descargas de tacógrafo; 258 conductores sin control de jornada | Ausencia de proceso de descarga y de mecanismo de verificación de jornada previa de externos | Exposición legal por incumplimiento Art. 25 bis; riesgo de siniestralidad por fatiga (caso km 312) |
| S2 | 26% de km en vacío (10,66 M km/año) | Asignación por memoria humana sin visibilidad de posición ni de cargas de retorno disponibles | Costo directo de combustible, peajes y desgaste sin contraprestación de ingreso; erosión del margen del 9% |
| S3 | $241,4 M CLP/año en cobros de sobreestadía no percibidos | Incapacidad de generar prueba fehaciente de hora de ingreso/salida en instalaciones de clientes | Pérdida directa de ingreso equivalente a un porcentaje significativo del margen operacional |
| S4 | 142 detenciones por sobrepeso; 2.556 h-camión perdidas | Falla en el proceso de verificación de peso en carga y despacho | Multas, inmovilización, pérdida de productividad, daño reputacional ante clientes y autoridades |
| S5 | 3 contratos a margen negativo (peor: −14%) durante 4 años | Costeo por prorrateo que enmascara subsidios cruzados; desfase de 40 días en registro de combustible | Destrucción sostenida de valor; financiamiento oculto de contratos deficitarios por los rentables |
| S6 | 6.000 vigencias en 4 Excel; infracción hazmat por curso vencido 3 semanas | Dispersión de datos en planillas sin alertas, sin integridad referencial y sin auditoría de cambios | Infracciones regulatorias; riesgo de prohibición de operar en rutas hazmat; exposición penal en caso de siniestro con carga peligrosa |
| S7 | 61 camiones con CANbus inactivo; 340 GPS en 3 plataformas | Hardware instalado sin proceso de descarga; plataformas no interoperables | Pérdida de datos de operación generados pero no capturados; fragmentación de visibilidad en torre |
| S8 | Liquidación de 9 días, 8 personas, 11% correcciones | Proceso manual intensivo sin verificación cruzada automatizada | Costo administrativo, tensión con 148 transportistas, demora en cierre contable mensual |
| S9 | 22% de flota subcontratada pasa < 1 vez/mes por terminal | Modelo de subcontratación sin mecanismo de verificación remota | Punto ciego total sobre estado mecánico, documental y de jornada de fracción relevante de la flota |
| S10 | Exigencia de exportador clave no satisfecha (trazabilidad, CO₂e, e-Docs) | Brecha entre las capacidades actuales de registro y las exigencias contractuales de 2029 | Riesgo de no renovación del contrato que representa el 19% de los ingresos |

---

## 2.4 Mapa de Actores y Grupos de Interés (Stakeholder Analysis)

### 2.4.1 Matriz de Poder/Influencia vs. Nivel de Interés

La siguiente matriz clasifica a los 10 actores identificados en el caso según su **capacidad de influir** en las decisiones organizacionales (poder) y su **grado de involucramiento** en la problemática diagnosticada (interés).

```
                         ALTO INTERÉS                          BAJO INTERÉS
              ┌───────────────────────────────┬──────────────────────────────┐
              │        GESTIONAR DE CERCA      │     MANTENER SATISFECHO      │
   ALTO       │                               │                              │
   PODER      │ • Gerencia General            │                              │
              │ • Operaciones (R. Mansilla)   │                              │
              │ • Exportadora Clave           │                              │
              │   (A. Lecaros)                │                              │
              │ • Finanzas (G. Ossandón)      │                              │
              ├───────────────────────────────┼──────────────────────────────┤
              │       MANTENER INFORMADO       │          MONITOREAR          │
   BAJO       │                               │                              │
   PODER      │ • Prevención (D. Aguayo)      │                              │
              │ • Taller (H. Trincado)        │                              │
              │ • Torre de Despacho           │                              │
              │ • Conductores Propios         │                              │
              │ • Conductores Externos        │                              │
              │   (Y. Colipán)                │                              │
              │ • 148 Dueños Subcontratados   │                              │
              │   (N. Sandoval)               │                              │
              └───────────────────────────────┴──────────────────────────────┘
```

> [!NOTE]
> Los 148 Dueños Subcontratados (representados por N. Sandoval) poseen **bajo poder formal** dentro de la estructura de Curimón, pero ejercen una **alta capacidad de bloqueo colectivo**: si un número significativo de ellos retira sus camiones de la operación, la empresa pierde el 60,4% de su capacidad de flota. Esta asimetría entre poder formal e influencia real los convierte en un actor de gestión crítica.

### 2.4.2 Tabla de Caracterización de Actores

| Actor | Expectativas Principales | Temores Principales | Capacidad de Bloqueo | Necesidades de Información |
|:---|:---|:---|:---|:---|
| **Gerencia General** | Rentabilidad sostenible; cumplimiento normativo total; renovación del contrato del exportador clave 2029; reducción de siniestralidad | Pérdida del contrato del 19%; sanción regulatoria grave; siniestro fatal con consecuencias penales; erosión del margen del 9% | Máxima: autoridad decisional final sobre inversiones, contratos y política operacional | Costeo analítico por contrato y ruta; indicadores de cumplimiento normativo; estado de avance hacia exigencias 2029 |
| **Operaciones (R. Mansilla)** | Continuidad del despacho sin interrupciones; máxima utilización de flota; cumplimiento de ventanas de entrega | Parálisis operacional por bloqueos de seguridad excesivos; penalizaciones comerciales por atrasos; pérdida de clientes por incumplimiento de SLA | Alta: controla la asignación diaria de los 374 tractocamiones y define prioridades de despacho | Posición de flota en tiempo real; disponibilidad de conductores; estado de cargas de retorno; alertas de incumplimiento que no paralicen la operación |
| **Finanzas (G. Ossandón)** | Visibilidad de rentabilidad real por contrato; cierre contable oportuno; costeo analítico por ruta y viaje | Mantener subsidios cruzados ocultos; desfase perpetuo en el registro de combustible; incapacidad de fundamentar renegociación tarifaria | Media-alta: capacidad de escalar alertas financieras a gerencia y condicionar la aprobación de nuevos compromisos contractuales | Costo real desglosado por viaje (combustible, peajes, mantención, horas-conductor); margen real por contrato; conciliación de liquidaciones |
| **Prevención de Riesgos (D. Aguayo)** | Cumplimiento irrestricto de normativa de jornada, habilitaciones y seguridad; bloqueo de salidas ante cualquier incumplimiento documental | Ser considerada obstruccionista; que un siniestro ocurra por una excepción operacional que ella no autorizó; exposición personal por omisión de fiscalización | Media: puede vetar despachos por incumplimiento, pero enfrenta presión constante de Operaciones para flexibilizar | Vigencia en tiempo real de todos los documentos (licencias, revisiones, seguros, cursos hazmat); registros objetivos de jornada; historial de siniestralidad |
| **Taller (H. Trincado)** | Confiabilidad mecánica de la flota; mantenimiento preventivo según plan; registro completo de intervenciones | Fallas mecánicas en ruta por mantenimiento diferido; reparaciones de emergencia en talleres externos sin registro; pérdida de garantías por falta de trazabilidad de servicio | Baja-media: puede recomendar baja de vehículos pero la decisión final es de Operaciones y Gerencia | Kilometraje acumulado por vehículo; datos de CANbus (temperatura, presión, códigos de falla); historial unificado de mantenciones propias y de terceros |
| **Torre de Despacho (22 operadores)** | Herramientas de trabajo que faciliten la asignación; reducción de llamadas telefónicas; visibilidad unificada de flota | Sobrecarga de decisiones con información insuficiente; errores de asignación por falta de datos; responsabilización por fallas de información que no controlan | Baja formal, pero alta operacional de facto: son el cuello de botella de cada despacho y su desempeño individual condiciona la eficiencia de toda la cadena | Vista única de posición de todos los vehículos; disponibilidad de conductores habilitados; cargas de retorno disponibles; estado de vigencias documentales |
| **Conductores Propios (196)** | Condiciones laborales seguras; descanso efectivo; jornada respetada; equipo mecánico confiable | Fiscalización excesiva que no considere la realidad vial; sanciones por situaciones fuera de su control; riesgo de asalto en detenciones en zonas inseguras | Baja individual, pero colectiva mediante sindicato o ausentismo concertado | Rutas con información de puntos seguros de detención; confirmación de que el vehículo asignado está en condiciones mecánicas adecuadas |
| **Conductores Externos (Y. Colipán, 258)** | Flexibilidad; ingresos estables; no ser sometidos a control excesivo por un operador que no es su empleador directo | Que Curimón intente controlar su jornada completa incluyendo servicios a otros operadores; pérdida de autonomía laboral; sanciones por incumplimiento de normas que no fueron comunicadas oportunamente | Media colectiva: pueden rechazar fletes de Curimón y optar por competidores con menos exigencias | Condiciones del flete antes de aceptarlo; puntos de descanso seguro; claridad sobre qué obligaciones documentales les corresponden |
| **148 Dueños Subcontratados (N. Sandoval)** | Flujo de fletes constante; liquidación oportuna y transparente; respeto de la soberanía sobre su activo | Que Curimón rastree sus camiones cuando prestan servicio a otros operadores; que les impongan costos o inversiones sin contraprestación; liquidaciones con errores recurrentes | Alta colectiva: retiro masivo de camiones colapsaría la capacidad operativa de Curimón (60,4% de la flota) | Detalle transparente de la liquidación; calendario de pagos; condiciones contractuales claras sobre uso de datos de su vehículo |
| **Exportadora Clave (A. Lecaros, 19% ingreso)** | Trazabilidad de jornada 100% (propios y terceros); posición en tiempo real; e-Docs; reporte de CO₂e/ton-km auditado; cumplimiento para renovación 2029 | Siniestro con su carga; incumplimiento regulatorio que comprometa su cadena de suministro; falta de evidencia para auditorías de sostenibilidad de sus propios clientes | Máxima externa: condición de renovación de contrato no negociable; pérdida de este actor equivale a pérdida del 19% del ingreso | Trazabilidad completa de cada viaje (conductor, jornada, ruta, posición, documentos, emisiones); acceso a reportes auditables |

---

## 2.5 Hallazgos Críticos y Matriz de Tensiones Operacionales (Análisis del Capítulo 8)

La sistematización de las 10 entrevistas del Capítulo 8 del Caso 10 revela **5 tensiones estructurales** que no son anomalías de gestión sino consecuencias lógicas de la fractura entre responsabilidad y control descrita en la sección 2.2. Cada tensión representa una **incompatibilidad verificable entre objetivos legítimos** de distintos actores que, en ausencia de información confiable y procesos de arbitraje basados en datos, se resuelve ad hoc mediante negociación informal, imposición jerárquica o simple omisión.

### Tensión 1: Seguridad vs. Continuidad Operacional

**Actores en conflicto:** Denisse Aguayo (Prevención de Riesgos) vs. Ricardo Mansilla (Operaciones).

**Naturaleza del conflicto:** Denisse Aguayo sostiene que ningún vehículo debe salir del terminal si presenta cualquier incumplimiento documental —licencia vencida, revisión técnica pendiente, curso hazmat expirado, o falta de certificación de descanso del conductor—. Su posición se fundamenta en la obligación legal de la empresa y en la experiencia del siniestro de febrero 2026. Ricardo Mansilla, por su parte, opera bajo la presión de **96.000 despachos anuales** con **22 operadores** en turno continuo y clientes con ventanas de entrega rígidas: un bloqueo de salida no solo detiene un camión, sino que puede desencadenar una cascada de incumplimientos contractuales con penalizaciones comerciales directas.

**Diagnóstico analítico:** Esta tensión es irresoluble bajo las condiciones actuales porque ambas posiciones son legítimas y el mecanismo de arbitraje es inexistente. No existe un protocolo basado en datos que permita distinguir entre un incumplimiento documental crítico (conductor con jornada excedida, curso hazmat vencido para carga peligrosa) y un incumplimiento menor (revisión técnica que vence mañana pero el vehículo fue inspeccionado ayer). La ausencia de esta gradación obliga a Prevención a adoptar una política de tolerancia cero (con el riesgo de paralizar despachos) o a transigir caso a caso (con el riesgo de que la excepción se convierta en norma). El dato de las **6.000 vigencias gestionadas en 4 planillas Excel** agrava la tensión: ni siquiera hay certeza compartida sobre cuáles documentos están efectivamente vencidos y cuáles no, lo que transforma cada despacho en una negociación de información contradictoria.

**Impacto en el margen del 9%:** Cada despacho detenido innecesariamente genera un costo de inactividad del activo y del conductor, y potencialmente una penalización comercial. Cada despacho liberado indebidamente genera un riesgo de multa, siniestro o inmovilización que puede ser órdenes de magnitud mayor.

---

### Tensión 2: Visibilidad vs. Soberanía del Activo

**Actores en conflicto:** Andrea Lecaros (Exportadora Clave) vs. Nolberto Sandoval (representante de los 148 Dueños Subcontratados).

**Naturaleza del conflicto:** Andrea Lecaros exige, como condición no negociable para la renovación del contrato en 2029, **tracking en tiempo real** de cada vehículo que transporta su carga, independientemente de si es propio o subcontratado. Esta exigencia responde a las obligaciones de trazabilidad de su propia cadena de suministro y a estándares de sostenibilidad de sus clientes internacionales. Nolberto Sandoval, en representación de los dueños de camiones, se opone a que Curimón rastree sus vehículos **cuando estos están prestando servicios a otros operadores o competidores directos de Curimón**. Su argumento es de soberanía patrimonial: el camión es su activo, y la información de su utilización fuera del contrato con Curimón es información comercial confidencial que puede ser usada en su perjuicio.

**Diagnóstico analítico:** Esta tensión revela un conflicto de intereses de información que es inherente al modelo de subcontratación. Curimón necesita la información de posición para satisfacer a su cliente exportador (19% del ingreso), pero los 148 dueños de camiones perciben esa misma información como una amenaza a su independencia comercial. Crucialmente, la posición de Sandoval no es solo un reclamo de conveniencia empresarial: la **Ley N° 21.719 sobre Protección de Datos Personales** —que refuerza el marco de la Ley N° 19.628 y armoniza la normativa chilena con estándares internacionales de protección de datos— reconoce la **geolocalización como dato personal** cuyo tratamiento requiere base de licitud, proporcionalidad y finalidad específica. En consecuencia, el rastreo continuo de un vehículo de propiedad de un tercero durante períodos en que **no** está prestando servicio a Curimón podría constituir un tratamiento de datos personales sin base de licitud, otorgando al transportista un **amparo legal expreso** para oponerse a dicho rastreo. Esta dimensión jurídica transforma la tensión de un problema puramente comercial a un problema de cumplimiento normativo bidireccional: Curimón debe satisfacer las exigencias de trazabilidad de su cliente exportador sin vulnerar los derechos de protección de datos de sus transportistas subcontratados. Actualmente, la empresa no puede ofrecer garantías verificables sobre el uso exclusivo de los datos de posición para el período en que el camión opera para Curimón, ni cuenta con un marco contractual que delimite con precisión los derechos de uso de la información posicional conforme a las exigencias de la Ley N° 21.719. La existencia de **34 camiones sin GPS** y la fragmentación en **3 plataformas incompatibles** agrava la tensión: incluso si se lograra un acuerdo de principio, la infraestructura actual es incapaz de implementar un rastreo selectivo, delimitado y auditable.

**Impacto en el contrato 2029:** Si esta tensión no se resuelve, Curimón no podrá cumplir la exigencia de trazabilidad del 100% de los viajes (incluyendo los operados por terceros), lo que precipitaría la no renovación del contrato que representa el 19% de los ingresos.

---

### Tensión 3: Jornada Legal vs. Geografía Vial

**Actores en conflicto:** Normativa vigente (Art. 25 bis del Código del Trabajo / Dirección del Trabajo) vs. Yasna Colipán (conductora representativa de los choferes de ruta).

**Naturaleza del conflicto:** La normativa laboral establece pausas de descanso obligatorias después de períodos determinados de conducción continua. Yasna Colipán, conductora con experiencia en la Ruta 5 Norte, expone una realidad geográfica que la norma no contempla: en el desierto de Atacama existen tramos de **más de 60-80 km sin bermas, estaciones de servicio ni zonas seguras de detención**. Detenerse en esos tramos para cumplir la pausa horaria expone al conductor a riesgos de **asalto, atropello o colisión por falta de espacio de detención seguro**. El conductor enfrenta un dilema binario: infringir la norma de jornada y continuar hasta un punto seguro (arriesgando sanción laboral y responsabilidad en caso de siniestro), o detenerse donde marca el reloj (arriesgando su integridad física).

**Diagnóstico analítico:** Esta tensión no es un problema de voluntad de cumplimiento sino un conflicto entre la abstracción normativa y la materialidad del territorio. La normativa asume la existencia de infraestructura vial que permita pausas seguras a intervalos regulares, una condición que no se cumple en segmentos significativos de la red vial que opera Curimón. El problema se agudiza porque la empresa carece de un **mapeo sistemático de puntos seguros de detención** a lo largo de sus 3.000 km de operación, y no dispone de información de contexto territorial que permita al despachador considerar las condiciones específicas de cada tramo al momento de programar un viaje y estimar los tiempos de descanso.

**Impacto en el margen del 9% y el riesgo legal:** Si un siniestro ocurre durante una pausa realizada en una zona insegura por cumplir la norma, la responsabilidad recae sobre la empresa. Si un siniestro ocurre por fatiga porque el conductor no se detuvo para evitar una zona insegura, la responsabilidad también recae sobre la empresa. La ausencia de un criterio documentado y basado en información territorial expone a Curimón a responsabilidad en ambos escenarios.

---

### Tensión 4: Visibilidad Financiera vs. Opacidad de Costos Reales

**Actores en conflicto:** Gabriela Ossandón (Finanzas) vs. la inercia organizacional del costeo por prorrateo.

**Naturaleza del conflicto:** Gabriela Ossandón ha identificado que **3 de los 8 contratos principales operan bajo costo** y que el peor de ellos arrastra un margen del **−14% durante 4 años consecutivos**. Sin embargo, carece de las herramientas y datos necesarios para realizar un **costeo analítico por tramo, viaje y contrato** que fundamente una renegociación tarifaria o una decisión de abandono. Los datos de combustible llegan con un **desfase de hasta 40 días**, y las tarifas pagadas a los 148 transportistas subcontratados son **planas** (no reflejan la variabilidad real del costo por ruta), lo que impide imputar correctamente el costo variable a cada servicio.

**Diagnóstico analítico:** Ossandón posee la hipótesis correcta (existen subsidios cruzados) y la evidencia parcial (margen negativo en 3 contratos), pero no dispone del **dato granular** que le permita convertir esa hipótesis en una demostración cuantitativa irrebatible ante la gerencia. El método de prorrateo no es una decisión deliberada de ocultamiento sino una inercia histórica: en una época de menor escala y menor complejidad, distribuir costos por volumen de ingreso podía ser una aproximación razonable. A la escala actual de **41 millones de kilómetros anuales**, **374 vehículos** y **8 contratos con perfiles de costo radicalmente distintos**, esa aproximación ya no es admisible.

La tensión se manifiesta además en el proceso de liquidación a terceros: las **8 personas** que durante **9 días hábiles** producen las liquidaciones mensuales operan con las mismas limitaciones de información que Finanzas, lo que explica el **11% de notas de corrección post-emisión**. Cada corrección es un síntoma de que el dato de entrada (kilómetros recorridos, combustible consumido, peajes pagados, horas de espera) no está capturado de forma confiable en el origen.

**Impacto en el margen del 9%:** La imposibilidad de costear analíticamente perpetúa la destrucción de valor en contratos deficitarios. Los **$241,4 millones no percibidos** por sobreestadías objetadas son otro síntoma de la misma raíz: sin dato fehaciente, no hay negociación posible.

---

### Tensión 5: Mantenimiento Técnico vs. Descentralización de Activos

**Actores en conflicto:** Hugo Trincado (Jefe de Talleres) vs. la realidad operacional de la flota subcontratada.

**Naturaleza del conflicto:** Hugo Trincado tiene como objetivo asegurar la **confiabilidad mecánica** de los vehículos que operan para Curimón, lo que requiere el cumplimiento de planes de mantenimiento preventivo basados en kilometraje y horas de operación, así como el registro completo de cada intervención mecánica para preservar garantías de fábrica y establecer trazabilidad de fallas. Sin embargo, el **60,4% de los camiones** (la flota subcontratada) **no pasa por el taller de San Bernardo** con regularidad alguna. Cuando un camión subcontratado sufre una falla mecánica en ruta, la reparación se realiza en talleres de terceros a lo largo de los 3.000 km de operación, y la documentación de esa intervención queda en **facturas sueltas** que en la mayoría de los casos **nunca se incorporan al historial técnico del equipo**.

**Diagnóstico analítico:** Esta tensión revela una **fragmentación del registro de vida del activo**. Un tractocamión subcontratado puede acumular cientos de miles de kilómetros y decenas de intervenciones mecánicas sin que Curimón tenga visibilidad sobre su estado real. Los **61 tractocamiones propios con CANbus inactivo** representan una versión menos extrema del mismo problema: el activo genera datos de diagnóstico mecánico continuamente, pero nadie los descarga ni los analiza, con lo cual Trincado programa mantenciones basándose en **intervalos calendario estimados** en lugar de en **condiciones operacionales reales**.

La consecuencia práctica es doble: (a) riesgo de falla mecánica en ruta por mantenimiento diferido o inadecuado, con los costos asociados de rescate, transferencia de carga, incumplimiento contractual y potencial siniestralidad; y (b) riesgo de **pérdida de garantías de fábrica** de los vehículos propios por incapacidad de demostrar el cumplimiento del plan de servicio recomendado por el fabricante, al no contar con un historial unificado y verificable de las intervenciones realizadas.

**Impacto en el margen del 9%:** Las fallas mecánicas en ruta generan costos de emergencia (grúa, taller externo, transferencia de carga) que pueden ser varias veces superiores al costo de un mantenimiento preventivo oportuno. La pérdida de garantías obliga a asumir como costo operacional reparaciones que deberían estar cubiertas por el fabricante.

---

### Matriz Consolidada de Tensiones

| Tensión | Polo A | Polo B | Variable en Disputa | Riesgo si Prevalece A | Riesgo si Prevalece B |
|:---:|:---|:---|:---|:---|:---|
| T1 | Prevención (bloqueo estricto) | Operaciones (continuidad) | Criterio de despacho | Parálisis operacional; penalizaciones comerciales | Siniestro; infracción regulatoria grave |
| T2 | Exportadora (tracking total) | 148 Dueños (soberanía del activo) | Alcance de la visibilidad posicional | Retiro de camiones subcontratados; pérdida de 60,4% de capacidad | No renovación del contrato 2029; pérdida del 19% del ingreso |
| T3 | Normativa DT (pausa rígida) | Conductora (geografía real) | Lugar y momento de descanso | Riesgo de asalto/accidente en zona insegura | Infracción de jornada; responsabilidad por fatiga |
| T4 | Finanzas (costeo analítico) | Inercia organizacional (prorrateo) | Granularidad del dato de costo | Ninguno (el escenario A es deseable pero inalcanzable sin datos) | Subsidios cruzados perpetuos; destrucción de valor en 31% del ingreso |
| T5 | Taller (mantenimiento preventivo) | Descentralización de activos (60,4% fuera de San Bernardo) | Registro y control del estado mecánico | Ninguno (el escenario A es deseable pero inalcanzable sin presencia física) | Fallas mecánicas en ruta; pérdida de garantías; siniestralidad mecánica |

---

## 2.6 Registro de Supuestos Declarados y Límites del Diagnóstico

El presente diagnóstico se ha elaborado sobre la base de la información disponible en el Caso 10 y las entrevistas del Capítulo 8. Sin embargo, existen **supuestos analíticos** que deben ser declarados explícitamente, así como **límites del diagnóstico** que condicionan la validez de ciertas conclusiones. Este registro se vincula particularmente con las **26 decisiones no tomadas** documentadas en el numeral 16.1 del caso, sobre las cuales la empresa no ha definido posición.

### Supuesto 1: Obtención de Jornada de Conductores Externos

El diagnóstico asume que Curimón reconoce la necesidad de obtener información verificable sobre la jornada previa de los 258 conductores externos, pero **no ha definido el mecanismo** mediante el cual se obtendrá esta información. Existen al menos tres interrogantes sin respuesta:

- ¿Los conductores externos estarán obligados contractualmente a declarar su jornada previa antes de aceptar un flete?
- ¿Se aceptará la declaración verbal como suficiente o se requerirá un registro instrumental?
- ¿Qué consecuencia operacional tendrá la negativa de un conductor externo a proporcionar esta información?

La respuesta a estas preguntas condiciona directamente la factibilidad de cumplir la exigencia de trazabilidad de jornada del 100% de los viajes requerida por el exportador clave para 2029.

### Supuesto 2: Adhesión de los 148 Transportistas Subcontratados

El diagnóstico identifica la tensión entre visibilidad y soberanía del activo (Tensión 2), pero asume que, en última instancia, será necesario lograr un **acuerdo de adhesión** con los 148 dueños de camiones para cualquier esquema de trazabilidad que incluya sus vehículos. Sin embargo, **no se ha establecido**:

- Si la adhesión será voluntaria o será condición contractual para continuar operando con Curimón.
- Si Curimón ofrecerá alguna contraprestación (prioridad de asignación de fletes, mejora en tiempos de liquidación, tarifas diferenciadas) a cambio de la participación del transportista.
- Si existe un **umbral mínimo de adhesión** bajo el cual el esquema de trazabilidad pierde su utilidad para el cumplimiento de la exigencia del exportador clave.
- Cuál sería el impacto operacional si un porcentaje significativo de los 148 transportistas rechazara la adhesión y retirara sus camiones de la operación.

### Supuesto 3: Preservación de Garantías de Vehículos

El diagnóstico señala que los **61 tractocamiones propios con CANbus inactivo** nunca han sido descargados, lo que implica una pérdida de datos de diagnóstico mecánico potencialmente relevantes para el mantenimiento preventivo y la preservación de garantías de fábrica. Se asume que:

- La activación de la descarga de datos CANbus no invalidará las garantías vigentes del fabricante.
- El proceso de descarga no requiere intervenciones de hardware que puedan ser interpretadas por el fabricante como modificaciones no autorizadas.
- La información extraída será propiedad de Curimón y podrá ser utilizada para fines de gestión interna sin restricciones contractuales del fabricante.

Estas asunciones deben verificarse con los contratos de adquisición y las condiciones de garantía de cada marca y modelo presente en la flota.

### Supuesto 4: Estabilidad del Marco Regulatorio

El diagnóstico toma como referencia la normativa vigente al momento de la elaboración del caso (Art. 25 bis del Código del Trabajo, regulación de carga peligrosa, obligatoriedad de tacógrafo digital). Se asume que el **marco regulatorio se mantendrá estable o se endurecerá** en el horizonte 2026-2029, lo que refuerza la urgencia de cerrar las brechas de cumplimiento identificadas. No obstante, eventuales modificaciones regulatorias (particularmente en materia de jornada de conducción, emisiones vehiculares o requisitos de trazabilidad digital) podrían alterar la magnitud y la prioridad relativa de los problemas diagnosticados.

### Supuesto 5: Veracidad y Completitud de los Datos del Caso

Se asume que los datos cuantitativos proporcionados en el Caso 10 (374 camiones, 96.000 viajes, 41 M km, 26% km vacío, $340 M sobreestadías, 142 detenciones, 9% margen, −14% peor contrato, entre otros) **son fidedignos y representan el estado real de la operación** al momento de la elaboración del caso. El análisis no ha podido verificar de forma independiente estas cifras, y cualquier inexactitud en los datos de entrada se propagaría a las conclusiones del diagnóstico.

### Supuesto 6: Integridad de los Testimonios del Capítulo 8

Las 5 tensiones identificadas se construyeron a partir de las declaraciones de los 10 entrevistados del Capítulo 8. Se asume que cada entrevistado expresó su posición de forma **honesta y representativa** de su rol, sin omisiones deliberadas ni sesgos por presión jerárquica. Las posibles dinámicas de poder dentro de la empresa (por ejemplo, la reticencia de un subordinado a contradecir a su superior directo en una entrevista) podrían haber atenuado o exacerbado la expresión de ciertas tensiones.

### Límite Explícito del Diagnóstico

> [!WARNING]
> El presente subdocumento describe, cuantifica y analiza los problemas y necesidades de Transportes Curimón S.A., pero **no propone ni insinúa ningún tipo de solución**. La formulación de la propuesta de intervención, la selección de alternativas y la definición de la arquitectura de respuesta corresponden a los subdocumentos posteriores, conforme a la estructura establecida por las bases de licitación y el Formulario T-22.

---

*Fin del Subdocumento 2 — Comprensión del Problema y de la Necesidad*
*Dupla 1 (D1) — Licitación N.º TFEP-01/2026*
*Caso 10: Transportes Curimón S.A.*
