# Consultas al CLIENTE — D3, versión 3

**Marcel V. y Martín V. · Arquitectura lógica y datos**
Empresa proponente: **AUDIT** · Cierre oficial del período: **01-09-2026**

## Qué cambió respecto de la v2

| # | Cambio | Motivo |
|---|---|---|
| 1 | Consulta 1 (latencia RT-05.29) **eliminada** | El caso SÍ fija 5 latencias explícitas bajo RT-05.29 en el Capítulo 15 (p.31), incluido el calificativo «con cobertura» para posición, que resuelve el escenario desconectado. Detectado por Marcel tras revisión cruzada con el Gemini. |
| 2 | Consulta 2 **fortalecida** y renumerada a **1** | Se incorpora la referencia al parámetro RT-05.29 del Capítulo 15 (p.31), que califica el costo con «componentes disponibles a esa fecha e indicación de los pendientes», reforzando la contradicción con el criterio 17 (p.41) que no incluye esa calificación. |
| 3 | Consulta 4 (ahora **2**) se mantiene sin cambios | |

## Reglas aplicables — Artículo 43° (FEP01 · p.27)

- Por escrito, por el canal oficial, dentro del período del Formulario T-20.
- Concretas, precisas y pertinentes. No pueden pedir información confidencial ni que
  el CLIENTE diseñe la solución en lugar del PROPONENTE (43.4).
- Planilla con columnas A–G: correlativo, empresa, fecha, **tipo**, referencia,
  consulta, propuesta de interpretación.
- Tipo: **`Administrativa`, `Técnica` o `Anexo`**. Solo esos tres valores.
- Nomenclatura: `CONSULTAS_[EMPRESA]_AAAAMMDD.XLSX` (43.3).
- Las respuestas se publican sin identificar a quien preguntó, y pasan a integrar las
  Bases con la precedencia del Artículo 5°.

## Consultas para envío

### Prioridad crítica

| N.º | Tipo | Referencia | Consulta | Propuesta de interpretación |
|---:|---|---|---|---|
| 1 | Técnica | Bases Técnicas Caso 10: criterio de aceptación 17 (Cap. 18, pág. 41); parámetro RT-05.29 (Cap. 15, pág. 31); sección B.1 (Cap. B, pág. 46); sección 7.3 (Cap. 7, pág. 15) | El criterio de aceptación 17 (pág. 41) establece que el costo por viaje estará disponible dentro de las 24 horas de cerrado el viaje, sin calificación. El parámetro RT-05.29 del Capítulo 15 (pág. 31) establece, para el mismo dato, «no superior a 24 horas tras su cierre, con los componentes que a esa fecha estén disponibles y con indicación explícita de los que aún no lo están». La sección B.1 (pág. 46) reproduce la misma calificación. El Capítulo 7.3 registra que el consumo de combustible llega con hasta 40 días de desfase y los peajes se liquidan mensualmente. Dado que el criterio 17 y el parámetro RT-05.29 describen el mismo dato con distinto grado de calificación, sírvase precisar si el criterio 17 se satisface con un costo preliminar trazable que declare los componentes pendientes, conforme al parámetro RT-05.29 y a la sección B.1, o si exige el costo completo y definitivo. | Se entiende que el criterio 17 se satisface conforme a la calificación que el propio caso introduce en el parámetro RT-05.29 y en la sección B.1: un costo preliminar trazable con los componentes disponibles al cierre, que se actualiza automáticamente a medida que cada componente llega, con historial de versiones. |

### Prioridad alta

| N.º | Tipo | Referencia | Consulta | Propuesta de interpretación |
|---:|---|---|---|---|
| 2 | Técnica | Bases Técnicas Caso 10, Capítulos 5 y 7.3, págs. 12 y 15; Anexo A, pág. 45; Bases Técnicas Transversales, sección 5.3, pág. 12 (RT-05.21) | El requisito RT-05.21 exige declarar, por cada integración, el modo, el volumen esperado, la ventana de disponibilidad y el comportamiento ante indisponibilidad del sistema contraparte. El Capítulo 5 y el Anexo A identifican el portal de la red de estaciones de servicio y el sistema del dispositivo de peaje como integraciones a mantener. Respecto de estos dos sistemas, sírvase indicar si disponen de interfaz de programación, exportación de archivos u otro mecanismo de obtención de datos, el formato en que los datos se entregan, la frecuencia con que están disponibles y si existe posibilidad de acceso anticipado respecto de la liquidación mensual actual. | De no existir antecedentes adicionales, se asumirá integración por archivo con periodicidad mensual para ambos sistemas, con el desfase actual de hasta 40 días para combustible, y se diseñará la capa de integración para soportar una eventual migración a acceso anticipado si alguno de los proveedores lo habilita en el futuro. |

## Consultas de reserva

Se incorporan solo si el equipo concluye que no están resueltas por las bases ni por
el propio levantamiento.

| N.º | Tipo | Referencia | Consulta | Por qué queda en reserva |
|---|---|---|---|---|
| R1 | Técnica | Caso 10, Caps. 5 y 15 | Marca, modelo y estándar de los tacógrafos digitales instalados en la flota, y si la descarga requiere presencia física o admite extracción remota. | D2 ya preguntó por interfaces y acceso a la telemetría de fábrica (consulta 7); la respuesta podría cubrir también los tacógrafos. |
| R2 | Técnica | Caso 10, Caps. 12 y 15 | Existencia de interfaces digitales con la autoridad aduanera chilena o argentina para la documentación de los cruces fronterizos. | Puede levantarse durante la Etapa 1 investigando directamente los sistemas públicos. La sección 16.2 indica que el cruce fronterizo es materia de investigación del PROPONENTE. |
| R3 | Técnica | Caso 10, Caps. 5 y 7.3 | Si la red de estaciones de servicio o el operador de peaje tienen en su hoja de ruta ofrecer acceso a datos con frecuencia superior a la mensual. | Condiciona el diseño futuro pero no el diseño base; se complementa con la consulta 2. |

## Lo que no se pregunta al CLIENTE

Estas materias son trabajo profesional del PROPONENTE. Preguntarlas sería pedirle al
CLIENTE que diseñe la solución, y el Art. 43.4 lo excluye expresamente.

| Materia | Origen | Tratamiento interno |
|---|---|---|
| Qué paradigma de persistencia usar | RT-05.02 | El PROPONENTE lo justifica por dominio de datos |
| Cómo separar el almacenamiento transaccional del analítico | RT-05.05 | Decisión de arquitectura del PROPONENTE |
| Cómo manejar la reconexión simultánea de cientos de camiones | RT-09.02 | El PROPONENTE lo deriva de la volumetría y lo declara |
| Cómo resolver conflictos de sincronización tras operación desconectada | RT-03.12 | El PROPONENTE documenta la regla de reconciliación |
| Qué funciones estarán disponibles sin conexión y cuáles no | RT-03.13 | El PROPONENTE lo declara; su ausencia es observación grave |
| Qué frecuencia de muestreo adoptar para posición y telemetría | Decisión 11 | Balancear precisión, costo de datos y almacenamiento |
| Qué agregar de los datos de posición después de dos años | Cap. 15 (RT-05.10) | El caso dice «política de agregación declarada por el PROPONENTE» |
| Cómo construir el linaje desde el indicador hasta la fuente | RT-05.10 | Requisito deseable; el PROPONENTE propone el alcance |
| Qué motor de base de datos o qué tecnología de mensajería usar | T-7, subdoc. 4 | La tecnología es decisión del PROPONENTE con justificación |
| Cuánto retener la evidencia de jornada | Cap. 15 (RT-05.10) | Ya definido: mínimo 5 años conforme a la normativa laboral |
| Qué latencia analítica aplicar durante la operación desconectada | Cap. 15 (RT-05.29) | Ya definido: el caso califica «con cobertura» para posición; el dato llega tras la reconexión (RT-03.13, 20 min por camión) |

## Consultas descartadas durante la revisión

| Candidata | Por qué se descartó |
|---|---|
| Latencia de la capa analítica durante operación desconectada (RT-05.29) | El caso fija 5 latencias explícitas bajo RT-05.29 en el Capítulo 15 (p.31): posición «con cobertura» ≤ 2 min, jornada en tiempo real, tiempos de llegada en el momento del evento, costo ≤ 24 h con indicación de pendientes, emisiones mensual. El calificativo «con cobertura» distingue el escenario conectado del desconectado, y RT-03.13 fija 20 minutos de sincronización tras la reconexión. La premisa de la consulta era incorrecta. |
| Plazo de retención de la evidencia de jornada de conducción | El caso lo define en el Capítulo 15 bajo RT-05.10: «Registro de jornada de conducción y su evidencia: mínimo 5 años, conforme a la normativa laboral aplicable.» |
| Estándares sectoriales de intercambio (RT-05.23) | El caso los identifica en el Capítulo 15: el formato del documento electrónico de transporte. La sección 16.2 indica que la telemática y los protocolos son materia de investigación del PROPONENTE. |
| Firma electrónica durante operación desconectada (RT-16.14/17) | El caso indica «en la modalidad que la normativa admita para cada caso»; determinar esa modalidad es trabajo del PROPONENTE. |
| Interfaces del sistema de mantenimiento de 2017 | El caso dice «se mantiene o se reemplaza, con justificación». Si el PROPONENTE decide reemplazarlo, no hay integración. Si decide mantenerlo, puede evaluar las interfaces durante la Etapa 1. |
| Retención de registros de auditoría (RT-16.10) | El valor por defecto es 5 años si el caso no fija otro. Los plazos del Cap. 15 (5 a 10 años según dominio) dan orientación suficiente al PROPONENTE. |

## Verificación antes de cruzar con D2

- [x] Empresa escrita como **AUDIT**.
- [x] Columna Tipo restringida a `Administrativa`, `Técnica` o `Anexo`.
- [x] Una sola materia concreta por fila.
- [x] Ninguna consulta pide al CLIENTE diseñar la solución.
- [x] Páginas verificadas contra el índice del corpus.
- [x] No se duplican las consultas 4, 5, 7, 8 ni 9 de D2.
- [x] Verificada la retención de jornada — está definida en el Cap. 15 (5 años); se descartó la consulta.
- [x] Verificada la latencia analítica — el caso fija 5 valores bajo RT-05.29; se descartó la consulta (detectado por Marcel).
- [ ] Coordinar con D2: la consulta 2 de D3 complementa la consulta R3 de D2 (que quedó en reserva); ambas tocan integración de fuentes de costo.
- [ ] Revisar y acordar cada propuesta de interpretación con Marcel.
- [ ] Confirmar la numeración final al consolidar con las demás duplas.
