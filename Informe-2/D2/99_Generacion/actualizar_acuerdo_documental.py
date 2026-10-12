"""Propaga las precisiones aprobadas a documentos y notas de generación."""
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
BASE=ROOT/'recursos/Formato-Oferta-audIT/subdocumentos'
files=[BASE/'03-solucion/contenido.tex',BASE/'03-solucion/formularios/T-12.tex',
       BASE/'03-solucion/formularios/T-12.md',BASE/'09-calidad/formularios/catalogo-T-17.tex',
       BASE/'09-calidad/formularios/T-17.md',ROOT/'Informe-2/d1/subdocs/formulario_t17_protocolo_aceptacion_plan_pruebas.md']
for p in files:
    text=p.read_text(encoding='utf-8')
    text=text.replace('vigente y registrado al corte','vigente, no revocado y registrado al corte')
    # S3 tiene el texto distribuido en dos líneas.
    text=text.replace('vigente y registrado al corte.', 'vigente, no revocado y registrado al corte.')
    p.write_text(text,encoding='utf-8')

for folder,purpose in [('03-solucion','Definición común de adhesión: 148 iniciales, corte M9, RUT único, firmas, vigencia y no revocación; estados técnicos y consentimientos separados'),
                       ('07-plan-trabajo','Precedencia A09 FS-10 de A13 y puerta G13; recálculo de holguras y actualización de PERT y gráficos; sprint 7 y complemento de sprint 8 dentro de 40 días'),
                       ('09-calidad','Ampliación de variantes RF-026 con conteo único por RUT, corte, ambas modalidades, vigencia y no revocación; instalación, activación y consentimientos separados')]:
    p=BASE/folder/'declaracion-ia.tex'
    section={'03-solucion':'3.4.3 y RF-026 del T-12','07-plan-trabajo':'7.3.1, T-15 y T-18'}.get(folder,'Conciliación de capacitación y adhesión')
    review='Nombre, cargo y alcance de la revisión humana' if folder in ('03-solucion','07-plan-trabajo') else 'Revisión humana y asociación a bitácora A-6 del responsable pendientes'
    line=f'\\usoIA{{{section}}}{{OpenAI Codex}}{{{purpose}}}{{Alto}}{{Ninguno}}{{\\marcador{{{review}}}}}\n'
    text=p.read_text(encoding='utf-8')
    if f'\\usoIA{{{section}}}{{OpenAI Codex}}' not in text:
        p.write_text(text+'\n'+line,encoding='utf-8')

p=ROOT/'Informe-2/d2/99_Generacion/generar_plan_detallado.py'
text=p.read_text(encoding='utf-8').replace('Los 25 registros CPM se transcriben del T-15',
    'Las 25 actividades CPM y el hito G13 de liberación se transcriben del T-15')
text=text.replace("notes=['Innovación", "notes=['Capacitación acordada: A13 inicia en el día 182, A09 FS-10 y G13 disponible; 40 días con complemento de sprint 8 incluido. Funciones certificadas de sprint 7 por definir con D3. Monte Carlo pendiente de verificación con la fuente de D4.','Adhesión acordada: 60 de 148 iniciales al cierre de M9 (31-10-2027 bajo SA-01); refuerzo con 59 o menos, RUT único, anexo vigente, no revocado y firmado por mandante y representante autorizado; ambas modalidades. Instalación, activación y consentimientos separados.','Innovación") if 'Capacitación acordada: A13' not in text else text
p.write_text(text,encoding='utf-8')

p=ROOT/'Informe-2/d2/99_Generacion/generar_laminas_impresion.py'
text=p.read_text(encoding='utf-8').replace('Capacitación y umbral de adhesión pendientes de acuerdo.',
    'Red de capacitación y umbral de adhesión acordados; Monte Carlo pendiente de verificación.')
p.write_text(text,encoding='utf-8')

p=ROOT/'Informe-2/d2/00_LEEME_ENTREGABLES.md'
text=p.read_text(encoding='utf-8').replace('Conserva la red CPM existente; el acuerdo de capacitación\ny el umbral de adhesión siguen pendientes.',
    'Usa la red CPM conciliada: A13 inicia en el día 182, condicionada a G13,\ncon 40 días de duración. Adhesión: al menos 60 de 148 iniciales al corte de M9.\nLa verificación de Monte Carlo con la fuente de D4 sigue pendiente.')
text=text.replace('25 actividades del T-15','25 actividades y el hito G13 del T-15')
p.write_text(text,encoding='utf-8')

p=ROOT/'Informe-2/d2/CONSIDERACIONES-D2.md'
text=p.read_text(encoding='utf-8')
text=text.replace('Los siguientes puntos deben cerrarse antes de aprobar la línea base consolidada.',
    'Los siguientes puntos son el registro histórico de conciliación. El acuerdo posterior de capacitación y adhesión está en `ACUERDO_CAPACITACION_ADHESION.md`; sus decisiones sustituyen los pendientes de definición de los puntos 2 y 3.')
text=text.replace('- Capacitación, denominador/umbral de adhesión y recálculo de la simulación permanecen pendientes del acuerdo conjunto; no se modificó la malla CPM.',
    '- Acuerdo ejecutado: A13 en días 182–222, HT 38 y HL 18; A06 HL 24; término día 420. G13 condiciona el inicio a PREPROD/material listo al cierre del sprint 7; complemento del sprint 8 dentro de los 40 días. Adhesión: 60 de 148 iniciales al corte de M9, RUT único, ambas modalidades y anexo firmado, vigente, no revocado y registrado. S3/T-12, S8/T-16 parcial y pruebas de D1 actualizados. Pendientes: definir con D3 funciones certificadas, integrar catálogo original de D4 y verificar Monte Carlo; 82,3 %, 14,1 %, 92,1 % y 0,1 % son resultados reportados, no verificados aquí.')
text=text.replace('Siete controles documentales automatizados pasan.',
    'Once controles documentales y de cálculo automatizados pasan.')
p.write_text(text,encoding='utf-8')
print('Definiciones, declaraciones de IA y registro de coordinación actualizados.')
