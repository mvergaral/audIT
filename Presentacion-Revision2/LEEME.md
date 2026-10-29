# Presentación Revisión 2

Abrir `index.html` en Chrome o Edge. Los activos son locales; no necesita conexión. Si el navegador restringe la carga de archivos locales, ejecutar `ABRIR.cmd` y abrir http://127.0.0.1:4318/ . La consola del servidor debe permanecer abierta durante la exposición.

## Manejo (estas instrucciones no aparecen en pantalla)

- Flecha derecha, espacio, Enter, PageDown o clic: siguiente revelación o diapositiva.
- Flecha izquierda, Backspace, PageUp o clic derecho: revelación anterior; al llegar al inicio, diapositiva anterior.
- F: alternar pantalla completa. Escape conserva el comportamiento de salida de pantalla completa del navegador.
- B: abrir el respaldo técnico. Escape: volver al punto de la presentación principal.
- Home: inicio de la secuencia actual. End: última diapositiva de la secuencia actual.
- P: modo presentador integrado, con notas privadas y una ventana de audiencia. Compartir solamente la audiencia. Para una exposición con una pantalla, usar F.

No hay botones, menús, instrucciones ni barras visibles en la superficie de exposición.

## Material

- 26 láminas principales en tres actos, 14 minutos y 49 segundos objetivo y 11 segundos de margen:
  - Apertura: contexto operacional y síntesis visual de cinco grupos de correcciones del Informe 1 (matriz Art. 46, fuentes vigentes del repositorio).
  - Acto 1, «Qué construimos»: contexto en tres planos, ocho capas, verificación en 30 s, arquitectura física, equipo a bordo, datos y operación sin enlace (S4, S5, T-11).
  - Acto 2, «Cómo lo ejecutamos»: EDT en tres niveles, carta Gantt de la red T-15 con Monte Carlo por hito, simulación de atraso de A09, G13 y transición (S7, T-14, T-15, S8).
  - Acto 3, «Cómo lo protegemos»: mapa P×I de los 28 riesgos, los siete de exposición alta, corbatín de R-28 con AMFE, y reservas y holguras (S8, T-16).
- 21 láminas de respaldo: registro completo de riesgos, AMFE, árbol de fallas, R-28, implantación, hitos, reversión, calidad, correcciones, innovaciones, límites y diccionario EDT.
- El respaldo no se muestra en el recorrido: se abre con B si una pregunta lo requiere; dentro, un número seguido de Enter salta a esa lámina. Escape vuelve.
- El puntero del mouse está visible y se oculta tras 4 segundos sin moverlo.
- `GUION-5-EXPOSITORES.md`: texto oral y relevos para cinco personas. `NOTAS-EXPOSICION.md`: notas por lámina.
- `construir.py` lee los formularios vigentes del repositorio (T-14, T-15, T-16, S4, S5, S7, S8, T-19 en `recursos/Formato-Oferta-audIT/salida/informe2/`) y regenera todo con `python3 construir.py`. Requiere Python 3; no usa paquetes externos.
- La versión original del compañero está en `original/`, como referencia.

La nueva lámina 3 se revela en tres pasos: requisitos y arquitectura; legado y capacidad; innovaciones. El detalle de las observaciones 37, 43 y 48 permanece en R10 (lámina 36).

Los cronometrajes son una pauta y requieren ensayo. Las pruebas del T-17 están diseñadas, no ejecutadas, y las exposiciones residuales son estimaciones.

## Tipografía

La fuente (Liberation Sans, licencia SIL OFL 1.1, subconjunto latino en `assets/fonts/`) va incrustada en la presentación. Así el texto mide lo mismo en cualquier navegador, pantalla o PC del proyector, y las etiquetas no se corren.

## Publicación

La presentación está en https://mvergaral.github.io/audIT/ (GitHub Pages, rama `gh-pages` del repositorio audIT, que contiene sólo los archivos de la presentación). Para republicar después de un cambio: `./publicar.sh` desde esta carpeta. No modifica `main`.

## Trabajo en equipo

1. Editar `construir.py` (contenido, láminas y orden en `RECORRIDO`) o los formularios del informe.
2. Ejecutar `python3 construir.py`: regenera `index.html`, `composition/`, `manifest.json`, `escenas.json` y `NOTAS-EXPOSICION.md`.
3. Abrir `index.html` para revisar y hacer commit de la fuente y de lo generado.
4. Si dos personas cambian la presentación a la vez, resolver el conflicto en `construir.py` y volver a generar; no editar a mano los archivos generados.
