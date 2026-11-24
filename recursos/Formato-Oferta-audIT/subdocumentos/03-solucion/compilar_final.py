"""Compila S3 y T-12 en modo final con salidas y auxiliares dentro de S3."""
from argparse import ArgumentParser
from pathlib import Path
import json
import os
import shutil
import subprocess

import fitz

HERE = Path(__file__).resolve().parent
BASE = HERE.parents[1]
OUTPUT = HERE / "preparacion-final"
BUILD = OUTPUT / "compilacion"
DOCUMENTS = (
    ("03", "subdocumento.tex", "SOBRE2_AUDIT_SUBDOC03_20261125"),
    ("03T-12", "formulario.tex", "AUDIT-Formulario-T-12"),
)


def title_paths(directory):
    yield from sorted(directory.rglob("*.aux"))


def external_assets(directory):
    for aux in title_paths(directory):
        if aux.parent == BUILD:
            continue
        match = None
        for index in range(1, 15):
            if aux.stem in (f"S{index:02d}", f"SOBRE2_AUDIT_SUBDOC{index:02d}_20261125"):
                match = f"S{index:02d}-"
                break
        if match:
            yield match, aux


def relative(path):
    return Path(os.path.relpath(path.resolve(), BASE)).as_posix()


def run(args, log, context):
    with log.open("w", encoding="utf-8") as stream:
        result = subprocess.run(
            args, cwd=BASE, env=context, stdin=subprocess.DEVNULL,
            stdout=stream, stderr=subprocess.STDOUT, check=False,
        )
    if result.returncode:
        print(log.read_text(encoding="utf-8", errors="replace")[-4500:])
        raise SystemExit(result.returncode)


def compile_one(key, template, stem, externals, env):
    declaration = [r"\def\RaizSubdocumentos{subdocumentos}", r"\def\NumeroSubdoc{3}",
                   r"\def\FolioInicialExterno{1}", r"\def\NombreArchivo{"+stem+"}",
                   r"\def\ArchivoActual{"+stem+"}"]
    if key == "03T-12":
        declaration.append(r"\def\FormularioActual{T-12}")
    if externals:
        ext = BUILD / (stem + "-externos.tex")
        tex = []
        for prefix, aux in externals.items():
            tex.extend([r"\RegistrarPrefijo{"+prefix+"}",
                        r"\externaldocument["+prefix+"]{"+relative(aux.with_suffix(""))+"}["+aux.stem+".pdf]"])
        ext.write_text("\n".join(tex)+"\n", encoding="utf-8")
        declaration.append(r"\def\ArchivoExternos{"+relative(ext)+"}")
    source = (BASE / template).read_text(encoding="utf-8")
    source = source.replace(r"\begin{document}", r"\AplicarInstancia{final}\Version{3.0}"+"\n"+r"\begin{document}", 1)
    wrapper = BUILD / (stem + ".tex")
    wrapper.write_text("\n".join(declaration)+"\n"+source, encoding="utf-8")

    cmd = ["lualatex", "-recorder", "--enable-installer", "-interaction=nonstopmode",
           "-halt-on-error", "-file-line-error", "-jobname="+stem,
           "-output-directory="+str(BUILD), str(wrapper)]
    for attempt in range(1,4):
        run(cmd, BUILD/(stem+f"-{attempt}.txt"), env)
        print(stem, "pasada", attempt, flush=True)
        if attempt == 1 and (BUILD/(stem+".bcf")).is_file():
            run(["biber", "--input-directory="+str(BUILD), "--output-directory="+str(BUILD), stem],
                BUILD/(stem+"-biber.txt"), env)
    path = OUTPUT/(stem+".pdf")
    shutil.copy2(BUILD/(stem+".pdf"), path)
    with fitz.open(path) as pdf:
        pages = len(pdf)
    return {
        "clave":key, "nombre":path.name, "folio_inicial":1, "paginas":pages,
        "aux":relative(BUILD/(stem+".aux")), "log":relative(BUILD/(stem+".log")),
        "fuentes":[["subdocumentos"], ["subdocumentos/03-solucion"]],
    }


def main():
    parser = ArgumentParser(__doc__)
    parser.add_argument("--fuentes", type=Path, help="Directorio local con los OTF de IBM Plex.")
    parser.add_argument("--auxiliares", type=Path, action="append", default=[],
                        help="Directorio con archivos AUX vigentes de otros subdocumentos.")
    parser.add_argument("--aux-t17", type=Path, help="Archivo AUX vigente del Formulario T-17.")
    args = parser.parse_args()
    BUILD.mkdir(parents=True, exist_ok=True)
    env = os.environ.copy()
    env["TEXINPUTS"] = os.pathsep.join(["."]+[
        (BASE/path).as_posix()+"//" for path in ("estilo","fuentes","temas","portadas","formularios","configuracion")
    ]+[""])
    if args.fuentes:
        if not (args.fuentes/"IBMPlexSerif-Regular.otf").is_file():
            parser.error("--fuentes debe contener los archivos OTF de IBM Plex")
        font_dir = args.fuentes.resolve().as_posix()
        env["OPENTYPEFONTS"] = font_dir+"//"+os.pathsep
        env["OSFONTDIR"] = font_dir
    external = dict(item for directory in args.auxiliares for item in external_assets(directory))
    if args.aux_t17:
        if not args.aux_t17.is_file():
            parser.error("--aux-t17 debe identificar un archivo AUX existente")
        external["T17-"] = args.aux_t17
    external.pop("S03-", None)
    entries = []
    for key, template, stem in DOCUMENTS:
        entries.append(compile_one(key,template,stem,external,env))
        if key == "03":
            external["S03-"] = BUILD/(stem+".aux")
    manifest = {"grupo":"final-s3-preparacion", "instancia":"final",
                "modo_folio":"subdocumento", "archivos":entries}
    (OUTPUT/"manifiesto.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2)+"\n", encoding="utf-8",
    )


if __name__ == "__main__":
    main()
