#!/usr/bin/env python3
"""Reproduce los insumos D3 sin modificar la planilla común ni el T-15.

Uso: python3 Informe-3/d3/calculo/calcular_d3.py
Los valores de horas son estimaciones declaradas; los rangos son los de E-26.
Una cotización ausente se conserva como null, nunca como cero.
"""
from collections import defaultdict
from decimal import Decimal
import json
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
P = json.loads((RAIZ / "datos/presupuesto_d3.json").read_text())
D = lambda x: Decimal(str(x))


def costo(horas):
    minimo = maximo = Decimal(0)
    for perfil, h in horas.items():
        p = P["perfiles"][perfil]
        minimo += D(h) * D(p["costo_min_uf_h"]) * D(P["uf_clp"])
        maximo += D(h) * D(p["costo_max_uf_h"]) * D(P["uf_clp"])
    return {"min_clp": float(minimo), "referencia_clp": float((minimo + maximo) / 2), "max_clp": float(maximo)}


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
            "costo_implementacion_atribuido": costo(i["horas"]),
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
    r["sonarqube"] = {"total_neto_clp": None, "cotizacion_pendiente": True}
    r["total_software_externo_cerrado"] = False
    r["advertencias"] = [
        "La asignación por perfil de EDT 5 a 8 es una propuesta para valorizar el presupuesto existente, no prueba de factibilidad mensual.",
        "EDT 6 y 7 tienen actividades hasta M24, mientras la curva de implementación T-15 termina en M20. D2 debe separar el cierre en operación sin sumar horas dos veces.",
        "No se demuestra holgura por perfil en EDT 13.2 ni 13.4; por ello no se afirma costo adicional cero ni se suman automáticamente las horas propuestas.",
        "Faltan SonarQube y los servicios cloud auxiliares no desglosados por D4. Los subtotales conocidos no son el total completo.",
    ]
    destino = RAIZ / "calculo/resumen_d3.json"
    destino.write_text(json.dumps(r, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(r, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
