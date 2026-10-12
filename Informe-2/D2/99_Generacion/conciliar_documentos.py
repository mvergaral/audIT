"""Correcciones acotadas de conciliación documental; no modifica la red CPM."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT / 'recursos/Formato-Oferta-audIT/subdocumentos'

def replace_file(path, replacements):
    text = path.read_text(encoding='utf-8')
    for old, new in replacements:
        text = text.replace(old, new)
    path.write_text(text, encoding='utf-8')

for ext in ('tex', 'md'):
    replace_file(BASE / f'03-solucion/formularios/T-12.{ext}', [
        ('Folio a bordo antes de que el camión se mueva, sin que ningún equipo emita',
         'Representación completa y conforme disponible en cabina antes del movimiento; sólo emite el sistema contable. Comprobación integral de los 90 segundos pendiente, incluida solicitud, emisión, retorno, reensamblado y verificación (S4 y S8, R-28)'),
        ('Ningún viaje inicia el movimiento sin documento de transporte emitido por el sistema contable',
         'Ningún viaje inicia el movimiento sin documento de transporte emitido por el sistema contable y su representación completa y conforme disponible en cabina'),
        ('de las salidas sin cobertura con folio a bordo antes del movimiento',
         'de las salidas sin cobertura con representación completa y conforme en cabina antes del movimiento'),
        ('Registro de folio contra primera posición',
         'Registro de disponibilidad y conformidad de la representación contra primera posición; ensayo integral de 90 segundos pendiente'),
    ])

replace_file(BASE / '13-innovaciones/contenido.tex', [
    (r'montaje propio \textbf{M6–M9}, terceros',
     r'montaje propio \textbf{M6–M9}, con \textbf{flota propia completa en M9}, terceros'),
])
replace_file(BASE / '13-innovaciones/formularios/T-19.tex', [
    ('12.2, con integración a 4.1 y 4.2; conciliación con S7 pendiente.',
     '12.2, con integración a 4.1 y 4.2; calendario acordado con S7.'),
    ('propios M6–M9; terceros', 'propios M6–M9, flota propia completa en M9; terceros'),
])
replace_file(BASE / '07-plan-trabajo/contenido.tex', [
    ('La columna izquierda reúne lo que construye la Etapa 1: gestión, levantamiento, plataforma, equipo a\n'
     'bordo, los seis contextos de la arquitectura lógica y sus integraciones. La columna derecha reúne lo\n'
     'que la acompaña o la sigue: datos y migración, la Etapa 2, la adhesión de los transportistas, la\n'
     'calidad, la implantación, las innovaciones y la operación de 36 meses.',
     'La vista general reúne los trece elementos de primer nivel. Las láminas de detalle desarrollan\n'
     'los mismos 54 paquetes, con su entregable, aceptación y responsable; no añaden alcance. La\n'
     'organización distingue gestión, diseño, plataforma, equipo a bordo, servicios, integraciones,\n'
     'datos, adhesión, calidad, implantación, innovaciones y operación de 36 meses.'),
])
for folder, section, purpose, diagrams in [
    ('03-solucion', '3.4.2 y RF-014/RN-11 del T-12', 'Conciliación de representación completa y conforme en cabina con S4 y R-28; definición del ensayo integral de 90 segundos', 'Ninguno'),
    ('07-plan-trabajo', '7.1 y 7.3.3', 'Actualización de descripción de EDT y generación de vistas generales y detalles legibles de EDT/Gantt; recuperación de PERT conservando el alcance de los paquetes', 'Alto'),
    ('13-innovaciones', '13.2 y ficha T-19 tipo 2', 'Explicitación del cierre de flota propia en M9 y conservación del calendario acordado; valorización incremental pendiente', 'Ninguno'),
]:
    p = BASE / folder / 'declaracion-ia.tex'
    review = 'Nombre, cargo y alcance de la revisión humana' if folder in ('03-solucion','07-plan-trabajo') else 'Revisión humana final y asociación a bitácora A-6 del responsable pendientes'
    line = (f'\\usoIA{{{section}}}{{OpenAI Codex}}{{{purpose}}}{{Alto}}{{{diagrams}}}'
            f'{{\\marcador{{{review}}}}}\n')
    text = p.read_text(encoding='utf-8')
    if f'\\usoIA{{{section}}}{{OpenAI Codex}}' not in text:
        p.write_text(text + '\n' + line, encoding='utf-8')

replace_file(ROOT / 'Informe-2/d2/99_Generacion/generar_plan_detallado.py', [
    ('montaje propio M6–M9, terceros adheridos',
     'montaje propio M6–M9 con flota propia completa en M9, terceros adheridos'),
    ('Documento sin cobertura pendiente de acuerdo con D3 y D4: definir representación completa, tamaño máximo y factibilidad del retorno satelital dentro de 90 s antes de afirmar cumplimiento.',
     'Documento sin cobertura: representación completa y conforme obligatoria en cabina. Tamaño máximo y comprobación integral de 90 s pendientes, conforme a S4 y S8 R-28.'),
])
print('Fuentes conciliadas; red CPM y umbral de adhesión conservados.')
