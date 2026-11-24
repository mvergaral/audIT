import fs from 'node:fs/promises';
import assert from 'node:assert/strict';
import {fileURLToPath} from 'node:url';
import {FileBlob, SpreadsheetFile} from '@oai/artifact-tool';

const output=fileURLToPath(new URL('../../../outputs/informe3-mejora/revision/',import.meta.url));
const book=await SpreadsheetFile.importXlsx(await FileBlob.load(output+'modelo-borrador-v4.xlsx'));
const cell=address=>{
  const [sheet, range]=address.split('!');
  return book.worksheets.getItem(sheet).getRange(range);
};
const v=address=>cell(address).values[0][0];
const same=(a,b,explain)=>assert.ok(Math.abs(a-b)<.02, `${explain}: ${a} frente a ${b}`);
const set=(key,value)=>{cell(key).values=[[value]];};
const results=[];
function trial(name, inputs, outputs, verify){
  const before=Object.fromEntries(outputs.map(k=>[k,v(k)]));
  const originals=Object.fromEntries(Object.keys(inputs).map(k=>[k,v(k)]));
  for (const [k,x] of Object.entries(inputs))set(k,x);
  book.recalculate();
  const after=Object.fromEntries(outputs.map(k=>[k,v(k)]));
  verify(before,after);
  for (const [k,x] of Object.entries(originals))set(k,x);
  book.recalculate();
  for (const k of outputs)same(v(k),before[k],`Restauración ${k}`);
  results.push({name,inputs,before,after,result:'verificada'});
}
book.recalculate();
const f22='Ingresos!J23',f23='Ingresos!J24',m57='Ingresos!J58',m58='Ingresos!J59';
trial('Desfase de cobro M57 a M58',{'Parámetros corrección!B36':2},
  [f22,f23,m57,m58,'Control de entrega!B8','Control de entrega!B22','Control de entrega!B23',
   'Indicadores!B8','Sensibilidad!AE14','Sensibilidad!M14'], (a,b)=>{
    same(b[f22],0,'Primera mensualidad ya no se cobra en M22');
    same(b[f23],a[f22],'Primer cobro en M23');
    same(b[m58],a[m57],'La última factura llega a M58');
    same(b['Control de entrega!B23'],58,'Mes de cobro en control');
    same(b['Control de entrega!B22'],36,'Conteo de cobros');
    same(b['Control de entrega!B8'],36,'Conteo de facturas estable');
    same(b['Sensibilidad!AE14'],b['Indicadores!B8'],'Escenario comparte calendario de cobros');
    assert.notEqual(b['Sensibilidad!M14'],a['Sensibilidad!M14']);
  });
trial('Ajuste operativo en M56',{'Ajustes de operación!B57':1250000},
  ['Ingresos!H57',m57,'Ingresos!E57','RESUMEN!H8','Curva S!C57','Indicadores!B2','Sensibilidad!AE14'], (a,b)=>{
    for(const k of Object.keys(b).filter(k=>k!=='Indicadores!B2'))same(b[k]-a[k],1250000,k);
    same(b['Indicadores!B2'],a['Indicadores!B2'],'M57 fuera del VAN base');
  });
trial('Inicio y duración del servicio',{'Parámetros D2!B16':35,'Parámetros D2!B17':22},
  ['Ingresos!G22','Ingresos!H22','Ingresos!J23','Control de entrega!B8','Control de entrega!B22'], (a,b)=>{
    same(b['Control de entrega!B8'],35,'Facturas emitidas');
    same(b['Control de entrega!B22'],35,'Facturas cobradas');
    same(b['Ingresos!G22'],a['Ingresos!G22'],'H12 independiente de la primera mensualidad');
    same(b['Ingresos!H22'],0,'M21 sin facturación operativa en este escenario');
    same(b['Ingresos!J23'],0,'M22 sin cobro operativo en este escenario');
  });
trial('Traslado de cinco kits M7 a M8',{'Parámetros corrección!B39':55,'Parámetros corrección!B40':65},
  ['Activaciones!B8','Activaciones!B9','Activaciones!E8','Activaciones!E9','Activaciones!F8',
   'Instalación por lote!H7','Dotación por perfil!F130','Flujo de Caja!W8','Gráficos UF!E8',
   'Control de entrega!B24'],(a,b)=>{
    same(b['Activaciones!B8']-a['Activaciones!B8'],-5,'Menos altas M7');
    same(b['Activaciones!B9']-a['Activaciones!B9'],5,'Más altas M8');
    same(b['Activaciones!E9'],a['Activaciones!E9'],'Inventario activo restaurado en M8');
    same(b['Control de entrega!B24'],0,'Inventario conciliado');
    for(const k of ['Activaciones!F8','Instalación por lote!H7','Dotación por perfil!F130',
      'Flujo de Caja!W8','Gráficos UF!E8'])assert.notEqual(b[k],a[k],k);
  });
const origin=JSON.parse(await fs.readFile(new URL('../referencia-3.0.json',import.meta.url),'utf8'));
trial('Reproducción de las decisiones económicas 3.0',{'Parámetros corrección!B59':1,'Parámetros corrección!B70':1},
  ['RESUMEN!C8','RESUMEN!H8','Indicadores!B2','Control de entrega!B2','Control de entrega!B21'], (a,b)=>{
    for(const [k,key] of Object.entries({'RESUMEN!C8':'costo','RESUMEN!H8':'venta','Indicadores!B2':'van',
       'Control de entrega!B2':'caja','Control de entrega!B21':'cota'}))same(b[k],origin[key],k);
  });
await fs.writeFile(output+'pruebas-propagacion.json',JSON.stringify(results,null,2)+'\n');
console.log(results.map(r=>r.name));
