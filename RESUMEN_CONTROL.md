# RESUMEN DIDÁCTICO — CONTROL FEP

> Temas: **Requisitos, Alcance y Planificación** · **Estimación de Software** · **Gestión de Riesgos**

---

# TEMA 1 — REQUISITOS, ALCANCE Y PLANIFICACIÓN

## La idea en una frase
> Todo el problema de un proyecto es: **no construir ni más ni menos de lo que se pidió**, y hacerlo en el plazo y precio correctos. Todo lo demás son herramientas para eso.

## 1.1 Proyecto vs Operación (esto cae seguro)

| | Proyecto | Operación |
|---|---|---|
| Duración | Temporal (tiene fin) | Continua |
| Resultado | Único | Repetitivo |

**Analogía**: construir una casa = proyecto (una sola vez, se acaba). Mantener la casa limpia todos los días = operación.

**Tip**: Si en el control te preguntan "¿qué NO es un proyecto?", la respuesta típica es *"el soporte mensual de un sistema"* o *"la operación continua de un servicio"*.

### PMBOK — memoriza los 3 números
- **5** grupos de procesos: **I**nicio, **P**lanificación, **E**jecución, **M**onitoreo y control, **C**ierre.
  - *Mnemotecnia*: "**I**nvertir **P**lata **E**xige **M**ucha **C**alma" (I-P-E-M-C).
- **10** áreas de conocimiento.
- **49** procesos.

**Trampa clásica**: "los grupos de procesos son fases". **FALSO** — los grupos se solapan y ocurren dentro de cada fase. El PMBOK lo repite porque es el error más común.

### Triple restricción
Alcance ↔ Tiempo ↔ Costo: son un triángulo. Si fijas dos, el tercero se obliga.

**Analogía**: es un globo — si aprietas un lado (plazo), se infla otro (costo o alcance).

**Tip de control**: "Si las bases fijan plazo y presupuesto, ¿qué le queda al oferente?" → **negociar el alcance**. Esa frase la puedes usar tal cual en una pregunta de desarrollo.

---

## 1.2 Requisitos

**Idea central**: el requisito es *lo más barato de corregir y lo más caro de equivocar* (hasta **100×** el costo). Por eso todo lo demás se construye sobre él.

### Qué es y qué NO es
Un requisito es una **necesidad** o una **condición que debe cumplir el sistema** (IEEE 610.12).

**Trampa**: "¿es requisito el diseño técnico?" → **NO**. El *cómo* es diseño, no requisito. Regla de oro:
> Si el enunciado admite otra solución técnica igualmente válida → es requisito. Si no admite otra → es diseño.

### Funcionales vs No funcionales
- **Funcional** = qué HACE (registrar, consultar, informar).
- **No funcional** = bajo qué CONDICIONES (rápido, seguro, disponible).

**Trampa favorita del profe**: *"El sistema será rápido"* NO es un requisito no funcional. Lo es: *"el 95% de las consultas responden en < 2 segundos con 500 usuarios concurrentes"*.
> **Sin número, no es requisito: es una intención.**

### Las 4 actividades del desarrollo de requisitos
**Extraer → Analizar → Especificar → Verificar** (es un ciclo: si verificando aparece una inconsistencia, vuelves a analizar).

### FURPS+ (memorizar las letras)
- **F**uncionalidad, **U**sabilidad (facilidad de uso), **R**eliability (fiabilidad), **P**erformance (rendimiento), **S**upport (soporte).
- El **"+"**: Implementación, Interfaz, Operaciones, Empaquetado, **L**egales.

**Tip**: el "+" es "donde vive la letra chica de las bases" (lenguaje obligatorio, licencias).

### Las 8 características de una buena ERS
No ambigua · Completa · Concisa · **Fácil de verificar** · **Consistente** · Fácil de modificar · **Trazable** · Priorizada.

**Tip de control**: las que más se incumplen son las 4 en negrita. Si te preguntan "cuál es la más difícil de cumplir", di **"fácil de verificar"** o **"no ambigua"**.

### SMART (para redactar bien)
**S**pecífico, **M**edible, **A**lcanzable, **R**esultado (orientado a resultados), **T**iempo (con plazo).

### Priorización
**MoSCoW**: **M**ust (debe), **S**hould (debería), **C**ould (podría), **W**on't (no será).

---

## 1.3 Alcance

**Idea central**: definir alcance es, sobre todo, **decidir qué NO se hará**. Lo que no excluyes por escrito, *se presume incluido* (y lo pagas tú).

### Producto vs Proyecto
- **Alcance del producto**: qué tendrá el producto (lo valida el **usuario**).
- **Alcance del proyecto**: todo el trabajo para entregarlo (lo aprueba el **patrocinador**).

**Tip**: dos proyectos con el mismo producto pueden costar distinto por la migración/capacitación/marcha blanca (eso no cambia el producto, pero sí el precio).

### Supuestos vs Restricciones (pregunta segura)
- **Supuesto**: algo que doy por cierto SIN verificar (ej: "el cliente entregará los datos completos"). Si es falso → me afecta.
- **Restricción**: limitación CONOCIDA que me acota (ej: "presupuesto fijo", "debe correr en su infraestructura").

**Frase clave**: *"un supuesto no declarado es un riesgo asumido gratis."*

### Scope creep vs Gold plating (trampa favorita)
- **Scope creep (corrupción del alcance)**: el CLIENTE pide de a poquito y el alcance crece sin control. → Lo evitas con control de cambios.
- **Gold plating (exceso de funcionalidad)**: el PROVEEDOR regala funciones de más por iniciativa propia. → Lo evitas entregando exactamente lo pedido.

**Tip**: aprende a distinguirlos por **quién los origina**: creep = cliente, gold plating = proveedor.

### Línea base del alcance = 3 documentos
1. Enunciado del alcance
2. EDT
3. Diccionario de la EDT

Solo cambia por **control de cambios**. *Un documento aprobado por correo pero no incorporado a la línea base NO es parte de la línea base.*

---

## 1.4 La EDT (WBS)

**Idea central**: la EDT es *desglosar el trabajo en pedazos cada vez más chicos* hasta poder estimar cada pedazo.

**Analogía**: partir una pizza — la pizza entera es el proyecto, las porciones son los entregables, el último bocado manejable es el **paquete de trabajo**.

### La regla del 100% (cae SIEMPRE)
Los hijos suman exactamente el 100% del padre.
- Si suman **menos** → hay "trabajo huérfano" (nadie lo hará).
- Si suman **más** → hay trabajo duplicado.

### Lo que la EDT NO es
**Trampa**: "¿la EDT muestra la secuencia de trabajo?" → **NO**. La EDT no tiene fechas ni flechas. El orden aparece DESPUÉS, en el cronograma. *Confundir EDT con cronograma es el error más frecuente.*

### Regla 8/80
Un paquete de trabajo debe durar entre **8 y 80 horas** (ni menos de un día, ni más de dos semanas).

### RACI (memorizar las 4 letras)
- **R** = Responsible (ejecuta)
- **A** = Accountable (responde/aprueba — **uno solo**)
- **C** = Consulted (consultado)
- **I** = Informed (informado)

**Truco**: la "A" es única. Si hay dos "A", está mal.

---

## 1.5 El cronograma

**Idea central**: la EDT dice QUÉ hacer; el cronograma dice CUÁNDO y en qué ORDEN.

### Esfuerzo ≠ Duración (concepto estrella)
- **Esfuerzo** = trabajo (horas-hombre). No cambia si agrego gente.
- **Duración** = tiempo calendario. Sí depende de cuánta gente.

**Analogía**: "9 mujeres embarazadas no producen un bebé en 1 mes". Agregar gente NO reduce el plazo proporcionalmente (comunicación, curva de aprendizaje, trabajo no paralelizable).

### PERT — las 3 fórmulas (memoriza, caen con números)
- **Triangular**: `tE = (O + M + P) / 3`
- **Beta (PERT)**: `tE = (O + 4M + P) / 6` ← la importante
- **Desviación**: `σ = (P − O) / 6`

**Tip**: la beta le da 4 veces más peso al "más probable". Si el control te da O=4, M=7, P=16 → tE = (4 + 28 + 16)/6 = **8 días**, σ = 2.

**Interpretación clave**: comprometer tE (8 días) = **50% de probabilidad de atraso**. Para ofertar con multas, compromete el ±2σ (95,45%).

### Ruta crítica
- Es el **camino más largo** del diagrama de red.
- Sus actividades tienen **holgura cero**.
- Si una se atrasa, el proyecto se atrasa.

**Truco para calcularla**: recorre hacia adelante (inicio temprano = max de los finales tempranos) y hacia atrás (final tardío = min de los inicios tardíos). Holgura = inicio tardío − inicio temprano. Las de holgura 0 = ruta crítica.

### Compresión del cronograma
- **Crashing**: más recursos → sube COSTO.
- **Fast-tracking**: paralelizar → sube RIESGO.

**Tip**: aprende la diferencia por "qué sube": crashing = costo, fast-tracking = riesgo.

### Reservas
- **Contingencia**: riesgos CONOCIDOS, dentro de la línea base, la usa el jefe de proyecto.
- **De gestión**: riesgos DESCONOCIDOS, fuera de la línea base, requiere la dirección.

---

## 1.6 Estimación y costo (puente con el Tema 2)

**Cadena**: Paquete EDT → horas → costo directo → gastos generales → margen → precio.

**Trampa**: estimar con **horas nominales** (180 h/mes) subestima el costo >20%. Hay que usar **horas productivas** (75–85%).

### Cono de incertidumbre
Al inicio puedes fallar de 0,25× a 4×. La oferta se firma en el punto más ancho del cono → **por eso existe la contingencia**.

---

# TEMA 2 — ESTIMACIÓN DE SOFTWARE

## La idea en una frase
> No puedes pesar el software en kilos, así que le inventas una unidad: **mides la funcionalidad que recibe el usuario** (no las líneas de código), y de ahí conviertes a horas y a plata.

**Analogía**: una casa se cotiza en m², una carretera en km. El software se cotiza en **Puntos de Función** o **Puntos de Casos de Uso**.

## 2.1 La cadena que debes tener clara
**Tamaño → Esfuerzo → Plazo → Costo** (4 cosas DISTINTAS, encadenadas).

| Eslabón | Qué mide | Unidad |
|---|---|---|
| Tamaño | cuánta funcionalidad | PF / UCP |
| Esfuerzo | cuánto trabajo cuesta | horas |
| Plazo | cuánto tiempo calendario | semanas |
| Costo | cuánta plata | pesos |

**Trampa**: *saltarse un eslabón* (pasar de requisitos directo a precio) es el error más frecuente y el que no puedes defender ante el evaluador.

**Tip clave**: los métodos estiman **solo esfuerzo y costo**. El plazo sale del cronograma; el precio, de una decisión comercial.

---

## 2.2 Punto Función (Albrecht)

**Idea**: cuenta 5 tipos de cosas que cruzan la "frontera" del sistema, cada una con un peso según su complejidad.

### Las 5 categorías (memoriza siglas y pesos)
- **Datos**: **ILF** (interno, lo mantengo yo: 7/10/15) y **EIF** (externo, lo mantiene otro: 5/7/10).
- **Transacciones**: **EI** (entrada: 3/4/6), **EO** (salida CON cálculo: 4/5/7), **EQ** (consulta SIN cálculo: 3/4/6).

**Trampa favorita**: distinguir **EO de EQ**.
> Si el dato que sale fue **calculado/derivado** → EO. Si sale **tal como está guardado** → EQ.

**Fórmula**: `FP = UFP × TCF`, donde `TCF = 0,65 + 0,01 × Σ(14 factores)`.

**Tip**: el ajuste (TCF) solo mueve ±35%. El esfuerzo debe ir a **contar bien**, no a discutir los factores.

---

## 2.3 Punto de Casos de Uso (Karner) — el que vas a aplicar

**Idea**: cuenta **actores** y **casos de uso**, los pesa, los ajusta por el sistema (TCF) y por el equipo (EF), y convierte a horas.

### Las 5 fórmulas (memoriza el orden)
1. `UUCP = UAW + UUCW`
2. `TCF = 0,6 + 0,01 × Σ(peso × valor)`
3. `EF = 1,4 − 0,03 × Σ(peso × valor)`
4. `UCP = UUCP × TCF × EF`
5. `E = UCP × CF`

**Truco de memoria**: "Uno, dos, tres, cuatro, cinco — suma, ajusta técnico, ajusta ambiente, multiplica, convierte".

### Actores (UAW)
- Simple (otro sistema con API) = **1**
- Medio (protocolo/texto) = **2**
- Complejo (persona con interfaz gráfica) = **3**

**Trampa**: *un actor es un ROL, no una persona*. 5.000 vecinos = **un solo** actor "Vecino" (3 puntos, no 15.000).

### Casos de uso (UUCW) — por transacciones
- Simple (1–3 transacciones) = **5**
- Medio (4–7) = **10**
- Complejo (8+) = **15**

**¿Qué es una transacción?** Un viaje de ida y vuelta usuario↔sistema que termina cuando el sistema queda esperando el siguiente estímulo.

---

## 2.4 Los dos ajustes (concepto que más vale entender)

**TCF habla del SISTEMA** (qué tan exigente es). **EF habla del EQUIPO** (qué tan bueno es).

### La lectura contraintuitiva (¡cae!)
> **EF bajo = BUENO.** El EF no mide cuán bueno es tu equipo, mide **cuánto le va a costar**. EF = 0,42 (equipo experto) reduce esfuerzo 58%. EF = 1,70 (equipo malo) lo sube 70%.

**Analogía**: no es una "nota" del equipo, es un "multiplicador de dolor". Menos dolor = menos horas.

### Los 8 factores de ambiente — el detalle trampa
E7 (personal a tiempo parcial) y E8 (dificultad del lenguaje) tienen **peso NEGATIVO (−1)**. Porque un valor alto ahí es MALO (sube el esfuerzo).

---

## 2.5 Del tamaño al esfuerzo

### Factor de conversión (CF) — el parámetro más sensible
`E = UCP × CF`. CF por defecto = **20 h/UCP**.

**Regla de los factores desfavorables** (cuenta E1–E6 < 3 y E7–E8 > 3):
- **≤ 2 desfavorables → 20 h/punto**
- **3–4 → 28 h/punto (+40%)**
- **≥ 5 → NO se estima, se replantea el proyecto**

**Tip**: cambiar de 20 a 28 sube el esfuerzo 40%. Es lo más sensible de todo el método → hay que justificarlo bien.

### Distribución del esfuerzo (memoriza)
Análisis **10%** · Diseño **20%** · Programación **40%** · Pruebas **15%** · Sobrecarga **15%**.

**Frase clave**: *programar es menos de la mitad del trabajo*. Quien estima solo programación deja fuera el 60%.

### Lectura A vs B (¡trampa del curso!)
- **A**: E = esfuerzo TOTAL (se reparte).
- **B**: E = solo PROGRAMACIÓN → total = E ÷ 0,40.

**El curso adopta la B** (y hay que DECLARARLO). Diferencia: 2,5×. Si no dices cuál usaste, tu número es inverificable.

### Esfuerzo → plazo NO es dividir
No divides horas por personas para sacar el plazo. El plazo sale del **cronograma** (ruta crítica). El cociente solo es una "cota inferior imposible".

---

## 2.6 El ejemplo completo (memoriza los números clave)
- UAW = 15, UUCW = 120 → **UUCP = 135**
- TCF = 1,095 · EF = 0,86 → **UCP = 127,1**
- CF = 20 → E = 2.542 h → **total = 6.355 h** (÷ 0,40)

**Sensibilidad** (¿qué mueve más la aguja?):
- CF 20→28 = **+40%** ← lo más dominante
- 3 casos de uso olvidados = +22%
- EF a 1,0 = +16%

**Tip**: dedica tiempo a **completar el modelo** (no olvidar casos de uso) y a **autoevaluarte con honestidad**, no a discutir si un factor vale 3 o 4.

---

# TEMA 3 — GESTIÓN DE RIESGOS

## La idea en una frase
> Un riesgo es algo que **TODAVÍA no pasó** pero puede pasar. Si ya pasó, es un **problema**. Y "gestionarlo" no es anotarlo en una lista: es **tomar una decisión que cambie la propuesta**.

**Trampa de la primera pregunta**: si puedes poner el verbo en pasado, no es riesgo. *"El proveedor no entregó la API"* = problema. *"Puede que el proveedor no entregue la API"* = riesgo.

## 3.1 Las 3 palabras que se confunden
- **Incertidumbre**: no sé (materia prima).
- **Riesgo**: evento incierto con efecto (se gestiona con respuesta + reserva).
- **Problema**: ya pasó (acción correctiva).

### Amenazas vs Oportunidades (¡importante!)
Un riesgo puede ser NEGATIVO (amenaza) o POSITIVO (oportunidad). La palabra que casi nadie lee es "positivo".

**Tip que da puntos**: las oportunidades son la única forma legítima de **bajar el precio sin bajar el alcance**. Un control que solo tiene amenazas está incompleto (el profe lo descuenta: "cero oportunidades").

### La fórmula más importante de todo el tema
**Exposición = Probabilidad × Impacto** (`E = P × I`)

Es la que ordena TODAS las decisiones. Memorízala como "la fórmula del riesgo".

### Los 5 elementos de un riesgo
Probabilidad · Impacto · Exposición · Marco de tiempo · **Evento de disparo** (la señal de que se está materializando).

---

## 3.2 Los 7 procesos (memoriza el orden)
1. Planificar → 2. Identificar → 3. Análisis **cualitativo** → 4. Análisis **cuantitativo** → 5. Planificar respuesta → 6. Implementar → 7. Monitorear.

**Tip**: cualitativo = **priorizar** (decide DÓNDE mirar). Cuantitativo = **dimensionar** (decide CUÁNTO pagar). En precio fijo, el cuantitativo NO es opcional.

---

## 3.3 Identificar: cómo escribir un riesgo bien

### La fórmula mágica (memoriza y usa)
> **"Dado que** \<causa cierta\> **entonces puede que** \<evento incierto\> **teniendo como consecuencia** \<efecto en un objetivo\>"

**Trampa**: confundir causa con riesgo.
- *"El equipo no tiene experiencia"* = **CAUSA** (hecho cierto, no lleva probabilidad).
- *"...puede que el desarrollo demore más, con consecuencia de 4 semanas de atraso"* = **RIESGO**.

### La fábrica de riesgos = supuestos
Por cada supuesto que escribes, escribe el riesgo de que sea falso.
> Ej: supuesto "ClaveÚnica se habilita en 8 semanas" → riesgo "puede que demore el doble → hito contractual incumplido".

### Frases de riesgo en las bases (reconócelas)
- *"…y todo lo necesario para su correcto funcionamiento"* → alcance sin borde.
- *"…a satisfacción del mandante"* → recepción subjetiva.
- *"…disponibilidad permanente"* → ¿99% o 99,99%? (2 órdenes de magnitud de diferencia de costo).
- *"…se integrará con los sistemas del mandante"* → no dice cuáles.

**Tip**: cada una de esas frases = una **consulta** que puedes hacer en el foro (gratis).

---

## 3.4 Analizar: poner números

### VME = Valor Monetario Esperado
`VME = Probabilidad × Impacto` (en dinero).

**Trampa de lectura**: el VME NO es lo que va a costar. "50% × $6.400.000 = $3.200.000" no significa que costará 3,2 millones — costará 6,4 millones o cero. Pero como los riesgos se suman, la **suma de VMEs = reserva de contingencia**.

### De la suma de VMEs a la reserva
Reserva = Σ VME de los riesgos aceptados. (En el caso: $12.680.000 → redondeado a 8% de costos directos.)

**Tip que da puntos**: la reserva **debe tener una tabla detrás**, no un porcentaje al azar. "8% por costumbre" = se lee como colchón y se descuenta.

### Simulación del cronograma
Compromete el **P80** (80% de probabilidad de cumplir), planifica internamente el **P50**. La diferencia = reserva de cronograma.

**Frase clave**: comprometer el plazo determinista = prometer una fecha con 50% de probabilidad de atraso.

---

## 3.5 Responder: las 5 estrategias

**Amenazas**: **E**scalar · **E**vitar · **T**ransferir · **M**itigar · **A**ceptar.
*(Mnemotecnia: "**E**n **E**l **T**rabajo **M**e **A**poyo" — E-E-T-M-A)*

| Estrategia | Qué hace | Ejemplo |
|---|---|---|
| Escalar | lo manda arriba (fuera de mi control) | normativa corporativa |
| Evitar | cambio el diseño para que NO exista | excluyo la integración |
| Transferir | se lo paso a un tercero (pago prima) | subcontrato al que mantiene el legado |
| Mitigar | bajo P o I (sin eliminar) | prueba de concepto temprana |
| Aceptar | reconozco y reservo (activo) o solo observo (pasivo) | riesgo de certificación |

**Oportunidades**: escalar · **explotar** · compartir · **mejorar** · aceptar.

### Cómo elegir la estrategia (algoritmo de 2 preguntas)
1. ¿Quién controla el riesgo? → nosotros: evitar/mitigar · tercero: transferir · nadie: escalar.
2. ¿La respuesta cuesta MENOS que el ahorro esperado? → si no, aceptar.

**Regla de oro**: haz la acción **en la etapa más temprana posible**. El mismo dinero gastado antes compra más reducción de riesgo.

### La escalera de costo (memoriza el orden)
De más barato a más caro:
1. **Consulta** (gratis) → 2. **Supuesto** → 3. **Exclusión** → 4. Decisión de arquitectura → 5. Prueba de concepto → 6. Reserva → 7. Rehacer → 8. **Reparar en producción** (carísimo).

**Frase clave**: *gestionar el riesgo = bajarlo de peldaño*. Los 3 primeros son gratis y la gente los deja pasar porque tienen plazo (el foro cierra).

### Riesgo residual, secundario y disparador
- **Residual**: lo que queda DESPUÉS de la respuesta (nunca es cero → se financia).
- **Secundario**: el riesgo NUEVO que crea tu respuesta.
- **Disparador**: la señal que activa el plan de contingencia. *Sin disparador, el plan B nunca se activa.*

---

## 3.6 La licitación: las 5 palancas (¡sección estrella!)

Frente a un riesgo detectado en las bases, tienes **5 palancas**:
1. **Consultar** (foro — gratis, la respuesta pasa a ser parte de las bases)
2. **Suponer** (declarar número + plazo + consecuencia)
3. **Excluir** (decir qué NO incluyo)
4. **Rediseñar** (cambiar alcance/arquitectura para que desaparezca)
5. **No ofertar** (retirarse — legítimo y a veces lo correcto)

**Tip**: un riesgo que no produjo NINGUNA de estas 5 = no fue gestionado, fue "mencionado".

### Consulta que sirve vs que no sirve
- **No sirve**: "¿puede aclarar el punto 5.3?" → te responden "remítase a las bases".
- **Sirve**: cita el numeral, transcribe la frase, explica por qué es ambigua, **propone una interpretación** y pide confirmar. → te responden algo que puedes costear.

### Supuesto que protege
Debe tener **3 cosas**: un número + un plazo + una consecuencia.
- "Se asume calidad razonable" ❌
- "No más de 180.000 registros; sobre el 5% de campos vacíos, el saneamiento se cotiza aparte" ✅

### Cuándo no ofertar (señales de retiro)
Presupuesto insuficiente, multas > margen, alcance abierto sin aclarar, riesgo depende de un competidor, plazo < P95, requisito habilitante incumplido.

---

## 3.7 Del riesgo a la solución (la cadena que se evalúa)

**5 eslabones**: Riesgo → **Decisión** → **Lugar** → **Etapa** → **Evidencia**.

**Trampa**: el eslabón que más falta es la **evidencia** — no basta decir "rediseñamos", hay que señalar *en qué página de la propuesta* está el resultado.

### Orden de preferencia para resolver
**Alcance (gratis) → Requisito → Arquitectura → Operación (se paga por mes)**

**Tip**: si solo puedes atenderlo en operación, es un riesgo que aceptaste al ofertar, y hay que decirlo.

### Las 4 etapas (y qué acción va en cada una)
1. **Propuesta**: consultar, suponer, excluir, rediseñar, reservar. *(Muy barato — la mejor relación costo/beneficio.)*
2. **Implementación**: probar, prototipar, integrar temprano.
3. **Implantación**: marcha blanca, doble operación, olas, reversa.
4. **Operación**: SLA, monitoreo, continuidad. *(Mensual y permanente.)*

**Frase clave**: *un plan de riesgos sano tiene la mayoría de sus acciones en etapas 1 y 2. Si la mayoría está en 3 y 4, no es un plan de riesgos: es un plan de reparaciones.*

---

# DECÁLOGO FINAL — lo que NO puede faltarte el viernes

1. **Proyecto = temporal + único** (≠ operación). PMBOK: 5 grupos, 10 áreas, 49 procesos. Los grupos NO son fases.
2. **Requisito sin número no es requisito.** "Rápido" ❌ / "p95 < 2 s con 500 usuarios" ✅.
3. **Alcance = decidir qué NO se hace.** Lo no excluido se presume incluido.
4. **Supuesto vs Restricción** (sin verificar vs conocido). Scope creep = cliente, gold plating = proveedor.
5. **EDT: regla del 100% + regla 8/80 + no tiene secuencia.** RACI: la "A" es única.
6. **Esfuerzo ≠ Duración.** PERT beta = (O+4M+P)/6. Ruta crítica = camino más largo, holgura cero.
7. **Tamaño → Esfuerzo → Plazo → Costo.** Mides funcionalidad, no líneas de código.
8. **UCP: UUCP=UAW+UUCW, TCF=0,6+0,01Σ, EF=1,4−0,03Σ, UCP=UUCP×TCF×EF, E=UCP×CF.** EF bajo = bueno. CF: ≤2→20, 3-4→28, ≥5→replantear. Curso usa **Lectura B** (÷0,40).
9. **Riesgo (puede pasar) ≠ Problema (ya pasó).** Exposición = P×I. 5 palancas: consultar, suponer, excluir, rediseñar, no ofertar. 5 estrategias: escalar, evitar, transferir, mitigar, aceptar.
10. **Todo con número, dueño, etapa y evidencia.** Si no puedes rastrear una cifra a su origen, no es defendible.

---

**Consejo de estudio**: el caso que recorre los 3 documentos es el mismo (la municipalidad, 8 trámites, $320M, 14 casos de uso). Los números se conectan: **Requisitos/Alcance/EDT** (FEP02) → **6.355 horas** (FEP03) → **reserva $12.684.800** (FEP04). Si entiendes cómo una cosa alimenta a la siguiente, ya tienes el 70% del control.
