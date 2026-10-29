#!/usr/bin/env bash
# Publica la presentación en GitHub Pages (rama gh-pages del repositorio audIT).
# Sólo sube lo que el navegador necesita; generador, guion y notas no se publican.
# Uso: ./publicar.sh ["mensaje del commit"]
set -euo pipefail

AQUI="$(cd "$(dirname "$0")" && pwd)"
if [ -e "$AQUI/../.git" ]; then REPO="$AQUI/.."; else REPO="$AQUI/../audIT"; fi
MENSAJE="${1:-Actualiza la presentación de la Revisión 2}"
TMP="$(mktemp -d)"
trap 'git -C "$REPO" worktree remove --force "$TMP" >/dev/null 2>&1 || true; rm -rf "$TMP"' EXIT

python3 "$AQUI/construir.py"
git -C "$REPO" fetch -q origin gh-pages
git -C "$REPO" worktree add -q --force "$TMP" gh-pages
git -C "$TMP" reset -q --hard origin/gh-pages

find "$TMP" -mindepth 1 -maxdepth 1 ! -name .git -exec rm -rf {} +
cp "$AQUI/index.html" "$AQUI/harness.js" "$TMP/"
cp -r "$AQUI/composition" "$AQUI/assets" "$TMP/"
touch "$TMP/.nojekyll"

git -C "$TMP" add -A
if git -C "$TMP" diff --cached --quiet; then
  echo "Sin cambios que publicar."
  exit 0
fi
git -C "$TMP" commit -q -m "$MENSAJE"
git -C "$TMP" push -q origin HEAD:gh-pages
echo "Publicado. En uno o dos minutos se verá en https://mvergaral.github.io/audIT/"
