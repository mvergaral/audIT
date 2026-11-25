"""Verificación oficial del técnico, conservando resultados sin ocultar hallazgos."""
from pathlib import Path
import os,sys,inspect,subprocess,json,contextlib
O=Path(__file__).resolve().parent;B=O/'fuentes'
sys.path.insert(0,str(B/'herramientas'))
import verificar as v
v.SALIDA=str(O/'evidencia')
v.es_contenido=lambda ruta:os.path.relpath(ruta,v.RAIZ).replace('\\','/').startswith(('subdocumentos/','anexos/','economico/'))
# pdffonts: campo 'emb' se comprueba directamente; 'uni=no' no implica fuente no incrustada.
code=inspect.getsource(v.verificar_pdfs)
assert '"no" in campos[-5:-3]' in code
code=code.replace('"no" in campos[-5:-3]','campos[-5] == "no"')
exec(compile(code,v.__file__,'exec'),v.__dict__)
original=subprocess.run
def run(cmd,*a,**kw):
    if isinstance(cmd,list) and Path(cmd[0]).stem in ('pdftotext','pdffonts'):
        kw['encoding']='utf-8';kw['errors']='replace'
    return original(cmd,*a,**kw)
subprocess.run=run
captured=[];print_original=v.Informe.imprimir
def capture(self):
    captured.extend({'codigo':x[0],'titulo':x[1],'estado':x[2],'detalle':x[3]} for x in self.puntos)
    return print_original(self)
v.Informe.imprimir=capture
manifest=B/'salida/final/manifiesto.json'
with (O/'evidencia/verificador-tecnico.log').open('w',encoding='utf-8') as log,contextlib.redirect_stdout(log),contextlib.redirect_stderr(log):
    result=v.verificar_grupo(str(manifest),v.Config())
(O/'evidencia/verificador-tecnico.json').write_text(json.dumps(captured,ensure_ascii=False,indent=2),encoding='utf-8')
print('Reglas:',len(captured),'No cumple:',result)
for x in captured:
    if x['estado']=='NO CUMPLE':print(x['codigo'],x['titulo'],str(x['detalle'])[:1700])
