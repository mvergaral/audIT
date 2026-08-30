#!/usr/bin/env bash
# OCR de PDFs escaneados, con eliminación de marca de agua.
#
#   1. Si el PDF ya trae capa de texto -> pdftotext, sin OCR.
#   2. Si no, se renderiza a PNG con pdftoppm y se procesa página por página,
#      repartiendo las páginas entre todos los núcleos.
#
# Dos modos de salida:
#   texto plano (por defecto)  rápido; una llamada a tesseract por página.
#   markdown (-m)              conserva tablas, títulos, viñetas y párrafos;
#                              delega en tools/page_to_md.py.
#
# La marca de agua se elimina binarizando por el CANAL MÍNIMO de RGB en vez del
# gris de luminancia: "CONFIDENCIAL" es gris neutro claro y desaparece, mientras
# que los títulos dorados tienen el canal azul casi negro y sobreviven. Con un
# gris normal el umbral se llevaría los títulos junto con el sello.

set -euo pipefail

DPI=300
LANG_T=spa
THRESH="60%"
JOBS=$(nproc)
PSM=3
OUTDIR=texto
WORKDIR=.ocr_work
KEEP=0
FORCE_OCR=0
MARKDOWN=0
HERE=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)

usage() {
  cat <<EOF
Uso: $0 [opciones] archivo.pdf [archivo2.pdf ...]

  -m        salida Markdown con tablas reconstruidas (def: texto plano)
  -o DIR    directorio de salida            (def: $OUTDIR)
  -l LANG   idioma tesseract                (def: $LANG_T; ej: spa+eng)
  -r DPI    resolución de render            (def: $DPI)
  -t UMBRAL umbral de binarización, solo modo texto plano (def: $THRESH)
  -p PSM    modo de segmentación, solo modo texto plano   (def: $PSM)
  -j N      trabajos en paralelo            (def: $JOBS)
  -k        conservar imágenes intermedias en $WORKDIR
  -f        forzar OCR aunque el PDF tenga capa de texto

Requisitos:  sudo pacman -S tesseract-data-spa poppler imagemagick
El modo -m añade: sudo pacman -S python-numpy python-pillow
EOF
  exit 1
}

while getopts "mo:l:r:t:p:j:kfh" opt; do
  case $opt in
    m) MARKDOWN=1 ;;
    o) OUTDIR=$OPTARG ;;
    l) LANG_T=$OPTARG ;;
    r) DPI=$OPTARG ;;
    t) THRESH=$OPTARG ;;
    p) PSM=$OPTARG ;;
    j) JOBS=$OPTARG ;;
    k) KEEP=1 ;;
    f) FORCE_OCR=1 ;;
    *) usage ;;
  esac
done
shift $((OPTIND - 1))
[ $# -ge 1 ] || usage

for bin in pdftoppm pdftotext pdfinfo magick tesseract; do
  command -v "$bin" >/dev/null || { echo "falta '$bin' en el PATH" >&2; exit 1; }
done

if ! tesseract --list-langs 2>/dev/null | grep -qx "${LANG_T%%+*}"; then
  echo "tesseract no tiene el idioma '${LANG_T%%+*}'." >&2
  echo "  sudo pacman -S tesseract-data-${LANG_T%%+*}" >&2
  exit 1
fi

EXT=txt
if [ "$MARKDOWN" -eq 1 ]; then
  EXT=md
  PYTHON=${PYTHON:-python3}
  if ! "$PYTHON" -c "import numpy, PIL" 2>/dev/null; then
    echo "el modo -m necesita numpy y pillow para \$PYTHON ($PYTHON)." >&2
    echo "  sudo pacman -S python-numpy python-pillow" >&2
    exit 1
  fi
  export PYTHON HERE
fi

mkdir -p "$OUTDIR"

# --- una página, modo texto plano --------------------------------------------
ocr_page() {
  local png=$1 base=${1%.png}
  [ -s "$base.txt" ] && return 0                    # reanudable
  magick "$png" -colorspace sRGB \
      -channel RGB -separate -evaluate-sequence min \
      -threshold "$2" "$base.clean.png"
  tesseract "$base.clean.png" "$base" -l "$3" --oem 1 --psm "$4" 2>/dev/null
  rm -f "$base.clean.png"
}

# --- una página, modo markdown -----------------------------------------------
md_page() {
  local png=$1 base=${1%.png}
  [ -s "$base.md" ] && return 0
  "$PYTHON" "$HERE/page_to_md.py" "$png" "$2" > "$base.md.part" && mv "$base.md.part" "$base.md"
}
export -f ocr_page md_page

for pdf in "$@"; do
  [ -f "$pdf" ] || { echo "no existe: $pdf" >&2; continue; }
  name=$(basename "$pdf" .pdf)
  slug=$(echo "$name" | tr -cs '[:alnum:]' '_' | sed 's/_*$//')
  out="$OUTDIR/$slug.$EXT"
  pages=$(pdfinfo "$pdf" | awk '/^Pages:/{print $2}')

  chars=$(pdftotext -f 1 -l 3 "$pdf" - 2>/dev/null | tr -d '[:space:]' | wc -c)
  if [ "$FORCE_OCR" -eq 0 ] && [ "$chars" -gt 200 ]; then
    echo ">> $name ($pages pág.) — ya trae capa de texto, se extrae sin OCR"
    pdftotext -layout "$pdf" "$OUTDIR/$slug.txt"
    echo "   -> $OUTDIR/$slug.txt"
    continue
  fi

  echo ">> $name ($pages pág.) — ${DPI}dpi, $JOBS procesos, idioma $LANG_T, salida .$EXT"
  wd="$WORKDIR/$slug"
  mkdir -p "$wd"

  # pdftoppm es monohilo: se reparten rangos de páginas entre los procesos.
  chunk=$(( (pages + JOBS - 1) / JOBS )); [ "$chunk" -lt 1 ] && chunk=1
  seq 1 "$chunk" "$pages" | xargs -P "$JOBS" -I{} sh -c '
      end=$(( {} + '"$chunk"' - 1 )); [ $end -gt '"$pages"' ] && end='"$pages"'
      pdftoppm -r '"$DPI"' -f {} -l $end -png "$1" "$2/p" 2>/dev/null
    ' _ "$pdf" "$wd"

  if [ "$MARKDOWN" -eq 1 ]; then
    find "$wd" -name 'p-*.png' -print0 \
      | xargs -0 -P "$JOBS" -I{} bash -c 'md_page "$1" "$2"' _ {} "$LANG_T"
  else
    find "$wd" -name 'p-*.png' -print0 \
      | xargs -0 -P "$JOBS" -I{} bash -c 'ocr_page "$1" "$2" "$3" "$4"' _ {} "$THRESH" "$LANG_T" "$PSM"
  fi

  # Ensamblado en orden de página, con marcador citable por número de página.
  : > "$out"
  find "$wd" -name "p-*.$EXT" | sort -V | while read -r f; do
    n=$(basename "$f" ".$EXT"); n=${n#p-}; n=$((10#$n))
    if [ "$MARKDOWN" -eq 1 ]; then
      # page_to_md deja en la primera línea el número impreso en el pie, que es
      # el que se cita; el del PDF va aparte porque no coinciden.
      imp=$(head -1 "$f" | sed -n 's/^<!--pag:\(.*\)-->$/\1/p')
      [ -n "$imp" ] || imp="? / $pages"
      printf '\n<!-- ===== página %s · PDF %d ===== -->\n\n' "$imp" "$n" >> "$out"
      tail -n +2 "$f" >> "$out"
      continue
    else
      printf '\n\n===== [%s] página %d/%s =====\n\n' "$name" "$n" "$pages" >> "$out"
    fi
    cat "$f" >> "$out"
  done

  words=$(wc -w < "$out")
  echo "   -> $out ($words palabras, ~$((words * 4 / 3)) tokens aprox.)"
  [ "$KEEP" -eq 1 ] || rm -rf "$wd"
done

rmdir "$WORKDIR" 2>/dev/null || true
echo "listo."
