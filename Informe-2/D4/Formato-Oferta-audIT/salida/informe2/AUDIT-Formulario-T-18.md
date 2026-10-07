# Formulario T-18. Propuesta de implantación y puesta en marcha controlada

audIT, Empresa N.º 10. Licitación TFEP-01/2026, Caso 10 Transporte de Carga. Oferta Técnica, Sobre N.º 2. Informe Preparatorio 2. Archivo AUDIT-Formulario-T-18.pdf. Anexo del Subdocumento N.º 7, Plan de trabajo, EDT, cronograma e implantación. Las fuentes están en las Referencias de ese subdocumento.

\begin{formulario}{T-18}

\providecommand\tituloBloqueFormulario[1]{
  \phantomsection\addcontentsline{toc}{section}{#1}{\sffamily\bfseries\fontsize{13bp}{16bp}\selectfont\color{audit-marino}#1}}

\begin{contenidoExigido}{T-18}
  \exigencia{Etapa 1: marcha blanca de los meses 13 a 15 y producción desde el mes 16.}{sección 7.3.4 y este formulario}
  \exigencia{Etapa 2: marcha blanca de los meses 19 y 20 y producción desde el mes 21.}{sección 7.3.4 y este formulario}
  \exigencia{Plan de convivencia entre ambas etapas.}{sección 7.2.4 y este formulario}
  \exigencia{Procedimiento de reversión.}{sección 7.3.3 y este formulario}
\end{contenidoExigido}

\tituloBloqueFormulario{Implantación de la Etapa 1}

La Etapa 1 se implanta por proceso y por terminal, y nunca como un evento único. La
Tabla 7.2 da la secuencia desde la capacitación hasta el fin de la estabilización, con el
calendario que resulta del inicio en febrero de 2027.

**Tabla 7.1.** Secuencia de implantación de la Etapa 1

| Meses | Calendario | Qué se habilita | Condición para avanzar |
|---|---|---|---|
| 6 a 10 | Julio a noviembre 2027 | Montaje de la flota propia y de los terceros adheridos | Acta de montaje por camión |
| 10 a 12 | Noviembre 2027 a enero 2028 | Capacitación de torre, terminales y conductores en el relevo | Usuarios certificados |
| 13 | Febrero 2028 | Vigencias, jornada, viaje y posición en registro paralelo, primero en San Bernardo | Conciliación diaria sin diferencias |
| 13 y 14 | Febrero y marzo 2028 | Documento de transporte y verificación bloqueante en paralelo, sin bloquear | Motivos de bloqueo explicados |
| 14 | Marzo 2028 | Liquidación por las dos vías, transportista por transportista | Diferencias explicadas |
| 15 | Abril 2028 | Bloqueo efectivo en la flota propia con regla de excepción y portal del transportista | Seis condiciones del Art. 17.3 |
| 16 | Mayo 2028 | Paso a producción en la segunda quincena, después del cierre mensual | Acta de aceptación, hito H7 |
| 16 y 17 | Mayo y junio 2028 | Estabilización con un analista por terminal en el relevo | 30 días hábiles sin incidente crítico |

*Fuente: elaboración propia sobre el FEP01, Artículo 17.1, p. 12 y el Caso, numeral 13.3, pp. 27 y 28.*

Los terminales regionales entran en el orden en que se mida su volumen de camiones en el levantamiento,
una semana después de San Bernardo cada uno. El paso a producción ocurre después de la temporada de fruta
y fuera del cierre mensual de liquidaciones, que es la ventana que el Caso, numeral 13.3, p. 28 protege.

\tituloBloqueFormulario{Implantación de la Etapa 2}

La Etapa 2 se implanta sobre la Etapa 1 en producción. La Tabla 7.3 da su secuencia.

**Tabla 7.2.** Secuencia de implantación de la Etapa 2

| Meses | Calendario | Qué se habilita | Condición para avanzar |
|---|---|---|---|
| 16 a 18 | Mayo a julio 2028 | Montaje de los terceros adheridos pendientes y talleres externos registrados | Acta de montaje por camión |
| 19 | Agosto 2028 | Portal del cliente con posición autorizada y registro de talleres | Cero posiciones sin autorización |
| 19 y 20 | Agosto y septiembre 2028 | Retornos propuestos sin asignación automática y cálculo de emisiones | Conciliación con viajes reales |
| 21 | Octubre 2028 | Paso a producción en la segunda quincena e inicio de la operación | Acta de aceptación final, hito H12 |

*Fuente: elaboración propia sobre el FEP01, Artículo 17.1, p. 12.*

El paso a producción de la Etapa 2 no redespliega los servicios de la Etapa 1: los procesos nuevos se
agregan como servicios propios que leen los datos existentes. Así se cumple que la Etapa 2 no degrade la
disponibilidad, el desempeño ni la integridad de la Etapa 1 (FEP01, Artículo 17.2, p. 13).

\tituloBloqueFormulario{Convivencia entre ambas etapas}

En los meses 19 y 20 conviven la Etapa 1 en producción y la Etapa 2 en marcha blanca. La convivencia se
gobierna con tres reglas. Los datos de viaje, conductor, camión y transportista tienen un solo dueño, el
contexto de la Etapa 1 que los crea, y la Etapa 2 los lee por eventos sin copiarlos. Ningún usuario
digita en la Etapa 2 algo que ya existe en la Etapa 1. Y la conciliación diaria compara los resultados
de la Etapa 2 con los viajes reales de la Etapa 1, con toda diferencia explicada antes del día
siguiente. Desde el mes 21 la operación cubre los dos alcances desde el primer día.

\tituloBloqueFormulario{Procedimiento de reversión}

La Tabla 7.4 es el procedimiento de reversión de un paso a producción. Se ensaya en
preproducción antes de cada paso y queda disponible durante toda la estabilización.

**Tabla 7.3.** Procedimiento de reversión de un paso a producción

| Paso | Acción | Responsable | Tiempo máximo |
|---|---|---|---|
| 1 | Detectar un incidente crítico atribuible a la versión nueva o una diferencia de conciliación sin explicar | Guardia de la mesa de servicio | 15 minutos |
| 2 | Decidir la reversión con la contraparte técnica informada | Jefe de Proyecto y Líder de Operación | 30 minutos |
| 3 | Cambiar el tráfico de la puerta de enlace a la versión anterior del servicio afectado | Ingeniero SRE de guardia | 15 minutos |
| 4 | Recibir los eventos que los equipos a bordo reenvían desde su copia de 72 horas | Líder de Operación | 20 minutos por camión |
| 5 | Conciliar los viajes y documentos del período con el sistema contable | Líder de Datos | 24 horas |
| 6 | Informar la causa raíz al mandante | Jefe de Proyecto | 5 días hábiles |

*Fuente: elaboración propia sobre el FEP01, Artículo 78.2, p. 40 y el Caso, RT-03.13, p. 31.*

La reversión no pierde información. Los documentos de transporte ya emitidos son del sistema contable y no
dependen de la plataforma, y los equipos a bordo conservan lo enviado durante 72 horas. Si la reversión
afecta un firmware, se reinstala la imagen anterior que guarda el gabinete del terminal en el siguiente
paso del camión. Durante la marcha blanca la reversión es más simple: la forma actual de trabajar sigue
operando en paralelo y basta con dejar de usar el proceso nuevo.

\end{formulario}

