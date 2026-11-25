from pathlib import Path
from html.parser import HTMLParser
import urllib.request,json
class Links(HTMLParser):
    def __init__(self):super().__init__();self.links=[]
    def handle_starttag(self,tag,attrs):
        for k,v in attrs:
            if k in ('href','src'):self.links.append(v)
u='https://carlosabarza.github.io/PaginaAudIT/'
try:
    with urllib.request.urlopen(u,timeout=25) as r:
        body=r.read().decode('utf-8');status=r.status
    parser=Links();parser.feed(body)
    result={'url':u,'status':status,'links':parser.links,'bytes':len(body),'alcance':'Disponibilidad y enlaces HTML; no acredita WCAG, navegación completa ni permanencia futura.'}
except Exception as e:result={'url':u,'error':str(e)}
out=Path(__file__).resolve().parent/'evidencia/sitio-web.json'
out.write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(result,ensure_ascii=False))
