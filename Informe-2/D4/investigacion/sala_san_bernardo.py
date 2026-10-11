#!/usr/bin/env python3
"""Balance eléctrico y térmico de la sala de San Bernardo, UPS, grupo electrógeno,
CCTV, ExpressRoute y UPS de terminal. Documento interno de la dupla 4 (2026-09-29).

Cada valor dice de dónde sale: ficha del fabricante (F), decisión aprobada (D) o
supuesto declarado (S). Se corre con: python3 sala_san_bernardo.py
"""

# --- Carga de TI de la sala (W, máximo) ---
carga_ti = {
    "2 servidores Dell PowerEdge R360 (S, D4-39: 300 W c/u)": 2 * 300,
    "2 firewalls FortiGate 90G (F: 19,9 W c/u)": 2 * 19.9,
    # FortiSwitch 124F-POE: 237,4 W máx. con 185 W de presupuesto PoE (F) => 52,4 W sin PoE
    "2 switches FortiSwitch 124F-POE sin PoE (F: 237,4 - 185)": 2 * (237.4 - 185),
    # 4 cámaras PoE 802.3af clase 3: 12,95 W máx. en el equipo (norma IEEE 802.3af)
    "PoE de 4 cámaras IP clase 3 (S: 12,95 W c/u)": 4 * 12.95,
    "Control de acceso, grabador, VESDA, panel y sensores (S)": 150,
    "Equipos terminales de los dos proveedores de enlace (S: 25 W c/u)": 2 * 25,
}
ti = sum(carga_ti.values())

# --- UPS: dos APC SRT3000 en alimentación A y B (2N) ---
ups_pot = 2700              # W por UPS (F)
disip_plena = 703 / 3.412   # W de calor a plena carga (F: 703 BTU/h)
perdida_frac = disip_plena / ups_pot
perdidas_ups = 2 * max(50, perdida_frac * ti / 2)   # S: piso de 50 W por equipo
vah_interna, vah_pack = 505, 1010                   # F: 505 VAh y 1.515 VAh con 1 SRT96BP
eta_inv, fin_vida = 0.90, 0.80                      # S: rendimiento del inversor y batería al final de su vida

def autonomia_min(vah, carga_w):
    return vah * eta_inv * fin_vida / carga_w * 60

# --- Clima: Liebert Mini-Mate2 de 1 tonelada (3,55 kW), N+1 ---
iluminacion = 26 * 8            # S: LED 8 W/m2 en 26 m2 (F del caso: 26 m2)
ganancias_recinto = 300         # S: muros, personas y equipos menores
calor = ti + perdidas_ups + iluminacion + ganancias_recinto
cop = 6.6 / 2.02                # F: Stulz MiniSpace EC, 6,6 kW con 2.020 W de compresor
ventilador_evap = 149           # F: Mini-Mate2, motor del evaporador 0,2 hp (149 W)
clima = calor / cop + ventilador_evap

total = ti + perdidas_ups + iluminacion + clima
pue = total / ti

# --- Grupo electrógeno: Himoinsa HYW-8 T5 S5, 8,8 kVA PRP ---
recarga = 2 * 168               # F: cargador de 168 W por UPS
carga_grupo_kw = (total + recarga) / 1000
fp_grupo = 0.8                  # potencia nominal de grupos a fp 0,8
carga_grupo_kva = carga_grupo_kw / fp_grupo
fraccion = carga_grupo_kva / 8.8
consumo_plena = 2.68            # F: l/h al 100 % PRP
litros_24h = consumo_plena * 24

# --- CCTV: 30 días en línea (RT-06.24) ---
camaras, mbps = 4, 2.0          # S: H.265 1080p a 2 Mbit/s
tb_30d = camaras * mbps * 1e6 / 8 * 30 * 86400 / 1e12

# --- ExpressRoute San Bernardo - Azure ---
usuarios_conc = 80              # Informe 1, Tabla 1.18: 50 a 80 internos en hora punta
mbps_usuario = 0.5              # S: aplicación web con mapas
crecimiento = 390 / 336         # F: Caso, numeral 14.1 (336 -> 390 con acceso)
otros = 5                       # S: nodo de continuidad, capa anticorrupción y respaldos
er_mbps = (usuarios_conc * mbps_usuario + otros) * crecimiento

# --- UPS de terminal: APC SRT1000XLI (F: 293 VAh internos) con criterio de 30 min ---
terminal = {
    "2 OnLogic Karbon 430 (F: 35 W c/u)": 70,
    "Router Teltonika RUTX50 (F: < 18 W)": 18,
    "Switch Teltonika TSW202 sin PoE (F: 8 W)": 8,
    "FortiAP 234G por su inyector (F: 28 W)": 28,
    "Lector Bluetooth de portería por PoE (S: 3 W)": 3,
    "Equipo terminal del proveedor fijo (S)": 25,
}
term_w = sum(terminal.values())

if __name__ == "__main__":
    print("Carga de TI de San Bernardo")
    for k, v in carga_ti.items():
        print(f"  {k}: {v:.0f} W")
    print(f"  Total TI: {ti:.0f} W")
    print(f"Pérdidas de UPS: {perdidas_ups:.0f} W ({perdida_frac:.1%} a plena carga)")
    print(f"Iluminación: {iluminacion:.0f} W. Ganancias del recinto: {ganancias_recinto} W")
    print(f"Calor a retirar: {calor:.0f} W. COP de referencia: {cop:.2f}")
    print(f"Clima (una unidad en servicio): {clima:.0f} W")
    print(f"Carga total: {total:.0f} W. PUE estimado: {pue:.2f}")
    print(f"Autonomía de una UPS sola con toda la carga de TI: "
          f"interna {autonomia_min(vah_interna, ti):.0f} min, "
          f"con 1 SRT96BP {autonomia_min(vah_interna + vah_pack, ti):.0f} min")
    print(f"Grupo: {carga_grupo_kw:.2f} kW, {carga_grupo_kva:.2f} kVA, "
          f"{fraccion:.0%} de 8,8 kVA. 24 h a plena carga: {litros_24h:.1f} L (estanque 100 L)")
    print(f"CCTV 30 días: {tb_30d:.2f} TB")
    print(f"ExpressRoute: {er_mbps:.0f} Mbit/s -> circuito de 100 Mbit/s")
    print(f"Terminal: {term_w} W. Autonomía con SRT1000XLI (F: 293 VAh): "
          f"{autonomia_min(293, term_w):.0f} min")
