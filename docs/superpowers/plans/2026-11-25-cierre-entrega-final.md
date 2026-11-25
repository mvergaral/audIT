# Plan de trabajo para cerrar la entrega final del 25 de noviembre de 2026

## Estado de ejecución al pausar el 25 de noviembre de 2026

**Pausado por solicitud expresa del usuario para conservar contexto y subir el avance al repositorio. No declarar la oferta lista.**

El registro completo y las instrucciones para retomar están en [REANUDAR.md](../../../outputs/cierre-20261125/REANUDAR.md) y el estado estructurado en [ESTADO-EJECUCION.json](../../../outputs/cierre-20261125/ESTADO-EJECUCION.json). No reiniciar desde cero ni ejecutar de nuevo los scripts de edición no idempotentes.

| Tarea | Estado al pausar |
|---|---|
| 1. Corte e inventario | Snapshot y registro realizados; matriz final depende del ensamblaje. |
| 2. Anexos | Fuentes e integración S1/S2/S5 preparadas; folios y PDF finales pendientes. |
| 3. IA y revisión humana | Autoría corporativa y declaraciones corregidas; revisión/firma reales pendientes. |
| 4. Sobre 1 | 25 piezas simuladas creadas por autorización expresa; PDF provisional de 37 páginas; verificar última edición de A-6/poder e índice tras recompilar. |
| 5. Sobre 3 | Cinco archivos y 37 partidas cotejados; fórmula/precio preservados. Revisión humana pendiente. |
| 6. Riesgo y coherencia | Correcciones documentales realizadas; capacidad/ventanas futuras no acreditadas y RIE-05 parcial. |
| 7. Art. 46 | 74 filas inventariadas; estados y localizadores corregidos; cotejar evidencia/folios finales. |
| 8. Regeneración | Segunda corrida global interrumpida durante su primera vuelta. Sin manifiesto final estabilizado. |
| 9. Verificación global | Runner preparado; pendiente ejecutarlo sobre técnico completo y revisar imágenes. |
| 10. Firmas y ZIP | Pendientes; no existen tres paquetes finales comprobados de este corte. |
| 11. Entrega | Carlos Abarza designado; no se envió ni presentó nada. |

El usuario confirmó que el video está listo y facilitará el enlace. Ignacio Cuevas mantiene revisión/firma D2/A-6, Carlos Abarza la entrega, y el plazo confirmado sigue siendo las 14:00 de Chile del 25-11-2026. Si se retoma después, confirmar la situación del plazo sin asumir prórroga.

> Para ejecutar este plan: trabajar tarea por tarea con la skill `executing-plans`, registrar evidencia y revisar cada resultado antes de continuar con sus dependencias. Este plan no acredita que las tareas estén realizadas.

**Objetivo:** disponer de los tres sobres completos, coherentes, revisados y preparados para su entrega simultánea.

**Enfoque:** congelar un corte de trabajo, corregir las brechas por dupla, revisar el contenido, regenerar los documentos afectados y verificar los paquetes extraídos. D1 coordina la integración; D2, D3 y D4 validan sus contenidos.

**Herramientas:** Git, fuentes LaTeX del formato oficial, compiladores y verificadores existentes, inspección de PDF, modelo XLSX y comprobación de ZIP y SHA-256.

**Base del plan:** revisión del repositorio en `c140209`, `CLAUDE.md`, `recursos/Formato-Oferta-audIT/GUIA.md`, registros de `Entrega_Final/`, cierre de D2 y manifiesto de `salida/final/`. Plazo registrado: 25-11-2026 a las 14:00, America/Santiago. Las duraciones siguientes son estimaciones de trabajo, no una garantía de llegada a ese plazo.

## Reglas de ejecución

- Conservar los cambios locales y originales. No usar limpieza destructiva, sobrescritura de paquetes históricos ni cambios de precio para hacer pasar controles.
- Antes de modificar LaTeX, leer íntegro `recursos/Formato-Oferta-audIT/LEEME-EQUIPO.md` y consultar `GUIA.md`.
- Cada dupla modifica sus subdocumentos. Los cambios de integración que alcancen `estilo/`, `configuracion/`, `portadas/`, `temas/` o `herramientas/` quedan a cargo del mantenedor habilitado según `CLAUDE.md`.
- Consultar las bases con `python -X utf8 tools/buscar.py`; no leer el corpus completo ni los PDF escaneados originales.
- Mantener los nombres personales en registros individuales y A-6 según corresponda; en la propuesta técnica usar códigos y roles corporativos conforme a `CLAUDE.md`.
- La revisión humana y sus firmas deben realizarse y acreditarse. Una imagen de media firma en el PDF no acredita esa revisión.
- Diferenciar condiciones futuras del contrato de requisitos de liberación actuales. No declarar ejecutados pilotos, autorizaciones, financiamientos o contratos por el hecho de describirlos.
- Este plan cubre preparación y comprobación. El envío requiere una instrucción explícita; no contactar al equipo automáticamente.

## Secuencia y reparto propuesto

| Bloque | Trabajo | Responsable propuesto | Estimación | Depende de |
|---|---|---|---|---|
| 1 | Congelar corte e inventario | D1 / integración | 15–25 min | Inicio |
| 2A | Anexos y completitud técnica | D3 + D1 | 20–40 min | 1 |
| 2B | Declaraciones IA y revisión humana | Cada dupla; D1 consolida | 30–60 min | 1 |
| 2C | Cotejo administrativo | D1 | 20–40 min | 1 |
| 2D | Coherencia económica y riesgo de plazo | D2 + D3 + D4 | 30–60 min | 1 |
| 3 | Observaciones y regeneración final | Cada dupla + mantenedor | 45–90 min | 2A–2D |
| 4 | Verificación global y correcciones | D1 / QA + dupla afectada | 40–60 min | 3 |
| 5 | Firmas, ZIP y preparación de entrega | Responsables humanos + integración | 30–45 min | 4 |

Los frentes 2A–2D pueden repartirse entre personas del equipo. Si ejecuta una sola persona, se acumulan los tiempos. Con responsables disponibles y sin fallos de compilación, reservar aproximadamente 3–5 horas, más impresión y traslado. Recalcular el tiempo restante al iniciar; si no alcanza, comunicar los bloqueos sin declararlos resueltos.

## Tarea 1. Fijar el corte y una matriz de control vigente

**Responsable:** D1 / integración. **Salida:** inventario y matriz actualizados del corte de entrega.

- [ ] Registrar commit, fecha, hora y estado local con `git rev-parse HEAD` y `git status --short`. Identificar archivos excluidos por sparse checkout; su ausencia física no significa ausencia en Git.
- [ ] Crear una carpeta nueva de preparación y evidencia, separada de `TRABAJO_*_INCOMPLETO` y de paquetes históricos.
- [ ] Inventariar Sobre 1, todos los capítulos S1–S14, formularios técnicos, anexos, Art. 46 y los tres entregables económicos E-21.
- [ ] Para cada archivo registrar fuente vigente, nombre, responsable, versión, presencia, revisión humana, firma aplicable y destino dentro del sobre.
- [ ] Conciliar `outputs/cierre-entrega-final/MATRIZ-UNICA.md` y `.csv` contra el corte nuevo: el diagnóstico anterior de ausencia del Sobre 1, figura física ilegible y condiciones económicas pendientes fue superado parcialmente por cambios posteriores. Conservar el historial.

**Cierre:** cada requisito tiene archivo identificado o una brecha explícita, responsable y comprobación; no se mezclan versiones históricas con finales.

## Tarea 2. Integrar los anexos faltantes y comprobar el inventario técnico

**Responsables:** D3 produce; D1 integra. **Archivos principales:** `subdocumentos/05-datos/contenido.tex`, `anexos.tex`, `salida/final-por-subdocumento/AUDIT-Subdocumento5-Anexos.pdf` y `salida/final/manifiesto.json`, todos dentro de `recursos/Formato-Oferta-audIT/`.

- [ ] Incorporar el diccionario independiente `AUDIT-Subdocumento5-Anexos.pdf` al conjunto definitivo. Existe en `final-por-subdocumento`, pero no figura en `final` ni en su manifiesto revisado.
- [ ] Comprobar que corresponde al modelo actual y a las correcciones de asignación/reasignación de S5 y T-17; regenerarlo si procede.
- [ ] Comprobar también los anexos independientes de S1 y S2, el catálogo de pruebas y el anexo Art. 46 contra todas las remisiones del cuerpo.
- [ ] Resolver con el mantenedor el tratamiento de folios de anexos: el manifiesto actual declara modo continuo, mientras los anexos S1/S2 comienzan en 1. Verificar el criterio autorizado y reflejarlo en índice, manifiesto y PDF.

**Cierre:** toda remisión a un archivo independiente encuentra ese archivo en el paquete, y su contenido, folios e índice coinciden.

## Tarea 3. Cerrar declaraciones IA y revisión humana

**Responsables:** D1, D2, D3 y D4 en su ámbito. Ignacio Cuevas consta como responsable designado para la revisión final de D2; confirmar su disponibilidad.

- [ ] Revisar `subdocumentos/*/declaracion-ia.tex`, especialmente S1, S2 y S9, y sustituir nombres reales de integrantes por códigos y roles en la propuesta técnica.
- [ ] Conservar la identificación y trazabilidad personal en las bitácoras individuales; no borrar la evidencia del uso de IA.
- [ ] D2 revisa el corte de S3/S7, formularios y Sobre 3. Sus declaraciones actuales indican revisión por realizar.
- [ ] D3 revisa las validaciones pendientes de S5 y S6: modelo/diccionario, disponibilidad, gobierno, capacidad y evidencia de sprints, cotejadas con S4, S7, S9 y S11.
- [ ] D1 y D4 confirman que sus revisiones acreditan la última edición y no solamente una versión anterior.
- [ ] Registrar para cada revisión persona, fecha, archivos/versiones, alcance, hallazgos y resolución. Actualizar la declaración del documento únicamente después de realizarla.
- [ ] Conciliar el A-6 consolidado del Sobre 1 con estas revisiones y completar las firmas que correspondan. La bitácora individual no sustituye el A-6 del oferente.

**Cierre:** no quedan afirmaciones falsas de revisión ni revisiones obligatorias pendientes para emitir; las versiones revisadas están identificadas.

## Tarea 4. Revisar la completitud del Sobre 1

**Responsable:** D1. **Entrada:** `recursos/Formato-Oferta-audIT/sobre1-antecedentes.tex` y el PDF administrativo existente.

- [ ] Cotejar identificación, A-1 a A-6, antecedentes legales, financieros, habilitantes y garantía contra las secciones aplicables de las bases mediante búsquedas dirigidas.
- [ ] Distinguir documentos efectivamente incorporados de tablas que solo enumeran antecedentes. Determinar si el expediente simulado contiene el respaldo exigido para cada ítem.
- [ ] Comprobar coherencia de razón social, RUT, representante, domicilios, vigencias y garantías con S1, T-6 y Sobre 3.
- [ ] Revisar el tratamiento de las referencias académicas y de simulación frente a los comunicados: conservar la transparencia exigida en el lugar permitido y evitar residuos prohibidos en la propuesta técnica.
- [ ] Confirmar carátula, índice, folios, firmas y respaldo digital.
- [ ] Asignar a una persona la impresión y preparación física. FEP01 · Artículo 48 · p.29 exige Sobre 1 físico, foliado y firmado, con respaldo digital; los sobres 2 y 3 son electrónicos y se entregan simultáneamente.

**Cierre:** checklist administrativo cotejado por D1 y responsable humano de la preparación física identificado. No se da por completo solo porque existe el PDF.

## Tarea 5. Cotejar el Sobre 3 y sus condiciones

**Responsables:** D2; apoyo D3/D4 para partidas. **Entrada:** `outputs/cierre-d2-final/CIERRE-D2.md`, `documentos/`, manifiestos y paquete económico del mismo corte.

- [ ] Confirmar los tres entregables E-21: oferta económica, análisis financiero y planilla auditable; cotejar sus nombres y formatos exigidos.
- [ ] Mantener las decisiones ya aceptadas: vigencia de 150 días, operación sin reajuste y tarifas E-26 sin modificar el precio global ni añadir facturación horaria.
- [ ] Cotejar venta, costo, IVA, moneda, parámetros E-24, hitos, curvas e indicadores entre PDF, DOCX y XLSX; usar como respaldo los 37 cruces y la evidencia de recálculo del cierre D2.
- [ ] Confirmar que se usa el modelo final con las notas de montaje corregidas, tarifas y condiciones, en lugar de una copia histórica 3.2.
- [ ] Revisar pagadores y costos de montaje, soporte, energía, combustible de pruebas e innovaciones frente al corte técnico vigente.
- [ ] Confirmar que la financiación y proveedores condicionados se presentan como supuestos o compromisos según su evidencia, sin afirmar contratos efectivos no acreditados.
- [ ] Reutilizar el recálculo documentado si el XLSX no cambió; si cambian fórmulas o entradas, recalcular una copia y repetir conciliación e indicadores antes de sustituir el paquete.

**Cierre:** los tres entregables son del mismo corte, sus cifras coinciden y las condiciones están revisadas y firmadas cuando corresponda.

## Tarea 6. Resolver la revisión del riesgo de plazo y la coherencia transversal

**Responsables:** D2 + D3 + D4; D1 comprueba aceptación y pruebas.

- [ ] Revisar S7, T-14/T-15/T-18, S8/T-16 y el aviso `Entrega_Final/D4/AVISO-D2-MALLA-SIN-MARGEN.md`.
- [ ] Ratificar la declaración actual: H4, H7 y H12 sin margen; H11 protegido por A23. No reutilizar el 92,1 % de la red histórica.
- [ ] Revisar capacidad neta por ejecutor/turno, terceros, ventanas y estimaciones de tres puntos. Registrar qué está validado ahora y qué queda como condición futura de H1.
- [ ] Si se aprueba modificar la malla, regenerar red, Gantt, holguras y simulación, y revisar el efecto económico y de aceptación antes de integrar. Si se mantiene, documentar su riesgo y respuesta coherentes, sin afirmar holgura recuperada.
- [ ] Cotejar los puntos corregidos en los últimos commits: autonomía sin enlace, DR/R-24/H7, montaje hasta M9, campo externo desde M19, dotación, innovaciones y pruebas T-17.

**Cierre:** decisión de ingeniería documentada y coherente entre planificación, riesgos, pruebas y presupuesto. Las validaciones futuras están distinguidas de trabajo de revisión pendiente hoy.

## Tarea 7. Cerrar la trazabilidad del Art. 46

**Responsable:** D1 consolida; cada dupla acredita sus filas. **Archivo:** `recursos/Formato-Oferta-audIT/anexos/observaciones-informe3.tex`.

- [ ] Para cada observación, comprobar respuesta, cambio aplicado y referencia concreta a capítulo/sección/folio del corte final.
- [ ] Separar cierre documental, condición contractual futura y observación realmente abierta. No marcar una promesa como ejecución acreditada.
- [ ] Revisar especialmente las filas tocadas por la incorporación del diccionario, revisión IA, riesgo de plazo y DR.
- [ ] Actualizar las referencias tras fijar la foliación e incluir el anexo en la ubicación exigida.

**Cierre:** todas las filas tienen estado sustentado y referencia localizable; las brechas materiales tienen resolución o quedan expresamente como bloqueos.

## Tarea 8. Regenerar el conjunto definitivo

**Responsables:** cada dupla corrige; el mantenedor realiza el ensamblaje global.

- [ ] Verificar disponibilidad de LuaLaTeX, biber, latexmk y su dependencia Perl. El cierre anterior registró un problema de Perl: comprobar el entorno antes de iniciar la compilación global.
- [ ] Leer la configuración y confirmar instancia `final` y criterio de foliación. El mantenedor aplica los ajustes de integración requeridos.
- [ ] Desde `recursos/Formato-Oferta-audIT/`, usar el flujo documentado `python herramientas/compilar.py subdocs --continuo --caratula` para el técnico, después de confirmar la instancia y el tratamiento de anexos.
- [ ] Regenerar el administrativo con su flujo mantenido; no asumir que el compilador de subdocumentos lo incluye automáticamente.
- [ ] Para el económico, conservar el corte D2 revisado o usar `python herramientas/compilar.py economico` solo después de verificar que sus fuentes y planilla corresponden a ese corte. No sustituirlo por salidas antiguas.
- [ ] Regenerar los Markdown afectados y los índices/manifiestos para que describan los PDF definitivos.

**Cierre:** documentos compilados, sin referencias sin resolver y con fuentes y registros del mismo corte. Compilar no equivale a aprobar el contenido.

## Tarea 9. Verificar el conjunto y corregir hallazgos

**Responsable:** D1 / QA; corrección por la dupla propietaria.

- [ ] Ejecutar `python herramientas/verificar.py salida/final/manifiesto.json` desde el formato oficial, sobre el manifiesto final completo. Agregar los manifiestos administrativo y económico que correspondan; ningún sobre debe quedar fuera del alcance.
- [ ] Exigir cero incumplimientos materiales. Analizar cada hallazgo del verificador para distinguir un defecto de una limitación del control, dejando evidencia del dictamen.
- [ ] Comprobar folios e índice, nombres, anexos, firmas aplicables, fuentes incrustadas, cuerpo/tablas/figuras legibles, tablas cortadas y ausencia de `??` o marcadores sin resolver.
- [ ] Inspeccionar visualmente las nuevas láminas físicas de S4, diccionario S5, cronograma S7, T-17, anexos S1/S2, Art. 46 y documentos económicos, además de portadas y transiciones de folios.
- [ ] Corregir en fuentes y regenerar los archivos afectados; repetir el control correspondiente y los controles globales afectados por cambios de páginas.

**Cierre:** informe final fechado, con alcance explícito y sin bloqueos abiertos. Los reportes antiguos no sustituyen esta comprobación.

## Tarea 10. Obtener firmas y preparar los ZIP

**Responsables:** revisores y representante según corresponda; D1 integra.

- [ ] Obtener las firmas sobre las versiones ya revisadas. Si se modifica contenido después de firmar, volver a revisar y firmar la versión afectada.
- [ ] Confirmar los nombres oficiales de los ZIP con los artículos 49–51 y el formato vigente; no inventar nombres para suplir un dato no consultado.
- [ ] Generar un paquete por sobre con los archivos exigidos. Excluir temporales, logs, cachés, código y borradores, salvo archivos expresamente exigidos.
- [ ] Verificar los nombres, cantidad de archivos, tamaños y SHA-256 de los archivos incorporados.
- [ ] Extraer cada ZIP en una carpeta nueva, comprobar integridad y abrir los PDF/DOCX/XLSX de la copia extraída; contrastar su inventario con el manifiesto.
- [ ] Confirmar ausencia de enlaces locales rotos y de archivos omitidos, especialmente `AUDIT-Subdocumento5-Anexos.pdf`.

**Cierre:** tres paquetes identificados, íntegros y cotejados; el contenido extraído coincide con las versiones aprobadas.

## Tarea 11. Preparar y registrar la entrega

**Responsable:** persona designada por el equipo para presentar la oferta.

- [ ] Confirmar canal, destinatario, plazo aplicable y responsable de entrega.
- [ ] Preparar el Sobre 1 físico con folios, firmas y respaldo digital, y los sobres electrónicos 2 y 3 según las bases y las instrucciones vigentes del proceso.
- [ ] Confirmar que no falta ningún sobre: FEP01 · Artículo 48 · p.29 exige presentación simultánea y copulativa.
- [ ] Si hay exposición o demostración exigida hoy, cotejar sus instrucciones específicas y ensayar los enlaces y materiales correspondientes con el corte final. No añadir una presentación como requisito sin comprobarlo.
- [ ] Realizar la entrega mediante la persona autorizada y conservar comprobante, hora y hashes de los paquetes presentados.

**Cierre:** recepción acreditada de los tres sobres. Tener los ZIP en disco solo permite declarar «preparado para entregar».

## Criterio de liberación

- [ ] Inventario completo y anexos presentes.
- [ ] Revisión humana y A-6 del corte actual acreditados.
- [ ] Declaraciones técnicas sin nombres personales prohibidos.
- [ ] Riesgos y condiciones futuras expresados de forma coherente.
- [ ] Cifras técnicas y económicas conciliadas.
- [ ] Art. 46 trazado a cambios reales.
- [ ] Índice, folios, formato y legibilidad verificados.
- [ ] Firmas aplicables obtenidas.
- [ ] Tres paquetes extraídos y comprobados; preparación física confirmada.
- [ ] Responsable, canal y plazo confirmados.

Si falla una condición, registrar archivo/requisito, responsable y acción necesaria. No sustituir un requisito de admisibilidad por un aviso editorial ni declarar realizada una revisión humana pendiente.
