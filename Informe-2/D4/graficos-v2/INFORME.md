# Informe de la segunda vuelta de las figuras de los Subdocumentos 4, 7 y 13

Fecha: 7 de octubre de 2026. No se tocó ningún `.tex`, ni `Formato-Oferta-audIT/`, ni `audIT/`. La primera vuelta sigue intacta en `D4/graficos-nuevos/`.

Abreviaturas de las fuentes que se citan con su línea:

- S4: `Formato-Oferta-audIT/subdocumentos/04-arquitectura/contenido.tex`.
- T-11: el formulario `formularios/T-11.tex` del mismo subdocumento.
- T-15: `07-plan-trabajo/formularios/T-15.tex`.
- S13: `13-innovaciones/contenido.tex`.
- T-19: `13-innovaciones/formularios/T-19.tex`.
- S3: `audIT/recursos/Formato-Oferta-audIT/subdocumentos/03-solucion/contenido.tex`.
- T-12: `03-solucion/formularios/T-12.tex`.
- MT: `message.txt`.

## Qué hay en esta carpeta

- `04-arquitectura/`, `13-innovaciones/` y `07-plan-trabajo/`: las 19 figuras de la primera vuelta, rehechas, más la EDT (`edt`) y la carta Gantt (`gantt`) de la dupla 2.
- `propuestas/`: las tres figuras nuevas (`racks-san-bernardo`, `instalacion-a-bordo` y `documento-sin-cobertura`).
- Cada figura va en SVG (con el texto como texto), en PDF vectorial con IBM Plex incrustada y en PNG de 300 dpi.
- `lamina.png`: las 24 figuras juntas.
- `comparacion.png`: cada una de las 19 figuras de la primera vuelta al lado de su segunda versión.
- `iconos/` y `CREDITOS.md`: 88 íconos de terceros, 37 propios y 10 compuestos, cada uno con su fuente y su licencia.
- `fuente/`: los guiones. `fuente/generar.py` regenera todo y vuelve a medir: `Formato-Oferta-audIT/herramientas/.venv/bin/python fuente/generar.py`.

## Comprobaciones hechas en las 24 figuras

- **Letra.** `herramientas/letra_diagramas.py` da 9,00 pt de mínimo en todas, ningún par de rótulos que choque y nada fuera del lienzo.
- **Fuentes y raster.** `pdffonts` muestra solo `IBMPlexSans` e `IBMPlexSans-SmBld`, y `pdfimages` no encuentra imágenes raster en ningún PDF.
- **Líneas sobre íconos y rótulos.** `fuente/lienzo.py` revisa cada figura en busca de líneas que crucen un ícono, una ficha o un texto. Los únicos casos que quedan son intencionales:
  - en `LogicaIntegraciones` y `documento-sin-cobertura`, la ficha se pone sobre su propia línea, como rótulo;
  - en `equipo-a-bordo` e `instalacion-a-bordo`, el arnés pasa bajo la pinza del CANCrocodile.
- **Cruces.** Donde dos líneas se cruzan, la que se dibuja después lleva un salto de 3 pt. Lo hace el lienzo de forma automática.
- **Color.** Fuera de los íconos hay blanco, el gris #F7F8FA de las subredes, grises neutros en barras, conos de cámara y racks, y el rojo #C0392B solo en la ruta crítica del PERT. La vista lateral `instalacion-a-bordo` usa la paleta de los íconos para el camión, porque es un dibujo y no una caja. Todo el texto es negro.
- **Lo que no se verificó con herramienta.** La grilla de 6 pt se siguió en las coordenadas principales, pero quedan posiciones intermedias: en el plano de la sala, a escala, y en los nodos PERT, escalados desde la grilla del guion. La separación mínima de 12 pt entre rótulos se revisó a ojo en cada figura; la herramienta solo detecta choques.

## Correcciones que valen para todas las figuras

1. **Nombres del PERT.** Ahora se leen de la malla del T-15, no de `d11_pert.py`. Los dos coinciden en precedencias, duraciones, ES, EF, LS y LF; solo difieren en los nombres. La descripción del T-15 no cabe en un nodo a 10 pt, así que cada nodo lleva un nombre corto hecho con palabras de esa descripción (tabla al final).
2. **Plataformas de terceros.** Usan el ícono de rastreador GPS (`pr-rastreador`) en todas las figuras.
3. **Región.** Se dibuja con `az-region`; el logo de Azure ya no aparece.
4. **Personas.** Cada rol tiene su ícono: una persona de Fluent Emoji con un distintivo.

   | Rol | Ícono |
   |---|---|
   | Conductor | volante |
   | Operador de torre | frente a la pantalla, con audífonos |
   | Terminal y taller | overol y llave |
   | Transportista | camión |
   | Cliente | edificio |
   | Gerencia | maletín |
   | Finanzas | gráfico |
   | Operaciones | casco y lista |

5. **Rótulos sueltos.** «Solo lectura» va sobre su flecha, y «Total < 2 s de 30 s» se reemplazó por la barra de presupuesto.
6. **Espacios vacíos.** Se llenaron con el detalle que pedía el encargo.
7. **Fichas.** El detalle va en cajas blancas de 9 pt, de dos a cuatro palabras. En algunas el texto del documento se abrevió; se indica en cada figura.
8. **Densidad.** `fisica-general` (unos 60 elementos rotulados) y `LogicaCapas` (unos 75) superan la guía de 45 de una figura horizontal. Todo cabe a 9 pt, así que no se sacó nada. Si el equipo quiere aligerarlas, lo más prescindible es:
   - en `fisica-general`, las fichas de zona y las de cada equipo dentro de los racks;
   - en `LogicaCapas`, la columna de servicios externos, que ya está en `LogicaIntegraciones`.

## Figura por figura

### Arquitectura física (S4)

**`fisica-general`** (horizontal, letra mínima 9,00 pt).
Qué cambió:
- La nube tiene tres fichas de zona y, en cada región, la red central y la red de producción como bloques.
- San Bernardo tiene dos minirracks, la torre, el grupo electrógeno y el patio con FortiAP y Minew. También los dos sistemas existentes, detrás de la capa anticorrupción, con la autoridad tributaria colgada del sistema contable.
- Los terminales muestran el gabinete con sus cuatro equipos y, fuera, el punto de acceso y el lector de portería.
- El enlace LTE pasa por el operador móvil, y el de Iridium por el satélite y la puerta de Iridium, en ambos sentidos.
- La flota suma los 210 semirremolques con baliza (44 refrigerados), unida al iWave G26I por Bluetooth.
- Las contrapartes se separan en «Por lotes» (línea discontinua) y «En línea».

Datos nuevos y su fuente:
- Equipos de los racks: S4 1229–1231 y T-11 156–189.
- Torre de 22 personas en turnos: MT 128 (`TORRE`).
- Patio de San Bernardo: MT 148 (`PAT_SB`).
- Zonas: S4 1133–1135.
- Rangos de Brazil South: S4 849–850.
- 210 semirremolques y 44 refrigerados: S13 203–206.
- Contrapartes: MT 172–180 y S4 326–334.

Diferencias con el texto:
- La **puerta de enlace de Iridium** no está en las fuentes; MT solo tiene «Red Satelital Iridium (SBD)». Se dibujó porque lo pidió el encargo. Si el equipo la mantiene, conviene nombrarla en el párrafo de enlaces (S4 906–908).
- El texto de la figura (S4 621–628) no menciona la capa anticorrupción ni las contrapartes. No hace falta cambiarlo.

**`region-primaria`** (horizontal, 9,00 pt).
Qué cambió:
- Flujos internos finos: DPS a IoT Hub, IoT Hub a Event Hubs, Event Hubs a AKS, API Management a AKS, y AKS a los dos PostgreSQL, Blob y Key Vault por un bus.
- Todos los servicios registran en Monitor, en discontinua.
- AKS lleva las fichas Zona 1, 2 y 3, y PostgreSQL transaccional la ficha «Primaria y espera».
- Cada servicio de datos tiene su ícono de punto de conexión privado.
- La salida al firewall pasa por la tabla de rutas, y Bastion llega a las subredes en discontinua.
- El circuito se rotula «ExpressRoute 100 Mbit/s, EdgeConnex SCL», y la réplica a Brazil South sale hacia el borde derecho.
- «Otros ambientes» cupo, así que se mantuvo.

Datos nuevos y su fuente:
- Puntos de conexión privados: S4 845.
- Tráfico por el firewall: S4 857.
- Bastion: S4 860–861.
- Zonas de AKS y espera de PostgreSQL: S4 883–885.
- EdgeConnex SCL: S4 911 y T-11 297.
- Réplica: S4 1273–1283.

Diferencias con el texto: la tabla de rutas es la forma de cumplir «todo el tráfico entre redes pasa por el cortafuegos» (S4 857), pero el texto no la nombra. No es obligatorio agregarla.

**`equipo-a-bordo`** (vertical, 9,00 pt).
Qué cambió:
- Dentro del G26I hay fichas: Linux, elemento seguro TA100 (arranque seguro y claves), audIT EdgeHub, motor de geocercas, búfer de 288 h y SQLite en modo WAL.
- Alimentación desde la batería del camión, de 9 a 32 V.
- Dos antenas sobre el techo, Iridium con doble punta, y el CANCrocodile pinzado sobre el arnés dibujado.
- La barra de memoria tiene la flecha «Actualización» entre los sistemas A y B.

Datos nuevos y su fuente:
- Linux: S4 694.
- TA100, y 9 a 32 V: S4 695–696.
- EdgeHub: S4 698.
- Motor de geocercas: T-11 647.
- Búfer de 288 h: S4 715.
- SQLite: S13 414.
- Dos particiones: S4 716–717.
- Sin cortar los cables: S4 704.

Diferencias con el texto:
- **Antenas en el techo.** Ninguna fuente dice dónde van, y el T-11 (35) ubica el Iridium Edge en la «cabina junto al equipo a bordo». Se dibujaron en el techo porque lo pidió el encargo. Hay que corregir el T-11 o la figura.
- **Batería del camión.** El texto solo dice «funciona de 9 a 32 V».
- **«Modo WAL».** El S13 dice «modo de registro anticipado de escritura». Conviene usar una sola forma en todo el documento.

**`ambientes`** (vertical, 9,00 pt).
Qué cambió:
- La promoción pasa por cada par: desarrollo, QA, preproducción, producción.
- Cada ambiente tiene una fila con AKS, PostgreSQL, IoT Hub y Event Hubs, y su rango.
- Producción lleva tres fichas de zona, y preproducción la ficha «Pruebas de carga 1,5 × peak».
- Del repositorio Git del mandante salen las cinco flechas.

Datos nuevos y su fuente:
- Rangos: S4 846–850.
- 1,5 × peak: S4 877–878.
- Repositorio del mandante: S4 829.
- Recuperación 10.21.0.0/20: S4 850.

Diferencias con el texto: que desarrollo y QA tengan los cuatro servicios se deduce de «los cinco se levantan desde el mismo código» (S4 880), pero el texto no lo enumera. No hace falta cambiarlo.

**`reconexion`** (vertical, 9,00 pt).
Qué cambió: la figura es ahora un embudo con los cinco tramos numerados:
- tres camiones con «192 mensajes», más las fichas «× 300» y «57.600 mensajes»;
- la red celular con espera aleatoria y reintento;
- IoT Hub con su medidor de «100 envíos/s»;
- Event Hubs como cola;
- cuatro pods «Por lotes»;
- PostgreSQL de series.

Abajo va una barra de tiempo proporcional, con 3 s, 1,5 min, 9,6 min y 20 min. La columna derecha mantiene el indicador.

Datos nuevos y su fuente: S4 970–986, 990–995 y 1046.

Diferencias con el texto: ninguna. La frase «la columna derecha de la figura marca la profundidad de la cola» (S4 994–995) sigue siendo cierta.

**`sala-san-bernardo`** (vertical, 9,00 pt).
Qué cambió: es un plano a escala de 6,5 × 4 m, con:
- muros gruesos;
- la esclusa con dos puertas, su giro y un lector en cada una;
- los racks a escala, con el frente marcado y el pasillo de trabajo;
- los climas en muros opuestos, cada uno con su cable detector de agua;
- el cilindro de FK-5-1-12 junto a la esclusa;
- la tubería VESDA discontinua, con sus puntos de muestreo;
- cuatro cámaras con su cono;
- el puesto de trabajo, el estante de repuestos y el tablero eléctrico;
- los dos ductos por muros distintos;
- el patio con el grupo electrógeno y el tablero de transferencia, unido al tablero de la sala por la línea de energía;
- las cotas y una escala de 1 m.

Datos nuevos y su fuente:
- Planta, esclusa y racks: S4 1227–1236.
- Cámaras en sala y esclusa: T-11 248.
- Detector bajo los climas: T-11 268.
- Cilindro junto a la esclusa: T-11 218.
- Climas en muros opuestos: T-11 198.
- 8,8 kVA: S4 1207.
- Tablero propio: S4 1151.

Diferencias con el texto:
- Las medidas de rack (0,6 × 1,0 m) y que la tubería VESDA vaya por el cielo vienen del encargo, no de las fuentes.
- El T-11 (197) dice que el clima es «de cielo»; el plano lo dibuja junto al muro, lo que no contradice «muros opuestos».
- La posición exacta de puertas, ductos y equipos es esquemática, porque el texto la deja para la Etapa 1 (S4 1236–1237).

**`gabinete-terminal`** (vertical, 9,00 pt).
Qué cambió:
- Vista frontal con riel DIN.
- Conexiones internas: RUTX50 al TSW202 por la izquierda, y TSW202 a los Karbon A y B por un bus.
- Los dos Karbon unidos en discontinua (activo y espera).
- La UPS alimenta a todos con una línea fina y un enchufe.
- En el patio, el punto de acceso actualiza un camión por Wi-Fi; en la portería, el Minew G1 lee la baliza del semirremolque que sale por la barrera.
- Fichas «24 h sin enlace» y «83 min».

Datos nuevos y su fuente:
- Riel DIN: S4 1248 y T-11 116.
- 83 min: S4 1252.
- 24 h: S4 1253–1255.
- Patio y portería: S4 1249–1251.

Diferencias con el texto: el texto solo dice «riel DIN» del TSW202, y la barrera de portería no está en las fuentes. Son detalles de dibujo.

**`recuperacion`** (horizontal, 9,00 pt).
Qué cambió:
- Ficha «2 pruebas al año» junto al paso 3.
- Vuelta a Chile Central en discontinua, con la ficha «Conciliación».
- Flecha discontinua «Reenvío de 72 h» desde los camiones a Brazil South.
- South Central US tachado, con la ficha «Sin redundancia geográfica».

Datos nuevos y su fuente:
- South Central US: S4 1281–1283.
- Reenvío de 72 h: S4 1289–1291.
- Conciliación y dos pruebas al año: S4 1304–1306.

Diferencias con el texto: ninguna nueva. Sigue la de la primera vuelta: «Mismo código» no dice que Key Vault tiene sus claves respaldadas (S4 1280–1281).

### Arquitectura lógica (S4, sección 4.1)

**`LogicaCapas`** (horizontal, 9,00 pt).
Qué cambió:
- Cada persona se une a su canal, y cada contexto lleva fichas con lo que decide.
- Nuevo grupo «Servicios externos» unido a la capa de integración, y el camión unido a IoT Hub.
- Los paneles de la izquierda suman Front Door, API Management, AKS, IoT Hub y Event Hubs; Entra ID, Key Vault y Azure Monitor siguen en sus bandas.

Datos nuevos y su fuente: las fichas de los contextos salen de S3 642–653 y del T-12:

| Contexto | Requerimientos del T-12 (línea) |
|---|---|
| Planificación y tráfico | RF-001 (54), RF-015 (208) |
| Flota y activos | RF-005 (106), RF-025 (318) |
| Personas y cumplimiento | RF-002 (66), RF-022 (285) |
| Telemetría y geocercas | RF-008 (132), RF-010 (154) |
| Operación de fletes | RF-006 (110), RF-012 (176), RF-013 (186) |
| Liquidación y costeo | RF-019 (253) |

Diferencias con el texto:
- **Canales.** El encargo pide que el operador de torre vaya al portal web y el personal de terminal y taller solo a las vistas. El texto (S4 89–92) dice que la aplicación móvil tiene cuatro perfiles: conductor, torre, terminal y taller, y transportista. Se siguió al encargo. Para que coincidan, se puede unir también la torre y el taller a la app móvil, o cambiar el texto.
- **Concesiones por espacio:**
  - el ícono de Kafka salió del panel de integración y queda como dato bajo Event Hubs («Protocolo Kafka»), para respetar los 12 pt entre rótulos;
  - el panel «Borde y puerta» y la lista de servicios externos llevan el nombre a la derecha del ícono;
  - Delta Lake se nombra en el panel de datos pero no tiene ícono.

**`LogicaContextos`** (vertical, 9,00 pt).
Qué cambió:
- Cada contexto tiene su pregunta en una ficha.
- «pregunta» va sobre las dos flechas de Planificación y tráfico.
- Se agregaron en discontinua los cuatro eventos de `D3-diagrama2` (viaje asignado, llegada y salida, semirremolque acoplado y viaje cerrado), con la misma dirección.
- «Solo lectura» va sobre la flecha de la telemetría de fábrica.

Datos nuevos y su fuente: las preguntas, S4 132–136.

Diferencias con el texto: sigue pendiente la de la primera vuelta. La frase «Despacho puede bloquear un viaje sin conocer por dentro a Personas ni a Flota, porque les pregunta» (S4 144–145) debería decir «Planificación y tráfico puede bloquear un viaje sin conocer por dentro a Personas y cumplimiento ni a Flota y activos, porque les pregunta».

**`D3-diagrama11_patrones_resiliencia_despacho`** (vertical, 9,00 pt).
Qué cambió:
- Pasos numerados del 1 al 5: contrato de entrada, clave en caché, tres invariantes, persistencia y efectos en el bus.
- La caché alimenta las invariantes, con respaldo en el motor transaccional en discontinua.
- La rama de rechazo lleva la ficha «Error estructurado < 1 s» y vuelve al operador.
- Tiempos de espera: 10 s hacia la capa anticorrupción y el sistema contable, y 90 s en la emisión hacia la autoridad tributaria.
- Junto al cortacircuito, la ficha «Abre con más de la mitad de 10 fallidas · 30 s».
- Abajo, la barra de presupuesto proporcional hasta 2 s, con el tope de 30 s después de un corte.

Datos nuevos y su fuente:
- Parámetros del cortacircuito: S4 224–225.
- Tiempos de espera: S4 228–231.
- Presupuesto: S4 256–263.
- Respaldo en el motor: S4 259.
- Rechazo: S4 266.

Diferencias con el texto: la tabla `4-presupuesto` junta en una fila el contrato y la clave (10 ms), y la figura los separa en los pasos 1 y 2. No hace falta cambiarla.

**`LogicaIntegraciones`** (horizontal, 9,00 pt).
Qué cambió: el mapa se reordenó y cada conexión lleva su ficha de modo y volumen.

Datos nuevos y su fuente: la tabla `4-integraciones` (S4 328–334).

Diferencias con el texto:
- **Contradicción pendiente.** La frase «Ninguno de los sistemas del mapa se reemplaza» (S4 347) choca con el sistema de gestión de 2013, que se sustituye. Una redacción posible: «Salvo el sistema de gestión de 2013, que se sustituye función por función detrás de la capa anticorrupción, ninguno de los sistemas del mapa se reemplaza».
- **Nombre prohibido en el S4.** La tabla `4-integraciones` (S4 328) y el inventario (S4 549) dicen «Sistema contable de 2013». Debería decir «Sistema contable y de facturación».
- La Dirección del Trabajo no está en la tabla `4-integraciones`, así que su conexión va sin ficha.

**`D3-diagrama12_integracion_acl_erp2013`** (horizontal, 9,00 pt).
Qué cambió:
- Nueva franja «Retiro del sistema de 2013 función por función», con los meses 16, 21 y 24, la banda «Solo lectura» del 21 al 24 y cada función unida al contexto que la asume.
- Se mantiene la cadena de cuatro piezas, con el reconciliador vigilando la cola.
- Se agregó el regreso: «Confirmación traducida» del sistema contable a los contextos.

Datos nuevos y su fuente: S3 296–304 y S3 306–311.

Diferencias con el texto: el texto de la 4.1 no menciona esos meses. Habría que agregar una frase que remita al S3, por ejemplo: «La sustitución sigue el calendario del Subdocumento 3 (\verSeccion{sec:3-sistema2013}): la asignación, el control de viajes y la base de la liquidación pasan a la plataforma en el mes 16, las órdenes y las tarifas a clientes en el mes 21, y el sistema se retira en el mes 24».

**`D3-diagrama13_arquitectura_analitica_lakehouse_bi`** (horizontal, 9,00 pt).
Qué cambió:
- Ícono de bitácora entre el motor y la capa cruda, con la ficha «RT-05.05».
- Costo por viaje en dos columnas (flota propia y subcontratada), con un ícono por componente.
- Fichas de latencia de RT-05.29: posición 2 min, preliminar 24 h y emisiones mensual.
- La explotación suma la exportación en formatos abiertos y el envío programado (RT-05.28).
- Gerencia, finanzas y operaciones tienen íconos distintos.

Datos nuevos y su fuente:
- Bitácora: S4 429–430.
- Tabla `4-costo`: S4 452–461.
- Latencias: S4 474–478.
- RT-05.28: S4 497.

Diferencias con el texto:
- Las fichas abrevian la tabla `4-costo`. Por ejemplo, «Igual, si lo asume» resume «Igual, cuando el peaje lo asume la compañía», y «En la tarifa pactada» resume «Incluida en la tarifa pactada, no descomponible».
- La segunda versión del costo se llama «Definitiva», como en S4 466–468. Ojo: la misma frase usa «costo consolidado» para la de 24 h (S4 465), así que el texto llama «consolidado» a lo que la figura llama «preliminar». Conviene unificar.
- Los productos del repositorio y del autoservicio siguen pendientes en el T-11.

**`D3-diagrama2_arquitectura_tactica_ddd`** (vertical, 9,00 pt).
Qué cambió:
- Los tres contextos vacíos se llenaron con entidades que el texto nombra.
- Cada agregado raíz lleva una corona en vez de la palabra «raíz».
- Los eventos van en discontinua, como en `LogicaContextos`.

Origen de las entidades nuevas:

| Contexto | Entidad | Fuente |
|---|---|---|
| Planificación y tráfico | Orden de transporte | S3 256 y 794 |
| Planificación y tráfico | Asignación | S3 644 |
| Telemetría y geocercas | Posición | S3 650–651 y S4 474 |
| Telemetría y geocercas | Geocerca de punto de carga | S4 221–222 y T-12 RF-010 (154) |
| Liquidación y costeo | Costo del viaje | S4 444–449 y S3 653 |
| Liquidación y costeo | Liquidación del transportista | S3 653 y T-12 RF-019 (253) |

Decisiones que tomó el asistente y que debe validar la dupla 3:
- Viaje, con Sobreestadía y Gasto operacional, queda en Operación de fletes.
- Vigencia aparece como entidad propia en Flota y activos y en Personas y cumplimiento.
- Las seis entidades nuevas se marcan como «entidad», sin decidir si alguna es raíz de agregado.
- Quién publica y quién recibe cada evento: viaje asignado (Planificación → Operación), llegada y salida en un punto (Telemetría → Operación), semirremolque acoplado (Telemetría → Flota), consentimiento revocado (Personas → Telemetría), viaje cerrado y documento emitido (Operación → Liquidación) y liquidación aprobada (Liquidación → capa anticorrupción).

Diferencias con el texto: la leyenda (S4 511) dice «Agregados, entidades y servicios por contexto», y la figura no tiene servicios de dominio. Habría que cambiarla por «Agregados, entidades y objetos de valor por contexto, con los eventos de dominio entre contextos».

### Subdocumento 13

**`cartera`** (vertical, 9,00 pt).
Qué cambió:
- Es una versión reducida de `LogicaCapas`, con presentación, servicios, integración, borde y equipo a bordo.
- Los marcadores numerados van sobre los componentes que usa cada innovación.
- Los nombres completos van arriba, en dos columnas, cada uno con su ícono: documento con sello, actualización, semirremolque, apretón de manos y cama.

Datos nuevos y su fuente:
- Nombres: T-19 13, 33, 53, 73 y 93.
- Componentes por innovación: S13 21–30 y 38–39.

Diferencias con el texto: ninguna. El T-19 (33) tiene un marcador pendiente para reformular la innovación 2; si cambia su nombre, hay que cambiarlo aquí.

**`semirremolque`** (horizontal, 9,00 pt).
Qué cambió:
- El semirremolque acoplado al tractocamión, con el Bluetooth entre la baliza y el G26I.
- Una escena de portería con barrera y el Minew G1.
- Junto a la baliza, las fichas temperatura, puerta, acelerómetro, «44 refrigerados» y «210 + 21».
- En los servicios, las fichas que pidió el encargo.

Datos nuevos y su fuente:
- Sensores: S13 219–221.
- 44 refrigerados: S13 205.
- 210 + 21: S13 259.
- Kilómetros para el plan preventivo: S13 254–255.
- «Semirremolque que sale = asignado»: S13 231.

Diferencias con el texto:
- La baliza también mide humedad (S13 220), pero no está entre las tres fichas que pidió el encargo.
- Sigue pendiente lo de la primera vuelta: el texto habla de «tres servicios» y nombra dos contextos.

### Subdocumento 7

**`pert-etapa1` y `pert-etapa2`** (horizontales, 9,00 pt).
Qué cambió:
- Nombres, precedencias y tiempos salen del T-15, leídos al generar.
- Arriba hay un eje de meses, con rombos en los hitos.
- Cada nodo no crítico lleva la ficha «Holgura N», con la holgura total.
- Los abanicos que salen de A01 y llegan a A12 usan un bus vertical común.
- Las líneas que se cruzan llevan salto.

Diferencias con el texto:
- **Eje de meses.** Con nodos legibles a 10 pt el eje no puede ser proporcional: dos columnas arrancan en el día 0 y el 5. Cada columna marca entonces el mes en que empiezan sus actividades, a 20 días hábiles por mes: meses 1 a 12 en la red 1 y 12 a 21 en la red 2.
- **Abreviaturas.** El S7 no define ES, EF, LS ni LF; solo el T-15 (173–174). Habría que agregar al párrafo de la línea 453 del S7: «En cada nodo, ES y EF son el inicio y el término tempranos, y LS y LF el inicio y el término tardíos, en días hábiles desde el día 0».
- **Filas de la etapa 2.** Sigue la diferencia de la primera vuelta en la descripción de las filas (S7 471–473). Con los nombres del T-15, la fila inferior ya muestra A18, «Terceros y montaje restante».

Nombres cortos y su descripción en el T-15:

| Código | Nombre en el nodo | Descripción en el T-15 (línea) |
|---|---|---|
| A01 | Inicio del proyecto | Inicio del proyecto: plan de dirección aprobado y equipo constituido (179) |
| A02 | Levantamiento y línea base | Levantamiento de procesos en los cinco terminales, línea base de alcance y matriz de trazabilidad (180) |
| A03 | Cobertura móvil en terreno | Caracterización en terreno de la cobertura móvil de las rutas (181) |
| A04 | Factibilidad con proveedores | Verificación de factibilidad con los tres proveedores de posicionamiento y con los fabricantes… (182) |
| A05 | Arquitectura y seguridad | Arquitectura, plan de seguridad y modelo de datos (183) |
| A06 | Plan de adhesión de transportistas | Plan de adhesión de los 148 transportistas subcontratados… (184) |
| A07 | Infraestructura y ambientes | Infraestructura híbrida y ambientes DEV, QA, PREPROD y PROD con observabilidad (185) |
| A08 | Migración de las vigencias | Migración y verificación documental de las 6.000 vigencias de cuatro planillas (186) |
| A09 | Construcción de la Etapa 1 | Construcción de la Etapa 1 en ocho sprints… (187) |
| A10 | Integraciones y plataformas | Integraciones con el sistema de gestión de transporte de 2013, el sistema contable y las tres plataformas… (188) |
| A11 | Piloto de 10 y flota propia | Piloto de 10 camiones en el mes 6 y montaje a bordo de la flota propia… (189) |
| A12 | Certificación de la Etapa 1 | Pruebas integrales y certificación de la Etapa 1… (190) |
| A13 | Capacitación de conductores | Capacitación de conductores en los terminales y de la torre 24x7 (191) |
| A14 | Reserva de la Etapa 1 | Reserva de contingencia de cronograma de la Etapa 1 (192) |
| A15 | Marcha blanca de la Etapa 1 | Marcha blanca de la Etapa 1, meses 13 a 15… (193) |
| A16 | Transferencia tecnológica | Transferencia tecnológica y certificación del equipo de TI del mandante (194) |
| A17 | Diseño detallado de la Etapa 2 | Levantamiento y diseño detallado de la Etapa 2 (195) |
| A18 | Terceros y montaje restante | Integración de los terceros por su plataforma (meses 13 a 15) y montaje restante a bordo (meses 16 a 18) (196) |
| A19 | Paso a producción de la Etapa 1 | Paso a producción de la Etapa 1 y acta de cierre de la marcha blanca (197) |
| A20 | Construcción de la Etapa 2 | Construcción de la Etapa 2 en cinco sprints… (198) |
| A21 | Estabilización de la Etapa 1 | Estabilización posterior al paso a producción de la Etapa 1… (199) |
| A22 | Certificación de la Etapa 2 | Certificación de la Etapa 2 y cierre del desarrollo (200) |
| A23 | Reserva de la Etapa 2 | Reserva de contingencia de cronograma de la Etapa 2 (201) |
| A24 | Marcha blanca de la Etapa 2 | Marcha blanca de la Etapa 2 en convivencia con la Etapa 1… (202) |
| A25 | Paso a producción de la Etapa 2 | Paso a producción de la Etapa 2 y aceptación final del proyecto (203) |

**`edt`** (vertical, 9,00 pt) y **`gantt`** (horizontal, 9,00 pt), de la dupla 2.
Se rehicieron con los datos que el guion lee del TikZ del S7 (líneas 51–198 y 554–635).
- La EDT tiene los 13 elementos en dos columnas, con sus paquetes en fichas.
- La Gantt muestra los 56 meses con años y meses clave, la temporada de diciembre a abril en gris muy claro, las barras por elemento y los doce hitos rotulados H1 a H12. Los hitos se rotulan en orden de fecha según el T-15, así que H8 queda antes que H7.

Diferencias con el texto: la Gantt ya no tiene leyenda, así que el texto (S7 549–552) debe explicar los cuatro tipos de barra:
- gris muy claro de fondo: la temporada de fruta;
- barra gris: marcha blanca;
- barra oscura: paso a producción;
- barra discontinua: operación.

Las dos van en archivos aparte y no reemplazan el TikZ hasta que la dupla 2 lo decida.

## Las tres figuras propuestas

**`propuestas/racks-san-bernardo`** (vertical, 9,00 pt). Elevación frontal de los dos racks de 24 U, con las unidades numeradas.
- Sección: S4 4.3.1, en el párrafo del plano de la sala.
- Frase actual que la anunciaría: «El de servidores ocupa cerca de 12 unidades con los dos R360, las dos UPS y sus baterías externas, y el de comunicaciones cerca de 8 con los firewalls, los switches, los paneles de conexión y los equipos de los proveedores» (S4 1229–1231).
- Frase para agregar: «La \figref{4-racksfig} muestra la elevación de los dos racks, con las unidades que ocupa cada equipo y las que quedan libres».
- **Supuesto.** Solo el Dell R360 tiene su altura en las fuentes (1 U, T-11 157). El resto se supuso para sumar lo que dice el texto, y hay que confirmarlo con las fichas de los fabricantes:
  - UPS y batería, 2 U cada una;
  - bandeja de los FortiGate, switches, paneles y equipos de los proveedores, 1 U cada uno.

**`propuestas/instalacion-a-bordo`** (horizontal, 9,00 pt). Vista lateral del tractocamión con el semirremolque y dónde va cada pieza.
- Sección: S4 4.2.2, después de la figura del equipo a bordo.
- Frase actual: «La \figref{4-bordofig} muestra el equipo con sus periféricos» (S4 699).
- Frase para agregar: «La \figref{4-instalacionfig} ubica cada pieza en el tractocamión y en el semirremolque».
- Las ubicaciones salen de la columna de ubicación del T-11 (líneas 15, 45, 55 y 76) y del S13 (222). Las antenas en el techo tienen la misma observación que en `equipo-a-bordo`.

**`propuestas/documento-sin-cobertura`** (vertical, 9,00 pt). Arriba, la emisión anticipada desde la orden. Abajo, los seis pasos numerados en un punto sin cobertura.
- Sección: S4 4.1, «Convivencia con el sistema contable heredado», donde hoy hay un marcador para la dupla 3 que pide justamente este mecanismo (S4 377–380). También podría ir en la 3.4.2 del S3.
- Frase actual relacionada: «Por el mismo canal, cuando un punto de carga no tiene cobertura, el equipo envía los datos mínimos del documento de transporte y recibe el folio que emite el sistema contable» (S4 710–712).
- Frase para agregar: «La \figref{4-sincoberturafig} muestra los dos caminos: la emisión anticipada desde la orden y la emisión con los datos enviados por el enlace satelital».
- Fuente: S3 812–818.

## Datos que no estaban en las fuentes

Se dibujaron porque los pidió el encargo y quedan por confirmar:
- la ubicación de las antenas en el techo;
- la puerta de enlace de Iridium;
- la barrera de portería;
- las medidas de rack de 0,6 × 1,0 m;
- la tubería VESDA por el cielo;
- la batería del camión como fuente de alimentación;
- las alturas en U de los equipos, salvo el R360.

Quedaron fuera o como texto:
- el ícono de Delta Lake, que no tiene licencia abierta;
- el producto de caché que reemplaza a Azure Cache for Redis, pendiente de la dupla 3;
- los tamaños de AKS y de PostgreSQL.

Contradicciones que no se resolvieron:
- el T-11 pone el Iridium Edge en la cabina;
- los canales de la torre y del taller;
- «Sistema contable de 2013» en S4 328 y 549;
- «Ninguno de los sistemas del mapa se reemplaza» en S4 347;
- «preliminar» frente a «consolidado» para la versión de 24 h.
