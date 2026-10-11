#!/usr/bin/env python3
"""Compila D3 con el formato oficial y su bibliografía adicional local.

Desde cualquier carpeta: python3 <ruta de este archivo> [04 05 06 13]
S3 se compila como dependencia cuando lo necesitan los enlaces de S13.
Las imágenes se leen de Informe-2/D3/graficos; no se duplican.
"""
from pathlib import Path
import os
import sys
import tempfile

OFERTA = Path(__file__).resolve().parents[2]
cache = Path(tempfile.gettempdir()) / 'audit-texlive-d3'
cache.mkdir(parents=True, exist_ok=True)
os.environ.setdefault('TEXMFVAR', str(cache))
os.environ.setdefault('TEXMFCACHE', str(cache))
sys.path.insert(0, str(OFERTA / 'herramientas'))
import compilar

compilar.OFERTA.bib = 'subdocumentos/04-arquitectura/referencias-d3.bib'
numeros = sys.argv[1:] or ['04', '05', '06', '13']
seleccion = set(numeros)
if seleccion & {'06', '13'}:
    seleccion.update({'03', '04', '13'})
numeros = sorted(seleccion, key=int)
sys.argv = [sys.argv[0], 'subdocs', *numeros, '-j', '2']
if __name__ == '__main__':
    raise SystemExit(compilar.main())
