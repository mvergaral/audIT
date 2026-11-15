"""Utilidades UNO: abrir xlsx en LibreOffice headless, editar, recalcular, guardar."""
import subprocess, time, uno, os, sys
from com.sun.star.beans import PropertyValue
def P(n,v):
    p=PropertyValue(); p.Name=n; p.Value=v; return p
_proc=None
def connect():
    global _proc
    _proc=subprocess.Popen(['soffice','--headless','--invisible','--nologo','--norestore',
        '-env:UserInstallation=file://'+os.environ.get('LO_PERFIL','/tmp/lo-perfil-audit')+'',
        '--accept=socket,host=localhost,port=2202;urp;'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
    ctx=uno.getComponentContext()
    res=ctx.ServiceManager.createInstanceWithContext('com.sun.star.bridge.UnoUrlResolver',ctx)
    for _ in range(60):
        try:
            c=res.resolve('uno:socket,host=localhost,port=2202;urp;StarOffice.ComponentContext'); break
        except Exception: time.sleep(0.5)
    return c.ServiceManager.createInstanceWithContext('com.sun.star.frame.Desktop',c)
def open_doc(desk,path):
    return desk.loadComponentFromURL(uno.systemPathToFileUrl(os.path.abspath(path)),'_blank',0,(P('Hidden',True),))
def save_xlsx(doc,path):
    doc.storeToURL(uno.systemPathToFileUrl(os.path.abspath(path)),(P('FilterName','Calc MS Excel 2007 XML'),))
def close(desk):
    try: desk.terminate()
    except Exception: pass
    if _proc: _proc.wait(timeout=30)
