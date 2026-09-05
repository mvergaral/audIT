# SUBDOCUMENTO 2: RESUMEN EJECUTIVO, COMPRENSIÓN DEL PROBLEMA Y DE LA NECESIDAD

**Licitación N.º TFEP-01/2026 — Caso 10: Transportes Curimón S.A.**  
**Dupla 1 (D1) — Subdocumento 2**  
**Empresa Proponente: audIT**  

---


## 2.1 Síntesis Ejecutiva de la Situación Actual y Dimensión del Desafío

El diagnóstico estructural de Transportes Curimón S.A. revela una fractura fundamental que compromete la viabilidad operacional y financiera de la compañía: la asimetría insostenible entre la responsabilidad legal, comercial y regulatoria que la empresa asume frente a sus mandantes, y el control efectivo que ejerce sobre los recursos que ejecutan el servicio. La compañía soporta el cien por ciento de la responsabilidad sobre cargas, siniestros y fiscalizaciones, pero opera en un escenario donde el 60,4 % de su capacidad de transporte (226 camiones subcontratados de un total de 374) y el 56,8 % de sus operadores (258 conductores externos frente a 196 propios) no se encuentran bajo su tuición directa. Esta disociación genera un vacío de gobernanza sobre operaciones críticas ejecutadas a nombre de Curimón, conformando un riesgo latente de magnitudes incalculables bajo el régimen de responsabilidad de la Ley N.° 20.123 (Ministerio del Trabajo y Previsión Social, 2006) y la Ley de Tránsito N.° 18.290 (Ministerio de Transportes y Telecomunicaciones, 2009).

La dimensión física del desafío amplifica esta fractura. La red logística moviliza 96.000 viajes anuales, totalizando 41 millones de kilómetros recorridos y 2,4 millones de toneladas transportadas por una flota de 374 tractocamiones a lo largo de un corredor de 3.000 kilómetros entre Antofagasta y Puerto Montt, complementado por ≈ 1.900 cruces internacionales por el paso Los Libertadores. Este despliegue territorial extenso se administra con un nivel de fragilidad financiera agudo: la facturación anual alcanza los $78.000 millones CLP, pero exhibe un margen operacional consolidado de apenas el 9 % ($7.020 millones CLP). El análisis pormenorizado del costeo expone un deterioro estructural grave: tres de los ocho contratos principales operan por debajo de la línea de costo, representando en conjunto el 31 % del ingreso total de la empresa ($24.180 millones CLP). El caso más crítico documenta un contrato ejecutado con un margen negativo del 14 % durante cuatro años consecutivos, subsidiado sistemáticamente por rutas rentables bajo un modelo ciego de prorrateo por ingreso.

La estructura de costos revela que el 38 % del gasto se destina a pagos a transportistas subcontratados ($29.640 millones CLP), el 14 % a combustible de flota propia ($10.920 millones CLP) —afectado por una dispersión de rendimiento del 19 % entre camiones idénticos y un rezago de información de 40 días— y el 12 % a remuneraciones de conductores propios ($9.360 millones CLP). Asimismo, existe una extrema concentración comercial: de una cartera de 84 clientes activos, sólo 8 contratos generan el 71 % de la facturación total ($55.380 millones CLP), situando a la empresa en una posición de vulnerabilidad crítica ante cualquier fricción de servicio.

La materialización de este desacople estructural se concentró en tres eventos críticos durante el primer semestre de 2026. El 14 de febrero (04:40 h), el accidente en el kilómetro 312 de la Ruta 5 Sur demostró la ceguera patronal de la compañía respecto a los tiempos de conducción y descanso previos de los choferes subcontratados, provocando la suspensión de contratos por seis semanas. En abril, una fiscalización inmovilizó durante 14 horas un tractocamión con sustancias peligrosas debido a un curso obligatorio vencido tres semanas antes, evidenciando el colapso del control documental bajo el D.S. N.° 298 (Ministerio de Transportes y Telecomunicaciones, 1995). Finalmente, en junio, el primer costeo analítico por ruta destapó la existencia de subsidios cruzados masivos. Estos eventos no constituyen fallas aisladas, sino manifestaciones directas de un ecosistema de datos desintegrado.

Este colapso de la gobernanza de datos se cuantifica en la gestión manual de aproximadamente 6.000 fechas de vencimiento vivas, distribuidas en cuatro planillas de cálculo aisladas que carecen de integridad referencial y alertas automáticas. A nivel de hardware instalado, se constata una omisión total en la extracción de evidencia: cero descargas históricas de tacógrafos digitales y 61 tractocamiones propios operando con telemetría CANbus de fábrica inactiva. En el plano de visibilidad, 34 camiones de terceros circulan sin ningún dispositivo GPS (monitoreados por llamada telefónica), mientras que los 340 restantes se monitorean a través de tres plataformas incompatibles que impiden conformar una vista operacional unificada.

Frente a esta vulnerabilidad sistémica, la compañía enfrenta una amenaza existencial hacia el año 2029: el cliente exportador mayor, responsable del 19 % de los ingresos ($14.820 millones CLP), ha condicionado la renovación de su contrato al cumplimiento de cuatro requisitos intransigibles. Estas exigencias imponen la necesidad de acreditar fehacientemente el cumplimiento de la jornada en cada viaje —incluyendo transportistas y choferes subcontratados bajo el Artículo 25 bis del Código del Trabajo—, contar con el cien por ciento de trazabilidad y posicionamiento de carga en tiempo real, digitalización integral de la documentación sin redigitación (e-Docs para ≈ 128.000 documentos anuales) y la emisión de reportes auditados de emisiones de gases de efecto invernadero (CO2e) por tonelada-kilómetro bajo estándares internacionales (Global Logistics Emissions Council [GLEC], 2023). Esta matriz de condiciones demanda una transformación absoluta de los estándares probatorios de Transportes Curimón S.A., cerrando el margen para operaciones basadas en la invisibilidad de los activos de terceros.


## 2.2 Desglose Cuantitativo y Diagnóstico de los 7 Bloques de Datos Duros

### Bloque 1: Flota y Asimetría de Tenencia

| Indicador | Valor |
| :--- | :--- |
| Capacidad total gestionada | 374 tractocamiones |
| Flota propia | 148 tractocamiones (39,6 %; antigüedad promedio 6,4 años) |
| Flota subcontratada | 226 tractocamiones (60,4 %) |
| Semirremolques propios | 210 equipos (ramplas planas, tolvas, furgones secos y portacontenedores) |
| Flota especializada en sustancias peligrosas (SUSPEL) | 18 tractocamiones habilitados bajo D.S. N.° 298 |
| Semirremolques refrigerados propios | 44 equipos (12 % de la capacidad; operación crítica diciembre-abril) |
| Proveedores subcontratados | 148 dueños independientes (microempresas de 1 a 4 camiones) |

> [!IMPORTANT]  
> El 60,4 % de la capacidad tractora principal no pertenece a la compañía, fragmentada entre 148 propietarios independientes que toman decisiones autónomas sobre el mantenimiento y disponibilidad de sus activos, limitando cualquier imposición jerárquica.

El análisis de la estructura de la flota evidencia una dependencia crítica hacia terceros que desequilibra la arquitectura de control. Curimón provee la interfaz comercial, los semirremolques propios (incluyendo 44 unidades refrigeradas de alta exigencia estacional) y absorbe la responsabilidad del servicio, pero el activo motriz fundamental está bajo el mando de terceros. Esta asimetría de tenencia bloquea cualquier esfuerzo de estandarización tecnológica forzada y determina que las capacidades de trazabilidad o integración no pueden depender de imposiciones jerárquicas, configurando el principal obstáculo para asegurar la fiabilidad operacional.

### Bloque 2: Fuerza Conductora y Brecha de Jornada

| Indicador | Valor |
| :--- | :--- |
| Dotación total de conductores programados | 454 operadores |
| Conductores propios | 196 (43,2 %; bajo Art. 25 bis Código del Trabajo) |
| Conductores subcontratados (externos) | 258 (56,8 %; sin relación contractual directa con Curimón) |
| Descargas históricas de tacógrafo digital | 0 registros descargados |
| Incidente de referencia (km 312) | Chofer externo con fatiga tras conducir para otro mandante sin descanso |
| Siniestros con lesiones (últimos 3 años) | 4 accidentes documentados |

El ecosistema laboral de la compañía presenta una ceguera probatoria total frente a la normativa de tiempos de conducción y descanso. Con 258 conductores que no mantienen un vínculo laboral con Curimón y cero descargas históricas de tacógrafo, la empresa asigna viajes sin evidencia objetiva de la jornada previa del operador. El accidente del kilómetro 312 subraya la gravedad de esta fisura: el cumplimiento aparente de los registros internos de la empresa no garantiza el descanso real del conductor externo, exponiendo a la compañía a responsabilidades penales, civiles y laborales subsidiarias bajo la Ley N.° 20.123 y la Ley N.° 18.290.

### Bloque 3: Red, Rutas y Fricción Logística

| Indicador | Valor |
| :--- | :--- |
| Volumetría anual | 96.000 viajes al año |
| Carga anual movilizada | 2.400.000 toneladas |
| Distancia anual recorrida | 41.000.000 de kilómetros |
| Operación en vacío | 26 % (10,66 millones de kilómetros sin carga) |
| Documentos Electrónicos de Transporte (DET) | ≈ 128.000 emisiones anuales proyectadas |
| Torre de programación | 22 operadores en turnos continuos 24x7x365 |
| Cruces fronterizos anuales (Paso Los Libertadores) | ≈ 1.900 cruces al año (cierres por nieve de hasta 12 días continuos) |

La coordinación de 41 millones de kilómetros anuales recae sobre una torre de control de 22 operadores que ejecutan la asignación de viajes sin soporte algorítmico, operando desde la memoria y la telefonía. El impacto más severo de este modelo es la generación de 10,66 millones de kilómetros recorridos sin carga, representando un 26 % de ineficiencia estructural directa sobre la capacidad rodante. A esta fricción logística se suma la volatilidad geográfica del paso Los Libertadores, cuyos cierres prolongados quiebran cualquier modelo estático de planificación de recursos, saturando la capacidad de respuesta manual del equipo de programación.

### Bloque 4: Desgobierno de Datos e Infraestructura Ociosa

| Indicador | Valor |
| :--- | :--- |
| Fechas de vencimiento vivas (estimado) | ~6.000 fechas de conductores y vehículos |
| Soporte de control documental | 4 planillas de cálculo (Excel) aisladas sin integridad referencial |
| Telemetría CANbus inactiva | 61 tractocamiones propios de fábrica nunca consultados |
| Camiones sin posicionamiento GPS | 34 tractocamiones de terceros (seguimiento puramente telefónico) |
| Plataformas de rastreo simultáneas incompatibles | 3 plataformas para 340 tractocamiones (una sin exportación) |
| Tramos en sombra celular continua | Superiores a 80 km en desierto norte y pasos cordilleranos |

Se constata un estado de inoperatividad de los datos donde la captura, integración y alerta preventiva han fallado sistemáticamente. La mantención manual de cerca de 6.000 vigencias en hojas de cálculo inconexas garantiza la aparición de incidentes por vencimientos documentales no detectados. Al mismo tiempo, la empresa desperdicia activos tecnológicos de fábrica, como el CANbus de 61 tractocamiones que nunca ha sido consultado. La fragmentación de 340 vehículos en tres plataformas de monitoreo divergentes, sumado a los 34 camiones ciegos y sombras de red celular > 80 km, destruye la posibilidad de conformar una vista operacional única.

### Bloque 5: Fricción Comercial y Tiempos de Espera

| Indicador | Valor |
| :--- | :--- |
| Tiempo medio de espera en puntos de carga | 3 horas 10 minutos (supera las 8 horas en faenas agrícolas) |
| Puntos de carga y descarga de clientes | ≈ 1.400 instalaciones ajenas |
| Cobros facturados por sobreestadía | $340.000.000 anuales |
| Cobros objetados / no recaudados por falta de prueba | 71 % ($241.400.000 anuales en pérdidas directas) |
| Documentos de entrega (POD / Guías) defectuosos o extraviados | 4,2 % con firmas ilegibles, tachaduras o pérdidas físicas |
| Proceso de liquidación mensual a terceros | 9 días hábiles de duración, 8 analistas involucrados |
| Tasa de refacturación / corrección en liquidaciones | 11 % de documentos corregidos tras reclamos de terceros |

La ausencia de registros de posicionamiento georreferenciado e inalterable genera una profunda merma financiera mediante la objeción del 71 % de los montos facturados por demoras en las instalaciones de clientes, representando $241,4 millones no recaudados. El soporte de papel, manipulable y de entrega diferida, fracasa como instrumento probatorio, agravado por un 4,2 % de comprobantes de entrega (POD) extraviados o ilegibles. Adicionalmente, el procesamiento de las liquidaciones de 148 dueños subcontratados exige 9 días de trabajo de 8 personas, resultando en un 11 % de notas de corrección post-emisión; un indicador de fricción que deteriora la confianza de los proveedores externos que sostienen la mayoría de la operación.

### Bloque 6: Estructura Financiera y Distorsión de Costos

| Indicador | Valor |
| :--- | :--- |
| Facturación bruta anual consolidada | $78.000.000.000 CLP ($78.000M) |
| Margen operacional consolidado | 9 % ($7.020.000.000 CLP anuales) |
| Contratos principales bajo la línea de costo | 3 de 8 contratos analizados |
| Participación de los 3 contratos bajo costo | 31 % del ingreso total ($24.180.000.000 CLP) |
| Caso crítico de rentabilidad negativa | -14 % de margen durante 4 años consecutivos (desde 2021) |
| Estructura de costos operacionales | Fletes terceros (38 %), Combustible (14 %), Conductores propios (12 %) |
| Combustible sobre ingreso y rezago contable | 14 % del ingreso ($10.920M CLP); hasta 40 días de desfase probatorio |
| Dispersión de rendimiento de combustible no justificada | 19 % de variación entre camiones idénticos en idéntica ruta |
| Concentración comercial de clientes | 84 clientes activos; 8 clientes concentran el 71 % de la facturación |

La rentabilidad del 9 % encubre un modelo de gestión basado en prorrateos generales que impiden el costeo analítico a nivel de ruta y viaje. El descubrimiento de que el 31 % de los ingresos de la empresa proviene de tres contratos deficitarios —uno de ellos drenando un margen del -14 % durante cuatro años ininterrumpidos— es el resultado de operar a ciegas respecto de los costos reales de ejecución. El rubro de combustible, responsable del 14 % del gasto ($10.920 millones CLP), opera bajo un esquema de facturación consolidada mensual que retrasa en 40 días la visualización del consumo, ocultando una dispersión injustificada del 19 % de rendimiento energético entre vehículos similares en la misma ruta.

### Bloque 7: Seguridad y Riesgo Existencial

| Indicador | Valor |
| :--- | :--- |
| Detenciones en ruta por exceso de peso (año 2025) | 142 eventos en plazas de pesaje oficiales |
| Horas de inmovilización por sobrepeso | 2.556 horas-camión perdidas (18 horas promedio por detención) |
| Marco normativo de pesos y dimensiones | D.S. N.° 158 (Ministerio de Obras Públicas, 1980) |
| Infracción Hazmat (abril 2026) | Curso vencido hace 3 semanas; 14 horas de inmovilización (D.S. N.° 298) |
| Siniestros con lesiones (últimos 3 años) | 4 accidentes (incluyendo vuelco en km 312 por fatiga) |
| Exigencias condicionantes del cliente principal (2029) | Trazabilidad 100 %, posición tiempo real, e-Docs, CO2e auditado |
| Participación del cliente principal en facturación | 19 % del ingreso total ($14.820.000.000 CLP anuales) |

> [!IMPORTANT]  
> La imposibilidad de certificar los estándares operacionales ya no solo genera multas y tiempos muertos, sino que constituye una amenaza a la continuidad del negocio frente al ultimátum del cliente mayor (19 % de los ingresos).

Las 142 detenciones por sobrepeso revelan una incapacidad sistemática de controlar la carga antes de iniciar la marcha, drenando 2.556 horas-camión del sistema anualmente, contraviniendo los límites de peso por eje establecidos en el Decreto Supremo N.° 158 (Ministerio de Obras Públicas, 1980). La negligencia de control documental se evidencia en infracciones críticas como la ocurrida en abril con sustancias peligrosas, reguladas bajo el D.S. N.° 298 (Ministerio de Transportes y Telecomunicaciones, 1995), sumándose a los 4 siniestros con lesiones documentados. Estos pasivos operativos y de seguridad colisionan de frente con las exigencias ineludibles para la renovación de 2029: un entorno donde la empresa no solo deberá erradicar las ineficiencias de peso y documentación, sino auditar con total transparencia parámetros como el CO2e bajo estándares internacionales (Global Logistics Emissions Council [GLEC], 2023) y la posición instantánea de la carga bajo amenaza de cancelación de contrato.

---

## 2.3 Mapeo de Infraestructura Operacional y Nodos Críticos

El análisis territorial de Transportes Curimón S.A. evidencia que la operación no transcurre en un recinto confinado, sino a través de una red logística distribuida en un corredor de 3.000 kilómetros lineales, donde la exposición al riesgo es máxima y el control directo es mínimo. La infraestructura fija y móvil se articula en torno a seis tipologías de nodos críticos, cuyas condiciones de conectividad y propiedad determinan los límites de la gobernanza operacional.

### 2.3.1 Los 5 Terminales Operacionales

La infraestructura principal se concentra en cinco terminales: San Bernardo (Región Metropolitana), Antofagasta, Talca, Los Ángeles y Puerto Montt. El Terminal de San Bernardo funciona como nodo matriz, alojando la torre de programación que opera 24/7, el estanque propio de combustible, el patio principal de maniobras y la sala central de servidores. Es, además, el único punto de convergencia donde se puede instalar o intervenir físicamente el equipamiento a bordo de la flota propia y de terceros. Su conectividad externa cuenta con dos enlaces de proveedores distintos. 

Sin embargo, a nivel de infraestructura tecnológica local, la sala de servidores de San Bernardo cuenta con apenas 26 m², climatización por split domiciliario, una UPS básica con autonomía de 20 minutos y carencia de respaldo eléctrico industrial redundante, lo que incumple formalmente los requerimientos de sitio e infraestructura física establecidos en las Bases Técnicas Transversales (RT-06.01 a RT-06.09). Esta limitación de sitio impide alojar de manera segura sistemas centrales de procesamiento transaccional ininterrumpido sin acometer obras civiles mayores.

En contraste, los cuatro terminales regionales operan como puntos de relevo, descanso y apoyo para el conductor, provistos de un único enlace comercial y careciendo de enlace de respaldo en tres de los cuatro recintos (RT-03.10). La asimetría de conectividad entre la matriz y las regiones introduce un riesgo de desconexión latente.

### 2.3.2 Los 2 Talleres Propios y la Red Externa

La capacidad de mantenimiento físico se sostiene en dos talleres propios (San Bernardo y Los Ángeles), operados por una dotación de 46 personas en sistema de turnos, encargados del cuidado de los 148 tractocamiones y 210 semirremolques propios. 

Cualquier contingencia mecánica que ocurra fuera del radio de estos dos talleres recae en talleres externos en ruta. Actualmente, las intervenciones de estos proveedores externos carecen de toda integración técnica o de registro con la compañía; ocurren al margen de la hoja de vida del equipo, fracturando la trazabilidad de mantenimiento y degradando la seguridad preventiva.

### 2.3.3 Paso Fronterizo Los Libertadores

El cruce hacia la provincia de Mendoza concentra un flujo de ≈ 1.900 operaciones anuales. Este nodo internacional impone la gestión simultánea de documentación aduanera y migratoria de dos países, y está sujeto a severas disrupciones climáticas. Entre los meses de junio y septiembre, los cierres por nieve desencadenan episodios impredecibles que han alcanzado hasta 12 días continuos de clausura, generando un efecto cascada sobre la flota detenida, la carga en tránsito y la programación de jornadas de los conductores.

### 2.3.4 Zonas de Sombra de Conectividad

La ruta de 3.000 kilómetros presenta extensas zonas de sombra geográficas, superando en algunos casos los 80 kilómetros continuos sin ninguna cobertura celular, particularmente en el desierto del norte y en tramos cordilleranos. Durante el tránsito por estas franjas, la operación experimenta ceguera sistémica: se pierde la transmisión en tiempo real de la posición GPS, se interrumpe la capacidad de emitir documentos electrónicos o solicitar apoyos de emergencia, y se difiere obligadamente la entrega de datos telemáticos o de jornada.

### 2.3.5 Puntos de Carga y Descarga de Clientes

El extremo comercial de cada viaje se materializa en aproximadamente 1.400 puntos distintos. Éstas constituyen instalaciones de terceros donde Curimón actúa exclusivamente en calidad de visita. Se imponen allí reglas, sistemas y tiempos de espera dictados por el cliente (registrándose tiempos medios de espera de 3 horas y 10 minutos, escalando hasta 8 horas en cosechas frutícolas). La empresa se encuentra normativamente inhabilitada para instalar equipamiento físico o infraestructura en estos recintos, varios de los cuales, además, carecen de cobertura móvil para la confirmación de entrega.

### 2.3.6 La Cabina del Camión

La cabina representa el verdadero puesto de trabajo. Constituye un entorno físico hostil, caracterizado por vibración constante, temperaturas extremas, resplandor solar y alimentación eléctrica fluctuante (12/24V). La restricción operacional y legal fundamental de este nodo (Ley N.° 18.290) es que el conductor se encuentra impedido de interactuar con cualquier dispositivo o pantalla mientras el camión está en movimiento, exigiendo que toda captura de información durante la marcha ocurra de manera automática y desatendida.

### 2.3.7 Tabla de Síntesis de Nodos Operacionales

| Nodo Operacional | Función Principal | Condiciones de Conectividad e Infraestructura | Criticidad Operacional |
| :--- | :--- | :--- | :--- |
| **Terminal San Bernardo (Matriz)** | Base de torre 24/7, taller principal, estanque de abastecimiento y gestión central. | Dos enlaces de datos. Sala de servidores de 26 m² con split doméstico y UPS 20 min (incumple RT-06.01 a RT-06.09). | Máxima. Único punto de intervención física a bordo para la flota. |
| **Terminales Regionales (4)** | Relevo, descanso y estacionamiento en Antofagasta, Talca, Los Ángeles y Pto. Montt. | Baja. Enlace único, sin respaldo en tres de los cuatro recintos (RT-03.10). | Media. Puntos de soporte geográfico con fragilidad de transmisión. |
| **Talleres Propios (2)** | Mantenimiento preventivo y correctivo de la flota propia (358 equipos sumados). | Integrados a la red corporativa de San Bernardo y Los Ángeles; 46 operarios. | Alta. Sostienen la disponibilidad mecánica de los activos de la empresa. |
| **Talleres Externos en Ruta** | Reparaciones correctivas de emergencia lejos de los terminales propios. | Nula integración tecnológica con el sistema central de Curimón; hojas de vida incompletas. | Alta. Intervenciones no registradas que degradan el historial mecánico. |
| **Paso Los Libertadores** | Operación internacional binacional (≈ 1.900 cruces al año). | Depende de infraestructura aduanera binacional. Cierres por nieve de hasta 12 días continuos. | Alta. Alta volatilidad climática con cierres prolongados y bloqueo de flota. |
| **Zonas de Sombra en Ruta** | Tránsito prolongado en áreas desérticas o cordilleranas de la Ruta 5 y ramales. | Nula. Extensión de más de 80 km continuos sin cobertura celular. | Crítica. Pérdida total de visibilidad, posición GPS y alertas de emergencia. |
| **Puntos de Clientes (~1.400)** | Recepción de carga, espera y entrega con firma de conformidad. | Variable. Infraestructura de terceros; varios sin cobertura celular; prohibición de instalar equipos. | Alta. Imposibilidad de instalar equipos propios; foco de objeción de esperas (71 %). |
| **Cabina del Camión** | Centro de trabajo móvil y origen del registro de la jornada. | Fluctuante según ruta. Ambiente físico hostil; prohibición legal de manipular pantallas en marcha. | Crítica. Restricción absoluta de interacción durante el avance (Ley N.° 18.290). |

---

## 2.4 Caracterización de Actores y Matriz de Tensiones Operacionales

El modelo operacional de Transportes Curimón S.A. se sostiene sobre un delicado equilibrio de intereses, responsabilidades y limitaciones estructurales. A partir del levantamiento oficial (Capítulo 8 de las Bases Técnicas del Caso), el diagnóstico evidencia que las fallas de control no responden primariamente a negligencia, sino a asimetrías de información y herramientas desalineadas con la realidad en terreno. A continuación, se caracterizan los diez actores críticos que determinan la viabilidad de cualquier intervención en los procesos de la compañía.

### 2.4.1 Fichas de Caracterización de los 10 Actores del Capítulo 8

**1. Enrique Valdebenito Rioseco — Gerente General (21 años en la empresa)**
* **Dolor Operacional Principal:** La fractura entre responsabilidad corporativa total y control operacional real sobre activos ajenos, cristalizada en el accidente de febrero, sumado a las pérdidas financieras ocultas.
* **Cita Clave:** «El sesenta por ciento de mi capacidad no me pertenece y esas personas no son mis trabajadores. Yo no les puedo dar una orden. Entonces cuando alguien me diga 'instalamos un dispositivo', le voy a preguntar quién le va a pedir permiso a ciento cuarenta y ocho dueños... y qué les vamos a ofrecer a cambio».
* **Dependencias y Necesidades de Información:** Necesita viabilidad táctica y contractual: mecanismos de incentivo a terceros e integración sin disrupción laboral ni parálisis operacional.
* **Capacidad de Bloqueo/Habilitación:** Máxima. Adjudicador final de la licitación y máxima autoridad corporativa.

**2. Ricardo Mansilla Oyarzo — Gerente de Operaciones**
* **Dolor Operacional Principal:** Gestión de 22 despachadores operando a ciegas con 3 plataformas GPS incompatibles, 34 camiones sin cobertura y un 26 % de kilómetros en vacío resueltos por teléfono y memoria. Necesita un bloqueo de seguridad automatizado en el despacho, pero teme una parálisis operacional por exceso de rigidez.
* **Cita Clave:** «Para asignar un viaje tengo que saber cuatro cosas al mismo tiempo: dónde está el camión, si el equipo sirve para esa carga, si el conductor tiene jornada, y si los papeles están al día. De esas cuatro, hoy sé una y media... Prefiero que me bloquee a que me deje pasar».
* **Dependencias y Necesidades de Información:** Depende de la posición real del vehículo, estado de jornada del conductor, vigencias y disponibilidad de cargas de retorno en tiempo real.
* **Capacidad de Bloqueo/Habilitación:** Alta. Controla la asignación diaria y puede desestimar flujos operativos que introduzcan fricción excesiva al despacho.

**3. Yasna Colipán Marín — Conductora de ruta (7 años, ruta norte)**
* **Dolor Operacional Principal:** Obligación de cumplir la jornada laboral en tramos de 60-80 km sin infraestructura vial segura, registro manual que no evidencia esperas abusivas de más de 6 horas en clientes, y tramos ciegos prolongados sin comunicación en el norte.
* **Cita Clave:** «Hay tramos donde a mí se me cumple el tiempo y no hay dónde parar. No hay banquina, no hay servicentro, no hay nada por sesenta kilómetros... Manejando no puedo tocar nada... Las esperas son lo peor: llego a las siete y salgo a la una de la tarde...».
* **Dependencias y Necesidades de Información:** Requiere alertas anticipadas de jornada compatibles con la disponibilidad física de paraderos seguros, sin interactuar con pantallas mientras conduce (Ley N.° 18.290).
* **Capacidad de Bloqueo/Habilitación:** Alta (operacional de facto). Si los procedimientos exigen manipulación en marcha, serán rechazados por poner en peligro la conducción.

**4. Nolberto Sandoval Pinto — Transportista subcontratado (2 camiones, 9 años)**
* **Dolor Operacional Principal:** Vulneración de la soberanía sobre su activo patrimonial ($200M+) mediante rastreo continuo cuando trabaja para competidores de Curimón, sumado a una opacidad financiera donde las liquidaciones tardan 9 días con frecuentes errores (11 %).
* **Cita Clave:** «Cuando me dicen que me van a instalar un aparato, yo pregunto tres cosas: quién lo paga, quién ve esa información, y qué pasa con ella cuando yo estoy trabajando para otro cliente... Si el aparato registra mis horas y eso me sirve a mí para demostrar que estoy en regla, lo acepto. Si el aparato es para que ellos me vigilen, no».
* **Dependencias y Necesidades de Información:** Depende de liquidaciones transparentes y visibilidad en tiempo real de sus viajes ejecutados para auditar sus cobros, exigiendo resguardo estricto de privacidad bajo la Ley N.° 21.719 (Ministerio Secretaría General de la Presidencia, 2024).
* **Capacidad de Bloqueo/Habilitación:** Muy Alta (colectiva). Representa a 148 dueños (60,4 % de la flota). Su resistencia activa puede desabastecer de camiones a Curimón.

**5. Gabriela Ossandón Prieto — Gerenta de Administración y Finanzas (ingreso Ene-26)**
* **Dolor Operacional Principal:** Ceguera financiera estructural. Descubrió contratos históricos operando con un −14 % de margen durante 4 años por culpa del prorrateo ciego por ingresos. Padece un retraso de 40 días en datos de combustible y un 38 % de costos en terceros gestionados con alto error manual (11 %).
* **Cita Clave:** «Repartíamos los costos por ingreso, que es la manera más elegante de no saber nada... Las rutas buenas venían subsidiando a las malas... 148 liquidaciones al mes que arman ocho personas en nueve días. El once por ciento hay que corregirlo después... Esta empresa gana nueve por ciento».
* **Dependencias y Necesidades de Información:** Requiere integración automatizada de consumo de combustible, horas-conductor y kilómetros reales para establecer un costeo analítico y liquidaciones precisas a terceros.
* **Capacidad de Bloqueo/Habilitación:** Alta. Custodia el margen operacional del 9 % y autoriza las inversiones de la compañía.

**6. Hugo Trincado Bahamonde — Jefe de Taller y Mantenimiento**
* **Dolor Operacional Principal:** Mantenimiento preventivo fundamentado en "adivinanza informada" por lectura manual visual de odómetros, y 61 camiones con telemetría de fábrica inactiva. No puede intervenir físicamente ningún equipo que no pase por taller (ciclo de paso de 6 días en propios y más de 30 días en terceros).
* **Cita Clave:** «El plan preventivo es una adivinanza informada... sesenta y un camiones traen telemetría de fábrica y desde que los compramos nadie ha bajado ese dato... Cuando un camión se rompe en ruta lo arregla un taller externo y no queda en la hoja de vida...».
* **Dependencias y Necesidades de Información:** Necesita kilometraje real y códigos de falla remotos para transitar de un modelo reactivo a uno preventivo y predictivo.
* **Capacidad de Bloqueo/Habilitación:** Alta (logística). Determina la viabilidad temporal del despliegue físico de cualquier equipamiento en la flota.

**7. Denisse Aguayo Lillo — Jefa de Prevención de Riesgos y Seguridad**
* **Dolor Operacional Principal:** Responsabilidad legal sobre 454 conductores (sólo 196 propios) sin herramientas de control previo. Gestiona ~6.000 vigencias en planillas Excel, con cero descargas de tacógrafo y una exposición directa que ya generó accidentes severos por fatiga y descontrol documental.
* **Cita Clave:** «Después del accidente me tocó explicarle a la autoridad cómo controlamos la jornada... por los de terceros no tuve nada que mostrar... Los vencimientos son mi otro dolor: como seis mil fechas vivas en cuatro planillas distintas... Prefiero frenar un viaje».
* **Dependencias y Necesidades de Información:** Requiere que el cumplimiento de jornada y vigencias documentales intercepte de forma mandatoria y vinculante el flujo de despacho.
* **Capacidad de Bloqueo/Habilitación:** Alta (normativa y de veto legal). Tiene la potestad legal y técnica de paralizar despachos ante incumplimientos de seguridad.

**8. Andrea Lecaros Vives — Gerenta de Logística de la exportadora clave (19 % de ingresos)**
* **Dolor Operacional Principal:** Riesgo de incumplimiento ante clientes internacionales por opacidad de Curimón. Ha impuesto un ultimátum para la renovación de contrato en 2029: trazabilidad total, e-Docs, certificación de jornada en cada flete y auditoría de huella de carbono.
* **Cita Clave:** «Pedimos cuatro cosas para 2029... acreditación del cumplimiento de la jornada del conductor en cada viaje, incluidos los camiones subcontratados. No es una amenaza, es una exigencia con plazo».
* **Dependencias y Necesidades de Información:** Trazabilidad de posición en tiempo real, e-Docs, emisiones CO₂e auditables bajo norma GLEC y certificación de jornada legal.
* **Capacidad de Bloqueo/Habilitación:** Extrema (comercial). Condiciona la continuidad del 19 % de la facturación de Curimón ($14.820M CLP).

**9. Patricio Kast Fuentealba — Jefe de Control de Flota**
* **Dolor Operacional Principal:** Equipo de 6 personas forzado a consolidar mapas de 3 proveedores distintos (algunos sin permisos de exportación), 34 camiones fantasmas sin GPS y zonas ciegas interurbanas de más de 80 kilómetros.
* **Cita Clave:** «Somos seis personas mirando tres pantallas distintas... En uno ni siquiera podemos exportar. Y hay treinta y cuatro camiones sin nada... En el norte hay más de ochenta kilómetros seguidos sin señal. Ahí el camión desaparece del mapa...».
* **Dependencias y Necesidades de Información:** Estandarización de la capa de captura posicional y resolución operativa de los baches de conectividad satelital/celular.
* **Capacidad de Bloqueo/Habilitación:** Alta (técnica). Diagnostica si los procedimientos operativos son factibles de asimilar por el equipo de monitoreo.

**10. Marcelo Riquelme Ibáñez — Jefe de Tecnologías de Información (TI)**
* **Dolor Operacional Principal:** Un ecosistema fragmentado heredado (TMS 2013 que ignora el viaje real), 5 sistemas y papeles que jamás convergen, y una dotación de solo 9 personas para atender toda la red nacional.
* **Cita Clave:** «El sistema de 2013 sabe qué viaje encargamos, no qué viaje ocurrió... hay puntos de carga sin cobertura donde el documento no se puede emitir en el momento... Cualquier cosa que vaya arriba de un camión se instala cuando pasa por un terminal: lo define la física».
* **Dependencias y Necesidades de Información:** Capacidad de operación local autónoma frente a caídas de conectividad e interoperabilidad con el legado transaccional contable.
* **Capacidad de Bloqueo/Habilitación:** Alta (tecnológica). Evalúa la viabilidad operacional de las integraciones de datos y el soporte de la infraestructura.

### 2.4.2 Matriz de Poder vs. Interés y Tabla de Brechas Operacionales

**a) Matriz de Poder / Influencia vs. Nivel de Interés**

```text
                           ALTO INTERÉS                          BAJO INTERÉS
                ┌───────────────────────────────┬──────────────────────────────┐
                │        GESTIONAR DE CERCA     │     MANTENER SATISFECHO      │
     ALTO       │                               │                              │
     PODER      │ • E. Valdebenito (G. General) │ • Dirección del Trabajo / MTT│
                │ • R. Mansilla (Operaciones)   │   (Autoridad Reguladora)     │
                │ • A. Lecaros (Cliente 19%)    │                              │
                │ • G. Ossandón (Finanzas)      │                              │
                │ • D. Aguayo (Prevención/Veto) │                              │
                ├───────────────────────────────┼──────────────────────────────┤
                │       MANTENER INFORMADO      │          MONITOREAR          │
     BAJO       │                               │                              │
     PODER      │ • Y. Colipán (Conductores)    │ • M. Riquelme (TI Interno)   │
    FORMAL      │ • N. Sandoval (Subcontratos)* │ • H. Trincado (Taller)       │
                │                               │ • P. Kast (Control Flota)    │
                └───────────────────────────────┴──────────────────────────────┘
* Nota: Los 148 dueños subcontratados tienen bajo poder jerárquico individual, pero alto poder de veto colectivo de facto.
```

**b) Tabla Consolidada de Caracterización y Brechas Operacionales**

| Actor | Expectativas Principales | Temores Principales | Capacidad de Bloqueo | Necesidades de Información / Brechas |
|:---|:---|:---|:---|:---|
| **E. Valdebenito** | Viabilidad sistémica; retención del cliente clave; mitigación de riesgo legal | Exposición penal por fallas ajenas; parálisis operativa por rechazo de transportistas externos | Máxima | Indicadores consolidados de riesgo, costo y cumplimiento en tablero de control |
| **R. Mansilla** | Asignación eficiente sin kilómetros vacíos; validación bloqueante pre-despacho | Sistemas excesivamente rígidos que impidan despachar; freno total de flota | Alta (operativa) | Visibilidad integrada de posición, idoneidad del equipo, jornada y vigencias |
| **Y. Colipán** | Respeto de sus tiempos reales de servicio (incluyendo esperas); paraderos seguros | Alertas inoportunas; ser sancionada por fallas del entorno vial o clientes | Alta (ejecución) | Operación sin distracción en ruta; reconocimiento probatorio del tiempo de espera |
| **N. Sandoval** | Autonomía sobre su activo; cobro ágil y preciso (sin 9 días de retraso) | Vigilancia permanente cuando opera para terceros; penalizaciones injustas | Muy Alta (colectiva) | Control estricto de privacidad de ubicación; transparencia en pre-liquidaciones |
| **G. Ossandón** | Erradicación de subsidios cruzados; costeo analítico por ruta/cliente | Mantener contratos a −14 %; retrasos de 40 días en datos de combustible | Alta (financiera) | Integración oportuna de datos de combustible, odómetro y fletes para cierre ágil |
| **H. Trincado** | Mantenimiento preventivo real basado en telemetría de uso | Daños inadvertidos; fallas en ruta no registradas; instalaciones masivas imposibles | Alta (logística) | Lectura remota de odómetros y CANbus; historial unificado de vida útil |
| **D. Aguayo** | Validación vinculante pre-despacho ante vigencias caducadas o fatiga | Nuevo siniestro con lesiones o fatal; responsabilidad penal/laboral solidaria | Alta (veto legal) | Repositorio unificado de vigencias con capacidad de intercepción previa al despacho |
| **A. Lecaros** | Cumplimiento estricto para 2029 (CO₂e, trazabilidad, e-Docs, jornada) | No poder auditar la cadena de suministro; perder certificaciones internacionales | Extrema (comercial) | Reportería verificada de emisiones e historial fidedigno del 100 % de los viajes |
| **P. Kast** | Coherencia en la visualización geoespacial de toda la flota | Intermitencias crónicas en ruta norte; gestión de equipos dispares | Alta (técnica) | Vista unificada de geolocalización que contemple áreas sin cobertura celular |
| **M. Riquelme** | Integración sin silos de datos; despliegue realista y paulatino | Exigencia de soluciones teóricas de instalación instantánea en 374 máquinas | Alta (tecnológica)| Resiliencia operativa frente a fallas de red y sincronización con el ERP contable |

### 2.4.3 Las Seis Tensiones Operacionales Irreconciliables del Modelo Actual

La sistematización de las posturas revela seis tensiones estructurales. Estas representan incompatibilidades verificables que requieren un mecanismo operativo y procedimental de arbitraje:

**1. Seguridad vs. Continuidad Operacional (Aguayo vs. Mansilla)**
* **Naturaleza del Conflicto:** Prevención de Riesgos exige bloquear la salida de cualquier camión con la mínima inconsistencia documental o de descanso, basándose en la responsabilidad legal y laboral (Ley N.° 20.123). Operaciones teme que un bloqueo estricto detenga despachos por caducidades administrativas menores, paralizando los 96.000 viajes anuales.
* **Diagnóstico Analítico:** Falta un protocolo semántico escalonado. Hoy, la torre depende de negociaciones verbales caso a caso porque las ~6.000 vigencias residen en 4 hojas de cálculo aisladas y desconectadas de las reglas operacionales.
* **Impacto Económico:** Frena la capacidad de respuesta y amenaza el margen del 9 % por despachos perdidos, mientras perpetúa la exposición a multas o accidentes graves.

**2. Visibilidad vs. Soberanía del Activo (Lecaros vs. Sandoval)**
* **Naturaleza del Conflicto:** El cliente estratégico demanda el seguimiento continuo de todos los viajes para el 2029. Sin embargo, el subcontratista advierte que no tolerará el rastreo de su posición cuando preste servicios a terceros o competidores de Curimón.
* **Diagnóstico Analítico (Ley N.° 21.719; Ministerio Secretaría General de la Presidencia, 2024):** Según el marco legal de datos personales, geolocalizar a un transportista externo fuera del marco del flete activo carece de base de licitud. Las plataformas actuales fuerzan una falsa disyuntiva entre ceguera total o monitoreo intrusivo permanente.
* **Impacto Económico:** Amenaza la renovación del contrato del 19 % de ingresos ($14.820M CLP), y simultáneamente arriesga el abandono masivo de la flota externa (60,4 %).

**3. Jornada Legal vs. Geografía Vial (Normativa vs. Colipán)**
* **Naturaleza del Conflicto:** La Dirección del Trabajo y el Artículo 25 bis exigen pausas de descanso rígidas. La conductora demuestra que la geografía de la ruta impone tramos desérticos de 60 a 80 km sin bermas ni paraderos seguros, forzando un incumplimiento por razones de seguridad personal y vial.
* **Diagnóstico Analítico:** El tacógrafo y los registros de asistencia desconocen el contexto geoespacial. Las alertas de descanso temporales no consideran la infraestructura física del camino, provocando que la norma escrita y la seguridad en terreno colisionen.
* **Impacto Económico:** Riesgo sistémico de siniestros en ruta por fatiga acumulada (como el accidente del km 312) e ineficacia en el control de conducción preventiva.

**4. Visibilidad Financiera vs. Opacidad de Costos (Ossandón vs. Inercia Organizacional)**
* **Naturaleza del Conflicto:** La gerencia financiera busca erradicar contratos con un −14 % de rentabilidad. Se enfrenta a un entorno transaccional donde el costeo de ruta está disgregado (combustible con 40 días de atraso, sobreestadías rechazadas, peajes desfasados).
* **Diagnóstico Analítico:** El prorrateo ciego de costos por ingreso oculta el verdadero consumo de cada ruta y bloquea la renegociación contractual de 2027. No existe trazabilidad unificada para fundamentar cobros de sobreestadía ($241,4M CLP perdidos).
* **Impacto Económico:** Perpetúa el subsidio cruzado en 3 contratos que absorben el 31 % de los ingresos, drenando el endeble 9 % de margen operacional de la compañía.

**5. Mantenimiento Técnico vs. Descentralización de Activos (Trincado vs. Realidad Operativa)**
* **Naturaleza del Conflicto:** El área de mantenimiento busca anticipar fallas mecánicas y aprovechar la telemetría vehicular. No obstante, la realidad operativa indica que el 22 % de la flota subcontratada ingresa a un terminal propio menos de una vez al mes, y los propios regresan cada 6 días.
* **Diagnóstico Analítico:** Proyectar inspecciones o descargas presenciales de datos sin considerar los ciclos de paso por taller es inviable. Toda captura de información de mantenimiento debe contemplar la dispersión geográfica y la operación remota desconectada.
* **Impacto Económico:** Desgaste prematuro de activos, 61 módulos telemáticos ociosos y sobrecostos por reparaciones de emergencia en ruta que no ingresan a la hoja de vida.

**6. Gobernanza Corporativa vs. Imposición Tecnocrática (Valdebenito vs. Enfoque Tecnológico Unilateral)**
* **Naturaleza del Conflicto:** La dirección de la empresa reconoce la urgencia de cumplir las metas de trazabilidad del cliente exportador para 2029, pero advierte que imponer aplicaciones o dispositivos a 148 empresarios independientes mediante decretos jerárquicos conducirá al rechazo masivo de la flota externa.
* **Diagnóstico Analítico:** Los transportistas subcontratados no son subordinados laborales; son proveedores autónomos que requieren incentivos tangibles (pre-liquidaciones rápidas, visibilidad de fletes, cobro oportuno de esperas) para adoptar estándares compartidos de datos.
* **Impacto Económico:** Riesgo de quiebre en la cadena de suministro si los terceros se niegan a operar, afectando de inmediato el 60,4 % de la capacidad de transporte de la compañía.

**Matriz Consolidada de Tensiones:**

| Tensión Operacional | Actores Involucrados | Riesgo de No Resolución | Requerimiento Operacional de Arbitraje |
|:---|:---|:---|:---|
| 1. Seguridad vs. Continuidad | Prevención / Operaciones | Infracciones o paralización de despachos | Criterio y protocolo estandarizado de validación pre-despacho |
| 2. Visibilidad vs. Soberanía | Cliente (Lecaros) / Transportistas externos | Pérdida del 19 % de ingresos o fuga de terceros | Acreditación y geolocalización circunscrita estrictamente al flete activo |
| 3. Jornada vs. Geografía | Ley laboral / Conductores | Multas por fatiga; accidentes en carretera | Alertas operacionales contextualizadas con la ubicación de paraderos seguros |
| 4. Rentabilidad vs. Opacidad | Finanzas / Inercia administrativa | Destrucción continua del margen del 9 % | Consolidación oportuna de datos de combustible, peajes y esperas por viaje |
| 5. Mantenimiento vs. Dispersión | Taller / Realidad de flota externa | Fallas en ruta; 61 CANbus ociosos | Captura remota y periódica de variables mecánicas sin exigir ingreso físico |
| 6. Gobernanza vs. Imposición | Gerencia General / Terceros | Rechazo masivo de 148 dueños subcontratados | Esquema de beneficios operativos mutuos y transparencia administrativa |

---

## 2.5 Las Diez Patologías Sistémicas de Curimón S.A. (Tabla de Síntomas S1 a S10)

El análisis del entorno operativo de Transportes Curimón S.A. evidencia que los síntomas observados no constituyen fallas aisladas, sino la manifestación clínica de diez patologías sistémicas originadas en la fractura entre responsabilidad y control. A continuación, se constata la cadena causal de cada patología, desde su origen estructural hasta su impacto cuantificable.

**S1 — Ceguera de Jornada**
La compañía registra cero descargas de tacógrafos digitales y carece por completo de visibilidad sobre los 258 conductores subcontratados al momento de asignar viajes. La causa raíz radica en la inexistencia de un proceso de extracción de datos y en la incapacidad de verificar remotamente la actividad previa de trabajadores externos. Esta condición genera un riesgo crítico de siniestralidad por fatiga, evidenciado en el accidente del kilómetro 312, y constituye un incumplimiento sostenido del Artículo 25 bis del Código del Trabajo (Ministerio del Trabajo y Previsión Social, 2001) y de la Ley N.° 20.123.

**S2 — Hemorragia Kilométrica en Vacío**
La operación acumula 10,66 millones de kilómetros anuales recorridos sin carga, cifra equivalente al 26 % del total transitado. Esta redundancia logística se origina en un modelo de asignación dependiente de la memoria humana en la torre de control, sin integración posicional unificada que permita triangular cargas de retorno. El impacto económico recae directamente sobre los costos de combustible, peajes y desgaste del activo sin contraprestación de ingreso, erosionando severamente el margen consolidado del 9 %.

**S3 — Erosión de Ingresos por Sobreestadía**
De los $340 millones CLP facturados anualmente por tiempos de espera, el 71 % ($241,4 millones CLP) resulta objetado por los clientes. Este drenaje financiero es consecuencia directa de la incapacidad operativa de producir una prueba irrefutable sobre los horarios de llegada y salida en las instalaciones de terceros (~1.400 puntos). La dependencia de anotaciones manuales vulnerables se traduce en una pérdida directa e irrecuperable de ingresos por servicios efectivamente prestados.

**S4 — Sobrepeso Recurrente**
Los registros oficiales constatan 142 detenciones por exceso de peso en un año, inmovilizando la flota productiva por un total de 2.556 horas-camión, en contravención a las disposiciones de peso máximo del D.S. N.° 158 (Ministerio de Obras Públicas, 1980). La patología surge de una deficiencia estructural en los procesos de verificación de tonelaje durante las fases de carga y despacho. Cada episodio materializa multas formales, detención del activo, pérdida de horas de conducción y un profundo daño reputacional frente a las autoridades viales y el mercado.

**S5 — Subsidios Cruzados Ocultos**
Tres de los ocho contratos principales operan a pérdida, absorbiendo el 31 % de los ingresos ($24.180 millones CLP) y registrando un margen negativo de hasta un -14 % sostenido por cuatro años. El origen del defecto es la aplicación de un prorrateo ciego de costos por ingreso y un rezago de cuarenta días en la lectura del consumo de combustible. Esta ceguera contable enmascara la verdadera rentabilidad, provocando que las rutas eficientes financien una destrucción continua de valor.

**S6 — Desgobierno de Vigencias**
La fiscalización de abril, que sancionó el transporte de sustancias peligrosas con un certificado vencido hace tres semanas, ilustra la fragilidad del control documental bajo el D.S. N.° 298 (Ministerio de Transportes y Telecomunicaciones, 1995). Aproximadamente 6.000 fechas críticas de caducidad se administran en cuatro planillas aisladas, sin integridad referencial, alertas automáticas ni pistas de auditoría. El impacto abarca inmovilizaciones vehiculares, riesgo de prohibición para operar faenas de carga peligrosa y exposición penal directa ante accidentes.

**S7 — Hardware Ocioso y Fragmentación Telemática**
La organización posee 61 tractocamiones propios con telemetría CANbus inactiva de fábrica y 340 unidades distribuidas en tres plataformas incompatibles de posicionamiento satelital (además de 34 camiones sin GPS). La causa subyacente es la instalación de equipamiento sin el desarrollo de procesos de descarga, y la contratación fragmentada de sistemas no interoperables. Como consecuencia, se pierde información operacional generada por la flota y la torre de control sufre una visibilidad parcial del territorio.

**S8 — Fricción Administrativa en Liquidación**
El ciclo mensual de liquidación a los 148 transportistas consume nueve días hábiles, ocupa a ocho administrativos y resulta en un 11 % de documentos que requieren notas de corrección tras reclamos. Esta ineficiencia surge de un procedimiento estrictamente manual que omite cualquier cruce de verificación automatizada. El efecto se manifiesta en costos de administración inflados, tensiones sostenidas con la red de transportistas subcontratados y un retraso crónico en el cierre financiero.

**S9 — Punto Ciego de Flota Subcontratada**
El 22 % de los vehículos pertenecientes a terceros transita por las instalaciones de Curimón con una frecuencia inferior a una vez por mes. La compañía sustenta su modelo de negocio en esta capacidad externa (60,4 %), pero no dispone de un mecanismo remoto de supervisión técnica. La empresa asume así la responsabilidad integral frente al cliente sobre una fracción mayoritaria de la flota de la cual desconoce el estado mecánico, el cumplimiento documental y la condición de jornada real.

**S10 — Brecha Existencial con Cliente Exportador**
El principal demandante logístico, responsable del 19 % de la facturación ($14.820 millones CLP), condiciona su renovación contractual de 2029 a la implementación de trazabilidad total, geolocalización, medición de emisiones de CO2e auditables según estándares internacionales (Global Logistics Emissions Council [GLEC], 2023) y documentación electrónica sin redigitación. La brecha operacional actual impide certificar estas obligaciones sobre los viajes despachados, arriesgando la subsistencia del negocio.

### Tabla de Síntesis Analítica: Las 10 Patologías de Transportes Curimón S.A.

| N.º | Patología | Síntoma Observable | Causa Raíz Identificada | Impacto Económico / Legal / Operacional | Trazabilidad al Caso |
|:---|:---|:---|:---|:---|:---|
| **S1** | Ceguera de Jornada | 0 descargas de tacógrafo; 258 conductores externos sin control. | Ausencia de proceso de descarga y de verificación previa al despacho para externos. | Incumplimiento Art. 25 bis y Ley N.° 20.123; siniestralidad por fatiga (km 312). | Caps. 1, 4.3, 7.1 |
| **S2** | Hemorragia Kilométrica en Vacío | 26 % de kilómetros vacíos (10,66 M km/año). | Asignación basada en memoria humana sin visibilidad de posición ni de cargas de retorno. | Gasto directo en combustible, peajes y desgaste; erosión del margen de 9 %. | Caps. 4.2, 7.2, 8 |
| **S3** | Erosión de Ingresos por Sobreestadía | $241,4 M CLP/año en cobros objetados (71 % de $340 M). | Incapacidad de generar prueba irrefutable de llegada/salida en instalaciones del cliente. | Pérdida directa de facturación por servicios efectivamente prestados. | Caps. 4.7, 7.2 |
| **S4** | Sobrepeso Recurrente | 142 detenciones; 2.556 h-camión inmovilizadas en 2025. | Falla estructural en verificación de tonelaje durante carga y despacho. | Infracción D.S. N.° 158; multas, inmovilización del activo y daño reputacional. | Caps. 4.5, 7.1 |
| **S5** | Subsidios Cruzados Ocultos | 3 contratos a pérdida (peor al -14 % por 4 años); 31 % del ingreso. | Costeo prorrateado que enmascara subsidios cruzados; desfase de 40 días en combustible. | Destrucción sostenida de valor en $24.180M CLP de ingresos facturados. | Caps. 1, 4.1, 7.3 |
| **S6** | Desgobierno de Vigencias | ~6.000 vencimientos en 4 Excel; infracción hazmat (curso vencido 3 semanas). | Datos dispersos sin alertas automáticas, integridad referencial ni pistas de auditoría. | Infracciones D.S. N.° 298, riesgo de clausura de faenas peligrosas y responsabilidad penal. | Caps. 1, 4.4, 7.1 |
| **S7** | Hardware Ocioso y Fragmentación Telemática | 61 CANbus inactivos; 340 GPS fragmentados en 3 plataformas; 34 camiones sin GPS. | Equipamiento instalado sin proceso de extracción; sistemas incompatibles no integrados. | Pérdida de analítica mecánica; ceguera operativa parcial en la torre de tráfico. | Caps. 4.10, 5, 7.4 |
| **S8** | Fricción Administrativa en Liquidación | Ciclo de 9 días con 8 administrativos; 11 % de correcciones post-emisión. | Procedimiento intensivo manual sin cruces de verificación automatizada. | Sobrecosto administrativo, demora en cierre contable y fricción con 148 transportistas. | Caps. 4.11, 7.3 |
| **S9** | Punto Ciego de Flota Subcontratada | 22 % de los camiones de terceros pasa < 1 vez/mes por terminal propio. | Modelo de subcontratación sin mecanismo de supervisión técnica remota. | Operación a ciegas sobre el estado del activo, vigencias y horas de conducción. | Caps. 2.3, 6, 7.4 |
| **S10** | Brecha Existencial con Cliente Exportador | Exigencias 2029 (CO2e, e-Docs, trazabilidad) no cumplidas actualmente. | Brecha absoluta entre capacidades vigentes de registro y exigencias futuras. | Riesgo de pérdida del 19 % de ingresos ($14.820M); colapso del margen corporativo. | Caps. 1, 4.6, 7.2 |

---

## 2.6 Registro de Supuestos Operacionales y Mapeo Exhaustivo del Numeral 16.1

### 2.6.1 Principios de Modelamiento y Delimitación del Diagnóstico

El análisis del Numeral 16.1 de las Bases Técnicas del Caso (Transportes Curimón S.A., 2026) evidencia la existencia de 26 decisiones operacionales y estratégicas deliberadamente omitidas por Transportes Curimón S.A. Para preservar el rigor metodológico del diagnóstico sin incurrir en la prefiguración prematura de soluciones, audIT ha procedido a transformar cada uno de estos vacíos en un «Supuesto Operacional y de Entorno Asumido». 

Esta técnica garantiza plena coherencia metodológica: los supuestos operan exclusivamente como un marco limitante para dimensionar el nivel de madurez, el grado de fricción logística y el riesgo latente del modelo actual, pero no constituyen arquitecturas de solución ni prefiguraciones de software.

### 2.6.2 Matriz Maestra de los 26 Supuestos del Numeral 16.1

| N.° Decisión | Área / Dominio | Dilema No Resuelto por Curimón (Numeral 16.1) | Condición Operacional / Supuesto del Entorno Asumido | Impacto en Riesgo / Viabilidad |
| :--- | :--- | :--- | :--- | :--- |
| **1** | Laboral y Normativo | Cómo obtener/acreditar la jornada de conductores externos de 148 contratistas que pueden haber conducido para otros clientes. | Se asume como supuesto operacional y de entorno de negocio que el mecanismo de acreditación de jornada debe generar evidencia objetiva e inalterable oponible ante la Dirección del Trabajo, descartando la mera declaración verbal no respaldada. | Riesgo legal alto; exposición por responsabilidad subsidiaria (Ley N.° 20.123) y fatiga no controlada. |
| **2** | Gestión de Terceros | Qué ofrecer a los 148 transportistas subcontratados a cambio de compartir datos, y penalizaciones para no adherentes. | Se asume como supuesto operacional y de entorno de negocio que la vinculación de transportistas independientes requiere un esquema de valor compartido y claridad en liquidaciones, pues la imposición unilateral resulta inejecutable. | Riesgo de adopción crítico; amenaza de merma en la disponibilidad de flota en hasta un 60,4 %. |
| **3** | Deuda Técnica | Qué hacer con el TMS de 2013: reemplazar, mantener/integrar o encapsular mediante sustitución progresiva. | Se asume como supuesto operacional y de entorno de negocio que el TMS de 2013 constituye un sistema transaccional cerrado con interfaces rígidas y silos de datos, requiriéndose evaluar su coexistencia o desacople funcional. | Impacto alto; obsolescencia basal que restringe la optimización operativa del negocio. |
| **4** | Visibilidad Geoespacial | Cómo unificar la posición de la flota operando con 3 proveedores, acceso limitado (solo lectura) en 2 de ellos y 34 camiones sin GPS. | Se asume como supuesto operacional y de entorno de negocio que la fragmentación de señales de posicionamiento genera una asimetría de visibilidad territorial crítica, tratando los 34 camiones sin equipo como un punto ciego de alto riesgo. | Riesgo operativo y de seguridad; incapacidad de asegurar acuerdos de nivel de servicio (SLA) con clientes. |
| **5** | Activos Físicos | Propiedad del dispositivo a bordo en camiones de terceros: quién costea, administra y qué sucede si el contratista abandona la flota. | Se asume como supuesto operacional y de entorno de negocio que la tenencia de dispositivos en cabinas de terceros introduce complejidad patrimonial y de inventario, debiendo contemplarse acuerdos claros de custodia y retiro. | Riesgo financiero medio; complejidad en la logística inversa del hardware instalado. |
| **6** | Continuidad Operativa | Qué ocurre cuando la verificación de requisitos bloquea un viaje ya comprometido: quién autoriza y mediante qué registro. | Se asume como supuesto operacional y de entorno de negocio que un bloqueo estricto no puede derivar en parálisis operacional, asumiéndose la necesidad de protocolos formales de escalamiento y excepciones auditables con registro de responsabilidad. | Riesgo de paralización crítico; impacto directo en compromisos comerciales y nivel de servicio. |
| **7** | Fatiga y Ruteo | Con cuánta antelación alertar el agotamiento de jornada, considerando tramos de ruta sin lugares seguros de detención. | Se asume como supuesto operacional y de entorno de negocio que el aviso de término de jornada no puede ser un reloj estático, sino que debe contextualizarse anticipadamente con la distancia hacia paraderos seguros en la red vial. | Riesgo de siniestralidad vital e infracciones laborales por detención en bermas no autorizadas. |
| **8** | Control de Tiempos | Cómo registrar llegadas/salidas en puntos de terceros sin intervención manual del conductor ni instalación de equipos locales. | Se asume como supuesto operacional y de entorno de negocio que el registro de presencia en recintos ajenos (~1.400 puntos) debe basarse en medios probatorios objetivos que no requieran instalar infraestructura en predios de clientes. | Riesgo financiero recurrente; objeción del 71 % de cobros de sobreestadía ($241,4M CLP anuales). |
| **9** | Integración Tributaria | Cómo emitir el e-Doc en puntos de carga sin cobertura móvil (sombra de red), considerando que su emisión es un requisito previo al rodaje. | Se asume como supuesto operacional y de entorno de negocio que el flujo documental no puede paralizarse en zonas sin señal celular, demandando procedimientos operativos de contingencia para la continuidad de faenas en sombra. | Riesgo normativo y operacional; inmovilización física de camiones en origen por falta de enlace. |
| **10** | Trazabilidad Comercial | Cómo obtener la confirmación de entrega (PoD) del destinatario y en qué momento se habilita para facturación o defensa de cobros. | Se asume como supuesto operacional y de entorno de negocio que la confirmación de entrega física es un hito asíncrono cuya demora actual (hasta días) y tasa de deterioro (4,2 %) retrasa el reconocimiento de ingresos. | Impacto severo en flujo de caja; aumento del ciclo de conversión de efectivo y cobros diferidos. |
| **11** | Transmisión de Datos | Qué frecuencia de muestreo utilizar para posición y telemetría, balanceando qué se transmite en línea versus qué se almacena a bordo. | Se asume como supuesto operacional y de entorno de negocio que las limitaciones de cobertura exigen priorizar eventos críticos de seguridad en línea, mientras que las tramas telemáticas detalladas se preservan en almacenamiento local a bordo. | Impacto en viabilidad técnica; saturación de planes de datos móviles y sobrecostos por tráfico innecesario. |
| **12** | Telemetría de Fábrica | Qué hacer con la telemetría FMS/CANbus instalada de fábrica en 61 tractocamiones, la cual no está siendo procesada actualmente. | Se asume como supuesto operacional y de entorno de negocio que la extracción de datos mecánicos en los 61 camiones propios debe ejecutarse bajo estándares homologados que no comprometan las garantías vigentes de los fabricantes. | Impacto operacional medio; desaprovechamiento de analítica de mantenimiento preventivo y consumo. |
| **13** | Custodia de Evidencia | Quién descarga la data del tacógrafo, con qué periodicidad, dónde se custodia y con qué garantías de integridad técnica. | Se asume como supuesto operacional y de entorno de negocio que los registros de tacógrafo demandan protocolos rigurosos de conservación e inalterabilidad para constituir prueba válida ante fiscalizaciones y litigios. | Riesgo legal alto; indefensión procesal ante investigaciones de la Dirección del Trabajo o tribunales. |
| **14** | Eficiencia de Flota | Cómo y con qué criterio asignar el viaje de retorno a un camión que previsiblemente quedará vacío (26 % de kilómetros en vacío). | Se asume como supuesto operacional y de entorno de negocio que los 10,66 millones de km en vacío provienen de la falta de visibilidad oportuna de itinerarios para triangular fletes de retorno antes del término del viaje de ida. | Impacto financiero directo; erosión masiva de márgenes de contribución por gasto en combustible y peajes. |
| **15** | Contabilidad Analítica | Cómo reconstruir el costo por viaje recibiendo insumos asíncronos (combustible a 40 días, TAG mensual, llantas por planilla). | Se asume como supuesto operacional y de entorno de negocio que la reconstrucción del costo por flete opera como un proceso incremental, donde el costo operacional estimado se ajusta conforme ingresan las liquidaciones tardías. | Impacto financiero alto; tarifas comerciales fijadas sin conocimiento del costo marginal real. |
| **16** | Costeo de Terceros | Cómo estimar el costo real operativo de un camión subcontratado cuando Curimón solo visibiliza la tarifa plana de flete pagada. | Se asume como supuesto operacional y de entorno de negocio que la reserva comercial del transportista externo obliga a considerar la tarifa de flete liquidada como el costo directo imputable, asumiendo su variabilidad contractual. | Riesgo de gestión estratégico; dificultad para optimizar económicamente la asignación entre flota propia y ajena. |
| **17** | Evaluación de Contratos | Qué acciones correctivas tomar ante los 3 contratos operativos bajo el costo y qué data levantar para su renegociación en 2027. | Se asume como supuesto operacional y de entorno de negocio que la renegociación de contratos deficitarios (31 % de ingresos) exige contar con evidencia granular y auditada de costos por kilómetro, ruta y tiempos de detención. | Impacto financiero crítico; persistencia del déficit comercial que destruye el margen consolidado. |
| **18** | Gestión Documental | Cómo fiscalizar ~6.000 fechas de expiración y a quién responsabilizar cuando el titular del documento es una empresa externa. | Se asume como supuesto operacional y de entorno de negocio que la responsabilidad legal solidaria en ruta recae sobre Curimón, exigiendo que la vigilancia de vigencias no descanse en la memoria de los funcionarios. | Riesgo administrativo y penal alto; retención de vehículos y sanciones formales por caducidades no detectadas. |
| **19** | Cargas Peligrosas | Cómo verificar que los documentos de sustancias peligrosas (SUSPEL) a bordo coincidan con la carga real física, no con la teórica. | Se asume como supuesto operacional y de entorno de negocio que el despacho de cargas peligrosas (18 camiones) exige verificación cruzada entre la guía física, el manifiesto de carga y la habilitación del conductor bajo D.S. N.° 298. | Riesgo de seguridad severo; emergencias químicas en ruta y sanciones ambientales graves. |
| **20** | Gestión de Contingencias| Cómo responde el modelo si el Paso Los Libertadores cierra 12 días con camiones inmovilizados, carga sellada y conductores perdiendo jornada. | Se asume como supuesto operacional y de entorno de negocio que los cierres climáticos prolongados en frontera requieren protocolos especiales de suspensión de cómputo de servicio, relocalización y custodia de cargas selladas. | Impacto logístico extremo; sobrecostos no recuperables y riesgos de deterioro en cargas perecibles. |
| **21** | Hoja de Vida del Activo | Cómo integrar intervenciones mecánicas realizadas por talleres de terceros dentro de la bitácora unificada de mantenimiento. | Se asume como supuesto operacional y de entorno de negocio que las reparaciones en ruta deben integrarse a la bitácora técnica de la máquina para no desvirtuar el control preventivo ni la seguridad operativa. | Impacto mecánico alto; fallas catastróficas por mantenciones externalizadas no trazadas. |
| **22** | Sostenibilidad (GHG) | Cómo reportar las emisiones de CO2 equivalente por tonelada-kilómetro en camiones de terceros donde no existe medición directa. | Se asume como supuesto operacional y de entorno de negocio que el cálculo de emisiones para la flota subcontratada debe sustentarse en metodologías estandarizadas reconocidas internacionalmente (GLEC / ISO 14083:2023). | Riesgo comercial vital; ultimátum del cliente exportador (19 % de ingresos) condicionado a reportes auditados. |
| **23** | Privacidad de Datos | Qué proporciones de ruta e historial se comparten con el cliente final y cómo conciliarlo con la autorización de cada dueño de camión. | Se asume como supuesto operacional y de entorno de negocio que la visibilidad para mandantes debe restringirse estrictamente a la ventana temporal del viaje contratado, protegiendo la privacidad según la Ley N.° 21.719. | Riesgo legal y de adopción; rechazo de transportistas y posibles demandas por vulneración de datos. |
| **24** | Seguridad de la Prueba | Cómo proteger la evidencia horaria frente a acusaciones de manipulación de registros de jornada por parte de los conductores o el contratista. | Se asume como supuesto operacional y de entorno de negocio que los registros de eventos de jornada y posicionamiento requieren mecanismos de custodia fidedigna que impidan la alteración unilateral de la prueba. | Riesgo probatorio alto; juicios laborales desfavorables por falta de medios de prueba fidedignos. |
| **25** | Logística de Implantación| Cómo desplegar equipos a bordo en 374 máquinas que pasan por terminal cada 6 días, o los contratistas que van menos de 1 vez al mes (22 %). | Se asume como supuesto operacional y de entorno de negocio que cualquier adecuación física a bordo estará sujeta a la cadencia de ingreso a los terminales propios, demandando un plan escalonado en el tiempo. | Riesgo de proyecto alto; dilatación de plazos si se asumen ritmos de enrolamiento irreales. |
| **26** | Transición Operativa | Cómo subsiste la trazabilidad de Curimón durante la fase de transición, donde convivirán camiones equipados y unidades rezagadas. | Se asume como supuesto operacional y de entorno de negocio que la operación deberá tolerar un régimen mixto transitorio, manteniendo procedimientos paralelos sin degradar la seguridad ni la asignación. | Riesgo de gestión operativa; duplicación de cargas de trabajo en torres de control durante la transición. |

### 2.6.3 Límite Explícito del Diagnóstico (Frontera formal con Subdoc 3 y Subdoc 4)

> [!WARNING]
> **DELIMITACIÓN RIGUROSA DEL PRESENTE DOCUMENTO (REGLA T-22)**  
> audIT declara formal y expresamente que todos los supuestos modelados, condiciones operacionales y dilemas analizados en este capítulo **pertenecen con estricta y absoluta exclusividad a la formulación y comprensión del problema y del entorno operacional de Transportes Curimón S.A.** Su único propósito es delimitar los vacíos de información, diagnosticar las brechas basales y cuantificar la exposición a riesgos del negocio sin prejuzgar la implementación técnica.  
> 
> **Ninguna de las condiciones o supuestos precedentes constituye una propuesta tecnológica, prefiguración de diseño de software ni selección de componentes de solución.** La totalidad de la respuesta tecnológica —abarcando la arquitectura lógica, los componentes de software, los modelos de integración y la infraestructura de implementación— corresponde metodológicamente al **Subdocumento 3** (Esquema de Solución y Alcance) y al **Subdocumento 4** (Arquitectura Lógica y Física de la Solución).

---

## 2.7 Referencias Normativas y de la Industria (Norma APA 7.ª Edición)

Global Logistics Emissions Council. (2023). *GLEC framework for logistics emissions methodologies: Version 3.0* (Coincidente con la norma ISO 14083:2023). Smart Freight Centre.

Ministerio de Obras Públicas. (1980). *Decreto Supremo N.° 158: Fija peso máximo de los vehículos que pueden circular por caminos públicos* (Texto refundido y actualizado con la modificación del Decreto N.° 181 de 2025). Biblioteca del Congreso Nacional de Chile. https://www.bcn.cl/leychile/navegar?idNorma=10212

Ministerio de Transportes y Telecomunicaciones. (2009). *Decreto con Fuerza de Ley N.° 1: Fija texto refundido, coordinado y sistematizado de la Ley de Tránsito N.° 18.290*. Biblioteca del Congreso Nacional de Chile. https://www.bcn.cl/leychile/navegar?idNorma=1007469

Ministerio de Transportes y Telecomunicaciones. (1995). *Decreto Supremo N.° 298: Reglamenta transporte de cargas peligrosas por calles y caminos*. Biblioteca del Congreso Nacional de Chile. https://www.bcn.cl/leychile/navegar?idNorma=12087

Ministerio del Trabajo y Previsión Social. (2003). *Decreto con Fuerza de Ley N.° 1: Fija el texto refundido, coordinado y sistematizado del Código del Trabajo (Artículo 25 bis sobre jornada de choferes de carga terrestre interurbana)*. Biblioteca del Congreso Nacional de Chile. https://www.bcn.cl/leychile/navegar?idNorma=207436

Ministerio del Trabajo y Previsión Social. (2006). *Ley N.° 20.123: Regula trabajo en régimen de subcontratación, el funcionamiento de las empresas de servicios transitorios y el contrato de trabajo de servicios transitorios*. Biblioteca del Congreso Nacional de Chile. https://www.bcn.cl/leychile/navegar?idNorma=254080

Ministerio Secretaría General de la Presidencia. (2024). *Ley N.° 21.719: Regula el tratamiento y la protección de los datos personales y crea la Agencia de Protección de Datos Personales*. Biblioteca del Congreso Nacional de Chile. https://www.bcn.cl/leychile/navegar?idNorma=1209272

Transportes Curimón S.A. (2026). *Pliego de Licitación TFEP-01/2026: Bases Administrativas FEP01.26, Bases Técnicas Transversales FEP02.26 y Bases Técnicas del Caso FEP03.10.26*.

---

*Fin del Subdocumento 2 — Comprensión del Problema y de la Necesidad*  
*Dupla 1 (D1) — Licitación N.º TFEP-01/2026*  
*Caso 10: Transportes Curimón S.A. · Proponente: audIT*