#!/usr/bin/env python3
"""Genera las figuras y las comprueba.

  herramientas/.venv/bin/python fuente/generar.py [nombre ...]

Por cada figura escribe SVG, PDF y PNG, revisa con pdffonts que la letra
incrustada sea IBM Plex Sans y mide la letra con herramientas/letra_diagramas.py.
"""
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lienzo  # noqa: E402
import s4_fisica  # noqa: E402
import s4_logica  # noqa: E402
import s7  # noqa: E402
import s13  # noqa: E402
import propuestas  # noqa: E402

FORMATO = "/mnt/NuevoVol/FEP/Formato-Oferta-audIT"
PY = os.path.join(FORMATO, "herramientas/.venv/bin/python")
MODULOS = [s4_fisica, s4_logica, s13, s7, propuestas]


def comprobar(base, tipo):
    fuentes = subprocess.run(["pdffonts", base + ".pdf"], capture_output=True, text=True).stdout
    nombres = {l.split()[0].split("+")[-1] for l in fuentes.splitlines()[2:] if l.strip()}
    otras = [n for n in nombres if not n.startswith("IBMPlexSans")]
    medida = ["148.9", "200"] if tipo == "V" else ["257.4", "167"]
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
            tipo = "H" if 'width="257.4mm"' in open(base + ".svg").read(300) else "V"
            nombres, otras, letra = comprobar(base, tipo)
            print(f"{os.path.relpath(base, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))} [{tipo}]")
            print("   fuentes:", ", ".join(nombres), "  OTRAS: " + ", ".join(otras) if otras else "")
            print("   " + letra.replace("\n", "\n   "))
            rev = lienzo.REVISION.get(os.path.basename(base), [])
            if rev:
                print("   líneas sobre:", "; ".join(rev))


if __name__ == "__main__":
    main()
