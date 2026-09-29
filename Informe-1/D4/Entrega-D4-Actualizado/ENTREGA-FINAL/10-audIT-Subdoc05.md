# Modelo y Gestión de Datos

**Subdocumento N.º 5**

| | |
|---|---|
| Empresa | audIT, Empresa N.º 10 |
| Licitación | Licitación Pública Internacional N.º TFEP-01/2026. Caso 10 Transporte de Carga |
| Proyecto | Plataforma Digital de Misión Crítica para Transporte de Carga |
| Cliente | Transportes Curimón S.A. |
| Instancia | Informe Preparatorio 1. Oferta Técnica Sobre N.º 2 |
| Contenido | Modelo de dominio, persistencia, auditoría, retención, respaldo, migración y protección de datos personales. |
| Versión | 1.0 |
| Fecha | 7 de septiembre de 2026 |
| Lugar | Viña del Mar, Chile |

---

## Modelo y gestión de datos


### Modelo de dominio


El modelo se construye sobre las entidades que el negocio nombra y no sobre las tablas que un
sistema anterior dejó. Las principales son Viaje, Tramo, Orden de Transporte, Conductor,
Tractocamión, Semirremolque, Transportista, Tarifa, Evento de Jornada, Geocerca, Liquidación y
Siniestro. Cada una pertenece a uno de los seis contextos delimitados de la Sección 4 y ninguna se
comparte entre contextos por acceso directo a su almacenamiento.


### Persistencia políglota


RT-05.02 exige justificar el motor escogido para cada dominio. La justificación se apoya en qué es
lo que ese dato no puede permitirse perder.


**Tabla. Persistencia por dominio de datos**

| **Dominio** | **Motor** | **Regla que gobierna la elección** |
|---|---|---|
| Despacho, viajes, documentos y liquidaciones | Relacional con consistencia estricta y alta disponibilidad multizona | Es preferible abortar o encolar el despacho antes que autorizar un viaje con conductor sin descanso o equipo sin revisión |
| Series de posición y telemetría | Series de tiempo con particionamiento horizontal | La telemetría nunca bloquea al camión. Se acumula a bordo y sincroniza por consistencia eventual al recuperar red |
| Buffer a bordo | Base embebida cifrada en el dispositivo | Registro local con integridad garantizada durante 72 horas de desconexión |
| Documentos y evidencia | Almacenamiento de objetos con inmutabilidad | La evidencia debe resistir una alegación de manipulación, incluso frente a credenciales administrativas |
| Sesiones, vigencias y geocercas de consulta | Caché en memoria | Latencia baja para la validación en el momento de asignar |


![Persistencia políglota. Consistencia estricta, disponibilidad extrema y capa transitoria](Persistencia.pdf)

*Figura. Persistencia políglota. Consistencia estricta, disponibilidad extrema y capa transitoria*


### Evidencia inalterable


El criterio 4 del Caso exige evidencia de jornada que resista una alegación de manipulación, tanto
por parte de la compañía como del conductor. Un registro que puede editarse no sirve ante la
autoridad, ante la aseguradora ni ante el cliente.

La bitácora de auditoría captura para cada escritura el identificador de transacción, el usuario o
dispositivo, la marca de tiempo, el origen y los valores anteriores y posteriores. Los registros de
jornada y de asignación se conservan en almacenamiento protegido contra borrado y contra
modificación durante todo su período de retención.


### Retención por dominio


Los plazos provienen de RT-05.10 del Caso y no admiten interpretación.


**Tabla. Política de retención por dominio de datos**

| **Dominio** | **Retención exigida** |
|---|---|
| Registro de jornada de conducción y su evidencia | Mínimo 5 años |
| Documento electrónico de transporte y antecedentes del viaje | 6 años |
| Antecedentes de siniestros | 10 años |
| Habilitaciones de conductores y equipos | Vigencia más 5 años |
| Registros de carga peligrosa | 5 años |
| Evidencia de tiempos de llegada y salida en instalaciones de cliente | 3 años |
| Liquidaciones a transportistas | 6 años |
| Series de posición y telemetría | 2 años en línea, con política de agregación declarada |


Una precisión que esta oferta hace explícita. La retención de la evidencia de jornada no distingue
entre camión propio y camión de tercero, porque la acreditación se exige por viaje. Lo que sí se
limita es el alcance. Se conserva la jornada del viaje que el mandante despachó, no la actividad
del conductor para otras empresas. Esa es la minimización que audIT declara y defiende.


### Respaldo y recuperación


RT-07.09 fija el esquema tres, dos, uno, uno, cero. Tres copias, en dos medios distintos, una fuera
de sitio, una inmutable o fuera de línea y cero errores de verificación de restauración.


**Tabla. Implementación del esquema de respaldo**

| **Elemento** | **Implementación** |
|---|---|
| Tres copias | Producción en la región primaria, réplica en la segunda región y copia en San Bernardo |
| Dos medios distintos | Almacenamiento de objetos en nube y medio físico transportable en el sitio |
| Una fuera de sitio | La segunda región y la custodia externa de medios |
| Una inmutable o fuera de línea | Almacenamiento con retención legal que resiste credenciales administrativas comprometidas |
| Cero errores de verificación | Prueba de restauración mensual documentada sobre muestra representativa |


La clave de cifrado de los respaldos se gestiona de forma independiente de la infraestructura
respaldada, de modo que no vive en la misma suscripción que protege. Los medios que salgan de
servicio se borran de forma segura y verificable con certificado entregado al mandante
(NIST, 2014).

Existe además una cuarta copia que ningún plan de respaldo planificó y que está disponible igual.
Los 374 dispositivos conservan 72 horas del registro operacional. No sustituye al respaldo, y es
una fuente real de reconciliación ante una pérdida de datos reciente.


### Migración y saneamiento


Las 6.000 fechas de vencimiento vivas se reparten en cuatro planillas mantenidas por personas
distintas. Su migración no es una carga de datos, es un saneamiento. RT-05.15 del Caso exige
verificación documental de cada una durante la migración, por tratarse de datos hoy dispersos.

El plan compromete perfilamiento, reglas de transformación, informe de excepciones por registro y
plan de reversión. Se ejecutan al menos dos ensayos completos de migración sobre el ambiente de
preproducción antes de la migración definitiva, con conciliación cuantitativa verificable mediante
recuentos y sumas de control. Se migran los maestros de flota, semirremolques, conductores,
transportistas y clientes en su totalidad, cinco años de viajes, seis años de liquidaciones y la
totalidad de los antecedentes de siniestros.


### Protección de datos personales


RT-11.10 del Caso exige cifrado a nivel de campo para los datos personales de los 258 conductores
que no son trabajadores de la compañía, para toda información de localización asociada a una
persona identificable, para los antecedentes de jornada y para las tarifas pactadas con cada
transportista. La Ley N.º 21.719 (Congreso Nacional de Chile, 2024) gobierna ese tratamiento.

De ahí se desprende una precisión de lenguaje que esta oferta sostiene. La solución no sabe dónde
está una persona. Sabe dónde está un camión, con autorización revocable de su dueño. RT-16.30
obliga a que el portal del transportista entregue el control de qué datos de sus camiones y
conductores autoriza compartir y con quién, con posibilidad de revocación, y RT-16.09 obliga a
registrar todo acceso a esa información indicando qué se mostró y bajo qué autorización.

Ante la revocación del consentimiento de un transportista, el seguimiento futuro y la visibilidad
comercial cesan de inmediato. Los datos históricos quedan bloqueados para fines exclusivamente
probatorios hasta cumplir los plazos legales de retención, momento en el cual se ejecuta su
destrucción segura.


### Analítica y costo real


La capa analítica se separa físicamente de la transaccional para que ninguna consulta de gestión
degrade la operación de la torre. El costo consolidado de un viaje se emite dentro de las 24 horas
posteriores a su cierre, indicando de manera explícita qué componentes están disponibles y cuáles
no, y se actualiza cuando llegan los que faltan.


![Construcción del costo real por kilómetro con fuentes de distinto desfase](Costo.pdf)

*Figura. Construcción del costo real por kilómetro con fuentes de distinto desfase*


Ese diseño responde a la razón por la que el problema existe. El combustible llega con 40 días de
desfase, los peajes se liquidan mensualmente y las tarifas de terceros son contractuales. Esperar a
que todo esté disponible convierte el costo por viaje en un cierre contable tardío, y esa demora es
la que permitió que un contrato operara cuatro años a menos 14 por ciento sin que nadie lo
advirtiera.

## Bibliografía

Dirección del Trabajo. (2009). *Resolución Exenta N.º 1213. Sistema obligatorio de control de asistencia, horas de trabajo y descanso para conductores de vehículos de carga terrestre interurbana*.

Ministerio del Trabajo. (2003). *Decreto con Fuerza de Ley N.º 1. Texto refundido del Código del Trabajo. Artículo 25 bis*. Biblioteca del Congreso Nacional de Chile. https://www.bcn.cl/leychile/navegar?idNorma=207436

Escuela de Informática PUCV. (2026a). *Bases Administrativas. Licitación Pública Internacional N.º TFEP-01/2026* (FEP01.26).

Escuela de Informática PUCV. (2026b). *Bases Técnicas Transversales* (FEP02.26).

Escuela de Informática PUCV. (2026c). *Bases Técnicas del Caso 10. Transporte de Carga* (FEP03.10.26).

FMS Standard. (2025). *Technical Specification rFMS vehicle data version 5.0.0*. https://www.fms-standard.com

Iridium Communications. (2024). *Iridium Short Burst Data Service Developers Guide*.

ISO. (2011). *ISO/IEC 27031*. ISO. (2013). *ISO 16290. Definition of the Technology Readiness Levels (TRLs) and their criteria of assessment*. ISO. (2019). *ISO 22301*. ISO. (2022). *ISO/IEC/IEEE 42010*. ISO. (2023). *ISO 14083*.

Microsoft. (2025). *Azure geographies. Chile Central region*.

Congreso Nacional de Chile. (2002). *Ley N.º 19.799 sobre documentos electrónicos, firma electrónica y servicios de certificación de dicha firma*. https://www.bcn.cl/leychile/navegar?idNorma=196640

Congreso Nacional de Chile. (2024). *Ley N.º 21.719 que regula la protección y el tratamiento de los datos personales y crea la Agencia de Protección de Datos Personales*. Diario Oficial de 13 de diciembre de 2024. https://www.bcn.cl/leychile/navegar?i=1209272

Ministerio de Transportes. (1995). *Decreto Supremo N.º 298*.

Ministerio del Trabajo. (2006). *Ley N.º 20.123 sobre trabajo en régimen de subcontratación*.

NFPA. (2022). *NFPA 2001*. NIST. (2014). *NIST SP 800-88 Rev. 1*.

Smart Freight Centre. (2023). *GLEC Framework, version 3.0*.

Webfleet Solutions. (2025). *WEBFLEET SAT. Ficha técnica del producto*.

World Wide Web Consortium. (2025). *Verifiable credentials data model v2.0*. W3C Recommendation de 15 de mayo de 2025. https://www.w3.org/TR/vc-data-model-2.0/
