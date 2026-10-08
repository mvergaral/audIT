#!/usr/bin/env python3
"""Íconos compuestos: una persona de Fluent Emoji con un distintivo chico abajo a la
derecha, para que cada rol se distinga, y el documento con sello de la innovación 1.
Son obras derivadas de Fluent Emoji (MIT) y de los íconos propios.

  python3 roles.py      escribe iconos/rol-*.svg e iconos/inn-*.svg
"""
import json
import os
import re

AQUI = os.path.dirname(os.path.abspath(__file__))
ICONOS = os.path.join(AQUI, "..", "iconos")

ROLES = {
    "rol-conductor": ("flu-conductor", "pr-volante", "Conductor: persona y volante"),
    "rol-operador": ("flu-operador", "flu-audifonos", "Operador de torre: persona frente a pantalla y audífonos"),
    "rol-taller": ("flu-taller", None, "Personal de terminal y taller: overol y llave"),
    "rol-transportista": ("flu-hombre", "flu-camion", "Transportista: dueño de camión"),
    "rol-cliente": ("flu-cliente", "flu-empresa", "Cliente: empresa"),
    "rol-gerencia": ("flu-gerencia", "flu-maletin", "Gerencia: maletín"),
    "rol-finanzas": ("flu-transportista", "flu-autoservicio", "Finanzas: gráfico"),
    "rol-operaciones": ("flu-obrero", "flu-portapapeles", "Operaciones: casco y lista"),
    "rol-usuarios": ("flu-usuarios", None, "Usuarios en general"),
    "inn-expediente": ("flu-documento", "flu-sello", "Documento con sello"),
}


def interior(clave, pre):
    t = open(os.path.join(ICONOS, clave + ".svg"), encoding="utf-8").read()
    t = re.sub(r"<\?xml.*?\?>|<!--.*?-->", "", t, flags=re.S)
    m = re.search(r"<svg\b([^>]*)>(.*)</svg>", t, re.S)
    attrs, cuerpo = m.group(1), m.group(2)
    vb = re.search(r'viewBox="([^"]+)"', attrs).group(1)
    for i in set(re.findall(r'\bid="([^"]+)"', cuerpo)):
        cuerpo = cuerpo.replace(f'id="{i}"', f'id="{pre}{i}"').replace(f"#{i})", f"#{pre}{i})") \
                       .replace(f'"#{i}"', f'"#{pre}{i}"')
    return vb, cuerpo


def main():
    for k, (base, badge, _) in ROLES.items():
        vb, cuerpo = interior(base, k + "-a-")
        partes = [f'<svg x="0" y="0" width="{27 if badge else 32}" height="{27 if badge else 32}" viewBox="{vb}">{cuerpo}</svg>']
        if badge:
            vb2, c2 = interior(badge, k + "-b-")
            partes.append('<circle cx="24.5" cy="24.5" r="7.4" fill="#FFFFFF" stroke="#B4ACBC" stroke-width="0.6"/>')
            partes.append(f'<svg x="18.8" y="18.8" width="11.4" height="11.4" viewBox="{vb2}">{c2}</svg>')
        open(os.path.join(ICONOS, k + ".svg"), "w", encoding="utf-8").write(
            '<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32">'
            + "".join(partes) + "</svg>\n")
    json.dump({k: v[2] for k, v in ROLES.items()}, open(os.path.join(ICONOS, "compuestos.json"), "w",
                                                         encoding="utf-8"), ensure_ascii=False, indent=1)
    print(len(ROLES), "íconos compuestos")


if __name__ == "__main__":
    main()
