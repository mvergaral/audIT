# Directrices de Vigencia Normativa e Interfaces con P1, P3, P4 y P5
## Datos Congelados por Persona 2 y Contradicciones Cruzadas Detectadas en el Corpus del Equipo

**Asignatura:** Taller de Formulación de Proyectos Informáticos (ICI-5444) · Escuela de Informática, PUCV  
**Empresa Consultora:** AudIT (Empresa 10)  
**Emisor:** Persona 2 (*Chilean Regulatory Research Specialist*)  
**Destinatarios:** Persona 1 (integración editorial), Persona 3 (marco internacional), Persona 4 (modelo económico), Persona 5 (arquitectura), Persona 8 (auditoría)  
**Fecha de emisión:** 21 de septiembre de 2026 · **Fecha de corte de la investigación:** 20 de septiembre de 2026  
**Estado:** **ACTA DE CONGELAMIENTO NORMATIVO + 8 DISCREPANCIAS CRUZADAS ABIERTAS**

> [!CAUTION]
> **Este documento es de lectura obligatoria antes del ensamblaje final.** Conforme a la Sección 3.4 del Plan Operativo, **Persona 2 es la dueña del dato «fechas de vigencia de normas chilenas»**. Ningún capítulo puede usar una fecha, un artículo o una cuantía chilena distinta de las congeladas aquí sin autorización formal de P1 y P8 documentada como enmienda al *baseline*. Las ocho discrepancias de la Sección 3 **fueron detectadas contra el corpus ya entregado por P4 y P5** y **requieren resolución antes de la entrega**.

---

## 1. Datos Congelados: Fechas de Vigencia y Estado Normativo

| Norma | Publicación (D.O.) | Entrada en vigencia | Estado al 20-09-2026 | Certeza |
| :--- | :---: | :---: | :--- | :---: |
| **Ley N° 21.719** (datos personales) | **13-12-2024** | **1 de diciembre de 2026** (Art. **primero** transitorio) | **PUBLICADA, NO VIGENTE.** Agencia **no constituida**. Proyecto de postergación (Boletín N° 18.623-07) **en primer trámite, sin votar, NO es ley** | **[V]** |
| **Ley N° 21.663** (ciberseguridad) | **08-04-2024** | **01-01-2025** general · **01-03-2025** Arts. 5, 8, 9 y Título VII | **PLENAMENTE VIGENTE Y EXIGIBLE** | **[S]** |
| **D.S. N° 295/2024** (reporte de incidentes) | **01-03-2025** | 01-03-2025 | **VIGENTE** — esquema 3/72/15 | **[V]** |
| **Ley N° 19.628** (vida privada) | 28-08-1999 **[NV]** | 1999 | **VIGENTE Y APLICABLE hasta el 30-11-2026** | **[S]** |
| **Ley N° 21.180** (transformación digital) | 11-11-2019 | 09-06-2022, **gradual** | **VIGENCIA PARCIAL**; tope legal **31-12-2027** | **[S]** |
| **Ley N° 21.729** (telecomunicaciones) | **13-02-2025** | Inmediata, **sin período de gracia** | **VIGENTE** | **[S]** |
| **Ley N° 21.459** (delitos informáticos) | Junio 2022 **[NV]** | — | **VIGENTE** | **[S]** |

> [!IMPORTANT]
> **Regla de oro del congelamiento.** La fecha **1 de diciembre de 2026** proviene de la fórmula literal del Artículo primero transitorio: «hasta el día primero del mes vigésimo cuarto posterior a su publicación». Publicada el 13-12-2024, **el mes vigésimo cuarto posterior es diciembre de 2026 y su día primero es el 1 de diciembre de 2026**. **No es «24 meses después del 13-12-2024» ni, por tanto, el 13 de diciembre de 2026.**

---

## 2. Matriz de Interfaces: qué Entrega P2 y qué Debe Respetar Cada Rol

| Destinatario | Insumo que P2 entrega | Obligación de consistencia |
| :--- | :--- | :--- |
| **P1** (integración) | Fechas de vigencia, terminología legal, estado de cada norma. | Verificar que **ningún capítulo** use una fecha de vigencia distinta a la de la tabla §1. Verificar uso uniforme de «responsable» / «mandatario o encargado». |
| **P3** (internacional) | Columna nacional del cuadro comparativo (Entregable 5). | Las celdas marcadas `[CG]` de la columna RGPD/NIS2 **no están verificadas por P2**: P3 debe confirmarlas contra EUR-Lex **o retirarlas**. |
| **P4** (económico) | Cuantías de multas, categorías de infracción, plazos legales, fechas de exigibilidad. | La columna «plazo» de la matriz de obligaciones **debe replicar las fechas de §1**. Toda cuantía debe declarar la paridad UTM usada. |
| **P5** (arquitectura) | Artículos que fundan cada control, canales y plazos de reporte, régimen de transferencias. | **Ningún diagrama puede citar un artículo distinto al congelado en §4.** El canal de la Agencia PDP debe representarse como **destinatario inexistente hoy**. |
| **P6** (cuestionario) | Todo el articulado verificado. | Solo puede preguntar sobre artículos marcados **[V]** o **[S]**; **jamás sobre los [NV]**. |
| **P8** (auditoría) | Listado de vacíos priorizados (Entregable 6, §3). | Debe verificar el punto 1 (estado del Boletín N° 18.623-07) **hasta la fecha de entrega**. |

---

## 3. Discrepancias Cruzadas Detectadas — REQUIEREN RESOLUCIÓN

> [!CAUTION]
> **Detectadas por P2 contra el corpus ya publicado de P4 y P5.** Cada una es un **indicio directo del Comunicado 9, letra c** (contradicciones entre capítulos escritos por separado). Se listan con la corrección propuesta y la evidencia que la sostiene.

### DC-01 · Fecha de vigencia de la Ley N° 21.719 — **CRÍTICA**

| Aspecto | Detalle |
| :--- | :--- |
| **Dónde** | `Persona-4/Entregables/Entregable_1_Matriz_Obligaciones.md` (líneas 41 y 152) y `Persona-4/Subdocumento_Persona_4_Consolidado.md` (filas OB-02 y OB-03). |
| **Lo que dice P4** | «vigencia diferida (*vacatio legis* de 24 meses), entrando en régimen general el **13 de diciembre de 2026**». |
| **Lo verificado por P2** | El Art. primero transitorio dice «hasta el día primero del mes vigésimo cuarto posterior a su publicación» → **1 de diciembre de 2026** **[V]**. |
| **Corrección** | Sustituir **13/12/2026 → 01/12/2026** en todas las apariciones. |
| **Impacto** | 12 días de diferencia. Afecta el hito de exigibilidad del DPO (OB-05) y la fila de plazos de toda la matriz de obligaciones. |

### DC-02 · Artículo del deber de reporte de incidentes (Ley N° 21.663) — **CRÍTICA**

| Aspecto | Detalle |
| :--- | :--- |
| **Dónde** | P4: `Subdocumento` fila OB-08, `Manual_Operativo` línea 302, `Entregable_4_Analisis_Sensibilidad` línea 98. P5: `Subdocumento` líneas 44 y 51, `Entregable_1_Arquitectura` línea 63, `Entregable_4_Vinculo` línea 63. |
| **Lo que dicen P4 y P5** | «notificación al CSIRT Nacional en menos de 3 horas (**Ley 21.663 Art. 14**)». |
| **Lo verificado por P2** | El deber de reportar incidentes con efectos significativos es el **Artículo 9**; la calificación del efecto significativo es el **Artículo 27** **[V]**; los plazos 3/72/15 están en el **D.S. N° 295/2024**. **Ninguna fuente sitúa el deber de reporte en el Artículo 14.** |
| **Corrección** | Sustituir **«Art. 14»** por **«Art. 9 de la Ley N° 21.663 y D.S. N° 295/2024»** en las 7 apariciones. |
| **Impacto** | Error de cita repetido en dos capítulos y en un diagrama. Es el tipo de dato que el docente puede verificar en segundos contra el texto oficial. |

### DC-03 · Artículo de la multa gravísima de la Ley N° 21.719

| Aspecto | Detalle |
| :--- | :--- |
| **Dónde** | `Persona-4/Subdocumento_Persona_4_Consolidado.md`, línea 101. |
| **Lo que dice P4** | «Multa Gravísima Ley N° 21.719 (**Art. 46**) de hasta 20.000 UTM». |
| **Lo verificado por P2** | La escala de multas es el **Artículo 35**; las infracciones gravísimas son el **Artículo 34 quáter** **[S]**. El Artículo 46 no aparece en ninguna fuente como norma sancionatoria de la Ley N° 21.719. |
| **Corrección** | Sustituir por **«Arts. 34 quáter y 35»**. |

### DC-04 · Artículo 8 ter: bloqueo, no borrado

| Aspecto | Detalle |
| :--- | :--- |
| **Dónde** | `Persona-5/Subdocumento_Persona_5_Consolidado.md`, línea 51. |
| **Lo que dice P5** | «clave simétrica por titular para garantizar el **derecho al borrado criptográfico (Art. 8 ter)**». |
| **Lo verificado por P2** | El **Art. 8 ter es BLOQUEO**, definido como «suspensión temporal de las operaciones de tratamiento mientras se resuelve la solicitud». La **supresión o cancelación es el Art. 7** **[S]**. |
| **Corrección** | Si el control es borrado criptográfico → citar **Art. 7**. Si es suspensión temporal → mantener Art. 8 ter y corregir la descripción. **P5 debe decidir cuál de los dos derechos implementa realmente el control.** |

### DC-05 · Artículo del DPO

| Aspecto | Detalle |
| :--- | :--- |
| **Dónde** | `Persona-4/Entregables/Entregable_1_Matriz_Obligaciones.md` (OB-05) y `Entregable_2_Modelo_TCO.md` línea 208. |
| **Lo que dice P4** | «Ley N° 21.719 (que incorpora el **Art. 48** a la Ley N° 19.628)» para el nombramiento del DPO. |
| **Lo investigado por P2** | Las fuentes discrepan entre **Art. 49** (Future of Privacy Forum, DLA Piper) y **Art. 50** (BCN). **Ninguna fuente consultada sitúa el DPO en el Artículo 48** **[NV]**. |
| **Corrección propuesta** | Citar como **«Art. 49 o 50 (numeración no resuelta entre fuentes)»** o, preferentemente, **omitir el número de artículo** y citar la obligación sin numeral hasta que P8 la verifique. |
| **Nota adicional** | P2 verificó que **la designación del DPO es FACULTATIVA** bajo la Ley N° 21.719, a diferencia del Art. 37 del RGPD, salvo dentro de modelos de cumplimiento certificados. **Si P4 presupuesta un DPO como obligación legal, debe reformular la justificación**: es una decisión de diseño de cumplimiento del proyecto, no un mandato legal. |

### DC-06 · Fundamento del principio de seguridad desde el diseño

| Aspecto | Detalle |
| :--- | :--- |
| **Dónde** | `Persona-4/Subdocumento_Persona_4_Consolidado.md`, fila OB-02; `Persona-5/Subdocumento`, §2. |
| **Lo que dicen** | «Arts. **3° sexies** y **14 bis**» como fundamento de la seguridad desde el diseño. |
| **Lo investigado por P2** | El **Art. 3°** contiene **ocho principios designados por LETRAS**, no por ordinales latinos; la seguridad es la **letra f)**. El **Art. 14 bis** es **secreto y confidencialidad**. El deber de adoptar medidas de seguridad es el **Art. 14 quinquies** **[S]**. **El listado completo de las ocho letras del Art. 3° no pudo verificarse [NV].** |
| **Corrección propuesta** | Citar **«Art. 3° letra f) y Art. 14 quinquies»**. Si se prefiere no arriesgar, citar **«principio de seguridad del Art. 3° y deber de medidas de seguridad del Art. 14 quinquies»** sin letra. |

### DC-07 · Atenuante del modelo de prevención: porcentaje sin fuente

| Aspecto | Detalle |
| :--- | :--- |
| **Dónde** | `Persona-4/Entregables/Entregable_4_Analisis_Sensibilidad.md`, línea 103; `Subdocumento` línea 101 («mitigables hasta un 70 % mediante la atenuante del Art. 49»). |
| **Lo que dice P4** | El modelo de prevención «permite a la Agencia rebajar la cuantía de la sanción pecuniaria **entre un 50 % y un 70 %**». |
| **Lo investigado por P2** | El **Art. 49** regula el modelo de prevención certificado y el **Art. 52** fija su duración en 3 años. **Ninguna fuente consultada afirma que opere como eximente ni atribuye un porcentaje específico de rebaja.** Su efecto documentado es **atenuante en la graduación** (Arts. 36 y 37, **cuyo detalle es [NV]**) y **reputacional** vía registro del Art. 40 **[S]**. |
| **Acción requerida** | **P4 debe aportar la fuente primaria del rango 50-70 % o retirar la cifra.** Una cifra porcentual sin respaldo en un modelo financiero es exactamente el indicio descrito en el Comunicado 9, letra b. |

### DC-08 · Paridad de la UTM y fecha de corte

| Aspecto | Detalle |
| :--- | :--- |
| **Dónde** | P4 usa **1 UTM = $70.000 CLP** (paridad contractual, Formulario E-24) y fecha de corte **16/09/2026**. P2 cita **1 UTM ≈ $69.542** (noviembre de 2025, fuente Firewall Chile) y fecha de corte **20/09/2026**. |
| **Diagnóstico** | **No es una contradicción**: son dos parámetros correctos en marcos distintos. P4 opera con una paridad **congelada por contrato de licitación**; P2 cita el valor **de la fuente consultada**. |
| **Acción requerida** | **Declararlo explícitamente en el informe.** Regla propuesta: **todas las conversiones a CLP del informe usan la paridad contractual E-24 (1 UTM = $70.000)**, y la cifra de $69.542 se cita únicamente como valor de la fuente original, entre paréntesis. **P1 debe además unificar la fecha de corte del informe**; se propone **20 de septiembre de 2026**, por ser la del barrido normativo más reciente. |

---

## 4. Artículos Congelados de Cita Obligatoria

> [!IMPORTANT]
> Todo capítulo que invoque uno de estos conceptos **debe usar exactamente este numeral**. Los marcados **[NV]** **no deben citarse con número**.

### Ley N° 21.719

| Concepto | Artículo | Certeza |
| :--- | :---: | :---: |
| Vigencia diferida | **Primero transitorio** | **[V]** |
| Definición de responsable | Art. 2° letra n) | [S] |
| Datos sensibles | Art. 2° letra g) | [S] |
| Principios | Art. 3° (ocho letras; seguridad = letra f) | [S] / listado completo **[NV]** |
| Derechos: acceso / rectificación / supresión / oposición | Arts. 5 / 6 / **7** / 8 | [S] |
| Decisiones automatizadas | Art. 8 bis | [S] |
| **Bloqueo (suspensión temporal)** | **Art. 8 ter** | [S] |
| Portabilidad | Art. 9 | [S] |
| **Plazo de respuesta: 30 días CORRIDOS + 30** | **Art. 11** | **[V]** |
| Consentimiento | Art. 12 | [S] |
| **Bases de licitud (5 letras, sin interés vital)** | **Art. 13** | **[V]** |
| Secreto y confidencialidad | Art. 14 bis | [S] |
| Información y transparencia | Art. 14 ter | [S] |
| **Deber de medidas de seguridad** | **Art. 14 quinquies** | [S] |
| **Notificación de brechas — «sin dilaciones indebidas», SIN plazo en horas** | **Art. 14 sexies** | **[V]** |
| **Régimen del encargado** | **Art. 15 bis** | **[V] parcial** |
| Evaluación de impacto (EIPD) | Art. 15 ter | [S] |
| Geolocalización | Art. 16 sexies | [S] |
| Sector público | Art. 20 | [S] |
| **Transferencias internacionales** | **Arts. 27-29** | **[V]** |
| Agencia: naturaleza / atribuciones / Consejo | Arts. 30 / 30 bis / 30 ter | [S] |
| Infracciones leves / graves / gravísimas | Arts. 34 bis / 34 ter / 34 quáter | [S] |
| **Escala de multas** | **Art. 35** | [S] |
| Graduación y atenuantes | Arts. 36 y 37 | **[NV]** |
| Registro Nacional de Sanciones | Art. 40 | [S] |
| Tutela administrativa / infracción / reclamo de ilegalidad | Arts. 41 / 42 / 43 | [S] |
| Responsabilidad civil | Art. 47 | [S] |
| Modelo de prevención certificado | Art. 49 | [S] |
| **DPO** | **Art. 49 o 50 — NO CITAR NÚMERO** | **[NV]** |
| **Registro de actividades de tratamiento** | **¿15 o 15 bis? — NO CITAR NÚMERO** | **[NV]** |

### Ley N° 21.663

| Concepto | Artículo | Certeza |
| :--- | :---: | :---: |
| Ámbito y sectores esenciales | Art. 4 | **[V]** |
| **Criterios sustantivos de OIV** | **Art. 5** | **[V]** |
| Procedimiento de calificación y revisión trienal | Art. 6 | **[V]** |
| Deberes generales (PSE) | Art. 7 | [S] |
| Deberes reforzados (OIV) | Art. 8 | [S] |
| **Deber de reportar incidentes** | **Art. 9** | [S] |
| Relación ministerial | Art. 10 | **[V]** |
| Consejo Multisectorial | Art. 20 | [S] |
| **«Incidente de efecto significativo»** | **Art. 27** | **[V]** |
| Equivalencia normativa sectorial (CMF) | Art. 37 | [S] |
| **Procedimiento sancionatorio** | **Art. 42** | **[V]** |
| **Reclamación ante Corte de Apelaciones** | **Art. 46** | **[V]** |
| Cuantías | **Título VII — articulado [NV]** | **[NV]** |

---

## 5. Terminología Unificada (Control de Coherencia de P1)

| Uso correcto | Uso prohibido | Motivo |
| :--- | :--- | :--- |
| **Ley N° 21.719** | «Ley 21719», «LPDP», «Ley N.º 21.719» | Estilo unificado del corpus AudIT. |
| **«mandatario o encargado»** | «procesador», «*data processor*» | Fórmula literal de la ley chilena; **no existe definición autónoma de «encargado»**. |
| **Agencia de Protección de Datos Personales** (o **Agencia PDP**) | «APD», «AEPD» | La AEPD es la autoridad española. |
| **Operador de Importancia Vital (OIV)** — invariable en plural | «OIVs» | Sigla invariable. |
| **Prestador de Servicios Esenciales (PSE)** | «servicios críticos» | Categoría legal distinta. |
| **RGPD** | «GDPR» | Unificado al español en todo el informe. |
| **ANCI** / **CSIRT Nacional** | usarlos como sinónimos | El CSIRT Nacional es una **función operada por** la ANCI, no un órgano separado. |
| **«no se encontró evidencia de…»** | «no existe…» | Ausencia de evidencia ≠ evidencia de ausencia. |
| **«la Ley N° 21.719 sustituye a la Ley N° 19.628»** | «la deroga» | **No la deroga**: conserva los Arts. 17, 18 y 19 y parte del Art. 2°. |

---

## 6. Alerta Permanente hasta la Entrega

> [!CAUTION]
> **VARIABLE VIVA — Boletín N° 18.623-07.** Si entre el 20 de septiembre y la fecha de entrega el proyecto de postergación fuera **aprobado y publicado en el Diario Oficial**, **cambian**: la fecha de vigencia (a 01-12-2027), la composición del Consejo Directivo (de 3 a 5), el plazo de designación (12 meses antes) y el alcance de las amonestaciones del primer año. **P8 debe verificar `tramitacion.senado.cl` y el Diario Oficial antes del despacho.** A la fecha de emisión de estas directrices, **el proyecto sigue sin votación y la fecha congelada es el 1 de diciembre de 2026**.
