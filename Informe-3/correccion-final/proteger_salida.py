"""Extiende la protección nativa a las vistas calculadas de la plantilla."""
import json,subprocess,time
from pathlib import Path
import uno
from com.sun.star.beans import PropertyValue
R=Path(__file__).resolve().parents[2];O=R/'outputs/informe3-corregido'
def prop(n,v):p=PropertyValue();p.Name=n;p.Value=v;return p
proc=subprocess.Popen(['libreoffice','-env:UserInstallation=file:///tmp/audit-informe3-proteccion','--headless','--accept=pipe,name=auditproteccion;urp;StarOffice.ComponentContext','--norestore','--nodefault'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
local=uno.getComponentContext();res=local.ServiceManager.createInstanceWithContext('com.sun.star.bridge.UnoUrlResolver',local)
for _ in range(60):
 try:ctx=res.resolve('uno:pipe,name=auditproteccion;urp;StarOffice.ComponentContext');break
 except Exception:time.sleep(.2)
desk=ctx.ServiceManager.createInstanceWithContext('com.sun.star.frame.Desktop',ctx)
doc=desk.loadComponentFromURL(uno.systemPathToFileUrl(str(O/'entrega/INFORME3_AUDIT_PLANILLA_20261114.xlsx')),'_blank',0,(prop('Hidden',True),))
def c(s,a):return doc.Sheets.getByName(s).getCellRangeByName(a)
try:
 before=[c(s,a).Value for s,a in [('RESUMEN','C8'),('RESUMEN','H8'),('Indicadores','B2'),('Control de entrega','B21')]]
 for sn in ['RESUMEN','PARÁMETROS','FLUJO DE CAJA COMPLETO','FLUJO DE CAJA NETO','COSTOS DE OPERACION','PUENTE D2','Conciliación IVA','Hitos E25']:doc.Sheets.getByName(sn).protect('')
 doc.calculateAll()
 after=[c(s,a).Value for s,a in [('RESUMEN','C8'),('RESUMEN','H8'),('Indicadores','B2'),('Control de entrega','B21')]]
 delta=max(abs(x-y) for x,y in zip(before,after))
 assert delta<.0001,(before,after)
 errors=[sh.Name for sh in doc.Sheets if sh.queryFormulaCells(uno.getConstantByName('com.sun.star.sheet.FormulaResult.ERROR')).Count]
 assert not errors,errors
 unlocked={f'{s}!{a}':not c(s,a).CellProtection.IsLocked for s,a in [('Parámetros corrección','B4'),('Parámetros corrección','B28'),('Parámetros D2','B13'),('Tarifas por perfil','B10'),('Contrato de soporte','B2')]}
 assert all(unlocked.values()),unlocked
 doc.store()
 (O/'revision/proteccion-final.json').write_text(json.dumps({'tolerancia_clp':.0001,'diferencia_maxima_clp':delta,'sin_errores':True,'entradas_desbloqueadas':unlocked},ensure_ascii=False,indent=2)+'\n')
finally:doc.close(True);desk.terminate();proc.wait(timeout=10)
