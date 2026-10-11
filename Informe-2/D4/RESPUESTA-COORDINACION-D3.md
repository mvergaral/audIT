# Respuesta de la dupla 4 a los puntos de coordinación de la dupla 3

Fecha: 11 de octubre de 2026. Responde la sección «Para D4» de
`audIT/Informe-2/D3/COORDINACION_D1_D2_D4.md`, con lo que hoy dicen el Subdocumento 4 (4.2 y 4.3), el
Formulario T-11, el Subdocumento 8 y el Formulario T-16 del formato de la dupla 4. Cada respuesta dice qué
está resuelto, qué no y qué hace falta de cada dupla.

Un dato de contexto antes de empezar: la dupla 4 ya integró al Subdocumento 4 su versión del 4.1 del 10 de
octubre (commit eef2475). El detalle de lo que se ajustó al integrar está en `AVISO-D3.md`, en esta misma
carpeta.

## 1. Stack y servicios

**Estado: acordado. Hay una corrección pendiente en TimescaleDB.**

- **Versiones.** El 4.1.1 del Subdocumento 4 ya usa .NET 10 LTS, Go 1.27 y PostgreSQL 16. Sus fechas se
  verificaron con cada fabricante el 10-10-2026:
  - .NET 10 tiene soporte hasta el 14-11-2028 (dotnet.microsoft.com, «.NET and .NET Core Support Policy»).
  - Go mantiene sus dos versiones mayores más recientes, que hoy son la 1.26 y la 1.27 (go.dev, «Release History»).
  - PostgreSQL 16 tiene soporte hasta el 09-11-2028 (postgresql.org, «Versioning Policy»).

  .NET 10 y PostgreSQL 16 se actualizan antes del mes 22, dentro de la mantención evolutiva, como pide el
  FEP02, numeral 1.6, p.5.
- **TimescaleDB, corrección.** En Azure Database for PostgreSQL Flexible, la extensión disponible para
  PostgreSQL 16 es la **2.24.0**. La 2.15.3 es la de PostgreSQL 13 y 14 (Microsoft Learn, «List of
  Extensions and Modules by Name», actualizada el 13-07-2026). La tabla 4.1.1 dice hoy «TimescaleDB 2.15»,
  con fin de soporte «mayo de 2029», y ese plazo no se pudo verificar. Propuesta: «TimescaleDB 2.24 (edición
  Apache-2 de Azure)» y quitar la fecha de fin de soporte, porque la extensión la mantiene Microsoft dentro
  del servicio. Se necesita el visto bueno de la dupla 3.
- **Disponibilidad en la región.** Todos los servicios del catálogo de la 4.2.4 están en Chile Central y en
  Brazil South, según la interfaz pública de precios de Azure (Subdocumento 4, sección 4.2.4). Azure Managed
  Redis se verificó aparte el 10-10-2026: tiene sus cuatro familias (Balanced, Compute Optimized, Memory
  Optimized y Flash Optimized) en las dos regiones. Microsoft lo declara redundante entre zonas por defecto.
- **Zonas.** Chile Central y Brazil South tienen tres zonas de disponibilidad. En producción van en tres
  zonas AKS, API Management, PostgreSQL con su copia en espera en otra zona, el almacenamiento con
  redundancia de zona y Azure Managed Redis.
- **Capacidad y cuotas.**
  - IoT Hub S1 con dos unidades admite 800.000 mensajes de 4 KB al día. La operación normal con 430
    camiones usa unos 330.000, más 57.600 de una reconexión masiva.
  - Event Hubs Premium parte con una unidad de procesamiento.
  - El tamaño de AKS, PostgreSQL y Azure Managed Redis se fija con la prueba de carga de 1,5 veces el peak
    en preproducción (FEP02, RT-09.06, p.21) antes del hito H5.
  - Las cuotas de vCPU de la suscripción se piden al proveedor cuando se crean las suscripciones del
    mandante. No hay hoy un dato de cuota que declarar.
- **T-11.** Ya trae Azure Managed Redis, Event Hubs Premium con Kafka, Delta Lake en ADLS Gen2 y el tamaño
  «fijado con la prueba de carga». No le quedan marcadores.

## 2. Capacidad

**Estado: resuelto. La dupla 4 ya usa 380 y 570.**

El documento de coordinación dice que la dupla 4 usa 350 y 525. Ya no es así: desde el 10-10-2026 el
Subdocumento 4 usa la pareja de la dupla 3, **380 sesiones y 570 en estrés**. Está en la tabla de
concurrencia del 4.1.20 y en el supuesto S-13 de la 4.2.9. Los tres escenarios van separados, cada uno con
sus recursos y su prueba:

| Escenario | Carga | Recursos que dimensiona | Fuente |
|---|---|---|---|
| Concurrencia de usuarios | 380 sesiones en hora punta, 570 en estrés (1,5 veces) | AKS, API Management, PostgreSQL transaccional, Azure Managed Redis | FEP03, RT-09.02, p.32, y FEP02, RT-09.06, p.21 |
| Crecimiento de volumetría | 3 veces la volumetría inicial sin rediseño | Unidades de IoT Hub, Event Hubs, servidor de series | FEP02, RT-09.03, p.21 |
| Reconexión masiva | 300 camiones tras 72 h: 57.600 mensajes en 9,6 min, 300 conexiones en 3 s y fotos en 1,5 min | IoT Hub S1 con dos unidades, Event Hubs, consumidores en AKS | FEP03, RT-03.13, p.31 |

Para la dupla 1: la prueba de 300 reconexiones mide la recuperación de 72 h en hasta 20 minutos por camión,
y no es la misma prueba que la de estrés de usuarios.

## 3. Retorno satelital

**Estado: abierto. La factibilidad de 90 s no está demostrada.**

- **Lo que hay hoy.** El Iridium Edge, conectado por RS232 al iWave G26I, envía mensajes de hasta 340 bytes
  de subida (Subdocumento 4, 4.2.2, y la ficha del fabricante). El límite de 270 bytes de bajada es el de los
  transceptores Iridium 9602 y 9603 (fichas RockBLOCK 9602 y 9603 de Ground Control). Para el Iridium Edge
  hay que confirmarlo en su propia ficha, porque no se encontró publicado.
- **Lo que pide la dupla 3.** Que la cabina tenga la representación completa y conforme del documento, no
  solo el folio o el hash. El Subdocumento 4 (4.1.13) dice hoy que «el folio vuelve por el mismo canal antes
  de que se autorice la salida». No afirma que se cumplan los 90 s por satélite.
- **Propuesta de la dupla 4.** La representación se arma a bordo con los datos que el propio equipo envió,
  más el folio y el timbre que devuelve el sistema contable. Así el retorno solo trae lo que el equipo no
  tiene, y cabe en pocos mensajes de bajada. El equipo nunca firma ni emite: solo compone y muestra lo que
  el sistema contable ya emitió.
- **Lo que falta.**
  - **Dupla 2:** el contenido y el tamaño máximo de la representación que exige el documento conforme, en
    particular el tamaño del timbre.
  - **Dupla 4:** con ese tamaño, calcula cuántos mensajes de bajada hacen falta y mide la latencia completa
    de ida y vuelta en la Etapa 1.

  Mientras no haya medición, el Subdocumento 4 no afirma cumplir los 90 s de RT-09.01 por el camino
  satelital. El camino principal sigue siendo la emisión anticipada desde la orden.
- **Riesgo.** Si la medición no cumple, se agrega al registro del Subdocumento 8 con su contingencia, que
  es emitir por anticipado o esperar cobertura.

## 4. Almacenamiento a bordo

**Estado: resuelto en el cálculo. Hay una frase del Subdocumento 4 que corregir.**

- **Memoria.** El iWave G26I lleva 8 GB de eMMC, y la tabla 4-emmc del Subdocumento 4 suma 2.374 MB
  requeridos:

  | Partición | Tamaño |
  |---|---|
  | Arranque | 16 MB |
  | Sistemas A y B | 2.048 MB |
  | Búfer de 288 h | 38,4 MB |
  | Registros | 256 MB |
  | Geocercas y maestros | 16 MB |

  La memoria útil después del sistema de archivos no está medida. Se verifica con la primera imagen en la
  Etapa 1 (supuesto S-07).
- **Requisito y margen.** El requisito es de 72 horas sin cobertura (FEP03, RT-03.10, p.31). El búfer de
  288 horas es un margen de cuatro veces el requisito, y cada 72 horas con fotos ocupan 3,2 MB.
- **Recuperación.** Tras la reconexión, el equipo reenvía su búfer. Una reconexión simultánea de 300
  camiones termina en 9,6 minutos, dentro de los 20 por camión de RT-03.13. Tras una conmutación de región,
  el equipo reenvía sus últimas 72 horas, y la clave de idempotencia de siete días descarta los duplicados.
- **Corrección aceptada.** La dupla 3 tiene razón: RT-10.05 (FEP03, p.32) trata los cierres del paso de
  hasta 12 días como una restricción del plan («deben absorberse sin desplazar hitos») y no como 12 días sin
  enlace. El Subdocumento 4 dice hoy «el búfer de 288 horas, que cubre los 12 días de cierre del paso Los
  Libertadores». Propuesta para la 4.2.2: «El búfer de 288 horas es cuatro veces el requisito de 72 horas de
  RT-03.10 y da margen a un camión que quede detenido sin señal durante un cierre del paso. RT-10.05 trata
  ese cierre como una restricción del plan, no del enlace».
- **Redis.** El plazo no se traslada a la caché. Las 288 horas viven a bordo, en SQLite. La caché en la nube
  solo guarda la clave de idempotencia de siete días, que además se respalda con una restricción de unicidad
  en PostgreSQL (Subdocumento 4, 4.1.10).

## 5. Recuperación y sitio alterno

**Estado: diseño completo. La transferencia de datos personales queda condicionada a la vía legal.**

- **Datos y eventos.** El RPO de 15 minutos y el RTO de 4 horas (FEP02, RT-07.04, p.17) cubren:
  - las dos bases PostgreSQL, con réplicas asíncronas y la de series en un servidor propio.
  - los objetos documentales, con replicación a una cuenta de Brazil South en minutos.
  - los eventos, con Event Hubs, que frena la entrada si el retraso de su réplica pasa de 10 minutos.
  - el reenvío de 72 horas desde el equipo a bordo, que cubre lo que la réplica no alcanzó.
- **RTO.** Lo determinan la promoción de las réplicas y el despliegue desde el mismo código de AKS, la
  puerta de enlace, IoT Hub y el monitoreo. La conmutación se prueba de verdad dos veces al año (RT-07.07).
- **Sin redundancia geográfica.** Ninguna copia usa redundancia geográfica, porque la región pareja de Brazil
  South es South Central US, fuera de Sudamérica.
- **Transferencia de datos personales.** El Subdocumento 4 (4.3.2) ya recoge lo que fija el S5 de la dupla
  3:
  - antes de activar la réplica se identifican el responsable y el destinatario.
  - se documenta la vía de los artículos 27 y 28 de la Ley N.º 21.719.
  - si esa vía no se documenta, los datos personales no se replican fuera de Chile.
- **Si Brazil South no fuera admisible.** No hay otro sitio en Chile que cumpla RT-07.02. Azure tiene una
  sola región en Chile, y San Bernardo comparte con ella el riesgo sísmico y la red eléctrica, así que no
  sirve como sitio de recuperación. En ese caso los datos que no son personales se siguen replicando, y los
  personales quedan protegidos en las tres zonas de Chile Central y en los respaldos. Frente a un desastre
  que tome toda la región, su recuperación no cumpliría el RPO y el RTO. Es el riesgo R-24 del Subdocumento 8
  (exposición 12 que baja a 8). Su contingencia lleva el caso al Comité Ejecutivo, y la declaración de
  cumplimiento de la recuperación quedaría condicionada a esa decisión.
- **Lo que falta de la dupla 3.** La vía legal de los artículos 27 y 28, con el responsable y el
  destinatario.

## 6. Innovación tipo 2

**Estado: la dupla 4 puede confirmar el equipo y la reversión. Los tiempos y las familias de vehículo se
miden en el piloto.**

- **Equipo y agente.** Hay una sola familia de hardware para los 182 equipos audIT: iWave G26I con Linux
  embebido y el elemento seguro TA100, Iridium Edge, CANCrocodile y lector MIFARE DESFire (Formulario T-11).
  El agente es audIT EdgeHub. La configuración deseada y reportada se lleva en IoT Hub, como propone la ficha.
- **Actualización fallida.** La memoria tiene dos particiones de sistema, A y B, de 1 GB cada una. La
  actualización se escribe en la partición que no está en uso y, si falla, el equipo vuelve a la anterior
  sin perder el búfer, que va en su propia partición (tabla 4-emmc). La imagen pesa cerca de 1 GB (supuesto
  S-07) y se descarga por el Wi-Fi del patio, con el FortiAP 234G. El enlace de 10 Mbit/s del terminal
  alcanza para 12,5 visitas diarias.
- **Disponibilidad física y reposición.** Un camión pasa por un terminal cada seis días en promedio (FEP03,
  capítulo 10, p.23). Hay 19 equipos de reposición, el 10 % del parque, en los terminales, y un equipo
  dañado se cambia en el mismo paso (riesgo R-02).
- **Lo que la dupla 4 no puede confirmar con datos de hoy.**
  - **Familias de vehículo.** El Caso no da marca ni modelo de los tractocamiones, y el punto de montaje
    del CANCrocodile puede cambiar con el arnés de cada marca. Se caracterizan en el piloto de 10 camiones del mes 6.
  - **Tiempo de sustitución.** La meta de 30 minutos de la ficha no tiene hoy medición. Se cronometra en el
    mismo piloto.
- **Subdocumento 8 y Formulario T-16.** El registro ya cubre la falla del equipo (R-02), el despliegue lento
  (R-19), el período mixto (R-20) y la adhesión de los terceros (R-11). Ninguno promete intervenir a un
  tercero sin adhesión. Cuando las duplas 2 y 3 aprueben la innovación en el Subdocumento 13, la dupla 4
  agrega dos riesgos con su contingencia manual:
  - el planificador propone una intervención que no ocurre, porque el camión no llega o no hay kit, y la
    contingencia es la programación manual del Líder de Implantación en el terminal.
  - el agente o el kit resultan incompatibles con una familia de vehículo, y la contingencia es volver a la
    versión anterior con el procedimiento manual homologado.

## Resumen de acciones

| Acción | Quién | Estado |
|---|---|---|
| Corregir TimescaleDB a 2.24 en la tabla 4.1.1 | Dupla 4, con visto bueno de la dupla 3 | Propuesta |
| Contenido y tamaño máximo de la representación del documento | Dupla 2 | Pendiente |
| Medir el retorno satelital y confirmar los 270 bytes de bajada del Iridium Edge | Dupla 4, en la Etapa 1 | Pendiente |
| Reformular la frase de las 288 horas en la 4.2.2 | Dupla 4 | Propuesta |
| Vía legal de la transferencia a Brazil South | Dupla 3 | Pendiente |
| Familias de vehículo y tiempo de sustitución | Piloto del mes 6 | Pendiente |
| Riesgos de la innovación 2 en el S8 y el T-16 | Dupla 4, cuando se apruebe la innovación | En espera |
| Pareja de capacidad 380 y 570 | Duplas 1, 3 y 4 | Resuelto |
