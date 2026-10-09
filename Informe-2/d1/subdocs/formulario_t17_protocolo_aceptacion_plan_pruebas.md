# Formulario T-17

**Entregables de cada hito y del producto final..**  La secuencia de actividades, dependencias y evidencias por hito se articula con la estructura canónica de la EDT de 13 elementos y 54 paquetes de trabajo (con especial foco en el elemento 10 «Calidad y pruebas», paquetes 10.1 a 10.4) y el cronograma contractual de actividades A01 a A25 de S7 (Formularios T-14, T-15 y T-18). La verificación integral de la Etapa 1 se concentra en la actividad A12 (meses 10 a 12), la certificación de la Etapa 2 en la actividad A22 (meses 17 a 18), y los ejercicios semestrales de recuperación ante desastres (DR) se programan en junio y noviembre de cada año operacional (M21 a M56); véanse sección 9.3.1 y sección 9.3.2.

  **Criterios de aceptación objetivos..**  Se aplican la disponibilidad mínima de 99,9 % (FEP01, Artículo 20, p. 14), RTO máximo de 4 h y RPO máximo de 15 min (FEP02, RT-07.04, p. 17), y retención local mínima de 72 h (Caso, RT-03.10, p. 31); véase también sección 9.1.2 y sección 9.2.2. Los demás umbrales se aprueban y documentan antes de ejecutar las pruebas.

  **Evidencia requerida..**  Cada evidencia registra requisito y caso, fecha, versión, ambiente, datos y parámetros, herramienta, resultado, defectos y responsable; véase sección 9.3.4.

  **Plazos de revisión..**  Diez días hábiles de revisión y diez de subsanación. La segunda presentación con observaciones de igual naturaleza constituye atraso imputable (FEP01, Artículo 18.3, p. 13); véase sección 9.3.1.

  **Procedimiento de observaciones..**  Las observaciones se registran con identificador, requisito relacionado, severidad, evidencia y respuesta; la subsanación se revisa contra el criterio aprobado y sin aceptación por silencio y con acta suscrita; véase sección 9.3.3.

  **Acta de conformidad..**  El cierre registra el hito y versión evaluados, casos ejecutados y su estado, defectos abiertos, métricas efectivamente medidas, evidencias y pronunciamiento de la contraparte; véase sección 9.3.3.

  **Estado del catálogo de pruebas..**  El catálogo contiene 120 casos diseñados (25 unitarios, 25 de integración, 20 de sistema, 20 no funcionales y de seguridad, 15 HIL y 15 UAT), con trazabilidad diseñada hacia los 42 requerimientos del sistema formalizados en el Formulario T-12 (28 funcionales RF-001 a RF-028 y 14 no funcionales RNF-001 a RNF-014) y sus paquetes EDT asociados. La matriz distingue cobertura diseñada de evidencia ejecutada; no afirma probar todos los 54 paquetes. No se declaran ejecutados ni aprobados. Los escenarios sintéticos y umbrales adicionales se fijan antes de ejecutar. Catálogo: \hyperref[sec:9-catalogo]{Catálogo detallado}, folio \pageref{sec:9-catalogo}.

Véanse los mínimos en sección 9.3.6 y las seis condiciones acumulativas y calendario en sección 9.3.5.

### 9.0.1 Catálogo de 120 casos diseñados

Este catálogo conserva los identificadores por batería. No se declara ejecución ni aprobación. Para cada ensayo se registra fixture, reloj/semilla, versión/configuración, script, oráculo, resultado, incidencias y evidencia. Los 120 casos se cotejan con 42 requerimientos del Formulario T-12: 28 funcionales RF-001 a RF-028 y 14 no funcionales RNF-001 a RNF-014. La matriz siguiente distingue la referencia de la comprobación diseñada. No se declara cobertura ejecutada ni verificación de los 54 paquetes EDT por el solo número de casos. Los criterios contractuales de S9 prevalecen; parámetros restantes son propuestas de ingeniería que se fijan antes de ejecutar. Las marcas, herramientas, interfaces, versiones y dispositivos mencionados en fixtures son configuraciones propuestas de ensayo, sujetas a la arquitectura homologada; no se atribuyen a los activos existentes del mandante. Antes de ejecutar se congela el manifiesto de datos, reloj, semilla, geometrías, señales, parámetros y configuración y se documenta el script correspondiente. Ningún objetivo de microsegundos, milisegundos, precisión térmica o concurrencia amplía una obligación normativa por el solo hecho de aparecer aquí. Toda condición aplicable debe cumplirse: cualquier incumplimiento implica Fail. Un servicio externo se prueba con doble controlado y posteriormente con el proveedor homologado, conservando permisos y configuración.

### 9.0.2 Matriz de requisitos, casos y alcance de verificación

La Tabla 9.2 recorre el catálogo de S3/T-12 y localiza las variantes diseñadas en los casos existentes. El detalle de cada variante establece entradas, salidas y límites. Se verifica conjuntamente la familia de pruebas: un mock no acredita proveedor real, una simulación temporal no acredita años operados y un examen documental no acredita conformidad externa. Todas las filas están diseñadas y pendientes de ejecución; la cobertura de código se mide separadamente.

**Tabla 9.1.** Trazabilidad del catálogo S3/T-12 a pruebas diseñadas

| Requisito | Casos existentes | Paquete EDT | Comprobación diseñada | Estado |
|---|---|---|---|---|
| RF-001 | CP-UNIT-01, CP-SYS-01, CP-HW-14, CP-PERF-04 | 5.3 | Preparar seis asignaciones con los cuatro factores presentes: fuentes de jornada 1, 2, 3, 4, 5 y ninguna | Diseñada; no ejecutada |
| RF-002 | CP-UNIT-02, CP-INT-02 | 5.1 | Construir un padrón sintético de 454 conductores identificados, 196 propios y 258 externos; asociar a cada tramo origen, conductor, vehículo y nivel 1–5, con muestras de todas las fuentes y ausencia de fuente | Diseñada; no ejecutada |
| RF-003 | CP-INT-03, CP-SYS-05, CP-HW-14 | 5.1, 9.2 | Crear dos conductores externos con igual viaje propuesto y jornadas previas distintas: descanso continuo de 8 h y de 6 h en la ventana de 24 h del fixture | Diseñada; no ejecutada |
| RF-004 | CP-UNIT-06, CP-SEC-08 | 5.1 | Sellar un evento original y una corrección que cambia un dato; conservar ambas versiones con autor, origen y fecha | Diseñada; no ejecutada |
| RF-005 | CP-UNIT-01, CP-SYS-08 | 5.1, 7.1 | Generar 6.000 vigencias sintéticas con titular, responsable, fecha y respaldo | Diseñada; no ejecutada |
| RF-006 | CP-UNIT-19, CP-SYS-06 | 5.5 | Preparar 18 unidades SUSPEL sintéticas, cada una con carga efectiva, DET emitido por ERP, conductor y lista firmada | Diseñada; no ejecutada |
| RF-007 | CP-HW-15, CP-INT-21 | 6.3 | Descargar dos archivos originales de tacógrafo con conductores y vehículos distintos; conservar bytes y huellas originales, relacionar conductor y vehículo y clasificar nivel 1 | Diseñada; no ejecutada |
| RF-008 | CP-SYS-16, CP-UAT-01 | 5.4, 6.2 | Construir 374 unidades únicas, 148 propias y 226 externas, con muestras de todas las fuentes y marcas de tiempo conocidas | Diseñada; no ejecutada |
| RF-009 | CP-HW-03, CP-PERF-02 | 4.1 | Desconectar 72 h con el perfil versionado de CP-PERF-02, reiniciar equipo y reconectar | Diseñada; no ejecutada |
| RF-010 | CP-UNIT-08, CP-SYS-03 | 5.4 | Versionar 1.400 polígonos y puntos de entrada, límite interior y exterior en el mismo sistema de coordenadas; ejecutar replay automático | Diseñada; no ejecutada |
| RF-011 | CP-UNIT-12, CP-SYS-03 | 5.5 | Usar un contrato sintético con 120 min libres y bloques facturables de 30 min, permanencias de 119, 120 y 330 min | Diseñada; no ejecutada |
| RF-012 | CP-SYS-04, CP-INT-20 | 5.5 | Emitir e-POD con receptor identificado, fecha, viaje y conformidad, primero con conectividad y después sin ella | Diseñada; no ejecutada |
| RF-013 | CP-INT-11, CP-INT-12 | 6.1 | Solicitar al ERP un DET desde una orden válida y repetir la misma clave con timeout y respuesta tardía | Diseñada; no ejecutada |
| RF-014 | CP-UNIT-21, CP-HW-11 | 6.1, 4.1 | Ejecutar dos rutas de contingencia: DET anticipado por ERP desde la orden y datos enviados por enlace satelital al ERP con folio de vuelta al vehículo | Diseñada; no ejecutada |
| RF-015 | CP-UNIT-15, CP-SYS-09 | 8.2 | Usar las dos ofertas de retorno del fixture de CP-UNIT-15 con márgenes analíticos 970 y 780, en unidades sintéticas ajenas a precios de oferta | Diseñada; no ejecutada |
| RF-016 | CP-INT-23, CP-SYS-15 | 5.6, 2.5 | Entregar dos viajes cerrados con factura de combustible tardía en uno | Diseñada; no ejecutada |
| RF-017 | CP-INT-23, CP-SYS-10 | 5.6 | Usar un viaje propio y uno de tercero con los mismos tipos de componentes conocidos | Diseñada; no ejecutada |
| RF-018 | CP-INT-18, CP-PERF-09 | 8.5 | Construir 12 meses de consumo y kilómetros por vehículo, ruta y conductor con condiciones registradas | Diseñada; no ejecutada |
| RF-019 | CP-INT-24, CP-SYS-10 | 5.6 | Cerrar un mes para 148 transportistas sintéticos, con viajes, tarifas y descuentos de referencia | Diseñada; no ejecutada |
| RF-020 | CP-SEC-07, CP-PERF-10 | 5.7 | Autenticar dos propietarios y solicitar viajes y liquidaciones propios y ajenos durante el cierre de 148 titulares | Diseñada; no ejecutada |
| RF-021 | CP-SYS-19, CP-PERF-07 | 8.1 | Con permiso por cliente, viaje y ventana, publicar posición cuya antigüedad se conoce | Diseñada; no ejecutada |
| RF-022 | CP-SEC-04, CP-SEC-05 | 5.7 | Crear permisos por propietario, dato, vehículo, destinatario y vigencia; conceder y revocar uno a hora fija | Diseñada; no ejecutada |
| RF-023 | CP-UNIT-09, CP-SYS-17 | 8.3 | Calcular emisiones mensuales de una muestra propia y otra externa con factores versionados, actividad y toneladas-kilómetro de referencia | Diseñada; no ejecutada |
| RF-024 | CP-INT-17, CP-UAT-02 | 8.4 | Registrar una intervención offline de taller externo con técnico, equipo, fecha, odómetro, trabajo, repuestos y evidencia; reconectar dos veces | Diseñada; no ejecutada |
| RF-025 | CP-UNIT-14, CP-HW-04 | 8.4, 6.4 | Configurar mantenimiento a 100.000 km como dato sintético, no norma | Diseñada; no ejecutada |
| RF-026 | CP-SYS-05, CP-UAT-09 | 9.2, 5.2 | Calcular los ocho indicadores mensuales de adhesión de S3 con sus denominadores | Diseñada; no ejecutada |
| RF-027 | CP-UNIT-18, CP-HW-06 | 4.1, 5.1 | Reproducir conducción acumulada 4 h 15 min y área segura alcanzable en 35 min: alertar antes de agotar cinco horas con diez minutos de holgura | Diseñada; no ejecutada |
| RF-028 | CP-SYS-05, CP-UAT-09 | 5.3 | Crear transportistas en modalidades completa, de datos y sin adhesión según S3; comprobar nivel 2, reposo de nivel 4 con atestación de nivel 5 y validación documental con y sin atestación firmada; visualizar modalidad, fuente, nivel y veredicto por separado | Diseñada; no ejecutada |
| RNF-001 | CP-UNIT-11, CP-HW-06 | 4.1 | Reproducir velocidad cero y velocidad positiva; intentar escritura, formulario y confirmación en ambos estados | Diseñada; no ejecutada |
| RNF-002 | CP-UNIT-23, CP-HW-03 | 4.1 | Repetir el conjunto de 72 h sin red, reinicios y reenvío de cada lote dos veces | Diseñada; no ejecutada |
| RNF-003 | CP-INT-07, CP-INT-08 | 6.2 | Conservar inventario de equipos GPS de terceros y permisos de dos propietarios | Diseñada; no ejecutada |
| RNF-004 | CP-UAT-02, CP-HW-08 | 4.2 | Usar agenda de visitas normales a terminal y órdenes de instalación; cada instalación se integra a una visita existente sin viaje adicional ni inmovilización extra | Diseñada; no ejecutada |
| RNF-005 | CP-UNIT-16, CP-HW-04 | 4.1, 6.3 | Medir con analizador independiente el bus durante lectura y reinicio del equipo: cero tramas transmitidas por audIT | Diseñada; no ejecutada |
| RNF-006 | CP-INT-12, CP-INT-11 | 6.1 | Repetir solicitud, timeout, reenvío y recuperación de respuesta con la misma clave de orden | Diseñada; no ejecutada |
| RNF-007 | CP-UNIT-08, CP-SYS-03 | 5.4 | Ejecutar detección de entrada, salida y espera con inventario de instalaciones de cliente vacío para componentes audIT | Diseñada; no ejecutada |
| RNF-008 | CP-HW-03, CP-PERF-02 | 4.1, 3.4 | Ensayar 288 h separadamente como compromiso propuesto para cierres fronterizos: cuatro repeticiones del perfil de 72 h, 23.816 registros y 12.950.624 bytes brutos por unidad antes de overhead | Diseñada; no ejecutada |
| RNF-009 | CP-SYS-16, CP-UAT-01 | 13.1, 11.4 | Con la dotación cliente de nueve personas, ejecutar altas, consulta de salud y escalamiento con cuentas limitadas; comparar matriz de responsabilidad con manual | Diseñada; no ejecutada |
| RNF-010 | CP-PERF-08, CP-SYS-01 | 1.1 | Conciliar inventario técnico y modelo económico de 36 meses: cantidades, unidades, periodicidad y cobertura de nube, enlaces, licencias, soporte, reposición, retiro y contingencia | Diseñada; no ejecutada |
| RNF-011 | CP-INT-05, CP-SYS-05 | 11.2 | Durante convivencia TMS 2013/nuevo sistema, desviar por función y repetir una misma orden por ambas rutas; esperar un solo viaje y ningún despacho que eluda bloqueo | Diseñada; no ejecutada |
| RNF-012 | CP-SEC-08, CP-UNIT-07 | 5.1 | Crear evidencia con autor, origen, fecha y contenido; añadir corrección como registro nuevo | Diseñada; no ejecutada |
| RNF-013 | CP-SEC-04, CP-SEC-05 | 3.2 | Inventariar atributos que requieren protección y roles autorizados; leerlos desde disco y mediante API con rol permitido y ajeno | Diseñada; no ejecutada |
| RNF-014 | CP-SEC-08, CP-INT-25 | 7.3 | Versionar dominios y plazos: jornada cinco años, documentos/viajes/liquidación seis, siniestros diez, habilitación vigencia más cinco, SUSPEL cinco, esperas tres, series dos en línea con agregación | Diseñada; no ejecutada |

### 9.0.3 Batería 1: Pruebas unitarias (25 casos)

Esta batería comprueba las reglas individuales mediante fixtures controlados y resultados esperados reproducibles.

#### 9.0.3.1 CP-UNIT-01 — Algoritmo de Asignación Bloqueante Pre-Despacho (4 Factores Síncronos)

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-UNIT-01`
**Nivel y Tipología:** Prueba Unitaria Automatizada / Lógica de Negocio y Enclavamiento Bloqueante.
**Requerimiento Trazado:** RF-001, RF-005.
**Precondiciones:**
- Instancia mock del motor de asignación inicializada en memoria.
- Tablas hash en Redis pobladas con perfiles de choferes, equipos, vigencias y cargas.

**Pasos de Ejecución:**
- Invocar la función pura `validatePreDispatchAssignment(candidateAssignment)`.
- Ejecutar secuencialmente las 4 comprobaciones: (a) Jornada disponible Art. 25 bis, (b) 6.000 vigencias vivas (licencia, revisión técnica, seguro), (c) Aptitud mecánica del tracto/rampla, (d) Compatibilidad de carga SUSPEL/frío.
- Medir el tiempo de ejecución de la rutina de validación.
- Evaluar la respuesta devuelta por la función.

**Datos de Entrada Sintéticos:**
\begin{quote}\ttfamily
  {
    "orderId": "OT-SYNTH-2026-0001",
    "driverId": "DRV-SYNTH-101",
    "truckId": "TRK-SYNTH-042",
    "trailerId": "TRL-SYNTH-015",
    "cargoType": "GENERAL_CARGO",
    "driverStatus": {"drivingHoursToday": 3.5, "continuousDrivingHours": 3.5, "licenseValidUntil": "2027-05-10"},
    "truckStatus": {"technicalInspectionValid": true, "insuranceValid": true, "activeFaults": 0}
  }
\end{quote}
**Resultado Esperado:** Objeto `AssignmentValidationResult` con `isApproved: true`, `rejectionReasons: []`, y tiempo medido sobre el fixture, contrastado con el objetivo adicional de treinta milisegundos en memoria.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P1 (Bloqueante)**.
**Entorno:** Local CI Runner / Jest Unit Runtime.

**Variantes negativas del fixture:** repetir retirando, de a uno, jornada disponible, habilitación, aptitud mecánica y compatibilidad; cada falta debe impedir asignación. El oráculo de cada variante es isApproved=false con motivo específico. Un caso unitario rápido no acredita por sí solo asignación E2E p95hasta 30 s.

**Variante trazada a RF-001 (S3/T-12):** Preparar seis asignaciones con los cuatro factores presentes: fuentes de jornada 1, 2, 3, 4, 5 y ninguna. Con saldo y habilitaciones válidos, comprobar la cascada general: asigna en 1–4, asigna con marca y responsabilidad del transportista en 5, y bloquea sin fuente. Repetir el nivel 4 en la modalidad de datos de S3: sin atestación firmada no asignar; con atestación válida de nivel 5 asignar con marca. Aplicar RN-04 únicamente a su excepción de caída de fuente, nunca a un incumplimiento legal. Retirar por separado cada factor: todos deben bloquear aun con dos firmas. Medir las tres salidas de extremo a extremo en hasta 30 s; el tiempo unitario no acredita ese límite. En ensayo unitario se comprueba la regla con reloj controlado; latencia y comportamiento externo se acreditan en la prueba de integración, sistema o HIL asociada.

**Variante trazada a RF-005 (S3/T-12):** Generar 6.000 vigencias sintéticas con titular, responsable, fecha y respaldo. Fijar reloj y fechas a 61, 60, 31, 30, 8 y 7 días del vencimiento; esperar alertas exactamente en 60, 30 y 7, sin duplicación al repetir. Vencer cada tipo habilitante por separado: cualquier vencimiento bloquea; renovar con documento válido libera únicamente ese impedimento. En ensayo unitario se comprueba la regla con reloj controlado; latencia y comportamiento externo se acreditan en la prueba de integración, sistema o HIL asociada.

#### 9.0.3.2 CP-UNIT-02 — Límite de Conducción Continua de 5 Horas (Artículo 25 bis Código del Trabajo)

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-UNIT-02`
**Nivel y Tipología:** Prueba Unitaria Automatizada / Cumplimiento Legal y Algorítmico.
**Requerimiento Trazado:** RF-002.
**Precondiciones:** Función `evaluateContinuousDriving(driverTimeline)` cargada.
**Pasos de Ejecución:**
- Inyectar serie temporal continua de eventos de ignición ON y odometría en movimiento.
- Simular bloque continuo de 5 horas y 1 minuto de conducción sin pausa de reposo.
- Ejecutar la función de evaluación de jornada legal.

**Datos de Entrada Sintéticos:**
\begin{quote}\ttfamily
  {
    "driverId": "DRV-SYNTH-102",
    "drivingSessionStart": "2026-10-01T08:00:00Z",
    "evaluationTime": "2026-10-01T13:01:00Z",
    "movementEventsCount": 602,
    "speedReadingsAverageKmh": 78.4
  }
\end{quote}
**Resultado Esperado:** Emisión inmediata de infracción `VIOLATION_CONTINUOUS_DRIVING_EXCEEDED` con estado `BLOCKED_FOR_DISPATCH`, registrando exceso de 60 segundos.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P1 (Bloqueante)**.
**Entorno:** Local CI Runner / Go Test Runtime.

**Variante trazada a RF-002 (S3/T-12):** Construir un padrón sintético de 454 conductores identificados, 196 propios y 258 externos; asociar a cada tramo origen, conductor, vehículo y nivel 1–5, con muestras de todas las fuentes y ausencia de fuente. El expediente debe conservar todos los tramos y distinguirlos; un GPS sin identificación ni atestación no prueba jornada del conductor. El registro voluntario de nivel 0 nunca habilita la asignación. En ensayo unitario se comprueba la regla con reloj controlado; latencia y comportamiento externo se acreditan en la prueba de integración, sistema o HIL asociada.

#### 9.0.3.3 CP-UNIT-03 — Descanso Mínimo Intermedio de 2 Horas tras 5 Horas de Conducción

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-UNIT-03`
**Nivel y Tipología:** Prueba Unitaria Automatizada / Lógica de Regulación Laboral.
**Requerimiento Trazado:** RF-002.
**Precondiciones:** Conductor ha completado bloque de 5 horas continuas de conducción a las 13:00:00Z.
**Pasos de Ejecución:**
- Inyectar evento de inicio de descanso a las 13:00:00Z.
- Intentar asignar o activar nuevo viaje a las 14:45:00Z (transcurridas solo 1 h 45 min).
- Invocar validador `canResumeDriving(driverId, currentTime)`.
- Repetir validación a las 15:00:01Z (transcurridas 2 h 01 s de descanso efectivo).

**Datos de Entrada Sintéticos:** `driverId: "DRV-SYNTH-103"`, `breakStartTime: "2026-10-01T13:00:00Z"`, consultas en `t1 = 14:45:00Z` y `t2 = 15:00:01Z`.
**Resultado Esperado:**
   En `t1`: `canResume: false`, motivo `INSUFFICIENT_MANDATORY_BREAK`, tiempo restante `15 minutos`.
   En `t2`: `canResume: true`, contador de conducción continua reiniciado a 0,0 horas.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P1 (Bloqueante)**.
**Entorno:** Local CI Runner / Jest.

#### 9.0.3.4 CP-UNIT-04 — Descanso Mínimo Diario de 8 Horas Continuas en Ciclo de 24 Horas

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-UNIT-04`
**Nivel y Tipología:** Prueba Unitaria Automatizada / Validación Cronológica de Jornada.
**Requerimiento Trazado:** RF-002.
**Precondiciones:** Registro de 24 horas del conductor cargado con múltiples trayectos y pausas fraccionadas de 1 hora, sumando 10 horas de pausa pero ninguna continua $\ge 8$ horas.
**Pasos de Ejecución:**
- Procesar la ventana deslizante de 24 horas mediante `verifyDailyRestPeriod(timeline)`.
- Comprobar existencia de un bloque ininterrumpido de motor apagado e inactividad $\ge 8$ horas.

**Datos de Entrada Sintéticos:** Array de 1.440 minutos con actividades fraccionadas donde $\max(\text{bloque_descanso}) = 6{,}5\text{ horas}$.
**Resultado Esperado:** Función retorna `hasValidDailyRest: false`, `maxContinuousRestHours: 6.5`, `deficitHours: 1.5`, generando alerta de infracción legal.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P1 (Bloqueante)**.
**Entorno:** Local CI Runner / Go Test.

#### 9.0.3.5 CP-UNIT-05 — Control Acumulativo de Tope Mensual de 180 Horas Ordinarias de Trabajo

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-UNIT-05`
**Nivel y Tipología:** Prueba Unitaria Automatizada / Regulación Mensual Art. 25 bis.
**Requerimiento Trazado:** RF-002.
**Precondiciones:** Chofer con 178 horas acumuladas en el mes en curso al día 28.
**Pasos de Ejecución:**
- Evaluar orden de transporte sintética de 4 horas estimadas de duración.
- Invocar `validateMonthlyDrivingHoursCap(driverId, 4.0)`.

**Datos de Entrada Sintéticos:** `accumulatedMonthlyHours: 178.0`, `projectedTripHours: 4.0`, `monthlyCap: 180.0`.
**Resultado Esperado:** Rechazo de asignación con código `MONTHLY_CAP_OVERRUN_PREVENTED`, indicando exceso proyectado de 2,0 horas.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P1 (Bloqueante)**.
**Entorno:** Local CI Runner / Jest.

#### 9.0.3.6 CP-UNIT-06 — Generación y Sellado Criptográfico SHA-256 de la Entidad `EvidenciaJornada`

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-UNIT-06`
**Nivel y Tipología:** Prueba Unitaria Automatizada / Criptografía y No Repudio Legal.
**Requerimiento Trazado:** RF-004.
**Precondiciones:** Implementación SHA-256 y serializador canónico seleccionados para el ensayo; una clave simulada no acredita certificación FIPS ni no repudio legal.
**Pasos de Ejecución:**
- Serializar la entidad canónica `EvidenciaJornada` a JSON canónico ordenado (RFC 8785).
- Ejecutar función de hashing SHA-256 sobre la cadena serializada.
- Modificar un carácter arbitrario en el payload (ej. alterar odómetro en 1 km) y recalcular hash.
- Comparar ambos hashes.

**Datos de Entrada Sintéticos:**
\begin{quote}\ttfamily
  {
    "evidenceId": "EV-SYNTH-889102",
    "driverRUT": "15.984.321-K",
    "truckPlate": "LKJH-89",
    "timestampUTC": "2026-10-01T10:15:30Z",
    "engineState": "RUNNING",
    "odometerKm": 184520.4,
    "gpsCoordinates": {"lat": -33.5982, "lon": -70.7045}
  }
\end{quote}
**Resultado Esperado:** Hash SHA-256 generado con longitud exacta de 64 caracteres hexadecimales. El hash de la entidad modificada difiere completamente (no se exige que cada par de hashes cambie más de la mitad de sus bits).
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P1 (Bloqueante)**.
**Entorno:** Local CI Runner / Go Crypto / Jest.

**Variante trazada a RF-004 (S3/T-12):** Sellar un evento original y una corrección que cambia un dato; conservar ambas versiones con autor, origen y fecha. Alterar el original y verificar fallo de integridad. Avanzar reloj virtual hasta cinco años de conservación y comprobar disponibilidad e integridad antes de su término; la simulación verifica la política y no acredita cinco años de operación real. En ensayo unitario se comprueba la regla con reloj controlado; latencia y comportamiento externo se acreditan en la prueba de integración, sistema o HIL asociada.

#### 9.0.3.7 CP-UNIT-07 — Encadenamiento Criptográfico de Bloques de Jornada (PrevHash y Timestamp RFC 3161)

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-UNIT-07`
**Nivel y Tipología:** Prueba Unitaria Automatizada / Integridad WORM e Inmutabilidad.
**Requerimiento Trazado:** RF-004, RNF-012.
**Precondiciones:** Cadena en memoria con 5 bloques de evidencia previamente sellados.
**Pasos de Ejecución:**
- Insertar el bloque 6 conteniendo el `previousHash` del bloque 5.
- Validar la función de integridad `verifyChainIntegrity(chain)`.
- Simular un ataque interno modificando el estado del motor en el bloque 3.
- Re-ejecutar `verifyChainIntegrity(chain)`.

**Datos de Entrada Sintéticos:** Bloque 6 con hash anterior `a1b2c3d4...`, timestamp `2026-10-01T10:20:00Z`.
**Resultado Esperado:** La verificación retorna `valid: true` inicialmente; tras alterar el bloque 3, retorna `valid: false` identificando ruptura de enlace en bloque 3 y 4.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P1 (Bloqueante)**.
**Entorno:** Local CI Runner / Go Test.

**Variante trazada a RNF-012 (S3/T-12):** Crear evidencia con autor, origen, fecha y contenido; añadir corrección como registro nuevo. Esperar histórico íntegro y vínculo entre versiones. Quitar autor u origen y alterar fecha: rechazar ingreso probatorio o dejar pendiente identificado, nunca completar datos inventados ni sobrescribir original. En ensayo unitario se comprueba la regla con reloj controlado; latencia y comportamiento externo se acreditan en la prueba de integración, sistema o HIL asociada.

#### 9.0.3.8 CP-UNIT-08 — Algoritmo de Detección de Geocercas Poligonales Complejas (Ray-Casting)

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-UNIT-08`
**Nivel y Tipología:** Prueba Unitaria Automatizada / Geometría Computacional y Telemetría.
**Requerimiento Trazado:** RF-010, RNF-007.
**Precondiciones:** Polígono cóncavo de 12 vértices que delimita el patio de carga de un cliente agroexportador.
**Pasos de Ejecución:**
- Probar un punto de coordenadas P_1 ubicado claramente en el interior del polígono.
- Probar un punto P_2 situado en el borde perimetral exacto (tolerancia $\pm 2\text{ m}$).
- Probar un punto P_3 exterior a 15 metros del cerco.
- Ejecutar el algoritmo `isPointInPolygon(point, polygonVertices)`.

**Datos de Entrada Sintéticos:** Geometría plana sintética en metros; cuadrado de vértices (0,0), (100,0), (100,100), (0,100). P1=(50,50), P2=(0,50), P3=(-15,50). El borde exacto se clasifica como interior según política versionada; no se usan coordenadas latitud/longitud como UTM.
**Resultado Esperado:** P1=INSIDE, P2=BOUNDARY_INSIDE y P3=OUTSIDE. Se mide latencia; el ensayo unitario no sustituye el límite E2E contractual. Todos los puntos se evalúan con el mismo sistema de referencia.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P2 (Crítica)**.
**Entorno:** Local CI Runner / C++ o Go Test.

**Variante trazada a RF-010 (S3/T-12):** Versionar 1.400 polígonos y puntos de entrada, límite interior y exterior en el mismo sistema de coordenadas; ejecutar replay automático. Esperar una entrada y una salida por cruce válido, ninguna para puntos exteriores y deduplicación de reintentos, sin equipos en instalaciones del cliente ni acciones del conductor. En ensayo unitario se comprueba la regla con reloj controlado; latencia y comportamiento externo se acreditan en la prueba de integración, sistema o HIL asociada.

**Variante trazada a RNF-007 (S3/T-12):** Ejecutar detección de entrada, salida y espera con inventario de instalaciones de cliente vacío para componentes audIT. Esperar hitos automáticos desde señales del vehículo y servidor, cero instalaciones en cliente y cero acciones del conductor; agregar dependencia de equipo de garita debe fallar. En ensayo unitario se comprueba la regla con reloj controlado; latencia y comportamiento externo se acreditan en la prueba de integración, sistema o HIL asociada.

#### 9.0.3.9 CP-UNIT-09 — Cálculo de Huella de Carbono GLEC Framework / ISO 14083 por Tonelada-Kilómetro

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-UNIT-09`
**Nivel y Tipología:** Prueba Unitaria Automatizada / Algoritmo de Sostenibilidad y Emisiones.
**Requerimiento Trazado:** RF-023.
**Precondiciones:** Factores de emisión Well-to-Wheel (WTW) para diésel B7 en Chile cargados en configuración ($3{,}18\text{ kg CO}_2\text{e / litro}$).
**Pasos de Ejecución:**
- Suministrar viaje de 450 km con carga transportada de 24,5 toneladas y consumo sintético del fixture, sin atribuir medición real por CAN de 152 litros de diésel.
- Invocar `calculateEmissionsISO14083(fuelConsumedLiters, distanceKm, payloadTons)`.
- Validar formulación: $\text{Emisión Total} = 152 \times 3{,}18 = 483{,}36\text{ kg CO}_2\text{e}; \text{Intensidad} = \dfrac{483{,}36}{450 \times 24{,}5} = 0{,}04384\text{ kg CO}_2\text{e/ton-km} = 43{,}84\text{ g/ton-km}$.

**Datos de Entrada Sintéticos:** `fuelLiters: 152.0`, `distanceKm: 450.0`, `cargoTons: 24.5`, `emissionFactorWTW: 3.18`.
**Resultado Esperado:** Retorno de objeto con `totalEmissionsKgCO2e: 483.36` e `intensityGramPerTonKm: 43.84`, con precisión de 2 decimales.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P3 (Mayor)**.
**Entorno:** Local CI Runner / Jest.

**Variante trazada a RF-023 (S3/T-12):** Calcular emisiones mensuales de una muestra propia y otra externa con factores versionados, actividad y toneladas-kilómetro de referencia. Reproducir sumas y unidades de la hoja independiente y desglosar cliente y contrato. Sin factor o actividad, declarar faltante y no emitir cero verificado. La conformidad externa del método se acredita separadamente. En ensayo unitario se comprueba la regla con reloj controlado; latencia y comportamiento externo se acreditan en la prueba de integración, sistema o HIL asociada.

#### 9.0.3.10 CP-UNIT-10 — Conciliación de Combustible Diésel por Flujo CAN J1939 vs Odometría

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-UNIT-10`
**Nivel y Tipología:** Prueba Unitaria Automatizada / Telemetría y Detección de Desvíos.
**Requerimiento Trazado:** RF-018.
**Precondiciones:** Algoritmo de rendimiento nominal para motor Scania/Volvo 13L cargado (rango típico: 2{,}1 a $2{,}6\text{ km/litro}$ con carga completa).
**Pasos de Ejecución:**
- Inyectar datos de viaje: 320 km recorridos y 240 litros reportados por surtidor (rendimiento anómalo de $1{,}33\text{ km/l}$).
- Comparar con telemetría acumulada en PGN 65257 (Total Fuel Used) que reporta 135 litros efectivos consumidos por motor.
- Ejecutar rutina de conciliación `reconcileFuelEfficiency(fuelMeter, telemetryFuel, distanceKm)`.

**Datos de Entrada Sintéticos:** `distanceKm: 320.0`, `pumpFuelLiters: 240.0`, `canBusFuelLiters: 135.0`.
**Resultado Esperado:** Disparo de evento `FUEL_DISCREPANCY_ALERT` con nivel de sospecha de merma/extracción no autorizada de 105 litros ($43{,}75%$ de inconsistencia).
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P2 (Crítica)**.
**Entorno:** Local CI Runner / Python/Go Unit.

#### 9.0.3.11 CP-UNIT-11 — Enclavamiento Cinético de Interfaz de Usuario (Ley No Chat 21.377)

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-UNIT-11`
**Nivel y Tipología:** Prueba Unitaria Automatizada / Seguridad Vial y Cumplimiento Normativo.
**Requerimiento Trazado:** RNF-001.
**Precondiciones:** Dispositivo en cabina con pantalla táctil activa en formulario de despacho.
**Pasos de Ejecución:**
- Enviar evento telemático de velocidad vehicular $v = 0{,}0\text{ km/h}$. Verificar que UI es interactiva (`touchEnabled: true`).
- Enviar evento de transición de velocidad $v = 1{,}2\text{ km/h} (v > 0$).
- Medir tiempo de bloqueo de la interfaz gráfica y activación de modo conducción pasiva.
- Intentar disparo de evento táctil `touchDown` en la pantalla bloqueada.

**Datos de Entrada Sintéticos:** Evento sensor `SpeedSensorReading{speedKmh: 1.2, timestamp: 1775001200000}`.
**Resultado Esperado:** La UI transiciona a pantalla negra o aviso visual pasivo en $< 150\text{ ms}$, rechazando el 100% de los eventos táctiles interactivos.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P1 (Bloqueante)**.
**Entorno:** Local CI Runner / Android/Linux HAL Mock.

**Variante trazada a RNF-001 (S3/T-12):** Reproducir velocidad cero y velocidad positiva; intentar escritura, formulario y confirmación en ambos estados. En movimiento descartar toda captura manual y mostrar solo aviso pasivo. La recuperación de interfaz detenida no debe perder datos; parámetros de milisegundos son objetivos adicionales, no permiso para interactuar conduciendo. En ensayo unitario se comprueba la regla con reloj controlado; latencia y comportamiento externo se acreditan en la prueba de integración, sistema o HIL asociada.

#### 9.0.3.12 CP-UNIT-12 — Cálculo Algorítmico de Sobreestadías en Andén de Clientes

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-UNIT-12`
**Nivel y Tipología:** Prueba Unitaria Automatizada / Liquidación y Reglas de Negocio.
**Requerimiento Trazado:** RF-011.
**Precondiciones:** Parámetro contractual para Cliente Frutícola Sintético: Tiempo de espera libre (free time) = 2 horas; Tarifa de sobreestadía por tramo de 30 minutos configurada.
**Pasos de Ejecución:**
- Inyectar evento de entrada a geocerca de andén a las 09:00:00Z.
- Inyectar eventos de ignición OFF y permanencia continua hasta las 14:30:00Z (5 horas y 30 minutos totales).
- Ejecutar `calculateDemurrage(entryTime, exitTime, freeTimeMinutes, ratePerHalfHour)`.

**Datos de Entrada Sintéticos:** `entry: 09:00:00Z`, `exit: 14:30:00Z`, `freeTime: 120 min`, estadía total = 330 min, tiempo excedente = 210 min (7 bloques de 30 min).
**Resultado Esperado:** Retorno de `billableOverstayMinutes: 210`, `billableUnits: 7`, con trazabilidad de coordenadas y odómetro inalterados.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P2 (Crítica)**.
**Entorno:** Local CI Runner / Jest.

**Variante trazada a RF-011 (S3/T-12):** Usar un contrato sintético con 120 min libres y bloques facturables de 30 min, permanencias de 119, 120 y 330 min. Esperar 0, 0 y 210 min facturables respectivamente, siete bloques en la última. Conservar entrada, salida y contrato. Repetir con otro tiempo libre contractual para verificar que no se fija universalmente en dos horas. En ensayo unitario se comprueba la regla con reloj controlado; latencia y comportamiento externo se acreditan en la prueba de integración, sistema o HIL asociada.

#### 9.0.3.13 CP-UNIT-13 — Deserialización y Validación de Esquemas Protobuf de Telemetría Vehicular

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-UNIT-13`
**Nivel y Tipología:** Prueba Unitaria Automatizada / Protocolos Binarios y Validación de Esquema.
**Requerimiento Trazado:** Ensayo adicional de ingeniería; no sustituye controles contractuales.
**Precondiciones:** Esquema `telemetry_v2.proto` compilado en clases binarias de deserialización.
**Pasos de Ejecución:**
- Construir un paquete binario corrupto (truncado en el byte 45).
- Intentar deserialización mediante `TelemetryPacket.parseFrom(corruptBytes)`.
- Construir un paquete válido de 118 bytes con telemetría completa y deserializarlo.

**Datos de Entrada Sintéticos:** Buffer de bytes válidos conteniendo timestamp, coordenadas, velocidad, RPM, combustible y temperatura y estado de balizas Bluetooth.
**Resultado Esperado:** El paquete corrupto lanza `InvalidProtocolBufferException` gestionada limpiamente sin crash; el paquete válido se deserializa en $< 5\text{ }\mu\text{s}$ con valores de campos 100% exactos.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P2 (Crítica)**.
**Entorno:** Local CI Runner / Go o Java Testcontainers.

#### 9.0.3.14 CP-UNIT-14 — Detección de Discrepancias y Manipulación en Odómetro CAN vs GNSS

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-UNIT-14`
**Nivel y Tipología:** Prueba Unitaria Automatizada / Detección de Fraude e Integridad.
**Requerimiento Trazado:** RF-025.
**Precondiciones:** Algoritmo de contraste cinemático inicializado.
**Pasos de Ejecución:**
- Inyectar serie de 1 hora donde la integración de velocidad GNSS acumula 85 km.
- Inyectar telemetría de odómetro de bus CAN que solo incrementa en 5 km (simulación de pinza desconectada o cable manipulado).
- Invocar validador `auditOdometerIntegrity(gpsDeltaKm, canDeltaKm)`.

**Datos de Entrada Sintéticos:** `gpsDeltaKm: 85.0`, `canDeltaKm: 5.0`, `thresholdDeltaPercentage: 10.0`.
**Resultado Esperado:** Emisión de alerta de seguridad `ODOMETER_TAMPERING_SUSPECTED` con discrepancia de $94{,}1%$.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P2 (Crítica)**.
**Entorno:** Local CI Runner / Jest.

**Variante trazada a RF-025 (S3/T-12):** Configurar mantenimiento a 100.000 km como dato sintético, no norma. Con odómetro real de 99.999 y 100.000 km esperar ausencia y presencia de aviso, respectivamente, enviado al sistema de talleres. Repetir con estimación: marcar incertidumbre y origen, sin presentar estimación como lectura real ni perder el aviso. En ensayo unitario se comprueba la regla con reloj controlado; latencia y comportamiento externo se acreditan en la prueba de integración, sistema o HIL asociada.

#### 9.0.3.15 CP-UNIT-15 — Algoritmo ALNS: Función de Costo de Inserción y Retornos en Vacío

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-UNIT-15`
**Nivel y Tipología:** Prueba Unitaria Automatizada / Optimización Combinatoria y Retornos.
**Requerimiento Trazado:** RF-015.
**Precondiciones:** Matriz de distancias viales entre Concepción, San Bernardo y Valparaíso precargada.
**Pasos de Ejecución:**
- Definir camión que finaliza descarga en Concepción a las 14:00.
- Proveer dos órdenes candidatas de retorno: O_1 (salida Talcahuano a San Bernardo, desvío 15 km) y O_2 (salida Chillán a San Bernardo, desvío 110 km).
- Ejecutar función heurística de inserción `evaluateALNSInsertionCost(truckState, [O1, O2])`.

**Datos de Entrada Sintéticos:** Dos candidatos legalmente viables y con ventanas compatibles. Fixture simplificado: ingreso 1.000 unidades por retorno; costo variable 2 unidades/km; O1: 15 km incrementales; O2: 110 km. Margen incremental O1=970 y O2=780. No son tarifas ni distancias medidas del caso; unidades abstractas del ensayo.
**Resultado Esperado:** O1 obtiene mayor margen (970 frente a 780) y se selecciona. Repetir O1 sin jornada disponible: debe descartarse y seleccionarse O2 si es viable. Si ambas incumplen restricciones, no se propone retorno.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: Alta cuando afecta seguridad o evidencia; mayor en objetivos adicionales.
**Entorno:** Local CI Runner / Go Test.

**Oráculo del fixture ALNS:** Ingreso menos costo incremental; el ensayo controlado valida decisión y restricciones. No demuestra optimalidad global del algoritmo en la red real.

**Variante trazada a RF-015 (S3/T-12):** Usar las dos ofertas de retorno del fixture de CP-UNIT-15 con márgenes analíticos 970 y 780, en unidades sintéticas ajenas a precios de oferta. Con ambas viables elegir la primera; sin jornada, habilitación, capacidad, compatibilidad o ventana de entrega en la primera, descartarla y elegir la segunda viable. Si ninguna cumple RN-09, no proponer retorno. En ensayo unitario se comprueba la regla con reloj controlado; latencia y comportamiento externo se acreditan en la prueba de integración, sistema o HIL asociada.

#### 9.0.3.16 CP-UNIT-16 — Parser de Tramas J1939: PGN 65265 (Velocidad) y PGN 65266 (Combustible)

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-UNIT-16`
**Nivel y Tipología:** Prueba Unitaria Automatizada / Parsing de Telecomunicaciones Automotrices.
**Requerimiento Trazado:** RNF-005.
**Precondiciones:** Mapa de decodificación versionado del equipo que se homologue. La compatibilidad J1939 de cada camión se verifica antes de instalar; este fixture valida aritmética, sin acreditar una señal de fábrica.
**Pasos de Ejecución:**
- Suministrar trama raw CAN ID `0x18FEF100` (PGN 65265) con payload `0xFF 0x50 0x4E 0xFF 0xFF 0xFF 0xFF 0xFF`.
- Decodificar velocidad de rueda (bytes 2 y 3, resolución $1/256\text{ km/h por bit}$).
- Suministrar trama raw PGN 65266 (Fuel Economy) y decodificar caudal instantáneo.

**Datos de Entrada Sintéticos:** Bytes sintéticos, sin atribuir captura a Technoton CANCrocodile ni a vehículos reales; mapa de caudal de laboratorio y patrón de dato no disponible versionados.
**Resultado Esperado:** Bajo el mapa sintético little-endian indicado, bytes 0x50 y 0x4E: entero 20.048; 20.048/256 = 78,3125 km/h. Añadir fixture de caudal: entero 2.000, resolución sintética 0,05 L/h por unidad, resultado 100 L/h. Verificar también valor no disponible según el mapa homologado, sin convertirlo en cero.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P2 (Crítica)**.
**Entorno:** Local CI Runner / C / Go Test.

**Variante trazada a RNF-005 (S3/T-12):** Medir con analizador independiente el bus durante lectura y reinicio del equipo: cero tramas transmitidas por audIT. Conservar autorización del fabricante, mapa de señales y evidencia de no corte/no interferencia. Un parser correcto o una tasa baja de pérdidas no acredita por sí solo lectura pasiva ni preservación de garantía. En ensayo unitario se comprueba la regla con reloj controlado; latencia y comportamiento externo se acreditan en la prueba de integración, sistema o HIL asociada.

#### 9.0.3.17 CP-UNIT-17 — Validación de Integridad de Certificados X.509 y Tokens JWT en Cabina

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-UNIT-17`
**Nivel y Tipología:** Prueba Unitaria Automatizada / Ciberseguridad y Autenticación Criptográfica.
**Requerimiento Trazado:** Ensayo adicional de ingeniería; no sustituye controles contractuales.
**Precondiciones:** Certificado raíz de la Autoridad Certificadora (CA) de audIT SpA cargado en almacén de confianza.
**Pasos de Ejecución:**
- Validar un token JWT firmado con algoritmo ECDSA (curva P-256) emitido por el API Gateway.
- Probar un token con firma alterada en un bit.
- Probar un token con vigencia expirada (`exp` en el pasado).

**Datos de Entrada Sintéticos:** Tokens JWT sintéticos con roles de chofer y despachador.
**Resultado Esperado:** Token válido verificado exitosamente en $< 2\text{ ms}$; token manipulado y token expirado rechazados con `SecurityException`.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P1 (Bloqueante)**.
**Entorno:** Local CI Runner / Jest.

#### 9.0.3.18 CP-UNIT-18 — Algoritmo de Estimación Dinámica de Alerta de Fatiga según ETA a Área Segura

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-UNIT-18`
**Nivel y Tipología:** Prueba Unitaria Automatizada / Lógica Predictiva y Seguridad Vial.
**Requerimiento Trazado:** RF-027.
**Precondiciones:** Chofer en Ruta 5 Norte a 4 horas y 15 minutos de conducción continua.
**Pasos de Ejecución:**
- Consultar base de áreas de descanso autorizadas en la ruta. Próxima área segura a 38 km (ETA = 35 minutos). Siguiente área a 140 km (ETA = 110 minutos).
- Evaluar tiempo restante legal (45 minutos hasta el límite de 5 horas).
- Invocar algoritmo de recomendación de detención `evaluateFatigueAlert(currentHours, nearestSafeSpots)`.

**Datos de Entrada Sintéticos:** Posición actual km 450 Ruta 5 Norte, velocidad media $65\text{ km/h}$, tiempo restante 45 min.
**Resultado Esperado:** Disparo preventivo de alerta sonora en cabina conminando a detenerse en el área de descanso del km 488 (arribo estimado en 35 min, con 10 min de holgura legal).
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P2 (Crítica)**.
**Entorno:** Local CI Runner / Go Test.

**Variante trazada a RF-027 (S3/T-12):** Reproducir conducción acumulada 4 h 15 min y área segura alcanzable en 35 min: alertar antes de agotar cinco horas con diez minutos de holgura. Mover área a 50 min: no recomendarla como alcanzable legalmente. La alerta en movimiento es pasiva y no solicita escritura ni confirmación táctil. En ensayo unitario se comprueba la regla con reloj controlado; latencia y comportamiento externo se acreditan en la prueba de integración, sistema o HIL asociada.

#### 9.0.3.19 CP-UNIT-19 — Validación de Incompatibilidad Química de Carga SUSPEL (D.S. 298 y NCh 2190)

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-UNIT-19`
**Nivel y Tipología:** Prueba Unitaria Automatizada / Regulación de Sustancias Peligrosas.
**Requerimiento Trazado:** RF-006.
**Precondiciones:** Matriz de segregación e incompatibilidad química de la norma chilena NCh 382 y NCh 2190 cargada.
**Pasos de Ejecución:**
- Intentar asignar en una misma unidad compartimentada o viaje combinado: Sustancia Clase 3 (Líquido Inflamable - Diésel UN 1202) con Sustancia Clase 5.1 (Comburente - Nitrato de Amonio UN 1942).
- Invocar validador `validateHazardousCargoCompatibility(cargoList)`.

**Datos de Entrada Sintéticos:** `[{"unNumber": 1202, "class": "3"}, {"unNumber": 1942, "class": "5.1"}]`.
**Resultado Esperado:** Bloqueo terminante con código `CHEMICAL_INCOMPATIBILITY_FATAL`, señalando prohibición expresa de transporte simultáneo.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P1 (Bloqueante)**.
**Entorno:** Local CI Runner / Jest.

**Variante trazada a RF-006 (S3/T-12):** Preparar 18 unidades SUSPEL sintéticas, cada una con carga efectiva, DET emitido por ERP, conductor y lista firmada. La muestra conforme vincula esos elementos y permite salida si los otros factores cumplen. Cambiar carga respecto del documento, quitar firma o vencer habilitación: cada variante bloquea. La compatibilidad química por sí sola no acredita este requisito. En ensayo unitario se comprueba la regla con reloj controlado; latencia y comportamiento externo se acreditan en la prueba de integración, sistema o HIL asociada.

#### 9.0.3.20 CP-UNIT-20 — Filtro de Kalman Unidimensional para Filtrado de Ruido y Deriva GNSS

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-UNIT-20`
**Nivel y Tipología:** Prueba Unitaria Automatizada / Procesamiento de Señales Satelitales.
**Requerimiento Trazado:** RF-008.
**Precondiciones:** Filtro de Kalman configurado con varianza de proceso Q = 10^{−5} y varianza de medición $R = 4{,}0\text{ m}^2$.
**Pasos de Ejecución:**
- Inyectar serie de 10 lecturas estacionarias (v = 0) afectadas por ruido gaussiano y un salto abrupto de 45 metros (efecto cañón urbano / multitrayectoria).
- Ejecutar función `filterGnssNoise(readings)`.

**Datos de Entrada Sintéticos:** Coordenadas lat/lon con desviación de 45 m en la muestra número 6.
**Resultado Esperado:** La coordenada filtrada amortigua el salto abrupto, manteniéndose a $< 3{,}5\text{ metros}$ de la posición media real.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P3 (Mayor)**.
**Entorno:** Local CI Runner / Python/C++.

#### 9.0.3.21 CP-UNIT-21 — Validación del Estado Conforme del DET y Bloqueo de Documento No Admitido

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-UNIT-21`
**Nivel y Tipología:** Ensayo de validación unitaria / Conformidad y bloqueo.
**Requerimiento Trazado:** RF-014.
**Precondiciones:** Vehículo detenido; orden y datos completos. Doble del ERP configurado con esquema e interfaz versionados. El fixture identifica un documento admitido y uno no emitido/no conforme; la validación fiscal real se homologa con el ERP y su proveedor, sin presumir API o contingencia certificada.
**Pasos de Ejecución:**
- Preparar datos desde la orden y enviarlos al ERP contable como único emisor, con identificador idempotente.
- Validar estado, identidad del emisor, firma, folio y asociación inequívoca a la orden según el contrato de integración. Una firma exclusiva de audIT no demuestra conformidad tributaria.
- Recuperar el documento conforme admitido por el fixture en cabina y cortar la cobertura. Confirmar disponibilidad local antes de autorizar movimiento.
- Repetir con documento ausente, rechazo, folio no válido, revocación o datos discordantes: debe mantenerse el bloqueo; no emitir un documento paralelo ni permitir salida con una promesa de regularización.
- Repetir el envío con el mismo identificador: debe existir una sola emisión y conservarse auditoría y respuesta del ERP. Verificar reconexión sin duplicados.

**Datos de Entrada Sintéticos:** Dos órdenes de prueba, mismo identificador repetido, estado `CONFORME` y estado `NO_EMITIDO`, documento/firma/folio y esquema de prueba versionados; manifestar emisor, orden y huellas. Reloj virtual del fixture.
**Resultado Esperado:** Disponible el documento conforme antes del movimiento; bloqueadas todas las variantes negativas, una única emisión por orden y evidencia de validación conservada. En pruebas de sistema/hardware se mide ≤90 s; en pruebas unitarias se valida el estado, sin sustituir el tiempo E2E.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: Alta cuando afecta seguridad o evidencia; mayor en objetivos adicionales.
**Entorno:** CI con doble de ERP. Homologación real del mecanismo de contingencia antes de despliegue; la falta de disponibilidad no se resuelve fingiendo certificación.

**Variante trazada a RF-014 (S3/T-12):** Ejecutar dos rutas de contingencia: DET anticipado por ERP desde la orden y datos enviados por enlace satelital al ERP con folio de vuelta al vehículo. Antes del movimiento debe existir DET conforme accesible localmente; ausencia de folio, datos discordantes y respuesta fuera de plazo bloquean. Un PDF local firmado por audIT no sustituye emisión del ERP. En ensayo unitario se comprueba la regla con reloj controlado; latencia y comportamiento externo se acreditan en la prueba de integración, sistema o HIL asociada.

#### 9.0.3.22 CP-UNIT-22 — Cálculo de Desgaste Predictivo de Neumáticos por Kilometraje y Eje RFID

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-UNIT-22`
**Nivel y Tipología:** Prueba Unitaria Automatizada / Mantenimiento Predictivo de Activos.
**Requerimiento Trazado:** RF-025.
**Precondiciones:** Parámetro de tasa de desgaste de banda de rodado por tipo de eje (direccional, tracción, remolque) en mm/10.000 km.
**Pasos de Ejecución:**
- Suministrar neumático RFID ID `TIRE-SYNTH-9941` en eje de tracción con 45.000 km recorridos.
- Invocar `predictRemainingTireLife(initialDepthMm, currentKm, axleType)`.

**Datos de Entrada Sintéticos:** Profundidad inicial $16{,}0\text{ mm}$, profundidad mínima legal $1{,}6\text{ mm}$, kilometraje acumulado 45.000 km.
**Resultado Esperado:** Retorno de profundidad remanente estimada ($9{,}2\text{ mm}$) y proyección de cambio en 38.000 km adicionales.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P3 (Mayor)**.
**Entorno:** Local CI Runner / Jest.

#### 9.0.3.23 CP-UNIT-23 — Compresión de Paquetes con Algoritmo Zstandard para Buffer de 288 Horas

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-UNIT-23`
**Nivel y Tipología:** Prueba Unitaria Automatizada / Rendimiento de Almacenamiento y Compresión.
**Requerimiento Trazado:** RNF-002.
**Precondiciones:** Librería `zstd` configurada en nivel de compresión 3 (balance óptimo CPU/ratio).
**Pasos de Ejecución:**
- Tomar lote de 34.560 paquetes de telemetría sin procesar (equivalente a 288 horas continuas, tamaño raw $≈ 4{,}15\text{ MB}$).
- Ejecutar compresión zstandard.
- Medir tamaño del buffer comprimido y tiempo de compresión en CPU de arquitectura ARM.
- Descomprimir el buffer y validar integridad bit a bit contra el original.

**Datos de Entrada Sintéticos:** Lote sintético de 288 h de telemetría de ruta de montaña.
**Resultado Esperado:** La descompresión reproduce exactamente los bytes de origen; conteo, orden e identificadores permanecen iguales. Se mide tamaño comprimido y se calcula razón raw/comprimido, sin anticipar 1,2 MB ni una razón universal. Este fixture de 34.560 paquetes de 120 bytes suma 4.147.200 bytes, sin fotos ni overhead; no representa el perfil operacional de S4.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: Alta cuando afecta seguridad o evidencia; mayor en objetivos adicionales.
**Entorno:** Local CI Runner / C/Go Test.

**Variante trazada a RNF-002 (S3/T-12):** Repetir el conjunto de 72 h sin red, reinicios y reenvío de cada lote dos veces. Esperar mismos identificadores y huellas al final, ninguna pérdida ni duplicado, con bitácora de conciliación. La compresión unitaria comprueba reversibilidad y no acredita capacidad ni sincronización del equipo completo. En ensayo unitario se comprueba la regla con reloj controlado; latencia y comportamiento externo se acreditan en la prueba de integración, sistema o HIL asociada.

#### 9.0.3.24 CP-UNIT-24 — Procesamiento de temperatura de baliza Bluetooth

Este ensayo define entradas, controles y evidencia; no declara resultados ejecutados.

**ID:** `CP-UNIT-24`
**Nivel y Tipología:** Prueba unitaria / Decodificación y validación del dato térmico.
**Requerimiento Trazado:** Ensayo adicional de ingeniería; no sustituye controles contractuales.
**Precondiciones:** Esquema de anuncio y conversión versionado del modelo de baliza ofertado; no usa resistencia eléctrica ni curva PT100.
**Pasos de Ejecución:**
- Decodificar anuncios sintéticos con identificador, temperatura, unidad y sello de recepción conocidos.
- Probar temperaturas dentro y fuera del rango documentado, trama truncada, unidad inválida y dato ausente o antiguo.
- Conservar origen y validez; no convertir ausencia en cero ni extrapolar fuera del rango.

**Datos de Entrada Sintéticos:** Anuncios conocidos con temperatura de referencia y casos inválidos; sin atribuir captura real.
**Resultado Esperado:** La temperatura decodificada coincide con el oráculo a la resolución del formato; entradas inválidas se marcan y no generan lecturas válidas. Esta prueba no acredita precisión metrológica del sensor.
**Pass/Fail y Severidad:** Pass solo si se cumplen todos los criterios y se conserva evidencia reproducible; cualquier pérdida, acceso no autorizado o salida incorrecta implica Fail. Severidad alta para seguridad y evidencia.
**Entorno:** CI / Decodificador Bluetooth.

#### 9.0.3.25 CP-UNIT-25 — Validación Sintáctica de Códigos QR para Hojas de Datos de Seguridad (HDS)

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-UNIT-25`
**Nivel y Tipología:** Prueba Unitaria Automatizada / Validación Documental y SUSPEL.
**Requerimiento Trazado:** Ensayo adicional de ingeniería; no sustituye controles contractuales.
**Precondiciones:** Expresión regular y esquema de carga peligrosa compilados.
**Pasos de Ejecución:**
- Parsear un payload de QR sintético válido con formato `HDS|UN1202|DIESEL|CL3|EMERGENCIA-800-222-333|HASH`.
- Parsear un payload con código UN inexistente (`UN9999`).
- Parsear un payload con formato corrupto.

**Datos de Entrada Sintéticos:** Cadenas de texto QR sintéticas.
**Resultado Esperado:** Payload válido parseado en objeto estructurado; payloads anómalos rechazados con código `INVALID_HDS_QR_STRUCTURE`.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P2 (Crítica)**.
**Entorno:** Local CI Runner / Jest.

### 9.0.4 Batería 2: Pruebas de Integración y APIs (25 Casos: `CP-INT-01` a `CP-INT-25`)

Esta batería verifica el acoplamiento técnico, los contratos de interfaz OpenAPI 3.1, la persistencia en bases de datos con contenedores efímeros (Testcontainers), la ingesta telemática de terceros bajo la Capa Anticorrupción (ACL), y los enlaces con el ERP tributario y Azure Key Vault.

#### 9.0.4.1 CP-INT-01 — Contrato OpenAPI 3.1 — Servicio de Despacho con Testcontainers PostgreSQL HA

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-INT-01`
**Nivel y Tipología:** Prueba de Integración / Contratos de API REST y Persistencia Relacional ACID.
**Requerimiento Trazado:** Ensayo adicional de ingeniería; no sustituye controles contractuales.
**Precondiciones:**
- Contenedor Docker efímero `postgres:16-alpine` levantado vía Testcontainers en pipeline.
- Migraciones Flyway ejecutadas exitosamente (tablas `dispatch_orders`, `trips`, `driver_status`).

**Pasos de Ejecución:**
- Realizar petición `POST /api/v1/dispatch/orders` con esquema OpenAPI 3.1.
- Validar que el middleware de validación sintáctica verifique campos obligatorios.
- Comprobar inserción transaccional atómica en PostgreSQL con clave foránea válida.
- Consultar `GET /api/v1/dispatch/orders/{orderId}` y validar consistencia.

**Datos de Entrada Sintéticos:**
\begin{quote}\ttfamily
  {
    "orderCode": "OT-2026-INT-001",
    "originTerminal": "SBO",
    "destinationZone": "VAL",
    "cargoWeightKg": 22400.0,
    "requiredEquipmentType": "FLATBED_TRAILER",
    "scheduledDeparture": "2026-10-02T06:00:00Z"
  }
\end{quote}
**Resultado Esperado:** Código HTTP `201 Created` con payload conforme a esquema JSON Schema, UUID generado, registro persistido en BD en $< 40\text{ ms}$.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P1 (Bloqueante)**.
**Entorno:** CI Testcontainers Runtime / Docker daemon.

#### 9.0.4.2 CP-INT-02 — Contrato OpenAPI 3.1 — Ingesta de Series Temporales con TimescaleDB Testcontainers

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-INT-02`
**Nivel y Tipología:** Prueba de Integración / Base de Datos de Series Temporales y Hypertables.
**Requerimiento Trazado:** RF-002.
**Precondiciones:** Contenedor `timescale/timescaledb:latest-pg16` activo con hypertable `truck_telemetry` particionada por intervalos de 7 días.
**Pasos de Ejecución:**
- Emitir petición `POST /api/v1/telemetry/batches` conteniendo array de 100 mediciones de telemetría.
- Verificar inserción masiva (copy protocol) en TimescaleDB.
- Ejecutar consulta analítica con función `time_bucket('5 minutes', timestamp)` para comprobar agregación.

**Datos de Entrada Sintéticos:** Array de 100 lecturas sintéticas con latitud, longitud, velocidad, odómetro, temperatura reefer y RPM para camión `TRK-SYNTH-012`.
**Resultado Esperado:** Código HTTP `202 Accepted`, 100 tuplas insertadas en la partición correspondiente en $< 50\text{ ms}$, consulta de agregación retorna datos consistentes.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P1 (Bloqueante)**.
**Entorno:** CI Testcontainers Runtime.

**Variante trazada a RF-002 (S3/T-12):** Construir un padrón sintético de 454 conductores identificados, 196 propios y 258 externos; asociar a cada tramo origen, conductor, vehículo y nivel 1–5, con muestras de todas las fuentes y ausencia de fuente. El expediente debe conservar todos los tramos y distinguirlos; un GPS sin identificación ni atestación no prueba jornada del conductor. El registro voluntario de nivel 0 nunca habilita la asignación. En ensayo unitario se comprueba la regla con reloj controlado; latencia y comportamiento externo se acreditan en la prueba de integración, sistema o HIL asociada.

#### 9.0.4.3 CP-INT-03 — Contrato OpenAPI 3.1 — Caché de Validación Pre-Despacho con Redis Cluster Testcontainers

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-INT-03`
**Nivel y Tipología:** Prueba de Integración / Almacenamiento en Memoria de Alta Velocidad.
**Requerimiento Trazado:** RF-003.
**Precondiciones:** Instancia Redis 7.2 en contenedor Testcontainers con políticas de desalojo LRU configuradas.
**Pasos de Ejecución:**
- Poblar Redis con 6.000 vigencias indexadas por clave `validity:{entity_type}:{id}`.
- Ejecutar petición de consulta de habilitación síncrona `GET /api/v1/compliance/check-eligibility?driverId=DRV-101&truckId=TRK-05`.
- Medir latencia de consulta compuesta en Redis mediante pipeline MGET.

**Datos de Entrada Sintéticos:** Claves Redis con TTL de 24 horas simulando revisiones técnicas, licencias A5 y pólizas de seguro de carga.
**Resultado Esperado:** Código HTTP `200 OK`, respuesta estructurada con estado de aptitud en latencia de red/backend $< 15\text{ ms} (P_{99} < 25\text{ ms}$).
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P1 (Bloqueante)**.
**Entorno:** CI Testcontainers Runtime.

**Variante trazada a RF-003 (S3/T-12):** Crear dos conductores externos con igual viaje propuesto y jornadas previas distintas: descanso continuo de 8 h y de 6 h en la ventana de 24 h del fixture. Con permiso y evidencia verificable, el primero dispone de descanso y el segundo bloquea. Repetir sin fuente, con atestación firmada del dueño y con permiso revocado: bloquear sin fuente, asignar con marca cuando la atestación acredita saldo válido y cesar la consulta revocada. No divulgar coordenadas de otros clientes. En ensayo unitario se comprueba la regla con reloj controlado; latencia y comportamiento externo se acreditan en la prueba de integración, sistema o HIL asociada.

#### 9.0.4.4 CP-INT-04 — Contrato OpenAPI 3.1 — Streaming de Telemetría con Apache Kafka Testcontainers

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-INT-04`
**Nivel y Tipología:** Prueba de Integración / Mensajería Asíncrona Distribuida y Eventos.
**Requerimiento Trazado:** Ensayo adicional de ingeniería; no sustituye controles contractuales.
**Precondiciones:** Broker Kafka efímero levantado con tópico `telemetry.raw.v1` con 6 particiones y factor de replicación 1.
**Pasos de Ejecución:**
- Publicar mensaje serializado mediante productor Kafka con clave de particionamiento `truckId`.
- Iniciar consumidor en grupo `telemetry-processor-group`.
- Verificar recepción del mensaje, deserialización y confirmación de commit manual de offset.

**Datos de Entrada Sintéticos:** Evento Kafka con encabezados de metadatos (timestamp, tenantId, schemaVersion) y payload JSON/Protobuf.
**Resultado Esperado:** Consumidor recibe el evento exacto en $< 20\text{ ms}$, procesa la carga y confirma offset sin reprocesamientos.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P1 (Bloqueante)**.
**Entorno:** CI Testcontainers Runtime.

#### 9.0.4.5 CP-INT-05 — Conector CDC Debezium con BD de TMS 2013 Legacy (Patrón Estrangulador)

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-INT-05`
**Nivel y Tipología:** Prueba de Integración / Change Data Capture (CDC) y Migración Progresiva.
**Requerimiento Trazado:** RNF-011.
**Precondiciones:** Contenedor simulando la BD relacional del TMS 2013 (Microsoft SQL Server / PostgreSQL legacy) con replicación lógica activa; Kafka Connect con plugin Debezium desplegado.
**Pasos de Ejecución:**
- Insertar una orden de transporte en la tabla legada `dbo.ORDENES_CARGA` emulando la operación de un despachador legacy.
- Monitorear el tópico Kafka `legacy.curimon.ordenes_carga`.
- Verificar que Debezium capture la mutación a nivel de log transaccional (WAL/CDC).
- Validar transformación de la estructura legacy al esquema moderno del nuevo core audIT.

**Datos de Entrada Sintéticos:** `INSERT INTO dbo.ORDENES_CARGA (ID_ORDEN, CLIENTE, ORIGEN, DESTINO, FECHA) VALUES ('ORD-9901', 'FRUTICOLA_SUR', 'SBO', 'PMC', GETDATE());`
**Resultado Esperado:** Evento CDC capturado en $< 500\text{ ms}$, transformado por el conector y disponible en el tópico Kafka canónico con los campos traducidos.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P1 (Bloqueante)**.
**Entorno:** CI Testcontainers Runtime (SQL Server + Debezium).

**Variante trazada a RNF-011 (S3/T-12):** Durante convivencia TMS 2013/nuevo sistema, desviar por función y repetir una misma orden por ambas rutas; esperar un solo viaje y ningún despacho que eluda bloqueo. Restaurar ruta anterior sin detener la flota. Assignment, tracking y liquidación pasan en M16, órdenes y tarifas cliente en M21; solo lectura hasta M24 según S3. El ERP contable permanece separado. En ensayo unitario se comprueba la regla con reloj controlado; latencia y comportamiento externo se acreditan en la prueba de integración, sistema o HIL asociada.

#### 9.0.4.6 CP-INT-06 — Interceptación y Ruteo de Órdenes TMS 2013 hacia Capa Anticorrupción (ACL)

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-INT-06`
**Nivel y Tipología:** Prueba de Integración / Arquitectura de Software y Capa Anticorrupción.
**Requerimiento Trazado:** Ensayo adicional de ingeniería; no sustituye controles contractuales.
**Precondiciones:** Capa ACL configurada para interceptar llamadas de asignación y enrutar validaciones al microservicio en AKS.
**Pasos de Ejecución:**
- Enviar requerimiento de despacho legacy a través del gateway de la ACL.
- Verificar que la ACL invoque internamente al nuevo motor de asignación bloqueante.
- Simular que el motor nuevo rechaza la asignación por exceso de jornada del conductor.
- Comprobar que la ACL traduce el error a un código comprensible por la UI del TMS 2013 legacy.

**Datos de Entrada Sintéticos:** Payload SOAP/XML legacy con chofer infractor.
**Resultado Esperado:** Respuesta SOAP con código de rechazo legacy `ERR_ASIG_BLOQUEO_SEGURIDAD`, impidiendo que el despachador del TMS 2013 fuerce el viaje.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P1 (Bloqueante)**.
**Entorno:** CI Testcontainers / WireMock Mock Server.

#### 9.0.4.7 CP-INT-07 — Normalización de datos GPS por acceso autorizado

Este ensayo define entradas, controles y evidencia; no declara resultados ejecutados.

**ID:** `CP-INT-07`
**Nivel y Tipología:** Prueba de integración / Interoperabilidad GPS.
**Requerimiento Trazado:** RNF-003.
**Precondiciones:** Inventario por plataforma y vehículo con permiso, mecanismo de acceso, campos y frecuencia; dos accesos de solo consulta y una plataforma sin exportación. Dobles versionados, sin fijar marca real.
**Pasos de Ejecución:**
- Probar consulta autorizada y rechazo con permiso ausente o revocado.
- Introducir posición fechada, duplicada, antigua, ausente y cambio de esquema.
- Simular prohibición de exportación: no ejecutar descarga ni suscripción Webhook; registrar cobertura no disponible.
- Normalizar solo los datos obtenidos legalmente, conservar fuente y antigüedad y verificar deduplicación.

**Datos de Entrada Sintéticos:** Tres perfiles de plataforma simulados; eventos y denegaciones deterministas.
**Resultado Esperado:** Cero accesos no autorizados, intervenciones de equipos o duplicados. La falta de datos queda visible y no se sustituye por posición o jornada inventada. Una consulta de posición no acredita jornada del conductor ni integración de los 192 vehículos; la aceptación real requiere muestra autorizada por plataforma.
**Pass/Fail y Severidad:** Pass solo si se cumplen todos los criterios y se conserva evidencia reproducible; cualquier pérdida, acceso no autorizado o salida incorrecta implica Fail. Severidad alta para seguridad y evidencia.
**Entorno:** QA / Dobles de plataforma y capa de integración.

#### 9.0.4.8 CP-INT-08 — Consulta restringida y plataforma sin exportación

Este ensayo define entradas, controles y evidencia; no declara resultados ejecutados.

**ID:** `CP-INT-08`
**Nivel y Tipología:** Prueba de integración / Interoperabilidad GPS.
**Requerimiento Trazado:** RNF-003.
**Precondiciones:** Inventario por plataforma y vehículo con permiso, mecanismo de acceso, campos y frecuencia; dos accesos de solo consulta y una plataforma sin exportación. Dobles versionados, sin fijar marca real.
**Pasos de Ejecución:**
- Probar consulta autorizada y rechazo con permiso ausente o revocado.
- Introducir posición fechada, duplicada, antigua, ausente y cambio de esquema.
- Simular prohibición de exportación: no ejecutar descarga ni suscripción Webhook; registrar cobertura no disponible.
- Normalizar solo los datos obtenidos legalmente, conservar fuente y antigüedad y verificar deduplicación.

**Datos de Entrada Sintéticos:** Tres perfiles de plataforma simulados; eventos y denegaciones deterministas.
**Resultado Esperado:** Cero accesos no autorizados, intervenciones de equipos o duplicados. La falta de datos queda visible y no se sustituye por posición o jornada inventada. Una consulta de posición no acredita jornada del conductor ni integración de los 192 vehículos; la aceptación real requiere muestra autorizada por plataforma.
**Pass/Fail y Severidad:** Pass solo si se cumplen todos los criterios y se conserva evidencia reproducible; cualquier pérdida, acceso no autorizado o salida incorrecta implica Fail. Severidad alta para seguridad y evidencia.
**Entorno:** QA / Dobles de plataforma y capa de integración.

#### 9.0.4.9 CP-INT-09 — Ingesta Normalizada de Telemetría Comercial Webfleet vía Capa ACL

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-INT-09`
**Nivel y Tipología:** Prueba de Integración / Conectores Telemáticos Internacionales.
**Requerimiento Trazado:** Ensayo adicional de ingeniería; no sustituye controles contractuales.
**Precondiciones:** Adaptador `WebfleetConnectAdapter` configurado con autenticación OAuth 2.0.
**Pasos de Ejecución:**
- Ejecutar ciclo de consulta de posiciones `showOrderReportExtern` a la API de Webfleet.
- Parsear el payload CSV/JSON retornado por Webfleet Connect.
- Mapear estado de ignición y odómetro a la entidad canónica audIT.

**Datos de Entrada Sintéticos:** Respuesta sintética de Webfleet conteniendo camiones subcontratados operando en la Macrozona Sur.
**Resultado Esperado:** Conversión completa al esquema canónico en $< 100\text{ ms}$; persistencia de traza en TimescaleDB.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P2 (Crítica)**.
**Entorno:** CI Testcontainers.

#### 9.0.4.10 CP-INT-10 — Resiliencia y Reintentos (Exponential Backoff con Jitter) ante Caída de APIs Externas

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-INT-10`
**Nivel y Tipología:** Prueba de Integración / Tolerancia a Fallos y Circuit Breaker.
**Requerimiento Trazado:** Ensayo adicional de ingeniería; no sustituye controles contractuales.
**Precondiciones:** WireMock configurado para responder con HTTP 503 Service Unavailable durante 3 intentos y HTTP 200 en el cuarto.
**Pasos de Ejecución:**
- Invocar conector telemático con política Resilience4j / Polly configurada.
- Monitorear los reintentos: 1° intento (inmediato), 2° intento ($2\text{ s} \pm \text{jitter}), 3° intento (4\text{ s} \pm \text{jitter}), 4° intento (8\text{ s} \pm \text{jitter}$).
- Medir intervalos entre reintentos y verificar recepción exitosa en el 4° intento.

**Datos de Entrada Sintéticos:** Solicitud de sincronización de flota tercera.
**Resultado Esperado:** El sistema ejecuta exactamente 3 reintentos con desfases crecientes aleatorios (jitter), evitando inundar el servicio externo, y procesa la respuesta en el intento 4 exitosamente.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P2 (Crítica)**.
**Entorno:** CI Testcontainers / WireMock.

#### 9.0.4.11 CP-INT-11 — Contrato del ERP Contable como Único Emisor de DET y Contingencia Homologada

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-INT-11`
**Nivel y Tipología:** Ensayo de integración de ERP / Conformidad y bloqueo.
**Requerimiento Trazado:** RF-013, RNF-006.
**Precondiciones:** Vehículo detenido; orden y datos completos. Doble del ERP configurado con esquema e interfaz versionados. El fixture identifica un documento admitido y uno no emitido/no conforme; la validación fiscal real se homologa con el ERP y su proveedor, sin presumir API o contingencia certificada.
**Pasos de Ejecución:**
- Preparar datos desde la orden y enviarlos al ERP contable como único emisor, con identificador idempotente.
- Validar estado, identidad del emisor, firma, folio y asociación inequívoca a la orden según el contrato de integración. Una firma exclusiva de audIT no demuestra conformidad tributaria.
- Recuperar el documento conforme admitido por el fixture en cabina y cortar la cobertura. Confirmar disponibilidad local antes de autorizar movimiento.
- Repetir con documento ausente, rechazo, folio no válido, revocación o datos discordantes: debe mantenerse el bloqueo; no emitir un documento paralelo ni permitir salida con una promesa de regularización.
- Repetir el envío con el mismo identificador: debe existir una sola emisión y conservarse auditoría y respuesta del ERP. Verificar reconexión sin duplicados.

**Datos de Entrada Sintéticos:** Dos órdenes de prueba, mismo identificador repetido, estado `CONFORME` y estado `NO_EMITIDO`, documento/firma/folio y esquema de prueba versionados; manifestar emisor, orden y huellas. Reloj virtual del fixture.
**Resultado Esperado:** Disponible el documento conforme antes del movimiento; bloqueadas todas las variantes negativas, una única emisión por orden y evidencia de validación conservada. En pruebas de sistema/hardware se mide ≤90 s; en pruebas unitarias se valida el estado, sin sustituir el tiempo E2E.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: Alta cuando afecta seguridad o evidencia; mayor en objetivos adicionales.
**Entorno:** CI con doble de ERP. Homologación real del mecanismo de contingencia antes de despliegue; la falta de disponibilidad no se resuelve fingiendo certificación.

**Variante trazada a RF-013 (S3/T-12):** Solicitar al ERP un DET desde una orden válida y repetir la misma clave con timeout y respuesta tardía. Esperar un solo folio emitido por ERP, asociado a la orden y disponible en hasta 90 s. El componente audIT no emite documentos tributarios. Rechazar documento no emitido o con datos discordantes. En ensayo unitario se comprueba la regla con reloj controlado; latencia y comportamiento externo se acreditan en la prueba de integración, sistema o HIL asociada.

**Variante trazada a RNF-006 (S3/T-12):** Repetir solicitud, timeout, reenvío y recuperación de respuesta con la misma clave de orden. Esperar una emisión y un folio del ERP; audIT nunca emite. Variar contenido manteniendo clave: rechazar conflicto y conservar auditoría, sin emitir segundo documento. En ensayo unitario se comprueba la regla con reloj controlado; latencia y comportamiento externo se acreditan en la prueba de integración, sistema o HIL asociada.

#### 9.0.4.12 CP-INT-12 — Idempotencia Estricta en Emisión de D.E.T. ante Reintentos de Red

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-INT-12`
**Nivel y Tipología:** Prueba de Integración / Transaccionalidad Idempotente y Cero Duplicados.
**Requerimiento Trazado:** RF-013, RNF-006.
**Precondiciones:** Tabla de control de idempotencia configurada con clave primaria `idempotency_key`.
**Pasos de Ejecución:**
- Generar una clave de idempotencia UUID `a4b6c8d0-1234-4567-89ab-cdef01234567`.
- Enviar solicitud de emisión de D.E.T. con dicha clave. Simular corte de red justo antes de recibir el acuse.
- Reenviar la misma solicitud con idéntica clave de idempotencia 5 segundos después.
- Verificar el número de documentos D.E.T. generados en el ERP y en la base transaccional.

**Datos de Entrada Sintéticos:** Dos peticiones idénticas con la misma `Idempotency-Key` en cabecera HTTP.
**Resultado Esperado:** La primera petición procesa y almacena el resultado; la segunda petición reconoce la clave existente y retorna la misma respuesta previa con HTTP `200 OK` sin duplicar la emisión ni consumir un nuevo folio tributario.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P1 (Bloqueante)**.
**Entorno:** CI Testcontainers.

**Variante trazada a RF-013 (S3/T-12):** Solicitar al ERP un DET desde una orden válida y repetir la misma clave con timeout y respuesta tardía. Esperar un solo folio emitido por ERP, asociado a la orden y disponible en hasta 90 s. El componente audIT no emite documentos tributarios. Rechazar documento no emitido o con datos discordantes. En ensayo unitario se comprueba la regla con reloj controlado; latencia y comportamiento externo se acreditan en la prueba de integración, sistema o HIL asociada.

**Variante trazada a RNF-006 (S3/T-12):** Repetir solicitud, timeout, reenvío y recuperación de respuesta con la misma clave de orden. Esperar una emisión y un folio del ERP; audIT nunca emite. Variar contenido manteniendo clave: rechazar conflicto y conservar auditoría, sin emitir segundo documento. En ensayo unitario se comprueba la regla con reloj controlado; latencia y comportamiento externo se acreditan en la prueba de integración, sistema o HIL asociada.

#### 9.0.4.13 CP-INT-13 — Integración con Azure Key Vault HSM para Firma Digital de `EvidenciaJornada`

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-INT-13`
**Nivel y Tipología:** Prueba de Integración / Seguridad Criptográfica en Hardware (Cloud HSM).
**Requerimiento Trazado:** Ensayo adicional de ingeniería; no sustituye controles contractuales.
**Precondiciones:** Conexión segura configurada hacia Azure Key Vault (o simulador LocalStack / Azure SDK Mock) con clave asimétrica RSA 2048 / ECC P-256 respaldada en hardware HSM.
**Pasos de Ejecución:**
- Tomar el hash SHA-256 de una entidad `EvidenciaJornada`.
- Invocar la operación remota de firma `keyClient.sign(SignatureAlgorithm.ES256, digest)`.
- Recibir el blob de firma criptográfica y verificar su validez con la clave pública exportada.

**Datos de Entrada Sintéticos:** Digest SHA-256 de 32 bytes de jornada de chofer propio de San Bernardo.
**Resultado Esperado:** Firma criptográfica generada en $< 45\text{ ms}$; verificación de firma con clave pública resulta `true`.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P1 (Bloqueante)**.
**Entorno:** CI Runner / Azure Key Vault Managed Identity (o Mock).

#### 9.0.4.14 CP-INT-14 — Rotación Automática de Claves Simétricas en Azure Key Vault sin Caída de Servicio

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-INT-14`
**Nivel y Tipología:** Prueba de Integración / Gestión de Claves y Cero Downtime.
**Requerimiento Trazado:** Ensayo adicional de ingeniería; no sustituye controles contractuales.
**Precondiciones:** Microservicio de Privacidad configurado para cifrar datos con la versión activa de la clave de encriptación de datos (DEK).
**Pasos de Ejecución:**
- Cifrar RUT de chofer sintético con la versión V_1 de la clave.
- Disparar evento de rotación de clave en Key Vault, generando la versión V_2.
- Cifrar un nuevo RUT sintético; verificar que utiliza la versión V_2.
- Descifrar el dato cifrado previamente con V_1.

**Datos de Entrada Sintéticos:** Datos personales sintéticos cifrados en dos instantes distintos.
**Resultado Esperado:** El sistema utiliza V_2 para nuevas escrituras y mantiene la capacidad de descifrar registros históricos con V_1 mediante metadatos de clave, sin errores de descifrado ni reinicio de pods.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P1 (Bloqueante)**.
**Entorno:** CI Testcontainers / Key Vault Mock.

#### 9.0.4.15 CP-INT-15 — Integración con API de Concesionarias Viales (TAG) para Conciliación de Peajes

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-INT-15`
**Nivel y Tipología:** Prueba de Integración / Conciliación de Costos Operacionales.
**Requerimiento Trazado:** Ensayo adicional de ingeniería; no sustituye controles contractuales.
**Precondiciones:** Archivo de liquidación sintético de Autopista Central / Ruta del Maipo con 50 pasadas de TAG con timestamp y pórtico.
**Pasos de Ejecución:**
- Ingerir archivo de pasadas vía servicio `TollGatewaysIntegrationService.ingestTollRecords(file)`.
- Ejecutar algoritmo de conciliación espacial y temporal contra la traza de viajes activos de los 374 camiones.
- Imputar el costo del peaje a la orden de transporte correspondiente.

**Datos de Entrada Sintéticos:** Registro TAG de camión `LKJH-89` pasando por pórtico Buin a las 11:22:15Z del 2026-10-01.
**Resultado Esperado:** 100% de las pasadas válidas correlacionadas con el viaje en ruta con ventana de tolerancia $\pm 3\text{ minutos}$; asignación del costo directo a la orden.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P2 (Crítica)**.
**Entorno:** CI Testcontainers / PostgreSQL.

#### 9.0.4.16 CP-INT-16 — Conciliación de Carga de Diésel con Surtidor y Caudalímetro en San Bernardo

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-INT-16`
**Nivel y Tipología:** Prueba de Integración / IoT Industrial y Conciliación de Combustible.
**Requerimiento Trazado:** Ensayo adicional de ingeniería; no sustituye controles contractuales.
**Precondiciones:** Dispositivo concentrador de patio en San Bernardo conectado al caudalímetro digital del estanque propio de diésel.
**Pasos de Ejecución:**
- Simular carga de combustible de 380 litros al camión `TRK-SYNTH-042`.
- Caudalímetro emite trama MQTT `curimon/terminal/sbo/fuel/dispense` con identificador de manguera, litros y tag RFID del camión.
- Servicio de combustible captura la trama, valida contra la orden de trabajo abierta y actualiza el nivel de estanque e inventario.

**Datos de Entrada Sintéticos:** Mensaje MQTT sintético con litros dispensados y código de conductor.
**Resultado Esperado:** Registro de abastecimiento creado en PostgreSQL, contrastado contra odómetro de cabina y conciliado en $< 2\text{ segundos}$.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P2 (Crítica)**.
**Entorno:** CI Testcontainers (Mosquitto MQTT Broker + PostgreSQL).

#### 9.0.4.17 CP-INT-17 — Integración de Órdenes de Trabajo desde Formulario Web PWA de Talleres en Ruta

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-INT-17`
**Nivel y Tipología:** Prueba de Integración / PWA Móvil y Hoja de Vida Vehicular.
**Requerimiento Trazado:** RF-024, RF-025.
**Precondiciones:** API REST `/api/v1/maintenance/external-work-orders` activa.
**Pasos de Ejecución:**
- Enviar formulario multipart/form-data desde PWA de taller en ruta conteniendo detalle de reparación de frenos, factura escaneada (PDF/JPG) y odómetro actual.
- API valida autenticación temporal por token OTP enviado al taller.
- Almacenar documento adjunto en Azure Blob Storage (emulado) y metadata en base de datos.
- Actualizar hoja de vida del tractocamión.

**Datos de Entrada Sintéticos:** Reparación sintética en taller externo de Los Ángeles, adjunto JPG de 1,2 MB.
**Resultado Esperado:** Código HTTP `201 Created`, archivo subido y blob referenciado; hoja de vida del camión actualizada inmediatamente.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P3 (Mayor)**.
**Entorno:** CI Testcontainers (Azurite Blob Storage + PostgreSQL).

**Variante de taller desconectado y mantenimiento (RF-024/RF-025):** Capturar una intervención offline con taller, técnico, fecha, odómetro, trabajo, repuestos y evidencia. Reconectar dos veces: debe registrarse una sola intervención. Comparar umbral preventivo configurado en el fixture con el kilometraje trazable y generar aviso cuando se alcance; si el odómetro no es confiable, mostrar incertidumbre y no inventar recorrido.

**Variante trazada a RF-024 (S3/T-12):** Registrar una intervención offline de taller externo con técnico, equipo, fecha, odómetro, trabajo, repuestos y evidencia; reconectar dos veces. Esperar una sola intervención íntegra en hoja de vida e inventario actualizado una vez. Quitar técnico o repuesto obligatorio: rechazar o señalar registro incompleto, sin tratarlo como intervención válida. En ensayo unitario se comprueba la regla con reloj controlado; latencia y comportamiento externo se acreditan en la prueba de integración, sistema o HIL asociada.

#### 9.0.4.18 CP-INT-18 — Sincronización Bidireccional entre TimescaleDB e Índices Analíticos de Costos

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-INT-18`
**Nivel y Tipología:** Prueba de Integración / Pipeline ETL y Modelado Analítico de Datos.
**Requerimiento Trazado:** RF-016, RF-018.
**Precondiciones:** Vista continua materializada (continuous aggregate) en TimescaleDB calculando consumo de combustible por tramo vial.
**Pasos de Ejecución:**
- Insertar lote de 1.000 lecturas telemáticas con consumo y distancia.
- Forzar refresco de la política continua `CALL refresh_continuous_aggregate('fuel_by_route_daily', NULL, NULL);`.
- Consultar la vista agregada y validar que refleje los datos recién inyectados.

**Datos de Entrada Sintéticos:** Mediciones telemáticas de ruta Ruta 5 Sur sector Talca-Chillán.
**Resultado Esperado:** Agregación materializada actualizada en $< 250\text{ ms}$; métricas de dispersión disponibles para el microservicio de analítica.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P2 (Crítica)**.
**Entorno:** CI Testcontainers TimescaleDB.

**Variante trazada a RF-018 (S3/T-12):** Construir 12 meses de consumo y kilómetros por vehículo, ruta y conductor con condiciones registradas. En una cohorte de referencia, razones 2, 4, 4, 4, 5, 5, 7 y 9 tienen media 5 y varianza poblacional 4, en unidades sintéticas. Añadir una condición de carga sintética x con valores 0, 2, 2, 2, 3, 3, 5 y 7 y consumo y=2+x: el modelo lineal de referencia debe reproducir coeficientes 2 y 1 y residual cero en ese fixture. Un modelo alternativo debe declarar su oráculo independiente. Esta exactitud sintética no se promete para datos reales. El modelo debe conservar cohorte, período, condiciones, versión y dispersión reproducible; registros incompletos no se mezclan como cero. El benchmark de inserción no demuestra explicación de dispersión. En ensayo unitario se comprueba la regla con reloj controlado; latencia y comportamiento externo se acreditan en la prueba de integración, sistema o HIL asociada.

#### 9.0.4.19 CP-INT-19 — Publicación y Suscripción de Eventos de Geocerca en Kafka Event Hubs

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-INT-19`
**Nivel y Tipología:** Prueba de Integración / Arquitectura Orientada a Eventos (EDA).
**Requerimiento Trazado:** RF-010.
**Precondiciones:** Tópico Kafka `geofence.events.v1` configurado con particionamiento por `truckId`.
**Pasos de Ejecución:**
- El motor de geocercas detecta entrada de camión a terminal San Bernardo y publica evento `GEOFENCE_ENTERED`.
- Dos microservicios suscriptores independientes consumen el evento: (a) Servicio de Torre de Control, (b) Servicio de Sobreestadías.
- Verificar que ambos consumidores reciban y procesen el evento en paralelo.

**Datos de Entrada Sintéticos:** Evento JSON con `eventType: "ENTER"`, `geofenceId: "GEO-SBO-01"`, `truckId: "TRK-042"`, timestamp actual.
**Resultado Esperado:** Ambos servicios consumen el evento en $< 30\text{ ms}$, disparando la actualización en pantalla de Torre y el inicio del cronómetro de estadía.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P1 (Bloqueante)**.
**Entorno:** CI Testcontainers Kafka.

#### 9.0.4.20 CP-INT-20 — Integración de Despacho de OTP para e-POD vía Mensajería SMS/Email

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-INT-20`
**Nivel y Tipología:** Prueba de Integración / Notificaciones y Doble Factor de Conformidad.
**Requerimiento Trazado:** RF-012.
**Precondiciones:** Mock del proveedor de mensajería (Twilio / SendGrid) configurado.
**Pasos de Ejecución:**
- Chofer llega a destino y solicita generación de código OTP de recepción de carga.
- Servicio genera token numérico de 6 dígitos con vigencia de 10 minutos y envía solicitud HTTP al proveedor mock.
- Capturar petición saliente, validar formato y tiempo de respuesta.
- Ingresar OTP generado en endpoint de confirmación y validar aceptación.

**Datos de Entrada Sintéticos:** Solicitud e-POD para receptor sintético en bodega Puerto Montt.
**Resultado Esperado:** OTP despachado en $< 600\text{ ms}$; validación exitosa del código numérico; bloqueo de reintentos tras 3 fallos consecutivos.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P2 (Crítica)**.
**Entorno:** CI Testcontainers / Mock Server.

**Variante trazada a RF-012 (S3/T-12):** Emitir e-POD con receptor identificado, fecha, viaje y conformidad, primero con conectividad y después sin ella. La recepción debe quedar disponible en el día o al recuperar cobertura, conservando firma y datos tras reinicio y reintento. El OTP es una variante de identificación, no condición que impida entregar cuando no hay red. En ensayo unitario se comprueba la regla con reloj controlado; latencia y comportamiento externo se acreditan en la prueba de integración, sistema o HIL asociada.

#### 9.0.4.21 CP-INT-21 — Descarga Remota Automatizada de Tacógrafo Digital hacia Repositorio Cloud

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-INT-21`
**Nivel y Tipología:** Prueba de Integración / Protocolos DSRC y Custodia de Evidencia Legal.
**Requerimiento Trazado:** RF-007.
**Precondiciones:** Simulador de tacógrafo digital emitiendo tramas bajo estándar europeo/chileno VDO/Stoneridge vía socket TCP seguro.
**Pasos de Ejecución:**
- Iniciar sesión de descarga telemática remota autenticada con tarjeta de empresa digital.
- Transmitir archivo DDD binario del tacógrafo (bloque de 2 MB de memoria de masa y tarjeta de chofer).
- Servicio de backend recibe el archivo, valida su firma criptográfica intrínseca y almacena en almacenamiento WORM.

**Datos de Entrada Sintéticos:** Archivo binario `.ddd` sintético con registros de conducción de 30 días.
**Resultado Esperado:** Archivo descargado íntegramente en $< 40\text{ segundos}$, firma digital del tacógrafo validada, y registro asentado en base de datos.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P2 (Crítica)**.
**Entorno:** CI Testcontainers.

**Variante trazada a RF-007 (S3/T-12):** Descargar dos archivos originales de tacógrafo con conductores y vehículos distintos; conservar bytes y huellas originales, relacionar conductor y vehículo y clasificar nivel 1. Archivo truncado, alterado o sin identidad debe rechazarse o quedar pendiente de verificación, sin convertirse en evidencia válida. En ensayo unitario se comprueba la regla con reloj controlado; latencia y comportamiento externo se acreditan en la prueba de integración, sistema o HIL asociada.

#### 9.0.4.22 CP-INT-22 — API Gateway — Enrutamiento Seguro mTLS y Rate Limiting por Tenant

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-INT-22`
**Nivel y Tipología:** Prueba de Integración / Seguridad Perimetral y Gestión de Tráfico.
**Requerimiento Trazado:** Ensayo adicional de ingeniería; no sustituye controles contractuales.
**Precondiciones:** Instancia de API Gateway (Envoy / Traefik / Azure API Management Mock) con mTLS exigido en endpoints telemáticos y bucket de rate limiting de 100 req/s por cliente.
**Pasos de Ejecución:**
- Conectar cliente sin certificado digital TLS. Verificar rechazo de conexión a nivel de handshake SSL.
- Conectar cliente con certificado X.509 legítimo y realizar ráfaga de 120 peticiones en 1 segundo.
- Verificar que las primeras 100 peticiones respondan HTTP 200 y las 20 excedentes respondan HTTP 429 Too Many Requests.

**Datos de Entrada Sintéticos:** Certificados de prueba generados con OpenSSL; tráfico sintético HTTP GET.
**Resultado Esperado:** Conexión sin certificado rechazada (`SSL_ERROR_NO_CLIENT_CERT`); ráfaga controlada por rate limiter con cabecera `Retry-After`.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P1 (Bloqueante)**.
**Entorno:** CI Testcontainers.

#### 9.0.4.23 CP-INT-23 — Servicio de Consolidación de Costo Diario Preliminar por Viaje en $\le 24\text{ h}$

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-INT-23`
**Nivel y Tipología:** Prueba de Integración / Procesamiento de Cierre y Liquidación de Órdenes.
**Requerimiento Trazado:** RF-016, RF-017, RF-018.
**Precondiciones:** Viaje finalizado con orden de entrega POD suscrita hace 6 horas.
**Pasos de Ejecución:**
- Disparar worker de liquidación diaria `CostConsolidationWorker.processCompletedTrips()`.
- El servicio integra: (a) Kilómetros reales del odómetro CAN, (b) Litros consumidos de telemetría y surtidor, (c) Peajes TAG de concesionarias, (d) Tarifa pactada de transportista tercero o chofer propio.
- Generar la tupla consolidada en `trip_cost_summary`.

**Datos de Entrada Sintéticos:** Datos de viaje cerrado Santiago-Concepción con 510 km.
**Resultado Esperado:** Costo preliminar consolidado y persistido con estado `PRELIMINARY_COST_CALCULATED` en $< 150\text{ ms}$, separando costos fijos y variables.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P2 (Crítica)**.
**Entorno:** CI Testcontainers / PostgreSQL.

**Variantes de costo y dispersión (RF-016/RF-017/RF-018):** Usar dos viajes sintéticos cerrados en el mismo instante, uno propio y otro de tercero, con componentes separados de combustible, peaje y tarifa contractual. Retener intencionalmente una factura; el consolidado debe publicarse en ≤24 h indicando el faltante, sin duplicar costos. Aplicar una serie controlada de litros/km por vehículo, ruta y jornada con media y dispersión calculadas por el fixture; contrastar agregación y exponer registros no explicados, sin exigir un porcentaje de explicación inventado. El cálculo esperado se obtiene sumando los componentes disponibles del fixture, sin tratar tarifa de tercero como consumo de combustible propio.

**Variante trazada a RF-016 (S3/T-12):** Entregar dos viajes cerrados con factura de combustible tardía en uno. Publicar costo preliminar en hasta 24 h con faltante explícito y recalcular una vez al recibirla, sin duplicación. Diferenciar estudio por ruta/contrato disponible en M6, EDT 2.5, de costeo por viaje en producción M16, EDT 5.6; exigir ambos entregables en sus hitos. En ensayo unitario se comprueba la regla con reloj controlado; latencia y comportamiento externo se acreditan en la prueba de integración, sistema o HIL asociada.

**Variante trazada a RF-017 (S3/T-12):** Usar un viaje propio y uno de tercero con los mismos tipos de componentes conocidos. Para el propio sumar costos internos y para el tercero la tarifa contractual y componentes aplicables, sin sumar combustible interno de otro vehículo. Esperar sumas de la hoja de referencia, con desglose y estado preliminar o final. En ensayo unitario se comprueba la regla con reloj controlado; latencia y comportamiento externo se acreditan en la prueba de integración, sistema o HIL asociada.

#### 9.0.4.24 CP-INT-24 — Integración del Portal de Transportistas con Motor de Pre-Liquidaciones

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-INT-24`
**Nivel y Tipología:** Prueba de Integración / Portal de Autoservicio y Transparencia Contractual.
**Requerimiento Trazado:** RF-019, RF-020.
**Precondiciones:** Transportista tercero sintético con 8 viajes completados en el mes.
**Pasos de Ejecución:**
- Usuario transportista consulta el endpoint `GET /api/v1/carrier-portal/settlements/current`.
- El portal consulta el motor de liquidaciones, aplicando descuentos de anticipos de combustible en estanque y peajes anticipados.
- Retornar desglose transparente viaje a viaje con estado de pago.

**Datos de Entrada Sintéticos:** Token de sesión del transportista `CARRIER-SYNTH-088`.
**Resultado Esperado:** Código HTTP `200 OK` con balance conciliado en $< 90\text{ ms}$; valores calculados coinciden exactamente con los registros contables.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P1 (Bloqueante)**.
**Entorno:** CI Testcontainers.

**Variante trazada a RF-019 (S3/T-12):** Cerrar un mes para 148 transportistas sintéticos, con viajes, tarifas y descuentos de referencia. Esperar una liquidación por titular con sumas exactas dentro de un día hábil del cierre mensual, no mensual. Medir proporción de correcciones manuales sobre liquidaciones emitidas: con 148, una corrección cumple menos de 1 por ciento y dos no. Registrar calendario hábil y denominador. En ensayo unitario se comprueba la regla con reloj controlado; latencia y comportamiento externo se acreditan en la prueba de integración, sistema o HIL asociada.

#### 9.0.4.25 CP-INT-25 — Sincronización Asíncrona entre Azure Chile Central y Réplica Brazil South (DRP)

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-INT-25`
**Nivel y Tipología:** Prueba de Integración / Recuperación ante Desastres y Replicación Cloud.
**Requerimiento Trazado:** RNF-014.
**Precondiciones:** Enlace de replicación configurado entre clúster primario (Virginia) y secundario (São Paulo).
**Pasos de Ejecución:**
- Insertar ráfaga transaccional de 50 órdenes de transporte en el clúster primario.
- Monitorear el retraso de replicación (replication lag) en la réplica de lectura secundaria.
- Validar consistencia de datos en el sitio secundario tras 60 segundos.

**Datos de Entrada Sintéticos:** Inserción de 50 registros con timestamp de precisión microsegundo.
**Resultado Esperado:** Retraso de replicación medido $< 120\text{ segundos}$ (muy inferior al límite contractual de 15 minutos de RPO); 100% de los registros presentes e idénticos en Brazil South.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P1 (Bloqueante)**.
**Entorno:** Staging Azure Multi-Region.

**Variante trazada a RNF-014 (S3/T-12):** Versionar dominios y plazos: jornada cinco años, documentos/viajes/liquidación seis, siniestros diez, habilitación vigencia más cinco, SUSPEL cinco, esperas tres, series dos en línea con agregación. Con reloj virtual antes/al cumplir cada umbral, retener mientras exista obligación o suspensión y aplicar después la política aprobada. Revocar permiso detiene captura/acceso comprendidos, sin borrado anticipado; cotejar réplica y original. En ensayo unitario se comprueba la regla con reloj controlado; latencia y comportamiento externo se acreditan en la prueba de integración, sistema o HIL asociada.

### 9.0.5 Batería 3: Pruebas de Sistema y E2E (20 Casos: `CP-SYS-01` a `CP-SYS-20`)

Esta batería somete la solución completa a pruebas punta a punta (End-to-End), simulando flujos reales de la operación de Transportes Curimón S.A., integrando la Torre de Control 24x7, terminales, camiones en ruta, recintos de clientes y portales web.

**Variante de retención en réplica (RNF-014):** Replicar muestras de todos los dominios de conservación de CP-SEC-08; contrastar políticas, metadatos, huellas y suspensión de borrado en ambos sitios. Reiniciar la replicación y confirmar que no acorta plazos ni borra evidencia por una revocación. Registrar retraso real y aplicar RPO ≤15 min a datos críticos, como control separado de FEP02 RT-07.04.

#### 9.0.5.1 CP-SYS-01 — Flujo E2E Completo de Despacho — De Orden de Transporte a Cierre de Viaje

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-SYS-01`
**Nivel y Tipología:** Prueba de Sistema E2E / Flujo Transaccional Troncal de Negocio.
**Requerimiento Trazado:** RF-001, RNF-010.
**Precondiciones:**
- Chofer propio habilitado con 0 horas de conducción en el día y documentos al día.
- Tractocamión propio con telemetría operativa en patio de San Bernardo.

**Pasos de Ejecución:**
- Crear Orden de Transporte (OT) en el portal de despachos para cliente retail (Santiago a Valparaíso).
- Ejecutar asignación automática; comprobar validación bloqueante en $< 30\text{ s}$.
- Emitir Documento Electrónico de Transporte (DET) integrado con ERP contable.
- Simular salida del terminal (detección de salida por geocerca y enclavamiento de pantalla a bordo al acelerar).
- Simular recorrido con peajes e ingreso al recinto del cliente en Valparaíso.
- Confirmar entrega mediante firma digital e-POD con OTP.
- Verificar cierre de viaje y consolidación preliminar de costos en base de datos.

**Datos de Entrada Sintéticos:** OT `OT-E2E-2026-001`, Chofer `DRV-SYNTH-101`, Tracto `LKJH-89`, Carga 22 ton paletizadas.
**Resultado Esperado:** Transición ordenada de estados de la orden (`CREADA` $\rightarrow `ASIGNADA` \rightarrow$ `EN_RUTA` $\rightarrow$ `EN_DESTINO` $\rightarrow `ENTREGADA` \rightarrow$ `LIQUIDADA`), sin intervención manual correctiva.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P1 (Bloqueante)**.
**Entorno:** Staging AKS / Emuladores Telemáticos IoT.

**Variante trazada a RF-001 (S3/T-12):** Preparar seis asignaciones con los cuatro factores presentes: fuentes de jornada 1, 2, 3, 4, 5 y ninguna. Con saldo y habilitaciones válidos, comprobar la cascada general: asigna en 1–4, asigna con marca y responsabilidad del transportista en 5, y bloquea sin fuente. Repetir el nivel 4 en la modalidad de datos de S3: sin atestación firmada no asignar; con atestación válida de nivel 5 asignar con marca. Aplicar RN-04 únicamente a su excepción de caída de fuente, nunca a un incumplimiento legal. Retirar por separado cada factor: todos deben bloquear aun con dos firmas. Medir las tres salidas de extremo a extremo en hasta 30 s; el tiempo unitario no acredita ese límite. En ensayo unitario se comprueba la regla con reloj controlado; latencia y comportamiento externo se acreditan en la prueba de integración, sistema o HIL asociada.

**Variante trazada a RNF-010 (S3/T-12):** Conciliar inventario técnico y modelo económico de 36 meses: cantidades, unidades, periodicidad y cobertura de nube, enlaces, licencias, soporte, reposición, retiro y contingencia. Esperar cero partidas omitidas o duplicadas y horizonte íntegro; precios solo en oferta económica. El escalamiento de pods no demuestra exhaustividad del costo de operación. En ensayo unitario se comprueba la regla con reloj controlado; latencia y comportamiento externo se acreditan en la prueba de integración, sistema o HIL asociada.

#### 9.0.5.2 CP-SYS-02 — Flujo E2E de Viaje en Ruta y Detección Automática de Hitos Georreferenciados

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-SYS-02`
**Nivel y Tipología:** Prueba de Sistema E2E / Georreferenciación y Máquina de Estados de Viaje.
**Requerimiento Trazado:** Ensayo adicional de ingeniería; no sustituye controles contractuales.
**Precondiciones:** Viaje activo en ruta Troncal Ruta 5 Sur (San Bernardo a Concepción, 510 km).
**Pasos de Ejecución:**
- Inyectar coordenadas progresivas del trayecto simulando velocidad de $75\text{ km/h}$.
- Detectar paso por hitos: Peaje Angostura (km 54), Bypass Rancagua (km 85), Terminal San Fernando (km 138), y Peaje Río Claro (km 220).
- Verificar que cada hito dispare un evento en Kafka, actualice la posición en la Torre 24x7 y recalcule el ETA hacia Concepción.

**Datos de Entrada Sintéticos:** Serie de 1.200 puntos GPS interpolados en el trazado de la Ruta 5 Sur.
**Resultado Esperado:** Hitos georreferenciados reconocidos con precisión de $\pm 20\text{ metros}$; actualización de la pantalla del despachador en tiempo real ($< 2\text{ segundos}$ tras cruzar el hito).
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P2 (Crítica)**.
**Entorno:** Staging AKS / Mock Geográfico.

#### 9.0.5.3 CP-SYS-03 — Detección Automática de Sobreestadías en Patio de Cliente y Sustento Probatorio

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-SYS-03`
**Nivel y Tipología:** Prueba de Sistema E2E / Registro Automatizado y Liquidación Comercial.
**Requerimiento Trazado:** RF-010, RF-011, RNF-007.
**Precondiciones:** Geocerca de cliente agroexportador con tiempo de espera libre pactado de 2 horas.
**Pasos de Ejecución:**
- Camión arriba al patio a las 10:00:00Z (evento de entrada por geocerca).
- El conductor apaga el motor a las 10:08:00Z; sensor de movimiento confirma inmovilidad.
- La permanencia se extiende hasta las 16:30:00Z (6 horas y 30 minutos totales de estadía).
- Camión enciende motor y abandona el patio a las 16:35:00Z (evento de salida por geocerca).
- El motor de liquidación genera el informe de sobreestadía (Demurrage Certificate).

**Datos de Entrada Sintéticos:** Geocerca `GEO-AGRO-CURICO-04`, Tracto `TRK-088`, Estadía total: 390 min (270 min facturables).
**Resultado Esperado:** Certificado PDF/JSON generado automáticamente con diagrama de permanencia, coordenadas de entrada/salida, traza de motor apagado y cobro liquidado por 9 tramos de 30 minutos, con no repudio.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P2 (Crítica)**.
**Entorno:** Staging AKS / Motor de Liquidación.

**Variante trazada a RF-010 (S3/T-12):** Versionar 1.400 polígonos y puntos de entrada, límite interior y exterior en el mismo sistema de coordenadas; ejecutar replay automático. Esperar una entrada y una salida por cruce válido, ninguna para puntos exteriores y deduplicación de reintentos, sin equipos en instalaciones del cliente ni acciones del conductor. En ensayo unitario se comprueba la regla con reloj controlado; latencia y comportamiento externo se acreditan en la prueba de integración, sistema o HIL asociada.

**Variante trazada a RF-011 (S3/T-12):** Usar un contrato sintético con 120 min libres y bloques facturables de 30 min, permanencias de 119, 120 y 330 min. Esperar 0, 0 y 210 min facturables respectivamente, siete bloques en la última. Conservar entrada, salida y contrato. Repetir con otro tiempo libre contractual para verificar que no se fija universalmente en dos horas. En ensayo unitario se comprueba la regla con reloj controlado; latencia y comportamiento externo se acreditan en la prueba de integración, sistema o HIL asociada.

**Variante trazada a RNF-007 (S3/T-12):** Ejecutar detección de entrada, salida y espera con inventario de instalaciones de cliente vacío para componentes audIT. Esperar hitos automáticos desde señales del vehículo y servidor, cero instalaciones en cliente y cero acciones del conductor; agregar dependencia de equipo de garita debe fallar. En ensayo unitario se comprueba la regla con reloj controlado; latencia y comportamiento externo se acreditan en la prueba de integración, sistema o HIL asociada.

#### 9.0.5.4 CP-SYS-04 — Emisión y Firma Digital de e-POD con OTP y Captura Fotográfica de Precintos

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-SYS-04`
**Nivel y Tipología:** Prueba de Sistema E2E / Prueba de Entrega Digital (e-POD) y Cero Papel.
**Requerimiento Trazado:** RF-012.
**Precondiciones:** Chofer en andén de destino con la App Móvil PWA lista para entrega de carga.
**Pasos de Ejecución:**
- Chofer inicia flujo de entrega en la PWA; el receptor de la bodega recibe código OTP en su teléfono.
- El chofer ingresa el código OTP dictado por el receptor.
- El receptor plasma su firma gráfica en la pantalla táctil (firma en cristal).
- La PWA captura dos fotografías: precinto de seguridad del semirremolque intacto y guía de despacho física timbrada.
- La PWA consolida el paquete e-POD, calcula hash SHA-256 y sincroniza con el backend.

**Datos de Entrada Sintéticos:** OTP `654321`, firma en cristal (SVG/PNG base64), dos imágenes comprimidas (JPEG, 800 KB c/u).
**Resultado Esperado:** Documento e-POD generado con sello temporal RFC 3161, notificaciones inmediatas por email al cliente exportador con copia del e-POD adjunto, y orden marcada como `DELIVERED_CONFIRMED`.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P1 (Bloqueante)**.
**Entorno:** Staging AKS / Dispositivos Móviles PWA.

**Variante trazada a RF-012 (S3/T-12):** Emitir e-POD con receptor identificado, fecha, viaje y conformidad, primero con conectividad y después sin ella. La recepción debe quedar disponible en el día o al recuperar cobertura, conservando firma y datos tras reinicio y reintento. El OTP es una variante de identificación, no condición que impida entregar cuando no hay red. En ensayo unitario se comprueba la regla con reloj controlado; latencia y comportamiento externo se acreditan en la prueba de integración, sistema o HIL asociada.

#### 9.0.5.5 CP-SYS-05 — Operación en Modo Mixto — Convivencia de Flota Propia (Nivel 2/3) y Terceros (Nivel 5)

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-SYS-05`
**Nivel y Tipología:** Prueba de Sistema E2E / Transición de Flota y Cascada Probatoria.
**Requerimiento Trazado:** RF-003, RF-026, RF-028, RNF-003, RNF-011.
**Precondiciones:** Torre de Programación operando simultáneamente con:
   Camión Propio `TRK-010` (equipado con Gateway audIT + Technoton CANCrocodile, Nivel 2 instrumental).
   Camión Subcontratado `TRK-305` (con acceso autorizado a datos de posición de plataforma de ensayo, posición comercial; jornada por atestación separada del transportista).
**Pasos de Ejecución:**
- Despachar viaje simultáneo para ambos camiones en la misma ruta Santiago-San Fernando.
- Monitorear la consola de la Torre de Control 24x7.
- Verificar que la Torre visualice ambos camiones en el mismo mapa unificado sin duplicidad de marcadores.
- Comprobar que en la ficha técnica del viaje se diferencie claramente el nivel probatorio: Nivel 2 (equipo a bordo con conductor identificado) vs posición comercial y Nivel 5 (atestación firmada del transportista, registrada separadamente).

**Datos de Entrada Sintéticos:** Dos viajes sintéticos paralelos despachados a las 08:30:00Z.
**Resultado Esperado:** Coexistencia armónica en la plataforma; la Torre opera sin fricciones y las reglas de liquidación y jornada aplican los algoritmos diferenciados según el nivel probatorio canónico.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P1 (Bloqueante)**.
**Entorno:** Staging AKS / Torre 24x7.

**Variante de jornada previa y adhesión (RF-003/RF-026/RNF-003):** Crear propietario, dos camiones y conductores sintéticos, permisos por destinatario/vigencia y evidencia previa con origen y sello. Registrar invitación, aceptación, rechazo y revocación; comprobar que no se activa integración no autorizada. Intentar asignar con jornada previa ausente, vencida o no verificable: debe bloquearse, sin asumir cero horas. Repetir con evidencia válida y saldo suficiente; aprobar solo después de las verificaciones obligatorias.

**Variante trazada a RF-003 (S3/T-12):** Crear dos conductores externos con igual viaje propuesto y jornadas previas distintas: descanso continuo de 8 h y de 6 h en la ventana de 24 h del fixture. Con permiso y evidencia verificable, el primero dispone de descanso y el segundo bloquea. Repetir sin fuente, con atestación firmada del dueño y con permiso revocado: bloquear sin fuente, asignar con marca cuando la atestación acredita saldo válido y cesar la consulta revocada. No divulgar coordenadas de otros clientes. En ensayo unitario se comprueba la regla con reloj controlado; latencia y comportamiento externo se acreditan en la prueba de integración, sistema o HIL asociada.

**Variante trazada a RF-026 (S3/T-12):** Calcular los ocho indicadores mensuales de adhesión de S3 con sus denominadores. Con 148 titulares, 104 en M16 y 134 en M21 cumplen las metas de al menos 70 y 90 por ciento; 103 y 133 no. En M9, menos del 40 por ciento firmado activa el escenario previsto: 59 de 148 no llega; 60 supera el umbral. Conservar serie mensual, estados de invitación/aceptación/rechazo/revocación y medida correctiva, sin inventar adhesiones reales. En ensayo unitario se comprueba la regla con reloj controlado; latencia y comportamiento externo se acreditan en la prueba de integración, sistema o HIL asociada.

**Variante trazada a RF-028 (S3/T-12):** Crear transportistas en modalidades completa, de datos y sin adhesión según S3; comprobar nivel 2, reposo de nivel 4 con atestación de nivel 5 y validación documental con y sin atestación firmada; visualizar modalidad, fuente, nivel y veredicto por separado. Comprobar la cascada de niveles 1 a 4 con asignación y el nivel 5 con asignación con marca y responsabilidad registrada, sin bloqueos legales. En la modalidad de datos, exigir la atestación firmada que complementa el reposo del camión: con ella asignar con marca y sin ella bloquear la asignación. En el estado sin adhesión, la validación documental con atestación válida permite asignar con marca; sin atestación no hay veredicto habilitante ni asignación. Sin fuente bloquear, con excepción sólo según RN-04; con incumplimiento legal bloquear en todas las modalidades. El nivel 0 voluntario no cambia el veredicto. En ensayo unitario se comprueba la regla con reloj controlado; latencia y comportamiento externo se acreditan en la prueba de integración, sistema o HIL asociada.

**Variante trazada a RNF-011 (S3/T-12):** Durante convivencia TMS 2013/nuevo sistema, desviar por función y repetir una misma orden por ambas rutas; esperar un solo viaje y ningún despacho que eluda bloqueo. Restaurar ruta anterior sin detener la flota. Assignment, tracking y liquidación pasan en M16, órdenes y tarifas cliente en M21; solo lectura hasta M24 según S3. El ERP contable permanece separado. En ensayo unitario se comprueba la regla con reloj controlado; latencia y comportamiento externo se acreditan en la prueba de integración, sistema o HIL asociada.

#### 9.0.5.6 CP-SYS-06 — Despacho Bloqueante para Unidades de Sustancias Peligrosas (D.S. 298 y D.S. 43)

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-SYS-06`
**Nivel y Tipología:** Prueba de Sistema E2E / Seguridad Química y Cumplimiento Normativo SUSPEL.
**Requerimiento Trazado:** RF-006.
**Precondiciones:**
- Orden de transporte con carga química peligrosa (Ácido Sulfúrico UN 1830, Clase 8).
- Tractocamión `TRK-SUSP-01` asignado con resolución sanitaria D.S. 43 al día.

**Pasos de Ejecución:**
- Asignar un conductor cuya certificación de curso de transporte de sustancias peligrosas (D.S. 298) venció ayer.
- Intentar autorizar el despacho en el sistema.
- Reasignar a un conductor con certificación vigente.
- Escanear mediante PWA el código QR de la Hoja de Datos de Seguridad (HDS) y verificar presencia de extintores y kit de derrames.
- Proceder al despacho definitivo.

**Datos de Entrada Sintéticos:** Carga UN 1830, Chofer con curso vencido $\rightarrow$ Chofer con curso vigente, QR de HDS válida.
**Resultado Esperado:** En el paso 2, el sistema bloquea terminantemente el viaje con alerta sonora y visual en Torre (`HAZMAT_DRIVER_CERTIFICATE_EXPIRED`); en el paso 5, tras subsanar todas las exigencias legales, autoriza la salida.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P1 (Bloqueante)**.
**Entorno:** Staging AKS / Módulo SUSPEL.

**Variante trazada a RF-006 (S3/T-12):** Preparar 18 unidades SUSPEL sintéticas, cada una con carga efectiva, DET emitido por ERP, conductor y lista firmada. La muestra conforme vincula esos elementos y permite salida si los otros factores cumplen. Cambiar carga respecto del documento, quitar firma o vencer habilitación: cada variante bloquea. La compatibilidad química por sí sola no acredita este requisito. En ensayo unitario se comprueba la regla con reloj controlado; latencia y comportamiento externo se acreditan en la prueba de integración, sistema o HIL asociada.

#### 9.0.5.7 CP-SYS-07 — Bloqueo Preventivo Pre-Despacho por Infracción de Jornada Laboral (Art. 25 bis CT)

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-SYS-07`
**Nivel y Tipología:** Prueba de Sistema E2E / Enclavamiento Legal Laboral.
**Requerimiento Trazado:** RF-002, RF-003.
**Precondiciones:** Conductor propio que finalizó un viaje hace 4 horas, habiendo conducido 5 horas continuas (descanso obligatorio pendiente de 2 horas satisfecho, pero descanso diario de 8 horas incompleto en ventana de 24 h).
**Pasos de Ejecución:**
- Despachador intenta programar al conductor en un viaje nocturno San Bernardo a Puerto Montt (12 horas estimadas).
- El motor de asignación bloqueante evalúa el historial del chofer en Redis y PostgreSQL.
- Comprobar la respuesta visual en la consola de la Torre 24x7.

**Datos de Entrada Sintéticos:** Solicitud de despacho para chofer `DRV-SYNTH-115` con déficit de descanso diario.
**Resultado Esperado:** Bloqueo automático en $< 2\text{ segundos}$ con mensaje explicativo: "Asignación Bloqueada por Ley: Conductor registra déficit de 4,0 horas de descanso diario continuo (Art. 25 bis Código del Trabajo)". El botón de confirmación queda inhabilitado.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P1 (Bloqueante)**.
**Entorno:** Staging AKS / Consola Torre.

#### 9.0.5.8 CP-SYS-08 — Bloqueo Preventivo Pre-Despacho por Vigencia Vencida (Revisión Técnica / SOAP)

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-SYS-08`
**Nivel y Tipología:** Prueba de Sistema E2E / Control de 6.000 Vigencias Vivas de Flota.
**Requerimiento Trazado:** RF-005.
**Precondiciones:** Semirremolque portacontenedor `TRL-SYNTH-019` con Revisión Técnica caducada hace 48 horas.
**Pasos de Ejecución:**
- Despachador intenta enganchar el semirremolque `TRL-SYNTH-019` a un tractocamión para despacho portuario en Valparaíso.
- El sistema consulta las vigencias en Redis Cluster.
- Evaluar el estado de la asignación de equipo.

**Datos de Entrada Sintéticos:** Intento de despacho con equipo en tabla `equipment_compliance` con fecha de caducidad en el pasado.
**Resultado Esperado:** Bloqueo inmediato del semirremolque; el sistema sugiere automáticamente las 3 ramplas sustitutas más cercanas disponibles en el patio con documentación al día.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P1 (Bloqueante)**.
**Entorno:** Staging AKS / Módulo de Flota.

**Variante trazada a RF-005 (S3/T-12):** Generar 6.000 vigencias sintéticas con titular, responsable, fecha y respaldo. Fijar reloj y fechas a 61, 60, 31, 30, 8 y 7 días del vencimiento; esperar alertas exactamente en 60, 30 y 7, sin duplicación al repetir. Vencer cada tipo habilitante por separado: cualquier vencimiento bloquea; renovar con documento válido libera únicamente ese impedimento. En ensayo unitario se comprueba la regla con reloj controlado; latencia y comportamiento externo se acreditan en la prueba de integración, sistema o HIL asociada.

#### 9.0.5.9 CP-SYS-09 — Optimización y Asignación Automática de Viaje de Retorno en Vacío (ALNS)

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-SYS-09`
**Nivel y Tipología:** Prueba de Sistema E2E / Inteligencia Operacional y Reducción de Kilómetros Vacíos.
**Requerimiento Trazado:** RF-015.
**Precondiciones:** Camión `TRK-055` descargando carga industrial en Puerto Montt; disponibilidad prevista en 2 horas. En la base de datos existen 3 solicitudes de carga hacia el norte (Osorno a Temuco, Llanquihue a Santiago, y Puerto Varas a Concepción).
**Pasos de Ejecución:**
- El sistema dispara el motor ALNS al detectarse la fase final de descarga (e-POD iniciado).
- El algoritmo analiza tiempos de viaje, horas de conducción restantes del chofer, peso de carga y compatibilidad de rampla.
- Presentar a la Torre la asignación óptima de retorno recomendada.

**Datos de Entrada Sintéticos:** Estado de camión, 3 órdenes de retorno en radio de 50 km de Puerto Montt.
**Resultado Esperado:** El sistema recomienda la orden Llanquihue-Santiago (menor desvío en vacío: solo 18 km desde Puerto Montt), reduciendo los km muertos del viaje y maximizando el margen operacional.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P2 (Crítica)**.
**Entorno:** Staging AKS / Microservicio ALNS.

**Variante trazada a RF-015 (S3/T-12):** Usar las dos ofertas de retorno del fixture de CP-UNIT-15 con márgenes analíticos 970 y 780, en unidades sintéticas ajenas a precios de oferta. Con ambas viables elegir la primera; sin jornada, habilitación, capacidad, compatibilidad o ventana de entrega en la primera, descartarla y elegir la segunda viable. Si ninguna cumple RN-09, no proponer retorno. En ensayo unitario se comprueba la regla con reloj controlado; latencia y comportamiento externo se acreditan en la prueba de integración, sistema o HIL asociada.

#### 9.0.5.10 CP-SYS-10 — Ciclo E2E de Pre-Liquidación a Transportistas Subcontratados con Descuentos

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-SYS-10`
**Nivel y Tipología:** Prueba de Sistema E2E / Cierre Financiero y Liquidación de Terceros.
**Requerimiento Trazado:** RF-017, RF-019.
**Precondiciones:** Quincena contable cerrada. Transportista subcontratado con 6 viajes completados con e-POD conforme, 2 abastecimientos de combustible en estanque San Bernardo y 14 pasadas por pórticos TAG.
**Pasos de Ejecución:**
- Ejecutar proceso de liquidación automática mensual.
- Verificar consolidación de fletes devengados según tarifa por tramo/tonelada.
- Aplicar deducción automática de los litros de diésel consumidos a precio de costo interno.
- Aplicar deducción de pasadas de peaje TAG conciliadas.
- Publicar borrador de liquidación en el Portal de Transportistas para visado del dueño del camión.

**Datos de Entrada Sintéticos:** Registros de fletes, surtidor y peajes del transportista `CARRIER-SYNTH-045`.
**Resultado Esperado:** Pre-liquidación emitida con balance matemático exacto; detalle íntegro visible en el portal en $< 2\text{ minutos}$ post-cierre (reducción del histórico de 9 días a tiempo real).
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P1 (Bloqueante)**.
**Entorno:** Staging AKS / Portal Transportistas.

**Variante trazada a RF-017 (S3/T-12):** Usar un viaje propio y uno de tercero con los mismos tipos de componentes conocidos. Para el propio sumar costos internos y para el tercero la tarifa contractual y componentes aplicables, sin sumar combustible interno de otro vehículo. Esperar sumas de la hoja de referencia, con desglose y estado preliminar o final. En ensayo unitario se comprueba la regla con reloj controlado; latencia y comportamiento externo se acreditan en la prueba de integración, sistema o HIL asociada.

**Variante trazada a RF-019 (S3/T-12):** Cerrar un mes para 148 transportistas sintéticos, con viajes, tarifas y descuentos de referencia. Esperar una liquidación por titular con sumas exactas dentro de un día hábil del cierre mensual, no mensual. Medir proporción de correcciones manuales sobre liquidaciones emitidas: con 148, una corrección cumple menos de 1 por ciento y dos no. Registrar calendario hábil y denominador. En ensayo unitario se comprueba la regla con reloj controlado; latencia y comportamiento externo se acreditan en la prueba de integración, sistema o HIL asociada.

#### 9.0.5.11 CP-SYS-11 — Documento de Transporte Conforme antes de Movimiento en Punto sin Cobertura

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-SYS-11`
**Nivel y Tipología:** Ensayo de sistema E2E / Conformidad y bloqueo.
**Requerimiento Trazado:** RF-014, RNF-006.
**Precondiciones:** Vehículo detenido; orden y datos completos. Doble del ERP configurado con esquema e interfaz versionados. El fixture identifica un documento admitido y uno no emitido/no conforme; la validación fiscal real se homologa con el ERP y su proveedor, sin presumir API o contingencia certificada.
**Pasos de Ejecución:**
- Preparar datos desde la orden y enviarlos al ERP contable como único emisor, con identificador idempotente.
- Validar estado, identidad del emisor, firma, folio y asociación inequívoca a la orden según el contrato de integración. Una firma exclusiva de audIT no demuestra conformidad tributaria.
- Recuperar el documento conforme admitido por el fixture en cabina y cortar la cobertura. Confirmar disponibilidad local antes de autorizar movimiento.
- Repetir con documento ausente, rechazo, folio no válido, revocación o datos discordantes: debe mantenerse el bloqueo; no emitir un documento paralelo ni permitir salida con una promesa de regularización.
- Repetir el envío con el mismo identificador: debe existir una sola emisión y conservarse auditoría y respuesta del ERP. Verificar reconexión sin duplicados.

**Datos de Entrada Sintéticos:** Dos órdenes de prueba, mismo identificador repetido, estado `CONFORME` y estado `NO_EMITIDO`, documento/firma/folio y esquema de prueba versionados; manifestar emisor, orden y huellas. Reloj virtual del fixture.
**Resultado Esperado:** Disponible el documento conforme antes del movimiento; bloqueadas todas las variantes negativas, una única emisión por orden y evidencia de validación conservada. En pruebas de sistema/hardware se mide ≤90 s; en pruebas unitarias se valida el estado, sin sustituir el tiempo E2E.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: Alta cuando afecta seguridad o evidencia; mayor en objetivos adicionales.
**Entorno:** staging/HIL con dispositivo y contrato ERP de ensayo. Homologación real del mecanismo de contingencia antes de despliegue; la falta de disponibilidad no se resuelve fingiendo certificación.

#### 9.0.5.12 CP-SYS-12 — Flujo E2E de Gestión de Discrepancias en Entrega (Rechazo Parcial y Daño)

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-SYS-12`
**Nivel y Tipología:** Prueba de Sistema E2E / Gestión de No Conformidades y Logística Inversa.
**Requerimiento Trazado:** Ensayo adicional de ingeniería; no sustituye controles contractuales.
**Precondiciones:** Chofer entregando 20 pallets de fruta fresca en Terminal Portuario de Valparaíso.
**Pasos de Ejecución:**
- Receptor detecta que 2 pallets presentan daño mecánico en embalaje y rechaza recibirlos.
- Chofer registra en PWA la entrega parcial: 18 pallets recibidos conforme, 2 pallets rechazados.
- Capturar fotografías de los pallets dañados y registrar causa (Daño de estiba).
- Receptor firma e-POD con reserva de conformidad.
- El sistema notifica de inmediato a la Torre 24x7 y al departamento de seguros de Curimón S.A.

**Datos de Entrada Sintéticos:** Discrepancia en OT: 18 conformes, 2 rechazados, código de anomalía `DAMAGED_CARGO`.
**Resultado Esperado:** Acta de entrega parcial firmada; alerta P2 en Torre 24x7 con fotografías adjuntas para apertura de siniestro con la compañía de seguros; orden reencaminada a logística inversa.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P2 (Crítica)**.
**Entorno:** Staging AKS / App Móvil PWA.

#### 9.0.5.13 CP-SYS-13 — Trazabilidad Térmica Continua y Alarma en Cadena de Frío (Rampla Reefer)

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-SYS-13`
**Nivel y Tipología:** Prueba de Sistema E2E / Telemetría de Frío y Preservación de Carga.
**Requerimiento Trazado:** Ensayo adicional de ingeniería; no sustituye controles contractuales.
**Precondiciones:** Rampla reefer transportando salmón fresco desde Puerto Montt a Santiago. Rango térmico de consigna: $-1{,}5\text{ }^\circ\text{C} a +1{,}5\text{ }^\circ\text{C}$.
**Pasos de Ejecución:**
- Inyectar telemetría térmica normal (temperatura media $+0{,}2\text{ }^\circ\text{C}$).
- Simular fallo en el equipo de refrigeración Thermo King / Carrier; la temperatura sube progresivamente a $+3{,}8\text{ }^\circ\text{C}$ en 20 minutos.
- Verificar que la plataforma detecte la desviación térmica al superar $+2{,}0\text{ }^\circ\text{C}$.
- Comprobar disparo de alerta sonora prioritaria en Torre de Control y notificación push en cabina del chofer.

**Datos de Entrada Sintéticos:** Anuncios de baliza Bluetooth con curva térmica sintética, identificador y cadencia versionados; no se atribuye cadencia al fabricante sin comprobación.
**Resultado Esperado:** Alarma crítica `COLD_CHAIN_BREACH_CRITICAL` disparada en $< 45\text{ segundos}$ tras el rebase térmico; despachador activa protocolo de desvío a taller técnico frigorífico en ruta.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P1 (Bloqueante)**.
**Entorno:** Staging AKS / Banco HIL Térmico.

#### 9.0.5.14 CP-SYS-14 — Flujo E2E de Relevo de Tripulación en Ruta con Cierre y Apertura de Sesión

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-SYS-14`
**Nivel y Tipología:** Prueba de Sistema E2E / Operación en Doble Conducción y Relevos en Nodos.
**Requerimiento Trazado:** Ensayo adicional de ingeniería; no sustituye controles contractuales.
**Precondiciones:** Tractocamión en viaje Santiago-Antofagasta deteniéndose en terminal intermedio (La Serena) para cambio de conductor.
**Pasos de Ejecución:**
- Conductor saliente `DRV-1` inserta tarjeta RFID en lector de cabina e indica fin de turno. El sistema sella la `EvidenciaJornada` de `DRV-1` con odómetro final y hash SHA-256.
- Conductor entrante `DRV-2` presenta su tarjeta RFID en el lector de cabina.
- El gateway realiza validación bloqueante de aptitud y descanso previo de `DRV-2`.
- Tras validar aptitud, abre nueva sesión de conducción para `DRV-2` vinculada al mismo viaje.
- Camión reanuda marcha.

**Datos de Entrada Sintéticos:** Eventos de logout chofer 1 y login chofer 2 con lectores RFID.
**Resultado Esperado:** Segregación 100% nítida de las horas de conducción y descanso de ambos choferes; cero mezcla de jornadas; bitácora legal inalterable para la Dirección del Trabajo.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P1 (Bloqueante)**.
**Entorno:** Staging / Banco HIL + Gateway.

#### 9.0.5.15 CP-SYS-15 — Registro y Conciliación E2E de Carga de Combustible en Estación de Ruta

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-SYS-15`
**Nivel y Tipología:** Prueba de Sistema E2E / Control de Gastos en Ruta y Odometría.
**Requerimiento Trazado:** RF-016.
**Precondiciones:** Camión en ruta cargando diésel en estación de servicio Copec / Shell autorizada.
**Pasos de Ejecución:**
- Conductor carga 250 litros con tarjeta de flota de la empresa.
- Conductor ingresa en la PWA móvil el monto de litros cargados y toma foto del voucher de la bomba.
- La plataforma cruza automáticamente el registro de la PWA con: (a) Variación positiva del sensor de nivel de estanque telemático CAN J1939 (+248 litros medidos), (b) Posición GPS en la estación de servicio, (c) Odómetro actual.

**Datos de Entrada Sintéticos:** Voucher sintético por 250 litros, telemetría reporta salto de nivel de estanque de $32% a 84%$.
**Resultado Esperado:** Carga conciliada con éxito (diferencia de solo 2 litros dentro del margen de tolerancia metrológica del $\pm 1%$); imputación inmediata al costo consolidado del viaje.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P2 (Crítica)**.
**Entorno:** Staging AKS / Módulo de Combustible.

**Variante trazada a RF-016 (S3/T-12):** Entregar dos viajes cerrados con factura de combustible tardía en uno. Publicar costo preliminar en hasta 24 h con faltante explícito y recalcular una vez al recibirla, sin duplicación. Diferenciar estudio por ruta/contrato disponible en M6, EDT 2.5, de costeo por viaje en producción M16, EDT 5.6; exigir ambos entregables en sus hitos. En ensayo unitario se comprueba la regla con reloj controlado; latencia y comportamiento externo se acreditan en la prueba de integración, sistema o HIL asociada.

#### 9.0.5.16 CP-SYS-16 — Vista Única Consolidada de 374 Tractocamiones en Torre de Programación 24x7

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-SYS-16`
**Nivel y Tipología:** Prueba de Sistema E2E / Supervisión Operacional Centralizada.
**Requerimiento Trazado:** RF-008, RNF-009.
**Precondiciones:** Simulación de cobertura funcional de 374 tractocamiones: 182 iWave G26I (148 propios y 34 terceros adheridos) y 192 terceros con dispositivos existentes. Los datos de estos últimos solo se incorporan por mecanismos autorizados y comprobados; incluir accesos de consulta restringida y exportación no disponible, sin declarar telemetría completa garantizada.
**Pasos de Ejecución:**
- Abrir la interfaz web de la Torre de Programación en pantalla mural y consolas de operadores.
- Verificar la carga consolidada del mapa cartográfico nacional.
- Validar filtros operacionales: por zona geográfica (Norte, Centro, Sur), por tipo de carga (SUSPEL, Frío, Seco), y por pertenencia de flota (Propio vs Tercero).
- Comprobar refresco continuo de estados telemáticos vía WebSockets sin recargar la página.

**Datos de Entrada Sintéticos:** Flujo concurrente de telemetría de 374 unidades en tiempo real.
**Resultado Esperado:** 374 camiones desplegados sin latencia de renderizado (tasa de refresco visual $\ge 30\text{ FPS}$); 0 unidades duplicadas u omitidas; latencia de actualización $< 2\text{ segundos}$.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P1 (Bloqueante)**.
**Entorno:** Staging AKS / Torre de Programación San Bernardo.

**Variante trazada a RF-008 (S3/T-12):** Construir 374 unidades únicas, 148 propias y 226 externas, con muestras de todas las fuentes y marcas de tiempo conocidas. La vista contiene 374 identidades sin duplicación; cada posición muestra fuente y antigüedad y la jornada su nivel real. Si no existe posición, mostrar no disponible; no inventar coordenadas ni equiparar ubicación a descanso. En ensayo unitario se comprueba la regla con reloj controlado; latencia y comportamiento externo se acreditan en la prueba de integración, sistema o HIL asociada.

**Variante trazada a RNF-009 (S3/T-12):** Con la dotación cliente de nueve personas, ejecutar altas, consulta de salud y escalamiento con cuentas limitadas; comparar matriz de responsabilidad con manual. Toda especialidad no disponible en cliente debe estar asignada al servicio audIT 24x7 con responsable, turno y escalamiento de prueba. La capacitación de despachadores no acredita cobertura operativa del servicio ni su dotación. En ensayo unitario se comprueba la regla con reloj controlado; latencia y comportamiento externo se acreditan en la prueba de integración, sistema o HIL asociada.

#### 9.0.5.17 CP-SYS-17 — Generación Automatizada de Reporte Mensual de Huella de Carbono (ISO 14083)

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-SYS-17`
**Nivel y Tipología:** Prueba de Sistema E2E / Reportería Corporativa y Sostenibilidad Ambiental.
**Requerimiento Trazado:** RF-023.
**Precondiciones:** Cierre mensual con 8.000 viajes completados para los 84 clientes activos de Curimón S.A.
**Pasos de Ejecución:**
- Solicitar generación de balance de emisiones para el mayor cliente exportador de fruta.
- El motor de sostenibilidad agrega los kilómetros recorridos, toneladas transportadas y diésel real medido por bus CAN en todos los viajes de dicho cliente.
- Aplicar metodología ISO 14083 / GLEC Framework segregando emisiones directas (Scope 1) e indirectas (Scope 3).
- Generar reporte auditable en formato PDF y exportable a Excel/CSV.

**Datos de Entrada Sintéticos:** ID de cliente sintético `CLI-EXPORT-FRUIT-01`, período mensual septiembre 2026.
**Resultado Esperado:** Informe formal de sostenibilidad con desglose mensual de toneladas-kilómetro netas, emisiones totales de $\text{CO}_2\text{e}$ e índice de intensidad de carbono verificado.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P3 (Mayor)**.
**Entorno:** Staging AKS / Módulo de Sostenibilidad.

**Variante trazada a RF-023 (S3/T-12):** Calcular emisiones mensuales de una muestra propia y otra externa con factores versionados, actividad y toneladas-kilómetro de referencia. Reproducir sumas y unidades de la hoja independiente y desglosar cliente y contrato. Sin factor o actividad, declarar faltante y no emitir cero verificado. La conformidad externa del método se acredita separadamente. En ensayo unitario se comprueba la regla con reloj controlado; latencia y comportamiento externo se acreditan en la prueba de integración, sistema o HIL asociada.

#### 9.0.5.18 CP-SYS-18 — Excepción por indisponibilidad de fuente según RN-04

La excepción verifica indisponibilidad de fuente, sin levantar incumplimientos legales o de seguridad.
**ID:** `CP-SYS-18`
**Nivel y Tipología:** Sistema E2E, gobernanza y auditoría.
**Requerimiento Trazado:** RF-001, RF-028; RN-04.
**Precondiciones:** Viaje sintético, cuatro factores legales y de seguridad conformes, fuente de jornada temporalmente indisponible; cuentas separadas de jefe de turno de torre y prevención de riesgos.
**Pasos de Ejecución:** Solicitar excepción motivada para un solo viaje; intentar aprobar con una firma, con rol ajeno y con las dos firmas autorizadas. Repetir con descanso incumplido, habilitación vencida, equipo no apto y carga incompatible.
**Datos de Entrada Sintéticos:** Una orden, motivo, responsable y fecha fijos; variantes conformes e infractoras identificadas.
**Resultado Esperado:** Solo el viaje conforme con ambas firmas puede recibir excepción registrada; una firma o rol incorrecto no la concede. Todas las infracciones mantienen bloqueo incluso con dos firmas. Conservar razón, identidades, vigencia de un viaje y registro para revisión mensual; no atribuir evidencia instrumental a la excepción.
**Pass/Fail y Severidad:** Pass si todas las variantes producen esos estados y auditoría íntegra; cualquier discrepancia es Fail de severidad bloqueante.
**Entorno:** Staging identificado, reloj y configuración de RN-04 versionados.

#### 9.0.5.19 CP-SYS-19 — Portal de Clientes con Tracking Activo y Geofencing Temporal (Ley 21.719)

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-SYS-19`
**Nivel y Tipología:** Prueba de Sistema E2E / Portal Web Seguro y Privacidad por Diseño.
**Requerimiento Trazado:** RF-021, RF-022.
**Precondiciones:** Cliente institucional ingresa a su portal web corporativo (`clientes.curimon.audit.cl`).
**Pasos de Ejecución:**
- Cliente consulta el viaje asignado a su carga que se encuentra actualmente en tránsito.
- Verificar que visualice la posición del camión en el mapa con refresco sub-2 minutos.
- Simular la entrega de la carga y el cierre del e-POD.
- Intentar rastrear nuevamente la posición del camión 5 minutos después de completada la entrega.

**Datos de Entrada Sintéticos:** Sesión de cliente autenticada, orden de transporte activa $\rightarrow$ cerrada.
**Resultado Esperado:** Durante el viaje, el cliente observa la ubicación en tiempo real; una vez cerrada la entrega, el camión desaparece de su vista (geofencing temporal), salvaguardando la privacidad de ruta del transportista conforme a la Ley N.º 21.719.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P1 (Bloqueante)**.
**Entorno:** Staging AKS / Portal Web Clientes.

**Variante trazada a RF-021 (S3/T-12):** Con permiso por cliente, viaje y ventana, publicar posición cuya antigüedad se conoce. Durante ventana autorizada, refrescar en hasta dos minutos y mostrar antigüedad; antes o después, negar acceso. Cambiar el viaje a otro cliente y repetir con token viejo: no compartir ubicación ni rutas de competidores. En ensayo unitario se comprueba la regla con reloj controlado; latencia y comportamiento externo se acreditan en la prueba de integración, sistema o HIL asociada.

#### 9.0.5.20 CP-SYS-20 — Actualización Masiva de Firmware FOTA en Flota Propia con Rollback Automático

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-SYS-20`
**Nivel y Tipología:** Prueba de Sistema E2E / Mantenimiento Remoto de Firmware y Resiliencia FOTA.
**Requerimiento Trazado:** RNF-011.
**Precondiciones:** Campaña FOTA de actualización de firmware v2.1.0 configurada para 10 camiones propios detenidos en terminales durante su ventana de mantenimiento.
**Pasos de Ejecución:**
- Antes de transferir, instalar o activar, verificar ubicación, vehículo detenido, autorización y ventana. Repetir la solicitud con ubicación en ruta, velocidad positiva o permiso ausente: debe rechazarse sin escribir la partición ni reiniciar.
- Despachar imagen de firmware firmada criptográficamente hacia los 10 gateways telemáticos habilitados en terminal.
- Los dispositivos descargan la imagen en la partición inactiva (partición B) en segundo plano.
- En 9 camiones el reinicio y verificación de arranque (watchdog health check) es exitoso.
- En un equipo se utiliza una imagen de ensayo con firma y huella válidas, pero con fallo de arranque inducido en el fixture. Probar por separado una firma/huella inválida, que debe rechazarse antes de instalación; ese rechazo no equivale al ensayo de reversión de un arranque fallido.
- Evaluar el comportamiento del mecanismo de recuperación dual A/B.

**Datos de Entrada Sintéticos:** Paquete de firmware `.ota` de 45 MB firmado digitalmente.
**Resultado Esperado:** Los 9 camiones actualizan a v2.1.0 sin incidencias; el equipo con fallo revierte de forma autónoma a la partición A funcional, preservando registros, configuración e identidad. Las solicitudes fuera de terminal, en movimiento o sin permiso se rechazan sin instalación o reinicio. Se mide el tiempo completo desde activación hasta recuperación y conciliación; el perfil de watchdog es el de CP-HW-09 (60 s por intento). No se promete recuperación total en menos de 30 s cuando el watchdog por sí solo espera 60 s.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P1 (Bloqueante)**.
**Entorno:** Staging / Banco HIL + Gateways Físicos.

Los reportes del catálogo se incorporan al pipeline con los controles de T-13 Tabla 13.1: cero pruebas fallidas, líneas de lógica de negocio ≥70 % y ramas ≥80 % por separado; complejidad ≤15 por función y cero vulnerabilidades críticas o altas abiertas en el artefacto promovido. Las exclusiones requieren justificación y no pueden ocultar lógica de negocio. El catálogo diseñado no acredita que esos resultados se hayan obtenido.

### 9.0.6 Batería 4: Pruebas No Funcionales, Ciberseguridad y Estrés K6 (20 Casos: `CP-PERF-01` a `CP-PERF-12`, `CP-SEC-01` a `CP-SEC-08`)

Esta batería somete la infraestructura cloud, la capa de ingesta distribuida y los portales web a ensayos rigurosos de carga sostenida, estrés extremo con K6, conmutación ante desastres (DRP) y penetración de ciberseguridad con OWASP ZAP y Trivy.

#### 9.0.6.1 CP-PERF-01 — Carga Sostenida Peak Frutícola — Hipótesis de 450 Viajes/Día; 380 Sesiones Nominales y 570 de Estrés

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-PERF-01`
**Nivel y Tipología:** Prueba No Funcional / Rendimiento y Carga Sostenida con K6.
**Requerimiento Trazado:** RF-001, RF-013 y RT-09.06; los volúmenes exploratorios adicionales no sustituyen umbrales contractuales.
**Precondiciones:** Clúster AKS en Staging con configuración nominal de producción (3 nodos primarios D8s_v5).
**Pasos de Ejecución:**
- Ejecutar script K6 simulando la jornada de mayor demanda estacional frutícola (diciembre a abril).
- Generar carga sintética con hipótesis de 450 viajes/día distribuidos en 14 horas de alta actividad (\textasciitilde{}32 viajes/hora, con ráfagas de 60 viajes/hora).
- Ejecutar fases separadas de carga nominal (380) y estrés (570) durante cuatro horas por fase, preservando mezcla, tiempos de espera y operaciones. La tasa exploratoria de 1.200 peticiones/minuto se registra por separado y no reemplaza la concurrencia ni fuerza resultados artificialmente.
- Monitorear consumo de CPU, memoria de pods, y latencia de base de datos PostgreSQL.

**Datos de Entrada Sintéticos:** K6 Virtual Users (VUs): 380 sesiones nominales y 570 de estrés, con mezcla de despacho, mapas y tracking versionada; no se atribuyen estas magnitudes al Caso.
**Resultado Esperado:** Se debe verificar que sostiene ambas fases sin caídas, pérdida o doble procesamiento, cumpliendo los umbrales aplicables de S9 §9.3.6 a 1,5 veces el peak: asignación p95 ≤30 s y DET ≤90 s, medidos con sus relojes y oráculos de CP-PERF-04/05. Se conservan percentiles, errores y throughput por perfil; un promedio no compensa incumplimientos. Los tiempos, porcentajes y magnitudes observados se registrarán después del ensayo; no se anticipan mediciones ni actas suscritas.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P1 (Bloqueante)**.
**Entorno:** Staging AKS / K6 Distributed Runner.

**Perfil de concurrencia de diseño:** 380 sesiones nominales y 570 de estrés (1,5 × 380), conforme a S4 compartido, «Concurrencia y volumen declarados». Se adopta el extremo superior de los rangos de diseño: 80 usuarios internos, 150 conductores, 50 transportistas y 100 clientes; estrés: 120, 225, 75 y 150 respectivamente. Esos rangos son hipótesis de simultaneidad sobre las poblaciones del Caso, no mediciones. La concurrencia de usuarios no modifica la población de vehículos. Versionar la mezcla de usuarios y operaciones en el manifiesto. Es una hipótesis de ingeniería, no un dato del Caso ni una equivalencia con viajes diarios.

#### 9.0.6.2 CP-PERF-02 — Reconexión de 300 camiones — 1.786.200 registros y confirmación por unidad en hasta 20 min

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-PERF-02`
**Nivel y Tipología:** Prueba No Funcional / Capacidad de Ingesta en Ráfaga y Streaming Kafka.
**Requerimiento Trazado:** RF-009, RNF-002, RNF-008.
**Precondiciones:** Perfil principal de 300 camiones/72 h definido abajo, despliegue de ensayo identificado y reloj común. El perfil de 60 camiones/288 h se ejecuta separadamente como ampliación propuesta.
**Pasos de Ejecución:**
- Generar el manifiesto principal con 1.786.200 registros y los adjuntos definidos abajo.
- Recuperar simultáneamente cobertura en las 300 unidades e iniciar cronómetro individual.
- Sincronizar con reintentos, deduplicación y conciliación por origen/tipo; comparar conteos, huellas y adjuntos.
- Detener cada cronómetro solo tras confirmación completa; registrar máximo y distribución.
- Repetir por separado el perfil adicional 60/288, sin usarlo para aprobar el principal.

**Datos de Entrada Sintéticos:** Perfil y manifiesto definidos abajo; tamaño serializado medido antes de aplicar transporte o compresión.
**Resultado Esperado:** Cada camión confirma su lote en ≤20 min, sin pérdida ni corrupción. Una sola unidad fuera del límite o evidencia discordante implica Fail de severidad alta/crítica. Los resultados se medirán al ejecutar.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: Alta cuando afecta seguridad o evidencia; mayor en objetivos adicionales.
**Entorno:** Staging AKS / Apache Kafka Event Hubs.

**Variante contractual obligatoria:** Generar 72 h de registros por unidad con el perfil de muestreo y tamaño versionado de la memoria de cálculo; reconectar 300 camiones simultáneamente. Medir desde recuperación de cobertura hasta confirmación conciliada de cada camión: todas las unidades deben sincronizar en ≤20 min, sin pérdida de jornada ni esperas, con deduplicación y conflictos registrados. El ensayo sintético de 60 unidades/288 h se conserva como ampliación separada y no sustituye este control.

**Perfil serializado de ensayo:** 300 unidades simuladas, 72 h por unidad con 30 h de marcha; este escenario de reconexión no implica comprar 300 equipos audIT. Por unidad: 4.104 posiciones de 64 bytes, 1.800 muestras de motor de 160 bytes, 50 eventos/documentos con 227.000 bytes agregados y ocho fotos con 2.460.000 bytes agregados. Son 5.954 registros y 3.237.656 bytes por unidad; conservar manifiesto de tipos, conteos y huellas. El lote nominal contiene 1.786.200 registros y 971.296.800 bytes, sin overhead. Separar la ampliación de 60 unidades/288 h; no mezclar ambos perfiles. Para 20 min se requiere al menos 6,48 Mbit/s útiles agregados; margen de transporte y almacenamiento se dimensiona explícitamente. Medir cada camión hasta confirmación completa, incluyendo datos y evidencia documental, y fallar si alguno supera veinte minutos o pierde jornada/esperas.

**Variante de cierre fronterizo:** Simular doce días de cierre de ruta con períodos separados de conexión y sombra. Debe preservarse jornada real, custodia y reprogramación sin inventar descanso, congelar cobros ni desplazar fases contractuales; el cierre no activa automáticamente doce días de desconexión.

**Presupuesto de transporte propuesto:** El mismo perfil descompone 45 eventos de 600 bytes (27.000 bytes) y cinco documentos de 40.000 bytes (200.000 bytes). Los 300 camiones requieren como mínimo 6,475312 Mbit/s útiles para el total con fotos en 1.200 segundos; el presupuesto con 25 % de transporte y 20 % de reserva temporal es 10,117675 Mbit/s (se dimensiona al menos 10,12 Mbit/s). Los paquetes de 4 KiB elegidos para registros ascienden a 238 por camión con el presupuesto de transporte: 71.400 admitidos a 100 operaciones/s requieren al menos 714 s (11,9 min). Esa admisión no demuestra transferencia de fotos ni persistencia; el cronómetro termina solo con conciliación completa por unidad. Conservar configuración de cuotas y medir otros cuellos de botella.

**Variante trazada a RF-009 (S3/T-12):** Desconectar 72 h con el perfil versionado de CP-PERF-02, reiniciar equipo y reconectar. Conciliar identificadores, orden y huellas de registros y documentos, sin pérdidas ni duplicados. El reloj de sincronización por camión va de recuperación de cobertura a confirmación completa y debe ser como máximo 20 min. En ensayo unitario se comprueba la regla con reloj controlado; latencia y comportamiento externo se acreditan en la prueba de integración, sistema o HIL asociada.

**Variante trazada a RNF-008 (S3/T-12):** Ensayar 288 h separadamente como compromiso propuesto para cierres fronterizos: cuatro repeticiones del perfil de 72 h, 23.816 registros y 12.950.624 bytes brutos por unidad antes de overhead. Conciliar registros y documentos tras reconexión; cualquier pérdida falla ese compromiso. No atribuir a las bases 288 h de desconexión ni sustituir la aprobación de 72 h por esta ampliación. En ensayo unitario se comprueba la regla con reloj controlado; latencia y comportamiento externo se acreditan en la prueba de integración, sistema o HIL asociada.

#### 9.0.6.3 CP-PERF-03 — Conmutación por Desastre (Failover DRP) a Azure Brazil South (RTO $\le 4\text{ h}, RPO \le 15\text{ min}$)

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-PERF-03`
**Nivel y Tipología:** Prueba No Funcional / Continuidad Operacional y Resiliencia ante Desastres.
**Requerimiento Trazado:** Ensayo adicional de ingeniería; no sustituye controles contractuales.
**Precondiciones:** Plataforma primaria en Azure Chile Central operando con carga activa. Sitio secundario Hot-Standby en Azure Brazil South sincronizado mediante replicación continua.
**Pasos de Ejecución:**
- Simular caída catastrófica no recuperable de la región Azure Chile Central (corte de red e inhabilitación de clúster primario).
- El responsable de continuidad designado por el Comité de Operación declara el desastre y activa el runbook automatizado de conmutación DRP (`drp-failover.sh`).
- Promover la base de datos réplica de PostgreSQL y TimescaleDB en Brazil South a nodo primario de lectura/escritura.
- Escalar los microservicios en el clúster AKS de Brazil South de 2 a 8 pods por servicio.
- Redirigir el tráfico global en Azure Front Door hacia la IP pública de Brazil South.
- Medir el tiempo total de recuperación (RTO medido) y verificar el desfase de transacciones perdidas (RPO medido).

**Datos de Entrada Sintéticos:** Carga continua previa de 100 viajes/hora; script de failover automatizado con Terraform.
**Resultado Esperado:** Se debe verificar que RTO $\le 4\text{ h} y RPO \le 15\text{ min}$. Los tiempos, porcentajes y magnitudes observados se registrarán después del ensayo; no se anticipan mediciones ni actas suscritas.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P1 (Bloqueante)**.
**Entorno:** Azure Chile Central $\rightarrow$ Azure Brazil South.

#### 9.0.6.4 CP-PERF-04 — Latencia de Validación Bloqueante Pre-Despacho ($P_{95} \le 30{,}0\text{ s}, P_{50} \le 8{,}0\text{ s}$)

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-PERF-04`
**Nivel y Tipología:** Prueba No Funcional / Desempeño y Latencia Sub-30s bajo Carga.
**Requerimiento Trazado:** RF-001.
**Precondiciones:** Perfil común de CP-PERF-01, con 380 sesiones nominales y 570 en estrés. Los usuarios internos de cada fase ejecutan la mezcla versionada de operaciones, incluida asignación; no se confunden sesiones, solicitudes y candidatos de viaje.
**Pasos de Ejecución:**
- Ejecutar validaciones de cuatro factores en las dos fases del perfil común y conservar su mezcla con las demás operaciones. El lote de 500 candidatos alimenta las solicitudes; no equivale a 500 sesiones concurrentes. Una ráfaga exploratoria adicional de 500 solicitudes se mide por separado y no reemplaza el ensayo a 1,5 veces el peak.
- Registrar la distribución percentílica de tiempos de respuesta (P_{50}, P_{90}, P_{95}, P_{99}).

**Datos de Entrada Sintéticos:** Lote de 500 candidatos de viaje con datos de choferes, camiones y ramplas.
**Resultado Esperado:** Se debe verificar que $P_{95} \le 30{,}0\text{ s}$. Los tiempos, porcentajes y magnitudes observados se registrarán después del ensayo; no se anticipan mediciones ni actas suscritas.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P1 (Bloqueante)**.
**Entorno:** Staging AKS / K6.

#### 9.0.6.5 CP-PERF-05 — Emisión de Documento D.E.T. en Cabina bajo Demanda Concurrente ($P_{99} \le 90{,}0\text{ s}$)

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-PERF-05`
**Nivel y Tipología:** Prueba No Funcional / Latencia de Generación Tributaria en Terminal.
**Requerimiento Trazado:** RF-013 (emisión) y RF-014 (disponibilidad antes del movimiento).
**Precondiciones:** Perfil común de CP-PERF-01 con 380 sesiones nominales y 570 en estrés, y fixture de salida matinal de 30 camiones en diez minutos en San Bernardo; esta cantidad es una entrada de ensayo, no una dotación inferida del Caso.
**Pasos de Ejecución:**
- Disparar las 30 solicitudes de DET hacia el sistema contable, único emisor, conservando la carga de fondo y las fases nominal/estrés de CP-PERF-01. El equipo a bordo recibe y conserva el documento; no se transforma en emisor tributario.
- Cronometrar el tiempo desde la confirmación de la orden hasta la disponibilidad del documento firmado con QR en cabina.

**Datos de Entrada Sintéticos:** 30 solicitudes D.E.T. con tokens de contingencia.
**Resultado Esperado:** Se debe verificar que $P_{99} \le 90\text{ s}$. Los tiempos, porcentajes y magnitudes observados se registrarán después del ensayo; no se anticipan mediciones ni actas suscritas.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P1 (Bloqueante)**.
**Entorno:** Staging / Banco HIL Multidispositivo.

#### 9.0.6.6 CP-PERF-06 — Transmisión y Recepción Prioritaria de Alarma SOS en Torre 24x7 ($P_{99} \le 15{,}0\text{ s}$)

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-PERF-06`
**Nivel y Tipología:** Prueba No Funcional / Latencia de Alerta Crítica de Pánico en Ruta.
**Requerimiento Trazado:** Ensayo adicional de ingeniería; no sustituye controles contractuales.
**Precondiciones:** Canal de red móvil degradado con ancho de banda restringido (simulación 2G/GPRS en ruta desértica).
**Pasos de Ejecución:**
- Pulsar botón físico de pánico / SOS en el gateway de cabina.
- El firmware interrumpe cualquier transmisión ordinaria y prioriza el paquete de emergencia (`EMERGENCY_PACKET_PRIORITY_0`).
- El paquete viaja por protocolo UDP/MQTT con QoS 1 hacia Azure IoT Hub / Event Hubs.
- Medir tiempo transcurrido hasta el disparo de la alarma visual y sonora en la pantalla del operador de Torre 24x7.

**Datos de Entrada Sintéticos:** Evento SOS físico disparado en gateway con coordenadas en km 740 Ruta 5 Norte.
**Resultado Esperado:** Se debe verificar que la alerta llega en $\le 15\text{ segundos}$. Los tiempos, porcentajes y magnitudes observados se registrarán después del ensayo; no se anticipan mediciones ni actas suscritas.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P1 (Bloqueante)**.
**Entorno:** Banco HIL / Red Celular Simulada con Emulador de Canal RF.

#### 9.0.6.7 CP-PERF-07 — Latencia de Refresco de Posición en Portal Clientes con 500 Usuarios Concurrentes

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-PERF-07`
**Nivel y Tipología:** Prueba No Funcional / Concurrencia de Consultas y Latencia de Tracking.
**Requerimiento Trazado:** RF-021.
**Precondiciones:** 500 clientes corporativos autenticados simultáneamente consultando el mapa de seguimiento de sus respectivas cargas activas.
**Pasos de Ejecución:**
- K6 simula 500 conexiones concurrentes vía WebSocket/HTTP long-polling solicitando posición telemática.
- Actualizar las coordenadas de los 374 tractocamiones en TimescaleDB cada 30 segundos.
- Medir el tiempo de propagación desde la base de datos hasta el navegador del usuario final.

**Datos de Entrada Sintéticos:** 500 sesiones virtuales con peticiones cada 15 segundos.
**Resultado Esperado:** Se debe verificar que el refresco se mantiene $\le 2\text{ minutos}$ para el 100% de los usuarios. Los tiempos, porcentajes y magnitudes observados se registrarán después del ensayo; no se anticipan mediciones ni actas suscritas.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P2 (Crítica)**.
**Entorno:** Staging AKS / K6 WebSocket Runner.

**Perfil de clientes:** 100 sesiones nominales de cliente y 150 en estrés, derivadas del rango de S4. Mantener antigüedad de posición publicada ≤2 min con cobertura. Un perfil exploratorio de 500 se conserva solo como sobrecarga adicional, sin atribuirlo a las bases.

**Variante trazada a RF-021 (S3/T-12):** Con permiso por cliente, viaje y ventana, publicar posición cuya antigüedad se conoce. Durante ventana autorizada, refrescar en hasta dos minutos y mostrar antigüedad; antes o después, negar acceso. Cambiar el viaje a otro cliente y repetir con token viejo: no compartir ubicación ni rutas de competidores. En ensayo unitario se comprueba la regla con reloj controlado; latencia y comportamiento externo se acreditan en la prueba de integración, sistema o HIL asociada.

#### 9.0.6.8 CP-PERF-08 — Escalamiento Horizontal Automático de Pods (HPA) en AKS ante Picos Repentinos

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-PERF-08`
**Nivel y Tipología:** Prueba No Funcional / Elasticidad Cloud y Autoescalado Horizontal.
**Requerimiento Trazado:** RNF-010.
**Precondiciones:** Microservicio de Asignación desplegado con Horizontal Pod Autoscaler (HPA) configurado: mínimo 2 pods, máximo 12 pods, umbral de CPU para escala = $70%$.
**Pasos de Ejecución:**
- Iniciar con carga base (2 pods consumiendo $25%$ de CPU).
- Inyectar ráfaga repentina de 1.000 peticiones/segundo durante 5 minutos.
- Monitorear métricas de Kubernetes Metrics Server y eventos de escalamiento del HPA.
- Reducir la carga a cero y observar el proceso de consolidación y scale-down.

**Datos de Entrada Sintéticos:** Ráfaga masiva K6 de 1.000 req/s.
**Resultado Esperado:** Se debe verificar que escala automáticamente en $< 90\text{ s}$ manteniendo disponibilidad. Los tiempos, porcentajes y magnitudes observados se registrarán después del ensayo; no se anticipan mediciones ni actas suscritas.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P2 (Crítica)**.
**Entorno:** Staging AKS.

**Variante trazada a RNF-010 (S3/T-12):** Conciliar inventario técnico y modelo económico de 36 meses: cantidades, unidades, periodicidad y cobertura de nube, enlaces, licencias, soporte, reposición, retiro y contingencia. Esperar cero partidas omitidas o duplicadas y horizonte íntegro; precios solo en oferta económica. El escalamiento de pods no demuestra exhaustividad del costo de operación. En ensayo unitario se comprueba la regla con reloj controlado; latencia y comportamiento externo se acreditan en la prueba de integración, sistema o HIL asociada.

#### 9.0.6.9 CP-PERF-09 — Capacidad de Inserción Continua en TimescaleDB ($\ge 10.000\text{ métricas/segundo}$)

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-PERF-09`
**Nivel y Tipología:** Prueba No Funcional / Rendimiento de Base de Datos de Series de Tiempo.
**Requerimiento Trazado:** RF-018.
**Precondiciones:** Instancia TimescaleDB en Azure PostgreSQL Flexible Server con disco SSD Premium v2.
**Pasos de Ejecución:**
- Ejecutar herramienta de benchmarking `tsbs` (Time Series Benchmark Suite).
- Inyectar flujo continuo de 10.000 métricas por segundo (odómetro, RPM, velocidad, presiones, temperaturas) durante 60 minutos.
- Medir la tasa sostenida de inserción y el ratio de compresión en disco tras la política de compresión columnar.

**Datos de Entrada Sintéticos:** 36.000.000 de registros sintéticos de sensores vehiculares.
**Resultado Esperado:** Se debe verificar que sostiene $\ge 10.000\text{ métricas/s}$ sin degradación. Los tiempos, porcentajes y magnitudes observados se registrarán después del ensayo; no se anticipan mediciones ni actas suscritas.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P2 (Crítica)**.
**Entorno:** Staging Azure PostgreSQL TimescaleDB.

**Variante trazada a RF-018 (S3/T-12):** Construir 12 meses de consumo y kilómetros por vehículo, ruta y conductor con condiciones registradas. En una cohorte de referencia, razones 2, 4, 4, 4, 5, 5, 7 y 9 tienen media 5 y varianza poblacional 4, en unidades sintéticas. Añadir una condición de carga sintética x con valores 0, 2, 2, 2, 3, 3, 5 y 7 y consumo y=2+x: el modelo lineal de referencia debe reproducir coeficientes 2 y 1 y residual cero en ese fixture. Un modelo alternativo debe declarar su oráculo independiente. Esta exactitud sintética no se promete para datos reales. El modelo debe conservar cohorte, período, condiciones, versión y dispersión reproducible; registros incompletos no se mezclan como cero. El benchmark de inserción no demuestra explicación de dispersión. En ensayo unitario se comprueba la regla con reloj controlado; latencia y comportamiento externo se acreditan en la prueba de integración, sistema o HIL asociada.

#### 9.0.6.10 CP-PERF-10 — Concurrencia Extrema en Cierre Mensual — 148 Transportistas en Portal Web

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-PERF-10`
**Nivel y Tipología:** Prueba No Funcional / Concurrencia de Usuarios y Transacciones Financieras.
**Requerimiento Trazado:** RF-020.
**Precondiciones:** 148 cuentas de transportistas subcontratados activas el día de cierre mensual.
**Pasos de Ejecución:**
- Simular inicio de sesión concurrente de los 148 transportistas en un intervalo de 3 minutos.
- Cada usuario consulta su pre-liquidación, descarga el archivo PDF de detalle de viajes y envía el acuse de conformidad de cobro.
- Medir tiempo de respuesta y concurrencia sobre la base de datos transaccional.

**Datos de Entrada Sintéticos:** 148 usuarios virtuales K6 autenticados con tokens independientes.
**Resultado Esperado:** Se debe verificar que atiende a los 148 transportistas en paralelo con latencia $< 3\text{ s}$. Los tiempos, porcentajes y magnitudes observados se registrarán después del ensayo; no se anticipan mediciones ni actas suscritas.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P2 (Crítica)**.
**Entorno:** Staging AKS / Portal Web.

**Variante trazada a RF-020 (S3/T-12):** Autenticar dos propietarios y solicitar viajes y liquidaciones propios y ajenos durante el cierre de 148 titulares. Mostrar detalle propio actualizado y negar toda consulta ajena; registrar autor y fecha. Conservar el ensayo de latencia adicional de 3 s como parámetro propuesto; no confundirlo con el plazo mensual de liquidación. En ensayo unitario se comprueba la regla con reloj controlado; latencia y comportamiento externo se acreditan en la prueba de integración, sistema o HIL asociada.

#### 9.0.6.11 CP-PERF-11 — Resiliencia ante Red Móvil Degradada (Latencia 150 ms, Jitter 50 ms, Pérdida 2%)

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-PERF-11`
**Nivel y Tipología:** Prueba No Funcional / Tolerancia a Inestabilidad de Telecomunicaciones.
**Requerimiento Trazado:** Ensayo adicional de ingeniería; no sustituye controles contractuales.
**Precondiciones:** Emulador de red WAN (NetEm / Toxiproxy) intercalado entre el gateway de cabina y el backend cloud, inyectando $150\text{ ms} de latencia base, 50\text{ ms} de jitter y 2%$ de pérdida de paquetes aleatoria.
**Pasos de Ejecución:**
- Operar el camión emulando transmisión telemática durante 2 horas continuas bajo enlace degradado.
- Evaluar el comportamiento del protocolo MQTT con QoS 1 y el mecanismo de sincronización local SQLite WAL.

**Datos de Entrada Sintéticos:** Flujo telemático de 2 horas en condiciones adversas de conectividad.
**Resultado Esperado:** Se debe verificar que concilia el conjunto del ensayo sin pérdida ni duplicados. Los tiempos, porcentajes y magnitudes observados se registrarán después del ensayo; no se anticipan mediciones ni actas suscritas.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P2 (Crítica)**.
**Entorno:** Banco HIL / Simulador de Red NetEm.

#### 9.0.6.12 CP-PERF-12 — Prueba de Longevidad (Soak Testing) — 72 Horas Continuas a Carga Nominal

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-PERF-12`
**Nivel y Tipología:** Prueba No Funcional / Estabilidad Temporal y Detección de Memory Leaks.
**Requerimiento Trazado:** Ensayo adicional de ingeniería; no sustituye controles contractuales.
**Precondiciones:** Entorno de Staging aislado ejecutando tráfico sintetizado a tasa constante (100 peticiones/s).
**Pasos de Ejecución:**
- Ejecutar prueba de carga ininterrumpida durante 72 horas consecutivas.
- Monitorear de forma continua el consumo de memoria heap en JVM/Go y descriptores de archivo en microservicios, brokers Kafka y nodos de base de datos.
- Comprobar que no existan tendencias lineales crecientes de memoria (memory leaks) ni saturación de conexiones en el pool de PostgreSQL (connection leaks).

**Datos de Entrada Sintéticos:** Tráfico sintético sostenido de 72 horas continuas.
**Resultado Esperado:** Se debe verificar que no hay fugas de recursos ni degradación acumulativa. Los tiempos, porcentajes y magnitudes observados se registrarán después del ensayo; no se anticipan mediciones ni actas suscritas.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P1 (Bloqueante)**.
**Entorno:** Staging AKS / Datadog Monitoring.

**Variante contractual de terminales:** Mantener cada tipo de terminal 24 h sin enlace exterior, con cómputo y red del ambiente de ensayo especificados; registrar transacciones locales bajo perfil versionado. Restaurar el enlace, reconciliar automáticamente y verificar conteos, huellas y conflictos deterministas. Fallar si se requiere acceso cloud para las funciones degradadas comprometidas o se pierden transacciones. No se presupone hardware del cliente.

#### 9.0.6.13 CP-SEC-01 — DAST OWASP ZAP — Prevención de Inyecciones SQL (SQLi) en APIs

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-SEC-01`
**Nivel y Tipología:** Prueba de Ciberseguridad / Análisis Dinámico de Seguridad (DAST).
**Requerimiento Trazado:** Ensayo adicional de ingeniería; no sustituye controles contractuales.
**Precondiciones:** Escáner OWASP ZAP Enterprise integrado en el pipeline de GitLab CI apuntando al endpoint `/api/v1/dispatch/orders`.
**Pasos de Ejecución:**
- Ejecutar ataque activo inyectando vectores de ataque SQLi en todos los parámetros de entrada (`' OR '1'='1`, `UNION SELECT`, inyecciones ciegas basadas en tiempo `SLEEP(5)`).
- Analizar las respuestas del servidor y logs de base de datos.

**Datos de Entrada Sintéticos:** Diccionario de 2.500 cargas útiles (payloads) de inyección SQL estándar OWASP.
**Resultado Esperado:** 0 vulnerabilidades detectadas; el 100% de las peticiones maliciosas son neutralizadas mediante consultas parametrizadas (Prepared Statements) en los ORMs y bloqueadas por el WAF con HTTP 400 o 403; cero exposición de esquemas de BD.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P1 (Bloqueante)**.
**Entorno:** CI Pipeline / OWASP ZAP Container.

#### 9.0.6.14 CP-SEC-02 — DAST OWASP ZAP — Prevención de Cross-Site Scripting (XSS) y CSRF en Portales

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-SEC-02`
**Nivel y Tipología:** Prueba de Ciberseguridad / Seguridad en Aplicaciones Web.
**Requerimiento Trazado:** Ensayo adicional de ingeniería; no sustituye controles contractuales.
**Precondiciones:** Portales Web de Clientes y Transportistas en Staging.
**Pasos de Ejecución:**
- Inyectar payloads de XSS reflejado y almacenado en campos de texto libre (observaciones de viaje, nombres de cliente, datos de chofer).
- Simular ataque CSRF intentando ejecutar una asignación forzada de viaje desde un origen no confiable.

**Datos de Entrada Sintéticos:** Payloads `<script>alert('XSS')</script>`, payloads basados en SVG, y formularios con dominios cruzados sin token CSRF.
**Resultado Esperado:** Cero alertas XSS; sanitización automática de entradas en frontend y backend; cabeceras `SameSite=Strict` en cookies y tokens anti-CSRF validan y bloquean peticiones no autorizadas.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P1 (Bloqueante)**.
**Entorno:** CI Pipeline / OWASP ZAP.

#### 9.0.6.15 CP-SEC-03 — Hardening de Cabeceras HTTP y Cifrado en Tránsito TLS 1.3 Estricto

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-SEC-03`
**Nivel y Tipología:** Prueba de Ciberseguridad / Configuración Segura de Servidores y Criptografía.
**Requerimiento Trazado:** Ensayo adicional de ingeniería; no sustituye controles contractuales.
**Precondiciones:** Azure Front Door y WAF configurados para dominios públicos `*.curimon.audit.cl`.
**Pasos de Ejecución:**
- Ejecutar escáner SSL Labs / `testssl.sh` sobre todos los endpoints expuestos.
- Verificar que se rechacen conexiones SSL v2, SSL v3, TLS 1.0 y TLS 1.1, permitiendo exclusivamente TLS 1.2 y TLS 1.3 con ciphers seguros (ECDHE-RSA-AES128-GCM-SHA256 o superior).
- Verificar presencia de cabeceras de seguridad: `Strict-Transport-Security: max-age=31536000; includeSubDomains; preload`, `Content-Security-Policy`, `X-Content-Type-Options: nosniff`, `X-Frame-Options: DENY`.

**Datos de Entrada Sintéticos:** Sondas de escaneo SSL y peticiones cURL a cabeceras HTTP.
**Resultado Esperado:** Calificación SSL Labs Grade A+; 100% de las cabeceras de seguridad requeridas presentes; rechazo inmediato de ciphers obsoletos.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P1 (Bloqueante)**.
**Entorno:** Staging Azure Front Door / SSL Labs Scanner.

#### 9.0.6.16 CP-SEC-04 — Cifrado a Nivel de Campo (FLE AES-256-GCM) para Datos de Choferes (Ley 21.719)

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-SEC-04`
**Nivel y Tipología:** Prueba de Ciberseguridad / Protección de Datos Personales y Privacidad.
**Requerimiento Trazado:** RF-022, RNF-013.
**Precondiciones:** Base de datos PostgreSQL con esquema de cifrado a nivel de campo configurado.
**Pasos de Ejecución:**
- Insertar registro de chofer sintético conteniendo RUT, teléfono personal y certificado médico de aptitud.
- Realizar un volcado directo de la base de datos (pg_dump) o consultar directamente la tabla mediante cliente SQL sin pasar por el microservicio autorizado.
- Verificar que los campos sensibles se encuentren almacenados como texto cifrado binario ininteligible (AES-256-GCM con vector de inicialización único).

**Datos de Entrada Sintéticos:** Chofer sintético `RUT: 14.887.654-3`, `Teléfono: +56987654321`.
**Resultado Esperado:** Los datos aparecen como cadenas cifradas en disco (`\$fle\$v1\$gAAAAABk...`); el texto en claro solo es accesible mediante invocación autorizada con la clave custodiada en Azure Key Vault.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P1 (Bloqueante)**.
**Entorno:** CI Testcontainers / PostgreSQL + Azure Key Vault Mock.

**Variante trazada a RF-022 (S3/T-12):** Crear permisos por propietario, dato, vehículo, destinatario y vigencia; conceder y revocar uno a hora fija. En hasta cinco minutos deben cesar accesos comprendidos, incluso con token o caché previa; conservar auditoría. Un conductor o propietario ajeno no puede revocar. No eliminar evidencia que tiene obligación de conservación. En ensayo unitario se comprueba la regla con reloj controlado; latencia y comportamiento externo se acreditan en la prueba de integración, sistema o HIL asociada.

**Variante trazada a RNF-013 (S3/T-12):** Inventariar atributos que requieren protección y roles autorizados; leerlos desde disco y mediante API con rol permitido y ajeno. Todos los atributos protegidos están cifrados en persistencia y filtrados por rol/atributo; cero valores claros o accesos ajenos. Conservar claves y configuración del fixture; el ejemplo de ciphertext no acredita algoritmo real. En ensayo unitario se comprueba la regla con reloj controlado; latencia y comportamiento externo se acreditan en la prueba de integración, sistema o HIL asociada.

#### 9.0.6.17 CP-SEC-05 — Revocación Inmediata de Consentimiento de Geolocalización ($\le 5\text{ min}$)

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-SEC-05`
**Nivel y Tipología:** Prueba de Ciberseguridad / Derechos ARCO y Soberanía del Titular de Datos.
**Requerimiento Trazado:** RF-022, RNF-003, RNF-013.
**Precondiciones:** Conductor subcontratado con consentimiento previo otorgado para uso de PWA.
**Pasos de Ejecución:**
- Conductor presiona en la PWA el botón "Revocar Consentimiento de Ubicación".
- La PWA envía la petición al backend; el módulo de privacidad invalida la autorización en Redis y PostgreSQL.
- Cronometrar el tiempo en que la Torre de Control y los servicios de ingesta dejan de capturar y mostrar las coordenadas personales del conductor fuera de viaje.

**Datos de Entrada Sintéticos:** Evento de revocación formal de consentimiento de chofer `DRV-SYNTH-204`.
**Resultado Esperado:** La revocación se propaga a todo el sistema en 12 segundos ($\ll 5\text{ minutos}$); el canal telemático del chofer se disocia inmediatamente; se genera comprobante legal de revocación.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P1 (Bloqueante)**.
**Entorno:** Staging AKS / Módulo de Privacidad.

**Titularidad y revocación:** El solicitante con derecho de revocar es el propietario/titular autorizado del camión, no cualquier conductor. Preparar permisos por dato, camión, viaje, destinatario y fecha. Al revocar, cesan los accesos comprendidos por ese permiso; no se borran datos con obligación de conservación ni se deshabilita una función cuya fuente legítima y permiso sigan vigentes. Intentar revocación por usuario ajeno debe producir denegación y auditoría.

**Variante trazada a RF-022 (S3/T-12):** Crear permisos por propietario, dato, vehículo, destinatario y vigencia; conceder y revocar uno a hora fija. En hasta cinco minutos deben cesar accesos comprendidos, incluso con token o caché previa; conservar auditoría. Un conductor o propietario ajeno no puede revocar. No eliminar evidencia que tiene obligación de conservación. En ensayo unitario se comprueba la regla con reloj controlado; latencia y comportamiento externo se acreditan en la prueba de integración, sistema o HIL asociada.

**Variante trazada a RNF-013 (S3/T-12):** Inventariar atributos que requieren protección y roles autorizados; leerlos desde disco y mediante API con rol permitido y ajeno. Todos los atributos protegidos están cifrados en persistencia y filtrados por rol/atributo; cero valores claros o accesos ajenos. Conservar claves y configuración del fixture; el ejemplo de ciphertext no acredita algoritmo real. En ensayo unitario se comprueba la regla con reloj controlado; latencia y comportamiento externo se acreditan en la prueba de integración, sistema o HIL asociada.

#### 9.0.6.18 CP-SEC-06 — Autenticación Mutua TLS (mTLS) entre Microservicios y Rotación de Certificados

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-SEC-06`
**Nivel y Tipología:** Prueba de Ciberseguridad / Arquitectura Zero Trust y Red de Servicios.
**Requerimiento Trazado:** Ensayo adicional de ingeniería; no sustituye controles contractuales.
**Precondiciones:** Service Mesh Istio desplegado en clúster AKS con política `PeerAuthentication` en modo `STRICT`.
**Pasos de Ejecución:**
- Intentar comunicación HTTP directa en texto plano entre el pod de Portal y el pod de Asignación.
- Verificar que Istio aborte la conexión con error de protocolo.
- Establecer conexión con certificado emitido por Istio Citadel y verificar cifrado mTLS.
- Simular rotación periódica del certificado interno de pod.

**Datos de Entrada Sintéticos:** Peticiones curl internas en clúster Kubernetes.
**Resultado Esperado:** Rechazo del 100% de conexiones no autenticadas con certificado de malla; rotación automática de certificados sin desconexión de servicios.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P1 (Bloqueante)**.
**Entorno:** Staging AKS con Istio Service Mesh.

#### 9.0.6.19 CP-SEC-07 — Prevención de Broken Object Level Authorization (BOLA/IDOR) en Portales

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-SEC-07`
**Nivel y Tipología:** Prueba de Ciberseguridad / Control de Acceso y Aislamiento Multi-Tenant.
**Requerimiento Trazado:** RF-020, RF-021, RNF-013.
**Precondiciones:** Usuario transportista `USER-CARRIER-A` con sesión activa. Existencia de liquidación perteneciente al transportista `USER-CARRIER-B` con ID `LIQ-99882`.
**Pasos de Ejecución:**
- `USER-CARRIER-A` realiza una petición HTTP directa: `GET /api/v1/carrier-portal/settlements/LIQ-99882`.
- Verificar la respuesta del middleware de autorización a nivel de objeto.

**Datos de Entrada Sintéticos:** Petición manipulada con token de sesión de transportista A consultando ID del transportista B.
**Resultado Esperado:** Código HTTP `403 Forbidden` o `404 Not Found`; denegación absoluta de acceso al documento ajeno; registro de alerta de seguridad en la consola SIEM por intento de vulneración BOLA/IDOR.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P1 (Bloqueante)**.
**Entorno:** CI Testcontainers / API Gateway.

**Variante trazada a RF-020 (S3/T-12):** Autenticar dos propietarios y solicitar viajes y liquidaciones propios y ajenos durante el cierre de 148 titulares. Mostrar detalle propio actualizado y negar toda consulta ajena; registrar autor y fecha. Conservar el ensayo de latencia adicional de 3 s como parámetro propuesto; no confundirlo con el plazo mensual de liquidación. En ensayo unitario se comprueba la regla con reloj controlado; latencia y comportamiento externo se acreditan en la prueba de integración, sistema o HIL asociada.

#### 9.0.6.20 CP-SEC-08 — Integridad WORM y Sellado Temporal RFC 3161 en Registro de `EvidenciaJornada`

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-SEC-08`
**Nivel y Tipología:** Prueba de Ciberseguridad / Cadena de Custodia e Inmutabilidad Legal.
**Requerimiento Trazado:** RF-004, RNF-012, RNF-014.
**Precondiciones:** Contenedor Azure Blob Storage configurado con política de inmutabilidad en nivel WORM (Write Once, Read Many) con bloqueo temporal de 5 años.
**Pasos de Ejecución:**
- Almacenar un lote de eventos de jornada laboral sellados con timestamp RFC 3161 en el blob inmutable.
- Intentar ejecutar una operación de modificación (overwrite) sobre el blob mediante credenciales de administrador de base de datos.
- Intentar ejecutar una operación de borrado (delete) sobre el blob.

**Datos de Entrada Sintéticos:** Bloque de auditoría de jornada laboral con sellado criptográfico.
**Resultado Esperado:** Azure Storage rechaza ambas operaciones con error `StorageOperationForbiddenByImmutabilityPolicy`; la evidencia permanece inalterada y lista para peritaje judicial o inspección de la Dirección del Trabajo.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P1 (Bloqueante)**.
**Entorno:** Staging Azure Blob Storage Inmutable.

**Variante trazada a RF-004 (S3/T-12):** Sellar un evento original y una corrección que cambia un dato; conservar ambas versiones con autor, origen y fecha. Alterar el original y verificar fallo de integridad. Avanzar reloj virtual hasta cinco años de conservación y comprobar disponibilidad e integridad antes de su término; la simulación verifica la política y no acredita cinco años de operación real. En ensayo unitario se comprueba la regla con reloj controlado; latencia y comportamiento externo se acreditan en la prueba de integración, sistema o HIL asociada.

**Variante trazada a RNF-012 (S3/T-12):** Crear evidencia con autor, origen, fecha y contenido; añadir corrección como registro nuevo. Esperar histórico íntegro y vínculo entre versiones. Quitar autor u origen y alterar fecha: rechazar ingreso probatorio o dejar pendiente identificado, nunca completar datos inventados ni sobrescribir original. En ensayo unitario se comprueba la regla con reloj controlado; latencia y comportamiento externo se acreditan en la prueba de integración, sistema o HIL asociada.

**Variante trazada a RNF-014 (S3/T-12):** Versionar dominios y plazos: jornada cinco años, documentos/viajes/liquidación seis, siniestros diez, habilitación vigencia más cinco, SUSPEL cinco, esperas tres, series dos en línea con agregación. Con reloj virtual antes/al cumplir cada umbral, retener mientras exista obligación o suspensión y aplicar después la política aprobada. Revocar permiso detiene captura/acceso comprendidos, sin borrado anticipado; cotejar réplica y original. En ensayo unitario se comprueba la regla con reloj controlado; latencia y comportamiento externo se acreditan en la prueba de integración, sistema o HIL asociada.

### 9.0.7 Batería 5: Pruebas de Hardware Telemático en Banco HIL (15 Casos: `CP-HW-01` a `CP-HW-15`)

Esta batería somete los equipos y periféricos físicos embarcados (iWave G26I con audIT EdgeHub, lector Technoton CANCrocodile, alimentación y balizas Bluetooth del inventario ofertado) a rigurosos ensayos en Banco de Simulación Física (Hardware-in-the-Loop, HIL) con instrumental calibrado de laboratorio, simulando las condiciones extremas de vibración, temperatura y cortes eléctricos de la flota de Transportes Curimón S.A.

**Variante de políticas de retención y correcciones (RNF-014):** Crear dominios separados: jornada ≥5 años, documento/viaje y liquidación 6, siniestro 10, habilitación vigencia+5, SUSPEL 5, esperas en cliente 3, series 2 en línea con agregación (Caso RT-05.10). Avanzar el reloj virtual antes y después del umbral de cada dominio y registrar el resultado esperado en el fixture. Mantener objetos con retención o suspensión de borrado; una revocación no elimina evidencia de conservación obligatoria. Toda corrección conserva valores previos, origen, autor y fecha, sin sobrescritura.

#### 9.0.7.1 CP-HW-01 — Corte Súbito de Energía Principal (12V/24V) — Conmutación a LiFePO4 en $< 10\text{ ms}$

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-HW-01`
**Nivel y Tipología:** Prueba de Hardware HIL / Gestión de Potencia Eléctrica y Conmutación Transitoria.
**Requerimiento Trazado:** Ensayo adicional de ingeniería; no sustituye controles contractuales.
**Precondiciones:** Gateway telemático conectado en banco HIL a fuente de alimentación programable DC ajustada a $24{,}0\text{ V}$. Osciloscopio digital de almacenamiento conectado al carril de alimentación interno ($V_{cc} = 3{,}3\text{ V}$) y al contacto de entrada principal. Batería LiFePO4 conectada y cargada al $100%$.
**Pasos de Ejecución:**
- El gateway se encuentra operando en régimen normal grabando datos telemáticos en eMMC.
- La fuente programable corta abruptamente la tensión de entrada principal a $0{,}0\text{ V} en < 1\text{ ms}$ (emulación de corte de bornes de batería del camión).
- Registrar con el osciloscopio la forma de onda de la tensión interna V_{cc} durante la transición.
- Verificar si se produce reinicio del procesador ARM o caída de tensión por debajo de $3{,}13\text{ V}$ (límite de reset de CPU).

**Datos de Entrada Sintéticos:** Transición escalón de tensión de $24{,}0\text{ V} a 0{,}0\text{ V} con t_{caída} \le 100\text{ }\mu\text{s}$.
**Resultado Esperado:** Se debe verificar que conmuta en $< 10\text{ ms}$ sin reboot. Los tiempos, porcentajes y magnitudes observados se registrarán después del ensayo; no se anticipan mediciones ni actas suscritas.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P1 (Bloqueante)**.
**Entorno:** Banco HIL / Osciloscopio Digital Rigol / Fuente DC Keysight.

#### 9.0.7.2 CP-HW-02 — Autonomía de Batería Interna LiFePO4 — $\ge 6\text{ Horas}$ Transmitiendo Telemetría

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-HW-02`
**Nivel y Tipología:** Prueba de Hardware HIL / Ensayo de Autonomía y Eficiencia Energética.
**Requerimiento Trazado:** Ensayo adicional de ingeniería; no sustituye controles contractuales.
**Precondiciones:** Batería LiFePO4 de 3.2V / 3.000 mAh en el gateway cargada al $100%$. Desconexión permanente de la alimentación de 24V del camión.
**Pasos de Ejecución:**
- Configurar el gateway en perfil de emergencia por corte de energía: GNSS activo con fijación cada 30 segundos, acelerómetro activo, y transmisión celular 4G cada 60 segundos.
- Monitorear continuamente el nivel de tensión de la celda LiFePO4 y el flujo de paquetes telemáticos emitidos hacia el broker de pruebas.
- Cronometrar el tiempo transcurrido hasta que el circuito de protección BMS (Battery Management System) corte por bajo voltaje seguro ($V_{cut} = 2{,}5\text{ V}$).

**Datos de Entrada Sintéticos:** Transmisión continua a intervalo de 60 segundos sobre red móvil simulada.
**Resultado Esperado:** Se debe verificar que la autonomía supera las 6 horas continuas. Los tiempos, porcentajes y magnitudes observados se registrarán después del ensayo; no se anticipan mediciones ni actas suscritas.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P1 (Bloqueante)**.
**Entorno:** Banco HIL / Registrador de Datos de Batería.

#### 9.0.7.3 CP-HW-03 — Retención embarcada obligatoria de 72 h y ampliación propuesta de 288 h

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-HW-03`
**Nivel y Tipología:** Prueba de Hardware HIL / Capacidad de Almacenamiento Masivo y Sombra Celular.
**Requerimiento Trazado:** RF-009, RNF-002, RNF-008.
**Precondiciones:** Gateway telemático con módulo de módem celular inhabilitado por software (ensayo controlado sin cobertura, sin atribuir duración a alta montaña o cierre fronterizo). Memoria industrial eMMC de 8,0 GB formateada con sistema de archivos ext4 transaccional con journaling.
**Pasos de Ejecución:**
- Inyectar mediante el simulador de bus CAN y generador de tramas GNSS primero el ciclo contractual de 72 horas y después, separadamente, la ampliación propuesta de 288 horas (muestreo: 1 paquete cada 30 s en movimiento, 1 paquete cada 5 min en detención).
- Verificar que la base de datos local SQLite WAL almacene cada paquete secuencialmente.
- Comprobar que no exista sobreescritura de registros antiguos (no ring-buffer overwrite) y medir el espacio físico, incluidos índices/WAL/adjuntos, y contrastarlo con la capacidad útil especificada y la reserva, sin imponer un límite de 100 MB sin cálculo.
- Habilitar la conexión celular y forzar la sincronización completa.

**Datos de Entrada Sintéticos:** 5.954 registros y ocho fotos por unidad para 72 h, según el perfil común; cuatro repeticiones para la ampliación 288 h.
**Resultado Esperado:** Se debe verificar que almacena las 72 horas contractuales sin pérdida ni corrupción; registrar por separado la ampliación 288 h. Los tiempos, porcentajes y magnitudes observados se registrarán después del ensayo; no se anticipan mediciones ni actas suscritas.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P1 (Bloqueante)**.
**Entorno:** Banco HIL / Inyector de Tramas de Simulación.

**Variante contractual obligatoria:** Ejecutar primero 72 h sin cobertura, con perfil de posición, jornada, eventos de conducción, tiempos en clientes y documentos del viaje. Conservar conteo y huellas de origen, cortar el enlace sin detener la captura, reabrirlo y conciliar registros sin pérdida ni corrupción. El ensayo de 288 h es adicional propuesto y su fallo no redefine el mínimo normativo. No se declara resultado previo.

**Conteo y capacidad del ensayo:** Para las 72 h se usa exactamente el perfil principal de CP-PERF-02 (3.237.656 bytes por unidad antes de overhead). Para 288 h se repite cuatro veces como hipótesis adicional (23.816 registros, 12.950.624 bytes), sin atribuirlo a datos del caso. Medir ocupación real con índices, WAL, adjuntos, cifrado y reserva. No se presupone ratio de compresión; comparar huellas de cada registro/adjunto tras reinicio y reconexión.

**Presupuesto físico propuesto:** El presupuesto de diseño usa 3,2 MB por 72 h con fotos, cuatro períodos para 288 h y factor de seguridad tres: 3,2 × 4 × 3 = 38,4 MB. Arranque 16 MB, sistemas A/B 2.048 MB, búfer 38,4 MB, diagnóstico rotativo 256 MB y geocercas/maestros 16 MB suman 2.374,4 MB, aproximadamente 2,4 GB. Son magnitudes aproximadas del presupuesto de arquitectura, no una conversión exacta del perfil serializado de prueba; la convención MB/GB y la ocupación efectiva de las imágenes se verifican al particionar. Los 8 GB nominales son la configuración mínima seleccionada del iWave G26I, no el volumen de telemetría ni una garantía de capacidad útil. No se presupone compresión; la homologación exige medir capacidad utilizable y ocupación con índices, WAL, adjuntos, cifrado y reserva, y recalcular ante desviaciones. Se conserva por separado el perfil serializado de CP-PERF-02 para conciliación de conteos y huellas; 38,4 MB no se presenta como su multiplicación exacta.

**Variante trazada a RF-009 (S3/T-12):** Desconectar 72 h con el perfil versionado de CP-PERF-02, reiniciar equipo y reconectar. Conciliar identificadores, orden y huellas de registros y documentos, sin pérdidas ni duplicados. El reloj de sincronización por camión va de recuperación de cobertura a confirmación completa y debe ser como máximo 20 min. En ensayo unitario se comprueba la regla con reloj controlado; latencia y comportamiento externo se acreditan en la prueba de integración, sistema o HIL asociada.

**Variante trazada a RNF-002 (S3/T-12):** Repetir el conjunto de 72 h sin red, reinicios y reenvío de cada lote dos veces. Esperar mismos identificadores y huellas al final, ninguna pérdida ni duplicado, con bitácora de conciliación. La compresión unitaria comprueba reversibilidad y no acredita capacidad ni sincronización del equipo completo. En ensayo unitario se comprueba la regla con reloj controlado; latencia y comportamiento externo se acreditan en la prueba de integración, sistema o HIL asociada.

**Variante trazada a RNF-008 (S3/T-12):** Ensayar 288 h separadamente como compromiso propuesto para cierres fronterizos: cuatro repeticiones del perfil de 72 h, 23.816 registros y 12.950.624 bytes brutos por unidad antes de overhead. Conciliar registros y documentos tras reconexión; cualquier pérdida falla ese compromiso. No atribuir a las bases 288 h de desconexión ni sustituir la aprobación de 72 h por esta ampliación. En ensayo unitario se comprueba la regla con reloj controlado; latencia y comportamiento externo se acreditan en la prueba de integración, sistema o HIL asociada.

#### 9.0.7.4 CP-HW-04 — Lectura CAN sin contacto con Technoton CANCrocodile — Lectura J1939 con Pérdida < 0{,}1%

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-HW-04`
**Nivel y Tipología:** Prueba de Hardware HIL / Adquisición Pasiva No Intrusiva en Bus CAN.
**Requerimiento Trazado:** RF-025, RNF-005.
**Precondiciones:** Lector sin contacto Technoton CANCrocodile montado sobre cables trenzados CAN_H y CAN_L sin pelar aislantes ni soldaduras. Generador de tráfico Vector CANoe emitiendo tramas SAE J1939 a $250\text{ kbps}$ con una carga de bus del $65%$.
**Pasos de Ejecución:**
- Emitir 1.000.000 de tramas CAN estándar SAE J1939 durante 2 horas.
- El firmware del gateway recibe y decodifica las tramas a través del lector sin contacto conectado al CAN del iWave G26I.
- Comparar el contador de tramas transmitidas por el generador Vector contra el contador de tramas válidas recibidas en el gateway.
- Calcular la tasa de pérdida de paquetes: $\text{Packet Loss Rate} = \dfrac{\text{Tramas Perdidas}}{\text{Tramas Emitidas}} \times 100$.

**Datos de Entrada Sintéticos:** 1.000.000 de tramas SAE J1939 generadas sintéticamente por hardware.
**Resultado Esperado:** Se debe verificar que la tasa de pérdida es $< 0{,}1%$. Los tiempos, porcentajes y magnitudes observados se registrarán después del ensayo; no se anticipan mediciones ni actas suscritas.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P1 (Bloqueante)**.
**Entorno:** Banco HIL / Analizador de Bus Vector CANoe + lector Technoton CANCrocodile.

**Variante trazada a RF-025 (S3/T-12):** Configurar mantenimiento a 100.000 km como dato sintético, no norma. Con odómetro real de 99.999 y 100.000 km esperar ausencia y presencia de aviso, respectivamente, enviado al sistema de talleres. Repetir con estimación: marcar incertidumbre y origen, sin presentar estimación como lectura real ni perder el aviso. En ensayo unitario se comprueba la regla con reloj controlado; latencia y comportamiento externo se acreditan en la prueba de integración, sistema o HIL asociada.

**Variante trazada a RNF-005 (S3/T-12):** Medir con analizador independiente el bus durante lectura y reinicio del equipo: cero tramas transmitidas por audIT. Conservar autorización del fabricante, mapa de señales y evidencia de no corte/no interferencia. Un parser correcto o una tasa baja de pérdidas no acredita por sí solo lectura pasiva ni preservación de garantía. En ensayo unitario se comprueba la regla con reloj controlado; latencia y comportamiento externo se acreditan en la prueba de integración, sistema o HIL asociada.

#### 9.0.7.5 CP-HW-05 — Eficiencia Energética y Consumo en Reposo — Standby $< 50\text{ mA}$ tras 30 min

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-HW-05`
**Nivel y Tipología:** Prueba de Hardware HIL / Consumo Parásito y Preservación de Batería de Arranque.
**Requerimiento Trazado:** Ensayo adicional de ingeniería; no sustituye controles contractuales.
**Precondiciones:** Instrumento de corriente calibrado con muestreo continuo en la alimentación de 24 V del conjunto ofertado. Registrar gateway, lectores y periféricos alimentados desde esa línea; no excluir cargas para alcanzar el umbral. Banco e instrumentos provistos o contratados por audIT.
**Pasos de Ejecución:**
- Simular apagado de ignición del motor (línea KL15 a 0V) a las 00:00.
- Durante los primeros 10 minutos, el equipo permanece en modo Shutdown Preparation cerrando archivos y sockets (consumo a medir, sin atribuir un valor típico no acreditado).
- A los 30 minutos, el gateway entra en modo Deep Sleep: configuración de bajo consumo homologada para el iWave G26I y sus periféricos, sin presuponer frecuencia de CPU o estados de módem disponibles. Registrar funciones que permanecen activas y comprobar despertar y continuidad de captura exigidas.
- Medir la corriente de reposo durante las siguientes 2 horas.

**Datos de Entrada Sintéticos:** Corte de ignición emulado por señal digital en banco HIL.
**Resultado Esperado:** Se debe verificar que la corriente de reposo es $< 50\text{ mA}$. Los tiempos, porcentajes y magnitudes observados se registrarán después del ensayo; no se anticipan mediciones ni actas suscritas.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P2 (Crítica)**.
**Entorno:** Banco HIL / Multímetro Keysight 34461A 6½ dígitos.

#### 9.0.7.6 CP-HW-06 — Transmisión y Recepción Prioritaria de Alerta SOS en Torre 24x7 en $\le 15\text{ s}$

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-HW-06`
**Nivel y Tipología:** Prueba de Hardware HIL / Respuesta Rápida de Pánico y Seguridad Vial.
**Requerimiento Trazado:** RF-027, RNF-001.
**Precondiciones:** Gateway en banco HIL conectado a la red celular real de pruebas mediante SIM card M2M multi-operador (Entel/Claro/Movistar).
**Pasos de Ejecución:**
- Pulsar el botón físico de pánico de cabina (contacto seco normalmente abierto).
- Cronometrar la transmisión y medir la llegada del evento a la consola web de la Torre 24x7.
- Repetir la prueba 10 veces en distintas horas del día.

**Datos de Entrada Sintéticos:** 10 pulsaciones físicas de botón de pánico en intervalos de 1 hora.
**Resultado Esperado:** Se debe verificar que el 100% de las alertas se reciben en $\le 15\text{ s}$. Los tiempos, porcentajes y magnitudes observados se registrarán después del ensayo; no se anticipan mediciones ni actas suscritas.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P1 (Bloqueante)**.
**Entorno:** Banco HIL / Red Móvil Real / Consola Torre.

**Variante trazada a RF-027 (S3/T-12):** Reproducir conducción acumulada 4 h 15 min y área segura alcanzable en 35 min: alertar antes de agotar cinco horas con diez minutos de holgura. Mover área a 50 min: no recomendarla como alcanzable legalmente. La alerta en movimiento es pasiva y no solicita escritura ni confirmación táctil. En ensayo unitario se comprueba la regla con reloj controlado; latencia y comportamiento externo se acreditan en la prueba de integración, sistema o HIL asociada.

**Variante trazada a RNF-001 (S3/T-12):** Reproducir velocidad cero y velocidad positiva; intentar escritura, formulario y confirmación en ambos estados. En movimiento descartar toda captura manual y mostrar solo aviso pasivo. La recuperación de interfaz detenida no debe perder datos; parámetros de milisegundos son objetivos adicionales, no permiso para interactuar conduciendo. En ensayo unitario se comprueba la regla con reloj controlado; latencia y comportamiento externo se acreditan en la prueba de integración, sistema o HIL asociada.

#### 9.0.7.7 CP-HW-07 — Ensayos Térmicos y Vibratorios SAE J1455 en Cámara Climática (-20 °C a +70 °C)

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-HW-07`
**Nivel y Tipología:** Prueba de Hardware HIL / Certificación Ambiental Automotriz y Estrés Físico.
**Requerimiento Trazado:** Ensayo adicional de ingeniería; no sustituye controles contractuales.
**Precondiciones:** Dispositivo gateway instalado dentro de cámara climática de ciclado térmico con mesa de vibración electrodinámica integrada.
**Pasos de Ejecución:**
- Someter el equipo a perfil de temperatura extrema: $-20\text{ }^\circ\text{C}$ durante 4 horas (emulación de noche cordillerana invernal), rampa a $+70\text{ }^\circ\text{C}$ durante 4 horas (emulación de cabina cerrada al sol en Desierto de Atacama).
- Aplicar el perfil de vibración aleatoria de ingeniería, sujeto a contraste del laboratorio con SAE J1455 (fixture de cabina pesada: $10\text{ Hz} a 2.000\text{ Hz}, 3{,}2\text{ G}_{RMS}$ en los 3 ejes).
- Operar el equipo continuamente durante todo el ciclo transmitiendo datos.

**Datos de Entrada Sintéticos:** Perfil térmico y dinámico de ingeniería; protocolo de laboratorio identificado con edición y apartados aplicables de SAE J1455. El laboratorio debe contrastar y aprobar el espectro, duración, montaje y ejes antes del ensayo; el fixture por sí solo no acredita conformidad normativa.
**Resultado Esperado:** Se debe verificar que supera el ciclo completo sin degradación funcional. Los tiempos, porcentajes y magnitudes observados se registrarán después del ensayo; no se anticipan mediciones ni actas suscritas.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P1 (Bloqueante)**.
**Entorno:** Laboratorio de Ensayos / Cámara Climática y Mesa de Vibración.

#### 9.0.7.8 CP-HW-08 — Grado de Estanqueidad IP67 — Resistencia a Polvo Minero y Sumersión Temporal

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-HW-08`
**Nivel y Tipología:** Prueba de Hardware HIL / Ensayos de Estanqueidad y Protección Ambiental.
**Requerimiento Trazado:** RNF-004.
**Precondiciones:** Muestra de tres conjuntos con gabinete, conectores y entradas de cableado exterior en su configuración ofertada, montados y sellados según procedimiento homologado. Registrar torque, juntas, modelo y montaje. El IP67 comprometido corresponde al conjunto expuesto, no a una certificación presumida del computador desnudo.
**Pasos de Ejecución:**
- Ensayo de Polvo (IP6X): Someter el equipo en cámara de polvo de talco circulante con presión negativa de 2 kPa durante 8 horas.
- Ensayo de Agua (IPX7): Sumergir el equipo en estanque de agua a 1 metro de profundidad durante 30 minutos continuos.
- Extraer el equipo, secar exteriormente, abrir el gabinete e inspeccionar presencia de humedad o partículas internas.

**Datos de Entrada Sintéticos:** Procedimiento de laboratorio con edición y apartados IP6X/IPX7 de IEC 60529 identificados; registrar su aplicabilidad al conjunto y configuración ensayados.
**Resultado Esperado:** Se debe verificar conformidad IP6X/IPX7 del conjunto según el procedimiento identificado y funcionamiento posterior de captura, persistencia y enlace. Inspección, mediciones y criterios de ingreso se registran por muestra; no se declara certificación obtenida. Los tiempos, porcentajes y magnitudes observados se registrarán después del ensayo; no se anticipan mediciones ni actas suscritas.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P1 (Bloqueante)**.
**Entorno:** Laboratorio de Certificación de Estanqueidad IP67.

**Variante trazada a RNF-004 (S3/T-12):** Usar agenda de visitas normales a terminal y órdenes de instalación; cada instalación se integra a una visita existente sin viaje adicional ni inmovilización extra. Comparar hora de liberación del vehículo con su visita prevista; cualquier demora adicional falla aunque el montaje dure menos de 60 min. Conservar orden, entrada, liberación y autorización. En ensayo unitario se comprueba la regla con reloj controlado; latencia y comportamiento externo se acreditan en la prueba de integración, sistema o HIL asociada.

#### 9.0.7.9 CP-HW-09 — Actualización de Firmware FOTA con Partición Dual A/B y Watchdog Hardware

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-HW-09`
**Nivel y Tipología:** Prueba de Hardware HIL / Recuperación Autónoma y Firmware Dual.
**Requerimiento Trazado:** Ensayo adicional de ingeniería; no sustituye controles contractuales.
**Precondiciones:** Equipo detenido en terminal autorizado y ventana de mantenimiento aprobada; probar además rechazo fuera de terminal o con vehículo en movimiento mediante ubicación/velocidad sintéticas. Gateway con esquema de arranque U-Boot configurado con particiones de sistema duales `/dev/mmcblk0p2` (Slot A) y `/dev/mmcblk0p3` (Slot B), y temporizador Watchdog hardware activado (timeout: 60 s).
**Pasos de Ejecución:**
- El sistema opera en Slot A. Flashear en Slot B una actualización corrupta con kernel panic intencional inducido.
- Configurar U-Boot para arrancar en Slot B en el próximo reinicio (bootcount = 1).
- Reiniciar el dispositivo.
- Observar que Slot B falla en arrancar; el Watchdog hardware expira a los 60 segundos y fuerza un hard reset.
- U-Boot incrementa el contador de fallos (bootcount = 2), detecta la anomalía y conmuta automáticamente el arranque al Slot A funcional.

**Datos de Entrada Sintéticos:** Imagen de firmware con instrucción de aborto inducida en `init`.
**Resultado Esperado:** Se debe verificar que el rollback opera de manera 100% autónoma. Los tiempos, porcentajes y magnitudes observados se registrarán después del ensayo; no se anticipan mediciones ni actas suscritas.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P1 (Bloqueante)**.
**Entorno:** Banco HIL / U-Boot Debug Port.

#### 9.0.7.10 CP-HW-10 — Verificación térmica y recepción de baliza Bluetooth

Este ensayo define entradas, controles y evidencia; no declara resultados ejecutados.

**ID:** `CP-HW-10`
**Nivel y Tipología:** Prueba HIL / Medición y comunicación Bluetooth.
**Requerimiento Trazado:** Ensayo adicional de ingeniería; no sustituye controles contractuales.
**Precondiciones:** Baliza del modelo T-11 vinculada al semirremolque, iWave G26I y patrón térmico independiente calibrado. Rango, resolución y error máximo documentados y aprobados para el modelo.
**Pasos de Ejecución:**
- Seleccionar puntos de ensayo dentro del rango documentado y de la aplicación refrigerada.
- Comparar lectura recibida por Bluetooth con patrón tras estabilización y registrar error por punto.
- Probar pérdida de anuncio, batería baja si está disponible y cambio de baliza; conservar identidad, fecha y calidad.

**Datos de Entrada Sintéticos:** Consignas dentro del rango aprobado; cada valor y tolerancia constan en el manifiesto.
**Resultado Esperado:** Error dentro de la tolerancia aprobada del modelo y asociación correcta. Ausencia o antigüedad genera aviso de dato no disponible; no se mantiene una lectura antigua como actual. Si el rango no cubre la carga prevista, no se homologa esa aplicación. No se presupone precisión de ±0,3 °C ni operación a −30 °C.
**Pass/Fail y Severidad:** Pass solo si se cumplen todos los criterios y se conserva evidencia reproducible; cualquier pérdida, acceso no autorizado o salida incorrecta implica Fail. Severidad alta para seguridad y evidencia.
**Entorno:** HIL / Cámara térmica, patrón y receptor Bluetooth.

#### 9.0.7.11 CP-HW-11 — Acceso Local al DET Conforme y Bloqueo ante Documento No Emitido

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-HW-11`
**Nivel y Tipología:** Ensayo de hardware y aplicación local / Conformidad y bloqueo.
**Requerimiento Trazado:** RF-014.
**Precondiciones:** Vehículo detenido; orden y datos completos. Doble del ERP configurado con esquema e interfaz versionados. El fixture identifica un documento admitido y uno no emitido/no conforme; la validación fiscal real se homologa con el ERP y su proveedor, sin presumir API o contingencia certificada.
**Pasos de Ejecución:**
- Preparar datos desde la orden y enviarlos al ERP contable como único emisor, con identificador idempotente.
- Validar estado, identidad del emisor, firma, folio y asociación inequívoca a la orden según el contrato de integración. Una firma exclusiva de audIT no demuestra conformidad tributaria.
- Recuperar el documento conforme admitido por el fixture en cabina y cortar la cobertura. Confirmar disponibilidad local antes de autorizar movimiento.
- Repetir con documento ausente, rechazo, folio no válido, revocación o datos discordantes: debe mantenerse el bloqueo; no emitir un documento paralelo ni permitir salida con una promesa de regularización.
- Repetir el envío con el mismo identificador: debe existir una sola emisión y conservarse auditoría y respuesta del ERP. Verificar reconexión sin duplicados.

**Datos de Entrada Sintéticos:** Dos órdenes de prueba, mismo identificador repetido, estado `CONFORME` y estado `NO_EMITIDO`, documento/firma/folio y esquema de prueba versionados; manifestar emisor, orden y huellas. Reloj virtual del fixture.
**Resultado Esperado:** Disponible el documento conforme antes del movimiento; bloqueadas todas las variantes negativas, una única emisión por orden y evidencia de validación conservada. En pruebas de sistema/hardware se mide ≤90 s; en pruebas unitarias se valida el estado, sin sustituir el tiempo E2E.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: Alta cuando afecta seguridad o evidencia; mayor en objetivos adicionales.
**Entorno:** staging/HIL con dispositivo y contrato ERP de ensayo. Homologación real del mecanismo de contingencia antes de despliegue; la falta de disponibilidad no se resuelve fingiendo certificación.

**Variante trazada a RF-014 (S3/T-12):** Ejecutar dos rutas de contingencia: DET anticipado por ERP desde la orden y datos enviados por enlace satelital al ERP con folio de vuelta al vehículo. Antes del movimiento debe existir DET conforme accesible localmente; ausencia de folio, datos discordantes y respuesta fuera de plazo bloquean. Un PDF local firmado por audIT no sustituye emisión del ERP. En ensayo unitario se comprueba la regla con reloj controlado; latencia y comportamiento externo se acreditan en la prueba de integración, sistema o HIL asociada.

#### 9.0.7.12 CP-HW-12 — Detección Inmediata de Desconexión de Antena GNSS y Anti-Jamming RF

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-HW-12`
**Nivel y Tipología:** Prueba de Hardware HIL / Detección de Sabotaje Físico y Seguridad de Activos.
**Requerimiento Trazado:** Ensayo adicional de ingeniería; no sustituye controles contractuales.
**Precondiciones:** Antena GNSS activa conectada a la entrada coaxial SMA del gateway con circuito de detección de polarización de antena (antenna supervisor).
**Pasos de Ejecución:**
- El gateway se encuentra rastreando satélites GPS/GLONASS normalmente.
- Desconectar físicamente el cable de la antena GNSS (simulación de corte de cable o sabotaje).
- El circuito hardware detecta la caída de consumo DC en la línea de antena ($I < 2\text{ mA}$).
- Encender transmisor de interferencia intencional RF (Jammer GNSS en bandas L1/L2) y verificar detección de relación señal/ruido degradada ($C/N_0 < 15\text{ dB-Hz}$).

**Datos de Entrada Sintéticos:** Desconexión física SMA e inyección controlada de ruido RF.
**Resultado Esperado:** Se debe verificar que detecta corte de antena y jamming sin ambigüedad. Los tiempos, porcentajes y magnitudes observados se registrarán después del ensayo; no se anticipan mediciones ni actas suscritas.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P1 (Bloqueante)**.
**Entorno:** Banco HIL / Jaula de Faraday / Generador de Ruido RF.

#### 9.0.7.13 CP-HW-13 — Acelerómetro 3D MEMS — Detección Inercial de Frenadas Bruscas y Volcamiento

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-HW-13`
**Nivel y Tipología:** Prueba de Hardware HIL / Seguridad Vial Activa y Detección de Accidentes.
**Requerimiento Trazado:** Ensayo adicional de ingeniería; no sustituye controles contractuales.
**Precondiciones:** Sensor acelerómetro/giróscopo triaxial MEMS de 16 bits muestreando internamente a $100\text{ Hz}$.
**Pasos de Ejecución:**
- Montar el gateway en banco de ensayos cinemáticos giratorio.
- Aplicar desaceleración longitudinal brusca de $-4{,}5\text{ m/s}^2 durante 800\text{ ms}$ (emulación de frenada de emergencia).
- Aplicar inclinación transversal brusca $> 60^\circ$ combinada con desaceleración lateral (emulación de vuelco).

**Datos de Entrada Sintéticos:** Perfil cinemático de frenada brusca y giro de vuelco en mesa giratoria.
**Resultado Esperado:** Se debe verificar que detecta el impacto y preserva la caja negra. Los tiempos, porcentajes y magnitudes observados se registrarán después del ensayo; no se anticipan mediciones ni actas suscritas.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P1 (Bloqueante)**.
**Entorno:** Banco HIL / Mesa de Giro Cinemático.

#### 9.0.7.14 CP-HW-14 — Identificación del conductor y bloqueo administrativo de asignación

Este ensayo verifica la identificación y la decisión de asignación sin actuar sobre el arranque, el motor o el bus del vehículo.

**ID:** `CP-HW-14`
**Nivel y Tipología:** Prueba HIL / Integración de identificación con Personas y cumplimiento y despacho.
**Requerimiento Trazado:** RF-001 y RF-003 (veredicto de asignación), RNF-005 (interfaz pasiva); ensayo complementario, sin sustituir sus casos funcionales.
**Precondiciones:** Banco provisto por audIT con el lector de identificación seleccionado y autorizado conforme a S4/T-11, conectado al iWave G26I mediante su interfaz homologada. Servicio de identificación y despacho en QA, reloj controlado y catálogo sintético de credenciales, vigencias y jornadas. Sin relé de corte, salida a motor ni escritura al CAN. Registrar modelo, firmware, interfaz y permisos; no se presupone RFID, iButton o RS-485 si no constan en el inventario.
**Pasos de Ejecución:**
- Solicitar asignación sin identidad válida: verificar rechazo, causa y registro, sin habilitar despacho.
- Presentar identificador desconocido y después uno revocado: verificar rechazo y conservación de origen/fecha del intento.
- Presentar identidad válida con licencia vencida o descanso insuficiente: verificar identificación correcta y asignación bloqueada por la causa legal correspondiente.
- Presentar identidad habilitada, jornada y vehículo conformes: verificar que la asignación procede únicamente después del veredicto favorable de todos los controles aplicables.
- Repetir con lector desconectado o lectura inválida: no convertir ausencia de identidad en un conductor habilitado ni reutilizar el veredicto de otro usuario.
- Observar las interfaces físicas durante la secuencia y el reinicio: no debe existir actuación sobre arranque ni transmisión de tramas de control al CAN.

**Datos de Entrada Sintéticos:** Credenciales desconocida, revocada y vigente; estados de licencia, descanso y vehículo conformes/no conformes, con reloj y oráculo independientes.
**Resultado Esperado:** Cada intento conserva identidad o motivo de ausencia, fuente, fecha, veredicto y causa. Solo la combinación de identidad válida y todos los controles conformes habilita asignación. Los casos no conformes bloquean el despacho administrativo; el vehículo no recibe órdenes de inmovilización. Lectura pasiva y montaje preservan garantía y sistemas de seguridad. No se impone un tiempo de liberación de relé ni se acredita una prueba ejecutada.
**Pass/Fail y Severidad:** Pass si todas las decisiones coinciden con el oráculo, se conservan los registros y no existe actuación física sobre el vehículo. Cualquier autorización indebida, pérdida de trazabilidad o actuación sobre arranque/CAN es Fail. Severidad: **P1 (Bloqueante)**.
**Entorno:** Banco HIL de identificación e iWave G26I, servicios de QA y analizador independiente de interfaces; sin tablero de encendido ni inmovilizador.

#### 9.0.7.15 CP-HW-15 — Descarga Remota Dedicada de Tacógrafo Digital Mediante Enlace DSRC

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-HW-15`
**Nivel y Tipología:** Prueba de Hardware HIL / Interfaz Directa de Tacógrafo Digital y Descarga Legal.
**Requerimiento Trazado:** RF-002, RF-007.
**Precondiciones:** Tacógrafo digital de pruebas VDO DTCO 1381 conectado al puerto serie del gateway mediante cable K-Line / CAN-C dedicado. Tarjeta digital de empresa insertada en el lector remoto.
**Pasos de Ejecución:**
- Enviar comando de descarga remota programada desde la nube hacia el gateway.
- El gateway autentica la sesión contra el tacógrafo digital utilizando los certificados de la tarjeta de empresa.
- Ejecutar descarga completa de la memoria masiva de 90 días y de la tarjeta de conductor.
- Medir tiempo total de transferencia y validar la integridad del archivo binario descargado.

**Datos de Entrada Sintéticos:** Tacógrafo con 90 días de actividad sintética grabada.
**Resultado Esperado:** Se debe verificar que descarga el archivo íntegro y autenticado. Los tiempos, porcentajes y magnitudes observados se registrarán después del ensayo; no se anticipan mediciones ni actas suscritas.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P2 (Crítica)**.
**Entorno:** Banco HIL / Tacógrafo Digital VDO DTCO 1381.

**Variante trazada a RF-007 (S3/T-12):** Descargar dos archivos originales de tacógrafo con conductores y vehículos distintos; conservar bytes y huellas originales, relacionar conductor y vehículo y clasificar nivel 1. Archivo truncado, alterado o sin identidad debe rechazarse o quedar pendiente de verificación, sin convertirse en evidencia válida. En ensayo unitario se comprueba la regla con reloj controlado; latencia y comportamiento externo se acreditan en la prueba de integración, sistema o HIL asociada.

### 9.0.8 Batería 6: Pruebas de Aceptación de Usuario (UAT) en Terreno (15 Casos: `CP-UAT-01` a `CP-UAT-15`)

Esta batería propone los ensayos de aceptación en terreno con usuarios operativos de Transportes Curimón S.A. en sus cinco nodos geográficos estratégicos: San Bernardo (Matriz), Antofagasta, Talca, Los Ángeles y Puerto Montt. Cada caso cuenta con la participación de despachadores, mecánicos de taller, conductores y jefaturas de terminal.

#### 9.0.8.1 CP-UAT-01 — UAT Terminal San Bernardo — Operación de Torre de Control 24x7 con 22 Despachadores

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-UAT-01`
**Nivel y Tipología:** Prueba de Aceptación de Usuario (UAT) / Operación en Tiempo Real y Ergonomía.
**Requerimiento Trazado:** RF-008, RNF-009, RNF-010.
**Precondiciones:** Sala de control de Torre 24x7 en San Bernardo operativa. 22 despachadores en sus puestos de trabajo organizados en 3 turnos rotativos.
**Pasos de Ejecución:**
- Los 22 despachadores inician sesión simultáneamente en sus estaciones de trabajo con credenciales corporativas SSO.
- Ejecutar tareas habituales de despacho durante un turno completo de 8 horas: asignación de órdenes, seguimiento de flota en mapa mural, atención de alertas de descanso e intercomunicación con choferes.
- Evaluar la tasa de finalización de tareas y la usabilidad de la interfaz sin asistencia de ingenieros de audIT.

**Datos de Entrada Sintéticos:** 180 órdenes de transporte sintéticas programadas durante el turno.
**Resultado Esperado:** Se debe verificar que el 100% de los despachadores opera de forma autónoma. Los tiempos, porcentajes y magnitudes observados se registrarán después del ensayo; no se anticipan mediciones ni actas suscritas.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P1 (Bloqueante)**.
**Entorno:** Terreno / Torre de Programación San Bernardo.

**Variantes de administración y costo de operación (RNF-009/RNF-010):** Personal TI designado de la dotación de nueve ejecuta con cuentas de prueba las tareas de alta, consulta de salud, restauración autorizada y escalamiento siguiendo el manual. Identificar tareas que requieren especialidad de audIT, sin atribuirla a TI del cliente. Revisar un modelo sintético de 36 meses con cantidades, unidades, periodicidad y componentes de nube, enlaces, licencias, soporte y reposición; cotejar sumas y categorías contra T-11 y modelo económico sin publicar valores de la oferta en el documento técnico. Fallar ante rubros omitidos, unidades incompatibles o doble conteo. El ensayo no demuestra por sí solo dotación suficiente 24x7.

**Variante trazada a RF-008 (S3/T-12):** Construir 374 unidades únicas, 148 propias y 226 externas, con muestras de todas las fuentes y marcas de tiempo conocidas. La vista contiene 374 identidades sin duplicación; cada posición muestra fuente y antigüedad y la jornada su nivel real. Si no existe posición, mostrar no disponible; no inventar coordenadas ni equiparar ubicación a descanso. En ensayo unitario se comprueba la regla con reloj controlado; latencia y comportamiento externo se acreditan en la prueba de integración, sistema o HIL asociada.

**Variante trazada a RNF-009 (S3/T-12):** Con la dotación cliente de nueve personas, ejecutar altas, consulta de salud y escalamiento con cuentas limitadas; comparar matriz de responsabilidad con manual. Toda especialidad no disponible en cliente debe estar asignada al servicio audIT 24x7 con responsable, turno y escalamiento de prueba. La capacitación de despachadores no acredita cobertura operativa del servicio ni su dotación. En ensayo unitario se comprueba la regla con reloj controlado; latencia y comportamiento externo se acreditan en la prueba de integración, sistema o HIL asociada.

#### 9.0.8.2 CP-UAT-02 — UAT Terminal San Bernardo — Protocolo de Instalación de Hardware en Taller Central

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-UAT-02`
**Nivel y Tipología:** Prueba de Aceptación de Usuario (UAT) / Despliegue Físico y Mantenimiento.
**Requerimiento Trazado:** RF-024, RNF-003, RNF-004, RNF-005.
**Precondiciones:** Tractocamión propio ingresando a mantenimiento programado de 10.000 km en taller central San Bernardo. Cuadrilla de técnicos mecánicos de Curimón S.A. capacitada por audIT.
**Pasos de Ejecución:**
- Técnico mecánico ejecuta el procedimiento de montaje físico del gateway telemático, antena externa GNSS/4G y lector sin contacto Technoton CANCrocodile.
- Verificar que no se corten ni perforen cables del bus CAN original del camión.
- Conectar equipo a la alimentación protegida por fusible aéreo automotriz.
- Realizar encendido de motor y ejecutar autodiagnóstico en la PWA de taller audIT.
- Cronometrar el tiempo total de intervención del camión.

**Datos de Entrada Sintéticos:** Checklist de instalación mecánica y eléctrica en PWA de taller.
**Resultado Esperado:** Se debe verificar que el tiempo de instalación es $< 60\text{ minutos}$ con 0 invasión de cables. Los tiempos, porcentajes y magnitudes observados se registrarán después del ensayo; no se anticipan mediciones ni actas suscritas.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P2 (Crítica)**.
**Entorno:** Terreno / Taller Central San Bernardo.

**Autorización y alcance físico:** No intervenir un equipo de terceros sin acuerdo expreso. Ejecutar durante una pasada regular por terminal, sin detener globalmente la flota. Documentar duración medida, modelo, permisos, procedimiento no invasivo, señales y garantía; disponer del equipo de ensayo especificado por audIT, sin presumirlo propiedad del cliente. El banco reproduce CANCrocodile y las balizas Bluetooth seleccionadas en T-11, sin agregar sensores alternativos a la oferta. El criterio se aplica a la interfaz efectivamente seleccionada.

**Variante trazada a RF-024 (S3/T-12):** Registrar una intervención offline de taller externo con técnico, equipo, fecha, odómetro, trabajo, repuestos y evidencia; reconectar dos veces. Esperar una sola intervención íntegra en hoja de vida e inventario actualizado una vez. Quitar técnico o repuesto obligatorio: rechazar o señalar registro incompleto, sin tratarlo como intervención válida. En ensayo unitario se comprueba la regla con reloj controlado; latencia y comportamiento externo se acreditan en la prueba de integración, sistema o HIL asociada.

**Variante trazada a RNF-004 (S3/T-12):** Usar agenda de visitas normales a terminal y órdenes de instalación; cada instalación se integra a una visita existente sin viaje adicional ni inmovilización extra. Comparar hora de liberación del vehículo con su visita prevista; cualquier demora adicional falla aunque el montaje dure menos de 60 min. Conservar orden, entrada, liberación y autorización. En ensayo unitario se comprueba la regla con reloj controlado; latencia y comportamiento externo se acreditan en la prueba de integración, sistema o HIL asociada.

#### 9.0.8.3 CP-UAT-03 — UAT Terminal San Bernardo — Conciliación de Carga de Diésel con Estanque Propio

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-UAT-03`
**Nivel y Tipología:** Prueba de Aceptación de Usuario (UAT) / Control de Combustible y Caudalímetro.
**Requerimiento Trazado:** Ensayo adicional de ingeniería; no sustituye controles contractuales.
**Precondiciones:** Estanque propio de diésel de San Bernardo equipado con caudalímetro digital y surtidor con identificación RFID.
**Pasos de Ejecución:**
- Camión `TRK-015` se posiciona en la pista de carga de combustible.
- Operador de patio pasa el identificador RFID del camión por el surtidor y suministra 350 litros de diésel.
- El caudalímetro digital transmite la carga al concentrador de patio.
- Verificar en el sistema de gestión de patio la concordancia entre los litros despachados y la lectura del sensor telemático de estanque del camión.

**Datos de Entrada Sintéticos:** Fixture de conciliación: 350 litros de referencia de ensayo, sin afirmar carga realizada o certificación examinada. En terreno se conserva lectura del instrumento homologado.
**Resultado Esperado:** Se debe verificar que concilia automáticamente sin descuadres de inventario. Los tiempos, porcentajes y magnitudes observados se registrarán después del ensayo; no se anticipan mediciones ni actas suscritas.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P2 (Crítica)**.
**Entorno:** Terreno / Pista de Combustible San Bernardo.

#### 9.0.8.4 CP-UAT-04 — UAT Instalación de Cliente — escenario sintético Valparaíso — Control de Semirremolques Portacontenedores y Precintos

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-UAT-04`
**Nivel y Tipología:** Prueba de Aceptación de Usuario (UAT) / Logística Portuaria y Despacho Rápido.
**Requerimiento Trazado:** Ensayo adicional de ingeniería; no sustituye controles contractuales.
**Precondiciones:** Escenario sintético de instalación ajena a Curimón; infraestructura, interfaces, permisos y participación por validar.  instalación de cliente en Valparaíso. Llegada de tractocamión a retirar contenedor marítimo de exportación de 40 pies.
**Pasos de Ejecución:**
- Despachador de Valparaíso escanea con la PWA el código del contenedor marítimo y el número de precinto aduanero (sello de seguridad).
- El sistema valida la orden de transporte marítima y asocia el contenedor a la rampla portacontenedor.
- Comprobar que el tiempo de despacho en garita sea inferior a 3 minutos.

**Datos de Entrada Sintéticos:** Contenedor `MSKU-998812-4`, Precinto aduanero `CL-VALP-55412`.
**Resultado Esperado:** Se debe verificar que el despacho en garita toma $< 3\text{ minutos}$. Los tiempos, porcentajes y magnitudes observados se registrarán después del ensayo; no se anticipan mediciones ni actas suscritas.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P2 (Crítica)**.
**Entorno:** Terreno / Garita instalación de cliente en Valparaíso.

#### 9.0.8.5 CP-UAT-05 — UAT Instalación de Cliente — escenario sintético Valparaíso — Inspección de Conexión Reefer y Cadena Fría Portuaria

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-UAT-05`
**Nivel y Tipología:** Prueba de Aceptación de Usuario (UAT) / Cadena de Frío y Conexión Eléctrica.
**Requerimiento Trazado:** Ensayo adicional de ingeniería; no sustituye controles contractuales.
**Precondiciones:** Escenario sintético de instalación ajena a Curimón; infraestructura, interfaces, permisos y participación por validar.  Patio de consolidación Valparaíso. Rampla reefer cargada con fruta de exportación conectada a torre eléctrica de patio (reefer plug).
**Pasos de Ejecución:**
- Técnico frigorista conecta la rampla a la toma de 440V del patio de Valparaíso.
- Verificar que el gateway audIT registre el cambio de fuente de energía (del motor diésel de la rampla a la red eléctrica trifásica).
- Monitorear las lecturas de la baliza Bluetooth asociada al semirremolque durante 3 horas; registrar recepción, antigüedad y cortes de comunicación.

**Datos de Entrada Sintéticos:** Parámetros de temperatura de pulpa de fruta a $-0{,}5\text{ }^\circ\text{C}$.
**Resultado Esperado:** Se debe verificar que mantiene trazabilidad térmica continua en patio. Los tiempos, porcentajes y magnitudes observados se registrarán después del ensayo; no se anticipan mediciones ni actas suscritas.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P1 (Bloqueante)**.
**Entorno:** Terreno / Patio Reefer instalación de cliente en Valparaíso.

#### 9.0.8.6 CP-UAT-06 — UAT Instalación de Cliente — escenario sintético Valparaíso — Detección Automática de Esperas en Antepuerto (ZEAL)

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-UAT-06`
**Nivel y Tipología:** Prueba de Aceptación de Usuario (UAT) / Detección Satelital de Esperas Portuarias.
**Requerimiento Trazado:** RF-010, RNF-007.
**Precondiciones:** Escenario sintético de instalación ajena a Curimón; infraestructura, interfaces, permisos y participación por validar.  Geocerca poligonal configurada sobre la Zona de Extensión de Apoyo Logístico (ZEAL) de Valparaíso.
**Pasos de Ejecución:**
- Camión ingresa a la ZEAL y queda en fila de espera de aduana por 4 horas y 15 minutos con motor encendido y apagado intermitente.
- Verificar que el sistema detecte automáticamente el ingreso a la ZEAL sin requerir que el chofer marque manualmente en la aplicación.
- Comprobar que registre con precisión el tiempo total de espera portuaria.

**Datos de Entrada Sintéticos:** Camión `LKJH-89` con contenedor en antepuerto ZEAL.
**Resultado Esperado:** Se debe verificar que detecta la estadía portuaria sin intervención humana. Los tiempos, porcentajes y magnitudes observados se registrarán después del ensayo; no se anticipan mediciones ni actas suscritas.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P2 (Crítica)**.
**Entorno:** Terreno / ZEAL Valparaíso.

#### 9.0.8.7 CP-UAT-07 — UAT Terminal Los Ángeles — Relevos de Tripulación Forestal y Descansos Art. 25 bis

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-UAT-07`
**Nivel y Tipología:** Prueba de Aceptación de Usuario (UAT) / Operación Forestal y Jornada Laboral.
**Requerimiento Trazado:** Ensayo adicional de ingeniería; no sustituye controles contractuales.
**Precondiciones:** Terminal Los Ángeles. Arribo de tractocamión maderero tras 4 horas y 45 minutos de conducción continua desde faena cordillerana en Arauco.
**Pasos de Ejecución:**
- Conductor titular se presenta en la garita de Los Ángeles y efectúa cambio de turno.
- El conductor relevo se autentica con su tarjeta RFID en el gateway de cabina.
- El sistema evalúa si el conductor relevo posee su descanso diario reglamentario de 8 horas cumplido.
- Autorizar la reanudación del viaje hacia el puerto de Coronel.

**Datos de Entrada Sintéticos:** Relevo de chofer forestal en Los Ángeles.
**Resultado Esperado:** Se debe verificar que gobierna el relevo y protege el descanso del chofer saliente. Los tiempos, porcentajes y magnitudes observados se registrarán después del ensayo; no se anticipan mediciones ni actas suscritas.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P1 (Bloqueante)**.
**Entorno:** Terreno / Terminal Los Ángeles.

#### 9.0.8.8 CP-UAT-08 — UAT Instalación de Cliente — escenario sintético Concepción — Integración de Órdenes y Control de Pesaje en Báscula

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-UAT-08`
**Nivel y Tipología:** Prueba de Aceptación de Usuario (UAT) / Pesaje Industrial y Control de Sobrepeso.
**Requerimiento Trazado:** Ensayo adicional de ingeniería; no sustituye controles contractuales.
**Precondiciones:** Escenario sintético de instalación ajena a Curimón; infraestructura, interfaces, permisos y participación por validar.  Báscula de pesaje de camiones de la instalación de cliente en Concepción conectada vía interfaz TCP/IP a la red audIT.
**Pasos de Ejecución:**
- Camión cargado con fardos de celulosa sube a la báscula de Concepción.
- La báscula captura el peso bruto vehicular (PBV = 44.800 kg; umbral sintético de ensayo = 45.000 kg; no se presenta como límite legal universal).
- El sistema cruza peso y orden contra la matriz de límites versionada del fixture. Repetir con 45.000 y 45.200 kg. La matriz normativa definitiva exige identificar configuración vehicular y límites por eje antes de homologar; el fixture no acredita conformidad normativa.

**Datos de Entrada Sintéticos:** Ticket de báscula digital con peso bruto y distribución por eje.
**Resultado Esperado:** Con los demás factores conformes, el fixture permite 44.800 y 45.000 kg y bloquea 45.200 kg por superar el umbral sintético; conservar ticket, configuración y motivo. No se afirma que 45.000 kg sea admisible para toda configuración. Los tiempos, porcentajes y magnitudes observados se registrarán después del ensayo; no se anticipan mediciones ni actas suscritas.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P1 (Bloqueante)**.
**Entorno:** Terreno / Báscula instalación de cliente en Concepción.

#### 9.0.8.9 CP-UAT-09 — UAT Terminal Talca — Despacho en Modo Mixto con Transportistas — escenario sintético

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-UAT-09`
**Nivel y Tipología:** Prueba de Aceptación de Usuario (UAT) / Gestión de Terceros en Macrozona Sur.
**Requerimiento Trazado:** RF-026, RF-028.
**Precondiciones:** 5 transportistas subcontratados de la zona de Talca (muestra sintética) registrados en el Portal de Adhesión (camiones con mecanismo autorizado de acceso a posición, sin presuponer API).
**Pasos de Ejecución:**
- Despachador de Talca asigna 5 órdenes de carga industrial a los camiones subcontratados.
- Los transportistas aceptan el viaje desde la PWA móvil firmando electrónicamente la atestación de jornada (Nivel 5 de evidencia probatoria).
- Verificar que los 5 camiones se visualicen en la consola de Talca y Torre Central sin retardos.

**Datos de Entrada Sintéticos:** 5 órdenes asignadas a patentes de terceros de Talca.
**Resultado Esperado:** Se debe verificar que integra a los transportistas externos con Nivel 5 conforme. Los tiempos, porcentajes y magnitudes observados se registrarán después del ensayo; no se anticipan mediciones ni actas suscritas.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P2 (Crítica)**.
**Entorno:** Terreno / Terminal Talca.

**Variante de incorporación de terceros (RF-026):** Además del despacho sobre cinco órdenes sintéticas, completar invitación, condiciones de adhesión, registro de camiones y conductores, consentimiento por propietario y alcance de los permisos. Rechazar la adhesión en una muestra y revocar otra; no debe habilitarse integración ni despacho sin las condiciones obligatorias. Conservar comprobante y auditoría de cada transición.

**Variante trazada a RF-026 (S3/T-12):** Calcular los ocho indicadores mensuales de adhesión de S3 con sus denominadores. Con 148 titulares, 104 en M16 y 134 en M21 cumplen las metas de al menos 70 y 90 por ciento; 103 y 133 no. En M9, menos del 40 por ciento firmado activa el escenario previsto: 59 de 148 no llega; 60 supera el umbral. Conservar serie mensual, estados de invitación/aceptación/rechazo/revocación y medida correctiva, sin inventar adhesiones reales. En ensayo unitario se comprueba la regla con reloj controlado; latencia y comportamiento externo se acreditan en la prueba de integración, sistema o HIL asociada.

**Variante trazada a RF-028 (S3/T-12):** Crear transportistas en modalidades completa, de datos y sin adhesión según S3; comprobar nivel 2, reposo de nivel 4 con atestación de nivel 5 y validación documental con y sin atestación firmada; visualizar modalidad, fuente, nivel y veredicto por separado. Comprobar la cascada de niveles 1 a 4 con asignación y el nivel 5 con asignación con marca y responsabilidad registrada, sin bloqueos legales. En la modalidad de datos, exigir la atestación firmada que complementa el reposo del camión: con ella asignar con marca y sin ella bloquear la asignación. En el estado sin adhesión, la validación documental con atestación válida permite asignar con marca; sin atestación no hay veredicto habilitante ni asignación. Sin fuente bloquear, con excepción sólo según RN-04; con incumplimiento legal bloquear en todas las modalidades. El nivel 0 voluntario no cambia el veredicto. En ensayo unitario se comprueba la regla con reloj controlado; latencia y comportamiento externo se acreditan en la prueba de integración, sistema o HIL asociada.

#### 9.0.8.10 CP-UAT-10 — UAT Terminal Antofagasta — Despacho Bloqueante SUSPEL, Código QR y Rótulos NCh 2190

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-UAT-10`
**Nivel y Tipología:** Prueba de Aceptación de Usuario (UAT) / Sustancias Peligrosas y Minería.
**Requerimiento Trazado:** RF-006.
**Precondiciones:** Terminal Antofagasta. Unidad SUSPEL preparándose para despacho de Cianuro de Sodio (UN 1689, Clase 6.1 Tóxico) hacia faena minera en Calama.
**Pasos de Ejecución:**
- Inspector de seguridad de Antofagasta realiza checklist de terreno con la PWA: rótulos NCh 2190 (rombo de tóxico), extintores certificados, y neutralizadores de derrame.
- Escanear el código QR de la Hoja de Datos de Seguridad (HDS) en cabina.
- Verificar que el sistema bloquee el botón de autorización final si falta cualquiera de los elementos del checklist.
- Completar el checklist con 100% de conformidad y autorizar despacho.

**Datos de Entrada Sintéticos:** Carga UN 1689, checklist digital de 14 puntos normativos.
**Resultado Esperado:** Se debe verificar que el enclavamiento físico y documental opera con tolerancia cero. Los tiempos, porcentajes y magnitudes observados se registrarán después del ensayo; no se anticipan mediciones ni actas suscritas.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P1 (Bloqueante)**.
**Entorno:** Terreno / Patio SUSPEL Terminal Antofagasta.

#### 9.0.8.11 CP-UAT-11 — UAT Terminal Antofagasta — Resiliencia en Sombra Extrema Ruta 5 Norte (>80 km)

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-UAT-11`
**Nivel y Tipología:** Prueba de Aceptación de Usuario (UAT) / Prueba de Ruta Real en Desierto de Atacama.
**Requerimiento Trazado:** RNF-008.
**Precondiciones:** Tractocamión equipado saliendo de Antofagasta en dirección sur por la Ruta 5 Norte atravesando el tramo de silencio celular de 85 km en el sector de Aguas Verdes / Domeyko.
**Pasos de Ejecución:**
- El camión entra en la zona de sombra celular; comprobar que el indicador de cabina señale modo Offline Buffer Active.
- Conducir a lo largo de los 85 km sin cobertura (duración aproximada: 1 hora y 15 minutos).
- El conductor realiza una detención de descanso de 15 minutos en berma de seguridad dentro de la zona de sombra.
- Al salir de la zona de sombra celular en el sector de Chañaral, verificar la sincronización automática de la telemetría acumulada con la Torre de Control.

**Datos de Entrada Sintéticos:** Viaje real en ruta desértica con 85 km sin señal móvil.
**Resultado Esperado:** Se debe verificar que reconstruye la trayectoria completa sin vacíos de datos. Los tiempos, porcentajes y magnitudes observados se registrarán después del ensayo; no se anticipan mediciones ni actas suscritas.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P1 (Bloqueante)**.
**Entorno:** Terreno / Ruta 5 Norte (Tramo Antofagasta-Chañaral).

#### 9.0.8.12 CP-UAT-12 — UAT Terminal Antofagasta — Protocolo de Emergencia ante Derrame Químico / Botón SOS

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-UAT-12`
**Nivel y Tipología:** Prueba de Aceptación de Usuario (UAT) / Simulacro de Emergencia Minera.
**Requerimiento Trazado:** Ensayo adicional de ingeniería; no sustituye controles contractuales.
**Precondiciones:** Simulacro programado de emergencia química con la mutualidad y Bomberos en Antofagasta.
**Pasos de Ejecución:**
- Chofer simula incidente de tránsito en faena minera y presiona el botón SOS de cabina.
- En paralelo, reporta vía PWA evento de derrame menor con código de producto químico.
- Cronometrar el despliegue del protocolo de emergencia en la Torre 24x7.
- El sistema presenta de inmediato la Ficha de Intervención Rápida de Emergencia (FIRE) con teléfonos de Carabineros, SAMU, Bomberos y teléfonos de emergencia del fabricante químico.

**Datos de Entrada Sintéticos:** Evento SOS en faena minera sintética en Antofagasta.
**Resultado Esperado:** Se debe verificar que despliega la ficha de emergencia en $\le 15\text{ s}$ con datos precisos. Los tiempos, porcentajes y magnitudes observados se registrarán después del ensayo; no se anticipan mediciones ni actas suscritas.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P1 (Bloqueante)**.
**Entorno:** Terreno / Terminal Antofagasta.

#### 9.0.8.13 CP-UAT-13 — Monitoreo térmico Bluetooth de semirremolque refrigerado

Este ensayo define entradas, controles y evidencia; no declara resultados ejecutados.

**ID:** `CP-UAT-13`
**Nivel y Tipología:** Prueba UAT / Cadena de frío.
**Requerimiento Trazado:** Ensayo adicional de ingeniería; no sustituye controles contractuales.
**Precondiciones:** Terminal Puerto Montt, semirremolque de prueba con baliza T-11 e iWave G26I. Rango requerido de la carga íntegramente dentro del rango homologado del sensor; permisos de ruta y patrón independiente disponibles.
**Pasos de Ejecución:**
- Vincular baliza y semirremolque y comprobar identidad y ubicación de medida.
- Configurar consigna, rango y cadencia aprobados; medir en terminal y ruta autorizada.
- Provocar pérdida controlada de Bluetooth y reconexión, conservando fechas y señalando dato no disponible.
- Conciliar lecturas con patrón y registros de torre, sin imputar temperatura de pulpa a una medida ambiental.

**Datos de Entrada Sintéticos:** Perfil de temperatura y carga de ensayo dentro del rango homologado, sin mercancía real expuesta.
**Resultado Esperado:** Trazabilidad de identidad, temperatura, fecha y calidad; error y cadencia dentro de los límites aprobados. No se declara funcionamiento a −30 °C ni cobertura térmica inferior al mínimo documentado; cualquier incompatibilidad de aplicación impide aceptación.
**Pass/Fail y Severidad:** Pass solo si se cumplen todos los criterios y se conserva evidencia reproducible; cualquier pérdida, acceso no autorizado o salida incorrecta implica Fail. Severidad alta para seguridad y evidencia.
**Entorno:** Terminal Puerto Montt / Ruta autorizada y HIL térmico.

#### 9.0.8.14 CP-UAT-14 — UAT Terminal Puerto Montt — Alerta Inmediata de Desviación Térmica ($\pm 1{,}5\text{ }^\circ\text{C}$)

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-UAT-14`
**Nivel y Tipología:** Prueba de Aceptación de Usuario (UAT) / Alerta Temprana de Pérdida de Frío.
**Requerimiento Trazado:** Ensayo adicional de ingeniería; no sustituye controles contractuales.
**Precondiciones:** Rampla reefer en patio Puerto Montt. Se simula intencionalmente la apertura de puertas traseras sin apagar el equipo frigorífico.
**Pasos de Ejecución:**
- Abrir puertas de la rampla reefer cargada.
- La temperatura en la baliza Bluetooth vinculada al semirremolque sube de $-19{,}0\text{ }^\circ\text{C} a -16{,}5\text{ }^\circ\text{C}$ en 8 minutos (desviación $> 1{,}5\text{ }^\circ\text{C}$ respecto a la consigna de $-18\text{ }^\circ\text{C}$).
- Verificar el tiempo de disparo de la alerta en el teléfono del chofer y en la consola del despachador de Puerto Montt.
- Cerrar puertas y verificar retorno a la temperatura nominal y cierre del evento de alarma.

**Datos de Entrada Sintéticos:** Apertura física de puertas en patio de pruebas de Puerto Montt.
**Resultado Esperado:** Se debe verificar que alerta en $< 60\text{ segundos}$ previniendo la descongelación. Los tiempos, porcentajes y magnitudes observados se registrarán después del ensayo; no se anticipan mediciones ni actas suscritas.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P1 (Bloqueante)**.
**Entorno:** Terreno / Patio Terminal Puerto Montt.

#### 9.0.8.15 CP-UAT-15 — UAT Terminal Puerto Montt — e-POD y Cierre de Viaje en Planta Procesadora Acuícola

Este ensayo comprueba el comportamiento descrito mediante entradas sintéticas y el criterio siguiente.

**ID:** `CP-UAT-15`
**Nivel y Tipología:** Prueba de Aceptación de Usuario (UAT) / Entrega Conforme y Cierre de Ciclo en Cliente.
**Requerimiento Trazado:** RF-012.
**Precondiciones:** Chofer arribando a planta procesadora de salmónidos en Chinquihue (Puerto Montt) en zona de baja conectividad costera.
**Pasos de Ejecución:**
- Descargar la carga en andén frigorífico del cliente.
- Encargado de recepción de la planta acuícola ingresa en la PWA del chofer su RUT y firma en cristal la recepción conforme de las 24 toneladas.
- Chofer fotografía el sello térmico y el documento de recepción físico de la planta.
- La PWA almacena localmente el e-POD en SQLite y lo sincroniza tan pronto el camión toma cobertura al salir del camino costero.
- Verificar que el viaje pase a estado `COMPLETED` en la Torre de San Bernardo.

**Datos de Entrada Sintéticos:** Cierre de viaje real/simulado en Chinquihue, firma en cristal y dos fotos de control.
**Resultado Esperado:** Se debe verificar que el e-POD opera en baja señal y sincroniza sin fallos. Los tiempos, porcentajes y magnitudes observados se registrarán después del ensayo; no se anticipan mediciones ni actas suscritas.
**Pass/Fail y Severidad:** Pass únicamente si se cumplen todas las salidas y límites del Resultado Esperado, las variantes y los criterios contractuales aplicables; cualquier discrepancia es Fail. No se admite una zona sin veredicto entre dos umbrales. Severidad: **P1 (Bloqueante)**.
**Entorno:** Terreno / Planta Acuícola Chinquihue (Puerto Montt).
