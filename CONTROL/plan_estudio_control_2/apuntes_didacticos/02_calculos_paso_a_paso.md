# Cálculos paso a paso

## 1. Puntos de Casos de Uso: qué estamos midiendo

La estimación no comienza con horas. Primero medimos el tamaño funcional del sistema. La secuencia es:

```text
Actores y casos de uso → UUCP → ajustes → UCP → horas → plazo y costo
```

## 2. Actores: UAW

| Actor | Ejemplo | Peso |
|---|---|---:|
| Simple | API sencilla | 1 |
| Medio | Protocolo especializado | 2 |
| Complejo | Usuario con GUI | 3 |

PagoAndes tiene 3 APIs, 2 protocolos y 4 tipos de usuario:

```text
UAW = 3×1 + 2×2 + 4×3
UAW = 3 + 4 + 12 = 19
```

No confundas cantidad con peso: cuatro actores complejos aportan 12.

## 3. Casos de uso: UUCW

La clasificación depende de transacciones:

| Transacciones | Clase | Peso |
|---:|---|---:|
| 1–3 | Simple | 5 |
| 4–7 | Medio | 10 |
| 8 o más | Complejo | 15 |

PagoAndes tiene 2 simples, 4 medios y 6 complejos:

```text
UUCW = 2×5 + 4×10 + 6×15
UUCW = 10 + 40 + 90 = 140
```

## 4. UUCP

```text
UUCP = UAW + UUCW
UUCP = 19 + 140 = 159
```

UUCP todavía no considera complejidad técnica ni experiencia del equipo.

## 5. TCF y EF

```text
TCF = 0,6 + 0,01 × suma técnica ponderada
EF  = 1,4 − 0,03 × suma ambiental ponderada
```

### TCF

Aumenta con distribución, concurrencia, seguridad, integración y procesamiento complejo. Si TCF sube, el mismo tamaño funcional requiere más esfuerzo.

### EF

Mide el ambiente del equipo. Poca experiencia, requisitos volátiles o alta rotación lo vuelven desfavorable.

- EF < 1: favorable, reduce esfuerzo.
- EF = 1: neutro.
- EF > 1: desfavorable, aumenta esfuerzo.

## 6. UCP, horas y esfuerzo total

Supón TCF = 1,10, EF = 0,95 y CF = 28 HH/UCP.

```text
UCP = 159 × 1,10 × 0,95
UCP = 166,16 aproximadamente
```

Esfuerzo de programación:

```text
E = 166,16 × 28
E = 4.652,48 HH
```

Como programación es solo el 40 %:

```text
Esfuerzo total = 4.652,48 / 0,40
Esfuerzo total = 11.631,20 HH
```

El resto incluye análisis, diseño, pruebas, gestión, documentación y coordinación. Por eso comparar 4.652 HH contra el esfuerzo total sería incorrecto.

## 7. Capacidad del equipo

Seis personas, 160 horas mensuales durante 6 meses:

```text
Capacidad = 6 × 160 × 6 = 5.760 HH
```

Como 5.760 es menor que 11.631, el equipo no alcanza para ese alcance y plazo. Las alternativas son aumentar plazo, aumentar recursos, reducir alcance o cambiar la solución.

## 8. Ruta crítica

| Actividad | Duración | Predecesoras |
|---|---:|---|
| A Requisitos | 4 | - |
| B Arquitectura | 3 | A |
| C Desarrollo | 8 | B |
| D Integración | 5 | B |
| E Pruebas | 4 | C, D |
| F Capacitación | 2 | E |

Rutas:

```text
A-B-C-E-F = 4+3+8+4+2 = 21 días
A-B-D-E-F = 4+3+5+4+2 = 18 días
```

La ruta crítica es A-B-C-E-F. D tiene 3 días de holgura.

La actividad crítica no es necesariamente la más larga individualmente; pertenece al camino total más largo y tiene holgura cero.

## 9. VME

Riesgo: cambio de API bancaria.

```text
Probabilidad = 30 %
Impacto = $5.000.000
VME = 0,30 × 5.000.000 = $1.500.000
```

El VME sirve para comparar riesgos y dimensionar una reserva. No significa que necesariamente se gastarán exactamente $1.500.000.

## 10. PUE y DCiE

Si el recinto consume 50.000 kWh y los equipos TI 40.000 kWh:

```text
PUE = 50.000 / 40.000 = 1,25
DCiE = 40.000 / 50.000 = 0,80 = 80 %
```

PUE bajo es mejor; DCiE alto es mejor.

## Errores de cálculo que debes evitar

- Usar 10 como peso para un caso con 8 transacciones: desde 8 es complejo y pesa 15.
- Sumar actores sin multiplicar por su peso.
- Pensar que EF bajo es malo: EF bajo es favorable.
- Olvidar dividir por 0,40.
- Confundir horas-hombre con horas de calendario.
- Calcular una sola ruta y llamarla crítica sin comparar las demás.
