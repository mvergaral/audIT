# Refuerzo focalizado y liquidez

La hoja «Escenarios de caja» captura cinco corridas del mismo modelo. La base mantiene el capital inicial de CLP 260.413.654. Al agregar refuerzo, el modelo recalcula precios con el margen de escenario. El gasto se trata como costo interno, sin IVA de proveedor.

## Alternativas de personal

| Ventana | Brecha bajo el supuesto nominal | Referencia CLP/h | Refuerzo CLP |
|---|---:|---:|---:|
| M9 Seguridad | 10,2 h | 44.000 | 448.800 |
| M9 SRE | 20,6 h | 32.000 | 659.200 |
| M21–M24 Datos | 66 h/mes | 32.000 | 2.112.000/mes |
| M21–M24 QA | 37 h/mes | 20.000 | 740.000/mes |
| **Total focalizado** | | | **12.516.000** |

La alternativa de reasignación tiene desembolso adicional cero si se acreditan ejecutores disponibles, compatibilidad de horarios y cobertura de sus otras tareas. La alternativa de refuerzo valora las brechas anteriores suponiendo 160 h disponibles en M9 para cada puesto nominal de Seguridad y Operación, y 80 h de Datos y 40 h de QA por mes en M21–M24. La disponibilidad real puede cambiar el costo. El refuerzo no cubre otros perfiles, la guardia ni todos los meses.

INN-1 mantiene CLP 16.072.000 de soporte atribuible como escenario sin cobertura durante M16–M56. Desde M21 requiere 6 h SRE, 4 h Software y 2 h Seguridad por mes. Esas horas se asignan dentro de la demanda D3 y no se suman al refuerzo focalizado. Para obtener su costo incremental, acreditar cobertura por perfil y mes y valorizar exclusivamente la parte sin cobertura atribuible a INN-1. [Demanda y dedicación](AUD-15_CONCILIACION_CAPACIDAD.md) · [Insumo D3](https://github.com/mvergaral/audIT/blob/4070a7e/Informe-3/d3/APORTE_COSTOS_SOFTWARE_DATOS.md)

## Sensibilidad de caja

Se simulan CLP 26.551.048 de IVA de compra referencial de equipos, SIM y firma. El débito de ventas y el IVA cobrado siguen el calendario del modelo. El crédito fiscal se simula completo, en el mismo mes o un mes después. Los demás impuestos de compras siguen pendientes. Ninguna corrida cambia la base aprobada ni acredita crédito fiscal.

| Corrida | Máximo de línea (CLP) | Déficit mensual sin cubrir |
|---|---:|---:|
| Base | 49.008.589 | 0 |
| Refuerzo | 49.776.085 | 0 |
| IVA con crédito en el mismo mes | 49.046.869 | 0 |
| IVA con crédito diferido | 49.059.629 | 0 |
| Refuerzo e IVA con crédito diferido | 49.827.125 | 0 |

El último escenario con precios recalculados conserva **CLP 172.875** de holgura frente al tope.

## Prueba con precios fijos

Se congelan los precios de la base y se conserva el capital inicial de CLP 260.413.654. Se aplican el refuerzo focalizado y el IVA referencial con crédito diferido un mes.

| Cobro de H5 | Máximo de línea (CLP) | Déficit mensual sin cubrir (CLP) |
|---|---:|---:|
| M12 | 50.000.000 | 167.629 |
| M13 | 50.000.000 | 161.790.931 |

El déficit es el máximo saldo negativo de cierre después de usar la línea. Sirve para medir la brecha de caja del escenario. El aporte inicial requerido se debe recalcular con las tasas y el calendario de financiamiento. La prueba se limita a cierres mensuales e IVA referencial de equipos, SIM y firma. Para comprometer refuerzo, primero acreditar la brecha de personal y volver a dimensionar la liquidez con precios y fechas aprobados.

## Financiamiento para el escenario H5 en M13

Con precios fijos, refuerzo focalizado, IVA referencial con crédito diferido y H5 en M13, el menor capital inicial en pesos enteros que cubre los cierres mensuales en el modelo es **CLP 434.348.059**, CLP 173.934.405 sobre la base. Con el reparto 80/20, corresponde aproximadamente a CLP 347.478.447 de banco y CLP 86.869.612 de socios. La línea llega al tope redondeado de CLP 50 millones. La holgura es inferior a un peso. El generador verifica que el umbral cubra caja y que un peso menos produzca déficit.

Es una sensibilidad con el calendario de desembolsos, intereses y amortización del modelo. Antes de adoptar este capital, confirmar disponibilidad y verificar caja intramensual y margen de seguridad. La base permanece en CLP 260.413.654 y conserva H5 en M12.
