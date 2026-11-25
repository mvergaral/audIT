# Caso transversal: SaludConecta

Usaremos una sola empresa ficticia para conectar toda la materia.

## 1. Contexto

La empresa **NovaTI** prepara una propuesta para desarrollar **SaludConecta**, una plataforma de atención remota para una red de centros médicos.

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

## 4. Regla de decisión

Durante el estudio, no preguntes solo “¿qué dice PMBOK?”. Pregunta también:

> ¿Qué decisión tomaría NovaTI para que SaludConecta pueda entregarse dentro del alcance, plazo, costo y calidad comprometidos?

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

