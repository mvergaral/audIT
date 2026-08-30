# Notas para Claude

Trabajo de investigación del ramo ICI-5444 (PUCV). Caso 10, **Transporte de Carga**,
licitación ficticia TFEP-01/2026. El entregable es un informe de 10 a 15 páginas más
una presentación, para el **21 de septiembre de 2026**.

El repositorio no es de software: el código que hay (`tools/`) existe solo para poder
consultar las bases. El producto final es el informe.

## Regla principal: no leer el corpus completo

Los tres documentos de las bases suman ~100.000 tokens. **Nunca los leas enteros ni
los adjuntes.** Para cualquier consulta, empieza por:

```bash
./tools/buscar.py "términos de la consulta"
```

Cuesta ~330 tokens y devuelve extractos con su cita. Para ver una sección completa
(~380 tokens):

```bash
./tools/buscar.py -v A:45      # por artículo
./tools/buscar.py -v 304       # por id de sección
```

Solo si de verdad hace falta más contexto, abre el `.md` con `sed -n '1200,1260p'`.
Leer un `.md` completo son 30.000 tokens y casi nunca se justifica.

Los PDF originales **no están en el repo** y no debes intentar leerlos aunque
aparezcan localmente: son escaneos de 88 MB sin capa de texto.

Otras opciones útiles: `-o` (cualquiera de las palabras), `-p` (frase literal),
`-f FEP01|FEP02|FEP03` (un documento), `-l` (mapa por capítulos, ~750 tokens, sirve
para orientarse al empezar).

## Cómo citar

Cada resultado trae documento, página, tipo y número. Cita así: `FEP01 · Artículo 35°
· p.24`. Los `.md` llevan marcadores `<!-- ===== página N / M ===== -->` que
corresponden a la página del PDF original, así que la cita es verificable contra el
documento impreso.

## Qué hay dónde

| | |
|---|---|
| `texto/FEP01_…md` | Bases Administrativas — 77 pág., 94 artículos, garantías, plazos, evaluación |
| `texto/FEP02_…md` | Bases Técnicas Transversales — 51 pág., requisitos RT-xx comunes a todas las industrias |
| `texto/FEP03_…md` | Bases Técnicas del Caso 10 — 49 pág., la empresa, la operación, las entrevistas |
| `texto/Indicaciones…txt` | reglas del trabajo: formato, extensión, entrega |
| `texto/INDICE.md` | listado de las 377 secciones |
| `equipo/asignacion-duplas.md` | quién hace qué, con las ponderaciones verificadas |

La ponderación de la evaluación técnica está en `FEP01 p.67`
(`./tools/buscar.py -v 172`). Es la tabla que decide cuánto vale cada subdocumento, y
los pesos **cambian entre el Informe 1, el Informe 2 y la ponderación final**. Al
razonar sobre esfuerzo o prioridades, di siempre a qué informe corresponde el
porcentaje.

## Las herramientas

- `tools/pdf_ocr.sh` — PDF escaneado a Markdown. Solo se corre si cambian los PDF.
- `tools/page_to_md.py` — reconstruye una página: tablas por detección de filetes,
  párrafos y listas por geometría, y reglas de corrección de OCR.
- `tools/buscar.py` — índice FTS5 que se arma en memoria en cada invocación. No se
  persiste a propósito: muchos visores de SQLite vienen sin el módulo fts5.

Si tocas las reglas de corrección de OCR en `page_to_md.py`, **verifica siempre la
regla contra todo el corpus antes de aplicarla**. Así se hicieron las que ya están: se
contaron las apariciones y se revisaron los contextos para descartar falsos positivos.
Un caso concreto: los porcentajes sin espacio (`17%`) son pesos de evaluación
legítimos y una regla de ordinales ingenua los habría destruido.

## Estado del texto

177 páginas, 208 tablas, 4.507 celdas, cero filas malformadas. Quedan dos rarezas
conocidas y sin corregir: el signo `≈` se leyó como `=` en 3 lugares (`las = 6.000
vigencias`) y `m²` como `m?` en 2.

## Convenciones

- Todo en español, incluidos comentarios y mensajes de commit.
- Los porcentajes y cifras del caso se citan con su fuente; no los repitas de memoria
  sin verificarlos con `buscar.py`.
