# CAPÍTULO II: COMPRENSIÓN DEL PROBLEMA Y DE LA NECESIDAD

**Licitación N.º TFEP-01/2026 — Caso 10: Transportes Curimón S.A.**  
**Dupla 1 (D1) — Subdocumento 2**  
**Empresa Proponente: audIT**  

---


## 2.1 Síntesis Ejecutiva de la Situación Actual y Dimensión del Desafío

El diagnóstico estructural de Transportes Curimón S.A. revela una fractura fundamental que compromete la viabilidad operacional y financiera de la compañía: la asimetría insostenible entre la responsabilidad legal, comercial y regulatoria que la empresa asume frente a sus mandantes, y el control efectivo que ejerce sobre los recursos que ejecutan el servicio. La compañía soporta el cien por ciento de la responsabilidad sobre cargas, siniestros y fiscalizaciones, pero opera en un escenario donde el 60,4 % de su capacidad de transporte (226 camiones subcontratados de un total de 374) y el 56,8 % de sus operadores (258 conductores externos frente a 196 propios) no se encuentran bajo su tuición directa. Esta disociación genera un vacío de gobernanza sobre operaciones críticas ejecutadas a nombre de Curimón, conformando un riesgo latente de magnitudes incalculables.

La dimensión física del desafío amplifica esta fractura. La red logística moviliza 96.000 viajes anuales, totalizando 41 millones de kilómetros recorridos por una flota de 374 tractocamiones a lo largo de un corredor de 3.000 kilómetros entre Antofagasta y Puerto Montt, complementado por el cruce fronterizo del paso Los Libertadores. Este despliegue territorial extenso se administra con un nivel de fragilidad financiera agudo, evidenciado por un margen operacional consolidado de apenas el 9 %. El análisis pormenorizado del costeo expone un deterioro estructural grave: tres de los ocho contratos principales operan por debajo de la línea de costo, representando en conjunto el 31 % del ingreso total de la empresa. El caso más extremo documenta un contrato ejecutado con un margen negativo del 14 % durante cuatro años consecutivos, subsidiado sistemáticamente por rutas rentables bajo un modelo ciego de prorrateo por ingreso.

La materialización de este desacople estructural se concentró en tres eventos críticos durante el primer semestre de 2026. El 14 de febrero, el accidente en el kilómetro 312 de la Ruta 5 Sur demostró la ceguera de la compañía respecto a los tiempos de descanso previos de los conductores subcontratados. En abril, una fiscalización inmovilizó un vehículo con sustancias peligrosas por presentar un certificado vencido hacía tres semanas, evidenciando el colapso del sistema de control documental. Finalmente, en junio, el levantamiento de costos demostró las profundas deficiencias del modelo de asignación financiera. Estos eventos no constituyen fallas aisladas, sino manifestaciones directas de un ecosistema de datos desintegrado.

Este colapso de la gobernanza de datos se cuantifica en la gestión manual de aproximadamente 6.000 fechas de vencimiento vivas, distribuidas en cuatro planillas de cálculo aisladas que carecen de integridad referencial. A nivel de hardware instalado, se constata una omisión total en la extracción de evidencia: cero descargas de información de los tacógrafos digitales y 61 tractocamiones operando con telemetría CANbus de fábrica inactiva. En el plano de visibilidad, 34 camiones circulan sin dispositivo de posicionamiento GPS, mientras que los 340 restantes se monitorean a través de tres plataformas incompatibles, fragmentando la lectura de la torre de control. 

Frente a esta vulnerabilidad sistémica, la compañía enfrenta una amenaza existencial hacia el año 2029: el cliente exportador mayor, responsable del 19 % de los ingresos, ha condicionado la renovación de su contrato al cumplimiento de requisitos ineludibles. Estas exigencias imponen la necesidad de acreditar el cumplimiento de la jornada en cada viaje —incluyendo transportistas subcontratados—, contar con el cien por ciento de trazabilidad y posicionamiento de carga en tiempo real, digitalización integral de la documentación (e-Docs) y la emisión de reportes auditados de huella de carbono (CO2e) por tonelada-kilómetro. Esta matriz de condiciones demanda una transformación absoluta de los estándares probatorios de Transportes Curimón S.A., cerrando el margen para operaciones basadas en la invisibilidad de los activos de terceros.

## 2.2 Desglose Cuantitativo y Diagnóstico de los 7 Bloques de Datos Duros

### Bloque 1: Flota y Asimetría de Tenencia

| Indicador | Valor |
| :--- | :--- |
| Capacidad total gestionada | 374 tractocamiones |
| Flota propia | 148 tractocamiones (39,6 %) |
| Flota subcontratada | 226 tractocamiones (60,4 %) |
| Semirremolques propios | 210 equipos |
| Proveedores subcontratados | 148 dueños independientes |

> [!IMPORTANT]  
> El 60,4 % de la capacidad tractora principal no pertenece a la compañía, fragmentada entre 148 propietarios independientes que toman decisiones autónomas sobre el mantenimiento y disponibilidad de sus activos.

El análisis de la estructura de la flota evidencia una dependencia crítica hacia terceros que desequilibra la arquitectura de control. Curimón provee la interfaz comercial, los semirremolques propios y absorbe la responsabilidad del servicio, pero el activo motriz fundamental está bajo el mando de terceros. Esta asimetría de tenencia bloquea cualquier esfuerzo de estandarización tecnológica forzada y determina que las capacidades de trazabilidad o integración no pueden depender de imposiciones jerárquicas, configurando el principal obstáculo para asegurar la fiabilidad operacional.

### Bloque 2: Fuerza Conductora y Brecha de Jornada

| Indicador | Valor |
| :--- | :--- |
| Dotación total de conductores programados | 454 operadores |
| Conductores propios | 196 (43,2 %) |
| Conductores subcontratados (externos) | 258 (56,8 %) |
| Descargas de tacógrafo digital | 0 registros |
| Incidente de referencia (km 312) | Chofer externo con descanso simulado tras operar para otro cliente |

El ecosistema laboral de la compañía presenta una ceguera probatoria total frente a la normativa de tiempos de conducción y descanso. Con 258 conductores que no mantienen un vínculo laboral con Curimón y cero descargas históricas de tacógrafo, la empresa asigna viajes sin evidencia objetiva de la jornada previa del operador. El accidente del kilómetro 312 subraya la gravedad de esta fisura: el cumplimiento aparente de los registros internos de la empresa no garantiza el descanso real del conductor externo, exponiendo a la compañía a responsabilidades penales, civiles y comerciales sobre comportamientos que están fuera de su campo visual.

### Bloque 3: Red, Rutas y Fricción Logística

| Indicador | Valor |
| :--- | :--- |
| Volumetría anual | 96.000 viajes |
| Distancia anual recorrida | 41.000.000 de kilómetros |
| Operación en vacío | 26 % (10,66 millones de kilómetros) |
| Torre de programación | 22 operadores en turnos de 24x7 |
| Cruces fronterizos anuales (Paso Los Libertadores) | ≈ 1.900 cruces al año (cierres estacionales por nieve de hasta 12 días continuos) |

La coordinación de 41 millones de kilómetros anuales recae sobre una torre de control de 22 operadores que ejecutan la asignación de viajes sin soporte algorítmico, operando desde la memoria y la telefonía. El impacto más severo de este modelo es la generación de 10,66 millones de kilómetros recorridos sin carga, representando un 26 % de ineficiencia estructural directa sobre la capacidad rodante. A esta fricción logística se suma la volatilidad geográfica del paso Los Libertadores, cuyos cierres prolongados quiebran cualquier modelo estático de planificación de recursos, saturando la capacidad de respuesta manual del equipo de programación.

### Bloque 4: Desgobierno de Datos e Infraestructura Ociosa

| Indicador | Valor |
| :--- | :--- |
| Fechas de vencimiento vivas (estimado) | ~6.000 fechas |
| Soporte de control documental | 4 planillas de cálculo (Excel) aisladas |
| Telemetría CANbus inactiva | 61 tractocamiones propios |
| Camiones sin posicionamiento GPS | 34 tractocamiones |
| Plataformas de rastreo simultáneas incompatibles | 3 plataformas para 340 tractocamiones |

Se constata un estado de inoperatividad de los datos donde la captura, integración y alerta preventiva han fallado sistemáticamente. La mantención manual de cerca de 6.000 vigencias en hojas de cálculo inconexas garantiza la aparición de incidentes por vencimientos documentales no detectados. Al mismo tiempo, la empresa desperdicia activos tecnológicos de fábrica, como el CANbus de 61 tractocamiones que nunca ha sido consultado. La fragmentación de 340 vehículos en tres plataformas de monitoreo divergentes, sumado a los 34 camiones ciegos, destruye la posibilidad de conformar una vista operacional única.

### Bloque 5: Fricción Comercial y Tiempos de Espera

| Indicador | Valor |
| :--- | :--- |
| Tiempo medio de espera en puntos de carga | 3 horas 10 minutos (hasta 8 horas en temporada de fruta) |
| Cobros facturados por sobreestadía | $ 340.000.000 anuales |
| Cobros objetados / no recaudados por falta de prueba | 71 % ($ 241.400.000) |
| Proceso de liquidación mensual a terceros | 9 días de duración, 8 analistas involucrados |
| Tasa de refacturación / corrección en liquidaciones | 11 % |

La ausencia de registros de posicionamiento georreferenciado e inalterable genera una profunda merma financiera mediante la objeción del 71 % de los montos facturados por demoras en las instalaciones de clientes, representando $241,4 millones no recaudados. El soporte de papel, manipulable y de entrega diferida, fracasa como instrumento probatorio. Adicionalmente, el procesamiento de las liquidaciones de 148 dueños subcontratados exige 9 días de trabajo de 8 personas, resultando en un 11 % de notas de corrección post-emisión; un indicador de fricción que deteriora la confianza de los proveedores externos que sostienen la mayoría de la operación.

### Bloque 6: Estructura Financiera y Distorsión de Costos

| Indicador | Valor |
| :--- | :--- |
| Margen operacional consolidado | 9 % |
| Contratos principales bajo el costo | 3 de 8 contratos |
| Participación de los contratos bajo costo | 31 % del ingreso total |
| Caso crítico de rentabilidad negativa | -14 % de margen durante 4 años consecutivos |
| Combustible sobre ingreso y rezago contable | 14 % del ingreso; hasta 40 días de desfase probatorio |

La rentabilidad del 9 % encubre un modelo de gestión basado en prorrateos generales que impiden el costeo analítico a nivel de ruta y viaje. El descubrimiento de que el 31 % de los ingresos de la empresa proviene de tres contratos deficitarios —uno de ellos drenando un margen del -14 % durante cuatro años ininterrumpidos— es el resultado de operar a ciegas respecto de los costos reales de ejecución. El rubro de combustible, responsable del 14 % del gasto, opera bajo un esquema de facturación consolidada mensual que retrasa en 40 días la visualización del consumo, impidiendo relacionar el rendimiento energético con los hábitos de conducción o el desgaste mecánico.

### Bloque 7: Seguridad y Riesgo Existencial

| Indicador | Valor |
| :--- | :--- |
| Detenciones en ruta por exceso de peso (año 2025) | 142 eventos |
| Horas de inmovilización por sobrepeso | 2.556 horas-camión perdidas |
| Infracción Hazmat (abril 2026) | Curso vencido hace 3 semanas; 14 horas de inmovilización |
| Siniestros con lesiones (últimos 3 años) | 4 accidentes |
| Exigencias condicionantes del cliente principal (2029) | Trazabilidad 100 %, posición tiempo real, e-Docs, CO2e |

> [!IMPORTANT]  
> La imposibilidad de certificar los estándares operacionales ya no solo genera multas y tiempos muertos, sino que constituye una amenaza a la continuidad del negocio frente al ultimátum del cliente mayor (19 % de los ingresos).

Las 142 detenciones por sobrepeso revelan una incapacidad sistemática de controlar la carga antes de iniciar la marcha, drenando 2.556 horas-camión del sistema anualmente, contraviniendo los límites de peso por eje establecidos en el Decreto Supremo N.° 158 (Ministerio de Obras Públicas [MOP], 1980). La negligencia de control documental se evidencia en infracciones críticas como la ocurrida en abril con sustancias peligrosas, reguladas bajo el D.S. N.° 298 (Ministerio de Transportes y Telecomunicaciones [MTT], 1995), sumándose a los 4 siniestros con lesiones documentados. Estos pasivos operativos y de seguridad colisionan de frente con las exigencias ineludibles para la renovación de 2029: un entorno donde la empresa no solo deberá erradicar las ineficiencias de peso y documentación, sino auditar con total transparencia parámetros como el CO2e bajo estándares internacionales (Global Logistics Emissions Council [GLEC], 2023) y la posición instantánea de la carga bajo amenaza de cancelación de contrato.

---

## 2.3 Mapeo de Infraestructura Operacional y Nodos Críticos

El análisis territorial de Transportes Curimón S.A. evidencia que la operación no transcurre en un recinto confinado, sino a través de una red logística distribuida en un corredor de 3.000 kilómetros lineales, donde la exposición al riesgo es máxima y el control directo es mínimo. La infraestructura fija y móvil se articula en torno a seis tipologías de nodos críticos, cuyas condiciones de conectividad y propiedad determinan los límites de la gobernanza operacional.

### 2.3.1 Los 5 Terminales Operacionales

La infraestructura principal se concentra en cinco terminales: San Bernardo (Región Metropolitana), Antofagasta, Talca, Los Ángeles y Puerto Montt. El Terminal de San Bernardo funciona como nodo matriz, alojando la torre de programación que opera 24/7, el estanque propio de combustible, el patio principal de maniobras y la sala de equipos. Es, además, el único punto de convergencia donde se puede instalar o intervenir el equipamiento a bordo de la flota. Su conectividad está asegurada por dos enlaces de proveedores distintos. 

En contraste, los cuatro terminales regionales operan como puntos de relevo, descanso y apoyo para el conductor, provistos de un único enlace de proveedor y sin respaldo en tres de ellos. La asimetría de conectividad entre la matriz y las regiones introduce un riesgo de desconexión latente.

### 2.3.2 Los 2 Talleres Propios y la Red Externa

La capacidad de mantenimiento físico se sostiene en dos talleres propios (San Bernardo y Los Ángeles), operados por una dotación de 46 personas en sistema de turnos, encargados del cuidado de los 148 tractocamiones y 210 semirremolques propios. 

Cualquier contingencia mecánica que ocurra fuera del radio de estos dos talleres recae en talleres externos en ruta. Actualmente, las intervenciones de estos proveedores externos carecen de toda integración técnica o de software con la compañía; ocurren al margen de la hoja de vida del equipo, fracturando la trazabilidad de mantenimiento.

### 2.3.3 Paso Fronterizo Los Libertadores

El cruce hacia la provincia de Mendoza concentra un flujo de 1.900 operaciones anuales. Este nodo internacional impone la gestión simultánea de documentación aduanera y migratoria de dos países, y está sujeto a severas disrupciones. Entre los meses de junio y septiembre, los cierres por nieve desencadenan episodios impredecibles que han alcanzado hasta 12 días continuos de clausura, generando un efecto cascada sobre la flota detenida, la carga en tránsito y la programación de jornadas de los conductores.

### 2.3.4 Zonas de Sombra de Conectividad

La ruta de 3.000 kilómetros presenta extensas "zonas de sombra" geográficas, superando en algunos casos los 80 kilómetros continuos sin ninguna cobertura móvil, particularmente en el desierto del norte y en zonas cordilleranas. Durante el tránsito por estas franjas, la operación experimenta ceguera sistémica: se pierde la transmisión en tiempo real de la posición GPS, se interrumpe la capacidad de emitir documentos electrónicos o solicitar apoyos de emergencia, y se difiere obligadamente la entrega de datos telemáticos o de jornada.

### 2.3.5 Puntos de Carga y Descarga de Clientes

El extremo comercial de cada viaje se materializa en aproximadamente 1.400 puntos distintos. Éstas constituyen instalaciones de terceros donde Curimón actúa exclusivamente en calidad de visita. Se imponen allí reglas, sistemas y tiempos de espera dictados por el cliente (registrándose tiempos medios de espera de 3 horas y 10 minutos). La empresa se encuentra normativamente inhabilitada para instalar equipamiento físico o infraestructura en estos recintos, varios de los cuales, además, carecen de cobertura móvil para la confirmación de entrega.

### 2.3.6 La Cabina del Camión

La cabina representa el verdadero puesto de trabajo. Constituye un entorno físico hostil, caracterizado por vibración constante, temperaturas extremas, resplandor solar y alimentación eléctrica fluctuante. La restricción operacional fundamental de este nodo es que el conductor se encuentra impedido de interactuar con cualquier dispositivo mientras el camión está en movimiento, exigiendo que toda captura de información durante la marcha ocurra de manera automática y desatendida.

### 2.3.7 Tabla de Síntesis de Nodos Operacionales

| Nodo Operacional | Función Principal | Condiciones de Conectividad | Criticidad Operacional |
| :--- | :--- | :--- | :--- |
| **Terminal San Bernardo (Matriz)** | Base de torre 24/7, taller principal, estanque de abastecimiento y gestión central. | Alta. Dos enlaces de proveedores distintos, sala de equipos. | Máxima. Único punto de intervención técnica a bordo para la flota. |
| **Terminales Regionales (4)** | Relevo, descanso y estacionamiento en Antofagasta, Talca, Los Ángeles y Pto. Montt. | Baja. Enlace único, sin respaldo en tres de los cuatro recintos. | Media. Puntos de soporte geográfico con fragilidad de transmisión. |
| **Talleres Propios (2)** | Mantenimiento preventivo y correctivo de la flota propia (358 equipos sumados). | Integrados a la red corporativa de San Bernardo y Los Ángeles. | Alta. Sostienen la disponibilidad mecánica de los activos de la empresa. |
| **Talleres Externos en Ruta** | Reparaciones correctivas de emergencia lejos de los terminales propios. | Nula integración tecnológica con el sistema central de Curimón. | Alta. Intervenciones no registradas que degradan el historial mecánico. |
| **Paso Los Libertadores** | Operación internacional binacional (1.900 cruces al año). | Externa. Depende de infraestructura pública y oficial de dos países. | Alta. Alta volatilidad climática con cierres prolongados y bloqueo de flota. |
| **Zonas de Sombra en Ruta** | Tránsito prolongado en áreas desérticas o cordilleranas de la Ruta 5 y anexos. | Nula. Extensión de más de 80 km continuos sin cobertura móvil. | Crítica. Pérdida total de visibilidad, posición GPS y alertas de emergencia. |
| **Puntos de Clientes (~1.400)** | Recepción de carga, espera y entrega con firma de conformidad. | Variable. Infraestructura de terceros; varios sin cobertura celular. | Alta. Imposibilidad de instalar equipos propios; foco de objeción de esperas. |
| **Cabina del Camión** | Centro de trabajo móvil y origen del registro de la jornada. | Fluctuante según ruta. Ambiente físico de vibración y temperaturas extremas. | Crítica. Restricción absoluta de manipulación de sistemas durante el avance. |

---

## 2.4 Caracterización de Actores y Matriz de Tensiones Operacionales

El modelo operacional de Transportes Curimón S.A. se sostiene sobre un delicado equilibrio de intereses, responsabilidades y limitaciones estructurales. A partir del levantamiento (Capítulo 8 de las Bases), el diagnóstico evidencia que las fallas de control no responden primariamente a negligencia, sino a asimetrías de información y herramientas desalineadas con la realidad en terreno. A continuación, se caracterizan los diez actores críticos que determinan la viabilidad de cualquier intervención tecnológica.

### 2.4.1 Fichas de Caracterización de los 10 Actores del Capítulo 8

**1. Ricardo Mansilla Oyarzo — Gerente de Operaciones**
* **Dolor Operacional Principal:** Gestión de 22 despachadores operando a ciegas con 3 plataformas GPS incompatibles, 34 camiones sin cobertura y un 26% de kilómetros en vacío resueltos por teléfono y memoria. Necesita un bloqueo de seguridad automatizado, pero teme una parálisis operacional.
* **Cita Clave:** «Para asignar un viaje tengo que saber cuatro cosas al mismo tiempo: dónde está el camión, si el equipo sirve para esa carga, si el conductor tiene jornada, y si los papeles están al día. De esas cuatro, hoy sé una y media... Prefiero que me bloquee a que me deje pasar.»
* **Dependencias y Necesidades de Información:** Depende de la posición real del vehículo, estado del conductor y disponibilidad de cargas de retorno. 
* **Capacidad de Bloqueo/Habilitación:** Alta. Controla la asignación diaria y puede desestimar sistemas que introduzcan fricción excesiva al despacho.

**2. Yasna Colipán Marín — Conductora de ruta (7 años, ruta norte)**
* **Dolor Operacional Principal:** Obligación de cumplir la jornada en tramos de 60-80 km sin infraestructura segura, registro manual retroactivo que no evidencia esperas de 6+ horas, y tramos ciegos prolongados sin comunicación en el norte.
* **Cita Clave:** «Hay tramos donde a mí se me cumple el tiempo y no hay dónde parar. No hay banquina, no hay servicentro, no hay nada por sesenta kilómetros... Manejando no puedo tocar nada.»
* **Dependencias y Necesidades de Información:** Requiere alertas anticipadas de jornada compatibles con la disponibilidad de paraderos seguros, sin interactuar con pantallas mientras conduce.
* **Capacidad de Bloqueo/Habilitación:** Alta (operacional de facto). Si la interfaz exige manipulación en ruta, será ignorada o generará riesgos de seguridad.

**3. Nolberto Sandoval Pinto — Transportista subcontratado (2 camiones, 9 años)**
* **Dolor Operacional Principal:** Vulneración de la soberanía sobre su activo ($200M+) mediante rastreo continuo incluso cuando trabaja para competidores de Curimón, sumado a una opacidad financiera donde las liquidaciones tardan 9 días en llegar con errores frecuentes.
* **Cita Clave:** «Si me preguntan qué me haría cambiar de opinión: que yo controle qué se comparte y cuándo. Si el aparato registra mis horas y eso me sirve a mí para demostrar que estoy en regla, lo acepto. Si el aparato es para que ellos me vigilen, no.»
* **Dependencias y Necesidades de Información:** Depende de liquidaciones transparentes y visibilidad en tiempo real de sus viajes ejecutados para auditar sus pagos.
* **Capacidad de Bloqueo/Habilitación:** Muy Alta (colectiva). Representa a 148 dueños (60% de la flota). Su resistencia activa puede impedir cualquier despliegue de trazabilidad.

**4. Gabriela Ossandón Prieto — Gerenta de Administración y Finanzas (ingreso Ene-26)**
* **Dolor Operacional Principal:** Ceguera financiera estructural. Descubrió contratos históricos operando con un −14% de margen durante 4 años por culpa del prorrateo por ingresos. Padece un retraso de 40 días en datos de combustible y un 38% de costos gestionados con alto porcentaje de error manual (11%).
* **Cita Clave:** «El problema de fondo es que los datos existen y están todos separados... Cinco fuentes que nunca se juntan.»
* **Dependencias y Necesidades de Información:** Requiere integración automatizada de consumo de combustible, horas-conductor y kilómetros reales para establecer un costeo analítico y liquidaciones precisas a terceros.
* **Capacidad de Bloqueo/Habilitación:** Alta. Autoriza las inversiones tecnológicas y supervisa el límite del 9% de margen.

**5. Hugo Trincado Bahamonde — Jefe de Taller y Mantenimiento**
* **Dolor Operacional Principal:** Mantenimiento fundamentado en "adivinanza informada" por lectura manual de odómetros, y 61 camiones con telemetría de fábrica inactiva. No puede instalar nada que no pase físicamente por un terminal.
* **Cita Clave:** «Sesenta y un camiones traen telemetría de fábrica... nadie ha bajado ese dato... si me dicen que hay que instalar algo en trescientos setenta y cuatro camiones, eso no es un proyecto de un mes: es un proyecto de meses.»
* **Dependencias y Necesidades de Información:** Necesita kilometraje y códigos de falla remotos para transitar de un modelo preventivo a uno predictivo.
* **Capacidad de Bloqueo/Habilitación:** Alta (logística). Determina la viabilidad temporal del despliegue de hardware en la flota.

**6. Denisse Aguayo Lillo — Jefa de Prevención de Riesgos y Seguridad**
* **Dolor Operacional Principal:** Responsabilidad legal sobre 454 conductores (sólo 196 propios) sin herramientas de control. Gestiona 6.000 vigencias en planillas Excel, con cero descargas de tacógrafo y una exposición directa que ya generó accidentes severos por fatiga y descontrol documental.
* **Cita Clave:** «Lo que yo quiero es que el sistema no deje salir un camión que no puede salir. No una alerta, no un correo: que no deje.»
* **Dependencias y Necesidades de Información:** Requiere que el cumplimiento de jornada y vigencias documentales intercepte de forma mandatoria el flujo de despacho.
* **Capacidad de Bloqueo/Habilitación:** Media-Alta. Puede escalar riesgos legales paralizando la operación si no existen garantías de cumplimiento normativo.

**7. Andrea Lecaros Vives — Gerenta de Logística de la exportadora clave (19% de ingresos)**
* **Dolor Operacional Principal:** Riesgo de incumplimiento ante clientes internacionales por opacidad de Curimón. Ha impuesto un ultimátum para la renovación de contrato en 2029: trazabilidad total e integración de procesos.
* **Cita Clave:** «Pedimos cuatro cosas para 2029... acreditación del cumplimiento de la jornada del conductor en cada viaje, incluidos los camiones subcontratados. No es una amenaza, es una exigencia con plazo.»
* **Dependencias y Necesidades de Información:** Trazabilidad de posición en tiempo real, e-Docs, emisiones CO₂e y certificación de jornada legal.
* **Capacidad de Bloqueo/Habilitación:** Extrema (comercial). Condiciona la supervivencia del 19% de los ingresos de la empresa.

**8. Enrique Valdebenito Rioseco — Gerente General (21 años en la empresa)**
* **Dolor Operacional Principal:** La fractura entre responsabilidad corporativa y control operacional real, cristalizada en el accidente de febrero, sumado a las pérdidas financieras ocultas.
* **Cita Clave:** «El sesenta por ciento de mi capacidad no me pertenece... no les puedo dar una orden. Entonces cuando alguien me diga 'instalamos un dispositivo', le voy a preguntar quién le va a pedir permiso a ciento cuarenta y ocho dueños... y qué les vamos a ofrecer a cambio.»
* **Dependencias y Necesidades de Información:** Necesita viabilidad táctica en la propuesta: mecanismos de incentivo a terceros e integración sin disrupción total.
* **Capacidad de Bloqueo/Habilitación:** Máxima. El adjudicador final de la licitación y responsable corporativo.

**9. Patricio Kast Fuentealba — Jefe de Control de Flota**
* **Dolor Operacional Principal:** Equipo de 6 personas forzado a consolidar mapas de 3 proveedores distintos (algunos sin permisos de exportación), 34 camiones fantasmas sin GPS y zonas ciegas interurbanas de más de 80 kilómetros. 
* **Cita Clave:** «El cliente grande quiere ver la posición en tiempo real... eso significa resolver tres proveedores, treinta y cuatro camiones sin equipo, los hoyos de cobertura, y convencer a ciento cuarenta y ocho dueños.»
* **Dependencias y Necesidades de Información:** Estandarización de la capa de captura posicional y resolución de los baches de conectividad satelital/celular.
* **Capacidad de Bloqueo/Habilitación:** Alta (técnica). Diagnosticará si las soluciones propuestas son factibles de integrar a nivel de señal en ruta.

**10. Marcelo Riquelme Ibáñez — Jefe de Tecnologías de Información**
* **Dolor Operacional Principal:** Un ecosistema fragmentado heredado (TMS 2013), con 5 sistemas y papel que jamás convergen. Redigitación constante de documentos, lo cual impide la trazabilidad en tiempo real.
* **Cita Clave:** «Toda esa información existe... pero nunca se junta, y ése es literalmente el proyecto... hay puntos de carga sin cobertura donde el documento electrónico no se puede emitir en el momento.»
* **Dependencias y Necesidades de Información:** Soluciones con arquitectura desacoplada, capaces de operar offline temporalmente e integrarse con el legado transaccional.
* **Capacidad de Bloqueo/Habilitación:** Alta (tecnológica). Evaluará la factibilidad arquitectónica, de integración de datos y la robustez del despliegue.

### 2.4.2 Matriz de Poder vs. Interés y Tabla de Brechas Operacionales

**a) Matriz de Poder / Influencia vs. Nivel de Interés**

```text
                           ALTO INTERÉS                          BAJO INTERÉS
                ┌───────────────────────────────┬──────────────────────────────┐
                │        GESTIONAR DE CERCA     │     MANTENER SATISFECHO      │
     ALTO       │                               │                              │
     PODER      │ • E. Valdebenito (G. General) │                              │
                │ • R. Mansilla (Operaciones)   │                              │
                │ • A. Lecaros (Cliente 19%)    │                              │
                │ • G. Ossandón (Finanzas)      │                              │
                │ • M. Riquelme (TI)            │                              │
                ├───────────────────────────────┼──────────────────────────────┤
                │       MANTENER INFORMADO      │          MONITOREAR          │
     BAJO       │                               │                              │
     PODER      │ • D. Aguayo (Prevención)      │                              │
    FORMAL      │ • H. Trincado (Mantenimiento) │                              │
                │ • P. Kast (Control Flota)     │                              │
                │ • Y. Colipán (Conductores)    │                              │
                │ • N. Sandoval (Subcontratos)* │                              │
                └───────────────────────────────┴──────────────────────────────┘
* Nota: Los 148 dueños subcontratados tienen bajo poder formal, pero alto poder de bloqueo sistémico colectivo.
```

**b) Tabla Consolidada de Caracterización y Brechas Operacionales**

| Actor | Expectativas Principales | Temores Principales | Capacidad de Bloqueo | Necesidades de Información / Brechas |
|:---|:---|:---|:---|:---|
| **E. Valdebenito** | Viabilidad sistémica; retención del cliente clave; control de riesgo legal | Exposición penal por fallas ajenas; parálisis operativa por boicot de transportistas externos | Máxima | Indicadores consolidados de riesgo, costo y cumplimiento en tablero único |
| **R. Mansilla** | Asignación eficiente sin kilómetros vacíos; bloqueo inteligente | Sistemas excesivamente rígidos que impidan despachar; freno total de flota | Alta (operativa) | Visibilidad integrada de posición, equipo, jornada y vigencias en 1 pantalla |
| **Y. Colipán** | Respeto de sus tiempos reales de servicio (incluyendo esperas) | Alertas inoportunas; ser sancionada por fallas del sistema o infraestructura vial | Alta (ejecución) | Dispositivo sin distracción; reconocimiento legal del tiempo de espera |
| **N. Sandoval** | Autonomía sobre su activo; cobro ágil y preciso (sin 9 días de retraso) | Espionaje corporativo cuando opera para terceros; penalizaciones injustas | Muy Alta (colectiva) | Control granular de la privacidad de su GPS; transparencia en liquidaciones |
| **G. Ossandón** | Erradicación de subsidios cruzados; costeo analítico por ruta/cliente | Mantener contratos a −14%; retrasos de 40 días en datos de combustible | Alta (financiera) | Integración automatizada de combustible, GPS y TMS para cierre rápido |
| **H. Trincado** | Mantenimiento preventivo real basado en telemetría de uso | Daños inadvertidos; fallas en ruta no registradas; instalaciones inmanejables | Alta (logística) | Lectura automática de odómetros y CANbus; historial unificado de vida útil |
| **D. Aguayo** | "Tolerancia cero" sistemática automatizada ante vigencias caducadas | Otro siniestro fatal predecible; responsabilidad penal por omisión | Media-Alta | Base de datos relacional de certificaciones conectada al motor de asignación |
| **A. Lecaros** | Cumplimiento estricto para 2029 (CO₂e, trazabilidad, e-Doc) | No poder auditar la cadena; perder certificaciones internacionales | Extrema (comercial) | Reportería de emisiones e historial verificable del 100% de la carga |
| **P. Kast** | Coherencia en la visualización geoespacial de toda la flota | Intermitencias crónicas en ruta norte; gestión de equipos dispares | Alta (técnica) | Protocolo unificado de geolocalización que cubra áreas sin señal celular |
| **M. Riquelme** | Arquitectura integrada sin silos; despliegue realista | Exigencia de soluciones mágicas o instalaciones instantáneas | Alta (tecnológica)| APIs de conexión fluida entre telemetría, contabilidad, TMS y dispositivos offline |

### 2.4.3 Las 5 Tensiones Operacionales Irreconciliables del Modelo Actual

La sistematización de las posturas revela cinco tensiones estructurales. Estas representan incompatibilidades verificables que requieren un mecanismo tecnológico y procedimental de arbitraje, y frente a las cuales el modelo actual no ofrece gobernanza (Supuesto Operacional Gobernado).

**1. Seguridad vs. Continuidad Operacional (Aguayo vs. Mansilla)**
* **Naturaleza del Conflicto:** Prevención de Riesgos exige bloquear la salida de cualquier camión con la mínima inconsistencia documental, basándose en la responsabilidad legal. Operaciones teme que un bloqueo binario detenga despachos por caducidades administrativas menores, paralizando los 96.000 viajes anuales.
* **Diagnóstico Analítico:** Falta un protocolo semántico escalonado. Hoy, la torre depende de negociaciones caso a caso porque las 6.000 vigencias están en 4 hojas de cálculo inasibles y desconectadas de las reglas de negocio del TMS.
* **Impacto Económico:** Frena la capacidad de respuesta (afectando el 9% de margen por despachos perdidos) mientras mantiene la exposición crítica a multas o accidentes fatales.

**2. Visibilidad vs. Soberanía del Activo (Lecaros vs. Sandoval)**
* **Naturaleza del Conflicto:** El cliente estratégico demanda el seguimiento continuo de todos los viajes para el 2029. Sin embargo, el subcontratista advierte que no entregará control permanente de su posición a Curimón. 
* **Diagnóstico Analítico (Ley 21.719):** Según la nueva ley de datos, geolocalizar a un transportista externo fuera del marco de su servicio a Curimón carece de base de licitud. Las plataformas actuales obligan a elegir entre trazabilidad nula o vigilancia permanente, y no poseen lógicas de "acceso consentido y temporalizado" por evento de despacho.
* **Impacto Económico:** Amenaza la renovación del contrato del 19% de ingresos, y simultáneamente arriesga el abandono masivo de la flota externa (60%).

**3. Jornada Legal vs. Geografía Vial (Normativa vs. Colipán)**
* **Naturaleza del Conflicto:** La Dirección del Trabajo exige pausas rígidas. La conductora demuestra que la geografía de la ruta impone tramos prolongados sin bermas o paraderos, forzando un incumplimiento por razones de seguridad personal y vial.
* **Diagnóstico Analítico:** El tacógrafo, incluso si se usara, no comprende el contexto geoespacial. Las alertas de fatiga actuales desconocen la infraestructura física, provocando que la norma y la seguridad in situ colisionen.
* **Impacto Económico:** Riesgo sistémico de accidentes en ruta norte e ineficacia en el control de conducción preventiva.

**4. Visibilidad Financiera vs. Opacidad de Costos (Ossandón vs. Inercia Organizacional)**
* **Naturaleza del Conflicto:** La nueva gerencia financiera busca erradicar contratos a −14% de rentabilidad. Se topa con un ecosistema transaccional donde el costeo de ruta está disgregado (combustible a 40 días, esperas no documentadas, peajes atrasados).
* **Diagnóstico Analítico:** El prorrateo de costos oculta el verdadero consumo de cada ruta y es una barrera para una facturación justa. No hay manera de sustentar renegociaciones sin un repositorio de datos consolidados de uso (combustible/kilómetro).
* **Impacto Económico:** Perpetúa el subsidio de rutas que destruyen valor, drenando el endeble 9% de margen corporativo y aumentando los cobros de sobreestadía rechazados ($241,4 M CLP).

**5. Mantenimiento Técnico vs. Descentralización de Activos (Trincado vs. Realidad Operativa)**
* **Naturaleza del Conflicto:** El taller anhela predecir fallas y descargar telemetría de fábrica. Sin embargo, la física dicta que el 22% de la flota subcontratada apenas visita el terminal una vez al mes, y los propios regresan cada 6 días.
* **Diagnóstico Analítico:** Proyectar intervenciones de hardware sin contemplar la asincronía del paso por taller es inviable. Toda estrategia de despliegue y recolección de datos deberá convivir con latencias y la operación remota desconectada.
* **Impacto Económico:** Desgaste acelerado del capital y mermas por lucro cesante derivado de mantenimientos reactivos en carretera.

**Matriz Consolidada de Tensiones:**

| Tensión Operacional | Actores Involucrados | Riesgo de No Resolución | Exigencia para la Solución Técnica |
|:---|:---|:---|:---|
| 1. Seguridad vs. Continuidad | Prevención / Operaciones | Infracciones o freno de la operación | Motor de reglas de validación en tiempo de despacho |
| 2. Visibilidad vs. Soberanía | Cliente (Lecaros) / Transportistas externos | Pérdida del 19% de ingresos | Geolocalización activada/desactivada por flete |
| 3. Jornada vs. Geografía | Ley laboral / Conductores | Multas y fatiga; rechazo de dispositivos | Alertas geo-conscientes anticipadas a zonas ciegas |
| 4. Rentabilidad vs. Opacidad | Finanzas / TI y Procesos de liquidación | Destrucción del 9% de margen | Unificación de fuentes (TMS, Telemetría, e-Doc) |
| 5. Mantenimiento vs. Dispersión | Taller / Realidad de flota de terceros | Fallas graves; parálisis logística | Captura asíncrona y sobre el aire (OTA) de los CANbus |

---

## 2.5 Las Diez Patologías Sistémicas de Curimón S.A. (Tabla de Síntomas S1 a S10)

El análisis del entorno operativo de Transportes Curimón S.A. evidencia que los síntomas observados no constituyen fallas aisladas, sino la manifestación clínica de diez patologías sistémicas originadas en la fractura entre responsabilidad y control. A continuación, audIT constata la cadena causal de cada patología, desde su origen estructural hasta su impacto cuantificable.

**S1 — Ceguera de Jornada**
La compañía registra cero descargas de tacógrafos digitales y carece por completo de visibilidad sobre los 258 conductores subcontratados al momento de asignar viajes. La causa raíz radica en la inexistencia de un proceso de extracción de datos y en la incapacidad de verificar remotamente la actividad previa de trabajadores externos. Esta condición genera un riesgo crítico de siniestralidad por fatiga, evidenciado en el accidente del kilómetro 312, y constituye un incumplimiento sostenido del Artículo 25 bis del Código del Trabajo.

**S2 — Hemorragia Kilométrica en Vacío**
La operación acumula 10,66 millones de kilómetros anuales recorridos sin carga, cifra equivalente al 26 % del total transitado. Esta redundancia logística se origina en un modelo de asignación dependiente de la memoria humana en la torre de control, sin integración posicional unificada que permita triangular cargas de retorno. El impacto económico recae directamente sobre los costos de combustible, peajes y desgaste del activo sin contraprestación de ingreso, erosionando severamente el margen consolidado del 9 %.

**S3 — Erosión de Ingresos por Sobreestadía**
De los $340 millones CLP facturados anualmente por tiempos de espera, el 71 % ($241,4 millones CLP) resulta objetado por los clientes. Este drenaje financiero es consecuencia directa de la incapacidad operativa de producir una prueba irrefutable sobre los horarios de llegada y salida en las instalaciones de terceros. La dependencia de anotaciones manuales vulnerables se traduce en una pérdida directa e irrecuperable de ingresos por servicios efectivamente prestados.

**S4 — Sobrepeso Recurrente**
Los registros oficiales constatan 142 detenciones por exceso de peso en un año, inmovilizando la flota productiva por un total de 2.556 horas-camión, en contravención a las disposiciones de peso máximo del D.S. N.° 158 (Ministerio de Obras Públicas [MOP], 1980). La patología surge de una deficiencia estructural en los procesos de verificación de tonelaje durante las fases de carga y despacho. Cada episodio materializa multas formales, detención del activo, pérdida de horas de conducción y un profundo daño reputacional frente a las autoridades viales y el mercado.

**S5 — Subsidios Cruzados Ocultos**
Tres de los ocho contratos principales operan a pérdida, absorbiendo el 31 % de los ingresos y registrando un margen negativo de hasta un -14 % sostenido por cuatro años. El origen del defecto es la aplicación de un prorrateo de costos por ingreso y un rezago de cuarenta días en la lectura del consumo de combustible. Esta ceguera contable enmascara la verdadera rentabilidad, provocando que las rutas eficientes financien una destrucción continua de valor.

**S6 — Desgobierno de Vigencias**
La fiscalización de abril, que sancionó el transporte de sustancias peligrosas con un certificado vencido hace tres semanas, ilustra la fragilidad del control documental bajo el D.S. N.° 298 (Ministerio de Transportes y Telecomunicaciones [MTT], 1995). Aproximadamente 6.000 fechas críticas de caducidad se administran en cuatro planillas aisladas, sin integridad referencial, alertas automáticas ni pistas de auditoría. El impacto abarca inmovilizaciones vehiculares, riesgo de prohibición para operar faenas de carga peligrosa y exposición penal directa ante accidentes.

**S7 — Hardware Ocioso y Fragmentación Telemática**
La organización posee 61 tractocamiones propios con telemetría CANbus inactiva y 340 unidades distribuidas en tres plataformas incompatibles de posicionamiento satelital. La causa subyacente es la instalación de equipamiento sin el desarrollo de procesos de descarga, y la contratación fragmentada de sistemas no interoperables. Como consecuencia, se pierde información operacional generada por la flota y la torre de control sufre una visibilidad parcial del territorio.

**S8 — Fricción Administrativa en Liquidación**
El ciclo mensual de liquidación a los 148 transportistas consume nueve días hábiles, ocupa a ocho administrativos y resulta en un 11 % de documentos que requieren notas de corrección. Esta ineficiencia surge de un procedimiento estrictamente manual que omite cualquier cruce de verificación automatizada. El efecto se manifiesta en costos de administración inflados, tensiones sostenidas con la red de transportistas subcontratados y un retraso crónico en el cierre financiero.

**S9 — Punto Ciego de Flota Subcontratada**
El 22 % de los vehículos pertenecientes a terceros transita por las instalaciones de Curimón con una frecuencia inferior a una vez por mes. La compañía sustenta su modelo de negocio en esta capacidad externa, pero no dispone de un mecanismo remoto de supervisión técnica. La empresa asume así la responsabilidad integral frente al cliente sobre una fracción de la flota de la cual desconoce el estado mecánico, el cumplimiento documental y la condición de jornada real.

**S10 — Brecha Existencial con Cliente Exportador**
El principal demandante logístico, responsable del 19 % de la facturación, condiciona su renovación contractual de 2029 a la implementación de trazabilidad total, geolocalización, medición de emisiones de CO2e auditables según estándares internacionales (Global Logistics Emissions Council [GLEC], 2023) y documentación electrónica. La brecha operacional actual impide certificar estas obligaciones sobre los viajes despachados. La imposibilidad de cerrar esta distancia supone el riesgo de no renovación, lo que comprometería la viabilidad del negocio al tensionar un margen operacional ya restringido al 9 %.

### Tabla de Síntesis Analítica: Las 10 Patologías de Transportes Curimón S.A.

| N.º | Patología | Síntoma Observable | Causa Raíz Identificada | Impacto Económico / Legal / Operacional | Trazabilidad al Caso |
|:---|:---|:---|:---|:---|:---|
| **S1** | Ceguera de Jornada | 0 descargas de tacógrafo; 258 conductores externos sin control. | Ausencia de proceso de descarga y de verificación previa al despacho para externos. | Incumplimiento Art. 25 bis; riesgo de accidente por fatiga (km 312). | Caps. 1, 4.3, 7.1 |
| **S2** | Hemorragia Kilométrica en Vacío | 26 % de kilómetros vacíos (10,66 M km/año). | Asignación basada en memoria humana sin visibilidad de posición ni de cargas de retorno. | Gasto directo en combustible, peajes y desgaste; erosión del margen de 9 %. | Caps. 4.2, 7.2, 8 |
| **S3** | Erosión de Ingresos por Sobreestadía | $241,4 M CLP/año en cobros objetados (71 % de $340 M). | Incapacidad de generar prueba irrefutable de llegada/salida en instalaciones del cliente. | Pérdida directa de facturación por servicios prestados. | Caps. 4.7, 7.2 |
| **S4** | Sobrepeso Recurrente | 142 detenciones; 2.556 h-camión inmovilizadas. | Falla estructural en verificación de peso durante carga y despacho. | Multas, inmovilización del activo, pérdida de productividad y daño reputacional. | Caps. 4.5, 7.1 |
| **S5** | Subsidios Cruzados Ocultos | 3 contratos a pérdida (peor al -14 % por 4 años); 31 % del ingreso. | Costeo prorrateado que enmascara subsidios cruzados; desfase de 40 días en combustible. | Destrucción sostenida de valor al interior de la compañía. | Caps. 1, 4.1, 7.3 |
| **S6** | Desgobierno de Vigencias | ~6.000 vencimientos en 4 Excel; infracción hazmat (curso vencido 3 semanas). | Datos dispersos sin alertas, integridad referencial ni pista de auditoría. | Infracciones, riesgo de prohibición de operar rutas peligrosas, exposición penal. | Caps. 1, 4.4, 7.1 |
| **S7** | Hardware Ocioso y Fragmentación Telemática | 61 CANbus inactivos; 340 GPS fragmentados en 3 plataformas. | Hardware instalado sin proceso de descarga; sistemas no interoperables. | Pérdida de analítica generada; ceguera parcial en la torre de despacho. | Caps. 4.10, 5, 7.4 |
| **S8** | Fricción Administrativa en Liquidación | Ciclo de 9 días con 8 administrativos; 11 % de correcciones. | Procedimiento intensivo manual sin verificación cruzada automatizada. | Sobrecosto administrativo, demora en cierre contable y tensión con 148 transportistas. | Caps. 4.11, 7.3 |
| **S9** | Punto Ciego de Flota Subcontratada | 22 % de los camiones de terceros pasa < 1 vez/mes por terminal. | Modelo de subcontratación sin mecanismo de verificación remota. | Operación a ciegas sobre el estado mecánico, documental y laboral. | Caps. 2.3, 6, 7.4 |
| **S10** | Brecha Existencial con Cliente Exportador | Exigencias 2029 (CO2e, e-Docs, trazabilidad) no cumplidas. | Brecha absoluta entre capacidades vigentes de registro y exigencias futuras. | Riesgo de pérdida del 19 % de ingresos; amenaza a la viabilidad del negocio (9 % margen). | Caps. 1, 4.6, 7.2 |

---

## 2.6 Registro de Supuestos Operacionales y Mapeo Exhaustivo del Numeral 16.1

### 2.6.1 Principios de Modelamiento y Delimitación del Diagnóstico

El análisis del Numeral 16.1 de las Bases Técnicas del Caso (FEP03.10.26) evidencia la existencia de 26 decisiones operacionales y estratégicas deliberadamente omitidas por Transportes Curimón S.A. Para preservar el rigor metodológico del diagnóstico sin incurrir en la prefiguración prematura de soluciones, audIT ha procedido a transformar cada uno de estos vacíos normativos en un «Supuesto Operacional Gobernado». Esta técnica garantiza plena transparencia algorítmica y funcional: los supuestos operan exclusivamente como un marco limitante para dimensionar el nivel de madurez, el grado de fricción logística y el riesgo latente del modelo actual, pero no constituyen arquitecturas de solución. El trazado de estos 26 supuestos se encuentra formalmente anclado a las interrogantes levantadas en el pliego oficial de *Consultas Consolidadas* del proponente audIT.

### 2.6.2 Matriz Maestra de los 26 Supuestos del Numeral 16.1

| N.° Decisión | Área / Dominio | Dilema No Resuelto por Curimón (Numeral 16.1) | Supuesto Técnico/Operacional Asumido por audIT para el Diagnóstico | Impacto en Riesgo / Viabilidad |
| :--- | :--- | :--- | :--- | :--- |
| **1** | Laboral y Normativo | Cómo obtener/acreditar la jornada de conductores externos de 148 contratistas que pueden haber conducido para otros clientes. | Ante el silencio de las bases en la Decisión N.° 1, audIT asume como supuesto técnico que el mecanismo de acreditación requerirá evidencia con valor probatorio ante la autoridad laboral, descartando la mera declaración verbal (Véase Consulta N.° 8 del pliego oficial de audIT). | Riesgo legal alto; exposición por responsabilidad subsidiaria y fatiga no controlada. |
| **2** | Gestión de Terceros | Qué ofrecer a los 148 transportistas subcontratados a cambio de compartir datos, y penalizaciones para no adherentes. | Ante el silencio de las bases en la Decisión N.° 2, audIT asume como supuesto técnico que la integración dependerá de un marco de incentivos y anexos contractuales exigibles, condicionando la viabilidad del ruteo a la transparencia del tercero. | Riesgo de adopción crítico; amenaza de merma en la disponibilidad de la flota en un 60,4%. |
| **3** | Deuda Técnica | Qué hacer con el TMS de 2013: reemplazar, mantener/integrar o encapsular mediante sustitución progresiva. | Ante el silencio de las bases en la Decisión N.° 3, audIT asume como supuesto técnico que el TMS de 2013 constituye deuda técnica activa cuyo ciclo de vida ha concluido, limitando las capacidades operativas actuales de forma estructural (Véase Consulta N.° 13). | Impacto alto; obsolescencia basal que impide la optimización algorítmica del flete. |
| **4** | Visibilidad Geoespacial | Cómo unificar la posición de la flota operando con 3 proveedores, acceso limitado (solo lectura) en 2 de ellos y 34 camiones sin GPS. | Ante el silencio de las bases en la Decisión N.° 4, audIT asume como supuesto técnico que la actual fragmentación de señales conforma un entorno de control asimétrico, tratando los 34 camiones sin cobertura como una zona ciega de alto riesgo patrimonial. | Riesgo operativo y de seguridad; imposibilidad de garantizar niveles de servicio (SLA). |
| **5** | Activos Físicos (IoT) | Propiedad del dispositivo a bordo en camiones de terceros: quién costea, administra y qué sucede si el contratista abandona la flota. | Ante el silencio de las bases en la Decisión N.° 5, audIT asume como supuesto técnico que la propiedad y gestión de inventario del hardware recaerá en Curimón, implicando costos hundidos y fricción de recuperación de activos. | Riesgo financiero medio; complejidad en la logística inversa del hardware. |
| **6** | Continuidad Operativa | Qué ocurre cuando la verificación de requisitos bloquea un viaje ya comprometido: quién autoriza y mediante qué registro. | Ante el silencio de las bases en la Decisión N.° 6, audIT asume como supuesto técnico que el bloqueo absoluto genera parálisis, por lo que el diagnóstico asume la necesidad de flujos de excepción (override) auditables y jerarquizados (Véase Consulta N.° 16). | Riesgo de paralización crítico; impacto directo en los tiempos de respuesta y compromisos comerciales. |
| **7** | Fatiga y Ruteo | Con cuánta antelación alertar el agotamiento de jornada, considerando tramos de ruta sin lugares seguros de detención. | Ante el silencio de las bases en la Decisión N.° 7, audIT asume como supuesto técnico que el cálculo de la alerta es dinámico espacialmente e indexado a una cartografía validada de paraderos seguros, no un simple contador regresivo (Véase Consulta N.° 20). | Riesgo de seguridad vital y multas normativas por conducción extendida forzosa. |
| **8** | Control de Tiempos | Cómo registrar llegadas/salidas en puntos de terceros sin intervención manual del conductor ni instalación de equipos locales. | Ante el silencio de las bases en la Decisión N.° 8, audIT asume como supuesto técnico que la certificación de estadías dependerá exclusivamente del cruce entre telemetría móvil y geocercas satelitales parametrizadas (Véase Consulta N.° 10). | Riesgo financiero medio; alta tasa de sobreestadías no facturables por ausencia de prueba. |
| **9** | Integración Tributaria | Cómo emitir el e-Doc en puntos de carga sin cobertura móvil (sombra de red), considerando que su emisión es un requisito previo al rodaje. | Ante el silencio de las bases en la Decisión N.° 9, audIT asume como supuesto técnico que la operación en sombra exige pre-foliado local y autorización de contingencia SII para evitar la inmovilización de la carga (Véase Consulta N.° 15). | Riesgo normativo y operativo; detención de faena por latencia de infraestructura de telecomunicaciones. |
| **10** | Trazabilidad Comercial | Cómo obtener la confirmación de entrega (PoD) del destinatario y en qué momento se habilita para facturación o defensa de cobros. | Ante el silencio de las bases en la Decisión N.° 10, audIT asume como supuesto técnico que el PoD es un evento asíncrono, cuya latencia actual entre el plano físico (firma) y el lógico retrasa el reconocimiento de ingresos. | Impacto alto en el flujo de caja; aumento del ciclo de conversión de efectivo. |
| **11** | Transmisión de Datos | Qué frecuencia de muestreo utilizar para posición y telemetría, balanceando qué se transmite en línea versus qué se almacena a bordo. | Ante el silencio de las bases en la Decisión N.° 11, audIT asume como supuesto técnico que la saturación de red exige discriminación entre paquetes críticos en tiempo real y tramas de alta resolución cacheadas localmente. | Impacto en viabilidad técnica; saturación de planes de datos M2M y sobrecostos por tráfico. |
| **12** | Telemetría de Fábrica | Qué hacer con la telemetría FMS/CANbus instalada de fábrica en 61 tractocamiones, la cual no está siendo procesada actualmente. | Ante el silencio de las bases en la Decisión N.° 12, audIT asume como supuesto técnico que la explotación de estos datos requerirá integración homologada para no vulnerar la garantía activa del tren motriz por parte del concesionario (Véase Consulta N.° 14). | Impacto medio; oportunidad perdida de optimización de combustible y mantenimiento predictivo. |
| **13** | Custodia de Evidencia | Quién descarga la data del tacógrafo, con qué periodicidad, dónde se custodia y con qué garantías de integridad técnica. | Ante el silencio de las bases en la Decisión N.° 13, audIT asume como supuesto técnico que la custodia manual actual representa una vulnerabilidad forense, asumiendo la necesidad de una extracción automatizada, centralizada y criptográficamente segura. | Riesgo legal alto; potencial pérdida o repudio de evidencia ante accidentes graves. |
| **14** | Eficiencia de Flota | Cómo y con qué algoritmo asignar el viaje de retorno a un camión que previsiblemente quedará vacío (26% de kilómetros en vacío). | Ante el silencio de las bases en la Decisión N.° 14, audIT asume como supuesto técnico que dicho porcentaje es una merma estructural derivada de la incapacidad algorítmica de triangular disponibilidad geoespacial con el *backhaul* oportuno. | Impacto financiero grave; erosión severa de los márgenes de utilidad neta de la operación. |
| **15** | Contabilidad Analítica | Cómo reconstruir el costo por viaje recibiendo insumos asíncronos (combustible a 40 días, TAG mensual, llantas por planilla). | Ante el silencio de las bases en la Decisión N.° 15, audIT asume como supuesto técnico que la métrica de costo se diagnostica mediante aproximaciones incrementales, donde el costo inicial es parcial y versionable en el tiempo (Véase Consulta N.° 18). | Impacto financiero alto; fijación de precios y rentabilidad calculadas sobre bases distorsionadas. |
| **16** | Costeo de Terceros | Cómo estimar el costo real operativo de un camión subcontratado cuando Curimón solo visibiliza la tarifa plana de flete pagada. | Ante el silencio de las bases en la Decisión N.° 16, audIT asume como supuesto técnico que la opacidad del contratista obliga a utilizar la tarifa pagada como un factor sustituto del costo directo, ocultando las deficiencias propias de los terceros. | Riesgo de gestión estratégico; imposibilidad de optimizar la red de subcontratistas bajo modelos *open-book*. |
| **17** | Evaluación de Contratos | Qué acciones correctivas tomar ante los 3 contratos operativos bajo el costo y qué data levantar para su renegociación en 2027. | Ante el silencio de las bases en la Decisión N.° 17, audIT asume como supuesto técnico que cualquier renegociación requerirá granularidad probatoria del costo por cliente/eje operativo, inexistente bajo el paradigma actual del TMS de 2013. | Impacto financiero crítico; subsidio cruzado prolongado que destruye valor corporativo. |
| **18** | Gestión Documental | Cómo fiscalizar ~6.000 fechas de expiración y a quién responsabilizar cuando el titular del documento es una empresa externa. | Ante el silencio de las bases en la Decisión N.° 18, audIT asume como supuesto técnico que la responsabilidad recae de forma solidaria sobre Curimón en ruta, lo que expone a la empresa a fallos de auditoría por dependencia manual (Véase Consulta N.° 21). | Riesgo operativo alto; multas, retenciones y suspensiones por caducidades no detectadas a tiempo. |
| **19** | Cargas Peligrosas | Cómo verificar que los documentos de sustancias peligrosas (SUSPEL) a bordo coincidan con la carga real física, no con la teórica. | Ante el silencio de las bases en la Decisión N.° 19, audIT asume como supuesto técnico que la desconexión entre la orden de transporte y la lectura de báscula en origen representa una brecha de seguridad grave bajo el D.S. N.° 298. | Riesgo legal severo y de daño ambiental; contingencias penales por discrepancia de manifiestos. |
| **20** | Gestión de Contingencias| Cómo responde el modelo si el Paso Los Libertadores cierra 12 días con camiones inmovilizados, carga sellada y conductores perdiendo jornada. | Ante el silencio de las bases en la Decisión N.° 20, audIT asume como supuesto técnico que la disrupción fronteriza actúa como factor exógeno incontrolable, evidenciando carencia de protocolos de hibernación segura de fletes y pausas de jornada. | Impacto logístico y laboral extremo; sobrecostos masivos no traspasables a clientes. |
| **21** | Hoja de Vida del Activo | Cómo integrar intervenciones mecánicas realizadas por talleres de terceros dentro de la bitácora unificada de mantenimiento. | Ante el silencio de las bases en la Decisión N.° 21, audIT asume como supuesto técnico que la fragmentación de la historia clínica del vehículo corrompe la fiabilidad del mantenimiento predictivo, operando actualmente a ciegas. | Impacto operativo; falla catastrófica de activos por mantenciones externalizadas no consolidadas. |
| **22** | Sostenibilidad (GHG) | Cómo reportar las emisiones de CO2 equivalente por tonelada-kilómetro en camiones de terceros donde no existe medición directa. | Ante el silencio de las bases en la Decisión N.° 22, audIT asume como supuesto técnico que el cálculo para la flota externa requerirá la aplicación de estándares internacionales paramétricos de interpolación conforme al GLEC Framework (Global Logistics Emissions Council [GLEC], 2023), dada la imposibilidad de ingesta telemática pura (Véase Consulta N.° 12). | Riesgo comercial estratégico; posible pérdida del 19% de ingresos por no cumplimiento ante exportadores. |
| **23** | Privacidad de Datos | Qué proporciones de ruta e historial se comparten con el cliente final y cómo conciliarlo con la autorización de cada dueño de camión. | Ante el silencio de las bases en la Decisión N.° 23, audIT asume como supuesto técnico que la transmisión de coordenadas está rígidamente confinada al ciclo activo del flete, limitando la visibilidad para preservar la observancia de la Ley N.° 21.719 (Ministerio Secretaría General de la Presidencia, 2024; Véase Consulta N.° 9). | Riesgo normativo; contingencias por uso indebido de posicionamiento en flotas no propias. |
| **24** | Seguridad de la Prueba | Cómo proteger la evidencia horaria frente a acusaciones de manipulación de registros de jornada por parte de los conductores o el contratista. | Ante el silencio de las bases en la Decisión N.° 24, audIT asume como supuesto técnico que la actual carencia de un sello criptográfico de tiempo y origen deja a Curimón expuesta a repudio de logs en tribunales laborales, requiriendo principios de confianza cero (National Institute of Standards and Technology [NIST], 2020) y controles de seguridad de la información (International Organization for Standardization [ISO], 2022). | Riesgo probatorio alto; juicios desfavorables e imposibilidad de certificar el apego a la norma. |
| **25** | Logística de Implantación| Cómo desplegar equipos a bordo en 374 máquinas que pasan por terminal cada 6 días, o los contratistas que van menos de 1 vez al mes (22%). | Ante el silencio de las bases en la Decisión N.° 25, audIT asume como supuesto técnico que el ciclo de penetración tecnológica estará indexado al patrón errático de visitas, impidiendo un despliegue masivo y simultáneo de infraestructura física (Véase Consulta N.° 19). | Riesgo de proyecto alto; dilatación severa de las fases de enrolamiento y puesta en marcha. |
| **26** | Transición Operativa | Cómo subsiste la trazabilidad de Curimón durante la fase de transición, donde convivirán camiones equipados y unidades rezagadas. | Ante el silencio de las bases en la Decisión N.° 26, audIT asume como supuesto técnico que el modelo operativo enfrentará una fricción crítica al tener que soportar procesos paralelos (modo mixto telemático/documental manual) de manera sostenida (Véase Consulta N.° 19). | Riesgo organizativo; duplicación de esfuerzos de control en las torres de tráfico durante el periodo de *ramp-up*. |

### 2.6.3 Límite Explícito del Diagnóstico (Frontera formal con Subdoc 3)

> [!WARNING]
> **DELIMITACIÓN RIGUROSA DEL PRESENTE DOCUMENTO**
> AudIT constata que la formulación de los Supuestos Operacionales Gobernados en el presente subdocumento **tiene un carácter estricta y exclusivamente diagnóstico**. Su propósito es modelar el impacto de los vacíos de información en la viabilidad técnica y operativa de Transportes Curimón S.A., delimitando el problema central. **Ninguna de las descripciones precedentes constituye una propuesta tecnológica, selección de arquitectura o definición de producto**. El diseño detallado de la solución que mitigará las deficiencias expuestas corresponde, por estructura, a las dimensiones arquitectónicas tratadas a partir del **Subdocumento 3** en adelante.

---

## 2.7 Referencias Normativas y de la Industria (Norma APA 7.ª Edición)

Global Logistics Emissions Council. (2023). *GLEC framework for logistics emissions methodologies* (v3.0) / ISO 14083:2023. Smart Freight Centre.

International Organization for Standardization. (2022). *ISO/IEC 27001:2022 Information security, cybersecurity and privacy protection — Information security management systems — Requirements*.

Ministerio de Obras Públicas. (1980). *Decreto Supremo N.° 158: Fija peso máximo de los vehículos que pueden circular por caminos públicos*. Biblioteca del Congreso Nacional de Chile.

Ministerio de Transportes y Telecomunicaciones. (1995). *Decreto Supremo N.° 298: Reglamenta transporte de cargas peligrosas por calles y caminos*. Biblioteca del Congreso Nacional de Chile.

Ministerio del Trabajo y Previsión Social. (2001). *Código del Trabajo de Chile* (Artículo 25 bis). Biblioteca del Congreso Nacional de Chile.

Ministerio Secretaría General de la Presidencia. (2024). *Ley N.° 21.719: Cumplimiento de obligaciones en materia de protección de datos personales*. Biblioteca del Congreso Nacional de Chile.

National Institute of Standards and Technology. (2020). *Zero trust architecture* (NIST Special Publication 800-207). U.S. Department of Commerce. https://doi.org/10.6028/NIST.SP.800-207

Transportes Curimón S.A. (2026). *Pliego de Licitación TFEP-01/2026: Bases Administrativas FEP01.26, Bases Técnicas Transversales FEP02.26 y Bases Técnicas del Caso FEP03.10.26*.

---

*Fin del Subdocumento 2 — Comprensión del Problema y de la Necesidad*  
*Dupla 1 (D1) — Licitación N.º TFEP-01/2026*  
*Caso 10: Transportes Curimón S.A. · Proponente: audIT*
