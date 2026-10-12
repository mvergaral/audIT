# Formulario T-19. Cartera de innovaciones

audIT, Empresa N.º 10. Licitación TFEP-01/2026, Caso 10 Transporte de Carga. Oferta Técnica, Sobre N.º 2. Informe Preparatorio 2. Archivo AUDIT-Formulario-T-19.pdf. Anexo del Subdocumento N.º 13, Innovaciones. Las fuentes están en las Referencias de ese subdocumento.

## Índice detallado

| Contenido | Página del PDF |
|---|---:|
| Ficha del documento | [3](AUDIT-Formulario-T-19.pdf#page=3) |
| T-19 Cartera de innovaciones | [5](AUDIT-Formulario-T-19.pdf#page=5) |
| Ficha T-19. Innovación tipo 1. Producto o servicio. Expediente verificable del transportista | [5](AUDIT-Formulario-T-19.pdf#page=5) |
| Ficha T-19. Innovación tipo 2. Proceso. Programación dinámica de intervenciones por oportunidad de patio | [7](AUDIT-Formulario-T-19.pdf#page=7) |
| Ficha T-19. Innovación tipo 3. Tecnológica o de arquitectura. Semirremolque conectado | [8](AUDIT-Formulario-T-19.pdf#page=8) |
| Ficha T-19. Innovación tipo 4. Modelo de negocio o de contratación. Esquema de adhesión y propiedad del dispositivo | [10](AUDIT-Formulario-T-19.pdf#page=10) |
| Ficha T-19. Innovación tipo 5. Experiencia de usuario, sostenibilidad o impacto social. Bienestar del conductor y descanso en parador seguro | [11](AUDIT-Formulario-T-19.pdf#page=11) |


## Innovación 1. Producto o servicio. Expediente verificable del transportista

| Campo | Contenido |
|---|---|
| Problema u oportunidad | 148 transportistas con 226 camiones y 258 conductores (Caso, numeral 14.1, p. 29), muchos de los cuales trabajan también para otros clientes (numeral 4.3, p. 9), no pueden acreditar ante terceros la jornada de sus conductores ni la vigencia de sus documentos. La solución produce esa evidencia para los viajes de Curimón, pero queda dentro del sistema del mandante |
| Tecnología o práctica | Documento firmado por el mandante con firma electrónica avanzada, con datos sólo del propio transportista, y servicio público de verificación que responde si el documento es auténtico y vigente sin revelar su contenido. La jornada de cada conductor entra sólo con su consentimiento. Credencial verificable como formato alternativo |
| Nivel de madurez | Escala de niveles de madurez tecnológica de 1 a 9. Firma electrónica avanzada con verificación en línea en nivel 9, formato comprometido. Credencial verificable entre los niveles 7 y 8, sólo si los destinatarios la aceptan |
| Fuentes | International Organization for Standardization (2013). Congreso Nacional de Chile (2002), Ley N.º 19.799. World Wide Web Consortium (2025). Ley N.º 21.719 (2024) |
| Dónde se inserta en la arquitectura | Servicio de emisión en el contexto Personas y cumplimiento, que consulta a Flota y activos. Servicio público de verificación detrás de la puerta de enlace. Firma desde la bóveda de claves. Emisión y consentimientos en el portal del transportista. Subdocumento 13, sección 13.1 |
| Paquetes de la EDT | EDT 12.1, sobre los paquetes 5.1 (Personas y cumplimiento) y 5.7 (Portal del transportista) |
| Mes del cronograma | Entrevistas a destinatarios y elección del formato en el mes 4. Construcción entre los meses 8 y 10. Disponible para la cohorte inicial en la marcha blanca de la Etapa 1 |
| Inversión requerida | Desarrollo de los servicios de emisión y de verificación sobre datos que la Etapa 1 ya produce |
| Efecto en el costo operacional | Certificado de firma del emisor y operación del servicio de verificación |
| Beneficio esperado | Incentivo de adhesión que no requiere pagar al transportista. Cada adherido amplía la jornada acreditada y la evidencia de espera que sostiene los cobros. Sin ingresos atribuidos en el flujo de caja |
| Indicador, línea base y meta | Transportistas adheridos que emitieron al menos un expediente, de no existente a 50 % de los adheridos. Verificaciones respondidas en no más de 5 segundos, 99 % |
| Momento de medición | Mes 21 para el primer indicador. Mensual desde el mes 16 para el segundo |
| Riesgo de adopción | Que el transportista no perciba utilidad, probabilidad media e impacto medio. Que los destinatarios no acepten el documento como prueba, probabilidad media e impacto alto. Que un conductor no consienta incluir su jornada |
| Mitigación | Primera emisión asistida en el terminal durante el enrolamiento. Entrevistas a destinatarios reales en el mes 4, antes de construir. Expediente con la jornada de los conductores que consintieron |
| Contingencia | Emisión automática mensual a los transportistas que lo pidan, sin acción de su parte |

## Innovación 2. Proceso. Programación dinámica de intervenciones por oportunidad de patio

| Campo | Contenido |
|---|---|
| Problema u oportunidad | 148 unidades propias y 34 de terceros sin equipo requieren montaje durante el paso normal por terminal. La disponibilidad simultánea de unidad, autorización, kit, técnico y ventana debe coordinarse. La línea base se levanta en M6; no se atribuye un ahorro ya medido. |
| Tecnología o práctica | Planificador determinista en Flota y activos: combina ETA y calidad de posición, autorización, compatibilidad del kit, stock, turnos, versión y ventana confirmada. Device Twins conserva configuración y Device Update distribuye paquetes a equipos homologados; las actas conservan intentos y resultados. |
| Nivel de madurez | TRL 2 propuesto, en escala NASA de nueve niveles: concepto definido, sin prueba de concepto ejecutada. Se valida factibilidad antes del piloto de M6 y se documenta el nivel alcanzado. |
| Fuentes | (NASA, s. f.; Microsoft, s. f.; Microsoft, s. f.) |
| Dónde se inserta en la arquitectura | Flota y activos registra las intervenciones; Telemetría aporta actualidad y configuración; la plataforma DevSecOps construye y firma el artefacto. Manifiesto por unidad, familia, kit, versión y acta. |
| Paquetes de la EDT | 12.2, con integración a 4.1 y 4.2; calendario del Subdocumento 7. |
| Mes del cronograma | Piloto de 10 camiones en M6; propios M6–M9, flota propia completa en M9; terceros adheridos desde M7; pausa M11–M15 y continuación M16–M18. |
| Inversión requerida | Planificador, tablero, integración, homologación del agente y kits diferenciales. No se cobra nuevamente el stock contractual de T-11. |
| Efecto en el costo operacional | Ejecución, almacenamiento de actas y mantenimiento del planificador, separados de la conectividad ya presupuestada. |
| Beneficio esperado | Reducción de preparación desperdiciada y visitas evitables. Se estima con cantidades y costos unitarios documentados, menos el costo incremental. Sin ahorro garantizado ni base inventada. |
| Indicador, línea base y meta | Reducir preparación inútil al menos 20 % respecto de la línea base homologada. Validación al primer intento al menos 95 % en cohorte de 20 intervenciones elegibles. Sustitución modular en hasta 30 min, dentro de la ventana normal. Metas propuestas. |
| Momento de medición | Línea base y contraste con planificación manual en M6; comparación por familia y terminal en M7–M9. Registro de causas, reintentos y denominadores. |
| Riesgo de adopción | ETA incorrecta, kit o agente incompatible, escaso beneficio frente a coordinación manual y falta de adhesión o paso de terceros. Probabilidad media; impacto alto salvo beneficio insuficiente, de impacto medio. |
| Mitigación | Calidad y actualidad de ETA, confirmación del jefe de terminal, matriz de familias, ensayo previo, paquete firmado, reversión validada y comparación trazable. |
| Contingencia | Abortar de forma segura y reprogramar cuando la ventana se acorte; método manual homologado y versión previa sin borrar eventos. Integración lógica de terceros sin intervención física no autorizada. |

## Innovación 3. Tecnológica o de arquitectura. Semirremolque conectado

| Campo | Contenido |
|---|---|
| Problema u oportunidad | 210 semirremolques propios, 245 a tres años y 44 refrigerados (Caso, numerales 2.2 y 14.1, pp. 6 y 29). La verificación bloqueante comprueba la revisión técnica del semirremolque (numeral 4.4, p. 10), pero el sistema no sabe cuál va enganchado. El plan preventivo usa el odómetro del camión (capítulo 8, p. 19) y el criterio 26 pide kilometraje real (capítulo 18, p. 43) |
| Tecnología o práctica | Baliza Bluetooth de baja energía Teltonika EYE Sensor BTSMP1 con identificador, temperatura, humedad, acelerómetro y sensor de puerta, IP67, de −20 a +60 °C. Lectura por el iWave G26I a bordo y por un lector Minew G1 en cada portería. Acople inferido por señal estable y movimiento conjunto |
| Nivel de madurez | Escala de niveles de madurez tecnológica de 1 a 9. Balizas y lectura en nivel 9. Inferencia del acople dentro de la verificación bloqueante de nivel 6 a nivel 7 en la marcha blanca |
| Fuentes | International Organization for Standardization (2013). Teltonika Telematics (2026a, 2026b). Minew (2023). iWave Global (2026) |
| Dónde se inserta en la arquitectura | Capa de borde con el G26I y el lector de portería. IoT Hub y Event Hubs en la capa de integración. Contextos Flota y activos (verificación bloqueante y kilometraje) y Telemetría y geocercas (temperatura y puerta). Consume el flujo de IoT Hub y expone el identificador del semirremolque acoplado. Sección 13.3 |
| Paquetes de la EDT | Paquete 12.3, con los paquetes 4.2 (instalación de balizas y lectores de portería) y 5.2 (Flota y activos) |
| Mes del cronograma | Instalación al paso por terminal en los meses 6 a 10 y 16 a 18, fuera de la temporada de diciembre a abril. Activación y primera medición en la marcha blanca, antes del mes 16 |
| Inversión requerida | Balizas y lectores de portería que compra el mandante (Caso, capítulo 11, p. 24) según el Formulario T-11, más la integración en tres servicios de negocio |
| Efecto en el costo operacional | Reposición de balizas al término de su batería y tráfico celular menor dentro de los mensajes del G26I |
| Beneficio esperado | Ningún semirremolque sale con la revisión técnica vencida. Mantención de semirremolques por kilometraje medido. Respaldo ante el cliente de la condición de la carga refrigerada |
| Indicador, línea base y meta | Asignaciones con semirremolque propio verificado por medición, de no verificado al asignar a 95 % o más. Semirremolques propios con kilometraje medido, 100 % de los que tienen baliza. Viajes refrigerados con temperatura continua, 100 %. Las dos últimas líneas base se miden en la Etapa 1 |
| Momento de medición | Marcha blanca antes del mes 16. Tercer mes de operación. Primera temporada de diciembre a abril |
| Riesgo de adopción | Acople falso con la baliza de un semirremolque vecino, probabilidad media e impacto alto. Temperatura bajo −20 °C en el paso cordillerano. Suplantación del identificador. Batería de menor duración |
| Mitigación | Señal estable y movimiento conjunto en los primeros minutos de marcha. Montaje a la sombra y prueba en el invierno de 2027 (meses 6 y 7). Lectura de portería como segundo control. Vigilancia del nivel de batería |
| Contingencia | La verificación vuelve a la declaración con la lectura de portería como control. Modelo de mayor rango térmico en los semirremolques que cruzan. Reposición desde la reserva del 10 %. Modelado de amenazas STRIDE en el Subdocumento 4, sección 4.1.21 (RT-26.07) |

## Innovación 4. Modelo de negocio o de contratación. Esquema de adhesión y propiedad del dispositivo

| Campo | Contenido |
|---|---|
| Problema u oportunidad | 148 dueños de 226 camiones (Caso, numeral 14.1, p. 29) preguntan de quién es el equipo, quién lo paga y si delatará cuándo trabajan para otro cliente. La decisión 5 del numeral 16.1 está abierta (p. 34) y la restricción 2 obliga a conseguirlo por contrato, incentivo o diseño (capítulo 10, p. 23) |
| Tecnología o práctica | Ventana de transmisión aplicada en el firmware del equipo a bordo, auditable por el dueño desde su consola de permisos. Comodato con retiro sin costo. Reparto con el transportista de la espera recuperada que su evidencia permite cobrar |
| Nivel de madurez | Escala de niveles de madurez tecnológica de 1 a 9. Control de transmisión por ventana en nivel 8. Registro de consentimiento en nivel 8. El componente contractual no se califica en esta escala |
| Fuentes | International Organization for Standardization (2013). Ministerio de Hacienda (2024), Ley N.º 21.719 |
| Dónde se inserta en la arquitectura | Equipo a bordo y búfer local con la ventana. Consentimiento en Personas y cumplimiento, adhesión en Flota y activos y reparto de la espera en Liquidación y costeo, regla RN-08 del Formulario T-12. Consola de permisos en el portal. Subdocumento 13, sección 13.4 |
| Paquetes de la EDT | EDT 12.4, sobre los paquetes 9.1 (Anexo de adhesión), 9.2 (Campaña y enrolamiento), 4.1 (Firmware) y 5.7 (Portal del transportista) |
| Mes del cronograma | Reparto aprobado por el Comité Ejecutivo en el mes 2. Validación jurídica del anexo en los meses 2 y 3. Cohorte inicial entre los meses 6 y 9. Ventana y consola entre los meses 6 y 10. Medición desde la marcha blanca |
| Inversión requerida | Diseño y validación jurídica del anexo, campaña en los cinco terminales y consola de consentimiento. El equipamiento lo compra el mandante (Caso, capítulo 11, p. 24) |
| Efecto en el costo operacional | Aumentan conectividad, soporte y reposición de los equipos en comodato. Disminuye el costo de gestionar objeciones de cobro |
| Beneficio esperado | Recupero de la espera hoy objetada en un 71 % (Caso, numeral 4.7, p. 11), que financia el incentivo. Se valoriza en la Oferta Económica y no se compromete como ingreso |
| Indicador, línea base y meta | Posiciones transmitidas fuera de la ventana de un viaje, cero. Transportistas adheridos con cobro respaldado que reciben su parte, 100 %. Consentimientos revocados, menos de 10 % |
| Momento de medición | Auditoría mensual desde el mes 13. Cada liquidación desde el mes 16. Mensual desde el mes 13 |
| Riesgo de adopción | Adhesión bajo el 70 % en la Etapa 1, probabilidad media e impacto alto. Desconfianza en la ventana. Rechazo de la evidencia de espera por los clientes. Anexo que no resista revisión jurídica, probabilidad baja e impacto alto |
| Mitigación | Conversación desde el mes 2 con el beneficio a la vista antes de pedir el equipo. Ventana auditable por el dueño. Validación jurídica antes de construir |
| Contingencia | Tres medidas del Subdocumento 3 si la adhesión no llega al 40 % en el mes 9. Financiar el incentivo con el ahorro de la liquidación automática |

## Innovación 5. Experiencia de usuario, sostenibilidad o impacto social. Bienestar del conductor y descanso en parador seguro

| Campo | Contenido |
|---|---|
| Problema u oportunidad | Una alerta de jornada entregada donde no hay dónde detenerse es inútil (Caso, capítulo 18, p. 43). Hay tramos sin lugar seguro para combinaciones de 45 toneladas (numeral 16.1, p. 35). 258 conductores externos no son trabajadores de la compañía (numeral 2.3, p. 6) |
| Tecnología o práctica | Motor predictivo sobre audIT EdgeHub, en el equipo a bordo, que cruza jornada acumulada, topografía y ventana circadiana de 02:00 a 06:00 h. Catálogo local de paradores calificados. Enclavamiento cinético de pantalla y síntesis de voz local en español |
| Nivel de madurez | Escala ISO 16290 de 1 a 9. Autoevaluación TRL 2 conceptual del modelo circadiano y catálogo integrado; sin evidencia aportada de prueba de concepto o validación del prototipo. Componentes comerciales no acreditan madurez del conjunto. Objetivos: TRL 6 tras ensayos en entorno representativo M10--M12 y TRL 7 tras piloto operacional M13--M15, sujetos a versión, protocolo, datos y resultados reproducibles. Se acreditan con el expediente de validación |
| Fuentes | International Organization for Standardization (2013, 2017, 2019). National Academies of Sciences, Engineering, and Medicine (2016). Congreso Nacional de Chile (2021), Ley N.º 21.377. Ministerio del Trabajo (2003, 2006) |
| Dónde se inserta en la arquitectura | Capa de borde con el motor predictivo, el catálogo y la síntesis de voz. Servicio de gobernanza de paradores en la torre de control. Consulta pasiva en el portal |
| Paquetes de la EDT | Paquete 12.5, con los paquetes 4.1 (firmware a bordo) y 5.1 (Personas y cumplimiento) |
| Mes del cronograma | Talleres ergonómicos M4; catálogo M3--M6; software a bordo M4--M9. Ensayos del prototipo integrado M10--M12. Piloto y validación con conductores en marcha blanca M13--M15; producción E1 en M16 |
| Inversión requerida | Software de borde incremental y talleres ergonómicos participativos. El catálogo se levanta dentro de la campaña de cobertura |
| Efecto en el costo operacional | Menor búsqueda errática de estacionamiento en ruta, con un efecto en combustible que se mide en la Etapa 1 |
| Beneficio esperado | Menor riesgo de siniestros graves por microsueño y supresión de multas por la Ley N.º 21.377 y el artículo 25 bis. Reflejado en mitigación de contingencias patrimoniales y ahorros de seguros |
| Indicador, línea base y meta | Alertas con parador calificado, de 0 a 98 % o más. Bloqueo cinético del 100 %. NASA-TLX con guantes bajo 35 puntos y adherencia voluntaria de 85 % o más, con línea base medida en la Etapa 1 |
| Momento de medición | Mensual durante la marcha blanca M13--M15, antes de producción E1 en M16; nivel alcanzado respaldado por informe de resultados |
| Riesgo de adopción | Que los 258 conductores externos lo perciban como vigilancia patronal encubierta, probabilidad media a alta e impacto alto |
| Mitigación | Diseño ergonómico participativo en horario de relevo en los cinco terminales y orientación al bienestar |
| Contingencia | Notificación solo acústica por el altavoz del vehículo, sin teléfonos personales ni botones adicionales en cabina |
