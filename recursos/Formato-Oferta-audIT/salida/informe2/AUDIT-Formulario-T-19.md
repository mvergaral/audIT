# Formulario T-19. Cartera de innovaciones

audIT, Empresa N.º 10. Licitación TFEP-01/2026, Caso 10 Transporte de Carga. Oferta Técnica, Sobre N.º 2. Informe Preparatorio 2. Archivo AUDIT-Formulario-T-19.pdf. Anexo del Subdocumento N.º 13, Innovaciones. Las fuentes están en las Referencias de ese subdocumento.


## Innovación 1. Producto o servicio. Portal del transportista con liquidación en curso

| Campo | Contenido |
|---|---|
| Problema u oportunidad | La liquidación al transportista subcontratado toma nueve días, la hacen ocho personas y el 11 % se corrige después de emitida (Caso, numeral 4.11, p. 12). Además, el transportista no puede probar ante terceros la evidencia que el sistema ya produce sobre él |
| Tecnología o práctica | Portal segregado por identidad alimentado por el motor de costeo de la liquidación oficial. Expediente exportable con jornada acreditada, habilitaciones y hoja de vida de los equipos, firmado y verificable por un tercero sin acceso al sistema |
| Nivel de madurez | Escala de niveles de madurez tecnológica de 1 a 9. Firma electrónica avanzada con verificación en línea en nivel 9, línea base comprometida. Credencial verificable entre los niveles 7 y 8 |
| Fuentes | International Organization for Standardization (2013). Congreso Nacional de Chile (2002), Ley N.º 19.799. World Wide Web Consortium (2025) |
| Dónde se inserta en la arquitectura | Servicio de emisión de expediente en la capa de servicios de negocio, que consume control de jornada, gestión documental y gestión de flota. Servicio público de verificación. Firma desde la bóveda de claves de la capa de seguridad. Solicitud y descarga en el portal |
| Paquetes de la EDT | EDT 4.3 (Servicios de Liquidación) y EDT 7.3 (Portal y Expedientes) |
| Mes del cronograma | Decisión de firma en el mes 4. Construcción entre los meses 10 y 12. Disponible en la marcha blanca de la Etapa 1 |
| Inversión requerida | Desarrollo incremental sobre el portal ya presupuestado y suscripción de certificados de firma del emisor |
| Efecto en el costo operacional | Reducción en horas de rectificación manual y soporte a transportistas; costo menor en certificados de firma digital |
| Beneficio esperado | Menos liquidaciones corregidas (de 11 % a menos de 2 %) y menor tiempo de cierre mensual. Reflejado en ahorros OPEX del flujo de caja |
| Indicador, línea base y meta | Tiempo medio de resolución de discrepancias en liquidaciones, de 9 días a menos de 48 horas. Expedientes de liquidación aceptados sin objeción documental formal, de 0 % a 98 % o más |
| Momento de medición | Cierre de la marcha blanca, mes 15. Tercer cierre mensual tras el paso a producción |
| Riesgo de adopción | Que el transportista no perciba utilidad y no emita el expediente, probabilidad media e impacto alto. Que los destinatarios no acepten el documento como prueba |
| Mitigación | Asistir la primera emisión en el terminal durante el enrolamiento. Levantar destinatarios reales en el mes 4, antes de construir |
| Contingencia | Generación asistida y despacho automático del expediente mensual por correo electrónico certificado ante baja adopción inicial |

## Innovación 2. Proceso. Despliegue continuo y modular sin detención de flota

| Campo | Contenido |
|---|---|
| Problema u oportunidad | Un camión detenido no produce (Caso, capítulo 10, restricción 10, p. 24). La intervención a bordo solo ocurre en terminal, cada seis días en promedio, y el 22 % de la flota subcontratada pasa menos de una vez al mes (Caso, numeral 2.3, p. 7) |
| Tecnología o práctica | Aprovisionamiento remoto con Azure IoT Hub Device Update y Device Twins, configuración precargada en fábrica, kits de reemplazo con arneses de acople rápido por familia de tractocamión y anticipación de llegada a terminal desde la posición de la flota |
| Nivel de madurez | Escala ISO 16290:2013 de 1 a 9. Metodología de sustitución modular y aprovisionamiento telemático en nivel 8 |
| Fuentes | International Organization for Standardization (2013). Microsoft Azure IoT (2024) |
| Dónde se inserta en la arquitectura | Capa de borde y servicio de aprovisionamiento Device Twins. Rutina de autodiagnóstico y enrolamiento con lectores CAN sin contacto del Formulario T-11 validada en barrera de salida |
| Paquetes de la EDT | EDT 4.2 (Instalación de Dispositivos a Bordo y Búfer) y EDT 4.5 (Integración Telemática y Lectores CAN) |
| Mes del cronograma | Piloto de 10 camiones en el mes 4. Flota propia completa al cierre del mes 8 |
| Inversión requerida | Kits de arneses de acople rápido y stock de búferes de intercambio rápido en terminales |
| Efecto en el costo operacional | Supresión absoluta de horas improductivas y lucro cesante por mantención en patio |
| Beneficio esperado | Cero horas de inmovilización de flota comercialmente activa atribuible a la instalación |
| Indicador, línea base y meta | Ritmo de 35 a 45 tractocamiones por mes. 100 % de los 148 propios al cierre del mes 8. Sustitución en terreno en menos de 30 minutos por camión |
| Momento de medición | Mensual hasta el mes 8 |
| Riesgo de adopción | Dispersión de unidades en ruta que retrase el paso por terminal, probabilidad media e impacto medio |
| Mitigación | Monitoreo telemático de proximidad y asignación de kits en andén previo a la llegada en los cinco terminales |
| Contingencia | Instalación coordinada durante paradas de mantención preventiva programada exclusivamente en terminales de Curimón |

## Innovación 3. Tecnológica o de arquitectura. Semirremolque conectado

| Campo | Contenido |
|---|---|
| Problema u oportunidad | 210 semirremolques propios, 245 a tres años y 44 refrigerados (Caso, numerales 2.2 y 14.1, pp. 6 y 29). La verificación bloqueante comprueba la revisión técnica del semirremolque (numeral 4.4, p. 10), pero el sistema no sabe cuál va enganchado. El plan preventivo usa el odómetro del camión (capítulo 8, p. 19) y el criterio 26 pide kilometraje real (capítulo 18, p. 43) |
| Tecnología o práctica | Baliza Bluetooth de baja energía Teltonika EYE Sensor BTSMP1 con identificador, temperatura, humedad, acelerómetro y sensor de puerta, IP67, de −20 a +60 °C. Lectura por el iWave G26I a bordo y por un lector Minew G1 en cada portería. Acople inferido por señal estable y movimiento conjunto |
| Nivel de madurez | Escala de niveles de madurez tecnológica de 1 a 9. Balizas y lectura en nivel 9. Inferencia del acople dentro de la verificación bloqueante de nivel 6 a nivel 7 en la marcha blanca |
| Fuentes | International Organization for Standardization (2013). Teltonika Telematics (2026a, 2026b). Minew (2023). iWave Global (2026) |
| Dónde se inserta en la arquitectura | Capa de borde con el G26I y el lector de portería. IoT Hub y Event Hubs en la capa de integración. Contextos Flota y activos (verificación bloqueante y kilometraje) y Telemetría y geocercas (temperatura y puerta). Consume el flujo de IoT Hub y expone el identificador del semirremolque acoplado. Sección 13.3 |
| Paquetes de la EDT | EDT 3.4 (Instalación de Balizas BLE y Lectores de Portería) y EDT 4.4 (Integración con Verificación Bloqueante) |
| Mes del cronograma | Instalación en la Etapa 1 al paso por terminal (meses 4 a 9), con los 44 refrigerados fuera de diciembre a abril. Activación y primera medición en marcha blanca (meses 13 a 15) |
| Inversión requerida | Balizas y lectores de portería que compra el mandante (Caso, capítulo 11, p. 24) según el Formulario T-11, más la integración en tres servicios de negocio |
| Efecto en el costo operacional | Reposición de balizas al término de su batería y tráfico celular menor dentro de los mensajes del G26I |
| Beneficio esperado | Ningún semirremolque sale con la revisión técnica vencida. Mantención de semirremolques por kilometraje medido. Respaldo ante el cliente de la condición de la carga refrigerada |
| Indicador, línea base y meta | Asignaciones con semirremolque propio verificado por medición, de no registrado a 95 % o más. Semirremolques propios con kilometraje medido, 100 % de los que tienen baliza. Viajes refrigerados con temperatura continua, 100 % |
| Momento de medición | Marcha blanca antes del mes 16. Tercer mes de operación. Primera temporada de diciembre a abril |
| Riesgo de adopción | Acople falso con la baliza de un semirremolque vecino, probabilidad media e impacto alto. Temperatura bajo −20 °C en el paso cordillerano. Suplantación del identificador. Batería de menor duración |
| Mitigación | Señal estable y movimiento conjunto en los primeros minutos de marcha. Montaje a la sombra y prueba invernal. Lectura de portería como segundo control. Vigilancia del nivel de batería |
| Contingencia | La verificación vuelve a la declaración con la lectura de portería como control. Modelo de mayor rango térmico en los semirremolques que cruzan. Reposición desde reserva del 10 %. Modelado STRIDE con mitigación criptográfica contra spoofing (RT-26.07) |

## Innovación 4. Modelo de negocio o de contratación. Esquema de adhesión y propiedad del dispositivo

| Campo | Contenido |
|---|---|
| Problema u oportunidad | Los dueños de camión preguntan de quién es el equipo, quién lo paga y si delatará cuándo trabajan para otro cliente. La decisión quinta del numeral 16.1 sigue abierta (Caso, p. 34) y la restricción 2 obliga a conseguirlo por contrato, incentivo o diseño (capítulo 10, p. 23) |
| Tecnología o práctica | Comodato sobre el equipamiento con retiro sin costo. Ventana de transmisión gobernada en el firmware. Consentimiento granular y revocable desde el portal con bitácora de accesos. Incentivo financiado con el recupero de los cobros de espera hoy objetados |
| Nivel de madurez | Escala de niveles de madurez tecnológica de 1 a 9. Control de transmisión por ventana en nivel 8. Registro de consentimiento en nivel 8. El componente contractual no se califica en esta escala |
| Fuentes | International Organization for Standardization (2013). Ministerio de Hacienda (2024), Ley N.º 21.719 |
| Dónde se inserta en la arquitectura | Unidad telemática y búfer local, concentrador de dispositivos, servicios nuevos de consentimiento y de adhesión, y consola de permisos en el portal |
| Paquetes de la EDT | EDT 1.3 (Convenio de Comodato), EDT 5.2 (Campaña de Enrolamiento) y EDT 7.4 (Consola de Consentimiento) |
| Mes del cronograma | Adhesión desde el mes 1. Validación jurídica entre los meses 1 y 3. Cohorte piloto entre los meses 6 y 9. Consola entre los meses 9 y 12. Resultado en la marcha blanca |
| Inversión requerida | Diseño y validación jurídica del anexo, campaña de enrolamiento en cinco terminales y consola de consentimiento. El equipamiento lo compra el mandante (Caso, capítulo 11, p. 24) |
| Efecto en el costo operacional | Aumentan conectividad, soporte y reposición del parque en comodato. Disminuyen el costo de la liquidación y de gestionar objeciones de cobro |
| Beneficio esperado | Reducir la objeción de los cobros de espera desde el 71 % (Caso, numeral 4.7, p. 11) bajo el 20 %. Reflejado en ingresos por recupero operacional en el flujo de caja de la Oferta Económica |
| Indicador, línea base y meta | Transportistas adheridos sobre 148, de 0 % a 70 % en la Etapa 1 y 90 % en la Etapa 2. Revocación bajo el 10 %. Objeción de cobros de espera bajo el 20 % |
| Momento de medición | Anexos firmados desde el mes 3. Cierre de la Etapa 1 y de la Etapa 2 |
| Riesgo de adopción | Adhesión bajo el 70 % en la Etapa 1, probabilidad media e impacto alto. Desconfianza en la ventana. Rechazo de la evidencia por los clientes. Anexo que no resista revisión jurídica, probabilidad baja e impacto alto |
| Mitigación | Comenzar en el mes 1 y mostrar beneficio antes de pedir el equipo. Ventana auditable por el dueño. Validación jurídica entre los meses 1 y 3 |
| Contingencia | Escalonar el incentivo y extender la modalidad de datos, que no requiere instalar nada. Financiar el incentivo con la reducción del costo de liquidación |

## Innovación 5. Experiencia de usuario, sostenibilidad o impacto social. Bienestar del conductor y descanso en parador seguro

| Campo | Contenido |
|---|---|
| Problema u oportunidad | Una alerta de jornada entregada donde no hay dónde detenerse es inútil (Caso, capítulo 18, p. 43). Hay tramos sin lugar seguro para combinaciones de 45 toneladas (numeral 16.1, p. 35). 258 conductores externos no son trabajadores de la compañía (numeral 2.3, p. 6) |
| Tecnología o práctica | Motor predictivo a bordo que cruza jornada acumulada, topografía y ventana circadiana de 02:00 a 06:00 h. Catálogo local de paradores calificados. Enclavamiento cinético de pantalla y síntesis de voz local en español |
| Nivel de madurez | Escala de niveles de madurez tecnológica de 1 a 9. Hardware de borde, almacenamiento local, síntesis de voz y enclavamiento en nivel 8. Modelo circadiano y ontología de paradores en nivel 6 (escalamiento a nivel 7 en marcha blanca mes 16) |
| Fuentes | International Organization for Standardization (2013, 2017, 2019). National Academies of Sciences, Engineering, and Medicine (2016). Congreso Nacional de Chile (2021), Ley N.º 21.377. Ministerio del Trabajo (2003, 2006) |
| Dónde se inserta en la arquitectura | Capa de borde con el motor predictivo, el catálogo y la síntesis de voz. Servicio de gobernanza de paradores en la torre de control. Consulta pasiva en el portal |
| Paquetes de la EDT | EDT 2.4 (Diseño Ergonómico), EDT 3.7 (Catálogo de Paradores), EDT 4.6 (Software Bordo Circadiano) y EDT 7.2 (Validación Marcha Blanca) |
| Mes del cronograma | Talleres ergonómicos en el mes 4. Catálogo entre los meses 3 y 6. Software entre los meses 7 y 10. Validación con conductores entre los meses 13 y 15 |
| Inversión requerida | Software de borde incremental y talleres ergonómicos participativos. El catálogo se levanta dentro de la campaña de cobertura |
| Efecto en el costo operacional | Menor búsqueda errática de estacionamiento en ruta, con un efecto en combustible que se mide en la Etapa 1 |
| Beneficio esperado | Menor riesgo de siniestros graves por microsueño y supresión de multas por la Ley N.º 21.377 y el artículo 25 bis. Reflejado en mitigación de contingencias patrimoniales y ahorros de seguros |
| Indicador, línea base y meta | Alertas con parador calificado, de 0 a 98 % o más. Bloqueo cinético del 100 %. NASA-TLX con guantes bajo 35 puntos y adherencia voluntaria de 85 % o más, con línea base medida en la Etapa 1 |
| Momento de medición | Mensual en la marcha blanca, antes del mes 16 |
| Riesgo de adopción | Que los 258 conductores externos lo perciban como vigilancia patronal encubierta, probabilidad media a alta e impacto alto |
| Mitigación | Diseño ergonómico participativo en horario de relevo en los cinco terminales y orientación al bienestar |
| Contingencia | Notificación solo acústica por el altavoz del vehículo, sin teléfonos personales ni botones adicionales en cabina |
