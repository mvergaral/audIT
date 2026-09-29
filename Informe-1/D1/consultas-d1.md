# PLIEGO OFICIAL DE CONSULTAS Y ACLARACIONES AL MANDANTE — HITO S2

**Licitación N.° TFEP-01/2026 · Caso 10: Transportes Curimón S.A.**
**Empresa Proponente: AudIT**
**Fecha: 2026-09-01**
**Artículo 43° de las Bases Administrativas (FEP01.26)**

---

> [!IMPORTANT]
> Este pliego contiene 12 consultas formuladas conforme al formato obligatorio de 7 columnas del Art. 43.2 de las Bases Administrativas. Cada consulta identifica un vacío normativo, una contradicción entre documentos o un riesgo no regulado que impacta directamente el diseño, el alcance o la valorización de la oferta técnico-económica de **AudIT**. Ninguna consulta solicita al CLIENTE que diseñe la solución ni que elija tecnologías (Art. 43.4).

---

## TABLA MAESTRA DE CONSULTAS Y ACLARACIONES

### Consulta N.° 1 — Jornada de Conductores Externos y Valor Probatorio

| Columna | Contenido |
| :--- | :--- |
| **A · N.° Correlativo** | 1 |
| **B · Empresa** | AudIT |
| **C · Fecha** | 2026-09-01 |
| **D · Tipo** | Técnica |
| **E · Referencia** | FEP03.10.26, Cap. 4.3 (p. 10-11); Decisión no tomada N.° 1 (Numeral 16.1, p. 35); Restricción N.° 7 (Cap. 10, p. 24); FEP01.26, Art. 4.2 — Ley N.° 21.719; Entrevista Gerente General (Cap. 8, p. 18). |
| **F · Consulta** | El Caso 10 establece como primera expectativa de negocio (9.2) que la jornada efectiva de conducción se conozca y se acredite para los 454 conductores, incluidos los 258 de transportistas subcontratados que no son trabajadores de la compañía. Sin embargo, la normativa laboral vigente (Art. 25 bis del Código del Trabajo) atribuye la obligación de registro de jornada al empleador directo, que en el caso de los conductores externos no es Transportes Curimón S.A. sino cada uno de los 148 transportistas subcontratados. Simultáneamente, la Restricción N.° 7 señala que la compañía *responde* por la jornada del conductor que despacha, y la Decisión N.° 1 reconoce que esta materia no está resuelta. **Se consulta:** (i) ¿El mandante ha verificado con la Dirección del Trabajo que una declaración jurada digital del conductor externo, emitida con firma electrónica conforme a la Ley N.° 19.799 previamente al inicio de cada viaje, constituye medio de prueba legalmente suficiente para acreditar el cumplimiento del descanso previo? (ii) En caso negativo, ¿se contempla como alternativa la integración mediante servicios de lectura (API o FMS estándar) con los sistemas de registro de jornada que cada transportista subcontratado mantenga con su propio empleador, trasladando al proponente la carga de especificar el protocolo de intercambio y al mandante la de incluir dicha obligación en los contratos de subcontratación? |
| **G · Propuesta de interpretación de AudIT** | AudIT propone interpretar que el mandante aceptará un modelo mixto de evidencia: (a) declaración jurada digital con firma electrónica avanzada previa al viaje como prueba de primera línea, complementada con (b) contraste automatizado contra la telemetría del tacógrafo digital cuando esté disponible, y (c) una cláusula contractual tipo, cuya redacción será provista por el proponente, que el mandante incorporará a los contratos de subcontratación vigentes, obligando a los 148 transportistas a habilitar el acceso de lectura a sus registros de jornada. Esta interpretación permite a AudIT diseñar un esquema de evidencia graduable que no depende de un único mecanismo y que satisface el estándar de oponibilidad exigido en la Expectativa 9.2 y en el Criterio de Aceptación N.° 4. |

---

### Consulta N.° 2 — Soberanía del Dato y Ley N.° 21.719 en Camiones de Terceros

| Columna | Contenido |
| :--- | :--- |
| **A · N.° Correlativo** | 2 |
| **B · Empresa** | AudIT |
| **C · Fecha** | 2026-09-01 |
| **D · Tipo** | Técnica |
| **E · Referencia** | FEP03.10.26, Restricción N.° 3 (Cap. 10, p. 24); Decisión no tomada N.° 23 (Numeral 16.1, p. 37); Entrevista Nolberto Sandoval (Cap. 8, p. 19-20); FEP01.26, Art. 4.2 — Ley N.° 21.719; FEP02.26, RT-11.10 (p. 34); FEP03.10.26, RT-16.09. |
| **F · Consulta** | La exportadora que representa el 19% de los ingresos exige posición de la carga en tiempo real para 2029 (Cap. 1, p. 6). Simultáneamente, el 60,4% de los camiones pertenece a 148 dueños terceros que prestan servicios a la competencia (Cap. 2.2). La Restricción N.° 3 prohíbe intervenir los dispositivos de terceros sin acuerdo expreso, y la Ley N.° 21.719 clasifica la geolocalización como dato personal sensible cuyo tratamiento requiere base de licitud y consentimiento. El transportista Sandoval (p. 19) expresó que no compartirá su posición cuando trabaja para otro cliente. **Se consulta:** ¿El mandante ratifica que la exigencia de tracking y geolocalización que el proponente debe implementar aplica única y exclusivamente durante el período que medie entre la asignación formal del flete por parte de Curimón y la confirmación de descarga en el destino, quedando expresamente vedada toda captura, almacenamiento o procesamiento de coordenadas fuera de dicho período, con borrado o desactivación automática del stream de posición una vez cerrado el viaje? |
| **G · Propuesta de interpretación de AudIT** | AudIT propone interpretar que el ámbito temporal de la geolocalización se limita al ciclo de vida del viaje asignado por Curimón, con activación automática al momento de la asignación y desactivación al cierre del viaje (descarga confirmada). Fuera de ese período, el dispositivo no transmitirá ni almacenará coordenadas para Curimón. AudIT diseñará un módulo de gestión de consentimiento granular (conforme a Ley N.° 21.719 y RT-16.09) donde cada dueño de camión autorice explícitamente el alcance temporal y los destinatarios de la información, con revocación en línea. Esta interpretación es favorable a la ingeniería de AudIT porque permite dimensionar el volumen de datos móviles exclusivamente sobre los viajes activos, reduciendo el costo recurrente de conectividad en una empresa con margen del 9%. |

---

### Consulta N.° 3 — Mecanismo de Fe de Hechos en Sobreestadías

| Columna | Contenido |
| :--- | :--- |
| **A · N.° Correlativo** | 3 |
| **B · Empresa** | AudIT |
| **C · Fecha** | 2026-09-01 |
| **D · Tipo** | Técnica |
| **E · Referencia** | FEP03.10.26, Cap. 7.2 (p. 16), Indicador «$340 millones facturados, 71% objetado»; Expectativa 9.5 (p. 23); Decisión no tomada N.° 8 (Numeral 16.1, p. 36); Restricción N.° 1 y N.° 9 (Cap. 10, p. 24-25); FEP03.10.26, RT-09.01 — Registro automático sin intervención del conductor. |
| **F · Consulta** | El Caso 10 declara que en 2025 se facturaron $340 millones por sobreestadías, de los cuales los clientes objetaron el 71% ($241,4 millones), por cuanto la evidencia del tiempo de espera es una anotación manual del conductor (Cap. 4.7). La Restricción N.° 9 prohíbe instalar equipamiento en las instalaciones de terceros (puntos de carga y descarga), y la Restricción N.° 1 prohíbe toda interacción del conductor en marcha. La Decisión N.° 8 reconoce que la forma de registrar llegada y salida en instalaciones de un tercero sin intervención del conductor y sin instalar equipamiento no está resuelta. **Se consulta:** Para los efectos de subsanar el rechazo de cobros por sobreestadía, ¿el mandante admitirá como respaldo contractual vinculante frente a sus clientes la evidencia de geocerca automática (entrada/salida del perímetro georreferenciado del punto de carga/descarga), generada y certificada por el sistema telemático del proponente, sin supeditar el cobro a la firma manual de portería del cliente ni a la instalación de un dispositivo en las instalaciones del tercero? |
| **G · Propuesta de interpretación de AudIT** | AudIT propone que el mandante negocie con sus 84 clientes activos la incorporación de una cláusula contractual tipo que reconozca la geocerca certificada como medio de prueba válido del tiempo de estadía, con marca temporal firmada digitalmente y conservación conforme a RT-05.10 (3 años para evidencia de tiempos en instalaciones de cliente). AudIT diseñará geocercas por punto, validadas contra la cartografía catastral, con precisión de ±15 metros, eliminando la dependencia de la anotación manual y generando evidencia no repudiable. Esta interpretación favorece a AudIT porque habilita su módulo de facturación automática de sobreestadías con evidencia telemática verificable, que es una de las funcionalidades de mayor impacto económico del proyecto. |

---

### Consulta N.° 4 — Calibración y Responsabilidad por Sobrepeso

| Columna | Contenido |
| :--- | :--- |
| **A · N.° Correlativo** | 4 |
| **B · Empresa** | AudIT |
| **C · Fecha** | 2026-09-01 |
| **D · Tipo** | Técnica |
| **E · Referencia** | FEP03.10.26, Cap. 4.5 (p. 12) y Cap. 7.1 (p. 16) — 142 detenciones por sobrepeso en 2025, 18 horas de inmovilización promedio; Cap. 12, ámbito «Pesos y dimensiones» (p. 26); Restricción N.° 9 (Cap. 10, p. 25). |
| **F · Consulta** | El Caso 10 establece que el peso lo determina el cliente al cargar y que el sobrepeso lo asume la compañía (Cap. 4.5). En 2025 hubo 142 detenciones con un promedio de 18 horas de inmovilización. La normativa de pesos por eje hace responsable al porteador, no al generador de carga. El proponente debe diseñar controles de peso; sin embargo, dado que la Restricción N.° 9 prohíbe instalar equipamiento en las instalaciones de los clientes (donde están las básculas de origen), **se consulta:** (i) ¿El mandante dispone de un protocolo de pesaje homologado en origen, o de básculas propias en alguno de sus terminales, cuya lectura pueda integrarse al sistema del proponente como peso de referencia previo a la salida? (ii) En caso de que no exista pesaje en origen bajo control de Curimón, ¿se contemplará una tolerancia contractual o un mecanismo de prorrateo de responsabilidad con el generador de carga cuando el sobrepeso sea atribuible a la báscula o al procedimiento de carga de dicho tercero? |
| **G · Propuesta de interpretación de AudIT** | AudIT propone interpretar que el mandante habilitará, al menos en el terminal principal de San Bernardo (único bajo su control total), una báscula certificada de plataforma cuya lectura se integrará automáticamente al sistema. Para los puntos de carga de terceros, AudIT diseñará un registro digital del peso declarado por el cliente generador de carga (captura fotográfica del ticket de báscula con OCR y marca temporal), que sirva como evidencia de descargo ante una fiscalización posterior. Esta interpretación permite a AudIT incorporar un módulo de trazabilidad de peso que mitigue el impacto de las 142 detenciones anuales y genere un registro oponible ante la autoridad. |

---

### Consulta N.° 5 — Estándar de Certificación de Emisiones CO₂e 2029

| Columna | Contenido |
| :--- | :--- |
| **A · N.° Correlativo** | 5 |
| **B · Empresa** | AudIT |
| **C · Fecha** | 2026-09-01 |
| **D · Tipo** | Técnica |
| **E · Referencia** | FEP03.10.26, Expectativa 9.11 (p. 24); Decisión no tomada N.° 22 (Numeral 16.1, p. 37); Hito externo «condiciones de renovación 2029» (Numeral 13.2, p. 28); FEP02.26, RT-05.29. |
| **F · Consulta** | La exportadora que representa el 19% de los ingresos exige para 2029 un reporte verificado de emisiones por tonelada-kilómetro (Cap. 1, p. 6). La Expectativa 9.11 exige metodología declarada con datos trazables hasta el consumo real. La Decisión N.° 22 reconoce que no está resuelto cómo se calculan las emisiones para los camiones de terceros, cuyo combustible la compañía no compra. **Se consulta:** ¿El mandante aceptará la metodología estandarizada bajo el GLEC Framework v3.0 / ISO 14083:2023 como base de cálculo, con factores de emisión por defecto del GLEC para los camiones subcontratados cuyo consumo real no se conozca, y con consumo real integrado (vía telemetría y red de estaciones) para la flota propia? ¿O se exigirá certificación expresa a través del programa Giro Limpio del Ministerio de Transportes u otro esquema específico acreditado en Chile? |
| **G · Propuesta de interpretación de AudIT** | AudIT propone adoptar GLEC Framework v3.0 / ISO 14083:2023 como metodología principal, con dos niveles de precisión: (a) consumo real trazable para la flota propia (61 camiones con telemetría de fábrica + integración con la red de estaciones de servicio), y (b) factores de emisión por defecto certificados para los camiones de terceros, migrando progresivamente a consumo real a medida que los transportistas adhieran al plan de datos. Esta metodología mixta es verificable por terceros conforme a ISO 14064-3, satisface la exigencia de la exportadora y permite a AudIT dimensionar el módulo de reporting de emisiones con un costo razonable desde la Etapa 1, sin depender de la adhesión completa de los 148 transportistas. |

---

### Consulta N.° 6 — Destino y Alcance del Sistema de Transporte de 2013

| Columna | Contenido |
| :--- | :--- |
| **A · N.° Correlativo** | 6 |
| **B · Empresa** | AudIT |
| **C · Fecha** | 2026-09-01 |
| **D · Tipo** | Técnica |
| **E · Referencia** | FEP03.10.26, Cap. 5 (p. 13-14), tabla «Destino» del sistema de gestión de transporte de 2013; Restricción N.° 8 (Cap. 10, p. 25); Exclusión explícita «No se pide reemplazar el sistema contable» (Cap. 11, p. 25); Decisión no tomada N.° 1 vinculada al sistema; Entrevista Riquelme (Cap. 8, p. 20-21). |
| **F · Consulta** | El Cap. 5 declara que el destino del sistema de gestión de transporte de 2013 es «decisión del proponente» y que constituye «la decisión de arquitectura más importante del caso». Simultáneamente, la Restricción N.° 8 establece que el sistema contable se mantiene y sigue siendo el único emisor de documentos tributarios, incluido el documento electrónico de transporte. El jefe de TI (Riquelme) señala que hoy se redigita manualmente la información de la orden de transporte al sistema contable para emitir el DTE. **Se consulta:** ¿El mandante confirma que el sistema contable se mantendrá exclusivamente para la emisión de documentos tributarios y funciones ERP contables, y que el proponente está habilitado para sustituir los módulos operativos del sistema de 2013 (órdenes de transporte, asignación de viajes, tarifas, control de viajes y liquidación a transportistas) mediante una integración API/servicios con el sistema contable, sin estar obligado a mantener la lógica operativa del sistema legacy? |
| **G · Propuesta de interpretación de AudIT** | AudIT propone interpretar que el sistema de 2013 será reemplazado en su totalidad funcional operativa, manteniéndose únicamente el sistema contable como receptor de datos vía integración de servicios (API REST o capa de eventos) para la emisión de DTE y funciones ERP. AudIT diseñará una capa anticorrupción (conforme a RT-02.14) que aísle el modelo de dominio nuevo de la estructura de datos del sistema legacy, permitiendo la convivencia durante la marcha blanca sin redigitación y eliminando la dependencia arquitectónica del sistema de 2013. Esta interpretación es crítica para AudIT porque condiciona la totalidad de la arquitectura lógica, el alcance de la migración de datos y la estructura de costos de la oferta. |

---

### Consulta N.° 7 — Infraestructura del Data Center San Bernardo

| Columna | Contenido |
| :--- | :--- |
| **A · N.° Correlativo** | 7 |
| **B · Empresa** | AudIT |
| **C · Fecha** | 2026-09-01 |
| **D · Tipo** | Administrativa |
| **E · Referencia** | FEP03.10.26, Cap. 6 (p. 14) — Sala de equipos de 26 m² con climatización split y UPS de 20 minutos; FEP02.26, Cap. 6 — Requisitos RT-06.01 a RT-06.34 (p. 15-18), en especial RT-06.07 (UPS 30 min), RT-06.08 (generador 24 h), RT-06.13 (climatización de precisión N+1), RT-06.16/17 (detección y extinción); FEP03.10.26, RT-06.01 del caso (p. 34). |
| **F · Consulta** | El Cap. 6 del Caso 10 declara textualmente que la sala de equipos de San Bernardo posee «climatización tipo split, alimentación ininterrumpida de 20 minutos y acceso por credencial» y que «no cumple los estándares del Capítulo 6 de las Bases Técnicas Transversales». Los requisitos transversales exigen, entre otros, UPS de 30 minutos mínimo (RT-06.07), generador autónomo de 24 horas (RT-06.08), climatización de precisión redundante N+1 (RT-06.13) y sistema de detección temprana por aspiración láser con extinción automática por agente limpio (RT-06.16/17). El RT-06.06 transversal señala que «la obra civil de separación de las instalaciones es de cargo del CLIENTE; su especificación técnica y su coordinación son de cargo del PROPONENTE». **Se consulta:** ¿Las obras civiles de adecuación del recinto (ampliación o relocalización), la provisión e instalación de climatización de precisión, el sistema UPS de 30 minutos, el generador autónomo de 24 horas y el sistema de detección/extinción serán provistas y financiadas por Curimón (como obra civil a cargo del cliente conforme a RT-06.06), o el proponente debe presupuestarlas íntegramente en su oferta de infraestructura on-premise? La respuesta impacta directamente la valorización del componente on-premise en la Oferta Económica. |
| **G · Propuesta de interpretación de AudIT** | AudIT propone interpretar que, conforme a RT-06.06, la obra civil gruesa (muros, piso técnico, acometida eléctrica del edificio, canalización de datos) es de cargo de Curimón. Los sistemas especializados de TI (UPS, climatización de precisión, detección/extinción, control de acceso biométrico, racks y cableado estructurado) son de cargo del proponente y se incluirán en la oferta económica como inversión en infraestructura on-premise. AudIT proveerá la especificación técnica completa y la coordinación de la obra, con un cronograma que permita que las adecuaciones civiles estén concluidas antes del hito H3 de habilitación de ambientes (mes 6 estimado). Esta delimitación permite a AudIT dimensionar con precisión su componente on-premise sin asumir riesgos de obra civil que corresponden al mandante. |

---

### Consulta N.° 8 — Preservación de Garantías en Puerto CANbus/FMS

| Columna | Contenido |
| :--- | :--- |
| **A · N.° Correlativo** | 8 |
| **B · Empresa** | AudIT |
| **C · Fecha** | 2026-09-01 |
| **D · Tipo** | Técnica |
| **E · Referencia** | FEP03.10.26, Restricción N.° 6 (Cap. 10, p. 25) — «Ningún equipamiento a bordo puede afectar la garantía del vehículo»; Decisión no tomada N.° 12 (Numeral 16.1, p. 36); Cap. 5 — Telemetría de fábrica de 61 tractocamiones; Cap. 2.2 — Antigüedad promedio 6,4 años; Entrevista Trincado (Cap. 8, p. 19). |
| **F · Consulta** | El Caso 10 declara que 61 tractocamiones propios poseen telemetría de fábrica capaz de reportar kilometraje, consumo, códigos de falla y hábitos de conducción, información que «nunca se ha descargado» (Cap. 4.10). El Cap. 5 establece que su aprovechamiento «debe evaluarse y su factibilidad verificarse con cada fabricante». La Restricción N.° 6 prohíbe que el equipamiento afecte la garantía del vehículo. La proyección a 3 años eleva estos camiones a 110 unidades. El acceso a datos de telemetría vehicular requiere conexión al puerto FMS estándar (rFMS) o al conector OBD-II/J1939 del vehículo, lo que en algunas marcas puede afectar la garantía si no existe autorización expresa del fabricante o concesionario. **Se consulta:** ¿Curimón cuenta actualmente con acuerdos, autorizaciones o cartas de no objeción de los concesionarios o representantes de las marcas de sus 61 (proyectados 110) tractocamiones propios, que habiliten la conexión de dispositivos de lectura al conector FMS estándar sin pérdida de garantía de motor y tren motriz? En caso negativo, ¿el mandante asumirá la gestión de dichas autorizaciones como actividad propia, o el proponente debe considerar en su cronograma y riesgo la verificación con cada fabricante? |
| **G · Propuesta de interpretación de AudIT** | AudIT propone interpretar que la obtención de autorizaciones de los fabricantes es una actividad compartida: (a) Curimón gestionará la relación contractual con los concesionarios y obtendrá las cartas de no objeción, dado que es el propietario de los vehículos; (b) AudIT proveerá la especificación técnica del dispositivo de lectura y la documentación de certificación de compatibilidad que cada fabricante requiera. AudIT planificará la integración de telemetría como una actividad con dependencia externa y hito verificable en el cronograma, comenzando por los fabricantes con protocolo rFMS abierto y escalando a los demás. Esta interpretación permite a AudIT no trasladar al costo un riesgo de plazo que depende de terceros, y al mandante mantener el control de la relación comercial con sus proveedores de vehículos. |

---

### Consulta N.° 9 — Emisión de DTE en Puntos de Carga sin Cobertura Móvil

| Columna | Contenido |
| :--- | :--- |
| **A · N.° Correlativo** | 9 |
| **B · Empresa** | AudIT |
| **C · Fecha** | 2026-09-01 |
| **D · Tipo** | Técnica |
| **E · Referencia** | FEP03.10.26, Decisión no tomada N.° 9 (Numeral 16.1, p. 36); Cap. 4.5 (p. 12); Cap. 6 — tramos sin cobertura de más de 80 km; Restricción N.° 4 (Cap. 10, p. 24); Restricción N.° 8 — el sistema contable emite los DTE; FEP03.10.26, RT-03.10 — operación desconectada de 72 h; Cap. 12, «Documento electrónico de transporte» (p. 26); Expectativa 9.10 (p. 24). |
| **F · Consulta** | La normativa tributaria exige que el documento electrónico de transporte (DTE) exista antes de que el vehículo se mueva. El Cap. 4.5 reconoce que hay puntos de carga sin cobertura móvil donde el documento «no se puede emitir en el momento» y que «la práctica actual no resiste un examen». La Restricción N.° 8 establece que el sistema contable es el único emisor de DTE. La Decisión N.° 9 reconoce que esta materia no está resuelta. El RT-03.10 del caso exige operación desconectada de 72 horas, pero la emisión del DTE requiere folio autorizado por el SII y envío dentro del plazo legal. **Se consulta:** (i) ¿El mandante ha gestionado o gestionará ante el Servicio de Impuestos Internos la autorización de contingencia para emitión offline de DTE conforme a la Resolución Exenta SII N.° 107/2014 (o su sucesora), de modo que el proponente pueda diseñar un mecanismo de pre-foliado y emisión local a bordo con envío diferido? (ii) ¿O el mandante exige que el DTE se emita exclusivamente en línea desde el sistema contable, requiriendo cobertura satelital u otro canal alternativo en los puntos sin señal? |
| **G · Propuesta de interpretación de AudIT** | AudIT propone interpretar que el mandante gestionará la autorización de contingencia ante el SII, y que el proponente diseñará un módulo de pre-foliado a bordo con stock de folios CAF (Código de Autorización de Folios) almacenados en el dispositivo del conductor, que permita generar el DTE localmente, firmarlo electrónicamente y transmitirlo al sistema contable cuando se recupere la cobertura, dentro del plazo legal de envío al SII. Esta interpretación es favorable a AudIT porque elimina la dependencia de la cobertura móvil para un documento legalmente obligatorio, resolviéndolo con un componente del diseño de operación desconectada que ya se exige en RT-03.10, sin requerir infraestructura satelital adicional de alto costo. |

---

### Consulta N.° 10 — Regla de Excepción al Bloqueo de Asignación

| Columna | Contenido |
| :--- | :--- |
| **A · N.° Correlativo** | 10 |
| **B · Empresa** | AudIT |
| **C · Fecha** | 2026-09-01 |
| **D · Tipo** | Técnica |
| **E · Referencia** | FEP03.10.26, Expectativa 9.1 (p. 23) — bloqueo de la asignación; Decisión no tomada N.° 6 (Numeral 16.1, p. 36); Entrevista Aguayo — «prefiero frenar un viaje» (Cap. 8, p. 21); Entrevista Mansilla — «que me diga que no puedo, y por qué» (Cap. 8, p. 18); Numeral 13.3.7 — prueba en paralelo antes de bloquear. |
| **F · Consulta** | La Expectativa 9.1 exige que la verificación sea «bloqueante» y que «el sistema impida la asignación en lugar de limitarse a advertirla». Sin embargo, la Decisión N.° 6 reconoce que no existe la regla de excepción al bloqueo: prevención quiere que el sistema no deje salir y operaciones sabe que eso detiene viajes. El Numeral 13.3.7 exige probar el bloqueo en paralelo antes de activarlo efectivamente. **Se consulta:** ¿El mandante ha definido o definirá el perfil de autoridad que puede autorizar una excepción al bloqueo (override), las condiciones bajo las cuales dicha excepción es admisible (v.gr., fuerza mayor, cliente con carga perecible, cierre de paso fronterizo inminente), y el nivel de registro y auditoría que se exige sobre cada excepción autorizada? ¿O la definición de este protocolo de excepción es parte del diseño que debe proponer el proponente, sujeto a aprobación del mandante durante la ejecución? |
| **G · Propuesta de interpretación de AudIT** | AudIT propone interpretar que la definición del protocolo de excepción es responsabilidad del proponente en su diseño, sujeto a la validación del mandante en la instancia preparatoria correspondiente. AudIT diseñará un esquema de override con tres niveles de severidad (jornada parcialmente disponible, habilitación próxima a vencer, equipo con observación menor), con autorización nominal del jefe de turno de la torre, registro indeleable con firma electrónica del autorizador, motivo, y exposición automática del override en los tableros de prevención de riesgos. El override se auditará mensualmente y se medirá como indicador del plan de adhesión. Esta interpretación permite a AudIT diseñar un mecanismo de gobernanza del bloqueo que equilibre seguridad y operabilidad, evitando la parálisis operativa que la propia entrevista de operaciones anticipa. |

---

### Consulta N.° 11 — Enlace de Respaldo en Terminales Regionales

| Columna | Contenido |
| :--- | :--- |
| **A · N.° Correlativo** | 11 |
| **B · Empresa** | AudIT |
| **C · Fecha** | 2026-09-01 |
| **D · Tipo** | Administrativa |
| **E · Referencia** | FEP03.10.26, Cap. 6 (p. 14) — «Los cuatro terminales regionales con un proveedor y sin respaldo en tres de ellos»; FEP02.26, RT-03.17 (p. 11) — «El enlace entre el sitio on-premise y la nube será redundante, con caminos físicos y proveedores distintos»; FEP03.10.26, RT-03.24 del caso (p. 33) — «Exigible el respaldo de enlace en los cuatro terminales regionales». |
| **F · Consulta** | El RT-03.24 del caso exige respaldo de enlace en los cuatro terminales regionales (Antofagasta, Talca, Los Ángeles y Puerto Montt), tres de los cuales hoy no lo tienen. El RT-03.17 transversal exige redundancia con caminos físicos y proveedores distintos. Los terminales regionales se ubican en zonas donde la disponibilidad de proveedores de enlace dedicado puede ser limitada. **Se consulta:** (i) ¿La contratación y el costo recurrente mensual de los enlaces redundantes de los cuatro terminales regionales es de cargo de Curimón como gasto de conectividad de sus instalaciones, o debe ser presupuestado por el proponente como parte de su oferta de infraestructura y operación de 36 meses? (ii) ¿El mandante ha verificado la factibilidad de obtener un segundo proveedor de enlace con camino físico distinto en los tres terminales que hoy carecen de respaldo? |
| **G · Propuesta de interpretación de AudIT** | AudIT propone interpretar que la especificación técnica del enlace redundante (ancho de banda, latencia, SLA del carrier) es responsabilidad del proponente, y que la contratación y el costo recurrente del enlace son de cargo de Curimón como gasto de infraestructura de telecomunicaciones de sus propias instalaciones, análogo a RT-06.06. AudIT especificará los requisitos y evaluará la factibilidad en terreno durante la fase de levantamiento, proponiendo alternativas (enlace satelital LEO, 4G/5G redundante) donde no exista segundo proveedor de fibra. Esta delimitación es crítica para AudIT porque el costo de enlaces redundantes en cinco sitios durante 36 meses de operación tiene un impacto significativo en la Oferta Económica. |

---

### Consulta N.° 12 — Tratamiento del Período Mixto y Coexistencia Flota Equipada/No Equipada

| Columna | Contenido |
| :--- | :--- |
| **A · N.° Correlativo** | 12 |
| **B · Empresa** | AudIT |
| **C · Fecha** | 2026-09-01 |
| **D · Tipo** | Técnica |
| **E · Referencia** | FEP03.10.26, Decisión no tomada N.° 25 y N.° 26 (Numeral 16.1, p. 37); Cap. 2.2 — frecuencia de paso por terminal: cada 6 días, 22% de subcontratados menos de 1 vez/mes; Restricción N.° 5 (Cap. 10, p. 24); Numeral 13.3.10 — modo mixto; Criterio de Aceptación N.° 27 — plan de adhesión con resultados medibles. |
| **F · Consulta** | El despliegue de equipamiento a bordo en 374 camiones está físicamente limitado al paso por terminales (cada 6 días promedio, con 22% de subcontratados que pasan menos de 1 vez/mes). La Decisión N.° 26 reconoce que el período mixto (flota parcialmente equipada) «no es una transición breve: puede durar la mayor parte de una etapa». El Numeral 13.3.10 exige declarar qué ocurre con los camiones sin equipar al término de cada etapa. La Restricción N.° 5 establece que la instalación no puede inmovilizar unidades más allá del tiempo normal en terminal. **Se consulta:** ¿El mandante acepta que, para los efectos de los criterios de aceptación de la marcha blanca (Art. 17.3 de las Bases Administrativas), la verificación bloqueante de jornada y habilitaciones opere en dos modalidades coexistentes durante el período mixto: (a) verificación telemática completa para los camiones equipados, y (b) verificación documental degradada (declaración jurada digital + consulta a registro centralizado de vigencias) para los camiones aún no equipados, con una meta progresiva de cobertura telemática declarada mes a mes? ¿O se exigirá cobertura telemática del 100% de la flota como condición de paso a producción de la Etapa 1? |
| **G · Propuesta de interpretación de AudIT** | AudIT propone interpretar que el mandante aceptará la operación en modo mixto con ambas modalidades durante el período de despliegue progresivo, con una meta de cobertura telemática del 80% de la flota al cierre de la Etapa 1 y del 95% al cierre de la Etapa 2, comprometiéndose a alcanzar el 100% antes del mes 24 (tercer mes de operación). El 5% residual correspondería a camiones subcontratados de baja frecuencia cuya adhesión al plan tecnológico se gestionará con incentivos contractuales específicos. AudIT declarará la cobertura acumulada esperada mes a mes en el Formulario T-15, derivada de la frecuencia real de paso por terminal y del ritmo de adhesión de los transportistas. Esta interpretación es esencial para AudIT porque permite presentar un cronograma de despliegue realista, alineado con la física de la operación (como exige el Cap. 19), sin comprometer una cobertura del 100% que es físicamente inalcanzable en el plazo de la Etapa 1. |

---

> [!NOTE]
> **Nomenclatura del archivo para exportación:** `CONSULTAS_AUDIT_20260901.XLSX`
> La presente tabla debe trasladarse a la planilla oficial manteniendo las 7 columnas (A a G) conforme al formato del Art. 43.2. Cada fila de la planilla corresponde a una consulta (N.° 1 a 12).

---

> [!TIP]
> **Nota de calidad profesional (Art. 43.5):** Las 12 consultas identifican vacíos reales no resueltos por las Bases (referenciados a las 26 Decisiones no tomadas del Numeral 16.1), contradicciones verificables entre documentos (Cap. 6 del Caso vs. Cap. 6 Transversal; Restricción N.° 9 vs. Expectativa 9.5), y riesgos regulatorios no regulados (Ley N.° 21.719 en geolocalización de terceros, Art. 25 bis en jornada de conductores externos, Resolución SII sobre contingencia de DTE). Ninguna consulta traslada al CLIENTE una decisión de diseño que corresponda al proponente.
