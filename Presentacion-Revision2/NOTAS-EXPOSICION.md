# Guion de exposición

Objetivo: 14 minutos y 49 segundos + 11 segundos de margen. No hay asignación ficticia de expositores.

## 1. Revisión 2 · Caso Transporte de Carga

Tiempo: 10 s.

Presentar el alcance de la revisión: correcciones del Informe 1, riesgos de solución, proyecto e implantación, EDT, planificación e hitos. La exposición dura 15 minutos y deja 15 minutos para preguntas.

Fuente: Transportes Curimón · TFEP-01/2026 · audIT Soluciones Tecnológicas SpA

## 2. Una salida segura exige información confiable.

Tiempo: 25 s.

Abrir desde la operación real. El camión se desplaza sobre un carril dedicado mientras se activan los tres controles bloqueantes inferiores: conductor, vehículo y documento deben aportar evidencia válida antes de autorizar la salida.

Fuente: S2 · S3 §3.3 · S8: verificación bloqueante de salida

## 3. Cambios principales del Informe 2

Tiempo: 40 s.

Síntesis de 40 segundos. [Vista inicial: requisitos y arquitectura.] El Informe 2 incorpora el catálogo T-12 de 42 requerimientos trazados a componentes, paquetes y pruebas diseñadas; S3 §3.2.8 y T-17 responden a las observaciones 01, 38, 45 y 48. El esquema conceptual de S3 §3.3 y las capas, interfaces y arquitectura física de S4 §§4.1.3 y 4.2 responden a 37, 53, 64 y 65, con el catálogo T-11. [Revelar legado y capacidad.] S3 §3.2.4 resuelve la observación 43 con sustitución por funciones en M16 y M21, consulta hasta M24 y conservación del ERP contable como único emisor tributario. S4 §§4.2.2 y 4.2.8 deriva memoria y reconexión para 73 y 74; T-17 CP-PERF-02 define el ensayo del proceso completo. [Revelar innovaciones.] Para 88–91, S13 §§13.2–13.3 reformula la programación por oportunidad de patio y el semirremolque conectado; T-19 entrega cinco fichas con los elementos exigidos. Se priorizan cambios que definen el alcance, la viabilidad y la verificación de la propuesta. Las correcciones editoriales permanecen en la matriz completa y las novedades de EDT y riesgos se explican en sus bloques. La selección no acredita cierre integral de las 100 observaciones ni ejecución de las pruebas. El respaldo de correcciones amplía 37, 43 y 48.

Fuente: Matriz Art. 46 · S3 · S4 · S13 · T-11 / T-12 / T-17 / T-19

## 4. Qué construimos

Tiempo: 3 s.

Separador. Cambio de voz: el expositor 1 presenta el problema y la arquitectura de alto nivel.

Fuente: S4 y S5

## 5. La solución es híbrida: nube, sitio y flota.

Tiempo: 40 s.

Abrir con el mapa completo. [Nube.] El núcleo vive en Azure Chile Central, en tres zonas: Front Door, API Management, los seis contextos en AKS, IoT Hub y Event Hubs para la ingesta, PostgreSQL con TimescaleDB, Managed Redis y Storage; Brazil South espera como recuperación. [Sitio.] San Bernardo no aloja el núcleo: mantiene viva la torre si cae el enlace y aloja la capa anticorrupción junto al sistema contable, que sigue siendo el único emisor. Cada terminal tiene dos nodos en activo y espera y un router 5G. [Flota.] 182 camiones llevan el equipo audIT; los 192 de terceros no se intervienen y llegan por la plataforma de su proveedor. [Componentes.] Son 39 componentes: 24 en la región primaria, uno en la secundaria y 14 fuera de la nube. Por eso es híbrida, como exige el Artículo 16.

Fuente: S4 §4.2, Tabla de planos y §4.2.3: 39 componentes (24 + 1 + 14) · T-11 · FEP01 Art. 16.1 a 16.4 · Caso RT-06.01 · íconos: Azure Architecture Icons y Simple Icons

## 6. Ocho capas, cada una con su producto.

Tiempo: 45 s.

Recorrer la pila de arriba abajo, nombrando el producto, no el concepto. [Capas.] Portales en Next.js y React, app Flutter; Front Door con cortafuegos como único punto público; API Management con certificado mutuo; los servicios de negocio en AKS en tres zonas sobre .NET 10 LTS; IoT Hub y Event Hubs con protocolo Kafka para la ingesta, escrita en Go; y una capa de datos políglota. [Transversales.] Seguridad, con Entra ID y Key Vault, y observabilidad, con Azure Monitor, no son un piso más: atraviesan todos. [Contextos.] El negocio son seis contextos; cada uno decide una sola cosa y tiene sus propios datos: Planificación pregunta a Personas y a Flota, no lee sus bases. Son los mismos nombres de los paquetes 5.1 a 5.6 de la EDT.

Fuente: S4 §4.1.1: productos y soporte · §4.1.3: las ocho capas (FEP02 2.1, RT-02.01) · §4.1.4: seis contextos delimitados · ISO/IEC/IEEE 42010

## 7. Un viaje se autoriza o se bloquea en 30 segundos.

Tiempo: 40 s.

Seguir una petición real por la pila. [Solicitud.] La torre pide asignar conductor, tracto, semirremolque y carga. [Invariantes.] Planificación evalúa en paralelo tres condiciones y pregunta a quien es dueño de cada dato: Personas, Flota y el documento del contable. Una causa legal bloquea siempre, y el rechazo explica por qué. [Presupuesto.] El Caso da 30 segundos: dos para identidad, ocho para las tres evaluaciones en paralelo, ocho para reservar y confirmar, cuatro para veredicto y auditoría, tres para responder, y cinco de margen. [Cierre.] Ojo: es un reparto de diseño, todavía sin medición.

Fuente: S4 §4.1.9 y Tabla 4.3: presupuesto de diseño de la asignación · Caso RT-09.01, p. 32 · S3: RN-01 a RN-04

## 8. Cada nodo declara su hardware y su enlace.

Tiempo: 45 s.

Bajar de la idea al equipo. [Nube.] Lo que se contrata en Azure, por subred, y Brazil South con RPO de 15 minutos y RTO de 4 horas. [Sitios.] San Bernardo va en pares: dos servidores Dell R360, dos FortiGate, clima N+1, detección por aspiración y grupo electrógeno. Cada terminal tiene dos Karbon 430 en activo y espera y un router 5G. El camión lleva el G26I, el módem Iridium, el lector CAN sin contacto y el lector de tarjeta. [Enlaces.] Cada enlace tiene medio, respaldo y tiempo de conmutación: ExpressRoute de 100 Mbit/s con VPN de respaldo en menos de un minuto; terminal fijo con 5G; camión LTE con Iridium hacia IoT Hub. [Cierre.] Cinco ambientes desde el mismo código. Todo el hardware lo compra el mandante; el detalle y las cantidades están en el T-11.

Fuente: S4 §4.2.1: implementos que compra el mandante · §4.2.4: catálogo Azure · §4.2.6: ambientes y respaldos · §4.2.7: enlaces y conmutación · T-11

## 9. El camión es un nodo que opera sin red.

Tiempo: 35 s.

El Caso pide tratar el equipo a bordo como un componente on-premise distribuido. [Equipo.] Es un iWave G26I: Linux, tres buses CAN, LTE, GNSS y un elemento seguro para arranque y claves; guarda los datos en SQLite y aguanta la cabina. [Periféricos.] Cada uno responde a una restricción: el CANCrocodile lee el bus sin cortar cables, para no tocar la garantía; el lector MIFARE identifica al conductor con el camión detenido; el Iridium cubre los tramos sin señal; y la baliza Bluetooth comprueba qué semirremolque va acoplado. [Memoria.] La observación 73 pidió derivar los 8 GB: se necesitan 2.374 MB, y el búfer de 288 horas para el cierre de Los Libertadores pesa menos del 2 %.

Fuente: S4 §4.2.2: equipo a bordo y Tabla de capacidad derivada (2.374 MB) · Caso RT-03.10, RT-06.01, RT-10.05, RT-12.11 · restricciones 5 y 6

## 10. Cada dato vive en el motor que su uso exige.

Tiempo: 40 s.

El dato no está en una sola base. [Dominios.] Asignación y vigencias van en PostgreSQL con transacciones: si no hay estado autoritativo, no se confirma una reserva. A bordo, SQLite sigue capturando y sincroniza después. La telemetría entra por Event Hubs a TimescaleDB. La caché, en Managed Redis, nunca habilita con una copia vieja. Documentos y auditoría quedan inmutables en Blob Storage, y la analítica se separa del despacho en Delta Lake. [Volumen.] 96 mil viajes y cerca de 120 millones de posiciones al año, con la retención que fija el Caso. [Migración.] Cuatro fases; las 6.000 vigencias se acreditan una a una con hash, y nada en cuarentena habilita un despacho.

Fuente: S5 Tabla 5.3: persistencia y conducta ante partición · Tabla 5.5: retención · Tabla 5.6: migración · S4 §4.1.20: volumen declarado

## 11. Si se corta el enlace, la operación sigue.

Tiempo: 30 s.

Cortar los enlaces en la misma vista. [Corte.] Lo que exige estado global, asignar un viaje nuevo y emitir el documento, sigue pasando por el servicio central: no se inventan vigencias ni asignaciones. [Autonomía.] San Bernardo y los terminales operan 24 horas: la torre, las emergencias, la consulta de vigencias en portería. El camión guarda al menos 72 horas, y el diseño llega a 288. [Reconexión.] Al volver la señal se sube por lotes con acuse, y la prueba CP-PERF-02 exige 20 minutos para 300 camiones. Este es el puente con los riesgos: estas mismas piezas son las barreras del R-28.

Fuente: S4 §4.1.26: operación desconectada y reconexión · §4.2.3: funciones on-premise · §4.3: plazos sin enlace · FEP01 Art. 16.4 · Caso RT-03.10 y RT-03.13

## 12. Cómo lo ejecutamos

Tiempo: 3 s.

Separador. Cambio de voz al expositor de la EDT.

Fuente: S7 · T-14 · T-15

## 13. La EDT cubre todo el alcance en 13 elementos.

Tiempo: 40 s.

Construir el árbol en voz alta. Nivel 0: el proyecto completo. Nivel 1: trece elementos orientados a entregables, no a fases. [Revelar paquetes.] Cada elemento baja a paquetes estimables y asignables: 54 en total; el elemento 5 es el más grande porque replica los contextos de la arquitectura. [Revelar agrupación.] Los elementos 1 a 6 construyen la Etapa 1; los 7 a 13 la acompañan, certifican y operan. La regla del 100 %: la suma de los hijos es el padre, sin vacíos ni dobles conteos.

Fuente: S7 §7.1, Figura 7.1 y Tabla 7.2 · T-14: diccionario de 54 paquetes · PMI (2019): regla del 100 %

## 14. Cada elemento baja a paquetes que se pueden aceptar.

Tiempo: 50 s.

Recorrer de izquierda a derecha sin leer paquete por paquete. Columnas 1 y 2: lo que construye la Etapa 1, con el elemento 5 nombrado igual que los contextos de la arquitectura. [Revelar columnas 3 y 4.] Datos, Etapa 2, adhesión, calidad, implantación, innovaciones y operación. [Revelar trazabilidad.] Destacar tres decisiones de diseño: 5.1 a 5.6 son los seis contextos de S4, por lo que cada componente tiene un único paquete que lo construye; 12.1 a 12.5 son las fichas del T-19; y la adhesión es un elemento propio con responsable, porque el Caso exige tratarla como actividad. El elemento 11 produce las actas de los hitos de marcha blanca.

Fuente: S7 Figura 7.1 · T-14: 54 paquetes · S4: seis contextos · T-19: cinco innovaciones · Caso §17.5, p. 40

## 15. El diccionario hace verificable cada paquete.

Tiempo: 45 s.

Tomar un paquete real, el 11.2, y leerlo como lo leería el mandante. [Revelar.] Entregable: lo que se recibe. Criterio: las seis condiciones del Art. 17.3, que se acreditan en los hitos H6 y H7. [Revelar.] Un solo responsable, el Líder de Implantación, y su lugar en la red: A15 y A19, meses 13 a 16. Es el mismo paquete al que llega la traza de la observación 48. [Revelar.] Cerrar con la regla del 100 %: se contrastó contra los 42 requerimientos, los seis contextos, las cinco innovaciones y las once exigencias del Caso; ninguno quedó sin paquete.

Fuente: T-14: paquete 11.2 · S7 Tabla 7.1: cobertura contra el alcance · T-12: RNF-011 · T-17: CP-INT-05 y CP-SYS-05

## 16. La red de 25 actividades define la ruta crítica.

Tiempo: 75 s.

Presentar la Gantt como red, no como barras sueltas. [Barras.] Veinticinco actividades en días hábiles, del día 0 al 420, que es el mes 21. [Dependencias.] Cada flecha es una precedencia fin a inicio del T-15: por ejemplo, la certificación A12 no parte hasta que terminan migración, construcción, integraciones y piloto a bordo. [Ruta crítica.] En rojo la ruta crítica: A01, A02, A05, A07, A09, A12, la reserva A14, y luego la Etapa 2: A17, A20, A22, la reserva A23, A24 y A25. Las líneas punteadas son holguras: la marcha blanca de la Etapa 1 queda fuera de la ruta, con 20 días. [Hitos.] Los rombos son los hitos del E-25; todos caen dentro de su mes contractual.

Fuente: T-15: malla de precedencias, ES/EF/LS/LF y holguras (PERT, días hábiles) · S7 §7.3.1, Tabla 7.7: hitos frente a la red

## 17. ¿Y si la construcción de la Etapa 1 se atrasa 10 días?

Tiempo: 35 s.

Poner la red a prueba con una pregunta que la comisión suele hacer. [Plan.] La cadena crítica de la Etapa 1: ambientes, construcción, certificación y la reserva A14 antes del inicio fijo de la marcha blanca en el día 240. [Atraso.] Si la construcción se atrasa 10 días, la certificación se corre y la reserva baja de 14 a 4 días. [Efecto.] H5 y H6 se cumplen igual: para eso existe la reserva. Pero H4, el fin de la construcción, tiene límite el día 200 y queda dos días tarde: la reserva protege la marcha blanca, no los hitos de pago, y eso es justamente el riesgo R-17. El consumo de más de la mitad de A14 activa el R-16.

Fuente: Cálculo sobre la red del T-15 (A09 +10 días hábiles) · S7 §7.3.1: reserva A14 · S8: Monte Carlo de 10.000 corridas · T-16: R-16 y R-17

## 18. El paquete 11.1 se controla con la compuerta G13.

Tiempo: 35 s.

Conectar la ficha del paquete 11.1 con su control en el cronograma: G13 exige versión probada en PREPROD, datos ficticios y material antes de iniciar los 40 días hábiles de A13 (10 de familiarización y 30 prácticos). Sin G13 disponible, A13 no comienza.

Fuente: T-14: paquete 11.1 · T-15: compuerta G13, actividad A13 (40 d) y reserva A14 · T-16: riesgo R-16

## 19. La transición se ejecuta en dos etapas niveladas.

Tiempo: 30 s.

Explicar el cronograma en escala proporcional M1–M24 con extensión a M56: E1 entra a marcha blanca en M13–M15 y producción en M16; E2 hace marcha blanca en M19–M20 y producción en M21. Destacar la partición en Células Alfa y Beta durante M13–M15 para evitar sobreasignación.

Fuente: S3 §3.2.4 · S7 §§7.2–7.3 · T-15: nivelación Células Alfa/Beta · T-18: etapas E1/E2 y legado hasta M24

## 20. Cómo lo protegemos

Tiempo: 3 s.

Separador. Cambio de voz al expositor de riesgos.

Fuente: S8 · T-16

## 21. Veintiocho riesgos evaluados; ninguno queda alto.

Tiempo: 50 s.

Partir por el panorama completo. [Mapa.] Probabilidad por impacto, de 1 a 5; el color sigue la escala del S8. [Riesgos.] Los 28 riesgos del T-16 en su celda inicial: la mayoría se concentra en exposición media; siete quedan en alta, y uno, el R-06, llega a 15. [Antes y después.] Después de mitigar, ninguno queda en alta. [Cierre.] Las categorías: técnicos, contrapartes, gestión, ciberseguridad y continuidad. Lo residual es una estimación, no una medición.

Fuente: T-16: 28 riesgos con probabilidad, impacto, exposición inicial y residual · S8 §8.1: escalas y umbrales

## 22. Siete riesgos altos, cada uno con su disparador.

Tiempo: 50 s.

Bajar a los siete de exposición alta, sin leer la tabla. [Primeros.] El más alto es R-06: Microsoft retira Azure Cache for Redis justo en el mes 20; se evita desde el diseño naciendo en Azure Managed Redis, y baja de 15 a 3. R-11, la adhesión, se vigila con un corte en el mes 9. [Medio.] Dos son de ciberseguridad y datos: el portal expuesto y la réplica de datos personales en Brazil South, que exige aprobación del mandante en el H2. [Últimos.] La marcha blanca en temporada, el bloqueo indebido de un viaje, que se calibra con la prueba en paralelo, y el R-28, que vemos a continuación.

Fuente: T-16: riesgos con exposición ≥ 12, respuesta, disparador, plazo y exposición residual · S8 §8.3: plan de acción

## 23. R-28: cuatro causas, cuatro barreras antes del evento.

Tiempo: 50 s.

Este es el riesgo que dio origen al bloqueo de salida. [Evento.] Que el documento completo no vuelva a la cabina en 90 segundos. [Causas.] Cuatro caminos: no hay LTE, la carga se conoce sólo en terreno, el documento no cabe en un mensaje satelital o se pierden fragmentos. [Prevención.] Cada uno tiene su barrera: el Iridium, la emisión anticipada, el protocolo fragmentado con integridad y un ensayo en el mes 3 con el peor documento. [Mitigación.] Si aun así ocurre, el camión no sale sin documento conforme, y si el ensayo supera 90 segundos se revisa la decisión de diseño. [AMFE.] Los diez modos de falla quedan bajo 50; los dos más altos se tratan detectando antes.

Fuente: S4 §4.1.13: emisión del documento sin cobertura · T-16: R-28 y análisis de modos de falla · Caso RT-09.01 (90 s) · restricción 8

## 24. Las reservas y holguras absorben el riesgo del plan.

Tiempo: 40 s.

El riesgo de plazo se trata con números del plan. [Revelar reservas.] A14 protege la Etapa 1 con 14 días hábiles: dos desviaciones estándar de su cadena crítica, 97,9 % de cumplir el inicio del mes 13. A23 hace lo mismo para la Etapa 2 con 10 días y 97,6 %. Las dos fechas a la vez: 95,6 %. Y hay una regla: si una reserva baja de la mitad cuando a su cadena le queda más de la mitad, el caso sube al Comité Ejecutivo. [Revelar holguras.] Lo que no depende de audIT queda fuera de la ruta crítica: la factibilidad con terceros puede atrasarse 61 días; un cierre del paso Los Libertadores, unos 9 días hábiles, cabe en la holgura del piloto y de la instalación.

Fuente: S7 §7.3.1: reservas A14 y A23 (PERT, 2σ), probabilidad conjunta 95,6 % y holguras de A04, A06, A11, A15 y A18 · Caso §13.2, p. 27

## 25. Tres compromisos que se pueden verificar.

Tiempo: 20 s.

Cerrar con tres frases, una por acto, sin repetir las láminas. Qué construimos: una arquitectura híbrida que sigue operando sin enlace. Cómo lo ejecutamos: 54 paquetes y una ruta crítica protegida por reservas. Cómo lo protegemos: 28 riesgos con disparador, ninguno alto después de mitigar. Mencionar que la calidad tiene 120 casos diseñados y abrir las preguntas.

Fuente: Síntesis del Informe 2: S4, S5, S7, S8 y formularios T-11 a T-19

## 26. Preguntas y discusión

Tiempo: 10 s.

Abrir los 15 minutos de preguntas. Si hace falta mostrar un detalle, la tecla B abre el respaldo técnico y Escape vuelve.

Fuente: Transportes Curimón · TFEP-01/2026 · audIT Soluciones Tecnológicas SpA

## 27. Registro de riesgos · R-01 a R-14.

Tiempo: 30 s. Respaldo.

Respaldo para preguntas sobre cualquier riesgo del registro.

Fuente: T-16: identificación, evaluación P×I, respuesta, disparador y exposición residual

## 28. Registro de riesgos · R-15 a R-28.

Tiempo: 30 s. Respaldo.

Respaldo para preguntas sobre cualquier riesgo del registro.

Fuente: T-16: identificación, evaluación P×I, respuesta, disparador y exposición residual

## 29. El AMFE completo: diez modos bajo NPR 50.

Tiempo: 30 s. Respaldo.

Respaldo del AMFE con los diez modos.

Fuente: T-16: análisis de modos de falla y efectos (S × O × D = NPR, umbral 50)

## 30. El árbol de fallas modela compuertas OR y AND.

Tiempo: 45 s. Respaldo.

Explicar la estructura lógica del árbol de fallas de S8 §8.2: el evento tope ocurre por una compuerta OR superior alimentada por cuatro ramas, donde cada rama requiere la conjunción (compuerta AND) de una falla técnica y una falla de control.

Fuente: S8 §8.2: árbol de fallas con compuerta OR superior y cuatro compuertas AND inferiores

## 31. Sin documento conforme, el viaje no puede salir.

Tiempo: 60 s. Respaldo.

Explicar que se exige el retorno del documento íntegro a la cabina dentro de 90 segundos, separado en un medidor dedicado. La pre-emisión aplica cuando la carga se conoce. El ensayo extremo a extremo sigue pendiente de acreditación en terreno.

Fuente: T-16: R-28 · S8 §8.2 · Caso RT-09.01: presupuesto de retorno documental en 90 s

## 32. La implantación converge en producción aceptada.

Tiempo: 60 s. Respaldo.

Mostrar cómo las tres corrientes operativas (adhesión de al menos 60 de 148 transportistas en M9, montaje mensual por flota y marcha blanca con reversión disponible) convergen directamente en el nodo de producción con aceptación formal.

Fuente: T-16: R-11 (adhesión), R-19 (montaje), R-18 (marcha blanca) · T-18: criterios de salida y reversión

## 33. Los hitos avanzan por evidencia y protegen fechas.

Tiempo: 90 s. Respaldo.

Explicar la cadena de compuertas e hitos: G13 habilita capacitación, H6 y H11 abren las marchas blancas, y H7/H12 formalizan la aceptación. Distinguir claramente entre fecha contractual de hito, holgura de actividad y las reservas explícitas A14 (14 días) y A23 (10 días).

Fuente: S7 §7.3.1 · T-15: G13 y reservas A14 (14 d) / A23 (10 d) · T-18: hitos H6, H7, H11 y H12

## 34. La reversión opera con tiempos y roles definidos.

Tiempo: 45 s. Respaldo.

Detallar el protocolo de reversión de T-18 en cuatro pasos con sus ventanas operativas y responsables, advirtiendo que no deben sumarse como un RTO único.

Fuente: T-18: procedimiento de reversión en 4 fases (15 min, 30 min, 15 min + 20 min/camión, 24 h / 5 d)

## 35. La calidad se controla desde el código hasta terreno.

Tiempo: 60 s. Respaldo.

Cubrir los capítulos S6 y S9 del Informe 2: ciclo iterativo con control de cambios formal y umbral de <=5% de cambios fallidos en producción; compuertas de calidad para hardware (SAE J1455, IP67, pérdida CAN <0,1%) y 120 casos de prueba diseñados en T-17 bajo ISO 29119.

Fuente: S6 / T-9 / T-10: metodología y control de cambios · S9 / T-13 / T-17: aseguramiento de calidad y 120 casos de prueba

## 36. Las correcciones vinculan decisiones y pruebas.

Tiempo: 60 s. Respaldo.

Unificar las tres correcciones estructurales del Informe 1: las observaciones 37 y 43 quedan resueltas en S3 con el esquema conceptual y el calendario de retiro del legado 2013. Para la observación 48, mostrar la cadena completa RNF-011 → 11.2 → CP-INT-05 → CP-SYS-05 advirtiendo que las pruebas están diseñadas, no ejecutadas.

Fuente: S3 §§3.2.4 y 3.3 · T-12: RNF-011 · T-14: 11.2 · T-17: CP-INT-05 y CP-SYS-05

## 37. Las cinco innovaciones distinguen TRL y condiciones.

Tiempo: 45 s. Respaldo.

Usar ante consultas sobre la Sección 13 (Innovaciones): detalla los 5 paquetes del área 12 de la EDT, diferenciando la madurez comercial del componente respecto del TRL de integración en Curimón.

Fuente: S13 · T-19: fichas de innovación 12.1 a 12.5, niveles TRL y supuestos de validación

## 38. La evidencia mantiene límites metodológicos explícitos.

Tiempo: 45 s. Respaldo.

Usar ante preguntas sobre el alcance de las afirmaciones: distinguimos con rigor entre diseño documental verificado y resultados de ejecución en terreno.

Fuente: S3 · S7 · S8 · T-12 / T-15 / T-17 / T-18

## 39. Diccionario EDT · paquetes 1.1 a 2.3.

Tiempo: 30 s. Respaldo.

Vista paginada del diccionario vigente del T-14 para localizar cualquier paquete durante las preguntas de la comisión.

Fuente: T-14: diccionario de la EDT, entregable, criterio, responsable, red y meses por paquete

## 40. Diccionario EDT · paquetes 2.4 a 3.4.

Tiempo: 30 s. Respaldo.

Vista paginada del diccionario vigente del T-14 para localizar cualquier paquete durante las preguntas de la comisión.

Fuente: T-14: diccionario de la EDT, entregable, criterio, responsable, red y meses por paquete

## 41. Diccionario EDT · paquetes 4.1 a 5.3.

Tiempo: 30 s. Respaldo.

Vista paginada del diccionario vigente del T-14 para localizar cualquier paquete durante las preguntas de la comisión.

Fuente: T-14: diccionario de la EDT, entregable, criterio, responsable, red y meses por paquete

## 42. Diccionario EDT · paquetes 5.4 a 6.2.

Tiempo: 30 s. Respaldo.

Vista paginada del diccionario vigente del T-14 para localizar cualquier paquete durante las preguntas de la comisión.

Fuente: T-14: diccionario de la EDT, entregable, criterio, responsable, red y meses por paquete

## 43. Diccionario EDT · paquetes 6.3 a 7.3.

Tiempo: 30 s. Respaldo.

Vista paginada del diccionario vigente del T-14 para localizar cualquier paquete durante las preguntas de la comisión.

Fuente: T-14: diccionario de la EDT, entregable, criterio, responsable, red y meses por paquete

## 44. Diccionario EDT · paquetes 8.1 a 9.1.

Tiempo: 30 s. Respaldo.

Vista paginada del diccionario vigente del T-14 para localizar cualquier paquete durante las preguntas de la comisión.

Fuente: T-14: diccionario de la EDT, entregable, criterio, responsable, red y meses por paquete

## 45. Diccionario EDT · paquetes 9.2 a 11.1.

Tiempo: 30 s. Respaldo.

Vista paginada del diccionario vigente del T-14 para localizar cualquier paquete durante las preguntas de la comisión.

Fuente: T-14: diccionario de la EDT, entregable, criterio, responsable, red y meses por paquete

## 46. Diccionario EDT · paquetes 11.2 a 12.3.

Tiempo: 30 s. Respaldo.

Vista paginada del diccionario vigente del T-14 para localizar cualquier paquete durante las preguntas de la comisión.

Fuente: T-14: diccionario de la EDT, entregable, criterio, responsable, red y meses por paquete

## 47. Diccionario EDT · paquetes 12.4 a 13.4.

Tiempo: 30 s. Respaldo.

Vista paginada del diccionario vigente del T-14 para localizar cualquier paquete durante las preguntas de la comisión.

Fuente: T-14: diccionario de la EDT, entregable, criterio, responsable, red y meses por paquete