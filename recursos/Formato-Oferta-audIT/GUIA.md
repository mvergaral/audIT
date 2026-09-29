# Guía del formato de la oferta técnica de audIT

Formato LaTeX de la oferta de audIT, Empresa N.º 10, en la Licitación Pública Internacional N.º TFEP-01/2026, Caso 10 Transporte de Carga, para Transportes Curimón S.A. Sirve para los tres informes preparatorios y para la propuesta final: la oferta técnica del Sobre N.º 2 y los documentos económicos del Informe 3 y del Sobre N.º 3.

El formato no trae contenido del proyecto. Los catorce subdocumentos tienen sus títulos y marcadores, y los formularios están vacíos con todos sus campos. Los documentos económicos traen sus apartados con marcadores y sus tablas de montos vacías, sin ninguna cifra del proyecto. La muestra (`salida/muestra.pdf`) enseña cada componente con marcadores y con tres extractos copiados tal cual: la tabla larga del Anexo A de `Entrega/contenido/c4.tex`, los diagramas `LogicaCapas.pdf` y `Main.pdf`, y tres filas de la tabla del Artículo 46. La muestra económica (`salida/muestra-economica-informe3/` y `salida/muestra-economica-final/`) demuestra los montos solo con valores de las bases: 1 UF y 1 USD del Formulario E-24.

## Primeros pasos

Hace falta TeX Live con LuaLaTeX, latexmk y biber, las utilidades de poppler (`pdfinfo`, `pdffonts`, `pdftotext`) y Python 3. Todo se corre desde la raíz de `Formato-Oferta-audIT/`.

```bash
./herramientas/preparar.sh                   # una vez: entorno del verificador con PyMuPDF
python3 herramientas/compilar.py muestra     # la muestra en los dos modos
python3 herramientas/verificar.py            # verifica todo lo que haya en salida/
```

## Qué hay en cada carpeta

| Carpeta | Contenido |
|---|---|
| `configuracion/` | `instancia.tex` (lo único que se edita al cambiar de entrega), `metadatos.tex` (empresa, cliente, representante, firmas), `subdocumentos.tex` (catálogo del T-7, formularios del T-21, subdocumentos del T-22 y calendario del T-20) y `economico.tex` (tipos de cambio e IVA del E-24, hitos del E-25, rangos del E-26 y documentos económicos de cada instancia) |
| `estilo/` | La clase `audit-oferta.cls` y sus módulos: `pagina`, `titulos`, `tablas`, `figuras`, `dispositivos`, `citas`, `ensamblado` y `compatibilidad` |
| `fuentes/` | Declaración de la familia IBM Plex. Las fuentes vienen con TeX Live |
| `temas/` | `marca.tex` con la paleta del manual y `grises.tex` para revisar la impresión en blanco y negro |
| `portadas/` | Portada, carátula, ficha, firma, contraportada, el motivo de la ruta y los activos de marca |
| `formularios/` | Un archivo por formulario (T-6, T-8 a T-19), la hoja resumen y la tabla del Artículo 46 |
| `subdocumentos/` | Una carpeta por subdocumento con `meta.tex`, `contenido.tex` y `formularios/` para los datos |
| `figuras/` | Diagramas por subdocumento. Junto a cada PDF conviene dejar su SVG de origen |
| `anexos/` | Tablas de observaciones de cada instancia (`observaciones-informe1.tex` y siguientes) |
| `referencias/` | `referencias.bib` con las fuentes externas en APA 7 |
| `muestra/` | Lo que usa la muestra: el Subdocumento 4 de demostración, sus observaciones y una referencia de ejemplo |
| `economico/` | Los documentos económicos (`costos-venta/`, `oferta-economica/`, `analisis-financiero/`), sus datos (`datos/partidas.csv` y `datos/tarifas.csv`) y la carpeta `planilla/` donde va la planilla del mandante |
| `herramientas/` | `compilar.py`, `verificar.py`, `tex2md.py`, `md2docx.py`, `planilla.py`, `letra_diagramas.py`, `migrar.py` y `preparar.sh` |
| `salida/` | PDF, Markdown, manifiestos e informes de verificación. `salida/aux/` guarda los intermedios |

## Cambiar de instancia y de modo de folio

Todo se decide en `configuracion/instancia.tex`:

```latex
\Instancia{informe2}          % informe1 | informe2 | informe3 | final
\Version{2.0}
\FechaEntrega{2026-10-05}     % AAAA-MM-DD, del Formulario T-20
\ModoFolio{subdocumento}      % subdocumento | continuo
\AnexoHorizontal{pagina}      % pagina | hoja
```

| Instancia | Fecha (T-20) | Subdocumentos (T-22) | Modo de folio | Nombre de cada PDF |
|---|---|---|---|---|
| `informe1` | 2026-09-07 | 1, 2, 3, 4, 5 y 13 | subdocumento | `INFORME1_AUDIT_SUBDOC04_20260907.pdf` |
| `informe2` | 2026-10-05 | 1 a 9 y 13 | subdocumento | `INFORME2_AUDIT_SUBDOC04_20261005.pdf` |
| `informe3` | 2026-11-13 | ninguno: solo documentos económicos | subdocumento | `INFORME3_AUDIT_COSTOS_VENTA_20261113.pdf` y la planilla `INFORME3_AUDIT_PLANILLA_20261113.xlsx` |
| `final` | 2026-11-25 | 1 a 14 | continuo | Sobre N.º 2: `SOBRE2_AUDIT_SUBDOC04_20261125.pdf` dentro de `SOBRE2_AUDIT_OFERTA_TECNICA_20261125.ZIP`. Sobre N.º 3: `AUDIT_OfertaEconomica_1_20261125.pdf`, `AUDIT_AnalisisFinanciero_2_20261125.pdf`, sus DOCX y `AUDIT_ModeloFinanciero_3_20261125.xlsx` dentro de `SOBRE3_AUDIT_OFERTA_ECONOMICA_20261125.ZIP` |

Con la instancia cambian solos el rótulo de portada, ficha y pie, la lista de subdocumentos, los documentos económicos, los nombres de archivo y la tabla de observaciones que se incluye (`informe2` toma `anexos/observaciones-informe1.tex`). El Formulario T-22 asigna al Informe 3 solo la parte económica: «De la Propuesta Económica corresponde a: el documento de costos frente a venta y la planilla de cálculo» (FEP01 p.69). Para los Informes 1 y 2 dice «De la Propuesta Técnica corresponde a los subdocumentos...», y para el 3 no lo dice. Por eso `informe3` no tiene subdocumentos técnicos y `compilar.py unico` y `subdocs` lo avisan y remiten a `compilar.py economico`.

En modo `subdocumento` cada PDF empieza en el folio 1. En modo `continuo` el folio es un solo correlativo a través de todos los PDF del sobre, como pidió el profesor para la propuesta final. La herramienta compila todo una vez para contar páginas, calcula dónde empieza cada archivo, recompila con esos folios y arma la hoja resumen con los folios reales. Si el conteo de páginas cambia, repite hasta que se estabiliza.

`\AnexoHorizontal` elige cómo sale la página horizontal. El valor es `pagina`: la hoja misma es apaisada (279,4 por 215,9 mm) y el pie se dibuja con sus medidas, así que el folio y la media firma quedan abajo a la derecha tal como se ven en pantalla y en papel. El Artículo 40.1 exige el folio «en zona visible del extremo inferior derecho» bajo pena de exclusión, y el Sobre N.º 2 se lee en pantalla (Artículo 48.1). El Artículo 40.4 admite anexos gráficos horizontales, así que la página apaisada cumple. Con `hoja`, pdflscape gira el contenido y el folio queda abajo a la derecha de la hoja física, pero en pantalla se ve abajo a la izquierda y de costado. Por eso en ese modo el anexo repite «Folio N» en su cabeza, y el verificador lo marca como no cumple. Queda solo por si alguien necesita esa disposición.

## Compilar

| Orden | Resultado |
|---|---|
| `python3 herramientas/compilar.py muestra` | `salida/muestra.pdf`, `salida/muestra-continua/` (carátula y tres subdocumentos en folio continuo) y la muestra económica de `informe3` y de `final` |
| `python3 herramientas/compilar.py unico` | La instancia completa en un solo PDF, en `salida/<instancia>/` |
| `python3 herramientas/compilar.py subdocs` | Un PDF y un Markdown por subdocumento, en `salida/<instancia>/`. En la final, además el ZIP |
| `python3 herramientas/compilar.py subdocs 04 13` | Solo esos subdocumentos (en modo continuo compila todos, porque el folio depende de todos) |
| `python3 herramientas/compilar.py md` | Solo los Markdown |
| `python3 herramientas/compilar.py economico` | Los documentos económicos de la instancia, en `salida/<instancia>-economica/`: en el Informe 3 el documento de costos frente a venta, y en la final los entregables 1 y 2 del Sobre N.º 3 con sus DOCX, la planilla y el ZIP |
| `python3 herramientas/compilar.py limpiar` | Borra `salida/aux/` |

Opciones: `-j N` fija cuántas compilaciones corren en paralelo (por defecto, los núcleos del equipo), `--forzar` recompila todo, `--continuo` y `--por-subdocumento` cambian el modo de folio sin tocar la configuración (la salida va entonces a `salida/<instancia>-continuo/` o `-por-subdocumento/`, para no pisar la entrega), y `--caratula` agrega la carátula del sobre (`SUBDOC00`) cuando el modo es por subdocumento.

La herramienta llama a LuaLaTeX sin interacción. Con `-usepretex`, latexmk arma su propia orden y no usaba la del `.latexmkrc`: ante un error, TeX quedaba esperando una respuesta en la terminal. Ahora el modo sin interacción va explícito y la entrada se cierra.

Cada compilación guarda una huella de `estilo/`, `fuentes/`, `temas/`, `portadas/`, `formularios/`, `configuracion/`, `referencias/`, `figuras/`, de las carpetas del subdocumento y del preámbulo que recibe. Si algo cambió, se fuerza la recompilación. En el formato anterior latexmk no veía los cambios en los archivos comunes y entregaba PDF viejos. Un subdocumento tarda entre 15 y 60 segundos, y los subdocumentos se compilan en paralelo.

## Escribir un subdocumento

Cada subdocumento vive en `subdocumentos/NN-nombre/`. El número, el título y los formularios salen de `configuracion/subdocumentos.tex`, así que la apertura y la portada se arman solas. En `meta.tex` va la descripción que aparece en la ficha:

```latex
\DescripcionFicha{Arquitectura lógica y física, integración, seguridad, despliegue, dimensionamiento y decisiones registradas.}
```

`contenido.tex` empieza con el resumen de apertura y sigue con los títulos:

```latex
\begin{resumenApertura}
Qué resuelve el subdocumento, en cuatro o cinco líneas, con el dato que lo dimensiona.
\begin{recibe}
  \item Lo que recibe el mandante.
\end{recibe}
\end{resumenApertura}

\section{Arquitectura lógica}\label{sec:4-logica}        % 4.1
\subsection{Capas y módulos}\label{sec:4-capas}          % 4.1.1
\subsubsection{Capa de negocio}                          % 4.1.1.1
\paragraph{Servicio de jornada} Texto en la misma línea. % cuarto nivel, sin número
```

La numeración nace del número de subdocumento: el Subdocumento 4 numera 4, 4.1, 4.1.1, también cuando se compila solo. El índice detallado de cada subdocumento, el índice general y el cuerpo salen del mismo archivo, así que no pueden discrepar. Al cerrar el resumen de apertura se imprime el índice detallado del subdocumento con sus figuras y tablas (Artículo 40.4, «en cada documento»), y el contenido sigue en la misma página. Cada subdocumento empieza en página nueva, arriba. Un título arrastra al menos cinco líneas: si no caben, pasa a la página siguiente.

Reglas que el verificador revisa en el fuente:

1. Después de un título va un párrafo. Nunca una tabla o una figura directamente.
2. Toda tabla y toda figura se cita desde el texto con `\tabref{...}` o `\figref{...}`, antes de que aparezca.
3. Después de una tabla va la conclusión que se saca de ella.
4. Lo que falta escribir se deja como `\marcador{qué va aquí}`. En los informes el verificador lo cuenta como aviso y en la final como error.

Las etiquetas tienen que ser únicas en toda la oferta, porque las referencias cruzan archivos. Convención: `sec:4-logica`, `tab:4-planos`, `fig:4-capas`.

## Tablas

Un solo entorno sirve para tablas cortas y largas:

```latex
\begin{tabla}[opciones]{Leyenda de la tabla}{planos}{L{35mm} L{45mm} X}
Plano & Contenido & Por qué \\ \midrule
Nube & ... & ... \\
\end{tabla}
```

Lo que va antes del primer `\midrule` es la cabecera. Una tabla con columna `X` ocupa todo el ancho. Una tabla de ancho natural (solo columnas de ancho fijo, como las del formato anterior) se centra en el espacio disponible. En una tabla larga la cabecera se repite en cada página con «(continuación)» y el pie dice «Continúa en el folio siguiente». Antes de empezar, la tabla reserva ocho líneas para no dejar la cabecera sola al pie. La etiqueta queda como `tab:planos` y se cita con `\tabref{planos}`.

Columnas: `L{ancho}` alineada a la izquierda, `C{ancho}` centrada, `R{ancho}` a la derecha y `X` flexible. Las `p{...}` del formato anterior también quedan alineadas a la izquierda. Opciones: `ancho=completo` (texto más carril, 183,9 mm), `fuente=condensada` (IBM Plex Sans Condensed, para formularios de muchas columnas sin bajar de 9 pt), `filetes=false`, `numerada=false` y `espacio=N` (líneas reservadas antes de la tabla). Bajo una tabla se puede poner `\notaTabla{fuente o aclaración}`.

La leyenda dice lo que la tabla muestra. Una tabla del contenido no se llama «Formulario T-NN»: los formularios reales los imprime `formularios/` al final del subdocumento. La revisión del Informe 1 objetó justamente eso en el Anexo A del Subdocumento 4, una tabla de emplazamiento rotulada «Formulario T-11» que no era el T-11. Si una leyenda nombra un formulario fuera del entorno `formulario`, la compilación deja un aviso y el verificador lo informa en el punto 21, igual que un título con ese nombre.

Lo que no hay que hacer, porque en el formato anterior produjo bucles o PDF de miles de páginas: usar `\extrarowheight`, poner texto largo en un `tabular` común, o definir macros de fila que terminen en `\\`. Tampoco hay que usar `\needspace` antes de una tabla ni en los títulos: reserva espacio con un truco de pegamento que confunde a longtable, que entonces deja una página solo con el pie de la tabla o pone la cabecera de continuación antes del título. El formato usa `\Needspace`, que compara con lo que queda de página.

## Figuras

```latex
\figura{figuras/04-arquitectura/Capas.pdf}{Leyenda}{capas}              % vertical, al ancho de texto
\figura[ancho=completo, alto=0.7]{figuras/...}{Leyenda}{capas}          % ocupa también el carril
\anexoGrafico{figuras/04-arquitectura/Main.pdf}{Leyenda}{fisica}        % página horizontal
\begin{figuraNativa}{Leyenda}{etiqueta} ...TikZ... \end{figuraNativa}   % figura dibujada en LaTeX
```

La figura vertical se ajusta al ancho y al alto útil sin deformarse ni cortarse. El anexo gráfico ocupa una página apaisada y aparece en el índice como «Anexo gráfico 4.A». En modo `pagina` su área va de 12 mm del borde izquierdo a 10 mm del derecho y de 8 mm del borde superior a 22 mm del inferior, sobre el filete del pie. Descontadas la cabeza del anexo y la leyenda, el diagrama dispone de 257,4 por 171 mm con una leyenda de una línea y de 257,4 por 167 mm con dos. Esta es la medida para la que hay que dibujar un diagrama horizontal. El registro de compilación informa el área y la escala de cada anexo en una línea `AUDIT-ANEXO`. En modo `hoja` el área es de 250 por 164 mm. Se imprime al final del subdocumento, después de sus formularios, para no dejar media página vacía donde se lo menciona. El texto lo cita con `\figref`, que da su número. Cada figura va en la sección que la explica, y el texto la cita antes con `\figref{...}`.

**Letra dentro de las figuras.** El Artículo 40.4 pide 9 pt como mínimo también en figuras. Cada figura deja en el `.aux` la escala con que entró al documento y la caja exacta donde quedó en la página. El verificador multiplica la escala por la letra más chica del PDF de origen, o del SVG si está al lado, y además mide en la página final el texto que cae dentro de esa caja. Separar por ubicación, y no por familia de fuente, hace falta desde que los diagramas usan IBM Plex igual que el documento.

**Fuente de los diagramas.** Los diagramas de `D4/canvas-d4` piden IBM Plex, pero `rsvg-convert` los exportaba con Noto Sans porque Plex estaba en TeX Live y no en fontconfig. Ahora los OTF de `/usr/share/texmf-dist/fonts/opentype/ibm/plex/` están enlazados en `~/.local/share/fonts/ibm-plex/` (se rehace con `fc-cache -f`), y `figuras/04-arquitectura/Main.pdf` y `LogicaCapas.pdf` se regeneraron desde sus SVG con `rsvg-convert -f pdf`: `pdffonts` muestra IBMPlexSans, IBMPlexSans-SmBld e IBMPlexMono. Lo que dicen los diagramas no cambió.

Los diagramas actuales tienen letra mínima de 8,5 unidades en un lienzo de 1123 por 794, es decir 6,38 pt a tamaño natural, y no cumplen en ninguna disposición en carta:

| Disposición | Área | Escala | Letra efectiva | `font-size` mínimo en el SVG |
|---|---|---|---|---|
| Figura vertical | 148,9 mm de ancho | 0,50 | 3,19 pt | 23,9 |
| Anexo gráfico horizontal, modo `pagina` | 257,4 por 167 mm | 0,82 | 5,20 pt | 14,7 |

Se midió qué pasa si toda la letra sube al tamaño necesario sin mover nada, con las métricas reales de IBM Plex (`python3 herramientas/letra_diagramas.py figuras/04-arquitectura/Main.svg 257.4 167`):

- **Main, como anexo horizontal.** Letra por 1,78. El texto ocuparía el 11 % del lienzo y chocan siete pares de etiquetas: «Servidor ×2», «Switch ×2», «Firewall ×2» y «Custodia» en la sala técnica, «Propios» con «148», «Terceros» con «226» y «Sin dispositivo» con «34 de 374» en la flota, y la línea de requisitos del pie con «audIT · TFEP-01/2026». Cabe a 9 pt agrandando las cajas y separando esas columnas, sin sacar nada. Es el trabajo pendiente en `build.py`.
- **LogicaCapas, como figura vertical.** Letra por 2,82. El texto ocuparía el 59 % del lienzo, con 128 choques y cuatro etiquetas fuera de él. No cabe a 9 pt en el ancho de texto sin sacar contenido. Las etiquetas que chocan son las descripciones largas de cada capa (por ejemplo «Cuatro perfiles distintos: torre de programación, conductor, terminal y taller, y externos.» y «Único punto público de entrada. Por aquí salen los portales del cliente y del transportista.») con los nombres de sus componentes («Portal web», «App móvil», «CDN», «WAF»). Qué sacar lo decide el equipo. Como anexo horizontal necesitaría letra por 1,78 y chocan 39 pares: cabe redistribuyendo.

## Dispositivos de venta

Cada dispositivo exige su dato verificable y su fuente. Si falta, la compilación se detiene con un error que lo dice.

**Resumen de apertura.** Abre cada subdocumento: qué resuelve y qué recibe el mandante. Responde el reclamo de que el capítulo «parte sin decir cuál es su objetivo». Sigue la práctica de Shipley de abrir cada sección con lo que el evaluador tiene que saber al terminar de leerla.

**Compromiso.** Una obligación medible, numerada C-01, C-02 y así. `\listaCompromisos` los reúne con su folio, por ejemplo en el resumen ejecutivo.

```latex
\begin{compromiso}[metrica={30 s como máximo por asignación},
                   verifica={criterio de aceptación 1 del Caso},
                   fuente={\caso{RT-09.01}{32}}]
Texto de la obligación, en una oración.
\end{compromiso}
```

**Decisión.** Reemplaza las tablas sueltas de registro de decisiones. Numerada D-01 y listada con `\listaDecisiones`.

```latex
\decision{titulo={...}, decide={...}, descarta={...}, criterio={...}, fuente={\transv{RT-05.18}{12}}}
```

**Requisito atendido.** `\req{RT-09.01}` en línea o `\reqMargen{RT-09.01}` en el carril, junto al párrafo que lo cumple. Si el Formulario T-12 trae la fila de ese requisito, el código enlaza a ella. La columna «Sección de la propuesta» del T-12 se completa sola con las secciones que usan el código, y si ningún párrafo lo atiende lo dice.

**Cifra con fuente.** `\cifra{340 de 374}{Caso, numeral 14.1, p. 29}` deja la cifra en el texto y la fuente en el carril. `\cifraMargen{374}{camiones gestionados}{Caso, numeral 14.1, p. 29}` la destaca en el carril. La cifra destacada ocupa unas seis líneas del carril: no se pone en el último párrafo antes de un título, porque las notas de margen no esquivan los números de título.

Quedan fuera del formato, porque se leen como folleto o como texto generado: tarjetas en grilla con ícono, insignias, píldoras, degradados, sombras, emoji, listas con una etiqueta en negrita al inicio de cada viñeta, recuadros de «conclusión clave» y eslóganes en el cuerpo. Las frases del manual de marca van solo en la portada y en la contraportada.

## Citas

Las bases y el Caso no son bibliografía. Se citan en línea por documento, artículo o numeral y página, siempre con la misma forma, y nunca generan entrada en la lista de referencias:

| Comando | Resultado |
|---|---|
| `\art{40.1}{26}` | FEP01, Artículo 40.1, p. 26 |
| `\form{T-7}{57}` | FEP01, Formulario T-7, p. 57 |
| `\transv{numeral 2.1}{6}` | FEP02, numeral 2.1, p. 6 |
| `\caso{numeral 14.1}{29}` | Caso, numeral 14.1, p. 29 |
| `\caso{RT-09.01}{32}` | Caso, RT-09.01, p. 32 |
| `\caso*{numeral 14.1}{29}` | (Caso, numeral 14.1, p. 29) |
| `\bases{FEP01}{Artículo 50.2}{29}` | forma general |

Con más de una página («66 y 67») sale «pp.». La ficha explica una sola vez qué es FEP01, FEP02 y Caso. Las páginas son las impresas en el original, las mismas que da `audIT/tools/buscar.py`.

Las fuentes externas reales (leyes, normas ISO, documentación de un fabricante) van en `referencias/referencias.bib` y se citan en APA 7 con `\parencite{clave}` o `\textcite{clave}`. Aparecen en el anexo «Referencias normativas y técnicas», al final, cada una con el folio donde se usa. Si no hay citas, el anexo no se imprime. El `.bib` actual es una copia de las entradas externas del formato anterior, sin las de la Escuela.

## Formularios

Cada subdocumento incluye al final los formularios que le asigna el Formulario T-21. Cada formulario empieza donde haya lugar para su encabezado, su instrucción y sus primeras filas, sin forzar página nueva. Si su carpeta trae `formularios/T-11.tex`, se usa ese archivo. Si no, se imprime la plantilla vacía con todos sus campos, de modo que ningún formulario puede faltar sin que se note.

| Formulario | Subdocumento | Cómo se llena |
|---|---|---|
| T-6 Experiencia en proyectos similares | 1 | `\begin{formularioTSeis} \proyectoTSeis{nombre=..., cliente=..., industria=..., periodo=..., monto=..., alcance=..., arquitectura=..., servicio=..., volumen=..., rol=..., contacto=...} \end{formularioTSeis}` |
| T-8 Equipo, subcontrataciones y alianzas | 12 | `\rolTOcho{rol=..., nombre=..., certificaciones=..., dedicacion=..., meses=...}` y `\subcontratoTOcho{empresa=..., servicio=..., porcentaje=..., justificacion=...}` dentro de `formularioTOcho` |
| T-9, T-10, T-13, T-14, T-17, T-18 | 6, 9, 7 | `\begin{contenidoExigido}{T-9} \exigencia{exigencia de las bases}{\verSeccionFolio{sec:6-gestion}} \end{contenidoExigido}` |
| T-11 Especificaciones técnicas ofertadas | 4 | `\componenteTOnce{componente=..., producto=..., caracteristicas=..., ubicacion=..., cantidad=..., adquiere=..., ciclo=..., justificacion=...}` dentro de `formularioTOnce` |
| T-12 Matriz de cumplimiento y trazabilidad | 3 | `\requisitoF{id=..., descripcion=..., actor=..., precondicion=..., resultado=..., prioridad=..., origen=..., cumple=..., componente=...}` y `\requisitoNF{id=..., descripcion=..., categoria=..., umbral=..., metodo=..., exigible=..., ...}` dentro de `formularioTDoce` |
| T-15 Nivelación de recursos | 7 | `\etapaTQuince{etapa=..., hh=..., personas=..., frentes=..., meses=...}` dentro de `formularioTQuince` |
| T-16 Plan de riesgos | 8 | `\riesgoTDieciseis{id=..., riesgo=..., categoria=..., probabilidad=..., impacto=..., exposicion=..., mitigacion=..., responsable=...}` dentro de `formularioTDieciseis` |
| T-19 Cartera de innovaciones | 13 | `\fichaInnovacion{tipo=..., nombre=..., problema=..., tecnologia=..., madurez=..., fuentes=..., arquitectura=..., edt=..., mes=..., inversion=..., costooperacional=..., beneficio=..., indicador=..., medicion=..., riesgo=..., mitigacion=..., contingencia=...}`, una por innovación |

Todo archivo de datos va envuelto en su página de formulario:

```latex
\begin{formulario}{T-11}
\begin{formularioTOnce}
  \componenteTOnce{componente=..., producto=..., cantidad=..., ...}
\end{formularioTOnce}
\end{formulario}
```

El T-12 une las columnas del formulario de las bases con los campos que el numeral 17.1 del Caso exige al catálogo: actor, precondición, resultado esperado, prioridad y origen para los funcionales, y categoría, umbral, método de verificación y a quién es exigible para los no funcionales. El T-19 agrupa sus 17 campos en los siete elementos del Artículo 29.

Artículo 50.2: ningún formulario tiene campos de monto. El T-11 no tiene columna de costo, aunque RT-08.10 pide «costo unitario estimado», y una nota remite ese dato al Sobre N.º 3. En el T-19, «Inversión requerida» y «Efecto en el costo operacional» describen las partidas sin montos y el formulario agrega la remisión al Sobre N.º 3 (Artículo 30.1). En el T-6, «Monto del contrato (rango)» remite a la nómina de contratos del Sobre N.º 1 salvo que se escriba `monto={...}`. El T-15 es el único lugar donde se admiten horas hombre, porque ese formulario las pide.

## Tabla del Artículo 46

Cada informe incorpora la resolución de las observaciones de la instancia anterior. Para el Informe 2 van en `anexos/observaciones-informe1.tex`:

```latex
\begin{tablaObservaciones}{Informe 1}
  \grupoObservaciones{General, formalidad y cumplimiento de instrucciones}
  \observacion[sub=0]{01}{Observación}{Respuesta}{Sección modificada}
  \grupoObservaciones{Subdocumento 1, presentación de la empresa}
  \observacion[sub=1, tipo=aclara]{17}{...}{...}{...}
\end{tablaObservaciones}
```

`sub` es el subdocumento al que corresponde la observación (0 para las generales, `E` para las de la propuesta económica). `tipo` es opcional y antepone «Se acepta.», «Se aclara.» o «Se acepta y se aclara.». En el documento único la tabla va completa después del índice. Cuando el informe va en varios PDF, la carátula (`SUBDOC00`) lleva la tabla completa y cada subdocumento abre con sus propias filas. El Informe 3 la lleva completa en el documento de costos frente a venta. En la propuesta final las filas `sub=E` van solo en el entregable 1 del Sobre N.º 3 y el Sobre N.º 2 muestra las demás: el Artículo 50.2 no admite en la oferta técnica nada que permita inferir el monto.

Si el archivo de la instancia todavía no existe, la tabla sale igual, vacía con sus columnas y un marcador, en el documento que lleva la tabla completa. Antes se omitía en silencio, y el Artículo 46 es obligatorio desde el Informe 2.

## Documentos económicos

El Informe 3 y el Sobre N.º 3 son documentos económicos. Tienen la misma identidad visual que la oferta técnica: portada, ficha, hoja resumen, índice detallado hasta el tercer nivel, folio y media firma en todas las páginas, y referencias. El pie y la portada dicen «Propuesta Económica» en el Informe 3 y «Oferta Económica, Sobre N.º 3» en la final.

| Documento | Instancia | Base | Apartados |
|---|---|---|---|
| Costos frente a venta (`economico/costos-venta/`) | `informe3` | T-22, FEP01 p.69 | Proveedores clave, adquisiciones clave, curva S, análisis de costos, VAN y TIR, valorización de las cinco innovaciones y planilla |
| Entregable 1. Propuesta económica formal (`economico/oferta-economica/`) | `final` | E-21, FEP01 pp.70 y 71 | 1.1 Propuesta de valor económico, 1.2 Estructura de pagos (hitos del E-25), 1.3 Resumen ejecutivo de valor |
| Entregable 2. Análisis económico-financiero (`economico/analisis-financiero/`) | `final` | E-21, FEP01 p.71 | 2.1 Costos frente a precio, 2.2 Evaluación financiera, 2.3 Curva S, 2.4 Adquisiciones, 2.5 Costos operacionales (con los perfiles del E-26), 2.6 Mantención y soporte, 2.7 Innovaciones |
| Entregable 3. Modelo financiero | `final` | E-21, FEP01 pp.71 y 72 | La planilla que entrega el mandante. El formato no la genera |

Cada documento trae, después del índice, la página «Tipo de cambio y parámetros» con la tabla del Formulario E-24: el E-21 pide el tipo de cambio «claramente indicado». La hoja resumen va al inicio del sobre (Artículo 40.3): en el documento de costos y en el entregable 1, que lista también las secciones del entregable 2 con su archivo y su folio. En la final el folio sigue del entregable 1 al 2.

**Montos.** Ninguna cifra se escribe a mano. Todas salen de un comando, que imprime el valor en CLP, UF y USD con los tipos de cambio de `configuracion/economico.tex`, el único lugar donde están:

| Comando | Resultado |
|---|---|
| `\monto{40000}` | CLP 40.000 · UF 1,00 · USD 44,44 |
| `\monto[UF]{1}`, `\monto[USD]{1}` | el valor se da en UF o en USD |
| `\montoPartida{implementacion}` | el valor de esa partida de `economico/datos/partidas.csv` |
| `\tablaMontos{leyenda}{etiqueta}{clave1, clave2}` | por cada partida, valor neto, IVA y total en las tres monedas, y el total general (Artículo 51.2). `\tablaMontos*` omite el total general |
| `\tablaHitosPago` | los doce hitos del E-25 con su porcentaje y su monto sobre el valor de la implementación |
| `\tablaParametros` | tipos de cambio y parámetros del E-24 |
| `\tablaTarifas` | costo y tarifa horaria de cada perfil contra el rango del E-26. Un valor fuera de rango detiene la compilación |

Regla de cálculo, la misma en todos los documentos: el valor se lleva a pesos enteros, y de ese valor en pesos se obtienen UF y USD con dos decimales, redondeando la mitad hacia arriba. Se calcula con enteros, sin coma flotante. El IVA se calcula sobre el neto en pesos y se redondea al peso. Las sumas se hacen en pesos, y cada total se convierte después. Por eso un total en UF puede diferir en 0,01 de la suma de sus partes en UF: cada cifra se deriva de su valor en pesos, igual que en una planilla. En la oferta técnica cualquiera de estos comandos detiene la compilación con el texto del Artículo 50.2.

**Una sola fuente de datos.** El E-21 exige que los tres documentos del sobre traigan valores idénticos y declara la discrepancia causal de descalificación. Por eso las cifras salen todas de `economico/datos/partidas.csv`:

```
clave;concepto;moneda;valor;iva;planilla
implementacion;Valor total de la fase de implementación (Etapa 1 y Etapa 2);CLP;;si;Resumen!C5
proyecto;Valor total del proyecto;CLP;=implementacion+operacion;si;
```

`valor` es un número sin separador de miles, vacío si está por completar o una suma de otras partidas. `iva` dice si la partida está afecta a IVA. `planilla` es la celda del modelo financiero del mandante donde va el valor neto en pesos. La plantilla trae las partidas que piden el T-22 y el E-21, todas vacías.

De esa fuente salen los cuatro formatos. LuaLaTeX calcula y compone el PDF, y anota cada cifra impresa en el `.aux` y cada tabla en `<documento>.eco.json`. `tex2md.py` arma el Markdown copiando esas cifras, sin recalcular, y `md2docx.py` arma el DOCX desde ese Markdown. `planilla.py` compara la planilla del mandante con las partidas, celda por celda (`python3 herramientas/planilla.py comparar`), y puede escribir las partidas en una copia de la planilla (`volcar`), sin tocar las celdas con fórmula. El verificador lo repite en cada compilación.

**Planilla.** La entrega el mandante. Se deja en `economico/planilla/`, un solo `.xlsx`, y la herramienta la copia a la salida con su nombre y, en la final, la mete en el ZIP del Sobre N.º 3.

**DOCX.** Los entregables 1 y 2 salen también en DOCX (E-21 y Artículo 40.4). `md2docx.py` escribe el OOXML directamente, sin dependencias, adaptado de `D4/tools-md2docx.py`: carta, IBM Plex, cuerpo de 11 pt, tablas de 9,5 pt, folio abajo a la derecha que empieza en el mismo número que el PDF e índice como campo que Word actualiza al abrir. La media firma va en el PDF, que es la versión firmada. El DOCX se revisa abriéndolo con PyMuPDF y comparando sus cifras con las del PDF. En este equipo no hay Word ni LibreOffice, así que no se probó en ellos (ver lo que queda abierto).

**Nombres de archivo.** Formulario E-21, «sin excepción»: `AUDIT_OfertaEconomica_1_20261125.pdf`, `AUDIT_AnalisisFinanciero_2_20261125.pdf`, sus `.docx` y `AUDIT_ModeloFinanciero_3_20261125.xlsx`, dentro de `SOBRE3_AUDIT_OFERTA_ECONOMICA_20261125.ZIP` (Artículo 51.3). Dos supuestos anotados: el E-21 no fija el formato de la fecha y se usa AAAAMMDD, como en los Artículos 49 a 51, y para el Informe 3, que las bases no nombran, se sigue el patrón de los informes: `INFORME3_AUDIT_COSTOS_VENTA_20261113.pdf` e `INFORME3_AUDIT_PLANILLA_20261113.xlsx`.

## Portada, ficha, hoja resumen y firmas

La portada ocupa dos páginas. La primera es la fotografía con el logo. La segunda es la carátula de texto con la licitación, el título, la instancia, el proyecto, el mandante, el motivo de la ruta y la firma completa. Después vienen la ficha del documento (con su nombre de archivo, sus folios y la convención de citas), la hoja resumen y el índice.

La hoja resumen (Artículo 40.3) se arma con el folio real de cada portada, ficha, subdocumento, formulario, anexo y anexo de referencias. En el documento único sale del `.aux` de la corrida anterior. Con varios PDF la herramienta junta las entradas de todos los archivos.

El folio y la media firma se dibujan en todas las páginas sin excepción, portada incluida, en el extremo inferior derecho, y no dependen del estilo de página. En `configuracion/metadatos.tex` se fijan el representante legal, su RUT y las imágenes de firma. `\ImagenMediaFirma` apunta hoy a la media firma que usó el Informe 1. Si se deja vacío, la zona queda en blanco para firmar sobre el PDF. `\ImagenFirmaCompleta` hace lo mismo con la firma completa de portada y ficha.

## Referencias entre subdocumentos

`\verSeccion{sec:4-fisica}` da «sección 4.2», `\verSeccionFolio{...}` agrega el folio, y `\figref`, `\tabref` y `\refx` funcionan igual en el documento único y entre PDF separados. Cuando el sobre va en varios PDF, la herramienta importa las etiquetas de los otros subdocumentos con xr-hyper y los enlaces abren el archivo correcto dentro del ZIP. En modo por subdocumento el folio de otro archivo no se imprime, porque los folios se repiten entre archivos.

## Markdown

`python3 herramientas/compilar.py md` escribe el equivalente en Markdown de cada subdocumento desde el mismo `contenido.tex`, con la misma numeración de títulos, tablas y figuras. En modo `subdocs` se genera junto a cada PDF. Los formularios se indican al final, porque su versión oficial es la del PDF.

## Traer contenido del formato anterior

```bash
python3 herramientas/migrar.py ../Entrega/contenido/c4.tex 4               # deja el resultado en salida/migracion/
python3 herramientas/migrar.py ../Entrega/contenido/c4.tex 4 --escribir --figuras ../Entrega/assets/images
```

La herramienta quita el `\section` que hacía de capítulo, sube cada título un nivel, cambia las rutas de figuras y agrega un resumen de apertura con marcadores. Deja igual `\figuraAncha`, `tablaAudit`, `\leyendaFont` y `\parencite`, que la capa de compatibilidad resuelve (se activa con la opción `compatibilidad` de la clase, como en la muestra). Informa lo que hay que revisar a mano: citas a las bases sin página, títulos seguidos directamente de una tabla y leyendas o títulos que nombran un «Formulario T-NN» sin ser el formulario. Las tablas del formato anterior que no caben en el texto pasan solas al ancho completo. Se probó con el `c4.tex` entregado: 859 líneas, 41 páginas, sin cajas desbordadas ni errores, y detectó los cinco títulos que van directo a una tabla y la leyenda «Tabla de emplazamiento de componentes. Formulario T-11» del Anexo A.

## Verificar

`python3 herramientas/verificar.py` revisa lo que haya en `salida/` y deja un informe en `salida/verificacion-<grupo>.md`. Sale con código 1 si algún punto no cumple.

| N.º | Punto | Cómo se mide |
|---|---|---|
| 1 | Papel carta y vertical, salvo anexos gráficos declarados | Tamaño y giro de cada página contra los anexos que registra el `.aux` |
| 2 | Folio en todas las páginas, abajo a la derecha, correlativo | Número impreso en el extremo inferior derecho de la página tal como se ve en pantalla, aplicando el giro que declara el PDF, y derecho. No cumple si la cabeza repite «Folio N» |
| 3 | Continuidad entre archivos | En modo continuo, cada PDF empieza donde terminó el anterior |
| 4 | Media firma y folio separados del texto, de los diagramas y entre sí | Posición de la firma, del folio, del texto más bajo y, en páginas con figura, de cada trazo del diagrama |
| 5 | Cuerpo 11 pt, tablas y leyendas 9 pt | Tamaño real de cada fragmento en el PDF, con PyMuPDF, fuera de las cajas de las figuras |
| 6 | Letra de las figuras 9 pt | Letra mínima del origen por la escala, y control en la página del texto que cae dentro de la caja de la figura |
| 7 | Fuentes incrustadas, texto buscable | `pdffonts`, `pdftotext`, búsqueda de palabras con tilde y con ligadura |
| 8 | Sin cajas desbordadas ni referencias sin resolver | Registro de compilación |
| 9 | Figuras y tablas citadas desde el texto | Etiquetas del `.aux` contra las citas del fuente |
| 10 | Ningún título seguido de tabla o figura | Fuente |
| 11 | Residuos prohibidos | Fuente y PDF: Escuela, dupla, nombres del equipo, Proyecto Semestral, meses en inglés, 192 como cantidad de camiones. En los documentos técnicos, además, horas hombre fuera del T-15 y cifras en dinero (Artículo 50.2). En los económicos esa prohibición no se aplica |
| 12 | Hoja resumen coincide con la foliación | Cada entrada contra la página que declara |
| 13 | Nombres de archivo | Patrón de los Artículos 49 a 51. En los económicos, el del E-21 y el Artículo 51.3, los DOCX de los entregables 1 y 2 y la planilla |
| 14 | Contraste de los colores de texto | Relación WCAG sobre blanco |
| 15 | Punto y coma, raya y guion doble | Fuente, como aviso |
| 16 | Marcadores pendientes | Aviso en informes, error en la final |
| 17 | Aperturas arriba de página nueva | Posición del título de cada subdocumento |
| 18 | Títulos al pie | Títulos en las últimas cinco líneas de una página, como aviso |
| 19 | Ninguna tabla deja su cabecera sola al pie | Una tabla cuya leyenda inicial aparece junto a su propia continuación dejó la página anterior solo con su pie |
| 20 | El encabezado nombra el subdocumento de la página | El «Subdocumento N» del encabezado o de la cabeza del anexo contra el subdocumento al que pertenece la página según los folios de inicio del `.aux`. Las páginas preliminares no nombran ninguno |
| 21 | Ninguna tabla ni título se llama «Formulario T-NN» sin serlo | Aviso del registro para las leyendas de tabla fuera del entorno `formulario`, y títulos del contenido, como aviso |
| 22 | Montos en CLP, UF y USD con el tipo de cambio del E-24 (solo económicos) | La configuración contra los valores del E-24, cada monto recalculado desde su valor en pesos, el tipo de cambio impreso en cada documento, y ninguna cifra en dinero en el PDF que no haya salido de un comando de montos |
| 23 | Neto, IVA desglosado y total general (solo económicos) | IVA de cada partida contra la tasa del E-24, total igual a neto más IVA, y una tabla con IVA en cada documento |
| 24 | Valores idénticos en PDF, DOCX y planilla (solo económicos) | Cada DOCX abierto con PyMuPDF trae las mismas cifras que su PDF, cada partida se imprime igual en todos los documentos y cada celda declarada de la planilla coincide con `partidas.csv` |

## Decisiones de diseño

**LuaLaTeX.** Es más lento que XeLaTeX, pero microtype hace en él protrusión y expansión, y cada ligadura queda con su equivalencia Unicode: «flota» y «ficha» se buscan en el PDF. En los PDF del Informe 1 esas palabras se extraían como «ota» y «cha». La lentitud se compensa compilando en paralelo y solo lo que cambió.

**Una familia, IBM Plex.** El manual de marca prescribe IBM Plex Sans y los diagramas usan Plex Sans y Plex Mono. El cuerpo va en IBM Plex Serif 11 pt, que tiene ojo medio grande y se lee bien en pantalla, que es donde la comisión lee un sobre electrónico. Títulos, tablas, leyendas, encabezado y pie van en Plex Sans. Los códigos de requisito van en Plex Mono y los formularios densos en Plex Sans Condensed. Se consideraron Source Serif, Libertinus y TeX Gyre Pagella: Libertinus entra más angosta, pero rompe la familia visual con la marca y los diagramas.

**Puntos del PDF.** Todos los tamaños se dan en `bp`, el punto de PostScript y de los procesadores de texto. El punto de TeX es algo menor: un cuerpo de «11pt» mide 10,96 en el PDF y quedaría bajo el mínimo. Por la misma razón la expansión de microtype solo estira y nunca comprime: una línea comprimida 1 % se mide como letra de 10,89 pt.

**Página.** El ancho de texto es de 148,9 mm, unos 82 caracteres por línea en promedio. Butterick recomienda 45 a 90 y Bringhurst 45 a 75. El formato empezó en 72 y subió a 82 para reducir el margen sin uso, como se pidió. Para volver a 75 basta `left=52mm, right=27.9mm` en `estilo/pagina.sty`. El margen izquierdo de 47 mm incluye un carril de 28 mm donde cuelgan los números de título, los códigos de requisito y las cifras con fuente. Las páginas preliminares (ficha, hoja resumen, índice, observaciones y referencias) no tienen números colgados y ocupan también el carril, desde 12 mm del borde, con el entorno `paginaAncha`. Solo el subdocumento fuerza página nueva: después del índice detallado el contenido sigue en la misma página, los formularios empiezan donde haya espacio y los anexos gráficos van al final. El interlineado es de 14,5 sobre 11 (1,32) y el alto de texto es una grilla exacta de 47 líneas, de 17 mm del borde superior a 23 mm del inferior. Cada párrafo lleva sangría de primera línea salvo el primero tras un título, sin espacio entre párrafos, como pide Butterick (sangría o espacio, no ambos). El encabezado va a 10 mm del borde superior y el pie a 8 mm del inferior, con la media firma y el folio en zonas propias que nunca tocan el texto.

**Folio fuera del estilo de página.** El folio y la media firma se dibujan en el gancho de salida de cada página. En el formato anterior el estilo `plain` del índice movía el folio al centro, y un `\pagenumbering` dejaba la portada sin folio. Aquí ningún estilo de página puede quitarlo ni moverlo. Hay una sola secuencia arábiga desde la portada, sin números romanos.

**Encabezado con marcas.** El número de subdocumento del encabezado viaja con la página como una marca de LaTeX, igual que el título de la sección, y no se lee de una variable. TeX arma cada página después de haber leído el texto que sigue, así que una variable ya tiene el valor del subdocumento siguiente cuando se imprime la última página del anterior. Eso pasaba en el documento único del Informe 2: la última página de los subdocumentos 1 a 8 decía el número del siguiente. La misma causa anotaba el conteo de figuras de un subdocumento al siguiente, y el índice detallado del Subdocumento 4 de la muestra salía sin su lista de figuras. Ahora el número se fija en la apertura, después de cerrar el anterior, y el punto 20 del verificador compara cada encabezado con la página.

**Color contenido.** El marino del manual (#0F2A43) lleva todo el texto de marca. El turquesa (#18B7C7) tiene contraste 2,43:1 sobre blanco, insuficiente para texto chico, así que se usa solo en filetes, en los nodos del motivo y sobre fondo marino, donde llega a 6,03:1. El gris claro (#E6EDF2) es el fondo de cabeceras de tabla. La paleta por dominio de los diagramas queda reservada para figuras. `temas/grises.tex` permite revisar la impresión en blanco y negro.

**Motivo gráfico.** Una línea con los cinco terminales de Transportes Curimón ubicados según su latitud, de Antofagasta a Puerto Montt, con San Bernardo como el nodo hexagonal del logo. Va en la carátula, en la cabeza de cada apertura y en la contraportada.

**Tablas con longtable.** Se prefirió `longtable` y `xltabular` a `tabularray` porque compilan más rápido, aceptan sin cambios las tablas del formato anterior y su comportamiento con cabeceras repetidas es conocido. Toda tabla es larga, así que ninguna se corta ni entra en bucle por crecer. La leyenda no usa `\caption`: longtable la centra respecto del bloque de texto y en las tablas que ocupan el carril quedaba corrida. Se arma como primera fila de la tabla, así que siempre arranca en su borde izquierdo, y la numeración la lleva longtable.

**Numeración desde el subdocumento.** El capítulo es el subdocumento y su contador se fija con el número del catálogo, en ambos modos de compilación. Tablas y figuras numeran por subdocumento (Tabla 4.3).

**Portada en dos páginas.** La fotografía va sola, con el logo, porque es la imagen que la comisión ya valoró. Los datos de la licitación, el título y la firma completa van en la carátula siguiente, todo como texto seleccionable. La `Portada.png` del manual traía el texto rasterizado y no se usa.

**Muestra sin contenido.** La muestra ejercita cada componente con marcadores. Los únicos extractos copiados tal cual son los que hacen falta para probar comportamiento: la tabla larga, los dos diagramas y tres filas del Artículo 46.

## Resultado de la verificación

Resultado de la última compilación, comparado con la línea base guardada al empezar esta corrección (`salida/linea-base/`). Todo lo que cumplía sigue cumpliendo.

| Grupo | Páginas | No cumple | Aviso | Diferencia con la línea base |
|---|---|---|---|---|
| `muestra` | 25 | 6 (letra de las figuras) | 9, 16 | Puntos nuevos 20 y 21 cumplen. El 2 ahora mide el folio como se ve |
| `muestra-continua` | 34 en 4 PDF | 6 | 9, 16 | Igual que la muestra. En la línea base, con el anexo en modo `hoja`, el punto 2 nuevo no cumplía en el folio 22 |
| `informe2-unico` | 33 | ninguno | 9, 16 | La línea base tenía el número de subdocumento equivocado en ocho encabezados (punto 20 nuevo) |
| `informe2` (10 PDF por subdocumento) | 55 | ninguno | 9, 16 | Sin cambios |
| `informe2-continuo` (carátula y 10 PDF) | | ninguno | 9, 16 | Nuevo |
| `muestra-economica-informe3` | 13 | ninguno | 13, 16, 24 | Nuevo |
| `muestra-economica-final` (entregables 1 y 2) | 24 | ninguno | 13, 16, 24 | Nuevo |

| Punto | Estado | Explicación |
|---|---|---|
| 6. Letra de las figuras | No cumple | Ver la sección Figuras: Main puede llegar a 9 pt redistribuyendo, LogicaCapas vertical no sin sacar contenido |
| 9. Figuras y tablas citadas | Aviso | Las tablas de los formularios vacíos no se citan desde el texto |
| 13 y 24. Planilla | Aviso | La planilla la entrega el mandante. Sin ella la salida no la trae y la comparación con el modelo financiero queda pendiente |
| 16. Marcadores | Aviso | La muestra y las plantillas están hechas de marcadores, a propósito |

En el registro de LuaTeX aparece el mensaje «ignored: Infinite glue shrinkage found in box being split» cuando una tabla larga cruza de página. Lo produce longtable incluso en un documento mínimo. Es informativo y no afecta el PDF.

## Lo que queda abierto

Lo que no se pudo resolver desde el formato:

1. **Letra de los diagramas (tarea 5, a medias).** Hecho: IBM Plex visible para fontconfig, respaldo de `D4/canvas-d4/` en `salida/respaldos/canvas-d4-20260927.tar.gz`, los dos PDF que usa el formato regenerados con Plex y el cálculo de qué choca a 9 pt. Falta: redistribuir Main en `build.py` para el área de 257,4 por 167 mm (cabe sin sacar nada) y que el equipo decida qué sacar de LogicaCapas o si pasa a anexo horizontal. `build_logica.py` y `build_d3.py` no se tocaron.
2. **DOCX sin probar en Word.** Es XML bien formado, sigue el orden de elementos del esquema OOXML y PyMuPDF lo abre con las mismas cifras que el PDF. En este equipo no hay Word ni LibreOffice para abrirlo.
3. **Mensaje de longtable en tablas largas.** Descrito arriba. No tiene efecto en el resultado.

Lo que tiene que decidir el equipo:

1. **Carátula `SUBDOC00` en los informes.** En modo por subdocumento la herramienta la genera cuando existe la tabla de observaciones, con la tabla completa del Artículo 46 y la hoja resumen. El patrón de nombres del Informe 1 no tenía un archivo 00. Si no se entrega, las observaciones generales (fila `sub=0`) no quedan en ningún subdocumento.
2. **Monto del T-6.** El formulario de las bases pide «Monto del contrato (rango)». El formato remite a la nómina del Sobre N.º 1 para no poner cifras de dinero en la oferta técnica. El profesor aceptó rangos en el Informe 1.
3. **Porcentaje del valor en el T-8.** Se dejó la columna «% del valor» que trae el formulario. Es una proporción, no un monto, pero combinada con el Sobre N.º 3 permite calcular lo que se paga a cada subcontratista.
4. **Horas hombre en el T-15.** Las bases las piden en ese formulario, y la revisión del Informe 1 las objetó en el Subdocumento 13 por el Artículo 50.2. El formato las admite solo en el T-15.
5. **Datos del representante legal.** Nombre, RUT del representante, RUT de la empresa e imagen de firma completa están como marcadores en `configuracion/metadatos.tex`. La media firma usa la imagen del Informe 1.
6. **Largo de línea.** 82 caracteres tras el pedido de reducir márgenes. El encargo original fijaba 75 como máximo. Se vuelve a 75 con dos valores en `estilo/pagina.sty`.
7. **Referencias externas.** `referencias/referencias.bib` copia las entradas del formato anterior. La Ley 21.719 figuraba con autor distinto en el Subdocumento 5 (Ministerio de Hacienda) y en el 13 (Congreso Nacional de Chile). Conviene revisar cada entrada contra su fuente antes de citarla.
8. **Nombres del Informe 3.** Las bases no nombran sus archivos. Se usa `INFORME3_AUDIT_COSTOS_VENTA_20261113.pdf` e `INFORME3_AUDIT_PLANILLA_20261113.xlsx`, siguiendo el patrón de los informes. En el E-21 la fecha va como AAAAMMDD porque el formulario no la fija.
9. **Fecha de referencia del tipo de cambio.** El E-21 la pide y el E-24 no la da. `\FechaTipoCambio` en `configuracion/economico.tex` está vacío y se imprime como marcador.
10. **Folio del Sobre N.º 3.** En la final el folio sigue del entregable 1 al 2, como en el Sobre N.º 2. El E-21 pide «numeración correlativa en cada documento», que esto también cumple. Si el equipo prefiere que cada documento empiece en 1, basta `--por-subdocumento`.
11. **IVA de los costos.** Las partidas de costo vienen con `iva=no` y la tabla dice «no aplica». Si alguna debe llevar IVA desglosado, se cambia en `partidas.csv`.

## Fuentes consultadas

Propuestas técnicas y comerciales:

- Shipley Associates. *Do your theme statements pass the litmus test?* https://www.shipleywins.com/blogs/do-your-theme-statements-pass-the-litmus-test. Se aplicó en el resumen de apertura: cada sección abre con lo que el evaluador debe retener, y el beneficio va ligado a un rasgo verificable.
- Shipley Associates. *Discriminators and theme statements.* https://www.shipleywins.com/training/discriminators-and-theme-statements. Base de la regla «sin dato verificable no hay dispositivo».
- Winning the Business. *APMP best practice 101: how to write a good executive summary.* https://winningthebusiness.com/apmp-best-practice-101s-how-to-write-a-good-executive-summary/. La estructura de cinco bloques y la regla de sostener cada beneficio con una prueba. El bloque de costos queda en el Sobre N.º 3 por el Artículo 50.2.
- APMP. *Body of Knowledge.* https://bok.apmp.org/about-the-bok/. Relación entre rasgo, beneficio y prueba, que da forma al compromiso (métrica, verificación y fuente).

Tipografía y legibilidad:

- Butterick, M. *Practical Typography*, «Line length» y «Summary of key rules». https://practicaltypography.com/line-length.html. Largo de 45 a 90 caracteres, interlineado de 120 a 145 %, sangría o espacio entre párrafos, no ambos.
- Bringhurst, R. *The Elements of Typographic Style*. Medida de 45 a 75 caracteres con 66 como ideal.
- W3C. *Web Content Accessibility Guidelines 2.1*, criterio 1.4.3. Contraste mínimo de 4,5:1 para texto, usado para decidir el uso del turquesa.

Paquetes:

- Schlicht, R. *The microtype package.* https://ctan.org/pkg/microtype. Protrusión y expansión en LuaTeX, y las opciones `stretch` y `shrink`.
- Documentación de `titlesec` y `titletoc`, `longtable`, `xltabular`, `tcolorbox`, `fancyhdr`, `pdflscape`, `xr-hyper`, `biblatex-apa` y `fontspec`, en su versión de TeX Live 2026.
- Kernel de LaTeX, ganchos `shipout/foreground` y `cmd/<comando>/before`, usados para el folio y para el arrastre de líneas tras cada título.

Compras públicas en Chile: la búsqueda en ChileCompra no dio convenciones de formato más allá de las bases de cada licitación (copias legibles, firma del representante, documentos vigentes). El formato se guía por las bases TFEP-01/2026.
