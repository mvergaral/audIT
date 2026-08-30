#!/usr/bin/env python3
"""Índice de búsqueda sobre el texto extraído de las bases.

Por qué SQLite FTS5 y no una base vectorial: el corpus son ~94k tokens de texto
contractual, donde se busca por término exacto ("boleta de garantía", "multa",
"Artículo 45"). BM25 sobre secciones acierta más que la similitud semántica en
ese material, no necesita modelo de embeddings ni dependencias — sqlite3 y FTS5
vienen en la biblioteca estándar — y el índice se reconstruye en un segundo.

La unidad de recuperación es la SECCIÓN (un artículo, un capítulo, una subsección),
no la página ni el documento: es el trozo más chico que se sostiene solo y que se
puede citar. Una consulta devuelve unos cientos de tokens en vez de los 30k que
pesa un documento entero.

Uso:
    ./tools/buscar.py "boleta de garantía"      buscar (todos los términos)
    ./tools/buscar.py -o multa sanción          buscar (cualquier término)
    ./tools/buscar.py -f FEP02 "observabilidad" limitar a un documento
    ./tools/buscar.py -v 137                    ver una sección completa
    ./tools/buscar.py -v A:45                   ver el Artículo 45
    ./tools/buscar.py -l                        listar el índice
    ./tools/buscar.py -r                        reconstruir el índice
"""

import argparse
import os
import re
import sqlite3
import sys
import unicodedata
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
TEXTO = RAIZ / "texto"
DB = TEXTO / "secciones.db"
MAPA = TEXTO / "INDICE.md"

PAGINA = re.compile(r"<!-- ===== página (\d+) ?/ ?(\d+) · PDF (\d+) ===== -->")
TITULO_MD = re.compile(r"^(#{2,3})\s+(.*\S)\s*$")
TITULO_TXT = re.compile(r"^(\d+)\.\s+([A-ZÁÉÍÓÚÑ].*\S)\s*$")

ARTICULO = re.compile(r"^ART[ÍI]CULO\s+(\d+)°?\.?\s*(.*)$", re.I)
CAPITULO = re.compile(r"^CAP[ÍI]TULO\s+(\d+)\s*(.*)$", re.I)
NUMERADA = re.compile(r"^(\d+(?:\.\d+)+)\s+(.*)$")
FORMULARIO = re.compile(r"^FORMULARIO\s+([\w-]+)\s*(.*)$", re.I)


def clasificar(titulo):
    """Devuelve (tipo, número, título limpio) para un encabezado."""
    for rx, tipo in ((ARTICULO, "artículo"), (CAPITULO, "capítulo"),
                     (FORMULARIO, "formulario"), (NUMERADA, "sección")):
        m = rx.match(titulo)
        if m:
            return tipo, m.group(1), (m.group(2) or "").strip(" .-–—·")
    return "título", "", titulo


def corto(nombre):
    """Nombre corto y citable del documento a partir del archivo."""
    base = nombre.split(".")[0]
    if base.startswith("FEP"):
        return base.split("_")[0]
    return base.split("_")[0][:12]


def secciones(path):
    """Parte un documento en secciones, siguiendo sus encabezados."""
    md = path.suffix == ".md"
    pagina, cur = 1, None
    for linea in path.read_text().split("\n"):
        m = PAGINA.match(linea)
        if m:
            pagina = int(m.group(1))       # la impresa, que es la que se cita
            continue
        t = TITULO_MD.match(linea) if md else TITULO_TXT.match(linea)
        if t:
            if cur:
                yield cur
            titulo = t.group(2) if md else f"{t.group(1)}. {t.group(2)}"
            tipo, num, limpio = clasificar(titulo)
            cur = {"doc": corto(path.name), "archivo": path.name, "pagina": pagina,
                   "tipo": tipo, "num": num, "titulo": limpio or titulo,
                   "encabezado": titulo, "lineas": []}
        elif cur is not None:
            cur["lineas"].append(linea)
    if cur:
        yield cur


def leer():
    """Todas las secciones del corpus, en orden de documento y página."""
    filas = []
    fuentes = [q for q in sorted(TEXTO.glob("*.md")) + sorted(TEXTO.glob("*.txt"))
               if q != MAPA]                       # el mapa no se indexa a sí mismo
    for p in fuentes:
        for s in secciones(p):
            texto = "\n".join(s["lineas"]).strip()
            filas.append((s["doc"], s["archivo"], s["pagina"], s["tipo"],
                          s["num"], s["titulo"], texto, s["encabezado"]))
    return filas


def indexar(filas):
    """Arma el índice FTS5 en memoria.

    El índice no se guarda en disco. Construirlo entero cuesta 0,16 s, así que no
    compensa persistirlo: obliga a controlar si quedó desactualizado, y sobre todo
    deja un archivo que muchos visores de SQLite no pueden abrir, porque vienen
    compilados sin el módulo fts5 y fallan al leer la tabla virtual.
    """
    con = sqlite3.connect(":memory:")
    con.execute("""create virtual table sec using fts5(
        doc UNINDEXED, archivo UNINDEXED, pagina UNINDEXED, tipo UNINDEXED,
        num UNINDEXED, titulo, texto,
        tokenize="unicode61 remove_diacritics 2")""")
    con.executemany("insert into sec(doc,archivo,pagina,tipo,num,titulo,texto) "
                    "values (?,?,?,?,?,?,?)", [f[:7] for f in filas])
    return con


def exportar(filas):
    """Escribe los dos artefactos consultables a mano.

    `secciones.db` son tablas normales, sin nada virtual, para poder abrirlo en
    cualquier visor. `INDICE.md` es el listado navegable.
    """
    if DB.exists():
        DB.unlink()
    con = sqlite3.connect(DB)
    con.execute("""create table seccion(
        id integer primary key, doc text, archivo text, pagina integer,
        tipo text, num text, titulo text, encabezado text, palabras integer,
        texto text)""")
    con.executemany(
        "insert into seccion values (?,?,?,?,?,?,?,?,?,?)",
        [(i, f[0], f[1], f[2], f[3], f[4], f[5], f[7], len(f[6].split()), f[6])
         for i, f in enumerate(filas, start=1)])
    con.execute("create index i_tipo on seccion(tipo, num)")
    con.execute("create index i_doc on seccion(doc, pagina)")
    con.commit()
    con.close()

    lineas = [f"# Índice del corpus\n",
              f"{len(filas)} secciones. Generado por `tools/buscar.py -r`.\n",
              "Para el detalle de una sección: `./tools/buscar.py -v <id>`.\n"]
    doc = None
    for i, f in enumerate(filas, start=1):
        if f[0] != doc:
            doc = f[0]
            lineas.append(f"\n## {doc} — `{f[1]}`\n")
        peso = len(f[6].split())
        lineas.append(f"- `{i:4d}` p.{f[2]:<3} **{f[7]}** — {peso} palabras")
    MAPA.write_text("\n".join(lineas) + "\n")


def exportes_al_dia():
    """¿Los artefactos en disco reflejan los textos actuales?"""
    if not (DB.exists() and MAPA.exists()):
        return False
    t = min(DB.stat().st_mtime, MAPA.stat().st_mtime)
    return all(p.stat().st_mtime <= t
               for p in list(TEXTO.glob("*.md")) + list(TEXTO.glob("*.txt"))
               if p != MAPA)


def consulta_fts(terminos, cualquiera, frase):
    """Arma la consulta FTS5 escapando cada término.

    Por defecto un argumento con espacios se parte en palabras: quien escribe
    `buscar.py "conductores subcontratados"` casi siempre quiere las dos palabras
    en la misma sección, no esa secuencia literal. Para lo segundo está --frase.
    """
    if frase:
        return " AND ".join('"' + t.replace('"', "") + '"' for t in terminos)
    palabras = [w for t in terminos for w in t.split()]
    partes = ['"' + w.replace('"', "") + '"' for w in palabras]
    return (" OR " if cualquiera else " AND ").join(partes)


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("terminos", nargs="*")
    ap.add_argument("-p", "--frase", action="store_true",
                    help="buscar la secuencia literal de palabras")
    ap.add_argument("-o", "--cualquiera", action="store_true",
                    help="basta con que aparezca uno de los términos")
    ap.add_argument("-f", "--doc", help="limitar a un documento (FEP01, FEP02, …)")
    ap.add_argument("-t", "--tipo", help="limitar a un tipo (artículo, capítulo, …)")
    ap.add_argument("-n", "--num", type=int, default=8, help="máximo de resultados")
    ap.add_argument("-v", "--ver", help="mostrar una sección: su id, o A:45 / C:3")
    ap.add_argument("-l", "--listar", action="store_true",
                    help="mapa por capítulos (barato: ~1k tokens)")
    ap.add_argument("-L", "--listar-todo", action="store_true",
                    help="listado completo de las 377 secciones")
    ap.add_argument("-r", "--reindexar", action="store_true",
                    help="reescribir secciones.db e INDICE.md")
    a = ap.parse_args()

    filas = leer()
    if a.reindexar or not exportes_al_dia():
        exportar(filas)
        print(f"[{len(filas)} secciones -> {DB.name}, {MAPA.name}]", file=sys.stderr)
        if a.reindexar and not (a.terminos or a.ver or a.listar or a.listar_todo):
            return
    con = indexar(filas)

    if a.ver:
        m = re.match(r"^([AaCcSs]):(.+)$", a.ver)
        if m:
            tipo = {"a": "artículo", "c": "capítulo", "s": "sección"}[m.group(1).lower()]
            q = ("select rowid,doc,pagina,tipo,num,titulo,texto from sec "
                 "where tipo=? and num=?")
            args = (tipo, m.group(2))
        else:
            q = "select rowid,doc,pagina,tipo,num,titulo,texto from sec where rowid=?"
            args = (a.ver,)
        filas = con.execute(q, args).fetchall()
        if not filas:
            sys.exit(f"sin resultados para {a.ver!r}")
        for r in filas:
            print(f"[{r[1]} p.{r[2]} · {r[3]} {r[4]} · id {r[0]}] {r[5]}\n")
            print(r[6])
        return

    if a.listar or a.listar_todo:
        # El mapa por capítulos es lo que conviene cargar para orientarse: el
        # listado completo pesa seis veces más y casi nunca hace falta entero.
        q = ("select rowid,doc,pagina,tipo,num,titulo from sec"
             + ("" if a.listar_todo else
                " where tipo in ('capítulo','formulario')") + " order by rowid")
        doc = None
        for r in con.execute(q):
            if r[1] != doc:
                doc = r[1]
                print(f"\n## {doc}")
            etq = f"{r[3][:3]}{r[4]}".strip()
            print(f"  {r[0]:4d} p.{r[2]:<3} {etq:<8} {r[5]}")
        return

    if not a.terminos:
        ap.print_help()
        return

    where = ["sec match ?"]
    args = [consulta_fts(a.terminos, a.cualquiera, a.frase)]
    if a.doc:
        where.append("doc = ?")
        args.append(a.doc)
    if a.tipo:
        where.append("tipo = ?")
        args.append(a.tipo)
    args.append(a.num)

    q = (f"select rowid, doc, pagina, tipo, num, titulo, "
         f"snippet(sec, 6, '«', '»', ' … ', 14), bm25(sec, 0,0,0,0,0, 5.0, 1.0) "
         f"from sec where {' and '.join(where)} order by 8 limit ?")
    filas = con.execute(q, args).fetchall()
    if not filas:
        print("sin resultados")
        return
    for r in filas:
        etq = f"{r[3]} {r[4]}".strip() if r[4] else r[3]
        print(f"\n[{r[1]} p.{r[2]} · {etq} · id {r[0]}] {r[5]}")
        print(f"   {' '.join(r[6].split())}")
    print(f"\n({len(filas)} de {a.num} máx. — detalle: ./tools/buscar.py -v <id>)")


if __name__ == "__main__":
    main()
