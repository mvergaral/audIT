"""Prepara el paquete de D2 para revisión humana e integración global."""
from pathlib import Path
import csv,json,hashlib,zipfile,shutil,re
OUT=Path(__file__).resolve().parent;ROOT=OUT.parents[1]
BASE=ROOT/'recursos/Formato-Oferta-audIT';DOC=OUT/'documentos'

def write(name,text):
    p=OUT/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(text,encoding='utf-8');return p

for scope in ['tecnico','economico']:
    log=(OUT/'evidencia'/f'verificador-{scope}-windows.log').read_text(encoding='utf-8')
    assert re.search(r'REGLAS_NO_CUMPLIDAS 0\b',log),f'Control {scope} aún no cerrado'
calc=json.loads((OUT/'evidencia/recalculo-modelo-final.json').read_text(encoding='utf-8'))
assert not calc['diferencias'] and not calc['errores'] and calc['tarifas_rango']
assert all(calc['conciliacion_venta_personal'].values())

tech=['AUDIT-Subdocumento3.pdf','AUDIT-Formulario-T-12.pdf','AUDIT-Subdocumento7.pdf',
      'AUDIT-Formulario-T-14.pdf','AUDIT-Formulario-T-15.pdf','AUDIT-Formulario-T-18.pdf']
econ=['AUDIT_OfertaEconomica_1_20261125.pdf','AUDIT_OfertaEconomica_1_20261125.docx',
      'AUDIT_AnalisisFinanciero_2_20261125.pdf','AUDIT_AnalisisFinanciero_2_20261125.docx',
      'AUDIT_ModeloFinanciero_3_20261125.xlsx']
for name in tech+econ:assert (DOC/name).is_file(),name

write('CIERRE-D2.md','''# Cierre documental de D2 para revisión e integración

**Preparado y verificado en el alcance indicado. Pendientes revisión humana, firmas e integración global. No se ha enviado ni publicado la oferta.**

## Técnico de D2

Se recompilaron S3, T-12, S7, T-14, T-15 y T-18 desde el mismo corte con bibliografía y referencias externas reales. No quedan referencias ?? ni cajas desbordadas en el control final. S7 corrige la afirmación de PERT completo y explicita los márgenes nulos y las condiciones de validación de capacidad. La fuente residual no usada de ReportLab en S7 se incrustó sin cambiar texto ni píxeles de las doce páginas afectadas.

El verificador ejecutado con correcciones de compatibilidad Windows informa **21 controles, cero incumplimientos y dos avisos**. Los avisos son de tablas de formularios y estilo de escritura. Es una comprobación formal; no acredita ejecución del proyecto ni revisión humana de cada afirmación de ingeniería. Se inspeccionó una muestra dirigida de 22 páginas de los seis PDF. Los siete controles activos de conciliación del presupuesto y la malla pasan. Los controles históricos de octubre corresponden a una red y gráficos reemplazados y no se presentan como comprobación de este corte.

Los seis PDF se entregan con folio inicial 1 por archivo para integración. **D1 debe asignar la secuencia global del Sobre 2 y su hoja resumen al ensamblar los 14 capítulos y formularios.** Este paquete de D2 no sustituye el Sobre 2 completo. No se aplicaron imágenes de firma a los PDF nuevos.

## Económico

Se completaron las fuentes de los entregables 1 y 2 del E-21, incluidas condiciones, doce criterios de aceptación, flujo mensual M1-M56, costos operacionales, cobertura de soporte, adquisiciones e innovaciones. Las monedas y principales tablas se derivan de las partidas del modelo. Se corrigieron cuatro inclusiones que el exportador DOCX omitía y se incorporaron ambas curvas como imágenes al DOCX de análisis.

Decisiones aceptadas por el usuario: vigencia comercial de 150 días y operación sin reajuste; desagregación de tarifas de referencia por fase dentro de E-26, sin facturación horaria adicional y sin cambiar el precio global. La fecha 25-11-2026 identifica la aplicación de parámetros convencionales E-24 a la oferta, no una cotización de mercado.

El XLSX conserva los flujos, fórmulas y precios de la base 3.2, corrige dos notas de montaje y añade las hojas Tarifas E26 Final y Condiciones oferta. Se declararon 31 entradas de perfil por fase, con validación de rango y fórmulas protegidas. Las referencias de roles adicionales son comparaciones de rango, no acreditaciones profesionales. La venta total de personal por fase se conserva exactamente.

Se retiraron los valores guardados de las fórmulas en una copia y se recalculó con LibreOffice: **32.661 fórmulas comparadas, cero diferencias y cero errores**. El verificador económico informa **24 controles, cero incumplimientos y un aviso editorial**. Compara 37 celdas contra partidas y las cifras entre PDF, DOCX y modelo. No equivale a probar todos los escenarios o a acreditar contratos bancarios y comerciales.

Los PDF económicos usan folios continuos: oferta 1-14 y análisis 15-33. Los DOCX tienen paginación propia de su formato; se revisaron mediante render. Las firmas y la revisión humana siguen pendientes. El modelo de evaluación mantiene VAN sobre Fila A M1-M56, informa M57 separado y conserva los escenarios condicionados de financiación sin presentarlos como aprobados.

## Respuesta a D4 y riesgo de plazo

Se reprodujo el script de D4 con la red de 122 nodos, 10.000 corridas y semilla 2026: reproduce las probabilidades del aviso. Son resultados provisionales con tres puntos supuestos, no estimaciones de ejecutores validadas. No se modificaron fechas, relaciones, duraciones, plantilla de personal ni costos para mejorar artificialmente el resultado.

H4, H7 y H12 siguen sin margen al límite; H11 es un hito de fecha fija protegido por A23. La secuencia obligatoria A24 (360-400), A25 (400-410) y R-H12 (410-420) consume el plazo hasta H12. No puede afirmarse recuperada una holgura sin revisar trabajo, solapamientos permitidos y capacidad neta. La exposición alta R-17 y la validación en H1 permanecen explícitas. Esto es un riesgo de ingeniería que el equipo debe defender y revisar, no un defecto corregido por tener PDF compilados.

## Qué falta para liberar

1. Ignacio Cuevas, como responsable designado de D2, debe revisar contenido, supuestos, condiciones y cifras y completar/firmar el A-6 correspondiente. La declaración de los PDF sigue indicando revisión por realizar.
2. D1 debe integrar los seis archivos y el anexo de observaciones con el resto del Sobre 2, asignar folios e índice global y comprobar nombres/enlaces del conjunto.
3. El equipo debe revisar la exposición R-17, disponibilidad de ejecutores/terceros y soporte comercial del financiamiento y proveedores. Las condiciones futuras no se dan por ejecutadas.
4. Obtener las firmas que correspondan al representante de la oferta. La firma A-6 del integrante no sustituye las firmas del oferente.
5. Confirmar el Sobre 1 con D1. No está cubierto por este paquete.

El ZIP de revisión contiene únicamente los seis PDF técnicos y los cinco archivos económicos. Los informes, código, manifiestos y borradores históricos se mantienen fuera. El ZIP económico dentro de la carpeta paquetes conserva el nombre normativo, pero su carpeta y este registro dejan clara la liberación pendiente.
''')

write('RESPUESTA-D4-PARA-COORDINAR.md','''D4: D2 reprodujo montecarlo32 sobre los 122 nodos vigentes (10.000 corridas, semilla 2026) y confirmó el resultado del aviso. No se alteró la malla ni se reutilizaron probabilidades históricas. H4/H7/H12 conservan margen cero; H11 mantiene su fecha fija y la reserva A23. S7 ahora explicita esta exposición y la diferencia entre capacidad presupuestada y capacidad neta. Para recuperar margen hace falta una variante de ingeniería sustentada; no se acortaron duraciones ni se asignaron refuerzos ficticios. R-17 y la validación de tres puntos/turnos en H1 siguen abiertas.

La copia económica final corrige C83 de Parámetros corrección y A17 de Conciliación técnica: 182 equipos montados M9 y técnico interno hasta antes de M19, sin alterar costos. La fuente de comparación y los resultados están en outputs/cierre-d2-final/evidencia/. Mensaje preparado para coordinación; no enviado.
''')

record='''# Registro A-6 del cierre de D2

Fecha: 25-11-2026. Responsable designado por el usuario: Ignacio Cuevas. Rol del proyecto: D2. Revisión humana y firma: pendientes; no se certifican mediante este registro.

Se utilizó OpenAI Codex para completar fuentes económicas E-21, aplicar condiciones comerciales aceptadas, desagregar tarifas dentro de E-26 manteniendo los precios de personal, agregar hojas de control al XLSX, compilar los seis PDF D2 y los dos económicos, corregir referencias y desbordes, reproducir conciliación y simulación existente, ejecutar verificadores y preparar paquetes para revisión. La red y las duraciones no se alteraron. El caso base conserva flujos y precios; no se inventaron contratos, cotizaciones, firmas ni resultados de ejecución del proyecto.

La revisión humana debe comprobar especialmente condiciones comerciales, perfiles y tarifas, holguras, capacidad por turno, sensibilidad de caja y supuestos de terceros. Las declaraciones de IA de S3/S7 no se actualizan a “revisado” hasta que la persona realice y acredite esa acción. El registro del corte está en CIERRE-D2.md y evidencia/ de outputs/cierre-d2-final.

Este registro interno debe asociarse al A-6 del oferente y a la bitácora individual que corresponda. El código D2 identifica una dupla del proyecto y no determina por sí solo la numeración Persona 1-8 del trabajo de investigación.
'''
write('REGISTRO-A6-D2-PARA-REVISION.md',record)
p=ROOT/'Investigacion/Registro_A6_Cierre_D2_20261125.md';p.parent.mkdir(parents=True,exist_ok=True);p.write_text(record,encoding='utf-8')

# Publicar las copias de trabajo en las carpetas propias de D2 sin borrar las versiones previas.
for folder,n,names in [('03-solucion',3,tech[:2]),('07-plan-trabajo',7,tech[2:])]:
    target=BASE/'subdocumentos'/folder/'preparacion-final/cierre-20261125';target.mkdir(parents=True,exist_ok=True)
    for name in names:shutil.copy2(DOC/name,target/name)
    (target/'LEEME.md').write_text('Corte verificado de D2. Revisión humana, firmas y folios globales del Sobre 2 pendientes. Ver outputs/cierre-d2-final/CIERRE-D2.md. No mezclar con los PDF de preparación anteriores.\n',encoding='utf-8')
target=BASE/'economico/planilla'/econ[-1];shutil.copy2(DOC/econ[-1],target)

readme=BASE/'subdocumentos/07-plan-trabajo/preparacion-final/LEEME.md'
old=readme.read_text(encoding='utf-8')
if 'cierre-20261125/' not in old:
    readme.write_text('## Corte actualizado del 25-11-2026\n\nUsar los PDF de `cierre-20261125/` y el registro `outputs/cierre-d2-final/CIERRE-D2.md`. Las copias siguientes se conservan como antecedentes. Faltan revisión humana, firmas e integración global de folios.\n\n'+old,encoding='utf-8')

write('LEEME.md','''# Entrega de D2 para revisión

Empezar por CIERRE-D2.md. Las decisiones comerciales aceptadas y los controles están en evidencia/.

El paquete D2_PARA_REVISION_20261125.zip contiene 11 archivos: seis PDF técnicos y cinco económicos. No incluye el Sobre 1 ni el resto del Sobre 2. No es una oferta enviada ni firmada. El PDF es la referencia de foliación del sobre económico; los DOCX deben revisarse en Word/LibreOffice según su propia paginación.

Para reproducir la generación: integrar las fuentes y datos del ZIP sobre el corte de repositorio indicado en evidencia/linea-base.json, ejecutar preparar_fuentes.py para crear la copia aislada y luego compilar_d2.py y compilar_economico.py, incorporar las curvas y normalizar los DOCX con completar_docx.py y verificar con verificar_corte.py. El paso de fuente residual en S7 conserva texto y píxeles. Los runners usan la copia aislada fuentes/ y no modifican estilos o configuración compartidos. compilar_d2.py requiere MiKTeX y biber disponibles; los scripts de documentos usan el runtime indicado por Codex.

No ejecutar los generadores iniciales de contenido sobre fuentes revisadas sin revisar su efecto. Los manifiestos técnico y económico tienen nombres separados. Los auxiliares y renders no se entregan.
''')

dest=OUT/'paquetes';dest.mkdir(exist_ok=True)
manifest=[]
def package(name,files):
    path=dest/name
    with zipfile.ZipFile(path,'w',zipfile.ZIP_DEFLATED) as z:
        for path_source,arc in files:z.write(path_source,arc)
    with zipfile.ZipFile(path) as z:
        assert z.testzip() is None
        assert set(z.namelist())=={arc for _,arc in files}
        extract=OUT/'revision/extraccion'/path.stem;extract.mkdir(parents=True,exist_ok=True);z.extractall(extract)
        for source,arc in files:assert hashlib.sha256(source.read_bytes()).digest()==hashlib.sha256((extract/arc).read_bytes()).digest()
    record=dict(paquete=path.name,bytes=path.stat().st_size,sha256=hashlib.sha256(path.read_bytes()).hexdigest(),crc='OK',extraccion='OK',
                archivos=[dict(nombre=arc,sha256=hashlib.sha256(src.read_bytes()).hexdigest(),bytes=src.stat().st_size) for src,arc in files])
    manifest.append(record)

package('D2_PARA_REVISION_20261125.zip',[(DOC/n,('tecnico/' if n in tech else 'economico/')+n) for n in tech+econ])
package('SOBRE3_AUDIT_OFERTA_ECONOMICA_20261125.ZIP',[(DOC/n,n) for n in econ])
sources=[]
for directory in ['subdocumentos/03-solucion','subdocumentos/07-plan-trabajo','economico']:
    for p in (BASE/directory).rglob('*'):
        if not p.is_file() or any(t in p.parts for t in ['preparacion-final','compilacion','version-anterior','__pycache__']):continue
        if p.suffix in ['.log','.aux','.bcf','.bbl','.blg','.fls','.gz']:continue
        if p.parent==BASE/'subdocumentos/07-plan-trabajo' and p.suffix=='.pdf':continue
        sources.append((p,(Path('recursos/Formato-Oferta-audIT')/p.relative_to(BASE)).as_posix()))
for relative in ['outputs/3.2/Entrega-3.2/INFORME3_AUDIT_PLANILLA_3.2_20261115.xlsx','Informe-3/d3/datos/dedicacion_mensual_d3.csv']:
    if (ROOT/relative).exists():sources.append((ROOT/relative,relative))
for p in OUT.glob('*.py'):sources.append((p,'outputs/cierre-d2-final/'+p.name))
sources.append((OUT/'CIERRE-D2.md','outputs/cierre-d2-final/CIERRE-D2.md'))
sources.append((OUT/'evidencia/tarifas-aceptadas.json','outputs/cierre-d2-final/evidencia/tarifas-aceptadas.json'))
sources.append((OUT/'evidencia/linea-base.json','outputs/cierre-d2-final/evidencia/linea-base.json'))
package('D2_FUENTES_PARA_INTEGRACION_20261125.zip',sources)
write('evidencia/manifiesto-final.json',json.dumps(manifest,ensure_ascii=False,indent=2))

# Actualizar la lista global sin declarar resueltos firmas o folios ajenos.
global_dir=ROOT/'outputs/cierre-entrega-final';p=global_dir/'MATRIZ-UNICA.csv'
if p.exists():
    rows=list(csv.DictReader(p.open(encoding='utf-8-sig')));fields=list(rows[0])
    local={'S2-S03','S2-S07','S2-T12','S2-T14','S2-T15','S2-T18','S3-E1','S3-E2','S3-MOD','S3-TAR','S3-TXT'}
    for r in rows:
        if r['ID'] in local:
            r['Evidencia']='Corte D2 verificado: outputs/cierre-d2-final/CIERRE-D2.md'
            r['Brecha']='Revisión humana y firmas; en técnico, integración global D1; ver límites del cierre D2.'
            r['Estado']='parcial'
        if r['ID'] in {'S3-COM','S3-FEC'}:
            r['Evidencia']='Condiciones aceptadas: vigencia150 días, sin reajuste; fecha convencional de aplicación E24 en la oferta.';r['Brecha']='Revisión de presentación y firmas';r['Estado']='verificado'
    with p.open('w',encoding='utf-8-sig',newline='') as f:w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
    esc=lambda x:str(x).replace('|','/').replace('\n',' ')
    (global_dir/'MATRIZ-UNICA.md').write_text('# Matriz única de cierre\n\nActualización D2: ver outputs/cierre-d2-final/CIERRE-D2.md.\n\n| '+' | '.join(fields)+' |\n|'+'---|'*len(fields)+'\n'+'\n'.join('| '+' | '.join(esc(r[k]) for k in fields)+' |' for r in rows)+'\n',encoding='utf-8')
    p=global_dir/'INFORME-DE-CIERRE.md';text=p.read_text(encoding='utf-8')
    if 'Actualización D2' not in text:p.write_text('> Actualización D2 del 25-11-2026: condiciones, tarifario y documentos económicos completados y verificados en `outputs/cierre-d2-final/CIERRE-D2.md`. Este informe conserva el diagnóstico global inicial; no confundir sus pendientes históricos de D2 con el corte nuevo. Sobre1, firmas y ensamblaje global siguen pendientes.\n\n'+text,encoding='utf-8')
print(json.dumps({'archivos_entregables':11,'paquetes':[r['paquete'] for r in manifest],'estado':'Verificado para revisión humana e integración; sin firmas ni envío'},ensure_ascii=False))
