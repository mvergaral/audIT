# Entregable 1: Ley N° 21.719 sobre Protección y Tratamiento de Datos Personales
## Análisis de Vigencia, Articulado, Autoridad de Control y Régimen Sancionatorio

**Asignatura:** Taller de Formulación de Proyectos Informáticos (ICI-5444) · Escuela de Informática, PUCV  
**Empresa Consultora:** AudIT (Empresa 10)  
**Tema de Investigación:** TI-12 · *Cumplimiento normativo en proyectos TIC: Ley 21.719, Ley 21.663 (ANCI) y marco internacional*  
**Proyecto de Aplicación:** Caso 10 — *Transportes Curimón S.A.*  
**Rol Responsable:** Persona 2 (*Chilean Regulatory Research Specialist*)  
**Fecha de corte:** 20 de septiembre de 2026  
**Estado:** Versión definitiva — articulado verificado por bloques, con marcas de certeza por afirmación

---

## 1. Advertencia Metodológica: Tres Niveles de Certeza

Este entregable distingue rigurosamente entre tres estados epistémicos y **no eleva el nivel de certeza de ninguna afirmación**:

| Marca | Significado | Fuentes que la sustentan |
| :---: | :--- | :--- |
| **[V]** | **Verificado contra fuente primaria** | Texto publicado en el Diario Oficial, ficha oficial de tramitación del Senado, repositorio normativo de la ANCI, Ley de Presupuestos de DIPRES, o PDF que reproduce el articulado oficial. |
| **[S]** | **Apoyado en fuente secundaria** | Síntesis institucional de la Biblioteca del Congreso Nacional (BCN), estudios jurídicos de primer nivel (Carey, Garrigues, Ontier), compilaciones especializadas (DLA Piper, IAPP, Future of Privacy Forum) o analistas sectoriales, sin contraste con el texto oficial. |
| **[NV]** | **No verificado** | La afirmación no pudo confirmarse en la investigación y se consigna expresamente como tal. |

Esta cautela no es retórica. El portal oficial **Ley Chile (BCN) resultó no recuperable**: sirve su articulado mediante JavaScript y devolvió reiteradamente la pantalla «Este proceso demora demasiado»; el *endpoint* `leychile.cl/Consulta/obtxml` entregó normas distintas de las solicitadas —devolvió el Decreto N° 419 de 2024 para dos `idNorma` diferentes— y el exportador PDF fue rechazado por el proxy.

**La ruta que sí funcionó es el PDF del Diario Oficial**, en el patrón `diariooficial.interior.gob.cl/publicaciones/AAAA/MM/DD/{edición}/01/{id}.pdf`, complementada por `tramitacion.senado.cl`. La consecuencia práctica es que buena parte de la numeración de artículos proviene de la síntesis de la BCN (Informe 12/25) y de un PDF que reproduce el articulado (ACHIPI), y que **el PDF oficial de la Ley N° 21.719 se trunca en la página 20 de 34, antes de las disposiciones transitorias**.

> [!CAUTION]
> **Identificadores oficiales fijados para consultas futuras:** Ley N° 21.719 = `idNorma 1209272` (D.O. 13-12-2024, edición 44023, documento 2583630). El truncamiento del PDF en la página 20 es la causa directa de que varios artículos transitorios figuren como **[NV]** en este entregable.

---

## 2. Vigencia: Publicada pero Dormida — 72 Días para una Entrada en Vigor que el Gobierno Intenta Postergar

### 2.1 Fechas oficiales y técnica legislativa

La **Ley N° 21.719** fue **promulgada el 25 de noviembre de 2024 y publicada en el Diario Oficial el 13 de diciembre de 2024** **[S]**.

Su **Artículo primero transitorio** difiere la entrada en vigencia «hasta el día primero del mes vigésimo cuarto posterior a su publicación», esto es, el **1 de diciembre de 2026**, y ordena que durante el período intermedio «seguirá operando la antigua ley N° 19.628» **[V]**.

> [!IMPORTANT]
> **Corrección de una atribución errónea frecuente.** La fecha de vigencia está en el **Artículo PRIMERO transitorio, no en el tercero**. Según la síntesis de la BCN, el **tercero transitorio** fija las reglas especiales de la primera designación del Consejo Directivo y el **cuarto transitorio** la ventana temporal para esa designación —los sesenta días anteriores a la entrada en vigencia, aproximadamente entre el 1 de octubre y el 30 de noviembre de 2026— **[S]**. El texto literal del tercero transitorio **no pudo obtenerse [NV]**.

| Disposición transitoria | Contenido | Estado |
| :--- | :--- | :---: |
| **Primero transitorio** | Vigencia diferida al **1 de diciembre de 2026**; continuidad de la Ley N° 19.628 en el intervalo. | **[V]** |
| **Segundo transitorio** | Dictar los reglamentos dentro de seis meses desde la publicación. **Plazo vencido el 13 de junio de 2025.** | **[S]** |
| **Tercero transitorio** | Reglas especiales de la primera designación del Consejo Directivo. | **[NV]** |
| **Cuarto transitorio** | Ventana de designación: sesenta días anteriores a la entrada en vigencia. | **[S]** |
| **Quinto transitorio** | Designación de delegados en el sector público «con cargo a la dotación vigente». | **[S]** |
| **Sexto transitorio** | Régimen del primer año: la Agencia solo puede aplicar **amonestación por escrito** a empresas de menor tamaño. | **[S]** |

Carey reporta además un hito de **20 meses** para que el Servicio de Registro Civil elimine determinadas bases de datos, **sin que haya sido posible identificar el artículo transitorio correspondiente [NV]**.

### 2.2 La Ley N° 21.719 NO deroga la Ley N° 19.628

Esta corrección se repite mal en la literatura de cumplimiento y tiene efecto directo sobre la redacción de contratos y políticas:

- La Ley N° 21.719 **sustituye casi íntegramente** la Ley N° 19.628 por reemplazo de su articulado y la **rebautiza** «Ley sobre protección de los datos personales».
- **Conserva**: los literales **b), d), e) y k) —que pasa a ser j)— del Artículo 2°**; los **Artículos 17, 18 y 19** sobre datos de obligaciones económicas, financieras, bancarias y comerciales; y el **inciso primero de su Artículo primero transitorio** **[S]**.
- **Consecuencia:** el número «19.628» seguirá existiendo después de diciembre de 2026, y el régimen del Boletín Comercial conserva su estatuto especial dentro de la ley nueva en lugar de ser absorbido por el régimen general de licitud.

### 2.3 Boletín N° 18.623-07: el proyecto de postergación NO es ley

| Hito | Fecha | Estado |
| :--- | :---: | :---: |
| Mensaje presidencial suscrito | 31-08-2026 | **[V]** |
| Ingreso al Senado (Boletín N° 18.623-07) | **01-09-2026** | **[V]** |
| Estado de tramitación | **Primer trámite constitucional** | **[V]** |
| Comisión asignada | **Ninguna** | **[V]** |
| Urgencia acreditada | **Ninguna** | **[V]** |
| Votación en comisión o Sala | **Ninguna** | **[V]** |
| Presencia en tabla de la Comisión de Constitución (sesión 16-09-2026 y citaciones del 21-09 al 05-10-2026) | **No figura** | **[V]** (evidencia indirecta) |

**Contenido del proyecto**, según el texto disponible en la Cámara de Diputados **[S]**:

1. Traslado de la vigencia **del 1 de diciembre de 2026 al 1 de diciembre de 2027**.
2. Ampliación del Consejo Directivo **de tres a cinco consejeros**, con elevación del quórum de sesión de dos a tres.
3. Exigencia de designarlos **a más tardar doce meses antes** de la entrada en vigencia, mediante **nómina única** aprobada por dos tercios del Senado.
4. Mandatos iniciales escalonados de **2, 4 y 6 años**.
5. Eliminación de la restricción que limitaba las amonestaciones del primer año a las empresas de menor tamaño, **extendiéndolas a todos los responsables**.

Fuentes secundarias añaden una regla de **silencio positivo** en el trámite senatorial de la primera designación y el financiamiento del primer año con cargo al Ministerio de Economía y al Tesoro Público **[S]**.

> [!WARNING]
> **Corrección de fuentes de baja fiabilidad.** Numerosos medios y sitios de cumplimiento dan la postergación por consumada con titulares en tiempo pasado —«Postergan Ley de Protección de Datos Personales a 2027»—. **Esas afirmaciones son incorrectas a la fecha de corte.** Mientras el Congreso no apruebe el proyecto y este no se publique en el Diario Oficial, **la fecha de entrada en vigencia sigue siendo el 1 de diciembre de 2026**, y la carga de demostrar cumplimiento continúa recayendo en cada organización. Las obligaciones que ninguna prórroga alteraría —ordenar tratamientos, levantar el registro de actividades, adecuar cláusulas contractuales con encargados, implementar controles de seguridad— son precisamente las que más tiempo consumen.

---

## 3. La Agencia de Protección de Datos Personales: un Bloqueo Aritmético antes que Técnico

### 3.1 Diseño institucional previsto por la ley

| Artículo | Contenido | Estado |
| :---: | :--- | :---: |
| **Art. 30** | Servicio público **descentralizado**, con personalidad jurídica y patrimonio propio, relacionado con el Presidente a través del **Ministerio de Economía, Fomento y Turismo**. Objeto: «velar por la efectiva protección de los derechos que garantizan la vida privada y los datos personales, y fiscalizar el cumplimiento de las disposiciones». | **[S]** |
| **Art. 30 bis** | Atribuciones: dictar instrucciones y normas generales obligatorias (a); interpretar administrativamente (b); fiscalizar (c); determinar infracciones (d); aplicar sanciones (e); resolver reclamos de titulares (f); proponer normas (g); colaborar con órganos públicos (j). | **[S]** |
| **Art. 30 ter** | **Consejo Directivo de tres consejeros** designados por el Presidente «con acuerdo del Senado, adoptado por los dos tercios de sus miembros en ejercicio». Mandato de **seis años no renovable**, dedicación exclusiva, sesión al menos semanal, quórum mínimo de dos. | **[S]** |
| **Art. 30 sexies** | Remoción exige **pronunciamiento de la Corte Suprema**. | **[S]** |
| **Art. 30 octies** | El Consejo fija sus estatutos mediante **decreto supremo**. | **[S]** |
| **Art. 30 nonies** | El presidente del Consejo es jefe de servicio. | **[S]** |
| **Art. 31** | Deber de **coordinación con el Consejo para la Transparencia**. | **[S]** |
| **Art. 32** | Personal bajo Código del Trabajo con normas de probidad; directivos bajo Ley N° 19.882 (Alta Dirección Pública); fiscalización de Contraloría, con resoluciones **exentas de toma de razón**. | **[S]** |

### 3.2 El rechazo senatorial del 19 de mayo de 2026

El **Boletín S 2716-05** ingresó el **2 de abril de 2026** con la nómina de **Joselyn Elizabeth Biermann Muñoz, Roberto Antonio Godoy Fuentes y Matías Larraguibel Goycoolea** —con períodos propuestos de 6, 4 y 2 años, esto es, un escalonamiento inicial—; fue remitido a las Comisiones unidas de Constitución y de Economía el 7 de abril, discutido entre el 12 y el 19 de mayo, y **votado en Sala en discusión única el 19 de mayo de 2026 con resultado «Rechazado»**, comunicándose formalmente el rechazo al Presidente de la República **[V]**. La causa formal fue **no alcanzar el quórum de dos tercios** **[V]**.

> [!NOTE]
> **Discrepancia de fechas consignada expresamente.** Datos Protegidos sitúa un **empate en comisiones unidas el 13 de mayo de 2026**; la ficha del Senado registra la votación en Sala el **19 de mayo**; y parte de la cobertura periodística fecha el hecho el **20 de mayo**. La lectura más coherente es que se trata de tres momentos sucesivos del mismo episodio, pero **no fue posible resolverlo documentalmente [NV]**. En caso de cita, se usa la fecha de la ficha del Senado por ser fuente primaria.

Una comisión asesora había recomendado que la Agencia estuviera constituida con su Consejo nombrado **a más tardar en junio de 2026**, para alcanzar a dictar reglamentos, procedimientos y canales de servicio antes del inicio de operaciones; **ese plazo venció sin cumplirse**. El **4 de agosto de 2026** el Ministro de Economía **Daniel Mas** reconoció públicamente que «ha costado encontrar a las personas que integren el consejo» y anunció que evaluaría con el Ministro Secretario General de la Presidencia, **José García Ruminot**, si postergar toda la ley o solo la puesta en marcha de la Agencia **[S]**. El ministro García había señalado antes «la dificultad de conformar ternas con profesionales que cumplan los estrictos requisitos de dedicación exclusiva e incompatibilidades exigidos por la ley».

### 3.3 Diagnóstico: el cuello de botella es de aritmética senatorial

**El bloqueo no es técnico sino aritmético.** Un diseño que exige dos tercios sobre tres nombres votados individualmente resultó inviable en un Senado fragmentado, y por eso el proyecto de septiembre sustituye ese mecanismo por una **nómina única de cinco**, que opera como instrumento de reparto político.

A ello se suma una **dependencia circular** que explica el incumplimiento reglamentario:

```
      ┌─────────────────────────────────────────────────────────────────────┐
      │        DEPENDENCIA CIRCULAR QUE BLOQUEA LA VÍA REGLAMENTARIA        │
      ├─────────────────────────────────────────────────────────────────────┤
      │                                                                     │
      │     Art. 26: el reglamento de comunicación/cesión entre             │
      │     organismos públicos y privados lo dicta MINSEGPRES,             │
      │     suscrito por Hacienda y Economía, PREVIO INFORME DE LA AGENCIA  │
      │                              │                                      │
      │                              ▼                                      │
      │     Art. 30 octies: los estatutos de la Agencia se fijan            │
      │     por decreto supremo, a propuesta de SU PROPIO CONSEJO           │
      │                              │                                      │
      │                              ▼                                      │
      │        SIN CONSEJO ──► SIN INFORME ──► SIN REGLAMENTO               │
      │                              │                                      │
      │                              └──────► SIN OPERACIÓN                 │
      └─────────────────────────────────────────────────────────────────────┘
```

*Lectura del esquema.* La figura muestra por qué el retraso no se resuelve por vía administrativa. El **Artículo 26** condiciona el reglamento de cesión de datos entre organismos a un **informe previo de la Agencia**, y el **Artículo 30 octies** condiciona los estatutos de la Agencia a un decreto supremo que presupone un Consejo ya constituido. Como el Consejo depende de una votación senatorial que fracasó, ninguno de los dos instrumentos puede dictarse: el sistema está bloqueado en su punto de entrada, y ninguna autoridad puede desbloquearlo unilateralmente.

**No se encontró evidencia de que se haya dictado y publicado ningún reglamento de la Ley N° 21.719 entre diciembre de 2024 y el 20 de septiembre de 2026** —afirmación que debe leerse como **ausencia de evidencia, no como evidencia de ausencia**—. Lo único documentado es actividad preparatoria: una **comisión asesora creada por el Ministerio de Justicia el 17 de junio de 2025** y la *Guía Práctica* de la Secretaría de Gobierno Digital, con cronograma diciembre 2025 – noviembre 2026 que fija catálogo de datos en mayo-junio de 2026, política de tratamiento en julio y protocolos entre agosto y noviembre **[S]**.

### 3.4 Tres efectos operativos de la inexistencia de la Agencia

1. **No hay ningún país declarado con nivel adecuado de protección**, porque esa declaración es competencia de la Agencia conforme al **Artículo 28**. Es un cuello de botella crítico para flujos transfronterizos desde diciembre de 2026.
2. **La vía de tutela administrativa de los Artículos 41 a 43 será inoperante en la práctica** aun entrando en vigor la ley, salvo designación del Consejo en la ventana de octubre-noviembre de 2026.
3. **El presupuesto 2026 de la Agencia no pudo verificarse [NV]**: no se localizó partida ni capítulo propio en la Ley de Presupuestos 2026, lo que es consistente —pero no concluyente— con que el financiamiento del primer año provendría del Ministerio de Economía y del Tesoro Público según el propio proyecto de postergación.

---

## 4. Responsable, Encargado y las Cinco Letras del Artículo 13

### 4.1 Definiciones y régimen del encargo

El **Artículo 2° letra n)** define al **responsable** como la «persona natural o jurídica que decide acerca de los fines y medios del tratamiento», y la **letra ñ)** al **titular** como la «persona natural a quien conciernen los datos personales» **[S]**.

La ley **no construye una definición autónoma de «encargado»** al modo del Artículo 4.8 del RGPD, sino que emplea la fórmula **«mandatario o encargado»**, con régimen diferenciado de responsabilidades **[S]**.

El régimen del encargo está en el **Artículo 15 bis**, **verificado parcialmente** contra el articulado **[V] parcial**:

- El tercero mandatario o encargado actúa **conforme a las instrucciones del responsable**.
- Le está **prohibido tratar los datos para un objeto distinto** del encargo.
- El contrato debe contener al menos **objeto, duración, finalidad y tipo de datos**.
- Se recuperó el fragmento «El encargado no podrá delegar parte o la totalidad del encargo» y una referencia a **responsabilidad solidaria** por daños.

> [!CAUTION]
> **Advertencia expresa: no debe afirmarse una prohibición absoluta de subencargo.** La técnica estándar y la práctica de los comentaristas sugieren que el fragmento continúa con una excepción del tipo «salvo autorización expresa del responsable», pero **el inciso completo no pudo verificarse [NV]**; tampoco se verificó el alcance exacto de la responsabilidad solidaria ni los deberes de confidencialidad y de supresión o devolución al término del encargo. La técnica chilena —mandato civil más ley especial— sugiere una articulación sobre las reglas del mandato del Código Civil complementadas por la ley, a diferencia del Artículo 28 del RGPD, que es autónomo; esta es una **inferencia estructural, no una cita**.

### 4.2 Consentimiento (Artículo 12)

El **Artículo 12** consagra el consentimiento como **regla general**, exigiendo que sea «libre, informado y específico en cuanto a su finalidad», manifestado «previa y de manera inequívoca» mediante declaración verbal, escrita o electrónica o acto afirmativo, con medios de otorgamiento y revocación **«expeditos, fidedignos, gratuitos y permanentemente disponibles»** **[S]**.

Su **inciso sexto** incorpora una **presunción de falta de consentimiento** cuando el responsable lo recaba «en el marco de la ejecución de un contrato o prestación de servicio en que no es necesario efectuar la recolección». Esta norma opera como **equivalente funcional del Artículo 7.4 del RGPD** e impide legitimar recolección excesiva empaquetada en la contratación.

### 4.3 Las cinco letras del Artículo 13 (VERIFICADO)

El **Artículo 13**, titulado «Otras fuentes de licitud del tratamiento de datos», fue **verificado contra el articulado [V]** y contiene **cinco letras**:

| Letra | Base de licitud | Nota comparativa |
| :---: | :--- | :--- |
| **a)** | Datos relativos a obligaciones de carácter **económico, financiero, bancario o comercial** | **Sin equivalente europeo.** Herencia directa del sistema DICOM de la Ley N° 19.628. |
| **b)** | Cumplimiento de una **obligación legal** | Análoga al Art. 6.1.c) del RGPD. |
| **c)** | **Celebración o ejecución de un contrato** | Análoga al Art. 6.1.b) del RGPD. |
| **d)** | Satisfacción de **intereses legítimos** del responsable | Análoga al Art. 6.1.f) del RGPD. |
| **e)** | **Formulación, ejercicio o defensa de un derecho ante los tribunales** | Sin correlato autónomo en el Art. 6 del RGPD. |

> [!IMPORTANT]
> **Dos hallazgos con consecuencia directa de ingeniería.**
> 1. **El interés vital NO figura como base autónoma del Artículo 13.** La protección de la vida, la salud o la integridad se canaliza por el **Artículo 16 bis**, dentro del régimen de datos sensibles. Esto obliga a reconducir el tratamiento de datos **no sensibles** por interés vital a otra letra —típicamente obligación legal o interés legítimo—, divergencia notable frente al Artículo 6.1.d) del RGPD.
> 2. **La letra a) no tiene equivalente europeo**, y confirma que el legislador chileno trató el dato financiero como el problema central de privacidad del país.

El **interés legítimo** se describe en la literatura especializada como sujeto a un **test de tres pasos** —análisis de finalidad, evaluación de necesidad, evaluación de impacto y salvaguardas apropiadas— **[S]**, y la doctrina chilena lo trata como la «nueva base de licitud» de la reforma.

**Sector público:** el **Artículo 20** invierte la regla —es lícito el tratamiento realizado para el cumplimiento de funciones legales dentro del ámbito de competencia, **sin consentimiento del titular**, actuando los órganos como responsables—; y el **Artículo 54** extiende un régimen análogo al Congreso Nacional, el Poder Judicial, la Contraloría, el Ministerio Público, el Tribunal Constitucional, el Banco Central, el Servicio Electoral, la Justicia Electoral y los tribunales especiales **[S]**.

### 4.4 Principios y ámbito territorial

El **Artículo 3°** fija **ocho principios**, de los cuales la síntesis oficial detalla cinco: **finalidad** (letra b), **proporcionalidad** (c), **responsabilidad** (e), **seguridad** (f) y **confidencialidad** (h), esta última con deber de secreto «subsistente después de concluida la relación». **El listado completo con sus ocho letras no pudo verificarse [NV].**

Sobre el **ámbito territorial**, la fuente comparativa sitúa en el **Artículo 1 bis** una cláusula de **triple conexión** —establecimiento en Chile; tratamiento por cuenta de responsable establecido en Chile; u oferta de bienes o servicios a residentes en Chile o monitoreo de su comportamiento, con independencia del lugar de establecimiento—, sustancialmente equivalente al Artículo 3 del RGPD **[S]**, no contrastado con el texto oficial.

---

## 5. Datos Sensibles, Derechos de los Titulares y Deberes del Responsable

### 5.1 Categorías especiales (Artículo 2° letra g)

El **Artículo 2° letra g)** define el dato personal sensible por referencia a «características físicas o morales, hechos o circunstancias de la vida privada», comprendiendo **[S]**:

- Origen **étnico o racial**
- Afiliación **política, sindical y gremial**
- **Situación socioeconómica**
- Convicciones **ideológicas y religiosas**
- **Salud**, perfil biológico humano y **datos biométricos**
- **Vida sexual**, orientación sexual e identidad de género

> [!IMPORTANT]
> **La inclusión de la situación socioeconómica carece de equivalente en el Artículo 9 del RGPD** y tiene impacto directo sobre *scoring* crediticio, segmentación comercial y focalización de programas sociales. Genera además una **fricción interpretativa interna**: la situación socioeconómica es dato sensible, pero la morosidad conserva su estatuto propio en los Artículos 17 a 19 heredados de la Ley N° 19.628.

**Arquitectura del régimen especial:**

| Artículo | Materia | Estado |
| :---: | :--- | :---: |
| **Art. 16** | Regla general sobre datos sensibles. Consentimiento con excepciones tasadas: datos manifiestamente públicos, interés legítimo de entidades sin fines de lucro, protección de vida/salud/integridad, defensa jurídica, ámbito laboral y de seguridad social, o autorización legal. | **[S]** |
| **Art. 16 bis** | Salud y perfil biológico humano. | **[NV]** |
| **Art. 16 ter** | Datos biométricos. | **[NV]** |
| **Art. 16 quáter** | Niños, niñas y adolescentes, **por tramos etarios**: menores de 14 requieren consentimiento de padres o tutores; entre 14 y 18 rigen las reglas generales, **salvo los datos sensibles de menores de 16**, que exigen consentimiento parental. Estándares de interés superior y autonomía progresiva. Descrita como **novedosa frente a sus pares regionales**. | **[S]** |
| **Art. 16 quinquies** | Fines históricos, estadísticos y científicos. | **[NV]** |
| **Art. 16 sexies** | **Geolocalización.** | **[NV]** en su contenido dispositivo |

**El contenido dispositivo de cada uno de los Artículos 16 bis a 16 sexies no fue verificado contra el texto oficial, como tampoco el texto vigente de los Artículos 17 a 19 [NV].**

### 5.2 Catálogo de derechos (Artículos 4 a 11)

| Derecho | Artículo | Alcance verificado | Estado |
| :--- | :---: | :--- | :---: |
| **Acceso** | 5 | — | **[S]** |
| **Rectificación** | 6 | — | **[S]** |
| **Supresión o cancelación** | 7 | — | **[S]** |
| **Oposición** | 8 | — | **[S]** |
| **Oposición a decisiones automatizadas** | 8 bis | Derecho a obtener explicación, expresar el punto de vista, solicitar revisión y obtener **intervención humana** frente a tratamientos automatizados con efectos jurídicos o afectación significativa. Explicita en el texto legal lo que en el RGPD se discute por la vía del considerando 71. | **[S]** |
| **Bloqueo** | 8 ter | **«Suspensión temporal de las operaciones de tratamiento mientras se resuelve la solicitud».** Sin equivalente directo en el RGPD. | **[S]** |
| **Portabilidad** | 9 | Copia «en formato electrónico estructurado, genérico y de uso común» y transmisión entre responsables. **Exigible solo cuando el tratamiento es automatizado y se funda en consentimiento**; transferencia directa cuando sea técnicamente posible; **el responsable no queda obligado a eliminar** los datos en origen. Alcance **más estrecho** que el Art. 20 del RGPD, que cubre también la base contractual. | **[S]** |

> [!WARNING]
> **Precisión terminológica obligatoria para todo el equipo.** El **Artículo 8 ter es BLOQUEO (suspensión temporal)**, no supresión ni borrado. La **supresión o cancelación es el Artículo 7**. Cualquier capítulo que use «Art. 8 ter» como fundamento del derecho al borrado incurre en una contradicción cruzada verificable.

**Plazo de ejercicio (VERIFICADO).** El **Artículo 11** fija que el responsable debe resolver **dentro de los treinta días CORRIDOS** siguientes al ingreso de la solicitud, plazo «prorrogable, por una sola vez, hasta por treinta días corridos» **[V]**.

> [!CAUTION]
> **Son días corridos, no hábiles.** La formulación «30 días hábiles» que circula en material de cumplimiento **no fue confirmada por ninguna fuente**.

La solicitud se presenta por correo electrónico habilitado, formulario de contacto o medio electrónico equivalente, y la denegación o falta de respuesta habilita el reclamo ante la Agencia. Frente a **órganos públicos**, el **Artículo 23** limita el ejercicio a **acceso, rectificación y oposición** **[S]**.

### 5.3 Vía de tutela: doble vía con acción civil autónoma

| Artículo | Procedimiento | Plazo |
| :---: | :--- | :--- |
| **Art. 41** | Tutela de derechos ante la Agencia cuando el responsable denegó la solicitud o no respondió dentro de plazo. | — |
| **Art. 42** | Procedimiento por infracción de ley, iniciable **de oficio o a petición de parte**. | — |
| **Art. 43** | **Reclamo de ilegalidad** ante la Corte de Apelaciones de Santiago o la del domicilio del reclamante. Impugnables tanto el acto que paraliza el procedimiento como la resolución final. | **Quince días hábiles** desde la notificación |
| **Art. 47** | **Responsabilidad civil** por daño patrimonial y extrapatrimonial derivado de la infracción de los principios del Art. 3° o de los derechos y obligaciones de la ley. | — |

### 5.4 Deberes del responsable (Artículos 14 a 15 ter)

| Artículo | Deber | Estado |
| :---: | :--- | :---: |
| **14 bis** | Secreto y confidencialidad. | **[S]** |
| **14 ter** | **Información y transparencia:** mantener permanentemente disponible en el sitio web la política de tratamiento, las categorías de datos, los destinatarios, las finalidades y las políticas de seguridad. | **[S]** |
| **14 quinquies** | **Adoptar medidas de seguridad**, sin fijar estándares técnicos. Traslada el detalle a las instrucciones generales de la Agencia, **que hoy no existen**. | **[S]** |
| **14 sexies** | **Reporte de vulneraciones a las medidas de seguridad.** | **[V]** |
| **15 ter** | **Evaluación de impacto previa** cuando sea probable un alto riesgo para los derechos de los titulares: evaluación sistemática automatizada, tratamiento masivo, monitoreo de zonas de acceso público, datos sensibles. | **[S]** |

> [!IMPORTANT]
> **HALLAZGO VERIFICADO QUE REFUTA A BUENA PARTE DEL MERCADO DE CUMPLIMIENTO.** El **Artículo 14 sexies**, titulado «Deber de reportar las vulneraciones a las medidas de seguridad», obliga a reportar a la Agencia **«por los medios más expeditos posibles y sin dilaciones indebidas»**, y **NO fija un plazo de 72 horas [V]**.
>
> La cifra de 72 horas, afirmada por varios proveedores comerciales, es con alta probabilidad un **traslado indebido del Artículo 33 del RGPD**: la ley chilena tomó la fórmula cualitativa pero no el plazo numérico. Analistas locales ya identifican la indeterminación como el problema práctico central. **Ningún capítulo del informe puede afirmar un plazo de 72 horas bajo la Ley N° 21.719.**

La **comunicación al titular** sería obligatoria, según fuente secundaria, cuando estén involucrados **datos sensibles, de niños, niñas y adolescentes o de obligaciones económicas** **[S]**.

### 5.5 Delegado de protección de datos: facultativo, con numeración no resuelta

El **delegado de protección de datos** está regulado, según la síntesis de la BCN, en el **Artículo 50** —designado por la máxima autoridad directiva, con autonomía, funciones de información, asesoría y supervisión del cumplimiento, y como punto de contacto con la Agencia— y su designación es **facultativa**, a diferencia del Artículo 37 del RGPD **[S]**.

> [!NOTE]
> **Discrepancia de numeración consignada expresamente.** La fuente comparativa (Future of Privacy Forum; DLA Piper) ubica el DPO en el **Artículo 49** y matiza que **sí es exigido dentro de los modelos de prevención o cumplimiento certificados**, pudiendo en micro, pequeñas y medianas empresas asumir la función el dueño o administrador; mientras la BCN sitúa en el **Artículo 49** el modelo de prevención. **La numeración exacta queda NO VERIFICADA [NV].** Ninguna fuente consultada sitúa el DPO en el Artículo 48.

Para el sector público, la guía oficial invoca el **Artículo quinto transitorio** para permitir la designación de delegados «con cargo a la dotación vigente», sin inversión presupuestaria adicional **[S]**.

> [!CAUTION]
> **Vacío operativamente relevante:** el **artículo que consagra el registro de actividades de tratamiento no pudo identificarse** con certeza —probablemente 15 o 15 bis—, pese a ser una de las obligaciones operativamente más exigentes **[NV]**.

### 5.6 Transferencias internacionales (Artículos 27 a 29)

El régimen quedó **verificado en su estructura [V]**:

| Artículo | Contenido |
| :---: | :--- |
| **Art. 27** | Hipótesis lícitas: (1) **país con nivel adecuado de protección** (remite al Art. 28); (2) **cláusulas contractuales tipo y normas corporativas vinculantes**; (3) **modelos de cumplimiento certificados**; (4) elenco de **excepciones** para transferencias específicas y puntuales. |
| **Art. 28** | Radica en la **Agencia** la determinación de los ordenamientos con nivel adecuado. |
| **Art. 29** | Fiscalización del régimen. |

Los cuatro mecanismos **mapean casi uno a uno con el Capítulo V del RGPD**, con la adición chilena de los modelos certificados. El **listado literal de las excepciones del Artículo 27 no fue verificado [NV]**; según fuente secundaria comprendería consentimiento expreso, transferencias financieras, obligaciones derivadas de tratados, cooperación entre organismos públicos, ejecución de contrato y medidas médicas o sanitarias urgentes.

> [!WARNING]
> **Consecuencia crítica para el Caso 10.** Como la declaración de adecuación compete a la Agencia (Art. 28) y la Agencia no existe, **al 20 de septiembre de 2026 no hay ningún país declarado con nivel adecuado**. Toda transferencia internacional debe sostenerse en **cláusulas contractuales tipo**, normas corporativas vinculantes, modelo certificado o excepción puntual, documentada caso a caso.

---

## 6. Régimen Sancionatorio: Severo en el Papel y Cero Exigible Hoy

### 6.1 Clasificación de infracciones

| Categoría | Artículo | Hipótesis consignadas | Estado |
| :--- | :---: | :--- | :---: |
| **Leves** | 34 bis | Incumplimiento total o parcial del deber de información y transparencia. | **[S]** |
| **Graves** | 34 ter | Tratamiento **sin consentimiento del titular ni otro fundamento legal**; tratamiento **con una finalidad distinta** de aquella para la que fueron recolectados. | **[S]** |
| **Gravísimas** | 34 quáter | Destinar **maliciosamente** los datos a una finalidad distinta de la consentida o autorizada; tratar, comunicar o ceder **a sabiendas** datos **sensibles** o de **menores**. | **[S]** |

> [!CAUTION]
> **Los catálogos son EJEMPLARES, NO COMPLETOS.** La BCN ilustra una hipótesis leve y dos de cada categoría restante. Las hipótesis adicionales previsibles —incumplimiento del deber de notificación de brechas, del registro de actividades o de las medidas de seguridad— **no pudieron confirmarse por artículo y letra [NV]**. Ningún capítulo puede presentar estos catálogos como taxativos.

### 6.2 Escala de multas (Artículo 35)

La escala es **concordante en todas las fuentes consultadas** **[S]**:

| Gravedad | Sanción | Equivalencia en CLP (1 UTM ≈ $69.542, noviembre 2025) | Equivalencia en USD (DLA Piper) |
| :--- | :--- | :---: | :---: |
| **Leve** | Amonestación escrita o multa de hasta **5.000 UTM** | ≈ **$347,7 millones** | **USD 397.100** |
| **Grave** | Hasta **10.000 UTM** | ≈ $695,4 millones | — |
| **Gravísima** | Hasta **20.000 UTM** | ≈ **$1.390 millones** | **USD 1.588.400** |

> [!NOTE]
> **Nota de conciliación con el modelo económico de Persona 4.** Las equivalencias de esta tabla usan el valor de la UTM de **noviembre de 2025 ($69.542)**, que es el de la fuente consultada. El modelo financiero de P4 opera con la **paridad contractual congelada del Formulario E-24 (1 UTM = $70.000 CLP)**. **Ambas cifras son correctas en su propio marco y no deben mezclarse**: el informe debe declarar explícitamente qué paridad usa cada tabla y por qué.

**Agravantes y multiplicadores del mismo Artículo 35** **[S]**:

- **Recargo del 50 %** de la multa si no se adoptan las medidas dentro de **60 días**.
- Multa hasta **tres veces** el monto en caso de **reincidencia** —definida por la fuente comparativa como **dos o más infracciones en 30 meses**—.
- Respecto de **empresas que no son de menor tamaño** conforme a la **Ley N° 20.416**: multas de hasta el **2 % de los ingresos anuales** por ventas y servicios del último año en infracciones **graves reiteradas**, y hasta el **4 %** en **gravísimas**.
- Fuentes secundarias añaden la **suspensión de las operaciones de tratamiento por hasta 30 días** como sanción accesoria en reincidencia de gravísimas; **el artículo que la contempla no fue identificado [NV]**.

Los **Artículos 36 y 37** fijan, respectivamente, circunstancias agravantes y atenuantes y criterios de determinación del monto, **cuyo detalle no fue verificado [NV]**; tampoco la prescripción de infracciones y sanciones.

### 6.3 Instrumentos reputacionales y modelo de prevención

| Artículo | Instrumento | Contenido | Estado |
| :---: | :--- | :--- | :---: |
| **Art. 40** | **Registro Nacional de Sanciones y Cumplimiento** | Público, electrónico y de acceso gratuito, administrado por la Agencia. Documenta tanto a los responsables sancionados como a las entidades que adoptan modelos de prevención. Una fuente secundaria le atribuye una vigencia de registro de **cinco años**. | **[S]** |
| **Art. 49** | **Modelo de prevención** | Programa de cumplimiento **certificado por la Agencia**. | **[S]** |
| **Art. 51** | Incorporación al registro | Ordena incorporar al registro a las entidades con certificación vigente. | **[S]** |
| **Art. 52** | Duración de la certificación | **Tres años**. | **[S]** |

> [!WARNING]
> **Precisión necesaria sobre el efecto del modelo de prevención.** **Ninguna fuente consultada afirma que el programa opere como EXIMENTE.** Su efecto es **atenuante** en la graduación de la sanción (Arts. 36 y 37, cuyo detalle es **[NV]**) y **reputacional** por vía del registro del Artículo 40. Cualquier afirmación sobre un porcentaje específico de rebaja de la multa **requiere fuente primaria que esta investigación no localizó**.

El techo porcentual del 2 % / 4 % opera **solo en reincidencia** y **solo respecto de empresas que no califican como de menor tamaño**, introduciendo un **factor de proporcionalidad por tamaño ausente del RGPD**.

### 6.4 Lo exigible hoy: Ley N° 19.628

> [!CAUTION]
> **Todo el régimen anterior es derecho suspendido.** Al 20 de septiembre de 2026 **no hay infracción administrativa posible bajo la Ley N° 21.719**, porque no está vigente y no hay órgano con potestad sancionatoria. El régimen aplicable es el de la **Ley N° 19.628**: **multas de una a diez UTM**, y de **dos a cincuenta UTM por retardo** en el cumplimiento, impuestas por el **juez de letras en lo civil** en el procedimiento de habeas data de su **Artículo 16** — un umbral **sin efecto disuasivo alguno** frente a operadores de escala nacional.

---

## 7. Síntesis de Hallazgos Verificados y Vacíos Declarados

### 7.1 Hallazgos verificados contra fuente primaria [V]

1. **Vigencia el 1 de diciembre de 2026** por el Artículo primero transitorio, no el tercero.
2. **Rechazo senatorial de la nómina de consejeros el 19 de mayo de 2026** y estado del Boletín N° 18.623-07 en primer trámite sin votación.
3. **Cinco letras del Artículo 13**, sin interés vital como base autónoma.
4. **Treinta días corridos** del Artículo 11, prorrogables una sola vez por otros treinta.
5. **Artículo 14 sexies sin plazo de 72 horas**: «sin dilaciones indebidas».
6. **Estructura de los Artículos 27 a 29** sobre transferencias internacionales.
7. **Artículo 15 bis** (parcial): instrucciones, prohibición de finalidad distinta, contenido mínimo del contrato.

### 7.2 Vacíos declarados [NV] — pendientes para Persona 8

| # | Vacío | Cómo verificar |
| :---: | :--- | :--- |
| 1 | Estado del Boletín N° 18.623-07 entre el 20-09 y el 01-12-2026. **Variable que puede invalidar la conclusión central.** | `tramitacion.senado.cl` + revisión diaria del Diario Oficial desde noviembre. |
| 2 | Texto literal de los artículos transitorios, en especial el tercero. | Páginas 20 a 34 del PDF del D.O. (edición 44023, documento 2583630) o `bcn.cl/leychile/navegar?idNorma=1209272` con JavaScript habilitado. |
| 3 | Régimen completo del encargado: **subencargo y responsabilidad solidaria** (Art. 15 bis). | Mismo procedimiento que (2), localizando el Art. 15 bis. |
| 4 | Catálogos completos de infracciones y criterios de graduación (Arts. 34 bis a 37). | PDF del Diario Oficial, edición 44023. |
| 5 | Existencia de reglamentos o de una segunda nómina de consejeros entre junio y septiembre de 2026. | Buscador del D.O. con «datos personales» y «Ley 21.719», período 01-01-2025 a 20-09-2026. |
| 6 | Numeración del DPO (Art. 49 o 50) y del registro de actividades de tratamiento (¿15 o 15 bis?). | Mismo procedimiento que (2). |
| 7 | Contenido dispositivo de los Arts. 16 bis a 16 sexies y texto vigente de los Arts. 17 a 19. | Mismo procedimiento que (2). |
| 8 | Las ocho letras completas del Artículo 3° y el texto del Artículo 1 bis. | Mismo procedimiento que (2). |

---

## 8. Fuentes Consultadas

**Primarias**

1. **Diario Oficial de la República de Chile.** *Ley N° 21.719, que regula la protección y el tratamiento de los datos personales y crea la Agencia de Protección de Datos Personales.* Edición 44023, 13 de diciembre de 2024, documento 2583630. [https://www.diariooficial.interior.gob.cl/publicaciones/2024/12/13/44023/01/2583630.pdf](https://www.diariooficial.interior.gob.cl/publicaciones/2024/12/13/44023/01/2583630.pdf) — *PDF truncado en la página 20 de 34.*
2. **Senado de la República.** *Boletín S 2716-05: nómina de consejeros de la Agencia de Protección de Datos Personales.* [https://www.senado.cl/actividad-legislativa/informacion-legislativa/asuntos-exclusivos-del-senado/3018](https://www.senado.cl/actividad-legislativa/informacion-legislativa/asuntos-exclusivos-del-senado/3018)
3. **Senado de la República.** *Ficha de tramitación del Boletín N° 18.623-07.* [https://tramitacion.senado.cl/appsenado/templates/tramitacion/index.php?boletin_ini=18623-07](https://tramitacion.senado.cl/appsenado/templates/tramitacion/index.php?boletin_ini=18623-07)
4. **Cámara de Diputadas y Diputados.** *Texto del Boletín N° 18.623-07.* [https://www.camara.cl/verDoc.aspx?prmID=18854&prmTIPO=INICIATIVA](https://www.camara.cl/verDoc.aspx?prmID=18854&prmTIPO=INICIATIVA)

**Secundarias institucionales**

5. **Biblioteca del Congreso Nacional (BCN).** *Informe 12/25 — Ley de Datos Personales.* [https://obtienearchivo.bcn.cl/obtienearchivo?id=repositorio%2F10221%2F37137%2F1%2FInforme_12_25_Ley_Datos_Personales_rev.pdf](https://obtienearchivo.bcn.cl/obtienearchivo?id=repositorio%2F10221%2F37137%2F1%2FInforme_12_25_Ley_Datos_Personales_rev.pdf)
6. **ACHIPI.** *Ley 21.719 — texto que reproduce el articulado.* [https://achipi.cl/wp-content/uploads/2025/06/Ley-21719-REGULA-LA-PROTECCION-Y-EL-TRATAMIENTO-DE-LOS-DATOS-PERSONALES-Y-CREA-LA-AGENCIA-DE-PROTECCION-DE-DATOS-PERSONALES.pdf](https://achipi.cl/wp-content/uploads/2025/06/Ley-21719-REGULA-LA-PROTECCION-Y-EL-TRATAMIENTO-DE-LOS-DATOS-PERSONALES-Y-CREA-LA-AGENCIA-DE-PROTECCION-DE-DATOS-PERSONALES.pdf)
7. **Secretaría de Gobierno Digital.** *Guía práctica de implementación de la nueva ley de datos personales.* [https://wikiguias.digital.gob.cl/datos-personales/guia-practica-implementacion-nueva-ley-datos-personales](https://wikiguias.digital.gob.cl/datos-personales/guia-practica-implementacion-nueva-ley-datos-personales)

**Secundarias especializadas**

8. **Carey.** *Publicación de la Ley N° 21.719* y *Gobierno ingresa proyecto que posterga su entrada en vigor.*
9. **Garrigues.** *Chile: el Ejecutivo refuerza la futura Agencia de Protección de Datos.*
10. **Future of Privacy Forum.** *Chile's New Data Protection Law: Context, Overview and Key Takeaways.* [https://fpf.org/blog/chiles-new-data-protection-law-context-overview-and-key-takeaways/](https://fpf.org/blog/chiles-new-data-protection-law-context-overview-and-key-takeaways/)
11. **DLA Piper.** *Data Protection Laws of the World — Chile.* [https://www.dlapiperdataprotection.com/index.html?t=law&c=CL](https://www.dlapiperdataprotection.com/index.html?t=law&c=CL)
12. **Ontier.** *Ley 21.719 que regula la protección de datos personales.*
13. **Emol.** *Gobierno evalúa postergar ley de datos personales*, 4 de agosto de 2026.

**Fuentes citadas para refutarlas (no admisibles como respaldo)**

14. **Von Marttens** y **CSITI** — dan por consumada la postergación; **incorrecto a la fecha de corte**.
15. **Confidata** y **Amsoft** — afirman un plazo de 72 horas bajo la Ley N° 21.719; **refutado contra el Art. 14 sexies**.
