# Adenda A-6 · Corrección económica del Informe 3, versión 3.2

**Responsable:** Persona 8 · **Fecha:** 15 de noviembre de 2026 · **Herramienta:** Claude Opus 5.5 en Claude Code · **Nivel:** Alto en cálculo y redacción técnica de la planilla.

## Alcance de la intervención

A partir de la revisión oral del profesor sobre la presentación económica, el asistente contrastó el feedback contra la planilla 3.1, auditó el aporte posterior de Codex y aplicó los cambios de la versión 3.2 mediante scripts reproducibles en `Informe-3/correccion-final/v32/`:

- Escalones de madurez del soporte en la base y sustitución efectiva del montaje interno.
- Salida del técnico de campo interno en M10 y servicio de campo externo por visita en operación, dimensionado con el stock de reposición de D4 4.1.
- Prepago anual del soporte de fabricantes y refuerzos de puesta en producción en H6, H7, H11 y H12.
- Precio por fase desde costo y margen objetivo de 18,5 %.
- Prepago del crédito bancario en M17 y M18 y corrección de la lógica de la línea en los escenarios.

Las bases se consultaron solo con `tools/buscar.py` (E-24, E-25, Art. 73, Art. 78.2, Aclaraciones §5 y §7).

## Comprobaciones realizadas por el asistente

Recálculo completo con LibreOffice: cero celdas con error, identidad de caja con diferencia menor a 1 CLP, controles de `Control de entrega` en cero y cinco pruebas de propagación (`probar_32.py`). La réplica de la 3.1 en LibreOffice coincide en 38.831 de 38.835 valores; las cuatro diferencias son TIR de escenarios sin convergencia.

## Pendiente de revisión humana

Las pruebas del asistente no equivalen a revisión humana. Quedan por validar personalmente los supuestos sin cotización (horas internas de campo, visitas y rondas del proveedor, refuerzos de puesta en producción), la decisión de precio y el calendario de prepago con D2 y D4. Esta adenda no incorpora firma ni acredita aceptación del contenido.
