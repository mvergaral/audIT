# Guion oral · Revisión 2 · cinco expositores

**Duración prevista:** 14:49 de exposición + 0:11 de margen, seguidos por 15 minutos de preguntas. Los tiempos son una pauta de ensayo, no una promesa de duración automática. Sustituir «Expositor 1–5» por la distribución real del equipo solo en este guion interno. En la presentación corporativa no se agregan nombres personales.

| Voz | Diapositivas | Tramo previsto | Tema |
| --- | --- | --- | --- |
| Expositor 1 | 1–7 | 0:00–3:23 | Problema, correcciones y arquitectura lógica |
| Expositor 2 | 8–11 | 3:23–5:53 | Arquitectura física, equipo a bordo, datos y desconexión |
| Expositor 3 | 12–15 | 5:53–8:11 | EDT: niveles 0–2, diccionario y regla del 100 % |
| Expositor 4 | 16–19 | 8:11–11:06 | Carta Gantt, qué pasa si, G13 y transición |
| Expositor 5 | 20–26 | 11:06–14:49 | Riesgos, reservas, cierre y preguntas |

Las indicaciones entre **[corchetes]** son para ensayar; no se pronuncian. Cada persona mira al público y usa la lámina como evidencia, sin leer palabra por palabra. Los relevos se realizan en los límites de la tabla anterior; los separadores introducen cada acto. Las marcas rojas «✓ Obs.» de la arquitectura indican la observación del Informe 1 que esa vista resuelve: se nombran sólo si hay tiempo o si la comisión pregunta.

## Expositor 1 · 0:00–3:23

**Diapositiva 1 · Portada · 10 s**

«Buenos días. Presentamos la segunda revisión de nuestra propuesta para Transportes Curimón. Revisaremos las correcciones del primer informe, los riesgos de la solución y del proyecto, y cómo la EDT y los hitos gobiernan la ejecución.»

**Diapositiva 2 · Salida segura · 25 s**

«Partimos de una decisión operacional: un viaje no debe liberarse solo porque el camión esté listo. La salida exige tres evidencias vigentes: conductor habilitado, vehículo conforme y documento íntegro disponible en cabina. [Revelar cada control.] Si alguna falla, la orden queda bloqueada. Ese es el problema que organiza el resto de la solución.»

**Diapositiva 3 · Cambios principales del Informe 2 · 40 s**

«Seleccionamos cinco cambios principales respecto del primer informe. [Requisitos y arquitectura.] El catálogo ahora traza 42 requisitos hasta pruebas diseñadas, y la arquitectura define esquema, capas y equipos. [Revelar legado y capacidad.] Resolvimos el futuro del sistema de 2013 mediante sustitución gradual y consulta hasta M24. También derivamos la memoria y la capacidad de reconexión. [Revelar innovaciones.] Reformulamos las innovaciones 2 y 3 y entregamos las cinco fichas. La matriz del Artículo 46 conserva el detalle. Las pruebas siguen pendientes de ejecución. Ahora profundizamos en la solución.»

Referencia para preguntas: observaciones 01/38/45/48, S3 §3.2.8 y T-12/T-17; 37/53/64/65, S3 §3.3 y S4 §§4.1.3/4.2 con T-11; 43, S3 §3.2.4; 73/74, S4 §§4.2.2/4.2.8 y CP-PERF-02; 88–91, S13 §§13.2–13.3 y T-19. Se priorizaron decisiones de alcance, viabilidad y verificación. La selección no acredita cierre de las 100 observaciones. La innovación 2 programa intervenciones por oportunidad de patio y la 3 conecta el semirremolque. El ERP contable se conserva como emisor tributario; M16 y M21 marcan la sustitución por funciones del sistema de gestión.

**Diapositiva 4 · Separador: Qué construimos · 3 s**

[Lámina de transición: avanzar enseguida.]

**Diapositiva 5 · Contexto y tres planos · 40 s**

«Abrir con el mapa completo. [Nube.] El núcleo vive en Chile Central, en tres zonas; Brazil South queda para recuperación. [Sitio.] San Bernardo sostiene la torre sin enlace y la integración con el contable, que sigue siendo el único emisor. Cada terminal tiene dos nodos y respaldo 5G. [Flota.] Los 182 camiones con equipo audIT conviven con 192 de terceros que conservan el suyo. [Componentes.] Son 39 componentes: 24 en la región primaria, uno en la secundaria y 14 fuera de la nube.»

**Diapositiva 6 · Arquitectura lógica · 45 s**

«Recorrer la pila. [Capas.] Portales Next.js y app Flutter; Front Door como borde público; API Management; seis contextos de negocio en AKS sobre .NET; IoT Hub y Event Hubs para ingesta; y persistencia según cada dato. [Transversales.] Entra ID y Key Vault aportan seguridad, Azure Monitor observabilidad. [Contextos.] Cada contexto decide sobre su negocio y sus datos: Planificación pregunta a Personas y Flota. Sus nombres coinciden con los paquetes 5.1 a 5.6 de la EDT.»

**Diapositiva 7 · Verificación en 30 s · 40 s**

«Seguir una petición real por la pila. [Solicitud.] La torre pide asignar conductor, tracto, semirremolque y carga. [Invariantes.] Planificación evalúa en paralelo tres condiciones y pregunta a quien es dueño de cada dato: Personas, Flota y el documento del contable. Una causa legal bloquea siempre, y el rechazo explica por qué. [Presupuesto.] El Caso da 30 segundos: dos para identidad, ocho para las tres evaluaciones en paralelo, ocho para reservar y confirmar, cuatro para veredicto y auditoría, tres para responder, y cinco de margen. [Cierre.] Ojo: es un reparto de diseño, todavía sin medición.»

## Expositor 2 · 3:23–5:53

**Diapositiva 8 · Arquitectura física · 45 s**

«Bajar de la idea al equipo. [Nube.] Lo que se contrata en Azure, por subred, y Brazil South con RPO de 15 minutos y RTO de 4 horas. [Sitios.] San Bernardo va en pares: dos servidores R360, dos FortiGate, clima N+1, detección por aspiración y grupo electrógeno. Cada terminal tiene dos Karbon 430 en activo y espera y un router 5G. El camión lleva el G26I, el módem Iridium, el lector CAN sin contacto y el lector de tarjeta. [Enlaces.] Cada enlace tiene medio, respaldo y tiempo de conmutación: ExpressRoute de 100 Mbit/s con VPN de respaldo en menos de un minuto; terminal fijo con 5G; camión LTE con Iridium. [Cierre.] Cinco ambientes desde el mismo código. Todo el hardware lo compra el mandante; el detalle y las cantidades están en el T-11.»

**Diapositiva 9 · El camión · 35 s**

«El Caso pide tratar el equipo a bordo como un componente on-premise distribuido. [Equipo.] Es un iWave G26I: Linux, tres buses CAN, LTE, GNSS y un elemento seguro para arranque y claves; aguanta la cabina. [Periféricos.] Cada uno responde a una restricción: el CANCrocodile lee el bus sin cortar cables, para no tocar la garantía; el lector MIFARE identifica al conductor con el camión detenido; el Iridium cubre los tramos sin señal; y la baliza comprueba qué semirremolque va acoplado. [Memoria.] La observación 73 pidió derivar los 8 GB: se necesitan 2.374 MB, y el búfer de 288 horas para el cierre de Los Libertadores pesa menos del 2 %.»

**Diapositiva 10 · Datos · 40 s**

«Cada dato tiene su motor. [Dominios.] PostgreSQL confirma asignaciones y vigencias; SQLite captura a bordo; TimescaleDB conserva telemetría. La caché nunca habilita con una copia vieja. Documentos y auditoría quedan inmutables y la analítica se separa del despacho. [Volumen.] Se dimensionan 96 mil viajes y cerca de 120 millones de posiciones al año. [Migración.] Cuatro fases y 6.000 vigencias verificadas una a una: nada en cuarentena habilita un despacho.»

**Diapositiva 11 · Sin enlace · 30 s**

«Cortar los enlaces en la misma vista. [Corte.] Lo que exige estado global, asignar un viaje nuevo y emitir el documento, sigue pasando por el servicio central: no se inventan vigencias ni asignaciones. [Autonomía.] San Bernardo y los terminales operan 24 horas: la torre, las emergencias, la consulta de vigencias en portería. El camión guarda al menos 72 horas, y el diseño llega a 288. [Reconexión.] Al volver la señal se sube por lotes con acuse, y la prueba CP-PERF-02 exige 20 minutos para 300 camiones. Este es el puente con los riesgos: estas mismas piezas son las barreras del R-28.»

## Expositor 3 · 5:53–8:11

Este tramo es el que más pesa en la evaluación (S7, 15 %). Quien lo exponga debe dominar el árbol sin leerlo: señalar, no recitar paquetes.

**Diapositiva 12 · Separador: Cómo lo ejecutamos · 3 s**

[Lámina de transición: avanzar enseguida. Aquí cambia la voz.]

**Diapositiva 13 · EDT, niveles 0 y 1 · 40 s**

«La EDT parte de un solo nivel 0: la plataforma de control de jornada, flota y viaje para Curimón. [Revelar nivel 1.] Se descompone en trece elementos orientados a entregables, no a fases: cada uno termina en algo que el mandante recibe y puede verificar. [Revelar paquetes.] Cada elemento baja a paquetes estimables y asignables; son 54 en total. El elemento 5 es el más grande porque tiene un paquete por cada contexto de la arquitectura. [Revelar agrupación.] Los elementos 1 a 6 construyen la Etapa 1; del 7 al 13 la acompañan, certifican y operan. Y se cumple la regla del 100 %: la suma de los hijos es el padre, sin vacíos ni dobles conteos.»

**Diapositiva 14 · EDT, nivel 2 · 50 s**

«Este es el árbol completo a nivel de paquete. [Columnas 1 y 2.] A la izquierda, lo que construye la Etapa 1: gestión, levantamiento, plataforma, equipo a bordo, servicios e integraciones. [Revelar columnas 3 y 4.] A la derecha, datos y migración, la Etapa 2, adhesión, calidad, implantación, innovaciones y la operación de 36 meses. [Revelar trazabilidad.] Quiero destacar tres decisiones de diseño. Primero, los paquetes 5.1 a 5.6 llevan el nombre de los seis contextos del Subdocumento 4: cada componente de la arquitectura tiene un único paquete que lo construye. Segundo, 12.1 a 12.5 son las cinco fichas de innovación del T-19, con los mismos nombres. Tercero, la adhesión de transportistas es un elemento propio, con responsable y riesgo, porque el Caso exige tratarla como actividad y no como supuesto. El elemento 11 es el que produce las actas de los hitos de marcha blanca.»

**Diapositiva 15 · Diccionario y regla del 100 % · 45 s**

«Cada paquete está definido en el diccionario del T-14. Tomemos el 11.2, marcha blanca de la Etapa 1. [Revelar.] Su entregable es la marcha blanca y el paso a producción de la Etapa 1; se acepta solo si se cumplen las seis condiciones del Artículo 17.3, que se acreditan en los hitos H6 y H7. [Revelar.] Tiene un único responsable, el Líder de Implantación, y se ubica en la red en las actividades A15 y A19, meses 13 a 16. Es también el paquete al que llega la traza de la observación 48: RNF-011, paquete 11.2, casos CP-INT-05 y CP-SYS-05. [Revelar.] Por último, comprobamos la regla del 100 % contra el alcance: 42 requerimientos, seis contextos, cinco innovaciones y once exigencias del Caso. Ninguno quedó sin paquete.»

## Expositor 4 · 8:11–11:06

**Diapositiva 16 · Carta Gantt y dependencias · 75 s**

«La EDT dice qué; la red del T-15 dice cuándo y en qué orden. [Barras.] Son 25 actividades en días hábiles, del día 0 al 420, que es el fin del mes 21. [Dependencias.] Cada línea es una precedencia fin a inicio. Por ejemplo, la certificación de la Etapa 1, A12, no puede partir hasta que terminen la migración, la construcción, las integraciones y el piloto a bordo. [Ruta crítica.] En rojo está la ruta crítica: trece actividades sin holgura, desde el inicio hasta la certificación de la Etapa 1, la reserva A14, y luego el diseño, la construcción y la certificación de la Etapa 2, la reserva A23 y la marcha blanca y paso a producción finales. Un atraso en la construcción de la Etapa 1 llega intacto hasta el mes 21. Las líneas punteadas son holguras: la marcha blanca de la Etapa 1 no está en la ruta y tiene 20 días. [Hitos.] Los rombos son los hitos del Formulario E-25; todos caen dentro de su mes contractual.»

**Diapositiva 17 · ¿Y si A09 se atrasa? · 35 s**

«Poner la red a prueba con una pregunta que la comisión suele hacer. [Plan.] La cadena crítica de la Etapa 1: ambientes, construcción, certificación y la reserva A14 antes del inicio fijo de la marcha blanca en el día 240. [Atraso.] Si la construcción se atrasa 10 días, la certificación se corre y la reserva baja de 14 a 4 días. [Efecto.] H5 y H6 se cumplen igual: para eso existe la reserva. Pero H4, el fin de la construcción, tiene límite el día 200 y queda dos días tarde: la reserva protege la marcha blanca, no los hitos de pago, y eso es justamente el riesgo R-17. El consumo de más de la mitad de A14 activa el R-16.»

**Diapositiva 18 · Paquete 11.1 y G13 · 35 s**

«Un ejemplo es el paquete 11.1, capacitación operacional. Su entregable es la capacitación de torre, terminales y conductores. Se acepta con G13 disponible antes de A13 y con los usuarios certificados. [Seguir la secuencia.] G13 requiere una versión probada en PREPROD, datos y material antes de iniciar A13. A13 contempla 40 días hábiles: diez de familiarización y treinta de práctica y evaluación. Si G13 no está aceptada, la capacitación no comienza. La reserva A14 protege la red, pero no elimina esta precedencia.»

**Diapositiva 19 · Transición en dos etapas · 30 s**

«A escala de meses, esto se ve así. [Señalar E1.] La Etapa 1 pasa a marcha blanca entre M13 y M15 y a producción en M16; durante ese solapamiento una célula atiende la marcha blanca y otra construye la Etapa 2, para no sobreasignar a nadie. [Señalar E2.] La Etapa 2 tiene su marcha blanca en M19 y M20 y su aceptación en M21. La operación sigue hasta M56 y el sistema de 2013 queda en consulta hasta M24.»

## Expositor 5 · 11:06–14:49

**Diapositiva 20 · Separador: Cómo lo protegemos · 3 s**

[Lámina de transición: avanzar enseguida. Aquí cambia la voz.]

**Diapositiva 21 · Mapa de calor P×I · 50 s**

«Partir por el panorama completo. [Mapa.] Probabilidad por impacto, de 1 a 5; el color sigue la escala del S8. [Riesgos.] Los 28 riesgos del T-16 en su celda inicial: la mayoría se concentra en exposición media; siete quedan en alta, y uno, el R-06, llega a 15. [Antes y después.] Después de mitigar, ninguno queda en alta. [Cierre.] Las categorías: técnicos, contrapartes, gestión, ciberseguridad y continuidad. Lo residual es una estimación, no una medición.»

**Diapositiva 22 · Riesgos de exposición alta · 50 s**

«Bajar a los siete de exposición alta, sin leer la tabla. [Primeros.] El más alto es R-06: Microsoft retira Azure Cache for Redis justo en el mes 20; se evita desde el diseño naciendo en Azure Managed Redis, y baja de 15 a 3. R-11, la adhesión, se vigila con un corte en el mes 9. [Medio.] Dos son de ciberseguridad y datos: el portal expuesto y la réplica de datos personales en Brazil South, que exige aprobación del mandante en el H2. [Últimos.] La marcha blanca en temporada, el bloqueo indebido de un viaje, que se calibra con la prueba en paralelo, y el R-28, que vemos a continuación.»

**Diapositiva 23 · Corbatín de R-28 · 50 s**

«Este es el riesgo que dio origen al bloqueo de salida. [Evento.] Que el documento completo no vuelva a la cabina en 90 segundos. [Causas.] Cuatro caminos: no hay LTE, la carga se conoce sólo en terreno, el documento no cabe en un mensaje satelital o se pierden fragmentos. [Prevención.] Cada uno tiene su barrera: el Iridium, la emisión anticipada, el protocolo fragmentado con integridad y un ensayo en el mes 3 con el peor documento. [Mitigación.] Si aun así ocurre, el camión no sale sin documento conforme, y si el ensayo supera 90 segundos se revisa la decisión de diseño. [AMFE.] Los diez modos de falla quedan bajo 50; los dos más altos se tratan detectando antes.»

**Diapositiva 24 · Reservas y holguras · 40 s**

«El riesgo de plazo también se trata con números del plan. [Revelar reservas.] A14 protege la Etapa 1 con 14 días hábiles: dos desviaciones estándar de su cadena crítica, un 97,9 % de probabilidad de llegar al mes 13. A23 protege la Etapa 2 con 10 días y un 97,6 %. Las dos fechas a la vez: 95,6 %. Y hay una regla: si una reserva baja de la mitad cuando a su cadena le queda más de la mitad, el caso sube al Comité Ejecutivo. [Revelar holguras.] Lo que no controla audIT quedó fuera de la ruta crítica: la factibilidad con terceros puede atrasarse 61 días; un cierre del paso Los Libertadores, unos 9 días hábiles, cabe en la holgura del piloto y de la instalación. Consumir holgura no mueve las fechas contractuales.»

**Diapositiva 25 · Tres compromisos · 20 s**

«Proponemos una arquitectura híbrida, 54 paquetes verificables y 28 riesgos tratados. Las reservas protegen la ejecución. Los 120 casos de prueba están diseñados y su ejecución corresponde a la fase contractual. Gracias.»

**Diapositiva 26 · Preguntas · 10 s**

«Muchas gracias. Abrimos los quince minutos de preguntas y discusión.» [Si una pregunta lo requiere, la tecla B abre el respaldo y Escape vuelve.]

## Ensayo y preguntas

Hacer al menos un ensayo completo con cronómetro y otro en el proyector disponible. Si un bloque se extiende, recortar ejemplos secundarios antes que las salvedades «diseñado, no ejecutado», «estimado, no medido» y «mes contractual relativo». Cada expositor debe saber qué diapositiva recibe y cuál entrega. Para preguntas, responder primero con la conclusión, luego señalar la evidencia del informe o formulario; si un resultado requiere ensayo futuro, decirlo expresamente.
