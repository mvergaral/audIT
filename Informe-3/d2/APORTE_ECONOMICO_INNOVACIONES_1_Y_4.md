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

### Insumos provisionales informados por D3

- **Construcción del expediente:** 480 horas provisionales. Falta distribuirlas por perfil, actividad y mes, conciliar el esfuerzo incremental con T-15 y aplicar los costos horarios respaldados. Las 560 horas informadas para programación corresponden a la innovación 2 y quedan fuera de AUD-21.
- **Operación del expediente:** 12 horas al mes entre M21 y M56, ambos inclusive. Son 432 horas en 36 meses, repartidas en 216 de SRE, 144 de software y 72 de seguridad. Falta aplicar costos horarios, verificar cobertura con la operación base y confirmar si se requieren horas adicionales durante la marcha blanca previa a M21.
- **Firma electrónica:** D3 reporta como referencias comerciales un certificado FEA de un año por CLP 19.990 más IVA y un eToken por CLP 34.990 más IVA. Pendientes la fuente comercial fechada y la cotización de una modalidad compatible con la emisión automática. Estas referencias quedan fuera del costo oficial.
- **Consumo del servicio:** estimar expedientes emitidos y verificaciones mensuales, y derivar de esos volúmenes el consumo y costo marginal frente a la infraestructura base.

## Innovación 4 · Esquema de adhesión y propiedad del dispositivo

| Partida | Mes o condición de registro | Cálculo y evidencia requerida |
| --- | --- | --- |
| Diseño del reparto y validación jurídica del anexo | M2–M3 | Horas adicionales × costo horario interno más servicios externos incrementales respaldados. Conciliar con EDT 12.4 y 9.1. |
| Campaña y enrolamiento | Cohorte inicial M6–M9 | Actividades adicionales por terminal × costo unitario, o detalle de horas y desembolsos. Conciliar con EDT 9.2 y el presupuesto base de enrolamiento. |
| Ventana de transmisión, consola de permisos y reparto en liquidación | Ventana y consola M6–M10. Fechar la implementación del reparto con T-15 | Horas adicionales por perfil × costo horario interno. Conciliar con EDT 4.1 y 5.7 y con la regla RN-08 de T-12. |
| Conectividad, soporte, retiro y reposición | Desde el alta o evento efectivo, según cada concepto | Unidades adicionales × costo incremental por mes o evento. Conciliar con T-11 y separar compra, stock base y servicio. La compra de equipos corresponde al mandante. T-12 establece instalación y retiro sin costo para el transportista. |
| Recupero atribuible a Curimón | Registrar cuando se espera el cobro efectivo y conciliar con la liquidación desde M16 | Recupero incremental bruto = monto elegible previamente objetado × fracción adicional efectivamente recuperable. Neto de reparto = recupero incremental bruto menos participación pactada del transportista. Documentar por separado cualquier ahorro incremental en gestión de objeciones con tiempos y costos respaldados. El porcentaje de espera objetada en T-19 describe la situación de partida. |

### Supuesto de recupero de D1

El [documento económico de D1](https://github.com/mvergaral/audIT/blob/4da4195/Informe-3/d1/ECONOMICO_SUPUESTOS_Y_PARAMETROS_D1.md) parte de CLP 340.000.000 facturados al año y 71 % objetado (Caso 10). El supuesto de planificación es recuperar el 50 % de lo objetado. El cálculo da CLP 241.400.000 objetados y CLP 120.700.000 de recupero bruto al año. D1 usa una proyección redondeada de CLP 360.000.000 en 36 meses. El beneficio neto de Curimón queda pendiente de la proporción pactada con el transportista. Mantener el recupero separado de los ingresos de audIT.

### Asignación provisional informada por D4

| Concepto | Pagador según el esquema actual | Pendiente |
| --- | --- | --- |
| Equipos en comodato | Mandante | T-11 cubre los equipos del esquema, salvo un caso pendiente de identificar y valorizar. |
| Conectividad | Mandante | Cuantificar el diferencial atribuible al comodato. |
| Soporte, retiro e instalación | audIT | Cuantificar servicios y mano de obra fuera de T-11. D4 evalúa traspasar estos tres conceptos al mandante. |
| Reposición por falla de uso normal | Mandante | Estimar frecuencia, costo unitario y cobertura por stock base. |
| Reposición por negligencia | Transportista | Confirmar criterio de imputación en el anexo. |

Si cambia el pagador de soporte, retiro o instalación, reclasificar cada importe entre el flujo de audIT y los costos del mandante y conciliar ambos totales.

## Integración y controles

- Registrar por línea mes, cantidad, unidad, costo unitario y total, moneda, IVA, fuente fechada, pagador, frecuencia y referencia EDT o contractual. Convertir a CLP con los parámetros acordados cuando corresponda.
- Conciliar el total mensual y el acumulado por innovación. El detalle puede identificar partidas que ya están en el presupuesto base para demostrar su cobertura sin sumarlas de nuevo. Separar el reparto al transportista del presupuesto de audIT y evitar descontarlo dos veces.
- Pendientes de D3: distribución de las 480 horas del expediente, esfuerzo incremental por perfil para la innovación 4, cotización compatible con la emisión automática y consumo del servicio. D2 debe conciliar las horas con T-15 y aplicar costos por perfil respaldados. Quedan por confirmar con D4 los importes y la asignación final de soporte, retiro e instalación, y con D1 y D2 la proporción pactada de reparto.
- Las claves `innovacion-1-inversion`, `innovacion-1-costo`, `innovacion-1-beneficio`, `innovacion-4-inversion`, `innovacion-4-costo` e `innovacion-4-beneficio` permanecen vacías hasta contar con respaldo. Confirmar la plantilla del mandante y sus celdas antes de ejecutar la comparación de planilla.

Fuentes internas de alcance y cronograma preliminar: T-19 fichas 1 y 4, S13 §§13.1 y 13.4, T-12 RN-08 y respuesta 05. Fuentes por conciliar antes de cargar cifras: T-15, T-11, E-26, parámetros económicos y cotizaciones.
