# Verificación de la presentación

## Revisión del 25 de noviembre de 2026

- La compilación en Windows generó 19 láminas principales y 30 de respaldo, con una pauta de 14:05.
- Los 49 SVG se analizaron como XML. Los recursos locales existen y la composición incrustada coincide con la que usa el servidor local.
- La lámina 16 se cotejó con el modelo final del Sobre 3 en las hojas «Parámetros D2», «Indicadores» y «Sensibilidad». Los márgenes de hitos y el estado de R-17 se cotejaron con S7 y S8.
- La revisión en Chrome sin interfaz no se completó por un fallo al iniciar el proceso gráfico. Queda pendiente verificar la proyección y las transiciones visuales en el navegador.

## Revisión histórica del 22 de octubre de 2026

- Chromium local: 16 diapositivas principales y 14 de respaldo localizadas mediante apertura directa de `index.html`.
- Comprobados: avance por teclado y clic; retroceso de fragmentos antes de cambiar de diapositiva; portada, cierre, respaldo con B y regreso con Escape.
- Movimiento continuo del camión de portada comprobado. En implantación, las tres entradas aparecen antes de las flechas.
- Capturadas las 30 diapositivas y una vista portátil de 1366 × 768. Las 16 principales y los 14 respaldos mantienen el texto SVG dentro del lienzo, cargan las imágenes y no presentan controles visibles.
- Tema claro revisado en portada, arquitectura, calidad, AMFE, EDT, cronograma y cierre: fondo blanco, texto azul oscuro y acentos de alto contraste. El logotipo utilizado corresponde a la variante para fondo claro.
- Sin errores de consola en el recorrido local. Evidencia: `revision/resultado.json` y capturas en `revision/`.
- HyperFrames 0.8.181: análisis estático sin errores. La comprobación de ejecución de la CLI no pudo completarse porque este entorno bloquea la conexión local a `127.0.0.1`; el recorrido equivalente del archivo final se verificó con Playwright.

La duración de 865 segundos es una pauta, no un ensayo oral. Las pruebas de T-17 se presentan como diseñadas, y las exposiciones residuales como estimaciones. No se ejecutaron pruebas del sistema propuesto ni se modificaron bitácoras personales.
