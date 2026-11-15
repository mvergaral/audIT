"""Prueba entradas representativas mediante recálculo completo de copias en memoria."""
import json,subprocess,time
from pathlib import Path
import uno
from com.sun.star.beans import PropertyValue
R=Path(__file__).resolve().parents[2];O=R/'outputs/informe3-corregido'
def prop(n,v):p=PropertyValue();p.Name=n;p.Value=v;return p
proc=subprocess.Popen(['libreoffice','-env:UserInstallation=file:///tmp/audit-informe3-pruebas','--headless','--accept=pipe,name=auditpruebas;urp;StarOffice.ComponentContext','--norestore','--nodefault'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
local=uno.getComponentContext();res=local.ServiceManager.createInstanceWithContext('com.sun.star.bridge.UnoUrlResolver',local)
for _ in range(60):
 try:ctx=res.resolve('uno:pipe,name=auditpruebas;urp;StarOffice.ComponentContext');break
 except Exception:time.sleep(.2)
desk=ctx.ServiceManager.createInstanceWithContext('com.sun.star.frame.Desktop',ctx)
def openbook():return desk.loadComponentFromURL(uno.systemPathToFileUrl(str(O/'entrega/INFORME3_AUDIT_PLANILLA_20261114.xlsx')),'_blank',0,(prop('Hidden',True),prop('ReadOnly',True)))
def c(doc,s,a):return doc.Sheets.getByName(s).getCellRangeByName(a)
def snapshot(doc):return {f'{s}!{a}':c(doc,s,a).Value for s,a in [('RESUMEN','C8'),('RESUMEN','H8'),('Indicadores','B2'),('Control de entrega','B21'),('Flujo de Caja','F13'),('Flujo de Caja','F14'),('Personal','D26'),('Gráficos UF','B10'),('Gráficos UF','E10')]}
results=[]
try:
 for label,s,a,fn,expected in [
  ('Capital inicial','Parámetros corrección','B4',lambda x:x-50_000_000,['Control de entrega!B21']),
  ('Tarifa desarrollo','Tarifas por perfil','B10',lambda x:x*1.1,['RESUMEN!C8','RESUMEN!H8','Indicadores!B2']),
  ('Mes de cobro H5','Parámetros D2','B13',lambda x:13,['Flujo de Caja!F13','Flujo de Caja!F14','Indicadores!B2']),
  ('Factor soporte M25','Parámetros corrección','B13',lambda x:1,['Personal!D26','RESUMEN!C8','RESUMEN!H8'])]:
  doc=openbook();doc.calculateAll();before=snapshot(doc);x=c(doc,s,a).Value;c(doc,s,a).Value=fn(x);doc.calculateAll();after=snapshot(doc)
  assert all(abs(after[k]-before[k])>1 for k in expected),(label,before,after)
  errors=[]
  # Consulta nativa de todas las celdas con error: evita decenas de miles de llamadas remotas.
  for sh in doc.Sheets:
   for rg in sh.queryFormulaCells(uno.getConstantByName('com.sun.star.sheet.FormulaResult.ERROR')).RangeAddresses:errors.append([sh.Name,rg.StartColumn,rg.StartRow])
  assert not errors,(label,errors)
  results.append({'prueba':label,'entrada':f'{s}!{a}','antes':x,'despues':fn(x),'salidas_antes':before,'salidas_despues':after,'sin_errores':True})
  doc.close(True)
 (O/'revision/pruebas-propagacion.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')
 print(json.dumps(results,ensure_ascii=False,indent=2))
finally:desk.terminate();proc.wait(timeout=10)
