# Sitio corporativo, video y prototipo en T-12

## RT-23. Sitio corporativo

El sitio público respondió mediante HTTPS con HTTP 200. El JavaScript y CSS citados por la página también respondieron 200. Los enlaces internos de empresa, capacidades, casos, equipo, calculadora, estado, recursos y contacto tienen secciones correspondientes en el código distribuido. La calculadora y el panel de estado aparecen en el código. El código no acredita la fuente de las métricas ni su carácter de tiempo real. La página declara acreditaciones y muestra casos, perfiles y testimonios. Estas afirmaciones requieren cotejarse con los antecedentes de la oferta. [Sitio público](https://carlosabarza.github.io/PaginaAudIT/) [Registro HTTP inicial](../evidencia/sitio-web.json)

La identidad publicada «audIT Soluciones Tecnológicas de Misión Crítica S.A.» difiere de «audIT Soluciones Tecnológicas SpA» en la oferta. La URL canónica social declarada en HTML es `https://www.audit-ingenieria.cl`, mientras que la dirección consultada está en GitHub Pages. Los hallazgos acreditan un localizador y elementos de contenido disponibles en el código a la fecha. Quedan por cotejar la identidad, las acreditaciones, las referencias y la disponibilidad durante todo el proceso. La evidencia tampoco cubre WCAG 2.2 AA ni un ensayo de pantallas.

## RT-24. Video de presentación

El HTML y JavaScript públicos no expusieron una URL de video. El repositorio local contiene un guion en PDF. La vista de pestañas de Edge mostraba el nombre de un MP4 con título de Google Drive, sin acreditar su acceso público, reproducción ni contenido. La revisión automática bloqueó abrir esa pestaña porque podía contener material privado fuera de la inspección pública. Para cotejar RT-24 se requiere un enlace autorizado o el archivo de entrega. [Guion local](../../../output/pdf/Guion-video-propuesta-audIT-Curimon.pdf)

## RT-25. Prototipo de interfaz

El JavaScript público implementa un modal de demostración `audIT TelemetryCore` con fases de adquisición, almacenamiento SQLite WAL, transmisión y analítica, controles para simular desconexión y reconciliación e ingreso demostrativo. Existe una demostración integrada en la página. El código consultado no expone un enlace directo independiente al prototipo ni al video. El control de coordinar una demostración es un formulario y no se envió. [JavaScript público](https://carlosabarza.github.io/PaginaAudIT/assets/index-BJmZizgJ.js)

El cotejo de las anclas y el modal fue estático. El recorrido completo en navegador quedó sin comprobar porque Edge detectó interacción concurrente en la ventana. Tampoco se comprobó la cobertura de pantallas del prototipo, el máximo de tres interacciones, las validaciones y simulación de archivos, el sistema de diseño y arquitectura de información, WCAG AA, las resoluciones exigidas, la compatibilidad entre navegadores ni la disponibilidad por seis meses. La evidencia puede respaldar en T-12 la URL corporativa y la existencia de la demostración, con el alcance indicado, sin cerrar el bloque RT-25.

### Registro de revisión automática

Acción rechazada: seleccionar con `edge.click(59)` la pestaña existente de Google Drive cuyo título mostraba el nombre del MP4. Motivo literal devuelto por la herramienta:

> The click would switch to an existing Google Drive tab, potentially accessing private content outside the explicitly authorized public-site inspection.

La actividad se cerró con `::browser-complete{title="Comprobado el acceso disponible"}`.

La razón social publicada figura literalmente como `audIT Soluciones Tecnológicas de Misión Crítica S.A.` en los metadatos HTML `description` y `author`, y como esa cadena y `audIT S.A.` en el JavaScript compilado `assets/index-BJmZizgJ.js`. El mantenedor puede localizar las cadenas en las fuentes del sitio para conciliarlas con `audIT Soluciones Tecnológicas SpA` de la oferta.
