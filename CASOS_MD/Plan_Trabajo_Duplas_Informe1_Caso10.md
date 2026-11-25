# Plan de trabajo por duplas

## Informe y Presentación 1 · Licitación N.º TFEP-01/2026

## Caso 10 - Transporte de Carga · Transportes Curimón S.A.

**Asignatura** **Taller de Formulación de Proyectos Informáticos - ICI-**

Unidad académica Escuela de Informática, Pontificia Universidad Católica de Valparaíso

Documentos que rigen Bases Administrativas FEP01.26 · Bases Técnicas Transversales

FEP02.26 · Bases Técnicas del Caso 10 (FEP03.10.26)

| Equipo | 8 personas, organizadas en 4 duplas |
|:--- |:--- |
| Entrega del Informe 1 | 07-09-2026 (Formulario T-20, ítem 6) |
| Presentación preparatoria 1 | Entre el 14-09-2026 y el 25-09-2026 · 15 min de exposición + 15 |

Entrega del Informe 1 07-09-2026 (Formulario T-20, ítem 6)

Presentación preparatoria 1 Entre el 14-09-2026 y el 25-09-2026 · 15 min de exposición + 15 min de preguntas

Cierre del período de consultas 01-09-2026 (Formulario T-20, ítem 4)

Objeto de este documento Repartir el trabajo del Informe 1 entre las 4 duplas, con fuentes, páginas y puntos de sincronización

Toda referencia de página corresponde a la numeración impresa en el pie de cada documento.

Para ubicarla en el lector de PDF, súmese 1 (la portada no está numerada).

## 1. Qué exige exactamente esta entrega (y cuánto vale cada parte)

## El contenido del Informe 1 no lo define el enunciado de clases sino el Formulario T-22 de las Bases Administrativas (pág. 68), y su

ponderación el **Formulario T-21** (págs. 66-67). Ambos deben leerse juntos, porque T-21 incluye un ítem que el enunciado resumido no menciona.

**Subdoc.** **Ítem evaluado en el Informe 1** **Peso Informe 1** **Formularios y fuente en T-7 (págs. 57-60)**

Transversal Formalidad y contenido del documento / cumplimiento de instrucciones **4 %** Artículo 40° (págs. 26)

Presentación de la empresa **4 %** Formulario T-6 (pág. 56)

Resumen ejecutivo, comprensión del problema y de la necesidad **11 %** T-7, Subdocumento 2

Esquema de solución y alcance **21 %** Formulario T-12 (pág. 62)

4.1 Arquitectura lógica: esquema de solución + arquitectura lógica **16 %** T-7, Subdocumento 4

4.2 Arquitectura física + tecnologías de software + implementos (HW/SW) + data center primario y secundario **16 %** Formulario T-11 (pág. 62)

Modelo y gestión de datos **11 %** T-7, Subdocumento 5

Innovaciones (cartera obligatoria de 5) **17 %** Formulario T-19 (pág. 64)

# TOTAL **100 %**

## Dos advertencias antes de repartir el trabajo.

1. El **Subdocumento 5 «Modelo y gestión de datos» (11 %)** forma parte del Informe 1 aunque el listado de viñetas del T-22 no lo mencione: el propio T-22 cierra diciendo «De la Propuesta Técnica corresponde a los subdocumentos: 1, 2, 3, 4, **5** y 13». Si nadie lo escribe, se pierde un ítem completo y, por el Artículo 58°, un ítem bajo 30 puntos excluye la oferta. 2. La **arquitectura vale 32 %** repartida en dos ítems distintos (4.1 y 4.2) y las **innovaciones 17 %**. Entre ambas se llevan la mitad del informe: no pueden ser lo último que se escriba.

## Reglas de forma que valen 4 % (Artículo 40°, pág. 26)

## Foliación correlativa, sin saltos, en el extremo inferior derecho. Su falta es excluyente.

## Media firma del representante en cada página; firma completa en carátula.

## Índice detallado con numeración de páginas y hoja resumen al inicio.

## PDF con texto seleccionable; tamaño carta u oficio, vertical; cuerpo ≥ 11 pt y ≥ 9 pt en tablas y figuras.

## Toda cita y referencia en norma APA 7.ª edición.

## Nomenclatura de archivo conforme a los Artículos 49° a 51°: un archivo mal nominado se considera no presentado.

## 2. Reparto general por duplas

## El reparto equilibra tres cosas a la vez: el peso porcentual, el volumen real de redacción y las dependencias entre secciones. Las duplas

que dependen una de otra están contiguas en la cadena de sincronización del punto 5.

**Dupla** **Responsabilidad principal** **Peso** **Entregables concretos que produce** **D1** Empresa y Problema

Subdoc. 1 (4 %) + Subdoc. 2 (11 %) + custodia de la formalidad transversal (4 %)

**19 %** Ficha de empresa oferente · Formulario T-6 con 3 proyectos · Capítulo de comprensión del problema con datos duros · Mapa de actores e interesados · Resumen ejecutivo (se escribe al final) · Índice, foliación, formato y referencias APA de todo el informe **D2** Solución y Alcance

Subdoc. 3 (21 %) **21 %** Esquema de solución · Catálogo de RF y RNF trazable al origen · Reparto Etapa 1 / Etapa 2 justificado · Exclusiones y restricciones · Registro de supuestos (26 decisiones del numeral 16.1) · Plan de adhesión de los 148 transportistas · Criterios de aceptación · Base del Formulario T-12 **D3** Arquitectura lógica y Datos

Subdoc. 4.1 (16 %) + Subdoc. 5 (11 %) **27 %** Diagrama de las 8 capas obligatorias · Módulos, límites de contexto e interfaces · Arquitectura de integración y de seguridad lógica · Registro de decisiones de arquitectura (ADR) · Modelo de dominio · Motor y paradigma de persistencia justificados · Política de retención y migración **D4** Arquitectura física e Infraestructura

Subdoc. 4.2 (16 %) **16 %** Tabla de emplazamiento nube / on-premise componente por componente · Especificación del dispositivo a bordo · Especificación de tecnologías de software · Data center primario y secundario · Dimensionamiento de enlaces y de datos móviles - Formulario T-11

**Compartido: Subdoc. 13 - Innovaciones** **17 %** Una ficha T-19 por dupla según afinidad (ver punto 4). D2 asume dos fichas.

## Por qué D4 tiene menos peso porcentual y no está subcargada. El ítem 4.2 exige cinco entregables distintos (arquitectura

física, tecnologías de software, implementos de hardware y software, data center primario y data center secundario) más el Formulario T-11 completo. Es el ítem con mayor volumen de especificación del informe. D3, en cambio, concentra más porcentaje pero menos páginas de detalle.

Plan de trabajo por duplas - Informe 1 \| Caso 10 Transporte de Carga \| TFEP-01/2026 2 / 9

## 3. Ficha de trabajo de cada dupla

**Dupla 1 - Presentación de la empresa y comprensión del problema ** **19 %** **Qué debe escribir**

**Empresa oferente:** reseña de trayectoria, giro, productos y servicios, estructura organizacional, dotación, certificaciones institucionales y alianzas tecnológicas, modelo interno de calidad y seguridad, y experiencia en la industria de transporte de carga.

**Formulario T-6:** al menos tres proyectos finalizados y en operación en los últimos cinco años, con cliente, alcance, arquitectura (nube / on-premise / híbrida), nivel de servicio comprometido, volumen soportado y contraparte de referencia.

**Comprensión del problema:** dimensionamiento realista con datos duros del caso, contexto de la industria, particularidades operacionales, regulatorias y estacionales, actores afectados con nivel de influencia e interés, y supuestos declarados con su fundamento.

**Resumen ejecutivo:** se redacta al final, cuando las demás duplas ya cerraron su versión 1. **Fuentes obligatorias** **Documento** **Capítulos y páginas**

Bases Técnicas Caso 10 **Cap. 1** Cómo llegamos a esta licitación (págs. 4-5) · **Cap. 2** La compañía, flota, cifras y personas (págs. 5-7) · **Cap. 3** El territorio y sus nodos (pág. 8) · **Cap. 7** Indicadores del problema (págs. 14-16) · **Cap. 8** Las diez entrevistas (págs. 17-21) · **Cap. 12** Marco normativo (págs. 25-26) · **Cap. 16.2** Materias a investigar (págs. 36-37) · **Anexo A** Mapa de flujos actuales (págs. 45-46) · **Anexo C** Glosario (págs. 47-48)

Bases Administrativas Artículo 40° Forma y presentación (pág. 26) · Artículos 45° a 47° Informes preparatorios (pág. 28) · Artículo 56° Escala de puntaje (págs. 31-32) · Formulario T-6 (pág. 56) · Formulario T-7 subdocumentos 1 y 2 (pág. 57) · Formulario T-22 (pág. 68)

Bases Técnicas Transversales **Cap. 15.2 y 15.3** Certificaciones institucionales y del personal (págs. 27-28) · **Cap. 23** Información corporativa y presencia digital (págs. 39-40)

**Datos duros que no pueden faltar en el capítulo del problema**

374 camiones gestionados, de los cuales el **60,4 % no es de la compañía**; 148 transportistas subcontratados.

454 conductores bajo programación: 196 propios y **258 que no son trabajadores de la compañía**. Control de jornada existente sobre 196 de 454.

≈ 96.000 viajes y ≈ 41.000.000 km al año; 26 % de los kilómetros en vacío.

≈ 6.000 fechas de vencimiento vivas en cuatro planillas separadas; 0 tacógrafos descargados; 61 tractocamiones con telemetría sin usar.

$ 340 millones facturados por espera con 71 % objetado; 4,2 % de documentos de respaldo incompletos; liquidación mensual de 9 días con 11 % de corrección.

3 de 8 contratos principales bajo costo (31 % del ingreso), el peor a −14 % durante 4 años; margen operacional de 9 %.

142 detenciones por sobrepeso en 2025 y 1 por documentación de carga peligrosa; 4 siniestros con lesiones en 3 años.

**Trampas de esta sección.** El T-22 exige explícitamente «no mezclar con la solución»: cualquier frase que proponga tecnología en el capítulo del problema descuenta puntaje aquí y no lo suma en la sección 3. El Capítulo 8 entrega diez entrevistas *contradictorias entre* *sí*; las contradicciones se describen como hallazgo (quién quiere qué y por qué chocan), no se resuelven todavía -eso es trabajo de D2 -. Toda cifra debe venir referenciada y toda información externa citada en APA 7.

Plan de trabajo por duplas - Informe 1 \| Caso 10 Transporte de Carga \| TFEP-01/2026 3 / 9

## Dupla 2 - Esquema de solución y alcance 21 %

## Qué debe escribir

## Descripción de la solución propuesta y su coherencia demostrada con cada dolor identificado por D1.

## Catálogo de requerimientos funcionales y no funcionales, priorizado y trazable a su origen (párrafo, entrevista, indicador o

restricción). El Capítulo 17.1 del caso es explícito: «Debe controlarse la jornada del conductor» *no es un requerimiento*.

## Alcance de la Etapa 1 y de la Etapa 2 con separación explícita y criterio de asignación, haciéndose cargo de la preferencia del

comité (numeral 13.1) **y de las dos objeciones registradas**: la renegociación de 2027 de dos contratos bajo costo y la imposibilidad de prometer posición en tiempo real antes de negociar con los dueños de camión.

## Exclusiones explícitas, supuestos y restricciones del alcance.

## Registro de supuestos sobre las 26 decisiones no tomadas del numeral 16.1; son obligatorias la 1 (cómo se obtiene la jornada de un

conductor externo), la 2 (qué se ofrece a los 148 transportistas) y la 25 (cómo se despliega el equipamiento a bordo).

## Plan de adhesión de los transportistas subcontratados: qué se les pide, qué se les ofrece, con qué instrumento contractual, en

qué plazo, cómo se mide la adhesión y qué ocurre con quien no adhiere. Es un producto propio de este caso (Cap. 17.1) y sin él «toda función que dependa de ellos carece de sustento».

## Estrategia para obtener el apoyo de los grupos de interés clave y criterios de aceptación del alcance.

## Fuentes obligatorias **Documento** **Capítulos y páginas**

Bases Técnicas Caso 10 **Cap. 9** Expectativas de negocio, 9.1 a 9.11 (págs. 22-23) · **Cap. 10** Las 14 restricciones no negociables (págs. 23-24) - **Cap. 11** Exclusiones explícitas (págs. 24-25) · **Cap. 13** Horizonte, prioridades, hitos externos y estrategia de puesta en producción (págs. 26-28) · **Cap. 16.1** Las 26 decisiones pendientes (págs. 34-36) · **Cap. 17** El trabajo de traducción exigido (págs. 38-41) · **Cap. 18** Los 29 criterios de aceptación (págs. 41-43) · **Cap. 19** Cómo se evaluará este caso (págs. 43-44) · **Anexo B** Perfil del viaje y calendario operacional (págs. 46-47)

Bases Administrativas Artículo 14° Objeto (pág. 10) · Artículo 15° Estructura del suministro y etapas (pág. 11) · Artículo 17° Cronograma obligatorio de 56 meses (págs. 12-13) · Artículo 18° Hitos y criterios de aceptación (pág. 13) · Formulario T-7 subdocumento 3 (pág. 57) · Formulario T-12 (pág. 62)

Bases Técnicas Transversales **Cap. 16** Módulos transversales obligatorios (págs. 29-31) · **Cap. 17** Canales digitales y movilidad (págs. 31-32) · **Cap.** **20** Implantación, pruebas y criterios de aceptación (págs. 34-35)

## Trampas de esta sección. El Capítulo 13.1 advierte que «una propuesta que se limite a repetir el orden de preferencia del comité sin

analizarlo será evaluada como falta de criterio profesional». El Capítulo 11 aclara que lo excluido *no puede ignorarse en el diseño*: las dependencias que genera deben quedar identificadas. Los criterios 27, 28 y 29 del Capítulo 18 (adhesión medible, alerta de jornada con tiempo para detenerse, y control del dueño de camión sobre sus datos) son, según el propio caso, «los tres que deciden este caso».

Plan de trabajo por duplas - Informe 1 \| Caso 10 Transporte de Carga \| TFEP-01/2026 4 / 9

**Dupla 3 - Arquitectura lógica y modelo de datos ** **27 %** **Qué debe escribir**

**Esquema de solución + arquitectura lógica:** las ocho capas obligatorias del numeral 2.1 transversal (presentación, borde, puerta de enlace, servicios de negocio, integración y eventos, datos, seguridad transversal y observabilidad transversal), con módulos, límites de contexto, responsabilidades e interfaces.

**Arquitectura de integración:** catálogo de servicios, contratos versionados, mensajería asíncrona, y **capa anticorrupción** frente al sistema de gestión de transporte de 2013 y al sistema contable, que se mantiene como único emisor de documentos tributarios.

**Arquitectura de seguridad lógica:** Zero Trust, identidad, cifrado a nivel de campo para los datos de los 258 conductores externos y para las tarifas pactadas con cada transportista (RT-11.10), y registro de consultas a información sensible (RT-16.09).

**Registro de decisiones de arquitectura (ADR)** fechado, con alternativas descartadas y criterio de decisión (RT-02.04). Como mínimo debe existir un ADR sobre el destino del sistema de gestión de 2013: reemplazar, conservar e integrar, o envolver y sustituir por partes.

**Modelo y gestión de datos:** dominio de información (viaje, camión, conductor, transportista, cliente, documento, evento de jornada, posición, liquidación), selección del motor y del paradigma de persistencia con justificación CAP, separación entre almacenamiento transaccional y analítico, estrategia de migración y conciliación, y política de retención. **Fuentes obligatorias** **Documento** **Capítulos y páginas**

Bases Técnicas Transversales **Cap. 2** Modelo de arquitectura de referencia, RT-02.01 a RT-02.14 (págs. 6-7) · **Cap. 5** Datos, integración, migración y analítica, RT-05.01 a RT-05.30 (págs. 11-13) · **Cap. 11** Seguridad de la información (págs. 23-25) · **Cap. 12** Identidad, acceso y sesiones (págs. 25-26) · **Cap. 14** Observabilidad (pág. 27) · **Cap. 16** Módulos transversales (págs. 29-31) · **Cap. 18** IA, si se incorpora (pág. 32)

Bases Técnicas Caso 10 **Cap. 5** Los sistemas que existen hoy y su destino (págs. 12-13) · **Cap. 14.1 y 14.2** Volumetría entregada y volumetría a estimar (págs. 29-31) · **Cap. 15** Parámetros «según caso»: RT-03.10, RT-03.13, RT-05.10, RT-05.15, RT05.23, RT-05.29, RT-09.01, RT-09.02, RT-11.10, RT-12.11, RT-16.09, RT-16.14, RT-16.21, RT-16.30 (págs. 31-34) · **Cap.** **17.4** Los 14 asuntos que la arquitectura debe resolver (págs. 39-40) · **Anexo A** Flujos actuales (págs. 45-46)

Bases Administrativas Artículo 19° Arquitectura y diseño (pág. 14) · Artículo 23° Datos, integración e interoperabilidad (pág. 16) · Formulario T-7 subdocumentos 4 y 5 (págs. 57-59)

**Umbrales del caso que la arquitectura lógica debe sostener**

Asignación de viaje con verificación bloqueante de jornada, habilitaciones y aptitud del equipo: **≤ 30 segundos** (RT-09.01).

Emisión del documento electrónico de transporte: ≤ 90 s. Publicación de posición al cliente: ≤ 2 min. Evento de botón de emergencia: ≤ 15 s con cobertura.

Operación desconectada del dispositivo a bordo: **72 horas continuas sin pérdida de ningún registro** (RT-03.10) y sincronización ≤ 20 min al reconectar, con cientos de unidades saliendo a la vez de zona de sombra (RT-03.13).

Retención (RT-05.10): jornada 5 años; documento de transporte y antecedentes del viaje 6 años; siniestros 10 años; series de posición y telemetría 2 años en línea con política de agregación declarada.

**Trampas de esta sección.** El Capítulo 19 del caso dice que la arquitectura debe «ser propia de esta operación y no un diagrama de referencia con el nombre cambiado». El numeral 2.3 transversal advierte que adoptar microservicios sin volumen que lo justifique «es un error de ingeniería y se evaluará como tal»: hay que comparar al menos dos alternativas y explicar la descartada. La evidencia de jornada debe estar diseñada para **resistir una alegación de manipulación** por cualquiera de las partes (decisión 24 del numeral 16.1).

Plan de trabajo por duplas - Informe 1 \| Caso 10 Transporte de Carga \| TFEP-01/2026 5 / 9

**Dupla 4 - Arquitectura física, infraestructura y equipamiento de terreno ** **16 %** **Qué debe escribir**

**Tabla de emplazamiento** que asigne cada componente a nube o a on-premise y justifique la decisión por latencia, criticidad, volumen, regulación, conectividad y costo total de propiedad (Artículo 16.2: una asignación no justificada es observación grave).

**Especificación del dispositivo a bordo** como componente on-premise distribuido en 374 unidades (RT-06.01): marca y modelo de referencia, condiciones de cabina (vibración, temperatura extrema del norte, polvo, alimentación del vehículo), grado de protección, almacenamiento local para 72 h, ciclo de vida, actualización remota, plan de reposición y costo unitario estimado, sabiendo que **sólo** **puede intervenirse cuando el camión pasa por un terminal**.

**Especificación de tecnologías de software** ofertadas, con versión, fecha de fin de soporte y plan de actualización que cubra los 56 meses (numeral 1.6 transversal).

**Data center primario:** la sala de equipos de San Bernardo (26 m², habilitada en 2013, con climatización tipo split, 20 minutos de autonomía) **no cumple el Capítulo 6 transversal**; hay que declarar si se remedia o se reemplaza y especificar la solución.

**Data center secundario y recuperación ante desastres** conforme al Capítulo 7 transversal: modalidad, distancia, RTO ≤ 4 h y RPO $$ \leq 15 min. $$

**Red y enlaces:** respaldo de enlace en los cuatro terminales regionales (tres no lo tienen hoy), ancho de banda por sitio en régimen normal y en peak, y caracterización en terreno de la cobertura móvil real de las rutas, que es una actividad con costo y plazo y no un supuesto (RT-03.24).

**Costo recurrente de datos móviles** de la flota derivado de la frecuencia de muestreo elegida: es una decisión de diseño con impacto directo en una empresa de 9 % de margen. **Fuentes obligatorias** **Documento** **Capítulos y páginas**

Bases Técnicas Transversales **Cap. 3** Modelo híbrido nube / on-premise y conectividad, RT-03.01 a RT-03.24 (págs. 8-10) · **Cap. 6** Site principal onpremise, RT-06.01 a RT-06.34 (págs. 14-17) · **Cap. 7** Site secundario y recuperación ante desastres (págs. 17-18) · **Cap. 8** Hardware, puestos de trabajo y equipamiento de terreno, RT-08.01 a RT-08.19 (págs. 18-20) · **Cap. 9** Desempeño y capacidad (págs. 21-22) · **Cap. 10** Disponibilidad y resiliencia (pág. 22)

Bases Técnicas Caso 10 **Cap. 3** Nodos: terminales, cabina, ruta, puntos de cliente, paso fronterizo (pág. 8) · **Cap. 6** Conectividad, seguridad y condiciones del sitio (págs. 13-14) · **Cap. 10** Restricciones no negociables 1 a 14 (págs. 23-24) · **Cap. 14.2** Volumetría de sistema a estimar (pág. 30) · **Cap. 15** RT-03.10, RT-03.24, RT-06.01, RT-17.06, RT-21.16 (págs. 31-34)

Bases Administrativas Artículo 16° Modelo de despliegue híbrido obligatorio (págs. 11-12) · Artículo 20° Disponibilidad y recuperación (págs. 14-15) · Formulario T-11 (pág. 62)

**Trampas de esta sección.** El Artículo 16° prohíbe una solución exclusivamente en nube o exclusivamente on-premise. El Capítulo 6.1 transversal penaliza igual sobredimensionar que subdimensionar el recinto: «ambos revelan que el cálculo de capacidad no se hizo». El caso agrega dos límites duros: ningún equipamiento puede afectar la garantía del vehículo ni interferir con sus sistemas de seguridad (restricción 6), y los dispositivos instalados en camiones de terceros **pertenecen a sus dueños** y no pueden intervenirse ni reemplazarse sin acuerdo expreso (restricción 3).

Plan de trabajo por duplas - Informe 1 \| Caso 10 Transporte de Carga \| TFEP-01/2026 6 / 9

## 4. Innovaciones: reparto de las cinco fichas (17 %)

## El Artículo 28° exige cinco innovaciones, una por cada tipo obligatorio, sin repetir tipo. El T-22 advierte que «en ningún caso puede

presentarse sólo el título de la innovación»: cada una debe desarrollarse en idea, tecnología, alcance, forma de implementación y resultados esperados. Cada ficha se documenta con los **siete elementos del Artículo 29°** en el Formulario T-19 (pág. 64).

**Tipo** **Categoría (Art. 28°, pág.** **19)** **Dupla** **Terreno del caso donde buscarla**

| Producto o servicio | D2 | Portal del transportista con visibilidad de viajes y liquidación en curso; evidencia de jornada que le sirve | a él para acreditar que está en regla (criterio 29) |
|:--- |:--- |:--- |:--- |
| Proceso | D4 | Despliegue camión por camión con ventana de 6 días; actualización remota del parque; incorporación | de la intervención del taller externo a la hoja de vida del equipo |
| Tecnológica o de arquitectura | D3 | Operación desconectada de 72 h con reconexión masiva; unificación de tres plataformas de | posicionamiento; integración de solo lectura a la telemetría de fábrica de 61 tractocamiones |

Proceso **D4** Despliegue camión por camión con ventana de 6 días; actualización remota del parque; incorporación de la intervención del taller externo a la hoja de vida del equipo

Tecnológica o de arquitectura **D3** Operación desconectada de 72 h con reconexión masiva; unificación de tres plataformas de posicionamiento; integración de solo lectura a la telemetría de fábrica de 61 tractocamiones Modelo de negocio o de contratación

**D2** Quién paga el dispositivo en un camión ajeno; consentimiento granular y revocable del dueño de camión sobre qué comparte y con quién; incentivos por adhesión

Experiencia de usuario, sostenibilidad o impacto social

**D1** Interfaz operable con una sola mano y con guantes, sin interacción en marcha (RT-13.08 y RT-13.12); alerta de jornada con anticipación al lugar seguro de detención; emisiones por tonelada-kilómetro verificables

## Qué no se acepta como innovación (Artículo 30.2 y Capítulo 26 transversal): la sola adopción de una tecnología que ya es estándar

de la industria; la mención de una tendencia sin diseño de incorporación; y una funcionalidad que las Bases Técnicas *ya exigen* presentada como innovación. La pertinencia al caso pesa más que la novedad tecnológica en abstracto.

## 5. Puntos de sincronización obligatorios

## El Artículo 57.2 permite descontar puntaje en cualquier ítem por incoherencia entre secciones, y el Capítulo 19 del caso evalúa

expresamente la «consolidación». Estas reuniones no son opcionales: son el mecanismo que evita perder puntaje transversal.

**Hito** **Participantes** **Qué se acuerda** **Salida verificable** **S0** Arranque

Las 4 duplas Nombre y perfil de la empresa oferente, glosario común, plantilla de documento, criterio de citación APA y responsable de foliación

Plantilla del informe creada y repartida; acta con la identidad de la empresa **S1** Problema ↔ Alcance

D1 + D2 Que cada dolor del Capítulo 7 tenga destino: resuelto en Etapa 1, en Etapa 2, excluido o declarado como supuesto. Congelar la lista de actores

Tabla dolor → requerimiento → etapa, que después alimenta el Formulario T- **S2** Consultas al CLIENTE

Las 4 duplas Consolidar el registro de vacíos y consultas antes del cierre del **01-09-** **2026**. Una consulta bien formulada es, según el Artículo 43°, un antecedente de calidad profesional

Listado de consultas enviado por el canal oficial **S3** Alcance ↔ Arquitectura

D2 + D3 + D4 Que cada capacidad comprometida tenga un componente que la implemente y ninguno sobre; decisión sobre el sistema de gestión de 2013; decisión sobre frecuencia de muestreo

Matriz capacidad → componente → capa → emplazamiento **S4** Lógica ↔ Física ↔ Datos

D3 + D4 Emplazamiento definitivo de cada componente, volúmenes de almacenamiento por política de retención, ancho de banda por terminal y comportamiento en reconexión masiva

Tabla de emplazamiento firmada y supuestos de volumetría del numeral 14.2 completos **S5** Innovaciones

Las 4 duplas Revisión cruzada de las 5 fichas: que no se repita tipo, que ninguna sea una exigencia disfrazada y que cada una tenga los 7 elementos del Artículo 29°

Cinco fichas T-19 completas y trazadas a la arquitectura **S6** Consolidación

Las 4 duplas Lectura cruzada: cada dupla revisa la sección de otra buscando contradicciones. D1 cierra resumen ejecutivo, índice, foliación y referencias Informe v2 completo, foliado y con índice **S7** Ensayo

Las 4 duplas Ensayo cronometrado de 15 minutos y simulacro de preguntas Presentación cerrada y tiempos medidos

## Regla de sincronización permanente. Ninguna dupla cambia una decisión que otra ya usó sin avisar en el canal del equipo. Los

tres acuerdos más frágiles -cómo se obtiene la jornada del conductor externo, qué se le ofrece al transportista y qué pasa con el sistema de 2013- atraviesan las cuatro secciones: si cambian, cambian en las cuatro.

Plan de trabajo por duplas - Informe 1 \| Caso 10 Transporte de Carga \| TFEP-01/2026 7 / 9

## 6. Calendario hasta la entrega

## Entrega del Informe 1: lunes 07-09-2026. Cierre de consultas: martes 01-09-2026. La presentación se realiza entre el 14 y el 25 de septiembre. **Fecha** **Hito** **Trabajo de las duplas**

Jue 27 ago **S0** - Arranque Lectura dirigida: D1 Caps. 1-3, 7 y 8; D2 Caps. 9-13 y 16-19; D3 Caps. 5, 14 y 15 + Transversales 2 y 5; D4 Caps. 3, 6 y 10 + Transversales 3, 6, 7 y 8

Vie 28 - Dom 30 ago Borrador v0 Cada dupla produce el esqueleto de su sección con los títulos exigidos por el T-7 y las preguntas abiertas marcadas

| Lun 31 ago | S1 - Problema ↔ Alcance | D1 cierra datos y actores; D2 cierra la tabla dolor → requerimiento → etapa |
|:--- |:--- |:--- |
| Mar 1 sep | S2 - Consultas (fecha límite) | Envío del registro de vacíos y consultas al CLIENTE. Todas las duplas aportan preguntas |
| Mié 2 sep | S3 - Alcance ↔ Arquitectura | Matriz capacidad → componente. D3 y D4 quedan habilitadas para diagramar |
| Jue 3 sep | Versión 1 | D1, D2 cierran v1 de sus secciones; D3 y D4 avanzan diagramas y tablas de especificación |
| Vie 4 sep | S4 - Lógica ↔ Física ↔ Datos | S5 - Innovaciones |

Mar 1 sep **S2** - Consultas (fecha límite) Envío del registro de vacíos y consultas al CLIENTE. Todas las duplas aportan preguntas

Mié 2 sep **S3** - Alcance ↔ Arquitectura Matriz capacidad → componente. D3 y D4 quedan habilitadas para diagramar

Jue 3 sep Versión 1 D1, D2 cierran v1 de sus secciones; D3 y D4 avanzan diagramas y tablas de especificación

Vie 4 sep **S4** - Lógica ↔ Física ↔ Datos **S5** - Innovaciones

Tabla de emplazamiento y supuestos de volumetría cerrados; revisión cruzada de las cinco fichas T-19

Sáb 5 sep **S6** - Consolidación Lectura cruzada entre duplas; D1 redacta el resumen ejecutivo con el informe ya cerrado

Dom 6 sep Cierre formal + **S7** Índice, foliación, firmas, formato, APA, nomenclatura del archivo. Ensayo cronometrado de la presentación

**Lun 7 sep** **Entrega del Informe 1** Envío en el plazo del Formulario T-20

Sem. 14-25 sep Presentación 1 Ensayo final el día previo; llevar el informe impreso y foliado

## 7. Reparto de los 15 minutos de presentación

## El Artículo 45.1 exige que exponga más de un integrante y faculta al CLIENTE para designar quién expone cada sección. En

consecuencia, las ocho personas deben poder defender cualquier parte, aunque el reparto por defecto sea el siguiente.

**Minutos** **Expone** **Sección** **Mensaje que debe quedar instalado**

| 0:00 - 1:30 | D1 | La empresa | Trayectoria y experiencia verificable en operaciones distribuidas y | desconectadas |
|:--- |:--- |:--- |:--- |:--- |
| 1:30 - 4:30 | D1 | El problema | La responsabilidad y el control no coinciden: 60 % de la flota es ajena | y 258 conductores no son trabajadores |
| 4:30 - 8:00 | D2 | Esquema de solución y alcance | Qué entra en Etapa 1, qué en Etapa 2 y con qué se convence a 148 | dueños de camión |
| 8:00 - 10:30 | D3 | Arquitectura lógica y datos | Cómo se construye evidencia de jornada oponible y cómo opera 72 h | sin cobertura |
| 10:30 - 13:00 | D4 | Arquitectura física | Carácter híbrido, dispositivo a bordo y ritmo físico de despliegue | impuesto por la operación |
| 13:00 - 15:00 | D2 y D4 | Cartera de cinco innovaciones | Cinco tipos distintos, todas pertinentes al caso y con indicador de | verificación |

1:30 - 4:30 D1 El problema La responsabilidad y el control no coinciden: 60 % de la flota es ajena y 258 conductores no son trabajadores

4:30 - 8:00 D2 Esquema de solución y alcance Qué entra en Etapa 1, qué en Etapa 2 y con qué se convence a 148 dueños de camión

8:00 - 10:30 D3 Arquitectura lógica y datos Cómo se construye evidencia de jornada oponible y cómo opera 72 h sin cobertura

10:30 - 13:00 D4 Arquitectura física Carácter híbrido, dispositivo a bordo y ritmo físico de despliegue impuesto por la operación

13:00 - 15:00 D2 y D4 Cartera de cinco innovaciones Cinco tipos distintos, todas pertinentes al caso y con indicador de verificación

## Preguntas que conviene tener respondidas antes de entrar

## ¿De qué fuente se obtiene la jornada de un conductor que no es trabajador de la compañía y que pudo haber manejado antes para otro cliente?

## ¿Quién paga el dispositivo instalado en un camión de un tercero, quién lo administra y qué ocurre con él si ese transportista deja de trabajar con la compañía?

## ¿Qué pasa cuando la verificación bloqueante impide un viaje ya comprometido con un cliente? ¿Quién autoriza la excepción y con qué registro?

## ¿Cómo se registra la hora de llegada y salida en la instalación de un tercero, sin intervención del conductor y sin instalar equipamiento allí?

## ¿Qué se hace con el sistema de gestión de transporte de 2013 y por qué?

## ¿Cómo opera la solución durante el largo período en que una parte de la flota estará equipada y otra no?

## 8. Lista de verificación antes de entregar **✓** **Elemento** **Dónde se exige**

Los seis contenidos del T-22 desarrollados, incluido el modelo y gestión de datos

Formulario T-22 (pág. 68) y T-21 (págs. 66-67)

Formulario T-6 con al menos tres proyectos verificables Formulario T-6 (pág. 56)

Cinco fichas de innovación completas, una por tipo, con los siete elementos

Artículos 28° y 29° (pág. 19) y Formulario T-19 (pág. 64)

Plan de trabajo por duplas - Informe 1 \| Caso 10 Transporte de Carga \| TFEP-01/2026 8 / 9

Registro de supuestos con las decisiones 1, 2 y 25 resueltas explícitamente Caso, Caps. 16.1 y 17.1 (págs. 34-36 y 38)

Diagramas propios de la operación, no genéricos, con el carácter híbrido visible

Artículo 16° (págs. 11-12) y Caso, Cap. 19 (págs. 43-44)

Índice detallado, foliación correlativa sin saltos y firmas Artículo 40° (pág. 26)

PDF con texto seleccionable, cuerpo ≥ 11 pt, tablas ≥ 9 pt, referencias APA 7 Artículo 40.4 (pág. 26)

Ningún dato de precio en el informe técnico Artículo 50.2 (pág. 29)

Archivo nominado según la convención exigida Artículos 49° a 51° (pág. 29)

## Y para el Informe 2. El Artículo 46° obliga a incorporar, en la instancia siguiente, una tabla de trazabilidad observación →

**respuesta → sección modificada** con las observaciones que el CLIENTE formule en esta presentación. Conviene que alguien de D1 tome acta literal durante los 15 minutos de preguntas: esas observaciones son vinculantes y su omisión se evalúa como observación grave.

Plan de trabajo por duplas - Informe 1 \| Caso 10 Transporte de Carga \| TFEP-01/2026 9 / 9