#!/usr/bin/env python3
"""Presupuesto de equipos de la tarea 4.1 (AUD-32).

Tipo de cambio del Formulario E-24 (FEP01, p. 73): USD $900, EUR $1.000, IVA 19 %.
Quién paga cada equipo sigue D4-143 (aclaraciones del Informe 3, §9):
  - audIT, en su flujo: servidores, cómputo de terminal, gabinetes y habilitación de la sala.
  - mandante, hoja informativa fuera del flujo: hardware de campo y de red.
Precios y URL en ../_borrador-precios.md. Uso: python3 presupuesto_41.py > presupuesto_41.out
"""
TC = {"USD": 900, "EUR": 1000}
IVA = 0.19

# clave: (fila T-11, equipo, precio, moneda, fuente). Precio None = sin precio.
P = {
    "g26i": ("1 y 2", "iWave G26I", 454.31, "EUR", "DigiKey ES"),
    "edge": ("3", "Iridium Edge", 359.00, "USD", "Satphonestore"),
    "croc": ("4", "Technoton CANCrocodile", 47.00, "EUR", "Technoton, tienda oficial"),
    "gao": ("5", "Lector GAO RFID DESFire (ref. GeoVision IP66)", 83.99, "USD", "IP Security Depot, equivalente"),
    "card": ("6", "Tarjeta MIFARE DESFire EV3 4K", 1.35, "EUR", "rfid.it, 200 a 799"),
    "eye": ("7 y 8", "Teltonika EYE Sensor BTSMP1", 19.99, "EUR", "Comet, desde 10"),
    "aaeon": ("9", "AAEON ICS-6280A-A10-00", 523.61, "EUR", "Texim Europe"),
    "ram": ("9", "Memoria DDR4-3200 8 GB, -40 a 85 °C (ref. Transcend TS1GSH64V2B1-I)", 149.99, "USD", "Almo Pro AV, lista, equivalente"),
    "ssd": ("9", "SSD SATA 2,5 pulg. 256 GB, -40 a 85 °C (ref. Innodisk 3TE7)", 298.00, "EUR", "cartft.com, equivalente"),
    "rutx": ("10", "Teltonika RUTX50", 422.00, "EUR", "nasstore"),
    "tsw": ("11", "Teltonika TSW202", 108.00, "EUR", "nasstore"),
    "sdr24": ("12", "Mean Well SDR-120-24 (ref.)", 51.87, "EUR", "alimentatorishop, equivalente"),
    "sdr48": ("12", "Mean Well SDR-120-48 (ref.)", 57.40, "EUR", "alimentatorishop, equivalente"),
    "rdn": ("12", "Mean Well DRDN20-24 o DRDN20-48", 21.20, "EUR", "Elmark"),
    "srt1": ("13", "APC SRT1000XLI", 1078.99, "EUR", "Bechtle"),
    "fap": ("14", "Fortinet FortiAP 234G", 1157.00, "USD", "SHI"),
    "gpi": ("14", "Fortinet GPI-145 (802.3bt)", 300.00, "USD", "Lista, gov.connection"),
    "minew": ("15", "Minew G1", 78.00, "USD", "DigiKey"),
    "r360": ("16", "Dell PowerEdge R360 (config. de entrada)", 5549.00, "USD", "Dell EE. UU., referencia"),
    "fg": ("17", "Fortinet FortiGate 90G", 2190.00, "USD", "SHI"),
    "pdc": ("17", "Fortinet SP-FG60E-PDC-5 (pack de 5 adaptadores)", 381.04, "USD", "CDW"),
    "fs": ("18", "Fortinet FortiSwitch 124F-POE", 1030.00, "USD", "SHI"),
    "srt3": ("19", "APC SRT3000RMXLI", 5278.00, "USD", "SHI"),
    "bat": ("19", "APC SRT96RMBP", 1447.99, "USD", "CDW"),
    "mm2": ("20", "Vertiv Liebert Mini-Mate2 MMD12E", 12000.00, "USD", "Estimado, D4-145"),
    "vesda": ("21", "Xtralis VESDA VLF-250-00", 2381.00, "USD", "firealarm.com"),
    "kidde": ("22", "Kidde FK-5-1-12 dimensionado a la sala", 15000.00, "USD", "Estimado, D4-145"),
    "ext": ("23", "Extintor CO2 5 kg (ref.)", 65.00, "EUR", "chlengenharia.pt, equivalente"),
    "supr": ("24", "Suprema FaceStation F2 FSF2-ODB", 2605.54, "USD", "Titan Security Supply"),
    "cam": ("25", "Axis M3215-LVE", 835.00, "USD", "SHI"),
    "nvr": ("26", "Axis S3008 Mk II 4 TB", 903.99, "EUR", "Bechtle PT"),
    "lt": ("27", "Vertiv Liebert LT460 con cable de 20 pies", 1142.44, "USD", "Kele"),
    "gen": ("28", "Himoinsa HYW-8 T5 insonorizado", 9750.00, "EUR", "Truck1"),
    "rack": ("29", "APC NetShelter SX 24U AR3104", 2256.00, "USD", "SHI"),
}

# Lo que provee audIT en su flujo (D4-143 a). El resto lo compra el mandante.
AUDIT = {"r360", "srt3", "bat", "mm2", "vesda", "kidde", "ext", "supr", "cam", "nvr", "lt", "gen",
         "rack", "aaeon", "ram", "ssd", "srt1", "sdr24", "sdr48", "rdn"}

# (grupo, clave, cantidad, mes de compra, nota). Meses de D4-141 (a).
M = [
    ("Grupo electrógeno", "gen", 1, 1, "Hasta 6 meses de plazo en SEV"),
    ("Sala de San Bernardo", "r360", 2, 3, ""), ("Sala de San Bernardo", "fg", 2, 3, ""),
    ("Sala de San Bernardo", "pdc", 1, 3, "Segundo adaptador de los 2 FortiGate"),
    ("Sala de San Bernardo", "fs", 2, 3, "Una sola fuente, RT-08.04 abierto"),
    ("Sala de San Bernardo", "srt3", 2, 3, ""), ("Sala de San Bernardo", "bat", 2, 3, ""),
    ("Sala de San Bernardo", "mm2", 2, 3, "N+1"), ("Sala de San Bernardo", "vesda", 1, 3, ""),
    ("Sala de San Bernardo", "kidde", 1, 3, ""), ("Sala de San Bernardo", "ext", 2, 3, ""),
    ("Sala de San Bernardo", "supr", 2, 3, ""), ("Sala de San Bernardo", "cam", 4, 3, ""),
    ("Sala de San Bernardo", "nvr", 1, 3, ""), ("Sala de San Bernardo", "lt", 1, 3, ""),
    ("Sala de San Bernardo", "rack", 2, 3, ""),
    ("Repuestos de sala (D4-141 c)", "r360", 1, 3, ""), ("Repuestos de sala (D4-141 c)", "fg", 1, 3, ""),
    ("Repuestos de sala (D4-141 c)", "fs", 1, 3, ""), ("Repuestos de sala (D4-141 c)", "srt3", 1, 3, ""),
    ("Gabinetes y patio", "aaeon", 8, 4, "2 por terminal regional"),
    ("Gabinetes y patio", "ram", 8, 4, "Una por ICS-6280, D4-142"),
    ("Gabinetes y patio", "ssd", 8, 4, "Uno por ICS-6280, D4-142"),
    ("Gabinetes y patio", "rutx", 4, 4, ""), ("Gabinetes y patio", "tsw", 4, 4, ""),
    ("Gabinetes y patio", "sdr24", 8, 4, "2 por gabinete"), ("Gabinetes y patio", "sdr48", 8, 4, "2 por gabinete"),
    ("Gabinetes y patio", "rdn", 8, 4, "1 de 24 V y 1 de 48 V por gabinete"),
    ("Gabinetes y patio", "srt1", 4, 4, ""), ("Gabinetes y patio", "fap", 5, 4, "5 terminales"),
    ("Gabinetes y patio", "gpi", 5, 4, "28 W del T-11"), ("Gabinetes y patio", "minew", 5, 4, ""),
    ("Repuestos de gabinete (D4-141 c)", "aaeon", 1, 4, ""), ("Repuestos de gabinete (D4-141 c)", "ram", 1, 4, ""),
    ("Repuestos de gabinete (D4-141 c)", "ssd", 1, 4, ""), ("Repuestos de gabinete (D4-141 c)", "rutx", 1, 4, ""),
    ("Repuestos de gabinete (D4-141 c)", "tsw", 1, 4, ""), ("Repuestos de gabinete (D4-141 c)", "srt1", 1, 4, ""),
    ("Repuestos de gabinete (D4-141 c)", "sdr24", 1, 4, ""), ("Repuestos de gabinete (D4-141 c)", "sdr48", 1, 4, ""),
    ("Piloto a bordo", "g26i", 10, 5, "Piloto de 10 camiones, mes 6"), ("Piloto a bordo", "edge", 10, 5, ""),
    ("Piloto a bordo", "croc", 10, 5, ""), ("Piloto a bordo", "gao", 10, 5, ""),
    ("Tarjetas y balizas", "card", 572, 5, "520 conductores más 10 %"),
    ("Tarjetas y balizas", "eye", 231, 5, "210 más 21 de reposición"),
    ("Resto a bordo", "g26i", 191, 6, "172 más 19 de reposición"), ("Resto a bordo", "edge", 191, 6, ""),
    ("Resto a bordo", "croc", 191, 6, ""), ("Resto a bordo", "gao", 191, 6, ""),
]
for mes, ng, nb in [(24, 8, 12), (36, 7, 12), (48, 7, 11)]:
    for k in ["g26i", "edge", "croc", "gao"]:
        M.append((f"Crecimiento año {(mes - 12) // 12}", k, ng, mes, "Juego completo, D4-141 b"))
    M.append((f"Crecimiento año {(mes - 12) // 12}", "eye", nb, mes, "Balizas por crecimiento"))

# Unidad de prueba de cada dispositivo de terreno (FEP02, RT-08.15), que paga audIT.
PRUEBA = [("Unidad de prueba (RT-08.15)", k, 1, 4, "") for k in
          ["g26i", "edge", "croc", "gao", "eye", "aaeon", "ram", "ssd", "rutx", "tsw", "fap", "minew"]]


def fmt(x, d=0):
    return f"{x:,.{d}f}".replace(",", "X").replace(".", ",").replace("X", ".")


def tabla(lineas):
    out = ["| N.º | Grupo | Fila T-11 | Equipo | Cant. | Precio unitario | Unitario en pesos | Total neto en pesos | IVA | Mes | Fuente | Nota |",
           "|---|---|---|---|---|---|---|---|---|---|---|---|"]
    tot, porgrupo, pormes, sinp = 0, {}, {}, []
    for i, (g, k, q, mes, nota) in enumerate(lineas, 1):
        fila, eq, p, mon, ref = P[k]
        if p is None:
            out.append(f"| {i} | {g} | {fila} | {eq} | {q} | sin precio | | | Afecto | {mes} | {ref} | {nota} |")
            sinp.append(eq)
            continue
        u = p * TC[mon]
        t = u * q
        tot += t
        porgrupo[g] = porgrupo.get(g, 0) + t
        pormes[mes] = pormes.get(mes, 0) + t
        out.append(f"| {i} | {g} | {fila} | {eq} | {q} | {mon} {fmt(p, 2)} | {fmt(u)} | {fmt(t)} | Afecto | {mes} | {ref} | {nota} |")
    return out, tot, porgrupo, pormes, sinp


def bloque(titulo, lineas):
    o, tot, pg, pm, sp = tabla(lineas)
    print(f"===== {titulo}")
    print("\n".join(o))
    print("\n| Grupo | Total neto en pesos |\n|---|---|")
    for g, v in pg.items():
        print(f"| {g} | {fmt(v)} |")
    print(f"| Total con precio | {fmt(tot)} |")
    print("\n| Mes | Total neto en pesos | IVA 19 % | Total con IVA |\n|---|---|---|---|")
    for m in sorted(pm):
        print(f"| {m} | {fmt(pm[m])} | {fmt(pm[m] * IVA)} | {fmt(pm[m] * (1 + IVA))} |")
    print(f"| Total | {fmt(tot)} | {fmt(tot * IVA)} | {fmt(tot * (1 + IVA))} |")
    print(f"SIN PRECIO: {sorted(set(sp))}")
    print(f"TOTAL {titulo}: {fmt(tot)}\n")


if __name__ == "__main__":
    bloque("AUDIT_INVERSION", [l for l in M if l[1] in AUDIT])
    bloque("AUDIT_PRUEBA", PRUEBA)
    bloque("MANDANTE_INFORMATIVA", [l for l in M if l[1] not in AUDIT])
