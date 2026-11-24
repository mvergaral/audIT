# INDEX — D2 · Conciliación con la entrega 3.2

> Índice para el cruce inter-duplas. Léelo primero antes de comparar D2 con D1, D3 o D4.
> Carpeta de evidencia: `output/auditoria-d2-32` · Worktree de trabajo: `tmp/cierre-entrega-3` (rama `codex/cierre-entrega-3`, **sin commit**).

## 1. Alcance y estado

- **Dupla:** D2.
- **Qué cubre:** S3 (solución) y S7 (plan de trabajo) con sus formularios T-12, T-14, T-15, T-18, los anexos gráficos activos y las observaciones del Art. 46 de S3/S7.
- **Qué no cubre:** no certifica la oferta completa ni los subdocumentos de otras duplas; no revalida las exigencias de las bases asociadas a observaciones fuera de S3/S7.
- **Estado:** revisión y corrección terminadas en fuentes; filas ALC/PLA del anexo Art. 46 del Informe 3 ya consolidadas con los estados de D2; **compilación LaTeX y revisión humana A-6 pendientes** (delegadas al controlador).
- **Git:** sin commit; `output/` (esta evidencia) e `Informe-3/d2/INSUMO_ART46_D2.md` están sin rastrear.
- **Referencia congelada:** planilla `outputs/3.2/Entrega-3.2/INFORME3_AUDIT_PLANILLA_3.2_20261115.xlsx`, commit `a59b9d2a809184b136396e4a61617ebe70f52821`, SHA-256 `7976df5e54cad827b688e9c35a9918631e984b961526f5901a5a25c55fd3247e`.

## 2. Mapa de archivos (qué hay y para qué sirve)

| Archivo | Rol | Contenido clave |
| --- | --- | --- |
| `Revision-consistencia-D2-entrega-3.2.md` | Revisión inicial | 14 hallazgos con evidencia y criterio de cierre. |
| `Plan-correccion.md` | Plan | 7 tareas de corrección aprobadas. |
| `resultado-s3.md` | Resolución S3/T-12 | Localizadores de los cambios en S3 y T-12. |
| `propuesta-red.md` | Red CPM + puente | Malla desagregada, precedencias y asignación por tarea/perfil/mes. |
| `revision-implementacion-s7.md` | Revisión independiente | 7 hallazgos residuales (ya resueltos; ver §5). |
| `RESUMEN.md` | Resumen humano | Qué se hizo, verificación y pendientes. |
| `datos/red32-propuesta.json` | Malla en JSON | Duración, precedencias FS/SS, liberaciones, límites, EDT. |
| `datos/evidencia-verificada.json` | Evidencia | Commit, hash, totales y estados comparados. |
| `datos/comparacion-mensual.csv` | Curva mensual | 56 meses de capacidad interna. |
| `scripts/` | Reproducción | `verificar_revision.py`, `conciliar_32.py` (en worktree), generadores y cierre A-6. |
| `fuentes/` | Copia de consulta | Copia congelada del commit remoto; no se edita. |
| `respaldo-antes-correccion.zip` | Respaldo | Copia de las fuentes locales previo a editar. |

**Entregables de dupla en el worktree** (fuera de esta carpeta):

| Archivo (worktree) | Rol |
| --- | --- |
| `Informe-3/d2/INSUMO_ART46_D2.md` | Insumo Art. 46 de D2: tabla ALC-01..06 y PLA-01..14 (observación, respuesta, fuente, estado). |
| `Informe-3/AUDIT-Anexo-Art46-Informe3-Revision-Independiente.md` | Anexo consolidado: filas ALC/PLA actualizadas con el insumo D2 + PLA-14 agregada. |
| `recursos/Formato-Oferta-audIT/anexos/observaciones-informe3.tex` | Anexo LaTeX del Art. 46 con las respuestas D2. |
| `Investigacion/Persona-8/Registro_A6_Consistencia_D2_20261124.md` | Registro A-6 de la intervención (sin revisión humana aún). |

## 3. Hechos canónicos de D2 (fuente única)

Usa estos valores como la posición de D2; si otra dupla cita otra cifra, hay que conciliar.

| Magnitud | Valor D2 |
| --- | --- |
| Horas internas implementación M1–M20 | **99.626,67 h** |
| Horas internas operación M21–M56 | **84.606 h** |
| Pico de implementación | **M7, 6.276,9 h = 39,2306 FTE** (equivalente a 160 h; no es recuento de personas) |
| Montaje inicial | 10 pilotos M6 + 60/60/52 externos M7/M8/M9 = **182 kits en M9** |
| Mesa N1 | 6 agentes + 1 FTE suplencias = **1.120 h/mes** (40.320 h en 36 meses) |
| Campo en operación | **80 h/mes internas** + 3 visitas correctivas y 2 rondas regionales externas |
| Balizas / lectores | 210 balizas base + 21 reposición; 5 lectores; 19 equipos a bordo reposición |
| Refuerzos de corte | 160 h SRE + 80 h Software en H6/H7/H11/H12 |
| Cierre de migración M21–M24 | 1.669 h compartidas (6.5 = 879 h, 7.2 = 790 h) |
| Paquetes EDT | 54 |
| Hitos E-25 | 12 (H1–H12), en su mes de factura |
| Salida del técnico de implementación | M19 (`Parámetros corrección!B83=19`) |
| Madurez de operación | factor de carga 100/75/50/25 % sobre la bolsa variable, condicionado |

**Reglas de lectura (evita errores de cruce):** horas = capacidad interna contratada (no horas netas de programación); montajes/visitas externas se declaran aparte y no se suman a las horas internas; FTE = horas/160, no headcount.

## 4. Interfaces con otras duplas

### D1 — empresa / calidad / innovaciones
- **Innovaciones INN-1..INN-5 → EDT 12.1..12.5.** Nombres corregidos por D2 (verificar contra T-19 de D1):
  - INN-3 = *acople verificado y registro térmico del semirremolque*; el **kilometraje va en alcance base (8.4)**, no en la innovación.
  - INN-5 = *anticipación circadiana y aviso no punitivo de descanso* (no «Bienestar del conductor y descanso en parador seguro»).
- **T-17 protocolos** consumidos por D2: `CP-SYS-20` (reversión) y `CP-SEC-05` (campaña G13).
- **Económico:** D2 usa la planilla 3.2; el hallazgo D2-14 advierte que los respaldos históricos (`partidas.csv`, presentación 3.1) **no** forman un paquete coherente con la 3.2. Coordinar E-21/E-24/E-25/E-26.

### D3 — datos / demanda
- D2 **reserva** la demanda de `Informe-3/d3/datos/dedicacion_mensual_d3.csv`:
  - `A09` = **6.008 h** (sprinteable en 5.x)
  - `agente_cp_sec_05` = 72 h → 4.1
  - `edt6_7_8_reparto_d2` = 17.531 h → 6/7/8
  - `cierre_ya_incluido_edt6_7` = **1.669 h** → 6.5/7.2 (presupuestado en 13.2/13.4)
  - Innovación 1/2 (implementación y soporte) → 12.1/12.2 y 13.2/13.4.
- Cierre compartido con operación: Datos 100+44 h/mes, QA 40+33 h/mes; ver tabla de correspondencia en `revision-implementacion-s7.md`.

### D4 — compras / proveedores
- Campo externo según `Detalle proveedores D4` (filas 380–426): reposiciones y costos externos.
- Universo de montaje: **148 propios + 34 terceros sin equipo** (montaje) y **192 terceros equipados** (integración lógica, sujeta a consentimientos).
- Límite agregado de subcontratación **40 %** (FEP01, Art. 73, p. 38).

### Bases — FEP01 / Caso
- Art. 17 (continuidad M21), Art. 18.3 (revisiones de 10 días hábiles, p. 13), Art. 73 (40 %), Art. 78 (SLA).
- Hitos `Hitos E25!A2:C13`.

## 5. Resolución de los hallazgos (para no reabrir lo ya cerrado)

Los 7 hallazgos de `revision-implementacion-s7.md` quedaron resueltos en fuentes:

| # | Hallazgo | Cierre |
| --- | --- | --- |
| 1 | Cierre EDT 7.2 sin presupuesto | Descompuesto 6.5/7.2 = 1.669 h; se distingue EDT-alcance de paquete-ejecución. |
| 2 | Demanda D3 ignorada | A09/4.1/6-7-8 reservados dentro de I/G; saldo = coordinación/revisión/guardia. |
| 3 | Banco y recepción de lotes | Balizas 52,5 h → EDT 12.3; banco 60,67 h y analista 424,67 h en 4.2. |
| 4 | Ventanas fuera de la malla | Asignación/Gantt derivadas de nodos; test de ventana activa en verde. |
| 5 | Días de T-18/S7 | Alineados: G13 d182, práctica d192–222, A21 d320–350, H12 d420. |
| 6 | Nombres de nodo | `LOT-P/7/8/9` → `A11-PIL/M7-KIT/M8-KIT/M9-KIT`. |
| 7 | Dependencias H12 + PERT | Cadena de control identificada; CPM no sustituye PERT de tres puntos. |

**Cadena de control hasta H12:** `A01 → A02 → R-H1 → H1 → A05 → INN5-D → INN5-C → INN5-Q → R-H6 → H6 → A17 → R-H8 → H8 → A20-1…5 → A22-SIS → R-H10 → H10 → A23 → H11 → A24 → A25 → R-H12 → H12`.

**Art. 46 consolidado:** las filas ALC-01..06 y PLA-01..14 del anexo `Informe-3/AUDIT-Anexo-Art46-Informe3-Revision-Independiente.md` quedaron con los estados del insumo D2 (69 observaciones; Incorporada 29, Parcial 12, Sin cierre acreditado 28). Los estados granulares se mapearon a esas categorías al recontar; la foliación correlativa se asigna al ensamblar.

## 6. Confirmaciones pendientes por dupla

Antes del cierre, estas dependencias requieren confirmación de la dupla dueña. No se dan por cerradas en D2.

### Con D3 (datos / demanda)
1. **Liderazgo de Desarrollo — 69 h (EDT 13.4):** la planilla no tiene fila de ese perfil en soporte. D2 propone cubrirlas con *Gestión de Servicio / EDT13.2* con acreditación de competencia en H1; D3 debe aceptarlo o declarar brecha.
2. **Prorrateo del cierre:** D2 repartió las 1.669 h en 6.5/7.2 según `dedicacion_mensual_d3.csv` (Datos 44+100, QA 33+40 h/mes). Confirmar que el CSV es la versión vigente y que el reparto refleja la intención de D3.
3. **Cierre «ya incluido»:** confirmar que las 1.669 h están contenidas en las bolsas de soporte y no deben volver a sumarse (evita doble imputación).

### Con D4 (compras / proveedores)
4. **Capacidad del proveedor para 172 montajes M7–M9** (60/60/52, 401,33 h de puesto): validación D2/D4 de los supuestos B78:B83.
5. **34 terceros sin equipo:** autorización de modalidad completa por unidad y agendas de vehículos de baja frecuencia; la meta del padrón de adhesión no acredita acceso.
6. **Campo en operación:** 3 visitas correctivas + 2 rondas regionales/mes en 5 terminales bajo SLA; confirmar capacidad y traslados del proveedor.
7. **Límite agregado 40 %** de subcontratación (FEP01, Art. 73, p. 38).

### Con D1 (empresa / calidad / innovaciones / económico)
8. **Innovaciones en T-19:** confirmar nombres y alcance: INN-3 = acople + registro térmico (kilometraje en base 8.4, no en la innovación); INN-5 = anticipación circadiana (no «Bienestar del conductor y descanso en parador seguro»).
9. **Protocolos T-17:** confirmar que `CP-SYS-20` (reversión) y `CP-SEC-05` (campaña G13) referenciados por D2 son los vigentes.
10. **Económico:** qué respaldos acompañan la oferta (los históricos de `partidas.csv` y la presentación 3.1 no concilian con la 3.2); comprobar E-21/E-24/E-25/E-26 y narrativa con responsables.
11. **Matriz de RT:** si D1 tiene evidencia que acredite filas hoy «No acreditado/Parcial» (RF-003, RF-014, RNF-005, ALC-03/04).

### Externas (mandante / H1 / controlador)
- **Disponibilidad de usuarios** en temporada de fruta y cierres sucesivos de Los Libertadores (PLA-10/PLA-12); las fechas civiles son visualización de SA-01.
- **Revisión humana de la A-6:** no declarada; los titulares revisan asignación por tarea/turno y competencias antes de emitir.
- **Compilación LaTeX** de `preparacion-final/` y foliación: a cargo del controlador (evitar concurrencia de MiKTeX).

## 7. Cómo usar este índice en el cruce

1. Si una dupla cita una cifra de horas/montaje/operación, contrasta contra §3.
2. Si hay un nombre de innovación, nodo o hito distinto, contrasta contra §4 y §5.
3. No des por cerrado lo que §6 marca como pendiente; esas dependencias necesitan confirmación de la dupla dueña.
4. Para el detalle numérico usa `datos/comparacion-mensual.csv` y `datos/red32-propuesta.json`; para el sustento lee el `.md` citado en §2.
