#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Trae un contenido.tex del formato anterior (Plantilla-audIT o Entrega) al
formato nuevo, con los cambios que no se pueden resolver con macros.

  python3 herramientas/migrar.py ORIGEN.tex NN            deja el resultado en
                                                        salida/migracion/
  python3 herramientas/migrar.py ORIGEN.tex NN --escribir lo escribe en
                                                        subdocumentos/NN-.../
  Opción --figuras DIR copia las figuras citadas desde DIR a figuras/NN-.../

Qué cambia:
  - Quita el primer \\section{...}: en el formato anterior era el título del
    capítulo. Ahora la apertura del subdocumento sale sola del catálogo.
  - Sube cada título un nivel: \\subsection pasa a \\section y
    \\subsubsection a \\subsection. Los \\section* y \\subsection* de anexos
    pasan a títulos numerados y se borra su \\addcontentsline.
  - Cambia las rutas assets/images/ por figuras/NN-carpeta/.
  - Agrega un resumenApertura con marcadores si el archivo no lo trae.
Qué deja igual, porque la capa de compatibilidad lo resuelve:
  \\figuraAncha, el entorno tablaAudit, \\leyendaFont y \\parencite.
Qué informa para revisar a mano:
  - \\parencite a las bases (bases_admin_2026 y otras): hay que pasarlas a
    \\art, \\caso o \\transv con artículo y página.
  - Títulos seguidos directamente de una tabla o figura.
  - Leyendas de tabla o figura y títulos que nombran un «Formulario T-NN».
    Los formularios reales los imprime formularios/ al final del
    subdocumento. Una tabla del contenido con ese nombre no es el formulario
    (la revisión del Informe 1 lo objetó en el Anexo A del Subdocumento 4) y
    hay que cambiarle la leyenda.
"""
import os
import re
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from comun import RAIZ, SALIDA, Config  # noqa: E402

TITULO = re.compile(r"^\s*\\(section|subsection|subsubsection|paragraph)\*?\{")
OBJETO = re.compile(r"^\s*\\(begin\{(tabla|tablaAudit|figure)\}|figura|figuraAncha|anexoGrafico)")
# Títulos, tablas y figuras: la línea que los abre lleva el rótulo
NIVELES = ("section", "subsection", "subsubsection", "paragraph")
ROTULO = re.compile(r"\\(section|subsection|subsubsection|paragraph|caption|figuraAncha|figura|anexoGrafico"
                    r"|begin\{tablaAudit\}|begin\{tabla\})(?![A-Za-z])\*?(.*)")


def migrar(texto, carpeta):
    avisos = []
    lineas = texto.split("\n")
    # 1. el primer \section sin asterisco era el capítulo
    for i, l in enumerate(lineas):
        m = re.match(r"^\s*\\section\{(.*)\}\s*$", l)
        if m:
            avisos.append(f"línea {i + 1}: se quitó el título de capítulo «{m.group(1)}»")
            lineas[i] = ""
            break
    t = "\n".join(lineas)
    # 2. niveles de título, con marcas intermedias para no pisar reemplazos
    t = re.sub(r"\\addcontentsline\{toc\}\{[a-z]+\}\{[^\n]*\}\s*\n", "", t)
    t = re.sub(r"\\section\*\{", "@@NIVEL1@@{", t)
    t = re.sub(r"\\subsection\*\{", "@@NIVEL2@@{", t)
    t = re.sub(r"\\subsubsection\{", "@@NIVEL2@@{", t)
    t = re.sub(r"\\subsection\{", "@@NIVEL1@@{", t)
    t = re.sub(r"\\section\{", "@@NIVEL1@@{", t)
    t = t.replace("@@NIVEL1@@", "\\section").replace("@@NIVEL2@@", "\\subsection")
    # 3. rutas de figuras
    figuras = sorted(set(re.findall(r"assets/images/([\w.\-]+)", t)))
    t = t.replace("assets/images/", f"figuras/{carpeta}/")
    # 4. resumen de apertura
    if "resumenApertura" not in t:
        t = ("\\begin{resumenApertura}\n\\marcador{Qué resuelve este subdocumento, en cuatro o "
             "cinco líneas}\n\\begin{recibe}\n  \\item \\marcador{Qué recibe el mandante}\n"
             "\\end{recibe}\n\\end{resumenApertura}\n\n" + t.lstrip("\n"))
        avisos.append("se agregó un resumenApertura con marcadores al inicio")
    # 5. revisiones a mano
    for i, l in enumerate(t.split("\n"), 1):
        for m in re.finditer(r"\\parencite\{(bases_[^}]*)\}", l):
            avisos.append(f"línea {i}: cita a las bases sin página ({m.group(1)}): usar \\art, \\caso o \\transv")
        if "Escuela de Inform" in l:
            avisos.append(f"línea {i}: menciona a la Escuela")
    for i, l in enumerate(t.split("\n"), 1):
        m = ROTULO.search(l)
        if m:
            n = re.search(r"Formulario[\s~]+(T-\d+)", m.group(2))
            if n:
                que = "el título" if m.group(1) in NIVELES else "la leyenda"
                avisos.append(f"línea {i}: {que} «{m.group(2).strip()[:60]}» nombra el Formulario "
                              f"{n.group(1)}, pero esto no es el formulario: el real lo imprime "
                              "formularios/. Cambiar el rótulo por lo que muestra")
    lin = t.split("\n")
    for i, l in enumerate(lin):
        if TITULO.match(l):
            j = i + 1
            while j < len(lin) and (not lin[j].strip() or lin[j].strip().startswith(("\\label", "%"))):
                j += 1
            if j < len(lin) and OBJETO.match(lin[j]):
                avisos.append(f"línea {i + 1}: título seguido directamente de {lin[j].strip()[:30]}, "
                              "falta el párrafo de contexto")
    return t, figuras, avisos


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if len(args) < 2:
        print(__doc__)
        return 2
    origen, numero = args[0], int(args[1])
    cfg = Config()
    carpeta = cfg.subdocs[numero]["carpeta"]
    t, figuras, avisos = migrar(open(origen, encoding="utf-8").read(), carpeta)
    if "--escribir" in sys.argv:
        destino = os.path.join(RAIZ, "subdocumentos", carpeta, "contenido.tex")
        actual = open(destino, encoding="utf-8").read() if os.path.exists(destino) else ""
        propio = re.sub(r"\\marcador\{[^}]*\}|\\(section|subsection|label|begin|end|item)\b[^\n]*|%[^\n]*",
                        "", actual)
        if propio.strip() and "--forzar" not in sys.argv:
            print(f"{destino} ya tiene contenido propio. Usar --forzar para reemplazarlo.")
            return 1
    else:
        destino = os.path.join(SALIDA, "migracion", carpeta, "contenido.tex")
    os.makedirs(os.path.dirname(destino), exist_ok=True)
    open(destino, "w", encoding="utf-8").write(t)
    print(f"escrito {os.path.relpath(destino, RAIZ)}")
    if "--figuras" in sys.argv:
        src = sys.argv[sys.argv.index("--figuras") + 1]
        dst = os.path.join(RAIZ, "figuras", carpeta)
        os.makedirs(dst, exist_ok=True)
        for f in figuras:
            if os.path.exists(os.path.join(src, f)):
                shutil.copy(os.path.join(src, f), dst)
                print(f"  figura copiada: {f}")
    elif figuras:
        print(f"  figuras citadas, copiar a figuras/{carpeta}/: {', '.join(figuras)}")
    for a in avisos:
        print("  revisar: " + a)
    return 0


if __name__ == "__main__":
    sys.exit(main())
