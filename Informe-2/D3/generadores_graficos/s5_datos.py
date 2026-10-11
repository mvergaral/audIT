"""Datos de D3: modelos relacionales, custodia, decisiones y flujos.
Los diccionarios exhaustivos van en el anexo Markdown de S5.
"""
from comun import Figura,titulo,nota,proceso,entidad,relacion,SUBRED,GRIS_CLARO

def figura_5_1_erd():
    f=Figura('audit-figura-5.1-erd'); titulo(f,'Modelo lógico: operación del viaje')
    # PK y FK son referencias lógicas entre contextos; no bases compartidas.
    for args in [
        (14,42,154,'CLIENTE',['PK id_cliente']),
        (206,42,154,'ORDEN_TRANSPORTE',['PK id_orden','FK id_cliente']),
        (398,42,140,'TRACTOCAMION',['PK id_tracto']),
        (574,42,140,'SEMIRREMOLQUE',['PK id_semirremolque']),
        (14,186,154,'TRANSPORTISTA',['PK id_transportista']),
        (206,186,154,'VIAJE',['PK id_viaje','FK id_orden','estado_viaje']),
        (398,186,140,'ASIGNACION',['PK id_asignacion','FK viaje / recursos','desde / hasta / estado']),
        (574,186,140,'CONDUCTOR',['PK id_conductor','FK transportista?']),
        (14,335,154,'LIQUIDACION',['PK id_liquidacion','FK id_transportista']),
        (206,335,154,'DOCUMENTO_TRANSP.',['PK id_documento','FK id_viaje','folio / emisor / hash']),
        (398,335,140,'EVAL_ASIGNACION',['PK id_evaluacion','FK id_asignacion','regla / veredicto']),
        (574,335,140,'COSTO_VERSION',['PK id_costo','FK id_viaje','version / faltantes'])]: entidad(f,*args)
    relacion(f,[(168,65),(206,65)])
    relacion(f,[(283,94),(283,186)])
    relacion(f,[(468,82),(468,186)])
    relacion(f,[(644,82),(644,147),(503,147),(503,186)],padre='0..1')
    relacion(f,[(360,229),(398,229)])
    relacion(f,[(574,217),(538,217)])
    relacion(f,[(91,226),(91,335)])
    relacion(f,[(283,250),(283,335)])
    relacion(f,[(468,250),(468,335)])
    relacion(f,[(350,250),(350,290),(644,290),(644,335)])
    # Maestro del empleador/propietario: relación opcional del conductor.
    relacion(f,[(91,186),(91,163),(644,163),(644,186)],padre='0..1')
    f.texto(14,453,'1, 0..1 y 0..*: multiplicidades por extremo. PK: identificador; FK: referencia lógica; ?: nullable.',9)
    return f.guardar()

def figura_5_7_evidencia():
    f=Figura('5-7-evidencia'); titulo(f,'Modelo lógico: evidencia y evaluación de asignación')
    entidad(f,14,48,200,'EVIDENCIA_JORNADA',['PK id_evidencia','fuente / estado / nivel?','conductor? / hora?','hash / original / rectifica?'])
    entidad(f,264,48,200,'EVALUACION_EVIDENCIA',['PK (evaluacion, evidencia)','FK id_evaluacion','FK id_evidencia','uso: jornada / reposo / atestación'])
    entidad(f,514,48,200,'EVALUACION_ASIGNACION',['PK id_evaluacion','FK id_asignacion','modalidad / veredicto','regla / causa / fecha'])
    relacion(f,[(214,96),(264,96)])
    relacion(f,[(514,96),(464,96)])
    entidad(f,14,255,200,'DOCUMENTO_RESPALDO',['PK id_documento','hash / origen / recibido_utc','URI inmutable / retención'])
    entidad(f,264,255,200,'EXCEPCION_RN04',['PK id_excepcion','FK id_evaluacion','dos aprobadores / motivo','un viaje / revisión mensual'])
    entidad(f,514,255,200,'PERMISO_COMPARTIR',['PK id_permiso','transportista / recurso / destino','finalidad / versión / vigencia','revocación / respaldo'])
    relacion(f,[(114,255),(114,124)],padre='0..1')
    relacion(f,[(614,124),(614,208),(364,208),(364,255)],hijo='0..1')
    nota(f,399,['Una evaluación usa cero o varias evidencias. Reposo y atestación pueden coexistir sin perder su origen.',
                'Sin fuente no se inventa una evidencia. Nivel 0 es voluntario; NULL expresa ausencia o invalidez.',
                'El permiso de compartir datos y la modalidad de adhesión no sustituyen una base legal de tratamiento.'])
    return f.guardar()

def figura_5_2_mdm():
    f=Figura('audit-figura-5.2-mdm'); titulo(f,'Datos maestros: propietario único y conciliación')
    f.grupo(14,46,200,324,'Fuentes',rx=6)
    proceso(f,114,96,'flu-contable',['Contable','Identidad comercial'])
    proceso(f,114,202,'flu-documento',['Documentos y contratos','Flota / personas'])
    proceso(f,114,308,'flu-gestion2013',['Gestión 2013','Fuente durante transición'])
    proceso(f,300,126,'pr-adaptador',['Capa anticorrupción','Esquemas y claves'])
    proceso(f,300,290,'pr-reconciliador',['Validar y conciliar','Pendientes en cuarentena'])
    for y in [96,202,308]: f.linea([(127,y),(232,y),(232,126),(286,126)])
    f.linea([(300,170),(300,276)])
    f.grupo(392,46,322,324,'Registro maestro único',rx=6)
    f.ficha(553,103,['Conductores y habilitaciones','Personas y cumplimiento'],w=282)
    f.ficha(553,163,['Tractos, semirremolques y taller','Flota y activos'],w=282)
    f.ficha(553,223,['Órdenes y puntos de servicio','Planificación y tráfico'],w=282)
    f.ficha(553,283,['Razón social y datos de facturación','Sistema contable; referencia en audIT'],w=282)
    f.linea([(314,290),(378,290)],flecha=None)
    f.linea([(378,103),(378,290)],flecha=None)
    for y in [103,163,223,283]: f.linea([(378,y),(412,y)])
    nota(f,396,['Cada atributo tiene un propietario; los demás contextos consumen referencias y eventos versionados.',
                'La validación de RUT y patente es sintáctica; la acreditación documental resuelve identidad y discrepancias.',
                'Los cambios se auditan y se concilian con el contable sin escrituras directas sobre sus tablas.'])
    return f.guardar()

def figura_5_2_custodia():
    f=Figura('5-2-custodia'); titulo(f,'Evidencia de jornada: recepción y cadena de custodia')
    fuentes=[('1 · Tacógrafo','flu-documento'),('2 · Equipo identificado','pr-g26i'),('3 · Fábrica','flu-fabrica'),('4 · Reposo','flu-espera'),('5 · Atestación','flu-sello'),('0 · Voluntario','rol-conductor')]
    for i,(n,ic) in enumerate(fuentes):
        x=65+i*120; proceso(f,x,68,ic,n,s=22)
        f.linea([(x,101),(x,134)],flecha=None)
    f.linea([(65,134),(665,134)],flecha=None)
    f.linea([(184,134),(184,190)])
    proceso(f,184,205,'pr-reconciliador',['Validar fuente','Identidad e integridad'])
    proceso(f,365,205,'flu-bitacora',['Sellar y encadenar','Original + hash + versión'])
    proceso(f,546,205,'az-storage',['Custodia inmutable','Retención por dominio'])
    f.linea([(198,205),(351,205)]); f.linea([(379,205),(532,205)])
    f.rotulo(274,198,'Válida')
    f.linea([(184,258),(184,309)])
    f.ficha(184,333,['Sin fuente / desconocida / inválida','Nivel NULL · no elevar a 0'],w=280)
    f.linea([(546,258),(546,309)])
    f.ficha(546,333,['Rectificación como registro nuevo','Vínculo al original; no sobrescribir'],w=280)
    nota(f,400,['El nivel de evidencia no es el código de fuente ni el resultado del despacho. Nivel 0 nunca habilita.',
                'El hash detecta cambios; firma, originales, sellos, acceso restringido y WORM sostienen la custodia.',
                'Ante una impugnación se exportan original, mapeo de nivel, regla aplicada, aprobadores y veredicto.'])
    return f.guardar()

def figura_5_3_permisos():
    f=Figura('5-3-permisos'); titulo(f,'Permiso de compartir datos y ciclo de conservación')
    for x,ic,n,d in [(78,'rol-transportista',['Otorgar permiso'],['Finalidad y destinatario']),
                       (300,'flu-candado',['Evaluar acceso'],['Viaje + alcance + versión']),
                       (548,'rol-cliente',['Mostrar lo autorizado'],['Auditar qué, a quién y cuándo'])]:
        proceso(f,x,90,ic,n,d)
    f.linea([(92,90),(286,90)]); f.linea([(314,90),(534,90)])
    f.rotulo(198,84,'Permiso vigente')
    f.rotulo(424,84,'Acceso aprobado')
    f.linea([(300,149),(300,162)])
    f.ficha(300,177,['Sin permiso vigente: denegar'],w=218)
    proceso(f,78,246,'flu-reintento',['Revocar permiso'],['Versionar y cesar accesos'])
    f.linea([(78,150),(78,232)])
    f.linea([(92,246),(286,246)])
    f.caja(286,214,168,66,['¿Retención obligatoria','o litigio vigente?'],tam=10)
    f.linea([(454,232),(534,232)])
    f.ficha(616,232,['Sí: conservar protegido','Excluir usos no autorizados'],w=162)
    f.rotulo(491,225,'Sí')
    f.linea([(370,280),(370,324)])
    f.ficha(370,340,['No: supresión verificable','Copias, réplicas y claves'],w=220)
    f.rotulo(390,303,'No')
    nota(f,399,['Revocar la compartición no elimina anticipadamente evidencia con deber de conservación.',
                'El dato fuera del servicio no se expone al cliente; controles en API, caché, portal y dispositivo.',
                'Brazil South: activar datos personales sólo con mecanismo jurídico documentado y DR comprobado.'])
    return f.guardar()

def figura_5_3_cap():
    f=Figura('audit-figura-5.3-cap'); titulo(f,'Decisiones ante una partición de red')
    f.grupo(14,48,332,340,'Operación crítica: priorizar consistencia',rx=6)
    proceso(f,180,98,'az-postgres',['PostgreSQL transaccional'],['Asignación, vigencias y documentos'])
    f.ficha(180,177,['Sólo confirmar tras commit','Reserva única + evidencia vigente'],w=290)
    f.linea([(180,146),(180,164)])
    f.ficha(180,265,['Sin acceso a estado autoritativo','Bloquear nueva asignación'],w=290)
    f.linea([(180,150),(24,150),(24,265),(35,265)])
    f.grupo(370,48,344,340,'Captura local: continuar y reconciliar',rx=6)
    proceso(f,542,98,'pr-g26i',['SQLite local ACID'],['Eventos de jornada y operación'])
    f.ficha(542,177,['Guardar sin enlace','Outbox persistente a bordo'],w=300)
    f.linea([(542,146),(542,164)])
    f.ficha(542,265,['Al volver: deduplicar y conciliar','Event Hubs → TimescaleDB'],w=300)
    f.linea([(542,191),(542,252)])
    f.texto(542,335,'El destino puede quedar atrasado; no inventar actualidad.',9,anc='middle')
    nota(f,401,['CAP describe un sistema distribuido bajo partición; ACID describe transacciones del motor.',
                'TimescaleDB es PostgreSQL: no se clasifica como AP sólo por recibir eventos asíncronos.',
                'Redis es caché; no es la autoridad para habilitar un despacho con datos vencidos o incompletos.'])
    return f.guardar()

def figura_5_4_cdc():
    f=Figura('audit-figura-5.4-cdc'); titulo(f,'Segregación transaccional y analítica')
    f.grupo(14,50,176,296,'Operación',rx=6)
    proceso(f,102,99,'az-postgres',['PostgreSQL OLTP'],['Datos de negocio'])
    proceso(f,102,247,'si-timescale',['TimescaleDB separado'],['Series de tiempo'])
    proceso(f,276,99,'flu-bitacora',['CDC Debezium'],['WAL / slots vigilados'])
    proceso(f,438,99,'az-eventhubs',['Event Hubs Premium'],['Protocolo Kafka'])
    proceso(f,615,99,'az-datalake',['ADLS Gen2 / Delta'],['Datos crudos y depurados'])
    f.linea([(116,99),(262,99)]); f.linea([(290,99),(424,99)]); f.linea([(452,99),(601,99)])
    f.linea([(116,247),(210,247),(210,191),(615,191),(615,149)])
    f.rotulo(438,185,'Telemetría y lotes de combustible / peaje')
    proceso(f,438,279,'flu-tablero',['Modelo dimensional'],['Costo por viaje versionado'])
    proceso(f,615,279,'flu-gerencia',['BI y autoservicio'],['Consulta, filtros y exportación'])
    f.linea([(615,149),(615,215),(438,215),(438,265)])
    f.linea([(452,279),(601,279)])
    nota(f,399,['Las consultas de BI se ejecutan en el repositorio analítico; no sobre tablas OLTP ni su réplica operacional.',
                'CDC consume recursos: medir retraso, retención de WAL y efecto sobre el despacho; no asumir carga nula.',
                'Costo v1 ≤ 24 h con faltantes visibles; nuevas versiones al conciliar fuentes tardías, sin borrar v1.'])
    return f.guardar()

def figura_5_5_migracion():
    f=Figura('audit-figura-5.5-migracion'); titulo(f,'Migración: saneamiento, acreditación y conciliación')
    xs=[86,270,454,638]
    fases=[('1. Extraer','flu-documento',['Inventario y copia','Perfilado de fuentes']),
           ('2. Homologar','pr-transformador',['Claves y catálogos','Duplicados / niveles']),
           ('3. Acreditar','flu-sello',['Vigencias una a una','Original y hash']),
           ('4. Ensayar / cortar','pr-reconciliador',['Conciliar y firmar acta','Delta final y reversa'])]
    for x,(n,ic,ls) in zip(xs,fases):
        f.grupo(x-72,52,144,158,n,rx=6)
        proceso(f,x,104,ic,ls,s=28)
    for a,b in zip(xs,xs[1:]): f.linea([(a+72,125),(b-72,125)])
    f.ficha(362,272,['Registro inválido o sin respaldo → cuarentena','No habilita despacho; corrección trazada al origen'],w=440)
    for x in xs[1:3]: f.linea([(x,210),(x,246),(362,246),(362,258)])
    f.linea([(638,210),(638,333),(582,333)])
    f.ficha(362,333,['Go / no go: totales, documentos y pruebas aceptados','Retorno al legado preservando lo ya emitido'],w=440)
    nota(f,400,['Migrar todos los maestros; viajes 5 años; liquidaciones 6 años; todos los siniestros y ≈ 6.000 vigencias.',
                '480.000 viajes y 10.656 liquidaciones son estimaciones: confirmar contra las fuentes históricas.',
                'Cortes por función en M16 y M21. Intervenciones por unidad y terminal; respetar congelamientos de S7.'])
    return f.guardar()

def figura_5_6_desempeno():
    f=Figura('audit-figura-5.6-desempeno'); titulo(f,'Desempeño: validar actualidad antes de confirmar')
    proceso(f,92,94,'pr-servicio',['Petición de despacho'],['30 s máximo'])
    proceso(f,290,94,'az-redis',['Caché versionada'],['Identidad y vigencia'])
    proceso(f,562,94,'az-postgres',['Estado autoritativo'],['Validar versión + reservar'])
    f.linea([(106,94),(276,94)]); f.linea([(304,94),(548,94)])
    f.rotulo(427,87,'Sin actualidad: consultar fuente')
    f.grupo(14,223,214,138,'Consultas puntuales',rx=6)
    proceso(f,121,268,'az-postgres',['B-tree: claves y FK'],['Unicidad y rangos de asignación'])
    f.grupo(256,223,214,138,'Datos geoespaciales',rx=6)
    proceso(f,363,268,'flu-ubicacion',['GiST: geocercas'],['Validar geometría y umbrales'])
    f.grupo(498,223,216,138,'Series y análisis',rx=6)
    proceso(f,606,268,'si-timescale',['Partición temporal'],['BRIN si hay orden físico'])
    nota(f,399,['Un índice acelera una consulta; no acredita por sí solo latencia ni cobertura del caso.',
                'Probar 380 usuarios (hipótesis), 570 en estrés y 300 reconexiones; registrar percentiles y máximos.',
                'Viaje permanece relacional sin partición inicial; el histórico voluminoso se particiona tras medir.'])
    return f.guardar()

FIGURAS=[figura_5_1_erd,figura_5_2_mdm,figura_5_2_custodia,figura_5_3_permisos,
         figura_5_3_cap,figura_5_4_cdc,figura_5_5_migracion,figura_5_6_desempeno,figura_5_7_evidencia]
