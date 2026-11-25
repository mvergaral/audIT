# Formulario T-14. Plan de trabajo, EDT y carta Gantt

audIT, Empresa N.º 10. Licitación TFEP-01/2026, Caso 10 Transporte de Carga. Oferta Técnica, Sobre N.º 2. Propuesta final. Archivo AUDIT-Formulario-T-14.pdf. Anexo del Subdocumento N.º 7, Plan de trabajo, EDT, cronograma e implantación. Las fuentes están en las Referencias de ese subdocumento.

\begin{formulario}{T-14}

\providecommand\tituloBloqueFormulario[1]{
  \phantomsection\addcontentsline{toc}{section}{#1}{\sffamily\bfseries\fontsize{13bp}{16bp}\selectfont\color{audit-marino}#1}}

\begin{contenidoExigido}{T-14}
  \exigencia{Estructura de descomposición del trabajo con el 100 % del alcance, hasta paquetes estimables y asignables.}{sección 7.1}
  \exigencia{Diccionario de la EDT con entregable, criterio de aceptación y responsable por paquete.}{Este formulario, diccionario de la EDT}
  \exigencia{Secuenciamiento, estimación, ruta crítica y holguras, con PERT y CPM.}{sección 7.2.2 y sección 7.3.1}
  \exigencia{Carta Gantt de los 56 meses, alineada con el Artículo 17 y los hitos del Formulario E-25, con marcha blanca, pasos a producción e inicio de la Operación.}{sección 7.3.2}
  \exigencia{Frentes de trabajo, paralelización y solapamiento de los meses 13 a 15 y 19 a 20.}{sección 7.2.4 y sección 7.2.5}
\end{contenidoExigido}

\tituloBloqueFormulario{Diccionario de la EDT}

La Tabla 7.2 declara cada uno de los 54 paquetes de trabajo con su entregable, su criterio de
aceptación, el rol responsable y su ubicación en la red de actividades del Subdocumento 7 y en los meses
del contrato. Los roles son los del Formulario T-15. Los identificadores de actividad y de revisión son los de la malla detallada de
precedencias del mismo formulario.

**Tabla 7.1.** Diccionario de la EDT por paquete de trabajo

| Paquete | Entregable | Criterio de aceptación | Responsable | Red y meses |
|---|---|---|---|---|
| 1.1 | Plan de dirección e informes del proyecto | Plan aprobado en H1 y un informe en cada Comité de Proyecto | Jefe de Proyecto | A01, DIR-REC; M1--20 |
| 1.2 | Plan de comunicaciones y registro de interesados | Aprobado por el Comité Ejecutivo en el mes 1 | Jefe de Proyecto | A01, DIR-REC; M1--20 |
| 1.3 | Especificación de compra confirmada y actas de recepción del hardware del mandante | Equipos del Formulario T-11 recibidos conforme antes del mes 6 | Líder de Implantación | A04-HW; M1--4 |
| 2.1 | Línea base de alcance, catálogo y matriz de trazabilidad | Aprobación de la contraparte, hito H1 | Líder Funcional | A02; M1--2 |
| 2.2 | Mapa de cobertura móvil medida por tramo y punto de carga | Rutas de la compañía medidas en terreno, según RT-03.24 del Caso | Ingeniero de telecomunicaciones y campo | A03; M1--3 |
| 2.3 | Actas de factibilidad con los tres proveedores de posicionamiento y los fabricantes | Respuesta escrita de cada uno sobre el acceso a sus datos | Líder de Integración | A04; M1--4 |
| 2.4 | Documento de arquitectura, plan de seguridad y modelo de datos | Aprobación de la contraparte, hito H2 | Arquitecto de Solución | A05, A17; M2--4, M13--14 |
| 2.5 | Estudio de costo real por ruta y por contrato con datos históricos | Entregado a finanzas antes de la renegociación de 2027 | Líder de Datos | A05-COST, COST-M6; M4--6 |
| 3.1 | Ambientes de desarrollo, calidad, preproducción, producción y recuperación desde código | Hito H3 con los cinco ambientes operativos | Líder de Operación | A07, A07-DEV; M4--6 |
| 3.2 | Identidad federada, bóveda de claves y cifrado de campo | Prueba de seguridad ofensiva aprobada en H5 | Encargado de Seguridad de la Información | A07, A07-DEV, A12-SEC; M4--6, M10--11 |
| 3.3 | Trazas, métricas y registros correlacionados | Tablero operativo disponible en H3 | Líder de Operación | A07; M4--6 |
| 3.4 | Sala de San Bernardo remediada y cuatro gabinetes de terminal | 24 horas sin enlace probadas en cada sitio | Líder de Operación | A07-SALA; M4--8 |
| 4.1 | Firmware con operación de 72 horas y actualización en terminal | Prueba de 72 horas sin pérdida de eventos | Ingeniero de firmware | CPSEC-PREP, A11-HOM, G13-Q; M4--10 |
| 4.2 | 182 equipos audIT montados camión por camión | Acta de montaje por camión sin inmovilización adicional | Líder de Implantación | A11-PIL, L7, M7-KIT, L8, M8-KIT, L9, M9-KIT, A21-PATIO; M6--9, M17--19 |
| 4.3 | 192 camiones de terceros en la vista única por su plataforma | Posición recibida de cada plataforma que exporta | Líder de Integración | A18-INT; M13--15 |
| 5.1 | Contexto Personas y cumplimiento | Artefacto versionado disponible en H4 para pruebas de sistema; aceptación integrada en H5 conforme a T-17 | Líder de Desarrollo | A09-1, A09-2, A09-7; M6--7, M9 |
| 5.2 | Contexto Flota y activos | Artefacto versionado disponible en H4 para pruebas de sistema; aceptación integrada en H5 conforme a T-17 | Líder de Desarrollo | A09-3; M7 |
| 5.3 | Contexto Planificación y tráfico con verificación bloqueante | Asignación en 30 segundos en el percentil 95 | Líder de Desarrollo | A09-3; M7 |
| 5.4 | Contexto Telemetría y geocercas | Vista única y geocercas probadas con 72 horas sin enlace | Líder de Desarrollo | A09-4, A09-5; M8 |
| 5.5 | Contexto Operación de fletes | Documento, conformidad y carga peligrosa probados | Líder de Desarrollo | A09-5, A09-6; M8--9 |
| 5.6 | Contexto Liquidación y costeo | Costo en 24 horas y liquidación conciliada | Líder de Desarrollo | A09-8; M10 |
| 5.7 | Portal del transportista con consentimientos | Revocación efectiva en cinco minutos | Líder de Desarrollo | A09-7, A09-8; M9--10 |
| 6.1 | Interfaz con el sistema contable para el documento de transporte | Cero folios duplicados en la prueba de reintentos | Líder de Integración | PREP-678, A10-CONT; M4--8 |
| 6.2 | Ingesta de las plataformas de posicionamiento | Datos de cada plataforma factible en la vista única | Líder de Integración | PREP-678, A10-POS; M4--9 |
| 6.3 | Lectura de telemetría de fábrica y descarga de tacógrafos | Archivo original conservado con su integridad | Líder de Integración | PREP-678, A10-OEM; M4--9 |
| 6.4 | Integración de combustible, peaje y sistema de taller | Componentes de costo recibidos por viaje | Líder de Integración | PREP-678, A10-TALLER; M4--9 |
| 6.5 | Capa anticorrupción frente al sistema de 2013 y su retiro | Funciones retiradas en los meses 16 y 21 y consulta cerrada en el 24 | Líder de Integración | PREP-678, A10-LEG, A19, A21-LEG, A25, CIERRE-PREP, CE2-LEG, CE2-OFF, CIERRE24; M4--9, M16--19, M21--24 |
| 7.1 | Migración de las cerca de 6.000 vigencias | Acta de conciliación con verificación documental de cada una | Líder de Datos | PREP-678, A08-VIG, HIST-VALID; M4--12 |
| 7.2 | Migración histórica de maestros, viajes, liquidaciones y siniestros | Cinco años de viajes y seis de liquidaciones conciliados | Líder de Datos | PREP-678, A08-HIST1, HIST-VALID, A24-HIST2, CE2-DAT, CIERRE-PREP, CIERRE24; M4--12, M19--24 |
| 7.3 | Repositorio analítico | Costo por viaje en 24 horas y retención de RT-05.10 | Líder de Datos | PREP-678, A08-BI0, A08-BI1; M4--9 |
| 8.1 | Portal del cliente con posición autorizada | Posición en 2 minutos sólo con autorización vigente | Líder de Desarrollo | PREP-678, A17, A20-2, A20-4, A20-5; M4--5, M13--17 |
| 8.2 | Asignación de retornos | Retorno propuesto antes de la descarga | Líder de Desarrollo | PREP-678, A17, A20-1, A20-4, A20-5; M4--5, M13--17 |
| 8.3 | Cálculo mensual de emisiones | Método verificable aplicado a dos meses completos | Líder de Desarrollo | PREP-678, A17, A20-2, A20-4, A20-5; M4--5, M13--17 |
| 8.4 | Talleres externos y mantenimiento por kilometraje real | Intervención registrada en la hoja de vida | Líder de Desarrollo | PREP-678, A17, A20-3, A20-4, A20-5; M4--5, M13--17 |
| 8.5 | Modelo de dispersión de rendimiento | Modelo validado con doce meses de datos | Líder de Datos | PREP-678, A17, A20-1, A20-4, A20-5; M4--5, M13--17 |
| 9.1 | Anexo de adhesión al contrato de transporte | Validación jurídica del mandante | Líder Funcional | A06-ANEXO; M2--3 |
| 9.2 | Campaña y enrolamiento de transportistas | 104 anexos en el mes 16 y 134 en el 21 | Líder Funcional | A06-LOTE, A06-CAMP, A06-H12, L7, L8, L9; M3--20 |
| 9.3 | Medición mensual y medidas de refuerzo | Ocho indicadores; refuerzo con 59 o menos RUT de 148 iniciales firmados, vigentes y registrados al 31-10-2027 (M9 bajo SA-01), en ambas modalidades | Líder Funcional | A06-CAMP, A06-H12; M7--20 |
| 10.1 | Pruebas de sistema e integración | Hitos H4 y H9 | Líder de Calidad y Pruebas | INN5-Q, A09-1, A09-2, A09-3, A09-4, A09-5, A09-6, A09-7, G13-Q, A09-8, G13, A12-SIS, A20-1, A20-2, A20-3, A20-4, A20-5, A22-SIS; M6--12, M14--17 |
| 10.2 | Pruebas de desempeño, estrés, resiliencia y seguridad | Hitos H5 y H10 | Líder de Calidad y Pruebas | CPSEC-PREP, A12-SEC, A22-SEC; M6--11, M17 |
| 10.3 | Pruebas de aceptación de usuario | Acta por perfil de usuario | Líder de Calidad y Pruebas | A12-UAT, A22-SIS; M11, M17 |
| 11.1 | Capacitación de torre, terminales y conductores | G13 disponible antes de A13; diez días de familiarización y treinta de práctica y evaluación por turnos, sin afectar la operación; usuarios certificados | Líder de Implantación | G13-Q, G13, A13-FAM, A13-PRA; M10--12 |
| 11.2 | Marcha blanca y paso a producción de la Etapa 1 | Seis condiciones del Art. 17.3, hitos H6 y H7 | Líder de Implantación | A15, A19; M13--16 |
| 11.3 | Marcha blanca y paso a producción de la Etapa 2 | Seis condiciones del Art. 17.3, hitos H11 y H12 | Líder de Implantación | A24, A25; M19--21 |
| 11.4 | Estabilización y traspaso al área de tecnología del mandante | 30 días hábiles con dotación en terminales y traspaso certificado | Líder de Operación | A16, EST-E1-CONT, A21, CE2-EST, CIERRE24; M13--24 |
| 12.1 | Expediente verificable del transportista | 50 % de adheridos con expediente en M21; 99 % de verificaciones en hasta 5 s, mensual desde M16 | Arquitecto de Solución | INN1-D, INN1-C, A15-INN, A21-MED; M4, M8--10, M13--20 |
| 12.2 | Programación dinámica de intervenciones por oportunidad de patio | Metas propuestas T-19: preparación inútil reducida al menos 20 %; primer intento al menos 95 % en 20 intervenciones elegibles; sustitución hasta 30 min | Arquitecto de Solución | A11-INN2, A11-PIL, M7-KIT, M8-KIT, M9-KIT, INN2-OPT, A21-PATIO; M4--9, M16--19 |
| 12.3 | Acople verificado y registro térmico del semirremolque | Al menos 95 % de asignaciones verificadas y registro continuo de temperatura en el 100 % de viajes refrigerados, según T-19. Kilometraje en 8.4 y criterio 26 | Arquitecto de Solución | INN3-REG, A11-LECT, A11-BAL7, A11-BAL8, A11-BAL9, A11-INN3, A15-INN, A21-MED, A21-PATIO; M5--20 |
| 12.4 | Esquema de adhesión y propiedad del dispositivo | Cero posiciones fuera de ventana; reparto al 100 % de adheridos con cobro respaldado; revocaciones menores al 10 %, según T-19 | Líder Funcional | A06-ANEXO, A06-LOTE, A06-CAMP, A06-H12, INN4-C; M2--20 |
| 12.5 | Anticipación circadiana y aviso no punitivo de descanso | Efectividad incremental al menos 98 %; bloqueo 100 %; NASA-TLX menor a 35; adherencia al menos 85 %, según T-19. El catálogo base se verifica por criterio 28 | Arquitecto de Solución | INN5-D, INN5-C, INN5-Q, A15-INN, A21-MED; M4--20 |
| 13.1 | Mesa de servicio 24x7x365 | Niveles del Artículo 78.2 cumplidos cada mes | Líder de Operación | OP-N1; M21--56 |
| 13.2 | Operación de la plataforma y gestión del servicio | Disponibilidad y recuperación del Artículo 78.3 | Líder de Operación | OP-SERV, CE2-EST; M21--56 |
| 13.3 | Ciclo de vida del equipo a bordo | Actualización y reposición sólo en terminal | Líder de Operación | OP-CAMPO; M21--56 |
| 13.4 | Mantención evolutiva | Cambios con tasa de fallo bajo el 5 % | Líder de Desarrollo | OP-EVOL, CE2-EST; M21--56 |

*Fuente: elaboración propia. Hitos del FEP01, Formulario E-25, p. 74.*

Cada paquete tiene un entregable que el mandante recibe, un criterio que permite aceptarlo o rechazarlo y
un único rol responsable. Los paquetes 5.1 a 5.6 llevan el nombre de los seis contextos del Subdocumento
4; el paquete 5.7 corresponde al portal del transportista y los del elemento 12 remiten a las fichas del Formulario T-19, de modo que la EDT, la arquitectura y la
cartera de innovaciones usan los mismos nombres.

\tituloBloqueFormulario{Trazabilidad de aceptación}
La Tabla 7.3 vincula los 42 requisitos con los paquetes y casos diseñados de T-17. La aceptación se acredita con los resultados y actas previstos en cada caso, no con la sola existencia de esta matriz. Todas las pruebas se planifican para la ejecución del contrato.

**Tabla 7.2.** Requisitos, paquetes y casos de prueba diseñados

| Requisito | Paquetes EDT | Casos T-17 |
|---|---|---|
| RF-001 | 5.3 | CP-UNIT-01, CP-SYS-01, CP-HW-14, CP-PERF-04 |
| RF-002 | 5.1 | CP-UNIT-02, CP-INT-02, CP-SYS-05 |
| RF-003 | 5.1, 9.2 | CP-INT-03, CP-SYS-05, CP-HW-14 |
| RF-004 | 5.1 | CP-UNIT-06, CP-SEC-08 |
| RF-005 | 5.1, 7.1 | CP-UNIT-01, CP-SYS-08 |
| RF-006 | 5.5 | CP-UNIT-19, CP-SYS-06 |
| RF-007 | 6.3 | CP-HW-15, CP-INT-21 |
| RF-008 | 5.4, 6.2 | CP-SYS-16, CP-UAT-01 |
| RF-009 | 4.1 | CP-HW-03, CP-PERF-02 |
| RF-010 | 5.4 | CP-UNIT-08, CP-SYS-03 |
| RF-011 | 5.5 | CP-UNIT-12, CP-SYS-03 |
| RF-012 | 5.5 | CP-SYS-04, CP-INT-20 |
| RF-013 | 6.1 | CP-INT-11, CP-INT-12, CP-PERF-05 |
| RF-014 | 6.1, 4.1 | CP-UNIT-21, CP-HW-11, CP-PERF-05 |
| RF-015 | 8.2 | CP-UNIT-15, CP-SYS-09 |
| RF-016 | 5.6, 2.5 | CP-INT-23, CP-SYS-15 |
| RF-017 | 5.6 | CP-INT-23, CP-SYS-10 |
| RF-018 | 8.5 | CP-INT-18, CP-PERF-09 |
| RF-019 | 5.6 | CP-INT-24, CP-SYS-10 |
| RF-020 | 5.7 | CP-SEC-07, CP-PERF-10 |
| RF-021 | 8.1 | CP-SYS-19, CP-PERF-07 |
| RF-022 | 5.7 | CP-SEC-04, CP-SEC-05 |
| RF-023 | 8.3 | CP-UNIT-09, CP-SYS-17 |
| RF-024 | 8.4 | CP-INT-17, CP-UAT-02 |
| RF-025 | 8.4, 6.4 | CP-UNIT-14, CP-HW-04 |
| RF-026 | 9.2, 5.2 | CP-SYS-05, CP-UAT-09 |
| RF-027 | 4.1, 5.1 | CP-UNIT-18, CP-HW-06 |
| RF-028 | 5.3 | CP-SYS-05, CP-UAT-09 |
| RNF-001 | 4.1 | CP-UNIT-11, CP-HW-06 |
| RNF-002 | 4.1 | CP-UNIT-23, CP-HW-03 |
| RNF-003 | 6.2 | CP-INT-07, CP-INT-08 |
| RNF-004 | 4.2 | CP-UAT-02, CP-HW-08 |
| RNF-005 | 4.1, 6.3 | CP-UNIT-16, CP-HW-04 |
| RNF-006 | 6.1 | CP-INT-12, CP-INT-11 |
| RNF-007 | 5.4 | CP-UNIT-08, CP-SYS-03 |
| RNF-008 | 4.1, 3.4 | CP-HW-03, CP-PERF-02 |
| RNF-009 | 13.1, 11.4 | CP-SYS-16, CP-UAT-01 |
| RNF-010 | 1.1 | CP-PERF-08, CP-SYS-01 |
| RNF-011 | 11.2 | CP-INT-05, CP-SYS-05 |
| RNF-012 | 5.1 | CP-SEC-08, CP-UNIT-07 |
| RNF-013 | 3.2 | CP-SEC-04, CP-SEC-05 |
| RNF-014 | 7.3 | CP-SEC-08, CP-INT-25, CP-PERF-03 |

*Fuente: catálogo S3/T-12 y matriz de trazabilidad S9/T-17. Estado: pruebas diseñadas, no ejecutadas.*

Los casos de integración, sistema, desempeño, seguridad, hardware y aceptación conservan los perfiles y límites definidos por S9. La firma de la contraparte se obtiene al verificar los resultados de cada etapa.

\tituloBloqueFormulario{Carta Gantt por paquete}

La carta que sigue integra las ventanas de los 54 paquetes y los hitos E-25. La red completa y
el esfuerzo por tarea y rol se presentan en T-15; las figuras no sustituyen sus dependencias.
Las láminas de la carta se citan como Figura 7.1, Figura 7.2, Figura 7.3, Figura 7.4, Figura 7.5, Figura 7.6, Figura 7.7, Figura 7.8, Figura 7.9, Figura 7.10, Figura 7.11, Figura 7.12.

![Figura 7.1. Horizonte contractual M1--M56](../../subdocumentos/07-plan-trabajo/graficos/revisada/gantt-panorama.pdf)

*Figura 7.1. Horizonte contractual M1--M56*

Fuente: Elaboración propia.

![Figura 7.2. Cadena de control hasta H12](../../subdocumentos/07-plan-trabajo/graficos/revisada/gantt-cpm.pdf)

*Figura 7.2. Cadena de control hasta H12*

Fuente: Elaboración propia.

![Figura 7.3. Gestión y levantamiento](../../subdocumentos/07-plan-trabajo/graficos/revisada/gantt-gestion.pdf)

*Figura 7.3. Gestión y levantamiento*

Fuente: Elaboración propia.

![Figura 7.4. Plataforma y equipo a bordo](../../subdocumentos/07-plan-trabajo/graficos/revisada/gantt-plataforma.pdf)

*Figura 7.4. Plataforma y equipo a bordo*

Fuente: Elaboración propia.

![Figura 7.5. Construcción por capacidades E1](../../subdocumentos/07-plan-trabajo/graficos/revisada/gantt-e1.pdf)

*Figura 7.5. Construcción por capacidades E1*

Fuente: Elaboración propia.

![Figura 7.6. Integraciones y migración](../../subdocumentos/07-plan-trabajo/graficos/revisada/gantt-datos.pdf)

*Figura 7.6. Integraciones y migración*

Fuente: Elaboración propia.

![Figura 7.7. Capacidades E2 y adhesión](../../subdocumentos/07-plan-trabajo/graficos/revisada/gantt-e2.pdf)

*Figura 7.7. Capacidades E2 y adhesión*

Fuente: Elaboración propia.

![Figura 7.8. Calidad e implantación](../../subdocumentos/07-plan-trabajo/graficos/revisada/gantt-implantacion.pdf)

*Figura 7.8. Calidad e implantación*

Fuente: Elaboración propia.

![Figura 7.9. Ventanas de innovaciones](../../subdocumentos/07-plan-trabajo/graficos/revisada/gantt-innovaciones.pdf)

*Figura 7.9. Ventanas de innovaciones*

Fuente: Elaboración propia.

![Figura 7.10. Lotes de montaje y condiciones](../../subdocumentos/07-plan-trabajo/graficos/revisada/gantt-hitos.pdf)

*Figura 7.10. Lotes de montaje y condiciones*

Fuente: Elaboración propia.

![Figura 7.11. G13 reservas y cierre técnico](../../subdocumentos/07-plan-trabajo/graficos/revisada/gantt-control.pdf)

*Figura 7.11. G13 reservas y cierre técnico*

Fuente: Elaboración propia.

![Figura 7.12. Continuidad operacional M21--M56](../../subdocumentos/07-plan-trabajo/graficos/revisada/gantt-operacion.pdf)

*Figura 7.12. Continuidad operacional M21--M56*

Fuente: Elaboración propia.

\end{formulario}

