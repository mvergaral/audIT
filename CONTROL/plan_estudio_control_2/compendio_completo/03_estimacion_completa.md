# Módulo 3 - Estimación, productividad y costo

## 1. Por qué medir tamaño

Sin una medida de tamaño no se puede comparar productividad ni defender una estimación. Las métricas convierten requisitos en un número repetible.

La secuencia general es:

```text
Identificar → clasificar → ponderar → sumar → ajustar → convertir a horas
```

## 2. Puntos de Función

El método de Albrecht clasifica funciones externas e internas:

- EI: entradas externas.
- EO: salidas externas.
- EQ: consultas externas.
- ILF: archivos lógicos internos.
- EIF: archivos de interfaz externos.

Primero se calcula UFP o FP sin ajustar. Luego se aplican factores generales y se obtiene FP ajustado. La idea es la misma: medir funcionalidad antes de convertir a horas.

## 3. Puntos de Casos de Uso

### Actores: UAW

| Tipo | Peso |
|---|---:|
| Simple / API | 1 |
| Medio / protocolo | 2 |
| Complejo / GUI | 3 |

### Casos: UUCW

| Transacciones | Tipo | Peso |
|---:|---|---:|
| 1–3 | Simple | 5 |
| 4–7 | Medio | 10 |
| 8 o más | Complejo | 15 |

### Fórmulas

```text
UUCP = UAW + UUCW
TCF = 0,6 + 0,01 × Σ(factor técnico × peso)
EF  = 1,4 − 0,03 × Σ(factor ambiental × peso)
UCP = UUCP × TCF × EF
E = UCP × CF
```

## 4. Ejemplo completo

SmartGrid Andes tiene 5 actores simples, 3 medios y 9 complejos.

```text
UAW = 5×1 + 3×2 + 9×3 = 38
```

Sus casos de uso se clasifican como 3 simples, 6 medios y 4 complejos:

```text
UUCW = 3×5 + 6×10 + 4×15 = 135
UUCP = 38 + 135 = 173
```

Sus factores técnicos ponderan 55 puntos:

```text
TCF = 0,6 + 0,01×55 = 1,15
```

Sus factores ambientales ponderan 15 puntos:

```text
EF = 1,4 − 0,03×15 = 0,95
```

```text
UCP = 173×1,15×0,95 = 189 aproximadamente
```

Si el CF es 20 HH/UCP:

```text
Programación = 189×20 = 3.780 HH
```

Como programación es solo el 40 %:

```text
Esfuerzo total = 3.780/0,40 = 9.450 HH
```

## 5. Productividad y factibilidad

Si trabajan 6 ingenieros durante 10 meses, 160 horas cada mes:

```text
Capacidad = 6×160×10 = 9.600 HH
```

El esfuerzo total es 9.450 HH, por lo que cabe en plazo con 150 HH de margen.

Duración estimada:

```text
9.450/(6×160) = 9,84375 meses
```

## 6. Distribución del esfuerzo

Una distribución típica:

| Actividad | Porcentaje |
|---|---:|
| Análisis | 10 % |
| Diseño | 20 % |
| Programación | 40 % |
| Pruebas | 15 % |
| Sobrecarga, gestión y calidad | 15 % |

La programación es menos de la mitad. Por eso estimar solo el código subestima costo y plazo.

## 7. Productividad

```text
Productividad = tamaño / esfuerzo
```

Para comparar equipos, usa la misma unidad de tamaño. Si un equipo mejora su experiencia, EF puede disminuir y la productividad UCP/persona-mes puede subir.

## 8. Costo

```text
Costo = esfuerzo total × tarifa por HH
```

SmartGrid Andes:

```text
9.450 HH × USD 55 = USD 519.750
```

El costo no es automáticamente el precio de venta: pueden sumarse margen, insumos, licencias, garantías, seguros y reservas.

## Errores típicos

- Contar casos, pero no transacciones.
- Clasificar 8 transacciones como medio: 8 ya es complejo.
- Confundir EF menor que 1 con algo negativo.
- Usar esfuerzo de programación como esfuerzo total.
- Confundir tamaño, HH, personas y meses.
