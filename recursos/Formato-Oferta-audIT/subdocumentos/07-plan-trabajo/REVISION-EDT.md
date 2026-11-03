# Revisión de la EDT · 02-11-2026

Estado actualizado: preparación para propuesta final, versión 3.0, 25-11-2026. Ignacio Cuevas confirmó la revisión de EDT v2 y Gantt v3; el registro nominal está en REGISTRO-PARA-A6.md. Los cierres actuales se detallan en PENDIENTES-ENTREGA-FINAL.md. Las notas siguientes conservan el historial de revisión y no sustituyen ese estado.

## Fuentes y decisiones

- Se conservaron los 13 elementos y 54 códigos del diccionario T-14. El árbol explicita raíz, elementos y descomposición; la ubicación de los nodos no indica precedencias.
- Cinco láminas muestran una vez cada paquete. T-14 conserva la ficha completa de entregable, aceptación, rol, red y meses.
- La ficha 11.2 reproduce los campos del T-14. Los nombres visibles 11.2 y 11.3 aclaran que incluyen marcha blanca y paso a producción; 5.7 permanece como portal adicional a los seis contextos 5.1–5.6.
- La matriz de requisitos toma los 42 códigos de T-12 y las asociaciones del `plan_detallado.json` de D2; todos aparecen al menos una vez. Esta correspondencia por código no verifica por sí sola la suficiencia de cada entregable ni de las pruebas T-17.
- Se corrigió la afirmación de cobertura total sin evidencia individual en la tabla del cuerpo. Falta cotejar con detalle las once exigencias del numeral 17.5 y los criterios genéricos de aceptación, en especial las innovaciones, antes de una versión final de T-14.
- Los 23 PDF anteriores se conservaron en `version-anterior/2026-11-02/edt/`.

## Comprobaciones

- Generador reproducible: `graficos/generar_edt_revisada.py`.
- Salida autónoma: `graficos/edt-revisada/EDT_Completa_Revisada.pdf` (9 páginas).
- Informe integrado: `S7_Integrado_Revision.pdf`, 46 páginas, EDT en folios 23–31 y Gantt en 32–43; referencias resueltas, sin `??`.
- Inspección visual de árbol, ficha y matriz en el PDF integrado. Texto de los nodos y matriz medido a 9,99 pt efectivos, sobre el mínimo de 9 pt.
- Los cambios sustantivos y la declaración de uso de IA requieren revisión humana y vínculo con la bitácora A-6 del responsable antes de entrega.
