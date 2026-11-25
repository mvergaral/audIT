# Apuntes didácticos - cómo estudiar el control 2

Los documentos anteriores sirven como resumen. Estos apuntes nuevos están pensados para aprender: explican qué significa cada idea, qué decisión tomarías y por qué una opción es mejor que otra.

## El caso que usaremos: PagoAndes

PagoAndes es una plataforma para que ciudadanos paguen cuentas municipales por internet.

Condiciones del caso:

- 500 usuarios concurrentes.
- Portal web para ciudadanos.
- Aplicación para funcionarios.
- Integración con bancos y tarjetas.
- Disponibilidad exigida de 99,9 % mensual.
- RTO de 15 minutos.
- RPO igual a 0.
- Plazo de 6 meses.
- Presupuesto fijo.
- Pasarela bancaria contratada a un proveedor externo.

Tú eres el jefe de proyecto. En el control debes actuar como alguien que toma decisiones técnicas y económicas, no como alguien que repite definiciones.

## El método de cada sesión

Para cada tema debes responder cuatro preguntas:

1. ¿Qué problema intenta resolver?
2. ¿Cómo se aplica en PagoAndes?
3. ¿Por qué elegiría esta alternativa y no otra?
4. ¿Qué error típico podría cometer?

Después tapa la sección de solución y explícasela a otra persona o en voz alta.

## Plan hasta el lunes

### Viernes

Lee `01_fundamentos_explicados.md`. Enfócate en arquitectura, atributos de calidad, requisitos, RTO y RPO. Termina escribiendo tres requisitos medibles.

### Sábado

Lee `02_calculos_paso_a_paso.md`. Resuelve primero los ejemplos mirando la explicación y luego repite sin mirar. Practica especialmente UAW, UUCW, TCF, EF, UCP, esfuerzo y ruta crítica.

### Domingo

Lee `03_riesgos_adquisiciones_y_servidores.md` y después `04_clase_de_repaso_y_simulacro.md`. Haz el simulacro sin consultar los apuntes.

### Lunes

Repasa solo las fórmulas y diferencias que se confunden: RTO/RPO, calidad/alcance, riesgo/problema, esfuerzo/plazo, PUE/DCiE y programación/esfuerzo total.

## Fórmulas imprescindibles

```text
UUCP = UAW + UUCW
UCP = UUCP × TCF × EF
E = UCP × CF
Esfuerzo total = E / 0,40
VME = Probabilidad × Impacto monetario
PUE = Energía total / Energía TI
DCiE = Energía TI / Energía total
```

La fórmula no es suficiente: en una respuesta desarrollada debes indicar qué representa cada término y qué decisión permite tomar.
