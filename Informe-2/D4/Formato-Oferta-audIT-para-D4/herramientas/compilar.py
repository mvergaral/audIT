#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Compila las entregas del formato.

  python3 herramientas/compilar.py muestra          salida/muestra.pdf y la
                                                    muestra en varios PDF con
                                                    folio continuo
  python3 herramientas/compilar.py unico            documento único de la
                                                    instancia vigente
  python3 herramientas/compilar.py subdocs [04 13]  un PDF por subdocumento,
                                                    con el modo de folio de
                                                    configuracion/instancia.tex
  python3 herramientas/compilar.py md [04 13]       equivalentes en Markdown
  python3 herramientas/compilar.py economico        documentos económicos de
                                                    la instancia: costos frente
                                                    a venta (Informe 3) o los
                                                    entregables del Sobre N.º 3
                                                    (final), con Markdown, DOCX,
                                                    planilla y ZIP
  python3 herramientas/compilar.py limpiar          borra salida/aux

Opciones: -j N compilaciones en paralelo (por defecto, los núcleos del equipo)
          --forzar recompila aunque nada haya cambiado
          --continuo / --por-subdocumento fuerza el modo de folio
          --caratula agrega la carátula del sobre (SUBDOC00) en modo por
          subdocumento. En modo continuo va siempre.

Modo continuo: primero compila todos los PDF para saber cuántas páginas
tiene cada uno, calcula el folio inicial de cada archivo, recompila con esos
folios y arma la hoja resumen con los folios reales de todos los archivos.
Si algún conteo de páginas cambia, repite (hasta cuatro vueltas).

Dependencias: latexmk sigue los archivos del .fls, pero en el formato
anterior no detectaba cambios en los archivos comunes. Aquí cada compilación
guarda un hash de estilo/, fuentes/, temas/, portadas/, formularios/,
configuracion/, referencias/, figuras/, de las carpetas de subdocumento que
usa y del preámbulo que recibe. Si el hash cambia, se fuerza la recompilación.
"""
import argparse
import concurrent.futures as cf
import hashlib
import os
import re
import shutil
import subprocess
import sys
import time
import zipfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from comun import RAIZ, SALIDA, Config, guardar_json, leer_json  # noqa: E402

COMUNES = ["estilo", "fuentes", "temas", "portadas", "formularios",
           "configuracion", "referencias", "figuras"]


# ----------------------------------------------------------------------------
#  Perfiles: qué raíces de subdocumentos, observaciones y bibliografía se usan
# ----------------------------------------------------------------------------
class Perfil:
    def __init__(self, nombre, raices, observaciones=None, bib=None,
                 compat=False, carpetas_extra=()):
        self.nombre = nombre
        self.raices = raices
        self.observaciones = observaciones
        self.bib = bib
        self.compat = compat
        self.carpetas_extra = list(carpetas_extra)

    def preambulo(self):
        p = ""
        if self.compat:
            p += r"\PassOptionsToClass{compatibilidad}{audit-oferta}"
        p += r"\def\RaizSubdocumentos{%s}" % ",".join(self.raices)
        if self.observaciones:
            p += r"\def\ArchivoObservaciones{%s}" % self.observaciones
        if self.bib:
            p += r"\def\BibliografiaAdicional{%s}" % self.bib
        return p


OFERTA = Perfil("oferta", ["subdocumentos"], carpetas_extra=["subdocumentos", "anexos"])
ECONOMICO = ["economico"]
ECONOMICO_MUESTRA = ["muestra/economico", "economico"]
MUESTRA = Perfil("muestra", ["muestra/subdocumentos", "subdocumentos"],
                 observaciones="muestra/observaciones-informe1.tex",
                 bib="muestra/referencias-muestra.bib", compat=True,
                 carpetas_extra=["muestra", "subdocumentos"])


# ----------------------------------------------------------------------------
#  Compilación de un documento
# ----------------------------------------------------------------------------
def huella(carpetas, extra=""):
    h = hashlib.sha256(extra.encode())
    for c in carpetas:
        base = os.path.join(RAIZ, c)
        if os.path.isfile(base):
            archivos = [base]
        else:
            archivos = []
            for d, _, fs in os.walk(base):
                archivos += [os.path.join(d, f) for f in fs]
        for f in sorted(archivos):
            h.update(f.encode())
            with open(f, "rb") as fh:
                h.update(fh.read())
    return h.hexdigest()


class Trabajo:
    """Un PDF: archivo fuente, nombre final, folio inicial y preámbulo."""

    def __init__(self, clave, fuente, nombre, auxdir, preambulo, carpetas):
        self.clave = clave
        self.fuente = fuente
        self.nombre = nombre
        self.auxdir = auxdir
        self.preambulo_base = preambulo
        self.carpetas = carpetas
        self.folio = 1
        self.extra = ""
        self.paginas = None
        self.ok = False
        self.segundos = 0.0

    @property
    def pdf(self):
        return os.path.join(self.auxdir, self.nombre + ".pdf")

    @property
    def aux(self):
        return os.path.join(self.auxdir, self.nombre + ".aux")

    @property
    def log(self):
        return os.path.join(self.auxdir, self.nombre + ".log")

    def preambulo(self):
        return (self.preambulo_base + r"\def\FolioInicialExterno{%d}" % self.folio
                + r"\def\NombreArchivo{%s}\def\ArchivoActual{%s}" % (self.nombre, self.nombre)
                + self.extra)

    def pide_otra_pasada(self):
        try:
            return bool(RERUN.search(open(self.log, encoding="utf-8", errors="replace").read()))
        except OSError:
            return False

    def compilar(self, forzar=False):
        os.makedirs(self.auxdir, exist_ok=True)
        pre = self.preambulo()
        firma = huella(COMUNES + self.carpetas + [self.fuente], pre)
        marca = os.path.join(self.auxdir, "huella.txt")
        anterior = open(marca).read() if os.path.exists(marca) else ""
        # Con -usepretex latexmk arma su propia orden de LuaLaTeX y no usa la
        # del .latexmkrc: el modo sin interacción se pide aquí. Sin él, ante
        # un error TeX se queda esperando una respuesta en la terminal.
        cmd = ["latexmk", "-lualatex", "-interaction=nonstopmode", "-halt-on-error",
               "-file-line-error", "-outdir=" + self.auxdir,
               "-jobname=" + self.nombre, "-usepretex=" + pre]
        if forzar or firma != anterior or not os.path.exists(self.pdf):
            cmd.append("-g")
        cmd.append(self.fuente)
        t = time.time()
        with open(os.path.join(self.auxdir, "compilacion.txt"), "w") as salida:
            r = subprocess.run(cmd, cwd=RAIZ, stdout=salida, stderr=subprocess.STDOUT,
                               stdin=subprocess.DEVNULL)
            # latexmk no reconoce el aviso de longtable «Table widths have
            # changed. Rerun LaTeX»: si el registro pide otra pasada, se fuerza
            for _ in range(2):
                if r.returncode != 0 or not self.pide_otra_pasada():
                    break
                forzado = [c for c in cmd if c != "-g"]
                forzado.insert(-1, "-g")
                r = subprocess.run(forzado, cwd=RAIZ, stdout=salida, stderr=subprocess.STDOUT,
                                   stdin=subprocess.DEVNULL)
        self.segundos = time.time() - t
        self.ok = r.returncode == 0 and os.path.exists(self.pdf)
        if self.ok:
            with open(marca, "w") as f:
                f.write(firma)
            self.paginas = contar_paginas(self.pdf)
        return self


RERUN = re.compile(r"Rerun LaTeX|Rerun to get|Label\(s\) may have changed|Table widths have changed")


def contar_paginas(pdf):
    out = subprocess.run(["pdfinfo", pdf], capture_output=True, text=True).stdout
    m = re.search(r"^Pages:\s+(\d+)", out, re.M)
    return int(m.group(1)) if m else None


def ejecutar(trabajos, jobs, forzar=False):
    with cf.ThreadPoolExecutor(max_workers=jobs) as ex:
        list(ex.map(lambda t: t.compilar(forzar), trabajos))
    for t in trabajos:
        estado = "ok   " if t.ok else "FALLA"
        pags = f"{t.paginas:3d} págs" if t.paginas else "   -    "
        print(f"  {estado} {t.nombre:42s} folio {t.folio:4d}  {pags}  {t.segundos:5.1f} s", flush=True)
        if not t.ok:
            mostrar_error(t)
    return all(t.ok for t in trabajos)


def mostrar_error(t):
    try:
        log = open(t.log, encoding="utf-8", errors="replace").read()
    except OSError:
        print("        sin registro, ver", os.path.join(t.auxdir, "compilacion.txt"))
        return
    for m in list(re.finditer(r"^(?:! |.*:\d+: )(.*)$", log, re.M))[:3]:
        print("        " + m.group(0)[:160])
    print("        registro:", os.path.relpath(t.log, RAIZ))


# ----------------------------------------------------------------------------
#  Oferta en varios PDF
# ----------------------------------------------------------------------------
def entradas_folio(aux):
    """Las \\entradaFolio del .aux, en orden, sin repetir."""
    try:
        texto = open(aux, encoding="utf-8", errors="replace").read()
    except OSError:
        return []
    vistas, salida = set(), []
    for m in re.finditer(r"\\entradaFolio\{([^{}]*)\}\{((?:[^{}]|\{[^{}]*\})*)\}\{(\d+)\}\{([^{}]*)\}", texto):
        if m.group(1) not in vistas:
            vistas.add(m.group(1))
            salida.append(m.groups())
    return salida


def varios(cfg, perfil, lista, grupo, continuo, caratula, jobs, forzar):
    auxbase = os.path.join(SALIDA, "aux", grupo)
    destino = os.path.join(SALIDA, grupo)
    os.makedirs(destino, exist_ok=True)
    pre = perfil.preambulo()
    trabajos = []
    for n in lista:
        sd = cfg.subdocs[n]
        t = Trabajo(f"{n:02d}", "subdocumento.tex", cfg.nombre_subdoc(n),
                    os.path.join(auxbase, f"{n:02d}"),
                    pre + r"\def\NumeroSubdoc{%d}" % n,
                    [os.path.join(r, sd["carpeta"]) for r in perfil.raices
                     if os.path.isdir(os.path.join(RAIZ, r, sd["carpeta"]))]
                    + ([perfil.observaciones] if perfil.observaciones else []))
        trabajos.append(t)
    # Comunicado 10, sección 1: cada formulario en su propio archivo
    formularios = []
    if cfg.instancia != "informe1":
        for n in lista:
            sd = cfg.subdocs[n]
            for f in sd["formularios"]:
                tf = Trabajo(f"{n:02d}{f}", "formulario.tex", cfg.nombre_formulario(f),
                             os.path.join(auxbase, f"{n:02d}{f}"),
                             pre + r"\def\NumeroSubdoc{%d}\def\FormularioActual{%s}" % (n, f),
                             [os.path.join(r, sd["carpeta"]) for r in perfil.raices
                              if os.path.isdir(os.path.join(RAIZ, r, sd["carpeta"]))])
                tf.subdoc, tf.formulario = n, f
                formularios.append(tf)
    subdocs_trab = list(trabajos)
    trabajos = trabajos + formularios
    car = None
    if continuo or caratula:
        car = Trabajo("00", "caratula.tex", cfg.nombre_caratula(), os.path.join(auxbase, "00"),
                      pre, perfil.carpetas_extra)

    # Referencias a los otros subdocumentos (xr-hyper). Cada vuelta lee una
    # copia congelada de los .aux ajenos: si leyera los .aux vivos, latexmk
    # vería que cambian mientras los otros compilan y entraría en un ciclo.
    congelados = os.path.join(auxbase, "externos")

    def congelar():
        shutil.rmtree(congelados, ignore_errors=True)
        os.makedirs(congelados, exist_ok=True)
        for o in trabajos:
            if os.path.exists(o.aux):
                shutil.copy(o.aux, os.path.join(congelados, o.nombre + ".aux"))

    def externos(t):
        ruta = os.path.join(t.auxdir, "externos.tex")
        os.makedirs(t.auxdir, exist_ok=True)
        with open(ruta, "w", encoding="utf-8") as f:
            for o in trabajos:
                if o is t:
                    continue
                base = os.path.relpath(os.path.join(congelados, o.nombre), RAIZ)
                f.write("\\RegistrarPrefijo{S%s-}\\externaldocument[S%s-]{%s}[%s.pdf]\n"
                        % (o.clave, o.clave, base, o.nombre))
        return os.path.relpath(ruta, RAIZ)

    previo = leer_json(os.path.join(auxbase, "folios.json"), {}) or {}
    for t in trabajos + ([car] if car else []):
        t.folio = previo.get(t.clave, 1) if continuo else 1

    ok = True
    for vuelta in range(1, 5):
        print(f"  vuelta {vuelta}", flush=True)
        congelar()
        for t in trabajos:
            t.extra = r"\def\ArchivoExternos{%s}" % externos(t)
        orden = ([car] if car else []) + trabajos
        ok = ejecutar(trabajos, jobs, forzar and vuelta == 1)
        if not ok:
            return None
        if car:
            # la carátula necesita los folios de todos: se arma al final
            if forzar and vuelta == 1:
                car.extra = ""
                if not ejecutar([car], 1, True):
                    return None
            if not hoja_estable(car, trabajos, auxbase):
                return None
        if not continuo:
            break
        # folio inicial de cada archivo a partir de los conteos reales
        nuevos, siguiente = {}, 1
        for t in orden:
            nuevos[t.clave] = siguiente
            siguiente += t.paginas
        cambio = any(nuevos[t.clave] != t.folio for t in orden)
        for t in orden:
            t.folio = nuevos[t.clave]
        guardar_json(os.path.join(auxbase, "folios.json"), nuevos)
        if not cambio and vuelta > 1:
            break
        if not cambio and vuelta == 1:
            # los folios ya eran correctos, falta solo resolver referencias
            continue

    # Copia con el nombre final y manifiesto para el verificador
    orden = ([car] if car else []) + trabajos
    manifiesto = {"grupo": grupo, "instancia": cfg.instancia, "modo_folio":
                  "continuo" if continuo else "subdocumento", "archivos": []}
    for t in orden:
        shutil.copy(t.pdf, os.path.join(destino, t.nombre + ".pdf"))
        manifiesto["archivos"].append({
            "clave": t.clave, "nombre": t.nombre + ".pdf", "folio_inicial": t.folio,
            "paginas": t.paginas, "aux": os.path.relpath(t.aux, RAIZ),
            "log": os.path.relpath(t.log, RAIZ),
            "fuentes": [perfil.raices, t.carpetas]})
    guardar_json(os.path.join(destino, "manifiesto.json"), manifiesto)
    # Markdown equivalente de cada subdocumento, desde el mismo contenido.tex
    import tex2md
    for n, t in zip(lista, subdocs_trab):
        with open(os.path.join(destino, t.nombre + ".md"), "w", encoding="utf-8") as f:
            f.write(tex2md.subdocumento(cfg, n, perfil.raices, t.aux))
    for t in formularios:
        with open(os.path.join(destino, t.nombre + ".md"), "w", encoding="utf-8") as f:
            f.write(tex2md.formulario(cfg, t.subdoc, t.formulario, perfil.raices))
    print(f"  {len(orden)} PDF y {len(trabajos)} Markdown en {os.path.relpath(destino, RAIZ)}/")
    return orden


def juntar_folios(car, trabajos, auxbase):
    """Archivo con las entradas de folio de todos los PDF, para la hoja resumen."""
    ruta = os.path.join(auxbase, "folios-sobre.tex")
    with open(ruta, "w", encoding="utf-8") as f:
        f.write("% Generado por herramientas/compilar.py a partir de los .aux\n")
        for t in [car] + trabajos:
            for clave, titulo, folio, _ in entradas_folio(t.aux):
                f.write("\\entradaFolio{%s}{%s}{%s}{%s}\n" % (clave, titulo, folio, t.nombre))
    car.extra = r"\def\FoliosSobre{%s}" % os.path.relpath(ruta, RAIZ)


def hoja_estable(car, otros, auxbase, veces=4):
    """Compila el documento que lleva la hoja resumen del sobre con los folios
    de todos, hasta que sus propios folios dejan de moverse. La hoja crece al
    recibir las entradas de los otros archivos y corre las secciones que la
    siguen en el mismo documento: si el archivo de folios se armara una sola
    vez, esas secciones quedarían con el folio de antes."""
    ruta = os.path.join(auxbase, "folios-sobre.tex")
    juntar_folios(car, otros, auxbase)
    for _ in range(veces):
        if not ejecutar([car], 1):
            return False
        antes = open(ruta, encoding="utf-8").read()
        juntar_folios(car, otros, auxbase)
        if open(ruta, encoding="utf-8").read() == antes:
            return True
    print(f"  Aviso: los folios de {car.nombre} no se estabilizaron")
    return True


def unico(cfg, perfil, fuente, nombre, grupo, forzar):
    auxdir = os.path.join(SALIDA, "aux", grupo)
    t = Trabajo("unico", fuente, nombre, auxdir, perfil.preambulo(), perfil.carpetas_extra)
    ok = ejecutar([t], 1, forzar)
    if ok:
        return t
    return None


# ----------------------------------------------------------------------------
#  Documentos económicos (Formulario T-22 y Formulario E-21)
# ----------------------------------------------------------------------------
def economicos(cfg, raices, grupo, jobs, forzar, forzar_instancia=False):
    """Compila los documentos económicos de la instancia de cfg. La hoja
    resumen va en el primero (Artículo 40.3: al inicio del sobre) y lista los
    folios de todos. En modo continuo el folio sigue de un documento al otro.
    Deja Markdown y, para los entregables del E-21, DOCX con las cifras que
    imprimió el PDF. Copia la planilla del mandante con su nombre y, en la
    propuesta final, arma el ZIP del Sobre N.º 3."""
    import tex2md
    import md2docx
    claves = cfg.docs_economicos.get(cfg.instancia, [])
    if not claves:
        print(f"  La instancia {cfg.instancia} no tiene documentos económicos "
              "(configuracion/economico.tex).")
        return None
    auxbase = os.path.join(SALIDA, "aux", grupo)
    destino = os.path.join(SALIDA, grupo)
    os.makedirs(destino, exist_ok=True)
    continuo = cfg.modo_folio == "continuo"
    pre = r"\def\RaizEconomico{%s}" % ",".join(raices)
    if forzar_instancia:
        pre += r"\def\InstanciaForzada{%s}" % cfg.instancia
    carpetas = raices + ["documento-economico.tex", "anexos"]
    trabajos = [Trabajo(c, "documento-economico.tex", cfg.nombre_economico(c),
                        os.path.join(auxbase, c), pre + r"\def\DocumentoEco{%s}" % c, carpetas)
                for c in claves]
    previo = leer_json(os.path.join(auxbase, "folios.json"), {}) or {}
    for t in trabajos:
        t.folio = previo.get(t.clave, 1) if continuo else 1
    for vuelta in range(1, 5):
        print(f"  vuelta {vuelta}", flush=True)
        if not ejecutar(trabajos, jobs, forzar and vuelta == 1):
            return None
        if len(trabajos) > 1:
            # la hoja resumen del primero lista los folios de todos
            if not hoja_estable(trabajos[0], trabajos[1:], auxbase):
                return None
        if not continuo:
            break
        nuevos, siguiente = {}, 1
        for t in trabajos:
            nuevos[t.clave] = siguiente
            siguiente += t.paginas
        cambio = any(nuevos[t.clave] != t.folio for t in trabajos)
        for t in trabajos:
            t.folio = nuevos[t.clave]
        guardar_json(os.path.join(auxbase, "folios.json"), nuevos)
        if not cambio:
            break
    manifiesto = {"grupo": grupo, "instancia": cfg.instancia, "tipo": "economico",
                  "modo_folio": "continuo" if continuo else "subdocumento", "archivos": []}
    entregables = []
    pie = ("TFEP-01/2026 · Caso 10 · "
           + ("Oferta Económica, Sobre N.º 3" if cfg.instancia == "final" else "Propuesta Económica")
           + " · " + cfg.rotulos.get(cfg.instancia, ("",))[0])
    for t in trabajos:
        pdf = t.nombre + ".pdf"
        shutil.copy(t.pdf, os.path.join(destino, pdf))
        eco = os.path.join(t.auxdir, t.nombre + ".eco.json")
        md = tex2md.economico(cfg, t.clave, raices, t.aux, eco)
        with open(os.path.join(destino, t.nombre + ".md"), "w", encoding="utf-8") as f:
            f.write(md)
        docx = None
        if t.clave in cfg.E21:
            # Formulario E-21 y Artículo 40.4: documentos 1 y 2 también en DOCX
            docx = t.nombre + ".docx"
            md2docx.construir(md, os.path.join(destino, docx), t.nombre, pie, t.folio)
        entregables += [pdf] + ([docx] if docx else [])
        manifiesto["archivos"].append({
            "clave": t.clave, "nombre": pdf, "folio_inicial": t.folio, "paginas": t.paginas,
            "aux": os.path.relpath(t.aux, RAIZ), "log": os.path.relpath(t.log, RAIZ),
            "eco": os.path.relpath(eco, RAIZ), "docx": docx, "fuentes": [raices, t.carpetas]})
    # Planilla del mandante: el formato no la genera, la copia con su nombre
    import planilla as pl
    origen = pl.buscar_planilla(raices)
    manifiesto["planilla"] = None
    if origen:
        nombre = cfg.nombre_planilla()
        shutil.copy(origen, os.path.join(destino, nombre))
        manifiesto["planilla"] = nombre
        entregables.append(nombre)
        print(f"  planilla {os.path.relpath(origen, RAIZ)} -> {nombre}")
    else:
        print("  Aviso: no hay planilla en " + " ni en ".join(f"{r}/planilla/" for r in raices)
              + ". La entrega el mandante y va con el nombre " + cfg.nombre_planilla())
    manifiesto["zip"] = None
    if cfg.instancia == "final":
        # FEP01, Artículo 51.3: SOBRE3_[EMPRESA]_OFERTA_ECONOMICA_AAAAMMDD.ZIP
        ruta = os.path.join(destino, cfg.nombre_zip_economico())
        with zipfile.ZipFile(ruta, "w", zipfile.ZIP_DEFLATED) as z:
            for e in entregables:
                z.write(os.path.join(destino, e), e)
        manifiesto["zip"] = cfg.nombre_zip_economico()
        print("  " + os.path.relpath(ruta, RAIZ))
    guardar_json(os.path.join(destino, "manifiesto.json"), manifiesto)
    print(f"  {len(trabajos)} PDF, {len(trabajos)} Markdown y "
          f"{sum(1 for a in manifiesto['archivos'] if a['docx'])} DOCX en {os.path.relpath(destino, RAIZ)}/")
    return trabajos


def orden_economico(cfg, args):
    print(f"Documentos económicos de {cfg.instancia}")
    r = economicos(cfg, ECONOMICO, cfg.instancia + "-economica", args.jobs, args.forzar)
    return 0 if r else 1


# ----------------------------------------------------------------------------
#  Órdenes
# ----------------------------------------------------------------------------
def orden_muestra(cfg, args):
    print("Muestra en documento único")
    t = unico(cfg, MUESTRA, "muestra/muestra.tex", "muestra", "muestra", args.forzar)
    if not t:
        return 1
    shutil.copy(t.pdf, os.path.join(SALIDA, "muestra.pdf"))
    guardar_json(os.path.join(SALIDA, "manifiesto-muestra.json"), {
        "grupo": "muestra", "instancia": cfg.instancia, "modo_folio": "unico",
        "archivos": [{"clave": "unico", "nombre": "muestra.pdf", "folio_inicial": 1,
                      "paginas": t.paginas, "aux": os.path.relpath(t.aux, RAIZ),
                      "log": os.path.relpath(t.log, RAIZ),
                      "fuentes": [MUESTRA.raices, []]}]})
    print("  salida/muestra.pdf")
    print("\nMuestra en tres subdocumentos con folio continuo")
    r = varios(cfg, MUESTRA, [2, 4, 13], "muestra-continua", True, True,
               args.jobs, args.forzar)
    if not r:
        return 1
    # documentos económicos: los del Informe 3 y los del Sobre N.º 3, con las
    # partidas de demostración de muestra/economico (1 UF y 1 USD del E-24)
    for inst in ("informe3", "final"):
        print(f"\nMuestra económica, {inst}")
        c = Config(inst)
        if not economicos(c, ECONOMICO_MUESTRA, "muestra-economica-" + inst, args.jobs,
                          args.forzar, forzar_instancia=True):
            return 1
    return 0


def sin_tecnica(cfg):
    if cfg.lista():
        return False
    print(f"La instancia {cfg.instancia} no tiene oferta técnica: el Formulario T-22 le asigna "
          "solo documentos económicos. Usar: python3 herramientas/compilar.py economico")
    return True


def orden_unico(cfg, args):
    if sin_tecnica(cfg):
        return 0
    print(f"Documento único, {cfg.instancia}")
    t = unico(cfg, OFERTA, "principal.tex", cfg.nombre_unico(), cfg.instancia + "-unico",
              args.forzar)
    if not t:
        return 1
    destino = os.path.join(SALIDA, cfg.instancia)
    os.makedirs(destino, exist_ok=True)
    shutil.copy(t.pdf, os.path.join(destino, t.nombre + ".pdf"))
    guardar_json(os.path.join(destino, "manifiesto-unico.json"), {
        "grupo": cfg.instancia + "-unico", "instancia": cfg.instancia, "modo_folio": "unico",
        "archivos": [{"clave": "unico", "nombre": t.nombre + ".pdf", "folio_inicial": 1,
                      "paginas": t.paginas, "aux": os.path.relpath(t.aux, RAIZ),
                      "log": os.path.relpath(t.log, RAIZ), "fuentes": [OFERTA.raices, []]}]})
    print("  " + os.path.relpath(os.path.join(destino, t.nombre + ".pdf"), RAIZ))
    return 0


def orden_subdocs(cfg, args):
    if sin_tecnica(cfg):
        return 0
    lista = cfg.lista()
    if args.numeros:
        pedidos = {int(x) for x in args.numeros}
        lista = [n for n in lista if n in pedidos]
    continuo = cfg.modo_folio == "continuo"
    if args.continuo:
        continuo = True
    if args.por_subdocumento:
        continuo = False
    if continuo and args.numeros:
        print("  Aviso: en modo continuo el folio depende de todos los subdocumentos.")
        print("  Se compila la instancia completa.")
        lista = cfg.lista()
    modo = "continuo" if continuo else "por subdocumento"
    print(f"Subdocumentos de {cfg.instancia}: {lista}, folio {modo}")
    # La carátula del sobre no se genera en los informes (D4-27): solo con --caratula
    caratula = args.caratula
    # Un modo de folio distinto del configurado sale en otra carpeta, para no
    # pisar la entrega: salida/informe2-continuo/
    grupo = cfg.instancia
    if continuo != (cfg.modo_folio == "continuo"):
        grupo += "-continuo" if continuo else "-por-subdocumento"
    orden = varios(cfg, OFERTA, lista, grupo, continuo, caratula,
                   args.jobs, args.forzar)
    if not orden:
        return 1
    if cfg.instancia == "final" and grupo == cfg.instancia:
        ruta = os.path.join(SALIDA, cfg.instancia, cfg.nombre_zip())
        with zipfile.ZipFile(ruta, "w", zipfile.ZIP_DEFLATED) as z:
            for t in orden:
                z.write(os.path.join(SALIDA, cfg.instancia, t.nombre + ".pdf"), t.nombre + ".pdf")
        print("  " + os.path.relpath(ruta, RAIZ))
    return 0


def anterior(instancia):
    return {"informe2": "informe1", "informe3": "informe2", "final": "informe3"}.get(instancia, "-")


def orden_md(cfg, args):
    import tex2md
    lista = cfg.lista()
    if args.numeros:
        lista = [n for n in lista if n in {int(x) for x in args.numeros}]
    destino = os.path.join(SALIDA, cfg.instancia)
    os.makedirs(destino, exist_ok=True)
    for n in lista:
        sd = cfg.subdocs[n]
        md = tex2md.subdocumento(cfg, n, ["subdocumentos"])
        ruta = os.path.join(destino, cfg.nombre_subdoc(n) + ".md")
        open(ruta, "w", encoding="utf-8").write(md)
        print("  " + os.path.relpath(ruta, RAIZ))
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("orden", choices=["muestra", "unico", "subdocs", "md", "economico", "limpiar"])
    ap.add_argument("numeros", nargs="*")
    ap.add_argument("-j", "--jobs", type=int, default=os.cpu_count() or 2)
    ap.add_argument("--forzar", action="store_true")
    ap.add_argument("--continuo", action="store_true")
    ap.add_argument("--por-subdocumento", action="store_true")
    ap.add_argument("--caratula", action="store_true")
    args = ap.parse_args()
    if shutil.which("latexmk") is None or shutil.which("lualatex") is None:
        print("Faltan latexmk o lualatex en el PATH")
        return 2
    cfg = Config()
    if args.orden == "limpiar":
        shutil.rmtree(os.path.join(SALIDA, "aux"), ignore_errors=True)
        print("salida/aux borrado")
        return 0
    return {"muestra": orden_muestra, "unico": orden_unico, "subdocs": orden_subdocs,
            "md": orden_md, "economico": orden_economico}[args.orden](cfg, args)


if __name__ == "__main__":
    sys.exit(main())
