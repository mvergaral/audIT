"""Copia de D4 de las figuras de la sección 4.1 que la dupla 3 publicó el 2026-10-11
(audIT/Informe-2/D3/generadores_graficos/s4_secuencias.py y s4_documento.py, commit f86e240).

Se conserva su contenido y su trazado. Solo cambia lo que pide el formato local:
  - sin título dentro de la figura, porque la leyenda de LaTeX lo da, y se recorta el margen
    superior que dejaba libre;
  - sin punto y coma en las notas;
  - «solo» sin tilde.
Los archivos de la dupla 3 no se tocan. El respaldo de la copia anterior (commit eef2475)
quedó en ../respaldo-secuencias-2026-10-11/.
"""
from lienzo import Figura, MM, SUBRED

C4 = "04-arquitectura"


class FiguraSinTitulo(Figura):
    """Lienzo apaisado al que se le quita el margen superior que ocupaba el título."""

    def __init__(self, nombre, recorte):
        super().__init__(nombre, C4, "H")
        self.recorte = recorte

    def svg(self):
        s = super().svg()
        alto = self.H - self.recorte
        viejo = f'height="{self.mm[1]}mm" viewBox="0 0 {self.W:g} {self.H:g}"'
        nuevo = f'height="{round(alto / MM, 1)}mm" viewBox="0 {self.recorte:g} {self.W:g} {alto:g}"'
        return s.replace(viejo, nuevo, 1)


def actor(f, x, nombre, w=124):
    f.caja(x - w / 2, 37, w, 38, nombre if isinstance(nombre, list) else [nombre], tam=9)
    f.linea([(x, 75), (x, 399)], disc=True, flecha=None, grosor=0.6, saltos=False)


def mensaje(f, xs, origen, destino, y, texto, retorno=False):
    a, b = xs[origen], xs[destino]
    f.linea([(a, y), (b, y)], disc=retorno, saltos=False)
    f.rotulo((a + b) / 2, y - 5, texto, tam=9)


def nota(f, y, lineas):
    f.grupo(14, y, f.W - 28, 22 + 13 * len(lineas), None, rx=6, relleno=SUBRED)
    for i, s in enumerate(lineas):
        f.texto(24, y + 18 + i * 13, s, 9)


XS = [78, 220, 366, 510, 651]


def secuencia_asignacion():
    f = FiguraSinTitulo("secuencia-asignacion", 24)
    for x, n in zip(XS, [["Operador / API"], ["Planificación", "y tráfico"],
                         ["Personas / Flota", "Servicios de validación"], ["PostgreSQL", "Reserva y outbox"],
                         ["Bus de eventos", "Consumidores"]]):
        actor(f, x, n)
    mensaje(f, XS, 0, 1, 106, "Orden, recursos y clave de idempotencia")
    mensaje(f, XS, 1, 2, 142, "Jornada, habilitaciones y aptitud · en paralelo")
    mensaje(f, XS, 2, 1, 178, "Veredicto + versión + evidencia", True)
    f.grupo(14, 199, 701, 97, None, rx=3)
    f.rotulo(23, 214, "Si todas las reglas habilitan", anc="start", tam=10, peso=600)
    mensaje(f, XS, 1, 3, 231, "Reserva única + asignación + outbox · una transacción")
    mensaje(f, XS, 3, 1, 261, "Commit confirmado", True)
    mensaje(f, XS, 1, 0, 285, "Asignación confirmada", True)
    mensaje(f, XS, 3, 4, 324, "Publicación desde outbox · entrega al menos una vez")
    f.grupo(14, 344, 701, 55, None, rx=3, relleno=SUBRED)
    f.rotulo(23, 359, "Si hay bloqueo legal, conflicto o límite agotado", anc="start", tam=10, peso=600)
    mensaje(f, XS, 1, 0, 384, "Rechazo trazable · no asignar", True)
    nota(f, 411, ["Techo contractual: 30 s de extremo a extremo. Presupuesto de diseño: 25 s + 5 s de margen.",
                  "RN-04 solo admite una excepción aprobada ante una fuente indisponible, nunca ante una causa legal."])
    return f.guardar()


def secuencia_documento():
    f = FiguraSinTitulo("secuencia-documento", 24)
    for x, n in zip(XS, [["Cabina", "Datos de carga"], ["Operación de fletes", "Validación"],
                         ["Capa anticorrupción", "Adaptador contable"], ["Sistema contable", "Único emisor"],
                         ["Custodia / SII", "Envío y respaldo"]]):
        actor(f, x, n)
    mensaje(f, XS, 0, 1, 108, "Datos definitivos · anticipados o por enlace satelital")
    mensaje(f, XS, 1, 2, 148, "Solicitud idempotente de emisión")
    mensaje(f, XS, 2, 3, 187, "Contrato de emisión homologado")
    mensaje(f, XS, 3, 4, 227, "Documento firmado · envío fiscal y custodia")
    mensaje(f, XS, 3, 2, 266, "Documento y representación del mismo contenido", True)
    mensaje(f, XS, 2, 0, 307, "Entrega completa · acuse e integridad verificados", True)
    f.grupo(14, 329, 701, 70, None, rx=3, relleno=SUBRED)
    f.rotulo(26, 344, "Comprobación antes de salir", anc="start", tam=10, peso=600)
    f.rotulo(26, 357, "Datos de carga coinciden + documento válido disponible + representación portable conforme.",
             anc="start")
    f.rotulo(26, 381, "Ausencia, discrepancia o plazo vencido: salida bloqueada hasta corregir y evaluar de nuevo.",
             anc="start")
    nota(f, 411, ["RT-09.01 del Caso: emisión ≤ 90 s. Un folio recibido por sí solo no habilita el traslado.",
                  "Cabina y terminal conservan copias, sin custodiar el CAF ni las claves de firma del emisor."])
    return f.guardar()


def secuencia_liquidacion():
    f = FiguraSinTitulo("secuencia-liquidacion", 24)
    for x, n in zip(XS, [["Operación de fletes"], ["Liquidación", "y costeo"],
                         ["Fuentes de costo", "Combustible / peajes"], ["Transportista", "Portal y conformidad"],
                         ["ACL / contable", "Registro y acuse"]]):
        actor(f, x, n)
    mensaje(f, XS, 0, 1, 106, "Viaje cerrado · distancias, tiempos y respaldos")
    mensaje(f, XS, 1, 3, 148, "v1 ≤ 24 h · componentes disponibles y faltantes")
    mensaje(f, XS, 2, 1, 190, "Lotes conciliados · combustible hasta 40 días")
    mensaje(f, XS, 1, 3, 232, "v2…vn · costo actualizado sin sobrescribir v1")
    mensaje(f, XS, 1, 3, 274, "Propuesta de liquidación mensual + detalle por viaje")
    mensaje(f, XS, 3, 1, 310, "Aceptación firmada o discrepancia trazable", True)
    mensaje(f, XS, 1, 4, 351, "Liquidación aprobada · clave de idempotencia")
    mensaje(f, XS, 4, 1, 387, "Acuse contable y conciliación", True)
    nota(f, 411, ["El costo preliminar de un viaje y la liquidación mensual son registros distintos.",
                  "Sin acuse contable queda pendiente, y el reintento no duplica el registro financiero."])
    return f.guardar()


def secuencia_reconexion():
    f = FiguraSinTitulo("secuencia-reconexion", 24)
    for x, n in zip(XS, [["Equipo a bordo", "SQLite / outbox"], ["IoT Hub", "Identidad y cuotas"],
                         ["Event Hubs", "Partición por equipo"], ["Consumidor", "Deduplicación"],
                         ["Persistencia", "Acuse duradero"]]):
        actor(f, x, n)
    mensaje(f, XS, 0, 1, 106, "Reautenticar · último acuse y secuencia local")
    mensaje(f, XS, 1, 0, 146, "Ventana de envío + reintento con variación aleatoria", True)
    mensaje(f, XS, 0, 1, 187, "Lotes numerados · prioridad a jornada y tiempos")
    mensaje(f, XS, 1, 2, 227, "Admisión al flujo · aún no es confirmación final")
    mensaje(f, XS, 2, 3, 267, "Evento y secuencia · entrega al menos una vez")
    mensaje(f, XS, 3, 4, 307, "INSERT único + conflictos auditados")
    mensaje(f, XS, 4, 0, 347, "Acuse después de commit · cursor confirmado", True)
    f.rotulo(78, 384, "Depurar solo lo confirmado")
    nota(f, 411, ["Caso RT-03.13: ≤ 20 min por camión tras 72 h. Perfil de prueba: 300 unidades simultáneas.",
                  "Las 288 h son una ampliación propuesta, con un ensayo propio que no sustituye al de 72 h."])
    return f.guardar()


def documento_sin_cobertura():
    f = FiguraSinTitulo("documento-sin-cobertura", 26)
    f.grupo(14, 44, 701, 130, "Datos conocidos antes de entrar en la zona sin señal", rx=6)
    for x, ic, n, d in [(86, "flu-documento", "Orden completa", None),
                        (292, "flu-contable", "Sistema contable", "Emite y firma"),
                        (522, "pr-g26i", "Cabina", "Documento y representación")]:
        f.nodo(ic, x, 99, 28, n, d)
    f.linea([(100, 99), (278, 99)])
    f.linea([(306, 99), (508, 99)])
    f.rotulo(407, 92, "Descarga y acuse verificados")
    f.grupo(14, 186, 701, 199, "Datos definitivos conocidos en el punto sin señal", rx=6)
    for x, ic, n, d in [(86, "pr-g26i", ["Carga definitiva"], ["Solicitud identificada"]),
                        (292, "flu-satelite", ["Iridium SBD"], ["Tramas y correlación"]),
                        (522, "flu-contable", ["ACL → contable"], ["Único emisor, firma original"])]:
        f.nodo(ic, x, 242, 28, n, d)
    f.linea([(100, 242), (278, 242)])
    f.linea([(306, 242), (508, 242)])
    f.linea([(522, 300), (522, 345), (86, 345), (86, 303)])
    f.rotulo(304, 343, "Entrega íntegra por fragmentos + verificación + acuse")
    nota(f, 400, ["El folio o el hash solos no sustituyen el documento ni su representación portable conforme.",
                  "SBD 9603: hasta 340 bytes de subida y 270 de bajada por mensaje. Se miden tamaño y tiempo total.",
                  "Emisión ≤ 90 s y documento disponible antes de salir. Si falta confirmación conforme: bloquear salida."])
    return f.guardar()


FIGURAS = [secuencia_asignacion, secuencia_documento, secuencia_liquidacion, secuencia_reconexion,
           documento_sin_cobertura]
