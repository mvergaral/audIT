from pathlib import Path
import json,re
O=Path(__file__).resolve().parent;B=O/'fuentes'
mapping={
'Bureau Veritas Certification S.A.':'Certificadora Simulada Horizonte TFEP S.A.',
'Bureau Veritas':'Certificadora Simulada Horizonte TFEP S.A.',
'BV-EXP-2026-CL-8921':'CSH-EXP-2026-CL-8921',
'Nexia Auditores SpA':'Auditores Simulados Faro TFEP SpA',
'Transportes del Sur Ltda.':'Transportes Simulados del Sur TFEP SpA',
'AgroFrutícola Los Andes S.A.':'Agrofrutícola Simulada Cordillera TFEP S.A.',
'Logística y Distribución Multimodal Bicentenario S.A.':'Logística Simulada Bicentenario TFEP S.A.',
'Logística Multimodal Bicentenario S.A.':'Logística Simulada Bicentenario TFEP S.A.',
'Maestranza y Laboratorio Electrónico Diesel del Norte Ltda.':'Centro Simulado TFEP Antofagasta SpA',
'Electromecánica y Telecomunicaciones del Maule SpA':'Centro Simulado TFEP Talca SpA',
'Centro Integral de Servicios Telemáticos Biobío S.A.':'Centro Simulado TFEP Los Ángeles S.A.',
'Laboratorio y Soporte Tecnológico Austral Ltda.':'Centro Simulado TFEP Puerto Montt Ltda.',
'miturra@transportesdelsur.cl':'referencia-p1@transportes-simulados-tfep.example',
'pconcha@agrofruticolalosandes.cl':'referencia-p2@agro-simulada-tfep.example',
'rbaeza@logisticabicentenario.cl':'referencia-p3@logistica-simulada-tfep.example',
'(como Certificadora Simulada Horizonte TFEP S.A. o SGS)':'(Certificadora Simulada Horizonte TFEP S.A.)'}
modified=[]
for p in B.rglob('*.tex'):
    if any(x in p.parts for x in ('salida','administrativo')) or p.name=='sobre1-antecedentes.tex':continue
    t=p.read_text(encoding='utf-8');a=t
    for old,new in mapping.items():t=t.replace(old,new)
    # Los documentos del ejercicio se verifican en el expediente, no llamando a terceros reales.
    if p.name=='T-6.tex':
        t=re.sub(r'\\, \+56~9~[0-9~]+\)',r'\\, contacto del expediente simulado)',t)
    if p.name=='contenido.tex' and p.parent.name=='01-empresa':
        anchor=r'\subsection{Alianzas'
        explanation='Los indicadores se calculan sobre bases identificadas en el resumen financiero simulado del Sobre N.º 1: ROE sobre patrimonio promedio, ROA sobre activos promedio y leverage sobre pasivo y patrimonio al cierre. Las razones de liquidez y prueba ácida usan los saldos corrientes de cierre. Esta distinción evita confundir promedios del ejercicio con saldos de fin de año.\n\n'
        target=t.find(r'\section',t.find('Retorno sobre Activos'))
        if target>=0 and explanation not in t:t=t[:target]+explanation+t[target:]
    if t!=a:
        backup=O/'evidencia/antes-emisores'/p.relative_to(B);backup.parent.mkdir(parents=True,exist_ok=True);backup.write_text(a,encoding='utf-8')
        p.write_text(t,encoding='utf-8');modified.append(str(p.relative_to(B)))
(O/'evidencia/emisores-ficticios.json').write_text(json.dumps({'instruccion':'Usuario confirma Art93 y validación docente de piezas simuladas; emisores ficticios inconfundibles.','mapa':mapping,'archivos':modified},ensure_ascii=False,indent=2),encoding='utf-8')
print('Normalizados',len(modified),'archivos')
