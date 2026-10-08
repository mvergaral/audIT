# Formulario T-17. Protocolo de aceptación

audIT, Empresa N.º 10. Licitación TFEP-01/2026, Caso 10 Transporte de Carga. Oferta Técnica, Sobre N.º 2. Informe Preparatorio 2. Archivo AUDIT-Formulario-T-17.pdf. Anexo del Subdocumento N.º 9, Plan de calidad. Las fuentes están en las Referencias de ese subdocumento.

\ifdefined\FormularioActual
\makeatletter
\audit@iniciarpartes

\renewcommand\@pnumwidth{2.2em}
\makeatother
{\renewcommand\textoEncabezado{\color{audit-marino}Índice}\indiceDetallado}

\makeatletter
\audit@marcasubdoc{Subdocumento 9}
\makeatother
\markboth{Formulario T-17}{}
\registrarFolio{formsd-9}{Formulario T-17}
\phantomsection
\addcontentsline{toc}{section}{Formulario T-17}
\fi
\begin{formulario}{T-17}
\begin{contenidoExigido}{T-17}
  \exigencia{Entregables de cada hito y del producto final.}{La secuencia de actividades, dependencias y evidencias por hito se articula con la estructura canónica de la EDT de 13 elementos y 54 paquetes de trabajo (con especial foco en el elemento 10 «Calidad y pruebas», paquetes 10.1 a 10.4) y el cronograma contractual de actividades A01 a A25 de S7 (Formularios T-14, T-15 y T-18). La verificación integral de la Etapa 1 se concentra en la actividad A12 (meses 10 a 12), la certificación de la Etapa 2 en la actividad A22 (meses 17 a 18), y los ejercicios semestrales de recuperación ante desastres (DR) se programan en junio y noviembre de cada año operacional (M21 a M56); véanse sección 9.3.1 y sección 9.3.2.}
  \exigencia{Criterios de aceptación objetivos.}{Se aplican la disponibilidad mínima de 99,9 % (FEP01, Artículo 20, p. 14), RTO máximo de 4 h y RPO máximo de 15 min (FEP02, RT-07.04, p. 17), y retención local mínima de 72 h (Caso, RT-03.10, p. 31); véase también sección 9.1.2 y sección 9.2.2. Los demás umbrales se aprueban y documentan antes de ejecutar las pruebas.}
  \exigencia{Evidencia requerida.}{Cada evidencia registra requisito y caso, fecha, versión, ambiente, datos y parámetros, herramienta, resultado, defectos y responsable; véase sección 9.3.4.}
  \exigencia{Plazos de revisión.}{Diez días hábiles de revisión y diez de subsanación. La segunda presentación con observaciones de igual naturaleza constituye atraso imputable (FEP01, Artículo 18.3, p. 13); véase sección 9.3.1.}
  \exigencia{Procedimiento de observaciones.}{Las observaciones se registran con identificador, requisito relacionado, severidad, evidencia y respuesta; la subsanación se revisa contra el criterio aprobado y sin aceptación por silencio y con acta suscrita; véase sección 9.3.3.}
  \exigencia{Acta de conformidad.}{El cierre registra el hito y versión evaluados, casos ejecutados y su estado, defectos abiertos, métricas efectivamente medidas, evidencias y pronunciamiento de la contraparte; véase sección 9.3.3.}
  \exigencia{Estado del catálogo de pruebas.}{El catálogo contiene 120 casos diseñados (25 unitarios, 25 de integración, 20 de sistema, 20 no funcionales y de seguridad, 15 HIL y 15 UAT), con trazabilidad diseñada hacia los 42 requerimientos del sistema formalizados en el Formulario T-12 (28 funcionales RF-001 a RF-028 y 14 no funcionales RNF-001 a RNF-014) y sus paquetes EDT asociados. La matriz distingue cobertura diseñada de evidencia ejecutada; no afirma probar todos los 54 paquetes. No se declaran ejecutados ni aprobados. Los escenarios sintéticos y umbrales adicionales se fijan antes de ejecutar. Catálogo: \hyperref[sec:9-catalogo]{Catálogo detallado}, folio \pageref{sec:9-catalogo}.}
\end{contenidoExigido}
Véanse los mínimos en sección 9.3.6 y las seis condiciones acumulativas y calendario en sección 9.3.5.
\input{subdocumentos/09-calidad/formularios/catalogo-T-17.tex}
\end{formulario}

