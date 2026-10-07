# Formulario T-19. Cartera de innovaciones

audIT, Empresa N.º 10. Licitación TFEP-01/2026, Caso 10 Transporte de Carga. Oferta Técnica, Sobre N.º 2. Informe Preparatorio 2. Archivo AUDIT-Formulario-T-19.pdf. Anexo del Subdocumento N.º 13, Innovaciones. Las fuentes están en las Referencias de ese subdocumento.


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

## Innovación 2. Proceso. Despliegue sin detener la flota **[Información requerida por dupla 3: reformular o reemplazar según la observación 89]**

| Campo | Contenido |
|---|---|
| Problema u oportunidad | Un camión detenido no produce (Caso, capítulo 10, restricción 10, p. 24). La intervención a bordo solo ocurre en terminal, cada seis días en promedio, y el 22 % de la flota subcontratada pasa menos de una vez al mes (Caso, numeral 2.3, p. 7) |
| Tecnología o práctica | Aprovisionamiento remoto con Azure IoT Hub Device Update y Device Twins, configuración precargada en fábrica, kits de reemplazo con arneses de acople rápido por familia de tractocamión y anticipación de llegada a terminal desde la posición de la flota |
| Nivel de madurez | **[Información requerida por dupla 3: nivel de madurez y escala]** |
| Fuentes | **[Información requerida por dupla 3: fuentes en APA]** |
| Dónde se inserta en la arquitectura | Capa de borde y servicio de actualización remota. Rutina de autodiagnóstico y enrolamiento validada en la barrera de salida del terminal. **[Información requerida por dupla 3: alinear con los lectores CAN del Formulario T-11]** |
| Paquetes de la EDT | Paquete 12.2, con los paquetes 4.1 (firmware y actualización en terminal) y 4.2 (montaje de los 182 equipos) |
| Mes del cronograma | Piloto de 10 camiones en el mes 6. Flota propia completa al cierre del mes 9 |
| Inversión requerida | **[Información requerida por dupla 3: partidas de inversión]** |
| Efecto en el costo operacional | **[Información requerida por dupla 3: efecto en el costo operacional]** |
| Beneficio esperado | Cero horas de inmovilización de flota comercialmente activa atribuible a la instalación |
| Indicador, línea base y meta | Ritmo de 35 a 45 tractocamiones por mes. 100 % de los 148 propios al cierre del mes 8. Sustitución en terreno en menos de 30 minutos por camión |
| Momento de medición | Mensual hasta el mes 8 |
| Riesgo de adopción | **[Información requerida por dupla 3: riesgo de adopción, probabilidad e impacto]** |
| Mitigación | **[Información requerida por dupla 3: estrategia de mitigación]** |
| Contingencia | **[Información requerida por dupla 3: plan de contingencia]** |

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
| Contingencia | La verificación vuelve a la declaración con la lectura de portería como control. Modelo de mayor rango térmico en los semirremolques que cruzan. Reposición desde la reserva del 10 %. **[Información requerida por dupla 3: modelado de amenazas de la baliza (RT-26.07)]** |

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
| Nivel de madurez | Escala de niveles de madurez tecnológica de 1 a 9. Hardware de borde, almacenamiento local, síntesis de voz y enclavamiento en nivel 8. Modelo circadiano y ontología de paradores en nivel 6 (escalamiento a nivel 7 en marcha blanca mes 16) |
| Fuentes | International Organization for Standardization (2013, 2017, 2019). National Academies of Sciences, Engineering, and Medicine (2016). Congreso Nacional de Chile (2021), Ley N.º 21.377. Ministerio del Trabajo (2003, 2006) |
| Dónde se inserta en la arquitectura | Capa de borde con el motor predictivo, el catálogo y la síntesis de voz. Servicio de gobernanza de paradores en la torre de control. Consulta pasiva en el portal |
| Paquetes de la EDT | Paquete 12.5, con los paquetes 4.1 (firmware a bordo) y 5.1 (Personas y cumplimiento) |
| Mes del cronograma | Talleres ergonómicos en el mes 4. Catálogo entre los meses 3 y 6. Software a bordo entre los meses 4 y 9. Validación con conductores entre los meses 13 y 15 |
| Inversión requerida | Software de borde incremental y talleres ergonómicos participativos. El catálogo se levanta dentro de la campaña de cobertura |
| Efecto en el costo operacional | Menor búsqueda errática de estacionamiento en ruta, con un efecto en combustible que se mide en la Etapa 1 |
| Beneficio esperado | Menor riesgo de siniestros graves por microsueño y supresión de multas por la Ley N.º 21.377 y el artículo 25 bis. Reflejado en mitigación de contingencias patrimoniales y ahorros de seguros |
| Indicador, línea base y meta | Alertas con parador calificado, de 0 a 98 % o más. Bloqueo cinético del 100 %. NASA-TLX con guantes bajo 35 puntos y adherencia voluntaria de 85 % o más, con línea base medida en la Etapa 1 |
| Momento de medición | Mensual en la marcha blanca, antes del mes 16 |
| Riesgo de adopción | Que los 258 conductores externos lo perciban como vigilancia patronal encubierta, probabilidad media a alta e impacto alto |
| Mitigación | Diseño ergonómico participativo en horario de relevo en los cinco terminales y orientación al bienestar |
| Contingencia | Notificación solo acústica por el altavoz del vehículo, sin teléfonos personales ni botones adicionales en cabina |
