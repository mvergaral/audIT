"""Genera el puente de horas por tarea y rol sin alterar la planilla entregada.

La demanda identificada de D3/innovaciones se reserva primero. El saldo de
capacidad se asigna al trabajo de revisión, coordinación, pruebas y atención
del paquete activo: es presupuesto de control, no productividad medida.
"""
from pathlib import Path
import csv, hashlib, json, re
import openpyxl

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[4]
PLANILLA=ROOT/'outputs/3.2/Entrega-3.2/INFORME3_AUDIT_PLANILLA_3.2_20261115.xlsx'
OUT=HERE/'conciliacion-3.2'
ALIAS={'arquitectura':'Arquitectura','lider':'Liderazgo desarrollo','software':'Software','frontend':'Frontend','seguridad':'Seguridad','datos':'Datos','qa':'QA','sre':'SRE'}
ROLES={
 'Jefe de proyecto':['1.1','1.2'], 'Arquitectura':['2.4','5.1','5.3','5.6','8.2','12.1'],
 'Seguridad':['3.2','10.2','9.1'], 'Líder QA':['10.1','10.2','10.3'],
 'Líder Datos':['2.5','7.1','7.2','7.3'], 'SRE':['3.1','3.3','3.4','11.2','11.3','11.4'],
 'PMO':['1.1','1.2','2.1','9.1','9.2','9.3'],
 'Liderazgo desarrollo':['5.1','5.2','5.3','5.4','5.5','5.6','5.7','8.1','8.2','8.3','8.4','8.5'],
 'Software':['5.1','5.2','5.3','5.4','5.5','5.6','6.1','6.2','6.3','6.4','6.5','8.2','8.3','8.4'],
 'Frontend':['5.7','8.1','8.4'], 'Datos':['2.5','7.1','7.2','7.3','8.5'],
 'QA':['10.1','10.2','10.3'], 'Firmware':['4.1','12.2','12.3'],
 'Electrónica':['4.1','4.2','12.3'], 'Técnico de campo':['2.2','4.2','11.2','11.3'],
 'Funcional':['2.1','2.4','9.1','9.2','9.3','12.4'],
 'Integración':['2.3','4.3','6.1','6.2','6.3','6.4','6.5'],
 'Implantación y cambio':['1.3','11.1','11.2','11.3','11.4','9.2'],
 'Analista terreno':['4.2','11.1','11.2','11.3','11.4']}

def construir(path):
    wb=openpyxl.load_workbook(path,data_only=True)
    plan=json.loads((ROOT/'Informe-2/d2/99_Generacion/plan_detallado.json').read_text(encoding='utf-8'))
    ajustes=json.loads((HERE/'ajustes-paquetes.json').read_text(encoding='utf-8'))
    paquetes={p['codigo']:dict(p,**ajustes.get(p['codigo'],{})) for p in plan['paquetes']}
    # Ventanas coherentes con preparación, desarrollo, cierre y presupuesto 3.2.
    ventanas={'2.4':[[1,4]],'3.2':[[1,12]],'4.1':[[3,9]],'4.2':[[5,9]],'4.3':[[6,10],[13,15]],
      '6.5':[[6,10],[16,24]],'7.2':[[6,12],[19,24]],'10.1':[[1,20]],'10.2':[[1,20]],'10.3':[[3,20]],
      '11.2':[[13,16]],'11.3':[[19,24]],'11.4':[[13,17],[21,24]]}
    for key,v in ventanas.items():paquetes[key]['ventanas']=v
    cap=[];alloc=[]
    red=calcular_red(json.loads((HERE/'red-3.2.json').read_text(encoding='utf-8'))['nodos'])
    with (ROOT/'Informe-3/d3/datos/dedicacion_mensual_d3.csv').open(encoding='utf-8') as source:
        d3=list(csv.DictReader(source))
    for pk,p in paquetes.items():
        months=sorted({m for n in red if pk in n['edt'] and n['duracion']>0 for m in range(1,57) if n['ES']<m*20 and n['EF']>(m-1)*20})
        windows=[]
        for m in months:
            if windows and windows[-1][1]+1==m:windows[-1][1]=m
            else:windows.append([m,m])
        if windows:p['ventanas']=windows
    def activo(pk,m):
        return any(pk in n['edt'] and n['duracion']>0 and n['ES']<20*m and n['EF']>20*(m-1) for n in red)
    def add(m,role,pk,h,task,clp=0,src=''):
        if h>1e-9:alloc.append(dict(mes=m,perfil=role,paquete=pk,horas=h,tarea=task,tarifa=clp,fuente=src))
    attrs={}
    for row in wb['Atribución innovaciones'].iter_rows(min_row=2,values_only=True):
        if isinstance(row[2],int) and row[2]<=20 and row[4]:
            key=(row[2],ALIAS.get(row[3],row[3]))
            pk=re.search(r'\d+\.\d+',str(row[1])).group(0)
            attrs.setdefault(key,[]).append((pk,float(row[4]),row[0]))
    for idx,row in enumerate(wb['Dotación por perfil'].iter_rows(min_row=2,values_only=True),2):
        if not isinstance(row[0],int):continue
        m,role=row[:2];hours=float(row[8] or 0); rate=row[9]
        cap.append(dict(mes=m,perfil=role,horas=hours,celda=f'Dotación por perfil!I{idx}'))
        remaining=hours
        for pk,h,inn in attrs.get((m,role),[]):
            if h>remaining+1e-6:raise ValueError(f'Atribución excede capacidad {m} {role}')
            add(m,role,pk,h,'Construcción y validación '+inn,rate,f'Atribución innovaciones; Dotación I{idx}')
            remaining-=h
        for record in d3:
            if int(record['mes'])!=m or ALIAS.get(record['perfil'])!=role or record['bloque'] not in ['A09','edt6_7_8_reparto_d2','agente_cp_sec_05']:continue
            h=float(record['horas_solicitadas'])
            if h>remaining+1e-5:raise ValueError(f'Demanda D3 excede capacidad restante {m} {role}')
            if record['bloque']=='A09':eligible=[p for p in paquetes if p.startswith('5.') and activo(p,m)]
            elif record['bloque']=='agente_cp_sec_05':eligible=['4.1']
            else:eligible=[p for p in paquetes if p.split('.')[0] in ['6','7','8'] and activo(p,m)]
            if not eligible:eligible=['2.4']
            for pk in eligible:add(m,role,pk,h/len(eligible),'Demanda D3 '+record['bloque']+'; ejecución y prueba de '+paquetes[pk]['nombre'],rate,'D3 dedicacion_mensual_d3.csv; '+str(m)+'/'+record['perfil'])
            remaining-=h
        if role in ['SRE','Software'] and m in [13,16,19]:
            h=160 if role=='SRE' else 80
            add(m,role,'11.2' if m<19 else '11.3',h,'Guardia de puesta en producción H'+{13:'6',16:'7',19:'11'}[m],rate,f'Parámetros corrección B85:B86; Dotación G{idx}')
            remaining-=h
        # El trabajo físico medible se separa del saldo de atención/revisión.
        if role=='Técnico de campo':
            banco=sum(r[5] or 0 for r in wb['Instalación por lote'].iter_rows(min_row=2,values_only=True) if r[0]==m)
            add(m,role,'4.2',banco,'Banco y configuración de kits',rate,'Instalación por lote F')
            remaining-=banco
            if m==6:
                directo=min(10*140/60,remaining)
                add(m,role,'4.2',directo,'Piloto a bordo',rate,f'Parámetros corrección B6/B38; I{idx}')
                remaining-=directo
            elif m in (7,8,9):
                directo=min(70*15/60,remaining)
                add(m,role,'12.3',directo,'Montaje de balizas base',rate,f'Parámetros corrección B52:B54; I{idx}')
                remaining-=directo
        if role=='Analista terreno' and m in [6,7,8,9]:
            h=sum(r[6] or 0 for r in wb['Instalación por lote'].iter_rows(min_row=2,values_only=True) if r[0]==m)
            add(m,role,'4.2',h,'Integración prueba y recepción de cada kit',rate,'Instalación por lote G');remaining-=h
        if role=='Electrónica' and m in [5,6]:
            add(m,role,'12.3',5,'Instalación y prueba de lectores de portería',rate,'Parámetros corrección B55:B56; dos tandas de trabajo');remaining-=5
        if remaining < -1e-5:raise ValueError(f'Reservas exceden contratación {m}/{role}: {remaining}')
        candidates=[p for p in ROLES[role] if activo(p,m)]
        if not candidates:candidates=['1.1']
        # Asignación presupuestaria explícita por entregable activo; no es
        # una estimación de velocidad ni habilita reducir la contratación.
        share=remaining/len(candidates)
        for pk in candidates:
            add(m,role,pk,share,'Reserva de capacidad para revisión atención y coordinación de '+paquetes[pk]['nombre'],rate,f'Dotación por perfil!I{idx}; saldo disponible de control, no ejecución acreditada')
    for idx,row in enumerate(wb['Soporte por perfil'].iter_rows(min_row=2,values_only=True),2):
        if not isinstance(row[0],int):continue
        m,role=row[:2];hours=float(row[6] or 0)
        pk=re.search(r'EDT(\d+\.\d+)',role).group(1)
        cap.append(dict(mes=m,perfil=role,horas=hours,celda=f'Soporte por perfil!G{idx}'))
        remaining=hours
        alias={'SRE':'sre','Seguridad':'seguridad','Gestión servicio':'lider','Software':'software','Datos':'datos','QA':'qa','Arquitectura cierre':'arquitectura','Frontend cierre':'frontend'}
        short=role.split(' /')[0]
        if m in range(21,25) and short in alias:
            for rec in d3:
                if int(rec['mes'])==m and rec['perfil']==alias[short] and rec['bloque']=='cierre_ya_incluido_edt6_7':
                    h=float(rec['horas_solicitadas'])
                    add(m,role,rec['edt_alcance'],h,'Cierre D3 de '+rec['edt_alcance']+' presupuestado en '+rec['paquete_ejecucion']+(' (conducción técnica del gestor de servicio)' if short=='Gestión servicio' else ''),row[7],'D3 cierre_ya_incluido_edt6_7; incluido en '+f'G{idx}')
                    remaining-=h
        if m==21 and short in ['SRE','Software']:
            h=160 if short=='SRE' else 80
            add(m,role,'11.3',h,'Guardia de puesta en producción H12',row[7],f'Soporte por perfil!F{idx}')
            remaining-=h
        if remaining < -1e-6:raise ValueError(f'Cierre excede soporte {m}/{role}')
        add(m,role,pk,remaining,row[9].split(' Reducción:')[0],row[7],f'Soporte por perfil!G{idx}; saldo tras cierre y refuerzo')
    montaje=[]
    for row in wb['Instalación por lote'].iter_rows(min_row=2,values_only=True):
        if isinstance(row[0],int) and (row[2] or row[3]):
            montaje.append(dict(mes=row[0],terminal=row[1],kits=(row[2] or 0)+(row[3] or 0),externos=row[3] or 0,horas_externas=row[4] or 0,banco=row[5] or 0,analista=row[6] or 0))
    return dict(paquetes=paquetes,capacidad=cap,asignaciones=alloc,montaje=montaje,sha256=hashlib.sha256(Path(path).read_bytes()).hexdigest())

def numero(v,dec=2):
    return f'{v:,.{dec}f}'.replace(',','@').replace('.',',').replace('@','.')

def calcular_red(raw):
    pending={n['id']:dict(n) for n in raw};by={};order=[]
    if len(pending)!=len(raw):raise ValueError('Identificadores de red repetidos')
    while pending:
        ready=[key for key,n in pending.items() if all(p['id'] in by for p in n['predecesoras'])]
        if not ready:raise ValueError('Ciclo o predecesora inexistente')
        for key in ready:
            n=pending.pop(key)
            n['ES']=max([n.get('liberacion',0)]+[by[p['id']]['EF' if p['tipo']=='FS' else 'ES']+p.get('lag',0) for p in n['predecesoras']])
            n['EF']=n['ES']+n['duracion'];by[key]=n;order.append(n)
            if n['EF']>n.get('limite',1120):raise ValueError('Límite excedido: '+key)
    successors={n['id']:[] for n in order}
    for n in order:
        for p in n['predecesoras']:successors[p['id']].append((n,p))
    for n in reversed(order):
        latest=[n.get('limite',1120)-n['duracion']]
        for s,p in successors[n['id']]:latest.append(s['LS']-p.get('lag',0)-(n['duracion'] if p['tipo']=='FS' else 0))
        n['LS']=min(latest);n['LF']=n['LS']+n['duracion'];n['HT']=n['LS']-n['ES']
        floats=[n.get('limite',1120)-n['EF']]
        for s,p in successors[n['id']]:floats.append(s['ES']-p.get('lag',0)-(n['EF'] if p['tipo']=='FS' else n['ES']))
        n['HL']=min(floats)
        if n['HT']<0 or n['HL']<0:raise ValueError('Holgura negativa: '+n['id'])
    return order

def tabla(title,label,cols,header,rows):
    return '\n'.join([r'\begin{tabla}[ancho=completo, fuente=condensada]{'+title+'}{'+label+'}{'+cols+'}',header+r' \\ \midrule',*[' & '.join(map(str,row))+r' \\' for row in rows],r'\end{tabla}'])+'\n'

def main():
    d=construir(PLANILLA);OUT.mkdir(exist_ok=True)
    (OUT/'puente.json').write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf-8')
    (OUT/'plan_32.json').write_text(json.dumps({'paquetes':list(d['paquetes'].values())},ensure_ascii=False,indent=2),encoding='utf-8')
    with (OUT/'asignacion-tarea-rol-mes.csv').open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.DictWriter(f,fieldnames=['mes','perfil','paquete','horas','tarea','tarifa','fuente']);w.writeheader();w.writerows(d['asignaciones'])
    monthly=[]
    for m in range(1,57):
        h=sum(a['horas'] for a in d['capacidad'] if a['mes']==m)
        monthly.append([m,numero(h),numero(h/160,4)])
    parts=[r'La \tabref{7-t15-curva32} fija la capacidad interna contratada de cada mes. Los FTE son equivalentes de 160 horas y no un recuento nominal de personas. La prestación externa se declara aparte y no se suma a esta curva.',tabla('Capacidad interna por mes contractual','7-t15-curva32','L{20mm} R{50mm} X','Mes & Horas contratadas & FTE equivalentes',monthly),r'La implementación M1--M20 suma 99.626,67 horas internas y la operación M21--M56, 84.606. El pico es M7, con 39,2306 FTE equivalentes. La variación incluye demanda de ingeniería, sustitución de montaje, refuerzos de puesta en producción y cierre. Las horas son presupuesto de contratación, no horas netas de programación.']
    # Totales por paquete y fase; incluye cierre posterior a H12 bajo su EDT.
    bypk=[]
    for pk,p in d['paquetes'].items():
        hi=sum(a['horas'] for a in d['asignaciones'] if a['paquete']==pk and a['mes']<=20)
        ho=sum(a['horas'] for a in d['asignaciones'] if a['paquete']==pk and a['mes']>=21)
        bypk.append([pk,p['nombre'],numero(hi),numero(ho)])
    parts.extend([r'La \tabref{7-t15-paquetes32} distribuye el presupuesto de capacidad sin duplicar horas. Las atribuciones de innovación se reservan primero conforme a la planilla; el saldo se asigna a preparación, ejecución, revisión y atención de entregables activos. Esta asignación de control no equivale a una medición de productividad ni permite evitar desembolsos de nómina.',tabla('Presupuesto de esfuerzo interno por paquete y fase','7-t15-paquetes32','L{12mm} X R{27mm} R{27mm}','EDT & Entregable & M1--M20 h & M21--M56 h',bypk),r'El cierre de integraciones y datos conserva su código de implementación aunque se ejecute en M21--M24. La suma por paquete y mes coincide con la contratación; las visitas y montaje externos se controlan como servicio adicional separado.'])
    taskrows=[]
    grouped={}
    for a in d['asignaciones']:
        key=(a['paquete'],a['perfil'],'Implementación' if a['mes']<=20 else 'Operación/cierre')
        grouped[key]=grouped.get(key,0)+a['horas']
    for (pk,role,phase),h in sorted(grouped.items()):taskrows.append([pk,role,phase,numero(h)])
    parts.extend([r'La \tabref{7-t15-tarea-rol32} asigna un presupuesto por rol y entregable. La tarea es preparar, ejecutar y revisar el entregable del diccionario T-14; en operación corresponde al servicio y alcance de cada perfil. El registro mensual de control conserva celda de origen, tarea y horas, y en H1 se contrasta con la estimación detallada del ejecutor antes de comprometer reducciones.',tabla('Asignación de trabajo por paquete rol y fase','7-t15-tarea-rol32','L{12mm} X L{35mm} R{24mm}','EDT & Perfil ejecutor & Fase & Horas',taskrows),r'La reserva de una persona no puede contarse dos veces en tareas simultáneas. La comprobación por perfil y mes aplica el límite de la columna I de dotación o G de soporte, descontando previamente las horas atribuidas a innovaciones.'])
    (OUT/'horas-formulario.tex').write_text('\n\n'.join(parts)+'\n',encoding='utf-8')
    red=calcular_red(json.loads((HERE/'red-3.2.json').read_text(encoding='utf-8'))['nodos'])
    (OUT/'red-calculada.json').write_text(json.dumps(red,ensure_ascii=False,indent=2),encoding='utf-8')
    rows=[]
    for n in red:
        pred=', '.join(p['id']+(' SS' if p['tipo']=='SS' else '')+(f"{p.get('lag',0):+}" if p.get('lag') else '') for p in n['predecesoras']) or 'Inicio'
        rows.append([n['id'],n['nombre'],pred,*[n[k] for k in ['duracion','ES','EF','LS','LF','HT','HL']]])
    tex=r'''La \tabref{7-malla32} incorpora las entregas de los contextos, los lotes físicos, el estudio de costo y la migración histórica. Las revisiones R-H son ventanas de contraparte; no duplican esfuerzo de audIT. FS significa fin-inicio y SS inicio-inicio, con el desfase indicado en días. Las cotas de liberación y fecha límite se registran por nodo; HT es LS menos ES y HL el menor margen disponible ante sucesores y fecha límite.

'''+tabla('Red detallada de actividades y holguras contractuales','7-malla32','L{21mm} X L{27mm} R{9mm} R{10mm} R{10mm} R{10mm} R{10mm} R{9mm} R{9mm}','ID & Actividad & Predecesoras & d & ES & EF & LS & LF & HT & HL',rows)+r'''
Las duraciones nuevas son estimaciones de ventana de planificación, no mediciones PERT. La red controla disponibilidad temporal; el presupuesto de esfuerzo se comprueba por perfil y mes. HT cero identifica una restricción activa, que puede ser la ventana de montaje o el límite de un hito, y no implica que todos esos nodos formen una única cadena hasta H12. No se atribuye una probabilidad conjunta a esta red sin un análisis de riesgo recalculado.
'''
    (OUT/'malla-formulario.tex').write_text(tex,encoding='utf-8')
    hits=[n for n in red if re.fullmatch(r'H\d+',n['id'])]
    rows=[[n['id'],n['EF'],n['mes_e25'],n.get('limite',n['EF'])-n['EF']] for n in hits]
    (OUT/'hitos-resumen.tex').write_text(tabla('Hitos E25 y aceptación planificada','7-hitos','L{22mm} R{40mm} R{35mm} X','Hito & Día de aceptación & Mes E-25 & Margen al límite en días',rows),encoding='utf-8')
    print('Conciliación generada:',len(d['asignaciones']),'asignaciones; referencia',d['sha256'])

if __name__=='__main__':main()
