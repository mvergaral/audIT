#!/usr/bin/env bash
# Exporta el informe maestro a PDF con la nomenclatura oficial de las Indicaciones §2.
set -euo pipefail
cd "$(dirname "$0")/.."
SALIDA="10 - AUDIT - TI-12.pdf"

pandoc INFORME-MAESTRO.md \
  --pdf-engine=xelatex \
  --from=markdown+pipe_tables+tex_math_dollars+raw_tex \
  --toc --toc-depth=2 \
  -V documentclass=article \
  -V papersize=letter \
  -V geometry:"margin=2.2cm" \
  -V fontsize=10pt \
  -V lang=es \
  -V mainfont="DejaVu Serif" \
  -V monofont="DejaVu Sans Mono" \
  -V monofontoptions="Scale=0.82" \
  -V colorlinks=true -V linkcolor=black -V urlcolor=black \
  -H build/preambulo.tex \
  -B build/portada.tex \
  -o "$SALIDA"

echo "Generado: $SALIDA"
command -v pdfinfo >/dev/null && pdfinfo "$SALIDA" | grep -E '^(Pages|File size)'
