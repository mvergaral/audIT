#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Genera los diagramas del Subdocumento 5 directamente en PNG con fondo blanco (#FFFFFF)
y con todo el texto y tipografía renderizados por el motor oficial de Mermaid.
"""

import os
import glob
import base64
import urllib.request

OUT_DIR = os.path.dirname(os.path.abspath(__file__))

def main():
    print(f"Generando PNGs con texto completo en: {OUT_DIR}")
    mmd_files = sorted(glob.glob(os.path.join(OUT_DIR, "*.mmd")))
    generated_pngs = []

    for mmd in mmd_files:
        base_name = os.path.splitext(os.path.basename(mmd))[0]
        png_path = os.path.join(OUT_DIR, f"{base_name}.png")
        print(f"\n--- Procesando: {base_name} ---")
        
        with open(mmd, "r", encoding="utf-8") as f:
            code = f.read()

        enc = base64.b64encode(code.encode("utf-8")).decode("ascii")
        url = f"https://mermaid.ink/img/{enc}?bgColor=FFFFFF&type=png"
        
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        try:
            with urllib.request.urlopen(req, timeout=25) as resp:
                data = resp.read()
            with open(png_path, "wb") as f:
                f.write(data)
            print(f"  [OK] PNG generado con texto ({len(data)} bytes, {resp.headers.get('content-type')})")
            generated_pngs.append(png_path)
        except Exception as e:
            print(f"  [ERROR] Fallo al descargar PNG para {base_name}: {e}")

    print(f"\n==========================================")
    print(f"Se actualizaron exitosamente {len(generated_pngs)} diagramas PNG.")
    print(f"==========================================")

if __name__ == "__main__":
    main()
