# Guion de exposición

Objetivo: 14 minutos y 25 segundos + 35 segundos de margen. No hay asignación ficticia de expositores.

## 1. Revisión 2 · Caso Transporte de Carga

Tiempo: 15 s. 

Presentar el alcance de la revisión: correcciones del Informe 1, riesgos de solución, proyecto e implantación, EDT, planificación e hitos. La exposición dura 15 minutos y deja 15 minutos para preguntas.

Fuente: Transportes Curimón · TFEP-01/2026 · audIT Soluciones Tecnológicas SpA

## 2. Una salida segura exige información confiable.

Tiempo: 30 s. 

Abrir desde la operación real. El camión se desplaza sobre un carril dedicado mientras se activan los tres controles bloqueantes inferiores: conductor, vehículo y documento deben aportar evidencia válida antes de autorizar la salida.

Fuente: S2 · S3 §3.3 · S8: verificación bloqueante de salida

## 3. La solución conecta cabina, terminal y torre.

Tiempo: 45 s. 

Recorrer el viaje del dato desde la cabina hasta la torre de control. El terminal aporta validación y sincronización. La torre coordina la operación y se integra mediante bus con el ERP contable (emisor tributario), posicionamiento y transportistas.

Fuente: S3 §3.3 · S3 §3.2.4: recorrido operacional e integraciones externas

## 4. La arquitectura integra borde, nube y trazabilidad.

Tiempo: 60 s. 

Explicar las tres capas técnicas del Informe 2: en el borde (S4.2/T-11), 374 gateways, 61 interfaces CANclick no invasivas y buffer local de 8 GB; en la nube (S4.1), ingesta asíncrona y continuidad en San Bernardo advirtiendo su condición de contingencia regional; en datos (S5), la entidad EvidenciaJornada y la migración de 96.000 viajes/año.

Fuente: S4.1: arquitectura lógica · S4.2 / T-11: equipamiento a bordo · S5: modelo de datos y migración

## 5. Las correcciones vinculan decisiones y pruebas.

Tiempo: 60 s. 

Unificar las tres correcciones estructurales del Informe 1: las observaciones 37 y 43 quedan resueltas en S3 con el esquema conceptual y el calendario de retiro del legado 2013. Para la observación 48, mostrar la cadena completa RNF-011 → 11.2 → CP-INT-05 → CP-SYS-05 advirtiendo que las pruebas están diseñadas, no ejecutadas.

Fuente: S3 §§3.2.4 y 3.3 · T-12: RNF-011 · T-14: 11.2 · T-17: CP-INT-05 y CP-SYS-05

## 6. La calidad se controla desde el código hasta terreno.

Tiempo: 60 s. 

Cubrir los capítulos S6 y S9 del Informe 2: ciclo iterativo con control de cambios formal y umbral de <=5% de cambios fallidos en producción; compuertas de calidad para hardware (SAE J1455, IP67, pérdida CAN <0,1%) y 120 casos de prueba diseñados en T-17 bajo ISO 29119.

Fuente: S6 / T-9 / T-10: metodología y control de cambios · S9 / T-13 / T-17: aseguramiento de calidad y 120 casos de prueba

## 7. El método P×I evalúa y reduce la exposición.

Tiempo: 60 s. 

Presentar los tres ámbitos de riesgo y la escala ordinal P×I a la izquierda. A la derecha, mostrar cómo los controles reducen la exposición estimada de R-28 (12→8), R-16 (8→4) y R-11 (12→8), recalcando que no son porcentajes y que el impacto sigue exigiendo contingencia.

Fuente: S8 §8.1 · T-16: matriz de exposición inicial y residual en escala ordinal 1–25

## 8. Sin documento conforme, el viaje no puede salir.

Tiempo: 60 s. 

Explicar que se exige el retorno del documento íntegro a la cabina dentro de 90 segundos, separado en un medidor dedicado. La pre-emisión aplica cuando la carga se conoce. El ensayo extremo a extremo sigue pendiente de acreditación en terreno.

Fuente: T-16: R-28 · S8 §8.2 · Caso RT-09.01: presupuesto de retorno documental en 90 s

## 9. El AMFE prioriza controles de detección temprana.

Tiempo: 60 s. 

Presentar el AMFE promovido al recorrido principal: severidad, ocurrencia y detección para equipo a bordo (NPR 36), módem satelital (NPR 32) y respaldo eléctrico (NPR 18). Todos quedan bajo el umbral 50 gracias a controles de detección anticipada.

Fuente: T-16: Análisis de Modos y Efectos de Falla (AMFE) · S8 §8.2

## 10. La implantación converge en producción aceptada.

Tiempo: 60 s. 

Mostrar cómo las tres corrientes operativas (adhesión de al menos 60 de 148 transportistas en M9, montaje mensual por flota y marcha blanca con reversión disponible) convergen directamente en el nodo de producción con aceptación formal.

Fuente: T-16: R-11 (adhesión), R-19 (montaje), R-18 (marcha blanca) · T-18: criterios de salida y reversión

## 11. La EDT estructura 54 paquetes e integra innovaciones.

Tiempo: 60 s. 

Presentar la descomposición de 54 paquetes en 13 áreas. Destacar el área 11 (Implantación) que conectaremos en la lámina siguiente y el área 12 (S13/T-19) con las 5 innovaciones propuestas y su piloto entre M13 y M15.

Fuente: S7 §7.1 · T-14: 54 paquetes en 13 áreas · S13 / T-19: 5 fichas de innovación (área 12)

## 12. El paquete 11.1 se controla con la compuerta G13.

Tiempo: 60 s. 

Conectar la ficha del paquete 11.1 con su control en el cronograma: G13 exige versión probada en PREPROD, datos ficticios y material antes de iniciar los 40 días hábiles de A13 (10 de familiarización y 30 prácticos). Sin G13 disponible, A13 no comienza.

Fuente: T-14: paquete 11.1 · T-15: compuerta G13, actividad A13 (40 d) y reserva A14 · T-16: riesgo R-16

## 13. La transición se ejecuta en dos etapas niveladas.

Tiempo: 90 s. 

Explicar el cronograma en escala proporcional M1–M24 con extensión a M56: E1 entra a marcha blanca en M13–M15 y producción en M16; E2 hace marcha blanca en M19–M20 y producción en M21. Destacar la partición en Células Alfa y Beta durante M13–M15 para evitar sobreasignación.

Fuente: S3 §3.2.4 · S7 §§7.2–7.3 · T-15: nivelación Células Alfa/Beta · T-18: etapas E1/E2 y legado hasta M24

## 14. Los hitos avanzan por evidencia y protegen fechas.

Tiempo: 90 s. 

Explicar la cadena de compuertas e hitos: G13 habilita capacitación, H6 y H11 abren las marchas blancas, y H7/H12 formalizan la aceptación. Distinguir claramente entre fecha contractual de hito, holgura de actividad y las reservas explícitas A14 (14 días) y A23 (10 días).

Fuente: S7 §7.3.1 · T-15: G13 y reservas A14 (14 d) / A23 (10 d) · T-18: hitos H6, H7, H11 y H12

## 15. La propuesta vincula arquitectura, riesgos y control.

Tiempo: 45 s. 

Cerrar sintetizando los tres pilares verificables de la propuesta: arquitectura y correcciones trazables, riesgos y calidad con umbrales explícitos, y ejecución controlada por compuertas y reservas. Queda abierta la sesión de preguntas con apoyo del respaldo técnico.

Fuente: Síntesis integral Informe 2: S2–S9 y S13 · Formularios T-9 a T-19

## 16. Preguntas y discusión

Tiempo: 10 s. 

Abrir los 15 minutos de preguntas. Usar el respaldo técnico para profundizar en riesgos, trazabilidad, cronograma y criterios de aceptación.

Fuente: Transportes Curimón · TFEP-01/2026 · audIT Soluciones Tecnológicas SpA

## 17. La evidencia mantiene límites metodológicos explícitos.

Tiempo: 45 s. Respaldo.

Usar ante preguntas sobre el alcance de las afirmaciones: distinguimos con rigor entre diseño documental verificado y resultados de ejecución en terreno.

Fuente: S3 · S7 · S8 · T-12 / T-15 / T-17 / T-18

## 18. Cada riesgo crítico tiene dueño, umbral y respuesta.

Tiempo: 45 s. Respaldo.

Respaldo directo para preguntas de gobernanza de riesgos: muestra quién responde, qué umbral numérico dispara la alerta y qué contingencia se activa en cada ámbito.

Fuente: T-16: registro de riesgos R-28, R-16 y R-11 con responsables y disparadores cuantitativos

## 19. Las cinco innovaciones distinguen TRL y condiciones.

Tiempo: 45 s. Respaldo.

Usar ante consultas sobre la Sección 13 (Innovaciones): detalla los 5 paquetes del área 12 de la EDT, diferenciando la madurez comercial del componente respecto del TRL de integración en Curimón.

Fuente: S13 · T-19: fichas de innovación 12.1 a 12.5, niveles TRL y supuestos de validación

## 20. El árbol de fallas modela compuertas OR y AND.

Tiempo: 45 s. Respaldo.

Explicar la estructura lógica del árbol de fallas de S8 §8.2: el evento tope ocurre por una compuerta OR superior alimentada por cuatro ramas, donde cada rama requiere la conjunción (compuerta AND) de una falla técnica y una falla de control.

Fuente: S8 §8.2: árbol de fallas con compuerta OR superior y cuatro compuertas AND inferiores

## 21. La reversión opera con tiempos y roles definidos.

Tiempo: 45 s. Respaldo.

Detallar el protocolo de reversión de T-18 en cuatro pasos con sus ventanas operativas y responsables, advirtiendo que no deben sumarse como un RTO único.

Fuente: T-18: procedimiento de reversión en 4 fases (15 min, 30 min, 15 min + 20 min/camión, 24 h / 5 d)

## 22. La EDT detalla sus paquetes (1–6).

Tiempo: 30 s. Respaldo.

Los criterios de aceptación completos permanecen en T-14 y en el diccionario CSV. Esta vista paginada permite localizar cualquier paquete durante las preguntas de la comisión.

Fuente: T-14 · Diccionario_EDT.csv: catálogo completo de paquetes de trabajo

## 23. La EDT detalla sus paquetes (7–12).

Tiempo: 30 s. Respaldo.

Los criterios de aceptación completos permanecen en T-14 y en el diccionario CSV. Esta vista paginada permite localizar cualquier paquete durante las preguntas de la comisión.

Fuente: T-14 · Diccionario_EDT.csv: catálogo completo de paquetes de trabajo

## 24. La EDT detalla sus paquetes (13–18).

Tiempo: 30 s. Respaldo.

Los criterios de aceptación completos permanecen en T-14 y en el diccionario CSV. Esta vista paginada permite localizar cualquier paquete durante las preguntas de la comisión.

Fuente: T-14 · Diccionario_EDT.csv: catálogo completo de paquetes de trabajo

## 25. La EDT detalla sus paquetes (19–24).

Tiempo: 30 s. Respaldo.

Los criterios de aceptación completos permanecen en T-14 y en el diccionario CSV. Esta vista paginada permite localizar cualquier paquete durante las preguntas de la comisión.

Fuente: T-14 · Diccionario_EDT.csv: catálogo completo de paquetes de trabajo

## 26. La EDT detalla sus paquetes (25–30).

Tiempo: 30 s. Respaldo.

Los criterios de aceptación completos permanecen en T-14 y en el diccionario CSV. Esta vista paginada permite localizar cualquier paquete durante las preguntas de la comisión.

Fuente: T-14 · Diccionario_EDT.csv: catálogo completo de paquetes de trabajo

## 27. La EDT detalla sus paquetes (31–36).

Tiempo: 30 s. Respaldo.

Los criterios de aceptación completos permanecen en T-14 y en el diccionario CSV. Esta vista paginada permite localizar cualquier paquete durante las preguntas de la comisión.

Fuente: T-14 · Diccionario_EDT.csv: catálogo completo de paquetes de trabajo

## 28. La EDT detalla sus paquetes (37–42).

Tiempo: 30 s. Respaldo.

Los criterios de aceptación completos permanecen en T-14 y en el diccionario CSV. Esta vista paginada permite localizar cualquier paquete durante las preguntas de la comisión.

Fuente: T-14 · Diccionario_EDT.csv: catálogo completo de paquetes de trabajo

## 29. La EDT detalla sus paquetes (43–48).

Tiempo: 30 s. Respaldo.

Los criterios de aceptación completos permanecen en T-14 y en el diccionario CSV. Esta vista paginada permite localizar cualquier paquete durante las preguntas de la comisión.

Fuente: T-14 · Diccionario_EDT.csv: catálogo completo de paquetes de trabajo

## 30. La EDT detalla sus paquetes (49–54).

Tiempo: 30 s. Respaldo.

Los criterios de aceptación completos permanecen en T-14 y en el diccionario CSV. Esta vista paginada permite localizar cualquier paquete durante las preguntas de la comisión.

Fuente: T-14 · Diccionario_EDT.csv: catálogo completo de paquetes de trabajo