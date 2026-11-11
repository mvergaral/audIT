# Anexo independiente del Subdocumento 5

## 5.5 Anexo. Diccionario de datos y supuestos de capacidad

\addcontentsline{toc}{section}{Anexo. Diccionario de datos y supuestos de capacidad}
\markright{Anexo. Diccionario de datos}
El diccionario especifica el modelo propuesto, por dominio, conforme a FEP02, RT-05.01, p. 11 y Comunicado 10 · capítulo 5. Las figuras del cuerpo seleccionan relaciones críticas para mantener legibilidad; aquí se explicitan atributos y controles. El catálogo se valida con los propietarios y fuentes del CLIENTE antes de congelar el esquema.

UUID identifica globalmente sin renumerar un original. TIMESTAMPTZ conserva un instante normalizado; la zona/offset de origen se registra aparte cuando importa; el valor original de fuente se guarda cuando su interpretación sea incierta. NULL significa ausente/desconocido cuando corresponde y nunca se rellena con cero. Las referencias entre contextos son lógicas y se validan por contratos; las FK físicas se implementan en las tablas locales del contexto. Una etiqueta PK/FK en el modelo no impone acceso directo a otra base. Los campos condicionales se exigen al confirmar su estado; una recepción incompleta se conserva sin habilitar operación. Los catálogos TEXT se validan con CHECK o catálogo versionado; JSONB requiere esquema y versión explícitos.

### 5.5.1 CLIENTE

Propietario de atributos: Contable (identidad comercial); Planificación (atributos operacionales). La tabla define el contrato del registro.

La Tabla 5.7 detalla los atributos y controles del registro.

**Tabla 5.7.** Atributos y controles de CLIENTE

| Atributo | Tipo | Dominio y regla | Obligatorio | Propietario | Sensibilidad/tratamiento |
|---|---|---|---|---|---|
| id_\allowbreak{}cliente | UUID | PK; generado una vez y preservado en reintentos | Sí | Planificación y tráfico | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| rut | TEXT | Identificador chileno validado; cifrado e índice ciego | Sí | Sistema contable | Personal si identifica persona natural; cifrado/acceso según RT-11.10 cuando aplica |
| razon_\allowbreak{}social | TEXT | Denominación acreditada | Sí | Sistema contable | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| estado | TEXT | ACTIVO / INACTIVO | Sí | Planificación y tráfico | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| referencia_\allowbreak{}contable | TEXT | ID externo homologado; unicidad por sistema | Sí | Sistema contable | Operacional; cifrado/acceso según RT-11.10 cuando aplica |

Estos atributos concretan las referencias, campos obligatorios y controles de acceso de CLIENTE.

### 5.5.2 TRANSPORTISTA

Propietario de atributos: Contable (identidad comercial); Personas y Flota (adhesión y recursos). La tabla define el contrato del registro.

La Tabla 5.8 detalla los atributos y controles del registro.

**Tabla 5.8.** Atributos y controles de TRANSPORTISTA

| Atributo | Tipo | Dominio y regla | Obligatorio | Propietario | Sensibilidad/tratamiento |
|---|---|---|---|---|---|
| id_\allowbreak{}transportista | UUID | PK; generado una vez y preservado en reintentos | Sí | Flota y activos | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| rut | TEXT | Identificador validado; cifrado e índice ciego | Sí | Sistema contable | Personal si identifica persona natural; cifrado/acceso según RT-11.10 cuando aplica |
| razon_\allowbreak{}social | TEXT | Denominación acreditada | Sí | Sistema contable | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| referencia_\allowbreak{}contable | TEXT | ID homologado | Sí | Sistema contable | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| estado_\allowbreak{}adhesion | TEXT | COMPLETA / DATOS / SIN_\allowbreak{}ADHESION; versionado | Sí | Flota y activos | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| id_\allowbreak{}documento_\allowbreak{}adhesion | UUID | Referencia a DOCUMENTO_\allowbreak{}RESPALDO | Condicional | Flota y activos | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| adhesion_\allowbreak{}desde | TIMESTAMPTZ | Inicio de vigencia contractual | Condicional | Flota y activos | Operacional; personal si vincula jornada; cifrado/acceso según RT-11.10 cuando aplica |
| adhesion_\allowbreak{}hasta | TIMESTAMPTZ | Vencimiento; NULL si sin fin fijado | No | Flota y activos | Operacional; personal si vincula jornada; cifrado/acceso según RT-11.10 cuando aplica |

Estos atributos concretan las referencias, campos obligatorios y controles de acceso de TRANSPORTISTA.

### 5.5.3 CONDUCTOR

Propietario de atributos: Personas y cumplimiento. La tabla define el contrato del registro.

La Tabla 5.9 detalla los atributos y controles del registro.

**Tabla 5.9.** Atributos y controles de CONDUCTOR

| Atributo | Tipo | Dominio y regla | Obligatorio | Propietario | Sensibilidad/tratamiento |
|---|---|---|---|---|---|
| id_\allowbreak{}conductor | UUID | PK; generado una vez y preservado en reintentos | Sí | Personas y cumplimiento | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| id_\allowbreak{}transportista | UUID | Referencia a TRANSPORTISTA; NULL propio | No | Personas y cumplimiento | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| rut | TEXT | Identificador validado, cifrado e índice ciego | Sí | Personas y cumplimiento | Personal; cifrado/acceso según RT-11.10 cuando aplica |
| nombre_\allowbreak{}completo | TEXT | Nombre acreditado; cifrado | Sí | Personas y cumplimiento | Personal; cifrado/acceso según RT-11.10 cuando aplica |
| clase_\allowbreak{}licencia | TEXT | Catálogo homologado; aptitud según vehículo | Sí | Personas y cumplimiento | Personal; cifrado/acceso según RT-11.10 cuando aplica |
| estado_\allowbreak{}operativo | TEXT | HABILITADO / BLOQUEADO; no sustituye evaluación | Sí | Personas y cumplimiento | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| id_\allowbreak{}documento_\allowbreak{}identidad | UUID | Referencia a DOCUMENTO_\allowbreak{}RESPALDO | Sí | Personas y cumplimiento | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| actualizado_\allowbreak{}utc | TIMESTAMPTZ | Última actualización acreditada | Sí | Personas y cumplimiento | Operacional; personal si vincula jornada; cifrado/acceso según RT-11.10 cuando aplica |

Estos atributos concretan las referencias, campos obligatorios y controles de acceso de CONDUCTOR.

### 5.5.4 TRACTOCAMION

Propietario de atributos: Flota y activos. La tabla define el contrato del registro.

La Tabla 5.10 detalla los atributos y controles del registro.

**Tabla 5.10.** Atributos y controles de TRACTOCAMION

| Atributo | Tipo | Dominio y regla | Obligatorio | Propietario | Sensibilidad/tratamiento |
|---|---|---|---|---|---|
| id_\allowbreak{}tracto | UUID | PK; generado una vez y preservado en reintentos | Sí | Flota y activos | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| patente | TEXT | Normalizada y única en el registro maestro | Sí | Flota y activos | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| tipo_\allowbreak{}propiedad | TEXT | PROPIO / TERCERO | Sí | Flota y activos | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| id_\allowbreak{}transportista | UUID | Referencia a TRANSPORTISTA; NULL si propio | No | Flota y activos | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| modelo | TEXT | Modelo y fabricante homologados | Sí | Flota y activos | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| estado | TEXT | DISPONIBLE / RESERVADO / MANTENCION / FUERA_\allowbreak{}SERVICIO | Sí | Flota y activos | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| acceso_\allowbreak{}fabrica | TEXT | AUTORIZADO / NO_\allowbreak{}AUTORIZADO / NO_\allowbreak{}DISPONIBLE; no booleano inferido | Sí | Flota y activos | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| mapa_\allowbreak{}senales_\allowbreak{}version | TEXT | Protocolo y señales autorizadas | No | Flota y activos | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| id_\allowbreak{}dispositivo | UUID | Referencia a DISPOSITIVO | No | Flota y activos | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |

Estos atributos concretan las referencias, campos obligatorios y controles de acceso de TRACTOCAMION.

### 5.5.5 SEMIRREMOLQUE

Propietario de atributos: Flota y activos. La tabla define el contrato del registro.

La Tabla 5.11 detalla los atributos y controles del registro.

**Tabla 5.11.** Atributos y controles de SEMIRREMOLQUE

| Atributo | Tipo | Dominio y regla | Obligatorio | Propietario | Sensibilidad/tratamiento |
|---|---|---|---|---|---|
| id_\allowbreak{}semirremolque | UUID | PK; generado una vez y preservado en reintentos | Sí | Flota y activos | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| patente | TEXT | Identificador normalizado; tercero según inventario | Sí | Flota y activos | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| tipo_\allowbreak{}carroceria | TEXT | Catálogo de compatibilidad de carga | Sí | Flota y activos | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| capacidad_\allowbreak{}kg | NUMERIC | >0; según certificado, no rango universal inventado | Sí | Flota y activos | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| tipo_\allowbreak{}propiedad | TEXT | PROPIO / TERCERO | Sí | Flota y activos | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| id_\allowbreak{}transportista | UUID | Referencia a TRANSPORTISTA | No | Flota y activos | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| estado | TEXT | Disponibilidad y aptitud versionadas | Sí | Flota y activos | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| id_\allowbreak{}baliza | TEXT | ID registrado y homologado; no evidencia personal | No | Flota y activos | Operacional; cifrado/acceso según RT-11.10 cuando aplica |

Estos atributos concretan las referencias, campos obligatorios y controles de acceso de SEMIRREMOLQUE.

### 5.5.6 PUNTO_\allowbreak{}SERVICIO

Propietario de atributos: Planificación y tráfico. La tabla define el contrato del registro.

La Tabla 5.12 detalla los atributos y controles del registro.

**Tabla 5.12.** Atributos y controles de PUNTO_\allowbreak{}SERVICIO

| Atributo | Tipo | Dominio y regla | Obligatorio | Propietario | Sensibilidad/tratamiento |
|---|---|---|---|---|---|
| id_\allowbreak{}punto | UUID | PK; generado una vez y preservado en reintentos | Sí | Planificación y tráfico | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| id_\allowbreak{}cliente | UUID | Referencia a CLIENTE | No | Planificación y tráfico | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| tipo | TEXT | ORIGEN / DESTINO / TERMINAL / TALLER / PARADOR | Sí | Planificación y tráfico | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| nombre | TEXT | Denominación operacional | Sí | Planificación y tráfico | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| geometria | GEOMETRY(Polygon,4326) | PostGIS GEOMETRY, SRID 4326; validar polígono y versión | Condicional | Planificación y tráfico | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| margen_\allowbreak{}geocerca | NUMERIC | Parámetro calibrado; unidad declarada | Condicional | Planificación y tráfico | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| version | INTEGER | Versión usada por el equipo | Sí | Planificación y tráfico | Operacional; cifrado/acceso según RT-11.10 cuando aplica |

Estos atributos concretan las referencias, campos obligatorios y controles de acceso de PUNTO_\allowbreak{}SERVICIO.

### 5.5.7 ORDEN_\allowbreak{}TRANSPORTE

Propietario de atributos: Planificación y tráfico. La tabla define el contrato del registro.

La Tabla 5.13 detalla los atributos y controles del registro.

**Tabla 5.13.** Atributos y controles de ORDEN_\allowbreak{}TRANSPORTE

| Atributo | Tipo | Dominio y regla | Obligatorio | Propietario | Sensibilidad/tratamiento |
|---|---|---|---|---|---|
| id_\allowbreak{}orden | UUID | PK; generado una vez y preservado en reintentos | Sí | Planificación y tráfico | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| id_\allowbreak{}cliente | UUID | Referencia a CLIENTE | Sí | Planificación y tráfico | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| id_\allowbreak{}origen | UUID | Referencia a PUNTO_\allowbreak{}SERVICIO | Sí | Planificación y tráfico | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| id_\allowbreak{}destino | UUID | Referencia a PUNTO_\allowbreak{}SERVICIO | Sí | Planificación y tráfico | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| carga | TEXT | Tipo/código y especificación del servicio | Sí | Planificación y tráfico | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| peso_\allowbreak{}previsto_\allowbreak{}kg | NUMERIC | >0 cuando disponible; no sustituye pesaje definitivo | No | Planificación y tráfico | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| requiere_\allowbreak{}semirremolque | BOOLEAN | BOOLEAN; determina campo obligatorio al asignar | Sí | Planificación y tráfico | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| estado | TEXT | ABIERTA / PROGRAMADA / CUMPLIDA / CANCELADA | Sí | Planificación y tráfico | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| fecha_\allowbreak{}servicio | TIMESTAMPTZ | Fecha programada; zona origen conservada | Sí | Planificación y tráfico | Operacional; personal si vincula jornada; cifrado/acceso según RT-11.10 cuando aplica |

Estos atributos concretan las referencias, campos obligatorios y controles de acceso de ORDEN_\allowbreak{}TRANSPORTE.

### 5.5.8 VIAJE

Propietario de atributos: Operación de fletes. La tabla define el contrato del registro.

La Tabla 5.14 detalla los atributos y controles del registro.

**Tabla 5.14.** Atributos y controles de VIAJE

| Atributo | Tipo | Dominio y regla | Obligatorio | Propietario | Sensibilidad/tratamiento |
|---|---|---|---|---|---|
| id_\allowbreak{}viaje | UUID | PK; generado una vez y preservado en reintentos | Sí | Operación de fletes | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| id_\allowbreak{}orden | UUID | Referencia a ORDEN_\allowbreak{}TRANSPORTE | Sí | Operación de fletes | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| codigo_\allowbreak{}viaje | TEXT | Identificador único legible | Sí | Operación de fletes | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| estado_\allowbreak{}viaje | TEXT | PROGRAMADO / EN_\allowbreak{}CARGA / EN_\allowbreak{}RUTA / EN_\allowbreak{}DESCARGA / CERRADO / CANCELADO | Sí | Operación de fletes | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| peso_\allowbreak{}origen_\allowbreak{}kg | NUMERIC | Pesaje definitivo; obligatorio antes de salida si aplica | Condicional | Operación de fletes | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| id_\allowbreak{}punto_\allowbreak{}actual | UUID | Referencia a PUNTO_\allowbreak{}SERVICIO | No | Operación de fletes | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| inicio_\allowbreak{}utc | TIMESTAMPTZ | Inicio efectivo | No | Operación de fletes | Operacional; personal si vincula jornada; cifrado/acceso según RT-11.10 cuando aplica |
| cierre_\allowbreak{}utc | TIMESTAMPTZ | Cierre efectivo | No | Operación de fletes | Operacional; personal si vincula jornada; cifrado/acceso según RT-11.10 cuando aplica |
| version | INTEGER | Entero positivo para control optimista | Sí | Operación de fletes | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| motivo_\allowbreak{}cancelacion | TEXT | Obligatorio al cancelar | Condicional | Operación de fletes | Operacional; cifrado/acceso según RT-11.10 cuando aplica |

Estos atributos concretan las referencias, campos obligatorios y controles de acceso de VIAJE.

### 5.5.9 ASIGNACION

Propietario de atributos: Planificación y tráfico. La tabla define el contrato del registro.

La Tabla 5.15 detalla los atributos y controles del registro.

**Tabla 5.15.** Atributos y controles de ASIGNACION

| Atributo | Tipo | Dominio y regla | Obligatorio | Propietario | Sensibilidad/tratamiento |
|---|---|---|---|---|---|
| id_\allowbreak{}asignacion | UUID | PK; generado una vez y preservado en reintentos | Sí | Planificación y tráfico | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| id_\allowbreak{}viaje | UUID | Referencia a VIAJE | Sí | Planificación y tráfico | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| id_\allowbreak{}conductor | UUID | Referencia a CONDUCTOR | Al confirmar | Planificación y tráfico | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| id_\allowbreak{}tracto | UUID | Referencia a TRACTOCAMION | Al confirmar | Planificación y tráfico | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| id_\allowbreak{}semirremolque | UUID | Referencia a SEMIRREMOLQUE | Si carga lo exige | Planificación y tráfico | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| id_\allowbreak{}transportista | UUID | Referencia a TRANSPORTISTA | Si tercero | Planificación y tráfico | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| desde_\allowbreak{}utc | TIMESTAMPTZ | Inicio de reserva | Sí | Planificación y tráfico | Operacional; personal si vincula jornada; cifrado/acceso según RT-11.10 cuando aplica |
| hasta_\allowbreak{}utc | TIMESTAMPTZ | Fin; NULL activa | No | Planificación y tráfico | Operacional; personal si vincula jornada; cifrado/acceso según RT-11.10 cuando aplica |
| estado | TEXT | PROPUESTA / CONFIRMADA / LIBERADA / RECHAZADA | Sí | Planificación y tráfico | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| clave_\allowbreak{}idempotencia | TEXT | Única por cliente de API y operación; persistencia duradera | Sí | Planificación y tráfico | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| version_\allowbreak{}recursos | TEXT | Versiones de validación usadas | Sí | Planificación y tráfico | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| correlacion | TEXT | ID común de la operación | Sí | Planificación y tráfico | Operacional; cifrado/acceso según RT-11.10 cuando aplica |

Estos atributos concretan las referencias, campos obligatorios y controles de acceso de ASIGNACION.

### 5.5.10 DOCUMENTO_\allowbreak{}RESPALDO

Propietario de atributos: Propietario del dominio que aporta el documento. La tabla define el contrato del registro.

La Tabla 5.16 detalla los atributos y controles del registro.

**Tabla 5.16.** Atributos y controles de DOCUMENTO_\allowbreak{}RESPALDO

| Atributo | Tipo | Dominio y regla | Obligatorio | Propietario | Sensibilidad/tratamiento |
|---|---|---|---|---|---|
| id_\allowbreak{}documento | UUID | PK; generado una vez y preservado en reintentos | Sí | Dominio del documento: Personas, Flota u Operación, uno por registro | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| tipo_\allowbreak{}documento | TEXT | Catálogo versionado; no se inventa total de tipos | Sí | Dominio del documento: Personas, Flota u Operación, uno por registro | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| hash_\allowbreak{}sha256 | TEXT | 64 hex; hash del original exacto | Sí | Dominio del documento: Personas, Flota u Operación, uno por registro | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| uri | TEXT | Objeto inmutable; sin secretos en URI | Sí | Dominio del documento: Personas, Flota u Operación, uno por registro | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| emisor | TEXT | Responsable u origen acreditado | Sí | Dominio del documento: Personas, Flota u Operación, uno por registro | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| recibido_\allowbreak{}utc | TIMESTAMPTZ | Recepción por plataforma | Sí | Dominio del documento: Personas, Flota u Operación, uno por registro | Operacional; personal si vincula jornada; cifrado/acceso según RT-11.10 cuando aplica |
| firma_\allowbreak{}estado | TEXT | VALIDA / INVALIDA / NO_\allowbreak{}APLICA / PENDIENTE; hash no es firma | Sí | Dominio del documento: Personas, Flota u Operación, uno por registro | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| retener_\allowbreak{}hasta | TIMESTAMPTZ | Fin mínimo contractual según dominio | Sí | Dominio del documento: Personas, Flota u Operación, uno por registro | Operacional; personal si vincula jornada; cifrado/acceso según RT-11.10 cuando aplica |
| retencion_\allowbreak{}litigio | BOOLEAN | BOOLEAN; prolonga sin permitir borrado anticipado | Sí | Dominio del documento: Personas, Flota u Operación, uno por registro | Operacional; cifrado/acceso según RT-11.10 cuando aplica |

Estos atributos concretan las referencias, campos obligatorios y controles de acceso de DOCUMENTO_\allowbreak{}RESPALDO.

### 5.5.11 VIGENCIA_\allowbreak{}HABILITACION

Propietario de atributos: Personas y cumplimiento (conductor); Flota y activos (equipos). La tabla define el contrato del registro.

La Tabla 5.17 detalla los atributos y controles del registro.

**Tabla 5.17.** Atributos y controles de VIGENCIA_\allowbreak{}HABILITACION

| Atributo | Tipo | Dominio y regla | Obligatorio | Propietario | Sensibilidad/tratamiento |
|---|---|---|---|---|---|
| id_\allowbreak{}vigencia | UUID | PK; generado una vez y preservado en reintentos | Sí | Dominio del sujeto: Personas o Flota, uno por registro | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| id_\allowbreak{}conductor | UUID | Referencia a CONDUCTOR | Excluyente | Personas y cumplimiento | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| id_\allowbreak{}tracto | UUID | Referencia a TRACTOCAMION | Excluyente | Flota y activos | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| id_\allowbreak{}semirremolque | UUID | Referencia a SEMIRREMOLQUE | Excluyente | Flota y activos | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| tipo_\allowbreak{}documento | TEXT | Catálogo homologado para el sujeto | Sí | Dominio del sujeto: Personas o Flota, uno por registro | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| fecha_\allowbreak{}vencimiento | DATE | DATE; cotejo documental | Sí | Dominio del sujeto: Personas o Flota, uno por registro | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| estado_\allowbreak{}verificacion | TEXT | VERIFICADO / PENDIENTE / RECHAZADO / REVOCADO | Sí | Dominio del sujeto: Personas o Flota, uno por registro | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| id_\allowbreak{}documento | UUID | Referencia a DOCUMENTO_\allowbreak{}RESPALDO | Al verificar | Dominio del sujeto: Personas o Flota, uno por registro | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| verificado_\allowbreak{}utc | TIMESTAMPTZ | Fecha real de cotejo | Al verificar | Dominio del sujeto: Personas o Flota, uno por registro | Operacional; personal si vincula jornada; cifrado/acceso según RT-11.10 cuando aplica |
| verificado_\allowbreak{}por | TEXT | Identidad del verificador | Al verificar | Dominio del sujeto: Personas o Flota, uno por registro | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| responsable_\allowbreak{}renovacion | TEXT | Rol/titular responsable; alertas 60/30/7 días | Sí | Dominio del sujeto: Personas o Flota, uno por registro | Operacional; cifrado/acceso según RT-11.10 cuando aplica |

Estos atributos concretan las referencias, campos obligatorios y controles de acceso de VIGENCIA_\allowbreak{}HABILITACION.

### 5.5.12 DISPOSITIVO

Propietario de atributos: Telemetría y geocercas. La tabla define el contrato del registro.

La Tabla 5.18 detalla los atributos y controles del registro.

**Tabla 5.18.** Atributos y controles de DISPOSITIVO

| Atributo | Tipo | Dominio y regla | Obligatorio | Propietario | Sensibilidad/tratamiento |
|---|---|---|---|---|---|
| id_\allowbreak{}dispositivo | UUID | PK; generado una vez y preservado en reintentos | Sí | Telemetría y geocercas | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| codigo_\allowbreak{}origen | TEXT | ID externo único por proveedor | Sí | Telemetría y geocercas | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| tipo | TEXT | AUDIT / TERCERO / FABRICA / TACOGRAFO | Sí | Telemetría y geocercas | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| proveedor | TEXT | Fuente homologada | Sí | Telemetría y geocercas | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| certificado_\allowbreak{}id | TEXT | Identidad por equipo cuando sea aplicable | Condicional | Telemetría y geocercas | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| version_\allowbreak{}config | TEXT | Configuración y esquema | Sí | Telemetría y geocercas | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| ultimo_\allowbreak{}acuse_\allowbreak{}utc | TIMESTAMPTZ | Último commit confirmado | No | Telemetría y geocercas | Operacional; personal si vincula jornada; cifrado/acceso según RT-11.10 cuando aplica |
| cursor_\allowbreak{}confirmado | TEXT | Secuencia duradera por flujo | No | Telemetría y geocercas | Operacional; cifrado/acceso según RT-11.10 cuando aplica |

Estos atributos concretan las referencias, campos obligatorios y controles de acceso de DISPOSITIVO.

### 5.5.13 EVIDENCIA_\allowbreak{}JORNADA

Propietario de atributos: Personas y cumplimiento. La tabla define el contrato del registro.

La Tabla 5.19 detalla los atributos y controles del registro.

**Tabla 5.19.** Atributos y controles de EVIDENCIA_\allowbreak{}JORNADA

| Atributo | Tipo | Dominio y regla | Obligatorio | Propietario | Sensibilidad/tratamiento |
|---|---|---|---|---|---|
| id_\allowbreak{}evidencia | UUID | PK; generado una vez y preservado en reintentos | Sí | Personas y cumplimiento | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| id_\allowbreak{}conductor | UUID | Referencia a CONDUCTOR; no inferir identidad | No | Personas y cumplimiento | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| id_\allowbreak{}dispositivo | UUID | Referencia a DISPOSITIVO | No | Personas y cumplimiento | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| id_\allowbreak{}documento_\allowbreak{}original | UUID | Referencia a DOCUMENTO_\allowbreak{}RESPALDO | Si hay artefacto firmado/archivo | Personas y cumplimiento | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| codigo_\allowbreak{}fuente | TEXT | Código original recibido, sin renumerarlo | Sí | Personas y cumplimiento | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| estado_\allowbreak{}evidencia | TEXT | VALIDA / CODIGO_\allowbreak{}FUENTE_\allowbreak{}DESCONOCIDO / EVIDENCIA_\allowbreak{}INVALIDA | Sí | Personas y cumplimiento | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| nivel_\allowbreak{}cascada | SMALLINT | SMALLINT NULL o 0–5; 0 sólo REG_\allowbreak{}COND; NULL no válida | Si VALIDA | Personas y cumplimiento | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| tipo_\allowbreak{}evento | TEXT | CONDUCCION / ESPERA / REPOSO / ATESTACION / VOLUNTARIO; catálogo versionado | Sí | Personas y cumplimiento | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| evento_\allowbreak{}utc | TIMESTAMPTZ | Hora de fuente interpretada; conservar original | No | Personas y cumplimiento | Operacional; personal si vincula jornada; cifrado/acceso según RT-11.10 cuando aplica |
| recibido_\allowbreak{}utc | TIMESTAMPTZ | Hora de recepción | Sí | Personas y cumplimiento | Operacional; personal si vincula jornada; cifrado/acceso según RT-11.10 cuando aplica |
| marca_\allowbreak{}original | TEXT | Hora/offset/código original para interpretación | No | Personas y cumplimiento | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| calidad_\allowbreak{}reloj | TEXT | GNSS / NTP / NO_\allowbreak{}SINCRONIZADO / DESCONOCIDO; deriva cuando medible | Sí | Personas y cumplimiento | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| odometro_\allowbreak{}km | NUMERIC | ≥0 cuando medido; NULL ausente | No | Personas y cumplimiento | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| velocidad_\allowbreak{}kmh | NUMERIC | ≥0 cuando medida; NULL ausente | No | Personas y cumplimiento | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| cadena_\allowbreak{}id | TEXT | Identificador de cadena de custodia | Sí | Personas y cumplimiento | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| secuencia_\allowbreak{}custodia | BIGINT | BIGINT >0; único por cadena | Sí | Personas y cumplimiento | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| hash_\allowbreak{}sha256 | TEXT | 64 hex; registro canónico y referencia al original | Sí | Personas y cumplimiento | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| hash_\allowbreak{}previo | TEXT | 64 hex; NULL sólo al inicio de cadena | Condicional | Personas y cumplimiento | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| rectifica_\allowbreak{}id | UUID | Referencia a EVIDENCIA_\allowbreak{}JORNADA original | No | Personas y cumplimiento | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| mapeo_\allowbreak{}version | TEXT | Versión origen$\rightarrow$nivel aplicada | Sí | Personas y cumplimiento | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| motivo_\allowbreak{}invalidez | TEXT | Obligatorio para fuente desconocida/inválida | Condicional | Personas y cumplimiento | Operacional; cifrado/acceso según RT-11.10 cuando aplica |

Estos atributos concretan las referencias, campos obligatorios y controles de acceso de EVIDENCIA_\allowbreak{}JORNADA.

### 5.5.14 EVALUACION_\allowbreak{}ASIGNACION

Propietario de atributos: Personas y cumplimiento. La tabla define el contrato del registro.

La Tabla 5.20 detalla los atributos y controles del registro.

**Tabla 5.20.** Atributos y controles de EVALUACION_\allowbreak{}ASIGNACION

| Atributo | Tipo | Dominio y regla | Obligatorio | Propietario | Sensibilidad/tratamiento |
|---|---|---|---|---|---|
| id_\allowbreak{}evaluacion | UUID | PK; generado una vez y preservado en reintentos | Sí | Personas y cumplimiento | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| id_\allowbreak{}asignacion | UUID | Referencia a ASIGNACION | Sí | Personas y cumplimiento | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| estado_\allowbreak{}evidencia | TEXT | VALIDA / SIN_\allowbreak{}EVIDENCIA / CODIGO_\allowbreak{}FUENTE_\allowbreak{}DESCONOCIDO / EVIDENCIA_\allowbreak{}INVALIDA | Sí | Personas y cumplimiento | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| modalidad_\allowbreak{}adhesion | TEXT | COMPLETA / DATOS / SIN_\allowbreak{}ADHESION | Sí | Personas y cumplimiento | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| veredicto | TEXT | HABILITADA / HABILITADA_\allowbreak{}CON_\allowbreak{}MARCA / BLOQUEADA / EXCEPCION_\allowbreak{}RN04_\allowbreak{}APROBADA | Sí | Personas y cumplimiento | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| regla_\allowbreak{}version | TEXT | Versión de reglas y catálogo normativo aplicado | Sí | Personas y cumplimiento | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| causa | JSONB | Causales y datos faltantes estructurados; esquema versionado | Sí | Personas y cumplimiento | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| evaluado_\allowbreak{}utc | TIMESTAMPTZ | Hora de decisión | Sí | Personas y cumplimiento | Operacional; personal si vincula jornada; cifrado/acceso según RT-11.10 cuando aplica |
| correlacion | TEXT | Enlace auditable a solicitud y respuesta | Sí | Personas y cumplimiento | Operacional; cifrado/acceso según RT-11.10 cuando aplica |

Estos atributos concretan las referencias, campos obligatorios y controles de acceso de EVALUACION_\allowbreak{}ASIGNACION.

### 5.5.15 EVALUACION_\allowbreak{}EVIDENCIA

Propietario de atributos: Personas y cumplimiento. La tabla define el contrato del registro.

La Tabla 5.21 detalla los atributos y controles del registro.

**Tabla 5.21.** Atributos y controles de EVALUACION_\allowbreak{}EVIDENCIA

| Atributo | Tipo | Dominio y regla | Obligatorio | Propietario | Sensibilidad/tratamiento |
|---|---|---|---|---|---|
| id_\allowbreak{}evaluacion | UUID | Referencia a EVALUACION_\allowbreak{}ASIGNACION; parte de PK | Sí | Personas y cumplimiento | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| id_\allowbreak{}evidencia | UUID | Referencia a EVIDENCIA_\allowbreak{}JORNADA; parte de PK | Sí | Personas y cumplimiento | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| uso | TEXT | JORNADA / REPOSO / ATESTACION / AUXILIAR | Sí | Personas y cumplimiento | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| condicion_\allowbreak{}validada | JSONB | Identidad, rango temporal e integridad comprobados; esquema versionado | Sí | Personas y cumplimiento | Operacional; cifrado/acceso según RT-11.10 cuando aplica |

Estos atributos concretan las referencias, campos obligatorios y controles de acceso de EVALUACION_\allowbreak{}EVIDENCIA.

### 5.5.16 EXCEPCION_\allowbreak{}RN04

Propietario de atributos: Personas y cumplimiento. La tabla define el contrato del registro.

La Tabla 5.22 detalla los atributos y controles del registro.

**Tabla 5.22.** Atributos y controles de EXCEPCION_\allowbreak{}RN04

| Atributo | Tipo | Dominio y regla | Obligatorio | Propietario | Sensibilidad/tratamiento |
|---|---|---|---|---|---|
| id_\allowbreak{}excepcion | UUID | PK; generado una vez y preservado en reintentos | Sí | Personas y cumplimiento | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| id_\allowbreak{}evaluacion | UUID | Referencia a EVALUACION_\allowbreak{}ASIGNACION; máximo una aprobada | Sí | Personas y cumplimiento | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| motivo | TEXT | Sólo indisponibilidad de fuente; causa legal nunca elegible | Sí | Personas y cumplimiento | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| aprobador_\allowbreak{}torre | TEXT | Jefe de turno identificado | Sí | Personas y cumplimiento | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| aprobador_\allowbreak{}prevencion | TEXT | Prevención de riesgos identificada; independiente | Sí | Personas y cumplimiento | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| aprobado_\allowbreak{}utc | TIMESTAMPTZ | Antes de confirmar excepción | Sí | Personas y cumplimiento | Operacional; personal si vincula jornada; cifrado/acceso según RT-11.10 cuando aplica |
| alcance | TEXT | Un único viaje/asignación | Sí | Personas y cumplimiento | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| revisado_\allowbreak{}utc | TIMESTAMPTZ | Revisión mensual real | No | Personas y cumplimiento | Operacional; personal si vincula jornada; cifrado/acceso según RT-11.10 cuando aplica |

Estos atributos concretan las referencias, campos obligatorios y controles de acceso de EXCEPCION_\allowbreak{}RN04.

### 5.5.17 PERMISO_\allowbreak{}COMPARTIR

Propietario de atributos: Personas y cumplimiento. La tabla define el contrato del registro.

La Tabla 5.23 detalla los atributos y controles del registro.

**Tabla 5.23.** Atributos y controles de PERMISO_\allowbreak{}COMPARTIR

| Atributo | Tipo | Dominio y regla | Obligatorio | Propietario | Sensibilidad/tratamiento |
|---|---|---|---|---|---|
| id_\allowbreak{}permiso | UUID | PK; generado una vez y preservado en reintentos | Sí | Personas y cumplimiento | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| id_\allowbreak{}transportista | UUID | Referencia a TRANSPORTISTA | Sí | Personas y cumplimiento | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| recurso | TEXT | Tipo e ID de camión/conductor/viaje autorizado | Sí | Personas y cumplimiento | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| destinatario | TEXT | Rol/cliente/sistema; referencia verificable | Sí | Personas y cumplimiento | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| finalidad | TEXT | Propósito específico; no autorización genérica | Sí | Personas y cumplimiento | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| datos_\allowbreak{}autorizados | JSONB | Catálogo granular de posición, documentos u otro dato; esquema versionado | Sí | Personas y cumplimiento | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| desde_\allowbreak{}utc | TIMESTAMPTZ | Inicio | Sí | Personas y cumplimiento | Operacional; personal si vincula jornada; cifrado/acceso según RT-11.10 cuando aplica |
| hasta_\allowbreak{}utc | TIMESTAMPTZ | Fin; permiso local siempre con expiración | Sí | Personas y cumplimiento | Operacional; personal si vincula jornada; cifrado/acceso según RT-11.10 cuando aplica |
| revocado_\allowbreak{}utc | TIMESTAMPTZ | Cese registrado | No | Personas y cumplimiento | Operacional; personal si vincula jornada; cifrado/acceso según RT-11.10 cuando aplica |
| version | INTEGER | Entero positivo; invalidación de caché | Sí | Personas y cumplimiento | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| id_\allowbreak{}respaldo | UUID | Referencia a DOCUMENTO_\allowbreak{}RESPALDO | Sí | Personas y cumplimiento | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| base_\allowbreak{}tratamiento_\allowbreak{}ref | TEXT | Registro jurídico separado; no se deduce del permiso comercial | Sí | Personas y cumplimiento | Operacional; cifrado/acceso según RT-11.10 cuando aplica |

Estos atributos concretan las referencias, campos obligatorios y controles de acceso de PERMISO_\allowbreak{}COMPARTIR.

### 5.5.18 ACCESO_\allowbreak{}DATO

Propietario de atributos: Seguridad y auditoría. La tabla define el contrato del registro.

La Tabla 5.24 detalla los atributos y controles del registro.

**Tabla 5.24.** Atributos y controles de ACCESO_\allowbreak{}DATO

| Atributo | Tipo | Dominio y regla | Obligatorio | Propietario | Sensibilidad/tratamiento |
|---|---|---|---|---|---|
| id_\allowbreak{}acceso | UUID | PK; generado una vez y preservado en reintentos | Sí | Seguridad y auditoría | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| actor | TEXT | Persona o sistema autenticado | Sí | Seguridad y auditoría | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| recurso | TEXT | Tipo, ID y campos mostrados/negados | Sí | Seguridad y auditoría | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| id_\allowbreak{}permiso | UUID | Referencia a PERMISO_\allowbreak{}COMPARTIR | Si aplica | Seguridad y auditoría | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| permiso_\allowbreak{}version | INTEGER | Versión evaluada | Si aplica | Seguridad y auditoría | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| resultado | TEXT | PERMITIDO / DENEGADO | Sí | Seguridad y auditoría | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| acceso_\allowbreak{}utc | TIMESTAMPTZ | Hora UTC | Sí | Seguridad y auditoría | Operacional; personal si vincula jornada; cifrado/acceso según RT-11.10 cuando aplica |
| correlacion | TEXT | Petición, dispositivo y canal | Sí | Seguridad y auditoría | Operacional; cifrado/acceso según RT-11.10 cuando aplica |

Estos atributos concretan las referencias, campos obligatorios y controles de acceso de ACCESO_\allowbreak{}DATO.

### 5.5.19 TELEMETRIA_\allowbreak{}EVENTO

Propietario de atributos: Telemetría y geocercas. La tabla define el contrato del registro.

La Tabla 5.25 detalla los atributos y controles del registro.

**Tabla 5.25.** Atributos y controles de TELEMETRIA_\allowbreak{}EVENTO

| Atributo | Tipo | Dominio y regla | Obligatorio | Propietario | Sensibilidad/tratamiento |
|---|---|---|---|---|---|
| id_\allowbreak{}evento | UUID | PK; generado una vez y preservado en reintentos | Sí | Telemetría y geocercas | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| id_\allowbreak{}dispositivo | UUID | Referencia a DISPOSITIVO | Sí | Telemetría y geocercas | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| id_\allowbreak{}viaje | UUID | Referencia a VIAJE | No | Telemetría y geocercas | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| id_\allowbreak{}conductor | UUID | Referencia a CONDUCTOR; sólo vínculo acreditado | No | Telemetría y geocercas | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| secuencia_\allowbreak{}origen | BIGINT | BIGINT; unicidad por equipo/flujo cuando fuente la ofrece | No | Telemetría y geocercas | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| evento_\allowbreak{}utc | TIMESTAMPTZ | Hora de fuente | No | Telemetría y geocercas | Operacional; personal si vincula jornada; cifrado/acceso según RT-11.10 cuando aplica |
| recibido_\allowbreak{}utc | TIMESTAMPTZ | Hora de recepción | Sí | Telemetría y geocercas | Operacional; personal si vincula jornada; cifrado/acceso según RT-11.10 cuando aplica |
| latitud | NUMERIC | −90..90; ambas coordenadas o ninguna | No | Telemetría y geocercas | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| longitud | NUMERIC | −180..180; ambas coordenadas o ninguna | No | Telemetría y geocercas | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| odometro_\allowbreak{}km | NUMERIC | Dato medido; NULL ausente | No | Telemetría y geocercas | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| parametros | JSONB | JSONB validado por esquema y mapa autorizado; esquema versionado | Sí | Telemetría y geocercas | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| hash_\allowbreak{}origen | TEXT | Integridad y procedencia | Sí | Telemetría y geocercas | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| autorizacion_\allowbreak{}version | INTEGER | Permiso aplicado; no transmitir fuera de su alcance | Si aplica | Telemetría y geocercas | Operacional; cifrado/acceso según RT-11.10 cuando aplica |

Estos atributos concretan las referencias, campos obligatorios y controles de acceso de TELEMETRIA_\allowbreak{}EVENTO.

### 5.5.20 ESTANCIA_\allowbreak{}CLIENTE

Propietario de atributos: Operación de fletes. La tabla define el contrato del registro.

La Tabla 5.26 detalla los atributos y controles del registro.

**Tabla 5.26.** Atributos y controles de ESTANCIA_\allowbreak{}CLIENTE

| Atributo | Tipo | Dominio y regla | Obligatorio | Propietario | Sensibilidad/tratamiento |
|---|---|---|---|---|---|
| id_\allowbreak{}estancia | UUID | PK; generado una vez y preservado en reintentos | Sí | Operación de fletes | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| id_\allowbreak{}viaje | UUID | Referencia a VIAJE | Sí | Operación de fletes | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| id_\allowbreak{}punto | UUID | Referencia a PUNTO_\allowbreak{}SERVICIO | Sí | Operación de fletes | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| llegada_\allowbreak{}utc | TIMESTAMPTZ | Evento automático geocerca | Sí | Operación de fletes | Operacional; personal si vincula jornada; cifrado/acceso según RT-11.10 cuando aplica |
| salida_\allowbreak{}utc | TIMESTAMPTZ | NULL mientras estancia abierta | No | Operación de fletes | Operacional; personal si vincula jornada; cifrado/acceso según RT-11.10 cuando aplica |
| id_\allowbreak{}evento_\allowbreak{}llegada | UUID | Referencia a TELEMETRIA_\allowbreak{}EVENTO | Sí | Operación de fletes | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| id_\allowbreak{}evento_\allowbreak{}salida | UUID | Referencia a TELEMETRIA_\allowbreak{}EVENTO | No | Operación de fletes | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| geocerca_\allowbreak{}version | TEXT | Polígono y regla usados | Sí | Operación de fletes | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| causa_\allowbreak{}demora | TEXT | Cliente / frontera / otra; no cobro automático por toda demora | No | Operación de fletes | Operacional; cifrado/acceso según RT-11.10 cuando aplica |

Estos atributos concretan las referencias, campos obligatorios y controles de acceso de ESTANCIA_\allowbreak{}CLIENTE.

### 5.5.21 DOCUMENTO_\allowbreak{}TRANSPORTE

Propietario de atributos: Operación de fletes; emisor fiscal externo contable. La tabla define el contrato del registro.

La Tabla 5.27 detalla los atributos y controles del registro.

**Tabla 5.27.** Atributos y controles de DOCUMENTO_\allowbreak{}TRANSPORTE

| Atributo | Tipo | Dominio y regla | Obligatorio | Propietario | Sensibilidad/tratamiento |
|---|---|---|---|---|---|
| id_\allowbreak{}documento_\allowbreak{}transporte | UUID | PK; generado una vez y preservado en reintentos | Sí | Operación de fletes; emisor fiscal externo contable | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| id_\allowbreak{}viaje | UUID | Referencia a VIAJE | Sí | Operación de fletes; emisor fiscal externo contable | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| id_\allowbreak{}original | UUID | Referencia a DOCUMENTO_\allowbreak{}RESPALDO | Sí | Operación de fletes; emisor fiscal externo contable | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| folio | TEXT | Asignado exclusivamente por contable; único por emisor/tipo | Sí | Operación de fletes; emisor fiscal externo contable | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| emisor | TEXT | Identidad del emisor | Sí | Operación de fletes; emisor fiscal externo contable | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| estado | TEXT | SOLICITADO / EMITIDO / ENTREGADO / RECHAZADO / ANULADO | Sí | Operación de fletes; emisor fiscal externo contable | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| representacion_\allowbreak{}uri | TEXT | Copia portable conforme del mismo contenido | Al habilitar salida | Operación de fletes; emisor fiscal externo contable | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| emitido_\allowbreak{}utc | TIMESTAMPTZ | Hora de emisión del contable | Al emitir | Operación de fletes; emisor fiscal externo contable | Operacional; personal si vincula jornada; cifrado/acceso según RT-11.10 cuando aplica |
| acuse_\allowbreak{}cabina_\allowbreak{}utc | TIMESTAMPTZ | Entrega completa verificada | Antes de salida | Operación de fletes; emisor fiscal externo contable | Operacional; personal si vincula jornada; cifrado/acceso según RT-11.10 cuando aplica |
| clave_\allowbreak{}idempotencia | TEXT | Solicitud fiscal correlacionada y duradera | Sí | Operación de fletes; emisor fiscal externo contable | Operacional; cifrado/acceso según RT-11.10 cuando aplica |

Estos atributos concretan las referencias, campos obligatorios y controles de acceso de DOCUMENTO_\allowbreak{}TRANSPORTE.

### 5.5.22 CONFORMIDAD_\allowbreak{}ENTREGA

Propietario de atributos: Operación de fletes. La tabla define el contrato del registro.

La Tabla 5.28 detalla los atributos y controles del registro.

**Tabla 5.28.** Atributos y controles de CONFORMIDAD_\allowbreak{}ENTREGA

| Atributo | Tipo | Dominio y regla | Obligatorio | Propietario | Sensibilidad/tratamiento |
|---|---|---|---|---|---|
| id_\allowbreak{}conformidad | UUID | PK; generado una vez y preservado en reintentos | Sí | Operación de fletes | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| id_\allowbreak{}viaje | UUID | Referencia a VIAJE | Sí | Operación de fletes | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| destinatario | TEXT | Persona identificada que recibe | Sí | Operación de fletes | Personal; acceso restringido; cifrado/acceso según RT-11.10 cuando aplica |
| resultado | TEXT | CONFORME / DISCREPANCIA / RECHAZADA | Sí | Operación de fletes | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| observacion | TEXT | Descripción concreta | No | Operación de fletes | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| id_\allowbreak{}original_\allowbreak{}firmado | UUID | Referencia a DOCUMENTO_\allowbreak{}RESPALDO | Sí | Operación de fletes | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| evento_\allowbreak{}utc | TIMESTAMPTZ | Firma/recepción | Sí | Operación de fletes | Operacional; personal si vincula jornada; cifrado/acceso según RT-11.10 cuando aplica |
| firma_\allowbreak{}modalidad | TEXT | Modalidad admitida para el caso; comprobación de identidad e integridad | Sí | Operación de fletes | Operacional; cifrado/acceso según RT-11.10 cuando aplica |

Estos atributos concretan las referencias, campos obligatorios y controles de acceso de CONFORMIDAD_\allowbreak{}ENTREGA.

### 5.5.23 CHECKLIST_\allowbreak{}CARGA_\allowbreak{}PELIGROSA

Propietario de atributos: Operación de fletes. La tabla define el contrato del registro.

La Tabla 5.29 detalla los atributos y controles del registro.

**Tabla 5.29.** Atributos y controles de CHECKLIST_\allowbreak{}CARGA_\allowbreak{}PELIGROSA

| Atributo | Tipo | Dominio y regla | Obligatorio | Propietario | Sensibilidad/tratamiento |
|---|---|---|---|---|---|
| id_\allowbreak{}checklist | UUID | PK; generado una vez y preservado en reintentos | Sí | Operación de fletes | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| id_\allowbreak{}viaje | UUID | Referencia a VIAJE | Sí | Operación de fletes | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| version | INTEGER | Versión de lista y regla | Sí | Operación de fletes | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| resultado | TEXT | APROBADA / RECHAZADA | Sí | Operación de fletes | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| items | JSONB | JSONB validado; carga y documentación cotejadas; esquema versionado | Sí | Operación de fletes | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| id_\allowbreak{}original_\allowbreak{}firmado | UUID | Referencia a DOCUMENTO_\allowbreak{}RESPALDO | Sí | Operación de fletes | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| verificado_\allowbreak{}utc | TIMESTAMPTZ | Antes del movimiento | Sí | Operación de fletes | Operacional; personal si vincula jornada; cifrado/acceso según RT-11.10 cuando aplica |

Estos atributos concretan las referencias, campos obligatorios y controles de acceso de CHECKLIST_\allowbreak{}CARGA_\allowbreak{}PELIGROSA.

### 5.5.24 TARIFA_\allowbreak{}CONTRATO

Propietario de atributos: Liquidación y costeo; terceros desde M16 y clientes desde M21. La tabla define el contrato del registro.

La Tabla 5.30 detalla los atributos y controles del registro.

**Tabla 5.30.** Atributos y controles de TARIFA_\allowbreak{}CONTRATO

| Atributo | Tipo | Dominio y regla | Obligatorio | Propietario | Sensibilidad/tratamiento |
|---|---|---|---|---|---|
| id_\allowbreak{}tarifa | UUID | PK; generado una vez y preservado en reintentos | Sí | Liquidación y costeo | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| id_\allowbreak{}cliente | UUID | Referencia a CLIENTE; exactamente una contraparte | Excluyente | Liquidación y costeo | Operacional; acceso restringido |
| id_\allowbreak{}transportista | UUID | Referencia a TRANSPORTISTA; exactamente una contraparte | Excluyente | Liquidación y costeo | Operacional; acceso restringido |
| ruta_\allowbreak{}servicio | TEXT | Alcance contractual | Sí | Liquidación y costeo | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| importe | NUMERIC | Moneda y regla de redondeo conservadas | Sí | Liquidación y costeo | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| moneda | TEXT | Catálogo ISO de moneda | Sí | Liquidación y costeo | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| desde_\allowbreak{}utc | TIMESTAMPTZ | Inicio de vigencia | Sí | Liquidación y costeo | Operacional; personal si vincula jornada; cifrado/acceso según RT-11.10 cuando aplica |
| hasta_\allowbreak{}utc | TIMESTAMPTZ | Fin; NULL si no fijado | No | Liquidación y costeo | Operacional; personal si vincula jornada; cifrado/acceso según RT-11.10 cuando aplica |
| version | INTEGER | No sobrescribir tarifa aplicada a un viaje | Sí | Liquidación y costeo | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| id_\allowbreak{}respaldo | UUID | Referencia a DOCUMENTO_\allowbreak{}RESPALDO | Sí | Liquidación y costeo | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |

Estos atributos concretan las referencias, campos obligatorios y controles de acceso de TARIFA_\allowbreak{}CONTRATO.

### 5.5.25 COSTO_\allowbreak{}VERSION

Propietario de atributos: Liquidación y costeo. La tabla define el contrato del registro.

La Tabla 5.31 detalla los atributos y controles del registro.

**Tabla 5.31.** Atributos y controles de COSTO_\allowbreak{}VERSION

| Atributo | Tipo | Dominio y regla | Obligatorio | Propietario | Sensibilidad/tratamiento |
|---|---|---|---|---|---|
| id_\allowbreak{}costo | UUID | PK; generado una vez y preservado en reintentos | Sí | Liquidación y costeo | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| id_\allowbreak{}viaje | UUID | Referencia a VIAJE | Sí | Liquidación y costeo | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| version | INTEGER | INTEGER >0; único por viaje | Sí | Liquidación y costeo | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| estado | TEXT | PRELIMINAR / ACTUALIZADO / DEFINITIVO | Sí | Liquidación y costeo | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| costo_\allowbreak{}total | NUMERIC | Importe con moneda y redondeo | Sí | Liquidación y costeo | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| distancia_\allowbreak{}km | NUMERIC | Denominador y origen medido/estimado; no dividir por cero | Sí | Liquidación y costeo | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| componentes | JSONB | Datos medidos, estimados y pendientes identificados; esquema versionado | Sí | Liquidación y costeo | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| fuentes | JSONB | IDs de lotes/telemetría/tarifa y versiones usadas; esquema versionado | Sí | Liquidación y costeo | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| calculado_\allowbreak{}utc | TIMESTAMPTZ | v1 no más de 24 h tras cierre | Sí | Liquidación y costeo | Operacional; personal si vincula jornada; cifrado/acceso según RT-11.10 cuando aplica |
| regla_\allowbreak{}version | TEXT | Fórmula y supuestos reproducibles | Sí | Liquidación y costeo | Operacional; cifrado/acceso según RT-11.10 cuando aplica |

Estos atributos concretan las referencias, campos obligatorios y controles de acceso de COSTO_\allowbreak{}VERSION.

### 5.5.26 LIQUIDACION

Propietario de atributos: Liquidación y costeo. La tabla define el contrato del registro.

La Tabla 5.32 detalla los atributos y controles del registro.

**Tabla 5.32.** Atributos y controles de LIQUIDACION

| Atributo | Tipo | Dominio y regla | Obligatorio | Propietario | Sensibilidad/tratamiento |
|---|---|---|---|---|---|
| id_\allowbreak{}liquidacion | UUID | PK; generado una vez y preservado en reintentos | Sí | Liquidación y costeo | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| id_\allowbreak{}transportista | UUID | Referencia a TRANSPORTISTA | Sí | Liquidación y costeo | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| periodo | TEXT | Mes y versión; único por transportista/periodo/versión | Sí | Liquidación y costeo | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| estado | TEXT | BORRADOR / EN_\allowbreak{}REVISION / APROBADA / REGISTRADA | Sí | Liquidación y costeo | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| importe_\allowbreak{}total | NUMERIC | Importe conciliado; moneda declarada | Sí | Liquidación y costeo | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| id_\allowbreak{}aceptacion_\allowbreak{}firmada | UUID | Referencia a DOCUMENTO_\allowbreak{}RESPALDO | Al aprobar | Liquidación y costeo | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| operacion_\allowbreak{}contable_\allowbreak{}id | TEXT | Acuse externo; NULL mientras pendiente | No | Liquidación y costeo | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| clave_\allowbreak{}idempotencia | TEXT | Evita doble registro en contable | Sí | Liquidación y costeo | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| aprobado_\allowbreak{}utc | TIMESTAMPTZ | Aceptación efectiva | No | Liquidación y costeo | Operacional; personal si vincula jornada; cifrado/acceso según RT-11.10 cuando aplica |

Estos atributos concretan las referencias, campos obligatorios y controles de acceso de LIQUIDACION.

### 5.5.27 LIQUIDACION_\allowbreak{}DETALLE

Propietario de atributos: Liquidación y costeo. La tabla define el contrato del registro.

La Tabla 5.33 detalla los atributos y controles del registro.

**Tabla 5.33.** Atributos y controles de LIQUIDACION_\allowbreak{}DETALLE

| Atributo | Tipo | Dominio y regla | Obligatorio | Propietario | Sensibilidad/tratamiento |
|---|---|---|---|---|---|
| id_\allowbreak{}liquidacion | UUID | Referencia a LIQUIDACION; parte de PK | Sí | Liquidación y costeo | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| id_\allowbreak{}viaje | UUID | Referencia a VIAJE; parte de PK | Sí | Liquidación y costeo | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| id_\allowbreak{}costo | UUID | Referencia a COSTO_\allowbreak{}VERSION usado | Sí | Liquidación y costeo | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| id_\allowbreak{}tarifa | UUID | Referencia a TARIFA_\allowbreak{}CONTRATO | Sí | Liquidación y costeo | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| importe | NUMERIC | Monto y conceptos conciliados | Sí | Liquidación y costeo | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| discrepancia | TEXT | Observación y resolución; no excluir sin historia | No | Liquidación y costeo | Operacional; cifrado/acceso según RT-11.10 cuando aplica |

Estos atributos concretan las referencias, campos obligatorios y controles de acceso de LIQUIDACION_\allowbreak{}DETALLE.

### 5.5.28 LOTE_\allowbreak{}COSTO

Propietario de atributos: Liquidación y costeo. La tabla define el contrato del registro.

La Tabla 5.34 detalla los atributos y controles del registro.

**Tabla 5.34.** Atributos y controles de LOTE_\allowbreak{}COSTO

| Atributo | Tipo | Dominio y regla | Obligatorio | Propietario | Sensibilidad/tratamiento |
|---|---|---|---|---|---|
| id_\allowbreak{}lote | UUID | PK; generado una vez y preservado en reintentos | Sí | Liquidación y costeo | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| fuente | TEXT | COMBUSTIBLE / PEAJE / OTRA | Sí | Liquidación y costeo | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| clave_\allowbreak{}fuente | TEXT | ID único por proveedor/lote | Sí | Liquidación y costeo | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| id_\allowbreak{}original | UUID | Referencia a DOCUMENTO_\allowbreak{}RESPALDO | Sí | Liquidación y costeo | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| recibido_\allowbreak{}utc | TIMESTAMPTZ | Recepción | Sí | Liquidación y costeo | Operacional; personal si vincula jornada; cifrado/acceso según RT-11.10 cuando aplica |
| totales | TEXT | Cantidad e importes originales y conciliados | Sí | Liquidación y costeo | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| errores | TEXT | Informe por registro; carga parcial trazada | Sí | Liquidación y costeo | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| estado | TEXT | RECIBIDO / CONCILIADO / PARCIAL / RECHAZADO | Sí | Liquidación y costeo | Operacional; cifrado/acceso según RT-11.10 cuando aplica |

Estos atributos concretan las referencias, campos obligatorios y controles de acceso de LOTE_\allowbreak{}COSTO.

### 5.5.29 INTERVENCION_\allowbreak{}TALLER

Propietario de atributos: Flota y activos. La tabla define el contrato del registro.

La Tabla 5.35 detalla los atributos y controles del registro.

**Tabla 5.35.** Atributos y controles de INTERVENCION_\allowbreak{}TALLER

| Atributo | Tipo | Dominio y regla | Obligatorio | Propietario | Sensibilidad/tratamiento |
|---|---|---|---|---|---|
| id_\allowbreak{}intervencion | UUID | PK; generado una vez y preservado en reintentos | Sí | Flota y activos | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| id_\allowbreak{}tracto | UUID | Referencia a TRACTOCAMION | Excluyente | Flota y activos | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| id_\allowbreak{}semirremolque | UUID | Referencia a SEMIRREMOLQUE | Excluyente | Flota y activos | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| taller | TEXT | Propio/externo y responsable identificado | Sí | Flota y activos | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| tipo | TEXT | Preventiva / correctiva / neumático; catálogo | Sí | Flota y activos | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| odometro_\allowbreak{}km | NUMERIC | Medido cuando disponible | No | Flota y activos | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| estado | TEXT | PROGRAMADA / EJECUTADA / VALIDADA | Sí | Flota y activos | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| id_\allowbreak{}respaldo | UUID | Referencia a DOCUMENTO_\allowbreak{}RESPALDO | Al validar | Flota y activos | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| ejecutado_\allowbreak{}utc | TIMESTAMPTZ | Fecha efectiva | No | Flota y activos | Operacional; personal si vincula jornada; cifrado/acceso según RT-11.10 cuando aplica |

Estos atributos concretan las referencias, campos obligatorios y controles de acceso de INTERVENCION_\allowbreak{}TALLER.

### 5.5.30 POSICION_\allowbreak{}NEUMATICO

Propietario de atributos: Flota y activos. La tabla define el contrato del registro.

La Tabla 5.36 detalla los atributos y controles del registro.

**Tabla 5.36.** Atributos y controles de POSICION_\allowbreak{}NEUMATICO

| Atributo | Tipo | Dominio y regla | Obligatorio | Propietario | Sensibilidad/tratamiento |
|---|---|---|---|---|---|
| id_\allowbreak{}posicion | UUID | PK; generado una vez y preservado en reintentos | Sí | Flota y activos | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| id_\allowbreak{}tracto | UUID | Referencia a TRACTOCAMION; sujeto exclusivo | Excluyente | Flota y activos | Operacional; acceso restringido |
| id_\allowbreak{}semirremolque | UUID | Referencia a SEMIRREMOLQUE; sujeto exclusivo | Excluyente | Flota y activos | Operacional; acceso restringido |
| ubicacion | TEXT | Eje/lado; catálogo por vehículo | Sí | Flota y activos | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| neumatico_\allowbreak{}id | TEXT | Identidad trazable | Sí | Flota y activos | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| km_\allowbreak{}acumulado | NUMERIC | Derivado de odómetro y montaje; no inventar medición | No | Flota y activos | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| montado_\allowbreak{}utc | TIMESTAMPTZ | Inicio | Sí | Flota y activos | Operacional; personal si vincula jornada; cifrado/acceso según RT-11.10 cuando aplica |
| retirado_\allowbreak{}utc | TIMESTAMPTZ | Fin | No | Flota y activos | Operacional; personal si vincula jornada; cifrado/acceso según RT-11.10 cuando aplica |
| id_\allowbreak{}intervencion | UUID | Referencia a INTERVENCION_\allowbreak{}TALLER | Sí | Flota y activos | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |

Estos atributos concretan las referencias, campos obligatorios y controles de acceso de POSICION_\allowbreak{}NEUMATICO.

### 5.5.31 SINIESTRO

Propietario de atributos: Operación de fletes. La tabla define el contrato del registro.

La Tabla 5.37 detalla los atributos y controles del registro.

**Tabla 5.37.** Atributos y controles de SINIESTRO

| Atributo | Tipo | Dominio y regla | Obligatorio | Propietario | Sensibilidad/tratamiento |
|---|---|---|---|---|---|
| id_\allowbreak{}siniestro | UUID | PK; generado una vez y preservado en reintentos | Sí | Operación de fletes | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| id_\allowbreak{}viaje | UUID | Referencia a VIAJE | No | Operación de fletes | Operacional; personal si vincula persona; cifrado/acceso según RT-11.10 cuando aplica |
| equipo_\allowbreak{}persona | JSONB | Referencias de activos/personas afectadas; esquema versionado | Sí | Operación de fletes | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| evento_\allowbreak{}utc | TIMESTAMPTZ | Hora conocida; precisión/origen declarados | Sí | Operación de fletes | Operacional; personal si vincula jornada; cifrado/acceso según RT-11.10 cuando aplica |
| tipo | TEXT | Catálogo de incidentes/siniestros | Sí | Operación de fletes | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| expediente | JSONB | Referencias a originales, peritajes y resoluciones; esquema versionado | Sí | Operación de fletes | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| estado | TEXT | ABIERTO / EN_\allowbreak{}TRAMITE / CERRADO | Sí | Operación de fletes | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| retencion_\allowbreak{}litigio | BOOLEAN | BOOLEAN; conserva hasta resolución aplicable | Sí | Operación de fletes | Operacional; cifrado/acceso según RT-11.10 cuando aplica |

Estos atributos concretan las referencias, campos obligatorios y controles de acceso de SINIESTRO.

### 5.5.32 AUDITORIA_\allowbreak{}EVENTO

Propietario de atributos: Seguridad y auditoría. La tabla define el contrato del registro.

La Tabla 5.38 detalla los atributos y controles del registro.

**Tabla 5.38.** Atributos y controles de AUDITORIA_\allowbreak{}EVENTO

| Atributo | Tipo | Dominio y regla | Obligatorio | Propietario | Sensibilidad/tratamiento |
|---|---|---|---|---|---|
| id_\allowbreak{}auditoria | UUID | PK; generado una vez y preservado en reintentos | Sí | Seguridad y auditoría | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| actor_\allowbreak{}dispositivo | TEXT | Identidades y origen | Sí | Seguridad y auditoría | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| entidad_\allowbreak{}id | TEXT | Tipo e ID del registro consultado/modificado | Sí | Seguridad y auditoría | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| operacion | TEXT | CREAR / MODIFICAR / CONSULTAR / RECTIFICAR / ELIMINAR_\allowbreak{}AUTORIZADO | Sí | Seguridad y auditoría | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| valores | JSONB | Antes/después o campos mostrados; cifrado si procede; esquema versionado | Sí | Seguridad y auditoría | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| evento_\allowbreak{}utc | TIMESTAMPTZ | Fecha y zona conservadas | Sí | Seguridad y auditoría | Operacional; personal si vincula jornada; cifrado/acceso según RT-11.10 cuando aplica |
| correlacion | TEXT | Operación end to end | Sí | Seguridad y auditoría | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| cadena_\allowbreak{}id | UUID | Identificador de cadena | Sí | Seguridad y auditoría | Operacional; acceso restringido |
| secuencia | BIGINT | >0; UNIQUE(cadena_\allowbreak{}id,secuencia) | Sí | Seguridad y auditoría | Operacional; acceso restringido |
| hash_\allowbreak{}actual | TEXT | 64 hex; registro canónico | Sí | Seguridad y auditoría | Operacional; acceso restringido |
| hash_\allowbreak{}previo | TEXT | 64 hex; NULL sólo inicio de cadena | Condicional | Seguridad y auditoría | Operacional; acceso restringido |
| manifiesto_\allowbreak{}worm | TEXT | Anclaje sellado e ID de segmento | Sí | Seguridad y auditoría | Operacional; cifrado/acceso según RT-11.10 cuando aplica |

Estos atributos concretan las referencias, campos obligatorios y controles de acceso de AUDITORIA_\allowbreak{}EVENTO.

### 5.5.33 OUTBOX_\allowbreak{}EVENTO

Propietario de atributos: Contexto productor del evento. La tabla define el contrato del registro.

La Tabla 5.39 detalla los atributos y controles del registro.

**Tabla 5.39.** Atributos y controles de OUTBOX_\allowbreak{}EVENTO

| Atributo | Tipo | Dominio y regla | Obligatorio | Propietario | Sensibilidad/tratamiento |
|---|---|---|---|---|---|
| id_\allowbreak{}evento | UUID | PK; generado una vez y preservado en reintentos | Sí | Contexto productor del evento | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| agregado_\allowbreak{}id | TEXT | ID, tipo y versión del agregado | Sí | Contexto productor del evento | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| tipo_\allowbreak{}esquema | TEXT | Contrato de evento y versión | Sí | Contexto productor del evento | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| payload | JSONB | JSON validado; datos mínimos autorizados; esquema versionado | Sí | Contexto productor del evento | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| creado_\allowbreak{}utc | TIMESTAMPTZ | Mismo commit que cambio de negocio | Sí | Contexto productor del evento | Operacional; personal si vincula jornada; cifrado/acceso según RT-11.10 cuando aplica |
| clave_\allowbreak{}particion | TEXT | Agregado/equipo para orden | Sí | Contexto productor del evento | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| estado | TEXT | PENDIENTE / PUBLICADO; acuse no equivale a consumo final | Sí | Contexto productor del evento | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| intentos | INTEGER | ≥0 | Sí | Contexto productor del evento | Operacional; cifrado/acceso según RT-11.10 cuando aplica |
| proximo_\allowbreak{}intento_\allowbreak{}utc | TIMESTAMPTZ | Fecha de reintento; NULL si publicado | No | Contexto productor del evento | Operacional; acceso restringido |
| correlacion | TEXT | ID común de solicitud y efectos | Sí | Contexto productor del evento | Operacional; cifrado/acceso según RT-11.10 cuando aplica |

Estos atributos concretan las referencias, campos obligatorios y controles de acceso de OUTBOX_\allowbreak{}EVENTO.

### 5.5.34 Restricciones transversales y custodia

VIGENCIA_\allowbreak{}HABILITACION, INTERVENCION_\allowbreak{}TALLER y POSICION_\allowbreak{}NEUMATICO usan FK explícitas y un CHECK de sujeto exclusivo; no una FK polimórfica ficticia. VIAJE puede existir programado sin recursos. ASIGNACION confirmada exige recursos válidos, evaluación y rangos activos no superpuestos; una reserva rechazada no termina el viaje. DOCUMENTO_\allowbreak{}TRANSPORTE requiere original y representación conforme antes de salir; el contable es el único emisor.

EVIDENCIA_\allowbreak{}JORNADA válida exige código homologado, nivel 0–5 y controles de integridad; 0 sólo REG_\allowbreak{}COND. Las fuentes desconocidas/inválidas tienen nivel NULL y motivo conservado. SIN_\allowbreak{}EVIDENCIA se registra en la evaluación, sin fabricar un artefacto. La evaluación puede referenciar múltiples fuentes mediante EVALUACION_\allowbreak{}EVIDENCIA; reposo nivel 4 y atestación nivel 5 no se colapsan en una fuente. Ninguna causa legal admite EXCEPCION_\allowbreak{}RN04.

El sello encadenado incluye ID de cadena, secuencia, bytes canónicos, hash previo y hash actual; sólo un registro inicial tiene hash previo NULL. Rectificación genera registro nuevo. Originales, manifiestos y claves de firma se conservan/administran separados; el hash no es firma. Las cuentas aplicativas no sobrescriben evidencia; almacenamiento WORM bloqueado y verificación independiente sostienen el control contra administradores.

Se indexan FK locales y claves de consulta. RUT cifrado utiliza índice ciego de deduplicación con clave separada; no se presume búsqueda SQL de texto sobre AES-GCM. VIAJE se mantiene sin partición inicial. Particionar una tabla PostgreSQL exige compatibilizar PK/UNIQUE con su clave de partición y revisar referencias. Las políticas de supresión contemplan retención, litigio, claves compartidas y todas las copias.

### 5.5.35 Supuestos de capacidad y migración

Caso, numeral 14.2, p. 30 pide estimación; la Tabla 5.40 diferencia tasas del Caso, tamaños supuestos y conteos históricos no entregados.

La Tabla 5.40 detalla los atributos y controles del registro.

**Tabla 5.40.** Presupuesto lógico inicial de datos, sin índices ni réplicas

| Dominio | Base / supuesto | Resultado de diseño |
|---|---|---|
| Viajes | 96.000/año $\times$2 KiB/registro compuesto | $≈197 MB/año; 5 años ≈$983 MB, sin documentos |
| Evaluaciones | 3 intentos/viaje $\times96.000 \times$1 KiB | ≈295 MB/año; intentos reales por medir |
| Documentos de transporte | 128.000/año $\times$20 KiB por XML/representación | $≈2,62 GB/año; 6 años ≈$15,73 GB. No acredita tamaño para envío SBD |
| Evidencia de jornada | 454 conductores $\times365 \times15 eventos/día \times512 bytes | ≈1,27 GB/año; 5 años ≈$6,36 GB, sin originales de tacógrafo/atestaciones |
| Vigencias vivas | $≈6.000 \times$100 KiB de respaldo medio | ≈614 MB por lote; tamaño y versiones por medir |
| Telemetría de posición | 119,82 millones/año $\times$64 bytes | ≈7,67 GB/año, escenario completo de S4.1.20 |
| Viajes históricos a migrar | 96.000/año $\times$5 sólo como extrapolación | ≈480.000 registros; contar el histórico real antes de dimensionar corte |
| Liquidaciones históricas | 148/mes $\times12 \times$6 sólo como extrapolación | ≈10.656 registros; verificar períodos, versiones y transportistas reales |
| Siniestros y maestros | Totalidad de la fuente según RT-05.15 | No hay conteo/bytes entregados; inventariar todos y preservar pendientes |

La Tabla 5.40 no es tamaño físico ni cifra medida. Un factor provisional 3$\times$ sobre registros cubre índices/estructura de manera aproximada, pero WAL, originales grandes, fotos, copias WORM, respaldos y réplicas se dimensionan explícitamente por separado. No se multiplica por un factor sin indicar qué incluye. El volumen de jornada se registra por eventos semánticos, sin convertir cada ping de GPS en prueba de descanso. Se ensayan extracción, transformación, carga y conciliación con tasa medida; volumen/tasa más delta final determina la ventana, conciliada con S7.
