# Anexo S5. Diccionario de datos y supuestos de capacidad

audIT, Empresa N.º 10. Licitación TFEP-01/2026. Informe 2.

El diccionario especifica el modelo propuesto de D3, por dominio, conforme a FEP02 · RT-05.01 · p.11 y Comunicado 10 · capítulo 5. Las figuras del cuerpo seleccionan relaciones críticas para mantener legibilidad; aquí se explicitan atributos y controles. El catálogo se valida con los propietarios y fuentes del CLIENTE antes de congelar el esquema.

UUID identifica globalmente sin renumerar un original. TIMESTAMPTZ conserva un instante normalizado; la zona/offset de origen se registra aparte cuando importa; el valor original de fuente se guarda cuando su interpretación sea incierta. NULL significa ausente/desconocido cuando corresponde y nunca se rellena con cero. Las referencias entre contextos son lógicas y se validan por contratos; las FK físicas se implementan en las tablas locales del contexto. Una etiqueta PK/FK en el modelo no impone acceso directo a otra base. Los campos condicionales se exigen al confirmar su estado; una recepción incompleta se conserva sin habilitar operación. Los catálogos TEXT se validan con CHECK o catálogo versionado; JSONB requiere esquema y versión explícitos.

## CLIENTE

Propietario de atributos: Contable (identidad comercial); Planificación (atributos operacionales). La tabla define el contrato del registro.

| Atributo | Tipo | Dominio y regla | Obligatorio | Propietario | Sensibilidad/tratamiento |
|---|---|---|---|---|---|
| id_cliente | UUID | PK; generado una vez y preservado en reintentos | Sí | Planificación y tráfico | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| rut | TEXT | Identificador chileno validado; cifrado e índice ciego | Sí | Sistema contable | Personal si identifica persona natural; cifrado/acceso según RT-11.10 cuando aplica |
| razon_social | TEXT | Denominación acreditada | Sí | Sistema contable | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| estado | TEXT | ACTIVO / INACTIVO | Sí | Planificación y tráfico | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| referencia_contable | TEXT | ID externo homologado; unicidad por sistema | Sí | Sistema contable | Operacional; cifrado/acceso según RT-11.10 cuando aplica |

## TRANSPORTISTA

Propietario de atributos: Contable (identidad comercial); Personas y Flota (adhesión y recursos). La tabla define el contrato del registro.

| Atributo | Tipo | Dominio y regla | Obligatorio | Propietario | Sensibilidad/tratamiento |
|---|---|---|---|---|---|
| id_transportista | UUID | PK; generado una vez y preservado en reintentos | Sí | Flota y activos | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| rut | TEXT | Identificador validado; cifrado e índice ciego | Sí | Sistema contable | Personal si identifica persona natural; cifrado/acceso según RT-11.10 cuando aplica |
| razon_social | TEXT | Denominación acreditada | Sí | Sistema contable | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| referencia_contable | TEXT | ID homologado | Sí | Sistema contable | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| estado_adhesion | TEXT | COMPLETA / DATOS / SIN_ADHESION; versionado | Sí | Flota y activos | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| id_documento_adhesion | UUID | Referencia a DOCUMENTO_RESPALDO | Condicional | Flota y activos | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| adhesion_desde | TIMESTAMPTZ | Inicio de vigencia contractual | Condicional | Flota y activos | Operacional; personal si vincula jornada; cifrado/acceso según RT-11.10 cuando aplica |
| adhesion_hasta | TIMESTAMPTZ | Vencimiento; NULL si sin fin fijado | No | Flota y activos | Operacional; personal si vincula jornada; cifrado/acceso según RT-11.10 cuando aplica |

## CONDUCTOR

Propietario de atributos: Personas y cumplimiento. La tabla define el contrato del registro.

| Atributo | Tipo | Dominio y regla | Obligatorio | Propietario | Sensibilidad/tratamiento |
|---|---|---|---|---|---|
| id_conductor | UUID | PK; generado una vez y preservado en reintentos | Sí | Personas y cumplimiento | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| id_transportista | UUID | Referencia a TRANSPORTISTA; NULL propio | No | Personas y cumplimiento | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| rut | TEXT | Identificador validado, cifrado e índice ciego | Sí | Personas y cumplimiento | Personal; cifrado/acceso según RT-11.10 cuando aplica |
| nombre_completo | TEXT | Nombre acreditado; cifrado | Sí | Personas y cumplimiento | Personal; cifrado/acceso según RT-11.10 cuando aplica |
| clase_licencia | TEXT | Catálogo homologado; aptitud según vehículo | Sí | Personas y cumplimiento | Personal; cifrado/acceso según RT-11.10 cuando aplica |
| estado_operativo | TEXT | HABILITADO / BLOQUEADO; no sustituye evaluación | Sí | Personas y cumplimiento | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| id_documento_identidad | UUID | Referencia a DOCUMENTO_RESPALDO | Sí | Personas y cumplimiento | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| actualizado_utc | TIMESTAMPTZ | Última actualización acreditada | Sí | Personas y cumplimiento | Operacional; personal si vincula jornada; cifrado/acceso según RT-11.10 cuando aplica |

## TRACTOCAMION

Propietario de atributos: Flota y activos. La tabla define el contrato del registro.

| Atributo | Tipo | Dominio y regla | Obligatorio | Propietario | Sensibilidad/tratamiento |
|---|---|---|---|---|---|
| id_tracto | UUID | PK; generado una vez y preservado en reintentos | Sí | Flota y activos | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| patente | TEXT | Normalizada y única en el registro maestro | Sí | Flota y activos | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| tipo_propiedad | TEXT | PROPIO / TERCERO | Sí | Flota y activos | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| id_transportista | UUID | Referencia a TRANSPORTISTA; NULL si propio | No | Flota y activos | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| modelo | TEXT | Modelo y fabricante homologados | Sí | Flota y activos | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| estado | TEXT | DISPONIBLE / RESERVADO / MANTENCION / FUERA_SERVICIO | Sí | Flota y activos | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| acceso_fabrica | TEXT | AUTORIZADO / NO_AUTORIZADO / NO_DISPONIBLE; no booleano inferido | Sí | Flota y activos | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| mapa_senales_version | TEXT | Protocolo y señales autorizadas | No | Flota y activos | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| id_dispositivo | UUID | Referencia a DISPOSITIVO | No | Flota y activos | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |

## SEMIRREMOLQUE

Propietario de atributos: Flota y activos. La tabla define el contrato del registro.

| Atributo | Tipo | Dominio y regla | Obligatorio | Propietario | Sensibilidad/tratamiento |
|---|---|---|---|---|---|
| id_semirremolque | UUID | PK; generado una vez y preservado en reintentos | Sí | Flota y activos | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| patente | TEXT | Identificador normalizado; tercero según inventario | Sí | Flota y activos | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| tipo_carroceria | TEXT | Catálogo de compatibilidad de carga | Sí | Flota y activos | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| capacidad_kg | NUMERIC | >0; según certificado, no rango universal inventado | Sí | Flota y activos | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| tipo_propiedad | TEXT | PROPIO / TERCERO | Sí | Flota y activos | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| id_transportista | UUID | Referencia a TRANSPORTISTA | No | Flota y activos | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| estado | TEXT | Disponibilidad y aptitud versionadas | Sí | Flota y activos | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| id_baliza | TEXT | ID registrado y homologado; no evidencia personal | No | Flota y activos | Operacional; cifrado/acceso según RT-11.10 cuando aplica |

## PUNTO_SERVICIO

Propietario de atributos: Planificación y tráfico. La tabla define el contrato del registro.

| Atributo | Tipo | Dominio y regla | Obligatorio | Propietario | Sensibilidad/tratamiento |
|---|---|---|---|---|---|
| id_punto | UUID | PK; generado una vez y preservado en reintentos | Sí | Planificación y tráfico | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| id_cliente | UUID | Referencia a CLIENTE | No | Planificación y tráfico | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| tipo | TEXT | ORIGEN / DESTINO / TERMINAL / TALLER / PARADOR | Sí | Planificación y tráfico | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| nombre | TEXT | Denominación operacional | Sí | Planificación y tráfico | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| geometria | GEOMETRY(Polygon,4326) | PostGIS GEOMETRY, SRID 4326; validar polígono y versión | Condicional | Planificación y tráfico | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| margen_geocerca | NUMERIC | Parámetro calibrado; unidad declarada | Condicional | Planificación y tráfico | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| version | INTEGER | Versión usada por el equipo | Sí | Planificación y tráfico | Operacional; cifrado/acceso según RT-11.10 cuando aplica |

## ORDEN_TRANSPORTE

Propietario de atributos: Planificación y tráfico. La tabla define el contrato del registro.

| Atributo | Tipo | Dominio y regla | Obligatorio | Propietario | Sensibilidad/tratamiento |
|---|---|---|---|---|---|
| id_orden | UUID | PK; generado una vez y preservado en reintentos | Sí | Planificación y tráfico | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| id_cliente | UUID | Referencia a CLIENTE | Sí | Planificación y tráfico | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| id_origen | UUID | Referencia a PUNTO_SERVICIO | Sí | Planificación y tráfico | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| id_destino | UUID | Referencia a PUNTO_SERVICIO | Sí | Planificación y tráfico | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| carga | TEXT | Tipo/código y especificación del servicio | Sí | Planificación y tráfico | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| peso_previsto_kg | NUMERIC | >0 cuando disponible; no sustituye pesaje definitivo | No | Planificación y tráfico | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| requiere_semirremolque | BOOLEAN | BOOLEAN; determina campo obligatorio al asignar | Sí | Planificación y tráfico | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| estado | TEXT | ABIERTA / PROGRAMADA / CUMPLIDA / CANCELADA | Sí | Planificación y tráfico | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| fecha_servicio | TIMESTAMPTZ | Fecha programada; zona origen conservada | Sí | Planificación y tráfico | Operacional; personal si vincula jornada; cifrado/acceso según RT-11.10 cuando aplica |

## VIAJE

Propietario de atributos: Operación de fletes. La tabla define el contrato del registro.

| Atributo | Tipo | Dominio y regla | Obligatorio | Propietario | Sensibilidad/tratamiento |
|---|---|---|---|---|---|
| id_viaje | UUID | PK; generado una vez y preservado en reintentos | Sí | Operación de fletes | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| id_orden | UUID | Referencia a ORDEN_TRANSPORTE | Sí | Operación de fletes | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| codigo_viaje | TEXT | Identificador único legible | Sí | Operación de fletes | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| estado_viaje | TEXT | PROGRAMADO / EN_CARGA / EN_RUTA / EN_DESCARGA / CERRADO / CANCELADO | Sí | Operación de fletes | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| peso_origen_kg | NUMERIC | Pesaje definitivo; obligatorio antes de salida si aplica | Condicional | Operación de fletes | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| id_punto_actual | UUID | Referencia a PUNTO_SERVICIO | No | Operación de fletes | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| inicio_utc | TIMESTAMPTZ | Inicio efectivo | No | Operación de fletes | Operacional; personal si vincula jornada; cifrado/acceso según RT-11.10 cuando aplica |
| cierre_utc | TIMESTAMPTZ | Cierre efectivo | No | Operación de fletes | Operacional; personal si vincula jornada; cifrado/acceso según RT-11.10 cuando aplica |
| version | INTEGER | Entero positivo para control optimista | Sí | Operación de fletes | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| motivo_cancelacion | TEXT | Obligatorio al cancelar | Condicional | Operación de fletes | Operacional; cifrado/acceso según RT-11.10 cuando aplica |

## ASIGNACION

Propietario de atributos: Planificación y tráfico. La tabla define el contrato del registro.

| Atributo | Tipo | Dominio y regla | Obligatorio | Propietario | Sensibilidad/tratamiento |
|---|---|---|---|---|---|
| id_asignacion | UUID | PK; generado una vez y preservado en reintentos | Sí | Planificación y tráfico | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| id_viaje | UUID | Referencia a VIAJE | Sí | Planificación y tráfico | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| id_conductor | UUID | Referencia a CONDUCTOR | Al confirmar | Planificación y tráfico | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| id_tracto | UUID | Referencia a TRACTOCAMION | Al confirmar | Planificación y tráfico | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| id_semirremolque | UUID | Referencia a SEMIRREMOLQUE | Si carga lo exige | Planificación y tráfico | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| id_transportista | UUID | Referencia a TRANSPORTISTA | Si tercero | Planificación y tráfico | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| desde_utc | TIMESTAMPTZ | Inicio de reserva | Sí | Planificación y tráfico | Operacional; personal si vincula jornada; cifrado/acceso según RT-11.10 cuando aplica |
| hasta_utc | TIMESTAMPTZ | Fin; NULL activa | No | Planificación y tráfico | Operacional; personal si vincula jornada; cifrado/acceso según RT-11.10 cuando aplica |
| estado | TEXT | PROPUESTA / CONFIRMADA / LIBERADA / RECHAZADA | Sí | Planificación y tráfico | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| clave_idempotencia | TEXT | Única por cliente de API y operación; persistencia duradera | Sí | Planificación y tráfico | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| version_recursos | TEXT | Versiones de validación usadas | Sí | Planificación y tráfico | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| correlacion | TEXT | ID común de la operación | Sí | Planificación y tráfico | Operacional; cifrado/acceso según RT-11.10 cuando aplica |

## DOCUMENTO_RESPALDO

Propietario de atributos: Propietario del dominio que aporta el documento. La tabla define el contrato del registro.

| Atributo | Tipo | Dominio y regla | Obligatorio | Propietario | Sensibilidad/tratamiento |
|---|---|---|---|---|---|
| id_documento | UUID | PK; generado una vez y preservado en reintentos | Sí | Dominio del documento: Personas, Flota u Operación, uno por registro | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| tipo_documento | TEXT | Catálogo versionado; no se inventa total de tipos | Sí | Dominio del documento: Personas, Flota u Operación, uno por registro | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| hash_sha256 | TEXT | 64 hex; hash del original exacto | Sí | Dominio del documento: Personas, Flota u Operación, uno por registro | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| uri | TEXT | Objeto inmutable; sin secretos en URI | Sí | Dominio del documento: Personas, Flota u Operación, uno por registro | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| emisor | TEXT | Responsable u origen acreditado | Sí | Dominio del documento: Personas, Flota u Operación, uno por registro | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| recibido_utc | TIMESTAMPTZ | Recepción por plataforma | Sí | Dominio del documento: Personas, Flota u Operación, uno por registro | Operacional; personal si vincula jornada; cifrado/acceso según RT-11.10 cuando aplica |
| firma_estado | TEXT | VALIDA / INVALIDA / NO_APLICA / PENDIENTE; hash no es firma | Sí | Dominio del documento: Personas, Flota u Operación, uno por registro | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| retener_hasta | TIMESTAMPTZ | Fin mínimo contractual según dominio | Sí | Dominio del documento: Personas, Flota u Operación, uno por registro | Operacional; personal si vincula jornada; cifrado/acceso según RT-11.10 cuando aplica |
| retencion_litigio | BOOLEAN | BOOLEAN; prolonga sin permitir borrado anticipado | Sí | Dominio del documento: Personas, Flota u Operación, uno por registro | Operacional; cifrado/acceso según RT-11.10 cuando aplica |

## VIGENCIA_HABILITACION

Propietario de atributos: Personas y cumplimiento (conductor); Flota y activos (equipos). La tabla define el contrato del registro.

| Atributo | Tipo | Dominio y regla | Obligatorio | Propietario | Sensibilidad/tratamiento |
|---|---|---|---|---|---|
| id_vigencia | UUID | PK; generado una vez y preservado en reintentos | Sí | Dominio del sujeto: Personas o Flota, uno por registro | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| id_conductor | UUID | Referencia a CONDUCTOR | Excluyente | Personas y cumplimiento | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| id_tracto | UUID | Referencia a TRACTOCAMION | Excluyente | Flota y activos | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| id_semirremolque | UUID | Referencia a SEMIRREMOLQUE | Excluyente | Flota y activos | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| tipo_documento | TEXT | Catálogo homologado para el sujeto | Sí | Dominio del sujeto: Personas o Flota, uno por registro | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| fecha_vencimiento | DATE | DATE; cotejo documental | Sí | Dominio del sujeto: Personas o Flota, uno por registro | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| estado_verificacion | TEXT | VERIFICADO / PENDIENTE / RECHAZADO / REVOCADO | Sí | Dominio del sujeto: Personas o Flota, uno por registro | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| id_documento | UUID | Referencia a DOCUMENTO_RESPALDO | Al verificar | Dominio del sujeto: Personas o Flota, uno por registro | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| verificado_utc | TIMESTAMPTZ | Fecha real de cotejo | Al verificar | Dominio del sujeto: Personas o Flota, uno por registro | Operacional; personal si vincula jornada; cifrado/acceso según RT-11.10 cuando aplica |
| verificado_por | TEXT | Identidad del verificador | Al verificar | Dominio del sujeto: Personas o Flota, uno por registro | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| responsable_renovacion | TEXT | Rol/titular responsable; alertas 60/30/7 días | Sí | Dominio del sujeto: Personas o Flota, uno por registro | Operacional; cifrado/acceso según RT-11.10 cuando aplica |

## DISPOSITIVO

Propietario de atributos: Telemetría y geocercas. La tabla define el contrato del registro.

| Atributo | Tipo | Dominio y regla | Obligatorio | Propietario | Sensibilidad/tratamiento |
|---|---|---|---|---|---|
| id_dispositivo | UUID | PK; generado una vez y preservado en reintentos | Sí | Telemetría y geocercas | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| codigo_origen | TEXT | ID externo único por proveedor | Sí | Telemetría y geocercas | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| tipo | TEXT | AUDIT / TERCERO / FABRICA / TACOGRAFO | Sí | Telemetría y geocercas | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| proveedor | TEXT | Fuente homologada | Sí | Telemetría y geocercas | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| certificado_id | TEXT | Identidad por equipo cuando sea aplicable | Condicional | Telemetría y geocercas | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| version_config | TEXT | Configuración y esquema | Sí | Telemetría y geocercas | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| ultimo_acuse_utc | TIMESTAMPTZ | Último commit confirmado | No | Telemetría y geocercas | Operacional; personal si vincula jornada; cifrado/acceso según RT-11.10 cuando aplica |
| cursor_confirmado | TEXT | Secuencia duradera por flujo | No | Telemetría y geocercas | Operacional; cifrado/acceso según RT-11.10 cuando aplica |

## EVIDENCIA_JORNADA

Propietario de atributos: Personas y cumplimiento. La tabla define el contrato del registro.

| Atributo | Tipo | Dominio y regla | Obligatorio | Propietario | Sensibilidad/tratamiento |
|---|---|---|---|---|---|
| id_evidencia | UUID | PK; generado una vez y preservado en reintentos | Sí | Personas y cumplimiento | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| id_conductor | UUID | Referencia a CONDUCTOR; no inferir identidad | No | Personas y cumplimiento | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| id_dispositivo | UUID | Referencia a DISPOSITIVO | No | Personas y cumplimiento | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| id_documento_original | UUID | Referencia a DOCUMENTO_RESPALDO | Si hay artefacto firmado/archivo | Personas y cumplimiento | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| codigo_fuente | TEXT | Código original recibido, sin renumerarlo | Sí | Personas y cumplimiento | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| estado_evidencia | TEXT | VALIDA / CODIGO_FUENTE_DESCONOCIDO / EVIDENCIA_INVALIDA | Sí | Personas y cumplimiento | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| nivel_cascada | SMALLINT | SMALLINT NULL o 0–5; 0 sólo REG_COND; NULL no válida | Si VALIDA | Personas y cumplimiento | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| tipo_evento | TEXT | CONDUCCION / ESPERA / REPOSO / ATESTACION / VOLUNTARIO; catálogo versionado | Sí | Personas y cumplimiento | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| evento_utc | TIMESTAMPTZ | Hora de fuente interpretada; conservar original | No | Personas y cumplimiento | Operacional; personal si vincula jornada; cifrado/acceso según RT-11.10 cuando aplica |
| recibido_utc | TIMESTAMPTZ | Hora de recepción | Sí | Personas y cumplimiento | Operacional; personal si vincula jornada; cifrado/acceso según RT-11.10 cuando aplica |
| marca_original | TEXT | Hora/offset/código original para interpretación | No | Personas y cumplimiento | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| calidad_reloj | TEXT | GNSS / NTP / NO_SINCRONIZADO / DESCONOCIDO; deriva cuando medible | Sí | Personas y cumplimiento | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| odometro_km | NUMERIC | ≥0 cuando medido; NULL ausente | No | Personas y cumplimiento | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| velocidad_kmh | NUMERIC | ≥0 cuando medida; NULL ausente | No | Personas y cumplimiento | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| cadena_id | TEXT | Identificador de cadena de custodia | Sí | Personas y cumplimiento | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| secuencia_custodia | BIGINT | BIGINT >0; único por cadena | Sí | Personas y cumplimiento | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| hash_sha256 | TEXT | 64 hex; registro canónico y referencia al original | Sí | Personas y cumplimiento | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| hash_previo | TEXT | 64 hex; NULL sólo al inicio de cadena | Condicional | Personas y cumplimiento | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| rectifica_id | UUID | Referencia a EVIDENCIA_JORNADA original | No | Personas y cumplimiento | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| mapeo_version | TEXT | Versión origen→nivel aplicada | Sí | Personas y cumplimiento | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| motivo_invalidez | TEXT | Obligatorio para fuente desconocida/inválida | Condicional | Personas y cumplimiento | Operacional; cifrado/acceso según RT-11.10 cuando aplica |

## EVALUACION_ASIGNACION

Propietario de atributos: Personas y cumplimiento. La tabla define el contrato del registro.

| Atributo | Tipo | Dominio y regla | Obligatorio | Propietario | Sensibilidad/tratamiento |
|---|---|---|---|---|---|
| id_evaluacion | UUID | PK; generado una vez y preservado en reintentos | Sí | Personas y cumplimiento | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| id_asignacion | UUID | Referencia a ASIGNACION | Sí | Personas y cumplimiento | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| estado_evidencia | TEXT | VALIDA / SIN_EVIDENCIA / CODIGO_FUENTE_DESCONOCIDO / EVIDENCIA_INVALIDA | Sí | Personas y cumplimiento | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| modalidad_adhesion | TEXT | COMPLETA / DATOS / SIN_ADHESION | Sí | Personas y cumplimiento | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| veredicto | TEXT | HABILITADA / HABILITADA_CON_MARCA / BLOQUEADA / EXCEPCION_RN04_APROBADA | Sí | Personas y cumplimiento | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| regla_version | TEXT | Versión de reglas y catálogo normativo aplicado | Sí | Personas y cumplimiento | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| causa | JSONB | Causales y datos faltantes estructurados; esquema versionado | Sí | Personas y cumplimiento | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| evaluado_utc | TIMESTAMPTZ | Hora de decisión | Sí | Personas y cumplimiento | Operacional; personal si vincula jornada; cifrado/acceso según RT-11.10 cuando aplica |
| correlacion | TEXT | Enlace auditable a solicitud y respuesta | Sí | Personas y cumplimiento | Operacional; cifrado/acceso según RT-11.10 cuando aplica |

## EVALUACION_EVIDENCIA

Propietario de atributos: Personas y cumplimiento. La tabla define el contrato del registro.

| Atributo | Tipo | Dominio y regla | Obligatorio | Propietario | Sensibilidad/tratamiento |
|---|---|---|---|---|---|
| id_evaluacion | UUID | Referencia a EVALUACION_ASIGNACION; parte de PK | Sí | Personas y cumplimiento | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| id_evidencia | UUID | Referencia a EVIDENCIA_JORNADA; parte de PK | Sí | Personas y cumplimiento | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| uso | TEXT | JORNADA / REPOSO / ATESTACION / AUXILIAR | Sí | Personas y cumplimiento | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| condicion_validada | JSONB | Identidad, rango temporal e integridad comprobados; esquema versionado | Sí | Personas y cumplimiento | Operacional; cifrado/acceso según RT-11.10 cuando aplica |

## EXCEPCION_RN04

Propietario de atributos: Personas y cumplimiento. La tabla define el contrato del registro.

| Atributo | Tipo | Dominio y regla | Obligatorio | Propietario | Sensibilidad/tratamiento |
|---|---|---|---|---|---|
| id_excepcion | UUID | PK; generado una vez y preservado en reintentos | Sí | Personas y cumplimiento | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| id_evaluacion | UUID | Referencia a EVALUACION_ASIGNACION; máximo una aprobada | Sí | Personas y cumplimiento | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| motivo | TEXT | Sólo indisponibilidad de fuente; causa legal nunca elegible | Sí | Personas y cumplimiento | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| aprobador_torre | TEXT | Jefe de turno identificado | Sí | Personas y cumplimiento | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| aprobador_prevencion | TEXT | Prevención de riesgos identificada; independiente | Sí | Personas y cumplimiento | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| aprobado_utc | TIMESTAMPTZ | Antes de confirmar excepción | Sí | Personas y cumplimiento | Operacional; personal si vincula jornada; cifrado/acceso según RT-11.10 cuando aplica |
| alcance | TEXT | Un único viaje/asignación | Sí | Personas y cumplimiento | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| revisado_utc | TIMESTAMPTZ | Revisión mensual real | No | Personas y cumplimiento | Operacional; personal si vincula jornada; cifrado/acceso según RT-11.10 cuando aplica |

## PERMISO_COMPARTIR

Propietario de atributos: Personas y cumplimiento. La tabla define el contrato del registro.

| Atributo | Tipo | Dominio y regla | Obligatorio | Propietario | Sensibilidad/tratamiento |
|---|---|---|---|---|---|
| id_permiso | UUID | PK; generado una vez y preservado en reintentos | Sí | Personas y cumplimiento | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| id_transportista | UUID | Referencia a TRANSPORTISTA | Sí | Personas y cumplimiento | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| recurso | TEXT | Tipo e ID de camión/conductor/viaje autorizado | Sí | Personas y cumplimiento | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| destinatario | TEXT | Rol/cliente/sistema; referencia verificable | Sí | Personas y cumplimiento | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| finalidad | TEXT | Propósito específico; no autorización genérica | Sí | Personas y cumplimiento | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| datos_autorizados | JSONB | Catálogo granular de posición, documentos u otro dato; esquema versionado | Sí | Personas y cumplimiento | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| desde_utc | TIMESTAMPTZ | Inicio | Sí | Personas y cumplimiento | Operacional; personal si vincula jornada; cifrado/acceso según RT-11.10 cuando aplica |
| hasta_utc | TIMESTAMPTZ | Fin; permiso local siempre con expiración | Sí | Personas y cumplimiento | Operacional; personal si vincula jornada; cifrado/acceso según RT-11.10 cuando aplica |
| revocado_utc | TIMESTAMPTZ | Cese registrado | No | Personas y cumplimiento | Operacional; personal si vincula jornada; cifrado/acceso según RT-11.10 cuando aplica |
| version | INTEGER | Entero positivo; invalidación de caché | Sí | Personas y cumplimiento | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| id_respaldo | UUID | Referencia a DOCUMENTO_RESPALDO | Sí | Personas y cumplimiento | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| base_tratamiento_ref | TEXT | Registro jurídico separado; no se deduce del permiso comercial | Sí | Personas y cumplimiento | Operacional; cifrado/acceso según RT-11.10 cuando aplica |

## ACCESO_DATO

Propietario de atributos: Seguridad y auditoría. La tabla define el contrato del registro.

| Atributo | Tipo | Dominio y regla | Obligatorio | Propietario | Sensibilidad/tratamiento |
|---|---|---|---|---|---|
| id_acceso | UUID | PK; generado una vez y preservado en reintentos | Sí | Seguridad y auditoría | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| actor | TEXT | Persona o sistema autenticado | Sí | Seguridad y auditoría | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| recurso | TEXT | Tipo, ID y campos mostrados/negados | Sí | Seguridad y auditoría | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| id_permiso | UUID | Referencia a PERMISO_COMPARTIR | Si aplica | Seguridad y auditoría | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| permiso_version | INTEGER | Versión evaluada | Si aplica | Seguridad y auditoría | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| resultado | TEXT | PERMITIDO / DENEGADO | Sí | Seguridad y auditoría | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| acceso_utc | TIMESTAMPTZ | Hora UTC | Sí | Seguridad y auditoría | Operacional; personal si vincula jornada; cifrado/acceso según RT-11.10 cuando aplica |
| correlacion | TEXT | Petición, dispositivo y canal | Sí | Seguridad y auditoría | Operacional; cifrado/acceso según RT-11.10 cuando aplica |

## TELEMETRIA_EVENTO

Propietario de atributos: Telemetría y geocercas. La tabla define el contrato del registro.

| Atributo | Tipo | Dominio y regla | Obligatorio | Propietario | Sensibilidad/tratamiento |
|---|---|---|---|---|---|
| id_evento | UUID | PK; generado una vez y preservado en reintentos | Sí | Telemetría y geocercas | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| id_dispositivo | UUID | Referencia a DISPOSITIVO | Sí | Telemetría y geocercas | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| id_viaje | UUID | Referencia a VIAJE | No | Telemetría y geocercas | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| id_conductor | UUID | Referencia a CONDUCTOR; sólo vínculo acreditado | No | Telemetría y geocercas | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| secuencia_origen | BIGINT | BIGINT; unicidad por equipo/flujo cuando fuente la ofrece | No | Telemetría y geocercas | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| evento_utc | TIMESTAMPTZ | Hora de fuente | No | Telemetría y geocercas | Operacional; personal si vincula jornada; cifrado/acceso según RT-11.10 cuando aplica |
| recibido_utc | TIMESTAMPTZ | Hora de recepción | Sí | Telemetría y geocercas | Operacional; personal si vincula jornada; cifrado/acceso según RT-11.10 cuando aplica |
| latitud | NUMERIC | −90..90; ambas coordenadas o ninguna | No | Telemetría y geocercas | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| longitud | NUMERIC | −180..180; ambas coordenadas o ninguna | No | Telemetría y geocercas | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| odometro_km | NUMERIC | Dato medido; NULL ausente | No | Telemetría y geocercas | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| parametros | JSONB | JSONB validado por esquema y mapa autorizado; esquema versionado | Sí | Telemetría y geocercas | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| hash_origen | TEXT | Integridad y procedencia | Sí | Telemetría y geocercas | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| autorizacion_version | INTEGER | Permiso aplicado; no transmitir fuera de su alcance | Si aplica | Telemetría y geocercas | Operacional; cifrado/acceso según RT-11.10 cuando aplica |

## ESTANCIA_CLIENTE

Propietario de atributos: Operación de fletes. La tabla define el contrato del registro.

| Atributo | Tipo | Dominio y regla | Obligatorio | Propietario | Sensibilidad/tratamiento |
|---|---|---|---|---|---|
| id_estancia | UUID | PK; generado una vez y preservado en reintentos | Sí | Operación de fletes | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| id_viaje | UUID | Referencia a VIAJE | Sí | Operación de fletes | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| id_punto | UUID | Referencia a PUNTO_SERVICIO | Sí | Operación de fletes | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| llegada_utc | TIMESTAMPTZ | Evento automático geocerca | Sí | Operación de fletes | Operacional; personal si vincula jornada; cifrado/acceso según RT-11.10 cuando aplica |
| salida_utc | TIMESTAMPTZ | NULL mientras estancia abierta | No | Operación de fletes | Operacional; personal si vincula jornada; cifrado/acceso según RT-11.10 cuando aplica |
| id_evento_llegada | UUID | Referencia a TELEMETRIA_EVENTO | Sí | Operación de fletes | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| id_evento_salida | UUID | Referencia a TELEMETRIA_EVENTO | No | Operación de fletes | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| geocerca_version | TEXT | Polígono y regla usados | Sí | Operación de fletes | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| causa_demora | TEXT | Cliente / frontera / otra; no cobro automático por toda demora | No | Operación de fletes | Operacional; cifrado/acceso según RT-11.10 cuando aplica |

## DOCUMENTO_TRANSPORTE

Propietario de atributos: Operación de fletes; emisor fiscal externo contable. La tabla define el contrato del registro.

| Atributo | Tipo | Dominio y regla | Obligatorio | Propietario | Sensibilidad/tratamiento |
|---|---|---|---|---|---|
| id_documento_transporte | UUID | PK; generado una vez y preservado en reintentos | Sí | Operación de fletes; emisor fiscal externo contable | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| id_viaje | UUID | Referencia a VIAJE | Sí | Operación de fletes; emisor fiscal externo contable | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| id_original | UUID | Referencia a DOCUMENTO_RESPALDO | Sí | Operación de fletes; emisor fiscal externo contable | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| folio | TEXT | Asignado exclusivamente por contable; único por emisor/tipo | Sí | Operación de fletes; emisor fiscal externo contable | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| emisor | TEXT | Identidad del emisor | Sí | Operación de fletes; emisor fiscal externo contable | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| estado | TEXT | SOLICITADO / EMITIDO / ENTREGADO / RECHAZADO / ANULADO | Sí | Operación de fletes; emisor fiscal externo contable | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| representacion_uri | TEXT | Copia portable conforme del mismo contenido | Al habilitar salida | Operación de fletes; emisor fiscal externo contable | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| emitido_utc | TIMESTAMPTZ | Hora de emisión del contable | Al emitir | Operación de fletes; emisor fiscal externo contable | Operacional; personal si vincula jornada; cifrado/acceso según RT-11.10 cuando aplica |
| acuse_cabina_utc | TIMESTAMPTZ | Entrega completa verificada | Antes de salida | Operación de fletes; emisor fiscal externo contable | Operacional; personal si vincula jornada; cifrado/acceso según RT-11.10 cuando aplica |
| clave_idempotencia | TEXT | Solicitud fiscal correlacionada y duradera | Sí | Operación de fletes; emisor fiscal externo contable | Operacional; cifrado/acceso según RT-11.10 cuando aplica |

## CONFORMIDAD_ENTREGA

Propietario de atributos: Operación de fletes. La tabla define el contrato del registro.

| Atributo | Tipo | Dominio y regla | Obligatorio | Propietario | Sensibilidad/tratamiento |
|---|---|---|---|---|---|
| id_conformidad | UUID | PK; generado una vez y preservado en reintentos | Sí | Operación de fletes | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| id_viaje | UUID | Referencia a VIAJE | Sí | Operación de fletes | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| destinatario | TEXT | Persona identificada que recibe | Sí | Operación de fletes | Personal; acceso restringido; cifrado/acceso según RT-11.10 cuando aplica |
| resultado | TEXT | CONFORME / DISCREPANCIA / RECHAZADA | Sí | Operación de fletes | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| observacion | TEXT | Descripción concreta | No | Operación de fletes | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| id_original_firmado | UUID | Referencia a DOCUMENTO_RESPALDO | Sí | Operación de fletes | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| evento_utc | TIMESTAMPTZ | Firma/recepción | Sí | Operación de fletes | Operacional; personal si vincula jornada; cifrado/acceso según RT-11.10 cuando aplica |
| firma_modalidad | TEXT | Modalidad admitida para el caso; comprobación de identidad e integridad | Sí | Operación de fletes | Operacional; cifrado/acceso según RT-11.10 cuando aplica |

## CHECKLIST_CARGA_PELIGROSA

Propietario de atributos: Operación de fletes. La tabla define el contrato del registro.

| Atributo | Tipo | Dominio y regla | Obligatorio | Propietario | Sensibilidad/tratamiento |
|---|---|---|---|---|---|
| id_checklist | UUID | PK; generado una vez y preservado en reintentos | Sí | Operación de fletes | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| id_viaje | UUID | Referencia a VIAJE | Sí | Operación de fletes | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| version | INTEGER | Versión de lista y regla | Sí | Operación de fletes | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| resultado | TEXT | APROBADA / RECHAZADA | Sí | Operación de fletes | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| items | JSONB | JSONB validado; carga y documentación cotejadas; esquema versionado | Sí | Operación de fletes | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| id_original_firmado | UUID | Referencia a DOCUMENTO_RESPALDO | Sí | Operación de fletes | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| verificado_utc | TIMESTAMPTZ | Antes del movimiento | Sí | Operación de fletes | Operacional; personal si vincula jornada; cifrado/acceso según RT-11.10 cuando aplica |

## TARIFA_CONTRATO

Propietario de atributos: Liquidación y costeo; terceros desde M16 y clientes desde M21. La tabla define el contrato del registro.

| Atributo | Tipo | Dominio y regla | Obligatorio | Propietario | Sensibilidad/tratamiento |
|---|---|---|---|---|---|
| id_tarifa | UUID | PK; generado una vez y preservado en reintentos | Sí | Liquidación y costeo | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| id_cliente | UUID | Referencia a CLIENTE; exactamente una contraparte | Excluyente | Liquidación y costeo | Operacional; acceso restringido |
| id_transportista | UUID | Referencia a TRANSPORTISTA; exactamente una contraparte | Excluyente | Liquidación y costeo | Operacional; acceso restringido |
| ruta_servicio | TEXT | Alcance contractual | Sí | Liquidación y costeo | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| importe | NUMERIC | Moneda y regla de redondeo conservadas | Sí | Liquidación y costeo | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| moneda | TEXT | Catálogo ISO de moneda | Sí | Liquidación y costeo | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| desde_utc | TIMESTAMPTZ | Inicio de vigencia | Sí | Liquidación y costeo | Operacional; personal si vincula jornada; cifrado/acceso según RT-11.10 cuando aplica |
| hasta_utc | TIMESTAMPTZ | Fin; NULL si no fijado | No | Liquidación y costeo | Operacional; personal si vincula jornada; cifrado/acceso según RT-11.10 cuando aplica |
| version | INTEGER | No sobrescribir tarifa aplicada a un viaje | Sí | Liquidación y costeo | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| id_respaldo | UUID | Referencia a DOCUMENTO_RESPALDO | Sí | Liquidación y costeo | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |

## COSTO_VERSION

Propietario de atributos: Liquidación y costeo. La tabla define el contrato del registro.

| Atributo | Tipo | Dominio y regla | Obligatorio | Propietario | Sensibilidad/tratamiento |
|---|---|---|---|---|---|
| id_costo | UUID | PK; generado una vez y preservado en reintentos | Sí | Liquidación y costeo | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| id_viaje | UUID | Referencia a VIAJE | Sí | Liquidación y costeo | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| version | INTEGER | INTEGER >0; único por viaje | Sí | Liquidación y costeo | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| estado | TEXT | PRELIMINAR / ACTUALIZADO / DEFINITIVO | Sí | Liquidación y costeo | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| costo_total | NUMERIC | Importe con moneda y redondeo | Sí | Liquidación y costeo | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| distancia_km | NUMERIC | Denominador y origen medido/estimado; no dividir por cero | Sí | Liquidación y costeo | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| componentes | JSONB | Datos medidos, estimados y pendientes identificados; esquema versionado | Sí | Liquidación y costeo | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| fuentes | JSONB | IDs de lotes/telemetría/tarifa y versiones usadas; esquema versionado | Sí | Liquidación y costeo | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| calculado_utc | TIMESTAMPTZ | v1 no más de 24 h tras cierre | Sí | Liquidación y costeo | Operacional; personal si vincula jornada; cifrado/acceso según RT-11.10 cuando aplica |
| regla_version | TEXT | Fórmula y supuestos reproducibles | Sí | Liquidación y costeo | Operacional; cifrado/acceso según RT-11.10 cuando aplica |

## LIQUIDACION

Propietario de atributos: Liquidación y costeo. La tabla define el contrato del registro.

| Atributo | Tipo | Dominio y regla | Obligatorio | Propietario | Sensibilidad/tratamiento |
|---|---|---|---|---|---|
| id_liquidacion | UUID | PK; generado una vez y preservado en reintentos | Sí | Liquidación y costeo | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| id_transportista | UUID | Referencia a TRANSPORTISTA | Sí | Liquidación y costeo | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| periodo | TEXT | Mes y versión; único por transportista/periodo/versión | Sí | Liquidación y costeo | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| estado | TEXT | BORRADOR / EN_REVISION / APROBADA / REGISTRADA | Sí | Liquidación y costeo | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| importe_total | NUMERIC | Importe conciliado; moneda declarada | Sí | Liquidación y costeo | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| id_aceptacion_firmada | UUID | Referencia a DOCUMENTO_RESPALDO | Al aprobar | Liquidación y costeo | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| operacion_contable_id | TEXT | Acuse externo; NULL mientras pendiente | No | Liquidación y costeo | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| clave_idempotencia | TEXT | Evita doble registro en contable | Sí | Liquidación y costeo | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| aprobado_utc | TIMESTAMPTZ | Aceptación efectiva | No | Liquidación y costeo | Operacional; personal si vincula jornada; cifrado/acceso según RT-11.10 cuando aplica |

## LIQUIDACION_DETALLE

Propietario de atributos: Liquidación y costeo. La tabla define el contrato del registro.

| Atributo | Tipo | Dominio y regla | Obligatorio | Propietario | Sensibilidad/tratamiento |
|---|---|---|---|---|---|
| id_liquidacion | UUID | Referencia a LIQUIDACION; parte de PK | Sí | Liquidación y costeo | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| id_viaje | UUID | Referencia a VIAJE; parte de PK | Sí | Liquidación y costeo | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| id_costo | UUID | Referencia a COSTO_VERSION usado | Sí | Liquidación y costeo | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| id_tarifa | UUID | Referencia a TARIFA_CONTRATO | Sí | Liquidación y costeo | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| importe | NUMERIC | Monto y conceptos conciliados | Sí | Liquidación y costeo | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| discrepancia | TEXT | Observación y resolución; no excluir sin historia | No | Liquidación y costeo | Operacional; cifrado/acceso según RT-11.10 cuando aplica |

## LOTE_COSTO

Propietario de atributos: Liquidación y costeo. La tabla define el contrato del registro.

| Atributo | Tipo | Dominio y regla | Obligatorio | Propietario | Sensibilidad/tratamiento |
|---|---|---|---|---|---|
| id_lote | UUID | PK; generado una vez y preservado en reintentos | Sí | Liquidación y costeo | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| fuente | TEXT | COMBUSTIBLE / PEAJE / OTRA | Sí | Liquidación y costeo | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| clave_fuente | TEXT | ID único por proveedor/lote | Sí | Liquidación y costeo | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| id_original | UUID | Referencia a DOCUMENTO_RESPALDO | Sí | Liquidación y costeo | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| recibido_utc | TIMESTAMPTZ | Recepción | Sí | Liquidación y costeo | Operacional; personal si vincula jornada; cifrado/acceso según RT-11.10 cuando aplica |
| totales | TEXT | Cantidad e importes originales y conciliados | Sí | Liquidación y costeo | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| errores | TEXT | Informe por registro; carga parcial trazada | Sí | Liquidación y costeo | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| estado | TEXT | RECIBIDO / CONCILIADO / PARCIAL / RECHAZADO | Sí | Liquidación y costeo | Operacional; cifrado/acceso según RT-11.10 cuando aplica |

## INTERVENCION_TALLER

Propietario de atributos: Flota y activos. La tabla define el contrato del registro.

| Atributo | Tipo | Dominio y regla | Obligatorio | Propietario | Sensibilidad/tratamiento |
|---|---|---|---|---|---|
| id_intervencion | UUID | PK; generado una vez y preservado en reintentos | Sí | Flota y activos | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| id_tracto | UUID | Referencia a TRACTOCAMION | Excluyente | Flota y activos | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| id_semirremolque | UUID | Referencia a SEMIRREMOLQUE | Excluyente | Flota y activos | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| taller | TEXT | Propio/externo y responsable identificado | Sí | Flota y activos | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| tipo | TEXT | Preventiva / correctiva / neumático; catálogo | Sí | Flota y activos | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| odometro_km | NUMERIC | Medido cuando disponible | No | Flota y activos | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| estado | TEXT | PROGRAMADA / EJECUTADA / VALIDADA | Sí | Flota y activos | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| id_respaldo | UUID | Referencia a DOCUMENTO_RESPALDO | Al validar | Flota y activos | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| ejecutado_utc | TIMESTAMPTZ | Fecha efectiva | No | Flota y activos | Operacional; personal si vincula jornada; cifrado/acceso según RT-11.10 cuando aplica |

## POSICION_NEUMATICO

Propietario de atributos: Flota y activos. La tabla define el contrato del registro.

| Atributo | Tipo | Dominio y regla | Obligatorio | Propietario | Sensibilidad/tratamiento |
|---|---|---|---|---|---|
| id_posicion | UUID | PK; generado una vez y preservado en reintentos | Sí | Flota y activos | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| id_tracto | UUID | Referencia a TRACTOCAMION; sujeto exclusivo | Excluyente | Flota y activos | Operacional; acceso restringido |
| id_semirremolque | UUID | Referencia a SEMIRREMOLQUE; sujeto exclusivo | Excluyente | Flota y activos | Operacional; acceso restringido |
| ubicacion | TEXT | Eje/lado; catálogo por vehículo | Sí | Flota y activos | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| neumatico_id | TEXT | Identidad trazable | Sí | Flota y activos | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| km_acumulado | NUMERIC | Derivado de odómetro y montaje; no inventar medición | No | Flota y activos | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| montado_utc | TIMESTAMPTZ | Inicio | Sí | Flota y activos | Operacional; personal si vincula jornada; cifrado/acceso según RT-11.10 cuando aplica |
| retirado_utc | TIMESTAMPTZ | Fin | No | Flota y activos | Operacional; personal si vincula jornada; cifrado/acceso según RT-11.10 cuando aplica |
| id_intervencion | UUID | Referencia a INTERVENCION_TALLER | Sí | Flota y activos | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |

## SINIESTRO

Propietario de atributos: Operación de fletes. La tabla define el contrato del registro.

| Atributo | Tipo | Dominio y regla | Obligatorio | Propietario | Sensibilidad/tratamiento |
|---|---|---|---|---|---|
| id_siniestro | UUID | PK; generado una vez y preservado en reintentos | Sí | Operación de fletes | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| id_viaje | UUID | Referencia a VIAJE | No | Operación de fletes | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| equipo_persona | JSONB | Referencias de activos/personas afectadas; esquema versionado | Sí | Operación de fletes | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| evento_utc | TIMESTAMPTZ | Hora conocida; precisión/origen declarados | Sí | Operación de fletes | Operacional; personal si vincula jornada; cifrado/acceso según RT-11.10 cuando aplica |
| tipo | TEXT | Catálogo de incidentes/siniestros | Sí | Operación de fletes | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| expediente | JSONB | Referencias a originales, peritajes y resoluciones; esquema versionado | Sí | Operación de fletes | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| estado | TEXT | ABIERTO / EN_TRAMITE / CERRADO | Sí | Operación de fletes | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| retencion_litigio | BOOLEAN | BOOLEAN; conserva hasta resolución aplicable | Sí | Operación de fletes | Operacional; cifrado/acceso según RT-11.10 cuando aplica |

## AUDITORIA_EVENTO

Propietario de atributos: Seguridad y auditoría. La tabla define el contrato del registro.

| Atributo | Tipo | Dominio y regla | Obligatorio | Propietario | Sensibilidad/tratamiento |
|---|---|---|---|---|---|
| id_auditoria | UUID | PK; generado una vez y preservado en reintentos | Sí | Seguridad y auditoría | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| actor_dispositivo | TEXT | Identidades y origen | Sí | Seguridad y auditoría | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| entidad_id | TEXT | Tipo e ID del registro consultado/modificado | Sí | Seguridad y auditoría | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| operacion | TEXT | CREAR / MODIFICAR / CONSULTAR / RECTIFICAR / ELIMINAR_AUTORIZADO | Sí | Seguridad y auditoría | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| valores | JSONB | Antes/después o campos mostrados; cifrado si procede; esquema versionado | Sí | Seguridad y auditoría | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| evento_utc | TIMESTAMPTZ | Fecha y zona conservadas | Sí | Seguridad y auditoría | Operacional; personal si vincula jornada; cifrado/acceso según RT-11.10 cuando aplica |
| correlacion | TEXT | Operación end to end | Sí | Seguridad y auditoría | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| cadena_id | UUID | Identificador de cadena | Sí | Seguridad y auditoría | Operacional; acceso restringido |
| secuencia | BIGINT | >0; UNIQUE(cadena_id,secuencia) | Sí | Seguridad y auditoría | Operacional; acceso restringido |
| hash_actual | TEXT | 64 hex; registro canónico | Sí | Seguridad y auditoría | Operacional; acceso restringido |
| hash_previo | TEXT | 64 hex; NULL sólo inicio de cadena | Condicional | Seguridad y auditoría | Operacional; acceso restringido |
| manifiesto_worm | TEXT | Anclaje sellado e ID de segmento | Sí | Seguridad y auditoría | Operacional; cifrado/acceso según RT-11.10 cuando aplica |

## OUTBOX_EVENTO

Propietario de atributos: Contexto productor del evento. La tabla define el contrato del registro.

| Atributo | Tipo | Dominio y regla | Obligatorio | Propietario | Sensibilidad/tratamiento |
|---|---|---|---|---|---|
| id_evento | UUID | PK; generado una vez y preservado en reintentos | Sí | Contexto productor del evento | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| agregado_id | TEXT | ID, tipo y versión del agregado | Sí | Contexto productor del evento | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| tipo_esquema | TEXT | Contrato de evento y versión | Sí | Contexto productor del evento | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| payload | JSONB | JSON validado; datos mínimos autorizados; esquema versionado | Sí | Contexto productor del evento | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| creado_utc | TIMESTAMPTZ | Mismo commit que cambio de negocio | Sí | Contexto productor del evento | Operacional; personal si vincula jornada; cifrado/acceso según RT-11.10 cuando aplica |
| clave_particion | TEXT | Agregado/equipo para orden | Sí | Contexto productor del evento | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| estado | TEXT | PENDIENTE / PUBLICADO; acuse no equivale a consumo final | Sí | Contexto productor del evento | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| intentos | INTEGER | ≥0 | Sí | Contexto productor del evento | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| proximo_intento_utc | TIMESTAMPTZ | Fecha de reintento; NULL si publicado | No | Contexto productor del evento | Operacional; acceso restringido |
| correlacion | TEXT | ID común de solicitud y efectos | Sí | Contexto productor del evento | Operacional; cifrado/acceso según RT-11.10 cuando aplica |

## Restricciones transversales y custodia

VIGENCIA_HABILITACION, INTERVENCION_TALLER y POSICION_NEUMATICO usan FK explícitas y un CHECK de sujeto exclusivo; no una FK polimórfica ficticia. VIAJE puede existir programado sin recursos. ASIGNACION confirmada exige recursos válidos, evaluación y rangos activos no superpuestos; una reserva rechazada no termina el viaje. DOCUMENTO_TRANSPORTE requiere original y representación conforme antes de salir; el contable es el único emisor.

EVIDENCIA_JORNADA válida exige código homologado, nivel 0–5 y controles de integridad; 0 sólo REG_COND. Las fuentes desconocidas/inválidas tienen nivel NULL y motivo conservado. SIN_EVIDENCIA se registra en la evaluación, sin fabricar un artefacto. La evaluación puede referenciar múltiples fuentes mediante EVALUACION_EVIDENCIA; reposo nivel 4 y atestación nivel 5 no se colapsan en una fuente. Ninguna causa legal admite EXCEPCION_RN04.

El sello encadenado incluye ID de cadena, secuencia, bytes canónicos, hash previo y hash actual; sólo un registro inicial tiene hash previo NULL. Rectificación genera registro nuevo. Originales, manifiestos y claves de firma se conservan/administran separados; el hash no es firma. Las cuentas aplicativas no sobrescriben evidencia; almacenamiento WORM bloqueado y verificación independiente sostienen el control contra administradores.

Se indexan FK locales y claves de consulta. RUT cifrado utiliza índice ciego de deduplicación con clave separada; no se presume búsqueda SQL de texto sobre AES-GCM. VIAJE se mantiene sin partición inicial. Particionar una tabla PostgreSQL exige compatibilizar PK/UNIQUE con su clave de partición y revisar referencias. Las políticas de supresión contemplan retención, litigio, claves compartidas y todas las copias.

## Supuestos de capacidad y migración

FEP03 · numeral 14.2 · p.30 pide estimación; la Tabla A5.1 diferencia tasas del Caso, tamaños supuestos y conteos históricos no entregados.

**Tabla A5.1.** Presupuesto lógico inicial de datos, sin índices ni réplicas

| Dominio | Base / supuesto | Resultado de diseño |
|---|---|---|
| Viajes | 96.000/año ×2 KiB/registro compuesto | ≈197 MB/año; 5 años ≈983 MB, sin documentos |
| Evaluaciones | 3 intentos/viaje ×96.000 ×1 KiB | ≈295 MB/año; intentos reales por medir |
| Documentos de transporte | 128.000/año ×20 KiB por XML/representación | ≈2,62 GB/año; 6 años ≈15,73 GB. No acredita tamaño para envío SBD |
| Evidencia de jornada | 454 conductores ×365 ×15 eventos/día ×512 bytes | ≈1,27 GB/año; 5 años ≈6,36 GB, sin originales de tacógrafo/atestaciones |
| Vigencias vivas | ≈6.000 ×100 KiB de respaldo medio | ≈614 MB por lote; tamaño y versiones por medir |
| Telemetría de posición | 119,82 millones/año ×64 bytes | ≈7,67 GB/año, escenario completo de S4.1.20 |
| Viajes históricos a migrar | 96.000/año ×5 sólo como extrapolación | ≈480.000 registros; contar el histórico real antes de dimensionar corte |
| Liquidaciones históricas | 148/mes ×12 ×6 sólo como extrapolación | ≈10.656 registros; verificar períodos, versiones y transportistas reales |
| Siniestros y maestros | Totalidad de la fuente según RT-05.15 | No hay conteo/bytes entregados; inventariar todos y preservar pendientes |

La Tabla A5.1 no es tamaño físico ni cifra medida. Un factor provisional 3× sobre registros cubre índices/estructura de manera aproximada, pero WAL, originales grandes, fotos, copias WORM, respaldos y réplicas se dimensionan explícitamente por separado. No se multiplica por un factor sin indicar qué incluye. El volumen de jornada se registra por eventos semánticos, sin convertir cada ping de GPS en prueba de descanso. Se ensayan extracción, transformación, carga y conciliación con tasa medida; volumen/tasa más delta final determina la ventana, conciliada con S7.

## Declaración de uso de IA

OpenAI Codex (GPT-6), 11-10-2026: elaboración sustancial asistida del diccionario y supuestos, Alto en texto y Ninguno en diagramas. Revisión humana pendiente: D3 valida atributos, propietarios y restricciones; D1 coteja evidencia/veredicto; D4 concilia capacidad/retención.
