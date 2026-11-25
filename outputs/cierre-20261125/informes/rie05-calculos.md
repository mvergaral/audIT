# RIE-05 y valorización de respuestas a riesgos

**Estado parcial.** El XLSX final permite trazar un costo incremental estimado para R-24 y calcular umbrales condicionales con el artículo 80. Faltan frecuencias atribuibles antes y después, pérdidas unitarias por escenario y costos incrementales de las demás respuestas. La razón definitiva queda pendiente.

## R-24. Asesoría sobre garantías contractuales de datos

`Detalle proveedores D4!A7:E7` registra M3, audIT y **CLP 3.000.000 netos** de asesoría legal. `D7:F7` indica que proveedor y régimen quedan por confirmar. El respaldo D4 4.7 identifica la asesoría como respuesta para preparar las cláusulas antes de H2. El camino alternativo de ensayo DR en sitio admisible requiere su propia valorización.

El artículo 80, FEP01 p. 41, fija 0,5 % del valor del hito por día corrido de atraso, con tope de 10 %. Para estimar un punto de equilibrio se supone que la asesoría solo reduce la probabilidad de una multa por un atraso de duración fija. El umbral para `beneficio/costo = 1` es:

`Δp = costo_incremental / [valor neto del hito × MIN(0,005 × días corridos; 0,10)]`

En la expresión, el numerador es el costo incremental positivo de CLP 3.000.000. A continuación se muestran **escenarios separados**, sin sumar H2 y H7. H2 usa `Hitos E25!G3 = D3*'Parámetros D2'!$B$14` (CLP 313.429.434). H7 usa `Hitos E25!G9 = D9*'Parámetros D2'!$B$14` (CLP 447.756.334). Un pago tardío o una decisión de contingencia no implican por sí mismos multa.

| Hito condicional | Días corridos | Exposición condicional CLP | Reducción absoluta de probabilidad de equilibrio |
|---|---:|---:|---:|
| H2 | 1 | 1.567.147 | 191,43 puntos porcentuales, inalcanzable |
| H2 | 2 | 3.134.294 | 95,72 puntos porcentuales |
| H2 | 5 | 7.835.736 | 38,29 puntos porcentuales |
| H2 | 20 o más | 31.342.943 | 9,57 puntos porcentuales |
| H7 | 1 | 2.238.782 | 134,00 puntos porcentuales, inalcanzable |
| H7 | 2 | 4.477.563 | 67,00 puntos porcentuales |
| H7 | 5 | 11.193.908 | 26,80 puntos porcentuales |
| H7 | 20 o más | 44.775.633 | 6,70 puntos porcentuales |

Los cambios de probabilidad son umbrales algebraicos. No hay evidencia de que la asesoría evite un atraso sancionable de H2 o H7 ni de sus duraciones efectivas. En H7 la ruta depende de la autorización, el sitio secundario y el ensayo con acta. La revisión final debe distinguir el costo de la asesoría, el costo incremental de la alternativa DR y los riesgos residuales de cada ruta. El cálculo de equilibrio monetario tampoco decide si omitir un control obligatorio.

## Respuestas restantes y datos que faltan

| Riesgo o respuesta | Insumo localizado | Información pendiente para calcular la razón |
|---|---|---|
| R-06, Azure Managed Redis | D4 4.7 describe Managed Redis como elección de arquitectura ya presupuestada, sin adicional identificado. | Cotizar diferencia de capacidad o migración y medir su indisponibilidad y frecuencia. Un denominador incremental cero deja la razón sin definir. |
| R-11, adhesión | Campaña A06 y comodatos incluidos en la base D2. | Costo de una intervención adicional y recupero neto atribuible después del reparto, con frecuencia y adopción verificadas. |
| R-17, refuerzo A09/A20 | H4, H7 y H12 tienen valor neto de CLP 447.756.334 por hito y exposición de multa de CLP 2.238.782 por día corrido hasta el tope. La simulación de la malla vigente tiene supuestos de tres puntos provisionales. | Horas netas aprobadas por rol/mes, tarifación de costo y una malla alternativa que mida distribución de atraso con y sin refuerzo. No convertir días hábiles CPM a corridos sin calendario. |
| R-18/R-27, ventanas y operación paralela | `Personal`, `Dotación por perfil` y `Costos` contienen dotación y calidad de referencia. D4 ubica las pruebas base en D1/D2. | Extraer solo turnos u horas incrementales y cuantificar interrupción o viajes afectados en escenarios comparables. |
| R-23, protección y pruebas | D4 atribuye Front Door/Firewall al presupuesto base y pruebas a D1. | Diferencia de costo frente a la base y frecuencia con impacto monetario de indisponibilidad, respuesta o sanción. |
| R-28, ensayo satelital | Unidades de prueba y conectividad ya presupuestadas por D4. | Costear la ampliación incremental y cuantificar transacciones tardías o no entregadas que evitaría. |

La reserva D4 de **CLP 152.699.775** procede de una regla presupuestaria del 10 % y aparece en `Parámetros corrección!B26`. `B27` fija M12 para sensibilidad, con variante M9. Sirve para ensayar liquidez, sin asignación causal por respuesta. La facilidad financiera es una partida distinta. Las exposiciones ordinales de T-16 y las probabilidades provisionales de una sola malla no suministran el par requerido de pérdidas esperadas antes y después.

Para cada respuesta, registrar `riesgo, escenario, mes, costo incremental, p sin respuesta, pérdida sin respuesta, p con respuesta, pérdida con respuesta, fuente y responsable`. Calcular la pérdida esperada evitada como `p_sin × L_sin − p_con × L_con` y dividir por el costo incremental positivo. Corregir S8 §8.3 donde afirma que cada respuesta material lleva su razón en Sobre 3 y conservar RIE-05 parcial hasta contar con el cuadro por respuesta.

[Evidencia de cálculo](rie05-calculos.json) · [Modelo financiero](../insumos-d2/documentos/AUDIT_ModeloFinanciero_3_20261125.xlsx) · Respaldo D4 consultado en el objeto Git `HEAD:Informe-3/d4/4.7-riesgos-contingencias.md`


