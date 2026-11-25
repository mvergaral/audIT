"""Adaptaciones de ejecución Windows sin editar el verificador compartido."""
from pathlib import Path
import os,sys,inspect,contextlib,subprocess
OUT=Path(__file__).resolve().parent;BASE=OUT/'fuentes'
sys.path.insert(0,str(BASE/'herramientas'))
import verificar as v
v.SALIDA=str(OUT/'evidencia')
v.es_contenido=lambda ruta:os.path.relpath(ruta,v.RAIZ).replace('\\','/').startswith(('subdocumentos/','anexos/','economico/'))
code=inspect.getsource(v.verificar_pdfs)
assert '"no" in campos[-5:-3]' in code
code=code.replace('"no" in campos[-5:-3]','campos[-5] == "no"')
exec(compile(code,v.__file__,'exec'),v.__dict__)
original=subprocess.run
def run(cmd,*args,**kwargs):
    if isinstance(cmd,list) and Path(cmd[0]).stem in ['pdftotext','pdffonts']:
        kwargs['encoding']='utf-8';kwargs['errors']='replace'
    return original(cmd,*args,**kwargs)
subprocess.run=run
mode=sys.argv[1] if len(sys.argv)>1 else 'tecnico'
manifest=OUT/'documentos/manifiesto-tecnico.json' if mode=='tecnico' else OUT/'documentos/manifiesto-economico.json'
with (OUT/'evidencia'/f'verificador-{mode}-windows.log').open('w',encoding='utf-8') as f,contextlib.redirect_stdout(f),contextlib.redirect_stderr(f):
    result=v.verificar_grupo(str(manifest),v.Config());print('REGLAS_NO_CUMPLIDAS',result)
print(mode,'reglas no cumplidas',result)
