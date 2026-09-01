# Consultas al CLIENTE — D3

**Marcel V. y Martín V. · Arquitectura lógica y datos**
Empresa proponente: **AUDIT** · Cierre oficial del período: **01-09-2026**

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
| 1 | Técnica | Bases Técnicas Transversales, sección 5.4, pág. 13 (RT-05.29); Bases Técnicas Caso 10, Capítulos 14.2 y 15, págs. 30 y 31 | El requisito RT-05.29 establece que la latencia máxima entre la ocurrencia de una transacción y su disponibilidad en la capa analítica será la que fije el caso y, en su defecto, no superará las cuatro horas. El caso no fija un valor explícito para esta latencia, pero establece que el dispositivo a bordo debe operar 72 horas sin cobertura y que la reconexión de cientos de unidades será simultánea (numeral 14.2). Durante esas 72 horas la transacción existe en el dispositivo y no en el sistema central. Sírvase precisar si la latencia de cuatro horas se mide desde la ocurrencia de la transacción en el dispositivo o desde su llegada efectiva al sistema central tras la reconexión. | Se entiende que la latencia de cuatro horas se medirá desde la recepción de los datos en el sistema central. Durante la operación desconectada, los tableros indicarán explícitamente la cobertura y antigüedad de la información disponible. |
| 2 | Técnica | Bases Técnicas Caso 10, Capítulos 7.3 y 18, págs. 15 y 41 (criterio de aceptación 17) | El criterio de aceptación 17 establece que el costo por viaje estará disponible dentro de las 24 horas de cerrado el viaje. El Capítulo 7.3 registra que el consumo de combustible de la red de estaciones de servicio llega con hasta 40 días de desfase, los peajes se liquidan mensualmente y los neumáticos se controlan en planilla. Sírvase precisar si el criterio 17 admite un costo preliminar calculado con los componentes disponibles al cierre y una declaración explícita de los pendientes, o si exige el costo completo y definitivo dentro de ese plazo. | Se entiende que el criterio se satisface con un costo preliminar trazable, calculado con los componentes disponibles al cierre del viaje, que se actualiza automáticamente a medida que cada componente llega, manteniendo el historial de versiones y la fecha de cada actualización. |

### Prioridad alta

| N.º | Tipo | Referencia | Consulta | Propuesta de interpretación |
|---:|---|---|---|---|
| 3 | Técnica | Bases Técnicas Caso 10, Capítulos 14.2 y 18, págs. 30 y 41; Bases Técnicas Transversales, sección 5.1, pág. 11 (RT-05.07) | La sección 14.2 incluye el «volumen de almacenamiento de la evidencia de jornada por el plazo de retención exigido» como dimensión que el PROPONENTE debe estimar, lo que presupone un plazo definido. El criterio de aceptación 4 exige que esa evidencia resista una alegación de manipulación y sea oponible ante la autoridad, el cliente y el seguro. Sin embargo, el caso no especifica el plazo de retención para la evidencia de jornada, a diferencia de los datos de posición y telemetría, para los cuales indica dos años en línea con política de agregación. Sírvase indicar el plazo de retención exigido para la evidencia de jornada, o confirmar que el PROPONENTE debe derivarlo de la normativa laboral aplicable y del plazo contractual. | Se aplicará el mayor entre el plazo de prescripción de las acciones laborales del régimen especial de jornada del transporte de carga y el plazo contractual de 56 meses, con la evidencia conservada a su granularidad original durante todo el período. |
| 4 | Técnica | Bases Técnicas Caso 10, Capítulos 5 y 7.3, págs. 12 y 15; Anexo A, pág. 45; Bases Técnicas Transversales, sección 5.3, pág. 12 (RT-05.21) | El requisito RT-05.21 exige declarar, por cada integración, el modo, el volumen esperado, la ventana de disponibilidad y el comportamiento ante indisponibilidad del sistema contraparte. El Capítulo 5 y el Anexo A identifican el portal de la red de estaciones de servicio y el sistema del dispositivo de peaje como integraciones a mantener. Respecto de estos dos sistemas, sírvase indicar si disponen de interfaz de programación, exportación de archivos u otro mecanismo de obtención de datos, el formato en que los datos se entregan, la frecuencia con que están disponibles y si existe posibilidad de acceso anticipado respecto de la liquidación mensual actual. | De no existir antecedentes adicionales, se asumirá integración por archivo con periodicidad mensual para ambos sistemas, con el desfase actual de hasta 40 días para combustible, y se diseñará la capa de integración para soportar una eventual migración a acceso anticipado si alguno de los proveedores lo habilita en el futuro. |

## Consultas de reserva

Se incorporan solo si el equipo concluye que no están resueltas por las bases ni por
el propio levantamiento.

| N.º | Tipo | Referencia | Consulta | Por qué queda en reserva |
|---|---|---|---|---|
| R1 | Técnica | Caso 10, Caps. 5 y 15 | Marca, modelo y estándar de los tacógrafos digitales instalados en la flota, y si la descarga requiere presencia física o admite extracción remota. | D2 ya preguntó por interfaces y acceso a la telemetría de fábrica (consulta 7); la respuesta podría cubrir también los tacógrafos. |
| R2 | Técnica | Caso 10, Caps. 12 y 15 | Existencia de interfaces digitales con la autoridad aduanera chilena o argentina para la documentación de los cruces fronterizos. | Puede levantarse durante la Etapa 1 investigando directamente los sistemas públicos. |
| R3 | Técnica | Caso 10, Caps. 5 y 7.3 | Si la red de estaciones de servicio o el operador de peaje tienen en su hoja de ruta ofrecer acceso a datos con frecuencia superior a la mensual. | Condiciona el diseño futuro pero no el diseño base; la respuesta puede obtenerse en la etapa de integración. |

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
| Qué agregar de los datos de posición después de dos años | Cap. 15 | El caso dice «política de agregación declarada por el PROPONENTE» |
| Cómo construir el linaje desde el indicador hasta la fuente | RT-05.10 | Requisito deseable; el PROPONENTE propone el alcance |
| Qué motor de base de datos o qué tecnología de mensajería usar | T-7, subdoc. 4 | La tecnología es decisión del PROPONENTE con justificación |

## Verificación antes de cruzar con D2

- [x] Empresa escrita como **AUDIT**.
- [x] Columna Tipo restringida a `Administrativa`, `Técnica` o `Anexo`.
- [x] Una sola materia concreta por fila.
- [x] Ninguna consulta pide al CLIENTE diseñar la solución.
- [x] Páginas verificadas contra el índice del corpus.
- [x] No se duplican las consultas 4, 5, 7, 8 ni 9 de D2.
- [ ] Coordinar con D2: la consulta 4 de D3 complementa la consulta 8 de D2 (ambas
      tocan integración de fuentes de costo).
- [ ] Revisar y acordar cada propuesta de interpretación con Marcel.
- [ ] Confirmar la numeración final al consolidar con las demás duplas.
