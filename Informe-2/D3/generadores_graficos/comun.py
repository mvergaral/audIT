"""Figuras de D3 con el lienzo, fuentes e iconos originales de D4.
La salida PNG y SVG queda exclusivamente en D3/graficos.
"""
from pathlib import Path
import sys
import subprocess
BASE_DIR = Path(__file__).resolve().parents[3]
D4_FUENTE = BASE_DIR / 'Informe-2/D4/graficos-v2/fuente'
sys.path.insert(0, str(D4_FUENTE))
from lienzo import Figura as FiguraD4, ancho, LINEA, BORDE, SUBRED, GRIS_CLARO, REVISION
SALIDA_D3_GRAFICOS = BASE_DIR / 'Informe-2/D3/graficos'

class Figura(FiguraD4):
    def __init__(self, nombre, tipo='H', alto=None):
        super().__init__(nombre, '', tipo, alto)
    def guardar(self):
        SALIDA_D3_GRAFICOS.mkdir(parents=True, exist_ok=True)
        base = SALIDA_D3_GRAFICOS / self.nombre
        svg = Path(str(base) + '.svg')
        svg.write_text(self.svg(), encoding='utf-8')
        subprocess.run([
            'rsvg-convert', '-f', 'png', '--dpi-x', '300', '--dpi-y', '300',
            '-b', 'white', '-o', str(base) + '.png', str(svg),
        ], check=True)
        REVISION[self.nombre] = self.revisar()
        return str(base)

def titulo(f, texto, detalle=None):
    f.texto(14,18,texto,11,600)
    if detalle: f.texto(14,32,detalle,9)

def actor(f,x,nombre,w=124):
    f.caja(x-w/2,37,w,38,nombre if isinstance(nombre,list) else [nombre],tam=9)
    f.linea([(x,75),(x,399)],disc=True,flecha=None,grosor=0.6,saltos=False)

def mensaje(f,xs,origen,destino,y,texto,retorno=False):
    a,b=xs[origen],xs[destino]
    f.linea([(a,y),(b,y)],disc=retorno,saltos=False)
    f.rotulo((a+b)/2,y-5,texto,tam=9)

def nota(f,y,lineas):
    f.grupo(14,y,f.W-28,22+13*len(lineas),None,rx=6,relleno=SUBRED)
    for i,s in enumerate(lineas): f.texto(24,y+18+i*13,s,9)

def proceso(f,x,y,icono,nombre,dato=None,s=28):
    return f.nodo(icono,x,y,s,nombre,dato)

def entidad(f,x,y,w,nombre,atributos):
    h=28+12*len(atributos)
    f.rect(x,y,w,h,rx=5)
    f.texto(x+8,y+15,nombre,9,600)
    f.linea([(x,y+22),(x+w,y+22)],flecha=None,grosor=0.6,saltos=False)
    for i,s in enumerate(atributos): f.texto(x+8,y+36+i*12,s,9)
    return x,y,w,h

def relacion(f,pts,padre='1',hijo='0..*'):
    """Relación sin flecha: multiplicidad en cada extremo, no flujo de datos."""
    f.linea(pts,flecha=None,grosor=0.8)
    x0,y0=pts[0]; x1,y1=pts[-1]
    dx0,dy0=pts[1][0]-x0,pts[1][1]-y0
    dx1,dy1=x1-pts[-2][0],y1-pts[-2][1]
    if dx0:
        f.rotulo(x0+(6 if dx0>0 else -6),y0-5,padre,anc='start' if dx0>0 else 'end')
    else:
        f.rotulo(x0+8,y0+(12 if dy0>0 else -5),padre,anc='start')
    if dx1:
        f.rotulo(x1+(-6 if dx1>0 else 6),y1-5,hijo,anc='end' if dx1>0 else 'start')
    else:
        f.rotulo(x1+8,y1+(-5 if dy1>0 else 12),hijo,anc='start')
