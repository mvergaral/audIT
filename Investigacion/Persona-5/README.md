# Persona 5: Arquitectura de Cumplimiento Técnico-Legal y Vinculación con el Caso Curimón S.A.
**Licitación TFEP-01/2026 · Caso 10: Transportes Curimón S.A. · Empresa Consultora audIT**  
**Tema de Investigación:** TI-12 (Cumplimiento Normativo en Proyectos TIC)  
**Responsable:** Martín (*Compliance Architecture Designer & Case Integrator*)  

---

## 1. Documento Consolidado Principal (Capítulo 3.1)
* **[Subdocumento_Persona_5_Consolidado.md](Subdocumento_Persona_5_Consolidado.md)**: Texto maestro consolidado en Markdown listo para integración en el informe final, calibrado a ~2,5 páginas útiles (~1.400 palabras) con estructura editorial, trazabilidad normativa y diagramas de flujo.

---

## 2. Entregables de Soporte Técnico (`Entregables/`)
Los cuatro análisis de arquitectura, privacidad y gobernanza que sustentan el subdocumento consolidado:
1. **[Entregable 1: Arquitectura de Cumplimiento Técnico-Legal](Entregables/Entregable_1_Arquitectura_Cumplimiento.md)**: Mapa de flujos de datos personales, distinción taxativa Responsable (Curimón) vs. Encargado (audIT / Azure), cifrado a nivel de campo FLE (RT-11.10) y canales perentorios de notificación al CSIRT Nacional ($\le 3\text{ h}$), APDP y Mandante.
2. **[Entregable 2: Privacidad y Seguridad desde el Diseño y por Defecto](Entregables/Entregable_2_Privacy_by_Design_Ciclo_Vida.md)**: Inserción de controles en las 3 etapas del proyecto (56 meses), gobernanza del RAT (Art. 14 ter), Evaluación de Impacto (EIPD / DPIA Art. 15 ter) sobre 374 camiones GPS, consentimiento móvil para 258 choferes externos y supervisión humana de despachos bloqueados (Art. 8 bis).
3. **[Entregable 3: Transferencias Internacionales y Selección de Región Cloud](Entregables/Entregable_3_Transferencias_Internacionales.md)**: Análisis de flujos transfronterizos bajo los Arts. 27 y 28 de la Ley 21.719: justificación de Azure Chile Central como primaria, réplica pasiva en Azure East US 2 con Cláusulas Contractuales Tipo (SCC), y tránsito terrestre a Mendoza (~1.900 cruces anuales) bajo la Ley N.º 25.326 argentina.
4. **[Entregable 4: Vínculo Contractual con la Propuesta Técnico-Económica](Entregables/Entregable_4_Vinculo_Propuesta_Tecnico_Econ.md)**: Cumplimiento del mandato de la Ficha TI-12: mapeo formal de obligaciones con la EDT (EDT 1.3, 2.4, 3.4, 4.2, 7.2), hitos en la Carta Gantt (Meses 4, 6, 12, 16, 20), calce biunívoco con perfiles E-26 y respaldo de criterios de aceptación del Caso 10.

---

## 3. Guías Operativas y Declaración Oficial A-6
* **[Bitacora_A6_Persona_5_Declaracion_Oficial.md](Bitacora_A6_Persona_5_Declaracion_Oficial.md)**: Formulario oficial A-6 de declaración de uso de IA bajo Nivel 3 oficial, amparado en las Secciones 6.1 a 6.4 de las Indicaciones del Curso.
* **[Bitacora_IA_A6_Persona_5.md](Bitacora_IA_A6_Persona_5.md)**: Registro exhaustivo de interacciones con IA, transcripción de prompts y control humano crítico.
* **[Directrices_Validacion_Cruzada_P4.md](Directrices_Validacion_Cruzada_P4.md)**: Acta de verificación de calce biunívoco 1:1 entre los componentes de arquitectura diseñados por Persona 5 y el presupuesto TCO de Persona 4. Cero componentes huérfanos y cero gastos no justificados.

---

## 4. Checklist de Blindaje Anti-Comunicado 9

| Criterio del Comunicado 9 | Cumplimiento en Carpeta Persona 5 | Evidencia Verificada |
| :--- | :---: | :--- |
| **Indicio a: Cero diagramas huérfanos** | ✅ **100% Cumplido** | Todo diagrama cuenta con descripción paso a paso, cita y análisis en el texto. |
| **Indicio b: Cifras derivadas del Caso** | ✅ **100% Cumplido** | Solo se usan las cifras oficiales: 374 camiones, 454 choferes (196/258), 148 pymes, ~1.900 viajes Mendoza. |
| **Indicio c: Coherencia entre capítulos** | ✅ **100% Cumplido** | 100% alineado con Microsoft Azure Chile Central, cifrado FLE RT-11.10 y TCO de Persona 4. |
| **Indicio d: Cero marcadores de IA** | ✅ **100% Cumplido** | No existen marcadores `[INSERTAR...]`, leyendas de `Fuente propia` huérfanas ni jerga académica ajena. |
