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

- **Implementación del expediente:** D3 desglosó las 480 horas provisionales por perfil. Las 560 horas de programación corresponden a la innovación 2 y quedan fuera de AUD-21.
- **Operación del expediente:** D3 propone imputar al presupuesto base 12 horas al mes entre M21 y M56, ambos inclusive. Son 432 horas en 36 meses, repartidas en 216 de SRE, 144 de Software y 72 de Seguridad. D2 debe comprobar la disponibilidad por perfil antes de determinar horas adicionales.
- **Firma electrónica:** D3 reporta como referencias comerciales un certificado FEA de un año por CLP 19.990 más IVA y un eToken por CLP 34.990 más IVA. Pendientes la fuente comercial fechada y la cotización de una modalidad compatible con la emisión automática. Estas referencias quedan fuera del costo oficial.
- **Consumo del servicio:** estimar expedientes emitidos y verificaciones mensuales, y derivar de esos volúmenes el consumo y costo marginal frente a la infraestructura base.

| Perfil informado por D3 | Horas de implementación | Correspondencia con E-26 |
| --- | ---: | --- |
| Arquitecto de Solución | 40 | Arquitecto Senior, confirmado por D3. |
| Ingeniero de software sénior | 160 | Ingeniero Senior. |
| Ingeniero frontend y móvil | 64 | Ingeniero Senior, confirmado por D3. |
| Seguridad TI | 48 | Encargado de Seguridad TI. |
| Ingeniero de datos | 32 | Ingeniero de Datos. |
| QA y automatización | 96 | Analista QA Senior, confirmado por D3. |
| DevOps/SRE | 40 | Ingeniero DevOps / SRE. |
| **Total** | **480** | |

**Cruce de calendario.** El [JSON vigente de D3](https://github.com/mvergaral/audIT/blob/993fa514357085fb75b79a329de0e5c278507233/Informe-3/d3/datos/presupuesto_d3.json) distribuye 416 h de preparación y construcción y 64 h de marcha blanca. Las fechas corresponden a T-14, paquete 12.1, y T-19.

| Mes | Arquitectura | Software | Frontend/Móvil | Seguridad | Datos | QA | SRE | Total (h) | Costo bruto de referencia (CLP) |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| M4 | 16 | 0 | 0 | 8 | 0 | 0 | 0 | 24 | 768.000–1.344.000 |
| M8 | 16 | 40 | 24 | 16 | 16 | 16 | 16 | 144 | 3.968.000–5.376.000 |
| M9 | 0 | 64 | 24 | 16 | 16 | 24 | 0 | 144 | 3.920.000–4.752.000 |
| M10 | 8 | 40 | 8 | 8 | 0 | 24 | 16 | 104 | 2.720.000–3.552.000 |
| M13 | 0 | 8 | 8 | 0 | 0 | 16 | 8 | 40 | 928.000–1.184.000 |
| M14 | 0 | 8 | 0 | 0 | 0 | 0 | 0 | 8 | 240.000 |
| M15 | 0 | 0 | 0 | 0 | 0 | 16 | 0 | 16 | 256.000–384.000 |
| **Total** | **40** | **160** | **64** | **48** | **32** | **96** | **40** | **480** | **12.800.000–16.832.000** |

El cálculo mensual usa CLP 30.000/h para Software y Frontend/Móvil y los extremos de E-26 para los demás perfiles. T-15 ubica la marcha blanca en A15. Las 64 h de esa actividad se reparten en 16 de Software, 8 de Frontend/Móvil, 32 de QA y 8 de SRE. Su costo bruto referencial es CLP 1.424.000–1.808.000, sujeto a conciliación con la carga de E1.

Según D3, el expediente debe funcionar desde M16. D3 mantiene las 12 horas estimadas para M21. H12 cierra la Etapa 2 al final de M21. Si el traspaso exige esfuerzo adicional, estimarlo en una partida separada del mantenimiento del expediente. Queda por conciliar la cobertura de M16 a M20 con la dotación de ese periodo.

### Costo interno de las 480 horas de implementación

D2 usa la columna de costo horario de [E-26](https://github.com/mvergaral/audIT/blob/4da4195/texto/FEP01_26_Bases_Administrativas_TFEP_01_2026_3.md#L2460) y la equivalencia de CLP 40.000 por UF establecida en [E-24](https://github.com/mvergaral/audIT/blob/4da4195/texto/FEP01_26_Bases_Administrativas_TFEP_01_2026_3.md#L2404). Los intervalos siguientes son límites de referencia de las bases aplicados al esfuerzo bruto informado por D3. La referencia provisional adoptada para Ingeniero Senior figura debajo de la tabla. Los demás costos horarios y el costo incremental quedan pendientes.

| Perfil E-26 | Horas | Costo permitido (UF/h) | Equivalente (CLP/h) | Límites del subtotal (CLP) |
| --- | ---: | ---: | ---: | ---: |
| Arquitecto Senior | 40 | 0,8–1,4 | 32.000–56.000 | 1.280.000–2.240.000 |
| Ingeniero Senior | 224 | 0,6–0,8 | 24.000–32.000 | 5.376.000–7.168.000 |
| Encargado de Seguridad TI | 48 | 0,8–1,4 | 32.000–56.000 | 1.536.000–2.688.000 |
| Ingeniero de Datos | 32 | 0,6–1,0 | 24.000–40.000 | 768.000–1.280.000 |
| Analista QA Senior | 96 | 0,4–0,6 | 16.000–24.000 | 1.536.000–2.304.000 |
| Ingeniero DevOps / SRE | 40 | 0,6–1,0 | 24.000–40.000 | 960.000–1.600.000 |
| **Total** | **480** | | | **11.456.000–17.280.000** |

**Referencia provisional aprobada por D2.** Aplicar CLP 30.000/h (0,75 UF/h) a las 224 horas de Ingeniero Senior de la implementación del expediente. El valor está dentro de E-26 y tiene como antecedente el costo utilizado por [D1](https://github.com/mvergaral/audIT/blob/4da4195/Informe-3/d1/ECONOMICO_SUPUESTOS_Y_PARAMETROS_D1.md#L56) para desarrollo sénior de la innovación 5. Las 160 horas de Software equivalen a CLP 4.800.000 y las 64 de Frontend/Móvil a CLP 1.920.000. El subtotal bruto de referencia es CLP 6.720.000. La aprobación cubre estas horas de implementación. Los costos comunes de los seis perfiles se confirmarán en [AUD-14](https://linear.app/audit-fep/issue/AUD-14).

**Conciliación con el presupuesto base.** T-14 identifica el expediente en el paquete 12.1. T-15 asigna 17.600 horas a Servicios de la Etapa 1 y 2.560 a Innovaciones, sin el detalle por persona, mes o subpaquete necesario para separar las 224 horas. Para cada bloque de trabajo de Software y Frontend/Móvil, registrar las horas de D3, su mes y el paquete de T-15 que las cubre. Aplicar la referencia solo al saldo que se acredite como adicional. [T-14, paquete 12.1](https://github.com/mvergaral/audIT/blob/4da4195/recursos/Formato-Oferta-audIT/subdocumentos/07-plan-trabajo/formularios/T-14.tex#L74) · [T-15, horas por elemento EDT](https://github.com/mvergaral/audIT/blob/4da4195/recursos/Formato-Oferta-audIT/subdocumentos/07-plan-trabajo/formularios/T-15.tex#L57)

| Bloque | Alcance base que se reutiliza | Trabajo propio del expediente | Horas con cobertura presupuestaria por verificar |
| --- | --- | --- | ---: |
| Software | EDT 5.1, registros de Personas y cumplimiento. Consulta de hoja de vida desde Flota y activos, EDT 5.2. | EDT 12.1, servicio de emisión, integración de firma y validador público. | 160 |
| Frontend/Móvil | EDT 5.7, portal del transportista y funciones base de viajes, liquidación y consentimientos. | EDT 12.1, botón de emisión y adaptación del consentimiento y la descarga para el expediente. | 64 |
| **Total por conciliar** | | | **224** |

| Mes | Software (h) | Frontend/Móvil (h) | Actividades informadas por D3 | Costo bruto de referencia (CLP) |
| --- | ---: | ---: | --- | ---: |
| M8 | 40 | 24 | Armado del expediente y controles de datos. Consentimiento y acceso desde el portal. | 1.920.000 |
| M9 | 64 | 24 | Integración de firma y conservación de versiones. Emisión y descarga. | 2.640.000 |
| M10 | 40 | 8 | Verificador público, vigencia y registros. Estados y errores. | 1.440.000 |
| M13 | 8 | 8 | Correcciones de marcha blanca. | 480.000 |
| M14 | 8 | 0 | Correcciones de marcha blanca. | 240.000 |
| **Total** | **160** | **64** | **224 h** | **6.720.000** |

D3 propone imputar las 480 horas al paquete 12.1, dentro de las 2.560 horas del elemento 12 de T-15. D2 debe confirmar la reserva por perfil y mes contra la carga de las demás innovaciones y conciliar el trabajo con los paquetes 5.1 y 5.7. Los importes brutos quedan fuera del incremento de implementación mientras se comprueba la imputación.

### Valorización preliminar de la operación del expediente

Para los 36 meses de M21 a M56 estimados por D3, se aplican los rangos horarios de E-26 y la equivalencia de E-24 ya citados. Los subtotales valorizan la carga completa informada, antes de conciliarla con la operación base.

| Perfil E-26 | h/mes | Horas en 36 meses | Rango (CLP/h) | Rango mensual (CLP) | Rango total (CLP) |
| --- | ---: | ---: | ---: | ---: | ---: |
| Ingeniero DevOps / SRE | 6 | 216 | 24.000–40.000 | 144.000–240.000 | 5.184.000–8.640.000 |
| Ingeniero Senior (Software) | 4 | 144 | 24.000–32.000 | 96.000–128.000 | 3.456.000–4.608.000 |
| Encargado de Seguridad TI | 2 | 72 | 32.000–56.000 | 64.000–112.000 | 2.304.000–4.032.000 |
| **Total bruto** | **12** | **432** | | **304.000–480.000** | **10.944.000–17.280.000** |

D3 propone imputar 6 h/mes de SRE y 2 h/mes de Seguridad al paquete 13.2, y 4 h/mes de Software al 13.4. T-15 reserva 640 h/mes para cada paquete en conjunto. Para comprobar la cobertura, D2 debe descontar las demás asignaciones del mismo perfil y mes y comparar el saldo con las horas propuestas. Las 12 h/mes quedan fuera del costo incremental mientras se valida esa capacidad. Si se acredita un faltante, valorizar solo esas horas con la tarifa aprobada en AUD-14. La firma automática y el consumo incremental se valorizan por separado.

### Conciliación de capacidad para D2

| Periodo | Resultado del cruce con T-15 | Comprobación pendiente |
| --- | --- | --- |
| M8–M10 | D3 asigna 200 h de Software y Frontend/Móvil al 12.1. La curva de T-15 entrega 4.800 h globales en M8 y M9, y 5.280 h en M10. El elemento 12 dispone de 2.560 h globales para todas las innovaciones. | Verificar la reserva mensual de cada perfil en el 12.1 y descontar la carga de las demás tareas. |
| M13–M15 | T-15 asigna el 100 % de Software sénior y Frontend/Móvil a E1 y E2. D3 identifica 16 h de correcciones en M13 y 8 h en M14. | Identificar qué actividad de la carga ya asignada incluye esas 24 h. Si están fuera de esa carga, determinar qué trabajo se puede reprogramar o cuántas horas habría que agregar. |
| M16–M20 | El expediente debe estar disponible desde M16. T-15 prevé 5.920 h globales por mes en M16–M17, 4.800 h en M18 y 4.160 h por mes en M19–M20. La reserva de los paquetes 13.2 y 13.4 comienza en M21. | Identificar quién cubre el expediente durante la estabilización y el cierre de implementación. Registrar por mes el esfuerzo de Software, SRE y Seguridad y la actividad base que lo financia. |
| M21–M56 | La propuesta ocupa 8 de 640 h/mes del 13.2 (1,25 %) y 4 de 640 h/mes del 13.4 (0,625 %). Esas proporciones se calculan sobre el paquete completo. | Verificar 6 h libres de SRE y 2 h libres de Seguridad en 13.2, y 4 h libres de Software en 13.4, una vez descontadas las demás asignaciones de cada perfil. Mantener M21 y registrar por separado cualquier esfuerzo extraordinario de H12. |

Para cerrar el cruce, D2 debe registrar por mes, perfil y paquete las horas presupuestadas, las horas ya asignadas y la parte de esa asignación que cubre el expediente. Las horas propuestas que queden sin cobertura se valorizan solo después de verificar si caben en la capacidad restante o si requieren ampliar la dotación. En M13 y M14, la prioridad es identificar las correcciones dentro de la carga de las escuadras, ya que ambos perfiles figuran totalmente asignados.

#### Imputación propuesta para las correcciones de M13 y M14

S7 encarga a la **Escuadra de Estabilización E1** la marcha blanca de la Etapa 1 y las correcciones de su software. T-15 sitúa esa ventana en **A15**, y T-14 incluye M13–M15 en el **paquete 12.1**, a cargo del Arquitecto de Solución. D2 puede registrar una sola imputación con esas tres referencias: **E1** ejecuta, **A15** identifica la actividad del cronograma y **12.1** identifica el alcance cuyo presupuesto debe cubrir las horas.

| Mes | Software sénior E1 | Frontend/Móvil E1 | Total | Capacidad mensual comprometida por perfil en E1 |
| --- | ---: | ---: | ---: | --- |
| M13 | 8 h | 8 h | 16 h | 160 h de Software y 160 h de Frontend/Móvil |
| M14 | 8 h | 0 h | 8 h | 160 h de Software y 160 h de Frontend/Móvil |
| **Total** | **16 h** | **8 h** | **24 h** | |

Cada bloque de 8 h ocupa el 5 % de la asignación mensual del perfil correspondiente en E1. D2 debe identificar las tareas que contienen esas horas o validar su redistribución dentro de A15 y conciliar su imputación al 12.1.

#### Roles propuestos para QA y SRE en E1

| Perfil en el JSON de D3 | Rol propuesto de T-15 | Demanda para A15 | Asignación nominal en E1 | Capacidad a comprobar |
| --- | --- | --- | --- | --- |
| QA y automatización | Ingeniero de pruebas y automatización (1 de planta) | 16 h en M13 y 16 h en M15 | 160 h/mes, 100 % asignado a E1 | Cada bloque ocupa el 10 % de la asignación. Identificar la validación del expediente dentro de las pruebas ya planificadas o reordenar la carga de ese mes. |
| DevOps/SRE | Ingeniero SRE / DevOps (2 de refuerzo) | 8 h en M13 | 320 h/mes entre dos personas, 100 % asignado a E1 | Las 8 h ocupan el 2,5 % del equipo o el 5 % de la jornada mensual de una persona. Identificar quién absorbe el bloque y comprobar su carga junto con la guardia. |

El Analista de QA de refuerzo está asignado a E2 durante M13–M15. Para SRE, S7 incorpora a los dos ingenieros de refuerzo a la rotación de guardia de E1, por lo que la asignación nominal de 320 h incluye otras responsabilidades. El cruce identifica los roles compatibles, con cobertura aún pendiente. Una vez identificadas las tareas y las personas en A15, D2 puede determinar el saldo de horas adicionales por perfil y valorizarlo en AUD-14.

Fuentes: [T-15, capacidad de QA y SRE por escuadra](https://github.com/mvergaral/audIT/blob/4da4195/recursos/Formato-Oferta-audIT/subdocumentos/07-plan-trabajo/formularios/T-15.tex#L118) · [S7, rotación de guardia de E1](https://github.com/mvergaral/audIT/blob/4da4195/recursos/Formato-Oferta-audIT/subdocumentos/07-plan-trabajo/contenido.tex#L273).

Fuentes: respuesta de D3 compartida con D2. [S7, Escuadra de Estabilización E1](https://github.com/mvergaral/audIT/blob/4da4195/recursos/Formato-Oferta-audIT/subdocumentos/07-plan-trabajo/contenido.tex#L260) · [T-14, paquete 12.1](https://github.com/mvergaral/audIT/blob/4da4195/recursos/Formato-Oferta-audIT/subdocumentos/07-plan-trabajo/formularios/T-14.tex#L74) · [T-15, capacidad por rol](https://github.com/mvergaral/audIT/blob/4da4195/recursos/Formato-Oferta-audIT/subdocumentos/07-plan-trabajo/formularios/T-15.tex#L105) · [T-15, actividad A15](https://github.com/mvergaral/audIT/blob/4da4195/recursos/Formato-Oferta-audIT/subdocumentos/07-plan-trabajo/formularios/T-15.tex#L209).

#### Cobertura del expediente entre M16 y M20

T-14 exige medir desde M16 el tiempo de respuesta de las verificaciones del paquete 12.1. S7 sitúa el inicio de la mesa de servicio en M16 y asigna al frente de Etapa 1 en producción la mesa, la guardia y las correcciones durante M19–M20. Con esas referencias, D2 propone el siguiente cruce para verificar la cobertura de la medición y del soporte técnico.

| Periodo | Cobertura propuesta | Comprobación para D2 |
| --- | --- | --- |
| M16 | A19/H7 para el paso a producción y A21 para la estabilización posterior, según la fecha efectiva del traspaso. Mesa de servicio de Etapa 1 como canal de atención. | Ubicar el inicio de la medición del 12.1, la puesta en servicio del emisor y verificador y la asignación de Software, SRE y Seguridad durante el traspaso. |
| M17 | A21, estabilización de Etapa 1 dentro de 11.4. | Identificar las tareas de medición, correcciones y permisos/firma dentro de la carga de estabilización. |
| M18 | Continuidad del frente de Etapa 1 en producción. La ventana de 11.4 en T-14 termina en M17. | Identificar la fila y los responsables que cubren el soporte de M18, donde el plan revisado solo muestra dotación global de 30 personas. |
| M19–M20 | Frente de Etapa 1 en producción, con 12 personas según S7. | Identificar quién monitorea la verificación y quién atiende correcciones, restauración y permisos/firma en cada mes. |

La referencia técnica de 12 h/mes de D3 aplica a M21–M56. Para M16–M20, registrar por mes la carga ya asignada a medición, atención y correcciones, separando las intervenciones puntuales de activación y traspaso de la demanda recurrente. El costo de personal de este tramo sigue pendiente de esa asignación. Los pagos de firma y nube se calendarizan desde la fecha real de activación.

Fuentes: [T-14, paquetes 11.2, 11.4 y 12.1](https://github.com/mvergaral/audIT/blob/4da4195/recursos/Formato-Oferta-audIT/subdocumentos/07-plan-trabajo/formularios/T-14.tex#L71) · [T-15, actividades A19 y A21](https://github.com/mvergaral/audIT/blob/4da4195/recursos/Formato-Oferta-audIT/subdocumentos/07-plan-trabajo/formularios/T-15.tex#L213) · [S7, frentes de M19–M20](https://github.com/mvergaral/audIT/blob/4da4195/recursos/Formato-Oferta-audIT/subdocumentos/07-plan-trabajo/contenido.tex#L315) · [D3, operación y tratamiento de M21](https://linear.app/audit-fep/document/d3-insumos-economicos-y-pendientes-verificados-informe-3-12-11-2026-31d849dd13ef).

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

#### Reparto del recupero entre Curimón y el transportista

[S13](https://github.com/mvergaral/audIT/blob/4da4195/recursos/Formato-Oferta-audIT/subdocumentos/13-innovaciones/contenido.tex#L373) establece que el porcentaje se fija en el anexo de adhesión y lo aprueba el Comité Ejecutivo en M2. La [regla RN-08 de T-12](https://github.com/mvergaral/audIT/blob/4da4195/recursos/Formato-Oferta-audIT/subdocumentos/03-solucion/formularios/T-12.tex#L596) suma la parte pactada de la espera recuperada en la liquidación del transportista. No se encontró un porcentaje pactado en las fuentes revisadas, incluidos el aporte económico de D1 y [AUD-9](https://linear.app/audit-fep/issue/AUD-9).

| Concepto | Fórmula para la planilla | Estado |
| --- | --- | --- |
| Recupero bruto elegible | Monto objetado elegible × tasa de recupero | CLP 120.700.000/año como referencia de régimen, a partir del 50 % de D1. |
| Incentivo pagado al transportista | Recupero bruto elegible × porcentaje de reparto pactado | Parámetro pendiente. El 50 % de D1 corresponde a la tasa de recupero. |
| Monto retenido por Curimón tras el reparto | Recupero bruto elegible − incentivo al transportista | Pendiente del porcentaje. Si se calcula un beneficio económico neto, descontar además los costos incrementales a cargo de Curimón que correspondan al mismo período. |

Usar para el cálculo la cifra exacta de CLP 120.700.000/año. La multiplicación por tres da CLP 362.100.000 antes del reparto si se mantienen 36 meses a régimen. Los CLP 360.000.000 del aporte de D1 son la referencia redondeada. La distribución mensual requiere acordar cuándo se cobra el recupero respaldado. Registrar los pagos al transportista en el mes que corresponda a la liquidación y mantener el beneficio fuera de los ingresos de audIT.

**Responsabilidad.** D2 mantiene la fórmula y deja el porcentaje sin valor hasta que se acuerde el supuesto de oferta con D1 y se concilie con el anexo de adhesión. D1 usa en AUD-9 el recupero bruto, el incentivo y el monto retenido que se acuerden con D2. El porcentaje contractual se aprueba por el Comité Ejecutivo según S13.

### Cruce actualizado con D4, T-11 y S3

La respuesta más reciente de D4 actualiza el criterio histórico de AUD-32 y AUD-39 para conectividad e instalación. Las aclaraciones del Informe 3, §9, incluyen en el flujo la instalación, configuración e integración ejecutadas por el proponente. D4 informa ejecución con personal propio de audIT y conectividad pagada por audIT. La revisión de D2 se limita a la valorización y a su trazabilidad.

| Concepto | Cobertura y pagador | Pendiente para D2 |
| --- | --- | --- |
| Equipos en comodato | Los 34 camiones de terceros sin equipo están incluidos en los 182 del T-11. S3, modalidad completa, también ofrece el equipo a quien lo pida. Entre los terceros que ya tienen equipo propio, D4 identifica hasta 192 potenciales solicitantes, sin previsión de demanda. D4 informa CLP 900.000 netos por equipo adicional como referencia, más instalación y plan mensual. | Confirmar el alcance o tope, el pagador de los equipos adicionales, la cantidad, el mes y el respaldo del precio. No volver a cargar los 34 equipos base. |
| Instalación, soporte y retiro | audIT asume estos conceptos. La instalación y el retiro son trabajo de personal propio. Un retiro comprende retiro físico, borrado de datos y reinstalación en otro camión. | Estimar horas por perfil y evento y tasa de rotación como supuesto explícito. Valorizar en recursos humanos y conciliar con el despliegue y soporte base. |
| Conectividad | audIT paga los planes LTE y los mensajes Iridium. Los 34 planes y mensajes del grupo base ya están dentro de la estimación para 182 equipos. | Medir el diferencial por altas adicionales o períodos de pago que el presupuesto base no cubra. D4 advierte que el plan sigue activo fuera de los viajes y que Iridium exige 12 meses de contrato. Registrar compromisos residuales solo si no están ya en el presupuesto y no se reutiliza el plan. |
| Reposición | D4 no prevé repuestos adicionales. El uso normal se cubre con el stock de 19 unidades del mandante. Por negligencia paga el transportista. | Confirmar en el anexo el monto a cargo del transportista. Conciliar el consumo de stock sin volver a cargarlo como compra. |

Fuentes: respuesta de coordinación de D4, aclaraciones del Informe 3 §9, T-11, S3 modalidad completa, y antecedentes de cobertura base de [AUD-32](https://linear.app/audit-fep/issue/AUD-32) y [AUD-39](https://linear.app/audit-fep/issue/AUD-39). La demanda adicional y la rotación siguen abiertas. La referencia de precio por equipo se documenta para el análisis y queda fuera de las partidas oficiales.
### Criterio para el cupo adicional de comodato

D2 aprobó preparar un cupo limitado de altas adicionales, con cantidad pendiente de aprobación. Los 34 equipos ya cubiertos se mantienen en la base. Los 192 camiones de terceros con equipo propio representan la población potencial informada por D4. La demanda efectiva sigue pendiente. Al precio referencial de CLP 900.000 netos por equipo, 192 altas representan CLP 172.800.000 solo en hardware. La cifra queda como exposición máxima de referencia, fuera de la valorización oficial.

| Componente por alta adicional | Cálculo | Dato pendiente |
| --- | --- | --- |
| Equipo | Precio neto unitario × unidades adicionales | Cotización y pagador de la compra adicional. |
| Instalación propia | Suma de horas por perfil × costo interno por hora | Horas por alta, perfiles, costos y capacidad disponible por mes en T-15. |
| Conectividad a cargo de audIT | Activación nueva de Iridium más meses adicionales facturados de LTE e Iridium, calculados por separado con las referencias de AUD-33. | Fecha de alta, confirmación de precios y condiciones de permanencia y reasignación. Contar cada mes facturado una vez. |
| Soporte, retiro y reasignación | Horas adicionales de soporte por perfil × costo interno, más retiros esperados × costo por evento de retiro, borrado y reinstalación | Horas por actividad y supuesto de rotación. Conciliar con las horas base ya presupuestadas. |

Para proponer el cupo, calcular cuántas altas permite financiar el presupuesto disponible de cada pagador con sus costos incrementales, cuántas permite instalar el personal propio en los meses habilitados y cuántas solicitudes son elegibles. El menor de esos límites determina el máximo proponible. Verificar el costo mensual y acumulado antes de presentar la cantidad a aprobación. Una vez aprobados el cupo y sus condiciones, D2 debe alinear S3 y la planilla económica.

#### Hardware por alta adicional

El [presupuesto vigente de D4](https://github.com/mvergaral/audIT/blob/8ae8c27/Informe-3/d4/4.1-presupuesto-equipos.md#L134) usa los siguientes precios unitarios netos para el juego a bordo del despliegue base. D2 toma el mismo juego como referencia para dimensionar una alta que requiera equipo nuevo. Los precios son de lista, sin flete ni internación, y el lector usa un modelo equivalente como referencia. Falta confirmar la configuración y el precio del lote adicional antes de cargarlo.

| Componente del kit | Precio de origen | Referencia unitaria neta (CLP) |
| --- | ---: | ---: |
| Equipo a bordo iWave G26I | EUR 454,31 | 454.310 |
| Módem Iridium Edge | USD 359,00 | 323.100 |
| Lector CAN Technoton CANCrocodile | EUR 47,00 | 47.000 |
| Lector RFID DESFire (referencia equivalente GeoVision IP66) | USD 83,99 | 75.591 |
| **Total del kit** | | **900.001** |

[S3](https://github.com/mvergaral/audIT/blob/4da4195/recursos/Formato-Oferta-audIT/subdocumentos/03-solucion/contenido.tex#L871) y [T-12, decisión 05](https://github.com/mvergaral/audIT/blob/4da4195/recursos/Formato-Oferta-audIT/subdocumentos/03-solucion/formularios/T-12.tex#L633) asignan al mandante la compra del equipo en comodato. [AUD-39](https://linear.app/audit-fep/issue/AUD-39) ubica el hardware de campo adquirido por el mandante en la hoja informativa, fuera del flujo de audIT. Aplicar ese criterio como referencia al analizar el cupo. La cantidad y la disponibilidad presupuestaria para las compras adicionales siguen pendientes. Las 19 unidades de reposición y los 22 kits de crecimiento ya tienen un destino en el presupuesto base. Para una reasignación, registrar la disponibilidad de un kit existente antes de sumar una compra.

#### Conectividad por alta adicional

Referencias netas de [AUD-33, conectividad](https://github.com/mvergaral/audIT/blob/8ae8c27/Informe-3/d4/4.2-nube-conectividad.md#L107), convertidas con los CLP 900 por USD de [E-24](https://github.com/mvergaral/audIT/blob/4da4195/texto/FEP01_26_Bases_Administrativas_TFEP_01_2026_3.md#L2404). La asignación a audIT se confirma en [AUD-39](https://linear.app/audit-fep/issue/AUD-39).

| Concepto | Costo neto de referencia | Cuándo imputarlo |
| --- | ---: | --- |
| Activación Iridium | CLP 28.350 por alta (USD 31,50) | Una vez, si se cobra una activación nueva. |
| Plan Iridium 25 KB | CLP 33.075 por mes (USD 36,75) | Meses adicionales facturados. D4 informa un contrato de 12 meses. |
| Plan LTE M2M | CLP 3.000 por mes | Meses adicionales facturados. Es un estimado de D4 pendiente de cotización. |

**Fórmula por alta.** CLP 28.350 × activaciones nuevas cobradas + CLP 33.075 × meses adicionales de Iridium + CLP 3.000 × meses adicionales de LTE. Con ambos planes facturados, el costo recurrente de referencia es CLP 36.075 al mes. Una activación nueva con 12 meses de ambos planes suma CLP 461.250 netos de conectividad. Los 12 meses de LTE se usan en ese cálculo para comparar el mismo período. La permanencia informada corresponde a Iridium.

Imputar únicamente el diferencial sobre el [calendario base de D4](https://github.com/mvergaral/audIT/blob/8ae8c27/Informe-3/d4/4.6-calendario-compras.md), que ya considera los 34 equipos de comodato dentro de los 182 y el crecimiento previsto. Cuando se retire y reasigne un equipo, verificar si conserva la línea y la activación antes de sumar otra. Si un plan sigue facturándose tras el retiro, incorporar solo los meses de compromiso que aún no estén en el calendario. Separar los pagos dentro de M1–M56 de cualquier compromiso que se extienda más allá de M56. Para proyectar el total del cupo siguen pendientes el número y mes de las altas, las condiciones de reasignación, la mano de obra y la disponibilidad presupuestaria para el lote adicional.

**Subtotal de referencia del primer año.** Con un kit nuevo y una activación nueva, más 12 meses facturados de ambos planes, los dos componentes suman CLP 1.361.251 netos. Para evaluar el cupo, mantener separados CLP 900.001 de compra de hardware bajo el criterio de S3 y T-12 y CLP 461.250 de conectividad a cargo de audIT. Quedan por valorizar las horas de instalación, soporte y retiro y por confirmar los cargos adicionales de la compra y del servicio, si corresponden.

#### Conciliación de soporte y retiro

| Concepto | Cobertura base comprobada | Tratamiento para un alta adicional |
| --- | --- | --- |
| Soporte externo y mantención de hardware | [AUD-34](https://github.com/mvergaral/audIT/blob/8ae8c27/Informe-3/d4/4.3-mantencion-operacion.md#L14) estima el 12 % anual del valor del hardware base en la hoja de proveedores de audIT. Su presupuesto global comienza en M13. | D2 aprobó como referencia provisional CLP 900.001 × 12 % ÷ 12 ≈ CLP 9.000 netos por mes de cobertura incremental. Confirmar el inicio efectivo de cobertura y la garantía del kit adicional antes de calendarizar. Verificar si el proveedor ya incluye ese equipo antes de sumar el importe. |
| Personal propio de instalación | El paquete 4.2 de T-14 cubre los 182 montajes base. AUD-32 identifica cantidades y ventanas y mantiene pendientes las horas unitarias. | Usar la ficha de instalación para identificar las horas por perfil de las altas adicionales y calcular su costo con AUD-14. |
| Personal propio de soporte, retiro y reinstalación | T-15 asigna 320 h/mes al ciclo de vida del equipo a bordo (EDT 13.3) en M21–M56. La cifra es la asignación total del paquete. | Revisar si el esfuerzo por evento cabe en las horas ya presupuestadas. Cuantificar solo las horas adicionales. Faltan el esfuerzo por evento, la cantidad esperada de retiros y la carga mensual del equipo. |
| Borrado y disposición final | AUD-34 incluye un servicio de gestor autorizado en M56. | Distinguir la disposición final de un retiro con borrado y reutilización durante el contrato. Usar el costo externo solo cuando se incurra en ese servicio y registrar el trabajo interno en la ficha de retiro. |

[AUD-32, horas pendientes](https://github.com/mvergaral/audIT/blob/8ae8c27/Informe-3/d4/4.1-presupuesto-equipos.md#L205) · [T-14, paquete 4.2](https://github.com/mvergaral/audIT/blob/4da4195/recursos/Formato-Oferta-audIT/subdocumentos/07-plan-trabajo/formularios/T-14.tex#L42) · [T-15, continuidad operacional](https://github.com/mvergaral/audIT/blob/4da4195/recursos/Formato-Oferta-audIT/subdocumentos/07-plan-trabajo/formularios/T-15.tex#L87)

**Costo de referencia por alta y pagador.** El mandante considera CLP 900.001 por kit nuevo, más los gastos de compra que correspondan. Para audIT, sumar CLP 28.350 por activación nueva de Iridium si se cobra, CLP 33.075 por mes incremental de Iridium, CLP 3.000 por mes incremental de LTE y CLP 9.000 por mes de soporte externo adicional que corresponda. A ese subtotal se suma la mano de obra propia incremental, valorizada por perfil. Los meses de soporte se determinan según la cobertura de cada alta, con independencia de los meses de conectividad. Las cifras son referencias para dimensionar el cupo. La partida oficial sigue pendiente.

**Datos para cerrar mano de obra.** D4 entregó una estimación de instalación, retiro, borrado y reinstalación. D2 registra las horas en la ficha, concilia la carga con T-15 y la valoriza con AUD-14. La preparación en banco para el montaje se imputa provisionalmente al Técnico instalador. Faltan los perfiles de retiro, borrado, revisión del kit retirado y montaje de balizas, así como la rotación de transportistas. Los tiempos y la asignación de la preparación se validan en el piloto de M6.

### Capacidad de instalación según el calendario base

El [paquete 4.2 de T-14](https://github.com/mvergaral/audIT/blob/4da4195/recursos/Formato-Oferta-audIT/subdocumentos/07-plan-trabajo/formularios/T-14.tex#L42) compromete 182 montajes: 148 camiones propios y 34 de terceros sin equipo. Las 19 unidades de reposición y las 22 de crecimiento se controlan por separado y solo ocupan agenda cuando corresponde una intervención. [S4, despliegue de equipos](https://github.com/mvergaral/audIT/blob/4da4195/recursos/Formato-Oferta-audIT/subdocumentos/04-arquitectura/contenido.tex#L965)

| Ventana | Trabajo base documentado | Qué falta para calcular capacidad adicional |
| --- | --- | --- |
| M6 | Piloto de 10 camiones y entrada de cuatro analistas de implantación para A11. | Duración y horas de personal por montaje validado en el piloto, por familia de camión. |
| M7–M9 | Completar la flota propia hasta M9. S4 prevé iniciar desde M7 los montajes de terceros adheridos. | Distribución de los montajes base por terminal y mes, con turnos y horas disponibles del personal habilitado. |
| M10 | Ventana de montaje según T-14/T-18. Los siete analistas están desde M10 y también cubren capacitación. | Agenda base restante y horas que quedan después de capacitación y otras funciones de terreno. |
| M11–M15 | Pausa de montaje en S4. La parte de A18 en M13–M15 corresponde a integración por plataforma según S7. | Capacidad de montaje en esta ventana: cero por calendario. |
| M16–M18 | Reanudación para terceros pendientes. M16 y M17 coinciden con estabilización; T-15 reduce la dotación global en M18. | Pendientes de la cohorte base, turnos disponibles y dotación efectiva de montaje por terminal, en particular para M18. |

S7 calcula que A11 debe atender 148 camiones propios en 60 días hábiles, cerca de 2,47 por día entre los cinco terminales. Esa cifra representa el ritmo del trabajo base. T-15 presenta dotaciones agregadas y asignación por rol para M13–M15. La holgura de 40 días de A18 en la red CPM es margen de plazo. Estas fuentes no cuantifican horas libres de instalación. La revisión del Informe 3 también pide, en PLA-11, separar integración y montaje en la red con recursos y capacidad por terminal. [S7, estimación de montaje](https://github.com/mvergaral/audIT/blob/4da4195/recursos/Formato-Oferta-audIT/subdocumentos/07-plan-trabajo/contenido.tex#L189) · [T-15, A18](https://github.com/mvergaral/audIT/blob/4da4195/recursos/Formato-Oferta-audIT/subdocumentos/07-plan-trabajo/formularios/T-15.tex#L212) · [Revisión PLA-11](https://github.com/mvergaral/audIT/blob/4da4195/Informe-3/AUDIT-Anexo-Art46-Informe3-Revision-Independiente.md#L123)

Para cada terminal, mes y perfil instalador, registrar las horas habilitadas en turnos con visita normal, las horas de los montajes base, las demás tareas comprometidas y las horas requeridas por alta adicional. Restar las horas comprometidas antes de convertir el saldo en altas enteras. Limitar el resultado por el perfil más restrictivo y por la coincidencia de ventana, camión, kit y personal. Medir en el piloto M6 el esfuerzo por familia de camión, incluida preparación, montaje, configuración, prueba y cierre del acta. Registrar aparte los reintentos. La medición permitirá sustituir la estimación por una duración observada. Hasta conciliar la agenda base y el esfuerzo unitario, la capacidad adicional en las ventanas habilitadas queda sin cuantificar.

#### Datos para completar la agenda de D2

El presupuesto adjunto a [AUD-32](https://linear.app/audit-fep/issue/AUD-32) separa 10 kits del piloto y 172 kits del resto del despliegue, más 19 de reposición. Los 172 son una cantidad de suministro. La compra de esos kits en M6 no fija el mes ni el terminal de cada instalación. Si los 10 montajes del piloto se aceptan, quedan 172 montajes base por distribuir, incluidos los de terceros que aún estén pendientes. Los 34 equipos en comodato forman parte de los 182. El [Gantt de D2](https://github.com/mvergaral/audIT/blob/4da4195/Informe-2/D2/02_Gantt/02_Editables/Gantt_Completa_M01-M56.mmd) fija las ventanas del paquete 4.2. [AUD-37](https://linear.app/audit-fep/issue/AUD-37) pasó a En progreso y ya adjunta el calendario mensual de compras y servicios. [AUD-33](https://linear.app/audit-fep/issue/AUD-33) usa 10, 70, 130 y 182 equipos activos en M6, M7, M8 y M9 para estimar conectividad. Esa secuencia es un supuesto de facturación y todavía falta la agenda de montajes por terminal.

| Mes | Montajes base que debe reconciliar la agenda | Capacidad adicional verificable |
| --- | --- | --- |
| M6 | 10 del piloto, previstos. | Pendiente de agenda y esfuerzo por instalación. |
| M7 | Continuación de flota propia e inicio de terceros adheridos. | Pendiente. |
| M8 | Montajes de flota propia y terceros adheridos. | Pendiente. |
| M9 | Cierre previsto de la flota propia. | Pendiente. |
| M10 | Cierre de la primera ventana de montaje, con capacitación en paralelo. | Pendiente. |
| M11–M15 | Cero montajes a bordo según el calendario base. | 0 durante la pausa. |
| M16 | Reanudación del montaje de terceros pendientes. | Pendiente. |
| M17 | Montaje de terceros pendientes durante la estabilización. | Pendiente. |
| M18 | Último mes de la segunda ventana del paquete 4.2. | Pendiente. |

**Agenda por terminal y mes.** Para cada terminal y turno, levantar responsable, perfiles habilitados, horas disponibles, camiones base con visita programada, horas ya comprometidas y ventanas simultáneas de camión, kit, puesto y personal. Incluir los 182 montajes base una sola vez y registrar aparte reposiciones, crecimiento, retiros y reinstalaciones. Si falta alguno de los datos, la capacidad de ese mes queda pendiente.

**Esfuerzo por instalación.** Registrar por familia de camión los minutos de ocupación del puesto y, por separado, las horas de cada perfil. Una intervención con dos personas durante una hora consume una hora de puesto y dos horas-persona. Incluir preparación, montaje, configuración, prueba y acta. Un [borrador histórico de S3](https://github.com/mvergaral/audIT/blob/4da4195/Informe-2/D2/90_Archivo/01_Borradores_anteriores/AUDIT-Subdocumento3.md#L242) menciona un objetivo inferior a 45 minutos. No contiene medición ni desglose de personal para usarlo en la valorización. Para estimar antes del piloto, solicitar una prueba cronometrada o un antecedente técnico equivalente y someter el supuesto resultante a revisión de D2.

**Cálculo.** Por terminal y mes, descontar de cada recurso sus compromisos base y dividir el saldo por el requerimiento de ese recurso por alta. Redondear cada cociente hacia abajo. Tomar el mínimo entre los resultados por perfil, por puesto y por visitas elegibles. Las horas de una misma cuadrilla compartida se asignan primero a sus turnos en cada terminal para impedir que aparezcan disponibles dos veces. Conciliar luego con kits disponibles y presupuesto para proponer el cupo.

#### Ficha D2 de horas por instalación

Completar una ficha por intervención. Identificar terminal, mes y turno, familia de camión, tipo de intervención (montaje base, alta adicional, retiro o reinstalación), orden de trabajo, ventana de la visita normal, kit y resultado de la prueba. Indicar si cada dato viene de una estimación técnica, una prueba cronometrada o un montaje del piloto. La instalación la ejecuta personal propio de audIT y D2 valoriza el esfuerzo en recursos humanos. El acta de montaje por camión es la evidencia del paquete 4.2. [Instalación interna, AUD-32](https://github.com/mvergaral/audIT/blob/8ae8c27/Informe-3/d4/4.1-presupuesto-equipos.md#L183) · [T-14, paquete 4.2](https://github.com/mvergaral/audIT/blob/4da4195/recursos/Formato-Oferta-audIT/subdocumentos/07-plan-trabajo/formularios/T-14.tex#L42)

| Actividad a registrar | Qué medir | Minutos de puesto | Personal y minutos efectivos por perfil |
| --- | --- | ---: | --- |
| Preparación | Confirmar orden, autorización y compatibilidad. Preparar y verificar kit y herramientas. Distinguir lo que se hace antes de que llegue el camión. | Por medir si ocupa puesto. | Por medir, aunque la tarea se haga fuera del puesto. |
| Montaje | Montar y conectar el equipo a bordo, módem, lector CAN y lector de tarjeta según la familia del camión. | Por medir. | Por medir. |
| Configuración | Asociar los dispositivos al camión, aplicar la configuración y habilitar las comunicaciones que correspondan. | Por medir si retiene el puesto. | Por medir. |
| Prueba y liberación | Verificar el funcionamiento del conjunto, registrar el resultado y liberar el camión. Identificar cualquier reintento. | Por medir. | Por medir. |
| Acta | Registrar la intervención y cerrar el acta con el resultado de la prueba. | Por medir si retiene el puesto. | Por medir. |
| Retiro por salida | Desmontar el kit, registrar el estado y el destino del equipo. | Por medir cuando corresponda. | Por medir por evento. |
| Borrado y reasignación | Registrar borrado y preparación para el siguiente camión. Si se reinstala, abrir una ficha de montaje vinculada al retiro. | Por medir si ocupa puesto. | Por medir por evento, con la reinstalación registrada en su propia ficha. |

**Cómo calcular.** Medir la ocupación desde que se reserva físicamente el puesto para el camión hasta que se libera, sin sumar dos veces tareas simultáneas. Para mano de obra, sumar los minutos de cada persona por perfil y dividir por 60. Incluir esperas cuando bloquean el puesto o mantienen personal asignado, e identificarlas por separado. El costo por intervención es la suma de las horas-persona de cada perfil multiplicadas por su costo interno aprobado en AUD-14. Para presupuestar altas adicionales, separar la mano de obra del alta inicial de los retiros y reinstalaciones, cuya frecuencia depende de la rotación. Conciliar las horas con T-15 para identificar el diferencial antes de incorporarlo a AUD-21.

Para validar la ficha, medir una intervención comparable de principio a fin y registrar qué tareas ocurrieron en paralelo, qué personal quedó comprometido y si el montaje se completó dentro de la visita normal. Si se dispone de tiempos de varias familias, conservarlos por separado antes de proponer un valor para planificar el cupo. El objetivo histórico de 45 minutos queda como referencia de ventana y no se imputa como horas-persona.

#### Estimación de D4 para instalación y retiro

Datos de coordinación de D4 transmitidos a D2. Son estimaciones previas a la medición del piloto de 10 camiones en M6. El bloque de instalación cubre el montaje del G26I, lector CAN, Iridium, lector de tarjeta y antenas, más prueba funcional y acta. Para calcular la capacidad del puesto, el piloto debe separar el tiempo ocupado de las tareas que se puedan realizar fuera del puesto.

| Actividad | Duración estimada | Personal | Esfuerzo por evento |
| --- | ---: | --- | ---: |
| Instalación a bordo | 140 min | 1 técnico instalador y 1 analista de implantación | 280 min-persona |
| Preparación en banco para instalar | 20 min | 1 Técnico instalador, asignación provisional de D2 | 20 min-persona |
| **Instalación completa del kit** | | | **300 min-persona = 5 h-persona** |
| Retiro físico del kit | 60 min | 2 personas, perfiles por confirmar | 120 min-persona |
| Borrado seguro del kit retirado | 15 min | 1 persona, perfil por confirmar | 15 min-persona |
| Revisión en banco del kit retirado | 20 min | 1 persona, perfil por confirmar | 20 min-persona |
| **Retiro, borrado y revisión** | | | **155 min-persona = 2 h 35 min-persona** |
| **Retiro completo más reinstalación** | | | **455 min-persona = 7 h 35 min-persona** |
| Montaje de una baliza | 15 min | 1 persona, perfil por confirmar | 15 min-persona |

**Base a conciliar en AUD-14 y AUD-15.** Aplicar las 5 h-persona por kit a los 182 montajes base del [paquete 4.2](https://github.com/mvergaral/audIT/blob/4da4195/recursos/Formato-Oferta-audIT/subdocumentos/07-plan-trabajo/formularios/T-14.tex#L42), incluidos los 34 equipos de terceros en comodato. Son 910 h-persona: 424 h 40 min de técnico instalador, 424 h 40 min de analista de implantación y 60 h 40 min de banco. El piloto representa 50 h-persona dentro de esas 910. El montaje de las [210 balizas base](https://github.com/mvergaral/audIT/blob/8ae8c27/Informe-3/d4/4.1-presupuesto-equipos.md#L190) representa otras 52 h 30 min-persona, que se imputan por separado. Los 192 camiones de terceros con equipo propio quedan fuera de este cálculo base. Los 22 kits y las 35 balizas de crecimiento siguen su propio calendario.

#### Valorización de mano de obra para AUD-14 y AUD-15

D2 aprobó tratar **Técnico instalador** y **Analista de implantación** como perfiles diferenciados. Ambos se declaran con su nombre y sus costos propios en la hoja de tarifas. [E-26](https://github.com/mvergaral/audIT/blob/4da4195/texto/FEP01_26_Bases_Administrativas_TFEP_01_2026_3.md#L2488) permite perfiles adicionales con rangos coherentes con su catálogo. Al revisar [AUD-14](https://linear.app/audit-fep/issue/AUD-14), [AUD-15](https://linear.app/audit-fep/issue/AUD-15) y el CSV de tarifas, todavía no constaban costos internos aprobados para estos roles.

| Recurso | Minutos-persona por instalación | Minutos-persona para 182 kits | Dato por completar |
| --- | ---: | ---: | --- |
| Técnico instalador | 140 | 25.480 | Costo interno por hora respaldado. |
| Analista de implantación | 140 | 25.480 | Costo interno por hora respaldado. |
| Preparación en banco | 20 | 3.640 | Técnico instalador, asignación provisional aprobada por D2 y sujeta a validación en M6. |
| **Total** | **300** | **54.600** | **910 h-persona.** |

- **Instalación por kit.** (160 × costo/h de Técnico instalador + 140 × costo/h de Analista de implantación) ÷ 60. Los 160 minutos del técnico incluyen el trabajo de banco. Para la base, aplicar a los 182 kits y conservar los 10 del piloto dentro de ese total.
- **Retiro con borrado y revisión.** (60 × costo/h del primer perfil de retiro + 60 × costo/h del segundo perfil de retiro + 15 × costo/h del perfil de borrado + 20 × costo/h del perfil de revisión) ÷ 60. Los perfiles se toman del registro efectivo. Si el evento termina en reinstalación, sumar una instalación completa. El importe del período depende de cuántos eventos se estimen con respaldo.
- **Montaje de balizas.** 52,5 h-persona para las 210 balizas base × costo/h del perfil que las instala. Registrar la carga aparte y conciliarla con T-15.

Los costos horarios se preparan en AUD-14 a partir del costo interno de cada perfil y se reutilizan en AUD-15 y AUD-21. Mantener trazados los montajes base como parte del presupuesto de personal. En AUD-21 registrar solo el costo de intervenciones adicionales del comodato tras verificar qué horas cubre T-15.

**Costos internos provisionales aprobados por D2.** La revisión del repositorio y de AUD-14 y AUD-15 no encontró una base de remuneraciones para estos perfiles. D2 aprobó estos valores como supuestos de presupuesto. Se usan los rangos de costo de [E-26](https://github.com/mvergaral/audIT/blob/4da4195/texto/FEP01_26_Bases_Administrativas_TFEP_01_2026_3.md#L2460) como referencias de coherencia para los dos roles adicionales, con CLP 40.000 por UF según E-24.

| Perfil propio de audIT | Costo interno provisional aprobado | Fundamento de la referencia |
| --- | ---: | --- |
| Técnico instalador | 0,40 UF/h = CLP 16.000/h | Coincide con el límite inferior del costo de Ingeniero Junior en E-26 (0,40–0,70 UF/h). Se usa como referencia para la ejecución técnica del montaje y las pruebas en terreno con un procedimiento definido, conservando el perfil propio. |
| Analista de implantación | 0,50 UF/h = CLP 20.000/h | Está en el rango de Analista / Diseñador Junior (0,30–0,60 UF/h) y coincide con el límite inferior del rango Senior (0,50–0,70 UF/h). Se usa como referencia para el rol de implantación en terreno durante la intervención, sin asignarle un nivel de antigüedad. |

Las 2 h 20 min de cada perfil suman CLP 84.000 por montaje a bordo. Los 20 minutos de preparación en banco del Técnico instalador agregan CLP 5.333,33. La instalación completa asciende a CLP 89.333,33 por kit: (160 × 16.000 + 140 × 20.000) ÷ 60. Para AUD-15, los 182 montajes base equivalen a CLP 16.258.667 redondeados al peso, incluidos CLP 893.333 para los 10 camiones del piloto. Calcular con precisión completa y redondear al final de cada total. Falta conciliar las horas y el monto con el presupuesto base de personal antes de cargarlo.

Para AUD-21, un alta con instalación completa incremental, kit nuevo y activación nueva con 12 meses de ambos planes tiene un subtotal referencial de CLP 550.583 para audIT (CLP 461.250 de conectividad y CLP 89.333,33 de instalación) y CLP 900.001 para el mandante por el kit, antes de los gastos de compra aplicables. Al costo de audIT se suma, según corresponda, CLP 9.000 por mes de cobertura incremental de soporte externo y la mano de obra incremental de retiro y reinstalación. Mantener fuera de este subtotal las intervenciones base y las que T-15 ya cubra.

Las balizas y los retiros se valorizan cuando se confirme el perfil efectivo de cada actividad. La tarifa de venta se determina por separado. Los valores quedan registrados como referencia de D2 para AUD-14, AUD-15 y AUD-21, con la carga oficial pendiente de conciliación.

#### AUD-15 · Conciliación de los 182 montajes base con T-15

La trazabilidad del montaje base es **EDT 4.2, actividades A11 y A18**. T-14 fija 182 montajes en las ventanas M6–M10 y M16–M18. S7 incorpora cuatro analistas de implantación en M6 para A11 y siete desde M10 para capacitación y otras funciones de terreno. T-15 agrega 8.800 horas en el elemento 4 «Equipo a bordo» y 12.800 en el elemento 11 «Implantación». Estos totales incluyen otros trabajos y no muestran la asignación de las 910 horas a los subpaquetes ni la carga de Técnico instalador por terminal. Para conciliar el costo base, registrar las horas de cada perfil contra 4.2 y verificar en qué fila del presupuesto de personal se financian, evitando volver a sumarlas en Implantación. [T-14, paquete 4.2](https://github.com/mvergaral/audIT/blob/4da4195/recursos/Formato-Oferta-audIT/subdocumentos/07-plan-trabajo/formularios/T-14.tex#L42) · [T-15, horas por EDT](https://github.com/mvergaral/audIT/blob/4da4195/recursos/Formato-Oferta-audIT/subdocumentos/07-plan-trabajo/formularios/T-15.tex#L57) · [S7, dotación de terreno](https://github.com/mvergaral/audIT/blob/4da4195/recursos/Formato-Oferta-audIT/subdocumentos/07-plan-trabajo/contenido.tex#L276)

**Referencia mensual provisional aprobada por D2.** Usar esta distribución en AUD-15 mientras se valida la agenda por terminal. AUD-33 supone 10, 70, 130 y 182 equipos activos de M6 a M9 para calcular conectividad. La referencia asume que cada alta se monta en su mes de activación. M6 coincide con los 10 montajes del piloto previstos por D4. M7–M9 se derivan de las diferencias del supuesto de facturación. La aprobación corresponde al uso de la referencia en la preparación del presupuesto. [AUD-33, supuesto de equipos activos](https://github.com/mvergaral/audIT/blob/8ae8c27/Informe-3/d4/4.2-nube-conectividad.md#L124) · [AUD-32, ventanas de instalación](https://github.com/mvergaral/audIT/blob/8ae8c27/Informe-3/d4/4.1-presupuesto-equipos.md#L183)

| Mes | Montajes del mes | Técnico instalador, con banco | Analista de implantación | Horas-persona | Costo base de referencia (CLP) |
| --- | ---: | ---: | ---: | ---: | ---: |
| M6, piloto | 10 | 26 h 40 min | 23 h 20 min | 50 | 893.333,33 |
| M7 | 60 | 160 h | 140 h | 300 | 5.360.000,00 |
| M8 | 60 | 160 h | 140 h | 300 | 5.360.000,00 |
| M9 | 52 | 138 h 40 min | 121 h 20 min | 260 | 4.645.333,33 |
| **Total** | **182** | **485 h 20 min** | **424 h 40 min** | **910** | **16.258.666,67** |

El total monetario usa la precisión completa del costo unitario. Si quedan montajes base pendientes al cierre de M9, conservar el total de 182 y trasladar sus horas y costos a las ventanas de M10 o M16–M18. Mantener M11–M15 sin montaje según S4. Las balizas y el crecimiento tienen su propio alcance y calendario.

Para confirmar la agenda definitiva faltan el desglose por terminal y perfil y la confirmación de que la activación coincide con el montaje. En M7 y M8, la referencia exige 160 h de Técnico instalador y 140 h de Analista de implantación al mes entre todos los terminales, incluyendo la preparación en banco. Con las 160 h mensuales nominales de T-15, eso equivale a 1,00 mes-persona de Técnico instalador y 0,875 mes-persona de Analista de implantación en cada uno de esos meses. Estas equivalencias expresan la carga, cuya cobertura se debe verificar contra los turnos, las demás tareas y la coincidencia de ambos perfiles durante los montajes. Hasta conciliar turnos y asignaciones, la capacidad restante para AUD-21 sigue sin cuantificar. AUD-15 continúa pendiente del cierre de AUD-14 en Linear.

#### Agenda de montaje por terminal y turno

Priorizar M7 y M8, que concentran 60 montajes base cada uno en la referencia aprobada. Repetir la misma ficha en M6, M9, M10 y M16–M18 según las intervenciones previstas. S7 identifica cuatro analistas que se incorporan en M6 y siete desde M10. El compromiso de 35 turnos semanales corresponde a la cobertura de relevo desde la capacitación hasta la estabilización. Para calcular el cupo hacen falta los turnos efectivos de montaje y las ventanas que comparten ambos perfiles, el puesto y el camión. El calendario de compras de AUD-37 no incluye personal. [S7, turnos de relevo](https://github.com/mvergaral/audIT/blob/4da4195/recursos/Formato-Oferta-audIT/subdocumentos/07-plan-trabajo/contenido.tex#L276) · [AUD-37](https://linear.app/audit-fep/issue/AUD-37)

Completar una fila por terminal, fecha y turno. Para cada perfil, indicar las horas programadas, las comprometidas en otras funciones y la asignación a montajes base. Registrar si el Técnico instalador comparte turno o se traslada entre terminales. Los campos quedan pendientes hasta contar con una agenda respaldada.

| Terminal | Fecha y turno | Técnico disponible y horas | Analista disponible y horas | Montajes base y otras tareas | Ventanas coincidentes de camión, puesto, kit y ambos perfiles |
| --- | --- | --- | --- | --- | --- |
| San Bernardo | Pendiente | Pendiente | Pendiente | Pendiente | Pendiente |
| Antofagasta | Pendiente | Pendiente | Pendiente | Pendiente | Pendiente |
| Talca | Pendiente | Pendiente | Pendiente | Pendiente | Pendiente |
| Los Ángeles | Pendiente | Pendiente | Pendiente | Pendiente | Pendiente |
| Puerto Montt | Pendiente | Pendiente | Pendiente | Pendiente | Pendiente |

**Control de carga base.** Conciliar las filas con 60 kits en M7 y 60 en M8, sin volver a sumar en Implantación las horas ya imputadas a Equipo a bordo. Para cada mes, verificar 140 horas de trabajo técnico durante el montaje más 20 horas de preparación en banco y 140 horas de Analista de implantación. Las 20 horas de banco pueden programarse antes de la visita, si se mantiene la trazabilidad de cada kit y no se usa el mismo tiempo técnico en otro compromiso. Si se mueve una instalación, trasladar también su carga y su costo y volver a conciliar con el calendario de activaciones.

**Control del cupo.** Después de asignar la base y las otras tareas, un alta adicional requiere 160 minutos de Técnico instalador y 140 de Analista de implantación. Además requiere una ventana continua para la intervención a bordo, usando los 140 minutos estimados de D4 como referencia sujeta a medición. Contar únicamente altas que se puedan calendarizar con los recursos coincidentes y la preparación previa. Las horas dispersas entre turnos o terminales se pueden sumar para un presupuesto agregado, pero solo sustentan capacidad cuando forman intervenciones completas. Revisar el piloto M6 para validar la duración de la ocupación del puesto antes de comprometer el cupo.

#### Propuesta provisional de turnos base para M7 y M8

**Responsable: D2, en AUD-15 y el paquete EDT 4.2 de S7/T-15.** El Líder de Implantación coordina la agenda y D2 concilia dotación, carga y costo. D4 aporta la validación técnica del montaje, el kit y los tiempos de intervención. Curimón es la fuente de las visitas normales, la autorización operativa y la disponibilidad de puestos por terminal. D2 usa la capacidad remanente que se acredite para proponer el cupo en AUD-21.

**Supuesto de trabajo.** Distribuir provisionalmente los 60 montajes base de cada mes en cinco terminales, con 12 por terminal mientras se obtiene el tráfico efectivo. Dividir cada mes en tres bloques de cuatro ventanas habilitadas por terminal. Los bloques sirven para repartir la carga y no representan semanas de calendario. Se asigna un montaje a cada ventana coincidente con una visita normal, un puesto, un kit y un Técnico instalador y Analista de implantación disponibles. No hay fechas, matrículas ni cuadrillas confirmadas. La cuota uniforme es una decisión de planificación preliminar y se ajusta a la demanda de cada terminal sin cambiar el objetivo mensual sin revisión de D2.

| Terminal | Bloque 1 | Bloque 2 | Bloque 3 | Montajes en cada mes | Horas de Técnico instalador, con banco | Horas de Analista de implantación |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| San Bernardo | 4 | 4 | 4 | 12 | 32 | 28 |
| Antofagasta | 4 | 4 | 4 | 12 | 32 | 28 |
| Talca | 4 | 4 | 4 | 12 | 32 | 28 |
| Los Ángeles | 4 | 4 | 4 | 12 | 32 | 28 |
| Puerto Montt | 4 | 4 | 4 | 12 | 32 | 28 |
| **Total en M7 o M8** | **20** | **20** | **20** | **60** | **160** | **140** |

Cada terminal requiere 28 horas mensuales de intervención con ambos perfiles y cuatro horas previas de preparación técnica en banco. Para cada ventana, reservar provisionalmente 140 minutos de puesto y de ambos perfiles, y programar los 20 minutos de banco fuera del puesto. Repetir el esquema en M7 y M8 da 120 montajes y 600 h-persona. La estimación se valida en el piloto M6.

**Asignación a turnos reales.** Curimón debe confirmar el día y horario de cada visita. D2 escalona las ventanas para evitar asignar simultáneamente la misma cuadrilla o superar la dotación confirmada. S7 menciona cuatro analistas desde M6. El esquema requiere coordinar cinco terminales sin asumir cinco parejas simultáneas ni traslados instantáneos. Reservar tiempo de traslado cuando el personal sea compartido, descontar las otras tareas y excluir los congelamientos aplicables, incluido el cierre mensual y las restricciones de Fiestas Patrias en M8. Si un terminal no tiene visitas elegibles suficientes, primero reasignar la cuota a otro terminal con una visita normal confirmada y después reprogramar lo que reste en las ventanas habilitadas. Registrar el efecto en horas, costos y activaciones. [S7, dotación de terreno](https://github.com/mvergaral/audIT/blob/4da4195/recursos/Formato-Oferta-audIT/subdocumentos/07-plan-trabajo/contenido.tex#L276) · [Caso, RT-10.05](https://github.com/mvergaral/audIT/blob/4da4195/texto/FEP03_10_26_Caso_10_Transporte_de_Carga_Bases_Tecnicas_del_Caso.md#L881)

La propuesta sirve para revisar la carga de los montajes base. El cupo adicional requiere una agenda confirmada con horas disponibles y visitas elegibles después de cubrir esa carga.

## Integración y controles

- Registrar por línea mes, cantidad, unidad, costo unitario y total, moneda, IVA, fuente fechada, pagador, frecuencia y referencia EDT o contractual. Convertir a CLP con los parámetros acordados cuando corresponda.
- Conciliar el total mensual y el acumulado por innovación. El detalle puede identificar partidas que ya están en el presupuesto base para demostrar su cobertura sin sumarlas de nuevo. Separar el reparto al transportista del presupuesto de audIT y evitar descontarlo dos veces.
- Pendientes: comprobar la reserva de las 480 h por perfil y mes en 12.1, incluida la cobertura de las 64 h de marcha blanca en E1/A15, validar capacidad libre por perfil en 13.2 y 13.4, conciliar la cobertura de M16 a M20, cotizar la firma automática y estimar el consumo incremental. Para la innovación 4 faltan el esfuerzo incremental de software, el alcance adicional del comodato, sus cantidades, la rotación y los costos internos por actividad. Falta confirmar con D1 y D2 la proporción pactada de reparto.
- Las claves `innovacion-1-inversion`, `innovacion-1-costo`, `innovacion-1-beneficio`, `innovacion-4-inversion`, `innovacion-4-costo` e `innovacion-4-beneficio` permanecen vacías hasta contar con respaldo. Confirmar la plantilla del mandante y sus celdas antes de ejecutar la comparación de planilla.

Fuentes internas de alcance y cronograma preliminar: T-19 fichas 1 y 4, S13 §§13.1 y 13.4, T-12 RN-08 y respuesta 05. Fuentes por conciliar antes de cargar cifras: T-15, T-11, E-26, parámetros económicos y cotizaciones.
