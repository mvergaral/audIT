"""Subdocumento 4, sección 4.1: diagramas de secuencia y flujos de negocio D3.

Implementa los tres diagramas de secuencia que detallan las reglas operacionales
y transaccionales del núcleo de despacho, emisión offline y liquidación:
  - 4-3-asignacion: Verificación de asignación y reserva atómica (<= 30 s).
  - 4-4-documento: Emisión conforme de documento antes del movimiento (Restricción 8).
  - 4-6-liquidacion: Liquidación trazable, costeo por viaje e integración ERP vía ACL.
"""
import os
import sys

from comun import Figura, ancho, ROJO, LINEA, BORDE, BORDE_FICHA, GRIS_CLARO, SUBRED

C4 = "04-arquitectura"


def figura_4_3_asignacion():
    """Diagrama de secuencia: verificación bloqueante del despacho antes de salir."""
    f = Figura("4-3-asignacion", C4, "V", alto=540)

    # Encabezado temático
    f.grupo(8, 8, 406, 52, "Verificación de asignación y reserva atómica", rx=5, peso=600)
    f.texto(16, 32, "Solicitud: orden + versión conocida + clave de idempotencia (RT-02.06)", 9)
    f.texto(16, 44, "Límite end-to-end: 30 s (RT-09.01) · Presupuesto de diseño: 25 s + 5 s de margen", 9, peso=600)

    # 5 Fases / Columnas de la secuencia
    cols = [
        (1, "1. Identidad", "Operador / API", 24, 68, 68),
        (2, "2. Evidencia", "Jornada y vigencias", 96, 68, 82),
        (3, "3. Reserva", "PostgreSQL ACID", 182, 68, 76),
        (4, "4. Decisión", "Invariantes", 262, 68, 70),
        (5, "5. Respuesta", "Outbox / Token", 336, 68, 70),
    ]

    for n, tit, sub, x, y, w in cols:
        f.grupo(x, y, w, 44, tit, rx=4, tam=9, peso=600)
        f.texto(x + w / 2, y + 36, sub, 9, anc="middle")
        # Línea de vida vertical
        cx = x + w / 2
        f.linea([(cx, y + 44), (cx, 380)], disc=True, flecha=None, color="#7A7A7A", grosor=0.7)

    # Tiempos de presupuesto asignados (barras proporcionales)
    f.ficha(cols[0][3] + cols[0][5] / 2, 126, "2 s")
    f.ficha(cols[1][3] + cols[1][5] / 2, 126, "8 s")
    f.ficha(cols[2][3] + cols[2][5] / 2, 126, "8 s")
    f.ficha(cols[3][3] + cols[3][5] / 2, 126, "4 s")
    f.ficha(cols[4][3] + cols[4][5] / 2, 126, "3 s")

    # Mensajes y flujos de secuencia entre líneas de vida
    # 1. Operador a Jornada y Vigencias
    c1 = cols[0][3] + cols[0][5] / 2
    c2 = cols[1][3] + cols[1][5] / 2
    c3 = cols[2][3] + cols[2][5] / 2
    c4 = cols[3][3] + cols[3][5] / 2
    c5 = cols[4][3] + cols[4][5] / 2

    # Mensaje 1: Solicitud de validación
    f.linea([(c1, 156), (c2, 156)])
    f.rotulo((c1 + c2) / 2, 152, "Valida Art. 25 bis + 6.000 vigencias")

    # Mensaje 2: Consulta concurrente de reserva en BD
    f.linea([(c2, 192), (c3, 192)])
    f.rotulo((c2 + c3) / 2, 188, "Bloqueo determinista de tracto y rampla")

    # Mensaje 3: Verificación de invariantes
    f.linea([(c3, 228), (c4, 228)])
    f.rotulo((c3 + c4) / 2, 224, "Aislamiento serializable confirmado")

    # Panel central: PostgreSQL Reglas y Garantías
    f.grupo(16, 252, 390, 48, "Garantías de aislamiento y concurrencia (PostgreSQL 16)", rx=4, relleno="#F8F9FA")
    f.texto(24, 276, "• Bloqueos ordenados por ID previenen deadlocks bajo reconexión masiva.", 9)
    f.texto(24, 288, "• Exclusión mutua estricta: un conductor o tracto no puede asignarse a 2 viajes.", 9)

    # Rama de decisión: Autorizado vs Bloqueado
    f.linea([(c4, 320), (c5, 320)])
    f.rotulo((c4 + c5) / 2, 316, "Invariantes OK · Commit outbox")

    # Resultado 1: Autorizado
    f.ficha(295, 350, ["AUTORIZADO", "Token de despacho emitido"], tam=9, peso=600)
    f.linea([(c4, 350), (c5, 350)], color="#1E824C", grosor=1.5)

    # Resultado 2: Bloqueado (Falla / conflicto / timeout)
    f.ficha(120, 350, ["BLOQUEADO", "Sin confirmación, no hay salida"], tam=9, peso=600)
    f.linea([(c4, 350), (c1, 350)], disc=True, color=ROJO, grosor=1.2)

    # Bloque inferior: Conclusiones normativas y de diseño
    f.grupo(8, 400, 406, 130, "Reglas de negocio y correlación probatoria", rx=5)
    f.marcador(26, 426, 1)
    f.texto(38, 428, "Sin decisión confirmada en <= 30 s, el sistema bloquea preventivamente.", 9)
    f.marcador(26, 452, 2)
    f.texto(38, 454, "La reserva del activo y la evidencia laboral quedan correlacionadas por UUID.", 9)
    f.marcador(26, 478, 3)
    f.texto(38, 480, "La clave de idempotencia se retiene 7 días en Redis y PostgreSQL (RT-02.06).", 9)
    f.marcador(26, 504, 4)
    f.texto(38, 506, "El token criptográfico autoriza el arranque del motor y la apertura de barrera.", 9)

    return f.guardar()


def figura_4_4_documento():
    """Diagrama de secuencia: emisión y cotejo del documento antes del movimiento."""
    f = Figura("4-4-documento", C4, "V", alto=540)

    # Encabezado temático
    f.grupo(8, 8, 406, 52, "Documento conforme antes del movimiento (Restricción 8)", rx=5, peso=600)
    f.texto(16, 32, "El ERP contable de 2013 conserva la emisión y firma exclusiva del DET.", 9)
    f.texto(16, 44, "Cotejo offline en cabina: el camión no inicia movimiento sin el archivo original.", 9, peso=600)

    # 4 Actores / Columnas
    cols = [
        (1, "1. audIT Plataforma", "Preparación viaje", 16, 68, 90),
        (2, "2. Capa ACL", "Traductor SOAP/XML", 114, 68, 88),
        (3, "3. ERP 2013", "Emisor único tributario", 210, 68, 94),
        (4, "4. Dispositivo G26I", "Cabina / Terreno", 312, 68, 94),
    ]

    for n, tit, sub, x, y, w in cols:
        f.grupo(x, y, w, 44, tit, rx=4, tam=9, peso=600)
        f.texto(x + w / 2, y + 36, sub, 9, anc="middle")
        cx = x + w / 2
        f.linea([(cx, y + 44), (cx, 396)], disc=True, flecha=None, color="#7A7A7A", grosor=0.7)

    c1 = cols[0][3] + cols[0][5] / 2
    c2 = cols[1][3] + cols[1][5] / 2
    c3 = cols[2][3] + cols[2][5] / 2
    c4 = cols[3][3] + cols[3][5] / 2

    # Paso 1: Preparación anticipada
    f.linea([(c1, 136), (c2, 136)])
    f.rotulo((c1 + c2) / 2, 132, "1. Datos definitivos de carga y viaje")

    # Paso 2: Solicitud al ERP
    f.linea([(c2, 168), (c3, 168)])
    f.rotulo((c2 + c3) / 2, 164, "2. Solicitud de folio y firma electrónica")

    # Paso 3: Retorno del documento firmado
    f.linea([(c3, 204), (c2, 204)])
    f.rotulo((c2 + c3) / 2, 200, "3. DET firmado + certificado digital SII")

    # Paso 4: Custodia y descarga en cabina
    f.linea([(c2, 240), (c1, 240)])
    f.rotulo((c1 + c2) / 2, 236, "4. Hash SHA-256 + acuse registrado")

    f.linea([(c1, 276), (c4, 276)])
    f.rotulo((c1 + c4) / 2, 272, "5. Descarga cifrada en cabina (antes de zona sin señal)")

    # Paso 5: Cotejo en punto de carga (offline)
    f.grupo(40, 298, 342, 50, "Cotejo local en punto de carga sin cobertura", rx=4, relleno="#F8F9FA")
    f.texto(50, 324, "• Compara pesaje de báscula + conductor efectivo vs DET firmado.", 9)
    f.texto(50, 338, "• Si no coincide: rechaza inicio de marcha y emite alerta satelital.", 9)

    # Decisión de salida en terreno
    f.linea([(c4, 366), (c4, 386)], flecha="fin")
    f.ficha(c4, 376, "Decisión en terreno")

    f.ficha(240, 376, ["CONFORME: Movimiento autorizado", "Folio y hash validados"], tam=9, peso=600)
    f.ficha(80, 376, ["DISCREPANCIA: Bloqueo", "Inmovilización de salida"], tam=9, peso=600)

    # Bloque inferior: Respaldo y garantías
    f.grupo(8, 412, 406, 118, "Garantías tributarias y operacionales (Restricción 8)", rx=5)
    f.marcador(26, 436, 1)
    f.texto(38, 438, "Folios y certificados tributarios permanecen en el ERP 2013 (emisor único).", 9)
    f.marcador(26, 460, 2)
    f.texto(38, 462, "El dispositivo embarcado verifica la firma digital y el hash del documento localmente.", 9)
    f.marcador(26, 484, 3)
    f.texto(38, 486, "En puntos sin cobertura, la emisión de emergencia se transmite por Iridium (<= 340 bytes).", 9)
    f.marcador(26, 508, 4)
    f.texto(38, 510, "Cualquier alteración en el archivo invalida el hash y activa el bloqueo de despacho.", 9)

    return f.guardar()


def figura_4_6_liquidacion():
    """Diagrama de secuencia: estimación de costo por viaje y liquidación ERP."""
    f = Figura("4-6-liquidacion", C4, "V", alto=540)

    # Encabezado temático
    f.grupo(8, 8, 406, 52, "Liquidación trazable e integración ERP", rx=5, peso=600)
    f.texto(16, 32, "La liquidación conserva fuente, calidad, reglas versionadas y revisión humana.", 9)
    f.texto(16, 44, "ERP contable de 2013 actúa como emisor único de órdenes de pago (RT-05.29).", 9, peso=600)

    # 5 Columnas de actores
    cols = [
        (1, "1. Terreno", "Conductor / G26I", 12, 68, 76),
        (2, "2. Evidencias", "Jornada y Peajes", 94, 68, 80),
        (3, "3. Costeo", "Liquidación audIT", 180, 68, 78),
        (4, "4. Revisor", "Operaciones / QA", 264, 68, 72),
        (5, "5. ACL / ERP", "ERP 2013 Contable", 342, 68, 68),
    ]

    for n, tit, sub, x, y, w in cols:
        f.grupo(x, y, w, 44, tit, rx=4, tam=9, peso=600)
        f.texto(x + w / 2, y + 36, sub, 9, anc="middle")
        cx = x + w / 2
        f.linea([(cx, y + 44), (cx, 396)], disc=True, flecha=None, color="#7A7A7A", grosor=0.7)

    c1 = cols[0][3] + cols[0][5] / 2
    c2 = cols[1][3] + cols[1][5] / 2
    c3 = cols[2][3] + cols[2][5] / 2
    c4 = cols[3][3] + cols[3][5] / 2
    c5 = cols[4][3] + cols[4][5] / 2

    # Paso 1: Fin de viaje y subida de datos
    f.linea([(c1, 136), (c2, 136)])
    f.rotulo((c1 + c2) / 2, 132, "1. Odómetro + peajes + ticket de entrega")

    # Paso 2: Validación de evidencia
    f.linea([(c2, 168), (c3, 168)])
    f.rotulo((c2 + c3) / 2, 164, "2. Evidencia validada · Fuente y calidad")

    # Ficha técnica: Reglas de valores nulos
    f.ficha((c2 + c3) / 2, 198, "REAL / ESTIMADO exigen fuente · AUSENTE -> NULL (nunca 0)", tam=9, peso=600)

    # Paso 3: Costeo preliminar < 24 h
    f.linea([(c3, 232), (c4, 232)])
    f.rotulo((c3 + c4) / 2, 228, "3. Costo preliminar < 24 h (RT-05.29)")

    # Paso 4: Revisión y aprobación
    f.linea([(c4, 268), (c3, 268)])
    f.rotulo((c3 + c4) / 2, 264, "4. Aprobación con reglas versionadas")

    # Paso 5: Persistencia Outbox idempotente
    f.linea([(c3, 304), (c5, 304)])
    f.rotulo((c3 + c5) / 2, 300, "5. id_operacion estable + patrón outbox")

    # Paso 6: Contabilización en ERP
    f.linea([(c5, 342), (c3, 342)])
    f.rotulo((c3 + c5) / 2, 338, "6. Folio contable + comprobante retornado")

    # Ficha outbox
    f.ficha((c3 + c5) / 2, 372, "Reintentos idempotentes evitan duplicar pagos en ERP", tam=9)

    # Bloque inferior: Reglas normativas de costeo y liquidación
    f.grupo(8, 412, 406, 118, "Políticas de costeo y conciliación financiera", rx=5)
    f.marcador(26, 436, 1)
    f.texto(38, 438, "El cierre del viaje y las fórmulas versionadas permiten reproducir el costo exacto.", 9)
    f.marcador(26, 460, 2)
    f.texto(38, 462, "Evidencia insuficiente deja el componente en NULL y abre excepción para revisión.", 9)
    f.marcador(26, 484, 3)
    f.texto(38, 486, "El ERP 2013 es el único facultado para emitir transferencias y liquidaciones finales.", 9)
    f.marcador(26, 508, 4)
    f.texto(38, 510, "Costo consolidado disponible a 24 h; conciliación definitiva a cierre mensual.", 9)

    return f.guardar()


FIGURAS = [figura_4_3_asignacion, figura_4_4_documento, figura_4_6_liquidacion]
