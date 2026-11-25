"""Agrega desagregación aprobada en OOXML conservando las fórmulas originales."""
from pathlib import Path
import zipfile,xml.etree.ElementTree as E,json,copy
import openpyxl

OUT=Path(__file__).resolve().parent;ROOT=OUT.parents[1]
BASE=ROOT/'recursos/Formato-Oferta-audIT'
source=ROOT/'outputs/cierre-entrega-final/trabajo/Sobre3/MODELO_CONCILIADO_PARA_REVISION.xlsx'
target=OUT/'documentos/AUDIT_ModeloFinanciero_3_20261125.xlsx'
proposal=json.loads((OUT/'evidencia/propuesta-tarifas.json').read_text(encoding='utf-8'))
proposal['estado']='Aceptado por el usuario: incorporar desagregación sin cambiar precios ni facturación.'
(OUT/'evidencia/tarifas-aceptadas.json').write_text(json.dumps(proposal,ensure_ascii=False,indent=2),encoding='utf-8')
NS='http://schemas.openxmlformats.org/spreadsheetml/2006/main';R='http://schemas.openxmlformats.org/officeDocument/2006/relationships';PKG='http://schemas.openxmlformats.org/package/2006/relationships';CT='http://schemas.openxmlformats.org/package/2006/content-types'
q=lambda s:'{'+NS+'}'+s

def cell(row,ref,value,formula=None,style=None):
    attrs={'r':ref}
    if style is not None:attrs['s']=str(style)
    c=E.SubElement(row,q('c'),attrs)
    if formula is not None:
        if isinstance(value,str):c.set('t','str')
        E.SubElement(c,q('f')).text=formula;E.SubElement(c,q('v')).text=str(value)
    elif isinstance(value,(int,float)):E.SubElement(c,q('v')).text=format(value,'.16g')
    else:
        c.set('t','inlineStr');E.SubElement(E.SubElement(c,q('is')),q('t')).text=str(value)

def sheet(headers,rows,numericstyle,inputstyle):
    s=E.Element(q('worksheet'));v=E.SubElement(E.SubElement(s,q('sheetViews')),q('sheetView'),{'workbookViewId':'0'})
    E.SubElement(v,q('pane'),{'ySplit':'1','topLeftCell':'A2','activePane':'bottomLeft','state':'frozen'})
    cols=E.SubElement(s,q('cols'))
    for i,width in enumerate([20,32,32,17,17,19,23,23,17,17,17,17,15],1):E.SubElement(cols,q('col'),{'min':str(i),'max':str(i),'width':str(width),'customWidth':'1'})
    sd=E.SubElement(s,q('sheetData'));r=E.SubElement(sd,q('row'),{'r':'1'})
    for i,h in enumerate(headers,1):cell(r,openpyxl.utils.get_column_letter(i)+'1',h)
    for idx,values in enumerate(rows,2):
        r=E.SubElement(sd,q('row'),{'r':str(idx)})
        for j,val in enumerate(values,1):
            coord=openpyxl.utils.get_column_letter(j)+str(idx)
            if isinstance(val,tuple):cell(r,coord,val[0],val[1],numericstyle)
            else:cell(r,coord,val,style=inputstyle if j==6 and isinstance(val,(int,float)) else numericstyle if isinstance(val,(int,float)) else None)
    E.SubElement(s,q('sheetProtection'),{'sheet':'1','objects':'1','scenarios':'1','selectLockedCells':'0','selectUnlockedCells':'0'})
    E.SubElement(s,q('autoFilter'),{'ref':f'A1:{openpyxl.utils.get_column_letter(len(headers))}{len(rows)+1}'})
    if len(headers)==13:
        dvs=E.SubElement(s,q('dataValidations'),{'count':str(len(rows))})
        for idx in range(2,len(rows)+2):
            dv=E.SubElement(dvs,q('dataValidation'),{'type':'decimal','operator':'between','allowBlank':'0','showErrorMessage':'1','errorTitle':'Fuera de rango','error':'La tarifa debe respetar el rango E-26 declarado.','sqref':f'F{idx}'})
            E.SubElement(dv,q('formula1')).text=f'K{idx}';E.SubElement(dv,q('formula2')).text=f'L{idx}'
    return E.tostring(s,encoding='utf-8',xml_declaration=True)

with zipfile.ZipFile(source) as zin:
    wb=E.fromstring(zin.read('xl/workbook.xml'));rels=E.fromstring(zin.read('xl/_rels/workbook.xml.rels'));ct=E.fromstring(zin.read('[Content_Types].xml'));styles=E.fromstring(zin.read('xl/styles.xml'))
    formats=styles.find(q('numFmts'))
    if formats is None:formats=E.Element(q('numFmts'),{'count':'0'});styles.insert(0,formats)
    fmtid=max([163]+[int(n.attrib['numFmtId']) for n in formats])+1;E.SubElement(formats,q('numFmt'),{'numFmtId':str(fmtid),'formatCode':'0.00000000'});formats.set('count',str(len(formats)))
    xfs=styles.find(q('cellXfs'));styleids=[]
    for locked in [True,False]:
        xf=copy.deepcopy(xfs[0]);xf.set('numFmtId',str(fmtid));xf.set('applyNumberFormat','1');xf.set('applyProtection','1')
        pr=xf.find(q('protection'))
        if pr is None:pr=E.SubElement(xf,q('protection'))
        pr.set('locked','1' if locked else '0');styleids.append(len(xfs));xfs.append(xf)
    xfs.set('count',str(len(xfs)))
    headers=['Fase','Perfil','Referencia E26','Horas','Costo UF/h','Tarifa UF/h','Costo CLP','Venta personal CLP','Costo mínimo UF/h','Costo máximo UF/h','Tarifa mínima UF/h','Tarifa máxima UF/h','Control rango']
    rows=[]
    for idx,r in enumerate(proposal['perfiles'],2):
        rows.append([r['fase'],r['perfil'],r['referencia'],r['horas'],r['costo_uf'],r['tarifa_uf'],
            (r['horas']*r['costo_uf']*40000,f"D{idx}*E{idx}*'Parámetros D2'!$B$21"),
            (r['ingreso_clp'],f"D{idx}*F{idx}*'Parámetros D2'!$B$21"),*r['rango_costo'],*r['rango_tarifa'],
            ('Cumple',f'IF(AND(E{idx}>=I{idx},E{idx}<=J{idx},F{idx}>=K{idx},F{idx}<=L{idx}),"Cumple","Revisar")')])
    conditions=[['Fecha oferta','2026-11-25'],['Vigencia comercial días',150],['Reajuste operación','Sin reajuste; precio nominal fijo'],['Fuente de decisión','Decisión comercial de oferta registrada: 150 días y sin reajuste'],['Base presupuestaria','Planilla 3.2; precios y flujos originales preservados'],['Tarifas','Desagregación de precio cerrado; no facturación adicional por hora'],['UF convencional CLP',40000],['USD convencional CLP',900],['Revisión humana y A6','D2, Analista de Planificación y Calidad; revisión humana y firma A-6 pendientes'],['Referencias de roles','Rangos de comparación para roles adicionales; no acreditan títulos'],['Montaje','10 pilotos M6 y 172 externos M7-M9; total182 montados M9'],['Financiación','Presupuesto condicionado; no acredita contratos bancarios']]
    parts={}
    sheets=wb.find(q('sheets'));nextid=max(int(s.attrib['sheetId']) for s in sheets)+1
    ridnum=max(int(r.attrib['Id'][3:]) for r in rels if r.attrib['Id'].startswith('rId'))+1
    for name,blob in [('Tarifas E26 Final',sheet(headers,rows,*styleids)),('Condiciones oferta',sheet(['Condición','Valor o alcance'],conditions,*styleids))]:
        while f'xl/worksheets/sheet{nextid}.xml' in zin.namelist():nextid+=1
        file=f'xl/worksheets/sheet{nextid}.xml';rid=f'rId{ridnum}'
        E.SubElement(sheets,q('sheet'),{'name':name,'sheetId':str(nextid),'{'+R+'}id':rid})
        E.SubElement(rels,'{'+PKG+'}Relationship',{'Id':rid,'Type':R+'/worksheet','Target':f'worksheets/sheet{nextid}.xml'})
        E.SubElement(ct,'{'+CT+'}Override',{'PartName':'/'+file,'ContentType':'application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml'})
        parts[file]=blob;nextid+=1;ridnum+=1
    for path,tree in [('xl/workbook.xml',wb),('xl/_rels/workbook.xml.rels',rels),('[Content_Types].xml',ct),('xl/styles.xml',styles)]:parts[path]=E.tostring(tree,encoding='utf-8',xml_declaration=True)
    with zipfile.ZipFile(target,'w',zipfile.ZIP_DEFLATED) as zout:
        for info in zin.infolist():zout.writestr(info,parts.pop(info.filename,zin.read(info.filename)))
        for path,blob in parts.items():zout.writestr(path,blob)

rows=[]
for r in proposal['perfiles']:
    dec=lambda n:f'{n:.8f}'.replace('.',',')
    rows.append(' & '.join([r['fase'],r['perfil'],r['referencia'],dec(r['costo_uf']),dec(r['tarifa_uf'])])+r' \\')
tex=r'\begin{tabla}[ancho=completo,fuente=condensada]{Costos y tarifas por fase en UF por hora}{eco-tarifas-final}{L{23mm} L{30mm} X R{24mm} R{24mm}}'+'\n'+r'Fase & Perfil & Referencia E-26 & Costo & Tarifa \\ \midrule'+'\n'+'\n'.join(rows)+'\n'+r'\end{tabla}'+'\n'
for base in [BASE,OUT/'fuentes']:
    (base/'economico/datos/tarifas-final.tex').write_text(tex,encoding='utf-8')
# No se cambia el CSV genérico protegido por su semántica de un perfil/una tarifa:
# el corte final utiliza dos tarifas por fase en una tabla y hoja explícitas.
print(target.name,'hojas añadidas',2,'tarifas',len(rows))
