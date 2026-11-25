# Registro de decisiones D2 - Ignacio C. y Matías V.

## Numeral 16.1 - Caso 10: Transporte de Carga

**Empresa proponente:** AudIT  
**Responsables:** Ignacio C. y Matías V.  
**Área:** D2 - Esquema de solución y alcance  
**Estado:** Borrador de trabajo  
**Última actualización:** 29-08-2026

---

## 1. Objetivo

Registrar las 26 decisiones que el CLIENTE dejó expresamente a cargo del PROPONENTE, documentando para cada una:

- Supuesto o decisión adoptada.
- Fundamento operacional, técnico, contractual o normativo.
- Alternativas evaluadas.
- Consecuencias sobre alcance, arquitectura, costo y cronograma.
- Impacto si el supuesto resulta incorrecto.
- Instancia de validación.
- Artefactos de la propuesta afectados.

Este registro alimentará el catálogo RF/RNF, la división por etapas, el Formulario T-12, la arquitectura, la EDT, los riesgos y los criterios de aceptación.

---

## 2. Estados

| Estado | Significado |
|---|---|
| Pendiente | Decisión identificada, todavía sin propuesta |
| Propuesta | Existe una alternativa redactada por D2 |
| Acordada | Revisada y aceptada por las duplas involucradas |
| Por validar | Requiere confirmación del CLIENTE, asesoría legal o prueba técnica |
| Validada | Existe evidencia suficiente para incorporarla como decisión definitiva |

---

## 3. Inventario de decisiones

| N.º | Decisión pendiente | Responsable principal | Dependencias | Estado |
|---:|---|---|---|---|
| 1 | Obtener y acreditar la jornada de un conductor externo, incluyendo conducción previa para otros clientes | D2 | D3, legal, transportistas | Propuesta |
| 2 | Definir qué se ofrece a los 148 transportistas y qué ocurre con quien no adhiere | D2 | D1, D3, D4, contratos | Propuesta |
| 3 | Definir el destino del sistema de gestión de transporte de 2013 | D2/D3 | Interfaces actuales, migración | Pendiente |
| 4 | Unificar la posición de tres proveedores y cubrir 34 camiones sin dispositivo | D3 | D2, proveedores, D4 | Pendiente |
| 5 | Definir propiedad, financiamiento, administración y retiro del dispositivo instalado en camiones de terceros | D2/D4 | Contratos, costos | Pendiente |
| 6 | Definir la regla de excepción cuando el bloqueo impide un viaje comprometido | D2 | Prevención, operaciones, auditoría | Pendiente |
| 7 | Definir la anticipación de la alerta de agotamiento de jornada | D2/D3 | Lugares seguros, rutas, posición | Pendiente |
| 8 | Registrar llegada y salida en instalaciones de terceros sin acción del conductor ni equipos en el cliente | D2/D3 | Geocercas, integraciones, posición | Pendiente |
| 9 | Emitir el documento electrónico de transporte en un punto sin cobertura | D2/D3 | Sistema contable, normativa | Pendiente |
| 10 | Obtener la conformidad de entrega y dejarla disponible el mismo día | D2/D3 | Firma, destinatario, modo desconectado | Pendiente |
| 11 | Definir frecuencia de muestreo, transmisión y almacenamiento de posición y telemetría | D2/D3/D4 | Datos móviles, retención, batería | Pendiente |
| 12 | Incorporar la telemetría de fábrica de 61 tractocamiones | D3 | Fabricantes, autorización, interfaces | Pendiente |
| 13 | Descargar, conservar y proteger los datos de tacógrafos digitales | D2/D3 | Normativa, integridad, operación | Pendiente |
| 14 | Definir el criterio de asignación de carga de retorno | D2 | Torre, clientes, optimización | Pendiente |
| 15 | Construir el costo de viaje con datos que llegan en momentos distintos | D2/D3 | Finanzas, contabilidad, analítica | Pendiente |
| 16 | Estimar el costo real de un camión subcontratado cuando sólo se conoce su tarifa | D2 | Transportistas, contratos, finanzas | Pendiente |
| 17 | Tratar los tres contratos bajo costo y disponer de información antes de la renegociación de 2027 | D2 | Finanzas, Etapa 1 | Pendiente |
| 18 | Controlar aproximadamente 6.000 vigencias cuando el titular del documento es un tercero | D2 | Transportistas, reglas, notificaciones | Pendiente |
| 19 | Verificar que la documentación de carga peligrosa corresponda a la carga efectiva | D2 | Cliente cargador, conductor, normativa | Pendiente |
| 20 | Operar ante cierres del paso fronterizo de hasta 12 días | D2/D3 | Jornada, rutas, contingencia | Pendiente |
| 21 | Incorporar intervenciones de talleres externos a la hoja de vida del equipo | D2 | Talleres, portal, mantenimiento | Pendiente |
| 22 | Calcular emisiones por tonelada-kilómetro, incluidos camiones de terceros | D2/D3 | Consumo, carga, metodología | Pendiente |
| 23 | Definir qué datos de viaje y posición se comparten con clientes según autorización del dueño | D2/D3 | Consentimiento, portal, auditoría | Pendiente |
| 24 | Proteger la evidencia de jornada frente a alegaciones de manipulación | D2/D3 | Seguridad, firma, auditoría | Pendiente |
| 25 | Desplegar equipamiento en 374 camiones según su paso real por terminales | D2/D4 | Adhesión, inventario, logística | Propuesta |
| 26 | Operar durante el período mixto con flota equipada y no equipada | D2/D3/D4 | Etapas, convivencia, reversión | Pendiente |

**Avance:** 3 de 26 decisiones con propuesta inicial.

---

## 4. Decisión 1 - Jornada de conductores externos

### 4.1 Pregunta

¿Cómo obtiene y acredita AudIT la jornada de conducción de una persona que no es trabajadora de Transportes Curimón y que pudo haber conducido previamente para otro cliente?

### 4.2 Propuesta inicial

Implementar un **expediente digital de jornada por conductor** que consolide evidencia de distintas fuentes y se consulte obligatoriamente antes de confirmar una asignación.

La evidencia se obtendrá mediante este orden de preferencia:

1. Datos firmados o exportados desde el tacógrafo digital o dispositivo a bordo.
2. Registros de viajes y eventos capturados por la plataforma de AudIT.
3. Información aportada por el transportista mediante portal o API, respaldada por una declaración electrónica del conductor y del transportista.
4. Procedimiento de contingencia documental sólo cuando una fuente técnica no esté disponible, conservando la evidencia y sometiéndola a revisión posterior.

Antes de asignar un viaje, la plataforma consolidará la actividad disponible, calculará la jornada y los descansos conforme a reglas parametrizadas y entregará uno de estos resultados:

- **Habilitado:** evidencia suficiente y jornada disponible.
- **No habilitado:** jornada insuficiente o incumplimiento comprobado.
- **Información incompleta:** no existe evidencia suficiente para acreditar el cumplimiento.

Los estados **No habilitado** e **Información incompleta** bloquearán la asignación. Una contingencia de integración no permitirá ignorar una jornada legalmente insuficiente. Cualquier procedimiento excepcional deberá limitarse a acreditar el dato por una fuente alternativa admitida, no a omitir la obligación.

### 4.3 Integridad y valor probatorio

- Cada evento conservará fuente, fecha, hora, zona horaria, conductor, vehículo y viaje.
- Los registros se almacenarán en una bitácora inalterable con trazabilidad de origen.
- Las correcciones conservarán el valor anterior, motivo, evidencia y responsables.
- Una corrección requerirá aprobación de un segundo perfil cuando afecte una asignación o una obligación regulatoria.
- La evidencia tendrá sello de tiempo y firma o mecanismo equivalente admitido por la normativa aplicable.
- Se conservará durante al menos cinco años, de acuerdo con el parámetro RT-05.10 del caso.
- Todo acceso, exportación y modificación quedará auditado.

### 4.4 Identificación y consentimiento

- El conductor se identificará al inicio del turno o viaje mediante un mecanismo compatible con dispositivos compartidos y sin interacción durante la marcha.
- El contrato de adhesión definirá la obligación del transportista de aportar información verificable.
- El conductor recibirá información sobre finalidad, datos tratados, retención, acceso y mecanismos de corrección.
- El consentimiento no se utilizará como sustituto de otra base jurídica que la normativa determine obligatoria.
- La validez legal del mecanismo será confirmada durante el levantamiento con asesoría especializada.

### 4.5 Alternativas descartadas

| Alternativa | Motivo del descarte |
|---|---|
| Declaración verbal del conductor | No ofrece integridad, trazabilidad ni valor probatorio suficiente |
| Considerar sólo viajes realizados para Curimón | Omite conducción previa para otros clientes y reproduce el problema actual |
| Depender únicamente del tacógrafo | No garantiza acceso oportuno ni homogéneo en toda la flota |
| Permitir asignar cuando no hay información | Convierte la falta de datos en autorización y mantiene el riesgo que originó la licitación |

### 4.6 Impacto si el supuesto resulta incorrecto

- Bloqueo excesivo de viajes si las fuentes externas no entregan datos oportunamente.
- Riesgo legal si la evidencia propuesta no es admisible ante la autoridad.
- Baja adhesión si el mecanismo es percibido como invasivo.
- Costos adicionales por integración con fabricantes o proveedores.

### 4.7 Validaciones requeridas

- [ ] Confirmar medios legalmente admitidos para acreditar jornada.
- [ ] Confirmar disponibilidad de tacógrafos e interfaces.
- [ ] Validar la regla de corrección y doble aprobación.
- [ ] Validar el tratamiento de datos personales y de localización.
- [ ] Probar el flujo con conductores y transportistas reales.
- [ ] Acordar con D3 el diseño de auditoría, firma e integración.

### 4.8 Artefactos afectados

- Catálogo RF/RNF.
- Plan de adhesión.
- Módulo de asignación.
- Arquitectura de integración y seguridad.
- Formulario T-12.
- Criterios de aceptación 1 a 4, 27, 28 y 29.
- Innovación de modelo de negocio o contratación.

**Estado:** Propuesta; requiere validación legal, técnica y contractual.

---

## 5. Decisión 2 - Adhesión de los 148 transportistas

### 5.1 Pregunta

¿Qué ofrece AudIT a los transportistas subcontratados a cambio de aportar sus datos y participar en la solución, y qué ocurre con quienes no adhieren?

### 5.2 Propuesta inicial

Ejecutar un **Programa de Adhesión Digital de Transportistas** basado en beneficios verificables, incorporación contractual progresiva y control granular de los datos compartidos.

### 5.3 Propuesta de valor para el transportista

- Portal con consulta de viajes asignados, ejecutados y pendientes de cierre.
- Liquidación en curso con desglose y evidencia de cada concepto.
- Notificación temprana de diferencias para corregirlas antes del cierre mensual.
- Acceso a evidencias de jornada, entrega, tiempos de espera y cumplimiento.
- Alertas de vencimientos de conductores y equipos.
- Menor tiempo de liquidación y menor tasa de correcciones.
- Control sobre qué datos de sus camiones y conductores se comparten, con quién y hasta cuándo.
- Historial de cumplimiento utilizable para acreditar su operación ante Curimón.
- Dispositivo, instalación inicial y soporte sin desembolso inicial para el transportista, sujeto al modelo económico definitivo.

### 5.4 Instrumento contractual

La adhesión se formalizará mediante un anexo al contrato de transporte que cubra:

- Datos requeridos y finalidad de tratamiento.
- Responsabilidad por calidad y oportunidad de la información.
- Propiedad y administración del dispositivo.
- Consentimientos y autorizaciones aplicables.
- Niveles de servicio de intercambio de información.
- Soporte, actualización, reposición y retiro del equipamiento.
- Beneficios e incentivos asociados a la adhesión.
- Consecuencias operacionales de no adherir.
- Procedimiento de revocación y término de la relación.

### 5.5 Ejecución por olas

| Período | Actividad | Meta preliminar |
|---|---|---|
| Meses 1-2 | Segmentación, diseño contractual y mesas de trabajo | 100 % de transportistas contactados |
| Meses 3-4 | Piloto con transportistas voluntarios representativos | 15 transportistas y al menos 30 camiones activos |
| Meses 5-8 | Primera ola en rutas y clientes prioritarios | 50 % de la capacidad subcontratada cubierta |
| Meses 9-12 | Segunda ola y extensión territorial | 75 % de la capacidad subcontratada cubierta |
| Meses 13-15 | Cierre de brechas durante marcha blanca | 90 % de la capacidad subcontratada cubierta o contingencia aprobada |

Las metas son preliminares y se ajustarán con el inventario real, la frecuencia de paso por terminal y el resultado del piloto.

### 5.6 Medición

- Porcentaje de transportistas contactados.
- Porcentaje con anexo contractual firmado.
- Porcentaje de camiones enrolados.
- Porcentaje de conductores identificados y capacitados.
- Porcentaje de viajes con jornada acreditada.
- Porcentaje de transportistas que consultan su liquidación.
- Tasa de correcciones de liquidación.
- Tiempo medio entre adhesión y activación.
- Porcentaje de consentimientos vigentes, revocados o restringidos.

### 5.7 Tratamiento de quienes no adhieren

Durante el período transitorio se habilitará un procedimiento controlado de evidencia alternativa, sin prometer funciones que dependan de datos no disponibles.

Después del plazo contractual de adhesión:

- No se asignarán al transportista servicios que exijan jornada acreditada, posición compartida u otras condiciones que no pueda demostrar.
- No se presentará al cliente información que el dueño del camión no haya autorizado.
- La continuidad para servicios compatibles quedará sujeta a reglas contractuales y de riesgo definidas por Curimón.
- Toda excepción será explícita, temporal, auditable y no podrá rebajar una obligación legal.

### 5.8 Alternativas descartadas

| Alternativa | Motivo del descarte |
|---|---|
| Imponer la solución por instrucción laboral | Los transportistas y 258 conductores no son trabajadores de Curimón |
| Exigir datos sin entregar beneficios | Reduce la probabilidad de adhesión y contradice las entrevistas del caso |
| Mantener exactamente la operación actual para quien no adhiere | Haría imposible cumplir los criterios de aceptación para la mayor parte de la flota |
| Desconectar inmediatamente a todo transportista no adherido | Generaría un riesgo operacional y de capacidad incompatible con una transición gradual |

### 5.9 Impacto si el supuesto resulta incorrecto

- Adhesión menor a la necesaria para cumplir los criterios del caso.
- Incremento del costo de dispositivos, soporte e incentivos.
- Resistencia por tratamiento de datos o percepción de vigilancia.
- Pérdida temporal de capacidad si transportistas relevantes no adhieren.

### 5.10 Validaciones requeridas

- [ ] Confirmar cláusulas existentes en contratos de transporte.
- [ ] Validar beneficios con una muestra de transportistas.
- [ ] Acordar propiedad y financiamiento con D4 y la dimensión económica.
- [ ] Validar metas de cobertura con el calendario de paso por terminal.
- [ ] Revisar protección de datos y consentimiento.
- [ ] Definir servicios permitidos para no adherentes durante la transición.

### 5.11 Artefactos afectados

- Alcance de Etapa 1 y Etapa 2.
- Catálogo RF/RNF.
- Portal del transportista.
- Cronograma e implantación.
- Arquitectura de identidad, integración y datos.
- Riesgos del proyecto.
- Innovaciones D2.
- Criterios de aceptación 27 y 29.

**Estado:** Propuesta; requiere validación contractual, económica y con transportistas.

---

## 6. Decisión 25 - Despliegue del equipamiento a bordo

### 6.1 Pregunta

¿Cómo se despliega el equipamiento en 374 camiones cuando sólo puede intervenirse en un terminal, un camión pasa cada seis días en promedio y el 22 % de la flota subcontratada aparece menos de una vez al mes?

### 6.2 Propuesta inicial

Realizar un **despliegue progresivo por olas y oportunidad de paso por terminal**, coordinado con el Programa de Adhesión y manteniendo operación mixta hasta alcanzar la cobertura requerida.

El despliegue no requerirá detener la flota fuera de sus pasos operacionales normales por terminal. Cada instalación se programará como una orden de trabajo vinculada al camión, transportista, terminal y ventana estimada de llegada.

### 6.3 Preparación

- Construir un inventario único de los 374 camiones, propietario, terminal habitual, ruta, dispositivo existente, fabricante y compatibilidad.
- Clasificar unidades propias, subcontratadas frecuentes y subcontratadas de baja frecuencia.
- Preparar kits preconfigurados por tipo de vehículo.
- Validar que la instalación no afecte garantía ni sistemas de seguridad.
- Capacitar equipos instaladores en los cinco terminales.
- Definir una instalación estándar, pruebas de aceptación y evidencia fotográfica/técnica.
- Mantener stock de contingencia y repuestos por terminal.

### 6.4 Olas propuestas

| Ola | Período | Población | Objetivo preliminar |
|---|---|---|---|
| 0 | Meses 1-2 | Inventario y laboratorio | Compatibilidad y procedimiento validados |
| 1 | Meses 3-4 | Flota propia y transportistas piloto | Al menos 30 camiones operativos |
| 2 | Meses 5-8 | Camiones de mayor frecuencia y rutas prioritarias | 50 % de la flota cubierta |
| 3 | Meses 9-12 | Resto de unidades con paso regular | 75 % de la flota cubierta |
| 4 | Meses 13-15 | Unidades de baja frecuencia y brechas | 90 % o más, con excepciones identificadas |

Las metas se validarán mediante simulación con los datos reales de paso por terminal. No se comprometerá una cobertura mensual que contradiga la frecuencia observada.

### 6.5 Unidades de baja frecuencia

Para el 22 % de la flota subcontratada que pasa menos de una vez al mes:

- Concertar cita de instalación vinculada a un viaje o renovación contractual.
- Ofrecer incentivo de adhesión y coordinación anticipada.
- Mantener kits disponibles en el terminal más probable.
- Activar aviso automático cuando la unidad sea programada hacia un terminal.
- No realizar intervención en ruta ni en instalaciones de clientes.
- Registrar formalmente las unidades aún no equipadas y aplicar el modo transitorio definido en la decisión 26.

### 6.6 Proceso por unidad

1. Confirmación de adhesión y autorización del propietario.
2. Validación de compatibilidad y garantía.
3. Reserva de kit y técnico en el terminal.
4. Instalación durante la permanencia operacional normal.
5. Prueba de energía, posicionamiento, almacenamiento local y comunicación.
6. Asociación entre dispositivo, vehículo, propietario y conductor activo.
7. Entrega de acta, propiedad, soporte y condiciones de uso.
8. Seguimiento remoto y aceptación después de un período de observación.

### 6.7 Actualización y soporte

- Las actualizaciones ordinarias serán remotas, firmadas y reversibles.
- La intervención física se reservará para fallas, reemplazos o incompatibilidades.
- El dispositivo mantendrá 72 horas de operación desconectada.
- La gestión central registrará versión, configuración, estado, propietario y garantía.
- Todo reemplazo conservará la trazabilidad del dispositivo retirado y del nuevo.

### 6.8 Alternativas descartadas

| Alternativa | Motivo del descarte |
|---|---|
| Instalar toda la flota en una ventana masiva | No existe ventana de detención y la flota opera 24x7x365 |
| Intervenir camiones en ruta | Está prohibido por las restricciones del caso |
| Exigir asistencia extraordinaria sin incentivo | No es realista para transportistas externos de baja frecuencia |
| Esperar cobertura total para iniciar la marcha blanca | Retrasaría el aprendizaje y desconoce la transición prolongada del caso |

### 6.9 Impacto si el supuesto resulta incorrecto

- Cobertura inferior a la requerida para cerrar la marcha blanca.
- Sobrecarga de técnicos o falta de kits en terminales.
- Retrasos por incompatibilidades de vehículo o restricciones de garantía.
- Extensión del período mixto y aumento de procedimientos manuales.
- Incremento del costo de inventario y desplazamiento.

### 6.10 Validaciones requeridas

- [ ] Obtener historial real de paso por terminal por vehículo.
- [ ] Confirmar modelos y condiciones de garantía.
- [ ] Validar duración máxima admisible de instalación.
- [ ] Simular cobertura acumulada por mes.
- [ ] Definir capacidad diaria de instalación por terminal.
- [ ] Acordar propiedad, financiamiento y reposición.
- [ ] Coordinar con D4 las especificaciones del dispositivo.
- [ ] Coordinar con D3 el enrolamiento, actualización y observabilidad.

### 6.11 Artefactos afectados

- Alcance y etapas.
- Plan de adhesión.
- Arquitectura física.
- Plan de implantación.
- Cronograma y nivelación de recursos.
- Criterios de avance de marcha blanca.
- Riesgos de adopción y despliegue.
- Costos de hardware, instalación, datos y soporte.

**Estado:** Propuesta; requiere simulación con datos operacionales y coordinación con D3/D4.

---

## 7. Próximas decisiones a resolver

El siguiente bloque debe trabajarse en este orden:

1. **Decisión 5:** propiedad y financiamiento del dispositivo, porque completa las decisiones 2 y 25.
2. **Decisión 6:** regla de excepción al bloqueo, porque completa la decisión 1.
3. **Decisión 3:** destino del sistema de gestión de 2013, porque habilita la arquitectura.
4. **Decisión 23:** consentimiento y datos compartidos, porque afecta portal, posición e innovación.
5. **Decisión 26:** operación mixta, porque conecta alcance e implantación.
6. **Decisiones 8, 9 y 10:** evidencia del ciclo de viaje y operación sin cobertura.

---

## 8. Control de revisión

| Decisión | D1 | D2 | D3 | D4 | Legal/cliente | Estado final |
|---:|---|---|---|---|---|---|
| 1 |  | Ignacio C. / Matías V. |  | N/A |  | Propuesta |
| 2 |  | Ignacio C. / Matías V. |  |  |  | Propuesta |
| 25 | N/A | Ignacio C. / Matías V. |  |  |  | Propuesta |
