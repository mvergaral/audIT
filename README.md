# audIT — Trabajo de investigación ICI-5444

Caso 10 · **Transporte de Carga** · Licitación TFEP-01/2026
Taller de Formulación de Proyectos Informáticos · Escuela de Informática · PUCV

Este repositorio contiene el texto de las bases de licitación —extraído por OCR desde
los PDF escaneados— junto con las herramientas para buscarlo, y el material de trabajo
del equipo.

## Por qué existe

Las bases vienen en tres PDF de 88 MB en total, escaneados y con marca de agua: no
tienen capa de texto, así que no se pueden buscar, copiar ni citar. Este repo resuelve
eso: el texto completo está en `texto/`, en Markdown, con las tablas reconstruidas y
un marcador de página en cada salto para poder citar contra el PDF original.

## Estructura

```
texto/            el texto de las bases, en Markdown
  FEP01_…md         Bases Administrativas (77 pág., 94 artículos)
  FEP02_…md         Bases Técnicas Transversales (51 pág.)
  FEP03_…md         Bases Técnicas del Caso 10 (49 pág.)
  Indicaciones…txt  Indicaciones del trabajo de investigación
  INDICE.md         listado de las 377 secciones del corpus
tools/
  pdf_ocr.sh        PDF escaneado -> Markdown
  page_to_md.py     reconstrucción de una página (tablas, títulos, listas)
  buscar.py         búsqueda sobre el corpus
equipo/
  asignacion-duplas.md   quién hace qué, con las ponderaciones verificadas
```

## Buscar en las bases

Es lo que vas a usar el 95 % del tiempo. No hace falta instalar nada: `buscar.py` solo
usa la biblioteca estándar de Python.

```bash
./tools/buscar.py "boleta de garantía"      # todas las palabras, en la misma sección
./tools/buscar.py -o multa sanción          # basta con que aparezca una
./tools/buscar.py -p "punto ciego"          # la secuencia literal
./tools/buscar.py -f FEP02 observabilidad   # limitar a un documento
./tools/buscar.py -v A:45                   # ver el Artículo 45 completo
./tools/buscar.py -v 304                    # ver una sección por su id
./tools/buscar.py -l                        # mapa por capítulos
```

Ignora acentos: `metricas` encuentra `métricas`. Cada resultado trae documento, página
e id, así que la cita al informe sale directa.

Si prefieres SQL, `tools/buscar.py -r` deja un `texto/secciones.db` con una tabla
normal (`seccion`) que se abre en cualquier visor:

```bash
sqlite3 -header -column texto/secciones.db \
  "select id,doc,pagina,num,titulo from seccion where tipo='artículo' limit 20;"
```

## Regenerar el texto desde los PDF

Solo hace falta si cambian los PDF originales. **No están en el repo** (88 MB): hay que
copiarlos a la raíz del proyecto, con sus nombres originales, desde el material del
curso.

```bash
sudo pacman -S --needed poppler imagemagick tesseract tesseract-data-spa \
                        python-numpy python-pillow
./tools/pdf_ocr.sh -m *.pdf
```

En Debian o Ubuntu los paquetes son `poppler-utils imagemagick tesseract-ocr
tesseract-ocr-spa python3-numpy python3-pil`.

Tarda unos 2 minutos para las 177 páginas, usando todos los núcleos. Los scripts
verifican sus dependencias al arrancar y dicen qué falta.

## Cómo funciona el OCR

Vale la pena saberlo si algún día hay que tocarlo:

- **La marca de agua** se elimina binarizando por el canal mínimo de RGB, no por el
  gris de luminancia. "CONFIDENCIAL" es gris neutro y desaparece; los títulos dorados
  tienen el canal azul casi negro y sobreviven. Con gris normal el umbral se llevaría
  los títulos junto con el sello.
- **Las tablas** están enrejadas en el original, así que la estructura se recupera de
  los propios filetes y cada celda se lee por separado. Salen como tablas Markdown
  reales: 208 tablas, 4.507 celdas, ninguna fila malformada.
- **Las listas y los párrafos** se reconstruyen por geometría. El glifo de viñeta no
  sobrevive al OCR, así que se detecta buscando tinta en el margen.
- **Las confusiones sistemáticas** de tesseract se corrigen con reglas verificadas
  contra todo el corpus: el signo ordinal (`Artículo 32°` salía `32*`), los números
  romanos de los índices, `ISO`/`IEC`, y el signo de número.

## Fechas

- **Lunes 21 de septiembre de 2026** — entrega del informe (10 a 15 páginas) y la
  presentación, impresos y por correo.
- El asunto del correo va como `[ICI544] - Nro. Empresa - nombre de la empresa y el
  código del tema`.
- Sin el anexo de declaración de uso de inteligencia artificial la entrega no se
  recibe conforme.
