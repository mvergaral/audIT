% ============================================================================
%  audit-oferta.cls
%  Clase de la oferta técnica de audIT, Licitación TFEP-01/2026, Caso 10.
%  Se compila con LuaLaTeX. Ver GUIA.md para el uso.
%
%  Opciones
%    grises           tema de prueba en escala de grises (temas/grises.tex)
%    compatibilidad   carga las macros del formato anterior
% ============================================================================
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{audit-oferta}[2026/09/26 v1.0 Oferta tecnica audIT]

\newif\ifaudit@grises
\newif\ifaudit@compat
\DeclareOption{grises}{\audit@grisestrue}
\DeclareOption{compatibilidad}{\audit@compattrue}
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{report}}
\ProcessOptions\relax

\LoadClass[11pt,letterpaper,oneside,openany]{report}

\RequirePackage{iftex}
\RequireLuaTeX

% ----------------------------------------------------------------------------
%  Paquetes base
% ----------------------------------------------------------------------------
\RequirePackage{etoolbox}
\RequirePackage{calc}
\RequirePackage[table]{xcolor}
\RequirePackage{graphicx}
\RequirePackage{tikz}
\usetikzlibrary{calc,positioning}
\RequirePackage{audit-fuentes}
\RequirePackage[spanish,es-tabla,es-noindentfirst,es-noshorthands,es-nolayout]{babel}
% microtype con protrusión y expansión solo hacia afuera (shrink=0). Una
% expansión que comprime el glifo 1 % se mide en el PDF como letra de 10,89 pt,
% y el Artículo 40.4 fija 11 como mínimo del cuerpo.
\RequirePackage[protrusion=true,expansion=true,stretch=20,shrink=0]{microtype}
\RequirePackage{enumitem}
\RequirePackage{csquotes}

\ifaudit@grises\input{grises}\else\input{marca}\fi

% ----------------------------------------------------------------------------
%  Datos de la oferta: metadatos e instancia
%  Cada dato se fija con su comando (\Cliente{...}) y se lee con \dato{cliente}
% ----------------------------------------------------------------------------
\ExplSyntaxOn
\prop_new:N \g_audit_datos_prop
\cs_new_protected:Npn \audit_definir_dato:nn #1#2
  {
    \exp_args:Nc \NewDocumentCommand {#1} { +m }
      { \prop_gput:Nnn \g_audit_datos_prop {#2} {##1} }
  }
\clist_map_inline:nn
  {
    {Empresa}{empresa}, {EmpresaNumero}{empresanumero}, {EmpresaRUT}{empresarut},
    {EmpresaDomicilio}{domicilio}, {Lugar}{lugar}, {Cliente}{cliente},
    {Licitacion}{licitacion}, {LicitacionCorta}{licitacioncorta}, {Caso}{caso},
    {Proyecto}{proyecto}, {RepresentanteLegal}{representante},
    {RepresentanteRUT}{representanterut}, {RepresentanteCargo}{representantecargo},
    {ImagenMediaFirma}{mediafirma}, {ImagenFirmaCompleta}{firmacompleta},
    {SiglaArchivo}{sigla}, {Version}{version}, {AnexoHorizontal}{anexohorizontal},
    {DescripcionFicha}{descripcion},
    {TextoSobre}{sobre}, {TituloSobre}{titulosobre}, {NombreOferta}{nombreoferta}
  }
  { \audit_definir_dato:nn #1 }

\NewExpandableDocumentCommand \dato { m }
  { \prop_item:Nn \g_audit_datos_prop {#1} }
\prg_new_conditional:Npnn \audit_dato_vacio:n #1 { T, F, TF }
  {
    \tl_if_blank:eTF { \prop_item:Nn \g_audit_datos_prop {#1} }
      { \prg_return_true: } { \prg_return_false: }
  }
\NewDocumentCommand \SiDato { m +m +m } { \audit_dato_vacio:nTF {#1} {#3} {#2} }

% Instancia
\tl_new:N \g_audit_instancia_tl
\NewDocumentCommand \Instancia { m } { \tl_gset:Nn \g_audit_instancia_tl {#1} }
\NewExpandableDocumentCommand \instancia { } { \tl_use:N \g_audit_instancia_tl }

% Modo de folio
\tl_new:N \g_audit_modofolio_tl
\NewDocumentCommand \ModoFolio { m } { \tl_gset:Nn \g_audit_modofolio_tl {#1} }
\prg_new_conditional:Npnn \audit_folio_continuo: { T, F, TF }
  { \tl_if_eq:NnTF \g_audit_modofolio_tl { continuo } { \prg_return_true: } { \prg_return_false: } }
\NewDocumentCommand \SiFolioContinuo { +m +m } { \audit_folio_continuo:TF {#1} {#2} }

% Fecha de entrega AAAA-MM-DD, con su forma larga y la del nombre de archivo
\tl_new:N \g_audit_fecha_larga_tl
\tl_new:N \g_audit_fecha_archivo_tl
\tl_new:N \g_audit_fecha_mes_tl
\seq_new:N \l_audit_fecha_seq
\tl_const:Nn \c_audit_meses_tl
  { {enero}{febrero}{marzo}{abril}{mayo}{junio}{julio}{agosto}
    {septiembre}{octubre}{noviembre}{diciembre} }
\NewDocumentCommand \FechaEntrega { m }
  {
    \seq_set_split:Nnn \l_audit_fecha_seq { - } {#1}
    \tl_gset:Ne \g_audit_fecha_larga_tl
      {
        \int_eval:n { \seq_item:Nn \l_audit_fecha_seq {3} } ~ de ~
        \tl_item:Nn \c_audit_meses_tl { \seq_item:Nn \l_audit_fecha_seq {2} } ~ de ~
        \seq_item:Nn \l_audit_fecha_seq {1}
      }
    \tl_gset:Ne \g_audit_fecha_mes_tl
      {
        \text_titlecase_first:n
          { \tl_item:Nn \c_audit_meses_tl { \seq_item:Nn \l_audit_fecha_seq {2} } }
        ~ de ~ \seq_item:Nn \l_audit_fecha_seq {1}
      }
    \tl_gset:Ne \g_audit_fecha_archivo_tl
      {
        \seq_item:Nn \l_audit_fecha_seq {1}
        \seq_item:Nn \l_audit_fecha_seq {2}
        \seq_item:Nn \l_audit_fecha_seq {3}
      }
  }
\NewExpandableDocumentCommand \fechaLarga { } { \tl_use:N \g_audit_fecha_larga_tl }
\NewExpandableDocumentCommand \fechaMes { } { \tl_use:N \g_audit_fecha_mes_tl }
\NewExpandableDocumentCommand \fechaArchivo { } { \tl_use:N \g_audit_fecha_archivo_tl }

% ----------------------------------------------------------------------------
%  Catálogo de subdocumentos e instancias (configuracion/subdocumentos.tex)
% ----------------------------------------------------------------------------
\cs_generate_variant:Nn \prop_item:Nn { Nv }
\prop_new:N \g_audit_sd_carpeta_prop
\prop_new:N \g_audit_sd_titulo_prop
\prop_new:N \g_audit_sd_corto_prop
\prop_new:N \g_audit_sd_formularios_prop
\prop_new:N \g_audit_instancia_lista_prop
\prop_new:N \g_audit_instancia_rotulo_prop
\prop_new:N \g_audit_instancia_prefijo_prop

\NewDocumentCommand \DeclararSubdocumento { m m m m m }
  {
    \prop_gput:Nnn \g_audit_sd_carpeta_prop {#1} {#2}
    \prop_gput:Nnn \g_audit_sd_titulo_prop {#1} {#3}
    \prop_gput:Nnn \g_audit_sd_corto_prop {#1} {#4}
    \prop_gput:Nnn \g_audit_sd_formularios_prop {#1} {#5}
  }
\NewDocumentCommand \SubdocumentosDeInstancia { m m }
  { \prop_gput:Nnn \g_audit_instancia_lista_prop {#1} {#2} }
\NewDocumentCommand \RotuloDeInstancia { m m m }
  {
    \prop_gput:Nnn \g_audit_instancia_rotulo_prop {#1} {#2}
    \prop_gput:Nnn \g_audit_instancia_prefijo_prop {#1} {#3}
  }
\NewExpandableDocumentCommand \rotuloInstancia { }
  { \prop_item:Nv \g_audit_instancia_rotulo_prop { g_audit_instancia_tl } }
\NewExpandableDocumentCommand \prefijoInstancia { }
  { \prop_item:Nv \g_audit_instancia_prefijo_prop { g_audit_instancia_tl } }
\NewExpandableDocumentCommand \tituloDeSubdocumento { m }
  { \prop_item:Nn \g_audit_sd_titulo_prop {#1} }
\NewExpandableDocumentCommand \cortoDeSubdocumento { m }
  { \prop_item:Nn \g_audit_sd_corto_prop {#1} }
\NewExpandableDocumentCommand \carpetaDeSubdocumento { m }
  { \prop_item:Nn \g_audit_sd_carpeta_prop {#1} }
\NewExpandableDocumentCommand \formulariosDeSubdocumento { m }
  { \prop_item:Nn \g_audit_sd_formularios_prop {#1} }

% Subdocumento en curso
\tl_new:N \g_audit_sd_actual_tl
\NewExpandableDocumentCommand \subdocActual { } { \tl_use:N \g_audit_sd_actual_tl }
\NewExpandableDocumentCommand \tituloSubdocActual { }
  { \prop_item:Nv \g_audit_sd_titulo_prop { g_audit_sd_actual_tl } }
\NewExpandableDocumentCommand \cortoSubdocActual { }
  { \prop_item:Nv \g_audit_sd_corto_prop { g_audit_sd_actual_tl } }
\NewDocumentCommand \FijarSubdocumento { m } { \tl_gset:Nn \g_audit_sd_actual_tl {#1} }
\NewDocumentCommand \SiHaySubdoc { +m +m } { \tl_if_empty:NTF \g_audit_sd_actual_tl {#2} {#1} }

% Calendario del Formulario T-20: fecha y modo de folio de cada instancia.
% \AplicarInstancia{final} cambia la instancia vigente con esos datos (lo usa
% la muestra económica, que arma documentos de otras instancias).
\prop_new:N \g_audit_calendario_prop
\NewDocumentCommand \CalendarioInstancia { m m m }
  { \prop_gput:Nnn \g_audit_calendario_prop {#1} { {#2} {#3} } }
\NewDocumentCommand \AplicarInstancia { m } { \audit_aplicar_instancia:e {#1} }
\cs_new_protected:Npn \audit_aplicar_instancia:n #1
  {
    \prop_get:NnNTF \g_audit_calendario_prop {#1} \l_tmpa_tl
      {
        \Instancia {#1}
        \exp_last_unbraced:NV \audit_aplicar_calendario:nn \l_tmpa_tl
      }
      { \msg_error:nnn { audit } { sin-calendario } {#1} }
  }
\cs_generate_variant:Nn \audit_aplicar_instancia:n { e }
\cs_new_protected:Npn \audit_aplicar_calendario:nn #1#2
  { \FechaEntrega {#1} \ModoFolio {#2} }
\msg_new:nnn { audit } { sin-calendario }
  { La~instancia~#1~no~está~en~el~calendario~de~configuracion/subdocumentos.tex. }

% Recorre los subdocumentos de la instancia vigente
\NewDocumentCommand \ParaCadaSubdocumento { +m }
  {
    \clist_map_inline:en
      { \prop_item:Nv \g_audit_instancia_lista_prop { g_audit_instancia_tl } }
      { #1 }
  }
\cs_generate_variant:Nn \clist_map_inline:nn { en }

% Nombre de archivo de un subdocumento según la instancia (Artículos 49 a 51 y
% patrón ya usado por el equipo): INFORME2_AUDIT_SUBDOC04_20261005
\NewExpandableDocumentCommand \nombreArchivoSubdoc { m }
  {
    \prefijoInstancia _ \dato{sigla} _SUBDOC
    \int_compare:nNnT {#1} < {10} {0} \int_eval:n {#1} _ \fechaArchivo
  }
\ExplSyntaxOff

% ----------------------------------------------------------------------------
%  Marcador: campo por completar. Se ve en el PDF y queda en el registro para
%  que el verificador lo cuente.
% ----------------------------------------------------------------------------
\DeclareRobustCommand\marcador[1]{%
  {\sffamily\color{audit-secundario}[\,#1\,]}%
  \ifdefined\audit@marcadores@log
    \immediate\write-1{AUDIT-MARCADOR: \detokenize{#1}}%
  \fi}
\def\audit@marcadores@log{}

% ----------------------------------------------------------------------------
%  Módulos del formato
% ----------------------------------------------------------------------------
\RequirePackage{pagina}
\RequirePackage{titulos}
\RequirePackage{tablas}
\RequirePackage{figuras}
\RequirePackage{dispositivos}
\RequirePackage{citas}
\RequirePackage{portadas}
\RequirePackage{formularios}
\RequirePackage{ensamblado}
\RequirePackage{economico}

% Referencias a otros subdocumentos cuando el sobre va en varios PDF. La
% herramienta de compilación entrega el archivo con -usepretex.
\ifdefined\ArchivoExternos\RequirePackage{xr-hyper}\fi
\RequirePackage[hidelinks,unicode,pdfusetitle,bookmarksnumbered]{hyperref}
\RequirePackage{bookmark}
\hypersetup{pdfcreator={audIT}, pdfauthor={audIT}}
\pdfstringdefDisableCommands{\def\marcador#1{[#1]}\def\req#1{#1}}
\RequirePackage{lastpage}
\ifdefined\ArchivoExternos\InputIfFileExists{\ArchivoExternos}{}{}\fi

\ifaudit@compat\RequirePackage{compatibilidad}\fi

% Datos por defecto, luego los reemplaza la configuración
\Version{1.0}
\FechaEntrega{2026-01-01}
\ModoFolio{subdocumento}
\AnexoHorizontal{pagina}
\DescripcionFicha{}
\TextoSobre{Oferta Técnica, Sobre N.º 2}
\TituloSobre{Oferta Técnica\\Sobre N.º 2}
\NombreOferta{oferta técnica}

\endinput
