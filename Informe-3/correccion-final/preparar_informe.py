"""Genera contenido LaTeX y figuras desde la planilla corregida recalculada."""
import csv,json,re,math
from decimal import Decimal,ROUND_HALF_UP
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import openpyxl
R=Path(__file__).resolve().parents[2];D=Path(__file__).resolve().parent;O=R/'outputs/informe3-corregido'
b=openpyxl.load_workbook(O/'entrega/INFORME3_AUDIT_PLANILLA_20261114.xlsx',data_only=True)
m=json.loads((O/'revision/resultados.json').read_text());eco=D/'economico';(eco/'costos-venta').mkdir(parents=True,exist_ok=True);(eco/'datos').mkdir(exist_ok=True)
fig=eco/'figuras';fig.mkdir(exist_ok=True)
def v(s,a):return b[s][a].value
def entero(x):return int(Decimal(str(x)).quantize(Decimal('1'),rounding=ROUND_HALF_UP))
def num(x,p=2):return f'{x:,.{p}f}'.replace(',','X').replace('.',',').replace('X','.')
def uf(x):return num(entero(x)/40000)
def esc(s):return str(s).replace('&',r'\&').replace('%',r'\%').replace('_',r'\_')
def roots(a):
 def f(r):return sum(x/(1+r)**i for i,x in enumerate(a,1))
 result=[]
 for i in range(3000):
  lo,hi=i/1000,(i+1)/1000
  if f(lo)*f(hi)<0:
   for _ in range(45):
    t=(lo+hi)/2
    if f(lo)*f(t)<0:hi=t
    else:lo=t
   result.append((lo+hi)/2)
 return result
baseflow=[v('Flujo de Caja',f'H{r}') for r in range(2,58)];m['raices_tir_base']=roots(baseflow)
m['raices_tir_escenarios']={}
for i in range(7):m['raices_tir_escenarios'][v('Sensibilidad',f'A{i+2}')]=roots([v('Escenarios corregidos',f'G{r}') for r in range(2+i*57,58+i*57)])
(O/'revision/resultados.json').write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n')
part={
 'costo':(m['costo_clp'],'Costo neto del proyecto','no','Control de entrega!B11'),
 'venta':(m['venta_clp'],'Venta neta del proyecto','si','RESUMEN!H8'),
 'implementacion':(v('RESUMEN','H6'),'Precio de implementación','si','RESUMEN!H6'),
 'operacion':(v('RESUMEN','H7'),'Precio de los 36 meses de operación','si','RESUMEN!H7'),
 'costo-impl':(v('RESUMEN','C6'),'Costo neto de implementación','no','RESUMEN!C6'),
 'costo-op':(v('RESUMEN','C7'),'Costo neto de operación','no','RESUMEN!C7'),
 'van':(m['van_clp'],'Valor actual neto','no','Indicadores!B2'),
 'capital':(m['capital_inicial_clp'],'Capital inicial','no','Parámetros corrección!B4'),
 'capital-anterior':(274452748,'Capital del corte de referencia anterior','no',''),
 'banco':(m['capital_inicial_clp']*.8,'Desembolso bancario inicial','no','Financiamiento!D2'),
 'socios':(m['capital_inicial_clp']*.2,'Aporte inicial de socios','no','Financiamiento!C2'),
 'puente':(m['facilidad_contingente_clp'],'Facilidad contingente total','no','Parámetros corrección!B28'),
 'piso':(v('Parámetros corrección','B3'),'Piso de liquidez','no','Parámetros corrección!B3'),
 'caja-min':(m['caja_minima_tesoreria'],'Caja mínima de tesorería','no','Control de entrega!B2'),
 'cota':(v('Control de entrega','B21'),'Mínimo con pagos antes de cobros','no','Control de entrega!B21'),
 'montaje-neto':(sum(v('Instalación por lote',f'H{r}') for r in range(2,22)),'Servicio externo de montaje','si',''),
 'montaje-evitado':(sum(v('Instalación por lote',f'K{r}') for r in range(2,22)),'Costo interno sustituido','no',''),
 'hardware':(225384199,'Hardware de cargo del mandante, informativo','si',''),
 'reserva':(v('Parámetros corrección','B26'),'Reserva D4 del estrés','no','Parámetros corrección!B26'),
 'intereses':(sum(v('Flujo de Caja',f'P{r}') for r in range(2,59)),'Interés bancario total base','no',''),
 'comision':(v('Parámetros corrección','B29'),'Comisión presupuestada del crédito','no','Parámetros corrección!B29'),
 'cobro-m57':(v('Flujo de Caja','F58'),'Cobro de la última factura operativa en M57','no','Indicadores!B8'),
 'soporte21':(v('Personal','D22'),'Personal de operación M21','no','Personal!D22'),
 'soporte25':(v('Personal','D26'),'Personal de operación M25','no','Personal!D26'),
 'soporte33':(v('Personal','D34'),'Personal de operación M33','no','Personal!D34'),
 'soporte45':(v('Personal','D46'),'Personal de operación M45','no','Personal!D46'),
 'firma':(sum(v('Costos',f'L{r}') for r in range(2,58)),'Firma automatizada INN1','si',''),
 'recupero':(v('Beneficios Curimón','B4'),'Recupero bruto referencial de sobreestadías','no','Beneficios Curimón!B4'),
 'capacidad-inn1':(v('Beneficios Curimón','B3'),'Capacidad anual liberada, hipótesis INN1','no','Beneficios Curimón!B3'),
 'equilibrio':(v('Indicadores','B13'),'Venta nominal a VAN cero','no','Indicadores!B13'),
}
for r in range(2,7):
 part[f'inn{r-1}-personal']=(v('Innovaciones',f'C{r}'),f'Costo personal atribuido INN-{r-1}','no',f'Innovaciones!C{r}')
 part[f'inn{r-1}-directo']=(v('Innovaciones',f'D{r}'),f'Egreso directo INN-{r-1}','no',f'Innovaciones!D{r}')
with (eco/'datos/partidas.csv').open('w') as f:
 f.write('clave;concepto;moneda;valor;iva;planilla\n')
 for k,(x,t,iva,cell) in part.items():f.write(f'{k};{t};CLP;{entero(x)};{iva};{cell if k!="costo" else "RESUMEN!C8"}\n')
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'axes.spines.top':False,'axes.spines.right':False,'pdf.fonttype':42})
colors=['#0F2A43','#087968','#B65B33','#6B7280'];xs=list(range(1,57))
def plot(name,title,series,ylabel='UF',bars=False):
 f,a=plt.subplots(figsize=(6.2,4.1),constrained_layout=True)
 for i,(label,values) in enumerate(series):
  if bars:a.bar(xs,[x/40000 for x in values],label=label,color=colors[i],alpha=.9)
  else:a.plot(xs,[x/40000 for x in values],label=label,color=colors[i],linewidth=1.8)
 a.axhline(0,color='#475569',linewidth=.8);a.grid(axis='y',alpha=.18);a.set(xlabel='Mes contractual',ylabel=ylabel,title=title);a.set_xticks([1,6,9,12,16,21,32,44,56])
 a.ticklabel_format(style='plain',axis='y');a.legend(loc='upper left',fontsize=11)
 f.savefig(fig/(name+'.pdf'));f.savefig(O/'revision'/(name+'.png'),dpi=130);plt.close(f)
plot('curva-s','Curva S de la base corregida',[(n,[v('Curva S',f'{c}{r}') for r in range(2,58)]) for n,c in [('Costo con intereses','B'),('Facturación','C'),('Caja financiada neta','D')]])
plot('egresos','Egresos mensuales del proyecto',[('Costo neto',[v('Costos',f'K{r}') for r in range(2,58)])],bars=True)
plot('caja','Liquidez y atraso de H5',[
 ('Base (tesorería)',[v('Flujo de Caja',f'W{r}') for r in range(2,58)]),
 ('H5 M14 + reserva, sin facilidad',[v('Escenarios corregidos',f'S{r}') for r in range(116,172)]),
 ('H5 M14 + reserva, con facilidad',[v('Escenarios corregidos',f'S{r}') for r in range(173,229)])])
f,a=plt.subplots(figsize=(6.2,4.1),constrained_layout=True)
a.bar(xs,[v('Flujo de Caja',f'AB{r}')/40000 for r in range(2,58)],label='Banco',color=colors[0]);a.bar(xs,[v('Flujo de Caja',f'AC{r}')/40000 for r in range(2,58)],bottom=[v('Flujo de Caja',f'AB{r}')/40000 for r in range(2,58)],label='Socios',color=colors[1]);a.bar(xs,[-v('Flujo de Caja',f'U{r}')/40000 for r in range(2,58)],label='Amortización bancaria',color=colors[2]);a.axhline(0,color='#475569');a.set(xlabel='Mes contractual',ylabel='UF',title='Desembolso, aporte y devolución');a.set_xticks([1,9,12,16,21,56]);a.legend(fontsize=11);f.savefig(fig/'financiamiento.pdf');f.savefig(O/'revision/financiamiento.png',dpi=130);plt.close(f)
tabla_resumen='\n'.join(f'{t} & {uf(x)} \\\\' for t,x in [('Costo neto',m['costo_clp']),('Venta neta',m['venta_clp']),('VAN',m['van_clp']),('Capital inicial',m['capital_inicial_clp']),('Caja mínima de tesorería',m['caja_minima_tesoreria'])])
scenario_rows='\n'.join(f'{esc(v("Sensibilidad",f"A{r}"))} & {uf(v("Sensibilidad",f"G{r}"))} & M{entero(v("Sensibilidad",f"H{r}"))} & {uf(v("Sensibilidad",f"I{r}"))} & {uf(v("Sensibilidad",f"S{r}"))} \\\\' for r in range(2,9))
soporte_rows='\n'.join(f'{t} & {uf(v("Personal",f"D{r}"))} \\\\' for t,r in [('M21',22),('M25--M32',26),('M33--M44',34),('M45--M56',46)])
inversiones='\n'.join(f'{i} & {name} & {uf(v("Innovaciones",f"C{i+1}"))} & {uf(v("Innovaciones",f"D{i+1}"))} \\\\' for i,name in enumerate(['Expediente verificable','Patio','Acople y registro térmico','Comodato y sobreestadías','Prevención de fatiga'],1))
adjudicados=[(int(v('Flujo de Caja',f'A{r}')),v('Flujo de Caja',f'U{r}')) for r in range(2,59) if v('Flujo de Caja',f'U{r}')>0]
mes_pago=max(x[0] for x in adjudicados);picos=sorted(((int(v('Costos',f'A{r}')),v('Costos',f'K{r}')) for r in range(2,58)),key=lambda x:-x[1])[:3]
contenido=r'''\begin{resumenApertura}
La oferta integra inversión, instalación, personal y continuidad durante los 56 meses contractuales. El presupuesto sustituye el montaje físico posterior al piloto por un servicio por lote y diferencia cobertura fija y carga variable de soporte. La base dispone de capital antes de sus egresos y reserva la línea para contingencias.
\begin{recibe}
\item Costos, precio y liquidez calculados desde un único modelo mensual, con trazabilidad de cantidades, horas, tasas y escenarios.
\end{recibe}
\end{resumenApertura}

\section{Proveedores clave de la solución}\label{sec:eco-proveedores}
La \tabref{eco-proveedores} identifica las familias de suministro y su función. Los importes son un presupuesto de oferta. La recepción del servicio requiere confirmar alcance, compatibilidad, disponibilidad y condiciones de pago de cada orden. No se presentan estimaciones como cotizaciones recibidas.
\begin{tabla}[ancho=completo]{Proveedores y criterio de contratación}{eco-proveedores}{L{30mm} L{38mm} X}
Proveedor o servicio & Alcance & Criterio \\ \midrule
Microsoft / canal CSP & Azure y recuperación & Región, disponibilidad y enlace autorizados por la arquitectura \\
Dell, Fortinet y AAEON & Cómputo y red & Capacidad, soporte y entrega antes de H3 \\
iWave, Teltonika y Technoton & Equipo a bordo y sensores & Compatibilidad, garantía y prueba en terminal \\
GitLab y SonarSource & Licencias & Cobertura de desarrollo y calidad, sin duplicar nube \\
Ground Control y operador móvil & Satélite y LTE & Activación por equipo, cobertura y costo recurrente \\
Servicio externo de montaje & 172 kits en cinco terminales & Mano de obra física por lote, recepción y término del servicio \\
\end{tabla}
La compra de campo y red de cargo de Curimón es informativa y permanece fuera de los egresos de audIT. La instalación, integración, infraestructura de audIT y servicios contratados sí forman parte del presupuesto.

\section{Adquisiciones clave o relevantes}\label{sec:eco-adquisiciones}
La \tabref{eco-calendario} relaciona el gasto con habilitación, montaje y aceptación. Los pagos no se distribuyen para suavizar la curva: siguen la compra, ejecución o mes de servicio. Los hitos conservan el calendario de \form{E-25}{74} y su aceptación requiere acta de la contraparte conforme al \art{18}{13}.
\begin{tabla}[ancho=completo]{Calendario de adquisiciones y despliegue}{eco-calendario}{L{23mm} L{36mm} X}
Meses & Actividad y pagador & Criterio de costo y recepción \\ \midrule
M1--M4 & Infraestructura, audIT & Grupo electrógeno, sala, gabinetes y cómputo antes de H3. Energía y pruebas de combustible incluidas conservadoramente en audIT \\
M5--M6 & Hardware, Curimón & Lote, unidades de prueba, tarjetas y sensores. Hoja informativa independiente \\
M6 & Piloto, audIT & Diez kits y 50 horas de referencia dentro del total de 182. Medición y recepción antes de liberar el servicio externo \\
M7--M9 & Montaje externo, audIT & Lotes de 60, 60 y 52 kits. Factura y pago tras recepción de cada lote. El servicio termina en M9 \\
M7--M9 & Balizas y lectores, audIT & 210 balizas, 52,5 horas, más cinco lectores a dos horas de referencia. Las 21 balizas de stock no se montan al alta inicial \\
M10--M12 & Pruebas y certificación & Capacidad de QA y seguridad, incluida preparación de pruebas. H4 y H5 conservan sus meses \\
M13--M20 & Marcha blanca y estabilización & Roles concurrentes de ambas etapas y soporte reforzado de E1 después de H7. Desmovilización por cierre de actividad \\
M21--M56 & Operación & Cobertura fija y variable por tramo. Reposiciones, licencias y fabricante conservan su calendario propio \\
\end{tabla}
La ventana física exige la visita normal del camión y consentimiento del dueño cuando corresponda. El montaje se limita a terminales y se evita el congelamiento diciembre--abril, sin ampliar la inmovilización no costeada, conforme a las restricciones 3, 5 y 10 del Caso, capítulo 10, pp.~23--24. Los importes y las horas se relacionan en las hojas Instalación por lote y Dotación por perfil.

\subsection{Servicio de instalación y trabajo que conserva audIT}\label{sec:eco-instalacion}
El piloto permanece interno. Los otros 172 montajes sustituyen 401 horas y 20 minutos de ejecución física interna. Se conserva el trabajo de banco, configuración, integración, analista, QA y recepción. La reducción se aplica a las horas del técnico de campo, nunca al equipo completo ni al salario de un recurso que deba seguir dedicado a otras actividades.
El servicio se presupuesta en \montoPartida{montaje-neto} netos equivalentes. Usa 140 minutos por kit, el costo de referencia del técnico, un recargo de coordinación e insumos y una provisión de traslado por terminal regional y lote. El costo interno sustituido es \montoPartida{montaje-evitado}. La diferencia paga el alcance del proveedor y su logística, no representa un ahorro ficticio.
La contratación queda sujeta a autorización previa escrita y al límite agregado del 40\,\% del valor contractual del \art{73}{38}. audIT conserva la responsabilidad, el núcleo de aplicaciones, credenciales y datos. El presupuesto de servicio no equivale a una autorización ya obtenida.

\section{Curva S del proyecto}\label{sec:eco-curva-s}
La \figref{eco-curva} presenta las tres series mensuales exigidas para M1--M56: costo acumulado con financiamiento, facturación acumulada y caja financiada neta de IVA. La tesorería con IVA se distingue en el análisis de liquidez. El principal del préstamo no se contabiliza como costo del proyecto.
\figura{../../Informe-3/correccion-final/economico/figuras/curva-s.pdf}{Curva S mensual en UF. Fuente: planilla, Curva S y Gráficos UF.}{eco-curva}
La \figref{eco-egresos} muestra los desembolsos por mes. Los mayores picos ocurren en @PICOS@ y se explican por capacidad concurrente de implementación, brechas de perfiles y adquisiciones del mes. La contratación se calcula desde horas y tarifas, no desde una pendiente acumulada prefijada.
\figura{../../Informe-3/correccion-final/economico/figuras/egresos.pdf}{Costos netos mensuales en UF. Fuente: Costos, columnas A y K.}{eco-egresos}
Los quiebres se deben a hitos de trabajo y a cambios de dotación. La demanda D3 se compara por perfil con la capacidad base del T-15 y se presupuesta el exceso una sola vez. El trabajo atribuido a innovaciones se identifica dentro de esas horas y no se vuelve a agregar al egreso.

\section{Análisis de costos de la solución}\label{sec:eco-costos}
La \tabref{eco-resumen} resume las magnitudes principales en UF del E-24. El horizonte corresponde a Etapa 1 M1--M16, Etapa 2 M13--M21 y 36 servicios operativos M21--M56. Los cierres de integración y datos que llegan hasta M24 se identifican y se pagan dentro del refuerzo temporal.
\begin{tabla}{Magnitudes principales, UF netas}{eco-resumen}{L{72mm} R{40mm}}
Concepto & UF \\ \midrule
@RESUMEN@
\end{tabla}
El precio se recalcula desde los costos corregidos para mantener un margen EBITDA sobre ingresos netos de @MARGEN@\,\%, inferior al máximo del 20\,\% de las Aclaraciones, sección 7. Los valores de utilidad sobre costo de la hoja Resumen del mandante se conservan con su rótulo y se distinguen de ese margen sobre ingresos.

\subsection{Personal, overhead y gastos de continuidad}\label{sec:eco-personal}
La implementación parte de las capacidades de referencia de 14, 24, 30, 33, 37, 30 y 26 FTE por tramo del T-15, a 160 horas por FTE. La hoja Tarifas por perfil declara el costo horario y su equivalencia con E-26. Dotación por perfil calcula horas base, demanda D3, refuerzo, horas sustituidas y costo. Los refuerzos son cupos de contratación presupuestados para cerrar una brecha, no disponibilidad de planta supuesta.
Los costos D4, licencias, calidad, primas, notaría y custodia conservan su fuente y mes. Se incorpora una provisión empresarial de overhead del 2\,\% del costo de personal, separada de primas y gastos legales. Energía y combustible de pruebas se incluyen a cargo de audIT como hipótesis conservadora. El IVA de compras y el IVA de cobros se muestran aparte, sin reconocer créditos fiscales sin respaldo.

\subsection{Soporte reforzado y reducción por madurez}\label{sec:eco-soporte}
El soporte de E1 en M16--M20 usa capacidad reservada de software, campo, QA y SRE de la implementación. Desde M21 se separan mesa 24\,\(\times\)\,7, plataforma, ciclo de vida y mantención evolutiva. Se conservan seis agentes L1 y una reserva mensual de suplencia, plataforma y guardia, y dos perfiles de campo. La carga variable de evolución se reduce al 75\,\%, 50\,\% y 25\,\% de su nivel inicial en M25, M33 y M45.
La \tabref{eco-soporte} muestra el efecto por tramo. M21--M24 incluye Datos, QA, Arquitectura y Frontend para los cierres que siguen a implementación. El contrato estimado de fabricante D4 permanece en proveedores y no se reduce por esta curva.
\begin{tabla}{Costo mensual de personal de operación, UF}{eco-soporte}{L{66mm} R{42mm}}
Tramo & UF por mes \\ \midrule
@SOPORTE@
\end{tabla}
La reducción requiere dos meses sin incidentes P1 atribuibles al sistema, backlog menor a diez y demanda que quepa en las horas contratadas. Si no se cumplen, se mantiene el factor anterior y se recalcula el costo. No se interpreta menor demanda como permiso para eliminar cobertura crítica. Respuesta y resolución son 15 minutos y cuatro horas, respectivamente, conforme al \art{78.2}{40}. Una recuperación de 225 minutos puede cumplir resolución, pero no acredita por sí misma 99,9\,\% de disponibilidad: la continuidad debe sostenerse mediante conmutación y su ensayo previo a H5.

\subsection{Cuadros formales de costos y venta}\label{sec:eco-venta}
La \tabref{eco-costos-formales} concilia las fases con la hoja Resumen. Las cifras de costo no incorporan IVA ni el principal de la deuda. La garantía de correcto funcionamiento se atribuye a implementación aunque el pago ocurra en M21.
\tablaMontos*{Costos netos por fase y total}{eco-costos-formales}{costo-impl,costo-op,costo}
La \tabref{eco-ventas-formales} presenta neto, IVA y total en las monedas del E-24. La fase de implementación usa los doce hitos del E-25, con reparto 60/40. Los 36 servicios operativos se facturan M21--M56 y se cobran M22--M57. No se anticipa venta de operación en implementación.
\tablaMontos{Venta por fase}{eco-ventas-formales}{implementacion,operacion}
El cobro de M57 es \montoPartida{cobro-m57}. Se presenta como conciliación de la última cuenta por cobrar y se excluye del VAN base de M1--M56. El indicador con M57 permite ver el efecto de esa cola sin ocultarla.

\section{VAN y TIR de la solución}\label{sec:eco-indicadores}
La Fila A descuenta cobros netos menos costos del proyecto, sin deuda, aportes ni amortización. M0 es cero y los flujos se descuentan desde M1. La tasa mensual antes de impuestos es @TASA@\,\%: 80\,\% de deuda al 0,9\,\% mensual y 20\,\% de capital propio al equivalente mensual de un 20\,\% efectivo anual supuesto. El costo de socios es una exigencia de retorno de presupuesto, no un dato impuesto por E-24.
El VAN base es \montoPartida{van} y la TIR mensual es @TIR@\,\%. Se comprobó la raíz sobre la Fila A. En escenarios con cambios sucesivos de signo pueden existir varias TIR: la hoja Sensibilidad identifica la semilla utilizada y el análisis prioriza VAN y liquidez en vez de elegir la raíz que parezca más favorable. La venta nominal de equilibrio a VAN cero, conservando costos y calendario de cobros, es \montoPartida{equilibrio}.

\subsection{Financiamiento y caja}\label{sec:eco-financiamiento}
La base dispone de \montoPartida{capital} en M1. Se compone de un préstamo y del aporte de socios, según el reparto 80/20 del E-24.
\begin{itemize}
\item Préstamo inicial: \montoPartida{banco}.
\item Aporte de socios: \montoPartida{socios}.
\end{itemize}
Se usa 0,9\,\% mensual sobre saldo bancario de apertura y una comisión presupuestada de \montoPartida{comision}. La devolución del banco se realiza en M@PAGO@, desde el inicio de amortización previsto en M21, conservando el piso de \montoPartida{piso}. No se modelan retiros ni restitución a socios.
El capital del corte de referencia anterior era \montoPartida{capital-anterior}. Se redimensiona por el calendario corregido y por la cobertura de pagos antes de cobros, en vez de conservar el monto de la versión anterior sin comprobar su suficiencia.
La \figref{eco-financiacion} muestra entradas y devolución. El capital se dimensiona con la cota conservadora que paga los egresos mensuales antes de recibir cobros, además de comprobar cierres netos y de tesorería. Esto evita afirmar cobertura diaria basándose solo en un saldo mensual o en fechas aún no pactadas.
\figura{../../Informe-3/correccion-final/economico/figuras/financiamiento.pdf}{Crédito, aportes y amortización, UF. Fuente: Flujo de Caja AB:AC y U.}{eco-financiacion}
La base mantiene cero giros y cero saldo de línea. La cota anterior a cobros es \montoPartida{cota}. La disponibilidad, monto neto, comisión y vencimientos forman parte de las condiciones financieras de esta oferta. Se verifica su compatibilidad antes de comprometer órdenes. No se presenta un supuesto presupuestario como un desembolso ya realizado.

\subsection{Atrasos y contingencia}\label{sec:eco-estres}
La \tabref{eco-escenarios} compara las pruebas a precio fijo. El atraso mueve el cobro de H5 y su IVA cobrado, manteniendo factura en M12. Si se desplaza la aceptación, debe revisarse también la facturación conforme al Artículo 18. La reserva D4 de \montoPartida{reserva} se prueba con desembolso M12 y anticipado M9. La facilidad adicional presupuestada de \montoPartida{puente} se estructura 80/20 y se dispone en el mes que requiere la reserva, antes de sus egresos. La línea tiene un máximo de 1.250 UF y tasa del 3\,\% mensual.
\begin{tabla}[ancho=completo,fuente=condensada]{Liquidez de los escenarios, UF de tesorería}{eco-escenarios}{X R{25mm} C{14mm} R{25mm} R{25mm}}
Escenario & Caja mínima & Mes & Línea máxima & Cota antes de cobros \\ \midrule
@ESCENARIOS@
\end{tabla}
Las filas sin facilidad muestran la exposición antes de cubrirla. El atraso simple conserva cierres mensuales positivos, pero su cota antes de cobros es negativa: requiere anticipar la facilidad o acordar el orden de pagos. El atraso con reserva sin facilidad presenta además déficit mensual, aun agotando la línea. Solo las dos pruebas con facilidad verifican el piso y la cota antes de cobros, con devolución desde M16. Los choques de costo y de cobros tampoco cubren esa cota y exigen redimensionar fondos si ocurren; no se declaran cubiertos por el cierre mensual. La línea no sostiene el caso base. Intereses, pagos y saldos se concilian mes a mes en Escenarios corregidos.
La \figref{eco-caja} compara la base y los atrasos. Los valores de tesorería incluyen el efecto de IVA conservador, mientras la tercera serie de la Curva S conserva la vista neta exigida por las Aclaraciones, nota 7.4. Ambas se reconcilian con el IVA acumulado.
\figura{../../Informe-3/correccion-final/economico/figuras/caja.pdf}{Caja, referencia cero y atraso de H5. Fuente: Flujo de Caja y Escenarios corregidos.}{eco-caja}
No se suavizan déficits ni se modifican precios al atrasar un pago. Las contingencias de costo y cobro conservan resultados propios y su condición de financiamiento adicional.

\section{Valorización de las cinco innovaciones}\label{sec:eco-innovaciones}
La \tabref{eco-innovaciones} distingue personal atribuido dentro de la nómina y egresos directos. El personal se calcula desde las horas D3, con 120 horas adicionales de integración de INN3 y el desarrollo y soporte de INN5. Es una vista de atribución, no otro costo para sumar al proyecto.
\begin{tabla}[ancho=completo,fuente=condensada]{Costo atribuido y egresos de innovaciones, UF}{eco-innovaciones}{C{10mm} X R{35mm} R{35mm}}
ID & Innovación & Personal atribuido & Egreso directo adicional \\ \midrule
@INNOVACIONES@
\end{tabla}
INN1 incorpora firma automatizada en proveedores. INN2 se evalúa por visitas, duración de atenciones y preparación evitada en patio. INN3 distingue verificación de acople y registro térmico del kilometraje obligatorio y mantiene las balizas y lectores en el inventario del mandante. INN4 usa 34 comodatos incluidos dentro de los 182 montajes, sin sumar una nueva instalación base. INN5 conserva desarrollo, talleres, calibración y soporte, con el catálogo de paradores separado del mérito innovador.
Los beneficios de Curimón no son ingresos de audIT. La base reconoce cero beneficio monetario incremental cuando faltan línea base, atribución o ahorro efectivo demostrado. La hoja Beneficios Curimón muestra por separado una hipótesis de capacidad liberada por INN1 y el recupero bruto referencial de INN4 por \montoPartida{recupero} en 36 meses. Este último requiere restar costos y repartir con transportistas antes de tratarlo como beneficio neto.
Antes de H5 se levantan, por innovación, volumen, adopción, costo por evento y resultado de comparación. INN2 mide minutos de preparación, INN3 eventos térmicos y acoples, e INN5 consumo y siniestralidad con denominador de viajes. Las estimaciones no se presentan como observaciones históricas ni se imputan dos veces los mismos minutos o pérdidas evitadas.

\section{Planilla de cálculo}\label{sec:eco-planilla}
La planilla adjunta conserva filas, rótulos y orden del Resumen del mandante. Sus totales se enlazan al modelo actualizado. Las nuevas hojas contienen entradas, fórmulas y controles explícitos. Los resultados se recalculan al cambiar capital, tarifa o mes de cobro. La protección evita alterar accidentalmente fórmulas y deja editables los parámetros de escenario.
La hoja Control de entrega concilia costos y venta con Resumen y Cuadro maestro, doce hitos, 36 facturaciones, kits, deuda final y ausencia de línea en base. Los escenarios mantienen los mismos precios para sus pruebas. El hardware que compra Curimón permanece informativo y fuera del flujo de audIT, conforme a Aclaraciones, sección 9.

\section{Demostración interactiva}\label{sec:eco-demo}
El avance está disponible en \href{https://carlosabarza.github.io/PaginaAudIT/}{el portal de audIT}. La ruta de revisión es Portal Clientes, Simulador Operativo en Vivo. Al activar pérdida de cobertura, la interfaz muestra paquetes en el búfer. Al restablecerla, muestra reconciliación. Se comprobó esa navegación para preparar esta entrega.
La demostración representa comportamiento de interfaz. Sus contadores, tiempos y estados no prueban el desempeño de una infraestructura productiva ni sustituyen la aceptación de T-17. El recorrido de exposición reserva dos minutos para mostrar desconexión y reconexión, dentro de una presentación total prevista de quince minutos.

\section*{Referencias}
El análisis se apoya en FEP01, Formularios T-22, E-21, E-24, E-25 y E-26, Artículos 18, 46, 57.2, 73 y 78.2; las Aclaraciones del Informe 3; el Caso, numeral 14.1 y capítulo 10; y las estimaciones técnicas de EDT, T-14/T-15 y presupuestos de software, datos e infraestructura incorporados al modelo. Las fuentes de precios, moneda, pagador y mes se conservan en las hojas de entrada. Los nuevos parámetros sin cotización se identifican como supuestos de presupuesto.

\section*{Declaración de uso de IA}
Se utilizó Codex para organizar la trazabilidad, generar fórmulas y documentos y reproducir cálculos. El nivel de asistencia en texto y gráficos es alto. Las pruebas automáticas registran comprobaciones numéricas y de formato, sin sustituir la revisión sustantiva del proponente. La validación de negocio y la aprobación para presentación corresponden a PMO y QA, y se registran en A-6 por sus responsables.
\begin{tabla}[ancho=completo,fuente=condensada,numerada=false]{Uso de IA y control de la propuesta}{eco-ia}{L{27mm} L{18mm} X L{18mm} L{18mm} L{35mm}}
Secciones & Herramienta & Finalidad & Texto & Gráficos & Revisión humana \\ \midrule
1--2 & Codex & Proveedores, calendario y montaje & Alto & Alto & PMO e infraestructura: validar los supuestos de contratación \\
3--5 & Codex & Modelo, cálculos, gráficos y escenarios & Alto & Alto & PMO y QA: contrastar parámetros, decisiones y defensa de resultados \\
6--8 y anexos & Codex & Trazabilidad, innovaciones y exposición & Alto & Alto & QA y responsables de cada componente: aceptar el alcance de lo presentado \\
\end{tabla}
La declaración identifica asistencia y responsables de validación, sin atribuir actas, mediciones o firmas que no consten en el expediente.
'''
reemplazos={'RESUMEN':tabla_resumen,'SOPORTE':soporte_rows,'ESCENARIOS':scenario_rows,'INNOVACIONES':inversiones,
 'MARGEN':num(m['margen']*100),'TASA':num(m['tasa_mensual']*100,7),'TIR':num(m['tir_mensual']*100,4),'PAGO':str(mes_pago),
 'PICOS':', '.join('M'+str(p[0]) for p in picos)}
for k,x in reemplazos.items():contenido=contenido.replace('@'+k+'@',x)
# TeX Live local antecede al cambio de contador de longtable de 2025.
# Se numeran aquí las tablas de este documento, sin modificar la clase común.
contenido=contenido.replace(r'\begin{tabla}',r'\refstepcounter{table}'+'\n'+r'\begin{tabla}').replace(r'\tablaMontos',r'\refstepcounter{table}'+'\n'+r'\tablaMontos')
contenido=contenido.replace(r'\figura{',r'\figura[lugar=H]{')
(eco/'costos-venta/contenido.tex').write_text(contenido)
# El anexo conserva estados técnicos del último corte disponible sin declararlos cerrados por esta revisión económica.
obs=(D/'observaciones-informe2-origen.tex').read_text()
correcciones=[('PROF-01','La exposición usa cifras extensas y monedas mezcladas.','Cuadros y cuatro gráficos principales en UF, conservando las salidas formales en CLP, UF y USD.','sec:eco-costos'),
 ('PROF-02','La base usa la línea para sostener M9.','Se dimensiona capital inicial con cierres positivos, cero línea y cota de pagos antes de cobros. El atraso se prueba a precio fijo.','sec:eco-financiamiento'),
 ('PROF-03','No se distinguen compras, instalación y puesta en producción.','Se vinculan calendario, perfiles y servicio por lote; se incorpora gráfico de egresos mensuales.','sec:eco-curva-s'),
 ('PROF-04','La carga de soporte no disminuye con la madurez.','Se separa cobertura fija, refuerzo temporal y demanda variable, con factores y condiciones medibles por tramo.','sec:eco-soporte'),
 ('PROF-05','Préstamo, aporte y devolución no se identifican visualmente.','Se explicitan capital, tasa, comisión y amortizaciones, con gráfico propio y conciliación de saldos.','sec:eco-financiamiento'),
 ('PROF-06','Se mantiene personal operativo de instalación sin término visible.','Se externalizan 172 montajes después del piloto, se retiran horas físicas sustituidas y se cierra el servicio por lote.','sec:eco-instalacion')]
filas='\n\\grupoObservaciones{Revisión económica}\n'
for ident,a,r,s in correcciones:filas+=f'\\observacion[sub=E]{{{ident}}}{{{ident}. {a}}}{{{r}}}{{\\verSeccionFolio{{{s}}}. Estado: incorporada en el modelo económico y comprobada por cálculo}}\n'
obs=obs.replace(r'\end{tablaObservaciones}',filas+r'\end{tablaObservaciones}')
# El formato reserva 7mm al número. Los códigos alfanuméricos se conservan
# en la observación y se usa numeración correlativa en la primera columna.
contador=[0]
def numerar(match):
 contador[0]+=1
 return match[1]+'{'+str(contador[0])+'}'
obs=re.sub(r'(\\observacion(?:\[[^\]]*\])?)\{[^}]*\}',numerar,obs)
obs=('Las primeras 68 filas conservan el estado documentado de las observaciones técnicas del Informe 2. Esta revisión económica no las declara cerradas. Las seis últimas filas identifican los cambios incorporados al presupuesto, la liquidez y la exposición del Informe 3.\\par\\smallskip\n'+obs)
(D/'observaciones.tex').write_text(obs)
driver=r'''\def\RaizEconomico{../../Informe-3/correccion-final/economico}
\def\ArchivoObservaciones{../../Informe-3/correccion-final/observaciones.tex}
\def\NombreArchivo{INFORME3_AUDIT_COSTOS_VENTA_20261114}
\def\ArchivoActual{INFORME3_AUDIT_COSTOS_VENTA_20261114}
\def\FolioInicialExterno{1}
\documentclass{audit-oferta}
\input{configuracion/metadatos}
\input{configuracion/instancia}
\input{configuracion/subdocumentos}
\input{configuracion/economico}
\usepackage{float}
\NewCommandCopy\montoPartidaOriginal\montoPartida
\RenewDocumentCommand\montoPartida{m}{\begingroup\renewcommand\enspace{\hspace{.5em}\allowbreak}\montoPartidaOriginal{#1}\endgroup}
\AplicarInstancia{informe3}
\Version{3.0}
\FechaEntrega{2026-11-14}
\FechaTipoCambio{Valores de referencia del Formulario E-24}
\begin{document}
\DocumentoEconomico{costos}
\end{document}
'''
(D/'documento.tex').write_text(driver)
print('Contenido, partidas, cuatro gráficos y anexo generados desde el Excel recalculado.')
print('TIR base:',m['raices_tir_base'],'; escenarios:',m['raices_tir_escenarios'])
