#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Qué pasa con un diagrama si toda su letra sube a 9 pt en el área donde se
imprime (FEP01, Artículo 40.4).

  python3 herramientas/letra_diagramas.py DIAGRAMA.svg ANCHO_MM ALTO_MM

Áreas: figura vertical 148,9 mm de ancho (alto 0,82 del texto, 196,9 mm) y
anexo horizontal en modo pagina 257,4 por 167 mm. Agranda cada texto por el
mismo factor sin moverlo, mide su ancho con las métricas de IBM Plex e informa
qué etiquetas chocan, cuáles salen del lienzo y qué parte del lienzo ocuparía
el texto. Sirve para decidir si un diagrama cabe redistribuyendo o si hay que
sacar algo, decisión que es del equipo.
"""
import html
import itertools
import os
import re
import sys

try:
    import pymupdf
except ImportError:
    venv = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".venv", "bin", "python")
    os.execv(venv, [venv] + sys.argv)
PLEX="/usr/share/texmf-dist/fonts/opentype/ibm/plex/"
F={("sans",False):pymupdf.Font(fontfile=PLEX+"IBMPlexSans-Regular.otf"),
   ("sans",True):pymupdf.Font(fontfile=PLEX+"IBMPlexSans-SemiBold.otf"),
   ("mono",False):pymupdf.Font(fontfile=PLEX+"IBMPlexMono-Regular.otf"),("mono",True):pymupdf.Font(fontfile=PLEX+"IBMPlexMono-Regular.otf")}
MM=72/25.4
def analizar(svg, ancho_mm, alto_mm):
    t=open(svg,encoding="utf-8").read()
    vb=[float(x) for x in re.search(r'viewBox="([^"]+)"',t).group(1).split()]
    W,H=vb[2],vb[3]
    unidad=min(ancho_mm*MM/W, alto_mm*MM/H)       # pt por unidad del lienzo
    textos=[]
    for m in re.finditer(r'<text([^>]*)>(.*?)</text>',t,re.S):
        a=m.group(1); s=html.unescape(re.sub(r"<[^>]+>","",m.group(2))).strip()
        if not s: continue
        g=lambda k,d=None:(re.search(k+r'="([^"]*)"',a) or [None,d])[1]
        x,y,fs=float(g("x",0)),float(g("y",0)),float(g("font-size",10))
        fam="mono" if "Mono" in (g("font-family","") or "") else "sans"
        b=(g("font-weight","400") or "400") in ("600","700","bold")
        textos.append(dict(s=s,x=x,y=y,fs=fs,anc=g("text-anchor","start"),f=F[(fam,b)]))
    minfs=min(x["fs"] for x in textos)
    k=9/(minfs*unidad)
    cajas=[]
    for x in textos:
        fs=x["fs"]*k; w=x["f"].text_length(x["s"],fontsize=fs)
        x0={"start":x["x"],"middle":x["x"]-w/2,"end":x["x"]-w}[x["anc"]]
        cajas.append((x0,x["y"]-0.75*fs,x0+w,x["y"]+0.22*fs,x["s"]))
    choques=[(a[4],b[4]) for a,b in itertools.combinations(cajas,2)
             if a[0]<b[2] and b[0]<a[2] and a[1]<b[3] and b[1]<a[3]]
    fuera=[c[4] for c in cajas if c[0]<0 or c[2]>W or c[1]<0 or c[3]>H]
    area=sum((c[2]-c[0])*(c[3]-c[1]) for c in cajas)
    print(f"{svg.split('/')[-1]}: {len(textos)} textos, letra mínima {minfs} u = {minfs*unidad:.2f} pt; "
          f"para 9 pt toda la letra x{k:.2f}; {len(choques)} pares de etiquetas chocan, {len(fuera)} salen del lienzo; "
          f"el texto ocuparía {100*area/(W*H):.0f} % del lienzo")
    for a,b in choques: print(f"   «{a}» con «{b}»")
    for x in fuera: print(f"   fuera del lienzo: «{x}»")


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print(__doc__)
        sys.exit(2)
    analizar(sys.argv[1], float(sys.argv[2]), float(sys.argv[3]))
