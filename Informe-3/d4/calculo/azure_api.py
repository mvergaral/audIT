#!/usr/bin/env python3
"""Consulta la API pública de precios minoristas de Azure y guarda la respuesta.

  python3 azure_api.py "<filtro OData>" [nombre]

Ejemplo:
  python3 azure_api.py "serviceName eq 'IoT Hub' and armRegionName eq 'chilecentral'" iothub_cc

Guarda azure_precios/<nombre>.json con todas las páginas y la fecha de consulta, y muestra
productName | skuName | meterName | precio | unidad | tipo.
"""
import datetime
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

BASE = "https://prices.azure.com/api/retail/prices"
AQUI = os.path.dirname(os.path.abspath(__file__))


def consultar(filtro):
    url = BASE + "?" + urllib.parse.urlencode({"$filter": filtro})
    items = []
    while url:
        for intento in range(8):
            try:
                with urllib.request.urlopen(url, timeout=60) as r:
                    d = json.load(r)
                break
            except urllib.error.HTTPError as e:
                if e.code != 429:
                    raise
                time.sleep(5 * (intento + 1))
        else:
            raise RuntimeError("la API sigue limitando las consultas")
        items += d.get("Items", [])
        url = d.get("NextPageLink")
    return items


if __name__ == "__main__":
    filtro = sys.argv[1]
    nombre = sys.argv[2] if len(sys.argv) > 2 else "consulta"
    items = consultar(filtro)
    os.makedirs(os.path.join(AQUI, "azure_precios"), exist_ok=True)
    with open(os.path.join(AQUI, "azure_precios", nombre + ".json"), "w", encoding="utf-8") as f:
        json.dump({"consultado": datetime.date.today().isoformat(), "filtro": filtro, "items": items},
                  f, ensure_ascii=False, indent=1)
    for i in sorted(items, key=lambda x: (x["productName"], x["skuName"], x["meterName"])):
        print(f'{i["productName"]} | {i["skuName"]} | {i["meterName"]} | {i["retailPrice"]} | '
              f'{i["unitOfMeasure"]} | {i["type"]} | {i.get("reservationTerm", "")} | tier {i["tierMinimumUnits"]}')
