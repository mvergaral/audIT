# Verificación de la presentación

Revisión del 29 de octubre de 2026: incorporación de la síntesis de cambios como lámina 3.

## Comprobado en esta revisión

- Generación con `python3 construir.py`: 26 láminas principales, 21 respaldos y 889 segundos objetivo (14:49), con 11 segundos de margen respecto de los 15 minutos. Es una pauta, no un ensayo oral.
- Orden inicial: portada, salida segura, cambios principales y separador «Qué construimos». Las escenas tienen identificadores únicos y referencias válidas en el manifiesto.
- Tabla con cinco grupos de observaciones del Informe 1, contrastados con la matriz consolidada y los capítulos S3, S4 y S13 vigentes del repositorio. Las referencias complementarias apuntan a T-11, T-12, T-17 y T-19. No se utilizaron como contenido las copias externas al repositorio ni `original/`.
- Tres fragmentos para la lámina 3, en posiciones 21, 23 y 25 de la composición: dos, cuatro y cinco filas visibles. La estructura y el pie de alcance pertenecen al primer fragmento; las filas anteriores se conservan.
- El detalle de las observaciones 37, 43 y 48 sigue en R10, ahora lámina 36.
- Coherencia entre los manifiestos incrustados, `manifest.json`, `escenas.json`, composición independiente e incrustada, notas y guion. Las 26 entradas y sus tiempos en el guion suman 889 segundos.
- Revisión visual estática de la nueva lámina a 1920 × 1080 y 1366 × 768, sus tres estados, las láminas vecinas 2 y 4 y el respaldo R10. Las etiquetas de la tabla caben en sus columnas, sin recortes ni solapamientos en los renders revisados.

## Evidencia y alcance de la comprobación visual

`revision/resultado-cambios.json` registra las comprobaciones. `revision/cambios-informe2-estatico.png` y `revision/cambios-informe2-estatico-1366.png` son renders estáticos obtenidos del SVG generado, con Liberation Sans, la fuente de origen de AuditSans. Reproducen la composición y sus estados; no son capturas de navegador ni acreditan el comportamiento de GSAP o el ajuste de texto del navegador.

## Pendiente de comprobación interactiva

El navegador disponible bloqueó la apertura del archivo local por política de seguridad. No se verificaron en esta revisión las animaciones en ejecución, avance y retroceso por teclado/clic, retorno desde el respaldo, modo presentador, carga en navegador ni consola. El adaptador de navegación y las bibliotecas se conservaron sin cambios; la lámina nueva utiliza sus grupos `data-step` y transiciones existentes. Se requiere abrir `index.html` en un navegador autorizado, recorrer los tres fragmentos de la lámina 3, retroceder, avanzar al separador, entrar a R10 con B y «10 + Enter», volver con Escape y comprobar P con su ventana de audiencia.

Realizar un ensayo oral con cronómetro y otro en proyector. Las pruebas T-17 siguen presentándose como diseñadas, no ejecutadas, y los riesgos residuales como estimaciones. Esta revisión no acredita el cierre integral de las 100 observaciones ni resultados de pruebas del sistema propuesto.

## Integración del cambio remoto 7aea637

Se integra el orden de contextos y los códigos EDT del remoto en la arquitectura lógica, actualmente lámina 6. Se conserva la síntesis de cambios en la lámina 3. Los seis códigos y nombres (5.1 a 5.6) se cotejaron con T-14 y el bloque de contextos de la fuente integrada coincide con el remoto. Los conflictos de los dos HTML generados se resolvieron regenerándolos desde la fuente combinada.

Se repitieron las comprobaciones de manifiestos, orden, fragmentos, notas y duración: 26 principales, 21 respaldos y 889 segundos. Se revisó el render estático de la lámina 6 a 1920 × 1080 y se generó también a 1366 × 768: `revision/arquitectura-integrada-estatico.png` y `revision/arquitectura-integrada-estatico-1366.png`. La confirmación visual del usuario y la comprobación interactiva siguen pendientes. No se publica ni se sube esta integración antes de la confirmación solicitada.
