# Control 2 — guía definitiva FEP26

## Qué entra

Esta versión considera **todo el contenido de las presentaciones FEP01.26 a FEP06.26**, más PMBOK 6.ª edición capítulos 05, 06, 08 y 11, el estándar WBS y las lecturas de estimación.

| Fuente de clase | Materia principal | Apuntes |
|---|---|---|
| FEP01.26 | Arquitectura lógica, física, nube, continuidad, seguridad, identidad y entrega | `05`, `06` |
| FEP02.26 | Proyecto, requisitos, alcance, EDT, cronograma, estimación y costo | `02`, `03`, `04`, `09` |
| FEP03.26 | Puntos de función, UCP, factores, esfuerzo y costo | `08`, `09` |
| FEP04.26 | Riesgos PMBOK, licitación y trazabilidad riesgo-solución | `10` |
| FEP05.26 | Sala de servidores | `07` |
| FEP06.26 | Adquisiciones, contratos, economía y calidad | `11`, `12` |
| PMBOK 05/06/08/11 | Procesos e ITTO | `03`, `04`, `10`, `12`, `16` |

> Corrección importante respecto del borrador anterior: arquitectura, sala de servidores, contratos y adquisiciones **sí forman parte del temario**.

## Orden de estudio

1. `01_caso_transversal.md`
2. `02_proyecto_interesados_y_requisitos.md`
3. `03_alcance_y_EDT_PMBOK05.md`
4. `04_cronograma_PMBOK06.md`
5. `05_arquitectura_logica.md`
6. `06_arquitectura_fisica_nube_y_continuidad.md`
7. `07_sala_de_servidores.md`
8. `08_estimacion_software_UCP.md`
9. `09_costos_tarifas_y_precio.md`
10. `10_riesgos_PMBOK11_y_licitacion.md`
11. `11_adquisiciones_contratos_y_TCO.md`
12. `12_calidad_PMBOK08.md`
13. `13_caso_integrador_resuelto.md`
14. `14_banco_de_preguntas.md`
15. `15_formulas_comparaciones_y_glosario.md`
16. `16_mapa_ITTO_PMBOK.md`
17. `17_matriz_de_cobertura.md`

## Cómo usar cada apunte

Para cada técnica responde cuatro preguntas:

1. ¿Qué problema resuelve?
2. ¿Qué información necesita?
3. ¿Por qué la elegiría en lugar de otra?
4. ¿Qué cambia en alcance, arquitectura, plazo, riesgo, calidad o precio?

Para cálculos usa siempre:

```text
Datos → fórmula → reemplazo con unidades → resultado → interpretación
```

Para casos usa:

```text
Problema → concepto/proceso → decisión → justificación → consecuencia
```

## Plan intensivo hasta el lunes

### Viernes: base de gestión y estimación

- 90 min: `02` y `03`.
- 90 min: `04`, rehaciendo PERT y ruta crítica.
- 120 min: `08` y ejercicio UCP completo.
- 30 min: fórmulas correspondientes en `15`.

### Sábado: arquitectura e infraestructura

- 120 min: `05`, comparando monolito, capas, microservicios y eventos.
- 150 min: `06`, dibujando una arquitectura física y una alternativa en nube.
- 120 min: `07`, practicando TIER, redundancia, PUE/DCiE, energía, clima y rack.
- 45 min: preguntas de arquitectura y sala en `14`.

### Domingo: negocio, riesgo y calidad

- 90 min: `09`, desde esfuerzo hasta monto ofertado.
- 120 min: `10`, redactando riesgos causa-evento-efecto y respuestas.
- 120 min: `11`, contratos, TCO y decisiones hacer/comprar/arrendar.
- 120 min: `12`, calidad, ISO 25010, COQ, SLA y aceptación.
- 90 min: `13` y simulacro en `14`.

### Lunes: activación

- 45–60 min: `15` y errores del simulacro.
- 20 min: nombres y propósitos de los 22 procesos en `16`.
- 10 min: explicar en voz alta cinco comparaciones: esfuerzo/plazo, costo/precio, calidad/grado, verificar/aceptar y riesgo/problema.

No abras un tema grande por primera vez el lunes. Recuperar activamente vale más que releer pasivamente.

