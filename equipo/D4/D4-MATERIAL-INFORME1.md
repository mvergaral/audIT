# Dupla 4 — Material para el Informe y Presentación 1

> **Estado:** material de trabajo ordenado, no redactado como informe.
> **Autores:** Ignacio V + Alonso (Dupla 4) · **Peso:** 16 % (subdoc. 4.2, Formulario T-11)
> **Fecha de corte:** 01-09-2026
> **Fuente de cada afirmación:** verificada por OCR sobre los PDF originales. Toda página
> citada es la **numeración impresa al pie**; en el lector de PDF súmese 1.

---

## 0. Reglas que gobiernan este material

### 0.1 Qué le toca a D4 y qué no

El plan de trabajo por duplas (pág. 5/9) asigna a D4 **siete entregables**:

1. Tabla de emplazamiento componente por componente, con justificación.
2. Especificación del dispositivo a bordo como componente on-premise distribuido en 374 unidades.
3. Especificación de tecnologías de software con versión, fin de soporte y plan de actualización a 56 meses.
4. Data center primario.
5. Data center secundario y recuperación ante desastres.
6. Red y enlaces, incluida la caracterización en terreno de la cobertura móvil.
7. Costo recurrente de datos móviles derivado de la frecuencia de muestreo.

Más **una** ficha de innovación: **tipo 2, Proceso**.

> ⚠️ **Discrepancia detectada entre nuestros propios documentos.** `CONTEXTO-CASO10.md`
> asigna a D4 la innovación tipo 2 y dice que la tipo 4 es de D1 y la tipo 5 de D2. El
> `Plan_Trabajo_Duplas_Informe1_Caso10.pdf` (pág. 6/9) dice tipo 4 = D2 y tipo 5 = D1.
> En lo que toca a D4 no hay conflicto (tipo 2 en ambos), pero **hay que alinear al equipo**
> antes del 04-09 o dos duplas van a escribir la misma ficha.

### 0.2 La regla de prelación caso ↔ transversales

Decisión del equipo: **prevalece el caso**. Queda anotada, y con una precisión que hay que
escribir bien porque el documento no dice exactamente eso.

El Cap. 15 del Caso (pág. 31/49) dice literalmente:

> «Cuando este capítulo endurece un umbral del documento transversal, **prevalece el más exigente**.»

No dice «prevalece el caso». Dice «prevalece el más exigente». En la práctica coinciden casi
siempre, porque el caso endurece. Pero hay al menos un punto donde **el transversal es más
exigente que el caso** y ahí la regla nos obliga al transversal. Redacción sugerida para el informe:

> «Ante discrepancia entre las Bases Técnicas Transversales y las Bases Técnicas del Caso 10,
> esta propuesta aplica el umbral más exigente, conforme al encabezado del Capítulo 15 del
> Caso (pág. 31/49). Cuando el Caso individualiza un parámetro que el documento transversal
> deja abierto, prevalece el Caso. El registro de las discrepancias detectadas se acompaña en
> el Anexo de consultas.»

### 0.3 Prohibición absoluta de cifras de precio

**Ninguna sección de este archivo destinada al Informe 1 contiene cifras en pesos.**
El Art. 50.2 de las Bases Administrativas lo sanciona con causal de exclusión. Todo el
material económico está aislado en la **§10, marcada como NO VA AL INFORME 1**, y su destino
es el Informe 3 / Sobre N.º 3.

Hay un conflicto abierto sobre esto que es consulta, no decisión nuestra: **RT-08.10**
(transversal, pág. 19/51) obliga a declarar el «costo unitario estimado» de cada dispositivo
de terreno dentro de la especificación técnica.

### 0.4 Lo que NO vamos a inventar

- **No existe inventario del parque telemático de los 226 camiones de terceros.** El caso solo
  dice que hay tres proveedores, uno contratado por la compañía y dos por los dueños, que en
  uno no se puede exportar, y que 34 camiones no tienen nada (Cap. 5, pág. 12/49). Marca,
  modelo, protocolo y almacenamiento: **desconocidos**. No se fabrican.
- **No hay medición de cobertura móvil.** Cualquier cifra de cuántas unidades necesitan capa
  satelital es supuesto hasta que se ejecute la campaña de RT-03.24.

---

### 0.5 Auditoría de cobertura de las fuentes obligatorias

El plan de trabajo (pág. 5/9) fija seis capítulos transversales como fuente obligatoria de D4.
Esta es la cobertura **antes** y **después** de la revisión del 01-09:

| Capítulo transversal | Requisitos | Antes | Ahora |
|---|---|---|---|
| Cap. 3 — Modelo híbrido y conectividad | 24 | 21 | **24** |
| Cap. 6 — Site principal on-premise | 34 | 25 | **34** |
| Cap. 7 — Site secundario y DR | 14 | 7 | **14** |
| Cap. 8 — Hardware, puestos y equipamiento de terreno | 19 | 9 | **19** |
| Cap. 9 — Desempeño, capacidad y escalabilidad | 10 | 0 | **10** |
| Cap. 10 — Disponibilidad, continuidad y resiliencia | 9 | 0 | **9** |
| **Total** | **110** | **62 (56 %)** | **110 (100 %)** |

Los caps. 9 y 10 figuraban como cubiertos porque se citaban RT-09.01 y RT-10.05, pero esos eran
los códigos **del Caso**, que según §11.1 no corresponden a los transversales homónimos. Del
documento transversal no había nada.

**D4 se trabaja como una sola unidad.** El reparto interno entre las dos personas queda sin efecto
para efectos de este documento: hay entregables —la política de respaldos, los puestos de trabajo,
los caps. 9 y 10— que no estaban asignados a nadie y que son fuente obligatoria.


---

## 1. «Debe presentar la Empresa» — aporte de D4

D1 escribe este capítulo. D4 aporta **dos insumos** y nada más:

- **Capacidad instalada en infraestructura y terreno.** Que el proponente acredite experiencia
  en telemática de flotas y en operación desconectada prolongada no es autoelogio: **RT-15.02**
  del Caso (pág. 33/49) lo exige como certificación sectorial del adjudicatario, junto con
  «conocimiento acreditado del régimen especial de jornada del conductor de carga y del
  reglamento de transporte de sustancias peligrosas».
- **Modelo de soporte de terreno.** Cinco terminales entre Antofagasta y Puerto Montt, más de
  2.500 km entre extremos, e intervención sobre camiones en ruta cuya llegada a terminal no es
  programable (**RT-21.16**, pág. 34/49). Esto condiciona la estructura de la empresa que se
  presenta en el subdoc. 1.

---

## 2. «Debe presentar el Problema» — aporte de D4

D1 escribe. D4 aporta la **lectura física del problema**, que es distinta de la lectura de
negocio y es lo que justifica luego nuestras decisiones:

**El problema de D4 en una frase: la unidad productiva de esta empresa está en movimiento,
desconectada buena parte del tiempo, y el 60 % de ella no le pertenece.**

Tres hechos físicos que gobiernan todo el diseño, del Cap. 3 del Caso (pág. 8/49):

| Nodo | Lo que el caso dice | Consecuencia física |
|---|---|---|
| Terminal San Bernardo | Casa matriz, torre 24×7, taller principal, estanque | «Único punto donde converge todo. Es donde se instala y se mantiene cualquier equipamiento a bordo» |
| 4 terminales regionales | Antofagasta, Talca, Los Ángeles, Puerto Montt | «Enlace propio de un proveedor, **sin respaldo en tres de los cuatro**» |
| La ruta | 3.000 km, tramos de **más de 80 km continuos sin cobertura** en el norte y la cordillera | «Es donde ocurre el 100 % del riesgo y donde la empresa tiene la menor visibilidad» |

Y el dato que define el ritmo de cualquier despliegue: **un camión pasa por un terminal cada 6
días en promedio, y el 22 % de la flota subcontratada pasa menos de una vez al mes**
(Cap. 6, pág. 14/49).

---

## 3. «Debe presentar el Esquema de Solución» — aporte de D4

D2 escribe. D4 aporta **la capa física del esquema**: dónde vive cada cosa y por qué.

**Principio rector propuesto, en una frase para la lámina:**

> El registro operacional de esta empresa no vive en un servidor: vive en 374 camiones, y la
> nube es donde se consolida. El borde no es una víctima de la caída del enlace, es parte del
> esquema de continuidad.

Ese enunciado no es retórica: **RT-06.01 del Caso (pág. 32/49) lo ordena literalmente**:

> «el dispositivo a bordo debe tratarse como un **componente on-premise distribuido en 374
> unidades**, con su propio ciclo de vida, su mecanismo de actualización remota, su gestión de
> seguridad y su plan de reposición, todo ello sujeto a la restricción de que sólo puede
> intervenirse físicamente cuando el camión pasa por un terminal.»

**Cumplimiento del Artículo 16° (híbrido obligatorio):** la propuesta es híbrida por
construcción y en tres planos simultáneos, no por conveniencia:

| Plano | Qué contiene | Por qué no puede estar en otro lado |
|---|---|---|
| Nube | Núcleo transaccional, analítica, portales, integración | Elasticidad para 430 camiones en 3 años (RT-02.12) y para el peak de reconexión masiva |
| On-premise de sitio | Continuidad de la torre 24×7 y terminación de enlaces en San Bernardo; gabinetes en 4 terminales regionales | RT-06.01 del Caso exige gabinete en cada terminal regional dimensionado para RT-03.10 |
| On-premise distribuido | 374 dispositivos a bordo | La operación no puede depender de la cobertura móvil (restricción 4) |

---

## 4. «Debe presentar el Alcance de la Solución» — aporte de D4

D2 escribe. D4 aporta **los límites físicos del alcance**, que son los que más se prestan a
que nos acusen de prometer lo que no podemos:

### 4.1 Tres poblaciones de camiones, tres tratamientos distintos

| Población | Unidades | Qué se hace | Fundamento |
|---|---|---|---|
| Flota propia | 148 | Especificación completa y despliegue directo | Son de la compañía |
| Terceros **con** dispositivo | ~192 | **No se reemplaza nada.** Estándar mínimo de homologación + unificación de la vista | Restricción 3 (pág. 23/49) + Cap. 11 (pág. 24/49) |
| Terceros **sin** dispositivo | 34 | Únicos candidatos a equipo nuevo, y **solo por adhesión** | Cap. 5 (pág. 12/49) |

El Cap. 11 del Caso (pág. 24/49) define exactamente el entregable para la población del medio:

> «No se pide reemplazar las plataformas de posicionamiento satelital instaladas en camiones de
> terceros, aunque **sí unificar la vista y especificar qué se requeriría si hubiera que
> homologarlas**.»

→ El entregable no es un inventario (que no tenemos) sino un **estándar mínimo de homologación**
contra el cual clasificar después cada equipo en cumple / no cumple / desconocido:
almacenamiento local de 72 h, sincronización diferida, formato de evento, identificación del
conductor, sello de tiempo con garantía de integridad. El levantamiento del parque es
**actividad de Etapa 1**, con costo, plazo y dependencia de terceros.

### 4.2 Lo que está fuera del alcance físico y hay que decir en voz alta

- No se instala equipamiento en puntos de carga y descarga de clientes (Cap. 11, pág. 24/49;
  restricción 9).
- No se interviene la electrónica de fábrica del vehículo (Cap. 11, pág. 24/49).
- El hardware **lo compra el CLIENTE**; nosotros especificamos qué comprar, cuánto y con qué
  características (Cap. 11, pág. 24/49).
- No se promete visibilidad total: 34 camiones no tienen nada y ~192 tienen equipos que no
  podemos tocar.

---

## 5. «Arquitectura Física» — el núcleo de D4 (16 %)

### 5.0 Advertencia de dependencia

**La tabla de emplazamiento (§5.2) no se puede cerrar hasta que D3 entregue el inventario de
componentes lógicos.** Sincronización S4, viernes 04-09. Todo lo demás de esta sección es
independiente de D3 y se puede escribir ya.

El Art. 16.2 califica como **observación grave** emplazar un componente sin justificar, y el
numeral 1.5 advierte que declarar «cumple» sin individualizar el componente «equivale a no
declarar». La tabla se llena componente por componente o no sirve.

---

### 5.1 Los nodos físicos del caso

```
                     ┌──────────────────────────────────────────┐
                     │   NUBE — Azure Chile Central (Santiago)  │
                     │   3 zonas de disponibilidad · GA 2025    │
                     │   Núcleo transaccional · Analítica       │
                     │   Portales · Integración · IoT Hub       │
                     └───────────────┬──────────────────────────┘
                                     │  ExpressRoute + VPN de respaldo
                                     │  (rutas físicas y proveedores distintos)
              ┌──────────────────────┴───────────────────────┐
              │                                              │
   ┌──────────▼───────────┐                    ┌─────────────▼─────────────┐
   │  SAN BERNARDO        │                    │  4 TERMINALES REGIONALES  │
   │  Sala técnica de     │                    │  Antofagasta · Talca ·    │
   │  sitio (26 m²)       │                    │  Los Ángeles · Pto Montt  │
   │  · Continuidad torre │                    │  Tipología: GABINETE      │
   │  · Terminación red   │                    │  · Cómputo local 12 h     │
   │  · Custodia medios   │                    │  · Enlace + respaldo      │
   └──────────┬───────────┘                    └─────────────┬─────────────┘
              │                                              │
              └──────────────────┬───────────────────────────┘
                                 │
              ┌──────────────────▼──────────────────────────┐
              │   ON-PREMISE DISTRIBUIDO — 374 CAMIONES     │
              │   (RT-06.01 del Caso, pág. 32/49)           │
              │   Cada uno: buffer 72 h + celular + [SBD]   │
              └─────────────────────────────────────────────┘

   Nodos donde NO se instala nada (restricción 9 / Cap. 11):
   · Puntos de carga y descarga de clientes  · Plazas de pesaje
   · Talleres externos en ruta               · Paso Los Libertadores
```

---

### 5.2 Tabla de emplazamiento — plantilla y criterios

**Bloqueada hasta S4.** Lo que sí está cerrado son las **columnas** y los **criterios**, que es
lo que el Art. 16.2 exige justificar. Estructura obligatoria:

| Componente | Emplazamiento | Latencia | Criticidad | Volumen | Regulación | Conectividad | TCO | Justificación |
|---|---|---|---|---|---|---|---|---|

Reglas de decisión propuestas, para que D3 pueda pre-clasificar sin nosotros:

| Si el componente… | Va a… | Fundamento |
|---|---|---|
| debe responder con el camión en ruta y sin enlace | Dispositivo a bordo | Restricción 4 · RT-03.10 |
| debe permitir asignar viaje, emitir DET o recibir pánico con la nube caída | San Bernardo | RT-21.06: severidad máxima |
| maneja datos personales de los 258 conductores externos | Nube, con cifrado a nivel de campo | RT-11.10 |
| es serie temporal de posición o telemetría | Nube, con política de agregación declarada | RT-05.10 del Caso: 2 años en línea |
| es evidencia de jornada o documento probatorio | Nube, con almacenamiento inmutable | RT-05.10 del Caso: 5–10 años · RT-07.11 |
| tiene perfil de carga variable | Nube, cómputo elástico | RT-03.09 |

---

### 5.3 Dispositivo a bordo — especificación T-11

#### 5.3.1 No es un dispositivo: son tres funciones

| Función | Qué hace | Por qué es obligatoria |
|---|---|---|
| **A. Unidad telemática** | GNSS, buffer no volátil, CAN/FMS, evaluación local de geocercas, cálculo local de jornada | RT-03.10, RT-06.01 del Caso |
| **B. Módulo satelital SBD** | Posición y eventos críticos fuera de cobertura celular | Restricción 4 · solo subconjunto por riesgo |
| **C. Identificación del conductor** | Atribuye el viaje a una persona **sin acción del conductor** | RT-12.11 |

**Son al menos dos piezas físicas por camión en la población satelital**, con impacto en tiempo
de instalación, arnés, y en el stock de repuestos del 10 % que exige el numeral 8.4 (pág. 20/51).

#### 5.3.2 El cálculo de las 72 h — respuesta al Cap. 14.2

El Cap. 14.2 del Caso (pág. 30/49) marca como **«a estimar y declarar como supuesto»** el
«volumen que debe almacenar el dispositivo a bordo durante 72 horas sin cobertura», y advierte:
«valores sin derivación, se evaluará como dimensionamiento no realizado».

**Supuestos de la derivación (declararlos todos):**

| Supuesto | Valor | Origen |
|---|---|---|
| Km por camión al año | 41.000.000 ÷ 374 ≈ 109.600 | Cap. 14.1, pág. 29/49 |
| Velocidad comercial media | 55 km/h | Supuesto D4 |
| Horas de marcha en 72 h calendario | ≈ 30 h | Art. 25 bis Código del Trabajo: descansos obligatorios |
| Registro de posición | 64 B | Supuesto D4: timestamp, lat, lon, alt, velocidad, rumbo, satélites, HDOP, estado E/S |
| Muestra de telemetría FMS/CAN | 160 B | Supuesto D4 |
| Evento discreto | 80 B | Supuesto D4 |
| DET en XML firmado | 40 KB | Supuesto D4 |
| Conformidad de entrega con firma gráfica | 30 KB | Supuesto D4 |
| Fotografía de evidencia comprimida | 300 KB | Supuesto D4 |

**Resultado, tres escenarios de muestreo:**

| Concepto | A: 10 s en marcha | **B: 30 s (recomendado)** | C: 60 s |
|---|---|---|---|
| Posición | 723 KB | 263 KB | 147 KB |
| Telemetría FMS 1/min | 288 KB | 288 KB | 288 KB |
| Eventos discretos | 32 KB | 32 KB | 32 KB |
| Documentos del viaje (≈3 viajes) | 195 KB | 195 KB | 195 KB |
| **Subtotal sin imágenes** | **≈ 1,3 MB** | **≈ 0,8 MB** | **≈ 0,7 MB** |
| Con 8 fotos de evidencia | ≈ 3,7 MB | ≈ 3,2 MB | ≈ 3,1 MB |
| **Con factor ×3** (formato, índices, journaling, cola de reintento) y margen RT-08.05 | **≈ 11 MB** | **≈ 10 MB** | **≈ 9 MB** |

#### 5.3.3 La conclusión que cambia la especificación

**No basta con dimensionar para 72 h.** RT-10.05 del Caso (pág. 32/49) declara que los cierres
del paso fronterizo por nieve son **de hasta 12 días continuos** y «deben absorberse sin
desplazar hitos». Un camión detenido 12 días en zona cordillerana sin cobertura sigue obligado
a no perder ningún registro.

→ **Exigencia de pliego propuesta: almacenamiento no volátil ≥ 8 GB**, no «suficiente para 72 h».
El sobrecosto de pasar de 16 MB a 8 GB es marginal y elimina toda una clase de riesgo.

> ⚠️ **Esto descarta el LINK 740 como unidad telemática**, y hay que decirlo con datos:
>
> | Especificación | LINK 740 (verificado en webfleet.com) | Lo que el caso exige |
> |---|---|---|
> | Memoria interna / buffer | **No publicada** | 72 h sin pérdida (RT-03.10) |
> | Protección de ingreso | **IP20** | «polvo» nombrado explícitamente (Cap. 6, pág. 14/49); RT-08.12 |
> | Temperatura de operación | **−30 a +70 °C** | «temperatura extrema en el norte» (Cap. 6, pág. 14/49) |
> | Módem | **LTE-M y GPRS** | RT-03.15 del Caso: sincronizar 72 h de datos en ≤20 min |
>
> El Iridium Edge sí cumple (−40/+85 °C, IP67), pero **el conjunto vale lo que vale su
> componente más débil**, y ese es el LINK. `BLOQUE2-INVESTIGACION-TECNICA.md` afirmaba que el
> rango térmico «cubre sin problema las condiciones del norte»: eso es cierto del Edge y falso
> del conjunto. **Corregir esa línea.**

#### 5.3.4 La brecha del producto, verificada en la ficha que nos pasaron

Ficha `wf-wfsat-datasheet.cl.pdf`, sección ALMACENAMIENTO DE DATOS, textual:

> «Cuando se transita en áreas de red remotas, los datos se almacenan por hasta **40 horas**
> mientras se conduce.»

**40 < 72.** Incumplimiento directo y verificable de RT-03.10.

Dos hallazgos más de la misma ficha que nadie había levantado:

1. **La conmutación a satélite tarda 10 minutos.** «Después de un período de 10 minutos sin red
   móvil, cambia a comunicación satelital.» En una sombra corta el camión queda ciego 10 min.
2. **En modo satelital la posición llega a la plataforma cada 10 minutos.** Nota al pie 3:
   «Intervalos de posición cada minuto. Actualización de la última posición **cada 10 minutos**
   en WEBFLEET.» → **Esto es incompatible con un botón de emergencia útil fuera de cobertura.**

#### 5.3.5 Sobre el botón de emergencia

Dijiste que el aparato de Webfleet SAT trae botón de emergencia. **No aparece en la ficha que
enviaste.** La ficha describe seguimiento satelital, geocercas, red Iridium, almacenamiento y
diseño resistente. No menciona botón de pánico. En la familia LINK el botón se implementa sobre
las entradas del conector de E/S o mediante un terminal de conductor, no viene integrado.

Y hay un conflicto físico que hay que verificar con el proveedor: la propia ficha dice que
**el Iridium Edge ocupa el conector de entrada/salida múltiple del LINK 7XX** a través del cable
adaptador. Si el botón de pánico y el lector de identificación del conductor también necesitan
ese conector, hay competencia por el mismo recurso. → **verificación con el fabricante**.

**Cómo se escribe el umbral sin contradecirse.** RT-09.01 del Caso (pág. 32/49) exige
transmisión del pánico a la torre en «no superior a 15 segundos **con cobertura**». El requisito
ya se limita él mismo. No hay contradicción con Iridium: hay un hueco que debemos llenar
declarando y fundamentando un umbral propio para el modo satelital.

> **Corrección a `BLOQUE2-INVESTIGACION-TECNICA.md` §5.5:** planteaba esto como inconsistencia
> a resolver. No lo es. Es un parámetro que el caso deja abierto y que nosotros declaramos.

#### 5.3.6 Alternativa recomendada y ADR

RT-02.04 (pág. 7/51) hace del registro de decisiones de arquitectura un **entregable
contractual**, con alternativa escogida, descartadas y criterio. Mínimo dos alternativas.

| Criterio (todos con fuente) | Peso |
|---|---|
| Almacenamiento no volátil ≥ 8 GB | Eliminatorio — RT-03.10 + RT-10.05 |
| IP y rango térmico coherentes con cabina polvorienta del norte | Eliminatorio — RT-08.11, RT-08.12 |
| Gestión remota: inventario, configuración, **firmware**, bloqueo y borrado | Eliminatorio — RT-03.18 |
| Modo de privacidad implementado **en firmware** | Eliminatorio — criterio 29, RT-16.30 |
| CAN/FMS + descarga remota de tacógrafo | Alto — decisiones 12 y 13 |
| Instalación que no afecte la garantía del vehículo | Eliminatorio — restricción 6 |
| Disponibilidad de repuestos y ciclo de vida ≥ 56 meses | Alto — RT-08.13 |

**Candidato A — Teltonika FMC650 + Iridium Edge.** Lo verificado:
- 4G LTE Cat 1, doble SIM o eSIM.
- **16 MB de flash interna + ranura microSD hasta 32 GB.** La flash sola no basta (Teltonika
  documenta que alcanza para «hasta 6 horas» de registros); **la microSD es la que cumple las 72 h
  y los 12 días**. Esto va explícito en el pliego: no «tiene memoria», sino «≥8 GB no volátil».
- Interfaces: 2× RS232, 1× RS485, CAN J1939, CAN J1708, 1-Wire, BLE 5.0.
- Alimentación 8–32 V DC con protección de sobretensión y polaridad inversa; batería de respaldo
  Ni-MH 550 mAh.
- **Descarga remota de tacógrafo**: DDD, y también TGD español y V1B/C1B franceses; soporta
  Smart Tachograph v2. Se conecta al conector C del tacógrafo (C5 = CAN2H, C7 = CAN2L) cuando la
  señal RDD no está disponible por FMS.

> ⚠️ **Verificar antes de citarlo en el informe:** al consultar el catálogo de Teltonika la ficha
> del FMC650 aparece marcada como *End of life* y *Out of stock*, mientras que su wiki registra
> actualizaciones de la guía de instalación en mayo de 2026. Los datos se contradicen.
> **RT-08.13 obliga a declarar ciclo de vida y disponibilidad de repuestos por 56 meses**:
> proponer un producto en fin de vida es un defecto de la propuesta. Confirmar con el
> distribuidor y, si procede, mover la especificación al sucesor de la familia.

**Candidato B — Webfleet LINK 740 + Iridium Edge (la línea que traías).** Se documenta en el ADR
como alternativa evaluada y **descartada por especificación**, con las cuatro brechas de §5.3.3
y las 40 h de §5.3.4. Descartarla con datos vale más que no haberla mirado.

**Candidato C — Queclink / CalAmp / Geotab GO + IOX satelital.** Comparar contra la misma tabla.

**Y la regla que no se puede romper:** cualquiera que se elija, **Webfleet u otra plataforma SaaS
entra como fuente de datos por API, nunca como arquitectura.** El Cap. 11 (pág. 24/49) dice que el
hardware lo compra el CLIENTE y que nosotros especificamos qué comprar. Si el diagrama de
despliegue tiene un producto comercial al centro, el Cap. 19 lo lee como no haber entendido el encargo.

---

### 5.4 Conectividad: la arquitectura por capas

**Redacción corregida del planteamiento, para que no incumpla nada.** El error a evitar es
presentar el satélite como si redujera la exigencia de almacenamiento. No la reduce.

> **Capa 0 — todas las unidades intervenidas: almacenamiento local.**
> RT-03.10 exige 72 horas continuas **sin cobertura móvil** registrando posición, eventos de
> conducción y jornada, tiempos en puntos de carga y descarga y documentos del viaje, sin pérdida
> de ningún registro. La disponibilidad de enlace satelital **no releva de este requisito**, por
> dos razones independientes: el requisito está escrito sobre la cobertura móvil, y el enlace de
> ráfaga corta no puede transportar documentos ni evidencia detallada. El almacenamiento local es
> la base de cumplimiento; el satélite es una capa de visibilidad, no de registro.
>
> **Capa 1 — todas las unidades intervenidas: celular como portador primario**, a tasa completa,
> con sincronización diferida y reconciliación determinista al recuperar enlace (RT-03.12).
>
> **Capa 2 — subconjunto acotado por riesgo: satelital de ráfaga corta.** Posición a tasa
> reducida, eventos críticos y botón de emergencia. La población se determina con la campaña de
> medición de RT-03.24; hasta entonces se declara como supuesto.
>
> **Descartada: banda ancha satelital de órbita baja para toda la flota.** La carga útil es de
> kilobytes por minuto, no megabits; el servicio cobra ancho de banda que no se usa, consume
> energía del vehículo y monta una antena sobre la cabina, lo que roza la restricción 6.
> Se documenta en el ADR (RT-02.04).

> ⚠️ **Incoherencia interna a corregir en `CONTEXTO-CASO10.md` §6.2.** Ese archivo dice
> «Capa 0 — **todas las unidades**». No puede ser «todas»: los ~192 equipos de terceros no se
> pueden intervenir (restricción 3, pág. 23/49). El texto correcto es **«todas las unidades
> intervenidas»**, y para el resto rige el estándar de homologación de §4.1. Si RT-03.10 se lee
> como exigible sobre las 374, es incumplible por diseño en el 51 % de la flota. → **consulta**.

**Corolario para el criterio 28:** la alerta de jornada **se calcula en el dispositivo** y no
necesita conectividad. Lo que necesita es saber dónde están los lugares seguros de detención,
dato que hoy nadie tiene. Ese catálogo georreferenciado es un entregable de Etapa 1 y es lo que
convierte el criterio 28 en algo verificable.

---

### 5.5 Datos móviles: respuesta a la decisión 11

La decisión 11 (pág. 35/49) dice que la frecuencia de muestreo «determina el costo mensual de
datos móviles de toda la flota, que es recurrente en una empresa con 9 % de margen».

**Base mensual por camión:** 9.135 km/mes ÷ 55 km/h ≈ **166 h de marcha**, 564 h detenido.
21,4 viajes/mes. 28,5 DET/mes (128.000 DET/año ÷ 374 ÷ 12).

| Componente | A: 10 s | **B: 30 s + 5 min detenido** | C: 60 s |
|---|---|---|---|
| Posición | 4,26 MB | 1,71 MB | 1,07 MB |
| Telemetría FMS 1/min en marcha | 1,59 MB | 1,59 MB | 1,59 MB |
| Eventos discretos | 0,24 MB | 0,24 MB | 0,24 MB |
| Documentos del viaje | 1,80 MB | 1,80 MB | 1,80 MB |
| **Carga útil** | **7,9 MB** | **5,3 MB** | **4,7 MB** |
| Con overhead ×2,5–3 (TCP/TLS, framing, reintentos) | **20–24 MB** | **13–16 MB** | **12–14 MB** |
| Si se transmite evidencia fotográfica (≈4 fotos/viaje) | +25 MB | +25 MB | +25 MB |

**Flota completa, escenario B sin fotografía:** 374 × ~15 MB ≈ **5,6 GB/mes**.

#### El hallazgo que hay que escribir

**El costo de datos móviles de esta flota es marginal; lo que pesa es el cargo fijo por SIM y por
suscripción de plataforma por vehículo, que se factura por unidad y no por byte.** 5,6 GB/mes
para 374 vehículos es un volumen trivial para cualquier plan M2M. La palanca económica de la
decisión 11 no está en la frecuencia de muestreo sino en el modelo de tarificación del
proveedor y en cuántas unidades se suscriben.

Eso reordena la recomendación:

1. **Muestreo adaptativo, no fijo.** 10 s en maniobra, geocerca y evento; 30 s en ruta estable;
   5 min detenido. Da resolución donde importa al costo del escenario C.
2. **La evidencia fotográfica multiplica por tres el consumo.** Debe transmitirse diferida,
   comprimida y solo al llegar a cobertura o a terminal. Decisión conjunta con D3.
3. **Negociar por parque, no por unidad**, y declarar el supuesto de tarificación.

#### Volumetría satelital

Un mensaje SBD transporta hasta 340 B; un reporte de posición comprimido ocupa 30–50 B. A una
posición por minuto, un camión que pase 40 h/mes en sombra genera ≈ 2.400 mensajes/mes
(≈120 KB). **Trivial en bytes, caro en mensajes**, porque SBD se tarifica por mensaje y por
paquete mensual.

→ **Palanca:** una posición cada 5 min en sombra (≈480 mensajes/mes, reducción de 5×) más
eventos críticos inmediatos: pánico, entrada y salida de geocerca, cruce de frontera, apertura
no autorizada. La trazabilidad fina queda en el buffer local y se vuelca por celular.

---

### 5.6 Tacógrafo digital — tu propuesta, con las correcciones

**Tu idea:** acordar con los dueños de camión que, si no tienen tacógrafo digital, se compre uno
cumpliendo toda la regulación.

**Es una buena idea y tiene tres problemas que hay que resolver antes de escribirla.**

#### Problema 1 — el supuesto de partida es falso

| Lo que se venía asumiendo | Lo que dice el documento |
|---|---|
| «Todos los camiones tienen tacógrafo» | Pág. 9/49, en el párrafo de los **196 conductores propios**: «Los camiones **nuevos** tienen tacógrafo digital». De los 226 de terceros el caso no afirma nada |
| «Están todos bien» | Tabla 7.1, pág. 14/49: «Tacógrafos digitales cuya información se descarga: **0**» |

El Cap. A del Caso lo remata: «Tacógrafo digital — Responsable: **Nadie** — El equipo lo genera;
**nunca se descarga**».

#### Problema 2 — comprar un tacógrafo para un camión ajeno choca con las mismas restricciones

Un tacógrafo es un dispositivo del vehículo. Le aplican:

- **Restricción 3** (pág. 23/49): los dispositivos instalados en camiones de terceros pertenecen
  a sus dueños; no pueden intervenirse, reconfigurarse ni reemplazarse sin acuerdo expreso.
- **Restricción 6** (pág. 23/49): ningún equipamiento a bordo puede afectar la garantía del
  vehículo ni interferir con sus sistemas de seguridad.
- **Restricción 5**: solo se instala cuando el camión pasa por un terminal.

→ **No es un programa aparte: es exactamente el mismo problema de adhesión que el dispositivo a
bordo, y debe viajar en el mismo plan.** Es la **decisión 5** (pág. 34/49): de quién es el
dispositivo, quién lo paga, quién lo administra y qué pasa con él si el transportista deja de
trabajar con la compañía. Presentarlo como dos negociaciones separadas con los mismos 148 dueños
es duplicar el punto de fricción. **Una sola conversación, un solo contrato, un solo incentivo.**

#### Problema 3 — el tacógrafo por sí solo no resuelve la jornada

El tacógrafo chileno **registra la conducción del vehículo, no la de la persona**. No es el
tacógrafo europeo con tarjeta de conductor. Sin identificación en cabina, el dato no se atribuye
a nadie — que es justamente lo que **RT-12.11** (pág. 32/49) obliga a resolver «sin exigir
manipulación de un dispositivo con el vehículo en movimiento y sin depender de que el conductor
recuerde una credencial».

→ **Tacógrafo + identificación del conductor**, o el gasto no compra acreditación.

#### Qué sí hay que especificar

**Hardware y mecanismo de descarga (decisión 13, pág. 35/49: quién descarga, con qué frecuencia,
dónde se conserva y con qué garantía de integridad):**

| Elemento | Especificación | Fundamento |
|---|---|---|
| Descarga | **Remota, desde la central**, sin intervención del conductor | Decisión 13 · restricción 1 |
| Vía | Unidad telemática con interfaz de tacógrafo; conexión por FMS o directo al conector C (C5 = CAN2H, C7 = CAN2L) | Verificado en documentación Teltonika |
| Formatos | DDD, y compatibilidad con TGD y V1B/C1B | Verificado |
| Tarjeta de empresa | Lectora en la central con la tarjeta de empresa: **es el elemento que autoriza la descarga remota** | Requisito funcional del mecanismo |
| Periodicidad | Declarar la política. La práctica europea es 28 días conductor / 90 días vehículo | A confirmar contra normativa chilena |
| Conservación | Mínimo 5 años | RT-05.10 del Caso, pág. 31/49 |
| Integridad | Sello de tiempo y almacenamiento inmutable | RT-07.11 · criterio 4 · decisión 24 |
| Estándares | Identificar por denominación y verificar con cada proveedor y fabricante qué es accesible | **RT-05.23 del Caso, pág. 32/49** |

**Marco normativo chileno — orientación, con verificación pendiente.** Búsqueda web indica que el
Decreto N.º 80 de 2004 exige dispositivo de registro en vehículos de servicios interurbanos, y
que desde el 1 de abril de 1995 los vehículos de carga con motor sobre 360 HP-SAE deben estar
dotados de tacógrafo. **No lo verifiqué en fuente oficial y no debe citarse en el informe hasta
confirmarlo en la Biblioteca del Congreso o el MTT.** Lo que sí está verificado en fuentes de la
Dirección del Trabajo es el régimen del **Art. 25 bis del Código del Trabajo** (180 h mensuales,
no distribuibles en menos de 21 días, descansos y esperas no imputables a jornada) y la
**Res. Ex. N.º 1213 de 08-10-2009**, que establece la libreta foliada, timbrada y registrada en
la Inspección del Trabajo, de confección y costo del empleador.

**Y la consecuencia legal que ordena todo:** para los 258 conductores externos **el empleador es
el transportista, no Curimón**. La libreta es del transportista. Eso no es un obstáculo: es el
mejor anclaje jurídico de nuestra postura, porque confirma que la obligación se persigue por el
**contrato con el dueño del camión**, que es exactamente lo que la restricción 2 permite.

**Retención — matiz que corrige el planteamiento «conservar solo cuando el viaje es nuestro»:**
RT-05.10 del Caso (pág. 31/49) fija el registro de jornada y su evidencia en **mínimo 5 años** y
no distingue propio de tercero, porque la acreditación se exige por viaje. Lo que sí se limita es
el **alcance**: se conserva la jornada del viaje que Curimón despachó, no la actividad del
conductor para otras empresas. Esa es la minimización que se declara y se defiende.

---

### 5.7 Telemetría de fábrica — qué es y qué hacemos con ella

**En una frase: el camión moderno ya trae de fábrica su propia unidad telemática, que envía datos
a la nube del fabricante. No hay que instalar nada — hay que pedir acceso.**

Los seis fabricantes europeos —Volvo, Scania, Mercedes-Benz, MAN, DAF e Iveco— crearon el
estándar **FMS** en 2002. Su versión remota es **rFMS** (*remote Fleet Management System*): una
API REST sobre HTTPS que expone los datos del vehículo de forma estandarizada, con métodos *pull*
y *push*. Especificación vigente **v5.0.0, julio de 2025**, publicada en `fms-standard.com`.

**En este caso son 61 tractocamiones propios.** El Cap. 5 (pág. 12/49) dice que generan
«kilometraje, consumo, códigos de falla y conducción» y que hoy **nadie los descarga**. Es la
**decisión 12** (pág. 35/49):

> «El dato existe, **es gratuito** y permitiría mantenimiento por condición, consumo real y
> hábitos de conducción. Su acceso depende de cada fabricante.»

**Las tres reglas que lo acotan:**

1. **RT-17.06** del Caso (pág. 34/49) lo lista entre los periféricos a integrar, «como
   **integración de solo lectura** sujeta a la autorización de cada fabricante».
2. El Cap. 11 (pág. 24/49) excluye expresamente intervenir los sistemas del vehículo o modificar
   su electrónica de fábrica.
3. El contrato y la suscripción son **específicos de cada OEM**: hay que negociar marca por marca.
   Es lo que el Cap. 5 quiere decir con «su factibilidad debe verificarse con cada fabricante».

**Por qué importa específicamente a D4 — y este es el argumento diferenciador:**

> Es la **única capacidad de terreno que no consume la restricción 5**. No hay hardware que
> comprar, no hay instalación, no hay que esperar a que el camión pase por un terminal cada 6
> días. Entra en producción sin tocar un solo vehículo, y da resultados desde la Etapa 1
> mientras el despliegue físico avanza a su propio ritmo.

Hoy el mantenimiento preventivo se gatilla con un odómetro leído a mano cuando el camión pasa por
el taller. Con rFMS pasa a gatillarse por condición y consumo real.

**Qué hay que verificar y declarar:** qué versión de rFMS soporta cada marca presente en la flota;
si el modelo y año de cada tractocamión expone el servicio; y bajo qué contrato y suscripción por
OEM. Crece a ≈110 tractocamiones en 3 años (Cap. 14.1, pág. 29/49).

---

### 5.8 Data center primario — nube

#### 5.8.1 La región y por qué cumple

**Azure Chile Central**, Santiago (comuna de Quilicura). Generalmente disponible desde 2025, con
**tres zonas de disponibilidad** y residencia de datos en Chile.

| Requisito | Texto | Cómo se cumple |
|---|---|---|
| RT-03.01 (pág. 8/51) | Zona en Chile o en Sudamérica | Chile Central, Santiago |
| RT-03.02 (pág. 8/51) | «al menos dos zonas de disponibilidad. **No se aceptará un diseño en una sola zona**» | 3 AZ disponibles; todo componente crítico zone-redundant |
| RT-11.10 (pág. 32/49) | Cifrado a nivel de campo para datos de los 258 conductores y localización asociada a persona identificable | Residencia en Chile + cifrado aplicativo con claves en HSM administrado |

#### 5.8.2 Mapa de servicios por función

| Función | Servicio Azure | Requisito que satisface |
|---|---|---|
| Ingesta de telemetría de 374 dispositivos | **Azure IoT Hub** + Device Provisioning Service | RT-03.18 |
| **Gestión del parque distribuido**: inventario, configuración, firmware, bloqueo y borrado remoto | **IoT Hub Device Twins + Device Update for IoT Hub** | **RT-03.18** — es la respuesta literal al requisito |
| Absorción del peak de reconexión masiva | **Azure Event Hubs**, particionado | Cap. 14.2: «trescientos camiones recuperan cobertura al mismo tiempo» |
| Cómputo de servicios de negocio | **AKS** zone-redundant, servicios sin estado | RT-03.02, RT-02.05 |
| Base transaccional | **Azure Database for PostgreSQL Flexible Server**, HA zone-redundant | RT-08.02, RT-07.03 |
| Series de posición y telemetría | **Azure Data Explorer** con política de agregación declarada | RT-05.10 del Caso: 2 años en línea + agregación |
| Documentos, evidencia de jornada, conformidades | **Blob Storage con immutable storage / legal hold** | RT-05.10 del Caso (5–10 años) · **RT-07.11** copias inmutables |
| Gestión de claves | **Key Vault Managed HSM**, clave independiente de la infraestructura respaldada | RT-07.10, RT-11.10 |
| Identidad interna / externa | **Microsoft Entra ID** + Entra External ID para 84 clientes y 148 transportistas | RT-12.11, RT-12.12 |
| API y contratos | **API Management** con OpenAPI 3.1, OAuth 2.1 | RT-05.16, RT-05.18 |
| Gobierno del borde y de los gabinetes | **Azure Arc** | RT-03.16: observabilidad unificada nube + on-premise |
| Observabilidad | **Azure Monitor + Log Analytics + Managed Grafana** | RT-03.16, RT-06.14, RT-06.19 |
| Infraestructura como código | **Bicep o Terraform**, versionado en el repositorio del CLIENTE | **RT-03.03: «No se admite infraestructura creada manualmente por consola»** |
| FinOps | **Cost Management**, etiquetado por ambiente/módulo/centro de costo, presupuestos con alertas, reporte mensual | RT-03.06 |
| Enlace privado a San Bernardo | **ExpressRoute** + VPN S2S de respaldo, proveedores y caminos distintos | RT-03.17, RT-03.21 |
| Recuperación ante desastres | **Segunda región Azure** + Site Recovery + replicación geo | Cap. 7, RT-07.02, RT-07.04 |

#### 5.8.3 Reversibilidad — no olvidarlo

**RT-03.07** (pág. 8/51) obliga a declarar la estrategia de reversibilidad y mitigación del
bloqueo por proveedor, «identificando qué componentes son portables, cuáles no lo son y cuál
sería el esfuerzo estimado de una migración». Proponer Azure sin esta declaración es una brecha.
Contenedores y PostgreSQL son portables; IoT Hub, Event Hubs y Data Explorer no lo son sin
reescritura. **Hay que decirlo.**

---

### 5.9 Data center secundario — aquí hay que corregir el plan

#### 5.9.1 El problema con «San Bernardo como respaldo de Azure»

**RT-07.02** (pág. 17/51):

> «El sitio secundario estará emplazado a una **distancia suficiente del principal para no verse
> afectado por el mismo evento de fuerza mayor**. El PROPONENTE declarará la distancia y el
> análisis de amenazas comunes considerado.»

Azure Chile Central está en Quilicura. San Bernardo está a ~20 km, en la misma Región
Metropolitana: **misma cuenca sísmica, mismo sistema eléctrico regional, mismo evento de fuerza
mayor**. Como par de recuperación ante desastres **no pasa RT-07.02**, y el evaluador lo va a ver
en la primera lectura.

Además, Cap. 7 exige que el secundario tenga «características tecnológicas **equivalentes a las
del sitio principal** en lo que respecta a los servicios críticos». Una sala de 26 m² no es
equivalente a una región de nube con tres zonas.

#### 5.9.2 La corrección: dos ejes, no uno

**No hay un único par primario/secundario. Hay dos funciones distintas que se estaban mezclando:**

| Eje | Primario | Secundario | Cumple |
|---|---|---|---|
| **Recuperación ante desastres** | Azure Chile Central, multi-AZ | **Segunda región Azure** (par declarado por Microsoft), activo-pasivo con replicación continua | RT-07.01 a RT-07.08 · RTO ≤ 4 h · RPO ≤ 15 min |
| **Continuidad operacional en el borde** | Azure | **San Bernardo**, sala técnica de sitio | RT-03.10 · RT-21.06 |

**San Bernardo no es el DR de la nube: es el nodo que mantiene viva la operación cuando el enlace
cae.** Son cosas distintas y hay que escribirlas distinto. Con esa formulación tu plan se sostiene
entero y además cumple RT-07.02.

#### 5.9.3 Por qué San Bernardo tiene que existir igual

**RT-21.06** del Caso (pág. 34/49):

> «24x7x365 sin excepción. La flota rueda a toda hora y **todo incidente que impida asignar un
> viaje, emitir un documento de transporte o recibir un evento de emergencia se clasifica en la
> severidad máxima**.»

Esas tres funciones no pueden depender del enlace a la nube. Ese es el argumento —verificable— de
por qué San Bernardo no desaparece.

#### 5.9.4 La tipología: la regla que legitima el enfoque

**Numeral 6.1 transversal (pág. 14/51)** define tres tipologías y ordena elegir una:

| Tipología | Cuándo aplica | Qué requisitos se aplican |
|---|---|---|
| **Sala técnica principal** | «El caso requiere cómputo, almacenamiento y procesamiento **sustantivos** en las instalaciones del CLIENTE» | **RT-06.01 a RT-06.24 íntegramente** |
| **Sala técnica secundaria o de sitio** | «Sitios operacionales que requieren cómputo local para continuidad, pero **no albergan el núcleo**» | Energía, climatización, control de acceso, detección de incendio y monitoreo, **dimensionados al sitio** |
| **Gabinete o borde operacional** | «Puntos de operación con equipamiento mínimo» | Protección eléctrica, control de acceso físico, monitoreo remoto y condiciones ambientales del equipo |

Y remata:

> «El PROPONENTE deberá **declarar expresamente qué tipología adopta en cada sitio** del caso y
> justificar el dimensionamiento. **Sobredimensionar el recinto es tan penalizado como
> subdimensionarlo**: ambos revelan que el cálculo de capacidad no se hizo.»

**Nuestra declaración:**

| Sitio | Tipología declarada | Justificación |
|---|---|---|
| San Bernardo (26 m²) | **Sala técnica secundaria o de sitio** | El núcleo está en nube; aquí queda cómputo de continuidad para la torre 24×7, terminación de enlaces y custodia de medios |
| 4 terminales regionales | **Gabinete o borde operacional** | RT-06.01 del Caso: «Gabinete en cada terminal regional dimensionado para RT-03.10» |
| 374 camiones | **On-premise distribuido** | RT-06.01 del Caso, texto expreso |

> ⚠️ **Aquí está la consulta más importante de D4.** RT-06.01 del **Caso** (pág. 32/49) ordena que
> la sala de San Bernardo «debe remediarse o reemplazarse **por no cumplir el Capítulo 6 del
> documento transversal**» — sin decir a qué tipología debe llevarse. Si el CLIENTE entiende
> «llevarla al estándar íntegro de sala principal», el costo se multiplica y contradice el
> numeral 6.1, que prohíbe sobredimensionar. **Hay que preguntarlo antes del 01-09.**

> ⚠️ **Corrección de dato:** la sala es de **26 m²**, no 23. Cap. 6 del Caso, pág. 13/49, y
> RT-06.01, pág. 32/49. Si el informe dice 23 m², es un error verificable contra el documento.

#### 5.9.5 Especificación de San Bernardo

**Brecha actual** (Cap. 6 del Caso, pág. 13/49): 26 m², habilitada en 2013, climatización tipo
split, alimentación ininterrumpida de 20 minutos, acceso por credencial. El caso declara
expresamente que **no cumple** el Cap. 6 transversal.

**Qué queda alojado ahí** (y solo esto — el dimensionamiento se justifica por esta lista):

1. Cómputo de continuidad de las tres funciones de severidad máxima de RT-21.06.
2. Terminación de enlaces y borde de red hacia Azure.
3. Custodia de medios de respaldo.

**Especificación de hardware:**

| Elemento | Especificación | Requisito |
|---|---|---|
| Cómputo | 2 servidores de rack 2U en clúster de 2 nodos + testigo, **fuentes redundantes a circuitos eléctricos distintos** | RT-03.14, RT-08.04 |
| Almacenamiento | Redundante, tolerante a la falla de al menos un disco, **con nivel RAID declarado y justificado frente a alternativas**, control de errores y monitoreo predictivo de salud | **RT-03.14, RT-08.02** |
| Red | 2 conmutadores de núcleo + 2 cortafuegos, **en alta disponibilidad, sin punto único de falla** | RT-08.03 |
| Racks | Servidores en racks **independientes** de los de comunicaciones, con ocupación proyectada y margen declarados | RT-06.05 |
| Equipamiento | **Nuevo, sin uso previo, con garantía de fábrica vigente** desde la recepción conforme | RT-08.06 |
| Margen de crecimiento | Declarado como % sobre la carga proyectada, con procedimiento de ampliación | RT-08.05 |

**Habilitación del recinto** (dimensionada a tipología «sala técnica de sitio»):

| Ámbito | Especificación | Requisito | Brecha vs. hoy |
|---|---|---|---|
| Energía | UPS con autonomía **≥30 min a plena carga** | RT-06.07 | Hoy 20 min |
| Energía | Generación autónoma **≥24 h continuas**, estanque dimensionado y contrato de reabastecimiento declarado | RT-06.08 | No existe |
| Energía | Instalación eléctrica **independiente del resto del edificio**, NCh Elec. 2777 para puesta a tierra | RT-06.09 | Verificar |
| Energía | Revisión y medición **semestral** con informe entregable | RT-06.10 | No existe |
| Energía | Declarar carga proyectada en kW, factor de potencia y **PUE** | RT-06.11 | No existe |
| Clima | Climatización de precisión **redundante N+1**, control de temperatura y humedad | RT-06.13 | Hoy split |
| Clima | Monitoreo en línea de temperatura, humedad y **presencia de agua**, integrado a observabilidad | RT-06.14 | No existe |
| Incendio | Detección temprana por **aspiración de aire con tecnología láser**, tipo AnaLASER o equivalente | RT-06.16 | No existe |
| Incendio | Extinción automática por **agente limpio**, aprobación UL, instalación conforme a NFPA | RT-06.17 | No existe |
| Incendio | Extintores portátiles con mantención y certificación vigentes | RT-06.18 | Verificar |
| Incendio | Integración al monitoreo y **notificación al NOC** | RT-06.19 | No existe |
| Acceso | Control de acceso **biométrico facial con AFIS de respaldo** | RT-06.20 | Hoy credencial |
| Acceso | Bitácora auditable de ingreso y egreso con persona, fecha, hora y motivo | RT-06.21 | No existe |
| Acceso | Videovigilancia IP, **30 días en línea**, respaldo posterior recuperable | RT-06.24 | No existe |
| Acceso | Procedimiento de acceso de terceros con **acompañamiento obligatorio** | RT-06.25 | No existe |
| Medios | Custodia en medio físico transportable a otro lugar | RT-06.26 | No existe |
| Medios | Inventario con rotación, **verificación periódica de legibilidad** y registro de movimientos | RT-06.28 | No existe |
| Operación | Espacio de operación **separado de la sala de equipos**, sin requerir ingreso al recinto técnico | RT-06.29, RT-06.30 | No existe |
| Operación | Declarar qué instalaciones sanitarias y zonas de seguridad existentes del edificio se usarán, **sin reimplementarlas** | RT-06.31 | Declarar |
| Redes | Acceso a comunicaciones por **rutas físicas distintas con ingreso al edificio por puntos separados** | RT-06.32 | Verificar |

#### 5.9.6 La jugada de sostenibilidad — dos ítems con un párrafo

**RT-06.34** (pág. 17/51, deseable):

> «Se privilegiará al PROPONENTE que ofrezca o provea especificaciones nuevas o **mejores** que
> las aquí establecidas, debidamente fundamentadas.»

RT-06.17 pide «FM-200 **o equivalente**». El FM-200 (HFC-227ea) es un hidrofluorocarbono de alto
potencial de calentamiento global, en retirada progresiva por regulación ambiental. La
alternativa habitual hoy es **FK-5-1-12** o sistemas inertes de nitrógeno/argón.

Y **RT-15.03** (pág. 27/51, obligatorio) exige estimar la huella de carbono anual de la operación
de la solución y declarar la metodología.

→ **Proponer el agente de bajo GWP suma en RT-06.34 y en el Cap. 15 con el mismo párrafo.** Es un
detalle chico que se nota.

---

### 5.10 Red y enlaces

| Elemento | Especificación | Requisito |
|---|---|---|
| San Bernardo ↔ Azure | Enlace redundante con **caminos físicos y proveedores distintos**, conmutación automática con tiempo declarado | **RT-03.17** |
| San Bernardo ↔ Azure | Enlace privado dedicado o VPN cifrada según volumen y criticidad | RT-03.21 |
| 4 terminales regionales | **Respaldo de enlace**, que tres de los cuatro no tienen hoy | Cap. 15 del Caso, pág. 31/49 |
| Ancho de banda | Dimensionado por sitio, en régimen normal y en peak, **justificado con el cálculo de volumen** | RT-03.20 · Cap. 14.2 |
| Acceso remoto del personal | Acceso a la red de confianza cero con verificación de postura. **«No se admite exponer servicios internos directamente a Internet»** | RT-03.22 |
| Segmentación | Subredes privadas para aplicación y datos. **«Ningún componente de datos será alcanzable desde Internet»** | RT-03.04 |

#### La campaña de medición de cobertura — actividad con costo y plazo

Cap. 15 del Caso, pág. 31/49, entrada «Red de los sitios operacionales»:

> «con carácter propio de este caso, se exige **caracterizar la cobertura móvil real de las rutas
> que la compañía opera mediante mediciones en terreno, y no suponerla**: la disponibilidad
> declarada por los operadores **no es un antecedente aceptable** para el diseño.»

Esto no es una nota al margen: es la razón por la cual **no podemos poner un número de unidades
satelitales en el Informe 1**. Se escribe como actividad de Etapa 1, con costo, plazo, método
—recorrido instrumentado de las rutas con registro de nivel de señal por operador y por
tecnología— y entregable: mapa de sombras georreferenciado.

Ese mismo recorrido produce el **catálogo de lugares seguros de detención** que el criterio 28
necesita. **Una campaña, dos entregables.** Vale la pena decirlo así.

---

---

### 5.11 Respaldos, continuidad de datos y recuperación — Cap. 7.3

**Ninguno de estos requisitos estaba cubierto y todos son obligatorios.**

#### RT-07.09 — el esquema 3-2-1-1-0

Textual (pág. 18/51): «La política de respaldo seguirá el esquema **3-2-1-1-0**: tres copias, en
dos medios distintos, una fuera de sitio, una inmutable o fuera de línea y cero errores de
verificación de restauración.»

| Elemento | Implementación propuesta | Requisito ligado |
|---|---|---|
| 3 copias | Producción en Azure + réplica en 2.ª región + copia en San Bernardo | RT-07.03 |
| 2 medios distintos | Almacenamiento de objetos en nube + medio físico transportable | RT-06.26 |
| 1 fuera de sitio | La 2.ª región Azure y la custodia externa de medios | RT-07.02 |
| 1 inmutable o fuera de línea | Almacenamiento inmutable con retención legal | RT-07.11 |
| 0 errores de verificación | Prueba de restauración mensual documentada | RT-07.12 |

**Un matiz propio de este caso que conviene escribir:** existe una cuarta copia que nadie
planificó y que está ahí igual — los 374 dispositivos a bordo conservan 72 horas del registro
operacional. No sustituye al respaldo, pero es una fuente real de reconciliación ante una pérdida
de datos reciente, y refuerza el argumento del borde como parte del esquema de continuidad.

#### Los demás requisitos de respaldo

- **RT-07.10:** respaldos cifrados en reposo y en tránsito, con clave gestionada **de forma
  independiente de la infraestructura respaldada**. Consecuencia de diseño: la clave no puede
  vivir en la misma suscripción que protege.
- **RT-07.11:** copias inmutables protegidas contra borrado y modificación durante su retención,
  **incluso frente a credenciales administrativas comprometidas**.
- **RT-07.12:** prueba de restauración **al menos mensual**, sobre muestra representativa, con
  medición del tiempo efectivo de restauración.
- **RT-07.13:** declarar **por cada dominio de datos** la frecuencia de respaldo, el período de
  retención y el tiempo estimado de restauración completa. Es una tabla obligatoria y se cruza
  con RT-05.10 del Caso (pág. 31/49):

| Dominio de datos | Retención exigida |
|---|---|
| Registro de jornada de conducción y su evidencia | mínimo 5 años |
| Documento electrónico de transporte y antecedentes del viaje | 6 años |
| Antecedentes de siniestros | 10 años |
| Habilitaciones de conductores y equipos | su vigencia y 5 años más |
| Registros de carga peligrosa | 5 años |
| Evidencia de tiempos de llegada y salida en instalaciones de cliente | 3 años |
| Liquidaciones a transportistas | 6 años |
| Series de posición y telemetría | 2 años en línea, con política de agregación declarada |

- **RT-07.14:** restauración granular — un registro, una tabla, un módulo o el sistema completo.

#### Procedimientos de conmutación — RT-07.05 a RT-07.08

- **RT-07.05:** conmutación documentada, automatizada en la mayor medida posible y **ejecutable
  por el personal del CLIENTE** tras la transferencia de conocimiento. Con un área de TI de 9
  personas, esto condiciona el diseño: el procedimiento no puede depender del adjudicatario.
- **RT-07.06:** procedimiento de **retorno** al sitio principal, igualmente documentado y probado,
  con reconciliación de los datos generados durante la contingencia.
- **RT-07.07:** el plan de DR se prueba **al menos dos veces al año mediante conmutación real**,
  con informe de resultados, medición del RTO y RPO efectivamente alcanzados y plan de corrección
  de brechas.
- **RT-07.08** (deseable): conmutación automática ante detección de indisponibilidad, con criterio
  de disparo declarado y protección contra conmutación innecesaria.

> ⚠️ **Choque con la ventana operacional del caso.** RT-07.07 exige dos conmutaciones reales al
> año. RT-10.05 del Caso (pág. 32/49) declara congelamiento de diciembre a abril por temporada de
> fruta, en las ventanas de restricción vehicular de Semana Santa y Fiestas Patrias, y durante los
> nueve días del cierre mensual de liquidaciones. **La ventana disponible para probar el DR es
> estrecha y hay que calendarizarla explícitamente**, o el requisito queda incumplible en la
> práctica. Vale como observación en la propuesta.

---

### 5.12 Desempeño, capacidad y escalabilidad — Cap. 9

#### Umbrales del numeral 9.1

Exigibles en producción, **medidos en el percentil 95 sobre la experiencia real de la persona
usuaria** y bajo la carga de peak declarada (pág. 21/51):

| Operación | Umbral transversal |
|---|---|
| Carga inicial de una página del portal | 2 s |
| Navegación entre vistas ya cargadas | 1 s |
| Interfaz de programación de consulta simple | 500 ms |
| Interfaz de programación de escritura transaccional | 800 ms |
| Transacción operacional crítica de terreno, de extremo a extremo | definido por el caso; en su defecto 3 s |
| Búsqueda con criterios compuestos | 3 s |
| Generación de un informe estándar en línea | 30 s |
| Procesamiento por lotes | 10.000 registros por minuto |
| Carga de un archivo de 100 MB | 60 s |
| Arranque en frío de un servicio | 60 s |

**El Caso endurece la fila crítica.** RT-09.01 del Caso (pág. 32/49) fija: asignación de viaje con
verificación bloqueante de jornada, habilitaciones y aptitud del equipo **≤30 s**; emisión del DET
**≤90 s**; transmisión del botón de emergencia a la torre **≤15 s con cobertura**; publicación de
la posición al cliente **≤2 min**. Por la regla de §0.2 prevalece el más exigente **fila por
fila**, no el documento completo.

#### Requisitos de capacidad

- **RT-09.01:** presentar el cálculo de capacidad con los supuestos de usuarios concurrentes,
  transacciones por segundo, volumen de datos y crecimiento anual, tomados de la volumetría del
  caso. → **Falta lo de concurrencia**: el Cap. 14.2 pide estimar personas usuarias internas
  concurrentes considerando turnos 24×7 (torre de 22 personas, 336 con acceso) y externas
  (84 clientes, 148 transportistas, 258 conductores).
- **RT-09.02** (según caso): la solución soportará la concurrencia y el volumen de transacciones
  que fije el caso, **manteniendo los umbrales del numeral 9.1 bajo esa carga**. El Caso lo
  parametriza (pág. 32/49): «El PROPONENTE lo deriva de la volumetría del numeral 14.1,
  considerando la **reconexión simultánea de unidades al salir de zonas de sombra**, y lo declara
  conforme al numeral 14.2.» Es decir: el peak de diseño de este caso **no es el peak de usuarios,
  es el peak de reconexión**.
- **RT-09.03:** soportar **sin rediseño un crecimiento de al menos tres veces la volumetría
  inicial en un horizonte de tres años**.
  > ⚠️ El caso proyecta 430 camiones y ≈118.000 viajes a tres años, que es ≈1,2×, no 3×. **El
  > requisito transversal es más exigente que la proyección del caso y por §0.2 manda.** Hay que
  > dimensionar a 3× y decirlo, o justificar por qué no.
- **RT-09.04:** escalamiento horizontal y automático de las capas de aplicación e integración, con
  tiempo de reacción declarado y **sin pérdida de transacciones en curso**.
- **RT-09.05:** identificar **el componente que primero se convertirá en cuello de botella** y
  explicar cómo se detecta y cómo se resuelve.
  > **En este caso la respuesta es concreta y defendible: la ingesta en la reconexión masiva.**
  > Cientos de unidades saliendo de la misma zona de sombra vuelcan simultáneamente hasta 72 h de
  > buffer contra el mismo punto de entrada. Se detecta por profundidad de cola y retraso de
  > procesamiento; se resuelve con particionado, retroceso aleatorizado y ventana de
  > sincronización escalonada. Responder esto bien vale más que cualquier cifra de capacidad.
- **RT-09.06:** pruebas de carga sobre Preproducción a **1,5 veces el peak declarado**, y pruebas
  de estrés hasta identificar el punto de quiebre.
- **RT-09.07:** informe de pruebas con curva de tiempo de respuesta frente a carga, punto de
  saturación, consumo de recursos y comportamiento **durante y después** del peak.
- **RT-09.08:** degradación controlada al superarse la capacidad — encolamiento, limitación de
  tasa y mensaje explícito a la persona usuaria, **nunca error genérico ni pérdida silenciosa de
  transacciones**.
- **RT-09.09:** gestión de capacidad durante la Operación con proyección trimestral de
  crecimiento, alertas anticipadas de agotamiento y propuesta de ajuste de dimensionamiento y de
  costo.
- **RT-09.10** (deseable): pruebas de carga automatizadas y periódicas en el flujo de integración
  continua, con detección de regresiones de desempeño.

---

### 5.13 Disponibilidad, continuidad y resiliencia — Cap. 10

- **RT-10.01:** disponibilidad mensual mínima de **99,9 % para los servicios críticos, medida
  sobre la transacción de negocio de extremo a extremo**. El numeral 7.2 lo aclara: los 99,95 % de
  infraestructura «son un medio, no un fin»; lo que se mide y se penaliza es el **Artículo 78° de
  las Bases Administrativas**.
- **RT-10.02:** clasificar cada servicio en crítico, alto, medio o bajo, justificando con el
  impacto operacional de su indisponibilidad. **Clasificación propuesta**, anclada en RT-21.06 del
  Caso (pág. 34/49):

| Servicio | Clase | Justificación |
|---|---|---|
| Asignación de viaje con verificación bloqueante | Crítico | RT-21.06: severidad máxima |
| Emisión del documento electrónico de transporte | Crítico | RT-21.06: severidad máxima |
| Recepción del evento de botón de emergencia | Crítico | RT-21.06: severidad máxima |
| Ingesta de telemetría y sincronización diferida | Alto | Tolera diferimiento por diseño: buffer de 72 h |
| Portal del cliente y del transportista | Alto | Compromiso con el cliente del 19 % de los ingresos |
| Liquidación mensual a transportistas | Alto | Proceso de nueve días, no continuo |
| Analítica y tableros de gestión | Medio | RT-05.29 admite consolidación diferida |

- **RT-10.03:** plan de continuidad del negocio conforme a **ISO 22301**, con análisis de impacto
  en el negocio, escenarios de contingencia, procedimientos manuales de respaldo y criterios de
  activación.
- **RT-10.04:** continuidad TIC conforme a **ISO/IEC 27031**, articulada con el plan de
  recuperación ante desastres del Cap. 7.
- **RT-10.05** (según caso): mantenimientos programados fuera de la ventana operacional crítica,
  con aviso previo mínimo de **diez días hábiles**. El Caso lo endurece: la flota rueda 24×7×365 y
  **no existe ventana de detención**; la intervención es camión por camión y terminal por terminal.
- **RT-10.06:** desplegar cambios **sin interrupción del servicio**. Las ventanas de
  indisponibilidad programada son excepcionales y se justifican caso a caso.
- **RT-10.07:** pruebas de resiliencia mediante **inyección controlada de fallas** —caída de
  instancia, de zona, de dependencia externa, latencia elevada, saturación de disco— antes de cada
  paso a producción y al menos una vez por semestre durante la Operación.
- **RT-10.08:** documentar, **por cada dependencia externa**, el comportamiento de la solución
  cuando esa dependencia no responde, responde con error o responde con lentitud.
  > En este caso las dependencias externas están nombradas y son muchas: las tres plataformas de
  > posicionamiento, la telemetría de fábrica por OEM, la red de estaciones de servicio, el
  > dispositivo de peaje, el sistema contable, los sistemas de los 84 clientes y la autoridad
  > aduanera. **Es una tabla larga y es obligatoria.**
- **RT-10.09** (deseable): presupuesto de error por servicio crítico, vinculado al ritmo de
  despliegue de cambios.

---

### 5.14 Ciclo de vida y disposición final del equipamiento — Cap. 8.5

- **RT-08.16:** plan de ciclo de vida del equipamiento: recepción, puesta en servicio, mantención,
  actualización, retiro y disposición final. **En este caso el plan tiene una restricción física
  única**: cada etapa que toque el vehículo sólo ocurre cuando el camión pasa por un terminal, y
  el 22 % de la flota subcontratada pasa menos de una vez al mes.
- **RT-08.17:** todo medio de almacenamiento que salga de servicio será **borrado de forma segura
  y verificable, con certificado de destrucción o de sanitización entregado al CLIENTE**.
  > Aplica de lleno a los dispositivos a bordo retirados: contienen posición y jornada de personas
  > identificables, que RT-11.10 obliga a cifrar a nivel de campo. Un dispositivo dado de baja sin
  > sanitizar es una fuga de datos personales.
- **RT-08.18:** disposición final del equipamiento electrónico con **gestor autorizado**, conforme
  a la normativa de residuos aplicable, con certificado de disposición.
- **RT-08.19** (deseable): estrategia de reacondicionamiento o de extensión de vida útil que
  reduzca el impacto ambiental, **cuantificada en la propuesta**. Se encadena con RT-15.03 (huella
  de carbono) y con RT-06.34, igual que el agente de extinción de bajo GWP.

**Y el punto que ya detectamos:** RT-08.13 obliga a declarar el ciclo de vida esperado, la
disponibilidad de repuestos y el plan de reposición **durante los 56 meses del Contrato**. Con un
dispositivo marcado como fin de vida, ese requisito no se puede firmar.

---

### 5.15 Infraestructura de cómputo y puestos de trabajo — Cap. 8.1 y 8.2

**RT-08.01** exige especificar el equipamiento de cómputo con **marca, modelo de referencia,
procesador, memoria, almacenamiento local, interfaces y consumo, junto con el cálculo de
dimensionamiento que lo sustenta**. Aplica al hardware de San Bernardo y de los gabinetes de
terminal.

**Los puestos de trabajo del numeral 8.2 no estaban asignados a nadie**, y la población es
conocida: torre de programación de **22 personas en turnos 24×7**, área de TI de **9 personas**,
**336 personas propias con acceso a sistemas** (Cap. 14.1, pág. 29/49).

- **RT-08.07:** especificar las estaciones de trabajo para la operación y la administración de la
  plataforma, en la cantidad que determine el dimensionamiento, **con monitores duales**.
- **RT-08.08:** los puestos cumplirán las condiciones ergonómicas de la **NCh 2527** y los equipos
  contarán con certificación de eficiencia energética. *Verificar la norma en el INN antes de
  citarla; si el código no corresponde, es consulta.*
- **RT-08.09:** estaciones gestionadas de forma centralizada, con **cifrado de disco, control de
  dispositivos extraíbles, antivirus con detección y respuesta y actualización automatizada**.
- **RT-08.14:** los dispositivos de terreno se integran a la gestión centralizada de flota exigida
  en RT-03.18.
- **RT-08.15** (deseable): proveer **una unidad de cada tipo de dispositivo especificado para
  pruebas de aceptación del CLIENTE antes de la compra masiva**.
  > En este caso es más que deseable: es la única forma de validar en terreno el buffer de 72 h y
  > el comportamiento térmico en el norte **antes** de comprometer el parque completo. Conviene
  > ofrecerlo aunque sea deseable, porque además desactiva el riesgo del dispositivo en fin de vida.

---

### 5.16 Requisitos del Capítulo 6 que faltaban

- **RT-06.02:** los muros no estructurales del recinto contarán con **blindaje perimetral**; el
  PROPONENTE especificará el material y la resistencia.
- **RT-06.03:** entregar el **plano de distribución interna** con separación de las zonas de
  generadores, baterías, climatización, servidores, comunicaciones, trabajo y respaldo.
  > **Es un entregable gráfico, y en 26 m² es una restricción real de diseño.** Separar siete
  > zonas en esa superficie es justamente lo que obliga a decidir la tipología del numeral 6.1 y
  > refuerza la consulta C-05 sobre si el espacio admite ampliación.
- **RT-06.04:** piso técnico, canalización, cableado estructurado y etiquetado conforme a norma,
  **con documentación de la certificación de cada enlace**.
- **RT-06.12** (deseable): redundancia de alimentación en configuración **2N o N+1** con doble
  acometida y transferencia automática.
- **RT-06.15** (deseable): estrategia de contención de pasillo frío o caliente y su efecto en la
  eficiencia energética. Con dos racks probablemente no aplica: **declararlo y justificar por qué
  no**, en lugar de omitirlo, porque la omisión se lee como olvido.
- **RT-06.22:** espacio para la atención de personas en proceso de **enrolamiento** entre el
  acceso principal y el término del pasillo de la zona de control. Las bases evalúan mejor que la
  estación de enrolamiento esté **fuera** del recinto técnico.
- **RT-06.23:** al término del pasillo, un acceso que **impida el paso de más de una persona a la
  vez**, con nueva verificación de identidad previa al ingreso.
- **RT-06.27:** el recinto de custodia cumplirá exigencias de **luminosidad, humedad, ventilación**
  y cualquier otro factor que pueda afectar la calidad y disponibilidad de los medios.
- **RT-06.33:** el PROPONENTE proveerá **toda la conectividad, la seguridad y las canalizaciones,
  cañerías o ductos** requeridos para cumplir los niveles de servicio comprometidos.

> ⚠️ **Tensión con la tipología declarada, y es importante.** El blindaje perimetral (RT-06.02),
> la esclusa (RT-06.23) y el espacio de enrolamiento (RT-06.22) pertenecen al bloque RT-06.01 a
> RT-06.24, que el numeral 6.1 aplica **íntegramente sólo a la sala técnica principal**. Si San
> Bernardo se declara «sala técnica secundaria o de sitio», ese numeral exige energía,
> climatización, control de acceso, detección de incendio y monitoreo **dimensionados al sitio**, y
> no necesariamente esclusa ni blindaje.
>
> **La diferencia de costo es grande en ambas direcciones y la decisión no es nuestra:** por eso
> C-03 es la consulta más importante de D4. Mientras no haya respuesta, la propuesta declara la
> tipología de sitio, la justifica, y deja el alcance íntegro como alternativa costeada aparte.

---

### 5.17 Capítulo 3 — tres requisitos que faltaban

- **RT-03.11:** durante la operación desconectada, la solución continuará registrando las
  transacciones operacionales críticas de forma local, **con integridad garantizada y sin pérdida
  de datos**. Es el complemento exacto de RT-03.10 y hay que citarlo junto a él.
- **RT-03.19** (deseable): se valorará el **procesamiento en el borde** de las cargas que lo
  admitan —filtrado, agregación previa, inferencia local— reduciendo el volumen transferido y la
  dependencia del enlace.
  > **Ya lo estamos haciendo y no lo estábamos nombrando:** las geocercas se evalúan a bordo y la
  > alerta de jornada se calcula a bordo. Citarlo con su código es puntaje regalado.
- **RT-03.23** (según caso): la red inalámbrica de los sitios operacionales contará con
  segmentación por tipo de dispositivo, autenticación por certificado o credencial de empresa y
  **cobertura verificada mediante estudio de sitio**. Aplica a los cinco terminales y los dos
  talleres propios.


### 5.18 Tecnologías de software

El plan (pág. 5/9) exige «versión, fecha de fin de soporte y plan de actualización que cubra los
56 meses». Plantilla obligatoria — **una fila por producto, sin excepción**:

| Producto | Versión ofertada | Fin de soporte del fabricante | Cobertura de los 56 meses | Plan de actualización | Reversibilidad (RT-03.07) |
|---|---|---|---|---|---|

Reglas que gobiernan las elecciones:

- **RT-03.05**: privilegiar servicios administrados sobre autoadministrados cuando reduzca riesgo
  operacional, y **justificar cada excepción**.
- **Numeral 2.3**: comparar al menos dos alternativas y explicar por qué se descarta la no elegida.
- **Error que el caso castiga explícitamente** (num. 2.3): adoptar microservicios sin volumen que
  lo justifique — «error de ingeniería». Con ~96.000 viajes/año, **hay que justificar el estilo
  arquitectónico con la volumetría, no con la moda**. Coordinar con D3.

---

### 5.19 Diagramas

#### Diagrama 1 — Arquitectura física general

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║  NUBE PÚBLICA — Azure Chile Central (Santiago)          3 zonas disp.         ║
║  ┌─────────────┐ ┌──────────────┐ ┌────────────┐ ┌──────────────────────┐    ║
║  │ IoT Hub +   │ │ Event Hubs   │ │ AKS        │ │ PostgreSQL Flexible  │    ║
║  │ Device      │→│ (particionado│→│ zone-      │↔│ HA zone-redundant    │    ║
║  │ Update      │ │  reconexión) │ │ redundant  │ │                      │    ║
║  └─────────────┘ └──────────────┘ └────────────┘ └──────────────────────┘    ║
║  ┌─────────────────┐ ┌───────────────────┐ ┌──────────────────────────┐      ║
║  │ Data Explorer   │ │ Blob inmutable    │ │ Key Vault HSM            │      ║
║  │ series posición │ │ evidencia jornada │ │ cifrado campo RT-11.10   │      ║
║  └─────────────────┘ └───────────────────┘ └──────────────────────────┘      ║
╚════════════════════════════════════╤══════════════════════════════════════════╝
              ┌─────────────────────┐ │ ┌──────────────────────────┐
              │ 2.ª REGIÓN AZURE    │◄┘ │ RTO ≤ 4 h · RPO ≤ 15 min │
              │ DR activo-pasivo    │   │ RT-07.02 amenaza distinta│
              └─────────────────────┘   └──────────────────────────┘
                                     │
                   ExpressRoute ══════╪══════ VPN respaldo
                   (proveedor A)      │       (proveedor B)   ← RT-03.17
                                     │
╔════════════════════════════════════▼══════════════════════════════════════════╗
║  SAN BERNARDO — Sala técnica DE SITIO (26 m²)      Tipología num. 6.1         ║
║  ┌──────────────────┐  ┌────────────────┐  ┌───────────────────────────────┐ ║
║  │ 2× servidor 2U   │  │ 2× switch núcleo│ │ Custodia de medios RT-06.26/28│ ║
║  │ clúster+testigo  │  │ 2× firewall HA  │ └───────────────────────────────┘ ║
║  │ doble fuente     │  └────────────────┘                                    ║
║  └──────────────────┘  UPS ≥30min · Grupo ≥24h · Clima precisión N+1         ║
║  Continuidad de: asignar viaje · emitir DET · recibir pánico  ← RT-21.06      ║
╚════════════════════════════════════╤══════════════════════════════════════════╝
                                     │
        ┌────────────────────────────┼────────────────────────────┐
        │                            │                            │
┌───────▼────────┐          ┌────────▼───────┐          ┌────────▼────────┐
│ GABINETE       │          │ GABINETE       │   ...    │ GABINETE        │
│ Antofagasta    │          │ Talca          │          │ Puerto Montt    │
│ cómputo 12 h   │          │ cómputo 12 h   │          │ cómputo 12 h    │
│ enlace+respaldo│          │ enlace+respaldo│          │ enlace+respaldo │
└────────────────┘          └────────────────┘          └─────────────────┘
        ↑ RT-06.01 del Caso: «gabinete en cada terminal dimensionado para RT-03.10»
```

#### Diagrama 2 — El camión: componente on-premise distribuido

```
┌────────────────────────────────────────────────────────────────────────────┐
│  CABINA DEL CAMIÓN            RT-06.01 Caso: on-premise distribuido ×374    │
│                                                                            │
│   ┌──────────────────────────────────────────────────────┐                │
│   │  A. UNIDAD TELEMÁTICA                                 │                │
│   │  · GNSS                                               │                │
│   │  · BUFFER NO VOLÁTIL ≥8 GB   ← RT-03.10 (72 h)        │                │
│   │      posición · eventos jornada · tiempos en          │                │
│   │      punto de cliente · documentos del viaje          │                │
│   │      (+ margen para 12 días de cierre fronterizo)     │                │
│   │  · Geocercas evaluadas A BORDO ← decisión 8, RT-09.01 │                │
│   │  · Alerta de jornada calculada A BORDO ← criterio 28  │                │
│   │  · Modo privacidad EN FIRMWARE ← criterio 29          │                │
│   │  · Gestión remota: firmware, bloqueo, borrado         │                │
│   │        ← RT-03.18 vía Azure IoT Hub Device Update     │                │
│   └───┬──────────┬──────────────┬───────────────┬─────────┘                │
│       │          │              │               │                          │
│   ┌───▼────┐ ┌───▼────────┐ ┌──▼──────────┐ ┌──▼─────────────┐            │
│   │ CELULAR│ │ B. MÓDULO  │ │ C. ID DEL   │ │ CAN / FMS      │            │
│   │ 4G     │ │ SATELITAL  │ │ CONDUCTOR   │ │ · tacógrafo    │            │
│   │ PRIMARIO│ │ SBD        │ │ NFC pasivo  │ │   descarga     │            │
│   │        │ │ solo        │ │ SIN acción  │ │   remota DDD   │            │
│   │ tasa   │ │ subconjunto │ │ del conduc- │ │ · telemetría   │            │
│   │ completa│ │ por riesgo │ │ tor         │ │   motor        │            │
│   └────────┘ └────────────┘ └─────────────┘ └────────────────┘            │
│                                  ↑ RT-12.11: sin manipular, sin recordar   │
│                                              credencial                    │
│   ✗ NINGUNA interacción del conductor en marcha   ← restricción 1          │
│   ✗ Solo se instala/actualiza en TERMINAL         ← restricción 5          │
│   ✗ No puede afectar la garantía del vehículo     ← restricción 6          │
└────────────────────────────────────────────────────────────────────────────┘

  61 tractocamiones adicionales: telemetría de fábrica por rFMS v5.0.0
  ── solo lectura, sin instalar hardware, sin pasar por terminal ──
     API REST/HTTPS del OEM ─────────────────────────► Azure (integración)
     RT-17.06 · decisión 12 · Cap. 11: no se interviene la electrónica
```

#### Diagrama 3 — Flujo de un evento de jornada sin cobertura

```
  t0   Camión en ruta, zona de sombra (>80 km sin señal)
        │
        ├─► Evento de jornada ocurre  ──► SE ESCRIBE EN BUFFER LOCAL
        │                                  (el registro YA existe, aunque
        │                                   caiga la nube entera)
        │
        ├─► ¿Es crítico? (pánico / geocerca / frontera)
        │        │
        │        └─ Sí ──► SBD ──► Iridium ──► nube   [solo capa 2]
        │                          latencia declarada ≠ 15 s
        │
   t+Xh  Recupera cobertura celular
        │
        ├─► Sincronización diferida con backoff aleatorizado
        │   (evita la avalancha de cientos de unidades saliendo
        │    de la misma sombra ← Cap. 14.2)
        │
        └─► Reconciliación determinista de conflictos
            con bitácora auditable        ← RT-03.12
            Objetivo: ≤20 min por camión  ← Cap. 15 del Caso, pág. 31/49
```

---

## 6. «Innovaciones» — ficha T-19 de D4: tipo 2, Proceso

**Terreno asignado** (plan, pág. 6/9): «Despliegue camión por camión con ventana de 6 días;
actualización remota del parque; incorporación de la intervención del taller externo a la hoja de
vida del equipo».

**Restricción de admisibilidad:** no se acepta como innovación la adopción de una tecnología ya
estándar, la mención de una tendencia sin diseño de incorporación, ni una funcionalidad que las
bases ya exigen. Y el T-22 advierte que «en ningún caso puede presentarse sólo el título».

**Idea propuesta — «Despliegue sin detener la flota»:**

El problema real no es técnico: **un camión detenido no produce** (restricción 10), un camión pasa
por terminal cada 6 días y el 22 % de la flota subcontratada pasa menos de una vez al mes
(Cap. 6, pág. 14/49), y la flota rueda 24×7×365 sin ventana de detención, con congelamientos de
diciembre a abril, Semana Santa, Fiestas Patrias y los nueve días del cierre mensual de
liquidaciones (RT-10.05, pág. 32/49).

Lo que se innova: convertir el paso fortuito por terminal en una **ventana de intervención
planificada y de duración acotada**, mediante preconfiguración total del dispositivo antes de que
el camión llegue —el numeral 8.4 exige stock de reemplazo en sitio «con configuración
precargada»—, de modo que la intervención física sea *sustituir y salir*, y todo el resto del
ciclo de vida ocurra por aire.

**Los siete elementos del Art. 29° a completar en el T-19** (esqueleto, falta redactar):

1. **Idea** — el despliegue deja de ser un proyecto con fecha de término y pasa a ser un proceso
   continuo que se ejecuta en la ventana que la operación ya tiene.
2. **Tecnología** — gestión remota del parque por Azure IoT Hub Device Update; configuración
   precargada; anticipación de llegada a terminal a partir de la propia posición de la flota.
3. **Alcance** — 148 propios por decisión; 34 sin dispositivo por adhesión; ~192 de terceros solo
   si su dueño adhiere.
4. **Forma de implementación** — kit preconfigurado, arnés estándar por familia de vehículo,
   procedimiento de 30 min, verificación automática post-instalación.
5. **Resultados esperados** — **indicador obligatorio**: unidades intervenidas por mes y tiempo de
   inmovilización por unidad. El criterio 27 exige resultados medibles: cuántos de los 148
   transportistas adhirieron y en qué plazo.
6. **Riesgos** — el 22 % que pasa menos de una vez al mes marca el techo del ritmo de despliegue.
7. **Encaje con el caso** — resuelve simultáneamente la restricción 5 y la restricción 10.

> **Sincronización pendiente:** la adhesión de los 148 transportistas es de D2 (innovación tipo 4).
> Nuestra ficha es el **cómo físico**; la de ellos es el **por qué comercial**. Deben citarse
> mutuamente o se leerán como dos propuestas desconectadas.

---

## 7. Supuestos que D4 declara

El Cap. 14.2 (pág. 30/49) advierte: «valores sin derivación, se evaluará como dimensionamiento no
realizado». Todo supuesto va con su derivación.

| # | Supuesto | Valor | Derivación | Cómo se cierra |
|---|---|---|---|---|
| S-01 | Velocidad comercial media | 55 km/h | Supuesto D4 sobre 41.000.000 km/año y perfil de ruta interurbana | Medición en Etapa 1 |
| S-02 | Horas de marcha en 72 h calendario | ≈ 30 h | Art. 25 bis: descansos obligatorios | — |
| S-03 | Tamaño de registro de posición | 64 B | Composición del registro declarada en §5.3.2 | Ajuste con el fabricante elegido |
| S-04 | Volumen en buffer tras 72 h | ≈ 0,8 MB sin imágenes; ≈ 3,2 MB con imágenes | §5.3.2 | — |
| S-05 | Especificación de almacenamiento a bordo | **≥ 8 GB no volátil** | S-04 × factor de seguridad + cierre fronterizo de 12 días (RT-10.05) | — |
| S-06 | Consumo mensual de datos por camión | 13–16 MB (escenario B, sin fotografía) | §5.5 | Campaña de medición |
| S-07 | Consumo agregado de la flota | ≈ 5,6 GB/mes | S-06 × 374 | — |
| S-08 | Población que requiere capa satelital | **No estimable hoy** | RT-03.24 prohíbe suponer la cobertura | Campaña de medición, Etapa 1 |
| S-09 | Composición del parque de terceros | **Desconocida** | El caso no la entrega | Levantamiento en Etapa 1 + consulta |
| S-10 | Tarificación satelital por mensaje, no por byte | Modelo SBD | §5.5 | Cotización |
| S-11 | Latencia de pánico en modo satelital | A declarar y fundamentar | RT-09.01 limita el umbral de 15 s a «con cobertura» | — |
| S-12 | Tipología de San Bernardo | Sala técnica de sitio | Numeral 6.1 transversal | **Consulta C-03** |

---

## 8. Consultas al CLIENTE — cierran el 01-09-2026

El Art. 43° advierte que el CLIENTE **registra qué empresas identifican vacíos, contradicciones y
riesgos**, y cuáles solo piden aclaraciones sobre materias ya resueltas en el texto.

**Las de D4, por orden de impacto:**

| # | Consulta | Por qué bloquea a D4 |
|---|---|---|
| **C-01** | RT-08.10 exige declarar el costo unitario estimado de cada dispositivo de terreno dentro de la especificación técnica; el Art. 50.2 prohíbe toda cifra de precio en la Oferta Técnica bajo causal de exclusión. ¿Se entrega la especificación sin valorización en el Sobre N.º 2 y los costos en el Sobre N.º 3? | Define el formato de la tabla del T-11, que es el corazón de 4.2 |
| **C-02** | RT-03.10 exige 72 h de operación desconectada del dispositivo a bordo. La restricción 3 impide intervenir, reconfigurar o reemplazar los dispositivos de camiones de terceros sin acuerdo expreso. ¿Se entiende RT-03.10 exigible solo sobre las unidades intervenidas, quedando el resto sujeto al estándar de homologación del Cap. 11? | Sin esto, el requisito es incumplible por diseño en el 51 % de la flota |
| **C-03** | RT-06.01 del Caso ordena remediar o reemplazar la sala de San Bernardo por no cumplir el Cap. 6 transversal, sin indicar tipología. El numeral 6.1 transversal define tres tipologías y penaliza sobredimensionar. ¿Se acepta declararla como «sala técnica secundaria o de sitio», quedando el núcleo en nube? | Define todo el capítulo de data center y su costo |
| **C-04** | ¿En qué instalaciones distintas de San Bernardo existe espacio apto para un sitio secundario que satisfaga RT-07.02 (distancia suficiente para no verse afectado por el mismo evento de fuerza mayor)? | El T-11 pide primario y secundario |
| **C-05** | ¿El espacio de San Bernardo admite ampliación más allá de los 26 m²? | Condiciona el dimensionamiento |
| **C-06** | ¿Existen mediciones previas de cobertura móvil, o la caracterización en terreno se ejecuta íntegramente en Etapa 1 con cargo al proyecto? | Determina costo y plazo de una actividad obligatoria |
| **C-07** | Parque telemático de los 226 camiones de terceros: ¿cuántos por proveedor? ¿Hay información de almacenamiento local y formato de exportación? | Sin esto no hay clasificación cumple/no cumple/desconocido |
| **C-08** | ¿Algún camión de tercero cuenta con tacógrafo digital, y en qué proporción? | Dimensiona el programa del tacógrafo |
| **C-09** | ¿Cuáles de los 18 camiones de carga peligrosa son propios y cuáles de terceros? | Es la población prioritaria de capa satelital |
| **C-10** | ¿Existe autorización de la Dirección del Trabajo para sustituir la libreta de la Res. Ex. 1213/2009 por un registro electrónico, o debe tramitarse como parte del proyecto? | Convierte una decisión de diseño en un hito regulatorio |
| **C-11** | El Cap. 15 del Caso cita códigos RT que en las Bases Técnicas Transversales corresponden a requisitos distintos (ver §11). ¿Prevalece el código o la materia descrita? | Afecta la trazabilidad de toda la sección |

---

## 9. Errores que este caso castiga y que D4 puede cometer

| Error | Sanción declarada |
|---|---|
| Solución exclusivamente en nube o exclusivamente on-premise | Art. 16° BA |
| Emplazar un componente sin justificar | Art. 16.2 — **observación grave** |
| Sobredimensionar el recinto | Numeral 6.1 — igual que subdimensionar |
| Suponer la cobertura móvil en vez de medirla | RT-03.24 del Caso |
| «Instalar un dispositivo en toda la flota» sin explicar quién se lo pide a 148 dueños | Cap. 19 — «será superado por una propuesta más modesta que traiga esa conversación resuelta» |
| Un diagrama de referencia con el nombre cambiado | Cap. 19 |
| Microservicios sin volumen que lo justifique | Numeral 2.3 — «error de ingeniería» |
| Declarar «cumple» sin individualizar componente | Numeral 1.5 — «equivale a no declarar» |
| Cifras en pesos en el informe técnico | Art. 50.2 — **exclusión** |
| No declarar qué funciones NO estarán disponibles en modo desconectado | **RT-03.13 — observación grave** |

> **RT-03.13 merece atención especial de D4** (pág. 9/51): «El PROPONENTE declarará qué funciones
> **NO** estarán disponibles en modo desconectado y qué procedimiento manual las suple. La ausencia
> de esta declaración se evaluará como **observación grave**.» Es una tabla que nadie ha escrito
> todavía y que es nuestra.

---

## 10. ⛔ ANEXO ECONÓMICO — NO VA AL INFORME 1

> **Art. 50.2 de las Bases Administrativas: la Oferta Técnica no puede contener cifras de precio
> ni nada que permita inferir el monto de la oferta económica, bajo causal de exclusión.**
> Todo lo que sigue es insumo para el **Informe 3 / Sobre N.º 3**. No se copia al Informe 1.

### 10.1 Advertencia sobre las cifras

**No incluyo precios en pesos ni en dólares porque no los verifiqué**, y fabricarlos sería peor
que no tenerlos. Los precios de telemática industrial en Chile son por cotización y varían por
volumen, por distribuidor y por si el equipo va con o sin plan de datos. Lo que entrego es el
**modelo de costo**: qué hay que cotizar, en qué unidad, y qué mueve la aguja.

### 10.2 Estructura de costo del equipamiento de terreno

| Ítem | Unidad de costo | Cantidad | Notas |
|---|---|---|---|
| Unidad telemática | Por unidad | 148 propios + 34 sin dispositivo + los de terceros que adhieran | RT-08.10 pide costo unitario estimado |
| Módulo satelital SBD | Por unidad | Solo población de capa 2 — **no dimensionable hasta la campaña** | |
| Cable adaptador | Por unidad | 1 por unidad satelital | El LINK 740 lo requiere; el 710 conecta directo |
| microSD industrial ≥8 GB | Por unidad | 1 por unidad | Rango térmico industrial, no de consumo |
| Lector NFC / identificación | Por unidad | 1 por unidad | |
| Arnés e instalación | Por unidad | 1 por unidad | Mano de obra en terminal |
| **Stock de repuestos** | **10 % del parque instalado**, con configuración precargada | Numeral 8.4, pág. 20/51 | Obligatorio |
| Tacógrafo digital | Por unidad | Solo los que adhieran y no lo tengan — **cantidad desconocida, ver C-08** | |
| Lectora de tarjeta de empresa | Por unidad | Central | Habilita la descarga remota |

**Dónde cotizar** (no verifiqué stock ni condiciones en Chile):
- Teltonika Telematics — red de distribuidores por país: `teltonika-gps.com`
- Iridium Edge — distribuidores: Ground Control, AST Networks, Satellite Phone Store
- Webfleet — canal directo y partners en Chile: `webfleet.com/es_cl`

### 10.3 Costos recurrentes — los que pesan a 36 meses

La restricción 14 obliga a evaluar la propuesta económica «con especial atención al costo de
operar 36 meses» sobre un margen operacional de 9 %.

| Concepto | Unidad | Comentario |
|---|---|---|
| Plan de datos M2M celular | Por SIM/mes | **≈15 MB/mes por camión — el volumen es trivial** |
| Suscripción de plataforma telemática | Por vehículo/mes | **Aquí está el costo real, no en los datos** |
| Plan satelital SBD | Por terminal/mes + paquete de mensajes | Tarificado por mensaje: la cadencia es la palanca |
| Suscripción rFMS por OEM | Por contrato | **El dato es gratuito; el acceso puede no serlo** — verificar marca por marca |
| Azure | Por consumo | Ver §10.4 |
| Soporte de hardware crítico | 24×7, resolución en 4 h | Numeral 8.4 |

**El hallazgo económico de D4:** el costo recurrente de esta solución no está dominado por el
tráfico de datos sino por los **cargos por unidad** — SIM, suscripción de plataforma, suscripción
satelital, suscripción por OEM. Todos escalan con las 374 unidades y luego con las 430. Esa es la
conversación que hay que tener con proveedores, y es lo que hay que modelar a 36 meses.

### 10.4 Azure — cómo costear sin inventar

**No entrego cifras.** Azure cambia precios, y Chile Central tiene tarifa propia. El camino
correcto:

1. **Calculadora oficial:** `azure.microsoft.com/pricing/calculator`, región **Chile Central**.
2. **Drivers de costo a modelar**, en orden de peso esperado:
   - Ingesta IoT Hub: mensajes/día. Con 374 unidades y muestreo adaptativo ≈ 26.700 mensajes/mes
     por camión → **≈10 M mensajes/mes** para la flota. Determina el nivel de IoT Hub.
   - Data Explorer: 2 años de series en línea (RT-05.10 del Caso) — el cálculo del volumen anual
     de series de posición es un ítem explícito del Cap. 14.2 y **falta hacerlo con D3**.
   - Blob inmutable: evidencia de jornada a 5 años, DET a 6, siniestros a 10.
   - AKS: nodos zone-redundant, el peak de asignación de la torre gobierna.
   - PostgreSQL HA zone-redundant: vCore + almacenamiento + réplica.
   - ExpressRoute: cargo por puerto + tránsito.
   - Egreso de datos: subestimado casi siempre; los portales de 84 clientes y 148 transportistas
     lo generan.
3. **Palancas que RT-03.08 pide reflejar:** instancias reservadas, planes de ahorro o capacidad
   comprometida a 1 y 3 años cuando el perfil de carga lo justifique.
4. **RT-03.06 obliga a FinOps de todos modos:** etiquetado por ambiente, módulo y centro de costo;
   presupuestos con alertas de desviación; reporte mensual desglosado al CLIENTE. Eso hay que
   presupuestarlo como trabajo, no solo como configuración.

### 10.5 Habilitación de San Bernardo

| Partida | Comentario |
|---|---|
| Obra civil de separación | **De cargo del CLIENTE**; nuestra es la especificación y la coordinación (RT-06.06) |
| UPS ≥30 min | Reemplaza el actual de 20 min |
| Grupo electrógeno ≥24 h + estanque + contrato de reabastecimiento | No existe hoy |
| Climatización de precisión N+1 | Reemplaza el split |
| Detección por aspiración láser | No existe |
| Extinción por agente limpio de bajo GWP | Ver RT-06.34: la mejora se privilegia |
| Control de acceso biométrico + CCTV 30 días | Reemplaza la credencial |
| Servidores, almacenamiento, red HA | Equipamiento nuevo con garantía vigente (RT-08.06) |
| Puesta a tierra y medición semestral | RT-06.09, RT-06.10 |

---

## 11. Registro de hallazgos y contradicciones

### 11.1 Códigos RT que no calzan entre el Caso y las Transversales

Verificado por OCR. **Recomiendo revisar las págs. 31–33 del Caso a ojo antes de enviar C-11.**

| Código | El Caso (Cap. 15) dice | Las Transversales dicen | Carácter transversal |
|---|---|---|---|
| RT-05.10 | Retención de datos históricos y de auditoría | Catálogo de datos con linaje automatizado (pág. 12/51) | **Deseable** |
| RT-15.02 | Certificaciones sectoriales del adjudicatario | Apagar ambientes no productivos fuera de horario (pág. 27/51) | Obligatorio |
| RT-09.01 | Latencias de transacción operacional crítica | Cálculo de capacidad y dimensionamiento (pág. 22/51) | Obligatorio |
| RT-16.14 | Firma electrónica | Motor de reglas sin recompilación | **Deseable** |
| RT-03.24 | Red de sitios operacionales y medición de cobertura | Calidad de servicio y priorización de tráfico (pág. 10/51) | **Deseable** |

Unos 15 de los 24 códigos sí calzan (RT-02.12, RT-05.23, RT-05.29, RT-11.10, RT-12.11, RT-13.08,
RT-17.06 y otros). **En tres casos el Caso convierte en exigible algo que transversalmente es
solo deseable.**

**Impacto directo en D4:** RT-03.24 era el código con que íbamos a justificar la medición de
cobertura en terreno, y transversalmente ese código es otra cosa y ni siquiera es obligatorio.
→ **Citar el requisito por su texto y su página, no solo por su código.**

### 11.2 Correcciones a nuestros propios documentos

| Documento | Qué dice | Qué corresponde |
|---|---|---|
| `CONTEXTO-CASO10.md` §6.2 | «Capa 0 — todas las unidades» | «todas las unidades **intervenidas**» — restricción 3 |
| `CONTEXTO-CASO10.md` §7 | «las otras dos tienen texto seleccionable» | **Los tres PDF son escaneos.** Se requiere OCR para los tres |
| `CONTEXTO-CASO10.md` §4 | Innovación tipo 4 = D1, tipo 5 = D2 | El plan (pág. 6/9) dice tipo 4 = D2, tipo 5 = D1 |
| `BLOQUE2-INVESTIGACION-TECNICA.md` §5.3 | «El rango térmico de −40 a +85 °C cubre sin problema las condiciones del norte» | Cierto del Iridium Edge; **falso del conjunto**: el LINK 740 es −30/+70 y **IP20** |
| `BLOQUE2-INVESTIGACION-TECNICA.md` §5.5 | Plantea el umbral de 15 s del pánico como inconsistencia | **No lo es.** RT-09.01 limita el umbral a «con cobertura»; el modo satelital es un hueco que declaramos |
| `BLOQUE2-INVESTIGACION-TECNICA.md` §5.3 | Cable de 270 mm | 270 mm es el cable flexible del Iridium Edge; el **cable adaptador para LINK es de 300 mm** |
| Conversación previa | Sala de San Bernardo de 23 m² | **26 m²** — Cap. 6 pág. 13/49 y RT-06.01 pág. 32/49 |

### 11.3 Hallazgos nuevos de la ficha de Webfleet SAT

1. Almacenamiento **40 h** declarado, contra las 72 h de RT-03.10. Incumplimiento verificable.
2. La conmutación a satélite ocurre **tras 10 minutos** sin red móvil.
3. En modo satelital la posición se actualiza en la plataforma **cada 10 minutos**, no cada minuto.
4. **La ficha no menciona botón de emergencia.**
5. El Iridium Edge **ocupa el conector de E/S múltiple del LINK 7XX** — verificar competencia con
   el botón de pánico y el lector de identificación.

---

## 12. Qué falta y de quién depende

| # | Pendiente | Depende de | Fecha |
|---|---|---|---|
| 1 | Enviar C-01 a C-11 | D4 + D1 (custodia de formalidad) | **01-09** |
| 2 | Tabla de emplazamiento | **D3** entrega inventario de componentes lógicos | S4, 04-09 |
| 3 | Volumen anual de series de posición y de evidencia de jornada | **D3** (política de agregación y retención) | S4, 04-09 |
| 4 | Tabla RT-03.13: funciones NO disponibles en modo desconectado | D4 + D3 | S4, 04-09 |
| 5 | Cerrar candidato de unidad telemática y confirmar ciclo de vida a 56 meses | D4 + cotización | 03-09 |
| 6 | Ficha T-19 tipo 2 redactada con los 7 elementos del Art. 29° | D4, citando la de D2 | 04-09 |
| 7 | Verificar NCh Elec. 2777 y NCh 2527 en el INN | D4 | 03-09 |
| 8 | Verificar Decreto N.º 80/2004 y régimen chileno de tacógrafo en fuente oficial | D4 | 03-09 |
| 9 | ADR con alternativas comparadas (RT-02.04) | D4 | 05-09 |
| 10 | Tabla RT-07.13: frecuencia, retención y tiempo de restauración por dominio de datos | D4 + D3 | S4, 04-09 |
| 11 | Tabla RT-10.08: comportamiento ante cada dependencia externa que no responde | D4 + D2 | 05-09 |
| 12 | Estimación de personas usuarias concurrentes internas y externas (RT-09.01) | D4 + D2 | 04-09 |
| 13 | Dimensionamiento a 3× la volumetría inicial (RT-09.03), superior a la proyección del caso | D4 | 05-09 |
| 14 | Calendario de las dos conmutaciones reales anuales (RT-07.07) contra las ventanas congeladas | D4 | 05-09 |
| 15 | Plano de distribución interna de San Bernardo (RT-06.03), entregable gráfico | D4 | 05-09 |
| 16 | Especificación de puestos de trabajo de la torre 24×7 (RT-08.07 a RT-08.09) | D4 | 05-09 |

