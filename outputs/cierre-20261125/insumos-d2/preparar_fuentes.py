"""Prepara la copia aislada desde el repositorio, incluidos archivos sparse ausentes."""
from pathlib import Path
import subprocess,shutil,json
OUT=Path(__file__).resolve().parent;ROOT=OUT.parents[1]
BASE=ROOT/'recursos/Formato-Oferta-audIT';TARGET=OUT/'fuentes'
ignore={'salida','preparacion-final','compilacion','version-anterior','__pycache__'}
tracked=subprocess.check_output(['git','ls-tree','-r','--name-only','HEAD','recursos/Formato-Oferta-audIT'],cwd=ROOT,text=True,encoding='utf-8').splitlines()
paths={Path(p).relative_to('recursos/Formato-Oferta-audIT') for p in tracked}
paths|={p.relative_to(BASE) for p in BASE.rglob('*') if p.is_file()}
count=0
for relative in sorted(paths):
    if any(part in ignore for part in relative.parts):continue
    source=BASE/relative;target=TARGET/relative;target.parent.mkdir(parents=True,exist_ok=True)
    if source.exists():shutil.copy2(source,target)
    else:target.write_bytes(subprocess.check_output(['git','show','HEAD:recursos/Formato-Oferta-audIT/'+relative.as_posix()],cwd=ROOT))
    count+=1
print('Copia aislada preparada:',count,'archivos. Usar las fuentes aceptadas del paquete y revisar el SHA del repositorio antes de regenerar.')
