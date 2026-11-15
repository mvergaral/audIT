"""Configura el verificador oficial para el directorio aislado de esta corrección.

Amplía la detección de fuentes del .fls a la raíz externa; no omite controles.
La fecha coincide con el driver, sin cambiar la configuración compartida.
"""
import json,os,sys,shutil
from itertools import accumulate
from pathlib import Path
import openpyxl,pymupdf
R=Path(__file__).resolve().parents[2];D=Path(__file__).resolve().parent;O=R/'outputs/informe3-mejora'
b=openpyxl.load_workbook(O/'entrega/INFORME3_AUDIT_PLANILLA_20261115.xlsx',data_only=True)
def col(s,c,first=2,last=57):return [b[s][f'{c}{r}'].value for r in range(first,last+1)]
uf=b['Parámetros D2']['B21'].value
data={'costos':col('Costos','K'),'curvaCostos':col('Curva S','B'),'curvaVentas':col('Curva S','C'),'curvaCaja':col('Curva S','D'),
 'cajaBase':col('Flujo de Caja','W'),'cajaEstres':col('Escenarios corregidos','S',126,181),'cajaCubierta':col('Escenarios corregidos','S',188,243),
 'cajaH4':col('Escenarios corregidos','S',436,491),'cotaH4':b['Sensibilidad']['S9'].value,
 'personal':col('Costos','G'),'infra':[x+y for x,y in zip(col('Costos','B'),col('Costos','C'))],
 'otros':[k-g-b-c for k,g,b,c in zip(col('Costos','K'),col('Costos','G'),col('Costos','B'),col('Costos','C'))],
 'ajustada':[x*uf for x in col('Gráficos UF','Q',2,58)],
 'operativo':[x*uf for x in col('Gráficos UF','R',2,58)],
 'cajaApertura':[x*uf for x in col('Gráficos UF','S',2,58)],
 'banco':col('Flujo de Caja','AB'),'socios':col('Flujo de Caja','AC'),'amort':col('Flujo de Caja','U'),'soporte':col('Personal','D',22,57),
 'finDeuda':max(b['Flujo de Caja'][f'A{r}'].value for r in range(2,59) if b['Flujo de Caja'][f'U{r}'].value>0),
 'montajeNeto':sum(col('Instalación por lote','H',2,21)),
 'innovaciones':[[b['Innovaciones'][f'B{r}'].value,b['Innovaciones'][f'C{r}'].value,b['Innovaciones'][f'D{r}'].value,k] for r,k in zip(range(2,7),['Minutos y adopción','Visitas y preparación','Acoples y eventos térmicos','Recupero neto compartido','Consumo y siniestralidad'])]}
data['brecha']=min(range(57),key=lambda i:data['ajustada'][i]-data['operativo'][i])
maturity=next(r for r in range(2,b['Escenarios corregidos'].max_row+1)
              if b['Escenarios corregidos'][f'A{r}'].value=='Soporte por madurez 3.0')
def mad(c):return col('Escenarios corregidos',c,maturity,maturity+55)
data['madurezOperativo']=[0,*accumulate(a+b for a,b in zip(mad('E'),mad('F')))]
data['madurezCajaApertura']=[data['cajaApertura'][0],
                           *(saldo-iva for saldo,iva in zip(mad('S'),accumulate(mad('L'))))]
assert all(abs(a-b)<.01 for a,b in zip(accumulate(mad('C')),data['curvaVentas']))
for origen,escenario in [('P','J'),('Q','K'),('U','Q'),('R','N'),('S','O'),('AB','H')]:
    base=col('Flujo de Caja',origen)
    if origen=='AB':
        base=[banco+socios for banco,socios in zip(base,col('Flujo de Caja','AC'))]
    assert all(abs(a-b)<.01 for a,b in zip(base,mad(escenario)))
assert all(abs(caja_madurez-caja_base+costos_madurez-costos_base)<.01
           for caja_madurez,caja_base,costos_madurez,costos_base
           in zip(data['madurezCajaApertura'],data['cajaApertura'],data['madurezOperativo'],data['operativo']))
(O/'revision/series.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
if '--series-only' in sys.argv:sys.exit(0)
name='INFORME3_AUDIT_COSTOS_VENTA_20261115'
shutil.copy2(O/f'revision/latex/{name}.pdf',O/f'entrega/{name}.pdf')
pdf=pymupdf.open(O/f'entrega/{name}.pdf');preview=O/'revision/paginas';preview.mkdir(exist_ok=True)
for i,p in enumerate(pdf):p.get_pixmap(matrix=pymupdf.Matrix(.7,.7)).save(preview/f'{i+1:02d}.png')
texroot=Path(os.environ['AUDIT_TEX_ROOT'])
rel=lambda p:os.path.relpath(p,texroot)
entry={'clave':'costos','nombre':name+'.pdf','folio_inicial':1,'paginas':len(pdf),'aux':rel(O/f'revision/latex/{name}.aux'),'log':rel(O/f'revision/latex/{name}.log'),'eco':name+'.eco.json','fuentes':[[rel(D/'economico')]]}
man={'grupo':'informe3-mejora','instancia':'informe3','tipo':'economico','modo_folio':'subdocumento','archivos':[entry],'planilla':'INFORME3_AUDIT_PLANILLA_20261115.xlsx'}
mp=O/'entrega/manifiesto.json';mp.write_text(json.dumps(man,ensure_ascii=False,indent=2)+'\n')
sys.path.insert(0,str(texroot/'herramientas'));import verificar
fuentes_original=verificar.fuentes_de;contenido_original=verificar.es_contenido
verificar.fuentes_de=lambda aux:sorted(set(fuentes_original(aux)+[str(D/'documento.tex'),str(D/'observaciones.tex'),str(D/'economico/costos-venta/contenido.tex')]))
verificar.es_contenido=lambda ruta:contenido_original(ruta) or Path(ruta).is_relative_to(D)
cfg=verificar.Config('informe3');cfg.fecha='2026-11-15'
sys.exit(1 if verificar.verificar_grupo(str(mp),cfg) else 0)
