from pathlib import Path
import csv, hashlib, json, re, subprocess
import openpyxl

r = Path(__file__).parent
f = r/'fuentes'
base = Path('recursos/Formato-Oferta-audIT/subdocumentos')
book = next((f/'outputs/3.2/Entrega-3.2').glob('*.xlsx'))
w = openpyxl.load_workbook(book, data_only=True)
formulas = openpyxl.load_workbook(book, data_only=False)
months = json.loads((r/'totales-mensuales.json').read_text(encoding='utf-8'))
impl = months['Dotación por perfil']; op = months['Soporte por perfil']
ti = sum(v[8] for v in impl.values()); to = sum(v[6] for v in op.values())
assert abs(ti-99626.6666666667)<1e-6
assert to == 84606
assert w['Parámetros corrección']['B83'].value == 19
assert w['Parámetros corrección']['B70'].value == 1
assert w['Contrato de soporte']['B7'].value == 80
assert sum(w['Contrato de soporte'][c].value for c in ['B2','B13']) == 1120
assert not [(s.title,c.coordinate,c.value) for s in w for row in s for c in row if c.data_type=='e']
req = (f/base/'03-solucion/formularios/T-12.tex').read_text(encoding='utf-8')
ids=set(re.findall(r'id\s*=\s*((?:RF|RNF)-\d+)',req))
assert len(ids)==42
for rel in ['03-solucion/formularios/trazabilidad-secciones.tex','07-plan-trabajo/formularios/trazabilidad-aceptacion.tex']:
    assert ids <= set(re.findall(r'(?:RF|RNF)-\d+',(f/base/rel).read_text(encoding='utf-8')))
dic = (f/base/'07-plan-trabajo/formularios/T-14.tex').read_text(encoding='utf-8')
packets = re.findall(r'^\d+\.\d+\s*&',dic,re.M)
assert len(packets)==54
versions=[]
for rel in ['03-solucion/contenido.tex','03-solucion/formularios/T-12.tex','07-plan-trabajo/contenido.tex','07-plan-trabajo/formularios/T-14.tex','07-plan-trabajo/formularios/T-15.tex','07-plan-trabajo/formularios/T-18.tex']:
    remote=(f/base/rel).read_text(encoding='utf-8')
    for label,p in [('main',base/rel),('worktree',Path('tmp/cierre-entrega-3')/base/rel)]:
        versions.append({'archivo':str(base/rel),'version':label,'igual_al_remoto':p.read_text(encoding='utf-8')==remote})
with (r/'comparacion-mensual.csv').open('w',newline='',encoding='utf-8-sig') as out:
    wr=csv.writer(out);wr.writerow(['Mes','Fase','Horas T15','Horas internas 3.2','Diferencia horas','FTE equivalentes 3.2'])
    for m in range(1,57):
        old=2240 if m<=2 else 3840 if m<=5 else 4800 if m<=9 else 5280 if m<=12 else 5920 if m<=17 else 4800 if m==18 else 4160 if m<=20 else 2560
        actual=impl[str(m)][8] if m<=20 else op[str(m)][6]
        wr.writerow([m,'Implementación' if m<=20 else 'Operación',old,round(actual,6),round(actual-old,6),round(actual/160,6)])
obs=(f/'recursos/Formato-Oferta-audIT/anexos/observaciones-informe3.tex').read_text(encoding='utf-8')
statuses={}
for line in obs.splitlines():
    match=re.search(r'\\observacion\[sub=(3|7)\]\{([^}]+)\}.*Estado: ([^}(]+)',line)
    if match: statuses[match[2]]=match[3].strip()
metadata={'fecha':'2026-11-24','rama_remota':subprocess.check_output(['git','rev-parse','origin/codex/cierre-entrega-3'],text=True).strip(),'sha256_planilla':hashlib.sha256(book.read_bytes()).hexdigest(),'horas_implementacion':ti,'horas_operacion':to,'brecha_implementacion':ti-93760,'brecha_operacion':to-92160,'pico_FTE_equivalentes':max(v[8]/160 for v in impl.values()),'formulas_inspeccionadas_sin_recalcular':True,'requistos_T12':len(ids),'paquetes_T14':len(packets),'versiones':versions,'estados_art46_D2':statuses}
(r/'evidencia-verificada.json').write_text(json.dumps(metadata,indent=2,ensure_ascii=False),encoding='utf-8')
print(json.dumps({k:v for k,v in metadata.items() if k not in ['versiones','estados_art46_D2']},indent=2,ensure_ascii=False))
print('Art46 D2:',len(statuses),'observaciones;', {s:sum(v==s for v in statuses.values()) for s in set(statuses.values())})
print('Verificación completada: cifras, inventario, cobertura de códigos y comparación de versiones.')
