"""Convierte las fórmulas de las lecciones a MathML nativo y autónomo."""
from pathlib import Path
import json
import html
import re
import markdown
from formulario_fep import build as build_formulario

root = Path(__file__).parent
def row(*parts):
    return '<mrow>' + ''.join(parts) + '</mrow>'
def symbol(value):
    return '<mi>' + html.escape(value) + '</mi>'
def op(value):
    return '<mo>' + html.escape(value) + '</mo>'
def num(value):
    return '<mn>' + str(value) + '</mn>'
def power(base, exponent):
    return '<msup>' + base + exponent + '</msup>'
def frac(top, bottom):
    return '<mfrac>' + top + bottom + '</mfrac>'
def group(value):
    return row(op('('), value, op(')'))
def math(value, label):
    return '<math xmlns="http://www.w3.org/1998/Math/MathML" aria-label="' + html.escape(label, quote=True) + '">' + value + '</math>'
def difference(a, b):
    return row(symbol(a), op('−'), symbol(b))
def equation(a, b):
    return row(symbol(a), op('='), b)

i = symbol('i')
growth = group(row(num(1), op('+'), i))
compound = power(growth, symbol('n'))
annuity = frac(row(i, op('×'), compound), row(compound, op('−'), num(1)))
pending = difference('BAC', 'EV')
mapping = {}
def add(text, value):
    mapping[text] = math(value, text)

add('C = P × i(1+i)^n / [(1+i)^n−1]', equation('C', row(symbol('P'), op('×'), annuity)))
add('A = P × i × (1 + i)^n / [(1 + i)^n − 1]', equation('A', row(symbol('P'), op('×'), annuity)))
add('P = L(1+i)^g', equation('P', row(symbol('L'), op('×'), power(growth, symbol('g')))))
add('F = P × (1 + i)^n', equation('F', row(symbol('P'), op('×'), compound)))
add('P = F / (1 + i)^n', equation('P', frac(symbol('F'), compound)))
for index, denominator in [('SPI','PV'),('CPI','AC')]:
    add(index+' = EV / '+denominator, equation(index,frac(symbol('EV'),symbol(denominator))))
for numerator, denominator in [('BAC','CPI'),('EV','AC'),('EV','PV')]:
    add(numerator+' / '+denominator,frac(symbol(numerator),symbol(denominator)))
for denominator in ['CPI','CPI × SPI','BAC − AC','EAC − AC']:
    den = row(symbol('CPI'),op('×'),symbol('SPI')) if denominator=='CPI × SPI' else difference(*denominator.split(' − ')) if ' − ' in denominator else symbol(denominator)
    text='(BAC − EV) / '+ ('('+denominator+')' if ' ' in denominator else denominator)
    add(text,frac(pending,den))
add('EAC=AC+(BAC−EV)/(CPI×SPI)',equation('EAC',row(symbol('AC'),op('+'),frac(pending,row(symbol('CPI'),op('×'),symbol('SPI'))))))
for meta in ['BAC','EAC']:
    add('(BAC – EV) / ('+meta+' – AC)',frac(pending,difference(meta,'AC')))
add('VAN = −I₀ + Σ [Fₜ / (1 + r)^t]',equation('VAN',row(op('−'),'<msub><mi>I</mi><mn>0</mn></msub>',op('+'),'<munderover><mo>∑</mo><mrow><mi>t</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover>',frac('<msub><mi>F</mi><mi>t</mi></msub>',power(group(row(num(1),op('+'),symbol('r'))),symbol('t'))))))
add('(1 + tasa anual)^(1/12) − 1',row(power(group(row(num(1),op('+'),'<msub><mi>i</mi><mtext>anual</mtext></msub>')),frac(num(1),num(12))),op('−'),num(1)))
add('(optimista + 4 × más probable + pesimista) / 6',frac(row(symbol('O'),op('+'),num(4),op('×'),symbol('M'),op('+'),symbol('P')),num(6)))
add('(80 + 4 × 100 + 150) / 6',frac(row(num(80),op('+'),num(4),op('×'),num(100),op('+'),num(150)),num(6)))
add('(80 + 100 + 150) / 3',frac(row(num(80),op('+'),num(100),op('+'),num(150)),num(3)))

data=json.loads((root/'datos_practica_fep.json').read_text(encoding='utf-8'))
for label, expression in [
    ('SV = EV − PV', equation('SV',difference('EV','PV'))),
    ('CV = EV − AC', equation('CV',difference('EV','AC'))),
    ('EAC = AC + ETC', equation('EAC',row(symbol('AC'),op('+'),symbol('ETC')))),
    ('EAC = BAC / CPI', equation('EAC',frac(symbol('BAC'),symbol('CPI')))),
    ('AC + (BAC − EV)',row(symbol('AC'),op('+'),group(pending))),
    ('I = P × i × n',equation('I',row(symbol('P'),op('×'),i,op('×'),symbol('n')))),
]:
    add(label,expression)
add('−12.000 + 3.000/1,1 + 4.000/1,1² + 4.800/1,1³ + 7.800/1,1⁴',row(op('−'),num('12.000'),op('+'),frac(num('3.000'),num('1,1')),op('+'),frac(num('4.000'),power(num('1,1'),num(2))),op('+'),frac(num('4.800'),power(num('1,1'),num(3))),op('+'),frac(num('7.800'),power(num('1,1'),num(4)))))
count=0
add('FORMULA_VENTA',equation('FC',row(symbol('V'),op('−'),group(row(symbol('V'),op('−'),symbol('VL'))),op('×'),symbol('t'))))
add('FORMULA_ANUALIDAD',equation('VA',row(symbol('C'),op('×'),frac(row(compound,op('−'),num(1)),row(i,op('×'),compound)))))
add('FORMULA_EQUILIBRIO',equation('Q',frac(symbol('CF'),difference('p','cv'))))
pattern=re.compile('|'.join(re.escape(text) for text in sorted(mapping,key=len,reverse=True)))
for key,label in {
    'FORMULA_VENTA':'Flujo de venta igual a precio de venta menos la diferencia entre precio y valor libro multiplicada por tasa tributaria',
    'FORMULA_ANUALIDAD':'Valor actual igual a cuota por el factor de valor presente de una anualidad',
    'FORMULA_EQUILIBRIO':'Cantidad de equilibrio igual a costo fijo dividido por precio menos costo variable unitario',
}.items():
    mapping[key]=mapping[key].replace('aria-label="'+key+'"','aria-label="'+label+'"')
for lesson in data['lessons']:
    lesson['body'], matches = pattern.subn(lambda match: mapping[match.group(0)], lesson['body'])
    count += matches
template=(root/'plantilla_practica_fep.html').read_text(encoding='utf-8')
exercise_source=(root/'ejercicios_certamen3.md').read_text(encoding='utf-8')
exercise_sections=[]
exercise_index=[]
for section_number, section in enumerate(re.split(r'^## ',exercise_source,flags=re.M)[1:],1):
    title, content=section.split('\n',1)
    anchor=f'tipo-ejercicio-{section_number}'
    exercise_index.append(f'<li><a href="#{anchor}">{html.escape(title)}</a></li>')
    cards=[]
    examples=re.split(r'^### ',content,flags=re.M)[1:]
    assert len(examples)==2, title
    for example in examples:
        heading, content=example.split('\n',1)
        prompt, answer=content.split('\n@@\n',1)
        prompt_html=markdown.markdown(prompt.strip())
        answer_html=markdown.markdown(answer.strip())
        answer_html=pattern.sub(lambda match: mapping[match.group(0)],answer_html)
        cards.append(f'<div class="card"><h4>{html.escape(heading)}</h4>{prompt_html}<details><summary>Ver desarrollo</summary><div class="feedback">{answer_html}</div></details></div>')
    exercise_sections.append(f'<section aria-labelledby="{anchor}"><h3 id="{anchor}">{html.escape(title)}</h3>{"".join(cards)}</section>')
page=template.replace('__DATA__',json.dumps(data,ensure_ascii=False).replace('</','<\\/'))
page=page.replace('__EXERCISE_INDEX__',''.join(exercise_index)).replace('__EXERCISES__',''.join(exercise_sections))
page=page.replace('__FORMULARIO__',build_formulario())
(root/'PRACTICA_CERTAMEN_3_FEP.html').write_text(page,encoding='utf-8')
print(f'{count} fórmulas convertidas a MathML.')
