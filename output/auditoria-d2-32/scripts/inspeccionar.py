from pathlib import Path
import json, hashlib
import openpyxl

root = Path(__file__).parent
p = next((root/'fuentes/outputs/3.2/Entrega-3.2').glob('*.xlsx'))
wb = openpyxl.load_workbook(p, data_only=True)
wf = openpyxl.load_workbook(p, data_only=False)
print('SHA256', hashlib.sha256(p.read_bytes()).hexdigest())
print('HOJAS', [(s.title,s.max_row,s.max_column) for s in wb])
selected = ['Parámetros corrección','Parámetros D2','Feedback 3.2','Contrato de soporte','Hitos E25','Control de entrega','Resumen Ejecutivo','Indicadores','Tarifas por perfil','Instalación por lote','Dotación por perfil','Soporte por perfil','Costos','Amortización','Innovaciones','Conciliación técnica','Mesa de ayuda','RESUMEN']
for name in selected:
    if name not in wb: continue
    lines=[]
    for row in wb[name]:
        vals=[f'{c.coordinate}={c.value}' for c in row if c.value is not None]
        if vals: lines.append(' | '.join(vals))
    (root/(name.replace('/','-')+'.txt')).write_text('\n'.join(lines),encoding='utf-8')
errors=[(s.title,c.coordinate,c.value) for s in wb for row in s for c in row if c.data_type=='e']
print('ERRORES_CACHE', errors)
stats={}
for name in ['Dotación por perfil','Soporte por perfil']:
    s=wb[name]
    print(name,'HEADERS', [c.value for c in s[1]])
    by_month={}
    for row in s.iter_rows(min_row=2,values_only=True):
        if isinstance(row[0],int):
            arr=by_month.setdefault(row[0],[0]*len(row))
            for i,v in enumerate(row):
                if i>1 and isinstance(v,(int,float)): arr[i]+=v
    stats[name]=by_month
(root/'totales-mensuales.json').write_text(json.dumps(stats,indent=2,ensure_ascii=False),encoding='utf-8')
print('HORAS_IMPLEMENTACION', sum(v[8] for v in stats['Dotación por perfil'].values()))
print('HORAS_OPERACION', sum(v[6] for v in stats['Soporte por perfil'].values()))
print('DOTACION_MENSUAL', [(m,round(v[8],3),round(v[8]/160,4)) for m,v in stats['Dotación por perfil'].items()])
print('SOPORTE_MENSUAL', [(m,round(v[6],3),round(v[6]/160,4)) for m,v in stats['Soporte por perfil'].items() if m in [21,22,23,24,25,32,33,44,45,56]])
print('SOPORTE_POR_PAQUETE')
for packet in ['13.1','13.2','13.3','13.4','6.5']:
    rows=[r for r in wb['Soporte por perfil'].iter_rows(min_row=2,values_only=True) if packet in str(r[1])]
    print(packet,sum(r[6] or 0 for r in rows))
import re, subprocess
base='recursos/Formato-Oferta-audIT/subdocumentos/'
targets=['03-solucion/contenido.tex','03-solucion/formularios/T-12.tex','07-plan-trabajo/contenido.tex','07-plan-trabajo/formularios/T-14.tex','07-plan-trabajo/formularios/T-15.tex','07-plan-trabajo/formularios/T-18.tex']
print('VERSIONES_FUENTES')
for t in targets:
    rp=base+t
    snap=(root/'fuentes'/rp).read_bytes()
    for label, pth in [('main',Path(rp)),('worktree',Path('tmp/cierre-entrega-3')/rp)]:
        if pth.exists():
            same=pth.read_text(encoding='utf-8')==snap.decode('utf-8').replace('\r\n','\n')
            print(t,label,'IGUAL' if same else 'DIFERENTE')
req=(root/'fuentes'/base/'03-solucion/formularios/T-12.tex').read_text(encoding='utf-8')
ids=re.findall(r'id\s*=\s*((?:RNF|RF)-\d+)',req)
print('REQUISITOS_T12',len(ids),len(set(ids)))
for name in ['03-solucion/formularios/trazabilidad-secciones.tex','07-plan-trabajo/formularios/trazabilidad-aceptacion.tex']:
    text=(root/'fuentes'/base/name).read_text(encoding='utf-8')
    present=set(re.findall(r'(?:RNF|RF)-\d+',text))
    print('TRAZABILIDAD',name,len(present),'FALTANTES',sorted(set(ids)-present))
try:
    from pypdf import PdfReader
    for pdf in (root/'fuentes'/base/'07-plan-trabajo').rglob('*.pdf'):
        if 'version-anterior' in pdf.parts: continue
        if ('preparacion-final' in pdf.parts or pdf.name=='S7_Integrado_Revision.pdf' or pdf.name.startswith('gantt-') or 'edt-revisada' in pdf.parts):
            doc=PdfReader(pdf)
            content='\n'.join(f'\n=== PAGINA PDF {i+1} ===\n'+page.extract_text() for i,page in enumerate(doc.pages))
            dest=root/'pdf-textos'/pdf.relative_to(root/'fuentes')
            dest=dest.with_suffix('.txt'); dest.parent.mkdir(parents=True,exist_ok=True)
            dest.write_text(content,encoding='utf-8')
    print('PDF extraidos')
except ImportError as exc: print('SIN_PYMUPDF',exc)
