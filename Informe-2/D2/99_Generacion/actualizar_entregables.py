from pathlib import Path
import shutil,subprocess,sys
from xml.etree import ElementTree as E
P=Path(__file__).resolve().parent.parent
GEN=P/'99_Generacion';TMP=GEN/'salida_temporal'
for script in ['generar_plan_detallado.py','generar_edt_arbol.py']:
 subprocess.run([sys.executable,str(GEN/script)],check=True)
# Fuentes independientes y una fuente conjunta: la versión completa y las 13 secciones.
sect=E.parse(TMP/'EDT_Seccionada.drawio').getroot();sect.remove(sect.findall('diagram')[0])
E.ElementTree(sect).write(P/'01_EDT/03_Editables/EDT_Seccionada.drawio',encoding='utf-8',xml_declaration=True)
whole=E.parse(TMP/'EDT_Completa.drawio').getroot()
E.ElementTree(whole).write(P/'01_EDT/03_Editables/EDT_Completa.drawio',encoding='utf-8',xml_declaration=True)
for d in sect.findall('diagram'):whole.append(d)
E.ElementTree(whole).write(P/'01_EDT/03_Editables/EDT_Completa_y_Seccionada.drawio',encoding='utf-8',xml_declaration=True)
mapping={'EDT_Proyecto_Completo.svg':'01_EDT/01_Completa/EDT_Completa.svg','Gantt_D2_56_meses.svg':'02_Gantt/01_Graficos/Gantt_Completa_M01-M56.svg','Gantt_D2_implementacion.svg':'02_Gantt/01_Graficos/Gantt_Implementacion_M01-M24.svg','Gantt_D2.mmd':'02_Gantt/02_Editables/Gantt_Completa_M01-M56.mmd','Gantt_Implementacion_D2.mmd':'02_Gantt/02_Editables/Gantt_Implementacion_M01-M24.mmd','Diccionario_EDT_D2.csv':'03_Apoyo/Diccionario_EDT.csv','Red_actividades_T15.csv':'03_Apoyo/Red_Actividades_y_Holguras.csv','plan_detallado.json':'99_Generacion/plan_detallado.json'}
slugs=['Gestion_del_proyecto','Levantamiento_y_diseno','Plataforma','Equipo_a_bordo','Servicios_Etapa_1','Integraciones','Datos_y_migracion','Servicios_Etapa_2','Adhesion_de_transportistas','Calidad_y_pruebas','Implantacion','Innovaciones','Operacion']
for i,slug in enumerate(slugs,1):mapping[f'EDT_{i:02}_detalle.svg']=f'01_EDT/02_Seccionada/EDT_{i:02}_{slug}.svg'
for src,dst in mapping.items():shutil.copy2(TMP/src,P/dst)
portal=(TMP/'EDT_Gantt_Proyecto_Completo.html').read_text(encoding='utf-8')
portal=portal.replace('EDT_00_completa.svg','01_EDT/01_Completa/EDT_Completa.svg')
for src,dst in mapping.items():portal=portal.replace(src,dst)
portal=portal.replace('href="EDT_D2.drawio"','href="01_EDT/03_Editables/EDT_Completa_y_Seccionada.drawio"')
portal=portal.replace('Fuente diagrams.net','EDT completa y seccionada en diagrams.net')
portal=portal.replace('<h2 id="edt">','<p><a href="00_LEEME_ENTREGABLES.md">Guía de archivos</a> · <a href="01_EDT/01_Completa/EDT_Completa.svg">Árbol completo en tamaño original</a> · <a href="01_EDT/03_Editables/EDT_Seccionada.drawio">EDT seccionada editable</a></p><h2 id="edt">')
(P/'00_ABRIR_ENTREGABLES.html').write_text(portal,encoding='utf-8')
# Las salidas temporales se mantienen como material de generación, no como entregables.
print('Portal actualizado; EDT completa, 13 secciones y 3 fuentes draw.io publicadas localmente.')
