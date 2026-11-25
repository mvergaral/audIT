#!/usr/bin/env python3
"""Selecciona los PDF de Informe 2 y arma un ZIP sin archivos de trabajo."""
import json
import shutil
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
from comun import Config

RAIZ = Path(__file__).resolve().parents[1]

def preparar():
    cfg = Config()
    if cfg.instancia != 'informe2':
        raise ValueError('Esta selección corresponde exclusivamente al Informe 2')
    salida = RAIZ / 'salida'
    origen = salida / 'informe2'
    manifiesto = json.loads((origen / 'manifiesto.json').read_text())
    claves = {'00', '01A', '02A'}
    for n in cfg.lista():
        claves.add(f'{n:02d}')
        claves.update(f'{n:02d}{f}' for f in cfg.subdocs[n]['formularios'])
    archivos = {a['clave']: a for a in manifiesto['archivos']}
    if set(archivos) != claves or len(archivos) != len(manifiesto['archivos']):
        raise ValueError('El manifiesto no coincide con los documentos de la entrega')
    if archivos['00']['nombre'] != cfg.nombre_caratula() + '.pdf':
        raise ValueError('La carátula no corresponde a la fecha de entrega vigente')
    seleccion = [origen / a['nombre'] for a in manifiesto['archivos']]
    seleccion.append(origen / 'Tabla-Art46-Informe2.pdf')
    if len({p.name for p in seleccion}) != len(seleccion):
        raise ValueError('Nombres de archivo duplicados')
    for p in seleccion:
        if p.suffix != '.pdf' or not p.is_file():
            raise ValueError(f'PDF ausente: {p.name}')
    destino = salida / f'Entrega-Informe2-{cfg.fecha_archivo}'
    destino.mkdir(exist_ok=True)
    anteriores = {p.name for p in destino.iterdir()}
    if anteriores - {p.name for p in seleccion}:
        raise ValueError('La carpeta de entrega contiene archivos ajenos a la selección')
    for p in seleccion:
        shutil.copy2(p, destino / p.name)
    paquete = salida / cfg.nombre_zip()
    with ZipFile(paquete, 'w', ZIP_DEFLATED) as z:
        for p in seleccion:
            z.write(destino / p.name, p.name)
    with ZipFile(paquete) as z:
        assert len(z.namelist()) == len(seleccion)
        assert all(n.endswith('.pdf') for n in z.namelist())
        assert z.testzip() is None
    guia = salida / f'ARCHIVOS-PARA-SUBIR-INFORME2-{cfg.fecha_archivo}.md'
    grupos = {
        'Carátula y tabla consolidada': [cfg.nombre_caratula() + '.pdf', 'Tabla-Art46-Informe2.pdf'],
        'Subdocumentos': [cfg.nombre_subdoc(n) + '.pdf' for n in cfg.lista()],
        'Formularios': [cfg.nombre_formulario(f) + '.pdf' for n in cfg.lista() for f in cfg.subdocs[n]['formularios']],
        'Anexos': ['AUDIT-Subdocumento1-Anexos.pdf', 'AUDIT-Subdocumento2-Anexos.pdf'],
    }
    contenido = '# Archivos para subir — Informe 2 — 12 de octubre de 2026\n\n'
    contenido += f'Entrega completa del equipo: **{len(seleccion)} PDF**. El archivo `{paquete.name}` contiene únicamente estos PDF. La carpeta `{destino.name}` permite revisarlos individualmente.\n\n'
    for titulo, nombres in grupos.items():
        contenido += '## ' + titulo + '\n\n' + '\n'.join('- `' + n + '`' for n in nombres) + '\n\n'
    contenido += '## Si se comparte únicamente el trabajo de D1\n\n'
    contenido += 'S1 y sus anexos, S2 y sus anexos, S9, T-6, T-13 y T-17; además, S13 y T-19 completos e integrados con las otras innovaciones. La carátula y la tabla consolidada son compartidas. El ZIP `Revision-D1-Informe2-20261012.zip` contiene esos 12 PDF para revisión interna y no reemplaza la entrega completa.\n\n'
    contenido += 'No subir Markdown, manifiestos JSON, registros de verificación, fuentes LaTeX, imágenes sueltas ni versiones anteriores. S10, S11, S12 y S14 no corresponden a esta instancia. La fecha de entrega se actualizó por instrucción del usuario respecto de la reprogramación del profesor; los documentos oficiales históricos se conservan.\n'
    guia.write_text(contenido)
    print(f'{len(seleccion)} PDF seleccionados; ZIP {paquete.name}; {paquete.stat().st_size / 1024 / 1024:.1f} MB')
    return destino, paquete, guia

if __name__ == '__main__':
    preparar()
