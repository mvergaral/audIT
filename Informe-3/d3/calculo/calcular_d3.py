#!/usr/bin/env python3
"""Reproduce los insumos D3 sin modificar la planilla común ni el T-15.

Uso: python3 Informe-3/d3/calculo/calcular_d3.py
Los valores de horas son estimaciones declaradas; los rangos son los de E-26.
Las estimaciones presupuestarias se distinguen de cotizaciones; un importe no
dimensionado se conserva como null, nunca como cero.
"""
from collections import defaultdict
from decimal import Decimal
import json
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
P = json.loads((RAIZ / "datos/presupuesto_d3.json").read_text())
D = lambda x: Decimal(str(x))


def costo(horas, referencias_clp_h=None):
    referencias_clp_h = referencias_clp_h or {}
    assert referencias_clp_h.keys() <= horas.keys(), "Referencia de costo para un perfil sin horas"
    minimo = referencia = maximo = Decimal(0)
    for perfil, h in horas.items():
        p = P["perfiles"][perfil]
        unitario_min = D(p["costo_min_uf_h"]) * D(P["uf_clp"])
        unitario_max = D(p["costo_max_uf_h"]) * D(P["uf_clp"])
        unitario_ref = D(referencias_clp_h[perfil]) if perfil in referencias_clp_h else (unitario_min + unitario_max) / 2
        assert unitario_min <= unitario_ref <= unitario_max, f"Costo fuera de E-26: {perfil}"
        minimo += D(h) * unitario_min
        referencia += D(h) * unitario_ref
        maximo += D(h) * unitario_max
    return {"min_clp": float(minimo), "referencia_clp": float(referencia), "max_clp": float(maximo)}


def main():
    r = {"fecha": P["fecha"], "naturaleza": P["naturaleza"], "base": {}, "innovaciones": {}, "gitlab": {}}
    base_perfil = defaultdict(int)
    for fila in P["implementacion_base"]:
        assert sum(fila["horas_perfil_propuestas"].values()) == fila["horas_t15"], fila["edt"]
        for perfil, h in fila["horas_perfil_propuestas"].items():
            base_perfil[perfil] += h
    r["base"] = {"horas": sum(base_perfil.values()), "por_perfil": dict(base_perfil), "costo_atribuido": costo(base_perfil), "sumar_al_t15": False}
    assert r["base"]["horas"] == 36800
    for n, esperado in [(1, 480), (2, 560)]:
        i = P[f"innovacion_{n}"]
        assert sum(i["horas"].values()) == esperado
        meses = defaultdict(int)
        for perfil, valores in i["mensual"].items():
            assert sum(valores.values()) == i["horas"][perfil], (n, perfil)
            for mes, h in valores.items():
                assert 1 <= int(mes) <= 56 and h >= 0
                meses[int(mes)] += h
        op = i["operacion_h_mes"]
        c_op = costo(op)
        r["innovaciones"][str(n)] = {
            "horas_implementacion": esperado,
            "horas_por_mes": dict(sorted(meses.items())),
            "costo_implementacion_atribuido": costo(i["horas"], i.get("costos_referencia_clp_h_implementacion")),
            "operacion_h_mes": sum(op.values()),
            "operacion_h_36_meses": sum(op.values()) * 36,
            "costo_operacion_mes_atribuido": c_op,
            "costo_operacion_36_meses_atribuido": {k: v * 36 for k, v in c_op.items()},
            "desembolso_personal_adicional_confirmado": None,
        }
    total_inn = sum(i["horas_implementacion"] for i in r["innovaciones"].values())
    assert total_inn == 1040 and total_inn <= 2560
    r["innovaciones"]["reserva_edt12_para_3_4_5_h"] = 2560 - total_inn
    pagos = []
    for pago in P["gitlab"]["pagos"]:
        usd = D(pago["usuarios"]) * D(P["gitlab"]["usd_usuario_mes"]) * D(P["gitlab"]["facturacion_meses"])
        pagos.append({**pago, "usd": float(usd), "neto_clp": float(usd * D(P["usd_clp"])), "iva_clp": float(usd * D(P["usd_clp"]) * D(P["iva"]))})
    r["gitlab"] = {"pagos": pagos, "total_usd": sum(x["usd"] for x in pagos), "total_neto_clp": sum(x["neto_clp"] for x in pagos), "total_iva_clp": sum(x["iva_clp"] for x in pagos)}
    nube = []
    for fila in P["nube_auxiliar_propuesta"]:
        meses = fila["fin"] - fila["inicio"] + 1
        usd_mes = D(fila["usd_h"]) * D(fila["cantidad"]) * D(fila["horas_mes"])
        nube.append({"id": fila["id"], "meses": meses, "neto_clp_mes": float(usd_mes * D(P["usd_clp"])), "neto_clp_total": float(usd_mes * D(P["usd_clp"]) * meses)})
    r["nube_auxiliar"] = {"filas": nube, "subtotal_vm_neto_clp": sum(x["neto_clp_total"] for x in nube), "incluido_en_total_d4": False, "total_completo": False}
    sonar = P["sonarqube"]
    assert sonar["periodo_modelado_meses"] == 12
    assert sonar["loc"] > 0 and sonar["instancias"] > 0
    anual = D(sonar["precio_catalogo_eur_neto"]) * D(sonar["instancias"])
    pagos_sonar = []
    for mes in sonar["pagos_propuestos"]:
        assert 1 <= mes <= 56
        neto = anual * D(P["eur_clp"])
        pagos_sonar.append({"mes": mes, "eur": float(anual), "neto_clp": float(neto), "neto_uf": float(neto / D(P["uf_clp"])), "neto_usd": float(neto / D(P["usd_clp"])), "iva_clp": float(neto * D(P["iva"])), "cobertura_hasta_mes": mes + 11})
    assert [x["mes"] for x in pagos_sonar] == list(range(4, 57, 12))
    alternativa = sonar["escenario_alternativo"]
    assert alternativa["moneda"] == "USD"
    neto_alternativo = D(alternativa["precio_anual"]) * D(P["usd_clp"]) * D(sonar["instancias"]) * len(pagos_sonar)
    r["sonarqube"] = {
        "tipo_importe": sonar["naturaleza_importe"], "es_cotizacion": False,
        "cotizacion_pendiente": sonar["cotizacion_pendiente"],
        "cotizacion_bloquea_informe3": sonar["cotizacion_bloquea_informe3"],
        "presupuesto_informe3_completo": sonar["presupuesto_informe3_completo"],
        "sku_catalogo": sonar["sku_catalogo"], "loc_objetivo_no_medido": sonar["loc"],
        "eur_anual_modelado": float(anual),
        "periodo_anual_es_supuesto": not sonar["periodo_catalogo_confirmado"],
        "pagos": pagos_sonar,
        "total_eur": sum(x["eur"] for x in pagos_sonar),
        "total_neto_clp": sum(x["neto_clp"] for x in pagos_sonar),
        "total_neto_uf": sum(x["neto_uf"] for x in pagos_sonar),
        "total_neto_usd": float(anual * len(pagos_sonar) * D(P["eur_clp"]) / D(P["usd_clp"])),
        "total_iva_clp": sum(x["iva_clp"] for x in pagos_sonar),
        "escenario_referencia_historica": {"usd_anual": alternativa["precio_anual"], "neto_clp_5_anualidades": float(neto_alternativo), "iva_clp": float(neto_alternativo * D(P["iva"])), "diferencia_sobre_base_clp": float(neto_alternativo - anual * D(P["eur_clp"]) * len(pagos_sonar)), "misma_capacidad_y_condiciones_confirmadas": False},
        "validacion_comercial_antes_de_compra": True,
    }
    r["licencias_comerciales_presupuestadas"] = {
        "total_neto_clp": r["gitlab"]["total_neto_clp"] + r["sonarqube"]["total_neto_clp"],
        "total_iva_referencial_clp": r["gitlab"]["total_iva_clp"] + r["sonarqube"]["total_iva_clp"],
        "sonar_es_estimacion": True, "incluye_alojamiento_y_personal": False,
    }
    neto_licencias = D(r["licencias_comerciales_presupuestadas"]["total_neto_clp"])
    r["licencias_comerciales_presupuestadas"].update({"total_neto_uf": float(neto_licencias / D(P["uf_clp"])), "total_neto_usd": float(neto_licencias / D(P["usd_clp"]))})
    r["total_software_externo_cerrado"] = False
    r["advertencias"] = [
        "La asignación por perfil de EDT 5 a 8 es una propuesta para valorizar el presupuesto existente, no prueba de factibilidad mensual.",
        "EDT 6 y 7 tienen actividades hasta M24, mientras la curva de implementación T-15 termina en M20. D2 debe separar el cierre en operación sin sumar horas dos veces.",
        "No se demuestra holgura por perfil en EDT 13.2 ni 13.4; por ello no se afirma costo adicional cero ni se suman automáticamente las horas propuestas.",
        "SonarQube se presupuesta con el catálogo EUR 215 para 100K LOC y duración anual supuesta. AUD-25 está completo para el Informe 3 con fuentes y supuestos; la confirmación comercial se reserva para una eventual compra real.",
        "Faltan completar servicios cloud auxiliares y conciliar personal; el total recurrente completo sigue abierto.",
    ]
    destino = RAIZ / "calculo/resumen_d3.json"
    destino.write_text(json.dumps(r, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(r, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
