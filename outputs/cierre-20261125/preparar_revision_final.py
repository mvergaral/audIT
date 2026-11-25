from pathlib import Path
import json,hashlib,difflib,subprocess
O=Path(__file__).resolve().parent;R=O.parents[1];B=O/'fuentes'
snapshot=json.loads((O/'evidencia/snapshot.json').read_text(encoding='utf-8'))
known={x['destino'].replace('\\','/'):x for x in snapshot if x['destino'].replace('\\','/').startswith('fuentes/')}
parts=['# Paquete de revisión de la ejecución\nBase c140209; correcciones aisladas; no hay commit ni envío.\n']
changed=[]
for p in B.rglob('*'):
    if not p.is_file() or 'salida' in p.parts or p.suffix not in ('.tex','.py','.sty','.cls') and p.name!='.latexmkrc':continue
    rel=p.relative_to(O).as_posix();info=known.get(rel);data=p.read_bytes()
    if info and hashlib.sha256(data).hexdigest()==info['sha256']:continue
    old=subprocess.check_output(['git','show','c140209:'+info['origen']],cwd=R).decode('utf-8') if info else ''
    new=data.decode('utf-8');changed.append(rel)
    parts.extend(difflib.unified_diff(old.splitlines(True),new.splitlines(True),fromfile='base/'+rel,tofile=rel,n=4))
(O/'evidencia/revision-final.diff').write_text('\n'.join(parts),encoding='utf-8')
(O/'evidencia/archivos-modificados.json').write_text(json.dumps(changed,ensure_ascii=False,indent=2),encoding='utf-8')
print(len(changed),'archivos en paquete de revisión')
