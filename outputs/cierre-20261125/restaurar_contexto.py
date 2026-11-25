"""Restaura dependencias del corte base sin sobrescribir correcciones del checkpoint."""
from pathlib import Path
import subprocess,tarfile
O=Path(__file__).resolve().parent;R=O.parents[1]
prefix='recursos/Formato-Oferta-audIT/'
proc=subprocess.Popen(['git','archive','c140209','recursos/Formato-Oferta-audIT','outputs/cierre-d2-final'],cwd=R,stdout=subprocess.PIPE)
written=0
with tarfile.open(fileobj=proc.stdout,mode='r|') as archive:
    for member in archive:
        if not member.isfile():continue
        if member.name.startswith(prefix):
            rel=member.name[len(prefix):]
            if rel.startswith('salida/'):
                if not rel.startswith(('salida/final/','salida/final-por-subdocumento/')):continue
                target=O/'referencia'/rel.removeprefix('salida/')
            else:target=O/'fuentes'/rel
        else:target=O/'insumos-d2'/member.name.removeprefix('outputs/cierre-d2-final/')
        target=target.resolve()
        if not target.is_relative_to(O.resolve()):raise RuntimeError(member.name)
        if target.exists():continue
        target.parent.mkdir(parents=True,exist_ok=True)
        target.write_bytes(archive.extractfile(member).read());written+=1
if proc.wait():raise RuntimeError('Falló la recuperación del corte c140209')
print('Archivos faltantes restaurados:',written,'; correcciones existentes conservadas.')
