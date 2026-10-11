"""Calendario contractual y flujo DevSecOps de seis puertas de calidad."""
from comun import Figura,titulo,nota,SUBRED,GRIS_CLARO

def figura_6_1_hitos():
    f=Figura('6-1-hitos')
    titulo(f,'Gestión híbrida e hitos contractuales','FEP01 · Artículo 17.1 · p.12. El detalle de actividades corresponde a S7.')
    x0=150; paso=19; fin=x0+24*paso
    def borde(m): return x0+(m-1)*paso
    for m in [1,6,12,13,16,19,21,24]:
        x=borde(m)
        # Guías sólo en las separaciones; no atraviesan barras ni rótulos.
        for ya,yb in [(62,80),(110,146),(176,212),(242,264),(288,292)]:
            f.linea([(x,ya),(x,yb)],flecha=None,disc=True,grosor=0.4,saltos=False)
        f.texto(x,53,f'M{m}',9,anc='middle')
    f.texto(666,53,'M25–56',9,anc='middle')
    def barra(y,a,b,etiqueta,gris=False):
        x=borde(a); w=(b-a+1)*paso
        f.rect(x,y,w,30,relleno=GRIS_CLARO if gris else '#FFFFFF',rx=3)
        f.texto(x+w/2,y+19,etiqueta,9,anc='middle')
    f.texto(14,99,'Etapa 1',10,600)
    barra(80,1,12,'Desarrollo M1–12'); barra(80,13,15,'Blanca',True); barra(80,16,24,'Producción desde M16')
    f.rect(fin+12,80,90,30,rx=3); f.texto(fin+57,99,'Continúa',9,anc='middle')
    f.texto(14,165,'Etapa 2',10,600)
    barra(146,13,18,'Desarrollo M13–18'); barra(146,19,20,'Blanca',True); barra(146,21,24,'Prod. M21')
    f.rect(fin+12,146,90,30,rx=3); f.texto(fin+57,165,'Continúa',9,anc='middle')
    f.texto(14,231,'Soporte',10,600); barra(212,21,24,'Operación')
    f.rect(fin+12,212,90,30,relleno=GRIS_CLARO,rx=3); f.texto(fin+57,231,'Hasta M56',9,anc='middle')
    f.ficha(211,279,'PMBOK: línea base, riesgos y cambios')
    f.ficha(506,279,'Scrum: incrementos cada 2 semanas')
    f.grupo(14,316,701,76,'Frentes simultáneos',rx=6)
    f.texto(26,346,'M13–15: marcha blanca E1 + desarrollo E2. M19–20: producción E1 + marcha blanca E2.',9)
    f.texto(26,372,'Kanban: incidencias y estabilización. Ningún cambio altera los hitos obligatorios.',9)
    nota(f,408,['SA-01 de S3/S7: M1 = febrero 2027; M16 = mayo 2028; M21 = octubre 2028; M56 = septiembre 2031.',
                'Cuatro comités y una reunión semanal gobiernan decisiones; aceptación y reversión se trazan a S9.'])
    return f.guardar()

def figura_6_2_pipeline():
    f=Figura('6-2-pipeline')
    titulo(f,'DevSecOps: seis puertas antes de producción','GitLab CI orquesta pruebas y herramientas especializadas; cada rechazo detiene la promoción.')
    fases=[('1. Pruebas','dev-dotnet',['.NET / Go / Flutter','Lógica ≥ 70 %','Ramas ≥ 80 %']),
           ('2. Estático','fui-codigo',['SAST + SonarQube','Calidad y secretos']),
           ('3. Contenedores','pr-pod',['Trivy + SCA','CVE críticas/altas = 0']),
           ('4. Procedencia','flu-sello',['SBOM + firma','Builder aislado']),
           ('5. Infraestructura','az-aks',['Terraform / escaneo','Plan revisado']),
           ('6. Dinámico','flu-candado',['ZAP + pruebas ASVS','QA / PREPROD'])]
    centros=[126,364,602]
    for i,(nom,ic,ls) in enumerate(fases):
        fila,col=divmod(i,3); x=centros[col]; y=74+fila*154
        f.grupo(x-102,y-20,204,110,nom,rx=6); f.icono(ic,x,y+15,26)
        for j,s in enumerate(ls): f.texto(x,y+45+j*12,s,9,anc='middle')
    for a,b,y in [(228,262,109),(466,500,109),(228,262,263),(466,500,263)]: f.linea([(a,y),(b,y)])
    f.linea([(704,109),(714,109),(714,207),(14,207),(14,263),(24,263)])
    f.rotulo(364,207,'La plataforma firma la procedencia; los pasos del proyecto no acceden a la clave')
    f.linea([(602,318),(602,352),(378,352)])
    f.ficha(256,352,'Promover el mismo digest a PROD',w=242)
    f.texto(14,391,'Aprobación independiente + verificación de firma, SBOM y procedencia antes de la admisión.',9)
    nota(f,409,['SLSA Build L3: aislamiento entre ejecuciones y material de firma inaccesible al código del proyecto.',
                'Reversa: versión previa compatible, eventos conservados y reconciliación; no deshacer evidencia emitida.'])
    return f.guardar()

FIGURAS=[figura_6_1_hitos,figura_6_2_pipeline]
