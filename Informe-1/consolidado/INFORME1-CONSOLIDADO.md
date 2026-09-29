# Informe y Presentación 1 — Documento consolidado

**Proponente:** audIT · **Mandante:** Transportes Curimón S.A.
**Licitación N.º TFEP-01/2026 · Caso 10 Transporte de Carga**
Taller de Formulación de Proyectos Informáticos (ICI-5444) · Escuela de Informática · PUCV

> **Qué es este documento.** Consolida el trabajo de las cuatro duplas en las seis
> presentaciones que exige el enunciado del Informe 1. No reemplaza los subdocumentos: cada
> sección remite al archivo donde está el desarrollo completo. Incluye al final una **auditoría
> de consistencia** entre duplas con lo que hay que corregir antes de la entrega.
>
> **Regla de precios (Art. 50.2, FEP01 p.29, verificado textualmente):** «la Oferta Técnica no
> podrá contener información de precios, tarifas, valores unitarios ni cifra alguna que permita
> inferir el monto de la oferta económica. Su inclusión es causal de exclusión inmediata.» Las
> cifras en pesos que aparecen aquí son **del CLIENTE y provienen del caso**; ninguna es
> valorización de la oferta de audIT.

---

## 1 · Debe presentar la Empresa

**Fuente completa:** `equipo/D1/subdoc1-empresa.md` · **Formulario T-6** · Peso 4 %

**audIT** es una empresa de ingeniería de software, arquitectura de datos y ciberseguridad
industrial fundada en 2022, orientada a la continuidad operacional, la visibilidad telemática y
la trazabilidad analítica en organizaciones con operaciones distribuidas y conectividad
intermitente.

| | |
|---|---|
| **Misión** | Transformar operaciones críticas de campo en flujos de datos auditables, continuos y seguros |
| **Visión** | Ser el socio tecnológico de referencia en el Cono Sur para sistemas de misión crítica bajo arquitecturas resilientes *offline-first* |
| **Valores** | Rigor metodológico · seguridad por diseño (Zero Trust) · transparencia auditable · continuidad de servicio |
| **Casa matriz** | Viña del Mar · laboratorio de dispositivos IoT y embarcados en Santiago |

**Tres líneas de negocio:**

1. **Ingeniería IoT y sistemas de terreno.** Firmware industrial, telemetría vehicular
   multimarca (SAE J1939, rFMS, tacógrafos digitales) y el paquete embarcado *audIT EdgeHub* con
   almacenamiento local inalterable y sincronización tras desconexión prolongada.
2. **Plataformas de datos y analítica avanzada.** *audIT TelemetryCore*: ingestión masiva de
   eventos, motores de despacho algorítmico y tableros operacionales.
3. **Consultoría en arquitectura híbrida y ciberseguridad operacional.** Capas anticorrupción
   para convivencia con ERP heredados, OWASP SAMM y gobierno de datos bajo la Ley N.º 21.719.

**Capacidad de soporte en terreno.** Convenios con red técnica certificada con presencia
permanente en los cuatro nodos regionales del CLIENTE —Antofagasta, Talca, Los Ángeles y Puerto
Montt— con intervención in situ en menos de 4 horas sobre el corredor de 3.000 km. Da
cumplimiento a **RT-08.04** y **RT-21.16**.

---

## 2 · Debe presentar el Problema

**Fuente completa:** `equipo/D1/subdoc2-problema.md` · **T-7 subdoc. 2** · Peso 11 %

### El problema raíz

**La responsabilidad y el control no coinciden.** Curimón soporta el 100 % de la responsabilidad
sobre cargas, siniestros y fiscalizaciones, pero **el 60,4 % de su capacidad de transporte** (226
camiones de 374) y **el 56,8 % de sus operadores** (258 conductores externos de 454) no están bajo
su tuición directa. Bajo el régimen de subcontratación de la Ley N.º 20.123, esa disociación es un
riesgo latente sin cuantificar.

### La dimensión física

| Magnitud | Valor |
|---|---|
| Viajes al año | 96.000 |
| Kilómetros al año | 41.000.000 · **26 % en vacío** |
| Toneladas al año | 2.400.000 |
| Flota | 374 tractocamiones · 210 semirremolques |
| Corredor | 3.000 km entre Antofagasta y Puerto Montt · ≈1.900 cruces por Los Libertadores |
| Documentos de transporte al año | ≈128.000 |
| Clientes | 84 activos; **8 concentran el 71 % de la facturación** |

### La fragilidad financiera

Facturación anual de **$78.000 millones** con margen operacional de **9 %**. Tres de los ocho
contratos principales operan bajo costo y representan el **31 % del ingreso**; el peor lleva
**cuatro años a −14 %**, subsidiado por rutas rentables bajo prorrateo ciego por ingreso.

### Los tres disparadores de 2026

1. **14 de febrero, 04:40 h.** Accidente en el km 312 de la Ruta 5 Sur. El conductor
   subcontratado había manejado el día anterior para otra empresa. Los registros de Curimón
   estaban impecables: mostraban 11 horas sin conducir **para ella**. Suspensión de contratos por
   seis semanas.
2. **Abril.** Fiscalización inmoviliza 14 horas un tractocamión con sustancias peligrosas por un
   curso vencido tres semanas antes, que vivía en una planilla actualizada «cuando alguien se
   acuerda». Colapso del control documental bajo el D.S. N.º 298.
3. **Junio.** El primer costeo por ruta destapa los subsidios cruzados masivos.

### El colapso de la gobernanza de datos

- **≈6.000 fechas de vencimiento vivas** en cuatro planillas aisladas sin integridad referencial.
- **Cero descargas históricas de tacógrafo digital.**
- **61 tractocamiones** con telemetría CANbus de fábrica **inactiva**.
- **34 camiones sin ningún dispositivo GPS**, monitoreados por teléfono; los **340 restantes** en
  **tres plataformas incompatibles**, una de las cuales no permite exportar.
- Espera media de 3 h 10 min en punto de carga, con **71 % de los cobros objetados**.

### La amenaza de 2029

El cliente exportador mayor —**19 % de los ingresos**— condicionó la renovación a cuatro
exigencias: documento electrónico de transporte integrado punta a punta; posición de la carga en
tiempo real; emisiones por tonelada-kilómetro verificadas por un tercero; y **acreditación del
cumplimiento de jornada en cada viaje, incluidos los camiones subcontratados**. La cuarta es el
problema central del caso y no tiene solución evidente.

### La advertencia que gobierna el diseño

> «El sesenta por ciento de nuestra capacidad no nos pertenece y esas personas no son nuestros
> trabajadores. Cualquier solución que suponga que podemos darles una orden va a fracasar el
> primer día.» — Gerente general, acta de directorio.

---

## 3 · Debe presentar el Esquema de Solución

**Fuente completa:** `equipo/D2/formulario-t12-preliminar-d2.md` y `catalogo-requisitos-d2.md`
**T-12** · Peso 21 % (junto con el alcance)

### Catálogo de requisitos

**42 requisitos trazables al origen:** `RF-001` a `RF-028` funcionales y `RNF-001` a `RNF-014` no
funcionales. Cada uno con descripción, componente que lo satisface y sección de la propuesta.

> **Advertencia de forma que vale puntaje.** El numeral 1.5 de las bases establece que declarar
> «cumple» sin individualizar el componente **equivale a no declarar**. Por eso la matriz usa hoy
> el estado interno *pendiente de verificación* en las 42 filas: ni el compromiso de atender una
> exigencia ni un componente propuesto justifican declarar cumplimiento antes de validarlo.

### Los requisitos que definen la solución

| ID | Qué exige | Por qué es el núcleo |
|---|---|---|
| RF-001 | Validación bloqueante de jornada, habilitaciones y aptitud antes de asignar | Criterio 1 del caso: ningún camión sale sin poder salir |
| RF-003 | Jornada previa del conductor **externo** disponible al asignar | La decisión 1 del numeral 16.1, la más importante del caso |
| RF-008 | Vista única de posición de los 374 camiones | Unifica tres plataformas incompatibles |
| RF-009 | Registro local de 72 h y sincronización posterior | La operación no puede depender de la cobertura móvil |
| RF-014 | DET conforme **antes** del movimiento, incluso sin cobertura | «La emisión diferida no basta» |
| RF-022 | Consentimiento granular, revocable y auditable | Criterio 29: quien entrega el dato conserva el control |
| RF-026 | Adhesión de transportistas gestionada y **medible** | Criterio 27: sin plan de adhesión, la arquitectura es un dibujo |
| RF-027 | Alerta de jornada según **lugar seguro alcanzable** | Criterio 28: la alerta que llega donde no se puede parar no sirve |
| RNF-001 | Cero interacción del conductor durante la marcha | Restricción 1, no negociable |

### La decisión estructurante

**Decisión 1 · jornada del conductor externo** (`equipo/D2/decision-01-jornada-externa.md`).
El encuadre acordado: Curimón no necesita saber dónde estuvo el conductor ni para quién manejó.
Necesita **un veredicto** —apto / no apto / apto hasta las HH:MM— y poder acreditar después que lo
verificó. Es un dato derivado, no un historial.

El sujeto obligado se traslada del conductor **al dueño del camión**, que es quien sí tiene
contrato comercial con Curimón. Es lo único que la restricción 2 permite.

---

## 4 · Debe presentar el Alcance de la Solución

**Fuente completa:** `equipo/D2/alcance-etapas-d2.md`

### Criterio de partición

**Etapa 1 controla los riesgos que pueden causar un despacho ilegal, pérdida probatoria,
duplicación tributaria o tratamiento indebido de datos**, y valida las dependencias técnicas y
contractuales antes de un despliegue masivo. Etapa 2 escala, optimiza y consolida la adopción.

### Etapa 1 — capacidades

| Capacidad | Resultado comprometido |
|---|---|
| Despacho seguro | Validación de jornada, vigencias, aptitud y **nivel de evidencia** antes de asignar |
| Evidencia y documentos | Registro maestro, trazabilidad, integridad; pilotos de carga peligrosa y tacógrafo |
| Posición y operación offline | Vista única piloto, geocercas y almacenamiento mínimo de 72 h |
| Viaje y facturación | Documento conforme antes del movimiento aun sin cobertura, con emisor contable único |
| Costos y liquidación | Costo consolidado en 24 h con faltantes explícitos; liquidación por excepción |
| Base de emisiones | Fuentes, línea base y metodología declarada — **no** cálculo productivo completo |
| Portales y consentimiento | Portal mínimo, segregación, adhesión y permisos granulares |
| Flota y mantenimiento | Pilotos de kilometraje real y alerta de lugar seguro |
| Implantación y operación | Pilotos por familia, RACI, despliegue progresivo |

### Entradas obligatorias de Etapa 1

Padrones de 374 tractocamiones, 210 semirremolques, 454 conductores, 148 transportistas y 84
clientes; las cuatro planillas de vigencias con sus respaldos.

### Lo que queda fuera del alcance y hay que decir en voz alta

- No se reemplaza el sistema contable ni la emisión de documentos tributarios.
- No se interviene la electrónica de fábrica del vehículo.
- **No se reemplazan las plataformas de posicionamiento de terceros**, aunque sí se unifica la
  vista y se especifica qué se requeriría para homologarlas (Cap. 11, FEP03 p.24).
- No se instala equipamiento en los puntos de carga y descarga de clientes.
- **El hardware lo adquiere el CLIENTE**; audIT especifica qué comprar, cuánto y con qué
  características.

---

## 5 · Debe presentar la Arquitectura Lógica y Física

### 5.A · Arquitectura lógica (subdoc. 4.1 · D3 · 16 %)

**Fuente completa:** `equipo/D3/subdoc4.1-arquitectura-logica.md`

Las **ocho capas del numeral 2.1 transversal** (FEP02 p.6) son de existencia obligatoria;
RT-02.01 exige el diagrama identificando cada capa, sus componentes y las interfaces.

| Capa | Contenido en esta solución |
|---|---|
| Presentación | Portal web, app móvil operable con guantes, terminales de torre y taller |
| Borde y exposición | Front Door / WAF gestionado, anti-DDoS L3-L7, terminación TLS 1.3 |
| Puerta de enlace | API Management: cuotas, límites de tasa, versionado semántico, validación de esquema |
| **Servicios de negocio** | Microservicios por límites de contexto: Despacho, Flota, Jornada, Documental, Liquidaciones, Contratos |
| Integración y eventos | Event Hubs para telemetría masiva, Service Bus transaccional, colas de mensajes fallidos |
| Datos | Políglota: relacional transaccional, series de tiempo, objeto documental, lakehouse analítico |
| **Seguridad** (transversal) | Key Vault, Entra ID (OAuth 2.1 / OIDC), auditoría criptográfica |
| **Observabilidad** (transversal) | OpenTelemetry sin puntos ciegos en nube ni terminales |

**Regla del propio numeral 2.1:** ninguna interfaz accede directamente a la base de datos.

**Piezas que definen el diseño lógico:**

- **Capa anticorrupción (ACL).** Sustituye los módulos operativos del sistema de 2013 —tráfico,
  despacho, tarifas, liquidación— y encapsula el ERP contable, que se conserva como **único emisor
  de documentos tributarios**. Fundamento: **RT-05.20** (obligatorio); RT-02.14 lo valora además
  como patrón de arquitectura evolutiva (deseable).
- **Servicios sin estado** con idempotencia estricta: claves UUIDv4 y ventana de deduplicación de
  7 días, dimensionada para tolerar los cortes prolongados en ruta.
- **Patrones de resiliencia obligatorios (RT-02.08):** *time-outs* explícitos —prohibida toda
  llamada remota sin límite declarado—, cortacircuitos, mamparos y reintento exponencial con
  variación aleatoria.
- **Separación OLTP / OLAP** por réplicas de lectura y lakehouse, para que la analítica no degrade
  la operación.

### 5.B · Arquitectura física (subdoc. 4.2 · D4 · 16 %)

**Fuente completa:** `equipo/D4/D4-MATERIAL-INFORME1.md`

**Principio rector:** el registro operacional de esta empresa no vive en un servidor, vive en 374
camiones; la nube es donde se consolida. El borde no es una víctima de la caída del enlace: es
parte del esquema de continuidad.

**Cumplimiento del Artículo 16° — híbrido en tres planos simultáneos**, no por conveniencia:

| Plano | Contenido | Por qué no puede estar en otro lado |
|---|---|---|
| **Nube** | Núcleo transaccional, analítica, portales, integración | Elasticidad a 430 camiones (RT-02.12) y peak de reconexión masiva |
| **On-premise de sitio** | Continuidad de la torre 24×7 y terminación de enlaces en San Bernardo; gabinetes en los 4 terminales regionales | RT-06.01 del Caso exige gabinete por terminal dimensionado para RT-03.10 |
| **On-premise distribuido** | 374 dispositivos a bordo | La operación no puede depender de la cobertura móvil (restricción 4) |

**El dispositivo a bordo es infraestructura, no accesorio.** RT-06.01 del Caso (FEP03 p.32) lo
ordena literalmente: «debe tratarse como un componente on-premise distribuido en 374 unidades, con
su propio ciclo de vida, su mecanismo de actualización remota, su gestión de seguridad y su plan
de reposición».

**Tipología de recintos declarada** (numeral 6.1 transversal exige declararla y justificarla, y
penaliza igual sobredimensionar que subdimensionar):

| Sitio | Tipología | Justificación |
|---|---|---|
| San Bernardo, 26 m² | **Sala técnica secundaria o de sitio** | El núcleo está en nube; aquí queda continuidad de la torre, terminación de enlaces y custodia de medios |
| 4 terminales regionales | **Gabinete o borde operacional** | RT-06.01 del Caso, texto expreso |
| 374 camiones | **On-premise distribuido** | RT-06.01 del Caso, texto expreso |

**Continuidad: dos ejes distintos, no uno.**

| Eje | Primario | Secundario | Fundamento |
|---|---|---|---|
| Recuperación ante desastres | Azure Chile Central, multizona | **Segunda región Azure** | RT-07.02 exige distancia suficiente para no compartir el evento de fuerza mayor; **Art. 16.3 obliga a declarar región primaria y secundaria** |
| Continuidad operacional | Azure | **San Bernardo** | RT-21.06: asignar viaje, emitir DET y recibir pánico son severidad máxima |

**Dimensionamiento derivado** (Cap. 14.2 exige estimarlo y advierte que «valores sin derivación se
evaluará como dimensionamiento no realizado»):

| Magnitud | Valor | Supuestos |
|---|---|---|
| Volumen en buffer tras 72 h | ≈0,8 MB sin imágenes · ≈3,2 MB con evidencia fotográfica | 55 km/h, 64 B por posición, 40 KB por DET, 300 KB por foto |
| **Especificación de almacenamiento** | **≥ 8 GB no volátil** | Cubre las 72 h de RT-03.10 **y los 12 días** de cierre de Los Libertadores (RT-10.05) |
| Datos móviles por camión | 13–16 MB/mes | Muestreo 30 s marcha / 5 min detenido |
| Datos móviles de la flota | ≈5,6 GB/mes | 374 unidades |

**El hallazgo económico:** el costo recurrente no está dominado por el tráfico de datos sino por
los **cargos fijos por unidad** —SIM, suscripción de plataforma, satelital y por OEM—, que escalan
con las 374 y luego con las 430.

**Conectividad por capas:**

- **Capa 0 · todas las unidades intervenidas:** almacenamiento local. RT-03.10 está escrito sobre
  la cobertura móvil, así que **el satélite no releva de este requisito**; además el enlace de
  ráfaga corta no transporta documentos ni evidencia detallada.
- **Capa 1 · todas las unidades intervenidas:** celular como portador primario.
- **Capa 2 · subconjunto acotado por riesgo:** satelital de ráfaga corta. **La población no es
  estimable hoy**: RT-03.24 del Caso prohíbe suponer la cobertura y exige medirla en terreno.
- **Descartada:** banda ancha satelital para toda la flota. Va al ADR (RT-02.04).

---

## 6 · Debe presentar potenciales Innovaciones

**Artículo 28°: cinco innovaciones, una por cada tipo obligatorio, sin repetir tipo.** El T-22
advierte que «en ningún caso puede presentarse sólo el título»: cada una se desarrolla en idea,
tecnología, alcance, forma de implementación y resultados esperados, con los siete elementos del
Artículo 29° en el Formulario T-19.

| Tipo | Categoría | Dupla | Terreno |
|---|---|---|---|
| **1** | Producto o servicio | D2 | Portal del transportista con viajes y liquidación en curso |
| **2** | Proceso | **D4** | Despliegue camión por camión con ventana de 6 días; actualización remota del parque |
| **3** | Tecnológica / arquitectura | **D3** | Operación desconectada 72 h y unificación de las tres plataformas GPS |
| **4** | Modelo de negocio o contratación | **D2** | Comodato del dispositivo, ventana de consentimiento en firmware, incentivos por adhesión |
| **5** | UX / sostenibilidad / impacto social | **D1** | Alerta de jornada con lugar seguro alcanzable, interfaz sin interacción en marcha |

> ✔ **Reparto zanjado el 6 de septiembre de 2026.** Los cinco tipos tienen dueño único y ninguno se
> repite, conforme al Artículo 28.1. Ver §7.1.

### Innovación tipo 3 — D3 · Operación desconectada 72 h y unificación GPS

- **Problema:** 41 millones de km al año con tramos de más de 80 km sin cobertura; 34 camiones sin
  GPS y 340 en tres plataformas incompatibles, una sin exportación por API.
- **Tecnología:** arquitectura *edge-to-cloud* con *store-and-forward* tolerante a partición de
  red; almacenamiento local cifrado; capa de ingestión telemática unificada; emisión de DET en
  sombra con folios CAF pre-asignados.
- **Madurez:** TRL 8/9.
- **Indicador:** 100 % de eventos recuperados tras 72 h sin pérdida; 100 % de la flota en una
  única torre; sincronización bajo el umbral de 20 min del Cap. 15.

### Innovación tipo 2 — D4 · Despliegue sin detener la flota

- **Problema:** un camión detenido no produce (restricción 10); pasa por terminal cada 6 días y
  **el 22 % de la flota subcontratada pasa menos de una vez al mes**; la flota rueda 24×7×365 sin
  ventana de detención, con congelamientos de diciembre a abril, Semana Santa, Fiestas Patrias y
  los nueve días del cierre de liquidaciones (RT-10.05).
- **Idea:** convertir el paso fortuito por terminal en **ventana de intervención planificada y
  acotada**, mediante preconfiguración total del dispositivo antes de que el camión llegue —el
  numeral 8.4 exige stock de reemplazo con configuración precargada—, de modo que la intervención
  física sea *sustituir y salir* y todo el ciclo de vida restante ocurra por aire.
- **Indicador:** unidades intervenidas por mes y tiempo de inmovilización por unidad.

---

## 7 · Auditoría de consistencia entre duplas

Verificado con `tools/buscar.py` contra las tres bases. **Esto es lo que hay que corregir antes de
la entrega.**

### 7.1 ✔ Reparto de innovaciones resuelto

El conflicto entre `equipo/asignacion-duplas.md`, que asignaba a D2 los tipos 1 y 5 y a D1 el 4, y
el plan de trabajo de D2, que asignaba los tipos 1 y 4, quedó zanjado por el equipo el 6 de
septiembre de 2026. El archivo de asignación fue corregido.

| Tipo | Dupla |
|---|---|
| 1 · Producto o servicio | **D2** |
| 2 · Proceso | **D4** |
| 3 · Tecnológica o de arquitectura | **D3** |
| 4 · Modelo de negocio o contratación | **D2** |
| 5 · Experiencia de usuario, sostenibilidad o impacto social | **D1** |

Los cinco tipos quedan cubiertos sin repetición, conforme al Artículo 28.1. Las fichas tipo 1 y
tipo 4 están desarrolladas con los siete elementos del Artículo 29°. **Las fichas tipo 2, 3 y 5
conservan cuatro elementos**, y el Artículo 29° advierte que la omisión de cualquiera reduce la
innovación a un enunciado. Como las cinco se entregan en un solo PDF, ese riesgo afecta al
subdocumento 13 completo y no solo a la dupla responsable.

→ **Acción: resolverlo hoy y actualizar `asignacion-duplas.md` para que quede una sola fuente.**

### 7.2 Errores puntuales detectados en `Para_D4.md`

| Punto | Dice | Debe decir |
|---|---|---|
| Código del buffer | «las 72 h de desconexión (**RT-03.13**)» | Las 72 h son **RT-03.10**. RT-03.13 es la declaración de funciones NO disponibles sin conexión |
| Wi-Fi de descarga | «Wi-Fi en los **5 terminales regionales**» | Son **4 regionales + San Bernardo** = 5 terminales en total (FEP03 Cap. 3) |
| Formato | «≥8 GB≥8 GB» (dos veces) y «374 tractocamiones ×× ~41M km» | Duplicación de marcado |
| Notación del cálculo | «374 tractocamiones × ~41M km/año» | Los 41M km son el **total de la flota**, no por camión. El resultado (745.000 h) es correcto; la fórmula, no |
| Pings anuales | «89,4 millones de pings/año» | Cuenta **sólo las horas de marcha**. Sumando el muestreo en detención (5 min) son ≈120 millones |
| Concurrencia | «300 a 350 sesiones pico» | Sus propios componentes suman **230 a 380** (50-80 + 100-150 + 30-50 + 50-100). El rango declarado no cuadra con su desglose |

### 7.3 Lo que D3 aceptó y quedó cerrado

- **Buffer ≥8 GB** en lugar de «120 horas», absorbiendo los 12 días de Los Libertadores. ✔
- **Partición real de la flota:** 148 propias + ~192 terceros con GPS + 34 sin GPS. ✔
- **App móvil como canal voluntario e incentivado**, no como mecanismo del que dependa la
  trazabilidad (restricciones 1 y 2, RT-12.11). ✔
- **Capa anticorrupción anclada a RT-05.20** (obligatorio) con RT-02.14 como deseable. ✔

### 7.4 Supuestos de D3 que no están en las bases y deben declararse

Verificado por búsqueda: **no aparecen en ninguno de los tres documentos**.

- Precisión de geocerca de **±15 m**.
- Las **120 horas** de retención del buffer (ya retiradas, pero siguen en `plan-de-trabajo.md`).
- **Res. Ex. N.º 107/2014 del SII** sobre folios CAF de contingencia: sin verificar.
- Latencia de sincronización «< 15 min»: más estricta que el ≤20 min del Cap. 15. Conviene
  redactarlo como «se supera el umbral exigido», no como un número propio sin origen.

### 7.5 Cifras en pesos — revisión bajo el Art. 50.2

`subdoc2-problema.md` contiene cifras en pesos **del CLIENTE**: $78.000 millones de facturación,
$7.020 M de margen, $24.180 M de contratos bajo costo, $29.640 M de pagos a terceros, $55.380 M de
concentración comercial y $14.820 M del cliente del 19 %.

**Criterio aplicado:** el Art. 50.2 prohíbe «precios, tarifas, valores unitarios o cifra alguna que
permita **inferir el monto de la oferta económica**». Ninguna de estas cifras describe la oferta de
audIT; describen la situación del mandante y varias están en el propio caso. **Se consideran
admisibles**, con dos precauciones: que ninguna se presente junto a un componente de la solución de
forma que sugiera su costo, y que las derivadas ($7.020 M, $24.180 M, $29.640 M, $55.380 M,
$14.820 M) se identifiquen como cálculo propio sobre el 9 %, el 31 % y el 71 % que entrega el caso.

### 7.6 Coherencia técnica confirmada entre D3 y D4

| Punto | D3 | D4 | Estado |
|---|---|---|---|
| Proveedor de nube | Azure (Front Door, APIM, AKS, Event Hubs, Service Bus, Key Vault, Entra ID, Monitor) | Azure Chile Central, 3 zonas | ✔ alineado |
| Frecuencia de muestreo | 30 s marcha / 5 min detenido | Idéntico (escenario B) | ✔ alineado |
| Buffer a bordo | ≥8 GB flash industrial con *wear-leveling* | ≥8 GB no volátil | ✔ alineado |
| Ocho capas | Numeral 2.1 completo | Matriz capa → emplazamiento | ✔ alineado |
| Retención por dominio | 10a / 6a / 5a / vig.+5a / 3a / 2a en línea | Misma tabla, RT-05.10 | ✔ alineado |
| RAID | Propone RAID-1 | RT-03.14 exige **justificarlo frente a alternativas**; es entregable T-11 de D4 | ⚠ lo redacta D4 |

---

## 8 · Lo que falta para cerrar el Informe 1

| # | Pendiente | Dueño | Bloquea |
|---|---|---|---|
| 1 | Completar las fichas T-19 tipo 2, 3 y 5 con los siete elementos del Artículo 29° | D3, D4 y D1 | 17 % del informe |
| 3 | Tabla de emplazamiento T-11 con los 19 componentes del Eje 5 de D3 | D4 | Art. 16.2 |
| 4 | Justificación de RAID frente a alternativas (RT-03.14) | D4 | Subdoc. 4.2 |
| 5 | Corregir los seis puntos de §7.2 en `Para_D4.md` | D3 | Consistencia |
| 6 | Declarar los supuestos de §7.4 o eliminarlos | D3 | Trazabilidad |
| 7 | Verificar las referencias normativas sin comprobar | D3 + D4 | Citas APA |
| 8 | Foliación correlativa, media firma y referencias APA 7.ª | D1 (custodia de formalidad) | **Art. 40.1: la falta de foliación produce exclusión automática** |
