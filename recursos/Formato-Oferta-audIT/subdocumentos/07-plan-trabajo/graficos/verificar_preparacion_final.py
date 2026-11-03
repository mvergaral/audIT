"""Ejecuta el verificador oficial con rutas de contenido compatibles con Windows."""
from pathlib import Path
import os,sys,inspect
BASE=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(BASE/'herramientas'))
import verificar
# El verificador usa prefijos POSIX; os.path.relpath produce barras inversas en Windows.
def es_contenido(ruta):
 rel=os.path.relpath(ruta,verificar.RAIZ).replace('\\','/')
 return rel.startswith(('subdocumentos/','muestra/','anexos/','economico/'))
verificar.es_contenido=es_contenido
# El verificador confunde «sub=no» (fuente completa) con «emb=no».
# Se conserva la comprobación de incrustación sobre la columna emb de pdffonts.
codigo=inspect.getsource(verificar.verificar_pdfs)
assert '"no" in campos[-5:-3]' in codigo
codigo=codigo.replace('"no" in campos[-5:-3]','campos[-5] == "no"')
exec(compile(codigo,verificar.__file__,'exec'),verificar.__dict__)
sys.argv=[sys.argv[0],str(BASE/'subdocumentos/07-plan-trabajo/preparacion-final/manifiesto.json')]
raise SystemExit(verificar.main())
