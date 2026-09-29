# Subdocumento 3. Esquema de solución y alcance

**Licitación TFEP-01/2026 · Caso 10 · Transportes Curimón S.A.**\
**Empresa proponente:** AUDIT\
**Dupla responsable:** Ignacio C. y Matías V.\
**Ponderación:** 21 % del Informe 1, 12 % del Informe 2, 10 % de la ponderación final
(FEP01 · Formulario T-21 · p.66)

**Estado:** versión 1 para el Informe 1 del 07-09-2026. Los mecanismos, las etapas y las
metas de este documento son propuesta del PROPONENTE. Ninguna afirmación de aquí
acredita cumplimiento demostrado.

---

## 1. Principio de solución

El problema del CLIENTE no es que le falten sistemas. Es que **responde por una
operación que en su mayor parte no controla**. El 60,4 % de la capacidad gestionada
pertenece a 148 transportistas subcontratados y 258 de los 454 conductores no son sus
trabajadores (FEP03 · Sección 2.2 · p.6; Capítulo 10, restricción 2 · p.23). El
gerente general lo dice sin rodeos, no les puede dar una orden, solo puede ponerles
condiciones contractuales, pagarles distinto o dejar de darles viajes (FEP03 ·
Capítulo 8 · p.17).

De ahí se sigue el principio que ordena toda la propuesta.

> **La solución hace coincidir responsabilidad y control mediante evidencia
> verificable, adhesión contractual de terceros y una implantación gradual que no
> depende de cobertura permanente.**

Ese principio se descompone en cuatro reglas de diseño que se aplican sin excepción a
lo largo del subdocumento.

1. **Lo que la compañía debe acreditar, la solución lo produce como evidencia, no como
   declaración.** El accidente del 14 de febrero ocurrió porque un dato existía y no
   estaba en ningún sistema de la compañía, ya que no era suyo. Una solución que
   registre mejor lo propio no habría evitado nada.
2. **Lo que depende de un tercero se consigue por contrato, por incentivo o por
   diseño, nunca por instrucción.** Toda capacidad que necesite datos de un
   transportista está condicionada a su adhesión, y esa condición es visible en la
   operación en vez de quedar disimulada.
3. **La operación esencial funciona sin cobertura.** Hay tramos de más de 80 km
   continuos sin señal y son parte permanente de la operación, no una excepción
   (FEP03 · Capítulo 10, restricción 4 · p.23).
4. **El bloqueo es la función, no el efecto secundario.** El gerente de operaciones lo
   pidió textualmente, prefiere que el sistema le impida asignar a que lo deje pasar
   (FEP03 · Capítulo 8 · p.17). Un incumplimiento legal o de seguridad no se convierte
   en excepción por una autorización operacional.

## 2. Coherencia entre el problema y la solución

La tabla siguiente conecta cada dolor medido del Capítulo 7 con la capacidad que lo
atiende y con los requisitos que la especifican. El catálogo completo de 28 requisitos
funcionales y 14 no funcionales está en `catalogo-requisitos-d2.md`, y su trazabilidad
hasta componente y prueba en `matriz-trazabilidad-d2.md`.

| Dolor medido | Valor 2025 | Capacidad de la solución | Requisitos |
|---|---|---|---|
| Conductores sin control de jornada | 196 de 454 | Despacho seguro con verificación bloqueante | RF-001, RF-002, RF-028 |
| Jornada previa de un conductor de un tercero | inexistente | Expediente de jornada por persona | RF-003, RF-007 |
| Verificación de vigencias al asignar | inexistente | Registro único de las 6.000 vigencias | RF-005 |
| Vencimientos vivos | 6.000 en cuatro planillas | Registro único con alerta y bloqueo | RF-005 |
| Camiones sin dispositivo de posición | 34 de 374 | Vista única con nivel de evidencia declarado | RF-008, RF-028 |
| Plataformas de posición en uso | 3, sin vista unificada | Ingestión y homologación multiproveedor | RF-008 |
| Kilómetros recorridos en vacío | 26 % del total | Recomendación de retorno bajo restricciones | RF-015 |
| Cobros por espera objetados | 71 % de $340 millones | Evidencia de permanencia con sello temporal | RF-010, RF-011 |
| Respaldos de entrega que no llegan | 4,2 % | Conformidad digital disponible el mismo día | RF-012 |
| Desfase del consumo de combustible | hasta 40 días | Costeo por viaje con componentes pendientes explícitos | RF-016 |
| Contratos servidos bajo costo | 3 de 8, 31 % del ingreso | Costo real por ruta y contrato | RF-016, RF-017 |
| Dispersión de rendimiento sin investigar | 19 % | Análisis reproducible sobre cohorte comparable | RF-018 |
| Duración de la liquidación mensual | 9 días, 8 personas | Liquidación automática por excepción | RF-019 |
| Liquidaciones corregidas tras emitirse | 11 % | Cálculo desde evidencia del viaje | RF-019 |
| Visibilidad del transportista | inexistente | Portal del transportista | RF-020, RF-026 |
| Posición de la carga para el cliente | inexistente | Portal de cliente sujeto a consentimiento | RF-021, RF-022 |
| Emisiones por tonelada-kilómetro | no se mide | Base metodológica y cálculo verificable | RF-023 |
| Detenciones por sobrepeso | 142, 18 h promedio | Verificación previa al despacho | RF-001, RF-006 |
| Detenciones por carga peligrosa | 1, con multa | Verificación de carga efectiva contra manifiesto | RF-006 |

Los valores de la columna central provienen de FEP03 · Secciones 7.1, 7.2 y 7.3 ·
pp.14-15, y de la Sección 2.2 · p.6.

## 3. Capacidades de la solución

Las nueve capacidades siguientes agrupan los 42 requisitos. Cada una declara qué
produce y de qué depende, porque varias no dependen de la tecnología sino de una
negociación con terceros.

| Capacidad | Qué produce | De qué depende |
|---|---|---|
| Despacho seguro | Autorización o bloqueo de la asignación en no más de 30 segundos, con motivo registrado | Expediente de jornada vigente y registro de vigencias saneado |
| Expediente de jornada | Historial por persona, con fuente, sello temporal, integridad e historial de correcciones | Acceso contractual a registros del transportista y validación jurídica |
| Registro único de vigencias | Titular, custodio, vencimiento, alerta y efecto bloqueante para 6.000 vigencias | Conciliación de las cuatro planillas actuales |
| Viaje y evidencia | Posición, permanencias, llegada y salida automáticas, conformidad de entrega | Adhesión del dueño del camión y cobertura declarada |
| Operación desconectada | 72 horas de registro local sin pérdida, con sincronización ordenada y sin duplicados | Capacidad de borde y reglas de conciliación |
| Integración tributaria | Documento electrónico de transporte conforme antes del movimiento, con el sistema contable como único emisor | Interfaz y mecanismo de contingencia del sistema contable |
| Costeo y liquidación | Costo por kilómetro, viaje, ruta y contrato; liquidación por excepción | Identificadores comunes entre fuentes de costo |
| Portales y consentimiento | Autoservicio del transportista y del cliente, con permisos granulares y revocables | Modelo de consentimiento y adhesión |
| Implantación progresiva | Despliegue camión por camión sin detener la flota, con convivencia y reversión | Frecuencia real de paso por terminal |

Ninguna capacidad se declara disponible para el 100 % de la flota por el solo hecho de
estar construida. La cobertura efectiva de las capacidades que tocan camiones de
terceros es una función de la adhesión, y por eso el Capítulo 5 de este subdocumento
tiene el mismo peso que los anteriores.

## 4. Alcance por etapas y su justificación

El detalle de capacidades, entradas, salidas, criterios de avance y exclusiones de cada
etapa está en `alcance-etapas-d2.md`. Aquí se justifica el reparto, que es lo que el
caso exige expresamente.

### 4.1. Por qué este reparto y no el orden del comité

El comité expresó un orden de urgencia, primero seguridad, luego viaje y evidencia, y
por último costo, liquidación y emisiones (FEP03 · Sección 13.1 · p.26). Ese mismo
capítulo advierte que repetirlo sin analizarlo se evalúa como falta de criterio
profesional, y que el CLIENTE contrata ingeniería, no obediencia.

**El PROPONENTE altera ese orden en un punto y lo mantiene en el resto.**

El costeo por ruta y contrato **se adelanta a la Etapa 1**, en contra de la tercera
prioridad del comité. El fundamento es un hito externo con fecha, no una preferencia.
Dos de los tres contratos servidos bajo costo se renegocian en 2027 (FEP03 · Sección
13.2 · p.27), y la Etapa 2 no entra en producción antes del mes 21 (FEP01 · Artículo
17° · p.12). Dejar el costo real para la Etapa 2 significa renegociar a ciegas por
segunda vez, que es exactamente la objeción que la gerenta de administración y finanzas
dejó registrada. Un contrato servido a menos 14 % durante cuatro años cuesta más que el
adelanto del módulo de costeo.

El resto del orden se mantiene, y por dependencia técnica, no por deferencia.

- La seguridad va primero porque el bloqueo de la asignación necesita el registro de
  vigencias saneado y el expediente de jornada, y ambos son entradas de todo lo demás.
- La posición en tiempo real para el cliente **no** se adelanta, pese a ser atractiva
  comercialmente. El jefe de control de flota dejó la objeción correcta, no se puede
  prometer posición en tiempo real sin resolver antes qué están dispuestos a compartir
  148 dueños de camión, y esa conversación toma meses (FEP03 · Sección 13.1 · p.26).
  Prometerla antes de la adhesión sería prometer un dato que no se tiene derecho a
  capturar.
- Las emisiones quedan repartidas. La base de datos, la línea base y la metodología en
  la Etapa 1; el cálculo productivo completo en la Etapa 2. La exigencia del cliente
  exportador es para 2029 (FEP03 · Sección 13.2 · p.27), de modo que lo que no admite
  espera es fijar la metodología, no producir el número.

### 4.2. Criterio general de distribución

Cinco criterios ordenan el reparto, aplicados en este orden de precedencia.

1. **Riesgo legal y operacional.** Primero se controla lo que puede producir un
   despacho ilegal, una pérdida probatoria o una duplicación tributaria.
2. **Dependencias.** No se escala hardware ni analítica antes de conocer interfaces,
   calidad de datos, cobertura y compatibilidad vehicular.
3. **Adopción.** Ninguna capacidad que dependa de terceros se masifica antes de probar
   adhesión, consentimiento y beneficio para el transportista.
4. **Continuidad.** La solución convive con los sistemas y la flota actuales sin una
   detención general.
5. **Valor medible.** La Etapa 1 establece líneas base y datos confiables; la Etapa 2
   los usa para optimizar y ampliar cobertura.

### 4.3. Resumen del reparto

| Etapa 1, producción desde el mes 16 | Etapa 2, producción desde el mes 21 |
|---|---|
| Registro único de conductores, equipos y vigencias | Optimización de la carga de retorno |
| Jornada y evidencia oponible | Costeo avanzado y análisis de rentabilidad |
| Verificación bloqueante de la asignación | Mantenimiento por condición |
| Gestión y reconstrucción del viaje real | Consolidación de telemetría de fábrica |
| Documento electrónico de transporte | Emisiones verificables en producción |
| Operación desconectada de 72 horas | Capacidades analíticas avanzadas |
| Costeo por viaje, ruta y contrato | Portal de talleres externos |
| Plan y portal inicial de adhesión | Evolución del portal y automatizaciones |
| Posición según consentimiento disponible | Ampliación según progreso de la adhesión |

Las ventanas del Artículo 17° son obligatorias e indivisibles. A ellas se suma una
restricción propia del caso que el plan debe respetar, ningún paso a producción puede
ocurrir entre diciembre y abril, ni en las ventanas de restricción vehicular, ni
durante el cierre mensual de liquidaciones (FEP03 · Sección 13.3 · p.27). **Supuesto
declarado.** Como la fecha de inicio del contrato no está fijada en las Bases, el
PROPONENTE asume que el CLIENTE la definirá de modo que el mes 16 no caiga dentro de la
temporada de fruta. Si cayera, el paso a producción se corre al primer mes hábil
posterior y el PROPONENTE lo declarará en el plan de trabajo del Informe 2.

## 5. Plan de adhesión de los 148 transportistas

Esta es la parte de la propuesta que el gerente general anunció que iba a mirar
primero. Su frase fue que cuando alguien le diga que instalará un dispositivo en toda
la flota, preguntará quién le va a pedir permiso a 148 dueños de camión y qué se les
va a ofrecer a cambio, y que si esa parte no está, la propuesta no sirve (FEP03 ·
Capítulo 8 · p.17).

### 5.1. Qué se les pide

Tres cosas, y ninguna es la instalación del aparato.

1. **Autorización de acceso** a los registros de jornada de sus conductores, en la
   medida y por el período necesarios para acreditar la jornada de los viajes que
   ejecuten para el CLIENTE.
2. **Consentimiento de tratamiento** de posición y actividad, acotado a la ventana del
   viaje asignado por el CLIENTE.
3. **Aceptación del equipamiento a bordo** en régimen de comodato, para quienes adhieran
   en la modalidad completa.

### 5.2. Qué se les ofrece

La contraprestación no es discursiva. Se compone de cuatro beneficios que el
transportista puede verificar por sí mismo, y tres de ellos resuelven un dolor que él
mismo declaró en la entrevista.

| Beneficio | Línea base actual | Compromiso propuesto |
|---|---|---|
| Liquidación visible en curso y pago más rápido | Ve su liquidación 9 días después del cierre | Viajes y liquidación en curso consultables en cualquier momento |
| Menos correcciones posteriores | 11 % de liquidaciones corregidas tras emitirse | Cálculo desde la evidencia del viaje, con corrección como excepción auditable |
| Reparto de la sobreestadía recuperada | 71 % de $340 millones objetado por falta de prueba | Participación declarada en el cobro que su propia evidencia permita sostener |
| Hoja de servicio portable | No dispone de ningún registro propio verificable | Expediente exportable y verificable por terceros, descrito en la ficha T-19 tipo 1 |

El cuarto beneficio es el que responde a la condición que el transportista puso
textualmente, que el aparato le sirva a él para demostrar que está en regla y no solo
para que lo vigilen (FEP03 · Capítulo 8 · p.17). Se desarrolla como innovación tipo 1
en `fichas-t19-d2.md`.

### 5.3. Quién compra, quién administra y quién tiene el dispositivo

Las Bases resuelven la primera mitad de la pregunta y no admiten lectura alternativa.
**Todo el hardware lo adquiere el CLIENTE**, y el PROPONENTE debe especificar qué
comprar, cuánto y con qué características (FEP03 · Capítulo 11 · p.24).

Lo que el caso deja abierto es la segunda mitad, y la formula en el numeral 16.1,
decisión 5, preguntando *de quién es el dispositivo a bordo en un camión de un tercero,
quién lo administra y qué ocurre con él si el transportista deja de trabajar con la
compañía* (FEP03 · p.34). Sobre esa parte sí decide el PROPONENTE.

| Materia | Propuesta del PROPONENTE |
|---|---|
| Adquisición y propiedad | Del CLIENTE, conforme al Capítulo 11, para toda la flota |
| Especificación de qué comprar | Del PROPONENTE, con cantidad y características declaradas |
| Tenencia en camión de tercero | Del transportista adherido, en comodato, mientras dure la relación comercial |
| Configuración, instalación y soporte | Del PROPONENTE, como parte del servicio, en el paso normal por terminal |
| Conectividad y suscripciones | Declaradas en el costo total de operación de 36 meses |
| Retiro | En el primer paso por terminal al término de la relación, sin costo para el transportista |
| Daño o pérdida | Régimen declarado en el anexo de adhesión, distinguiendo uso normal de negligencia |
| Equipos preexistentes del transportista | No se intervienen. Se homologa la vista, conforme al Capítulo 11 |

**Lo que hace viable la adhesión no es quién paga el aparato, sino de quién son los
datos.** El transportista entrevistado hizo tres preguntas, quién lo paga, quién ve esa
información y qué pasa con ella cuando trabaja para otro cliente (FEP03 · Capítulo 8 ·
p.17). La primera la responden las Bases. Las otras dos las responde el diseño, y son
las que deciden si adhiere. Por eso la propuesta **separa la propiedad del equipo de la
propiedad del dato**. El equipo es del CLIENTE; el dato de la actividad del transportista
sigue siendo suyo, y el dispositivo solo transmite dentro de la ventana del viaje
asignado. Esa separación es el núcleo de la innovación tipo 4.

### 5.4. Instrumento contractual

Un anexo al contrato de transporte vigente, no un contrato nuevo, para no reabrir la
negociación comercial completa con 148 contrapartes. El anexo regula el acceso a
registros de jornada, el consentimiento de tratamiento con su alcance y su revocación,
el comodato del equipo, el reparto de la sobreestadía recuperada y las causales de
término. La redacción del anexo es responsabilidad del CLIENTE con apoyo del
PROPONENTE. **No es un dictamen jurídico y requiere validación legal antes de su uso.**

### 5.5. Cómo se enrola y cómo se capacita

El enrolamiento sigue el ritmo físico de la operación, no un calendario de escritorio.
Un camión pasa por un terminal cada 6 días en promedio y el 22 % de la flota
subcontratada pasa menos de una vez al mes (FEP03 · Capítulo 10, restricción 5 · p.23).
Ese 22 % es aproximadamente 50 camiones y define el límite físico de cualquier meta de
cobertura.

La capacitación considera que los conductores no están en un lugar fijo, que 258 de
ellos no son trabajadores de la compañía y que el relevo en terminal es de madrugada
(FEP03 · Sección 13.3 · p.27). Por eso se diseña como capacitación de dos minutos en el
punto de paso, sin aula y sin material que el conductor deba conservar, y se apoya en
que la interfaz a bordo no exige interacción en marcha.

### 5.6. Modalidades de adhesión y qué ocurre con quien no adhiere

Tres modalidades, y la tercera no es un castigo sino un modo de operación declarado.

| Modalidad | Qué aporta el transportista | Qué capacidades habilita |
|---|---|---|
| Completa | Consentimiento, acceso a jornada y equipo en comodato | Todas, incluida posición en tiempo real y hoja de servicio |
| De datos | Consentimiento y acceso a jornada, sin equipo, homologando su GPS actual | Posición homologada, jornada acreditada, portal y liquidación |
| Sin adhesión | Nada | Validación documental controlada, sin posición ni jornada telemática |

Quien no adhiere sigue operando. **Lo que no ocurre es que su nivel de evidencia se
presente como equivalente al de un camión adherido.** La vista de la torre distingue
visiblemente cobertura completa, homologada, documental y no disponible (RF-008,
RF-028). Esa distinción es lo que impide que el período de flota mixta genere dos
formas paralelas de trabajar que después no se puedan unificar, que es el riesgo que el
propio caso señala (FEP03 · Capítulo 17 · p.41).

### 5.7. Cómo se mide la adhesión

Ocho indicadores, medidos mensualmente desde el mes 1.

1. Transportistas contactados.
2. Transportistas con anexo firmado.
3. Vehículos enrolados, por modalidad.
4. Conductores capacitados.
5. Viajes con jornada acreditada por fuente.
6. Transportistas que consultan su liquidación en curso.
7. Tasa de revocación del consentimiento.
8. Tiempo desde la firma hasta la activación efectiva.

**Metas propuestas, sujetas a ratificación.** Adhesión de al menos el 70 %, es decir
104 de 148, al cierre de la Etapa 1, y de al menos el 90 %, es decir 134 de 148, al
cierre de la Etapa 2. Estas metas son oferta del PROPONENTE y no exigencia textual de
las Bases. La cobertura telemática de la flota es un indicador distinto y no debe
confundirse con el porcentaje de transportistas adheridos, porque los 148 transportistas
tienen entre uno y cuatro camiones cada uno.

### 5.8. Contingencia si la adhesión es insuficiente

Si al mes 9 la adhesión firmada es inferior al 40 %, se activan tres medidas en este
orden, y las tres están costeadas en el modelo económico.

1. Ampliar el reparto de la sobreestadía recuperada, que es el incentivo con mejor
   relación entre costo para el CLIENTE y valor percibido por el transportista.
2. Priorizar la asignación de retornos a la flota adherida, dentro de lo que permita el
   contrato vigente y sin comprometer el nivel de servicio al cliente final.
3. Extender la modalidad de datos, que no requiere instalar nada, a transportistas que
   rechazan el equipo pero aceptan compartir jornada y posición.

Lo que **no** se hace es rebajar el estándar probatorio ni presentar la validación
documental como equivalente a la telemática. La compañía responde por la jornada del
conductor que despacha, sea propio o de un tercero (FEP03 · Capítulo 10, restricción 7 ·
p.23), y esa responsabilidad no cambia con la tasa de adhesión.

## 6. Supuestos y decisiones declaradas

El Capítulo 16 del caso deja 26 decisiones deliberadamente sin resolver, y el Capítulo
19 evalúa que estén resueltas y declaradas como supuesto (FEP03 · p.34 y p.43). **Las
26 están resueltas y ratificadas por el PROPONENTE**, con su detalle en
`registro-decisiones-d2.md`. Ninguna queda implícita ni se traslada al CLIENTE.

Resolverlas no equivale a validarlas. Cada decisión distingue lo que el PROPONENTE
decide, que es alcance, de lo que debe confirmarse con un tercero, que es viabilidad.
Las siguientes son las decisiones cuya validación externa condiciona el alcance
comprometido, y se declaran como supuestos con su impacto explícito.

- **D-01, jornada de conductores externos.** Se decide el expediente multifuente por
  persona y el bloqueo sin excepción operacional. La suficiencia probatoria requiere
  validación jurídica. Si resultara insuficiente, cambia el medio de acreditación, no la
  regla de bloqueo.
- **D-05, propiedad y administración del dispositivo.** Se decide el régimen del
  numeral 5.3. El CLIENTE adquiere el hardware conforme al Capítulo 11 y el equipo del
  camión ajeno se entrega en comodato al transportista adherido, con el PROPONENTE a
  cargo de configuración, instalación, soporte y retiro. Falta costear ese servicio y
  formalizar el anexo contractual.
- **D-09, emisión tributaria sin cobertura.** Se decide usar exclusivamente el mecanismo
  offline oficialmente soportado por el sistema contable. Si no existiera tal mecanismo,
  el documento conforme antes del movimiento no es alcanzable y el CLIENTE debe
  gestionar la autorización ante la autoridad tributaria.
- **D-10, conformidad de entrega.** Se decide firma con código de un solo uso del
  receptor identificado, operable sin cobertura. Requiere validación jurídica de su
  valor probatorio frente a los clientes.
- **D-12 y D-13, telemetría y tacógrafo.** Se decide acceso remoto de solo lectura como
  vía primaria, con lectura física sujeta a autorización expresa por modelo. Los 61
  tractocamiones con telemetría de fábrica se incorporan según autorización del
  fabricante, sin afectar la garantía.
- **D-23 y D-24, consentimiento y retención.** Se decide consentimiento granular y
  revocable, con evidencia protegida en registro inalterable. La articulación entre
  revocación y retención legal requiere validación jurídica.
- **D-26, operación mixta.** Se decide validación telemática para equipados y
  documental reforzada para el resto, con el nivel de evidencia siempre visible. Si la
  vía documental resultara insuficiente para acreditar jornada, la cobertura de la
  Etapa 1 se restringe a la flota adherida.

## 7. Exclusiones y límites del alcance

El PROPONENTE adopta íntegramente las exclusiones del Capítulo 11 del caso y declara
además tres límites propios.

**Del Capítulo 11 · p.24.** No se reemplaza el sistema contable ni la emisión de
documentos tributarios. No se interviene la electrónica de fábrica del vehículo. No se
reemplazan las plataformas de posición de camiones de terceros, aunque sí se unifica la
vista. No se administra la contabilidad de los transportistas. No se instala
infraestructura en los puntos de carga y descarga de clientes.

**Límites propios del PROPONENTE.**

1. No se promete visibilidad donde no exista señal, exportación o adhesión. La ausencia
   se muestra como ausencia.
2. No se ofrece cálculo productivo completo de emisiones en la Etapa 1. Lo que se
   compromete en esa etapa es la base de datos, la línea base y la metodología
   declarada y verificable.
3. No se comprometen capacidades que dependan de datos open book de los transportistas
   sin su autorización expresa.

Que algo esté excluido no significa que se ignore en el diseño. Las dependencias que
cada exclusión genera están identificadas en la matriz de trazabilidad.

## 8. Criterios de aceptación y verificación

Los 29 criterios del Capítulo 18 del caso están comprometidos, con su línea base, su
meta, el hito y el método de medición, en `criterios-aceptacion-d2.md`. La distinción
que ese documento mantiene es la siguiente. Donde las Bases fijan el resultado, se marca
**Obligatorio** y el PROPONENTE lo compromete sin condición. Donde las Bases dejan el
umbral a propuesta del oferente, se marca **meta del PROPONENTE** y se declara como
oferta propia, no como exigencia del texto. Y donde el valor no puede fijarse sin
levantamiento previo, se marca **parámetro a fijar en la Etapa 1**, comprometiendo el
hito y el método en vez de un número anterior a la medición. Los siete supuestos bajo
los que se sostienen esas metas se declaran al cierre de ese mismo documento.

La trazabilidad completa desde el origen hasta la prueba está en
`matriz-trazabilidad-d2.md`, con la cadena problema, requisito, etapa, capacidad,
componente, verificación y criterio de aceptación. Las reglas de control que esa matriz
aplica son cuatro. Todo problema relevante tiene requisito, exclusión o supuesto
asociado. Todo requisito tiene origen, etapa, componente y método de verificación. Todo
criterio de aceptación tiene al menos un requisito. Ningún componente de arquitectura
carece de un requisito que lo justifique.

## 9. Matriz de cumplimiento técnico, Formulario T-12

El Formulario T-12 preliminar, con las cinco columnas del formato oficial y los 42
requisitos de solución, está en `formulario-t12-preliminar-d2.md`.

**Alcance declarado y su limitación.** El T-12 exige declarar el cumplimiento de cada
requerimiento de las Bases Técnicas del caso y de los requisitos transversales del
Capítulo 3 (FEP01 · Formulario T-12 · p.62). El Capítulo 3 de las Bases Técnicas
Transversales es «Modelo híbrido, nube y on premise», uno de veintinueve capítulos, lo
que resulta incompatible con el propósito de una matriz integral de cumplimiento. El
PROPONENTE consultó formalmente esta contradicción dentro del período del Artículo 43°
y el Acta de Respuestas se publica el mismo día de entrega de este informe (FEP01 ·
Formulario T-20 · p.65).

Mientras esa respuesta no exista, el PROPONENTE cubre en este informe los requisitos
del caso y los requisitos transversales que afectan alcance, arquitectura, datos e
innovaciones, e incorporará el resto de manera incremental. **Ninguna fila del T-12
declara cumplimiento en esta versión.** Todas están en verificación, porque un
compromiso de atender una exigencia y un componente propuesto no son evidencia de
cumplimiento.

## 10. Riesgos del alcance

Cinco riesgos pueden mover el alcance comprometido. Se declaran aquí y se desarrollan
en el plan de riesgos del Informe 2 (FEP01 · Formulario T-22 · p.68).

| Riesgo | Efecto sobre el alcance | Mitigación |
|---|---|---|
| Adhesión insuficiente de transportistas | Reduce la cobertura de jornada, posición y emisiones sobre el 60,4 % de la capacidad | Incentivo económico verificable y modalidad de datos sin equipo |
| Ausencia de mecanismo tributario de contingencia | Impide el documento conforme antes del movimiento en puntos sin cobertura | Gestión del CLIENTE ante la autoridad tributaria y bloqueo de salida mientras no exista |
| Interfaces del sistema de 2013 más pobres de lo supuesto | Obliga a integración por archivos y retrasa el costeo | Capa anticorrupción y levantamiento de interfaces en el mes 1 |
| Insuficiencia probatoria de la jornada declarada | Invalida la acreditación de la jornada de conductores externos | Expediente con varias fuentes y validación jurídica temprana |
| Ritmo de paso por terminal menor al promedio | Retrasa la cobertura del equipamiento a bordo | Cobertura declarada mes a mes y tratamiento específico del 22 % de baja frecuencia |

## 11. Documentos de respaldo de este subdocumento

| Documento | Contenido |
|---|---|
| `catalogo-requisitos-d2.md` | 28 requisitos funcionales y 14 no funcionales, con origen, etapa y verificación |
| `matriz-trazabilidad-d2.md` | Trazabilidad de los 42 requisitos hasta componente, prueba y brecha |
| `alcance-etapas-d2.md` | Etapas 1 y 2 con entradas, salidas, criterios de avance y exclusiones |
| `criterios-aceptacion-d2.md` | Los 29 criterios del caso con línea base, meta, hito y medición |
| `registro-decisiones-d2.md` | Las 26 decisiones del numeral 16.1 con su estado y coordinación |
| `decision-01-jornada-externa.md` | Desarrollo de la decisión 1, alternativas, recomendación y contingencias |
| `formulario-t12-preliminar-d2.md` | Matriz de cumplimiento técnico y trazabilidad, versión preliminar |
| `fichas-t19-d2.md` | Innovaciones tipo 1 y tipo 4, con los siete elementos del Artículo 29° |
