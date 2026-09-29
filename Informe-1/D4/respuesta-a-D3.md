# D4 → D3 · Respuesta al plan de trabajo v2.0

**De:** Ignacio V y Alonso (Dupla 4 · Subdoc. 4.2) · **Para:** Marcel y Martín (Dupla 3)
**Fecha:** 03-09-2026 · **Cierre de la sincronización S4:** viernes 04-09

Respuesta a los seis puntos donde su plan pide coordinación con D4, más tres choques que
conviene resolver antes de la S4 y cinco correcciones menores. Todo lo que se afirma sobre las
bases está verificado con `tools/buscar.py` y lleva su cita.

---

## 1 · Buffer a bordo — coordinado, pero 120 h no alcanzan

Su objetivo 7 pide «coordinar con D4 el buffer de almacenamiento». Su Innovación Tipo 3 propone
**«retención de hasta 120 horas»**.

Nuestro cálculo del volumen en 72 h, con todos los supuestos derivados:

| Concepto | Sin imágenes | Con evidencia fotográfica |
|---|---|---|
| Posición (30 s marcha / 5 min detenido) | 263 KB | 263 KB |
| Telemetría FMS 1/min | 288 KB | 288 KB |
| Eventos discretos | 32 KB | 32 KB |
| Documentos del viaje (≈3 viajes) | 195 KB | 2,6 MB |
| **Subtotal** | **≈ 0,8 MB** | **≈ 3,2 MB** |
| Con factor ×3 (formato, índices, journaling, cola de reintento) | ≈ 2,5 MB | ≈ 10 MB |

**El problema no es el tamaño, es la duración.** RT-10.05 del Caso (FEP03 p.32) y el numeral 13.2
(FEP03 p.27) declaran cierres del paso Los Libertadores de **hasta 12 días continuos = 288 horas**.
Verificado en dos secciones distintas. Un camión detenido allí sigue obligado por RT-03.10 a no
perder ningún registro.

**120 h < 288 h.**

→ **Propuesta de D4: especificar la capacidad, no la duración. Almacenamiento no volátil ≥ 8 GB.**
Una duración obliga a rehacer el cálculo cada vez que cambia la frecuencia de muestreo o se agrega
un tipo de evidencia; una capacidad no. El sobrecosto frente al mínimo es marginal y elimina toda
una clase de riesgo.

> Las **120 horas no aparecen en ninguno de los tres documentos** (verificado). Es un supuesto de
> D3 y, si se mantiene, debe declararse como tal con su derivación.

---

## 2 · Frecuencia de muestreo — coincidimos exactamente

Su decisión 11 propone «30 s en movimiento con cobertura, 5 min en ralentí/detención». Es
**idéntico** al escenario B de nuestro §5.5. **Confirmado, sin cambios.**

Aportamos lo que faltaba: el consumo que se deriva de esa elección, que es el otro ítem del
Cap. 14.2 y la respuesta a la decisión 11.

| Concepto | Por camión/mes |
|---|---|
| Carga útil | 5,3 MB |
| Con overhead de protocolo (×2,5–3) | **13–16 MB** |
| Flota completa (374 unidades) | **≈ 5,6 GB/mes** |

**Y el hallazgo que conviene que sepan:** el costo de datos móviles de esta flota es marginal. Lo
que pesa son los **cargos fijos por unidad** —SIM, suscripción de plataforma, suscripción
satelital, suscripción por OEM—, que escalan con las 374 y luego con las 430. La palanca económica
de la decisión 11 no está en la frecuencia.

**Decisión conjunta pendiente:** si el DET, la conformidad de entrega o la lista de carga peligrosa
llevan **fotografías**, el consumo sube a ≈40 MB por camión y el buffer se triplica. **D3 define
qué cuenta como «documento asociado al viaje»; D4 dimensiona a partir de eso.** Es la pregunta 2
de nuestra lista final.

Supuestos declarados: 55 km/h de velocidad comercial, 64 B por registro de posición, 160 B por
muestra FMS, 40 KB por DET, 300 KB por fotografía.

---

## 3 · RAID (RT-03.14) — lo redacta D4, y no basta con declararlo

Su plan declara «**RAID-1** en nodos de borde de terminales y flash industrial con wear-leveling
en cabina».

RT-03.14 (FEP02 p.9) exige: «Los equipos on-premise críticos serán redundantes. El almacenamiento
local tolerará la falla de al menos un disco; el PROPONENTE declarará el nivel RAID escogido **y lo
justificará frente a las alternativas**».

Dos observaciones:

- **La justificación es obligatoria, no solo la declaración.** RAID-1 sobre dos discos es defendible
  en un gabinete de terminal; en San Bernardo, con el clúster de dos nodos, hay que compararlo con
  RAID-10 y RAID-6 y decir por qué.
- Es especificación de hardware, o sea Formulario T-11, o sea **entregable de D4**. Cítenlo, pero
  déjennos fijarlo.

**El «flash industrial con wear-leveling» sí es correcto y conviene mantenerlo**: es exactamente lo
que exige RT-08.11 sobre condiciones reales de uso —vibración, temperatura, polvo—.

---

## 4 · Tabla RT-03.13 · funciones no disponibles sin conexión

Entregable D3-15, revisor Ignacio V, en curso. Ustedes listaron tres funciones. RT-03.13 advierte
que **la ausencia de esta declaración se evalúa como observación grave**, así que conviene que esté
completa. Propuesta de tabla conjunta:

| Función | ¿Disponible sin enlace? | Procedimiento manual supletorio | Dueño |
|---|---|---|---|
| Registro de posición, jornada y eventos | **Sí** — se escribe en buffer local | — | D4 |
| Evaluación de geocerca de llegada y salida | **Sí** — se evalúa a bordo | — | D4 |
| Alerta de jornada próxima a agotarse | **Sí** — se calcula a bordo | — | D4 |
| Botón de emergencia | **Sí** por satélite, en la población de capa 2 | Protocolo telefónico con la torre donde no hay SBD | D4 |
| Emisión del DET | **Sí**, con folio CAF pre-asignado | — | D3 |
| Asignación de un viaje nuevo no pre-cargado | **No** | Autorización de la torre, registrada y reconciliada al reconectar | D3 |
| Verificación bloqueante de jornada y habilitaciones | **Parcial**: contra copia local, no contra dato fresco | Regla de excepción de la decisión 6, con rol nominado y registro | D3 + D4 |
| Consulta de liquidación por el transportista | **No** | Portal, al reconectar | D3 |
| Notificación en tiempo real al cliente | **No** | Aviso diferido | D3 |
| Actualización de firmware del dispositivo | **No** | Sólo en terminal (restricción 5) | D4 |

**La fila delicada es la de verificación bloqueante.** Si el camión sale desde una zona sin
cobertura, ¿se valida contra la copia local o se bloquea el despacho? Enlaza con la decisión 6 del
numeral 16.1 y hoy no está resuelto por ninguna de las dos duplas.

---

## 5 · Tabla RT-07.13 · respaldo por dominio de datos

RT-07.13 pide, **por cada dominio**: frecuencia de respaldo, período de retención y tiempo estimado
de restauración completa. Los plazos de retención de su §6 están correctos y coinciden con RT-05.10
(FEP03 p.31). Faltan las otras dos columnas.

| Dominio | Retención (RT-05.10) | Frecuencia de respaldo | Restauración completa |
|---|---|---|---|
| Jornada de conducción y su evidencia | mínimo 5 años | Continua + diaria | D3 + D4 |
| DET y antecedentes del viaje | 6 años | Continua + diaria | D3 + D4 |
| Antecedentes de siniestros | 10 años | Diaria | D3 + D4 |
| Habilitaciones de conductores y equipos | vigencia + 5 años | Diaria | D3 + D4 |
| Registros de carga peligrosa | 5 años | Diaria | D3 + D4 |
| Tiempos en instalaciones de cliente | 3 años | Diaria | D3 + D4 |
| Liquidaciones a transportistas | 6 años | Diaria + antes y después del cierre mensual | D3 + D4 |
| Series de posición y telemetría | 2 años en línea + agregación declarada | Continua | D3 + D4 |

**Y el esquema que falta:** RT-07.09 (FEP02 p.18) exige la política **3-2-1-1-0** — tres copias, dos
medios distintos, una fuera de sitio, una inmutable o fuera de línea, cero errores de verificación
de restauración. Está desarrollada en nuestro §5.11.

> **Un matiz que conviene escribir en la propuesta:** existe una cuarta copia que nadie planificó y
> que está ahí igual — los 374 dispositivos conservan 72 h del registro operacional. No sustituye al
> respaldo, pero es una fuente real de reconciliación ante una pérdida de datos reciente, y refuerza
> el argumento del borde como parte del esquema de continuidad.

---

## 6 · Inventario de componentes lógicos (D3-06) — no nos ha llegado

Su matriz lo marca **Completado**, con Alonso (D4) como revisor y cierre 04-09. **No lo hemos
recibido.** Es el bloqueo declarado de nuestra sección: sin él, la tabla de emplazamiento del
Formulario T-11 no se puede llenar.

Lo que necesitamos **por cada componente**, que son las columnas que el Artículo 16.2 obliga a
justificar —verificado textualmente en FEP01 p.12—:

> «El PROPONENTE deberá justificar, componente por componente, la decisión de emplazamiento en
> función de latencia, criticidad operacional, volumen de datos, restricciones regulatorias,
> disponibilidad de conectividad y costo total de propiedad. **Una asignación no justificada será
> evaluada como observación grave.**»

Mientras llega, dejamos hechas las reglas de decisión y una matriz capa → emplazamiento (lámina
«4.1 → 4.2» del canvas de diagramas). Es una **propuesta a confirmar**, no un reemplazo.

---

# Tres choques que conviene resolver antes de la S4

## A · La App Móvil en el teléfono del conductor

Aparece tres veces en su plan: como persistencia para «las 226 restantes», como geolocalización
autónoma para los 34 sin GPS, y como mitigación ante la negativa de un proveedor GPS.

**Choca de frente con cuatro cosas:**

- **Restricción 2** (FEP03 p.23): a los 258 conductores de terceros no se les puede imponer nada por
  la vía laboral. Instalar una app en su teléfono personal y depender de que la lleve encendida es
  pedirle algo a quien no se le puede pedir nada.
- **Restricción 1**: ninguna interacción con el vehículo en movimiento.
- **RT-12.11** (FEP03 p.32): la identificación del conductor debe resolverse «sin exigir
  manipulación de un dispositivo con el vehículo en movimiento y sin depender de que el conductor
  recuerde una credencial».
- **Capítulo 19**: castiga explícitamente proponer algo que dependa de los 148 dueños sin explicar
  quién se lo pide, y advierte que una propuesta más modesta con esa conversación resuelta gana.

Esta idea ya se descartó una vez: es la «libreta portable del conductor» de `CONTEXTO-CASO10.md`
§6.1, descartada por el mismo motivo.

→ **Propuesta:** la app del conductor **puede existir** —RT-17.01 (FEP03 p.33) de hecho exige una
app en cuatro perfiles, uno de ellos el conductor—, pero como **canal voluntario e incentivado**,
nunca como el mecanismo del que dependa la trazabilidad. Su tasa de adopción es exactamente lo que
mide el **criterio 27**, y nadie puede garantizarla en el Informe 1.

## B · La partición de la flota está mal

Su matriz de persistencia dice «148 kits físicos + App Móvil en 226 restantes».

El Capítulo 5 (FEP03 p.12) dice otra cosa: de los 374, **340 tienen dispositivo** repartido en tres
plataformas y **34 no tienen ninguno**. De los 226 de terceros, **~192 sí tienen equipo**, de dos
proveedores contratados por los propios dueños.

| Población | Unidades | Tratamiento |
|---|---|---|
| Flota propia | 148 | Kit completo, despliegue directo |
| Terceros **con** dispositivo | ~192 | **No se reemplaza** (restricción 3). Estándar de homologación + unificación de la vista (Cap. 11, p.24) |
| Terceros **sin** dispositivo | 34 | Únicos candidatos a equipo nuevo, y sólo por adhesión |

Los «148 kits» también quedan cortos: hay que sumar los 34 sin dispositivo y los terceros que
adhieran.

## C · «Homologado con D4» — todavía no

Su Definition of Done marca «Coherencia cruzada absoluta con la infraestructura física de D4
(Completado y homologado)».

**No lo está.** D4 no ha revisado ningún entregable de D3 y este documento es el primer
intercambio. Conviene bajarlo a «pendiente» hasta la S4: si el evaluador pregunta por la
homologación en la presentación y las dos duplas responden distinto, se nota.

---

# Correcciones menores

1. **RT-02.14 es Deseable, no Obligatorio.** Texto verificado (FEP02 p.6): «Se valorará la
   aplicación documentada de patrones de arquitectura evolutiva… capa anticorrupción frente a
   sistemas heredados… | **Deseable**». La capa anticorrupción **obligatoria** es **RT-05.20**
   (FEP02 p.12): «Las integraciones con sistemas heredados o de terceros **se aislarán** mediante
   una capa anticorrupción». Anclar el ACL a un requisito deseable lo debilita sin necesidad: citen
   RT-05.20 como fundamento y RT-02.14 como el punto extra.
2. **La precisión de geocerca de ±15 m no está en las bases.** Búsqueda sin resultados. Es supuesto
   de D3 y hay que declararlo, o preguntarán de dónde salió.
3. **Las 120 h del buffer tampoco aparecen** en ninguno de los tres documentos.
4. **La latencia de sincronización «< 15 min»** es más estricta que el ≤20 min del Capítulo 15
   (FEP03 p.31). Comprometerse a menos está bien; conviene decir «se supera el umbral exigido»
   en vez de presentar otro número sin origen.
5. **Res. Ex. N.º 107/2014 del SII** (folios CAF de contingencia): no la verificamos. Queda en el
   mismo nivel «sin verificar» que nuestras referencias laborales pendientes; conviene abrir la
   norma antes de citarla.

---

# Lo que D4 necesita de D3, en orden de urgencia

1. **El inventario de componentes lógicos (D3-06).** Es el bloqueo. Sin él no hay tabla T-11.
2. **¿Qué cuenta como «documento asociado al viaje»? ¿Lleva fotografías?** Define el buffer a bordo
   y el costo recurrente de datos móviles de toda la flota.
3. **Volumen anual de series de posición y de evidencia de jornada**, con su política de agregación,
   para dimensionar el almacenamiento en nube (Cap. 14.2).
4. **Confirmación de que aceptan la especificación de ≥8 GB** en lugar de las 120 h.
5. **Personas usuarias concurrentes**, internas y externas, para RT-09.01. Lo pide el Cap. 14.2 y
   hoy no lo tiene nadie.
