"""Ejecuta la integración oficial con LuaLaTeX/biber directos en Windows."""
from pathlib import Path
import sys,os,subprocess,time,json,hashlib
import pymupdf

OUT=Path(__file__).resolve().parent
BASE=OUT/'fuentes'
sys.path.insert(0,str(BASE/'herramientas'))
import compilar as c

ENV=os.environ.copy()
ENV['TEXINPUTS']=BASE.as_posix()+'//;'
ENV['BIBINPUTS']=(BASE/'referencias').as_posix()+'//;'
ENV['MIKTEX_ENABLE_INSTALLER']='0'
ENV['PYTHONUTF8']='1'

def count(pdf):
    with pymupdf.open(pdf) as doc:return len(doc)
c.contar_paginas=count

def direct(self,forzar=False):
    begin=time.time()
    aux=Path(self.auxdir);aux.mkdir(parents=True,exist_ok=True)
    pre=self.preambulo()
    wrapper=aux/(self.nombre+'-entrada.tex')
    wrapper.write_text(pre+'\n'+r'\input{'+self.fuente.replace('\\','/')+'}\n',encoding='utf-8')
    signature=c.huella(c.COMUNES+self.carpetas+[self.fuente],pre)
    # El contenido congelado de las referencias externas también es entrada.
    external=aux/'externos.tex'
    if external.exists():
        signature=hashlib.sha256((signature+external.read_text(encoding='utf-8')).encode()).hexdigest()
        frozen=BASE/'salida/aux/final/externos'
        for other in sorted(frozen.glob('*.aux')):
            signature=hashlib.sha256(signature.encode()+other.read_bytes()).hexdigest()
    mark=aux/'huella-directa.txt'
    if not forzar and mark.exists() and mark.read_text()==signature and Path(self.pdf).exists():
        self.ok=True;self.paginas=count(self.pdf);self.segundos=time.time()-begin;return self
    cmd=['lualatex','--disable-installer','-recorder','-interaction=nonstopmode','-halt-on-error','-file-line-error',
         '-jobname='+self.nombre,'-output-directory='+str(aux),str(wrapper)]
    records=[]
    with (aux/'compilacion-directa.txt').open('w',encoding='utf-8') as log:
        for i in range(6):
            r=subprocess.run(cmd,cwd=BASE,env=ENV,stdout=log,stderr=subprocess.STDOUT,stdin=subprocess.DEVNULL,timeout=240)
            records.append({'latex':i+1,'exit':r.returncode})
            if r.returncode:break
            if i==0 and (aux/(self.nombre+'.bcf')).exists():
                b=subprocess.run(['biber','--input-directory='+str(aux),'--output-directory='+str(aux),self.nombre],
                    cwd=BASE,env=ENV,stdout=log,stderr=subprocess.STDOUT,stdin=subprocess.DEVNULL,timeout=180)
                records.append({'biber':b.returncode})
                if b.returncode:r=b;break
            if i>=2 and not self.pide_otra_pasada():break
        self.ok=r.returncode==0 and Path(self.pdf).exists()
    (aux/'resultado-directo.json').write_text(json.dumps(records),encoding='utf-8')
    if self.ok:
        self.paginas=count(self.pdf);mark.write_text(signature)
    self.segundos=time.time()-begin
    return self
c.Trabajo.compilar=direct

if __name__=='__main__':
    if len(sys.argv)>1 and sys.argv[1]=='admin':
        import shutil
        t=c.Trabajo('ADMIN','sobre1-antecedentes.tex','AUDIT-Sobre1-Antecedentes-Administrativos',
                    str(BASE/'salida/aux/administrativo'),'',['administrativo','sobre1-antecedentes.tex'])
        if not c.ejecutar([t],1,True):sys.exit(1)
        dest=BASE/'salida/administrativo';dest.mkdir(parents=True,exist_ok=True)
        shutil.copy2(t.pdf,dest/(t.nombre+'.pdf'))
        (dest/'manifiesto.json').write_text(json.dumps({'grupo':'administrativo','instancia':'final','modo_folio':'unico',
            'archivos':[{'clave':'ADMIN','nombre':t.nombre+'.pdf','folio_inicial':1,'paginas':t.paginas,
            'aux':t.aux,'log':t.log,'fuentes':[['administrativo'],['sobre1-antecedentes.tex']]}]},ensure_ascii=False,indent=2),encoding='utf-8')
        sys.exit(0)
    if len(sys.argv)>1 and sys.argv[1]=='single':
        cfg=c.Config()
        t=c.Trabajo('01','subdocumento.tex',cfg.nombre_subdoc(1),str(BASE/'salida/aux/final/01'),
                    c.OFERTA.preambulo()+r'\def\NumeroSubdoc{1}',['subdocumentos/01-empresa'])
        sys.exit(0 if c.ejecutar([t],1,True) else 1)
    sys.argv=['compilar.py','subdocs','--continuo','--caratula','-j','4']
    sys.exit(c.main())
