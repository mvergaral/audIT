# Conciliación de respaldos de personal, gastos e infraestructura

Corte base auditado `c9a6515`, cotejado con los insumos de D1 a D4. Los importes presupuestados, las atribuciones de trabajo y los escenarios se identifican por separado. Los cargos adicionales dependen de su acreditación y de la conciliación con partidas ya presupuestadas.

## D1, D2 y D3 · Personal y CP-SEC-05

[Cruce por perfil, mes y celda de nómina](CRUCE-CP-SEC-05-D2.md).

Linear acepta la coordinación nominal para la entrega. La ficha de reservas de AUD-14 y la matriz INN-5 de AUD-15 conservan vacíos los campos de ejecutor, aceptación y horas netas acreditadas. El Excel consolidado tiene 40 cruces de capacidad y ninguno registra horas disponibles acreditadas.

| Partida | Mes y base de cálculo | Neto CLP | Estado |
|---|---|---:|---|
| Seguridad/SRE | M9 | 1.108.000 | Cupo presupuestado |
| Datos/QA | M21–M24, 2.852.000 por mes | 11.408.000 | Cupos presupuestados |
| INN-5 desarrollo | M4–M9, 50 h/mes × 30.000 | 9.000.000 | Refuerzo nominal |
| INN-5 soporte | M21–M56, 10 h/mes × 28.000 | 10.080.000 | Refuerzo nominal |
| **Total de refuerzos** | Hoja Refuerzo presupuestado | **31.596.000** | Conservar hasta acreditar cobertura interna |

INN-5 concilia en importes con D1. La inversión de CLP 13.000.000 se compone de CLP 9.000.000 de desarrollo, CLP 2.200.000 de talleres M4 y CLP 1.800.000 de calibración M13–M15. La operación de CLP 10.080.000 corresponde al soporte. La aceptación por ejecutor y el IVA de la calibración siguen pendientes.

| Preparación CP-SEC-05, 4.1/A11 | Horas por perfil | Total |
|---|---|---:|
| M6 | Arquitectura 4, Software 8, Seguridad 4 | 16 |
| M7 | Software 16, QA 8 | 24 |
| M8 | Software 8, QA 4, SRE 4 | 16 |
| M9 | Software 4, QA 8, SRE 4 | 16 |
| **Total** | Demanda documentada fuera de A09 | **72** |

La preparación tiene un costo atribuible de referencia de CLP 2.016.000. Se requiere identificar la fila de nómina, ejecutor y horas netas por perfil y mes. Las 8 h QA de M9 podrían coincidir con CP-HW-03. Descontarlas exige comprobar que es la misma ejecución. La campaña G13 cuenta con 15 h estimadas de D1 y D4 dentro de una reserva condicional de 16 h en 10.1. Esa campaña se concilia por separado.

[Reserva AUD-14](https://linear.app/audit-fep/issue/AUD-14) · [Refuerzo y cobertura INN-5 AUD-15](https://linear.app/audit-fep/issue/AUD-15) · [Detalle de preparación](https://github.com/mvergaral/audIT/blob/8c950fa/Informe-3/d2/AUD-14_COSTO_PERSONAL_POR_PERFIL.md#L723) · [Calidad AUD-10](https://linear.app/audit-fep/issue/AUD-10)

## D1, D2 y D4 · IVA, garantías y overhead

| Partida | Tratamiento comprobado | Evidencia pendiente |
|---|---|---|
| LTE a bordo y ExpressRoute | CLP 14.432.400 de IVA referencial en la caja base, en el mes del servicio. Crédito fiscal modelado en cero. | Cotización, emisor, receptor, documento, fecha de pago y crédito aplicable. |
| Hardware inicial audIT y SIM 5G | CLP 21.828.338 de IVA referencial en el registro D4. | Canal, base de internación, factura y mes efectivo. |
| Azure/Entra, Iridium, soporte, reposición, R-24 y disposición final | Registro mensual con netos y canales de referencia. | Emisor, receptor, base afecta, impuesto, pago y eventual crédito. |
| GitLab, SonarQube y firma | Netos presupuestados e IVA referencial. | Facturación, titularidad, pago y crédito aplicable. |
| Calibración INN-5 | CLP 1.800.000 netos. Sensibilidad de CLP 114.000 de IVA mensual en M13–M15. | Régimen y documento del prestador. |
| Fiel cumplimiento, RC, ciberriesgo, notaría y custodia | CLP 85.400.000 calendarizados. CLP 13.800.000 adicionales en M56 por extensión y cola, imputados una vez. | Condiciones de póliza, base, prorrateos y pago. |
| Garantía de correcto funcionamiento | 0,15 % sobre precio de implementación, con desembolso estimado en M21. | Condiciones y fecha de constitución. |
| Seriedad de oferta | CLP 2.812.500 de referencia. Sensibilidad preoperacional en M0. | Comisión, exigibilidad y fecha. |
| Todo riesgo, accidentes y overhead | Criterios preliminares documentados. | Base asegurable y mapa de importes ya incluidos en RRHH o R-24. |

El subtotal histórico de CLP 69.374.046 de IVA referencial comprende equipos y SIM de audIT, firma y hardware de Curimón. La referencia de GitLab y SonarQube suma CLP 7.226.194 adicionales. Los CLP 14.432.400 modelados en caja corresponden al operador de ExpressRoute y a LTE a bordo. Para cerrar por partida se requiere identificar pagador, emisor, receptor, neto, IVA, mes efectivo y crédito recuperable. El [puente de IVA](d2/AUD-16_IVA_PROVEEDORES_D4.md) reproduce el importe por origen y el [cruce T-22](d2/AUD-16_GASTOS_ADMINISTRATIVOS.md#conciliación-por-naturaleza-para-t-22) concilia los 56 meses por naturaleza.

[AUD-16](https://linear.app/audit-fep/issue/AUD-16) · [Detalle mensual IVA D4](d2/AUD-16_IVA_PROVEEDORES_D4.csv) · [Calendario administrativo](d2/AUD-16_CALENDARIO_ADMIN_D1.csv) · [Criterios administrativos](d2/AUD-16_GASTOS_ADMINISTRATIVOS.md)

## D4 · Pagadores y precios estimados

| Partida | Base que usa el expediente | Evidencia pendiente |
|---|---|---|
| Hardware de campo y red | Mandante según Aclaraciones §9. | Verificar canal y costo puesto en destino antes de contratar. |
| Infraestructura local, instalación, Azure y conectividad | audIT según reparto actualizado de D4. | Confirmar condiciones comerciales y responsabilidades de cada contrato. |
| Energía de sala/gabinetes y combustible | Mandante según decisión interna D4-143 b. El propio D4 señala que falta base expresa. | Aclaración del mandante o decisión de presupuestarlo en audIT, con consumo, tarifa y calendario. |
| Clima de precisión | Dos unidades estimadas a USD 12.000 cada una. | Cotización con instalación, alcance y entrega. |
| Extinción | Una solución estimada a USD 15.000. | Cotización dimensionada y condiciones de instalación. |
| LTE M2M | CLP 28.260.000 netos de referencia. | Oferta por operador, líneas, cobertura, IVA y pago. |
| Circuito ExpressRoute | CLP 47.700.000 netos de referencia. | Oferta del operador, SLA, IVA y plazo. El puerto Microsoft se presupuesta en Azure. |

[AUD-39](https://linear.app/audit-fep/issue/AUD-39) · [Reparto D4](d4/4.8-compras-audit-y-mandante.md) · [Presupuesto de equipos](d4/4.1-presupuesto-equipos.md) · [Nube y conectividad](d4/4.2-nube-conectividad.md) · [Aclaraciones §9](../texto/Aclaraciones_Informe_3.md)

La [matriz de adquisiciones](d4/4.5-matriz-adquisiciones.md#2-orden-pago-y-disponibilidad-para-hitos) distingue órdenes, pagos, recepción e instalación de grupo, G26I y circuito. El [registro de riesgos](d4/4.7-riesgos-contingencias.md) identifica qué cargos ya se incluyen y qué importes deben estimarse por riesgo y mes para comprobar la reserva. La [prueba de caja](d2/AUD-20_DECISIONES_MODELO.md#disponibilidad-de-fondos-y-aceptación-de-h5) separa condiciones de H5, fuentes de fondos y sensibilidad intramensual.

## Valorización e imputación de las cinco innovaciones

| Innovación | Inversión y ventana | Operación y ventana | Pagador, efecto en caja y solapes |
|---|---|---|---|
| INN-1 · Expediente | 480 h en 12.1, CLP 14.816.000 atribuidos. M4: 24 h; M8: 144 h; M9: 144 h; M10: 104 h; M13–M15: 64 h. | 6 h SRE + 4 h Software + 2 h Seguridad por mes, M16–M56: 492 h y CLP 16.072.000 atribuidos. Firma: 3 × CLP 73.950 M13–M15 + 41 × CLP 600.840 M16–M56 = CLP 24.856.290. Nube: CLP 3.000/mes M13–M56. | audIT. La firma se carga una vez en Costos L; nube cubierta por la reserva. Cruce 12.1 con EDT 5.1/5.7 y A15 en implementación, soporte de Etapa 1 en M16–M20 y 13.2/13.4 desde M21. Agregar solo horas sin cobertura acreditada y aprobadas para compra. |
| INN-2 · Oportunidad de patio | 560 h en 12.2, CLP 16.576.000 atribuidos. M4–M9: 488 h; M16–M18: 72 h. | 16 h/mes M21–M56, 576 h × su mezcla por perfil = CLP 16.992.000. Capacidad cloud adicional en reserva. | audIT. 12.2 compite por las 2.560 h nominales del elemento 12. En M21–M56, 6 h/mes en 13.2 y 10 h/mes en 13.4. Conciliar banco, firmware, personal y kit base; no duplicar mantenimiento ni conectividad. |
| INN-3 · Acople y frío | Integración 120 h y montaje 70 h, a CLP 30.000/h: CLP 5.700.000 atribuidos a M6–M10/M16–M18. En M4, 5 lectores × CLP 70.200; en M5/M24/M36/M48, 231/12/12/11 balizas × CLP 19.990. | 4 h/mes M21–M56 × CLP 28.000 = CLP 4.032.000 atribuidos. Soporte físico en 4.3. | audIT integra y monta; Curimón paga CLP 5.668.340 de lectores/balizas en su hoja informativa. De las 231 balizas de M5, 210 son de montaje base y 21 de reposición. Imputar las 70 h estimadas por instalación efectiva, no por compra de repuestos. Registrar instalaciones de crecimiento al alta. Las unidades de prueba y la conectividad de equipo a bordo ya están presupuestadas. |
| INN-4 · Adhesión y sobreestadías | Diseño y validación jurídica en M2–M3, ventana y consola M6–M10 y auditoría M13–M21, según 12.4. AUD-14 estima en M9 96 h atribuibles: 16 Firmware, 24 Software, 16 Frontend y 40 QA. Los 182 montajes base incluyen 34 comodatos, con 5 h de trabajo por montaje como referencia. | Alta adicional de referencia: CLP 550.583 audIT por instalación, activación y 12 meses de conectividad, más CLP 9.000/mes si corresponde soporte. CLP 900.001 por kit de Curimón. Retiro/reinstalación según evento. | Conectividad audIT y hardware Curimón ya presupuestados para base. Cupo adicional aprobado en base: cero. Conciliar 12.4 con 9.1/9.2, 4.1, 5.7 y pruebas de permisos. Para una ampliación, imputar unidades, horas y meses diferenciales según agenda y existencias. |
| INN-5 · Fatiga | 300 h de Software sénior de borde × CLP 30.000 (M4–M9) + 5 talleres × CLP 440.000 (M4) + 60 h de servicio de ergonomía de campo × CLP 30.000 (M13–M15) = CLP 13.000.000. | 10 h/mes × CLP 28.000 × 36 = CLP 10.080.000, M21–M56. En cada revisión semestral, 8 h de Software y 2 h de Seguridad están dentro de las 10 h del mes. | audIT. Desarrollo y soporte están en Refuerzo presupuestado/Personal; talleres y calibración en INN-5 Costos/Costos H. Desarrollo y soporte usan referencia Ingeniería Senior de E-26, con Seguridad como perfil separado para validar su tarifa en los meses de revisión. Ergonomía es un perfil especializado sin categoría literal en E-26; registrar la referencia, competencia y cotización del prestador. IVA de calibración en sensibilidad. |

Para INN-3, el aporte D4 desglosa CLP 3.600.000 de integración y CLP 2.100.000 de montaje. A 15 minutos-persona por baliza, las 210 de montaje base explican 52,5 h; quedan 17,5 h de la estimación de 70 h para conciliar con lectores, pruebas y actividades efectivas. Las ventanas 12.3 y 4.2 son candidatos a imputación. Falta distribuir tareas y horas por mes y cruzar 5.2/5.3 y las cuadrillas con la nómina. Para INN-4, las 96 h de M9 se cruzan con 4.1, A09/G13 y 10.1 por caso de prueba y ejecución antes de valorizar el saldo. Para INN-5, las 50 h de M9 ya figuran en el escenario de demanda, y la auditoría semestral forma parte de las 360 h de soporte. La calibración se presupuestó como servicio externo en A15 mientras se acredita capacidad interna competente. Ajustar el refuerzo de INN-5 por la cobertura interna aprobada y registrar únicamente el diferencial. [Detalle D3 por perfil y mes](d3/datos/dedicacion_mensual_d3.csv) · [AUD-14, balizas e INN-4](d2/AUD-14_COSTO_PERSONAL_POR_PERFIL.md#escenario-de-m9-para-innovaciones-4-y-5) · [INN-1 e INN-4](d2/APORTE_ECONOMICO_INNOVACIONES_1_Y_4.md) · [INN-2](d3/APORTE_ECONOMICO_INNOVACION_2.md) · [INN-3](d4/4.9-innovacion-3.md) · [INN-4, cupo y altas](d2/AUD-21_CUPO_COMODATO.md) · [INN-5, cobertura](https://linear.app/audit-fep/issue/AUD-11#comment-77aba19c-72e5-41bb-b4f5-59a4cf20219a) · [INN-5, calibración](https://linear.app/audit-fep/issue/AUD-11#comment-661f7c78-b701-404c-b0d9-d2443718c6ed)

### Beneficio esperado de Curimón

| Innovación | Cálculo mensual y momento de reconocimiento | Datos pendientes para monetizar |
|---|---|---|
| INN-1 | Desde M16 medir el expediente y desde M21 valorar expedientes elegibles × minutos netos evitados por expediente × costo de tiempo de Curimón × adopción. Restar costos propios. | Cronometrar preparación y verificación comparables; identificar titular de cada ahorro y separar trámites ya valorizados en INN-4. Las 350 emisiones/mes del presupuesto de firma son una hipótesis de costo. |
| INN-2 | Desde el piloto M6 comparar la planificación manual y la recomendada. En operación, visitas adicionales evitadas × costo por visita de Curimón más minutos evitados de sus recursos no incluidos en ese costo. | Visitas y ventanas elegibles, causas, costo incremental, volumen y adopción. Las jornadas ahorradas de personal de audIT se registran por separado. |
| INN-3 | Desde M21 separar salidas en falso evitadas × costo por salida y reclamos térmicos evitados × costo neto por reclamo, ajustados por cobertura y adopción. | Frecuencia y costo de cada evento. La población de referencia es 210 semirremolques propios y 44 refrigerados. El kilometraje del criterio 26 se excluye del incremento. |
| INN-4 | CLP 340.000.000/año facturados × 71 % objetado × 50 % recuperable supuesto = CLP 120.700.000/año brutos a régimen. Equivale a CLP 10.058.333,33/mes y CLP 362.100.000 en 36 meses. Neto = recupero cobrado × (1 − participación del transportista) − costos adicionales de Curimón, por mes de liquidación. | Definir cartera elegible, adopción mensual, tasa incremental, regla pactada de reparto y costos propios de altas/retiros. El escenario bruto presupone 36 meses a régimen. |
| INN-5 | Combustible: km de desvío evitados × litros/km × CLP/litro. Siniestralidad: viajes elegibles × diferencia de frecuencia atribuible × costo neto por incidente. Aplicar adopción y descontar costos propios. | En M13–M15, comparar viajes similares y aislar el efecto del motor de fatiga respecto del catálogo obligatorio del criterio 28. En siniestralidad, controlar exposición y evitar duplicar costos de combustible o cobertura de seguros. |

Las referencias de beneficios sirven para estimar el efecto del cliente cuando estén respaldadas sus entradas. El caso base reconoce cero en INN-2 e INN-3 y mantiene pendiente la cuantificación de INN-1 e INN-5. El recupero de INN-4 es bruto de escenario. Estos importes permanecen fuera de los ingresos de audIT. [Criterio D1 vigente](d1/ECONOMICO_SUPUESTOS_Y_PARAMETROS_D1.md) · [Fichas T-19](d1/13-innovaciones/formularios/T-19.tex)
