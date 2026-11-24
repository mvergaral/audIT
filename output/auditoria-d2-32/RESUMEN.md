# Resumen de la conciliación D2 con la entrega 3.2

Fecha: 24 de noviembre de 2026. Carpeta de evidencia: `output/auditoria-d2-32`.

Este documento resume el trabajo de revisión y corrección de consistencia de la dupla 2 (D2) con la entrega 3.2, y cierra el ciclo dejando constancia de qué se hizo, qué quedó verificado y qué permanece pendiente.

## Objetivo

Alinear los subdocumentos, anexos y formularios de S3/S7 (y sus formularios T-12, T-14, T-15, T-18) con la planilla económica entregada como 3.2, sin modificar la planilla histórica ni la rama de trabajo.

**Referencia congelada:** `outputs/3.2/Entrega-3.2/INFORME3_AUDIT_PLANILLA_3.2_20261115.xlsx`, extraída de `origin/codex/cierre-entrega-3`, commit `a59b9d2a809184b136396e4a61617ebe70f52821`. SHA-256: `7976df5e54cad827b688e9c35a9918631e984b961526f5901a5a25c55fd3247e`.

## Documentos de esta carpeta

| Archivo | Rol |
| --- | --- |
| `Revision-consistencia-D2-entrega-3.2.md` | Revisión inicial: 14 hallazgos con evidencia y criterio de cierre. |
| `Plan-correccion.md` | Plan de 7 tareas para corregir los hallazgos aprobados. |
| `resultado-s3.md` | Resultado de la corrección de S3 y T-12. |
| `propuesta-red.md` + `datos/red32-propuesta.json` | Red CPM desagregada y puente de horas por tarea/perfil/mes. |
| `revision-implementacion-s7.md` | Revisión independiente de la implementación S7: 7 hallazgos residuales. |
| `INDEX.md` | Guía para el cruce inter-duplas (para la IA). |
| `datos/evidencia-verificada.json` | Commit, hash, totales y estados comparados. |
| `datos/comparacion-mensual.csv` | Detalle de los 56 meses. |
| `scripts/` | Scripts de verificación, generación y cierre (ver nota al pie). |
| `fuentes/` | Copia de consulta del commit remoto (congelada, no se edita). |
| `respaldo-antes-correccion.zip` | Respaldo de las fuentes locales previo a editar. |

## Qué se ejecutó

1. **Revisión** (`Revision-consistencia-D2-entrega-3.2.md`): 14 hallazgos sobre horas y pico, operación/madurez, suplencias de mesa N1, campo, calendarios de montaje, balizas/lectores, refuerzos, innovaciones, red, T-12, reversión, PDF, rótulos heredados y respaldos económicos.
2. **Corrección S3/T-12** (`resultado-s3.md`): montaje 10/60/60/52, balizas/lectores, operación 6+1 y campo 80 h+externo, matriz individual de RT, reversión A/B.
3. **Red y puente S7** (`propuesta-red.md`): malla CPM con 12 hitos en su mes, y puente de horas que concilia exactamente 99.626,67 h internas M1–M20 y 84.606 h M21–M56.
4. **Cierre de anexos y A-6** (`scripts/cerrar_registros.py`, ejecutado): actualizó `observaciones-informe3.tex`, generó el `Registro_A6_Consistencia_D2_20261124.md` y las `declaracion-ia.tex`.
5. **Resolución de los 7 hallazgos de la revisión independiente** (`revision-implementacion-s7.md`):

| Hallazgo | Resolución |
| --- | --- |
| 1 · Cierre EDT 7.2 sin presupuesto | Descompuesto en 6.5 (879 h) y 7.2 (790 h) = 1.669 h; se distingue EDT de alcance del paquete de ejecución (`presupuestado en 13.2/13.4`). |
| 2 · Demanda D3 ignorada | Se reservan A09 (6.008 h), 4.1 y 6/7/8 dentro de I/G; el saldo queda como coordinación/revisión/guardia. |
| 3 · Banco y recepción de lotes | Balizas (52,5 h) movidas a EDT 12.3; piloto y banco conservados en 4.2. |
| 4 · Ventanas fuera de la malla | Asignación y Gantt derivadas de los nodos; `test_toda_asignacion_tiene_ventana_activa` en verde. |
| 5 · Días de T-18/S7 | Alineados a la malla (G13 d182, práctica d192–222, A21 d320–350, H12 d420). |
| 6 · Nombres de nodo | `LOT-P/7/8/9` sustituido por `A11-PIL/M7-KIT/M8-KIT/M9-KIT`; diccionario T-14 con nodos precisos. |
| 7 · Dependencias de H12 y PERT | Identificada la cadena de control A01→…→H12 y declarado que el CPM no sustituye el PERT de tres puntos. |

6. **Entrega como dupla**: se creó `Informe-3/d2/INSUMO_ART46_D2.md` (tabla Art. 46 con ALC-01..06 y PLA-01..14, siguiendo la convención de D3/D4) y se actualizó el anexo consolidado `Informe-3/AUDIT-Anexo-Art46-Informe3-Revision-Independiente.md`: 19 filas ALC/PLA con los textos del insumo + fila PLA-14 nueva; cabecera a 69 observaciones con estados Incorporada (29) / Parcial (12) / Sin cierre acreditado (28).

## Verificación

- Sumas conservadas: M1–M20 = 99.626,67 h; M21–M56 = 84.606 h; cierre 6.5/7.2 = 1.669 h.
- 7 pruebas de `test_conciliacion_32.py` en verde (esfuerzo total y mensual, inventario de montaje 182 kits, suplencias/campo, red sin holguras negativas, reservas directas y cierre, ventanas activas).
- Referencia SHA-256 de la planilla sin cambios: `7976df…3247e`.

## Pendiente (fuera del alcance de esta sesión)

- **Confirmaciones por dupla**: ver `INDEX.md` §6 (D3: 69 h de liderazgo y prorrateo del cierre; D4: 172 montajes externos y campo; D1: innovaciones en T-19, protocolos T-17 y respaldos económicos).
- **Compilación LaTeX** de los PDF de `preparacion-final/`, delegada al controlador de integración para evitar concurrencia de MiKTeX.
- **Revisión humana** de la A-6, que no se declara realizada.
- **Git**: no se hizo commit, merge ni publicación; los cambios viven en el worktree `tmp/cierre-entrega-3`. Además, `output/` (evidencia) y `Informe-3/d2/INSUMO_ART46_D2.md` están sin rastrear (`??`); deben incluirse al subir.

---

Nota: los scripts de `scripts/` se movieron desde la raíz de esta carpeta. Fueron ejecutados en su ubicación original; si se reejecutan desde `scripts/`, ajustar los índices de `Path(__file__).resolve().parents[N]` que apuntan al worktree `tmp/cierre-entrega-3`.
