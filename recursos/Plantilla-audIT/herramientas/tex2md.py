# -*- coding: utf-8 -*-
"""Convierte las secciones .tex del informe a un unico Markdown."""
import re, os

CITAS = {
 "bases_admin_2026": "Escuela de Informática PUCV, 2026a",
 "bases_transversales_2026": "Escuela de Informática PUCV, 2026b",
 "bases_caso10_2026": "Escuela de Informática PUCV, 2026c",
 "codigo_trabajo_25bis": "Ministerio del Trabajo, 2003",
 "res_ex_1213_2009": "Dirección del Trabajo, 2009",
 "ley21719": "Ministerio de Hacienda, 2024",
 "ley20123": "Ministerio del Trabajo, 2006",
 "ds298": "Ministerio de Transportes, 1995",
 "fms_standard_2025": "FMS Standard, 2025",
 "iridium_sbd": "Iridium Communications, 2024",
 "webfleet_sat": "Webfleet Solutions, 2025",
 "azure_regions": "Microsoft, 2025",
 "iso42010": "ISO, 2022", "iso22301": "ISO, 2019", "iso27031": "ISO, 2011",
 "glec2023": "Smart Freight Centre, 2023", "iso14083": "ISO, 2023", "ley21663": "Congreso Nacional de Chile, 2024", "nfpa2001": "NFPA, 2022", "nist80088": "NIST, 2014",
}

def limpia(t):
    t = re.sub(r"\\parencite\{([^}]+)\}", lambda m: "(" + CITAS.get(m.group(1), m.group(1)) + ")", t)
    t = t.replace("\\textordmasculine{}", "º").replace("\\textordmasculine", "º")
    t = t.replace("\\textbar{}", "|").replace("\\,", " ")
    t = re.sub(r"\\textbf\{([^{}]*)\}", r"**\1**", t)
    t = re.sub(r"\\emph\{([^{}]*)\}", r"*\1*", t)
    t = re.sub(r"\\leyendaFont\{([^{}]*)\}", r"\1", t)
    t = t.replace("\\midrule", "").replace("\\toprule", "").replace("\\bottomrule", "")
    t = t.replace("\\%", "%").replace("\\&", "&").replace("\\_", "_").replace("\\#", "#")
    t = re.sub(r"\\label\{[^}]*\}", "", t)
    t = re.sub(r"\\ref\{[^}]*\}", "", t)
    return t

def tabla(bloque, cap):
    filas = [f.strip() for f in bloque.split("\\\\") if f.strip()]
    out = []
    for i, f in enumerate(filas):
        celdas = [c.strip() for c in f.split("&")]
        out.append("| " + " | ".join(celdas) + " |")
        if i == 0:
            out.append("|" + "---|" * len(celdas))
    return ["", f"**Tabla. {cap}**", ""] + out + [""]

def convierte(path):
    t = open(path, encoding="utf-8").read()
    t = limpia(t)
    out, i = [], 0
    lineas = t.split("\n")
    while i < len(lineas):
        ln = lineas[i]
        m = re.match(r"\\(sub)*section\*?\{(.*)\}", ln)
        if m:
            lvl = 2 + (ln.count("subsection") + (1 if "subsubsection" in ln else 0))
            lvl = {"\\section": 2, "\\section*": 2, "\\subsection": 3, "\\subsection*": 3,
                   "\\subsubsection": 4}.get(ln.split("{")[0], 3)
            out.append("\n" + "#" * lvl + " " + m.group(2) + "\n"); i += 1; continue
        if ln.startswith("\\begin{tablaAudit}"):
            cap = re.match(r"\\begin\{tablaAudit\}\{([^}]*)\}", ln).group(1)
            buf = []; i += 1
            while i < len(lineas) and not lineas[i].startswith("\\end{tablaAudit}"):
                buf.append(lineas[i]); i += 1
            i += 1; out += tabla("\n".join(buf), cap); continue
        if ln.startswith("\\figuraAncha"):
            m2 = re.match(r"\\figuraAncha\{([^}]*)\}\{([^}]*)\}", ln)
            out.append(f"\n![{m2.group(2)}]({m2.group(1)})\n\n*Figura. {m2.group(2)}*\n"); i += 1; continue
        if ln.strip() in ("\\begin{enumerate}", "\\begin{itemize}", "\\end{enumerate}", "\\end{itemize}"):
            out.append(""); i += 1; continue
        if ln.strip().startswith("\\item"):
            out.append("- " + ln.strip()[5:].strip()); i += 1; continue
        if ln.startswith("\\") or ln.strip().startswith("%"):
            i += 1; continue
        out.append(ln); i += 1
    return "\n".join(out)



import glob, os, sys, re as _re

RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
os.chdir(RAIZ)

def leer_meta(d):
    t = open(os.path.join(d, "meta.tex"), encoding="utf-8").read()
    g = lambda k: _re.search(r"\\newcommand\{\\%s\}\{(.*)\}" % k, t).group(1)
    return g("elNumero"), g("elTitulo"), g("laDescripcion")

def leer_instancia():
    t = open("comun/instancia.tex", encoding="utf-8").read()
    g = lambda k: _re.search(r"\\newcommand\{\\%s\}\{(.*)\}" % k, t).group(1)
    lim = lambda x: x.replace("\\textordmasculine{}", "º").replace("\\,", " ")
    return {k: lim(g(k)) for k in
            ("laEmpresa","elNumeroEmpresa","elProyecto","elCliente",
             "laLicitacion","laInstancia","laVersion","laFecha","elLugar")}

BIB = open("comun/bibliografia.md", encoding="utf-8").read() if os.path.exists("comun/bibliografia.md") else ""

ins = leer_instancia()
sel = sys.argv[1:]
carpetas = sorted(glob.glob("subdocumentos/*/"))
if sel:
    carpetas = [c for c in carpetas if any(os.path.basename(c.rstrip("/")).startswith(a) for a in sel)]

os.makedirs("salida", exist_ok=True)
for c in carpetas:
    d = c.rstrip("/")
    num, tit, desc = leer_meta(d)
    enc = f"""# {tit}

**Subdocumento N.º {num}**

| | |
|---|---|
| Empresa | {ins['laEmpresa']}, Empresa N.º {ins['elNumeroEmpresa']} |
| Licitación | {ins['laLicitacion']} |
| Proyecto | {ins['elProyecto']} |
| Cliente | {ins['elCliente']} |
| Instancia | {ins['laInstancia']} |
| Contenido | {desc} |
| Versión | {ins['laVersion']} |
| Fecha | {ins['laFecha']} |
| Lugar | {ins['elLugar']} |

---
"""
    cuerpo = convierte(os.path.join(d, "contenido.tex"))
    txt = _re.sub(r"\n{4,}", "\n\n\n", enc + cuerpo + BIB)
    pref = os.path.basename(d).split("-")[0]
    salida = f"salida/{pref}-audIT-Subdoc{int(num):02d}.md"
    open(salida, "w", encoding="utf-8").write(txt)
    print(f"  {salida:42s} {len(txt.split()):>6} palabras")
