from pathlib import Path
import re,json,hashlib
O=Path(__file__).resolve().parent; B=O/'fuentes'; changes=[]
def edit(rel,func,reason):
    p=B/rel;a=p.read_text(encoding='utf-8');z=func(a)
    if a==z:return
    bak=O/'evidencia/antes-conciliacion'/rel;bak.parent.mkdir(parents=True,exist_ok=True);bak.write_text(a,encoding='utf-8')
    p.write_text(z,encoding='utf-8');changes.append({'archivo':rel,'motivo':reason,'antes':hashlib.sha256(a.encode()).hexdigest(),'despues':hashlib.sha256(z.encode()).hexdigest()})

def observations(t):
    t=t.replace('Consolida el 100 % de las observaciones de la Revisión Final del Informe 2','Consolida las 74 filas inventariadas de observaciones del Informe 2')
    t=t.replace('(60 observaciones de Revisión 1 + 6 observaciones complementarias de','(68 observaciones sin etiqueta complementaria + 6 observaciones complementarias de')
    t=t.replace('Revisión 2 = 66 observaciones)','Revisión 2 = 74 observaciones)')
    t=t.replace('Son 35 riesgos: 17 de terceros, 12 de audIT y 6 del mandante.','Son 36 riesgos: 17 de terceros, 13 de audIT y 6 del mandante.')
    t=t.replace('H4, H7, H11 y H12 quedan sin margen.','H4, H7 y H12 quedan sin margen; H11 tiene fecha fija protegida por A23.')
    t=t.replace('conciliación diaria, reversión probada y acta del mandante.','conciliación diaria, ensayo de reversión exigido antes del paso y acta futura del mandante.')
    rows={
    'GEN-05':('Se conserva la trazabilidad de las revisiones declaradas en versiones anteriores y se declara expresamente la intervención de cierre. La revisión humana de la edición final debe acreditarse por responsable y versión antes de emitir.','Declaraciones de IA de cada capítulo y A-6 del Sobre 1. Estado: Parcial; revisión humana del corte final pendiente'),
    'EMP-02':('S1 identifica estructura, dedicaciones y escalamiento. La asignación formal de subrogancias gerenciales y poderes durante M1--M20 requiere ratificación documentada; no se atribuye una tabla inexistente.','S1 §§1.2--1.3. Estado: Parcial; falta acreditar la cobertura gerencial y la representación durante la dedicación contractual'),
    'RIE-05':('S8 define la razón de retorno como pérdida esperada evitada sobre costo. La valoración por respuesta material requiere insumos y cálculos trazables; no se presenta como incorporado un cuadro económico no localizado.','S8 §8.3 y revisión del Sobre 3. Estado: Parcial; cálculo sustentado por respuesta material pendiente')}
    for id,(answer,ev) in rows.items():
        lines=t.splitlines()
        for n,line in enumerate(lines):
            if r'}{'+id+'}' in line:
                # Separar los cinco argumentos de observacion respetando grupos.
                start=line.index('{'+id+'}')
                args=[];i=start
                while i<len(line):
                    if line[i]!='{':i+=1;continue
                    depth=1;j=i+1
                    while depth and j<len(line):
                        if line[j]=='{' and line[j-1]!='\\':depth+=1
                        elif line[j]=='}' and line[j-1]!='\\':depth-=1
                        j+=1
                    args.append(line[i+1:j-1]);i=j
                assert len(args)==4,(id,len(args))
                lines[n]=line[:start]+'{'+args[0]+'}{'+args[1]+'}{'+answer+'}{'+ev+'}'
        t='\n'.join(lines)+'\n'
    return t
edit('anexos/observaciones-informe3.tex',observations,'Conteo y estados respaldados; no atribuir cierres humanos, cuadros o subrogancias no acreditados.')

def risk(t):
    t=t.replace('firmar el contrato con febrero de 2027 como mes 1 (R-21)','validar la fecha efectiva de inicio y las ventanas estacionales bajo SA-01 (R-21)')
    t=t.replace('el contrato fija febrero de 2027 como mes 1 (R-21)','la fecha efectiva y las ventanas se validan bajo SA-01 antes de fijar la línea base (R-21)')
    return t
edit('subdocumentos/08-riesgos/contenido.tex',risk,'Separar escenario civil SA-01 de fecha contractual efectiva.')
def t16(t):
    t=t.replace('El contrato empieza en enero de 2027 y el mes 16 cae en abril, dentro de la temporada','La fecha efectiva de inicio desplaza la equivalencia civil de M16 y sus ventanas estacionales respecto del escenario SA-01')
    t=t.replace('Fijar en el contrato febrero de 2027 como mes 1 y escalar al Comité Ejecutivo cualquier cambio de fecha','Validar la fecha efectiva, capacidad y ventanas bajo SA-01 antes de fijar la línea base; febrero de 2027 es un escenario civil, no una fecha contractual acreditada; escalar al Comité Ejecutivo cambios incompatibles con las ventanas')
    t=t.replace('Fecha de inicio del contrato distinta de febrero de 2027','Fecha efectiva incompatible con las ventanas estacionales bajo SA-01')
    t=t.replace('Después de mitigar, ningún riesgo queda con exposición alta.','Las exposiciones residuales son objetivos condicionados a ejecutar y verificar las respuestas. R-17 conserva exposición alta hasta acreditar la revisión de capacidad, ventanas y tres puntos antes de H1; el objetivo 12 a 6 no acredita una reducción ya conseguida. En el objetivo de mitigación, ningún riesgo queda con exposición alta.')
    return t
edit('subdocumentos/08-riesgos/formularios/T-16.tex',t16,'R-21 conciliado con SA-01 y exposición residual diferenciada de reducción efectivamente acreditada.')
edit('subdocumentos/04-arquitectura/contenido.tex',lambda t:t.replace('contrato de respaldo con el proveedor de combustible.','contrato de respaldo previsto con el proveedor de combustible, cuya disponibilidad y condiciones deben acreditarse antes de la puesta en servicio.'),'No presentar como suscrito el contrato de combustible sin respaldo localizado.')
edit('subdocumentos/01-empresa/contenido.tex',lambda t:re.sub(r'Sobre N\.º 1, Carpeta Idoneidad Económica, Fols\. \d+--\d+',r'Sobre N.º 1, antecedentes financieros declarados; respaldo y folios por acreditar',t),'Retirar folios de antecedentes financieros inexistentes en el expediente localizado.')
def cp25(t):
    s=t.index(r'\subsubsection*{CP-INT-25');e=t.find(r'\subsection*{',s+1)
    if e<0:e=len(t)
    b=t[s:e].replace('Réplica Brazil South','réplica del sitio secundario admisible').replace('en Brazil South','en el sitio secundario aprobado conforme a R-24')
    return t[:s]+b+t[e:]
edit('subdocumentos/09-calidad/formularios/catalogo-T-17.tex',cp25,'CP-INT-25 coherente con ambas ramas del sitio secundario de CP-PERF-03/R-24.')
for form in ('T-14','T-15','T-18'):
    def own(t,form=form):
        if r'\usoIA{'+form in t:return t
        return t.rstrip()+'\n\n'+r'\section*{Declaración de uso de IA del Formulario '+form+'}\n'+r'\usoIA{'+form+r'}{OpenAI Codex}{Conciliación de planificación, presupuesto y trazabilidad; generación e integración documental}{Alto}{Alto}{D2, responsable de Planificación y Calidad: revisión humana del corte final pendiente antes de emitir.}'+'\n'
    edit('subdocumentos/07-plan-trabajo/formularios/'+form+'.tex',own,'Declaración propia del formulario; revisión humana pendiente explícita.')
source=(B/'subdocumentos/02-problema/contenido.tex').read_text(encoding='utf-8')
s=source.index(r'\paragraph{SUP-01.');e=source.index(r'\paragraph{Condicionantes',s)
supp=source[s:e]
edit('subdocumentos/02-problema/anexos.tex',lambda t:t+'\n'+r'\section*{Anexo 2.F. Supuestos críticos y comprobación}'+'\n'+r'\label{sec:02-anexo-supuestos}\addcontentsline{toc}{section}{Anexo 2.F. Supuestos críticos y comprobación}'+'\nEl listado reproduce los supuestos SUP-01 a SUP-06 de la sección 2.5.2 del documento principal, con sus condiciones de aceptación y el efecto de su incumplimiento. Su presencia no acredita que las comprobaciones futuras ya se hayan realizado.\n\n'+supp,'Incorporar al anexo independiente los seis supuestos críticos ya descritos en el cuerpo, sin inventar supuestos nuevos.')
(O/'evidencia/conciliacion-cambios.json').write_text(json.dumps(changes,ensure_ascii=False,indent=2),encoding='utf-8')
print('Conciliados',len(changes),'archivos')
