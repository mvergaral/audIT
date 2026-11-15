"""Recálculo nativo, dimensionamiento de entradas y protección de fórmulas en Calc.

La autoría del libro se realiza en modelo.mjs con Artifact Tool. Aquí se usan
calculateAll y las capacidades nativas de Goal Seek/protección no documentadas
en la superficie de autoría disponible. Nunca se altera el archivo de origen.
"""
import json,subprocess,time
from pathlib import Path
import uno
from com.sun.star.beans import PropertyValue
R=Path(__file__).resolve().parents[2]
O=R/'outputs/informe3-corregido'
def prop(n,v):
 p=PropertyValue();p.Name=n;p.Value=v;return p
proc=subprocess.Popen(['libreoffice','-env:UserInstallation=file:///tmp/audit-informe3-cierre-uno','--headless',
 '--accept=pipe,name=auditcierrefinal;urp;StarOffice.ComponentContext','--norestore','--nodefault'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
local=uno.getComponentContext();resolver=local.ServiceManager.createInstanceWithContext('com.sun.star.bridge.UnoUrlResolver',local)
for _ in range(80):
 try:ctx=resolver.resolve('uno:pipe,name=auditcierrefinal;urp;StarOffice.ComponentContext');break
 except Exception:time.sleep(.25)
else:proc.terminate();raise RuntimeError('No conectó Calc')
desktop=ctx.ServiceManager.createInstanceWithContext('com.sun.star.frame.Desktop',ctx)
doc=desktop.loadComponentFromURL(uno.systemPathToFileUrl(str(O/'revision/modelo-borrador-v4.xlsx')),'_blank',0,(prop('Hidden',True),prop('UpdateDocMode',3)))
def cell(s,a):return doc.Sheets.getByName(s).getCellRangeByName(a)
def val(s,a):return cell(s,a).Value
try:
 for sh in doc.Sheets:
  if sh.isProtected():sh.unprotect('')
 for name in ['Cotejo D1','Criterios y pendientes','Capacidad por perfil','Refuerzo presupuestado','Escenarios de caja']:
  if doc.Sheets.hasByName(name):doc.Sheets.removeByName(name)
 doc.calculateAll()
 # Entradas explícitas dimensionadas por búsqueda, no celdas de resultado forzadas.
 floor=val('Parámetros corrección','B3')
 def base_min(capital):
  cell('Parámetros corrección','B4').Value=capital;doc.calculateAll()
  return min(val('Control de entrega','B2'),val('Control de entrega','B3'),val('Control de entrega','B21'))
 lo,hi=0,2_000_000_000
 assert base_min(hi)>=floor,'El rango presupuestario no cubre la base'
 while lo<hi:
  mid=(lo+hi)//2
  if base_min(mid)>=floor:hi=mid
  else:lo=mid+1
 minimo=lo
 # Redondeo hacia arriba a CLP 5 millones: no una holgura menor a un peso.
 capital=((minimo+4_999_999)//5_000_000)*5_000_000
 base_min(capital)
 # Dimensiona facilidad del estrés de dos meses y reserva, con el mismo precio.
 def stress_min(funds):
  cell('Parámetros corrección','B28').Value=funds;doc.calculateAll()
  return min(val('Sensibilidad','G5'),val('Sensibilidad','G8'),val('Sensibilidad','S5'),val('Sensibilidad','S8'))
 lo,hi=0,2_000_000_000
 assert stress_min(hi)>=floor,'El rango presupuestario no cubre el estrés'
 while lo<hi:
  mid=(lo+hi)//2
  if stress_min(mid)>=floor:hi=mid
  else:lo=mid+1
 puente=((lo+4_999_999)//5_000_000)*5_000_000
 stress_min(puente)
 # Serie de control y salidas para documentación, siempre desde el libro recalculado.
 metrics={
  'capital_inicial_clp':capital,'capital_minimo_modelo_clp':minimo,'facilidad_contingente_clp':puente,
  'costo_clp':sum(val('Costos',f'K{r}') for r in range(2,58)),
  'venta_clp':sum(val('Ingresos',f'E{r}') for r in range(2,58)),
  'implementacion_clp':val('Parámetros D2','B14'),'mensualidad_clp':val('Parámetros D2','B15'),
  'van_clp':val('Indicadores','B2'),'tir_mensual':val('Indicadores','B3'),'margen':val('Indicadores','B10'),
  'tasa_mensual':val('Parámetros D2','B10'),'caja_minima_tesoreria':val('Control de entrega','B2'),
  'caja_minima_neta':val('Control de entrega','B3'),'linea_base_maxima':val('Control de entrega','B5'),
  'controles':[(cell('Control de entrega',f'A{r}').String,val('Control de entrega',f'B{r}')) for r in range(2,22)],
  'escenarios':[[cell('Sensibilidad',f'A{r}').String,*[val('Sensibilidad',f'{c}{r}') for c in 'GHIJKLMNOPQ'],val('Sensibilidad',f'S{r}')] for r in range(2,9)],
  'flujo':[[val('Flujo de Caja',f'{c}{r}') for c in ['A','E','F','G','H','O','P','Q','R','S','T','U','V','W','AA','AB','AC','AD']] for r in range(2,59)],
  'costos':[[val('Costos',f'{c}{r}') for c in ['A','B','C','D','E','F','G','H','I','J','K','L']] for r in range(2,58)],
  'soporte_mensual':[[m,val('Personal',f'D{m+1}')] for m in range(21,57)],
  'instalacion':[[cell('Instalación por lote',f'B{r}').String,*[val('Instalación por lote',f'{c}{r}') for c in ['A','C','D','E','F','G','H','I','J','K']]] for r in range(2,22)]}
 errors=[]
 for sh in doc.Sheets:
  for rg in sh.queryFormulaCells(uno.getConstantByName('com.sun.star.sheet.FormulaResult.ERROR')).RangeAddresses:
   errors.append([sh.Name,rg.StartColumn+1,rg.StartRow+1,rg.EndColumn+1,rg.EndRow+1])
 metrics['errores']=errors
 (O/'revision/resultados.json').write_text(json.dumps(metrics,ensure_ascii=False,indent=2)+'\n')
 print(json.dumps({k:v for k,v in metrics.items() if k not in ['flujo','costos','soporte_mensual','instalacion']},ensure_ascii=False,indent=2),flush=True)
 if errors:raise RuntimeError(f'{len(errors)} errores de recálculo')
 # Protección contra edición accidental: entradas azules quedan desbloqueadas.
 for sn in ['RESUMEN','PARÁMETROS','FLUJO DE CAJA COMPLETO','FLUJO DE CAJA NETO','COSTOS DE OPERACION','PUENTE D2','Conciliación IVA','Hitos E25','Flujo de Caja','Ingresos','Financiamiento','Costos','Personal','Indicadores','Curva S','Gráficos UF','Control de entrega','Resumen Ejecutivo','Escenarios corregidos','Cuadro maestro','Dotación por perfil','Soporte por perfil','Atribución innovaciones','Innovaciones','Beneficios Curimón']:
  doc.Sheets.getByName(sn).protect('')
 for sn,ranges in {'Parámetros corrección':['B2:B56'],'Parámetros D2':['B2:B3','B5:B9','B11:B13','B19:B26','B30:B34'],
  'Tarifas por perfil':['B2:I20'],'Contrato de soporte':['B2:D13'],'Sensibilidad':['B2:F8'],'Instalación por lote':['L2:L21']}.items():
  sh=doc.Sheets.getByName(sn)
  for ar in ranges:
   rng=sh.getCellRangeByName(ar);cp=rng.CellProtection;cp.IsLocked=False;rng.CellProtection=cp
  sh.protect('')
 path=O/'entrega/INFORME3_AUDIT_PLANILLA_20261114.xlsx'
 doc.storeAsURL(uno.systemPathToFileUrl(str(path)),(prop('FilterName','Calc MS Excel 2007 XML'),prop('Overwrite',True)))
 print('Planilla cerrada:',path,flush=True)
finally:
 doc.close(True);desktop.terminate();proc.wait(timeout=10)
