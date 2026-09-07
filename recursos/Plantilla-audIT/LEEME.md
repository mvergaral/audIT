# Plantilla de entregas audIT

Estructura reutilizable para las cuatro entregas de la Licitación TFEP-01/2026, Caso 10.
Cada uno de los catorce subdocumentos vive en su propia carpeta y se compila como PDF
independiente, que es lo que exige el CLIENTE desde el Informe 1.

## Cómo se usa

**Compilar.** Desde la raíz del proyecto.

```bash
./herramientas/construir.sh              # todos los subdocumentos
./herramientas/construir.sh 04 13        # solo esos dos
./herramientas/construir.sh --limpiar    # borra archivos intermedios
```

Los PDF quedan en `salida/`, ya nombrados como `NN-audIT-SubdocNN.pdf`.

**Generar las versiones Markdown.**

```bash
python3 herramientas/tex2md.py           # todos
python3 herramientas/tex2md.py 04        # solo ese
```

**Crear un subdocumento nuevo.**

```bash
./herramientas/nuevo-subdocumento.sh 15-anexo "Anexo Técnico" "Sub. 15 Anexo" "Descripción breve."
```

## Cómo se cambia de entrega

Se edita **un solo archivo**, `comun/instancia.tex`, y los catorce subdocumentos quedan
actualizados. Las tres líneas que cambian entre informes son la instancia, la versión y la
fecha. El propio archivo trae comentados los valores de las otras entregas.

```latex
\newcommand{\laInstancia}{Informe Preparatorio 2. Oferta Técnica Sobre N.º 2}
\newcommand{\laVersion}{2.0}
\newcommand{\laFecha}{...}
```

## Qué hay dónde

| Ruta | Contenido |
|---|---|
| `comun/instancia.tex` | Datos de la entrega. **El único archivo que se edita al cambiar de informe** |
| `comun/preambulo.tex` | Paquetes, colores de marca, formato de títulos, encabezado y pie |
| `comun/portada.tex` | Macros de portada y de ficha del documento |
| `comun/inf-pucv.cls` | Clase base del formato de la Escuela |
| `comun/styles.sty` | Estilos, tabla `tablaAudit` y figura horizontal `figuraAncha` |
| `comun/referencias.bib` | Bibliografía compartida en norma APA |
| `comun/bibliografia.md` | La misma bibliografía para las versiones Markdown |
| `comun/assets/portada.jpeg` | Portada de la empresa |
| `comun/assets/figuras/` | Diagramas en PDF vectorial |
| `comun/mapa-entregas.md` | Qué subdocumento va en cada informe y cómo cambian las exigencias |
| `subdocumentos/NN-nombre/` | Un subdocumento. Contiene `meta.tex`, `contenido.tex` y `main.tex` |
| `salida/` | PDF y Markdown generados. `salida/aux/` guarda los intermedios y los logs |

## Anatomía de un subdocumento

Tres archivos por carpeta.

**`meta.tex`** define número, título, título corto para el encabezado y descripción para la
ficha. Es lo único que distingue un subdocumento de otro a nivel de portada.

**`contenido.tex`** es donde se escribe. Empieza con un `\section{}` que se renderiza en
grande y sigue con `\subsection{}` y `\subsubsection{}`.

**`main.tex`** es idéntico en los catorce y no hay que tocarlo.

## Recursos disponibles al escribir

**Tabla.** Cuerpo a 10 puntos, se parte entre páginas sin problema.

```latex
\begin{tablaAudit}{Leyenda de la tabla}{etiqueta}{@{}p{4cm}p{9cm}@{}}
\textbf{Columna} & \textbf{Otra} \\ \midrule
Dato & Dato \\
\end{tablaAudit}
```

**Figura a página completa en horizontal.** Para diagramas anchos.

```latex
\figuraAncha{NombreArchivo.pdf}{Leyenda de la figura}{etiqueta}
```

El archivo se busca en `comun/assets/figuras/`, sin ruta.

**Cita en APA.** `\parencite{clave}` con las claves de `comun/referencias.bib`.

## Convenciones de redacción acordadas

Sin punto y coma. Sin raya em ni guion doble. Sin repetir explicaciones que ya se dieron.
Toda afirmación sobre las bases se cita con documento, numeral o código de requisito y
página, según la numeración impresa al pie del original. Toda cifra que no venga de las
bases lleva su derivación, porque el numeral 14.2 del Caso evalúa como dimensionamiento no
realizado cualquier valor entregado sin ella.

## Estado actual

Escritos y compilando con contenido real, los subdocumentos 1, 2, 3, 4, 5 y 13, que son los
del Informe 1.

Los ocho restantes tienen la carpeta creada, la portada funcionando y un `contenido.tex`
que lista las exigencias del Formulario T-7 para ese subdocumento, en forma de
comprobación. Compilan desde ya, con cuatro páginas cada uno, para que la estructura esté
disponible antes de escribir.
