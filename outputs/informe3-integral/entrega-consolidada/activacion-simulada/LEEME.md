# Activación académica · Instalación y SLA

**TFEP-01/2026 · 14 de noviembre de 2026 · audIT / Transportes Curimón**

Se incorpora al paquete consolidado una variante académica en la que audIT mantiene el piloto interno y contrata **172 montajes físicos** por CLP 7.641.386 brutos. La caja supone pago al término de cada mes de montaje y conserva la nómina completa y el gasto de IVA. El alcance y los importes de la cotización y la autorización condicionada están en el [anexo técnico D1/D2](../Cierre-tecnico-D1-D2.md).

El refuerzo de M9 calculado es **CLP 7.867.985**, con CLP 6.294.388 de banco y CLP 1.573.597 de socios. Se gira antes de egresos, devenga 0,9 % sobre el saldo bancario de apertura desde M10 y se amortiza en M21. En el escenario con H5 en marzo y reserva en M9, el mínimo es **CLP 10.000.003,78 en M13**. Las 224 comprobaciones de cierre y los 313 movimientos de once meses críticos cumplen el piso y mantienen la línea en cero dentro de los cuatro escenarios. El giro adicional, las fechas y el costo de crédito corresponden al escenario académico. [Orden de caja](Caja-activacion-montaje.csv)

Se programaron **930 horas de L1 en un mes de 31 días**. El turno modelado cubre las 24 horas, añade seis horas de solapamiento por día y respeta 160 horas por agente y 12 horas de descanso entre turnos como criterios internos de simulación. La guardia L2/L3 alterna ocho perfiles con titular y suplente. En el presupuesto crítico, respuesta en 15 min, diagnóstico en 30 min y recuperación en 180 min suman **225 min**. Tres incidentes simultáneos requieren apoyo paralelo para cumplir los 15 min. La disponibilidad de 99,9 % se mide por separado. Cuatro interrupciones de 10 minutos caben en el presupuesto de 40,32 min de un mes de 28 días. [Turno y guardia](Turno-L1-y-guardia.csv) · [Casos SLA](Pruebas-SLA-critico.csv)

## Condiciones para desplegarlo fuera del ejercicio

El [expediente de acreditación](Expediente-acreditacion-tecnica.md) reúne el acta de piloto, la cotización y autorización, la constancia de giro y el acta del ejercicio de mesa, con los controles y evidencias por adjuntar.

- **D1 y Curimón** acreditan la autorización escrita, el cupo de subcontratación agregado y las condiciones de la cotización. **D2/D4** registran la recepción del piloto con tiempos por kit y confirman las visitas, el equipo, los puestos y los turnos. Se libera cada lote contra su acta.
- **D1/Tesorería** comprueban giro y aporte antes del primer pago que los requiera. **D2** recalcula con condiciones financieras y crédito fiscal efectivos y evalúa si aparecen horas de nómina realmente evitables.
- **Operación/D3/D4** nominan guardias y suplencias, miden demanda, ensayan recuperación y registran disponibilidad por servicio. La compra de soporte debe acreditar el tiempo de recuperación desde el diagnóstico.
- La hoja de supuestos y la adenda registran esta variante como simulación. El flujo original y sus escenarios históricos se preservan en el paquete de referencia. Registro para A-6: simulación de caja, turnos y pruebas de SLA con asistencia de IA.
