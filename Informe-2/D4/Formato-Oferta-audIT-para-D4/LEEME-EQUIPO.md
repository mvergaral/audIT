# Formato de la oferta, para el equipo

Formato LaTeX de la oferta de audIT para la licitación TFEP-01/2026. Cada subdocumento se escribe
dentro de él. La guía completa está en `GUIA.md`.

## Antes de empezar

- Hace falta TeX Live con LuaLaTeX, latexmk y biber, Python 3 y las utilidades de poppler
  (`pdfinfo`, `pdftotext`, `pdffonts`). Las fuentes IBM Plex vienen con TeX Live. Se probó en
  Linux.
- Una sola vez, desde esta carpeta: `./herramientas/preparar.sh`. Instala lo que usa el
  verificador.
- Para ver cómo queda sin compilar nada, abre `salida/muestra.pdf`.
- Lee `GUIA.md` antes de escribir. Si trabajas con un agente, que la lea completa primero.

## Para trabajar en paralelo sin pisarse

1. Cada uno edita solo la carpeta de su subdocumento, `subdocumentos/NN-nombre/`. No se tocan
   `estilo/`, `configuracion/`, `formularios/`, `portadas/`, `temas/` ni `herramientas/`. Si algo
   del formato no sirve, se avisa a quien lo mantiene en vez de cambiarlo.
2. Las etiquetas tienen que ser únicas en toda la oferta. Usa el número de tu subdocumento como
   prefijo: `sec:4-logica`, `tab:4-planos`, `fig:4-capas`.
3. Para compilar solo lo tuyo: `python3 herramientas/compilar.py subdocs 04`.
4. Antes de entregar: `python3 herramientas/verificar.py`. No debe quedar ningún punto que no
   cumpla.
5. **Lo que escriba un agente lo revisa una persona antes de entregarlo.** La comisión avisó que
   en el Informe 2 cualquier indicio de inteligencia artificial sin revisar hace que el
   subdocumento completo se tenga por no presentado. El verificador revisa formato y residuos, pero
   no detecta prosa con tono de IA.

## Pendientes conocidos

- Los diagramas todavía no llegan a 9 pt, el mínimo del Artículo 40.4 para figuras. Por eso el
  punto 6 del verificador no cumple. Hay que redibujarlos. Mientras tanto se pueden incluir y
  escribir el texto que los cita.
- La tabla de observaciones del Artículo 46 para el Informe 2 va en
  `anexos/observaciones-informe1.tex`, con el formato que explica la guía. El borrador con las 100
  observaciones y sus respuestas está en `anexos/tabla-art46-informe1-borrador.md`. Ese borrador
  trae una nota interna al inicio que no se entrega. Las filas 05, 12, 94 y 100 citan la
  observación con palabras que el verificador marca como residuo prohibido: «Escuela»,
  «duplas» y «horas hombre». Al pasarlas a la tabla, redáctalas sin esas palabras, por ejemplo
  «la unidad académica» u «organización interna del equipo».
- Los datos del representante legal en `configuracion/metadatos.tex` están por definir.
