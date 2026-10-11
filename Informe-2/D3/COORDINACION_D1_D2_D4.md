# Puntos de D3 para coordinar con D1, D2 y D4 — Informe 2

## Para D1 — Calidad y pruebas

En D3 ya vinculamos los 42 requisitos de T-12 con sus componentes, paquetes EDT y casos del catálogo T-17. Necesitamos que S9, T-13 y T-17 mantengan los siguientes criterios al integrar la entrega:

- **Evidencia de jornada:** niveles 1 tacógrafo, 2 equipo identificado, 3 fábrica, 4 reposo, 5 atestación y 0 registro voluntario. Evidencia ausente o inválida no se convierte en nivel 0. La evaluación admite varias fuentes y registra el veredicto aunque no haya evidencia válida. RN-04 no permite levantar un impedimento legal.
- **Asignación:** el límite de 30 s corresponde al proceso completo. Incluir el cambio concurrente de una vigencia o permiso, la reserva y los reintentos; verificar que un reintento no duplique la asignación.
- **Documento sin cobertura:** comprobar la recepción de una representación completa y conforme antes del movimiento, con el límite de 90 s del camino satelital. Folio o hash aislados no demuestran que cabina dispone del documento.
- **Concurrencia y reconexión:** D3 quedó provisionalmente en 380 usuarios y 570 de estrés; D4 usa 350/525. Acordemos una pareja común para dimensionamiento y pruebas. La prueba de 300 reconexiones es otro escenario: recuperación de 72 h en hasta 20 min por unidad.
- **Custodia y recuperación:** contemplar alteración por administradores, rectificaciones como nuevos registros, revocación de permisos y restauración conjunta de datos, documentos y eventos. Un hash o una copia diaria por sí solos no acreditan estos controles.

Las referencias de aceptación corresponden al catálogo existente de T-17. Estas comprobaciones son criterios para el proyecto; el Informe 2 no las presenta como ensayos ejecutados.

## Para D2 — Alcance, planificación y economía

Necesitamos conciliar S3/T-12 y S7 con estos puntos del diseño de D3:

- **Documento sin cobertura:** S3 menciona el folio de retorno; S4.1 exige que cabina reciba la representación completa y conforme. Acordemos el contenido, tamaño máximo y camino de retorno con D4. Si el enlace no puede cumplir 90 s, hay que ajustar la solución y T-11 antes de afirmar cumplimiento.
- **Innovación de proceso, ficha T-19 tipo 2:** preparé una propuesta de programación dinámica de intervenciones según oportunidades reales de patio. La instalación sin detener la flota ya es una obligación y no basta para justificar la innovación. Necesitamos acordar la incorporación de esta propuesta a S13 y sus métricas, y reflejarla en EDT 12.2 con integración a 4.1/4.2.
- **Calendario de esa ficha:** se adoptó el piloto de 10 camiones en M6, montaje propio M6–M9, terceros adheridos desde M7, pausa M11–M15 y continuación M16–M18. Revisemos que S7/T-18 y la ficha consolidada usen los mismos meses.
- **Valorización:** faltan costos incrementales del planificador, integración, homologación y operación, y su reflejo en partidas y flujo de caja. No duplicar el stock contractual de T-11 ni presentar ahorros medidos sin línea base; las metas del piloto son propuestas. Los valores vacíos de la fuente económica siguen pendientes.
- **Transición del legado:** S4.1/S5 conservan los cortes M16 para tarifas y liquidación de transportistas y M21 para contratos y facturación de clientes, con consulta del transporte antiguo hasta M24. Revisemos su correspondencia con S3 y S7; el sistema contable continúa como emisor fiscal.

La [ficha propuesta T-19 tipo 2](./formulario_t19_innovacion_2_proceso.md) reúne el diseño, calendario, métricas y riesgos que debemos conciliar.

## Para D4 — Infraestructura, equipos y riesgos

Necesitamos que S4.2/T-11 y S8/T-16 sean coherentes con estas decisiones de D3:

- **Stack y servicios:** S4.1 usa .NET 10, Go 1.27, PostgreSQL 16, TimescaleDB Apache-2 sobre PostgreSQL Flexible, Event Hubs Premium con protocolo Kafka y Azure Managed Redis. Confirmemos versiones compatibles, extensiones, productos, capacidad, cuotas y zonas realmente disponibles para la región elegida, y traslademos las decisiones acordadas a T-11.
- **Capacidad:** acordar con D1 los usuarios simultáneos y el estrés (D3: 380/570 provisional; D4: 350/525). Separar esa carga del crecimiento 3× y de las 300 reconexiones para que recursos y casos de prueba correspondan al mismo escenario.
- **Retorno satelital:** fijar con D2 el tamaño de la representación documental y demostrar factibilidad del límite de 90 s. El diseño contempla mensajes SBD de hasta 340 bytes de subida y 270 de bajada, descontando cabeceras y usando fragmentación/reensamblado; ese tamaño de mensaje no acredita la latencia completa.
- **Almacenamiento a bordo:** confirmar memoria útil, reserva, consumo y recuperación para las 72 h requeridas y la ampliación propuesta a 288 h. No equiparar un cierre vial de doce días con doce días sin enlace ni trasladar ese plazo sólo a la caché de Redis.
- **Recuperación y sitio alterno:** conciliar RPO ≤15 min y RTO ≤4 h incluyendo bases, objetos documentales y eventos. Si se mantiene Brazil South, documentar el mecanismo de transferencia y su viabilidad; si no resulta admisible, seleccionar otro sitio antes de afirmar cumplimiento de DR.
- **Innovación tipo 2:** confirmar compatibilidad del equipo y agente, recuperación ante actualización fallida, familias de kit, tiempos de sustitución y disponibilidad física durante el paso normal por terminal. Incorporar a S8/T-16 los riesgos del planificador y su contingencia manual, sin prometer intervenciones de terceros sin adhesión.
