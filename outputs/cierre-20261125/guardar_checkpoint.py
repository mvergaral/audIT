from pathlib import Path
import json,hashlib,shutil,datetime,subprocess
O=Path(__file__).resolve().parent;R=O.parents[1];B=O/'fuentes'
snapshot=json.loads((O/'evidencia/snapshot.json').read_text(encoding='utf-8'))
known={x['destino'].replace('\\','/'):x for x in snapshot if x['destino'].replace('\\','/').startswith('fuentes/')}
modified=[]
for p in B.rglob('*'):
    if not p.is_file() or 'salida' in p.parts or (p.suffix not in ('.tex','.py','.sty','.cls') and p.name!='.latexmkrc'):continue
    relative=p.relative_to(O).as_posix();old=known.get(relative)
    if not old or hashlib.sha256(p.read_bytes()).hexdigest()!=old['sha256']:modified.append(p)
comp=[]
for p in sorted((B/'salida/aux/final').glob('*/resultado-directo.json')):
    comp.append({'documento':p.parent.name,'ultimo_resultado':json.loads(p.read_text()),'mtime':datetime.datetime.fromtimestamp(p.stat().st_mtime,datetime.timezone.utc).isoformat()})
(O/'evidencia/compilacion-checkpoint.json').write_text(json.dumps(comp,ensure_ascii=False,indent=2),encoding='utf-8')
admin=B/'salida/administrativo/AUDIT-Sobre1-Antecedentes-Administrativos.pdf'
if admin.exists():
    (O/'documentos').mkdir(exist_ok=True)
    shutil.copy2(admin,O/'documentos/PROVISIONAL_Sobre1_20261125.pdf')
state={'estado':'PAUSADO_A_SOLICITUD_DEL_USUARIO','fecha_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
       'base':'c140209','plazo_confirmado':'2026-11-25 14:00 America/Santiago','revisor_d2':'Ignacio Cuevas',
       'responsable_entrega':'Carlos Abarza','revision_humana_acreditada':False,'enviado':False,
       'video':'Usuario confirma listo; enlace pendiente','fuentes_modificadas':[p.relative_to(R).as_posix() for p in modified],
       'compilacion_tecnica':'Interrumpida durante primera vuelta de la segunda corrida; sin conjunto final estabilizado.',
       'administrativo':'25 piezas simuladas escritas; último PDF concluido de 37 páginas conservado como provisional.',
       'economico':'5 archivos cotejados, 37 partidas conciliadas; modelo y precio sin cambios.',
       'pendientes':['Compilar formularios IA y terminar técnico','Recompilar y cotejar A6 y poder administrativo finales','Verificación global y visual de los PDF definitivos','Razones por respuesta material RIE-05','Enlace video y coherencia identidad web','Revisión humana y firmas','Tres ZIP extraídos y verificados','Preparación física y entrega simultánea por Carlos']}
(O/'ESTADO-EJECUCION.json').write_text(json.dumps(state,ensure_ascii=False,indent=2),encoding='utf-8')
ledger=O/'LEDGER.md'
ledger.write_text(ledger.read_text(encoding='utf-8')+'\n## Pausa solicitada por el usuario\n\nEjecución detenida el 25-11-2026 aproximadamente a las 13:21 de Chile. El estado inicial anterior queda supersedido por REANUDAR.md y ESTADO-EJECUCION.json. Fuentes corregidas y revisiones guardadas; no hay oferta liberada ni enviada. Compilaciones activas interrumpidas; no quedaron procesos de esta ejecución activos en la comprobación.\n',encoding='utf-8')
plan=R/'docs/superpowers/plans/2026-11-25-cierre-entrega-final.md'
t=plan.read_text(encoding='utf-8')
notice='''
## Estado de ejecución al pausar el 25 de noviembre de 2026

**Pausado por solicitud expresa del usuario para conservar contexto y subir el avance al repositorio. No declarar la oferta lista.**

El registro completo y las instrucciones para retomar están en [REANUDAR.md](../../../outputs/cierre-20261125/REANUDAR.md) y el estado estructurado en [ESTADO-EJECUCION.json](../../../outputs/cierre-20261125/ESTADO-EJECUCION.json). No reiniciar desde cero ni ejecutar de nuevo los scripts de edición no idempotentes.

| Tarea | Estado al pausar |
|---|---|
| 1. Corte e inventario | Snapshot y registro realizados; matriz final depende del ensamblaje. |
| 2. Anexos | Fuentes e integración S1/S2/S5 preparadas; folios y PDF finales pendientes. |
| 3. IA y revisión humana | Autoría corporativa y declaraciones corregidas; revisión/firma reales pendientes. |
| 4. Sobre 1 | 25 piezas simuladas creadas por autorización expresa; PDF provisional de 37 páginas; verificar última edición de A-6/poder e índice tras recompilar. |
| 5. Sobre 3 | Cinco archivos y 37 partidas cotejados; fórmula/precio preservados. Revisión humana pendiente. |
| 6. Riesgo y coherencia | Correcciones documentales realizadas; capacidad/ventanas futuras no acreditadas y RIE-05 parcial. |
| 7. Art. 46 | 74 filas inventariadas; estados y localizadores corregidos; cotejar evidencia/folios finales. |
| 8. Regeneración | Segunda corrida global interrumpida durante su primera vuelta. Sin manifiesto final estabilizado. |
| 9. Verificación global | Runner preparado; pendiente ejecutarlo sobre técnico completo y revisar imágenes. |
| 10. Firmas y ZIP | Pendientes; no existen tres paquetes finales comprobados de este corte. |
| 11. Entrega | Carlos Abarza designado; no se envió ni presentó nada. |

El usuario confirmó que el video está listo y facilitará el enlace. Ignacio Cuevas mantiene revisión/firma D2/A-6, Carlos Abarza la entrega, y el plazo confirmado sigue siendo las 14:00 de Chile del 25-11-2026. Si se retoma después, confirmar la situación del plazo sin asumir prórroga.

'''
if '## Estado de ejecución al pausar' not in t:t=t.replace('\n> Para ejecutar este plan:',notice+'> Para ejecutar este plan:',1)
plan.write_text(t,encoding='utf-8')
# Lista estricta para no incorporar cambios locales anteriores o cachés.
files=[plan,*modified,*O.glob('*.py'),O/'REANUDAR.md',O/'LEDGER.md',O/'ESTADO-EJECUCION.json']
files += list((O/'informes').glob('*.md'))+list((O/'informes').glob('*.json'))+list((O/'informes').glob('*.csv'))
files += list((O/'evidencia').glob('*.json'))+list((O/'evidencia').glob('compilacion-*.log'))+list((O/'evidencia').glob('prueba-compilador.log'))
files += list((O/'documentos').glob('PROVISIONAL_*.pdf'))
names=sorted({p.relative_to(R).as_posix() for p in files if p.exists()})
(O/'evidencia/archivos-checkpoint.json').write_text(json.dumps(names,ensure_ascii=False,indent=2),encoding='utf-8')
names.append('outputs/cierre-20261125/evidencia/archivos-checkpoint.json')
subprocess.run(['git','add','--',*names],cwd=R,check=True)
print(json.dumps({'archivos_preparados':len(names),'fuentes_corregidas':len(modified),'pdf_administrativo':admin.exists()},ensure_ascii=False))
