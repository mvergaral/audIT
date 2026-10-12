"""Registro de riesgos del Subdocumento 8 (D4-100 a D4-104).

Fuente única de los datos: escribe el Formulario T-16 del formato local y las tres figuras del
capítulo (RBS, mapa de calor y árbol de fallas) con el lienzo de D4/graficos-v2.
Uso: Formato-Oferta-audIT/herramientas/.venv/bin/python D4/riesgos/registro.py
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "graficos-v2", "fuente"))
import lienzo  # noqa: E402
import rutas  # noqa: E402

FORMATO = rutas.FORMATO
# Color de cada categoría: la paleta por dominio de Formato-Oferta-audIT/temas/marca.tex
CATEGORIAS = [
    ("T", "Técnicos", "#1B4FA8"),
    ("C", "Organizacionales y de contrapartes", "#96600B"),
    ("G", "Gestión del proyecto", "#0A6B45"),
    ("S", "Ciberseguridad y datos", "#A32222"),
    ("O", "Continuidad operativa", "#5B3BB5"),
]
NOMBRE_CAT = {c: n for c, n, _ in CATEGORIAS}

# id, categoría, nombre corto, riesgo, P, I, P residual, I residual, mitigación, responsable,
# respuesta, disparador, plazo
R = [
    ("R-01", "T", "Reconexión masiva",
     "La reconexión de cientos de camiones tras una sombra satura la ingesta o la base de series, y la transferencia, la persistencia y la conciliación completas pasan de 20 minutos",
     2, 3, 1, 3,
     "Espera aleatoria y reintento exponencial en el equipo, Event Hubs desacopla la llegada, IoT Hub S1 con dos unidades y alerta por profundidad de cola",
     "Líder de Operación", "Mitigar", "Retraso de proceso de Event Hubs sobre 10 minutos", "Prueba CP-PERF-02 en A12"),
    ("R-02", "T", "Falla del equipo a bordo",
     "El equipo a bordo de un camión falla entre dos pasos por terminal",
     3, 3, 3, 2,
     "Búfer de 288 horas, 19 equipos de reposición en los terminales y alerta por camión que llega sin reportar",
     "Líder de Implantación", "Mitigar", "Camión que llega al terminal sin reporte reciente", "Cambio en el mismo paso por terminal"),
    ("R-03", "T", "Homologación del equipo",
     "El iWave G26I o el Iridium Edge no obtienen la homologación de SUBTEL o la marca E-Mark",
     2, 4, 1, 4,
     "Verificación de ambas certificaciones en la factibilidad, antes de la compra, como condición declarada en el Formulario T-11",
     "Líder de Implantación", "Evitar", "Ficha o fabricante sin la certificación al cierre de A04", "Mes 4"),
    ("R-04", "T", "Cobertura móvil real",
     "La cobertura móvil medida en las rutas es peor que la supuesta para el dimensionamiento",
     3, 3, 3, 2,
     "Medición en terreno de la cobertura (A03), búfer de 288 horas y mensajería Iridium para los eventos críticos",
     "Líder de Implantación", "Mitigar", "Tramo medido sin cobertura que el diseño no consideraba", "Meses 1 a 3"),
    ("R-05", "T", "Crecimiento de volumetría",
     "El crecimiento a 430 camiones y a tres veces la volumetría inicial supera la capacidad dimensionada",
     2, 3, 1, 3,
     "Dimensionamiento sobre RT-09.03, escalado automático de AKS, unidades adicionales de IoT Hub y prueba de carga a 1,5 veces el peak",
     "Arquitecto de Solución", "Mitigar", "Uso diario de IoT Hub sobre el 75 % de su cuota", "Revisión mensual"),
    ("R-06", "T", "Retiro de Redis en 2028",
     "Azure Cache for Redis se retira el 30 de septiembre de 2028, en el mes 20, durante la marcha blanca de la Etapa 2, y su edición Enterprise el 31 de marzo de 2027",
     5, 3, 1, 3,
     "La arquitectura usa Azure Managed Redis, el servicio de reemplazo, desde la Etapa 1 (Subdocumento 4, sección 4.1.1)",
     "Arquitecto de Solución", "Evitar", "Un componente de la Etapa 1 que dependa de Azure Cache for Redis en el hito H2", "Mes 4"),
    ("R-07", "T", "Bloqueo por proveedor",
     "La solución queda atada al proveedor de nube y el mandante no puede cambiarlo",
     2, 3, 2, 2,
     "Contenedores y motor relacional portables, Event Hubs con protocolo Kafka, infraestructura como código y suscripciones a nombre del mandante",
     "Arquitecto de Solución", "Mitigar", "Decisión de arquitectura sin alternativa portable", "Cada Comité de Arquitectura"),
    ("R-08", "C", "Plataformas sin interfaz",
     "Las plataformas de los terceros no entregan datos por interfaz, porque dos son de solo consulta y una no exporta",
     3, 3, 3, 2,
     "Factibilidad con los tres proveedores (A04) y estándar de homologación. Si falla, esos camiones pasan a operar como sin equipo",
     "Líder de Integración", "Mitigar", "Proveedor sin interfaz de salida en la factibilidad", "Meses 1 a 4"),
    ("R-09", "C", "Telemetría de fábrica",
     "Los fabricantes no autorizan la lectura de la telemetría de fábrica de los 61 tractocamiones, que RT-17.06 sujeta a su autorización",
     3, 3, 2, 3,
     "Consulta a cada fabricante en la factibilidad (A04) con el acoplamiento sin contacto y de solo lectura, que no toca el arnés ni la garantía. Sin autorización, el viaje se registra igual con el equipo a bordo",
     "Líder de Integración", "Mitigar", "Fabricante sin autorización escrita al cierre de A04", "Mes 4"),
    ("R-10", "C", "Apagado de 2G y 3G",
     "El apagado de las redes 2G y 3G deja sin posición a equipos de terceros que hoy reportan",
     3, 3, 3, 2,
     "LTE exigida en el estándar de homologación y seguimiento mensual de la adhesión por proveedor",
     "Líder Funcional", "Mitigar", "Caída de posiciones de un proveedor en el seguimiento mensual", "Mensual"),
    ("R-11", "C", "Adhesión bajo la meta",
     "La adhesión de los transportistas queda bajo la meta de 104 al mes 16 y 134 al mes 21",
     3, 4, 2, 4,
     "Campaña desde el mes 1 (A06), anexo de adhesión con propiedad del dispositivo y expediente verificable como incentivo",
     "Líder Funcional", "Mitigar", "59 o menos RUT de los 148 iniciales con anexo firmado, vigente, no revocado y registrado al cierre del mes 9 (31-10-2027)", "Mes 9"),
    ("R-12", "C", "Contable sin interfaz",
     "El sistema contable y de facturación no recibe datos por interfaz",
     2, 3, 2, 2,
     "Prueba técnica en el mes 3. Si falla, intercambio de archivos con conciliación",
     "Líder de Integración", "Mitigar", "Prueba técnica fallida", "Mes 3"),
    ("R-13", "C", "Registro electrónico de jornada",
     "La autoridad no admite el registro electrónico de jornada",
     2, 3, 2, 2,
     "Consulta C-10 en el mes 2. Si la respuesta es negativa, se mantiene el respaldo en papel firmado",
     "Líder Funcional", "Aceptar", "Respuesta negativa a la consulta C-10", "Mes 2"),
    ("R-14", "C", "Rechazo de conductores",
     "Los conductores rechazan la medición o la perciben como vigilancia, en especial los 258 externos",
     3, 3, 2, 3,
     "Plan de gestión del cambio, consentimiento revocable por dato y período, y capacitación en los terminales (A13)",
     "Líder de Implantación", "Mitigar", "Aumento de revocaciones en el indicador mensual de adhesión", "Mensual desde el mes 6"),
    ("R-15", "C", "Contraparte del mandante",
     "Los usuarios clave de la torre y de los terminales no tienen tiempo para el levantamiento, las pruebas y la capacitación, sobre todo en la temporada, o un entregable vuelve con observaciones y la segunda revisión del Artículo 18.3 consume el margen del hito",
     3, 3, 2, 3,
     "Calendario de participación de los usuarios clave acordado en el arranque, revisión previa de cada entregable con la Contraparte Técnica en el Comité de Proyecto y entregables con la evidencia y la trazabilidad del Artículo 18.2",
     "Jefe de Proyecto", "Mitigar", "Sesión con usuarios clave suspendida dos veces o entregable con observaciones", "Cada entregable"),
    ("R-16", "G", "Inicio de la marcha blanca 1",
     "La ruta crítica o la capacitación atrasan el inicio de la marcha blanca de la Etapa 1, fijado en el día 240",
     2, 4, 1, 4,
     "Reserva A14 de 14 días y A13 diez días antes del fin de A09, condicionada a la entrega G13, con registro del atraso si faltan la versión de preproducción, los datos o el material",
     "Jefe de Proyecto", "Mitigar", "Entrega G13 incompleta el día 182 o consumo de más de la mitad de la reserva A14", "Quincenal hasta el día 240"),
    ("R-17", "G", "Hitos H1 a H4",
     "Los primeros hitos de pago se atrasan, porque su margen es de 2 a 8 días hábiles",
     2, 3, 2, 3,
     "Levantamiento en los cinco terminales en paralelo y seguimiento semanal del margen de cada hito",
     "Jefe de Proyecto", "Aceptar", "Margen de un hito bajo 2 días hábiles", "Semanal hasta H4"),
    ("R-18", "G", "Cierre de la marcha blanca 1",
     "La marcha blanca de la Etapa 1, que cae en la temporada de fruta, no cumple las condiciones del Artículo 17.3 en tres meses",
     3, 4, 2, 4,
     "Analistas en los cinco terminales en el horario de relevo, medición diaria y reversión activa",
     "Líder de Operación", "Mitigar", "Condición de cierre bajo su umbral al cierre del mes 14", "Mes 14"),
    ("R-19", "G", "Despliegue a bordo lento",
     "El montaje a bordo avanza más lento que la cobertura declarada mes a mes, por un cierre del paso Los Libertadores, por la temporada de diciembre a abril o porque un camión pasa poco por los terminales",
     3, 2, 3, 1,
     "Montaje en los meses 6 a 10 y 16 a 18, con holguras de 20 días (A11) y 40 días (A18)",
     "Líder de Implantación", "Mitigar", "Cobertura acumulada bajo la declarada para el mes", "Meses 6 a 10 y 16 a 18"),
    ("R-20", "G", "Período mixto prolongado",
     "La parte de la flota sin equipo audIT queda así más tiempo del previsto y se forman dos maneras de trabajar que después no se unifican",
     3, 3, 2, 3,
     "Una sola fuente de verdad y un solo flujo de asignación para toda la flota, con el nivel de evidencia de cada camión visible en la torre, y seguimiento mensual de los camiones sin equipar",
     "Líder de Implantación", "Mitigar", "Menos de 24 de los 34 camiones de terceros sin equipo montados en el mes 16", "Mes 16"),
    ("R-21", "G", "Inicio en enero",
     "El contrato empieza en enero de 2027 y el mes 16 cae en abril, dentro de la temporada",
     2, 5, 1, 5,
     "Fijar en el contrato febrero de 2027 como mes 1 y escalar al Comité Ejecutivo cualquier cambio de fecha",
     "Jefe de Proyecto", "Evitar", "Fecha de inicio del contrato distinta de febrero de 2027", "Firma del contrato"),
    ("R-22", "S", "Suplantación de equipos",
     "Alguien suplanta un equipo a bordo o una baliza para falsear posición, jornada o acople",
     2, 4, 1, 4,
     "Elemento seguro TA100 y certificado por equipo, certificado mutuo en IoT Hub y acople confirmado en la portería",
     "Encargado de Seguridad", "Mitigar", "Un certificado usado desde dos equipos", "Revocación inmediata"),
    ("R-23", "S", "Ataque al portal",
     "Un ataque al portal expuesto a internet compromete datos de localización de los conductores externos",
     3, 4, 2, 4,
     "Cortafuegos de aplicación en Front Door, Entra ID con control por rol y atributo, cifrado de campo y pruebas de seguridad ofensiva en A12",
     "Encargado de Seguridad", "Mitigar", "Vulnerabilidad crítica abierta o acceso anómalo", "7 días corridos"),
    ("R-24", "S", "Licitud en Brazil South",
     "La réplica de datos personales en Brazil South no cuenta con base de licitud ni con la aprobación del mandante",
     3, 4, 2, 4,
     "Base de licitud del Subdocumento 5 y aprobación del mandante que exige el Artículo 23. Sin ellas, los datos personales se replican en San Bernardo, que levanta los servicios críticos que los usan",
     "Arquitecto de Solución", "Mitigar", "Hito H2 sin aprobación del mandante", "Mes 4"),
    ("R-25", "O", "Caída de la región",
     "La región Azure Chile Central deja de responder por un desastre",
     1, 5, 1, 3,
     "Brazil South en espera, conmutación en cuatro pasos con confirmación de la guardia y dos pruebas reales al año",
     "Líder de Operación", "Transferir", "Región primaria sin respuesta por 15 minutos", "4 horas (RTO)"),
    ("R-26", "O", "Retraso de la réplica",
     "El retraso de la réplica asíncrona supera los 15 minutos de pérdida admitida con escritura intensa",
     2, 4, 1, 3,
     "Servidor de series separado, Event Hubs con retraso máximo de 10 minutos y reenvío de 72 horas desde el equipo a bordo",
     "Líder de Datos", "Mitigar", "Retraso de la réplica cerca de 15 minutos", "Continuo"),
    ("R-27", "O", "Bloqueo indebido",
     "La verificación bloqueante detiene un viaje comprometido que debía salir, por un dato vencido, un registro sin sincronizar o una regla mal calibrada",
     3, 4, 2, 3,
     "Verificación en paralelo sin bloquear en los meses 13 y 14, que mide cuántos viajes habría detenido y por qué, evaluación sobre el estado autoritativo con versión y vencimiento, y excepción RN-04 solo ante una fuente de evidencia no disponible, aprobada y registrada",
     "Líder Funcional", "Mitigar", "Viaje que la prueba en paralelo habría detenido sin causa válida", "Meses 13 a 15"),
    ("R-28", "T", "Documento satelital sobre 90 s",
     "En un punto de carga sin cobertura, el documento completo que emite el sistema contable no vuelve a la cabina por satélite dentro de los 90 segundos de RT-09.01",
     3, 4, 2, 4,
     "Emisión anticipada desde la orden en todo viaje cuya carga se conoce al programar, ensayo del retorno en fragmentos con el documento de mayor tamaño y salida bloqueada sin documento conforme",
     "Líder de Integración", "Mitigar", "Ensayo con un retorno sobre 90 segundos o con fragmentos perdidos", "Mes 3, con la prueba técnica del sistema contable"),
]

# Modos de falla técnicos (AMFE): modo, efecto, S, O, D, control de detección, riesgo
AMFE = [
    ("Equipo a bordo deja de registrar", "Pérdida de registros del camión", 4, 3, 3, "Revisión al pasar por terminal", "R-02"),
    ("Módem Iridium sin servicio en una sombra", "Sin evento de emergencia ni documento sin cobertura", 4, 2, 4, "Lo nota el conductor al usarlo", "R-04"),
    ("Grupo electrógeno no arranca en un corte", "San Bernardo con 66 minutos de UPS", 3, 2, 3, "Prueba periódica en sitio", "R-25"),
    ("Baliza sin batería o acople falso", "Semirremolque sin verificar", 2, 3, 2, "Monitoreo de batería en la nube", "R-22"),
    ("Lector CAN sin señal", "Sin telemetría del motor", 2, 2, 2, "Monitoreo en la nube", "R-09"),
    ("Lector de tarjeta no lee", "Conductor sin identificar", 3, 2, 1, "Aviso inmediato en cabina", "R-02"),
    ("Búfer lleno por una sombra de más de 288 horas", "Pérdida de los registros más antiguos", 4, 1, 2, "Monitoreo en la nube", "R-04"),
    ("Réplica atrasada más de 15 minutos", "Pérdida de datos sobre el RPO", 4, 2, 1, "Alerta automática", "R-26"),
    ("Ingesta saturada en una reconexión", "Sincronización sobre 20 minutos", 3, 2, 1, "Alerta por profundidad de cola", "R-01"),
    ("Enlace de terminal caído más de 24 horas", "Terminal en procedimiento supletorio", 3, 2, 1, "Alerta automática", "R-04"),
]


def tex(s):
    return s.replace("%", r"\%")


def zona(e):
    return "Alta" if e >= 12 else ("Media" if e >= 6 else "Baja")


def escribir_t16():
    filas = []
    for (i, c, _n, r, p, im, *_rest) in R:
        mit, resp = _rest[2], _rest[3]
        filas.append(f"  \\riesgoTDieciseis{{id={i}, riesgo={{{tex(r)}}}, categoria={{{NOMBRE_CAT[c]}}}, "
                     f"probabilidad={p}, impacto={im}, exposicion={p * im}, mitigacion={{{tex(mit)}}}, "
                     f"responsable={{{resp}}}}}")
    resp_filas = []
    for (i, _c, _n, _r, p, im, pr, ir, _m, _resp, estr, disp, plazo) in R:
        resp_filas.append(f"{i} & {estr} & {tex(disp)} & {tex(plazo)} & {p * im} a {pr * ir} \\\\")
    amfe_filas = []
    for (modo, efecto, s, o, d, det, rid) in sorted(AMFE, key=lambda a: -a[2] * a[3] * a[4]):
        amfe_filas.append(f"{tex(modo)} & {tex(efecto)} & {s} & {o} & {d} & {s * o * d} & {tex(det)} & {rid} \\\\")
    t = r"""% ============================================================================
%  Formulario T-16. Plan de riesgos (FEP01 p. 63). Lo escribe D4/riesgos/registro.py
%  a partir del registro de riesgos: no se edita a mano.
% ============================================================================
\begin{formulario}{T-16}

\providecommand\tituloBloqueFormulario[1]{%
  \par\Needspace{10\baselineskip}\vspace{14pt plus 3pt}\phantomsection\addcontentsline{toc}{section}{#1}\noindent{\sffamily\bfseries\fontsize{13bp}{16bp}\selectfont\color{audit-marino}#1}\par\vspace{6pt}\noindent}

\begin{contenidoExigido}{T-16}
  \exigencia{Identificación y cuantificación de riesgos técnicos, organizacionales, de proyecto, de seguridad y de operación.}{\verSeccionFolio{sec:8-identificacion} y este formulario, registro de riesgos}
  \exigencia{Análisis cualitativo y cuantitativo con modos de falla, árbol de fallas o simulación.}{\verSeccionFolio{sec:8-identificacion} y este formulario, análisis de modos de falla}
  \exigencia{Estrategias de mitigación con costo-beneficio, responsable, plazo y disparador.}{\verSeccionFolio{sec:8-accion} y este formulario, respuesta, disparador y plazo}
  \exigencia{Obsolescencia, bloqueo por proveedor, escalabilidad, ciberseguridad y disponibilidad de contrapartes del mandante.}{\verSeccionFolio{sec:8-identificacion}}
  \exigencia{Reservas de contingencia y de gestión, con su reflejo en el cronograma y en el flujo de caja.}{\verSeccionFolio{sec:8-accion}}
\end{contenidoExigido}

\tituloBloqueFormulario{Registro de riesgos}

El registro tiene """ + str(len(R)) + r""" riesgos de la solución propuesta. La probabilidad y el impacto van de 1 a 5 con las
escalas de la \verSeccion{sec:8-plan}, y la exposición es su producto. Una exposición de 12 o más es alta
y exige plan de contingencia, que está en la \verSeccion{sec:8-accion}.

\begin{formularioTDieciseis}
""" + "\n".join(filas) + r"""
\end{formularioTDieciseis}

\tituloBloqueFormulario{Respuesta, disparador, plazo y exposición residual}

La \tabref{t16-respuesta} completa cada riesgo con lo que pide \transv{RT-19.04}{33}: la estrategia de
respuesta, el disparador que la activa y el plazo, más la exposición antes y después de mitigar.

\begin{tabla}[ancho=completo, fuente=condensada]{Respuesta, disparador y plazo de cada riesgo}{t16-respuesta}{L{12mm} L{18mm} X L{36mm} L{22mm}}
ID & Respuesta & Disparador & Plazo & Exposición \\ \midrule
""" + "\n".join(resp_filas) + r"""
\end{tabla}
\notaTabla{Fuente: elaboración propia. La exposición va de la inicial a la residual.}

Después de mitigar, ningún riesgo queda con exposición alta. Los cinco que quedan en 8 (R-11, R-18, R-23, R-24 y R-28)
conservan su impacto de 4, porque la mitigación baja su probabilidad y deja igual su consecuencia.

\tituloBloqueFormulario{Análisis de modos de falla de los componentes técnicos}

La \tabref{t16-amfe} aplica el análisis de modos de falla a los componentes físicos de la solución. La
severidad (S) usa la escala de impacto y la ocurrencia (O) la de probabilidad. La detección (D) va de 1,
detección automática en menos de 30 segundos, a 5, falla que no se nota hasta que ocurre en ruta. El
número de prioridad es S × O × D, y un valor de 50 o más exige plan de contingencia.

\begin{tabla}[ancho=completo, fuente=condensada]{Análisis de modos de falla y efectos}{t16-amfe}{L{40mm} X R{6mm} R{6mm} R{6mm} R{10mm} L{34mm} L{11mm}}
Modo de falla & Efecto & S & O & D & NPR & Detección & Riesgo \\ \midrule
""" + "\n".join(amfe_filas) + r"""
\end{tabla}
\notaTabla{Fuente: elaboración propia. Escala de detección del plan de riesgos (sección 8.1).}

Ningún modo de falla llega a 50. Los dos más altos, el equipo a bordo que deja de registrar y el módem
satelital sin servicio, tienen detección tardía. Su mitigación apunta a detectar antes la falla.

\end{formulario}
"""
    ruta = os.path.join(FORMATO, "subdocumentos/08-riesgos/formularios/T-16.tex")
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    open(ruta, "w", encoding="utf-8").write(t)
    return ruta


# ----------------------------------------------------------------------------- figuras
SALIDA = os.path.join(FORMATO, "figuras")


def _tinte(color, k=0.10):
    """Mezcla el color con blanco: k es la parte de color."""
    r, g, b = (int(color[n:n + 2], 16) for n in (1, 3, 5))
    return "#{:02X}{:02X}{:02X}".format(*(round(255 - (255 - v) * k) for v in (r, g, b)))


def _texto_blanco(f, x, y, s, tam, peso=400):
    w = f.texto(x, y, s, tam, peso)
    f.textos[-1] = f.textos[-1].replace('fill="#000000"', 'fill="#FFFFFF"')
    return w


def fig_rbs():
    """Estructura de desglose con un color por categoría (D4-107): borde y franja de encabezado en el
    color, fichas con un tinte claro del mismo color y texto negro. Sin íconos."""
    f = lienzo.Figura("rbs", "08-riesgos", "V", alto=538)
    f.caja(111, 8, 200, 34, [("Riesgos de la solución", 10, 600), (f"{len(R)} riesgos en cinco categorías", 9, 400)])
    y = 62
    xbus = 18
    x, w, rx, hb = 34, 380, 8, 22
    for c, nombre, color in CATEGORIAS:
        rs = [r for r in R if r[1] == c]
        filas = (len(rs) + 1) // 2
        h = 30 + filas * 18 + 4
        f.rect(x, y, w, h, relleno="#FFFFFF", borde=color, grosor=1.2, rx=rx)
        f.crudo(f'<path d="M{x},{y + hb} L{x},{y + rx} A{rx},{rx} 0 0 1 {x + rx},{y} L{x + w - rx},{y} '
                f'A{rx},{rx} 0 0 1 {x + w},{y + rx} L{x + w},{y + hb} Z" fill="{color}"/>', capa="fondo")
        wt = _texto_blanco(f, x + 10, y + 15, nombre, 10, 600)
        _texto_blanco(f, x + 10 + wt + 6, y + 15, f"{len(rs)} riesgos", 9)
        f.linea([(xbus, y + 11), (x, y + 11)], flecha="fin")
        for k, r in enumerate(rs):
            col, fil = k % 2, k // 2
            alta = r[4] * r[5] >= 12
            x0, yc = 42 + col * 186, y + 33 + fil * 18
            f.rect(x0, yc - 7, 180, 14, relleno=_tinte(color), borde=color, grosor=0.6, rx=3, capa="frente")
            f.texto(x0 + 90, yc + 3, f"{r[0]}  {r[2]}", 9, 600 if alta else 400, "middle", capa=f.frente,
                    revisar=False)
            f.cajas_icono.append((x0, yc - 7, x0 + 180, yc + 7, "ficha " + r[0]))
        y += h + 6
    f.linea([(211, 42), (211, 52), (xbus, 52), (xbus, y - h - 6 + 11)], flecha=None)
    return f.guardar(SALIDA)


def fig_mapa():
    f = lienzo.Figura("mapa-calor", "08-riesgos", "V", alto=546)
    gris = {"Baja": "#FFFFFF", "Media": "#EDEDED", "Alta": "#CFCFCF"}
    cw, ch = 62, 39
    for k, (titulo, ip, ii) in enumerate([("Antes de mitigar", 4, 5), ("Después de mitigar", 6, 7)]):
        y0 = 4 + k * 272
        f.grupo(8, y0, 406, 266, titulo)
        gx, gy = 70, y0 + 40
        f.texto(24, gy - 9, "Probabilidad", 9, 600, "start")
        for p in range(5, 0, -1):
            yy = gy + (5 - p) * ch
            f.texto(gx - 10, yy + ch / 2 + 3, str(p), 9, 400, "end")
            for i in range(1, 6):
                xx = gx + (i - 1) * cw
                f.rect(xx, yy, cw, ch, relleno=gris[zona(p * i)], borde="#8C8C8C", grosor=0.5)
                ids = [r[0] for r in R if r[ip] == p and r[ii] == i]
                for j, rid in enumerate(ids):
                    rid = rid[2:]
                    cx = xx + 13 + (j % 3) * 18
                    cy = yy + 12 + (j // 3) * 11
                    f.texto(cx, cy, rid, 9, 600 if p * i >= 12 else 400, "middle")
        for i in range(1, 6):
            f.texto(gx + (i - 1) * cw + cw / 2, gy + 5 * ch + 12, str(i), 9, 400, "middle")
        f.texto(gx + 2.5 * cw, gy + 5 * ch + 25, "Impacto", 9, 600, "middle")
    return f.guardar(SALIDA)


def _puerta(f, cx, cy, tipo):
    """Compuerta lógica del árbol: «O» con forma de escudo y «Y» con forma de D."""
    if tipo == "O":
        d = (f"M{cx - 13},{cy + 9} Q{cx},{cy + 2} {cx + 13},{cy + 9} Q{cx + 12},{cy - 4} {cx},{cy - 11} "
             f"Q{cx - 12},{cy - 4} {cx - 13},{cy + 9} Z")
    else:
        d = f"M{cx - 12},{cy + 9} L{cx - 12},{cy - 3} A12,12 0 0 1 {cx + 12},{cy - 3} L{cx + 12},{cy + 9} Z"
    f.crudo(f'<path d="{d}" fill="#FFFFFF" stroke="#2B2B2B" stroke-width="1"/>')
    f.cajas_icono.append((cx - 13, cy - 11, cx + 13, cy + 9, "compuerta"))


def fig_arbol():
    f = lienzo.Figura("arbol-fallas", "08-riesgos", "H")
    W = f.W
    f.caja(W / 2 - 130, 63, 260, 36, [("Viaje asignado a un conductor no apto", 10, 600)])
    f.linea([(W / 2, 99), (W / 2, 124)], flecha=None)
    _puerta(f, W / 2, 135, "O")
    ramas = [
        (["Registro de jornada incompleto", "tomado como válido"],
         ["Registro", "incompleto", "en el equipo"], ["R-02", "R-22"], ["No se muestra", "la antigüedad", "del dato"]),
        (["Excepción RN-04", "mal aplicada"],
         ["La torre aplica", "la excepción", "RN-04"], [], ["Sin fuente caída,", "aprobación", "o registro"]),
        (["Asignación sin la", "reserva central"],
         ["Terminal o San", "Bernardo", "sin enlace"], [], ["Asignación local", "sin la torre", "ni la reserva"]),
        (["Conductor externo aprobado", "sin evidencia"],
         ["Transportista no", "adherido o en", "modalidad de datos"], ["R-08", "R-10", "R-11"],
         ["Atestación", "documental", "aceptada por error"]),
    ]
    xs = [W * (k + 0.5) / 4 for k in range(4)]
    f.linea([(W / 2, 144), (W / 2, 157)], flecha=None)
    f.linea([(xs[0], 157), (xs[3], 157)], flecha=None)
    for x in xs:
        f.linea([(x, 157), (x, 173)], flecha=None)
    for x, (titulo, h1, r1, h2) in zip(xs, ramas):
        f.caja(x - 85, 173, 170, 40, titulo, tam=10)
        f.linea([(x, 213), (x, 237)], flecha=None)
        _puerta(f, x, 248, "Y")
        f.linea([(x, 257), (x, 273)], flecha=None)
        f.linea([(x - 45, 273), (x + 45, 273)], flecha=None)
        for dx, lineas, rids in ((-45, h1, r1), (45, h2, [])):
            bx = x + dx
            f.linea([(bx, 273), (bx, 289)], flecha=None)
            f.caja(bx - 43, 289, 86, 56, lineas, tam=9, rx=4, alto_linea=12)
            for k2, rid in enumerate(rids):
                f.ficha(bx, 363 + k2 * 19, rid, w=42)
    return f.guardar(SALIDA)


if __name__ == "__main__":
    print("T-16:", escribir_t16())
    for g in (fig_rbs, fig_mapa, fig_arbol):
        print("figura:", g())
    altos = [r for r in R if r[4] * r[5] >= 12]
    print("Riesgos:", len(R), "| exposición alta:", ", ".join(f"{r[0]} ({r[4] * r[5]})" for r in altos))
    print("Residual máxima:", max(r[6] * r[7] for r in R))
    print("NPR máximo:", max(a[2] * a[3] * a[4] for a in AMFE))
    print("Revisión de líneas:", {k: v for k, v in lienzo.REVISION.items() if v})
