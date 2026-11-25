from pathlib import Path
import json
import markdown

root = Path(__file__).parent
rows = """Proyectos|¿Qué caracteriza a un proyecto?|Resultado único y duración temporal|Servicio repetitivo indefinido|Solo el presupuesto anual|Ausencia de interesados|Un proyecto tiene inicio y fin y crea un resultado único. Operar diariamente el servicio es operación.
Proyectos|¿Qué integra la línea base del alcance?|Declaración, EDT y diccionario de EDT|Solo carta Gantt|Acta y facturas|Registro de riesgos y costos|La EDT descompone entregables; su diccionario define paquetes y criterios.
Proyectos|El cliente pide otra función con precio y fecha pactados. ¿Qué corresponde primero?|Analizar impacto y tramitar el cambio|Agregarla y registrar después|Modificar el BAC de inmediato|Compensarla eliminando pruebas|Se evalúan alcance, costo, plazo, calidad y riesgos antes de aprobar una nueva línea base.
Proyectos|¿Cuál requisito permite comprobar aceptación?|P95 de respuesta ≤ 2 s con 500 usuarios|Interfaz moderna|Servicio suficientemente rápido|Máxima seguridad posible|Condición, métrica, umbral y método hacen verificable un requisito.
Proyectos|Una prueba técnica exitosa produce principalmente…|Un entregable verificado|Un contrato cerrado|Una aceptación formal del cliente|Una actualización automática del alcance|Controlar calidad verifica; validar alcance busca aceptación formal.
Proyectos|¿Qué representa la ruta crítica?|La secuencia de mayor duración que determina el plazo|La de más costo|La de más personas|La de mayor holgura|En una red sin restricciones adicionales, la ruta más larga limita la duración mínima.
Proyectos|Dos rutas duran 12 y 9 días. Se agregan 2 días a la segunda. ¿Plazo nuevo?|12 días|14 días|11 días|13 días|La segunda queda en 11, todavía menor que 12.
Proyectos|Superponer diseño y construcción para acortar plazo corresponde a…|Fast tracking|Crashing|Nivelación de costos|Reserva de gestión|Superponer actividades aumenta riesgo de retrabajo. Crashing agrega recursos para comprimir duración.
Proyectos|¿Qué distingue un riesgo de un problema ocurrido?|El riesgo es incierto; el problema ya existe|El problema siempre cuesta más|El riesgo solo es negativo|El problema no tiene responsable|Un riesgo puede ser amenaza u oportunidad. Al ocurrir debe gestionarse como situación real.
Proyectos|Pérdida de 800 UF con probabilidad 25 %. ¿Exposición esperada?|200 UF|600 UF|3.200 UF|800 UF|Valor esperado de pérdida = 0,25 × 800. Es una media ponderada, no un desembolso seguro.
Proyectos|Contratar un seguro para una amenaza corresponde principalmente a…|Transferir|Evitar|Explotar|Escalar|Se transfiere una parte de la consecuencia financiera mediante contrato.
Proyectos|¿Qué es una auditoría de calidad?|Revisión del proceso y su cumplimiento|Aceptación comercial del cliente|Cálculo de la TIR|Prueba funcional exclusiva del producto|Gestionar calidad revisa procesos; controlar calidad examina resultados.
Proyectos|En precio fijo, un alcance bien definido transfiere más riesgo de costo a…|El proveedor|El cliente|Los usuarios|El regulador|El proveedor debe cumplir el alcance por el precio pactado, sujeto a cambios contractuales.
Proyectos|¿Qué permite la trazabilidad?|Conectar requisito, entregable, prueba y aceptación|Eliminar la necesidad de pruebas|Congelar todos los requisitos|Reemplazar el presupuesto|Ayuda a revisar cobertura e impacto de cambios.
Proyectos|Un interesado con alto poder y alto interés requiere…|Gestión cercana|Solo informes al cierre|Monitoreo mínimo|Delegar toda decisión técnica|La participación se adapta al poder, interés e impacto.
Costos|Una estimación usa 300 HH a 0,5 UF/HH. ¿Técnica y monto?|Paramétrica, 150 UF|Análoga, 150 UF|Ascendente, 600 UF|PERT, 150 UF|Se aplica un parámetro unitario a una cantidad.
Costos|PERT con optimista 80, probable 110 y pesimista 200 da…|120 UF|130 UF|110 UF|160 UF|(80 + 4×110 + 200)/6 = 120.
Costos|¿Qué reserva integra la línea base de costos?|Contingencia|Gestión completa|Utilidad del proveedor|Intereses futuros por defecto|La contingencia cubre riesgos identificados; gestión integra el presupuesto total.
Costos|BAC 2.000, avance real ponderado 35 %. ¿EV?|700 UF|1.300 UF|Depende del AC|2.000 UF|EV valora el trabajo realizado a precios del presupuesto: 2.000×0,35.
Costos|Una actividad cuesta 900 y dura meses 4 a 6 uniformemente. ¿PV al cierre del mes 5?|600 UF|500 UF|900 UF|450 UF|Han transcurrido dos de sus tres meses planificados: 900×2/3.
Costos|Una actividad futura se inicia antes y completa 10 %. ¿Cómo afecta al corte?|Suma EV y AC; su PV sigue según el plan|Suma PV automáticamente|No suma EV hasta su mes planificado|Solo aumenta BAC|PV depende de la línea base; EV recoge avance real autorizado incluso anticipado.
Costos|EV 800, AC 1.000, PV 700. ¿Diagnóstico?|Adelantado con sobrecosto|Atrasado con ahorro|Adelantado con ahorro|Atrasado con sobrecosto|SV=100 y CV=−200. Cronograma compara EV con PV; costo con AC.
Costos|CPI 0,8 significa…|0,8 UF de trabajo presupuestado por UF gastada|80 % de avance total|20 % de atraso temporal|80 % del presupuesto disponible|CPI=EV/AC mide eficiencia de costo.
Costos|SPI 0,8 permite afirmar…|Se ejecutó 80 % del valor previsto a la fecha|El proyecto lleva 80 % de avance total|Falta 20 % de días|El AC supera BAC en 20 %|SPI compara trabajo ejecutado con planificado al mismo corte.
Costos|BAC 1.000, EV 400, AC 500. Resto al costo original. ¿EAC?|1.100 UF|1.250 UF|900 UF|600 UF|EAC=AC+(BAC−EV)=500+600.
Costos|Mismos datos, persiste eficiencia de costo. ¿EAC?|1.250 UF|1.100 UF|800 UF|1.500 UF|CPI=400/500=0,8; EAC=1.000/0,8.
Costos|BAC 1.000, EV 400, AC 500, SPI 0,75. Influyen ambos índices. ¿EAC?|1.500 UF|1.250 UF|1.100 UF|1.000 UF|ETC=600/(0,8×0,75)=1.000. EAC=500+1.000.
Costos|BAC 1.000, EV 400, AC 500. ¿TCPI para BAC?|1,2|0,8|0,6|1,5|Trabajo faltante 600 dividido por fondos restantes 500.
Costos|BAC 1.000, EV 400, AC 500, EAC 1.300. Meta revisada. ¿TCPI?|0,75|1,2|0,8|1,3|Denominador EAC−AC=800. Numerador BAC−EV=600.
Costos|Se pronostica EAC 1.300 pero se exige terminar con BAC 1.000. TCPI usa…|BAC−AC en el denominador|EAC−AC en el denominador|BAC−PV en el denominador|EAC−EV en el denominador|La meta exigida decide el denominador, aunque exista otro pronóstico.
Costos|Paquetes 100 y 900 avanzan 100 % y 0 %. ¿EV?|100 UF|500 UF|900 UF|1.000 UF|Pondera por presupuesto: 100×1+900×0. El promedio simple de porcentajes distorsiona.
Costos|EAC 1.500 y AC 600. ¿ETC?|900 UF|2.100 UF|600 UF|1.500 UF|ETC es lo que falta gastar: EAC−AC.
Caja|Un estudio ya pagado, irrecuperable, se trata como…|Costo hundido excluido de la decisión futura|Inversión incremental en año 0|Costo de oportunidad anual|Recuperación al cierre|Ocurrirá el mismo costo histórico con o sin ejecutar la alternativa.
Caja|Dejar un empleo para emprender implica…|Costo de oportunidad de ingresos sacrificados|Costo hundido|Depreciación|Ingreso financiero|La decisión sacrifica una alternativa disponible. La pauta incluye esos sueldos en el flujo económico.
Caja|Capital de trabajo aportado al inicio y recuperable al cierre se registra…|Negativo al inicio y positivo al cierre|Gasto anual repetido|Solo como depreciación|Como ingreso inicial|Los fondos quedan comprometidos temporalmente.
Caja|Flujos −100, +60, +60. Nominal y VAN a 10 % son…|20 y 4,13|20 y 20|4,13 y 20|20 y −4,13|VAN=−100+60/1,1+60/1,1²=4,13.
Caja|VAN cero significa…|Se alcanza exactamente la tasa exigida|No hay ingresos|La TIR es cero|Se pierde toda la inversión|El valor actual de cobros netos cubre la inversión y el rendimiento exigido.
Caja|Si un ingreso del año 1 cae en 110 UF, a 10 % el VAN cae…|100 UF|110 UF|121 UF|90 UF|La variación de VAN es −110/1,1.
Caja|Una inversión convencional tiene TIR 14 % y tasa exigida 10 %. Entonces…|VAN positivo|VAN cero|VAN negativo|PRI necesariamente un año|Para desembolso inicial y cobros posteriores, TIR superior a r implica VAN positivo.
Caja|Dos excluyentes comparables difieren de tamaño. Se prioriza…|Mayor VAN|Mayor TIR siempre|Menor inversión siempre|Menor PRI siempre|VAN mide riqueza creada en unidades monetarias actuales.
Caja|Con varios cambios de signo, la TIR puede…|Ser múltiple|Siempre ser única|Coincidir con la inflación|Eliminar el costo de oportunidad|Puede haber varias raíces de VAN=0.
Caja|Depreciación 200 e impuesto 25 %, con utilidad gravable suficiente. Efecto anual tributario…|Ahorro de 50|Salida de caja de 200|Ingreso por ventas de 50|Ahorro de 200|Reduce impuesto en 200×0,25=50. El desembolso del activo se registra en su compra.
Caja|Costo 500 y precio 600. Markup y margen sobre ventas son…|20 % y 16,67 %|20 % y 20 %|16,67 % y 20 %|25 % y 16,67 %|Utilidad 100. Markup=100/500; margen=100/600.
Caja|Flujos −400, −300, +900. Aporte inicial mínimo para saldo ≥0…|700|400|900|200|Acumulados −400, −700, +200. El valle exige 700, sin intereses.
Caja|Préstamo 1.000 al 1 % mensual, 2 meses sin pagos. Deuda…|1.020,10|1.020|1.000|1.200|Interés capitalizado: 1.000×1,01².
Caja|12 % nominal anual con división explícita por 12 implica…|1 % mensual|0,9489 % mensual|12 % mensual|1,12 % mensual|La convención contractual indicada gobierna. La raíz doce aplica a equivalencia de tasa efectiva.
Caja|Intereses totales con gracia capitalizada y cuotas iguales…|Suma de cuotas menos préstamo original|Suma de cuotas menos saldo tras gracia|Cuota por tasa mensual|Saldo tras gracia menos última cuota|Restar el préstamo original incluye intereses de la gracia y de amortización.
Caja|Con la misma deuda y tasa positiva, más cuotas producen…|Menor cuota y mayor interés total|Mayor cuota y menor interés|Igual interés total|Menor deuda inicial|La deuda permanece más tiempo generando intereses.
Caja|EBITDA 600, depreciación 100, impuesto 20 %, sin deuda ni inversión anual. Flujo…|500|400|600|480|EBIT=500; impuesto=100; utilidad=400; se suma de vuelta 100.
Caja|Precio de venta del activo igual a su valor contable. Ganancia sobre libros…|Cero|El precio completo|La depreciación anual|El costo original|Ganancia contable=precio de venta−valor contable. La venta sí aporta caja."""
questions=[]
for i,line in enumerate(rows.splitlines()):
    topic,prompt,*parts=line.split('|')
    options=parts[:4]; explanation=parts[4]
    offset=(i*3+1)%4
    options=options[offset:]+options[:offset]
    questions.append(dict(topic=topic,prompt=prompt,options=options,answer=(-offset)%4,explanation=explanation))
assert len(questions)==50

extra="""# Lo que añade la pauta del Control 3 de 2026

## Costos pertinentes y costo de oportunidad
Un costo **hundido** ya ocurrió y es irrecuperable. El estudio de mercado pagado por 300 UF queda fuera de la decisión futura. Un costo **de oportunidad** es lo que sacrificas por elegir el proyecto. Los socios que dejan sueldos por 1.200 UF anuales deben descontarlos en la evaluación económica. Ese sacrificio afecta la conveniencia, aunque no sea un pago de tesorería del negocio.

**Recuerda “pasado irrecuperable fuera, alternativa sacrificada dentro”.** Para cada partida pregunta qué cambia si aceptas el proyecto.

## La pauta de flujo resuelta
Inversión inicial = 6.000 equipos + 4.500 desarrollo + 1.500 capital de trabajo = 12.000 UF. Flujo anual = ingresos − operación − costo de oportunidad. Al cierre se agregan 1.500 de capital recuperado y 1.000 de venta de equipos.

|Año|0|1|2|3|4|
|---|---:|---:|---:|---:|---:|
|Flujo UF|−12.000|3.000|4.000|4.800|7.800|

Nominal = suma de flujos = 7.600 UF. VAN = −12.000 + 3.000/1,1 + 4.000/1,1² + 4.800/1,1³ + 7.800/1,1⁴ = 2.966,87 UF. **Nominal positivo puede coexistir con VAN negativo.** Al reducir a la mitad el ingreso del año 1, el flujo de ese año pasa a −750. El VAN pierde 3.750/1,1 y queda en −442,22 UF.

## Préstamos con meses de gracia
Durante la gracia sin pagos, el interés se incorpora al saldo. Si el préstamo original es L, la tasa mensual i y hay g meses de gracia, el saldo para calcular cuotas es **P = L(1+i)^g**. La primera cuota ocurre al mes siguiente del fin de la gracia.

Luego **C = P × i(1+i)^n / [(1+i)^n−1]**, donde C es cuota mensual y n el número de cuotas. Intereses totales = n×C − L. Se resta el préstamo original para incluir los intereses de la gracia.

En la pauta L=12.000, i=0,01, g=6. Saldo al mes 6 ≈12.738,24. A 12 cuotas, C≈1.131,78; a 18, C≈776,80. Usando cuotas redondeadas, intereses ≈1.581,36 y 1.982,40 UF. Un plazo mayor reduce la cuota y eleva el costo financiero total.

## Valor ganado de la pauta
BAC=4.000. PV al mes 5=400+600+1.200×2/4+900×2/3=2.200. EV=400+600+480+450+60=1.990. AC=2.340. Integración anticipada suma 60 de EV aunque su PV al corte sea cero.

CV=−350 y SV=−210. CPI=0,8504 y SPI=0,9045. EAC=AC+(BAC−EV)/(CPI×SPI). La pauta informa 4.952,93 UF usando redondeos intermedios. Con los dos índices mostrados y sin redondear su producto resulta aproximadamente 4.953,15 UF; acepta diferencias pequeñas si el procedimiento está justificado.

El patrocinador exige BAC, así que TCPI=(4.000−1.990)/(4.000−2.340)=1,2108. Comparado con CPI≈0,8504, exige mejorar la eficiencia cerca de 42 %. El pronóstico y la meta son dos cantidades diferentes.

## Cómo escribir el desarrollo
1. Anota datos, siglas y unidades.
2. Identifica el supuesto y escribe la fórmula antes de reemplazar.
3. Sustituye números y conserva precisión.
4. Interpreta signo, tamaño, decisión y limitaciones.

La pauta del Control 3 exige desarrollo incluso al seleccionar alternativas. Practica la explicación además del número.
"""

sources=[
('Gestión de proyectos','Proyecto, interesados y requisitos','guia_estudio_fep26_por_temas/01_proyecto_interesados_requisitos.md'),
('Gestión de proyectos','Alcance y EDT','guia_estudio_fep26_por_temas/02_alcance_y_EDT.md'),
('Gestión de proyectos','Planificación y cronograma','guia_estudio_fep26_por_temas/03_planificacion_y_cronograma.md'),
('Gestión de proyectos','Riesgos','guia_estudio_fep26_por_temas/09_gestion_de_riesgos.md'),
('Gestión de proyectos','Adquisiciones','guia_estudio_fep26_por_temas/10_adquisiciones_contratos_TCO.md'),
('Gestión de proyectos','Calidad','guia_estudio_fep26_por_temas/11_gestion_de_calidad.md'),
('Gestión de proyectos','Procesos y sus conexiones','guia_estudio_fep26_por_temas/14_procesos_PMBOK_ITTO.md'),
('Costos y flujo de caja','Guía explicada con fórmulas','GUIA_ESTUDIO_CONTROL_3_FEP.md')]
lessons=[]
for topic,title,path in sources:
    body=markdown.markdown((root/path).read_text(encoding='utf-8'),extensions=['tables','fenced_code'])
    lessons.append(dict(topic=topic,title=title,body=body))
lessons.insert(0,dict(topic='Pauta 2026',title='Los ejercicios que debes dominar',body=markdown.markdown(extra,extensions=['tables'])))

exam=[
dict(title='Decisión de gestión',points=10,prompt='Un cliente pide integrar pagos durante la construcción. Contrato de precio fijo, fecha comprometida y alcance aprobado. El proveedor propone incorporarlo quitando pruebas. Redacta una respuesta que conecte alcance, calidad, riesgo y aprobación.',rubric=['Identifica una solicitud de cambio y documenta el requisito (2).','Analiza impacto en alcance, costo, plazo y dependencias (3).','Explica riesgo de reducir pruebas y propone alternativas verificables (3).','Obtiene decisión autorizada y actualiza las líneas base aprobadas (2).']),
dict(title='Valor ganado por actividades',points=25,prompt='Corte al final del mes 4. A: costo 600, meses 1–2, avance 100 %, AC 660. B: costo 1.200, meses 3–6, avance 35 %, AC 500. C: costo 900, meses 4–6, avance 20 %, AC 250. D: costo 300, meses 7–8, avance 10 %, AC 50. Distribución uniforme por actividad. Calcula BAC, PV, EV, AC, CV, SV, CPI y SPI. Explica cómo tratar D.',rubric=['BAC=3.000 y PV=600+600+300=1.500 (5).','EV=600+420+180+30=1.230; AC=1.460 (5).','CV=−230 y SV=−270 UF (5).','CPI=0,8425; SPI=0,82; sobrecosto y atraso (5).','D suma EV y AC reales, pero PV=0 al corte según línea base (5).']),
dict(title='Pronóstico y exigencia del patrocinador',points=15,prompt='Usa el caso anterior. Tanto costo como plazo influyen sobre el trabajo restante, pero el patrocinador exige BAC. Calcula ETC, EAC y TCPI para la meta exigida. Compara TCPI con CPI e indica qué cambios tendrían que evaluarse. Usa cocientes sin redondear hasta el final.',rubric=['ETC=1.770/[(1.230/1.460)×0,82]≈2.562,17 UF (4).','EAC=1.460+ETC≈4.022,17 UF (4).','TCPI=1.770/(3.000−1.460)=1,1494 (4).','Mejora relativa de eficiencia≈36,43 %. Analizar alternativas de productividad, alcance aprobado y financiamiento (3).']),
dict(title='Flujo económico y sensibilidad',points=20,prompt='Proyecto de 3 años. Año 0: equipos 5.000, software 3.000, capital de trabajo 1.000 UF. Estudio irrecuperable ya pagado 400. Ingresos 5.500, 6.500 y 7.000; operación 2.200, 2.500 y 2.700. Sueldo sacrificado 800 por año. Al final del año 3 se vende equipo por 900 y se recupera todo el capital de trabajo. Sin impuestos ni depreciación; tasa 10 %. Construye flujo, nominal y VAN. Recalcula si ingresos del año 1 caen 40 %, sin recuperación posterior.',rubric=['Excluye 400 hundidos e incluye 800 de oportunidad anuales (4).','Flujos −9.000; 2.500; 3.200; 5.400 (5).','Nominal=2.100; VAN≈−25,54 UF; no cubre el 10 % (5).','Caída de 2.200 en año 1: flujo=300, nominal=−100; VAN≈−2.025,54 (4).','Interpreta correctamente descuento y decisión (2).']),
dict(title='Crédito con gracia',points=15,prompt='Se financian 9.000 UF a 12 % nominal anual dividido por 12, con 3 meses sin pagos e interés capitalizado. Primera cuota al final del mes 4. Compara 12 y 18 cuotas. Calcula saldo al finalizar gracia, cuota e intereses totales desde el desembolso original. Redondea solo resultados finales.',rubric=['i=1 % mensual; P=9.000×1,01³=9.272,709 UF (3).','Aplica fórmula de anualidad sobre saldo capitalizado (4).','12 cuotas≈823,87 UF; intereses≈886,43 UF (3).','18 cuotas≈565,47 UF; intereses≈1.178,44 UF (3).','Más plazo reduce cuota pero aumenta interés total (2).']),
dict(title='Contabilidad y caja',points=15,prompt='Una máquina cuesta 2.400 UF al año 0, vida 4 años y residual contable cero. EBITDA anual 1.500 UF durante 2 años. Impuesto 20 %, sin deuda ni capital de trabajo. Se vende al final del año 2 por su valor contable. Calcula depreciación, EBIT, impuesto, flujo anual y flujo terminal. Justifica sumar depreciación de vuelta.',rubric=['Depreciación=600/año; EBIT=900; impuesto=180 (5).','Flujo operativo=900−180+600=1.320 (4).','Valor contable final=1.200; flujo año 2=2.520; año 0=−2.400 (4).','Depreciación es gasto sin desembolso corriente y afecta base tributaria (2).'])]
data=dict(questions=questions,lessons=lessons,exam=exam)
(root/'datos_practica_fep.json').write_text(json.dumps(data,ensure_ascii=False),encoding='utf-8')
