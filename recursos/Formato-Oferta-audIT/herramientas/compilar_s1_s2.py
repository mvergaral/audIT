#!/usr/bin/env python3
"""Compila S1, S2, T-6 y sus anexos independientes sin cambiar otros subdocumentos."""
import os
from pathlib import Path
import shutil
import subprocess
import sys

AQUI=Path(__file__).resolve().parent
sys.path.insert(0,str(AQUI))
import compilar
from comun import leer_json, guardar_json

def main():
    base=Path(compilar.RAIZ)
    (base/'salida/aux/cache').mkdir(parents=True,exist_ok=True)
    os.environ['TEXMFCACHE']='salida/aux/cache'
    destino=base/'salida/informe2'
    archivo=destino/'manifiesto.json'
    previo=leer_json(str(archivo),{}) or {}
    resultado=subprocess.run([sys.executable,str(AQUI/'compilar.py'),'subdocs','01','02','-j','1','--forzar'],cwd=base)
    if resultado.returncode:return resultado.returncode
    manifiesto=leer_json(str(archivo),{})
    afectados={'01','02','01T-6','01A','02A'}
    manifiesto['archivos'] += [a for a in previo.get('archivos',[]) if a['clave'] not in afectados]
    for n,carpeta in [(1,'01-empresa'),(2,'02-problema')]:
        nombre=f'AUDIT-Subdocumento{n}-Anexos'
        tarea=compilar.Trabajo(f'{n:02d}A','anexo.tex',nombre,str(base/'salida/aux/informe2'/f'{n:02d}A'),compilar.OFERTA.preambulo()+r'\def\NumeroSubdoc{%d}'%n,[f'subdocumentos/{carpeta}'])
        tarea.compilar(True)
        if not tarea.ok:
            print('No se pudo compilar',nombre,'Ver:',Path(tarea.log).parent/'compilacion.txt')
            return 1
        shutil.copy2(tarea.pdf,destino/(nombre+'.pdf'))
        manifiesto['archivos'].append({'clave':tarea.clave,'nombre':nombre+'.pdf','folio_inicial':1,'paginas':tarea.paginas,'aux':str(Path(tarea.aux).relative_to(base)),'log':str(Path(tarea.log).relative_to(base)),'fuentes':[['subdocumentos'],tarea.carpetas]})
        print('OK',nombre,tarea.paginas,'páginas',flush=True)
    guardar_json(str(archivo),manifiesto)
    revision=dict(manifiesto)
    revision['archivos']=[a for a in manifiesto['archivos'] if a['clave'] in afectados]
    guardar_json(str(destino/'manifiesto-s1-s2.json'),revision)
    return 0

if __name__=='__main__':sys.exit(main())
