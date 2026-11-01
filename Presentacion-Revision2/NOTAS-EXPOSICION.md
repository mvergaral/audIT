# Guion de exposición

Objetivo: 15 minutos y 14 segundos + -14 segundos de margen. No hay asignación ficticia de expositores.

## 1. Revisión 2 · Caso Transporte de Carga

Tiempo: 15 s.

Presentar el alcance de la revisión: correcciones del Informe 1, riesgos de solución, proyecto e implantación, EDT, planificación e hitos. La exposición dura 15 minutos y deja 15 minutos para preguntas.

Fuente: Transportes Curimón · TFEP-01/2026 · audIT Soluciones Tecnológicas SpA

## 2. Una salida segura exige información confiable.

Tiempo: 25 s.

La salida requiere conductor habilitado, vehículo conforme y documento íntegro en cabina. La identificación del conductor utiliza tarjeta MIFARE con el camión detenido; no se propone biometría de conductores. La biometría del T-11 corresponde a la sala de datos. Una asignación de recursos no sustituye la autorización de salida: la condición documental se verifica antes del traslado.

Fuente: S2 · S3 §3.3 · S8: verificación bloqueante de salida

## 3. Cambios principales del Informe 2

Tiempo: 40 s.

Síntesis de 40 segundos. [Vista inicial: requisitos y arquitectura.] El Informe 2 incorpora el catálogo T-12 de 42 requerimientos trazados a componentes, paquetes y pruebas diseñadas; S3 §3.2.8 y T-17 responden a las observaciones 01, 38, 45 y 48. El esquema conceptual de S3 §3.3 y las capas, interfaces y arquitectura física de S4 §§4.1.3 y 4.2 responden a 37, 53, 64 y 65, con el catálogo T-11. [Revelar legado y capacidad.] S3 §3.2.4 resuelve la observación 43 con sustitución por funciones en M16 y M21, consulta hasta M24 y conservación del ERP contable como único emisor tributario. S4 §§4.2.2 y 4.2.8 deriva memoria y reconexión para 73 y 74; T-17 CP-PERF-02 define el ensayo del proceso completo. [Revelar innovaciones.] Para 88–91, S13 §§13.2–13.3 reformula la programación por oportunidad de patio y el semirremolque conectado; T-19 entrega cinco fichas con los elementos exigidos. Se priorizan cambios que definen el alcance, la viabilidad y la verificación de la propuesta. Las correcciones editoriales permanecen en la matriz completa y las novedades de EDT y riesgos se explican en sus bloques. La selección no acredita cierre integral de las 100 observaciones ni ejecución de las pruebas. El respaldo de correcciones amplía 37, 43 y 48.

Fuente: Matriz Art. 46 · S3 · S4 · S13 · T-11 / T-12 / T-17 / T-19

## 4. Qué construimos

Tiempo: 3 s.

Separador de acto; el expositor 1 continúa con la arquitectura.

Fuente: S4 y S5

## 5. La solución es híbrida: nube, sitio y flota.

Tiempo: 40 s.

[Nube.] Azure Chile Central en tres zonas; Brazil South es la región de recuperación prevista. [Sitios.] San Bernardo sostiene la torre y aloja la capa anticorrupción junto al contable, único emisor tributario; cuatro terminales tienen nodos activo y espera y respaldo 5G. [Flota.] Se instalan equipos audIT en 182 camiones. Los 192 de terceros conservan sus equipos: el acceso por interfaz o exportación se sujeta a autorización y factibilidad por proveedor, sin prometer una API disponible para todos. La cobertura efectiva y antigüedad se muestran por unidad. [Componentes.] El catálogo arquitectónico tiene 39: 24 primarios, uno de recuperación y 14 fuera de la nube. R24 exige base de licitud, aprobación del mandante y cláusulas firmadas antes de H2; si falta esa condición no se autoriza producción, según S4.

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

Tiempo: 40 s.

[Nube.] Chile Central es la región primaria: red central 10.10.0.0/22 y red de producción 10.11.0.0/20. Brazil South recibe réplicas para recuperación, con RPO de 15 minutos y RTO de 4 horas. [Enlaces.] El camión llega por LTE o Iridium a IoT Hub en Chile Central. San Bernardo usa ExpressRoute de 100 Mbit/s y VPN de respaldo; cada terminal, enlace fijo y 5G. [Energía.] San Bernardo mantiene equipos A/B en circuitos distintos: cada R360 tiene dos fuentes y cada FortiGate 90G, dos adaptadores. En cada terminal hay un bus de 24 V para cómputo y router y otro de 48 V para el TSW202, que alimenta el punto de acceso y el lector por PoE. Cada bus tiene dos fuentes DIN y un módulo de redundancia: una fuente desde la UPS y otra desde un circuito distinto del tablero, según RT-08.04 y T-11. [Cierre.] Cinco ambientes desde el mismo código. El mandante compra el hardware detallado en T-11.

Fuente: S4 §4.2.1: hardware · §4.2.5: redes · §4.2.6: ambientes · §4.2.7: enlaces y alimentación redundante · T-11 · FEP02 RT-08.04, p. 18

## 9. La arquitectura física completa, parte por parte.

Tiempo: 45 s.

[Completa.] La misma arquitectura de la lámina anterior, en una sola vista: nube, San Bernardo, cuatro terminales, flota y contrapartes, con cada enlace y su capacidad. [Nube.] Chile Central, en tres zonas, separa borde, aplicación, integración, gestión y datos dentro de la red de producción 10.11.0.0/20. IoT Hub recibe a los camiones y Event Hubs, con protocolo Kafka, reparte los eventos. Brazil South recibe la réplica asíncrona y queda en espera, con RTO de 4 horas y RPO de 15 minutos. [San Bernardo.] Dos racks de 24 U: servidores R360 A y B, dos FortiGate 90G en alta disponibilidad, FortiSwitch A y B y dos UPS SRT3000, con 66 minutos. El grupo electrógeno Himoinsa de 8,8 kVA sostiene 24 horas con 64,3 litros. La capa anticorrupción une el sistema contable, único emisor tributario, con el sistema de 2013. ExpressRoute de 100 Mbit/s y la VPN de respaldo la conectan con Azure. [Terminales.] Cada gabinete tiene dos Karbon 430, uno activo y otro en espera, el router RUTX50 con enlace fijo de al menos 10 Mbit/s y 5G con dos SIM, y el switch TSW202. La portería lee la baliza del semirremolque con el Minew G1 y el patio tiene un FortiAP 234G. El terminal opera 24 horas sin enlace. [Flota.] Los 182 tractocamiones con equipo audIT, 148 propios y 34 de terceros, llevan el iWave G26I con Iridium Edge, el lector CAN sin contacto y el lector de tarjeta. De los 8 GB de memoria se usan 2,4 GB, con el búfer de 288 horas. Los 192 camiones de terceros conservan su equipo.

Fuente: S4 §4.2.1: implementos · §4.2.3: emplazamiento · §4.2.5: redes · §4.2.7: enlaces · T-11 · versión extendida de la Figura 4.13 del S4

## 10. El camión es un nodo que opera sin red.

Tiempo: 35 s.

El Caso pide tratar el equipo a bordo como un componente on-premise distribuido. [Equipo.] Es un iWave G26I: Linux, tres buses CAN, LTE, GNSS y un elemento seguro para arranque y claves; guarda los datos en SQLite y aguanta la cabina. [Periféricos.] Cada uno responde a una restricción: el CANCrocodile lee el bus sin cortar cables, para no tocar la garantía; el lector MIFARE identifica al conductor con el camión detenido; el Iridium cubre los tramos sin señal; y la baliza Bluetooth comprueba qué semirremolque va acoplado. [Memoria.] La observación 73 pidió derivar los 8 GB: se necesitan 2.374 MB, y el búfer de 288 horas para el cierre de Los Libertadores pesa menos del 2 %.

Fuente: S4 §4.2.2: equipo a bordo y Tabla de capacidad derivada (2.374 MB) · Caso RT-03.10, RT-06.01, RT-10.05, RT-12.11 · restricciones 5 y 6

## 11. Cada dato vive en el motor que su uso exige.

Tiempo: 35 s.

[Dominios.] PostgreSQL confirma las asignaciones; SQLite captura a bordo; TimescaleDB conserva telemetría. La caché no habilita con una copia desactualizada. Documentos y auditoría conservan integridad y la analítica se separa del despacho. [Volumen.] 96.000 viajes y cerca de 120 millones de posiciones anuales. [Migración.] Las aproximadamente 6.000 vigencias requieren verificación documental individual, respaldo custodiado y acta de conciliación. El hash SHA-256 comprueba integridad y no sustituye la verificación documental. Nada en cuarentena habilita despacho.

Fuente: S5 Tabla 5.3: persistencia y conducta ante partición · Tabla 5.5: retención · Tabla 5.6: migración · S4 §4.1.20: volumen declarado

## 12. Si se corta el enlace, la operación sigue.

Tiempo: 35 s.

[Autoridad.] Una asignación nueva requiere el estado autoritativo de Azure. El sistema contable de San Bernardo permanece como único emisor tributario, integrado a través de la capa anticorrupción. [Autonomía.] Los sitios mantienen 24 horas de funciones locales y el camión conserva un mínimo contractual de 72 horas, con diseño para 288. Una copia local no permite inventar vigencias ni confirmar asignaciones globales. [Reconexión.] Se sincroniza por lotes con deduplicación y acuse duradero. CP-PERF-02 diseña la comprobación con 300 camiones tras 72 horas, incluyendo transferencia, persistencia y conciliación. Es un criterio de ensayo, no una medición ya realizada.

Fuente: S4 §4.1.26: operación desconectada y reconexión · §4.2.3: funciones on-premise · §4.3: plazos sin enlace · FEP01 Art. 16.4 · Caso RT-03.10 y RT-03.13

## 13. Cómo lo ejecutamos

Tiempo: 3 s.

Separador. Cambio de voz al expositor de la EDT.

Fuente: S7 · T-14 · T-15

## 14. La EDT cubre todo el alcance en 13 elementos.

Tiempo: 35 s.

Construir el árbol en voz alta. Nivel 0: el proyecto completo. Nivel 1: trece elementos orientados a entregables, no a fases. [Revelar paquetes.] Cada elemento baja a paquetes estimables y asignables: 54 en total; el elemento 5 es el más grande porque replica los contextos de la arquitectura. [Revelar agrupación.] Los elementos 1 a 6 construyen la Etapa 1; los 7 a 13 la acompañan, certifican y operan. La regla del 100 %: la suma de los hijos es el padre, sin vacíos ni dobles conteos.

Fuente: S7 §7.1, Figura 7.1 y Tabla 7.2 · T-14: diccionario de 54 paquetes · PMI (2019): regla del 100 %

## 15. Cada elemento baja a paquetes que se pueden aceptar.

Tiempo: 40 s.

Recorrer de izquierda a derecha sin leer paquete por paquete. Columnas 1 y 2: lo que construye la Etapa 1, con el elemento 5 nombrado igual que los contextos de la arquitectura. [Revelar columnas 3 y 4.] Datos, Etapa 2, adhesión, calidad, implantación, innovaciones y operación. [Revelar trazabilidad.] Destacar tres decisiones de diseño: 5.1 a 5.6 son los seis contextos de S4, por lo que cada componente tiene un único paquete que lo construye; 12.1 a 12.5 son las fichas del T-19; y la adhesión es un elemento propio con responsable, porque el Caso exige tratarla como actividad. El elemento 11 produce las actas de los hitos de marcha blanca.

Fuente: S7 Figura 7.1 · T-14: 54 paquetes · S4: seis contextos · T-19: cinco innovaciones · Caso §17.5, p. 40

## 16. El diccionario hace verificable cada paquete.

Tiempo: 40 s.

Tomar un paquete real, el 11.2, y leerlo como lo leería el mandante. [Revelar.] Entregable: lo que se recibe. Criterio: las seis condiciones del Art. 17.3, que se acreditan en los hitos H6 y H7. [Revelar.] Un solo responsable, el Líder de Implantación, y su lugar en la red: A15 y A19, meses 13 a 16. Es el mismo paquete al que llega la traza de la observación 48. [Revelar.] Cerrar con la regla del 100 %: se contrastó contra los 42 requerimientos, los seis contextos, las cinco innovaciones y las once exigencias del Caso; ninguno quedó sin paquete.

Fuente: T-14: paquete 11.2 · S7 Tabla 7.1: cobertura contra el alcance · T-12: RNF-011 · T-17: CP-INT-05 y CP-SYS-05

## 17. La red de 25 actividades define la ruta crítica.

Tiempo: 65 s.

[Barras.] Veinticinco actividades y la compuerta G13, del día 0 al 420, fin M21. [Dependencias.] Se muestran precedencias fin a inicio; A09 hacia G13 y A13 incluye adelanto FS−10. A12 depende de migración, construcción, integraciones y piloto. [Ruta.] Trece actividades críticas; las reservas A14 y A23 son explícitas. Un atraso se propaga si se mantienen todas las duraciones; consumir una reserva modifica ese escenario. [Hitos.] Los rombos muestran la posición planificada y los porcentajes, redondeados, la probabilidad Monte Carlo de cumplir el límite contractual de S8. No son probabilidades de terminar en la fecha temprana: A12 se planifica al día 226, pero el 96,2 % corresponde al límite 240. Redondear un resultado a 100 % no constituye una garantía.

Fuente: T-15: precedencias y holguras · S7 §7.3.1, Tabla 7.7: posición planificada · S8: Monte Carlo al límite contractual (10.000 corridas)

## 18. ¿Y si la construcción de la Etapa 1 se atrasa 10 días?

Tiempo: 40 s.

Este es un escenario determinista sobre la red del T-15, sin nueva simulación. A09 termina el día 202 y supera el límite 200 de H4. A12 se desplaza hasta el 236 y la reserva A14 baja de 14 a 4 días, conservando el inicio fijo de H6 en el día 240. G13 y A13 se desplazan: A13 acaba el día 232 y conserva ocho días antes de H6. Los 38 días de holgura total de la red no autorizan a mover esa fecha fija. Se activa R16 por consumo superior al 50 % de A14 y permanece R17 por incumplimiento del hito intermedio. Los porcentajes Monte Carlo de S8 pertenecen a la línea base; no se atribuyen a este escenario.

Fuente: T-15 y S7 §7.3.1: A09 +10 días hábiles y consumo de A14 · T-16: R-16 y R-17 · No se recalcula Monte Carlo

## 19. El paquete 11.1 se controla con la compuerta G13.

Tiempo: 35 s.

Conectar la ficha del paquete 11.1 con su control en el cronograma: G13 exige versión probada en PREPROD, datos ficticios y material antes de iniciar los 40 días hábiles de A13 (10 de familiarización y 30 prácticos). Sin G13 disponible, A13 no comienza.

Fuente: T-14: paquete 11.1 · T-15: compuerta G13, actividad A13 (40 d) y reserva A14 · T-16: riesgo R-16

## 20. La transición se ejecuta en dos etapas niveladas.

Tiempo: 45 s.

[Etapas.] Marcha blanca E1 M13–M15 y producción M16; marcha blanca E2 M19–M20 y aceptación M21; operación hasta M56. [Legado.] Retiro funcional del sistema de 2013 en M16 y M21, consulta histórica hasta M24; el contable permanece como emisor. [Capacidad M13–M15.] Son 37 personas, 21 de planta y 16 de refuerzo. Los 37 FTE se distribuyen en 21,5 para E1, 14,1 para E2 y 1,4 de coordinación. Seguridad de la Información y Líder de Integración son dos roles distintos, cada uno de un FTE: 0,4 E1, 0,4 E2 y 0,2 coordinación. No hay un especialista combinado. La tabla T-15 desglosa el resto de roles sin sobreasignación. En M19–M20 S7 prevé 26 personas; 16 integran la operación desde M21.

Fuente: S3 §3.2.4 · S7 §§7.2–7.3 · T-15: nivelación Células Alfa/Beta · T-18: etapas E1/E2 y legado hasta M24

## 21. Cómo lo protegemos

Tiempo: 3 s.

Separador. Cambio de voz al expositor de riesgos.

Fuente: S8 · T-16

## 22. Veintiocho riesgos evaluados; ninguno queda alto.

Tiempo: 45 s.

Partir por el panorama completo. [Mapa.] Probabilidad por impacto, de 1 a 5; el color sigue la escala del S8. [Riesgos.] Los 28 riesgos del T-16 en su celda inicial: la mayoría se concentra en exposición media; siete quedan en alta, y uno, el R-06, llega a 15. [Antes y después.] Después de mitigar, ninguno queda en alta. [Cierre.] Las categorías: técnicos, contrapartes, gestión, ciberseguridad y continuidad. Lo residual es una estimación, no una medición.

Fuente: T-16: 28 riesgos con probabilidad, impacto, exposición inicial y residual · S8 §8.1: escalas y umbrales

## 23. Siete riesgos altos, cada uno con su disparador.

Tiempo: 45 s.

Seleccionar los siete riesgos de exposición alta inicial. R06 se evita usando Managed Redis desde el diseño; R11 se vigila con al menos 60 de los 148 transportistas al corte M9 y refuerzo con 59 o menos. R23 protege el portal. R24 exige base de licitud, aprobación del mandante y cláusulas firmadas antes de H2; la región secundaria no se considera autorizada por el solo calendario. Completar con marcha blanca en temporada, bloqueo indebido y retorno documental R28. Las exposiciones residuales son estimaciones de diseño.

Fuente: T-16: riesgos con exposición ≥ 12, respuesta, disparador, plazo y exposición residual · S8 §8.3: plan de acción

## 24. R-28: cuatro causas, cuatro barreras antes del evento.

Tiempo: 45 s.

[Evento.] El documento completo no vuelve a cabina dentro de 90 segundos. [Causas y controles.] Sin LTE se utiliza Iridium. Si la carga definitiva se conoce solo en terreno, se solicita por satélite al contable; la preemisión únicamente sirve cuando se conoce antes. Un documento mayor que un mensaje requiere fragmentación y reensamblado; las pérdidas requieren acuse de integridad y reintentos dentro del presupuesto total. El ensayo M3 utiliza el documento mayor, con pérdidas y reintentos, para validar estas barreras; no es una barrera operativa por sí solo. [Respuesta.] Sin documento conforme no se permite salir; si el ensayo falla se revisan diseño y T-11 según R28, sin asumir resuelto el camino de carga desconocida. [AMFE.] Diez modos, todos bajo NPR 50 estimado; no son mediciones de terreno.

Fuente: S4 §4.1.13: emisión del documento sin cobertura · T-16: R-28 y análisis de modos de falla · Caso RT-09.01 (90 s) · restricción 8

## 25. Las reservas y holguras absorben el riesgo del plan.

Tiempo: 50 s.

[Reservas.] A14 aporta 14 días y A23 diez. S7 usa una aproximación normal por cadenas: probabilidades 97,9 % y 97,6 %, con producto conjunto 95,6 %. [Red completa.] S8 simula 10.000 corridas con semilla 2026 y Beta-PERT sobre el T-15: H6 96,2 %, H11 95,5 % y ambas marchas blancas a tiempo 92,1 %. La diferencia recoge las rutas convergentes y la capacitación condicionada a G13; no se presentan ambos resultados como equivalentes. Si la reserva baja del 50 % con más de la mitad de cadena pendiente, se eleva al Comité Ejecutivo. [Holguras.] A04 tiene 61 días totales; A18 cuarenta, A11 y A15 veinte, y A06 veinticuatro libres. Son holguras internas; no permiten desplazar hitos ni condiciones contractuales.

Fuente: S7 Tabla 7.6: PERT por cadenas (97,9 %, 97,6 %; conjunta 95,6 %) · S8: red completa (96,2 %, 95,5 %; conjunta 92,1 %) · T-15

## 26. Tres compromisos que se pueden verificar.

Tiempo: 20 s.

Cerrar con tres frases, una por acto, sin repetir las láminas. Qué construimos: una arquitectura híbrida que sigue operando sin enlace. Cómo lo ejecutamos: 54 paquetes y una ruta crítica protegida por reservas. Cómo lo protegemos: 28 riesgos con disparador, ninguno alto después de mitigar. Mencionar que la calidad tiene 120 casos diseñados y abrir las preguntas.

Fuente: Síntesis del Informe 2: S4, S5, S7, S8 y formularios T-11 a T-19

## 27. Preguntas y discusión

Tiempo: 5 s.

Abrir los 15 minutos de preguntas. Si hace falta mostrar un detalle, la tecla B abre el respaldo técnico y Escape vuelve.

Fuente: Transportes Curimón · TFEP-01/2026 · audIT Soluciones Tecnológicas SpA

## 28. Registro de riesgos · R-01 a R-14.

Tiempo: 30 s. Respaldo.

Respaldo para preguntas sobre cualquier riesgo del registro.

Fuente: T-16: identificación, evaluación P×I, respuesta, disparador y exposición residual

## 29. Registro de riesgos · R-15 a R-28.

Tiempo: 30 s. Respaldo.

Respaldo para preguntas sobre cualquier riesgo del registro.

Fuente: T-16: identificación, evaluación P×I, respuesta, disparador y exposición residual

## 30. El AMFE completo: diez modos bajo NPR 50.

Tiempo: 30 s. Respaldo.

Respaldo del AMFE con los diez modos.

Fuente: T-16: análisis de modos de falla y efectos (S × O × D = NPR, umbral 50)

## 31. El árbol de fallas modela compuertas OR y AND.

Tiempo: 45 s. Respaldo.

El evento tope se alimenta por OR de cuatro ramas. Cada AND expresa una conjunción de falla técnica y falla de control. Se utiliza como análisis lógico cualitativo para diseñar pruebas; dibujar AND no acredita independencia estadística ni autoriza multiplicar probabilidades sin datos.

Fuente: S8 §8.2: árbol de fallas con compuerta OR superior y cuatro compuertas AND inferiores

## 32. Sin documento conforme, el viaje no puede salir.

Tiempo: 60 s. Respaldo.

Explicar que se exige el retorno del documento íntegro a la cabina dentro de 90 segundos, separado en un medidor dedicado. La pre-emisión aplica cuando la carga se conoce. El ensayo extremo a extremo sigue pendiente de acreditación en terreno.

Fuente: T-16: R-28 · S8 §8.2 · Caso RT-09.01: presupuesto de retorno documental en 90 s

## 33. La implantación converge en producción aceptada.

Tiempo: 60 s. Respaldo.

Mostrar cómo las tres corrientes operativas (adhesión de al menos 60 de 148 transportistas en M9, montaje mensual por flota y marcha blanca con reversión disponible) convergen directamente en el nodo de producción con aceptación formal.

Fuente: T-16: R-11 (adhesión), R-19 (montaje), R-18 (marcha blanca) · T-18: criterios de salida y reversión

## 34. Los hitos avanzan por evidencia y protegen fechas.

Tiempo: 90 s. Respaldo.

Explicar la cadena de compuertas e hitos: G13 habilita capacitación, H6 y H11 abren las marchas blancas, y H7/H12 formalizan la aceptación. Distinguir claramente entre fecha contractual de hito, holgura de actividad y las reservas explícitas A14 (14 días) y A23 (10 días).

Fuente: S7 §7.3.1 · T-15: G13 y reservas A14 (14 d) / A23 (10 d) · T-18: hitos H6, H7, H11 y H12

## 35. La reversión opera con tiempos y roles definidos.

Tiempo: 45 s. Respaldo.

Recorrer las seis acciones del T-18. Detecta la guardia de la mesa de servicio en 15 minutos. Deciden Jefe de Proyecto y Líder de Operación en 30 minutos, con contraparte técnica informada. El SRE de guardia conmuta en 15 minutos. El Líder de Operación recibe los eventos reenviados en 20 minutos por camión. El Líder de Datos concilia en 24 horas. El Jefe de Proyecto informa la causa raíz en cinco días hábiles. Las ventanas no constituyen un RTO sumado; el procedimiento se ensaya en PREPROD antes de cada paso a producción. Un firmware vuelve a la imagen anterior en el siguiente paso por terminal, sin borrar eventos pendientes.

Fuente: T-18: procedimiento de reversión, seis acciones con sus responsables y tiempos máximos

## 36. La calidad se controla desde el código hasta terreno.

Tiempo: 60 s. Respaldo.

S6 combina sprints de dos semanas con control de cambios y umbral mensual ≤5 % de cambios fallidos. T-13 aplica SAE J1455 al perfil de montaje e IP67 al conjunto exterior expuesto, no uniformemente a todos los periféricos de cabina: el lector MIFARE del T-11 es IP66. La lectura CAN exige pérdida <0,1 % y cero tramas transmitidas por audIT. Los 120 casos del T-17 son 25 unitarios, 25 integración, 20 sistema, 12 rendimiento, ocho seguridad, 15 hardware/HIL y 15 UAT. Rendimiento y seguridad se agrupan como veinte no funcionales en la gráfica. Son casos diseñados, cuya ejecución y actas corresponden a la fase contractual.

Fuente: S6 / T-9 / T-10: metodología y control de cambios · S9 / T-13 / T-17: aseguramiento de calidad y 120 casos de prueba

## 37. Las correcciones vinculan decisiones y pruebas.

Tiempo: 60 s. Respaldo.

Unificar las tres correcciones estructurales del Informe 1: las observaciones 37 y 43 quedan resueltas en S3 con el esquema conceptual y el calendario de retiro del legado 2013. Para la observación 48, mostrar la cadena completa RNF-011 → 11.2 → CP-INT-05 → CP-SYS-05 advirtiendo que las pruebas están diseñadas, no ejecutadas.

Fuente: S3 §§3.2.4 y 3.3 · T-12: RNF-011 · T-14: 11.2 · T-17: CP-INT-05 y CP-SYS-05

## 38. Las cinco innovaciones distinguen TRL y condiciones.

Tiempo: 60 s. Respaldo.

Cada innovación conserva su propio calendario y meta. Son propuestas: no se declara medición ni piloto ejecutados. Expediente: 50 % de adheridos con al menos una emisión en M21, y respuesta ≤5 s en 99 % de verificaciones desde M16; el formato alternativo depende de aceptación. Proceso: concepto TRL 2, piloto de 10 camiones M6, flota propia completa M9, terceros desde M7, pausa M11–M15 y continuación M16–M18; la mejora de 20 % exige línea base homologada. Semirremolque: el 95 % se refiere a asignaciones con semirremolque propio verificado por medición; montaje M6–M10 y M16–M18, validación antes de M16. Adhesión: ventana y consentimiento TRL 8; el contrato no recibe TRL. Bienestar: TRL 2 conceptual; objetivos TRL 6 tras ensayos M10–M12 y TRL 7 tras piloto M13–M15, sujetos a evidencia. Su efectividad divide episodios con recomendación válida y oportuna por episodios en que el oráculo exige parada; falta de parador, aviso omitido o tardío son fallos, y con denominador cero no se informa tasa. Talleres M4, catálogo M3–M6 y software M4–M9 preceden a esa validación.

Fuente: S13 §§13.1–13.5 · T-19: madurez, calendarios e indicadores por ficha · EDT 12.1–12.5

## 39. La evidencia mantiene límites metodológicos explícitos.

Tiempo: 45 s. Respaldo.

Usar ante preguntas sobre el alcance de las afirmaciones: distinguimos con rigor entre diseño documental verificado y resultados de ejecución en terreno.

Fuente: S3 · S7 · S8 · T-12 / T-15 / T-17 / T-18

## 40. Diccionario EDT · paquetes 1.1 a 2.3.

Tiempo: 30 s. Respaldo.

Vista paginada del diccionario vigente del T-14 para localizar cualquier paquete durante las preguntas de la comisión.

Fuente: T-14: diccionario de la EDT, entregable, criterio, responsable, red y meses por paquete

## 41. Diccionario EDT · paquetes 2.4 a 3.4.

Tiempo: 30 s. Respaldo.

Vista paginada del diccionario vigente del T-14 para localizar cualquier paquete durante las preguntas de la comisión.

Fuente: T-14: diccionario de la EDT, entregable, criterio, responsable, red y meses por paquete

## 42. Diccionario EDT · paquetes 4.1 a 5.3.

Tiempo: 30 s. Respaldo.

Vista paginada del diccionario vigente del T-14 para localizar cualquier paquete durante las preguntas de la comisión.

Fuente: T-14: diccionario de la EDT, entregable, criterio, responsable, red y meses por paquete

## 43. Diccionario EDT · paquetes 5.4 a 6.2.

Tiempo: 30 s. Respaldo.

Vista paginada del diccionario vigente del T-14 para localizar cualquier paquete durante las preguntas de la comisión.

Fuente: T-14: diccionario de la EDT, entregable, criterio, responsable, red y meses por paquete

## 44. Diccionario EDT · paquetes 6.3 a 7.3.

Tiempo: 30 s. Respaldo.

Vista paginada del diccionario vigente del T-14 para localizar cualquier paquete durante las preguntas de la comisión.

Fuente: T-14: diccionario de la EDT, entregable, criterio, responsable, red y meses por paquete

## 45. Diccionario EDT · paquetes 8.1 a 9.1.

Tiempo: 30 s. Respaldo.

Vista paginada del diccionario vigente del T-14 para localizar cualquier paquete durante las preguntas de la comisión.

Fuente: T-14: diccionario de la EDT, entregable, criterio, responsable, red y meses por paquete

## 46. Diccionario EDT · paquetes 9.2 a 11.1.

Tiempo: 30 s. Respaldo.

Vista paginada del diccionario vigente del T-14 para localizar cualquier paquete durante las preguntas de la comisión.

Fuente: T-14: diccionario de la EDT, entregable, criterio, responsable, red y meses por paquete

## 47. Diccionario EDT · paquetes 11.2 a 12.3.

Tiempo: 30 s. Respaldo.

Vista paginada del diccionario vigente del T-14 para localizar cualquier paquete durante las preguntas de la comisión.

Fuente: T-14: diccionario de la EDT, entregable, criterio, responsable, red y meses por paquete

## 48. Diccionario EDT · paquetes 12.4 a 13.4.

Tiempo: 30 s. Respaldo.

Vista paginada del diccionario vigente del T-14 para localizar cualquier paquete durante las preguntas de la comisión.

Fuente: T-14: diccionario de la EDT, entregable, criterio, responsable, red y meses por paquete