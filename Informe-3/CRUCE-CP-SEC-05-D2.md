# Cruce D2 de preparación CP-SEC-05 · EDT 4.1 / A11

La demanda de D3 suma 72 h en M6–M9. La nómina AUD-17 permite identificar las partidas candidatas, pero no desglosa sus asignaciones a CP-SEC-05. El cruce usa las columnas H–K de la hoja «Personal M1–M12».

| Mes | Perfil | Horas | Celda de nómina candidata | Estado |
|---|---|---:|---|---|
| M6 | Arquitectura | 4 | H9 · Arquitecto de Solución | Pendiente de asignación en el calendario |
| M6 | Software | 8 | H14 · Dotación restante | Pendiente de identificar ejecutor y horas |
| M6 | Seguridad | 4 | H10 · Oficial de Seguridad | Pendiente de asignación en el calendario |
| M7 | Software | 16 | I14 · Dotación restante | Pendiente de identificar ejecutor y horas |
| M7 | QA | 8 | I14 · Dotación restante | Pendiente de identificar ejecutor y horas de QA de componente |
| M8 | Software | 8 | J14 · Dotación restante | Pendiente de identificar ejecutor y horas |
| M8 | QA | 4 | J14 · Dotación restante | Pendiente de identificar ejecutor y horas |
| M8 | SRE | 4 | J13 · Líder de Operación/SRE | Pendiente de asignación en el calendario |
| M9 | Software | 4 | K14 · Dotación restante | Pendiente de identificar ejecutor y horas |
| M9 | QA | 8 | K14 · Dotación restante | Posible solapamiento con CP-HW-03, pendiente de comprobar |
| M9 | SRE | 4 | K13 · Líder de Operación/SRE | Pendiente de asignación en el calendario |
| **Total** | | **72** | **11 cruces** | **Cobertura por acreditar** |

Las filas 9, 10 y 13 identifican roles con 160 h mensuales presupuestadas. Esa dedicación mensual incluye otros trabajos. La fila 14 agrupa 3.840 h mensuales en M6–M9, sin reparto nominal por perfil. Para QA de componente se usa esa fila como candidata. La fila 12 corresponde al liderazgo de calidad. Los cupos de refuerzo de Seguridad/SRE en M9 y Datos/QA en M21–M24 tienen su propia imputación y requieren verificar disponibilidad antes de reasignarlos.

**Decisión propuesta a D2.** Mantener las 72 h en A11, fuera de las 6.008 h de A09, y conservar los CLP 31.596.000 de refuerzo vigentes. Registrar para cada fila código de ejecutor, semana, horas netas disponibles tras sus otras tareas, referencia y horas incrementales confirmadas. Para descontar horas compartidas con CP-HW-03, D3 y D4 deben identificar la tarea común y su duración. Las 15 h estimadas de campaña G13 de D1 y D4 se mantienen en su propia reserva de 16 h de 10.1.

## Reserva semanal propuesta para aprobación de D2

La secuencia reserva primero diseño, luego implementación y al final regresión. S1–S4 son semanas contractuales. Los códigos de Software y QA identifican puestos propuestos. Cada titular debe confirmar horas netas tras descontar sus otros compromisos. La columna de horas solicitadas queda lista para reservar.

| Mes | Semana | Puesto o código propuesto | Horas solicitadas | Entregable para comprobar la reserva |
|---|---|---|---:|---|
| M6 | S2 | Arquitecto de Solución | 4 | Diseño de autorización local |
| M6 | S2 | Oficial de Seguridad | 4 | Revisión de vencimiento y revocación |
| M6 | S3 | Software A11 | 8 | Contrato local listo para implementar |
| M7 | S2 | Software A11 | 16 | Control previo al registro |
| M7 | S3 | QA A11 | 8 | Pruebas de componente |
| M8 | S2 | Software A11 | 8 | Instrumentación configurable |
| M8 | S2 | Líder de Operación/SRE | 4 | Preparación de entorno y registros |
| M8 | S3 | QA A11 | 4 | Comprobación de la correlación con registros locales |
| M9 | S1 | Software A11 | 4 | Preparación del candidato |
| M9 | S1 | Líder de Operación/SRE | 4 | Configuración del candidato |
| M9 | S2 | QA A11 | 8 | Regresión de componente antes del cierre temprano de A11 |
| **Total** | | | **72** | |

En M9 la regresión se propone en S2 para evitar el pico de QA de S3 y terminar antes del día hábil 172. La disponibilidad de esa ventana requiere confirmación. Para SRE, verificar el saldo de S1 y si las 4 h ya forman parte de la demanda usada para dimensionar las 20,6 h de apoyo. El cupo existente tiene sus propias asignaciones propuestas.

### Cruce con CP-HW-03

Mantener las 8 h de QA de M9 en la demanda. El trabajo potencialmente común es preparar datos y banco, comprobar reinicio y reconexión y extraer registros. CP-HW-03 verifica continuidad de captura autorizada y recuperación sin pérdidas. CP-SEC-05 verifica el cese de la captura revocada y la conservación de evidencia previa. Para imputar una actividad común una sola vez, registrar la tarea, versión y configuración, ventana, evidencia de ambos casos y horas compartidas. La evidencia revisada permite identificar trabajo potencialmente común. **Horas descontadas por solapamiento acreditado: 0.**

[Plan semanal y cupos de apoyo en AUD-14](https://linear.app/audit-fep/issue/AUD-14#comment-7a0de7bb-482c-4aa1-97c2-d78b26859a9a) · [Frontera de pruebas D3](d3/3.1-esfuerzo-perfiles.md)


## Prueba de caja a precios fijos

Como sensibilidad, se simuló que las 72 h se compran íntegramente a los puntos medios de E-26, usando la Fila C del escenario combinado de H5 con CLP 400 millones adicionales. El desembolso neto de referencia es CLP 576.000 en M6, CLP 608.000 en M7, CLP 432.000 en M8 y CLP 400.000 en M9. Se conserva el tratamiento fiscal vigente y no se añaden comisiones. La caja de M12 pasa de CLP 11.223.065 a CLP 9.207.065, quedando CLP 792.935 bajo la meta de CLP 10 millones. Esta prueba dimensiona el impacto de comprar todas las horas. El presupuesto vigente conserva sus cifras hasta confirmar el costo incremental real.

[Nómina AUD-17](d2/AUD-17_FLUJO_DE_CAJA.xlsx) · [Cruce de preparación D2](d2/AUD-14_COSTO_PERSONAL_POR_PERFIL.md) · [Estimación D3](d3/3.1-esfuerzo-perfiles.md) · [Planilla consolidada](AUDIT-Informe3-Modelo-Economico.xlsx) · [AUD-14 en Linear](https://linear.app/audit-fep/issue/AUD-14)
