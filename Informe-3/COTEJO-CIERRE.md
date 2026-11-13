# Cotejo de cierre · Informe 3

La planilla consolidada toma como base el paquete OFERTA_D2 del commit c601503. El corte de insumos es 8c950fa. El escenario conserva los precios y el calendario base publicados.

## Controles reproducidos en Excel

| Control | Resultado |
|---|---:|
| Costo neto | CLP 7.984.400.845 |
| Precio neto | CLP 9.796.810.853 |
| Margen sobre ventas | 18,50 % |
| VAN M0–M56 | CLP 1.235.043.316 |
| TIR mensual | 83,6613 % |
| Cobro en M57 | CLP 143.833.557 |
| Equilibrio nominal con costos fijos del caso | CLP 7.984.400.845 |
| Venta de equilibrio a VAN cero con calendario base y escala uniforme | CLP 8.175.218.018 |
| Recuperación descontada sostenida | M16 |
| Déficit en M12 si se atrasa H5 | CLP 155.747.160 |
| Déficit en M12 con H5 atrasado y reserva D4, antes del financiamiento adicional | CLP 308.446.935 |

Se conservaron los rótulos, las fórmulas y las celdas combinadas de RESUMEN. El Resumen Ejecutivo explica las referencias invertidas de costo y venta de la plantilla y su métrica de utilidad sobre costo. El archivo se recalculó en Excel, sin vínculos externos ni errores de celda. La Fila A y la Curva S coinciden con los CSV de OFERTA_D2.

## Decisión de financiamiento H5 · 13-11-2026

D1 aprobó modelar el atraso del cobro de H5 a M13 junto con el desembolso de la reserva D4 en M12. El supuesto aprobado incorpora CLP 400.000.000 adicionales desde M1: CLP 320.000.000 de crédito y CLP 80.000.000 de socios. Se aplica 0,9 % mensual al saldo bancario de apertura y amortización desde M21, según la caja disponible. La meta es mantener CLP 10.000.000 de caja en M12. El recálculo en Excel dejó CLP 11.223.065 de caja mínima en M12 y cero giros de línea en el escenario combinado. Se mantienen los precios y el cálculo del VAN sobre la Fila A.

La aprobación corresponde a la modelación de la licitación. La disponibilidad de los fondos, los términos de giro y las comisiones requieren respaldo. El escenario actual no incluye comisiones adicionales de este crédito. Si se confirman, se incorporan en la Fila C y se vuelve a comprobar la holgura.

### Respaldo revisado

- **Bases del modelo.** El Formulario E-24, FEP01 p. 73, fija 0,9 % mensual para el crédito de consumo de referencia y los topes de 80 % bancario, 20 % propio y CLP 50 millones para la línea. El [dimensionamiento anterior de D2](https://github.com/mvergaral/audIT/commit/a89084b) y el [paquete OFERTA_D2](https://github.com/mvergaral/audIT/commit/c601503) respaldan la metodología de caja.
- **Disponibilidad.** En las ramas remotas revisadas al 13-11-2026, con main en 8c950fa, no se encontró una aprobación de crédito por CLP 320 millones ni un compromiso de socios por CLP 80 millones. La [guía pública de BancoEstado](https://www.bancoestado.cl/content/dam/bancoestado-public/pdf/microempresas/guia-de-uso-emprendedor.pdf) sirve de referencia para el uso de crédito comercial como capital de trabajo. El monto, la tasa contractual y las condiciones de giro requieren confirmación específica.
- **Estado de entrega.** Escenario de financiamiento aprobado por D1 para la licitación y verificado en la Fila C. Disponibilidad, condiciones de giro y comisiones pendientes de respaldo.

## Pendientes con evidencia externa

[Conciliación de personal, gastos e infraestructura](CONCILIACION-RESPALDOS.md).

| Responsable | Pendiente | Evidencia para cerrarlo |
|---|---|---|
| D1 y D2 | Disponibilidad de financiamiento ante atraso de H5 y contingencia | Monto, fecha, instrumento, costo y holgura acreditados. Recalcular caja con el instrumento real. |
| D1 y D2 | IVA de proveedores, seguros y overhead | Condiciones tributarias por proveedor, términos de las pólizas y conciliación de overhead con RRHH y R-24. |
| D1 y D2 | Horas de calidad, PCU y personal | T-15 y E-26 conciliados con ejecutores y disponibilidad. Identificar las 72 h de preparación de CP-SEC-05. |
| D1 y D2 | Innovación 5 | Los montos concilian con talleres, calibración, desarrollo y soporte. Sigue pendiente acreditar cobertura por ejecutor e IVA de calibración. |
| D2 y D3 | Innovaciones 1 y 2, licencias y firma | Acreditar cobertura de horas, condición comercial de Sonar y firma, y base de medición del beneficio para Curimón. |
| D2 y D4 | Innovaciones 3 y 4, suministros y reserva | Relacionar costos con partidas, confirmar energía y combustible, validar reparto de recuperos y calendario de uso de la reserva. |
| D1–D4 | Anexo Art. 46 | Revisar la evidencia y los folios de cada cambio. El anexo de origen registra 43 observaciones sin cierre acreditado. |
| Equipo | Prototipo navegable y validación de entrega | [Acceso al sitio audIT](https://carlosabarza.github.io/PaginaAudIT/#equipo). El sitio ofrece «Simulador Operativo en Vivo». Recorrido verificado el 13-11-2026: Portal Clientes → Simulador Operativo en Vivo → Simular Pérdida de Cobertura Celular → Restablecer Cobertura Móvil. La interfaz mostró el búfer local y la confirmación de reconciliación. Queda la validación humana y el ensayo completo de exposición. |

Regeneración de la planilla desde la raíz del repositorio con PowerShell 7 y Excel de escritorio:

    pwsh -NoProfile -File Informe-3/d2/consolidar_informe3.ps1

Los insumos OFERTA_D2 están versionados en Informe-3/d2. El archivo generado se guarda en Informe-3.
