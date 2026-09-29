# SUBDOCUMENTO 13: CARTERA DE INNOVACIONES
## FORMULARIO T-19 · FICHA DE INNOVACIÓN TIPO 3: TECNOLÓGICA / ARQUITECTURA

**Licitación Pública TFEP-01/2026 · Caso 10: Transportes Curimón S.A.**  
**Dupla Responsable:** D3 (Marcel y Martín) · **Área:** Arquitectura de Software, Datos y Telecomunicaciones  
**Estándares y Marcos de Cumplimiento:** Artículos 28° y 29° (FEP01 · p.19); Formulario T-19 (FEP01 · p.64); Formulario T-22 (FEP01 · p.68); RT-26.01 a RT-26.08 (FEP02 · p.44); RT-03.10 a RT-03.14 (FEP02 · p.8-9); RT-10.05 (FEP03 · p.32); Restricciones 1, 2, 3, 4 y 9; Decisiones D-02, D-04, D-09, D-11, D-20 y D-26; Formato de Citación APA 7.ª edición.

---

### FICHA TÉCNICA OFICIAL FORMULARIO T-19

| Campo Oficial (FEP01 · p.64) | Contenido de la Propuesta Técnica audIT |
| :--- | :--- |
| **Tipo de Innovación (1 a 5)** | **Tipo 3: Tecnológica / Arquitectura** (Artículo 28°, FEP01 · p.19) |
| **Nombre de la Innovación** | **Arquitectura Edge-to-Cloud con Store-and-Forward Determinista ($\ge 8\text{ GB}$) y Capa de Ingestión Telemática Unificada para Flota Heterogénea** |
| **Subdocumento Asociado** | Subdocumento 13 (con trazabilidad directa a Subdoc. 4.1, 4.2 y 5) |
| **Dupla Responsable** | Dupla 3 (Marcel y Martín), en coordinación técnica con Dupla 4 (Alonso e Ignacio V) |
| **Nivel de Madurez (TRL)** | **TRL 8/9** (Tecnología probada en entorno operacional real / Sistema comercialmente desplegado) |

---

### 1. Problema u Oportunidad Concreta del Caso y Evidencia Cuantitativa (Art. 29.1)

#### 1.1 Dimensión del Desafío Operacional y Geográfico
Transportes Curimón S.A. recorre anualmente **$\approx 41.000.000\text{ de kilómetros}$** a través de la geografía de Chile y rutas internacionales hacia Argentina. La operación enfrenta dos realidades críticas de desconexión:
1. **Sombras Telemáticas en Rutas Principales:** En la Ruta 5 Norte (desierto de Atacama) y tramos cordilleranos existen zonas de sombra celular continuas que superan los **80 kilómetros de longitud** (equivalentes a 1,5 a 2 horas de marcha sin conectividad móvil).
2. **Aislamiento Extremo en Paso Fronterizo Los Libertadores:** Conforme a **RT-10.05 (FEP03 · p.32)** y el numeral 13.2 (p.27), los camiones de Curimón realizan aproximadamente **1.900 cruces anuales** por el Paso Los Libertadores. Durante la temporada invernal, las nevadas provocan cierres fronterizos de **hasta 12 días continuos (288 horas)**, dejando a decenas de unidades varadas en la alta cordillera sin enlace telemático terrestre confiable.

#### 1.2 Fragmentación Telemática de la Flota (374 Tractocamiones)
El parque tractivo de Curimón presenta una profunda heterogeneidad técnica y contractual ([Capítulo 5, FEP03 · p.12](file:///home/axeler8/Escritorio/audIT/texto/FEP03_26_Bases_Tecnicas_TFEP_01_2026_3.md#L160-L190)):
* **148 tractocamiones propios:** Cuentan con equipos telemáticos antiguos con fallas recurrentes de reporte. De ellos, 61 unidades poseen puerto CANbus/FMS SAE J1939 inactivo de fábrica (Consulta N.° 14).
* **~192 tractocamiones de terceros con GPS:** Pertenecientes a 148 pequeños y medianos transportistas, equipados con dispositivos de dos proveedores comerciales distintos contratados privadamente por los dueños, cuyos accesos se limitan a portales web aislados sin integración API unificada.
* **34 tractocamiones de terceros sin GPS:** Unidades completamente ciegas que operan sin ningún hardware de rastreo.

#### 1.3 Impacto en el Negocio de Curimón
La pérdida de visibilidad y la fragmentación provocan:
* Pérdida sistemática de trazas de viaje, impidiendo respaldar el cobro de sobreestadías en plantas de clientes (\$340M facturados al año con un **71 % objetado** por falta de sellos de tiempo continuos).
* Imposibilidad de fiscalizar en ruta el descanso efectivo y las horas de conducción del **Art. 25 bis del Código del Trabajo** en las 288 horas de aislamiento fronterizo.
* Infracción tributaria en puntos de carga remotos (faenas forestales o mineras sin red celular), donde la ley chilena exige portar el Documento Electrónico de Transporte (DET / Guía de Despacho) timbrado **antes de mover la carga** (RF-014, Criterio 14, Res. Ex. SII N.° 107/2014).

---

### 2. Tecnología y Modelo Arquitectónico que la Sustenta (Art. 29.2)

La innovación abandona el paradigma clásico de "rastreador GPS simple dependiente de señal móvil" e implementa una **Arquitectura Híbrida Edge-to-Cloud con Almacenamiento Local Robusto y Pipeline de Ingestión Elástica**:

![Figura 4: Flujo Telemático, Búfer Local Resiliente y Despacho en Terreno](./diagramas/diagrama4_eventos_telemetria.png)

#### 2.1 Almacenamiento no Volátil en Cabina ($\ge 8\text{ GB}$ Flash Industrial con *Wear-Leveling*)
* **Hardware Especializado (RT-08.11):** En las 148 unidades propias y terceros adheridos, el dispositivo embarcado incorpora memoria flash eMMC/SD industrial de **$\ge 8\text{ GB}$**, diseñada con algoritmos de nivelación de desgaste (*wear-leveling*) para soportar vibraciones severas, polvo y choques térmicos de $-20^\circ\text{C}$ a $+70^\circ\text{C}$.
* **Motor Embebido SQLite en Modo WAL:** La base de datos local gestiona escrituras atómicas en modo *Write-Ahead Logging* (WAL). Los eventos de telemetría, posiciones GPS muestreadas cada 30 segundos, muestras CANbus/FMS por minuto y registros de jornada se serializan en formato binario ultracompacto **Protocol Buffers (Protobuf)**, requiriendo menos de 10 MB para 72 horas completas.
* **Capacidad Real de Autonomía:** Los 8 GB permiten almacenar **meses continuos de trazas de telemetría y documentos en disco**, absorbiendo sin ninguna degradación ni pérdida de paquetes los **12 días continuos (288 horas)** de aislamiento en Los Libertadores (RT-10.05).

#### 2.2 Capa de Ingestión Telemática Unificada para Flota Heterogénea
Para resolver la fragmentación de las 3 plataformas comerciales sin infringir la **Restricción N.° 3** ("No intervenir equipamiento de terceros sin acuerdo contractual") ni la **Restricción N.° 2** (no imponer obligaciones laborales a conductores subcontratados):
1. **Flota Propia (148 unidades):** Transmisión directa MQTT v5.0 / TLS 1.3 desde el dispositivo a bordo hacia el Broker Kafka/Event Hubs de audIT, complementada con lectura inductiva *contactless* de CANbus/FMS (Consulta N.° 14).
2. **Terceros con GPS (~192 unidades):** Conectores adaptadores en la nube (*Adapters/Webhooks*) que ingieren los datos telemáticos vía API de los dos proveedores de los transportistas, normalizando la carga útil al esquema unificado del modelo de dominio audIT sin tocar físicamente los camiones (Decisión D-02 y Cap. 11).
3. **Terceros sin GPS (34 unidades):** Plan de adhesión voluntaria con subsidio de kit telemático financiado por el proyecto (Decisión D-25) y portal web/móvil para registro previo de viajes.
4. **App Móvil del Conductor (Canal Voluntario e Incentivado - RT-17.01):** Opera como interfaz de consulta de liquidaciones, detalle de fletes y carga opcional de comprobantes de entrega (PoD) para acelerar el pago. **No se impone como mecanismo bloqueante de rastreo en ruta** (Restricciones 1 y 2; RT-12.11).

#### 2.3 Emisión Tributaria Offline de DET antes del Rodado (RF-014 / Consulta Oficial N.° 15)
Para cumplir con la legislación del SII y la Decisión D-09 ratificada por D2:
* El dispositivo en cabina almacena en memoria criptográfica protegida un stock pre-asignado de folios CAF (*Código de Autorización de Folios*) y certificado digital del contribuyente.
* En zonas sin señal (faenas remotas), el sistema emite y firma localmente el XML timbrado con Timbre Electrónico DTE (TED) y genera la representación gráfica PDF/QR en cabina **antes de iniciar el movimiento**.
* Al restablecerse el enlace celular, se ejecuta una sincronización asíncrona idempotente con el ERP contable 2013 en San Bernardo y el SII, garantizando emisor centralizado y correlación unívoca de folios sin riesgo de multas de tránsito.

---

### 3. Nivel de Madurez Tecnológica (TRL) y Citas en Norma APA 7.ª Edición (Art. 29.3 / RT-26.03)

La solución se sustenta en componentes comerciales y arquitecturas de referencia con madurez probada en entornos operacionales reales de transporte y defensa:

$$\text{Nivel de Madurez: } \mathbf{TRL \; 8/9} \quad (\text{ISO 16290:2013 / Horizon Europe Standard})$$

#### Referencias Bibliográficas Oficiales (Norma APA 7.ª Edición):

* **Kleppmann, M.** (2017). *Designing Data-Intensive Applications: The Big Ideas Behind Reliable, Scalable, and Maintainable Systems*. O'Reilly Media. *(Fundamentación de arquitecturas desconectadas, consistencia eventual, replicación multi-líder y algoritmos de sincronización de datos en borde)*.
* **OASIS Standard.** (2019). *MQTT Version 5.0*. OASIS Open. https://docs.oasis-open.org/mqtt/mqtt/v5.0/mqtt-v5.0.html. *(Estándar internacional de mensajería liviana pub/sub para telemetría telemática con QoS 1 garantizado y soporte a redes móviles inestables)*.
* **Open Container Initiative.** (2021). *OCI Image and Runtime Specifications v1.0*. Linux Foundation. https://opencontainers.org/ *(Estándar de empaquetamiento y ejecución de microservicios sin estado para despliegues elásticos en la nube)*.
* **SAE International.** (2020). *Surface Vehicle Recommended Practice: Serial Control and Communications Heavy Duty Vehicle Network — Part 71: Vehicle Application Layer* (SAE J1939-71). SAE International. https://doi.org/10.4271/J1939_202003. *(Protocolo estándar mundial para lectura de parámetros telemáticos de motor y combustible FMS en vehículos pesados)*.
* **Shapiro, M., Preguiça, N., Baquero, C., & Zawirski, M.** (2011). *Conflict-Free Replicated Data Types*. En X. Défago, F. Petit, & V. Villain (Eds.), *Stabilization, Safety, and Security of Distributed Systems* (Lecture Notes in Computer Science, Vol. 6976, pp. 386–400). Springer. https://doi.org/10.1007/978-3-642-24550-3_29. *(Base formal para la reconciliación determinista de estados y deduplicación de eventos tras particiones prolongadas de red)*.

---

### 4. Diseño de la Incorporación en la Arquitectura, EDT y Cronograma (Art. 29.4 / RT-26.01, RT-26.02)

#### 4.1 Inserción en la Arquitectura Lógica Multicapa (Subdoc. 4.1):
* **Capa 1 (Terreno / Borde):** Dispositivo telemático físico con flash industrial $\ge 8\text{ GB}$, motor SQLite WAL local y servicio de serialización Protobuf; acopladores inductivos CANbus en 61 unidades (Consulta N.° 14).
* **Capa 3 (Puerta de Enlace / APIM):** Ingress seguro con terminación mTLS y limitación de tasa elástica para ráfagas de reconexión (60 req/min por dispositivo).
* **Capa 5 (Event Ingestion & Broker):** Clúster Apache Kafka / Azure Event Hubs con particionamiento por camión y búfer de absorción elástica de hasta **1.500 pings/minuto**.
* **Capa 6 (Persistencia Especializada):** Motor de series temporales TimescaleDB para persistencia de trayectorias, y PostgreSQL 16 con deduplicación por `idempotency_key` (RNF-002).

#### 4.2 Trazabilidad con la Estructura de Descomposición del Trabajo (EDT) y Cronograma Contractual (Art. 17°):
La innovación se materializa a través de los siguientes paquetes de trabajo en la **Etapa 1**:

| Paquete EDT | Denominación del Paquete de Trabajo | Mes de Inicio | Mes de Hito / Entrega | Responsables |
| :---: | :--- | :---: | :---: | :---: |
| **EDT 3.4** | Desarrollo del Conector de Ingestión Telemática Unificada | Mes 3 | **Mes 6** (Cierre de diseño) | D3 (Software) |
| **EDT 4.2** | Homologación e Instalación de Búfer a Bordo en Cabina ($\ge 8\text{ GB}$) | Mes 4 | **Mes 8** (Piloto 10 unidades) | D4 (Hardware) |
| **EDT 4.5** | Configuración de Acopladores Inductivos FMS J1939 en 61 tractos | Mes 6 | **Mes 9** (Flota propia) | D4 + D3 |
| **EDT 5.2** | Mecanismo de Emisión Offline de DET con Folios CAF y Firma Local | Mes 5 | **Mes 8** (Integración SII/ERP) | D3 (Lógica/Datos) |
| **EDT 7.1** | **Marcha Blanca Telemática y Validación 72h–288h en Terreno** | Mes 12 | **Mes 15** (Fin Marcha Blanca E1) | Duplas D3 y D4 |

> **Cumplimiento del Criterio Deseable RT-26.08:** El beneficio de la Innovación Tipo 3 es **100 % verificable durante la marcha blanca de la Etapa 1 (Meses 12 a 15)**, mucho antes del mes 16 exigido por las Bases.

---

### 5. Impacto Económico Preliminar y Supuestos del Negocio (Art. 29.5 / RT-26.05)

*(Conforme a la Consulta Oficial N.° 5: Estimación preliminar y supuestos declarados en Informe 1; flujo de caja valorizado definitivo en Informe 3)*

#### 5.1 Inversión Requerida (CAPEX Preliminar)
* Memoria flash industrial no volátil $\ge 8\text{ GB}$ SLC/pSLC con *wear-leveling* para 148 tractos propios y 34 terceros adheridos: Sobrecosto marginal frente a tarjetas comerciales estándar ($\approx \$25.000\text{ CLP}$ por unidad).
* Desarrollo de microservicios de ingesta multicanal y adaptación de conectores API para los dos proveedores de terceros: Estimado en 320 horas-hombre especializadas de ingeniería de software.
* 61 acopladores inductivos sin contacto para puerto FMS: Hardware estándar de mercado de bajo costo.

#### 5.2 Efecto en el Costo Operacional (OPEX Preliminar)
* **Ahorro Radical en Consumo de Datos Móviles:** El protocolo binario Protobuf combinado con muestreo adaptativo (30 s marcha / 5 min detenido) genera apenas **13 a 16 MB/mes por camión** (frente a los > 150 MB de protocolos JSON en texto plano). Toda la flota de 374 unidades consume apenas **$\approx 5,6\text{ GB/mes}$**.
* **Cero Sobrecosto Satelital en Descargas Fotográficas:** Las fotos de entrega y siniestros se transmiten por Wi-Fi gratuito al ingresar a los 5 terminales regionales de Curimón, evitando planes de datos de alta tarificación.

#### 5.3 Beneficio Cuantitativo Esperado
1. **Recuperación de Sobreestadías No Pagadas:** Permite certificar con marcas de tiempo inalterables los tiempos de espera en clientes, recuperando al menos un **35 % de las sobreestadías hoy rechazadas** (lo que equivale a recuperar sobre **$\$80.000.000\text{ CLP anuales}$** para Curimón y sus transportistas).
2. **Mitigación Total de Multas Laborales (Art. 25 bis):** Supresión del 100 % de sanciones por pérdida de trazabilidad de descansos en zonas desérticas o pasos fronterizos.
3. **Cero Multas Tributarias por Traslado sin Guía:** Blindaje ante fiscalizaciones del SII y Carabineros al portar siempre el DET timbrado localmente.

---

### 6. Indicadores de Verificación del Beneficio y Línea Base (Art. 29.6 / RT-26.05)

| Indicador de Desempeño | Línea Base (Situación Actual Caso 10) | Meta Comprometida audIT | Momento de Medición |
| :--- | :---: | :---: | :---: |
| **Pérdida de paquetes en desconexión 72h** | 100 % de pérdida en sombra > 2 h | **0,0 % de pérdida de paquetes** | Pruebas de integración y Marcha Blanca E1 |
| **Resistencia en contingencia Los Libertadores** | Ceguera total tras 24–48 h | **Preservación continua hasta 288 h (12 días)** | Simulacro de aislamiento invernal (Mes 12) |
| **Visibilidad unificada de flota en Torre** | 3 plataformas web separadas + 34 camiones ciegos | **100 % de unidades visibles en vista única** | Cierre de Etapa 1 (Mes 15) |
| **Latencia de reconciliación post-sombra** | No existe sincronización (datos perdidos) | **$< 15\text{ minutos}$** (supera $\le 20\text{ min}$ de Cap. 15) | Marcha Blanca Etapa 1 |
| **Emisión legal de DET en puntos sin señal** | Rezagada o inexistente (riesgo de incautación) | **100 % emitido conforme antes del rodado** | Operación continua Etapa 1 |

---

### 7. Análisis de Riesgos de Adopción, Mitigación y Contingencia (Art. 29.7 / RT-26.04)

Conforme a **RT-26.04** y **RT-26.07**, se identifican los tres riesgos críticos de adopción y su tratamiento:

#### Riesgo 1: Negativa o lentitud de un proveedor GPS externo de terceros para habilitar API/Webhooks
* **Probabilidad:** Media | **Impacto:** Alto.
* **Estrategia de Mitigación:** Negociación corporativa centralizada liderada por Curimón ofreciendo homologación formal sin costo de desarrollo para el proveedor; activación de lectura mediante conectores adaptadores estándar de mercado.
* **Plan de Contingencia Supletorio:** Si un proveedor bloquea el acceso, el transportista puede autorizar la activación voluntaria del tracking temporal en la App Móvil del conductor durante el viaje activo para fines exclusivos de liquidación y sobreestadías, o acogerse al kit subsidiado en terminal (Decisión D-25).

#### Riesgo 2: Sobreescritura de memoria flash por permanencia imprevista superior a 12 días en alta cordillera
* **Probabilidad:** Muy Baja | **Impacto:** Medio.
* **Estrategia de Mitigación:** El dimensionamiento de $\ge 8\text{ GB}$ flash industrial supera por un factor de **$\times 800$** el volumen generado por un camión en 288 horas continuas (~10 MB con fotos).
* **Plan de Contingencia Supletorio:** Implementación de algoritmo FIFO de descarte selectivo que preserva indefinidamente eventos de jornada (Art. 25 bis) y DET, reduciendo la frecuencia de pings de motor si la memoria alcanzara el 90 % de ocupación.

#### Riesgo 3: Riesgo de Seguridad y Falsificación de Trazas Telemáticas en Tránsito (STRIDE / RT-26.07)
* **Probabilidad:** Baja | **Impacto:** Alto.
* **Estrategia de Mitigación:** Modelado de amenazas Zero Trust. Enlace cifrado mediante TLS 1.3 con certificados de dispositivo x.509. Todo payload de posición incorpora firma criptográfica HMAC-SHA256 generada por el enclave seguro del hardware telemático.
* **Plan de Contingencia Supletorio:** Cuarentena automática en el broker de ingestión ante cualquier paquete con firma inválida o reloj GPS no monótono, alertando de inmediato a la Torre de Control.
