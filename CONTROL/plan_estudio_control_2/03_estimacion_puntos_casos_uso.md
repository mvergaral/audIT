# Estimación mediante Puntos de Casos de Uso

## 1. Secuencia completa

```text
UUCP = UAW + UUCW
UCP = UUCP × TCF × EF
E = UCP × CF
Esfuerzo total = E / 0,40
```

## 2. Actores: UAW

| Actor | Peso |
|---|---:|
| Simple / API | 1 |
| Medio / protocolo | 2 |
| Complejo / GUI | 3 |

Ejemplo: dos APIs, un protocolo y tres interfaces GUI:

```text
UAW = 2×1 + 1×2 + 3×3 = 13
```

## 3. Casos de uso: UUCW

| Transacciones | Clasificación | Peso |
|---:|---|---:|
| 1–3 | Simple | 5 |
| 4–7 | Medio | 10 |
| 8 o más | Complejo | 15 |

Ejemplo: dos simples, tres medios y cuatro complejos:

```text
UUCW = 2×5 + 3×10 + 4×15 = 100
```

## 4. Factores de ajuste

```text
TCF = 0,6 + 0,01 × suma técnica ponderada
EF  = 1,4 − 0,03 × suma ambiental ponderada
```

El TCF sube cuando el sistema es técnicamente más complejo. El EF sube cuando el ambiente es desfavorable.

Interpretación del EF:

- EF menor que 1: equipo y ambiente favorables.
- EF igual a 1: ambiente neutro.
- EF mayor que 1: ambiente desfavorable.

## 5. Factor de conversión

- 0–2 factores desfavorables: 20 HH/UCP.
- 3–4 factores desfavorables: 28 HH/UCP.
- 5 o más: el proyecto debe replantearse.

El CF no se elige por gusto: representa el riesgo y la productividad esperada del equipo.

## 6. Esfuerzo y capacidad

Si el equipo tiene 8 personas, trabaja 160 horas al mes y el plazo es 6 meses:

```text
Capacidad = 8 × 160 × 6 = 7.680 HH
```

Pero si la estimación corresponde solo a programación, hay que compararla con el 40 % del esfuerzo total o convertirla a esfuerzo total mediante división por 0,40.

No confundas esfuerzo con plazo: 7.680 HH no significa automáticamente 7.680 horas calendario.

## Ejercicio completo

Para PagoAndes inventa:

- 3 actores simples, 2 medios y 4 complejos.
- 4 casos simples, 5 medios y 8 complejos.
- valores para TCF y EF.

Calcula UAW, UUCW, UUCP, TCF, EF, UCP, esfuerzo de programación y esfuerzo total.
