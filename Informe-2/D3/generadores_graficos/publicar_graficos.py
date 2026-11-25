#!/usr/bin/env python3
"""Publica los gráficos canónicos de D3 en el formato oficial de la oferta.

Las fuentes PNG/SVG están en D3/graficos (selección del commit f86e240).
Los PDF se derivan del SVG de D3 o se toman de las versiones vectoriales
de los mismos diagramas conservadas en graficos-v2.
"""
from pathlib import Path
import shutil
import subprocess

REPO = Path(__file__).resolve().parents[3]
FUENTES = REPO / 'Informe-2/D3/graficos'
DESTINO = REPO / 'recursos/Formato-Oferta-audIT/figuras'
VECTORES_S4 = REPO / 'Informe-2/D4/graficos-v2/04-arquitectura'
PDF_VECTORIALES = {
    'audit-figura-4.2-contextos': 'LogicaContextos.pdf',
    'audit-figura-4.3-resiliencia': 'D3-diagrama11_patrones_resiliencia_despacho.pdf',
    'LogicaIntegraciones': 'LogicaIntegraciones.pdf',
    'audit-figura-4.4-acl': 'D3-diagrama12_integracion_acl_erp2013.pdf',
    'audit-figura-4.5-analitica': 'D3-diagrama13_arquitectura_analitica_lakehouse_bi.pdf',
    'audit-figura-4.6-tactico': 'D3-diagrama2_arquitectura_tactica_ddd.pdf',
}

EQUIVALENCIAS = {
    'LogicaCapas': ['_LogicaCapas', 'diagrama10_arquitectura_logica_8capas', 'esquema_conceptual_solucion'],
    'audit-figura-4.2-contextos': ['LogicaContextos', 'diagrama1_bounded_contexts'],
    'audit-figura-4.3-resiliencia': ['diagrama11_patrones_resiliencia_despacho'],
    'audit-figura-4.4-acl': ['diagrama12_integracion_acl_erp2013'],
    'audit-figura-4.5-analitica': ['diagrama13_arquitectura_analitica_lakehouse_bi'],
    'audit-figura-4.6-tactico': ['diagrama2_arquitectura_tactica_ddd'],
    '4-3-asignacion': ['secuencia-asignacion'],
    '4-4-documento': ['secuencia-documento'],
    '4-6-liquidacion': ['secuencia-liquidacion'],
    '4-7-reconexion': ['secuencia-reconexion'],
    'documento-sin-cobertura': [],
    'audit-figura-5.1-erd': ['diagrama5_modelo_erd_persistencia'],
    'audit-figura-5.2-mdm': ['diagrama8_gestion_datos_maestros_mdm'],
    'audit-figura-5.3-cap': ['diagrama3_teorema_cap'],
    'audit-figura-5.4-cdc': ['diagrama7_oltp_olap_cdc'],
    'audit-figura-5.5-migracion': ['diagrama6_migracion_datos'],
    'audit-figura-5.6-desempeno': ['diagrama9_estrategia_desempeno'],
    '5-2-custodia': [], '5-3-permisos': [], '5-7-evidencia': [],
    '6-1-hitos': [], '6-2-pipeline': [],
    '13-cartera': ['cartera'],
    '13-2-intervenciones': ['intervenciones'],
    'LogicaIntegraciones': ['_LogicaIntegraciones'],
}
ALIAS = {}
for nombre, variantes in EQUIVALENCIAS.items():
    for variante in [nombre, *variantes]:
        ALIAS[variante] = nombre
        if variante.startswith('diagrama'):
            ALIAS['D3-' + variante] = nombre


def carpeta(nombre):
    if nombre.startswith('13-'):
        return '13-innovaciones'
    if nombre.startswith(('5-', 'audit-figura-5.')):
        return '05-datos'
    if nombre.startswith('6-'):
        return '06-metodologias'
    return '04-arquitectura'


def ruta_oficial(nombre):
    vectorial = nombre in PDF_VECTORIALES or (FUENTES / (nombre + '.svg')).exists()
    extension = '.pdf' if vectorial else '.png'
    return DESTINO / carpeta(nombre) / (nombre + extension)


def copiar_version_canonica(base):
    """Sustituye una copia reconocida y devuelve su nombre canónico, o None."""
    base = Path(base)
    nombre = ALIAS.get(base.name)
    if nombre is None:
        return None
    base.parent.mkdir(parents=True, exist_ok=True)
    for extension in ('.png', '.svg'):
        origen = FUENTES / (nombre + extension)
        destino = Path(str(base) + extension)
        if origen.exists():
            if origen.resolve() != destino.resolve():
                shutil.copy2(origen, destino)
        elif destino.exists():
            destino.unlink()
    svg = FUENTES / (nombre + '.svg')
    pdf = Path(str(base) + '.pdf')
    if svg.exists():
        subprocess.run(['rsvg-convert', '-f', 'pdf', '-o', str(pdf), str(svg)], check=True)
    elif nombre in PDF_VECTORIALES:
        shutil.copy2(VECTORES_S4 / PDF_VECTORIALES[nombre], pdf)
    elif pdf.exists():
        pdf.unlink()
    return nombre


def publicar():
    for nombre in EQUIVALENCIAS:
        copiar_version_canonica(DESTINO / carpeta(nombre) / nombre)
    vectoriales = sum(ruta_oficial(nombre).suffix == '.pdf' for nombre in EQUIVALENCIAS)
    print(f'Publicados {len(EQUIVALENCIAS)} gráficos de D3, {vectoriales} en PDF vectorial.')


if __name__ == '__main__':
    publicar()
