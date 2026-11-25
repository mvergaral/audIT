# Aviso de D4 a D2: hitos sin margen en la malla conciliada

| Dato | Valor |
|---|---|
| Fecha | 2026-11-24 |
| De | D4 (S8, riesgos) |
| Para | D2 (S7, T-14, T-15, T-18) |
| Malla revisada | `subdocumentos/07-plan-trabajo/graficos/conciliacion-3.2/red-calculada.json` en `main` (5011546) |
| Guion | `Informe-2/D4/riesgos/montecarlo32.py` (salida `montecarlo32.json`) |
| Decisión de D4 | D4-161 y D4-162 |

## 1. Hallazgo

En la malla conciliada, cuatro hitos de pago terminan justo en su límite contractual, sin días de margen:

| Hito | Límite | Margen en la malla | Cadena sin holgura que lo determina |
|---|---|---|---|
| H4 | Día 200, M10 | 0 | A09-1 a A09-8 (ocho sprints de 10 días) y R-H4 |
| H7 | Día 320, M16 | 0 | A15 (ventana fija de 60 días), A19 (10 días) y R-H7 |
| H11 | Día 360, M19 | Reserva A23 de 10 días | A17, A20-1 a A20-5, A22-SIS y R-H10 |
| H12 | Día 420, M21 | 0 | H11, A24 (40), A25 (10) y R-H12 |

En la red anterior, H4 tenía 8 días, H7 tenía 10 y H12 quedaba protegido por A23.

## 2. Efecto en la simulación

El S7 pide recalcular las probabilidades sobre esta malla y no trasladar las de la red anterior. D4 la simuló con 10.000 corridas, semilla 2026, hitos, revisiones R-H* y ventanas fijas, y Beta-PERT en el resto del trabajo:

| Regla de tres puntos | H4 | H6 | H7 | H11 | H12 | Ambas marchas blancas |
|---|---|---|---|---|---|---|
| 0,85 / 1 / 1,4 | 5,9 % | 35,7 % | 5,8 % | 6,3 % | 2,1 % | 4,4 % |
| 0,90 / 1 / 1,2 | 17,2 % | 95,0 % | 17,3 % | 16,8 % | 11,4 % | 16,3 % |
| 0,95 / 1 / 1,1 | 19,5 % | 100 % | 18,0 % | 17,3 % | 16,1 % | 17,3 % |

Con la red anterior, ambas marchas blancas a tiempo daban 92,1 %. Un hito sin margen se cumple como máximo en la mitad de los escenarios, porque cualquier variación de su cadena lo atrasa. Por eso el resultado casi no depende de la regla.

## 3. Qué hizo D4 en el S8

- Sacó todas las probabilidades de la red anterior (78,4 %, 92,1 %, 82,3 % y las demás).
- Reemplazó la tabla de la simulación por el margen de cada hito y la actividad que lo determina.
- Subió R-17 («Margen de los hitos de pago») a exposición alta (4 × 3 = 12), con contingencia: refuerzo de los sprints de A09 o A20 desde la reserva de gestión y entrega con el alcance comprometido y acta de la Contraparte Técnica.
- Dejó como respuesta un ajuste de la malla antes del H1 y una nueva simulación con las tres estimaciones validadas por los ejecutores.
- Actualizó las holguras citadas: capacitación 8 días, A21-PATIO 15, A21-LEG 10. Piloto, lotes, A18-INT y A15 son ventanas fijas sin holgura.

## 4. Qué se necesita de D2

1. Revisar si se puede devolver margen a H4, H7, H11 y H12 sin mover las fechas fijas del Art. 17.1. Por ejemplo: adelantar el inicio de A09 o de A20, acortar la cadena de sprints con más capacidad o mover A19 antes del cierre de la marcha blanca.
2. Si la malla cambia, avisar a D4 para correr `montecarlo32.py` de nuevo y publicar las probabilidades en el S8.
3. Corregir la nota de la planilla sobre el montaje. El S7 (líneas 359 y 421) y la malla (A21-PATIO: «sin montajes iniciales») dejan los 182 equipos montados en M9, y M17–M19 queda para validar reglas de patio y acople, cerrar recepciones y reponer por excepción. La nota C83 de la planilla 3.2 todavía dice «instalación de etapas 1 y 2 (M7-M9 y M16-M18 según T-14 y S4)», y la hoja «Conciliación técnica» A17 dice «Técnico M18–M20». El costo no cambia, porque el técnico sigue hasta antes de M19, pero el texto de la nota contradice al S7. D4 alineó S4, S12, S13, T-19 y R-19/R-31 del T-16 con el S7.

## 5. Archivos de D4 que dependen de esto

- `subdocumentos/08-riesgos/contenido.tex`: simulación, escalas, reservas, cierres del paso y contingencias.
- `subdocumentos/08-riesgos/formularios/T-16.tex`: R-17 y R-34 (generado por `Informe-2/D4/riesgos/registro.py`).
- `subdocumentos/14-ventajas/contenido.tex`: equilibrio de tiempo.
- `subdocumentos/04-arquitectura/contenido.tex`, `12-equipo/contenido.tex`, `13-innovaciones/contenido.tex` y ficha 3 del T-19: calendario de montaje.
