from pathlib import Path
import re,json,hashlib

OUT=Path(__file__).resolve().parent
BASE=OUT/'fuentes'
changes=[]
def save(path,text,reason):
    before=path.read_text(encoding='utf-8')
    if before==text:return
    rel=path.relative_to(BASE)
    backup=OUT/'evidencia/originales'/rel
    backup.parent.mkdir(parents=True,exist_ok=True)
    if not backup.exists():backup.write_text(before,encoding='utf-8')
    path.write_text(text,encoding='utf-8')
    changes.append({'archivo':str(rel),'motivo':reason,'antes_sha256':hashlib.sha256(before.encode()).hexdigest(),'despues_sha256':hashlib.sha256(text.encode()).hexdigest()})

# La identidad del revisor original se conserva en los originales de evidencia.
people={r'Carlos(?: Jesús)? Abarza(?: Calderón)?':'D1',r'Naomi N[uú]ñez':'responsable de Calidad',
        r'Ignacio Vera':'responsable de Arquitectura',r'Marcel Guti[eé]rrez':'responsable de Arquitectura',
        r'Ignacio Cuevas':'D2',r'Mat[ií]as Vergara':'D2'}
for path in (BASE/'subdocumentos').rglob('*.tex'):
    text=path.read_text(encoding='utf-8')
    if not re.search(r'\b(Carlos|Naomi|Ignacio|Matías|Martín|Marcel|Alonso)\b',text):continue
    for name,role in people.items():text=re.sub(name,role,text)
    save(path,text,'Autoría corporativa en propuesta técnica; identidad original preservada en evidencia interna.')

for folder in (BASE/'subdocumentos').iterdir():
    path=folder/'declaracion-ia.tex'
    if not path.exists():continue
    text=path.read_text(encoding='utf-8')
    addition=r'\usoIA{Cierre documental del 25-11-2026}{OpenAI Codex}{Integración del corte final, normalización de autoría corporativa y comprobación documental}{Medio}{Ninguno}{Responsable corporativo del subdocumento: revisión humana de esta edición pendiente antes de emitir; las verificaciones automáticas no la sustituyen.}'
    if addition not in text:save(path,text.rstrip()+'\n'+addition+'\n','Declaración transparente de esta intervención sin atribuir revisión humana realizada.')

path=BASE/'subdocumentos/09-calidad/formularios/catalogo-T-17.tex'
text=path.read_text(encoding='utf-8')
start=text.index(r'\subsubsection*{CP-PERF-03')
end=text.find(r'\subsubsection*{',start+1)
if end<0:end=len(text)
block=text[start:end]
block=block.replace('a Azure Brazil South (RTO','al sitio secundario admisible (RTO')
block=block.replace('Sitio secundario Hot-Standby en Azure Brazil South sincronizado mediante replicación continua.',
    'Sitio secundario aprobado en S4/T-11, sincronizado mediante replicación continua. El fixture identifica región, recursos, autorizaciones y mecanismo homologado antes del ensayo. Brazil South sólo se usa con vía habilitante acreditada; en caso contrario se usa el sitio secundario admisible seleccionado conforme a R-24.')
block=block.replace('en Brazil South','en el sitio secundario aprobado').replace('de Brazil South','del sitio secundario aprobado')
block=block.replace(r'Azure Chile Central $\rightarrow$ Azure Brazil South.',r'Azure Chile Central $\rightarrow$ sitio secundario admisible identificado en el fixture y aprobado conforme a S4/T-11 y R-24.')
save(path,text[:start]+block+text[end:],'CP-PERF-03 parametrizado para ambas ramas del protocolo R-24/H7; sin dar por autorizada una región.')

path=BASE/'anexos/observaciones-informe3.tex'
text=path.read_text(encoding='utf-8').replace('Anexo 1.A (f. 7)','Anexo 1.A, sección de plan de certificación')
save(path,text,'Referencia semántica estable al Anexo 1.A; el folio exacto se fija tras compilar.')

# Compatibilidad Windows solamente en esta copia de compilación.
path=BASE/'.latexmkrc'
text=path.read_text(encoding='utf-8').replace("join(':',","join(';',").replace('referencias//:"','referencias//;"')
text+='\n$ENV{\'MIKTEX_ENABLE_INSTALLER\'} = \'0\';\n'
save(path,text,'Separador de rutas Windows en la copia aislada; instalación automática deshabilitada.')
path=BASE/'herramientas/compilar.py'
text=path.read_text(encoding='utf-8')
text=text.replace('base = os.path.relpath(os.path.join(congelados, o.nombre), RAIZ)', 'base = os.path.relpath(os.path.join(congelados, o.nombre), RAIZ).replace(os.sep, "/")')
text=text.replace('return os.path.relpath(ruta, RAIZ)','return os.path.relpath(ruta, RAIZ).replace(os.sep, "/")')
text=text.replace('os.path.relpath(ruta, RAIZ)\n','os.path.relpath(ruta, RAIZ).replace(os.sep, "/")\n')
needle='    trabajos = trabajos + formularios\n'
insert='''    # Anexos independientes integrados al mismo correlativo del sobre.
    for n in (1, 2, 5):
        trabajos.append(Trabajo(f"A{n}", "anexo.tex", f"AUDIT-Subdocumento{n}-Anexos",
            os.path.join(auxbase, f"A{n}"),
            pre + r"\\def\\NumeroSubdoc{%d}" % n,
            ["subdocumentos", "anexos"]))
'''
assert needle in text
text=text.replace(needle,needle+insert)
save(path,text,'Anexos S1/S2/S5 en correlativo global y rutas de referencias compatibles con Windows; sólo copia aislada.')

(OUT/'evidencia/cambios.json').write_text(json.dumps(changes,ensure_ascii=False,indent=2),encoding='utf-8')
print('Archivos corregidos:',len(changes))
