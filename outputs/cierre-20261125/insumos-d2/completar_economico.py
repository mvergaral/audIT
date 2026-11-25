"""Completa fuentes E-21 usando partidas y texto conciliado; no altera precios."""
from pathlib import Path
import re, json, shutil
import openpyxl

ROOT=Path(__file__).resolve().parents[2]
OUT=Path(__file__).resolve().parent
BASE=ROOT/'recursos/Formato-Oferta-audIT'
cost=(BASE/'economico/costos-venta/contenido.tex').read_text(encoding='utf-8')
wb=openpyxl.load_workbook(ROOT/'outputs/cierre-entrega-final/evidencia/planilla-original-3.2.xlsx',data_only=True)

def write(relative,text):
    target=BASE/relative
    backup=OUT/'evidencia/fuentes-antes'/relative
    if target.exists() and not backup.exists():backup.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(target,backup)
    target.parent.mkdir(parents=True,exist_ok=True);target.write_text(text,encoding='utf-8')
    copy=OUT/'fuentes'/relative;copy.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(target,copy)

def body(name):
    start=cost.index('\\section{'+name+'}')
    start=cost.index('\n',start)+1
    end=cost.find('\\section{',start)
    return cost[start:end if end!=-1 else len(cost)].strip()

offer=r'''\begin{resumenApertura}
audIT oferta la implementación y la operación de la plataforma de Transportes Curimón como un
contrato de alcance completo, con precios por fase y pagos contra aceptación. Los valores se
concilian con la planilla de presupuesto 3.2 y sus partidas, sin incorporar recuperos hipotéticos
del mandante a los cobros de audIT.
\begin{recibe}
\item Precio, hitos, servicios incluidos, exclusiones y condiciones comerciales de la oferta.
\end{recibe}
\end{resumenApertura}

\section{Propuesta de valor económico}\label{sec:eco-valor}

La \tabref{eco-valores} presenta los precios de implementación y de los 36 meses de operación.
La suma es el valor total del contrato. Los valores netos, IVA y total se muestran en las tres
monedas del \form{E-24}{73}; la fase de operación no se anticipa a implementación.

\tablaMontos{Valores ofertados por fase}{eco-valores}{implementacion,operacion}

El precio total neto es \montoPartida{proyecto}. El hardware de campo y de red adquirido por el
mandante se informa por separado: no incrementa el ingreso ni el egreso de audIT.

\subsection{Tipo de cambio, reajustabilidad y vigencia}\label{sec:eco-condiciones}

Para esta oferta de fecha 25 de noviembre de 2026 se utilizan los parámetros convencionales
del E-24. Esa fecha identifica la aplicación de las bases a la oferta, no una cotización de
mercado. Los precios de ambas etapas de implementación son firmes, conforme al
\art{9.4}{7}. La operación se oferta sin reajuste: audIT asume la variación de sus costos
dentro del precio comprometido. El presupuesto base no incorpora reajustes de ingresos.

La oferta tiene vigencia comercial de 150 días corridos contados desde la fecha de entrega.
La vigencia y condiciones de la garantía de seriedad se acreditan por separado en el Sobre
N.º 1; este plazo comercial no sustituye dicha garantía ni certifica su emisión.

\section{Estructura de pagos detallada}\label{sec:eco-pagos}

La implementación se factura contra los doce hitos del \form{E-25}{74 y 75}. Un hito
presupuestado no acredita un acta ni un pago realizado: la aceptación exige el pronunciamiento
de la Contraparte Técnica y las evidencias del \art{18}{13}.

\subsection{Hitos de implementación}\label{sec:eco-hitos}

La \tabref{hitos-e25} distribuye el precio de implementación. Los porcentajes son los de
las bases y suman el 100 por ciento; los importes provienen de la partida implementación.

\tablaHitosPago

La \tabref{eco-criterios} vincula cada hito con la evidencia que debe aceptar la contraparte.
Los protocolos detallados y sus trazas a requerimientos se conservan en T-13 y T-17.

\begin{tabla}[ancho=completo]{Aceptación vinculada a los hitos de pago}{eco-criterios}{L{12mm} X}
Hito & Evidencia y condición de aceptación \\ \midrule
H1 & Acta de alcance, catálogo y matriz de trazabilidad aprobados. \\
H2 & Arquitectura, seguridad y modelo de datos aprobados. \\
H3 & Infraestructura híbrida y cuatro ambientes habilitados, con observabilidad probada. \\
H4 & Candidato E1 con QA superado y evidencia de cobertura, listo para pruebas. \\
H5 & Aceptación de usuario, carga, resiliencia y seguridad ofensiva E1 aprobadas. \\
H6 & Inicio de marcha blanca E1, reversión operativa y usuarios capacitados. \\
H7 & Cierre conforme de marcha blanca E1 y acta de paso a producción. \\
H8 & Línea base y diseño detallado E2 aprobados. \\
H9 & Candidato E2 con QA superado, listo para pruebas. \\
H10 & Certificación E2 y cierre del desarrollo aceptados. \\
H11 & Inicio de marcha blanca E2 en convivencia con E1 en producción. \\
H12 & Paso a producción E2 y aceptación final de implementación. \\
\end{tabla}

Cada acta debe acompañarse de artefacto, verificación objetiva, trazabilidad y resolución de
observaciones. Se respetan los plazos de revisión y subsanación del artículo 18; el modelo
distingue fecha contractual, facturación y cobro efectivo.

\subsection{Pagos mensuales de operación}\label{sec:eco-mensual}

La operación se factura de M21 a M56 en 36 pagos mensuales. El caso base cobra cada servicio
en el mes siguiente, de M22 a M57. La mensualidad neta es \montoPartida{cobro-m57}.
El componente fijo incluye operación, soporte, mantención, nube, conectividad y los servicios
presupuestados. No se presupuesta un componente variable positivo adicional ni cobros por hora
fuera de ese precio. Las deducciones por incumplimiento de SLA se aplican conforme al
\art{78}{40} y al E-25. La revisión de la factura y los indicadores no sustituye el
procedimiento de aplicación de multas.

\section{Resumen ejecutivo de valor}\label{sec:eco-resumen}

La \tabref{eco-incluidos} delimita los productos y servicios comprendidos. La asignación de
pagadores se concilia con T-11 y las hojas de proveedores para evitar que una exclusión
comercial elimine una prestación ya costeada.

\begin{tabla}[ancho=completo]{Servicios y productos incluidos}{eco-incluidos}{L{35mm} X}
Componente & Inclusión contractual \\ \midrule
Plataforma & Infraestructura on-premise de audIT, nube, observabilidad, seguridad y ambientes. \\
Software y datos & Alcances E1/E2, integraciones, migración, pruebas y documentación. \\
Instalación & Piloto, montaje externo por lotes M7--M9, banco, integración, supervisión y recepción interna. \\
Adopción & Capacitación, acompañamiento de marchas blancas y transferencia. \\
Operación & Mesa de ayuda, guardias, mantenimiento y campo externo por visita con coordinación interna. \\
Innovaciones & Cinco propuestas S13/T-19, con costo y atribución de personal identificados. \\
\end{tabla}

La infraestructura, integración y atención permanecen bajo responsabilidad de audIT aunque se
contraten servicios externos. Los criterios de cobertura y recepción son los de S3, S7 y S9.

\subsection{Exclusiones}\label{sec:eco-exclusiones}

Curimón adquiere el hardware de campo y de red especificado en T-11. Su referencia presupuestaria
es \montoPartida{hardware-mandante}, informada fuera del flujo de audIT. La exclusión de
combustible corresponde a la flota vehicular: no excluye las pruebas del grupo electrógeno
presupuestadas por audIT. No se eliminan de la oferta la energía, infraestructura, instalación,
conectividad ni servicios que el modelo incluye a cargo de audIT. Las ampliaciones de alcance
requieren gestión formal de cambios.

\subsection{Dependencias comerciales}\label{sec:eco-supuestos}

La puesta en servicio requiere equipos homologados y recibidos, accesos a terminales, ventanas
de montaje y factibilidad de integraciones con terceros. Las tarifas y calendarios de proveedores
son supuestos presupuestarios hasta contar con respaldo comercial. El financiamiento inicial y
la facilidad contingente no se presentan como aprobaciones bancarias emitidas. La subcontratación
se ejecutará bajo las autorizaciones y límites del \art{73}{38}, manteniendo responsabilidad
de audIT sobre el servicio.

\subsection{Beneficios del mandante}\label{sec:eco-beneficios}

El beneficio esperado se mide contra líneas base operacionales de S13/T-19. El recupero bruto
referencial de INN-4 es\par\noindent\montoPartida{recupero-inn4} en 36 meses, bajo el supuesto de recuperar
la mitad del monto objetado. No equivale a beneficio neto ni a cobro de audIT. Las otras mejoras
se someten a medición incremental y adopción, sin incorporar ahorros hipotéticos a ingresos
contractuales ni duplicar costos compartidos.

\subsection{Términos comerciales}\label{sec:eco-terminos}

La oferta comprende el alcance indivisible y el calendario del \art{17}{12}. Se expresan
neto, IVA y total en las monedas de evaluación. La facturación sigue el E-25 y la aceptación
del artículo 18. Las ampliaciones, exclusiones o cambios deben formalizarse sin alterar de
manera unilateral los plazos ni los criterios de recepción. Las referencias a financiación,
proveedores y beneficios mantienen sus condiciones de verificación y no acreditan ejecución.
'''
write('economico/oferta-economica/contenido.tex',offer)

analysis=r'''\begin{resumenApertura}
El análisis concilia costos, precio y liquidez de la configuración 3.2, manteniendo el precio
aprobado para esta oferta sin reajuste de operación. Se separan la rentabilidad del proyecto,
la tesorería financiada y los beneficios del mandante.
\begin{recibe}
\item Evaluación reproducible, calendario de adquisiciones, estructura de soporte y valorización de innovaciones.
\end{recibe}
\end{resumenApertura}

\section{Costos frente a precio}\label{sec:eco-costo-precio}
'''+body('Costo y precio por fase')+r'''

La \tabref{eco-componentes} contrasta el costo y precio de cada componente. El margen se
calcula sobre ventas; los porcentajes de componentes no se suman para obtener el consolidado.

\begin{tabla}[ancho=completo,fuente=condensada]{Costo y precio por componente}{eco-componentes}{L{30mm} X X}
Componente & Costo neto & Precio neto \\ \midrule
Implementación directa & \montoPartida{cuadro-impl-directo-costo} & \montoPartida{cuadro-impl-directo-venta} \\
Implementación indirecta & \montoPartida{cuadro-impl-indirecto-costo} & \montoPartida{cuadro-impl-indirecto-venta} \\
Operación directa & \montoPartida{cuadro-op-directo-costo} & \montoPartida{cuadro-op-directo-venta} \\
Operación indirecta & \montoPartida{cuadro-op-indirecto-costo} & \montoPartida{cuadro-op-indirecto-venta} \\
\end{tabla}

La operación indirecta se traslada sin margen en esta clasificación. El margen directo compensa
esa distribución y mantiene 18,50 por ciento sobre la venta neta total. La plantilla RESUMEN
presenta además utilidad sobre costo: son bases de comparación distintas.

\section{Evaluación financiera}\label{sec:eco-evaluacion}
'''+body('Evaluación financiera')+r'''

La reproducción del caso base se realizó en una copia de LibreOffice después de retirar los
valores guardados de las fórmulas. Los resultados se contrastaron contra el archivo 3.2. La
coincidencia del cálculo no valida por sí sola supuestos, contratos, capacidad ni una raíz
única de TIR. El criterio de decisión combina VAN, sensibilidad y liquidez.

\section{Curva S y flujo mensual}\label{sec:eco-curva}
'''+body('Curva contractual y solvencia')+r'''

La \tabref{eco-flujo-mensual} permite reproducir el flujo del proyecto y distinguirlo del
flujo financiado. Los valores se expresan en UF, con los parámetros convencionales E-24;
el modelo conserva las series exactas en CLP y sus conversiones. Fila A excluye financiamiento;
Fila C incorpora sus movimientos según las columnas del modelo. El saldo de caja es acumulado.

\input{./economico/datos/flujo-mensual-final.tex}

La cola de cobro de M57 se informa por separado y no se suma al VAN base M1--M56. Una caja
de cierre positiva no acredita disponibilidad diaria antes de los cobros; ese orden se revisa
en la sensibilidad de tesorería.

\section{Estrategia de adquisiciones}\label{sec:eco-estrategia}
'''+body('Proveedores y adquisiciones')+r'''

Se adquiere equipamiento estándar y se conservan integración, banco, pruebas y recepción como
responsabilidad de audIT. La negociación busca disponibilidad, garantías, soporte y calendario
de pagos compatibles con H3 y los lotes. La dependencia de importación y homologación debe
confirmarse antes de emitir cada orden; no se afirma una internación ni una cotización recibida.

\section{Costos operacionales y perfiles}\label{sec:eco-operacion}

La operación combina personal dedicado, guardia, proveedores de infraestructura, nube, licencias,
conectividad, campo y administración. La \tabref{eco-operacion-categorias} muestra el costo por
categoría para los 36 meses. Las partidas corresponden a Cuadro maestro y RESUMEN, sin sumar
por segunda vez infraestructura ya incorporada a proveedores.

\input{./economico/datos/operacion-categorias-final.tex}

El precio de operación permanece sin reajuste. La reducción de carga variable por madurez no
se aplica a costos fijos ni autoriza rebajar cobertura SLA. La nómina y los servicios de
campo se controlan por separado.

\subsection{Costos y tarifas por perfil}\label{sec:eco-tarifas}

La \tabref{eco-tarifas-final} identifica costos y tarifas de referencia por fase, su perfil
y el rango de comparación E-26. Los roles adicionales se declaran como tales: la referencia
de rango no constituye una acreditación de competencias. Las tarifas desagregan el precio
cerrado de personal y no generan facturación horaria adicional al E-25.

\input{./economico/datos/tarifas-final.tex}

La suma de horas por tarifa conserva la venta de personal de RESUMEN en implementación y
operación. Se utilizan valores sin redondear en el cálculo; la presentación no modifica los
totales del contrato ni la base del impuesto.

\section{Mantención y soporte}\label{sec:eco-mantencion}

El presupuesto mantiene cobertura fija, guardia y la carga variable por tramo de madurez.
Las reducciones desde M25, M33 y M45 requieren carga observada compatible con SLA, cobertura
por turno y capacidad de escalamiento. No son una autorización para dejar puestos sin cubrir.
La \tabref{eco-soporte-final} identifica el costo horario y la dedicación inicial de los paquetes.

\input{./economico/datos/soporte-final.tex}

Las horas de cierre M21--M24 se separan del régimen para evitar duplicarlas con mantenimiento
evolutivo. El campo externo por visita sustituye solo las tareas previstas y audIT conserva
coordinación, stock y recepción. La mantención preventiva se programa por activo, la correctiva
por incidente, y la evolutiva por bolsa priorizada con control de cambios y pruebas de regresión.
Los servicios de terceros y renovaciones se trazan a Proveedores, Detalle proveedores D4 y
Contrato de soporte. Los refuerzos por puesta en producción permanecen presupuestados.

\section{Valorización de innovaciones}\label{sec:eco-innovaciones}
'''+body('Innovaciones y capacidad')+r'''

La \tabref{eco-innovaciones-montos} explicita inversión y operación atribuidas y el beneficio
reconocido en el caso base. La atribución de nómina no se agrega como un segundo gasto y el
beneficio del mandante no se transforma en venta de audIT.

\tablaMontos*[fuente=condensada]{Atribución económica de las cinco innovaciones}{eco-innovaciones-montos}{innovacion-1-inversion,innovacion-1-costo,innovacion-1-beneficio,innovacion-2-inversion,innovacion-2-costo,innovacion-2-beneficio,innovacion-3-inversion,innovacion-3-costo,innovacion-3-beneficio,innovacion-4-inversion,innovacion-4-costo,innovacion-4-beneficio,innovacion-5-inversion,innovacion-5-costo,innovacion-5-beneficio}

La medición incremental requiere línea base, adopción y responsable. Se mantiene beneficio
monetario reconocido igual a cero para audIT, mientras que los resultados de Curimón se
evalúan separadamente y sin doble conteo entre innovaciones.
'''
write('economico/analisis-financiero/contenido.tex',analysis)

def tex_table(title,label,cols,headers,rows):
    esc=lambda x:str(x).replace('&',r'\&').replace('%',r'\%').replace('_',r'\_')
    return '\\begin{tabla}[ancho=completo,fuente=condensada]{'+title+'}{'+label+'}{'+cols+'}\n'+' & '.join(headers)+r' \\ \midrule'+'\n'+'\n'.join(' & '.join(esc(c) for c in r)+r' \\' for r in rows)+'\n\\end{tabla}\n'
fmt=lambda v:f'{v:,.2f}'.replace(',','@').replace('.',',').replace('@','.')
rows=[]
for row in wb['Flujo de Caja'].iter_rows(min_row=2,values_only=True):
    if isinstance(row[0],int) and 1<=row[0]<=56:
        rows.append([row[0]]+[fmt((row[j] or 0)/40000) for j in [5,6,7,23,22]])
write('economico/datos/flujo-mensual-final.tex',tex_table('Flujo mensual en UF','eco-flujo-mensual','L{9mm} R{26mm} R{26mm} R{26mm} R{26mm} X',['Mes','Cobro neto','Costo neto','Fila A','Fila C','Caja'],rows))
op=[]
for r in wb['Cuadro maestro'].iter_rows(min_row=11,max_row=18,values_only=True):
    if r[1] and isinstance(r[2],(float,int)):
        key='final-op-'+str(len(op)+1);op.append((key,r[1],r[2]))
p=BASE/'economico/datos/partidas.csv';data=p.read_text(encoding='utf-8')
for key,label,value in op:
    line=f'{key};{label};CLP;{value};no;\n'
    if key+';' not in data:data+='\n'+line
write('economico/datos/partidas.csv',data)
optex='\\tablaMontos*{Costo operacional por categoría}{eco-operacion-categorias}{'+','.join(p[0] for p in op)+'}\n'
write('economico/datos/operacion-categorias-final.tex',optex)
support=[]
for r in wb['Contrato de soporte'].iter_rows(min_row=2,max_row=13,values_only=True):
    if r[0]:support.append([r[0],fmt(r[1] or 0),fmt(r[2] or 0),fmt((r[3] or 0)/40000)])
write('economico/datos/soporte-final.tex',tex_table('Cobertura inicial de soporte','eco-soporte-final','X R{25mm} R{25mm} R{25mm}',['Paquete','Horas fijas','Horas variables','Costo UF/h'],support))
print('Fuentes E-21 completas; tarifario pendiente de incorporación según decisión del usuario.')
