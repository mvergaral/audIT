# 3.7 · Valorización de la innovación 2

**Innovación:** programación de intervenciones por oportunidad de patio, EDT 12.2. **Fecha:** 12-11-2026.

## Inversión de desarrollo

| Perfil | Horas propuestas | Costo de referencia UF/h | Costo atribuido CLP |
|---|---:|---:|---:|
| Arquitectura | 40 | 1,10 | 1.760.000 |
| Software sénior | 176 | 0,70 | 4.928.000 |
| Frontend/móvil sénior | 64 | 0,70 | 1.792.000 |
| Seguridad | 32 | 1,10 | 1.408.000 |
| Datos | 64 | 0,80 | 2.048.000 |
| QA sénior | 104 | 0,50 | 2.080.000 |
| SRE | 80 | 0,80 | 2.560.000 |
| **Total** | **560** | | **16.576.000** |

Son costos internos ilustrativos, puntos medios de E-26, no tarifas de venta ni sueldos acreditados. Rango total: $13.184.000–$19.968.000, UF contractual $40.000. D2 debe sustituirlos por sus costos seleccionados. Reproducción: datos/presupuesto_d3.json y calculo/calcular_d3.py.

Las 560 h se proponen dentro de las 2.560 h de innovaciones T-15. En el flujo son RRHH de implementación; en Innovaciones se muestran como atribución a 12.2, sin sumarlas nuevamente. **Gasto RRHH adicional sobre T-15: no determinado hasta nivelación**, no $16.576.000 extra por defecto.

| Mes | Horas | Actividad dominante |
|---|---:|---|
| M4 | 80 | Contratos de entradas y diseño determinista |
| M5 | 168 | Planificador/tablero y ensayo de agente/reversa |
| M6 | 128 | Laboratorio y piloto de diez camiones, medición manual comparable |
| M7 | 56 | Correcciones e integración autorizada |
| M8 | 24 | Ajuste de reglas e interfaz |
| M9 | 32 | Regresión y cierre de montaje propio |
| M16 | 40 | Revalidación de agente, permisos y entradas |
| M17 | 8 | Correcciones del escalamiento |
| M18 | 24 | Regresión y acta de cierre |

La preparación M4–M5 de 12.2 habilita el piloto M6; se conservan montaje M6–M9 y continuación M16–M18. QA validará laboratorio, reintentos y reversa. Las pruebas físicas requieren el trabajo de firmware y campo de D4, con imputación única de las jornadas.

## Operación

Propuesta nominal M21–M56: SRE 4, Software 4, Seguridad 2, Datos 2 y QA 4 h/mes; **16 h/mes y 576 h en 36 meses**. Es una revisión mensual de servicio/despliegue, reglas, autorización, calidad de entradas y regresión, no atención ilimitada de incidentes.

Costo atribuido de referencia: $472.000/mes y $16.992.000 en 36 meses; rango $368.000–$576.000/mes. SRE/Seguridad irían a 13.2 y el resto a 13.4. D2 debe demostrar capacidad del mismo perfil: si se absorbe, ya está en RRHH base; si falta, se agrega solo el déficit. D4 incluyó el cómputo auxiliar en 4.2 §5 y asignó la capacidad adicional de actas, twin y paquetes de esta innovación a su reserva del 10 % (4.7, commit b8adac2). Se adopta como supuesto presupuestario sujeto al consumo real, sin cargo cloud separado ni equivalencia con consumo cero. No se cobra otra vez conectividad, kit estándar, stock contractual ni soporte físico.

## Beneficio de Curimón pendiente de cuantificar

El Artículo 29.5 (FEP01 p.19) exige impacto económico **estimado** y beneficio esperado. Para el avance del Informe 3 se puede formular una proyección con hipótesis justificadas; no se exige disponer hoy de resultados medidos del piloto contractual M6. La medición y el acta del piloto pertenecen a la verificación futura de la solución, no son una condición que D3 añada para poder preparar el presupuesto actual.

El Caso no entrega preparación desperdiciada ni visitas adicionales causadas por la programación manual. El **caso base monetario prudente de D3 sigue en $0**, mientras no se documente una proyección causal atribuible a Curimón; significa beneficio no cuantificado en ese escenario, no ausencia de utilidad ni necesidad de ejecutar el proyecto antes de estimarlo.

Para Curimón, el beneficio bruto mensual estimado se expresa como:

`visitas adicionales evitadas cuyo costo asumiría Curimón × costo incremental evitado por visita + minutos evitados de recursos de Curimón × costo operativo por minuto`.

Cada término debe indicar volumen elegible, frecuencia, comparación manual, mejora supuesta y responsable de pagar el costo evitado. Si se monetiza el mismo recurso en una visita evitada, sus minutos no se vuelven a sumar como otro ahorro. Se excluyen paradas normales, visitas que no habrían ocurrido e instalación obligatoria sin inmovilización adicional. Inversión y operación van en sus filas; no se restan otra vez dentro del beneficio bruto.

La instalación es trabajo interno de audIT, conforme a las aclaraciones del Informe 3 §9 y al reparto económico de D4. Por tanto, tiempo liberado de esos técnicos se trata como capacidad o costo evitado de audIT, según su efecto real de caja. No se atribuye automáticamente a Curimón ni se suma como ingreso de audIT. Si un ahorro se traslada al cliente mediante un precio menor, se documenta una sola vez y no se duplica como beneficio independiente.

El criterio vigente de D1, publicado en el commit **8967f18** el 13-11-2026, retira la sensibilidad monetaria anterior de la innovación 2 por falta de respaldo para atribuir ese ahorro a Curimón. Se mantiene **$0 reconocido en el caso base y el beneficio monetario pendiente de cuantificar**, sin importe alternativo activo en la tabla de beneficios o en el flujo. Las horas de instalación liberadas siguen correspondiendo a audIT según su efecto real, no automáticamente a Curimón.

Una futura estimación debe derivarse de los parámetros causales y del pagador de cada costo evitado, con una comparación trazable; no se parte de una cifra objetivo para fabricar sus supuestos. Las metas físicas y la fórmula anterior se conservan como método de estimación y medición. Retirar el monto no elimina la utilidad propuesta ni modifica las 560 h y los costos de implementación/operación. La cobertura del personal sigue siendo una conciliación distinta con D2.

El beneficio del cliente se presenta separado de los costos y de los ingresos de audIT. La inversión y el costo incremental de la innovación se calculan por separado.

## Evidencia y carga

En la ejecución contractual se prevé registrar en M6 cada oportunidad: terminal/familia, autorización, ventana, kit, técnico, preparación, cancelación/causa, visita adicional real, costo y resultado. El plan manual se registra antes de la recomendación. Se compara la misma muestra separando no comparables y unidades sin autorización. Sin esa muestra o compatibilidad del agente no se acredita una reducción observada ni el escalamiento operativo. Esto se distingue de la estimación del Informe 3. La meta técnica −20 % de preparación inútil no se aplica automáticamente a todos los costos de patio.

| Clave económica | Valor de referencia | Entrada al flujo |
|---|---|---|
| innovacion-2-inversion | Atribución $16.576.000, sustituible por costo de D2 | Reconciliar 560 h con RRHH; no duplicar |
| innovacion-2-costo | Atribución de personal $16.992.000 en 36 meses; nube en presupuesto/reserva D4, sin sumar otra partida | Agregar únicamente déficit de personal conciliado con D2; conservar explícito el supuesto de cobertura cloud de D4; total todavía abierto |
| innovacion-2-beneficio | Base prudente $0 reconocido; beneficio monetario pendiente de cuantificar, sin sensibilidad numérica activa, según D1 en 8967f18 | Hoja de beneficios del mandante, fuera de ingresos de audIT; no cargar el monto retirado ni interpretarlo como ahorro cero demostrado |

**Fuentes:** S13 §13.2/T-19 ficha 2; S7/T-14, 12.2; T-15, 2.560 h; FEP01 Art.29.5, p.19; E-24 p.73/E-26 p.76; paquete económico D1 §1.3 y textos LaTeX económicos, commit 8967f18; Aclaraciones Informe 3 §§1, 5 y 9; D4, 4.8-compras-audit-y-mandante.md §1.
