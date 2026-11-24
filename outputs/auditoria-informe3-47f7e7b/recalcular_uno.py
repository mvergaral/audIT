"""Recalcula íntegramente copias temporales mediante Calc; no abre originales."""
import subprocess
import time
from pathlib import Path
import uno
from com.sun.star.beans import PropertyValue

def propiedad(nombre,valor):
    p=PropertyValue();p.Name=nombre;p.Value=valor;return p

proceso=subprocess.Popen(['libreoffice','-env:UserInstallation=file:///tmp/audit-informe3-uno',
    '--headless','--accept=pipe,name=auditinforme3;urp;StarOffice.ComponentContext','--norestore','--nodefault'],
    stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
contexto=uno.getComponentContext()
resolver=contexto.ServiceManager.createInstanceWithContext('com.sun.star.bridge.UnoUrlResolver',contexto)
for intento in range(40):
    try:
        remoto=resolver.resolve('uno:pipe,name=auditinforme3;urp;StarOffice.ComponentContext');break
    except Exception:
        time.sleep(.25)
else:
    proceso.terminate();raise RuntimeError('No fue posible conectar con Calc')
escritorio=remoto.ServiceManager.createInstanceWithContext('com.sun.star.frame.Desktop',remoto)
salida=Path('/tmp/audit-informe3-native/calculo-completo');salida.mkdir(exist_ok=True)
try:
    for origen in sorted(Path('/tmp/audit-informe3-native/entrada').glob('*.xlsx')):
        doc=escritorio.loadComponentFromURL(uno.systemPathToFileUrl(str(origen)), '_blank',0,
            (propiedad('Hidden',True),propiedad('UpdateDocMode',3),propiedad('ReadOnly',False)))
        doc.calculateAll()
        doc.storeAsURL(uno.systemPathToFileUrl(str(salida/origen.name)),
            (propiedad('FilterName','Calc MS Excel 2007 XML'),propiedad('Overwrite',True)))
        doc.close(True)
        print('Cálculo íntegro:',origen.name,flush=True)
finally:
    escritorio.terminate()
    proceso.wait(timeout=10)
