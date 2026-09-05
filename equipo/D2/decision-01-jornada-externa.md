# D-01: acreditación de jornada de conductores externos

Estado: propuesta de Ignacio C. para revisión de Matías y coordinación con D3/D4.
No constituye acuerdo del CLIENTE ni dictamen jurídico.

## Problema y requisitos de origen

La jornada previa puede incluir conducción para otros clientes. El dato del vehículo
actual no demuestra por sí solo la jornada de la persona ni sus descansos previos.
No disponer de información tampoco equivale a jornada cero.

Fuentes verificadas:

- FEP03, sección 16.1, decisión 1, p.34: resolver obtención y acreditación de jornada externa.
- FEP03, capítulo 18, criterios 1 a 4, p.41: bloqueo, cobertura de conductores,
  jornada previa disponible y evidencia resistente a manipulación.
- FEP03, capítulo 15, RT-09.01: asignación con verificación en no más de 30 segundos.
- FEP03, capítulo 15, RT-12.11: identificación sin manipulación en marcha ni dependencia
  de recordar una credencial.
- FEP03, capítulo 15, RT-16.14: firma electrónica de jornada en modalidad admitida.
- FEP03, capítulo 15, RT-05.10: conservar jornada y evidencia al menos cinco años.
- FEP03, capítulo 15, RT-11.10 y RT-16.09: cifrado de campo y registro de accesos sensibles.
- FEP03, capítulo 15, RT-03.10 y RT-03.13: registro local 72 horas y sincronización
  en hasta 20 minutos por camión, con reconexión masiva.

## Alternativas

| Alternativa | Ventaja | Limitación | Evaluación propuesta |
|---|---|---|---|
| Declaración del conductor como única fuente | Puede recogerse sin integración | Firmar no demuestra que el historial sea completo ni verdadero | No aceptarla automáticamente como acreditación suficiente |
| Tacógrafo como única fuente | Evidencia operacional contrastable | Puede faltar identificación personal o historial de otros vehículos | No usarlo como fuente única universal |
| Integración exclusiva con el empleador | Reduce transcripción y permite obtener registros | Depende de contratos, sistemas e interfaces aún desconocidos | Vía preferente donde esté disponible, no dependencia universal |
| Expediente por conductor con varias fuentes y evaluación previa | Reconcilia historial, autoría y discrepancias | Requiere reglas de suficiencia, revisión y mayor esfuerzo de enrolamiento | Recomendada para el borrador |

## Recomendación

Construir un expediente de jornada por persona, no solamente por camión. Recoger
registros autorizados del transportista, declaración firmada del conductor y datos de
tacógrafo cuando estén disponibles. La declaración complementa la evidencia: su sola
existencia no habilita el despacho.

Antes de asignar, evaluar identidad, cobertura temporal, procedencia, vigencia del
expediente y coherencia entre fuentes. El motor no elegirá silenciosamente la fuente
que entregue más jornada disponible. Una contradicción relevante requiere resolución
documentada antes de habilitar el viaje.

La suficiencia probatoria, periodos de cómputo, reglas de descanso y modalidad de firma
deben validarse jurídicamente. No se fijan aquí horas legales por inferencia ni se
declara aprobada una tecnología de registro ante la autoridad.

## Flujo propuesto

1. Matías incorpora al acuerdo de adhesión las obligaciones de entrega de registros,
   autorizaciones de acceso, corrección y responsabilidades, sin órdenes laborales
   a conductores externos. La base jurídica del tratamiento debe revisarse por dato.
2. Enrolar al conductor con identidad comprobada y asociarlo al transportista y viaje.
   D4 propone el medio de identificación; no se exige teléfono personal ni recordar
   una contraseña para iniciar el viaje.
3. Obtener antes de la asignación el historial requerido para el cómputo aplicable.
   Conservar intervalos de actividad/descanso, fuente, fecha de obtención, identidad,
   firma admitida, respaldo original y versiones. No pedir datos comerciales ajenos
   que no sean necesarios para acreditar jornada.
4. Detectar huecos, solapamientos, cambio de conductor, alteraciones y reloj dudoso.
   Preparar el expediente antes del despacho para no depender de una API externa
   durante la transacción crítica de 30 segundos.
5. Al asignar, comprobar que el expediente sigue vigente y que el viaje es compatible
   con jornada y descanso. Registrar resultado, versión de reglas, evidencias usadas
   y motivo del bloqueo o autorización.
6. Durante el viaje, registrar automáticamente eventos y mantener alertas locales sin
   cobertura. No confundir el funcionamiento offline con conocimiento actualizado de
   actividad realizada en otros vehículos.
7. Corregir mediante nuevos eventos vinculados al original, nunca sobrescribiendo el
   historial. Si una corrección invalida una asignación activa, activar revisión y
   contingencia operacional segura; no exigir interacción del conductor en marcha.

## Estados y contingencias

| Estado | Tratamiento antes del despacho | Recuperación |
|---|---|---|
| Evidencia suficiente y jornada disponible | Permitir tras verificar las demás condiciones | Registrar evidencia y decisión |
| Jornada insuficiente | Bloquear | Reprogramar o asignar conductor habilitado con jornada acreditada |
| Fuente ausente, desactualizada o incompleta | Bloquear por jornada no acreditada | Obtener evidencia admisible y recalcular |
| Fuentes contradictorias | Bloquear y abrir revisión | Resolver con respaldo y corrección trazable |
| Proveedor de datos caído | Usar expediente local solo si cumple vigencia y suficiencia validadas | Si no cumple, bloquear; no asumir jornada cero |
| Tercero no adherido | No prometer acceso a sus datos | Evaluar vía documental legalmente admitida; sin evidencia suficiente no despachar |
| Reconexión tardía o duplicados | Preservar originales e identificar eventos únicos | Reconciliar sin doble cómputo y auditar conflictos |

Un jefe de turno no puede convertir la falta de acreditación o la jornada insuficiente
en un permiso mediante override. D-06 debe respetar este límite.

## Riesgos y tratamiento

| Riesgo | Tratamiento propuesto | Validación pendiente |
|---|---|---|
| Declaración falsa o incompleta | Contraste de fuentes y revisión de inconsistencias | Suficiencia y valor probatorio |
| Identidad equivocada al rotar camiones | Asociación explícita conductor-vehículo-viaje | Medio de identificación y prueba real |
| Falta de adhesión | Incentivos y alternativas documentales admisibles | D-02/D-05, costo y aceptación |
| Exposición de jornada de terceros | Minimización, cifrado de campo, permisos y auditoría | Base jurídica y retención |
| Cola de revisiones detiene la operación | Preparación anticipada y medición de carga operacional | Capacidad de torre, costo y roles |
| Desfase offline produce datos incompletos | Vigencia explícita y bloqueo ante incertidumbre | Reglas de conciliación D3 y capacidad de borde D4 |

No se cuantifican probabilidades sin datos del piloto. Los costos de integración,
firma, enrolamiento y revisión deberán incorporarse al modelo económico.

## Pruebas para aceptar el diseño

- [ ] Historial de otro cliente incluido sin revelar información comercial innecesaria.
- [ ] Declaración sola, hueco temporal o identidad dudosa no habilitan automáticamente.
- [ ] Jornada insuficiente y discrepancia relevante bloquean sin override operacional.
- [ ] Asignación resuelta en hasta 30 segundos en la carga acordada, incluida caída de fuente externa.
- [ ] Cambios de vehículo y correcciones no duplican ni borran actividad.
- [ ] Ensayo de 72 horas sin cobertura y sincronización en hasta 20 minutos por camión.
- [ ] Firma, autoría, retención y accesos cumplen el diseño jurídicamente validado.
- [ ] Revisión ejecutable por los roles acordados, con carga y costos medidos.

## Verificado

| Grupo | Qué debe verificar | Estado | Persona, fecha y evidencia |
|---|---|---|---|
| D1 | Coherencia con problema, actores y fuentes del caso | Pendiente | Sin registrar |
| D2: Ignacio y Matías | Alternativa elegida, adhesión, contingencias y alcance | Pendiente | Sin registrar |
| D3 | Modelo por persona, conciliación, reglas, auditoría y desempeño | Pendiente | Sin registrar |
| D4 | Identificación, registro local y sincronización | Pendiente | Sin registrar |
| Revisión jurídica por coordinar | Régimen de jornada, firma, suficiencia probatoria y tratamiento de datos | Pendiente | Sin registrar |

Impacta RF-001 a RF-004, RF-007, RF-026 a RF-028 y RNF-001, RNF-002,
RNF-003, RNF-012, RNF-013 y RNF-014. No se cierra D-01 hasta registrar las
validaciones necesarias; documentar esta propuesta no equivale a ratificarla.
