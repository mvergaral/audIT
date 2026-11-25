"""Crea una rama de respaldo mediante índice separado, sin alterar un rebase abierto."""
from pathlib import Path
import os,json,subprocess
O=Path(__file__).resolve().parent;R=O.parents[1]
env=os.environ.copy();env['GIT_INDEX_FILE']=str(O/'evidencia/indice-checkpoint.git')
def git(*args):
    return subprocess.check_output(['git',*args],cwd=R,env=env,stderr=subprocess.PIPE).decode('utf-8').strip()
parent=git('rev-parse','HEAD')
names=json.loads((O/'evidencia/archivos-checkpoint.json').read_text(encoding='utf-8'))
names+=['outputs/cierre-20261125/evidencia/archivos-checkpoint.json','outputs/cierre-20261125/subir_checkpoint.py']
git('read-tree',parent)
git('add','--sparse','--',*names)
stat=git('diff','--cached','--shortstat')
# Validación sintáctica de scripts sin ejecutarlos ni retomar el trabajo.
for name in names:
    p=R/name
    if p.suffix=='.py':compile(p.read_text(encoding='utf-8'),str(p),'exec')
tree=git('write-tree')
commit=git('commit-tree',tree,'-p',parent,'-m','Guarda avance del cierre final y plan de continuidad del 25 de noviembre')
branch='codex/continuidad-cierre-20261125'
git('update-ref','refs/heads/'+branch,commit,'0'*40)
print(json.dumps({'commit':commit,'rama':branch,'resumen':stat},ensure_ascii=False),flush=True)
push=subprocess.run(['git','push','-u','origin',branch],cwd=R,env=env,text=True,encoding='utf-8',stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
print(push.stdout)
if push.returncode:raise SystemExit(push.returncode)
remote=git('ls-remote','--heads','origin','refs/heads/'+branch).split()[0]
if remote!=commit:raise RuntimeError('La referencia remota no coincide')
(O/'evidencia/subida-confirmada.json').write_text(json.dumps({'commit':commit,'rama':branch,'remote':remote,'resumen':stat},ensure_ascii=False,indent=2),encoding='utf-8')
print('SUBIDA_VERIFICADA',commit)
