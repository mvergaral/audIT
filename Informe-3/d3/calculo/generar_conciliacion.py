#!/usr/bin/env python3
"""Exporta demanda por perfil/mes y escenarios de costo, sin modificar T-15 ni D2."""
from collections import defaultdict
import csv
from decimal import Decimal, ROUND_HALF_UP
import json
from pathlib import Path
import re

from calcular_d3 import P, costo, revision_edt5

RAIZ = Path(__file__).resolve().parents[1]
C = json.loads((RAIZ / "datos/conciliacion_presupuesto.json").read_text())
D = lambda x: Decimal(str(x))
PESO = lambda x: D(x).quantize(Decimal(1), rounding=ROUND_HALF_UP)


def generar():
    filas = []
    tarifas = C["costos_integracion_clp_h"]
    for perfil, precio in tarifas.items():
        limites = P["perfiles"][perfil]
        assert D(limites["costo_min_uf_h"]) * D(P["uf_clp"]) <= D(precio) <= D(limites["costo_max_uf_h"]) * D(P["uf_clp"])

    def agregar(bloque, edt, mes, horas, tratamiento, referencias=None, ejecucion=None):
        for perfil, h in horas.items():
            if not h:
                continue
            assert 1 <= int(mes) <= 56 and D(h) >= 0
            ref_perfil = {perfil: referencias[perfil]} if referencias and perfil in referencias else None
            ref = costo({perfil: 1}, ref_perfil)["referencia_clp"]
            filas.append({"bloque": bloque, "edt_alcance": edt, "paquete_ejecucion": ejecucion or edt,
                          "mes": int(mes), "perfil": perfil, "horas_solicitadas": D(h),
                          "fte_nominal_160h": D(h) / D(C["horas_persona_mes_nominal"]),
                          "costo_atribuido_clp": D(h) * D(ref), "tratamiento": tratamiento})

    a09 = revision_edt5()
    for mes, x in a09["mensual_prorrateado"].items():
        agregar("A09", "5", mes, x["horas_por_perfil"], "sustituye_17600_no_se_suma", tarifas)
    # Reutilizar el reparto D2 para EDT 6-8 y sustituir sólo el A09 histórico.
    # El cierre M21-M24 se detalla más abajo: no importarlo dos veces.
    fuente_d2 = RAIZ.parent / "d2/AUD-14_COSTO_PERSONAL_POR_PERFIL.md"
    texto_d2 = fuente_d2.read_text()
    cabecera = "| Mes | Arquitectura | Liderazgo | Software | Frontend/Móvil | Seguridad | Datos | QA | SRE | Total (h) | Costo (CLP) |"
    assert texto_d2.count(cabecera) == 1
    tabla = texto_d2.split(cabecera, 1)[1].split("\n\n", 1)[0]
    perfiles = list(P["perfiles"])
    viejo_a09 = P["implementacion_base"][0]["horas_perfil_propuestas"]
    resto, meses_d2 = Decimal(0), set()
    for linea in tabla.splitlines():
        if not re.match(r"\| M\d+ \|", linea):
            continue
        celdas = [x.strip() for x in linea.split("|")[1:-1]]
        mes = int(celdas[0][1:])
        meses_d2.add(mes)
        valores = {p: D(celdas[n + 1].replace(".", "").replace(",", ".")) for n, p in enumerate(perfiles)}
        assert sum(valores.values()) == D(celdas[9].replace(".", "").replace(",", "."))
        if 6 <= mes <= 10:
            valores = {p: h - D(viejo_a09[p]) / 5 for p, h in valores.items()}
        assert all(h >= 0 for h in valores.values())
        if mes <= 20:
            agregar("edt6_7_8_reparto_d2", "6+7+8", mes, valores, "sustituir_curva_d2_no_agregar_a_ella", tarifas)
            resto += sum(valores.values())
    assert meses_d2 == set(range(4, 25)), "Cambió la curva D2: revisar el origen"
    assert resto == 17531
    for n in (1, 2):
        i = P[f"innovacion_{n}"]
        for perfil, meses in i["mensual"].items():
            for mes, h in meses.items():
                agregar(f"innovacion_{n}_implementacion", f"12.{n}", mes, {perfil: h}, "dentro_2560_edt12", i.get("costos_referencia_clp_h_implementacion"))
    for fila in C["agente"]:
        agregar("agente_cp_sec_05", "4.1", fila["mes"], fila["horas"], "reserva_4_1_por_conciliar")
    soporte = C["soporte_expediente"]
    for mes in range(soporte["inicio_mes"], soporte["fin_mes"] + 1):
        for perfil, h in soporte["horas_mes"].items():
            edt = soporte["paquete_hasta_m20"] if mes < 21 else ("13.2" if perfil in ("sre", "seguridad") else "13.4")
            agregar("innovacion_1_soporte", edt, mes, {perfil: h}, "reservar_base_o_valorizar_deficit")
    for mes in range(21, 57):
        for perfil, h in P["innovacion_2"]["operacion_h_mes"].items():
            edt = "13.2" if perfil in ("sre", "seguridad") else "13.4"
            agregar("innovacion_2_soporte", edt, mes, {perfil: h}, "reservar_base_o_valorizar_deficit")
    for fila in C["cierres_m21_m24"]:
        for perfil, h in fila["horas"].items():
            ejecucion = "13.2" if perfil in ("sre", "seguridad") else "13.4"
            agregar("cierre_ya_incluido_edt6_7", fila["edt"], fila["mes"], {perfil: h}, "incluido_edt6_7_no_sumar_otra_vez", tarifas, ejecucion)

    horas_bloque, costos_bloque = defaultdict(Decimal), defaultdict(Decimal)
    por_mes = defaultdict(lambda: defaultdict(Decimal))
    for f in filas:
        horas_bloque[f["bloque"]] += f["horas_solicitadas"]
        costos_bloque[f["bloque"]] += f["costo_atribuido_clp"]
        por_mes[f["mes"]][f["perfil"]] += f["horas_solicitadas"]
    assert horas_bloque["A09"] == 6008
    assert horas_bloque["innovacion_1_implementacion"] == 480
    assert horas_bloque["innovacion_2_implementacion"] == 560
    assert horas_bloque["agente_cp_sec_05"] == 72
    assert horas_bloque["cierre_ya_incluido_edt6_7"] == 1669
    assert horas_bloque["A09"] + horas_bloque["edt6_7_8_reparto_d2"] + horas_bloque["cierre_ya_incluido_edt6_7"] == 25208
    assert horas_bloque["innovacion_1_soporte"] == 492
    assert horas_bloque["innovacion_2_soporte"] == 576
    for perfil in perfiles:
        esperado = sum(D(f["horas_perfil_propuestas"][perfil]) for f in P["implementacion_base"][1:])
        actual = sum(f["horas_solicitadas"] for f in filas if f["perfil"] == perfil and f["bloque"] in ("edt6_7_8_reparto_d2", "cierre_ya_incluido_edt6_7"))
        assert actual == esperado, (perfil, actual, esperado)

    ruta = RAIZ / "datos/dedicacion_mensual_d3.csv"
    with ruta.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(filas[0]), lineterminator="\n")
        w.writeheader()
        w.writerows(sorted(filas, key=lambda x: (x["mes"], x["bloque"], x["perfil"])))
    with (RAIZ / "datos/dedicacion_mensual_d3_resumen.csv").open("w", newline="") as f:
        campos = ["mes"] + perfiles + ["total_h", "fte_nominal_160h"]
        w = csv.DictWriter(f, fieldnames=campos, lineterminator="\n")
        w.writeheader()
        for mes, valores in sorted(por_mes.items()):
            total = sum(valores.values())
            w.writerow({"mes": mes, **{p: valores[p] for p in perfiles}, "total_h": total,
                        "fte_nominal_160h": total / D(C["horas_persona_mes_nominal"])})
    v = C["expediente_consumo"]
    eventos = []
    documentos = 0
    for mes in range(v["piloto_inicio_mes"], v["fin_mes"] + 1):
        emisiones = v["emisiones_piloto_mes"] if mes <= v["piloto_fin_mes"] else v["poblacion_dimensionamiento"] * v["emisiones_por_transportista_mes"]
        verificaciones = emisiones * v["verificaciones_por_emision"]
        documentos += emisiones
        bruto = D(emisiones) * D(v["firma_bruto_clp_unidad"]) + D(v["provision_servicio_api_bruto_clp_mes"])
        neto = PESO(bruto / (1 + D(v["iva_referencia"])))
        gb_region = D(documentos) * D(v["bytes_por_documento"]) * D(v["factor_almacenamiento_por_region"]) / D(10**9)
        storage = gb_region * (D(14490) / 500 + D(14670) / 500)
        egreso_gb = D(verificaciones) * D(v["bytes_por_documento"]) / D(10**9)
        egreso = egreso_gb * D(v["egreso_referencia_usd_gb"]) * D(P["usd_clp"])
        peticiones = emisiones * (v["peticiones_gestion_por_emision"] + v["verificaciones_por_emision"])
        logs_gb = D(peticiones) * D(v["bytes_log_por_peticion"]) / D(10**9)
        logs = logs_gb * D(370275) / D(90)
        nube = storage + egreso + logs
        assert nube <= D(v["nube_asignacion_neto_clp_mes"]), "Reestimar la asignación de nube"
        eventos.append({"mes": mes, "emisiones": emisiones, "verificaciones": verificaciones,
                        "firma_servicio_neto_clp": int(neto), "iva_referencia_clp": int(bruto - neto),
                        "pago_bruto_clp": int(bruto), "gb_acumulados_por_region": float(gb_region),
                        "nube_consumo_modelado_clp": float(PESO(nube)),
                        "nube_asignacion_solicitada_clp": v["nube_asignacion_neto_clp_mes"]})
    out = {"fecha": C["fecha"], "naturaleza": C["naturaleza"], "filas_csv": len(filas),
           "alcance_csv": "Sólo bloques D3 detallados. No es toda la dotación del proyecto; no sumar al presupuesto padre ni a curvas D2 que ya contengan esos bloques.",
           "a09": {"trabajo_adoptado_d3_h": 6008, "presupuesto_anterior_h": 17600, "diferencia_h": 11592,
                   "costo_integracion_clp": int(costos_bloque["A09"]), "ahorro_nomina_acreditado_clp": None},
           "horas_por_bloque": dict(horas_bloque), "costo_atribuido_por_bloque_clp": dict(costos_bloque),
           "demanda_bloques_d3_por_mes": {str(m): dict(p) for m, p in sorted(por_mes.items())},
           "expediente": {"implementacion_h_dentro_edt12": 480, "implementacion_costo_atribuido_clp": 14816000,
                          "nuevo_presupuesto_por_sumar_otra_vez_480_h": 0,
                          "soporte_m16_m56_h": 492, "soporte_costo_atribuido_clp": int(costos_bloque["innovacion_1_soporte"]),
                          "personal_adicional_confirmado_clp": None,
                          "escenario_soporte_sin_cobertura_clp": int(costos_bloque["innovacion_1_soporte"]),
                          "firma_servicio_neto_clp": sum(x["firma_servicio_neto_clp"] for x in eventos),
                          "iva_referencia_clp": sum(x["iva_referencia_clp"] for x in eventos),
                          "pago_firma_servicio_bruto_clp": sum(x["pago_bruto_clp"] for x in eventos),
                          "nube_asignacion_solicitada_clp": sum(x["nube_asignacion_solicitada_clp"] for x in eventos),
                          "proveedor_propuesto": v["proveedor_propuesto"],
                          "modalidad_compatible_documentada": v["modalidad_compatible_documentada"],
                          "integracion_probada": v["integracion_probada"],
                          "tarifa_ecert_confirmada": v["tarifa_ecert_confirmada"],
                          "proveedor_modo_automatico_contratado": False,
                          "calendario_externo": eventos}}
    salida = RAIZ / "calculo/conciliacion_presupuesto.json"
    salida.write_text(json.dumps(out, ensure_ascii=False, indent=2, default=lambda x: float(x) if x % 1 else int(x)) + "\n")
    return out


if __name__ == "__main__":
    resultado = generar()
    print(json.dumps({"filas_csv": resultado["filas_csv"], "a09": resultado["a09"],
                      "costos_por_bloque": resultado["costo_atribuido_por_bloque_clp"],
                      "firma_servicio_neto_clp": resultado["expediente"]["firma_servicio_neto_clp"],
                      "pago_bruto_clp": resultado["expediente"]["pago_firma_servicio_bruto_clp"]}, default=str, ensure_ascii=False, indent=2))
