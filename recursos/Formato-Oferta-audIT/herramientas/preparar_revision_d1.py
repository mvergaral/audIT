#!/usr/bin/env python3
"""Paquete local de revisión D1: PDF seleccionados, sin archivos de trabajo."""
import json
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED

RAIZ = Path(__file__).resolve().parents[1]
CLAVES = {'00', '01', '02', '09', '13', '01T-6', '09T-13', '09T-17', '13T-19', '01A', '02A'}

def preparar(destino):
    salida = RAIZ / 'salida/informe2'
    datos = json.loads((salida / 'manifiesto.json').read_text())
    elegidos = {f['clave']: salida / f['nombre'] for f in datos['archivos'] if f['clave'] in CLAVES}
    if set(elegidos) != CLAVES:
        raise ValueError('Faltan PDF D1 en el manifiesto de compilación')
    archivos = list(elegidos.values()) + [salida / 'Tabla-Art46-Informe2.pdf']
    for archivo in archivos:
        if archivo.suffix.lower() != '.pdf' or not archivo.is_file():
            raise ValueError('Archivo PDF faltante o de formato distinto')
    if len({p.name for p in archivos}) != len(archivos):
        raise ValueError('Nombre de PDF duplicado')
    destino = Path(destino)
    destino.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(destino, 'w', ZIP_DEFLATED) as paquete:
        for archivo in archivos:
            paquete.write(archivo, archivo.name)
    with ZipFile(destino) as paquete:
        assert len(paquete.namelist()) == len(archivos)
        assert all(nombre.endswith('.pdf') for nombre in paquete.namelist())
    return archivos

if __name__ == '__main__':
    import sys
    destino = sys.argv[1] if len(sys.argv) > 1 else RAIZ / 'salida/Revision-D1-Informe2.zip'
    archivos = preparar(destino)
    print(f'Paquete local de revisión: {len(archivos)} PDF. No publica ni envía archivos.')
