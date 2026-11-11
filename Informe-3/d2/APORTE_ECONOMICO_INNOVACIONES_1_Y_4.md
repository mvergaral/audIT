# AUD-21 · Respaldo económico de las innovaciones 1 y 4

Para la planilla común de D2 (AUD-16) y el análisis de beneficios de D1 (AUD-9).
Montos pendientes de respaldo. Los meses indicados corresponden a la ficha T-19 y se deben conciliar con T-15 y con la fecha efectiva de devengo o pago.

## Innovación 1 · Expediente verificable del transportista

| Partida | Mes o condición de registro | Cálculo y evidencia requerida |
| --- | --- | --- |
| Levantamiento con destinatarios y elección de formato | M4 | Horas adicionales por perfil × costo horario interno validado dentro del rango aplicable del E-26. Registrar la dedicación y conciliar con EDT 12.1, 5.1 y 5.7. |
| Construcción, integración y pruebas de emisión y verificación | M8–M10 | Horas adicionales por perfil × costo horario interno. Conciliar con T-15 y separar el esfuerzo de la ficha de los servicios y datos ya cubiertos por la Etapa 1. Costear el formato comprometido con firma electrónica avanzada. |
| Certificado de firma | Alta y renovaciones según vigencia de la oferta | Certificados adicionales × precio neto por alta o renovación. Obtener cotización fechada, vigencia, moneda, IVA y responsable del pago. |
| Servicio de verificación y soporte incremental | Desde la activación efectiva en marcha blanca, hasta M56 según continuidad | Diferencia entre el costo del servicio con y sin la innovación, al mismo volumen y bajo el mismo contrato. Desglosar capacidad, transferencias y soporte cuando corresponda. Conciliar con el dimensionamiento y presupuesto de T-11. |
| Beneficio de adhesión | Medición de verificaciones desde M16 y de uso del expediente en M21 | Transportistas adheridos con al menos una emisión ÷ total adherido y verificaciones dentro de 5 segundos ÷ verificaciones observadas. T-19 mantiene el beneficio fuera de los ingresos de audIT. Una atribución monetaria requeriría evidencia del efecto marginal del expediente y conciliación con la innovación 4. |

## Innovación 4 · Esquema de adhesión y propiedad del dispositivo

| Partida | Mes o condición de registro | Cálculo y evidencia requerida |
| --- | --- | --- |
| Diseño del reparto y validación jurídica del anexo | M2–M3 | Horas adicionales × costo horario interno más servicios externos incrementales respaldados. Conciliar con EDT 12.4 y 9.1. |
| Campaña y enrolamiento | Cohorte inicial M6–M9 | Actividades adicionales por terminal × costo unitario, o detalle de horas y desembolsos. Conciliar con EDT 9.2 y el presupuesto base de enrolamiento. |
| Ventana de transmisión, consola de permisos y reparto en liquidación | Ventana y consola M6–M10. Fechar la implementación del reparto con T-15 | Horas adicionales por perfil × costo horario interno. Conciliar con EDT 4.1 y 5.7 y con la regla RN-08 de T-12. |
| Conectividad, soporte, retiro y reposición | Desde el alta o evento efectivo, según cada concepto | Unidades adicionales × costo incremental por mes o evento. Conciliar con T-11 y separar compra, stock base y servicio. La compra de equipos corresponde al mandante. T-12 establece instalación y retiro sin costo para el transportista. |
| Recupero atribuible a Curimón | Registrar cuando se espera el cobro efectivo y conciliar con la liquidación desde M16 | Recupero incremental bruto = monto elegible previamente objetado × fracción adicional efectivamente recuperable. Neto de reparto = recupero incremental bruto menos participación pactada del transportista. Documentar por separado cualquier ahorro incremental en gestión de objeciones con tiempos y costos respaldados. El porcentaje de espera objetada en T-19 describe la situación de partida. |

## Integración y controles

- Registrar por línea mes, cantidad, unidad, costo unitario y total, moneda, IVA, fuente fechada, pagador, frecuencia y referencia EDT o contractual. Convertir a CLP con los parámetros acordados cuando corresponda.
- Conciliar el total mensual y el acumulado por innovación. El detalle puede identificar partidas que ya están en el presupuesto base para demostrar su cobertura sin sumarlas de nuevo. Separar el reparto al transportista del presupuesto de audIT y evitar descontarlo dos veces.
- Confirmar dedicaciones y costos por perfil con D2 y D3, cobertura y costos de equipos y operación con D4, y método de atribución del beneficio con D1. Para la innovación 4, obtener además la base de esperas elegibles y cobradas y la proporción aprobada de reparto. Estos son insumos requeridos, sin solicitudes externas cursadas.
- Las claves `innovacion-1-inversion`, `innovacion-1-costo`, `innovacion-1-beneficio`, `innovacion-4-inversion`, `innovacion-4-costo` e `innovacion-4-beneficio` permanecen vacías hasta contar con respaldo. Confirmar la plantilla del mandante y sus celdas antes de ejecutar la comparación de planilla.

Fuentes internas de alcance y cronograma preliminar: T-19 fichas 1 y 4, S13 §§13.1 y 13.4, T-12 RN-08 y respuesta 05. Fuentes por conciliar antes de cargar cifras: T-15, T-11, E-26, parámetros económicos y cotizaciones.
