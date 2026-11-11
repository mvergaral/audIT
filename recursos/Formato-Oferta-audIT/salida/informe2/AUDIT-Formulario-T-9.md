# Formulario T-9. 

audIT, Empresa N.º 10. Licitación TFEP-01/2026, Caso 10 Transporte de Carga. Oferta Técnica, Sobre N.º 2. Informe Preparatorio 2. Archivo AUDIT-Formulario-T-9.pdf. Anexo del Subdocumento N.º 6, Metodologías. Las fuentes están en las Referencias de ese subdocumento.

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

La matriz de trece destinatarios de S6 fija información, emisor, frecuencia, canal y escalamiento. Para una excepción operativa, el supervisor recibe el caso en el turno; el responsable funcional decide dentro de sus atribuciones; si afecta línea base o aceptación contractual, el Jefe de Proyecto lo eleva al comité correspondiente. Curimón designa titular y suplente funcionales por acta antes del primer sprint. El titular prioriza y revisa producto; H4 y H9 se aceptan mediante actas y evidencias de S7/S9. Una compra crítica se vincula a paquete, fecha de necesidad, responsable de suministro, recepción técnica y contingencia por retraso; los equipos del T-11 que compra el CLIENTE no se vuelven a presupuestar como compra de audIT.
\end{formulario}

