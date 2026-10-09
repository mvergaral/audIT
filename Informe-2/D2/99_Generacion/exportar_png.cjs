const fs = require('fs');
const path = require('path');
const sharp = require('C:/Users/mvergara/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/sharp');
const root = path.resolve(__dirname, '..');
const folders = ['01_EDT/01_Completa','01_EDT/02_Seccionada','02_Gantt/01_Graficos'];
(async () => {
 for (const folder of folders) {
  for (const name of fs.readdirSync(path.join(root,folder)).filter(n=>n.endsWith('.svg'))) {
   const src=path.join(root,folder,name);
   await sharp(src).png().toFile(src.replace(/\.svg$/,'.png'));
  }
 }
 console.log('16 gráficos exportados a PNG.');
})();
