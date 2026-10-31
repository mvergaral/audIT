---
workflow: slideshow
flow: automation
storyboard: yes
language: es
aspect_ratio: '16:9'
---
# Revisión 2 · audIT / Transportes Curimón

Presentación de 15 minutos y 15 minutos de discusión. El recorrido vigente tiene 26 escenas principales, incluida portada y cierre, y 21 de respaldo.

## Preferencias confirmadas
Pantalla completa. Diagramas grandes y explicados por etapas, tablas breves y gráficos con movimiento. Sin botones, menús, barras de navegación ni instrucciones de manejo visibles. Avance por teclado o clic. Sin desplazamiento vertical ni apariencia de página web. Material de respaldo fuera del recorrido principal.

## Evidencia y límites
Referencia de contenido: LaTeX oficiales de S1–S9 y S13 y sus formularios, cotejados con las exportaciones del generador. Fuentes exclusivamente del repositorio: matriz consolidada `recursos/Formato-Oferta-audIT/anexos/observaciones-informe1.tex` y exportaciones Markdown vigentes de S3, S4, S5, S7, S8, S13, T-11, T-12, T-14, T-15, T-16, T-17, T-18 y T-19; observaciones del Informe 1 incorporadas al artículo 46. No confundir las revisiones internas de Informe 2 con observaciones de Informe 1. Los riesgos residuales son estimaciones. Las pruebas están diseñadas, no ejecutadas. Omitir probabilidades Monte Carlo no reproducidas. Usar meses contractuales; febrero de 2027 es supuesto. No declarar todas las correcciones cerradas. No asignar revisiones humanas ni autores ficticiamente.

## Decisiones de producción
26 diapositivas principales, 14 minutos y 29 segundos objetivo más 31 segundos de margen. Respaldo separado. Diagramas vectoriales propios, fuente AuditSans (Liberation Sans) incrustada y activos locales para funcionamiento sin conexión. Identidad audIT con fondo blanco, texto azul oscuro y acentos turquesa y ámbar para proyección. Sin música ni voz sintética. Guion oral distribuido entre cinco expositores en `GUION-5-EXPOSITORES.md`.

## Entorno
HyperFrames 0.8.181 y GSAP 3.14.2. CLI descargado en caché local del workspace. La actualización de la skill verificó presencia, pero no frescura por GitHub inaccesible. El catálogo no devolvió recursos por fallo de red; se construyen diagramas propios. Cuota HyperFrames desconocida; no se infiere disponibilidad.

## Resumen de cambios
La lámina 3, «Cambios principales del Informe 2», precede al primer acto y resume cinco grupos de observaciones: requisitos y trazabilidad, esquema y arquitectura, sistema de 2013, dimensionamiento e innovaciones. Cada fila identifica observaciones, cambio y ubicación. El texto es breve, con iconos vectoriales y tres revelaciones que conservan las filas anteriores. Los detalles permanecen en las notas y el guion. No se utilizan como fuente las copias externas al repositorio ni `original/`.

La tabla de correcciones ocupa 40 segundos. El recorrido completo se distribuye en 14:29 y conserva 31 segundos para relevos y contingencias de exposición. El guion refleja esos tiempos. La actualización es local; la web se actualiza mediante `publicar.sh`. La pauta requiere ensayo oral.

## Criterios de contenido

- Identificación del conductor mediante MIFARE; biometría reservada al acceso de la sala de datos.
- Integraciones de terceros sujetas a autorización y factibilidad por proveedor.
- Capacidad M13–M15: 37 FTE repartidos en 21,5 E1, 14,1 E2 y 1,4 de coordinación; Seguridad e Integración son roles distintos.
- R-28 distingue preemisión con carga conocida y solicitud satelital cuando se conoce en terreno; fragmentación, acuse y reintentos respetan el plazo.
- S7: PERT por cadenas con 95,6 % conjunto. S8: Monte Carlo de red completa con 92,1 % conjunto. El ejemplo A09 +10 días no recalcula esas probabilidades.
- Operación M21–M56; reversión con las seis acciones del T-18 y responsables originales.
- Cada innovación conserva su calendario y denominador. El diccionario EDT se distribuye por altura de fila sin descartar líneas.
