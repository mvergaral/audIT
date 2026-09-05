# Matriz consolidada de requisitos del equipo

**Estado:** borrador para verificación cruzada por duplas
**Origen:** catálogo D2 (RF/RNF) + inventario de códigos `RT-xx` citados por D1, D3 y D4

## 1. Cómo leer esta matriz

- **Bloque:** agrupación de trabajo provisional, no significado normativo inferido del capítulo.
- **Códigos citados:** identificadores presentes en el corte del inventario; falta resolver su documento y texto.
- **RF/RNF D2:** hipótesis de relación para contraste individual, no equivalencias ni cumplimiento.
- **Dueño:** asignación propuesta de revisión, por confirmar por las duplas.
- **Verificado:** solo puede marcarse `Sí` con documento, código, página, texto aplicable
  y evidencia localizada en la propuesta para cada requisito, sin brechas abiertas.

> **Regla:** ninguna fila se considera cerrada hasta que el dueño marca `Sí`. Un `—`
> en la columna `Verificado` significa que nadie lo ha confirmado todavía.

Los 19 bloques no sustituyen una matriz normativa requisito por requisito. Una cita
correcta no demuestra cumplimiento; tampoco la ausencia en este inventario demuestra
incumplimiento o inaplicabilidad. No se deducen requisitos faltantes por continuidad numérica.

## 2. Matriz por bloque temático

| Bloque | Códigos citados | RF/RNF D2 relacionados | Dueño | Verificado |
|---|---|---|---|---|
| Arquitectura lógica | RT-02.01, RT-02.04, RT-02.05, RT-02.06, RT-02.08, RT-02.10, RT-02.13, RT-02.14 | RF-001, RF-013, RF-028, RNF-006 | D3 | — |
| Escalamiento y diseño de capacidad | RT-02.02, RT-02.12 | RF-008, RNF-011 | D3 + D4 | — |
| Infraestructura de nube | RT-03.01 a RT-03.24 | RNF-002, RNF-008, RNF-009, RNF-010, RNF-011 | D4 | — |
| Desarrollo y ambientes | RT-04.14 | RNF-013 | D3 | — |
| Gestión de datos e integración | RT-05.01 a RT-05.11, RT-05.13 a RT-05.21, RT-05.23 a RT-05.30 | RF-004, RF-005, RF-007, RF-016, RF-017, RF-019, RF-023, RNF-012, RNF-014 | D3 | — |
| Seguridad física de sala | RT-06.01 a RT-06.34 | RNF-008 | D4 | — |
| Recuperación y respaldo | RT-07.01 a RT-07.14 | RNF-012, RNF-014 | D4 | — |
| Equipamiento y ciclo de vida | RT-08.01 a RT-08.19 | RNF-004, RNF-005, RNF-010 | D4 | — |
| Desempeño y latencias | RT-09.01 a RT-09.10 | RF-001, RF-013, RF-027, RNF-002 | D3 + D4 | — |
| Continuidad operacional | RT-10.01 a RT-10.09 | RNF-008 | D4 | — |
| Seguridad y privacidad | RT-11.01, RT-11.10 | RF-022, RNF-013 | D3 + D4 | — |
| Identidad y acceso | RT-12.11, RT-12.12 | RF-020, RF-021, RF-022, RNF-013 | D4 | — |
| Experiencia de usuario | RT-13.08, RT-13.12 | RNF-001, RF-027 | D1 | — |
| RT-15: sostenibilidad / certificaciones, según fuente | FEP02: RT-15.02, RT-15.03; FEP03: RT-15.02 | Por contrastar; sin enlace funcional confirmado | D4 | — |
| Auditoría y trazabilidad | RT-16.06, RT-16.07, RT-16.09, RT-16.10, RT-16.14, RT-16.21, RT-16.30 | RF-004, RF-011, RF-019, RNF-012 | D3 + D4 | — |
| Integración vehicular y periféricos | RT-17.01, RT-17.06 | RF-007, RNF-005 | D3 + D4 | — |
| Atención y traslado a sitios alejados | RT-21.06, RT-21.16 | RNF-008 | D4 | — |
| Calidad y empresa | RT-23.01 a RT-23.04 | — | D1 | — |
| Innovaciones | RT-26.01 | RF-020, RF-022, RF-023, RF-026 | D2 | — |

## 3. Referencias y cobertura pendientes de contraste

Separar referencias generales, citas compartidas y cobertura por verificar. No se
eliminan citas ni se crean ausencias normativas a partir de saltos de secuencia.

| Código | Dónde aparece | Problema | Resolver con |
|---|---|---|---|
| RT-02, RT-03, RT-05, RT-11, RT-16, RT-17, RT-26 | plan-de-trabajo D3 | Referencia a capítulo, no a requisito | Confirmar si alude a un requisito puntual |
| RT-26.01 | plan-de-trabajo D3 | Requisito FEP02 de ubicación de innovaciones en arquitectura; cita compartida, no duplicado demostrado | D2 + D3 |
| RT-06.15 | D4-MATERIAL-INFORME1.md, apartado de contención de pasillos | Sí está citado; verificar fuente y evidencia, no tratar como ausencia | D4 |
| RT-15.02, RT-15.03 | D4-MATERIAL-INFORME1.md | Desambiguar: FEP02 §15.1 p.27 trata eficiencia/huella de la solución; FEP03 cap.15 trata certificaciones en RT-15.02. No equivalen automáticamente a telemática ni a emisiones de transporte | D4 |
| Cobertura normativa completa | Inventario pendiente de contraste literal | Comparar requisitos existentes y aplicables en las Bases con las citas; no inferir faltantes por secuencia | Todas las duplas |

## 4. Checklist de verificación por dupla

### D1

- [ ] Contrastar RT-13.08 y RT-13.12 por fuente; no asumir que exigencias de interfaz constituyen innovación tipo 5.
- [ ] Verificar que los RT-23.01 a RT-23.04 citados en subdoc1 son correctos.
- [ ] Confirmar que los RT-06 citados en consultas coinciden con el texto de las Bases.

### D2

- [ ] Confirmar que cada RF/RNF del catálogo enlaza con el bloque correcto.
- [ ] Contrastar RF-023 con CA-24 y FEP03 RT-05.29 (consolidación mensual); verificar por separado cualquier enlace propuesto con RT-05.30.
- [ ] Confirmar la trazabilidad de RF-026 (adhesión) con el bloque de innovaciones.

### D3

- [ ] Verificar que los RT-02, RT-04, RT-05 y RT-16 citados son correctos y completos.
- [ ] Comparar la cobertura RT-05 con el texto aplicable, sin completar secuencias supuestas.
- [ ] Verificar la cobertura de seguridad por requisito y fuente, no por numeración.

### D4

- [ ] Verificar que los RT-03, RT-06, RT-07, RT-08, RT-09, RT-10 y RT-21 son correctos.
- [ ] Verificar fuente y evidencia de RT-06.15, ya citado en D4.
- [ ] Resolver si los RT-09.03 a RT-09.10 corresponden a su documento.

## 5. Resumen de estado

| Dupla | Bloques asignados | Verificados | Pendientes |
|---|---|---:|---:|
| D1 | 2 | 0 | 2 |
| D2 | 1 | 0 | 1 |
| D3 | 8 | 0 | 8 |
| D4 | 13 | 0 | 13 |

**19 bloques únicos; 24 asignaciones dupla-bloque; 0 bloques verificados.** Los cinco
bloques compartidos D3 + D4 cuentan una vez para cada dupla: capacidad, desempeño,
seguridad/privacidad, auditoría e integración vehicular/periféricos. Las asignaciones
siguen siendo propuestas, no aceptación de responsabilidad por sus destinatarios.

## 6. Pasos siguientes

1. Cada dupla confirma su asignación y contrasta cada requisito con fuente y evidencia.
2. Resolver las referencias y la cobertura pendientes de la sección 3.
3. Consolidar un T-12 definitivo con todos los requisitos aplicables y su estado real; no omitir los no verificados.
4. Detectar duplicados reales entre RF/RNF D2 y RT normativos una vez verificado.
