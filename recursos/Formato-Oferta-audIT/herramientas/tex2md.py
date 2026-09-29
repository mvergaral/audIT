#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Equivalente en Markdown de cada subdocumento, desde el mismo contenido.tex.

  python3 herramientas/tex2md.py 04            imprime el Markdown del subdocumento 4
  python3 herramientas/compilar.py md [04 13]  lo escribe en salida/<instancia>/

Numera los títulos, las tablas y las figuras igual que el PDF (el número nace
del subdocumento), convierte las tablas del entorno tabla y tablaAudit en
tablas Markdown, y los dispositivos de venta, las citas a las bases y los
marcadores a texto. Los formularios se indican al final: su versión oficial es
la del PDF.

Documentos económicos (economico()): las cifras y las filas de las tablas de
montos no se calculan aquí. Se copian de <documento>.eco.json, que escribe
LuaLaTeX al compilar el PDF, y los números de tablas y secciones se toman del
.aux. Así el Markdown y el DOCX traen exactamente las cifras del PDF.
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from comun import RAIZ, Config  # noqa: E402


# ----------------------------------------------------------------------------
#  Lectura de argumentos con llaves anidadas
# ----------------------------------------------------------------------------
def arg(t, i):
    """Devuelve (contenido, índice siguiente) del argumento {..} que empieza en i."""
    while i < len(t) and t[i] in " \n\t":
        i += 1
    if i >= len(t) or t[i] != "{":
        return "", i
    nivel, j = 0, i
    while j < len(t):
        if t[j] == "\\":
            j += 2
            continue
        if t[j] == "{":
            nivel += 1
        elif t[j] == "}":
            nivel -= 1
            if nivel == 0:
                return t[i + 1:j], j + 1
        j += 1
    return t[i + 1:], len(t)


def opcional(t, i):
    while i < len(t) and t[i] in " \n\t":
        i += 1
    if i < len(t) and t[i] == "[":
        nivel, j = 0, i
        while j < len(t):
            if t[j] == "[":
                nivel += 1
            elif t[j] == "]":
                nivel -= 1
                if nivel == 0:
                    return t[i + 1:j], j + 1
            j += 1
    return None, i


def reemplazar(t, comando, n, funcion, estrella=False, opt=False):
    """Reemplaza \\comando[opt]{a1}..{an} por funcion(args)."""
    patron = re.compile(r"\\" + comando + (r"(\*?)" if estrella else r"()") + r"(?![a-zA-Z])")
    salida, pos = [], 0
    for m in patron.finditer(t):
        if m.start() < pos:
            continue
        i = m.end()
        o = None
        if opt:
            o, i = opcional(t, i)
        args = []
        for _ in range(n):
            a, i = arg(t, i)
            args.append(a)
        salida.append(t[pos:m.start()])
        salida.append(funcion(*args, estrella=bool(m.group(1)), opt=o))
        pos = i
    salida.append(t[pos:])
    return "".join(salida)


def claves(texto):
    """Pares clave = {valor} de una lista clave-valor de primer nivel."""
    res, i = {}, 0
    for m in re.finditer(r"(\w+)\s*=\s*", texto):
        if m.start() < i:
            continue
        j = m.end()
        if j < len(texto) and texto[j] == "{":
            v, j = arg(texto, j)
        else:
            k = texto.find(",", j)
            k = len(texto) if k < 0 else k
            v, j = texto[j:k].strip(), k
        res[m.group(1)] = v
        i = j
    return res


# ----------------------------------------------------------------------------
class Conversor:
    def __init__(self, cfg, numero, etiquetas=None, eco=None):
        self.cfg = cfg
        self.n = numero
        self.sec = [0, 0, 0]
        self.ntab = 0
        self.nfig = 0
        self.ncomp = 0
        self.ndec = 0
        # etiquetas del .aux, si las hay: mandan sobre la numeración propia
        self.aux = etiquetas or {}
        self.etiquetas = dict(self.aux)
        self.eco = eco
        self.bib = self.leer_bib()
        self.datos = self.leer_datos()

    def leer_bib(self):
        bib = {}
        for ruta in ("referencias/referencias.bib", "muestra/referencias-muestra.bib"):
            try:
                t = open(os.path.join(RAIZ, ruta), encoding="utf-8").read()
            except OSError:
                continue
            for m in re.finditer(r"@\w+\{([^,]+),(.*?)\n\}", t, re.S):
                cuerpo = m.group(2)
                a = re.search(r"author\s*=\s*\{+([^}]*)\}+", cuerpo)
                y = re.search(r"year\s*=\s*\{([^}]*)\}", cuerpo)
                bib[m.group(1).strip()] = ((a.group(1) if a else "s. a."), (y.group(1) if y else "s. f."))
        return bib

    def leer_datos(self):
        t = open(os.path.join(RAIZ, "configuracion/metadatos.tex"), encoding="utf-8").read()
        mapa = {"Empresa": "empresa", "Cliente": "cliente", "Proyecto": "proyecto",
                "Lugar": "lugar", "Licitacion": "licitacion", "Caso": "caso"}
        return {v: (re.search(r"\\" + k + r"\{([^}]*)\}", t) or re.search("()", "")).group(1)
                for k, v in mapa.items()}

    # --- primera pasada: números de títulos, tablas y figuras ---------------
    def numerar(self, t):
        s = [0, 0, 0]
        nt = nf = 0
        for m in re.finditer(r"\\(section|subsection|subsubsection)\{|\\label\{([^}]*)\}|"
                             r"\\begin\{(tabla|tablaAudit)\}(?:\[[^\]]*\])?|"
                             r"\\(figura|figuraAncha|anexoGrafico)\b", t):
            if m.group(1):
                k = ["section", "subsection", "subsubsection"].index(m.group(1))
                s[k] += 1
                for j in range(k + 1, 3):
                    s[j] = 0
                self._ultima = ".".join(str(x) for x in self._prefijo() + s[:k + 1])
            elif m.group(2):
                if m.group(2) not in self.aux:
                    self.etiquetas.setdefault(m.group(2), getattr(self, "_ultima", str(self.n)))
            elif m.group(3):
                nt += 1
                i = m.end()
                _, i = arg(t, i)
                et, _ = arg(t, i)
                self.etiquetas.setdefault("tab:" + et, self._num(nt))
            elif m.group(4):
                nf += 1
                i = m.end()
                if m.group(4) == "figura":
                    _, i = opcional(t, i)
                a1, i = arg(t, i)
                a2, i = arg(t, i)
                a3, i = arg(t, i)
                self.etiquetas.setdefault("fig:" + a3, self._num(nf))

    def _prefijo(self):
        return [self.n] if self.n else []

    def _num(self, k):
        return ".".join(str(x) for x in self._prefijo() + [k])

    # --- montos de los documentos económicos ---------------------------------
    def _monto(self, clave):
        if not self.eco:
            return f"[{clave}]"
        if clave in self.eco.get("cifras", {}):
            return self.eco["cifras"][clave]
        pend = self.eco.get("pendientes") or {}
        if isinstance(pend, dict) and clave in pend:
            return f"[monto por completar: {pend[clave]}]"
        return f"[{clave}: sin cifra en el PDF]"

    def _tabla_eco(self, etiqueta, leyenda):
        tabla = (self.eco or {}).get("tablas", {}).get(etiqueta)
        num = self.etiquetas.get("tab:" + etiqueta, "?")
        out = ["", f"**Tabla {num}.** {self.en_linea(leyenda)}", ""]
        if not tabla:
            return "\n".join(out + ["[tabla sin datos en el PDF]", ""])
        cab = [self.en_linea(c) for c in tabla["cabecera"]]
        out.append("| " + " | ".join(cab) + " |")
        out.append("|" + "---|" * len(cab))
        for f in tabla["filas"]:
            out.append("| " + " | ".join(c.replace("|", "\\|") for c in f) + " |")
        return "\n".join(out) + "\n"

    # --- conversión ---------------------------------------------------------
    def en_linea(self, t):
        pagina = lambda p: ("p. " if re.fullmatch(r"\d+", p.strip()) else "pp. ") + p.strip()

        def bases(doc):
            def f(loc, pag, estrella=False, opt=None):
                s = f"{doc}, {loc}, {pagina(pag)}"
                return f"({s})" if estrella else s
            return f
        t = reemplazar(t, "art", 2, lambda a, p, **k: bases("FEP01")("Artículo " + a, p, **k), estrella=True)
        t = reemplazar(t, "form", 2, lambda a, p, **k: bases("FEP01")("Formulario " + a, p, **k), estrella=True)
        t = reemplazar(t, "transv", 2, bases("FEP02"), estrella=True)
        t = reemplazar(t, "caso", 2, bases("Caso"), estrella=True)
        t = reemplazar(t, "bases", 3, lambda d, l, p, **k: bases(d)(l, p, **k), estrella=True)
        t = reemplazar(t, "montoPartida", 1, lambda c, **k: self._monto("partida " + c))
        t = reemplazar(t, "monto", 1, lambda v, opt=None, **k: self._monto(f"monto {opt or 'CLP'} {v}"),
                       opt=True)
        t = reemplazar(t, "tasaIVA", 0, lambda **k: str(self.cfg.iva))
        # \textbackslash deja una barra literal. Se guarda con un carácter
        # provisional para que una segunda pasada no la tome por un comando.
        t = re.sub(r"\\textbackslash\s*", "\x1b", t)
        t = t.replace("\\{", "{").replace("\\}", "}")
        t = reemplazar(t, "marcador", 1, lambda x, **k: f"[{self.en_linea(x)}]")
        t = reemplazar(t, "reqMargen", 1, lambda x, **k: f"`{x}` ")
        t = reemplazar(t, "req", 1, lambda x, **k: f"`{x}`")
        t = reemplazar(t, "cifraMargen", 3, lambda v, d, f, **k: f"**{v}** {d} ({f}) ")
        t = reemplazar(t, "cifra", 2, lambda v, f, **k: f"**{v}** ({f})")
        t = reemplazar(t, "parencite", 1, lambda c, opt=None, **k: "(" + "; ".join(
            f"{self.bib.get(x.strip(), (x, ''))[0]}, {self.bib.get(x.strip(), (x, ''))[1]}"
            for x in c.split(",")) + ")", opt=True)
        t = reemplazar(t, "textcite", 1, lambda c, **k: ", ".join(
            f"{self.bib.get(x.strip(), (x, ''))[0]} ({self.bib.get(x.strip(), (x, ''))[1]})"
            for x in c.split(",")))
        t = reemplazar(t, "tabref", 1, lambda x, **k: "Tabla " + self.etiquetas.get("tab:" + x, "?"))
        t = reemplazar(t, "figref", 1, lambda x, **k: "Figura " + self.etiquetas.get("fig:" + x, "?"))
        t = reemplazar(t, "verSeccionFolio", 1, lambda x, **k: "sección " + self.etiquetas.get(x, "?"))
        t = reemplazar(t, "verSeccion", 1, lambda x, **k: "sección " + self.etiquetas.get(x, "?"))
        t = reemplazar(t, "refx", 1, lambda x, **k: self.etiquetas.get(x, "?"))
        t = reemplazar(t, "ref", 1, lambda x, **k: self.etiquetas.get(x, "?"))
        t = reemplazar(t, "dato", 1, lambda x, **k: self.datos.get(x, x))
        t = reemplazar(t, "textbf", 1, lambda x, **k: f"**{x}**")
        t = reemplazar(t, "emph", 1, lambda x, **k: f"*{x}*")
        t = reemplazar(t, "textit", 1, lambda x, **k: f"*{x}*")
        t = reemplazar(t, "texttt", 1, lambda x, **k: f"`{x}`")
        t = reemplazar(t, "leyendaFont", 1, lambda x, **k: x)
        t = re.sub(r"\\label\{[^}]*\}", "", t)
        t = re.sub(r"\$\\leq\$|\\leq", "≤", t)
        t = re.sub(r"\$\\geq\$|\\geq", "≥", t)
        t = re.sub(r"\$\\approx\$|\\approx", "≈", t)
        t = (t.replace("\\%", "%").replace("\\&", "&").replace("\\_", "_").replace("\\#", "#")
             .replace("\\,", " ").replace("~", " ").replace("\\textordmasculine{}", "º")
             .replace("\\\\", " "))
        return t

    def tabla(self, leyenda, etiqueta, cuerpo):
        self.ntab += 1
        cab, _, resto = cuerpo.partition("\\midrule")
        filas = [f for f in re.split(r"\\\\", cab + "\\\\" + resto) if f.strip()]
        filas = [re.sub(r"\\(midrule|toprule|bottomrule|hline)", "", f) for f in filas]
        out = ["", f"**Tabla {self.n}.{self.ntab}.** {self.en_linea(leyenda)}", ""]
        for k, f in enumerate(filas):
            celdas = [self.en_linea(c).strip().replace("\n", " ").replace("|", "\\|") for c in f.split("&")]
            out.append("| " + " | ".join(celdas) + " |")
            if k == 0:
                out.append("|" + "---|" * len(celdas))
        return "\n".join(out) + "\n"

    def figura(self, archivo, leyenda):
        self.nfig += 1
        ley = self.en_linea(leyenda)
        return f"\n![Figura {self.n}.{self.nfig}. {ley}]({archivo})\n\n*Figura {self.n}.{self.nfig}. {ley}*\n"

    def convertir(self, t):
        t = "\n".join(re.sub(r"(?<!\\)%.*$", "", l) for l in t.split("\n"))
        self.numerar(t)
        # tablas generadas de los documentos económicos
        t = reemplazar(t, "tablaMontos", 3, lambda l, e, c, **k: self._tabla_eco(e, l),
                       estrella=True, opt=True)
        t = reemplazar(t, "tablaHitosPago", 0, lambda **k: self._tabla_eco(
            "hitos-e25", "Hitos de pago de la fase de implementación, conforme al "
            "\\form{E-25}{74}, con su monto neto"), opt=True)
        t = reemplazar(t, "tablaTarifas", 0, lambda **k: self._tabla_eco(
            "tarifas-e26", "Costo y tarifa horaria por perfil, dentro de los rangos del "
            "\\form{E-26}{76}"))
        # entornos de tabla
        t = re.sub(r"\\begin\{(tabla|tablaAudit)\}(\[[^\]]*\])?(.*?)\\end\{\1\}",
                   lambda m: self._tabla_env(m.group(3)), t, flags=re.S)
        # figuras
        t = reemplazar(t, "figura", 3, lambda a, l, e, **k: self.figura(a, l), opt=True)
        t = reemplazar(t, "figuraAncha", 3, lambda a, l, e, **k: self.figura(a, l))
        t = reemplazar(t, "anexoGrafico", 3, lambda a, l, e, **k: self.figura(a, l))
        # dispositivos
        t = re.sub(r"\\begin\{resumenApertura\}(.*?)\\end\{resumenApertura\}",
                   lambda m: self._resumen(m.group(1)), t, flags=re.S)
        t = re.sub(r"\\begin\{compromiso\}(\[.*?\])?\s*(.*?)\\end\{compromiso\}",
                   lambda m: self._compromiso(m.group(1) or "", m.group(2)), t, flags=re.S)
        t = reemplazar(t, "decision", 1, lambda kv, **k: self._decision(kv))
        # listas
        t = re.sub(r"\\begin\{(itemize|enumerate)\}(\[[^\]]*\])?", "", t)
        t = re.sub(r"\\end\{(itemize|enumerate)\}", "", t)
        t = re.sub(r"^\s*\\item\s*", "- ", t, flags=re.M)
        # títulos
        t = self._titulos(t)
        t = reemplazar(t, "paragraph", 1, lambda x, **k: f"**{self.en_linea(x)}.** ")
        t = self.en_linea(t)
        t = re.sub(r"\\(FloatBarrier|clearpage|newpage|noindent|par)\b", "", t)
        t = re.sub(r"[ \t]+\n", "\n", t)
        t = re.sub(r"\n{3,}", "\n\n", t)
        return t.strip().replace("\x1b", "\\") + "\n"

    def _tabla_env(self, resto):
        leyenda, i = arg(resto, 0)
        etiqueta, i = arg(resto, i)
        _, i = arg(resto, i)
        return self.tabla(leyenda, etiqueta, resto[i:])

    def _resumen(self, cuerpo):
        cuerpo = re.sub(r"\\begin\{recibe\}", f"\n**Qué recibe {self.datos.get('cliente', '')}**\n", cuerpo)
        cuerpo = cuerpo.replace("\\end{recibe}", "")
        cuerpo = re.sub(r"^\s*\\item\s*", "- ", cuerpo, flags=re.M)
        lineas = self.en_linea(cuerpo).strip().split("\n")
        return "\n> **Resumen de apertura.**\n>\n" + "\n".join("> " + l.strip() for l in lineas) + "\n"

    def _compromiso(self, opciones, cuerpo):
        self.ncomp += 1
        kv = claves(opciones.strip("[]"))
        return (f"\n> **Compromiso C-{self.ncomp:02d}.** {self.en_linea(cuerpo).strip()}\n>\n"
                f"> Métrica: {self.en_linea(kv.get('metrica', ''))}. "
                f"Se verifica en: {self.en_linea(kv.get('verifica', ''))}. "
                f"Fuente: {self.en_linea(kv.get('fuente', ''))}.\n")

    def _decision(self, kv):
        self.ndec += 1
        d = {k: self.en_linea(v) for k, v in claves(kv).items()}
        return (f"\n**Decisión D-{self.ndec:02d}. {d.get('titulo', '')}**\n\n"
                f"| Se decide | Se descarta | Criterio | Fuente |\n|---|---|---|---|\n"
                f"| {d.get('decide', '')} | {d.get('descarta', '')} | {d.get('criterio', '')} | "
                f"{d.get('fuente', '')} |\n")

    def _titulos(self, t):
        """Títulos en una sola pasada, en orden, para numerarlos como el PDF."""
        salida, pos = [], 0
        for m in re.finditer(r"\\(section|subsection|subsubsection)\*?(?=\{)", t):
            if m.start() < pos:
                continue
            texto, fin = arg(t, m.end())
            nivel = ["section", "subsection", "subsubsection"].index(m.group(1))
            salida += [t[pos:m.start()], self._titulo(nivel, texto)]
            pos = fin
        salida.append(t[pos:])
        return "".join(salida)

    def _titulo(self, nivel, texto):
        self.sec[nivel] += 1
        for j in range(nivel + 1, 3):
            self.sec[j] = 0
        num = ".".join(str(x) for x in self._prefijo() + self.sec[:nivel + 1])
        return f"\n{'#' * (nivel + 2)} {num} {self.en_linea(texto)}\n"


def buscar(carpeta, archivo, raices):
    for r in raices:
        ruta = os.path.join(RAIZ, r, carpeta, archivo)
        if os.path.exists(ruta):
            return ruta
    return None


def subdocumento(cfg, n, raices):
    sd = cfg.subdocs[n]
    ruta = buscar(sd["carpeta"], "contenido.tex", raices)
    cuerpo = Conversor(cfg, n).convertir(open(ruta, encoding="utf-8").read())
    rotulo = cfg.rotulos.get(cfg.instancia, ("",))[0]
    cabeza = (f"# Subdocumento {n}. {sd['titulo']}\n\n"
              f"audIT, Empresa N.º 10. Licitación TFEP-01/2026, Caso 10 Transporte de Carga. "
              f"Oferta Técnica, Sobre N.º 2. {rotulo}.\n\n")
    pie = ""
    if sd["formularios"]:
        pie = ("\n## Formularios\n\n" + "\n".join(
            f"- Formulario {f}: su versión oficial es la del PDF." for f in sd["formularios"]) + "\n")
    return cabeza + cuerpo + pie


# ----------------------------------------------------------------------------
#  Documentos económicos
# ----------------------------------------------------------------------------
CARPETAS_ECO = {"costos": "costos-venta", "oferta": "oferta-economica",
                "analisis": "analisis-financiero"}
TITULOS_ECO = {"costos": ("Informe Preparatorio 3", "Costos frente a venta"),
               "oferta": ("Entregable 1", "Propuesta económica formal"),
               "analisis": ("Entregable 2", "Análisis económico-financiero")}


def etiquetas_aux(ruta):
    """Número de cada etiqueta, del .aux del PDF."""
    try:
        t = open(ruta, encoding="utf-8", errors="replace").read()
    except OSError:
        return {}
    return {m.group(1): m.group(2) for m in re.finditer(r"\\newlabel\{([^}]*)\}\{\{([^}]*)\}", t)}


def _con_inputs(ruta):
    """Contenido con los \\input{./...} de la muestra ya incorporados."""
    t = open(ruta, encoding="utf-8").read()
    return re.sub(r"\\input\{\./([^}]*)\}",
                  lambda m: open(os.path.join(RAIZ, m.group(1)), encoding="utf-8").read(), t)


def economico(cfg, clave, raices, aux, eco_json):
    """Markdown de un documento económico, con las cifras que imprimió el PDF."""
    try:
        eco = json.load(open(eco_json, encoding="utf-8"))
    except (OSError, ValueError):
        eco = {"cifras": {}, "tablas": {}, "pendientes": {}}
    numero = {"oferta": 1, "analisis": 2}.get(clave)
    conv = Conversor(cfg, numero, etiquetas_aux(aux), eco)
    ruta = buscar(CARPETAS_ECO[clave], "contenido.tex", raices)
    cuerpo = conv.convertir(_con_inputs(ruta))
    rotulo, titulo = TITULOS_ECO[clave]
    sobre = "Oferta Económica, Sobre N.º 3" if cfg.instancia == "final" else "Propuesta Económica"
    instancia = cfg.rotulos.get(cfg.instancia, ("",))[0]
    cabeza = (f"# {rotulo}. {titulo}\n\n"
              f"audIT, Empresa N.º 10. Licitación TFEP-01/2026, Caso 10 Transporte de Carga. "
              f"{sobre}. {instancia}.\n\n")
    tc = eco.get("tablas", {}).get("parametros-e24")
    param = ""
    if tc:
        param = ("\n## Tipo de cambio y parámetros\n\n"
                 "Todos los valores de este documento están en pesos chilenos, Unidades de Fomento "
                 "y dólares de los Estados Unidos, con los tipos de cambio del FEP01, Formulario "
                 "E-24, p. 73, conforme a FEP01, Artículo 51.2, p. 29. Son valores netos, con el IVA "
                 "desglosado. Cada valor en UF y en USD se calcula a partir de su valor en pesos y se "
                 "redondea a dos decimales. Las sumas se hacen en pesos.\n\n"
                 "**Condiciones y parámetros para la preparación de la oferta económica, conforme al "
                 "FEP01, Formulario E-24, p. 73**\n\n"
                 "| " + " | ".join(tc["cabecera"]) + " |\n|" + "---|" * len(tc["cabecera"]) + "\n"
                 + "\n".join("| " + " | ".join(f) + " |" for f in tc["filas"]) + "\n")
    return cabeza + param + f"\n## {(str(numero) + ' ') if numero else ''}{titulo}\n\n" + cuerpo


if __name__ == "__main__":
    cfg = Config()
    raices = ["muestra/subdocumentos", "subdocumentos"] if "--muestra" in sys.argv else ["subdocumentos"]
    for a in [x for x in sys.argv[1:] if not x.startswith("--")] or [str(x) for x in cfg.lista()]:
        print(subdocumento(cfg, int(a), raices))
