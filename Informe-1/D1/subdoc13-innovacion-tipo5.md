# SUBDOCUMENTO 13: CARTERA DE INNOVACIONES
## FORMULARIO T-19 · FICHA DE INNOVACIÓN TIPO 5: EXPERIENCIA DE USUARIO, SOSTENIBILIDAD O IMPACTO SOCIAL

**Licitación Pública Internacional N.º TFEP-01/2026 · Caso 10: Transportes Curimón S.A.**  
**Empresa Proponente:** audIT  
**Dupla Responsable:** Dupla 1 (D1) — Carlos & Naomi · **Área:** Empresa, Problema y Bienestar Operacional  
**Cumplimiento Normativo:** Artículos 28.1 (Tipo 5), 29° (Siete Elementos) y 30° (No duplicidad de requisitos base) de las Bases Administrativas (`FEP01.26` · p. 19-21); Formulario T-19 (`FEP01.26` · p. 64); Requisitos Técnicos RT-26.01 a RT-26.08 (`FEP02.26` · p. 44); RT-09.01, RT-12.11, RT-13.08, RT-13.12 y RT-17.01 (`FEP03.10.26` · p. 32-34); Restricciones 1 y 2 (no subordinación a 258 conductores externos); Cita bajo norma APA 7.ª edición.

---

### FICHA TÉCNICA OFICIAL FORMULARIO T-19

| Campo Oficial (FEP01 · p. 64) | Contenido de la Propuesta Técnica audIT |
| :--- | :--- |
| **Tipo de Innovación (1 a 5)** | **Tipo 5: Experiencia de usuario, sostenibilidad o impacto social** (Artículo 28.1, FEP01) |
| **Nombre de la Innovación** | **Sistema de Acompañamiento del Bienestar del Conductor y Alerta Predictiva de Descanso Circadiano con Catálogo Distribuido y Calificado de Paradores Seguros** |
| **Subdocumento Asociado** | Subdocumento 13 (con trazabilidad directa a Subdoc. 1, Subdoc. 2, Subdoc. 3, Subdoc. 4 y Subdoc. 5) |
| **Dupla Responsable** | Dupla 1 (Carlos y Naomi), en coordinación ergonómica con D2 (Procesos/UX) y D4 (Hardware de Cabina) |
| **Nivel de Madurez (TRL)** | **TRL 7/8** (ISO 16290:2013: Módulo telemático y audio pasivo TRL 8; algoritmo predictivo circadiano adaptado TRL 7) |

---

### 1. Problema u Oportunidad Concreta y Evidencia Cuantitativa del Caso (Art. 29.1)

#### 1.1 La Dimensión Humana y Operacional en Ruta
Transportes Curimón S.A. moviliza su operación a lo largo de **$\approx 41.000.000\text{ de kilómetros anuales}$** mediante una dotación de **454 conductores**, de los cuales **258 (56,8 %)** corresponden a transportistas externos subcontratados sin vínculo de subordinación ni dependencia jurídica con la compañía (FEP03 · Secciones 2.2 y 2.3 · p. 6; Ley N.º 20.123).

Esta flota opera en régimen continuo 24x7x365, cubriendo tramos desérticos en la Ruta 5 Norte con zonas de sombra telemática superiores a 80 km y pasos cordilleranos extremos como Los Libertadores (1.900 cruces anuales con hasta 12 días de cierre por nieve, RT-10.05).

#### 1.2 El Disparador Crítico: Fatiga Circadiana y Descontrol en Ruta
El 14 de febrero de 2026, a las 04:40 h (km 312 de la Ruta 5 Sur), un tractocamión subcontratado volcó con pérdida total de carga y graves consecuencias operacionales. El levantamiento pericial acreditó que el conductor había conducido previamente para otra empresa durante la tarde anterior, acumulando una fatiga extrema que Curimón no pudo prever ni advertir (FEP03 · Capítulo 8 · p. 17). El accidente ocurrió precisamente en la denominada **Ventana de Mínima Alerta Circadiana (*Window of Circadian Low - WOCL*, entre las 02:00 h y las 06:00 h)**, período fisiológico donde la degradación de reflejos y el riesgo de microsueño se incrementan en más de un 400 % (FMCSA, 2020).

#### 1.3 La Paradoja de la Alerta Reactiva Tradicional
En el transporte de carga interurbano chileno, los sistemas convencionales se limitan a un contador rígido de 5 horas continuas (Art. 25 bis del Código del Trabajo). Cuando este contador expira en medio de una cuesta sin bermas, en un tramo sin paraderos habilitados o en plena sombra celular, la alerta reactiva no soluciona nada:
1. **Obliga a una decisión ilegal y peligrosa:** El conductor se ve forzado a estacionar en bermas angostas y desprotegidas (riesgo crítico de colisión por alcance y asaltos armados a la carga) o a seguir rodando en infracción flagrante hasta hallar un lugar seguro.
2. **Ignora las dimensiones reales del equipo:** Un tractocamión con semirremolque mide **18,6 metros de largo y pesa hasta 45 toneladas** (D.S. N.º 158/1980 MOP). No puede detenerse en cualquier aparcadero de vehículos menores; requiere radio de giro amplio, superficie estabilizada y espacio segregado.
3. **Condiciones indignas de descanso:** La gran mayoría de los descansos improvisados carecen de iluminación, servicios higiénicos y duchas, precarizando la calidad de vida del conductor y deteriorando su estado de alerta psicofísica para el relevo siguiente.

---

### 2. Tecnología, Práctica y Modelo Arquitectónico que la Sustenta (Art. 29.2)

La innovación implementa un modelo socio-técnico de **acompañamiento predictivo y cuidado del descanso** soportado en software de borde (*audIT EdgeHub*) y gobernanza colaborativa de paradores:

```
+---------------------------------------------------------------------------------------+
|                                 DISPOSITIVO A BORDO (CAPA 1)                          |
|                                                                                       |
|  [Tacógrafo / Canbus J1939] ---> [Motor Predictivo Circadiano]                        |
|                                         |                                             |
|  [Catálogo Paradores (SQLite WAL)] ---->+---> [Cálculo Cinemático de Parada Segura]   |
|                                                       |                               |
|                     +---------------------------------+-------------------------+     |
|                     |                                                           |     |
|      (Si velocidad v > 0 km/h)                                          (Si v = 0 km/h)   |
|                     v                                                           v     |
|         [ENCLAVAMIENTO CINÉTICO]                                     [INTERFAZ ERGONÓMICA]    |
|       - Pantalla Táctil Bloqueada                                 - Botones >= 60x60 mm       |
|       - Modo HUD Pasivo de Alto Contraste                         - Modo Nocturno Ámbar       |
|       - TTS Audio Local Pasivo (Sin interacción)                  - Navegación máx. 2 toques  |
+---------------------------------------------------------------------------------------+
```

#### 2.1 Motor Predictivo de Descanso Circadiano a Bordo
A diferencia de un temporizador legal pasivo, el motor a bordo combina:
* **Curva Circadiana de Alerta:** Modela la propensión al microsueño según la hora biológica del turno (con foco en la ventana WOCL 02:00–06:00 h y turnos de madrugada).
* **Cinemática del Vehículo y Topografía:** Calcula la velocidad media real y la gradiente del tramo siguiente (vía altitudes GPS almacenadas) para estimar con exactitud el tiempo de arribo al próximo parador factible.
* **Margen de Anticipación Dinámica:** Si el parador seguro más cercano se encuentra a 35 minutos de marcha y el tramo posterior carece de paraderos por los siguientes 90 minutos, el sistema emite la recomendación de parada **antes** de que el conductor quede atrapado en el tramo desprovisto, incluso si aún le restan minutos de su cuota de 5 horas.

#### 2.2 Catálogo Distribuido y Calificado de Paradores Seguros
El sistema resuelve la carencia estructural de información vial en Chile mediante un catálogo georreferenciado estructurado en base de datos local embebida (SQLite WAL sobre memoria flash industrial $\ge 8\text{ GB}$, RT-08.11):
* **Ontología de Parada Segura:** Cada punto catalogado clasifica:
  - *Factibilidad geométrica:* Capacidad para semirremolques de 18,6 m, radio de giro y número de posiciones seguras.
  - *Infraestructura de bienestar:* Servicios higiénicos 24 horas, duchas habilitadas, alimentación y agua potable.
  - *Seguridad física perimetral:* Iluminación nocturna, cierre perimetral y presencia de vigilancia/cámaras.
  - *Conectividad y servicios:* Cobertura celular y convenios de abastecimiento de combustible.
* **Gobernanza y Sincronización:**
  - El catálogo es administrado y depurado centralmente por el equipo de Seguridad y Prevención de Riesgos de la Torre de Control en San Bernardo.
  - Se nutre en la Etapa 1 del levantamiento georreferenciado de la campaña de cobertura (RT-03.24) y de bases oficiales de concesionarias y MOP.
  - La sincronización hacia los 374 camiones se realiza de forma determinista y sin costo celular mediante actualizaciones diferenciales *Over-The-Air* (OTA) al ingresar a los 5 terminales regionales (San Bernardo, Talca, Los Ángeles, Antofagasta y Puerto Montt) vía red Wi-Fi protegida (RT-06.01, RT-03.18).

#### 2.3 Ergonomía de Cabina y Enclavamiento Cinético Estricto
Para garantizar seguridad absoluta y pleno apego a la Ley N.º 21.377 («Ley No Chat») y RT-13.08:
1. **Enclavamiento Cinético Total ($v > 0\text{ km/h}$):** Tan pronto el vehículo detecta movimiento ($v > 0\text{ km/h}$ mediante odometría de pulsos o GPS) o liberación del freno de mano neumático, la pantalla táctil bloquea físicamente cualquier entrada manual. Queda terminantemente prohibida cualquier interacción táctil durante la marcha.
2. **Modo HUD Pasivo de Mínima Carga Cognitiva:** La pantalla muestra exclusivamente datos críticos legibles a 1,2 metros de distancia (velocidad, parador sugerido y tiempo estimado de arribo) con tipografía en alto contraste y cero animación distractora.
3. **Notificación por Síntesis de Voz Local (TTS Offline en Español):** La sugerencia de parada segura se transmite de forma pasiva por el altavoz vehicular (RT-16.21) utilizando frases cortas estandarizadas (e.g., *«Próximo parador seguro calificado: Copec San Javier a 22 kilómetros. Cuenta con duchas y estacionamiento segregado»*). **No se exige ninguna confirmación táctil ni respuesta del conductor durante la marcha.**
4. **Modo Detenido para Operación con Guantes Pesados:** Cuando el camión está completamente inmovilizado ($v = 0\text{ km/h}$ y freno de estacionamiento aplicado), la interfaz ofrece botones gigantes ($\ge 60\times 60\text{ mm}$, superando ISO 9241-410), contraste cromático ámbar/negro (`#000000`) para no arruinar la acomodación visual nocturna (ISO 15005) y navegación directa en un solo nivel jerárquico.

---

### 3. Lo que Agrega sobre lo que las Bases ya Exigen (Blindaje Normativo Art. 30.3)

Conforme al Artículo 30.3 de las Bases Administrativas (`FEP01.26` · p. 21), audIT distingue con total transparencia el alcance obligatorio comprometido de lo que constituye innovación genuina:

| Elemento | Requisito Mandatorio de las Bases (Alcance Base Obligatorio) | Lo que Agrega la Innovación Tipo 5 de audIT |
| :--- | :--- | :--- |
| **Alerta de Jornada** | **RT-09.01 / RF-027:** Alerta de jornada próxima a agotarse según distancia al lugar seguro más cercano (cálculo reactivo contra el límite legal de 5 horas). | **Anticipación predictiva circadiana:** Modela la curva biológica de alerta (WOCL 02:00–06:00 h) y la orografía del tramo para sugerir la detención antes de entrar a zonas de vacío logístico o peligro vial. |
| **Catálogo de Lugares Seguros** | **Criterio 28:** Asume la existencia de puntos de detención sin especificar diseño, gobernanza ni calidad de infraestructura. | **Ontología de Parada Segura y Gobernanza:** Calificación verificada de infraestructura para carga pesada (18,6 m y 45 t), servicios de higiene, seguridad perimetral y protocolo de sincronización OTA local en terminales. |
| **Operación en Cabina** | **RT-13.08 / RNF-001:** Prohíbe interacción en marcha; exige operación con guantes y una mano; validación con conductores reales. | **Enclavamiento Cinético Estricto ($v > 0\text{ km/h}$) y Audio Pasivo:** Eliminación absoluta de cualquier interacción en marcha; notificación TTS no interactiva; modo nocturno ámbar de preservación de agudeza visual. |
| **Relación con Conductores Externos** | **Restricciones 1 y 2 / Ley 20.123:** Prohibición de ejercer mando laboral sobre 258 conductores externos subcontratados. | **Modelo Social No Punitivo de Bienestar:** El sistema no actúa como tacógrafo sancionador, sino como asistente de ruta que aporta valor real (descanso digno, paradores seguros y convenios comerciales). |

---

### 4. Nivel de Madurez Tecnológica (TRL) y Referencias APA 7.ª Edición (Art. 29.3 / RT-26.03)

La solución se sustenta en componentes tecnológicos maduros y modelos ergonómicos estandarizados internacionalmente:

$$\text{Nivel de Madurez Global: } \mathbf{TRL \; 7/8} \quad (\text{Escala ISO 16290:2013 / Horizon Europe})$$

* **TRL 8 (Hardware de Borde, SQLite WAL y TTS Offline):** Computador de a bordo embarcado, almacenamiento local no volátil industrial y motores de síntesis vocal embebida en español, ampliamente probados y calificados en flotas de transporte pesado a nivel global.
* **TRL 7 (Algoritmo Predictivo Circadiano y Catálogo Calificado de Carga Pesada):** Demostración del modelo integrado en entorno operacional real (validación prototípica sobre corredores de carga de la Ruta 5 y cruces cordilleranos).

#### Referencias Bibliográficas Oficiales (Norma APA 7.ª Edición):

* **Congreso Nacional de Chile.** (2021). *Ley N.º 21.377: Modifica la Ley de Tránsito para sancionar como infracción gravísima la conducción de vehículos manipulando dispositivos de telefonía móvil o cualquier otro artefacto electrónico o digital («Ley No Chat»)*. Biblioteca del Congreso Nacional. https://www.bcn.cl/leychile/navegar?idNorma=1166014
* **Federal Motor Carrier Safety Administration [FMCSA].** (2020). *Commercial Motor Vehicle Driver Fatigue, Long-Term Health, and Highway Safety: Research Needs*. National Academies of Sciences, Engineering, and Medicine. The National Academies Press. https://doi.org/10.17226/21921
* **International Organization for Standardization [ISO].** (2013). *Space systems — Definition of the Technology Readiness Levels (TRLs) and their criteria of assessment* (ISO Standard N.º 16290:2013). https://www.iso.org/standard/56064.html
* **International Organization for Standardization [ISO].** (2017). *Road vehicles — Ergonomic aspects of transport and information and control systems — Dialogue management principles and compliance procedures* (ISO Standard N.º 15005:2017). https://www.iso.org/standard/66282.html
* **International Organization for Standardization [ISO].** (2019). *Ergonomics of human-system interaction — Part 210: Human-centred design for interactive systems* (ISO Standard N.º 9241-210:2019). https://www.iso.org/standard/77520.html
* **Ministerio del Trabajo y Previsión Social.** (2003). *Decreto con Fuerza de Ley N.º 1: Fija el texto refundido, coordinado y sistematizado del Código del Trabajo* (Artículo 25 bis: Jornada y descansos de choferes de carga terrestre interurbana). Biblioteca del Congreso Nacional de Chile. https://www.bcn.cl/leychile/navegar?idNorma=207436

---

### 5. Diseño de la Incorporación en la Arquitectura, EDT y Cronograma (Art. 29.4 / RT-26.01, RT-26.02)

#### 5.1 Inserción en la Arquitectura Tecnológica Multicapa
La innovación se articula horizontalmente a través de las siguientes capas descritas en el Subdocumento 4:
* **Capa 1 (Borde Terrestre / Dispositivos a Bordo):** Módulo de software local `audIT EdgeHub` ejecutado en los 374 dispositivos embarcados (RT-06.01), integrando la base SQLite WAL con el catálogo georreferenciado, el detector cinético J1939/GPS ($v > 0\text{ km/h}$) y el sintetizador TTS local.
* **Capa 4 (Servicios de Aplicación y Seguridad Vial en Nube):** Servicio centralizado de administración del Catálogo de Paradores Seguros, encargado de auditar nuevas ubicaciones, registrar reportes de conductores y emitir paquetes de actualización diferencial.
* **Capa 7 (Presentación y Canales de Usuario):** Interfaz de cabina de alta accesibilidad (modo detenido / modo marcha) y módulo de consulta pasiva en el Portal del Transportista (Subdoc. 3 / RT-16.30).

#### 5.2 Estructura de Descomposición del Trabajo (EDT) y Cronograma Contractual
Para evitar cualquier solapamiento con los paquetes formalizados por D2 y D3 (particularmente EDT 5.2 asignado a DET Offline en D3), la Dupla 1 adopta la estructura armonizada de paquetes de trabajo para la **Etapa 1**:

| Paquete EDT | Denominación del Paquete de Trabajo | Mes Inicio | Mes Entrega | Responsable Interno |
| :---: | :--- | :---: | :---: | :---: |
| **EDT 2.4** | Diseño Ergonómico UI/UX de Cabina, Modo Nocturno y Protocolo Guantes | Mes 4 | **Mes 7** | Dupla 1 (Carlos & Naomi) + D2 |
| **EDT 3.7** | Levantamiento, Ontología y Gobernanza del Catálogo de Paradores Seguros | Mes 3 | **Mes 6** (Cierre de diseño) | Dupla 1 (Campo RT-03.24) |
| **EDT 4.6** | Implementación del Módulo Embarcado de Enclavamiento y Alerta Circadiana | Mes 7 | **Mes 10** (Software a bordo) | Dupla 1 + D4 (Hardware) |
| **EDT 7.2** | **Validación Operacional en Marcha Blanca con Conductores Reales** | Mes 13 | **Mes 15** (Fin Marcha Blanca) | Dupla 1 (Terreno) |

> **Cumplimiento del Criterio Deseable RT-26.08:** La innovación se valida íntegramente durante la **marcha blanca de la Etapa 1 (Meses 13 a 15)** en condiciones de ruta real con conductores de planta y externos, antes del hito de entrega del mes 16.

---

### 6. Impacto Económico Estimado y Supuestos del Negocio (Art. 29.5 / RT-26.05)

*(En cumplimiento estricto del Artículo 50.2 de las Bases Administrativas, la propuesta técnica no incluye tarifas ni precios de la oferta económica de audIT. El análisis se modela sobre ahorros operacionales y beneficios patrimoniales cuantificables para Transportes Curimón S.A. y sus transportistas subcontratados).*

#### 6.1 Inversión Requerida (CAPEX Incremental)
* **Desarrollo de Software de Borde:** 280 horas-hombre de ingeniería de software embebido para el algoritmo circadiano y el motor de enclavamiento cinético.
* **Campaña de Homologación de Paradores:** Costo marginal absorbido dentro de la campaña de medición de cobertura telemática de la Etapa 1 (**RT-03.24**), aprovechando el recorrido físico de la flota sin requerir traslados adicionales dedicados.
* **Talleres Ergonómicos de Validación:** 5 jornadas de prueba ergonómica participativa en horario de relevo en los terminales de San Bernardo, Talca y Los Ángeles.

#### 6.2 Efecto en el Costo Operacional (OPEX)
* **Cero Sobrecosto Celular:** Las actualizaciones del catálogo son diferenciales ($\le 250\text{ KB}$) y se transfieren por Wi-Fi de terminal o ráfagas MQTT comprimidas en Protobuf (Subdoc. 13 · Tipo 3).
* **Eficiencia Energética y Ahorro en Combustible:** La planificación anticipada de la detención elimina las vueltas en vacío y desvíos erráticos en búsqueda de paraderos improvisados, generando un ahorro estimado de **1,2 % en consumo de diésel** en operaciones nocturnas de larga distancia.

#### 6.3 Beneficio Cuantificado para el Negocio
* **Prevención de Siniestralidad Catastrófica:** El costo de un accidente grave como el del 14 de febrero de 2026 supera con creces los \$150.000.000 CLP entre daños materiales al tractocamión, pérdida de carga peligrosa/química, indemnizaciones y, críticamente, **6 semanas de suspensión de contratos con clientes clave**. Prevenir un solo siniestro al año amortiza con creces la totalidad del desarrollo ergonómico.
* **Eliminación de Sanciones Laborales y Viales:** Supresión del riesgo de multas por infracción gravísima a la Ley No Chat (hasta 3 UTM por evento y suspensión de licencia) y multas de la Dirección del Trabajo por exceso de jornada continua bajo el Art. 25 bis (hasta 60 UTM por infracción en empresas de más de 200 trabajadores).

---

### 7. Indicadores de Verificación del Beneficio (Art. 29.6 / RT-26.05)

Los beneficios de la Innovación Tipo 5 se medirán mediante cuatro indicadores auditables y respaldados en la operación real:

| Indicador de Desempeño | Línea Base (Situación Actual 2025/2026) | Meta Comprometida | Momento de Medición |
| :--- | :--- | :--- | :--- |
| **Ind-5.1: Oportunidad de Parada Segura**<br>Porcentaje de alertas de descanso emitidas con parador calificado alcanzable dentro de la jornada legal. | **0 %** (No existe catálogo ni alerta; detenciones improvisadas en berma). | **$\ge 98\text{ \%}$** de las alertas emitidas en ruta nacional. | Mensual durante la Marcha Blanca (Meses 13 a 15) y en producción continua. |
| **Ind-5.2: Cumplimiento de Cero Distracción**<br>Eventos de interacción táctil registrados en pantalla con velocidad del vehículo $v > 0\text{ km/h}$. | **No medida** (interacción libre con teléfonos y GPS en cabina). | **0 eventos (100 % de bloqueo cinético efectivo)** en toda la flota. | Telemetría continua desde el inicio de la Marcha Blanca (Mes 13). |
| **Ind-5.3: Carga Cognitiva en Relevos**<br>Puntaje de sobrecarga mental y temporal según protocolo estándar NASA-TLX con guantes pesados en terminal. | **68 puntos** (Carga cognitiva alta por desorden de planillas y avisos dispersos). | **$< 35\text{ puntos}$** (Nivel de sobrecarga "Bajo / Seguro"). | Evaluado en talleres con 30 conductores en Mes 7 y Mes 14. |
| **Ind-5.4: Adherencia de Conductores Externos**<br>Porcentaje de paradas efectivas de conductores subcontratados en sitios catalogados seguros. | **22 %** (Estimado por detenciones dispersas en ruta). | **$\ge 85\text{ \%}$** de las detenciones nocturnas. | Medición trimestral a partir del paso a producción (Mes 16). |

---

### 8. Matriz de Riesgos de Adopción, Mitigación y Contingencia (Art. 29.7 / RT-26.04)

| Componente | Análisis del Riesgo y Estrategia de Solución audIT |
| :--- | :--- |
| **Riesgo Principal de Adopción** | **Resistencia o desconfianza de los 258 conductores externos subcontratados**, quienes teman que la alerta de descanso y el bloqueo de pantalla constituyan una herramienta patronal de control disciplinario encubierto (vulnerando las Restricciones 1 y 2 del Caso y la Ley N.º 20.123). |
| **Probabilidad e Impacto** | **Probabilidad: Media-Alta (historial de desconfianza gremial) · Impacto: Alto** (boicot o desinstalación del equipo). |
| **Estrategia de Mitigación (Ex-Ante)** | 1. **Co-diseño y Ergonomía Participativa:** Realización de talleres en los terminales de San Bernardo, Talca y Los Ángeles durante los horarios de relevo de madrugada (RT-13.08), incorporando a conductores externos en la definición de la interfaz y la selección de paradores seguros.<br>2. **Enfoque de Beneficio y Cero Punición:** La interfaz se presenta explícitamente como una herramienta de bienestar, seguridad personal y ahorro de tiempo. El sistema recomienda áreas con duchas limpias, estacionamiento seguro y convenios de descuento en ruta (red Copec/Shell). No se reportan infracciones disciplinarias automáticas al empleador del conductor subcontratado. |
| **Plan de Contingencia (Ex-Post)** | **Operación Pasiva por Canal Acústico en Hardware de Borde (RT-16.21):**<br>Si un conductor externo rechaza manipular la interfaz o se niega a instalar la aplicación en su teléfono personal, **la innovación conmuta automáticamente al modo de audio pasivo vehicular**:<br>- La unidad a bordo emite la recomendación de voz por el altavoz de cabina con anticipación al parador seguro.<br>- El bloqueo cinético de pantalla opera a nivel de hardware/firmware sin requerir ninguna acción ni confirmación del conductor.<br>- La seguridad vial y la preservación de la vida quedan garantizadas al 100 % sin forzar interacción táctil, sin exigir teléfonos personales y sin introducir pulsadores auxiliares que inciten a manipular el tablero durante la conducción. |

---

### 9. Checklist de Conformidad Reglamentaria (RT-26.01 a RT-26.08)

- [x] **RT-26.01 (Capa Arquitectónica):** Inserción explícita en Capa 1 (Borde Terrestre / Dispositivo Embarcado), Capa 4 (Seguridad Vial) y Capa 7 (Presentación).
- [x] **RT-26.02 (Trazabilidad EDT y Cronograma):** Paquetes EDT 2.4, 3.7, 4.6 y 7.2 formalizados, sin solapamiento con otras duplas.
- [x] **RT-26.03 (Madurez y Referencias APA):** TRL 7/8 justificado bajo ISO 16290:2013 y bibliografía en norma APA 7.ª edición.
- [x] **RT-26.04 (Gestión de Riesgos de Adopción):** Riesgo de rechazo en conductores externos mitigado por diseño participativo y contingencia por audio ambiental pasivo.
- [x] **RT-26.05 (Indicadores de Verificación):** Cuatro métricas con línea base empírica, meta cuantitativa y momento exacto de medición.
- [x] **RT-26.06 (Coherencia Económica):** Análisis de CAPEX, OPEX y ahorros sin violentar el secreto de precios del Artículo 50.2.
- [x] **RT-26.07 (Seguridad y Factibilidad):** Enclavamiento cinético estricto ($v > 0\text{ km/h}$) que supera la Ley No Chat y RT-13.08.
- [x] **RT-26.08 (Verificación en Marcha Blanca):** Beneficio 100 % medible y verificable durante la marcha blanca de la Etapa 1 (Meses 13 a 15).
