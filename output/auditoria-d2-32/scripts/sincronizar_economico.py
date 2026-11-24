"""Actualiza el documento económico activo desde resultados 3.2 congelados."""
from pathlib import Path
import json
R=Path(__file__).resolve().parents[2]/'tmp/cierre-entrega-3'
B=R/'recursos/Formato-Oferta-audIT'
D=json.loads((B/'economico/datos/respaldo-3.2.json').read_text(encoding='utf-8'))
def num(v,d=2):return f'{v:,.{d}f}'.replace(',','@').replace('.',',').replace('@','.')
rows=[]
for s in D['sensibilidad']:
    tir=s['TIR mensual'];tir=num(tir*100,2)+r'\,\%' if isinstance(tir,(float,int)) else 'Revisar raíces'
    rows.append(' & '.join([s['Escenario'].replace('%',r'\%'),num(s['VAN Fila A CLP']/1e6),tir,num(s['Déficit residual CLP']/1e6)])+r' \\')
texto=r'''\begin{resumenApertura}
El documento concilia costo, precio y liquidez de la configuración ofertada para Transportes Curimón.
La evaluación conserva la base de cálculo 3.2 y separa el resultado del contrato del financiamiento.
\begin{recibe}
\item Costos y precios por fase, adquisiciones, sensibilidad y tratamiento de innovaciones trazados a la planilla.
\end{recibe}
\end{resumenApertura}

\section{Proveedores y adquisiciones}\label{sec:eco-proveedores}

La \tabref{eco-proveedores} relaciona las adquisiciones con su pagador y fecha de uso. Las referencias
de presupuesto no equivalen a una cotización aceptada ni a una recepción efectiva.

\begin{tabla}[ancho=completo]{Proveedores y condiciones de adquisición}{eco-proveedores}{L{32mm} L{21mm} L{25mm} X}
Proveedor o servicio & Pagador & Ventana & Condición de puesta en servicio \\ \midrule
Microsoft Azure por CSP & audIT & M1--M56 & Regiones Chile Central y Brazil South; circuito privado sujeto a factibilidad. \\
Dell y equipamiento de sala & audIT & M1--M6 & Energía, clima, extinción y recepción antes de H3. \\
Fortinet y hardware de campo & Curimón según T-11 & M5--M6 & Recepción y homologación del lote antes de montaje. \\
iWave, Teltonika y Technoton & Curimón según T-11 & Piloto M6, lotes M7--M9 & 182 kits iniciales, 210 balizas, cinco lectores; el stock de reposición no es montaje inicial. \\
Montaje por terminal & audIT & M7--M9 & 172 montajes externos; audIT conserva banco, recepción y prueba. \\
Ground Control / Iridium y LTE & audIT & Activación por unidad & Cobertura medida y activación solo al recibir el equipo. \\
GitLab y SonarSource & audIT & Según licencias & Cobertura comercial y condiciones de soporte confirmadas antes de usar. \\
Servicio de campo y soporte fabricante & audIT & Campo desde M19; soporte M13 & Visitas y rondas por orden; fabricantes con pagos anticipados anuales. \\
\end{tabla}

El proveedor masivo termina el montaje inicial en M9; los diez pilotos de M6 ya forman parte de
los 182 equipos. Si falta adhesión, stock o ventana se registra una desviación y se actualizan
instalación, activación y caja; no se da por ejecutado el escenario presupuestado.

\section{Costo y precio por fase}\label{sec:eco-costos}

La \tabref{eco-maestro} muestra los costos netos conciliados. Personal incluye los refuerzos de
producción y cierre de M21--M24; no se suman otra vez como incrementos. Los servicios externos
de montaje y campo se distinguen de la contratación interna. El hardware adquirido por el
mandante se informa separado de los egresos de audIT.

\tablaMontos*{Costo neto por fase}{eco-maestro}{costo-fase-implementacion,costo-fase-operacion,costo-proyecto}

La \tabref{eco-venta} presenta el precio por fase. El margen objetivo consolidado sobre ventas
es 18,50\,\%; la utilidad sobre costo que conserva el Resumen de la plantilla equivale a 22,70\,\%.

\tablaMontos{Precio neto ofertado por fase}{eco-venta}{implementacion,operacion}

La implementación se factura en los doce hitos E-25. La operación tiene 36 servicios M21--M56,
cobrados M22--M57. La última mensualidad es \montoPartida{cobro-m57}. La comisión de garantía
de funcionamiento se atribuye a implementación por objeto aun cuando se pague en M21.

\section{Curva contractual y solvencia}\label{sec:eco-curva-s}

La \figref{eco-curva-s} compara costos acumulados con intereses y facturación acumulada.
La \figref{eco-solvencia32} muestra por separado la caja financiada: es un saldo de tesorería,
no una tercera serie de avance contractual. La amortización del principal afecta la caja y no
se vuelve a contar como costo. Las dos figuras cubren M1--M56; M57 se concilia como cola de cobro.

\figura{economico/costos-venta/curva-s.pdf}{Costo con intereses y facturación acumulada}{eco-curva-s}
\figura{economico/costos-venta/solvencia-3.2.pdf}{Saldo de caja financiada del caso base}{eco-solvencia32}

\section{Evaluación financiera}\label{sec:eco-van}

El VAN utiliza los flujos de la Fila A en M1--M56, con M0 igual a cero y tasa mensual 1,0261894\,\%.
La tasa pondera deuda al 0,9\,\% mensual y capital propio al 20\,\% efectivo anual supuesto.
El VAN es \montoPartida{van}; la TIR mensual del caso base es '''+num(D['tir']*100,4)+r'''\,\%.
La cola de M57 se informa aparte. La recuperación descontada sostenida ocurre en M'''+str(D['recuperacion'])+r'''.

La \tabref{eco-sensibilidad} conserva los escenarios calculados en la planilla. El déficit residual
mide faltante antes de cobros bajo el orden conservador de pagos; una caja mensual de cierre
positiva no demuestra suficiencia intramensual. Las TIR sin raíz convergente se rotulan para revisión.

\begin{tabla}[ancho=completo,fuente=condensada]{Sensibilidad y liquidez del escenario}{eco-sensibilidad}{X R{28mm} L{29mm} R{29mm}}
Escenario & VAN millones CLP & TIR mensual & Déficit millones CLP \\ \midrule
'''+ '\n'.join(rows)+r'''
\end{tabla}

El equilibrio nominal es \montoPartida{equilibrio-nominal}; la venta que lleva el VAN a cero
con escala uniforme y calendario base es \montoPartida{equilibrio-van}. Son umbrales distintos.
La facilidad contingente es \montoPartida{capital-adicional-h5}, adicional y condicionada, con
desembolso previsto en M12. La base contempla capital inicial de 18.250 UF, 80\,\% bancario y
20\,\% propio; el crédito se prepaga en M17 y M18. La disponibilidad, instrumentos y comisiones
exigen respaldo antes de contratar. No se reutilizan las sensibilidades de caja de versiones anteriores.

\section{Innovaciones y capacidad}\label{sec:eco-innovaciones}

La \tabref{eco-innovaciones} separa atribución de personal, egreso directo y beneficios de Curimón.
Las horas atribuidas pertenecen a la nómina existente y no constituyen un segundo gasto.

\begin{tabla}[ancho=completo]{Tratamiento presupuestario de las innovaciones}{eco-innovaciones}{L{39mm} X X}
Innovación & Imputación & Evidencia de resultado \\ \midrule
1. Expediente verificable & Firma \montoPartida{firma-inn1}; trabajo dentro de nómina. & Medir expedientes y minutos evitados sin duplicar recuperos de INN-4. \\
2. Programación de patio & Desarrollo \montoPartida{innovacion-2-inversion}; operación \montoPartida{innovacion-2-costo} atribuidos. & Comparar preparación y primer intento contra línea base. \\
3. Acople y registro térmico & Desarrollo \montoPartida{innovacion-3-inversion}; operación \montoPartida{innovacion-3-costo} atribuidos. & El kilometraje es alcance base; medir acople y temperatura por separado. \\
4. Comodato y sobreestadías & 34 comodatos ya incluidos en 182 kits; nuevas altas requieren capacidad y pagador. & Recupero bruto de referencia \montoPartida{recupero-inn4}; no es cobro de audIT. \\
5. Prevención de fatiga & Trabajo dentro de nómina; talleres y calibración en Otros confirmados. & Medir resultado incremental y adopción; IVA y ejecutores a confirmar. \\
\end{tabla}

El caso base no incorpora beneficios hipotéticos de Curimón en los cobros de audIT. La atribución
mensual de cada innovación se verifica contra la capacidad disponible antes de reservar una tarea.

\section{Planilla y control de versión}\label{sec:eco-planilla}

La planilla entregada 3.2 se conserva como evidencia. La copia vigente de conciliación corrige
únicamente descripciones heredadas de campo y precio; mantiene idénticos números, fórmulas y
resultados almacenados. El recálculo en Excel debe contrastarse con la referencia antes de liberar
un cambio de cálculo. Los documentos económicos anteriores son históricos y no se adjuntan a
este paquete como respaldo vigente.
'''
(B/'economico/costos-venta/contenido.tex').write_text(texto,encoding='utf-8')
print('Documento económico activo sincronizado con indicadores, caja y escenario 3.2.')
