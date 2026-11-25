from pathlib import Path
import re
O=Path(__file__).resolve().parent;B=O/'fuentes'
p=B/'anexos/observaciones-informe3.tex';t=p.read_text(encoding='utf-8')
updates={
'GEN-05':('Se conserva la trazabilidad de las revisiones declaradas en versiones anteriores y se declara expresamente la intervención de cierre. La revisión humana de la edición final debe acreditarse por responsable y versión antes de emitir.','Declaraciones de IA de cada capítulo y A-6 del Sobre 1. Estado: Parcial; revisión humana del corte final pendiente'),
'EMP-02':('S1 identifica estructura, dedicaciones y escalamiento. La asignación formal de subrogancias gerenciales y poderes durante M1--M20 requiere ratificación documentada; no se atribuye una tabla inexistente.','S1 §§1.2--1.3. Estado: Parcial; falta acreditar la cobertura gerencial y la representación durante la dedicación contractual'),
'RIE-05':('S8 define la razón de retorno como pérdida esperada evitada sobre costo. La valoración por respuesta material requiere insumos y cálculos trazables; no se presenta como incorporado un cuadro económico no localizado.','S8 §8.3 y revisión del Sobre 3. Estado: Parcial; cálculo sustentado por respuesta material pendiente')}
lines=t.splitlines()
for i,line in enumerate(lines):
    for id,(answer,ev) in updates.items():
        if not re.match(r'\\observacion\[sub=\d+\]\{'+id+r'\}',line):continue
        start=line.index('{'+id+'}');args=[];j=start
        while j<len(line):
            if line[j]!='{':j+=1;continue
            depth=1;k=j+1
            while depth:
                if line[k]=='{' and line[k-1]!='\\':depth+=1
                elif line[k]=='}' and line[k-1]!='\\':depth-=1
                k+=1
            args.append(line[j+1:k-1]);j=k
        assert len(args)==4,(id,len(args))
        lines[i]=line[:start]+'{'+args[0]+'}{'+args[1]+'}{'+answer+'}{'+ev+'}'
p.write_text('\n'.join(lines)+'\n',encoding='utf-8')
for form in ('T-14','T-15','T-18'):
    p=B/'subdocumentos/07-plan-trabajo/formularios'/f'{form}.tex';t=p.read_text(encoding='utf-8')
    if r'\filasUsoIA' not in t:
        t=t.replace(r'\usoIA{'+form,'La declaración de la '+form+' se consolida en el Formulario A-6; la revisión de esta edición debe acreditarse antes de emitir.\n'+r'\usoIA{'+form)
        t+='\n'+r'\begin{tabla}[ancho=completo,fuente=condensada,numerada=false]{Declaración de uso de IA}{07-usoia-'+form.lower()+r'}{L{13mm} L{24mm} X L{15mm} L{17mm} L{44mm}}'+'\n'+r'Sección & Herramienta & Finalidad & Nivel en texto & Nivel en diagramas & Revisión humana \\ \midrule'+'\n'+r'\filasUsoIA'+'\n'+r'\end{tabla}'+'\n'
    p.write_text(t,encoding='utf-8')
for p in (B/'subdocumentos').rglob('*.tex'):
    t=p.read_text(encoding='utf-8');a=t
    t=t.replace('responsable de Calidad, Líder de Calidad, e responsable de Arquitectura y responsable de Arquitectura, Arquitectos de Solución','responsables corporativos de Calidad y Arquitectura de Solución')
    t=t.replace('responsable de Arquitectura, Arquitecto de Solución','responsable corporativo de Arquitectura de Solución')
    if t!=a:p.write_text(t,encoding='utf-8')
assert all('Estado: Parcial' in line for line in lines if any('{'+id+'}' in line for id in updates))
print('Corregidas 3 filas y tablas IA propias de T-14/T-15/T-18; normalización de roles revisada.')
