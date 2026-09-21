# Auditoría de Calidad Previa al Despacho — Comunicado 9

## TI-12 · Cumplimiento normativo en proyectos TIC · audIT (Empresa N.º 10)

**Caso:** Transportes Curimón S.A. (Licitación TFEP-01/2026)
**Auditor:** Matías V. (Persona 8)
**Fecha del barrido:** 21 de septiembre de 2026
**Corpus auditado:** `Investigacion/Persona-1/` a `Persona-6/` (73 archivos, ~129.000 palabras)
**Marco de control:** Comunicado 9 (`texto/Comunicado_09.md`), Indicaciones FEP00.3.26 §§4, 5 y 6, ficha TI-12.

---

## 1. Método

Barrido cruzado de los seis capítulos entregados contra los cuatro indicios del
Comunicado 9 y contra las exigencias de las Indicaciones. Cada hallazgo indica archivo
y línea, de modo que el responsable pueda verificarlo sin releer el corpus.

| Indicio | Qué se buscó |
| :--- | :--- |
| **(a)** Figuras huérfanas | Tablas y diagramas sin texto que los cite, explique o derive conclusiones |
| **(b)** Cifras no rastreables | Números sin fórmula mostrada, sin fuente, o que no derivan de la volumetría del caso |
| **(c)** Contradicción entre capítulos | Misma decisión de diseño resuelta de dos maneras distintas |
| **(d)** Marcadores residuales | Notas del asistente, referencias a anexos inexistentes, ruptura de la ficción |

---

## 2. Hallazgos críticos

### H-01 · Dos líneas base de TCO vivas en paralelo — indicios (b) y (c)

| | |
| :--- | :--- |
| **Responsable** | Persona 4 (Carlos) |
| **Naturaleza** | Decisión pendiente. No puede resolverla el auditor |

Conviven dos cifras incompatibles para la misma variable:

| Base | Archivos que la sostienen |
| :--- | :--- |
| **7.705,00 UF** (\$308.200.000) | `Subdocumento_P4_Consolidado.md`, `.tex`, `README.md`, `Entregable_1`, `Entregable_2_Modelo_TCO`, `Entregable_3`, `Entregable_4_Sensibilidad` |
| **8.375,40 UF** (\$335.016.000) | `Subdocumento_P4_Consolidado_Definitivo.md`, `Bitacora_A6_Persona_4`, y ya citada por P6 en `P_Avanzadas.md:35,61` y en su `.tex` |

El archivo marcado como definitivo **se contradice a sí mismo**: su §3 declara 8.375,4 UF,
pero la matriz de sensibilidad del §4.2 (línea 116) fija como «Escenario Base · Línea
Central · Baseline (0,00%)» la cifra de **7.705,00 UF**, con los escenarios ±6,14%
anclados a ella. El §4.1 sí fue migrado (10.330,6 = 8.375,4 + 1.955,2). La migración
quedó a medio camino.

Lo mismo ocurre con el valor actual neto: **5.757,68 UF** (`E-2`, `E-4`, `.tex`, README)
frente a **6.582,3 UF** (Definitivo, A-6). La tasa es la misma en ambos (0,9 % mensual
= 11,351 % anual); lo que cambia es la base.

> La discrepancia registrada en `PENDIENTES_Y_CORRECCIONES_POR_PERSONA.md` (6.582,3
> frente a 6.537,13 UF) **ya no existe en el repositorio**. La discrepancia real es la
> aquí descrita y es de mayor magnitud.

**Acción:** Persona 4 elige una base, corrige el §4.2 del definitivo y propaga a los
demás archivos. Persona 6 y Persona 7 dependen de esta decisión.

---

### H-02 · Atribución del deber de reporte al «Art. 14» de la Ley 21.663 — indicio (c)

| | |
| :--- | :--- |
| **Responsable** | Persona 4 (Carlos) |
| **Naturaleza** | Errata verificada. Corrección mecánica |

Persona 2 dejó consignado en su propio capítulo (`Entregable_2_Ley_21663`, §2):
«*Cualquier capítulo que atribuya el deber de reporte al «Artículo 14» de la Ley N° 21.663
incurre en un error de cita verificable contra el texto oficial*». Persona 5 corrigió sus
apariciones (commit `9e6b246`) y Persona 6 usa el Art. 9 correctamente.

Persona 4 conserva la atribución errónea en siete lugares, **incluido el archivo
definitivo**:

| Archivo | Línea |
| :--- | :---: |
| `Subdocumento_P4_Consolidado_Definitivo.md` | 144 |
| `Subdocumento_P4_Consolidado.md` | 28, 76, 101 |
| `Subdocumento_P4_Consolidado.tex` | 166 |
| `Entregable_3_Tabla_Precios_Metadatos.md` | 76, 124 |
| `Entregable_4_Analisis_Sensibilidad.md` | 98 |
| `Manual_Operativo_Persona_4.md` | 302 |

Dos capítulos del mismo informe afirman cosas opuestas sobre el mismo artículo: es el
supuesto textual del indicio (c).

**Corrección:** deber de reporte → **Art. 9**; calificación del efecto significativo →
**Art. 27**; plazos 3/72/15 → **D.S. N° 295/2024**.

---

### H-03 · La plataforma GRC presupuestada no fue evaluada — indicio (c)

| | |
| :--- | :--- |
| **Responsables** | Persona 3 (Ignacio V.) y Persona 4 (Carlos) |
| **Naturaleza** | Decisión pendiente entre ambos |

Persona 3 compara ocho plataformas con criterios ponderados y la ganadora es
**Microsoft Purview** (3,70). **CISO Assistant no aparece ni una sola vez en
`Persona-3/`.** Persona 4 la presupuesta como la herramienta adoptada (280,00 UF en 56
meses) y Persona 6 le dedica una pregunta del cuestionario sobre su licenciamiento
AGPLv3 (`P_Basicas.md:56,85`).

El informe compara una cosa, cotiza otra y pregunta por la segunda.

**Acción:** acordar una sola herramienta, o presentarlas explícitamente como decisiones
distintas y justificar por qué (por ejemplo, Purview como capa de descubrimiento dentro
del ecosistema Azure ya comprometido y CISO Assistant como registro de cumplimiento
autoalojado). Lo que no puede quedar es la elección sin explicar.

---

### H-04 · Matriz de decisión sin análisis posterior — indicio (a)

| | |
| :--- | :--- |
| **Responsable** | Persona 3 (Ignacio V.) |
| **Naturaleza** | Redacción faltante. Nivel 0 obligatorio (§6.1: análisis comparativo) |

`Subdocumento_Persona_3_Consolidado.md` cierra el §3.3 con la matriz de puntuación
(línea 159 y siguientes) y salta directamente a `## 4. Cierre del subdocumento`. **Ningún
párrafo nombra a Purview como recomendación, explica por qué gana ni interpreta el
resultado.** El cierre se refiere a «la licencia anual de la herramienta recomendada»
sin decir cuál es.

Esto es exactamente lo que el Comunicado 9 describe en su letra a): una tabla que aparece
sin que el texto la cite, la explique ni derive conclusiones de ella.

Agravante de indicio (b): las columnas «Encaje Azure» y «Esfuerzo de operación» puntúan
datos que **no existen en la ficha objetiva del §3.2**. El propio documento lo reconoce
en la línea 153: «*Se infiere del modelo de despliegue, no está como columna en tu tabla
actual*».

**Acción:** dos párrafos tras la matriz —por qué gana Purview pese a puntuar 1 en
consentimiento, y qué significa que seis de ocho proveedores no publiquen precio a la luz
del punto 5 de las Indicaciones— y una columna o nota que justifique las dos puntuaciones
inferidas.

---

### H-05 · Voz del asistente dentro del cuerpo del informe — indicio (d)

| | |
| :--- | :--- |
| **Responsable** | Persona 3 (Ignacio V.) |
| **Naturaleza** | Corrección mecánica |

| Línea | Texto |
| :---: | :--- |
| 153 | «…no está como columna en **tu tabla actual**» |
| 156 | «**Si al reunirse con P2 deciden** que la transparencia del precio pesa menos porque de todas formas van a cotizar, **bájenla y suban** encaje con arquitectura» |
| 159 | «### 2. Matriz de puntuación **con tus datos**» |

Es texto dirigido al autor, no al evaluador. Es el hallazgo de detección más inmediata
de todo el corpus.

---

### H-06 · Cifras sin origen rastreable — indicio (b)

| | |
| :--- | :--- |
| **Responsable** | Persona 4 (Carlos) |
| **Naturaleza** | Aportar fuente o retirar |

| Cifra | Dónde | Situación |
| :--- | :--- | :--- |
| **«~215.000 UF» de presupuesto total de la licitación** | `…Definitivo.md` §3.3 | Búsqueda sobre las tres bases (FEP01, FEP02, FEP03) con `tools/buscar.py`: **no hay monto total publicado**. De esta cifra se deriva el 3,9 % de proporcionalidad |
| **«rango 3 %–5 % de la industria logística»** | `…Definitivo.md` §3.3 | Sin fuente |
| **«rebaja de la sanción entre un 50 % y un 70 %»** | `E-4:103` y `Subdocumento:101` | Persona 2 verificó (DC-07) que **ninguna fuente atribuye porcentaje** al Art. 49. Sigue sin corregir |
| **Azure Key Vault** | Un residuo, no una contradicción | **0,00 UF marginal** en el subdocumento antiguo y su README («absorbido en tier CSP»), superado por el definitivo. Las cifras **725,4 UF** (claves) y **845,4 UF** (claves + 120 UF de ingeniería) son dos alcances coherentes, y Persona 5 cita la segunda. Detalle en `Verificacion_Aritmetica_P4.md`, §6 |

Una cifra porcentual sin respaldo dentro de un modelo financiero es el supuesto literal
de la letra b) del Comunicado 9.

---

### H-07 · Conflicto de arquitectura criptográfica — indicio (c)

| | |
| :--- | :--- |
| **Responsables** | Persona 4 (Carlos) y Persona 5 (Martín) |

Persona 4, en el §4.1 del definitivo, adopta **Key Vault Premium** (725,4 UF) y descarta
explícitamente **Managed HSM** por costo (2.680,6 UF). Persona 5, en
`Entregable_3_Transferencias_Internacionales.md:56`, especifica para la región Chile
Central **«Azure Key Vault Managed HSM (FIPS 140-2 Nivel 3 local)»**: precisamente la
alternativa descartada.

Es una contradicción de tecnología entre capítulos, con su cifra asociada.

---

### H-08 · Anexos sin plan maestro — indicio (d)

| | |
| :--- | :--- |
| **Responsable** | Persona 1 (Ignacio C.), con insumo de todos |

| Capítulo | Anexo que invoca |
| :--- | :--- |
| Persona 6 | Anexo E |
| Persona 4 | Anexo A, Anexo D |
| Persona 3 | Anexo C, Anexo I |

No existe índice de anexos. Tal como está, cada capítulo remite a un anexo que el informe
no contiene: «referencias a secciones o anexos inexistentes», letra d).

Relacionado: `Subdocumento_Persona_6_Consolidado.tex` invoca el paquete
**`informe-ti12.sty`**, que **no existe en el repositorio**. El `.tex` no compila.

---

### H-09 · Ruptura de la ficción dentro de un entregable — indicio (d)

| | |
| :--- | :--- |
| **Responsable** | Persona 4 (Carlos) |
| **Naturaleza** | Corrección mecánica |

`Subdocumento_Persona_4_Consolidado_Definitivo.md` §8, línea 273:

> «Conforme a las reglas del Comunicado 9, **el docente evaluador** puede interrogar
> aleatoriamente a cualquier integrante… **La Persona 4** debe dominar con soltura…»

Es coordinación interna dentro de un capítulo del informe. Su lugar es el manual
operativo.

Caso análogo menor: `Entregable_1_Matriz_Obligaciones.md:168`, referencia (5), cita a la
PUCV como **fuente de las Bases Técnicas del Caso 10**, mezclando el plano académico con
el de la licitación.

> Las cabeceras «Asignatura: ICI-5444 · Escuela de Informática, PUCV» de los
> subdocumentos **no se consideran hallazgo**: el entregable es un trabajo de
> investigación académico, no la propuesta de licitación.

---

### H-10 · Fecha de vigencia de la Ley 21.719 — indicio (c), DC-01 parcialmente cerrado

| | |
| :--- | :--- |
| **Responsable** | Persona 4 (Carlos) |
| **Naturaleza** | Errata verificada. Corrección mecánica |

Persona 2 verificó contra el Art. primero transitorio («*el día primero del mes vigésimo
cuarto posterior a su publicación*») que la vigencia es el **01/12/2026**, no el
13/12/2026.

| Archivo | Apariciones pendientes |
| :--- | :---: |
| `Entregable_1_Matriz_Obligaciones.md` | 12 |
| `Subdocumento_P4_Consolidado.md` | 10 |
| `Subdocumento_P4_Consolidado_Definitivo.md` | 0 (corregido) |

La matriz de obligaciones es el entregable que la ficha TI-12 exige por nombre y es el
que conserva el error.

---

### H-11 · Artículo del Delegado de Protección de Datos — sin verificar

| | |
| :--- | :--- |
| **Responsable** | Persona 8 (verificación) y Persona 4 (redacción) |
| **Naturaleza** | Requiere fuente primaria. **No es corrección mecánica** |

Tres versiones conviven: Persona 4 cita **Art. 48** (`…Definitivo.md:63`,
`Entregable_2:208`, `Justificacion_Proxys:58`); Persona 6 cita **Art. 50**
(`P_Basicas.md:78`); Persona 2 investigó y encontró fuentes que discrepan entre **Art. 49
y Art. 50**, sin que **ninguna sitúe el DPO en el Art. 48** (DC-05, marcado `[NV]`).

Punto adicional de fondo, señalado por Persona 2: la designación del DPO es
**facultativa** en la Ley 21.719, a diferencia del Art. 37 del RGPD. Persona 4 presupuesta
2.016,0 UF de *retainer* de DPO presentándolo como obligación legal (OB-05). Si se
mantiene la partida, hay que reformular la justificación como **decisión de diseño de
cumplimiento del proyecto**, no como mandato legal, o la cifra queda sin fundamento.

**Acción:** hasta que la verificación en fuente primaria se cierre, citar la obligación
**sin numeral**.

---

### H-12 · Matiz de plazos de reporte — menor

Persona 6 (`P_Intermedias.md:85`) atribuye la reducción del segundo reporte de 72 a 24
horas a la condición de **OIV**. Persona 2 (`Entregable_2`, §5.1) la atribuye a la
afectación de **servicios esenciales**, que es una categoría distinta —y Persona 3 sostiene
que Curimón queda obligada por ser servicio esencial **aunque no figure como OIV**.

Es un matiz, pero es del tipo que se verifica en segundos contra el D.S. 295/2024.

---

## 3. Defectos de forma en el capítulo de Persona 3

Independientes del contenido, todos de corrección inmediata:

| Línea | Defecto |
| :---: | :--- |
| 6 | `### 1.1 Aapertura` — errata |
| 40 | `# Análisis de la asimetría normativa:` — encabezado de nivel 1 a mitad de documento y con dos puntos finales |
| 80 | `### Justificación del aporte.` — sin numerar y con punto final |
| 145 / 159 | `#### 1. Criterios ponderados` seguido de `### 2. Matriz…` — jerarquía invertida |
| Tabla §3.2 | Fechas en formato `[20-9-2026]`, entre corchetes e inconsistentes con el resto del informe (`20-09-2026`) |
| Referencias, fila 3 | Acento grave suelto al final de la URL del Reglamento (UE) 2024/1689 |
| Referencias, fila 6 | **ISO/IEC 27001:2022 apunta a `iso.org/standard/27701`** — enlace equivocado, idéntico al de la fila 7 |

---

## 4. Estado consolidado por integrante

| Persona | Responsable | Estado | Bloqueante |
| :---: | :--- | :--- | :---: |
| **P1** | Ignacio C. | Estructura completa, contenido 0 %. Los cuatro bloques `> **COMPLETAR A MANO.**` siguen en blanco: resumen ejecutivo, aporte propio, discusión crítica y conclusiones. Son las cuatro secciones donde §6.1 prohíbe la IA | **Sí** |
| **P2** | Alonso | El capítulo más sólido del corpus. Método de tres niveles de certeza declarado y aplicado. Pendientes: 29 celdas `[CG]` y los `[NV]` del §7.2 | No |
| **P3** | Ignacio V. | Investigación correcta, redacción no entregable: H-04, H-05 y los defectos del §3 de esta auditoría | **Sí** (H-04, H-05) |
| **P4** | Carlos | Mayor volumen y mayor riesgo: H-01, H-02, H-06, H-07, H-09, H-10, H-11 | **Sí** (H-01) |
| **P5** | Martín | Limpio. DC-02, DC-04 y DC-06 cerrados. Único pendiente: H-07 | No |
| **P6** | Marcel | Completo: 30 preguntas (12/12/6), cuatro formatos, índice temático. Bien alineado con la línea normativa de P2 (Art. 9, DPO facultativo, Art. 49 atenuante). Depende de H-01 y H-03 | No |
| **P7** | Naomi | Carpeta inexistente. Sin presentación ni libreto de defensa | **Sí** |
| **P8** | Matías | Esta auditoría, la tabla de vigencias y el A-6 consolidado | **Sí** (A-6) |

---

## 5. Cierre

El corpus tiene fondo suficiente y en algunos capítulos —Persona 2, Persona 5, Persona 6—
trabajo de ingeniería propio claramente evidenciado. El riesgo no está en la investigación
sino en el ensamblaje: **dos cifras maestras sin unificar, una herramienta comparada que
no es la presupuestada y dos tablas de decisión sin conclusión escrita**.

Los hallazgos H-02, H-05, H-09 y H-10 son erratas verificadas y se corrigen sin decidir
nada. Los hallazgos H-01, H-03, H-04, H-06, H-07 y H-11 exigen que su autor decida o
redacte: el auditor los reporta, no los resuelve, porque cada integrante debe poder
explicar oralmente lo que firma.

---

*Barrido realizado el 21 de septiembre de 2026 sobre el estado del repositorio en la rama
`main`. Los números de línea corresponden a ese estado y se desplazan con cada corrección
aplicada.*
