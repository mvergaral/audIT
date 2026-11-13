import path from "node:path";
import { createRequire } from "node:module";
import { pathToFileURL } from "node:url";

const require = createRequire(path.join(process.env.D2_NODE_MODULES, "..", "package.json"));
const { FileBlob, SpreadsheetFile } = await import(pathToFileURL(require.resolve("@oai/artifact-tool")).href);
const [plantilla, modelo, salida] = process.argv.slice(2);
if (!plantilla || !modelo || !salida) throw new Error("Uso: node integrar_resumen_mandante.mjs plantilla.xlsx modelo.xlsx salida.xlsx");
const wb = await SpreadsheetFile.importXlsx(await FileBlob.load(plantilla));
const d2 = await SpreadsheetFile.importXlsx(await FileBlob.load(modelo));
const costs = d2.worksheets.getItem("Costos").getRange("A2:L57").values;
const parameters = d2.worksheets.getItem("Parámetros").getRange("B14:B16").values.flat();
const fx = wb.worksheets.getItem("PARÁMETROS");
const uf = fx.getRange("B6").values[0][0];
if (uf !== 40000 || fx.getRange("B4").values[0][0] !== 900) throw new Error("Tipos de cambio incompatibles");
const implementation = costs.slice(0, 20);
const operation = costs.slice(20);
const sum = (rows, index) => rows.reduce((total, row) => total + Number(row[index] ?? 0), 0);
const guarantee = sum(costs, 9);
const groups = [
  sum(implementation, 6),
  sum(implementation, 1),
  sum(implementation, 3),
  sum(implementation, 8) - sum(implementation, 6) - sum(implementation, 1) - sum(implementation, 3) + guarantee,
  sum(operation, 6),
  sum(operation, 8) - sum(operation, 6),
];
const bridge = wb.worksheets.add("PUENTE D2");
bridge.getRange("A1:D7").values = [
  ["Grupo del Resumen","Costo CLP","Costo UF","Tarifa UF"],
  ...groups.map((value,i)=>[[
    "Implementación RRHH","Implementación adquisiciones","Implementación capacitaciones",
    "Implementación servicios","Soporte RRHH","Soporte servicios",
  ][i],value,null,null]),
];
bridge.getRange("A10:B16").values = [
  ["Precio implementación CLP",parameters[0]],
  ["Precio operación CLP",parameters[1]*parameters[2]],
  ["UF contractual",uf],
  ["Versión modelo","D2_MODELO_TRABAJO.xlsx · escenario de 96991e8"],
  ["Clasificación","M1–M20 implementación, M21–M56 soporte. Garantía se atribuye a implementación."],
  ["Alcance","Copia de integración de Resumen. El calendario y la Fila A válidos para revisión están en el modelo D2."],
  ["VAN y TIR","Pendientes de resultados validados por D1 sobre la Fila A de cierre."],
];
bridge.getRange("C2:D7").formulas = groups.map((_,i)=>{
  const row=i+2;
  return [`=B${row}/$B$12`,i<4?`=C${row}*$B$10/SUM(B2:B5)`:i===4?"=$B$11/$B$12-C7":"=C7"];
});
bridge.getRange("A:A").format.columnWidth=34;
bridge.getRange("B:D").format.columnWidth=22;
bridge.getRange("B2:D7").setNumberFormat("#,##0.00");
const cost = wb.worksheets.getItem("COSTOS DE OPERACION");
const tariff = wb.worksheets.getItem("TARIFAS DE OPERACION");
const net = wb.worksheets.getItem("FLUJO DE CAJA NETO");
const complete = wb.worksheets.getItem("FLUJO DE CAJA COMPLETO");
const formula = (sheet, cell, value) => { sheet.getRange(cell).formulas=[[value]]; };
for(const [cell,row] of [["V35",2],["V45",4],["AL35",6]]){
  formula(cost,cell,`='PUENTE D2'!C${row}`);
  formula(tariff,cell,`='PUENTE D2'!D${row}`);
}
formula(tariff,"B47","='PUENTE D2'!B10/SUM('PUENTE D2'!B2:B5)-1");
for(const range of ["C33:BB33","B35:AL35"]){
  const sheetRange=net.getRange(range);
  sheetRange.values=[Array(range.startsWith("C")?52:37).fill(null)];
}
formula(net,"C33","=-'PUENTE D2'!C3");
formula(net,"B35","=-'PUENTE D2'!C5");
formula(net,"O35","=-'PUENTE D2'!C7");
formula(complete,"B23",'=""');
formula(complete,"B26",'=""');
const summary = wb.worksheets.getItem("RESUMEN");
wb.recalculate();
for(const [cell,expected] of [
  ["C6",groups.slice(0,4).reduce((a,b)=>a+b,0)],
  ["C7",groups[4]+groups[5]],
  ["H6",parameters[0]],["H7",parameters[1]*parameters[2]],
]){
  const actual=summary.getRange(cell).values[0][0];
  if(typeof actual!=="number"||Math.abs(actual-expected)>.01) throw new Error(`${cell}: ${actual} vs ${expected}`);
}
const result = await SpreadsheetFile.exportXlsx(wb);
await result.save(salida);
