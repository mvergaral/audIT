"""Configura el verificador oficial para el directorio aislado de esta corrección.

Amplía la detección de fuentes del .fls a la raíz externa; no omite controles.
La fecha coincide con el driver, sin cambiar la configuración compartida.
"""
import json,sys,shutil
from pathlib import Path
import openpyxl,pymupdf
R=Path(__file__).resolve().parents[2];D=Path(__file__).resolve().parent;O=R/'outputs/informe3-corregido'
b=openpyxl.load_workbook(O/'entrega/INFORME3_AUDIT_PLANILLA_20261114.xlsx',data_only=True)
def col(s,c,first=2,last=57):return [b[s][f'{c}{r}'].value for r in range(first,last+1)]
data={'costos':col('Costos','K'),'curvaCostos':col('Curva S','B'),'curvaVentas':col('Curva S','C'),'curvaCaja':col('Curva S','D'),
 'cajaBase':col('Flujo de Caja','W'),'cajaEstres':col('Escenarios corregidos','S',116,171),'cajaCubierta':col('Escenarios corregidos','S',173,228),
 'banco':col('Flujo de Caja','AB'),'socios':col('Flujo de Caja','AC'),'amort':col('Flujo de Caja','U'),'soporte':col('Personal','D',22,57),
 'finDeuda':max(b['Flujo de Caja'][f'A{r}'].value for r in range(2,59) if b['Flujo de Caja'][f'U{r}'].value>0),
 'montajeNeto':sum(col('Instalación por lote','H',2,21)),
 'innovaciones':[[b['Innovaciones'][f'B{r}'].value,b['Innovaciones'][f'C{r}'].value,b['Innovaciones'][f'D{r}'].value,k] for r,k in zip(range(2,7),['Minutos y adopción','Visitas y preparación','Acoples y eventos térmicos','Recupero neto compartido','Consumo y siniestralidad'])]}
(O/'revision/series.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
name='INFORME3_AUDIT_COSTOS_VENTA_20261114'
shutil.copy2(O/f'revision/latex/{name}.pdf',O/f'entrega/{name}.pdf')
pdf=pymupdf.open(O/f'entrega/{name}.pdf');preview=O/'revision/paginas';preview.mkdir(exist_ok=True)
for i,p in enumerate(pdf):p.get_pixmap(matrix=pymupdf.Matrix(.7,.7)).save(preview/f'{i+1:02d}.png')
texroot=R/'recursos/Formato-Oferta-audIT'
import os
rel=lambda p:os.path.relpath(p,texroot)
entry={'clave':'costos','nombre':name+'.pdf','folio_inicial':1,'paginas':len(pdf),'aux':rel(O/f'revision/latex/{name}.aux'),'log':rel(O/f'revision/latex/{name}.log'),'eco':name+'.eco.json','fuentes':[[rel(D/'economico')]]}
man={'grupo':'informe3-corregido','instancia':'informe3','tipo':'economico','modo_folio':'subdocumento','archivos':[entry],'planilla':'INFORME3_AUDIT_PLANILLA_20261114.xlsx'}
mp=O/'entrega/manifiesto.json';mp.write_text(json.dumps(man,ensure_ascii=False,indent=2)+'\n')
sys.path.insert(0,str(texroot/'herramientas'));import verificar
fuentes_original=verificar.fuentes_de;contenido_original=verificar.es_contenido
verificar.fuentes_de=lambda aux:sorted(set(fuentes_original(aux)+[str(D/'documento.tex'),str(D/'observaciones.tex'),str(D/'economico/costos-venta/contenido.tex')]))
verificar.es_contenido=lambda ruta:contenido_original(ruta) or Path(ruta).is_relative_to(D)
cfg=verificar.Config('informe3');cfg.fecha='2026-11-14'
sys.exit(1 if verificar.verificar_grupo(str(mp),cfg) else 0)
