# Plan de ejecución D2 · Entrega 3 — Curimón

Corte del 12 de noviembre de 2026. El proyecto de Linear tiene fecha objetivo del 13 de noviembre. Se revisaron sus 37 incidencias y se identificaron las 10 asignadas a D2.

| Orden | Tarea | Estado en Linear al revisar | Acción y evidencia de cierre |
|---|---|---|---|
| 1 | [AUD-14](https://linear.app/audit-fep/issue/AUD-14) | En curso | Conciliar EDT 5–8 y CP-SEC-05 con AUD-24, T-15 y E-26. Confirmar las horas por perfil y mes, su tarifa y capacidad. Mantener explícita la reserva condicional de 16 h. |
| 2 | [AUD-15](https://linear.app/audit-fep/issue/AUD-15) | Backlog | Integrar personal M1–M56 por implementación, operación y soporte tras AUD-14. Comprobar que instalación, calidad y mantenimiento se cuenten una vez. |
| 3 | [AUD-21](https://linear.app/audit-fep/issue/AUD-21) | En curso | Cuantificar INN-1 e INN-4 por inversión, operación y beneficio. Conciliar horas incrementales, firma, comodatos, pagadores y reparto del recupero. |
| 4 | [AUD-20](https://linear.app/audit-fep/issue/AUD-20) | Backlog | Aplicar E-24 y los criterios de AUD-5. Conciliar costo, precio y margen por fase y componente. Separar la cuenta por cobrar M56 de la caja de M57. |
| 5 | [AUD-16](https://linear.app/audit-fep/issue/AUD-16) | Backlog | Integrar D1–D4 en la plantilla del mandante, con hoja de proveedores y montos del mandante separados. Conciliar la base D4 con AUD-37/38 y las licencias con AUD-26. |
| 6 | [AUD-18](https://linear.app/audit-fep/issue/AUD-18) | Backlog | Verificar los 12 hitos E-25 y las 36 mensualidades. Aplicar precios de AUD-20, componentes variables y multas, y probar desfase de H5. |
| 7 | [AUD-17](https://linear.app/audit-fep/issue/AUD-17) | Backlog | Cerrar 56 meses de flujo libre y financiado, IVA, saldos y prueba de línea de crédito. Conciliar M57 por fuera del horizonte. |
| 8 | [AUD-19](https://linear.app/audit-fep/issue/AUD-19) | Backlog | Graficar costos más intereses, facturación y saldo de caja financiado. Conciliar las tres series con el flujo. |
| 9 | [AUD-22](https://linear.app/audit-fep/issue/AUD-22) | Backlog | Entregar a D1 una versión identificada, con controles, flujo libre, tasa, supuestos y conciliación M56–M57. |
| 10 | [AUD-23](https://linear.app/audit-fep/issue/AUD-23) | Backlog | Incorporar y contrastar VAN, TIR, sensibilidad y punto de equilibrio de AUD-6/8 sobre la misma versión. |

AUD-14/15 y AUD-21 pueden avanzar junto con AUD-20/18. AUD-16/17 reúnen ambos frentes y habilitan AUD-19/22. AUD-23 requiere el retorno de D1.

## Decisiones y datos pendientes

- D3 y D2 deben confirmar el reparto mensual por perfil y la cobertura de las horas candidatas en EDT 5, así como la operación y el cierre M21–M24. D1 debe confirmar la composición de la reserva de CP-SEC-05. La estimación de 7 h de D4 pertenece a las 16 h condicionales existentes.
- Para INN-1 faltan horas realmente incrementales, costo de firma y consumo. Para INN-4 falta validar cupo, retiros, cobertura y reparto del recupero. Los beneficios del mandante se mantienen fuera de la facturación de audIT.
- Las decisiones financieras delegadas por D1 se fijan en `AUD-20_DECISIONES_MODELO.md`. El monto del crédito y los precios resultan del presupuesto integrado. El servicio de M56 se cobra en M57, de acuerdo con E-25 y el paquete D1 integrado en main.
- D4 publica CLP 1.526.997.751 de base y CLP 152.699.775 de reserva. El calendario redondeado suma CLP 1.526.997.752. El ajuste de CLP −1 se registra por separado en M56. La reserva conserva su total presupuestario y queda como desembolso de sensibilidad hasta acordar su calendario.
- Del subtotal D1 de calidad y capacitación, el calendario publicado suma CLP 37.250.000 de implementación y CLP 16.500.000 de operación. El detalle de innovación 5 exige conciliar las horas con RRHH antes de incorporarlo al precio.
- Para cerrar AUD-16 se necesita la hoja Resumen del mandante. La aclaración §5 obliga a preservar sus filas, rótulos y orden. Las demás hojas pueden ajustarse con las restricciones de E-21, T-22 y la aclaración. El Excel de AUD-17 es un escenario de trabajo. La entrega a D1 requiere terminar el presupuesto y validar IVA, deuda y supuestos de venta.

## Ejecución del 12 de noviembre

- AUD-14/15: contrasté el último documento de D3 con el respaldo D2 en 494e42b. Ambos ubican las 72 h de preparación en 4.1/A11, M6–M9, separadas de A09. Sus referencias de CLP 2.016.000 y CLP 2.088.000 son alternativas para las mismas horas. El escenario de 2.737 h por CLP 84.360.000 describe contratación sin absorción de los bloques evaluados. Hace falta probar la cobertura base y la dedicación disponible antes de usarlo como costo incremental.
- AUD-16/17: concilié en `D2_Insumos_Conciliados.xlsx` CLP 1.632.580.351 netos de egresos parciales identificados. Incluye base D4 conciliada, licencias D3, calidad/capacitación D1 y pago de cierre D1. La reserva de CLP 152.699.775 se muestra aparte y las compras del mandante de CLP 225.384.199 tienen su propia columna informativa. Quedan por integrar RRHH, demás indirectos, innovaciones y su tratamiento tributario.
- AUD-18: contrasté cada hito con FEP01, E-25, p. 74. Etapa 1 suma 60 %, etapa 2 suma 40 %. El calendario tiene 36 servicios facturados y 36 cobros, incluido M57. Los montos esperan el precio de AUD-20. La sensibilidad de H5 desplaza el cobro a M13 y conserva el mes contractual M12.
- AUD-20: verifiqué los tipos de cambio, IVA, tasas, tope de línea y margen máximo contra E-24. Se adopta una tasa de descuento de 1,02619 % mensual antes de impuestos bajo 80 % deuda al 0,9 % mensual y 20 % capital propio con costo anual de 20 %.
- AUD-19: la curva debe tomar el saldo financiado de la Fila C, facturación por devengo y costos acumulados con intereses de ambas deudas. La amortización se registra en caja y se excluye de la serie de costos. Fuente: Aclaraciones, §6.

## Orden de publicación en main y Linear

1. **Criterios financieros y plan.** Publicar el acuerdo delegado D1/D2 y la conciliación de costos identificados. Referenciar los archivos desde AUD-16/17/18/20.
2. **Presupuesto.** Completar RRHH, innovaciones, proveedores, gastos administrativos y su afectación a IVA. Revisar cada partida por cantidad, unidad, precio, fuente, fase, pagador y mes. Publicar respaldo y actualizar AUD-14/15/16/21.
3. **Modelo y cobros.** Integrar la plantilla del mandante, precios y 12 hitos, operación mensual, caja de 56 meses, conciliación M57 y Curva S. Probar integridad, topes y escenarios. Publicar y actualizar AUD-17/18/19/20.
4. **Entrega e indicadores.** Congelar versión con resultados y control de fuentes. Registrar el paquete en AUD-22 e integrar VAN, TIR, sensibilidad y punto de equilibrio en AUD-23 usando esa versión.

## Confirmaciones externas para el presupuesto

- **D3:** entregar la dedicación reservable por perfil y mes, el cruce de las 6.008 h con las 17.600 h de A09 y los cierres M21–M24. Identificar para INN-1 horas realmente adicionales y consumos de firma y almacenamiento. Para CP-SEC-05, confirmar el paquete que absorbe cada bloque dentro de las 72 h de preparación.
- **D4:** confirmar el cupo adicional de INN-4, quién paga soporte y retiros, cuántos meses se presta el servicio y qué importes del calendario de proveedores son afectos y recuperables por IVA. El calendario disponible ya permite integrar su base neta y preservar los equipos del mandante fuera de la caja audIT.
