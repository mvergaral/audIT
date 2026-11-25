from pathlib import Path
import pymupdf,json,re
from PIL import Image,ImageOps,ImageDraw
O=Path(__file__).resolve().parent
p=O/'fuentes/salida/administrativo/AUDIT-Sobre1-Antecedentes-Administrativos.pdf'
doc=pymupdf.open(p);results=[];selected=[]
for i,page in enumerate(doc,1):
    text=page.get_text()
    footer=[w[4] for w in page.get_text('words') if w[0]>page.rect.width*.7 and w[1]>page.rect.height*.88 and re.fullmatch(r'\d+',w[4])]
    spans=[s for b in page.get_text('dict')['blocks'] if 'lines'in b for l in b['lines'] for s in l['spans'] if s['text'].strip()]
    results.append({'pagina':i,'folios':footer,'min_fuente':min(s['size'] for s in spans),'referencias_rotas':'??' in text,
                    'pendientes':[x.strip()[:230] for x in text.splitlines() if re.search('pendiente|por incorporar|por acreditar',x,re.I)],
                    'emisor_real_prohibido':bool(re.search(r'Bureau Veritas|Nexia',text)),
                    'sobre2_en_pie':any('Sobre N.º 2' in s['text'] for s in spans if s['bbox'][1]>page.rect.height*.88)})
    if i<=6 or any(x in text for x in ['ISO 9001','Resumen de estados financieros','Garantía de Seriedad','Carta de referencia','Certificado simulado de calidad']):
        dest=O/'revision'/f'admin-{i:02d}.png';page.get_pixmap(matrix=pymupdf.Matrix(1.25,1.25)).save(dest)
        selected.append(str(dest))
thumbs=[]
for i,page in enumerate(doc,1):
    pix=page.get_pixmap(matrix=pymupdf.Matrix(.40,.40),alpha=False)
    im=Image.frombytes('RGB',[pix.width,pix.height],pix.samples)
    tile=Image.new('RGB',(260,345),'#eeeeee');im.thumbnail((250,320));tile.paste(im,((260-im.width)//2,10))
    ImageDraw.Draw(tile).text((8,330),f'Folio {i}',fill='black');thumbs.append(tile)
sheet=Image.new('RGB',(260*5,345*((len(thumbs)+4)//5)),'white')
for i,t in enumerate(thumbs):sheet.paste(t,((i%5)*260,(i//5)*345))
sheet.save(O/'revision/contacto-administrativo.jpg')
summary={'paginas':len(doc),'folios_correctos':all(str(r['pagina']) in r['folios'] for r in results),
         'referencias_rotas':sum(r['referencias_rotas'] for r in results),
         'emisores_prohibidos':sum(r['emisor_real_prohibido'] for r in results),
         'pies_sobre2':sum(r['sobre2_en_pie'] for r in results),'paginas_detalle':results,'renders':selected}
(O/'evidencia/auditoria-administrativo.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in summary.items() if k not in ('paginas_detalle','renders')},ensure_ascii=False))
print('Páginas con pendientes:',[(r['pagina'],r['pendientes']) for r in results if r['pendientes']])
