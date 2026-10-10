"""Módulo base y utilidades comunes para diagramas de Dupla 3 (lienzo.py).

Configura rutas del proyecto, importa el framework vectorial de D4 y define
constantes tipográficas y estéticas conforme al estándar oficial de la oferta.
"""
import os
import sys

# Rutas del repositorio
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
D4_GRAFICOS = os.path.join(BASE_DIR, "Informe-2/D4/graficos-v2")
D4_FUENTE = os.path.join(D4_GRAFICOS, "fuente")

if D4_FUENTE not in sys.path:
    sys.path.insert(0, D4_FUENTE)

from lienzo import (  # noqa: E402
    Figura,
    ancho,
    ROJO,
    LINEA,
    BORDE,
    BORDE_AZ,
    BORDE_FICHA,
    SUBRED,
    GRIS_CLARO,
    GUION,
    FAMILIA,
    SALTO,
    REVISION,
)

# Carpetas de salida
SALIDA_D3_FIGURAS = os.path.join(BASE_DIR, "Informe-2/D3/figuras")
FORMATO_FIGURAS = os.path.join(BASE_DIR, "recursos/Formato-Oferta-audIT/figuras")

# Colores complementarios oficiales
VERDE_EXITO = "#1E824C"
AZUL_AUDIT = "#26C9FC"
AZUL_OSCURO = "#00A6ED"
GRIS_TEXTO = "#404040"
GRIS_FONDO_SECCION = "#F8F9FA"
AMARILLO_ALERTA = "#D4AC0D"
