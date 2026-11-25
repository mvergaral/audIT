"""Compila una copia integrada de revisión del S7 sin modificar la plantilla."""
from pathlib import Path
import os,subprocess,shutil,urllib.request,zipfile,sys
HERE=Path(__file__).resolve().parent
BASE=HERE.parents[2]
OUT=HERE/'revisada/compilacion';OUT.mkdir(parents=True,exist_ok=True)
FONTS=OUT/'dependencias/fuentes'
if not (FONTS/'IBMPlexSerif-Regular.otf').exists():
 FONTS.mkdir(parents=True,exist_ok=True)
 package=OUT/'dependencias/plex.zip'
 print('Descargando fuentes IBM Plex desde CTAN a la carpeta local de compilación.',flush=True)
 with urllib.request.urlopen('https://mirrors.ctan.org/fonts/plex.zip',timeout=60) as source, package.open('wb') as target:
  shutil.copyfileobj(source,target)
 with zipfile.ZipFile(package) as z:
  for entry in z.namelist():
   if entry.endswith('.otf'):(FONTS/Path(entry).name).write_bytes(z.read(entry))
FINAL='--informe2' not in sys.argv
wrapper=OUT/'s7-revision.tex'
wrapper.write_text(r'''\def\RaizSubdocumentos{subdocumentos}
\def\NumeroSubdoc{7}
\def\FolioInicialExterno{1}
\def\NombreArchivo{S7-Integrado-Revision}
\def\ArchivoActual{S7-Integrado-Revision}
\input{subdocumento.tex}
''',encoding='utf-8')
if FINAL:
 entry=OUT/'entrada-final.tex'
 template=(BASE/'subdocumento.tex').read_text(encoding='utf-8')
 template=template.replace(r'\begin{document}',r'\AplicarInstancia{final}\Version{3.0}'+'\n'+r'\begin{document}')
 entry.write_text(template,encoding='utf-8')
 wrapper.write_text(wrapper.read_text(encoding='utf-8').replace(r'\input{subdocumento.tex}',r'\input{'+entry.relative_to(BASE).as_posix()+'}'),encoding='utf-8')
env=os.environ.copy();env['TEXINPUTS']='.;'+';'.join(str(BASE/p).replace('\\','/')+'//' for p in ['estilo','fuentes','temas','portadas','formularios','configuracion'])+';'
env['OPENTYPEFONTS']=str(FONTS).replace('\\','/')+'//;';env['OSFONTDIR']=str(FONTS)
args=['lualatex','-recorder','--enable-installer','-interaction=nonstopmode','-halt-on-error','-file-line-error','-jobname=S7-Integrado-Revision','-output-directory='+str(OUT),str(wrapper)]
# Freeze real section labels from S3/S4/S6 for cross-document references.
ext=OUT/'externos';ext.mkdir(exist_ok=True)
registrations=[]
for number in (3,4,6):
 name=f'S{number:02d}';w=ext/(name+'.tex')
 w.write_text('\\def\\RaizSubdocumentos{subdocumentos}\n\\def\\NumeroSubdoc{'+str(number)+'}\n\\def\\FolioInicialExterno{1}\n\\def\\NombreArchivo{'+name+'}\n\\def\\ArchivoActual{'+name+'}\n\\input{subdocumento.tex}\n',encoding='utf-8')
 cmd=['lualatex','-recorder','--enable-installer','-draftmode','-interaction=nonstopmode','-halt-on-error','-jobname='+name,'-output-directory='+str(ext),str(w)]
 with (ext/(name+'-compilacion.txt')).open('w',encoding='utf-8') as log:
  r=subprocess.run(cmd,cwd=BASE,env=env,stdout=log,stderr=subprocess.STDOUT,stdin=subprocess.DEVNULL)
 print('etiquetas externas',name,r.returncode,flush=True)
 if r.returncode==0:
  relative=(ext/name).relative_to(BASE).as_posix()
  registrations.append('\\RegistrarPrefijo{'+name+'-}\\externaldocument['+name+'-]{'+relative+'}[AUDIT-Subdocumento'+str(number)+'.pdf]')
(ext/'externos.tex').write_text('\n'.join(registrations)+'\n',encoding='utf-8')
ws=wrapper.read_text(encoding='utf-8');ws='\\def\\ArchivoExternos{'+(ext/'externos.tex').relative_to(BASE).as_posix()+'}\n'+ws;wrapper.write_text(ws,encoding='utf-8')
for i in range(3):
 with (OUT/f'pasada-{i+1}.txt').open('w',encoding='utf-8') as log:
  result=subprocess.run(args,cwd=BASE,env=env,stdout=log,stderr=subprocess.STDOUT,stdin=subprocess.DEVNULL)
 print('pasada',i+1,'exit',result.returncode,flush=True)
 if result.returncode:
  print((OUT/f'pasada-{i+1}.txt').read_text(encoding='utf-8',errors='replace')[-3000:]);raise SystemExit(result.returncode)
 if i==0 and (OUT/'S7-Integrado-Revision.bcf').exists():
  with (OUT/'biber.txt').open('w',encoding='utf-8') as log:
   r=subprocess.run(['biber','--input-directory='+str(OUT),'--output-directory='+str(OUT),'S7-Integrado-Revision'],cwd=BASE,env=env,stdout=log,stderr=subprocess.STDOUT,stdin=subprocess.DEVNULL)
  print('biber',r.returncode,flush=True)
  if r.returncode:
   print((OUT/'biber.txt').read_text(encoding='utf-8',errors='replace')[-2500:]);raise SystemExit(r.returncode)
target=HERE.parent/('S7_Integrado_Revision.pdf' if FINAL else 'S7_Informe2_Revision.pdf')
try:
 shutil.copy2(OUT/'S7-Integrado-Revision.pdf',target)
except PermissionError:
 # El visor de PDF de Windows puede mantener abierta la revisión previa.
 target=HERE.parent/('S7_Final_actualizado.pdf' if FINAL else 'S7_Informe2_actualizado.pdf')
 shutil.copy2(OUT/'S7-Integrado-Revision.pdf',target)
print('PDF integrado:',target)
