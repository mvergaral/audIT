"""Simula la activación de la instalación y verifica el turno y el SLA."""

import csv
from collections import defaultdict
from datetime import datetime, timedelta
from io import BytesIO

from pypdf import PdfReader, PdfWriter
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.util import Inches, Pt
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

from acreditar_fondos import Stress, bank_rate, model, period, size, stage
from probar_cierre_tecnico import agenda, comparison
from regenerar_cierre import CASES, CRITICAL, DEFERRED_RESERVE, FLOOR, OUT, clp, last_weekday
from regenerar_cierre import movements, weekday, workbook


FINAL = OUT / "activacion-simulada"
MONTHS = tuple(sorted({*CRITICAL, 7, 8}))
ROTATION = [(0, 1, 2, 3), (0, 1, 2, 4), (0, 1, 2, 5),
            (3, 4, 5, 0), (3, 4, 5, 1), (3, 4, 5, 2)]
SHIFTS = [(0, 8), (8, 16), (16, 24), (4, 10)]
HEAD_FIN = ["Escenario", "Mes", "Fecha simulada", "Hora", "Movimiento", "Flujo CLP", "Saldo CLP"]
HEAD_ROSTER = ["Fecha simulada", "Inicio", "Fin", "Equipo L1", "Guardia L2 L3", "Suplente"]
HEAD_SLA = ["Prueba simulada", "Respuesta min", "Diagnóstico min", "Recuperación min", "Total min", "Resultado"]


def treasury_input():
    base = size(Stress(12), {}, 1)
    variants = [(name, stress, delayed, model(stress, stage(stress, base, 16), 16))
                for name, stress, delayed in CASES]
    invoices = {row[0]: row[5] for row in comparison(agenda())}
    return variants, invoices


def evaluate(capital, variants, invoices):
    loan = capital * 4 // 5
    trace = []
    summary = []
    for name, stress, delayed, rows in variants:
        opening_adjustment = 0
        for row in rows[:56]:
            month = row["mes"]
            cash = row["caja_apertura"] + opening_adjustment
            if delayed and month == 13:
                cash += DEFERRED_RESERVE
            injection = capital if month == 9 else 0
            interest = loan * bank_rate if 10 <= month <= 21 else 0
            loan_repayment = loan if month == 21 else 0
            gross_bill = invoices.get(month, 0)
            net_change = injection - gross_bill - interest - loan_repayment
            closing = row["caja_cierre"] + opening_adjustment + net_change
            if delayed and month == 12:
                closing += DEFERRED_RESERVE
            opening_adjustment += net_change
            if month not in MONTHS:
                summary.append((name, month, closing, closing))
                continue
            events = movements(row, stress, delayed)
            if injection:
                events.extend([(weekday(9, 1), "08:15", "Desembolso adicional banco", loan),
                               (weekday(9, 1), "08:20", "Aporte adicional socios", capital-loan)])
            if gross_bill:
                events.append((last_weekday(month), "16:30", "Pago bruto montaje externo", -gross_bill))
            if interest:
                events.append((weekday(month, 21), "13:10", "Interés crédito adicional", -interest))
            if loan_repayment:
                events.append((last_weekday(21), "16:10", "Amortización crédito adicional", -loan_repayment))
            trace.append((name, month, period(month).isoformat(), "00:00", "Apertura", cash, cash))
            balances = [cash] if month != 1 else []
            for when, hour, item, value in sorted(events):
                cash += value
                trace.append((name, month, when, hour, item, value, cash))
                if month != 1 or hour >= "08:10":
                    balances.append(cash)
            assert abs(cash - closing) < 0.005
            summary.append((name, month, min(balances), closing))
    return trace, summary


def dimension():
    inputs = treasury_input()
    low, high = 0, 10_000_000 // 5
    while low < high:
        mid = (high + low) // 2
        if min(r[2] for r in evaluate(mid * 5, *inputs)[1]) >= FLOOR:
            high = mid
        else:
            low = mid + 1
    minimum = low * 5
    trace, summary = evaluate(minimum, *inputs)
    assert min(r[2] for r in summary) >= FLOOR
    assert min(r[2] for r in evaluate(minimum-5, *inputs)[1]) < FLOOR
    return minimum, trace, summary


def duty_roster():
    start = datetime(2028, 10, 1)
    people = defaultdict(list)
    result = []
    for i in range(31):
        day = start + timedelta(days=i)
        for who, (begin, end) in zip(ROTATION[i % 6], SHIFTS):
            a, b = day + timedelta(hours=begin), day + timedelta(hours=end)
            people[who].append((a, b))
            result.append((day.date().isoformat(), a.strftime("%H:%M"),
                           "24:00" if end == 24 else b.strftime("%H:%M"),
                           f"L1-{who+1}", f"G-{i%8+1}", f"G-{(i+1)%8+1}"))
    for slots in people.values():
        assert sum((b-a).total_seconds()/3600 for a,b in slots) <= 160
        assert all((next_slot[0]-prior[1]).total_seconds()/3600 >= 12
                   for prior,next_slot in zip(slots,slots[1:]))
    assert all(any(a <= start+timedelta(hours=h) < b for slots in people.values() for a,b in slots)
               for h in range(31*24))
    return result


def critical_sla():
    cases = [("Dos críticas simultáneas", 5 + 2*5, 30, 180),
             ("Tres críticas con suplente al minuto 10", max(5+2*5, 10+5), 30, 180),
             ("Tres críticas sin suplente", 5+3*5, 30, 180),
             ("Proveedor tarda 240 min desde diagnóstico", 15, 30, 240)]
    result = [(case, ack, diag, restore, ack+diag+restore,
               "Cumple tiempo simulado" if ack<=15 and ack+diag+restore<=240 else "Incumple")
              for case,ack,diag,restore in cases]
    assert [r[-1] for r in result]==["Cumple tiempo simulado","Cumple tiempo simulado","Incumple","Incumple"]
    assert 40 <= 28*24*60*0.001 < 50
    return result


def csv_file(name, header, rows):
    with (FINAL / name).open("w", encoding="utf-8-sig", newline="") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(header)
        writer.writerows([f"{v:.2f}".replace(".", ",") if isinstance(v, float) else v for v in row] for row in rows)


def write_pdf(capital):
    styles = getSampleStyleSheet()
    story = []
    loan = capital * 4 // 5
    data = [
        ("Activación simulada · Instalación y SLA", "Title"),
        ("TFEP-01/2026 · Informe 3 · 14 de noviembre de 2026", "BodyText"),
        ("Decisión del ejercicio", "Heading2"),
        ("El piloto de 10 instalaciones se mantiene con audIT. Se simulan 172 montajes físicos externos "
         "por CLP 6.421.333 netos y CLP 7.641.386 brutos, pagados por lote en M7–M9. "
         "La orden de cada lote requiere recepción del piloto, visita elegible, puesto, kit, analista "
         "y técnico. La contraparte académica contempla autorización escrita condicionada al Art. 73. "
         "audIT conserva integración, credenciales, QA, recepción y responsabilidad.", "BodyText"),
        ("Cobertura financiera", "Heading2"),
        (f"Se simula en M9 un desembolso adicional de CLP {clp(capital)} "
         f"(banco {clp(loan)} y socios {clp(capital-loan)}), manteniendo nómina completa "
         "y pagando las facturas brutas al cierre de cada mes, sin crédito fiscal dentro del horizonte. "
         "El crédito adicional aplica 0,9 % mensual sobre saldo de apertura y se amortiza en M21. "
         "La simulación verifica 56 cierres, 11 meses por fecha y cuatro escenarios, con piso de "
         "CLP 10 millones y cero giros de línea. Incorpora el atraso simulado de H6 y el diferimiento "
         "de CLP 19.510.000 de una reserva reprogramable.", "BodyText"),
        ("Prueba de soporte", "Heading2"),
        ("Seis agentes L1 en un ciclo de seis días cubren 24 horas y refuerzan seis horas diarias. "
         "Se probó un mes de 31 días, 930 horas asignadas y descanso interno mínimo de 12 horas. "
         "Ocho perfiles L2/L3 alternan guardia primaria y suplencia. Datos y QA conservan 103 h "
         "mensuales de refuerzo en M21–M24. En los casos críticos probados, el presupuesto de "
         "tiempo es de 225 minutos con recuperación en 180 minutos desde diagnóstico. "
         "Tres incidentes simultáneos requieren apoyo paralelo. Un proveedor que demora 240 "
         "minutos desde diagnóstico excede el SLA de 4 horas.", "BodyText"),
        ("Condiciones de acreditación", "Heading2"),
        ("Este anexo documenta la simulación académica. Para habilitar la operación, se deben "
         "medir los tiempos del piloto, confirmar visitas y recepciones, obtener la cotización y "
         "autorización escritas, y comprobar turnos y demanda real. Se debe probar la recuperación "
         "y registrar minutos de indisponibilidad por separado, con el acuerdo de soporte firmado.", "BodyText"),
    ]
    for text,style in data:
        story.extend([Paragraph(text,styles[style]),Spacer(1,7)])
    b = BytesIO()
    SimpleDocTemplate(b, leftMargin=55, rightMargin=55, topMargin=52, bottomMargin=45).build(story)
    b.seek(0)
    w=PdfWriter()
    w.append(PdfReader(OUT/"INFORME3_AUDIT_COSTOS_VENTA_CONSOLIDADO.pdf"))
    w.append(b, outline_item="Activación simulada de instalación y SLA")
    w.write(FINAL/"Informe-3-Activacion-simulada.pdf")


def write_slide(capital):
    deck=Presentation(OUT/"AUDIT-Informe3-Presentacion-Economica.pptx")
    slide=deck.slides.add_slide(min(deck.slide_layouts, key=lambda layout: len(layout.placeholders)))
    content=[
        ("Activación simulada del montaje y soporte", .62, 34),
        ("172 montajes externos después del piloto · CLP 7,64 millones brutos", 1.51, 22),
        (f"Refuerzo en M9 de CLP {clp(capital)} al mantener la nómina y pagar el IVA. Los cuatro escenarios conservan el piso de CLP 10 millones.", 2.40, 20),
        ("Turno 24×7 probado con seis agentes L1, cobertura adicional en horas pico y guardia primaria y suplente.", 3.52, 20),
        ("Recuperación crítica en 225 minutos bajo supuestos. Tres críticas simultáneas requieren apoyo paralelo.", 4.57, 20),
        ("Pendientes de ejecución: aceptación del piloto, autorización escrita, turnos efectivos y ensayo de recuperación.", 5.62, 19),
        ("Informe 3 · Simulación académica · audIT / Curimón", 6.91, 12),
    ]
    for text, top, font in content:
        box=slide.shapes.add_textbox(Inches(.8), Inches(top), deck.slide_width-Inches(1.6), Inches(.85))
        box.text_frame.word_wrap=True
        run=box.text_frame.paragraphs[0].add_run()
        run.text=text
        run.font.name="Aptos"
        run.font.size=Pt(font)
        run.font.bold=font>=22
        run.font.color.rgb=RGBColor.from_string("087968" if font==22 else "12304A")
    deck.save(FINAL/"Presentacion-activacion-simulada.pptx")


def main():
    capital, trace, summary = dimension()
    roster = duty_roster()
    cases = critical_sla()
    FINAL.mkdir(exist_ok=True)
    csv_file("Caja-activacion-montaje.csv", HEAD_FIN, trace)
    csv_file("Turno-L1-y-guardia.csv", HEAD_ROSTER, roster)
    csv_file("Pruebas-SLA-critico.csv", HEAD_SLA, cases)
    workbook([
        ("Caja activacion montaje", [HEAD_FIN, *trace], True),
        ("Cierres activacion", [["Escenario", "Mes", "Mínimo CLP", "Cierre CLP"], *summary], False),
        ("Turnos L1 y guardia", [HEAD_ROSTER, *roster], False),
        ("Casos SLA critico", [HEAD_SLA, *cases], False),
    ], previous=OUT/"AUDIT-Informe3-Modelo-Economico.xlsx",
        destination=FINAL/"Modelo-activacion-simulada.xlsx")
    write_pdf(capital)
    write_slide(capital)
    worst=min(summary,key=lambda row: row[2])
    print(f"Capital simulado M9: {capital}; banco {capital*4//5}; socios {capital//5}")
    print(f"Mínimo por fecha y cierre: {worst}; {len(trace)} eventos; {len(summary)} cierres; {len(roster)} turnos.")


if __name__=="__main__":
    main()
