"""Extrae insumos versionados sin alterar las planillas de origen."""
import csv,json,os,subprocess
from pathlib import Path
from io import BytesIO
import openpyxl
D=Path(__file__).resolve().parent
R=Path(os.environ['AUDIT_ORIGIN_REPO'])

raw=subprocess.check_output(['git','show','c9a6515:Informe-3/AUDIT-Informe3-Modelo-Economico.xlsx'],cwd=R)
(D/'build/origen.xlsx').write_bytes(raw)
b=openpyxl.load_workbook(BytesIO(raw),data_only=True)
cols=['d4','licencias','calidad','administracion','cierre','personal_anterior','otros','precio_base','garantia','costo_anterior','firma']
costos=[dict(mes=row[0],**dict(zip(cols,row[1:]))) for row in b['Costos'].values if isinstance(row[0],int)]
demanda=list(csv.DictReader((R/'Informe-3/d3/datos/dedicacion_mensual_d3_resumen.csv').open()))
data={'corte':'c9a6515652c3357ea684bf0bb9338b7c4ec028fd','costos':costos,'demanda':demanda,
 'detalle_d3':list(csv.DictReader((R/'Informe-3/d3/datos/dedicacion_mensual_d3.csv').open())),
 'hitos':[(row[0],row[1],row[2]) for row in list(b['Flujo de Caja'].values)[1:] if row[1]],
 'proveedores_d4':list(b['Detalle proveedores D4'].values),
 'hardware_mandante':list(b['Hardware del mandante'].values)}
(D/'insumos.json').write_text(json.dumps(data,ensure_ascii=False,indent=2,default=str)+'\n')
print('Insumos extraídos:',len(costos),'meses y',len(demanda),'meses de demanda D3')
