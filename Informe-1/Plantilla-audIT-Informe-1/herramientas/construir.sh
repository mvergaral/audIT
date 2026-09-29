#!/usr/bin/env bash
# Compila uno, varios o todos los subdocumentos.
#   ./herramientas/construir.sh              todos los que tengan contenido
#   ./herramientas/construir.sh 04 13        solo esos
#   ./herramientas/construir.sh --limpiar    borra archivos intermedios
set -u
TEXINPUTS=${TEXINPUTS:-}
BIBINPUTS=${BIBINPUTS:-}
cd "$(dirname "$0")/.." || exit 1
RAIZ=$(pwd)
mkdir -p salida

# la clase, los estilos y la bibliografia viven en comun/
export TEXINPUTS="$RAIZ/comun:$RAIZ:$TEXINPUTS"
export BIBINPUTS="$RAIZ/comun:$BIBINPUTS"
export TEXMFOUTPUT="$RAIZ/salida"

if [ "${1:-}" = "--limpiar" ]; then
  rm -rf salida/aux; echo "intermedios borrados"; exit 0
fi

mapfile -t TODOS < <(ls -d subdocumentos/*/ | sed 's#subdocumentos/##; s#/##')
if [ $# -gt 0 ]; then
  SEL=(); for a in "$@"; do
    for d in "${TODOS[@]}"; do [[ "$d" == "$a"* ]] && SEL+=("$d"); done
  done
else
  SEL=("${TODOS[@]}")
fi

ok=0; fail=0
for d in "${SEL[@]}"; do
  ruta="subdocumentos/$d"
  num=$(sed -n 's/.*elNumero}{\([0-9]*\)}.*/\1/p' "$ruta/meta.tex")
  aux="salida/aux/$d"; mkdir -p "$aux"
  latexmk -pdf -interaction=nonstopmode -halt-on-error \
    -outdir="$aux" -jobname="sub$num" \
    -pretex="\\def\\subdocRuta{$ruta}" -usepretex \
    "$ruta/main.tex" > "$aux/build.log" 2>&1
  if [ -f "$aux/sub$num.pdf" ]; then
    dest="salida/${d%%-*}-audIT-Subdoc$(printf %02d "$num").pdf"
    canon="salida/INFORME1_AUDIT_SUBDOC$(printf %02d "$num")_20260907.pdf"
    cp "$aux/sub$num.pdf" "$dest"
    cp "$aux/sub$num.pdf" "$canon"
    printf "  ok    %-22s %2s pags -> %s\n" "$d" \
      "$(pdfinfo "$dest" | awk '/^Pages/{print $2}')" "$(basename "$dest")"
    ok=$((ok+1))
  else
    printf "  FALLA %-22s ver %s\n" "$d" "$aux/build.log"
    grep -m2 -A2 "^!" "$aux/build.log" | sed 's/^/        /'
    fail=$((fail+1))
  fi
done
echo "  ─────────────────────────────"
printf "  %s compilados, %s con error\n" "$ok" "$fail"

# Generar archivo ZIP canónico según Art. 50.3
if [ $ok -gt 0 ]; then
  (
    cd salida || exit 1
    python3 -c '
import glob, zipfile
canons = sorted(glob.glob("INFORME1_AUDIT_SUBDOC*_20260907.pdf"))
if canons:
    with zipfile.ZipFile("INFORME1_AUDIT_20260907.ZIP", "w", zipfile.ZIP_DEFLATED) as zf:
        for f in canons:
            zf.write(f)
    print(f"  ok    archivo zip generado: salida/INFORME1_AUDIT_20260907.ZIP ({len(canons)} subdocumentos)")
'
  )
fi

# Los .md se regeneran siempre desde el mismo contenido.tex, para que nunca
# queden desfasados respecto de los PDF.
echo ""
echo "  Markdown"
python3 herramientas/tex2md.py

