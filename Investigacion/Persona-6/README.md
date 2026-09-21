# Persona 6: Diseñador Pedagógico del Cuestionario de Evaluación (30 Preguntas)
**Asignatura:** Taller de Formulación de Proyectos Informáticos (ICI-5444) · Escuela de Informática, PUCV  
**Empresa:** audIT Soluciones de Software SpA (Empresa N.º 10)  
**Tema Asignado:** TI-12 · *Cumplimiento normativo en proyectos TIC: Ley 21.719, Ley 21.663 (ANCI) y marco internacional*  
**Área:** Evaluación, Medición & Gobierno de Cumplimiento  
**Caso de Aplicación:** Caso 10 · Transportes Curimón S.A. (Licitación TFEP-01/2026)  
**Rol Funcional:** Persona 6 · *Assessment & Knowledge Verification Lead* (Marcel)  
**Fecha de Entrega:** 21 de septiembre de 2026  

---

## 1. Misión Operativa y Documento Maestro (Anexo E)

Persona 6 es responsable del diseño pedagógico, formulación técnica y verificación del banco íntegro de **30 preguntas** del Anexo E del informe final, destinadas a certificar la asimilación del marco legal, los estándares técnicos y las decisiones de arquitectura del Caso Curimón.

* **[Subdocumento_Persona_6_Consolidado.tex](Subdocumento_Persona_6_Consolidado.tex):** Bloque tipográfico en LaTeX listo para inserción directa por Persona 1 (Editor Líder) en `content/(7)-anexos.tex` del proyecto `Formato_INF_PUCV__4_`, utilizando las macros nativas `\pregunta` de `informe-ti12.sty`.
* **Uso de IA (Formulario A-6):** **Nivel 0 estricto** (autoría 100% humana, conforme al Punto 6.1 de las Indicaciones; registrado directamente en la planilla consolidada de Persona 8).

---

## 2. Entregables Modulares de Evaluación (`Entregables/`)

El banco de preguntas se estructura en cuatro componentes modulares calibrados bajo la Taxonomía de Bloom:

1. **[Entregable 1: Banco de Preguntas Básicas (12 Preguntas · 40%)](Entregables/P_Basicas.md):** P01 a P12. Evalúa memoria y comprensión de definiciones legales formales, plazos perentorios, sanciones y autoridades (3 Selección, 3 V/F, 3 Completar, 3 Corta).
2. **[Entregable 2: Banco de Preguntas Intermedias (12 Preguntas · 40%)](Entregables/P_Intermedias.md):** P13 a P24. Evalúa aplicación práctica al Caso Curimón (374 camiones, 454 choferes, Dictamen DT 569/2018 sobre GPS, Azure Chile Central sin *paired region*, EIPD y SLAs contractuales).
3. **[Entregable 3: Banco de Preguntas Avanzadas (6 Preguntas · 20%)](Entregables/P_Avanzadas.md):** P25 a P30. Evalúa análisis crítico y compensaciones complejas (US CLOUD Act y BYOK/HYOK, TCO y sensibilidad de roles, borrado criptográfico y modelo Gordon-Loeb $\le 37\%$).
4. **[Entregable 4: Índice Temático y Matriz de Distribución Multidimensional](Entregables/P_Indice_Tematico.md):** Mapeo biunívoco de las 30 preguntas frente a las 14 secciones del informe final y los 6 subtemas obligatorios de la ficha TI-12.

---

## 3. Estado de Cumplimiento Frente a la Planificación General

| Criterio de la Asignatura | Requisito Oficial | Estado Persona 6 | Evidencia Verificable |
| :--- | :---: | :---: | :--- |
| **Total de Preguntas** | 30 preguntas | **30 preguntas** | P01 a P30 en entregables y `.tex` |
| **Distribución Dificultad** | 40% B / 40% I / 20% A | **12 B / 12 I / 6 A** | Matriz en `P_Indice_Tematico.md` |
| **Variedad de Formatos** | 4 formatos equilibrados | **8 Sel, 8 VF, 7 Comp, 7 Corta** | Calibrado según rúbrica |
| **Cobertura Ficha TI-12** | $\ge 1$ por cada subtema (6) | **6 de 6 cubiertos** | Tabla cruzada en `P_Indice_Tematico.md` |
| **Formulario A-6 (IA)** | Nivel 0 obligatorio | **Nivel 0 Declarado** | Fila en Formulario A-6 consolidado (P8) |
| **Integración LaTeX** | Código compilable | **Compilable** | `Subdocumento_Persona_6_Consolidado.tex` |
