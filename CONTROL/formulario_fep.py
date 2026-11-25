"""Formulario autónomo con notación MathML."""
from html import escape

TIPS = {
    'PV y EV por actividad': ('PV = previsto, EV = ejecutado, AC = cuánto costó.', 'Si una tarea de 100 UF lleva 40 % real, aporta 40 UF de EV. Si debiera llevar 60 %, aporta 60 de PV. El símbolo ∑ pide sumar esos aportes para todas las tareas.'),
    'Variación de costo': ('Costo compara trabajo conseguido con dinero gastado.', 'EV=100 y AC=120 da CV=−20. Hacer ese trabajo costó 20 UF más que su presupuesto.'),
    'Variación de cronograma': ('Cronograma compara ejecutado con previsto.', 'EV=100 y PV=120 da SV=−20. Debías producir 20 UF más de trabajo al corte. Para expresar la demora en días necesitas datos del cronograma.'),
    'Índice de costo': ('CPI responde cuánto trabajo consigo por cada UF.', 'CPI=0,80 significa obtener 0,80 UF de trabajo presupuestado por cada UF gastada. El punto de referencia es 1.'),
    'Índice de cronograma': ('SPI responde cuánto hice de lo que debía llevar hoy.', 'SPI=0,80 significa completar el 80 % del trabajo previsto a la fecha. Para el avance del proyecto completo, divide EV por BAC.'),
    'Relación general del pronóstico': ('Gastado + faltante = total final.', 'AC mira el gasto hasta hoy, ETC lo que esperas gastar desde hoy y EAC el total de ambos. Si ya gastaste 300 y faltan 500, terminarás en 800.'),
    'Resto al costo presupuestado': ('Si fue algo puntual, al resto le aplico el plan original.', 'Busca frases como “costos atípicos” o “el resto costará lo estimado”. BAC−EV quita del presupuesto el trabajo ya ganado y deja el trabajo pendiente a precios del plan.'),
    'Continúa la eficiencia de costo': ('Si seguimos igual de eficientes, el CPI ajusta el total.', 'Busca “se mantendrá el desempeño actual”. Con BAC=1.000 y CPI=0,80, el pronóstico sube a 1.250. Una eficiencia inferior a uno exige más gasto para completar el mismo trabajo.'),
    'Influyen costo y cronograma': ('Si influyen los dos, multiplico los dos índices.', 'Busca que el enunciado diga que costo y plazo afectarán el trabajo restante. Divide el trabajo pendiente por CPI×SPI y después suma lo gastado.'),
    'Nueva estimación detallada': ('Si recalcularon lo que falta, uso ese nuevo dato.', 'Si el equipo vuelve a presupuestar las tareas pendientes en 600 y AC=400, EAC=1.000. ETC nuevo corresponde al futuro.'),
    'TCPI para terminar con BAC': ('Trabajo que falta dividido por dinero que queda del presupuesto original.', 'Busca “el patrocinador exige el presupuesto original”. Aunque el EAC pronostique otro total, aquí la meta es BAC. Si faltan 600 de trabajo y quedan 500 UF, TCPI=1,20.'),
    'TCPI para terminar con EAC': ('La meta revisada cambia el dinero disponible.', 'Busca “terminar según el pronóstico revisado”. Arriba sigue BAC−EV. Abajo cambia a EAC−AC. Si la meta deja cero fondos o fondos negativos y todavía queda trabajo, revisa su viabilidad antes de interpretar el cociente.'),
    'Variación prevista al cierre': ('Lo aprobado menos lo que espero gastar.', 'BAC=1.000 y EAC=1.250 da VAC=−250. Anticipas necesitar 250 UF adicionales.'),
    'PERT y promedio triangular': ('PERT da cuatro votos al más probable.', 'Los pesos 1, 4 y 1 suman seis. El promedio triangular da un voto a cada escenario y divide por tres. El método solicitado determina cuál usar.'),
    'Markup y margen sobre ventas': ('Pregunta “¿porcentaje sobre qué?” y coloca esa base abajo.', 'Costo 100 y venta 120 dejan utilidad 20. Sobre costo es 20 % de markup. Sobre venta es 16,67 % de margen.'),
    'Evaluación ponderada de proveedores': ('Cada nota aporta según cuánto importa el criterio.', 'Una nota 80 con peso 60 % aporta 48 puntos. Convierte 60 % a 0,60 y suma todos los aportes.'),
    'Flujo del periodo y saldo': ('Flujo es el movimiento del mes; saldo es lo acumulado.', 'Cobras 100 y pagas 150: FC=−50. Si tenías 200, terminas con 150. Para capital inicial busca el saldo más negativo antes de aportar fondos.'),
    'Depreciación y valor libro': ('Reparto el desgaste por año y resto el desgaste acumulado.', 'Una compra de 1.000 con residual cero y vida de cinco años deprecia 200/año. Después de dos depreciaciones, VL=600.'),
    'Caja operativa después de impuestos': ('Depreciación baja la utilidad, reduce impuesto y vuelve al flujo.', 'Si D=100 y t=20 %, su escudo tributario es 20. El factor 1−t representa la fracción que queda después del impuesto. Esta expresión abreviada supone que aprovechas la deducción.'),
    'Venta de un activo neta de impuesto': ('Primero compara venta con libros, luego calcula impuesto.', 'V=800, VL=600 y t=25 %: ganancia 200, impuesto 50 y venta neta 750. Si hay pérdida, verifica cuándo puedes aprovechar el ahorro tributario.'),
    'Flujo incremental': ('¿Qué cambia por hacer el proyecto?', 'Si sin proyecto pagas 500 y con proyecto 350, la mejora bruta de caja es 150. Evalúa también impuestos y otras diferencias entre escenarios.'),
    'Valor futuro y presente': ('Hacia adelante multiplico; hacia hoy divido.', 'A 10 %, 100 hoy equivalen a 110 en un año. Traer esos 110 a hoy exige dividir por 1,10. El exponente cuenta cuántos periodos recorres.'),
    'Equivalencia de tasas efectivas': ('Lee primero si la tasa es efectiva o nominal.', 'Una efectiva anual debe convertirse por equivalencia compuesta. Si el préstamo dice expresamente “12 % nominal anual dividido por 12”, usa 1 % mensual.'),
    'Saldo tras gracia y cuota fija': ('Primero crece la deuda durante la gracia; luego se reparte en cuotas.', 'g cuenta los meses sin pagos y n las cuotas posteriores. Con 1.000 al 1 % y dos meses de gracia, P=1.020,10. Para intereses totales resta siempre las 1.000 originales de la suma de cuotas.'),
    'Valor presente de pagos iguales': ('Si todos los pagos son iguales, puedo resumir la serie.', 'La fórmula reúne en un solo valor los pagos C de cada periodo. Si el primer pago es al final del año 1, el resultado queda en año 0.'),
    'Valor actual neto': ('Traigo cada flujo a hoy y recupero la inversión inicial.', 'VAN=+50 significa 50 de valor adicional en dinero de hoy después de cubrir el rendimiento exigido. En la sumatoria, t indica el año de cada flujo y n el último año.'),
    'Relación beneficio/costo': ('Cuánto beneficio presente obtengo por cada unidad de costo presente.', 'B/C=1,20 significa 1,20 de beneficios actualizados por cada 1 de costos actualizados. Para comparar riqueza entre proyectos de distinta escala, revisa además el VAN.'),
    'Equilibrio en unidades': ('Cada venta ayuda a cubrir una parte del costo fijo.', 'Precio 30 y variable 20 dejan 10 por unidad. Para cubrir 1.000 de fijos necesitas vender 100 unidades.'),
    'Valor económico agregado básico': ('Al resultado le cobro el uso del capital.', 'Capital 1.000 al 10 % exige 100. Si el resultado operativo después de impuestos es 130, VEA=30.'),
}

def m(text):
    return '<mi>'+escape(text)+'</mi>'
def n(text):
    return '<mn>'+str(text)+'</mn>'
def o(text):
    return '<mo>'+escape(text)+'</mo>'
def r(*terms):
    return '<mrow>'+''.join(terms)+'</mrow>'
def f(a,b):
    return '<mfrac>'+a+b+'</mfrac>'
def p(a,b):
    return '<msup>'+a+b+'</msup>'
def sub(a,b):
    return '<msub>'+m(a)+m(b)+'</msub>'
def par(a):
    return r(o('('),a,o(')'))
def diff(a,b):
    return r(m(a),o('−'),m(b))
def plus(a,b):
    return r(m(a),o('+'),m(b))
def eq(lhs,rhs):
    return r(m(lhs),o('='),rhs)
def card(title,formula,variables,use):
    memory,example=TIPS[title]
    return '<div class="card"><h3>'+title+'</h3><div class="formula"><math xmlns="http://www.w3.org/1998/Math/MathML" display="block">'+formula+'</math></div><p>'+variables+'</p><p><strong>Cuándo usarla.</strong> '+use+'</p><div class="tip"><p><strong>Para acordarte</strong> · '+memory+'</p><p>'+example+'</p></div></div>'

pending=diff('BAC','EV')
growth=par(r(n(1),o('+'),m('i')))
factor=p(growth,m('n'))
combined=r(m('CPI'),o('×'),m('SPI'))
cards=[]
def add(*args):
    cards.append(card(*args))

def build():
    cards.clear()
    cards.append('<h2>Valor ganado y pronósticos</h2><p><strong>BAC</strong> es presupuesto total al término. <strong>PV</strong> es trabajo planificado valorizado al presupuesto. <strong>EV</strong> es trabajo ejecutado valorizado al presupuesto. <strong>AC</strong> es costo real incurrido. Los cuatro se expresan en la misma unidad monetaria.</p>')
    add('PV y EV por actividad',r(eq('PV',r(o('∑'),sub('B','j'),o('×'),sub('p','j'))),o(';'),eq('EV',r(o('∑'),sub('B','j'),o('×'),sub('a','j')))),
        'Bⱼ es el presupuesto de la actividad j, pⱼ su fracción planificada al corte y aⱼ su fracción real. Usa 0,40 para 40 %. AC es la suma de los costos reales.',
        'Pondera cada actividad por su presupuesto. Si el costo se distribuye uniformemente, la fracción planificada depende de los periodos transcurridos dentro de esa actividad.')
    for title,lhs,rhs,meaning in [
        ('Variación de costo','CV',diff('EV','AC'),'Positiva significa costo favorable para el trabajo realizado. Negativa indica sobrecosto.'),
        ('Variación de cronograma','SV',diff('EV','PV'),'Positiva significa adelanto en trabajo valorizado y negativa atraso. La unidad es monetaria.'),
        ('Índice de costo','CPI',f(m('EV'),m('AC')),'Mayor que uno es favorable. Expresa valor presupuestado obtenido por unidad gastada.'),
        ('Índice de cronograma','SPI',f(m('EV'),m('PV')),'Mayor que uno indica más trabajo ejecutado que previsto a la fecha.'),
    ]:
        add(title,eq(lhs,rhs),'V significa variación e I significa índice. Los índices son adimensionales.',meaning+' Recuerda EV primero, S con P y C con A.')
    add('Relación general del pronóstico',eq('EAC',plus('AC','ETC')),
        'EAC es costo total estimado al terminar y ETC es costo pendiente estimado.',
        'Se cumple para cualquier pronóstico. El supuesto del enunciado determina cómo calcular ETC.')
    for title,formula,use in [
        ('Resto al costo presupuestado',eq('EAC',r(m('AC'),o('+'),par(pending))),'Los costos pasados fueron atípicos y el resto costará lo previsto. ETC es BAC menos EV.'),
        ('Continúa la eficiencia de costo',eq('EAC',f(m('BAC'),m('CPI'))),'Se mantiene el CPI actual. ETC es el trabajo pendiente presupuestado dividido por CPI.'),
        ('Influyen costo y cronograma',eq('EAC',r(m('AC'),o('+'),f(pending,combined))),'El enunciado indica que tanto CPI como SPI afectarán lo que falta. La fracción completa es ETC.'),
        ('Nueva estimación detallada',eq('EAC',r(m('AC'),o('+'),sub('ETC','nuevo'))),'Se ha vuelto a estimar el trabajo restante con datos actualizados.'),
    ]:
        add(title,formula,'Usa BAC, EV y AC al mismo corte y con la misma unidad.',use)
    for target in ['BAC','EAC']:
        add('TCPI para terminar con '+target,eq('TCPI',f(pending,diff(target,'AC'))),
            'TCPI es el índice de desempeño del trabajo por completar. El numerador mide trabajo faltante y el denominador fondos restantes para la meta.',
            'La meta '+target+' debe estar indicada. Compara la eficiencia requerida con el CPI observado. Un valor mayor que uno exige más de una unidad de trabajo presupuestado por unidad disponible.')
    add('Variación prevista al cierre',eq('VAC',diff('BAC','EAC')),'VAC es variación al término.','Un valor negativo anticipa que el costo final superará el presupuesto.')
    cards.append('<h2>Estimaciones, precio y adquisiciones</h2>')
    add('PERT y promedio triangular',r(eq('C',f(r(m('O'),o('+'),n(4),m('M'),o('+'),m('P')),n(6))),o(';'),eq('C',f(r(m('O'),o('+'),m('M'),o('+'),m('P')),n(3)))),
        'O es costo optimista, M más probable y P pesimista. La primera fórmula es PERT y la segunda triangular.',
        'Usa el método solicitado. Paramétrica multiplica cantidad por costo unitario y ascendente suma costos detallados.')
    add('Markup y margen sobre ventas',r(eq('Markup',f(diff('Precio','Costo'),m('Costo'))),o(';'),eq('Margen',f(diff('Precio','Costo'),m('Precio')))),
        'Multiplica el cociente por 100 para expresar porcentaje.','Precio = costo × (1 + markup). Identifica la base requerida.')
    add('Evaluación ponderada de proveedores',eq('Puntaje',r(o('∑'),sub('w','j'),o('×'),sub('nota','j'))),
        'wⱼ es peso decimal de cada criterio y la suma de pesos es uno.',
        'Aplica criterios publicados y comprueba requisitos excluyentes antes del ranking. Los incentivos contractuales usan la regla de reparto y los límites pactados.')
    cards.append('<h2>Flujo, impuestos y valores terminales</h2>')
    add('Flujo del periodo y saldo',r(eq('FC',diff('Cobros','Pagos')),o(';'),eq('Saldo',r(sub('Saldo','anterior'),o('+'),m('FC')))),
        'FC es flujo neto del periodo.','Acumula por fecha para hallar el valle de caja. Sin intereses ni otras restricciones, el aporte para saldo mayor o igual a cero cubre el déficit acumulado máximo.')
    add('Depreciación y valor libro',r(eq('D',f(diff('Costo','Residual'),m('Vida'))),o(';'),eq('VL',diff('Costo','Depreciación acumulada'))),
        'D es depreciación anual lineal, VL valor libro y Vida número de años depreciables.',
        'El año de compra y de inicio de uso determina cuántas depreciaciones se registran al corte.')
    add('Caja operativa después de impuestos',eq('FCO',r(par(diff('Ingresos','Costos desembolsables')),par(r(n(1),o('−'),m('t'))),o('+'),m('D'),m('t'))),
        'FCO es flujo de caja operativo, t tasa tributaria y D depreciación. Equivale a utilidad neta más D en este modelo sin deuda.',
        'Supone que las deducciones se aprovechan en el periodo. Después resta inversiones y variaciones de capital de trabajo y suma recuperaciones pertinentes.')
    add('Venta de un activo neta de impuesto',eq('Venta neta',r(m('V'),o('−'),par(diff('V','VL')),m('t'))),
        'V es precio de venta, VL valor libro y t tasa de impuesto.',
        'La diferencia V menos VL es ganancia o pérdida gravable. El ahorro por pérdida depende de poder aprovecharlo en el periodo.')
    add('Flujo incremental',eq('ΔFC',diff('FC con proyecto','FC sin proyecto')),
        'Δ significa cambio entre escenarios.','Incluye costos de oportunidad, venta de activos y efectos tributarios diferenciales. Los costos iguales en ambos escenarios se cancelan.')
    cards.append('<h2>Dinero en el tiempo y préstamos</h2><p>Usa tasa y número de periodos con la misma frecuencia. Las tasas se reemplazan como decimales, por ejemplo 0,01 para 1 %.</p>')
    add('Valor futuro y presente',r(eq('VF',r(m('VA'),factor)),o(';'),eq('VA',f(m('VF'),factor))),
        'VA es valor actual, VF futuro, i tasa por periodo y n cantidad de periodos.','Capitalizar multiplica y descontar divide por el factor compuesto.')
    add('Equivalencia de tasas efectivas',eq('i mensual',r(p(par(r(n(1),o('+'),m('i anual'))),f(n(1),n(12))),o('−'),n(1))),
        'Las dos tasas deben ser efectivas.','Si el enunciado fija tasa nominal anual divisible por 12, aplica esa división contractual.')
    add('Saldo tras gracia y cuota fija',r(eq('P',r(m('L'),p(growth,m('g')))),o(';'),eq('C',r(m('P'),f(r(m('i'),factor),r(factor,o('−'),n(1)))))),
        'L es préstamo original, g meses sin pagos con interés capitalizado, P saldo al terminar gracia, C cuota y n número de cuotas posteriores.',
        'Primero capitaliza la gracia y luego calcula la cuota. Intereses totales = n por C menos L. Para la primera amortización, resta a la cuota el interés del saldo inicial.')
    add('Valor presente de pagos iguales',eq('VA',r(m('C'),f(r(factor,o('−'),n(1)),r(m('i'),factor)))),
        'C es pago constante al final de cada periodo durante n periodos.',
        'El resultado queda un periodo antes del primer pago. Si hay diferimiento, descuéntalo además hasta año cero.')
    cards.append('<h2>Viabilidad económica</h2>')
    add('Valor actual neto',eq('VAN',r(opminus:=o('−'),sub('I','0'),o('+'),'<munderover><mo>∑</mo><mrow><mi>t</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover>',f(sub('FC','t'),p(par(r(n(1),o('+'),m('r'))),m('t'))))),
        'I₀ es inversión inicial positiva, FCₜ flujo del periodo t, r tasa exigida y n horizonte.',
        'VAN positivo supera el rendimiento exigido. Si FC₀ ya tiene signo negativo, usa FC₀ más los valores presentes. La TIR es la tasa r que hace VAN cero.')
    add('Relación beneficio/costo',eq('B/C',f(m('VP beneficios'),m('VP costos'))),
        'VP significa valor presente.','Mayor que uno señala beneficio neto positivo con partidas consistentes. Para excluyentes comparables, evalúa riqueza mediante VAN.')
    add('Equilibrio en unidades',eq('Q equilibrio',f(m('CF'),diff('precio','cv'))),
        'CF es costo fijo total y cv costo variable unitario.','Supone precio superior a cv y parámetros constantes en el rango analizado.')
    add('Valor económico agregado básico',eq('VEA',r(m('Resultado operativo después de impuestos'),o('−'),m('Capital'),o('×'),m('Costo de capital'))),
        'El costo de capital se expresa como tasa para el mismo periodo.','Evalúa si el resultado cubre la remuneración exigida al capital. Para flujos sostenibles revisa reinversiones.')
    cards.append('<div class="notice"><strong>PRI simple y descontado.</strong> Acumula los flujos originales o sus valores presentes, respectivamente, hasta recuperar la inversión. Con cobros al cierre informa el periodo. Una fracción de año requiere un supuesto sobre distribución dentro del periodo.<p><strong>Para acordarte</strong> · PRI pregunta “¿cuándo recupero?”. Si dice descontado, trae primero cada cobro a hoy. Por ejemplo, inviertes 100 y cobras 55 al final de cada uno de dos años. Recuperas nominalmente en el año 2, pero al 10 % esos cobros valen juntos 95,45 y todavía falta recuperar en términos descontados.</p></div>')
    return ''.join(cards)
