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


def revision_edt5():
    """Agrega la propuesta por tareas, separada del presupuesto T-15 vigente."""
    e = json.loads((RAIZ / "datos/estimacion_edt5.json").read_text())
    perfiles = e["perfiles"]
    assert set(perfiles) == set(P["perfiles"])
    tareas = e["tareas"]
    assert len({t["id"] for t in tareas}) == len(tareas), "ID de actividad repetido"
    c = e["calendario"]
    por_sprint = []
    mensual = defaultdict(lambda: {p: Decimal(0) for p in perfiles})
    for sprint in range(1, c["numero_sprints"] + 1):
        grupo = [t for t in tareas if t["sprint"] == sprint]
        assert grupo, f"Sprint sin actividades: {sprint}"
        for t in grupo:
            assert set(t["horas"]) == set(perfiles), t["id"]
            assert all(type(h) is int and h >= 0 for h in t["horas"].values()), t["id"]
            assert sum(t["horas"].values()) > 0 and t["entregable"] and t["limite_con_otros_paquetes"], t["id"]
            for perfil, desglose in t.get("base_estimacion_por_perfil", {}).items():
                assert sum(desglose.values()) == t["horas"][perfil], (t["id"], perfil)
        horas = {p: sum(t["horas"][p] for t in grupo) for p in perfiles}
        inicio = c["inicio_a09_dia_habil"] + (sprint - 1) * c["dias_sprint"]
        fin = inicio + c["dias_sprint"]
        meses = {}
        for mes in range(inicio // c["dias_mes_contractual"] + 1, (fin - 1) // c["dias_mes_contractual"] + 2):
            dias = max(0, min(fin, mes * c["dias_mes_contractual"]) - max(inicio, (mes - 1) * c["dias_mes_contractual"]))
            if dias:
                meses[str(mes)] = dias
                for p, h in horas.items():
                    mensual[mes][p] += D(h) * dias / c["dias_sprint"]
        assert sum(meses.values()) == c["dias_sprint"]
        por_sprint.append({"sprint": sprint, "inicio_dia_habil": inicio, "fin_dia_habil": fin,
                           "dias_por_mes": meses, "horas_por_perfil": horas, "total_h": sum(horas.values())})
    assert all(1 <= t["sprint"] <= c["numero_sprints"] for t in tareas)
    assert por_sprint[6]["fin_dia_habil"] == c["g13_dia_habil"]
    assert por_sprint[-1]["fin_dia_habil"] == c["h4_dia_habil"]
    totales = {p: sum(s["horas_por_perfil"][p] for s in por_sprint) for p in perfiles}
    assert all(sum(h[p] for h in mensual.values()) == D(totales[p]) for p in perfiles)
    total = sum(totales.values())
    return {"estado": e["estado"], "archivo_actividades": "datos/estimacion_edt5.json",
            "numero_actividades": len(tareas), "por_sprint": por_sprint,
            "horas_por_perfil": totales, "total_h": total,
            "mensual_prorrateado": {str(m): {"horas_por_perfil": {p: float(h) for p, h in valores.items()},
                                              "total_h": float(sum(valores.values()))} for m, valores in sorted(mensual.items())},
            "costo_atribuido_referencia_e26": costo(totales),
            "horas_t15_vigentes": e["horas_edt5_t15_vigente"],
            "diferencia_pendiente_de_conciliar_h": e["horas_edt5_t15_vigente"] - total,
            "modifica_t15": False,
            "interpretacion": "Estimación técnica revisada; la diferencia no es ahorro, duplicidad demostrada ni capacidad libre. No sumar esta propuesta al presupuesto vigente."}


def main():
    r = {"fecha": P["fecha"], "naturaleza": P["naturaleza"], "base": {}, "innovaciones": {}, "gitlab": {}}
    base_perfil = defaultdict(int)
    for fila in P["implementacion_base"]:
        assert sum(fila["horas_perfil_propuestas"].values()) == fila["horas_t15"], fila["edt"]
        for perfil, h in fila["horas_perfil_propuestas"].items():
            base_perfil[perfil] += h
    r["base"] = {"horas": sum(base_perfil.values()), "por_perfil": dict(base_perfil), "costo_atribuido": costo(base_perfil), "sumar_al_t15": False}
    assert r["base"]["horas"] == 36800
    r["revision_edt5"] = revision_edt5()
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
    r["nube_auxiliar"] = {"filas": nube, "subtotal_vm_neto_clp": sum(x["neto_clp_total"] for x in nube), "incluido_en_total_d4": True, "total_completo": False,
        "fuente_consolidacion": "Informe-3/d4/4.2-nube-conectividad.md, sección 5, commit b8adac2",
        "alcance": "Solo subtotal de las cuatro filas VM D3-AUX, ya incluido en Azure D4; el total con discos, respaldo, ACR, identidad y CDC/analítica se consolida en D4 y no se suma aquí otra vez."}
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
        "La base conserva el reparto presupuestario histórico EDT 5 a 8. revision_edt5 entrega el catálogo técnico completo de A09 por sprint/perfil; su adopción y nivelación siguen pendientes de conciliación con D2.",
        "EDT 6 y 7 tienen actividades hasta M24, mientras la curva de implementación T-15 termina en M20. D2 debe separar el cierre en operación sin sumar horas dos veces.",
        "No se demuestra holgura por perfil en EDT 13.2 ni 13.4; por ello no se afirma costo adicional cero ni se suman automáticamente las horas propuestas.",
        "SonarQube se presupuesta con el catálogo EUR 215 para 100K LOC y duración anual supuesta; el precio y período se confirman antes de contratar.",
        "D4 incorporó los auxiliares en 4.2 sección 5, commit b8adac2; no sumar otra vez las VM D3-AUX. Falta conciliar personal y su integración sin duplicaciones; el total recurrente completo sigue abierto.",
    ]
    destino = RAIZ / "calculo/resumen_d3.json"
    destino.write_text(json.dumps(r, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(r, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
