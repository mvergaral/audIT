from pathlib import Path
import subprocess, tarfile, json, hashlib, datetime

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
PREFIX = 'recursos/Formato-Oferta-audIT/'
OUT.mkdir(exist_ok=True)
for folder in ['fuentes', 'referencia', 'evidencia', 'informes', 'paquetes', 'revision', 'insumos-d2']:
    (OUT / folder).mkdir(exist_ok=True)

def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT).decode('utf-8')

baseline = {'commit': git('rev-parse', 'HEAD').strip(), 'estado': git('status', '--porcelain'),
            'sparse': git('sparse-checkout', 'list'), 'fecha_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
            'plazo': '2026-11-25 14:00 America/Santiago', 'revisor_d2': 'Ignacio Cuevas',
            'responsable_entrega': 'Carlos Abarza'}
(OUT/'evidencia/linea-base.json').write_text(json.dumps(baseline,ensure_ascii=False,indent=2),encoding='utf-8')
proc = subprocess.Popen(['git', 'archive', 'HEAD', 'recursos/Formato-Oferta-audIT', 'outputs/cierre-d2-final'],cwd=ROOT,stdout=subprocess.PIPE)
manifest=[]
with tarfile.open(fileobj=proc.stdout,mode='r|') as archive:
    for item in archive:
        if not item.isfile(): continue
        if item.name.startswith(PREFIX):
            rel=item.name[len(PREFIX):]
            if rel.startswith('salida/'):
                if not rel.startswith(('salida/final/', 'salida/final-por-subdocumento/')): continue
                dest=OUT/'referencia'/rel.removeprefix('salida/')
            else:
                dest=OUT/'fuentes'/rel
        else:
            rel=item.name.removeprefix('outputs/cierre-d2-final/')
            dest=OUT/'insumos-d2'/rel
        dest=dest.resolve()
        if not dest.is_relative_to(OUT.resolve()): raise RuntimeError(item.name)
        dest.parent.mkdir(parents=True,exist_ok=True)
        data=archive.extractfile(item).read()
        dest.write_bytes(data)
        manifest.append({'origen':item.name,'destino':str(dest.relative_to(OUT)),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
if proc.wait(): raise RuntimeError('git archive falló')
(OUT/'evidencia/snapshot.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
(OUT/'LEDGER.md').write_text('''# Registro de ejecución del cierre

Base c140209. Plazo 25-11-2026 a las 14:00 America/Santiago.
Revisión humana D2/A-6: Ignacio Cuevas. Responsable de entregar: Carlos Abarza.

## Decisiones de ejecución

- Se conserva el checkout y se ejecuta en una copia aislada de fuentes y entregables bajo esta carpeta. No se modifican las carpetas protegidas del formato original ni cambios locales previos.
- Las correcciones de integración y compatibilidad se aplican solamente a la copia, documentadas y verificadas.
- No se acredita revisión humana ni se aplican firmas nuevas sin evidencia. El nombramiento de responsables no equivale a revisión realizada.
- La malla y el precio se conservan; se verifica su coherencia y se explicitan riesgos y condiciones futuras.

## Estado

1. Snapshot e inventario: creado; manifiesto en evidencia/snapshot.json.
2. Anexos: pendiente de integración.
3. Declaraciones IA: pendiente de corrección y revisión humana.
4. Administrativo: pendiente de cotejo.
5. Económico: pendiente de cotejo.
6. Riesgo de plazo: pendiente de cotejo.
7. Art. 46: pendiente de cotejo.
8. Regeneración: pendiente.
9. Verificación global: pendiente.
10. Paquetes: pendiente.
11. Entrega y preparación física: Carlos Abarza; pendientes de ejecución humana.
''',encoding='utf-8')
print(json.dumps({'archivos':len(manifest),'bytes':sum(x['bytes'] for x in manifest),'directorio':str(OUT)},ensure_ascii=False))
