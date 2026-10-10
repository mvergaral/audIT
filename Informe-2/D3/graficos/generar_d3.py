#!/usr/bin/env python3
"""Generador y auditor de figuras oficiales de Dupla 3 (lienzo.py).

Genera las 13 figuras vectoriales en SVG, PDF y PNG a 300 DPI:
  - Subdocumento 4.1: 4-3-asignacion, 4-4-documento, 4-6-liquidacion
  - Subdocumento 5: 5-2-custodia, 5-3-permisos, 5-3-cap, 5-4-cdc, 5-5-migracion, 5-6-desempeno, 5-2-mdm, 5-1-erd
  - Subdocumento 6: 6-1-hitos, 6-2-pipeline

Valida tipografía oficial (IBM Plex Sans >= 9 pt) y sincroniza automáticamente:
  1. Informe-2/D3/figuras/ (para los documentos markdown)
  2. recursos/Formato-Oferta-audIT/figuras/ (para compilación LaTeX)
"""
import os
import shutil
import subprocess
import sys

# Asegurar importación de módulos locales
AQUI = os.path.dirname(os.path.abspath(__file__))
if AQUI not in sys.path:
    sys.path.insert(0, AQUI)

import s4_secuencias  # noqa: E402
import s5_datos  # noqa: E402
import s6_metodologias  # noqa: E402
from comun import BASE_DIR, SALIDA_D3_FIGURAS, FORMATO_FIGURAS  # noqa: E402

MODULOS = [s4_secuencias, s5_datos, s6_metodologias]
HERRAMIENTA_LETRA = os.path.join(BASE_DIR, "recursos/Formato-Oferta-audIT/herramientas/letra_diagramas.py")


def comprobar_figura(base_path, tipo="V"):
    """Audita fuentes incrustadas con pdffonts y tamaños con letra_diagramas.py."""
    pdf_path = base_path + ".pdf"
    svg_path = base_path + ".svg"

    # 1. Comprobar fuentes en el PDF
    fuentes_out = subprocess.run(["pdffonts", pdf_path], capture_output=True, text=True).stdout
    nombres = {line.split()[0].split("+")[-1] for line in fuentes_out.splitlines()[2:] if line.strip()}
    otras = [n for n in nombres if not n.startswith("IBMPlexSans")]

    # 2. Medir tamaños de tipografía en SVG
    medida = ["148.9", "200"] if tipo == "V" else ["257.4", "167"]
    letra_proc = subprocess.run(["python3", HERRAMIENTA_LETRA, svg_path] + medida,
                                capture_output=True, text=True)
    letra_res = letra_proc.stdout.strip() or letra_proc.stderr.strip()

    return sorted(nombres), otras, letra_res


def main():
    pedidas = set(sys.argv[1:])
    os.makedirs(SALIDA_D3_FIGURAS, exist_ok=True)

    print("=" * 70)
    print(" GENERADOR VECTORIAL OFICIAL DE FIGURAS DUPLA 3 (audIT)")
    print("=" * 70)

    total_generadas = 0

    for mod in MODULOS:
        nombre_mod = mod.__name__
        print(f"\n>>> Procesando módulo: {nombre_mod}")

        for fn in mod.FIGURAS:
            nombre_fn = fn.__name__
            if pedidas and nombre_fn not in pedidas and not any(p in nombre_fn for p in pedidas):
                continue

            # Genera la figura en D4/graficos-v2/<carpeta>/<nombre>
            base_generada = fn()
            nombre_archivo = os.path.basename(base_generada)
            carpeta_subdoc = os.path.basename(os.path.dirname(base_generada))

            tipo = "H" if 'width="257.4mm"' in open(base_generada + ".svg").read(300) else "V"

            # Destinos de sincronización
            dest_d3 = os.path.join(SALIDA_D3_FIGURAS, nombre_archivo + ".png")
            dest_formato_dir = os.path.join(FORMATO_FIGURAS, carpeta_subdoc)
            os.makedirs(dest_formato_dir, exist_ok=True)

            # Sincronizar archivos .svg, .pdf y .png
            for ext in [".svg", ".pdf", ".png"]:
                origen = base_generada + ext
                if os.path.exists(origen):
                    # Copiar a LaTeX
                    shutil.copy2(origen, os.path.join(dest_formato_dir, nombre_archivo + ext))
                    # Copiar PNG a D3/figuras/
                    if ext == ".png":
                        shutil.copy2(origen, dest_d3)

            # Comprobar calidad técnica
            fuentes, otras, letra_info = comprobar_figura(base_generada, tipo)

            alerta_fuente = f" [¡AVISO! Fuentes no IBM: {', '.join(otras)}]" if otras else ""
            print(f"  [OK] {nombre_archivo} [{tipo}]{alerta_fuente}")
            print(f"       Fuentes: {', '.join(fuentes)}")
            print(f"       Auditoría: {letra_info}")
            total_generadas += 1

    print("\n" + "=" * 70)
    print(f" Proceso finalizado exitosamente. Total figuras generadas: {total_generadas}")
    print(f" Sincronizado en:")
    print(f"   • {SALIDA_D3_FIGURAS}")
    print(f"   • {FORMATO_FIGURAS}")
    print("=" * 70)


if __name__ == "__main__":
    main()
