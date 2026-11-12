# 3.7 · Valorización de la innovación 2

**Tarea:** AUD-30. **Innovación:** programación de intervenciones por oportunidad de patio, EDT 12.2. **Reciben:** D2/AUD-16 y D1/AUD-9/AUD-12. **Fecha:** 12-11-2026. **Estado:** costo atribuido y escenarios preparados; cierre pendiente de capacidad, nube y consolidación.

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

D2 debe hacer visible la preparación M4–M5 dentro de 12.2 para llegar al piloto M6; se conservan montaje M6–M9 y continuación M16–M18. No se afirman homologación o piloto ejecutados. QA valida laboratorio/reintentos/reversa; las pruebas físicas del equipo requieren firmware y campo ya presupuestados, que se concilian con D4 para no duplicar jornadas.

## Operación

Propuesta nominal M21–M56: SRE 4, Software 4, Seguridad 2, Datos 2 y QA 4 h/mes; **16 h/mes y 576 h en 36 meses**. Es una revisión mensual de servicio/despliegue, reglas, autorización, calidad de entradas y regresión, no atención ilimitada de incidentes.

Costo atribuido de referencia: $472.000/mes y $16.992.000 en 36 meses; rango $368.000–$576.000/mes. SRE/Seguridad irían a 13.2 y el resto a 13.4. D2 debe demostrar capacidad del mismo perfil: si se absorbe, ya está en RRHH base; si falta, se agrega solo el déficit. Nube/actas/paquetes/operaciones IoT se concilian con D4 por separado. No se cobra otra vez conectividad, kit estándar, stock contractual ni soporte físico.

## Beneficio de Curimón y sensibilidad

El Caso no entrega preparación desperdiciada ni visitas adicionales realmente causadas por la programación manual. El **caso base monetario prudente es $0** hasta justificar parámetros; significa ahorro no acreditado, no ausencia de utilidad.

Beneficio bruto mensual = visitas adicionales efectivamente evitadas × costo unitario de visita + minutos de preparación efectivamente evitados × costo por minuto.

Se excluyen paradas normales, visitas que no habrían ocurrido e instalación obligatoria sin inmovilización adicional. Inversión y operación van en sus filas; no se restan otra vez dentro del beneficio bruto. Los ahorros son de Curimón y no ingresos de audIT.

El paquete económico D1 incluye **$30.000.000/año por patio**, $90.000.000 en 36 meses. D3 no encontró su derivación en cantidades/costos ni acta de línea base. Ese importe puede mantenerse como **hipótesis de sensibilidad**, $2.500.000 mensuales M21–M56, hasta demostrar el cálculo. No se valida como beneficio consolidado. D1 debe conciliarlo con el escenario prudente antes de publicar el total global.

## Evidencia y carga

En M6 se registra cada oportunidad: terminal/familia, autorización, ventana, kit, técnico, preparación, cancelación/causa, visita adicional real, costo y resultado. El plan manual se registra antes de la recomendación. Se compara la misma muestra separando no comparables y unidades sin autorización. Sin muestra o compatibilidad del agente no se escala ni acredita reducción monetaria. La meta técnica −20 % de preparación inútil no se aplica automáticamente a todos los costos de patio.

| Clave económica | Valor de referencia | Entrada al flujo |
|---|---|---|
| innovacion-2-inversion | Atribución $16.576.000, sustituible por costo de D2 | Reconciliar 560 h con RRHH; no duplicar |
| innovacion-2-costo | Atribución $16.992.000 en 36 meses; nube pendiente | Agregar únicamente déficit de personal y consumo adicionales; total todavía abierto |
| innovacion-2-beneficio | Base prudente $0; sensibilidad D1 $90.000.000/36 meses | Hoja de beneficios del mandante, fuera de ingresos de audIT |

El archivo común economico/datos/partidas.csv sigue sin cifras de innovación 2 porque falta conciliar el costo incremental neto. No se sustituyen faltantes por costo atribuido para aparentar cierre. Las dependencias FF AUD-24/AUD-26 siguen abiertas.

**Fuentes:** S13 §13.2/T-19 ficha 2; S7/T-14, 12.2; T-15, 2.560 h; E-24 p.73/E-26 p.76; paquete económico D1, Beneficios; Aclaraciones Informe 3 §§1 y 5. Esta tarea no modifica S13, T-19 ni los valores de D1.
