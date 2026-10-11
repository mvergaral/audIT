"""Secuencias de D3: mensajes, respuestas y ramas de fallo explícitas."""
from comun import Figura,titulo,actor,mensaje,nota,SUBRED

def figura_4_3_asignacion():
    f=Figura('4-3-asignacion'); titulo(f,'Asignación bloqueante del viaje')
    xs=[78,220,366,510,651]
    for x,n in zip(xs,[['Operador / API'],['Planificación','y tráfico'],['Personas / Flota','Servicios de validación'],['PostgreSQL','Reserva y outbox'],['Bus de eventos','Consumidores']]): actor(f,x,n)
    mensaje(f,xs,0,1,106,'Orden, recursos y clave de idempotencia')
    mensaje(f,xs,1,2,142,'Jornada, habilitaciones y aptitud · en paralelo')
    mensaje(f,xs,2,1,178,'Veredicto + versión + evidencia',True)
    f.grupo(14,199,701,97,None,rx=3)
    f.rotulo(23,214,'Si todas las reglas habilitan',anc='start',tam=10,peso=600)
    mensaje(f,xs,1,3,231,'Reserva única + asignación + outbox · una transacción')
    mensaje(f,xs,3,1,261,'Commit confirmado',True)
    mensaje(f,xs,1,0,285,'Asignación confirmada',True)
    mensaje(f,xs,3,4,324,'Publicación desde outbox · entrega al menos una vez')
    f.grupo(14,344,701,55,None,rx=3,relleno=SUBRED)
    f.rotulo(23,359,'Si hay bloqueo legal, conflicto o límite agotado',anc='start',tam=10,peso=600)
    mensaje(f,xs,1,0,384,'Rechazo trazable · no asignar',True)
    nota(f,411,['Techo contractual: 30 s de extremo a extremo. Presupuesto de diseño: 25 s + 5 s de margen.',
                'RN-04 sólo admite excepción aprobada ante fuente indisponible; nunca ante una causa legal.'])
    return f.guardar()

def figura_4_4_documento():
    f=Figura('4-4-documento'); titulo(f,'Documento de transporte antes del movimiento')
    xs=[78,220,366,510,651]
    for x,n in zip(xs,[['Cabina','Datos de carga'],['Operación de fletes','Validación'],['Capa anticorrupción','Adaptador contable'],['Sistema contable','Único emisor'],['Custodia / SII','Envío y respaldo']]): actor(f,x,n)
    mensaje(f,xs,0,1,108,'Datos definitivos · anticipados o por enlace satelital')
    mensaje(f,xs,1,2,148,'Solicitud idempotente de emisión')
    mensaje(f,xs,2,3,187,'Contrato de emisión homologado')
    mensaje(f,xs,3,4,227,'Documento firmado · envío fiscal y custodia')
    mensaje(f,xs,3,2,266,'Documento y representación del mismo contenido',True)
    mensaje(f,xs,2,0,307,'Entrega completa · acuse e integridad verificados',True)
    f.grupo(14,329,701,70,None,rx=3,relleno=SUBRED)
    f.rotulo(26,344,'Comprobación antes de salir',anc='start',tam=10,peso=600)
    f.rotulo(26,357,'Datos de carga coinciden + documento válido disponible + representación portable conforme.',anc='start')
    f.rotulo(26,381,'Ausencia, discrepancia o expiración del plazo: salida bloqueada; corrección y nueva evaluación.',anc='start')
    nota(f,411,['RT-09.01 del Caso: emisión ≤ 90 s. Un folio recibido por sí solo no habilita el traslado.',
                'Cabina y terminal conservan copias; no custodian CAF ni claves de firma del emisor.'])
    return f.guardar()

def figura_4_6_liquidacion():
    f=Figura('4-6-liquidacion'); titulo(f,'Costeo por viaje y liquidación mensual')
    xs=[78,220,366,510,651]
    for x,n in zip(xs,[['Operación de fletes'],['Liquidación','y costeo'],['Fuentes de costo','Combustible / peajes'],['Transportista','Portal y conformidad'],['ACL / contable','Registro y acuse']]): actor(f,x,n)
    mensaje(f,xs,0,1,106,'Viaje cerrado · distancias, tiempos y respaldos')
    mensaje(f,xs,1,3,148,'v1 ≤ 24 h · componentes disponibles y faltantes')
    mensaje(f,xs,2,1,190,'Lotes conciliados · combustible hasta 40 días')
    mensaje(f,xs,1,3,232,'v2…vn · costo actualizado sin sobrescribir v1')
    mensaje(f,xs,1,3,274,'Propuesta de liquidación mensual + detalle por viaje')
    mensaje(f,xs,3,1,310,'Aceptación firmada o discrepancia trazable',True)
    mensaje(f,xs,1,4,351,'Liquidación aprobada · clave de idempotencia')
    mensaje(f,xs,4,1,387,'Acuse contable y conciliación',True)
    nota(f,411,['El costo preliminar de un viaje y la liquidación mensual son registros distintos.',
                'Sin acuse contable permanece pendiente; el reintento no duplica el registro financiero.'])
    return f.guardar()

def figura_4_7_reconexion():
    f=Figura('4-7-reconexion'); titulo(f,'Reconexión automática y conciliación por camión')
    xs=[78,220,366,510,651]
    for x,n in zip(xs,[['Equipo a bordo','SQLite / outbox'],['IoT Hub','Identidad y cuotas'],['Event Hubs','Partición por equipo'],['Consumidor','Deduplicación'],['Persistencia','Acuse duradero']]): actor(f,x,n)
    mensaje(f,xs,0,1,106,'Reautenticar · último acuse y secuencia local')
    mensaje(f,xs,1,0,146,'Ventana de envío + reintento con variación aleatoria',True)
    mensaje(f,xs,0,1,187,'Lotes numerados · prioridad a jornada y tiempos')
    mensaje(f,xs,1,2,227,'Admisión al flujo · aún no es confirmación final')
    mensaje(f,xs,2,3,267,'Evento y secuencia · entrega al menos una vez')
    mensaje(f,xs,3,4,307,'INSERT único + conflictos auditados')
    mensaje(f,xs,4,0,347,'Acuse después de commit · cursor confirmado',True)
    f.rotulo(78,384,'Depurar sólo lo confirmado')
    nota(f,411,['Caso RT-03.13: ≤ 20 min por camión tras 72 h. Perfil de prueba: 300 unidades simultáneas.',
                '288 h es una ampliación propuesta; requiere ensayo independiente y nunca sustituye el de 72 h.'])
    return f.guardar()

FIGURAS=[figura_4_3_asignacion,figura_4_4_documento,figura_4_6_liquidacion,figura_4_7_reconexion]
