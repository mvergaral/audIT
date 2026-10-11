"""Rutas de los guiones de D4, para que corran igual desde la carpeta local de D4
(/mnt/NuevoVol/FEP/D4) y desde el repositorio (<repo>/Informe-2/D4).

AUDIT_REPO y AUDIT_FORMATO permiten fijarlas a mano.
"""
import os

AQUI = os.path.dirname(os.path.abspath(__file__))            # .../D4/graficos-v2/fuente
D4 = os.path.normpath(os.path.join(AQUI, "..", ".."))        # .../D4
_DENTRO = os.path.normpath(os.path.join(D4, "..", ".."))     # <repo> si D4 es <repo>/Informe-2/D4
EN_REPO = os.path.isdir(os.path.join(_DENTRO, "recursos", "Formato-Oferta-audIT"))

REPO = os.environ.get("AUDIT_REPO") or (_DENTRO if EN_REPO else "/mnt/NuevoVol/FEP/audIT")
# Desde el repositorio se escribe en su formato. Desde la carpeta local, en el formato local de D4.
FORMATO = os.environ.get("AUDIT_FORMATO") or (
    os.path.join(REPO, "recursos", "Formato-Oferta-audIT") if EN_REPO else "/mnt/NuevoVol/FEP/Formato-Oferta-audIT")
# El T-15 es de la dupla 2 y se lee siempre del repositorio.
T15 = os.path.join(REPO, "recursos", "Formato-Oferta-audIT", "subdocumentos", "07-plan-trabajo",
                   "formularios", "T-15.tex")
