# Art. 46 · Respuestas de D4 a la revisión del Informe 2

| Dato | Valor |
|---|---|
| Para | Anexo de trazabilidad del Informe 3 (`Informe-3/AUDIT-Anexo-Art46-Informe3-Revision-Independiente.md`), columnas «Respuesta» y «Sección modificada» |
| Versión | 2026-11-11 |
| Decisión | D4-146 |
| Base | FEP01, Art. 46, p. 28. Aclaraciones del Informe 3, §1 b: la tabla puede ser breve y va como anexo |

El Informe 3 no vuelve a presentar la propuesta técnica (aclaraciones, §1 a). Por eso la mayoría de los
cambios se incorporan en la oferta final del 25-11, y el estado al Informe 3 es «Aceptada, se incorpora
en la oferta final». RIE-05, INN-05 y el costo de ARQ-04 y ARQ-05 ya quedan respondidos en el análisis
económico del Informe 3.

| ID | Observación | Respuesta de audIT | Sección que se modifica | Estado al Informe 3 |
|---|---|---|---|---|
| GEN-04 | Las declaraciones de S3, S4 y S6 tienen seis columnas | Se conservan los seis campos del Comunicado 10, §7.2, en la declaración del S4, separada de las tablas analíticas del cuerpo | S4, declaración de uso de IA | Aceptada, se incorpora en la oferta final |
| GEN-05 | S8 declara uso alto de IA con revisión concentrada | Se reproduce el modelo de riesgos del S8 desde el T-15 vigente (10.000 corridas, semilla 2026) y se registra la verificación humana en la declaración del S8 y en el A-6 | S8, declaración de uso de IA, y A-6 | Aceptada, se incorpora en la oferta final |
| GEN-06 | El T-11 no tiene declaración propia | El T-11 lleva su propia declaración de uso de IA, y sus filas se consolidan en el A-6 | T-11 | Aceptada, se incorpora en la oferta final |
| ARQ-04 | La llegada de ExpressRoute a Chile Central depende del proveedor | Se pide al proveedor (Cirion, Equinix o PitChile) confirmación escrita de que el circuito llega a Chile Central con el nivel Estándar, y la conmutación a la VPN se prueba en la Etapa 1. Si no llega, se contrata el complemento Premium de ExpressRoute o se usan dos VPN por proveedores y rutas distintas, que cumplen el RT-03.17. El riesgo se registra en el T-16. El circuito está presupuestado en el Informe 3 y la diferencia del complemento cabe en la reserva de contingencia | S4 §4.2.7, T-11 fila 30, T-16 y T-17. Informe 3, tareas 4.2 y 4.7 | Aceptada. Costo en el Informe 3, texto en la oferta final |
| ARQ-05 | La recuperación de datos personales en Brazil South no tiene vía documentada | La vía es la firma de cláusulas contractuales tipo (Ley 21.719, art. 27) antes del H2, con asesoría legal presupuestada. Si no se firman, la réplica en Brazil South guarda los datos personales cifrados a nivel de campo (RT-11.10) y las claves quedan en Chile, con copia en custodia en San Bernardo. Así ningún dato personal legible sale del país, y en un desastre de la región las claves se recuperan desde San Bernardo dentro del RTO de 4 h. La decisión del H2 y su efecto sobre el H7 quedan en el T-16 (R-24) y el T-18 | S4 §4.2 y §4.3.2, S5 §5.1.6, T-16 R-24, T-18 y T-17. Informe 3, tarea 4.7 | Aceptada. Costo en el Informe 3, texto en la oferta final |
| ARQ-06 | La tabla del T-11 repite el número de la tabla del S4 | El T-11 usa numeración propia y cita sus fuentes de especificación y soporte por fila, con remisiones explícitas al S4 | T-11 y S4 | Aceptada, se incorpora en la oferta final |
| ARQ-07 | Brechas de cobertura, parque de terceros, conductor sin rastro, consultas sin respuesta y autonomía satelital | Tabla de brechas con el dato que falta, la prueba o consulta, el plazo y la contingencia: cobertura real con la campaña A03 de la Etapa 1, parque de terceros con A04, y autonomía del módem Iridium Edge del T-11, separada del producto del Informe 1 | S4 §4.1 y §4.2, S3 supuestos, T-16 y T-17 | Aceptada, se incorpora en la oferta final |
| PLA-13 | El plan de montaje no incluye las balizas ni los lectores de portería | Las 210 balizas, sus 21 de reposición y los 5 lectores se montan en el paquete 4.2, en los meses 6 a 10 y 16 a 18, con personal propio. Se separan las unidades de montaje del stock de reposición | S7, T-14, T-15 y T-18 (D2), T-11 y T-19 | Aceptada, se incorpora con D2 en la oferta final |
| RIE-01 | El registro mezcla riesgos internos de audIT y R-06 ya está resuelto | El registro se clasifica por origen (mandante, terceros y audIT), exposición residual y actuación del mandante. R-06 pasa a antecedente de la decisión de caché y sale del registro activo | S8 §8.1 a §8.3 y T-16 | Aceptada, se incorpora en la oferta final |
| RIE-02 | Falta el riesgo de convivencia y retiro del sistema de 2013 | Riesgo nuevo, por función, en los meses 16, 21 y 24, con disparadores, conciliación, reversión, responsables y efecto sobre los hitos | S8 y T-16 | Aceptada, se incorpora en la oferta final |
| RIE-03 | Faltan los riesgos de adopción de las innovaciones 1 y 2 | Riesgos de adopción de las innovaciones 1 y 2, con residual, vinculados a sus fichas del T-19 | S8 y T-16 | Aceptada, se incorpora en la oferta final |
| RIE-04 | El árbol de fallas no está cuantificado | Antes de la prueba en paralelo de los meses 13 y 14 se define cómo se cuentan los eventos, y el árbol se cuantifica con esos datos, con su incertidumbre | S8 §8.2, Figura 8.3, T-16, T-17 y T-18 | Aceptada, se incorpora en la oferta final |
| RIE-05 | El costo-beneficio de las respuestas no tiene razón de retorno | El costo incremental de cada respuesta material está en el Informe 3. La razón de retorno, pérdida esperada evitada sobre costo, va en el análisis económico, y el S8 deja el criterio técnico | Informe 3, tarea 4.7. S8 §8.3 | Aceptada. Costo en el Informe 3 |
| RIE-06 | R-17 se acepta con seguimiento pese a 21,6 % de atraso de H1 y 16,1 % de H2 | Umbrales de alerta, escalamiento, recuperación y contingencia para H1 y H2, y residual recalculado con la red vigente del T-15 | S8 §8.3 y T-16 | Aceptada, se incorpora en la oferta final |
| RIE-07 | Las tablas 8.1 a 8.3 se repiten entre S8 y T-16 | El T-16 usa numeración propia y remisiones explícitas a contingencias, disparadores y respuestas | S8 §8.3 y T-16 | Aceptada, se incorpora en la oferta final |
| INN-02 | La innovación 3 presenta como novedad el kilometraje de los semirremolques | El kilometraje real pasa a cumplimiento del criterio 26. La innovación 3 queda en la verificación del acople y el registro térmico de los 44 refrigerados, con sus pruebas, indicadores y beneficios separados | S13 §13.3 y T-19, ficha 3 | Aceptada, se incorpora en la oferta final |
| INN-05 | La innovación 3 no tiene base ni magnitud de beneficio | Beneficio en unidades físicas (asignaciones con el semirremolque verificado, 44 refrigerados con registro térmico) y valorización con inversión y costo operacional en el flujo. El beneficio monetario tiene un escenario prudente de $0 y una sensibilidad, con su fórmula y los parámetros que se miden en la Etapa 1 | Informe 3, tarea 4.9. T-19, ficha 3 | Aceptada. Valorización en el Informe 3 |

Aviso para D1: al aceptar INN-02, la parte del beneficio de la innovación 3 que viene del kilometraje
deja de ser de la innovación. Por eso el beneficio queda en $0 en el escenario base y los $135.000.000 de
la tarea 1.5 como sensibilidad, hasta que se rehagan sin el kilometraje (D4-149).
