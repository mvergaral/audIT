# Criterios de aceptación - D2

**Fuente:** FEP03 · Capítulo 18 · pp.41-43\
**Estado:** propuesta para ratificación

El CLIENTE exige comprometer los 29 resultados, proponer meta cuando no esté fijada,
indicar el hito y cómo se medirá. Las metas marcadas **D2, por ratificar** son oferta
del equipo, no exigencias textuales de las Bases.

Los hitos E1/E2 y los mecanismos de solución son propuestas no ratificadas; la palabra
**Obligatorio** identifica el resultado exigido, no la aprobación de su implementación
ni evidencia de cumplimiento. Parámetros concretos: FEP03 · Capítulo 15 · pp.31-34.

| CA | Resultado y línea base | Meta e hito | Medición | Requisitos |
|---:|---|---|---|---|
| 01 | No se verifica jornada, habilitación ni aptitud al asignar. | **Obligatorio:** cero salidas con incumplimiento legal o de seguridad; E1. | Asignaciones, bloqueos y excepciones auditadas. | RF-001, RF-028 |
| 02 | Jornada en papel para 196 de 454 conductores. | **Obligatorio:** jornada conocida y acreditable para 454/454 al asignar; E1-E2 según adhesión. | Conciliación por conductor, fuente y viaje. | RF-002, RF-028 |
| 03 | Jornada previa externa inexistente. | **Obligatorio:** evidencia previa en toda asignación externa; cobertura inicial por ratificar; E1. | Muestreo de asignaciones, fuente, sello y bloqueo. | RF-003 |
| 04 | Registro en papel, a veces completado al final del día. | 100 % con autor, origen, sello, integridad e historial; **D2, por ratificar**; E1. | Alteración controlada, hashes, WORM y auditoría legal. | RF-004, RNF-012, RNF-014 |
| 05 | Aproximadamente 6.000 vigencias en cuatro planillas. | Registro único y bloqueante; 100 % conciliado; **D2, por ratificar**; E1. | Conciliación documental, alertas y bloqueos. | RF-005 |
| 06 | Lista en papel; una detención por documentación incorrecta. | **Obligatorio:** cero despachos con discrepancia carga-manifiesto; E1. | Casos coincidente, discrepante y sin evidencia. | RF-006 |
| 07 | Información del tacógrafo nunca descargada. | 100 % de tacógrafos compatibles incorporados; periodicidad por ratificar; E1-E2. | Inventario, registro de descarga, original y hash. | RF-007 |
| 08 | Tres pantallas y 34 camiones sin dispositivo. | Vista única 374/374 indicando fuente, antigüedad y ausencia. Cobertura 80 % E1, 95 % E2 y 100 % antes del mes 24: **propuesta por ratificar**. | Padrón mensual por modo y antigüedad de dato. | RF-008, RF-028 |
| 09 | Los tramos sin señal dejan vacíos. | **Obligatorio:** al menos 72 h, cero registros perdidos; E1. Sincronización máxima: por ratificar. | Ensayo offline, conteo/hash y reconexión simultánea. | RF-009, RNF-002 |
| 10 | Llegadas/salidas anotadas en papel y de memoria. | Registro automático sin acción del conductor ni equipos en el cliente; precisión por ratificar; E1. | Piloto, evidencia independiente y falsos cruces. | RF-010, RNF-001, RNF-007 |
| 11 | $340 millones facturados; 71 % objetado. | Objeciones ≤20 % de cobros respaldados; **D2, por ratificar**; E2. | Monto y número objetado sobre total presentado. | RF-011 |
| 12 | Evidencia viaja en papel; 4,2 % no llega. | Disponible el mismo día; cero conformidades perdidas y ≥99 % antes del cierre diario; **D2, por ratificar**; E1. | Tiempos de entrega, captura y publicación. | RF-012, RNF-007 |
| 13 | Documento redigitado al sistema contable. | 100 % originado desde la orden, sin redigitación y con emisor contable único; E1. | Comparación campo a campo y tasa de intervención manual. | RF-013, RNF-006 |
| 14 | La práctica sin cobertura no resiste examen. | **Exigencia:** solución declarada y conforme para emitir sin cobertura, con documento conforme antes del movimiento y emisor contable único. Mecanismo y prueba del 100 % de escenarios: **D2, condicionados y por ratificar**; E1. No basta una solicitud de emisión diferida. | Documento y sello previos al movimiento, bloqueo ante ausencia, pruebas offline, reintentos, folios y validación tributaria. | RF-014, RNF-006 |
| 15 | 26 % de kilómetros en vacío. | Reducir a ≤18 % en población comparable; **D2, por ratificar**; E2. | Kilómetros vacíos/total por GPS y viaje. | RF-015 |
| 16 | Solo existe una planilla construida en junio de 2026. | ≥95 % de viajes con costo trazable y 100 % de rutas/contratos modelados; **D2, por ratificar**; E1. | Cobertura y conciliación contable. | RF-016, RF-017 |
| 17 | Combustible disponible hasta 40 días después. | **Obligatorio:** costo por viaje disponible en 24 h del cierre. **Parámetro FEP03 RT-05.29:** costo consolidado con componentes disponibles y faltantes explícitos. Versionado preliminar/consolidado e historial: **propuesta D2 por validar**, no equivalencia aprobada; E1 propuesto. | Tiempo cierre-publicación ≤24 h, componentes incluidos/faltantes y conciliación posterior; contrastar con costo real CA-16/19. | RF-016 |
| 18 | Dispersión de 19 % no investigada. | Modelo reproducible que explique ≥80 % de la variación comparable; **D2, por ratificar**; E2. | Validación por modelo, ruta, carga y conductor. | RF-018 |
| 19 | Dos contratos bajo costo se renegocian en 2027. | Costo disponible antes de ambas renegociaciones y 100 % de sus rutas cubiertas; **D2, por ratificar**; E1. | Acta de disponibilidad y expediente contractual. | RF-016 |
| 20 | Liquidación: 9 días, 8 personas y 11 % corregido. | ≤1 día hábil y ≤2 % de correcciones; **D2, por ratificar**; E1. | Tiempo, usuarios y tasa de corrección en paralelo. | RF-019 |
| 21 | El transportista se informa al recibir el documento. | Consulta en cualquier momento para todo transportista habilitado; disponibilidad por ratificar; E1. | Aceptación, disponibilidad y segregación. | RF-020 |
| 22 | Seguimiento del cliente inexistente. | Posición/estado solo durante el servicio y según autorización; cobertura por ratificar; E1. | Acceso antes, durante y después; antigüedad del dato. | RF-021 |
| 23 | No existe control de datos compartidos. | 100 % de permisos granulares; revocación efectiva ≤5 min; **D2, por ratificar**; E1. | Casos de permiso, revocación y pruebas negativas. | RF-022, RNF-013, RNF-014 |
| 24 | Emisiones no medidas. | **Exigencia:** emisiones por tonelada-kilómetro con metodología declarada/verificable, incluidos terceros; consolidación mensual según FEP03 RT-05.29. **Propuesta D2 no ratificada:** base y metodología E1; cálculo productivo completo E2; cobertura/precisión por ratificar. | E1: revisión de fuentes, línea base y método; E2: reproducción independiente y consolidación mensual con fuentes versionadas, incluidos terceros. E1 no acredita cumplimiento completo. | RF-023 |
| 25 | Intervenciones externas no quedan registradas. | ≥95 % recibidas y 100 % de las validadas en hoja de vida; **D2, por ratificar**; E2. | Conciliación con facturas, aprobaciones y hoja de vida. | RF-024 |
| 26 | Odómetro leído al pasar por taller. | 100 % de unidades con telemetría gatilladas por kilometraje real; restantes marcadas como estimadas; **D2, por ratificar**; E1-E2. | Comparación telemetría-odómetro y órdenes. | RF-025 |
| 27 | No existe conversación de adhesión. | ≥70 % (104/148) adheridos al cierre E1 y ≥90 % (134/148) al cierre E2; **D2, por ratificar**. | Registro contractual de invitación, respuesta y capacidades. | RF-026, RF-028 |
| 28 | Alerta existente, pero no considera dónde detenerse. | 100 % calculadas con jornada y lugar seguro alcanzable; margen por ruta por ratificar; E1-E2. | Hora, jornada restante, ETA y catálogo validado. | RF-027, RNF-001 |
| 29 | El dueño se entera nueve días después y no controla datos. | Todo adherido consulta camiones, viajes, liquidación y permisos revocables; actualización por ratificar; E1. | Aceptación, segregación, consentimiento y auditoría. | RF-020, RF-022, RNF-013 |

## Controles antes de comprometer metas

- [ ] Ratificar metas 80/95/100 de cobertura telemática con D4.
- [ ] No confundir cobertura de flota con porcentaje de transportistas adheridos.
- [ ] Validar el versionado propuesto contra el costo consolidado en 24 h de FEP03 RT-05.29 y el costo real de CA-16/19; no equiparar automáticamente costo preliminar y cumplimiento.
- [ ] Validar jurídicamente jornada externa, evidencia y documento tributario conforme antes del movimiento, incluso sin cobertura.
- [ ] Ratificar base/metodología de emisiones E1 y cálculo productivo completo E2, sin rebajar CA-24.
- [ ] Unificar cuántos contratos están bajo costo y cuáles se renegocian en 2027.
- [ ] Acordar líneas base y poblaciones comparables para vacío y rendimiento.
- [ ] Confirmar que las metas ofrecidas sean financiables en el TCO de 36 meses.
