#!/usr/bin/env python3
"""Genera el código TikZ de las figuras de la EDT y de la carta Gantt del
Subdocumento 7. Los datos de esta fuente son los mismos de la EDT del
Formulario T-14 y de la red del Formulario T-15. Uso:
    python3 figuras_tikz.py > figuras_generadas.tex
Se pega cada bloque dentro de su figuraNativa en contenido.tex."""

EDT = [
    ("1", "Gestión del proyecto", ["1.1 Dirección y control", "1.2 Interesados y comunicaciones",
                                    "1.3 Hardware del mandante"]),
    ("2", "Levantamiento y diseño", ["2.1 Línea base y catálogo", "2.2 Cobertura móvil en terreno",
                                     "2.3 Factibilidad con terceros", "2.4 Arquitectura y datos",
                                     "2.5 Estudio de costo por ruta"]),
    ("3", "Plataforma", ["3.1 Ambientes y despliegue", "3.2 Seguridad e identidad",
                         "3.3 Observabilidad", "3.4 San Bernardo y gabinetes"]),
    ("4", "Equipo a bordo", ["4.1 Firmware y gestión remota", "4.2 Montaje camión por camión",
                             "4.3 Integración de terceros"]),
    ("5", "Servicios de la Etapa 1", ["5.1 Personas y cumplimiento", "5.2 Flota y activos",
                                      "5.3 Planificación y tráfico", "5.4 Telemetría y geocercas",
                                      "5.5 Operación de fletes", "5.6 Liquidación y costeo",
                                      "5.7 Portal del transportista"]),
    ("6", "Integraciones", ["6.1 Sistema contable", "6.2 Plataformas de posición",
                            "6.3 Telemetría y tacógrafo", "6.4 Combustible, peaje y taller",
                            "6.5 Sistema de 2013 y su retiro"]),
    ("7", "Datos y migración", ["7.1 Migración de vigencias", "7.2 Migración histórica",
                                "7.3 Repositorio analítico"]),
    ("8", "Servicios de la Etapa 2", ["8.1 Portal del cliente", "8.2 Asignación de retornos",
                                      "8.3 Emisiones", "8.4 Talleres y mantenimiento",
                                      "8.5 Dispersión de rendimiento"]),
    ("9", "Adhesión de transportistas", ["9.1 Anexo de adhesión", "9.2 Campaña y enrolamiento",
                                         "9.3 Medición y refuerzo"]),
    ("10", "Calidad y pruebas", ["10.1 Sistema e integración", "10.2 Desempeño y seguridad",
                                 "10.3 Aceptación de usuario"]),
    ("11", "Implantación", ["11.1 Capacitación", "11.2 Marcha blanca, Etapa 1",
                            "11.3 Marcha blanca, Etapa 2", "11.4 Estabilización y traspaso"]),
    ("12", "Innovaciones", ["12.1 a 12.5, una por innovación"]),
    ("13", "Operación de 36 meses", ["13.1 Mesa de servicio 24x7", "13.2 Operación de la plataforma",
                                     "13.3 Ciclo de vida del equipo a bordo", "13.4 Mantención evolutiva"]),
]

LH = 4.3   # alto de línea en mm
GAP = 2.2  # espacio entre grupos en mm


def edt():
    cols = [EDT[:6], EDT[6:]]
    out = [r"\begin{tikzpicture}[",
           r"  t/.style={font=\sffamily\fontsize{9.5bp}{11bp}\selectfont\color{audit-tinta},anchor=west,inner sep=0.6mm},",
           r"  n1/.style={font=\sffamily\bfseries\fontsize{9.5bp}{11bp}\selectfont\color{audit-marino},anchor=west,inner sep=0.6mm},",
           r"  ln/.style={draw=audit-filete,line width=0.6pt}]",
           r"  \node[draw=audit-marino,line width=0.7pt,fill=audit-gris-claro,font=\sffamily\bfseries\fontsize{9.5bp}{11bp}\selectfont\color{audit-marino},minimum width=146mm,minimum height=8mm] (raiz) at (73mm,6mm) {Plataforma de control de jornada, flota y viaje para Transportes Curimón};"]
    for ci, col in enumerate(cols):
        x0 = 2 + ci * 75
        y = -4.0
        titles = []
        for code, name, kids in col:
            titles.append(y)
            out.append(rf"  \draw[ln] ({x0}mm,{y:.1f}mm) -- ({x0 + 3}mm,{y:.1f}mm);")
            out.append(rf"  \node[n1] at ({x0 + 3}mm,{y:.1f}mm) {{{code} {name}}};")
            ky0 = y
            for k in kids:
                y -= LH
                out.append(rf"  \draw[ln] ({x0 + 6}mm,{y:.1f}mm) -- ({x0 + 8}mm,{y:.1f}mm);")
                out.append(rf"  \node[t] at ({x0 + 8}mm,{y:.1f}mm) {{{k}}};")
            out.append(rf"  \draw[ln] ({x0 + 6}mm,{ky0 - 2.0:.1f}mm) -- ({x0 + 6}mm,{y:.1f}mm);")
            y -= LH + GAP
        out.append(rf"  \draw[ln] ({x0}mm,2mm) -- ({x0}mm,{titles[-1]:.1f}mm);")
    out.append(r"\end{tikzpicture}")
    return "\n".join(out)


# Carta Gantt: meses 1 a 56, inicio en febrero de 2027 (supuesto SA-01).
# Temporada de fruta de diciembre a abril: meses 1-3, 11-15, 23-27, 35-39, 47-51.
FRUTA = [(1, 3), (11, 15), (23, 27), (35, 39), (47, 51)]
FILAS = [
    ("1 Gestión", [(1, 21, "b")]),
    ("2 Levantamiento", [(1, 6, "b"), (13, 14, "b")]),
    ("3 Plataforma", [(4, 12, "b")]),
    ("4 Equipo a bordo", [(6, 10, "b"), (13, 18, "b")]),
    ("5 Servicios Etapa 1", [(6, 10, "b")]),
    ("6 Integraciones", [(6, 10, "b"), (16, 21, "b")]),
    ("7 Datos y migración", [(6, 12, "b"), (19, 24, "b")]),
    ("8 Servicios Etapa 2", [(13, 18, "b")]),
    ("9 Adhesión", [(1, 21, "b")]),
    ("10 Calidad y pruebas", [(10, 12, "b"), (17, 18, "b")]),
    ("11 Implantación", [(10, 12, "b"), (13, 15, "m"), (16, 16, "p"), (17, 18, "b"), (19, 20, "m"), (21, 21, "p")]),
    ("12 Innovaciones", [(4, 15, "b")]),
    ("13 Operación", [(21, 56, "o")]),
]
HITOS = [2, 4, 6, 10, 12, 13, 14, 16, 17, 18, 19, 21]
ANIOS = [(1, 11, "2027"), (12, 23, "2028"), (24, 35, "2029"), (36, 47, "2030"), (48, 56, "2031")]


def gantt():
    W = 1.9  # mm por mes
    X0 = 40.0  # inicio del área de barras
    RH = 5.6   # alto de fila
    n = len(FILAS)
    out = [r"\begin{tikzpicture}[",
           r"  t/.style={font=\sffamily\fontsize{9.5bp}{11bp}\selectfont\color{audit-tinta}},",
           r"  lab/.style={t,anchor=west,inner sep=0pt}]"]
    ytop = 0.0
    ybot = -(n + 1) * RH
    for a, b in FRUTA:
        out.append(rf"  \fill[audit-gris-claro] ({X0 + (a - 1) * W:.2f}mm,{ytop + 9:.1f}mm) rectangle ({X0 + b * W:.2f}mm,{ybot:.1f}mm);")
    # años
    for a, b, lab in ANIOS:
        out.append(rf"  \node[t] at ({X0 + ((a - 1) + b) / 2 * W:.2f}mm,{ytop + 6.5:.1f}mm) {{{lab}}};")
        out.append(rf"  \draw[audit-filete] ({X0 + (a - 1) * W:.2f}mm,{ytop + 9:.1f}mm) -- ({X0 + (a - 1) * W:.2f}mm,{ytop + 4.5:.1f}mm);")
    # meses de referencia
    for m in [1, 13, 16, 21, 33, 45, 56]:
        out.append(rf"  \node[t] at ({X0 + (m - 0.5) * W:.2f}mm,{ytop + 2.2:.1f}mm) {{{m}}};")
    out.append(rf"  \node[lab] at (0mm,{ytop + 6.5:.1f}mm) {{Año}};")
    out.append(rf"  \node[lab] at (0mm,{ytop + 2.2:.1f}mm) {{Mes del contrato}};")
    estilos = {"b": "fill=audit-marino!55,draw=audit-marino",
               "m": "fill=audit-turquesa!45,draw=audit-marino",
               "p": "fill=audit-marino,draw=audit-marino",
               "o": "fill=audit-gris-claro!60!audit-marino!25,draw=audit-marino"}
    for i, (lab, barras) in enumerate(FILAS):
        y = ytop - (i + 0.5) * RH
        out.append(rf"  \node[lab] at (0mm,{y:.2f}mm) {{{lab}}};")
        for a, b, e in barras:
            out.append(rf"  \draw[{estilos[e]},line width=0.4pt] ({X0 + (a - 1) * W:.2f}mm,{y - 1.6:.2f}mm) rectangle ({X0 + b * W:.2f}mm,{y + 1.6:.2f}mm);")
    yh = ytop - (n + 0.5) * RH
    out.append(rf"  \node[lab] at (0mm,{yh:.2f}mm) {{Hitos del E-25}};")
    for m in HITOS:
        x = X0 + (m - 0.5) * W
        out.append(rf"  \fill[audit-marino] ({x:.2f}mm,{yh + 1.6:.2f}mm) -- ({x - 1.1:.2f}mm,{yh - 1.2:.2f}mm) -- ({x + 1.1:.2f}mm,{yh - 1.2:.2f}mm) -- cycle;")
    # leyenda
    yl = ybot - 5
    out.append(rf"  \draw[{estilos['m']}] (0mm,{yl - 1.4:.1f}mm) rectangle (4mm,{yl + 1.4:.1f}mm); \node[lab] at (5mm,{yl:.1f}mm) {{Marcha blanca}};")
    out.append(rf"  \draw[{estilos['p']}] (36mm,{yl - 1.4:.1f}mm) rectangle (40mm,{yl + 1.4:.1f}mm); \node[lab] at (41mm,{yl:.1f}mm) {{Paso a producción}};")
    out.append(rf"  \fill[audit-gris-claro] (78mm,{yl - 1.4:.1f}mm) rectangle (82mm,{yl + 1.4:.1f}mm); \node[lab] at (83mm,{yl:.1f}mm) {{Diciembre a abril}};")
    out.append(r"\end{tikzpicture}")
    return "\n".join(out)


if __name__ == "__main__":
    print("% ---- EDT ----")
    print(edt())
    print("% ---- Gantt ----")
    print(gantt())
