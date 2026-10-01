# Registro de decisiones de la dupla 4

Informe 2, Licitación TFEP-01/2026, Caso 10. Alcance: Subdocumento 4 en su parte física (4.2, 4.2.1,
4.3, 4.3.1 y 4.3.2), Formulario T-11 y la innovación 3 del Subdocumento 13 con su ficha del T-19.

Regla de trabajo: ninguna decisión se aplica sin aprobación explícita de la dupla. Cada entrada dice
quién la aprobó, cuándo y con qué texto. Lo que depende de otra dupla queda en espera y no se toca.

## Decisiones aprobadas

| N.º | Fecha | Decisión | Fundamento | Aprobación |
|---|---|---|---|---|
| D4-01 | 2026-09-28 | El T-11 declara dispositivos audIT para los 148 camiones propios y los 34 de terceros sin equipo, más repuestos. Los 192 camiones de terceros que ya tienen equipo se integran por datos y no se intervienen | Restricción 3 (Caso, cap. 10, p.23). Reparto derivado del Caso, numeral 2.2, p.6 | Usuario, opción «148 + 34 + repuestos» |
| D4-02 | 2026-09-28 | Región primaria Azure Chile Central y secundaria Azure Brazil South | Art. 16.3 (FEP01 p.11) exige declarar ambas. La réplica fuera del país exige base de licitud (Art. 23, FEP01 p.17, Ley 21.719) | Usuario, opción «Chile Central + Brazil South» |
| D4-03 | 2026-09-28 | La innovación 3 del plan (visión artificial en cabina) no se desarrolla sin antes proponer alternativas que el equipo elige | Art. 30 (FEP01 p.20), superposición con la innovación 5, Ley 21.719 y restricciones 2, 3 y 6 | Usuario, opción «Proponer alternativas» |
| D4-04 | 2026-09-28 | Todos los diagramas de D4 se hacen en Lucid, específicos de la solución, se exportan y se insertan en el subdocumento | Comunicado 10, sección 4 | Instrucción del usuario |
| D4-05 | 2026-09-28 | La búsqueda de datos y de piezas de hardware se hace con la skill de investigación profunda | | Instrucción del usuario |
| D4-06 | 2026-09-28 | Se trabaja directo en `Formato-Oferta-audIT/` y se transcribe del Informe 1 solo lo necesario de D4 | | Instrucción del usuario |
| D4-07 | 2026-09-28 | Se retoma la adaptación completa del formato al Comunicado 10: nombres `AUDIT-SubdocumentoX`, formularios y anexos en archivos propios, Referencias y Declaración de uso de IA, marcadores como error, verificador corregido | Comunicado 10, secciones 1, 2 y 7 | Usuario, opción «Retomar completo» |
| D4-08 | 2026-09-28 | En el archivo del Subdocumento 4, D4 pone solo los títulos obligatorios 4.1 y 4.1.1 con un marcador para D3, sin contenido | El archivo es compartido. Comunicado 10, sección 11 | Usuario, opción «Solo títulos» |
| D4-09 | 2026-09-28 | La capacidad de almacenamiento a bordo se deriva de abajo hacia arriba y se elige el menor tamaño industrial que la cubre, con el cálculo expuesto. Si da menos de 8 GB, se ajusta | Obs. 73. Comunicado 10, sección 3.3 | Usuario, opción «Derivar y elegir tamaño» |
| D4-11 | 2026-09-28 | Se transcriben del Informe 1, corrigiendo lo criticado: dimensionamiento del búfer y del consumo de datos (a 4.2, con la reconexión masiva), tipología por sitio y brecha de San Bernardo (a 4.3.1, sin celdas explicativas), continuidad y DR como ejes separados (a 4.3.2, con factibilidad), especificación del dispositivo y tabla de emplazamiento (al T-11, con la matriz de trazabilidad en 4.2) | Obs. 64 a 80. Comunicado 10, secciones 5 y 11 | Usuario, los cuatro bloques |
| D4-12 | 2026-09-28 | Se investiga con la skill de investigación profunda: equipo a bordo, gabinete de terminal, sala de San Bernardo y regiones Azure. Cada pieza encontrada se presenta para aprobación antes de usarla | D4-05 | Usuario, las cuatro opciones |
| D4-13 | 2026-09-28 | Las alternativas para la innovación 3 se investigan en paralelo con el hardware | D4-03 | Usuario, opción «En paralelo» |
| D4-14 | 2026-09-28 | Se corrigen las líneas 188 y 226 de `TRASPASO-SESION.md` | Caso, numeral 2.2, p.6 | Usuario, opción «Sí, corrige» |
| D4-15 | 2026-09-28 | Cada subdocumento se entrega también en versión `.md` junto al PDF | | Instrucción del usuario |
| D4-16 | 2026-09-28 | Antes de elegir la clase de equipo a bordo se buscan dos o tres candidatos más por clase (rastreador profesional y computador vehicular Linux) | `investigacion/01-equipo-a-bordo.md`, decisión A1 | Usuario, opción «Más candidatos primero» |
| D4-17 | 2026-09-28 | El equipo lee el bus del camión con un lector sin contacto, sin cortar cables | Restricción 6 (Caso, p.24). Decisión A2 | Usuario, opción «Lector sin contacto» |
| D4-18 | 2026-09-28 | El conductor se identifica con tarjeta RFID acercada al lector con el camión detenido | Caso, RT-12.11, p.32, y restricción 1, p.23. Decisión A3 | Usuario, opción «Tarjeta RFID detenido» |
| D4-19 | 2026-09-28 | Módem satelital de ráfaga corta en los 182 equipos audIT | Tramos de más de 80 km sin señal (restricción 4, p.23). Cierra la observación de «módulos satelitales no estimable». Decisión A4 | Usuario, opción «Módem en todos» |
| D4-20 | 2026-09-28 | El apagado de 2G y 3G que puede dejar sin señal a los 192 equipos de terceros se registra como riesgo del Subdocumento 8 y queda en espera para avisar a la dupla 2 | Diario Financiero, 02-02-2026. Decisión A5 | Usuario, opción «S8 y aviso a D2» |
| D4-21 | 2026-09-28 | Recuperación activo-pasivo: Brazil South en espera con réplicas asíncronas y conmutación documentada | FEP02, RT-07.01 y RT-07.04, p.17. Decisión B1 | Usuario, opción «Activo-pasivo» |
| D4-22 | 2026-09-28 | Las réplicas en Brazil South usan redundancia local o de zona, nunca geográfica, para que los datos no lleguen a South Central US | La pareja de Brazil South es South Central US (Microsoft Learn, 23-09-2026). Art. 23, FEP01 p.17. Decisión B2 | Usuario, «Apruebo las dos» |
| D4-23 | 2026-09-28 | La latencia entre Chile Central y Brazil South se declara como dato a medir en Etapa 1, con el mínimo físico de unos 26 ms calculado desde los 2.586 km | Microsoft no publica la latencia de Chile Central. Decisión B3 | Usuario, «Apruebo las dos» |
| D4-24 | 2026-09-28 | Equipo a bordo: iWave G26I (Linux, IP67, −40 a +70 °C, 9 a 32 V, eMMC ampliable, 3 CAN con J1939, RS232). E-Mark y homologación SUBTEL quedan como condición de compra a confirmar | `investigacion/01-equipo-a-bordo.md`. Decisión A1 | Usuario, opción «iWave G26I» |
| D4-25 | 2026-09-28 | Módem satelital de ráfaga corta: Iridium Edge en los 182 equipos. Homologación en Chile como condición de compra | Decisiones D4-19 y A4. Comparado con el Webfleet SAT a pedido del usuario: es el mismo módem, pero exige el LINK 7XX, manda los datos a Webfleet y guarda 40 h. Su ficha chilena indica que el Iridium Edge ya se vende en Chile | Usuario, opción «Sí, Iridium Edge» |
| D4-26 | 2026-09-28 | Tabla del Artículo 46: cada subdocumento muestra sus filas después del índice detallado, y la tabla completa con las observaciones generales va en un archivo propio que define la dupla 1 | Comunicado 10 no le asigna archivo. Plan maestro, sección 6.1 | Usuario, opción «Filas en cada subdoc + completa aparte» |
| D4-27 | 2026-09-28 | La carátula del sobre (hoja resumen y tabla completa) no se genera en los informes. En la propuesta final se revisa contra el Art. 40.3 | Nomenclatura del Comunicado 10, sección 1 | Usuario, opción «Solo en la final» |
| D4-28 | 2026-09-28 | En la Declaración de uso de IA, la revisión humana se firma con nombre y cargo en audIT. Hay que avisar al equipo porque el plan maestro prohíbe nombres | Comunicado 10, sección 7.2 | Usuario, opción «Nombre y cargo en audIT» |
| D4-29 | 2026-09-28 | Cada formulario sale en su propio PDF con portada y ficha, igual que los subdocumentos | Comunicado 10, sección 1. Art. 40 | Usuario, opción «Portada y ficha» |
| D4-30 | 2026-09-28 | Las bases citadas en el texto entran a «Referencias» en APA con autor Transportes Curimón S.A. (FEP01, FEP02, Caso y Comunicados 9 y 10), solo en los subdocumentos que las citan | Comunicado 10, sección 6.3. Revisión del Informe 1, obs. 05 | Usuario, opción «Sí, autor el mandante» |
| D4-31 | 2026-09-28 | El nombre del ZIP del Informe 2 lo decide la dupla 1. El formato lo deja configurable | Comunicado 10, sección 1.4. Las bases solo nombran el ZIP de la final (Art. 51) | Usuario, opción «Lo decide D1» |
| D4-32 | 2026-09-28 | Cada capítulo abre con el título literal del Comunicado 10 (por ejemplo «Introducción a la Arquitectura Lógica y Física de la Solución»). Portada y ficha mantienen el nombre del T-7 | Comunicado 10, secciones 2.1 y 11 | Usuario, opción «El del Com. 10» |
| D4-33 | 2026-09-28 | Los títulos 13.1 a 13.5 se copian literales con raya («Innovación 1 — Producto o servicio»). Es la única excepción a la regla de no usar raya, porque es texto exigido | Comunicado 10, sección 11, capítulo 13 | Usuario, opción «Literal con raya» |
| D4-34 | 2026-09-28 | Almacenamiento a bordo derivado: arranque 16 MB (Mender), sistema A y B 2 × 1 GB (supuesto: imagen ≤ 1 GB, se verifica en Etapa 1), búfer de 288 h 38,4 MB (método del Informe 1: 3,2 MB por 72 h con fotos × 4 × 3), registros 256 MB (supuesto), geocercas y maestros 16 MB. Total ≈ 2,4 GB. Se declaran 8 GB como configuración mínima del G26I, margen 3,3 veces. Escrituras ≈ 14 GB al año (supuesto: 12 actualizaciones de 1 GB al año), sin límite de desgaste | Obs. 73. Mender, documentación de variables. Decisión D4-09 | Usuario, opción «Apruebo» |
| D4-35 | 2026-09-28 | El dimensionamiento de ingesta y reconexión se hace para 300 camiones simultáneos, aunque hoy los equipos audIT sean 182 | Caso, numeral 14.2, p.30. Obs. 74 | Usuario |
| D4-36 | 2026-09-28 | IoT Hub S1 con 2 unidades (800 mil mensajes al día). Reconexión de 300 camiones en 9,6 min con el límite de 100 envíos por segundo | Microsoft Learn, cuotas de IoT Hub (06-05-2026). RT-03.13, Caso p.31 | Usuario |
| D4-37 | 2026-09-28 | Las fotos acumuladas se suben en un paquete por camión al reconectar: 3 min para 300 camiones con una unidad | Límite de 1,67 cargas por segundo por unidad | Usuario |
| D4-38 | 2026-09-28 | El equipo a bordo se actualiza solo en terminal, por la red del terminal. Enlace principal de al menos 10 Mbit/s por terminal más el respaldo que exige el RT-03.24 | Restricción 5 (Caso p.23). Cálculo en `investigacion/03-dimensionamiento.md` | Usuario |
| D4-39 | 2026-09-29 | Nodo de continuidad de San Bernardo: 2 Dell PowerEdge R360 en alta disponibilidad activo-pasivo con virtualización. Consumo supuesto 300 W cada uno, a verificar con la herramienta de Dell | FEP02, numeral 6.1, p.14. Decisión C1 | Usuario, opción «2 × Dell R360 en HA» |
| D4-40 | 2026-09-29 | Red de San Bernardo: 2 FortiGate 90G en alta disponibilidad y 2 switches. Enlace con Azure por ExpressRoute con un proveedor de Santiago (Cirion, Equinix o PitChile) y VPN de respaldo por otro proveedor, con rutas físicas distintas | FEP02, RT-06.32, p.17. Microsoft Learn, ExpressRoute (16-09-2026). Decisiones C2 y C4 | Usuario, opción «FortiGate 90G HA + ExpressRoute + VPN» |
| D4-41 | 2026-09-29 | Extinción con FK-5-1-12 de un fabricante vigente (Fike o Kidde), en reemplazo del Novec 1230 del Informe 1, que dejó de fabricarse a fines de 2025 | FEP02, RT-06.17, p.15. Decisión C3 | Usuario, opción «FK-5-1-12 de otro fabricante» |
| D4-42 | 2026-09-29 | Gabinete de cada terminal regional: 2 OnLogic Karbon 430 en activo-pasivo, router Teltonika RUTX50 como respaldo del enlace fijo de 10 Mbit/s, punto de acceso para actualizar camiones y UPS | Caso, RT-03.10, p.31. D4-38. Decisión C5 | Usuario, opción «2 Karbon 430 + RUTX50 + UPS» |
| D4-43 | 2026-09-29 | Lectores del equipo a bordo: CANCrocodile de Technoton (sin contacto, salida CAN 2.0B J1939, 10 a 50 V) al CAN del G26I, y lector MIFARE DESFire IP66 de GAO RFID por el RS485 del G26I | D4-17 y D4-18 | Usuario, opción «CANCrocodile + GAO DESFire» |
| D4-44 | 2026-09-29 | Tarjetas RFID de conductor: 572 (520 conductores proyectados a 3 años más 10 % de reposición) | Caso, numeral 14.1, p.29 | Usuario |
| D4-45 | 2026-09-29 | Cinco ambientes, cada uno en su suscripción: desarrollo y QA en Chile Central con niveles menores, preproducción igual a producción a escala reducida, producción en tres zonas y DR en Brazil South en espera | Comunicado 10, capítulo 4, 4.2 | Usuario, opción «Cinco, pre a escala reducida» |
| D4-46 | 2026-09-29 | Conmutación a Brazil South: el monitoreo detecta y alerta con criterio declarado, la guardia confirma y ejecuta un procedimiento automatizado | FEP02, RT-07.05 y RT-07.08, p.17 | Usuario, opción «Detección automática, decisión humana» |
| D4-47 | 2026-09-29 | Red en Azure hub and spoke: red central con el firewall de Azure y las puertas de ExpressRoute y VPN, y una red por ambiente con subredes de borde, aplicación, datos, integración y gestión | FEP01, Art. 16.3, p.11 | Usuario, opción «Hub and spoke» |
| D4-48 | 2026-09-29 | El T-11 declara 182 equipos a bordo más 19 de reposición (10 %) para la Etapa 1, y una fila aparte con 22 equipos para los propios nuevos a 3 años, comprados en operación | Caso, numeral 14.1, p.29 | Usuario, opción «Cantidad inicial más fila de crecimiento» |
| D4-49 | 2026-09-29 | Se readapta al Comunicado 10 el formato local `/mnt/NuevoVol/FEP/Formato-Oferta-audIT`, solo en lo que exigen el 4 y el 13 (nombres `AUDIT-…`, índice del Com. 10, cierre con Referencias y Declaración de uso de IA). El repo del equipo no se toca | Los fuentes adaptados de D4-07 se perdieron. Solo queda el PDF en `D4-revision-Subdocumento4-20260929.zip` | Usuario, opción «Local, lo adapto» |
| D4-50 | 2026-09-29 | Se generan el 4 y el 13 como documentos principales, y además `AUDIT-Formulario-T-11.pdf` y `AUDIT-Formulario-T-19.pdf` en archivo propio, cada uno con su `.md`. No se generan archivo de anexos ni tabla del Art. 46 aparte | Comunicado 10, sección 1 | Usuario: «Genera los anexos igualmente, pero lo principal son los subdocumentos» |
| D4-51 | 2026-09-29 | La 4.1 y la 4.1.1 se trasladan del PDF entregado en el Informe 1 sin quitar contenido, ordenadas al índice del Com. 10, y lo que pidió el profesor se marca «[Información requerida por dupla 3]». Reemplaza a D4-08 | Instrucción del usuario: no quitar información del Informe 1 | Usuario, opción «PDF entregado + marcas D3» |
| D4-52 | 2026-09-29 | Las innovaciones 1, 2, 4 y 5 se trasladan del PDF del Informe 1 quitando solo lo que el profesor sancionó (nombres, punto 1.6, horas hombre, cifras en pesos, líneas base sin fuente), y lo que falta se marca «[Información requerida por dupla N]»: 1 y 4 a D2, 5 a D1, 2 a D3 | Obs. 88 a 100. Reparto del Informe 1 (S13 p.13) y plan maestro | Usuario, opción «PDF entregado, depurado» |
| D4-53 | 2026-09-29 | Lo que depende de otra dupla se marca en el PDF y en el `.md` como «[Información requerida por dupla X]». Se advirtió que el verificador (punto 11) y el Com. 10 (7.1 d) lo tratan como residuo y deben retirarse antes del 05-10 | | Instrucción del usuario |
| D4-54 | 2026-09-29 | Se mantiene D4-25: Iridium Edge conectado al G26I. El Webfleet SAT se descarta como paquete porque exige el LINK 710/740, manda los datos a la plataforma de Webfleet y guarda 40 h. Su ficha chilena se cita como prueba de que el Iridium Edge se vende en Chile | RT-03.10 y RT-10.05 del Caso, p.31 y 32. Art. 23, FEP01 p.17 | Usuario, opción «Iridium Edge al G26I», tras proponer Webfleet SAT |
| D4-55 | 2026-09-29 | Innovación tipo 3: semirremolque conectado. Balizas Bluetooth en los semirremolques propios leídas por el G26I y en portería, para verificar el semirremolque que sale, medir sus kilómetros y registrar temperatura en los refrigerados. Cierra la decisión E | `investigacion/05-innovacion-3.md`. Art. 28 y 30, FEP01 pp.19 y 20 | Usuario, opción «A. Semirremolque conectado» |
| D4-56 | 2026-09-29 | Equipos de sala y terminal: 2 FortiSwitch 124F-POE, 5 FortiAP 234G, 4 Teltonika TSW202, 4 APC SRT1000XLI, 2 APC SRT3000RMXLI con 1 SRT96RMBP cada una (alimentación A y B), 2 Liebert Mini-Mate2 MMD12E (N+1), VESDA VLF-250, Kidde Fluoro-K, 2 Suprema FaceStation F2 en esclusa, Himoinsa HYW-8 T5 S5 con estanque de 100 L, 5 Minew G1 en portería. Cierra G y K | `investigacion/06-hardware-pendiente.md` | Usuario, opción «Apruebo todo» |
| D4-57 | 2026-09-29 | Balance de San Bernardo: 996 W de TI, 1.944 W en total, PUE 1,95, factor de potencia de diseño 0,95. Cierra H | FEP02, RT-06.11, p.15. `investigacion/sala_san_bernardo.py` | Usuario, opción «Apruebo todo» |
| D4-58 | 2026-09-29 | ExpressRoute de 100 Mbit/s en Santiago con VPN de respaldo por el segundo proveedor de San Bernardo. Cierra J | Derivación en `sala_san_bernardo.py`. Caso p.12 | Usuario, opción «Apruebo todo» |
| D4-59 | 2026-09-29 | Catálogo de nube: Event Hubs Premium y PostgreSQL Flexible con TimescaleDB según el plan maestro, Front Door y API Management Premium, Key Vault Premium, AKS e IoT Hub S1 × 2. Caché y confirmación del stack con marca para D3. Cierra F | Plan maestro, 3.3. Retiro de Azure Cache for Redis el 30-09-2028 | Usuario, opción «Plan + marca D3» |
| D4-60 | 2026-09-29 | Plano de San Bernardo con las zonas del RT-06.03 proporcionado a 26 m², con nota de que las medidas de detalle se confirman en el levantamiento. Cierra I | Caso p.12 da solo la superficie | Usuario, opción «Zonas a escala de 26 m²» |
| D4-10 | 2026-09-28 | Diagramas en Lucid: vista general, región primaria con redes y SKU, región secundaria y conmutación, plano de la sala de San Bernardo, gabinete de terminal, dispositivo a bordo, enlaces con anchos de banda y SPOF, ambientes de desarrollo a DR | Comunicado 10, secciones 4 y 11 (4.2) | Usuario, las cuatro opciones |

## Diagramas en Lucid (D4-10)

| Figura | Documento de Lucid | Archivo en el formato |
|---|---|---|
| Arquitectura física general (4-fisicafig) | https://lucid.app/lucidchart/1c11af5b-81ae-4f1a-9606-eddce55fd523/edit | `figuras/04-arquitectura/fisica-general.png` |
| Región primaria Azure Chile Central (4-azurefig) | https://lucid.app/lucidchart/017b6f81-f41c-411a-9555-8001029df3c6/edit | `figuras/04-arquitectura/region-primaria.png` |
| Equipo a bordo (4-bordofig) | https://lucid.app/lucidchart/6586a83f-cfbb-44e0-8ee1-ac8cd4f76a61/edit | `figuras/04-arquitectura/equipo-a-bordo.png` |
| Ambientes (4-ambientesfig) | https://lucid.app/lucidchart/0a366ea4-945f-49ae-a9e1-44c682f1ab41/edit | `figuras/04-arquitectura/ambientes.png` |
| Reconexión masiva (4-reconexionfig) | https://lucid.app/lucidchart/7520d0e1-be65-4c1b-9212-51068b784029/edit | `figuras/04-arquitectura/reconexion.png` |
| Sala de San Bernardo (4-planofig) | https://lucid.app/lucidchart/53f217fd-0b70-4a8c-987f-0b84da61f0a7/edit | `figuras/04-arquitectura/sala-san-bernardo.png` |
| Gabinete de terminal (4-terminalfig) | https://lucid.app/lucidchart/a22bea8c-0975-4cfa-93e4-c917bc6a7853/edit | `figuras/04-arquitectura/gabinete-terminal.png` |
| Recuperación y continuidad (4-drfig) | https://lucid.app/lucidchart/5ca729a7-9c53-42fb-a92f-4e5e728c154b/edit | `figuras/04-arquitectura/recuperacion.png` |

Se generan con `D4/lucid/lucidgen.py` y un guion por figura (`d1_general.py` a `d8_recuperacion.py`),
con íconos Azure 2024 y la paleta del manual de marca. Se exportan como PNG a 160 DPI, casi 1:1 con la
página, y `D4/lucid/recortar.sh` quita el margen. La letra es de 10 pt en Lucid y llega impresa sobre
9 pt. Si el verificador necesita medir la letra en vectorial, se exportan a mano como PDF desde Lucid
(Archivo, Exportar, PDF).

Quedan en la cuenta de Lucid versiones intermedias que se pueden borrar: cfd65255, 198e3e82,
0ca7a66f, 4dd665a7, c7cad875, 6e1e06f7, f658dacc, 14c577e5, 5fbda6c7, e6b553de (prueba de rótulos) y las de la
sesión anterior d1726381, 234ae633 y 94c4400a.

## Lo que no es decisión porque lo fijan las bases

| Materia | Valor | Fuente |
|---|---|---|
| Disponibilidad de servicios críticos | 99,9 % mensual, medida sobre la transacción de extremo a extremo | FEP01, Art. 20, p.14 |
| Índice del capítulo 4 | Introducción, 4.1, 4.1.1, 4.2, 4.2.1, 4.3, 4.3.1, 4.3.2. Anexo T-11 | Comunicado 10, sección 11 |
| Índice del capítulo 13 | Introducción, 13.1 a 13.5 «Innovación N» con su tipo. Anexo T-19 | Comunicado 10, secciones 8 y 11 |
| Reparto de la flota | 148 propios equipados, 192 de terceros con equipo, 34 de terceros sin equipo | Caso, numeral 2.2, p.6 |

## Correcciones a documentos internos

| Fecha | Documento | Error | Corrección |
|---|---|---|---|
| 2026-09-28 | `D4/TRASPASO-SESION.md`, líneas 188 y 226 | Dice que el reparto de los 340 entre propios y terceros no está en el caso | Está en el Caso, numeral 2.2, p.6. Corregido (D4-14) |
| 2026-09-28 | `Formato-Oferta-audIT/herramientas/verificar.py`, punto 11 | Marca «192 camiones» como residuo prohibido | El 192 es derivable. Regla quitada (D4-14) |
| 2026-09-29 | Formato, `estilo/tablas.sty` | Una tabla corta (Tabla 4.8) quedaba partida entre dos folios | Opción `junta` que impide el corte. El Comunicado 10, sección 5.3 pide tablas de una página |
| 2026-09-29 | Formato, `estilo/figuras.sty` | La leyenda «Fuente:» salía centrada bajo un título alineado a la izquierda | Alineada a la izquierda, igual que el título de la figura |
| 2026-09-29 | Formato, `estilo/cierre.sty` | En Referencias la lista justificada estiraba las URL («https : / / …») | Lista alineada a la izquierda, como pide APA 7 |
| 2026-09-29 | Formato, `estilo/citas.sty` y `estilo/ensamblado.sty` | La ficha de un formulario decía que las referencias estaban «al final del subdocumento», pero el formulario es otro archivo | La ficha del formulario y la de anexos remiten a las Referencias del Subdocumento N.º N |
| 2026-09-29 | Formato, `herramientas/verificar.py`, punto 20 | No reconocía el encabezado de la página horizontal («SUBDOCUMENTO 4 · Página horizontal…») | Busca sin distinguir mayúsculas y reconoce el nuevo rótulo |
| 2026-09-29 | Formato, `herramientas/tex2md.py` | El Markdown dejaba `\figuraHorizontal` sin convertir, numeraba mal las figuras, apuntaba mal a las imágenes y rompía las URL de Referencias | Convierte la figura horizontal con su fuente, usa el número de la etiqueta, rutas relativas a `salida/<instancia>/` y extrae las referencias sin perder los guiones de las URL |
| 2026-09-29 | `subdocumentos/04-arquitectura/contenido.tex` | Citas con doble paréntesis: «((Caso, capítulo 10, p. 23))» | `\caso*` ya pone los paréntesis. Se quitaron los de afuera |
| 2026-09-30 | Formato, `herramientas/verificar.py`, punto 11 | La regla del «192 camiones» había vuelto al restaurar el formato (D4-49) | Quitada otra vez, con su mención en `GUIA.md` (D4-14) |
| 2026-09-30 | Formato, `formulario.tex` | `\DocumentoFormulario` recibía `\NumeroSubdoc` sin expandir: el T-11 salía como plantilla vacía de 4 folios y la ficha con huecos | Los dos argumentos se expanden antes de entrar. El T-11 sale con sus 68 filas en 13 folios |
| 2026-09-30 | Formato, `estilo/comunicado10.sty` y `herramientas/verificar.py`, punto 20 | Las páginas del formulario en archivo propio se tomaban por preliminares | El formulario registra el folio `formsd-N` donde empieza su contenido y el verificador lo asigna al subdocumento N |
| 2026-09-30 | Formato, `estilo/ensamblado.sty` y `herramientas/tex2md.py` | El título «Resolución de observaciones» iba seguido directo de la tabla (Comunicado 10, sección 3.1) | Párrafo de caída antes de la tabla, en el PDF y en el Markdown |
| 2026-09-30 | Formato, `estilo/citas.sty` | Cuatro direcciones largas desbordaban en Referencias (punto 8) | Corte de URL en cualquier carácter y holgura de 1 pt en la bibliografía |
| 2026-09-30 | Formato, `herramientas/tex2md.py` | El Markdown dejaba `\notaTabla` y `$-40$` sin convertir | Fuente de tabla en cursiva y matemática simple como texto |
| 2026-09-30 | `subdocumentos/04-arquitectura/contenido.tex` | Bastion figuraba en la subred de gestión en el catálogo y en la red central en el plan de direcciones | Red central en ambos. Es donde vive en una topología central y radial |
| 2026-09-30 | `subdocumentos/04-arquitectura/contenido.tex`, 4.3.2 | Decía que São Paulo está en «otra placa tectónica»: Santiago y São Paulo están en la placa Sudamericana | «Lejos de la zona de subducción que concentra los grandes sismos de Chile». También se quitó «a unos 20 km de la región primaria», porque Microsoft no publica dónde están sus centros de datos |
| 2026-09-30 | `subdocumentos/04-arquitectura/contenido.tex` y T-11 | «CO$_2$» imprimía el subíndice a 7,7 pt (punto 5) | «Dióxido de carbono», también en la leyenda del plano |
| 2026-09-30 | `subdocumentos/04-arquitectura/formularios/T-11.tex` y `declaracion-ia.tex` | «dupla» en texto corrido fuera de un marcador | Pasado a marcador en el T-11 y reescrito en la declaración |

## En espera porque depende de otra dupla

| Materia | Dupla | Por qué afecta a D4 |
|---|---|---|
| 4.1.1 Tecnologías de software, versiones y fin de soporte (obs. 58, 62, 63 y 68) | D3 | El Comunicado 10 la pone bajo 4.1. La 4.2 tiene que usar los mismos productos |
| Motor de series de tiempo y bus de eventos (obs. 65 y 84) | D3 | Define los servicios y SKU del diagrama físico |
| Modelo Zero Trust (parte de la obs. 80) | D3 | El Comunicado 10 lo pone en 4.1. D4 solo refleja la segmentación de red |
| Emisor del documento electrónico (obs. 76) | D3 y D2 | D4 solo asegura que ningún equipo del T-11 emita documentos |
| Residencia del dato y región del respaldo en el S5 (obs. 83) | D3 | Tiene que coincidir con D4-02 |
| Fichas 1, 4 y 5 del T-19 y texto común del capítulo 13 (obs. 99, 100 y 12) | Sin asignar en el plan | D4 solo escribe 13.3 y su ficha |
| Parámetros del plan maestro: SLA 99,5 %, East US 2, «374 gateways», desglose de 8 GB, terminales Valparaíso y Concepción | Todo el equipo | Chocan con las bases o con D4-01 y D4-02 |
| Consolidación de la tabla del Artículo 46 | D1 | D4 solo actualiza las filas 64 a 80 y las de la innovación 3 |
| Nombre del ZIP del Informe 2 (D4-31) y nombre del archivo con la tabla completa del Art. 46 (D4-26) | D1 | El formato los deja configurables |
| Nombres con cargo en la Declaración de uso de IA (D4-28) | Todo el equipo | Choca con la regla del plan maestro que prohíbe nombres |
| Apagado de 2G y 3G y los 192 equipos de terceros (D4-20) | D2 | Afecta el plan de adhesión y la modalidad «de datos» del Subdocumento 3 |
| Chile Central sin región pareja, sin respaldo georredundante de PostgreSQL, riesgo de retraso de la réplica en el peak y base de licitud de la réplica en Brazil South | D3 | El Subdocumento 5 tiene que coincidir con 4.3.2 |

## Decisiones pendientes

Las decisiones E a L quedaron cerradas por D4-55 a D4-60. Estas están aplicadas en el Subdocumento 4
y esperan aprobación explícita. Se mueven a «aprobadas» cuando la dupla responde.

| N.º | Decisión aplicada | Dónde está |
|---|---|---|
| M | Videovigilancia con cuatro Axis M3215-LVE y grabador S3008 Mk II de 4 TB para 30 días | 4.3.1, T-11 |
| N | Detector de agua Liebert LT460 y dos extintores portátiles de dióxido de carbono | 4.3.1, T-11 |
| O | Dos racks de 24 unidades, servidores y comunicaciones separados | 4.3.1, plano |
| P | Plan de direcciones: 10.10 a 10.14 en Chile Central, 10.20 y 10.21 en Brazil South, 172.16.0.0/22 San Bernardo y 172.16.4.0/22 terminales | 4.2.5 |
| Q | Azure Firewall Premium, Bastion en la red central y puertas ErGw1AZ y VpnGw1AZ | 4.2.4, 4.2.5 |
| R | La custodia física de RT-06.26 se cubre con la copia inmutable fuera de sitio que el mismo requisito admite | 4.2.6 |
| S | El equipo a bordo conserva 72 horas de lo ya enviado para reenviarlo tras una conmutación | 4.3.2 |
| T | Servidor PostgreSQL de series separado del transaccional (también marcado para D3) | 4.2.4, 4.3.2 |
| U | Criterio de conmutación: región primaria sin responder 15 minutos, con confirmación de la guardia | 4.3.2 |
| V | RT-08.04 en el FortiSwitch 124F-POE de fuente única: la redundancia la da el par, cada equipo en otro circuito | 4.2.7 |
| W | S-18: las suscripciones de Azure a nombre del mandante | 4.2.9 |
| X | Diseñar San Bernardo y terminales para 24 horas sin enlace y declarar la diferencia entre Art. 16.4 (24 h) y RT-03.10 (12 h) | 4.3 |
| Y | Planta supuesta de 6,5 × 4 m para el plano de 26 m² | 4.3.1, plano |
| Z | Nivel «Medio» en diagramas en la Declaración de uso de IA: los ocho diagramas se escribieron como código para Lucid a partir de las decisiones aprobadas | Declaración de uso de IA del S4 |

## Estado al 2026-09-30

Subdocumento 4 terminado en el formato local. `Formato-Oferta-audIT/salida/informe2/`:
`AUDIT-Subdocumento4.pdf` (64 folios), `AUDIT-Formulario-T-11.pdf` (13 folios) y sus dos `.md`.
Ocho diagramas en Lucid, tabla del Art. 46 del S4 (filas 53 a 80) en `anexos/observaciones-informe1.tex`,
filas 64 a 80 actualizadas en `Informe/Tabla-Art46-Informe2.md`. El verificador da 21 puntos: no
cumplen el 6 (figuras de D3 con letra de 3,2 pt, y los PNG de D4 no se pueden medir aunque imprimen a
9,6 pt o más) y el 11 (solo los marcadores «[Información requerida por dupla N]» de D4-53).

Falta: aprobación de M a Z, Subdocumento 13 con su T-19 y filas 88 a 100 del Art. 46, y retirar los
marcadores antes del 05-10.
