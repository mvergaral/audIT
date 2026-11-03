"""Genera la Gantt de la red T-15 con el lenguaje visual de Presentación-Revision2."""
from pathlib import Path
import json

from reportlab.lib.colors import HexColor, white
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas


HERE = Path(__file__).resolve().parent
ROOT = Path(__file__).resolve().parents[5]
DATA_PATH = ROOT / "Informe-2" / "d2" / "99_Generacion" / "plan_detallado.json"
LOGO_PATH = ROOT / "recursos" / "Formato-Oferta-audIT" / "portadas" / "activos" / "logo-audit.png"
OUTPUT = HERE / "gantt-red-critica.pdf"
DATA = json.loads(DATA_PATH.read_text(encoding="utf-8"))

W, H = 840, 525
NAVY = HexColor("#102D3E")
TEAL = HexColor("#007582")
RED = HexColor("#B3343C")
AMBER = HexColor("#9B5A00")
GRID = HexColor("#D7E2E7")
MUTED = HexColor("#48606E")
PALE_RED = HexColor("#F8ECEC")

LABELS = {
    "A01": "Inicio del proyecto",
    "A02": "Levantamiento y línea base",
    "A03": "Cobertura móvil en terreno",
    "A04": "Factibilidad con terceros",
    "A05": "Arquitectura y datos",
    "A06": "Adhesión de transportistas",
    "A07": "Infraestructura y ambientes",
    "A08": "Migración de vigencias",
    "A09": "Construcción Etapa 1",
    "A10": "Integraciones",
    "A11": "Piloto a bordo",
    "A12": "Certificación Etapa 1",
    "G13": "Entrega G13 a capacitación",
    "A13": "Capacitación",
    "A14": "Reserva Etapa 1",
    "A15": "Marcha blanca E1",
    "A16": "Transferencia tecnológica",
    "A17": "Diseño Etapa 2",
    "A18": "Instalación progresiva",
    "A19": "Paso a producción E1",
    "A20": "Construcción Etapa 2",
    "A21": "Estabilización E1",
    "A22": "Certificación Etapa 2",
    "A23": "Reserva Etapa 2",
    "A24": "Marcha blanca E2",
    "A25": "Producción Etapa 2",
}
CRITICAL = {
    "A01", "A02", "A05", "A07", "A09", "A12", "A14",
    "A17", "A20", "A22", "A23", "A24", "A25",
}
RESERVES = {"A14", "A23"}
TASKS = [task for task in DATA["red"] if task["id"].startswith("A") or task["id"] == "G13"]
if len(TASKS) != 26 or {task["id"] for task in TASKS} != set(LABELS):
    raise ValueError("La red T-15 cambió; revisar los rótulos de la Gantt")
if {task["id"] for task in TASKS if task["critica"] == "Sí"} != CRITICAL:
    raise ValueError("La ruta crítica de T-15 cambió; revisar el énfasis gráfico")
if int(TASKS[-1]["fin_temprano"]) != 420:
    raise ValueError("El horizonte T-15 debe terminar en el día hábil 420")

c = canvas.Canvas(str(OUTPUT), pagesize=(W, H), pageCompression=1)
c.setTitle("Carta Gantt y dependencias: red de 25 actividades")
c.setAuthor("audIT Soluciones Tecnológicas SpA")
c.setFillColor(TEAL)
c.setFont("Helvetica-Bold", 12)
c.drawString(42, 493, "CARTA GANTT Y DEPENDENCIAS / S7 §7.3.1 · T-15 · FEP01 E-25")
c.setFillColor(NAVY)
c.setFont("Helvetica-Bold", 26)
c.drawString(42, 456, "La red de 25 actividades define la ruta crítica.")
c.drawImage(ImageReader(str(LOGO_PATH)), 738, 466, width=76, height=25, mask="auto", preserveAspectRatio=True, anchor="c")

left, right = 250, 816
axis_top, axis_bottom = 408, 88
duration = 420
unit = (right - left) / duration
xday = lambda day: left + int(day) * unit

# Month grid: one contractual month is 20 working days.
c.setStrokeColor(GRID)
c.setLineWidth(0.65)
for month in range(1, 22, 2):
    x = xday((month - 1) * 20)
    c.line(x, axis_bottom, x, axis_top)
    if month not in (13, 19):
        c.setFillColor(NAVY)
        c.setFont("Helvetica", 12)
        c.drawString(x + 2, axis_top + 13, f"M{month}")
c.setStrokeColor(GRID)
c.line(right, axis_bottom, right, axis_top)

# Fixed contractual starts H6/M13 and H11/M19.
for month in (13, 19):
    x = xday((month - 1) * 20)
    c.saveState()
    c.setStrokeColor(AMBER)
    c.setLineWidth(1.2)
    c.setDash(4, 3)
    c.line(x, axis_bottom, x, axis_top)
    c.restoreState()
    c.setFillColor(AMBER)
    c.setFont("Helvetica-Bold", 12)
    c.drawString(x + 4, axis_top + 13, f"M{month}")

row_step = 12.0
first_y = 389
bar_h = 7.5
for index, task in enumerate(TASKS):
    task_id = task["id"]
    y = first_y - index * row_step
    critical = task_id in CRITICAL
    color = RED if critical else TEAL
    c.setFillColor(color)
    c.setFont("Helvetica-Bold" if critical else "Helvetica", 12)
    c.drawString(42, y - 3.6, task_id)
    c.setFillColor(NAVY)
    c.setFont("Helvetica-Bold" if critical else "Helvetica", 12)
    c.drawString(82, y - 3.6, LABELS[task_id])

    start = int(task["inicio_temprano"])
    end = int(task["fin_temprano"])
    if task_id == "G13":
        x = xday(start)
        size = 6
        c.setFillColor(TEAL)
        p = c.beginPath()
        p.moveTo(x, y + size)
        p.lineTo(x + size, y)
        p.lineTo(x, y - size)
        p.lineTo(x - size, y)
        p.close()
        c.drawPath(p, stroke=0, fill=1)
        continue

    x0, x1 = xday(start), xday(end)
    width = max(1.5, x1 - x0)
    if task_id in RESERVES:
        c.saveState()
        c.setStrokeColor(RED)
        c.setFillColor(PALE_RED)
        c.setLineWidth(1.0)
        c.setDash(2, 1.5)
        c.roundRect(x0, y - bar_h / 2, width, bar_h, 2, stroke=1, fill=1)
        c.restoreState()
    else:
        c.setFillColor(color)
        c.roundRect(x0, y - bar_h / 2, width, bar_h, 2.5, stroke=0, fill=1)

# Legend and source line.
c.setStrokeColor(HexColor("#B8CDD5"))
c.setLineWidth(0.8)
c.line(42, 66, W - 42, 66)
legend_y = 49
c.setFillColor(RED)
c.roundRect(42, legend_y, 22, 7, 2, fill=1, stroke=0)
c.setFillColor(NAVY)
c.setFont("Helvetica", 12)
c.drawString(71, legend_y - 2, "Ruta crítica")
c.setFillColor(TEAL)
c.roundRect(207, legend_y, 22, 7, 2, fill=1, stroke=0)
c.setFillColor(NAVY)
c.drawString(236, legend_y - 2, "No crítica")
c.saveState()
c.setStrokeColor(RED)
c.setFillColor(PALE_RED)
c.setDash(2, 1.5)
c.roundRect(352, legend_y, 22, 7, 2, fill=1, stroke=1)
c.restoreState()
c.setFillColor(NAVY)
c.drawString(381, legend_y - 2, "Reserva")
c.setFillColor(TEAL)
p = c.beginPath()
p.moveTo(498, legend_y + 10)
p.lineTo(504, legend_y + 4)
p.lineTo(498, legend_y - 2)
p.lineTo(492, legend_y + 4)
p.close()
c.drawPath(p, stroke=0, fill=1)
c.setFillColor(NAVY)
c.drawString(510, legend_y - 2, "G13")
c.setFont("Helvetica", 12)
c.setFillColor(MUTED)
c.drawString(42, 28, "T-15: precedencias y holguras en días hábiles · M1 = día 0 · M21 = día 420 · G13 condiciona A13 (FS−10).")
c.save()
print(OUTPUT)
