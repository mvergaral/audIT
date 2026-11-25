#!/usr/bin/env python3
"""Figuras vectoriales verticales de S5/S6; contenido procedente de los modelos originales."""
from pathlib import Path
import math
from io import BytesIO
from pypdf import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor

RAIZ = Path(__file__).resolve().parents[2]
pdfmetrics.registerFont(TTFont('AudSans', '/usr/share/fonts/noto/NotoSans-Regular.ttf'))
pdfmetrics.registerFont(TTFont('AudBold', '/usr/share/fonts/noto/NotoSans-Bold.ttf'))
W=500
def legible(s):
    return s.replace('≥', '>=').replace('≤', '<=').replace('→', '->')

class Figura:
    def __init__(self, n, name, title, h=680):
        self.h=h; self.bottom=0; self.path=RAIZ/'figuras'/n/'vertical'/(name+'.pdf')
        self.path.parent.mkdir(parents=True,exist_ok=True)
        self.c=canvas.Canvas(str(self.path),pagesize=(W,h));self.c.setTitle(title)
        self.c.setAuthor('audIT');self.c.setFillColor(HexColor('#17354c'))
        self.text(15,21,title,12,True)
    def text(self,x,y,s,size=11,bold=False):
        self.c.setFillColor(HexColor('#17354c'));self.c.setFont('AudBold' if bold else 'AudSans',size)
        self.c.drawString(x,self.h-y,legible(s));self.bottom=max(self.bottom,y+size*.3)
    def lines(self,s,width=450,size=11,bold=False):
        s=legible(s)
        font='AudBold' if bold else 'AudSans';result=[]
        for para in s.split('\n'):
            line=''
            for word in para.split():
                if pdfmetrics.stringWidth((line+' '+word).strip(),font,size)>width:
                    result.append(line);line=word
                else:line=(line+' '+word).strip()
            result.append(line)
        return result
    def box(self,x,y,w,title,lines,h=None):
        body=[]
        for s in lines:body+=self.lines(s,w-18)
        heading=self.lines(title,w-18,bold=True)
        height=h or 15+14*(len(heading)+len(body))+9
        assert y+height<self.h-5,(self.path.name,y,height,self.h)
        self.c.setStrokeColor(HexColor('#536f82'));self.c.setFillColor(HexColor('#f6f9fc'))
        self.c.roundRect(x,self.h-y-height,w,height,5,fill=1,stroke=1)
        yy=y+17
        for s in heading:self.text(x+9,yy,s,11,True);yy+=14
        for s in body:self.text(x+9,yy,s);yy+=14
        self.bottom=max(self.bottom,y+height)
        return height
    def line(self,pts,arrow=True,label=None):
        self.c.setStrokeColor(HexColor('#536f82'));self.c.setLineWidth(.9)
        p=self.c.beginPath();p.moveTo(pts[0][0],self.h-pts[0][1])
        for x,y in pts[1:]:p.lineTo(x,self.h-y)
        self.c.drawPath(p);self.bottom=max(self.bottom,max(y for x,y in pts))
        if arrow:
            x,y=pts[-1];px,py=pts[-2];a=math.atan2(y-py,x-px)
            for da in [-.45,.45]:
                self.c.line(x,self.h-y,x-6*math.cos(a+da),self.h-(y-6*math.sin(a+da)))
        if label:
            x,y,s=label;self.text(x,y,s)
    def note(self,y,items):return self.box(15,y,470,'Controles y lectura del diagrama',items)
    def save(self):
        self.c.showPage();self.c.save()
        reader=PdfReader(BytesIO(self.path.read_bytes()));page=reader.pages[0]
        page.mediabox.lower_left=(0,max(0,self.h-self.bottom-15))
        page.cropbox=page.mediabox
        writer=PdfWriter();writer.add_page(page)
        writer.add_metadata({'/Title':reader.metadata.title or self.path.stem,'/Author':'audIT'})
        with self.path.open('wb') as stream:writer.write(stream)
        return self.path

def flow(name,title,steps,notes,n='05-datos'):
    f=Figura(n,name,title)
    y=45
    for i,(t,ls) in enumerate(steps):
        h=f.box(35,y,430,t,ls)
        if i<len(steps)-1:f.line([(250,y+h),(250,y+h+18)])
        y+=h+22
    h=f.note(y+3,notes)
    assert y+3+h<f.h-10,(name,y+h)
    return f.save()

def erd():
    f=Figura('05-datos','audit-figura-5.1-erd','Modelo lógico: operación del viaje')
    entities=[('CLIENTE',['PK id_cliente']),('TRANSPORTISTA',['PK id_transportista']),
      ('ORDEN_TRANSPORTE',['PK id_orden','FK id_cliente']),('CONDUCTOR',['PK id_conductor','FK transportista?']),
      ('VIAJE',['PK id_viaje','FK id_orden','estado_viaje']),('TRACTOCAMION',['PK id_tracto']),
      ('ASIGNACION',['PK id_asignacion','FK viaje / recursos','desde / hasta / estado']),('SEMIRREMOLQUE',['PK id_semirremolque']),
      ('DOCUMENTO_TRANSP.',['PK id_documento','FK id_viaje','folio / emisor / hash']),('EVAL_ASIGNACION',['PK id_evaluacion','FK id_asignacion','regla / veredicto']),
      ('COSTO_VERSION',['PK id_costo','FK id_viaje','version / faltantes']),('LIQUIDACION',['PK id_liquidacion','FK id_transportista'])]
    # Conexiones antes de cajas; trazados por carriles exteriores y espacio entre columnas.
    for row in [0,1,2]:f.line([(120,48+row*83+72),(120,48+(row+1)*83)],label=(128,48+row*83+81,'1 : 0..*'))
    f.line([(380,120),(380,131)],label=(388,127,'0..1 : 0..*'))
    f.line([(15,242),(5,242),(5,408),(15,408)],False)
    f.line([(15,242),(9,242),(9,491),(15,491)],False)
    for y in [159,242,325]:f.line([(275,y),(252,y),(252,325),(225,325)],False)
    f.line([(225,325),(245,325),(245,408),(275,408)],False)
    f.line([(485,76),(495,76),(495,491),(485,491)],False)
    for i,(title,attrs) in enumerate(entities):
        x=15 if i%2==0 else 275;y=48+(i//2)*83
        f.box(x,y,210,title,attrs,h=72)
    f.note(554,['1 : 0..* en las relaciones; propietario del conductor 0..1.',
                'Semirremolque por asignación: 0..1; conductor y tracto: 1.',
                'Viaje → documentos / costos; asignación → evaluaciones.',
                'Transportista → liquidaciones y conductores.',
                'PK: identificador. FK: referencia lógica; ?: nullable.'])
    return f.save()

def evidencia():
    return flow('5-7-evidencia','Modelo lógico: evidencia, evaluación y permiso',[
      ('EVIDENCIA_JORNADA',['PK id_evidencia; fuente / estado / nivel?','conductor? / hora?; hash / original / rectifica?']),
      ('EVALUACION_EVIDENCIA',['PK (evaluacion, evidencia); FK id_evaluacion y FK id_evidencia','Uso: jornada / reposo / atestación; relación de varias evidencias por evaluación.']),
      ('EVALUACION_ASIGNACION',['PK id_evaluacion; FK id_asignacion','modalidad / veredicto; regla / causa / fecha']),
      ('Respaldos, excepción y permisos separados',['DOCUMENTO_RESPALDO: original, URI inmutable y retención; evidencia 0..1 respaldo.','EXCEPCION_RN04: 0..1 por evaluación, dos aprobadores, motivo y un viaje.','PERMISO_COMPARTIR: transportista, recurso, destino, finalidad, versión, vigencia y revocación.'])],
      ['Reposo y atestación pueden coexistir. Sin fuente no se inventa una evidencia.',
       'Nivel 0 voluntario; NULL expresa ausencia o invalidez. Adhesión y permiso no sustituyen base legal.'])

def cap():
    return flow('audit-figura-5.3-cap','Decisiones ante una partición de red',[
      ('Operación crítica: priorizar consistencia',['PostgreSQL transaccional: asignación, vigencias y documentos.','Confirmar solo tras commit: reserva única y evidencia vigente.','Sin estado autoritativo: bloquear nueva asignación.']),
      ('Captura local: continuar y reconciliar',['SQLite local ACID: jornada y eventos operacionales.','Sin enlace: guardar en outbox persistente a bordo.','Al volver: deduplicar y conciliar mediante Event Hubs y TimescaleDB.'])],
      ['CAP se refiere a particiones de red; ACID, a transacciones del motor.',
       'TimescaleDB es PostgreSQL; la recepción asíncrona no lo convierte por sí sola en AP.',
       'Redis es caché; no acredita actualidad ni habilita un despacho con evidencia incompleta.'])

def calendario():
    return flow('6-1-hitos','Gestión híbrida e hitos contractuales',[
      ('Etapa 1',['Desarrollo M1–M12; marcha blanca M13–M15.','Producción desde M16, con continuidad de la operación.']),
      ('Etapa 2',['Desarrollo M13–M18; marcha blanca M19–M20.','Producción desde M21. Operación M21–M56.']),
      ('Gobernanza y frentes simultáneos',['PMBOK: línea base, riesgos y cambios. Scrum: incrementos cada dos semanas.','M13–M15: marcha blanca E1 + desarrollo E2.','M19–M20: producción E1 + marcha blanca E2.','Kanban: incidencias y estabilización; no altera hitos obligatorios.'])],
      ['SA-01: M1 = febrero 2027; M16 = mayo 2028; M21 = octubre 2028; M56 = septiembre 2031.',
       'Cuatro comités y reunión semanal; aceptación y reversión trazadas a S9. El detalle mensual corresponde a S7.'],n='06-metodologias')

def pipeline():
    f=Figura('06-metodologias','6-2-pipeline','DevSecOps: seis puertas antes de producción')
    steps=[('1. Pruebas',['.NET / Go / Flutter','Lógica ≥70 %; ramas ≥80 %']),('2. Análisis estático',['SAST + SonarQube','Calidad y secretos']),
      ('3. Contenedores',['Trivy + SCA','CVE críticas / altas = 0']),('4. Procedencia',['SBOM + firma','Builder aislado']),
      ('5. Infraestructura',['Terraform y escaneo','Plan revisado']),('6. Dinámico',['ZAP + pruebas ASVS','QA / PREPROD'])]
    for i,(t,ls) in enumerate(steps):
        row=i//2;col=i%2;x=20+col*260;y=48+row*116
        f.box(x,y,200,t,ls,h=80)
    for row in range(3):f.line([(220,88+row*116),(280,88+row*116)])
    for row in range(2):f.line([(480,88+row*116),(491,88+row*116),(491,149+row*116),(9,149+row*116),(9,204+row*116),(20,204+row*116)])
    f.box(35,417,430,'Promover el mismo digest a PROD',['Aprobación independiente; verificar firma, SBOM y procedencia.'])
    f.line([(380,360),(380,407)])
    f.note(500,['GitLab CI orquesta; cada rechazo detiene la promoción.',
      'SLSA Build L3: aislamiento y material de firma inaccesible al código del proyecto.',
      'Reversa: versión previa compatible, eventos conservados y conciliación; no deshacer evidencia emitida.'])
    return f.save()

if __name__=='__main__':
    paths=[erd(),evidencia(),cap(),calendario(),pipeline()]
    specs=[
      ('audit-figura-5.2-mdm','Datos maestros: propietario único y conciliación',[
        ('Fuentes autorizadas',['Contable: identidad comercial. Documentos y contratos: flota y personas.','Gestión 2013: fuente durante la transición.']),
        ('Capa anticorrupción y conciliación',['Homologar esquemas y claves. Validar identidad y respaldos.','Duplicados y discrepancias: cuarentena y resolución del propietario.']),
        ('Registro maestro único por atributo',['Personas y cumplimiento: conductores y habilitaciones.','Flota y activos: tractos, semirremolques y taller.','Planificación y tráfico: órdenes y puntos de servicio.','Sistema contable: razón social y facturación; referencia en audIT.'])],
        ['Los demás contextos consumen referencias y eventos versionados.',
         'RUT y patente: validación sintáctica y acreditación documental. Cambios auditados; sin escritura directa en el contable.']),
      ('5-2-custodia','Evidencia de jornada: cadena de custodia',[
        ('Fuentes de evidencia',['1 Tacógrafo; 2 equipo identificado; 3 fábrica.','4 reposo; 5 atestación; 0 registro voluntario.']),
        ('Validar fuente, identidad e integridad',['Sin fuente / desconocida / inválida: nivel NULL; no elevar a 0.','Fuente válida: conservar original, hash, versión y vínculo al evento.']),
        ('Sellar, encadenar y conservar',['Custodia inmutable y retención por dominio.','Rectificación como registro nuevo vinculado al original; no sobrescribir.'])],
        ['El nivel no es el código de fuente ni el veredicto del despacho; nivel 0 no habilita.',
         'Hash, firma, originales, sellos, acceso restringido y WORM sostienen la custodia.',
         'Impugnación: exportar original, nivel, regla, aprobadores y veredicto.']),
      ('5-3-permisos','Compartición autorizada y conservación',[
        ('Otorgar permiso',['Transportista: finalidad, destinatario, viaje, alcance, vigencia y versión.']),
        ('Evaluar cada acceso y auditar',['Con permiso vigente: mostrar lo autorizado; registrar qué, a quién y cuándo.','Sin permiso vigente: denegar. Controles en API, caché, portal y dispositivo.']),
        ('Revocar y decidir conservación',['Versionar revocación y cesar accesos cubiertos por el permiso.','Con retención obligatoria o litigio: conservar protegido, sin usos no autorizados.','Sin obligación: supresión verificable de copias, réplicas y claves.'])],
        ['La revocación no elimina anticipadamente evidencia con deber de conservación.',
         'Brazil South: datos personales solo con mecanismo jurídico documentado y DR comprobado.']),
      ('audit-figura-5.4-cdc','Segregación transaccional y analítica',[
        ('Origen operacional',['PostgreSQL OLTP: datos de negocio. TimescaleDB separado: series de tiempo.']),
        ('Captura y transporte',['CDC Debezium: WAL / slots vigilados. Event Hubs Premium: protocolo Kafka.','Telemetría y lotes de combustible / peaje alimentan el repositorio analítico.']),
        ('Repositorio y explotación',['ADLS Gen2 / Delta: datos crudos y depurados.','Modelo dimensional: costo por viaje versionado. BI y autoservicio: consulta y exportación.'])],
        ['BI consulta el repositorio analítico, no OLTP ni su réplica operacional.',
         'Medir retraso, retención de WAL y efecto en despacho; CDC no tiene carga nula.',
         'Costo v1 ≤24 h con faltantes visibles; posteriores versiones sin borrar v1.']),
      ('audit-figura-5.5-migracion','Migración: saneamiento y conciliación',[
        ('1. Extraer',['Inventario, copia y perfilado de fuentes.']),('2. Homologar',['Claves, catálogos, duplicados y niveles.']),
        ('3. Acreditar',['Vigencias una a una; original y hash. Inválidos o sin respaldo: cuarentena.']),
        ('4. Ensayar y cortar',['Conciliar, firmar acta y cargar delta final. Go/no go con totales y pruebas aceptados.','Retorno al legado preservando lo emitido; corregir con trazabilidad al origen.'])],
        ['Maestros; viajes 5 años; liquidaciones 6 años; siniestros y ≈6.000 vigencias.',
         '480.000 viajes y 10.656 liquidaciones son estimaciones a contrastar.',
         'Cortes M16/M21; intervención por unidad y terminal; congelamientos de S7.']),
      ('audit-figura-5.6-desempeno','Desempeño: actualidad antes de confirmar',[
        ('Petición de despacho: máximo 30 s',['Caché versionada: identidad y vigencia. Sin actualidad: consultar la fuente.','Estado autoritativo: validar versión y reservar; no habilitar con datos vencidos.']),
        ('Índices y cargas separados',['B-tree: claves, FK, unicidad y rangos de asignación.','GiST: geocercas, geometrías y umbrales.','Partición temporal; BRIN cuando el orden físico lo justifique.'])],
        ['Un índice no acredita por sí solo latencia ni cobertura del caso.',
         'Ensayar 380 usuarios (hipótesis), 570 en estrés y 300 reconexiones; percentiles y máximos.',
         'Viaje inicialmente sin partición; histórico voluminoso se particiona tras medir.'])]
    for spec in specs:paths.append(flow(*spec))
    print('Generadas',len(paths),'figuras vectoriales verticales; texto mínimo 11 puntos a tamaño natural.')
