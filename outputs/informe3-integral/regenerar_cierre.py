"""Consolida los respaldos del cierre en copias del paquete c9a6515."""

import csv
from datetime import date, timedelta
from io import BytesIO
from pathlib import Path
from subprocess import check_output
from zipfile import ZipFile

from lxml import etree as XML
from pypdf import PdfReader, PdfWriter
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.util import Inches, Pt
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import PageBreak, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

from acreditar_fondos import Stress, model, period, size, stage
from reproducir import CUT, ROOT, book, flux, h5, vat_rate


OUT = Path(__file__).resolve().parent / "entrega-consolidada"
FLOOR = 10_000_000
DEFERRED_RESERVE = 19_510_000
CRITICAL = (1, 9, 10, 12, 13, 14, 15, 16, 21)
INSTALL = [(6, 10), (7, 60), (8, 60), (9, 52)]
CASES = [
    ("H5 M13 / reserva M12", Stress(13, 12), False),
    ("H5 M14 / reserva M12", Stress(14, 12), False),
    ("H5 M14 / reserva M9", Stress(14, 9), False),
    ("H6 atrasado / H5 M14", Stress(14, 12), True),
]


def source(filename):
    return BytesIO(check_output(["git", "show", f"{CUT}:Informe-3/{filename}"], cwd=ROOT))


def clp(amount):
    return f"{amount:,.0f}".replace(",", ".")


def millions(amount):
    return f"{amount / 1_000_000:,.2f}".replace(",", " ").replace(".", ",").replace(" ", ".")


def weekday(month, day):
    planned = period(month).replace(day=day)
    while planned.weekday() >= 5:
        planned += timedelta(days=1)
    return planned.isoformat()


def last_weekday(month):
    planned = period(month + 1) - timedelta(days=1)
    while planned.weekday() >= 5:
        planned -= timedelta(days=1)
    return planned.isoformat()


def movements(row, stress, delayed):
    m = row["mes"]
    events = []

    def add(when, hour, label, amount):
        if abs(amount) > 0.001:
            events.append((when, hour, label, amount))

    add(weekday(m, 1), "08:00", "Desembolso banco", row["banco_abonado"])
    add(weekday(m, 1), "08:10", "Aporte socios", row["socios_abonado"])
    h5_gross = h5[5] * (1 + vat_rate) if m == stress.collection else 0
    add(weekday(m, 15 if m == 13 else 1), "11:00", "Cobro H5 con IVA", h5_gross)
    collection = row["cobro_neto"] + row["iva_cobrado"] - h5_gross
    add(weekday(m, 17 if m == 13 and delayed else 15), "09:00",
        {10: "H4", 13: "H6", 14: "H8", 16: "H7", 21: "H12"}.get(m, "Cobro ordinario")
        + " con IVA", collection)
    add(weekday(m, 16), "12:00", "IVA del mes previo", -row["entero_iva"])
    add(weekday(m, 17), "15:00", "Egresos netos distintos de nómina e IVA de compras", -(
        row["egreso_neto"] - book["Costos"].cell(m + 1, 7).value + row["iva_compra"] + row["iva_calibracion"]))
    add(weekday(m, 21), "12:00", "Interés bancario y comisión", -row["interes"] - row["comision"])
    add(weekday(m, 21), "13:00", "Horas condicionales de preparación", -row["compra_horas"])
    reserve = row["reserva_d4"] - (DEFERRED_RESERVE if delayed and m == 12 else 0)
    add(weekday(m, 24), "12:00", "Pago reserva D4", -reserve)
    if delayed and m == 13:
        add(weekday(m, 17), "10:00", "Liberación de reserva D4 tras H6", -DEFERRED_RESERVE)
    add(last_weekday(m), "14:00", "Nómina", -book["Costos"].cell(m + 1, 7).value)
    add(last_weekday(m), "15:00", "Amortización puente", -row["repago_puente"])
    add(last_weekday(m), "16:00", "Amortización inicial", -row["principal_banco"])
    return sorted(events)


def treasury():
    records = []
    month_summaries = []
    base = size(Stress(12), {}, 1)
    for name, stress, delayed in CASES:
        rows = model(stress, stage(stress, base, 16), 16)
        assert all(row["caja_cierre"] >= FLOOR and not row["saldo_linea"] for row in rows[:56])
        for month in CRITICAL:
            row = rows[month - 1]
            opening = row["caja_apertura"] + (DEFERRED_RESERVE if delayed and month == 13 else 0)
            balance = opening
            records.append((name, month, period(month).isoformat(), "00:00", "Apertura", opening, balance))
            balances = [] if month == 1 else [opening]
            for when, hour, label, amount in movements(row, stress, delayed):
                balance += amount
                records.append((name, month, when, hour, label, amount, balance))
                if month != 1 or hour >= "08:10":
                    balances.append(balance)
            expected = row["caja_cierre"] + (DEFERRED_RESERVE if delayed and month == 12 else 0)
            assert abs(balance - expected) < 0.005, (name, month, balance, expected)
            minimum = min(balances)
            assert minimum >= FLOOR, (name, month, minimum)
            month_summaries.append((name, month, minimum, balance))
    return records, month_summaries


def operating_rows():
    rows = [["Tipo", "Período", "Cantidad", "Horas técnico", "Horas analista",
             "Horas totales", "CLP de referencia", "Estado"]]
    for month, count in INSTALL:
        rows.append(["Instalación EDT 4.2", f"M{month}", count, count * 160 / 60,
                     count * 140 / 60, count * 5, count * (160 * 16000 + 140 * 20000) / 60,
                     "Carga referencial en nómina; confirmar correspondencia con T-15"])
    rows.extend([
        ["Balizas base", "Agenda pendiente", 210, "", "", 52.5, "",
         "Perfil, terminal y pago pendientes"],
        ["Soporte fabricante D4", "M13–M56", 44, "", "", "", 3331927,
         "CLP por mes; incluido en proveedores"],
        ["Mesa de servicio EDT 13.1", "M21–M56", 6, "", "", 960, "",
         "Horas por mes de T-15; atención 24x7"],
        ["Plataforma y servicio EDT 13.2", "M21–M56", 4, "", "", 640, "",
         "Horas por mes de T-15"],
        ["Ciclo de vida EDT 13.3", "M21–M56", 2, "", "", 320, "",
         "Horas por mes; carga presupuestada de todo el paquete"],
        ["Mantención evolutiva EDT 13.4", "M21–M56", 4, "", "", 640, "",
         "Horas por mes de T-15"],
        ["Nómina total", "M21–M24", 4, "", "", "", 88252000, "CLP por mes; incluye varios roles"],
        ["Nómina total", "M25–M56", 32, "", "", "", 85400000, "CLP por mes; diferencia de CLP 2.852.000"],
    ])
    assert sum(row[2] for row in rows[1:5]) == 182 and sum(row[5] for row in rows[1:5]) == 910
    return rows


NS = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"
OFFICE = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
REL = "http://schemas.openxmlformats.org/package/2006/relationships"
TYPES = "http://schemas.openxmlformats.org/package/2006/content-types"


def sheet_xml(rows, balance_formula):
    sheet = XML.Element(f"{{{NS}}}worksheet", nsmap={None: NS})
    views = XML.SubElement(sheet, f"{{{NS}}}sheetViews")
    view = XML.SubElement(views, f"{{{NS}}}sheetView", workbookViewId="0")
    XML.SubElement(view, f"{{{NS}}}pane", ySplit="1", topLeftCell="A2", activePane="bottomLeft", state="frozen")
    cols = XML.SubElement(sheet, f"{{{NS}}}cols")
    widths = [31, 18, 18, 17, 55, 20, 22, 67]
    for n, width in enumerate(widths, 1):
        XML.SubElement(cols, f"{{{NS}}}col", min=str(n), max=str(n), width=str(width), customWidth="1")
    data = XML.SubElement(sheet, f"{{{NS}}}sheetData")
    for i, line in enumerate(rows, 1):
        row = XML.SubElement(data, f"{{{NS}}}row", r=str(i))
        for n, value in enumerate(line):
            node = XML.SubElement(row, f"{{{NS}}}c", r=f"{chr(65+n)}{i}")
            if isinstance(value, str):
                node.set("t", "inlineStr")
                item = XML.SubElement(node, f"{{{NS}}}is")
                XML.SubElement(item, f"{{{NS}}}t").text = value
            else:
                if balance_formula and n == 6:
                    formula = f"F{i}" if line[4] == "Apertura" else f"G{i-1}+F{i}"
                    XML.SubElement(node, f"{{{NS}}}f").text = formula
                XML.SubElement(node, f"{{{NS}}}v").text = str(value)
    return XML.tostring(sheet, encoding="UTF-8", xml_declaration=True)


def workbook(tabs, previous=None, destination=None):
    filename = "AUDIT-Informe3-Modelo-Economico.xlsx"
    with ZipFile(previous or source(filename)) as original, ZipFile(destination or OUT / filename, "w", compression=8) as result:
        manifests = {name: XML.fromstring(original.read(name)) for name in (
            "xl/workbook.xml", "xl/_rels/workbook.xml.rels", "[Content_Types].xml")}
        sheets = manifests["xl/workbook.xml"].find(f"{{{NS}}}sheets")
        next_id = max(int(sheet.get("sheetId")) for sheet in sheets) + 1
        for index, (name, rows, formulas) in enumerate(tabs, next_id):
            relationship = f"rIdCierre{index}"
            target = f"worksheets/cierre{index}.xml"
            node = XML.SubElement(sheets, f"{{{NS}}}sheet", name=name, sheetId=str(index))
            node.set(f"{{{OFFICE}}}id", relationship)
            XML.SubElement(manifests["xl/_rels/workbook.xml.rels"], f"{{{REL}}}Relationship",
                           Id=relationship, Type=f"{OFFICE}/worksheet", Target=target)
            XML.SubElement(manifests["[Content_Types].xml"], f"{{{TYPES}}}Override",
                           PartName=f"/xl/{target}", ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml")
            result.writestr(f"xl/{target}", sheet_xml(rows, formulas))
        for item in original.infolist():
            content = XML.tostring(manifests[item.filename], encoding="UTF-8", xml_declaration=True) if item.filename in manifests else original.read(item)
            result.writestr(item, content)


NAVY = "#12304A"
TEAL = "#087968"
PENDING = (
    "Instalación: quedan por acreditar la agenda por terminal, la cotización externa, la autorización "
    "del mandante y las horas de nómina sustituibles. Soporte: quedan por conciliar dotación, volumen "
    "de atención y cobertura del SLA por tramo. Los importes identificados se mantienen en sus cuentas de origen."
)


def annex_tables():
    return [
        ["Escenario reserva", "Banco M9", "Banco M12", "Socios M9", "Socios M12"],
        ["Pago en M9", "123.772.620", "186.019.528", "30.943.155", "46.504.882"],
        ["Pago en M12", "1.612.800", "305.521.560", "403.200", "76.380.390"],
    ]


def report(summaries):
    styles = getSampleStyleSheet()
    styles["Title"].textColor = colors.HexColor(NAVY)
    styles["Heading2"].textColor = colors.HexColor(TEAL)
    story = []

    def para(s, style="BodyText"):
        story.extend([Paragraph(s, styles[style]), Spacer(1, 8)])

    def table(rows, widths=None):
        t = Table(rows, colWidths=widths, repeatRows=1, hAlign="LEFT")
        t.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor(NAVY)),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.HexColor("#EEF4F8"), colors.white]),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
            ("FONTSIZE", (0, 0), (-1, -1), 9),
        ]))
        story.extend([t, Spacer(1, 12)])

    para("Cierre económico · Informe 3", "Title")
    para("TFEP-01/2026 · audIT / Transportes Curimón · 14 de noviembre de 2026")
    para("Simulación académica · Addendum al corte c9a6515. Los importes de este addendum corresponden a las nuevas pruebas de tesorería. El cuerpo original conserva las cifras de sus escenarios históricos.")
    para("La caja se mantiene sobre el piso de CLP 10 millones en los nueve meses críticos para cuatro secuencias simuladas. La prueba parte de los 56 cierres mensuales conciliados. M1 se mide desde el desembolso que precede a los egresos.", "BodyText")
    labels = ["H5 feb. / reserva ene.", "H5 mar. / reserva ene.", "H5 mar. / reserva oct.", "H6 atrasado"]
    table([["Mes", *labels]] + [[f"M{m}", *[millions(row[2]) for row in summaries if row[1] == m]] for m in CRITICAL],
          [45, 113, 113, 113, 98])
    para("Saldos mínimos en millones de CLP. Las fechas de IVA, proveedores y nómina son supuestos de tesorería para el ejercicio.")
    para("Secuencia M13: H6 el 15 de febrero a las 09:00, H5 a las 11:00 en la prueba de 15 días, "
         "IVA el 16, proveedores el 17, administración e intereses el 21 y nómina el 29. "
         "Con H5 en marzo, el saldo del cierre de febrero es CLP 10.000.002,98.")
    para("Contingencia H6. Si H5 pasa a marzo y H6 pasa del 15 al 17 de febrero, pagar el IVA el 16 exige CLP 19.506.394 adicionales para mantener el piso. El escenario prueba diferir CLP 19.510.000 de la reserva de enero al 17 de febrero, con abono de H6 a las 09:00 y liberación a las 10:00. Requiere que esa partida de reserva admita el diferimiento.")
    story.append(PageBreak())
    para("Anexos aprobados de financiamiento y pago", "Title")
    para("Simulación académica · 14 de noviembre de 2026")
    para("1. Carta de disponibilidad de financiamiento", "Heading2")
    para("Emisor ficticio. Para el ejercicio, la entidad financiera contempla un desembolso inicial de CLP 266.251.504 antes del primer egreso de M1 y financiamiento contingente neto hasta CLP 309.792.148. Se aplica 0,9 % mensual sobre el saldo de apertura y una comisión ilustrativa de CLP 250.000 en M12 bajo estrés. El principal inicial se amortiza en M21 y el refuerzo en M16, sujeto a H5 y H7.")
    para("2. Acuerdo de aporte de socios", "Heading2")
    para("Los socios de audIT aportan CLP 66.562.876 antes del primer egreso de M1 y comprometen hasta CLP 77.448.037 contingentes para el ejercicio. Los aportes coinciden con los giros bancarios y representan el 20 % de cada tramo.")
    table(annex_tables())
    para("Importes en CLP. Los calendarios de refuerzo son alternativos.")
    para("3. Confirmación del plazo de H5", "Heading2")
    para("Contraparte simulada de Curimón. La factura de H5 se emite al suscribirse el acta de aceptación. El plazo de pago de ejercicio es de 15 días corridos desde la recepción válida. El acta y la recepción se simulan el 31 de enero de 2028, con abono el 15 de febrero. La prueba a 30 días traslada el abono al 1 de marzo. H5 conserva M12 y el monto neto de CLP 461.880.281,50.")
    story.append(PageBreak())
    para("Instalación y soporte · Conciliación", "Title")
    para("EDT 4.2 / A11 y A18. Los 182 montajes incluyen 34 comodatos y 10 montajes de piloto. La referencia D2 usa 160 minutos de técnico (incluye banco) y 140 minutos de analista. Sus costos provisionales son CLP 16.000 y CLP 20.000 por hora.")
    table([["Mes", "Kits", "Horas-persona", "CLP de referencia"]] +
          [[f"M{m}", n, n * 5, clp(n * (160 * 16000 + 140 * 20000) / 60)] for m, n in INSTALL] +
          [["Total", 182, 910, "16.258.667"]])
    para("El total usa precisión completa. Las 210 balizas requieren otras 52,5 horas-persona. Si el externo sustituye solo los 140 minutos del técnico a bordo, el costo interno comparable es CLP 37.333 por kit (CLP 6.794.667 en total). Este valor sirve para comparar cotizaciones. La decisión requiere verificar las horas sustituibles y obtener autorización escrita conforme al Art. 73.")
    para("Soporte. D4 presupuesta CLP 3.331.927 mensuales de fabricante y mantención en M13–M56. T-15 asigna desde M21 un total de 2.560 h/mes: 960 a mesa 24x7, 640 a plataforma, 320 al ciclo de vida a bordo y 640 a mantención evolutiva. La nómina global pasa de CLP 88.252.000 al mes en M21–M24 a CLP 85.400.000 desde M25. El descenso agregado es CLP 2.852.000 al mes.")
    para(PENDING)
    para("Fuentes. T-14/T-15, AUD-14/15/21 y AUD-33/34/37. Cálculo interno a partir del modelo versionado c9a6515. Los horarios de tesorería y las pruebas de sensibilidad fueron preparados con apoyo de IA.")
    path = "INFORME3_AUDIT_COSTOS_VENTA_20261113.pdf"
    original = PdfReader(source(path))

    def footer(canvas, doc):
        canvas.setFont("Helvetica", 8)
        canvas.setFillColor(colors.HexColor(NAVY))
        canvas.drawString(52, 31, "TFEP-01/2026 · Addendum de cierre económico")
        canvas.drawRightString(doc.pagesize[0] - 52, 31, str(len(original.pages) + doc.page))

    buffer = BytesIO()
    SimpleDocTemplate(buffer, leftMargin=52, rightMargin=52, topMargin=56, bottomMargin=48).build(
        story, onFirstPage=footer, onLaterPages=footer)
    buffer.seek(0)
    merged = PdfWriter()
    merged.append(original)
    merged.append(buffer, outline_item="Cierre económico y anexos simulados")
    merged.write(OUT / "INFORME3_AUDIT_COSTOS_VENTA_CONSOLIDADO.pdf")


def slides():
    path = "AUDIT-Informe3-Presentacion-Economica.pptx"
    deck = Presentation(source(path))
    for title, lead, points in [
        ("Liquidez en los meses críticos", "Piso simulado de CLP 10 millones",
         ["Capital M1 de CLP 332,81 millones y refuerzo por tramos de hasta CLP 387,24 millones.",
          "H6 entra el 15 de febrero antes del IVA de M13. H5 se prueba el 15 de febrero y el 1 de marzo.",
          "Si H6 pasa al 17, el diferimiento de CLP 19,51 millones de reserva cubre el IVA del 16.",
          "Nueve meses críticos cotejados en cuatro escenarios con fechas simuladas."]),
        ("Instalación y soporte", "Trazabilidad de las partidas",
         ["182 montajes de EDT 4.2. Referencia de 910 horas-persona y CLP 16,26 millones.",
          "Los 10 kits de piloto y los 34 comodatos están incluidos. Hay 210 balizas con 52,5 horas adicionales.",
          "Fabricante y mantención D4 por CLP 3,33 millones mensuales en M13–M56.",
          "Agenda por terminal, cotización externa y cobertura SLA por rol siguen por acreditar."]),
    ]:
        layout = min(deck.slide_layouts, key=lambda candidate: len(candidate.placeholders))
        slide = deck.slides.add_slide(layout)
        for idx, (value, top, font_size, bold) in enumerate(
                [(title, .64, 36, True), (lead, 1.44, 22, True)] +
                [(point, 2.3 + i * .77, 20, False) for i, point in enumerate(points)] +
                [("Informe 3 · Simulación académica · audIT / Curimón", 6.9, 12, False)]):
            box = slide.shapes.add_textbox(Inches(.8), Inches(top), deck.slide_width - Inches(1.6), Inches(.70))
            box.text_frame.word_wrap = True
            p = box.text_frame.paragraphs[0]
            run = p.add_run()
            run.text = value
            run.font.name = "Aptos"
            run.font.size = Pt(font_size)
            run.font.bold = bold
            run.font.color.rgb = RGBColor.from_string((TEAL if idx == 1 else NAVY).strip("#"))
    deck.save(OUT / path)


def main():
    records, summaries = treasury()
    headers = ["Escenario", "Mes", "Fecha simulada", "Hora", "Movimiento", "Flujo CLP", "Saldo CLP"]
    with (OUT / "Tesoreria-orden-simulado.csv").open("w", encoding="utf-8-sig", newline="") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(headers)
        writer.writerows([*r[:5], *[f"{v:.2f}".replace(".", ",") for v in r[5:]]] for r in records)
    workbook([
        ("Caja por fecha simulada", [headers, *records], True),
        ("Minimos meses criticos", [["Escenario", "Mes", "Mínimo CLP", "Cierre CLP"], *summaries], False),
        ("Instalacion y soporte", operating_rows(), False),
        ("Anexos simulados", [
            ["Concepto", "Mes", "Importe o fecha", "Condición"],
            ["Banco inicial", 1, 266251504, "Antes del primer egreso"],
            ["Socios inicial", 1, 66562876, "Antes del primer egreso"],
            ["Banco contingente máximo", "9 y 12", 309792148, "Ver tramos alternativos del PDF"],
            ["Socios contingente máximo", "9 y 12", 77448037, "Ver tramos alternativos del PDF"],
            ["H5 a 15 días", 13, "2028-02-15", "Acta y recepción simuladas el 31-01-2028"],
            ["H5 a 30 días", 14, "2028-03-01", "Sensibilidad"],
            ["Diferimiento de reserva", 13, DEFERRED_RESERVE, "Alternativa si H6 pasa al 17-02"],
        ], False),
    ])
    report(summaries)
    slides()
    print(f"{len(records)} movimientos y {len(summaries)} conciliaciones de tesorería")


if __name__ == "__main__":
    main()
