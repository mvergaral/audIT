# Control de Pendientes y Correcciones por Integrante
## TI-12 · Cumplimiento Normativo en Proyectos TIC · audIT (Empresa N.º 10)
**Caso:** Transportes Curimón S.A. | **Actualizado:** 21-09-2026 (post-pull)

---

## Estado del Equipo

| Persona | Integrante | Repo | Estado |
| :--- | :--- | :--- | :--- |
| Persona 1 | Ignacio C. | `Persona-1/` | Estructura lista; secciones humanas en blanco |
| Persona 2 | Alonso | `Persona-2/` | Subido (12 archivos, Nivel 2). Columna `[CG]` requiere verificación de P3 |
| Persona 3 | Ignacio V. | `Persona-3/` | Subido (17 archivos). Corrección de fecha ya aplicada |
| Persona 4 | Carlos | `Persona-4/` | Definitivo. A-6 declarado (Nivel 0/1). Algunas cifras internas difieren entre archivos |
| Persona 5 | Martín | `Persona-5/` | Completo y sin pendientes técnicos |
| Persona 6 | Marcel | Sin carpeta | Pendiente crítico: 0% de avance, 100% humano obligatorio |
| Persona 7 | Naomi | Sin carpeta | Pendiente: habilitada para iniciar PPT |
| Persona 8 | Matías | Sin carpeta | Pendiente: habilitado para iniciar fact-checking y A-6 |

---

## Regla de autoría humana obligatoria (Sección 6.1 de las Indicaciones)

Solo estas secciones prohíben el uso de IA (Nivel 0 estricto):

1. Análisis comparativo y justificación de criterios — **P2 y P3**
2. Conclusiones y recomendaciones — **P1**
3. Párrafo de aporte propio y discusión crítica — **P1**
4. Cuestionario completo (preguntas, alternativas, respuestas, justificaciones) — **P6**
5. Cifras, fórmulas y verificación de vigencia en fuentes primarias — **P4 y P8**

---

## Persona 1 — Ignacio C.

**Rol:** Líder Editorial, Introducción, Conclusiones y Coherencia Global.  
**Estado:** Carpeta lista con 10 archivos. Los textos consolidados de P2, P3, P4 y P5 ya están en el repositorio.

**Redacción 100% humana obligatoria (sin IA):**
- [ ] Resumen Ejecutivo (máx. 0,5 págs.): sintetizar el problema, el marco legal, el TCO y la solución.
- [ ] Párrafo de Aporte Propio en la Introducción: usar los insumos del borrador Q&A (conectividad por capas, trazabilidad integral, diagnóstico de descontrol de flota).
- [ ] Conclusiones y Recomendaciones: sintetizar hallazgos de P2 a P5.
- [ ] 5 respuestas personales de defensa oral en `Guia_Auditoria_Humana_Defensa_Oral_Persona_1.md`.

**Correcciones:**
- [ ] Al ensamblar el capítulo económico, usar únicamente `Subdocumento_Persona_4_Consolidado_Definitivo.md`. El archivo antiguo tiene cifras previas a la corrección E-24.
- [ ] Verificar que no queden residuos de la sesión inicial donde se asumió que el trabajo no aplicaba a Curimón S.A.

**Tareas:**
- [ ] Reemplazar los bloques `> **COMPLETAR A MANO.**` del subdocumento consolidado.
- [ ] Ensamblar los capítulos de los 8 integrantes en el documento maestro (10 a 15 páginas útiles).
- [ ] Exportar con nomenclatura oficial: `10 - AUDIT - TI-12.pdf`.

---

## Persona 2 — Alonso

**Rol:** Marco Legal Chileno (Ley 21.719, Ley 21.663 y normativa complementaria).  
**Estado:** Subido con 12 archivos (subdocumento consolidado, 6 entregables, guía de defensa, manual, README y Prompts.txt). Nivel 2 declarado: Alonso escribió el contenido desde sus notas propias; la IA corrigió ortografía y consistencia. Hay puntos concretos sin cerrar.

**Pendientes de resolución (con o sin ayuda de P3/P8):**

- [ ] **Columna `[CG]` en el Entregable 5 (Cuadro Comparativo):** 29 celdas de la columna europeo/internacional tienen la marca `[CG]` (conocimiento general, pendiente de verificación por P3). Alonso y P3 deben cruzar esa columna y reemplazar `[CG]` por `[V]` o `[S]` según lo que Ignacio V. pueda confirmar con sus fuentes.
- [ ] **Vacíos declarados `[NV]` que P8 debe cerrar:** El Entregable 1 sección §7.2 lista verificaciones específicas no confirmadas, etiquetadas como `[NV]`, que corresponden al fact-checking de Matías (P8). Alonso ya los declaró; P8 los debe resolver.
- [ ] **Estado del Convenio 108+ (CETS 223):** El Entregable 6 señala explícitamente que no se pudo verificar si Chile firmó o no el Convenio 108+. Debe consultarse el Treaty Office del Consejo de Europa y corregir el texto a "no consta que Chile haya adherido" o con la cifra exacta.
- [ ] **Fechas de publicación en Diario Oficial pendientes de confirmación primaria:** El Entregable 6 lista 9 leyes con fechas no verificadas en fuente primaria (Leyes 19.628, 20.285, 21.096, 21.459, 21.521, 21.680, 21.659, Instructivo N.º 8 y Reglamento de Ciberseguridad de la Defensa). P8 debe confirmarlas.
- [ ] **ZG-3: CMF vs ANCI:** El Entregable 4 señala que el principio de equivalencia del Art. 37 de la Ley 21.663 está "pendiente de declaración formal" y no hay convenio publicado. Monitorear si antes de la entrega se publica algo; si no, dejar como `[NV]` declarado.

**Verificación anti-Comunicado 9:**
- Entregable 4 incluye un mapa de organismos con diagramas ASCII. Cumple el requisito de no entregar texto puro (Indicio a).
- Entregable 5 incluye tabla de 30 criterios. Correcto.

**No hay correcciones estructurales que hacer.** El capítulo está bien construido. Los pendientes son de verificación puntual en fuentes primarias, no de redacción nueva.

---

## Persona 3 — Ignacio V.

**Rol:** Marco Internacional, Directivas UE, Normas ISO/NIST y Herramientas GRC.  
**Estado:** Subido con 17 archivos. Corrección de errata de fecha (`[20-10-2026]` → `[20-09-2026]`) ya aplicada en el commit `05de556`.

**Pendientes:**
- [ ] **Cerrar la columna `[CG]` del Entregable 5 de Alonso (P2):** Las 29 celdas europeas/internacionales del cuadro comparativo llevan la marca `[CG]` porque P2 las completó de memoria como referencia. P3 debe revisar cada una contra sus fuentes y marcarlas `[V]` o `[S]`.
- [ ] **Justificación final de la herramienta GRC recomendada (Nivel 0):** La matriz de puntuación ya está (Microsoft Purview: 3,70). La defensa del criterio de ponderación (por qué 25% a transparencia del precio y 20% a encaje Azure) debe poder explicarse oralmente sin leer.
- [ ] **Complementariedad Purview vs CISO Assistant Pro:** P3 evaluó Microsoft Purview como primera opción GRC; P4 presupuestó CISO Assistant Pro. Antes de que P1 ensamble, los tres deben acordar si esto se presenta como opciones secuenciales, complementarias o alternativas. Dejar constancia por escrito en algún archivo del repo.

---

## Persona 4 — Carlos

**Rol:** Modelado Económico del Cumplimiento, Matriz de Obligaciones, TCO y Sensibilidad.  
**Estado:** Definitivo. Subió además dos archivos de declaración A-6 (`Bitacora_A6_Persona_4_Declaracion_Oficial.md` y `Bitacora_IA_A6_Persona_4.md`) con declaración Nivel 0 en cálculos y Nivel 1 en formato y ortografía.

**Inconsistencia interna que P4 o P8 deben resolver:**
- [ ] El subdocumento definitivo menciona $\text{VAN}_{\text{costo}} = \mathbf{6.582,3\text{ UF}}$ en el cuerpo del texto, pero la declaración A-6 indica $6.537,13\text{ UF}$ como VAN. Son dos cifras distintas para la misma variable. Carlos debe identificar cuál es la correcta, corregir el archivo donde está el error y notificar a P1 para que use el número definitivo al ensamblar.

**Correcciones ya aplicadas (no requieren acción):**
- [x] Paridades E-24: 1 UF = \$40.000 CLP, 1 USD = \$900 CLP, tasa de descuento 0,9% mensual.
- [x] Plataforma en Azure Chile Central con Key Vault Premium (686 claves RSA individuales).
- [x] GRC: CISO Assistant Pro ($255\text{ UF}$), auditoría inicial ISO 27001 ($387,5\text{ UF}$), seguro Chubb ($90\text{ UF/año}$).
- [x] TCO total definitivo: **$8.375,4\text{ UF}$** netas (\$335,0M CLP / USD 372.240).
- [x] Declaración A-6 completa con herramienta y versión.

---

## Persona 5 — Martín

**Rol:** Arquitecto de Cumplimiento Técnico-Legal y Vinculación con el Caso 10.  
**Estado:** Completo. Subió los 7 archivos técnicos más la declaración A-6 completa (`Bitacora_IA_A6_Persona_5.md` y `Bitacora_A6_Persona_5_Declaracion_Oficial.md`) con **Nivel 3 declarado transparentemente** y registro de 13 interacciones reales. Sin pendientes técnicos.

**Dominio obligatorio para defensa oral (Nivel 0 en juicio técnico):**
- [ ] Distinción jurídica Responsable (Curimón) vs Encargado (audIT / Azure) bajo Art. 15 bis.
- [ ] Justificación del consentimiento para los 258 choferes externos vs relación laboral de los 196 propios.
- [ ] Plazos de notificación al CSIRT Nacional ($\le 3\text{ h}$, 72 h, 15 d) bajo Ley 21.663.
- [ ] Legalidad de la réplica en Azure East US 2 mediante Cláusulas Contractuales Tipo (SCC).
- [ ] Justificación técnica de no instalar hardware HSM físico en la sala de 26 m² de San Bernardo.

**Tarea al cierre:**
- [ ] Revisar el documento maestro ensamblado por P1 para verificar que los diagramas Mermaid mantienen la diagramación correcta en el formato de exportación final.

---

## Persona 6 — Marcel

**Rol:** Diseñador del Cuestionario de Evaluación (30 preguntas).  
**Estado:** Sin carpeta ni archivos. Es el único entregable con 0% de avance y exigencia de autoría 100% humana.

**Regla:** La Sección 6.1 prohíbe usar IA para redactar preguntas, alternativas, respuestas o justificaciones. Todo el cuestionario debe ser de autoría humana verificable.

**Requisitos obligatorios:**
- [ ] Crear carpeta `Investigacion/Persona-6/`.
- [ ] Redactar **30 preguntas originales** con distribución exacta:
  - 12 básicas (40%): definiciones, organismos, plazos de la normativa.
  - 12 intermedias (40%): aplicación al caso Curimón, comparación entre normas, consecuencias prácticas.
  - 6 avanzadas (20%): análisis crítico, trade-offs de arquitectura, conflictos normativos.
- [ ] Formatos mixtos: selección múltiple (4 alternativas), verdadero/falso con justificación, completar términos técnicos y desarrollo breve.
- [ ] Clave de respuestas: respuesta correcta + justificación técnica de por qué se descartan las erróneas.
- [ ] Índice temático cruzado: tabla que vincule cada pregunta con su capítulo del informe y su subtema TI-12.
- [ ] Cobertura mínima: al menos 1 pregunta por cada subtema de la ficha.

---

## Persona 7 — Naomi

**Rol:** Presentación Ejecutiva y Preparación de Defensa Oral.  
**Estado:** Sin carpeta. Con los capítulos de P2, P3, P4 y P5 ya disponibles, puede iniciar.

**Redacción 100% humana obligatoria:**
- [ ] Libreto de defensa oral: distribución de tiempo por integrante (~3 min por persona, 24 min totales) y puntos de transición.
- [ ] Matriz de al menos 15 preguntas difíciles anticipadas, con la respuesta asignada al integrante que corresponde.
- [ ] Coordinar y dirigir el ensayo general cronometrado del grupo.

**Regla de coherencia numérica (crítica):** Toda cifra en las diapositivas debe coincidir exactamente con el TCO definitivo de P4 ($8.375,4\text{ UF}$, paridades E-24) y la volumetría del Caso 10. Cero contradicciones PPT vs informe.

**Tareas:**
- [ ] Crear carpeta `Investigacion/Persona-7/`.
- [ ] Diseñar mazo de 12 a 15 diapositivas ejecutivas (PowerPoint o PDF exportado).
- [ ] Documento de libreto y matriz de preguntas difíciles.

---

## Persona 8 — Matías

**Rol:** Auditor de Calidad, Fact-Checking de Fuentes y Custodio del Formulario A-6.  
**Estado:** Sin carpeta. Puede iniciar de inmediato con las fuentes que P2 y P3 ya identificaron.

**Todo el trabajo de Matías es Nivel 0 estricto (sin IA).**

**Verificaciones urgentes que P2 dejó pendientes para P8:**
- [ ] Confirmar fechas de publicación en el Diario Oficial de las 9 leyes marcadas `[NV]` en el Entregable 6 de P2 (Leyes 19.628, 20.285, 21.096, 21.459, 21.521, 21.680, 21.659, Instructivo N.º 8 y Reglamento de Ciberseguridad de la Defensa).
- [ ] Verificar el estado de Chile ante el Convenio 108+ en el Treaty Office del Consejo de Europa.
- [ ] Cerrar los `[NV]` del Entregable 1 de P2, Sección §7.2.
- [ ] Fiscalizar que P2, P3 y P4 no tengan capítulos sin figuras o tablas integradas en el texto (Comunicado 9, Indicio a).
- [ ] Resolver la inconsistencia de VAN en P4: $6.582,3\text{ UF}$ vs $6.537,13\text{ UF}$. La cifra correcta debe quedar en todos los archivos.

**Formulario A-6:**
- [ ] Crear carpeta `Investigacion/Persona-8/`.
- [ ] Consolidar las 8 declaraciones individuales con herramienta **y versión exacta** (ej. "Claude 3.5 Sonnet", no solo "IA"). P4 ya entregó su declaración completa.
- [ ] Recopilar evidencia de prompts para quienes declaren Nivel 2 o superior.
- [ ] Verificar límites formales del informe final: 10 a 15 páginas útiles, nomenclatura `10 - AUDIT - TI-12.pdf` y asunto del correo institucional.

---

## Prioridades de cierre

1. **Marcel (P6):** Iniciar el cuestionario de inmediato. Es el único entregable con 0% de avance y trabajo 100% manual.
2. **Alonso (P2) + Ignacio V. (P3):** Coordinar y cerrar la columna `[CG]` del cuadro comparativo.
3. **Carlos (P4):** Resolver la discrepancia del VAN ($6.582,3$ vs $6.537,13\text{ UF}$) y notificar a P1.
4. **Ignacio C. (P1):** Con los capítulos de P2 a P5 disponibles, puede redactar el Aporte Propio, Resumen Ejecutivo y Conclusiones, e iniciar el ensamblaje del documento maestro.
5. **Naomi (P7) y Matías (P8):** Iniciar en paralelo la presentación y el fact-checking/A-6.
