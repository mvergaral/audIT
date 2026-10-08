# Formulario T-13. Plan de calidad y verificación

audIT, Empresa N.º 10. Licitación TFEP-01/2026, Caso 10 Transporte de Carga. Oferta Técnica, Sobre N.º 2. Informe Preparatorio 2. Archivo AUDIT-Formulario-T-13.pdf. Anexo del Subdocumento N.º 9, Plan de calidad. Las fuentes están en las Referencias de ese subdocumento.

\ifdefined\FormularioActual
\makeatletter
\audit@iniciarpartes
\makeatother
{\renewcommand\textoEncabezado{\color{audit-marino}Índice}\indiceDetallado}

\makeatletter
\audit@marcasubdoc{Subdocumento 9}
\makeatother
\markboth{Formulario T-13}{}
\registrarFolio{formsd-9}{Formulario T-13}
\phantomsection
\addcontentsline{toc}{section}{Formulario T-13}
\fi
\begin{formulario}{T-13}
\begin{contenidoExigido}{T-13}
\exigencia{Niveles y tipos de prueba conforme a ISO/IEC/IEEE 29119.}{\hyperref[sec:9-t13-1]{Apartado 1}, folio \pageref{sec:9-t13-1}}
\exigencia{Ambientes y datos de prueba.}{\hyperref[sec:9-t13-2]{Apartado 2}, folio \pageref{sec:9-t13-2}}
\exigencia{Criterios de entrada y de salida.}{\hyperref[sec:9-t13-3]{Apartado 3}, folio \pageref{sec:9-t13-3}}
\exigencia{Automatización de pruebas.}{\hyperref[sec:9-t13-4]{Apartado 4}, folio \pageref{sec:9-t13-4}}
\exigencia{Calendario de las pruebas de carga, resiliencia, recuperación ante desastres y seguridad ofensiva.}{\hyperref[sec:9-t13-5]{Apartado 5}, folio \pageref{sec:9-t13-5}}
\end{contenidoExigido}

### 9.0.1 Niveles y tipos de prueba conforme a ISO/IEC/IEEE 29119.

\addcontentsline{toc}{subsection}{Niveles y tipos de prueba conforme a ISO/IEC/IEEE 29119.}
Se aplica planificación, seguimiento, diseño, preparación, ejecución y cierre de los procesos de prueba (ISO/IEC/IEEE, 2021). La estructura de nueve campos del catálogo es una convención de audIT. Se diseñan 25 casos unitarios, 25 de integración, 20 de sistema, 12 de rendimiento y 8 de seguridad, 15 de hardware/HIL y 15 UAT: 120 identificadores únicos. Unitarias contrastan reglas/oráculos; integración valida esquemas e idempotencia; sistema verifica flujos completos; no funcionales miden carga, seguridad y recuperación; HIL utiliza dispositivos homologados; UAT comprueba tareas con contraparte. Véase sección 9.2.

### 9.0.2 Ambientes y datos de prueba.

\addcontentsline{toc}{subsection}{Ambientes y datos de prueba.}
CI utiliza dobles y fixtures sintéticos; QA integra contratos; staging reproduce configuración/carga; HIL conserva modelo, firmware, señales y permisos; UAT usa terminales y usuarios designados con autorización. Producción se utiliza solo en ejercicio autorizado, con respaldo y reversión. Se versionan entradas, semilla/reloj, oráculo y manifiesto. No se atribuyen marcas o API ensayadas al parque existente sin homologación. Datos operacionales requieren acceso autorizado y minimización. Véase sección 9.2.1.

### 9.0.3 Criterios de entrada y de salida.

\addcontentsline{toc}{subsection}{Criterios de entrada y de salida.}
Entrada: versión/configuración y ambiente identificados, requisito/caso/criterio fijados, datos y permisos disponibles, observabilidad y reversión verificadas. Salida: todos los criterios aplicables cumplidos, reporte reproducible y defectos relacionados, sin críticos/altos para cierre de marcha blanca. Se aplican los mínimos de sección 9.3.6; cuatro semanas sostenidas y las seis condiciones acumulativas de sección 9.3.5 gobiernan aceptación. Un promedio o cobertura de código no reemplaza otro criterio.

### 9.0.4 Automatización de pruebas.

\addcontentsline{toc}{subsection}{Automatización de pruebas.}
Cada cambio ejecuta compilación, pruebas unitarias y regresión; contratos e integración se ejecutan contra dobles versionados y en QA. Cobertura de lógica de negocio mínima de 70 % es bloqueante; 80 % es objetivo adicional. Análisis estático/dependencias y pruebas de autorización acompañan cada promoción; el resultado se conserva por versión. Carga, cortes de enlace y recuperación requieren script, manifiesto y cronómetro; HIL/UAT conservan las verificaciones manuales que no puede suplir un pipeline. Un fallo bloquea promoción y dispara corrección/reevaluación; una excepción no rebaja mínimos contractuales. Véase sección 9.2.3.

### 9.0.5 Calendario de las pruebas de carga, resiliencia, recuperación ante desastres y seguridad ofensiva.

\addcontentsline{toc}{subsection}{Calendario de las pruebas de carga, resiliencia, recuperación ante desastres y seguridad ofensiva.}
Construcción E1: A09/A10/A11; certificación E1 A12, M12/H5, con informes separados de las cuatro familias y UAT. Marcha blanca A15, M13--M15; producción A19, M16/H7. Construcción E2 A20 y certificación A22, M18/H10, incluyendo regresión E1 y las cuatro familias. Marcha blanca A24, M19--M20; aceptación final A25, M21/H12. DR y seguridad ofensiva requieren autorización previa y reversión; las ventanas contractuales no se desplazan por ensayos. Resiliencia y DR se repiten semestralmente en operación; intrusión anual y antes de producción por tercero independiente, con informe íntegro y remediación. Se realizan dos ensayos de migración antes de la definitiva (FEP02, 20.1, pp. 34--35; RT-11.20, p. 24). Véase sección 9.3.2.
\end{formulario}

