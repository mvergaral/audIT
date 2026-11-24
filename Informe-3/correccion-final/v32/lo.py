"""Utilidades UNO: abrir xlsx en LibreOffice headless, editar, recalcular, guardar."""
import subprocess, time, uno, os, sys
from com.sun.star.beans import PropertyValue
def P(n,v):
    p=PropertyValue(); p.Name=n; p.Value=v; return p
_proc=None
def connect():
    global _proc
    port=int(os.environ.get('LO_PUERTO','2202'))
    _proc=subprocess.Popen([os.environ.get('LO_EJECUTABLE','soffice'),'--headless','--invisible','--nologo','--norestore',
        '-env:UserInstallation=file://'+os.environ.get('LO_PERFIL','/tmp/lo-perfil-audit')+'',
        f'--accept=socket,host=localhost,port={port};urp;'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
    ctx=uno.getComponentContext()
    res=ctx.ServiceManager.createInstanceWithContext('com.sun.star.bridge.UnoUrlResolver',ctx)
    c=None
    for _ in range(60):
        try:
            c=res.resolve(f'uno:socket,host=localhost,port={port};urp;StarOffice.ComponentContext'); break
        except Exception: time.sleep(0.5)
    if c is None:
        if _proc.poll() is None:
            _proc.terminate()
            _proc.wait(timeout=10)
        raise RuntimeError(f'LibreOffice no responde en el puerto {port}; revisar LO_EJECUTABLE, LO_PERFIL y LO_PUERTO.')
    return c.ServiceManager.createInstanceWithContext('com.sun.star.frame.Desktop',c)
def open_doc(desk,path):
    return desk.loadComponentFromURL(uno.systemPathToFileUrl(os.path.abspath(path)),'_blank',0,(P('Hidden',True),))
def save_xlsx(doc,path):
    doc.storeToURL(uno.systemPathToFileUrl(os.path.abspath(path)),(P('FilterName','Calc MS Excel 2007 XML'),))
def close(desk):
    try: desk.terminate()
    except Exception: pass
    if _proc: _proc.wait(timeout=30)
