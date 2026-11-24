from pathlib import Path
import json,re
B=Path(__file__).resolve().parents[2]/'tmp/cierre-entrega-3/recursos/Formato-Oferta-audIT/subdocumentos/07-plan-trabajo'
D=json.loads((B/'graficos/conciliacion-3.2/puente.json').read_text(encoding='utf-8'))
R=json.loads((B/'graficos/conciliacion-3.2/red-calculada.json').read_text(encoding='utf-8'))
p=B/'formularios/T-14.tex';lines=[]
for line in p.read_text(encoding='utf-8').splitlines():
    match=re.match(r'^(\d+\.\d+) &',line)
    if match:
        pk=match[1];nodes=[n['id'] for n in R if pk in n['edt']]
        windows=D['paquetes'][pk]['ventanas']
        months=', '.join('M'+str(a)+(('--'+str(b)) if b!=a else '') for a,b in windows)
        line=line.rsplit('&',1)[0]+'& '+', '.join(nodes)+'; '+months+r' \\'
    lines.append(line)
p.write_text('\n'.join(lines)+'\n',encoding='utf-8')
p=B/'contenido.tex';s=p.read_text(encoding='utf-8')
s=s.replace('el estudio EDT2.5 antes de M6','el estudio EDT2.5 entregado durante M6')
s=s.replace('LOT-P y LOT7/8/9','A11-PIL y M7/8/9-KIT').replace('LOT-P/7/8/9','A11-PIL y M7/8/9-KIT').replace('LOT9','M9-KIT')
s=s.replace('la capacidad mensual contratada procede de la conciliación de perfiles y demanda de desarrollo.','la capacidad mensual contratada procede de la conciliación de perfiles y demanda de desarrollo.')
s=s.replace('El cierre M21--M24 de EDT6.5 y EDT7.2 tiene recursos',r'''El cierre M21--M24 de EDT6.5 y EDT7.2 reserva 1.669 horas ya incluidas en la contratación.
La conducción técnica de cierre utiliza 18, 17, 17 y 17 horas de la capacidad de Gestión de Servicio
en M21, M22, M23 y M24: ese puesto debe acreditar competencia de liderazgo de desarrollo para
asumir esta responsabilidad. La reserva deja 62 o 63 horas para su gestión ordinaria dentro de
las 80 contratadas. En H1 se asigna un titular que cumpla ambos cometidos o un sustituto de igual
capacidad y tarifa, conservando la cobertura de servicio y sin declarar una equivalencia ya acreditada.
El presupuesto identifica esa asignación como propuesta de ejecución, no como nombramiento confirmado.

El cierre tiene recursos''')
p.write_text(s,encoding='utf-8')
p=B/'formularios/T-18.tex';s=p.read_text(encoding='utf-8')
s=s.replace('familiarización diez días antes del fin de A09-8','familiarización desde G13; práctica desde día 192').replace('16 y 17 & Mayo y junio 2028 & Estabilización','17 y 18 & Junio y julio 2028 & Estabilización')
s=s.replace('Paso a producción en la segunda quincena e inicio de la operación','Operación desde el inicio de M21; aceptación final al cierre de M21')
p.write_text(s,encoding='utf-8')
p=B/'formularios/T-15.tex';s=p.read_text(encoding='utf-8').replace('LOT9','M9-KIT')
s=s.replace('de integraciones y datos M21--M24 en su celda de nómina, sin volver a sumarlos como costo adicional.','de integraciones y datos M21--M24 en su celda de nómina, sin volver a sumarlos como costo adicional. La reserva de 69 horas de conducción técnica utiliza Gestión de Servicio con competencia de liderazgo de desarrollo requerida, según la asignación y condición de S7. El resto de su jornada conserva el control de SLA y cambios.')
p.write_text(s,encoding='utf-8')
print('T-14 trazado a nodos reales; T-18 y cierre conciliados.')
