#!/usr/bin/env python3
"""Arma CREDITOS.md con la ficha de cada ícono (terceros.json y propios.py) y las
figuras que lo usan, leídas de los SVG generados."""
import glob
import json
import os
import re

RAIZ = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import propios  # noqa: E402

uso = {}
for svg in sorted(glob.glob(os.path.join(RAIZ, "*", "*.svg"))):
    if "/iconos/" in svg:
        continue
    fig = os.path.relpath(svg, RAIZ)[:-4]
    for k in set(re.findall(r'<symbol id="ic-([^"]+)"', open(svg, encoding="utf-8").read())):
        uso.setdefault(k, []).append(fig)
ter = json.load(open(os.path.join(RAIZ, "iconos", "terceros.json"), encoding="utf-8"))

o = ["# Créditos de los íconos", "",
     "Cada ícono está en `iconos/` con el nombre de la primera columna. Los de terceros se usan sin",
     "deformar, recortar ni recolorear; en las figuras solo cambia su tamaño. Las marcas de los",
     "productos (Azure, Flutter, React, Next.js, .NET, Go, PostgreSQL, Redis, SQLite, Apache Kafka,",
     "TimescaleDB) pertenecen a sus dueños y aparecen porque son productos de la solución.", "",
     "## Íconos de terceros", "",
     "| Archivo | Ícono | Autor | Licencia | Fuente | Figuras |", "|---|---|---|---|---|---|"]
for k in sorted(ter):
    d = ter[k]
    figs = ", ".join(f"`{x.split('/')[-1]}`" for x in uso.get(k, [])) or "No se usa (queda de reserva)"
    o.append(f"| `{k}.svg` | {d['nombre']} | {d['autor']} | {d['licencia']} | {d.get('pagina', d['url'])} | {figs} |")
o += ["", "Paquetes oficiales de Microsoft:", "",
      "- Azure Architecture Icons V24: https://arch-center.azureedge.net/icons/Azure_Public_Service_Icons_V24.zip,",
      "  publicado en https://learn.microsoft.com/azure/architecture/icons/",
      "- Microsoft Entra architecture icons (octubre de 2023):",
      "  https://learn.microsoft.com/entra/architecture/architecture-icons", "",
      "## Íconos propios", "",
      "Ningún set abierto trae router, switch, firewall, rack, UPS, generador, clima de precisión,",
      "lectores, gabinete o semirremolque en un estilo plano coherente con Fluent Emoji, así que se",
      "dibujaron para esta entrega con la paleta de Fluent Emoji (`fuente/propios.py`). No copian",
      "fotos ni logos de fabricantes: el modelo va como nombre bajo el ícono.", "",
      f"Licencia: {propios.CREDITO}.", "",
      "| Archivo | Representa | Figuras |", "|---|---|---|"]
QUE = {"pr-router": "Router 5G (RUTX50)", "pr-switch": "Switch (TSW202, FortiSwitch)",
       "pr-firewall": "Firewall (FortiGate 90G)", "pr-servidor": "Servidores en rack (Dell R360)",
       "pr-rack": "Rack de 24 U", "pr-ups": "UPS", "pr-generador": "Grupo electrógeno",
       "pr-clima": "Clima de precisión", "pr-camara": "Cámara de videovigilancia",
       "pr-lector-tarjeta": "Lector de tarjeta DESFire", "pr-lector-facial": "Lector facial",
       "pr-antena": "Red celular (antena)", "pr-wifi": "Punto de acceso Wi-Fi (FortiAP 234G)",
       "pr-ble": "Lector Bluetooth de portería (Minew G1)", "pr-pc-industrial": "Computador industrial (Karbon 430)",
       "pr-g26i": "Computador vehicular (iWave G26I)", "pr-can": "Lector CAN sin contacto",
       "pr-iridium": "Módem satelital (Iridium Edge)", "pr-baliza": "Baliza Bluetooth (EYE Sensor)",
       "pr-gabinete": "Gabinete de terminal", "pr-vesda": "Detección por aspiración (VESDA)",
       "pr-transferencia": "Tablero de transferencia", "pr-cola": "Cola de mensajes",
       "pr-cortacircuito": "Cortacircuito", "pr-semirremolque": "Semirremolque refrigerado",
       "pr-tracto": "Tractocamión", "pr-servicio": "Servicio de negocio", "pr-adaptador": "Adaptador, capa anticorrupción",
       "pr-transformador": "Transformador de esquemas", "pr-reconciliador": "Reconciliador",
       "pr-memoria": "Memoria eMMC o búfer", "pr-rastreador": "Rastreador GPS (plataformas de terceros)",
       "pr-pod": "Pod de contenedores", "pr-barrera": "Barrera de portería", "pr-medidor": "Medidor de envíos por segundo",
       "pr-aleta": "Antena de aleta LTE y GNSS", "pr-volante": "Volante (distintivo del conductor)"}
for k in sorted(propios.I):
    figs = ", ".join(f"`{x.split('/')[-1]}`" for x in uso.get(k, [])) or "No se usa"
    o.append(f"| `{k}.svg` | {QUE.get(k, k)} | {figs} |")
comp = json.load(open(os.path.join(RAIZ, "iconos", "compuestos.json"), encoding="utf-8"))
o += ["", "## Íconos compuestos", "",
      "Cada rol es una persona de Fluent Emoji con un distintivo chico (otro emoji de Fluent o un ícono propio)",
      "en un círculo blanco, para que los roles se distingan entre sí (`fuente/roles.py`). Son obras derivadas",
      "de Fluent Emoji, licencia MIT, y de los íconos propios.", "",
      "| Archivo | Qué combina | Figuras |", "|---|---|---|"]
import roles  # noqa: E402
for k in sorted(comp):
    base, badge, _ = roles.ROLES[k]
    figs = ", ".join(f"`{x.split('/')[-1]}`" for x in uso.get(k, [])) or "No se usa"
    o.append(f"| `{k}.svg` | {comp[k]}: `{base}.svg`" + (f" con `{badge}.svg`" if badge else "") + f" | {figs} |")
open(os.path.join(RAIZ, "CREDITOS.md"), "w", encoding="utf-8").write("\n".join(o) + "\n")
print("CREDITOS.md:", len(ter), "de terceros y", len(propios.I), "propios")
