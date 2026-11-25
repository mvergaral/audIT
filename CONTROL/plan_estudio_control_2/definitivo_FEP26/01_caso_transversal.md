# Caso transversal: licitación SaludConecta

Usaremos una sola empresa ficticia para conectar toda la materia.

## 1. Contexto

La empresa oferente **NexoSalud SpA** prepara una propuesta técnico-económica para **Red Salud Austral**, el mandante. El proyecto **SaludConecta** construirá y operará una plataforma de atención remota.

El sistema permitirá:

- registrar pacientes;
- reservar horas;
- realizar videoconsultas;
- emitir recetas;
- consultar resultados de laboratorio;
- integrar una pasarela de pagos;
- enviar notificaciones;
- generar reportes administrativos.

## 2. Restricciones del proyecto

- Plazo contractual: 8 meses.
- Equipo inicial: 6 personas.
- Presupuesto: $180.000.000.
- Primera etapa: portal web y aplicación administrativa.
- Se requiere migrar 120.000 registros de pacientes.
- El proveedor del laboratorio aún no entrega documentación completa de su API.
- El cliente exige criterios de calidad medibles y aceptación por entregable.
- El contrato será a precio fijo y tendrá multas por atraso e incumplimiento de SLA.
- El mandante exige operación durante 24 meses después de la implantación.
- Parte de la solución se instalará en una sala de servidores existente con seis racks; se debe decidir qué queda local y qué va a nube.
- Se exige disponibilidad de 99,5 %, RTO de 4 horas y RPO de 1 hora.
- NexoSalud puede construir componentes, comprar licencias o contratar servicios administrados.

## 3. Por qué este caso sirve para todo el curso

### Alcance

Hay que decidir qué queda dentro de la primera etapa y qué se posterga. Si “integración con cualquier laboratorio” queda sin límite, el alcance es peligroso.

### EDT/WBS

El trabajo debe descomponerse en entregables: requisitos, arquitectura, portal, agenda, integración, migración, pruebas, capacitación y puesta en marcha.

### Cronograma

La migración y la integración tienen dependencias externas. Hay que identificar ruta crítica, holguras y alternativas de compresión.

### Estimación

Los casos de uso, actores y factores técnicos/ambientales permiten estimar UCP, horas y capacidad del equipo.

### Riesgos

Hay riesgos de requisitos, integración, calidad de datos, proveedor, disponibilidad del cliente y adopción.

### Calidad

Se requieren métricas, pruebas, auditorías y criterios de aceptación. No basta con prometer que el sistema será “rápido y seguro”.

### Arquitectura

Hay que elegir estilo lógico, integraciones, despliegue físico, identidad, continuidad y ambientes. La decisión debe equilibrar calidad, costo y riesgo.

### Sala de servidores

La oferta debe declarar potencia, racks, energía de respaldo, climatización, acceso, conectividad, PUE esperado y límites de responsabilidad.

### Adquisiciones y contratos

Cada decisión de hacer, comprar o arrendar cambia CAPEX/OPEX, dependencia del proveedor, plazo, TCO y exposición contractual.

## 4. Regla de decisión

Durante el estudio, no preguntes solo “¿qué dice PMBOK?”. Pregunta también:

> ¿Qué decisión tomaría NexoSalud para ganar sin prometer una solución que no puede construir, operar ni financiar?

## 5. Conceptos que no debes confundir

| Concepto A | Concepto B | Diferencia |
|---|---|---|
| Alcance del producto | Alcance del proyecto | Características versus trabajo necesario |
| EDT/WBS | Cronograma | Descomposición del alcance versus secuencia temporal |
| Esfuerzo | Duración | Horas-persona versus tiempo calendario |
| Validar alcance | Controlar calidad | Aceptación del cliente versus verificación técnica |
| Riesgo | Problema | Evento futuro incierto versus hecho ocurrido |
| Calidad | Grado | Cumplimiento de requisitos versus cantidad de prestaciones |
| Prevención | Inspección | Evitar defectos versus detectarlos |
| Costo | Precio | Lo que gasta la empresa versus lo que cobra |
| Disponibilidad | Continuidad | Porcentaje operativo versus capacidad de recuperarse |
| Hacer | Comprar/arrendar | Control interno versus dependencia y servicio externo |

## 6. Regla del caso

Toda decisión debe dejar rastro:

```text
Requisito → diseño → EDT → estimación → riesgo → prueba → cláusula/precio
```

Si un componente no puede justificarse mediante esa cadena, probablemente sobra; si un requisito no llega a una prueba y un costo, probablemente falta trabajo.

