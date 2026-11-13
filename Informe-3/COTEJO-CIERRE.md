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
| Déficit en M12 con H5 atrasado y reserva D4 desembolsada en M12 | CLP 308.446.935 |

Se conservaron los rótulos, las fórmulas y las celdas combinadas de RESUMEN. El Resumen Ejecutivo explica las referencias invertidas de costo y venta de la plantilla y su métrica de utilidad sobre costo. El archivo se recalculó en Excel, sin vínculos externos ni errores de celda. La Fila A y la Curva S coinciden con los CSV de OFERTA_D2.

## Pendientes con evidencia externa

| Responsable | Pendiente | Evidencia para cerrarlo |
|---|---|---|
| D1 y D2 | Disponibilidad de financiamiento ante atraso de H5 y contingencia | Monto, fecha, instrumento, costo y holgura acreditados. Recalcular caja con el instrumento real. |
| D1 y D2 | IVA de proveedores, seguros y overhead | Condiciones tributarias por proveedor, términos de las pólizas y conciliación de overhead con RRHH y R-24. |
| D1 y D2 | Horas de calidad, PCU y personal | T-15 y E-26 conciliados con ejecutores y disponibilidad. Identificar las 72 h de preparación de CP-SEC-05. |
| D1 y D2 | Innovación 5 | Conciliar inversión y operación D1 con talleres, calibración, personal y refuerzo. |
| D2 y D3 | Innovaciones 1 y 2, licencias y firma | Acreditar cobertura de horas, condición comercial de Sonar y firma, y base de medición del beneficio para Curimón. |
| D2 y D4 | Innovaciones 3 y 4, suministros y reserva | Relacionar costos con partidas, confirmar energía y combustible, validar reparto de recuperos y calendario de uso de la reserva. |
| D1–D4 | Anexo Art. 46 | Revisar la evidencia y los folios de cada cambio. El anexo de origen registra 43 observaciones sin cierre acreditado. |
| Equipo | Prototipo navegable y validación de entrega | URL accesible del avance real, prueba de navegación y validación humana de documento, planilla y exposición. |

Regeneración de la planilla desde la raíz del repositorio con PowerShell 7 y Excel de escritorio:

    pwsh -NoProfile -File Informe-3/d2/consolidar_informe3.ps1

Los insumos OFERTA_D2 están versionados en Informe-3/d2. El archivo generado se guarda en Informe-3.
