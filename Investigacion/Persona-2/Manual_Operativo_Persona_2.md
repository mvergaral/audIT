# Manual Operativo — Persona 2
## Método de Investigación Normativa, Convenciones de Estilo y Protocolo Anti-Comunicado 9

**Asignatura:** Taller de Formulación de Proyectos Informáticos (ICI-5444) · Escuela de Informática, PUCV  
**Empresa Consultora:** AudIT (Empresa 10)  
**Tema de Investigación:** TI-12 · *Cumplimiento normativo en proyectos TIC: Ley 21.719, Ley 21.663 (ANCI) y marco internacional*  
**Rol:** Persona 2 · *Chilean Regulatory Research Specialist*  
**Fecha de corte de la investigación:** 20 de septiembre de 2026

---

## 1. Alcance del Rol y Cumplimiento del Encargo

| # | Tarea asignada en el Plan Operativo | Entregable que la cumple | Estado |
| :---: | :--- | :--- | :---: |
| 1 | Análisis profundo de la **Ley N° 21.719** | [Entregable 1](Entregables/Entregable_1_Ley_21719_Datos_Personales.md) | ✅ |
| 2 | Análisis profundo de la **Ley N° 21.663** | [Entregable 2](Entregables/Entregable_2_Ley_21663_Ciberseguridad_ANCI.md) | ✅ |
| 3 | **Ley N° 21.180**, **Ley N° 19.628** y **≥ 2 normativas adicionales** justificadas | [Entregable 3](Entregables/Entregable_3_Normativa_Complementaria.md) — **8 incorporadas, 1 con reserva, 3 descartes** | ✅ **excede el mínimo** |
| 4 | **Mapa de organismos chilenos** con competencias, constitución y estado operacional | [Entregable 4](Entregables/Entregable_4_Mapa_Organismos_Zonas_Grises.md) — **13 organismos + 7 zonas grises** | ✅ |
| 5 | Contribución a la **columna nacional** del cuadro comparativo | [Entregable 5](Entregables/Entregable_5_Cuadro_Comparativo_Columna_Nacional.md) — **30 criterios** | ✅ |
| 6 | **Declaración de exhaustividad negativa** con bitácora de búsqueda | [Entregable 6](Entregables/Entregable_6_Declaracion_Exhaustividad_Bitacora.md) | ✅ |

---

## 2. Método de Investigación: el Sistema de Tres Niveles de Certeza

> [!IMPORTANT]
> **Esta es la decisión metodológica central del trabajo de Persona 2 y el principal mecanismo de defensa frente al Comunicado 9.** En lugar de presentar un texto uniformemente afirmativo, **cada afirmación del corpus declara el nivel de evidencia que la sostiene**. El resultado es un documento en el que **es imposible confundir un dato verificado con una inferencia**.

| Marca | Significado | Fuentes admitidas |
| :---: | :--- | :--- |
| **[V]** | Verificado contra **fuente primaria** | Diario Oficial (PDF), ficha oficial de tramitación del Senado, repositorio normativo de la ANCI, Ley de Presupuestos de DIPRES, o PDF que reproduce el articulado oficial. |
| **[S]** | Apoyado en **fuente secundaria** | BCN, estudios jurídicos de primer nivel (Carey, Garrigues, Ontier), compilaciones especializadas (DLA Piper, IAPP, Future of Privacy Forum), analistas sectoriales. |
| **[NV]** | **No verificado** | Se consigna expresamente como tal. **No se cita con número de artículo.** |
| `[CG]` | Conocimiento general | Solo en la columna de contexto RGPD/NIS2 del Entregable 5. **Pendiente de verificación por P3.** |

**Reglas de aplicación:**

1. **Nunca elevar el nivel de certeza de una afirmación** por conveniencia narrativa.
2. Cuando dos fuentes discrepan, **se consigna la discrepancia y se declara si fue resuelta o no**. El corpus documenta **12 discrepancias**, de las cuales **4 quedaron resueltas** y **8 permanecen abiertas**.
3. Las afirmaciones negativas se redactan siempre como **«no se encontró evidencia de…»**, nunca como **«no existe…»**.
4. Cuando una fuente comercial contradice el texto legal, **se cita para refutarla**, no para sostener la afirmación (casos del plazo de 72 horas y de la postergación «ya consumada»).

---

## 3. Limitación Técnica Determinante y Ruta de Desbloqueo

> [!CAUTION]
> **El portal oficial Ley Chile (BCN) resultó no recuperable en esta investigación.** Sirve su articulado mediante JavaScript y devolvió reiteradamente «Este proceso demora demasiado»; el *endpoint* `leychile.cl/Consulta/obtxml` **entregó normas distintas de las solicitadas** (devolvió el Decreto N° 419 de 2024 para dos `idNorma` diferentes) y el exportador PDF fue rechazado por el proxy. **Esta limitación explica por qué una parte sustancial del articulado figura como [S] y no como [V].**

**Ruta de desbloqueo que sí funcionó:**

```
  PATRÓN VERIFICADO DE ACCESO AL DIARIO OFICIAL
  ─────────────────────────────────────────────────────────────────────
  diariooficial.interior.gob.cl/publicaciones/AAAA/MM/DD/{edición}/01/{id}.pdf

  Ley N° 21.719 → /2024/12/13/44023/01/2583630.pdf   (trunca en pág. 20 de 34)
  Ley N° 21.663 → /2024/04/08/43820/01/2475674.pdf
  Res. Ex. 87   → /2025/12/17/44326-B/01/2743431.pdf
  Normas técn.  → /2023/08/17/43629/01/2361371.pdf
  D. 276/2024   → /2025/02/12/44073/01/2608697.pdf
  ─────────────────────────────────────────────────────────────────────
  COMPLEMENTOS: tramitacion.senado.cl · obtienearchivo.bcn.cl · anci.gob.cl
```

**Identificadores oficiales fijados** (para quien retome la verificación con navegador):

| Norma | `idNorma` | Norma | `idNorma` |
| :--- | :---: | :--- | :---: |
| Ley N° 21.719 | **1209272** | Ley N° 21.658 | 1200907 |
| Ley N° 21.663 | **1202434** | Ley N° 21.659 | 1202067 |
| Ley N° 21.729 | 1211063 | Ley N° 18.168 | 29591 |
| Ley N° 21.730 | 1210815 | Decreto N° 83/2017 (Budapest) | 1106936 |
| Ley N° 21.180 | 1138479 | Circular Bancos N° 2.261 | 1150515 |
| Ley N° 21.096 | 1119730 | Ley N° 21.459 | 1177743 |

---

## 4. Convenciones de Estilo Aplicadas (Casa AudIT)

| Elemento | Convención | Ejemplo |
| :--- | :--- | :--- |
| **Referencia a ley** | `Ley N° 21.719` en toda cita formal | *no* «Ley 21719», *no* «Ley N.º 21.719» |
| **Artículo en prosa** | Desarrollado y capitalizado | «El **Artículo 13** contiene cinco letras» |
| **Artículo en tabla, paréntesis o cita** | Abreviado | «(Art. 13)», «Arts. 27-29» |
| **Ordinales latinos** | Minúscula, sin cursiva | `bis`, `ter`, `quáter`, `quinquies`, `sexies` |
| **Decretos supremos** | `D.S. N° 295/2024` | *no* «D. 295/2024» |
| **Citas textuales de norma** | Comillas latinas | «sin dilaciones indebidas» |
| **Fechas en prosa** | Formato largo | «20 de septiembre de 2026» |
| **Fechas en tabla y bitácora** | `DD-MM-AAAA` | `20-09-2026` |
| **Miles y decimales** | Punto y coma | `1.154 OIV`, `46,6 %` |
| **Porcentajes** | Espacio antes del signo | `46,6 %` |
| **Moneda** | Declarando siempre la paridad | `20.000 UTM (≈ $1.390 M con 1 UTM = $69.542)` |
| **Siglas invariables** | Sin `-s` en plural | `1.154 OIV`, *no* «OIVs» |
| **Reglamento europeo** | `RGPD` | *no* «GDPR» |

---

## 5. Protocolo de Trabajo Diario

1. **Antes de escribir:** localizar la fuente primaria. Si no se obtiene, escribir igual **pero marcando [S] o [NV]**. Nunca esperar a la fuente perfecta, nunca fingir tenerla.
2. **Al citar un artículo:** verificar que el numeral aparece en al menos una fuente que reproduzca articulado. Si dos fuentes discrepan en el numeral, **no citar el número**.
3. **Al encontrar una discrepancia:** registrarla en el listado del Entregable 6, §2, con su estado (resuelta / no resuelta) y el criterio de preferencia aplicado.
4. **Al cerrar el día:** actualizar el listado de vacíos priorizados y comunicar a P8 cualquier vacío que afecte a otro capítulo.
5. **Al detectar una contradicción con otro capítulo:** documentarla en [Directrices_Vigencia_Normativa_P1_P3_P4_P5.md](Directrices_Vigencia_Normativa_P1_P3_P4_P5.md), §3, con ubicación exacta (archivo y línea), evidencia y corrección propuesta.

---

## 6. Checklist Anti-Comunicado 9 para el Corpus de Persona 2

| Indicio del Comunicado 9 | Cumplimiento en la carpeta Persona 2 | Evidencia |
| :--- | :---: | :--- |
| **(a) Cero figuras huérfanas** |  | Los 4 esquemas del corpus (mapa ministerial, dependencia circular, embudo de calificación de OIV, tres políticas digitales) tienen **descripción integral inmediatamente posterior** que los cita, los recorre y deriva conclusiones. |
| **(b) Cifras rastreables** |  | Toda cifra tiene fuente y fecha. Los **cuatro cálculos derivados** están mostrados: 72 días (20-09 → 01-12-2026); 46,6 % (1.712→915); 77 días = 11 semanas (24-12-2024 → 11-03-2025); 60 días corridos (17-12-2025 → 15-02-2026 y 24-07-2026 → 22-09-2026). |
| **(c) Coherencia entre capítulos** |  **8 discrepancias detectadas y documentadas** | [Directrices](Directrices_Vigencia_Normativa_P1_P3_P4_P5.md), §3. **DC-01 y DC-02 son críticas y requieren corrección por P4 y P5 antes del despacho.** |
| **(d) Cero marcadores residuales de IA** |  | Sin `[cite: n]`, `[INSERTAR…]`, `Anexo ??`, «pendiente de validar» ni «Fuente: elaboración propia» sin análisis. Los **[NV]** son marcas metodológicas declaradas y explicadas, no marcadores residuales. |
| **(e) Sin ruptura de ficción** |  | Sin menciones a «curso», «docente» o «tarea» en el cuerpo analítico. Las referencias a la ficha TI-12 y al Plan Operativo se confinan al Manual Operativo y a los encabezados de estado. |

---

## 7. Declaración de Uso de IA (Insumo para el Formulario A-6)

> [!IMPORTANT]
> **Nivel declarado para el conjunto del trabajo de Persona 2: NIVEL 2.**
>
> **Descripción del uso real.** Se emplearon herramientas de IA como **apoyo a la búsqueda y localización de información normativa** —identificar qué fuentes consultar, rastrear rutas de acceso a textos oficiales y sintetizar cuerpos legales extensos para orientar la lectura—. **El contenido sustantivo está escrito desde la base de investigación propia del integrante**: la selección de normas, la verificación contra fuente, la asignación de los niveles de certeza, la interpretación jurídica, los criterios de descarte y las conclusiones son elaboración humana. **Posteriormente el corpus fue sometido a una revisión de ortografía, estilo y consistencia terminológica** sobre texto ya redactado y verificado.

### 7.1 Nivel por sección

Conforme al punto 6.1 de las indicaciones y a la exigencia del A-6 de declarar **nivel por sección y no un nivel global único**:

| Sección del corpus | Nivel | Uso concreto declarado |
| :--- | :---: | :--- |
| **Búsqueda y localización de fuentes normativas** (Entregables 1-4) | **Nivel 2** | Apoyo para identificar qué fuentes consultar y rastrear rutas de acceso a textos oficiales, ante el bloqueo del portal Ley Chile (§3). |
| **Síntesis inicial de cuerpos legales extensos** | **Nivel 2** | Lectura orientada de la Ley N° 21.719 y la Ley N° 21.663 para estructurar el esquema de análisis. |
| **Verificación contra fuente y asignación de marcas [V] / [S] / [NV]** | **Nivel 0** | Juicio humano sobre qué sostiene cada afirmación. Es la decisión metodológica central del trabajo. |
| **Interpretación jurídica** (bases de licitud, régimen del encargado, alcance del Art. 14 sexies) | **Nivel 0** | Restricción mandatoria del punto 6.1. |
| **Análisis comparativo y ponderación de criterios** (Entregable 5) | **Nivel 0** | Restricción mandatoria del punto 6.1. |
| **Criterios de inclusión y descarte de normativas** (Entregable 3) | **Nivel 0** | Criterio de selección propio: cada norma entra por el eje diferenciador que solo ella aporta. |
| **Declaración de exhaustividad y niveles de confianza** (Entregable 6) | **Nivel 0** | Juicio metodológico propio sobre el alcance y los límites del barrido. |
| **Revisión ortotipográfica, unificación de estilo y consistencia terminológica** | **Nivel 1** | Revisión de forma sobre texto ya redactado y verificado: unificación de `Ley N° 21.719`, `Art.` / `Artículo`, `RGPD`, comillas latinas y formato de decretos. |

### 7.2 Evidencia trazable a adjuntar al A-6

- **Exportación de los chats** empleados para la búsqueda de fuentes y la síntesis inicial de los cuerpos legales.
- **Enlace directo a cada norma en su fuente primaria**, con el patrón del Diario Oficial documentado en §3 y los identificadores `idNorma` fijados.
- **Bitácora de búsqueda consolidada** (Entregable 6, §2): ~90 consultas, rutas que funcionaron, rutas que fallaron con su código de error e identificadores obtenidos.

> [!IMPORTANT]
> **La bitácora de búsqueda es, por sí sola, evidencia de trabajo humano de investigación.** Documenta fracasos técnicos concretos (HTTP 403 en `csirt.gob.cl` y `digital.gob.cl`, redirecciones infinitas en `anci.gob.cl/comite-interministerial/`, `ROBOTS_DISALLOWED` en `ontier.law`, bucle 302 en `dipres.cl`) que **ninguna generación automática produciría**, porque describen el proceso real de obtención y no su resultado idealizado.

### 7.3 Coherencia entre el nivel declarado y el texto observable

Persona 8 debe verificar que el nivel declarado sea coherente con lo observado en el corpus. Los siguientes rasgos del texto **sostienen la declaración de Nivel 2 con contenido de base propia**:

1. **El sistema de tres niveles de certeza** ([V] / [S] / [NV]) aplicado afirmación por afirmación, incluidas **12 discrepancias de fuentes** con su estado de resolución declarado.
2. **Las refutaciones explícitas a fuentes comerciales** —el plazo de 72 horas del Art. 14 sexies y la postergación dada por consumada—, que requieren contraste deliberado entre fuente y texto legal.
3. **Las correcciones a la literatura especializada**: los criterios de OIV están en el Art. 5 y no en el Art. 6; la Ley N° 21.719 no deroga la Ley N° 19.628.
4. **Los cuatro cálculos derivados mostrados** (72 días, 46,6 %, 77 días = 11 semanas, 60 días corridos de exigibilidad).
5. **La declaración de exhaustividad negativa**, que asume y documenta los límites del propio trabajo en lugar de presentarlo como completo.
