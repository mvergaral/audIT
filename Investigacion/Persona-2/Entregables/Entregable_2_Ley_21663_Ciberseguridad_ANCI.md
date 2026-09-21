# Entregable 2: Ley N° 21.663, Marco de Ciberseguridad e Infraestructura Crítica
## ANCI, CSIRT Nacional, Calificación de Operadores de Importancia Vital y Reporte de Incidentes

**Asignatura:** Taller de Formulación de Proyectos Informáticos (ICI-5444) · Escuela de Informática, PUCV  
**Empresa Consultora:** AudIT (Empresa 10)  
**Tema de Investigación:** TI-12 · *Cumplimiento normativo en proyectos TIC: Ley 21.719, Ley 21.663 (ANCI) y marco internacional*  
**Proyecto de Aplicación:** Caso 10 — *Transportes Curimón S.A.*  
**Rol Responsable:** Persona 2 (*Chilean Regulatory Research Specialist*)  
**Fecha de corte:** 20 de septiembre de 2026  
**Estado:** Versión definitiva — **único marco del informe plenamente exigible a la fecha de corte**

> [!NOTE]
> **Convención de certeza.** **[V]** = verificado contra fuente primaria · **[S]** = apoyado solo en fuente secundaria · **[NV]** = no verificado. Identificador oficial fijado: **Ley N° 21.663 = `idNorma 1202434`** (D.O. 08-04-2024, edición 43820, documento 2475674).

---

## 1. Vigencia Escalonada: el Marco que Sí Funciona

La **Ley N° 21.663**, Ley Marco de Ciberseguridad e Infraestructura Crítica de la Información, fue **promulgada el 26 de marzo de 2024 y publicada el 8 de abril de 2024** **[S]**.

Su vigencia fue **escalonada en dos tramos**:

| Tramo | Fecha | Contenido |
| :--- | :---: | :--- |
| **Tramo general** | **1 de enero de 2025** | El grueso del cuerpo legal, incluida la puesta en marcha de la ANCI. |
| **Tramo diferido** | **1 de marzo de 2025** | **Art. 5** (calificación de operadores de importancia vital), **Art. 8** (deberes específicos de los OIV), **Art. 9** (deber de reportar incidentes con efectos significativos) y **Título VII** (infracciones y sanciones). |

La propia ANCI confirma que «la obligación de reportar incidentes comenzó el 1 de marzo de 2025» **[S]**. **El texto de los artículos transitorios no pudo verificarse literalmente [NV].**

> [!IMPORTANT]
> **Precisión de articulado obligatoria para todo el equipo.** El **deber de reportar incidentes con efectos significativos es el Artículo 9**, y la calificación del incidente como de efecto significativo es el **Artículo 27**. El desarrollo de plazos está en el **D.S. N° 295/2024**. Cualquier capítulo que atribuya el deber de reporte al «Artículo 14» de la Ley N° 21.663 incurre en un error de cita verificable contra el texto oficial.

---

## 2. La ANCI: Instalación Rápida, Dotación Estrecha

### 2.1 Naturaleza jurídica y cronología de instalación

La ANCI es un **servicio público funcionalmente descentralizado, con personalidad jurídica y patrimonio propio, de carácter técnico y especializado**, y **comenzó a funcionar el jueves 2 de enero de 2025** **[V]**.

Su andamiaje normativo se completó con **rapidez inusual**:

| Instrumento | Materia | Fecha |
| :--- | :--- | :---: |
| **DFL N° 1-21.663** | Fija la planta directiva | **24 de diciembre de 2024** |
| **Decreto N° 483/2024** | Aprueba la estructura interna | Publicado el **21 de febrero de 2025** |
| **Decreto N° 479/2024** | Nombra a **Daniel Álvarez Valenzuela** como primer **Director Nacional** | Publicado el **11 de marzo de 2025** |

**Del DFL N° 1-21.663 al nombramiento del Director Nacional transcurrieron 77 días: once semanas exactas.** Esta cifra es el contrapunto cuantitativo de los veintiún meses que la Agencia de Protección de Datos lleva sin constituirse, y sostiene la conclusión central del capítulo.

Álvarez seguía ejerciendo el cargo en **agosto de 2026**, participando como Director Nacional en el encuentro «Ciberseguridad en Salud» de la Alianza Chilena de Ciberseguridad **[S]**. **No se verificó una ratificación formal por el gobierno iniciado en marzo de 2026 [NV]**, y existe una controversia pública previa sobre conflicto de interés **cuyo desenlace no fue verificado [NV]**.

### 2.2 Radicación ministerial confirmada presupuestariamente

El **Artículo 10 de la Ley N° 21.663** emplea deliberadamente una **fórmula funcional y no nominativa**: «La Agencia se relacionará con el Presidente de la República por intermedio del **Ministerio encargado de la seguridad pública**» **[V]**. Fue redactada así porque el nuevo Ministerio estaba en tramitación cuando se aprobó la ley.

Creado el **Ministerio de Seguridad Pública** por la **Ley N° 21.730**, publicada el **5 de febrero de 2025**, la relación se desplazó automáticamente. **La prueba dura es la Ley de Presupuestos 2026** **[V]**:

| Concepto | Valor |
| :--- | ---: |
| **Ubicación presupuestaria** | **Partida 32** (Ministerio de Seguridad Pública), **Capítulo 06, Programa 01** |
| **Total** | **$4.782.293 miles** |
| Gastos en personal | $2.397.951 miles |
| Bienes y servicios de consumo | $2.287.340 miles |
| Adquisición de activos no financieros | $97.002 miles |
| **Dotación máxima** | **40 personas** (Código del Trabajo) |
| Honorarios adicionales | Hasta 4 contrataciones por $100.000 miles en conjunto |

Una **glosa presupuestaria** obliga a la ANCI a **informar semestralmente a comisiones del Congreso** sobre sus iniciativas y sobre «una relación de los ataques que hubieren sufrido las distintas plataformas del Estado». La ANCI declara domicilio en **Teatinos 220, piso 10** —la misma dirección del Ministerio— y opera la línea **1510**.

> [!WARNING]
> **Cuarenta funcionarios para supervisar más de mil entidades obligadas es un cuello de botella estructural.** Este dato explica —y permite predecir— que la Agencia privilegie **instrumentos de bajo costo de fiscalización** (instrucciones generales, estándares mínimos autoejecutables, consulta pública) por sobre la fiscalización caso a caso. Para efectos de diseño de cumplimiento, la consecuencia es que **el riesgo dominante no es la inspección sino el incidente**: la ANCI actúa cuando el reporte llega, no antes.

### 2.3 CSIRT Nacional y CSIRT de Defensa Nacional

El **CSIRT Nacional no es un órgano separado** sino una **función operada por la ANCI**, destinataria de los reportes de incidentes a través de una plataforma tecnológica disponible **24/7** **[S]**; en la práctica, el portal `portal.anci.gob.cl` con Clave Única, más la línea **1510** y correo electrónico.

El **CSIRT de Defensa Nacional (CSIRT-DN)** quedó formalizado por el **Reglamento de Ciberseguridad de la Defensa Nacional, publicado en el Diario Oficial el 16 de febrero de 2026** **[S]**. **Depende del Estado Mayor Conjunto**, actúa como órgano de coordinación sectorial, fija protocolos y estándares mínimos y supervisa los CSIRT institucionales de los organismos de defensa. Se dicta al amparo de las Leyes N° 21.663 y N° 20.285 y del Código de Justicia Militar, con reglas especiales de confidencialidad, y fija plazos de **seis meses** para evaluaciones de madurez y **doce meses** para implementar estándares mínimos, lo que sitúa los vencimientos en **agosto de 2026 y febrero de 2027**. **El número de decreto de ese reglamento no fue verificado [NV].**

> [!CAUTION]
> **Las estadísticas de incidentes 2025-2026 del CSIRT Nacional no pudieron obtenerse**: el portal `csirt.gob.cl/estadisticas/` devolvió **HTTP 403**. **No se consigna ninguna cifra de incidentes en este informe.** Cualquier número de incidentes que aparezca en otro capítulo carece de respaldo en esta investigación y debe ser retirado o sustentado con fuente propia.

---

## 3. Sujetos Obligados: Servicios Esenciales y Operadores de Importancia Vital

### 3.1 Distinción verificada contra el texto oficial

La distinción entre categorías de obligados quedó **verificada contra el texto oficial [V]**, resolviendo una discrepancia de numeración que circula en la literatura:

| Artículo | Contenido verificado |
| :---: | :--- |
| **Art. 4** | Define el **ámbito de aplicación** y contiene en su **inciso segundo** el listado de **sectores esenciales**. |
| **Art. 5** | Titulado «Operadores de importancia vital», fija los **criterios sustantivos copulativos**: (a) que la provisión del servicio **dependa de las redes y sistemas informáticos**, y (b) que la afectación, interceptación, interrupción o destrucción de sus servicios tenga un **impacto significativo** en la seguridad pública, la continuidad de servicios esenciales o el ejercicio de funciones estatales. Se extiende a instituciones privadas no prestadoras de servicios esenciales que adquieran «un rol crítico en el abastecimiento de la población». |
| **Art. 6** | Regula el **procedimiento** de calificación y su **revisión al menos cada tres años** por resolución del Director Nacional. |

> [!IMPORTANT]
> **Corrección a la literatura especializada.** **La atribución de los criterios sustantivos al Artículo 6 que hace parte de la literatura —incluida IAPP— es imprecisa.** Los criterios están en el **Artículo 5**; el **Artículo 6** contiene el procedimiento y la revisión trienal. Esta discrepancia quedó **resuelta contra el texto oficial**.

La **crítica doctrinal de fondo se mantiene**: la ley «no incluyó un anexo que especifique claramente cuáles actividades económicas corresponden a cada sector definido como crítico». La ANCI cuantifica el universo de servicios esenciales en **35 categorías**, incluidos organismos de la Administración del Estado, prestadores eléctricos, de agua y combustibles, telecomunicaciones e infraestructura digital, **transporte aéreo, terrestre, marítimo y ferroviario**, banca, salud y farmacéutica, y administradoras de seguridad social **[S]**.

### 3.2 Primer procedimiento de calificación: de 1.712 a 1.154

El primer procedimiento de calificación se ejecutó en **dos etapas**:

```
┌──────────────────────────────────────────────────────────────────────────────────┐
│     PRIMER PROCEDIMIENTO DE CALIFICACIÓN DE OIV (2025-2026)                       │
├──────────────────────────────────────────────────────────────────────────────────┤
│                                                                                  │
│  30-05-2025 ─► Requerimientos de informe a reguladores sectoriales                │
│                              │                                                   │
│  16-09-2025 ─► NÓMINA PRELIMINAR: 1.712 instituciones                            │
│                              │                                                   │
│                              ├─► Consulta pública de 30 días                      │
│                              │                                                   │
│  17-12-2025 ─► ETAPA 1 DEFINITIVA: 915 instituciones                             │
│                 (Res. Ex. N° 87, de 16-12-2025)                                  │
│                 ▼ CAÍDA DE 797 INSTITUCIONES = 46,6 %                            │
│                 147 eléctricas · 29 telecomunicaciones · 413 servicios digitales │
│                  34 banca y finanzas · 114 salud · 20 empresas públicas           │
│                 158 organismos de la Administración del Estado                    │
│                              │                                                   │
│  24-07-2026 ─► ETAPA 2: +239 instituciones                                        │
│                  25 combustibles · 18 agua potable y saneamiento (98 % del país) │
│                  40 TRANSPORTE terrestre, aéreo, ferroviario y marítimo           │
│                  32 concesionarias · 25 seguridad social · 15 farmacéuticas       │
│                  84 de sectores ya cubiertos en la 1ª etapa                       │
│                              │                                                   │
│                              ▼                                                   │
│                   TOTAL VIGENTE: 1.154 OIV                                        │
└──────────────────────────────────────────────────────────────────────────────────┘
```

*Lectura de la figura.* El esquema traza el embudo completo del primer procedimiento y permite tres lecturas de fondo. Primero, **la caída de 1.712 a 915 —un 46,6 %— demuestra que la consulta pública tuvo efecto material** y no fue un trámite formal: casi la mitad del universo preliminar logró excluirse. Segundo, **el peso de los servicios digitales (413 de 915, un 45 % de la primera etapa) revela un perímetro OIV sesgado hacia proveedores tecnológicos más que hacia infraestructura física**, lo que sitúa a las empresas de software y servicios TI en el centro del régimen. Tercero, **la segunda etapa incorporó 40 entidades de transporte terrestre, aéreo, ferroviario y marítimo**, dato directamente pertinente para evaluar la exposición del Caso 10.

Contra la calificación proceden los **recursos administrativos de la Ley N° 19.880**. Existe una **discrepancia de cifras** consignada expresamente: la fuente especializada describe la nómina preliminar de septiembre como de «casi 1.400 instituciones» mientras la ANCI reporta **1.712**; **se prefiere la cifra de la Agencia por ser fuente primaria**.

### 3.3 Exigibilidad: los 60 días corridos

Las obligaciones sustantivas de cada OIV rigen **desde los 60 días corridos siguientes a la publicación de la resolución que lo califica** **[S]**:

| Etapa | Resolución publicada | Exigibilidad plena (cálculo) |
| :--- | :---: | :---: |
| **Primera** | 17-12-2025 | **15-02-2026** |
| **Segunda** | Fecha exacta **[NV]** (cierre del proceso: 24-07-2026) | **≈ 22-09-2026** |

> [!CAUTION]
> **Advertencia sobre el cómputo de la segunda etapa.** Este cálculo es una **inferencia aritmética** que depende de la fecha exacta de publicación de la resolución de segunda etapa (Res. Ex. N° 187/2026), **no verificada [NV]**. Si se toma como referencia el cierre del proceso el 24-07-2026, las 239 entidades de la segunda etapa quedarían plenamente obligadas **el 22 de septiembre de 2026, dos días después de la fecha de corte de esta investigación**. La verificación de esa fecha es **prioridad 7** del listado de vacíos (Entregable 6).

---

## 4. Deberes de Ciberseguridad: Dos Niveles y Cuatro Instrucciones Generales

### 4.1 Distribución de deberes

| Artículo | Sujetos | Deberes |
| :---: | :--- | :--- |
| **Art. 7** | **Todos los prestadores de servicios esenciales (PSE)** | Deberes **generales** de prevención y de reporte. |
| **Art. 8** | **Operadores de Importancia Vital (OIV)** | Paquete **reforzado**: sistemas de gestión de seguridad de la información (SGSI), planes de continuidad operacional **certificados y revisados periódicamente**, evaluaciones continuas de redes, certificaciones de ciberseguridad, programas de capacitación y designación de un **delegado de ciberseguridad**. |

### 4.2 Instrucciones generales dictadas por la ANCI

La ANCI ha desarrollado **selectivamente** los literales del Artículo 8 mediante **cuatro instrucciones generales** **[V]**:

| Instrucción | Fecha | Fundamento | Contenido |
| :---: | :---: | :---: | :--- |
| **N° 1** | **04-06-2025** | — | Inscripción de las instituciones calificadas como prestadores de servicios esenciales. |
| **N° 2** | **26-12-2025** | — | Registro. |
| **N° 3** | **26-12-2025** | **Art. 8 literal i)** | **Delegado de ciberseguridad:** obligación exclusiva de los OIV; requisitos mínimos de formación, experiencia o certificación; **independencia funcional respecto del área de TI**; reporte directo a la alta administración; documento formal de designación ante la ANCI; notificación de cambios en un plazo máximo de **cinco días hábiles**. |
| **N° 4** | **26-12-2025** | **Art. 8 literal e)** | **Gestión de incidentes:** medidas mínimas de contención **dentro de las tres horas siguientes al conocimiento del incidente** —restricción de accesos, cambio de contraseñas administrativas, deshabilitación de accesos remotos y aislamiento de sistemas—, con **aplicación preventiva cada seis meses**. |

> [!IMPORTANT]
> **La Instrucción General N° 4 es inusual en el derecho comparado.** Al exigir que las medidas mínimas de contención se **ejerciten preventivamente cada seis meses**, convierte un deber reactivo en un **ejercicio periódico verificable en fiscalización**. Esta es la norma que transforma la respuesta a incidentes de una capacidad declarada en una capacidad auditable, y es la que mejor se presta a evidencia documental ante la ANCI.

### 4.3 Lo que sigue sin desarrollo instruccional

**Los literales del Artículo 8 sobre SGSI, certificaciones, planes de continuidad y capacitación siguen sin desarrollo instruccional**, operando con el **estándar legal genérico**.

La ANCI abrió el **30 de mayo de 2026** una **consulta pública hasta el 29 de junio de 2026** sobre una normativa que volvería obligatorias **seis de las recomendaciones de los «9 básicos de la ciberseguridad»**, seleccionadas a partir del análisis de incidentes de 2025 **[S]**.

> [!CAUTION]
> **No fue posible confirmar si esa norma definitiva fue dictada al 20 de septiembre de 2026 [NV]**, ni consta en el listado oficial consultado ninguna instrucción general de 2026. Esta es la **prioridad 6** del listado de vacíos (Entregable 6) y afecta directamente al dimensionamiento del SGSI en el modelo económico.

---

## 5. Reporte de Incidentes: el Esquema 3/72/15

### 5.1 El D.S. N° 295/2024

El deber de reportar se desarrolla en el **Decreto N° 295, de 2024, del Ministerio del Interior y Seguridad Pública**, «Aprueba reglamento de reporte de incidentes de ciberseguridad», **publicado el 1 de marzo de 2025** **[V]**.

| Hito | Plazo | Contenido |
| :--- | :---: | :--- |
| **Alerta temprana** | **3 horas** desde el conocimiento o detección | Notificación inicial. |
| **Segundo reporte / actualización** | **72 horas**, **reducido a 24 horas cuando se afectan servicios esenciales** | Actualización técnica. |
| **Plan de acción** | **7 días** | Medidas de mitigación y recuperación. |
| **Informe final** | **15 días** | Análisis consolidado y evaluación de impacto. |

La regla se conoce en el mercado como **«3/72/15»** **[S]**.

> [!NOTE]
> **Dos precisiones que el mercado omite.**
> 1. **Tensión entre fuentes sobre el número de etapas.** La ANCI describe **tres etapas progresivas de notificación** mientras el análisis jurídico describe **cuatro fases**. La lectura más plausible —**no resuelta documentalmente [NV]**— es que la plataforma implementa **tres formularios de notificación** (alerta temprana, actualización e informe final) y que **el plan de acción a 7 días es un entregable adicional** exigido por el reglamento, sin contarse como etapa de notificación.
> 2. **El plazo abreviado de 24 horas** cuando hay afectación de servicios esenciales es una **regla de segundo nivel poco difundida**: la mayoría de las fuentes comerciales solo menciona las 72 horas.

> [!CAUTION]
> **Limitación metodológica declarada.** **No fue posible distinguir con fuentes confiables qué plazos están en la ley y cuáles en el reglamento [NV]**, distinción que el encargo de la ficha TI-12 pedía expresamente. La atribución de los cuatro hitos al D.S. N° 295/2024 se sustenta en análisis jurídico secundario, no en lectura directa del texto reglamentario.

### 5.2 «Incidente de efecto significativo» (Artículo 27) — VERIFICADO

La calificación quedó **verificada contra el texto oficial [V]** y corresponde al **Artículo 27 de la Ley N° 21.663**. El incidente tiene efecto significativo cuando puede:

- «**interrumpir la continuidad de un servicio esencial** o **afectar la integridad física o la salud de las personas**», o
- cuando **afecta sistemas que contengan datos personales**,

evaluándose conforme a **tres criterios enumerados**: **el número de personas afectadas, la duración del incidente y la extensión geográfica de la zona afectada**.

> [!IMPORTANT]
> **Esos tres criterios coinciden literalmente con los de la Directiva NIS / NIS2**, confirmando el modelo europeo de la ley. Este es el punto de anclaje más sólido para la comparación Chile-UE del capítulo de Persona 3.

El desarrollo reglamentario añade como criterios de calificación el **compromiso de la confidencialidad de datos personales** y el **acceso no autorizado a redes o sistemas** **[S]**.

### 5.3 Contenido de los reportes y restricción crítica

El **contenido obligatorio** de cada reporte comprende **[S]**:

- Identificación de la institución afectada
- Fecha del incidente y evidencia de respaldo
- Impacto sobre otras instituciones y activos afectados
- Detalles técnicos relevantes

> [!WARNING]
> **Restricción clave de diseño: los reportes deben EXCLUIR datos personales**, salvo excepciones expresamente permitidas. Esta prohibición es la que genera la zona gris **ZG-1** (Entregable 4): un mismo evento obliga a reportar a la ANCI **sin datos personales** y a notificar a la Agencia de Protección de Datos **precisamente por causa de esos datos personales**. La arquitectura de respuesta a incidentes del proyecto debe contemplar **dos flujos de información separados en origen**, no uno solo reutilizado.

La ANCI complementa el reglamento con una **Taxonomía de Incidentes de Ciberseguridad**, aprobada por **Resolución Exenta N° 7/2025**, y autoriza la publicación de alertas tempranas por **Resolución Exenta N° 2/2025** **[V]**.

---

## 6. Procedimiento Sancionatorio y Cuantías

### 6.1 Procedimiento (Artículos 42 y 46) — VERIFICADO

El **procedimiento sancionatorio** quedó **verificado contra el texto oficial [V]**:

| Etapa | Plazo | Artículo |
| :--- | :--- | :---: |
| Formulación de cargos **precisos y fundados** | — | 42 |
| **Descargos** | «No inferior a quince ni superior a treinta días» | 42 |
| **Término probatorio** | «No inferior a diez ni superior a veinte días» | 42 |
| **Informe del instructor** | Máximo quince días | 42 |
| **Resolución del Subdirector** | Máximo quince días | 42 |
| **Reclamación** ante la **Corte de Apelaciones** de Santiago o la del domicilio del reclamante | **Quince días hábiles** desde la notificación | 46 |

**No se verificó si los plazos del Artículo 42 son hábiles o corridos, ni si el reclamo suspende los efectos de la sanción [NV].**

### 6.2 Cuantías: la estructura duplicadora

Las **cuantías solo constan en fuente secundaria de fiabilidad media [S]**:

| Gravedad | **Prestadores de Servicios Esenciales (PSE)** | **Operadores de Importancia Vital (OIV)** |
| :--- | :---: | :---: |
| **Leve** | Hasta **5.000 UTM** | Hasta **10.000 UTM** |
| **Grave** | Hasta **10.000 UTM** | Hasta **20.000 UTM** |
| **Gravísima** | Hasta **20.000 UTM** | Hasta **40.000 UTM** |

> [!CAUTION]
> **La distribución exacta leve/grave/gravísima y el articulado del Título VII no pudieron verificarse [NV]**, y **no se encontró registro de sanciones efectivamente aplicadas por la ANCI a septiembre de 2026**. Cualquier cifra de multa de ciberseguridad usada en el modelo económico debe declararse con esta marca de fiabilidad media.

**Dos lecturas analíticas de la estructura duplicadora:**

1. **Es deliberada.** Hace que la calificación como OIV tenga **consecuencia económica directa**, lo que explica por qué la primera nómina fue tan disputada en consulta pública y por qué 797 instituciones lograron excluirse.
2. **Los topes de ciberseguridad duplican los de protección de datos** (20.000 UTM en la Ley N° 21.719 frente a 40.000 UTM para OIV en la Ley N° 21.663). Esto es señal de que **el legislador ponderó el riesgo sistémico sobre infraestructura crítica por encima del riesgo individual de una brecha**.

---

## 7. Síntesis de Hallazgos y Vacíos

### 7.1 Hallazgos verificados contra fuente primaria [V]

1. **ANCI operativa desde el 2 de enero de 2025**, con presupuesto 2026 de **$4.782.293 miles** y **40 cupos** en la Partida 32.
2. **Artículo 5** contiene los criterios sustantivos de OIV; **Artículo 6**, el procedimiento y la revisión trienal. Corrige a la literatura especializada.
3. **1.154 OIV** calificados (915 + 239), con caída documentada de 1.712 a 915 en consulta pública.
4. **Artículo 27**: tres criterios de efecto significativo idénticos a NIS2.
5. **Artículos 42 y 46**: etapas y plazos del procedimiento sancionatorio.
6. **Cuatro instrucciones generales** de la ANCI (N° 1 de 2025 y N° 2, 3 y 4 de diciembre de 2025).
7. **Resoluciones Exentas N° 2/2025 y N° 7/2025** (alertas tempranas y taxonomía de incidentes).

### 7.2 Vacíos declarados [NV]

| # | Vacío | Impacto | Cómo verificar |
| :---: | :--- | :--- | :--- |
| 1 | Articulado del **Título VII** y distribución exacta de gravedades. | Sustenta las cuantías del modelo económico. | PDF del D.O., edición 43820. |
| 2 | Fecha exacta de publicación de la **Res. Ex. N° 187/2026** (segunda etapa de OIV). | De ella depende el cómputo de los 60 días para 239 entidades. | Buscador del D.O., julio de 2026. |
| 3 | Si la ANCI **dictó la norma definitiva de estándares básicos** tras la consulta cerrada el 29-06-2026. | Dimensiona el SGSI exigible. | `anci.gob.cl/normativa/instrucciones/` y `/resoluciones/`. |
| 4 | **Estadísticas de incidentes del CSIRT Nacional 2025-2026** y reportes semestrales al Congreso. | Ninguna cifra de incidentes es citable hoy. | `csirt.gob.cl/estadisticas/` desde navegador; solicitud de transparencia; actas de comisiones. |
| 5 | Qué plazos del esquema 3/72/15 están en la **ley** y cuáles en el **reglamento**. | Exigido expresamente por la ficha TI-12. | Texto del D.S. N° 295/2024 en el D.O. de 01-03-2025. |
| 6 | Texto de los **artículos transitorios** de la Ley N° 21.663. | Sustenta las fechas de vigencia escalonada. | PDF del D.O., edición 43820. |
| 7 | **Número de decreto** del Reglamento de Ciberseguridad de la Defensa Nacional. | Cita incompleta del CSIRT-DN. | Buscador del D.O., 16-02-2026. |
| 8 | Ratificación formal del Director Nacional por el gobierno iniciado en marzo de 2026. | Afecta la vigencia del dato de autoridad. | `anci.gob.cl/normativa/decretos/`. |

---

## 8. Fuentes Consultadas

**Primarias**

1. **Diario Oficial.** *Ley N° 21.663, Ley Marco de Ciberseguridad e Infraestructura Crítica de la Información.* Edición 43820, 8 de abril de 2024, documento 2475674. [https://www.diariooficial.interior.gob.cl/publicaciones/2024/04/08/43820/01/2475674.pdf](https://www.diariooficial.interior.gob.cl/publicaciones/2024/04/08/43820/01/2475674.pdf)
2. **Diario Oficial.** *Resolución Exenta N° 87 de la ANCI (nómina definitiva de OIV, primera etapa).* Edición 44326-B, 17 de diciembre de 2025, documento 2743431. [https://www.diariooficial.interior.gob.cl/publicaciones/2025/12/17/44326-B/01/2743431.pdf](https://www.diariooficial.interior.gob.cl/publicaciones/2025/12/17/44326-B/01/2743431.pdf)
3. **DIPRES.** *Ley de Presupuestos 2026 — Partida 32, Capítulo 06, Programa 01.* [https://www.dipres.gob.cl/597/articles-397416_doc_pdf.pdf](https://www.dipres.gob.cl/597/articles-397416_doc_pdf.pdf)
4. **ANCI.** *Repositorio normativo: leyes, decretos, instrucciones y resoluciones.* [https://anci.gob.cl/normativa/decretos/](https://anci.gob.cl/normativa/decretos/) · [https://anci.gob.cl/normativa/instrucciones/](https://anci.gob.cl/normativa/instrucciones/) · [https://anci.gob.cl/normativa/resoluciones/](https://anci.gob.cl/normativa/resoluciones/)
5. **ANCI.** *Nóminas de OIV: primera y segunda etapa.* [https://anci.gob.cl/noticias/anci-presenta-nomina-de-oiv-correspondiente-al-primer-procedimiento-de-calificacion/](https://anci.gob.cl/noticias/anci-presenta-nomina-de-oiv-correspondiente-al-primer-procedimiento-de-calificacion/) · [https://anci.gob.cl/noticias/anci-finaliza-el-primer-proceso-de-calificacion-de-operadores-de-importancia-vital/](https://anci.gob.cl/noticias/anci-finaliza-el-primer-proceso-de-calificacion-de-operadores-de-importancia-vital/)
6. **Subsecretaría del Interior.** *Inicio de funcionamiento de la ANCI, 2 de enero de 2025.* [https://www.subinterior.gob.cl/noticias/2025/01/02/este-jueves-2-de-enero-comenzo-a-funcionar-la-agencia-nacional-de-ciberseguridad/](https://www.subinterior.gob.cl/noticias/2025/01/02/este-jueves-2-de-enero-comenzo-a-funcionar-la-agencia-nacional-de-ciberseguridad/)

**Secundarias**

7. **Biblioteca del Congreso Nacional.** *Asesorías Parlamentarias, documento 83750.* [https://www.bcn.cl/asesoriasparlamentarias/detalle_documento.html?id=83750](https://www.bcn.cl/asesoriasparlamentarias/detalle_documento.html?id=83750)
8. **Carey.** *Entrada en vigencia de la Ley de Ciberseguridad* y *ANCI publica Instrucciones Generales N° 2, 3 y 4.* [https://www.carey.cl/anci-publica-instrucciones-generales-n2-3-y-4-sobre-registro-delegado-de-ciberseguridad-y-gestion-de-incidentes-para-servicios-esenciales-y-oiv](https://www.carey.cl/anci-publica-instrucciones-generales-n2-3-y-4-sobre-registro-delegado-de-ciberseguridad-y-gestion-de-incidentes-para-servicios-esenciales-y-oiv)
9. **IAPP.** *El balance normativo en ciberseguridad en Chile 2025* y *Servicios esenciales y operadores de importancia vital según la Ley N° 21.663.*
10. **Diario Constitucional.** *Ley Marco de Ciberseguridad: claves del reglamento de reporte de incidentes.* [https://www.diarioconstitucional.cl/estudios-juridicos/ley-marco-de-ciberseguridad-claves-del-reglamento-de-reporte-de-incidentes/](https://www.diarioconstitucional.cl/estudios-juridicos/ley-marco-de-ciberseguridad-claves-del-reglamento-de-reporte-de-incidentes/)
11. **GlobalSuite Solutions.** *Ley Marco sobre Ciberseguridad e Infraestructura Crítica de la Información de Chile.*
12. **Firewall Chile** y **Netprovider.** *Multas de la Ley Marco de Ciberseguridad.* — **fiabilidad media**, única fuente de las cuantías.
13. **Infodefensa.** *Chile publica reglamento de ciberseguridad de la defensa nacional.*
