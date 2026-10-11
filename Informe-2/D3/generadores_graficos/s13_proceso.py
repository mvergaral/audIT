"""Ficha T-19 de D3: proceso diferencial de programación de intervenciones."""
from comun import Figura,titulo,nota,proceso

def figura_13_2_proceso():
    f=Figura('13-2-intervenciones')
    titulo(f,'Proceso propuesto: programar intervenciones por oportunidad de patio')
    xs=[122,365,608]
    pasos=[
        (122,65,'1. Observar','flu-ubicacion',['ETA y paso por terminal','Permiso y actualidad']),
        (365,65,'2. Preparar','flu-documento',['Familia de equipo / kit','Versión y pruebas previas']),
        (608,65,'3. Programar','pr-servicio',['Ventana, técnico y stock','Prioridad + plan manual']),
        (122,249,'4. Autorizar','flu-candado',['Vehículo detenido en terminal','Ventana y kit confirmados']),
        (365,249,'5. Intervenir','pr-g26i',['Configurar / instalar','Validar antes de liberar']),
        (608,249,'6. Aprender','pr-reconciliador',['Acta y tiempos reales','Recalibrar el próximo plan'])]
    for x,y,t,ic,ls in pasos:
        f.grupo(x-105,y,210,122,t,rx=6)
        proceso(f,x,y+48,ic,ls,s=28)
    for y in [126,310]:
        f.linea([(227,y),(260,y)]); f.linea([(470,y),(503,y)])
    f.linea([(608,187),(608,216),(122,216),(122,249)])
    f.rotulo(365,211,'Plan factible → confirmar ventana; si no existe, reprogramar')
    nota(f,405,['La instalación por unidad en terminal es obligatoria; el aporte es la planificación dinámica verificable.',
                'Piloto: 10 unidades en M6; flota propia M6–9. Metas y línea base se miden; no se inventan resultados.',
                'El twin conserva estado deseado/reportado. Eventos y actas guardan el historial de cada intervención.'])
    return f.guardar()

FIGURAS=[figura_13_2_proceso]
