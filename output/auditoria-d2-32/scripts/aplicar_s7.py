"""Aplica la conciliación documental de S7 a la referencia entregada 3.2."""
from pathlib import Path
import json,re
ROOT=Path(__file__).resolve().parents[2]/'tmp/cierre-entrega-3'
BASE=ROOT/'recursos/Formato-Oferta-audIT/subdocumentos/07-plan-trabajo'
p=BASE/'contenido.tex';s=p.read_text(encoding='utf-8')
s=s.replace('La dotación mes a mes, con 37 personas en el peak de los meses 13 a 17, y su esfuerzo por etapa en el Formulario T-15.','La capacidad interna mes a mes, con un máximo de 39,2306 FTE equivalentes en M7, el servicio externo y el esfuerzo por paquete en el Formulario T-15.')
s=s.replace('Cierres fronterizos por nieve & 4.1, 4.2 & Holguras A11 y A18 en la red CPM','Cierres fronterizos por nieve & 4.1, 4.2 & Ventanas de piloto y lotes, rutas alternativas y control de cambios')
a=s.index('La estimación usa el método');b=s.index('% ============================================================================\n\\section{Cronograma',a)
s=s[:a]+r'''La estimación separa capacidad de ingeniería, atención y servicio externo. Las actividades tienen
entregable y dependencia identificables en T-14/T-15. Las duraciones son ventanas de planificación;
la capacidad mensual contratada procede de la conciliación de perfiles y demanda de desarrollo.
El montaje utiliza 140 minutos de puesto por kit, 20 minutos de banco y 140 minutos de analista,
como hipótesis a validar en el piloto; no se presentan como tiempos ya medidos.

\subsection{Capacidad interna y servicio externo}\label{sec:7-dotacion}

La capacidad de implementación alcanza 39,2306 FTE equivalentes en M7. Un FTE equivale a 160 horas
mensuales; la fracción expresa contratación de capacidad y no un número nominal de personas.
La curva detallada por mes, tarea, rol y paquete está en T-15. Se presupuestan 99.626,67 horas
internas en M1--M20 y 84.606 en M21--M56, incluido el cierre de integraciones y migración.
Los refuerzos SRE y Software de H6, H7, H11 y H12 están dentro de esa contratación.

El montaje externo de M7--M9 sustituye las horas de puesto internas; audIT conserva banco,
analista, prueba y recepción. El técnico de implementación se mantiene antes de M19 y sale
desde ese mes. En operación hay 0,5 FTE interno de coordinación de campo, más visitas externas,
reposiciones y rondas. No se compromete una cuadrilla permanente de dos personas.

\subsection{Partición de capacidad en M13 a M15}\label{sec:7-particion}

En M13--M15 conviven la estabilización E1 y la construcción E2. El equipo base de referencia
es 37,0 FTE, dividido en 21,5 para E1, 14,1 para E2 y 1,4 de coordinación. Esa partición
es una regla de control del equipo base, no el máximo de contratación de toda la implementación.
M13 añade 160 horas SRE y 80 horas Software para la puesta en producción: total 38,5 FTE
equivalentes. M14 y M15 conservan 37,0. Los refuerzos no se cuentan simultáneamente en ambos frentes.

Los siete roles de dirección comparten su jornada al 80 por ciento entre los frentes y reservan
el resto a coordinación. El resto de los puestos mantiene frente primario y una única reserva
semanal. El líder de cada frente asigna la tarea del diccionario a su ejecutor y descuenta
guardia, atención, revisión y ausencia antes de fijar capacidad neta de sprint. No se identifica
capacidad bruta con horas netas de programación.

En terreno se programan los 35 relevos semanales de los cinco terminales con los siete analistas
de implantación presupuestados en este tramo. La agenda se confirma con cada terminal y
reserva capacitación por turno sin retirar usuarios críticos de la operación. El Jefe de Proyecto
revisa semanalmente cupos, ausencias y reemplazos. Si un cupo no se confirma se usa simulación
en PREPROD y se reasigna la práctica; no se certifica un usuario que no completó la evaluación.

\begin{compromiso}[metrica={35 turnos de relevo semanales en los cinco terminales durante marcha blanca y estabilización E1},
verifica={registro semanal de turno, ejecutor y suplencia},fuente={\caso{numeral 13.3}{27}}]
audIT mantiene presencia de implantación en el relevo y protege la atención de la operación vigente.
\end{compromiso}

\subsection{Solapamiento de M19 y M20}\label{sec:7-solapamiento-19-20}

La contratación interna equivale a 26,5 FTE en M19 y 25,0 en M20. El técnico de campo ya no
forma parte de esa nómina; la atención física se ejecuta por visita externa. La Etapa 1 en
producción y la Etapa 2 en marcha blanca comparten los registros de viaje, conductor, camión y
transportista. Cada contexto conserva un único dueño y la conciliación diaria contrasta el
resultado con el registro vigente. El refuerzo de H11 pertenece a M19 y no se extiende por
defecto a M20. T-15 contiene el presupuesto por perfil; el Líder de Operación protege primero
la continuidad E1 y el de Desarrollo ejecuta el alcance E2 sin usar dos veces la misma jornada.

\subsection{Continuidad y madurez del soporte}\label{sec:7-soporte32}

La mesa N1 dispone de seis agentes regulares y un FTE de suplencias y picos: 1.120 horas por mes.
La coordinación interna de campo dispone de 80 horas mensuales; el proveedor atiende tres visitas
correctivas y dos rondas regionales mensuales presupuestadas, además de las reposiciones incluidas
en el contrato. Los tiempos de respuesta y resolución se mantienen conforme al \art{78.2}{40}.
Las tarifas de servicio de campo son provisiones de presupuesto y requieren orden de servicio
y cobertura confirmada por sitio antes de su activación.

La carga variable de Software, Datos y QA utiliza factores 100, 75, 50 y 25 por ciento desde
M21, M25, M33 y M45. La cobertura fija permanece. Cada reducción exige dos meses sin P1,
backlog menor que diez y demanda dentro de capacidad; si no se cumple, se mantiene el factor
anterior y se activa el escenario sin reducción. La supervisión conserva los SLA y no convierte
una hipótesis de madurez en una reducción automática de la obligación de servicio.

El cierre M21--M24 de EDT6.5 y EDT7.2 tiene recursos de Arquitectura, Frontend, Datos y QA
en T-15, y una actividad formal de estabilización E2 posterior a H12. La aceptación contractual
no elimina ese trabajo ni lo duplica dentro de la mantención evolutiva.

'''+s[b:]
a=s.index('La red de la implementación tiene');b=s.index('\\subsection{Carta Gantt}',a)
s=s[:a]+r'''La red detallada del Formulario T-15 conecta entregables, revisiones, hitos y operación.
A09 y A20 son grupos de ocho y cinco sprints, respectivamente; los nodos individuales de diez
días identifican la entrega de cada contexto. G13 es una entrega probada de PREPROD al cierre
del séptimo sprint y habilita capacitación; su disponibilidad real es condición de inicio.

La red incorpora los lotes M6--M9, el escalamiento lógico M13--M15 sin intervención física,
el estudio EDT2.5 antes de M6, la migración histórica y la estabilización E2 hasta M24.
Cada relación declara FS o SS y su desfase. Se calculan ES, EF, LS, LF, HT y HL con cotas
propias de liberación y límite; la criticidad se interpreta contra esas fechas. La presencia
de varias tareas con HT cero no se presenta como una única ruta crítica hasta H12.

La \tabref{7-hitos} presenta las fechas de aceptación planificadas, incluidas las ventanas de
revisión de contraparte. Los inicios de marcha blanca H6 y H11 se fijan al comienzo de M13 y M19.
Las fechas civiles son una visualización de SA-01; al fijar el inicio contractual se contrastan
contra temporada de fruta, cierres y relevos sin desplazar los hitos del E-25.

\input{subdocumentos/07-plan-trabajo/graficos/conciliacion-3.2/hitos-resumen.tex}

Las reservas A14 y A23 son ventanas de contingencia de planificación y no una probabilidad
calculada de cumplimiento. Si se reciben observaciones se evalúa la subsanación y se registra
el consumo de reserva. Las duraciones nuevas deben contrastarse en H1 con el ejecutor y el
calendario real; esa revisión no autoriza mover las fechas obligatorias.

'''+s[b:]
a=s.index('La planificación se lee');b=s.index('% INICIO LAMINAS GANTT',a)
s=s[:a]+r'''La carta Gantt muestra las ventanas de los 54 paquetes, los hitos y la red de control.
La descomposición por contexto permite distinguir una dependencia técnica de la espera de un
acta. El Formulario T-14 incorpora directamente la carta, sin depender de una remisión al cuerpo.
T-15 presenta la red detallada y sus holguras; el presupuesto de capacidad se verifica por mes y perfil.

'''+s[b:]
a=s.index('La figura muestra tres cosas');b=s.index('\\subsection{Implantación y puesta en marcha}',a)
s=s[:a]+r'''El montaje se concentra en el piloto M6 y los lotes externos M7--M9, sin trabajos físicos
programados durante diciembre--abril bajo SA-01. El escalamiento de plataformas de terceros
M13--M15 es lógico. Las órdenes de montaje requieren firma de adhesión aplicable, stock recibido,
ventana normal de paso y reserva del proveedor por terminal. Una condición incumplida se trata
como desviación del escenario y exige reprogramación técnica y financiera, sin declarar equipos
instalados ni activar servicios de una unidad que aún no fue recibida.

'''+s[b:]
a=s.index('\\begin{tabla}{Equipos audIT montados');b=s.index('\\paragraph{Pruebas}',a)
s=s[:a]+r'''\begin{tabla}{Equipos audIT montados al cierre de cada mes}{7-cobertura}{L{20mm} L{35mm} R{28mm} X}
Mes & Modalidad de ejecución & Nuevos & Acumulados \\ \midrule
M6 & Piloto interno San Bernardo & 10 & 10 \\
M7 & Cinco terminales, proveedor externo & 60 & 70 \\
M8 & Cinco terminales, proveedor externo & 60 & 130 \\
M9 & Cinco terminales, proveedor externo & 52 & 182 \\
M10--M56 & Operación, reposición y crecimiento según orden & 0 de alta inicial & 182 de configuración inicial \\
\end{tabla}
\notaTabla{Fuente: calendario de instalación del escenario económico de referencia; piloto incluido en los 182 equipos, sin duplicarlo.}

La curva es el escenario de contratación, no evidencia de montaje ejecutado. Incluye 148 camiones
propios y 34 de terceros sin equipo; la distribución de los 34 entre lotes exige adhesión y paso
confirmados. La firma por RUT, el consentimiento de cada conductor, el montaje y la activación
se miden por separado. Para quien no haya completado esas condiciones se mantiene modalidad
de datos o documental y se registra la diferencia frente al presupuesto. No se transforma la meta
de adhesión M16/M21 en una instalación retroactiva.

Los cinco terminales reciben 12 kits cada uno en M7 y M8. En M9 San Bernardo recibe 12 y cada
terminal regional diez. audIT conserva banco y recepción; el proveedor aporta 401,33 horas
de puesto para los 172 montajes externos. Las 210 balizas iniciales se montan M7--M9, a razón
de 70 por mes y 15 minutos presupuestados cada una; las 21 de reposición son stock. Los cinco
lectores de portería se prueban M5--M6, dos horas por lector. Los 19 equipos a bordo de reserva
no se cuentan como altas iniciales. El criterio de montaje exige permanecer dentro de la
estadía normal; los 140 minutos son hipótesis a validar, no una ampliación de la estadía.

'''+s[b:]
s=s.replace('Nada se\npierde al revertir. Los documentos de transporte ya emitidos son del sistema contable y no dependen de la\nplataforma, y los equipos a bordo conservan lo enviado durante 72 horas para reenviarlo. La reversión de\nun firmware usa la imagen anterior que guarda el gabinete del terminal (\\verSeccion{sec:4-dc-secundario}).','Se preservan los registros transaccionales y se cotejan viajes, documentos y eventos por identificador. El ensayo CP-SYS-20 comprueba reenvío y deduplicación antes del paso. El firmware retorna por A/B ante fallo de arranque; la imagen del terminal respalda la recuperación presencial en una visita posterior si resulta necesaria (\\verSeccion{sec:4-dc-secundario}).')
s=s.replace('La de la Etapa 1 tiene 20 días hábiles de holgura antes de afectar la marcha\nblanca de la Etapa 2, según la \\verSeccion{sec:7-ruta}. La de la Etapa 2 no tiene holgura y por eso está\nprotegida por la reserva A23.','La red de T-15 calcula el margen por actividad y límite contractual; una extensión requiere revisar la fecha de aceptación, capacidad y reserva consumida. La Etapa 2 mantiene la reserva A23 y la fecha de H12.')
p.write_text(s,encoding='utf-8')
# T-14 usa la misma codificación; elimina ventanas incompatibles con la base 3.2.
p=BASE/'formularios/T-14.tex';s=p.read_text(encoding='utf-8')
s=s.replace('Fuera de la red, 4 a 6','A25-COSTO, 4 a 6').replace('A11 y A18, 6 a 10 y 16 a 18','LOT-P y LOT7/8/9, 6 a 9').replace('A10 y A18, 6 a 10 y 13 a 15','A10 y A18-INT, 6 a 10 y 13 a 15').replace('A10, 6 a 9, y 16 a 24','A10 y MIG-CIERRE, 6 a 10 y 16 a 24').replace('6 a 12 y 19 a 24','MIG-HIST y MIG-CIERRE, 6 a 12 y 19 a 24')
s=s.replace('Preparación M4–M5; piloto M6; M6–M9 y M16–M18','Preparación M4--M5; piloto M6; lotes M7--M9').replace('M6–M10; activación M13–M15; M16–M18','Lectores M5--M6; balizas M7--M9; activación M13--M15')
s=s.replace('A16 y A21, 13 a 17','A16, A21 y EST-E2, 13 a 17 y 21 a 24')
s=s.replace('Las actividades A01 a A25 son las de la malla de','Los identificadores de actividad y de revisión son los de la malla detallada de')
s=s.replace('\\end{formulario}',r'''
\tituloBloqueFormulario{Carta Gantt por paquete}

La carta que sigue integra las ventanas de los 54 paquetes y los hitos E-25. La red completa y
el esfuerzo por tarea y rol se presentan en T-15; las figuras no sustituyen sus dependencias.
\input{subdocumentos/07-plan-trabajo/graficos/conciliacion-3.2/gantt-formulario.tex}

\end{formulario}''')
p.write_text(s,encoding='utf-8')
# T-15 sustituye las curvas previas en lugar de dejar dos líneas base activas.
(BASE/'formularios/T-15.tex').write_text(r'''\begin{formulario}{T-15}

La nivelación separa capacidad interna, trabajo externo y ventanas de contraparte. La referencia
de contratación se concilia por perfil y mes; cada asignación pertenece a un único paquete.
El esfuerzo atribuible a una innovación se descuenta antes de repartir el saldo de capacidad.

\input{subdocumentos/07-plan-trabajo/graficos/conciliacion-3.2/horas-formulario.tex}

\subsection*{Servicio físico externo y reservas de atención}

Los 172 montajes externos M7--M9 requieren 401,33 horas de puesto. No se añaden a las horas
internas contratadas; se pagan en el servicio de montaje. audIT conserva 60,67 horas de banco
y 424,67 horas de analista para los 182 equipos incluidos los pilotos, dentro de la capacidad
interna. Las 52,5 horas de montaje de balizas y diez horas de lectores se reservan en campo y
electrónica. Una misma intervención compartida conserva una sola imputación.

En M21--M56, EDT13.1 incluye 960 horas regulares y 160 de suplencias por mes. EDT13.3 dispone
de 80 horas internas de recepción, stock y coordinación, más visitas externas. La cobertura fija
no se reduce con la madurez; la bolsa variable pasa a 75, 50 y 25 por ciento en M25, M33 y M45
sujeta a los criterios de servicio de S7. Se conservan los refuerzos de H6/H7/H11/H12 y el cierre
de integraciones y datos M21--M24 en su celda de nómina, sin volver a sumarlos como costo adicional.

\subsection*{Red detallada y aceptación contractual}

La malla descompone A09 y A20 en entregas de sprint con dependencias entre personas, flota,
asignación, documento y costo. A18-INT cubre escalamiento lógico; el montaje inicial termina
en LOT9. El estudio de costo por ruta, la migración histórica y la estabilización E2 tienen
nodos propios y recursos identificados en las tablas de este formulario.

\input{subdocumentos/07-plan-trabajo/graficos/conciliacion-3.2/malla-formulario.tex}

\end{formulario}
''',encoding='utf-8')
# T-18 conserva el procedimiento local mejorado, actualiza el calendario físico.
p=BASE/'formularios/T-18.tex';s=p.read_text(encoding='utf-8')
s=s.replace('6 a 10 & Julio a noviembre 2027 & Montaje de la flota propia y de los terceros adheridos & Acta de montaje por camión','6 a 9 & Julio a octubre 2027 & Piloto 10 y lotes externos 60, 60 y 52 en cinco terminales & Adhesión, stock, ventana y acta por unidad')
s=s.replace('16 a 18 & Mayo a julio 2028 & Montaje de los terceros adheridos pendientes y talleres externos registrados & Acta de montaje por camión','13 a 15 & Febrero a abril 2028 & Escalamiento lógico de plataformas de terceros sin intervención física & Factibilidad, consentimiento y posición conciliada')
s=s.replace('21 & Octubre 2028 & Paso a producción en la segunda quincena e inicio de la operación & Acta de aceptación final, hito H12 \\\\','21 & Octubre 2028 & Paso a producción en la segunda quincena e inicio de la operación & Acta de aceptación final, hito H12 \\\\\n21 a 24 & Octubre 2028 a enero 2029 & Estabilización E2 y cierre de integraciones/migración & Acta de traspaso y diferencias resueltas \\\\')
s=s.replace('disponiblealdía','disponible al día').replace('días 182 a 222','días 180 a 220').replace('diez días antes del fin de A09','diez días antes del fin de A09-8')
s=s.replace('\\end{formulario}',r'''
\tituloBloqueFormulario{Condiciones de montaje y atención de campo}

El calendario base completa los 182 equipos en M9. La adhesión por transportista, el
consentimiento por conductor, el montaje y la activación son registros distintos. El proveedor
ejecuta los lotes masivos; audIT conserva banco, recepción y prueba. Si no se recibe una firma,
kit o ventana a tiempo se registra desviación y se reprograma el escenario técnico y financiero;
no se certifica como instalada la unidad pendiente. Los 140 minutos por kit son estimación de
puesto a validar en piloto y deben caber en la estadía normal.

Las 210 balizas iniciales se montan M7--M9, y cinco lectores M5--M6; 21 balizas y 19 equipos
a bordo son reserva de reposición. En operación hay 80 horas internas mensuales para campo
y un servicio externo de visitas y rondas. La contratación exige disponibilidad por terminal,
registro de despacho y escalamiento para mantener el tiempo de respuesta y resolución.

\end{formulario}''')
p.write_text(s,encoding='utf-8')
print('Fuentes S7/T-14/T-15/T-18 conciliadas')
