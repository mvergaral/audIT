#!/usr/bin/env python3
"""Genera las figuras y las comprueba.

  herramientas/.venv/bin/python fuente/generar.py [nombre ...]

Por cada figura escribe SVG, PDF y PNG, revisa con pdffonts que la letra
incrustada sea IBM Plex Sans y mide la letra con herramientas/letra_diagramas.py.
"""
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lienzo  # noqa: E402
import rutas  # noqa: E402
import s4_fisica  # noqa: E402
import s4_logica  # noqa: E402
import s7  # noqa: E402
import s13  # noqa: E402
import propuestas  # noqa: E402
import s4_copias_d3  # noqa: E402
import fisica_completa  # noqa: E402

FORMATO = rutas.FORMATO
PY = sys.executable
MODULOS = [s4_fisica, fisica_completa, s4_logica, s4_copias_d3, s13, s7, propuestas]


def medida_svg(base):
    """Ancho y alto impresos del SVG, en mm."""
    cab = open(base + ".svg", encoding="utf-8").read(400)
    m = re.search(r'width="([\d.]+)mm" height="([\d.]+)mm"', cab)
    return m.group(1), m.group(2)


def comprobar(base, tipo):
    fuentes = subprocess.run(["pdffonts", base + ".pdf"], capture_output=True, text=True).stdout
    nombres = {l.split()[0].split("+")[-1] for l in fuentes.splitlines()[2:] if l.strip()}
    otras = [n for n in nombres if not n.startswith("IBMPlexSans")]
    medida = {"V": ["148.9", "200"], "H": ["257.4", "167"]}.get(tipo) or list(medida_svg(base))
    letra = subprocess.run([PY, os.path.join(FORMATO, "herramientas/letra_diagramas.py"), base + ".svg"] + medida,
                           capture_output=True, text=True, cwd=FORMATO).stdout.strip()
    return sorted(nombres), otras, letra


def main():
    pedidas = set(sys.argv[1:])
    for m in MODULOS:
        for fn in m.FIGURAS:
            if pedidas and fn.__name__ not in pedidas:
                continue
            base = fn()
            ancho_mm = medida_svg(base)[0]
            tipo = {"257.4": "H", "148.9": "V"}.get(ancho_mm, "L")
            nombres, otras, letra = comprobar(base, tipo)
            print(f"{os.path.relpath(base, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))} [{tipo}]")
            print("   fuentes:", ", ".join(nombres), "  OTRAS: " + ", ".join(otras) if otras else "")
            print("   " + letra.replace("\n", "\n   "))
            rev = lienzo.REVISION.get(os.path.basename(base), [])
            if rev:
                print("   líneas sobre:", "; ".join(rev))
            if os.path.exists(base + "-oficio.svg"):
                _, _, letra = comprobar(base + "-oficio", "L")
                print("   oficio apaisado: " + letra.replace("\n", "\n   "))


if __name__ == "__main__":
    main()
