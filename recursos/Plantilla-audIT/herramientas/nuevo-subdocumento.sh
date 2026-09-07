#!/usr/bin/env bash
# Crea una carpeta de subdocumento nueva a partir de la plantilla.
#   ./herramientas/nuevo-subdocumento.sh 15-anexo "Anexo Tecnico" "Sub. 15 Anexo" "Descripcion breve."
set -eu
cd "$(dirname "$0")/.."
[ $# -eq 4 ] || { echo "uso: $0 <carpeta> <titulo> <corto> <descripcion>"; exit 1; }
CARPETA=$1; TITULO=$2; CORTO=$3; DESC=$4
NUM=${CARPETA%%-*}; NUM=$((10#$NUM))
d="subdocumentos/$CARPETA"
[ -d "$d" ] && { echo "ya existe $d"; exit 1; }
mkdir -p "$d"
cat > "$d/meta.tex" <<META
\newcommand{\elNumero}{$NUM}
\newcommand{\elTitulo}{$TITULO}
\newcommand{\elCorto}{$CORTO}
\newcommand{\laDescripcion}{$DESC}
META
cp subdocumentos/01-empresa/main.tex "$d/main.tex"
cat > "$d/contenido.tex" <<CONT
\section{$TITULO}

\subsection{Primera sección}

Contenido pendiente.
CONT
echo "creado $d"
