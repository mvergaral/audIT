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
    if "/iconos/" in svg or svg.endswith("-oficio.svg"):
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
HW = {"hw-fortiswitch": "FortiSwitch 124F-POE, 1 U", "hw-r360": "Dell PowerEdge R360, 1 U",
      "hw-proveedor": "Equipo de un proveedor de enlace, 1 U", "hw-patch": "Panel de conexión, 1 U",
      "hw-bandeja-fortigate": "Dos FortiGate 90G sobre una bandeja de 1 U", "hw-fortigate": "FortiGate 90G de escritorio",
      "hw-bandeja-grabador": "Grabador Axis S3008 Mk II sobre una bandeja de 1 U",
      "hw-ups-rack": "APC Smart-UPS SRT3000, 2 U", "hw-bateria-rack": "Batería externa SRT96RMBP, 2 U",
      "hw-rutx50": "Teltonika RUTX50 con sus antenas", "hw-tsw202": "Teltonika TSW202 en riel DIN",
      "hw-karbon": "OnLogic Karbon 430, sin ventilador", "hw-ups-torre": "APC Smart-UPS SRT1000XLI, torre",
      "hw-inyector": "Inyector PoE 802.3bt", "hw-fortiap": "FortiAP 234G de exterior",
      "hw-minew": "Lector de portería Minew G1", "hw-g26i": "Computador vehicular iWave G26I",
      "hw-iridium": "Módem satelital Iridium Edge", "hw-aleta": "Antena de aleta LTE y GNSS",
      "hw-can": "Technoton CANCrocodile sobre el arnés", "hw-desfire": "Lector de tarjeta DESFire",
      "hw-baliza": "Baliza Teltonika EYE Sensor", "hw-bateria": "Batería del camión",
      "hw-generador": "Grupo electrógeno insonorizado Himoinsa HYW-8", "hw-tablero": "Tablero de transferencia",
      "hw-clima": "Clima de precisión de cielo Liebert Mini-Mate2", "hw-camara": "Cámara de mini domo Axis M3215-LVE",
      "hw-facial": "Lector facial Suprema FaceStation F2", "hw-vesda": "Detector por aspiración VESDA VLF-250",
      "hw-cilindro": "Cilindro del agente FK-5-1-12", "hw-torre": "Torre de telefonía con antenas de panel",
      "hw-rack": "Rack cerrado de 24 U"}
o += ["", "## Ilustraciones de hardware", "",
      "Vista frontal de cada equipo del T-11, dibujada en vector para esta entrega a partir de la forma",
      "del modelo real (proporciones, puertos, luces y antenas), sin marca ni logo del fabricante",
      "(`fuente/hardware.py`). Se buscaron imágenes en Openclipart, que es de dominio público: no trae",
      "estos modelos y lo que trae es genérico y de estilos dispares, así que de ahí solo se tomó el",
      "satélite (`oc-satelite.svg`, en la tabla de terceros). Las fotos de los fabricantes tienen",
      "derechos y no se usaron.", "",
      "Licencia: dibujo propio de esta entrega, sin elementos de terceros ni marcas. Uso libre para el",
      "equipo audIT.", "",
      "| Archivo | Representa | Figuras |", "|---|---|---|"]
for ruta in sorted(glob.glob(os.path.join(RAIZ, "iconos", "hw-*.svg"))):
    k = os.path.basename(ruta)[:-4]
    figs = ", ".join(f"`{x.split('/')[-1]}`" for x in uso.get(k, [])) or "No se usa (queda de reserva)"
    o.append(f"| `{k}.svg` | {HW.get(k, k)} | {figs} |")
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
