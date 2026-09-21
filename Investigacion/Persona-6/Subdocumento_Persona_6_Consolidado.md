# Subdocumento Consolidado: Cuestionario de Evaluación de Conocimientos (30 Preguntas)
## Trabajo de Investigación TI-12 · Caso 10: Transportes Curimón S.A. · Empresa audIT
**Autor:** Persona 6 (*Assessment & Knowledge Verification Lead* — Marcel)  
**Asignatura:** Taller de Formulación de Proyectos Informáticos (ICI-5444) · PUCV  
**Estado:** Consolidado final para integración en el Anexo E del informe y defensa oral  
**Nivel de Declaración de IA (Punto 6.1):** Nivel 0 (Autoría 100% humana auditada, sin IA)  

---

## 1. Resumen Metodológico y Control de Distribución

El presente subdocumento formaliza el cuestionario de **30 preguntas de autoría propia** exigido en el Punto 3 de las *Indicaciones a cumplir y fichas de los temas asignados* (FEP00.3.26) para el tema **TI-12** (*Cumplimiento normativo en proyectos TIC: Ley 21.719, Ley 21.663 y marco internacional*).

### 1.1 Tabla de Control de Distribución de Dificultad (Mandato 40% / 40% / 20%)

| Nivel de Dificultad | Cantidad | Porcentaje | Criterio Pedagógico y Nivel Bloom | Rango de Preguntas |
| :--- | :---: | :---: | :--- | :---: |
| **Básica** | **12** | **40%** | Recordar y Comprender: definiciones legales exactas, plazos explícitos, organismos, multas y vigencias. | P01 a P12 |
| **Intermedia** | **12** | **40%** | Aplicar y Analizar: escenarios fácticos del Caso 10 Curimón, cruce de roles (responsable/encargado), directivas y herramientas GRC. | P13 a P24 |
| **Avanzada** | **6** | **20%** | Evaluar y Sintetizar: trade-offs técnicos y económicos, impacto de la CLOUD Act, Gordon-Loeb, borrado criptográfico y dilemas normativos. | P25 a P30 |
| **TOTAL** | **30** | **100%** | **Cobertura 100% integral de la Ficha TI-12 y del Caso Curimón S.A.** | **P01 a P30** |

### 1.2 Balance de Formatos Exigidos

| Formato | Código LaTeX | Cantidad | Distribución por Dificultad | Porcentaje |
| :--- | :---: | :---: | :--- | :---: |
| **Selección Múltiple** | `seleccion` | **8** | 3 Básicas, 3 Intermedias, 2 Avanzadas | 26,7% |
| **Verdadero o Falso** | `vf` | **8** | 3 Básicas, 3 Intermedias, 2 Avanzadas | 26,7% |
| **Completar** | `completar` | **7** | 3 Básicas, 3 Intermedias, 1 Avanzada | 23,3% |
| **Respuesta Corta** | `corta` | **7** | 3 Básicas, 3 Intermedias, 1 Avanzada | 23,3% |
| **TOTAL** | | **30** | **Equilibrio pedagógico multidimensional** | **100%** |

---

## 2. Banco Completo de Preguntas, Respuestas y Justificaciones

### Bloque 1: Preguntas Básicas (12 Preguntas · 40%)

#### Pregunta 1 (Selección múltiple · Básica · Sección: 1.3 Ley 21.663 y ANCI)
* **Enunciado:** Si un operador calificado como prestador de servicios esenciales sufre un incidente de ciberseguridad con efecto significativo, ¿de qué plazo perentorio dispone para emitir la alerta temprana ante el CSIRT Nacional según la Ley 21.663?  
  a) 1 hora corrida.  
  b) 3 horas corridas.  
  c) 24 horas corridas.  
  d) 72 horas corridas.  
* **Respuesta:** b) 3 horas corridas.
* **Justificación técnica:** El Art. 9 de la Ley 21.663 y el D.S. 295/2024 fijan un esquema escalonado de tres reportes: la alerta temprana obligatoria en un máximo de 3 horas corridas de tomado conocimiento, una actualización con antecedentes técnicos a las 72 horas y el informe final a los 15 días corridos.

#### Pregunta 2 (Verdadero o Falso · Básica · Sección: 1.2 Ley 21.719)
* **Enunciado:** Con la entrada en vigencia de la Ley 21.719 sobre Protección de Datos Personales, ¿es legalmente obligatorio para cualquier empresa privada en Chile designar un Delegado de Protección de Datos (DPO)?
* **Respuesta:** Falso.
* **Justificación técnica:** El Art. 50 de la Ley 21.719 deja la figura del DPO como voluntaria para el sector privado. No es un mandato legal forzoso (a diferencia del RGPD europeo en ciertos supuestos), sino un incentivo: el Art. 49 lo reconoce expresamente como medida atenuante de responsabilidad dentro de los modelos de prevención de infracciones.

#### Pregunta 3 (Completar · Básica · Sección: 1.2 Ley 21.719)
* **Enunciado:** Bajo el régimen general sancionatorio de la Ley 21.719, el tope máximo de multa para infracciones calificadas como gravísimas cometidas por un responsable del tratamiento alcanza hasta `\rule{3cm}{0.4pt}` UTM (sin considerar los agravantes por reincidencia).
* **Respuesta:** 20.000
* **Justificación técnica:** El Art. 35 reformado de la Ley 19.628 establece una escala de sanciones fijada en hasta 5.000 UTM para infracciones leves, 10.000 UTM para graves y 20.000 UTM para gravísimas. Solo en casos de reincidencia reiterada de grandes empresas la multa puede calcularse como un porcentaje (2% o 4%) de sus ingresos anuales.

#### Pregunta 4 (Respuesta corta · Básica · Sección: 1.1 Estado de vigencia)
* **Enunciado:** ¿Cuál es el estado de vigencia real de la Ley 21.719 sobre protección de datos personales a septiembre de 2026?
* **Respuesta:** Fue promulgada y publicada en el Diario Oficial el 13 de diciembre de 2024, pero se encuentra en período de vacancia legal de 24 meses (rige desde el 1 de diciembre de 2026). Paralelamente, se tramita en el Congreso el Boletín 18.623-07 que propone postergar su entrada en vigor a diciembre de 2027.
* **Justificación técnica:** La verificación en fuentes oficiales de la BCN constata que la reforma aún no aplica su régimen punitivo debido a la vacancia legal diferida de 24 meses y la demora en la conformación de la Agencia de Protección de Datos.

#### Pregunta 5 (Selección múltiple · Básica · Sección: 1.8 Normas certificables)
* **Enunciado:** Al auditar la seguridad de la información de una empresa, ¿cuál de los siguientes instrumentos internacionales corresponde a una norma de requisitos auditable y certificable por una casa acreditadora independiente?  
  a) NIST Cybersecurity Framework (CSF 2.0).  
  b) ISO/IEC 27001:2022.  
  c) Directiva NIS2 de la Unión Europea.  
  d) OWASP Application Security Verification Standard (ASVS).  
* **Respuesta:** b) ISO/IEC 27001:2022.
* **Justificación técnica:** ISO/IEC 27001 es el único estándar internacional de la lista que posee un esquema de certificación formal de tercera parte (organismos acreditados como BSI, SGS o AENOR). NIST CSF es una guía voluntaria de buenas prácticas, NIS2 es una directiva regulatoria comunitaria vinculante y OWASP ofrece pautas de verificación para desarrollo de software.

#### Pregunta 6 (Verdadero o Falso · Básica · Sección: 1.4 Normativa complementaria)
* **Enunciado:** Tras la promulgación de la Ley 21.459 sobre delitos informáticos, una empresa en Chile puede ser objeto de responsabilidad penal como persona jurídica por delitos de sabotaje o acceso ilícito a sistemas informáticos.
* **Respuesta:** Verdadero.
* **Justificación técnica:** La Ley 21.459 modernizó la tipificación de los delitos informáticos homologándolos al Convenio de Budapest e incorporó expresamente estos tipos penales al catálogo de conductas que hacen responsable penalmente a la persona jurídica bajo la Ley 20.393.

#### Pregunta 7 (Completar · Básica · Sección: 1.7 Marco internacional)
* **Enunciado:** Conforme al artículo 33 del RGPD de la Unión Europea, ante una violación de seguridad que comprometa datos personales, el responsable debe notificar a la autoridad de control en un plazo perentorio que no exceda las `\rule{3cm}{0.4pt}` horas tras tomar conocimiento de ella.
* **Respuesta:** 72
* **Justificación técnica:** El Art. 33 del RGPD estipula que la notificación debe hacerse a más tardar a las 72 horas de haber tenido constancia del incidente, salvo que sea improbable que represente un riesgo para los derechos y libertades de las personas.

#### Pregunta 8 (Respuesta corta · Básica · Sección: 1.3 Ley 21.663 y ANCI)
* **Enunciado:** ¿Cuál es la diferencia práctica entre calificar como «Servicio Esencial» y ser declarado «Operador de Importancia Vital» (OIV) bajo la Ley 21.663 de Ciberseguridad?
* **Respuesta:** La condición de Servicio Esencial opera por ministerio de la ley según el rubro o sector económico (transporte, telecomunicaciones, energía, salud, según el Art. 4). En cambio, la calidad de OIV requiere una resolución administrativa fundada y particular de la ANCI (Art. 5), dirigida a entidades específicas cuya alteración provocaría un daño crítico al país.
* **Justificación técnica:** El Art. 4 califica sectores económicos completos por ministerio de la ley. En contraste, el Art. 5 reserva la calidad de OIV para entidades específicas mediante resolución exenta de la ANCI, activando exigencias de reporte más estrictas (24 h) y multas agravadas de hasta 40.000 UTM.

#### Pregunta 9 (Selección múltiple · Básica · Sección: 2.2 Herramientas GRC)
* **Enunciado:** ¿Bajo qué esquema de licenciamiento opera la herramienta de gestión de cumplimiento CISO Assistant evaluada como alternativa GRC en el proyecto?  
  a) Software SaaS propietario de código cerrado con cobro mensual por activo monitoreado.  
  b) Código abierto bajo licencia GNU AGPLv3, con opción de soporte empresarial Pro autogestionado.  
  c) Licencia de código abierto permisiva MIT sin restricciones de redistribución comercial.  
  d) Licencia gubernamental restringida exclusiva para organismos del sector público de la Unión Europea.  
* **Respuesta:** b) Código abierto bajo licencia GNU AGPLv3, con opción de soporte empresarial Pro autogestionado.
* **Justificación técnica:** CISO Assistant es una solución de GRC comunitaria de código abierto regida por la licencia copyleft de red AGPLv3. Esto permite a audIT implementarla on-premise o en nube privada sin costo de licencia de entrada, pagando únicamente una suscripción anual fija (EUR 2.400/año) si se requiere soporte y módulos Pro.

#### Pregunta 10 (Verdadero o Falso · Básica · Sección: 1.6 Transferencias internacionales)
* **Enunciado:** En el marco de la Ley 21.719, las transferencias de datos personales hacia servidores alojados en Estados Unidos quedan autorizadas de forma automática y libre de salvaguardas contractuales, ya que dicho país posee declaración de adecuación plena en Chile.
* **Respuesta:** Falso.
* **Justificación técnica:** La futura Agencia de Protección de Datos Personales (APDP) no ha dictado resoluciones de adecuación para Estados Unidos conforme al Art. 28. En consecuencia, transferir datos a ese territorio exige salvaguardas específicas, típicamente la firma de Cláusulas Contractuales Tipo (SCC) entre responsable y destinatario (Art. 27).

#### Pregunta 11 (Completar · Básica · Sección: 1.8 Normas certificables)
* **Enunciado:** El estándar internacional auditable que define los requisitos para establecer, implementar, mantener y mejorar un Sistema de Gestión de Inteligencia Artificial (SGIA) corresponde a la norma ISO/IEC `\rule{3cm}{0.4pt}`.
* **Respuesta:** 42001 (o 42001:2023)
* **Justificación técnica:** ISO/IEC 42001:2023 es la primera norma certificable a nivel mundial que aborda de manera sistemática los riesgos éticos, técnicos y de gobernanza operacional vinculados al ciclo de vida de modelos y algoritmos de IA.

#### Pregunta 12 (Respuesta corta · Básica · Sección: 1.2 Ley 21.719)
* **Enunciado:** En la Ley 21.719 que reforma la Ley 19.628, ¿bajo qué categoría legal quedan los datos biométricos (como reconocimiento facial o huella dactilar) y qué condición de licitud general se les exige?
* **Respuesta:** Se clasifican expresamente como datos sensibles (Art. 2 letra g). Su tratamiento exige como regla general el consentimiento expreso y fundamentado del titular otorgado por escrito o por un medio electrónico indubitado, salvo causales legales taxativas (Art. 16).
* **Justificación técnica:** La reforma superó la omisión de la ley antigua e incorporó expresamente los datos biométricos como datos sensibles (Art. 2 letra g), exigiendo consentimiento expreso y fundamentado (Art. 16) bajo el estándar más exigente de confidencialidad y medidas de seguridad.

---

### Bloque 2: Preguntas Intermedias (12 Preguntas · 40%)

#### Pregunta 13 (Selección múltiple · Intermedia · Sección: 1.2 Ley 21.719)
* **Enunciado:** En la operación del Caso 10 de Transportes Curimón, ¿qué roles jurídicos asumen la empresa de transporte y el proveedor audIT respecto al tratamiento de datos y telemetría de los 454 choferes bajo la Ley 21.719?  
  a) Curimón actúa como encargado del tratamiento y audIT asume la calidad de responsable principal de las bases de datos.  
  b) Ambas partes operan como corresponsables solidarios directos ante la APDP sin mediar contrato de mandato.  
  c) Curimón es el responsable del tratamiento y audIT actúa exclusivamente como encargado del tratamiento bajo instrucciones.  
  d) audIT es calificado como un simple proveedor de infraestructura física exento de obligaciones de tratamiento de datos.  
* **Respuesta:** c) Curimón es el responsable del tratamiento y audIT actúa exclusivamente como encargado del tratamiento bajo instrucciones.
* **Justificación técnica:** Curimón determina los fines y medios del negocio logístico (responsable). audIT procesa y aloja la telemetría por cuenta de la mandante siguiendo sus instrucciones contractuales (encargado, Art. 15 bis), formalizado a través de un Acuerdo de Procesamiento de Datos (DPA).

#### Pregunta 14 (Verdadero o Falso · Intermedia · Sección: 3.1 Arquitectura)
* **Enunciado:** En el despliegue cloud propuesto para Curimón sobre Microsoft Azure, la réplica de datos entre la región primaria (Chile Central) y el sitio secundario de contingencia (East US 2) puede implementarse habilitando almacenamiento geo-redundante nativo con zonas (GZRS).
* **Respuesta:** Falso.
* **Justificación técnica:** Azure Chile Central carece de «región emparejada» (paired region) en la topología global de Microsoft. La sincronización hacia East US 2 debe gestionarse a nivel de aplicación y motor de base de datos con transferencias internacionales controladas bajo SCC.

#### Pregunta 15 (Completar · Intermedia · Sección: 1.4 Normativa complementaria)
* **Enunciado:** El Dictamen Ordinario N.º 569/2018 de la Dirección del Trabajo prohíbe taxativamente que los dispositivos de posicionamiento satelital (GPS) a bordo de la flota vehicular se utilicen como mecanismos directos de control de `\rule{4cm}{0.4pt}` laboral.
* **Respuesta:** asistencia y jornada (o jornada laboral)
* **Justificación técnica:** La doctrina laboral chilena dictamina que la geolocalización continua es un medio técnico para la seguridad física de la carga y la gestión logística vial, pero no constituye un mecanismo lícito para fiscalizar pausas, descansos o registrar el inicio/término de la jornada de trabajo.

#### Pregunta 16 (Respuesta corta · Intermedia · Sección: 3.2 Matriz de obligaciones)
* **Enunciado:** Si el módulo analítico de fatiga de Curimón bloquea automáticamente a un conductor para un despacho minero por considerar que presenta signos de somnolencia, ¿qué garantías específicas le confiere el Art. 8 bis de la Ley 21.719?
* **Respuesta:** El conductor tiene derecho a ser informado de que la resolución fue automatizada, a exigir que se le explique la lógica y las variables consideradas por el modelo, y a impugnar el bloqueo exigiendo una revisión e intervención humana directa por parte de un operador calificado de Curimón.
* **Justificación técnica:** El Art. 8 bis prohíbe que las personas queden sujetas a decisiones puramente algorítmicas que impacten negativamente sus derechos laborales o contractuales sin una instancia de supervisión y contradicción humana.

#### Pregunta 17 (Selección múltiple · Intermedia · Sección: 1.5 Privacidad desde el diseño)
* **Enunciado:** Considerando el cronograma a 56 meses del proyecto de Curimón, ¿en qué momento debe ejecutarse formalmente la Evaluación de Impacto en la Protección de Datos (EIPD / DPIA) sobre el sistema telemático de cabina?  
  a) Durante las pruebas integradas de carga en la Etapa 2, inmediatamente antes del despliegue en producción.  
  b) En la fase de arquitectura y diseño conceptual durante la Etapa 1, de manera previa al inicio del tratamiento de telemetría masiva.  
  c) En el mes 21 de operación, una vez consolidada la línea base de los primeros 100 camiones en ruta.  
  d) Solo en caso de que ocurra una filtración de seguridad de datos personales que deba ser reportada a la autoridad.  
* **Respuesta:** b) En la fase de arquitectura y diseño conceptual durante la Etapa 1, de manera previa al inicio del tratamiento de telemetría masiva.
* **Justificación técnica:** Por mandato del Art. 15 ter de la Ley 21.719 y el principio de Privacy by Design, la EIPD debe ser preventiva. Analizar los riesgos de 454 choferes en la Etapa 1 permite incorporar controles técnicos (como cifrado y consentimiento granular) en el diseño de software antes de capturar datos reales.

#### Pregunta 18 (Verdadero o Falso · Intermedia · Sección: 2.1 Marcos normativos)
* **Enunciado:** A diferencia del RGPD de la Unión Europea, la Ley Marco de Ciberseguridad de Chile (Ley 21.663) estructura sus multas exclusivamente en Unidades Tributarias Mensuales (UTM), sin considerar un porcentaje sobre los ingresos anuales de la empresa infractora.
* **Respuesta:** Verdadero.
* **Justificación técnica:** El Art. 40 de la Ley 21.663 tasa las infracciones exclusivamente en UTM (hasta 20.000 UTM generales y hasta 40.000 UTM si se trata de un OIV reincidente), sin incorporar la figura del porcentaje de facturación que sí utilizan el RGPD y la Ley 21.719 de datos personales.

#### Pregunta 19 (Completar · Intermedia · Sección: 1.3 Ley 21.663 y ANCI)
* **Enunciado:** Si un Operador de Importancia Vital (OIV) experimenta un incidente de ciberseguridad que provoca la interrupción efectiva de su servicio esencial, la Ley 21.663 reduce el plazo de envío de la actualización intermedia al CSIRT Nacional de 72 a `\rule{3cm}{0.4pt}` horas corridas.
* **Respuesta:** 24
* **Justificación técnica:** El Art. 9 establece un procedimiento agravado de notificación para OIV cuando hay afectación a la continuidad operacional: se mantiene la alerta temprana en 3 horas, pero la actualización técnica se reduce de 72 a 24 horas corridas, exigiendo un plan de contingencia formal a los 7 días.

#### Pregunta 20 (Respuesta corta · Intermedia · Sección: 1.7 Marco internacional)
* **Enunciado:** ¿Por qué el módulo telemático de detección de fatiga y despacho automatizado de Curimón clasificaría como sistema de «Alto Riesgo» según el Reglamento de IA de la Unión Europea (Reglamento UE 2024/1689)?
* **Respuesta:** Porque el Anexo III (numeral 4) del Reglamento europeo clasifica taxativamente como sistemas de alto riesgo a los modelos de IA utilizados en el ámbito laboral para evaluar el rendimiento de los trabajadores, monitorear su comportamiento o tomar decisiones que afecten sus condiciones laborales o acceso a turnos.
* **Justificación técnica:** El monitoreo continuo de conductores y la inferencia algorítmica sobre su capacidad física impactan directamente en sus derechos laborales y su seguridad personal, requiriendo gobernanza, trazabilidad y supervisión humana según los estándares internacionales.

#### Pregunta 21 (Selección múltiple · Intermedia · Sección: 3.2 Matriz de obligaciones)
* **Enunciado:** De acuerdo con las Bases Técnicas del Caso 10 de Curimón, ¿cuál es el plazo máximo contractual fijado en el requerimiento RT-11.18 para que audIT notifique a la contraparte ante un incidente de ciberseguridad calificado como crítico?  
  a) Máximo 2 horas.  
  b) Máximo 6 horas.  
  c) Máximo 12 horas.  
  d) Máximo 24 horas.  
* **Respuesta:** a) Máximo 2 horas.
* **Justificación técnica:** El requerimiento contractual RT-11.18 impone un estándar privado más estricto que la ley estatal chilena (que otorga 3 horas para la alerta al CSIRT), exigiendo que el proveedor alerte formalmente al cliente en un plazo no superior a 2 horas desde la confirmación de la criticidad del evento.

#### Pregunta 22 (Verdadero o Falso · Intermedia · Sección: 1.6 Transferencias internacionales)
* **Enunciado:** Cuando un camión de Transportes Curimón cruza la frontera y opera en el tramo internacional hacia Mendoza, la telemetría capturada en ruta y el tratamiento de datos de los choferes en territorio trasandino quedan alcanzados por la Ley 25.326 de la República Argentina.
* **Respuesta:** Verdadero.
* **Justificación técnica:** Por el principio universal de territorialidad de la ley, cualquier tratamiento o captura de datos personales efectuada en territorio argentino se rige por su propia legislación (Ley 25.326), quedando bajo la fiscalización de la Agencia de Acceso a la Información Pública (AAIP).

#### Pregunta 23 (Completar · Intermedia · Sección: 3.2 Matriz de obligaciones)
* **Enunciado:** Para cumplir el requerimiento RT-11.10 de las Bases Técnicas, la plataforma de audIT debe asegurar que las llaves criptográficas utilizadas para el cifrado a nivel de campo se resguarden en un módulo de seguridad de hardware denominado `\rule{3cm}{0.4pt}` (o por su sigla en inglés).
* **Respuesta:** HSM (Hardware Security Module)
* **Justificación técnica:** El almacenamiento de claves maestras en un dispositivo HSM certificado (mínimo FIPS 140-2 Nivel 3) garantiza que las claves no residan en texto plano en la memoria del servidor de aplicaciones ni puedan ser extraídas por el proveedor del servicio cloud.

#### Pregunta 24 (Respuesta corta · Intermedia · Sección: 2.2 Herramientas GRC)
* **Enunciado:** ¿Cuál es la principal justificación técnica y económica para incorporar una plataforma de software GRC (como CISO Assistant) frente al uso tradicional de hojas de cálculo en el proyecto de Curimón?
* **Respuesta:** Facilita el mapeo cruzado de controles (cross-framework mapping). Una única evidencia técnica implementada (como el cifrado en reposo o la política de contraseñas) se vincula y acredita simultáneamente para ISO 27001, Ley 21.663, Ley 21.719 y RGPD, eliminando la duplicidad de auditorías internas y reduciendo los costos de consultoría externa.
* **Justificación técnica:** Centralizar la trazabilidad y la gestión de evidencias normativas en una única plataforma evita redundancias operacionales y disminuye drásticamente el costo de horas profesionales de auditoría presupuestadas en el TCO del proyecto.

---

### Bloque 3: Preguntas Avanzadas (6 Preguntas · 20%)

#### Pregunta 25 (Selección múltiple · Avanzada · Sección: 1.6 Transferencias internacionales)
* **Enunciado:** Dado que la infraestructura cloud seleccionada es Microsoft Azure (proveedor domiciliado en EE.UU.), ¿qué salvaguarda técnica previene que Microsoft pueda entregar la telemetría sensible de Curimón en texto plano ante una orden judicial federal bajo la US CLOUD Act?  
  a) Contratar el servicio de cifrado estándar en reposo con claves administradas automáticamente por Microsoft (SSE con claves de plataforma).  
  b) Alojar los datos en máquinas virtuales aisladas sin conexión a Internet pública ni puertos de administración remota abiertos.  
  c) Implementar cifrado a nivel de campo con claves maestras custodiadas exclusivamente por Curimón en un HSM bajo esquema BYOK / HYOK.  
  d) Suscribir una cláusula contractual que someta cualquier requerimiento judicial extranjero a los tribunales ordinarios de Santiago.  
* **Respuesta:** c) Implementar cifrado a nivel de campo con claves maestras custodiadas exclusivamente por Curimón en un HSM bajo esquema BYOK / HYOK.
* **Justificación técnica:** La US CLOUD Act obliga a matrices estadounidenses a entregar datos bajo su custodia sin importar su ubicación física en el mundo. La única mitigación técnica real es que el cliente retenga el control absoluto de las llaves en un HSM (Bring/Hold Your Own Key): si Microsoft es compelido legalmente a entregar los datos, solo podrá suministrar bloques de texto cifrado matemáticamente ininteligibles.

#### Pregunta 26 (Verdadero o Falso · Avanzada · Sección: 3.3 Impacto económico)
* **Enunciado:** En el modelo TCO a 56 meses formulado para el cumplimiento normativo de Curimón (8.492,16 UF), la partida presupuestaria que introduce la mayor variabilidad y riesgo financiero es el costo de adquisición de licencias de software y servidores en la nube.
* **Respuesta:** Falso.
* **Justificación técnica:** Las suscripciones de software GRC y el consumo cloud representan una fracción menor y predecible ($<30\%$). Más del 70% del TCO proviene de las horas profesionales de perfiles expertos de alta renta (CISO a 2,0 UF/h, DPO y Asesor Legal externo bajo los aranceles del Formulario E-26), donde cualquier retraso en auditorías o fiscalizaciones impacta severamente el presupuesto.

#### Pregunta 27 (Completar · Avanzada · Sección: 3.1 Arquitectura)
* **Enunciado:** La técnica criptográfica que permite satisfacer el derecho de supresión de un conductor (Art. 8 ter de la Ley 21.719) sin corromper la integridad referencial de las bases de datos de despachos ni infringir los plazos de retención tributaria de 6 años se denomina `\rule{4cm}{0.4pt}` (o su término en inglés).
* **Respuesta:** borrado criptográfico (o crypto-shredding)
* **Justificación técnica:** Se asigna una llave de cifrado simétrica individual a cada chofer en Azure Key Vault. Al solicitar la supresión o finalizar el contrato, se destruye su llave específica: la información histórica de la carga permanece intacta para el SII y la DT, pero los datos personales del conductor quedan matemáticamente irrecuperables de forma irreversible.

#### Pregunta 28 (Respuesta corta · Avanzada · Sección: 4. Tendencias)
* **Enunciado:** Si el Congreso Nacional promulga la postergación de la Ley 21.719 hasta diciembre de 2027 (Boletín 18.623-07), ¿por qué audIT no puede rebajar el presupuesto de ciberseguridad ni desmantelar los controles planificados para el primer año de operación de Curimón?
* **Respuesta:** Porque la Ley Marco de Ciberseguridad (Ley 21.663) rige plenamente sin postergación (Curimón es operador de transporte calificado como servicio esencial), y porque las Bases Técnicas de la Licitación exigen contractualmente controles ISO 27001 y cifrado desde el día uno (requisitos RT-11.05 y RT-11.10). Una prórroga legislativa solo atrasa las multas de la APDP, pero no extingue las obligaciones de ciberseguridad ni los compromisos del contrato de licitación.
* **Justificación técnica:** El estándar de seguridad de la información está anclado a dos pilares independientes del régimen de la ley de datos: la legislación de ciberseguridad vigente y los requerimientos mandatorios del contrato privado con el cliente.

#### Pregunta 29 (Selección múltiple · Avanzada · Sección: 2.1 Marcos normativos)
* **Enunciado:** Al comparar la Ley 21.719 de Chile con el RGPD europeo respecto a la toma de decisiones basada en tratamientos automatizados y perfilamiento algorítmico:  
  a) La ley chilena prohíbe de manera absoluta cualquier algoritmo en relaciones laborales, mientras que el RGPD lo admite siempre que cuente con autorización sindical previa.  
  b) Ambos cuerpos legales reconocen el derecho del titular a no quedar sujeto a decisiones exclusivamente automatizadas, facultándolo a exigir intervención humana y a conocer los criterios del modelo.  
  c) El RGPD faculta la impugnación de decisiones algorítmicas solo en el sector público, mientras que la normativa chilena limita este derecho exclusivamente al comercio electrónico.  
  d) La legislación chilena exige una auditoría judicial previa al despliegue de cualquier algoritmo, mientras que el RGPD solo contempla sanciones indemnizatorias a posteriori.  
* **Respuesta:** b) Ambos cuerpos legales reconocen el derecho del titular a no quedar sujeto a decisiones exclusivamente automatizadas, facultándolo a exigir intervención humana y a conocer los criterios del modelo.
* **Justificación técnica:** El Art. 8 bis de la Ley 21.719 homologó el principio del Art. 22 del RGPD: el titular tiene derecho a no ser objeto de una decisión basada únicamente en valoraciones automatizadas que produzcan efectos jurídicos, teniendo derecho a ser informado de la lógica aplicada y a solicitar la intervención de un operador humano.

#### Pregunta 30 (Verdadero o Falso · Avanzada · Sección: 3.3 Impacto económico)
* **Enunciado:** De acuerdo con el modelo microeconómico de Gordon-Loeb aplicado en el análisis de inversión del proyecto, el gasto óptimo y racional en medidas de ciberseguridad para proteger la plataforma de Curimón no debe superar teóricamente un tercio (≈37%) de la pérdida económica esperada ante una vulneración.
* **Respuesta:** Verdadero.
* **Justificación técnica:** Gordon y Loeb (2002) demostraron analíticamente que, bajo el principio de rendimientos marginales decrecientes de las tecnologías defensivas, la inversión óptima en seguridad de la información se encuentra acotada superiormente por $1/e \approx 36,79\%$ de la pérdida esperada. Destinar más recursos que dicho umbral destruye valor económico y resulta irracional desde la perspectiva financiera.

---

## 3. Matriz de Cobertura Temática y Trazabilidad

| Subtema Ficha TI-12 | Preguntas Asociadas | Cantidad | Porcentaje Cobertura |
| :--- | :--- | :---: | :---: |
| **1. Protección de Datos (Ley 21.719 / RGPD)** | P02, P03, P04, P07, P10, P12, P13, P16, P17, P22, P27, P29 | 12 | 40,0% |
| **2. Ciberseguridad & ANCI (Ley 21.663)** | P01, P06, P08, P18, P19 | 5 | 16,7% |
| **3. Arquitectura Cloud & Seguridad (Azure / HSM / CLOUD Act)** | P14, P23, P25 | 3 | 10,0% |
| **4. Gobierno de IA & Automatización (AI Act / ISO 42001)** | P11, P20 | 2 | 6,7% |
| **5. Economía de la Seguridad & TCO (Gordon-Loeb / E-24)** | P26, P30 | 2 | 6,7% |
| **6. Cumplimiento Operacional, GRC & Bases (RT-11 / DT 569)** | P05, P09, P15, P21, P24, P28 | 6 | 20,0% |
| **TOTAL** | **P01 a P30** | **30** | **100,0%** |
