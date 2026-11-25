"""Compilación aislada de D2 con las referencias externas reales del mismo corte."""
from pathlib import Path
import os, subprocess, json, shutil, sys

OUT=Path(__file__).resolve().parent
BASE=OUT/'fuentes'
BUILD=OUT/'revision/latex'
BUILD.mkdir(parents=True,exist_ok=True)
ENV=os.environ.copy();ENV['TEXINPUTS']=str(BASE).replace('\\','/')+'//;'
DOCS=[('S03',3,None,'AUDIT-Subdocumento3'),('T12',3,'T-12','AUDIT-Formulario-T-12'),
      ('S07',7,None,'AUDIT-Subdocumento7'),('T14',7,'T-14','AUDIT-Formulario-T-14'),
      ('T15',7,'T-15','AUDIT-Formulario-T-15'),('T18',7,'T-18','AUDIT-Formulario-T-18')]
EXT=[('S04',4,None),('S06',6,None),('T17',9,'T-17'),('S07',7,None)]
RESULT=[]

def call(cmd,name):
    with (OUT/'evidencia'/f'{name}.log').open('w',encoding='utf-8') as log:
        r=subprocess.run(cmd,cwd=BASE,env=ENV,stdout=log,stderr=subprocess.STDOUT,stdin=subprocess.DEVNULL,timeout=180)
    RESULT.append(dict(paso=name,exit=r.returncode))
    (OUT/'evidencia/compilacion-tecnica.json').write_text(json.dumps(RESULT,indent=2),encoding='utf-8')
    if r.returncode:
        print((OUT/'evidencia'/f'{name}.log').read_text(encoding='utf-8',errors='replace')[-1900:],flush=True)
        raise RuntimeError(name)

def wrapper(key,num,form,stem,refs=False):
    dest=BUILD/(key+'.tex')
    template=(BASE/('formulario.tex' if form else 'subdocumento.tex')).read_text(encoding='utf-8')
    declarations=[r'\def\RaizSubdocumentos{subdocumentos}',r'\def\NumeroSubdoc{'+str(num)+'}',
        r'\def\FolioInicialExterno{1}',r'\def\NombreArchivo{'+stem+'}',r'\def\ArchivoActual{'+stem+'}']
    if form:declarations.append(r'\def\FormularioActual{'+form+'}')
    if refs:
        ext=BUILD/(key+'-externos.tex');lines=[]
        for other in ['S03','S04','S06','S07','T17']:
            aux=BUILD/other
            if other!=key and aux.with_suffix('.aux').exists():
                filename=next((d[3] for d in DOCS if d[0]==other),f'AUDIT-Subdocumento{int(other[1:])}' if other.startswith('S') else 'AUDIT-Formulario-T-17')
                lines.append(r'\RegistrarPrefijo{'+other+'-}'+r'\externaldocument['+other+'-]{'+aux.as_posix()+'}['+filename+'.pdf]')
        ext.write_text('\n'.join(lines),encoding='utf-8');declarations.append(r'\def\ArchivoExternos{'+ext.as_posix()+'}')
    # La firma humana no se aplica automáticamente a contenido recién generado.
    template=template.replace(r'\begin{document}',r'\AplicarInstancia{final}\Version{3.1}'+
        '\n'+r'\ImagenMediaFirma{}\ImagenFirmaCompleta{}'+'\n'+r'\begin{document}',1)
    dest.write_text('\n'.join(declarations)+'\n'+template,encoding='utf-8')
    return dest

def latex(key,num,form,stem,refs=False,passes=1,draft=False):
    source=wrapper(key,num,form,stem,refs)
    for i in range(1,passes+1):
        cmd=['lualatex','--disable-installer','-recorder','-interaction=nonstopmode','-halt-on-error',
             '-file-line-error','-jobname='+key,'-output-directory='+str(BUILD)]
        if draft:cmd.append('-draftmode')
        call(cmd+[str(source)],f'{key}-pasada-{i}')
        if i==1 and not draft and (BUILD/(key+'.bcf')).exists():
            call(['biber','--input-directory='+str(BUILD),'--output-directory='+str(BUILD),key],key+'-biber')
    print(key,'compilado',flush=True)

def main():
    for key,n,f in EXT:latex(key,n,f,key,draft=True)
    entries=[]
    for key,n,f,stem in DOCS:
        latex(key,n,f,stem,refs=True,passes=3)
        shutil.copy2(BUILD/(key+'.pdf'),OUT/'documentos'/(stem+'.pdf'))
        entries.append(dict(clave=key,nombre=stem+'.pdf',folio_inicial=1,
             aux=str(BUILD/(key+'.aux')),log=str(BUILD/(key+'.log')),
             fuentes=[['subdocumentos'],[f'subdocumentos/{"03-solucion" if n==3 else "07-plan-trabajo"}']]))
    (OUT/'documentos/manifiesto.json').write_text(json.dumps(dict(grupo='d2-cierre-final',instancia='final',modo_folio='subdocumento',archivos=entries),ensure_ascii=False,indent=2),encoding='utf-8')

if __name__=='__main__':main()
