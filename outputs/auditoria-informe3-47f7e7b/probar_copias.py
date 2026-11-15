"""Prepara copias desechables para recalcular con LibreOffice; conserva los originales."""
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
import xml.etree.ElementTree as E

BASE=Path(__file__).resolve().parents[2]
ORIGEN=BASE/'outputs/informe3-integral/entrega-consolidada/activacion-simulada/Modelo-activacion-simulada.xlsx'
TEMP=Path('/tmp/audit-informe3-native')
NS={'s':'http://schemas.openxmlformats.org/spreadsheetml/2006/main',
    'r':'http://schemas.openxmlformats.org/officeDocument/2006/relationships'}
def copia(nombre, cambios):
    entrada=TEMP/'entrada';entrada.mkdir(parents=True,exist_ok=True)
    with ZipFile(ORIGEN) as z:
        relaciones={n.attrib['Id']:n.attrib['Target'].lstrip('/') for n in E.fromstring(z.read('xl/_rels/workbook.xml.rels'))}
        hojas={n.attrib['name']:relaciones[n.attrib['{'+NS['r']+'}id']] for n in E.fromstring(z.read('xl/workbook.xml')).find('s:sheets',NS)}
        modificadas={}
        for hoja,celda,valor in cambios:
            ruta=hojas[hoja];ruta=ruta if ruta.startswith('xl/') else 'xl/'+ruta
            arbol=modificadas.get(ruta,E.fromstring(z.read(ruta)))
            nodo=arbol.find('.//s:c[@r="'+celda+'"]',NS)
            assert nodo is not None and nodo.find('s:f',NS) is None
            nodo.find('s:v',NS).text=str(valor)
            modificadas[ruta]=arbol
        with ZipFile(entrada/nombre,'w',ZIP_DEFLATED) as w:
            for n in z.namelist():
                w.writestr(n,E.tostring(modificadas[n],encoding='utf-8',xml_declaration=True) if n in modificadas else z.read(n))
copia('base.xlsx',[])
copia('capital-mas-10m.xlsx',[('Parámetros D2','B4',284452748)])
copia('evento-menos-1m.xlsx',[('Caja activacion montaje','F3',265251504)])
print(TEMP)
