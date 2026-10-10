"""Subdocumento 5: Modelo y Gestión de Datos (Fase 1 y Fase 2).

Implementa las figuras oficiales del modelo y ciclo de vida de los datos:
  - 5-2-custodia: Cadena de custodia forense append-only y rectificación auditable.
  - 5-3-permisos: Soberanía de datos, gestión de consentimiento y ciclo de vida Ley 21.719.
  - audit-figura-5.3-cap: Clasificación de motores bajo el Teorema CAP.
  - audit-figura-5.4-cdc: Segregación OLTP / OLAP mediante Change Data Capture (CDC).
  - audit-figura-5.5-migracion: Metodología de migración de las 6.000 vigencias documentales.
  - audit-figura-5.6-desempeno: Estrategia de particionamiento, índices y retención.
  - audit-figura-5.2-mdm: Gestión de Datos Maestros (MDM) y Capa Anticorrupción.
  - audit-figura-5.1-erd: Modelo conceptual y relacional de persistencia.
"""
import os
import sys

from comun import Figura, ancho, ROJO, LINEA, BORDE, BORDE_FICHA, GRIS_CLARO, SUBRED

C5 = "05-datos"


def figura_5_2_custodia():
    """Cadena de custodia forense append-only y almacenamiento inmutable."""
    f = Figura("5-2-custodia", C5, "V", alto=540)

    # Encabezado temático
    f.grupo(8, 8, 406, 52, "Cadena de custodia forense append-only y rectificación", rx=5, peso=600)
    f.texto(16, 32, "Fuente y nivel 0-5 se conservan por separado; no prueban veracidad por sí mismos.", 9)
    f.texto(16, 44, "Inmutabilidad matemática: encadenamiento SHA-256 y bloqueo WORM (RT-16.07).", 9, peso=600)

    # 3 Columnas principales de fases
    cols = [
        ("1. Captura identificada", 16, 68, 122),
        ("2. Validación de esquema", 146, 68, 130),
        ("3. Custodia inmutable", 284, 68, 130),
    ]

    for tit, x, y, w in cols:
        f.grupo(x, y, w, 80, tit, rx=4, tam=9, peso=600)

    # Detalle columna 1
    f.texto(22, 94, "• Conductor + fuente", 9)
    f.texto(22, 106, "• Marca de tiempo UTC", 9)
    f.texto(22, 118, "• Secuencia monótona", 9)
    f.texto(22, 130, "• Nivel de certeza 0-5", 9)

    # Detalle columna 2
    f.texto(152, 94, "• Esquema Protobuf/JSON", 9)
    f.texto(152, 106, "• Firma del dispositivo", 9)
    f.texto(152, 118, "• Canonicalización canónica", 9)
    f.texto(152, 130, "• Verificación de identidad", 9)

    # Detalle columna 3
    f.texto(290, 94, "• Hash previo + actual", 9)
    f.texto(290, 106, "• Hash Chain SHA-256", 9)
    f.texto(290, 118, "• Acuse persistente", 9)
    f.texto(290, 130, "• Bloqueo append-only", 9)

    # Flechas entre fases superiores
    f.linea([(138, 108), (146, 108)])
    f.linea([(276, 108), (284, 108)])

    # Bloque central: Cadena de rectificación (E1, E2, E3)
    f.grupo(16, 160, 390, 136, "Cadena de rectificación auditable (Modelo de tuplas inmutables)", rx=5, relleno="#F8F9FA")

    # Tupla E1/E2
    f.rect(26, 184, 170, 48, relleno="#FFFFFF", rx=3)
    f.texto(32, 198, "E1 / E2: Registros originales", 9, peso=600)
    f.texto(32, 210, "• Jornada de conducción y descanso", 9)
    f.texto(32, 222, "• Evaluación V1 inicial conforme", 9)

    # Tupla E3 Rectificatoria
    f.rect(226, 184, 170, 48, relleno="#FFFFFF", rx=3)
    f.texto(232, 198, "E3: Rectificación vinculada", 9, peso=600)
    f.texto(232, 210, "• FK evidencia_rect_id -> E1", 9)
    f.texto(232, 222, "• Motivo auditable preservado", 9)

    # Flecha de enlace entre registros
    f.linea([(196, 208), (226, 208)])
    f.rotulo(211, 204, "Enlace", anc="middle")

    # Reglas de versión y evaluación V2
    f.ficha(206, 256, "Evaluación V2: Aplica reglas versionadas referenciando E1, E2 y E3 sin borrar", tam=9, peso=600)

    # Panel de Almacenamiento y Seguridad WORM
    f.grupo(16, 308, 390, 92, "Mecanismos de inmutabilidad física y lógica", rx=4)
    f.texto(26, 334, "• Base de datos: Revocación total de UPDATE, DELETE y TRUNCATE a roles de app.", 9)
    f.texto(26, 348, "• Azure Blob Storage WORM: Bloqueo de retención legal (Legal Hold) inmodificable.", 9)
    f.texto(26, 362, "• Prueba negativa forense: La alteración de 1 byte rompe la cadena criptográfica.", 9)
    f.texto(26, 376, "• Retención obligatoria: 5 años para jornada laboral (DT) y 6 años para DET (SII).", 9)

    # Bloque inferior: Conclusiones
    f.grupo(8, 410, 406, 120, "Garantías de validez probatoria ante fiscalización laboral", rx=5)
    f.marcador(26, 434, 1)
    f.texto(38, 436, "Cualquier rectificación de jornada genera un nuevo registro inmutable; no sobreescribe.", 9)
    f.marcador(26, 458, 2)
    f.texto(38, 460, "La cadena de hashes SHA-256 garantiza trazabilidad inalterable ante la Dirección del Trabajo.", 9)
    f.marcador(26, 482, 3)
    f.texto(38, 484, "La falta de evidencia suficiente mantiene el bloqueo del despacho del viaje.", 9)
    f.marcador(26, 506, 4)
    f.texto(38, 508, "Exportación forense independiente con certificados y firmas públicas de verificación.", 9)

    return f.guardar()


def figura_5_3_permisos():
    """Soberanía de datos, gestión de consentimiento y ciclo de vida Ley 21.719."""
    f = Figura("5-3-permisos", C5, "V", alto=540)

    # Encabezado temático
    f.grupo(8, 8, 406, 52, "Soberanía de datos, consentimiento y ciclo de vida Ley 21.719", rx=5, peso=600)
    f.texto(16, 32, "Base de tratamiento por titular; el permiso comercial no sustituye al laboral.", 9)
    f.texto(16, 44, "Privacidad por diseño (PbD) y destrucción criptográfica (NIST SP 800-88).", 9, peso=600)

    # 4 Titulares
    titulares = [
        ("Conductores propios", ["196 choferes", "Art. 25 bis"], 16, 68, 92),
        ("Conductores terceros", ["258 choferes", "Subcontratados"], 114, 68, 94),
        ("Transportistas pymes", ["148 pymes", "Comercial"], 214, 68, 92),
        ("Clientes corporativos", ["84 clientes", "Destinos"], 312, 68, 92),
    ]

    for tit, lineas, x, y, w in titulares:
        f.grupo(x, y, w, 48, tit, rx=4, tam=9, peso=600)
        f.texto(x + w / 2, y + 30, lineas[0], 9, anc="middle")
        f.texto(x + w / 2, y + 42, lineas[1], 9, anc="middle")

    # Tabla central de Consentimiento y Alcance
    f.grupo(16, 126, 390, 80, "Entidad CONSENTIMIENTO_DATOS y atributos de soberanía", rx=5, relleno="#F8F9FA")
    f.texto(26, 150, "• id_consentimiento (UUIDv4) · Clave primaria de trazabilidad legal", 9, peso=600)
    f.texto(26, 164, "• comparte_posicion (Boolean) · GPS habilitado exclusivamente durante viaje activo", 9)
    f.texto(26, 178, "• comparte_telemetria (Boolean) · Lectura de odómetro y CANbus autorizada", 9)
    f.texto(26, 192, "• fecha_otorgamiento / fecha_revocacion · Sello de tiempo UTC inmutable", 9)

    # Mecanismos de soberanía en cabina y nube
    f.grupo(16, 216, 188, 96, "Borde y Cabina (Offline)", rx=4)
    f.texto(24, 240, "• Lease temporal < 5 min.", 9, peso=600)
    f.texto(24, 254, "• Sin renovación por API:", 9)
    f.texto(24, 266, "  inhibe GPS fuera de flete.", 9)
    f.texto(24, 280, "• Botón de desconexión.", 9)
    f.texto(24, 294, "• Acuse criptográfico local.", 9)

    f.grupo(218, 216, 188, 96, "Nube y API (Soberanía)", rx=4)
    f.texto(226, 240, "• Ejercicio derechos ARCO.", 9, peso=600)
    f.texto(226, 254, "• Revocación inmediata de", 9)
    f.texto(226, 266, "  visibilidad a clientes.", 9)
    f.texto(226, 280, "• Bloqueo operativo seguro.", 9)
    f.texto(226, 294, "• Manifiesto de excepciones.", 9)

    # Ciclo de vida y Retención Legal
    f.grupo(16, 320, 390, 80, "Ciclo de vida y preservación legal de datos personales", rx=5, relleno="#F8F9FA")
    f.texto(26, 344, "1. Viaje Activo: Telemetría y geocercas en caliente (TimescaleDB / Redis).", 9)
    f.texto(26, 358, "2. Retención Obligatoria: 5 años laboral (DT), 6 años tributaria (SII), 10 años siniestros.", 9)
    f.texto(26, 372, "3. Vencimiento Legal: Crypto-shredding irreversible (destrucción de KEK en Key Vault).", 9)
    f.texto(26, 386, "   Conforme a NIST SP 800-88 Rev. 1, imposibilitando la recuperación de datos cifrados.", 9)

    # Bloque inferior: Conclusiones
    f.grupo(8, 410, 406, 120, "Cumplimiento normativo estricto Ley N.º 21.719", rx=5)
    f.marcador(26, 434, 1)
    f.texto(38, 436, "La revocación detiene transmisiones futuras pero no destruye la evidencia laboral obligatoria.", 9)
    f.marcador(26, 458, 2)
    f.texto(38, 460, "El dispositivo embarcado respeta la privacidad del chofer fuera de su turno de conducción.", 9)
    f.marcador(26, 482, 3)
    f.texto(38, 484, "Cifrado a nivel de campo (FLE) con claves maestras administradas en Azure Key Vault HSM.", 9)
    f.marcador(26, 506, 4)
    f.texto(38, 508, "Transportes Curimón actúa como Responsable; audIT opera como Encargado (Art. 15 bis).", 9)

    return f.guardar()


def figura_5_3_cap():
    """Clasificación de motores y almacenamiento bajo el Teorema CAP."""
    f = Figura("audit-figura-5.3-cap", C5, "V", alto=480)

    f.grupo(8, 8, 406, 52, "Clasificación de motores bajo el Teorema CAP", rx=5, peso=600)
    f.texto(16, 32, "Segregación técnica según consistencia, disponibilidad y tolerancia a fallos.", 9)
    f.texto(16, 44, "Diseño políglota: ningún motor asume funciones fuera de su perfil óptimo.", 9, peso=600)

    # 3 Grupos CAP
    f.grupo(16, 68, 390, 86, "Consistencia + Tolerancia a Particiones (CP) · Transaccional", rx=4)
    f.texto(26, 96, "• Motor: Azure Database for PostgreSQL 16 Flexible Server (Multi-AZ)", 9, peso=600)
    f.texto(26, 110, "• Dominio: Asignación bloqueante, órdenes de viaje, liquidaciones y cadena de custodia.", 9)
    f.texto(26, 124, "• Garantía: Aislamiento serializable, transacciones ACID estrictas y cero doble despacho.", 9)
    f.texto(26, 138, "• Conmutación: Réplica síncrona en zona de disponibilidad con RPO = 0.", 9)

    f.grupo(16, 162, 390, 86, "Disponibilidad + Tolerancia a Particiones (AP) · Telemetría y Borde", rx=4)
    f.texto(26, 190, "• Motores: TimescaleDB (series temporales en nube) + SQLite WAL (borde cabina)", 9, peso=600)
    f.texto(26, 204, "• Dominio: Ingesta masiva de 374 camiones cada 30 s, telemetría CANbus y geocercas.", 9)
    f.texto(26, 218, "• Garantía: Ingesta continua garantizada; tolera hasta 72 h desconectado en frontera.", 9)
    f.texto(26, 232, "• Reconciliación: Reenvío con control de versión e inserción idempotente.", 9)

    f.grupo(16, 256, 390, 86, "Baja Latencia y Sesión · Caché en Memoria", rx=4)
    f.texto(26, 284, "• Motor: Azure Cache for Redis Premium (Clustering Multi-AZ)", 9, peso=600)
    f.texto(26, 298, "• Dominio: Claves de idempotencia de 7 días, tokens de sesión y leases de permisos.", 9)
    f.texto(26, 312, "• Garantía: Respuestas en < 10 ms para pre-validación de despachos y auth tokens.", 9)
    f.texto(26, 326, "• Respaldo: Caída de caché degrada a consulta directa en PostgreSQL sin pérdida de datos.", 9)

    f.grupo(16, 350, 390, 74, "Almacenamiento Inmutable WORM · Archivo Legal", rx=4, relleno="#F8F9FA")
    f.texto(26, 376, "• Motor: Azure Blob Storage con Inmutable Storage (Legal Hold)", 9, peso=600)
    f.texto(26, 390, "• Dominio: Documentos electrónicos DET firmados, bitácoras SHA-256 y pólizas.", 9)
    f.texto(26, 404, "• Garantía: Prohibición física de borrado o sobreescritura durante el período legal.", 9)

    f.ficha(211, 442, "Arquitectura políglota optimizada: consistencia en negocio, resiliencia en terreno", tam=9, peso=600)

    return f.guardar()


def figura_5_4_cdc():
    """Segregación transaccional OLTP y analítica OLAP mediante CDC."""
    f = Figura("audit-figura-5.4-cdc", C5, "V", alto=440)

    f.grupo(8, 8, 406, 52, "Segregación transaccional OLTP y analítica mediante CDC", rx=5, peso=600)
    f.texto(16, 32, "Desacoplamiento total entre transacciones críticas y consultas pesadas de BI.", 9)
    f.texto(16, 44, "Ingesta basada en logs: Debezium + Apache Kafka / Event Hubs (RT-05.05).", 9, peso=600)

    # 4 Etapas del Pipeline CDC
    f.grupo(16, 68, 86, 76, "1. OLTP", rx=4)
    f.texto(24, 96, "PostgreSQL 16", 9, peso=600)
    f.texto(24, 110, "WAL Engine", 9)
    f.texto(24, 124, "ACID puro", 9)

    f.grupo(114, 68, 88, 76, "2. Captura", rx=4)
    f.texto(122, 96, "Debezium", 9, peso=600)
    f.texto(122, 110, "Lee el WAL", 9)
    f.texto(122, 124, "Cero impacto", 9)

    f.grupo(214, 68, 92, 76, "3. Streaming", rx=4)
    f.texto(222, 96, "Kafka / Event", 9, peso=600)
    f.texto(222, 110, "Event Hubs", 9)
    f.texto(222, 124, "Bus durable", 9)

    f.grupo(318, 68, 88, 76, "4. OLAP", rx=4)
    f.texto(326, 96, "Delta Lake", 9, peso=600)
    f.texto(326, 110, "Lakehouse", 9)
    f.texto(326, 124, "Power BI", 9)

    # Conexiones horizontales
    f.linea([(102, 106), (114, 106)])
    f.linea([(202, 106), (214, 106)])
    f.linea([(306, 106), (318, 106)])

    # Bloque de Beneficios de Arquitectura
    f.grupo(16, 160, 390, 130, "Garantías de aislamiento operacional y latencia", rx=5, relleno="#F8F9FA")
    f.texto(26, 184, "• Cero contención de bloqueo: Las consultas de costo por km no bloquean tablas transaccionales.", 9)
    f.texto(26, 198, "• Replicación asíncrona sub-segundo: Los eventos de viaje se reflejan en el bus en < 1 s.", 9)
    f.texto(26, 212, "• Trazabilidad histórica completa: CDC captura inserciones, actualizaciones y estados previos.", 9)
    f.texto(26, 226, "• Resiliencia ante caídas analíticas: Si el Lakehouse se detiene, el bus retiene eventos.", 9)
    f.texto(26, 240, "• Formato abierto Delta Lake: Consultas reproducibles y gobernadas por OpenMetadata.", 9)
    f.texto(26, 254, "• Cumple RT-05.05: Segregación física obligatoria entre bases transaccionales y analíticas.", 9, peso=600)

    # Bloque inferior
    f.grupo(8, 306, 406, 114, "Métricas y Acuerdos de Nivel de Servicio (SLA)", rx=5)
    f.marcador(26, 330, 1)
    f.texto(38, 332, "Costo por kilómetro y liquidación preliminar calculados en < 24 horas (RT-05.29).", 9)
    f.marcador(26, 352, 2)
    f.texto(38, 354, "Telemetría de posición reflejada en torre de control en <= 2 minutos.", 9)
    f.marcador(26, 374, 3)
    f.texto(38, 376, "Reportes de emisiones de CO2 y conciliación consolidada disponibles mensualmente.", 9)
    f.marcador(26, 396, 4)
    f.texto(38, 398, "El motor transaccional mantiene 100 % de su CPU dedicada al despacho de camiones.", 9)

    return f.guardar()


def figura_5_5_migracion():
    """Metodología de extracción, saneamiento, carga y conciliación histórica."""
    f = Figura("audit-figura-5.5-migracion", C5, "V", alto=540)

    f.grupo(8, 8, 406, 52, "Metodología de migración de 6.000 vigencias documentales", rx=5, peso=600)
    f.texto(16, 32, "Transición ordenada desde 4 planillas Excel y ERP 2013 hacia PostgreSQL.", 9)
    f.texto(16, 44, "Control de calidad en 5 fases con conciliación paralela y corte sin pérdida de datos.", 9, peso=600)

    fases = [
        ("Fase 1: Extracción y Catalogación", "4 planillas Excel (flota, choferes, talleres, contratos) + ERP 2013", 68),
        ("Fase 2: Saneamiento y Normalización", "Detección de duplicados, validación de RUT, patentes y fechas vencidas", 136),
        ("Fase 3: Validación con Padrones", "Cotejo con padrones oficiales (MTT, SEC, mutualidades laborales)", 204),
        ("Fase 4: Carga Atómica Versionada", "Inserción con control de versiones en PostgreSQL; hash SHA-256", 272),
        ("Fase 5: Conciliación y Marcha Blanca", "Operación paralela de 90 días; conciliación del 100 % antes del corte", 340),
    ]

    for tit, desc, y in fases:
        f.grupo(16, y, 390, 56, tit, rx=4)
        f.texto(26, y + 26, desc, 9)
        f.texto(26, y + 40, "Control: Trazabilidad por fila, bitácora de anomalías y firma de aceptación", 9, peso=600)

    # Conexiones verticales entre fases
    for y in [124, 192, 260, 328]:
        f.linea([(211, y), (211, y + 12)])

    # Bloque inferior
    f.grupo(8, 412, 406, 118, "Criterios de éxito y contingencia de corte (Rollback)", rx=5)
    f.marcador(26, 436, 1)
    f.texto(38, 438, "Cero discrepancias permitidas en habilitaciones de conductores de sustancias peligrosas.", 9)
    f.marcador(26, 460, 2)
    f.texto(38, 462, "Las 6.000 vigencias quedan registradas con fecha de vencimiento y alerta proactiva.", 9)
    f.marcador(26, 484, 3)
    f.texto(38, 486, "Plan de rollback: Durante la marcha blanca se conserva espejo en frío del sistema legado.", 9)
    f.marcador(26, 508, 4)
    f.texto(38, 510, "Corte definitivo formalizado en acta conjunta entre Curimón y audIT (Etapa 1).", 9)

    return f.guardar()


def figura_5_6_desempeno():
    """Estrategia integral de desempeño, particionamiento y retención."""
    f = Figura("audit-figura-5.6-desempeno", C5, "V", alto=480)

    f.grupo(8, 8, 406, 52, "Estrategia integral de desempeño de base de datos", rx=5, peso=600)
    f.texto(16, 32, "Particionamiento, índices BRIN/B-Tree y tiering de almacenamiento.", 9)
    f.texto(16, 44, "Diseñado para sostener 41 millones de km anuales y 3x volumetría inicial (RT-09.03).", 9, peso=600)

    f.grupo(16, 68, 390, 80, "Particionamiento Temporal de Tablas", rx=4)
    f.texto(26, 96, "• Telemetría (POSICION_GPS): Particionamiento por rango mensual (TimescaleDB chunks).", 9, peso=600)
    f.texto(26, 110, "• Transacciones (VIAJE / DESPACHO): Particionamiento por año calendario.", 9)
    f.texto(26, 124, "• Beneficio: Mantenimiento modular; borrado instantáneo vía DROP PARTITION sin vaciado.", 9)
    f.texto(26, 138, "• Compresión automática de chunks antiguos: Reduce hasta 85 % el volumen en disco.", 9)

    f.grupo(16, 156, 390, 80, "Estrategia de Indexación Especializada", rx=4)
    f.texto(26, 184, "• Índices BRIN (Block Range Index): En marcas temporales telemáticas (uso mínimo de RAM).", 9, peso=600)
    f.texto(26, 198, "• Índices B-Tree parciales: En viajes con estado activo (acelera despacho bloqueante).", 9)
    f.texto(26, 212, "• Índices GIN: En columnas de datos semiestructurados JSONB y atributos de auditoría.", 9)
    f.texto(26, 226, "• Regla: Prohibición de índices redundantes para evitar degradación de escritura.", 9)

    f.grupo(16, 244, 390, 80, "Tiering de Almacenamiento y Ciclo de Vida", rx=4)
    f.texto(26, 272, "• Capa Caliente (Hot SSD Premium): Datos transaccionales y telemetría de últimos 90 días.", 9, peso=600)
    f.texto(26, 286, "• Capa Tibia (Warm Cool Blob): Historial de viajes cerrados entre 90 días y 2 años.", 9)
    f.texto(26, 300, "• Capa Fría (Archive WORM): Retención legal inmutable hasta 10 años (DT, SII, siniestros).", 9)
    f.texto(26, 314, "• Optimización económica: Minimiza costo de almacenamiento cloud respetando SLA.", 9)

    f.grupo(16, 332, 390, 72, "Conexiones y Caché en Memoria", rx=4, relleno="#F8F9FA")
    f.texto(26, 358, "• PgBouncer integrado: Agrupamiento de conexiones con modo de transacción.", 9)
    f.texto(26, 372, "• Redis L2 Cache: Claves de idempotencia y tablas de referencia maestras en RAM.", 9)
    f.texto(26, 386, "• Límite: Mantiene uso de CPU transaccional por debajo del 65 % bajo carga pico.", 9, peso=600)

    f.ficha(211, 442, "Escalabilidad probada: soporta el triple de demanda sin alterar el modelo lógico", tam=9, peso=600)

    return f.guardar()


def figura_5_2_mdm():
    """Gestión de Datos Maestros (MDM) y Capa Anticorrupción."""
    f = Figura("audit-figura-5.2-mdm", C5, "V", alto=480)

    f.grupo(8, 8, 406, 52, "Gestión de Datos Maestros (MDM) y Capa Anticorrupción", rx=5, peso=600)
    f.texto(16, 32, "Catálogo maestro unificado y sincronización con sistemas legados.", 9)
    f.texto(16, 44, "Gobierno centralizado en OpenMetadata con diccionario de datos activo.", 9, peso=600)

    maestros = [
        ("Tractocamiones y Ramplas", "374 tractos + 210 semirremolques · Estado y mantención", 68),
        ("Conductores y Choferes", "454 conductores (196 propios + 258 externos) · Habilitaciones", 136),
        ("Transportistas Terceros", "148 empresas pymes subcontratadas · Contratos y tarifas", 204),
        ("Clientes y Puntos de Carga", "84 clientes corporativos · Geocercas de plantas y patios", 272),
    ]

    for tit, desc, y in maestros:
        f.grupo(16, y, 390, 56, tit, rx=4)
        f.texto(26, y + 26, desc, 9)
        f.texto(26, y + 40, "Fuente maestra: audIT DataHub · ID canónico global con sincronización ACL", 9, peso=600)

    # Conexiones verticales
    for y in [124, 192, 260]:
        f.linea([(211, y), (211, y + 12)])

    # Bloque inferior
    f.grupo(8, 340, 406, 120, "Capa Anticorrupción (ACL) y Gobierno de Datos", rx=5, relleno="#F8F9FA")
    f.texto(20, 368, "• Traducción bidireccional entre identificadores legados del ERP 2013 y UUIDv4.", 9)
    f.texto(20, 382, "• Validación de integridad referencial antes de permitir la entrada de cualquier dato maestro.", 9)
    f.texto(20, 396, "• Registro de linaje de datos (Data Lineage) auditable desde la ingesta hasta el reporte de BI.", 9)
    f.texto(20, 410, "• Notificación inmediata a supervisores ante discrepancias en padrones o vigencias.", 9)
    f.texto(20, 424, "• Catálogo activo disponible 24/7 para contrapartes técnicas en el Espacio Colaborativo.", 9, peso=600)

    return f.guardar()


def figura_5_1_erd():
    """Modelo conceptual y relacional de persistencia de datos."""
    f = Figura("audit-figura-5.1-erd", C5, "V", alto=540)

    f.grupo(8, 8, 406, 52, "Modelo conceptual y relacional de persistencia (PostgreSQL 16)", rx=5, peso=600)
    f.texto(16, 32, "Entidades centrales de dominio y relaciones con integridad referencial.", 9)
    f.texto(16, 44, "Diseñado bajo Domain-Driven Design (DDD) con esquemas normalizados y auditables.", 9, peso=600)

    # Entidades representadas como cajas con dimensiones y textos limpios
    entidades = [
        ("TRACTOCAMION", ["PK id_tracto (UUID)", "patente, marca, modelo", "odómetro, estado_op", "requiere_rampla (Bool)"], 16, 68, 122),
        ("SEMIRREMOLQUE", ["PK id_semirremolque", "patente, tipo_rampla", "capacidad_kg, refrig.", "id_baliza_ble (UUID)"], 146, 68, 130),
        ("CONDUCTOR", ["PK id_conductor (UUID)", "rut, nombre, contrato", "licencia, vigencia_lic", "estado_jornada (Enum)"], 284, 68, 130),

        ("VIAJE (Transacción Central)", ["PK id_viaje (UUID) · codigo_viaje (VJ-YYYYMM-XXXXXX)", "FK id_tracto, FK id_semirremolque, FK id_conductor", "FK id_cliente, origen_id, destino_id, peso_kg", "estado_viaje (Enum: 6 estados) · sellos UTC"], 16, 172, 390),

        ("DOCUMENTO_TRANSPORTE", ["PK id_documento (UUID)", "FK id_viaje, folio_sii", "hash_sha256, DET_xml", "estado_emision (Enum)"], 16, 270, 122),
        ("EVIDENCIA_JORNADA", ["PK id_evidencia (UUID)", "FK id_conductor, marca", "hash_actual, previo", "evidencia_rect_id"], 146, 270, 130),
        ("LIQUIDACION_FLETE", ["PK id_liquidacion (UUID)", "FK id_viaje, id_transp.", "costo_total, version", "id_operacion_erp"], 284, 270, 130),
    ]

    for tit, attrs, x, y, w in entidades:
        h = 28 + len(attrs) * 12
        f.grupo(x, y, w, h, tit, rx=4, tam=9, peso=600)
        for i, a in enumerate(attrs):
            f.texto(x + 6, y + 26 + i * 12, a, 9)

    # Líneas de relación entre tablas
    f.linea([(77, 138), (77, 172)])
    f.linea([(211, 138), (211, 172)])
    f.linea([(349, 138), (349, 172)])

    f.linea([(77, 240), (77, 270)])
    f.linea([(211, 240), (211, 270)])
    f.linea([(349, 240), (349, 270)])

    # Bloque inferior: Integridad
    f.grupo(8, 362, 406, 168, "Reglas de integridad y restricciones del modelo de datos", rx=5, relleno="#F8F9FA")
    f.marcador(26, 386, 1)
    f.texto(38, 388, "Integridad referencial estricta (ON DELETE RESTRICT en todas las claves foráneas).", 9)
    f.marcador(26, 408, 2)
    f.texto(38, 410, "La entidad VIAJE actúa como agregado raíz que coordina el despacho y cierre operacional.", 9)
    f.marcador(26, 430, 3)
    f.texto(38, 432, "EVIDENCIA_JORNADA y DOCUMENTO_TRANSPORTE implementan hash chains inmutables.", 9)
    f.marcador(26, 452, 4)
    f.texto(38, 454, "LIQUIDACION_FLETE almacena fórmulas y reglas versionadas para reproducibilidad forense.", 9)
    f.marcador(26, 474, 5)
    f.texto(38, 476, "Todas las claves primarias utilizan UUIDv4 para permitir generación descentralizada en cabina.", 9)
    f.marcador(26, 496, 6)
    f.texto(38, 498, "Las marcas de tiempo utilizan TIMESTAMPTZ con estandarización obligatoria a UTC.", 9, peso=600)

    return f.guardar()


FIGURAS = [
    figura_5_2_custodia,
    figura_5_3_permisos,
    figura_5_3_cap,
    figura_5_4_cdc,
    figura_5_5_migracion,
    figura_5_6_desempeno,
    figura_5_2_mdm,
    figura_5_1_erd,
]
