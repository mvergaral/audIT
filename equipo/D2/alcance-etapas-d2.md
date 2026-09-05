# Alcance por etapas - D2

**Subdocumento 3 · Esquema de solución y alcance**\
**Estado:** propuesta para revisión de Ignacio C. y Matías V.

Todas las etapas, salidas y puertas de avance siguientes son propuestas no ratificadas,
no resultados ya obtenidos. La distribución temporal no rebaja exigencias de las Bases.

## 1. Criterio de distribución

El reparto no replica el orden de preferencias del comité. Se basa en cinco criterios:

1. **Riesgo legal y operacional:** primero se controlan jornada, habilitaciones,
   documentos tributarios, carga peligrosa y evidencia.
2. **Dependencias:** no se escala hardware ni analítica antes de conocer interfaces,
   calidad de datos, cobertura y compatibilidad vehicular.
3. **Adopción:** ninguna capacidad dependiente de terceros se masifica antes de probar
   adhesión, consentimiento y beneficio para el transportista.
4. **Continuidad:** la solución debe convivir con sistemas y flota actuales sin una
   detención general.
5. **Valor medible:** Etapa 1 establece líneas base y datos confiables; Etapa 2 usa
   esos datos para optimizar y ampliar cobertura.

## 2. Etapa 1 - Fundamento seguro y piloto operacional

### Objetivo

Controlar los riesgos que pueden causar un despacho ilegal, pérdida probatoria,
duplicación tributaria o tratamiento indebido de datos, y validar las dependencias
técnicas y contractuales antes de un despliegue masivo.

### Capacidades incluidas

| Capacidad | Requisitos | Resultado de Etapa 1 |
|---|---|---|
| Despacho seguro | RF-001, RF-002, RF-003, RF-028 | Validación de jornada, vigencias, aptitud y nivel de evidencia antes de asignar |
| Evidencia y documentos | RF-004, RF-005, RF-006, RF-007, RNF-012, RNF-014 | Registro maestro, trazabilidad, integridad y pilotos de carga/tacógrafo |
| Posición y operación offline | RF-008, RF-009, RF-010, RNF-001, RNF-002 | Vista única piloto, geocercas y almacenamiento mínimo de 72 h |
| Viaje y facturación | RF-011, RF-012, RF-013, RF-014, RNF-006, RNF-007 | Evidencia de permanencia/entrega; documento conforme antes del movimiento aun sin cobertura, con emisor contable único e integración idempotente |
| Costos y liquidación | RF-016, RF-017, RF-019 | Costo consolidado en 24 h con componentes disponibles y faltantes explícitos según FEP03 RT-05.29; versionado propuesto por validar y liquidación por excepción |
| Base de emisiones | RF-023 | Fuentes, línea base y metodología declarada/verificable, incluidos terceros; preparación de consolidación mensual, no cálculo productivo completo |
| Portales y consentimiento | RF-020, RF-021, RF-022, RF-026, RNF-003, RNF-013 | Portal mínimo, segregación, adhesión y permisos granulares |
| Flota y mantenimiento | RF-025, RF-027 | Pilotos de kilometraje real y alerta de lugar seguro |
| Implantación y operación | RNF-004, RNF-005, RNF-008, RNF-009, RNF-010, RNF-011 | Pilotos por familia, continuidad, RACI, TCO y despliegue progresivo |

### Entradas obligatorias

- Padrones de 374 tractocamiones, 210 semirremolques, 454 conductores, 148
  transportistas y 84 clientes.
- Las cuatro planillas de vigencias y sus respaldos.
- Inventario e interfaces verificadas del TMS y sistema contable de 2013.
- Inventario de las tres plataformas GPS y derechos de integración.
- Marca, modelo, año y acceso rFMS/CAN de los 61 tractocamiones.
- Contratos, tarifas, reglas de liquidación y fuentes de costos.
- Campaña de cobertura y levantamiento de lugares seguros.
- Revisión legal de jornada externa, tacógrafo, consentimiento y retención.
- Modelo contractual de adhesión, propiedad, soporte y retiro del dispositivo.

### Salidas

- Catálogo RF/RNF y matriz de trazabilidad ratificados.
- Registro de decisiones sin vacíos críticos.
- Registro único de vigencias y documentos saneados.
- Núcleo de despacho bloqueante y auditable.
- Integración con el sistema contable sin redigitación ni doble emisión.
- Costeo básico por viaje, ruta y contrato antes de la renegociación de 2027.
- Piloto offline, telemático y de geocercas sobre unidades autorizadas.
- Vista que distinga cobertura completa, homologada, documental y no disponible.
- Portal mínimo de transportista y cliente con segregación comprobada.
- Plan de adhesión probado con una cohorte representativa.
- Catálogo inicial de lugares seguros y alertas validadas en ruta.
- Base y metodología de emisiones documentadas para el cálculo productivo completo E2.
- TCO de 36 meses por escenarios y plan de despliegue progresivo.

### Criterios de avance a Etapa 2

- [ ] Cero discrepancias críticas en maestros y vigencias habilitantes.
- [ ] Bloqueos legales y de seguridad aprobados, sin excepciones indebidas.
- [ ] Prueba offline de 72 horas sin pérdida, desorden ni duplicados.
- [ ] Continuidad lógica equivalente a un cierre fronterizo de 12 días probada.
- [ ] Documento conforme antes del movimiento sin cobertura y emisión única del contable ante caída/reintentos; bloqueo si falta documento.
- [ ] Costo consolidado en 24 h con faltantes explícitos; validación de que el versionado propuesto satisface el parámetro, no solo su denominación.
- [ ] Fuentes, línea base y metodología de emisiones revisadas, incluidos terceros; alcance E1/E2 ratificado antes de comprometerlo.
- [ ] Cadena de custodia y auditoría append-only validadas.
- [ ] Consentimiento representable por camión, viaje, dato, destinatario y periodo.
- [ ] Interfaces vehiculares autorizadas por fabricante para cada familia piloto.
- [ ] Inventario de equipos de terceros clasificado y conciliado.
- [ ] Adhesión contractual probada con una cohorte representativa.
- [ ] Mapa de cobertura y catálogo de lugares seguros aprobados.
- [ ] Dispositivo con disponibilidad, repuestos y soporte para el horizonte del proyecto.
- [ ] Operación y contingencia ejecutables por el equipo TI del CLIENTE.

### Exclusiones de Etapa 1

- Despliegue indiscriminado sobre los 374 camiones.
- Intervención de equipos o electrónica de terceros sin acuerdo expreso.
- Optimización productiva de retornos.
- Analítica avanzada de rendimiento.
- Cálculo productivo completo de emisiones.
- Workflow completo de talleres externos.
- Compra masiva antes de aceptar pilotos.
- Instalación de infraestructura en recintos de clientes.
- Sustitución del sistema contable como emisor tributario.
- Compromisos basados exclusivamente en consultas no respondidas.

## 3. Etapa 2 - Escalamiento, adopción y optimización

### Objetivo

Escalar las capacidades validadas y usar datos estabilizados para optimización,
analítica, sostenibilidad y ampliación de cobertura, sin forzar la intervención de
terceros no adheridos.

### Capacidades incluidas

| Capacidad | Requisitos | Resultado de Etapa 2 |
|---|---|---|
| Optimización de retornos | RF-015 | Recomendaciones bajo restricciones y reducción medible de kilómetros vacíos |
| Rendimiento operacional | RF-018 | Explicación reproducible de dispersión entre camiones comparables |
| Emisiones verificables | RF-023 | Cálculo productivo completo de CO2e por tonelada-kilómetro, incluidos terceros, con método/factores versionados y consolidación mensual |
| Talleres externos | RF-024 | Registro offline, aprobación e incorporación a la hoja de vida |
| Escalamiento telemático | RF-002, RF-003, RF-007, RF-008, RF-009, RF-025 | Cobertura ampliada según adhesión, compatibilidad y autorización |
| Maduración de portales | RF-020, RF-021, RF-022, RF-026 | Autoservicio, consentimiento y auditoría completos |
| Analítica avanzada de costos | RF-016, RF-017 | Modelos avanzados sin sacrificar el costo básico ya disponible en E1 |

### Entradas

- Acta de salida y resultados de pilotos de Etapa 1.
- Datos operacionales y financieros con calidad medida.
- Transportistas adheridos y autorizaciones por fabricante.
- Línea base de kilómetros vacíos, rendimiento, objeciones y emisiones.
- Mapa de cobertura y segmentación del riesgo de conectividad.
- TCO actualizado con cantidades y consumos reales.

### Salidas

- Despliegue progresivo a flota propia y terceros adheridos.
- Homologación de plataformas de terceros sin reemplazo forzoso.
- Conformidad digital y evidencia de carga peligrosa estabilizadas.
- Recomendador de retornos y analítica de rendimiento.
- Cálculo verificable de emisiones.
- Portal de talleres externos y actualización de hoja de vida.
- Portales y consentimiento con cobertura ampliada.
- Indicadores de adopción, calidad, cobertura, costo y beneficio.

### Criterios de cierre

- [ ] Cobertura y nivel de evidencia reportados por unidad.
- [ ] El modo documental no se presenta como equivalente al telemático.
- [ ] Metas ratificadas con línea base para vacío, objeciones, rendimiento y emisiones.
- [ ] Segregación de datos aprobada mediante pruebas negativas.
- [ ] Conciliaciones financieras y documentales dentro de tolerancias acordadas.
- [ ] Disponibilidad, recuperación y resiliencia demostradas bajo carga.
- [ ] TCO real dentro de límites aprobados.
- [ ] Despliegue sin detención global y con reversión probada.

### Exclusiones de Etapa 2

- Capacidades que requieran datos de transportistas no adheridos.
- Acceso open-book no autorizado.
- Sustitución del sistema contable como emisor tributario.
- Instalación de equipos en puntos de carga o descarga.
- Intervención vehicular no autorizada por dueño o fabricante.
- Promesa de visibilidad donde no exista señal, exportación o adhesión.

## 4. Dependencias entre etapas

| Dependencia | E1 produce | E2 consume |
|---|---|---|
| Datos maestros | Identidades y vigencias saneadas | Optimización y analítica confiables |
| Telemetría | Interfaces y calidad comprobadas | Cobertura y mantenimiento ampliados |
| Adhesión | Contrato, incentivo y piloto | Escalamiento sobre terceros |
| Consentimiento | Modelo granular y auditoría | Visibilidad ampliada para clientes |
| Costeo | Costo consolidado en 24 h con faltantes explícitos; versionado por validar | Rentabilidad y optimización avanzada |
| Emisiones | Base de datos, línea base y metodología | Cálculo productivo completo y consolidación mensual, incluidos terceros |
| Cobertura | Mapa y almacenamiento offline | Segmentación móvil/satelital |
| Lugares seguros | Catálogo piloto validado | Alertas y planificación a escala |
| Equipamiento | Pilotos por familia | Compra e instalación progresivas |

## 5. Decisiones que pueden alterar el alcance

1. D-05: propiedad y financiamiento del dispositivo.
2. D-10: mecanismo de conformidad de entrega.
3. D-12 y D-13: acceso a telemetría y tacógrafo por modelo.
4. D-14: función objetivo del retorno.
5. D-19: evidencia de carga peligrosa efectiva.
6. D-21: captura y aprobación de talleres externos.
7. D-23: retención frente a revocación.
8. D-25 y D-26: cobertura física y operación mixta.
9. D-22: distribución propuesta de emisiones, base/metodología E1 y productivo completo E2.
10. D-09 y D-15/D-17: viabilidad tributaria antes del movimiento y costeo conforme en 24 h.
