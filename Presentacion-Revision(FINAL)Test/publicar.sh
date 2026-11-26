#!/usr/bin/env bash
# Publica la presentación en GitHub Pages (rama gh-pages del repositorio audIT).
# Sólo sube lo que el navegador necesita; generador, guion y notas no se publican.
# Uso: ./publicar.sh ["mensaje del commit"]
set -euo pipefail

AQUI="$(cd "$(dirname "$0")" && pwd)"
if [ -e "$AQUI/../.git" ]; then REPO="$AQUI/.."; else REPO="$AQUI/../audIT"; fi
MENSAJE="${1:-Actualiza la presentación de la propuesta final}"

python3 "$AQUI/construir.py"
git -C "$REPO" fetch -q origin refs/heads/gh-pages:refs/remotes/origin/gh-pages

TMP="$(mktemp -d)"
PAGINAS="$TMP/gh-pages"
limpiar() {
  git -C "$REPO" worktree remove --force -- "$PAGINAS" >/dev/null 2>&1 || true
  rmdir -- "$TMP" 2>/dev/null || true
}
trap limpiar EXIT
git -C "$REPO" worktree add -q --detach "$PAGINAS" refs/remotes/origin/gh-pages

# Renueva los recursos de la portada y conserva las demás rutas de Pages.
git -C "$PAGINAS" rm -rq --ignore-unmatch -- assets composition
cp -- "$AQUI/index.html" "$AQUI/harness.js" "$PAGINAS/"
cp -R -- "$AQUI/composition" "$AQUI/assets" "$PAGINAS/"
touch "$PAGINAS/.nojekyll"

git -C "$PAGINAS" add -A -- .nojekyll assets composition harness.js index.html
if git -C "$PAGINAS" diff --cached --quiet; then
  echo "Sin cambios que publicar."
  exit 0
fi
git -C "$PAGINAS" commit -q -m "$MENSAJE"
git -C "$PAGINAS" push -q origin HEAD:refs/heads/gh-pages
echo "Cambios enviados a GitHub Pages. La publicación se verá en https://mvergaral.github.io/audIT/"
