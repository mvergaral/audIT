# Ruta de estudio para el certamen

Guía basada en el aviso del profesor y los materiales de FEP26 disponibles en la carpeta del curso. La prioridad combina **puntaje**, **tipo de pregunta** y el hecho de que algunos temas requieren práctica escrita.

## Cómo usar esta guía

Para cada bloque sigue este ciclo:

1. Lee el significado de los conceptos y las siglas.
2. Tapa la explicación e intenta contar el tema con tus palabras.
3. Resuelve los ejercicios sin mirar la pauta.
4. Corrige errores y anota qué confusión los produjo.

En cualquier desarrollo escribe: **datos → qué se pide → fórmula o concepto → reemplazo → resultado con unidades → interpretación**. Conserva dos decimales durante los cálculos y redondea al final.

## Priorización del temario

| Orden | Tema | Preguntas | Puntaje | Prioridad de estudio |
|---:|---|---:|---:|---|
| 1 | Estimación de Software | 6 | 99 | Máxima: método UCP y conversión a esfuerzo |
| 2 | Requisitos, Alcance, Planificación y EDT | 6 | 72 | Máxima: conceptos + redes, Gantt y holguras |
| 3 | Arquitectura de Software y nube | 5 | 45 | Alta: justificar decisiones y consecuencias |
| 4 | Calidad | 4 | 45 | Alta: distinciones, costos y requisitos medibles |
| 5 | Trabajos de Investigación | 6 (se responden 5) | 45 | Alta: repasar exposiciones; omitir la propia |
| 6 | Sala de Servidores | 3 | 36 | Media-alta: fórmulas y dimensionamiento |
| 7 | Gestión de los Riesgos | 2 | 18 | Menor puntaje, pero conceptos y EMV son abordables |
| 8 | Lecturas PMBOK 5, 6, 8 y 11 | Refuerzan materias | No separado | Repasar definiciones y diferencias de procesos |

La suma indicada por materia llega a 360 puntos, considerando que de Investigación se contestan cinco preguntas. Si el tiempo es corto, no abandones los temas de 45 puntos: juntos pesan más que cualquiera de los bloques individuales.

---

# 1. Estimación de Software — 99 puntos

## Qué significa estimar

Estimar es producir una predicción razonada con información incompleta. El primer paso es saber **qué magnitud te piden**:

- **Tamaño:** cuánto producto/funcionalidad se estima; aquí, puntos UCP.
- **Esfuerzo:** trabajo humano; se expresa en horas-persona (HH).
- **Duración o plazo:** tiempo calendario.
- **Costo:** dinero, a partir del esfuerzo, tarifas y otros costos.

No son sinónimos: 1.000 HH no equivalen automáticamente a 1.000 horas calendario.

## UCP, explicado por el significado

UCP es *Use Case Points*, o **Puntos de Casos de Uso**. Cuenta las interacciones y funciones del sistema, las ajusta por dificultad y convierte el tamaño resultante en esfuerzo.

La historia que conviene memorizar:

> **Actores + funciones = tamaño inicial; técnica y ambiente lo ajustan; el factor de conversión lo pasa a horas.**

### Actores: UAW

UAW es *Unadjusted Actor Weight*: **peso no ajustado de actores**. Actor es una persona o sistema externo que interactúa con el sistema que estimamos.

Pregunta para clasificar: **¿quién interactúa y mediante qué tipo de interfaz?**

| Clase | Interacción típica | Peso |
|---|---|---:|
| Simple | Otro sistema por API definida | 1 |
| Medio | Sistema por protocolo o interacción textual | 2 |
| Complejo | Persona por interfaz gráfica | 3 |

`UAW = Σ(cantidad de actores × peso)`

El peso no es la importancia del usuario. Es una aproximación a la complejidad de su interacción.

### Casos de uso: UUCW

UUCW es *Unadjusted Use Case Weight*: **peso no ajustado de casos de uso**. Un caso de uso es una función/objetivo que el sistema ofrece a un actor. Las transacciones son intercambios significativos con respuesta observable, no cada clic.

| Clase | Transacciones | Peso |
|---|---:|---:|
| Simple | 1–3 | 5 |
| Media | 4–7 | 10 |
| Compleja | 8 o más | 15 |

`UUCW = Σ(cantidad de casos de uso × peso)`

### Tamaño no ajustado: UUCP

UUCP es *Unadjusted Use Case Points*: **puntos de caso de uso sin ajustes**.

`UUCP = UAW + UUCW`

“Sin ajustar” recuerda que todavía no se consideró ni la dificultad técnica ni el contexto del equipo.

### Dificultad técnica: TCF

TCF es *Technical Complexity Factor*: **factor de complejidad técnica**. Resume factores como distribución, rendimiento, seguridad, concurrencia, portabilidad y facilidad de cambio.

Cada factor se califica de 0 a 5, se multiplica por su peso y se suma para obtener `TFactor`:

`TCF = 0,6 + 0,01 × TFactor`

Pregunta de memoria: **¿qué requisitos técnicos hacen más difícil construirlo?**

### Condiciones del equipo/proyecto: EF

EF es *Environmental Factor*: **factor ambiental**, donde ambiente significa condiciones de trabajo/equipo, no el medioambiente natural. Incluye experiencia, motivación, estabilidad de requisitos, dedicación parcial y dificultad del lenguaje.

Califica factores 0–5, aplica pesos (algunos negativos) y suma `EFactor`:

`EF = 1,4 − 0,03 × EFactor`

Pregunta de memoria: **¿qué condiciones ayudan o dificultan al equipo?**

### Tamaño ajustado: UCP

`UCP = UUCP × TCF × EF`

UCP todavía expresa tamaño ajustado; **no son horas**.

### Conversión a HH y esfuerzo total

Cuenta los factores ambientales desfavorables según la convención de la clase: E1–E6 con valoración menor que 3; E7–E8 con valoración mayor que 3.

| Factores desfavorables | Factor de conversión |
|---:|---:|
| 0–2 | 20 HH/UCP |
| 3–4 | 28 HH/UCP |
| 5 o más | Replantear viabilidad |

`Esfuerzo de programación = UCP × HH/UCP`

La convención de las lecturas del curso considera programación como 40 % del total:

`Esfuerzo total = esfuerzo de programación / 0,40`

Se divide por 0,40 porque el esfuerzo de programación es una parte del total. No se multiplica por 0,40.

## Ejemplo completo

Datos:

- 2 actores simples, 1 medio, 2 complejos.
- 3 casos simples, 2 medios, 1 complejo.
- `TFactor = 30`, `EFactor = 15`.
- Tres factores ambientales desfavorables.

**1. Actores:** `UAW = 2×1 + 1×2 + 2×3 = 10`.

**2. Casos de uso:** `UUCW = 3×5 + 2×10 + 1×15 = 50`.

**3. No ajustado:** `UUCP = 10 + 50 = 60`.

**4. Factores:** `TCF = 0,6 + 0,01×30 = 0,90`; `EF = 1,4 − 0,03×15 = 0,95`.

**5. Ajustado:** `UCP = 60×0,90×0,95 = 51,30`.

**6. Programación:** tres factores desfavorables → 28 HH/UCP. `51,30×28 = 1.436,40 HH`.

**7. Total:** `1.436,40/0,40 = 3.591,00 HH`.

Interpretación: esta cifra es esfuerzo humano estimado. Para obtener calendario hacen falta personas disponibles, perfiles, dependencias y trabajo paralelo. Para dinero hacen falta tarifas, infraestructura, licencias y otros costos.

## Sensibilidad: qué mueve el resultado

Si solo cambia TCF:

`ΔUCP = UUCP × ΔTCF × EF`

Si solo cambia EF:

`ΔUCP = UUCP × TCF × ΔEF`

Más actores o casos de uso elevan UUCP. Cambios técnicos afectan TCF; cambios en la experiencia, dedicación o estabilidad afectan EF. Recalcula desde el factor que cambió hasta el resultado final.

## Otros métodos de estimación que debes distinguir

- **Juicio experto:** experiencia humana; rápido y contextual, pero expuesto a sesgos.
- **Analogía:** compara con proyectos históricos semejantes; útil temprano si la comparación es real.
- **Paramétrica:** relaciona tamaño con esfuerzo mediante datos/fórmula calibrados.
- **Top-down/descendente:** estima el total y reparte; rápida al inicio.
- **Bottom-up/ascendente:** estima partes de la EDT y suma; más trazable si el detalle es bueno.
- **Puntos de función:** mide funcionalidad del usuario con EI, EO, EQ, ILF y EIF; no depende directamente del lenguaje.
- **COCOMO:** estima esfuerzo mediante tamaño y factores de costo; los parámetros deben servir al contexto.

No confundas el `TCF` de UCP con el de puntos de función: las fórmulas y factores son distintos.

## Práctica

1. Un actor humano usa interfaz gráfica. ¿Clase y peso?
2. Un caso de uso tiene 6 transacciones significativas. ¿Clase y peso?
3. `UAW=13`, `UUCW=55`, `TFactor=32`, `EFactor=18`. Calcula UUCP, TCF, EF y UCP.
4. Si hay tres factores desfavorables, calcula programación y esfuerzo total.
5. Explica por qué una fecha límite no reduce automáticamente el esfuerzo estimado.
6. Con 3.600 HH, 5 personas, 160 horas nominales por mes y 75 % de disponibilidad, calcula el plazo ideal y nombra dos limitaciones.

---

# 2. Requisitos, Alcance, Planificación y EDT — 72 puntos

Este bloque conecta el **qué** del proyecto con el **trabajo**, el **orden** y el **tiempo**.

## Requisitos y alcance

- **Requisito:** necesidad o condición que debe satisfacer el producto/proyecto.
- **Alcance del producto:** funciones y características del producto.
- **Alcance del proyecto:** trabajo necesario para entregar ese producto.
- Un requisito verificable contiene comportamiento/atributo, condición, medida/valor y método de comprobación.

Malo: “El sistema debe ser rápido”. Mejor: “Con 500 usuarios concurrentes, el percentil 95 responderá en ≤2 s, medido con prueba de carga en preproducción”.

### EDT/WBS

EDT (Estructura de Desglose del Trabajo), también WBS (*Work Breakdown Structure*), descompone jerárquicamente el **alcance total**, orientado a entregables.

- **Regla del 100 %:** la EDT cubre todo el trabajo requerido, incluyendo gestión; los hijos cubren al padre sin duplicación.
- **Paquete de trabajo:** nivel manejable para estimar, asignar y controlar.
- **Cuenta de control:** punto de integración de alcance, costo y cronograma para medir desempeño.
- **Paquete de planificación:** trabajo conocido que todavía no tiene detalle para ser paquete de trabajo.
- **Diccionario EDT:** explica cada elemento y sus criterios, responsables, supuestos, etc.
- **Línea base del alcance:** enunciado aprobado + EDT + diccionario de EDT.

La EDT no es una lista de tareas ni un cronograma: primero organiza entregables; luego se definen actividades.

### Aceptación y cambio

- **Controlar la Calidad:** ¿el entregable cumple técnicamente?
- **Validar el Alcance:** ¿el cliente/interesado autorizado lo acepta formalmente?
- Un entregable puede estar verificado sin estar aceptado.
- Un cambio se documenta y analiza; no se agrega a la línea base sin aprobación.

## Cronograma y red

El cronograma vincula actividades, duraciones, recursos, calendarios y dependencias. El diagrama de red representa las relaciones; la carta Gantt coloca las actividades sobre una escala de tiempo.

### Relaciones entre actividades

| Sigla | Significado | Cómo recordarlo |
|---|---|---|
| FS | Fin-Inicio (*Finish to Start*) | la sucesora empieza cuando termina la predecesora |
| SS | Inicio-Inicio (*Start to Start*) | ambos inicios se relacionan |
| FF | Fin-Fin (*Finish to Finish*) | ambos términos se relacionan |
| SF | Inicio-Fin (*Start to Finish*) | el inicio de una determina el término de otra; rara |

Un `+2` es un retraso de 2 unidades; un adelanto permite solapar trabajo. Ejemplo `FS+2`: B empieza dos unidades después de terminar A. `SS+2`: B empieza dos unidades después de iniciar A.

Tipos de dependencia:

- **Obligatoria:** lógica física/técnica/contractual.
- **Discrecional:** preferencia de ejecución del equipo.
- **Externa:** depende de una entidad fuera del proyecto.
- **Interna:** está bajo control del proyecto.

### Dibujo de red: receta

1. Haz una tabla con ID, duración y predecesoras.
2. Pon primero las actividades sin predecesoras.
3. Dibuja una flecha desde cada predecesora a su sucesora.
4. Si hay dos predecesoras, la actividad sucesora espera a ambas, salvo que la relación indique otra cosa.
5. Etiqueta relaciones especiales/adelantos/retrasos en las flechas.
6. Calcula fechas tempranas hacia adelante y tardías hacia atrás.

Ejemplo:

```text
             ┌─ B (3) ─┐
Inicio ─ A(2)            ├─ D(3) ─ E(2) ─ Fin
             └─ C (4) ─┘
```

B y C pueden avanzar en paralelo. D espera a ambas.

### Recorrido hacia adelante y atrás

- **ES** (*Early Start*): inicio temprano.
- **EF** (*Early Finish*): fin temprano.
- **LS** (*Late Start*): inicio tardío que no retrasa el proyecto.
- **LF** (*Late Finish*): fin tardío que no retrasa el proyecto.

En el ejemplo, usa tiempo cero:

| Actividad | Duración | ES | EF |
|---|---:|---:|---:|
| A | 2 | 0 | 2 |
| B | 3 | 2 | 5 |
| C | 4 | 2 | 6 |
| D | 3 | max(5,6)=6 | 9 |
| E | 2 | 9 | 11 |

Hacia adelante: `EF = ES + duración`; con varias predecesoras FS, usa el mayor EF. Hacia atrás: parte desde la fecha final, resta duración; cuando hay varias sucesoras, usa el menor LS para fijar LF.

### Holguras y ruta crítica

- **Holgura total:** cuánto puede atrasarse una actividad sin atrasar el proyecto. `LS−ES` o `LF−EF`.
- **Holgura libre:** cuánto puede atrasarse sin mover el inicio temprano de su sucesora inmediata.
- **Ruta crítica:** secuencia que determina el plazo total, normalmente con holgura total cero.

En el ejemplo, el camino A–C–D–E dura 11 días y es crítico. Atrasar actividad no crítica dentro de su holgura no cambia el término; atrasarla más puede desplazar el proyecto y también cambiar la ruta crítica.

### Carta Gantt: receta

1. Dibuja una fila por actividad.
2. Dibuja columnas para días/semanas.
3. Usa ES y EF para ubicar las barras.
4. Marca la duración de cada actividad.
5. Representa hitos como diamante o punto y dependencias con flechas si se solicitan.

Ejemplo con convención de intervalos `[inicio, fin)`:

```text
Día       0 1 2 3 4 5 6 7 8 9 10
A         ■ ■
B             ■ ■ ■
C             ■ ■ ■ ■
D                     ■ ■ ■
E                             ■ ■
```

La Gantt debe respetar las relaciones de la red; no inventes fechas independientes.

### Comprimir el cronograma y sesgos

- **Crashing/intensificación:** agrega recursos/costo a actividades críticas para acortar duración.
- **Fast tracking/ejecución rápida:** solapa trabajo originalmente secuencial; sube el riesgo de retrabajo.
- **Nivelación de recursos:** resuelve recursos sobreasignados; puede alargar y cambiar la ruta crítica.
- **Suavizamiento:** mueve actividades dentro de holgura sin cambiar la fecha final.

Solo comprimir una tarea crítica puede adelantar el proyecto. Estimaciones pueden sufrir optimismo, anclaje en una fecha impuesta, presión externa y omisión de tareas de coordinación. Usa datos, supuestos explícitos y tres valores si hay incertidumbre.

### PERT (tres valores)

`O` = optimista, `M` = más probable, `P` = pesimista.

- Triangular: `(O+M+P)/3`.
- PERT beta: `(O+4M+P)/6`.
- Desviación aproximada: `(P−O)/6`.

## Práctica

1. A dura 4 días desde 0; B dura 5 días y tiene `SS+2` con A. ¿Inicio/fin de B?
2. Explica FS, SS y FF con un ejemplo.
3. Dibuja y resuelve la red de cinco actividades del ejemplo.
4. Si una tarea tiene holgura total 2 y se retrasa 3 días, ¿qué debes revisar?
5. Diferencia crashing y fast tracking en costo y riesgo.
6. ¿Cuál es la diferencia entre EDT, lista de actividades, red y Gantt?

---

# 3. Arquitectura de Software y nube — 45 puntos

Arquitectura describe responsabilidades, fronteras, relaciones y despliegue de los componentes. Una buena respuesta liga **requisito → decisión → consecuencia**.

## Estilos y consecuencias

- **Monolito modular:** una unidad desplegable con módulos internos separados. Suele servir a equipo pequeño o dominio todavía cambiante; simplifica operación y consistencia, pero limita despliegues independientes.
- **Capas:** separa presentación, negocio y datos. Facilita orden y pruebas; no confundas capa lógica con servidor físico.
- **Microservicios:** servicios autónomos desplegables por separado. Permiten escalar capacidades selectivamente; exigen operación, red, observabilidad, seguridad y consistencia distribuidas.
- **Eventos:** un productor publica un hecho y consumidores reaccionan. Desacopla tiempo; requiere manejar duplicados, orden, reintentos e idempotencia.
- **Síncrono:** quien llama espera respuesta. Adecuado cuando la respuesta inmediata es necesaria.
- **Asíncrono:** quien envía no espera que el receptor procese en ese momento. Útil para notificaciones y cargas desacopladas.

Un sistema escala horizontalmente si puede operar agregando instancias y repartiendo carga sin depender de estado exclusivo en una máquina; se deben atender sesiones, datos, coordinación y cuellos de botella compartidos.

## Nube: quién administra qué

| Modelo | Proveedor administra | Cliente administra | Ejemplo de uso |
|---|---|---|---|
| IaaS | hardware y virtualización | SO, middleware y aplicación | se necesita control del entorno |
| PaaS | infraestructura y plataforma administrada | aplicación y datos/configuración | priorizar desarrollo sobre operación de plataforma |
| SaaS | solución completa | uso y configuración disponible | proceso estándar que calza con el producto |

No confundas modelo de servicio (IaaS/PaaS/SaaS) con despliegue (pública/privada/híbrida/multicloud).

## Términos que suelen confundirse

- **Escalabilidad:** capacidad de atender más carga al ampliar recursos.
- **Elasticidad:** ajustar recursos al alza o baja según demanda.
- **Disponibilidad:** proporción de tiempo que el servicio funciona.
- **Rendimiento:** tiempos de respuesta/capacidad bajo carga.
- **RTO:** tiempo máximo objetivo de recuperación.
- **RPO:** cantidad máxima de datos/pérdida temporal tolerada.
- **SLI:** indicador medido.
- **SLO:** objetivo de servicio.
- **SLA:** compromiso contractual con medición y consecuencias.

La disponibilidad se combina según la **topología**:

- **En serie (AND):** el servicio funciona solo si todos los componentes funcionan. Multiplica disponibilidades: `A_serie = A1×A2×…×An`. Dos componentes de 99,9 % en serie dan `0,999²=99,8001 %`.
- **En paralelo redundante (OR):** el servicio funciona mientras al menos uno de los componentes esté disponible. Primero calcula la probabilidad de que **todos fallen** y réstala de 1: `A_paralelo = 1 − (1−A1)×(1−A2)` para un par independiente.

**Ejemplo de un par:** dos equipos redundantes tienen disponibilidad de 99 % cada uno (`A1=A2=0,99`). La indisponibilidad de cada uno es `1−0,99=0,01` (1 %). La probabilidad de que fallen ambos a la vez, suponiendo independencia, es `0,01×0,01=0,0001` (0,01 %). Por tanto:

`A_paralelo = 1−0,0001 = 0,9999 = 99,99 %`

**Cómo recordarlo:** en serie suman oportunidades de falla, así que multiplicas las disponibilidades; en paralelo hay que fallar en todos los caminos, así que multiplicas las indisponibilidades y restas el resultado de 1.

**Supuesto importante:** la fórmula del par supone independencia. Si ambos equipos comparten energía, red, tablero, software defectuoso, sala o una causa común, pueden fallar juntos; la disponibilidad real será menor. La redundancia solo ayuda si el camino alternativo también puede sostener el servicio y el cambio/conmutación funciona.

Para dos componentes distintos: `A_paralelo = 1−(1−A1)(1−A2)`. Para `n` componentes paralelos independientes: `A = 1−∏(1−Ai)`.

## Práctica

1. ¿Por qué un microservicio no escala automáticamente mejor que un monolito?
2. ¿Qué debe cuidar una aplicación sin estado local para escalar horizontalmente?
3. Elige IaaS, PaaS o SaaS para una necesidad muy personalizada y justifica.
4. Calcula disponibilidad en serie de tres componentes de 99,9 %.
5. Distingue RTO/RPO y SLI/SLO/SLA.

---

# 4. Calidad — 45 puntos

## Calidad versus grado

- **Calidad:** cumplimiento de los requisitos.
- **Grado:** categoría o nivel de prestaciones.

Un producto básico puede ser de bajo grado y alta calidad si cumple perfectamente los requisitos de su categoría. Más funcionalidades no significan automáticamente más calidad.

## Costo de la calidad (COQ)

COQ = costo de conformidad + costo de no conformidad.

| Categoría | Significado | Ejemplo |
|---|---|---|
| Prevención | Evitar defectos | formación, estándares, revisión de diseño |
| Evaluación | Detectar defectos | inspección y pruebas |
| Falla interna | Defecto detectado antes de entregar | retrabajo, descarte |
| Falla externa | Defecto detectado después de entregar | garantía, multa, atención de incidente |

Prevención + evaluación son conformidad; fallas internas + externas, no conformidad.

## Procesos y orden

1. **Planificar la calidad:** decidir estándares, métricas y cómo cumplirlos.
2. **Gestionar la calidad:** auditar/mejorar procesos para producir calidad.
3. **Controlar la calidad:** medir productos/resultados y detectar desviaciones.
4. **Validar el alcance:** recibir aceptación formal del cliente; conecta con el capítulo de alcance.

Memoria rápida: **planifico el criterio, gestiono el proceso, controlo el resultado, el cliente acepta**.

## Herramientas y requisitos

- **Pareto:** prioriza las pocas causas que explican la mayor parte de los problemas.
- **Ishikawa:** organiza causas posibles por categorías para investigar.
- **5 porqués:** profundiza hasta causas raíz.
- **Hoja de verificación:** registra frecuencias de manera consistente.
- **Histograma:** muestra distribución de datos.
- **Gráfico de control:** observa estabilidad del proceso en el tiempo.
- **Dispersión:** explora relación entre dos variables, no demuestra causalidad por sí sola.
- **Diagrama de flujo:** visualiza pasos y puntos de falla.

Un requisito de calidad bien escrito tiene **atributo + métrica + valor + condición + método de verificación**. Ejemplo: “Con 500 usuarios, P95 ≤2 s, medido en prueba de carga en preproducción”.

Límites de control describen variación del proceso; límites de especificación expresan lo que exige el cliente. Un proceso estable puede incumplir especificaciones.

## Práctica

1. Clasifica capacitación, inspección, retrabajo preentrega y garantía.
2. Da un ejemplo de producto bajo grado y alta calidad.
3. Escribe requisito medible para “debe ser seguro”.
4. ¿Cuándo usar Pareto y cuándo Ishikawa?
5. ¿Qué diferencia hay entre Controlar Calidad y Validar Alcance?

---

# 5. Trabajos de Investigación — 45 puntos

El aviso dice que se repasen las presentaciones de compañeros y que no se responde la pregunta del trabajo propio.

## Ficha de estudio por trabajo

Completa una ficha por cada presentación ajena:

1. Tema y problema central.
2. Concepto o argumento principal.
3. Alternativas que comparó el grupo.
4. Ventajas/desventajas de cada alternativa.
5. Cifra, ejemplo, resultado o caso que destacaron.
6. Conclusión/recomendación del grupo y razón.
7. Una pregunta que podrían hacer y respuesta en tres frases.

No inventes datos si no aparecen en el informe. Prioriza lo que cada grupo eligió destacar, porque eso ayuda a distinguir sus trabajos.

## Preparación para el examen

Antes de rendir, identifica cuál exposición fue la tuya y márcala como **no responder**. En las otras preguntas, contesta concepto + comparación + dato/ejemplo + consecuencia.

---

# 6. Sala de Servidores — 36 puntos

## Qué dimensionar

La sala debe mantener energía, clima, conectividad, seguridad y monitoreo. Dimensiona a partir de carga TI; evita partir con un número arbitrario de racks.

Cadena de pensamiento:

> equipos TI → potencia → UPS y pérdidas → potencia total → calor → climatización → redundancia y continuidad.

## TIER

- **Tier I:** camino único, sin redundancia significativa.
- **Tier II:** componentes redundantes.
- **Tier III:** mantenimiento concurrente de componentes/capacidad, sin detener el servicio en condiciones previstas.
- **Tier IV:** tolerancia a fallas.

Una certificación TIER caracteriza infraestructura evaluada. No convierte por sí sola una aplicación en altamente disponible: aplicación, red, identidad, datos y operación también importan.

`N` es capacidad requerida; `N+1` agrega un componente; `2N` duplica sistemas completos. Redundancia de equipos sin independencia de caminos puede dejar un punto común de falla.

## Energía y eficiencia

`PUE = energía total de instalación / energía de equipos TI`

`DCiE = energía TI / energía total = 1/PUE`

Si TI consume 40 kW y PUE=1,6, potencia/consumo equivalente total = `40×1,6=64 kW`; el resto son cargas no TI y pérdidas. Siempre usa la misma base temporal/unidades.

La potencia eléctrica que consumen los equipos se transforma mayormente en calor en la sala; climatización debe retirar esa carga térmica, considerando capacidad y redundancia. En la prueba usa las conversiones y unidades enseñadas en clases.

## Práctica

1. Calcula PUE/DCiE si total=72 kW y TI=45 kW.
2. Diferencia N+1 y 2N.
3. Explica por qué TIER III no certifica automáticamente la aplicación.
4. Describe qué consecuencias tendría una UPS que comparte un único tablero y camino eléctrico.

---

# 7. Gestión de los Riesgos — 18 puntos

Un riesgo es un evento o condición incierta que afecta objetivos positiva o negativamente. Si ya ocurrió, es problema/incidente.

## Cómo redactar y medir

Formato de memoria: **causa → evento incierto → efecto**.

Ejemplo: “Como el proveedor no congela la API (causa), podría cambiar el contrato durante el desarrollo (evento), lo que causaría retrabajo y atraso de integración (efecto)”.

`Exposición = probabilidad × impacto`

`EMV = probabilidad × impacto monetario`; amenaza con costo negativo, oportunidad con beneficio positivo. Un EMV es valor esperado, no una garantía del resultado real.

## Zonas de acción y respuestas

La matriz probabilidad-impacto suele separar zonas baja, media y alta según umbrales acordados. Zona alta requiere atención/respuesta prioritaria; zona media seguimiento y evaluación; zona baja puede aceptarse o monitorearse. La matriz exacta y los umbrales los define el curso/proyecto.

**Amenazas:** escalar, evitar, transferir, mitigar, aceptar.

**Oportunidades:** escalar, explotar, compartir, mejorar, aceptar.

- **Mitigar:** bajar probabilidad o impacto.
- **Transferir:** cambiar quién asume parte del impacto; no borra la amenaza.
- **Evitar:** eliminar causa/amenaza mediante cambio de plan.
- **Aceptar:** reconocer y decidir no actuar preventivamente (puede haber contingencia).
- **Residual:** queda después de responder.
- **Secundario:** lo genera la respuesta.

Una respuesta conviene cuando es viable, cuesta menos que la exposición que reduce (considerando impactos relevantes), tiene responsable y disparador/fecha claros, y se alinea con la tolerancia al riesgo.

## Práctica

1. Redacta riesgo causa-evento-efecto de un proveedor.
2. Calcula EMV de 25 % de probabilidad e impacto de −$40 millones.
3. Distingue mitigar, transferir y aceptar.
4. Da un ejemplo de riesgo secundario y residual.

---

# 8. Lecturas PMBOK 5, 6, 8 y 11

No intentes leer cada capítulo palabra por palabra la noche anterior. Usa las lecturas para fijar vocabulario y diferencias:

- **Capítulo 5 (Alcance):** requisitos, alcance, EDT, línea base, validar vs controlar.
- **Capítulo 6 (Cronograma):** actividades, secuencias, duraciones, cronograma, ruta crítica y control.
- **Capítulo 8 (Calidad):** planificar, gestionar y controlar calidad; costo y métricas.
- **Capítulo 11 (Riesgos):** planificar, identificar, cualitativo/cuanti, respuestas e implementación/monitoreo.

Para cada proceso responde: **¿qué problema resuelve?, ¿qué información usa?, ¿qué produce?, ¿con qué proceso vecino se confunde?**

---

# Secuencia sugerida para estudiar hoy

Adáptala al tiempo que tengas; es una secuencia de prioridades, no una promesa de cobertura total en horas:

1. **UCP:** memoriza la historia UAW + UUCW → UUCP → TCF/EF → UCP → HH. Resuelve dos ejercicios completos y uno de sensibilidad.
2. **Red/EDT:** dibuja una red y su Gantt; calcula recorrido adelante/atrás, holguras y ruta crítica. Practica relaciones FS, SS y FF con lag/lead.
3. **Arquitectura/nube:** haz una tabla mental de alternativas, condición para elegir y consecuencia/costo.
4. **Calidad:** clasifica ejemplos y escribe requisitos verificables; repite calidad vs grado y proceso vs aceptación.
5. **Investigación:** prepara fichas de todas las presentaciones salvo la propia.
6. **Sala:** resuelve PUE/DCiE y explica TIER/N+1/2N en voz alta.
7. **Riesgos:** calcula exposición/EMV y redacta una amenaza con respuesta, dueño y disparador.
8. **PMBOK:** repasa definiciones de los capítulos 5, 6, 8 y 11 y las diferencias de procesos.

## Lista final de recuperación activa

Antes de dormir, sin mirar, explica en voz alta:

- qué significa cada sigla de UCP;
- diferencia entre tamaño, esfuerzo, plazo, dotación y costo;
- cómo construir red y Gantt;
- diferencia entre holgura total y libre;
- qué aporta y qué cuesta cada modelo de nube/arquitectura;
- calidad vs grado y las cuatro categorías COQ;
- TIER, PUE, carga TI y relación con refrigeración;
- exposición, EMV y estrategias de respuesta.

En la prueba, la alternativa sola puede no recibir puntaje en desarrollos: deja escrito el procedimiento y concluye con una interpretación breve.

