"""Evidencia independiente de lectura del paquete de Informe 3; no modifica la oferta."""
import csv
import hashlib
import json
import subprocess
import sys
from collections import Counter
from pathlib import Path
from zipfile import ZipFile
from io import BytesIO
import xml.etree.ElementTree as ET

import openpyxl
from pypdf import PdfReader

RAIZ = Path(__file__).resolve().parents[2]
SALIDA = Path(__file__).resolve().parent
PAQUETE = RAIZ / "outputs/informe3-integral/entrega-consolidada"
NS = {"a": "http://schemas.openxmlformats.org/drawingml/2006/main",
      "c": "http://schemas.openxmlformats.org/drawingml/2006/chart"}
informe = {"sha": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=RAIZ, text=True).strip(),
           "archivos": {}, "planillas": {}, "presentaciones": {}, "pdf": {}}

for ruta in sorted(PAQUETE.rglob("*")):
    if not ruta.is_file():
        continue
    relativo = str(ruta.relative_to(RAIZ))
    informe["archivos"][relativo] = {"sha256": hashlib.sha256(ruta.read_bytes()).hexdigest(),
                                   "bytes": ruta.stat().st_size}
    if ruta.suffix == ".pdf":
        lector = PdfReader(ruta)
        paginas = [p.extract_text() or "" for p in lector.pages]
        destino = SALIDA / (ruta.stem + ".txt")
        destino.write_text("\n\n".join(f"PÁGINA FÍSICA {n}\n{t}" for n,t in enumerate(paginas, 1)), encoding="utf-8")
        informe["pdf"][relativo] = {"paginas": len(paginas), "texto": str(destino.relative_to(RAIZ)),
                                   "academico": [n for n,t in enumerate(paginas,1) if "académic" in t.lower()],
                                   "paginas_con_UF": [n for n,t in enumerate(paginas,1) if "UF" in t]}
    if ruta.suffix == ".xlsx":
        formulas = openpyxl.load_workbook(ruta, data_only=False)
        valores = openpyxl.load_workbook(ruta, data_only=True)
        hojas = {}
        for hoja in formulas:
            cuentas = Counter("formula" if c.data_type == "f" else "numero" if isinstance(c.value,(float,int)) else "texto"
                              for fila in hoja for c in fila if c.value is not None)
            errores = [c.coordinate for fila in valores[hoja.title] for c in fila if c.data_type == "e"]
            hojas[hoja.title] = dict(filas=hoja.max_row, columnas=hoja.max_column,
                cuentas=dict(cuentas), errores=errores, protegida=hoja.protection.sheet,
                validaciones=len(hoja.data_validations.dataValidation), graficos=len(hoja._charts))
        claves = {h: {c: {"formula": formulas[h][c].value,"guardado":valores[h][c].value}
                     for c in cc}
                  for h,cc in {"Parámetros D2":["B4","B5","B6","B7","B8","B9","B10","B21"],
                     "Indicadores":["B2","B3","B10"],"Flujo de Caja":["R10","T10","W10"],
                     "Personal":["D22","D26"]}.items() if h in formulas.sheetnames}
        informe["planillas"][relativo] = {"hojas": hojas,"claves":claves,
            "vinculos_externos":len(formulas._external_links),"recalculo":str(formulas.calculation)}
        volcado=[]
        for hoja in formulas:
            if hoja.title in ("Resumen Ejecutivo","Indicadores","Parámetros D2","Supuestos cierre","Cierres activacion","Control cierre") or "cierre" in hoja.title.lower():
                volcado.append(f"\nHOJA {hoja.title}\n")
                for fila in hoja:
                    volcado.append(" | ".join(f"{c.coordinate}: {c.value}" for c in fila if c.value is not None))
        (SALIDA/(ruta.stem+"-celdas.txt")).write_text("\n".join(volcado),encoding="utf-8")
    if ruta.suffix == ".pptx":
        with ZipFile(ruta) as archivo:
            nombres = sorted([n for n in archivo.namelist() if n.startswith("ppt/slides/slide") and n.endswith(".xml")],
                             key=lambda n: int(n.split("slide")[-1].split(".")[0]))
            diapositivas = [[t.text for t in ET.fromstring(archivo.read(n)).findall(".//a:t",NS)] for n in nombres]
            graficos = {n:[[t.text for t in s.findall(".//c:v",NS)] for s in ET.fromstring(archivo.read(n)).findall(".//c:ser",NS)]
                        for n in archivo.namelist() if n.startswith("ppt/charts/chart") and n.endswith(".xml")}
        informe["presentaciones"][relativo] = {"laminas":len(diapositivas),"texto":diapositivas,"graficos":graficos}
        (SALIDA/(ruta.stem+".txt")).write_text("\n\n".join(f"LÁMINA {n}\n"+"\n".join(t)
                     for n,t in enumerate(diapositivas,1)),encoding="utf-8")

# Reproducción separada de deuda y caja histórica desde los insumos guardados.
datos = openpyxl.load_workbook(PAQUETE/"AUDIT-Informe3-Modelo-Economico.xlsx",data_only=True)
p=datos["Parámetros D2"]
saldo_caja=saldo_banco=saldo_linea=0
diferencias=[]
for fila in list(datos["Flujo de Caja"].values)[1:]:
    mes=fila[0]
    entrada=p["B4"].value if mes==1 else 0
    interes_banco=saldo_banco*p["B6"].value
    interes_linea=saldo_linea*p["B7"].value
    antes=saldo_caja+entrada+fila[5]-fila[6]+fila[14]-interes_banco-interes_linea
    giro=min(p["B8"].value-saldo_linea,max(0,-antes))
    devolucion=min(saldo_linea,max(0,antes))
    saldo_linea+=giro-devolucion
    amortizacion=min(saldo_banco,max(0,antes+giro-devolucion)) if mes>=p["B17"].value else 0
    saldo_banco+=entrada*p["B5"].value-amortizacion
    saldo_caja=antes+giro-devolucion-amortizacion
    diferencias.append(dict(mes=mes,caja=saldo_caja,delta_caja=saldo_caja-fila[22],
                            delta_banco=saldo_banco-fila[21],delta_linea=saldo_linea-fila[19]))
serie=list(datos["Flujo de Caja"].values)[1:57]
tasa=p["B5"].value*p["B6"].value+(1-p["B5"].value)*((1+p["B9"].value)**(1/12)-1)
van=sum(f[7]/(1+tasa)**f[0] for f in serie)
inferior,superior=0.,2.
for _ in range(90):
    media=(inferior+superior)/2
    if sum(f[7]/(1+media)**f[0] for f in serie)>0: inferior=media
    else: superior=media
informe["reproduccion_independiente"]={"meses":len(diferencias),"diferencia_maxima":
    {c:max(abs(f[c]) for f in diferencias) for c in ("delta_caja","delta_banco","delta_linea")},
    "caja_minima":min(diferencias,key=lambda f:f["caja"]),"tasa_mensual":tasa,"van":van,
    "tir_mensual":(inferior+superior)/2,"costo":sum(f[6] for f in serie),
    "venta":sum(f[4] for f in serie),"hitos":[(f[0],f[1],f[2]) for f in serie if f[1]],
    "facturaciones_operacion":sum(f[0]>=21 and bool(f[4]) for f in serie)}

SALIDA.joinpath("evidencia.json").write_text(json.dumps(informe,ensure_ascii=False,indent=2,default=str)+"\n",encoding="utf-8")
print(json.dumps({"pdf":informe["pdf"],"planillas":{n:len(v["hojas"]) for n,v in informe["planillas"].items()},
 "presentaciones":{n:v["laminas"] for n,v in informe["presentaciones"].items()},
 "reproduccion":informe["reproduccion_independiente"]},ensure_ascii=False,indent=2))
