# Criterios de aceptación - D2

**Fuente:** FEP03 · Capítulo 18 · pp.41-43\
**Estado:** versión comprometida para el Informe 1 del 07-09-2026

El CLIENTE exige comprometer los 29 resultados, proponer meta cuando no esté fijada,
indicar el hito y cómo se medirá. Este documento distingue tres cosas, y la distinción
es deliberada.

- **Obligatorio** identifica el resultado que las Bases exigen en su texto. El
  PROPONENTE lo compromete sin condición.
- **Meta del PROPONENTE** identifica el umbral que las Bases dejan a propuesta del
  oferente. Es una oferta comprometida, no una exigencia textual, y por eso se declara
  como propia.
- **Parámetro a fijar en la Etapa 1** identifica el valor que no puede establecerse
  responsablemente sin el levantamiento previo. Lo que se compromete es el hito y el
  método con que quedará fijado, no un número inventado antes de medir.

Marcar la diferencia protege al CLIENTE y al PROPONENTE. Un umbral ofrecido como si
fuera exigencia de las Bases confunde la evaluación, y un umbral fijado sin línea base
se incumple después. Parámetros concretos del caso en FEP03 · Capítulo 15 · pp.31-34.

Los mecanismos de solución descritos son propuesta técnica del PROPONENTE y su
implementación se acredita durante la ejecución, no en este informe.

| CA | Resultado y línea base | Meta e hito | Medición | Requisitos |
|---:|---|---|---|---|
| 01 | No se verifica jornada, habilitación ni aptitud al asignar. | **Obligatorio:** cero salidas con incumplimiento legal o de seguridad; E1. | Asignaciones, bloqueos y excepciones auditadas. | RF-001, RF-028 |
| 02 | Jornada en papel para 196 de 454 conductores. | **Obligatorio:** jornada conocida y acreditable para 454/454 al asignar; E1-E2 según adhesión. | Conciliación por conductor, fuente y viaje. | RF-002, RF-028 |
| 03 | Jornada previa externa inexistente. | **Obligatorio:** evidencia previa en toda asignación externa; E1. La cobertura inicial sigue la adhesión y se reporta mes a mes, sin rebajar la exigencia de acreditación. | Muestreo de asignaciones, fuente, sello y bloqueo. | RF-003 |
| 04 | Registro en papel, a veces completado al final del día. | 100 % con autor, origen, sello, integridad e historial; **meta del PROPONENTE**; E1. | Alteración controlada, hashes, WORM y auditoría legal. | RF-004, RNF-012, RNF-014 |
| 05 | Aproximadamente 6.000 vigencias en cuatro planillas. | Registro único y bloqueante; 100 % conciliado; **meta del PROPONENTE**; E1. | Conciliación documental, alertas y bloqueos. | RF-005 |
| 06 | Lista en papel; una detención por documentación incorrecta. | **Obligatorio:** cero despachos con discrepancia carga-manifiesto; E1. | Casos coincidente, discrepante y sin evidencia. | RF-006 |
| 07 | Información del tacógrafo nunca descargada. | 100 % de tacógrafos compatibles incorporados; **meta del PROPONENTE**. Periodicidad de descarga: **parámetro a fijar en la Etapa 1**, conforme al plazo legal que determine la revisión jurídica; E1-E2. | Inventario, registro de descarga, original y hash. | RF-007 |
| 08 | Tres pantallas y 34 camiones sin dispositivo. | Vista única 374/374 indicando fuente, antigüedad y ausencia. Cobertura 80 % al cierre E1, 95 % al cierre E2 y 100 % antes del mes 24: **meta del PROPONENTE**. | Padrón mensual por modo y antigüedad de dato. | RF-008, RF-028 |
| 09 | Los tramos sin señal dejan vacíos. | **Obligatorio:** al menos 72 h, cero registros perdidos; E1. Ventana máxima de sincronización tras reconexión: **parámetro a fijar en la Etapa 1**, sobre la base de RT-03.13 y del ensayo de reconexión masiva. | Ensayo offline, conteo/hash y reconexión simultánea. | RF-009, RNF-002 |
| 10 | Llegadas/salidas anotadas en papel y de memoria. | Registro automático sin acción del conductor ni equipos en el cliente; **Obligatorio**. Radio de geocerca y precisión aceptable: **parámetro a fijar en la Etapa 1**, con la campaña de cobertura y el piloto en terreno; E1. | Piloto, evidencia independiente y falsos cruces. | RF-010, RNF-001, RNF-007 |
| 11 | $340 millones facturados; 71 % objetado. | Objeciones ≤20 % de cobros respaldados; **meta del PROPONENTE**; E2. | Monto y número objetado sobre total presentado. | RF-011 |
| 12 | Evidencia viaja en papel; 4,2 % no llega. | Disponible el mismo día; cero conformidades perdidas y ≥99 % antes del cierre diario; **meta del PROPONENTE**; E1. | Tiempos de entrega, captura y publicación. | RF-012, RNF-007 |
| 13 | Documento redigitado al sistema contable. | 100 % originado desde la orden, sin redigitación y con emisor contable único; E1. | Comparación campo a campo y tasa de intervención manual. | RF-013, RNF-006 |
| 14 | La práctica sin cobertura no resiste examen. | **Exigencia:** solución declarada y conforme para emitir sin cobertura, con documento conforme antes del movimiento y emisor contable único. Mecanismo y prueba del 100 % de escenarios: **meta del PROPONENTE**, condicionada al mecanismo de contingencia que soporte el sistema contable; E1. No basta una solicitud de emisión diferida. | Documento y sello previos al movimiento, bloqueo ante ausencia, pruebas offline, reintentos, folios y validación tributaria. | RF-014, RNF-006 |
| 15 | 26 % de kilómetros en vacío. | Reducir a ≤18 % en población comparable; **meta del PROPONENTE**; E2. | Kilómetros vacíos/total por GPS y viaje. | RF-015 |
| 16 | Solo existe una planilla construida en junio de 2026. | ≥95 % de viajes con costo trazable y 100 % de rutas/contratos modelados; **meta del PROPONENTE**; E1. | Cobertura y conciliación contable. | RF-016, RF-017 |
| 17 | Combustible disponible hasta 40 días después. | **Obligatorio:** costo por viaje disponible en 24 h del cierre. **Parámetro FEP03 RT-05.29:** costo consolidado con componentes disponibles y faltantes explícitos. Versionado preliminar y consolidado con historial: **meta del PROPONENTE**, sujeta a validación de que satisface el parámetro y no solo su denominación; E1. | Tiempo cierre-publicación ≤24 h, componentes incluidos/faltantes y conciliación posterior; contrastar con costo real CA-16/19. | RF-016 |
| 18 | Dispersión de 19 % no investigada. | Modelo reproducible que explique ≥80 % de la variación comparable; **meta del PROPONENTE**; E2. | Validación por modelo, ruta, carga y conductor. | RF-018 |
| 19 | Dos contratos bajo costo se renegocian en 2027. | Costo disponible antes de ambas renegociaciones y 100 % de sus rutas cubiertas; **meta del PROPONENTE**; E1. | Acta de disponibilidad y expediente contractual. | RF-016 |
| 20 | Liquidación: 9 días, 8 personas y 11 % corregido. | ≤1 día hábil y ≤2 % de correcciones; **meta del PROPONENTE**; E1. | Tiempo, usuarios y tasa de corrección en paralelo. | RF-019 |
| 21 | El transportista se informa al recibir el documento. | Consulta en cualquier momento para todo transportista habilitado; **Obligatorio**. Nivel de servicio del portal comprometido en el modelo operativo; E1. | Aceptación, disponibilidad y segregación. | RF-020 |
| 22 | Seguimiento del cliente inexistente. | Posición y estado solo durante el servicio y según autorización; **Obligatorio**. La cobertura efectiva sigue la adhesión y se reporta mes a mes; E1. | Acceso antes, durante y después; antigüedad del dato. | RF-021 |
| 23 | No existe control de datos compartidos. | 100 % de permisos granulares; revocación efectiva ≤5 min; **meta del PROPONENTE**; E1. | Casos de permiso, revocación y pruebas negativas. | RF-022, RNF-013, RNF-014 |
| 24 | Emisiones no medidas. | **Exigencia:** emisiones por tonelada-kilómetro con metodología declarada/verificable, incluidos terceros; consolidación mensual según FEP03 RT-05.29. **Meta del PROPONENTE:** base y metodología en E1, cálculo productivo completo en E2. Cobertura y precisión del factor por tercero: **parámetro a fijar en la Etapa 1**, con la línea base medida. | E1: revisión de fuentes, línea base y método; E2: reproducción independiente y consolidación mensual con fuentes versionadas, incluidos terceros. E1 no acredita cumplimiento completo. | RF-023 |
| 25 | Intervenciones externas no quedan registradas. | ≥95 % recibidas y 100 % de las validadas en hoja de vida; **meta del PROPONENTE**; E2. | Conciliación con facturas, aprobaciones y hoja de vida. | RF-024 |
| 26 | Odómetro leído al pasar por taller. | 100 % de unidades con telemetría gatilladas por kilometraje real; restantes marcadas como estimadas; **meta del PROPONENTE**; E1-E2. | Comparación telemetría-odómetro y órdenes. | RF-025 |
| 27 | No existe conversación de adhesión. | ≥70 % (104/148) adheridos al cierre E1 y ≥90 % (134/148) al cierre E2; **meta del PROPONENTE**. | Registro contractual de invitación, respuesta y capacidades. | RF-026, RF-028 |
| 28 | Alerta existente, pero no considera dónde detenerse. | 100 % calculadas con jornada y lugar seguro alcanzable; **meta del PROPONENTE**. Margen de anticipación por ruta: **parámetro a fijar en la Etapa 1**, derivado del catastro de lugares seguros; E1-E2. | Hora, jornada restante, ETA y catálogo validado. | RF-027, RNF-001 |
| 29 | El dueño se entera nueve días después y no controla datos. | Todo adherido consulta camiones, viajes, liquidación y permisos revocables; **meta del PROPONENTE**; frecuencia de actualización fijada con el piloto de portal de la Etapa 1; E1. | Aceptación, segregación, consentimiento y auditoría. | RF-020, RF-022, RNF-013 |

## Supuestos declarados de estas metas

Las metas anteriores se comprometen bajo los supuestos siguientes. Se declaran de forma
expresa porque, si alguno no se verifica, la meta correspondiente cambia y el PROPONENTE
prefiere decirlo ahora antes que ajustarla durante la ejecución.

1. **Cobertura telemática.** Las metas de 80 %, 95 % y 100 % suponen la frecuencia de
   paso por terminal declarada en las Bases, cada 6 días en promedio, con un 22 % de la
   flota subcontratada que pasa menos de una vez al mes. Si la frecuencia real es menor,
   la meta se recalcula sobre el ritmo medido y no sobre el promedio.
2. **Cobertura de flota y adhesión son indicadores distintos.** El porcentaje de camiones
   con posición no equivale al porcentaje de transportistas adheridos, porque los 148
   transportistas tienen entre uno y cuatro camiones cada uno. Ninguna meta de este
   documento mezcla ambas magnitudes.
3. **Costeo en 24 horas.** La meta supone que un costo consolidado con componentes
   disponibles y pendientes explícitos satisface el parámetro RT-05.29. El PROPONENTE
   consultó formalmente este punto. Si la respuesta exigiera el costo completo en 24
   horas, la meta es inalcanzable mientras el combustible llegue con 40 días de desfase,
   y debe replantearse el hito, no el mecanismo.
4. **Jornada externa y documento tributario.** Las metas de CA-02, CA-03 y CA-14 suponen
   que la evidencia propuesta tiene valor probatorio y que existe un mecanismo de
   contingencia soportado por el sistema contable. Ambos extremos requieren validación
   jurídica y confirmación del proveedor contable, y así está declarado en el capítulo 6
   del Subdocumento 3.
5. **Emisiones.** La meta reparte base y metodología en la Etapa 1 y cálculo productivo
   completo en la Etapa 2. Esa distribución no rebaja CA-24, lo escalona, y la exigencia
   del cliente exportador es para 2029.
6. **Líneas base de vacío y rendimiento.** Las metas de CA-15 y CA-18 se miden sobre
   población comparable, definida en la Etapa 1. Sin esa definición, una comparación
   entre flotas distintas no significa nada.
7. **Financiamiento.** Todas las metas ofrecidas están dentro del costo total de
   operación de 36 meses declarado en RNF-010, y ninguna supone gasto no presupuestado.

Los contratos servidos bajo costo son 3, equivalentes al 31 % del ingreso, y 2 de ellos
se renegocian en 2027 (FEP03 · Sección 7.3 · p.15 y Sección 13.2 · p.27).
