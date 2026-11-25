# Simulacro final - PagoAndes

Responde sin mirar los otros documentos. Justifica cálculos y decisiones.

## Parte A: teoría

1. ¿Qué diferencia hay entre arquitectura lógica y física?
2. ¿Cuándo usarías un monolito en vez de microservicios?
3. ¿Qué significa RTO de 15 minutos?
4. ¿Qué significa RPO igual a 0?
5. ¿Por qué “el sistema será rápido” no es un requisito verificable?
6. ¿Qué diferencia hay entre validar el alcance y controlar la calidad?
7. ¿Qué es una dependencia discrecional?
8. ¿Qué significa EF menor que 1?
9. ¿Cuál es la diferencia entre riesgo residual y secundario?
10. ¿Qué riesgo se transfiere al contratar una pasarela bancaria y qué riesgos nuevos aparecen?

## Parte B: cálculo

PagoAndes tiene 3 actores simples, 2 medios y 4 complejos. Además tiene 2 casos de uso simples, 4 medios y 6 complejos.

1. Calcula UAW.
2. Calcula UUCW.
3. Calcula UUCP.
4. Si TCF = 1,10 y EF = 0,95, calcula UCP.
5. Si CF = 28 HH/UCP, calcula esfuerzo de programación.
6. Calcula el esfuerzo total considerando que programación es el 40 %.
7. Compara con un equipo de 6 personas, 160 horas mensuales durante 6 meses.

## Parte C: planificación

| Actividad | Duración | Predecesoras |
|---|---:|---|
| A Requisitos | 4 | - |
| B Arquitectura | 3 | A |
| C Desarrollo | 8 | B |
| D Integración | 5 | B |
| E Pruebas | 4 | C, D |
| F Capacitación | 2 | E |

Calcula la duración total y la ruta crítica.

## Parte D: riesgo y adquisiciones

Riesgo: el proveedor bancario cambia su API. Probabilidad 30 %. Impacto $5.000.000.

1. Calcula el VME.
2. Propón una mitigación técnica.
3. Propón una cláusula contractual.
4. Identifica un riesgo residual y uno secundario.

## Parte E: calidad

Redacta:

- un requisito de rendimiento;
- un requisito de disponibilidad;
- un requisito de seguridad;
- una prueba para cada requisito;
- un criterio de aceptación para el módulo de pagos.

## Lista de comprobación antes del lunes

- [ ] Puedo calcular UAW, UUCW y UUCP.
- [ ] Puedo calcular TCF, EF y UCP.
- [ ] Recuerdo dividir por 0,40 para obtener esfuerzo total.
- [ ] Puedo encontrar una ruta crítica.
- [ ] Sé diferenciar riesgo, problema, causa y efecto.
- [ ] Sé calcular VME.
- [ ] Sé diferenciar calidad y validación del alcance.
- [ ] Sé explicar RTO, RPO, PUE y DCiE.
- [ ] Sé justificar construir versus comprar.
- [ ] Puedo redactar requisitos y criterios de aceptación medibles.
