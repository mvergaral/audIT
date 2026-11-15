import fs from 'node:fs/promises';
import {FileBlob,SpreadsheetFile} from '@oai/artifact-tool';
const root='/home/axeler8/Escritorio/audIT';
const wb=await SpreadsheetFile.importXlsx(await FileBlob.load(root+'/outputs/informe3-integral/entrega-consolidada/AUDIT-Informe3-Modelo-Economico.xlsx'));
console.log((await wb.inspect({kind:'table',range:'Resumen Ejecutivo!A1:C12',maxChars:1800,tableMaxRows:12,tableMaxCols:3})).ndjson);
const p=await wb.render({sheetName:'RESUMEN',range:'A1:N22',scale:1,format:'png'});
await fs.writeFile(root+'/outputs/informe3-corregido/revision/resumen-antes.png',new Uint8Array(await p.arrayBuffer()));
console.log('Importación y vista original listas');
