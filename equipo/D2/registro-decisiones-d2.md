# Registro de decisiones de diseño - D2

**Ignacio C. y Matías V. · Esquema de solución y alcance**

**Caso 10 · Transporte de Carga · Transportes Curimón S.A.**

**Estado:** decisiones ratificadas por D2; validaciones externas pendientes

**Ratificación D2:** Ignacio C. y Matías V. acordaron las 26 decisiones y las metas
indicadas en este registro el 6 de septiembre de 2026. La ratificación fija el alcance
que propone D2, pero no sustituye las validaciones jurídicas, tributarias, comerciales
o técnicas identificadas en la columna correspondiente.

**Fuente principal:** FEP03 · sección 16.1 · p.34

## 1. Cómo usar este registro

Este documento convierte las 26 decisiones pendientes de las Bases en propuestas de
trabajo trazables. Una propuesta no se considera acordada hasta que D2 la ratifique y,
cuando corresponda, la coordine con D1, D3 o D4.

No existe en el repositorio un Acta de Respuestas a Consultas. Por ello, las propuestas
de interpretación incluidas en las consultas no se tratan como respuestas ni como
acuerdos del CLIENTE.

### Estados

- **Propuesta:** existe una solución suficientemente concreta para revisarla.
- **Propuesta parcial:** existe una dirección, pero faltan elementos relevantes.
- **Abierta:** no existe una solución suficiente y requiere diseño inmediato.
- **Ratificada:** acordada por el equipo y apta para alimentar requisitos y alcance.
- **Ratificada D2:** acordada por la dupla para la propuesta; puede conservar
  validaciones externas pendientes sin volver a abrir la decisión de alcance.

## 2. Decisiones críticas ratificadas y validaciones pendientes

Desarrollo de D-01: `decision-01-jornada-externa.md`. Incluye alternativas,
recomendación, bloqueo ante evidencia insuficiente, contingencias y verificación
por grupo. D2 ratificó la alternativa multifuente y el bloqueo sin excepción
operacional; siguen pendientes la validación jurídica y las verificaciones por grupo.

Las decisiones de alcance están tomadas. Antes de declarar viabilidad o cumplimiento
deben validarse estas materias:

1. **Alcance del equipamiento:** validar con D3/D4 la meta de cobertura sobre los 374
   camiones, interviniendo terceros solo con adhesión y autorización.
2. **Telemetría de fábrica:** comprobar rFMS/API del fabricante como vía primaria y
   mantener el lector físico CAN/FMS sujeto a autorización expresa por modelo y garantía.
3. **Costeo:** separar costeo operacional básico en Etapa 1 de analítica avanzada en
   Etapa 2, asegurando información útil antes de la renegociación de 2027.
4. **Propiedad del dispositivo:** costear y formalizar que AUDIT financia, administra,
   mantiene y retira el equipo como parte del servicio.
5. **Privacidad:** distinguir captura futura, visibilidad para clientes, conservación
   histórica y eliminación legalmente procedente.
6. **Bloqueos:** implementar y validar que jornada o evidencia insuficientes no admiten
   excepción operacional y que el viaje se reprograma o cambia de conductor.

## 3. Registro maestro

| N° | Estado | Decisión propuesta | Validación o trabajo pendiente | Coordinación |
|---:|---|---|---|---|
| 1 | Ratificada D2 | Acreditar la jornada externa con un expediente multifuente por conductor: declaración identificada, registros del transportista y tacógrafo cuando esté disponible. Ante caída de una fuente externa solo podrá usarse un expediente local vigente, suficiente y con cobertura temporal comprobada; en otro caso se bloquea. | Validar valor probatorio, identidad, correcciones, retención y acceso a jornada de otros clientes. | D1, D3 y revisión legal |
| 2 | Ratificada D2 | Ofrecer adhesión contractual como servicio integral: dispositivo, instalación, soporte, portal, evidencias y liquidación más rápida a cambio de intercambio autorizado de datos. Quien no adhiera o revoque operará en modo documental limitado, sin capacidades ni beneficios dependientes de telemetría. Meta: 70 % (104/148) al cierre E1 y 90 % (134/148) al cierre E2. | Redactar instrumento contractual, permanencia, retiro y tratamiento comercial del modo limitado; validar metas y costo. | Matías lidera; D1 y D4 |
| 3 | Ratificada D2 | Envolver el TMS 2013 con una capa de integración y sustituir gradualmente sus módulos operacionales, manteniendo continuidad y al sistema contable como emisor tributario único. | Confirmar interfaces, exportaciones, soporte y separación real entre TMS y sistema contable; preparar contingencia por archivos o base de datos. | D3 |
| 4 | Ratificada D2 | Unificar los tres proveedores GPS mediante una capa de ingestión multicanal. Homologar equipos existentes y usar aplicación móvil o dispositivo AUDIT en unidades sin GPS, sin intervenir terceros no adheridos. | Confirmar API, derechos, históricos y límites; validar cobertura 80 % E1, 95 % E2 y 100 % antes del mes 24. | D3 y D4 |
| 5 | Ratificada D2 | AUDIT financiará, conservará en inventario, configurará, administrará, mantendrá y retirará el dispositivo adicional; su costo se incorporará al servicio. En camiones de terceros se exige adhesión y autorización expresa. | Costear instalación, conectividad, suscripciones, mantención, repuestos y retiro; regular equipos preexistentes y término de la relación. | Matías lidera; D1 y D4 |
| 6 | Ratificada D2 | Jornada insuficiente o evidencia ausente, vencida o contradictoria bloquean el despacho sin excepción operacional. Se debe reprogramar el viaje o sustituir al conductor por uno habilitado. | Definir escalamiento y comunicación cuando el bloqueo afecte un viaje comprometido; validar causales legales y de seguridad. | D1, D3 y operación |
| 7 | Ratificada D2 | Calcular la alerta a bordo según jornada restante, ruta, condiciones vigentes y tiempo hasta el próximo lugar seguro, con margen configurable validado en piloto. | Levantar y aprobar el catastro de lugares seguros, márgenes por ruta y contingencia cuando no exista detención alcanzable. | D4 y conductores |
| 8 | Ratificada D2 | Registrar llegada y salida automáticamente con geocercas y sello temporal, contrastando los cruces con agenda, EDI, API u otra evidencia disponible, sin acción del conductor ni equipos en el cliente. | Validar precisión, falsos cruces, resolución de disputas y aceptación contractual de la evidencia. | D3, D4 y área comercial |
| 9 | Ratificada D2 | Usar exclusivamente el mecanismo offline autorizado por el sistema contable para emitir un documento conforme antes del movimiento, originado desde la orden, sin redigitación y con sincronización idempotente posterior. | Confirmar mecanismo, folios, firma, CAF si corresponde e interfaz tributaria; bloquear si no puede emitirse conforme. | D3 y proveedor contable |
| 10 | Ratificada D2 | Obtener la conformidad digital mediante firma y código OTP del receptor identificado, con sello temporal, ubicación y evidencia adjunta; debe operar offline y sincronizarse después. Meta: cero conformidades perdidas y al menos 99 % disponible el mismo día. | Validar facultades del receptor, rechazo o ausencia, momento que habilita facturación, controversias y valor probatorio. | Ignacio lidera; D1, D3 y revisión legal |
| 11 | Ratificada D2 | Usar muestreo adaptativo con valores iniciales de piloto: 10 s en eventos o maniobras, 30 s en ruta estable y 5 min detenido. Conservar detalle local sin cobertura y transmitirlo posteriormente. | Ajustar frecuencias con el piloto y dimensionar eventos, fotografías, datos móviles, almacenamiento y reconexión masiva. | D3 y D4 |
| 12 | Ratificada D2 | Priorizar rFMS/API remota del fabricante en modo de solo lectura. Usar CAN/FMS físico solo donde no exista acceso remoto y haya autorización expresa, sin afectar garantía ni seguridad. | Levantar marca, modelo, año, suscripción e interfaces de los 61 tractocamiones y confirmar condiciones de garantía. | D3 y D4 |
| 13 | Ratificada D2 | AUDIT ejecutará y custodiará la descarga remota del tacógrafo cuando el modelo lo permita y aplicará descarga física controlada como contingencia; Curimón controlará cumplimiento, accesos y auditoría. | Confirmar modelos, periodicidad legal, asociación conductor-vehículo, retención, integridad y responsabilidades contractuales. | D3, D4 y revisión legal |
| 14 | Ratificada D2 | Incorporar en E2 optimización de retorno que maximice el margen esperado después de cumplir jornada, habilitaciones, ubicación, plazo, compatibilidad, nivel de servicio y aceptación del transportista. Meta: kilómetros vacíos iguales o inferiores a 18 % en población comparable. | Definir fórmula y ponderaciones secundarias, población comparable y reglas de adjudicación entre flota propia y terceros. | Matías lidera; D1 y D3 |
| 15 | Ratificada D2 | Publicar dentro de 24 h una versión inicial del costo con componentes disponibles y faltantes explícitos; emitir versiones conciliadas posteriores sin sobrescribir el historial. | Validar que el versionado satisface RT-05.29; definir estimaciones, fuentes, identificadores y responsables de conciliación. | D3 y finanzas |
| 16 | Ratificada D2 | Separar el costo de Curimón por contratar a un tercero de su costo operacional interno. Usar tarifa y cargos para el primero y datos open-book solo con adhesión expresa para el segundo. Meta E1: 95 % de viajes trazables y 100 % de rutas y contratos modelados. | Acordar datos compartidos, indicadores y método de estimación; no presentar la tarifa como costo real del tercero. | Matías lidera; D1 y D3 |
| 17 | Ratificada D2 | Entregar en E1 costos trazables por viaje, ruta y contrato antes de las renegociaciones de 2027; dejar la decisión comercial en Curimón y la analítica avanzada para E2. | Confirmar contratos, fechas de corte, información mínima, escenarios y responsable comercial. | D1, D3 y finanzas |
| 18 | Ratificada D2 | Consolidar las aproximadamente 6.000 vigencias en un registro único con titular, responsable de renovación, custodio, vencimiento, alertas y bloqueo. El titular externo renueva y Curimón verifica antes de asignar. | Definir responsables, escalamiento y umbrales por tipo documental. | D1 y D3 |
| 19 | Ratificada D2 | Antes del despacho, escanear el identificador o código UN de la carga peligrosa, contrastarlo con el manifiesto y adjuntar fotografía sellada. Toda discrepancia o ausencia de evidencia bloquea la salida. | Validar identificadores disponibles, calidad de evidencia, auditoría y operación sin instalar equipos en el cliente. | Ignacio lidera; D1, D3 y operación |
| 20 | Ratificada D2 | Aplicar ante cierres fronterizos un protocolo de contingencia que mantenga evidencia offline, controle jornada y carga, permita reprogramar y comunicar estados y sincronice ordenadamente al recuperar conectividad. | Precisar relevo, custodia, trámites, sobreestadías y responsabilidades para cierres de hasta 12 días. | Matías lidera; D3 y D4 |
| 21 | Ratificada D2 | Permitir que el taller externo registre la intervención en un portal web o móvil, incluso offline, con identidad, fecha, kilometraje, trabajo, repuestos y evidencia. El responsable de flota aprobará antes de incorporarla a la hoja de vida. Meta: recibir al menos 95 % e incorporar el 100 % de las validadas. | Definir usuarios, datos mínimos, plazo, correcciones, garantías y conciliación con facturas. | Ignacio lidera; D3 y D4 |
| 22 | Ratificada D2 | Calcular CO2e por tonelada-kilómetro con ISO 14083/GLEC, consumo real cuando exista y factores documentados y versionados para terceros; preparar base y método en E1 y cálculo productivo completo con consolidación mensual en E2. | Validar estándar, factores, tratamiento de vacío, masa, cobertura, precisión y verificación independiente. | D1 y D3 |
| 23 | Ratificada D2 | Aplicar consentimiento granular y revocable por transportista, vehículo, viaje, dato, destinatario y período. Compartir posición solo durante el servicio autorizado, auditar accesos y hacer efectiva la revocación de datos futuros en hasta 5 min. | Conciliar revocación con retención legal e histórica y derechos del conductor; probar segregación y revocación. | Ignacio lidera; D3 y revisión legal |
| 24 | Ratificada D2 | Proteger la evidencia de jornada mediante identidad fuerte, sello temporal, registro append-only, hash encadenado y almacenamiento inmutable; conservar el original y el historial de correcciones sin sobrescritura. | Validar autoría, cadena de custodia, sello de tiempo, auditoría independiente y valor probatorio. | D3 y revisión legal |
| 25 | Ratificada D2 | Desplegar kits preconfigurados durante pasos normales por terminal, con piloto por familia de vehículo, verificación y actualización remota. Intervenir terceros solo con adhesión y autorización. Meta: cobertura 80 % E1, 95 % E2 y 100 % antes del mes 24. | Calcular cronograma con frecuencia real de paso, stock, capacidad de talleres, tiempos de piloto y TCO. | D4; Matías revisa adhesión |
| 26 | Ratificada D2 | Operar en modo mixto con validación telemática para equipados y validación documental reforzada para no equipados, mostrando claramente nivel de evidencia y riesgo; ambos modos deben respetar los bloqueos legales. | Validar carga operacional, criterios de avance/reversión y suficiencia jurídica del modo documental. | Matías lidera; D3 y D4 |

## 4. Acuerdos de alcance que propone D2

Estas reglas permiten que el catálogo de requisitos avance aunque existan validaciones
externas pendientes:

1. Toda dependencia no confirmada se declara como supuesto y tiene contingencia.
2. Ninguna consulta enviada se cita como respuesta del CLIENTE mientras no exista acta.
3. Ningún requisito obliga a intervenir equipos de terceros sin acuerdo expreso.
4. La operación esencial debe funcionar sin cobertura y sincronizarse después.
5. La ausencia de adhesión no puede ocultarse: reduce capacidades y debe tener un modo
   operacional explícito, medible y seguro.
6. Los incumplimientos legales o de seguridad no se transforman en excepciones por una
   autorización operacional.
7. El sistema contable se conserva como único emisor de documentos tributarios.
8. La arquitectura implementa las decisiones de alcance de D2; no debe inventarlas ni
   contradecirlas.

## 5. Validación mínima para cerrar D2-01

- [x] Las 26 propuestas fueron revisadas y acordadas por D2.
- [x] Las decisiones 1, 2, 5 y 25 quedaron ratificadas por D2 y fundamentadas.
- [x] Las decisiones abiertas 10, 14, 19 y 21 tienen solución acordada por D2.
- [x] Se resolvió el alcance propuesto de equipamiento en flota propia y de terceros.
- [x] Se acordó la estrategia primaria para telemetría de fábrica.
- [x] Se resolvió la división del costeo entre Etapa 1 y Etapa 2.
- [x] Se definió el modelo contractual y económico propuesto del dispositivo.
- [x] Se acordaron reglas de consentimiento y revocación de geolocalización.
- [ ] D3 y D4 confirmaron que pueden implementar las decisiones sin supuestos nuevos.
- [ ] Cada decisión ratificada alimenta al menos un RF, RNF, supuesto o exclusión.

## 6. Fuentes internas consultadas

- `equipo/D1/subdoc2-problema.md`
- `equipo/D1/consultas-d1.md`
- `equipo/D2/plan-trabajo-d2-v2.md`
- `equipo/D2/consultas-d2-v2.md`
- `equipo/D3/plan-de-trabajo.md`
- `equipo/D3/subdoc4.1-arquitectura-logica.md`
- `equipo/D3/subdoc5-datos.md`
- `equipo/D4/D4-MATERIAL-INFORME1.md`
- `equipo/consultas-consolidadas-audit.md`
