# Formulario T-16. 

audIT, Empresa N.º 10. Licitación TFEP-01/2026, Caso 10 Transporte de Carga. Oferta Técnica, Sobre N.º 2. Informe Preparatorio 2. Archivo AUDIT-Formulario-T-16.pdf. Anexo del Subdocumento N.º 8, Plan de riesgos. Las fuentes están en las Referencias de ese subdocumento.

\begin{formulario}{T-16}

\providecommand\tituloBloqueFormulario[1]{
  \phantomsection\addcontentsline{toc}{section}{#1}{\sffamily\bfseries\fontsize{13bp}{16bp}\selectfont\color{audit-marino}#1}}

\begin{contenidoExigido}{T-16}
  \exigencia{Identificación y cuantificación de riesgos técnicos, organizacionales, de proyecto, de seguridad y de operación.}{sección 8.2 y este formulario, registro de riesgos}
  \exigencia{Análisis cualitativo y cuantitativo con modos de falla, árbol de fallas o simulación.}{sección 8.2 y este formulario, análisis de modos de falla}
  \exigencia{Estrategias de mitigación con costo-beneficio, responsable, plazo y disparador.}{sección 8.3 y este formulario, respuesta, disparador y plazo}
  \exigencia{Obsolescencia, bloqueo por proveedor, escalabilidad, ciberseguridad y disponibilidad de contrapartes del mandante.}{sección 8.2}
  \exigencia{Reservas de contingencia y de gestión, con su reflejo en el cronograma y en el flujo de caja.}{sección 8.3}
\end{contenidoExigido}

\tituloBloqueFormulario{Registro de riesgos}

El registro tiene 28 riesgos de la solución propuesta. La probabilidad y el impacto van de 1 a 5 con las
escalas de la sección 8.1, y la exposición es su producto. Una exposición de 12 o más es alta
y exige plan de contingencia, que está en la sección 8.3.

\begin{formularioTDieciseis}
  \riesgoTDieciseis{id=R-01, riesgo={La reconexión de cientos de camiones tras una sombra satura la ingesta o la base de series, y la transferencia, la persistencia y la conciliación completas pasan de 20 minutos}, categoria={Técnicos}, probabilidad=2, impacto=3, exposicion=6, mitigacion={Espera aleatoria y reintento exponencial en el equipo, Event Hubs desacopla la llegada, IoT Hub S1 con dos unidades y alerta por profundidad de cola}, responsable={Líder de Operación}}
  \riesgoTDieciseis{id=R-02, riesgo={El equipo a bordo de un camión falla entre dos pasos por terminal}, categoria={Técnicos}, probabilidad=3, impacto=3, exposicion=9, mitigacion={Búfer de 288 horas, 19 equipos de reposición en los terminales y alerta por camión que llega sin reportar}, responsable={Líder de Implantación}}
  \riesgoTDieciseis{id=R-03, riesgo={El iWave G26I o el Iridium Edge no obtienen la homologación de SUBTEL o la marca E-Mark}, categoria={Técnicos}, probabilidad=2, impacto=4, exposicion=8, mitigacion={Verificación de ambas certificaciones en la factibilidad, antes de la compra, como condición declarada en el Formulario T-11}, responsable={Líder de Implantación}}
  \riesgoTDieciseis{id=R-04, riesgo={La cobertura móvil medida en las rutas es peor que la supuesta para el dimensionamiento}, categoria={Técnicos}, probabilidad=3, impacto=3, exposicion=9, mitigacion={Medición en terreno de la cobertura (A03), búfer de 288 horas y mensajería Iridium para los eventos críticos}, responsable={Líder de Implantación}}
  \riesgoTDieciseis{id=R-05, riesgo={El crecimiento a 430 camiones y a tres veces la volumetría inicial supera la capacidad dimensionada}, categoria={Técnicos}, probabilidad=2, impacto=3, exposicion=6, mitigacion={Dimensionamiento sobre RT-09.03, escalado automático de AKS, unidades adicionales de IoT Hub y prueba de carga a 1,5 veces el peak}, responsable={Arquitecto de Solución}}
  \riesgoTDieciseis{id=R-06, riesgo={Azure Cache for Redis se retira el 30 de septiembre de 2028, en el mes 20, durante la marcha blanca de la Etapa 2, y su edición Enterprise el 31 de marzo de 2027}, categoria={Técnicos}, probabilidad=5, impacto=3, exposicion=15, mitigacion={La arquitectura usa Azure Managed Redis, el servicio de reemplazo, desde la Etapa 1 (Subdocumento 4, sección 4.1.1)}, responsable={Arquitecto de Solución}}
  \riesgoTDieciseis{id=R-07, riesgo={La solución queda atada al proveedor de nube y el mandante no puede cambiarlo}, categoria={Técnicos}, probabilidad=2, impacto=3, exposicion=6, mitigacion={Contenedores y motor relacional portables, Event Hubs con protocolo Kafka, infraestructura como código y suscripciones a nombre del mandante}, responsable={Arquitecto de Solución}}
  \riesgoTDieciseis{id=R-08, riesgo={Las plataformas de los terceros no entregan datos por interfaz, porque dos son de solo consulta y una no exporta}, categoria={Organizacionales y de contrapartes}, probabilidad=3, impacto=3, exposicion=9, mitigacion={Factibilidad con los tres proveedores (A04) y estándar de homologación. Si falla, esos camiones pasan a operar como sin equipo}, responsable={Líder de Integración}}
  \riesgoTDieciseis{id=R-09, riesgo={Los fabricantes no autorizan la lectura de la telemetría de fábrica de los 61 tractocamiones, que RT-17.06 sujeta a su autorización}, categoria={Organizacionales y de contrapartes}, probabilidad=3, impacto=3, exposicion=9, mitigacion={Consulta a cada fabricante en la factibilidad (A04) con el acoplamiento sin contacto y de solo lectura, que no toca el arnés ni la garantía. Sin autorización, el viaje se registra igual con el equipo a bordo}, responsable={Líder de Integración}}
  \riesgoTDieciseis{id=R-10, riesgo={El apagado de las redes 2G y 3G deja sin posición a equipos de terceros que hoy reportan}, categoria={Organizacionales y de contrapartes}, probabilidad=3, impacto=3, exposicion=9, mitigacion={LTE exigida en el estándar de homologación y seguimiento mensual de la adhesión por proveedor}, responsable={Líder Funcional}}
  \riesgoTDieciseis{id=R-11, riesgo={La adhesión de los transportistas queda bajo la meta de 104 al mes 16 y 134 al mes 21}, categoria={Organizacionales y de contrapartes}, probabilidad=3, impacto=4, exposicion=12, mitigacion={Campaña desde el mes 1 (A06), anexo de adhesión con propiedad del dispositivo y expediente verificable como incentivo}, responsable={Líder Funcional}}
  \riesgoTDieciseis{id=R-12, riesgo={El sistema contable y de facturación no recibe datos por interfaz}, categoria={Organizacionales y de contrapartes}, probabilidad=2, impacto=3, exposicion=6, mitigacion={Prueba técnica en el mes 3. Si falla, intercambio de archivos con conciliación}, responsable={Líder de Integración}}
  \riesgoTDieciseis{id=R-13, riesgo={La autoridad no admite el registro electrónico de jornada}, categoria={Organizacionales y de contrapartes}, probabilidad=2, impacto=3, exposicion=6, mitigacion={Consulta C-10 en el mes 2. Si la respuesta es negativa, se mantiene el respaldo en papel firmado}, responsable={Líder Funcional}}
  \riesgoTDieciseis{id=R-14, riesgo={Los conductores rechazan la medición o la perciben como vigilancia, en especial los 258 externos}, categoria={Organizacionales y de contrapartes}, probabilidad=3, impacto=3, exposicion=9, mitigacion={Plan de gestión del cambio, consentimiento revocable por dato y período, y capacitación en los terminales (A13)}, responsable={Líder de Implantación}}
  \riesgoTDieciseis{id=R-15, riesgo={Los usuarios clave de la torre y de los terminales no tienen tiempo para el levantamiento, las pruebas y la capacitación, sobre todo en la temporada, o un entregable vuelve con observaciones y la segunda revisión del Artículo 18.3 consume el margen del hito}, categoria={Organizacionales y de contrapartes}, probabilidad=3, impacto=3, exposicion=9, mitigacion={Calendario de participación de los usuarios clave acordado en el arranque, revisión previa de cada entregable con la Contraparte Técnica en el Comité de Proyecto y entregables con la evidencia y la trazabilidad del Artículo 18.2}, responsable={Jefe de Proyecto}}
  \riesgoTDieciseis{id=R-16, riesgo={La ruta crítica o la capacitación atrasan el inicio de la marcha blanca de la Etapa 1, fijado en el día 240}, categoria={Gestión del proyecto}, probabilidad=2, impacto=4, exposicion=8, mitigacion={Reserva A14 de 14 días y A13 diez días antes del fin de A09, condicionada a la entrega G13, con registro del atraso si faltan la versión de preproducción, los datos o el material}, responsable={Jefe de Proyecto}}
  \riesgoTDieciseis{id=R-17, riesgo={Los primeros hitos de pago se atrasan, porque su margen es de 2 a 8 días hábiles}, categoria={Gestión del proyecto}, probabilidad=2, impacto=3, exposicion=6, mitigacion={Levantamiento en los cinco terminales en paralelo y seguimiento semanal del margen de cada hito}, responsable={Jefe de Proyecto}}
  \riesgoTDieciseis{id=R-18, riesgo={La marcha blanca de la Etapa 1, que cae en la temporada de fruta, no cumple las condiciones del Artículo 17.3 en tres meses}, categoria={Gestión del proyecto}, probabilidad=3, impacto=4, exposicion=12, mitigacion={Analistas en los cinco terminales en el horario de relevo, medición diaria y reversión activa}, responsable={Líder de Operación}}
  \riesgoTDieciseis{id=R-19, riesgo={El montaje a bordo avanza más lento que la cobertura declarada mes a mes, por un cierre del paso Los Libertadores, por la temporada de diciembre a abril o porque un camión pasa poco por los terminales}, categoria={Gestión del proyecto}, probabilidad=3, impacto=2, exposicion=6, mitigacion={Montaje en los meses 6 a 10 y 16 a 18, con holguras de 20 días (A11) y 40 días (A18)}, responsable={Líder de Implantación}}
  \riesgoTDieciseis{id=R-20, riesgo={La parte de la flota sin equipo audIT queda así más tiempo del previsto y se forman dos maneras de trabajar que después no se unifican}, categoria={Gestión del proyecto}, probabilidad=3, impacto=3, exposicion=9, mitigacion={Una sola fuente de verdad y un solo flujo de asignación para toda la flota, con el nivel de evidencia de cada camión visible en la torre, y seguimiento mensual de los camiones sin equipar}, responsable={Líder de Implantación}}
  \riesgoTDieciseis{id=R-21, riesgo={El contrato empieza en enero de 2027 y el mes 16 cae en abril, dentro de la temporada}, categoria={Gestión del proyecto}, probabilidad=2, impacto=5, exposicion=10, mitigacion={Fijar en el contrato febrero de 2027 como mes 1 y escalar al Comité Ejecutivo cualquier cambio de fecha}, responsable={Jefe de Proyecto}}
  \riesgoTDieciseis{id=R-22, riesgo={Alguien suplanta un equipo a bordo o una baliza para falsear posición, jornada o acople}, categoria={Ciberseguridad y datos}, probabilidad=2, impacto=4, exposicion=8, mitigacion={Elemento seguro TA100 y certificado por equipo, certificado mutuo en IoT Hub y acople confirmado en la portería}, responsable={Encargado de Seguridad}}
  \riesgoTDieciseis{id=R-23, riesgo={Un ataque al portal expuesto a internet compromete datos de localización de los conductores externos}, categoria={Ciberseguridad y datos}, probabilidad=3, impacto=4, exposicion=12, mitigacion={Cortafuegos de aplicación en Front Door, Entra ID con control por rol y atributo, cifrado de campo y pruebas de seguridad ofensiva en A12}, responsable={Encargado de Seguridad}}
  \riesgoTDieciseis{id=R-24, riesgo={La réplica de datos personales en Brazil South no cuenta con base de licitud ni con la aprobación del mandante}, categoria={Ciberseguridad y datos}, probabilidad=3, impacto=4, exposicion=12, mitigacion={Base de licitud del Subdocumento 5 y aprobación del mandante que exige el Artículo 23. Sin ellas, los datos personales se replican en San Bernardo, que levanta los servicios críticos que los usan}, responsable={Arquitecto de Solución}}
  \riesgoTDieciseis{id=R-25, riesgo={La región Azure Chile Central deja de responder por un desastre}, categoria={Continuidad operativa}, probabilidad=1, impacto=5, exposicion=5, mitigacion={Brazil South en espera, conmutación en cuatro pasos con confirmación de la guardia y dos pruebas reales al año}, responsable={Líder de Operación}}
  \riesgoTDieciseis{id=R-26, riesgo={El retraso de la réplica asíncrona supera los 15 minutos de pérdida admitida con escritura intensa}, categoria={Continuidad operativa}, probabilidad=2, impacto=4, exposicion=8, mitigacion={Servidor de series separado, Event Hubs con retraso máximo de 10 minutos y reenvío de 72 horas desde el equipo a bordo}, responsable={Líder de Datos}}
  \riesgoTDieciseis{id=R-27, riesgo={La verificación bloqueante detiene un viaje comprometido que debía salir, por un dato vencido, un registro sin sincronizar o una regla mal calibrada}, categoria={Continuidad operativa}, probabilidad=3, impacto=4, exposicion=12, mitigacion={Verificación en paralelo sin bloquear en los meses 13 y 14, que mide cuántos viajes habría detenido y por qué, evaluación sobre el estado autoritativo con versión y vencimiento, y excepción RN-04 solo ante una fuente de evidencia no disponible, aprobada y registrada}, responsable={Líder Funcional}}
  \riesgoTDieciseis{id=R-28, riesgo={En un punto de carga sin cobertura, el documento completo que emite el sistema contable no vuelve a la cabina por satélite dentro de los 90 segundos de RT-09.01}, categoria={Técnicos}, probabilidad=3, impacto=4, exposicion=12, mitigacion={Emisión anticipada desde la orden en todo viaje cuya carga se conoce al programar, ensayo del retorno en fragmentos con el documento de mayor tamaño y salida bloqueada sin documento conforme}, responsable={Líder de Integración}}
\end{formularioTDieciseis}

\tituloBloqueFormulario{Respuesta, disparador, plazo y exposición residual}

La Tabla 8.3 completa cada riesgo con lo que pide FEP02, RT-19.04, p. 33: la estrategia de
respuesta, el disparador que la activa y el plazo, más la exposición antes y después de mitigar.

**Tabla 8.1.** Respuesta, disparador y plazo de cada riesgo

| ID | Respuesta | Disparador | Plazo | Exposición |
|---|---|---|---|---|
| R-01 | Mitigar | Retraso de proceso de Event Hubs sobre 10 minutos | Prueba CP-PERF-02 en A12 | 6 a 3 |
| R-02 | Mitigar | Camión que llega al terminal sin reporte reciente | Cambio en el mismo paso por terminal | 9 a 6 |
| R-03 | Evitar | Ficha o fabricante sin la certificación al cierre de A04 | Mes 4 | 8 a 4 |
| R-04 | Mitigar | Tramo medido sin cobertura que el diseño no consideraba | Meses 1 a 3 | 9 a 6 |
| R-05 | Mitigar | Uso diario de IoT Hub sobre el 75 % de su cuota | Revisión mensual | 6 a 3 |
| R-06 | Evitar | Un componente de la Etapa 1 que dependa de Azure Cache for Redis en el hito H2 | Mes 4 | 15 a 3 |
| R-07 | Mitigar | Decisión de arquitectura sin alternativa portable | Cada Comité de Arquitectura | 6 a 4 |
| R-08 | Mitigar | Proveedor sin interfaz de salida en la factibilidad | Meses 1 a 4 | 9 a 6 |
| R-09 | Mitigar | Fabricante sin autorización escrita al cierre de A04 | Mes 4 | 9 a 6 |
| R-10 | Mitigar | Caída de posiciones de un proveedor en el seguimiento mensual | Mensual | 9 a 6 |
| R-11 | Mitigar | 59 o menos RUT de los 148 iniciales con anexo firmado, vigente, no revocado y registrado al cierre del mes 9 (31-10-2027) | Mes 9 | 12 a 8 |
| R-12 | Mitigar | Prueba técnica fallida | Mes 3 | 6 a 4 |
| R-13 | Aceptar | Respuesta negativa a la consulta C-10 | Mes 2 | 6 a 4 |
| R-14 | Mitigar | Aumento de revocaciones en el indicador mensual de adhesión | Mensual desde el mes 6 | 9 a 6 |
| R-15 | Mitigar | Sesión con usuarios clave suspendida dos veces o entregable con observaciones | Cada entregable | 9 a 6 |
| R-16 | Mitigar | Entrega G13 incompleta el día 182 o consumo de más de la mitad de la reserva A14 | Quincenal hasta el día 240 | 8 a 4 |
| R-17 | Aceptar | Margen de un hito bajo 2 días hábiles | Semanal hasta H4 | 6 a 6 |
| R-18 | Mitigar | Condición de cierre bajo su umbral al cierre del mes 14 | Mes 14 | 12 a 8 |
| R-19 | Mitigar | Cobertura acumulada bajo la declarada para el mes | Meses 6 a 10 y 16 a 18 | 6 a 3 |
| R-20 | Mitigar | Menos de 24 de los 34 camiones de terceros sin equipo montados en el mes 16 | Mes 16 | 9 a 6 |
| R-21 | Evitar | Fecha de inicio del contrato distinta de febrero de 2027 | Firma del contrato | 10 a 5 |
| R-22 | Mitigar | Un certificado usado desde dos equipos | Revocación inmediata | 8 a 4 |
| R-23 | Mitigar | Vulnerabilidad crítica abierta o acceso anómalo | 7 días corridos | 12 a 8 |
| R-24 | Mitigar | Hito H2 sin aprobación del mandante | Mes 4 | 12 a 8 |
| R-25 | Transferir | Región primaria sin respuesta por 15 minutos | 4 horas (RTO) | 5 a 3 |
| R-26 | Mitigar | Retraso de la réplica cerca de 15 minutos | Continuo | 8 a 3 |
| R-27 | Mitigar | Viaje que la prueba en paralelo habría detenido sin causa válida | Meses 13 a 15 | 12 a 6 |
| R-28 | Mitigar | Ensayo con un retorno sobre 90 segundos o con fragmentos perdidos | Mes 3, con la prueba técnica del sistema contable | 12 a 8 |

*Fuente: elaboración propia. La exposición va de la inicial a la residual.*

Después de mitigar, ningún riesgo queda con exposición alta. Los cinco que quedan en 8 (R-11, R-18, R-23, R-24 y R-28)
conservan su impacto de 4, porque la mitigación baja su probabilidad y deja igual su consecuencia.

\tituloBloqueFormulario{Análisis de modos de falla de los componentes técnicos}

La Tabla 8.4 aplica el análisis de modos de falla a los componentes físicos de la solución. La
severidad (S) usa la escala de impacto y la ocurrencia (O) la de probabilidad. La detección (D) va de 1,
detección automática en menos de 30 segundos, a 5, falla que no se nota hasta que ocurre en ruta. El
número de prioridad es S × O × D, y un valor de 50 o más exige plan de contingencia.

**Tabla 8.2.** Análisis de modos de falla y efectos

| Modo de falla | Efecto | S | O | D | NPR | Detección | Riesgo |
|---|---|---|---|---|---|---|---|
| Equipo a bordo deja de registrar | Pérdida de registros del camión | 4 | 3 | 3 | 36 | Revisión al pasar por terminal | R-02 |
| Módem Iridium sin servicio en una sombra | Sin evento de emergencia ni documento sin cobertura | 4 | 2 | 4 | 32 | Lo nota el conductor al usarlo | R-04 |
| Grupo electrógeno no arranca en un corte | San Bernardo con 66 minutos de UPS | 3 | 2 | 3 | 18 | Prueba periódica en sitio | R-25 |
| Baliza sin batería o acople falso | Semirremolque sin verificar | 2 | 3 | 2 | 12 | Monitoreo de batería en la nube | R-22 |
| Lector CAN sin señal | Sin telemetría del motor | 2 | 2 | 2 | 8 | Monitoreo en la nube | R-09 |
| Búfer lleno por una sombra de más de 288 horas | Pérdida de los registros más antiguos | 4 | 1 | 2 | 8 | Monitoreo en la nube | R-04 |
| Réplica atrasada más de 15 minutos | Pérdida de datos sobre el RPO | 4 | 2 | 1 | 8 | Alerta automática | R-26 |
| Lector de tarjeta no lee | Conductor sin identificar | 3 | 2 | 1 | 6 | Aviso inmediato en cabina | R-02 |
| Ingesta saturada en una reconexión | Sincronización sobre 20 minutos | 3 | 2 | 1 | 6 | Alerta por profundidad de cola | R-01 |
| Enlace de terminal caído más de 24 horas | Terminal en procedimiento supletorio | 3 | 2 | 1 | 6 | Alerta automática | R-04 |

*Fuente: elaboración propia. Escala de detección del plan de riesgos (sección 8.1).*

Ningún modo de falla llega a 50. Los dos más altos, el equipo a bordo que deja de registrar y el módem
satelital sin servicio, tienen detección tardía. Su mitigación apunta a detectar antes la falla.

\end{formulario}

