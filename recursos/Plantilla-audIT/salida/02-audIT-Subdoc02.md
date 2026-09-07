# Comprensión del Problema y de la Necesidad

**Subdocumento N.º 2**

| | |
|---|---|
| Empresa | audIT, Empresa N.º 10 |
| Licitación | Licitación Pública Internacional N.º TFEP-01/2026. Caso 10 Transporte de Carga |
| Proyecto | Plataforma Digital de Misión Crítica para Transporte de Carga |
| Cliente | Transportes Curimón S.A. |
| Instancia | Informe Preparatorio 1. Oferta Técnica Sobre N.º 2 |
| Contenido | Dimensionamiento del problema, contexto de la industria, actores afectados y supuestos declarados. |
| Versión | 1.0 |
| Fecha | 7 de septiembre de 2026 |
| Lugar | Viña del Mar, Chile |

---

## Comprensión del problema


### Síntesis ejecutiva de la situación actual y dimensión del desafío


El diagnóstico estructural de Transportes Curimón S.A. revela una fractura fundamental que compromete la viabilidad operacional y financiera de la compañía: la asimetría insostenible entre la responsabilidad legal, comercial y regulatoria que la empresa asume frente a sus mandantes, y el control efectivo que ejerce sobre los recursos que ejecutan el servicio. La compañía soporta el cien por ciento de la responsabilidad sobre cargas, siniestros y fiscalizaciones, pero opera en un escenario donde el 60,4 % de su capacidad de transporte (226 camiones subcontratados de un total de 374) y el 56,8 % de sus operadores (258 conductores externos frente a 196 propios) no se encuentran bajo su tuición directa. Esta disociación genera un vacío de gobernanza sobre operaciones críticas ejecutadas a nombre de Curimón, conformando un riesgo latente de magnitudes incalculables bajo el régimen de responsabilidad de la (Ministerio del Trabajo, 2006) y la (Ministerio de Transportes y Telecomunicaciones, 2009).

La dimensión física del desafío amplifica esta fractura. La red logística moviliza 96.000 viajes anuales, totalizando 41 millones de kilómetros recorridos y 2,4 millones de toneladas transportadas por una flota de 374 tractocamiones a lo largo de un corredor de 3.000 kilómetros entre Antofagasta y Puerto Montt, complementado por $\approx 1.900$ cruces internacionales por el paso Los Libertadores. Este despliegue territorial extenso se administra con un nivel de fragilidad financiera agudo: la facturación anual alcanza los \$78.000 millones CLP, pero exhibe un margen operacional consolidado de apenas el 9 % (\$7.020 millones CLP). El análisis pormenorizado del costeo expone un deterioro estructural grave: tres de los ocho contratos principales operan por debajo de la línea de costo, representando en conjunto el 31 % del ingreso total de la empresa (\$24.180 millones CLP). El caso más crítico documenta un contrato ejecutado con un margen negativo del 14 % durante cuatro años consecutivos, subsidiado sistemáticamente por rutas rentables bajo un modelo ciego de prorrateo por ingreso.

La estructura de costos revela que el 38 % del gasto se destina a pagos a transportistas subcontratados (\$29.640 millones CLP), el 14 % a combustible de flota propia (\$10.920 millones CLP) ---afectado por una dispersión de rendimiento del 19 % entre camiones idénticos y un rezago de información de 40 días--- y el 12 % a remuneraciones de conductores propios (\$9.360 millones CLP). Asimismo, existe una extrema concentración comercial: de una cartera de 84 clientes activos, sólo 8 contratos generan el 71 % de la facturación total (\$55.380 millones CLP), situando a la empresa en una posición de vulnerabilidad crítica ante cualquier fricción de servicio.

La materialización de este desacople estructural se concentró en tres eventos críticos durante el primer semestre de 2026. El 14 de febrero (04:40 h), el accidente en el kilómetro 312 de la Ruta 5 Sur demostró la ceguera patronal de la compañía respecto a los tiempos de conducción y descanso previos de los choferes subcontratados, provocando la suspensión de contratos por seis semanas. En abril, una fiscalización inmovilizó durante 14 horas un tractocamión con sustancias peligrosas debido a un curso obligatorio vencido tres semanas antes, evidenciando el colapso del control documental bajo el (Ministerio de Transportes, 1995). Finalmente, en junio, el primer costeo analítico por ruta destapó la existencia de subsidios cruzados masivos. Estos eventos no constituyen fallas aisladas, sino manifestaciones directas de un ecosistema de datos desintegrado.

Este colapso de la gobernanza de datos se cuantifica en la gestión manual de aproximadamente 6.000 fechas de vencimiento vivas, distribuidas en cuatro planillas de cálculo aisladas que carecen de integridad referencial y alertas automáticas. A nivel de hardware instalado, se constata una omisión total en la extracción de evidencia: cero descargas históricas de tacógrafos digitales y 61 tractocamiones propios operando con telemetría CANbus de fábrica inactiva. En el plano de visibilidad, 34 camiones de terceros circulan sin ningún dispositivo GPS (monitoreados por llamada telefónica), mientras que los 340 restantes se monitorean a través de tres plataformas incompatibles que impiden conformar una vista operacional unificada.

Frente a esta vulnerabilidad sistémica, la compañía enfrenta una amenaza existencial hacia el año 2029: el cliente exportador mayor, responsable del 19 % de los ingresos (\$14.820 millones CLP), ha condicionado la renovación de su contrato al cumplimiento de cuatro requisitos intransigibles. Estas exigencias imponen la necesidad de acreditar fehacientemente el cumplimiento de la jornada en cada viaje ---incluyendo transportistas y choferes subcontratados bajo el (Ministerio del Trabajo, 2003)---, contar con el cien por ciento de trazabilidad y posicionamiento de carga en tiempo real, digitalización integral de la documentación sin redigitación (e-Docs para $\approx 128.000$ documentos anuales) y la emisión de reportes auditados de emisiones de gases de efecto invernadero (CO$_2$e) por tonelada-kilómetro bajo estándares internacionales (Smart Freight Centre, 2023). Esta matriz de condiciones demanda una transformación absoluta de los estándares probatorios de Transportes Curimón S.A., cerrando el margen para operaciones basadas en la invisibilidad de los activos de terceros.


### Desglose cuantitativo y diagnóstico de los siete bloques de datos duros


#### Bloque 1: Flota y asimetría de tenencia


**Tabla. Bloque 1: Flota y asimetría de tenencia**

| **Indicador** | **Valor** |
|---|---|
| Capacidad total gestionada | 374 tractocamiones |
| Flota propia | 148 tractocamiones (39,6 %; antigüedad promedio 6,4 años) |
| Flota subcontratada | 226 tractocamiones (60,4 %) |
| Semirremolques propios | 210 equipos (ramplas planas, tolvas, furgones secos y portacontenedores) |
| Flota especializada en sustancias peligrosas (SUSPEL) | 18 tractocamiones habilitados bajo (Ministerio de Transportes, 1995) |
| Semirremolques refrigerados propios | 44 equipos (12 % de la capacidad; operación crítica diciembre-abril) |
| Proveedores subcontratados | 148 dueños independientes (microempresas de 1 a 4 camiones) |


El 60,4 % de la capacidad tractora principal no pertenece a la compañía, fragmentada entre 148 propietarios independientes que toman decisiones autónomas sobre el mantenimiento y disponibilidad de sus activos, limitando cualquier imposición jerárquica.

El análisis de la estructura de la flota evidencia una dependencia crítica hacia terceros que desequilibra la arquitectura de control. Curimón provee la interfaz comercial, los semirremolques propios (incluyendo 44 unidades refrigeradas de alta exigencia estacional) y absorbe la responsabilidad del servicio, pero el activo motriz fundamental está bajo el mando de terceros. Esta asimetría de tenencia bloquea cualquier esfuerzo de estandarización tecnológica forzada y determina que las capacidades de trazabilidad o integración no pueden depender de imposiciones jerárquicas, configurando el principal obstáculo para asegurar la fiabilidad operacional.


#### Bloque 2: Fuerza conductora y brecha de jornada


**Tabla. Bloque 2: Fuerza conductora y brecha de jornada**

| **Indicador** | **Valor** |
|---|---|
| Dotación total de conductores programados | 454 operadores |
| Conductores propios | 196 (43,2 %; bajo Art. 25 bis Código del Trabajo) |
| Conductores subcontratados (externos) | 258 (56,8 %; sin relación contractual directa con Curimón) |
| Descargas históricas de tacógrafo digital | 0 registros descargados |
| Incidente de referencia (km 312) | Chofer externo con fatiga tras conducir para otro mandante sin descanso |
| Siniestros con lesiones (últimos 3 años) | 4 accidentes documentados |


El ecosistema laboral de la compañía presenta una ceguera probatoria total frente a la normativa de tiempos de conducción y descanso. Con 258 conductores que no mantienen un vínculo laboral con Curimón y cero descargas históricas de tacógrafo, la empresa asigna viajes sin evidencia objetiva de la jornada previa del operador. El accidente del kilómetro 312 subraya la gravedad de esta fisura: el cumplimiento aparente de los registros internos de la empresa no garantiza el descanso real del conductor externo, exponiendo a la compañía a responsabilidades penales, civiles y laborales subsidiarias bajo la (Ministerio del Trabajo, 2006) y la (Ministerio de Transportes y Telecomunicaciones, 2009).


#### Bloque 3: Red, rutas y fricción logística


**Tabla. Bloque 3: Red, rutas y fricción logística**

| **Indicador** | **Valor** |
|---|---|
| Volumetría anual | 96.000 viajes al año |
| Carga anual movilizada | 2.400.000 toneladas |
| Distancia anual recorrida | 41.000.000 de kilómetros |
| Operación en vacío | 26 % (10,66 millones de kilómetros sin carga) |
| Documentos Electrónicos de Transporte (DET) | $\approx 128.000$ emisiones anuales proyectadas |
| Torre de programación | 22 operadores en turnos continuos 24x7x365 |
| Cruces fronterizos anuales (Paso Los Libertadores) | $\approx 1.900$ cruces al año (cierres por nieve de hasta 12 días continuos) |


La coordinación de 41 millones de kilómetros anuales recae sobre una torre de control de 22 operadores que ejecutan la asignación de viajes sin soporte algorítmico, operando desde la memoria y la telefonía. El impacto más severo de este modelo es la generación de 10,66 millones de kilómetros recorridos sin carga, representando un 26 % de ineficiencia estructural directa sobre la capacidad rodante. A esta fricción logística se suma la volatilidad geográfica del paso Los Libertadores, cuyos cierres prolongados quiebran cualquier modelo estático de planificación de recursos, saturando la capacidad de respuesta manual del equipo de programación.


#### Bloque 4: Desgobierno de datos e infraestructura ociosa


**Tabla. Bloque 4: Desgobierno de datos e infraestructura ociosa**

| **Indicador** | **Valor** |
|---|---|
| Fechas de vencimiento vivas (estimado) | $\approx 6.000$ fechas de conductores y vehículos |
| Soporte de control documental | 4 planillas de cálculo (Excel) aisladas sin integridad referencial |
| Telemetría CANbus inactiva | 61 tractocamiones propios de fábrica nunca consultados |
| Camiones sin posicionamiento GPS | 34 tractocamiones de terceros (seguimiento puramente telefónico) |
| Plataformas de rastreo simultáneas incompatibles | 3 plataformas para 340 tractocamiones (una sin exportación) |
| Tramos en sombra celular continua | Superiores a 80 km en desierto norte y pasos cordilleranos |


Se constata un estado de inoperatividad de los datos donde la captura, integración y alerta preventiva han fallado sistemáticamente. La mantención manual de cerca de 6.000 vigencias en hojas de cálculo inconexas garantiza la aparición de incidentes por vencimientos documentales no detectados. Al mismo tiempo, la empresa desperdicia activos tecnológicos de fábrica, como el CANbus de 61 tractocamiones que nunca ha sido consultado. La fragmentación de 340 vehículos en tres plataformas de monitoreo divergentes, sumado a los 34 camiones ciegos y sombras de red celular mayores a 80 km, destruye la posibilidad de conformar una vista operacional única.


#### Bloque 5: Fricción comercial y tiempos de espera


**Tabla. Bloque 5: Fricción comercial y tiempos de espera**

| **Indicador** | **Valor** |
|---|---|
| Tiempo medio de espera en puntos de carga | 3 horas 10 minutos (supera las 8 horas en faenas agrícolas) |
| Puntos de carga y descarga de clientes | $\approx 1.400$ instalaciones ajenas |
| Cobros facturados por sobreestadía | \$340.000.000 anuales |
| Cobros objetados / no recaudados por falta de prueba | 71 % (\$241.400.000 anuales en pérdidas directas) |
| Documentos de entrega (POD / Guías) defectuosos o extraviados | 4,2 % con firmas ilegibles, tachaduras o pérdidas físicas |
| Proceso de liquidación mensual a terceros | 9 días hábiles de duración, 8 analistas involucrados |
| Tasa de refacturación / corrección en liquidaciones | 11 % de documentos corregidos tras reclamos de terceros |


La ausencia de registros de posicionamiento georreferenciado e inalterable genera una profunda merma financiera mediante la objeción del 71 % de los montos facturados por demoras en las instalaciones de clientes, representando \$241,4 millones no recaudados. El soporte de papel, manipulable y de entrega diferida, fracasa como instrumento probatorio, agravado por un 4,2 % de comprobantes de entrega (POD) extraviados o ilegibles. Adicionalmente, el procesamiento de las liquidaciones de 148 dueños subcontratados exige 9 días de trabajo de 8 personas, resultando en un 11 % de notas de corrección post-emisión; un indicador de fricción que deteriora la confianza de los proveedores externos que sostienen la mayoría de la operación.


#### Bloque 6: Estructura financiera y distorsión de costos


**Tabla. Bloque 6: Estructura financiera y distorsión de costos**

| **Indicador** | **Valor** |
|---|---|
| Facturación bruta anual consolidada | \$78.000.000.000 CLP (\$78.000M) |
| Margen operacional consolidado | 9 % (\$7.020.000.000 CLP anuales) |
| Contratos principales bajo la línea de costo | 3 de 8 contratos analizados |
| Participación de los 3 contratos bajo costo | 31 % del ingreso total (\$24.180.000.000 CLP) |
| Caso crítico de rentabilidad negativa | -14 % de margen durante 4 años consecutivos (desde 2021) |
| Estructura de costos operacionales | Fletes terceros (38 %), Combustible (14 %), Conductores propios (12 %) |
| Combustible sobre ingreso y rezago contable | 14 % del ingreso (\$10.920M CLP); hasta 40 días de desfase probatorio |
| Dispersión de rendimiento de combustible no justificada | 19 % de variación entre camiones idénticos en idéntica ruta |
| Concentración comercial de clientes | 84 clientes activos; 8 clientes concentran el 71 % de la facturación |


La rentabilidad del 9 % encubre un modelo de gestión basado en prorrateos generales que impiden el costeo analítico a nivel de ruta y viaje. El descubrimiento de que el 31 % de los ingresos de la empresa proviene de tres contratos deficitarios ---uno de ellos drenando un margen del -14 % durante cuatro años ininterrumpidos--- es el resultado de operar a ciegas respecto de los costos reales de ejecución. El rubro de combustible, responsable del 14 % del gasto (\$10.920 millones CLP), opera bajo un esquema de facturación consolidada mensual que retrasa en 40 días la visualización del consumo, ocultando una dispersión injustificada del 19 % de rendimiento energético entre vehículos similares en la misma ruta.


#### Bloque 7: Seguridad y riesgo existencial


**Tabla. Bloque 7: Seguridad y riesgo existencial**

| **Indicador** | **Valor** |
|---|---|
| Detenciones en ruta por exceso de peso (año 2025) | 142 eventos en plazas de pesaje oficiales |
| Horas de inmovilización por sobrepeso | 2.556 horas-camión perdidas (18 horas promedio por detención) |
| Marco normativo de pesos y dimensiones | (Ministerio de Obras Públicas, 1980) |
| Infracción Hazmat (abril 2026) | Curso vencido hace 3 semanas; 14 horas de inmovilización ((Ministerio de Transportes, 1995)) |
| Siniestros con lesiones (últimos 3 años) | 4 accidentes (incluyendo vuelco en km 312 por fatiga) |
| Exigencias condicionantes del cliente principal (2029) | Trazabilidad 100 %, posición tiempo real, e-Docs, CO$_2$e auditado |
| Participación del cliente principal en facturación | 19 % del ingreso total (\$14.820.000.000 CLP anuales) |


La imposibilidad de certificar los estándares operacionales ya no solo genera multas y tiempos muertos, sino que constituye una amenaza a la continuidad del negocio frente al ultimátum del cliente mayor (19 % de los ingresos).

Las 142 detenciones por sobrepeso revelan una incapacidad sistemática de controlar la carga antes de iniciar la marcha, drenando 2.556 horas-camión del sistema anualmente, contraviniendo los límites de peso por eje establecidos en el (Ministerio de Obras Públicas, 1980). La negligencia de control documental se evidencia en infracciones críticas como la ocurrida en abril con sustancias peligrosas, reguladas bajo el (Ministerio de Transportes, 1995), sumándose a los 4 siniestros con lesiones documentados. Estos pasivos operativos y de seguridad colisionan de frente con las exigencias ineludibles para la renovación de 2029: un entorno donde la empresa no solo deberá erradicar las ineficiencias de peso y documentación, sino auditar con total transparencia parámetros como el CO$_2$e bajo estándares internacionales (Smart Freight Centre, 2023) y la posición instantánea de la carga bajo amenaza de cancelación de contrato.


### Mapeo de infraestructura operacional y nodos críticos


El análisis territorial de Transportes Curimón S.A. evidencia que la operación no transcurre en un recinto confinado, sino a través de una red logística distribuida en un corredor de 3.000 kilómetros lineales, donde la exposición al riesgo es máxima y el control directo es mínimo. La infraestructura fija y móvil se articula en torno a seis tipologías de nodos críticos, cuyas condiciones de conectividad y propiedad determinan los límites de la gobernanza operacional.


#### Los cinco terminales operacionales


La infraestructura principal se concentra en cinco terminales: San Bernardo (Región Metropolitana), Antofagasta, Talca, Los Ángeles y Puerto Montt. El Terminal de San Bernardo funciona como nodo matriz, alojando la torre de programación que opera 24/7, el estanque propio de combustible, el patio principal de maniobras y la sala central de servidores. Es, además, el único punto de convergencia donde se puede instalar o intervenir físicamente el equipamiento a bordo de la flota propia y de terceros. Su conectividad externa cuenta con dos enlaces de proveedores distintos.

Sin embargo, a nivel de infraestructura tecnológica local, la sala de servidores de San Bernardo cuenta con apenas 26 m$^2$, climatización por split domiciliario, una UPS básica con autonomía de 20 minutos y carencia de respaldo eléctrico industrial redundante, lo que incumple formalmente los requerimientos de sitio e infraestructura física establecidos en las Bases Técnicas Transversales (RT-06.01 a RT-06.09). Esta limitación de sitio impide alojar de manera segura sistemas centrales de procesamiento transaccional ininterrumpido sin acometer obras civiles mayores.

En contraste, los cuatro terminales regionales operan como puntos de relevo, descanso y apoyo para el conductor, provistos de un único enlace comercial y careciendo de enlace de respaldo en tres de los cuatro recintos (RT-03.10). La asimetría de conectividad entre la matriz y las regiones introduce un riesgo de desconexión latente.


#### Los dos talleres propios y la red externa


La capacidad de mantenimiento físico se sostiene en dos talleres propios (San Bernardo y Los Ángeles), operados por una dotación de 46 personas en sistema de turnos, encargados del cuidado de los 148 tractocamiones y 210 semirremolques propios.

Cualquier contingencia mecánica que ocurra fuera del radio de estos dos talleres recae en talleres externos en ruta. Actualmente, las intervenciones de estos proveedores externos carecen de toda integración técnica o de registro con la compañía; ocurren al margen de la hoja de vida del equipo, fracturando la trazabilidad de mantenimiento y degradando la seguridad preventiva.


#### Paso fronterizo Los Libertadores


El cruce hacia la provincia de Mendoza concentra un flujo de $\approx 1.900$ operaciones anuales. Este nodo internacional impone la gestión simultánea de documentación aduanera y migratoria de dos países, y está sujeto a severas disrupciones climáticas. Entre los meses de junio y septiembre, los cierres por nieve desencadenan episodios impredecibles que han alcanzado hasta 12 días continuos de clausura, generando un efecto cascada sobre la flota detenida, la carga en tránsito y la programación de jornadas de los conductores.


#### Zonas de sombra de conectividad


La ruta de 3.000 kilómetros presenta extensas zonas de sombra geográficas, superando en algunos casos los 80 kilómetros continuos sin ninguna cobertura celular, particularmente en el desierto del norte y en tramos cordilleranos. Durante el tránsito por estas franjas, la operación experimenta ceguera sistémica: se pierde la transmisión en tiempo real de la posición GPS, se interrumpe la capacidad de emitir documentos electrónicos o solicitar apoyos de emergencia, y se difiere obligadamente la entrega de datos telemáticos o de jornada.


#### Puntos de carga y descarga de clientes


El extremo comercial de cada viaje se materializa en aproximadamente 1.400 puntos distintos. Éstas constituyen instalaciones de terceros donde Curimón actúa exclusivamente en calidad de visita. Se imponen allí reglas, sistemas y tiempos de espera dictados por el cliente (registrándose tiempos medios de espera de 3 horas y 10 minutos, escalando hasta 8 horas en cosechas frutícolas). La empresa se encuentra normativamente inhabilitada para instalar equipamiento físico o infraestructura en estos recintos, varios de los cuales, además, carecen de cobertura móvil para la confirmación de entrega.


#### La cabina del camión


La cabina representa el verdadero puesto de trabajo. Constituye un entorno físico hostil, caracterizado por vibración constante, temperaturas extremas, resplandor solar y alimentación eléctrica fluctuante (12/24V). La restricción operacional y legal fundamental de este nodo ((Ministerio de Transportes y Telecomunicaciones, 2009)) es que el conductor se encuentra impedido de interactuar con cualquier dispositivo o pantalla mientras el camión está en movimiento, exigiendo que toda captura de información durante la marcha ocurra de manera automática y desatendida.


#### Síntesis de nodos operacionales


**Tabla. Síntesis de nodos operacionales e infraestructura crítica**

| **Nodo** | **Función Principal** | **Condiciones de Conectividad** | **Criticidad** |
|---|---|---|---|
| Terminal San Bernardo | Base de torre 24/7, taller principal, estanque propio y gestión central. | Dos enlaces. Sala servidores 26 m$^2$ con split doméstico y UPS 20 min (incumple RT-06.01 a 06.09). | Máxima. Único punto de intervención física a bordo. |
| Terminales Regionales (4) | Relevo, descanso y estacionamiento en Antofagasta, Talca, Los Ángeles y Pto. Montt. | Baja. Enlace único, sin respaldo en 3 de 4 recintos (RT-03.10). | Media. Soporte geográfico con fragilidad de transmisión. |
| Talleres Propios (2) | Mantenimiento preventivo y correctivo de flota propia (358 equipos sumados). | Integrados a red corporativa en San Bernardo y Los Ángeles; 46 operarios. | Alta. Sostienen disponibilidad mecánica de activos propios. |
| Talleres Externos en Ruta | Reparaciones correctivas de emergencia lejos de terminales propios. | Nula integración tecnológica; hojas de vida incompletas. | Alta. Intervenciones no registradas que degradan historial. |
| Paso Los Libertadores | Operación internacional binacional ($\approx 1.900$ cruces anuales). | Infraestructura aduanera binacional. Cierres por nieve de hasta 12 días continuos. | Alta. Volatilidad climática y bloqueo masivo de flota. |
| Zonas de Sombra en Ruta | Tránsito prolongado en áreas desérticas o cordilleranas de Ruta 5. | Nula. Más de 80 km continuos sin cobertura celular. | Crítica. Pérdida total de visibilidad, GPS y alertas. |
| Puntos de Clientes ($\approx 1.400$) | Recepción de carga, espera y entrega con firma de conformidad. | Infraestructura de terceros; varios sin señal; prohibido instalar equipos. | Alta. Foco de objeción de sobreestadías (71 %). |
| Cabina del Camión | Centro de trabajo móvil y origen del registro de jornada. | Ambiente hostil; prohibición legal de manipular pantallas en marcha. | Crítica. Restricción absoluta de interacción ((Ministerio de Transportes y Telecomunicaciones, 2009)). |


### Caracterización de actores y matriz de tensiones operacionales


El modelo operacional de Transportes Curimón S.A. se sostiene sobre un delicado equilibrio de intereses, responsabilidades y limitaciones estructurales. A partir del levantamiento oficial (Capítulo 8 de las Bases Técnicas del Caso), el diagnóstico evidencia que las fallas de control no responden primariamente a negligencia, sino a asimetrías de información y herramientas desalineadas con la realidad en terreno. A continuación, se caracterizan los diez actores críticos que determinan la viabilidad de cualquier intervención en los procesos de la compañía.


#### Fichas de caracterización de los diez actores clave


**1. Enrique Valdebenito Rioseco --- Gerente General (21 años en la empresa)**

- **Dolor Operacional Principal:** La fractura entre responsabilidad corporativa total y control operacional real sobre activos ajenos, cristalizada en el accidente de febrero, sumado a las pérdidas financieras ocultas.
- **Cita Clave:** «El sesenta por ciento de mi capacidad no me pertenece y esas personas no son mis trabajadores. Yo no les puedo dar una orden. Entonces cuando alguien me diga 'instalamos un dispositivo', le voy a preguntar quién le va a pedir permiso a ciento cuarenta y ocho dueños... y qué les vamos a ofrecer a cambio».
- **Dependencias y Necesidades de Información:** Necesita viabilidad táctica y contractual: mecanismos de incentivo a terceros e integración sin disrupción laboral ni parálisis operacional.
- **Capacidad de Bloqueo/Habilitación:** Máxima. Adjudicador final de la licitación y máxima autoridad corporativa.


**2. Ricardo Mansilla Oyarzo --- Gerente de Operaciones**

- **Dolor Operacional Principal:** Gestión de 22 despachadores operando a ciegas con 3 plataformas GPS incompatibles, 34 camiones sin cobertura y un 26 % de kilómetros en vacío resueltos por teléfono y memoria. Necesita un bloqueo de seguridad automatizado en el despacho, pero teme una parálisis operacional por exceso de rigidez.
- **Cita Clave:** «Para asignar un viaje tengo que saber cuatro cosas al mismo tiempo: dónde está el camión, si el equipo sirve para esa carga, si el conductor tiene jornada, y si los papeles están al día. De esas cuatro, hoy sé una y media... Prefiero que me bloquee a que me deje pasar».
- **Dependencias y Necesidades de Información:** Depende de la posición real del vehículo, estado de jornada del conductor, vigencias y disponibilidad de cargas de retorno en tiempo real.
- **Capacidad de Bloqueo/Habilitación:** Alta. Controla la asignación diaria y puede desestimar flujos operativos que introduzcan fricción excesiva al despacho.


**3. Yasna Colipán Marín --- Conductora de ruta (7 años, ruta norte)**

- **Dolor Operacional Principal:** Obligación de cumplir la jornada laboral en tramos de 60-80 km sin infraestructura vial segura, registro manual que no evidencia esperas abusivas de más de 6 horas en clientes, y tramos ciegos prolongados sin comunicación en el norte.
- **Cita Clave:** «Hay tramos donde a mí se me cumple el tiempo y no hay dónde parar. No hay banquina, no hay servicentro, no hay nada por sesenta kilómetros... Manejando no puedo tocar nada... Las esperas son lo peor: llego a las siete y salgo a la una de la tarde...».
- **Dependencias y Necesidades de Información:** Requiere alertas anticipadas de jornada compatibles con la disponibilidad física de paraderos seguros, sin interactuar con pantallas mientras conduce ((Ministerio de Transportes y Telecomunicaciones, 2009)).
- **Capacidad de Bloqueo/Habilitación:** Alta (operacional de facto). Si los procedimientos exigen manipulación en marcha, serán rechazados por poner en peligro la conducción.


**4. Nolberto Sandoval Pinto --- Transportista subcontratado (2 camiones, 9 años)**

- **Dolor Operacional Principal:** Vulneración de la soberanía sobre su activo patrimonial (\$200M+) mediante rastreo continuo cuando trabaja para competidores de Curimón, sumado a una opacidad financiera donde las liquidaciones tardan 9 días con frecuentes errores (11 %).
- **Cita Clave:** «Cuando me dicen que me van a instalar un aparato, yo pregunto tres cosas: quién lo paga, quién ve esa información, y qué pasa con ella cuando yo estoy trabajando para otro cliente... Si el aparato registra mis horas y eso me sirve a mí para demostrar que estoy en regla, lo acepto. Si el aparato es para que ellos me vigilen, no».
- **Dependencias y Necesidades de Información:** Depende de liquidaciones transparentes y visibilidad en tiempo real de sus viajes ejecutados para auditar sus cobros, exigiendo resguardo estricto de privacidad bajo la (Congreso Nacional de Chile, 2024).
- **Capacidad de Bloqueo/Habilitación:** Muy Alta (colectiva). Representa a 148 dueños (60,4 % de la flota). Su resistencia activa puede desabastecer de camiones a Curimón.


**5. Gabriela Ossandón Prieto --- Gerenta de Administración y Finanzas (ingreso Ene-26)**

- **Dolor Operacional Principal:** Ceguera financiera estructural. Descubrió contratos históricos operando con un -14 % de margen durante 4 años por culpa del prorrateo ciego por ingresos. Padece un retraso de 40 días en datos de combustible y un 38 % de costos en terceros gestionados con alto error manual (11 %).
- **Cita Clave:** «Repartíamos los costos por ingreso, que es la manera más elegante de no saber nada... Las rutas buenas venían subsidiando a las malas... 148 liquidaciones al mes que arman ocho personas en nueve días. El once por ciento hay que corregirlo después... Esta empresa gana nueve por ciento».
- **Dependencias y Necesidades de Información:** Requiere integración automatizada de consumo de combustible, horas-conductor y kilómetros reales para establecer un costeo analítico y liquidaciones precisas a terceros.
- **Capacidad de Bloqueo/Habilitación:** Alta. Custodia el margen operacional del 9 % y autoriza las inversiones de la compañía.


**6. Hugo Trincado Bahamonde --- Jefe de Taller y Mantenimiento**

- **Dolor Operacional Principal:** Mantenimiento preventivo fundamentado en ``adivinanza informada'' por lectura manual visual de odómetros, y 61 camiones con telemetría de fábrica inactiva. No puede intervenir físicamente ningún equipo que no pase por taller (ciclo de paso de 6 días en propios y más de 30 días en terceros).
- **Cita Clave:** «El plan preventivo es una adivinanza informada... sesenta y un camiones traen telemetría de fábrica y desde que los compramos nadie ha bajado ese dato... Cuando un camión se rompe en ruta lo arregla un taller externo y no queda en la hoja de vida...».
- **Dependencias y Necesidades de Información:** Necesita kilometraje real y códigos de falla remotos para transitar de un modelo reactivo a uno preventivo y predictivo.
- **Capacidad de Bloqueo/Habilitación:** Alta (logística). Determina la viabilidad temporal del despliegue físico de cualquier equipamiento en la flota.


**7. Denisse Aguayo Lillo --- Jefa de Prevención de Riesgos y Seguridad**

- **Dolor Operacional Principal:** Responsabilidad legal sobre 454 conductores (sólo 196 propios) sin herramientas de control previo. Gestiona $\approx 6.000$ vigencias en planillas Excel, con cero descargas de tacógrafo y una exposición directa que ya generó accidentes severos por fatiga y descontrol documental.
- **Cita Clave:** «Después del accidente me tocó explicarle a la autoridad cómo controlamos la jornada... por los de terceros no tuve nada que mostrar... Los vencimientos son mi otro dolor: como seis mil fechas vivas en cuatro planillas distintas... Prefiero frenar un viaje».
- **Dependencias y Necesidades de Información:** Requiere que el cumplimiento de jornada y vigencias documentales intercepte de forma mandatoria y vinculante el flujo de despacho.
- **Capacidad de Bloqueo/Habilitación:** Alta (normativa y de veto legal). Tiene la potestad legal y técnica de paralizar despachos ante incumplimientos de seguridad.


**8. Andrea Lecaros Vives --- Gerenta de Logística de la exportadora clave (19 % de ingresos)**

- **Dolor Operacional Principal:** Riesgo de incumplimiento ante clientes internacionales por opacidad de Curimón. Ha impuesto un ultimátum para la renovación de contrato en 2029: trazabilidad total, e-Docs, certificación de jornada en cada flete y auditoría de huella de carbono.
- **Cita Clave:** «Pedimos cuatro cosas para 2029... acreditación del cumplimiento de la jornada del conductor en cada viaje, incluidos los camiones subcontratados. No es una amenaza, es una exigencia con plazo».
- **Dependencias y Necesidades de Información:** Trazabilidad de posición en tiempo real, e-Docs, emisiones CO$_2$e auditables bajo norma GLEC y certificación de jornada legal.
- **Capacidad de Bloqueo/Habilitación:** Extrema (comercial). Condiciona la continuidad del 19 % de la facturación de Curimón (\$14.820M CLP).


**9. Patricio Kast Fuentealba --- Jefe de Control de Flota**

- **Dolor Operacional Principal:** Equipo de 6 personas forzado a consolidar mapas de 3 proveedores distintos (algunos sin permisos de exportación), 34 camiones fantasmas sin GPS y zonas ciegas interurbanas de más de 80 kilómetros.
- **Cita Clave:** «Somos seis personas mirando tres pantallas distintas... En uno ni siquiera podemos exportar. Y hay treinta y cuatro camiones sin nada... En el norte hay más de ochenta kilómetros seguidos sin señal. Ahí el camión desaparece del mapa...».
- **Dependencias y Necesidades de Información:** Estandarización de la capa de captura posicional y resolución operativa de los baches de conectividad satelital/celular.
- **Capacidad de Bloqueo/Habilitación:** Alta (técnica). Diagnostica si los procedimientos operativos son factibles de asimilar por el equipo de monitoreo.


**10. Marcelo Riquelme Ibáñez --- Jefe de Tecnologías de Información (TI)**

- **Dolor Operacional Principal:** Un ecosistema fragmentado heredado (TMS 2013 que ignora el viaje real), 5 sistemas y papeles que jamás convergen, y una dotación de solo 9 personas para atender toda la red nacional.
- **Cita Clave:** «El sistema de 2013 sabe qué viaje encargamos, no qué viaje ocurrió... hay puntos de carga sin cobertura donde el documento no se puede emitir en el momento... Cualquier cosa que vaya arriba de un camión se instala cuando pasa por un terminal: lo define la física».
- **Dependencias y Necesidades de Información:** Capacidad de operación local autónoma frente a caídas de conectividad e interoperabilidad con el legado transaccional contable.
- **Capacidad de Bloqueo/Habilitación:** Alta (tecnológica). Evalúa la viabilidad operacional de las integraciones de datos y el soporte de la infraestructura.


#### Matriz de poder vs. interés y tabla de brechas operacionales


![Matriz de Poder / Influencia vs. Nivel de Interés](\subdocRuta/Img.png)

*Figura. Matriz de Poder / Influencia vs. Nivel de Interés*


**Tabla. Consolidación de caracterización de actores y brechas operacionales**

| **Actor** | **Expectativas** | **Temores** | **Poder** | **Brechas de Información** |
|---|---|---|---|---|
| E. Valdebenito | Viabilidad sistémica; retención de cliente clave; mitigación de riesgo legal. | Exposición penal por fallas ajenas; parálisis operativa por rechazo de transportistas. | Máxima | Indicadores consolidados de riesgo, costo y cumplimiento en tablero de control. |
| R. Mansilla | Asignación eficiente sin kilómetros vacíos; validación bloqueante pre-despacho. | Sistemas excesivamente rígidos que impidan despachar; freno total de flota. | Alta (operativa) | Visibilidad integrada de posición, idoneidad del equipo, jornada y vigencias. |
| Y. Colipán | Respeto de sus tiempos reales de servicio; paraderos seguros en ruta. | Alertas inoportunas; ser sancionada por fallas del entorno vial o clientes. | Alta (ejecución) | Operación sin distracción en ruta; reconocimiento probatorio de tiempos de espera. |
| N. Sandoval | Autonomía sobre su activo; cobro ágil y preciso (sin 9 días de retraso). | Vigilancia permanente cuando opera para terceros; penalizaciones injustas. | Muy Alta (colectiva) | Control estricto de privacidad de ubicación; transparencia en pre-liquidaciones. |
| G. Ossandón | Erradicación de subsidios cruzados; costeo analítico por ruta/cliente. | Mantener contratos a -14 %; retrasos de 40 días en datos de combustible. | Alta (financiera) | Integración oportuna de combustible, odómetro y fletes para cierre ágil. |
| H. Trincado | Mantenimiento preventivo real basado en telemetría de uso. | Daños inadvertidos; fallas en ruta no registradas; instalaciones masivas imposibles. | Alta (logística) | Lectura remota de odómetros y CANbus; historial unificado de vida útil. |
| D. Aguayo | Validación vinculante pre-despacho ante vigencias caducadas o fatiga. | Nuevo siniestro con lesiones o fatal; responsabilidad penal/laboral solidaria. | Alta (veto legal) | Repositorio unificado de vigencias con capacidad de intercepción previa al despacho. |
| A. Lecaros | Cumplimiento estricto para 2029 (CO$_2$e, trazabilidad, e-Docs, jornada). | No poder auditar la cadena de suministro; perder certificaciones internacionales. | Extrema (comercial) | Reportería verificada de emisiones e historial fidedigno del 100 % de los viajes. |
| P. Kast | Coherencia en la visualización geoespacial de toda la flota. | Intermitencias crónicas en ruta norte; gestión de equipos dispares. | Alta (técnica) | Vista unificada de geolocalización que contemple áreas sin cobertura celular. |
| M. Riquelme | Integración sin silos de datos; despliegue realista y paulatino. | Exigencia de soluciones teóricas de instalación instantánea en 374 máquinas. | Alta (tecnológica) | Resiliencia operativa frente a fallas de red y sincronización con el ERP contable. |


#### Las seis tensiones operacionales irreconciliables del modelo actual


La sistematización de las posturas revela seis tensiones estructurales. Estas representan incompatibilidades verificables que requieren un mecanismo operativo y procedimental de arbitraje:


- **Seguridad vs. Continuidad Operacional (Aguayo vs. Mansilla):** Prevención de Riesgos exige bloquear la salida de cualquier camión con la mínima inconsistencia documental o de descanso ((Ministerio del Trabajo, 2006)). Operaciones teme que un bloqueo estricto detenga despachos por caducidades administrativas menores, paralizando los 96.000 viajes anuales. Falta un protocolo semántico escalonado, pues hoy la torre depende de negociaciones verbales caso a caso.
- **Visibilidad vs. Soberanía del Activo (Lecaros vs. Sandoval):** El cliente estratégico demanda el seguimiento continuo de todos los viajes para el 2029. Sin embargo, el subcontratista no tolerará el rastreo de su posición cuando preste servicios a competidores de Curimón. Bajo la (Congreso Nacional de Chile, 2024), geolocalizar a un transportista externo fuera del marco del flete activo carece de base de licitud.
- **Jornada Legal vs. Geografía Vial (Normativa vs. Colipán):** La Dirección del Trabajo y el (Ministerio del Trabajo, 2003) exigen pausas de descanso rígidas. La conductora demuestra que la geografía impone tramos desérticos de 60 a 80 km sin bermas ni paraderos seguros, forzando un incumplimiento por razones de seguridad personal y vial.
- **Visibilidad Financiera vs. Opacidad de Costos (Ossandón vs. Inercia Organizacional):** La gerencia financiera busca erradicar contratos con un -14 % de rentabilidad. Se enfrenta a un entorno transaccional donde el costeo de ruta está disgregado (combustible con 40 días de atraso, sobreestadías rechazadas, peajes desfasados), perpetuando subsidios cruzados en 3 contratos que absorben el 31 % de ingresos.
- **Mantenimiento Técnico vs. Descentralización de Activos (Trincado vs. Realidad Operativa):** Mantenimiento busca anticipar fallas mecánicas y aprovechar telemetría vehicular. No obstante, el 22 % de la flota subcontratada ingresa a un terminal propio menos de una vez al mes, y los propios regresan cada 6 días.
- **Gobernanza Corporativa vs. Imposición Tecnocrática (Valdebenito vs. Enfoque Tecnológico Unilateral):** La dirección reconoce la urgencia de cumplir las metas del cliente para 2029, pero advierte que imponer aplicaciones o dispositivos a 148 empresarios independientes mediante decretos jerárquicos conducirá al rechazo masivo de la flota externa.


**Tabla. Matriz consolidada de tensiones operacionales**

| **Tensión Operacional** | **Actores Involucrados** | **Riesgo de No Resolución** | **Requerimiento de Arbitraje** |
|---|---|---|---|
| 1. Seguridad vs. Continuidad | Prevención / Operaciones | Infracciones o paralización de despachos | Protocolo escalonado de validación pre-despacho |
| 2. Visibilidad vs. Soberanía | Cliente (Lecaros) / Transportistas externos | Pérdida del 19 % de ingresos o fuga de terceros | Geolocalización circunscrita estrictamente al flete activo |
| 3. Jornada vs. Geografía | Ley laboral / Conductores | Multas por fatiga; accidentes en carretera | Alertas contextualizadas con paraderos seguros |
| 4. Rentabilidad vs. Opacidad | Finanzas / Inercia administrativa | Destrucción continua del margen del 9 % | Consolidación oportuna de combustible, peajes y esperas |
| 5. Mantenimiento vs. Dispersión | Taller / Flota externa | Fallas en ruta; 61 CANbus ociosos | Captura remota periódica sin exigir ingreso físico |
| 6. Gobernanza vs. Imposición | Gerencia General / Terceros | Rechazo masivo de 148 dueños subcontratados | Esquema de beneficios mutuos y transparencia |


### Las diez patologías sistémicas de Transportes Curimón S.A.


El análisis del entorno operativo de Transportes Curimón S.A. evidencia que los síntomas observados no constituyen fallas aisladas, sino la manifestación clínica de diez patologías sistémicas originadas en la fractura entre responsabilidad y control. A continuación, se constata la cadena causal de cada patología, desde su origen estructural hasta su impacto cuantificable.


- **S1 --- Ceguera de Jornada:** La compañía registra cero descargas de tacógrafos digitales y carece por completo de visibilidad sobre los 258 conductores subcontratados al momento de asignar viajes. Causa raíz: inexistencia de proceso de extracción de datos y de verificación previa al despacho. Impacto: incumplimiento del (Ministerio del Trabajo, 2003) y de la (Ministerio del Trabajo, 2006), con riesgo crítico de siniestralidad (accidente km 312).
- **S2 --- Hemorragia Kilométrica en Vacío:** Acumulación de 10,66 millones de km anuales sin carga (26 % del total). Causa raíz: asignación basada en memoria humana en torre sin visibilidad de retornos. Impacto: gasto directo en combustible, peajes y desgaste del activo, erosionando el margen del 9 %.
- **S3 --- Erosión de Ingresos por Sobreestadía:** De \$340M facturados por espera, el 71 % (\$241,4M) resulta objetado. Causa raíz: incapacidad de producir prueba irrefutable de llegada y salida en $\approx 1.400$ puntos de clientes. Impacto: pérdida directa de facturación por servicios prestados.
- **S4 --- Sobrepeso Recurrente:** 142 detenciones anuales que inmovilizan 2.556 horas-camión en 2025. Causa raíz: deficiencia estructural en la verificación de tonelaje durante carga y despacho. Impacto: infracciones al (Ministerio de Obras Públicas, 1980), multas e inmovilización de equipos.
- **S5 --- Subsidios Cruzados Ocultos:** 3 contratos a pérdida (el peor a -14 % por 4 años), absorbiendo el 31 % de ingresos (\$24.180M). Causa raíz: prorrateo ciego de costos por ingreso y desfase de 40 días en combustible. Impacto: destrucción sistemática de valor financiero.
- **S6 --- Desgobierno de Vigencias:** Infracción de sustancias peligrosas con certificado vencido 3 semanas. Causa raíz: $\approx 6.000$ fechas críticas administradas en 4 planillas Excel sin integridad ni alertas. Impacto: sanciones bajo el (Ministerio de Transportes, 1995), clausura de faenas y exposición penal.
- **S7 --- Hardware Ocioso y Fragmentación Telemática:** 61 camiones con CANbus inactivo y 340 unidades en 3 plataformas GPS incompatibles (más 34 sin GPS). Causa raíz: equipamiento adquirido sin procesos de integración ni extracción. Impacto: ceguera operativa parcial y desaprovechamiento de telemetría.
- **S8 --- Fricción Administrativa en Liquidación:** Ciclo mensual de 9 días con 8 personas y 11 % de documentos corregidos tras reclamos. Causa raíz: procedimiento manual sin cruces automáticos. Impacto: costos administrativos inflados y fricción con 148 transportistas.
- **S9 --- Punto Ciego de Flota Subcontratada:** El 22 % de los camiones de terceros pasa menos de una vez al mes por terminal propio. Causa raíz: modelo de subcontratación sin supervisión técnica remota. Impacto: operación a ciegas sobre el 60,4 % de la flota.
- **S10 --- Brecha Existencial con Cliente Exportador:** El cliente mayor (19 % de facturación, \$14.820M) condiciona la renovación de 2029 a trazabilidad 100 %, posición en tiempo real, e-Docs y emisiones auditadas bajo (Smart Freight Centre, 2023). Causa raíz: brecha total entre capacidades vigentes y estándares futuros. Impacto: riesgo existencial para el negocio.


**Tabla. Las diez patologías sistémicas de Transportes Curimón S.A.**

| **N.º** | **Patología** | **Síntoma** | **Causa Raíz** | **Impacto Cuantificado** | **Caso** |
|---|---|---|---|---|---|
| **S1** | Ceguera de Jornada | 0 descargas de tacógrafo; 258 conductores sin control. | Falta de extracción y verificación pre-despacho. | Incumplimiento Art. 25 bis y Ley 20.123; fatiga (km 312). | Caps. 1, 4.3, 7.1 |
| **S2** | Hemorragia en Vacío | 26 % de km vacíos (10,66 M km/año). | Asignación manual sin visibilidad de retornos. | Gasto en combustible y peajes; erosión del margen del 9 %. | Caps. 4.2, 7.2, 8 |
| **S3** | Erosión Sobreestadía | \$241,4M/año objetados (71 % de \$340M). | Sin prueba irrefutable de llegada/salida en clientes. | Pérdida directa de facturación por servicios prestados. | Caps. 4.7, 7.2 |
| **S4** | Sobrepeso Recurrente | 142 detenciones; 2.556 h-camión perdidas en 2025. | Falla en verificación de tonelaje al cargar. | Infracción D.S. 158; multas e inmovilización de flota. | Caps. 4.5, 7.1 |
| **S5** | Subsidios Ocultos | 3 contratos a pérdida (peor al -14 %); 31 % ingreso. | Prorrateo ciego; desfase de 40 días en combustible. | Destrucción de valor en \$24.180M de ingresos facturados. | Caps. 1, 4.1, 7.3 |
| **S6** | Desgobierno Vigencias | $\approx 6.000$ fechas en 4 Excel; infracción hazmat. | Datos dispersos sin alertas automáticas ni auditoría. | Infracciones D.S. 298, riesgo penal y retención de camiones. | Caps. 1, 4.4, 7.1 |
| **S7** | Hardware Ocioso | 61 CANbus inactivos; 3 GPS dispares; 34 sin GPS. | Equipos sin extracción; sistemas incompatibles. | Pérdida de analítica; ceguera operativa parcial en torre. | Caps. 4.10, 5, 7.4 |
| **S8** | Fricción Liquidación | Ciclo 9 días, 8 personas; 11 % correcciones. | Proceso intensivo manual sin cruces automáticos. | Sobrecosto administrativo y fricción con 148 contratistas. | Caps. 4.11, 7.3 |
| **S9** | Punto Ciego Terceros | 22 % camiones externos pasa $<$ 1 vez/mes por base. | Subcontratación sin supervisión técnica remota. | Operación a ciegas sobre el estado de la flota externa. | Caps. 2.3, 6, 7.4 |
| **S10** | Brecha Existencial | Exigencias 2029 (CO$_2$e, e-Docs, trazabilidad). | Brecha total entre registro actual y exigencias 2029. | Riesgo de pérdida del 19 % de ingresos (\$14.820M). | Caps. 1, 4.6, 7.2 |


### Registro de supuestos operacionales y mapeo exhaustivo del Numeral 16.1


#### Principios de modelamiento y delimitación del diagnóstico


El análisis del Numeral 16.1 de las (Escuela de Informática PUCV, 2026c) evidencia la existencia de 26 decisiones operacionales y estratégicas deliberadamente omitidas por Transportes Curimón S.A. Para preservar el rigor metodológico del diagnóstico sin incurrir en la prefiguración prematura de soluciones, audIT ha procedido a transformar cada uno de estos vacíos en un «Supuesto Operacional y de Entorno Asumido».

Esta técnica garantiza plena coherencia metodológica: los supuestos operan exclusivamente como un marco limitante para dimensionar el nivel de madurez, el grado de fricción logística y el riesgo latente del modelo actual, pero no constituyen arquitecturas de solución ni prefiguraciones de software.


#### Matriz maestra de los 26 supuestos operacionales del Numeral 16.1


**Tabla. Matriz maestra de los 26 supuestos operacionales del Numeral 16.1**

| **N.°** | **Dominio** | **Dilema No Resuelto (Num. 16.1)** | **Supuesto del Entorno Asumido** | **Impacto en Riesgo** |
|---|---|---|---|---|
| **1** | Laboral | Acreditación de jornada en 148 contratistas que manejan para terceros. | Exige evidencia objetiva e inalterable oponible ante la DT, descartando la mera declaración verbal. | Riesgo legal alto; responsabilidad subsidiaria ((Ministerio del Trabajo, 2006)). |
| **2** | Terceros | Qué ofrecer a los 148 transportistas por compartir datos, y sanciones. | Requiere esquema de valor compartido y claridad en liquidaciones; imposición unilateral inejecutable. | Riesgo de adopción crítico; merma de disponibilidad en hasta 60,4 %. |
| **3** | Deuda Técnica | Qué hacer con el TMS de 2013: reemplazar, mantener o encapsular. | TMS 2013 es un sistema cerrado con interfaces rígidas; evaluar coexistencia o desacople funcional. | Obsolescencia basal que restringe la optimización operativa. |
| **4** | Visibilidad | Unificación con 3 proveedores GPS, acceso restringido y 34 sin GPS. | Fragmentación genera asimetría territorial crítica; 34 camiones son punto ciego de alto riesgo. | Incapacidad de asegurar acuerdos de nivel de servicio (SLA). |
| **5** | Activos Físicos | Propiedad del equipo a bordo en terceros: costeo, custodia y retiro. | Tenencia en cabinas ajenas introduce complejidad patrimonial; requiere acuerdos de custodia y retiro. | Riesgo financiero medio; complejidad en logística inversa de hardware. |
| **6** | Continuidad | Bloqueo de viaje comprometido: quién autoriza y mediante qué registro. | Bloqueo estricto no puede paralizar la operación; requiere protocolos de excepción auditables. | Riesgo de paralización crítico; impacto directo en compromisos de servicio. |
| **7** | Fatiga y Ruteo | Antelación de alerta de jornada en tramos sin paraderos seguros. | El aviso de jornada debe contextualizarse con la distancia hacia paraderos seguros en la red vial. | Siniestralidad vital e infracciones laborales por detención en bermas. |
| **8** | Tiempos | Registro de llegadas/salidas en terceros sin intervención manual. | Registro en recintos ajenos ($\approx 1.400$ puntos) debe basarse en medios probatorios objetivos sin obra local. | Objeción del 71 % de cobros de sobreestadía (\$241,4M anuales). |
| **9** | Tributaria | Emisión de e-Doc en puntos sin cobertura antes del rodaje. | Flujo documental no puede paralizarse en zonas sin señal; requiere procedimientos de contingencia. | Inmovilización física de camiones en origen por falta de enlace. |
| **10** | Comercial | Confirmación de entrega (PoD) y habilitación para facturar. | Confirmación física es asíncrona; su demora y deterioro (4,2 %) retrasa reconocimiento de ingresos. | Impacto severo en flujo de caja; aumento del ciclo de conversión. |
| **11** | Transmisión | Muestreo para posición y telemetría: en línea vs. almacenamiento. | Priorizar eventos críticos en línea; tramas telemáticas detalladas en almacenamiento local a bordo. | Saturación de planes de datos móviles y sobrecostos por tráfico. |
| **12** | Telemetría | Extracción de datos FMS/CANbus en 61 camiones propios sin procesar. | Extracción bajo estándares homologados que no comprometan las garantías vigentes de fábrica. | Desaprovechamiento de analítica de mantenimiento preventivo. |
| **13** | Evidencia | Descarga y custodia de datos de tacógrafo con integridad técnica. | Registros demandan protocolos rigurosos de conservación para constituir prueba válida ante fiscalizaciones. | Indefensión procesal ante investigaciones de la DT o tribunales. |
| **14** | Eficiencia | Criterio de asignación de retornos vacíos (26 % de km en vacío). | 10,66 M km en vacío provienen de falta de visibilidad para triangular fletes antes del fin de ida. | Erosión masiva de márgenes por gasto en combustible y peajes. |
| **15** | Analítica | Reconstrucción de costo por viaje con insumos asíncronos. | Reconstrucción opera como proceso incremental, ajustando el costo estimado al llegar liquidaciones tardías. | Tarifas comerciales fijadas sin conocimiento del costo marginal real. |
| **16** | Costeo | Costo real de camión subcontratado con solo tarifa plana visible. | Reserva comercial de terceros obliga a imputar la tarifa liquidada como costo directo contractual. | Dificultad para optimizar económicamente asignación entre flota propia y ajena. |
| **17** | Contratos | Corrección de 3 contratos bajo costo e insumos para renegociar 2027. | Renegociación de contratos deficitarios (31 % ingresos) exige evidencia granular de costos por km y ruta. | Persistencia del déficit comercial que destruye el margen consolidado. |
| **18** | Documental | Fiscalización de $\approx 6.000$ fechas con titulares externos. | Responsabilidad solidaria recae sobre Curimón; vigilancia no puede descansar en la memoria de personas. | Retención de vehículos y sanciones formales por caducidades no detectadas. |
| **19** | SUSPEL | Coincidencia entre documentos de sustancias peligrosas y carga real. | Despacho de cargas peligrosas (18 camiones) exige verificación cruzada bajo el (Ministerio de Transportes, 1995). | Riesgo de seguridad severo; emergencias químicas y sanciones graves. |
| **20** | Contingencias | Respuesta operativa ante cierre de 12 días en Los Libertadores. | Cierres prolongados requieren protocolos de suspensión de cómputo, relocalización y custodia de sellos. | Sobrecostos no recuperables y riesgos de deterioro en cargas perecibles. |
| **21** | Mantenimiento | Integración de reparaciones en talleres externos a la hoja de vida. | Reparaciones en ruta deben integrarse a la bitácora técnica para no desvirtuar el control preventivo. | Fallas catastróficas por mantenciones externalizadas no trazadas. |
| **22** | Sostenibilidad | Reporte de emisiones CO$_2$e/ton-km en terceros sin medición directa. | Cálculo de emisiones debe sustentarse en metodologías estandarizadas internacionales ((Smart Freight Centre, 2023)). | Ultimátum del cliente exportador (19 % de ingresos) no cumplido. |
| **23** | Privacidad | Proporciones de ruta e historial compartidos con clientes y terceros. | Visibilidad para mandantes debe restringirse a la ventana temporal del viaje contratado ((Congreso Nacional de Chile, 2024)). | Riesgo legal y de adopción; demandas por vulneración de datos personales. |
| **24** | Prueba | Protección de evidencia horaria ante acusaciones de manipulación. | Registros de jornada y posición requieren custodia fidedigna que impida la alteración unilateral. | Juicios laborales desfavorables por falta de medios de prueba fidedignos. |
| **25** | Implantación | Despliegue en 374 máquinas con pasos cada 6 días o $<$ 1 vez/mes (22 %). | Adecuación física sujeta a cadencia de ingreso a terminales; plan escalonado en el tiempo. | Dilatación de plazos si se asumen ritmos de enrolamiento irreales. |
| **26** | Transición | Subsistencia de la trazabilidad durante convivencia de regímenes. | Operación deberá tolerar régimen mixto transitorio con procedimientos paralelos sin degradar asignación. | Duplicación de cargas de trabajo en torres de control durante transición. |


#### Límite explícito del diagnóstico


**DELIMITACIÓN RIGUROSA DEL PRESENTE DOCUMENTO (REGLA T-22)**

audIT declara formal y expresamente que todos los supuestos modelados, condiciones operacionales y dilemas analizados en este capítulo **pertenecen con estricta y absoluta exclusividad a la formulación y comprensión del problema y del entorno operacional de Transportes Curimón S.A.** Su único propósito es delimitar los vacíos de información, diagnosticar las brechas basales y cuantificar la exposición a riesgos del negocio sin prejuzgar la implementación técnica.

**Ninguna de las condiciones o supuestos precedentes constituye una propuesta tecnológica, prefiguración de diseño de software ni selección de componentes de solución.** La totalidad de la respuesta tecnológica ---abarcando la arquitectura lógica, los componentes de software, los modelos de integración y la infraestructura de implementación--- corresponde metodológicamente al **Subdocumento 3** (Esquema de Solución y Alcance) y al **Subdocumento 4** (Arquitectura Lógica y Física de la Solución).

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
