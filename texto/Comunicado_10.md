# Comunicado 10 — Estructura Obligatoria de las Propuestas Preparatorias y Técnica Final

> **Curso:** ICI-5444 Formulación y Evaluación de Proyectos TIC (FEP)  
> **Docente:** Antonio Moya Villegas  
> **Fecha de emisión:** 23 de septiembre de 2026  
> **Carácter:** Normativo oficial (complementa los Formularios T-7 y T-21 de las Bases Administrativas; pasa a formar parte de las Bases de Licitación).

---

## Propósito y Alcance

Este documento establece el **índice obligatorio de los subdocumentos de la Oferta Técnica** y las **reglas de forma** con que debe desarrollarse cada uno. El propósito es que cada PROPONENTE conozca exactamente qué contenido corresponde a cada capítulo, en qué archivo va y cómo debe presentarse.

* **Complementariedad:** Complementa el Formulario T-7 y el Formulario T-21 de las Bases Administrativas; no los reemplaza.
* **Entregas parciales:** En cada instancia se entregan únicamente los subdocumentos que exige el Formulario T-22 para dicha instancia; el índice detallado a continuación rige para todos ellos.

---

## 1. Archivos y Nomenclatura

Cada capítulo constituye un subdocumento independiente. Sus anexos y los formularios asociados se entregan en archivos separados del subdocumento principal:

| Tipo de archivo | Formato de nombre | Ejemplo |
|---|---|---|
| **Subdocumento** | `EMPRESA-SubdocumentoX` | `VORA-Subdocumento3.pdf` |
| **Anexos del subdocumento** | `EMPRESA-SubdocumentoX-Anexos` | `VORA-Subdocumento3-Anexos.pdf` |
| **Formulario técnico** | `EMPRESA-Formulario-T-X` | `VORA-Formulario-T-12.pdf` |

### Reglas de entrega:
1. **Un formulario por archivo:** No se aceptan formularios incrustados dentro del subdocumento ni dentro del archivo de anexos.
2. **Cita en texto:** Cuando el índice señala *«Anexo: Formulario T-X»*, significa que ese formulario acompaña al capítulo como archivo propio y debe citarse expresamente en el texto del capítulo donde se utiliza.
3. **Sanción por nomenclatura:** Un archivo mal nominado se considera no presentado (**Art. 40.4**).
4. **Empaquetado:** Todo debe entregarse comprimido en un archivo ZIP según las indicaciones de las Bases Administrativas.

---

## 2. Reglas del Índice

1. **Fidelidad estricta al 100%:** Los títulos y subtítulos declarados deben respetarse íntegramente: misma numeración, mismo texto exacto y mismo orden. No se puede omitir, renombrar, fusionar ni reordenar ninguno.
2. **Subtítulos de menor nivel:** Se permite agregar subtítulos de menor nivel bajo los declarados (por ejemplo, `2.2.1`, `2.2.2` bajo `2.2`; o `4.1.2` y `4.1.3` después del `4.1.1` obligatorio), siempre y cuando todos los títulos declarados estén presentes.
3. **Prohibición de títulos del mismo nivel:** No se pueden agregar títulos del mismo nivel que los declarados (no existe un `2.6` ni un `Capítulo 15`).
4. **Tratamiento de títulos no aplicables:** Si un título declarado no aplica al caso, se mantiene y se justifica formalmente por escrito el porqué no aplica. No se acepta un título vacío ni la sola frase *«no aplica»*.
5. **Estructura de apertura y cierre:** Cada subdocumento comienza con su índice detallado con número de página (**Art. 40.4**) y concluye con dos secciones sin numerar en este orden estricto:
   - **Referencias**
   - **Declaración de uso de IA**
6. **Texto introductorio obligatorio:** Cada capítulo abre con un texto de introducción inmediatamente bajo el título principal del capítulo: resume el capítulo y explica cómo se conecta con los otros capítulos o subdocumentos y con los anexos y formularios asociados. Esta regla aplica obligatoriamente a los 14 capítulos.

---

## 3. Reglas de Redacción

1. **Texto de caída bajo cada título:** Ningún título, de ningún nivel, puede ir seguido directamente de otro elemento que no sea texto. Bajo cada título debe existir un texto de caída con una explicación, introducción o análisis. **Queda estrictamente prohibido:**
   - Título seguido directamente de otro título.
   - Título seguido directamente de una imagen o diagrama.
   - Título seguido directamente de una tabla.
   - Título seguido directamente de una lista sin frase introductoria.
2. **Propósito analítico:** El subdocumento resume y analiza; el anexo y el formulario detallan y listan (**Formulario T-21**). Un capítulo estructurado principalmente como tablas de listado no cumple lo solicitado.
3. **Cálculo y trazabilidad de cifras:** Toda cifra relevante debe derivar directamente de las Bases Técnicas del caso o de un cálculo numérico expuesto.
4. **Coherencia terminológica:** La terminología y los nombres de componentes, módulos y servicios deben ser idénticos en todos los subdocumentos.
5. **Prohibición de cifras económicas:** La Oferta Técnica no puede contener precios, tarifas, valores unitarios ni cifras que permitan inferir el monto de la oferta (**Art. 50.2**).

### Consideraciones Transversales de Evaluación (Formulario T-7)
Aplican a todos y cada uno de los capítulos:
* **Consistencia técnica:** Todas las secciones deben mantener absoluta coherencia arquitectónica y tecnológica entre sí.
* **Trazabilidad:** Mapeo explícito y continuo entre requerimientos, diseño, implementación y operación.
* **Fundamentación ingenieril:** Todas las decisiones deben respaldarse con análisis cuantitativo, modelos formales y mejores prácticas.
* **Cumplimiento normativo:** Consideración rigurosa de aspectos regulatorios, estándares del **Art. 4.3** y marcos de gobierno de TI. La sola mención de un estándar sin evidencia concreta de cómo la solución lo satisface se evalúa con **puntaje cero** en el criterio respectivo (**Art. 4.3**).

---

## 4. Figuras, Diagramas y Esquemas

1. **Construcción combinada:** La explicación técnica se construye combinando texto y diagramas. Los esquemas y diagramas guían la explicación, mientras que el texto los recorre, los interpreta y extrae conclusiones de ellos. Un capítulo técnico sin figuras integradas, o con figuras relegadas sólo a anexos, no cumple lo solicitado.
2. **Rotulación y cita obligatoria:** Cada figura se numera y titula (por ejemplo: *«Figura 4.3 — Vista de despliegue en la región primaria»*), se cita en el texto antes de aparecer y se explica en detalle con posterioridad.
3. **Legibilidad:** Todo el texto contenido dentro de una figura debe leerse sin necesidad de ampliar, en el tamaño impreso de la página, con tipografía no inferior a **9 puntos** (**Art. 40.4**). Se admite página en orientación horizontal para figuras de gran formato.
4. **Diagramas complejos:** Se debe presentar primero una vista general panorámica y posteriormente explicarla por partes. Cada parte debe ser un diagrama dibujado y preparado con el nivel de detalle que corresponde a esa sección.
5. **Prohibición de recortes:** No se acepta el recorte (*crop*) ni la simple ampliación de una sección de una imagen mayor como figura de detalle.
6. **Leyenda de fuente:** Cada figura debe indicar su fuente (*«Fuente: Elaboración propia»* o referencia en norma **APA 7.ª edición** si se basa en obras de terceros). La leyenda acompaña siempre a una figura efectivamente insertada y explicada en el texto; una leyenda sin su figura es indicio de generación no supervisada por IA (**sección 7.1, letra a**). No se aceptan diagramas genéricos ajenos a la solución propuesta.

---

## 5. Tablas en el Cuerpo del Subdocumento

> [!NOTE]
> Esta sección rige exclusivamente para las tablas insertas en el cuerpo principal de cada subdocumento. No aplica a los anexos ni a los formularios, los cuales se rigen únicamente por los mínimos de legibilidad del **Art. 40.4**.

1. **Cuándo usar una tabla:** La tabla sirve para presentar datos comparables multidimensionalmente: cifras, dimensionamientos, comparación de alternativas, matrices de decisión o matrices de mapeo. **No sirve para explicar.** Una explicación de base (definición de un componente, funcionamiento de un proceso, justificación de una decisión) debe redactarse como texto, apoyada en diagramas cuando corresponda.
2. **Prohibición de texto en tablas:** Una tabla del tipo *«Concepto | Descripción»*, o cuyas celdas contengan párrafos explicativos, se considera texto forzado en tabla y no se acepta en el cuerpo del documento.
   * *Regla práctica:* Si una celda requiere más de una frase, dicho contenido corresponde a texto de redacción y no a tabla.
3. **Tamaño y columnas:** La tabla del cuerpo muestra únicamente lo necesario para sostener el análisis del punto.
   * Cada columna debe aportar a la explicación del punto en que aparece. Deben eliminarse columnas no comentadas en el texto, las que repitan el mismo valor en todas las filas y las columnas vacías.
   * *Límites de referencia:* Una tabla en el cuerpo no debe superar **cinco columnas** ni extenderse por más de **una página**.
   * Si el contenido excede estas dimensiones, constituye un **listado**: el listado completo debe ir en el anexo o formulario técnico, presentando en el cuerpo únicamente una tabla de síntesis (totales por categoría, elementos críticos o más relevantes), citando el anexo o formulario correspondiente.
4. **Legibilidad:**
   * Tipografía no inferior a **9 puntos** (**Art. 40.4**), sin palabras cortadas por columnas angostas y sin texto en orientación vertical.
   * Si una tabla continúa en la página siguiente, se repite obligatoriamente la fila de encabezado y no se cortan filas entre páginas.
   * Orientación vertical (salvo tablas de anexos, que admiten formato apaisado/horizontal).
5. **Formato corporativo unificado:** Todas las tablas de la propuesta deben usar el mismo estilo gráfico definido en la plantilla de la empresa: encabezado corporativo, idéntica tipografía, bordes uniformes y alineación consistente (texto a la izquierda, valores numéricos a la derecha con sus respectivas unidades). No se admiten tablas pegadas como imagen ni estilos por defecto de procesadores de texto mezclados.
6. **Integración en el texto:**
   * Cada tabla se numera, titula (por ejemplo: *«Tabla 5.2 — Volumetría anual por dominio»*), indica fuente y se cita en el texto previo a su aparición.
   * Tras la tabla, el texto debe explicitar las conclusiones derivadas de ella. Una tabla sin análisis posterior incumple la norma.
   * Ningún título puede anteceder directamente a una tabla sin texto intermedio.

---

## 6. Referencias Bibliográficas

1. **Citas en el texto:** Las referencias deben citarse en el lugar preciso donde se emplean, bajo norma **APA 7.ª edición**, evidenciando el aporte concreto de cada fuente (dato, criterio, estándar o postulado).
2. **Citas a las Bases de Licitación:** Indicar taxativamente documento, capítulo o artículo y número de página (por ejemplo: *Bases Técnicas del caso, Cap. 7, p. 12*).
3. **Correspondencia unívoca:** Al final de cada subdocumento va la sección **Referencias** con la nómina exhaustiva. Toda referencia listada debe estar citada en el texto, y toda cita en el texto debe figurar en la lista. No se admiten referencias huérfanas ni citas sin entrada bibliográfica.

---

## 7. Uso de Inteligencia Artificial Generativa

> [!IMPORTANT]
> Estas indicaciones actualizan y formalizan el uso de IA en la propuesta y pasan a formar parte vinculante de las **Bases de Licitación**.

### 7.1 Uso de IA generativa en los subdocumentos
Se prohíbe presentar capítulos o secciones cuyo texto haya sido generado íntegramente por IA generativa y entregado sin elaboración ni revisión humana sustantiva. El uso de estas herramientas como apoyo a la redacción, síntesis o revisión está autorizado, siempre que el contenido haya sido producido, validado y asumido formalmente como propio por integrantes del grupo, declarándose en el **Formulario A-6** (**Art. 13.5**).

Un capítulo se considerará generado íntegramente por IA cuando no evidencie trabajo de ingeniería propio. Son indicios taxativos de ello:

* **a)** Ausencia de diagramas, tablas de cálculo o figuras integradas en el desarrollo del texto (o relegadas a anexos sin cita, explicación ni conclusiones). La sola inclusión de la leyenda *«Fuente: elaboración propia»* sin diagrama acredita que la IA generó el marcador para insertar una figura que nunca fue elaborada.
* **b)** Cifras no derivables de la volumetría del caso ni trazables a un cálculo numérico expuesto, o inclusión de líneas base, mediciones o certificaciones ficticias.
* **c)** Contradicciones entre capítulos o subdocumentos en decisiones de diseño (tecnologías, etapas, umbrales, proveedores, regiones de despliegue), revelando generación aislada sin lectura conjunta.
* **d)** Presencia de marcadores, instrucciones o notas residuales del asistente o revisor (`[cite: n]`, `[INSERTAR DIAGRAMA…]`, `Anexo ??`, `por indicación del usuario`, `borrador`, `pendiente de validar`), referencias a secciones o anexos inexistentes, cuadros de aprobación en blanco o expresiones que rompan la ficción de la licitación (*curso*, *docente*, *estudiantes*, *propuesta académica*).

> [!CAUTION]
> #### Régimen de Sanción
> * **Informe 1:** Sanción grave mediante descuento de puntaje en el ítem del Formulario T-21 al que pertenece el capítulo afectado, consignándose en la retroalimentación.
> * **Informe 2 y Propuesta Final:** La detección de cualquiera de estos indicios en un capítulo o sección implicará que el **Subdocumento completo se declarará por no presentado**, obteniendo **puntaje 0** en todos los ítems del Formulario T-21 dependientes de él, impactando la admisibilidad de la oferta conforme al **Art. 58°**, sin posibilidad de subsanación (**Art. 55.2**).
> * **Defensa oral:** Cualquier capítulo, sección o figura de la propuesta que el grupo sea incapaz de defender o explicar técnicamente recibirá idéntico tratamiento sancionatorio desde el Informe 1.

### 7.2 Declaración de uso de IA por subdocumento
Al final de cada subdocumento, inmediatamente después de las Referencias, se incluye la sección **Declaración de uso de IA**. Consta de un texto breve introductorio y una tabla con una fila por cada sección del capítulo (más una fila por cada anexo o formulario asociado):

#### Formato de la Tabla de Declaración:
| Sección | Herramienta | Finalidad del uso | Nivel en texto | Nivel en diagramas | Revisión humana (quién y qué verificó) |
|---|---|---|---|---|---|
| *Ej: 1.1* | *Herramienta utilizada* | *Objetivo concreto* | *Ninguno / Bajo / Medio / Alto* | *Ninguno / Bajo / Medio / Alto* | *Nombre del integrante y aspecto verificado* |

#### Escala Oficial de Niveles:
| Nivel | Definición en Texto | Definición en Diagramas |
|:---:|---|---|
| **Ninguno** | Sin uso de IA. | Sin uso de IA. |
| **Bajo** | Corrección ortográfica, de estilo o reformulación de frases redactadas por el grupo. | Sugerencias de formato o disposición sobre un diagrama elaborado por el grupo. |
| **Medio** | Borradores o síntesis de partes que el grupo reescribió y verificó técnicamente. | Diagrama generado con asistencia (ej. código Mermaid o PlantUML) a partir de un modelo definido por el grupo. |
| **Alto** | Texto generado sustancialmente por IA y editado por el grupo. | Diagrama generado sustancialmente por IA. |

* Si no se utilizó IA en una sección, se consigna expresamente **«Ninguno»**.
* Esta declaración por subdocumento se consolida en el **Formulario A-6** (**Art. 13.5**) y no exime de la responsabilidad íntegra sobre el contenido.
* La declaración no convalida infracciones a la sección 7.1: un nivel «Alto» declarado no autoriza la entrega de un capítulo sin ingeniería humana.

---

## 8. Innovaciones

Las innovaciones deben satisfacer estrictamente el **Capítulo 5 de las Bases Administrativas (Arts. 28° a 30°)**, respetando la correspondencia unívoca de **una innovación por tipo**:

1. **Innovación 1:** Producto o servicio.
2. **Innovación 2:** Proceso.
3. **Innovación 3:** Tecnológica o de arquitectura.
4. **Innovación 4:** Modelo de negocio o de contratación.
5. **Innovación 5:** Experiencia de usuario, sostenibilidad o impacto social.

### Reglas obligatorias de desarrollo:
* **Correspondencia numérica:** La innovación $N$ del Capítulo 13 corresponde forzosamente al tipo $N$. No se admiten dos innovaciones del mismo tipo.
* **Los 7 elementos del Art. 29°:** Cada propuesta debe desarrollar obligatoriamente:
  1. Problema u oportunidad dimensionado.
  2. Tecnología o práctica propuesta.
  3. Nivel de madurez tecnológica con respaldo bibliográfico formal.
  4. Diseño de incorporación (arquitectura, paquetes de la EDT y mes del cronograma).
  5. Impacto económico cualitativo/cuantitativo.
  6. Indicador medible con línea base y meta comprometida.
  7. Riesgo de adopción con estrategia de mitigación y contingencia.
* **Exclusiones taxativas (Art. 30°):** No se aceptan como innovación tecnologías estándar de la industria, tendencias conceptuales sin diseño de incorporación, ni funcionalidades requeridas explícitamente en las Bases Técnicas.
* **Restricción de montos:** En la Oferta Técnica el impacto económico se expresa sin valores económicos de la oferta (**Art. 50.2**); la valorización financiera pertenece a la Oferta Económica.

---

## 9. Recordatorios Formales (Art. 40°)

* Formato PDF con capa de texto seleccionable, tamaño carta u oficio, cuerpo tipográfico de **11 puntos o superior**.
* Índice detallado con número de página en cada subdocumento, con hipervínculos funcionales (*linkeables*) hacia cada título y subtítulo.
* Foliación correlativa en el extremo inferior derecho y firma conforme al **Art. 40°**.
* Portada formal con la identidad de la empresa proponente, exenta de elementos ajenos a la ficción de la licitación.

---

## 10. Criterios de Evaluación

Las infracciones sobre uso de IA generativa se sancionan conforme a la **sección 7.1**. En todos los demás aspectos, el cumplimiento de este comunicado se evalúa en el ítem **Transversal del Formulario T-21** (formalidad, contenido y cumplimiento estricto de instrucciones) y en el ítem particular de cada subdocumento afectado. Un título obligatorio ausente se considera **contenido no presentado** en dicho ítem.

---

## 11. Índice Obligatorio por Capítulo (Subdocumentos 1 al 14)

> [!NOTE]
> Cada capítulo corresponde al subdocumento del Formulario T-7 con idéntica numeración. Todo el contenido exigido por el Formulario T-7 se encuentra asignado a un título específico: ninguno puede omitirse y debe desarrollarse en el acápite correspondiente.

---

### Capítulo 1 · Introducción
* **Subdocumento 1 del T-7:** *Presentación de la empresa*
* **Texto de introducción:** Resumen del capítulo y su articulación con los demás capítulos, anexos y formularios.
* **1.1 Presentación de la empresa:** Reseña de la trayectoria, capacidades instaladas, líneas de negocio, catálogo de productos y servicios ofrecidos.
* **1.2 Estructura Organizacional:** Organigrama como figura explicada analíticamente y dotación institucional.
* **1.3 Gobierno interno Calidad, Seguridad y Conocimiento:** Políticas, instancias de gobierno, comités y roles responsables de calidad, seguridad de la información y gestión del conocimiento.
* **1.4 Experiencia y Certificaciones:** Proyectos relevantes en la industria del caso y de complejidad equivalente; certificaciones corporativas. Resumen y análisis en el cuerpo; el detalle exhaustivo va en el **Formulario T-6** (**Art. 34°**: al menos tres proyectos, incluyendo uno de arquitectura híbrida y uno con SLA de disponibilidad $\ge 99,5\%$).
* **1.5 Estructura para Proyecto:** Organización interna adoptada para abordar este contrato específico (el equipo técnico nominado se detalla en el Capítulo 12).
* **1.6 Alianzas:** Alianzas tecnológicas estratégicas vigentes (ej. partners oficiales de nube). Alianzas exclusivas del proyecto van en 12.3.
* **Anexos:**
  * `EMPRESA-Formulario-T-6.pdf`

---

### Capítulo 2 · Introducción al Problema y Necesidad
* **Subdocumento 2 del T-7:** *Comprensión del problema y de la necesidad*
* **Texto de introducción:** Resumen del capítulo y su articulación general.
* *Directriz transversal:* No confundir el problema con la solución propuesta. Referenciar fuentes en norma APA 7.ª edición en el punto exacto de utilización.
* **2.1 Resumen Ejecutivo del problema:** Síntesis ejecutiva de la problemática, escala de impacto y actores involucrados.
* **2.2 Comprensión del problema y de la necesidad:** Contexto operacional de la industria, particularidades de la cadena logística, aspectos regulatorios y dinámicas de estacionalidad.
* **2.3 Dimensionamiento del problema:** Dimensionamiento cuantitativo riguroso con datos de soporte. Cada cifra debe derivar de las Bases Técnicas del caso o de un modelo de cálculo explícito.
* **2.4 Actores y Grupos de Interés:** Mapeo de grupos de interés, caracterizando niveles de influencia, interés y riesgos asociados.
* **2.5 Resumen de Requerimientos, Supuestos, Exclusiones y Restricciones:** Síntesis y análisis de exigencias del CLIENTE, supuestos operativos fundados, exclusiones contractuales y restricciones operativas.
* **Anexos:**
  * `EMPRESA-Subdocumento2-Anexos.pdf` (con Listado de Requerimientos, Listado de Supuestos, Exclusiones y Restricciones, y otros listados de soporte).

---

### Capítulo 3 · Introducción al Alcance de la Solución
* **Subdocumento 3 del T-7:** *Esquema de solución y alcance*
* **Texto de introducción:** Resumen del capítulo y articulación sistemática.
* **3.1 Resumen Ejecutivo de la Solución:** Visión integral del ciclo: fases de implementación (Etapa 1 y Etapa 2), implantación (marchas blancas y pasos a producción) y operación continuada (36 meses).
* **3.2 Alcance:** Descomposición modular estructurada del proyecto, desarrollando:
  * Alcance diferenciado de Etapa 1 y Etapa 2, con criterios de corte y justificación.
  * Exclusiones explícitas, supuestos y restricciones del alcance.
  * Catálogo priorizado de requerimientos funcionales y no funcionales (resumen en el capítulo; matriz de trazabilidad íntegra en el **Formulario T-12**).
  * Criterios formales de aceptación del alcance comprometido.
* **3.3 Esquema de solución:** Modelo conceptual y diagramas de arquitectura de solución. Cada diagrama se explica exhaustivamente en el texto (por partes si es de alta complejidad).
* **3.4 Explicación de la Solución:** Descripción operacional y de negocio, demostrando coherencia con la problemática del Capítulo 2 y estrategia de adopción con los grupos de interés de 2.4. Mapeo al 100% con la Arquitectura Lógica (4.1), conservando idéntica nomenclatura de componentes.
* **Anexos:**
  * `EMPRESA-Formulario-T-12.pdf`

---

### Capítulo 4 · Introducción a la Arquitectura Lógica y Física de la Solución
* **Subdocumento 4 del T-7:** *Arquitectura lógica y física de la solución*
* **Texto de introducción:** Resumen del capítulo y articulación con otros subdocumentos.
* *Directriz transversal:* Arquitectura específica y original; prohibidos diagramas genéricos. Toda decisión estructural debe acompañarse del registro de alternativas evaluadas y criterios de selección.
* **4.1 Arquitectura lógica:** Mapeo unívoco con el Esquema de Solución (3.3) y la Explicación (3.4). Diagramas detallados y analizados desarrollando:
  * Capas, módulos funcionales, bounded contexts, responsabilidades e interfaces expuestas.
  * Arquitectura de integración: catálogo de servicios, contratos API, patrones de mensajería asíncrona, versionado y gobernanza.
  * Arquitectura de seguridad: modelo Zero Trust, perímetro expuesto, gestión de identidad/accesos, criptografía y controles preventivos.
  * **4.1.1 Especificaciones Tecnologías de Software a utilizar:** Lenguajes, frameworks, bases de datos, middlewares y servicios cloud, justificando su selección con base en alternativas descartadas.
* **4.2 Arquitectura física:** Mapeo estricto con la Arquitectura Lógica. Diagramas comentados desarrollando:
  * Emplazamiento de componentes en nube pública y on-premise (**Art. 16°**).
  * Catálogo de servicios contratados en proveedores cloud.
  * Arquitectura de despliegue en todos los entornos: Desarrollo, QA, Preproducción, Producción y Disaster Recovery (DR), topología de redes, esquemas de alta disponibilidad y políticas de respaldo.
  * Enlaces de comunicación, análisis de puntos únicos de falla (SPOF) y mecanismos de conmutación/mitigación.
  * Dimensionamiento y capacidad: modelos cuantitativos de concurrencia, rendimiento, almacenamiento y tasas de crecimiento.
  * **4.2.1 Especificaciones Implementos a proveer (Hardware y Software):** Resumen ejecutivo (detalle de inventario en el **Formulario T-11**).
* **4.3 Data center:** Estrategia integral de infraestructura y centros de datos.
  * **4.3.1 Especificaciones Data Center Primaria:** Proveedor, región geográfica, zonas de disponibilidad (AZ) e infraestructura on-premise asociada.
  * **4.3.2 Especificaciones Data Center Secundario:** Sitio de recuperación, esquema de replicación de datos, objetivos RPO y RTO comprometidos, y protocolo operativo de failover.
* **Anexos y recomendaciones:**
  * `EMPRESA-Formulario-T-11.pdf`
  * *Recomendación:* Incorporar en 4.2 una matriz de trazabilidad que cruce componente por componente su representación en el esquema conceptual (3.3), arquitectura lógica (4.1) y nodo físico (4.2).

---

### Capítulo 5 · Introducción al Modelo y Gestión de Datos
* **Subdocumento 5 del T-7:** *Modelo y gestión de datos*
* **Texto de introducción:** Resumen del capítulo y conexiones transversales.
* **5.1 Modelo:** Definición de dominios de información y diagramas conceptuales/lógicos de datos legibles por dominio (el diccionario de datos completo se entrega en anexos).
* **5.2 Gestión de datos:**
  * Justificación de motores y paradigmas de persistencia (SQL vs. NoSQL, transaccionalidad ACID vs. BASE, teorema CAP).
  * Segregación arquitectónica entre cargas transaccionales (OLTP) y analíticas (OLAP/Data Lake), detallando el modelo de explotación.
  * Políticas de gobernanza: calidad del dato, retención histórica, archivado y protocolo de sanitización/borrado seguro.
* **5.3 Estrategia de migración:** Metodología de extracción, transformación, saneamiento, carga y conciliación de información histórica; estimación de volumetría y ventanas de corte operativas acordes al cronograma.
* **5.4 Estrategia de desempeño:** Estrategias de indexación avanzada, esquemas de particionamiento, mecanismos de caching distribuido y optimización de consultas fundadas en la volumetría del caso.

---

### Capítulo 6 · Introducción a las Metodologías
* **Subdocumento 6 del T-7:** *Metodologías*
* **Texto de introducción:** Resumen del capítulo y su inserción metodológica.
* **6.1 Metodología de Gestión de Proyectos:** Adaptación del marco PMBOK combinada con metodologías ágiles (híbrido). Gobernanza de stakeholders, planes de comunicación, adquisiciones y gestión de integración. Cadencias, ceremonias y comités de decisión del proyecto.
  * *Anexo asociado:* `EMPRESA-Formulario-T-9.pdf`
* **6.2 Metodología de Desarrollo Software:**
  * Ciclo de vida adaptado a la naturaleza del proyecto: gestión evolutiva de requerimientos, diseño arquitectónico continuo, prevención y mitigación de deuda técnica, y time-to-market.
  * Prácticas de ingeniería DevSecOps: integración y entrega continuas (CI/CD), infraestructura como código (IaC) y automatización de pruebas en pipeline.
  * Ceremonias, artefactos de ingeniería, cadencias operativas y mecanismos de aprobación técnica.
  * *Anexo asociado:* `EMPRESA-Formulario-T-10.pdf`

---

### Capítulo 7 · Introducción al Plan de Trabajo
* **Subdocumento 7 del T-7:** *Plan de trabajo, EDT, cronograma e implantación*
* **Texto de introducción:** Resumen del capítulo y coherencia con el marco metodológico.
* **7.1 EDT:** Estructura de Descomposición del Trabajo con el 100% del alcance (innovaciones, seguridad, calidad, migración, pruebas y despliegue) desagregada hasta paquetes de trabajo estimables y asignables. Resumen analítico del Diccionario de la EDT (el catálogo exhaustivo va en el **Formulario T-14**).
* **7.2 Plan de trabajo:** Alineación con las metodologías del Capítulo 6. Secuenciamiento, estimación de esfuerzo, asignación de frentes de trabajo paralelos y sincronización (atención especial a los solapamientos críticos de los meses 13 a 15 y 19 a 20).
* **7.3 Cronograma e implantación:**
  * Determinación de la Ruta Crítica y análisis de holguras empleando técnicas PERT y CPM.
  * Carta Gantt articulada con el cronograma contractual mandatado en el **Art. 17°** e hitos de control del **Formulario E-25**.
  * Plan de implantación y puesta en marcha: patrón de despliegue (blue-green, canary o rolling update), pruebas UAT de aceptación de usuario, pruebas no funcionales de estrés/rendimiento, métricas de éxito y protocolo de rollback/reversión.
  * Plan de marcha blanca de Etapa 1 y Etapa 2 con criterios e indicadores formales de cierre (**Art. 17.3**).
* **Anexos:**
  * `EMPRESA-Formulario-T-14.pdf`
  * `EMPRESA-Formulario-T-15.pdf`
  * `EMPRESA-Formulario-T-18.pdf`

---

### Capítulo 8 · Introducción a los Riesgos
* **Subdocumento 8 del T-7:** *Plan de riesgos*
* **Texto de introducción:** Resumen del capítulo y articulación preventiva.
* *Directriz transversal:* Los riesgos deben reflejar taxativamente la solución tecnológica y operacional propuesta, prohibiéndose inventarios genéricos.
* **8.1 Plan de riesgos:** Enfoque metodológico de administración del riesgo, estructura de roles, matrices de probabilidad e impacto calibradas, y cadencias de monitoreo.
* **8.2 Identificación y Análisis de Riesgos:**
  * Identificación estructurada mediante Estructura de Desglose de Riesgos (RBS) abarcando riesgos técnicos, organizacionales, de gestión, ciberseguridad y continuidad operativa.
  * Énfasis en riesgos de obsolescencia de software, lock-in de proveedor de nube, escalabilidad elástica, ciberamenazas y disponibilidad de contrapartes del CLIENTE.
  * Modelamiento cualitativo y cuantitativo mediante técnicas de árbol de fallas, análisis FMEA/AMFE o simulaciones probabilísticas.
* **8.3 Plan de Acción a Riesgos:** Planes de mitigación y contingencia soportados en análisis costo-beneficio, asignando responsables, plazos y umbrales disparadores (*triggers*). Definición técnica de reservas de contingencia y gestión (su valorización económica se reserva para la Oferta Económica, **Art. 50.2**).
* **Anexos:**
  * `EMPRESA-Formulario-T-16.pdf`

---

### Capítulo 9 · Introducción al Plan de Calidad
* **Subdocumento 9 del T-7:** *Plan de calidad*
* **Texto de introducción:** Resumen del capítulo y directrices de gobernanza de calidad.
* **9.1 Plan de Calidad:** Marco formal de calidad basado en la norma **ISO/IEC 25010** y modelos de madurez. Métricas de mantenibilidad, cobertura de pruebas automáticas, complejidad ciclomática y acoplamiento, fijando umbrales bloqueantes de paso a producción.
* **9.2 Estrategia de Aseguramiento de Calidad:**
  * Quality Gates, revisiones cruzadas de código (*peer reviews*), análisis estático (SAST) y análisis dinámico (DAST).
  * Estrategia de testing alineada a **ISO/IEC/IEEE 29119**: tipologías, niveles de prueba, gestión de datos sintéticos y automatización.
  * Mecanismos de verificación y validación (V&V) y matriz de trazabilidad entre requerimientos, diseño, código fuente, casos de prueba y releases.
* **9.3 Alineación con Plan de Trabajo:** Mapeo de actividades e hitos de calidad dentro de los paquetes de trabajo de la EDT y el cronograma del Capítulo 7.
* **Anexos:**
  * `EMPRESA-Formulario-T-13.pdf`
  * `EMPRESA-Formulario-T-17.pdf`

---

### Capítulo 10 · Introducción a los Servicios
* **Subdocumento 10 del T-7:** *Servicios de operación y niveles de servicio*
* **Texto de introducción:** Resumen del capítulo y modelo operacional de soporte.
* **10.1 Servicios de operación:**
  * Modelo de mesa de servicios basado en **ITIL 4**: niveles de soporte (L1, L2, L3), canales de atención omnicanal, ventanas horarias y matriz de escalamiento funcional/jerárquico.
  * Dimensionamiento cuantitativo de dotación de la mesa de servicio fundamentado en teoría de colas (modelo Erlang C o formulación matemática declarada).
  * Runbooks operativos, base de conocimiento (*KEDB*) y planes de automatización progresiva de incidentes rutinarios.
  * Pila de observabilidad integral (métricas, trazas, logs), correlación de eventos y monitoreo proactivo sintético.
* **10.2 Niveles de servicio:** Definición rigurosa de SLAs, SLOs y SLIs en concordancia con el **Art. 78°**. Acuerdos de nivel operacional internos (OLAs) y contratos de soporte con terceros (UCs) que sustentan contractualmente los compromisos exteriores.

---

### Capítulo 11 · Introducción a los Planes en Operación
* **Subdocumento 11 del T-7:** *Planes en operación*
* **Texto de introducción:** Resumen del capítulo y gestión del ciclo de vida en régimen.
* **11.1 Plan Mantención Preventiva / Evolutiva:**
  * Protocolos de mantenimiento preventivo, correctivo y evolutivo, estableciendo matrices de priorización y asignación de capacidad de ingeniería.
  * Política de parchado, actualización de dependencias, auditoría de deuda técnica y gestión proactiva ante obsolescencia tecnológica.
* **11.2 Plan Servicios de Operación:**
  * Marco de operación basado en Site Reliability Engineering (SRE): presupuestos de error (*error budgets*), erradicación sistemática del trabajo manual repetitivo (*toil reduction*) y autopsias sin culpa (*blameless post-mortems*).
  * Gestión de capacidad y optimización financiera de infraestructura en la nube bajo principios **FinOps**.
  * Calendario periódico de simulacros de desastre (DR drills) y pruebas de resiliencia (Chaos Engineering).

---

### Capítulo 12 · Introducción al Equipo de Trabajo, Subcontrataciones y Alianzas
* **Subdocumento 12 del T-7:** *Equipo de trabajo, subcontrataciones y alianzas*
* **Texto de introducción:** Resumen del capítulo y gobierno humano del proyecto.
* **12.1 Equipo de trabajo:**
  * Organigrama del proyecto, roles clave, responsabilidades operativas y matriz RACI.
  * Perfiles del personal clave nominado: currículos, certificaciones vigentes, porcentaje de dedicación y cronograma de participación.
  * Curva de dotación mensual por perfil, sincronizada con la nivelación de recursos del **Formulario T-15**.
  * Estrategia de retención de talento, mitigación de rotación y transferencia formal de conocimiento.
* **12.2 Subcontrataciones:** Análisis de conveniencia *Make vs. Buy*. Catálogo de empresas subcontratadas, justificación de idoneidad técnica, porcentaje de participación asignado (**Art. 73°**) y mecanismos de supervisión contractual.
* **12.3 Alianzas:** Socios estratégicos incorporados para este proyecto en particular: roles asumidos, participación relativa y marco de gobernanza conjunto.
* **Anexos:**
  * `EMPRESA-Formulario-T-8.pdf`

---

### Capítulo 13 · Introducción a las Innovaciones
* **Subdocumento 13 del T-7:** *Innovaciones*
* **Texto de introducción:** Resumen del capítulo y estrategia de valor agregado.
* **13.1 Innovación 1 — Producto o servicio**
* **13.2 Innovación 2 — Proceso**
* **13.3 Innovación 3 — Tecnológica o de arquitectura**
* **13.4 Innovación 4 — Modelo de negocio o de contratación**
* **13.5 Innovación 5 — Experiencia de usuario, sostenibilidad o impacto social**
* *Regla de redacción obligatoria:* El título de cada acápite se conserva idéntico a lo indicado (`13.X Innovación X`); el primer párrafo bajo el título declara explícitamente el tipo y nombre propio de la innovación.
* *Contenido de cada innovación:* Cada una de las cinco innovaciones desarrolla obligatoriamente los siete elementos del **Art. 29°** y su trazabilidad con arquitectura, paquetes EDT y flujo de caja, citando fuentes académicas o de industria en norma APA 7.ª edición.
* **Anexos:**
  * `EMPRESA-Formulario-T-19.pdf`

---

### Capítulo 14 · Introducción a las Ventajas, Beneficios y Consolidación
* **Subdocumento 14 del T-7:** *Ventajas, beneficios y consolidación*
* **Texto de introducción:** Resumen del capítulo y cierre integrador de la oferta técnica.
* **14.1 Ventajas:** Síntesis consolidada de la propuesta de valor diferencial desde una óptica de ingeniería de sistemas integral.
* **14.2 Beneficios y consolidación:**
  * Cuantificación de beneficios directos para el CLIENTE: mejoras de throughput/latencia, reducción de MTTR, elevación de disponibilidad porcentual y ahorros de costos operacionales directos e indirectos.
  * Demostración analítica de cómo la propuesta optimiza el balance de la cuádruple restricción: alcance, tiempo, costo y calidad.
  * Evidencia de coherencia arquitectónica y tecnológica transversal entre todos los subdocumentos.
  * Demostración de trazabilidad integral extremo a extremo (*End-to-End*): desde los requerimientos de licitación hasta la operación y mantenimiento continuo a 36 meses.
