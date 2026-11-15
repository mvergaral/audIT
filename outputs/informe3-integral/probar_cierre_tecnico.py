"""Reproduce la agenda y las sensibilidades del cierre técnico académico."""

import csv
from collections import defaultdict
from datetime import date, time, timedelta, datetime
from fractions import Fraction
from math import ceil, exp, factorial

from acreditar_fondos import Stress, model, size, stage
from regenerar_cierre import OUT, FLOOR
from reproducir import book


TERMINALS = ["San Bernardo", "Antofagasta", "Talca", "Los Ángeles", "Puerto Montt"]
WINDOWS = {
    6: [(7, [6, 7, 8, 9])],
    7: [(8, [2, 3, 4, 5]), (8, [9, 10, 11, 12])],
    8: [(9, [1, 2, 3, 6]), (9, [9, 10, 13, 14])],
    9: [(10, [4, 5, 6, 7]), (10, [12, 13, 14, 15])],
}
STARTS = [time(8), time(10, 40), time(13, 20)]
RATE = 16_000
MOUNT_MINUTES = 140
VAT = Fraction(19, 100)


def save(name, header, rows):
    with (OUT / name).open("w", encoding="utf-8-sig", newline="") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(header)
        writer.writerows(rows)


def agenda():
    rows = []
    simultaneous = defaultdict(set)
    for month in (6, 7, 8, 9):
        count_terminals = 1 if month == 6 else 5
        for i, terminal in enumerate(TERMINALS[:count_terminals]):
            n = (10 if month == 6 else 12 if month in (7, 8) or i == 0 else 10)
            own = n if month <= 8 else (6 if i == 0 else 3)
            calendar_month, days = WINDOWS[month][int(i >= 3)]
            for k in range(n):
                day = date(2027, calendar_month, days[k // 3])
                start = datetime.combine(day, STARTS[k % 3])
                stop = start + timedelta(minutes=MOUNT_MINUTES)
                group = i % 3 + 1
                key = (day, start.time())
                assert group not in simultaneous[key]
                simultaneous[key].add(group)
                assert day.weekday() < 5 and day.day <= 15
                rows.append((month, terminal, day.isoformat(), start.strftime("%H:%M"),
                             stop.strftime("%H:%M"), f"IMPL-{group}",
                             f"{'AUD-PILOTO' if month == 6 else 'EXT'}-{i+1}",
                             "Flota propia" if k < own else "Comodato",
                             20, MOUNT_MINUTES, MOUNT_MINUTES))
    assert len(rows) == 182 and max(map(len, simultaneous.values())) == 3
    assert sum(row[7] == "Flota propia" for row in rows) == 148
    assert sum(sum(row[8:]) for row in rows) == 910 * 60
    # Las 182 reservas corresponden a cupos, sujetos a coincidencia con la visita normal.
    return rows


def comparison(agenda_rows):
    stress = Stress(14, 12)
    base = size(Stress(12), {}, 1)
    cash = model(stress, stage(stress, base, 16), 16)
    totals = []
    cumulative_vat = cumulative_gross = 0
    for m in range(6, 10):
        external = sum(row[0] == m and row[6].startswith("EXT-") for row in agenda_rows)
        net = round(Fraction(external * MOUNT_MINUTES * RATE, 60))
        tax = round(net * VAT)
        cumulative_vat += tax
        cumulative_gross += net + tax
        cached = cash[m - 1]["caja_cierre"]
        totals.append((m, external, external * MOUNT_MINUTES, net, tax, net + tax,
                       round(cached), round(cached - cumulative_vat),
                       round(cached - cumulative_gross), ceil(max(0, FLOOR - cached + cumulative_vat)),
                       ceil(max(0, FLOOR - cached + cumulative_gross))))
    assert sum(row[1] for row in totals) == 172
    assert sum(row[3] for row in totals) == 6421333 and cumulative_vat == 1220053
    return totals


def support():
    rows = []
    for m in range(21, 25):
        assert book["Personal"].cell(m+1, 4).value == 88_252_000
        for role, demand, base, hourly in [("Ingeniería de Datos", 146, 80, 32_000),
                                           ("QA Senior", 77, 40, 20_000)]:
            gap = demand - base
            rows.append((m, role, demand, base, gap, hourly, gap * hourly,
                         "La disponibilidad base requiere una reserva expresa de las horas"))
    assert sum(row[6] for row in rows) == 11_408_000
    assert book["Personal"]["D26"].value == 85_400_000
    return rows


def erlang(c, arrivals, service_rate, wait_min):
    load = arrivals / service_rate
    rho = load / c
    tail = load ** c / (factorial(c) * (1-rho))
    wait = tail / (sum(load ** i / factorial(i) for i in range(c)) + tail)
    return rho, wait * exp(-(c*service_rate-arrivals) * wait_min/60)


def sla_cases():
    cases = []
    for label, agents, arrivals in [("Valle", 1, 2), ("Pico", 2, 4)]:
        rho, tail = erlang(agents, arrivals, 4, 15)
        cases.append((label, agents, arrivals, 15, round(rho * 100, 2), round(tail * 100, 2)))
    assert round(cases[0][5], 2) == 30.33 and cases[1][5] == 12.26
    worst_month = 31
    assert worst_month * (24+6) == 930 < 960
    assert 66*32000 + 37*20000 == 2_852_000
    assert 15+30+180 == 225 < 240
    assert 15+30+240 == 285 > 240
    assert 5+2*5 == 15 and 5+3*5 > 15
    assert 4*10 <= 28*24*60*0.001 < 5*10
    return cases


def main():
    rows = agenda()
    estimate = comparison(rows)
    coverage = support()
    cases = sla_cases()
    save("Agenda-montaje-simulada.csv",
         ["Mes", "Terminal", "Fecha simulada", "Inicio", "Fin", "Analista audIT", "Técnico",
          "Flota", "Minutos banco audIT", "Minutos montaje técnico", "Minutos analista"], rows)
    save("Instalacion-caja-sensibilidad.csv",
         ["Mes", "Kits externos", "Minutos a sustituir", "Neto externo CLP", "IVA CLP",
          "Pago bruto CLP", "Cierre de referencia CLP", "Cierre con descuento nómina CLP",
          "Cierre sin descuento nómina CLP", "Refuerzo mínimo con descuento CLP",
          "Refuerzo mínimo sin descuento CLP"], estimate)
    save("Soporte-Datos-QA-simulado.csv",
         ["Mes", "Rol", "Demanda h", "Reserva base supuesta h", "Refuerzo h",
          "CLP por h", "Refuerzo CLP", "Condición"], coverage)
    save("Soporte-prueba-de-carga.csv",
         ["Tramo", "Agentes", "Llegadas supuestas por h", "Minutos medios de atención",
          "Ocupación %", "Probabilidad espera sobre 15 minutos %"], cases)
    print("182 montajes, 172 externos, 910 h, CLP 11.408.000 en refuerzos de Datos y QA.")
    print(f"Sensibilidad M9: {estimate[-1]}")
    print(f"Erlang C: {cases}")


if __name__ == "__main__":
    main()
