# Propuesta Final

Abre `index.html` en Chrome o Edge. La presentación usa archivos locales y funciona sin conexión. Si el navegador restringe su carga, ejecuta `python3 visualizar.py` y abre http://127.0.0.1:4318/. Mantén el servidor abierto durante la exposición.

## Compilación

Desde esta carpeta del repositorio audIT, ejecuta `python3 construir.py`. Solo necesitas Python 3. El generador lee las exportaciones de T-14, T-15, T-16 y S8 en `recursos/Formato-Oferta-audIT/salida/informe2/` y las partidas económicas del repositorio.

## Manejo (estas instrucciones no aparecen en pantalla)

- Flecha derecha, espacio, Enter, PageDown o clic: siguiente revelación o diapositiva.
- Flecha izquierda, Backspace, PageUp o clic derecho: revelación anterior; al llegar al inicio, diapositiva anterior.
- F: alternar pantalla completa. Escape conserva el comportamiento de salida de pantalla completa del navegador.
- B: abrir el respaldo técnico. Escape: volver al punto de la presentación principal.
- Home: inicio de la secuencia actual. End: última diapositiva de la secuencia actual.
- P: modo presentador integrado, con notas privadas y una ventana de audiencia. Compartir solamente la audiencia. Para una exposición con una pantalla, usar F.

No hay botones, menús, instrucciones ni barras visibles en la superficie de exposición.

## Material

- **Versión final de 15 minutos:** 19 láminas principales, 14 minutos y 5 segundos objetivo y 55 segundos de margen (`construir.py` verifica la suma):
  - Apertura: portada, problema de la salida segura y resumen de la oferta (S2, S3).
  - Qué construimos: arquitectura híbrida, ocho capas, verificación en 30 s y camión sin red (S4, S5, T-11).
  - Cómo lo ejecutamos: EDT, ruta crítica de la red T-15 y compuerta G13 (S7, T-14, T-15).
  - Cómo lo protegemos: mapa de los 28 riesgos y reservas/holguras (S8, T-16).
  - Comercial: proveedores y adquisiciones, curva S, costos por categoría, VAN y TIR, garantías y pagos por hito (T-22, E-21, E-24, FEP01 Art. 35, 36 y p.74).
  - Cierre: tres compromisos verificables y preguntas.
- **Curva S:** se genera a partir de la planilla corregida del Sobre 3 en `Formato-Oferta-audIT/economico/planilla/`. Compara la facturación y los costos con intereses de la hoja «Curva S» y muestra el saldo de caja de la Fila C con IVA en el panel inferior.
- **Otras cifras económicas:** salen de `Formato-Oferta-audIT/economico/datos/partidas.csv`. Los campos vacíos se muestran como «POR COMPLETAR» y `construir.py` lista los pendientes al terminar. La tasa de descuento y la TIR se configuran en `TASA_DESCUENTO` y `TIR`.
- 30 láminas de respaldo: las de la Revisión 2 (riesgos, AMFE, árbol de fallas, implantación, hitos, reversión, calidad, correcciones, innovaciones, límites y diccionario EDT) más las que salieron del recorrido principal (hardware por nodo, datos, enlace cortado, paquetes de la EDT, qué pasa si, transición, siete riesgos altos y R-28).
- El respaldo no se muestra en el recorrido: se abre con B si una pregunta lo requiere; dentro, un número seguido de Enter salta a esa lámina. Escape vuelve.
- El puntero del mouse está visible y se oculta tras 4 segundos sin moverlo.
- `NOTAS-EXPOSICION.md` contiene las notas del recorrido actual por lámina. `GUION-5-EXPOSITORES.md` conserva el texto oral y los relevos de la versión anterior.

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
