# Formulario T-11 · Tabla de emplazamiento de componentes

**Dupla 4 · Subdocumento 4.2 · audIT · Licitación TFEP-01/2026 · Caso 10**
**Fuente del formato:** FEP01 · Formulario T-11 · p.62
**Insumo:** inventario lógico de D3 (`subdoc4.1-arquitectura-logica.md`, Eje 5), recibido y revisado.

---

## Regla que gobierna esta tabla

**Artículo 16.2** (FEP01 p.12, verificado textualmente):

> «El PROPONENTE deberá justificar, **componente por componente**, la decisión de emplazamiento en
> función de **latencia, criticidad operacional, volumen de datos, restricciones regulatorias,
> disponibilidad de conectividad y costo total de propiedad**. Una asignación no justificada será
> evaluada como **observación grave**.»

**Artículo 16.1:** «No se admiten propuestas exclusivamente en nube ni exclusivamente on-premise.»

Y el numeral 1.5 advierte que declarar «cumple» sin individualizar el componente **equivale a no
declarar**. Por eso cada fila lleva su justificación propia y ninguna dice «según corresponda».

## Los cuatro emplazamientos de esta solución

| Código | Emplazamiento | Tipología declarada | Fundamento |
|---|---|---|---|
| **N** | Nube — Azure Chile Central, tres zonas | — | RT-03.01, RT-03.02 |
| **N2** | Nube — segunda región Azure | — | RT-07.02 · **Art. 16.3 obliga a declarar región primaria y secundaria** |
| **SB** | San Bernardo, 26 m² | Sala técnica secundaria o de sitio | Numeral 6.1 transversal |
| **GT** | Gabinete de terminal ×4 | Gabinete o borde operacional | RT-06.01 del Caso |
| **DB** | Dispositivo a bordo | On-premise distribuido ×374 | RT-06.01 del Caso, texto expreso |
| **BM** | Borde móvil | — | RT-17.01 |

---

## Tabla A · Decisión de emplazamiento

| # | Componente lógico | Capa | Empl. | Justificación de la decisión |
|---:|---|---|:---:|---|
| 1 | CDN y protección perimetral | Borde | **N** | Punto de presencia distribuido; no tiene sentido físico fuera de la nube |
| 2 | Puerta de enlace de servicios | Borde | **N** | Autenticación y enrutamiento centralizados; escala con el peak de reconexión |
| 3 | Servicio de despacho y asignación | Negocio | **N** | Orquesta recursos de toda la red; requiere la vista completa de flota y jornada |
| 4 | **Nodo de continuidad operacional** | Negocio | **SB** | **RT-21.06: asignar viaje, emitir DET y recibir pánico son severidad máxima. No pueden depender del enlace a la nube** |
| 5 | Servicio de flota y mantenimiento | Negocio | **N** | Administración centralizada de activos; tolera latencia de segundos |
| 6 | Servicio de jornada | Negocio | **N** | Validación bloqueante ≤30 s (RT-09.01) contra el dato consolidado |
| 7 | Servicio de gestión documental | Negocio | **N** | Sellado y control de retención centralizados |
| 8 | Servicio de tarifas y liquidación | Negocio | **N** | Proceso por lotes mensual; sin exigencia de latencia operacional |
| 9 | Bus de eventos de telemetría | Eventos | **N** | Absorbe la ráfaga de cientos de unidades saliendo de la misma sombra |
| 10 | Bus transaccional | Eventos | **N** | Entrega garantizada con cola de mensajes fallidos |
| 11 | Pasarela de la capa anticorrupción | Integración | **SB** | Debe alcanzar el ERP heredado, que está físicamente en San Bernardo |
| 12 | Integración telemática de terceros | Integración | **N** | Consume APIs de los dos proveedores externos; **cero intervención física** (restricción 3) |
| 13 | Integración rFMS de fábrica | Integración | **N** | API del fabricante, solo lectura, autorización por OEM (RT-17.06) |
| 14 | Base transaccional | Datos | **N** | Consistencia estricta con alta disponibilidad multizona |
| 15 | Base de series de tiempo | Datos | **N** | Volumen y patrón de escritura masiva; 2 años en línea (RT-05.10 del Caso) |
| 16 | Caché distribuida | Datos | **N** | Sesiones, vigencias y geocercas de consulta; **no sustituye la evaluación a bordo** |
| 17 | Repositorio documental inmutable | Datos | **N** | Evidencia probatoria con retención de 5 a 10 años (RT-07.11, RT-05.10) |
| 18 | Lakehouse analítico | Analítica | **N** | Aislamiento OLTP/OLAP; costo por km en ≤24 h (RT-05.29) |
| 19 | Capa semántica de autoservicio | Analítica | **N** | Explotación por Finanzas sin intervención de TI (RT-05.27) |
| 20 | Gestión del parque de dispositivos | Terreno | **N** | Inventario, configuración, **firmware**, bloqueo y borrado remotos (RT-03.18) |
| 21 | Identidad, secretos y cifrado de campo | Seguridad | **N** | Clave gestionada **independiente de la infraestructura respaldada** (RT-07.10, RT-11.10) |
| 22 | Observabilidad | Observab. | **N** | Cobertura unificada de nube y on-premise, sin puntos ciegos (RT-03.16) |
| 23 | Réplica de recuperación ante desastres | Todas | **N2** | RT-07.02: distancia suficiente para no compartir el evento de fuerza mayor |
| 24 | **ERP contable heredado 2013** | Legado | **SB** | Sistema existente no reemplazable y **único emisor de documentos tributarios** (Cap. 11) |
| 25 | Terminación de enlaces y borde de red | Red | **SB** | Punto de entrada de ExpressRoute y VPN por rutas físicas distintas (RT-03.17, RT-06.32) |
| 26 | Custodia de medios de respaldo | Datos | **SB** | Medio físico transportable fuera de sitio (RT-06.26, esquema 3-2-1-1-0 de RT-07.09) |
| 27 | Nodo de terminal | Negocio | **GT** | **RT-03.10 del Caso: «Los terminales deben operar 12 horas sin enlace hacia el exterior»** |
| 28 | Lector de portería y enrolamiento | Terreno | **GT** + **SB** | Verificación local de vigencias en los 5 terminales; el enrolamiento biométrico se centraliza (RT-06.22) |
| 29 | **Buffer no volátil ≥ 8 GB** | Terreno | **DB** | **RT-03.10: 72 h sin cobertura sin pérdida de registro; RT-10.05: hasta 12 días (288 h) de cierre fronterizo** |
| 30 | Motor de geocercas a bordo | Terreno | **DB** | **RT-09.01: registro de llegada y salida automático, sin intervención del conductor y sin equipamiento en instalaciones del cliente** |
| 31 | Cálculo de alerta de jornada a bordo | Terreno | **DB** | Criterio 28: la alerta debe llegar aunque no haya enlace, con anticipación al lugar seguro |
| 32 | Identificación del conductor | Terreno | **DB** | RT-12.11: sin manipular un dispositivo y sin recordar una credencial |
| 33 | Módulo satelital de ráfaga corta | Terreno | **DB** | Subconjunto por riesgo. **Población no estimable hasta la medición de RT-03.24** |
| 34 | App móvil del conductor | Borde | **BM** | RT-17.01. **Canal voluntario e incentivado; la trazabilidad obligatoria no depende de él** (restricciones 1 y 2) |

**Reparto resultante:** 18 en nube · 1 en segunda región · 5 en San Bernardo · 2 en gabinete de
terminal · 5 en el dispositivo a bordo · 1 en borde móvil. **Cumple el Art. 16.1**: ni
exclusivamente nube ni exclusivamente on-premise, y la parte on-premise no es decorativa —
sostiene las tres funciones de severidad máxima cuando cae el enlace.

---

## Tabla B · Matriz de los seis criterios del Artículo 16.2

| # | Componente | Latencia | Criticidad | Volumen | Regulación | Conectividad | TCO |
|---:|---|---|---|---|---|---|---|
| 3 | Despacho y asignación | ≤30 s extremo a extremo | Máxima | 96.000 viajes/año | — | Requiere enlace | Elástico |
| 4 | Nodo de continuidad | ≤30 s local | **Máxima** | Ventana de 12 h | — | **Opera sin enlace** | Fijo, dos nodos |
| 6 | Servicio de jornada | ≤30 s | **Máxima** | 454 conductores | **Datos personales de 258 externos** | Requiere enlace | Elástico |
| 9 | Bus de telemetría | ≤100 ms | Crítica | Peak de reconexión masiva | — | Requiere enlace | Elástico por partición |
| 14 | Base transaccional | ≤15 ms | Máxima | Particionado mensual | Retención 5–10 años | Requiere enlace | Reservado |
| 15 | Series de tiempo | ≤20 ms | Alta | 2 años en línea + agregación | — | Requiere enlace | Por capa hot/cold |
| 17 | Repositorio inmutable | ≤1 s | Alta | Evidencia probatoria | **WORM, 10 años siniestros** | Requiere enlace | Por capa de acceso |
| 21 | Identidad y cifrado | ≤50 ms | Crítica | — | **RT-11.10 cifrado a nivel de campo · Ley 21.719** | Requiere enlace | Fijo por HSM |
| 23 | Réplica de DR | RPO ≤15 min | Crítica | Espejo de producción | — | Enlace entre regiones | Activo-pasivo |
| 24 | ERP heredado | N/A | Externa | Contabilidad y DTE | **Único emisor tributario** | Local | Existente |
| 27 | Nodo de terminal | Local | Alta | 12 h de operación autónoma | — | **Opera sin enlace 12 h** | 4 gabinetes |
| 29 | Buffer a bordo | Inmediata | **Máxima** | ≈0,8 MB en 72 h · ≥8 GB de capacidad | Evidencia de jornada | **Opera sin cobertura** | Por unidad |
| 30 | Geocercas a bordo | Inmediata | Alta | Eventos discretos | — | **Opera sin cobertura** | Sin costo marginal |
| 33 | Módulo satelital | ≤ decenas de s | Alta | Ráfagas cortas | — | Sin cobertura celular | **Por mensaje** |
| 34 | App móvil | ≤1 s | Media, **no bloqueante** | 454 potenciales | Consentimiento revocable | Requiere enlace | Por desarrollo |

*Las filas no listadas comparten el perfil de su capa; el detalle completo por componente está en el
Subdocumento 4.2.*

---

## Cuatro cambios respecto de la recomendación de D3, con su motivo

**1 · Se agrega el nodo de continuidad operacional en San Bernardo (fila 4).**
La recomendación de D3 sitúa el servicio de despacho **íntegramente en la nube** y no contempla
ningún componente de continuidad on-premise. Pero **RT-03.10 del Caso** (FEP03 p.31) exige que
«los terminales deben operar **12 horas sin enlace** hacia el exterior», y **RT-21.06** clasifica en
severidad máxima todo incidente que impida asignar un viaje, emitir un documento de transporte o
recibir un evento de emergencia. Sin este nodo, un corte de enlace detiene el despacho.

**2 · Se separa la evaluación de geocercas a bordo de la caché en nube (filas 16 y 30).**
D3 asigna la evaluación de geocercas a la caché distribuida en nube. **RT-09.01 exige que el
registro de llegada y salida sea automático, sin intervención del conductor y sin equipamiento en
las instalaciones del cliente** — y varios puntos de carga no tienen cobertura. La evaluación debe
ocurrir **a bordo**; la caché en nube sirve para consulta y reporte, no para producir el evento.

**3 · Se corrigen dos errores de código y de conteo heredados.**
- Las 72 h son **RT-03.10**, no RT-03.13. RT-03.13 es la declaración de funciones no disponibles
  sin conexión.
- Son **cuatro terminales regionales más San Bernardo**, cinco en total. La descarga por Wi-Fi
  ocurre en los cinco, no en «los 5 terminales regionales».

**4 · El buffer cubre más unidades que las 182 declaradas.**
D3 lo dimensiona para «148 propias y 34 adheridas». Se mantiene esa base, pero el plan de
reposición y el stock del 10 % (numeral 8.4) deben cubrir además **los terceros con dispositivo que
adhieran y acepten kit**, cuyo número depende del plan de adhesión de D2 y hoy no está cerrado.

---

## Consecuencia que reabre la consulta C-03

D3 sitúa el **ERP contable heredado en la sala de San Bernardo**, y ese sistema es el **único emisor
de documentos tributarios** de la compañía. Sumado al nodo de continuidad de la fila 4, San Bernardo
deja de alojar solo terminación de enlaces y custodia.

El numeral 6.1 transversal aplica **íntegramente RT-06.01 a RT-06.24** cuando «el caso requiere
cómputo, almacenamiento y procesamiento **sustantivos** en las instalaciones del CLIENTE». Un ERP
que emite todos los documentos tributarios, más el nodo que sostiene tres funciones de severidad
máxima, es discutible que sea «no sustantivo».

→ **Refuerza la consulta C-03**: hay que preguntar al CLIENTE a qué tipología debe llevarse la sala,
porque la diferencia de alcance —esclusa, blindaje perimetral, espacio de enrolamiento— es grande en
ambas direcciones y el numeral 6.1 penaliza igual sobredimensionar que subdimensionar.

Mientras no haya respuesta, esta tabla declara **sala técnica secundaria o de sitio** y deja el
alcance íntegro costeado como alternativa.

---

## Lo que esta tabla todavía no puede cerrar

| Ítem | Por qué | Cómo se cierra |
|---|---|---|
| Población del módulo satelital (fila 33) | **RT-03.24 del Caso prohíbe suponer la cobertura**: exige medirla en terreno | Campaña de medición, Etapa 1 |
| Unidades totales con buffer (fila 29) | Depende de cuántos terceros adhieran | Plan de adhesión de D2 (criterio 27) |
| Dimensionamiento del nodo de continuidad (fila 4) | Requiere el peak de asignación de la torre | RT-09.02 + volumetría del Cap. 14.2 |
