"""Entrada compatible: genera la versión revisada del anexo Gantt."""
from pathlib import Path
import runpy
runpy.run_path(str(Path(__file__).with_name("generar_gantt_revisada.py")), run_name="__main__")
