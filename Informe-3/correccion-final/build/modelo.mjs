import fs from 'node:fs/promises';
import {FileBlob,SpreadsheetFile} from '@oai/artifact-tool';
const R='/home/axeler8/Escritorio/audIT', D=R+'/Informe-3/correccion-final', O=R+'/outputs/informe3-corregido';
const ins=JSON.parse(await fs.readFile(D+'/insumos.json','utf8'));
const wb=await SpreadsheetFile.importXlsx(await FileBlob.load(D+'/build/origen.xlsx'));
const S=n=>wb.worksheets.getItem(n), F=(s,c,v)=>S(s).getRange(c).formulas=[[v]], V=(s,c,v)=>S(s).getRange(c).values=[[v]];
const q=n=>`'${n}'!`, pc=r=>`${q('Parámetros corrección')}$B$${r}`, pd=r=>`${q('Parámetros D2')}$B$${r}`;
const add=n=>{const s=wb.worksheets.add(n);s.showGridLines=false;s.freezePanes.freezeRows(1);return s;};
const nuevos=['Parámetros corrección','Tarifas por perfil','Dotación por perfil','Instalación por lote','Soporte por perfil','Contrato de soporte','Hitos E25','Escenarios corregidos','Atribución innovaciones','Control de entrega','Gráficos UF'];
nuevos.forEach(add);
const param=[
 ['Parámetro','Valor','Fuente y criterio'],
 ['Horas de referencia por FTE y mes',160,'T-15. Capacidad bruta; no son horas netas de programación.'],
 ['Piso de caja CLP',20000000,'Supuesto de tesorería: 500 UF. Complemento a financiación de contingencias.'],
 ['Capital inicial total CLP',Number(process.env.CAPITAL_BASE||450000000),'Entrada dimensionada con base neta y tesorería; banco 80%, socios 20%.'],
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
 ['Financiamiento contingente total CLP',Number(process.env.PUENTE_ESTRES||400000000),'Facilidad presupuestaria 80/20 adicional en M12; condición financiera de la oferta.'],
 ['Comisión bancaria CLP',250000,'Supuesto de presupuesto del instrumento; pagada M1.'],
 ['Comisión contingencia CLP',250000,'Supuesto, se aplica únicamente al activar la facilidad.'],
 ['Mes desembolso contingencia',12,'Antes de egresos del mes crítico; disponibilidad condicionada.'],
 ['Mes amortización contingencia',16,'Tras H5 y H7, conservando el piso.'],
 ['Control cierre SLA respuesta min',15,'FEP01 Art.78.2 p.40.'],
 ['Control cierre SLA resolución min',240,'FEP01 Art.78.2 p.40.'],
 ['Disponibilidad crítica mínima',0.999,'FEP01 Art.78.2 p.40.'],
 ['Base contractual de pago operativo: desfase',1,'E-25: cobro al mes siguiente vencido.'],
 ['Mes piloto',6,'10 equipos, San Bernardo.'],
 ['Nº kits piloto',10,'Incluidos en los 182 montajes; no se duplican.'],
 ['Nº kits externos M7',60,'Agenda por cinco terminales, 12 por terminal.'],
 ['Nº kits externos M8',60,'Agenda por cinco terminales, 12 por terminal.'],
 ['Nº kits externos M9',52,'San Bernardo 12; otros terminales 10 cada uno.'],
 ['Mes final montaje externo',9,'Pago y término de servicio por lote; no hay costo recurrente de montaje.'],
 ['Línea habilitada base 0/1',0,'Base sin línea. Las sensibilidades conservan tope E-24 de CLP50 millones.'],
 ['Horas de preparación CP-SEC-05',72,'Alcance registrado por D3; incluido en la demanda mensual, no se suma nuevamente.'],
 ['Mes cierre de observación económica',56,'Horizonte E-24; M57 solo cobra la última factura de operación.'],
 ['Viajes anuales de referencia',96000,'FEP03, numeral 14.1 p.29.'],
 ['Minutos por expediente evitables',2,'Hipótesis de INN1 para sensibilidad de capacidad, no ahorro contractual.'],
 ['Costo de oportunidad CLP/h',6000,'Hipótesis de valorización de capacidad de Curimón; no cobro de audIT.'],
 ['Adopción INN1',0.5,'Hipótesis; sólo cuenta el universo con expediente verificable.'],
 ['Recupero anual INN4 CLP',120700000,'Insumo D2, recupero bruto bajo supuesto 50% del monto objetado.'],
 ['Meses de régimen beneficios',36,'Operación M21-M56; no se suman estos beneficios a ventas audIT.'],
 ['Balizas base a montar',210,'Caso14.1 y D4 4.1. Las 21 de stock no se montan al alta inicial.'],
 ['Minutos montaje por baliza',15,'Estimación D4, no medición.'],
 ['Meses montaje balizas',3,'M7-M9, 70 unidades por mes; ventanas por terminal.'],
 ['Lectores de portería',5,'D4 4.9: uno por terminal, hardware del mandante.'],
 ['Horas por lector de portería',2,'Supuesto de instalación y prueba dentro de Electrónica en M5-M6.'],
 ];
S('Parámetros corrección').getRange(`A1:C${param.length}`).values=param;
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
const ih=[['Mes','Terminal','Kits piloto','Kits externos','Horas técnico externo','Horas banco audIT','Horas analista audIT','Neto servicio CLP','IVA CLP','Pago bruto CLP','Costo interno evitable CLP','Estado y ventana']];
for(let m=6;m<=9;m++)for(const [i,t] of ['San Bernardo','Antofagasta','Talca','Los Ángeles','Puerto Montt'].entries()){
 const pilot=m===6&&i===0?10:0;const ext=m===6?0:m===9?(i===0?12:10):12;const r=ih.length+1;
 ih.push([m,t,m===6&&i===0?`=${pc(38)}`:0,m===6?0:m===9?`=INT(${pc(41)}/(${pc(11)}+1))+IF(B${r}="San Bernardo",MOD(${pc(41)},${pc(11)}+1),0)`:`=${pc(m===7?39:40)}/(${pc(11)}+1)`,`=D${r}*${pc(6)}/60`,`=(C${r}+D${r})*${pc(7)}/60`,`=(C${r}+D${r})*${pc(8)}/60`,
 `=E${r}*${q('Tarifas por perfil')}$B$16*(1+${pc(9)})+IF(D${r}>0,IF(B${r}="San Bernardo",0,${pc(10)}),0)`,
 `=H${r}*${pd(11)}`,`=SUM(H${r}:I${r})`,`=E${r}*${q('Tarifas por perfil')}$B$16`,'Presupuesto: visita normal habilitada; 140 min de puesto. Art.73, autorización previa al lote.']);
}
write('Instalación por lote',ih);
const dh=[['Mes','Perfil','EDT / actividad','FTE referencia','Horas brutas','Demanda D3 h','Horas adicionales','Horas montaje sustituidas','Horas internas contratadas','CLP/h','Costo CLP','Criterio']];
const mapa={'Arquitectura':'B','Liderazgo desarrollo':'C','Software':'D','Frontend':'E','Seguridad':'F','Datos':'G','QA':'H','SRE':'I'};
for(let m=1;m<=20;m++)for(let j=0;j<perfiles.length;j++){
 let tramo=m<=2?2:m<=5?3:m<=9?4:m<=12?5:m<=17?6:m===18?7:8;const r=dh.length+1,tr=j+2;
 const perfil=perfiles[j][0];const rr=m+1;
 dh.push([m,perfil,perfiles[j][9],`=${q('Tarifas por perfil')}${String.fromCharCode(65+tramo)}${tr}`,`=D${r}*${pc(2)}`,
 mapa[perfil]?`=${q('Dedicación D3')}${mapa[perfil]}${rr}`:perfil==='Técnico de campo'&&m>=7&&m<=9?`=SUMIF('Instalación por lote'!$A$2:$A$21,A${r},'Instalación por lote'!$E$2:$E$21)+SUMIF('Instalación por lote'!$A$2:$A$21,A${r},'Instalación por lote'!$F$2:$F$21)+${pc(52)}*${pc(53)}/60/${pc(54)}`:0,
 `=MAX(0,F${r}-E${r})`,perfil==='Técnico de campo'?`=SUMIF('Instalación por lote'!$A$2:$A$21,A${r},'Instalación por lote'!$E$2:$E$21)`:0,
 `=MAX(0,E${r}+G${r}-H${r})`,`=${q('Tarifas por perfil')}B${tr}`,`=I${r}*J${r}`,
 'Base por rol + brecha D3; resta montaje operativo externalizado. El resto conserva tareas propias.']);
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
 sh.push([m,a[0],`='Contrato de soporte'!B${sr}`,`='Contrato de soporte'!C${sr}`,`=${pc(factor)}`,m<=24?(a[0].startsWith('Datos')?66:a[0].startsWith('QA')?37:a[0].startsWith('Arquitectura')?Number(ins.demanda.find(d=>+d.mes===m).arquitectura):a[0].startsWith('Frontend')?Number(ins.demanda.find(d=>+d.mes===m).frontend):0):0,
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
V('Parámetros D2','B4',450000000);F('Parámetros D2','B4',`=${pc(4)}`);V('Parámetros D2','C4','Capital base corregido. Fuente: Parámetros corrección.');
V('Parámetros D2','B33',250000);V('Parámetros D2','C33','Comisión presupuestada, ver Parámetros corrección.');
// El modelo conserva los precios calculados desde costos base cuando se prueba un atraso.
const h=[['Hito','Etapa','Mes factura','% implementación','Mes cobro base','Mes cobro prueba','Monto neto CLP','Criterio']];
for(const [m,id,p] of ins.hitos){const r=h.length+1;h.push([id,+id.slice(1)<=7?1:2,m,p,m,`=IF(A${r}="H5",${pd(13)},E${r})`,`=D${r}*${pd(14)}`,'Facturación condicionada a acta conforme Art.18; mes contractual E-25.']);}
write('Hitos E25',h);
for(let m=1;m<=57;m++){
 const r=m+1,prev=r-1;
 F('Flujo de Caja',`B${r}`,`=IF(COUNTIF('Hitos E25'!$C$2:$C$13,A${r})=0,"",INDEX('Hitos E25'!$A$2:$A$13,MATCH(A${r},'Hitos E25'!$C$2:$C$13,0)))`);
 F('Flujo de Caja',`C${r}`,`=SUMIF('Hitos E25'!$C$2:$C$13,A${r},'Hitos E25'!$D$2:$D$13)`);
 F('Flujo de Caja',`E${r}`,`=SUMIF('Hitos E25'!$C$2:$C$13,A${r},'Hitos E25'!$G$2:$G$13)+IF(AND(A${r}>=21,A${r}<=56),${pd(15)}+D${r},0)`);
 F('Flujo de Caja',`F${r}`,`=SUMIF('Hitos E25'!$F$2:$F$13,A${r},'Hitos E25'!$G$2:$G$13)+IF(AND(A${r}>=22,A${r}<=57),${pd(15)}+D${prev},0)`);
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
 F('Flujo de Caja',`AE${r}`,`=H${r}/(1+${pd(10)})^A${r}`);F('Flujo de Caja',`AF${r}`,`=SUM($AE$2:AE${r})`);
 for(const [c,expr] of [['B',injection],['C',`AC${r}`],['D',`AB${r}`],['E',`P${r}`],['F',`Q${r}`],['G',`R${r}`],['H',`S${r}`],['I',`T${r}`],['J',`U${r}`],['K',`V${r}`],['L',`W${r}`]])F('Financiamiento',`${c}${r}`,`=${c==='B'?expr:`'Flujo de Caja'!${expr}`}`);
}
S('Flujo de Caja').getRange('Y1:AF1').values=[['Antes línea y amortización','IVA acumulado','Caja neta sin IVA','Banco desembolsado','Aporte socios','Comisión banco','Flujo descontado','Acumulado descontado']];
V('Flujo de Caja','AG1','Cota pagos antes de cobros');
V('Financiamiento','C1','Aporte socios');V('Financiamiento','D1','Crédito bancario');
F('Indicadores','B7',`=SUMPRODUCT((COUNTIF(Proveedores!A2:A281,Proveedores!A2:A281)>1)*1)`);
F('Indicadores','B14',`=IF(MIN('Flujo de Caja'!AF2:AF57)>=0,1,LOOKUP(2,1/('Flujo de Caja'!AF2:AF57<0),'Flujo de Caja'!A2:A57)+1)`);
V('Indicadores','B9','Base corregida 3.0; ver condiciones y controles');
F('Indicadores','B15',`=MIN('Flujo de Caja'!AA2:AA57)`);V('Indicadores','A15','Caja mínima neta sin IVA');
// Sensibilidades simultáneas: se conserva la arquitectura de escenarios del modelo original,
// con un cálculo explícito de cada movimiento; todos los resultados se expresan con fórmulas.
const cases=[['Atraso H5 M13',13,0,0,0,0],['Atraso H5 M14',14,0,0,0,0],['H5 M14 + reserva M12',14,12,0,0,0],
 ['H5 M14 + reserva + facilidad',14,12,1,0,0],['Costos +5%',12,0,0,0.05,0],['Cobros -5%',12,0,0,0,0.05],['Reserva anticipada M9',14,9,1,0,0]];
S('Sensibilidad').getRange('A1:Z500').clear({applyTo:'contents'});
const ss=[['Escenario','Mes cobro H5','Mes reserva','Activar facilidad','Shock costo','Shock ingreso','Caja mínima CLP','Mes mínimo','Línea máxima CLP','Déficit residual CLP','Interés línea CLP','Interés banco CLP','VAN Fila A CLP','TIR mensual','Aporte socios CLP','Banco desembolsado CLP','Saldo deuda M57']];
const er=[['Escenario','Mes','Factura neta','Cobro neto','Costo base','Reserva / shock','Fila A','Capital inicial','Capital contingente','Interés banco','Interés línea','IVA neto caja','Antes giro','Giro línea','Pago línea','Saldo línea','Pago banco','Saldo banco','Caja cierre','Fila C','Flujo descontado','Cota antes de cobros']];
for(let ci=0;ci<cases.length;ci++){
 const cr=ci+2,start=er.length+1,end=start+56;const ca=cases[ci];
 ss.push([...ca,`=MIN('Escenarios corregidos'!S${start}:S${end})`,`=INDEX('Escenarios corregidos'!B${start}:B${end},MATCH(G${cr},'Escenarios corregidos'!S${start}:S${end},0))`,
 `=MAX('Escenarios corregidos'!P${start}:P${end})`,`=MAX(0,-G${cr})`,`=SUM('Escenarios corregidos'!K${start}:K${end})`,`=SUM('Escenarios corregidos'!J${start}:J${end})`,
 `=NPV(${pd(10)},'Escenarios corregidos'!G${start}:G${end-1})`,`=IRR('Escenarios corregidos'!G${start}:G${end-1},0.1)`,
 `=SUM('Escenarios corregidos'!H${start}:I${end})*(1-${pd(5)})`,`=SUM('Escenarios corregidos'!H${start}:I${end})*${pd(5)}`,`='Escenarios corregidos'!R${end}`,
 ci<=3?'Flujo no convencional: comprobar raíces; priorizar VAN y liquidez.':'Semilla TIR 0,1; comparar con VAN.',`=MIN('Escenarios corregidos'!V${start}:V${end})`]);
 for(let m=1;m<=57;m++){
  const r=er.length+1,pr=r-1,br=m+1;const cash=m===1?'0':`S${pr}`,bank=m===1?'0':`R${pr}`,line=m===1?'0':`P${pr}`;
  const hit=`SUMIF('Hitos E25'!$E$2:$E$13,B${r},'Hitos E25'!$G$2:$G$13)`;
  const h5=`SUMIF('Hitos E25'!$A$2:$A$13,"H5",'Hitos E25'!$G$2:$G$13)`;
  er.push([ca[0],m,`='Flujo de Caja'!E${br}`,`=(${hit}+IF(B${r}=Sensibilidad!$B$${cr},${h5},0)-IF(B${r}=12,${h5},0)+IF(AND(B${r}>=22,B${r}<=57),${pd(15)},0))*(1-Sensibilidad!$F$${cr})`,
   `='Flujo de Caja'!G${br}`,`=IF(B${r}=Sensibilidad!$C$${cr},${pc(26)},0)+E${r}*Sensibilidad!$E$${cr}`,`=D${r}-E${r}-F${r}`,`=IF(B${r}=1,${pd(4)},0)`,
   `=IF(AND(Sensibilidad!$D$${cr}=1,B${r}=IF(Sensibilidad!$C$${cr}=9,9,${pc(31)})),${pc(28)},0)`,`=${bank}*${pd(6)}`,`=${line}*${pd(7)}`,
   `=('Flujo de Caja'!O${br}+(D${r}-'Flujo de Caja'!F${br})*${pd(11)})*${pd(12)}`,
   `=${cash}+G${r}+H${r}+I${r}+L${r}-J${r}-K${r}-IF(B${r}=1,${pc(29)},0)-IF(I${r}>0,${pc(30)},0)`,
   `=MIN(MAX(0,${pd(8)}-${line}),MAX(0,-M${r}))`,`=MIN(${line},MAX(0,M${r}-${pc(3)}))`,`=${line}+N${r}-O${r}`,
   `=IF(B${r}>=${pc(32)},IF(B${r}<${pc(5)},MIN(MAX(0,${bank}-${pd(4)}*${pd(5)}),MAX(0,M${r}+N${r}-O${r}-${pc(3)})),MIN(${bank},MAX(0,M${r}+N${r}-O${r}-${pc(3)}))),0)`,
   `=${bank}+(H${r}+I${r})*${pd(5)}-Q${r}`,`=M${r}+N${r}-O${r}-Q${r}`,`=S${r}-${cash}`,`=G${r}/(1+${pd(10)})^B${r}`,`=M${r}-D${r}*(1+${pd(11)}*${pd(12)})`]);
 }
}
ss[0].push('Criterio de TIR','Cota pagos antes de cobros CLP');write('Sensibilidad',ss);write('Escenarios corregidos',er);
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
const gr=[['Mes','Costo acumulado UF','Facturación acumulada UF','Caja neta financiada UF','Costos mensuales UF','Caja tesorería UF','Cero UF','Banco UF','Socios UF','Amortización UF']];
for(let m=1;m<=56;m++){const r=m+1;gr.push([`M${m}`,`='Curva S'!B${r}/${pd(21)}`,`='Curva S'!C${r}/${pd(21)}`,`='Curva S'!D${r}/${pd(21)}`,`=Costos!K${r}/${pd(21)}`,
 `='Flujo de Caja'!W${r}/${pd(21)}`,0,`='Flujo de Caja'!AB${r}/${pd(21)}`,`='Flujo de Caja'!AC${r}/${pd(21)}`,`='Flujo de Caja'!U${r}/${pd(21)}`]);}write('Gráficos UF',gr);
S('Curva S').charts.deleteAll();S('Gráficos UF').charts.deleteAll();
for(const [title,cols,place,type] of [['Curva S (UF)',['A1:A57','B1:B57','C1:C57','D1:D57'],['L2','AC21'],'line'],['Egresos mensuales (UF)',['A1:A57','E1:E57'],['L23','AC42'],'bar'],
 ['Caja y cero (UF)',['A1:A57','D1:D57','F1:F57','G1:G57'],['L44','AC63'],'line'],['Banco, socios y amortización (UF)',['A1:A57','H1:H57','I1:I57','J1:J57'],['L65','AC84'],'bar']]){
 const s=S('Gráficos UF');const chart=s.charts.add(type,cols.map(c=>s.getRange(c)));chart.title=title;chart.setPosition(...place);
 chart.titleTextStyle.typeface='Arial';chart.titleTextStyle.fontSize=14;chart.xAxis={axisType:'textAxis',textStyle:{typeface:'Arial',fontSize:10}};
 chart.yAxis={numberFormatCode:'#,##0',numberFormatSourceLinked:false,textStyle:{typeface:'Arial',fontSize:10}};chart.legend={position:'bottom',textStyle:{typeface:'Arial',fontSize:10}};
}
const controls=[['Comprobación','Resultado','Criterio'],['Caja mínima tesorería',"=MIN('Flujo de Caja'!W2:W57)",'Debe superar cero y el piso presupuestado'],
 ['Caja mínima neta',"=MIN('Flujo de Caja'!AA2:AA57)",'Vista neta de las aclaraciones'],['Giros de línea base',"=SUM('Flujo de Caja'!R2:R57)",'Debe ser cero'],['Saldo máximo línea base',"=MAX('Flujo de Caja'!T2:T57)",'Debe ser cero'],
 ['Porcentajes E25',"=SUM('Hitos E25'!D2:D13)",'Debe ser uno'],['Número de hitos',"=COUNTA('Hitos E25'!A2:A13)",'Debe ser doce'],['Facturas de operación',36,'M21-M56; cobros M22-M57'],
 ['Kits totales',"=SUM('Instalación por lote'!C2:D21)",'Debe ser 182'],['Kits externos',"=SUM('Instalación por lote'!D2:D21)",'Debe ser 172'],
 ['Costo menos Cuadro maestro',"=SUM(Costos!K2:K57)-'Cuadro maestro'!C19",'Debe ser cero'],['Ventas menos Cuadro maestro',"=SUM(Ingresos!E2:E57)-'Cuadro maestro'!D19",'Debe ser cero'],
 ['Saldo bancario M57',"='Flujo de Caja'!V58",'Debe ser cero'],['Margen EBITDA',"=Indicadores!B10",'No supera 20%'],['Diferencia RESUMEN costo',"=RESUMEN!C8-SUM(Costos!K2:K57)",'Debe ser cero'],
 ['Diferencia RESUMEN venta',"=RESUMEN!H8-SUM(Ingresos!E2:E57)",'Debe ser cero'],['H5 factura M12',"=SUMIF('Hitos E25'!A2:A13,\"H5\",'Hitos E25'!C2:C13)",'Debe ser doce'],
 ['Costo de montaje posterior M9',"=SUMIF('Instalación por lote'!A2:A21,\">9\",'Instalación por lote'!H2:H21)",'Debe ser cero'],
 ['Reducción soporte variable',`=${pc(12)}-${pc(15)}`,'Factor sujeto a métricas; el fijo no cambia'],['Fuente de cierre','3.0 / 14-11-2026','Base corregida; presupuesto y condiciones de oferta'],
 ['Cota base: pagos antes de cobros',"=MIN('Flujo de Caja'!AG2:AG57)",'Cobertura conservadora antes de cobrar; evita inventar fechas dentro del mes']];write('Control de entrega',controls);
// Resumen Ejecutivo presenta el escenario realmente activo, no valores copiados.
S('Resumen Ejecutivo').getRange('A1:F30').clear({applyTo:'contents'});
write('Resumen Ejecutivo',[
 ['audIT / Transportes Curimón','Informe 3 · versión 3.0','Unidad'],
 ['Costo neto',`=SUM(Costos!K2:K57)/${pd(21)}`,'UF'],['Venta neta',`=SUM(Ingresos!E2:E57)/${pd(21)}`,'UF'],
 ['Margen EBITDA',`=Indicadores!B10`,'%'],['VAN M1-M56',`=Indicadores!B2/${pd(21)}`,'UF'],['TIR mensual',`=Indicadores!B3`,'%'],
 ['Caja mínima base',`=MIN('Flujo de Caja'!W2:W57)/${pd(21)}`,'UF tesorería'],['Línea máxima base',`=Indicadores!B5/${pd(21)}`,'UF'],
 ['Capital inicial',`=${pd(4)}/${pd(21)}`,'UF total'],['Banco inicial',`=${pd(4)}*${pd(5)}/${pd(21)}`,'UF'],['Socios inicial',`=${pd(4)}*(1-${pd(5)})/${pd(21)}`,'UF'],
 ['Atraso H5 M13 déficit',`=Sensibilidad!J2/${pd(21)}`,'UF tras línea'],['Atraso combinado déficit',`=Sensibilidad!J4/${pd(21)}`,'UF tras línea'],['Facilidad contingente',`=${pc(28)}/${pd(21)}`,'UF condicionados'],
 ['Cola de cobro M57',`='Flujo de Caja'!F58/${pd(21)}`,'UF netos'],['Tratamiento','Supuestos de presupuesto identificados; sin beneficios hipotéticos en cobros de audIT.',''],
 ['Soporte','Reducción variable condicionada a SLA y backlog; la cobertura fija se conserva.',''],['Financiamiento','E-24: 80% banco, 20% socios. Comisiones y plazos presupuestados.','']]);
for(const sn of ['Criterios y pendientes','Cotejo D1','Escenarios de caja','Capacidad por perfil','Refuerzo presupuestado']){
 V(sn,'A1','Referencia de insumo anterior (no es el escenario corregido)');
 V(sn,'A2','La versión vigente se calcula en Personal, Dotación por perfil, Soporte por perfil y Sensibilidad.');
}
// Formato de nuevas hojas y de los resultados de cierre.
for(const sn of [...nuevos,'Sensibilidad','Resumen Ejecutivo']){
 const s=S(sn);const u=s.getUsedRange();u.format.font={name:'Arial',size:10};u.format.rowHeight=21;u.format.verticalAlignment='center';
 const cols=Math.min(21,u.columnCount||21);s.getRange('A:A').format.columnWidth=27;s.getRange('B:U').format.columnWidth=18;
 s.getRange('A1:U1').format.fill='#0F2A43';s.getRange('A1:U1').format.font={name:'Arial',size:10,bold:true,color:'#FFFFFF'};
 s.getRange('A1:U1').format.rowHeight=42;s.getRange('A1:U1').format.wrapText=true;
 u.setNumberFormat('#,##0.00;(#,##0.00);–');s.showGridLines=false;
}
S('Parámetros corrección').getRange('A:A').format.columnWidth=50;S('Parámetros corrección').getRange('C:C').format.columnWidth=100;
S('Parámetros corrección').getRange('B2:B56').format.font={name:'Arial',size:10,color:'#0000FF'};
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
