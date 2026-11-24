import path from "node:path";
import { spawnSync } from "node:child_process";
import { fileURLToPath } from "node:url";

const [input, output] = process.argv.slice(2);
if (!input || !output) {
  throw new Error("Uso: node aplicar_controles_modelo.mjs entrada.xlsx salida.xlsx");
}
const consolidate = fileURLToPath(new URL("consolidar_informe3.ps1", import.meta.url));
const result = spawnSync("pwsh", [
  "-NoProfile", "-File", consolidate,
  "-Entrada", path.resolve(input), "-Salida", path.resolve(output),
], { stdio: "inherit", windowsHide: true });
if (result.error) throw result.error;
process.exitCode = result.status ?? 1;
