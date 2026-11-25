from pathlib import Path
import json
import markdown

root=Path(__file__).parent
data=json.loads((root/'datos_practica_fep.json').read_text(encoding='utf-8'))
def lesson(title,text):
    return dict(topic='Temario confirmado',title=title,body=markdown.markdown(text,extensions=['tables','fenced_code']))

adquisiciones="""# Adquisiciones · PMBOK 6, capítulo 12

Adquirir implica obtener productos, servicios o resultados externos mediante acuerdos. El contrato obliga a ambas partes: el vendedor entrega lo pactado y el comprador cumple pagos y obligaciones. **El director del proyecto puede participar en la negociación; la firma corresponde a quien tenga autoridad.**

## Los tres procesos y sus resultados

|Proceso|Qué se decide o ejecuta|Entradas, herramientas y salidas|
|---|---|---|
|Planificar la gestión de adquisiciones|Qué adquirir, cómo y cuándo|Parte de necesidades, alcance, recursos, riesgos, mercado y políticas. Usa análisis hacer/comprar, investigación de mercado y juicio experto. Produce plan, estrategia, SOW, documentos de licitación y criterios de selección.|
|Efectuar adquisiciones|Obtener propuestas, evaluar, negociar y adjudicar|Usa documentos de licitación, criterios y propuestas. Conferencias de oferentes aclaran dudas con información equitativa. El análisis de propuestas y la negociación producen vendedores seleccionados y acuerdos.|
|Controlar adquisiciones|Monitorear obligaciones, gestionar cambios y reclamaciones, cerrar|Usa contratos, datos de desempeño y cambios aprobados. Inspecciones, auditorías y análisis permiten gestionar desviaciones. Produce información de desempeño, cambios y adquisiciones cerradas.|

**Para recordar: preparar → elegir y acordar → vigilar y cerrar.** En PMBOK 6 el cierre contractual está dentro de Controlar las Adquisiciones.

## Hacer o comprar

Compara capacidad interna, disponibilidad, costo completo, riesgo, plazos, propiedad intelectual y dependencia futura. Un equipo propio que cuesta menos pero retrasa un hito puede resultar peor que contratar.

Ejemplo sin descuento: fabricar internamente cuesta 1.000 de preparación más 20 por unidad. Comprar cuesta 30 por unidad. A 100 unidades ambos cuestan 3.000; a 150, fabricar cuesta 4.000 y comprar 4.500. Verifica capacidad y calidad antes de elegir.

**TCO** significa costo total de propiedad. Incluye compra, implantación, operación, soporte, renovación, transición y salida. Al comparar muchos años, actualiza los desembolsos.

## Documentos y siglas

|Sigla|Significado|Ejemplo de uso|
|---|---|---|
|RFI|Request for Information, solicitud de información|Desconoces proveedores y soluciones disponibles. Exploras el mercado.|
|RFQ|Request for Quotation, solicitud de cotización|Necesitas precios y condiciones para una compra definida.|
|RFP|Request for Proposal, solicitud de propuesta|Solicitas un enfoque de solución además de precio y capacidades.|
|SOW|Statement of Work, enunciado del trabajo|Define entregables, alcance contratado, cantidades, calidad, ubicación, fechas y servicios adicionales.|
|TOR|Terms of Reference, términos de referencia|En servicios, precisa tareas, coordinación, estándares, datos aportados y revisión.|
|SLA|Service Level Agreement, acuerdo de nivel de servicio|Precisa métrica, objetivo, medición y consecuencias del incumplimiento.|

La **estrategia** fija entrega, formas contractuales y fases. El **plan** organiza actividades, roles, autoridad, calendario, coordinación y control. La oferta del vendedor es evaluada; la adjudicación culmina en el acuerdo.

## Tipos de contrato

|Tipo|Pago y asignación de riesgo|Cuándo considerarlo|
|---|---|---|
|FFP, precio fijo cerrado|Precio acordado para alcance definido; sobrecostos propios recaen principalmente en vendedor|Requisitos estables|
|FPIF, precio fijo con incentivo|Objetivos, fórmula de incentivo y precio máximo|Interesa premiar desempeño medible y compartir desviaciones según contrato|
|FPEPA, precio fijo con ajuste económico|Ajustes predefinidos por índices o condiciones|Plazos largos y exposición a inflación o monedas|
|CPFF, costos más honorarios fijos|Reembolso de costos autorizados más un honorario fijo|Alcance incierto; comprador asume más riesgo de costo|
|CPIF, costos más incentivo|Reembolso más honorarios ajustados mediante reparto pactado|Alinear eficiencia con incertidumbre de alcance|
|CPAF, costos más honorarios por desempeño|Honorario depende de evaluación de criterios de desempeño del comprador|Desempeño difícil de reducir a una fórmula totalmente objetiva|
|T&M, tiempo y materiales|Tarifa fija por unidad, cantidad variable; conviene poner límites y controles|Expertos o personal cuando cuesta definir el trabajo completo al inicio|

**Fijo se refiere al precio o al honorario según el nombre.** En CPFF el honorario puede ser fijo y el total pagado aumentar por costos reembolsables.

Ejemplo de incentivo, con reparto explícito de ahorro: costo objetivo 1.000, honorario objetivo 100 y 20 % del ahorro para vendedor. Si el costo real autorizado es 900, ahorra 100, honorario final 120 y pago total 1.020. Aplica topes o mínimos si el contrato los contiene.

## Selección, cambios y cierre

Define antes los criterios y ponderaciones: técnica, costo del ciclo de vida, personal, experiencia, entrega y estabilidad financiera. Las conferencias de oferentes deben proporcionar un entendimiento común. Una oferta anormalmente baja requiere analizar si omite trabajo.

Una **reclamación** aparece cuando las partes discrepan sobre un cambio o su compensación. Documenta hechos y aplica negociación y mecanismos contractuales de resolución. Un acuerdo verbal informal no basta para actualizar obligaciones contractuales.

Para cerrar, revisa entregables aceptados, obligaciones, pagos, facturas y reclamaciones pendientes. El administrador autorizado comunica formalmente por escrito el cierre. Conserva registros y lecciones.

**Caso para pensar.** Un proveedor termina el software pero falta entregar los manuales pactados. La funcionalidad terminada no agota las obligaciones del contrato; verifica documentación y aceptación antes de cerrar.
"""
costos="""# Gestión de costos · PMBOK 6, capítulo 7

## Cuatro procesos conectados

|Proceso|Pregunta|Resultado principal|
|---|---|---|
|Planificar|¿Con qué reglas estimaremos y controlaremos?|Plan de gestión de costos|
|Estimar|¿Cuánto costarán recursos y trabajo?|Estimaciones y bases de estimación|
|Determinar presupuesto|¿Cuánto autorizamos y en qué fechas?|Línea base y requisitos de financiamiento|
|Controlar|¿Cómo vamos y cuánto costará terminar?|Información de desempeño, pronósticos y solicitudes de cambio|

**Plan → estimación → presupuesto → control.** Las entradas conectan requisitos, recursos, actividades, riesgos, acuerdos y mercado. La EDT sirve para agregar costos por paquetes; el cronograma ubica el presupuesto en el tiempo.

## Exactitud, precisión y bases

La precisión define el detalle o redondeo, por ejemplo a UF enteras. La exactitud describe el rango esperado de error. Una estimación temprana puede ser muy incierta aunque tenga muchos decimales.

La base de estimación documenta método, supuestos, restricciones, fuentes, rango y confianza. Ejemplo: “120 HH a 0,6 UF/HH, suponiendo una integración disponible, con rango de ±15 %”. Si falla ese supuesto, debes revisar la estimación.

**Análoga** usa un proyecto comparable. **Paramétrica** aplica costo por unidad. **Ascendente** suma componentes detallados. **Tres valores** considera optimista, probable y pesimista: promedio triangular con pesos iguales o PERT con peso cuatro al más probable. La guía de fórmulas incluye cálculos.

## Reservas y financiamiento

Contingencia para riesgos identificados integra la línea base. Gestión cubre trabajo imprevisto dentro del alcance y se añade para obtener el presupuesto total. Su aplicación requiere aprobación para transferir el monto correspondiente a la línea base.

Ejemplo: trabajo 900 + contingencia 100 = línea base 1.000. Reserva de gestión 80 → presupuesto total 1.080. BAC en el análisis de valor ganado corresponde al presupuesto de referencia del trabajo, excluyendo la reserva de gestión.

Conciliar límites de financiamiento exige comparar desembolsos por periodo con fondos disponibles. Que el total alcance no garantiza poder pagar cada mes.

## Control y pronóstico

PV es trabajo planificado valorizado, EV trabajo realizado valorizado y AC costo real. El avance se pondera por presupuesto. Un trabajo anticipado puede tener EV positivo y PV cero. AC puede incluir costos incurridos aún no pagados; la tesorería sigue fechas de pago.

**“EV primero; S con P; C con A. Variación resta, índice divide.”** Los desarrollos de la pauta y la guía explican CV, SV, CPI, SPI, ETC, EAC y TCPI. VAC significa variación al terminar: presupuesto BAC menos pronóstico EAC. VAC negativo anticipa sobrecosto.

El EAC es pronóstico; TCPI expresa eficiencia necesaria para una meta. Si el patrocinador exige BAC, usa BAC como meta aunque el pronóstico sea mayor. La autorización de cambios y las acciones correctivas deben documentarse.

Al finalizar todo el trabajo de la línea base, EV y PV terminan iguales y SPI tiende a uno. Por eso complementa valor ganado con el seguimiento real de fechas para interpretar retrasos al cierre.
"""
tributos="""# Lectura · Capítulo 4
# Aspectos tributarios, legales y administrativos

Los ejemplos de esta lectura usan tasas y supuestos históricos. Para el certamen aplica los datos del enunciado. El objetivo es explicar efectos económicos, sin convertir sus tasas antiguas en normativa vigente.

## Venta de activos y valor libro

**Valor libro** es costo de adquisición menos depreciación acumulada. **Valor de mercado** es lo que podría pagarse por el activo. **Residual contable** es el valor supuesto al finalizar su vida depreciable. Los tres pueden diferir.

La ganancia gravable de una venta es precio de venta menos valor libro. Si V es precio, VL valor libro y t tasa tributaria, el flujo neto de venta es:

FORMULA_VENTA

Ejemplo: V=2.500, VL=2.000 y t=15 %. Ganancia=500; impuesto=75; caja neta=2.425. El valor libro se resta al calcular utilidad y se agrega de vuelta al obtener caja.

Si V=3.000 y VL=4.000 hay pérdida contable de 1.000. Con tasa 15 % y utilidades suficientes para aprovecharla en ese periodo, el ahorro es 150 y el efecto incremental de caja es 3.150. **Una pérdida no garantiza un reembolso inmediato.** Verifica la capacidad de absorberla y cuándo se permite usarla según el caso.

## Compra, depreciación, costos e intereses

Comprar un activo intercambia efectivo por un activo. En el modelo de la lectura, su efecto deducible se distribuye mediante depreciación. Una compra de 9.000 depreciable en tres años produce 3.000 de depreciación anual. A 15 % y con base gravable suficiente, ahorra 450 de impuesto anual.

El ahorro es futuro: para compararlo con la inversión inicial hay que descontarlo. Depreciación acelerada cambia el momento de los ahorros y puede cambiar su valor actual.

Un costo deducible adicional de 200 a tasa de 15 % genera ahorro tributario de 30. El costo neto es 170. Un ahorro de costos también aumenta la base gravable: ahorro bruto 200 deja 170 después de impuestos.

Los intereses deducibles pueden producir escudo tributario. Interés 100 a tasa 20 % deja costo neto de 80 si se aprovecha la deducción. La devolución del principal se registra después del cálculo tributario.

## Pérdidas y análisis incremental

Compara impuesto total de la empresa **con y sin proyecto**. Si la empresa ya tiene utilidades, una pérdida del proyecto puede reducir el pago actual. Si la empresa también tiene pérdidas, el beneficio podría diferirse. Evita contabilizar el mismo crédito fiscal como beneficio de varias alternativas.

## IVA

El impuesto al valor agregado cobrado en ventas genera débito y el pagado en compras puede generar crédito recuperable, bajo los supuestos de la lectura. Aun siendo recuperable, puede requerir financiamiento entre el pago y la recuperación.

Tres situaciones relevantes: capital de trabajo para financiar IVA de compras; ventas exentas con compras gravadas cuyo crédito no se recupera; e inversiones con IVA elevado y recuperación tardía. El IVA recuperable se separa del costo depreciable. Si no es recuperable, revisa el tratamiento del enunciado.

## Administración y aspectos legales

Diseñar cargos, remuneraciones, oficinas, sistemas de facturación y cobranza determina inversión inicial y gastos recurrentes. Dimensiona según la operación; revisa crecimiento y reorganización.

La viabilidad legal pregunta si la actividad está permitida y bajo qué condiciones. El análisis económico cuantifica permisos, patentes, contratos, constitución, registros, propiedad intelectual, obligaciones y sus fechas. Un proyecto permitido puede perder rentabilidad por costos de cumplimiento omitidos.

**Tip de desarrollo:** identifica partida → efecto sobre utilidad → impuesto → movimiento efectivo → año en que ocurre.
"""
flujos="""# Lectura · Capítulo 7
# Cómo construir los flujos de caja

## Horizonte y momento

El horizonte es el periodo evaluado, que puede ser menor que la vida real del negocio. Año 0 registra compromisos iniciales. Cada flujo se ubica cuando ocurre; si se agregan años, se usa la convención del ejercicio sobre cobros al cierre.

Una vida real mayor exige representar los beneficios posteriores mediante un valor terminal adecuado. Si comparas alternativas de vidas distintas, usa un horizonte compatible o equivalentes anuales con supuestos explícitos de repetición.

## Los cinco pasos

1. Ordena ingresos y egresos afectos a impuestos.
2. Resta gastos contables no desembolsables para calcular utilidad gravable.
3. Calcula el impuesto y la utilidad neta.
4. Revierte los gastos sin desembolso previamente deducidos.
5. Incorpora inversiones, capital de trabajo y otros beneficios o egresos tratados fuera de la utilidad, evitando duplicaciones.

Ejemplo: ventas 1.000, operación 500, depreciación 100, impuesto 20 %. Utilidad 400, impuesto 80, utilidad neta 320. Sumando depreciación obtienes 420 de caja operativa. Una reinversión de 200 ese año reduce el flujo a 220.

## Tres finalidades

**Proyecto** mide el negocio sin financiamiento. **Inversionista** incluye entrada de deuda, intereses y amortización del principal y mide recursos propios. **Capacidad de pago** comprueba efectivo disponible para el servicio de deuda. Un valor terminal que solo representa continuidad del negocio no sirve por sí mismo para pagar una cuota.

En el flujo del inversionista, la deuda entra al inicio como financiamiento y reduce el aporte propio. Intereses afectan impuesto si son deducibles; principal se devuelve como caja después del cálculo tributario.

## Leasing

Permite usar un activo mediante pagos. El contrato puede contemplar compra final, renovación o devolución. La lectura distingue leasing financiero, con compromiso de largo plazo y características de financiación, y operativo, tratado en su ejemplo como alquiler deducible.

En el ejemplo de alquiler deducible, cuota de 100 y tasa tributaria de 20 % implican costo neto 80 con base gravable suficiente. Evita deducir además una depreciación del mismo activo si el esquema del ejercicio asigna el ahorro a la cuota. En leasing financiero distingue el modelo contable del tributario indicado.

## Capital de trabajo, reemplazos y valor terminal

Capital de trabajo es la inversión en fondos necesarios para operar antes de recuperar cobros. Puede aumentar con las ventas. Registra el incremento cuando se compromete y la recuperación cuando se libera.

Si vendes activos al cierre, incorpora precio menos efecto tributario. El método contable aproxima el remanente por valor libro. El método económico valora capacidad futura de generar beneficios. En este último, no agregues recuperaciones incompatibles con mantener el negocio ni dupliques capital ya incluido en la valoración.

Un reemplazo requiere salida por el equipo nuevo y entrada neta por vender el antiguo. Además cambian operación, depreciaciones, impuestos, futuras reposiciones y valor final.

## Con proyecto menos sin proyecto

El flujo incremental se calcula por diferencias entre escenarios. La base representa continuar razonablemente sin hacer la inversión. Si el negocio obtiene 10.000 sin proyecto y 13.000 con él, el beneficio incremental es 3.000. Ambos escenarios pueden ser rentables y uno ser mejor.

Si energía baja de 1.000 a 800, el ahorro incremental bruto es 200. Si además pierdes un arriendo de 50 por ocupar un local propio, incorpora ese costo de oportunidad. Los costos iguales en ambos escenarios se cancelan.

**Ejemplo de reemplazo:** comprar por 5.000, vender antiguo por 1.000 con VL=600 y tasa 25 %. Venta neta=900. Inversión incremental inicial=−4.100. Si ahorras 800/año y la depreciación incremental es 200, mejora de utilidad=600; impuesto adicional=150; flujo incremental=650.
"""
viabilidad="""# Lectura · Capítulo 8
# Cálculo y análisis de viabilidad económica

## Equivalencias temporales

Capitalizar lleva un valor hacia el futuro; descontar lo lleva hacia el presente. Para una tasa i y n periodos, VF = VA multiplicado por (1+i) elevado a n. La guía contiene las fórmulas renderizadas.

Una **anualidad** es una serie de flujos iguales espaciados regularmente. Su valor actual un periodo antes del primer pago se obtiene con:

FORMULA_ANUALIDAD

C representa el pago periódico. Cinco pagos de 100 al 10 % valen 379,08 hoy. Si la serie comienza más tarde, descuenta además el valor calculado hasta el año 0. Para acumular pagos iguales al final del último periodo se usa C multiplicado por el factor de acumulación.

## VAN, TIR y uso de planillas

VAN suma valores presentes y resta inversión inicial. Es valor adicional sobre el rendimiento exigido. TIR es la tasa que hace VAN cero. En flujos convencionales, TIR mayor que tasa exigida implica VAN positivo.

En Excel, VNA(tasa; flujos desde año 1) se suma al flujo del año 0, que ya está en presente. TIR incluye la secuencia completa desde año 0. Revisa periodicidad y signos.

Cambios de signo múltiples pueden dar varias TIR o ninguna solución útil. Para excluyentes de distinto tamaño, una TIR mayor puede coexistir con menor riqueza creada. Compara VAN bajo supuestos compatibles.

## Recuperación y beneficio/costo

**PRI simple** acumula sin descuento. **PRI descontado** acumula flujos actualizados, incorporando rendimiento exigido. La lectura desarrolla recuperación considerando ese rendimiento.

Ejemplo: inversión 100 y cobros de 60 en los años 1 y 2. Recupera dentro del segundo año bajo ambos criterios al 10 %, aunque el acumulado actualizado es menor. Si el pago ocurre solo al cierre, informa el periodo. Interpolar una fracción supone distribución dentro del año.

Relación beneficio/costo = valor presente de beneficios dividido por valor presente de costos. Mayor que 1 indica beneficios superiores a costos, con partidas y tasa consistentes. Beneficios presentes de 1.200 y costos de 1.000 → razón 1,2 y VAN 200. Un cociente mayor no garantiza mayor VAN entre alternativas de escala distinta.

## Valor económico agregado y punto de equilibrio

**VEA**, valor económico agregado, compara resultado operativo después de impuestos con cargo por capital utilizado. En una formulación básica: resultado neto operativo menos capital invertido por costo de capital. Si resultado=150, capital=1.000 y costo de capital=12 %, VEA=30.

La lectura advierte que mantener capacidad productiva exige reinversiones; incorpora ese efecto cuando se usa un flujo sostenible o perpetuo. Beneficio contable y creación de valor pueden diferir.

Punto de equilibrio operativo en unidades:

FORMULA_EQUILIBRIO

CF es costo fijo, p precio y cv costo variable unitario, con p mayor que cv. CF=1.000, p=30, cv=20 → 100 unidades. Cubre costos operativos bajo ese modelo. Para exigir además rendimiento sobre la inversión debes incorporar impuestos, reposición y costo de capital.

## Equivalente anual, perfil y opciones

Valor anual equivalente distribuye un VAN en una anualidad a la tasa y vida utilizadas. CAE es costo anual equivalente: anualiza el valor presente de costos netos. Entre servicios equivalentes, menor CAE es preferible cuando la comparación y repetición son válidas.

En evaluación de perfil se usan aproximaciones para decidir si profundizar. Un flujo perpetuo sostenible F vale F/i si permanece constante, inicia el próximo periodo y la tasa es positiva. Exige contemplar reinversiones, crecimiento y límites de capacidad antes de aceptar esa simplificación.

Las **opciones reales** representan decisiones futuras como esperar, ampliar o abandonar. La flexibilidad puede tener valor ante incertidumbre, pero ese valor requiere estimar escenarios, costos y derechos concretos. La lectura introduce la analogía con opciones de compra: derecho a invertir que puede ejercerse o postergarse.

**Tip:** primero construye correctamente el flujo y sus supuestos. Una fórmula de VAN bien aplicada a un flujo mal construido sigue dando una decisión equivocada.
"""
data['lessons']=[data['lessons'][0],lesson('Adquisiciones · procesos y contratos',adquisiciones),lesson('Costos · procesos y reservas',costos),data['lessons'][-1],lesson('Lectura 4 · efectos tributarios y legales',tributos),lesson('Lectura 7 · construcción de flujos',flujos),lesson('Lectura 8 · viabilidad económica',viabilidad)]
new_rows="""¿Qué proceso incluye cerrar contratos en PMBOK 6?|Controlar adquisiciones|Efectuar adquisiciones|Planificar adquisiciones|Estimar costos|El capítulo 12 integra cierre y seguimiento contractual en Controlar las Adquisiciones.
Necesitas explorar proveedores y tecnologías antes de fijar una compra. ¿Documento?|RFI|RFQ|Acta de aceptación|Orden de pago|RFI solicita información del mercado; después puedes preparar una cotización o propuesta.
Se busca resolver un problema técnico con distintos enfoques posibles. ¿Solicitud apropiada?|RFP|Factura|RFQ centrada solo en precio|Informe de cierre|Una RFP solicita propuestas de solución, enfoque técnico y condiciones.
¿Qué define el SOW de una adquisición?|Trabajo y resultados incluidos en ese contrato|Todo el portafolio empresarial|Solo el precio máximo|Solo el calendario de pagos|El enunciado del trabajo precisa alcance contratado, calidad, cantidades, plazos y servicios.
Alcance estable y producto bien definido. ¿Tipo coherente?|FFP|CPAF por defecto|T&M ilimitado|CPFF obligatorio|Precio fijo cerrado es adecuado cuando hay buena definición; cambios de alcance siguen el procedimiento contractual.
¿Qué permanece fijo en CPFF si el alcance no cambia?|El honorario pactado|El total de costos reembolsados|Toda la factura final|El costo de cada recurso|Costo más honorarios fijos reembolsa costos autorizados más un honorario fijo.
¿Qué diferencia FPIF de FFP?|Incentivos por desempeño y precio tope|Pago exclusivo por horas|Ausencia de obligación de entrega|Reembolso irrestricto|FPIF permite incentivos según métricas y fija un precio máximo.
Contrato largo expuesto a inflación con ajustes definidos. ¿Tipo?|FPEPA|CPAF|T&M sin límite|CPFF|Precio fijo con ajuste económico contempla mecanismos de ajuste previamente pactados.
¿Qué riesgo conserva el comprador en T&M?|Cantidad de horas y costo total variable|Imposibilidad de fijar tarifas|Pago total fijo por definición|Ausencia de supervisión|Las tarifas pueden ser fijas, pero el total depende de cantidades; convienen topes y control.
Objetivo de costo 1.000, honorario 100, vendedor recibe 20 % del ahorro; real 900. ¿Pago sin otros límites?|1.020|900|1.100|1.080|Ahorro=100; incentivo=20; honorario=120; pago=900+120.
¿Qué beneficio tiene una conferencia de oferentes?|Entendimiento común y trato equitativo|Adjudicar antes de recibir ofertas|Cambiar criterios sin informar|Garantizar menor precio|Aclara requisitos y consultas para los potenciales vendedores.
Dos proveedores tienen precios iniciales distintos. ¿Evaluación más completa?|Criterios publicados y costo del ciclo de vida|Precio inicial como único criterio siempre|Número de empleados como criterio exclusivo|Cambiar ponderaciones tras ver las ofertas|La selección considera requisitos técnicos, riesgo, operación y costos relevantes.
¿Qué hacer ante discrepancia sobre compensación de un cambio?|Documentar reclamación y aplicar mecanismos contractuales|Pagar sin verificar|Cerrar unilateralmente como rutina|Modificar línea base sin autorización|Las reclamaciones se documentan y gestionan; se prioriza negociación y mecanismos del acuerdo.
¿Qué evidencia permite el cierre normal?|Entregables aceptados, obligaciones y pagos resueltos, notificación formal|Solo software ejecutable|Solo una reunión interna|Solo consumo del presupuesto|El administrador autorizado verifica condiciones contractuales y comunica cierre formal.
¿Qué analiza hacer o comprar?|Costo completo, capacidad, riesgo y tiempo|Solo el precio del equipo|Solo la cantidad de proveedores|Solo la depreciación|Incluye costos de oportunidad, capacidad disponible y consecuencias del suministro."""
questions=[]
for idx,line in enumerate(new_rows.splitlines()):
    prompt,*parts=line.split('|');opts=parts[:4];offset=(idx*3+1)%4
    questions.append(dict(topic='Adquisiciones',prompt=prompt,options=opts[offset:]+opts[:offset],answer=(-offset)%4,explanation=parts[4]))
data['questions']=questions+data['questions'][15:]
replacements={
37:('Lecturas','Vendes por 2.500 un activo con valor libro 2.000; impuesto 15 %. ¿Caja neta?',['2.425','2.125','2.500','2.000'],'Ganancia=500; impuesto=75; venta neta=2.425.'),
39:('Lecturas','Venta 3.000, valor libro 4.000, tasa 15 %, base gravable suficiente. Efecto neto de venta…',['3.150','3.000','2.850','4.000'],'Pérdida contable=1.000; ahorro tributario=150; efecto incremental=3.150.'),
40:('Lecturas','IVA recuperable de una compra que se recupera meses después puede…',['Exigir financiamiento temporal','Ser siempre costo depreciable','Excluirse siempre de tesorería','Constituir una venta'],'El desfase compromete fondos aunque el impuesto se recupere.'),
42:('Lecturas','Proyecto reduce energía de 1.000 a 800; impuesto 20 % y utilidades suficientes. Ahorro neto…',['160','200','40','240'],'El ahorro bruto aumenta utilidad en 200; el impuesto aumenta 40; quedan 160.'),
43:('Lecturas','VP de beneficios 1.200 y VP de costos 1.000. Razón B/C y VAN…',['1,2 y 200','0,2 y 200','1,2 y 1.200','200 y 1,2'],'Beneficio/costo=1.200/1.000. VAN es diferencia, 200.'),
48:('Lecturas','Resultado operativo después de impuesto 150; capital 1.000; costo de capital 12 %. VEA básico…',['30','150','120','−30'],'Cargo de capital=120. Valor económico agregado=150−120=30.'),
49:('Lecturas','Evaluar un reemplazo mediante flujo incremental requiere…',['Flujo con proyecto menos flujo sin proyecto','Solo el costo original hundido','Sumar íntegramente ambos escenarios','Excluir la venta del activo antiguo siempre'],'Se identifican cambios en inversión, operación, impuestos, venta y valores finales.')
}
for idx,(topic,prompt,opts,exp) in replacements.items():
    off=(idx*3+1)%4
    data['questions'][idx]=dict(topic=topic,prompt=prompt,options=opts[off:]+opts[:off],answer=(-off)%4,explanation=exp)
data['exam'][0]=dict(title='Adquisición con alcance incierto',points=10,prompt='Se necesita diagnosticar e integrar un sistema legado sin documentación. Proveedor A ofrece FFP de 800 UF excluyendo interfaces no identificadas. B ofrece T&M a 2 UF/HH con tope de 900 y revisión semanal. Compara alternativas, propone qué información pedir, contenido mínimo del SOW, criterios de selección, controles y condiciones de cierre. Justifica qué aceptarías y con qué condiciones.',rubric=['Reconoce incertidumbre y exclusiones; costo total y riesgo no se deducen solo de 800 frente a 900 (2).','Propone RFI o diagnóstico previo y RFP para enfoques; justifica elección (2).','SOW con entregables, interfaces, aceptación, responsabilidades y gestión de cambios (2).','T&M con topes, evidencia de horas, hitos y aprobación; o FFP tras delimitar alcance (2).','Selección transparente y cierre con entregables aceptados, pagos y reclamaciones resueltos (2).'])
data['exam'][5]=dict(title='Lecturas · reemplazo y efectos tributarios',points=15,prompt='Empresa con utilidades suficientes evalúa reemplazar equipo. Compra nuevo por 5.000 UF en año 0 y vende antiguo por 1.000, cuyo valor libro es 600. Tasa de impuesto 25 %. Ahorro anual de operación 800 y depreciación incremental anual 200. Sin cambio de ingresos ni capital de trabajo. Calcula inversión inicial neta y flujo incremental operativo. Explica el tratamiento de un estudio hundido de 100 y de IVA recuperable pagado hoy y recuperado en seis meses. Distingue recuperación simple y descontada.',rubric=['Venta neta=1.000−(1.000−600)×0,25=900; flujo inicial=−4.100 (4).','Utilidad incremental=800−200=600; impuesto adicional=150; flujo=600−150+200=650 (4).','Estudio ya pagado irrecuperable se excluye de la decisión futura (2).','IVA recuperable genera necesidad temporal de fondos; registrar pago y recuperación para caja (3).','PRI simple acumula sin actualizar; descontado incorpora tasa exigida (2).'])
assert len(data['questions'])==50 and sum(x['points'] for x in data['exam'])==100
(root/'datos_practica_fep.json').write_text(json.dumps(data,ensure_ascii=False),encoding='utf-8')
