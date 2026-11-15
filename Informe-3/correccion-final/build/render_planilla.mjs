import fs from 'node:fs/promises';
import {FileBlob,SpreadsheetFile} from '@oai/artifact-tool';
const root='/home/axeler8/Escritorio/audIT/outputs/informe3-corregido';
const wb=await SpreadsheetFile.importXlsx(await FileBlob.load(root+'/entrega/INFORME3_AUDIT_PLANILLA_20261114.xlsx'));
for(const [sheetName,range,name] of [['RESUMEN','A1:N22','resumen-despues'],['Resumen Ejecutivo','A1:C12','ejecutivo'],['Control de entrega','A1:C21','controles'],['Instalación por lote','A1:L8','instalacion']]){
 const p=await wb.render({sheetName,range,scale:1,format:'png'});await fs.writeFile(root+'/revision/'+name+'.png',new Uint8Array(await p.arrayBuffer()));
}
console.log('Vistas finales generadas');process.exit(0);
