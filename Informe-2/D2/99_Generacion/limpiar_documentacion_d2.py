"""Correcciones editoriales de S3/T-12 y S7, con trazabilidad por sección."""
from pathlib import Path
import re
import json

ROOT=Path(__file__).resolve().parents[3]
BASE=ROOT/'recursos/Formato-Oferta-audIT'
S3=BASE/'subdocumentos/03-solucion'

labels={}
sec=sub=0
for m in re.finditer(r'\\(section|subsection)\{[^\n]+?\}\\label\{([^}]+)\}',(S3/'contenido.tex').read_text(encoding='utf-8')):
    if m.group(1)=='section':
        sec+=1; sub=0
        number=f'3.{sec}'
    else:
        sub+=1; number=f'3.{sec}.{sub}'
    labels[m.group(2)]=number

rf=['evidencia','evidencia','evidencia','evidencia','etapa1','viaje','etapa1',
    'contextos','viaje','viaje','viaje','viaje','viaje','viaje','etapa2',
    'etapa1','etapa1','etapa2','viaje','adhesion','etapa2','adhesion',
    'etapa2','etapa2','contextos','adhesion','etapa1','evidencia']
rnf=['restricciones','atributos','exclusiones','implantacion','restricciones',
     'viaje','restricciones','atributos','operacion','restricciones',
     'implantacion','evidencia','atributos','operacion']
mapping={f'{prefix}-{i:03}':{'etiqueta':f'sec:3-{name}','seccion':labels[f'sec:3-{name}']}
         for prefix,names in [('RF',rf),('RNF',rnf)] for i,name in enumerate(names,1)}
assert len(mapping)==42
(S3/'formularios/trazabilidad-secciones.json').write_text(json.dumps(mapping,ensure_ascii=False,indent=2),encoding='utf-8')
registry=['% Secciones de S3 donde se atiende cada requerimiento del T-12.']
registry += [f"\\reqUsado{{{ident}}}{{{v['seccion']}}}{{}}" for ident,v in mapping.items()]
(S3/'formularios/trazabilidad-secciones.tex').write_text('\n'.join(registry)+'\n',encoding='utf-8')

p=S3/'formularios/T-12.tex'
text=p.read_text(encoding='utf-8')
text=text.replace('Comprobación integral de los 90 segundos pendiente, incluida solicitud, emisión, retorno, reensamblado y verificación (S4 y S8, R-28)',
                  'Comprobación integral del límite de 90 segundos en CP-HW-11 y CP-PERF-05 durante A12, incluida solicitud, emisión, retorno, reensamblado y verificación (S4 y S8, R-28)')
text=text.replace('ensayo integral de 90 segundos pendiente','ensayo integral del límite de 90 segundos en CP-HW-11 y CP-PERF-05 durante A12')
text=text.replace('CP-UNIT-21 y CP-HW-11','CP-UNIT-21, CP-HW-11 y CP-PERF-05')
line=r'\input{subdocumentos/03-solucion/formularios/trazabilidad-secciones.tex}'
if line not in text:
    text=text.replace(r'\begin{formulario}{T-12}',line+'\n'+r'\begin{formulario}{T-12}',1)
for ident,record in mapping.items():
    pattern=r'(id\s*=\s*'+re.escape(ident)+r',\n)(?:\s*seccion\s*=\s*\{[^\n]*\},\n)?'
    text,n=re.subn(pattern,lambda m:m.group(1)+f"  seccion      = {{Sección {record['seccion']}}},\n",text)
    assert n==1,(ident,n)
p.write_text(text,encoding='utf-8')

md=S3/'formularios/T-12.md'
text=md.read_text(encoding='utf-8')
text=text.replace('Comprobación integral de los 90 segundos pendiente, incluida solicitud, emisión, retorno, reensamblado y verificación (S4 y S8, R-28)',
                  'Comprobación integral del límite de 90 segundos en CP-HW-11 y CP-PERF-05 durante A12, incluida solicitud, emisión, retorno, reensamblado y verificación (S4 y S8, R-28)')
text=text.replace('ensayo integral de 90 segundos pendiente','ensayo integral del límite de 90 segundos en CP-HW-11 y CP-PERF-05 durante A12')
text=text.replace('CP-UNIT-21 y CP-HW-11','CP-UNIT-21, CP-HW-11 y CP-PERF-05')
for ident,record in mapping.items():
    pattern=r'(### '+re.escape(ident)+r'\n.*?\| Sección \| )[^\n]*(?=\n)'
    text,n=re.subn(pattern,lambda m:m.group(1)+f"Sección {record['seccion']} |",text,flags=re.S)
    assert n==1,(ident,n)
md.write_text(text,encoding='utf-8')

# Sólo las respuestas que el aviso asigna a S3; las otras filas se conservan.
p=BASE/'anexos/observaciones-informe1.tex'
text=p.read_text(encoding='utf-8')
changes={
 '01':('El Formulario T-12 se entrega en archivo propio con 42 requerimientos: 28 funcionales y 14 no funcionales. Cada ficha identifica origen, componente, paquete EDT, sección de S3 y casos de verificación del T-17.',
       'S3 3.2.8; T-12; T-17, matriz de requisitos y casos de prueba.'),
 '12':('S3 y T-12 presentan la solución con la voz corporativa de audIT, sin nombres de integrantes ni referencias a equipos internos en el contenido técnico. La declaración de uso de IA se incluye en su apartado específico.',
       'Subdocumento 3 y Formulario T-12.'),
 '40':('Las referencias apuntan a la sección exacta del Subdocumento 4 que describe cada componente de la solución.',
       'S3 3.3 y 3.4.7; Subdocumento 4.'),
 '48':('T-12 vincula los 42 requerimientos con su origen, componente, paquete EDT y casos de prueba. T-17 contiene la matriz de cobertura, los casos de verificación y los criterios de aceptación correspondientes.',
       'S3 3.2.8; T-12; T-17, matriz de requisitos y variantes por caso.'),
}
lines=[]
for line in text.splitlines():
    m=re.match(r'(\\observacion\[[^\]]*sub=3[^\]]*\]\{(\d+)\}\{[^}]*\})\{',line)
    if m and m.group(2) in changes:
        response,section=changes[m.group(2)]
        line=m.group(1)+'{'+response+'}{'+section+'}'
    lines.append(line)
p.write_text('\n'.join(lines)+'\n',encoding='utf-8')

for folder in ['03-solucion','07-plan-trabajo']:
    p=BASE/f'subdocumentos/{folder}/declaracion-ia.tex'
    text=p.read_text(encoding='utf-8')
    text=text.replace('desde las decisiones D4-61 a D4-67','desde las decisiones de diseño del equipo')
    text=text.replace('; ensayo integral de 90 segundos pendiente','; definición del ensayo integral de 90 segundos')
    text=text.replace('Conciliación y controles documentales automatizados realizados; revisión humana final pendiente.',
                      r'\marcador{Nombre, cargo y alcance de la revisión humana}')
    text=re.sub(r'\\marcador\{(?:nombre y cargo de quien revisó, y qué verificó|Revisión humana[^{}]*)\}',
                lambda _:r'\marcador{Nombre, cargo y alcance de la revisión humana}',text)
    text=text.replace(r'\usoIA{Conciliación de capacitación y adhesión}',
                      r'\usoIA{3.4.3 y RF-026 del T-12}' if folder=='03-solucion' else r'\usoIA{7.3.1, T-15 y T-18}')
    text=text.replace('sin modificar precedencias','conservando el alcance de los paquetes')
    p.write_text(text,encoding='utf-8')
print('42 referencias de sección y cuatro respuestas de Art. 46 corregidas; declaraciones editoriales depuradas.')
