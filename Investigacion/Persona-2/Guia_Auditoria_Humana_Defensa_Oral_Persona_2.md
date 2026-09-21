# Guía de Auditoría Humana y Defensa Oral — Persona 2
## Balotario de Preguntas Críticas sobre el Marco Legal Chileno

**Asignatura:** Taller de Formulación de Proyectos Informáticos (ICI-5444) · Escuela de Informática, PUCV  
**Empresa Consultora:** AudIT (Empresa 10)  
**Rol:** Persona 2 · *Chilean Regulatory Research Specialist*  
**Fecha de corte:** 20 de septiembre de 2026

> [!CAUTION]
> **Regla del Comunicado 9.** El docente puede interrogar a **cualquier** integrante sobre **cualquier** parte del trabajo. Persona 2 debe poder explicar **sin apoyo** las diez respuestas de esta guía, y muy especialmente **por qué una afirmación está marcada [V] y otra [NV]**. Una marca de certeza que no se sabe justificar es peor que no haberla puesto.

---

## P1 · ¿Está vigente la Ley N° 21.719? Responda con precisión.

**No.** Fue publicada el **13 de diciembre de 2024** pero **no está vigente**. Su **Artículo primero transitorio** difiere la entrada en vigor «hasta el día primero del mes vigésimo cuarto posterior a su publicación», esto es, el **1 de diciembre de 2026**. Hasta el 30 de noviembre de 2026 sigue aplicándose la **Ley N° 19.628 de 1999**.

**Si preguntan por la postergación:** el Gobierno ingresó el **1 de septiembre de 2026** el **Boletín N° 18.623-07**, que la trasladaría a 2027, pero está **en primer trámite constitucional, sin comisión asignada, sin urgencia y sin ninguna votación**. **No es ley.** Muchos medios lo dan por hecho en tiempo pasado; esas notas son incorrectas.

> **Trampa habitual:** decir «24 meses después de la publicación, o sea el 13 de diciembre de 2026». **Es incorrecto.** La fórmula legal apunta al **día PRIMERO del mes vigésimo cuarto**, no a los 24 meses exactos. Son 12 días de diferencia y es un error que figura en otro capítulo del informe (ver DC-01 de las Directrices).

---

## P2 · ¿Cuál es la diferencia entre responsable y encargado, y por qué importa para Curimón?

**Responsable** (Art. 2° letra n): quien «decide acerca de los fines y medios del tratamiento» → **Transportes Curimón S.A.**, que decide qué se monitorea, para qué y por cuánto tiempo.

**Encargado:** la ley chilena **no crea una definición autónoma** como el Art. 4.8 del RGPD; usa la fórmula **«mandatario o encargado»**, regulada en el **Artículo 15 bis** → **AudIT y el proveedor de nube**, que tratan datos solo bajo instrucciones documentadas.

**Por qué importa para Curimón:** los **258 conductores subcontratados no son trabajadores de Curimón**. El contrato de transporte vincula a Curimón con los **148 transportistas**, no con sus conductores. Por eso **la base de licitud del Art. 13 letra c) —ejecución de un contrato— no los alcanza**, y hay que recurrir al consentimiento del Art. 12 o al interés legítimo de la letra d), con su test de finalidad, necesidad y salvaguardas.

> **Si preguntan por el subencargo:** el fragmento recuperado dice «El encargado no podrá delegar parte o la totalidad del encargo», pero **no pudimos verificar el inciso completo**, y la técnica legislativa estándar sugiere que continúa con una excepción por autorización expresa. **Por eso el informe NO afirma una prohibición absoluta de subencargo.** Está marcado [NV] deliberadamente.

---

## P3 · ¿En cuánto tiempo hay que notificar una brecha de datos personales en Chile?

**No hay plazo en horas.** El **Artículo 14 sexies** obliga a reportar **«por los medios más expeditos posibles y sin dilaciones indebidas»**. Este dato está **verificado [V]** contra el articulado.

**La cifra de 72 horas que circula en el mercado es incorrecta:** es un traslado indebido del **Artículo 33 del RGPD**. La ley chilena tomó la fórmula cualitativa europea **pero no el plazo numérico**. Varios proveedores comerciales lo afirman; el informe los cita **para refutarlos**, no como respaldo.

> **No confundir con ciberseguridad.** Bajo la **Ley N° 21.663** sí hay plazos perentorios: **3 horas** de alerta temprana, **72 horas** de actualización —**reducidas a 24 horas si se afectan servicios esenciales**—, **7 días** de plan de acción y **15 días** de informe final, fijados por el **D.S. N° 295/2024**. Son dos regímenes distintos con destinatarios distintos.

---

## P4 · Existe la Agencia de Protección de Datos. ¿Verdadero o falso?

**Falso.** La ley la crea (Arts. 30 y siguientes) pero **no está constituida**. El **Senado rechazó la nómina de consejeros el 19 de mayo de 2026** por no alcanzar los dos tercios, y no consta nueva nómina.

**El bloqueo es aritmético, no técnico:** exigir dos tercios del Senado sobre **tres nombres votados individualmente**, para cargos con dedicación exclusiva y fuertes incompatibilidades, produjo un universo de elegibles demasiado estrecho para un Senado fragmentado. Por eso el proyecto de septiembre sustituye ese mecanismo por una **nómina única de cinco**.

**Tres consecuencias que sí hay que saber:**
1. **Ningún país está declarado con nivel adecuado de protección**, porque esa declaración es competencia de la Agencia (Art. 28). Afecta directamente las transferencias a Argentina del Caso 10.
2. **No se encontró evidencia de que se haya dictado ningún reglamento** de la ley entre diciembre de 2024 y septiembre de 2026. Hay además una **dependencia circular**: el Art. 26 exige informe previo de la Agencia para el reglamento de cesión de datos, y sin Consejo no hay informe.
3. **La tutela administrativa de los Arts. 41 a 43 será inoperante** aunque la ley entre en vigor.

> **Contraste que cierra el argumento:** la **ANCI se instaló por decreto del Ejecutivo en once semanas** —del DFL N° 1-21.663 del 24 de diciembre de 2024 al Decreto N° 479 publicado el 11 de marzo de 2025, 77 días— y lleva **veinte meses operando**. La Agencia de Datos lleva **veintiún meses sin existir**. Misma arquitectura institucional, reglas de designación opuestas.

---

## P5 · ¿Qué es un OIV y podría serlo Curimón?

**Operador de Importancia Vital.** Los **criterios sustantivos son copulativos y están en el Artículo 5** de la Ley N° 21.663 **[V]**: (a) que la provisión del servicio **dependa de redes y sistemas informáticos**, y (b) que su afectación tenga **impacto significativo** en la seguridad pública, la continuidad de servicios esenciales o el ejercicio de funciones estatales. El **Artículo 6** regula el procedimiento y la **revisión al menos cada tres años**.

> **Corrección a la literatura:** parte de la doctrina especializada —incluida IAPP— atribuye los criterios al Artículo 6. **Es impreciso**, y lo verificamos contra el texto oficial.

**Universo actual: 1.154 OIV.** 915 en la primera etapa (Res. Ex. N° 87, de 16 de diciembre de 2025) y 239 en la segunda, cerrada el 24 de julio de 2026.

**¿Curimón?** **No consta que figure en las nóminas publicadas — está marcado [NV]**, no afirmamos ni que lo sea ni que no lo sea. Pero la segunda etapa incorporó **40 entidades de transporte terrestre, aéreo, ferroviario y marítimo**, y la calificación se revisa cada tres años. **Por eso la propuesta prevé el escenario de calificación sobreviniente**, cuyo efecto económico inmediato es la **duplicación de los topes de multa** (de 20.000 a 40.000 UTM en gravísimas) y la exigibilidad del paquete reforzado del Art. 8 a los 60 días corridos de la resolución.

---

## P6 · ¿Por qué la caída de 1.712 a 915 instituciones es relevante?

Porque **demuestra que la consulta pública tuvo efecto material y no fue un trámite formal**: **797 instituciones lograron excluirse, un 46,6 %**.

Hay dos lecturas adicionales:
- **Los servicios digitales son 413 de las 915 de la primera etapa, un 45 %.** El perímetro OIV está **sesgado hacia proveedores tecnológicos más que hacia infraestructura física**, lo que sitúa a las empresas de software y servicios TI en el centro del régimen.
- **La estructura duplicadora de multas explica por qué se disputó tanto.** Ser calificado OIV duplica la exposición sancionatoria; por eso la consulta pública fue un ejercicio con consecuencia económica directa, no un trámite.

---

## P7 · ¿Por qué incluyeron ocho normativas adicionales si la ficha pedía dos?

Porque el criterio de selección **no fue la relevancia genérica sino el eje diferenciador**: cada norma entra por **la variable de la matriz comparativa que solo ella hace variar**.

| Norma | Eje que solo ella aporta |
| :--- | :--- |
| Ley N° 21.096 | **Rango constitucional** — sin ella, «jerarquía normativa» no tiene variación |
| Ley N° 20.285 | **Finalidad opuesta**: publicidad frente a confidencialidad |
| Ley N° 21.459 | **Consecuencia penal** |
| PNCS 2023-2028 | **Soft law** con metas fechadas |
| RAN 20-10 de la CMF | **Anticipación regulatoria** — cuatro años antes de la Ley N° 21.663 |
| Ley N° 21.521 y NCG | **Portabilidad con infraestructura obligatoria (APIs)** |
| Ley N° 21.729 | **Colisión normativa vigente** |
| Ley N° 21.658 / N° 21.680 / NCh-ISO | Estabilidad institucional / base nacional / voluntariedad |

**También descartamos con criterio explícito:** la Ley N° 21.046 (su objeto es velocidad mínima de Internet, sin contenido de datos), la Ley N° 19.223 (derogada, degradada a nota histórica) y la Ley N° 19.799 (firma electrónica: regula validez probatoria, no derechos del titular). **Documentar los descartes es lo que impide acusar la comparativa de selección arbitraria.**

---

## P8 · Deme un ejemplo concreto de contradicción dentro del propio ordenamiento chileno.

**La Ley N° 21.729, publicada el 13 de febrero de 2025.** Introduce un **Artículo 26 quáter a la Ley N° 18.168** que obliga a las concesionarias de telecomunicaciones a mantener registros de abonados —nombre, domicilio, cédula, **IMEI, MSISDN e IMSI**— **almacenados por cinco años**.

**Una ley de 2025 ordena retener datos identificatorios de prácticamente toda la población por cinco años, mientras la Ley N° 21.719 consagra minimización y limitación del plazo de conservación.** El plazo es además notablemente más extenso que los estándares europeos posteriores a *Digital Rights Ireland*.

**Un segundo caso:** la **Ley N° 21.459** sobre delitos informáticos impone a los proveedores deberes de **conservación de datos de tráfico y de abonados**, en la misma tensión.

> **Conclusión que conviene enunciar:** el sistema chileno **sigue produciendo obligaciones de acumulación al mismo tiempo que promete minimización**. El 1 de diciembre de 2026 no resuelve esa contradicción; solo la hace exigible.

---

## P9 · ¿Qué es la zona gris ZG-1 y cómo afecta al diseño del sistema?

**Es la brecha que es simultáneamente incidente de ciberseguridad y de datos personales.**

| | Ley N° 21.663 | Ley N° 21.719 |
| :--- | :--- | :--- |
| Destinatario | CSIRT Nacional (ANCI) | Agencia PDP |
| Plazo | **3 horas** | «Sin dilaciones indebidas» |
| Contenido | **Debe EXCLUIR datos personales** | Notificación **por causa de** esos datos |
| Destinatario real | **Existe** | **No existirá el 01-12-2026 si la Agencia sigue vacante** |

**Impacto de diseño:** la arquitectura de respuesta a incidentes debe contemplar **dos flujos de información separados en origen**, no uno reutilizado, **porque un flujo debe excluir precisamente lo que el otro exige**.

**Impacto jurídico:** si el Boletín N° 18.623-07 no se aprueba antes del 1 de diciembre, existirá **una obligación exigible sin órgano receptor**.

---

## P10 · ¿Por qué hay tantas afirmaciones marcadas [NV]? ¿No debilita eso el informe?

**Al contrario: es lo que lo hace defendible.**

El portal oficial **Ley Chile (BCN) no fue recuperable**: sirve su articulado por JavaScript y devolvía «Este proceso demora demasiado»; el *endpoint* `obtxml` **entregó normas distintas de las solicitadas** —devolvió el Decreto N° 419 de 2024 para dos `idNorma` diferentes—; y el **PDF oficial de la Ley N° 21.719 se trunca en la página 20 de 34, justo antes de las disposiciones transitorias**.

**La alternativa a marcar [NV] habría sido afirmar con seguridad cosas que no verificamos.** El sistema de tres niveles permite que el lector —y el auditor— sepa exactamente qué sostiene cada afirmación.

**Y la declaración de exhaustividad es deliberadamente NEGATIVA:** decimos que **la lista no es exhaustiva**, con confianza **ALTA** en el estrato legal, **MEDIA-BAJA** en el infralegal y **BAJA** sobre la actividad reglamentaria en curso. El fundamento es empírico: el barrido de ANCI y CMF **produjo hallazgos que no estaban en el listado de partida** —el D.S. N° 295/2024, nueve resoluciones exentas y el Reglamento de Defensa Nacional—, **lo que demuestra que esa capa estaba subrepresentada**.

---

## Datos que Persona 2 Debe Saber de Memoria

| Dato | Valor |
| :--- | :--- |
| Publicación / vigencia de la Ley N° 21.719 | **13-12-2024** / **01-12-2026** (Art. primero transitorio) |
| Publicación / vigencia de la Ley N° 21.663 | **08-04-2024** / **01-01-2025** y **01-03-2025** |
| Rechazo de la nómina de consejeros | **19 de mayo de 2026**, por no alcanzar los dos tercios |
| Boletín de postergación | **N° 18.623-07**, ingresado el **01-09-2026**, **sin votar** |
| Inicio de funciones de la ANCI | **2 de enero de 2025** |
| Presupuesto y dotación de la ANCI 2026 | **$4.782.293 miles** · **40 personas** · Partida 32, Cap. 06, Prog. 01 |
| Total de OIV | **1.154** (915 + 239) |
| Esquema de reporte de incidentes | **3 h / 72 h (24 h si hay servicio esencial) / 7 d / 15 d** |
| Plazo de respuesta a solicitudes de titulares | **30 días CORRIDOS + 30** (Art. 11) |
| Escala de multas de datos | **5.000 / 10.000 / 20.000 UTM** + 2 % / 4 % de ingresos |
| Escala de multas de ciberseguridad | PSE 5.000/10.000/20.000 · **OIV el doble: 10.000/20.000/40.000 UTM** |
| Bases de licitud del Art. 13 | **Cinco letras; el interés vital NO es base autónoma** |
| Dato sensible sin equivalente en el RGPD | **Situación socioeconómica** |
| Multas hoy exigibles | **1 a 10 UTM** (Ley N° 19.628, Art. 16), ante juez civil |

> [!IMPORTANT]
> **Si no recuerda una cifra, diga que está en el Entregable correspondiente y explique el razonamiento.** El Comunicado 9 evalúa que el integrante **pueda reconstruir el razonamiento**, no que memorice. Lo que **no** es admisible es inventar un número o afirmar con seguridad algo marcado **[NV]** en el propio informe.
