import fs from "node:fs/promises";
import path from "node:path";
import { createRequire } from "node:module";
import { execFileSync } from "node:child_process";
import { fileURLToPath, pathToFileURL } from "node:url";

const require = createRequire(path.join(process.env.D2_NODE_MODULES, "..", "package.json"));
const { Workbook, SpreadsheetFile } = await import(pathToFileURL(require.resolve("@oai/artifact-tool")).href);
const folder = path.dirname(fileURLToPath(import.meta.url));
const wb = Workbook.create();
const flujo = wb.worksheets.add("Flujo de Caja");
const parametros = wb.worksheets.add("Parámetros");
const costos = wb.worksheets.add("Costos");
const proveedores = wb.worksheets.add("Proveedores");
const personal = wb.worksheets.add("Personal");
const innovaciones = wb.worksheets.add("Innovaciones");
const curva = wb.worksheets.add("Curva S");
const indicadores = wb.worksheets.add("Indicadores");
const dedicacion = wb.worksheets.add("Dedicación D3");

async function read(name, range) {
  const source = await Workbook.fromCSV(await fs.readFile(path.join(folder,name),"utf8"),{sheetName:"CSV"});
  return source.worksheets.getItem("CSV").getRange(range).values;
}
function init(sheet, headers, widths) {
  sheet.getRangeByIndexes(0,0,1,headers.length).values = [headers];
  const top = sheet.getRangeByIndexes(0,0,1,headers.length);
  top.format.fill = "#173650";
  top.format.font.color = "#FFFFFF";
  top.format.font.bold = true;
  top.format.rowHeight = 24;
  widths.forEach((width,i)=>{sheet.getRangeByIndexes(0,i,1,1).format.columnWidth = width;});
}
function data(sheet, rows, start=1) {
  sheet.getRangeByIndexes(start,0,rows.length,rows[0].length).values = rows;
}
function formulas(sheet,start,col,rows) {
  sheet.getRangeByIndexes(start,col,rows.length,rows[0].length).formulas = rows;
}
const raw = await read("AUD-17_FLUJO_INTEGRADO_PROVISIONAL.csv","A2:Z57");
const demandCsv = execFileSync("git",["show","4070a7e:Informe-3/d3/datos/dedicacion_mensual_d3_resumen.csv"],{cwd:folder,encoding:"utf8"});
const demandBook = await Workbook.fromCSV(demandCsv,{sheetName:"Demanda"});
const demand = demandBook.worksheets.getItem("Demanda").getRange("A2:J54").values;
const e25 = await read("AUD-18_CALENDARIO_INGRESOS_E25.csv","A2:J49");
const hit = new Map(e25.filter(r=>r[0]==="implementacion").map(r=>[Number(r[4]),[r[2],Number(r[6])/100]]));
init(parametros,["Parámetro","Valor","Criterio"],[39,18,86]);
data(parametros,[
 ["Margen objetivo",.185,"AUD-20. Precio de escenario calculado desde los costos."],
 ["Comisión correcto funcionamiento",.0015,"E-24 y Art. 37. 5 % × 1,5 % anual × 2 años."],
 ["Capital inicial",260413654,"Escenario publicado. Editar para simular otra disponibilidad."],
 ["Fracción bancaria",.8,"E-24. El resto corresponde a aporte propio."],
 ["Tasa bancaria mensual",.009,"E-24"],
 ["Tasa de línea mensual",.03,"E-24"],
 ["Tope línea",50000000,"E-24"],
 ["Costo capital propio anual",.2,"AUD-20"],
 ["Tasa de descuento mensual",null,"Ponderación banco y socios."],
 ["IVA",.19,"E-24. Aplicar solo a bases identificadas."],
 ["Activar IVA de caja (0/1)",0,"Escenario de referencia sin IVA. Al activar, completar bases y usar el calendario fiscal."],
 ["Mes de cobro H5",12,"Mover a 13 para sensibilidad. Su facturación contractual sigue en M12."],
 ["Precio implementación",null,"Costo M1–M20 más comisión de correcto funcionamiento."],
 ["Mensualidad operación",null,"Costo M21–M56 dividido en 36 mensualidades, con margen."],
 ["Meses operación",36,"E-25"],
 ["Inicio operación",21,"E-25. Coincide con H12."],
 ["Meses por año",12,"Conversión efectiva de tasas."],
]);
parametros.getRange("B10").formulas=[["=B5*B6+(1-B5)*((1+B9)^(1/B18)-1)"]];
parametros.getRange("B14:B15").formulas=[["=SUM(Costos!I2:I21)/(1-B2-B3)"],["=SUM(Costos!I22:I57)/(1-B2)/B16"]];
for(const address of ["B2:B3","B5:B7","B9:B11"]) parametros.getRange(address).setNumberFormat("0.000%");

init(proveedores,["ID mensual","Mes","Bloque","Pagador","CLP netos","Fuente","IVA pagado","Crédito fiscal"],[19,9,24,17,19,49,16,17]);
const ivaEquipo = new Map([[1,1852500],[3,15751217],[4,3548341]]);
const vendor = raw.flatMap(r=>{
 const month=Number(r[0]);
 const ivaD4=(ivaEquipo.get(month)??0)+(month>=4?12760:0);
 const firma=month<13?0:month<=15?73950:600840;
 const ivaFirma=month<13?0:month<=15?14050:114160;
 return [
 [`D4-M${month}`,month,"Base D4","audIT",Number(r[2]),"AUD-37 / IVA parcial: equipos y SIM 5G",ivaD4||null,null],
 [`D3-M${r[0]}`,Number(r[0]),"Licencias D3","audIT",Number(r[3]),"AUD-26 / GitLab y SonarQube",null,null],
 [`D1-M${r[0]}`,Number(r[0]),"Calidad D1","audIT",Number(r[4]),"AUD-10 / calidad y capacitación",null,null],
 [`MAND-M${r[0]}`,Number(r[0]),"Equipos del mandante","Curimón",Number(r[8]),"D4-143 / compras informativas",null,null],
 [`FEA-M${month}`,month,"Firma automática","audIT",firma,"4070a7e / ecert, estimación D3 por analogía",ivaFirma||null,null],
 ];
});
data(proveedores,vendor);
proveedores.getRange("E2:E281").setNumberFormat("#,##0");
proveedores.getRange("G2:H281").format.fill="#FFF1CE";

init(dedicacion,["Mes","Arquitectura","Liderazgo","Software","Frontend","Seguridad","Datos","QA","SRE","Horas D3","FTE nominal"],[9,...Array(10).fill(15)]);
data(dedicacion,demand.map(r=>r.map(Number)));
dedicacion.getRange("A57").values=[["Demanda D3 (4070a7e). 160 h/FTE nominal. Las horas no representan disponibilidad ni costo incremental."]];

init(personal,["Mes","Dotación escenario","Ajuste confirmado","Costo integrado","Fuente / criterio"],[10,24,23,23,65]);
data(personal,raw.map(r=>[Number(r[0]),Number(r[7]),null,null,"AUD-17_FLUJO_DE_CAJA.xlsx · escenario mensual, pendiente de conciliación"]));
formulas(personal,1,3,raw.map((_,i)=>[`=SUM(B${i+2}:C${i+2})`]));
personal.getRange("C2:C57").format.fill="#FFF1CE";
personal.getRange("B2:D57").setNumberFormat("#,##0");
personal.getRange("A60:F63").values=[
 ["Perfil","Horas","Costo CLP/h","Costo atribuible","Tratamiento","Fuente"],
 ["Seguridad D1",8,44000,null,"Dentro de reserva 10.1/G13","D1 ff1389e"],
 ["Técnico D4",5,16000,null,"Dentro de reserva 10.1/G13","AUD-14 / D4"],
 ["Operación/SRE D4",2,32000,null,"Dentro de reserva 10.1/G13","AUD-14 / D4"],
];
formulas(personal,60,3,[["=B61*C61"],["=B62*C62"],["=B63*C63"]]);
personal.getRange("A65:E65").values=[["Preparación D3",72,null,null,"4.1/A11 · cobertura incremental pendiente"]];

init(innovaciones,["Innovación","Componente","Referencia CLP","Tratamiento","Fuente"],[13,32,22,64,45]);
data(innovaciones,[
 [1,"Implementación atribuible, 480 h",14816000,"Dentro de EDT 12.1. No se suma al costo de personal.","4070a7e / D3"],
 [1,"Soporte atribuible, 492 h",16072000,"M16–M56. Adicional solo por déficit de cobertura.","4070a7e / D3"],
 [1,"Firma automática, neto",24856290,"Integrado en Proveedores, M13–M56. Estimación D3.","4070a7e / D3"],
 [1,"Nube atribuible",132000,"Asignación dentro del presupuesto Azure D4.","4070a7e / D3"],
 [4,"Instalación y 12 meses de conectividad",550583,"Referencia por alta adicional. Cantidad pendiente.","AUD-21 / insumos D4"],
 [4,"Hardware por kit",900001,"Costo del mandante por alta adicional.","AUD-21 / insumos D4"],
 [4,"Soporte por mes",9000,"Costo unitario. Cobertura y pagador pendientes.","AUD-21 / insumos D4"],
 [4,"Recupero bruto anual",120700000,"Escenario de Curimón. Reparto pendiente.","AUD-21"],
]);
innovaciones.getRange("C2:C9").setNumberFormat("#,##0");
innovaciones.getRange("A12:D16").values=[
 ["Mes de alta","Altas adicionales","Soporte externo (meses)","Criterio"],
 [null,null,null,"Cupo adicional sin comprometer hasta acreditar capacidad posterior a los 182 montajes base."],
 ["Alta audIT",null,null,"Instalación más 12 meses de conectividad por alta."],
 ["Hardware mandante",null,null,"Información del mandante, fuera de la caja audIT."],
 ["Soporte audIT",null,null,"Presupuesto de sensibilidad si audIT asume el pago."],
];
formulas(innovaciones,13,1,[["=IF(ISNUMBER(B13),B13*C6,\"\")"],["=IF(ISNUMBER(B13),B13*C7,\"\")"],["=IF(AND(ISNUMBER(B13),ISNUMBER(C13)),B13*C13*C8,\"\")"]]);

init(costos,["Mes","Base D4","Licencias","Calidad","Administración","Cierre","Personal","Otros confirmados","Base de precio","Comisión garantía","Egreso neto","Firma automática"],[8,17,17,17,17,17,17,20,18,19,18,19]);
data(costos,raw.map(r=>[Number(r[0]),null,null,null,Number(r[5]),Number(r[6]),null,null,null,null,null]));
formulas(costos,1,1,raw.map((_,i)=>{
 const row=i+2, first=2+i*5;
 return [`=Proveedores!E${first}`,`=Proveedores!E${first+1}`,`=Proveedores!E${first+2}`];
}));
formulas(costos,1,6,raw.map((_,i)=>{
 const r=i+2;
 return [`=Personal!D${r}`,null,`=SUM(B${r}:H${r},L${r})`,`=IF(A${r}='Parámetros'!$B$17,'Parámetros'!$B$14*'Parámetros'!$B$3,0)`,`=SUM(I${r}:J${r})`,`=Proveedores!E${6+i*5}`];
}));
costos.getRange("H2:H57").format.fill="#FFF1CE";
costos.getRange("B2:K57").setNumberFormat("#,##0");

init(flujo,["Mes","Hito","% hito","Variable neto","Facturación","Cobros netos","Costos netos","Fila A","IVA débito","IVA cobrado","IVA pagado","Crédito fiscal","IVA por pagar","Crédito arrastre","IVA neto caja","Interés banco","Interés línea","Giro línea","Pago línea","Saldo línea","Pago banco","Saldo banco","Caja acumulada","Fila C"],[8,9,10,16,...Array(20).fill(17)]);
data(flujo,Array.from({length:57},(_,i)=>[i+1,hit.get(i+1)?.[0]??null,hit.get(i+1)?.[1]??null,null]));
flujo.getRange("C2:C58").setNumberFormat("0%");
flujo.getRange("D2:D57").format.fill="#FFF1CE";
formulas(flujo,1,4,Array.from({length:57},(_,i)=>{
 const m=i+1,r=i+2,p=r-1, v=2+i*5;
 const bank=i?`V${p}`:"0", line=i?`T${p}`:"0", cash=i?`W${p}`:"0", credit=i?`N${p}`:"0";
 const param="'Parámetros'!", initial=i?"0":`${param}$B$4`;
 const available=`(${cash}+H${r}+O${r}+${initial}-P${r}-Q${r})`;
 return [
 `=C${r}*${param}$B$14+IF(AND(A${r}>=${param}$B$17,A${r}<${param}$B$17+${param}$B$16),${param}$B$15+D${r},0)`,
 `=IF(B${r}="H5",0,C${r}*${param}$B$14)+IF(A${r}=${param}$B$13,$C$13*${param}$B$14,0)+${i>=21?`${param}$B$15+D${p}`:"0"}`,
 m<=56?`=Costos!K${r}`:"=0",`=F${r}-G${r}`,
 `=E${r}*${param}$B$11`,`=F${r}*${param}$B$11`,
 m<=56?`=SUM(Proveedores!G${v}:G${v+2},Proveedores!G${v+4})`:"=0",
 m<=56?`=SUM(Proveedores!H${v}:H${v+2},Proveedores!H${v+4})`:"=0",
 `=MAX(0,I${r}-L${r}-${credit})`,`=MAX(0,${credit}+L${r}-I${r})`,
 `=${param}$B$12*(J${r}-K${r}-${i?`M${p}`:"0"})`,
 `=${bank}*${param}$B$6`,`=${line}*${param}$B$7`,
 `=MAX(0,MIN(${param}$B$8-${line},-${available}))`,
 `=MIN(${line},MAX(0,${available}))`,`=${line}+R${r}-S${r}`,
 `=IF(A${r}>=${param}$B$17,MIN(${bank},MAX(0,${available}+R${r}-S${r})),0)`,
 `=${bank}+${initial}*${param}$B$5-U${r}`,
 `=${available}+R${r}-S${r}-U${r}`,`=W${r}-${cash}`];
}));
flujo.getRange("D2:X58").setNumberFormat("#,##0;[Red](#,##0);–");
init(curva,["Mes","Costos con intereses","Facturación","Caja financiada"],[10,24,21,22]);
formulas(curva,1,0,raw.map((_,i)=>{
 const r=i+2,f="'Flujo de Caja'!";
 return [`=${f}A${r}`,`=SUM(${f}G$2:G${r},${f}P$2:Q${r})`,`=SUM(${f}E$2:E${r})`,`=${f}W${r}`];
}));
curva.getRange("B2:D57").setNumberFormat("#,##0");
const chart=curva.charts.add("line",curva.getRange("A1:D57"));
chart.title="Curva S · escenario D2";
chart.setPosition("F2","Q24");

init(indicadores,["Control o indicador","Resultado","Criterio"],[38,20,72]);
data(indicadores,[
 ["VAN",null,"Fila A M1–M56. M0 = 0."],
 ["TIR mensual",null,"Fila A M1–M56. Escenario provisional."],
 ["VAN con M57",null,"Sensibilidad con cobro neto efectivo en M57."],
 ["Mayor uso de línea",null,"Debe respetar el tope E-24."],
 ["Caja mínima",null,"Valor negativo indica déficit sin cubrir."],
 ["IDs duplicados",null,"Cero es el resultado esperado."],
 ["Cobro M57",null,"Reconciliación posterior al horizonte."],
 ["Estado","Provisional","Personal e innovaciones por conciliar. Hoja Resumen del mandante pendiente."],
]);
const f="'Flujo de Caja'!",p="'Parámetros'!";
formulas(indicadores,1,1,[
 [`=NPV(${p}B10,${f}H2:H57)`],[`=IRR(${f}H2:H57,0.8)`],
 [`=NPV(${p}B10,${f}H2:H58)`],[`=MAX(${f}T2:T57)`],[`=MIN(${f}W2:W57)`],
 ["=SUMPRODUCT(--(COUNTIF(Proveedores!A2:A281,Proveedores!A2:A281)>1))"],[`=${f}F58`],
]);
indicadores.getRange("B2:B8").setNumberFormat("#,##0;[Red](#,##0);–");
indicadores.getRange("B3").setNumberFormat("0.00%");
wb.recalculate();
const get=(s,a)=>s.getRange(a).values[0][0];
for(const [s,cell,expected] of [[indicadores,"B7",0],[dedicacion,"J7",3354.2]]){
 const actual=get(s,cell);
 if(typeof actual!=="number"||Math.abs(actual-expected)>.01) throw new Error(`${s.name}!${cell}: ${actual} vs ${expected}`);
}
parametros.getRange("B13").values=[[13]];
wb.recalculate();
if(get(flujo,"F13")!==0 || get(flujo,"F14")<=0) throw new Error("No pasó sensibilidad H5");
parametros.getRange("B13").values=[[12]];
const originalVan=get(indicadores,"B2");
personal.getRange("C2").values=[[1000000]];
wb.recalculate();
if(Math.abs(get(indicadores,"B2")-originalVan)<1) throw new Error("Personal no alimenta VAN");
personal.getRange("C2").values=[[null]];
parametros.getRange("B12").values=[[1]];
proveedores.getRange("G2:H2").values=[[1000000,1000000]];
wb.recalculate();
if(Math.abs(get(flujo,"O2")+1000000)>.01 || Math.abs(get(flujo,"N2")-1000000)>.01) {
 throw new Error("IVA pagado y crédito fiscal no alimentan caja");
}
parametros.getRange("B12").values=[[0]];
proveedores.getRange("G2:H2").values=[[1852500,null]];
wb.recalculate();
const signatureTotal=costos.getRange("L2:L57").values.flat().reduce((a,b)=>a+b,0);
if(signatureTotal!==24856290) throw new Error("Total de firma incorrecto");
console.log(JSON.stringify({firma:signatureTotal,van:get(indicadores,"B2"),cajaMinima:get(indicadores,"B6")}));
const out = await SpreadsheetFile.exportXlsx(wb);
await out.save(process.argv[2]);
