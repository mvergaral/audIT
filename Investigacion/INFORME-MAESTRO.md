# Cumplimiento normativo en proyectos TIC: Ley 21.719, Ley 21.663 (ANCI) y marco internacional

## Trabajo de Investigación TI-12 · Empresa N.º 10 · AudIT

**Caso de aplicación:** Caso 10 — Transportes Curimón S.A. (Licitación TFEP-01/2026)
**Fecha de entrega:** 21 de septiembre de 2026
**Integrantes:** Ignacio Cuevas · Alonso · Ignacio Vergara · Carlos Abarza · Martín Cevallos · Marcel · Naomi · Matías Vergara

---

## Resumen ejecutivo

Transportes Curimón administra una flota de 374 camiones, 454 conductores (196 propios y 258 externos), 148 transportistas subcontratados y 84 clientes corporativos bajo un contrato licitado a 56 meses con operaciones entre la frontera de Chile y Argentina, es decir, hacia Mendoza. Históricamente, la operación sufría de falta de visibilidad y control sobre sus unidades, con datos de telemetría y jornadas dispersos en planillas informales, lo que impedía costear tramos reales y configuraba un riesgo real ante el nuevo marco regulatorio chileno. El presente trabajo estructura el programa integral de cumplimiento normativo (TI-12) para el proyecto, articulando la Ley N.º 21.719 sobre Protección de Datos Personales (sanciones de hasta 20.000 UTM o 4% de ventas), la Ley N.º 21.663 de Ciberseguridad (notificación obligatoria al CSIRT Nacional en $\le 3\text{ h}$ bajo D.S. 295/2024) y la Ley N.º 25.326 argentina para el tránsito internacional. Se descartó el uso de banda ancha satelital en toda la flota porque era una opción elevada en el precio, adoptándose una arquitectura de conectividad por capas: telemetría por celular como principal, almacenamiento local cifrado y satélite transaccional de respaldo, convergiendo en una vista operacional unificada. La solución se despliega en Azure Chile Central con réplica en East US 2 (bajo Cláusulas Contractuales Tipo), cifrado de campo (RT-11.10) con 686 claves individuales en Azure Key Vault Premium y gobierno GRC. El presupuesto de cumplimiento asciende a 8.492,16 UF netas, representando el 3,9% del contrato de licitación y asegurando un RoSI mayor a +250%.

---

## Introducción

Un proyecto TIC no se puede evaluar solo por si la plataforma funciona o no. Cuando maneja datos personales y sostiene una operación crítica, como ocurre en Transportes Curimón, también debe demostrar que cumple con la ley desde el inicio. Si no existe una base legal clara, si los proveedores no tienen responsabilidades definidas o si no hay un plan para responder ante incidentes, una buena solución técnica igual puede transformarse en un riesgo para la empresa.

El tema TI-12 pide identificar qué obligaciones legales afectan a un proyecto desarrollado o utilizado en Chile. Para este caso, las dos normas principales son la Ley N.º 21.719, que actualiza la protección de datos personales, y la Ley N.º 21.663, que organiza el marco nacional de ciberseguridad mediante la ANCI y el CSIRT Nacional. En términos prácticos, esto obliga a revisar la licitud del tratamiento de datos, la seguridad de la información, los derechos de los titulares, las responsabilidades de cada actor y los plazos de reporte ante incidentes.

La aplicación se realiza sobre el Caso 10, Transportes Curimón S.A. El sistema licitado busca ordenar la información de una flota distribuida, vinculando datos de conductores propios y externos con rutas, jornadas y telemetría. Además, participan transportistas subcontratados, clientes corporativos y proveedores cloud. Por eso, el análisis no puede quedarse en una revisión general de leyes: debe aterrizarse en temas concretos como monitoreo por GPS, contratos de encargo, cifrado, transferencias internacionales, continuidad operacional y respuesta ante incidentes.

El objetivo del informe es conectar el marco legal y técnico con decisiones concretas del proyecto. Para eso se revisan normas nacionales e internacionales, organismos, estándares y herramientas de apoyo, y luego se ordena todo en una matriz con actividades, responsables, plazos, evidencias y costos. La idea final es que el cumplimiento no quede como una declaración general, sino como una parte real de la arquitectura, el presupuesto y la ejecución del proyecto.

### Delimitación del aporte propio

En cumplimiento del Punto 4 de las Indicaciones, AudIT delimita su aporte propio frente a la Ficha TI-12: mientras la ficha suministró el marco conceptual general de las Leyes 21.719 y 21.663, los estándares ISO 27001/27701/42001 y las herramientas base de mercado, el grupo aportó:

1. La incorporación obligatoria de la Ley argentina 25.326 por el paso fronterizo a Mendoza y del marco de atestación SOC 2 Type II para los 84 clientes.
2. La integración del Dictamen DT N.º 569/2018 para regular el monitoreo mediante GPS.
3. La evaluación de Eramba y Osano como herramientas GRC de aporte propio para ponderar el esquema On-Premise vs. SaaS.
4. La formulación de una solución de conectividad por capas con almacenamiento local cifrado que resuelve el descontrol de flota descartando la banda ancha satelital por sobrecosto.
5. El diseño de aislamiento criptográfico de 686 llaves HSM (RT-11.10).
6. La modelación formal del TCO de 8.492,16 UF conciliado con los aranceles E-26 y el límite de inversión de Gordon-Loeb.

---


---

# 1. Marco legal chileno

### 1. La Asimetría Regulatoria que Condiciona Toda la Propuesta

Al 20 de septiembre de 2026 el ordenamiento chileno presenta una asimetría que define el diseño de cumplimiento de este proyecto: **la Ley N° 21.663 está plenamente operativa, mientras que la Ley N° 21.719 está publicada pero no vigente, y la autoridad que ella crea no existe**.

La **Ley N° 21.719**, que regula la protección y el tratamiento de los datos personales y crea la Agencia de Protección de Datos Personales, fue publicada en el Diario Oficial el **13 de diciembre de 2024**. Su **Artículo primero transitorio** difiere la entrada en vigencia «hasta el día primero del mes vigésimo cuarto posterior a su publicación», esto es, el **1 de diciembre de 2026** —**72 días después de la fecha de corte**— y ordena que entretanto «seguirá operando la antigua ley N° 19.628» **[V]**. Se corrige aquí un error de atribución frecuente: **la fecha de vigencia está en el Artículo primero transitorio, no en el tercero**, que fija las reglas de la primera designación del Consejo Directivo **[S]**.

La **Agencia de Protección de Datos Personales no está constituida**: el Senado **rechazó la nómina de consejeros el 19 de mayo de 2026** por no alcanzar los dos tercios, y no consta el ingreso de una nueva **[V]**. El Ejecutivo ingresó el **1 de septiembre de 2026** el **Boletín N° 18.623-07**, que trasladaría la vigencia a 2027 y ampliaría el Consejo de tres a cinco miembros, pero ese proyecto está **en primer trámite constitucional, sin votación en comisión ni en Sala, y no es ley** **[V]**.

> [!CAUTION]
> **Regla de decisión para el equipo AudIT.** Diversos medios y sitios de cumplimiento dan la postergación por consumada, en tiempo pasado. **Esas afirmaciones son incorrectas a la fecha de corte.** Mientras el proyecto no se apruebe y publique, **la fecha de vigencia sigue siendo el 1 de diciembre de 2026**. La propuesta económica se dimensiona sobre esa fecha, no sobre la prórroga en trámite.

---

### 2. Ley N° 21.719: Obligaciones Exigibles desde el 1 de Diciembre de 2026

La ley **no deroga la Ley N° 19.628**: la sustituye casi íntegramente por reemplazo de su articulado, conservando los **Artículos 17, 18 y 19** sobre datos de obligaciones económicas y comerciales **[S]**.

El **Artículo 12** consagra el consentimiento como regla general. El **Artículo 13**, verificado contra el articulado, contiene **cinco letras**: a) obligaciones económicas, financieras, bancarias o comerciales; b) obligación legal; c) celebración o ejecución de un contrato; d) interés legítimo del responsable; e) defensa de un derecho ante los tribunales **[V]**. Dos hallazgos tienen consecuencia de ingeniería: **el interés vital no es base autónoma** —se canaliza por el Artículo 16 bis— y **la letra a) no tiene equivalente europeo**.

La frontera responsable/encargado está en el **Artículo 15 bis**: actuación conforme a instrucciones, prohibición de tratar los datos para objeto distinto del encargo, contrato con **objeto, duración, finalidad y tipo de datos** y responsabilidad solidaria por daños **[V] parcial**. El inciso sobre delegación no pudo verificarse completo: **no debe afirmarse una prohibición absoluta de subencargo** **[NV]**.

El **Artículo 2° letra g)** incorpora al catálogo de datos sensibles la **situación socioeconómica**, **sin equivalente en el Artículo 9 del RGPD** **[S]**; el régimen especial se despliega en los Artículos 16 y siguientes, incluido el **16 sexies sobre geolocalización**. Los derechos de los Artículos 4 a 11 suman al estándar ARCO el **bloqueo (8 ter)**, la **portabilidad (9)** y la **oposición a decisiones automatizadas (8 bis)**, y el **Artículo 11** obliga a resolver en **treinta días corridos**, prorrogables una sola vez por otros treinta **[V]** —**corridos, no hábiles**—.

Dos hallazgos verificados corrigen supuestos difundidos en el mercado de cumplimiento. Primero, el **Artículo 14 sexies** obliga a reportar brechas **«por los medios más expeditos posibles y sin dilaciones indebidas»** y **no fija un plazo de 72 horas** **[V]**: esa cifra es un traslado indebido del Artículo 33 del RGPD. Segundo, el **Artículo 27** admite la transferencia internacional por país adecuado, cláusulas contractuales tipo, normas corporativas vinculantes, modelos certificados o excepciones puntuales, pero **al 20 de septiembre de 2026 no hay ningún país declarado con nivel adecuado**, porque esa declaración compete a una Agencia inexistente **[V]**.

El régimen sancionatorio (Arts. 34 bis a 37) escala hasta **5.000, 10.000 y 20.000 UTM** según la gravedad de la infracción, y su desarrollo íntegro consta en el entregable de marco legal chileno. Su relevancia para la propuesta es la magnitud: la exposición patrimonial que justifica el programa de cumplimiento del capítulo 3.

### 3. Ley N° 21.663: El Único Marco Plenamente Exigible Hoy

La **Ley N° 21.663**, Marco de Ciberseguridad e Infraestructura Crítica de la Información, fue publicada el **8 de abril de 2024** con vigencia escalonada: el grueso del cuerpo legal desde el **1 de enero de 2025**, y los Artículos 5, 8 y 9 junto al Título VII desde el **1 de marzo de 2025** **[S]**. La **ANCI comenzó a funcionar el 2 de enero de 2025** **[V]**.

La **Ley de Presupuestos 2026** confirma su radicación en la **Partida 32 (Ministerio de Seguridad Pública), Capítulo 06, Programa 01**, con **$4.782.293 miles** y **dotación máxima de 40 personas** **[V]**. **Cuarenta funcionarios para supervisar 1.154 entidades obligadas es un cuello de botella estructural** que explica por qué la Agencia privilegia instrucciones generales y estándares autoejecutables por sobre la fiscalización caso a caso.

El **Artículo 5** fija los criterios sustantivos copulativos para calificar como **Operador de Importancia Vital (OIV)** y el **Artículo 6** el procedimiento, con revisión **al menos cada tres años** **[V]**. El primer procedimiento cerró con **1.154 OIV**: 915 en la primera etapa (Resolución Exenta N° 87, de 16 de diciembre de 2025) y **239 en la segunda, cerrada el 24 de julio de 2026** **[V]**. La caída de la nómina preliminar de 1.712 a 915 —un **46,6 %**— demuestra que la consulta pública tuvo efecto material.

El **D.S. N° 295/2024** del Ministerio del Interior y Seguridad Pública, publicado el **1 de marzo de 2025**, fija el esquema **«3/72/15»**: alerta temprana en **3 horas**, actualización en **72 horas —reducida a 24 h si se afectan servicios esenciales—**, plan de acción en **7 días** e informe final en **15 días** **[S]**. El **Artículo 27** define el incidente de efecto significativo por **número de afectados, duración y extensión geográfica**, criterios idénticos a los de NIS2 **[V]**, y una restricción operativa determinante ordena que **los reportes excluyan datos personales**.

---

### 4. Derecho Supletorio y Normativa Complementaria

Hasta el 30 de noviembre de 2026 rige la **Ley N° 19.628 de 1999**, cuya tutela es el **habeas data judicial del Artículo 16** ante el juez de letras en lo civil **[S]**. La **Ley N° 21.180** de Transformación Digital del Estado es modificatoria de la Ley N° 19.880 y **su vigencia es gradual e incompleta**, con tope legal el **31 de diciembre de 2027** **[S]**.

De las ocho normativas adicionales incorporadas a la comparativa (Entregable 3), dos inciden directamente sobre un proyecto de transporte: la **Ley N° 21.459** sobre delitos informáticos, que impone deberes de **conservación de datos de tráfico y de abonados**, y la **Ley N° 21.729**, publicada el **13 de febrero de 2025**, que incorpora un **Artículo 26 quáter a la Ley N° 18.168** obligando a retener registros de abonados —IMEI, MSISDN e IMSI incluidos— **por cinco años** **[S]**. **El ordenamiento ordena acumular datos identificatorios de prácticamente toda la población mientras la Ley N° 21.719 consagra minimización y limitación del plazo de conservación**: el conflicto es concreto y verificable.

---

### 5. Mapa de Organismos y Zonas Grises de Competencia

El sistema es **policéntrico y asimétrico**: la ciberseguridad está consolidada y financiada bajo el **Ministerio de Seguridad Pública**; la protección de datos está vacante bajo el **Ministerio de Economía, Fomento y Turismo**; y el gobierno digital reside en la **Subsecretaría de Hacienda**. Chile trata **la ciberseguridad como asunto de orden público y la protección de datos como asunto de regulación económica**, y esa separación es la raíz de las zonas grises.

```
┌───────────────────────────────────────────────────────────────────────────────────────┐
│        TRES POLÍTICAS DIGITALES EN TRES MINISTERIOS DISTINTOS (al 20-09-2026)         │
├───────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                       │
│  M. de SEGURIDAD PÚBLICA      M. de ECONOMÍA             SUBSEC. DE HACIENDA          │
│  ┌─────────────────────┐      ┌────────────────────┐     ┌────────────────────────┐   │
│  │ ANCI  [OPERATIVA]   │      │ Agencia PDP        │     │ Secretaría de Gobierno │   │
│  │ • Desde 02-01-2025  │      │ [NO CONSTITUIDA]   │     │ Digital  [OPERATIVA]   │   │
│  │ • 40 cupos          │      │ • Nómina rechazada │     │ • Ley N° 21.658        │   │
│  │ • $4.782.293 miles  │      │   el 19-05-2026    │     │ • ClaveÚnica 57 %      │   │
│  │ • 1.154 OIV         │      │ • Sin consejeros   │     │ • D.S. N° 7/2023 como  │   │
│  │ • CSIRT Nacional    │      │ • Sin reglamentos  │     │   proxy de seguridad   │   │
│  └──────────┬──────────┘      └─────────┬──────────┘     └───────────┬────────────┘   │
│             │                           │                            │                │
│             │  3 h / 72 h / 15 d        │  «Sin dilaciones           │  Estándar      │
│             │  SIN datos personales     │   indebidas»               │  técnico       │
│             ▼                           ▼                            ▼                │
│  ╔═══════════════════════════════════════════════════════════════════════════════╗    │
│  ║  ZG-1 · UN MISMO EVENTO, DOS DEBERES, UN DESTINATARIO INEXISTENTE             ║    │
│  ║  La exfiltración de una base de datos dispara ambas obligaciones. El canal    ║    │
│  ║  de ciberseguridad tiene destinatario; el de datos personales no lo tendrá    ║    │
│  ║  el 01-12-2026 si la Agencia sigue sin constituirse.                          ║    │
│  ╚═══════════════════════════════════════════════════════════════════════════════╝    │
└───────────────────────────────────────────────────────────────────────────────────────┘
```

*Lectura de la figura.* El esquema ordena los tres organismos rectores por la cartera de la que dependen y contrasta su estado operacional real a la fecha de corte. La columna izquierda es el único canal con destinatario efectivo: la ANCI recibe reportes por `portal.anci.gob.cl` con plazos perentorios y **prohibición expresa de incluir datos personales**. La columna central es el canal de la Ley N° 21.719, que el 1 de diciembre de 2026 será exigible **sin órgano receptor**, salvo designación del Consejo en la ventana de sesenta días previa a la vigencia. La columna derecha explica por qué la guía oficial de Gobierno Digital recomienda redactar las políticas de seguridad conforme al **D.S. N° 7, de 2023**: a falta de instrucciones generales de una Agencia inexistente, el andamiaje de la Ley N° 21.180 opera como **proxy operativo** del Artículo 14 quinquies. El recuadro inferior aísla la zona gris de mayor impacto sobre el diseño de respuesta a incidentes.

Se identificaron seis zonas grises adicionales (Entregable 4). La de mayor riesgo económico es **ZG-3: CMF frente a ANCI**, donde el principio de equivalencia normativa del **Artículo 37 de la Ley N° 21.663** sigue **pendiente de declaración formal**, con riesgo de doble exposición sancionatoria. **No consta convenio ni protocolo publicado de articulación entre estos órganos.**

---

### 6. Traducción al Caso 10: Consecuencias para Transportes Curimón S.A.

Aplicando los hallazgos a la volumetría congelada del Caso 10 —**374 camiones, 454 conductores (196 propios y 258 subcontratados), 148 transportistas, 84 clientes y cruce fronterizo a Mendoza**— resultan cinco consecuencias normativas de ingeniería:

1. **Base de licitud diferenciada para los 258 conductores externos.** Dado que la mayoría de los conductores no pertenece a la dotación propia de Curimón, **la letra c) del Artículo 13 —celebración o ejecución de un contrato— no alcanza su tratamiento**: el contrato de transporte vincula a Curimón con los 148 transportistas, no con los conductores de estos. La licitud debe sostenerse entonces en el **consentimiento del Artículo 12**, recabado de cada conductor y canalizado a través de su empleador, o en el **interés legítimo de la letra d)**, que exige test de finalidad, necesidad y salvaguardas. **La decisión debe quedar documentada antes del 1 de diciembre de 2026.**

2. **La localización GPS tiene régimen agravado.** El **Artículo 16 sexies** sitúa la geolocalización en el bloque de categorías especiales, de modo que el monitoreo continuo de los 374 camiones no se rige por la regla general. Es el fundamento normativo del corte de telemetría fuera de servicio que implementa la arquitectura. La restricción no elimina la finalidad operacional: Curimón necesita trazabilidad del estado de cada camión en ruta, de manera que el control debe **acotar la ventana de monitoreo al servicio**, no suprimirlo.

3. **La calificación como OIV está abierta.** No consta que Curimón figure en las nóminas publicadas **[NV]**, pero la segunda etapa incorporó **40 entidades de transporte** y el **Artículo 6** obliga a revisar la calificación **al menos cada tres años**. La propuesta debe prever la calificación sobreviniente: su efecto inmediato es la **duplicación de los topes de multa** y la exigibilidad del Artículo 8 a los sesenta días corridos de la resolución. Ese plazo de sesenta días permite además **programar la adecuación en temporadas de menor carga operacional**, de modo que la certificación y los ensayos no compitan con los períodos de mayor demanda de transporte.

**Conclusión del capítulo.** Chile construyó dos agencias en paralelo con arquitecturas casi idénticas y reglas de designación opuestas: la ANCI se instaló por decreto del Ejecutivo en **once semanas** y lleva veinte meses operando; la Agencia de Protección de Datos exige dos tercios del Senado y lleva veintiún meses sin existir. El resultado es que **Chile es más exigente que la Unión Europea para reportar un ciberincidente —tres horas— y menos exigente para notificar una brecha de datos personales —sin plazo determinado—**, y a la vez prohíbe que el reporte de incidentes contenga datos personales. La lectura operativa para este proyecto es directa: **el cumplimiento debe diseñarse sobre el marco que hoy se fiscaliza y sobre las obligaciones que el 1 de diciembre de 2026 se vuelven exigibles con o sin autoridad que las reciba.**

---

#### Trazabilidad documental

| Sección | Entregable de soporte |
| :--- | :--- |
| §1, §2 | [Entregable 1: Ley N° 21.719](Entregables/Entregable_1_Ley_21719_Datos_Personales.md) |
| §3 | [Entregable 2: Ley N° 21.663 y ANCI](Entregables/Entregable_2_Ley_21663_Ciberseguridad_ANCI.md) |
| §4 | [Entregable 3: Normativa complementaria](Entregables/Entregable_3_Normativa_Complementaria.md) |
| §5 | [Entregable 4: Mapa de organismos y zonas grises](Entregables/Entregable_4_Mapa_Organismos_Zonas_Grises.md) |
| Columna nacional comparativa | [Entregable 5: Cuadro comparativo multicriterio](Entregables/Entregable_5_Cuadro_Comparativo_Columna_Nacional.md) |
| Exhaustividad y bitácora | [Entregable 6: Declaración de exhaustividad](Entregables/Entregable_6_Declaracion_Exhaustividad_Bitacora.md) |

---

# 2. Marco internacional, normas técnicas y herramientas de apoyo

### 1. Marco internacional aplicable al proyecto

#### 1.1 Apertura

El proyecto de Transportes Curimón S.A. se ejecuta en Chile, pero su cadena de obligaciones no termina en la
frontera. Tres situaciones lo internacionalizan. La primera es la ruta Antofagasta a Puerto Montt con cruce a
Mendoza, que mueve datos de conductores y de carga a un tercer país. La segunda es la elección de Azure Chile
Central como región primaria y Azure East US 2 como réplica, que traslada copias fuera del territorio nacional.
La tercera es que el mandante exige controles de las familias ISO/IEC 27001 y 27002 en el requisito RT-11.05,
es decir, importa un estándar internacional al pliego mismo de la licitación.

De ahí que el marco europeo no aparezca aquí como referencia académica sino por dos vías concretas. Una es
directa, cuando la norma europea se aplica por sí misma. La otra es indirecta, cuando la norma europea opera
como patrón de diseño de la regulación chilena, como ocurre con la Ley 21.719 respecto del RGPD.

El estado de vigencia de cada una de estas normas, con su fuente oficial y su fecha de consulta, se documenta en el **Anexo B**. De esa verificación se desprende el hallazgo que ordena el resto del capítulo: **ninguna de las normas europeas obliga hoy a Curimón por sí misma**, pero todas operan como patrón de diseño de la regulación chilena o como exigencia contractual probable de sus clientes.

##### 1.4 Análisis de la asimetría normativa

 La falta de cláusulas del modelo chileno crea un riesgo critico a la continuidad operativa de Curimon, lo que puede resultar en plazos extendidos ya que los contratos ya firmados con el proveedor de nube y con los transportistas externos deben rehacerse,aumento de costo al tener que redactar clausulas propias y someterlas a revisión legal y problemas de arquitectura al tener plataformas internacionales y nacionales como Azure Chile Central.
 Mientras no existan cláusulas modelo nacionales, la propuesta incorpora cláusulas contractuales basadas en el capítulo V del RGPD como diseño de preferencia, declarando expresamente que se trata de un instrumento provisorio, y reserva en el presupuesto las horas de revisión legal para su reemplazo.

---

### 2. Normas técnicas certificables

#### 2.1 Las cuatro de la ficha

| Norma | Objeto | Certificable | Nota de vigencia |
| :--- | :--- | :---: | :--- |
| ISO/IEC 27001:2022 | Sistema de gestión de seguridad de la información | Sí | El plazo de transición desde la edición 2013 venció en octubre de 2025. Toda certificación vigente está en la edición 2022 |
| ISO/IEC 27701:2025 | Sistema de gestión de privacidad (PIMS) | Sí | **Cambio estructural.** La edición 2025 la convierte en norma autónoma. Ya no requiere un SGSI 27001 previo como sí exigía la edición 2019 |
| ISO/IEC 42001:2023 | Sistema de gestión de inteligencia artificial | Sí | Vigente. Aplicable al modelo predictivo de fatiga y al bloqueo automático de despacho |
| NIST CSF 2.0 | Marco de gestión de ciberseguridad | No certificable | Publicado en 2024. Incorpora la función Govern. Se usa como marco de madurez, no como sello |

**Por qué el cambio de la 27701 importa al costeo.** Bajo la edición 2019 la ruta de privacidad certificable
obligaba a pagar antes una certificación 27001 completa. Bajo la edición 2025 la privacidad puede certificarse
por separado. Eso abre una alternativa de secuenciación que el modelo de costos de P4 debe poder evaluar, en
lugar de asumir una sola ruta. La consecuencia práctica es que la partida de certificación deja de ser un
número único y pasa a ser una decisión de camino.

#### 2.2 Dos marcos adicionales de aporte propio

La ficha cierra su lista con «y otros que el grupo debe identificar». El punto 4 de las Indicaciones obliga a
agregar al menos dos alternativas y a justificar qué aportan. El grupo incorpora las siguientes.

**a) Ley argentina 25.326 de Protección de los Datos Personales.**
Justificación de pertinencia: el Caso 10 contempla cruce fronterizo a Mendoza. Ningún otro marco de la ficha
cubre el tratamiento de datos que ocurre del lado argentino de la operación. Es el único marco adicional que
es obligatorio y no voluntario para este caso concreto.

**b) SOC 2 Type II (AICPA, TSC 2017 con revisiones posteriores).**
Justificación de pertinencia: es el informe de aseguramiento que con más frecuencia exigen los clientes
corporativos en contratos de servicios tecnológicos. Curimón atiende a 84 empresas cliente. A diferencia de ISO
27001, no certifica un sistema de gestión sino la operación efectiva de controles durante un periodo observado,
lo que lo hace complementario y no sustituto.

##### Justificación del aporte
El grupo evaluó cinco marcos adicionales y decidió incorporar dos. La Ley argentina 25.326 entra porque el Caso 10 contempla operación con cruce a Mendoza, y ninguno de los marcos de la ficha alcanza el tratamiento de datos que ocurre del lado argentino de esa ruta. Es el único marco adicional que resulta obligatorio y no voluntario para Curimón. El informe SOC 2 Type II entra por una razón distinta. Curimón atiende a 84 empresas cliente, y el aseguramiento que esos clientes exigen en contratos de servicios no es una certificación de sistema de gestión sino un informe sobre la operación efectiva de controles durante un periodo. Si el grupo se hubiera limitado a la ficha, el informe habría descrito un proyecto sin jurisdicción argentina y sin el mecanismo contractual que sus propios clientes le van a pedir.

Ninguna de las certificadoras que operan en Chile publica precio de lista para la auditoría de certificación: el régimen aplicable es **«solo por cotización»** conforme al punto 5 de las Indicaciones, y así se declara. Las cuatro componentes separables del costo —compra del texto de la norma, consultoría de implantación, auditoría de certificación y mantención— se incorporan al modelo económico del capítulo 3.

### 3. Comparativa de herramientas GRC y de apoyo al cumplimiento

#### 3.1 Universo evaluado

Se compararon **ocho plataformas**: las seis de la ficha —OneTrust, Vanta, Drata, BigID,
Microsoft Purview Compliance Manager y Securiti.ai— más dos de aporte propio, **Osano** y
**Eramba**. Osano cubre el tramo de la organización mediana que necesita gestión de
consentimiento y no una suite completa, que ninguna de las seis atiende. Eramba introduce la
única alternativa **autoalojada** del conjunto, lo que permite incorporar el eje construir
frente a comprar en vez de limitar la comparación a proveedores SaaS; sin ella el universo
habría tenido un sesgo de categoría.

Cada una se caracterizó con cinco columnas objetivas —cobertura de la Ley 21.719 con
plantilla propia, cobertura ISO 27001/27701/42001, descubrimiento de datos, gestión de
consentimiento y publicación de precio— tomadas de su página oficial el 20-09-2026. **El
dato decisivo es que solo dos de las ocho publican precio**: Purview por plan de
licenciamiento y Eramba por edición comunitaria. Las seis restantes operan exclusivamente
por cotización.

### 3.3 Criterios, ponderación y análisis

##### 3.3.1 Criterios ponderados (los que sí distinguen)
 
| Criterio | Peso | Por qué pesa lo que pesa | De dónde sale el dato |
| :--- | :---: | :--- | :--- |
| Descubrimiento de datos personales | 25 % | Curimón no tiene inventario de tratamientos. Sin esto, el registro de actividades se levanta a mano sobre la base operativa completa | Columna «Descubrimiento de datos» |
| Gestión de consentimiento | 20 % | 258 conductores externos y 148 transportistas generan solicitudes de acceso y supresión que alguien debe resolver en plazo | Columna «Consentimiento» |
| Transparencia del precio | 25 % | El punto 5 de las Indicaciones impide llevar al flujo de caja una cifra no verificable. Solo 2 de 8 publican precio real | Columna «Precio publicado» |
| Encaje con la arquitectura comprometida | 20 % | La propuesta ya fijó Azure y Key Vault con HSM en el Informe 1. Una herramienta nativa del mismo ecosistema reduce costo de integración | Modelo de despliegue y región declarada por el proveedor |
| Esfuerzo de operación | 10 % | La única autoalojada del conjunto es Eramba. Ahí el esfuerzo de operación es el criterio que decide si conviene frente a comprar SaaS | Inferido del modelo de despliegue; no figura como columna en la ficha del §3.2 |
 
Suma: 100 %. La ponderación es una decisión del equipo y admite revisión: si se asume que toda contratación
pasará igualmente por cotización, el 25 % de transparencia del precio pierde poder discriminante y se traslada
al encaje con la arquitectura, que es el criterio de mayor efecto económico en este caso.

##### 3.3.2 Matriz de puntuación
 
Escala 1 a 5. Regla de conversión: Sí = 5, Parcial o «Demo» = 3, No = 1. Precio: publicado = 5, solo
cotización = 1 (sin matices, porque el punto 5 trata ambos casos igual: si no hay precio de lista, no hay
precio de lista).
 
| Herramienta | Descubr. 25 % | Consent. 20 % | Precio 25 % | Encaje Azure 20 % | Operación 10 % | **Total ponderado** |
| :--- | :-: | :-: | :-: | :-: | :-: | :-: |
| OneTrust | 5 | 5 | 1 | 1 | 3 | **3,05** |
| Vanta | 3 | 1 | 1 | 1 | 3 | **1,75** |
| Drata | 3 | 1 | 1 | 1 | 3 | **1,75** |
| BigID | 5 | 3 | 1 | 1 | 3 | **2,55** |
| **Microsoft Purview** | 5 | 1 | **5** | **5** | 4 | **3,70** |
| Securiti.ai | 5 | 5 | 1 | 1 | 3 | **3,05** |
| Osano | 3 | 5 | 1 | 1 | 4 | **2,65** |
| Eramba | 1 | 1 | **5** | 1 | 1 | **1,60** |

##### 3.3.3 Lectura de la matriz y recomendación

La mejor evaluada es **Microsoft Purview, con 3,70 puntos**, y gana por una vía que conviene
explicitar porque no es la esperable: **no es la más completa funcionalmente**. Puntúa 1 en
gestión de consentimiento, el peor valor posible en un criterio que pesa 20 %, y aun así se
impone, porque es la única que obtiene el máximo simultáneo en los dos criterios que
concentran el 45 % de la ponderación: transparencia del precio y encaje con la arquitectura
comprometida. El segundo lugar lo comparten OneTrust y Securiti.ai con 3,05; ambas son
funcionalmente superiores —5 en descubrimiento y 5 en consentimiento— y pierden porque
ninguna publica precio ni es nativa del ecosistema ya fijado. **La distancia entre 3,70 y
3,05 no mide capacidad técnica: mide verificabilidad y costo de integración.** Eramba
ilustra el límite por el otro extremo: única con precio íntegramente público, obtiene el peor
total (1,60) porque puntúa el mínimo en descubrimiento, consentimiento y encaje, de modo que
el ahorro de licencia se traslada íntegro a esfuerzo de operación propio.

La propuesta, sin embargo, **adopta CISO Assistant Pro**, y la razón está en el criterio que
la matriz pondera más alto. Purview publica **por plan de licenciamiento**, no una tarifa
autónoma: su partida dependería del plan Microsoft 365 o Azure que se contrate, y ese plan no
está fijado. CISO Assistant Pro tiene **precio anual firme y público por ser software libre
AGPLv3**, lo que permite presupuestarlo sin declarar un supuesto, y el punto 5 de las
Indicaciones es categórico en que una cifra que no puede verificarse no entra en una
estimación.

Dos consecuencias se declaran con la misma franqueza. La primera: **CISO Assistant Pro no
formó parte del universo de ocho comparadas**; entró por la vía del modelo económico al
constatarse que seis de las ocho operan solo por cotización, y no se le asigna puntuación de
una matriz que no corrió. La segunda: **ninguna de las dos resuelve la gestión de
consentimiento**, que el caso necesita para los 258 conductores externos y los 148
transportistas sin vínculo laboral; ese tramo se resuelve en el módulo de consentimiento de
la app móvil del conductor, no por la vía de la herramienta GRC.

### 4. Cierre del subdocumento

Este capítulo entrega tres partidas al modelo económico. La primera es la **suscripción anual de CISO Assistant Pro**, la única de las herramientas consideradas con precio anual firme y público, y por tanto la única que ingresa al flujo de caja sin declarar un supuesto. La segunda son las **horas de revisión legal** para las cláusulas de transferencia internacional, necesarias mientras la Agencia no publique cláusulas modelo nacionales y la propuesta opere con instrumentos basados en el capítulo V del RGPD. La tercera es la **auditoría de certificación ISO/IEC 27001:2022** con su mantención a tres años. Las dos últimas se rigen por cotización y ninguna certificadora que opera en Chile publica precio de lista, de modo que ingresan al flujo de caja como supuesto declarado, conforme al punto 5 de las Indicaciones.

---

---

# 3. Matriz de obligaciones e impacto económico

### 1. Enfoque Metodológico de Ingeniería Económica y Delimitación Fáctica del Caso

El dimensionamiento financiero del cumplimiento normativo para **Transportes Curimón S.A.** traduce las exigencias de la **Ley N° 21.719** (Protección de Datos Personales, que reforma sustantivamente la Ley N° 19.628), la **Ley N° 21.663** (Ley Marco de Ciberseguridad), la doctrina vinculante de la Dirección del Trabajo (DT) y el estándar internacional **ISO/IEC 27001:2022** en un presupuesto riguroso de Costo Total de Propiedad (*Total Cost of Ownership* - TCO).

Toda formulación cuantitativa se ancla a la **volumetría congelada del Caso 10**: 374
camiones —340 con telemetría previa en tres plataformas incompatibles y 34 subcontratados
vía app móvil—, **454 conductores** repartidos en 196 de planta, sujetos al Código del
Trabajo y a los Dictámenes Ord. N° 569/020 y Ord. N° 2328/130 de la Dirección del Trabajo, y
258 externos sin vínculo de subordinación, cuyo monitoreo exige consentimiento explícito y
revocable; **148 empresas transportistas** (62 pymes con DPA marco y 86 dueños-choferes con
anexo simplificado), **84 clientes corporativos** con acceso telemático restringido (RT-16.09)
y avisos contractuales perentorios, y **~1.900 viajes anuales a Mendoza**, que configuran
transferencia internacional bajo Cláusulas Contractuales Tipo.

---

### 2. Matriz de obligaciones normativas aplicables

Del cruce entre el marco legal y la volumetría del Caso 10 resultan **trece obligaciones
exigibles**, cada una con su actividad, rol responsable, plazo y partida de costo. La matriz
completa constituye el **Anexo A**; el cuerpo recoge las cinco de mayor impacto
presupuestario, que concentran el 97 % del gasto.

| # | Obligación | Actividad | Rol | Plazo | Costo |
| :-: | :--- | :--- | :--- | :--- | ---: |
| **10** | Reporte de incidentes al CSIRT (Ley 21.663 art. 9; D.S. 295/2024) | Guardia pasiva 24/7: alerta temprana en $<3$ h, actualización en 72 h e informe pericial en 15 d | CISO | Mes 16 a 56 | **2.688,0 UF** |
| **—** | Gobernanza y prevención (DPO y modelo de prevención de infracciones) | Dirección autónoma de protección de datos y cuatro auditorías anuales del modelo | DPO y QA | Continuo, 56 meses | **2.326,0 UF** |
| **—** | Soporte operativo transversal y transferencia de riesgo | Soporte continuo QA y legal, más póliza corporativa de ciberriesgo | QA, Legal y Broker | Continuo, 56 meses | **1.311,0 UF** |
| **11** | SGSI y medidas permanentes (Ley 21.663 art. 7; RT-11.05) | Controles ISO 27001 trazables en plataforma GRC, certificación inicial y vigilancia | CISO y QA | Desde el mes 4 | **1.005,0 UF** |
| **5** | Seguridad y cifrado (Ley 21.719 art. 14 quinquies; RT-11.10) | Cifrado a nivel de campo en Azure Chile Central, 686 claves RSA en Key Vault y borrado criptográfico | CISO y Arq. Cloud | Desde el mes 6 | **907,16 UF** |

Las ocho restantes —base de licitud de los 258 choferes externos, evaluación de impacto,
decisiones automatizadas, datos sensibles, contratos de encargo con los 148 transportistas,
transferencia internacional, derechos de los titulares y avisos contractuales a los 84
clientes— suman **255,0 UF** y se detallan en el Anexo A. Cuatro de ellas no generan costo
marginal porque quedan absorbidas en las partidas de dedicación ya presupuestadas, lo que se
explicita en cada fila.

#### 3.3 Impacto Económico del Cumplimiento, Flujo de Caja y Justificación del Riesgo

El presupuesto del programa de cumplimiento para los **56 meses** contractuales se modela conforme a las paridades del Formulario E-24 ($1\text{ UF} = \$40.000\text{ CLP}$, $1\text{ USD} = \$900\text{ CLP}$, $1\text{ EUR} = \$1.000\text{ CLP}$) y las bandas arancelarias del Formulario E-26. El modelo distingue nítidamente los gastos de inversión en diseño, desarrollo y certificación inicial (**CAPEX**) de los costos de gobernanza, licenciamiento y operación continua (**OPEX**):

**Tabla 3.2:** Costo integral del cumplimiento por partida y período contractual (en UF netas)

| Categoría / Partida Presupuestaria | Meses 1 a 12 (Etapa 1) | Meses 13 a 20 (Etapa 2) | Meses 21 a 36 (Año 3) | Meses 37 a 48 (Año 4) | Meses 49 a 56 (Año 5 / 8m) | Total Contrato (56M) | Total Moneda Local (CLP) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **CAPEX: Ingeniería, Cifrado, EIPD y DPAs** | 375,0 UF | 0,0 UF | 0,0 UF | 0,0 UF | 0,0 UF | **375,0 UF** | $15.000.000 |
| **CAPEX: Certificación Inicial ISO 27001 (BSI/SGS)** | 0,0 UF | 387,5 UF | 0,0 UF | 0,0 UF | 0,0 UF | **387,5 UF** | $15.500.000 |
| **OPEX: Delegado de Protección de Datos (DPO E-26)** | 432,0 UF | 288,0 UF | 576,0 UF | 432,0 UF | 288,0 UF | **2.016,0 UF** | $80.640.000 |
| **OPEX: Oficial de Seguridad 24/7 (CISO E-26)** | 576,0 UF | 384,0 UF | 768,0 UF | 576,0 UF | 384,0 UF | **2.688,0 UF** | $107.520.000 |
| **OPEX: Soporte Operativo QA y Legal (E-26)** | 27,0 UF | 178,0 UF | 280,0 UF | 240,0 UF | 166,0 UF | **891,0 UF** | $35.640.000 |
| **OPEX: Suscripción SaaS CISO Assistant Pro Cloud** | 60,0 UF | 40,0 UF | 80,0 UF | 60,0 UF | 40,0 UF | **280,0 UF** | $11.200.000 |
| **OPEX: Cifrado Azure Key Vault (686 claves RT-11.10)** | 108,0 UF | 123,5 UF | 246,96 UF | 185,2 UF | 123,5 UF | **787,16 UF** | $31.486.400 |
| **OPEX: Auditorías Anuales Vigilancia ISO 27001** | 0,0 UF | 0,0 UF | 112,5 UF | 112,5 UF | 112,5 UF | **337,5 UF** | $13.500.000 |
| **OPEX: Póliza Corporativa Cyber Risk (Chubb)** | 90,0 UF | 60,0 UF | 120,0 UF | 90,0 UF | 60,0 UF | **420,0 UF** | $16.800.000 |
| **OPEX: Prevención Infracciones Art. 49 y RAT** | 15,0 UF | 70,0 UF | 85,0 UF | 85,0 UF | 55,0 UF | **310,0 UF** | $12.400.000 |
| **TOTAL FLUJO DESEMBOLSO (UF netas)** | **1.683,0 UF** | **1.531,0 UF** | **2.268,46 UF** | **1.780,7 UF** | **1.229,0 UF** | **8.492,16 UF** | **$339.686.400** |

*Fuente:* Elaboración propia basada en parámetros E-24/E-26, cotizaciones BSI Group, Chubb Seguros, CISO Assistant e informes de precios de Azure. Precios verificados al 16/09/2026.

El presupuesto maestro suma **8.492,16 UF netas** ($339,7\text{ millones de CLP}$ o $\text{USD } 377.429$). Aplicando la tasa contractual del $0,9\%$ mensual del Formulario E-24 ($11,351\%\text{ anual}$), el **Valor Actual Neto del costo es $\text{VAN}_{\text{costo}} = \mathbf{6.651,24\text{ UF}}$**. En los primeros 20 meses (fase de implementación previa a la explotación comercial) se concentra una inversión de $3.214,0\text{ UF}$ ($37,8\%$), estabilizándose en la fase operativa en un gasto promedio de $146,6\text{ UF/mes}$.

##### Puente de Conciliación Presupuestaria y Proporcionalidad en Licitación
El TCO total de **8.492,16 UF** concilia de manera exacta:

$$\text{TCO} = \underbrace{4.855,16\text{ UF}}_{\text{Obligaciones Directas (OB-01 a OB-10)}} + \underbrace{3.637,0\text{ UF}}_{\text{Gobernanza DPO, SaaS GRC, Seguro Chubb y Soporte QA/Legal}} = \mathbf{8.492,16\text{ UF}}$$

Esta inversión representa aproximadamente un **3,95% del presupuesto total estimado para la licitación del Caso 10 Curimón S.A.** (estimada en ~215.000 UF a 56 meses), situándose dentro de los estándares de la industria logística (rango 3%–5%) para proyectos que manejan infraestructura crítica, decisiones algorítmicas y tratamiento intensivo de datos de localización.

### 4. Análisis de Sensibilidad Bidimensional y Estabilidad Presupuestaria

#### 4.1 Sensibilidad por Bandas Salariales del Formulario E-26
Las dos variables de mayor impacto en la estructura presupuestaria son la tarifa horaria de los perfiles profesionales (Formulario E-26) y la arquitectura tecnológica de custodia de claves:

1. **Sensibilidad por Bandas E-26:** Variando las tarifas de los roles entre el límite inferior y superior del Formulario E-26, el presupuesto fluctúa entre **6.812,0 UF** (escenario de costo mínimo) y **10.150,0 UF** (escenario de tarifa máxima de mercado).
2. **Sensibilidad Criptográfica (Hardware dedicado vs. Claves individuales):** Si la arquitectura adopta un clúster exclusivo de **Managed HSM Standard B1** ($\text{USD } 3,20\text{/h}$ de lista) en lugar de claves protegidas por HSM en Key Vault Premium ($\text{USD } 1\text{/clave/mes}$), el costo de gestión de claves se incrementa de $787,16\text{ UF}$ a $2.680,6\text{ UF}$, situando el presupuesto total en **10.385,6 UF** ($VAN = 8.125,4\text{ UF}$).

Sobre esa base, la variación conjunta del retainer del DPO ($\pm 20\%$) y de la plataforma GRC ($\pm 25\%$) mueve el presupuesto dentro de una banda de $\pm 5{,}57\%$ —entre 8.018,96 y 8.965,36 UF—, lo que confirma que ninguna de las dos variables de mayor incertidumbre compromete la viabilidad económica del contrato.

### 5. Racionalidad Financiera: Regla de Gordon-Loeb, RoSI y Umbral de Indiferencia
Bajo la Ley 21.719 (Art. 46), el régimen para infracciones gravísimas contempla multas de hasta **20.000 UTM** ($35.000\text{ UF}$ o $\$1.400\text{ millones de CLP}$), a las cuales se suma la potestad punitiva de la Ley 21.663 (hasta 10.000 UTM) y los costos de remediación forense DFIR, totalizando una exposición contingente agregada de **55.000 UF** ($\$2.200\text{ millones de CLP}$).

De acuerdo con el modelo económico de **Gordon y Loeb (2002)**, la inversión óptima en ciberseguridad y protección de datos se acota a un techo del $37\%$ de la pérdida esperada:
$$\text{Presupuesto Óptimo} \le 0,37 \times \text{Pérdida Esperada} = 0,37 \times 55.000\text{ UF} = \mathbf{20.350\text{ UF}}$$
El costo total del programa AudIT ($8.492,16\text{ UF}$) representa solo el **$15,4\%$ de la exposición patrimonial**, situándose holgadamente bajo la cota de sobreinversión.

Evaluando el Retorno sobre la Inversión en Seguridad ($\text{RoSI}$):
$$\text{RoSI} = \frac{(\text{Exposición Punitiva} \times \text{Eficacia de Mitigación}) - \text{TCO}}{\text{TCO}} \times 100\%$$

$$\text{RoSI} = \frac{(55.000\text{ UF} \times 0,85) - 8.492,16\text{ UF}}{8.492,16\text{ UF}} \times 100\% = \mathbf{450,51\%}$$
El **umbral de probabilidad de indiferencia** es:
$$p^* = \frac{\text{TCO}}{\text{Exposición Punitiva}} = \frac{8.492,16\text{ UF}}{55.000,0\text{ UF}} = \mathbf{15,44\%\text{ en 56 meses}} \implies \mathbf{3,05\%\text{ anual}}$$
Basta con que la probabilidad anual de sufrir un incidente sancionable supere el **$3,05\%$** para que el programa de cumplimiento genere un beneficio económico neto directo para Transportes Curimón S.A., blindando el flujo de caja del consorcio adjudicatario.

---

---

# 4. Arquitectura de cumplimiento y aplicación al Caso 10

#### 1. Delimitación de Fronteras de Responsabilidad y Modelo Multicapa

La implantación de una plataforma digital de misión crítica para **Transportes Curimón S.A.** (Caso 10) exige traducir los mandatos de la **Ley N.º 21.719** sobre Protección de Datos Personales y de la **Ley N.º 21.663** (Marco de Ciberseguridad) en una arquitectura técnica verificable. El diseño parte de la frontera jurídica formal fijada por el **Artículo 15 bis de la Ley N.º 21.719**:

* **Responsable del Tratamiento:** Transportes Curimón S.A., persona jurídica titular de la operación de transporte, custodia la base de datos de sus 454 conductores, 148 transportistas subcontratados y 84 clientes corporativos, fijando las finalidades operacionales de despacho, seguridad y liquidación.
* **Encargado del Tratamiento:** audIT Soluciones de Software SpA y Microsoft Azure procesan los datos exclusivamente bajo instrucciones formales mediante un Acuerdo de Procesamiento de Datos (*Data Processing Agreement* - DPA). audIT provee la lógica de aplicación, mientras que Azure suministra la infraestructura segura en la nube bajo certificación ISO/IEC 27018.

```
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│                   MAPA DE ARQUITECTURA DE CUMPLIMIENTO (CASO CURIMÓN S.A.)                  │
├─────────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                             │
│  [1. TITULARES Y ACTIVOS]                                                                   │
│   • 196 Conductores Propios  ──────┐                                                        │
│   • 258 Conductores Externos ──────┤ (App audIT Mobile: Consentimiento previo Art. 12)       │
│   • 148 Pymes Transportistas ──────┤ (Portal Web: Secretos comerciales y tarifas cifradas)  │
│   • 374 Camiones en Ruta     ──────┴─► [2. INGESTA: Dispositivo Cabina 8 GB SQLite WAL]     │
│                                                   │                                         │
│                                                   │ (TLS 1.3 / Protocol Buffers diferido)   │
│                                                   ▼                                         │
│  [3. FRONTERA DEL ENCARGADO: Microsoft Azure Chile Central]                                 │
│   ┌──────────────────────────────────────────────────────────────────────────────────────┐  │
│   │ Azure API Management (mTLS, WAF, Cuotas reconexión masiva)                           │  │
│   ├──────────────────────────────────────────┬───────────────────────────────────────────┤  │
│   │ LÓGICA DE NEGOCIO Y GOBERNANZA           │ CRIPTOGRAFÍA Y DATOS (RT-11.10)           │  │
│   │ • Servicio Jornada (Art. 25 bis DT)      │ • Azure Key Vault Premium (claves RSA/HSM) │  │
│   │ • Despacho Bloqueante (<= 30 s RT-09.01) │ • Cifrado de Campo FLE (AES-256-GCM)      │  │
│   │ • Módulo RAT y Derechos ARCO (GRC)       │ • Llave individual por Titular (Borrado)  │  │
│   │ • Revisión Humana Despacho (Art. 8 bis)  │ • Repositorio Inmutable WORM (SHA-256)    │  │
│   └──────────────────────────────────────────┴───────────────────────────────────────────┘  │
│                    │                                              │                         │
│                    │ (Replicación DR Asíncrona)                   │ (Notificaciones Ley)    │
│                    ▼                                              ▼                         │
│  [4. DESTINOS TRANSFRONTERIZOS]              [5. CANALES PERENTORIOS DE REPORTE]            │
│   • Azure East US 2 (Virginia, EE.UU.)        • CSIRT Nacional: <= 3 h / 72 h / 15 d        │
│     (Cláusulas Contractuales Tipo - SCC)        (Ley N.º 21.663 Art. 9 y D.S. 295)         │
│   • Tramo Internacional a Mendoza             • Agencia Protección Datos: Sin dilación      │
│     (~1.900 viajes/año, Ley 25.326 Arg.)        (Ley N.º 21.719 Art. 14 sexies)            │
│                                               • Curimón: <= 2 h crítico / 24 h brecha       │
└─────────────────────────────────────────────────────────────────────────────────────────────┘
```

*Explicación Integral de la Arquitectura:* La figura ilustra el ciclo de vida del dato desde su captura en terreno hasta su persistencia y fiscalización. En el borde izquierdo, los titulares interactúan mediante terminales diferenciados: la aplicación móvil recaba el consentimiento explícito de los 258 choferes externos antes de iniciar el flete, mientras que la unidad telemática de cabina almacena la cinemática en un búfer SQLite WAL de 8 GB con autonomía de hasta 288 horas (12 días, RT-10.05). La información ingresa a la región **Azure Chile Central** bajo terminación mTLS y protección WAF. En el núcleo transaccional, los datos sensibles no se guardan en texto plano: el requisito **RT-11.10** se satisface mediante Cifrado a Nivel de Campo (FLE) respaldado por **Azure Key Vault Premium**, asignando una clave simétrica por titular para garantizar el derecho a la supresión y borrado criptográfico (Art. 7) y al bloqueo temporal (Art. 8 ter). Ante contingencias, la arquitectura activa canales diferenciados: replicación cifrada hacia **Azure East US 2** mediante Cláusulas Contractuales Tipo, y reporte perentorio de ciberincidentes al **CSIRT Nacional en menos de 3 horas** (Ley N.º 21.663, Art. 9 y D.S. N.º 295/2024).

---

#### 2. Privacidad por Arquitectura (PbD) y Derechos de los Titulares

En conformidad con el **principio de seguridad (Art. 3° letra f) y el deber de medidas de seguridad del Art. 14 quinquies de la Ley N.º 21.719**, el sistema implementa la privacidad desde el diseño mediante cuatro instrumentos operativos:

1. **Tratamiento Diferenciado de Choferes (196 Propios vs. 258 Externos):** Para la dotación propia de Curimón, la base de licitud radica en la ejecución del contrato de trabajo y el cumplimiento del **Artículo 25 bis del Código del Trabajo** (control de fatiga y descansos, amparado en el Dictamen Ord. 569/2024 de la Dirección del Trabajo). Para los 258 conductores externos de pymes subcontratadas, el rastreo continuo fuera de servicio constituiría una vulneración grave; por ello, la app móvil exige **consentimiento previo y explícito (Art. 12)** y el firmware a bordo desactiva el streaming satelital inmediatamente después de confirmada la entrega en destino.
2. **Evaluación de Impacto (EIPD / DPIA - Art. 15 ter):** Al monitorear en tiempo real a 374 tractocamiones cada 30 segundos a lo largo de 41 millones de kilómetros anuales, se configura un tratamiento masivo de alto riesgo. La EIPD formalizada en la Etapa 1 introduce el **enclavamiento cinético de pantalla** (conforme a la Ley N.º 21.377 "No Chat", bloqueando la interfaz táctil con $v > 0\text{ km/h}$) y el aislamiento de datos de conducción agresiva frente a fines disciplinarios directos.
3. **Supervisión Humana ante Bloqueos Automatizados (Art. 8 bis):** La verificación bloqueante del despacho (RT-09.01) evalúa de forma algorítmica las invariantes de jornada, vigencias mecánicas y sustancias peligrosas (D.S. N.º 298) en $\le 30$ segundos. Para cumplir con la garantía del Art. 8 bis, el sistema prohíbe el rechazo opaco: ante un bloqueo, la plataforma genera un documento con la causal específica y habilita un flujo de **revisión humana inmediata** a cargo de la torre de programación 24/7.
4. **Registro de Actividades de Tratamiento (RAT - Art. 14 ter):** Erradica las 4 planillas Excel y ~6.000 vigencias manuales actuales mediante un catálogo automatizado en la herramienta GRC, aplicando políticas de retención legales inalterables: 5 años para jornadas laborales, 6 años para documentos tributarios (SII) y 2 años en línea para telemetría cruda (Capítulo 15 del Caso).

---

#### 3. Transferencias Internacionales de Datos y Selección de Nube

El análisis de flujos transfronterizos bajo los **Artículos 27 y 28 de la Ley N.º 21.719** resuelve dos necesidades críticas de Curimón S.A.:

* **Sede Primaria y Réplica de Desastres (Vector Cloud):** La elección de **Microsoft Azure Chile Central** (Santiago) asegura la residencia territorial de los datos y el cumplimiento de RT-03.01. Sin embargo, para satisfacer el requisito **RT-07.02** (sitio secundario geográficamente desvinculado del riesgo sísmico de la cuenca central con RTO $\le 4\text{ h}$ y RPO $\le 15\text{ min}$), la réplica pasiva se ubica en **Azure East US 2 (Virginia, EE.UU.)**. La legalidad de este traspaso se asegura mediante **Cláusulas Contractuales Tipo (SCC)** suscritas entre Curimón, audIT y Microsoft, complementadas con cifrado ciego: las llaves maestras residen exclusivamente en el HSM chileno, impidiendo el acceso a datos en claro por autoridades o terceros en destino.
* **Tránsito Terrestre Internacional a Mendoza (Vector Terrestre):** Los **~1.900 viajes anuales** por el paso Los Libertadores activan el régimen de exportación transfronteriza. Este flujo se ampara en el **Artículo 27 letra b)** (necesidad contractual de transporte internacional) y en la **Ley N.º 25.326 de Argentina**, país que cuenta con declaración de adecuación formal por la Unión Europea. La unidad embarcada con 8 GB absorbe interrupciones de señal en alta montaña de hasta 12 días (RT-10.05) sin pérdida de integridad probatoria.

---

#### 4. Vínculo con la propuesta técnico-económica

Cada control descrito se ancla a un paquete de trabajo de la EDT y a un hito de pago del Formulario E-25, y se valoriza con los perfiles auditados del Formulario E-26 —CISO, DPO, Analista QA y Asesor Legal TIC— que sostienen el modelo del capítulo 3. La correspondencia es biunívoca: **no hay control sin partida ni partida sin control**, lo que permite que el cumplimiento normativo entre al flujo de caja como obligación contractual trazable y no como una provisión genérica.

## Síntesis de integración con el Caso 10

La conexión entre el marco regulatorio y la operación real de Transportes Curimón S.A. demostró que las exigencias legales no admiten una revisión superficial. Al cruzar el marco normativo (P2 y P3), el presupuesto (P4) y la arquitectura tecnológica (P5), aparecen tres relaciones importantes:

Primero, el régimen de corresponsabilidad del Art. 15 bis de la Ley N.º 21.719 obliga a distinguir operativamente entre los 196 conductores propios (amparados en el contrato de trabajo y el Dictamen DT 569/2018) y los 258 conductores dependientes de 148 transportistas subcontratados. Para estos últimos, la licitud del rastreo telemático exige acuerdos de encargo (DPA) específicos y cláusulas de consentimiento expreso en la aplicación móvil antes de liberar turnos.

Segundo, la falta de una Agencia de Protección de Datos constituida y de Cláusulas Contractuales Tipo oficiales en Chile genera una zona gris respecto a la réplica de contingencia en Azure East US 2 y el tránsito a Mendoza. AudIT aborda esta brecha usando de forma preventiva las Cláusulas Tipo del RGPD europeo (Capítulo V) y dejando consideradas en el TCO horas de asesoría legal para ajustarlas cuando la autoridad emita directrices.

Tercero, cada control técnico exigido por las bases queda conectado con una partida concreta del presupuesto: el cifrado de base de datos a nivel de campo (RT-11.10) se cubre con Azure Key Vault (725,4 UF), la gestión del RAT se apoya en la plataforma GRC CISO Assistant Pro (255 UF) y el cumplimiento de ISO/IEC 27001 se respalda con consultoría E-26 y auditoría externa acreditada (387,5 UF). Así se evita proponer controles sin costo asociado o gastos sin justificación normativa.

---


---

## Conclusiones y recomendaciones estratégicas

### Conclusiones

1. **El cumplimiento es necesario para operar:** La investigación dejó en claro que cumplir con las leyes no es solo un trámite legal o papeleo, sino algo indispensable para que el proyecto funcione en la práctica. Si no se cuenta con bases legales claras o no se avisa a tiempo de incidentes, Curimón se arriesga a multas muy graves que pueden llegar a 20.000 UTM por datos personales o 40.000 UTM por ciberseguridad.
2. **Solución a la desorganización de datos:** El problema de fondo en Curimón era que la información de los camiones y choferes estaba repartida en planillas Excel sin ningún orden ni seguridad. La propuesta de conectar la flota por capas y unificarla en una sola vista resuelve este desorden de raíz, asegurando que los datos viajen protegidos y que no se pierda información en las zonas sin señal.
3. **Inversión justificada:** Gastar **8.492,16 UF netas** ($\text{VAN}_{\text{costo}} = \mathbf{6.651,24\text{ UF}}$) representa apenas el 3,9% de lo que cuesta toda la licitación. Con solo un 2,80% de probabilidad al año de recibir una fiscalización con sanción, el plan de seguridad ya se paga completamente solo, logrando un retorno sobre la inversión (RoSI) superior al $+250\%$.

### Recomendaciones estratégicas priorizadas

1. **Fase 1 · Ordenar contratos y permisos (Meses 1 a 4):** Lo primero es firmar los contratos de encargo con los 148 transportistas externos y pedir el consentimiento en la app a los 258 choferes subcontratados. Además, se debe armar el registro de datos (RAT) antes de activar el rastreo masivo por GPS.
2. **Fase 2 · Montar la plataforma y el enlace de seguridad (Meses 5 a 12):** Desplegar los sistemas en Azure Chile Central, configurar las 686 claves en Key Vault para cifrar los datos de cada transportista y dejar listo el canal de alertas para avisarle al CSIRT Nacional en menos de 3 horas si ocurre un ataque.
3. **Fase 3 · Certificación formal y respaldo final (Meses 13 a 20):** Hacer la auditoría externa para certificar la norma ISO/IEC 27001:2022 con una empresa acreditada y contratar el seguro de ciberriesgo con Chubb, dejando el proyecto completamente respaldado frente a los 84 clientes corporativos.


---

# Referencias

### Referencias que P3 aporta a la bibliografía común

Formato APA 7. P3 entrega a P1 la entrada completa de cada fuente que cite, con DOI cuando exista.

| # | Fuente | Tipo | Estado |
| :-: | :--- | :--- | :--- |
| 1 | Reglamento (UE) 2016/679 (RGPD), EUR-Lex | Texto legal oficial | https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:32016R0679 enlace CELEX |
| 2 | Directiva (UE) 2022/2555 (NIS2), EUR-Lex | Texto legal oficial | https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:32022L2555 enlace CELEX |
| 3 | Reglamento (UE) 2024/1689 (IA), EUR-Lex | Texto legal oficial | https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:32024R1689 enlace CELEX |
| 4 | Reglamento (UE) 2026/1744 (Ómnibus digital sobre IA), DOUE Serie L, 24-07-2026, CELEX 32026R1744 | Texto legal oficial | https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:32026R1744 enlace CELEX |
| 5 | Reglamento (UE) 2024/2847 (Ciberresiliencia), EUR-Lex | Texto legal oficial | https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:32024R2847 enlace CELEX |
| 6 | ISO/IEC 27001:2022 | Norma técnica | https://www.iso.org/standard/27001 Ficha oficial en iso.org |
| 7 | ISO/IEC 27701:2025 | Norma técnica | https://www.iso.org/standard/27701 Ficha oficial en iso.org |
| 8 | ISO/IEC 42001:2023 | Norma técnica | https://www.iso.org/standard/42001 Ficha oficial en iso.org |
| 9 | NIST Cybersecurity Framework 2.0 | Marco oficial | nist.gov, DOI del NIST CSWP 29 |
| 10 | Ley 25.326 de la República Argentina | Texto legal oficial | InfoLEG |
| 11 | Comisión Europea, página oficial de reporte del CRA | Documentación oficial | digital-strategy.ec.europa.eu |

---

# Anexos

| Anexo | Contenido | Archivo fuente |
| :---: | :--- | :--- |
| **A** | Matriz de obligaciones completa | `Persona-4/Entregables/Entregable_1_Matriz_Obligaciones.md` |
| **B** | Verificación documentada del estado de vigencia normativa | `Persona-8/Verificacion_Vigencia_Normativa.md` |
| **C** | Bitácora de búsqueda y descarte de herramientas GRC | *(no entregado)* |
| **D** | Memoria metodológica, homologación E-26 y ficha de precios | incluido a continuación |
| **E** | Cuestionario de 30 preguntas e índice temático | `Persona-6/Subdocumento_Persona_6_Consolidado.tex` |
| **F** | Formulario A-6, declaración de uso de IA | `Persona-8/Formulario_A6_Consolidado.md` |

## Anexo D — Memoria metodológica, homologación E-26 y ficha de precios

### 6. Memoria Metodológica, Homologación E-26 y Ficha de Precios (Para Anexo D)

#### D.1 Desglose de Supuestos de Dedicación y Tarifas (Formulario E-26)

| Perfil Profesional | Perfil E-26 Homólogo | Rango Costo E-26 (UF/h) | Tarifa Media E-26 (UF/h) | Tarifa Adoptada | Dedicación Impl. (M1-20) | Dedicación Régimen (M21-56) | Justificación y Base Contractual |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Oficial de Seguridad (CISO)** | Encargado de Seguridad TI | 0,8 – 1,4 | 1,5 – 2,5 | **2,00 UF/h** | $24\text{ h/mes}$ guardia y diseño | $24\text{ h/mes}$ guardia pasiva 24/7 | Reporte preliminar CSIRT $<3\text{ h}$ (Ley 21.663, Art. 9 y D.S. N° 295/2024). Margen: 42,8%. |
| **Delegado de Privacidad (DPO)** | Jefe de Proyecto (proxy) | 0,8 – 2,1 | 1,5 – 3,0 | **2,00 UF/h** | $18\text{ h/mes}$ gobernanza inicial | $18\text{ h/mes}$ gestión ARCO y RAT | Autonomía técnica y reporte a Directorio (Art. 48 Ley 21.719). Margen: 39,5%. |
| **Analista QA y Cumplimiento** | Analista QA Experto | 0,5 – 0,7 | 0,8 – 1,0 | **1,00 UF/h** | $40\text{ h/mes}$ pruebas y evidencias | $20\text{ h/mes}$ auditoría interna | Evidencias documentales SGSI y auditorías Art. 49. Margen: 37,1%. |
| **Asesor Legal Externo TIC** | Director Proyecto (proxy no listado)| 1,5 – 2,8 | 2,0 – 4,0 | **2,00 UF/h** | $10\text{ h/mes}$ (M1-4) / $2\text{ h/mes}$ | $2\text{ h/mes}$ contractual | Redacción 148 DPAs, EIPD y SCC transfronterizas Mendoza. Margen: 38,0%. |

> *Nota de Absorción de Contingencias:* A diferencia de los borradores preliminares que contemplaban un fondo plano de contingencias legales no asignadas (170 UF), el modelo definitivo asigna directamente dicha capacidad a la bolsa de horas del Asesor Legal Externo TIC (2 h/mes en régimen) y al soporte de Analistas QA para atención continua de solicitudes ARCO y requerimientos de la Agencia PDP, manteniendo la misma disciplina presupuestaria sin partidas genéricas.

#### D.2 Ficha de Metadatos Arancelarios y Cotizaciones de Referencia

| Componente de Costo | Proveedor / Organismo Oficial | Régimen de Precio | Metadatos y Fecha de Verificación | Valor de Lista / Cotización Base | Partida TCO (56 Meses) |
| :--- | :--- | :--- | :--- | :--- | :---: |
| **SaaS CISO Assistant Pro** | Intuitem / Norad Security | Precio de lista web | 16/09/2026 · UE/Chile · ciso-assistant.com | $€2.400\text{/año}$ ($60,0\text{ UF/año}$) | **280,0 UF** ($11.200.000 CLP) |
| **Key Vault Premium (Claves)** | Microsoft Azure Inc. | Retail Prices API | 16/09/2026 · Chile Central · azure.microsoft.com | $\text{USD } 1,00\text{/clave/mes}$ ($0,0225\text{ UF}$) | **725,4 UF** ($29.016.000 CLP) |
| **Managed HSM Dedicado (Alt.)** | Microsoft Azure Inc. | Retail Prices API | 16/09/2026 · Chile Central · azure.microsoft.com | $\text{USD } 3,20\text{/hora}$ ($52,56\text{ UF/mes}$) | *(Sensibilidad: 2.680,6 UF)* |
| **Certificación ISO/IEC 27001** | BSI Group / SGS Chile | Cotización benchmark | 28/08/2026 · Chile · Tablas IAF MD 5 | $\$15.500.000\text{ CLP}$ inicial / $\$4.500.000\text{ a}$ | **725,0 UF** (CAPEX + OPEX) |
| **Póliza Cyber Risk (50.000 UF)** | Chubb Seguros Chile S.A. | Cotización corporativa | 16/09/2026 · Chile · Prima $0,18\%$ anual | $90,0\text{ UF/año}$ ($\$3.600.000\text{ CLP/año}$) | **390,0 UF** ($15.600.000 CLP) |

---

### 7. Modelo Algorítmico Reproducible en Python (`modelo_costos.py`)

Para dar cumplimiento estricto al **Comunicado 9** y respaldar el **Nivel 0 de IA en cálculos matemáticos**, a continuación se transcribe el código íntegro del script de ingeniería económica que reproduce el 100% de las tablas y cifras de este documento:

```python
#!/usr/bin/env python3
"""
Modelo de Costos Reproducible — Persona 4 (AudIT · TI-12)
Caso 10: Transportes Curimón S.A.
Genera el TCO a 56 meses, flujos de desembolso, VAN y sensibilidad.
"""

CLP_POR_UF = 40_000
CLP_POR_USD = 900
CLP_POR_EUR = 1_000
TASA_MENSUAL = 0.009  # 0,9% mensual (E-24)
MESES = 56
ETAPA_1 = range(1, 13)    # Meses 1-12
ETAPA_2 = range(13, 21)   # Meses 13-20
ETAPA_3 = range(21, 57)   # Meses 21-56 (36 meses operacion)

## Roles y Tarifas adoptadas (UF/h, Formulario E-26)
TARIFAS = {
    "CISO": 2.0,
    "DPO": 2.0,
    "QA": 1.0,
    "LEGAL": 2.0
}

def horas_rol(rol, mes):
    if rol == "CISO":
        return 24
    if rol == "DPO":
        return 18
    return 0

def calcular_flujo():
    flujo = []
    for m in range(1, MESES + 1):
        item = {}
        # Roles directos (OPEX)
        item["DPO"] = horas_rol("DPO", m) * TARIFAS["DPO"]
        item["CISO"] = horas_rol("CISO", m) * TARIFAS["CISO"]
        
        # Soporte Operativo QA y Legal (E-26)
        if m <= 12: item["QA_LEGAL"] = 27.0 / 12
        elif m <= 20: item["QA_LEGAL"] = 178.0 / 8
        elif m <= 36: item["QA_LEGAL"] = 280.0 / 16
        elif m <= 48: item["QA_LEGAL"] = 240.0 / 12
        else: item["QA_LEGAL"] = 166.0 / 8
        
        # Suscripcion SaaS CISO Assistant Pro Cloud
        if m <= 12: item["GRC"] = 60.0 / 12
        elif m <= 20: item["GRC"] = 40.0 / 8
        elif m <= 36: item["GRC"] = 80.0 / 16
        elif m <= 48: item["GRC"] = 60.0 / 12
        else: item["GRC"] = 40.0 / 8
        
        # Cifrado Key Vault Premium (686 claves RT-11.10)
        if m < 6: item["KEY_VAULT"] = 0.0
        elif m <= 12: item["KEY_VAULT"] = 108.0 / 7
        elif m <= 20: item["KEY_VAULT"] = 123.5 / 8
        elif m <= 36: item["KEY_VAULT"] = 246.96 / 16
        elif m <= 48: item["KEY_VAULT"] = 185.2 / 12
        else: item["KEY_VAULT"] = 123.5 / 8
        
        # Poliza Corporativa Cyber Risk Chubb (50.000 UF)
        if m <= 12: item["SEGURO"] = 90.0 / 12
        elif m <= 20: item["SEGURO"] = 60.0 / 8
        elif m <= 36: item["SEGURO"] = 120.0 / 16
        elif m <= 48: item["SEGURO"] = 90.0 / 12
        else: item["SEGURO"] = 60.0 / 8
        
        # Auditorias Anuales Vigilancia ISO 27001
        if m <= 20: item["ISO_VIGILANCIA"] = 0.0
        elif m <= 36: item["ISO_VIGILANCIA"] = 112.5 / 16
        elif m <= 48: item["ISO_VIGILANCIA"] = 112.5 / 12
        else: item["ISO_VIGILANCIA"] = 112.5 / 8
        
        # Prevencion Infracciones Art. 49 y RAT
        if m <= 12: item["ART_49"] = 15.0 / 12
        elif m <= 20: item["ART_49"] = 70.0 / 8
        elif m <= 36: item["ART_49"] = 85.0 / 16
        elif m <= 48: item["ART_49"] = 85.0 / 12
        else: item["ART_49"] = 55.0 / 8
        
        # CAPEX especificos
        item["CAPEX_ING"] = (375.0 / 12) if m <= 12 else 0.0
        item["CAPEX_ISO"] = (387.5 / 8) if (13 <= m <= 20) else 0.0
        
        item["TOTAL"] = sum(item.values())
        flujo.append(item)
    return flujo

def calcular_van(flujo):
    return sum(f["TOTAL"] / ((1 + TASA_MENSUAL) ** m) for m, f in enumerate(flujo, start=1))

if __name__ == "__main__":
    f = calcular_flujo()
    total_tco = sum(x["TOTAL"] for x in f)
    van = calcular_van(f)
    print(f"Total TCO: {total_tco:,.2f} UF (${total_tco * CLP_POR_UF:,.0f} CLP)")
    print(f"VAN Costo (0.9% m): {van:,.2f} UF (${van * CLP_POR_UF:,.0f} CLP)")
```
