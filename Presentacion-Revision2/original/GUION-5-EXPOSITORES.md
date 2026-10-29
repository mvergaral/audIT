# Guion oral · Revisión 2 · cinco expositores

**Duración prevista:** 14:25 de exposición + 0:35 de margen, seguidos por 15 minutos de preguntas. Los tiempos son una pauta de ensayo, no una promesa de duración automática. Sustituir «Expositor 1–5» por la distribución real del equipo solo en este guion interno. En la presentación corporativa no se agregan nombres personales.

| Voz | Diapositivas | Tramo previsto | Tema |
| --- | --- | --- | --- |
| Expositor 1 | 1–4 | 0:00–2:30 | Problema, solución y arquitectura |
| Expositor 2 | 5–7 | 2:30–5:30 | Correcciones, calidad y método de riesgos |
| Expositor 3 | 8–10 | 5:30–8:30 | Riesgos de solución, AMFE e implantación |
| Expositor 4 | 11–12 y primera mitad de 13 | 8:30–11:15 | EDT, paquete 11.1 y primera etapa del cronograma |
| Expositor 5 | Segunda mitad de 13 y 14–16 | 11:15–14:25 | Segunda etapa, hitos, síntesis y preguntas |

Las indicaciones entre **[corchetes]** son para ensayar; no se pronuncian. Cada persona debe mirar al público y usar la diapositiva como evidencia, sin leer sus tarjetas palabra por palabra. Avanzar las revelaciones al llegar a la idea correspondiente. Quien termina entrega la voz sin que la siguiente persona repita la conclusión anterior.

## Expositor 1 · 0:00–2:30

**Diapositiva 1 · Portada · 15 s**

«Buenos días. Presentamos la segunda revisión de nuestra propuesta para Transportes Curimón. Revisaremos las correcciones del primer informe, los riesgos de la solución y del proyecto, y cómo la EDT y los hitos gobiernan la ejecución.»

**Diapositiva 2 · Salida segura · 30 s**

«Partimos de una decisión operacional: un viaje no debe liberarse solo porque el camión esté listo. La salida exige tres evidencias vigentes: conductor habilitado, vehículo conforme y documento íntegro disponible en cabina. [Revelar cada control.] Si alguna falla, la orden queda bloqueada. Ese es el problema que organiza el resto de la solución.»

**Diapositiva 3 · Recorrido del viaje · 45 s**

«La información nace en la cabina, pasa por el terminal y llega a la torre de control. [Seguir el recorrido del diagrama.] El terminal valida y sincroniza incluso cuando el enlace se interrumpe; la torre reúne la evidencia para coordinar el viaje. Desde allí se integran los sistemas externos: el ERP contable sigue siendo el emisor tributario, y se conectan posicionamiento y transportistas. Así evitamos presentar módulos aislados: mostramos un recorrido completo del dato.»

**Diapositiva 4 · Arquitectura · 60 s**

«La arquitectura tiene tres capas. [Señalar la primera.] En el borde proponemos 374 gateways, 61 interfaces CANclick de lectura no invasiva y un buffer local de 8 GB para conservar eventos durante zonas sin cobertura. [Señalar la segunda.] En la nube, la ingesta asíncrona desacopla la telemetría; la continuidad en San Bernardo incluye enlaces y respaldo eléctrico, con una contingencia regional documentada que aún debe acreditarse. [Señalar la tercera.] En datos, EvidenciaJornada vincula conductor, vehículo, documento y huella de autorización. La migración considera un histórico del orden de 96 mil viajes por año. Con esta base, pasamos a lo corregido respecto del Informe 1.»

## Expositor 2 · 2:30–5:30

**Diapositiva 5 · Correcciones del Informe 1 · 60 s**

«Las observaciones 37 y 43 exigían decisiones explícitas. [Señalar ambos recuadros.] La 37 se aborda con el esquema extremo a extremo entre cabina, terminal, torre y ERP. La 43 define el futuro del sistema de 2013: sustitución progresiva por funciones, manteniendo el ERP como emisor tributario y la consulta histórica durante la transición. [Seguir la cadena inferior.] La observación 48 se responde con trazabilidad: el requisito RNF-011 se relaciona con el paquete EDT 11.2 y con los casos CP-INT-05 y CP-SYS-05. Esos casos están diseñados; su ejecución y sus actas corresponden a la fase contractual.»

**Diapositiva 6 · Metodología y calidad · 60 s**

«El desarrollo combina iteraciones de dos semanas con control formal de cambios. Antes de liberar a producción, se evalúa el impacto en plazo, red y seguridad; el umbral propuesto para cambios fallidos es de hasta cinco por ciento mensual. [Pasar al centro.] Las compuertas de calidad cubren hardware embarcado, telemetría, software, seguridad y recepción del montaje. [Pasar al gráfico.] El plan T-17 distribuye 120 casos diseñados entre pruebas unitarias, de integración, de sistema y de aceptación en terreno. El criterio decisivo no es el volumen de pruebas: los casos críticos deben salir sin defectos de severidad S1 o S2.»

**Diapositiva 7 · Método de riesgos · 60 s**

«Para comparar riesgos usamos una escala ordinal de probabilidad por impacto, de uno a cinco en cada eje. Distinguimos solución, desarrollo e implantación porque fallan por causas y responsables distintos. [Señalar los tres desplazamientos.] Con controles definidos, la exposición estimada del documento en ruta baja de 12 a 8; la capacitación, de 8 a 4; y la adhesión de transportistas, de 12 a 8. Estos números priorizan atención: no son porcentajes ni resultados medidos en operación. En particular, un impacto alto sigue exigiendo contingencia aunque baje la probabilidad. Ahora veremos los riesgos concretos.»

## Expositor 3 · 5:30–8:30

**Diapositiva 8 · Riesgo de la solución · 60 s**

«El riesgo R-28 aparece cuando un documento emitido por el ERP debe volver íntegro a la cabina en una ruta con cobertura variable. [Seguir origen, enlace y cabina.] La propuesta usa conmutación LTE/satélite, fragmentación con acuse y una verificación bloqueante en la tablet. Cuando se conoce la carga en planta, la preemisión reduce exposición. El objetivo de 90 segundos es un presupuesto extremo a extremo sujeto a ensayo; no afirmamos que ya esté acreditado en terreno. Si el documento no está conforme, el viaje no sale. El responsable de integración debe activar el tratamiento ante exceso de tiempo o pérdida de fragmentos.»

**Diapositiva 9 · AMFE técnico · 60 s**

«El AMFE añade una mirada de falla técnica: severidad, ocurrencia y capacidad de detección se combinan en el número de prioridad de riesgo. [Recorrer las barras.] Equipo a bordo sin registro marca NPR 36 y requiere watchdog más alerta de latido; módem sin servicio marca 32 y se enfrenta con buffer y enlace alternativo; respaldo eléctrico marca 18 y exige prueba automatizada. Los tres casos quedan bajo el umbral de priorización 50 del análisis. Eso no significa riesgo nulo: el punto de diseño es detectar temprano y actuar antes de que la falla afecte la operación.»

**Diapositiva 10 · Riesgos de implantación · 60 s**

«La implantación depende de tres corrientes que deben converger. [Revelar cada entrada antes de las flechas.] Primero, adhesión: al corte M9 se busca contar al menos 60 anexos firmados de 148 transportistas; si son 59 o menos, se activa apoyo legal y comercial. Segundo, montaje: se controla la cobertura acumulada por camión y se coordinan cuadrillas en terminales. Tercero, marcha blanca: se verifican criterios y se conserva la posibilidad de reversión. [Mostrar las flechas.] Solo cuando convergen estas evidencias se solicita aceptación formal para producción en las etapas E1 y E2. La siguiente pregunta es cómo se distribuye y controla ese trabajo.»

## Expositor 4 · 8:30–11:15

**Diapositiva 11 · EDT · 60 s**

«La EDT divide la propuesta en 54 paquetes de trabajo agrupados en 13 áreas. Cada paquete identifica un entregable verificable, un criterio de aceptación y un responsable. [Señalar área 11.] Implantación no queda como una actividad genérica: se descompone para poder programarla y aceptarla. [Señalar área 12.] Las cinco fichas de innovación se integran en la misma estructura y su piloto se sitúa entre M13 y M15; sus beneficios deberán contrastarse con una línea base en terreno. La EDT conecta el alcance prometido con la red de trabajo.»

**Diapositiva 12 · Paquete 11.1 y G13 · 60 s**

«Un ejemplo es el paquete 11.1, capacitación operacional. Su entregable incluye manuales por perfil, entorno de práctica y asistencia. La aceptación exige la compuerta G13 aprobada y evaluación práctica de al menos 80 por ciento por rol. [Seguir la secuencia.] G13 requiere una versión probada en PREPROD, datos y material antes de iniciar A13. A13 contempla 40 días hábiles: diez de familiarización y treinta de práctica y evaluación. Si G13 no está aceptada, la capacitación no comienza. La reserva A14 protege la red, pero no elimina esta precedencia.»

**Diapositiva 13 · Cronograma, primera parte · 45 s**

«El cronograma muestra dos etapas y meses contractuales relativos al inicio. [Señalar E1.] La primera construye borde y servicios, pasa a marcha blanca entre M13 y M15 y busca aceptación para producción en M16. Durante el solapamiento M13–M15, una célula atiende la marcha blanca y el soporte de E1 mientras otra continúa la construcción de E2. Esa división evita prometer a la misma capacidad simultáneamente en dos frentes. [Entregar la voz sin cambiar de diapositiva.]»

## Expositor 5 · 11:15–14:25

**Diapositiva 13 · Cronograma, segunda parte · 45 s**

«Retomo desde E2. Su construcción corre en paralelo, pero su marcha blanca se programa entre M19 y M20; la aceptación de producción se ubica en M21. [Señalar el extremo derecho.] La operación se proyecta hasta M56 y el legado de 2013 permanece consultable durante la transición hasta M24. Así, M16 y M21 son hitos de aceptación distintos, no una sola puesta en marcha. Los meses se fijarán en calendario desde el inicio contractual.»

**Diapositiva 14 · Hitos y reservas · 90 s**

«La red avanza por evidencia. [Recorrer los hitos en orden.] G13 habilita la capacitación; H6 abre la marcha blanca de la primera etapa; H7 formaliza su aceptación en M16. Después, H11 abre la marcha blanca de E2 y H12 formaliza la aceptación final en M21. Las reservas A14, de 14 días, y A23, de 10 días, protegen actividades de la red. Hay una distinción importante: consumir reserva u holgura interna no cambia por sí solo la fecha contractual de H7 o H12. Si una compuerta falla, se aplica control de cambios y se evalúa el efecto real; no se da el hito por cumplido. Esto permite exponer la planificación como una secuencia gobernable y verificable, no solo como una barra de tiempo.»

**Diapositiva 15 · Síntesis · 45 s**

«Cerramos con tres compromisos. Primero, una solución trazable: arquitectura, correcciones y evidencia desde la salida del viaje hasta las pruebas diseñadas. Segundo, riesgos y calidad con responsables, controles y umbrales explícitos; las exposiciones residuales siguen siendo estimaciones. Tercero, ejecución controlada: 54 paquetes, compuertas de aceptación, dos etapas y reservas identificadas. Cada afirmación importante tiene una ruta hacia el informe o sus formularios. Ese es el criterio con que proponemos evaluar la solución.»

**Diapositiva 16 · Preguntas · 10 s**

«Muchas gracias. Disponemos de quince minutos para preguntas y discusión; podemos abrir el respaldo técnico si desean profundizar en algún punto.»

## Ensayo y preguntas

Hacer al menos un ensayo completo con cronómetro y otro en el proyector disponible. Si un bloque se extiende, recortar ejemplos secundarios antes que las salvedades «diseñado, no ejecutado», «estimado, no medido» y «mes contractual relativo». Cada expositor debe saber qué diapositiva recibe y cuál entrega. Para preguntas, responder primero con la conclusión, luego señalar la evidencia del informe o formulario; si un resultado requiere ensayo futuro, decirlo expresamente.
