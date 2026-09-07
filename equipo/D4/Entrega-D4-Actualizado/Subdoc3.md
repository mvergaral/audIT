# Esquema de Solución y Alcance

**Subdocumento N.º 3**

| | |
|---|---|
| Empresa | audIT, Empresa N.º 10 |
| Licitación | Licitación Pública Internacional N.º TFEP-01/2026, Caso 10 Transporte de Carga |
| Proyecto | Plataforma Digital de Misión Crítica para Transporte de Carga |
| Cliente | Transportes Curimón S.A. |
| Instancia | Informe Preparatorio 1, Oferta Técnica Sobre N.º 2 |
| Contenido | Decisiones estructurantes, catálogo de requisitos, alcance por etapas, plan de adhesión, consultas y contradicciones detectadas. |
| Fecha | 7 de septiembre de 2026 |

---

## Esquema de solución y alcance


### Principio rector


El registro operacional de esta empresa no vive en un servidor. Vive en 374 camiones, y la nube es
donde se consolida. De ese enunciado se desprenden las tres decisiones que ordenan la propuesta.


### Decisión primera. El sujeto obligado de la acreditación de jornada


El mandante no necesita saber dónde estuvo un conductor externo ni para quién manejó. Necesita un
veredicto en el momento de asignar, apto o no apto, y necesita poder acreditar después que lo
verificó. Es un dato derivado, no un historial.

La obligación se traslada del conductor, a quien nada puede exigírsele por la vía laboral, al dueño
del camión, que sí mantiene contrato comercial con el mandante. Al aceptar el viaje, el
transportista firma electrónicamente que el conductor designado cuenta con descanso reglamentario.
El dispositivo aporta la evidencia instrumental que contrasta esa declaración, y la identificación
del conductor ocurre sin acción suya.


**Tabla. Cascada de fuentes para el veredicto de jornada**

| **Nivel** | **Fuente** | **Valor probatorio** |
|---|---|---|
| 1 | Tacógrafo digital descargado por la central | Máximo, donde exista |
| 2 | Dispositivo a bordo con identificación del conductor | Evidencia instrumental |
| 3 | Telemetría de fábrica en solo lectura | Complementa |
| 4 | Señal de reposo del activo, sin coordenadas | Contrasta la atestación |
| 5 | Atestación firmada del transportista | Piso contractual universal |
| 0 | Registro portable del conductor, voluntario e incentivado | Beneficio, nunca requisito |


La regla de bloqueo depende de la calidad de la evidencia y no solo de las horas. Con evidencia
instrumental se asigna. Solo con atestación se asigna con marca y responsabilidad registrada. Sin
ninguna fuente se bloquea. La ausencia de datos se trata como evidencia negativa y no como dato
neutro. La excepción la autoriza un rol nominado, con motivo, vigencia y registro auditable.

Queda una brecha que esta oferta declara en lugar de disimularla. El conductor que manejó otro
camión, de otra empresa, sin dispositivo, no deja rastro instrumental alguno. Esa situación se
cierra por responsabilidad contractual y no por tecnología.


### Decisión segunda. La operación no depende de la cobertura móvil


La conectividad se resuelve por capas y no con una única opción para toda la flota.


- **Almacenamiento local en toda unidad intervenida.** El requisito RT-03.10 del Caso
    exige que el dispositivo opere 72 horas continuas sin cobertura móvil registrando posición,
    eventos de conducción y jornada, tiempos en puntos de carga y descarga, y documentos asociados
    al viaje, sin pérdida de ningún registro. Ese requisito está escrito sobre la cobertura móvil,
    de modo que la disponibilidad de enlace satelital no releva de cumplirlo.
- **Celular como portador primario en toda unidad intervenida**, a tasa completa, con
    sincronización diferida y reconciliación determinista al recuperar enlace.
- **Satelital de ráfaga corta en un subconjunto acotado por riesgo**, para posición a
    tasa reducida, botón de emergencia y eventos críticos. La carga útil de esta operación se mide
    en kilobytes por minuto, no en megabits (Iridium Communications, 2024).


La banda ancha satelital para toda la flota se evaluó y se descarta. Cobra ancho de banda que la
operación no usa, consume energía del vehículo y exige montar una antena sobre la cabina, lo que
compromete la restricción que prohíbe afectar la garantía del vehículo. La alternativa descartada
queda registrada en el registro de decisiones de arquitectura conforme a RT-02.04.


### Decisión tercera. Continuidad y recuperación son problemas distintos


El sitio de borde y el sitio secundario de nube no resuelven lo mismo, y confundirlos incumple
RT-07.02, que exige que el secundario esté a distancia suficiente para no verse afectado por el
mismo evento de fuerza mayor. La Sección 4 desarrolla los dos ejes por separado.


### Catálogo de requisitos


El alcance funcional se expresa en 42 requisitos trazables al origen, 28 funcionales y 14 no
funcionales. La tabla siguiente recoge los que definen la solución. El catálogo completo acompaña
esta oferta en el Formulario T-12.


**Tabla. Requisitos que estructuran la solución**

| **ID** | **Exigencia** | **Criterio que satisface** |
|---|---|---|
| RF-001 | Validación bloqueante de jornada, habilitaciones y aptitud antes de asignar | Ningún camión sale sin poder salir |
| RF-003 | Jornada previa del conductor externo disponible al asignar | Decisión primera del Caso |
| RF-008 | Vista única de posición de los 374 camiones | Unifica tres plataformas |
| RF-009 | Registro local de 72 horas y sincronización posterior | Independencia de la cobertura |
| RF-010 | Llegada y salida automáticas en instalaciones de cliente | Origen del 71 por ciento objetado |
| RF-014 | Documento de transporte conforme antes del movimiento, incluso sin cobertura | La emisión diferida no basta |
| RF-022 | Consentimiento granular, revocable y auditable | Criterio 29 |
| RF-026 | Adhesión de transportistas gestionada y medible | Criterio 27 |
| RF-027 | Alerta de jornada según lugar seguro alcanzable | Criterio 28 |
| RNF-001 | Cero interacción del conductor durante la marcha | Restricción 1 |
| RNF-002 | Operación desconectada íntegra e idempotente | RT-03.10 y RT-03.11 |
| RNF-003 | Sin intervención de equipos de terceros sin acuerdo expreso | Restricción 3 |


### Alcance por etapas


El criterio de partición no es de tamaño sino de riesgo. La Etapa 1 controla lo que puede producir
un despacho ilegal, una pérdida probatoria, una duplicación tributaria o un tratamiento indebido de
datos personales, y valida las dependencias técnicas y contractuales antes de comprometer un
despliegue masivo.


**Tabla. Capacidades comprometidas en la Etapa 1**

| **Capacidad** | **Resultado comprometido** |
|---|---|
| Despacho seguro | Validación de jornada, vigencias, aptitud y nivel de evidencia antes de asignar |
| Evidencia y documentos | Registro maestro, trazabilidad e integridad, con pilotos de carga peligrosa y de tacógrafo |
| Posición y operación desconectada | Vista única piloto, geocercas y almacenamiento mínimo de 72 horas |
| Viaje y facturación | Documento conforme antes del movimiento aun sin cobertura, con emisor contable único |
| Costos y liquidación | Costo consolidado dentro de 24 horas con faltantes explícitos, y liquidación por excepción |
| Base de emisiones | Fuentes, línea base y metodología declarada conforme a ISO 14083 y al marco GLEC. No cálculo productivo completo |
| Portales y consentimiento | Portal mínimo, segregación, adhesión y permisos granulares |
| Flota y mantenimiento | Pilotos de kilometraje real y de alerta de lugar seguro |
| Implantación y operación | Pilotos por familia de vehículo, matriz de responsabilidades y despliegue progresivo |


La Etapa 2 escala el despliegue al resto del parque adherido, incorpora la optimización de retornos
para atacar el 26 por ciento de kilómetros en vacío, lleva el cálculo de emisiones a régimen
productivo completo y consolida la adopción de los transportistas.


### Tres poblaciones de camiones, tres tratamientos


La flota no admite un tratamiento único. La restricción 3 establece que los dispositivos instalados
en camiones de terceros pertenecen a sus dueños y no pueden intervenirse, reconfigurarse ni
reemplazarse sin acuerdo expreso.


**Tabla. Tratamiento por población de la flota**

| **Población** | **Unidades** | **Tratamiento** |
|---|---|---|
| Flota propia | 148 | Especificación completa y despliegue directo |
| Terceros con dispositivo | 192 | No se reemplaza nada. Estándar mínimo de homologación y unificación de la vista |
| Terceros sin dispositivo | 34 | Únicos candidatos a equipamiento nuevo, y solo por adhesión |


El entregable para la población intermedia no es un inventario, que el mandante no entregó, sino un
estándar mínimo de homologación contra el cual clasificar después cada equipo. Almacenamiento local
de 72 horas, sincronización diferida, formato de evento, identificación del conductor y sello de
tiempo con garantía de integridad.


### Lo que queda fuera del alcance


El Capítulo 11 del Caso declara con precisión qué no se pide, y esta oferta lo respeta.


- No se reemplaza el sistema contable ni la emisión de documentos tributarios.
- No se interviene la electrónica de fábrica del vehículo.
- No se reemplazan las plataformas de posicionamiento instaladas en camiones de terceros.
    Sí se unifica la vista y se especifica qué se requeriría para homologarlas.
- No se instala infraestructura en los puntos de carga y descarga de los clientes.
- El hardware lo adquiere el mandante. audIT especifica qué comprar, cuánto y con qué
    características.


### Plan de adhesión


El criterio 27 mide si el proponente entendió que la mayor parte de la solución depende de personas
a las que no se les puede dar una orden. La respuesta de audIT combina tres palancas. Una ventaja
concreta para el transportista, que obtiene visibilidad de sus viajes y de su liquidación en curso
y deja de esperar nueve días por un cálculo que se corrige el once por ciento de las veces. Una
garantía de soberanía, porque cada dueño autoriza qué datos comparte y puede revocarlo. Y una
prioridad de asignación para quien adhiere, que convierte la adhesión en un beneficio comercial.

El indicador comprometido es explícito. Número de transportistas adheridos sobre el total de 148, y
plazo en que cada tramo se alcanza. La adhesión se mide, no se supone.


### Consultas formuladas al mandante


**Tabla. Consultas presentadas durante el período del Artículo 43**

| **ID** | **Materia** | **Qué desbloquea** |
|---|---|---|
| C-01 | RT-08.10 exige declarar el costo unitario estimado de cada dispositivo dentro de la especificación técnica, y el Artículo 50.2 prohíbe toda cifra de precio en la Oferta Técnica bajo causal de exclusión | Formato de la especificación de implementos |
| C-02 | RT-03.10 exige 72 horas de operación desconectada del dispositivo a bordo, y la restricción 3 impide intervenir los equipos de camiones de terceros sin acuerdo expreso | Alcance real del requisito sobre la flota |
| C-03 | RT-06.01 ordena remediar o reemplazar la sala de San Bernardo sin indicar a qué tipología del numeral 6.1 debe llevarse | Dimensionamiento y costo del recinto |
| C-04 | Instalaciones distintas de San Bernardo con espacio apto para un sitio secundario que satisfaga RT-07.02 | Emplazamiento del sitio secundario |
| C-05 | Posibilidad de ampliar el espacio más allá de los 26 metros cuadrados | Dimensionamiento del recinto |
| C-06 | Existencia de mediciones previas de cobertura móvil | Costo y plazo de la campaña de Etapa 1 |
| C-07 | Composición del parque telemático de los 226 camiones de terceros por proveedor | Estándar de homologación |
| C-08 | Proporción de camiones de terceros con tacógrafo digital | Alcance del programa de tacógrafo |
| C-09 | Identificación de los 18 camiones de carga peligrosa entre propios y de terceros | Población prioritaria de capa satelital |
| C-10 | Existencia de autorización de la Dirección del Trabajo para sustituir la libreta de registro por un medio electrónico (Dirección del Trabajo, 2009) | Hito regulatorio del registro de jornada |
| C-11 | Códigos de requisito citados en el Capítulo 15 del Caso que corresponden a materias distintas en las Bases Técnicas Transversales | Trazabilidad de toda la oferta |


### Contradicciones detectadas entre los documentos de la licitación


El Artículo 43 registra qué proponentes identifican vacíos, contradicciones y riesgos. audIT
consigna las siguientes.


- **RT-08.10 contra Artículo 50.2.** El primero obliga a declarar el costo unitario
    estimado de cada dispositivo de terreno dentro de la especificación técnica. El segundo prohíbe
    toda cifra de precio en la Oferta Técnica bajo causal de exclusión inmediata. Esta oferta
    entrega la especificación sin valorización y remite los costos al Sobre N.º
    3, a la espera de la respuesta a C-01.
- **RT-03.10 contra la restricción 3.** Si las 72 horas de operación desconectada se
    entienden exigibles sobre las 374 unidades, el requisito resulta incumplible por diseño sobre
    el 51 por ciento de la flota, cuyos equipos no pueden intervenirse. Esta oferta lo interpreta
    exigible sobre las unidades intervenidas y somete el resto al estándar de homologación.
- **Códigos del Capítulo 15 del Caso.** Varios códigos citados allí corresponden en
    las Bases Técnicas Transversales a materias distintas de las que el Caso les atribuye, y en
    tres casos el Caso convierte en exigible un requisito que transversalmente es solo deseable.
    Esta oferta cita cada requisito por su texto y su página además de su código.
- **RT-09.03 contra la proyección del propio Caso.** El requisito transversal obliga a
    soportar tres veces la volumetría inicial en tres años. La proyección del Caso llega a 1,2
    veces. Esta oferta dimensiona sobre el umbral más exigente.
- **RT-07.07 contra la ventana operacional protegida.** El primero exige dos
    conmutaciones reales al año para probar el plan de recuperación. RT-10.05 congela diciembre a
    abril, Semana Santa, Fiestas Patrias y los nueve días del cierre mensual. La ventana disponible
    es estrecha y esta oferta la calendariza de manera explícita.


### Materias pendientes al cierre de esta instancia


Esta oferta declara con la misma claridad lo que aún no está cerrado.


**Tabla. Materias pendientes al cierre del Informe 1**

| **Materia** | **Condición de cierre** |
|---|---|
| Fichas T-19 de los tipos 4 y 5 | Requiere resolver la asignación interna de responsabilidad, hoy consignada de forma distinta en dos documentos de trabajo del proponente |
| Estimación de personas usuarias concurrentes internas y externas | Insumo de RT-09.01, derivado de la volumetría del numeral 14.2 |
| Volumen anual de series de posición y de evidencia de jornada | Requiere la política de agregación definitiva |
| Justificación comparada del nivel de redundancia de almacenamiento | RT-03.14 exige compararlo con las alternativas y no solo declararlo |
| Verificación de dos normas chilenas citadas en las bases | Confirmación ante el organismo normalizador antes de citarlas en la oferta definitiva |
| Verificación de las referencias laborales de jornada y registro | Lectura directa de la norma antes de su cita definitiva |


## Bibliografía

Dirección del Trabajo. (2009). *Resolución Exenta N.º 1213. Sistema obligatorio de control de asistencia, horas de trabajo y descanso para conductores de vehículos de carga terrestre interurbana*.

Ministerio del Trabajo. (2003). *Decreto con Fuerza de Ley N.º 1. Texto refundido del Código del Trabajo. Artículo 25 bis*. Biblioteca del Congreso Nacional de Chile. https://www.bcn.cl/leychile/navegar?idNorma=207436

Escuela de Informática PUCV. (2026a). *Bases Administrativas. Licitación Pública Internacional N.º TFEP-01/2026* (FEP01.26).

Escuela de Informática PUCV. (2026b). *Bases Técnicas Transversales* (FEP02.26).

Escuela de Informática PUCV. (2026c). *Bases Técnicas del Caso 10. Transporte de Carga* (FEP03.10.26).

FMS Standard. (2025). *Technical Specification rFMS vehicle data version 5.0.0*. https://www.fms-standard.com

Iridium Communications. (2024). *Iridium Short Burst Data Service Developers Guide*.

ISO. (2011). *ISO/IEC 27031*. ISO. (2019). *ISO 22301*. ISO. (2022). *ISO/IEC/IEEE 42010*. ISO. (2023). *ISO 14083*.

Microsoft. (2025). *Azure geographies. Chile Central region*.

Ministerio de Hacienda. (2024). *Ley N.º 21.719 sobre protección y tratamiento de datos personales*.

Ministerio de Transportes. (1995). *Decreto Supremo N.º 298*.

Ministerio del Trabajo. (2006). *Ley N.º 20.123 sobre trabajo en régimen de subcontratación*.

NFPA. (2022). *NFPA 2001*. NIST. (2014). *NIST SP 800-88 Rev. 1*.

Smart Freight Centre. (2023). *GLEC Framework, version 3.0*.

Webfleet Solutions. (2025). *WEBFLEET SAT. Ficha técnica del producto*.
