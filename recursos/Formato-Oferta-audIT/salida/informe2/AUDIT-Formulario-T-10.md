# Formulario T-10. 

audIT, Empresa N.º 10. Licitación TFEP-01/2026, Caso 10 Transporte de Carga. Oferta Técnica, Sobre N.º 2. Informe Preparatorio 2. Archivo AUDIT-Formulario-T-10.pdf. Anexo del Subdocumento N.º 6, Metodologías. Las fuentes están en las Referencias de ese subdocumento.

\begin{formulario}{T-10}

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
\begin{contenidoExigido}{T-10}
\exigencia{Ciclo de vida, requerimientos, arquitectura evolutiva y deuda técnica}{sección 6.2.1}
\exigencia{DevSecOps y automatización de pruebas}{sección 6.2.2}
\exigencia{Infraestructura y configuración como código}{sección 6.2.3}
\exigencia{Criterios de ingeniería, Definición de Preparado y Definición de Terminado}{sección 6.2.4}
\exigencia{Cadencias, promoción, reversión y métricas de entrega}{sección 6.2.5}
\end{contenidoExigido}
\end{formulario}
