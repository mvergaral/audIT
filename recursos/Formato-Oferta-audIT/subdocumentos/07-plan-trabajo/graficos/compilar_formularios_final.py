"""Compila T-14, T-15 y T-18 con las referencias del S7 preparado para final."""
from pathlib import Path
import os,subprocess,shutil,json
import fitz
HERE=Path(__file__).resolve().parent
BASE=HERE.parents[2]
WORK=HERE/'revisada/compilacion'
OUT=HERE.parent/'preparacion-final';OUT.mkdir(exist_ok=True)
FONTS=WORK/'dependencias/fuentes'
assert FONTS.exists(), 'Compilar primero compilar_revision.py --final'
env=os.environ.copy()
env['TEXINPUTS']='.;'+';'.join(str(BASE/p).replace('\\','/')+'//' for p in ['estilo','fuentes','temas','portadas','formularios','configuracion'])+';'
env['OPENTYPEFONTS']=str(FONTS).replace('\\','/')+'//;';env['OSFONTDIR']=str(FONTS)
ext=WORK/'externos-formularios.tex'
ext.write_text((WORK/'externos/externos.tex').read_text(encoding='utf-8')+'\n\\externaldocument{'+(WORK/'S7-Integrado-Revision').relative_to(BASE).as_posix()+'}\n',encoding='utf-8')
entry=WORK/'entrada-formulario-final.tex'
entry.write_text((BASE/'formulario.tex').read_text(encoding='utf-8').replace(r'\begin{document}',r'\AplicarInstancia{final}\Version{3.0}'+'\n'+r'\begin{document}'),encoding='utf-8')
entries=[]
for code in ('T-14','T-15','T-18'):
 job='AUDIT-Formulario-'+code
 wrapper=WORK/(job+'.tex')
 wrapper.write_text(r'\def\RaizSubdocumentos{subdocumentos}\def\NumeroSubdoc{7}\def\FolioInicialExterno{1}'+'\n'+r'\def\FormularioActual{'+code+'}\n'+r'\def\NombreArchivo{'+job+'}\n'+r'\def\ArchivoActual{'+job+'}\n'+r'\def\ArchivoExternos{'+ext.relative_to(BASE).as_posix()+'}\n'+r'\input{'+entry.relative_to(BASE).as_posix()+'}'+'\n',encoding='utf-8')
 args=['lualatex','-recorder','--enable-installer','-interaction=nonstopmode','-halt-on-error','-file-line-error','-jobname='+job,'-output-directory='+str(WORK),str(wrapper)]
 for i in range(3):
  with (WORK/(job+f'-{i+1}.txt')).open('w',encoding='utf-8') as log:r=subprocess.run(args,cwd=BASE,env=env,stdout=log,stderr=subprocess.STDOUT,stdin=subprocess.DEVNULL)
  print(code,'pasada',i+1,r.returncode,flush=True)
  if r.returncode:raise SystemExit(r.returncode)
  if i==0 and (WORK/(job+'.bcf')).exists():
   with (WORK/(job+'-biber.txt')).open('w',encoding='utf-8') as log:r=subprocess.run(['biber','--input-directory='+str(WORK),'--output-directory='+str(WORK),job],cwd=BASE,env=env,stdout=log,stderr=subprocess.STDOUT,stdin=subprocess.DEVNULL)
   if r.returncode:raise SystemExit(r.returncode)
 shutil.copy2(WORK/(job+'.pdf'),OUT/(job+'.pdf'))
 entries.append({'clave':'07'+code,'nombre':job+'.pdf','folio_inicial':1,'paginas':len(fitz.open(OUT/(job+'.pdf'))),'aux':str((WORK/(job+'.aux')).relative_to(BASE)),'log':str((WORK/(job+'.log')).relative_to(BASE)),'fuentes':[['subdocumentos'],['subdocumentos/07-plan-trabajo']]})
shutil.copy2(HERE.parent/'S7_Integrado_Revision.pdf',OUT/'SOBRE2_AUDIT_SUBDOC07_20261125.pdf')
entries.insert(0,{'clave':'07','nombre':'SOBRE2_AUDIT_SUBDOC07_20261125.pdf','folio_inicial':1,'paginas':len(fitz.open(HERE.parent/'S7_Integrado_Revision.pdf')),'aux':str((WORK/'S7-Integrado-Revision.aux').relative_to(BASE)),'log':str((WORK/'S7-Integrado-Revision.log').relative_to(BASE)),'fuentes':[['subdocumentos'],['subdocumentos/07-plan-trabajo']]})
(OUT/'manifiesto.json').write_text(json.dumps({'grupo':'final-s7-preparacion','instancia':'final','modo_folio':'subdocumento','archivos':entries},ensure_ascii=False,indent=2),encoding='utf-8')
print('Preparación final generada; foliación global pendiente del ensamblado de la oferta.',flush=True)
