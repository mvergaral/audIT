# -*- coding: utf-8 -*-
"""Lectura de la configuración del formato y nombres de archivo.

La fuente de verdad son los .tex de configuracion/. Este módulo los lee con
expresiones regulares para que Python y LaTeX usen exactamente los mismos
datos: instancia, fecha, modo de folio, catálogo de subdocumentos y
subdocumentos de cada instancia.
"""
import json
import os
import re

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SALIDA = os.path.join(RAIZ, "salida")


def _leer(rel):
    with open(os.path.join(RAIZ, rel), encoding="utf-8") as f:
        # sin comentarios
        return "\n".join(l.split("%")[0] if not l.lstrip().startswith("%") else ""
                         for l in f.read().split("\n"))


def _uno(texto, comando, defecto=None):
    m = re.search(r"\\" + comando + r"\{([^}]*)\}", texto)
    return m.group(1).strip() if m else defecto


class Config:
    """Datos de la entrega, leídos de configuracion/*.tex.

    Config(instancia="final") arma los datos de otra instancia con la fecha
    y el modo de folio del calendario del Formulario T-20 (la muestra
    económica lo usa, igual que \\AplicarInstancia en LaTeX)."""

    def __init__(self, instancia=None):
        inst = _leer("configuracion/instancia.tex")
        meta = _leer("configuracion/metadatos.tex")
        cat = _leer("configuracion/subdocumentos.tex")
        eco = _leer("configuracion/economico.tex")
        self.instancia = _uno(inst, "Instancia", "informe1")
        self.fecha = _uno(inst, "FechaEntrega", "2026-01-01")
        self.modo_folio = _uno(inst, "ModoFolio", "subdocumento")
        self.anexo = _uno(inst, "AnexoHorizontal", "pagina")
        self.calendario = {m.group(1): (m.group(2), m.group(3)) for m in re.finditer(
            r"\\CalendarioInstancia\{([^}]*)\}\{([^}]*)\}\{([^}]*)\}", cat)}
        if instancia and instancia != self.instancia:
            self.instancia = instancia
            self.fecha, self.modo_folio = self.calendario[instancia]
        # Formulario E-24: pesos por unidad de cada moneda, tasa del IVA
        self.tipos_cambio = {m.group(1): int(m.group(3)) for m in re.finditer(
            r"\\TipoCambio\{([^}]*)\}\{([^}]*)\}\{(\d+)\}", eco)}
        self.iva = int(_uno(eco, "TasaIVA", "19"))
        self.docs_economicos = {m.group(1): [x.strip() for x in m.group(2).split(",") if x.strip()]
                                for m in re.finditer(
            r"\\DocumentosEconomicosDeInstancia\{([^}]*)\}\{([^}]*)\}", eco)}
        self.sigla = _uno(meta, "SiglaArchivo", "AUDIT")
        self.subdocs = {}
        for m in re.finditer(r"\\DeclararSubdocumento\{(\d+)\}\{([^}]*)\}\s*\{([^}]*)\}\s*"
                             r"\{([^}]*)\}\s*\{([^}]*)\}", cat):
            n = int(m.group(1))
            self.subdocs[n] = {
                "numero": n, "carpeta": m.group(2), "titulo": " ".join(m.group(3).split()),
                "corto": m.group(4),
                "formularios": [f.strip() for f in m.group(5).split(",") if f.strip()],
            }
        self.listas = {m.group(1): [int(x) for x in m.group(2).split(",") if x.strip()]
                       for m in re.finditer(r"\\SubdocumentosDeInstancia\{([^}]*)\}\{([^}]*)\}", cat)}
        self.rotulos = {m.group(1): (m.group(2), m.group(3))
                        for m in re.finditer(r"\\RotuloDeInstancia\{([^}]*)\}\{([^}]*)\}\{([^}]*)\}", cat)}

    @property
    def fecha_archivo(self):
        return self.fecha.replace("-", "")

    @property
    def prefijo(self):
        return self.rotulos.get(self.instancia, ("", "INFORME"))[1]

    def lista(self):
        return self.listas.get(self.instancia, [])

    # Artículos 49 a 51 y patrón usado por el equipo en el Informe 1
    def nombre_subdoc(self, n):
        # Comunicado 10, sección 1 (desde el Informe 2): EMPRESA-SubdocumentoX.
        # El Informe 1 se entregó con el patrón anterior.
        if self.instancia == "informe1":
            return f"{self.prefijo}_{self.sigla}_SUBDOC{n:02d}_{self.fecha_archivo}"
        return f"{self.sigla}-Subdocumento{n}"

    def nombre_formulario(self, f):
        # Comunicado 10, sección 1: EMPRESA-Formulario-T-X, un formulario por archivo
        return f"{self.sigla}-Formulario-{f}"

    def nombre_caratula(self):
        return f"{self.prefijo}_{self.sigla}_SUBDOC00_{self.fecha_archivo}"

    def nombre_unico(self):
        return f"{self.prefijo}_{self.sigla}_OFERTA_TECNICA_{self.fecha_archivo}"

    def nombre_zip(self):
        # FEP01, Artículo 50.3: SOBRE2_[EMPRESA]_OFERTA_TECNICA_AAAAMMDD.ZIP
        return f"SOBRE2_{self.sigla}_OFERTA_TECNICA_{self.fecha_archivo}.ZIP"

    # Documentos económicos. Formulario E-21 (FEP01 p.72), «sin excepción»:
    # [EMPRESA]_OfertaEconomica_1_[FECHA].pdf, [EMPRESA]_AnalisisFinanciero_2_
    # [FECHA].pdf y [EMPRESA]_ModeloFinanciero_3_[FECHA].xlsx. El formulario no
    # fija el formato de la fecha: se usa AAAAMMDD, como en los Artículos 49 a
    # 51 (supuesto anotado en la guía). El Informe 3 sigue el patrón de los
    # informes: INFORME3_AUDIT_COSTOS_VENTA_20261113.pdf (supuesto).
    E21 = {"oferta": "OfertaEconomica_1", "analisis": "AnalisisFinanciero_2"}

    def nombre_economico(self, clave):
        if clave in self.E21:
            return f"{self.sigla}_{self.E21[clave]}_{self.fecha_archivo}"
        return f"{self.prefijo}_{self.sigla}_COSTOS_VENTA_{self.fecha_archivo}"

    def nombre_planilla(self):
        if self.instancia == "final":
            return f"{self.sigla}_ModeloFinanciero_3_{self.fecha_archivo}.xlsx"
        return f"{self.prefijo}_{self.sigla}_PLANILLA_{self.fecha_archivo}.xlsx"

    def nombre_zip_economico(self):
        # FEP01, Artículo 51.3: SOBRE3_[EMPRESA]_OFERTA_ECONOMICA_AAAAMMDD.ZIP
        return f"SOBRE3_{self.sigla}_OFERTA_ECONOMICA_{self.fecha_archivo}.ZIP"


def guardar_json(ruta, datos):
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(datos, f, ensure_ascii=False, indent=2)


def leer_json(ruta, defecto=None):
    try:
        with open(ruta, encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError):
        return defecto
