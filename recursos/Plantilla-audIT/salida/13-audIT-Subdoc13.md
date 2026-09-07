# Innovaciones

**Subdocumento N.º 13**

| | |
|---|---|
| Empresa | audIT, Empresa N.º 10 |
| Licitación | Licitación Pública Internacional N.º TFEP-01/2026. Caso 10 Transporte de Carga |
| Proyecto | Plataforma Digital de Misión Crítica para Transporte de Carga |
| Cliente | Transportes Curimón S.A. |
| Instancia | Informe Preparatorio 1. Oferta Técnica Sobre N.º 2 |
| Contenido | Cartera de cinco innovaciones, una por cada tipo obligatorio del Artículo 28. |
| Versión | 1.0 |
| Fecha | 7 de septiembre de 2026 |
| Lugar | Viña del Mar, Chile |

---

## Innovaciones


El Artículo 28 exige una cartera de cinco innovaciones, una por cada tipo obligatorio y sin repetir
tipo. En esta instancia cada innovación se nombra y se explica en su alcance, con su idea, la
tecnología que la sustenta y el resultado esperado. El refinamiento trazable con la arquitectura y
la estructura de desglose corresponde al Informe 2, la valorización al Informe 3 y el Formulario
T-19 con los siete elementos del Artículo 29 a la propuesta final.

El Artículo 30.2 establece que se valora la pertinencia al caso por sobre la novedad tecnológica en
abstracto, y que una innovación sofisticada que no resuelve un problema real del caso obtiene menor
puntaje que una sencilla, bien justificada y con impacto verificable. Las cinco propuestas que
siguen se eligieron con ese criterio.


**Tabla. Cartera de innovaciones y responsables**

| **Tipo** | **Categoría del Artículo 28** | **Innovación** | **Responsable** |
|---|---|---|---|
| 1 | Producto o servicio | Portal del transportista con liquidación en curso | Ignacio C. |
| 2 | Proceso | Despliegue sin detener la flota | Ignacio V. y Alonso |
| 3 | Tecnológica o de arquitectura | Operación desconectada y vista única de flota | Marcel y Martín |
| 4 | Modelo de negocio o contratación | Esquema de adhesión y propiedad del dispositivo | Matías V. |
| 5 | Experiencia de usuario, sostenibilidad o impacto social | Alerta de jornada con lugar seguro alcanzable | Carlos y Naomi |


### Tipo 1. Portal del transportista con liquidación en curso


**Idea.** Hoy el transportista subcontratado espera nueve días a que ocho personas calculen su
liquidación, y el once por ciento de esos cálculos se corrige después. Durante ese tiempo no tiene
forma de saber cuánto va a cobrar ni por qué. La innovación consiste en mostrarle su liquidación
mientras se construye, viaje a viaje, en lugar de entregársela cerrada al final del mes.

**Tecnología que la sustenta.** Portal segregado por identidad con vista propia de cada
transportista, alimentado por el mismo motor de costeo que produce la liquidación oficial. Cada
viaje aparece con su tarifa aplicada, sus tiempos de espera certificados por geocerca y sus
descuentos, en el momento en que el dato entra al sistema y no cuando el mes cierra.

**Resultado esperado.** Reducción del tiempo de cierre mensual y del porcentaje de
liquidaciones corregidas. Y un efecto que importa más que ambos, porque el portal es la primera
razón concreta que un dueño de camión tiene para adherir. La transparencia del pago es el
argumento comercial del plan de adhesión que mide el criterio 27.

**Investigación adicional requerida.** Ninguna. La capacidad depende del motor de costeo que
ya forma parte del alcance de la Etapa 1.


### Tipo 2. Despliegue sin detener la flota


**Idea.** Un camión detenido no produce, la intervención a bordo solo puede hacerse cuando el
camión pasa por un terminal, y ese paso ocurre cada seis días en promedio mientras el 22 por ciento
de la flota subcontratada pasa menos de una vez al mes. La innovación convierte ese paso fortuito
en una ventana de intervención planificada y de duración acotada.

**Tecnología que la sustenta.** Anticipación de la llegada al terminal a partir de la posición
de la propia flota, equipo preconfigurado en el stock de reemplazo antes de que el camión llegue, y
gestión remota del parque para que todo el ciclo de vida posterior ocurra por aire. La intervención
física se reduce a sustituir y salir.

**Resultado esperado.** Unidades intervenidas por mes y tiempo de inmovilización por unidad.
El techo del ritmo lo fija el 22 por ciento que pasa menos de una vez al mes, y esa limitación se
declara en lugar de ocultarse.

**Investigación adicional requerida.** Ninguna en el concepto. El tiempo real de intervención
por familia de vehículo se mide en el piloto de la Etapa 1.


### Tipo 3. Operación desconectada y vista única de flota


**Idea.** Cuarenta y un millones de kilómetros al año con tramos de más de 80 kilómetros sin
cobertura, 34 camiones sin dispositivo y 340 repartidos en tres plataformas incompatibles, una de
las cuales no permite exportar. La innovación hace que el registro exista en el vehículo antes de
que exista cualquier enlace, y que las tres plataformas se vean como una sola.

**Tecnología que la sustenta.** Almacenamiento local estructurado y cifrado a bordo con
volcado diferido y reconciliación determinista, capa de ingestión que normaliza los eventos de las
tres plataformas bajo un formato común, y emisión del documento de transporte con folio autorizado
en memoria protegida del dispositivo para los puntos de carga sin señal.

**Resultado esperado.** Los indicadores parten de una línea base medida.


**Tabla. Indicadores de la innovación tipo 3**

| **Indicador** | **Línea base** | **Meta** |
|---|---|---|
| Pérdida de registros en desconexión de 72 horas | Pérdida total en sombras de más de dos horas | Cero pérdida |
| Resistencia al cierre de Los Libertadores | Ceguera tras 24 a 48 horas | Preservación hasta 288 horas |
| Visibilidad unificada de la flota | Tres plataformas separadas y 34 unidades ciegas | Totalidad de unidades en vista única |
| Latencia de reconciliación tras la sombra | No existe sincronización | Supera el umbral de 20 minutos del Capítulo 15 |
| Emisión del documento sin señal | Rezagada o inexistente | Emitido conforme antes de que el vehículo se mueva |


**Investigación adicional requerida.** La factibilidad de exportación de la plataforma que hoy
no la permite debe verificarse con ese proveedor. Es una dependencia de terceros con actividad
propia en la Etapa 1.


### Tipo 4. Esquema de adhesión y propiedad del dispositivo


**Idea.** Financiamiento del dispositivo, incentivos de adhesión, consentimiento granular y
beneficios verificables. La primera pregunta que hace un dueño de camión es de quién es el equipo, quién lo
paga y qué pasa con él si deja de trabajar con la compañía. La segunda es si el aparato va a
delatar cuándo trabaja para la competencia. Mientras esas dos preguntas no tengan respuesta, ningún
diseño técnico se despliega. La innovación separa la propiedad del equipo de la propiedad del dato,
y le entrega la segunda al dueño del camión.

**Tecnología que la sustenta.** Figura de comodato sobre el equipamiento, con condiciones de
retiro y de traspaso definidas desde el inicio. Modo de privacidad implementado en el firmware del
dispositivo y no en configuración de servidor, de modo que la posición deja de emitirse hacia el
mandante cuando el camión trabaja para otro cliente, y esa garantía sea verificable por el dueño en
lugar de prometida. Consentimiento granular y revocable administrado desde el portal, con registro
auditable de cada acceso a la información de localización.

**Resultado esperado.** Número de transportistas adheridos sobre el total de 148 y plazo en
que cada tramo se alcanza. Es la innovación que responde de manera directa al criterio 29, que
exige que quien entrega el dato conserve el control sobre él.

**Investigación adicional requerida.** El modelo de financiamiento del equipamiento y el
tratamiento contable del comodato requieren definición conjunta con el mandante. La decisión de
quién paga el dispositivo permanece abierta en el Capítulo 16 del Caso.


### Tipo 5. Alerta de jornada con lugar seguro alcanzable


**Idea.** Una alerta que avisa al conductor que su jornada se agota, entregada en un tramo
donde no existe dónde detenerse, no evita nada. Convierte una infracción en una infracción con
aviso. La innovación calcula la alerta contra la distancia al lugar seguro de detención más
cercano, y no contra un contador de horas.

**Tecnología que la sustenta.** Cálculo del margen restante a bordo del vehículo, sin depender
del enlace, contrastado con un catálogo georreferenciado de lugares seguros de detención que hoy no
existe y que se levanta durante la misma campaña de medición de cobertura de la Etapa 1. Interfaz
operable con una sola mano y con guantes, sin ninguna interacción exigible durante la marcha,
validada con conductores reales antes de su despliegue.

**Resultado esperado.** Porcentaje de alertas entregadas con anticipación suficiente para
alcanzar un lugar seguro, medido sobre el total de alertas emitidas. El impacto social es directo
sobre las 454 personas que conducen, y responde al criterio 28, que el propio Caso identifica entre
los tres que deciden la evaluación.

**Investigación adicional requerida.** El catálogo de lugares seguros de detención no existe
en ninguna fuente disponible y debe construirse en terreno. La anticipación mínima en minutos se
declara y se fundamenta una vez que ese catálogo permita calcular distancias reales.


### Estado de elaboración y responsables


El reparto de responsabilidades quedó ratificado el 6 de septiembre de 2026. Las fichas tipo 1 y
tipo 4 corresponden a la dupla del subdocumento 3, la tipo 2 a la dupla del subdocumento 4, la tipo
3 a la dupla de los subdocumentos 4.1 y 5, y la tipo 5 a la dupla de los subdocumentos 1 y 2.


### Trazabilidad con el resto de la propuesta


Ninguna de las cinco es una funcionalidad que las bases ya exijan. Las tipo 2, 3 y 5 se apoyan en
componentes de la arquitectura descritos en el subdocumento 4. La tipo 1 se apoya en el motor de
costeo del subdocumento 5. La tipo 4 es contractual antes que técnica, y su viabilidad determina
cuántas unidades del parque llegan a intervenirse.

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
