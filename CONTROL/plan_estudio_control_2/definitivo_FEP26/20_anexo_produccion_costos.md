# Anexo - Producción, costos y decisiones de la empresa

Este anexo recoge la teoría económica del resumen didáctico disponible en la carpeta. Ayuda a relacionar productividad, costo y beneficio, y a distinguir costo de producción de precio de venta.

## Empresa, producción y beneficio

La empresa transforma factores productivos en bienes o servicios. El trabajo se representa por `L`, el capital por `K`, la producción por `Q` y el precio por unidad por `P`. El ingreso total es `IT = P × Q`; el beneficio es `π = IT − CT`. La decisión económica busca maximizar el beneficio, no producir la mayor cantidad posible sin considerar el costo.

**Corto plazo** significa que al menos un factor está fijo para la decisión analizada. No significa necesariamente menos de un año. **Largo plazo** permite variar todos los factores, incluso el tamaño de planta o el capital.

## Productividad: producto total, medio y marginal

- **Producto total (PT):** la cantidad producida, `Q = f(L,K)`. En el corto plazo, `K` se mantiene fijo.
- **Producto medio del trabajo (PMeL):** producción promedio por unidad de trabajo, `Q/L`.
- **Producto marginal del trabajo (PMgL):** cuánto cambia la producción al añadir trabajo, `ΔQ/ΔL` en datos discretos o `dQ/dL` con una función continua.

El producto marginal es la pendiente del producto total. Si `PMgL > PMeL`, el promedio sube; si `PMgL < PMeL`, baja. Es la misma lógica de un promedio de notas: una observación superior al promedio lo eleva.

En una función típica aparecen tres regiones: al principio la especialización puede elevar el producto marginal; después el producto total sigue subiendo con productividad marginal decreciente; finalmente alcanza un máximo y puede caer. La región económicamente racional se ubica donde el producto marginal es decreciente pero todavía positivo. El punto exacto depende de precios y costos.

### Ejemplo de los puntos técnicos

Para `Q(L) = L + 2L² − 3L³`:

```text
PMgL = dQ/dL = 1 + 4L − 9L²
Máximo del PMgL: d²Q/dL² = 4 − 18L = 0 → L1 = 2/9 ≈ 0,222
Máximo del PMeL: PMeL = Q/L = 1 + 2L − 3L²; d(PMeL)/dL = 2 − 6L = 0 → L2 = 1/3 ≈ 0,333
Máximo del PT: 1 + 4L − 9L² = 0 → L0 = (2 + √13)/9 ≈ 0,623
```

Por tanto, `L1 < L2 < L0`. `L2` es el óptimo técnico (máximo producto medio); `L0` es el máximo técnico (máximo producto total). Más allá de `L0`, el producto marginal es negativo.

## Costos de corto plazo

`CT = CF + CV`: el costo total suma costo fijo y costo variable. El costo fijo no cambia con la cantidad producida mientras se mantenga la planta; el variable sí cambia. Los costos medios son `CMe = CT/Q`, `CVMe = CV/Q` y `CFMe = CF/Q`, por lo que `CMe = CVMe + CFMe`. El costo fijo medio cae a medida que se reparte entre más unidades.

El **costo marginal** (`CMg`) mide el costo de una unidad adicional: `ΔCT/ΔQ` o `dCT/dQ`. Como el costo fijo no cambia con `Q`, también puede calcularse como `dCV/dQ`. En las curvas habituales, el CMg corta al CVMe y al CMe en sus mínimos. Si el CMg está bajo el costo medio, lo empuja hacia abajo; si está sobre el promedio, lo empuja hacia arriba.

La intuición conecta productividad y costos: si cada trabajador adicional produce mucho, cuesta relativamente poco obtener una unidad más. Cuando cae la productividad marginal, el costo marginal tiende a subir.

### Ejemplo de costo y beneficio

Con `Q = 2√(LK)`, capital fijo `K = 25`, salario `w = 2` y renta del capital `r = 4`, resulta `Q = 10√L`, de donde `L = Q²/100`. El costo es `CT = wL + rK = 2L + 100`, así que `CT(Q) = Q²/50 + 100`. Si `P = 100`:

```text
π(Q) = IT − CT = 100Q − Q²/50 − 100
dπ/dQ = 100 − Q/25 = 0 → Q* = 2.500
L* = Q²/100 = 62.500
IT = $250.000; CT = $125.100; πmáx = $124.900
```

El máximo de producción no es automáticamente el máximo beneficio: la decisión incorpora ingreso y costo marginales.

## Largo plazo: isocuantas e isocostos

Una **isocuanta** reúne combinaciones de `L` y `K` que producen la misma cantidad. Una isocuanta más alejada del origen representa mayor producción. Su pendiente es `−PMgL/PMgK`; su valor absoluto expresa la tasa marginal de sustitución técnica.

Una **recta de isocosto** muestra combinaciones de factores con igual costo: `CT = wL + rK`. Despejando `K`, `K = CT/r − (w/r)L`; su pendiente es `−w/r`, con interceptos `CT/r` y `CT/w`.

Con presupuesto dado, la empresa elige la isocuanta más alta que puede alcanzar. En el óptimo interior, la isocuanta es tangente al isocosto:

```text
PMgL / PMgK = w / r
equivalentemente: PMgL / w = PMgK / r
```

Esto iguala el producto marginal por peso gastado en cada factor. Si no fueran iguales, convendría mover gasto hacia el factor que aporta más producción por peso.

### Ejemplo de elección de factores

Para `Q = 2√(LK)`, con `w = 4`, `r = 6` y presupuesto `$120.000`, la condición de tangencia da `K/L = w/r = 2/3`. Junto con `4L + 6K = 120.000`:

```text
K = (2/3)L
4L + 6(2L/3) = 120.000 → L* = 15.000; K* = 10.000
Q* = 2√(15.000 × 10.000) ≈ 24.494,90
```

Para obtener una producción dada al menor costo, se busca la combinación de factores sobre la isocuanta objetivo que toque el isocosto más bajo. Ejemplo: con `Q = √(KL)`, `w = 2`, `r = 8` y `Q = 128`, la combinación `L = 256`, `K = 64` produce 128 y cuesta `$1.024`.

## Otros ejemplos de beneficio y contenidos de mercado

Si el requerimiento de trabajo es `L(Q) = 8Q − 6Q² + 3Q³`, con `w = 1` y `P = 8`, entonces `π(Q) = 8Q − L(Q) = 6Q² − 3Q³`. La condición de primer orden produce `Q = 0` o `Q = 4/3`; la solución interior relevante da `π = 32/9 ≈ 3,56`.

Un **precio máximo** es un límite legal al mayor precio permitido. Si queda bajo el precio de equilibrio, aumenta la cantidad demandada, reduce la cantidad ofrecida y crea o agrava escasez; el control por sí solo no garantiza atender a quienes más lo necesitan.

Las elasticidades miden respuestas porcentuales:

```text
Elasticidad-precio de demanda: Ed = %ΔQd / %ΔP
Elasticidad-ingreso: Ey = %ΔQd / %ΔY
Elasticidad cruzada: Exy = %ΔQx / %ΔPy
```

`|Ed| > 1` indica demanda elástica; `< 1`, inelástica; `= 1`, unitaria. `Ey > 0` caracteriza un bien normal y `Ey < 0`, uno inferior. `Exy > 0` indica sustitutos y `< 0`, complementarios.

## Errores que evitar

- Definir corto plazo por una cantidad fija de meses; depende de si algún factor está fijo.
- Confundir producto marginal con producto medio o máximo técnico con máximo beneficio.
- Olvidar que `CFMe` se reduce al aumentar la producción.
- Confundir el mínimo del costo marginal con los mínimos de los costos medios.
- Elegir una combinación de factores que no cabe en el presupuesto.
- Omitir el signo negativo de las pendientes de isocuanta e isocosto.
