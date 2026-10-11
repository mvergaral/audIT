"""CPM con desfase fin-inicio y puerta de disponibilidad; oráculo de pruebas de firma."""
from pathlib import Path
import re
import csv
import json

ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT/'recursos/Formato-Oferta-audIT/subdocumentos'
T15 = BASE/'07-plan-trabajo/formularios/T-15.tex'

def leer_red():
    nodes={}
    for line in T15.read_text(encoding='utf-8').splitlines():
        if not re.match(r'^A\d\d &',line):
            continue
        fields=[x.strip().removesuffix('\\\\').strip() for x in line.split('&')]
        if len(fields)!=11:
            continue
        ident=fields[0]
        preds={p:0 for p in re.findall(r'A\d\d',fields[2])}
        nodes[ident]={'duracion':float(fields[3]),'preds':preds,'actividad':fields[1]}
    nodes['G13']={'duracion':0,'preds':{'A09':-10},'actividad':'Versión de entrenamiento y material por perfil probados y congelados en PREPROD'}
    nodes['A13']['preds']={'A06':0,'A09':-10,'G13':0}
    return nodes

def calcular_red(nodes, disponibilidad=None):
    result={}
    pending=dict(nodes)
    while pending:
        ready=[ident for ident,node in pending.items() if all(p in result for p in node['preds'])]
        if not ready:
            raise ValueError('Dependencia inexistente o ciclo')
        for ident in ready:
            node=pending.pop(ident)
            es=max([0]+[result[p]['EF']+lag for p,lag in node['preds'].items()])
            if ident=='G13' and disponibilidad is not None:
                es=max(es,disponibilidad)
            result[ident]={**node,'ES':es,'EF':es+node['duracion']}
    finish=max(n['EF'] for n in result.values())
    for ident in reversed(result):
        node=result[ident]
        successors=[(other,v['preds'][ident]) for other,v in result.items() if ident in v['preds']]
        lf=min([result[s]['LS']-lag for s,lag in successors],default=finish)
        node.update(LF=lf,LS=lf-node['duracion'])
        node['HT']=node['LS']-node['ES']
        node['HL']=min([result[s]['ES']-lag-node['EF'] for s,lag in successors],default=finish-node['EF'])
    return result

def contar_firmados(records,corte='2027-10-31'):
    """Datos ficticios de prueba; las condiciones se evalúan al corte, no al día actual."""
    return len({r['rut'] for r in records
                if r.get('poblacion_inicial') and r.get('modalidad') in ('completa','datos')
                and all(r.get(k) for k in ('firma_mandante','firma_representante','representante_autorizado','vigente'))
                and not r.get('revocado',False)
                and r.get('firma','9999')<=corte and r.get('registrado','9999')<=corte})

def actualizar():
    red=calcular_red(leer_red())
    text=T15.read_text(encoding='utf-8')
    lines=[]
    for line in text.splitlines():
        if re.match(r'^G13 &',line):
            continue
        if re.match(r'^A\d\d &',line) and len(line.split('&'))==11:
            fields=[x.strip().removesuffix('\\\\').strip() for x in line.split('&')]
            ident=fields[0]; node=red[ident]
            if ident=='A09':
                fields[1]='Construcción de Etapa 1 en ocho sprints; entrega G13 al cierre del sprint 7 y entrega completa para pruebas (H4)'
            if ident=='A13':
                gate=red['G13']
                lines.append('G13 & Entrega probada y congelada de PREPROD y material por perfil para capacitación & A09 FS$-10$ & 0 & '+' & '.join(str(int(gate[k])) for k in ('ES','EF','LS','LF','HT','HL'))+' & No \\\\')
                fields[1]='Capacitación por turnos: 10 días de familiarización y 30 de práctica y evaluación'
                fields[2]='A06, A09 FS$-10$, G13'
            fields[4:10]=[str(int(node[k])) for k in ('ES','EF','LS','LF','HT','HL')]
            fields[10]='Sí' if node['HT']==0 else 'No'
            line=' & '.join(fields)+' \\\\'
        lines.append(line)
    T15.write_text('\n'.join(lines)+'\n',encoding='utf-8')
    out=ROOT/'Informe-2/d2/03_Apoyo'
    result={ident:{k:v for k,v in node.items() if k!='preds'}|{'precedencias':node['preds']} for ident,node in red.items()}
    (out/'CPM_acuerdo_capacitacion.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
    # Pruebas de D1: conservar casos existentes y ampliar la definición y sus bordes.
    definition=(' Denominador fijo: población inicial de 148 transportistas. Corte de M9: 31 de octubre de 2027 bajo SA-01. '
                'Contar una vez por RUT, con anexo firmado por el mandante y el representante autorizado, vigente, no revocado y registrado al corte, '
                'en modalidad completa o de datos. Instalación, activación técnica y consentimientos de conductores se controlan por separado; '
                'la firma del transportista no los sustituye. Probar duplicados por RUT y ambas modalidades, anexo vencido o revocado, '
                'firma incompleta, representante sin autorización, registro posterior al corte y transportista ajeno a la población inicial. '
                'Un anexo válido cuenta aunque la instalación o activación esté pendiente; esto no habilita operaciones sin los consentimientos exigibles.')
    for path in [BASE/'09-calidad/formularios/catalogo-T-17.tex',BASE/'09-calidad/formularios/T-17.md',
                 ROOT/'Informe-2/d1/subdocs/formulario_t17_protocolo_aceptacion_plan_pruebas.md']:
        s=path.read_text(encoding='utf-8')
        phrase='59 de 148 no llega; 60 supera el umbral.'
        if definition not in s:
            s=s.replace(phrase,phrase+definition)
            path.write_text(s,encoding='utf-8')
    # Actualizar los números del PERT conservando geometría y dependencias ajenas.
    from xml.etree import ElementTree as ET
    for n in (1,2):
        p=ROOT/f'recursos/Formato-Oferta-audIT/figuras/07-plan-trabajo/pert-etapa{n}.svg'
        tree=ET.parse(p); root=tree.getroot(); nodes=list(root)
        current=None
        for elem in nodes:
            if not elem.tag.endswith('text'):
                continue
            value=elem.text or ''
            if re.fullmatch(r'A\d\d(?: \(H\d+\))?',value):
                current=value[:3]
            if current=='A13':
                elem.text=value.replace('ES 192','ES 182').replace('HT 28, HL 8','HT 38, HL 18')
            elif current=='A06':
                elem.text=value.replace('HT 62, HL 34','HT 62, HL 24')
            if value.startswith('A06, A11, A13 y A14 siguen'):
                elem.text='A09 a A13: FS -10; G13 exige PREPROD y material listos. A06, A11, A13 y A14 siguen en Etapa 2.'
        ET.register_namespace('', 'http://www.w3.org/2000/svg')
        tree.write(p,encoding='utf-8',xml_declaration=True)
    print('A13:',red['A13'],'A06 HL:',red['A06']['HL'],'Término:',red['A25']['EF'])

if __name__=='__main__':
    actualizar()
