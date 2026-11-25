# PMBOK 06 — Gestión del cronograma

## 1. La pregunta que responde este capítulo

El alcance dice **qué trabajo hay que realizar**. El cronograma transforma ese trabajo en una secuencia temporal y responde:

> ¿Qué actividades debemos ejecutar, en qué orden, cuánto durarán, con qué restricciones y cuándo terminará el proyecto?

Un cronograma no es solo una lista de fechas. Es un **modelo** que relaciona actividades, dependencias, duraciones, recursos, calendarios y restricciones. Por eso, cambiar una actividad puede desplazar muchas fechas posteriores.

En SaludConecta, la EDT contiene el entregable “Integración con laboratorio”. El cronograma debe descomponerlo en actividades como definir contrato de la API, desarrollar conector, preparar datos de prueba, ejecutar pruebas y corregir defectos.

---

## 2. Los seis procesos del capítulo 6

| Proceso | Pregunta práctica | Resultado principal |
|---|---|---|
| 6.1 Planificar la gestión del cronograma | ¿Cómo construiremos y controlaremos el cronograma? | Plan de gestión del cronograma |
| 6.2 Definir las actividades | ¿Qué acciones concretas producen los entregables? | Lista de actividades, atributos e hitos |
| 6.3 Secuenciar las actividades | ¿Qué debe ocurrir antes o después? | Diagrama de red y dependencias |
| 6.4 Estimar la duración de las actividades | ¿Cuánto tiempo requiere cada actividad? | Estimaciones y bases de estimación |
| 6.5 Desarrollar el cronograma | ¿Qué fechas resultan al integrar todo? | Línea base y cronograma del proyecto |
| 6.6 Controlar el cronograma | ¿Estamos cumpliendo y cómo tratamos las desviaciones? | Pronósticos, información y solicitudes de cambio |

La lógica completa es:

```text
EDT → actividades → dependencias → duraciones → modelo de cronograma → línea base → control
```

---

## 3. Planificar la gestión del cronograma

Antes de calcular fechas, el equipo acuerda las reglas. El plan puede especificar:

- método de programación y herramienta;
- unidades de medida: horas, días o semanas;
- calendarios laborales y períodos de actualización;
- nivel de precisión esperado;
- umbrales de control;
- reglas para medir avance;
- formatos de informes;
- forma de gestionar cambios a la línea base.

### ¿Por qué conviene definir esto primero?

Supón que una persona informa que una tarea está “al 80 %”. ¿Significa que gastó el 80 % de las horas, que completó 8 de 10 módulos o que cree que le falta poco? Sin una regla común, el porcentaje no es comparable ni verificable.

Un buen criterio sería medir avance mediante entregables terminados: “8 de 10 casos de prueba aprobados”, no mediante una percepción subjetiva.

---

## 4. Definir las actividades

La EDT representa **entregables y alcance**; las actividades representan **acciones necesarias para producirlos**.

Ejemplo:

| Elemento de la EDT | Actividades posibles |
|---|---|
| 1.3 Integración con laboratorio | Definir contrato API, programar conector, configurar ambiente, probar respuestas, corregir defectos |

### Técnica de descomposición

Se toma un paquete de trabajo y se lo divide hasta obtener actividades que puedan:

- estimarse;
- asignarse;
- secuenciarse;
- medirse y controlarse.

No hay una duración universal para una actividad. Debe tener el detalle suficiente para gestionarla, sin convertir el cronograma en miles de microtareas administrativas.

### Planificación gradual u “onda progresiva”

El trabajo cercano se planifica en detalle y el trabajo lejano queda a mayor nivel hasta disponer de más información.

Es mejor que inventar detalles prematuramente cuando existe incertidumbre. Por ejemplo, se puede planificar en detalle la primera integración y dejar las integraciones del segundo semestre como paquetes de planificación.

### Hitos

Un hito representa un punto significativo y normalmente tiene duración cero:

- alcance aprobado;
- versión candidata liberada;
- certificación obtenida;
- aceptación del cliente.

Un hito no es trabajo; señala que algo relevante ocurrió.

### Salidas importantes

- **Lista de actividades:** todas las actividades requeridas.
- **Atributos de las actividades:** identificador, descripción, predecesoras, sucesoras, restricciones, responsables y otros datos.
- **Lista de hitos:** eventos obligatorios u opcionales.

---

## 5. Secuenciar las actividades

Secuenciar consiste en identificar y documentar las relaciones entre actividades.

### Método de diagramación por precedencia

Las cuatro relaciones lógicas son:

| Relación | Significado | Ejemplo |
|---|---|---|
| Fin a inicio, FS | B comienza cuando A termina | Programar después de aprobar el diseño |
| Inicio a inicio, SS | B comienza cuando A comienza | Documentar en paralelo al desarrollo |
| Fin a fin, FF | B termina cuando A termina | Terminar revisión junto con la redacción |
| Inicio a fin, SF | B termina cuando A comienza | El turno antiguo termina cuando inicia el nuevo |

**FS** es la relación más frecuente. **SF** existe, pero es poco habitual; no debe elegirse solo para demostrar que se conoce.

### Tipos de dependencias

| Tipo | Qué la origina | Ejemplo |
|---|---|---|
| Obligatoria | Naturaleza física o contractual | No probar un módulo antes de construirlo |
| Discrecional | Preferencia o práctica del equipo | Diseñar primero todas las pantallas |
| Externa | Parte ajena al proyecto | Esperar autorización del regulador |
| Interna | Relación bajo control del proyecto | Aprobar diseño antes de programar |

Una dependencia discrecional puede revisarse para comprimir el cronograma. Una obligación física o externa suele ofrecer menos flexibilidad.

### Adelantos y retrasos

- **Adelanto (lead):** permite iniciar antes la actividad sucesora. Ejemplo: comenzar pruebas parciales dos días antes de terminar todo el desarrollo.
- **Retraso (lag):** impone una espera. Ejemplo: esperar 24 horas después de migrar datos antes de validar la sincronización.

No se deben usar adelantos para esconder una dependencia que en realidad no ha sido analizada.

---

## 6. Estimar la duración de las actividades

### Duración no es lo mismo que esfuerzo

- **Esfuerzo:** trabajo humano requerido, por ejemplo 80 horas-persona.
- **Duración:** tiempo calendario necesario, por ejemplo 10 días laborales.

Dos personas no siempre reducen una tarea a la mitad: pueden necesitar coordinación, trabajar sobre el mismo componente o depender de un recurso indivisible.

### Técnicas y cuándo conviene usarlas

| Técnica | Cuándo conviene | Ventaja | Riesgo o limitación |
|---|---|---|---|
| Juicio de expertos | Hay experiencia específica | Rápido y contextual | Sesgos y optimismo |
| Análoga | Etapa temprana y proyecto similar | Poco costosa | Menor precisión |
| Paramétrica | Existe relación medible y datos confiables | Repetible y transparente | El parámetro puede no representar el caso |
| Tres valores | Hay incertidumbre relevante | Hace visible el rango | Depende de la calidad de O, M y P |
| Ascendente | Hay EDT y actividades detalladas | Mayor trazabilidad | Requiere más tiempo |
| Análisis de reserva | Se reconocen incertidumbres | Protege el compromiso | Inflar todas las tareas oculta la reserva |

### Estimación de tres valores

Sean:

- `O`: optimista;
- `M`: más probable;
- `P`: pesimista.

Distribución triangular:

```text
Duración esperada = (O + M + P) / 3
```

Distribución beta o PERT:

```text
Duración esperada = (O + 4M + P) / 6
Desviación estándar aproximada = (P - O) / 6
```

Ejemplo: O = 4, M = 6 y P = 14 días.

- triangular: `(4 + 6 + 14) / 3 = 8 días`;
- beta: `(4 + 4×6 + 14) / 6 = 7 días`;
- desviación aproximada: `(14 - 4) / 6 = 1,67 días`.

PERT da más peso al valor más probable. No significa que siete días estén garantizados; sigue siendo una estimación.

### Reservas

- **Reserva de contingencia:** cubre riesgos identificados y forma parte de la línea base del cronograma.
- **Reserva de gestión:** cubre trabajo imprevisto dentro del alcance global y está fuera de la línea base, aunque dentro del requisito total del proyecto.

---

## 7. Desarrollar el cronograma

Se integran actividades, dependencias, duraciones, recursos, calendarios y restricciones para obtener fechas viables.

### Método de la ruta crítica

La ruta crítica es la secuencia de actividades que determina la duración mínima del proyecto. Habitualmente posee holgura total cero.

Conceptos:

- **Inicio temprano (ES)** y **fin temprano (EF):** primeras fechas posibles.
- **Inicio tardío (LS)** y **fin tardío (LF):** últimas fechas posibles sin retrasar el proyecto.
- **Holgura total:** cuánto puede retrasarse una actividad sin retrasar la fecha final.

```text
Holgura total = LS - ES = LF - EF
```

### Ejemplo resuelto

| Actividad | Descripción | Duración | Predecesora |
|---|---|---:|---|
| A | Levantar requisitos | 3 | — |
| B | Diseñar arquitectura | 2 | A |
| C | Construir prototipo UX | 4 | A |
| D | Desarrollar backend | 5 | B |
| E | Desarrollar frontend | 4 | B y C |
| F | Integrar solución | 3 | D y E |
| G | Ejecutar aceptación | 2 | F |

Cálculo hacia adelante:

| Actividad | ES | EF |
|---|---:|---:|
| A | 0 | 3 |
| B | 3 | 5 |
| C | 3 | 7 |
| D | 5 | 10 |
| E | 7 | 11 |
| F | 11 | 14 |
| G | 14 | 16 |

La duración mínima es **16 días**. La ruta crítica es:

```text
A → C → E → F → G
```

B y D tienen un día de holgura. Si D se atrasa un día, no cambia la fecha final; si se atrasa dos, la retrasa. Si C se atrasa un día, el proyecto se atrasa un día, salvo que se adopte una medida correctiva.

> La ruta crítica puede cambiar durante el proyecto. No es una etiqueta permanente.

### Optimización de recursos

| Técnica | Qué hace | Efecto típico |
|---|---|---|
| Nivelación de recursos | Ajusta fechas porque los recursos están sobreasignados o limitados | Puede cambiar la ruta crítica y alargar el proyecto |
| Suavizamiento de recursos | Ajusta dentro de la holgura disponible | No debería cambiar la ruta crítica ni la fecha final |

Ejemplo: si la misma desarrolladora está asignada simultáneamente a C y D, el cronograma matemático no es ejecutable. La nivelación mueve una de las tareas, aunque aumente la duración.

### Compresión del cronograma

| Técnica | Qué hace | Costo/riesgo |
|---|---|---|
| Intensificación o crashing | Agrega recursos a actividades críticas | Sube el costo; no siempre mejora proporcionalmente |
| Ejecución rápida o fast tracking | Superpone trabajo antes secuencial | Aumenta retrabajo y riesgo |

Solo sirve comprimir actividades de la ruta crítica. Acortar una actividad con holgura puede no adelantar nada.

### Análisis de escenarios y simulación

- **¿Qué pasa si…?** evalúa huelgas, retrasos de proveedor, pérdida de personal u otras situaciones.
- **Monte Carlo** simula muchas combinaciones de duraciones para estimar probabilidades de terminar en determinadas fechas.

Una fecha con 50 % de probabilidad no tiene el mismo nivel de compromiso que una con 80 %.

### Salidas importantes

- **Línea base del cronograma:** versión aprobada para comparar desempeño.
- **Cronograma del proyecto:** puede mostrarse como barras, hitos o red.
- **Datos del cronograma:** supuestos, reservas, recursos, restricciones y detalles del modelo.
- **Calendarios del proyecto:** días y turnos de trabajo disponibles.

---

## 8. Controlar el cronograma

Controlar no significa obligar al equipo a cumplir fechas imposibles. Significa:

1. conocer el estado real;
2. comparar contra la línea base;
3. analizar variaciones y tendencias;
4. pronosticar resultados;
5. gestionar cambios aprobados.

Preguntas útiles:

- ¿Qué actividades críticas están retrasadas?
- ¿La holgura se está consumiendo?
- ¿La estimación restante sigue siendo válida?
- ¿Apareció una restricción nueva?
- ¿Conviene nivelar recursos, comprimir o solicitar un cambio?

Si cambia la línea base sin aprobación, se pierde la capacidad de saber si el proyecto tuvo una desviación. Primero se analiza y aprueba el cambio; después se actualiza la línea base.

---

## 9. Enfoque predictivo y enfoque adaptativo

En un proyecto predictivo se intenta construir una secuencia y línea base detalladas. En un enfoque adaptativo, el producto se desarrolla por iteraciones y el detalle de largo plazo es menor.

Eso no elimina la gestión del tiempo. Se siguen usando:

- cadencia de iteraciones;
- priorización del backlog;
- planificación de versiones;
- capacidad o velocidad del equipo;
- revisión y replanificación frecuentes.

La diferencia está en cuánto se compromete por adelantado y con qué frecuencia se recalcula.

---

## 10. Errores típicos de control

1. **Confundir EDT con cronograma.** La EDT contiene alcance; el cronograma agrega orden y tiempo.
2. **Sumar todas las duraciones.** Actividades paralelas no se suman linealmente.
3. **Confundir esfuerzo con duración.** 80 horas-persona no implican automáticamente 10 días.
4. **Llamar crítico a lo “importante”.** En CPM, crítico significa que afecta la fecha final por su holgura.
5. **Comprimir tareas no críticas.** Puede aumentar costo sin adelantar el proyecto.
6. **Nivelar sin recalcular.** La limitación de recursos puede crear una nueva ruta crítica.
7. **Actualizar la línea base para ocultar atrasos.** Una línea base solo cambia mediante control integrado de cambios.

---

## 11. Autoevaluación

Intenta responder sin mirar:

1. ¿Por qué la EDT debe existir antes de definir actividades?
2. Da un ejemplo de FS, SS y FF en SaludConecta.
3. ¿Qué diferencia existe entre adelanto y retraso?
4. ¿Cuándo preferirías una estimación análoga y cuándo una ascendente?
5. ¿Por qué dos personas no siempre reducen la duración a la mitad?
6. ¿Qué diferencia hay entre nivelación y suavizamiento?
7. ¿Cuándo usarías crashing y cuándo fast tracking?
8. ¿Por qué una actividad importante para el cliente puede no pertenecer a la ruta crítica?
9. ¿Qué ocurre con la fecha final si una actividad crítica se retrasa y no se toma acción?
10. ¿Por qué no debe cambiarse la línea base cada vez que el proyecto se desvía?

