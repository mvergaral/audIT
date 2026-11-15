import fs from 'node:fs/promises';
import {FileBlob,SpreadsheetFile} from '@oai/artifact-tool';
import {fileURLToPath} from 'node:url';
const D=fileURLToPath(new URL('..',import.meta.url)).replace(/\/$/,'');
const O=D+'/../../outputs/informe3-mejora';
await fs.mkdir(O+'/revision',{recursive:true});
await fs.mkdir(O+'/entrega',{recursive:true});
const horizon=56, tail=62, periods=tail;
const baseline=JSON.parse(await fs.readFile(D+'/referencia-3.0.json','utf8'));
const ins=JSON.parse(await fs.readFile(D+'/insumos.json','utf8'));
const wb=await SpreadsheetFile.importXlsx(await FileBlob.load(D+'/build/origen.xlsx'));
const S=n=>wb.worksheets.getItem(n), F=(s,c,v)=>S(s).getRange(c).formulas=[[v]], V=(s,c,v)=>S(s).getRange(c).values=[[v]];
const q=n=>`'${n}'!`, pc=r=>`${q('Parámetros corrección')}$B$${r}`, pd=r=>`${q('Parámetros D2')}$B$${r}`;
const add=n=>{const s=wb.worksheets.add(n);s.showGridLines=false;s.freezePanes.freezeRows(1);return s;};
const nuevos=['Conciliación técnica','Activaciones','Calendario E25','Mesa de ayuda','Parámetros corrección','Tarifas por perfil','Dotación por perfil','Instalación por lote','Soporte por perfil','Contrato de soporte','Hitos E25','Escenarios corregidos','Atribución innovaciones','Control de entrega','Gráficos UF'];
nuevos.forEach(add);
const param=[
 ['Parámetro','Valor','Fuente y criterio'],
 ['Horas de referencia por FTE y mes',160,'T-15. Capacidad bruta; no son horas netas de programación.'],
 ['Piso de caja CLP',20000000,'Supuesto de tesorería: 500 UF. Complemento a financiación de contingencias.'],
 ['Capital inicial total CLP',baseline.capital,'Presupuesto 3.0 conservado para medir la exposición. Fracción bancaria E-24.'],
 ['Mes inicio de amortización',21,'H12; pago anticipado sujeto al piso de caja.'],
 ['Minutos técnico a bordo por kit',140,'D2/D4, estimación por validar en piloto; no representa una medición.'],
 ['Minutos banco por kit',20,'D2/D4; actividad que conserva audIT.'],
 ['Minutos analista por kit',140,'D2/D4; integración, prueba y recepción conservadas.'],
 ['Recargo servicio externo',0.15,'Supuesto de cotización presupuestaria para coordinación e insumos menores.'],
 ['Traslado por terminal regional y lote CLP',300000,'Provisión de viaje por visita; 4 regiones por lote M7-M9. Supuesto, no cotización recibida.'],
 ['Terminales regionales por lote',4,'Antofagasta, Talca, Los Ángeles y Puerto Montt; San Bernardo local.'],
 ['Factor variable soporte M21-M24',1,'Estabilización H12; aceptación y saneamiento de pendientes.'],
 ['Factor variable soporte M25-M32',0.75,'Hipótesis: 25% menos trabajo variable, tras cumplir criterios de reducción.'],
 ['Factor variable soporte M33-M44',0.5,'Hipótesis: demanda variable a la mitad; se conserva cobertura fija.'],
 ['Factor variable soporte M45-M56',0.25,'Hipótesis de régimen maduro; permanece capacidad fija y guardia.'],
 ['Overhead incremental sobre personal',0.02,'Provisión empresarial de gerencia, contabilidad y administración; adicional a primas y notaría.'],
 ['Consumo energía por mes kWh',3000,'Presupuesto de sala y gabinetes, no medición; se incluye a cargo de audIT.'],
 ['Costo energía CLP/kWh',180,'Supuesto de presupuesto, sin cotización comercial acreditada.'],
 ['Combustible de pruebas L/mes',50,'Grupo electrógeno: provisión de pruebas, sin considerar una emergencia prolongada.'],
 ['Costo combustible CLP/L',1100,'Supuesto de presupuesto, neto.'],
 ['Inicio gastos energía/combustible',4,'Habilitación previa a H3.'],
 ['Costo crítico +5%',0.05,'Sensibilidad sin reajuste de precio.'],
 ['Ingreso -5%',0.05,'Sensibilidad sin reducir costos.'],
 ['Mes cobro H5 estrés 1',13,'Se mantiene factura H5 M12.'],
 ['Mes cobro H5 estrés 2',14,'Dos meses respecto del caso base de cobro.'],
 ['Reserva D4 CLP',152699775,'D4 4.7: 10% del costo referencial D4; sensibilidad, no gasto base.'],
 ['Mes pago reserva D4',12,'Disparador: contingencia antes de certificar H5; variante adelanta a M9.'],
 ['Financiamiento contingente total CLP',baseline.facilidad,'Facilidad presupuestaria 80/20 adicional en M12; condición financiera de la oferta.'],
 ['Comisión bancaria CLP',250000,'Supuesto de presupuesto del instrumento; pagada M1.'],
 ['Comisión contingencia CLP',250000,'Supuesto, se aplica únicamente al activar la facilidad.'],
 ['Mes desembolso contingencia',12,'Antes de egresos del mes crítico; disponibilidad condicionada.'],
 ['Mes amortización contingencia',16,'Tras H5 y H7, conservando el piso.'],
 ['Control cierre SLA respuesta min',15,'FEP01 Art.78.2 p.40.'],
 ['Control cierre SLA resolución min',240,'FEP01 Art.78.2 p.40.'],
 ['Disponibilidad crítica mínima',0.999,'FEP01 Art.78.2 p.40.'],
 ['Desfase de cobro operativo (meses)',1,'E-25: mes siguiente al servicio vencido. Modificar solo para sensibilidad.'],
 ['Mes piloto',6,'10 equipos, San Bernardo.'],
 ['Nº kits piloto',10,'Incluidos en los 182 montajes; no se duplican.'],
 ['Nº kits externos M7',60,'Agenda por cinco terminales, 12 por terminal.'],
 ['Nº kits externos M8',60,'Agenda por cinco terminales, 12 por terminal.'],
 ['Nº kits externos M9',52,'San Bernardo 12; otros terminales 10 cada uno.'],
 ['Mes final montaje externo',"=MAXIFS('Instalación por lote'!A2:A21,'Instalación por lote'!D2:D21,\">0\")",'Pago y término de servicio por lote; no hay costo recurrente de montaje.'],
 ['Línea habilitada base 0/1',0,'Base sin línea. Las sensibilidades conservan tope E-24 de CLP50 millones.'],
 ['Horas de preparación CP-SEC-05',72,'Alcance registrado por D3; incluido en la demanda mensual, no se suma nuevamente.'],
 ['Mes cierre de observación económica',56,'Horizonte E-24; M57 solo cobra la última factura de operación.'],
 ['Viajes anuales de referencia',96000,'FEP03, numeral 14.1 p.29.'],
 ['Minutos por expediente evitables',2,'Hipótesis de INN1 para sensibilidad de capacidad, no ahorro contractual.'],
 ['Costo de oportunidad CLP/h',6000,'Hipótesis de valorización de capacidad de Curimón; no cobro de audIT.'],
 ['Adopción INN1',0.5,'Hipótesis; sólo cuenta el universo con expediente verificable.'],
 ['Recupero anual INN4 CLP',120700000,'Insumo D2, recupero bruto bajo supuesto 50% del monto objetado.'],
 ['Meses de régimen beneficios',`=${pd(16)}`,'Operación M21-M56; no se suman estos beneficios a ventas audIT.'],
 ['Balizas base a montar',210,'Caso14.1 y D4 4.1. Las 21 de stock no se montan al alta inicial.'],
 ['Minutos montaje por baliza',15,'Estimación D4, no medición.'],
 ['Meses montaje balizas',3,'M7-M9, 70 unidades por mes; ventanas por terminal.'],
 ['Lectores de portería',5,'D4 4.9: uno por terminal, hardware del mandante.'],
 ['Horas por lector de portería',2,'Supuesto de instalación y prueba dentro de Electrónica en M5-M6.'],
 ['Semilla TIR base',0.8,'Semilla numérica histórica. Verificar raíces y VAN.'],
 ['Semilla TIR sensibilidades',0.1,'Semilla numérica histórica. Verificar raíces y VAN.'],
 ['Fracción del costo interno de montaje evitable',0,'Sin baja de nómina, horas extra o compra acreditada; 3.0 modelaba 100%.'],
 ['Precio implementación de referencia',baseline.implementacion,'RESUMEN!H6 en el corte auditado del 14-11-2026, CLP netos.'],
 ['Mensualidad de referencia',baseline.mensualidad,'Parámetros D2!B15 del corte 3.0, CLP netos al mes.'],
 ['Usar precio de referencia (1) o simular recálculo (0)',1,'Precio a igual alcance para medir variaciones. El recálculo es un escenario.'],
 ['Kits iniciales adjudicables',182,'148 propios + 34 terceros sin dispositivo. D4 4.1; incluye pilotos.'],
 ['Activación Iridium por equipo (USD)',31.5,'D4 4.2 / Ground Control, referencia inicial USD/equipo, sin validación comercial.'],
 ['Aire Iridium mensual por equipo (USD)',36.75,'D4 4.2 / Ground Control, 25 KB/equipo/mes.'],
 ['LTE mensual por línea (CLP)',3000,'D4-145 estimación, operador por seleccionar.'],
 ['Crecimiento M24',8,'D4 4.2: equipos adicionales, escenario presupuestario.'],
 ['Crecimiento M36',7,'D4 4.2: equipos adicionales, escenario presupuestario.'],
 ['Crecimiento M48',7,'D4 4.2: equipos adicionales, escenario presupuestario.'],
 ['Habilitar escalones de madurez (0/1)',0,'Caso base conserva 100% de carga variable. B12:B15 son el escenario de madurez.'],
 ['Mes de pago de la garantía de funcionamiento',21,'H12 presupuestado en M21; se imputa a implementación por objeto.'],
 ['H4: cobro de referencia',ins.hitos.find(([,id])=>id==='H4')[0],'E-25; confirmar acta, factura y vencimiento.'],
 ['H12: cobro de referencia',ins.hitos.find(([,id])=>id==='H12')[0],'E-25; confirmar acta, factura y vencimiento.'],
 ['Mes H4 de atraso',11,'Escenario de caja, factura en M10 salvo atraso del acta.'],
 ['Mes H12 de atraso de cobro',22,'Supuesto de un mes de atraso sobre M21.'],
 ['Mes de anticipo alternativo de facilidad',9,'Escenario H4 / reserva adelantada. No acredita disponibilidad.'],
 ['Cuotas de amortización alternativas',4,'Escenario: hasta cuatro cuotas de capital iguales desde M21; sujeto al piso.'],

 ];
write('Parámetros corrección',param);
const perfiles=[
 ['Jefe de proyecto',58000,1,1,1,1,1,1,1,'E-26 Jefe de Proyecto, costo medio 1,45 UF/h; gestión EDT1'],
 ['Arquitectura',44000,1,1,1,1,1,1,1,'E-26 Arquitecto Senior, 1,10 UF/h; EDT2/3/5-8'],
 ['Seguridad',44000,1,1,1,1,1,1,1,'E-26 Seguridad TI; EDT2/3/10, guardia y pruebas'],
 ['Líder QA',24000,1,1,1,1,1,1,1,'E-26 QA Experto; EDT10 y aceptación independiente'],
 ['Líder Datos',32000,1,1,1,1,1,1,1,'E-26 Ingeniero Datos; EDT7'],
 ['SRE',32000,1,1,2,2,3,3,3,'E-26 DevOps/SRE; EDT3 y entornos, estabilización H7/H12'],
 ['PMO',24000,3,3,3,3,3,2,2,'Rol adicional, referencia analista junior; EDT1/9'],
 ['Liderazgo desarrollo',42000,1,1,1,1,1,1,1,'E-26 Jefe Desarrollo; EDT5/6/8'],
 ['Software',30000,2,2,4,4,4,3,2,'E-26 Ingeniero Senior; incluye full-stack; se amplía por demanda D3'],
 ['Frontend',30000,1,2,2,2,2,2,1,'E-26 Ingeniero Senior; web y móvil'],
 ['Datos',32000,1,1,1,1,2,2,2,'E-26 Ingeniero Datos; implementación y migración'],
 ['QA',20000,0,1,1,1,2,2,1,'E-26 QA Senior; pruebas de construcción'],
 ['Firmware',28000,0,2,3,3,3,2,1,'Rol adicional; referencia Ingeniero Senior, EDT4/8'],
 ['Electrónica',28000,0,1,1,1,1,1,1,'Rol adicional; referencia Ingeniero Senior, EDT4'],
 ['Técnico de campo',16000,0,1,1,1,1,1,1,'Rol adicional; referencia costo mínimo Ingeniero Junior, EDT4/11'],
 ['Funcional',30000,0,1,1,1,1,1,1,'Rol adicional; referencia Analista Senior, EDT2/9'],
 ['Integración',30000,0,1,1,1,1,1,1,'Rol adicional; referencia Ingeniero Senior, EDT6'],
 ['Implantación y cambio',30000,0,1,1,1,1,1,1,'Rol adicional; referencia Analista Senior, EDT11'],
 ['Analista terreno',20000,0,1,3,6,7,3,3,'Rol adicional; referencia Analista Junior; banco, instalación lógica, QA y recepción'],
 ];
// Los tramos son estimación de presupuesto por rol; D3 es un mínimo de carga, no una bolsa libre.
S('Tarifas por perfil').getRange('A1:J20').values=[['Perfil','CLP/h','M1-2 FTE','M3-5','M6-9','M10-12','M13-17','M18','M19-20','Fuente / actividad'],...perfiles];
const dr=[['Mes',...['arquitectura','lider','software','frontend','seguridad','datos','qa','sre'],'Fuente']];
for(let m=1;m<=56;m++){const row=ins.demanda.find(r=>+r.mes===m);dr.push([m,...dr[0].slice(1,9).map(k=>(row?+row[k]:0)+(k==='software'&&m>=8&&m<=12?24:0)+(k==='software'&&m>=4&&m<=9?50:0)+(k==='software'&&m>=21?10:0)),'D3 matriz + INN3 (120h) + INN5 (300h desarrollo, 360h soporte); estimación y preparación de pruebas.']);}
S('Dedicación D3').getRange('A1:Z100').clear({applyTo:'contents'});S('Dedicación D3').getRange('A1:J57').values=dr;
const ih=[['Mes','Terminal','Kits piloto','Kits externos','Horas técnico externo','Horas banco audIT','Horas analista audIT','Neto servicio CLP','IVA CLP','Pago bruto CLP','Costo interno sustituido teórico CLP','Estado y ventana']];
for(let m=6;m<=9;m++)for(const [i,t] of ['San Bernardo','Antofagasta','Talca','Los Ángeles','Puerto Montt'].entries()){
 const r=ih.length+1; const lote=pc(39+m-7);
 ih.push([m,t,m===6&&i===0?`=${pc(38)}`:0,m===6?0:`=QUOTIENT(${lote},5)+IF(B${r}="San Bernardo",MOD(${lote},5),0)`,`=D${r}*${pc(6)}/60`,`=(C${r}+D${r})*${pc(7)}/60`,`=(C${r}+D${r})*${pc(8)}/60`,
 `=E${r}*${q('Tarifas por perfil')}$B$16*(1+${pc(9)})+IF(D${r}>0,IF(B${r}="San Bernardo",0,${pc(10)}),0)`,
 `=H${r}*${pd(11)}`,`=SUM(H${r}:I${r})`,`=E${r}*${q('Tarifas por perfil')}$B$16`,'Presupuesto: visita normal habilitada; 140 min de puesto. Art.73, autorización previa al lote.']);
}
write('Instalación por lote',ih);
const activation=[['Mes','Aceptación inicial presupuestada','Crecimiento','Nuevas altas','Equipos activos','Activación Iridium CLP','Aire Iridium CLP','LTE CLP']];
for(let m=1;m<=horizon;m++){
 const r=m+1;
 activation.push([m,`=SUMIF('Instalación por lote'!$A$2:$A$21,A${r},'Instalación por lote'!$C$2:$C$21)+SUMIF('Instalación por lote'!$A$2:$A$21,A${r},'Instalación por lote'!$D$2:$D$21)`,
  ({24:`=${pc(67)}`,36:`=${pc(68)}`,48:`=${pc(69)}`})[m] ?? 0,
  `=B${r}+C${r}`,`=SUM($D$2:D${r})`,`=D${r}*${pc(64)}*${pd(19)}`,`=E${r}*${pc(65)}*${pd(19)}`,`=E${r}*${pc(66)}`]);
}
write('Activaciones',activation);
for(const [i,row] of ins.proveedores_d4.entries()){
 const col={'Activación Iridium':'F','Tiempo de aire Iridium':'G','LTE a bordo':'H'}[row[2]];
 if(!col || row[1]!=='audIT')continue;
 const r=i+1;
 F('Detalle proveedores D4',`E${r}`,`=INDEX(Activaciones!$${col}$2:$${col}$57,A${r})`);
}

const dh=[['Mes','Perfil','EDT / actividad','FTE referencia','Horas brutas','Demanda D3 h','Horas adicionales','Horas montaje sustituidas','Horas internas contratadas','CLP/h','Costo CLP','Criterio']];
const mapa={'Arquitectura':'B','Liderazgo desarrollo':'C','Software':'D','Frontend':'E','Seguridad':'F','Datos':'G','QA':'H','SRE':'I'};
for(let m=1;m<=20;m++)for(let j=0;j<perfiles.length;j++){
 let tramo=m<=2?2:m<=5?3:m<=9?4:m<=12?5:m<=17?6:m===18?7:8;const r=dh.length+1,tr=j+2;
 const perfil=perfiles[j][0];const rr=m+1;
 dh.push([m,perfil,perfiles[j][9],`=${q('Tarifas por perfil')}${String.fromCharCode(65+tramo)}${tr}`,`=D${r}*${pc(2)}`,
 mapa[perfil]?`=${q('Dedicación D3')}${mapa[perfil]}${rr}`:perfil==='Técnico de campo'&&m>=6&&m<=9?`=SUMIF('Instalación por lote'!$A$2:$A$21,A${r},'Instalación por lote'!$E$2:$E$21)+SUMIF('Instalación por lote'!$A$2:$A$21,A${r},'Instalación por lote'!$F$2:$F$21)+IF(A${r}=${pc(37)},${pc(38)}*${pc(6)}/60,${pc(52)}*${pc(53)}/60/${pc(54)})`:perfil==='Analista terreno'?`=SUMIF('Instalación por lote'!$A$2:$A$21,A${r},'Instalación por lote'!$G$2:$G$21)`:0,
 `=MAX(0,F${r}-E${r})`,perfil==='Técnico de campo'?`=SUMIF('Instalación por lote'!$A$2:$A$21,A${r},'Instalación por lote'!$E$2:$E$21)*${pc(59)}`:0,
 `=MAX(0,E${r}+G${r}-H${r})`,`=${q('Tarifas por perfil')}B${tr}`,`=I${r}*J${r}`,
 'Base por rol más brecha documentada. Se resta únicamente la fracción de montaje interno efectivamente evitable.']);
}
write('Dotación por perfil',dh);
const sh=[['Mes','Perfil / paquete','Horas fijas','Horas variables iniciales','Factor madurez','Refuerzo h','Horas contratadas','CLP/h','Costo mensual CLP','Actividad y condición']];
const soportes=[['L1 24x7 / EDT13.1',960,0,16000,'Seis agentes; 930 h programadas en mes de 31 días y reserva de 30 h.'],
 ['SRE / EDT13.2',320,0,32000,'Operación, monitoreo y guardia; dos perfiles.'],
 ['Seguridad / EDT13.2',80,0,44000,'Gestión de incidentes de seguridad y guardia.'],
 ['Gestión servicio / EDT13.2',80,0,42000,'SLA, cambios y coordinación de guardias.'],
 ['Monitoreo / EDT13.2',160,0,24000,'Supervisión y mantenimiento preventivo.'],
 ['Campo / EDT13.3',320,0,16000,'Dos perfiles: ciclo de vida, reposiciones y recepción en terminal.'],
 ['Software / EDT13.4',160,160,30000,'Base correctiva y guardia; variable: mejoras y deuda técnica.'],
 ['Datos / EDT13.4',80,80,32000,'Base operación datos; refuerzo temporal 66h para cierre EDT6.5/7.2.'],
 ['QA / EDT13.4',80,80,20000,'Base regresión; refuerzo temporal 37h para cierres e implantación.'],
 ['Arquitectura cierre / EDT6.5',0,0,44000,'Revisión de cierre de integraciones y migración, D3 M21-M24.'],
 ['Frontend cierre / EDT6.5',0,0,30000,'Correcciones de convivencia y retiro de interfaces, D3 M21-M24.'],
 ['L1 suplencias y picos / EDT13.1',160,0,16000,'Reserva mensual de un FTE para ausencias, descanso y colas críticas.']];
write('Contrato de soporte',[['Rol / paquete','Horas fijas','Horas variables iniciales','CLP/h','Fuente y alcance'],...soportes]);
for(let m=21;m<=56;m++)for(const [i,a] of soportes.entries()){const r=sh.length+1;const factor=m<=24?12:m<=32?13:m<=44?14:15;const sr=i+2;
 sh.push([m,a[0],`='Contrato de soporte'!B${sr}`,`='Contrato de soporte'!C${sr}`,`=IF(${pc(70)}=1,${pc(factor)},1)`,m<=24?(a[0].startsWith('Datos')?66:a[0].startsWith('QA')?37:a[0].startsWith('Arquitectura')?Number(ins.demanda.find(d=>+d.mes===m).arquitectura):a[0].startsWith('Frontend')?Number(ins.demanda.find(d=>+d.mes===m).frontend):0):0,
 `=C${r}+D${r}*E${r}+F${r}`,`='Contrato de soporte'!D${sr}`,`=G${r}*H${r}`,a[4]+' Reducción: dos meses sin P1, backlog <10 y demanda dentro de la capacidad; si falla, se conserva factor anterior.']);}
write('Soporte por perfil',sh);
for(let m=1;m<=56;m++){
 const r=m+1;
 V('Personal',`A${r}`,m);V('Personal',`B${r}`,ins.costos[m-1].personal_anterior);
 F('Personal',`D${r}`,m<=20?`=SUMIF('Dotación por perfil'!$A$2:$A$381,A${r},'Dotación por perfil'!$K$2:$K$381)`:
 `=SUMIF('Soporte por perfil'!$A$2:$A$433,A${r},'Soporte por perfil'!$I$2:$I$433)`);
 F('Personal',`C${r}`,`=D${r}-B${r}`);V('Personal',`E${r}`,'Referencia anterior en B; costo corregido D desde horas y tarifas, sin sumar otra vez los refuerzos.');
 F('Costos',`B${r}`,`=Proveedores!E${2+(m-1)*5}+SUMIF('Instalación por lote'!$A$2:$A$21,A${r},'Instalación por lote'!$H$2:$H$21)+IF(A${r}>=${pc(21)},${pc(17)}*${pc(18)}+${pc(19)}*${pc(20)},0)`);
 F('Costos',`G${r}`,`=Personal!D${r}`);
 F('Costos',`E${r}`,`=SUMIF('Gastos Administrativos'!$B$2:$B$31,A${r},'Gastos Administrativos'!$C$2:$C$31)+G${r}*${pc(16)}`);
}
V('Personal','B1','Costo histórico CLP');V('Personal','C1','Variación CLP');V('Personal','E1','Trazabilidad');
V('Costos','B1','D4 + montaje + energía');
F('Parámetros D2','B4',`=${pc(4)}`);V('Parámetros D2','C4','Capital base corregido. Fuente: Parámetros corrección.');
for(const [r,p] of [[22,26],[23,27],[24,22],[27,28],[31,24],[32,36],[33,30],[34,31]])F('Parámetros D2',`B${r}`,`=${pc(p)}`);
F('Parámetros D2','B25',`=-${pc(23)}`);
F('Parámetros D2','B14',`=IF(${pc(62)}=1,${pc(60)},SUM(Costos!I2:INDEX(Costos!I2:I57,B17-1))/(1-B2-B3))`);
F('Parámetros D2','B15',`=IF(${pc(62)}=1,${pc(61)},SUM(INDEX(Costos!I2:I57,B17):INDEX(Costos!I2:I57,B17+B16-1))/(1-B2)/B16)`);
V('Parámetros D2','C14','Precio 3.0 para el cotejo. Recálculo opcional con margen explícito.');
V('Parámetros D2','C15','Mensualidad 3.0 para el cotejo. Recálculo opcional con el calendario de servicio.');
V('Parámetros D2','C27','Vínculo a facilidad presupuestada en Parámetros corrección.');
V('Parámetros D2','C34','Vínculo al mes provisional de desembolso y comisión de la facilidad.');
V('Gastos Administrativos','B35','Provisión incluida');
V('Gastos Administrativos','E35','2% de nómina audIT en Costos!E. Conciliar R-24 y evitar duplicar cargas.');
V('Costos','M1','Fase garantía');
for(let m=1;m<=horizon;m++){
 const r=m+1;
 F('Costos',`J${r}`,`=IF(A${r}=${pc(71)},${pd(14)}*${pd(3)},0)`);
 F('Costos',`M${r}`,`=IF(J${r}>0,"Implementación","")`);
}
F('RESUMEN','B18',`=(SUM(Costos!K2:INDEX(Costos!K2:K57,${pd(17)}-1))+SUM(Costos!J2:J57)-SUM(Costos!J2:INDEX(Costos!J2:J57,${pd(17)}-1)))/PARÁMETROS!$B$6`);
F('RESUMEN','B19',`=SUM(Costos!K2:K57)/PARÁMETROS!$B$6-B18`);
F('RESUMEN','G18',`=${pd(14)}/PARÁMETROS!$B$6`);
F('RESUMEN','G19',`=SUM('Calendario E25'!E2:E57)/PARÁMETROS!$B$6`);

// El modelo conserva los precios calculados desde costos base cuando se prueba un atraso.
const h=[['Hito','Etapa','Mes factura','% implementación','Mes cobro base','Mes cobro prueba','Monto neto CLP','Criterio']];
for(const [m,id,p] of ins.hitos){
 const cobro={H4:`=${pc(72)}`,H5:`=${pd(13)}`,H12:`=${pc(73)}`}[id] ?? m;
 h.push([id,+id.slice(1)<=7?1:2,m,p,m,cobro,`=D${h.length+1}*${pd(14)}`,
  'Mes E-25 condicionado a acta conforme (art. 18). Fechas efectivas de acta, factura y pago pendientes de acreditar.']);
}
write('Hitos E25',h);
const op=[['Mes','Mes de servicio (1/0)','Ajuste neto CLP','Mes vencimiento modelado','Factura servicio CLP','Cobro servicio CLP','Factura cobrada (conteo)']];
for(let m=1;m<=tail;m++){
 const r=m+1;
 op.push([m,`=IF(AND(A${r}>=${pd(17)},A${r}<${pd(17)}+${pd(16)},A${r}<=${pc(45)}),1,0)`,
  `=SUMIF('Ajustes de operación'!$A$2:$A$57,A${r},'Ajustes de operación'!$B$2:$B$57)-SUMIF('Ajustes de operación'!$A$2:$A$57,A${r},'Ajustes de operación'!$C$2:$C$57)`,
  `=IF(B${r}=1,A${r}+${pc(36)},0)`,`=IF(B${r}=1,${pd(15)}+C${r},0)`,
  `=SUMIF($D$2:$D$57,A${r},$E$2:$E$57)`,`=COUNTIF($D$2:$D$57,A${r})`]);
}
write('Calendario E25',op);
S('Ingresos').getRange('G1:K1').values=[['Factura hito CLP','Factura servicio CLP','Cobro hito CLP','Cobro servicio CLP','Facturas de servicio cobradas']];
for(let m=1;m<=tail;m++){
 const r=m+1,prev=r-1;
 if(m>57)V('Flujo de Caja',`A${r}`,m);
 F('Flujo de Caja',`B${r}`,`=IF(COUNTIF('Hitos E25'!$C$2:$C$13,A${r})=0,"",INDEX('Hitos E25'!$A$2:$A$13,MATCH(A${r},'Hitos E25'!$C$2:$C$13,0)))`);
 F('Flujo de Caja',`C${r}`,`=SUMIF('Hitos E25'!$C$2:$C$13,A${r},'Hitos E25'!$D$2:$D$13)`);
 F('Flujo de Caja',`D${r}`,`='Calendario E25'!C${r}`);
 F('Ingresos',`G${r}`,`=SUMIF('Hitos E25'!$C$2:$C$13,'Flujo de Caja'!A${r},'Hitos E25'!$G$2:$G$13)`);
 F('Ingresos',`H${r}`,`='Calendario E25'!E${r}`);
 F('Ingresos',`I${r}`,`=SUMIF('Hitos E25'!$F$2:$F$13,'Flujo de Caja'!A${r},'Hitos E25'!$G$2:$G$13)`);
 F('Ingresos',`J${r}`,`='Calendario E25'!F${r}`);
 F('Ingresos',`K${r}`,`='Calendario E25'!G${r}`);
 if(m>57)for(const c of 'ABCDEF')F('Ingresos',`${c}${r}`,`='Flujo de Caja'!${c}${r}`);
 F('Flujo de Caja',`E${r}`,`=SUM(Ingresos!G${r}:H${r})`);
 F('Flujo de Caja',`F${r}`,`=SUM(Ingresos!I${r}:J${r})`);
 F('Flujo de Caja',`G${r}`,m<=56?`=Costos!K${r}`:'=0');F('Flujo de Caja',`H${r}`,`=F${r}-G${r}`);
 F('Flujo de Caja',`I${r}`,`=E${r}*${pd(11)}`);F('Flujo de Caja',`J${r}`,`=F${r}*${pd(11)}`);
 F('Flujo de Caja',`K${r}`,`=SUMIF(Proveedores!$B$2:$B$281,A${r},Proveedores!$G$2:$G$281)+SUMIF(Proveedores!$B$2:$B$281,A${r},Proveedores!$I$2:$I$281)+SUMIF('Instalación por lote'!$A$2:$A$21,A${r},'Instalación por lote'!$I$2:$I$21)`);
 // Conservador: no reconocer crédito fiscal hasta contar con documento; IVA se presenta por separado.
 V('Flujo de Caja',`L${r}`,0);F('Flujo de Caja',`M${r}`,`=I${r}`);V('Flujo de Caja',`N${r}`,0);
 F('Flujo de Caja',`O${r}`,`=(J${r}-K${r}-${m===1?'0':`M${prev}`})*${pd(12)}`);
 F('Flujo de Caja',`P${r}`,m===1?'=0':`=V${prev}*${pd(6)}`);
 F('Flujo de Caja',`Q${r}`,m===1?'=0':`=T${prev}*${pd(7)}`);
 const opening=m===1?'0':`W${prev}`, bankprev=m===1?'0':`V${prev}`,lineprev=m===1?'0':`T${prev}`;
 const injection=`IF(A${r}=1,${pd(4)},0)`,fee=`IF(A${r}=1,${pc(29)},0)`;
 F('Flujo de Caja',`Y${r}`,`=${opening}+H${r}+O${r}+${injection}-P${r}-Q${r}-${fee}`);
 F('Flujo de Caja',`R${r}`,`=IF(${pc(43)}=1,MIN(MAX(0,${pd(8)}-${lineprev}),MAX(0,-Y${r})),0)`);
 F('Flujo de Caja',`S${r}`,`=MIN(${lineprev},MAX(0,Y${r}-${pc(3)}))`);
 F('Flujo de Caja',`T${r}`,`=${lineprev}+R${r}-S${r}`);
 F('Flujo de Caja',`U${r}`,`=IF(A${r}>=${pc(5)},MIN(${bankprev},MAX(0,Y${r}+R${r}-S${r}-${pc(3)})),0)`);
 F('Flujo de Caja',`V${r}`,`=${bankprev}+${injection}*${pd(5)}-U${r}`);
 F('Flujo de Caja',`W${r}`,`=Y${r}+R${r}-S${r}-U${r}`);
 F('Flujo de Caja',`X${r}`,`=W${r}-${opening}`);
 F('Flujo de Caja',`Z${r}`,`=SUM($O$2:O${r})`);
 F('Flujo de Caja',`AA${r}`,`=W${r}-Z${r}`);
 F('Flujo de Caja',`AB${r}`,`=${injection}*${pd(5)}`);F('Flujo de Caja',`AC${r}`,`=${injection}*(1-${pd(5)})`);
 F('Flujo de Caja',`AD${r}`,`=${fee}`);F('Flujo de Caja',`AG${r}`,`=Y${r}-F${r}-J${r}`);
 F('Flujo de Caja',`AH${r}`,`=X${r}-(F${r}-G${r}+O${r}+AB${r}+AC${r}-P${r}-Q${r}-AD${r}+R${r}-S${r}-U${r})`);
 F('Flujo de Caja',`AE${r}`,`=H${r}/(1+${pd(10)})^A${r}`);F('Flujo de Caja',`AF${r}`,`=SUM($AE$2:AE${r})`);
 for(const [c,expr] of [['B',injection],['C',`AC${r}`],['D',`AB${r}`],['E',`P${r}`],['F',`Q${r}`],['G',`R${r}`],['H',`S${r}`],['I',`T${r}`],['J',`U${r}`],['K',`V${r}`],['L',`W${r}`]])F('Financiamiento',`${c}${r}`,`=${c==='B'?expr:`'Flujo de Caja'!${expr}`}`);
}
S('Flujo de Caja').getRange('Y1:AF1').values=[['Antes línea y amortización','IVA acumulado','Caja neta sin IVA','Banco desembolsado','Aporte socios','Comisión banco','Flujo descontado','Acumulado descontado']];
V('Flujo de Caja','AG1','Cota pagos antes de cobros');
V('Flujo de Caja','AH1','Diferencia identidad caja');
V('Financiamiento','C1','Aporte socios');V('Financiamiento','D1','Crédito bancario');
F('Indicadores','B3',`=IFERROR(IRR('Flujo de Caja'!H2:H57,${pc(57)}),"Revisar raíces")`);
F('Indicadores','B8',`=SUM('Flujo de Caja'!F58:F${tail+1})`);
V('Indicadores','A8','Cobros posteriores al M56');
F('Indicadores','B7',`=SUMPRODUCT((COUNTIF(Proveedores!A2:A281,Proveedores!A2:A281)>1)*1)`);
F('Indicadores','B14',`=IF(MIN('Flujo de Caja'!AF2:AF57)>=0,1,LOOKUP(2,1/('Flujo de Caja'!AF2:AF57<0),'Flujo de Caja'!A2:A57)+1)`);
V('Indicadores','B9','Base presupuestaria 3.1; ver condiciones y controles');
F('Indicadores','B15',`=MIN('Flujo de Caja'!AA2:AA57)`);V('Indicadores','A15','Caja mínima neta sin IVA');
// Sensibilidades simultáneas: se conserva la arquitectura de escenarios del modelo original,
// con un cálculo explícito de cada movimiento; todos los resultados se expresan con fórmulas.
const cases=[
 ['Atraso H5 M13',`=${pc(24)}`,0,0,0,0,0,0,1,0,0],
 ['Atraso H5 M14',`=${pc(25)}`,0,0,0,0,0,0,1,0,0],
 ['H5 M14 + reserva M12',`=${pc(25)}`,`=${pc(27)}`,0,0,0,0,0,1,0,0],
 ['H5 M14 + reserva + facilidad',`=${pc(25)}`,`=${pc(27)}`,1,0,0,0,0,1,0,0],
 ['Costos +5%',0,0,0,`=${pc(22)}`,0,0,0,0,0,0],
 ['Cobros -5%',0,0,0,0,`=${pc(23)}`,0,0,0,0,0],
 ['Reserva anticipada M9',`=${pc(25)}`,`=${pc(76)}`,1,0,0,0,0,1,0,0],
 ['H4 cobro M11, sin línea',0,0,0,0,0,`=${pc(74)}`,0,0,0,0],
 ['H4 cobro M11, con línea',0,0,0,0,0,`=${pc(74)}`,0,1,0,0],
 ['H4 cobro M11, facilidad M9',0,0,1,0,0,`=${pc(74)}`,0,0,0,0],
 ['H4 acta y cobro M11',0,0,0,0,0,`=${pc(74)}`,0,0,1,0],
 ['H12 cobro al mes siguiente',0,0,0,0,0,0,`=${pc(75)}`,0,0,0],
 ['Soporte sin reducción',0,0,0,0,0,0,0,0,0,1],
 ['Soporte por madurez 3.0',0,0,0,0,0,0,0,0,0,-1],
 ['Banco en cuotas desde M21',0,0,0,0,0,0,0,0,0,0,`=${pc(77)}`],
];
S('Sensibilidad').getRange('A1:AZ500').clear({applyTo:'contents'});
const ss=[['Escenario','Mes cobro H5','Mes reserva','Activar facilidad','Shock costo','Shock ingreso','Caja mínima CLP','Mes mínimo','Línea máxima CLP','Déficit residual CLP','Interés línea CLP','Interés banco CLP','VAN Fila A CLP','TIR mensual','Aporte socios CLP','Banco desembolsado CLP','Saldo deuda final','Criterio de TIR','Cota antes de cobros CLP','Mes cobro H4','Mes cobro H12','Línea 0/1','Mover acta H4 0/1','Carga soporte (1 pleno, -1 escalones, 0 base)','Cuotas banco','Giro individual máx.','Mes cota mínima','Faltante frente a piso CLP','Comisiones CLP','Caja al cierre M56','Cobros posteriores a M56']];
const er=[['Escenario','Mes','Factura neta','Cobro neto','Costo base','Reserva / shock','Fila A','Capital inicial','Capital contingente','Interés banco','Interés línea','IVA neto caja','Antes giro','Giro línea','Pago línea','Saldo línea','Pago banco','Saldo banco','Caja cierre','Fila C','Flujo descontado','Cota antes de cobros']];
for(let ci=0;ci<cases.length;ci++){
 const cr=ci+2,start=er.length+1,end=start+periods-1,evalEnd=start+horizon-1;
 const [label,h5,res,bridge,cost,revenue,h4,h12,lineEnabled,acceptance,maturity,instalments=0]=cases[ci];
 const rg=c=>`'Escenarios corregidos'!${c}${start}:${c}${end}`;
 ss.push([label,h5,res,bridge,cost,revenue,`=MIN(${rg('S')})`,`=INDEX(${rg('B')},MATCH(G${cr},${rg('S')},0))`,
  `=MAX(${rg('P')})`,`=MAX(0,-G${cr})`,`=SUM(${rg('K')})`,`=SUM(${rg('J')})`,
  `=NPV(${pd(10)},'Escenarios corregidos'!G${start}:G${evalEnd})`,`=IFERROR(IRR('Escenarios corregidos'!G${start}:G${evalEnd},${pc(58)}),"Revisar raíces")`,
  `=(SUM(${rg('H')})+SUM(${rg('I')}))*(1-${pd(5)})`,`=(SUM(${rg('H')})+SUM(${rg('I')}))*${pd(5)}`,
  `='Escenarios corregidos'!R${end}+'Escenarios corregidos'!P${end}`,'Contrastar raíces; priorizar VAN y liquidez.',`=MIN(${rg('V')})`,h4,h12,lineEnabled,acceptance,maturity,instalments,
  `=MAX(${rg('N')})`,`=INDEX(${rg('B')},MATCH(S${cr},${rg('V')},0))`,`=MAX(0,${pc(3)}-MIN(G${cr},S${cr}))`,
  `=${pc(29)}+IF(D${cr}=1,${pc(30)},0)`,`='Escenarios corregidos'!S${evalEnd}`,`=SUM('Escenarios corregidos'!D${evalEnd+1}:D${end})`]);
 for(let m=1;m<=tail;m++){
  const r=er.length+1,pr=r-1,br=m+1;
  const cash=m===1?'0':`S${pr}`,bank=m===1?'0':`R${pr}`,line=m===1?'0':`P${pr}`;
  const paramAt=c=>`Sensibilidad!$${c}$${cr}`;
  const hit=(id,column)=>`SUMIF('Hitos E25'!$A$2:$A$13,"${id}",'Hitos E25'!$${column}$2:$${column}$13)`;
  const move=(id,col,when)=>`IF(${paramAt(col)}>0,(IF(B${r}=${paramAt(col)},1,0)-IF(B${r}=${hit(id,when)},1,0))*${hit(id,'G')},0)`;
  const stage=m<=24?12:m<=32?13:m<=44?14:15;
  const support=m>=21&&m<=56?`IF(${paramAt('X')}=0,0,(IF(${paramAt('X')}=1,1,${pc(stage)})-IF(${pc(70)}=1,${pc(stage)},1))*SUMPRODUCT('Contrato de soporte'!$C$2:$C$13,'Contrato de soporte'!$D$2:$D$13)*(1+${pc(16)}))`:'0';
  const prevInvoice=m===1?'0':`C${pr}`;
  const sched=`MAX(0,M${r}+N${r}-O${r}-${pc(3)})`;
  er.push([label,m,`=('Flujo de Caja'!E${br}+IF(${paramAt('W')}=1,${move('H4','T','C')},0))*(1-${paramAt('F')})`,
   `=('Flujo de Caja'!F${br}+${move('H4','T','F')}+${move('H5','B','F')}+${move('H12','U','F')})*(1-${paramAt('F')})`,
   `='Flujo de Caja'!G${br}`,`=IF(B${r}=${paramAt('C')},${pc(26)},0)+E${r}*${paramAt('E')}+${support}`,
   `=D${r}-E${r}-F${r}`,`=IF(B${r}=1,${pd(4)},0)`,
   `=IF(AND(${paramAt('D')}=1,B${r}=IF(OR(${paramAt('C')}=${pc(76)},${paramAt('T')}>0),${pc(76)},${pc(31)})),${pc(28)},0)`,
   `=${bank}*${pd(6)}`,`=${line}*${pd(7)}`,
   `=((D${r}-${prevInvoice})*${pd(11)}-'Flujo de Caja'!K${br})*${pd(12)}`,
   `=${cash}+G${r}+H${r}+I${r}+L${r}-J${r}-K${r}-IF(B${r}=1,${pc(29)},0)-IF(I${r}>0,${pc(30)},0)`,
   `=IF(${paramAt('V')}=1,MIN(MAX(0,${pd(8)}-${line}),MAX(0,-M${r})),0)`,
   `=MIN(${line},MAX(0,M${r}-${pc(3)}))`,`=${line}+N${r}-O${r}`,
   `=IF(B${r}>=${pc(5)},MIN(${bank},${sched},IF(${paramAt('Y')}>0,${pd(4)}*${pd(5)}/MAX(1,${paramAt('Y')}),${bank})),IF(B${r}>=${pc(32)},MIN(MAX(0,${bank}-${pd(4)}*${pd(5)}),${sched}),0))`,
   `=${bank}+(H${r}+I${r})*${pd(5)}-Q${r}`,
   `=M${r}+N${r}-O${r}-Q${r}`,`=S${r}-${cash}`,`=G${r}/(1+${pd(10)})^B${r}`,
   `=M${r}-D${r}*(1+${pd(11)}*${pd(12)})`]);
 }
}
write('Sensibilidad',ss);write('Escenarios corregidos',er);
// Las atribuciones explican dónde se consume capacidad ya pagada; no generan otro egreso.
const at=[['Innovación','EDT','Mes','Perfil','Horas atribuidas','Costo CLP/h','Costo atribuido CLP','Tratamiento']];
const roleMap={arquitectura:3,lider:9,software:10,frontend:11,seguridad:4,datos:12,qa:13,sre:7};
for(const z of ins.detalle_d3.filter(d=>d.bloque.startsWith('innovacion_'))){const r=at.length+1;const id=z.bloque.split('_')[1];at.push([`INN-${id}`,z.edt_alcance,+z.mes,z.perfil,+z.horas_solicitadas,`='Tarifas por perfil'!B${roleMap[z.perfil]}`,`=E${r}*F${r}`,'Dentro de las horas de D3 y de la nómina; no se suma al costo.']);}
for(let m=8;m<=12;m++){const r=at.length+1;at.push(['INN-3','12.3',m,'software',24,`='Tarifas por perfil'!B10`,`=E${r}*F${r}`,'120h D4 distribuidas y agregadas a demanda D3; se pagan en nómina una sola vez.']);}
for(let m=21;m<=56;m++){const r=at.length+1;at.push(['INN-3','13.4',m,'software',4,`='Tarifas por perfil'!B10`,`=E${r}*F${r}`,'Dentro de capacidad de Software del contrato de soporte, no adicional.']);}
for(let m=4;m<=9;m++){const r=at.length+1;at.push(['INN-5','12.5',m,'software',50,`='Tarifas por perfil'!B10`,`=E${r}*F${r}`,'300h D1/D2 de desarrollo, agregadas a demanda y cubiertas en nómina.']);}
for(let m=21;m<=56;m++){const r=at.length+1;at.push(['INN-5','13.4',m,'software',10,`='Tarifas por perfil'!B10`,`=E${r}*F${r}`,'360h de soporte dentro de capacidad contratada; no se duplican como refuerzo.']);}
write('Atribución innovaciones',at);const last=at.length;
S('Innovaciones').getRange('A1:U60').clear({applyTo:'contents'});
const inn=[['ID','Innovación','Costo personal atribuido CLP','Egreso directo adicional CLP','Beneficio monetario base Curimón','Cobro incremental audIT','Evaluación y medición'],
 ['INN-1','Expediente verificable',`=SUMIF('Atribución innovaciones'!$A$2:$A$${last},A2,'Atribución innovaciones'!$G$2:$G$${last})`,'=SUM(Costos!L2:L57)',0,0,'Firma en proveedores y personal en nómina. Minutos evitados y adopción: medir antes de reconocer ahorro.'],
 ['INN-2','Programación de patio',`=SUMIF('Atribución innovaciones'!$A$2:$A$${last},A3,'Atribución innovaciones'!$G$2:$G$${last})`,0,0,0,'Comparar visitas, minutos y atenciones. No monetizar sin línea base.'],
 ['INN-3','Acople y registro térmico',`=SUMIF('Atribución innovaciones'!$A$2:$A$${last},A4,'Atribución innovaciones'!$G$2:$G$${last})`,0,0,0,'Kilometraje es alcance base. Montaje de balizas y lectores en capacidad de campo/electrónica.'],
 ['INN-4','Comodato y sobreestadías',0,0,0,0,'34 comodatos dentro de los 182 kits, sin duplicar instalación. Recupero bruto referencial en Beneficios Curimón, sin convertirlo en cobro audIT.'],
 ['INN-5','Prevención de fatiga',`=SUMIF('Atribución innovaciones'!$A$2:$A$${last},A6,'Atribución innovaciones'!$G$2:$G$${last})`,`=SUM('INN-5 Costos'!E2:E5)`,0,0,'Desarrollo y soporte en nómina; talleres/calibración en Otros. Beneficio por consumo/siniestralidad sujeto a medición.']];write('Innovaciones',inn);
S('Beneficios Curimón').getRange('A1:L60').clear({applyTo:'contents'});write('Beneficios Curimón',[
 ['Concepto','Valor CLP','Tratamiento'],['Beneficio base monetario reconocido',0,'Sin ahorro monetario acreditado; no se agrega a ingresos de audIT.'],
 ['INN1: capacidad anual liberada, hipótesis',`=${pc(46)}*${pc(47)}/60*${pc(48)}*${pc(49)}`,'Sensibilidad de tiempo valorizado, no reducción demostrada de egresos.'],
 ['INN4: recupero bruto referencial 36 meses',`=${pc(50)}*${pc(51)}/12`,'Escenario D2; falta repartir con transportistas y restar costos. No es beneficio neto ni ingreso de audIT.'],
 ['INN2/3/5',0,'Beneficios físicos y protocolo de medición descritos en informe; se excluyen importes sin respaldo.']]);
// Curva S conserva series formales netas; la vista de tesorería se informa adicionalmente.
for(let m=1;m<=56;m++){const r=m+1;F('Curva S',`B${r}`,`=SUM(Costos!$K$2:K${r})+SUM('Flujo de Caja'!$P$2:Q${r})+SUM('Flujo de Caja'!$AD$2:AD${r})`);
 F('Curva S',`C${r}`,`=SUM('Flujo de Caja'!$E$2:E${r})`);F('Curva S',`D${r}`,`='Flujo de Caja'!AA${r}`);}
const gr=[['Mes','Costo acumulado UF','Facturación acumulada UF','Caja neta financiada UF','Costos mensuales UF','Caja tesorería UF','Cero UF','Banco UF','Socios UF','Amortización UF','Personal UF','Infraestructura UF','Otros y pagos puntuales UF','Facturación ajustada UF','Costo operativo acumulado UF']];
for(let m=1;m<=56;m++){const r=m+1;gr.push([`M${m}`,`='Curva S'!B${r}/${pd(21)}`,`='Curva S'!C${r}/${pd(21)}`,`='Curva S'!D${r}/${pd(21)}`,`=Costos!K${r}/${pd(21)}`,
 `='Flujo de Caja'!W${r}/${pd(21)}`,0,`='Flujo de Caja'!AB${r}/${pd(21)}`,`='Flujo de Caja'!AC${r}/${pd(21)}`,`='Flujo de Caja'!U${r}/${pd(21)}`,
 `=Costos!G${r}/${pd(21)}`,`=SUM(Costos!B${r}:C${r})/${pd(21)}`,`=E${r}-K${r}-L${r}`,
 `=( 'Curva S'!C${r}+${pd(4)}-SUM('Flujo de Caja'!$P$2:Q${r})-SUM('Flujo de Caja'!$AD$2:AD${r})-SUM('Flujo de Caja'!$U$2:U${r}))/${pd(21)}`,
 `=SUM(Costos!$K$2:K${r})/${pd(21)}`]);}
gr.push(['M0',null,null,null,null,null,null,null,null,null,null,null,null,`=${pd(4)}/${pd(21)}`,0]);
write('Gráficos UF',gr);
S('Gráficos UF').getRange('P1:S1').values=[['Mes de la serie auxiliar','Facturación ajustada UF','Costo operativo acumulado UF','Caja neta financiada UF']];
for(let m=0;m<=horizon;m++){
 const r=m+2, sr=m===0?58:m+1;
 V('Gráficos UF',`P${r}`,`M${m}`);
 F('Gráficos UF',`Q${r}`,`=N${sr}`);
 F('Gráficos UF',`R${r}`,`=O${sr}`);
 F('Gráficos UF',`S${r}`,m===0?`=N${sr}`:`=D${sr}`);
}

S('Curva S').charts.deleteAll();S('Gráficos UF').charts.deleteAll();
for(const [title,cols,place,type] of [['Curva S (UF)',['A1:A57','B1:B57','C1:C57','D1:D57'],['L2','AC21'],'line'],['Egresos mensuales (UF)',['A1:A57','K1:K57','L1:L57','M1:M57'],['L23','AC42'],'bar'],
 ['Caja y cero (UF)',['A1:A57','D1:D57','F1:F57','G1:G57'],['L44','AC63'],'line'],['Banco, socios y amortización (UF)',['A1:A57','H1:H57','I1:I57','J1:J57'],['L65','AC84'],'bar'],['Facturación ajustada, costo operativo y caja (UF)',['P1:P58','Q1:Q58','R1:R58','S1:S58'],['L86','AC105'],'line']]){
 const s=S('Gráficos UF');const chart=s.charts.add(type,cols.map(c=>s.getRange(c)));chart.title=title;chart.setPosition(...place);
 if(title.startsWith('Egresos')){chart.barOptions.direction='column';chart.barOptions.grouping='stacked';chart.barOptions.overlap=100;}
 chart.titleTextStyle.typeface='Arial';chart.titleTextStyle.fontSize=14;chart.xAxis={axisType:'textAxis',textStyle:{typeface:'Arial',fontSize:10}};
 chart.yAxis={numberFormatCode:'#,##0',numberFormatSourceLinked:false,textStyle:{typeface:'Arial',fontSize:10}};chart.legend={position:'bottom',textStyle:{typeface:'Arial',fontSize:10}};
}
write('Mesa de ayuda',[
 ['Indicador / alcance','Interna (base)','Compartida','Dedicada','Criterio'],
 ['N1 fijo y suplencias CLP/mes',"='Contrato de soporte'!B2*'Contrato de soporte'!D2+'Contrato de soporte'!B13*'Contrato de soporte'!D13",null,null,'Contrato de soporte. Antes de overhead.'],
 ['Horas N1 regulares / mes',"='Contrato de soporte'!B2",null,null,'Capacidad antes de ausencias; evidencia de cuadrante pendiente.'],
 ['Horas de suplencia / mes',"='Contrato de soporte'!B13",null,null,'Capacidad de reserva; cobertura durante licencia, descanso y picos.'],
 ['Horas mínimas de un puesto en 31 días','=31*24',null,null,'Prueba de límite superior por mes calendario.'],
 ['Horas regulares sobre un puesto','=B3-B5',null,null,'Disponible para segundo puesto, relevos y trabajo solapado; no confirma concurrencia.'],
 ['N1 interno efectivamente evitable',null,null,null,'Ingresar CLP/mes con respaldo de nómina que cesa, horas extra o terceros evitados.'],
 ['Abono externo mensual',null,null,null,'Ingresar tarifa adjudicable con SLA, puestos reservados y tramos.'],
 ['Excedentes mensuales',null,null,null,'Según volúmenes y precio de excedencia.'],
 ['Herramientas y supervisión incrementales',null,null,null,'Escalamiento, gobierno, gestión de accesos y licencias.'],
 ['Transición (pago único)',null,null,null,'Capacitación, integración, marcha paralela y traspaso.'],
 ['Ahorro mensual a igual alcance',null,'=IF(COUNT(C7:C10)<4,"Pendiente",C7-SUM(C8:C10))','=IF(COUNT(D7:D10)<4,"Pendiente",D7-SUM(D8:D10))','CLP antes de transición. La nómina reasignada sigue como egreso.'],
 ['Ahorro de 36 meses tras transición',null,`=IF(COUNT(C11:C12)<2,"Pendiente",C12*${pd(16)}-C11)`,`=IF(COUNT(D11:D12)<2,"Pendiente",D12*${pd(16)}-D11)`,'Comparación simple de costos; fecha de transición y VAN dependen de cotización.'],
 ['Cobertura y escalamiento','Crítico y alto 24×7×365','Capacidad reservada para dos críticos simultáneos','Puestos reservados por franja','Art. 78.2. Respuesta crítica 15 min; resolución 4 h; disponibilidad de servicio 99,9%.'],
 ['Evidencia requerida','Cuadrante, demanda por franja y prueba con relevo','Oferta escrita, cola, excedencias y prueba','Oferta escrita, suplencias y prueba','Todos: N2/N3 audIT, autorización escrita y límite agregado 40% (art. 73 / T-8).'],
]);
S('Mesa de ayuda').getRange('C7:D11').dataValidation={rule:{type:'decimal',operator:'greaterThanOrEqual',formula1:0}};

const tech=[['Mes o partida','Plan técnico','Presupuesto 3.1','Diferencia / holgura','Evidencia y decisión']];
const s7={6:10,7:59,8:115,9:164,10:168,11:168,12:168,13:168,14:168,15:168,16:172,17:176,18:179};
for(const [mes,acum] of Object.entries(s7)){
 const r=tech.length+1;
 tech.push([+mes,acum,`=SUM(Activaciones!$B$2:INDEX(Activaciones!$B$2:$B$57,A${r}))`,`=C${r}-B${r}`,
  'S7 tabla 7-cobertura (propios y terceros); activación presupuestada ligada a instalación. Ventanas de terceros por acreditar.']);
}
tech.push(
 ['EDT 5 A09',17600,6008,'=B15-C15','T-15 y D3 3.1 del 12-11-2026, HH. La diferencia requiere nivelación semanal antes de evitar desembolsos.'],
 ['EDT 6–8',19200,19200,'=B16-C16','6400 integración + 4800 datos/migración + 8000 alcance E2; presupuesto T-15 en HH.'],
 ['Técnico M18–M20 (HH/mes)',160,`='Tarifas por perfil'!H16*${pc(2)}`,'=C17-B17','Campo: marcha blanca, sustituciones y asistencia a recepción. Falta cuadrante y demanda por terminal.'],
 ['Analistas M18–M20 (HH/mes)',480,`='Tarifas por perfil'!H20*${pc(2)}`,'=C18-B18','Tres perfiles: capacitación, prueba por rol y recepción. Falta programación semanal y curva de concurrencia.'],
 ['Funcional e Implantación (CLP/h)',28000,`=MAX('Tarifas por perfil'!B17,'Tarifas por perfil'!B19)`,'=C19-B19','E-26 máximo de referencia Analista Senior. Conservar provisión hasta acreditar equivalencia y costo empresa.'],
 ['Balizas base (unidades)',210,`=${pc(52)}`,'=C20-B20','D4 4.1; 21 unidades de reposición fuera del montaje inicial.'],
 ['Montaje balizas (HH)',52.5,`=${pc(52)}*${pc(53)}/60`,'=C21-B21','210 × 15 min. Validar en piloto; solo esfuerzo presupuestado.'],
 ['Montaje externo (HH de puesto)',null,"=SUM('Instalación por lote'!E2:E21)",null,'140 min por equipo más banco y analista. Comparar franja/terminal, recepción y retrabajo.'],
 ['Disponibilidad de instalaciones',null,null,null,'Tres variantes: ejecución interna S7; híbrida anticipada 3.1; híbrida en ventanas S7. Requieren confirmación de stock, turnos y oferta comparable.'],
);
write('Conciliación técnica',tech);

const controls=[['Comprobación','Resultado','Criterio'],['Caja mínima tesorería',"=MIN('Flujo de Caja'!W2:W57)",'Debe superar cero y el piso presupuestado'],
 ['Caja mínima neta',"=MIN('Flujo de Caja'!AA2:AA57)",'Vista neta de las aclaraciones'],['Giros de línea base',"=SUM('Flujo de Caja'!R2:R57)",'Debe ser cero'],['Saldo máximo línea base',"=MAX('Flujo de Caja'!T2:T57)",'Debe ser cero'],
 ['Porcentajes E25',"=SUM('Hitos E25'!D2:D13)",'Debe ser uno'],['Número de hitos',"=COUNTA('Hitos E25'!A2:A13)",'Debe ser doce'],['Facturas de operación',"=SUM('Calendario E25'!B2:B57)",'Conciliar contra la duración E-25; incluye M21 junto a H12'],
 ['Kits totales',"=SUM('Instalación por lote'!C2:D21)",'Inventario de la configuración inicial, Parámetros corrección B63.'],['Kits externos',"=SUM('Instalación por lote'!D2:D21)",'Inventario inicial menos piloto si se completa el escenario híbrido.'],
 ['Costo menos Cuadro maestro',"=SUM(Costos!K2:K57)-'Cuadro maestro'!C19",'Debe ser cero'],['Ventas menos Cuadro maestro',"=SUM(Ingresos!E2:E57)-'Cuadro maestro'!D19",'Debe ser cero'],
 ['Saldo bancario al cierre de cola',"='Flujo de Caja'!V63",'Debe ser cero'],['Margen EBITDA',"=Indicadores!B10",'No supera 20%'],['Diferencia RESUMEN costo',"=RESUMEN!C8-SUM(Costos!K2:K57)",'Debe ser cero'],
 ['Diferencia RESUMEN venta',"=RESUMEN!H8-SUM(Ingresos!E2:E57)",'Debe ser cero'],['H5 factura M12',"=SUMIF('Hitos E25'!A2:A13,\"H5\",'Hitos E25'!C2:C13)",'Debe ser doce'],
 ['Costo de montaje posterior M9',"=SUMIF('Instalación por lote'!A2:A21,\">9\",'Instalación por lote'!H2:H21)",'Debe ser cero'],
 ['Reducción soporte variable en base',`=IF(${pc(70)}=1,${pc(12)}-${pc(15)},0)`,'Escalones sujetos a medición. La cobertura fija se conserva'],['Fuente de cierre','3.1 / 15-11-2026','Base corregida; presupuesto y condiciones de oferta'],
 ['Cota base: pagos antes de cobros',"=MIN('Flujo de Caja'!AG2:AG57)",'Cobertura conservadora antes de cobrar; evita inventar fechas dentro del mes']];
controls.push(
 ['Facturas de operación cobradas',`=SUM(Ingresos!K2:K${tail+1})`,'Debe conciliar con las facturas de servicio emitidas.'],
 ['Último mes de cobro operación',`=MAX('Calendario E25'!D2:D57)`,'M57 contractual; varía en sensibilidades de desfase.'],
 ['Diferencia de kits contra inventario',`=B9-${pc(63)}`,'Cero para liberar. Reasignar el remanente entre lotes sin duplicar kits.'],
 ['Saldo de facturación menos cobros',`=SUM(Ingresos!E2:E${tail+1})-SUM(Ingresos!F2:F${tail+1})`,'Cero tras la cola cuando el caso base se cobra íntegro.'],
 ['Diferencia meses programados',`=B8-${pd(16)}`,'Cero; inicio y duración deben caber antes del cierre del horizonte.'],
 ['Último pago banco',`=LOOKUP(2,1/('Flujo de Caja'!U2:U${tail+1}>0),'Flujo de Caja'!A2:A${tail+1})`,'Mes efectivo en el modelo.'],
 ['Reconciliación de caja (máx.)',`=MAX(MAX('Flujo de Caja'!AH2:AH${tail+1}),-MIN('Flujo de Caja'!AH2:AH${tail+1}))`,'Cero salvo redondeo. Identidad de principal, IVA, ingresos y egresos.'],
 ['Desfase inicio E-25 frente a H12',`=${pd(17)}-SUMIF('Hitos E25'!A2:A13,"H12",'Hitos E25'!C2:C13)`,'Cero en el caso contractual.'],
 ['Último lote externo',`=MAXIFS('Instalación por lote'!A2:A21,'Instalación por lote'!D2:D21,">0")`,'Calendario presupuestado M7-M9; confirmar ventanas y stock.'],
 ['Inventario externo restante',`=${pc(63)}-B9`,'Cero en base; positivo durante reasignación, negativo indica exceso.'],
);
write('Control de entrega',controls);

// Resumen Ejecutivo presenta el escenario realmente activo, no valores copiados.
S('Resumen Ejecutivo').getRange('A1:F30').clear({applyTo:'contents'});
write('Resumen Ejecutivo',[
 ['audIT / Transportes Curimón','Informe 3 · versión 3.1','Unidad'],
 ['Costo neto',`=SUM(Costos!K2:K57)/${pd(21)}`,'UF'],['Venta neta',`=SUM(Ingresos!E2:E57)/${pd(21)}`,'UF'],
 ['Margen EBITDA',`=Indicadores!B10`,'%'],['VAN M1-M56',`=Indicadores!B2/${pd(21)}`,'UF'],['TIR mensual',`=Indicadores!B3`,'%'],
 ['Caja mínima base',`=MIN('Flujo de Caja'!W2:W57)/${pd(21)}`,'UF tesorería'],['Línea máxima base',`=Indicadores!B5/${pd(21)}`,'UF'],
 ['Capital inicial',`=${pd(4)}/${pd(21)}`,'UF total'],['Banco inicial',`=${pd(4)}*${pd(5)}/${pd(21)}`,'UF'],['Socios inicial',`=${pd(4)}*(1-${pd(5)})/${pd(21)}`,'UF'],
 ['Atraso H5 M13 déficit',`=Sensibilidad!J2/${pd(21)}`,'UF tras línea'],['Atraso combinado déficit',`=Sensibilidad!J4/${pd(21)}`,'UF tras línea'],['Facilidad contingente',`=${pc(28)}/${pd(21)}`,'UF condicionados'],
 ['Cola de cobro posterior a M56',`=Indicadores!B8/${pd(21)}`,'UF netos'],['Tratamiento','Supuestos de presupuesto identificados; sin beneficios hipotéticos en cobros de audIT.',''],
 ['Soporte','Base al 100%; escalones de madurez sujetos a medición y aprobación.',''],['Financiamiento','E-24: 80% banco, 20% socios. Comisiones y plazos presupuestados.','']]);
for(const sn of ['Criterios y pendientes','Cotejo D1','Escenarios de caja','Capacidad por perfil','Refuerzo presupuestado'])S(sn).delete();
// Formato de nuevas hojas y de los resultados de cierre.
for(const sn of [...nuevos,'Sensibilidad','Resumen Ejecutivo']){
 const s=S(sn);const u=s.getUsedRange();u.format.font={name:'Arial',size:10};u.format.rowHeight=21;u.format.verticalAlignment='center';
 const cols=Math.min(21,u.columnCount||21);s.getRange('A:A').format.columnWidth=27;s.getRange('B:U').format.columnWidth=18;
 s.getRange('A1:U1').format.fill='#0F2A43';s.getRange('A1:U1').format.font={name:'Arial',size:10,bold:true,color:'#FFFFFF'};
 s.getRange('A1:U1').format.rowHeight=42;s.getRange('A1:U1').format.wrapText=true;
 u.setNumberFormat('#,##0.00;(#,##0.00);–');s.showGridLines=false;
}
S('Parámetros corrección').getRange('A:A').format.columnWidth=50;S('Parámetros corrección').getRange('C:C').format.columnWidth=100;
S('Parámetros corrección').getRange('B2:B77').format.font={name:'Arial',size:10,color:'#0000FF'};
S('Tarifas por perfil').getRange('J:J').format.columnWidth=95;S('Soporte por perfil').getRange('J:J').format.columnWidth=100;
S('Dotación por perfil').getRange('C:C').format.columnWidth=60;S('Dotación por perfil').getRange('L:L').format.columnWidth=100;
S('Instalación por lote').getRange('L:L').format.columnWidth=100;S('Resumen Ejecutivo').getRange('A:A').format.columnWidth=35;
S('Resumen Ejecutivo').getRange('B:B').format.columnWidth=26;S('Resumen Ejecutivo').getRange('C:C').format.columnWidth=30;
S('Resumen Ejecutivo').getRange('B4').setNumberFormat('0.00%');S('Resumen Ejecutivo').getRange('B6').setNumberFormat('0.00%');
S('Resumen Ejecutivo').getRange('B5').setNumberFormat('#,##0.00');S('Resumen Ejecutivo').getRange('B7').setNumberFormat('#,##0.00');
S('Resumen Ejecutivo').getRange('C4').values=[['']];S('Resumen Ejecutivo').getRange('C6').values=[['']];
S('RESUMEN').getRange('G21').setNumberFormat('"CLP "0');
S('Control de entrega').getRange('A:A').format.columnWidth=43;S('Control de entrega').getRange('C:C').format.columnWidth=95;
S('Control de entrega').getRange('B6').setNumberFormat('0.00%');S('Control de entrega').getRange('B7:B10').setNumberFormat('0');
S('Control de entrega').getRange('B14').setNumberFormat('0.00%');S('Control de entrega').getRange('B17').setNumberFormat('0');S('Control de entrega').getRange('B19').setNumberFormat('0.00%');
S('Instalación por lote').getRange('A:A').format.columnWidth=8;S('Instalación por lote').getRange('B:B').format.columnWidth=23;
S('Instalación por lote').getRange('A2:A21').setNumberFormat('0');S('Instalación por lote').getRange('C2:D21').setNumberFormat('0');
for(const [sn,range] of [['Tarifas por perfil','B2:I20'],['Contrato de soporte','B2:D13'],['Sensibilidad','B2:F8']])S(sn).getRange(range).format.font={name:'Arial',size:10,color:'#0000FF'};
for(const range of ['B4','B28'])S('Parámetros corrección').getRange(range).dataValidation={rule:{type:'decimal',operator:'between',formula1:0,formula2:2000000000}};
S('Parámetros corrección').getRange('B12:B15').dataValidation={rule:{type:'decimal',operator:'between',formula1:0,formula2:1}};
S('Tarifas por perfil').getRange('B2:B20').dataValidation={rule:{type:'decimal',operator:'between',formula1:1,formula2:1000000}};
S('Tarifas por perfil').getRange('C2:I20').dataValidation={rule:{type:'decimal',operator:'between',formula1:0,formula2:100}};
S('Contrato de soporte').getRange('B2:C13').dataValidation={rule:{type:'decimal',operator:'between',formula1:0,formula2:2000}};
S('Sensibilidad').getRange('N2:N8').setNumberFormat('0.00%');
S('Parámetros corrección').getRange('B9').setNumberFormat('0.0%');S('Parámetros corrección').getRange('B12:B16').setNumberFormat('0.0%');
S('Parámetros corrección').getRange('B35').setNumberFormat('0.00%');
S('Parámetros corrección').getRange('B43').dataValidation={rule:{type:'list',values:['0','1']}};
const whole=(sn,address,min,max)=>{
 S(sn).getRange(address).dataValidation={rule:{type:'whole',operator:'between',formula1:min,formula2:max}};
};
whole('Parámetros D2','B16:B17',1,56);
whole('Parámetros corrección','B36',0,tail-horizon);
whole('Parámetros corrección','B38:B41',0,baseline.kits);
whole('Parámetros corrección','B67:B69',0,baseline.kits);
S('Ajustes de operación').getRange('B2:C57').dataValidation={rule:{type:'decimal',operator:'greaterThanOrEqual',formula1:0}};
whole('Parámetros corrección','B62',0,1);
whole('Parámetros corrección','B70',0,1);
whole('Parámetros corrección','B72:B76',1,horizon);
whole('Parámetros corrección','B77',1,36);
for(const r of [59,70])S('Parámetros corrección').getRange(`B${r}`).setNumberFormat('0.00%');
S('Parámetros corrección').getRange('B59').dataValidation={rule:{type:'decimal',operator:'between',formula1:0,formula2:1}};
S('Parámetros D2').getRange('B13').dataValidation={rule:{type:'whole',operator:'between',formula1:12,formula2:14}};
wb.recalculate();
console.log((await wb.inspect({kind:'table',range:'Resumen Ejecutivo!A1:C15',tableMaxRows:15,tableMaxCols:3,maxChars:3000})).ndjson);
console.log((await wb.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#NUM!',options:{useRegex:true,maxResults:20},maxChars:1500})).ndjson);
await (await SpreadsheetFile.exportXlsx(wb)).save(O+'/revision/modelo-borrador-v4.xlsx');
console.log('Modelo exportado');
process.exit(0);
function write(sn,rows){const width=Math.max(...rows.map(r=>r.length));const padded=rows.map(r=>[...r,...Array(width-r.length).fill(null)]);
 const sheet=S(sn);sheet.getRangeByIndexes(0,0,padded.length,width).values=padded.map(r=>r.map(v=>typeof v==='string'&&v.startsWith('=')?null:v));
 for(let i=0;i<padded.length;i++){const formulas=padded[i].map(v=>typeof v==='string'&&v.startsWith('=')?v:null);if(formulas.some(Boolean))
  for(let j=0;j<formulas.length;j++)if(formulas[j])sheet.getCell(i,j).formulas=[[formulas[j]]];}
}
