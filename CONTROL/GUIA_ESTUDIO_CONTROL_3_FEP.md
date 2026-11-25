# FEP · Guía de estudio para el control 3

Material base: **FEP07.26 — Gestión de Costos** y **FEP08.26 — Evaluación Financiera de Proyectos**.

| Pregunta | Herramienta |
|---|---|
| ¿Cuánto debería costar el trabajo? | Estimación, presupuesto y línea base |
| ¿Cómo va la ejecución frente al plan? | Valor ganado, variaciones e índices |
| ¿Cuánto costará terminar? | EAC, ETC y TCPI |
| ¿Cuánta plata hace falta antes de cobrar? | Flujo mensual y saldo acumulado |
| ¿El negocio crea valor? | VAN, TIR y PRI |

## 1. Planificar, estimar y presupuestar

**Planificar costos** significa fijar unidades (HH, UF, pesos), precisión (redondeo), exactitud esperada (rango de error), cuentas de control de la EDT, umbrales de variación, reglas para medir avance y frecuencia de informes. Por ejemplo, la regla 50/50 acredita la mitad del valor al iniciar una tarea y la otra mitad al terminar.

**Estimar costos** significa calcular cuánto costarán los recursos de cada actividad.

| Técnica | Cómo funciona |
|---|---|
| Análoga | Usar un proyecto similar como referencia. Es rápida y depende de qué tan comparable sea. |
| Ascendente | Estimar componentes pequeños y sumar. Requiere más detalle. |
| Paramétrica | Aplicar una relación de costo por unidad. Ejemplo: 120 HH × 0,6 UF/HH = 72 UF. |
| Tres valores, PERT | (optimista + 4 × más probable + pesimista) / 6. Con 80, 100 y 150 UF resulta 105 UF. |

### Cómo aplicar las cuatro técnicas

| Técnica | Datos del ejercicio | Cálculo |
|---|---|---|
| Análoga | Un portal parecido costó 100 UF. El equipo estima que el nuevo costará 20 % más porque tiene mayor alcance. | 100 × 1,20 = **120 UF**. El ajuste viene del juicio del equipo o de un dato del enunciado. Si ambos proyectos son comparables y se supone que cuestan lo mismo, puedes usar 100 UF como aproximación. |
| Ascendente | Análisis cuesta 15 UF, desarrollo 75 UF y pruebas 30 UF. | 15 + 75 + 30 = **120 UF**. Si te dan horas y tarifas, calcula primero el costo de cada componente. |
| Paramétrica | Según datos históricos, preparar un informe cuesta 3 UF. El proyecto requiere 40 informes de complejidad comparable. | 40 informes × 3 UF/informe = **120 UF**. Si te dan el costo y la cantidad histórica, divide para obtener el costo por unidad. |
| Tres valores, PERT | El costo optimista es 80 UF, el más probable 100 UF y el pesimista 150 UF. | (80 + 4 × 100 + 150) / 6 = **105 UF**. Si el enunciado pide un promedio simple de los tres escenarios, resulta (80 + 100 + 150) / 3 = **110 UF**. |

**Cómo reconocerlas en el control.** Si partes del costo total de un proyecto parecido, es **análoga**. Si sumas partidas estimadas por separado, es **ascendente**. Si aplicas un costo por unidad a una cantidad, es **paramétrica**. Si ponderas tres escenarios con pesos 1, 4 y 1, es **PERT**. La análoga requiere justificar el ajuste cuando corresponda. Para las otras, el enunciado debe aportar los componentes, el parámetro o los tres valores.

También puedes comparar alternativas como comprar o arrendar, usar información histórica, consultar al equipo y considerar costos de calidad (prevención, evaluación y fallas).

**Determinar el presupuesto** consiste en agregar las estimaciones, distribuirlas en el cronograma y conciliar los desembolsos con el financiamiento disponible en cada fecha. Si falta caja, se pueden negociar hitos, reprogramar trabajo o buscar fondos adicionales.

- **Contingencia:** cubre riesgos identificados e inciertos. Se incluye en la línea base de costos y el director del proyecto puede gestionarla según el plan.
- **Gestión:** cubre trabajo imprevisto. Se añade a la línea base para formar el presupuesto total. Su uso requiere aprobación y la parte aprobada se incorpora a la línea base.
- **Línea base de costos:** presupuesto aprobado distribuido en el tiempo. Su acumulado suele dibujarse como una **curva S**. Alcance (EDT), cronograma y costo integran la línea base de medición del desempeño.

## 2. Valor ganado

| Sigla | Qué mide | Cómo obtenerlo |
|---|---|---|
| **BAC** | Presupuesto total de referencia | Dato o suma de paquetes |
| **PV** | Valor presupuestado del trabajo que debía estar listo a la fecha | Línea base al corte |
| **EV** | Valor presupuestado del trabajo realizado a la fecha | Presupuesto × avance real, ponderado por paquete |
| **AC** | Costo real incurrido a la fecha | Dato o suma de gastos reales |

En ejercicios con un porcentaje global ya ponderado, usa **PV = BAC × avance planificado** y **EV = BAC × avance real**. Si el plan indica gasto uniforme, la fracción de tiempo transcurrida sirve para el avance planificado. Si hay paquetes con presupuestos distintos, calcula el EV por separado y suma.

| Pregunta | Variación | Índice |
|---|---|---|
| ¿Cómo va el cronograma? | **SV = EV − PV** | **SPI = EV / PV** |
| ¿Cómo va el costo? | **CV = EV − AC** | **CPI = EV / AC** |

**EV va primero**. Una variación positiva es favorable, cero indica que vas según el plan y una negativa es desfavorable. Para los índices, el punto de referencia es 1. SV se expresa en la unidad del presupuesto. EV mide trabajo valorizado y AC mide gasto efectivo.

### Ejercicio 1 · Diagnóstico de atraso y sobrecosto

BAC = 1.000 HH, avance planificado = 50 %, avance real = 30 %, AC = 700 HH.

- PV = 500 HH y EV = 300 HH.
- SV = −200 HH y SPI = 0,60. Se completó el 60 % del trabajo que se debía haber hecho hasta la fecha.
- CV = −400 HH y CPI ≈ 0,43. Por cada HH gastada se obtuvo el equivalente de 0,43 HH presupuestadas.

### Ejercicio 2 · Adelanto con gasto favorable

BAC = $3.000 y gasto planificado uniforme en 6 meses. Al mes 3 se terminaron 6 de 10 unidades de igual presupuesto y se gastaron $1.200.

- PV = 3.000 × 3/6 = $1.500.
- EV = 3.000 × 6/10 = $1.800.
- SV = $300 y SPI = 1,2. El proyecto está adelantado.
- CV = $600 y CPI = 1,5. El trabajo realizado costó $600 menos de lo presupuestado.

Si una gráfica muestra **AC > EV > PV**, el proyecto está adelantado y tiene sobrecosto. Lee cada comparación por separado.

## 3. Pronósticos de costo

**EAC** es el costo total pronosticado al terminar. **ETC** es lo que todavía se estima gastar. Siempre se cumple **EAC = AC + ETC**. Elige según la frase del enunciado.

| Supuesto sobre el trabajo que falta | ETC | EAC |
|---|---|---|
| Se ejecutará al costo presupuestado | BAC − EV | AC + (BAC − EV) |
| Se mantendrá la eficiencia de costo actual | (BAC − EV) / CPI | BAC / CPI |
| Influirán tanto costo como cronograma | (BAC − EV) / (CPI × SPI) | AC + ETC |
| Se hizo una nueva estimación detallada | Nueva estimación | AC + nueva estimación |

Con BAC = $100.000, AC = $70.000 y EV = $40.000, si el trabajo restante sigue el presupuesto original, **ETC = $60.000 y EAC = $130.000**.

En el ejemplo de las cuatro naves, BAC = $4.000, AC = $2.800, PV = $3.000 y EV = $2.500. Si influyen plazo y costo, ETC = 1.500 / [(2.500/2.800) × (2.500/3.000)] = **$2.016** usando los índices exactos. La diapositiva marca **$2.031**, que es la alternativa más cercana al cálculo exacto. Conserva decimales hasta el final cuando puedas.

> En la diapositiva que resume los casos, el ETC combinado aparece una vez con CPI × CPI. El EAC de esa misma diapositiva y el ejercicio posterior confirman que el denominador es **CPI × SPI**.

### TCPI · Eficiencia requerida para el trabajo restante

**TCPI = trabajo restante valorizado / fondos disponibles para ese trabajo**.

- Si la meta es el presupuesto original: **(BAC − EV) / (BAC − AC)**.
- Si la meta es el costo final revisado: **(BAC − EV) / (EAC − AC)**.

Mayor que 1 implica que hay que producir más de $1 de trabajo presupuestado por cada $1 disponible. Compáralo con el CPI observado para juzgar cuánto tendría que mejorar el desempeño.

**Ejemplo con BAC.** BAC = $1.000, EV = $600 y AC = $750. TCPI = 400/250 = **1,6**.

**Ejemplo por paquetes con EAC.** Tres paquetes presupuestan $500, $4.000 y $3.000 y llevan 100 %, 75 % y 50 % de avance. BAC = $7.500. EV = 500 + 3.000 + 1.500 = $5.000. Con AC = $4.750 y EAC = $7.125, **TCPI = 2.500/2.375 ≈ 1,05**. El numerador siempre se calcula con BAC.

## 4. Del cronograma al flujo de caja

- **Costo directo:** se asigna al proyecto, como horas de desarrollo, licencias específicas o hardware.
- **Costo indirecto:** se prorratea, como arriendo o administración.
- **Costo por HH:** lo que cuesta proveer el recurso. **Tarifa por HH:** lo que se cobra al cliente.

Para cada periodo suma los recursos × costo unitario y agrega las compras en su fecha de pago. Registra los anticipos, hitos, cuotas y demás cobros en el periodo de percepción.

**Flujo neto = cobros − pagos**. **Saldo acumulado = saldo anterior + flujo neto**.

El saldo acumulado más bajo señala la necesidad máxima de capital antes de financiar. En el ejemplo de clase, el periodo 7 llega a **−USD 6.000**. En el periodo 8 se cobran USD 10.000, se pagan USD 400 y el saldo acumulado pasa a **+USD 3.600**. El saldo final es **+USD 3.200**. Para atravesar el déficit hacen falta al menos USD 6.000 bajo los supuestos del ejercicio. Si se exige caja estrictamente positiva o existen intereses, hace falta más.

En la gráfica de cobros y pagos acumulados, la diferencia vertical entre ambas curvas es la caja. Cuanto más se retrasa un hito, más tiempo se deben financiar los costos que lo preceden.

## 5. Matemática financiera

El costo de oportunidad es el rendimiento sacrificado al destinar el capital al proyecto en vez de usarlo en la mejor alternativa comparable.

| Concepto | Fórmula |
|---|---|
| Interés simple acumulado | I = P × i × n |
| Valor futuro compuesto | F = P × (1 + i)^n |
| Valor presente | P = F / (1 + i)^n |
| Cuota fija de un préstamo | A = P × i × (1 + i)^n / [(1 + i)^n − 1] |

P es el capital inicial, i la tasa por periodo y n el número de periodos. Con $1.000, 14 % anual y 3 años, el saldo es **$1.420** con interés simple y **$1.481,54** con compuesto.

- Para convertir una tasa **efectiva anual** a mensual, usa **(1 + tasa anual)^(1/12) − 1**. En el ejercicio en UF el enunciado fija 0,5 % mensual para calcular los intereses del préstamo.
- En cada cuota, **interés = saldo inicial × tasa**, **amortización de deuda = cuota − interés** y **saldo final = saldo inicial − amortización**.
- Ejemplo de clase: préstamo de $215.375 a 12 % por periodo, en 4 cuotas de aproximadamente $70.909. En la primera, interés = $25.845, amortización ≈ $45.064 y saldo ≈ $170.311. A medida que cae el saldo, baja el interés y sube la amortización.

## 6. Inflación, tasas y tipo de cambio

- **Inflación:** aumento generalizado y sostenido de precios. Puede venir de mayor demanda, aumento de costos, expansión monetaria o expectativas de alzas. El **IPC** mide la variación de precios de la canasta y sirve de base para reajustar la **UF**.
- **TPM:** referencia de la política monetaria que influye sobre el costo del crédito. El material distingue sobrecalentamiento (crecimiento rápido con presión inflacionaria), estanflación (actividad débil con inflación alta), reflación (repunte de actividad y precios asociado a estímulos) y recuperación (repunte tras la recesión).
- **Dólar:** una depreciación del peso encarece en CLP los insumos cotizados en USD. La presentación destaca el precio del cobre, el riesgo global, la diferencia de tasas con EE. UU. y el ciclo mundial del dólar.
- **Nominal y real:** (1 + tasa nominal) = (1 + tasa real) × (1 + inflación). Con tasa nominal de 10 % e inflación de 4 %, tasa real = 1,10/1,04 − 1 = **5,77 %**. Usa flujos nominales con tasas nominales y flujos reales con tasas reales, a la misma periodicidad.

## 7. Construir el flujo para evaluar

1. Ingresos operacionales − costos operacionales antes de depreciación y amortización = **EBITDA**.
2. EBITDA − depreciación y amortización contable = **EBIT**.
3. Para el flujo puro, calcula el impuesto sobre el resultado operativo gravable según los supuestos. Para el financiado, incorpora además el efecto de los intereses sobre la base imponible.
4. Resta el impuesto y vuelve a sumar los gastos contables sin desembolso.
5. Resta inversiones y capital de trabajo cuando se pagan. Suma recuperaciones y el valor de desecho, con el tratamiento tributario del enunciado.

Una plataforma de 900 UF pagada al comprarla genera una salida de 900 UF ese mes. Depreciarla en 36 meses reduce el resultado gravable en 25 UF por mes. Esos 25 UF se agregan de vuelta al convertir utilidad en flujo, ya que corresponden al costo contabilizado de la plataforma que se pagó antes.

| Flujo | Qué incluye y qué pregunta responde |
|---|---|
| Proyecto puro | Operación, impuestos e inversión sin deuda. ¿El negocio crea valor? |
| Inversionista | Efecto del préstamo, intereses y amortización del principal. ¿Cuánto rinde el capital propio? |
| Tesorería | Todos los cobros y desembolsos en sus fechas efectivas, incluido el financiamiento. ¿Alcanza la caja para pagar? |

El préstamo entra como efectivo y la devolución del principal sale como efectivo. En el modelo del curso, el principal se mueve fuera de la base imponible y los intereses se consideran al calcular el impuesto del flujo financiado.

## 8. Indicadores de evaluación

### VAN · Valor Actual Neto

**VAN = −I₀ + Σ [Fₜ / (1 + r)^t]**, donde I₀ es la inversión inicial, Fₜ el flujo neto y r la tasa de descuento por periodo.

- **VAN > 0:** supera la rentabilidad exigida y crea riqueza en dinero de hoy.
- **VAN = 0:** logra exactamente la rentabilidad exigida.
- **VAN < 0:** queda por debajo de la rentabilidad exigida.
- Entre alternativas excluyentes y comparables, se elige el **mayor VAN**.

Ejemplo: inviertes $100 y cobras $120 en un año. A 10 %, VAN = −100 + 120/1,10 = **$9,09**. La tasa de descuento representa la rentabilidad mínima exigida, o **TRMA**, frente a una alternativa de riesgo comparable. Una tasa mayor reduce el VAN de un proyecto convencional con cobros futuros positivos.

### TIR · Tasa Interna de Retorno

Es la tasa que hace **VAN = 0**. En el ejemplo anterior es **20 %**. Para flujos convencionales, si TIR > tasa exigida, VAN > 0. Puedes aproximarla probando tasas hasta que el VAN cambie de signo o con la función TIR de una planilla.

En el ejemplo de las diapositivas, con flujos −350.000, +16.000, +16.000 y +466.000, el **VAN a 7 % es aproximadamente 59.323** y la **TIR es aproximadamente 12,96 %**.

La TIR puede dar un ranking distinto al VAN si las inversiones o las vidas útiles difieren. Por ejemplo, al 10 %, invertir $1.000 y recibir $2.000 al año da TIR de 100 % y VAN de $818. Invertir $20.000 y recibir $25.000 da TIR de 25 % y VAN de $2.727. Si son excluyentes y se busca maximizar el valor, se elige el segundo. Con varios cambios de signo pueden existir varias TIR, y con todos los flujos positivos puede no existir ninguna.

### PRI, punto de equilibrio y riesgo

- **PRI simple:** primer periodo en que el acumulado recupera la inversión. En el ejemplo en USD, el acumulado va de −6.000 a +3.600 entre los periodos 7 y 8, por lo que el PRI se alcanza en el periodo 8. Si se usa PRI descontado, se acumulan flujos actualizados.
- **Punto de equilibrio:** nivel de ventas, volumen o momento en que ingresos y costos totales se igualan.
- **Rentabilidad nominal:** proporción calculada sin descontar los flujos. Revisa la base del enunciado. El cuadro de cierre del curso usa margen dividido por costo.
- **Sensibilidad:** cambia un supuesto (precio, demanda, costo o plazo) y observa la variación en VAN, TIR o PRI. También se pueden comparar escenarios pesimista, base y optimista. La matriz de riesgo ordena riesgos por probabilidad e impacto.

## 9. Ejercicio integrador en UF

La implementación dura 18 meses. Cuesta **5.000 UF** y se vende a **6.000 UF**. El markup es (6.000 − 5.000)/5.000 = **20 %**. El margen sobre ventas es (6.000 − 5.000)/6.000 = **16,67 %**.

| Mes | Hito | Cobro |
|---:|---:|---:|
| 5 | 20 % | 1.200 UF |
| 9 | 20 % | 1.200 UF |
| 13 | 25 % | 1.500 UF |
| 18 | 35 %, aceptación | 2.100 UF |

1. **Sin financiamiento**, el saldo llega a **−1.300 UF** en los meses 4, 8 y 12. Con los hitos y la compra de una plataforma de 900 UF en el mes 18, la implementación termina con saldo puro de +100 UF antes de impuestos.
2. **Con financiamiento**, se prueban 1.300, 1.350 y 1.400 UF. Las primeras dos alternativas dejan saldo negativo. Con 1.400 UF, la empresa aporta 280 y el banco 1.120.
3. **Intereses:** 1.120 × 0,5 % = **5,6 UF por mes**. En el mes 12, la caja es 1.400 − 1.300 − 12 × 5,6 = **32,8 UF**. Se pagan 100,8 UF de intereses en 18 meses y se devuelve el principal al cobrar la aceptación.
4. **Caja al mes 18:** 1.400 + 100 − 100,8 − 1.120 = **279,2 UF**. Las 1.400 UF corresponden al menor capital entre los montos probados que mantiene la caja positiva.
5. **Operación:** meses 19 a 54, con cobro de 175 UF y costo operacional de 125 UF por mes. EBITDA mensual = 50 UF. Depreciación de la plataforma = 25 UF mensuales. EBIT mensual = 25 UF. Con 27 % de impuesto en el enunciado, se debe calcular su base anual y registrar su pago cuando corresponda.
6. **Cuadro nominal:** tarifa total de 12.300 UF y costo total de 10.400 UF, incluida la plataforma. Margen del cuadro = 1.900 UF. Margen/costo ≈ **18,3 %**. El flujo puro y el flujo del inversionista tienen sus propios VAN y TIR.

### Apalancamiento

Un proyecto de un año cuesta 100 y devuelve 120. Su rentabilidad es 20 %. Si el banco aporta 80 al 10 % y el dueño pone 20, el banco recibe 88 y quedan 32 para el dueño. El dueño gana 12 sobre su aporte de 20, así que su rentabilidad es **60 %**.

Si con la misma deuda el proyecto devuelve 105, quedan 17 para el dueño. Pierde 3 sobre 20, o **−15 %**. El efecto depende de la diferencia entre la rentabilidad del negocio y el costo de la deuda.

## 10. Repaso antes del control

**Si aparecen BAC, PV, EV y AC:** calcula plan, avance y gasto al mismo corte. Compara EV con PV para cronograma y con AC para costo. Para pronosticar, identifica el supuesto sobre el trabajo restante. Para TCPI, identifica si la meta es BAC o EAC.

**Si aparecen cobros, pagos e inversión:** arma primero el flujo por periodo y el acumulado. Encuentra el valle de caja. Luego calcula el VAN con una tasa de la misma periodicidad, identifica la TIR y decide qué flujo corresponde a la pregunta.

### Autoevaluación

1. BAC = 2.000, avance planificado = 60 %, avance real = 40 %, AC = 1.000. Calcula PV, EV, SPI y CPI. Interpreta.
2. Con los mismos datos, ¿cuál es el EAC si se mantiene la eficiencia de costo?
3. Pagas 100 hoy y recibes 121 en dos años. ¿Cuál es el VAN al 10 % anual?
4. Cobros acumulados de 2.000 y pagos acumulados de 2.700. ¿Qué aporte adicional lleva la caja a cero?
5. Una inversión de 900 UF se deprecia en 36 meses. ¿En qué mes registras la salida y cuánto deprecias cada mes?
6. Con BAC = 7.500, EV = 5.000, AC = 4.750 y EAC = 7.125, calcula TCPI con ambas metas.

### Respuestas

1. PV = 1.200. EV = 800. SPI ≈ 0,67. CPI = 0,8. Hay atraso y sobrecosto.
2. EAC = 2.000/0,8 = 2.500.
3. VAN = −100 + 121/1,1² = 0. El proyecto rinde exactamente 10 %.
4. 700. Para un saldo estrictamente positivo el aporte debe superar 700.
5. La salida se registra al pagar la compra. La depreciación es 25 UF por mes.
6. Con BAC: 2.500/2.750 ≈ 0,91. Con EAC: 2.500/2.375 ≈ 1,05.
