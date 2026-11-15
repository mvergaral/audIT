"""Conciliación final y paquete limpio de entrega, sin respaldos internos."""
import hashlib,json,sys,zipfile,re
from pathlib import Path
import openpyxl,pymupdf
from lxml import etree
R=Path(__file__).resolve().parents[2];D=Path(__file__).resolve().parent;O=R/'outputs/informe3-corregido';E=O/'entrega'
sys.path.insert(0,str(R/'recursos/Formato-Oferta-audIT/herramientas'))
import planilla
b=openpyxl.load_workbook(E/'INFORME3_AUDIT_PLANILLA_20261114.xlsx',data_only=True)
f=openpyxl.load_workbook(E/'INFORME3_AUDIT_PLANILLA_20261114.xlsx',data_only=False)
a=openpyxl.load_workbook(D/'build/origen.xlsx',data_only=False)
labels=lambda s:[(c.coordinate,c.value) for row in s for c in row if c.data_type!='f' and isinstance(c.value,str)]
assert labels(a['RESUMEN'])==labels(f['RESUMEN'])
assert len(f.sheetnames)==40 and not f._external_links
assert not [(s.title,c.coordinate,c.value) for s in b for row in s for c in row if c.data_type=='e']
assert all(f[s].protection.sheet for s in ['RESUMEN','Flujo de Caja','Costos','Financiamiento','Resumen Ejecutivo','Escenarios corregidos'])
assert not f['Parámetros corrección']['B4'].protection.locked
assert f['Resumen Ejecutivo']['B4'].number_format=='0.00%'
assert '%' not in f['Resumen Ejecutivo']['B5'].number_format
assert '%' not in f['Resumen Ejecutivo']['B7'].number_format
assert abs(b['Control de entrega']['B21'].value-22050292.4204057)<.001
assert b['Control de entrega']['B5'].value==0
part=planilla.leer_partidas(['../../Informe-3/correccion-final/economico'])
comp=planilla.comparar(str(E/'INFORME3_AUDIT_PLANILLA_20261114.xlsx'),part,{'USD':900,'UF':40000,'EUR':1000})
assert comp and all(x[-1] for x in comp),[x for x in comp if not x[-1]]
m=json.loads((O/'revision/resultados.json').read_text());old=json.loads((O/'revision/resultados-documentos-v3.json').read_text())
for key in ['capital_inicial_clp','costo_clp','venta_clp','van_clp','caja_minima_tesoreria','facilidad_contingente_clp']:assert abs(m[key]-old[key])<.001
for r,s in zip(m['flujo'],old['flujo']):assert all(abs(x-y)<.001 for x,y in zip(r,s))
for key in ['raices_tir_base','raices_tir_escenarios']:m[key]=old[key]
(O/'revision/resultados.json').write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n')
ser=json.loads((O/'revision/series.json').read_text())
expected=[[ser['costos']],[ser['curvaCostos'],ser['curvaVentas'],ser['curvaCaja']],
 [ser['cajaBase'],ser['cajaEstres'],ser['cajaCubierta'],[0]*56],[ser['banco'],ser['socios'],[-x for x in ser['amort']]]]
ns={'c':'http://schemas.openxmlformats.org/drawingml/2006/chart'}
pptx=E/'INFORME3_AUDIT_PRESENTACION_20261114.pptx'
with zipfile.ZipFile(pptx) as z:
 parts=sorted(n for n in z.namelist() if re.fullmatch(r'ppt/slides/charts/chart\d+.xml',n))
 assert len(parts)==4
 for part,rows in zip(parts,expected):
  native=etree.fromstring(z.read(part));series=native.findall('.//c:ser',ns);assert len(series)==len(rows)
  for native_series,vals in zip(series,rows):
   pts=native_series.findall('./c:val/c:numRef/c:numCache/c:pt',ns)
   pts=sorted(pts,key=lambda x:int(x.get('idx')));got=[float(pt.find('c:v',ns).text) for pt in pts]
   assert len(got)==56,(part,len(got))
   assert all(abs(x-y/40000)<=.00501 for x,y in zip(got,vals)),part
pdf=pymupdf.open(E/'INFORME3_AUDIT_COSTOS_VENTA_20261114.pdf')
assert len(pdf)==27
assert len(pymupdf.open(E/'INFORME3_AUDIT_PRESENTACION_20261114.pdf'))==10
txt=' '.join(p.get_text() for p in pdf).casefold()
assert not any(t in txt for t in ['ignacio cuevas','martín cevallos','martin cevallos'])
files=['INFORME3_AUDIT_COSTOS_VENTA_20261114.pdf','INFORME3_AUDIT_PLANILLA_20261114.xlsx','INFORME3_AUDIT_PRESENTACION_20261114.pptx','INFORME3_AUDIT_PRESENTACION_20261114.pdf','LEEME.txt']
target=O/'INFORME3_AUDIT_CORREGIDO_20261114.zip'
with zipfile.ZipFile(target,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
 for name in files:z.write(E/name,name)
with zipfile.ZipFile(target) as z:assert z.testzip() is None and z.namelist()==files
manifest={'zip':str(target),'sha256':hashlib.sha256(target.read_bytes()).hexdigest(),'archivos':[{ 'nombre':n,'bytes':(E/n).stat().st_size,'sha256':hashlib.sha256((E/n).read_bytes()).hexdigest()} for n in files],
 'hojas':40,'formulas':sum(c.data_type=='f' for s in f for row in s for c in row),'celdas_conciliadas':len(comp),'paginas_informe':27,'laminas':10,'graficos_nativos':4,'resumen_conservado':True,'vinculos_externos':0}
(O/'revision/paquete-verificado.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(manifest,ensure_ascii=False,indent=2))
