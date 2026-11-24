import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath,pathToFileURL} from 'node:url';
import {Presentation,PresentationFile} from '@oai/artifact-tool';
const root=fileURLToPath(new URL('../../..',import.meta.url));
const out=path.join(root,'outputs/informe3-mejora');
const skill=process.env.AUDIT_SLIDES_SKILL;
if(!skill)throw new Error('Define AUDIT_SLIDES_SKILL con la ruta de la guía de presentaciones.');
const {applyPresentationChartFont,finalizePresentation}=await import(pathToFileURL(path.join(skill,'container_tools/artifact_tool_utils.mjs')));
const m=JSON.parse(await fs.readFile(path.join(out,'revision/resultados.json'),'utf8'));
const d=JSON.parse(await fs.readFile(path.join(out,'revision/series.json'),'utf8'));
const p=Presentation.create({slideSize:{width:1280,height:720}});
const navy='#0F2A43', teal='#087968', orange='#B65B33', gray='#526170',font='Liberation Sans';
const n=(x,dec=0)=>new Intl.NumberFormat('es-CL',{minimumFractionDigits:dec,maximumFractionDigits:dec}).format(x);
const uf=(x,dec=0)=>n(x/40000,dec);
function text(sl,t,x,y,w,h,size=28,color=navy,bold=false){
 const s=sl.shapes.add({geometry:'textbox',position:{left:x,top:y,width:w,height:h},fill:'none',line:{fill:'none',width:0}});
 s.text=t;s.text.style={fontSize:size,typeface:font,color,bold,autoFit:'none',insets:0,wrap:'square'};return s;
}
function slide(title,subtitle=''){
 const s=p.slides.add();s.background.fill='#FFFFFF';
 text(s,'audIT  /  TRANSPORTES CURIMÓN',64,29,1050,28,17,teal,true);
 text(s,title,64,84,1148,90,42,navy,true);
 if(subtitle)text(s,subtitle,64,179,1148,65,24,gray);
 text(s,'TFEP-01/2026  ·  Informe 3  ·  15 noviembre 2026',64,674,1050,25,15,gray);
 text(s,String(p.slides.items.length).padStart(2,'0'),1168,672,50,28,18,gray);
 return s;
}
function table(s,values,widths,y=260,height=310,size=24){
 const t=s.tables.add({rows:values.length,columns:values[0].length,left:64,top:y,width:1152,height,columnWidths:widths,values});
 t.borders.assign({fill:'#D4DEE4',width:.6,style:'solid'});
 for(let r=0;r<values.length;r++)for(let c=0;c<values[0].length;c++){
  let cell=t.getCell(r,c);cell.fill=r===0?navy:(r%2===0?'#F1F5F7':'#FFFFFF');
  cell.text.style={fontSize:size,typeface:font,color:r===0?'#FFFFFF':navy,bold:r===0,insets:12,verticalAlignment:'middle'};
 }
 return t;
}
const categories=Array.from({length:56},(_,i)=>String(i+1));
function chart(s,type,series,y=244,height=350,barOptions,months=categories){
 const palette=[navy,teal,orange,'#8B97A5'];
 let ch=s.charts.add(type,{position:{left:70,top:y,width:1140,height},categories:months,
  series:series.map(([name,values],i)=>({name,smooth:false,values:values.map(x=>Number((x/40000).toFixed(2))),fill:palette[i],line:{fill:palette[i],width:2.5}})),
  lineOptions:{smooth:false},
  hasLegend:true,legend:{position:'bottom',textStyle:{fontSize:20}},
  xAxis:{textStyle:{fontSize:14},title:{text:'Mes contractual',textStyle:{fontSize:20}}},
  yAxis:{numberFormatCode:'0',textStyle:{fontSize:18},title:{text:'UF',textStyle:{fontSize:20}},majorGridlines:{fill:'#DCE4E8',width:.7}},barOptions});
 applyPresentationChartFont(ch,{fontFamily:font});return ch;
}
function note(s,source,minutes,script){s.speakerNotes.text=`Tiempo previsto: ${minutes} min. ${script}\nFuente: ${source}. Planilla INFORME3_AUDIT_PLANILLA_20261115.xlsx. UF presupuestaria E-24 = CLP 40.000; USD = CLP 900. Cifras netas salvo caja de tesorería. Asistencia de IA alta; validación humana según declaración del informe.`;}
{
 const s=slide('Costos, venta y continuidad','Oferta de audIT Soluciones Tecnológicas SpA');
 text(s,'56 meses',64,306,1000,100,76,navy,true);
 text(s,'Implementación por etapas y 36 meses de operación',64,428,1050,60,32);
 text(s,'Presupuesto en UF  ·  Modelo mensual y escenarios de liquidez',64,537,1050,60,26,teal);
 note(s,'T-22; E-24; E-25',.5,'Presentar alcance y unidades. La exposición completa prevé 15 minutos, incluida demostración de dos minutos.');
}
{
 const s=slide('Magnitudes de la oferta','Valores netos del modelo corregido, en UF');
 const rows=[['Costo total',uf(m.costo_clp)],['Venta total',uf(m.venta_clp)],['VAN del proyecto',uf(m.van_clp)]];
 for(let i=0;i<3;i++){text(s,rows[i][0],64,270+i*105,480,60,30,gray);text(s,rows[i][1],620,255+i*105,580,85,58,navy,true);}
 text(s,`Margen EBITDA ${n(m.margen*100,2)}%  ·  Tasa ${n(m.tasa_mensual*100,4)}% mensual`,64,592,1148,45,24,teal);
 note(s,'RESUMEN!C8 y H8; Indicadores!B2, B3 y B10; tasa de descuento del modelo',1,'Costo total y venta del mismo corte. La TIR base es '+n(m.tir_mensual*100,4)+'% mensual, no anual; escenarios de atraso tienen múltiples raíces. Priorizar VAN y liquidez. Último cobro M57 conciliado fuera del VAN de 56 meses.');
}
{
 const s=slide('Compras y montaje por lote','El servicio externo termina en M9; los 182 kits incluyen 34 comodatos');
 table(s,[['Periodo','Trabajo','Responsable / término'],['M1–M5','Diseño, compras y preparación','audIT y proveedores de plataforma'],['M6','10 kits piloto','Equipo interno; validación en terminal'],['M7 / M8 / M9','60 / 60 / 52 kits','Proveedor de montaje; recepción por lote'],['M10–M21','Integración y aceptación de etapas','audIT conserva banco, QA y analista']],[190,430,532],258,302,24);
 text(s,`172 montajes externos: ${uf(d.montajeNeto,2)} UF netas; 401 h 20 min de montaje sustituible. Se mantiene la nómina.`,64,594,1150,52,23,teal);
 note(s,'Instalación por lote; Dotación por perfil; Caso, capítulo 10, pp.23–24; Art.73',1.5,'Precio presupuestado: 140 min por kit a costo técnico, 15% coordinación e insumos, CLP300.000 por visita a terminal regional y lote. No es cotización confirmada. Mantener consentimiento del dueño, montaje en terminal y congelamiento diciembre–abril. Autorización escrita y límite agregado40% antes de subcontratar. Contrastar 164 previstos por S7 en M9 con 182 de la hipótesis; se requieren 18 adhesiones y visitas adicionales. Se conserva la nómina hasta acreditar ahorro.');
}
{
 const s=slide('Egresos mensuales','La concurrencia de perfiles y las adquisiciones explican los picos');
 chart(s,'bar',[['Personal',d.personal],['Infraestructura y licencias',d.infra],['Otros y pagos puntuales',d.otros]],240,365,{direction:'column',grouping:'stacked',overlap:100,gapWidth:25});
 text(s,'Personal, infraestructura y pagos puntuales explican los cambios de pendiente.',64,615,1140,45,23,teal);
 note(s,'Costos!A2:K57; Dotación por perfil; estimación de horas por perfil',1,'Mostrar picos de implementación y paso a operación M21. Las compras del mandante quedan informativas fuera del flujo de audIT. No se fabrica una pendiente mensual suave.');
}
const ahorroMadurez=d.operativo.at(-1)-d.madurezOperativo.at(-1);
for(const [titulo,costo,caja,pie,fuente,minutos,guion] of [
 ['Curva S del presupuesto base',d.operativo,d.cajaApertura,
  `Brecha mínima frente al costo en M${d.brecha}. En M${d.finDeuda} se devuelve el principal.`,
  'Gráficos UF!P:S',1.5,'Vista de solvencia y tesorería con capital inicial en M0. A diferencia de la curva contractual E-21 (que parte de cero y sólo computa pagos de Curimón), la facturación ajustada suma el capital de trabajo antes del primer egreso de M1 y descuenta intereses, comisión y amortización del crédito en M21.'],
 ['Curva S con soporte por madurez',d.madurezOperativo,d.madurezCajaApertura,
  `El costo acumulado baja ${uf(ahorroMadurez,2)} UF desde M25 en este escenario.`,
  'Sensibilidad!A15; Escenarios corregidos',.75,'El escenario aplica los escalones de madurez al trabajo variable y mantiene la cobertura fija, el precio y el calendario de cobros.'],
]){
 const s=slide(titulo,`Facturación ajustada y caja parten de ${uf(caja[0])} UF en M0`);
 chart(s,'line',[['Facturación ajustada por financiamiento',d.ajustada],['Costo operativo acumulado',costo],['Caja financiada neta',caja]],240,348,undefined,
  Array.from({length:57},(_,i)=>String(i)));
 text(s,pie,64,608,1140,46,23,teal);
 note(s,fuente,minutos,guion);
}
{
 const s=slide('Atrasos de H4 y H5','Caja de tesorería con financiamiento presupuestado');
 chart(s,'line',[['Base',d.cajaBase],['H5 M14 + reserva, sin facilidad',d.cajaEstres],['Mismo estrés, con facilidad',d.cajaCubierta],['H4 M11 sin línea',d.cajaH4]],240,350);
 text(s,`Cota previa a cobros en H4: ${uf(d.cotaH4)} UF. Facilidad presupuestada: ${uf(m.facilidad_contingente_clp)} UF.`,64,605,1140,59,23,teal);
 note(s,'Sensibilidad; Escenarios corregidos; Flujo de Caja!AG',1.5,'Comparar atraso de cobro frente a atraso del acta. La facilidad M9 o M12 requiere disponibilidad antes del gasto. La cota previa a cobros se evalúa por separado de los cierres y de los giros mensuales.');
}
{
 const s=slide('Préstamo, socios y amortización',`Capital inicial ${uf(m.capital_inicial_clp)} UF: ${uf(m.capital_inicial_clp*.8)} UF banco y ${uf(m.capital_inicial_clp*.2)} UF socios`);
 chart(s,'bar',[['Banco',d.banco],['Aporte socios',d.socios],['Amortización',d.amort.map(x=>-x)]],245,350,{direction:'column',grouping:'stacked',overlap:100,gapWidth:30});
 text(s,`Banco 0,9% mensual  ·  Amortiza desde M21 hasta M${d.finDeuda}  ·  Línea base: cero`,64,610,1140,48,24,teal);
 note(s,'Financiamiento; Flujo de Caja!P, U, V, AB, AC, AD; Parámetros corrección!B3:B5',1,'El capital inicial se redimensionó desde la versión previa para cubrir la secuencia conservadora de pagos antes de cobros y piso500UF. Comisión presupuestada250mil. El saldo de apertura determina interés. No hay devolución a socios. Diferenciar crédito base de la facilidad eventual.');
}
{
 const s=slide('Soporte y cobertura de mesa','Presupuesto con carga completa hasta demostrar madurez');
 table(s,[['Tramo','Factor variable','Personal / mes, UF'],['M21','100%',uf(d.soporte[0],2)],['M25–M32','100%',uf(d.soporte[4],2)],['M33–M44','100%',uf(d.soporte[12],2)],['M45–M56','100%',uf(d.soporte[24],2)]],[360,360,432],252,285,26);
 text(s,'Escalones de 75%, 50% y 25% sujetos a demanda, capacidad y SLA.',64,563,1140,45,26,teal);
 text(s,'Mesa 24×7, reserva de suplencia y guardia: respuesta 15 min; resolución 4 h.',64,611,1140,45,23,gray);
 note(s,'Contrato de soporte; Soporte por perfil; Personal!D22:D57; Art.78.2',1.5,'M22–M24 difieren ligeramente deM21 por cierre de arquitectura y frontend: ver detalle del libro. Datos y QA tienen refuerzo hastaM24. No se reduce fabricanteD4 por esta curva. Si fallan umbrales, conservar factor previo y recalcular. Disponibilidad99,9% exige continuidad, no basta resolver en225min.');
}
{
 const s=slide('Costo y valor de cinco innovaciones','El personal atribuido ya está en nómina; no se agrega otra vez al costo');
 table(s,[['Innovación','Personal UF','Egreso directo UF','Cómo verificar valor'],...d.innovaciones.map(r=>[r[0],uf(r[1],1),uf(r[2],1),r[3]])],[360,190,220,382],242,326,21);
 text(s,'Beneficio incremental monetario reconocido en base: cero; las hipótesis se miden antes de valorarlas.',64,594,1150,64,23,teal);
 note(s,'Innovaciones!A2:G6; Atribución innovaciones; Beneficios Curimón; Costos!L',2,'INN1firma; INN2patio; INN3acople y registro térmico separados del kilometraje obligatorio; INN4recupero bruto no es ingreso deaudIT ni beneficio neto; INN5fatiga, no catálogo deparadores. Montajescomodatos dentro182. DesarrolloINN3eINN5incorporado. Hipótesis de capacidadINN1 yrecuperoINN4 no son ahorro observado.');
}
{
 const s=slide('Demostración de desconexión y reconexión','Prototipo de interfaz; sus contadores no acreditan un SLA productivo');
 text(s,'1   Portal Clientes',64,280,1140,58,34,navy,true);
 text(s,'2   Simulador Operativo en Vivo',64,358,1140,58,34,navy,true);
 text(s,'3   Simular pérdida de cobertura y restablecerla',64,436,1140,72,34,navy,true);
 const link=text(s,'Abrir prototipo audIT',64,565,1140,56,30,teal,true);
 link.text.get('Abrir prototipo audIT').link={uri:'https://carlosabarza.github.io/PaginaAudIT/',isExternal:true};
 note(s,'https://carlosabarza.github.io/PaginaAudIT/; T-17',2,'La compilación local distingue contadores simulados de mediciones. La URL enlaza al despliegue previo. No mostrar datos personales del apartadoequipo ni presentar certificados o contratos ficticios como respaldo real. El ensayo productivo decontinuidad se exige antesH5. Cerrar recordando presupuesto y alcance de liquidez.');
}
await fs.mkdir(path.join(out,'revision/slides'),{recursive:true});
for(let i=0;i<p.slides.items.length;i++){
 const blob=await p.export({slide:p.slides.items[i],format:'png',scale:2});
 await fs.writeFile(path.join(out,`revision/slides/slide-${String(i+1).padStart(2,'0')}.png`),new Uint8Array(await blob.arrayBuffer()));
}
const candidatePath=path.join(out,'revision/presentacion-candidata.pptx');
await(await PresentationFile.exportPptx(p)).save(candidatePath);
const SKILL=skill;
const result=await finalizePresentation({workspaceDir:root,candidatePath,finalPath:path.join(out,'entrega/INFORME3_AUDIT_PRESENTACION_20261115.pptx'),
 pythonExecutable:process.env.AUDIT_PYTHON || '/usr/bin/python3',integrityValidatorPath:path.join(SKILL,'container_tools/inspect_presentation_package_integrity.py'),
 layoutValidatorPath:path.join(SKILL,'container_tools/inspect_presentation_layout_geometry.py'),
 layoutArgs:['--expected-slide-size-emu','12192000,6858000','--validate-bullet-geometry','--validate-heading-fit',...[3,9,10].flatMap(x=>['--require-native-table-slide',String(x)])],
 explicitTotalSlideCount:11,requiredNativeTableOwnerSlides:[3,9,10],requiredNativeChartOwnerSlides:[4,5,6,7,8],materializeLiteralChartWorkbooks:true,
 fontPolicy:{basis:'design',families:[font]},verifyArtifactToolImport:true,receiptPath:path.join(out,'revision/presentacion-validacion.json')});
console.log(JSON.stringify(result));process.exit(0);
