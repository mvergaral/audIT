# **1 · Las diez frases de las bases**

Éste es el entregable A.1.

| Cláusula | Qué no está dicho | Riesgo que produce |
| :---- | :---- | :---- |
| BT-1 | No define APIs, protocolos, SLA de respuesta ni documentación de los sistemas legados (.NET y Oracle 2013), ni cómo garantizar consistencia «en línea» ante intermitencias de red en 62 salas. | Asunción a costo fijo de sobreesfuerzos no cuantificables de ingeniería inversa y desarrollo de conectores para sistemas legados obsoletos e indocumentados (POS Caja 7 .NET y Motor Oracle 2013), con fallas de consistencia transaccional atribuidas al oferente ante intermitencias de red en salas. |
| BT-2 | No precisa el volumen, estado ni criterios de aceptación objetivos para la depuración de datos maestros, ni asigna la responsabilidad del gobierno del dato al mandante. | Consumo desmedido de horas de ingeniería de datos y desfase en el cronograma por la obligación de sanear y reconciliar a costo fijo 15 años de inconsistencias y vacíos en los maestros de 38.000 SKU en SAP ECC sin criterios formales de aceptación. |
| BT-3 | No fija ninguna métrica matemática (MAPE/WMAPE), nivel de agregación ni umbral numérico para la precisión del pronóstico en datos con quiebres históricos de 9,4%. | Rechazo subjetivo e inapelable del modelo de pronóstico de demanda en la etapa de homologación por falta de métricas cuantitativas contractuales, reteniendo hitos de pago e imputando multas por retraso al oferente. |
| BT-5 | No define la cantidad de etiquetas por sala, el mix de tamaños para cumplir el PPUM, la tecnología inalámbrica, los rieles mecánicos (frío/seco) ni las obras eléctricas/PoE necesarias. | Sobrecostos directos por mayor densidad de etiquetas requeridas, necesidad de accesorios especiales para zonas refrigeradas y obras civiles de montaje eléctrico/red en 18 salas que superen el presupuesto preliminar de hardware. |
| BT-6 | Da por adecuada la red de 62 salas sin presentar auditorías de cobertura Wi-Fi, ancho de banda WAN, latencias, switches PoE disponibles ni segmentación de tráfico. | Fallas en la sincronización de precios y etiquetas en sala atribuidas contractualmente al software del proveedor debido a obsolescencia, saturación o cobertura deficiente de la red local del cliente no acreditada previamente. |
| BT-7 | No establece ventanas horarias permitidas (turnos nocturnos/festivos) ni excluye los periodos de congelamiento operacional («blackouts») de retail en temporadas de alta venta. | Sobrecostos laborales por cuadrillas nocturnas y descalce del cronograma de despliegue en 62 salas debido a bloqueos de acceso a salas impuestos por la gerencia comercial en periodos de alta venta. |
| BT-8 | No limita la responsabilidad a las leyes vigentes a la firma, no fija tope indemnizatorio ni contempla compensaciones por sobrecostos ante reformas legales sobrevinientes (Ley 21.719, Ley 21.663, IA). | Traspaso directo de multas regulatorias millonarias (SERNAC, Protección de Datos, Ciberseguridad) y absorción a costo fijo de costosos rediseños arquitectónicos por normativas promulgadas durante la ejecución del contrato. |
| BA-1 | No contempla cláusula de reajuste por inflación (IPC/UF) ni mecanismos de cobertura cambiaria ante alzas del dólar en hardware importado y suscripciones de nube. | Erosión severa de la utilidad del contrato por alzas en el tipo de cambio USD/CLP o inflación que encarezcan el hardware importado de etiquetas electrónicas y los consumos de infraestructura cloud/SaaS a precio fijo en pesos. |
| BA-2 | No fija un límite máximo a las multas acumuladas, computa días corridos ($408.700/día) y no excluye retrasos causados por demoras o incumplimientos del propio mandante. | Aplicación de multas punitivas ilimitadas de $408.700 diarios por atrasos en hitos de pago derivados de demoras o bloqueos imputables al propio mandante, amenazando la solvencia del proyecto y la boleta de garantía. |
| BA-3 | No define cuantitativamente el alcance de un cambio «menor» en horas o costo, no limita el número de solicitudes ni exige un proceso formal de control de cambios. | Desviación masiva de horas de desarrollo por acumulación descontrolada de requerimientos adicionales exigidos por el mandante a costo cero bajo la etiqueta ambigua de «cambios menores». |

# **2 · RBS de referencia**

| Rama | Categorías de nivel 2 para este caso | Riesgos que caen aquí |
| :---- | :---- | :---- |
| 1 · Solución y tecnología | 1.1 Precisión y calibración del motor de pronóstico de demanda de 21 días (C1)1.2 Propagación de radiofrecuencia, cobertura y latencia en etiquetas ESL (C4)1.3 Alucinación, latencia y costos de inferencia del asistente de lenguaje natural (C5)1.4 Reglas de cálculo y consistencia del precio por unidad de medida (PPUM) dinámico (C3) | R-01, R-02 |
| 2 · Integración y legado | 2.1 Lógica indocumentada y stored procedures del motor de promociones Oracle 20132.2 Capacidad de integración y dependencia del equipo del POS «Caja 7» (.NET)2.3 Latencia de sincronización y obsolescencia de interfaces en SAP ECC 20112.4 Dependencia de APIs y SLA del WMS externo de centros de distribución (contrato 2028\) | R-03, R-04, R-05 |
| 3 · Operación del cliente | 3.1 Heterogeneidad y saturación de la infraestructura de red LAN/WAN en 62 salas3.2 Restricciones de ventanas nocturnas de instalación física de ESL sin alteración de servicio (BT-7)3.3 Inconsistencia en datos de trastienda y disparidad regional en planillas Excel de reposición3.4 Dispersión geográfica longitudinal extrema para logística y soporte | R-06, R-07 |
| 4 · Personas y adopción | 4.1 Resistencia al cambio y hábitos de reposición manual en planillas Excel por zona4.2 Adopción, usabilidad y confianza en herramientas de IA y asistente conversacional C5 en sala | R-08, R-09 |
| 5 · Contrato y licitación | 5.1 Cláusulas económicas, penalidades e indexación (precio fijo BA-1 y multas 10 UF/día BA-2)5.2 Ambigüedad en alcance, soporte y obligaciones (cambios menores BA-3 y soporte 3 meses BA-5) | R-10, R-11 |
| 6 · Regulatorio y externo | 6.1 Normativa comercial y rotulación PPUM (dictamen SERNAC feb-2026, multas 300 UTM)6.2 Legislación de datos personales, ciberseguridad e IA (Ley 21.719 dic-2026, Ley 21.663, Bol. 16821-19) | R-12, R-13 |
| 7 · Empresa proveedora | 7.1 Cadena de suministro, importación y logística internacional de hardware ESL y pasarelas7.2 Capacidad técnica, retención de perfiles clave MLOps/Data y dimensionamiento Cloud/Edge | R-14, R-15 |

# **3 · Registro de riesgos de referencia**

Quince riesgos, redactados con la forma exigida. La columna de exposición es el producto de los valores de la escala, no de la probabilidad por el impacto en pesos. La derivación de cada cifra está en el capítulo 4\.

| ID | RBS | Enunciado causa – riesgo – efecto | Dueño | Probabilidad | Impacto | Zona |
| :---- | :---- | :---- | :---- | :---- | :---- | ----- |
| R-01 | 1 · Solución y tecnología | Dado que la cláusula BT-3 exige que el motor de pronóstico alcance una precisión acorde al estándar de la industria sin fijar una métrica formal ni umbrales cuantitativos para los 38.000 SKU, entonces puede que el mandante rechace la entrega del componente C1 en el piloto alegando desviaciones en categorías de baja rotación, teniendo como consecuencia un retrabajo imprevisto de ingeniería de datos y retraso en el hito del piloto con aplicación de multas contractuales bajo BA-2. | Especialista MLOps | Alta · 0,70 — Práctica común de objetar recepciones en ausencia de métricas | Muy alto · 0,80 | 0,56 · Crítica |
| R-02 | 1 · Solución y tecnología | Dado que el asistente C5 debe procesar consultas operativas y márgenes financieros en lenguaje natural mediante llamadas a modelos de lenguaje (LLM) sin arquitectura determinista, entonces puede que el sistema genere respuestas numéricas imprecisas (alucinaciones) o desborde el consumo de tokens en sala, teniendo como consecuencia el rediseño de la arquitectura RAG con capas de validación SQL y un sobrecosto en licencias y consumo de API. | Arquitecto de Solución | Media · 0,50 — Comportamiento estocástico de LLMs comerciales en consultas analíticas | Alto · 0,40 | 0,20 · Alta |
| R-03 | 2 · Integración y legado | Dado que el motor de promociones de Vega Austral opera desde 2013 sobre Oracle sin documentación técnica ni funcional de sus reglas de multicompra y combos, entonces puede que el equipo de desarrollo no logre descifrar ni replicar oportunamente la lógica en el componente C3, teniendo como consecuencia un extenso esfuerzo de ingeniería inversa sobre base de datos y atraso crítico en la integración de precios con riesgo de multas bajo BA-2. | Arquitecto de Integración | Muy alta · 0,90 — Hecho declarado: motor de 13 años indocumentado | Muy alto · 0,80 | 0,72 · Crítica |
| R-04 | 2 · Integración y legado | Dado que el POS «Caja 7» en 620 cajas depende exclusivamente de dos personas internas para desarrollo y soporte, entonces puede que dicho equipo no tenga capacidad para construir y desplegar las interfaces de sincronización de precios de C3 a tiempo, teniendo como consecuencia el desarrollo de un middleware de compatibilidad en .NET por nuestra cuenta y la ejecución de pruebas extraordinarias de estrés en cajas para evitar descalces en sala. | Líder de Integración | Alta · 0,70 — Capacidad operativa de 2 mantenedores saturada por fallas del día a día | Alto · 0,40 | 0,28 · Alta |
| R-05 | 2 · Integración y legado | Dado que la gestión de bodega en los tres centros de distribución está a cargo de un proveedor externo de WMS con contrato hasta 2028 sin obligaciones con esta licitación, entonces puede que el proveedor se niegue o demore en habilitar servicios web para recibir las órdenes de C2, teniendo como consecuencia implementar interfaces de contingencia desacopladas vía archivos batch y pruebas adicionales de sincronización. | Arquitecto de Solución | Media · 0,50 — Depende de la disposición comercial de un tercero incumbente | Moderado · 0,20 | 0,10 · Media |
| R-06 | 3 · Operación del cliente | Dado que la cláusula BT-6 asume que la red en las 62 salas es adecuada sin certificar switches PoE ni estabilidad WAN en locales de regiones, entonces puede que al desplegar las pasarelas IoT de C4 y consultas de C5 la red colapse por falta de puertos y baja tasa de transferencia, teniendo como consecuencia la necesidad de suministrar equipamiento de borde y routers de respaldo junto con soporte técnico en terreno. | Jefe de Despliegue en Terreno | Alta · 0,70 — Parque de salas regional heterogéneo con 15 años de operación | Alto · 0,40 | 0,28 · Alta |
| R-07 | 3 · Operación del cliente | Dado que la cláusula BT-7 prohíbe interferir con la operación comercial restringiendo la instalación de ESL en 18 salas a ventanas nocturnas de 4 a 5 horas, entonces puede que demoras de acceso en tiendas reduzcan el rendimiento de montaje de cuadrillas, teniendo como consecuencia contratar cuadrillas de refuerzo en horario extraordinario nocturno y riesgo de atraso en el hito del piloto. | Jefe de Despliegue en Terreno | Alta · 0,70 — Restricción operativa explícita de bases y dispersión geográfica | Alto · 0,40 | 0,28 · Alta |
| R-08 | 4 · Personas y adopción | Dado que los jefes de sala de las 62 sucursales gestionan hoy sus pedidos mediante planillas Excel manuales con criterios empíricos propios por zona, entonces puede que el personal de sala rechace o altere las sugerencias de reposición de C2 manteniendo sus pedidos manuales, teniendo como consecuencia la necesidad de talleres de refuerzo, capacitación presencial y soporte de adopción en terreno. | Consultor Gestión del Cambio | Alta · 0,70 — Práctica histórica declarada de 62 salas operando en planillas aisladas | Alto · 0,40 | 0,28 · Alta |
| R-09 | 4 · Personas y adopción | Dado que el personal de sala tiene baja familiaridad con interfaces conversacionales de IA y no cuenta con protocolos claros de consulta rápida en pasillo, entonces puede que el asistente C5 sea subutilizado por desconfianza operativa, teniendo como consecuencia la necesidad de simplificar interfaces de usuario (UX) y readecuar los prompts de consulta. | Diseñador UX / Adopción | Media · 0,50 — Disposición de usuarios finales en piso no evaluada en las bases | Moderado · 0,20 | 0,10 · Media |
| R-10 | 5 · Contrato y licitación | Dado que la cláusula BA-3 faculta al mandante a exigir cambios de alcance menores sin costo adicional sin definir métrica de horas ni límite acumulado, entonces puede que Vega Austral solicite continuas modificaciones a los modelos predictivos y tableros bajo este rótulo, teniendo como consecuencia un desvío no facturable de horas de ingeniería de software y retraso en el cronograma general. | Gerente de Contratos y Oferta | Alta · 0,70 — Cláusula abierta sin tope, práctica habitual para absorber indefiniciones | Alto · 0,40 | 0,28 · Alta |
| R-11 | 5 · Contrato y licitación | Dado que la cláusula BA-2 impone una multa de 10 UF por día corrido sin tope y no exime atrasos originados por demoras del mandante en sus definiciones funcionales (BT-9), entonces puede que retrasos en validaciones comerciales desfacen el hito piloto, teniendo como consecuencia la retención y cobro de penalidades sobre el estado de pago del proyecto. | Abogado Contractual | Media · 0,50 — Gerencia comercial suele dilatar aprobaciones por contingencias de sala | Alto · 0,40 | 0,20 · Alta |
| R-12 | 6 · Regulatorio y externo | Dado que el dictamen del SERNAC de feb-2026 exige que el PPUM en promociones tenga al menos el 50% del tamaño del precio y un mínimo de 0,5 cm mientras BT-8 traslada responsabilidad total al oferente, entonces puede que la plantilla gráfica en etiquetas ESL no cumpla las medidas en ofertas complejas, teniendo como consecuencia el rediseño de layouts gráficos, adquisición de etiquetas de mayor pulgada y riesgo de sanciones legales. | Consultor Legal y Regulatorio | Alta · 0,70 — Dictamen vigente y dos fiscalizaciones ya recibidas en zona sur | Muy alto · 0,80 | 0,56 · Crítica |
| R-13 | 6 · Regulatorio y externo | Dado que la Ley N° 21.719 de Protección de Datos entra en plena vigencia el 01/12/2026 (mes 10\) exigiendo evaluaciones de impacto y BT-8 obliga a cumplir normativa futura, entonces puede que la autoridad o auditoría interna exijan módulos de explicabilidad algorítmica y auditoría EIPD, teniendo como consecuencia la contratación de asesoría legal especializada y desarrollo de módulos de trazabilidad. | Oficial de Cumplimiento TIC | Media · 0,50 — Ley promulgada con fecha cierta; incertidumbre en plazos de fiscalización | Alto · 0,40 | 0,20 · Alta |
| R-14 | 7 · Empresa proveedora | Dado que la cláusula BT-5 compromete 18 salas de ESL al mes 7 bajo precio fijo BA-1 dependiendo de importación internacional de hardware y trámites de Aduana, entonces puede que se produzcan desfases logísticos en el transporte o retención aduanera, teniendo como consecuencia recurrir a fletes de urgencia y riesgo de multas contractuales por atraso en el piloto. | Jefe de Compras / Procurement | Media · 0,50 — Importación sujeta a contingencias de fletes y aforo aduanero | Muy alto · 0,80 | 0,40 · Crítica |
| R-15 | 7 · Empresa proveedora | Dado que el proyecto demanda 13.500 horas de ingeniería con fuerte componente de MLOps y series de tiempo en un mercado laboral altamente competido, entonces puede que se produzca la renuncia o falta de asignación oportuna de ingenieros senior de datos en los primeros meses, teniendo como consecuencia la contratación de staff augmentation externo y sobretiempos de inducción técnica. | Gerente de Operaciones | Alta · 0,70 — Escasez estructural declarada de perfiles especializados de MLOps/Data | Alto · 0,40 | 0,28 · Alta |

s.

# **4 · De dónde sale cada cifra**

## **4.1 · La probabilidad, riesgo por riesgo**

 La probabilidad se justifica con una evidencia.

| ID | Nivel | En qué se apoya |
| :---- | :---- | :---- |
| R-01 | Alta · 0,70 | Es la práctica declarada y habitual en licitaciones TIC sin métricas cuantitativas contractuales de objetar recepciones técnicas. |
| R-02 | Media · 0,50 | Depende del comportamiento estocástico de modelos LLM comerciales de terceros y no hay datos de evaluación previa en sala. |
| R-03 | Muy alta · 0,90 | Hay evidencia explícita en el enunciado de que el motor de promociones opera desde 2013 sin documentación alguna. |
| R-04 | Alta · 0,70 | Es un hecho comprobable que solo dos personas mantienen 620 cajas activas, estando absorbidas por la operación diaria. |
| R-05 | Media · 0,50 | Depende de la voluntad comercial y tarifas de un proveedor externo de WMS con contrato vigente y no alineado al proyecto. |
| R-06 | Alta · 0,70 | Es la situación habitual en cadenas de 62 salas con infraestructura dispar donde no se adjuntó site survey técnico. |
| R-07 | Alta · 0,70 | La restricción de horario nocturno de 4-5 horas y la dispersión entre La Serena y Puerto Montt dificulta el rendimiento de montaje. |
| R-08 | Alta · 0,70 | El caso declara explícitamente que los jefes de 62 salas operan históricamente con planillas Excel propias enviadas por correo. |
| R-09 | Media · 0,50 | Depende del grado de adopción y alfabetización digital de los operarios de sala, factor no evaluado en las bases. |
| R-10 | Alta · 0,70 | La redacción abierta de BA-3 sin tope de horas es la vía habitual utilizada por mandantes para absorber indefiniciones a costo cero. |
| R-11 | Media · 0,50 | Depende de la agilidad del área comercial de Vega Austral para aprobar definiciones en periodos de alta carga operacional. |
| R-12 | Alta · 0,70 | El dictamen del SERNAC rige desde feb-2026 y la empresa ya registra dos fiscalizaciones en la zona sur. |
| R-13 | Media · 0,50 | La Ley 21.719 tiene fecha de vigencia fija al 01/12/2026, pero la exigencia sobre modelos B2B depende de los primeros dictámenes de la Agencia. |
| R-14 | Media · 0,50 | La importación marítima/aérea de hardware ESL depende de tiempos de tránsito internacional y aforo en Aduanas de Chile. |
| R-15 | Alta · 0,70 | Existe una escasez estructural demostrada de ingenieros de datos y MLOps en el mercado nacional frente a la demanda del retail. |

## **4.2 · El impacto en pesos, riesgo por riesgo**

El impacto se compone con los tres sumandos del capítulo 6.2 del enunciado.

| ID | Cómo se compone el impacto | Total |
| ----- | :---- | ----: |
| R-01 | Retrabajo sobre paquetes 4.1 (Feature engineering) y 4.2 (Modelos de pronóstico) (200 h × $34.000 \= $6.800.000) \+ Multas BA-2 por 20 días de desfase en hito Mes 7 (20 días × 10 UF × $40.870 \= $8.174.000) | $ 14.974.000 |
| R-02 | Retrabajo sobre paquetes 5.1 (Capa de consultas gobernadas) y 5.2 (Asistente conversacional) (150 h × $34.000 \= $5.100.000) \+ Sobrecosto en licencias y consumo de API en nube ($4.500.000) | $ 9.600.000 |
| R-03 | Retrabajo sobre paquetes 2.3 (Integración legada) y 3.2 (Motor de promociones) (240 h × $34.000 \= $8.160.000) \+ Multas BA-2 por 20 días de atraso en hito Mes 6 (20 días × 10 UF × $40.870 \= $8.174.000) | $ 16.334.000 |
| R-04 | Retrabajo sobre paquete 2.3 e implementación de middleware desacoplado en paquete libre 2.4 (170 h × $34.000 \= $5.780.000) \+ Servicio externo de pruebas de estrés en 620 cajas ($4.000.000) | $ 9.780.000 |
| R-05 | Retrabajo sobre paquete 2.3 (Integración WMS) para interfaces batch (140 h × $34.000 \= $4.760.000) \+ Consultoría externa de validación de esquemas ($1.200.000) | $ 5.960.000 |
| R-06 | Retrabajo de ingeniería en paquete 6.1 (Nodo de borde en sala) (120 h × $34.000 \= $4.080.000) \+ Adquisición de kit de routers celulares 4G/5G y switches PoE para 18 salas piloto ($7.200.000) | $ 11.280.000 |
| R-07 | Replanificación de cuadrillas y sobretiempos en paquetes 6.2 (Instalación piloto) y 6.3 (Despliegue 62 salas) ($7.500.000) \+ Multas BA-2 por 6 días de desfase (6 días × 10 UF × $40.870 \= $2.452.200) | $ 9.952.200 |
| R-08 | Refuerzo sobre paquetes 1.5 (Gestión del cambio) y 6.4 (Capacitación y acompañamiento en sala) (180 h × $34.000 \= $6.120.000) \+ Consultoría de adopción operacional en terreno ($3.400.000) | $ 9.520.000 |
| R-09 | Retrabajo de simplificación de interfaces UX sobre paquetes 5.2 (Asistente) y 5.3 (Tableros) (140 h × $34.000 \= $4.760.000) | $ 4.760.000 |
| R-10 | Horas no presupuestadas absorbidas sobre paquetes 3.1 (Reglas precio), 4.3 (Reposición) y 5.3 (Tableros) (310 h × $34.000 \= $10.540.000) | $ 10.540.000 |
| R-11 | Retención contractual de 25 días de multas BA-2 por demoras del mandante en validación de BT-9 sobre hito Mes 6 (25 días × 10 UF × $40.870 \= $10.217.500) | $ 10.217.500 |
| R-12 | Retrabajo sobre paquete 3.3 y paquete libre 3.5 (Layouts certificados PPUM) (120 h × $34.000 \= $4.080.000) \+ Compra de mix ESL de mayor tamaño ($6.500.000) \+ Provisión sanción SERNAC ($4.000.000) | $ 14.580.000 |
| R-13 | Activación del paquete libre 1.6 (Gestión de cumplimiento EIPD y privacidad) (150 h × $34.000 \= $5.100.000) \+ Asesoría jurídica externa en Ley 21.719 ($4.500.000) | $ 9.600.000 |
| R-14 | Flete aéreo urgente internacional para asegurar hardware al Mes 5 previo al piloto de Mes 7 en paquete 6.2 ($3.200.000) \+ Multas BA-2 por 28 días (28 × 10 UF × $40.870 \= $11.443.600) | $ 14.643.600 |
| R-15 | Inducción técnica y onboarding sobre paquetes 4.1 y 4.4 (400 h) (80 h × $34.000 \= $2.720.000) \+ Sobretarifa de staff augmentation en MLOps ($6.800.000) | $ 9.520.000 |

## **4.3 · El registro cuantificado**

| ID | Probabilidad | Impacto si ocurre | Valor esperado | Zona |
| :---- | ----- | ----: | ----: | :---: |
| R-01 | 70 % | $ 14.974.000 | $ 10.481.800 | Crítica |
| R-02 | 50 % | $ 9.600.000 | $ 4.800.000 | Alta |
| R-03 | 90 % | $ 16.334.000 | $ 14.700.600 | Crítica |
| R-04 | 70 % | $ 9.780.000 | $ 6.846.000 | Alta |
| R-05 | 50 % | $ 5.960.000 | $ 2.980.000 | Media |
| R-06 | 70 % | $ 11.280.000 | $ 7.896.000 | Alta |
| R-07 | 70 % | $ 9.952.200 | $ 6.966.540 | Alta |
| R-08 | 70 % | $ 9.520.000 | $ 6.664.000 | Alta |
| R-09 | 50 % | $ 4.760.000 | $ 2.380.000 | Media |
| R-10 | 70 % | $ 10.540.000 | $ 7.378.000 | Alta |
| R-11 | 50 % | $ 10.217.500 | $ 5.108.750 | Alta |
| R-12 | 70 % | $ 14.580.000 | $ 10.206.000 | Crítica |
| R-13 | 50 % | $ 9.600.000 | $ 4.800.000 | Alta |
| R-14 | 50 % | $ 14.643.600 | $ 7.321.800 | Crítica |
| R-15 | 70 % | $ 9.520.000 | $ 6.664.000 | Alta |
| Total | — | $ 161.261.300 | $ 105.193.490 | — |

## **4.4 · La cifra que hay que defender**

| Concepto | Valor |
| :---- | ----: |
| Exposición bruta: suma de los impactos si todo ocurriera | $ 161.261.300 |
| Reserva de contingencia: suma de los valores esperados | $ 105.193.490 |
| Reserva como porcentaje de los costos directos de $ 710.000.000 | 14,82 % |
| Reserva según la regla interna del gerente de operaciones, 5% | $ 35.500.000 |
| Brecha entre la costumbre y el cálculo | $ 69.693.490 (+196,3 %) |

*Argumentación técnica ante el Gerente de Operaciones: «La regla tradicional del 5% ($35.500.000) no constituye una decisión técnica informada sino una costumbre inercial que dejaría a nuestra empresa con un déficit de cobertura de $69.693.490 frente al valor esperado real de los riesgos cuantificados ($105.193.490, un 14,82% de los costos directos). Aceptar a ciegas ese 5% comprometería el 75,7% de nuestra utilidad esperada ($92.016.000) ante la materialización de riesgos críticos como la opacidad del motor Oracle 2013 o las sanciones del PPUM. Sin embargo, no trasladamos este 14,82% al cliente: mediante la gestión preventiva en la etapa de propuesta (consultas formales, supuestos de precisión WMAPE, blindaje contractual de cambios menores y rediseño de hardware ESL), eliminamos $66.896.740 en valor esperado invirtiendo solo $16.500.000 en mitigaciones directas, reduciendo la reserva residual final a $38.296.750 (5,39% de los costos directos). De este modo, defendemos una oferta altamente competitiva de $917.071.150 (93,6% del presupuesto del cliente) con un margen protegido y sin pasivos ocultos.»*

# **5 · El orden y los ocho de mayor exposición**

Ordenados por exposición, con la regla de desempate del capítulo 6.4 del enunciado.

| Lugar | ID | Exposición | Valor esperado | Zona | Observación |
| :---: | :---- | ----- | ----: | :---: | :---- |
| 1 | R-03 | 0,72 | $ 14.700.600 | Crítica | Se cambia el diseño para que el riesgo deje de existir, o se elimina la causa en la propuesta. |
| 2 | R-01 | 0,56 | $ 10.481.800 | Crítica | Se cambia el diseño para que el riesgo deje de existir, fijando métrica WMAPE en propuesta. |
| 3 | R-12 | 0,56 | $ 10.206.000 | Crítica | Se cambia el diseño de hardware/plantillas ESL para cumplir dictamen SERNAC en propuesta. |
| 4 | R-14 | 0,40 | $ 7.321.800 | Crítica | Acción de mitigación logística y anticipación de órdenes de compra con costo y plazo en el plan. |
| 5 | R-06 | 0,28 | $ 7.896.000 | Alta | Acción de mitigación con costo y plazo dentro del plan de trabajo (routers 4G y switches PoE). |
| 6 | R-10 | 0,28 | $ 7.378.000 | Alta | Acción de mitigación contractual acotando cambios menores a 16 h en la propuesta. |
| 7 | R-07 | 0,28 | $ 6.966.540 | Alta | Acción de mitigación con logística descentralizada y premontaje diurno de rieles. |
| 8 | R-04 | 0,28 | $ 6.846.000 | Alta | Acción de mitigación mediante SDK/API emuladora en .NET desacoplada. |
| 9 | R-08 | 0,28 | $ 6.664.000 | Alta | Acción de mitigación con plan de adopción, refuerzo presencial y capacitación en sala. |
| 10 | R-15 | 0,28 | $ 6.664.000 | Alta | Acción de mitigación con staff augmentation temprano y plan de retención de talentos. |
| 11 | R-11 | 0,20 | $ 5.108.750 | Alta | Acción de mitigación contractual con cláusula de suspensión de plazos ante demoras del cliente. |
| 12 | R-13 | 0,20 | $ 4.800.000 | Alta | Acción de mitigación incorporando evaluación de impacto EIPD y logs de auditoría. |
| 13 | R-02 | 0,20 | $ 4.800.000 | Alta | Acción de mitigación rediseñando arquitectura RAG determinista para el asistente C5. |
| 14 | R-05 | 0,10 | $ 2.980.000 | Media | Se acepta activamente: reserva de contingencia y disparador definido para interfaz batch. |
| 15 | R-09 | 0,10 | $ 2.380.000 | Media | Se acepta activamente: reserva de contingencia y disparador para simplificación UX. |

# **6 · Respuestas con etapa declarada**

Ocho respuestas para los ocho riesgos de mayor exposición, más las siete restantes en forma abreviada.

## **6.1 · Los ocho de mayor exposición**

| ID | Estrategia | Acción concreta | Dueño | Costo $ | Disparador | Etapa |
| ----- | :---- | :---- | :---- | ----- | :---- | ----- |
| R-03 | Evitar / Mitigar | Formular consulta en Mes 1 y activar paquete libre 2.4 (Adaptador y middleware de integración desacoplado) en sustitución de PL/SQL legado, blindando la ruta crítica (paquetes 2.3 y 3.2) hacia el hito Mes 6\. | Arquitecto de Integración | $ 0 | Falta de diccionario de datos Oracle en acta de respuestas de Mes 1\. | Propuesta |
| R-01 | Evitar / Alcance | Establecer en anexo de Mes 1 la cláusula de aceptación con umbrales WMAPE \<= 22% por categoría y \<= 30% por SKU en paquetes 4.1 y 4.2, protegiendo el hito Mes 7 en la ruta crítica. | Especialista MLOps | $ 0 | Observaciones del mandante a la precisión del modelo al cierre de Mes 1\. | Propuesta |
| R-12 | Mitigar / EDT | Activar paquete libre 3.5 (Renderizador y layouts certificados de PPUM) e incorporar mix de hardware ESL 4,2" en paquete 6.1, asegurando el cumplimiento del dictamen SERNAC en el hito Mes 6 (paquetes 3.1 y 3.3). | Consultor Legal y Regulatorio | $ 4.200.000 | Discrepancias visuales en pruebas de rotulación PPUM en Mes 2\. | Implementación |
| R-14 | Mitigar / Logística | Emitir orden de compra internacional de ESL en la semana 1 posfirma (Mes 1\) con entrega garantizada en bodega Santiago al Mes 4 y buffer local del 15%, blindando la ruta crítica del paquete 6.2 hacia el hito Mes 7\. | Jefe de Compras / Procurement | $ 3.500.000 | Alerta de retraso de embarque \>10 días del fabricante en Mes 2\. | Propuesta |
| R-06 | Mitigar / Borde | Suministrar en paquete 6.1 un kit de 2 routers celulares 4G/5G con switch PoE integrado por sala piloto y caché local en nodo de borde, desacoplando la ruta crítica (6.1 y 6.2) de la red BT-6 para el hito Mes 7\. | Jefe de Despliegue en Terreno | $ 3.800.000 | Latencia \>300 ms o pérdida de paquetes \>2% en Site Survey de Mes 3\. | Implementación |
| R-10 | Evitar / Contrato | Incorporar en el contrato de Mes 1 la definición de «cambio menor» acotada a máximo 16 h por requerimiento y 80 h acumuladas en paquete 1.1, exigiendo Change Request formal para excesos sobre paquetes 3.1 y 5.3. | Gerente de Contratos y Oferta | $ 0 | Solicitud de cambio que supere 16 h de desarrollo en Mes 3\. | Propuesta |
| R-07 | Evitar / Plan | Fijar en contrato de Mes 1 el calendario de congelamiento comercial (blackout) y organizar en paquete 6.3 cuadrillas en 3 nodos con premontaje diurno y montaje nocturno, protegiendo el hito Mes 12\. | Jefe de Despliegue en Terreno | $ 0 | Restricción de acceso nocturno a salas en el plan de Mes 2\. | Propuesta |
| R-04 | Mitigar / Arquitectura | Desarrollar en paquete libre 2.4 una API REST ligera en .NET con emulador de transacciones de caja, desacoplando el desarrollo del POS Caja 7 y protegiendo la ruta crítica del paquete 2.3 hacia el hito Mes 6\. | Líder de Integración | $ 5.000.000 | Demora \>10 días en la entrega de endpoints por mantenedores de Caja 7 en Mes 2\. | Implementación |

## **6.2 · Las siete restantes, en breve**

| ID | Acción | Costo | Etapa |
| ----- | :---- | ----: | ----- |
| R-08 | Implementar programa de adopción operacional en paquete 1.5 y talleres en sala en paquete 6.4 con monitores líderes y bonificación ligada a reducción de quiebres hacia el hito Mes 12\. | $ 0 | Implementación |
| R-15 | Suscribir acuerdo marco de staff augmentation preferente en Mes 1 y fijar bono de permanencia a ingenieros clave sobre paquetes 4.1 y 4.4 previo al hito Mes 10\. | $ 0 | Propuesta |
| R-11 | Incluir en contrato de Mes 1 cláusula de suspensión automática de plazos y exención de multas BA-2 ante demoras del mandante \>5 días en validaciones de BT-9. | $ 0 | Propuesta |
| R-13 | Activar paquete libre 1.6 (Gestión transversal de cumplimiento y privacidad EIPD / ANCI) y registrar actividades de tratamiento en capa transversal previo a Mes 10\. | $ 0 | Propuesta |
| R-02 | Implementar en paquete 5.1 arquitectura RAG determinista con capa intermedia de consultas SQL gobernadas y límite de tokens previo al hito Mes 10\. | $ 0 | Implementación |
| R-05 | Diseñar en paquete 2.3 interfaces desacopladas mediante SFTP/archivos planos CSV con validación de esquemas para el WMS de CD previo a Mes 4\. | $ 0 | Implementación |
| R-09 | Diseñar en paquete 5.2 interfaz móvil simplificada con botones de un toque («quiebre hoy», «merma ayer») para jefes de sala hacia el hito Mes 10\. | $ 0 | Implantación |

## **6.3 · Distribución por etapa**

| Etapa | Acciones | Lectura |
| ----- | ----- | :---- |
| Propuesta | 9 acciones (60,0 %)\[R-01, R-03, R-04, R-06, R-07, R-10, R-11, R-12, R-13\] | Concentración masiva de respuestas preventivas a costo cero o de bajo impacto antes de firmar el contrato, neutralizando las cláusulas ambiguas. |
| Implementación | 5 acciones (33,3 %)\[R-02, R-05, R-08, R-14, R-15\] | Mitigaciones tempranas de ingeniería, logística de abastecimiento y gestión del cambio ejecutadas durante la construcción del software. |
| Implantación | 1 acción (6,7 %)\[R-09\] | Acompañamiento ergonómico y usabilidad en sala durante la puesta en marcha del piloto. |
| Operación | 0 acciones (0,0 %) | Ninguna acción se posterga a la fase de operación, evitando un plan de reparaciones reactivas tardías y costosas. |

.

# **7 · Consulta, supuesto y exclusión de referencia**

## **Consulta · origen R-03, cláusula BT-1**

| *«Respecto a la cláusula BT-1 y la integración con el motor de promociones Oracle construido en 2013 (Capítulo 2.1 del caso): Se solicita al mandante confirmar si pondrá a disposición del oferente adjudicado, dentro de los primeros 15 días posteriores a la firma del contrato, el diccionario de datos completo, el modelo entidad-relación y los scripts fuente de los stored procedures y paquetes PL/SQL que rigen las promociones vigentes. Decisión que depende de la respuesta: En caso de no contar con dicha documentación técnica, nuestra oferta contempla la sustitución funcional de las reglas mediante un microservicio moderno de cálculo desacoplado provisto por nuestra empresa, requiriendo únicamente la extracción de tablas maestras sin realizar ingeniería inversa sobre la base de datos Oracle legada.» (Origen: R-03, Cláusula BT-1)* |
| :---- |

## **Supuesto · origen R-01, cláusula BT-3, para el caso de que la consulta no se responda**

| *«Respecto a la cláusula BT-3 sobre la precisión del motor de pronóstico (C1): La oferta asume formalmente como criterio de recepción y aceptación técnica un error porcentual absoluto medio ponderado (WMAPE) no superior al 22% a nivel de categoría-sala y no superior al 30% a nivel de SKU individual para las categorías de alta rotación (tipo A y B), calculado sobre series históricas de ventas que hayan sido previamente saneadas de quiebres de góndola documentados. Si durante las pruebas de homologación el mandante exige umbrales de precisión más estrictos o calibraciones para el 100% de los 38.000 SKU incluyendo productos de rotación esporádica (cola larga), los trabajos de reentrenamiento y feature engineering adicionales se considerarán cambios de alcance fuera del contrato base y se valorizarán a la tarifa acordada de $34.000 por hora.» (Origen: R-01, Cláusula BT-3)* |
| :---- |

## **Exclusión · origen R-06, cláusula BT-6**

| *«Respecto a la cláusula BT-6 sobre la infraestructura de red en las 62 salas: Se excluyen expresamente del alcance de la oferta las obras civiles de cableado estructurado, canalizaciones eléctricas en sala de ventas, provisión de acometidas de energía en cielo falso y el reemplazo de switches de distribución interna de las tiendas de Vega Austral. La oferta suministra únicamente las pasarelas RF de borde para las etiquetas ESL y routers celulares 4G/5G dedicados con conectividad IoT independiente para las 18 salas del piloto. Razón técnica: La adecuación física de redes y canalizaciones eléctricas locales es responsabilidad patrimonial del mandante. Vía de incorporación: En caso de requerir que nuestro equipo ejecute el cableado y certificación PoE en tienda, el mandante podrá contratar dicho servicio a través del Catálogo de Obras Civiles Opcionales valorizado en el Anexo Económico N° 4 a razón de $1.850.000 netos por sala.» (Origen: R-06, Cláusula BT-6)* |
| :---- |

# **8 · Matriz de riesgo a solución**

Los cinco de mayor exposición. Ésta es la tabla que decide la nota de la Parte B.

| Riesgo | Alcance | Requisitos | Arquitectura | Plan y EDT | Precio |
| ----- | :---- | :---- | :---- | :---- | ----- |
| R-03 (Motor Oracle) | Se explicita que el alcance contempla la sustitución de la lógica legacy mediante un microservicio desacoplado de promociones (C3). | RF: Exportación batch de reglas y catálogo de promociones desde Oracle. RNF: Tiempo de respuesta del cálculo de promociones \< 100 ms en cajas. | Capa Servicios de Negocio: Microservicio de promociones en contenedores desacoplado de la BD Oracle. Capa Integración: Adaptador asíncrono. | Se activa paquete libre 2.4 (Adaptador y middleware de integración desacoplado) y se añade hito «H-2.4: Validación de microservicio de promociones» en Mes 3, protegiendo ruta crítica (2.3 y 3.2). | $ 0 |
| R-01 (Precisión Pronóstico) | El alcance delimita la precisión contractual del modelo C1 al surtido base (categorías A y B) con series históricas depuradas. | RNF: Criterio formal de aceptación fijado en WMAPE \<= 22% a nivel categoría-sala y \<= 30% por SKU en 21 días. | Capa Modelos: Pipeline MLOps con monitoreo automatizado de data drift y reentrenamiento quincenal sobre zona conformada de datos. | Se ajustan paquetes 4.1 y 4.2 y se incorpora el hito «H-4.2: Homologación matemática de pronóstico» en Mes 5, protegiendo la ruta crítica hacia el hito Mes 7\. | $ 0 |
| R-12 (PPUM SERNAC) | Se amplía el alcance de hardware para incluir etiquetas electrónicas e-ink de 4,2" en cabeceras de góndola y promociones complejas. | RF: Cálculo centralizado de PPUM en única fuente de verdad. RNF: Carácter PPUM \>= 50% de precio venta y altura física \>= 0,5 cm en pantalla. | Capa Servicios de Negocio: Cálculo de PPUM en motor central (no en etiqueta). Capa Experiencia: Módulo de renderizado dinámico e-ink. | Se activa paquete libre 3.5 (Renderizador y layouts certificados de PPUM) con 120 h de ingeniería y se fija hito «Certificación visual SERNAC» en Mes 2, blindando paquetes 3.1 y 3.3. | \+ $ 4.200.000 |
| R-14 (Cadena ESL) | Se incluye en el alcance la gestión de importación anticipada y almacenamiento de buffer local del 15% de hardware ESL en Santiago. | RNF: SLA de entrega de hardware en bodega central Santiago al Mes 4 (2 meses antes del hito Mes 7). | Vista Física: Pasarelas RF duales de borde compatibles con protocolo estándar de mercado y firmware homologado. | Se adelanta en el cronograma el hito «Emisión de Orden de Compra Internacional de Hardware» a la semana 1 posfirma (Mes 1), protegiendo la ruta crítica del paquete 6.2 hacia Mes 7\. | \+ $ 3.500.000 |
| R-06 (Red Salas BT-6) | El alcance incorpora provisión de 2 routers celulares 4G/5G con switch PoE integrado por sala en el piloto de 18 locales. | RNF: Enlace VPN IPsec redundante independiente de la LAN corporativa de tienda con failover automático \< 5 s. | Vista Física \- Nodo de Borde en Sala: Caché local de precios en nodo de borde y túnel cifrado sobre enlace móvil 4G/5G dedicado. | Se refuerza paquete 6.1 (+120 h) y se añade hito «Site Survey y certificación de enlace celular en 18 salas» en Mes 4, blindando paquetes 6.1 y 6.2 hacia el hito Mes 7\. | \+ $ 3.800.000 |

# **9 · Recálculo**

| Qué entra y qué no entra Regla del recálculo, declarada en el capítulo 8.5 del enunciado: la reserva se recalcula sólo con las respuestas de las zonas crítica y alta, que son las que la regla de zona obliga a mitigar. Los riesgos de zona media se aceptan activamente y su valor esperado se queda en la reserva: para eso está la reserva.  |
| :---- |

## **9.1 · Retorno de la respuesta**

| ID   |   VE inicial | VE residual |       Ahorro | Costo de la acción | Retorno  |
| ---- | -----------: | ----------: | -----------: | -----------------: | :------: |
| R-03 | $ 14.700.600 |   $ 600.000 | $ 14.100.600 |                $ 0 | Infinito |
| R-01 | $ 10.481.800 |   $ 300.000 | $ 10.181.800 |                $ 0 | Infinito |
| R-12 | $ 10.206.000 |   $ 500.000 |  $ 9.706.000 |        $ 4.200.000 |   2,31   |
| R-14 |  $ 7.321.800 |   $ 900.000 |  $ 6.421.800 |        $ 3.500.000 |   1,83   |
| R-06 |  $ 7.896.000 |   $ 750.000 |  $ 7.146.000 |        $ 3.800.000 |   1,88   |
| R-10 |  $ 7.378.000 |   $ 200.000 |  $ 7.178.000 |                $ 0 | Infinito |
| R-07 |  $ 6.966.540 |   $ 900.000 |  $ 6.066.540 |        $ 2.800.000 |   2,17   |
| R-04 |  $ 6.846.000 |   $ 750.000 |  $ 6.096.000 |        $ 2.200.000 |   2,77   |

## **9.2 · La reserva después de gestionar**

| Concepto | Valor |
| :---- | ----: |
| Reserva bruta, antes de responder | $ 105.193.490 |
| Valor esperado eliminado por las respuestas | $ 66.896.740 |
| Reserva residual | $ 38.296.750 (5,39 % de los costos directos base) |

## **9.3 · La oferta gestionada**

| Concepto | Monto |
| :---- | ----: |
| Costos directos, con las acciones de respuesta incorporadas | $ 726.500.000 |
| Gastos generales, 8% | $ 58.120.000 |
| Utilidad, 12% | $ 94.154.400 |
| Reserva residual | $ 38.296.750 |
| Oferta neta gestionada | $ 917.071.150 |
| Oferta neta sin gestionar el riesgo (costumbre 5%) | $ 894.316.000 |
| Diferencia frente a oferta con 5% ciego | \+ $ 22.755.150 (+ 2,54 %) |

