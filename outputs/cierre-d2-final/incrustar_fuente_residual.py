"""Incrusta la fuente residual de ReportLab sin cambiar texto ni representación."""
from pathlib import Path
import hashlib,json,fitz,shutil
OUT=Path(__file__).resolve().parent
records=[]
for p in (OUT/'documentos').glob('AUDIT-Subdocumento7.pdf'):
    d=fitz.open(p)
    old=sorted({f[0] for page in d for f in page.get_fonts(full=True) if f[3]=='Helvetica'})
    if not old:d.close();continue
    affected=[i for i,page in enumerate(d) if any(f[0] in old for f in page.get_fonts(full=True))]
    # El recurso procede del estado inicial del canvas: ningún texto visible usa Helvetica.
    for i in affected:
        names={s['font'] for b in d[i].get_text('dict')['blocks'] for l in b.get('lines',[]) for s in l['spans']}
        assert 'Helvetica' not in names,(p.name,i)
    before={i:hashlib.sha256(d[i].get_pixmap(matrix=fitz.Matrix(1,1)).samples).hexdigest() for i in affected}
    texts=[page.get_text() for page in d]
    new=d[0].insert_font(fontname='D2FuenteBaseIncrustada',fontbuffer=fitz.Font('helv').buffer,set_simple=True)
    description=d.xref_object(new)
    for xref in old:d.update_object(xref,description)
    temp=p.with_suffix('.incrustado.pdf');d.save(temp,garbage=4,deflate=True);d.close()
    with fitz.open(temp) as check:
        assert texts==[page.get_text() for page in check]
        assert all(before[i]==hashlib.sha256(check[i].get_pixmap(matrix=fitz.Matrix(1,1)).samples).hexdigest() for i in affected)
    backup=OUT/'evidencia'/('antes-incrustacion-'+p.name)
    if not backup.exists():shutil.copy2(p,backup)
    temp.replace(p)
    records.append(dict(archivo=p.name,recursos_incrustados=len(old),paginas_verificadas=[i+1 for i in affected],texto_identico=True,pixeles_identicos_72dpi=True))
(OUT/'evidencia/incrustacion-fuente-residual.json').write_text(json.dumps(records,ensure_ascii=False,indent=2),encoding='utf-8')
print(records)
