#!/usr/bin/env python3
"""Baja los íconos de terceros a graficos-nuevos/iconos/ y deja su ficha en
iconos/terceros.json (nombre, URL, autor, licencia). CREDITOS.md se arma desde
esa ficha y desde los íconos propios (propios.py).

Azure y Entra salen de los paquetes oficiales de Microsoft, que se bajan una vez
y se descomprimen en una carpeta temporal (argumento 1).
"""
import json
import os
import shutil
import sys
import urllib.parse
import urllib.request

AQUI = os.path.dirname(os.path.abspath(__file__))
ICONOS = os.path.join(AQUI, "..", "iconos")
TMP = sys.argv[1] if len(sys.argv) > 1 else "/tmp/iconos-audit"

AZ_ZIP = "https://arch-center.azureedge.net/icons/Azure_Public_Service_Icons_V24.zip"
AZ_PAG = "https://learn.microsoft.com/azure/architecture/icons/"
ENTRA_ZIP = ("https://download.microsoft.com/download/3/1/a/31a56038-856a-4489-88e4-ee5a1c4352be/"
             "Microsoft%20Entra%20architecture%20icons%20-%20Oct%202023.zip")
AZ_LIC = ("Microsoft, Azure Architecture Icons V24. Uso permitido en diagramas de arquitectura "
          "según los términos del paquete (Microsoft_Terms_of_Use.pdf), sin deformar ni recolorear")
ENTRA_LIC = ("Microsoft, Microsoft Entra architecture icons (oct. 2023). Uso permitido en diagramas "
             "según los términos del paquete (Microsoft Terms of Use.docx)")

AZURE = {
    "az-frontdoor": "web/10073-icon-service-Front-Door-and-CDN-Profiles.svg",
    "az-apim": "web/10042-icon-service-API-Management-Services.svg",
    "az-iothub": "iot/10182-icon-service-IoT-Hub.svg",
    "az-dps": "iot/10369-icon-service-Device-Provisioning-Services.svg",
    "az-deviceupdate": "other/02475-icon-service-Device-Update-IoT-Hub.svg",
    "az-eventhubs": "analytics/00039-icon-service-Event-Hubs.svg",
    "az-aks": "containers/10023-icon-service-Kubernetes-Services.svg",
    "az-postgres": "databases/10131-icon-service-Azure-Database-PostgreSQL-Server.svg",
    "az-storage": "storage/10086-icon-service-Storage-Accounts.svg",
    "az-datalake": "storage/10090-icon-service-Data-Lake-Storage-Gen1.svg",
    "az-keyvault": "security/10245-icon-service-Key-Vaults.svg",
    "az-monitor": "monitor/00001-icon-service-Monitor.svg",
    "az-loganalytics": "monitor/00009-icon-service-Log-Analytics-Workspaces.svg",
    "az-firewall": "networking/10084-icon-service-Firewalls.svg",
    "az-vpngw": "networking/10063-icon-service-Virtual-Network-Gateways.svg",
    "az-expressroute": "networking/10079-icon-service-ExpressRoute-Circuits.svg",
    "az-bastion": "networking/02422-icon-service-Bastions.svg",
    "az-vnet": "networking/10061-icon-service-Virtual-Networks.svg",
    "az-subnet": "networking/02742-icon-service-Subnet.svg",
    "az-nsg": "networking/10067-icon-service-Network-Security-Groups.svg",
    "az-subscription": "general/10002-icon-service-Subscriptions.svg",
    "az-region": "general/10116-icon-service-Region-Management.svg",
    "az-redis": "databases/10137-icon-service-Cache-Redis.svg",
    "az-privateendpoint": "other/02579-icon-service-Private-Endpoints.svg",
    "az-routetable": "networking/10082-icon-service-Route-Tables.svg",
}
ENTRA = {"entra-id": "Microsoft Entra color icons SVG/Microsoft Entra ID color icon.svg"}

DEVICON = "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/{0}/{0}-{1}.svg"
DEV = {
    "dev-flutter": ("flutter", "original"), "dev-react": ("react", "original"),
    "dev-nextjs": ("nextjs", "original"), "dev-dotnet": ("dotnetcore", "original"),
    "dev-go": ("go", "original-wordmark"), "dev-postgresql": ("postgresql", "original"),
    "dev-redis": ("redis", "original"), "dev-sqlite": ("sqlite", "original"),
    "dev-kafka": ("apachekafka", "original"), "dev-linux": ("linux", "original"),
    "dev-azure": ("azure", "original"),
    "dev-git": ("git", "original"),
}
FLUENT = "https://cdn.jsdelivr.net/gh/microsoft/fluentui-emoji@main/assets/{}/{}"
FLU = {
    "flu-camion": ("Articulated lorry", "Flat/articulated_lorry_flat.svg"),
    "flu-edificio-publico": ("Classical building", "Flat/classical_building_flat.svg"),
    "flu-empresa": ("Office building", "Flat/office_building_flat.svg"),
    "flu-combustible": ("Fuel pump", "Flat/fuel_pump_flat.svg"),
    "flu-peaje": ("Motorway", "Flat/motorway_flat.svg"),
    "flu-fabrica": ("Factory", "Flat/factory_flat.svg"),
    "flu-satelite": ("Satellite", "Flat/satellite_flat.svg"),
    "flu-internet": ("Globe with meridians", "Flat/globe_with_meridians_flat.svg"),
    "flu-movil": ("Mobile phone", "Flat/mobile_phone_flat.svg"),
    "flu-portal": ("Laptop", "Flat/laptop_flat.svg"),
    "flu-consola": ("Desktop computer", "Flat/desktop_computer_flat.svg"),
    "flu-tablero": ("Bar chart", "Flat/bar_chart_flat.svg"),
    "flu-autoservicio": ("Chart increasing", "Flat/chart_increasing_flat.svg"),
    "flu-repuestos": ("Package", "Flat/package_flat.svg"),
    "flu-extintor": ("Fire extinguisher", "Flat/fire_extinguisher_flat.svg"),
    "flu-agua": ("Droplet", "Flat/droplet_flat.svg"),
    "flu-contable": ("Ledger", "Flat/ledger_flat.svg"),
    "flu-gestion2013": ("Card file box", "Flat/card_file_box_flat.svg"),
    "flu-ubicacion": ("Round pushpin", "Flat/round_pushpin_flat.svg"),
    "flu-documento": ("Page facing up", "Flat/page_facing_up_flat.svg"),
    "flu-tarjeta": ("Identification card", "Flat/identification_card_flat.svg"),
    "flu-candado": ("Locked", "Flat/locked_flat.svg"),
    "flu-reloj": ("Stopwatch", "Flat/stopwatch_flat.svg"),
    "flu-parador": ("Bed", "Flat/bed_flat.svg"),
    "flu-engranaje": ("Gear", "Flat/gear_flat.svg"),
    "flu-peligro": ("Warning", "Flat/warning_flat.svg"),
    "flu-campana": ("Bell", "Flat/bell_flat.svg"),
    "flu-hombre": ("Man", "Medium-Light/Flat/man_flat_medium-light.svg"),
    "flu-audifonos": ("Headphone", "Flat/headphone_flat.svg"),
    "flu-maletin": ("Briefcase", "Flat/briefcase_flat.svg"),
    "flu-portapapeles": ("Clipboard", "Flat/clipboard_flat.svg"),
    "flu-obrero": ("Construction worker", "Medium-Light/Flat/construction_worker_flat_medium-light.svg"),
    "flu-usuarios": ("Busts in silhouette", "Flat/busts_in_silhouette_flat.svg"),
    "flu-acuerdo": ("Handshake", "Flat/handshake_flat.svg"),
    "flu-sello": ("Rosette", "Flat/rosette_flat.svg"),
    "flu-corona": ("Crown", "Flat/crown_flat.svg"),
    "flu-enchufe": ("Electric plug", "Flat/electric_plug_flat.svg"),
    "flu-bateria": ("Battery", "Flat/battery_flat.svg"),
    "flu-bitacora": ("Scroll", "Flat/scroll_flat.svg"),
    "flu-antena-tierra": ("Satellite antenna", "Flat/satellite_antenna_flat.svg"),
    "flu-espera": ("Hourglass not done", "Flat/hourglass_not_done_flat.svg"),
    "flu-reintento": ("Counterclockwise arrows button", "Flat/counterclockwise_arrows_button_flat.svg"),
    "flu-conductor": ("Person", "Medium-Light/Flat/person_flat_medium-light.svg"),
    "flu-operador": ("Technologist", "Medium-Light/Flat/technologist_flat_medium-light.svg"),
    "flu-taller": ("Mechanic", "Medium-Light/Flat/mechanic_flat_medium-light.svg"),
    "flu-transportista": ("Office worker", "Medium-Light/Flat/office_worker_flat_medium-light.svg"),
    "flu-cliente": ("Woman office worker", "Medium-Light/Flat/woman_office_worker_flat_medium-light.svg"),
    "flu-gerencia": ("Man office worker", "Medium-Light/Flat/man_office_worker_flat_medium-light.svg"),
}
FLUENT_UI = "https://cdn.jsdelivr.net/gh/microsoft/fluentui-system-icons@main/assets/{}"
FUI = {"fui-codigo": "Code/SVG/ic_fluent_code_24_color.svg"}
SIMPLE = {"si-timescale": ("timescale", "#FDB515")}


def bajar(url, destino):
    req = urllib.request.Request(url, headers={"User-Agent": "audit-graficos/1.0"})
    with urllib.request.urlopen(req) as r, open(destino, "wb") as f:
        f.write(r.read())


def main():
    os.makedirs(ICONOS, exist_ok=True)
    os.makedirs(TMP, exist_ok=True)
    ficha = {}
    az = os.path.join(TMP, "azure")
    if not os.path.isdir(az):
        bajar(AZ_ZIP, os.path.join(TMP, "az.zip"))
        shutil.unpack_archive(os.path.join(TMP, "az.zip"), az)
    base = os.path.join(az, "Azure_Public_Service_Icons", "Icons")
    for k, rel in AZURE.items():
        shutil.copy(os.path.join(base, rel), os.path.join(ICONOS, k + ".svg"))
        ficha[k] = dict(nombre=os.path.basename(rel), url=AZ_ZIP, pagina=AZ_PAG, autor="Microsoft",
                        licencia=AZ_LIC)
    en = os.path.join(TMP, "entra")
    if not os.path.isdir(en):
        bajar(ENTRA_ZIP, os.path.join(TMP, "entra.zip"))
        shutil.unpack_archive(os.path.join(TMP, "entra.zip"), en)
    for k, rel in ENTRA.items():
        shutil.copy(os.path.join(en, "Microsoft Entra architecture icons - Oct 2023", rel),
                    os.path.join(ICONOS, k + ".svg"))
        ficha[k] = dict(nombre=os.path.basename(rel), url=ENTRA_ZIP,
                        pagina="https://learn.microsoft.com/entra/architecture/architecture-icons",
                        autor="Microsoft", licencia=ENTRA_LIC)
    for k, (n, v) in DEV.items():
        url = DEVICON.format(n, v)
        bajar(url, os.path.join(ICONOS, k + ".svg"))
        ficha[k] = dict(nombre=f"{n}-{v}.svg", url=url, autor="Proyecto Devicon y colaboradores",
                        licencia="MIT. Las marcas pertenecen a sus dueños")
    for k, (n, rel) in FLU.items():
        url = FLUENT.format(urllib.parse.quote(n), rel)
        bajar(url, os.path.join(ICONOS, k + ".svg"))
        ficha[k] = dict(nombre=f"Fluent Emoji «{n}», estilo plano", url=url, autor="Microsoft",
                        licencia="MIT")
    for k, rel in FUI.items():
        url = FLUENT_UI.format(rel)
        bajar(url, os.path.join(ICONOS, k + ".svg"))
        ficha[k] = dict(nombre="Fluent UI System Icons «Code», variante color", url=url,
                        autor="Microsoft", licencia="MIT")
    for k, (slug, color) in SIMPLE.items():
        url = f"https://cdn.jsdelivr.net/npm/simple-icons@latest/icons/{slug}.svg"
        dest = os.path.join(ICONOS, k + ".svg")
        bajar(url, dest)
        t = open(dest, encoding="utf-8").read().replace("<path ", f'<path fill="{color}" ', 1)
        open(dest, "w", encoding="utf-8").write(t)
        ficha[k] = dict(nombre=f"Simple Icons «{slug}», con el color de marca {color} que publica el proyecto",
                        url=url, autor="Proyecto Simple Icons y colaboradores",
                        licencia="CC0 1.0. La marca pertenece a su dueño")
    with open(os.path.join(ICONOS, "terceros.json"), "w", encoding="utf-8") as f:
        json.dump(ficha, f, ensure_ascii=False, indent=1)
    print(len(ficha), "íconos de terceros")


if __name__ == "__main__":
    main()
