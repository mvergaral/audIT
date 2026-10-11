# Recuperación de innovación 2 y figuras

Fecha de revisión: 2026-10-11. Base integrada: `ea974f8`.

## Historial

- `34b439a` sustituyó en S13 y T-19 la innovación 2 de D3 por la versión antigua «Despliegue sin detener la flota».
- Las referencias PDF de los PERT de S7 proceden de `7b8d8eb`, anterior; sus archivos estaban excluidos por `*.pdf`.
- La integración reciente añadió referencias a PDF no versionados en S4, S8 y S13.

## Recuperación localizada

Se restaura de `cec61e1` exclusivamente S13 §13.2 y T-19 tipo 2. Se concilian la descripción de apertura, el gráfico general y la declaración de IA asociada. Las otras cuatro innovaciones conservan el contenido de `ea974f8`.

No se reinstalan los incrementos manuales del contador de tablas de la versión antigua: el estilo vigente ya incrementa el contador al iniciar las tablas. Esta decisión aplica a las dos tablas recuperadas de §13.2; no constituye una auditoría completa de la numeración de los otros subdocumentos.

`recursos/Formato-Oferta-audIT/herramientas/recuperar_figuras.py` regenera 24 figuras PDF desde SVG existentes y versionados de D3 y D4. La excepción de `.gitignore` permite versionar exclusivamente los PDF de la carpeta de figuras; conserva la exclusión de entregables y escaneos.

## Originales todavía ausentes

No hay archivo ni fuente local/versionada de:

- S4: `ambientes-promocion.pdf`, `region-secundaria.pdf`.
- S8: `rbs.pdf`, `mapa-calor.pdf`, `arbol-fallas.pdf`.

Se requieren las fuentes u originales del autor para completar la recuperación de S4 y S8. No se sustituyen por gráficos distintos ni por figuras vacías.

## Estado de entrega

La recuperación y los cambios D1 anteriores se incluyen en el commit de esta entrega para su publicación en `main`. La compilación y revisión se registran en el chat. S7 compila con referencias cruzadas pendientes que ya trae la integración; no se presenta como validación completa de su contenido. Se recuperan en la bibliografía común las tres entradas originales usadas por la innovación 2.

## Verificación realizada

- S7: compilación de 25 páginas; PERT recuperados en folios 15 y 16.
- S13: compilación de 27 páginas; innovación 2 recuperada en folios 12 a 15, tablas 13.2 y 13.3 sin incremento manual adicional.
- T-19: compilación de 13 páginas; ficha tipo 2 recuperada en folios 7 y 8, sin citas bibliográficas pendientes.
- Revisión visual de las páginas recuperadas y comprobación de preservación de las otras cuatro innovaciones y de los cambios D1 previos.
- Permanecen referencias cruzadas sin resolver en otras partes de S7 y S13; la compilación exitosa no supone aprobación integral de la entrega.
