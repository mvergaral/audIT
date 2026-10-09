"""Genera una EDT multipágina editable para diagrams.net."""
from pathlib import Path
from xml.etree import ElementTree as ET
from html import escape

OUT = Path(__file__).resolve().parent / "EDT_D2.drawio"
PAGES = [
 ("01 Gobierno y habilitación", "Gobierno, alcance y habilitación", [
  ("1", "Dirección y control integrado", [("1.1", "Acta de inicio, alcance y línea base integrada"), ("1.2", "Control de cambios, riesgos, dependencias e informes"), ("1.3", "Aceptaciones, transferencia y cierre documental")]),
  ("2", "Requisitos y diseño de solución", [("2.1", "Trazabilidad de 42 requisitos T-12 a paquetes EDT · H1 / M2"), ("2.2", "Arquitectura, seguridad e información aprobadas · H2 / M4"), ("2.3", "Cobertura de rutas, factibilidad de proveedores y costo por ruta antes de renegociar*")]),
  ("3", "Plataforma e integración común", [("3.1", "Ambientes DEV, QA, PREPROD y PROD con observabilidad · H3 / M6"), ("3.2", "Identidad, privacidad, cifrado, auditoría y retención"), ("3.3", "Contratos API, integración, entrega y operación técnica")]),
  ("4", "Fundación de datos", [("4.1", "Inventario y saneamiento de cerca de 6.000 vigencias · RF-005"), ("4.2", "Inventario, migración y conciliación histórica; alcance por acordar"), ("4.3", "Modelo analítico, calidad, linaje y publicación de indicadores")]),
 ], "* Fecha de renegociación y plazo del costo por ruta requieren confirmación del mandante. Fuentes: T-12 y FEP03 §14.1 / §17.5."),
 ("02 Capacidades de Etapa 1", "Capacidades de Etapa 1 y preparación operacional", [
  ("5", "Jornada, cumplimiento y despacho", [("5.1", "Expediente de jornada y documentación · RF-001 a RF-005, RF-007"), ("5.2", "Pre-despacho bloqueante, carga peligrosa y alertas · RF-001, RF-006, RF-027"), ("5.3", "Portales, consentimiento, privacidad e integridad · RF-020 a RF-022, RF-028; RNF-001, RNF-003, RNF-012–014")]),
  ("6", "Flota, viajes y ciclo económico", [("6.1", "Vista operacional y posicionamiento de 374 camiones · RF-008"), ("6.2", "Geocercas, evidencias, buffer y mantenimiento · RF-009 a RF-012, RF-025; RNF-002, RNF-008"), ("6.3", "Costo, liquidación y datos de desempeño · RF-016 a RF-019; línea base RF-023")]),
  ("7", "Integraciones, pruebas y aceptación", [("7.1", "Integración GPS, telemetría, tacógrafo y ERP · RF-007, RF-013, RF-014; RNF-006"), ("7.2", "Pruebas de sistema, desempeño, resiliencia y seguridad · H4 M10 / H5 M12"), ("7.3", "UAT con usuarios del mandante y actas por terminal confirmado"), ("7.4", "Marcha blanca Etapa 1 · 3 meses / M13–M15 · H6"), ("7.5", "Paso Etapa 1 a producción · M16 · H7")]),
  ("8", "Adhesión y despliegue físico", [("8.1", "Adhesión de 148 transportistas: responsable, plazo y riesgo · RF-026"), ("8.2", "Instalación progresiva y conectividad a bordo; cantidades según T-11"), ("8.3", "Capacitación, convivencia operacional, no detención global y reversión · RNF-004, RNF-011")]),
 ], "FEP03 §14.1 informa 374 camiones (148 propios y 226 terceros), con dispositivo de posición en 340/374. El BOM y la intervención de unidades se concilian con T-11."),
 ("03 Etapa 2 y operación", "Etapa 2, operación y transferencia", [
  ("9", "Capacidades de Etapa 2", [("9.1", "Alcance y diseño detallado aprobados · H8 / M14"), ("9.2", "Retornos, analítica, emisiones y talleres · RF-015, RF-018, RF-023, RF-024"), ("9.3", "Construcción e integración para pruebas · H9 / M17"), ("9.4", "Certificación y cierre del desarrollo · H10 / M18"), ("9.5", "Marcha blanca M19–M20 · H11; producción y aceptación M21 · H12"), ("9.6", "Incorporación y aceptación de cinco innovaciones según T-19 vigente")]),
  ("10", "Operación y ciclo de vida", [("10.1", "Soporte y niveles de servicio para ambos alcances · M21–M56 / 36 meses"), ("10.2", "Monitoreo, incidentes, continuidad, recuperación y mantenimiento"), ("10.3", "Versiones, mejora evolutiva y costo total de operación · RNF-009, RNF-010"), ("10.4", "Transferencia de conocimiento y cierre al término del contrato")]),
 ], "Las cinco innovaciones deben concordar con las fichas T-19 vigentes. La EDT agrupa su incorporación; los dueños de esas fichas deben confirmar su alcance."),
]

NAVY, TEAL = "#17324D", "#0F766E"
def add_cell(parent, cid, value, style, pos=None, source=None, target=None):
    attrs = {"id": cid, "value": value, "style": style, "parent": "1"}
    if source:
        attrs.update(edge="1", source=source, target=target)
    else:
        attrs["vertex"] = "1"
    node = ET.SubElement(parent, "mxCell", attrs)
    geom = ET.SubElement(node, "mxGeometry", {"as": "geometry"})
    if source:
        geom.set("relative", "1")
    else:
        for k, v in zip(("x", "y", "width", "height"), pos): geom.set(k, str(v))

mx = ET.Element("mxfile", {"host":"app.diagrams.net", "modified":"2026-10-09T22:00:00.000Z", "agent":"Codex", "version":"25.0.3", "type":"device"})
for n, (pname, title, accounts, note) in enumerate(PAGES, 1):
    d = ET.SubElement(mx, "diagram", {"id":f"edt-d2-{n}", "name":pname})
    model = ET.SubElement(d, "mxGraphModel", {"dx":"1320", "dy":"900", "grid":"1", "gridSize":"10", "guides":"1", "tooltips":"1", "connect":"1", "arrows":"1", "fold":"1", "page":"1", "pageScale":"1", "pageWidth":"1320", "pageHeight":"820", "math":"0", "shadow":"0"})
    r = ET.SubElement(model, "root")
    ET.SubElement(r, "mxCell", {"id":"0"}); ET.SubElement(r, "mxCell", {"id":"1", "parent":"0"})
    add_cell(r, "project", f"Proyecto audIT · Transportes Curimón<br><span style='font-size:11px;font-weight:normal'>EDT D2 · Informe 2 · propuesta de trabajo</span>", f"rounded=1;whiteSpace=wrap;html=1;fillColor={NAVY};strokeColor={NAVY};fontColor=#FFFFFF;fontSize=18;fontStyle=1;align=center;verticalAlign=middle;arcSize=12;", (410,25,500,66))
    count, width = len(accounts), 270
    margin = {2: 300, 3: 180, 4: 25}.get(count, 25)
    gap = (1320 - 2*margin - count*width) / max(1,count-1) if count > 1 else 0
    edges=[]
    for j,(code,name,leaves) in enumerate(accounts):
        x = margin+j*(width+gap); aid=f"a{n}-{code}"
        add_cell(r,aid,f"{code} · {escape(name)}",f"rounded=1;whiteSpace=wrap;html=1;fillColor={TEAL};strokeColor={TEAL};fontColor=#FFFFFF;fontSize=15;fontStyle=1;align=center;verticalAlign=middle;arcSize=10;",(x,125,width,66))
        edges.append((f"e{n}-{code}-root","project",aid))
        for i,(pcode,desc) in enumerate(leaves):
            pid=f"p{n}-{code}-{i}"
            label=f"<b>{escape(code+'.'+pcode)}</b><br>{escape(desc)}"
            add_cell(r,pid,label,"rounded=1;whiteSpace=wrap;html=1;fillColor=#E8F0F6;strokeColor=#A8BBCB;fontColor=#243447;fontSize=12;align=left;verticalAlign=middle;spacingLeft=12;spacingRight=10;spacingTop=6;spacingBottom=6;arcSize=8;",(x,220+i*92,width,72))
            edges.append((f"e{n}-{code}-{i}",aid,pid))
    for eid,src,dst in edges:
        add_cell(r,eid,"","edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#8AA0B3;strokeWidth=1.5;endArrow=none;",source=src,target=dst)
    note_y=220+max(len(a[2]) for a in accounts)*92+4
    label=f"<b>Lectura</b> · Nivel 1: cuenta de control · Nivel 2: paquete de trabajo / entregable verificable.<br>{escape(note)}<br>Alcance común: T-12 y FEP01 Art. 17; fuentes adicionales indicadas aquí."
    add_cell(r,f"note{n}",label,"rounded=1;whiteSpace=wrap;html=1;fillColor=#F6F8FA;strokeColor=#D5DEE6;fontColor=#536779;fontSize=11;align=left;verticalAlign=middle;spacing=12;arcSize=8;",(25,note_y,1270,58))
ET.indent(mx, space="  ")
OUT.write_bytes(ET.tostring(mx,encoding="utf-8",xml_declaration=True))
