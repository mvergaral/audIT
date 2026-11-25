#!/usr/bin/env python3
"""Recupera las figuras PDF de S4/S7/S8/S13 desde SVG versionados.

Ejecutar desde cualquier carpeta: python3 herramientas/recuperar_figuras.py.
No crea sustitutos para figuras cuya fuente no está disponible.
"""
from pathlib import Path
import re
import subprocess

FORMATO = Path(__file__).resolve().parents[1]
REPO = FORMATO.parents[1]
D3 = REPO / "Informe-2/D3/graficos"
D4 = REPO / "Informe-2/D4/graficos-v2"
ALIAS = {
    "04-arquitectura/secuencia-asignacion.pdf": D3 / "4-3-asignacion.svg",
    "04-arquitectura/secuencia-documento.pdf": D3 / "4-4-documento.svg",
    "04-arquitectura/secuencia-liquidacion.pdf": D3 / "4-6-liquidacion.svg",
    "04-arquitectura/secuencia-reconexion.pdf": D3 / "4-7-reconexion.svg",
    "04-arquitectura/documento-sin-cobertura.pdf": D3 / "documento-sin-cobertura.svg",
    "13-innovaciones/cartera.pdf": D3 / "13-cartera.svg",
}
CARPETAS = ["04-arquitectura", "07-plan-trabajo", "08-riesgos", "13-innovaciones"]


def main():
    referencias = set()
    for carpeta in CARPETAS:
        for fuente in (FORMATO / "subdocumentos" / carpeta).rglob("*.tex"):
            referencias.update(re.findall(r"figuras/([^{}\s]+\.pdf)", fuente.read_text()))
    pendientes = []
    for relativa in sorted(referencias):
        destino = FORMATO / "figuras" / relativa
        candidatos = [ALIAS.get(relativa), D4 / Path(relativa).with_suffix(".svg"),
                      destino.with_suffix(".svg")]
        fuente = next((p for p in candidatos if p and p.is_file()), None)
        if fuente is None:
            pendientes.append(relativa)
            continue
        destino.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run(["rsvg-convert", "-f", "pdf", "-o", str(destino), str(fuente)], check=True)
        print(f"RECUPERADA {relativa} <- {fuente.relative_to(REPO)}")
    for pendiente in pendientes:
        print(f"FALTA FUENTE ORIGINAL: {pendiente}")
    return int(bool(pendientes))


if __name__ == "__main__":
    raise SystemExit(main())
