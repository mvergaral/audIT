# Aporte D3 al Informe 3: innovación 2

**Destino:** documento de costos frente a venta y planilla mensual del Informe 3. **Base técnica:** S13, innovación 2 y ficha 2 de T-19. Las tres partidas ya existen, sin valor, en `economico/datos/partidas.csv` (`innovacion-2-inversion`, `innovacion-2-costo`, `innovacion-2-beneficio`). D3 no dispone de cotizaciones, tarifas internas ni una línea base medida; por eso aquí no se asignan montos ficticios.

## Qué se valoriza

| Partida | Cantidad y precio que deben respaldarse | Meses que deben cotejarse con S7/T-15 | Evitar doble conteo |
| --- | --- | --- | --- |
| Inversión incremental | Días de diseño y construcción del planificador y tablero, integración, ensayo de agente y kits **adicionales**; tarifa y cotización por componente | Preparación antes de M6; piloto M6; despliegues M6–M9 y M16–M18 | No cobrar otra vez equipos, stock de sustitución ni horas ya incluidos en T-11 o EDT ordinaria |
| Costo operativo incremental | Horas mensuales de mantenimiento y soporte del planificador, ejecución cloud adicional, almacenamiento de actas y renovación/homologación de agente | Desde la activación efectiva; proyectar hasta M56 según las unidades habilitadas | Excluir conectividad, observabilidad y operación base ya presupuestadas |
| Beneficio bruto esperado | Visitas **realmente evitadas** × costo unitario de visita + minutos de preparación evitados × costo operativo por minuto | Desde el período posterior a la medición comparable de M6; rampas acordes con M7–M9 y M16–M18 | No restar aquí el costo operativo incremental: va en la fila de costo |

**Resultado neto atribuible en cada mes:** beneficio bruto − costo operativo incremental − inversión incremental. El flujo de caja debe registrar cada componente en su fila y mes; VAN/TIR se recalculan sobre el flujo completo de la oferta, no sobre una promesa aislada de esta ficha. La inversión total del proyecto se distribuye según la curva S de S7.

## Medición que permite poner cifras

En el piloto M6 se registra una ficha por oportunidad elegible: terminal, familia de camión, ventana normal, autorización, kit, técnico, preparación, cancelación y causa, visita adicional ocurrida, costo unitario y resultado físico. El plan manual se registra **antes** de mostrar la recomendación. Se comparan manual y propuesta sobre el mismo conjunto, separando observaciones no comparables. Los denominadores y exclusiones se aprueban al cierre de M6. La meta técnica de reducción de preparación inútil es 20 % respecto de esa base; el Caso no entrega el valor inicial. Si el piloto no genera muestra comparable, el ahorro monetario se deja sin acreditar y se muestra sensibilidad con beneficio cero.

## Datos que el equipo económico debe obtener

1. Tarifa cargada por día de los perfiles que diseñan, implementan, prueban y mantienen el planificador, sin duplicar jornadas de T-15.
2. Cotización y cantidad de kits diferenciales, distinguidos del suministro contractual T-11; costo de homologación por familia de equipo.
3. Precio mensual incremental de cómputo, almacenamiento y operación, con proveedor, región, moneda y tipo de cambio según E-24.
4. Costo real de visita adicional y costo operativo por minuto de preparación, con fuente contable o contrato; cantidades mensuales y meses de aplicación.
5. Acta del piloto M6 con línea base, muestra y decisión de continuar, limitar o sustituir la innovación. Sin acta, modelar escenario prudente de beneficio cero y señalar que la meta permanece pendiente.

**Estado:** esquema de cálculo y calendario preparados; valorización monetaria pendiente de los cinco respaldos. La ficha T-19 y S13 no afirman ahorro medido ni TRL superior al 2 propuesto.
