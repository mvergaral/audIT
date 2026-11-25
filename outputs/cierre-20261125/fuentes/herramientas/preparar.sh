#!/usr/bin/env bash
# Prepara el entorno de las herramientas: un entorno virtual de Python con
# PyMuPDF, que mide el tamaño real de cada fragmento de texto del PDF y abre
# los DOCX para compararlos, y openpyxl, que lee y escribe la planilla del
# modelo financiero. Se corre una vez. No toca el Python del sistema.
set -e
cd "$(dirname "$0")"
python3 -m venv .venv
./.venv/bin/pip install --quiet --upgrade pip
./.venv/bin/pip install --quiet pymupdf openpyxl
./.venv/bin/python -c "import pymupdf, openpyxl; print('PyMuPDF', pymupdf.__version__, 'y openpyxl', openpyxl.__version__, 'listos')"
