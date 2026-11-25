"""Usa el ensamblador del repositorio con LuaLaTeX directo y bibliografía."""
from pathlib import Path
import sys, os, subprocess, shutil

OUT=Path(__file__).resolve().parent;BASE=OUT/'fuentes'
sys.path.insert(0,str(BASE/'herramientas'))
import compilar as c
from comun import Config
ENV=os.environ.copy();ENV['TEXINPUTS']=str(BASE).replace('\\','/')+'//;'
source=OUT/'documentos/AUDIT_ModeloFinanciero_3_20261125.xlsx'
shutil.copy2(source,BASE/'economico/planilla'/source.name)

def direct(self,forzar=False):
    Path(self.auxdir).mkdir(parents=True,exist_ok=True)
    text=(BASE/self.fuente).read_text(encoding='utf-8')
    text=text.replace(r'\begin{document}',r'\Version{3.1}\FechaTipoCambio{25 de noviembre de 2026, parámetros convencionales E-24}'+
        '\n'+r'\ImagenMediaFirma{}\ImagenFirmaCompleta{}'+'\n'+r'\begin{document}',1)
    wrapper=Path(self.auxdir)/(self.nombre+'-entrada.tex')
    pre=self.preambulo()
    pre=pre.replace('salida\\aux\\','salida/aux/').replace('final-economica\\','final-economica/')
    wrapper.write_text(pre+'\n'+text,encoding='utf-8')
    for i in [1,2,3]:
        cmd=['lualatex','--disable-installer','-recorder','-interaction=nonstopmode','-halt-on-error',
            '-file-line-error','-jobname='+self.nombre,'-output-directory='+self.auxdir,str(wrapper)]
        with (OUT/'evidencia'/f'{self.clave}-economico-{i}.log').open('w',encoding='utf-8') as log:
            r=subprocess.run(cmd,cwd=BASE,env=ENV,stdout=log,stderr=subprocess.STDOUT,stdin=subprocess.DEVNULL,timeout=180)
        if r.returncode:self.ok=False;return False
        if i==1 and Path(self.auxdir,self.nombre+'.bcf').exists():
            with (OUT/'evidencia'/f'{self.clave}-economico-biber.log').open('w',encoding='utf-8') as log:
                r=subprocess.run(['biber','--input-directory='+self.auxdir,'--output-directory='+self.auxdir,self.nombre],cwd=BASE,env=ENV,stdout=log,stderr=subprocess.STDOUT,timeout=120)
            if r.returncode:self.ok=False;return False
    self.paginas=int(subprocess.check_output(['C:/Program Files/Python311/python.exe','-c','import fitz,sys;print(len(fitz.open(sys.argv[1])))',self.pdf],text=True))
    self.ok=True;print(self.nombre,'folio',self.folio,'páginas',self.paginas,flush=True);return True

def juntar(car,otros,auxbase):
    ruta=Path(auxbase)/'folios-sobre.tex';lines=[]
    for t in [car]+otros:
        for clave,titulo,folio,_ in c.entradas_folio(t.aux):lines.append('\\entradaFolio{%s}{%s}{%s}{%s}'%(clave,titulo,folio,t.nombre))
    ruta.write_text('\n'.join(lines)+'\n',encoding='utf-8');car.extra=r'\def\FoliosSobre{'+ruta.as_posix()+'}'

c.Trabajo.compilar=direct;c.juntar_folios=juntar
if __name__=='__main__':
    jobs=c.economicos(Config(),['economico'],'final-economica',1,True)
    if jobs is None:raise SystemExit('No se pudo completar la compilación económica; consultar logs.')
    for p in (BASE/'salida/final-economica').iterdir():
        if p.suffix.lower() in ['.pdf','.docx','.xlsx','.md','.json']:
            shutil.copy2(p,OUT/'documentos'/p.name)
    print('Documentos económicos preparados, firma humana pendiente.',flush=True)
