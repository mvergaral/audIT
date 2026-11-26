# Notas de exposición · Propuesta Final

La pauta contempla 14:05 de exposición y 0:55 de margen.

## 1. Propuesta Final

Tiempo: 10 s. 

Presentar el recorrido de la propuesta: qué construimos, cómo lo ejecutamos, cómo lo protegemos y por qué conviene económicamente. La exposición dura 15 minutos; el resto es preguntas y evaluación.

Fuente: Transportes Curimón · TFEP-01/2026 · audIT Soluciones Tecnológicas SpA

## 2. Una salida segura exige información confiable.

Tiempo: 45 s. 

Abrir desde la operación real. El camión se desplaza sobre un carril dedicado mientras se activan los tres controles bloqueantes inferiores: conductor, vehículo y documento deben aportar evidencia válida antes de autorizar la salida.

Fuente: S2 · S3 §3.3 · S8: verificación bloqueante de salida

## 3. Resumen de la oferta: qué recibe Transportes Curimón.

Tiempo: 50 s. 

Vender la propuesta en una lámina. Qué entregamos: una solución híbrida de 47 componentes que sigue operando sin enlace. Cómo lo ejecutamos: 54 paquetes aceptables, dos etapas y márgenes de aceptación por hito. Cuánto cuesta: el valor total del proyecto y, más adelante, su explicación por categoría, VAN y TIR. Cerrar con la evidencia: cinco innovaciones con TRL, 36 riesgos con disparador y 120 casos de prueba diseñados, no ejecutados.

Fuente: S4 · S7 · S8 · T-11 · T-14 · T-15 · T-16 · T-17 · T-19 · economico/datos/partidas.csv

## 4. La solución es híbrida: nube, sitio y flota.

Tiempo: 50 s. 

Abrir con el mapa completo. [Nube.] El núcleo vive en Azure Chile Central, en tres zonas: Front Door, API Management, los seis contextos en AKS, IoT Hub y Event Hubs para la ingesta, PostgreSQL con TimescaleDB, Managed Redis y Storage; Brazil South espera como recuperación. [Sitio.] San Bernardo no aloja el núcleo: mantiene viva la torre si cae el enlace y aloja la capa anticorrupción junto al sistema contable, que sigue siendo el único emisor. Cada terminal tiene dos nodos en activo y espera y un router 5G. [Flota.] 182 camiones llevan el equipo audIT; los 192 de terceros no se intervienen y llegan por la plataforma de su proveedor. [Componentes.] Son 47 componentes: 32 en la región primaria, uno en la secundaria y 14 fuera de la nube. Por eso es híbrida, como exige el Artículo 16.

Fuente: S4 §4.2, Tabla de planos y §4.2.3: 47 componentes (32 + 1 + 14) · T-11 · FEP01 Art. 16.1 a 16.4 · Caso RT-06.01 · íconos: Azure Architecture Icons y Simple Icons

## 5. Ocho capas, cada una con su producto.

Tiempo: 40 s. 

Recorrer la pila de arriba abajo, nombrando el producto, no el concepto. [Capas.] Portales en Next.js y React, app Flutter; Front Door con cortafuegos como único punto público; API Management con certificado mutuo; los servicios de negocio en AKS en tres zonas sobre .NET 10 LTS; IoT Hub y Event Hubs con protocolo Kafka para la ingesta, escrita en Go; y una capa de datos políglota. [Transversales.] Seguridad, con Entra ID y Key Vault, y observabilidad, con Azure Monitor, no son un piso más: atraviesan todos. [Contextos.] El negocio son seis contextos; cada uno decide una sola cosa y tiene sus propios datos: Planificación pregunta a Personas y a Flota, no lee sus bases. Son los mismos nombres de los paquetes 5.1 a 5.6 de la EDT.

Fuente: S4 §4.1.1: productos y soporte · §4.1.3: las ocho capas (FEP02 2.1, RT-02.01) · §4.1.4: seis contextos delimitados · ISO/IEC/IEEE 42010

## 6. Un viaje se autoriza o se bloquea en 30 segundos.

Tiempo: 40 s. 

[Solicitud.] La torre pide asignar conductor, tracto, semirremolque y carga. [Validaciones.] Planificación consulta en paralelo a Personas, Flota y al sistema contable. Serializa la reserva y confirma solo si las evaluaciones siguen vigentes. Una causa legal bloquea siempre y el rechazo explica por qué. [Presupuesto.] Los 30 segundos incluyen 5 de margen. Es un presupuesto de diseño pendiente de medición de extremo a extremo.

Fuente: S4 §4.1.9 y Tabla 4.3: presupuesto de diseño de la asignación · Caso RT-09.01, p. 32 · S3: RN-01 a RN-04

## 7. El camión es un nodo que opera sin red.

Tiempo: 45 s. 

El Caso pide tratar el equipo a bordo como un componente on-premise distribuido. [Equipo.] Es un iWave G26I: Linux, tres buses CAN, LTE, GNSS y un elemento seguro para arranque y claves; guarda los datos en SQLite y aguanta la cabina. [Periféricos.] Cada uno responde a una restricción: el CANCrocodile lee el bus sin cortar cables, para no tocar la garantía; el lector MIFARE identifica al conductor con el camión detenido; el Iridium cubre los tramos sin señal; y la baliza Bluetooth comprueba qué semirremolque va acoplado. [Memoria.] La observación 73 pidió derivar los 8 GB: se necesitan 2.374 MB, y el búfer de 288 horas para el cierre de Los Libertadores pesa menos del 2 %.

Fuente: S4 §4.2.2: equipo a bordo y Tabla de capacidad derivada (2.374 MB) · Caso RT-03.10, RT-06.01, RT-10.05, RT-12.11 · restricciones 5 y 6

## 8. La EDT cubre todo el alcance en 13 elementos.

Tiempo: 40 s. 

Construir el árbol en voz alta. Nivel 0: el proyecto completo. Nivel 1: trece elementos orientados a entregables, no a fases. [Revelar paquetes.] Cada elemento baja a paquetes estimables y asignables: 54 en total; el elemento 5 es el más grande porque replica los contextos de la arquitectura. [Revelar agrupación.] Los elementos 1 a 6 construyen la Etapa 1; los 7 a 13 la acompañan, certifican y operan. La regla del 100 %: la suma de los hijos es el padre, sin vacíos ni dobles conteos.

Fuente: S7 §7.1, Figura 7.1 y Tabla 7.2 · T-14: diccionario de 54 paquetes · PMI (2019): regla del 100 %

## 9. La red de actividades define la ruta crítica.

Tiempo: 55 s. 

[Panorama.] Presentar la carta de 420 días hábiles, con barras rojas para las ventanas sin holgura, líneas de precedencia y rombos en las fechas de acta. [H4.] Sprints y revisión del candidato E1 hasta el día 200 (M10). [H7.] Marcha blanca, corte y revisión del paso a producción E1 hasta el día 320 (M16). [H12.] Marcha blanca E2 del día 360 al 400, corte hasta el 410 y revisión hasta el acta del día 420 (M21). Según S7, las tres actas llegan al límite contractual.

Fuente: T-15: malla CPM final de 122 nodos · S7 §7.3.1 · E-25: actas H1–H12

## 10. El paquete 11.1 se controla con la compuerta G13.

Tiempo: 40 s. 

Conectar la ficha del paquete 11.1 con su control en el cronograma: G13 exige versión probada en PREPROD, datos ficticios y material antes de iniciar los 40 días hábiles de A13 (10 de familiarización y 30 prácticos). Sin G13 disponible, A13 no comienza.

Fuente: T-14: paquete 11.1 · T-15: compuerta G13, actividad A13 (40 d) y reserva A14 · T-16: riesgo R-16

## 11. 36 riesgos evaluados y un riesgo de plazo abierto.

Tiempo: 50 s. 

Mostrar la distribución inicial y recorrer los tres ejemplos de mitigación del T-16. R-17 permanece alto hasta que se validen los plazos, la capacidad y las ventanas de terceros antes de fijar la línea base en H1. Las cifras residuales son objetivos de mitigación.

Fuente: T-16: 36 riesgos con probabilidad, impacto, exposición inicial y residual · S8 §8.1: escalas y umbrales

## 12. Dos reservas protegen las marchas blancas.

Tiempo: 45 s. 

A14 y A23 son ventanas de planificación de 14 y 10 días. R-17 permanece alto hasta validar capacidad, ventanas y estimaciones de tres puntos con los ejecutores. La malla CPM informa márgenes; las probabilidades de cumplimiento quedan sujetas a la validación de la línea base.

Fuente: S7 §7.3.1 · S8 §8.2 · T-15 y T-16 (R-17)

## 13. Proveedores y adquisiciones clave de la solución.

Tiempo: 55 s. 

Mostrar de dónde viene cada pieza y quién la paga. La nube se contrata en Azure. audIT asume cómputo y respaldo eléctrico. El mandante compra equipos de red y de campo conforme a la asignación del T-11. Cada proveedor responde a una restricción técnica ya vista en la arquitectura. El valor por adquisición y los gastos asociados a proveedores están en la planilla económica.

Fuente: T-11: especificaciones ofertadas · S4 §4.2 · T-22 (FEP01 p.69) · economico/datos/partidas.csv

## 14. Curva S del proyecto

Tiempo: 50 s. 

[Curva contractual.] La facturación avanza por hitos hasta H12 en M21. Ese mes se emite la primera factura de operación y el primer cobro mensual llega en M22. Facturación sobre costos desde M17. En M56, la facturación y los costos con intereses totalizan CLP 8.368 y 6.907 millones, respectivamente. [Caja.] Usamos el saldo mensual de la Fila C, con el efecto del IVA. Tras tres meses sin cobros, el mínimo de cierre es CLP 227 millones en M9. El mínimo es mensual. El orden de pagos y cobros dentro del mes se revisa en la sensibilidad de tesorería. El último cobro de operación queda en M57, fuera del horizonte graficado.

Fuente: Sobre 3 · Modelo financiero del 25.11.2026 · hojas «Curva S» (B:C) y «Flujo de Caja» (W) · E-21 y E-25

## 15. Costos por categoría, frente al valor ofertado.

Tiempo: 60 s. 

Las bases evalúan con severidad un presupuesto sobreestimado o subestimado, así que cada categoría debe poder justificarse con el plan de actividades. Mostrar las cuatro categorías del T-22. La lámina desglosa operación en costos propios y servicios de proveedores. Comparar el costo neto total con el precio neto por fase. El margen consolidado se calcula sobre el precio de venta.

Fuente: T-22 (FEP01 p.69): gastos por categoría, con los gastos de proveedores sumados a operación · E-21 · economico/datos/partidas.csv

## 16. VAN y TIR: la evaluación financiera a 56 meses.

Tiempo: 70 s. 

El VAN usa la Fila A de M1 a M56 con M0 en cero. La tasa mensual pondera deuda al 0,9 % mensual y capital propio al 20 % efectivo anual supuesto. La TIR es la raíz reportada por el modelo y su unicidad queda por validar. El VAN sigue positivo en los cuatro escenarios mostrados. Con atraso H5 a M14 y reserva en M12 queda un déficit antes de cobros de CLP 368,65 millones. La facilidad contingente de CLP 420 millones lo cubre en el escenario modelado, sujeto a disponibilidad. El cobro de M57 y los beneficios hipotéticos para Curimón se informan por separado del VAN base.

Fuente: Sobre 3 · Modelo financiero 25.11.2026 (Indicadores y Sensibilidad) · Análisis financiero § Evaluación financiera

## 17. Condiciones comerciales: garantías y pagos por hito.

Tiempo: 40 s. 

Cerrar el bloque económico con lo que el mandante necesita para decidir: las dos garantías que respaldan la oferta, de USD 500.000 por seriedad y de USD 1.000.000 por fiel cumplimiento, y la estructura de pagos por hito, 60 % en la Etapa 1 y 40 % en la Etapa 2, cada pago contra un entregable aceptado. Terminar con el valor ofertado por fase.

Fuente: FEP01 Art. 35° y 36°, p.23 · FEP01 p.74: hitos de pago H1 a H12 · economico/datos/partidas.csv

## 18. Tres compromisos que se pueden verificar.

Tiempo: 50 s. 

Cerrar con tres frases, una por acto, sin repetir las láminas. Qué construimos: una arquitectura híbrida que sigue operando sin enlace. Cómo lo ejecutamos: 54 paquetes y reservas para los inicios de marcha blanca. Cómo lo protegemos: 36 riesgos con disparador, R-17 se mantiene alto hasta validar la línea base. Mencionar que la calidad tiene 120 casos diseñados y abrir las preguntas.

Fuente: Síntesis de la oferta final: S4, S5, S7, S8 y formularios T-11 a T-19

## 19. Preguntas y discusión

Tiempo: 10 s. 

Abrir las preguntas. Si hace falta mostrar un detalle, la tecla B abre el respaldo técnico y Escape vuelve.

Fuente: Transportes Curimón · TFEP-01/2026 · audIT Soluciones Tecnológicas SpA

## 20. Cada nodo declara su hardware y su enlace.

Tiempo: 45 s. Respaldo.

Bajar de la idea al equipo. [Nube.] Lo que se contrata en Azure, por subred, y Brazil South con RPO de 15 minutos y RTO de 4 horas. [Sitios.] San Bernardo va en pares: dos servidores Dell R360, dos FortiGate, clima N+1, detección por aspiración y grupo electrógeno. Cada terminal tiene dos AAEON ICS-6280A en activo y espera y un router 5G. El camión lleva el G26I, el módem Iridium, el lector CAN sin contacto y el lector de tarjeta. [Enlaces.] Cada enlace tiene medio, respaldo y tiempo de conmutación: ExpressRoute de 100 Mbit/s con VPN de respaldo en menos de un minuto; terminal fijo con 5G; camión LTE con Iridium hacia IoT Hub. [Cierre.] Cinco ambientes desde el mismo código. El T-11 detalla los equipos a cargo de audIT y del mandante.

Fuente: S4 §4.2.1: implementos que compra el mandante · §4.2.4: catálogo Azure · §4.2.6: ambientes y respaldos · §4.2.7: enlaces y conmutación · T-11

## 21. Cada dato vive en el motor que su uso exige.

Tiempo: 45 s. Respaldo.

El dato no está en una sola base. [Dominios.] Asignación y vigencias van en PostgreSQL con transacciones: si no hay estado autoritativo, no se confirma una reserva. A bordo, SQLite sigue capturando y sincroniza después. La telemetría entra por Event Hubs a TimescaleDB. La caché, en Managed Redis, nunca habilita con una copia vieja. Documentos y auditoría quedan inmutables en Blob Storage, y la analítica se separa del despacho en Delta Lake. [Volumen.] 96 mil viajes y cerca de 120 millones de posiciones al año, con la retención que fija el Caso. [Migración.] Cuatro fases; las 6.000 vigencias se acreditan una a una con hash, y nada en cuarentena habilita un despacho.

Fuente: S5 Tabla 5.3: persistencia y conducta ante partición · Tabla 5.5: retención · Tabla 5.6: migración · S4 §4.1.20: volumen declarado

## 22. Si se corta el enlace, la operación sigue.

Tiempo: 30 s. Respaldo.

Cortar los enlaces en la misma vista. [Corte.] Lo que exige estado global, asignar un viaje nuevo y emitir el documento, sigue pasando por el servicio central: no se inventan vigencias ni asignaciones. [Autonomía.] San Bernardo y los terminales operan 24 horas: la torre, las emergencias, la consulta de vigencias en portería. El camión guarda al menos 72 horas, y el diseño llega a 288. [Reconexión.] Al volver la señal se sube por lotes con acuse, y la prueba CP-PERF-02 exige 20 minutos para 300 camiones. Este es el puente con los riesgos: estas mismas piezas son las barreras del R-28.

Fuente: S4 §4.1.26: operación desconectada y reconexión · §4.2.3: funciones on-premise · §4.3: plazos sin enlace · FEP01 Art. 16.4 · Caso RT-03.10 y RT-03.13

## 23. Cada elemento baja a paquetes que se pueden aceptar.

Tiempo: 70 s. Respaldo.

Recorrer de izquierda a derecha sin leer paquete por paquete. Columnas 1 y 2: lo que construye la Etapa 1, con el elemento 5 nombrado igual que los contextos de la arquitectura. [Revelar columnas 3 y 4.] Datos, Etapa 2, adhesión, calidad, implantación, innovaciones y operación. [Revelar trazabilidad.] Destacar tres decisiones de diseño: 5.1 a 5.6 son los seis contextos de S4, por lo que cada componente tiene un único paquete que lo construye; 12.1 a 12.5 son las fichas del T-19; y la adhesión es un elemento propio con responsable, porque el Caso exige tratarla como actividad. El elemento 11 produce las actas de los hitos de marcha blanca.

Fuente: S7 Figura 7.1 · T-14: 54 paquetes · S4: seis contextos · T-19: cinco innovaciones · Caso §17.5, p. 40

## 24. El diccionario hace verificable cada paquete.

Tiempo: 60 s. Respaldo.

Tomar un paquete real, el 11.2, y leerlo como lo leería el mandante. [Revelar.] Entregable: lo que se recibe. Criterio: las seis condiciones del Art. 17.3, que se acreditan en los hitos H6 y H7. [Revelar.] Un solo responsable, el Líder de Implantación, y su lugar en la red: A15 y A19, meses 13 a 16. Es el mismo paquete al que llega la traza de la observación 48. [Revelar.] Cerrar con la regla del 100 %: se contrastó contra los 42 requerimientos, los seis contextos, las cinco innovaciones y las once exigencias del Caso; ninguno quedó sin paquete.

Fuente: T-14: paquete 11.2 · S7 Tabla 7.1: cobertura contra el alcance · T-12: RNF-011 · T-17: CP-INT-05 y CP-SYS-05

## 25. La transición se ejecuta en dos etapas niveladas.

Tiempo: 90 s. Respaldo.

Explicar el cronograma en escala proporcional M1–M24 con extensión a M56: E1 entra a marcha blanca en M13–M15 y producción en M16; E2 hace marcha blanca en M19–M20 y producción en M21. Destacar la partición en Células Alfa y Beta durante M13–M15 para evitar sobreasignación.

Fuente: S3 §3.2.4 · S7 §§7.2–7.3 · T-15: nivelación Células Alfa/Beta · T-18: etapas E1/E2 y legado hasta M24

## 26. Diez riesgos con exposición inicial alta.

Tiempo: 50 s. Respaldo.

Mostrar los diez riesgos de exposición inicial alta, sus disparadores y los objetivos de mitigación. R-17 sigue alto mientras se valida la línea base del cronograma.

Fuente: T-16: riesgos con exposición ≥ 12, respuesta, disparador, plazo y exposición residual · S8 §8.3: plan de acción

## 27. R-28: cuatro causas, cuatro barreras antes del evento.

Tiempo: 50 s. Respaldo.

Este es el riesgo que dio origen al bloqueo de salida. [Evento.] Que el documento completo no vuelva a la cabina en 90 segundos. [Causas.] Cuatro caminos: no hay LTE, la carga se conoce sólo en terreno, el documento no cabe en un mensaje satelital o se pierden fragmentos. [Prevención.] Cada uno tiene su barrera: el Iridium, la emisión anticipada, el protocolo fragmentado con integridad y un ensayo en el mes 3 con el peor documento. [Mitigación.] Si aun así ocurre, el camión no sale sin documento conforme, y si el ensayo supera 90 segundos se revisa la decisión de diseño. [AMFE.] Los diez modos de falla quedan bajo 50; los dos más altos se tratan detectando antes.

Fuente: S4 §4.1.13: emisión del documento sin cobertura · T-16: R-28 y análisis de modos de falla · Caso RT-09.01 (90 s) · restricción 8

## 28. Registro de riesgos · R-01 a R-13.

Tiempo: 30 s. Respaldo.

Respaldo para preguntas sobre cualquier riesgo del registro.

Fuente: T-16: identificación, evaluación P×I, respuesta, disparador y exposición residual

## 29. Registro de riesgos · R-14 a R-25.

Tiempo: 30 s. Respaldo.

Respaldo para preguntas sobre cualquier riesgo del registro.

Fuente: T-16: identificación, evaluación P×I, respuesta, disparador y exposición residual

## 30. Registro de riesgos · R-26 a R-37.

Tiempo: 30 s. Respaldo.

Respaldo para preguntas sobre cualquier riesgo del registro.

Fuente: T-16: identificación, evaluación P×I, respuesta, disparador y exposición residual

## 31. El AMFE completo: diez modos bajo NPR 50.

Tiempo: 30 s. Respaldo.

Respaldo del AMFE con los diez modos.

Fuente: T-16: análisis de modos de falla y efectos (S × O × D = NPR, umbral 50)

## 32. El árbol de fallas modela compuertas OR y AND.

Tiempo: 45 s. Respaldo.

Explicar la estructura lógica del árbol de fallas de S8 §8.2: el evento tope ocurre por una compuerta OR superior alimentada por cuatro ramas, donde cada rama requiere la conjunción (compuerta AND) de una falla técnica y una falla de control.

Fuente: S8 §8.2: árbol de fallas con compuerta OR superior y cuatro compuertas AND inferiores

## 33. Sin documento conforme, el viaje no puede salir.

Tiempo: 60 s. Respaldo.

Explicar que se exige el retorno del documento íntegro a la cabina dentro de 90 segundos, separado en un medidor dedicado. La pre-emisión aplica cuando la carga se conoce. El ensayo extremo a extremo sigue pendiente de acreditación en terreno.

Fuente: T-16: R-28 · S8 §8.2 · Caso RT-09.01: presupuesto de retorno documental en 90 s

## 34. La implantación converge en producción aceptada.

Tiempo: 60 s. Respaldo.

Mostrar cómo las tres corrientes operativas (adhesión de al menos 60 de 148 transportistas en M9, montaje mensual por flota y marcha blanca con reversión disponible) convergen directamente en el nodo de producción con aceptación formal.

Fuente: T-16: R-11 (adhesión), R-19 (montaje), R-18 (marcha blanca) · T-18: criterios de salida y reversión

## 35. Los hitos avanzan por evidencia y protegen fechas.

Tiempo: 90 s. Respaldo.

Explicar la cadena de compuertas e hitos: G13 habilita capacitación, H6 y H11 abren las marchas blancas, y H7/H12 formalizan la aceptación. Distinguir claramente entre fecha contractual de hito, holgura de actividad y las reservas explícitas A14 (14 días) y A23 (10 días).

Fuente: S7 §7.3.1 · T-15: G13 y reservas A14 (14 d) / A23 (10 d) · T-18: hitos H6, H7, H11 y H12

## 36. La reversión opera con tiempos y roles definidos.

Tiempo: 45 s. Respaldo.

Detallar el protocolo de reversión de T-18 en cuatro pasos con sus ventanas operativas y responsables, advirtiendo que no deben sumarse como un RTO único.

Fuente: T-18: procedimiento de reversión en 4 fases (15 min, 30 min, 15 min + 20 min/camión, 24 h / 5 d)

## 37. La calidad se controla desde el código hasta terreno.

Tiempo: 60 s. Respaldo.

Cubrir los capítulos S6 y S9 del Informe 2: ciclo iterativo con control de cambios formal y umbral de <=5% de cambios fallidos en producción; compuertas de calidad para hardware (SAE J1455, IP67, pérdida CAN <0,1%) y 120 casos de prueba diseñados en T-17 bajo ISO 29119.

Fuente: S6 / T-9 / T-10: metodología y control de cambios · S9 / T-13 / T-17: aseguramiento de calidad y 120 casos de prueba

## 38. Las correcciones vinculan decisiones y pruebas.

Tiempo: 60 s. Respaldo.

Unificar las tres correcciones estructurales del Informe 1: las observaciones 37 y 43 quedan resueltas en S3 con el esquema conceptual y el calendario de retiro del legado 2013. Para la observación 48, mostrar la cadena completa RNF-011 → 11.2 → CP-INT-05 → CP-SYS-05 advirtiendo que las pruebas están diseñadas, no ejecutadas.

Fuente: S3 §§3.2.4 y 3.3 · T-12: RNF-011 · T-14: 11.2 · T-17: CP-INT-05 y CP-SYS-05

## 39. Las cinco innovaciones distinguen TRL y condiciones.

Tiempo: 45 s. Respaldo.

Usar ante consultas sobre la Sección 13 (Innovaciones): detalla los 5 paquetes del área 12 de la EDT, diferenciando la madurez comercial del componente respecto del TRL de integración en Curimón.

Fuente: S13 · T-19: fichas de innovación 12.1 a 12.5, niveles TRL y supuestos de validación

## 40. La evidencia mantiene límites metodológicos explícitos.

Tiempo: 45 s. Respaldo.

Usar ante preguntas sobre el alcance de las afirmaciones: distinguimos con rigor entre diseño documental verificado y resultados de ejecución en terreno.

Fuente: S3 · S7 · S8 · T-12 / T-15 / T-17 / T-18

## 41. Diccionario EDT · paquetes 1.1 a 2.3.

Tiempo: 30 s. Respaldo.

Vista paginada del diccionario vigente del T-14 para localizar cualquier paquete durante las preguntas de la comisión.

Fuente: T-14: diccionario de la EDT, entregable, criterio, responsable, red y meses por paquete

## 42. Diccionario EDT · paquetes 2.4 a 3.4.

Tiempo: 30 s. Respaldo.

Vista paginada del diccionario vigente del T-14 para localizar cualquier paquete durante las preguntas de la comisión.

Fuente: T-14: diccionario de la EDT, entregable, criterio, responsable, red y meses por paquete

## 43. Diccionario EDT · paquetes 4.1 a 5.3.

Tiempo: 30 s. Respaldo.

Vista paginada del diccionario vigente del T-14 para localizar cualquier paquete durante las preguntas de la comisión.

Fuente: T-14: diccionario de la EDT, entregable, criterio, responsable, red y meses por paquete

## 44. Diccionario EDT · paquetes 5.4 a 6.2.

Tiempo: 30 s. Respaldo.

Vista paginada del diccionario vigente del T-14 para localizar cualquier paquete durante las preguntas de la comisión.

Fuente: T-14: diccionario de la EDT, entregable, criterio, responsable, red y meses por paquete

## 45. Diccionario EDT · paquetes 6.3 a 7.3.

Tiempo: 30 s. Respaldo.

Vista paginada del diccionario vigente del T-14 para localizar cualquier paquete durante las preguntas de la comisión.

Fuente: T-14: diccionario de la EDT, entregable, criterio, responsable, red y meses por paquete

## 46. Diccionario EDT · paquetes 8.1 a 9.1.

Tiempo: 30 s. Respaldo.

Vista paginada del diccionario vigente del T-14 para localizar cualquier paquete durante las preguntas de la comisión.

Fuente: T-14: diccionario de la EDT, entregable, criterio, responsable, red y meses por paquete

## 47. Diccionario EDT · paquetes 9.2 a 11.1.

Tiempo: 30 s. Respaldo.

Vista paginada del diccionario vigente del T-14 para localizar cualquier paquete durante las preguntas de la comisión.

Fuente: T-14: diccionario de la EDT, entregable, criterio, responsable, red y meses por paquete

## 48. Diccionario EDT · paquetes 11.2 a 12.3.

Tiempo: 30 s. Respaldo.

Vista paginada del diccionario vigente del T-14 para localizar cualquier paquete durante las preguntas de la comisión.

Fuente: T-14: diccionario de la EDT, entregable, criterio, responsable, red y meses por paquete

## 49. Diccionario EDT · paquetes 12.4 a 13.4.

Tiempo: 30 s. Respaldo.

Vista paginada del diccionario vigente del T-14 para localizar cualquier paquete durante las preguntas de la comisión.

Fuente: T-14: diccionario de la EDT, entregable, criterio, responsable, red y meses por paquete