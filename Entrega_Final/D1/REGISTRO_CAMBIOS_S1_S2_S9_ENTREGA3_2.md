# REGISTRO DE CAMBIOS Y JUSTIFICACIÓN TÉCNICO-NORMATIVA: S1, S2 Y S9
## audIT Soluciones Tecnológicas SpA · Licitación Pública TFEP-01/2026 (Caso 10: Transportes Curimón S.A.)

**Fecha de cierre:** 24 de noviembre de 2026  
**Línea base de verdad (inmutable):** Entrega 3 (v3.2) — `INFORME3_AUDIT_PLANILLA_3.2_20261115.xlsx`, documentos económicos (`economico/`), Bitácora A-6 v3.2 y Bases Oficiales (`FEP01.26`, `FEP02.26`, `FEP03.10.26`).  
**Documento de auditoría origen:** `INFORME_CONSISTENCIA_ENTREGA3_VS_S1_S2_S9.md` (dos vueltas de auditoría independiente cero-confianza + validación automatizada con `verificar.py`).  
**Resumen cuantitativo:** **17 archivos fuente modificados** (`1` configuración + `7` `.tex` + `9` `.md`), **43 hallazgos resueltos** (`0` infracciones al Art. 50.2) y **8 PDF finales compilados** sin errores.

---

## 1. Configuración Global de Instancia

### `recursos/Formato-Oferta-audIT/configuracion/instancia.tex`
| Qué se cambió | Por qué se cambió |
| :--- | :--- |
| `\Instancia{informe3}` → `\Instancia{final}`, `\Version{2.0}` → `\Version{3.0}`, `\FechaEntrega{2026-11-13}` → `\FechaEntrega{2026-11-25}`, `\ModoFolio{subdocumento}` → `\ModoFolio{continuo}`. | Alinear la compilación con la entrega final de sobres cerrados fijada en `FEP01.26` (Formulario T-20, 25-11-2026) y habilitar la compilación de subdocumentos técnicos (`compilar.py subdocs`, que bajo `informe3` solo compila económicos). |

---

## 2. Subdocumento 1 — Empresa, Experiencia, Formulario T-6 y Anexo 1.A (`subdocumentos/01-empresa/`)

### `contenido.tex`
| Área / Sección | Qué se cambió | Por qué se cambió |
| :--- | :--- | :--- |
| **Tabla 1.1 (`1-dedicacion-roles`) — Arquitecto de Solución** | Dedicación en operación cambiada de `25% FTE` a `Cierre M21--M24 (45 HH totales; a demanda en M25--M56)`. | En la Planilla 3.2 (`Contrato de soporte` R11; `Soporte por perfil`), `Arquitectura cierre / EDT6.5` tiene **0 h fijas/variables** en régimen y solo **45 HH** en M21–M24 (12+11+11+11 h). Comprometer `25% FTE` (1.440 HH) generaba una brecha no costeada de 1.395 HH en un rol habilitante del Art. 34.1. |
| **Tabla 1.1 (`1-dedicacion-roles`) — Líder de Calidad y Pruebas y Líder de Datos** | `Líder de Calidad y Pruebas` actualizado de `25% FTE` a `50% FTE fijo (más bolsa variable/cierre)`, y misma precisión aplicada a `Líder de Datos`. | En la Planilla 3.2 (`Contrato de soporte` R10, `QA / EDT13.4`), la cobertura fija mínima de QA en M21–M56 es **80 h/mes = 50 % FTE** (más bolsa variable escalonada y cierre M21–M24), idéntica a `Datos / EDT13.4`. |
| **Tabla 1.1 — Encabezados y texto introductorio** | Reemplazado `las dos etapas del contrato` / `Fase 1 (M1--M20)` / `Fase 2 (M21--M56)` por `las dos fases del contrato` / `Implementación (M1--M20)` / `Operación (M21--M56)`, aclarando aceptación final H12 en M21. | Evitar confusión con **Etapa 1** (M1–M16) y **Etapa 2** (M13–M21) dentro de la Fase de Implementación (`FEP01.26` Art. 17; `Hitos E25` R13). |
| **Dotación y pico de carga (§1.2)** | Precisado que `37,0 FTE` es la carga de referencia en M13–M17, sumando los refuerzos puntuales de puesta en producción en **H6 (M13) y H7 (M16) hasta 38,50 FTE**, y el pico real contratado de **39,23 FTE en M7** (M7–M9). | En la Planilla 3.2 (`Dotación por perfil` y `Parámetros corrección` B85–B86), las horas internas contratadas alcanzan su máximo en **M7 (39,23 FTE)** y suman +160 h SRE / +80 h Software en H6 y H7. |
| **Soporte de campo y Red Regional Ruta 5 (§1.1 y §1.2)** | Reemplazado `cuadrilla móvil` por `atención en terreno por despacho programado o visita correctiva` y `cuadrillas de turno 24/7` por `servicio de campo externalizado por visita y rondas preventivas regionales en los cinco terminales (coordinado desde el 0,5 FTE interno en M21--M56, tras transición a modalidad externa en M19)`. | En E3.2 (`Parámetros corrección` B59, B78–B83; `Contrato de soporte` R7), el técnico interno sale en M19 y en operación se presupuestan **0,5 FTE interno (80 h/mes)** + servicio externo por visita (3 visitas correctivas/mes + 2 rondas regionales/mes + reposiciones), no cuadrillas permanentes 24/7. |
| **Matriz de escalamiento — Nivel 1 (§1.3)** | Reemplazado `Analistas de Soporte Técnico (PMO y Soporte)` por `Agentes dedicados de Mesa de Ayuda N1 24×7 (6 agentes regulares más 1 FTE de suplencias y picos en fase de operación, bajo supervisión de Gestión de Servicio y PMO)`. | Contradecía tanto la dotación de 3 analistas PMO de la misma sección como E3.2 (`Contrato de soporte` R2, R13; `Mesa de ayuda` R3–R4), que presupuesta **7 FTE internos dedicados** (1.120 h/mes) para N1 24×7. |
| **Credenciales financieras (§1.4)** | Corregida la cita `\art{39}{25}, numeral 4` → `\art{39.2}{26}`; ajustada la redacción de capital de trabajo eliminando la afirmación de *"más de seis meses de operación sin cobranzas inmediatas"* y remitiendo la proyección de caja al Sobre N.º 3. | En `FEP01.26` p. 26, los antecedentes financieros corresponden al **numeral 2 (`Art. 39.2`)**, no al numeral 4 (antecedentes técnicos). Además, E3.2 (`Resumen Ejecutivo` R9–R14) financia el contrato 80 % deuda / 20 % socios con facilidad contingente ante atraso en H5. |
| **Alianzas tecnológicas (§1.6)** | Precisadas las regiones `Azure Chile Central y Brazil South (canal CSP)`; eliminada la referencia a fabricantes de semiconductores (`NXP Semiconductors`, `STMicroelectronics`, `Quectel`); incorporados los proveedores clave de E3.2 (**Dell**, **Fortinet**, **iWave**, **Teltonika** + EYE Sensor BTSMP1, **Technoton**, **Ground Control / Iridium**, **GitLab** y **SonarSource**), aclarando que el hardware de campo/red de T-11 es adquirido por el mandante. | Alineación 1:1 con `economico/costos-venta/contenido.tex` (`tabla eco-proveedores`), `oferta-economica/contenido.tex` L69 y `Detalle proveedores D4`. audIT no fabrica placas con chips NXP/Quectel. |
| **Paginación de Tabla 1.2 (`1-proyectos`)** | Agregado `\Needspace{55mm}` antes de `\begin{tabla}...{1-proyectos}`. | Mitigar el aviso de `verificar.py` (Regla 19) sobre el corte de página del pie de la Tabla 1.2. |

### `anexo-1a.tex`
| Qué se cambió | Por qué se cambió |
| :--- | :--- |
| Fecha de firma actualizada de `03 de octubre de 2026` a `25 de noviembre de 2026`. | La fecha del 03-10-2026 correspondía al Informe 2; la fecha oficial de entrega de la Oferta Final según `FEP01.26` (Formulario T-20) es **25 de noviembre de 2026**. |

### `contenido.md`, `anexo-1a.md`, `anexos.md` y `formularios/T-6.md`
| Qué se cambió | Por qué se cambió |
| :--- | :--- |
| Regeneración completa desde los `.tex` corregidos usando el `.aux` compilado; reescritura limpia en Markdown nativo de `T-6.md`. | Estaban congelados al 2 de noviembre con encabezado obsoleto `Informe Preparatorio 2`, tabla histórica de observaciones del Informe 1, omisión del párrafo de cobertura de flota (`contenido.md`), macros LaTeX crudas (`\proyectoTSeis`, `\begin{minipage}`, `\addcontentsline`, `[4pt]`), doble numeración de encabezados (`anexo-1a.md`), expresiones KaTeX malformadas y comas suprimidas en `T-6.md`. |

---

## 3. Subdocumento 2 — Resumen Ejecutivo, Diagnóstico y Anexos (`subdocumentos/02-problema/`)

### `contenido.tex`
| Área / Sección | Qué se cambió | Por qué se cambió |
| :--- | :--- | :--- |
| **Delimitación de adquisiciones y servicio de campo (§2.5)** | Reemplazado `Curimón adquiere los equipos...` por: `Curimón adquiere el hardware de campo y de red especificado en T-11 en las cantidades y con las características definidas por audIT; audIT provee la infraestructura on-premise, la instalación y el servicio de campo (con montaje externo por lote en M7--M9 y atenciones externas por visita en operación, conservando audIT banco, analista y supervisión técnica), la nube, la conectividad, el soporte y la mantención.` | En E3.2 (`oferta-economica/contenido.tex` L69, `Hardware del mandante`, `Feedback 3.2` P5, `Parámetros corrección` B59 y B78–B83), Curimón adquiere exclusivamente el hardware de campo y red de T-11, mientras audIT provee infraestructura on-premise, montaje externo por lotes M7–M9, servicio externo por visita en operación, nube, conectividad y soporte. |
| **Exclusiones — Combustible (§2.5)** | Precisado `combustible físico` → `combustible físico de la flota vehicular`. | En E3.2 (`Parámetros corrección` B19–B21), audIT presupuesta `50 L/mes` de combustible de pruebas para el grupo electrógeno de la sala técnica desde M4; acotar la exclusión a la flota elimina cualquier ambigüedad. |
| **Innovación 3 (§2.5)** | Precisado `innovación 3 de S13/T-19` → `innovación 3 (verificación de acople y registro térmico) de S13/T-19`. | Alineación terminológica exacta con E3.2 (`costos-venta/contenido.tex` L118 y hoja `Innovaciones` R4). |
| **Citas de Bases y correcciones editoriales** | Corregidas citas de sobrepeso (`4.4` → `4.5`, p. 11) y cierres del paso (`4.6` → `4.12` y Cap. 3); corregida puntuación `, El accidente` → `. El accidente`; unificado `\textit{AUDIT-Subdocumento2-Anexos.pdf}` → `\texttt{...}`. | Exactitud normativa frente a `FEP03.10.26` y consistencia tipográfica interna. |

### `anexos.tex`
| Área / Sección | Qué se cambió | Por qué se cambió |
| :--- | :--- | :--- |
| **Anexo 2.C — `REST-FIS-01`** | Cambiado despliegue secuencial *"en San Bernardo"* por *"al paso por terminal (piloto en San Bernardo y despliegue por lotes en los cinco terminales de la red)"*. | En E3.2 (`Parámetros corrección` R10–R11, R37–R42; `Feedback 3.2` R7), el piloto (10 kits en M6) ocurre en San Bernardo, pero el despliegue masivo externo por lotes (172 kits en M7–M9; 182 montajes base) se ejecuta en los **5 terminales** (San Bernardo, Antofagasta, Talca, Los Ángeles y Puerto Montt). |
| **Anexo 2.C — `EXC-01`** | Acotado a `Suministro de combustible diésel y lubricantes de la flota vehicular`, aclarando que no excluye el combustible de pruebas del grupo electrógeno de la sala técnica. | Coherencia con la provisión de `50 L/mes` de pruebas del grupo electrógeno en E3.2 (`Parámetros corrección` B19–B21). |
| **Anexo 2.A — `REQ-NEG-12`** | Cambiado `previo a sus vencimientos en 2027` → `previo a la renegociación de dos de ellos en 2027`. | En `FEP03.10.26` (§13.1, §13.2, §16.1 Decisión 17, §17.3, §18 Criterio 19), de los 3 contratos bajo costo, **dos** se renegocian en 2027. |
| **Anexo 2.A — 7 citas de Bases y signos `~`** | Corregidas citas en `REQ-NEG-04` (`4.4 y 4.12`), `REQ-NEG-08` (`2.2` + nombre completo Innovación 3), `REQ-NEG-09` (`4.5`), `REQ-NEG-10` (`4.8`), `REQ-NEG-17` (`Art. 4.2 y Art. 27; RT-11.10`), `REQ-NEG-19` (`2.2, 4.6 y 5`), `REQ-NEG-24` (`Cap. 1 y 7.2`). Reemplazados todos los `~6.000` y `(~1.400)` por `$\approx 6.000$` y `($\approx 1.400$)`. | Exactitud con la numeración real de `FEP03.10.26` y `FEP01.26`; en LaTeX, `~` es espacio indivisible y omitía el signo `≈` en PDF y Markdown. |

### `contenido.md` y `anexos.md`
| Qué se cambió | Por qué se cambió |
| :--- | :--- |
| Regeneración completa desde los `.tex` corregidos usando el `.aux` compilado; conversión de `figuraNativa` (TikZ) a resumen estructurado y de `\begin{equation}` a bloque KaTeX válido `$$\begin{aligned}...\end{aligned}$$`; corrección de `(Dirección del Trabajo, 2009)`, `:.**` y eliminación de `Informe Preparatorio 2` y tabla histórica del Informe 1. | Eliminar desincronización desde el 2 de noviembre, referencias rotas (`Figura ?`), código LaTeX/TikZ crudo, error de sintaxis matemática en la ecuación de balance anual y artefactos de exportación. |

---

## 4. Subdocumento 9 — Aseguramiento de Calidad, T-13, T-17 y Catálogo (`subdocumentos/09-calidad/`)

### `contenido.tex`
| Área / Sección | Qué se cambió | Por qué se cambió |
| :--- | :--- | :--- |
| **Referencias cruzadas a S6** | Reemplazadas las 4 ocurrencias de `\tabref{06-tabla-6-3}` por `Tabla 6.3`. | En compilación independiente por subdocumento, `\tabref{06-tabla-6-3}` producía referencias sin resolver (`??` en 9,5 pt), causando fallos en las Reglas 5 y 8 de `verificar.py`. |
| **Figura TikZ `9-cronograma-calidad`** | Ajustada barra `A20` de `8/12` (M14–M17) a `7/13` (M13–M18) e incorporados los hitos `H3 (M6)`, `H6 (M13)`, `H8 (M14)` y `H11 (M19)` en el carril `Hitos E-25`. | Cuadratura exacta con la tabla `9-calendario-contractual` (`Desarrollo E2: M13--M18`) y con los hitos del Formulario E-25 (`Hitos E25` de E3.2). |

### `formularios/T-13.tex`
| Área / Sección | Qué se cambió | Por qué se cambió |
| :--- | :--- | :--- |
| **Referencia cruzada y herramienta CAN** | Reemplazado `\tabref{06-tabla-6-3}` por `Tabla 6.3`; reemplazado `CANoe y analizador independiente` por `Generador/analizador CAN J1939 independiente (banco HIL)`. | Resolver referencia cruzada rota en `verificar.py` (Regla 8) y eliminar la dependencia de licencia comercial **Vector CANoe** no presupuestada en `Licencias D3` (E3.2 presupuesta arriendo de banco CAN/HIL en `Calidad D1`). |

### `formularios/catalogo-T-17.tex`
| Caso(s) de Prueba | Qué se cambió | Por qué se cambió |
| :--- | :--- | :--- |
| **`CP-UAT-02` (incl. variante `RNF-004`)** | Reemplazada `"Cuadrilla de técnicos mecánicos de Curimón S.A."` por `"Equipo de montaje autorizado por audIT (técnico interno en piloto y proveedor externo de montaje en despliegue por lotes) con supervisión operativa del taller de Curimón S.A."`; actualizado umbral bloqueante `< 60 minutos` → `≤ 140 minutos por kit (validada en piloto)`. | En E3.2 (`Feedback 3.2` R7, `Parámetros corrección` R6–R8, B59, B83, `Conciliación técnica` R22), el montaje lo ejecuta audIT/proveedor externo (no mecánicos de Curimón) y el tiempo de referencia presupuestado es **140 min/kit**. Mantener `< 60 min` imponía un criterio de aceptación incumplible. |
| **`CP-PERF-09`, `CP-PERF-12`, `CP-SEC-01`, `CP-UNIT-13`, `CP-INT-13`, `CP-INT-19`, `CP-SYS-02`, `CP-PERF-02`** | Reemplazados: `Datadog Monitoring` → `Azure Monitor y Log Analytics`; `OWASP ZAP Enterprise` → `OWASP ZAP (Apache-2.0)`; `compresión columnar` (Timescale License) → `particiones temporales (chunks) del subconjunto Apache-2`; `JVM/Go` y `Java Testcontainers` → `.NET/Go` y `.NET Testcontainers`; `LocalStack` (AWS) → `Azure SDK Mock`; `Apache Kafka Event Hubs` / `Kafka` → `Azure Event Hubs Premium (protocolo Kafka)`. | Eliminar herramientas comerciales, nubes (AWS) o stacks (Java/JVM) **no presupuestados** en E3.2 (`Proveedores`, `Cuadro maestro`, `3.2-licencias-herramientas.md` y S4/T-11). |
| **`CP-HW-04`** | Reemplazado `Vector CANoe` / `generador Vector` por `generador/analizador de bus CAN SAE J1939 independiente (arrendado en banco HIL)`; corregido `< 0{,}1\%` → `\(< 0{,}1\%\)`. | Coherencia con `Licencias D3` y `Calidad D1` de E3.2 (arriendo de banco HIL sin compra de licencia Vector CANoe) y corrección de sintaxis LaTeX. |
| **`CP-INT-16` y `CP-UAT-03`** | Reformulados para validar el registro de despacho del estanque propio de San Bernardo mediante **PWA de patio o carga estructurada administrativa** conciliada contra telemetría CAN/odómetro del iWave G26I (dejando caudalímetro MQTT/RFID como interfaz opcional futura fuera de alcance base). | `FEP03.10.26` Anexo A declara que el estanque de San Bernardo opera por **planilla**, y E3.2 (`Hardware del mandante`, `Detalle proveedores D4`) **no presupuesta** caudalímetro digital, concentrador MQTT ni lector RFID de surtidor. |
| **`CP-SYS-05` y `CP-PERF-03`** | Agregado `RF-002` a `CP-SYS-05`; actualizado `Requerimiento Trazado` de `CP-PERF-03` de ensayo adicional a `RNF-014 (S3/T-12); RT-07.04 y RT-07.07 (FEP02)`; corregido modo matemático `RTO $\le 4\text{ h}$ y RPO $\le 15\text{ min}$`. | Cuadratura 1:1 con `trazabilidad-T-17.tex` (L7 y L47), carácter contractual obligatorio de DRP (`RT-07.04`/`RT-07.07`) y corrección de renderizado matemático. |
| **`CP-INT-09`** | Generalizado de `Webfleet` / `WebfleetConnectAdapter` / `showOrderReportExtern` a un **perfil simulado de plataforma GPS comercial tercera con OAuth 2.0 vía capa ACL**. | Cumplimiento estricto de la regla de `T-13.tex:32` (*«No se atribuyen marcas o API ensayadas al parque existente sin homologación»*). |

### `contenido.md`, `formularios/T-13.md` y `formularios/T-17.md`
| Qué se cambió | Por qué se cambió |
| :--- | :--- |
| Regeneración completa desde los `.tex` corregidos usando los `.aux` compilados; eliminación de **6.128 `\allowbreak{}`** en `T-17.md`, entorno `contenidoExigido` crudo en `T-13.md`, `figuraNativa` cruda en `contenido.md`, referencias `?`, título erróneo de `T-13.md`, encabezado `Informe Preparatorio 2`, resultado fabricado `"en 12 segundos"` (`CP-SEC-05`) y contaminación `"Polvo Minero"` (`CP-HW-08`). | Sincronización 1:1 con los `.tex` vigentes, eliminación de riesgos graves de evaluación técnica (datos fabricados y contaminación de otro caso) y cumplimiento del título oficial de `FEP01.26` p. 63 (`Plan de pruebas y validación`). |

---

## 5. Artefactos Finales Generados y Verificados

**Ruta de compilación:** `06_Repositorios_Git/repo/recursos/Formato-Oferta-audIT/salida/final-por-subdocumento/`

| Archivo PDF | Páginas | Estado `verificar.py` / Compilación |
| :--- | :---: | :--- |
| `AUDIT-Subdocumento1.pdf` | 27 | Compilado OK · 0 refs rotas · 0 infracciones Art. 50.2 |
| `AUDIT-Subdocumento1-Anexos.pdf` | 7 | Compilado OK · Fecha 25-11-2026 |
| `AUDIT-Formulario-T-6.pdf` | 6 | Compilado OK · Cumple Art. 34.1 y 11 campos T-6 |
| `AUDIT-Subdocumento2.pdf` | 30 | Compilado OK · 0 refs rotas · 0 infracciones Art. 50.2 |
| `AUDIT-Subdocumento2-Anexos.pdf` | 28 | Compilado OK · Anexos 2.A–2.E alineados a E3.2 y Bases |
| `AUDIT-Subdocumento9.pdf` | 18 | Compilado OK · Reglas 5 y 8 CUMPLE (`0` refs rotas) |
| `AUDIT-Formulario-T-13.pdf` | 8 | Compilado OK · Reglas 5 y 8 CUMPLE (`0` refs rotas) |
| `AUDIT-Formulario-T-17.pdf` | 116 | Compilado OK · 120 casos y 42 requisitos trazados |
