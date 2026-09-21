# Declaración Oficial de Uso de Inteligencia Artificial (Formulario A-6)
## Persona 2: Marco Legal Chileno — Ley 21.719, Ley 21.663 y normativa complementaria

**Asignatura:** Taller de Formulación de Proyectos Informáticos (ICI-5444) · Escuela de Informática, PUCV
**Empresa Asignada:** AudIT (Empresa N.º 10)
**Tema de Investigación:** TI-12 · *Cumplimiento normativo en proyectos TIC*
**Caso de Aplicación:** Caso 10 — *Transportes Curimón S.A.*
**Responsable:** Alonso (Persona 2)
**Marco Normativo:** Bases Administrativas FEP01.26 (Art. 13.5 y Formulario A-6), Indicaciones FEP00.3.26 (Secciones 6.1 a 6.4) y Comunicado 9.
**Fecha de Emisión:** 21 de septiembre de 2026

> **Nota de procedencia.** El contenido de esta declaración fue redactado por Persona 2 y
> se encontraba en la Sección 7 de su `Manual_Operativo_Persona_2.md`. Persona 8, en su
> calidad de custodio del Formulario A-6, lo trasladó al formato del anexo sin alterar
> niveles, alcances ni redacción sustantiva. Los prompts del §4 se transcriben literalmente
> desde `Prompts.txt`.

---

## 1. Nivel declarado y descripción del uso real

**Nivel declarado para el conjunto del trabajo de Persona 2: Nivel 2.**

Se emplearon herramientas de IA como **apoyo a la búsqueda y localización de información
normativa** —identificar qué fuentes consultar, rastrear rutas de acceso a textos oficiales
y sintetizar cuerpos legales extensos para orientar la lectura—. **El contenido sustantivo
está escrito desde la base de investigación propia del integrante**: la selección de normas,
la verificación contra fuente, la asignación de los niveles de certeza, la interpretación
jurídica, los criterios de descarte y las conclusiones son elaboración humana.
Posteriormente el corpus fue sometido a una **revisión de ortografía, estilo y consistencia
terminológica** sobre texto ya redactado y verificado.

---

## 2. Matriz de declaración por sección

> Conforme al §6.3, el nivel se declara **por sección y no como un nivel global único**.

| Sección del corpus | Nivel | Uso concreto declarado |
| :--- | :---: | :--- |
| **Búsqueda y localización de fuentes normativas** (Entregables 1-4) | **2** | Apoyo para identificar qué fuentes consultar y rastrear rutas de acceso a textos oficiales, ante el bloqueo del portal Ley Chile |
| **Síntesis inicial de cuerpos legales extensos** | **2** | Lectura orientada de la Ley N° 21.719 y la Ley N° 21.663 para estructurar el esquema de análisis |
| **Verificación contra fuente y asignación de marcas [V] / [S] / [NV]** | **0** | Juicio humano sobre qué sostiene cada afirmación. Es la decisión metodológica central del trabajo |
| **Interpretación jurídica** (bases de licitud, régimen del encargado, alcance del Art. 14 sexies) | **0** | Restricción mandatoria del §6.1 |
| **Análisis comparativo y ponderación de criterios** (Entregable 5) | **0** | Restricción mandatoria del §6.1 |
| **Criterios de inclusión y descarte de normativas** (Entregable 3) | **0** | Criterio de selección propio: cada norma entra por el eje diferenciador que solo ella aporta |
| **Declaración de exhaustividad y niveles de confianza** (Entregable 6) | **0** | Juicio metodológico propio sobre el alcance y los límites del barrido |
| **Revisión ortotipográfica, unificación de estilo y consistencia terminológica** | **1** | Revisión de forma sobre texto ya redactado y verificado: unificación de `Ley N° 21.719`, `Art.` / `Artículo`, `RGPD`, comillas latinas y formato de decretos |

---

## 3. Herramienta y versión

> [!CAUTION]
> **Campo pendiente de completar por Persona 2.** El §6.3 exige indicar «**las herramientas
> y versiones utilizadas en cada caso**». Ni el `Manual_Operativo_Persona_2.md` ni el
> `Prompts.txt` consignan cuál se usó. El custodio no lo completa porque no le consta.

| Sección | Herramienta y versión exacta |
| :--- | :--- |
| Búsqueda y síntesis de fuentes (Nivel 2) | ____________________ |
| Revisión ortotipográfica (Nivel 1) | ____________________ |

---

## 4. Prompts efectivamente empleados (§6.3, exigible en Nivel 2)

> Transcripción literal de `Prompts.txt`, tal como fue entregado por Persona 2.

```
- quiero que me ayudes a corregir mi parte de un trabajo de investigacion, toda mi
  investigacion esta en @"Persona2/Normativa chilena datos y ciberseguridad.md" y quiero
  que cumpla con lo que se dividio en @Division.md de persona 2, ya tengo toda la
  informacion escrita y revisada por mi parte, pero quiero que arregles ortografia y
  concistencia que exista, trata de dejarlo como @audIT/Investigacion/ en estilo de orden
  y documentos

- puedes editar para que sea nivel 2, con uso de ia para ayuda a la busqueda de informacion
  pero que esta escrito desde mi base y luego fue corregido de ortografia y concistencia

- Le añadi cosas al punto 6 del subdocumento, puedes arreglarlo para que suene mejor? y con
  eso bastaria?
```

El primer prompt acredita el punto central de esta declaración: **la investigación estaba
escrita y revisada por el integrante antes de cualquier intervención de la herramienta**, y
lo solicitado fue corrección de ortografía y consistencia.

---

## 5. Evidencia trazable (§6.3)

- **Exportación de los chats** empleados para la búsqueda de fuentes y la síntesis inicial
  de los cuerpos legales. *(Pendiente de adjuntar por Persona 2.)*
- **Enlace directo a cada norma en su fuente primaria**, con el patrón del Diario Oficial y
  los identificadores `idNorma` fijados en el `Manual_Operativo_Persona_2.md`, §3.
- **Bitácora de búsqueda consolidada** (`Entregable_6_Declaracion_Exhaustividad_Bitacora.md`,
  §2): ~90 consultas, con las rutas que funcionaron y las que fallaron, su código de error e
  identificadores obtenidos.
- **Historial de commits** del repositorio `github.com/mvergaral/audIT`, rama `main`,
  carpeta `Investigacion/Persona-2/`.

> La bitácora de búsqueda es, por sí sola, evidencia de trabajo humano de investigación:
> documenta fracasos técnicos concretos —HTTP 403 en `csirt.gob.cl` y `digital.gob.cl`,
> redirecciones infinitas en `anci.gob.cl/comite-interministerial/`, `ROBOTS_DISALLOWED` en
> `ontier.law`, bucle 302 en `dipres.cl`— que ninguna generación automática produciría,
> porque describen el proceso real de obtención y no su resultado idealizado.

---

## 6. Firma

> Pendiente. La firma de Persona 2 está digitalizada en
> `../Persona-8/firmas/P2_Alonso.png` y se estampa una vez que el titular revise esta
> transcripción y complete el §3.

**Alonso**
Persona 2 — Marco Legal Chileno
AudIT (Empresa N.º 10) · TI-12 · 21 de septiembre de 2026

Firma: ______________________   Fecha: ____________
