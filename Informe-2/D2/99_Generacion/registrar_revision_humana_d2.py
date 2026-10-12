"""Formaliza revisiones declaradas por el responsable, con reparto por registros."""
from pathlib import Path
import re
import json
ROOT=Path(__file__).resolve().parents[3]
BASE=ROOT/'recursos/Formato-Oferta-audIT/subdocumentos'

people={
    'I':'Ignacio Cuevas, Analista de Requerimientos',
    'M':'Matías Vergara, Analista de Planificación y Calidad',
}
reviews={
 '03-solucion':[
    ('M','revisión de las respuestas del Artículo 46 y sus referencias a la solución y los formularios'),
    ('I','revisión del resumen, comprensión del alcance y correspondencia de los meses contractuales'),
    ('I','revisión del reparto por etapas, exclusiones, supuestos, restricciones, catálogo y criterios de aceptación'),
    ('I','revisión del esquema de solución, contextos, evidencia de jornada y atributos de calidad'),
    ('I','revisión del funcionamiento del viaje, adhesión, implementación, implantación y operación'),
    ('M','revisión de los 42 requerimientos, campos, referencias de sección, trazabilidad y casos de prueba del T-12'),
    ('M','revisión de la representación completa y conforme en cabina y del ensayo programado de 90 segundos en A12'),
    ('M','revisión del denominador de adhesión, umbral, corte, firmas, modalidades y separación de estados técnicos y consentimientos'),
 ],
 '07-plan-trabajo':[
    ('I','revisión del propósito del plan y su correspondencia con las fases y obligaciones de la oferta'),
    ('I','revisión de la dotación, asignación por rol y cobertura durante los solapamientos'),
    ('I','revisión de la secuencia PERT/CPM, precedencias, ruta crítica y reservas'),
    ('I','revisión de la dotación, esfuerzo, estimaciones de tres puntos y malla del T-15'),
    ('M','revisión de cobertura de la EDT, partición del trabajo, cronograma, implantación y correspondencia de las figuras con el plan'),
    ('M','revisión del diccionario de los 54 paquetes, secuencias de implantación, reversión y esfuerzo de T-14, T-15 y T-18'),
    ('M','revisión de las vistas generales y detalles de EDT/Gantt, sus códigos, leyendas y referencias PERT'),
    ('M','revisión del adelanto condicionado de A13, entrega G13, holguras, duración y complemento del sprint 8 dentro de los 40 días'),
 ],
}
counts={'I':0,'M':0}
record=[]
for folder,entries in reviews.items():
    p=BASE/folder/'declaracion-ia.tex'
    lines=p.read_text(encoding='utf-8').splitlines()
    indexes=[i for i,line in enumerate(lines) if line.startswith(r'\usoIA{')]
    assert len(indexes)==len(entries),(folder,len(indexes))
    for i,(person,scope) in zip(indexes,entries):
        line=lines[i]
        section=re.match(r'\\usoIA\{([^}]+)\}',line).group(1)
        value=people[person]+': '+scope+'.'
        line,n=re.subn(r'\{\\marcador\{Nombre, cargo y alcance de la revisión humana\}\}$',
                       lambda _:'{'+value+'}',line)
        if n==0:
            assert line.endswith('{'+value+'}'),(folder,section)
        lines[i]=line
        counts[person]+=1
        record.append({'subdocumento':folder,'seccion':section,'revisor':people[person],'alcance':scope})
    p.write_text('\n'.join(lines)+'\n',encoding='utf-8')
assert counts=={'I':8,'M':8},counts
(ROOT/'Informe-2/D2/03_Apoyo/Revision_humana_declarada.json').write_text(
    json.dumps({'fecha_declaracion':'2026-10-12','origen':'Revisión humana declarada por el responsable en la conversación; reparto por registros autorizado',
                'bitacoras_vinculadas':{
                    'Ignacio Cuevas':'Investigacion/Persona-1/Bitacora_A6_Persona_1_Declaracion_Oficial.md',
                    'Matías Vergara':'Investigacion/Persona-8/Bitacora_A6_Persona_8_Declaracion_Oficial.md'},
                'reparto':counts,'registros':record},ensure_ascii=False,indent=2),encoding='utf-8')
print('Declaraciones completadas: ocho registros por revisor, dieciséis en total.')
