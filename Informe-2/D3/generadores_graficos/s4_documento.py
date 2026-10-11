"""Los dos caminos de emisión de D4 con entrega completa antes de salir."""
from comun import Figura,titulo,nota,proceso,SUBRED

def documento_sin_cobertura():
    f=Figura('documento-sin-cobertura')
    titulo(f,'Documento sin cobertura: dos caminos, un único emisor')
    f.grupo(14,44,701,130,'Datos conocidos antes de entrar en la zona sin señal',rx=6)
    for x,ic,n,d in [(86,'flu-documento','Orden completa',None),(292,'flu-contable','Sistema contable','Emite y firma'),(522,'pr-g26i','Cabina','Documento y representación')]: proceso(f,x,99,ic,n,d)
    f.linea([(100,99),(278,99)]); f.linea([(306,99),(508,99)])
    f.rotulo(407,92,'Descarga y acuse verificados')
    f.grupo(14,186,701,199,'Datos definitivos conocidos en el punto sin señal',rx=6)
    for x,ic,n,d in [(86,'pr-g26i',['Carga definitiva'],['Solicitud identificada']),
                      (292,'flu-satelite',['Iridium SBD'],['Tramas y correlación']),
                      (522,'flu-contable',['ACL → contable'],['Único emisor; firma original'])]: proceso(f,x,242,ic,n,d)
    f.linea([(100,242),(278,242)]); f.linea([(306,242),(508,242)])
    f.linea([(522,300),(522,345),(86,345),(86,303)])
    f.rotulo(304,343,'Entrega íntegra por fragmentos + verificación + acuse')
    nota(f,400,['El folio o el hash solos no sustituyen el documento ni su representación portable conforme.',
                'SBD 9603: hasta 340 bytes de subida y 270 de bajada por mensaje; medir tamaño y tiempo total.',
                'Emisión ≤ 90 s y documento disponible antes de salir. Si falta confirmación conforme: bloquear salida.'])
    return f.guardar()
FIGURAS=[documento_sin_cobertura]
