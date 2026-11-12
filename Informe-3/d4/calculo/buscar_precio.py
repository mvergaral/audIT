#!/usr/bin/env python3
"""Busca en azure_precios/<archivo>.json las líneas cuyo texto contiene todas las palabras dadas.
  python3 buscar_precio.py pg_cc "Storage" "Data Stored" """
import json, os, sys
d = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "azure_precios", sys.argv[1] + ".json"), encoding="utf-8"))
for i in d["items"]:
    txt = f'{i["productName"]} | {i["skuName"]} | {i["meterName"]}'
    if all(p.lower() in txt.lower() for p in sys.argv[2:]):
        print(f'{txt} | {i["retailPrice"]} | {i["unitOfMeasure"]} | {i["type"]} | tier {i["tierMinimumUnits"]}')
