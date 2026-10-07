# Formulario T-14. Plan de trabajo, EDT y carta Gantt

audIT, Empresa N.º 10. Licitación TFEP-01/2026, Caso 10 Transporte de Carga. Oferta Técnica, Sobre N.º 2. Informe Preparatorio 2. Archivo AUDIT-Formulario-T-14.pdf. Anexo del Subdocumento N.º 7, Plan de trabajo, EDT, cronograma e implantación. Las fuentes están en las Referencias de ese subdocumento.

\begin{formulario}{T-14}

\providecommand\tituloBloqueFormulario[1]{
  \phantomsection\addcontentsline{toc}{section}{#1}{\sffamily\bfseries\fontsize{13bp}{16bp}\selectfont\color{audit-marino}#1}}

\begin{contenidoExigido}{T-14}
  \exigencia{Estructura de descomposición del trabajo con el 100 % del alcance, hasta paquetes estimables y asignables.}{sección 7.1}
  \exigencia{Diccionario de la EDT con entregable, criterio de aceptación y responsable por paquete.}{Este formulario, diccionario de la EDT}
  \exigencia{Secuenciamiento, estimación, ruta crítica y holguras, con PERT y CPM.}{sección 7.2.2 y sección 7.3.1}
  \exigencia{Carta Gantt de los 56 meses, alineada con el Artículo 17 y los hitos del Formulario E-25, con marcha blanca, pasos a producción e inicio de la Operación.}{sección 7.3.2}
  \exigencia{Frentes de trabajo, paralelización y solapamiento de los meses 13 a 15 y 19 a 20.}{sección 7.2.3 y sección 7.2.4}
\end{contenidoExigido}

\tituloBloqueFormulario{Diccionario de la EDT}

La Tabla 7.2 declara cada uno de los 54 paquetes de trabajo con su entregable, su criterio de
aceptación, el rol responsable y su ubicación en la red de actividades del Subdocumento 7 y en los meses
del contrato. Los roles son los del Formulario T-15. Las actividades A01 a A25 son las de la malla de
precedencias del mismo formulario.

**Tabla 7.1.** Diccionario de la EDT por paquete de trabajo

| Paquete | Entregable | Criterio de aceptación | Responsable | Red y meses |
|---|---|---|---|---|
| 1.1 | Plan de dirección e informes del proyecto | Plan aprobado en H1 y un informe en cada Comité de Proyecto | Jefe de Proyecto | A01, 1 a 21 |
| 1.2 | Plan de comunicaciones y registro de interesados | Aprobado por el Comité Ejecutivo en el mes 1 | Jefe de Proyecto | A01, 1 a 21 |
| 1.3 | Especificación de compra confirmada y actas de recepción del hardware del mandante | Equipos del Formulario T-11 recibidos conforme antes del mes 6 | Líder de Implantación | A04, 1 a 5 |
| 2.1 | Línea base de alcance, catálogo y matriz de trazabilidad | Aprobación de la contraparte, hito H1 | Líder Funcional | A02, 1 y 2 |
| 2.2 | Mapa de cobertura móvil medida por tramo y punto de carga | Rutas de la compañía medidas en terreno, según RT-03.24 del Caso | Ingeniero de telecomunicaciones y campo | A03, 1 a 3 |
| 2.3 | Actas de factibilidad con los tres proveedores de posicionamiento y los fabricantes | Respuesta escrita de cada uno sobre el acceso a sus datos | Líder de Integración | A04, 1 a 4 |
| 2.4 | Documento de arquitectura, plan de seguridad y modelo de datos | Aprobación de la contraparte, hito H2 | Arquitecto de Solución | A05, 2 a 4 |
| 2.5 | Estudio de costo real por ruta y por contrato con datos históricos | Entregado a finanzas antes de la renegociación de 2027 | Líder de Datos | Fuera de la red, 4 a 6 |
| 3.1 | Ambientes de desarrollo, calidad, preproducción, producción y recuperación desde código | Hito H3 con los cinco ambientes operativos | Líder de Operación | A07, 4 a 6 |
| 3.2 | Identidad federada, bóveda de claves y cifrado de campo | Prueba de seguridad ofensiva aprobada en H5 | Encargado de Seguridad de la Información | A07 y A12, 4 a 12 |
| 3.3 | Trazas, métricas y registros correlacionados | Tablero operativo disponible en H3 | Líder de Operación | A07, 4 a 6 |
| 3.4 | Sala de San Bernardo remediada y cuatro gabinetes de terminal | 24 horas sin enlace probadas en cada sitio | Líder de Operación | Paralelo a A07 a A12, 4 a 12 |
| 4.1 | Firmware con operación de 72 horas y actualización en terminal | Prueba de 72 horas sin pérdida de eventos | Ingeniero de firmware | A11, 4 a 9 |
| 4.2 | 182 equipos audIT montados camión por camión | Acta de montaje por camión sin inmovilización adicional | Líder de Implantación | A11 y A18, 6 a 10 y 16 a 18 |
| 4.3 | 192 camiones de terceros en la vista única por su plataforma | Posición recibida de cada plataforma que exporta | Líder de Integración | A10 y A18, 6 a 10 y 13 a 15 |
| 5.1 | Contexto Personas y cumplimiento | Pruebas de sistema aprobadas en H4 | Líder de Desarrollo | A09, 6 a 10 |
| 5.2 | Contexto Flota y activos | Pruebas de sistema aprobadas en H4 | Líder de Desarrollo | A09, 6 a 10 |
| 5.3 | Contexto Planificación y tráfico con verificación bloqueante | Asignación en 30 segundos en el percentil 95 | Líder de Desarrollo | A09, 6 a 10 |
| 5.4 | Contexto Telemetría y geocercas | Vista única y geocercas probadas con 72 horas sin enlace | Líder de Desarrollo | A09, 6 a 10 |
| 5.5 | Contexto Operación de fletes | Documento, conformidad y carga peligrosa probados | Líder de Desarrollo | A09, 6 a 10 |
| 5.6 | Contexto Liquidación y costeo | Costo en 24 horas y liquidación conciliada | Líder de Desarrollo | A09, 6 a 10 |
| 5.7 | Portal del transportista con consentimientos | Revocación efectiva en cinco minutos | Líder de Desarrollo | A09, 6 a 10 |
| 6.1 | Interfaz con el sistema contable para el documento de transporte | Cero folios duplicados en la prueba de reintentos | Líder de Integración | A10, 6 a 9 |
| 6.2 | Ingesta de las plataformas de posicionamiento | Datos de cada plataforma factible en la vista única | Líder de Integración | A10, 6 a 9 |
| 6.3 | Lectura de telemetría de fábrica y descarga de tacógrafos | Archivo original conservado con su integridad | Líder de Integración | A10, 6 a 9 |
| 6.4 | Integración de combustible, peaje y sistema de taller | Componentes de costo recibidos por viaje | Líder de Integración | A10, 6 a 9 |
| 6.5 | Capa anticorrupción frente al sistema de 2013 y su retiro | Funciones retiradas en los meses 16 y 21 y consulta cerrada en el 24 | Líder de Integración | A10, 6 a 9, y 16 a 24 |
| 7.1 | Migración de las cerca de 6.000 vigencias | Acta de conciliación con verificación documental de cada una | Líder de Datos | A08, 6 a 9 |
| 7.2 | Migración histórica de maestros, viajes, liquidaciones y siniestros | Cinco años de viajes y seis de liquidaciones conciliados | Líder de Datos | 6 a 12 y 19 a 24 |
| 7.3 | Repositorio analítico | Costo por viaje en 24 horas y retención de RT-05.10 | Líder de Datos | A09, 4 a 10 |
| 8.1 | Portal del cliente con posición autorizada | Posición en 2 minutos sólo con autorización vigente | Líder de Desarrollo | A17, A20 y A22, 13 a 18 |
| 8.2 | Asignación de retornos | Retorno propuesto antes de la descarga | Líder de Desarrollo | A17, A20 y A22, 13 a 18 |
| 8.3 | Cálculo mensual de emisiones | Método verificable aplicado a dos meses completos | Líder de Desarrollo | A17, A20 y A22, 13 a 18 |
| 8.4 | Talleres externos y mantenimiento por kilometraje real | Intervención registrada en la hoja de vida | Líder de Desarrollo | A17, A20 y A22, 13 a 18 |
| 8.5 | Modelo de dispersión de rendimiento | Modelo validado con doce meses de datos | Líder de Datos | A17, A20 y A22, 13 a 18 |
| 9.1 | Anexo de adhesión al contrato de transporte | Validación jurídica del mandante | Líder Funcional | A06, 2 a 3 |
| 9.2 | Campaña y enrolamiento de transportistas | 104 anexos en el mes 16 y 134 en el 21 | Líder Funcional | A06 y A18, 2 a 21 |
| 9.3 | Medición mensual y medidas de refuerzo | Ocho indicadores mensuales y medidas activadas si el mes 9 baja del 40 % | Líder Funcional | 2 a 21 |
| 10.1 | Pruebas de sistema e integración | Hitos H4 y H9 | Líder de Calidad y Pruebas | A09, A12, A20 y A22 |
| 10.2 | Pruebas de desempeño, estrés, resiliencia y seguridad | Hitos H5 y H10 | Líder de Calidad y Pruebas | A12 y A22 |
| 10.3 | Pruebas de aceptación de usuario | Acta por perfil de usuario | Líder de Calidad y Pruebas | A12 y A22 |
| 11.1 | Capacitación de torre, terminales y conductores | Torre y terminales certificados | Líder de Implantación | A13, 10 a 12 |
| 11.2 | Marcha blanca y paso a producción de la Etapa 1 | Seis condiciones del Art. 17.3, hitos H6 y H7 | Líder de Implantación | A15 y A19, 13 a 16 |
| 11.3 | Marcha blanca y paso a producción de la Etapa 2 | Seis condiciones del Art. 17.3, hitos H11 y H12 | Líder de Implantación | A24 y A25, 19 a 21 |
| 11.4 | Estabilización y traspaso al área de tecnología del mandante | 30 días hábiles con dotación en terminales y traspaso certificado | Líder de Operación | A16 y A21, 13 a 17 |
| 12.1 | Innovación 1, producto o servicio | Indicador y meta de su ficha del Formulario T-19 | Arquitecto de Solución | Según su ficha |
| 12.2 | Innovación 2, proceso | Indicador y meta de su ficha del Formulario T-19 | Arquitecto de Solución | Según su ficha |
| 12.3 | Innovación 3, tecnológica o de arquitectura | Indicador y meta de su ficha del Formulario T-19 | Arquitecto de Solución | Según su ficha |
| 12.4 | Innovación 4, modelo de negocio o de contratación | Indicador y meta de su ficha del Formulario T-19 | Líder Funcional | Según su ficha |
| 12.5 | Innovación 5, experiencia de usuario o impacto social | Indicador y meta de su ficha del Formulario T-19 | Arquitecto de Solución | Según su ficha |
| 13.1 | Mesa de servicio 24x7x365 | Niveles del Artículo 78.2 cumplidos cada mes | Líder de Operación | 21 a 56 |
| 13.2 | Operación de la plataforma y gestión del servicio | Disponibilidad y recuperación del Artículo 78.3 | Líder de Operación | 21 a 56 |
| 13.3 | Ciclo de vida del equipo a bordo | Actualización y reposición sólo en terminal | Líder de Operación | 21 a 56 |
| 13.4 | Mantención evolutiva | Cambios con tasa de fallo bajo el 5 % | Líder de Desarrollo | 21 a 56 |

*Fuente: elaboración propia. Hitos del FEP01, Formulario E-25, p. 74.*

Cada paquete tiene un entregable que el mandante recibe, un criterio que permite aceptarlo o rechazarlo y
un único rol responsable. Los paquetes del elemento 5 llevan el nombre de los contextos del Subdocumento
4 y los del elemento 12 remiten a las fichas del Formulario T-19, de modo que la EDT, la arquitectura y la
cartera de innovaciones usan los mismos nombres.

\end{formulario}

