# Revisión de consistencia del Informe 1 y del repositorio audIT

Fecha de corte 06-09-2026, actualizada tras los cambios de D1, D2 y D3 de las 18:45. Verificado contra los tres documentos de la licitación con
`audIT/tools/buscar.py` y por contraste cruzado entre los archivos de las cuatro duplas.

---

## 1. Lo que quedó consistente

| Materia | Estado |
|---|---|
| Cifras de volumetría del numeral 14.1 | Coinciden en las cuatro duplas y en el informe |
| Partición de la flota en 148, 192 y 34 | Alineada tras la corrección enviada a D3 |
| Buffer a bordo de 8 GB en lugar de 120 horas | Aceptado por D3 y reflejado en ambos documentos |
| Frecuencia de muestreo 30 s en marcha y 5 min detenido | Idéntica en D3 y D4 |
| Capa anticorrupción anclada a RT-05.20 | Corregido por D3 |
| App móvil como canal voluntario | Corregido por D3 |
| Plazos de retención por dominio | Idénticos en D3 y D4 |
| Proveedor de nube y región | Azure Chile Central en ambas duplas |
| Reglas de escritura del informe | Cero punto y coma, cero raya em, cero guion doble |
| Reparto de las cinco innovaciones | Ratificado por D2 el 06-09 y reflejado en el subdocumento 13 |
| Cita del Código del Trabajo | Alineada con la corrección APA de D1. Decreto con Fuerza de Ley N.º 1 de 2003, no 2001 ni 2024 |
| Metodología de emisiones | ISO 14083 y marco GLEC, ratificados por D2 en RF-023 |
| Indicadores de la innovación tipo 3 | Línea base y meta tomadas de la ficha de D3 |

## 2. Lo que sigue abierto y afecta la entrega

### 2.1 Innovaciones tipo 4 y tipo 5. RESUELTO el 06-09-2026

D2 zanjó el conflicto en su plan de trabajo y dejó constancia del acuerdo.

> Una nota anterior de reparto daba a D2 los tipos 1 y 5, y el tipo 4 a D1. Se resolvió mantener el
> reparto del plan general: D2 toma 1 y 4, y D1 queda con el tipo 5.

| Tipo | Dupla | Responsable |
|---|---|---|
| 1 Producto o servicio | D2 | Ignacio C. |
| 2 Proceso | D4 | Ignacio V. y Alonso |
| 3 Tecnológica o de arquitectura | D3 | Marcel y Martín |
| 4 Modelo de negocio o contratación | D2 | Matías V. |
| 5 Experiencia de usuario, sostenibilidad o impacto social | D1 | Carlos y Naomi |

Los marcadores de responsable pendiente ya no existen en el subdocumento 13. Queda una tarea
menor. `equipo/asignacion-duplas.md` sigue diciendo que el tipo 4 es de D1 y el tipo 5 de D2, que
es lo contrario del acuerdo. Ese archivo debe corregirse para que exista una sola fuente.

### 2.2 Las 6.000 vigencias están asignadas al contexto equivocado

El modelo de dominio sitúa la matriz completa en el contexto de Flota y activos. La mitad de esas
fechas son de personas, es decir licencia de conducir, examen médico y curso de sustancias
peligrosas. Con el reparto actual, el servicio que valida la jornada tiene que salir de su contexto
para verificar una licencia. Lo defendible es llevarla íntegra al contexto de Personas y
cumplimiento, o crear un contexto propio de Cumplimiento que sirva a los otros dos.

### 2.3 Supuestos de D3 que no aparecen en ninguna base

Verificado por búsqueda sobre los tres documentos.

| Dato | Dónde aparece | Situación |
|---|---|---|
| Precisión de geocerca de más menos 15 metros | `D3/plan-de-trabajo.md` | No está en las bases. Es supuesto y debe declararse |
| Retención de 120 horas del buffer | `D3/plan-de-trabajo.md` | Retirada en `Para_D4.md`, pero sigue en el plan |
| Resolución Exenta 107 de 2014 del SII | `D3/plan-de-trabajo.md` | Sin verificar |
| Latencia de sincronización menor a 15 minutos | `D3/plan-de-trabajo.md` | Más estricta que el umbral del Capítulo 15. Conviene redactarla como superación del umbral exigido |

### 2.4 Errores puntuales en `Para_D4.md`

| Punto | Dice | Corresponde |
|---|---|---|
| Código del buffer | Las 72 horas de desconexión, RT-03.13 | Las 72 horas son RT-03.10. RT-03.13 es la declaración de funciones no disponibles |
| Terminales con descarga por red inalámbrica | Los 5 terminales regionales | Son 4 regionales más San Bernardo, cinco en total |
| Notación del cálculo | 374 tractocamiones por 41 millones de kilómetros | Los 41 millones son el total de la flota. El resultado de 745.000 horas es correcto, la fórmula no |
| Pings anuales | 89,4 millones | Cuenta solo horas de marcha. Sumando el muestreo en detención son cerca de 120 millones |
| Concurrencia | 300 a 350 sesiones pico | El desglose propio suma 230 a 380 |
| Marcado | Repeticiones de mayor o igual a 8 GB y del signo de multiplicación | Duplicación de formato |

### 2.6 Integración de `D3/subdoc4.1-arquitectura-logica.md` al subdocumento 4

El subdocumento 4 vale 16 % por la arquitectura lógica y 16 % por la física en el Informe 1, y el
Formulario T-21 las evalúa en un solo documento. La versión anterior recogía la mitad del material
lógico de D3. Ahora está completo. Se incorporaron el diagnóstico del sistema de 2013, los
componentes declarados por capa, el contexto de cada decisión de arquitectura, los parámetros de
los patrones de resiliencia, el reparto del presupuesto de 30 segundos, la gobernanza de interfaces
del numeral 5.3, las piezas de la capa anticorrupción, la emisión del documento de transporte sin
cobertura, los parámetros leídos de la telemetría de fábrica, las capas del repositorio analítico,
la explotación analítica del numeral 5.4, el inventario de componentes lógicos y la concurrencia
derivada del numeral 14.1.

Se agregaron además cuatro requisitos obligatorios que no estaban en el material de D3 ni en el
subdocumento. RT-02.09 sobre degradación elegante, RT-02.10 sobre escalamiento automático declarado,
RT-02.11 sobre puntos únicos de falla, que evalúa como observación grave omitir la declaración
cuando existen, y RT-02.13 sobre el modelo de dominio.

#### Correcciones aplicadas al material de D3 durante la integración

| Punto | Dice el material de D3 | Corresponde según las bases |
|---|---|---|
| OpenAPI y AsyncAPI | RT-05.16 y RT-05.17 por separado | Ambos son RT-05.16, FEP02 p.12 |
| Versionado semántico y política de obsolescencia | RT-05.18 y RT-05.24 | Ambos son RT-05.17 |
| Prohibición de la clave estática en la ruta | RT-05.19 | Es RT-05.18 |
| Cuotas y límites de tasa | RT-05.21 | RT-05.21 obliga a declarar modo, volumen, ventana de la contraparte y comportamiento ante no respuesta. No trata de cuotas |
| Navegación hasta la transacción de origen | RT-05.28 | Es RT-05.26 |
| Exportación en formatos abiertos | RT-05.30 | Es RT-05.28. RT-05.30 es analítica predictiva, deseable |
| Plataformas de posicionamiento de terceros | Dos proveedores GPS | Tres plataformas distintas, dos con acceso de solo consulta y una que no permite exportar. FEP03 numeral 14.1 p.29 y p.34 |
| Contratos servidos bajo costo | Dos contratos | Tres de los ocho principales, 31 % del ingreso, el peor a menos catorce por ciento durante cuatro años. FEP03 numeral 7.3 p.15 |
| Costo preliminar en 24 horas | Atribuido a la Consulta N.º 18 | Lo fija RT-05.29 del Caso, Capítulo 15 p.31, con texto expreso sobre los componentes pendientes |
| Consultas 13, 14, 17 y 18 | Citadas como confirmadas | Están enviadas y sin responder. Lo que figura en el pliego es la interpretación propuesta por audIT |
| Parque telemático de terceros | 192 homologados y 34 sin equipo | El Caso solo declara 340 de 374 con dispositivo. La partición 192 y 34 es aritmética propia y no un inventario. El documento entrega el estándar de homologación, no el inventario |
| Retención de series de posición | RT-05.10 sin distinguir documento | RT-05.10 del Caso fija dos años en línea. El mismo código transversal es otra materia y solo deseable. Queda anotado en el texto |
| Sincronización tras la reconexión | No aparece | RT-03.13 del Caso fija 20 minutos por camión tras 72 horas sin cobertura. Incorporado |

#### Contradicciones internas del subdocumento 4, corregidas el 07-09-2026

| Punto | Decía | Dice ahora |
|---|---|---|
| Figura de arquitectura física general | Rotulaba la flota como Propios 148, Terceros 192 y Sin equipo 34, un reparto que el Caso no entrega y que el propio texto del documento declara desconocido en el supuesto S-09 | Propios 148, Terceros 226 y Sin dispositivo 34 de 374, que son los valores del numeral 14.1 página 29. El 192 exigía suponer que las 34 unidades sin equipo son todas de terceros y que los 148 propios están todos equipados, y el Caso no afirma ninguna de las dos cosas |
| Pie de cuatro figuras | Llevaba la marca Dupla 4 · Subdoc. 4.2, que es reparto interno del equipo | audIT · TFEP-01/2026 |

Corregidas en el generador `equipo/D4/canvas-d4/build.py`, no solo en la salida, de modo que no
reaparezcan al regenerar. Afecta a `Main.pdf`, `Camion.pdf`, `DosEjes.pdf` y `Flujo.pdf`.

El subdocumento 3 conserva el 192 en una tabla y es material de D2. Queda fuera de esta corrección
y se avisa al equipo.

#### Material de D3 que no se incorporó

| Elemento | Motivo |
|---|---|
| Diagrama de las ocho capas, `diagrama10` | Relación de aspecto de 0,51 sobre 3.713 píxeles de alto. A tamaño de página el texto queda en unos 3 puntos. Se usa el diagrama propio equivalente, que cumple el mismo RT-02.01 y es legible |
| Nombres comerciales de productos | El numeral 2.3 advierte que el estilo se justifica con la volumetría del caso y no con la tendencia del mercado. La declaración de productos con versión y fin de soporte va en la sección de tecnologías |
| Fórmulas del costo por kilómetro en notación matemática | Sustituidas por la tabla de componentes con su origen y con la marca de cuáles no son observables en flota de terceros |
| Cuadro comparativo de innovaciones técnicas | Su lugar es el subdocumento 13, no el 4 |
| Columna de dupla responsable en la matriz de operación desconectada | Es reparto interno del equipo y no información para el mandante |

### 2.5 El archivo `audIT/CLAUDE.md` describe otro entregable

Ese archivo describe el trabajo como un informe de investigación de 10 a 15 páginas con
cuestionario de 30 preguntas y anexo de declaración de uso de inteligencia artificial, con entrega
el 21 de septiembre. Eso corresponde al Trabajo de Investigación 2026, documento FEP00.3.26, que es
una evaluación distinta de la simulación de licitación.

Lo que las cuatro duplas están construyendo es la Oferta Técnica del Sobre N.º 2, cuyo contenido lo
fija el Formulario T-22, cuya forma la fija el Artículo 40 y cuya fecha la fija el Formulario T-20.
Son dos entregas con reglas y fechas distintas. Conviene separarlas en el archivo de notas para que
nadie aplique el límite de 15 páginas a la oferta ni el Artículo 40 al informe de investigación.

## 3. Verificaciones normativas hechas sobre el texto de las bases

| Referencia | Estado |
|---|---|
| Artículo 16.1, prohibición de solución exclusivamente en nube o en on-premise | Verificado |
| Artículo 16.2, justificación componente por componente | Verificado |
| Artículo 16.3, obligación de declarar región primaria y secundaria | Verificado |
| Artículo 40.1, foliación correlativa como requisito excluyente | Verificado |
| Artículo 50.2, prohibición de cifras de precio | Verificado |
| RT-03.10, 72 horas del dispositivo y 12 horas de los terminales | Verificado |
| RT-06.01 del Caso, dispositivo a bordo como componente distribuido | Verificado |
| RT-07.02, distancia del sitio secundario | Verificado |
| RT-09.03, crecimiento de tres veces la volumetría | Verificado |
| RT-10.05, cierres de 12 días del paso fronterizo | Verificado en dos secciones |
| Numeral 2.1, las ocho capas obligatorias | Verificado |
| Numeral 6.1, las tres tipologías de recinto | Verificado |

## 4. Cumplimiento del Artículo 40 en el documento generado

Actualizado el 07-09-2026 y verificado sobre los PDF renderizados, no sobre el fuente.

| Exigencia | Estado |
|---|---|
| 40.1 Foliación correlativa, sin páginas sin numerar | Cumple. Folio 1 en la portada y correlativo hasta la última página en los seis documentos |
| 40.1 Folio en el extremo inferior derecho | Cumple. Estaba centrado y se corrigió. El estilo `plain` del índice, que lo forzaba al centro, también se redefinió |
| 40.2 Media firma en cada página y firma en carátula | **No cumple.** No hay espacio de firma. Requiere la firma real del representante legal |
| 40.3 Correspondencia exacta entre índice y foliación | Cumple. Antes el índice contaba dos páginas menos que la foliación real |
| 40.4 PDF con texto seleccionable | Cumple |
| 40.4 Tamaño carta y orientación vertical | Cumple. Cero páginas apaisadas |
| 40.4 Cuerpo de al menos 11 puntos | Cumple, cuerpo a 12 puntos |
| 40.4 Tablas de al menos 9 puntos | Cumple, tablas a 11 puntos y leyendas a 10 |
| 40.4 Figuras de al menos 9 puntos | **No cumple.** Las diez figuras vectoriales son A4 apaisadas escaladas al 52 %, y su texto interior queda entre 4 y 6 puntos. El propio 40.4 permite anexos gráficos horizontales, que es la salida natural |
| 40.4 Referencias en norma APA séptima edición | Cumple en cinco de los seis. El subdocumento 13 no tiene ninguna fuente y el 1 tiene una entrada sin cita en el texto |
| 40.4 Nomenclatura de los Artículos 49 a 51 | **Por resolver.** Los archivos se llaman `10-audIT-SubdocNN.pdf`, que no sigue el patrón del 50.3 ni el `INFORME1_AUDIT_AAAAMMDD` asumido en la consulta 3 |
| 50.2 Ausencia de cifras de precio de la oferta | Cumple. La única cifra en pesos es la facturación del mandante, tomada del Caso |

## 5. Materias pendientes antes de la entrega

1. Resolver la asignación de las innovaciones tipo 4 y tipo 5, y actualizar `asignacion-duplas.md`
   para que exista una sola fuente.
2. Reasignar la matriz de vigencias al contexto de Personas y cumplimiento.
3. Corregir los seis puntos de `Para_D4.md`.
4. Declarar o eliminar los cuatro supuestos de D3 que no están en las bases.
5. Verificar las dos normas chilenas citadas y las referencias laborales de jornada.
6. Estimar personas usuarias concurrentes, internas y externas, para RT-09.01.
7. Incorporar la firma real en el pie de página.
8. Separar en `audIT/CLAUDE.md` los dos entregables del curso.
