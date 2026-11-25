# Formulario T-9. 

audIT, Empresa N.º 10. Licitación TFEP-01/2026, Caso 10 Transporte de Carga. Oferta Técnica, Sobre N.º 2. Propuesta final. Archivo AUDIT-Formulario-T-9.pdf. Anexo del Subdocumento N.º 6, Metodologías. Las fuentes están en las Referencias de ese subdocumento.

\begin{formulario}{T-9}

\ifdefined\AuditNumeracionTablas\else
\global\let\AuditNumeracionTablas\empty
\global\let\NumeracionTablasDthree\empty
\ExplSyntaxOn
\bool_new:N \g_audit_lt_avanzar_bool
\bool_new:N \g_audit_lt_paso_bool
\bool_new:N \g_audit_lt_pendiente_bool
\bool_new:N \g_audit_lt_numerada_bool
\bool_new:N \g_audit_lt_anotado_bool
\int_new:N \g_audit_lt_antes_int
\cs_if_exist:NT \AuditLongtableSinPaso { \bool_gset_true:N \g_audit_lt_avanzar_bool }
\cs_gset_protected:Npn \AuditEvaluarTabla
  {
    \bool_if:NT \g_audit_lt_pendiente_bool
      {
        \bool_gset_false:N \g_audit_lt_pendiente_bool
        \bool_if:NTF \g_audit_lt_numerada_bool
          {
            \int_set:Nn \l_tmpa_int { \value { table } - \g_audit_lt_antes_int }
            \bool_if:NTF \g_audit_lt_paso_bool
              { \int_compare:nNnT { \l_tmpa_int } > { 1 } { \bool_gset_false:N \g_audit_lt_avanzar_bool } }
              { \int_compare:nNnT { \l_tmpa_int } < { 1 } { \bool_gset_true:N \g_audit_lt_avanzar_bool } }
          }
          { \bool_if:NT \g_audit_lt_paso_bool { \addtocounter { table } { -1 } } }
        \bool_lazy_and:nnT { \g_audit_lt_avanzar_bool } { ! \g_audit_lt_anotado_bool }
          {
            \bool_gset_true:N \g_audit_lt_anotado_bool
            \exp_args:Nc \iow_now:Nn { @auxout } { \gdef \AuditLongtableSinPaso { } }
          }
      }
  }
\cs_gset_protected:Npn \AuditAntesDeTabla
  {
    \AuditEvaluarTabla
    \int_gset:Nn \g_audit_lt_antes_int { \value { table } }
    \bool_gset_false:N \g_audit_lt_numerada_bool
    \bool_gset_true:N \g_audit_lt_pendiente_bool
    \bool_gset_eq:NN \g_audit_lt_paso_bool \g_audit_lt_avanzar_bool
    \bool_if:NT \g_audit_lt_paso_bool { \refstepcounter { table } }
  }
\cs_gset_protected:Npn \AuditMarcarNumerada
  { \bool_if:NT \g_audit_lt_pendiente_bool { \bool_gset_true:N \g_audit_lt_numerada_bool } }
\ExplSyntaxOff
\AddToHook{env/tabla/before}[audit-numeracion]{\AuditAntesDeTabla}
\AddToHook{env/tabla/after}[audit-numeracion]{\AuditEvaluarTabla}
\AddToHook{cmd/addcontentsline/before}[audit-numeracion]{\AuditMarcarNumerada}
\fi

\AddToHook{env/contenidoExigido/before}[audit-exigido]{\AuditAntesDeTabla}
\AddToHook{env/contenidoExigido/after}[audit-exigido]{\AuditEvaluarTabla}
\begin{contenidoExigido}{T-9}
\exigencia{PMBOK adaptado y prácticas ágiles justificadas}{sección 6.1.1}
\exigencia{Interesados y comunicaciones}{sección 6.1.2}
\exigencia{Adquisiciones e integración contractual}{sección 6.1.3}
\exigencia{Control de cambios, comités y cadencias de decisión}{sección 6.1.4}
\end{contenidoExigido}

La línea base contractual se controla por paquete EDT, responsable, fecha temprana/tardía, holgura y evidencia de hito de S7. El Jefe de Proyecto compara avance y consumo de reservas cada semana, registra desvíos en el espacio colaborativo y lleva al Comité de Proyecto los bloqueos que afecten una entrega. Una modificación de alcance, plazo, costo o nivel de servicio se inicia con RFC; incluye impacto en EDT, ruta crítica, riesgo y pruebas; requiere acuerdo escrito conforme al Artículo 72 antes de ejecutarse. La revisión de sprint no reemplaza esa autorización.

La matriz de S6 fija información, emisor, frecuencia, canal y escalamiento para los trece actores. Las áreas de operación, mantenimiento, prevención y TI tienen seguimiento semanal. Finanzas recibe conciliaciones quincenales. Gerencia y familia reciben corte mensual, el fondo recibe informe trimestral y el cliente recibe el reporte contractual. Conductores reciben material por liberación y transportistas un corte mensual y por hito. Curimón comunica a la Dirección del Trabajo y la aseguradora por canal formal cuando procede.

Curimón designa titular y suplente funcionales por acta antes del primer sprint. El titular prioriza y revisa el incremento, con plazos propuestos de dos días hábiles para dudas bloqueantes y cinco para decidir. Ante ausencia actúa el suplente y ante falta de decisión se escala al Comité de Proyecto. H4 y H9 conservan sus actas y evidencias contractuales. Cada compra crítica registra paquete, fecha de necesidad, responsable, recepción y contingencia. El inventario T-11 identifica qué compra el CLIENTE.

El Líder Funcional dirige la adhesión de 148 transportistas mediante EDT 9.1 a 9.3. Registra cada mes los RUT con anexo firmado, vigente y registrado, y lleva bloqueos al Comité de Proyecto quincenal. Con 59 o menos al cierre de M9 activa refuerzo con el Administrador del Contrato. T-14 fija las metas de 104 en M16 y 134 en M21. El reporte mensual aplica los ocho indicadores y denominadores de S3. Se distinguen la firma por RUT, el consentimiento del conductor, el montaje y la activación, según S7.
\end{formulario}

