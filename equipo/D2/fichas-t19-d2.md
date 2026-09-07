# Formulario T-19. Fichas de innovación de la dupla D2

**Licitación TFEP-01/2026 · Caso 10 · Transportes Curimón S.A.**\
**Empresa proponente:** AUDIT\
**Dupla responsable:** Ignacio C. y Matías V.\
**Formato:** FEP01 · Formulario T-19 · p.64

D2 desarrolla dos de las cinco innovaciones obligatorias del Artículo 28°, el **tipo 1,
producto o servicio**, y el **tipo 4, modelo de negocio o contratación**. El reparto de
la cartera completa quedó confirmado por el equipo el 6 de septiembre de 2026 y consta
en `equipo/asignacion-duplas.md`.

| Tipo | Dupla |
|---|---|
| 1 · Producto o servicio | **D2** |
| 2 · Proceso | D4 |
| 3 · Tecnológica o de arquitectura | D3 |
| 4 · Modelo de negocio o contratación | **D2** |
| 5 · Experiencia de usuario, sostenibilidad o impacto social | D1 |

Los cinco tipos quedan cubiertos sin repetición, conforme al Artículo 28.1.

Cada ficha desarrolla los **siete elementos del Artículo 29°** (FEP01 · p.19), cuya
omisión reduce la innovación a un enunciado, y cierra con la verificación contra los
requisitos **RT-26.01 a RT-26.08** (FEP02 · Capítulo 26 · p.44).

> **Trazabilidad de las fuentes.** Las referencias de los elementos 3 de ambas fichas
> fueron verificadas en su fuente oficial el 6 de septiembre de 2026 y se consolidan al
> final de este documento. Las cifras económicas unitarias no se citan porque no han
> sido cotizadas, y así se declara en cada elemento 5. Una cifra sin fecha y sin fuente
> no se considera válida.

---

# Ficha 1. Innovación tipo 1, producto o servicio

## Hoja de servicio del transportista

### Elemento 1. Problema u oportunidad concreta, con el dato que la dimensiona

El 60,4 % de la capacidad gestionada pertenece a 148 transportistas subcontratados
(FEP03 · Sección 2.2 · p.6). El proyecto necesita de ellos jornada, posición y
consentimiento, y no puede obtenerlos por instrucción porque sus 258 conductores no son
trabajadores de la compañía (FEP03 · Capítulo 10, restricción 2 · p.23).

El dato que dimensiona la oportunidad no es un indicador de eficiencia sino una
condición declarada en la entrevista de levantamiento. El transportista subcontratado
formuló el criterio con el que va a aceptar o rechazar el equipamiento.

> «Si el aparato registra mis horas y eso me sirve a mí para demostrar que estoy en
> regla, lo acepto. Si el aparato es para que ellos me vigilen, no.»
> (FEP03 · Capítulo 8 · p.17)

Hoy ese transportista no tiene ningún registro propio verificable de su propia
operación. Ve su liquidación 9 días después del cierre, el 11 % de las liquidaciones se
corrige después de emitida, y su visibilidad sobre viajes y liquidación en curso es
inexistente (FEP03 · Sección 7.3 · p.15).

**La oportunidad.** Toda la evidencia que el proyecto va a producir para proteger al
CLIENTE sirve también para acreditar al transportista ante sus otros clientes, ante la
autoridad y ante su aseguradora. Hoy esa evidencia se produce, se guarda y no se le
devuelve.

### Elemento 2. Tecnología, práctica o modelo que la sustenta

La innovación es un **expediente exportable y verificable por un tercero sin acceso al
portal**, emitido por el CLIENTE y de titularidad del transportista. Contiene, por el
período que el transportista escoja, la jornada acreditada de sus conductores, la
vigencia de sus habilitaciones y las de sus equipos, la hoja de vida de mantenimiento
de sus camiones y el registro de viajes ejecutados con sus tiempos y evidencias.

Se descarta la vía genérica de «exportar un PDF», porque un PDF no es verificable por
quien lo recibe. Se especifican dos alternativas técnicas y el criterio para elegir
entre ellas en el mes 4 del cronograma.

| Alternativa | Mecanismo | Ventaja | Limitación |
|---|---|---|---|
| **A. Documento firmado con verificación en línea** | Documento con firma electrónica avanzada conforme a la Ley N.º 19.799, con resumen criptográfico y código de verificación en un servicio público del CLIENTE | Marco legal chileno consolidado y receptor sin requisitos técnicos | Requiere que el verificador consulte un servicio del CLIENTE, lo que crea dependencia |
| **B. Credencial verificable** | Credencial conforme al modelo de datos de credenciales verificables del W3C, firmada por el CLIENTE como emisor y presentada por el transportista como tenedor | Verificación sin consultar al emisor y control real del titular sobre qué revela | Madurez de adopción menor en el ecosistema local de destinatarios |

**Criterio de elección.** Se adopta la alternativa A como línea base comprometida,
porque su marco legal y su curva de adopción son las que el caso puede sostener, y se
diseña el modelo de datos de modo que la alternativa B pueda incorporarse sin rehacer
la emisión. La decisión se documenta en el mes 4 con el resultado del levantamiento de
destinatarios reales.

### Elemento 3. Nivel de madurez, con la escala utilizada y las fuentes

**Escala utilizada.** Niveles de madurez tecnológica, TRL, de 1 a 9.

| Componente | TRL | Fundamento |
|---|---:|---|
| Firma electrónica avanzada y verificación en línea, alternativa A | 9 | Tecnología en operación productiva y regulada en Chile desde 2002 |
| Credencial verificable, alternativa B | 7 a 8 | Especificación estable y recomendada, con despliegues productivos aún acotados en el sector logístico local |
| Composición del expediente sobre datos de jornada y mantenimiento | 6 | El componente es convencional; lo nuevo es la composición y su uso probatorio por el titular |

**Referencias, en norma APA 7.ª edición.** Verificadas en su fuente oficial el 6 de
septiembre de 2026. La cita completa está en la bibliografía al final del documento.

- International Organization for Standardization. (2013). *Space systems. Definition of
  the Technology Readiness Levels (TRLs) and their criteria of assessment*
  (ISO 16290:2013).
- Ley N.º 19.799 de 2002. Sobre documentos electrónicos, firma electrónica y servicios
  de certificación de dicha firma. 12 de abril de 2002. Diario Oficial de la República
  de Chile.
- World Wide Web Consortium. (2025, 15 de mayo). *Verifiable credentials data model
  v2.0* (Recomendación del W3C).

### Elemento 4. Diseño de la incorporación

**Dónde se inserta en la arquitectura, RT-26.01.**

| Capa | Componente | Interfaz |
|---|---|---|
| Presentación | Portal Unificado, sección del transportista | Expone la solicitud y la descarga del expediente |
| Servicios de negocio | Servicio de Emisión de Expediente, componente nuevo | Consume Control de Jornada, Gestión Documental y Gestión de Flota |
| Datos | Repositorio WORM y Auditoría Append Only | Provee la evidencia sellada y su cadena de custodia |
| Seguridad | Gestión de identidad y bóveda de claves | Provee la firma del emisor y el registro del acceso |
| Público | Servicio de Verificación, sin autenticación | Recibe un código y responde válido o inválido, sin revelar contenido |

El componente que hoy no existe en la arquitectura de D3 es el **Servicio de Emisión de
Expediente** y su **Servicio de Verificación** público. Ambos están declarados como
brecha en `matriz-trazabilidad-d2.md` y deben incorporarse en la revisión con D3.

**Paquetes de la estructura de descomposición del trabajo, RT-26.02.** La EDT
definitiva se entrega en el Informe 2 (FEP01 · Formulario T-22 · p.68). Los paquetes se
identifican aquí de manera provisional y sus códigos se ajustarán entonces.

| Paquete provisional | Contenido | Mes |
|---|---|---:|
| P-PORT-01 | Portal del transportista, alcance obligatorio de CA-21 y CA-29 | 7 a 10 |
| P-EXPE-01 | Modelo del expediente y decisión entre alternativas A y B | 4 |
| P-EXPE-02 | Servicio de emisión, firma y sellado | 10 a 12 |
| P-EXPE-03 | Servicio público de verificación | 12 |
| P-EXPE-04 | Medición en marcha blanca con cohorte de transportistas | 13 a 15 |

**Cuándo se materializa.** El expediente queda disponible en la marcha blanca de la
Etapa 1, meses 13 a 15, y entra en producción con la Etapa 1 en el mes 16 (FEP01 ·
Artículo 17° · p.12).

### Elemento 5. Impacto económico estimado

**Inversión requerida.** Es incremental sobre el portal, que ya es obligatorio por
CA-21 y CA-29 y está presupuestado con independencia de esta innovación. Lo que la
innovación agrega son tres partidas.

| Partida | Naturaleza | Estado |
|---|---|---|
| Servicio de emisión, firma y sellado del expediente | Desarrollo | Por cotizar |
| Servicio público de verificación | Desarrollo e infraestructura | Por cotizar |
| Certificados de firma electrónica avanzada del emisor | Suscripción anual | Por cotizar |

**Efecto en el costo operacional.** Marginal y positivo. El expediente se compone de
evidencia que el sistema ya produce y almacena por obligación de CA-04 y RT-05.10, de
modo que no agrega captura ni retención. Agrega almacenamiento de documentos emitidos y
la operación del servicio de verificación.

**Beneficio esperado.** El beneficio principal de esta innovación **no se realiza en su
propia línea sino en la adhesión**, que es la variable de la que depende el 60,4 % de la
capacidad. Se declara así de manera explícita en vez de atribuirle un ahorro directo que
no tiene. El beneficio directo verificable es la reducción de las consultas y
reclamaciones de transportistas sobre su liquidación, hoy asociadas a un 11 % de
liquidaciones corregidas después de emitidas.

**Valorización en el flujo de caja.** Se incorpora en el Informe 3 conforme al
Formulario T-22 (FEP01 · p.68). El PROPONENTE consultó formalmente el nivel de
cuantificación exigido en el Informe 1 dentro del período del Artículo 43°.

### Elemento 6. Indicador de verificación del beneficio

| Indicador | Línea base | Meta propuesta | Momento de medición |
|---|---|---|---|
| Transportistas que emiten al menos un expediente | 0, la capacidad no existe | 40 % de los adheridos | Cierre de la marcha blanca, mes 15 |
| Adhesión firmada de transportistas | 0 de 148 | 70 %, es decir 104 de 148 | Cierre de la Etapa 1, mes 16 |
| Liquidaciones corregidas tras emitirse | 11 % | Bajo 2 % | Tercer cierre mensual posterior al mes 16 |
| Consultas de transportistas sobre su liquidación | Sin registro, canal telefónico | Reducción del 50 % respecto del primer mes medido | Mes 18 |

La primera medición ocurre en el mes 15, antes del paso a producción de la Etapa 1, lo
que satisface el requisito deseable RT-26.08.

### Elemento 7. Riesgo de adopción

| Riesgo | Probabilidad | Impacto | Mitigación | Contingencia |
|---|---|---|---|---|
| El transportista no percibe utilidad y no emite el expediente | Media | Alto, porque desaparece el argumento central de la adhesión | Diseñar la primera emisión asistida en el terminal durante el enrolamiento | Reforzar los incentivos económicos de la ficha tipo 4, que no dependen de este mecanismo |
| Los destinatarios no aceptan el expediente como prueba | Media | Medio, reduce el valor externo pero no el interno | Levantar destinatarios reales en el mes 4 y ajustar formato antes de construir | Mantener el valor de uso interno, que es visibilidad de viajes y liquidación |
| Exposición de datos de un tercero en el expediente | Baja | Alto, riesgo legal y de confianza | Minimización, expediente acotado al titular y modelado de amenazas propio | Suspender la emisión y revisar el alcance de campos |
| El expediente revela a un cliente la actividad del transportista con otro | Baja | Alto, contradice la promesa de la adhesión | El expediente lo emite y lo presenta el titular, nunca el CLIENTE a un tercero | Revocación del documento emitido y auditoría del acceso |

**Contingencia general si la innovación no rinde lo esperado.** El portal obligatorio de
CA-21 y CA-29 se entrega igual, porque la innovación es una capa sobre él y no una
condición de su funcionamiento. Lo que se pierde es el argumento de reciprocidad de la
adhesión, y esa pérdida se compensa con las medidas del numeral 5.8 del Subdocumento 3.

### Verificación contra el Capítulo 26 transversal

| Requisito | Cumplimiento |
|---|---|
| RT-26.01, ubicación en la arquitectura | Elemento 4, tabla de capas y componentes |
| RT-26.02, paquetes de la EDT y mes | Elemento 4, paquetes provisionales, definitivos en el Informe 2 |
| RT-26.03, madurez con escala y fuentes APA | Elemento 3, escala TRL y tres referencias por verificar |
| RT-26.04, riesgo, probabilidad, impacto, mitigación y contingencia | Elemento 7 |
| RT-26.05, indicador con línea base, meta y momento | Elemento 6 |
| RT-26.06, inteligencia artificial | No aplica. La innovación no incorpora inteligencia artificial |
| RT-26.07, modelado de amenazas propio | **Aplica.** El servicio público de verificación amplía la superficie expuesta y requiere su propio modelado, coordinado con D4 |
| RT-26.08, verificable antes del mes 16 | Sí. Primera medición en el mes 15 |

### Por qué no es una función que las Bases ya exigen

El Artículo 30° y el Capítulo 26 rechazan presentar como innovación una funcionalidad
exigida por las Bases. La delimitación es la siguiente.

**Lo que las Bases ya exigen** es que el transportista autenticado consulte sus viajes,
estados, evidencias y liquidación en curso, dentro del portal del CLIENTE (CA-21 y
CA-29, FEP03 · Capítulo 18 · p.41). Eso está comprometido en RF-020 y RF-022 y no se
presenta como innovación.

**Lo que agrega la innovación** es que esa evidencia salga del portal como un documento
del transportista, verificable por un tercero que no tiene acceso al sistema del
CLIENTE. Las Bases no lo piden. Tampoco cae en la exclusión del Capítulo 11, que
descarta administrar la contabilidad de los transportistas, porque el expediente no
administra nada, devuelve evidencia ya producida a su titular.

---

# Ficha 2. Innovación tipo 4, modelo de negocio o contratación

## Adhesión recíproca con consentimiento por ventana de viaje

### Elemento 1. Problema u oportunidad concreta, con el dato que la dimensiona

El proyecto necesita instalar equipamiento y capturar datos en camiones que no son del
CLIENTE, y no dispone de ningún mecanismo para conseguirlo. El gerente general fijó el
estándar con el que evaluará las propuestas.

> «Cuando alguien me diga "instalamos un dispositivo en toda la flota", le voy a
> preguntar quién le va a pedir permiso a ciento cuarenta y ocho dueños de camión, y
> qué les vamos a ofrecer a cambio. Si esa parte no está en la propuesta, la propuesta
> no sirve.» (FEP03 · Capítulo 8 · p.17)

Los datos que dimensionan el problema son cuatro. El 60,4 % de la capacidad no es
propiedad de la compañía. Son 226 camiones de 148 dueños con entre uno y cuatro
camiones cada uno. 34 camiones subcontratados no tienen ningún dispositivo de posición.
Y 258 de los 454 conductores no son trabajadores de la compañía (FEP03 · Secciones 2.2
y 2.3 · p.6).

El obstáculo no es el precio del aparato. Es una objeción de confianza, formulada con
precisión por el transportista.

> «Si el aparato es de ellos y anda prendido siempre, ellos van a saber cuándo trabajo
> para la competencia. Eso no se lo voy a dar.» (FEP03 · Capítulo 8 · p.17)

### Elemento 2. Tecnología, práctica o modelo que la sustenta

El modelo tiene tres piezas que funcionan juntas. Ninguna es tecnología nueva; lo nuevo
es el esquema de contratación que las combina.

**Pieza 1. Consentimiento acotado a la ventana del viaje, implementado en el
dispositivo.** El equipo a bordo instalado en un camión de tercero transmite al CLIENTE
únicamente entre la asignación del viaje y la confirmación de la descarga. Fuera de esa
ventana no transmite. No se trata de filtrar en el servidor lo que ya se capturó, sino
de que la ventana gobierne la transmisión en el propio dispositivo, de modo que el dato
de la actividad del transportista con otro cliente nunca llegue al CLIENTE. Es la
respuesta técnica y verificable a la objeción citada, y es también minimización en el
sentido de la normativa de datos personales.

**Pieza 2. Comodato del equipo, con la propiedad del dato separada de la del aparato.**
El hardware lo adquiere el CLIENTE conforme al Capítulo 11 del caso, y el PROPONENTE
especifica qué comprar. Lo que las Bases dejan abierto, y donde está la innovación, es
el régimen del equipo instalado en un camión ajeno. Se entrega en comodato al
transportista adherido, con el PROPONENTE a cargo de configuración, instalación,
soporte y retiro sin costo al término de la relación, y con prohibición de
reconfiguración unilateral.

**El cambio de modelo de negocio no está en quién compra el aparato, sino en quién
gobierna el dato que produce.** En el esquema convencional, quien paga el dispositivo
manda sobre lo que transmite, y por eso el dueño del camión lo rechaza. Aquí la
propiedad del equipo y la del dato se separan: el equipo es del CLIENTE, y la actividad
del transportista sigue siendo suya, con transmisión limitada por la ventana del viaje.
Eso es un cambio en la forma de capturar valor en el sentido del Artículo 28°, tipo 4,
porque convierte un activo de vigilancia en un servicio contratado con contraprestación
verificable.

**Pieza 3. Contraprestación medible y financiada por el propio proyecto.** El incentivo
económico no sale del margen operacional del CLIENTE, que es de 9 % (FEP03 · Capítulo
10, restricción 14 · p.23), sino de un ingreso que hoy se pierde por falta de prueba.
En 2025 se facturaron $340 millones por tiempos de espera y el 71 % fue objetado, es
decir $241,4 millones (FEP03 · Sección 7.2 · p.15). Esa objeción existe porque la hora
de llegada y de salida se anota en papel. La evidencia telemática que produce el
dispositivo es lo que permite sostener el cobro, y una parte del cobro recuperado se
reparte con el transportista cuyo camión produjo la evidencia.

**Modalidades de adhesión.** Completa, con equipo en comodato. De datos, sin equipo,
homologando el GPS que el transportista ya tiene. Sin adhesión, con validación
documental controlada. El detalle está en el numeral 5.6 del Subdocumento 3.

### Elemento 3. Nivel de madurez, con la escala utilizada y las fuentes

**Escala utilizada.** Niveles de madurez tecnológica, TRL, de 1 a 9, aplicados a los
componentes técnicos. El componente contractual se califica por precedente de uso, no
por TRL, porque no es una tecnología.

| Componente | Madurez | Fundamento |
|---|---|---|
| Control de transmisión por ventana en el dispositivo a bordo | TRL 8 | La gestión remota de configuración de dispositivos conectados es tecnología productiva; lo específico es la regla de negocio que la gobierna |
| Registro de consentimiento granular y revocable | TRL 8 | Práctica consolidada en plataformas de tratamiento de datos personales |
| Comodato de equipamiento a proveedores de servicio | Precedente establecido | Figura contractual de uso corriente, no requiere desarrollo |
| Reparto de recupero sobre evidencia aportada | Precedente acotado | Existe en esquemas de incentivo logístico, con poca documentación pública en el sector nacional |

**Referencias, en norma APA 7.ª edición.** Verificadas en su fuente oficial el 6 de
septiembre de 2026. La cita completa está en la bibliografía al final del documento.

- International Organization for Standardization. (2013). *Space systems. Definition of
  the Technology Readiness Levels (TRLs) and their criteria of assessment*
  (ISO 16290:2013).
- Ley N.º 21.719 de 2024. Regula la protección y el tratamiento de los datos personales
  y crea la Agencia de Protección de Datos Personales. 13 de diciembre de 2024. Diario
  Oficial de la República de Chile.
- Decreto con Fuerza de Ley N.º 1 de 2002 [Ministerio del Trabajo y Previsión Social].
  Fija el texto refundido, coordinado y sistematizado del Código del Trabajo, artículo
  25 bis. 16 de enero de 2003. Diario Oficial de la República de Chile.

**Dato normativo con efecto sobre el cronograma.** La Ley N.º 21.719 se publicó el 13
de diciembre de 2024 y entra en plena vigencia el **1 de diciembre de 2026**, es decir
seis días después de la entrega de propuestas en sobres cerrados y el mismo día en que
el Formulario T-20 fija la entrega de resultados de la licitación. El modelo de
consentimiento de esta innovación no se diseña para una norma futura, se diseña para
una norma que estará vigente desde el primer día del contrato.

### Elemento 4. Diseño de la incorporación

**Dónde se inserta en la arquitectura, RT-26.01.**

| Capa | Componente | Interfaz |
|---|---|---|
| Borde, a bordo | Unidad telemática y búfer local | Aplica la ventana de transmisión y almacena localmente fuera de ella |
| Integración | Concentrador de dispositivos conectados | Distribuye la configuración de ventana a cada equipo |
| Servicios de negocio | Servicio de Consentimiento y Servicio de Adhesión, componentes nuevos | Definen la ventana desde la asignación del viaje y registran la revocación |
| Presentación | Portal Unificado, sección del transportista | Consola de permisos, otorgamiento y revocación con bitácora |
| Datos | Registro de consentimiento y Auditoría Append Only | Conservan la traza de cada permiso y de cada acceso |

Los componentes **Servicio de Adhesión** y el flujo contractual asociado están
declarados como brecha en `matriz-trazabilidad-d2.md` y deben incorporarse en la
revisión con D3 y D4.

**Paquetes de la estructura de descomposición del trabajo, RT-26.02.** Provisionales,
definitivos en el Informe 2.

| Paquete provisional | Contenido | Mes |
|---|---|---:|
| P-ADH-01 | Diseño del anexo contractual y validación jurídica | 1 a 3 |
| P-ADH-02 | Modelo de consentimiento y ventana de viaje | 3 a 5 |
| P-ADH-03 | Cohorte piloto de adhesión, entre 10 y 15 transportistas | 6 a 9 |
| P-ADH-04 | Consola de permisos en el portal | 9 a 12 |
| P-ADH-05 | Campaña de enrolamiento por terminal | 10 en adelante, continua |
| P-ADH-06 | Medición de adhesión y de recupero en marcha blanca | 13 a 15 |

**Cuándo se materializa.** La adhesión **comienza en el mes 1**, antes que cualquier
construcción. El caso lo advierte de manera expresa, hay decisiones cuyo plazo no lo
fija la tecnología sino una negociación con terceros, y las negociaciones no se
paralelizan (FEP03 · Sección 13.1 · p.26). El resultado se mide en la marcha blanca,
meses 13 a 15.

### Elemento 5. Impacto económico estimado

**Inversión requerida.**

| Partida | Naturaleza | Estado |
|---|---|---|
| Equipamiento a bordo para camiones de terceros adheridos | Adquisición del CLIENTE, conforme al Capítulo 11; el PROPONENTE especifica y dimensiona | Cantidad determinada por la adhesión efectiva; precio unitario por cotizar |
| Conectividad y suscripciones de los equipos en comodato | Costo recurrente declarado en el TCO de 36 meses | Por cotizar |
| Diseño y validación jurídica del anexo contractual | Servicio profesional | Por cotizar |
| Campaña de enrolamiento en cinco terminales | Dotación y horas | Por cotizar, con presencia en horario de relevo |
| Consola de consentimiento y servicio de adhesión | Desarrollo | Por cotizar |

**Efecto en el costo operacional.** Tres efectos que deben presentarse juntos, porque
dos son favorables y uno no.

1. Aumenta el costo recurrente de conectividad, soporte y reposición de cada equipo en
   comodato, proporcional a la adhesión efectiva y no al total de 226 camiones de
   terceros. Se declara íntegro en el TCO de 36 meses de RNF-010.
2. Disminuye el costo de la liquidación mensual, que hoy ocupa 9 días y 8 personas para
   148 transportistas (FEP03 · Sección 7.3 · p.15).
3. Disminuye el costo de gestionar las objeciones de cobro de sobreestadía.

El CLIENTE opera con un margen de 9 % y evaluará con especial atención el costo de
operación de los 36 meses (FEP03 · Capítulo 10, restricción 14 · p.23), de modo que el
punto 1 se dimensiona sobre la adhesión efectiva y se revisa en cada cierre.

**Beneficio esperado.** Se declara sobre la base verificada de 2025 y con la meta
propuesta por el PROPONENTE, y se identifica cuál cifra es dato y cuál es meta.

| Concepto | Valor | Origen |
|---|---|---|
| Cobros por espera facturados en 2025 | $340 millones | Dato, FEP03 · Sección 7.2 · p.15 |
| Porcentaje objetado en 2025 | 71 % | Dato, misma fuente |
| Monto objetado en 2025 | $241,4 millones | Aritmética sobre los dos datos anteriores |
| Meta de objeción con evidencia telemática | Bajo 20 % de los cobros respaldados | **Meta del PROPONENTE**, comprometida en CA-11 |
| Recupero anual implícito si se alcanza la meta | Del orden de $173 millones | Cálculo derivado de la meta, no un compromiso de ingreso |

El recupero es el que financia el incentivo de la adhesión. Su reparto concreto entre
CLIENTE y transportista se fija en el anexo contractual y **no se define en este
informe**, porque depende de la validación comercial y jurídica del numeral 5.4 del
Subdocumento 3.

**Valorización en el flujo de caja.** Informe 3, conforme al Formulario T-22.

### Elemento 6. Indicador de verificación del beneficio

| Indicador | Línea base | Meta propuesta | Momento de medición |
|---|---|---|---|
| Transportistas con anexo firmado | 0 de 148 | 70 %, es decir 104 de 148 | Cierre de la Etapa 1, mes 16 |
| Transportistas con anexo firmado | 0 de 148 | 90 %, es decir 134 de 148 | Cierre de la Etapa 2, mes 21 |
| Camiones con posición disponible | 340 de 374, en tres plataformas sin vista única | Vista única de 374 con nivel de evidencia declarado por unidad | Mensual desde el mes 10 |
| Objeción sobre cobros de espera respaldados | 71 % | Bajo 20 % | Tercer cierre mensual posterior al mes 16 |
| Tasa de revocación del consentimiento | 0, no existe el mecanismo | Bajo 10 % de los adheridos | Mensual desde el mes 13 |
| Duración de la liquidación mensual | 9 días y 8 personas | Un día hábil | Tercer cierre posterior al mes 16 |

La primera medición de adhesión firmada ocurre desde el mes 3, mucho antes del mes 16,
lo que satisface con holgura el requisito deseable RT-26.08.

La línea base de 340 de 374 camiones con dispositivo es dato de las Bases (FEP03 ·
Sección 2.2 · p.6). Esa misma tabla observa que los 34 sin dispositivo son
subcontratados y que los que sí tienen se reparten entre tres proveedores distintos. La
meta se expresa sobre el total de 374 y no sobre el subconjunto de terceros, para no
apoyar el indicador en una resta que las Bases no declaran de manera inequívoca.

### Elemento 7. Riesgo de adopción

| Riesgo | Probabilidad | Impacto | Mitigación | Contingencia |
|---|---|---|---|---|
| La adhesión no alcanza el 70 % en la Etapa 1 | Media | Alto, limita jornada, posición y emisiones sobre el 60,4 % de la capacidad | Comenzar en el mes 1, cohorte piloto en el mes 6 y beneficio verificable antes de pedir el equipo | Escalonar el incentivo, priorizar retornos a la flota adherida y extender la modalidad de datos sin equipo |
| El transportista desconfía de la ventana de transmisión | Media | Alto, es la objeción declarada en la entrevista | Hacer la ventana auditable por el propio transportista desde su consola de permisos | Ofrecer verificación por un tercero independiente sobre el comportamiento del equipo |
| El recupero de sobreestadía es menor al proyectado | Media | Medio, encarece el incentivo | Medir el recupero en la cohorte piloto antes de comprometer el reparto general | Ajustar el reparto conforme a la cláusula de revisión del anexo |
| Los clientes no aceptan la evidencia telemática como respaldo del cobro | Media | Alto, elimina la fuente de financiamiento del incentivo | Acordar con el área comercial el reconocimiento contractual de la geocerca sellada | Financiar el incentivo con la reducción del costo de liquidación, que no depende del cliente |
| El anexo contractual no resiste revisión jurídica | Baja | Alto, bloquea todo el modelo | Validación jurídica en los meses 1 a 3, antes de construir | Reducir el alcance del consentimiento a lo estrictamente necesario para acreditar jornada |
| El costo recurrente del parque en comodato excede lo previsto | Media | Medio, presiona el TCO de 36 meses frente al margen de 9 % | Dimensionar sobre adhesión efectiva y no sobre los 226 camiones; escalonar la compra por cohorte | Revisar el plan de reposición y el alcance de la modalidad de datos, que no requiere equipo |
| Un transportista revoca el consentimiento a mitad de viaje | Media | Medio, deja el viaje sin evidencia | Separar revocación de captura futura, de visibilidad y de retención obligatoria | Conservar la evidencia cuya retención es legal y bloquear la asignación siguiente |

**Contingencia general si la innovación no rinde lo esperado.** La solución opera en
modo mixto de manera permanente, con validación telemática para la flota adherida y
validación documental controlada para el resto, sin presentar la segunda como
equivalente a la primera. Las capacidades que dependen de datos de terceros quedan
declaradas con su cobertura real, en vez de prometerse sobre una flota que no las
alimenta.

### Verificación contra el Capítulo 26 transversal

| Requisito | Cumplimiento |
|---|---|
| RT-26.01, ubicación en la arquitectura | Elemento 4, tabla de capas y componentes |
| RT-26.02, paquetes de la EDT y mes | Elemento 4, paquetes provisionales, definitivos en el Informe 2 |
| RT-26.03, madurez con escala y fuentes APA | Elemento 3, escala TRL y tres referencias por verificar |
| RT-26.04, riesgo, probabilidad, impacto, mitigación y contingencia | Elemento 7 |
| RT-26.05, indicador con línea base, meta y momento | Elemento 6 |
| RT-26.06, inteligencia artificial | No aplica. La innovación no incorpora inteligencia artificial |
| RT-26.07, modelado de amenazas propio | **Aplica.** El control de transmisión por ventana modifica la arquitectura de seguridad del borde y requiere modelado propio, coordinado con D4 |
| RT-26.08, verificable antes del mes 16 | Sí. Adhesión firmada medible desde el mes 3 |

### Por qué no es una función que las Bases ya exigen

**Lo que las Bases ya resuelven** es quién compra el hardware. El Capítulo 11 del caso
declara que lo adquiere el CLIENTE y que el PROPONENTE debe especificar qué comprar.
Presentar «el CLIENTE compra el dispositivo» como innovación sería presentar como
propia una decisión que ya está en las Bases.

**Lo que las Bases dejan expresamente abierto** es la decisión 5 del numeral 16.1, qué
ocurre con un dispositivo a bordo en un camión de un tercero, quién lo administra y qué
se le ofrece a su dueño (FEP03 · Sección 16.1 · p.34). Y el Capítulo 10, restricción 2,
obliga a que lo que dependa de terceros se consiga por contrato, por incentivo o por
diseño, con su viabilidad argumentada en la propuesta.

**Lo que agrega la innovación** son tres cosas que las Bases no piden. La ventana de
transmisión gobernada en el dispositivo, que convierte una promesa de privacidad en una
propiedad verificable. El comodato con retiro sin costo, que elimina el riesgo
patrimonial del transportista. Y el financiamiento del incentivo con el recupero de un
ingreso que hoy se pierde, que hace que la adhesión no compita con el margen de 9 % del
CLIENTE.

---

## Bibliografía

Referencias en norma APA 7.ª edición. Todas fueron verificadas en su fuente oficial el
**6 de septiembre de 2026**, fecha de consulta que se declara conforme a las
Indicaciones del curso.

**Normas técnicas**

International Organization for Standardization. (2013). *Space systems. Definition of
the Technology Readiness Levels (TRLs) and their criteria of assessment*
(ISO 16290:2013). https://www.iso.org/standard/56064.html

> Norma vigente. Primera edición de noviembre de 2013, confirmada en la revisión
> periódica de 2024. La propia norma declara que su ámbito primario son los sistemas
> espaciales y que sus definiciones pueden usarse en dominios más amplios, que es el
> uso que se le da aquí.

**Especificaciones**

World Wide Web Consortium. (2025, 15 de mayo). *Verifiable credentials data model v2.0*
(Recomendación del W3C). https://www.w3.org/TR/vc-data-model-2.0/

> Alcanzó el estado de Recomendación del W3C el 15 de mayo de 2025, junto con el resto
> de la familia de especificaciones de credenciales verificables 2.0.

**Textos legales**

Decreto con Fuerza de Ley N.º 1 de 2002 [Ministerio del Trabajo y Previsión Social].
Fija el texto refundido, coordinado y sistematizado del Código del Trabajo. 16 de enero
de 2003. Diario Oficial de la República de Chile.

> El artículo 25 bis regula la jornada de los choferes de vehículos de carga terrestre
> interurbana, que es exactamente la operación del caso. Fija un máximo de 180 horas
> mensuales distribuidas en no menos de 21 días, un descanso mínimo ininterrumpido de 8
> horas dentro de cada 24, y un máximo de 5 horas continuas de conducción seguidas de
> un descanso de al menos 2 horas. **Existe tramitación legislativa posterior sobre
> esta materia, de modo que la redacción vigente debe reconfirmarse antes de la oferta
> final del 25 de noviembre de 2026.**

Ley N.º 19.799 de 2002. Sobre documentos electrónicos, firma electrónica y servicios de
certificación de dicha firma. 12 de abril de 2002. Diario Oficial de la República de
Chile.

> Promulgada el 25 de marzo de 2002 y publicada el 12 de abril de 2002 por el entonces
> Ministerio de Economía, Fomento y Reconstrucción. Ha sido objeto de modificaciones
> posteriores, por lo que se cita su texto vigente a la fecha de consulta.

Ley N.º 21.719 de 2024. Regula la protección y el tratamiento de los datos personales y
crea la Agencia de Protección de Datos Personales. 13 de diciembre de 2024. Diario
Oficial de la República de Chile.

> Publicada el 13 de diciembre de 2024. Su entrada en plena vigencia es el 1 de
> diciembre de 2026, dentro del horizonte de este contrato.

**Fuentes primarias de la licitación**

Las Bases Administrativas (FEP01), las Bases Técnicas Transversales (FEP02) y las Bases
Técnicas del Caso 10 (FEP03) se citan en el cuerpo por documento, artículo o capítulo y
página impresa, de modo que cada cita sea verificable contra el documento entregado por
el CLIENTE.

## Control antes de consolidar el subdocumento 13

- [ ] Coordinar con D3 la incorporación del Servicio de Emisión de Expediente, del
      Servicio de Verificación y del Servicio de Adhesión.
- [ ] Coordinar con D4 el modelado de amenazas que exige RT-26.07 para ambas fichas.
- [ ] Reemplazar los códigos provisionales de paquetes por los de la EDT del Informe 2.
- [ ] Confirmar con el área comercial la viabilidad del reconocimiento contractual de la
      evidencia de geocerca ante los 84 clientes.
