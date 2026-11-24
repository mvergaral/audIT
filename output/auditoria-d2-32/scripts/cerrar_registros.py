from pathlib import Path
import re
ROOT=Path(__file__).resolve().parents[2]/'tmp/cierre-entrega-3'
B=ROOT/'recursos/Formato-Oferta-audIT'
source=Path(__file__).parent/'fuentes/recursos/Formato-Oferta-audIT/anexos/observaciones-informe3.tex'
target=B/'anexos/observaciones-informe3.tex'
s=target.read_text(encoding='utf-8') if target.exists() else source.read_text(encoding='utf-8')
updates={
'ALC-01':('Meses contractuales separados del calendario civil SA-01; curva física 10/60/60/52 y condiciones de firma, stock y paso por terminal explícitas.','S3 supuestos y tabla 3-montaje; S7 calendario; T-12 SA-01 y T-18. Estado: Incorporada documentalmente'),
'ALC-02':('El procedimiento distingue preservación, reenvío, deduplicación, conciliación y retorno A/B de recuperación presencial. El ensayo CP-SYS-20 se exige antes del paso.','S3 sec:3-reversion; T-18 tabla t18-reversion; T-17 CP-SYS-20. Estado: Incorporada en diseño; ensayo futuro'),
'ALC-03':('Inventario individual incorporado: 374 RT transversales, 27 requisitos del Caso y 13 cruces administrativos, con localizador, estado documental y verificación prevista. La acreditación de filas sin evidencia específica se mantiene diferenciada.','T-12 tablas t12-transversales, t12-caso y t12-administrativas. Estado: Parcial; inventario incorporado y evidencia por acreditar'),
'ALC-04':('Los 42 requisitos propios distinguen compromiso, evidencia de diseño y comprobación futura, incluidas autorizaciones, adhesión y retorno satelital. No se atribuyen resultados de ensayos aún no ejecutados.','T-12 RF-003, RF-014 y RNF-005; S3 catálogo. Estado: Incorporada documentalmente'),
'ALC-05':('Tablas del formulario con prefijo propio T-12 y remisiones separadas de las tablas del cuerpo S3.','T-12 numeración y referencias. Estado: Incorporada'),
'ALC-06':('S3 se presenta como oferta autónoma; el historial se conserva en el expediente interno y esta tabla.','S3 contenido; registro D2 de conciliación. Estado: Incorporada'),
'PLA-01':('Los contextos y productos conservan código EDT; la lectura por capacidades cruza ambas etapas y los sprints detallan su entrega y dependencia.','S7 capacidades y EDT; T-14; T-15 nodos A09 y A20 desagregados. Estado: Incorporada documentalmente'),
'PLA-02':('Se regeneraron árbol y vistas jerárquicas desde el mismo catálogo de 54 paquetes; el diccionario queda en T-14.','S7 anexos EDT y T-14. Estado: Incorporada'),
'PLA-03':('Cinco innovaciones con ventanas y nodos identificables, atribución de demanda reservada dentro de la capacidad mensual, sin duplicar nómina.','T-14 EDT12; T-15 asignación por tarea, rol y fase; anexos vigentes. Estado: Incorporada documentalmente'),
'PLA-04':('Puente mensual por tarea, paquete, perfil y fase concilia exactamente con 99.626,67 horas internas de implementación y 84.606 de operación; se separan demanda directa, guardias y saldo de capacidad reservada.','T-15 curvas y asignación; registro mensual de control. Estado: Incorporada como presupuesto de ejecución sujeto a revisión en H1'),
'PLA-05':('A09 se divide en ocho sprints y A20 en cinco con dependencias por capacidad; se recalculan ES, EF, LS, LF, HT y HL sin atribuir una ruta única a todos los nodos con HT cero.','T-15 malla detallada; S7 red y Gantt de control. Estado: Incorporada'),
'PLA-06':('El estudio de costo, la migración histórica, la preparación del cierre y el retiro del legado tienen nodos, límites, predecesoras y recursos propios.','T-15 COST-M6, A08-HIST1, A24-HIST2 y CE2; T-14 EDT2.5/7.2. Estado: Incorporada'),
'PLA-07':('Carta por paquete incorporada a T-14 y malla completa con dependencias y holguras en T-15; la vista CPM muestra la cadena de control de H12.','T-14 carta Gantt; T-15 malla; S7 diagrama CPM. Estado: Incorporada documentalmente'),
'PLA-08':('La red libera diseño preparatorio y ambientes de desarrollo para paralelizar trabajo sin esperar actas no habilitantes; conserva revisiones de aceptación y los doce hitos en su mes.','T-15 relaciones FS/SS y fechas de liberación. Estado: Incorporada como línea base de planificación'),
'PLA-09':('EDT separada de la Gantt; doce vistas temáticas y una malla tabular sustituyen las conclusiones de la red anterior.','S7 anexos activos y T-14. Estado: Incorporada'),
'PLA-10':('Se reserva presencia en los 35 relevos semanales y se documentan cupos, reemplazo, simulación en PREPROD y certificación por perfil; la agenda se confirma con terminales.','S7 partición de capacidad; T-18 capacitación. Estado: Parcial; programación documentada y disponibilidad del mandante por confirmar'),
'PLA-11':('Se eliminó el nodo mixto A18: montaje físico en A11-PIL y M7/8/9-KIT; escalamiento lógico en A18-INT M13--M15.','T-15 malla; T-14 EDT4.2/4.3; Gantt de plataforma. Estado: Incorporada'),
'PLA-12':('Los lotes tienen límites por ventana y no se presume que un cierre aislado represente el riesgo de invierno. Se exige agenda, stock previo y tratamiento de cierres sucesivos mediante alternativa y control de cambios.','S7 calendario y condiciones de montaje; T-18; T-16 riesgo por mantener actualizado. Estado: Parcial; mecanismo documentado y logística efectiva por acreditar'),
'PLA-13':('El montaje distingue 210 balizas iniciales, 21 de reserva, cinco lectores y 19 equipos a bordo de reposición; banco, puesto, analista y servicio externo se imputan una vez.','S3 balizas; T-14 EDT12.3; T-15 servicio físico y asignación; T-18. Estado: Incorporada en planificación'),
'PLA-14':('T-14 incorpora directamente las doce láminas de Gantt. El cierre y estabilización E2 M21--M24 están separados de H12 y conciliados con la capacidad de soporte.','T-14 carta; T-15 CE2 y cierre; T-18 M21--M24. Estado: Incorporada documentalmente'),
}
def fields(line):
    # Conserva literalmente la observación de origen y cambia solo respuesta y localizador.
    pos=line.index(']')+1;vals=[]
    while pos<len(line):
        if line[pos]!='{':pos+=1;continue
        start=pos+1;level=1;pos+=1
        while pos<len(line) and level:
            if line[pos]=='{':level+=1
            elif line[pos]=='}':level-=1
            pos+=1
        vals.append(line[start:pos-1])
    return vals
out=[]
for line in s.splitlines():
    if line.startswith(r'\observacion[sub='):
        f=fields(line)
        if f and f[0] in updates:
            response,locator=updates[f[0]]
            line=line[:line.index(']')+1]+''.join('{'+x+'}' for x in [f[0],f[1],response,locator])
    out.append(line)
target.write_text('\n'.join(out)+'\n',encoding='utf-8')
for sub in ['03-solucion','07-plan-trabajo']:
    p=B/'subdocumentos'/sub/'declaracion-ia.tex'
    scope='S3, T-12, matriz de bases y reversión' if sub.startswith('03') else 'S7, T-14, T-15, T-18, EDT y Gantt'
    p.write_text(r'\usoIA{'+scope+r'}{OpenAI Codex}{Conciliación con la entrega económica 3.2, generación de fuentes y salidas, cálculo y comprobación documental}{Alto}{Alto}{D2, Analista de Planificación y Calidad: revisión humana de esta corrección por realizar antes de emitir. Las revisiones de versiones previas no se extienden automáticamente a esta edición.}'+'\n',encoding='utf-8')
reg=ROOT/'Investigacion/Persona-8/Registro_A6_Consistencia_D2_20261124.md';reg.parent.mkdir(parents=True,exist_ok=True)
reg.write_text('''# Registro A6 de conciliación D2 con la entrega 3.2

Fecha: 24 de noviembre de 2026. Herramienta: OpenAI Codex. Alcance: revisión y corrección de S3/S7, T-12/T-14/T-15/T-18, anexos activos y respaldos económicos relacionados.

Intervención alta en redacción, cálculo de planificación, generación de matrices y gráficos. Se emplearon asistentes separados para S3, revisión independiente de la red y cierre económico; el controlador integró y verificó los cambios.

Se preservó la planilla histórica 3.2. La copia vigente cambia rótulos; fórmulas, números y cachés se contrastan con el original. Las horas mensuales y las atribuciones se comprobaron por perfil; las ventanas de red son estimaciones de planificación y no mediciones de ejecución.

La revisión humana de los cambios del 24 de noviembre no se ha declarado realizada. Los titulares revisan la asignación por tarea/turno, la competencia de conducción técnica reservada en Gestión de Servicio y las condiciones externas antes de emitir. La conformidad de versiones anteriores no acredita estos cambios. Este registro debe incorporarse al expediente A6 individual y firmarse por el responsable después de su revisión.

Expediente de evidencia: output/auditoria-d2-32 en la raíz de trabajo. Fuentes y entregables corregidos: worktree tmp/cierre-entrega-3. No se hizo commit ni publicación.
''',encoding='utf-8')
for name in ['ARCHIVOS-VIGENTES.md','PENDIENTES-ENTREGA-FINAL.md']:
    (B/'subdocumentos/07-plan-trabajo'/name).write_text('''# S7 conciliado con la entrega 3.2

La edición activa es la conciliación del 24 de noviembre de 2026: contenido.tex, formularios T-14/T-15/T-18 y preparacion-final/. La Gantt activa usa red-3.2.json y los resultados de conciliacion-3.2/. Las figuras se regeneran con conciliar_32.py, generar_anexos_32.py y generar_edt_revisada.py. generar_gantt_revisada.py redirige a la versión vigente.

S7_Integrado_Revision.pdf es la copia integrada activa. Los documentos de preparacion-final/ se revisan individualmente desde folio 1; los folios globales y hoja resumen se asignan al ensamblar la oferta completa.

La planilla histórica 3.2 conserva su contenido. Las cifras de T-15 son capacidad interna contratada; los montajes y visitas externos se controlan aparte. La red desagregada sustituye el análisis PERT anterior; no se trasladan probabilidades de la red histórica a los nodos nuevos.

Antes de emitir se revisan capacidad neta por ejecutor y turno, disponibilidad de terceros, competencia del puesto de conducción de cierre y bitácora A6. Las evidencias de ejecución y autorizaciones futuras no se declaran realizadas. El paquete de revisión conserva estas condiciones y no certifica la oferta completa ni los subdocumentos ajenos a D2.
''',encoding='utf-8')
print('Art46 actualizado en alcance D2; registro A6 y declaraciones transparentes generados.')
