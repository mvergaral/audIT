# Curva S y resultado del proyecto · Notas para explicar

Apoyo para explicar las láminas 2 a 5 cuando el profesor lo pida. No es un texto para leer: son los puntos que hay que transmitir y las cifras que conviene tener a mano. Todos los montos son netos, sin IVA, en millones de pesos (M), y salen del modelo financiero del Informe 3.

> **En una frase:** el proyecto vende 9.796,8 M, cuesta 7.984,4 M y deja un VAN de 1.235,0 M. La Curva S muestra que se puede financiar sin pasar el tope de la línea de crédito y que, desde el inicio de la operación, la caja solo crece.

## Lámina 3 · Curva S

### Las tres curvas

| Curva | Qué representa | Cómo se calcula | Valor en M56 |
|---|---|---|---|
| Facturación (azul) | Lo que audIT factura a Curimón, acumulado | Hitos E-25 en su mes + mensualidades de operación | 9.796,8 M |
| Costos con intereses (roja) | Lo que cuesta ejecutar el proyecto, acumulado | Costos operativos + intereses del crédito y de la línea. No suma la devolución del crédito, porque no es costo | 8.025,3 M |
| Caja financiada (verde, punteada) | El dinero disponible a fin de cada mes | Cobros − pagos + financiamiento − intereses − devoluciones ± IVA | 1.668,2 M |

Las tres son acumuladas: cada punto suma todo lo anterior. Por eso la azul y la roja nunca bajan, y la verde sí puede bajar.

### Facturación: por qué sube en escalones

- En la implementación solo se factura cuando se cumple un hito. Entre hitos la línea queda plana.
- Cada 1 % de la implementación equivale a 46,2 M.
- Desde M21 sube en línea recta: 36 mensualidades iguales de 143,8 M.

| Hito | Mes | % | Monto |
|---|---|---|---|
| H1 | M2 | 8 % | 369,5 M |
| H2 | M4 | 7 % | 323,3 M |
| H3 | M6 | 10 % | 461,9 M |
| H4 | M10 | 10 % | 461,9 M |
| H5 | M12 | 10 % | 461,9 M |
| H6 · H8 | M13 · M14 | 5 % c/u | 230,9 M c/u |
| H7 | M16 | 10 % | 461,9 M |
| H9 · H10 | M17 · M18 | 10 % c/u | 461,9 M c/u |
| H11 | M19 | 5 % | 230,9 M |
| H12 | M21 | 10 % | 461,9 M |

La Etapa 1 suma 60 % (H1–H7) y la Etapa 2, 40 % (H8–H12). En M21 la facturación del mes es 605,7 M: H12 más la primera mensualidad.

### Costos con intereses: dónde se acelera

- **M1–M6:** arranque, entre 79 y 216 M al mes según las compras de infraestructura.
- **M7–M17:** el tramo más intenso de construcción, entre 186 y 250 M al mes. Es la parte más empinada de la curva roja.
- **M18–M20:** baja a 168–193 M al mes al cerrar el desarrollo.
- **Operación (M21–M56):** entre 114 y 132 M al mes. Por eso la pendiente roja es menor que la azul.
- **Intereses:** 40,8 M en total (39,5 M del crédito bancario y 1,3 M de la línea). Por eso la curva termina en 8.025,3 M y no en 7.984,4 M.

### Caja financiada: forma de sierra

- La caja **sube** cada vez que entra un hito y **baja** en los meses sin cobro.
- Parte con un capital inicial de 274,5 M en M1: 219,6 M de crédito bancario (80 %) y 54,9 M de socios (20 %).
- **Valles** (antes de cada cobro grande):
  - **M9: 0 M.** Es el punto crítico. Pasan tres meses sin cobros (M7–M9) con el costo más alto. Se usa la línea de crédito por **45,0 M**, bajo el tope de 50 M, y se devuelve en M10 con H4. Es el único mes en que se usa la línea.
  - **M11: 1,9 M** y **M15: 12,7 M.** Quedan muy justos, pero sin usar la línea.
- **Máximo de la implementación:** 844,9 M en M19.
- **M21:** entra H12 y se devuelve completo el crédito bancario (219,6 M). La caja queda en 835,3 M.
- **Operación:** la caja crece unos 24 M al mes, la diferencia entre la mensualidad (143,8 M) y el costo mensual. Llega a 1.668,2 M en M56.

### Momentos que hay que señalar en el gráfico

| Mes | Qué pasa | Valor clave |
|---|---|---|
| M2 | Primer cobro (H1) | Facturación 369,5 M frente a 194,7 M de costo acumulado |
| M9 | Valle de caja | Caja 0 M · línea 45,0 M de 50 M |
| M16 | Paso a producción de la Etapa 1 (H7) | Recuperación descontada: desde aquí el flujo acumulado descontado queda positivo |
| M17 | La azul supera definitivamente a la roja | Facturación 3.464,1 M frente a costos 3.254,2 M |
| M21 | Fin de la implementación (H12) e inicio de la operación | Se devuelve el crédito · caja 835,3 M |
| M56 | Cierre del horizonte | Facturación 9.796,8 · costos 8.025,3 · caja 1.668,2 M |

### Cómo leer las distancias entre curvas

- **Azul sobre roja:** audIT ha facturado más de lo que ha gastado. Las curvas se cruzan varias veces durante la implementación, porque cada hito adelanta la azul y los meses sin cobro la dejan atrás. Desde **M17** la azul queda siempre arriba.
- **Distancia final azul − roja: 1.771,5 M.** Es el margen del proyecto (1.812,4 M) menos los intereses (40,8 M).
- **La verde no es igual a esa distancia**, y se puede explicar con exactitud:

| Concepto | M |
|---|---:|
| Distancia azul − roja en M56 | 1.771,5 |
| + Aporte de socios, que queda en la caja | 54,9 |
| − Mensualidad de M56, que se cobra en M57 (pago mes vencido, E-25) | −143,8 |
| − IVA de enlaces LTE y ExpressRoute, modelado sin crédito fiscal | −14,4 |
| **= Caja financiada en M56** | **1.668,2** |

## Lámina 2 · Resultado del proyecto

### Qué transmitir

- **Precio construido desde el costo:** a cada fase se le aplica un margen de 18,5 % sobre la venta. La métrica de las bases es EBITDA sobre ingresos netos, con un tope de 20 %.
- **El VAN es el indicador principal.** Se calcula sobre el flujo del proyecto, mes a mes del 1 al 56, sin intereses ni IVA. Los intereses ya están considerados en la tasa.
- **La tasa sale del financiamiento del E-24:** 80 % crédito al 0,9 % mensual y 20 % socios al 20 % anual, que en mensual compuesto es 1,531 %. El resultado es 1,026 % mensual, cerca de 13,0 % anual.
- **La TIR es alta y hay que explicarla, no esconderla:** H1 entra en M2 con 369,5 M, cuando el gasto acumulado es 194,7 M. Los hitos financian la construcción, y por eso la TIR es muy sensible al calendario.

### Valores

| Indicador | Valor | Qué significa |
|---|---|---|
| Venta neta | 9.796,8 M | Implementación 4.618,8 M + operación 5.178,0 M |
| Costo neto | 7.984,4 M | Implementación 3.764,3 M + operación 4.220,1 M. Personal: ~78 % |
| Margen | 18,50 % | (Venta − costo) / venta = 1.812,4 M. Tope de 20 % |
| Tasa de descuento | 1,026 % mensual | ≈ 13,0 % anual |
| VAN M0–M56 | 1.235,0 M | Valor que agrega el proyecto sobre el costo del capital |
| Recuperación descontada | M16 | Coincide con el paso a producción de la Etapa 1 |
| Venta de equilibrio (VAN = 0) | 8.175,2 M | La venta podría bajar 1.621,6 M (16,6 %) antes de destruir valor |
| TIR | 83,7 % mensual | Solución única, pero dominada por los primeros meses |

## Lámina 4 · Lectura de la Curva S

Resume la lámina 3 en cuatro cifras. Si ya se explicó el gráfico, basta con recorrerlas rápido:

- **Facturación, 9.796,8 M:** 12 hitos y 36 mensualidades.
- **Costos con intereses, 8.025,3 M:** costo neto más 40,8 M de intereses.
- **Valle de M9, 0 M:** la línea cubre 45 M, bajo el tope de 50 M.
- **Caja al cierre, 1.668,2 M:** positiva desde M21 hasta el final.

## Lámina 5 · Sensibilidad

### Qué transmitir

- El **VAN** se mantiene positivo en todos los escenarios. Lo que hay que vigilar es la **caja** si se atrasa un cobro.
- La caída de la TIR, de 84 % a 17 %, con solo 5 % de cambio confirma que hay que decidir con el VAN.

| Escenario | VAN | TIR mensual | Efecto en la caja |
|---|---:|---:|---|
| Base | 1.235,0 M | 83,7 % | Valle de 0 M en M9, línea de 45 M |
| Costos +5 %, precio fijo | 923,7 M | 17,3 % | — |
| Cobros −5 % | 862,0 M | 16,6 % | — |
| H5 cobrado en M13 | 1.230,9 M | 83,0 % | Déficit de 155,7 M en M12, con la línea al tope |
| H5 en M13 + uso de la reserva de infraestructura | 1.095,8 M | 82,5 % | Déficit de 308,4 M en M12 antes del refuerzo |

- **Respuesta al escenario de estrés:** un refuerzo de 400 M desde M1 (320 M de crédito y 80 M de socios) deja una caja mínima de 11,2 M en M12, sobre la meta de 10 M. Ese financiamiento está modelado, pero su disponibilidad y sus condiciones aún se deben confirmar.

## Preguntas probables

**¿Por qué la caja llega a cero justo en M9?**
Es el tercer mes seguido sin cobros (entre H3 en M6 y H4 en M10) y coincide con el mayor costo mensual. El capital inicial se dimensionó para que ese valle quede cubierto con la línea bajo el tope.

**¿Por qué la curva de costos incluye intereses y no la devolución del crédito?**
Así lo definen las bases para la Curva S: los intereses son costo del financiamiento. Devolver el capital no es un costo, solo un movimiento de caja, y por eso aparece en la curva verde.

**¿Por qué el VAN no usa la caja financiada?**
El VAN mide si el negocio es rentable por sí mismo. Usa el flujo del proyecto, sin financiamiento ni IVA. La caja financiada responde a otra pregunta: si cada mes hay dinero disponible.

**¿Por qué no usan 20 % como tasa?**
El 20 % es el tope de rentabilidad. La tasa es el costo del capital (≈ 13 % anual). Si se descontara al 20 %, un proyecto en el tope tendría un VAN de cero.

**¿Por qué la tabla Resumen de la plantilla muestra 22,7 %?**
Esa celda divide la utilidad por el costo. Las bases miden utilidad sobre venta: 18,5 %. La hoja Resumen no se puede modificar, así que la diferencia se aclara en el Resumen Ejecutivo.

**¿Qué pasa con el cobro de M57?**
La operación se paga mes vencido. El servicio de M56 (143,8 M) se cobra en M57 y queda fuera del horizonte y del VAN base. Si se incluyera, el VAN subiría a unos 1.315 M.

**¿El hardware de los camiones está en los costos?**
No. Lo compra Curimón (~225 M) y va en una hoja informativa fuera del flujo, como indican las aclaraciones. Sí se incluyen la instalación y la sala técnica.

**¿Qué falta para la oferta final?**
Conciliar las horas de personal con el plan de trabajo, incorporar el overhead de la empresa y los seguros pendientes, confirmar el financiamiento de estrés y cuantificar los beneficios de las innovaciones para Curimón.
