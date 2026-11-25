# Clase de repaso y simulacro

## Cómo responder una alternativa con desarrollo

Usa siempre esta estructura:

1. Escribe la fórmula o regla.
2. Reemplaza los datos.
3. Calcula paso a paso.
4. Interpreta el resultado.
5. Explica por qué la alternativa elegida es la correcta.

En una pregunta conceptual:

1. Define el concepto.
2. Relaciónalo con el caso.
3. Descarta la alternativa confundible.

## Simulacro

### 1. Estimación

PagoAndes tiene 3 actores simples, 2 medios y 4 complejos. Tiene 2 casos simples, 4 medios y 6 complejos. Usa TCF = 1,10, EF = 0,95 y CF = 28 HH/UCP.

Calcula UAW, UUCW, UUCP, UCP, esfuerzo de programación y esfuerzo total.

### Solución guiada

```text
UAW = 3×1 + 2×2 + 4×3 = 19
UUCW = 2×5 + 4×10 + 6×15 = 140
UUCP = 19 + 140 = 159
UCP = 159×1,10×0,95 = 166,16 aproximadamente
E programación = 166,16×28 = 4.652,48 HH
E total = 4.652,48/0,40 = 11.631,20 HH
```

Interpretación: el proyecto necesita aproximadamente 11.631 horas-hombre totales bajo esas condiciones. Si el equipo solo dispone de 5.760 HH, el plan no es factible sin cambiar alcance, plazo, equipo o solución.

### 2. Ruta crítica

| Actividad | Duración | Predecesoras |
|---|---:|---|
| A Requisitos | 4 | - |
| B Arquitectura | 3 | A |
| C Desarrollo | 8 | B |
| D Integración | 5 | B |
| E Pruebas | 4 | C, D |
| F Capacitación | 2 | E |

Solución:

```text
A-B-C-E-F = 4+3+8+4+2 = 21 días
A-B-D-E-F = 4+3+5+4+2 = 18 días
```

Ruta crítica: A-B-C-E-F. Holgura de D: 3 días.

### 3. Riesgo

La pasarela puede cambiar su API. Probabilidad 30 %, impacto $5.000.000.

```text
VME = 0,30×5.000.000 = $1.500.000
```

Una buena respuesta combina mitigación técnica, como una prueba de concepto y un adaptador, con una cláusula contractual que obligue a avisar los cambios y entregar soporte.

### 4. Calidad

Redacta estos requisitos:

- rendimiento;
- disponibilidad;
- seguridad.

Ejemplos de respuesta:

> Con 500 usuarios concurrentes, el 95 % de las consultas de saldo responde en menos de 2 segundos.

> PagoAndes mantiene 99,9 % de disponibilidad mensual, excluyendo mantenimientos avisados con cinco días de anticipación.

> Todo dato personal se cifra durante transmisión y almacenamiento, y cada acceso queda registrado por 12 meses.

### 5. Adquisiciones

Explica por qué contratarías la pasarela bancaria y qué riesgos quedan.

Respuesta esperada: conviene contratarla porque ya posee conexiones y certificaciones, pero quedan dependencia, cambios de API, indisponibilidad, costo y salida del proveedor.

## Preguntas rápidas

1. ¿Por qué EF menor que 1 es favorable?
2. ¿Por qué RPO 0 no se logra con respaldo diario?
3. ¿Por qué una actividad crítica tiene holgura cero?
4. ¿Qué diferencia hay entre asegurar calidad y controlar calidad?
5. ¿Qué significa PUE = 1,25?
6. ¿Qué diferencia hay entre riesgo residual y secundario?
7. ¿Cuándo usarías comunicación asíncrona?
8. ¿Por qué microservicios pueden ser una mala decisión para un equipo pequeño?

## Lista final

- [ ] Puedo explicar cada fórmula.
- [ ] Puedo clasificar actores y casos por su peso.
- [ ] Puedo convertir programación en esfuerzo total.
- [ ] Puedo calcular ruta crítica y holgura.
- [ ] Puedo calcular VME y proponer una respuesta.
- [ ] Puedo distinguir calidad, alcance y aceptación.
- [ ] Puedo explicar RTO, RPO, PUE y DCiE.
- [ ] Puedo justificar construir versus comprar.
- [ ] Puedo escribir requisitos medibles.
