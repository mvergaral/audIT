#!/usr/bin/env python3
"""Compila el diccionario independiente de S5 con la clase oficial."""

from pathlib import Path
import shutil
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "herramientas"))
import compilar  # noqa: E402


def main() -> int:
    nombre = "AUDIT-Subdocumento5-Anexos"
    instancia = compilar.Config().instancia
    trabajo = compilar.Trabajo(
        "05A",
        "anexo.tex",
        nombre,
        str(ROOT / "salida" / "aux" / instancia / "05A"),
        compilar.OFERTA.preambulo() + r"\def\NumeroSubdoc{5}",
        [str(ROOT / "subdocumentos" / "05-datos")],
    )
    trabajo.compilar(True)
    if not trabajo.ok:
        compilar.mostrar_error(trabajo)
        return 1
    destino = ROOT / "salida" / f"borrador-{instancia}-d3" / f"{nombre}.pdf"
    destino.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(trabajo.pdf, destino)
    print(f"{destino}: {trabajo.paginas} páginas")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
