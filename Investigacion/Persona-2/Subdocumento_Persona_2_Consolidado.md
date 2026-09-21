# Capítulo 2: Marco Legal Chileno de Protección de Datos y Ciberseguridad

## Licitación TFEP-01/2026 · Caso 10: Transportes Curimón S.A. · Empresa Consultora AudIT

**Asignatura:** Taller de Formulación de Proyectos Informáticos (ICI-5444) · Escuela de Informática, PUCV  
**Tema de Investigación:** TI-12 · *Cumplimiento normativo en proyectos TIC: Ley 21.719, Ley 21.663 (ANCI) y marco internacional*  
**Rol Responsable:** Persona 2 (*Chilean Regulatory Research Specialist*)  
**Fecha de corte de la investigación:** 20 de septiembre de 2026  
**Extensión actual:** ~2.020 palabras de prosa (≈3,0 págs.) · Formato de integración para el informe final  
**Presupuesto asignado por P1:** 2,0–2,5 págs. — **reserva de recorte declarada** (ver nota editorial)

> [!NOTE]
> **Nota editorial para Persona 1 (control de extensión).** Este capítulo excede en ~0,5 página el presupuesto asignado. El recorte está **pre-identificado y ordenado por prioridad de eliminación**, de modo que P1 pueda ajustarlo sin romper la cadena argumental: (1) el detalle del régimen sancionatorio del §2, cuyo desarrollo íntegro está en el Entregable 1; (2) el desglose de etapas de calificación de OIV del §3, íntegro en el Entregable 2; (3) los ítems 3 y 4 del §6, que son aplicaciones derivadas y no hallazgos. **No son recortables** la asimetría del §1, el Artículo 14 sexies del §2, el esquema 3/72/15 del §3 ni la figura del §5, por ser los hallazgos que sostienen los capítulos de P4 y P5.

> [!IMPORTANT]
> **Convención de certeza aplicada en todo el capítulo.** **[V]** = verificado contra fuente primaria (Diario Oficial, ficha oficial de tramitación del Senado, repositorio normativo de la ANCI, Ley de Presupuestos de DIPRES). **[S]** = apoyado solo en fuente secundaria (síntesis de la Biblioteca del Congreso Nacional, estudios jurídicos, compilaciones especializadas). **[NV]** = no verificado. Ninguna afirmación de este capítulo eleva su nivel de certeza por conveniencia narrativa.

---

## 1. La Asimetría Regulatoria que Condiciona Toda la Propuesta

Al 20 de septiembre de 2026 el ordenamiento chileno presenta una asimetría que define el diseño de cumplimiento de este proyecto: **la Ley N° 21.663 está plenamente operativa, mientras que la Ley N° 21.719 está publicada pero no vigente, y la autoridad que ella crea no existe**.

La **Ley N° 21.719**, que regula la protección y el tratamiento de los datos personales y crea la Agencia de Protección de Datos Personales, fue publicada en el Diario Oficial el **13 de diciembre de 2024**. Su **Artículo primero transitorio** difiere la entrada en vigencia «hasta el día primero del mes vigésimo cuarto posterior a su publicación», esto es, el **1 de diciembre de 2026** —**72 días después de la fecha de corte**— y ordena que entretanto «seguirá operando la antigua ley N° 19.628» **[V]**. Se corrige aquí un error de atribución frecuente: **la fecha de vigencia está en el Artículo primero transitorio, no en el tercero**, que fija las reglas de la primera designación del Consejo Directivo **[S]**.

La **Agencia de Protección de Datos Personales no está constituida**: el Senado **rechazó la nómina de consejeros el 19 de mayo de 2026** por no alcanzar los dos tercios, y no consta el ingreso de una nueva **[V]**. El Ejecutivo ingresó el **1 de septiembre de 2026** el **Boletín N° 18.623-07**, que trasladaría la vigencia a 2027 y ampliaría el Consejo de tres a cinco miembros, pero ese proyecto está **en primer trámite constitucional, sin votación en comisión ni en Sala, y no es ley** **[V]**.

> [!CAUTION]
> **Regla de decisión para el equipo AudIT.** Diversos medios y sitios de cumplimiento dan la postergación por consumada, en tiempo pasado. **Esas afirmaciones son incorrectas a la fecha de corte.** Mientras el proyecto no se apruebe y publique, **la fecha de vigencia sigue siendo el 1 de diciembre de 2026**. La propuesta económica se dimensiona sobre esa fecha, no sobre la prórroga en trámite.

---

## 2. Ley N° 21.719: Obligaciones Exigibles desde el 1 de Diciembre de 2026

La ley **no deroga la Ley N° 19.628**: la sustituye casi íntegramente por reemplazo de su articulado, conservando los **Artículos 17, 18 y 19** sobre datos de obligaciones económicas y comerciales **[S]**.

El **Artículo 12** consagra el consentimiento como regla general. El **Artículo 13**, verificado contra el articulado, contiene **cinco letras**: a) obligaciones económicas, financieras, bancarias o comerciales; b) obligación legal; c) celebración o ejecución de un contrato; d) interés legítimo del responsable; e) defensa de un derecho ante los tribunales **[V]**. Dos hallazgos tienen consecuencia de ingeniería: **el interés vital no es base autónoma** —se canaliza por el Artículo 16 bis— y **la letra a) no tiene equivalente europeo**.

La frontera responsable/encargado está en el **Artículo 15 bis**: actuación conforme a instrucciones, prohibición de tratar los datos para objeto distinto del encargo, contrato con **objeto, duración, finalidad y tipo de datos** y responsabilidad solidaria por daños **[V] parcial**. El inciso sobre delegación no pudo verificarse completo: **no debe afirmarse una prohibición absoluta de subencargo** **[NV]**.

El **Artículo 2° letra g)** incorpora al catálogo de datos sensibles la **situación socioeconómica**, **sin equivalente en el Artículo 9 del RGPD** **[S]**; el régimen especial se despliega en los Artículos 16 y siguientes, incluido el **16 sexies sobre geolocalización**. Los derechos de los Artículos 4 a 11 suman al estándar ARCO el **bloqueo (8 ter)**, la **portabilidad (9)** y la **oposición a decisiones automatizadas (8 bis)**, y el **Artículo 11** obliga a resolver en **treinta días corridos**, prorrogables una sola vez por otros treinta **[V]** —**corridos, no hábiles**—.

Dos hallazgos verificados corrigen supuestos difundidos en el mercado de cumplimiento. Primero, el **Artículo 14 sexies** obliga a reportar brechas **«por los medios más expeditos posibles y sin dilaciones indebidas»** y **no fija un plazo de 72 horas** **[V]**: esa cifra es un traslado indebido del Artículo 33 del RGPD. Segundo, el **Artículo 27** admite la transferencia internacional por país adecuado, cláusulas contractuales tipo, normas corporativas vinculantes, modelos certificados o excepciones puntuales, pero **al 20 de septiembre de 2026 no hay ningún país declarado con nivel adecuado**, porque esa declaración compete a una Agencia inexistente **[V]**.

El régimen sancionatorio (Arts. 34 bis a 37) escala hasta **5.000, 10.000 y 20.000 UTM** según gravedad, con techo del **2 % y 4 % de los ingresos anuales** para empresas que no son de menor tamaño conforme a la Ley N° 20.416 **[S]**. **Todo ello es hoy derecho suspendido**: lo exigible son las multas de 1 a 10 UTM de la Ley N° 19.628.

---

## 3. Ley N° 21.663: El Único Marco Plenamente Exigible Hoy

La **Ley N° 21.663**, Marco de Ciberseguridad e Infraestructura Crítica de la Información, fue publicada el **8 de abril de 2024** con vigencia escalonada: el grueso del cuerpo legal desde el **1 de enero de 2025**, y los Artículos 5, 8 y 9 junto al Título VII desde el **1 de marzo de 2025** **[S]**. La **ANCI comenzó a funcionar el 2 de enero de 2025** **[V]**.

La **Ley de Presupuestos 2026** confirma su radicación en la **Partida 32 (Ministerio de Seguridad Pública), Capítulo 06, Programa 01**, con **$4.782.293 miles** y **dotación máxima de 40 personas** **[V]**. **Cuarenta funcionarios para supervisar 1.154 entidades obligadas es un cuello de botella estructural** que explica por qué la Agencia privilegia instrucciones generales y estándares autoejecutables por sobre la fiscalización caso a caso.

El **Artículo 5** fija los criterios sustantivos copulativos para calificar como **Operador de Importancia Vital (OIV)** y el **Artículo 6** el procedimiento, con revisión **al menos cada tres años** **[V]**. El primer procedimiento cerró con **1.154 OIV**: 915 en la primera etapa (Resolución Exenta N° 87, de 16 de diciembre de 2025) y **239 en la segunda, cerrada el 24 de julio de 2026** **[V]**. La caída de la nómina preliminar de 1.712 a 915 —un **46,6 %**— demuestra que la consulta pública tuvo efecto material.

El **D.S. N° 295/2024** del Ministerio del Interior y Seguridad Pública, publicado el **1 de marzo de 2025**, fija el esquema **«3/72/15»**: alerta temprana en **3 horas**, actualización en **72 horas —reducida a 24 h si se afectan servicios esenciales—**, plan de acción en **7 días** e informe final en **15 días** **[S]**. El **Artículo 27** define el incidente de efecto significativo por **número de afectados, duración y extensión geográfica**, criterios idénticos a los de NIS2 **[V]**, y una restricción operativa determinante ordena que **los reportes excluyan datos personales**.

---

## 4. Derecho Supletorio y Normativa Complementaria

Hasta el 30 de noviembre de 2026 rige la **Ley N° 19.628 de 1999**, cuya tutela es el **habeas data judicial del Artículo 16** ante el juez de letras en lo civil **[S]**. La **Ley N° 21.180** de Transformación Digital del Estado es modificatoria de la Ley N° 19.880 y **su vigencia es gradual e incompleta**, con tope legal el **31 de diciembre de 2027** **[S]**.

De las ocho normativas adicionales incorporadas a la comparativa (Entregable 3), dos inciden directamente sobre un proyecto de transporte: la **Ley N° 21.459** sobre delitos informáticos, que impone deberes de **conservación de datos de tráfico y de abonados**, y la **Ley N° 21.729**, publicada el **13 de febrero de 2025**, que incorpora un **Artículo 26 quáter a la Ley N° 18.168** obligando a retener registros de abonados —IMEI, MSISDN e IMSI incluidos— **por cinco años** **[S]**. **El ordenamiento ordena acumular datos identificatorios de prácticamente toda la población mientras la Ley N° 21.719 consagra minimización y limitación del plazo de conservación**: el conflicto es concreto y verificable.

---

## 5. Mapa de Organismos y Zonas Grises de Competencia

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

## 6. Traducción al Caso 10: Consecuencias para Transportes Curimón S.A.

Aplicando los hallazgos a la volumetría congelada del Caso 10 —**374 camiones, 454 conductores (196 propios y 258 subcontratados), 148 transportistas, 84 clientes y cruce fronterizo a Mendoza**— resultan cinco consecuencias normativas de ingeniería:

1. **Base de licitud diferenciada para los 258 conductores externos.** Dado que la mayoría de los conductores no pertenece a la dotación propia de Curimón, **la letra c) del Artículo 13 —celebración o ejecución de un contrato— no alcanza su tratamiento**: el contrato de transporte vincula a Curimón con los 148 transportistas, no con los conductores de estos. La licitud debe sostenerse entonces en el **consentimiento del Artículo 12**, recabado de cada conductor y canalizado a través de su empleador, o en el **interés legítimo de la letra d)**, que exige test de finalidad, necesidad y salvaguardas. **La decisión debe quedar documentada antes del 1 de diciembre de 2026.**

2. **La localización GPS tiene régimen agravado.** El **Artículo 16 sexies** sitúa la geolocalización en el bloque de categorías especiales, de modo que el monitoreo continuo de los 374 camiones no se rige por la regla general. Es el fundamento normativo del corte de telemetría fuera de servicio que implementa la arquitectura. La restricción no elimina la finalidad operacional: Curimón necesita trazabilidad del estado de cada camión en ruta, de manera que el control debe **acotar la ventana de monitoreo al servicio**, no suprimirlo.

3. **Las tarifas de los 148 transportistas pueden constituir dato sensible.** Tratándose en parte de personas naturales, la tarifa revela **situación socioeconómica**, categoría sensible sin equivalente en el RGPD. Esto sostiene por vía legal —y no solo contractual— el cifrado a nivel de campo **RT-11.10** exigido por las Bases Técnicas. De ello se sigue una regla de segregación: **los datos de quienes no pertenecen a Curimón no se almacenan junto a los de la dotación propia**, sino en repositorios cifrados y de acceso diferenciado.

4. **El cruce a Mendoza activa el Artículo 27 sin red de seguridad regulatoria.** Como **no hay país declarado con nivel adecuado**, la transferencia debe sostenerse en **cláusulas contractuales tipo** o en una excepción puntual, documentadas caso a caso **con cada transportista empleador** cuyos conductores crucen la frontera.

5. **La calificación como OIV está abierta.** No consta que Curimón figure en las nóminas publicadas **[NV]**, pero la segunda etapa incorporó **40 entidades de transporte** y el **Artículo 6** obliga a revisar la calificación **al menos cada tres años**. La propuesta debe prever la calificación sobreviniente: su efecto inmediato es la **duplicación de los topes de multa** y la exigibilidad del Artículo 8 a los sesenta días corridos de la resolución. Ese plazo de sesenta días permite además **programar la adecuación en temporadas de menor carga operacional**, de modo que la certificación y los ensayos no compitan con los períodos de mayor demanda de transporte.

**Conclusión del capítulo.** Chile construyó dos agencias en paralelo con arquitecturas casi idénticas y reglas de designación opuestas: la ANCI se instaló por decreto del Ejecutivo en **once semanas** y lleva veinte meses operando; la Agencia de Protección de Datos exige dos tercios del Senado y lleva veintiún meses sin existir. El resultado es que **Chile es más exigente que la Unión Europea para reportar un ciberincidente —tres horas— y menos exigente para notificar una brecha de datos personales —sin plazo determinado—**, y a la vez prohíbe que el reporte de incidentes contenga datos personales. La lectura operativa para este proyecto es directa: **el cumplimiento debe diseñarse sobre el marco que hoy se fiscaliza y sobre las obligaciones que el 1 de diciembre de 2026 se vuelven exigibles con o sin autoridad que las reciba.**

---

### Trazabilidad documental

| Sección | Entregable de soporte |
| :--- | :--- |
| §1, §2 | [Entregable 1: Ley N° 21.719](Entregables/Entregable_1_Ley_21719_Datos_Personales.md) |
| §3 | [Entregable 2: Ley N° 21.663 y ANCI](Entregables/Entregable_2_Ley_21663_Ciberseguridad_ANCI.md) |
| §4 | [Entregable 3: Normativa complementaria](Entregables/Entregable_3_Normativa_Complementaria.md) |
| §5 | [Entregable 4: Mapa de organismos y zonas grises](Entregables/Entregable_4_Mapa_Organismos_Zonas_Grises.md) |
| Columna nacional comparativa | [Entregable 5: Cuadro comparativo multicriterio](Entregables/Entregable_5_Cuadro_Comparativo_Columna_Nacional.md) |
| Exhaustividad y bitácora | [Entregable 6: Declaración de exhaustividad](Entregables/Entregable_6_Declaracion_Exhaustividad_Bitacora.md) |
