# Subdocumento 2 (Anexos): Inventarios Técnicos, Restricciones y Caracterización de Actores
**Licitación Pública TFEP-01/2026 — Solución Integral de Transporte de Carga Terrestre**  
**Cliente:** Transportes Curimón S.A.  
**Proponente:** audIT Soluciones Tecnológicas SpA  
**Documento Principal Asociado:** Subdocumento 2 (`subdocumento_02_problema_adaptado.md`)  
**Área Técnica:** Gerencia de Aseguramiento de Calidad y Gobernanza

---

El presente documento complementario contiene los inventarios detallados, matrices de requerimientos, caracterización exhaustiva de flota y conductores, matrices normativas y fichas pormenorizadas de stakeholders que respaldan analíticamente el **Subdocumento 2** (*Comprensión del Problema y de la Necesidad*) presentado por **audIT Soluciones Tecnológicas SpA** para la Licitación Pública TFEP-01/2026 de **Transportes Curimón S.A.**

Conforme a lo instruido en el Comunicado 10 (§1 y §5), las tablas de catalogación y los listados que superan cinco columnas o una página de extensión se presentan en este archivo de anexos independiente para salvaguardar la legibilidad del cuerpo principal. Este documento se divide en cuatro anexos formales:
* **Anexo 2.A:** Catálogo Exhaustivo de Requerimientos de Negocio y Operacionales Preliminares.
* **Anexo 2.B:** Inventario Detallado de Flota y Caracterización de Conductores.
* **Anexo 2.C:** Matriz Exhaustiva de Restricciones Operacionales, Legales y Exclusiones Contractuales.
* **Anexo 2.D:** Fichas Detalladas de Caracterización de los Trece (13) Actores del Ecosistema.

---

## Anexo 2.A: Catálogo Exhaustivo de Requerimientos de Negocio y Operacionales Preliminares

El catálogo compendia las necesidades preliminares de negocio levantadas desde las Bases Técnicas del Caso 10, las entrevistas en terreno con los diez actores del Capítulo 8 y las exigencias normativas del transporte terrestre chileno. Cada requerimiento se codifica unívocamente, estableciendo su trazabilidad formal y su nivel de criticidad para la continuidad operacional.

#### Tabla A2.1 — Catálogo de Requerimientos de Negocio y Operacionales Preliminares
*Fuente: Elaboración propia a partir de Bases Técnicas del Caso 10 y entrevistas operacionales (Transportes Curimón S.A., 2026).*

| ID Requerimiento | Dominio Operacional | Descripción Detallada del Requerimiento Preliminar | Fuente en Pliego / Entrevista | Criticidad |
| :--- | :--- | :--- | :--- | :---: |
| **REQ-NEG-01** | Asignación y Despacho | Validar síncronamente en pre-despacho ($\le 30\text{ s}$) que el conductor cuente con horas de jornada disponibles conforme al Art. 25 bis del Código del Trabajo, bloqueando la asignación si se superan las 5 h de manejo o no se acredita el descanso previo. | Caso 10, Cap. 4.3; Entrevista R. Mansilla | **Crítica** |
| **REQ-NEG-02** | Asignación y Despacho | Cotejar automáticamente el estado de vencimiento de las ~6.000 vigencias vivas (licencias A5, revisiones técnicas, certificados de gases, permisos, seguros), impidiendo despachar vehículos o choferes con documentación caducada. | Caso 10, Cap. 4.4; Entrevista D. Aguayo | **Crítica** |
| **REQ-NEG-03** | Asignación y Despacho | Verificar la aptitud física del equipo asignado respecto al tipo de carga requerida (semirremolque refrigerado para perecibles, tolva para granel, o autorización D.S. N.° 298 para sustancias peligrosas). | Caso 10, Cap. 4.5; Entrevista R. Mansilla | **Crítica** |
| **REQ-NEG-04** | Sustancias Peligrosas | Comprobar de forma obligatoria que el conductor asignado a una de las 18 unidades SUSPEL cuente con el curso específico vigente del D.S. N.° 298 y que el vehículo porte Hoja de Datos de Seguridad y rotulación NCh 2190. | Caso 10, Cap. 4.5; Entrevista D. Aguayo | **Crítica** |
| **REQ-NEG-05** | Trazabilidad y Geocercas | Detectar automáticamente mediante geocercas poligonales la entrada, tiempo de permanencia y salida en los ~1.400 puntos de clientes, sin requerir intervención manual del conductor ni instalación de equipos en predios ajenos. | Caso 10, Cap. 4.7; Entrevista E. Valdebenito | **Alta** |
| **REQ-NEG-06** | Cobro de Sobreestadías | Generar reportes cronológicos certificados e inalterables con estampa de tiempo y coordenadas GPS del tiempo de espera en andén, proveyendo sustento probatorio irrefutable para recuperar el 71% de los cobros por sobreestadías hoy objetados. | Caso 10, Cap. 4.7; Entrevista G. Ossandón | **Alta** |
| **REQ-NEG-07** | Retornos en Vacío | Identificar en tiempo real los tractocamiones que finalizarán su descarga para sugerir triangulaciones con cargas de retorno compatibles, reduciendo el 26% de kilómetros recorridos en vacío (10,66 millones de km anuales). | Caso 10, Cap. 4.2; Entrevista R. Mansilla | **Alta** |
| **REQ-NEG-08** | Cadena de Frío | Monitorear en tiempo real la temperatura interna de las 44 ramplas refrigeradas (-30 °C a +30 °C), emitiendo alertas inmediatas a la Torre 24x7 ante desviaciones térmicas de $\pm 1{,}5\text{ }^\circ\text{C}$ o apertura no autorizada de puertas. | Caso 10, Cap. 2.1 y 4.8; Entrevista A. Lecaros | **Crítica** |
| **REQ-NEG-09** | Documentación Digital | Emitir Documentos Electrónicos de Transporte (DET para ~128.000 guías anuales) integrados con el ERP contable y el SII, habilitando la emisión offline pre-firmada en zonas de carga sin cobertura celular. | Caso 10, Cap. 4.6; Entrevista M. Riquelme | **Alta** |
| **REQ-NEG-10** | Confirmación de Entrega | Digitalizar el comprobante de entrega (*Proof of Delivery* [POD]) mediante captura fotográfica y firma digital en pantalla en destino, abatiendo el 4,2% de pérdidas o roturas de guías físicas en papel. | Caso 10, Cap. 4.7; Entrevista G. Ossandón | **Media** |
| **REQ-NEG-11** | Costeo por Ruta y Viaje | Reconstruir el costo marginal directo real de cada viaje (< 24 h post-cierre), integrando consumo de diésel por CAN bus, pasadas de peajes TAG y flete liquidado a terceros, erradicando el prorrateo ciego por ingreso. | Caso 10, Cap. 4.1 y 7.3; Entrevista G. Ossandón | **Crítica** |
| **REQ-NEG-12** | Renegociación Contratos | Proveer a la Gerencia de Finanzas la matriz de rentabilidad histórica desagregada por cliente y ruta para renegociar los 3 contratos deficitarios (31% del ingreso, peor a -14%) previo a sus vencimientos en 2027. | Caso 10, Cap. 2.3; Entrevista G. Ossandón | **Crítica** |
| **REQ-NEG-13** | Telemetría CAN bus | Capturar y procesar de forma pasiva y no intrusiva los parámetros de operación del motor (RPM, odómetro, temperatura de refrigerante, códigos de falla DTC y consumo acumulado) en los 61 tractos con CAN bus de fábrica. | Caso 10, Cap. 4.10; Entrevista H. Trincado | **Alta** |
| **REQ-NEG-14** | Mantenimiento Preventivo | Generar órdenes automáticas de mantenimiento en base al kilometraje y horas de motor efectivamente acumulados por telemetría, sustituyendo la planificación visual manual cada 6 días en taller San Bernardo. | Caso 10, Cap. 4.10; Entrevista H. Trincado | **Alta** |
| **REQ-NEG-15** | Integración Talleres Ruta | Habilitar un canal web simplificado para que los talleres externos en ruta registren intervenciones de emergencia y repuestos instalados, actualizando la hoja de vida vehicular de forma inmediata. | Caso 10, Cap. 4.10; Entrevista H. Trincado | **Media** |
| **REQ-NEG-16** | Liquidación a Terceros | Automatizar el cálculo de pre-liquidaciones mensuales a los 148 transportistas terceros a partir de los viajes validados en sistema, reduciendo el ciclo de 9 días hábiles y la tasa de error del 11%. | Caso 10, Cap. 4.11; Entrevista G. Ossandón | **Alta** |
| **REQ-NEG-17** | Privacidad de Terceros | Desconectar automáticamente la geolocalización y telemetría de los camiones subcontratados una vez finalizado el viaje asignado (Geofencing temporal), resguardando su privacidad conforme a la Ley N.° 21.719. | Bases Admin. Art. 4.3; Entrevista N. Sandoval | **Crítica** |
| **REQ-NEG-18** | Homologación Plataformas | Ingerir y unificar en una vista de mapa única las posiciones GPS provenientes de las tres plataformas dispares existentes (Wialon, Wisetrack, Webfleet) para los 192 camiones terceros que cuentan con rastreo previo. | Caso 10, Cap. 5; Entrevista P. Kast | **Alta** |
| **REQ-NEG-19** | Sensorización 34 Camiones | Equipamiento telemático estándar en los 34 camiones de terceros que carecen de GPS, incorporándolos a la vista operacional de la Torre de Control. | Caso 10, Cap. 2.1 y 5; Entrevista E. Valdebenito | **Alta** |
| **REQ-NEG-20** | Resiliencia Desconexión | Garantizar la persistencia y almacenamiento local en memoria industrial a bordo de al menos 288 horas continuas (12 días) de telemetría completa durante cierres climáticos del Paso Los Libertadores. | Caso 10, RT-03.10; Entrevista M. Riquelme | **Crítica** |
| **REQ-NEG-21** | Seguridad en Cabina | Restringir cualquier interacción táctil del chofer con dispositivos en cabina cuando el camión se encuentre en movimiento ($v > 0\text{ km/h}$), canalizando alertas exclusivamente por síntesis vocal pasiva (Ley No Chat). | Ley N.° 21.377; Entrevista Y. Colipán | **Crítica** |
| **REQ-NEG-22** | Alerta Anticipada Fatiga | Calcular la alerta de descanso del Art. 25 bis considerando la distancia y tiempo estimado hacia el próximo punto seguro de detención (berma o servicentro), evitando que la alarma venza en zonas desérticas sin servicios. | Caso 10, Cap. 4.3; Entrevista Y. Colipán | **Alta** |
| **REQ-NEG-23** | Tacógrafo Digital | Habilitar la descarga y custodia criptográfica periódica de los archivos binarios de los tacógrafos digitales, preservando la cadena de custodia probatoria ante requerimientos de la Dirección del Trabajo. | Código del Trabajo Art. 25 bis; D. Aguayo | **Crítica** |
| **REQ-NEG-24** | Huella de Carbono GLEC | Computar y reportar de manera mensual las emisiones de gases de efecto invernadero ($\text{g CO}_2\text{e}/\text{t-km}$) auditables bajo norma GLEC / ISO 14083 para responder a las exigencias 2029 del cliente exportador (19%). | Caso 10, Cap. 4.6; Entrevista A. Lecaros | **Crítica** |
| **REQ-NEG-25** | Trazabilidad Cliente 19% | Proveer un portal web seguro para clientes que exponga en tiempo real la posición georreferenciada de la carga, temperatura del furgón y estado del despacho durante el tránsito del flete contratado. | Caso 10, Cap. 4.6; Entrevista A. Lecaros | **Alta** |

---

## Anexo 2.B: Inventario Detallado de Flota y Caracterización de Conductores

Este anexo desglosa la infraestructura vehicular móvil y la fuerza laboral que compone la operación de Transportes Curimón S.A., diferenciando el régimen de propiedad, el nivel de equipamiento telemático basal y la estrategia de integración tecnológica requerida para cada segmento.

### 2.B.1 Inventario Desagregado del Parque Vehicular (374 Tractocamiones)

El parque de tractocamiones se clasifica de acuerdo con su titularidad jurídica y su madurez instrumental:

#### Tabla A2.2 — Inventario Clasificado de Tractocamiones
*Fuente: Elaboración propia a partir de Bases Técnicas del Caso 10 (Transportes Curimón S.A., 2026).*

| Segmento de Flota | Cantidad | Participación | Antigüedad Media | Equipamiento Telemático Actual | Requerimiento de Homologación e Integración |
| :--- | :---: | :---: | :---: | :--- | :--- |
| **Flota Propia CAN bus Fábrica** | 61 | 16,3% | 3,2 años | Módulo telemático de fábrica con bus CAN J1939 inactivo. Nunca consultado. | Requerimiento de captura pasiva no intrusiva mediante acopladores inductivos sin corte de cableado. |
| **Flota Propia sin Telemetría Fábrica**| 87 | 23,3% | 8,6 años | Sin telemetría de bus de datos. Dispositivos GPS básicos de primera generación. | Instalación de dispositivo telemático estándar con acoplamiento inductivo no invasivo. |
| **Flota Terceros con GPS Previo** | 192 | 51,3% | Variable (4-12 años)| Dispositivos GPS de 3 proveedores comerciales dispares (Wialon, Wisetrack, Webfleet). | Ingesta estandarizada mediante interfaces API/Webhooks en modalidad de intercambio de datos telemáticos. |
| **Flota Terceros sin Dispositivo GPS** | 34 | 9,1% | Variable (>10 años) | Cero equipamiento tecnológico. Monitoreo puramente telefónico por voz. | Requerimiento de equipamiento telemático estándar e integración de posicionamiento georreferenciado. |
| **TOTAL PARQUE TRACTOCAMIONES** | **374** | **100,0%** | **6,4 años (media)** | **Parque altamente asimétrico y heterogéneo.** | **Integración unificada bajo modelo agnóstico de ingesta telemática.** |

### 2.B.2 Inventario de Semirremolques y Equipos de Arrastre Propios (210 Unidades)

Curimón es propietaria del 100% de los 210 semirremolques utilizados en la operación, asegurando el acople físico de la carga independientemente de si el tracto motriz es propio o subcontratado:

#### Tabla A2.3 — Inventario de Semirremolques Propios por Tipología de Carga
*Fuente: Elaboración propia a partir de Bases Técnicas del Caso 10 (Transportes Curimón S.A., 2026).*

| Tipología de Semirremolque | Cantidad | % Flota Arrastre | Operación Principal y Rubro de Clientes | Instrumental y Requerimiento Específico |
| :--- | :---: | :---: | :--- | :--- |
| **Semirremolques Refrigerados (Reefers)**| 44 | 21,0% | Cadena de frío agroexportadora (diciembre-abril) e industria acuícola en Puerto Montt. | Sensorización con sondas de temperatura Pt100 (-30 °C a +30 °C) y sensor de apertura de puertas. |
| **Semirremolques Sustancias Peligrosas** | 18 | 8,6% | Transporte químico, combustibles y reactivos mineros (Antofagasta y Concepción). | Certificación bajo D.S. N.° 298/1994, rotulación NCh 2190, extintores y revisión especial. |
| **Ramplas Planas y Furgones Secos** | 98 | 46,7% | Carga general paletizada, materiales industriales, retail y productos de consumo masivo. | Monitoreo de enganche, control de precintos y odometría de eje mediante sensor de rueda. |
| **Tolvas Graneleras** | 32 | 15,2% | Transporte de graneles minerales, áridos y productos agrícolas a granel. | Control de accionamiento hidráulico de volteo y sensor de sobrepeso por eje. |
| **Portacontenedores Portuarios** | 18 | 8,5% | Operación marítimo-portuaria en Valparaíso y San Antonio; contenedores de exportación. | Control de trabas de seguridad (*twistlocks*) e integración documental aduanera. |
| **TOTAL SEMIRREMOLQUES PROPIOS** | **210** | **100,0%** | **Capacidad total de arrastre corporativo.** | **Flota 100% de propiedad de Curimón S.A.** |

### 2.B.3 Caracterización Detallada de la Dotación de Conductores (454 Operadores)

La operación de la flota requiere una fuerza laboral de 454 choferes, estructurada en dos grupos con relaciones contractuales radicalmente distintas:

#### Tabla A2.4 — Caracterización Sociolaboral y de Control de Conductores
*Fuente: Elaboración propia a partir de Bases Técnicas del Caso 10 y Código del Trabajo (Transportes Curimón S.A., 2026).*

| Atributo / Parámetro | Conductores Propios de Curimón | Conductores Subcontratados de Terceros |
| :--- | :--- | :--- |
| **Dotación Asignable** | **196 conductores (43,2% de la fuerza laboral)** | **258 conductores (56,8% de la fuerza laboral)** |
| **Relación Contractual** | Contrato de trabajo indefinido directo con Curimón S.A. | Dependientes laborales de los 148 transportistas terceros. Cero subordinación con Curimón. |
| **Marco Jurídico Laboral** | Artículo 25 bis del Código del Trabajo (régimen especial de carga). | Art. 25 bis bajo régimen de subcontratación de la Ley N.° 20.123 (responsabilidad solidaria/subsidiaria). |
| **Límites de Jornada Legal** | Máx. 5 h conducción continua; 2 h descanso; 8 h descanso diario; 180 h mensuales. | Mismos límites legales, pero con fiscalización histórica nula por parte de Curimón. |
| **Régimen de Turnos y Descanso** | Controlado administrativamente por la empresa; turnos conocidos. | Desconocimiento total de turnos previos realizados para otros mandantes o clientes ajenos. |
| **Mecanismo Probatorio Requerido** | Registro digital inalterable de jornada con trazabilidad y custodia probatoria. | Atestación documental al aceptar despacho y registro de eventos operacionales del viaje. |
| **Resguardo de Privacidad** | Datos laborales procesados en virtud del contrato de trabajo y deber patronal. | Geocercas temporales y disociación de coordenadas: telemetría desvinculada fuera del viaje asignado (Ley N.° 21.719). |
| **Representante / Referente** | Yasna Colipán Marín (conductora de ruta norte, 7 años de antigüedad). | Nolberto Sandoval Pinto (transportista con 2 tractos y chofer a cargo, 9 años en Curimón). |

---

## Anexo 2.C: Matriz Exhaustiva de Restricciones Operacionales, Legales y Exclusiones Contractuales

Este anexo recopila de forma sistemática las restricciones legales vigentes en Chile, las restricciones físicas de la operación en carretera y las exclusiones explícitas de la propuesta técnica de audIT SpA.

#### Tabla A2.5 — Matriz de Restricciones Legales, Normativas y Regulatorias
*Fuente: Elaboración propia a partir de la legislación chilena aplicable al transporte de carga terrestre.*

| Código | Norma Legal / Estándar | Exigencia Normativa Concreta | Impacto Directo en el Diseño Operacional |
| :--- | :--- | :--- | :--- |
| **REST-LEG-01** | **Código del Trabajo Art. 25 bis** | Límite estricto de 5 horas continuas de conducción; descanso intermedio no inferior a 2 horas; descanso diario ininterrumpido de 8 horas en período de 24 h; tope mensual de 180 horas. | Prohibición algorítmica de asignar viajes a conductores que no dispongan de ciclo de descanso legal acreditado. Alerta dinámica en ruta a $\ge 45\text{ min}$ de la quinta hora. |
| **REST-LEG-02** | **Ley N.° 20.123 (Subcontratación)** | Responsabilidad solidaria o subsidiaria de la empresa principal por obligaciones laborales, previsionales y de seguridad de trabajadores de contratistas. | Deber ineludible de Curimón de verificar la jornada y descansos de los 258 choferes subcontratados antes del despacho para evitar contingencias judiciales indemnizatorias. |
| **REST-LEG-03** | **Ley N.° 21.377 (Ley No Chat)** | Sanciona como gravísima la conducción manipulando dispositivos electrónicos o teléfonos que no vengan de fábrica, salvo manos libres sin desvío visual. | Enclavamiento cinético: bloqueo total de pantallas táctiles en cabina con $v > 0\text{ km/h}$. Alertas operacionales canalizadas exclusivamente por síntesis vocal pasiva fuera de línea. |
| **REST-LEG-04** | **Ley N.° 21.719 (Protección de Datos)** | Tratamiento lícito de datos personales (ubicación e identidad del conductor externo) supeditado a finalidad legítima, proporcionalidad y consentimiento. | Geofencing temporal: la posición del camión subcontratado solo se procesa mientras el viaje asignado esté activo. Cifrado a nivel de campo (FLE) sobre datos personales. |
| **REST-LEG-05** | **D.S. N.° 298/1994 (MTT - SUSPEL)** | Reglamenta el transporte de cargas peligrosas: curso de capacitación vigente del chofer, antigüedad máxima, revisión periódica, rotulado NCh 2190 y HDS. | Validación cruzada bloqueante en pre-despacho: verificación digital de la credencial del chofer y rótulos antes de destrabar la orden de carga en las 18 unidades SUSPEL. |
| **REST-LEG-06** | **D.S. N.° 43/2015 (MINSAL - Almacenamiento)** | Almacenamiento seguro de sustancias peligrosas: distancias de seguridad, pretiles de retención de derrames y prohibición de estacionar camiones cargados fuera de zona. | Zonificación espacial en el Terminal Matriz de San Bernardo y control telemático de permanencia de tractos cargados en zonas autorizadas de estacionamiento. |
| **REST-LEG-07** | **D.S. N.° 158/1980 (MOP - Pesajes)** | Límites máximos de peso bruto vehicular y peso por eje para preservar la infraestructura vial nacional. Control en plazas de pesaje oficiales. | Monitoreo y control del manifiesto de estiba en origen para abatir las 142 detenciones registradas en 2025 (2.556 horas-camión inmovilizadas). |
| **REST-LEG-08** | **Marco GLEC / ISO 14083:2023** | Cálculo estandarizado de emisiones de gases de efecto invernadero ($\text{g CO}_2\text{e}/\text{t-km}$) considerando factores Well-to-Wheel (WTT + TTW). | Reportabilidad auditada obligatoria para la renovación contractual de 2029 con el cliente exportador principal (19% de ingresos corporativos). |

#### Tabla A2.6 — Matriz de Restricciones Físicas, Ambientales y Operacionales de la Red
*Fuente: Elaboración propia a partir de Bases Técnicas del Caso 10 y Bases Transversales (Transportes Curimón S.A., 2026).*

| Código | Restricción Operacional | Descripción del Límite Físico o Ambiental | Consecuencia en la Arquitectura Tecnológica |
| :--- | :--- | :--- | :--- |
| **REST-FIS-01** | **Ventana de Intervención de Flota** | La flota rueda 24/7/365. Los propios pasan por taller cada 6 días; el 22% de los terceros pasa menos de 1 vez/mes por terminal. | Prohibición de planificar detenciones masivas de flota. Despliegue secuencial de hardware en San Bernardo a razón de 25 camiones/mes. |
| **REST-FIS-02** | **Sombra Celular Prolongada** | Tramos de más de 80 kilómetros continuos sin cobertura de red móvil en el Desierto de Atacama (Ruta 5 Norte) y cordillera. | Arquitectura *Offline-First*: persistencia en búfer local vehicular con retransmisión asíncrona determinista (*exponential backoff* con jitter). |
| **REST-FIS-03** | **Cierres Paso Los Libertadores** | Cortes climáticos de hasta 12 días continuos (288 horas) por nieve y viento blanco en alta montaña (> 3.200 msnm). | Hardware embarcado dotado de memoria flash eMMC industrial $\ge 8{,}0\text{ GB}$, capaz de retener $> 288\text{ h}$ de telemetría completa. |
| **REST-FIS-04** | **Condiciones Térmicas y Vibratorias** | Temperaturas extremas de cabina entre -20 °C y +70 °C y vibración severa continua en caminos pavimentados y no pavimentados. | Hardware certificado obligatoriamente bajo norma industrial SAE J1455 con sellado ambiental grado IP67. |
| **REST-FIS-05** | **Infraestructura de Servidores Matriz** | Sala de servidores en San Bernardo de 26 m², split doméstico y UPS 20 min; incumple requerimientos RT-06.01 a RT-06.09. | Descarte de infraestructura central transaccional *on-premise*; emplazamiento obligatorio en nube pública resiliente (Azure Multi-AZ). |
| **REST-FIS-06** | **Puntos de Clientes Ajenos (~1.400)** | Recintos privados de terceros donde está estrictamente prohibido instalar infraestructura física, antenas o sensores de Curimón. | Trazabilidad basada exclusivamente en geocercas satelitales virtuales poligonales y telemetría propia del camión. |

#### Tabla A2.7 — Matriz de Exclusiones Contractuales Explícitas
*Fuente: Elaboración propia conforme a pliego de licitación y estándares de audIT SpA.*

| Código | Objeto Excluido | Justificación Técnica y Delimitación de Responsabilidad |
| :--- | :--- | :--- |
| **EXC-01** | Suministro de combustible diésel y lubricantes | La provisión física del carburante corresponde a los convenios de Curimón con distribuidoras mayoristas; audIT audita el consumo. |
| **EXC-02** | Mantenimiento mecánico y repuestos de taller | El recambio físico de piezas, neumáticos y reparaciones mecánicas es potestad exclusiva del personal de talleres de Curimón. |
| **EXC-03** | Modificación del código fuente del ERP contable | Curimón mantiene la titularidad de su software contable; audIT interoperará exclusivamente mediante servicios web y APIs. |
| **EXC-04** | Obras civiles mayores en terminales | Se excluyen ampliaciones edilicias en San Bernardo; la plataforma transaccional de misión crítica se alojará en la nube. |
| **EXC-05** | Honorarios y costos de desarrollo en la Oferta Técnica | En estricto cumplimiento del Artículo 50.2 de las Bases Administrativas, la propuesta técnica no contiene montos ni tarifas de audIT SpA. |

---

## Anexo 2.D: Fichas Detalladas de Caracterización de los Trece (13) Actores del Ecosistema

A continuación se presentan las fichas completas de caracterización de los trece grupos de interés, integrando los tres actores omitidos en informes previos (Fondo de Inversión, Dirección del Trabajo y Aseguradora de Carga y Flota) y profundizando en las dependencias y riesgos de cada uno.

---

### FICHA N.° 01: Fondo de Inversión Institucional (Accionista Minoritario)

* **Identificación y Emplazamiento:** Representa al fondo de inversión institucional que adquirió el **22% de la propiedad accionaria** de Transportes Curimón S.A. en el año 2019. Posee representación formal en el Directorio corporativo.
* **Objetivos Estratégicos:** Maximización del retorno sobre el capital invertido (ROIC), resguardo del margen EBITDA, saneamiento de contratos deficitarios, erradicación de pasivos contingentes laborales y aseguramiento de un gobierno corporativo robusto para una eventual salida estratégica o refinanciamiento.
* **Dolores Operacionales y Financieros:** Deterioro del margen operacional (comprimido al 9,0%), existencia de 3 contratos principales bajo costo (-14%), ceguera frente a pasivos laborales contingentes derivados del régimen de subcontratación (Ley N.° 20.123) y amenaza de pérdida del cliente principal (19% de la facturación corporativa).
* **Testimonio Representativo de Directorio:** *«Nosotros ingresamos a Curimón en 2019 para profesionalizar la gestión y rentabilizar la compañía. No es tolerable que un tercio de los ingresos provenga de contratos que operan a pérdida y que sigamos administrando seis mil vencimientos en planillas Excel. Si la empresa enfrenta una demanda colectiva por responsabilidad solidaria en un siniestro grave o pierde el contrato del 19%, el valor de la empresa se destruye. Exigimos auditoría de costos en tiempo real y gobernanza técnica certificada».*
* **Dependencias y Necesidades de Información:** Requiere tableros analíticos consolidados de EBITDA por unidad de negocio, auditoría de costos marginales por viaje, reportabilidad de cumplimiento normativo y reducción sistemática de riesgos operacionales.
* **Poder Formal / Veto:** **Máximo (en Directorio).** Capacidad de condicionar aumentos de capital, vetar inversiones y exigir auditorías forenses externas.
* **Nivel de Interés:** **Bajo en la contingencia diaria / Muy Alto en la estabilidad estratégica corporativa.**
* **Cuadrante de Gestión:** **Cuadrante 2: Mantener Satisfecho (Gobernanza y Retorno).**
* **Riesgo Operacional si no se Resuelve:** Bloqueo de presupuesto corporativo, desalineamiento de accionistas y retiro de respaldo financiero para el plan de renovación de flota.
* **Mecanismo de Interacción y Mitigación de Fricción:** Presentación mensual de indicadores consolidados de rentabilidad marginal por cliente y matriz de reducción de pasivos contingentes auditados bajo normas ISO 27001 e ISO 9001.

---

### FICHA N.° 02: Dirección del Trabajo (DT — Autoridad Laboral Fiscalizadora)

* **Identificación y Emplazamiento:** Órgano fiscalizador del Estado de Chile dependiente del Ministerio del Trabajo y Previsión Social. Ejerce inspecciones laborales en terreno, terminales viales y carretera.
* **Objetivos Estratégicos:** Tutela y fiscalización del cumplimiento estricto de la legislación laboral chilena, con especial énfasis en el régimen de jornada especial y descansos de los choferes de carga interurbana consagrados en el Artículo 25 bis del Código del Trabajo y la Ley N.° 20.123.
* **Dolores Operacionales e Infraccionales:** Cero descargas históricas de tacógrafos digitales en Curimón, ceguera institucional respecto a la jornada previa de los 258 choferes subcontratados, manipulación de libros de asistencia en papel y ocurrencia de siniestros graves en carretera vinculados a fatiga extrema (ej. volcamiento en km 312).
* **Testimonio Representativo de Inspección:** *«El Artículo 25 bis no admite ambigüedades: cinco horas de conducción como máximo continuo y dos horas obligatorias de descanso. En faenas de transporte interurbano, la empresa principal tiene la obligación legal de controlar las condiciones de trabajo de los subcontratados. Si no exhiben registros electrónicos automatizados e inalterables en la fiscalización, aplicaremos las multas máximas y procederemos a la clausura temporal de las faenas de despacho».*
* **Dependencias y Necesidades de Información:** Requiere registros electrónicos de asistencia y conducción auditables, con cadena de custodia inalterable, marcas de tiempo exactas y disponibilidad inmediata ante requerimiento de inspectores en cualquier terminal de la red.
* **Poder Formal / Veto:** **Extremo (Potestad Pública Sancionatoria y de Clausura).** Capacidad legal de paralizar despachos, aplicar multas gravísimas y remitir antecedentes a tribunales de cobranza laboral y previsional.
* **Nivel de Interés:** **Bajo en la logística diaria / Crítico ante fiscalizaciones e incidentes viales.**
* **Cuadrante de Gestión:** **Cuadrante 2: Mantener Satisfecho (Cumplimiento Legal Invariable).**
* **Riesgo Operacional si no se Resuelve:** Paralización legal de terminales de Curimón, multas reiteradas por infracciones gravísimas y pérdida de la calidad de empleador habilitado para contratar con el Estado o grandes mandantes.
* **Mecanismo de Interacción y Mitigación de Fricción:** Implementación de registro electrónico de jornada inalterable con sellado cronológico y descarga periódica certificada de tacógrafos digitales.

---

### FICHA N.° 03: Compañías Aseguradoras de Carga y Flota

* **Identificación y Emplazamiento:** Entidades financieras aseguradoras nacionales e internacionales que suscriben las pólizas de Responsabilidad Civil (RC), daños a la carga perecible (cadena de frío), transporte de sustancias peligrosas y casco de tractocamiones de Curimón.
* **Objetivos Estratégicos:** Determinación precisa del riesgo asegurable, verificación estricta de condiciones de operabilidad previa a liquidar siniestros, exigencia de debida diligencia patronal y rechazo de coberturas ante negligencia inexcusable o transgresión de normas legales de tránsito y jornada.
* **Dolores Operacionales y de Siniestralidad:** Ocurrencia de 4 siniestros graves con lesiones en los últimos 3 años, falta de telemetría de temperatura histórica ininterrumpida ante reclamos de quiebre de frío en las 44 ramplas refrigeradas, y ausencia de medios probatorios de velocidad en camiones de terceros al momento de volcamientos.
* **Testimonio Representativo de Ajustador de Seguros:** *«Cuando se presenta un siniestro de pérdida total de carga de salmones o fruta refrigerada por valor de cientos de miles de dólares, lo primero que exige la póliza es el registro continuo del termógrafo. Si hay baches de información de doce horas porque el camión pasó por una zona de sombra o no hay bitácora de temperatura, el reclamo se rechaza de plano. Lo mismo aplica a siniestros de carretera: si el conductor manejó seis horas sin parar, la cobertura de responsabilidad civil caduca por negligencia patronal».*
* **Dependencias y Necesidades de Información:** Requiere series temporales inalterables de temperatura (-30 °C a +30 °C) a 1 Hz en reefers, bitácoras de velocidad y odometría de segundo a segundo previas al impacto, y acreditación documental de revisiones técnicas y mantenciones al día.
* **Poder Formal / Veto:** **Alto (Capacidad de Denegación de Cobertura y Elevación de Primas).** Capacidad de no indemnizar siniestros millonarios y elevar las primas comerciales hasta hacer inviable la operación.
* **Nivel de Interés:** **Bajo en la operación rutinaria / Crítico ante la ocurrencia de siniestros.**
* **Cuadrante de Gestión:** **Cuadrante 2: Mantener Satisfecho (Mitigación Probatoria de Riesgo).**
* **Riesgo Operacional si no se Resuelve:** Pérdidas patrimoniales catastróficas no cubiertas por seguros ante volcamientos o descomposición de cargas de alto valor en ruta.
* **Mecanismo de Interacción y Mitigación de Fricción:** Sensorización Pt100 certificada en las 44 ramplas de frío, registro circular local inalterable de telemetría cinemática y emisión de certificados de viaje seguros.

---

### FICHA N.° 04: Directorio y Familia Fundadora (78% de la Propiedad)

* **Identificación y Emplazamiento:** Representa a la segunda generación familiar fundadora de Transportes Curimón S.A., controladora del 78% del capital social de la compañía cerrada.
* **Objetivos Estratégicos:** Continuidad histórica de la empresa familiar, preservación del patrimonio corporativo, mantenimiento de relaciones comerciales de largo plazo y defensa de la reputación de la marca Curimón construida durante décadas.
* **Dolores Operacionales:** Sentimiento de pérdida de control sobre la operación, amenaza existencial por la posible no renovación del contrato del 19% en 2029, daño a la reputación corporativa por accidentes de carretera y fricción con los socios del fondo de inversión por la baja rentabilidad (9,0%).
* **Testimonio Representativo de Accionista:** *«Mi padre fundó esta empresa con un camión propio y la convirtió en un actor nacional. Hoy nos encontramos con que más de la mitad de los camiones no son nuestros y que un cliente histórico nos pone un ultimátum para 2029. Queremos que la empresa siga siendo viable para la tercera generación, pero necesitamos recuperar el control real de lo que pasa en la ruta sin destruir la relación con los transportistas que nos han acompañado por años».*
* **Dependencias y Necesidades de Información:** Informes de desempeño global, estado de mitigación de la brecha 2029 y preservación de la solvencia patrimonial.
* **Poder Formal / Veto:** **Máximo (Societario y de Control Estratégico).**
* **Nivel de Interés:** **Medio en el detalle técnico / Máximo en la viabilidad y reputación corporativa.**
* **Cuadrante de Gestión:** **Cuadrante 2: Mantener Satisfecho (Alineamiento Patrimonial y Reputacional).**
* **Riesgo Operacional si no se Resuelve:** Reestructuraciones traumáticas de la administración, pérdida de foco de negocio e insolvencia por pasivos ocultos.
* **Mecanismo de Interacción y Mitigación de Fricción:** Reportes trimestrales de avance en la erradicación de brechas normativas y cumplimiento del pliego licitado.

---

### FICHA N.° 05: Enrique Valdebenito Rioseco — Gerente General (21 años en Curimón)

* **Identificación y Emplazamiento:** Máxima autoridad ejecutiva y representante legal de Transportes Curimón S.A. Conduce la compañía reportando directamente al Directorio.
* **Objetivos Estratégicos:** Asegurar la viabilidad integral de la empresa, equilibrar la relación entre transportistas independientes y clientes corporativos, erradicar la exposición penal personal por accidentes en carretera y liderar la modernización operacional hacia 2029.
* **Dolores Operacionales:** La fractura insostenible entre la responsabilidad civil y penal total que asume como representante legal y el control nulo sobre los activos y choferes externos; temor fundado a que la imposición de tecnología provoque la fuga de los 148 transportistas terceros.
* **Testimonio Representativo:** *«El sesenta por ciento de mi capacidad rodante no me pertenece y esas personas no son mis trabajadores. Yo no les puedo dar una orden patronal. Entonces, cuando alguien me proponga instalar un dispositivo, le voy a preguntar quién le va a pedir permiso a ciento cuarenta y ocho dueños independientes y qué les vamos a ofrecer a cambio para que acepten».*
* **Dependencias y Necesidades de Información:** Requiere un modelo de adopción viable, basado en incentivos compartidos y métricas de riesgo consolidadas en tiempo real.
* **Poder Formal / Veto:** **Máximo (Liderazgo Ejecutivo y Adjudicador de Licitación).**
* **Nivel de Interés:** **Máximo en la totalidad de las dimensiones del proyecto.**
* **Cuadrante de Gestión:** **Cuadrante 1: Gestionar de Cerca (Socio Estratégico Principal).**
* **Riesgo Operacional si no se Resuelve:** Parálisis operacional por conflicto con la red de transportistas subcontratados o pérdida del 19% de ingresos corporativos.
* **Mecanismo de Interacción y Mitigación de Fricción:** Modelo de gobernanza colaborativo con terceros, portal de liquidación transparente e integración estandarizada para las 34 unidades sin GPS.

---

### FICHA N.° 06: Ricardo Mansilla Oyarzo — Gerente de Operaciones y Despacho

* **Identificación y Emplazamiento:** Responsable de la Torre de Programación de San Bernardo y del cumplimiento diario de los 96.000 viajes anuales con una dotación de 22 despachadores en turnos 24x7x365.
* **Objetivos Estratégicos:** Cumplimiento estricto de itinerarios de clientes, reducción sistemática del 26% de kilómetros en vacío, asignación eficiente de la flota mixta y erradicación de errores humanos en el despacho.
* **Dolores Operacionales:** Coordinar despachos a ciegas mirando tres pantallas GPS incompatibles; desconocimiento de la jornada previa de conductores externos; 34 camiones gestionados exclusivamente por teléfono; y el temor permanente a que un sistema excesivamente rígido paralice los despachos diarios.
* **Testimonio Representativo:** *«Para asignar un viaje tengo que saber cuatro cosas al mismo tiempo: dónde está el camión, si el equipo sirve para esa carga, si el conductor tiene jornada, y si los papeles están al día. De esas cuatro, hoy sé una y media... Prefiero que un sistema me bloquee automáticamente a que me deje pasar un viaje ilegal».*
* **Dependencias y Necesidades de Información:** Visualización unificada de posición GPS, algoritmo de asignación con validación bloqueante pre-despacho (< 30 s) y motor heurístico para triangular cargas de retorno.
* **Poder Formal / Veto:** **Alto (Capacidad de rechazo operativo de herramientas complejas).**
* **Nivel de Interés:** **Máximo (Opera las 24 horas del día).**
* **Cuadrante de Gestión:** **Cuadrante 1: Gestionar de Cerca (Usuario Operativo Crítico).**
* **Riesgo Operacional si no se Resuelve:** Persistencia del 26% de kilómetros en vacío, sobreutilización de conductores y riesgo continuo de detenciones en ruta.
* **Mecanismo de Interacción y Mitigación de Fricción:** Torre de control unificada con validación automática en memoria Redis y protocolo claro de escalamiento excepcional.

---

### FICHA N.° 07: Gabriela Ossandón Prieto — Gerenta de Administración y Finanzas (Ene-26)

* **Identificación y Emplazamiento:** Líder del área financiera y contable, incorporada recientemente para sanear los márgenes corporativos y profesionalizar la gestión de costos.
* **Objetivos Estratégicos:** Recuperación del margen operacional corporativo (por sobre el 9,0%), erradicación de subsidios cruzados en contratos, costeo marginal analítico por viaje y aceleración del ciclo de liquidación a transportistas.
* **Dolores Operacionales:** Ceguera financiera estructural provocada por el prorrateo ciego de costos por ingresos; contratos deficitarios operando a -14% durante cuatro años; rezago de 40 días en la facturación de diésel; y un proceso de liquidación manual mensual a 148 dueños que toma 9 días a 8 personas con un 11% de notas de corrección.
* **Testimonio Representativo:** *«Repartíamos los costos por ingreso, que es la manera más elegante de no saber nada. Las rutas buenas venían subsidiando a las malas... 148 liquidaciones al mes que arman ocho personas en nueve días y el once por ciento hay que corregirlo después. Esta empresa gana apenas nueve por ciento, no hay margen para seguir a ciegas».*
* **Dependencias y Necesidades de Información:** Conciliación diaria (< 24 h) de combustible, peajes de autopista y fletes por orden de transporte; telemetría de consumo directo por CAN bus; e integración contable con ERP.
* **Poder Formal / Veto:** **Alto (Control de caja, inversiones y autorizaciones de pago).**
* **Nivel de Interés:** **Alto (Orientado al margen operacional).**
* **Cuadrante de Gestión:** **Cuadrante 1: Gestionar de Cerca (Custodia de la Rentabilidad).**
* **Riesgo Operacional si no se Resuelve:** Colapso de liquidez corporativa por persistencia de contratos bajo costo y deterioro de relaciones con transportistas subcontratados.
* **Mecanismo de Interacción y Mitigación de Fricción:** Módulo de costeo analítico por kilómetro y tonelada habilitado en el Mes 9 (Etapa 1) para respaldar la renegociación contractual de 2027.

---

### FICHA N.° 08: Hugo Trincado Bahamonde — Jefe de Taller y Mantenimiento

* **Identificación y Emplazamiento:** Responsable del mantenimiento preventivo y correctivo de los 148 tractocamiones y 210 semirremolques propios en los talleres de San Bernardo y Los Ángeles, liderando un equipo de 46 mecánicos y técnicos.
* **Objetivos Estratégicos:** Maximización de la disponibilidad mecánica de los activos propios, transición desde un modelo reactivo hacia mantenimiento predictivo basado en uso real, y reducción de fallas catastróficas en carretera.
* **Dolores Operacionales:** Mantenimiento preventivo fundamentado en "adivinanza informada" por lectura visual manual de odómetros; 61 tractocamiones propios con módulos CAN bus de fábrica inactivos desde su compra; y reparaciones de emergencia en ruta efectuadas por talleres externos que no quedan registradas en la hoja de vida técnica del camión.
* **Testimonio Representativo:** *«El plan preventivo es una adivinanza informada. Sesenta y un camiones traen telemetría de fábrica y desde que los compramos nadie ha bajado ese dato. Cuando un camión se rompe en ruta lo arregla un taller externo y no queda registro en la hoja de vida. Además, la flota propia pasa por taller cada seis días y los terceros pasan una vez al mes o nunca: la física manda».*
* **Dependencias y Necesidades de Información:** Odometría telemática remota en tiempo real, captura de códigos de falla de motor (DTCs) por CAN bus J1939 y formulario ligero para registro de talleres externos.
* **Poder Formal / Veto:** **Medio-Alto (Logística y disponibilidad de bahías de taller).**
* **Nivel de Interés:** **Medio-Alto (Orientado a la confiabilidad mecánica).**
* **Cuadrante de Gestión:** **Cuadrante 3: Monitorear y Coordinar (Soporte Técnico de Despliegue).**
* **Riesgo Operacional si no se Resuelve:** Fallas de motor masivas en carretera, sobrecostos de reparación reactiva y desgaste acelerado de flota propia.
* **Mecanismo de Interacción y Mitigación de Fricción:** Acopladores inductivos no intrusivos en taller San Bernardo coordinados según la cadencia regular de pasadas de mantenimiento cada 6 días.

---

### FICHA N.° 09: Denisse Aguayo Lillo — Jefa de Prevención de Riesgos y Seguridad

* **Identificación y Emplazamiento:** Responsable del cumplimiento normativo en seguridad vial, salud ocupacional y transporte de sustancias peligrosas (SUSPEL) para toda la red de Curimón.
* **Objetivos Estratégicos:** Cero fatalidades en ruta, cumplimiento del 100% de los descansos del Art. 25 bis, control estricto de las 18 unidades SUSPEL bajo D.S. N.° 298 y erradicación de retenciones viales por sobrepeso (D.S. N.° 158).
* **Dolores Operacionales:** Responsabilidad legal personal ante fiscalizaciones por accidentes de 258 conductores externos sobre los cuales no tiene visibilidad previa; gestión manual de ~6.000 fechas vivas de vencimiento en 4 planillas Excel; y antecedentes de inmovilizaciones de camiones químicos por cursos vencidos.
* **Testimonio Representativo:** *«Después del accidente del kilómetro 312 me tocó explicarle a la autoridad cómo controlamos la jornada de un chofer externo y no tuve nada que mostrar. Los vencimientos son mi otro dolor de cabeza: como seis mil fechas vivas en cuatro planillas distintas. Prefiero frenar un viaje antes que lamentar un muerto en la carretera».*
* **Dependencias y Necesidades de Información:** Repositorio centralizado de vigencias con alertamiento escalonado (60, 30 y 7 días), bloqueo vinculante pre-despacho y trazabilidad de jornada del conductor.
* **Poder Formal / Veto:** **Alto (Potestad legal y reglamentaria de veto de despachos).**
* **Nivel de Interés:** **Máximo (Enfocado en la seguridad y cumplimiento legal).**
* **Cuadrante de Gestión:** **Cuadrante 1: Gestionar de Cerca (Gobernanza de Seguridad).**
* **Riesgo Operacional si no se Resuelve:** Siniestros fatales en ruta, clausura de faenas por la Dirección del Trabajo y querellas penales contra la plana ejecutiva.
* **Mecanismo de Interacción y Mitigación de Fricción:** Bloqueo algorítmico pre-despacho intransigible y alertas escalonadas de caducidad documental.

---

### FICHA N.° 10: Marcelo Riquelme Ibáñez y Patricio Kast Fuentealba — Jefaturas de TI y Control de Flota

* **Identificación y Emplazamiento:** Responsables de los sistemas informáticos, infraestructura de comunicaciones y monitoreo satelital de la flota en la sala central de San Bernardo, con una dotación total de 9 analistas de TI y 6 operadores de monitoreo.
* **Objetivos Estratégicos:** Garantizar la continuidad de servicios informáticos, consolidar las 3 plataformas GPS en una vista cartográfica unificada, mantener la interoperabilidad con el legado TMS 2013 y soportar la resiliencia en zonas de sombra celular.
* **Dolores Operacionales:** Monitorear 340 tractocamiones en tres sistemas comerciales que no conversan entre sí; 34 camiones fantasmas sin ningún GPS; zonas de desconexión celular de más de 80 kilómetros; y una sala de servidores de 26 m² precaria que incumple los estándares de misión crítica (RT-06).
* **Testimonio Representativo:** *«Somos seis personas mirando tres pantallas distintas con mapas que no se integran. En una ni siquiera podemos exportar datos por API. Y hay treinta y cuatro camiones que no sabemos dónde están salvo que los llamemos por teléfono. En el norte hay más de ochenta kilómetros sin señal y el camión desaparece. Nuestro TMS de 2013 sabe qué viaje encargamos, no qué viaje ocurrió».*
* **Dependencias y Necesidades de Información:** Infraestructura tecnológica escalable desacoplada de la sala local, interfaces de integración progresiva con el TMS 2013 y conectores API unificados.
* **Poder Formal / Veto:** **Alto (Viabilidad técnica y absorción de integraciones).**
* **Nivel de Interés:** **Alto (Orientado a la estabilidad informática).**
* **Cuadrante de Gestión:** **Cuadrante 3: Monitorear y Coordinar (Soporte de Arquitectura).**
* **Riesgo Operacional si no se Resuelve:** Colapso de servidores locales ante fallas eléctricas, pérdida de datos por sombras de red y fragmentación de la información de tráfico.
* **Mecanismo de Interacción y Mitigación de Fricción:** Modernización de la infraestructura transaccional de misión crítica y coexistencia gradual no disruptiva con el TMS 2013.

---

### FICHA N.° 11: Yasna Colipán Marín y Colectivo de Conductores Propios (196 Choferes)

* **Identificación y Emplazamiento:** Representa al colectivo de 196 conductores con contrato indefinido de Curimón, quienes tripulan la flota propia en rutas troncales norte y sur.
* **Objetivos Estratégicos:** Seguridad vial y personal en carretera, respeto efectivo de los descansos del Art. 25 bis, transparencia en el registro de horas de servicio, reconocimiento de las esperas en clientes y no ser forzados a interactuar con dispositivos mientras conducen.
* **Dolores Operacionales:** Alertas de fin de jornada que se disparan en tramos desérticos o cordilleranos donde no existen bermas ni estaciones de servicio seguras; esperas abusivas en clientes (> 8 horas) que degradan el descanso y no son computadas objetivamente; y resplandor o distracciones en cabina.
* **Testimonio Representativo:** *«Hay tramos en el norte donde a mí se me cumple el tiempo de manejo y no hay dónde parar en sesenta u ochenta kilómetros. No hay berma, no hay servicentro, no hay nada. Si me paro al costado de la carretera me asaltan o me choca otro camión. Manejando no puedo tocar ninguna pantalla. Y las esperas en los packings son lo peor: llegas a las siete de la mañana y te descargan a la una de la tarde, y ese tiempo nadie lo cuenta como trabajo».*
* **Dependencias y Necesidades de Información:** Alerta sonora pasiva de fin de jornada contextualizada con paraderos seguros en ruta y captura automática de tiempos de espera sin manipulación manual.
* **Poder Formal / Veto:** **Alto de facto (Rechazo operacional y seguridad de conducción).**
* **Nivel de Interés:** **Alto (Afecta su bienestar, remuneración y seguridad física).**
* **Cuadrante de Gestión:** **Cuadrante 4: Mantener Informado y Asegurar Adhesión.**
* **Riesgo Operacional si no se Resuelve:** Fatiga extrema en ruta, vuelcos con lesiones o muerte, paralización gremial y multas de la Dirección del Trabajo.
* **Mecanismo de Interacción y Mitigación de Fricción:** Cumplimiento de la Ley No Chat (síntesis de voz fuera de línea sin pantallas activas) y alertas dinámicas calculadas hacia áreas seguras de detención.

---

### FICHA N.° 12: Nolberto Sandoval Pinto y Colectivo de Transportistas Subcontratados (148 Dueños)

* **Identificación y Emplazamiento:** Representa a los 148 pequeños y medianos transportistas subcontratados (dueños de 1 a 4 camiones), quienes aportan 226 tractocamiones (60,4% de la capacidad rodante) y 258 conductores externos.
* **Objetivos Estratégicos:** Preservación de la autonomía sobre su activo patrimonial de alto valor por tractocamión, cobro oportuno y transparente de fletes y sobreestadías, certeza en pre-liquidaciones mensuales y protección de su información comercial frente a otros clientes.
* **Dolores Operacionales:** Invasión de su privacidad cuando se pretende monitorearlos fuera de los viajes de Curimón; liquidaciones manuales que tardan 9 días con un 11% de errores; cobros indebidos de combustible; y temor a que la instalación de dispositivos telemáticos sea un mecanismo de vigilancia patronal sin compensación.
* **Testimonio Representativo:** *«Cuando me dicen que me van a instalar un aparato en mi camión, yo pregunto tres cosas: quién lo paga, quién ve esa información y qué pasa cuando estoy trabajando para otro cliente. Si el aparato registra mis horas y me sirve para que me paguen rápido y demuestre que estoy en regla, bienvenido. Si es para que me vigilen todo el mes, me voy con mis camiones a otra empresa».*
* **Dependencias y Necesidades de Información:** Portal de autogestión de pre-liquidaciones, transparencia en cargos de diésel por viaje y garantía estricta de desconexión de telemetría fuera de servicio (Ley N.° 21.719).
* **Poder Formal / Veto:** **Muy Alto colectivo (Pueden desabastecer el 60,4% de la flota de Curimón).**
* **Nivel de Interés:** **Alto (Afecta directamente el flujo de caja de sus microempresas).**
* **Cuadrante de Gestión:** **Cuadrante 4: Asegurar Adhesión e Incentivo Compartido.**
* **Riesgo Operacional si no se Resuelve:** Fuga masiva de camiones hacia empresas competidoras, desabastecimiento de flota y colapso de la operación de Curimón.
* **Mecanismo de Interacción y Mitigación de Fricción:** Geocercas temporales que respetan la privacidad, equipamiento estandarizado para los 34 camiones sin GPS, y aceleración de liquidaciones a 48 horas tras viaje conforme.

---

### FICHA N.° 13: Andrea Lecaros Vives y Grandes Clientes Estratégicos (Cliente 19% y Otros 7)

* **Identificación y Emplazamiento:** Gerenta de Logística de la multinacional agroexportadora líder (representa el 19% del ingreso corporativo de Curimón, superando holgadamente el margen total de la compañía) y portavoz del grupo de los 8 clientes principales que concentran el 71% de la facturación.
* **Objetivos Estratégicos:** Visibilidad completa de su cadena de suministro de exportación, aseguramiento estricto de la cadena de frío para mercados de Norteamérica, Europa y Asia, descarbonización logística auditada bajo estándares globales y cero exposición a escándalos por trabajo ilegal de choferes en su cadena de valor.
* **Dolores Operacionales:** Incapacidad de Curimón para proveer seguimiento en tiempo real unificado; soporte de entrega en guías físicas manchadas o demoradas; imposibilidad de auditar la huella de carbono de los camiones de terceros; y el riesgo reputacional de que un embarque de exportación sea detenido por choferes sin jornada legal.
* **Testimonio Representativo:** *«Nosotros no estamos evaluando una mejora cosmética; pedimos cuatro compromisos intransigibles para la licitación de 2029: posición continua en tiempo real, digitalización documental sin papeles, certificación de jornada legal del conductor en cada viaje —incluyendo los camiones subcontratados— y auditoría de emisiones de CO2 equivalente por tonelada-kilómetro bajo el estándar internacional GLEC. No es una sugerencia, es la condición excluyente para renovar el contrato del diecinueve por ciento».*
* **Dependencias y Necesidades de Información:** APIs directas de ingesta logística, portal B2B de seguimiento satelital de temperatura y carga, emisión de e-Docs sin papel y reportería mensual auditada de gases de efecto invernadero bajo norma GLEC / ISO 14083:2023.
* **Poder Formal / Veto:** **Extremo (Comercial y Contractual).** La no renovación del contrato en 2029 destruye el resultado operacional de Curimón.
* **Nivel de Interés:** **Máximo (Condiciona su propia operación logística de exportación).**
* **Cuadrante de Gestión:** **Cuadrante 1: Gestionar de Cerca (Supervivencia del Negocio).**
* **Riesgo Operacional si no se Resuelve:** Pérdida inmediata de su cliente principal (19% de la facturación anual), comprometiendo la solvencia financiera corporativa y provocando el colapso del resultado operacional.
* **Mecanismo de Interacción y Mitigación de Fricción:** Entrega de portal cliente en tiempo real, integración documental e-Docs en Etapa 1 y motor de cálculo de emisiones GLEC basado en datos reales de telemetría CAN bus.

---

*Fin del Anexo del Subdocumento 2 — Comprensión del Problema y de la Necesidad*  
*Licitación N.° TFEP-01/2026 · Caso 10: Transportes Curimón S.A. · Proponente: audIT Soluciones Tecnológicas SpA*
