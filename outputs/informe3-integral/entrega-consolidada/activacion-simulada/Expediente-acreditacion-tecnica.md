# Expediente de acreditación técnica y financiera

**TFEP-01/2026 · Informe 3 · audIT / Transportes Curimón · 14 de noviembre de 2026**

**Alcance.** El expediente deja comprobada la coherencia documental de la simulación académica. Las ventanas del piloto y los abonos son fechas futuras del modelo. Las actas, compromisos y resultados de operación se acreditan con evidencia de sus respectivos responsables.

| Evidencia | Comprobación académica | Evidencia de ejecución por adjuntar |
|---|---|---|
| Recepción del piloto | 10 ventanas de montaje y 50 horas-persona conciliadas | Acta de recepción y fichas de prueba de los 10 vehículos |
| Cotización y autorización | Cotización de 172 instalaciones conciliada por lote y alcance de autorización preparado | Cotización emitida por el proveedor y autorización escrita de Curimón |
| Desembolso adicional | CLP 7.867.985 reproducidos en M9 y principal bancario amortizado en M21 | Carta o contrato de crédito, acuerdo de socios y comprobantes de disponibilidad y abono |
| Ensayo con guardia | Turno, secuencia y umbrales de un ejercicio de mesa verificados | Acta del ensayo, registro de guardia, bitácora con horas medidas y verificación de recuperación |

## 1. Acta de recepción del piloto · Formato D2/D4

**Lugar y fechas programadas.** San Bernardo, del 6 al 9 de julio de 2027 (M6). La agenda reserva 3, 3, 3 y 1 intervenciones, respectivamente. audIT mantiene a su cargo los 10 montajes. Por vehículo se consideran 20 minutos de banco, 140 de técnico en puesto y 140 de analista. El total programado es de 50 horas-persona.

| Control | Registro para la recepción |
|---|---|
| Identidad del lote | Identificador del vehículo, kit y serie, puesto, responsable y visita autorizada |
| Tiempos | Hora inicio y fin de banco y de ocupación del puesto, y horas efectivas por perfil |
| Prueba | Instalación física y fijaciones, configuración por audIT, lectura del equipo, prueba funcional y resultado |
| Excepciones | Defecto, severidad, corrección y fecha y resultado de repetición |
| Aceptación | Ficha por vehículo y decisión de la contraparte técnica. El lote externo se libera con los 10 registros completos y las desviaciones resueltas o aceptadas expresamente |

**Constancia académica.** Los cupos y las horas del plan se verificaron. Los datos medidos y el resultado de la recepción quedan en blanco para la prueba efectiva. **Firmas por recabar** del responsable de implantación, del responsable técnico D4 y de la contraparte técnica. [Agenda del piloto](../Agenda-montaje-simulada.csv) · [AUD-15](https://linear.app/audit-fep/issue/AUD-15) · [AUD-32](https://linear.app/audit-fep/issue/AUD-32)

## 2. Cotización escrita simulada y autorización condicionada

**Emisor ficticio · Alcance de la cotización.** Montaje físico posterior al piloto en San Bernardo, Antofagasta, Talca, Los Ángeles y Puerto Montt. Se cotizan 140 minutos de técnico por kit a CLP 16.000/h. La recepción conforme por lote da lugar a la factura. La simulación supone pago al cierre de cada mes de montaje.

| Lote | Kits | Neto CLP | IVA CLP | Bruto CLP |
|---|---:|---:|---:|---:|
| M7 | 60 | 2.240.000 | 425.600 | 2.665.600 |
| M8 | 60 | 2.240.000 | 425.600 | 2.665.600 |
| M9 | 52 | 1.941.333 | 368.853 | 2.310.186 |
| **Total** | **172** | **6.421.333** | **1.220.053** | **7.641.386** |

**Texto de autorización para la contraparte de Curimón.** «Se autoriza, para el ejercicio TFEP-01/2026 y conforme al Art. 73, el alcance físico descrito para un máximo de 172 kits y CLP 6.421.333 netos. La liberación de cada lote se condiciona a la recepción del piloto, la confirmación de las visitas y puestos, la identificación del proveedor y la comprobación del límite agregado de subcontratación del 40 % del contrato. audIT mantiene configuración, integración, QA, credenciales, acceso a datos, recepción y responsabilidad por el trabajo».

**Firmas por recabar.** Proveedor en la cotización y representante autorizado de Curimón en el permiso previo. D1 registra folio, vigencia, alcance y condiciones en el expediente. [Cálculo de lotes](../Instalacion-caja-sensibilidad.csv) · [Calendario de compras AUD-37](https://linear.app/audit-fep/issue/AUD-37)

## 3. Constancia simulada del desembolso adicional · D1/D2

| Movimiento | Fecha y hora simuladas | CLP |
|---|---|---:|
| Desembolso bancario adicional | 1 de octubre de 2027, 08:15 (M9) | 6.294.388 |
| Aporte adicional de socios | 1 de octubre de 2027, 08:20 (M9) | 1.573.597 |
| **Fondos a acreditar antes de los egresos en M9** | **Total** | **7.867.985** |
| Amortización del principal adicional | 31 de octubre de 2028, 16:10 (M21) | 6.294.388 |

D2 verificó que el aporte y el crédito siguen el 80/20 del ejercicio y que los movimientos se reflejan en la caja. La tasa modelada es de 0,9 % mensual sobre saldo bancario de apertura. Con nómina completa e IVA sin recuperación en el horizonte, el menor saldo simulado quedó en CLP 10.000.003,78. **D1/Tesorería** debe adjuntar instrumento de crédito con su disponibilidad neta y fechas, acuerdo de socios y comprobantes del banco o cartola con las fechas valor. [Movimientos simulados de caja](Caja-activacion-montaje.csv) · [AUD-20](https://linear.app/audit-fep/issue/AUD-20)

## 4. Acta del ensayo de recuperación · Ejercicio de mesa

**Fecha simulada.** 1 de octubre de 2028. El turno de las 02:00 se asigna a L1-1, con G-1 de guardia y G-2 de suplente. Los códigos representan roles de la simulación.

| Hora simulada | Evento de control | Resultado del ejercicio |
|---|---|---|
| 02:00 | Ingreso de incidente crítico | Inicia la medición de respuesta y resolución |
| 02:05 | Notificación a L1 y guardia | Detección y aviso en cinco minutos |
| 02:15 | Primera respuesta en el límite del escenario | Cumple 15 minutos |
| 02:45 | Diagnóstico completado por guardia primaria | Quedan 195 minutos hasta el límite contractual de resolución |
| 05:45 | Recuperación simulada y verificación funcional por guardia | 180 minutos desde diagnóstico y 225 minutos desde ingreso |
| 06:00 | Límite contractual de resolución | Margen simulado de 15 minutos |

En la prueba de tres incidentes se activa el suplente al minuto 10 para responder en paralelo. El escenario sin suplente llega a 20 minutos y falla el plazo de respuesta. El supuesto de recuperación de proveedor en 240 minutos desde el diagnóstico también falla, con 285 minutos totales. La disponibilidad mensual se mide por separado.

**Acta efectiva por recabar.** Operación debe nombrar titular y suplente, identificar el entorno ensayado, registrar hora de ingreso, respuesta, diagnóstico, restauración y comprobación funcional, y adjuntar registros del evento y aceptación de la contraparte. Un ensayo de recuperación debe verificar que el servicio crítico recupera su función y que se mantienen los datos requeridos para el caso. [Turnos y guardia](Turno-L1-y-guardia.csv) · [Casos con resultados esperados](Pruebas-SLA-critico.csv) · [AUD-34](https://linear.app/audit-fep/issue/AUD-34)

**Consulta de evidencia.** Se revisaron el paquete local de activación y los adjuntos y comentarios de AUD-15, AUD-20, AUD-32, AUD-34, AUD-37 y AUD-38. Los adjuntos identificados documentan presupuestos, calendarios y controles del modelo. Las actas, firmas, abonos y mediciones de ejecución se mantienen como campos de acreditación.
