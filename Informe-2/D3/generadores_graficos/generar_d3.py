#!/usr/bin/env python3
"""Regenera sólo D3/graficos. Conserva PNG 300 dpi y SVG editable.
No escribe en D4 ni en la plantilla de LaTeX.
"""
import json
import re
import sys
from pathlib import Path
import subprocess
from tempfile import TemporaryDirectory
import xml.etree.ElementTree as ET
import s4_secuencias,s5_datos,s6_metodologias,s4_capas,s4_documento,s13_proceso,s13_cartera
from comun import SALIDA_D3_GRAFICOS,BASE_DIR,REVISION
MODULOS=[s4_secuencias,s5_datos,s6_metodologias,s4_capas,s4_documento,s13_proceso,s13_cartera]

def main():
    pedidas=set(sys.argv[1:]); resultados=[]
    for mod in MODULOS:
        for fn in mod.FIGURAS:
            if pedidas and not any(p in fn.__name__ for p in pedidas): continue
            base=Path(fn())
            svg=Path(str(base)+'.svg')
            # El PDF para inspeccionar fuentes existe sólo durante esta comprobación.
            with TemporaryDirectory(prefix='audit-d3-fuentes-') as temporal:
                pdf=Path(temporal)/'grafico.pdf'
                subprocess.run(['rsvg-convert','-f','pdf','-o',str(pdf),str(svg)],check=True)
                fuentes=subprocess.run(['pdffonts',str(pdf)],check=True,capture_output=True,text=True).stdout
            nombres={s.split()[0].split('+')[-1] for s in fuentes.splitlines()[2:] if s.strip()}
            if any(not s.startswith('IBMPlexSans') for s in nombres): raise RuntimeError(f'Fuente incorrecta: {base.name}: {nombres}')
            lienzo=ET.parse(svg).getroot()
            ancho=lienzo.attrib['width'].removesuffix('mm')
            alto=lienzo.attrib['height'].removesuffix('mm')
            medicion=subprocess.run([sys.executable,str(BASE_DIR/'recursos/Formato-Oferta-audIT/herramientas/letra_diagramas.py'),str(svg),ancho,alto],capture_output=True,text=True,check=True)
            resumen=re.search(r'= ([\d.]+) pt;.*?; (\d+) pares de etiquetas chocan, (\d+) salen del lienzo',medicion.stdout)
            if not resumen or float(resumen[1])<9 or int(resumen[2]) or int(resumen[3]):
                raise RuntimeError(f'Revisar legibilidad de {base.name}: {medicion.stdout}')
            resultados.append({'figura':base.name,'fuentes':sorted(nombres),'medicion':medicion.stdout.strip(),'lineas_sobre_elementos':REVISION.get(base.name,[])})
            print(base.name,medicion.stdout.strip(),flush=True)
    registro=Path(__file__).with_name('verificacion.json')
    if pedidas and registro.exists():
        anteriores={r['figura']:r for r in json.loads(registro.read_text())}
        anteriores.update({r['figura']:r for r in resultados})
        registro.write_text(json.dumps(list(anteriores.values()),ensure_ascii=False,indent=2)+'\n')
    else:
        registro.write_text(json.dumps(resultados,ensure_ascii=False,indent=2)+'\n')
    print(f'{len(resultados)} gráficos generados exclusivamente en {SALIDA_D3_GRAFICOS}')
if __name__=='__main__': main()
