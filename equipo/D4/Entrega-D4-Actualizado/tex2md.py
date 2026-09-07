# -*- coding: utf-8 -*-
"""Convierte las secciones .tex del informe a un unico Markdown."""
import re, os

CITAS = {
 "bases_admin_2026": "Escuela de Informática PUCV, 2026a",
 "bases_transversales_2026": "Escuela de Informática PUCV, 2026b",
 "bases_caso10_2026": "Escuela de Informática PUCV, 2026c",
 "codigo_trabajo_25bis": "Ministerio del Trabajo, 2003",
 "res_ex_1213_2009": "Dirección del Trabajo, 2009",
 "ley21719": "Congreso Nacional de Chile, 2024",
 "ley20123": "Ministerio del Trabajo, 2006",
 "ds298": "Ministerio de Transportes, 1995",
 "fms_standard_2025": "FMS Standard, 2025",
 "iridium_sbd": "Iridium Communications, 2024",
 "webfleet_sat": "Webfleet Solutions, 2025",
 "azure_regions": "Microsoft, 2025",
 "iso42010": "ISO, 2022", "iso22301": "ISO, 2019", "iso27031": "ISO, 2011",
  "cis_benchmarks": "Center for Internet Security, 2024",
 "ds158": "Ministerio de Obras Públicas, 1980",
 "ds43": "Ministerio de Salud, 2016",
 "iso9001": "ISO, 2015", "iso12207": "ISO, 2017", "iso16290": "ISO, 2013",
 "iso20000_1": "ISO, 2018", "iso27001": "ISO, 2022",
 "ley18290": "Ministerio de Transportes y Telecomunicaciones, 2009",
 "ley19799": "Congreso Nacional de Chile, 2002",
 "nist_csf2": "NIST, 2024", "nist_sp800_207": "NIST, 2020",
 "owasp_asvs": "OWASP, 2021",
 "w3c_vcdm2": "World Wide Web Consortium, 2025",
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


SUB = [
 ("1","contenido/c1.tex","Presentación de la Empresa",
  "Identificación, líneas de negocio, capacidad de intervención en terreno y acreditaciones."),
 ("2","contenido/c2.tex","Problema y Necesidad",
  "Comprensión del problema, dimensión de la operación, brechas de información y exigencias del cliente mayor."),
 ("3","contenido/c3.tex","Esquema de Solución y Alcance",
  "Decisiones estructurantes, catálogo de requisitos, alcance por etapas, plan de adhesión, consultas y contradicciones detectadas."),
 ("4","contenido/c4.tex","Arquitectura Lógica y Física",
  "Ocho capas, contextos delimitados, emplazamiento, dispositivo a bordo, dimensionamiento, supuestos y diagramas."),
 ("5","contenido/c5.tex","Modelo y Gestión de Datos",
  "Modelo de dominio, persistencia políglota, evidencia inalterable, retención, respaldo, migración y protección de datos personales."),
 ("13","contenido/c13.tex","Innovaciones",
  "Cartera de cinco innovaciones con su idea, la tecnología que la sustenta y el resultado esperado."),
]

BIB = """
## Bibliografía

Dirección del Trabajo. (2009). *Resolución Exenta N.º 1213. Sistema obligatorio de control de asistencia, horas de trabajo y descanso para conductores de vehículos de carga terrestre interurbana*.

Ministerio del Trabajo. (2003). *Decreto con Fuerza de Ley N.º 1. Texto refundido del Código del Trabajo. Artículo 25 bis*. Biblioteca del Congreso Nacional de Chile. https://www.bcn.cl/leychile/navegar?idNorma=207436

Escuela de Informática PUCV. (2026a). *Bases Administrativas. Licitación Pública Internacional N.º TFEP-01/2026* (FEP01.26).

Escuela de Informática PUCV. (2026b). *Bases Técnicas Transversales* (FEP02.26).

Escuela de Informática PUCV. (2026c). *Bases Técnicas del Caso 10. Transporte de Carga* (FEP03.10.26).

FMS Standard. (2025). *Technical Specification rFMS vehicle data version 5.0.0*. https://www.fms-standard.com

Iridium Communications. (2024). *Iridium Short Burst Data Service Developers Guide*.

ISO. (2011). *ISO/IEC 27031*. ISO. (2019). *ISO 22301*. ISO. (2022). *ISO/IEC/IEEE 42010*. ISO. (2023). *ISO 14083*.

Microsoft. (2025). *Azure geographies. Chile Central region*.

Ministerio de Hacienda. (2024). *Ley N.º 21.719 sobre protección y tratamiento de datos personales*.

Ministerio de Transportes. (1995). *Decreto Supremo N.º 298*.

Ministerio del Trabajo. (2006). *Ley N.º 20.123 sobre trabajo en régimen de subcontratación*.

NFPA. (2022). *NFPA 2001*. NIST. (2014). *NIST SP 800-88 Rev. 1*.

Smart Freight Centre. (2023). *GLEC Framework, version 3.0*.

Webfleet Solutions. (2025). *WEBFLEET SAT. Ficha técnica del producto*.
"""

for num, arch, titulo, desc in SUB:
    enc = f"""# {titulo}

**Subdocumento N.º {num}**

| | |
|---|---|
| Empresa | audIT, Empresa N.º 10 |
| Licitación | Licitación Pública Internacional N.º TFEP-01/2026, Caso 10 Transporte de Carga |
| Proyecto | Plataforma Digital de Misión Crítica para Transporte de Carga |
| Cliente | Transportes Curimón S.A. |
| Instancia | Informe Preparatorio 1, Oferta Técnica Sobre N.º 2 |
| Contenido | {desc} |
| Fecha | 7 de septiembre de 2026 |

---
"""
    cuerpo = convierte(arch)
    txt = re.sub(r"\n{4,}", "\n\n\n", enc + cuerpo + BIB)
    open(f"Subdoc{num}.md", "w", encoding="utf-8").write(txt)
    print(f"Subdoc{num}.md  {len(txt.split()):>6} palabras")
