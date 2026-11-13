import path from "node:path";
import { createRequire } from "node:module";
import { pathToFileURL } from "node:url";

const [input, output] = process.argv.slice(2);
if (!input || !output || !process.env.D2_NODE_MODULES) {
  throw new Error("Uso: D2_NODE_MODULES=<node_modules> node aplicar_controles_modelo.mjs entrada.xlsx salida.xlsx");
}
const require = createRequire(path.join(process.env.D2_NODE_MODULES, "..", "package.json"));
const { FileBlob, SpreadsheetFile } = await import(pathToFileURL(require.resolve("@oai/artifact-tool")).href);
const workbook = await SpreadsheetFile.importXlsx(await FileBlob.load(input));
const sheets = workbook.worksheets;
const params = "'Parámetros D2'!";
const flow = "'Flujo de Caja'!";
const put = (sheet, address, value) => {
  const range = sheet.getRange(address);
  if (typeof value === "string" && value.startsWith("=")) range.formulas = [[value]];
  else range.values = [[value]];
};
function header(sheet, labels, widths) {
  const range = sheet.getRangeByIndexes(0, 0, 1, labels.length);
  range.values = [labels];
  range.format.fill = "#173650";
  range.format.font.color = "#FFFFFF";
  range.format.font.bold = true;
  range.format.rowHeight = 25;
  widths.forEach((width, index) => {
    sheet.getRangeByIndexes(0, index, 1, 1).format.columnWidth = width;
  });
}
function inputRange(sheet, address, rule) {
  sheet.getRange(address).format.fill = "#FFF1CE";
  sheet.dataValidations.add({ range: address, rule });
}
const nonnegative = { type: "decimal", operator: "greaterThanOrEqual", formula1: 0 };
const parameters = sheets.getItem("Parámetros D2");
const adjustments = sheets.items.find(sheet => sheet.name === "Ajustes de operación")
  ?? sheets.add("Ajustes de operación");
header(adjustments, ["Mes de servicio", "Variable CLP", "Descuento CLP", "Fuente"], [17, 20, 20, 46]);
adjustments.getRange("A2:D57").values = Array.from({ length: 56 }, (_, i) =>
  [i + 1, 0, 0, "Base sin ajuste"]);
inputRange(adjustments, "B22:B57", nonnegative);
inputRange(adjustments, "C22:C57", {
  type: "custom", formula1: "AND(ISNUMBER(C22),C22>=0,C22<=B22+MensualidadBase)",
});
workbook.names.add("MensualidadBase", "='Parámetros D2'!$B$15");
adjustments.getRange("D22:D57").format.fill = "#FFF1CE";
adjustments.getRange("B2:C57").setNumberFormat("#,##0");
put(adjustments, "A59", "Editar desde M21 y consignar la fuente. Se factura por mes de servicio y se cobra al mes siguiente.");

parameters.getRange("A32:C34").values = [
  ["Desfase de cobro de operación", 1, "E-25. Mes siguiente al servicio vencido."],
  ["Comisión incremental del crédito de estrés", 0, "CLP. Se modela en cero hasta confirmar el instrumento."],
  ["Mes de pago de la comisión en estrés", 1, "Mes provisional. Confirmar con el instrumento."],
];
inputRange(parameters, "B33", nonnegative);
inputRange(parameters, "B34", { type: "whole", operator: "between", formula1: 1, formula2: 56 });
put(parameters, "C9", "Supuesto del costo de capital propio. El 20 % efectivo anual se convierte a mensual antes de ponderar.");

const cashFlow = sheets.getItem("Flujo de Caja");
const personnel = sheets.getItem("Personal");
for (let row = 2; row <= 58; row++) {
  const month = "A" + row;
  const service = month + "-" + params + "$B$32";
  const adjustmentMonths = "'Ajustes de operación'!$A$2:$A$57";
  put(cashFlow, "D" + row, "=SUMIF(" + adjustmentMonths + "," + month + ",'Ajustes de operación'!$B$2:$B$57)"
    + "-SUMIF(" + adjustmentMonths + "," + month + ",'Ajustes de operación'!$C$2:$C$57)");
  put(cashFlow, "F" + row, '=IF(B' + row + '="H5",0,C' + row + "*" + params + "$B$14)"
    + "+IF(" + month + "=" + params + '$B$13,SUMIF($B$2:$B$58,"H5",$C$2:$C$58)*' + params + "$B$14,0)"
    + "+IF(AND(" + service + ">=" + params + "$B$17," + service + "<" + params + "$B$17+" + params + "$B$16),"
    + params + "$B$15+SUMIF($A$2:$A$58," + service + ",$D$2:$D$58),0)");
  if (row < 58 && personnel.getRange("C" + row).formulas[0][0]?.includes("Refuerzo presupuestado")) {
    put(personnel, "C" + row, "=SUMIF('Refuerzo presupuestado'!$A$2:$A$48,A" + row
      + ",'Refuerzo presupuestado'!$E$2:$E$48)");
  }
}
const sensitivity = sheets.getItem("Sensibilidad");
for (const [result, scenario] of [["C3", "B"], ["C4", "C"]]) {
  put(sensitivity, result, '=IFERROR(IRR(' + scenario + '11:' + scenario + '66,' + params
    + 'B10),"Sin convergencia")');
}
for (let row = 11; row <= 66; row++) {
  const address = "O" + row;
  const formula = sensitivity.getRange(address).formulas[0][0];
  if (!formula.includes("$B$34")) {
    put(sensitivity, address, formula + "-IF(A" + row + "=" + params + "$B$34," + params + "$B$33,0)");
  }
}
put(sensitivity, "G6", "H5, reserva y calibración sin crédito fiscal. Comisión parametrizable en caja.");
put(sensitivity, "A9", "Meta de caja M12 en estrés (CLP)");
put(sensitivity, "B9", 10000000);
put(sensitivity, "C9", "=INDEX(J11:J66,MATCH('Parámetros D2'!B23,A11:A66,0))-B9");
put(sensitivity, "D9", "Holgura frente a la meta en el mes de la reserva");
put(sheets.getItem("Indicadores"), "C11", "Equivalencia matemática para respaldo técnico.");

const admin = sheets.getItem("Gastos Administrativos");
admin.getRange("F1:H1").values = [["Base o cantidad", "Tasa o valor unitario", "Meses de cobertura"]];
for (let row = 2; row <= 31; row++) {
  const criterion = admin.getRange("E" + row).values[0][0];
  if (!criterion) continue;
  if (criterion.includes("900.000.000")) {
    put(admin, "F" + row, 900000000);
    put(admin, "G" + row, 0.012);
    put(admin, "H" + row, Number(criterion.match(/(\d+)\/12$/)[1]));
    put(admin, "C" + row, "=F" + row + "*G" + row + "*H" + row + "/" + params + "$B$18");
  } else {
    const units = Number(criterion.match(/(\d+) UF/)[1]);
    put(admin, "F" + row, units);
    put(admin, "G" + row, "=" + params + "$B$21");
    put(admin, "C" + row, "=F" + row + "*G" + row);
  }
}

const master = sheets.add("Cuadro maestro");
header(master, ["Fase", "Componente", "Costo CLP", "Venta CLP", "Margen", "Costo UF",
  "Venta UF", "Costo USD", "Venta USD", "Criterio"], [19, 29, 20, 20, 13, 17, 17, 17, 17, 53]);
const categories = [
  ["Personal", "G", "Dotación y refuerzos del costo integrado"],
  ["Infraestructura y servicios", "B", "Consolidado de equipos, nube, conectividad y soporte"],
  ["Licencias", "C", "GitLab y SonarQube"],
  ["Calidad y capacitación", "D", "Partidas de calidad y capacitación"],
  ["Firma automática", "L", "Provisión de firma incluida en el flujo"],
  ["Otros confirmados", "H", "Partidas confirmadas en Costos"],
  ["Administración", "E", "Indirecto, según calendario de gastos"],
  ["Cierre", "F", "Indirecto, extensión de coberturas"],
];
let masterRow = 2;
for (const [phase, from, to] of [["Implementación", 2, 21], ["Operación", 22, 57]]) {
  for (const [category, column, source] of categories) {
    const row = masterRow++;
    put(master, "A" + row, phase);
    put(master, "B" + row, category);
    put(master, "C" + row, "=SUM(Costos!" + column + from + ":" + column + to + ")");
    put(master, "J" + row, source);
  }
  if (phase === "Implementación") {
    const row = masterRow++;
    put(master, "A" + row, phase);
    put(master, "B" + row, "Garantía correcto funcionamiento");
    put(master, "C" + row, "=SUM(Costos!J2:J57)");
    put(master, "J" + row, "Indirecto, pago estimado M21");
  }
}
for (let row = 2; row < masterRow; row++) {
  const c = "C" + row;
  const d = "D" + row;
  const implementation = row <= 10;
  const numerator = implementation ? "RESUMEN!$H$6" : "RESUMEN!$H$7";
  const denominator = implementation ? "SUM($C$2:$C$10)" : "SUM($C$11:$C$18)";
  const price = implementation ? c + "*" + numerator + "/" + denominator
    : row === 11 ? numerator + "-SUM($C$12:$C$18)" : c;
  put(master, d, "=" + price);
  put(master, "E" + row, '=IF(' + d + '=0,"",(' + d + "-" + c + ")/" + d + ")");
  for (const [col, formula] of [["F", c + "/" + params + "$B$21"], ["G", d + "/" + params + "$B$21"],
    ["H", c + "/" + params + "$B$19"], ["I", d + "/" + params + "$B$19"]]) put(master, col + row, "=" + formula);
}
put(master, "A19", "Total");
for (const col of ["C", "D", "F", "G", "H", "I"]) put(master, col + "19", "=SUM(" + col + "2:" + col + "18)");
put(master, "E19", "=(D19-C19)/D19");
put(master, "A20", "Diferencia con RESUMEN");
put(master, "C20", "=C19-RESUMEN!C8");
put(master, "D20", "=D19-RESUMEN!H8");
put(master, "A22", "Venta por componente según el puente vigente. Implementación proporcional al costo y margen de operación asignado a personal.");
put(master, "A23", "La fase de M21–M24 y el overhead incremental se ajustan al acreditar su imputación. Cifras netas.");
master.getRange("C2:D20").setNumberFormat("#,##0");
master.getRange("E2:E19").setNumberFormat("0.00%");
master.getRange("F2:I19").setNumberFormat("#,##0.00");

const tax = sheets.add("Conciliación IVA");
header(tax, ["Mes", "IVA referencial CLP", "IVA pagado audIT", "Crédito fiscal", "Diferencia referencial"],
  [10, 23, 24, 22, 24]);
for (let row = 2; row <= 57; row++) {
  put(tax, "A" + row, "=" + flow + "A" + row);
  put(tax, "B" + row, "=SUMIF(Proveedores!$B$2:$B$281,A" + row + ",Proveedores!$I$2:$I$281)");
  put(tax, "C" + row, "=" + flow + "K" + row);
  put(tax, "D" + row, "=" + flow + "L" + row);
  put(tax, "E" + row, "=B" + row + "-C" + row);
}
put(tax, "A58", "Total");
for (const col of ["B", "C", "D", "E"]) put(tax, col + "58", "=SUM(" + col + "2:" + col + "57)");
put(tax, "A60", "El IVA referencial incluye partidas de distinto pagador y cobertura. Confirmar documento, emisor, receptor, pago y crédito fiscal.");
tax.getRange("B2:E58").setNumberFormat("#,##0.00");

const benefit = sheets.getItem("Beneficios Curimón");
benefit.getRange("A8:D12").values = [
  ["Innovación", "Base de medición", "Unidad", "Condición"],
  ["INN-1", "Expedientes, tiempo de preparación y verificación", "Minutos por expediente", "Medir y evitar solape con INN-4"],
  ["INN-2", "Visitas y tiempo de preparación evitados", "Visitas y minutos", "Validar línea base y piloto"],
  ["INN-3", "Acoples y eventos térmicos", "Eventos por clase", "Kilometraje corresponde al criterio 26"],
  ["INN-5", "Consumo y siniestralidad", "Litros y eventos", "Medición con línea base"],
];
put(benefit, "A14", "INN-4 · Recupero bruto de referencia en 36 meses a régimen");
put(benefit, "B14", "=Innovaciones!C9*" + params + "B16/" + params + "B18");
put(benefit, "D14", "El neto depende del reparto, los costos y la adopción. Fuera de ingresos de audIT.");
benefit.getRange("A17:H17").values = [["Innovación", "Métrica", "Unidades evitadas al mes",
  "Valor por unidad CLP", "Adopción", "Costos y reparto mensual CLP", "Beneficio neto mensual CLP", "Evidencia"]];
benefit.getRange("A18:B23").values = [
  ["INN-1", "Minutos de preparación y verificación evitados"],
  ["INN-2", "Visitas adicionales evitadas y pagadas por Curimón"],
  ["INN-2", "Minutos evitados en recursos de Curimón, sin solapar visitas"],
  ["INN-3", "Eventos de acople evitados o resueltos"],
  ["INN-3", "Eventos térmicos evitados o resueltos"],
  ["INN-5", "Litros de combustible evitados"],
];
for (let row = 18; row <= 24; row++) {
  put(benefit, "G" + row, '=IF(AND(COUNT(C' + row + ':F' + row + ')=4,H' + row + '<>""),'
    + "C" + row + "*D" + row + "*E" + row + "-F" + row + ',"")');
}
put(benefit, "A24", "INN-5");
put(benefit, "B24", "Eventos de siniestralidad evitados");
inputRange(benefit, "C18:D24", nonnegative);
inputRange(benefit, "E18:E24", { type: "decimal", operator: "between", formula1: 0, formula2: 1 });
inputRange(benefit, "F18:F24", nonnegative);
benefit.getRange("H18:H24").format.fill = "#FFF1CE";
benefit.getRange("E18:E24").setNumberFormat("0.00%");
put(benefit, "A26", "Proyecciones de referencia. Las celdas de resultados se calculan al ingresar supuestos y evidencia.");
put(benefit, "A28", "INN-4 · Escenario mensual a régimen");
benefit.getRange("A29:G29").values = [["Bruto mensual CLP", "Adopción", "Reparto a terceros",
  "Costo incremental Curimón CLP", "Neto mensual CLP", "Evidencia", "Alcance"]];
put(benefit, "A30", "=Innovaciones!C9/" + params + "B18");
put(benefit, "E30", '=IF(AND(COUNT(B30:D30)=3,F30<>""),A30*B30*(1-C30)-D30,"")');
put(benefit, "G30", "No alimenta ingresos de audIT. Ingresar costos y reparto acreditados.");
inputRange(benefit, "B30:C30", { type: "decimal", operator: "between", formula1: 0, formula2: 1 });
inputRange(benefit, "D30", nonnegative);
benefit.getRange("F30").format.fill = "#FFF1CE";
benefit.getRange("B30:C30").setNumberFormat("0.00%");
const innovations = sheets.getItem("Innovaciones");
innovations.getRange("A19:E24").values = [
  ["Innovación", "Partida", "Referencia CLP", "Mes o ventana", "Tratamiento"],
  [2, "Desarrollo", 16576000, "Implementación EDT 12.2", "Atribución de nómina. Cobertura por acreditar."],
  [2, "Operación", 16992000, "M21–M56", "Atribución de nómina. Solo agregar brecha acreditada."],
  [3, "Integración y montaje", 5700000, "M6–M10 y M16–M18", "Estimado. Conciliar su imputación en EDT y compras."],
  [3, "Operación", 4032000, "M21–M56", "Estimado. Confirmar si está cubierto por nómina."],
  [5, "Inversión y soporte", null, "M4–M9, M13–M15 y M21–M56", "Desarrollo y soporte en refuerzos. Talleres y calibración en INN-5 Costos."],
];
put(innovations, "C24", "=SUM('INN-5 Costos'!E2:E5)+SUMIF('Refuerzo presupuestado'!B2:B48,\"INN-5*\",'Refuerzo presupuestado'!E2:E48)");
put(sheets.getItem("Escenarios de caja"), "A2", "Captura anterior al corte b15ebb6");
put(sheets.getItem("Escenarios de caja"), "A1", "Histórico. Para cifras vigentes consultar Sensibilidad e Indicadores.");
const summary = sheets.getItem("Resumen Ejecutivo");
put(summary, "B11", "Estrés modelado con CLP 400 millones adicionales. Disponibilidad, giros y comisiones por confirmar.");
put(summary, "A18", "Cuadro maestro y conciliación IVA");
put(summary, "B18", "Ver costos, ventas y márgenes por fase y componente. El puente de IVA distingue referencia, pago y crédito.");
put(summary, "A19", "Ajustes de operación");
put(summary, "B19", "Registrar variable y descuento en el mes de servicio. M56 se cobra en M57.");
put(summary, "A20", "Caja mínima del estrés CLP");
put(summary, "B20", "=Sensibilidad!D6");
put(summary, "A21", "Holgura frente a la meta CLP");
put(summary, "B21", "=Sensibilidad!C9");

const outputFile = await SpreadsheetFile.exportXlsx(workbook);
await outputFile.save(output);
