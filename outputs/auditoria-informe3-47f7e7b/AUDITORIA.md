# Auditoría del trabajo de IA sobre el Informe 3

**Uso interno. Corte auditado: `47f7e7b1717e531fcbed6a171b6ed2023a1552e6`, rama `main`.**

## 1. Dictamen y alcance

**El trabajo contiene cálculos útiles y reproducibles, pero todavía no constituye una corrección completa del Informe 3. No recomiendo presentar el paquete agregado en este commit como versión corregida definitiva.** La principal brecha es de integración: se anexaron escenarios a un modelo económico cuyo flujo principal, costos y gráficos siguen siendo los anteriores. Además, las nuevas hojas de resultados contienen valores fijos que no se actualizan al modificar sus entradas.

La transcripción aportada por el usuario confirma que la preocupación del profesor era la credibilidad de la curva de costos, la liquidez, la reducción del soporte y el término del gasto de instalación. Resolver eso exige modificar las actividades y sus costos, calcular el flujo resultante y mostrarlo en los entregables. Agregar financiamiento y anexos de simulación no cierra por sí solo esas correcciones.

Esta auditoría revisa el commit de 38 archivos agregado por el compañero, sus dos paquetes económicos y las fuentes de generación. Compara con el corte `c9a6515652c3357ea684bf0bb9338b7c4ec028fd` que esos scripts utilizan. El checkout estaba limpio al inicio. Se consultaron los refs remotos en lectura y `origin/main` coincide con el corte auditado. No se modificaron los entregables ni LaTeX, ni se publicaron cambios o modificaron tickets.

| Paquete realmente inspeccionado | PDF | Excel | Presentación |
|---|---:|---:|---:|
| `entrega-consolidada/` | 26 páginas | 38 hojas | 9 láminas |
| `entrega-consolidada/activacion-simulada/` | 27 páginas | 42 hojas | 10 láminas |
| Constancia de alcance de la variante | 1 página | — | — |

El PDF original de revisión del Informe 2 tiene 48 páginas. Las bases se consultaron por secciones con `tools/buscar.py`, sin leer sus PDF escaneados. El inventario, huellas SHA-256 y estructura de los entregables están en [evidencia.json](/home/axeler8/Escritorio/audIT/outputs/auditoria-informe3-47f7e7b/evidencia.json).

No se acreditó cuál fue exactamente el paquete mostrado al profesor. La transcripción contiene estimaciones orales contradictorias del préstamo y no identifica una versión; la referencia posterior de CLP 210–250 millones más unos CLP 50 millones de socios es compatible con la base revisada, pero no demuestra identidad. Tampoco corresponde convertir la sospecha oral de varios usos de línea en un dato: en el escenario base inspeccionado hay un giro en M9 y devolución en M10. Los escenarios de atraso tienen otro comportamiento.

## 2. Contraste con la transcripción

El prompt recoge razonablemente los temas económicos del intercambio. Añade criterios de auditoría y exigencias de cierre más detallados que las palabras del profesor. No deben atribuirse al profesor todos esos detalles: por ejemplo, la meta de CLP 10 millones y la externalización exacta de 172 montajes son decisiones del modelo. La preferencia por UF/USD surge del intercambio inicial, sin una orden literal tan categórica como la de corregir instalación y liquidez.

Fuente preservada: [transcripción del profesor](/home/axeler8/Escritorio/audIT/outputs/auditoria-informe3-47f7e7b/fuentes/transcripcion-profesor.txt). Prompt revisado: [prompt del compañero](/home/axeler8/Escritorio/audIT/outputs/auditoria-informe3-47f7e7b/fuentes/prompt-companero.md).

| Criterio | Evidencia oral | Qué quedó en el paquete | Estado de cierre |
|---|---|---|---|
| PROF-01: unidades legibles | 00:00:07–00:01:55: intercambio sobre millones, UF y dólares | El PDF anterior ya incluye equivalencias. Las láminas 2, 5, 6 y 8–10 siguen usando CLP/millones. Los PNG en UF están fuera del PDF y de las láminas. | Parcial |
| PROF-02: línea para contingencias | 00:02:45–00:06:15: ajustar para estar sobre la línea de flotación y reservar el crédito para riesgo | Se reproduce una base alternativa con CLP 332.814.380 de capital y caja mínima CLP 10.000.002,46 en M9. El flujo principal del Excel conserva CLP 274.452.748 y un giro cercano a CLP 45 millones. | Parcial: simulación calculada, base principal pendiente |
| PROF-03: costos creíbles y picos | 00:06:18–00:09:34: no se distinguen adquisiciones, instalación y puestas en producción | Hay un gráfico PNG de egresos y conciliaciones, pero se conserva la Curva S anterior. No se implantó un calendario integrado de compras, instalación, pruebas y estabilización con costos por actividad. | Parcial |
| PROF-04: bajar soporte con la madurez | 00:05:43–00:08:36: disminuir carga de soporte al estabilizarse el sistema | Se explica el retiro de 103 h de Datos/QA en M25. Esa reducción corresponde a cierres de implementación y ya estaba en la base. La nómina mantiene CLP 85.400.000/mes entre M25 y M56. | Parcial: falta la reducción operativa sustentada |
| PROF-05: préstamo, socios y devolución visibles | 00:07:51–00:10:19: cuánto se pidió, cuándo se paga y dónde se refleja | Deuda e intereses se reproducen y aparecen en tablas/CSV. Los gráficos principales no se regeneraron con las nuevas entradas y amortizaciones identificadas. Conviven varias estructuras de capital. | Parcial |
| PROF-06: instalación como servicio que termina | 00:09:34–00:12:11: revisar técnicos, cotizar y externalizar lo operativo | Se simulan 172 montajes externos después de 10 pilotos. El servicio termina en M9, pero se conserva toda la nómina y los costos principales no incorporan el servicio. | Parcial: no se resolvió la sustitución de horas/costos |

**Ninguno de los seis criterios queda cerrado íntegramente en el paquete de entrega inspeccionado.** Esto no significa que sus cálculos sean todos incorrectos: se distingue a continuación la evidencia que sí conviene conservar.

## 3. Hallazgos comprobados

### AI3-01 · Alta · La nueva base no reemplaza el escenario dependiente de la línea

Los 34 worksheets originales y sus partes de gráficos/relaciones inspeccionadas permanecen idénticos a los del Excel de `c9a6515`: **36 de 36 partes comparadas sin cambios**. Las cuatro hojas del consolidado y otras cuatro de activación se agregan alrededor de ese núcleo.

En ambos Excel, `Parámetros D2!B4 = 274.452.748`; `Flujo de Caja!R10 = 44.999.999,54` de giro y `W10 = 0` de caja al cierre de M9. En cambio, los anexos usan capital inicial CLP 332.814.380. El PDF conserva en p.12 el caso con línea y agrega en pp.24–25 otros importes; la Curva S de p.9 y la lámina 4 siguen representando el caso anterior.

El addendum avisa que preserva escenarios históricos. Esa aclaración permite usarlos como antecedentes, pero no convierte el modelo original en la oferta corregida que solicita el modo Integral del prompt.

**Cierre:** definir una base activa y parametrizada; incorporar su financiamiento y costos a `Financiamiento`, `Costos`, `Flujo de Caja`, `Curva S` e indicadores afectados; regenerar el PDF y las láminas. La base debe mostrar cero giros/saldo de línea y cierres positivos. El estrés debe conservar su propio resultado, incluso si queda condicionado.

Referencias: PROF-02/03/05; Aclaraciones del Informe 3 §§5.3–5.5; [generador de hojas](/home/axeler8/Escritorio/audIT/outputs/informe3-integral/regenerar_cierre.py:178); [AUD-17](https://linear.app/audit-fep/issue/AUD-17), [AUD-20](https://linear.app/audit-fep/issue/AUD-20), [AUD-23](https://linear.app/audit-fep/issue/AUD-23).

### AI3-02 · Alta · Los resúmenes nuevos no reaccionan a sus entradas

Se recalcularon íntegramente tres copias mediante **LibreOffice Calc `calculateAll()`**, sin alterar los originales:

| Prueba | Resultado que sí cambia | Resultado nuevo que permanece congelado |
|---|---|---|
| Subir `Parámetros D2!B4` en CLP 10 millones | `Financiamiento!B2` sube y el giro de M9 baja de CLP 44.999.999,54 a CLP 35.575.999,54 | Las hojas de caja por fecha y sus mínimos conservan los números anteriores |
| Reducir `Caja activacion montaje!F3` en CLP 1 millón | `G3` baja de CLP 266.251.504 a CLP 265.251.504 | `Cierres activacion!D2` sigue en CLP 219.061.826, aunque ese cierre debe reflejar el millón menos |

`Minimos meses criticos` contiene 108 celdas numéricas y ninguna fórmula. `Cierres activacion` contiene 672 celdas numéricas y ninguna fórmula. En las hojas de movimientos solo la columna G de saldo se formula; los importes y las aperturas de cada mes son instantáneas. Al cambiar un evento tampoco se traslada automáticamente su efecto a la apertura del mes siguiente.

Las cifras guardadas coinciden con la corrida Python original. El defecto es que el Excel entregado no funciona como modelo integrado de esos escenarios. Las Aclaraciones §5.5 prohíben resultados fijos digitados y exigen formulación íntegra. Generarlos automáticamente con Python no resuelve esa exigencia del Excel.

**Cierre:** vincular entradas, deuda, movimientos, aperturas, cierres y mínimos mediante fórmulas. Repetir las dos mutaciones y verificar también indicadores/gráficos cuando corresponda. Cambiar solo financiamiento no tiene por qué cambiar el VAN de la Fila A; ese resultado constante es correcto.

Prueba: [resultados del recálculo](/home/axeler8/Escritorio/audIT/outputs/auditoria-informe3-47f7e7b/pruebas-libreoffice.json). Origen: [escritura de resultados fijos y saldos](/home/axeler8/Escritorio/audIT/outputs/informe3-integral/regenerar_cierre.py:164). [AUD-23](https://linear.app/audit-fep/issue/AUD-23).

### AI3-03 · Alta · Se agrega outsourcing sin resolver qué trabajo deja la nómina

La variante declara expresamente que conserva la nómina completa. La simulación suma pagos externos de CLP 6.421.333 netos y CLP 1.220.053 de IVA, total CLP 7.641.386, y dimensiona nuevo capital para pagarlos. Es una sensibilidad conservadora válida; no demuestra la sustitución que pidió el profesor.

No corresponde descontar automáticamente todo el valor interno: antes hay que identificar horas efectivamente evitables y conservar integración, banco, QA, supervisión y recepción. Tampoco debe llamarse ahorro a un costo fijo que seguirá pagándose. La tarea pendiente es demostrar la reasignación o el término del costo por perfil y mes.

Si la variante con nómina completa se adopta como base, su costo neto debe incluir el servicio una vez: CLP 7.984.400.845,22 + CLP 6.421.333 = **CLP 7.990.822.178,22**. A venta fija de CLP 9.796.810.853,03, el margen pasa de 18,50 % a aproximadamente **18,4345 %**, antes de otros cambios. El interés adicional calculado de CLP 679.793,90 es financiamiento, no costo operativo del EBITDA. Actualmente esos efectos no se integran a las hojas principales.

La tarifa externa de CLP 16.000/h se construye a paridad con el costo interno y se identifica como supuesto. No es una cotización independiente; hay que justificar cómo cubre traslado, coordinación y servicio en cinco terminales, o conservarla claramente como hipótesis. El Art.73 exige autorización previa escrita, tope agregado del 40 %, resguardo del núcleo crítico y responsabilidad por subcontratistas.

**Cierre:** matriz `rol/actividad/mes → horas internas originales → horas sustituidas → horas retenidas → costo interno remanente → servicio externo`. Hacerla alimentar el flujo y comprobar el término de cada lote, sin duplicaciones.

Referencias: PROF-06; FEP01 · Artículo 73° · p.38; FEP01 · Artículo 57.2 · p.32; [LEEME de activación](/home/axeler8/Escritorio/audIT/outputs/informe3-integral/entrega-consolidada/activacion-simulada/LEEME.md:5); [puente pendiente desde nómina](/home/axeler8/Escritorio/audIT/outputs/informe3-integral/entrega-consolidada/Cierre-tecnico-D1-D2.md:37). [AUD-15](https://linear.app/audit-fep/issue/AUD-15), [AUD-32](https://linear.app/audit-fep/issue/AUD-32), [AUD-37](https://linear.app/audit-fep/issue/AUD-37).

### AI3-04 · Alta · La explicación de Datos/QA no cierra la maduración del soporte

El descenso de CLP 88.252.000 a CLP 85.400.000/mes equivale a CLP 2.852.000, un 3,23 %. El anexo lo explica por 66 h de Datos y 37 h de QA que terminan en M25, principalmente asociadas a cierre de migración/retiro del TMS. Los números cuadran, pero ese descenso ya estaba en `Personal!D22:D57` antes del último commit.

La nueva prueba de 930 h de L1 y la guardia describen capacidad de servicio. No justifican una nueva curva de carga ni un descenso posterior del costo de soporte: la nómina queda constante durante M25–M56. Tampoco se documentó como nueva corrección el soporte reforzado posterior a H7 en M16.

**Cierre:** separar cobertura fija necesaria para SLA, refuerzo de cada salida a producción y atención variable por incidencias. Estimar horas y costo por tramo con demanda, tiempo medio, escalamiento y umbrales de reducción. La madurez puede reducir carga variable sin permitir recortar indiscriminadamente un puesto 24×7. Mantener los servicios fijos que realmente sigan siendo necesarios.

Referencias: PROF-04; FEP01 · Artículo 78.2 · p.40; [explicación del refuerzo](/home/axeler8/Escritorio/audIT/outputs/informe3-integral/entrega-consolidada/Cierre-tecnico-D1-D2.md:45); [prueba que confirma valores ya existentes](/home/axeler8/Escritorio/audIT/outputs/informe3-integral/probar_cierre_tecnico.py:86). [AUD-15](https://linear.app/audit-fep/issue/AUD-15), [AUD-26](https://linear.app/audit-fep/issue/AUD-26), [AUD-34](https://linear.app/audit-fep/issue/AUD-34).

### AI3-05 · Alta · Los gráficos de entrega no muestran la corrección solicitada

La presentación conserva en la lámina 4 la Curva S original y en la 5 el déficit y refuerzo históricos. Las nuevas láminas agregan texto; no reemplazan los gráficos con la base corregida. Los PNG separados en UF no se incorporan al PDF/PPTX. Falta en esos entregables el conjunto coherente de egresos mensuales, caja contra cero y entradas/devoluciones de deuda claramente anotadas.

Los picos originales de M13, M17 y M16 se reproducen: CLP 249.763.158, CLP 226.554.448 y CLP 224.519.448, respectivamente. Pero coincidir con un mes de hito no demuestra la atribución de cada costo a instalación, pruebas o puesta en producción. Primero se debe terminar el calendario de costos.

**Cierre:** regenerar Curva S de 56 meses, egresos por mes y caja contra cero desde la misma base; usar UF en las vistas de exposición, con 1 UF = CLP 40.000, y mantener las monedas formales donde correspondan. Señalar desembolsos, aportes, amortizaciones y meses críticos. No dibujar picos ni reducciones arbitrarias para que la curva parezca más realista.

Referencias: PROF-01/03/05; FEP01 · Formulario E-24 · p.73; FEP01 · Formulario T-22, contenido Informe 3 · p.68; Aclaraciones §§5.3–5.4. PDF pp.9 y 24; presentación, láminas 2/4/5/8–10. [AUD-19](https://linear.app/audit-fep/issue/AUD-19), [AUD-12](https://linear.app/audit-fep/issue/AUD-12), [AUD-13](https://linear.app/audit-fep/issue/AUD-13).

### AI3-06 · Media · La documentación final y las fuentes no identifican una sola entrega vigente

El dictamen de la IA todavía inventaría 23 páginas, 34 hojas y 7 láminas y deja pendiente regenerar archivos. Son las dimensiones del corte original; no describen los paquetes agregados de 26/38/9 y 27/42/10. La ficha del PDF, p.3, continúa declarando el nombre anterior y folios 1–23; el índice no incorpora los addenda. La p.27 de activación no tiene folio impreso.

Los scripts leen `c9a6515` desde Git. Ese corte no es ancestro de `main` auditado; ambos divergen desde `8c950fa`. Además, la rama remota `codex/cierre-entrega-3` está en `c948a69`, con cambios posteriores en el anexo de observaciones y documentos técnicos, entre otros archivos. No significa que todas las cifras económicas hayan cambiado, pero debe reconciliarse qué respuestas del Art.46 y qué fuentes se están entregando. En `main` faltan varias fuentes de consolidación que solo existen en esa rama; compilar las fuentes económicas actuales de `main` no equivale a reproducir el paquete anexado.

**Cierre:** fijar el corte y manifiesto de una entrega; conciliar cambios pertinentes de las ramas preservando el trabajo de `main`; actualizar matriz, ficha, índice, versión, referencias, foliado y órdenes de generación. Mantener los antecedentes históricos fuera de la lectura principal o rotularlos de modo inequívoco.

Referencias: FEP01 · Artículo 46° · p.28; [inventario desactualizado](/home/axeler8/Escritorio/audIT/outputs/informe3-integral/Informe-3-Revision-Integral.md:15); [commit auditado](https://github.com/mvergaral/audIT/commit/47f7e7b1717e531fcbed6a171b6ed2023a1552e6); [corte fuente](https://github.com/mvergaral/audIT/commit/c9a6515652c3357ea684bf0bb9338b7c4ec028fd); [rama posterior](https://github.com/mvergaral/audIT/commit/c948a69356b44bbb78d73d71713288911584d27f).

### AI3-07 · Media · Referencias académicas y evidencia de IA pendientes de ordenar

Los nuevos PDF y las láminas contienen «Simulación académica», «contraparte académica» y «Anexos aprobados» con emisor ficticio. Los expedientes distinguen correctamente supuestos, firmas por recabar y ejecución futura: no encontré prueba de que se hayan presentado transferencias o pilotos reales como hechos ocurridos. Sin embargo, esas expresiones académicas son inadecuadas para una propuesta que debe sostener la ficción corporativa. Los borradores y controles de aprobación corresponden al expediente interno.

El Comunicado 09 y el Comunicado 10 §7.1.d identifican las rupturas de ficción y residuos de elaboración. El Comunicado 10 tiene un alcance explícito sobre subdocumentos técnicos: **esta auditoría no extrapola automáticamente una nota cero o inadmisibilidad al documento económico del Informe 3**. Sí recomienda depurar el material de entrega conforme a las instrucciones del repositorio.

Por otra parte, FEP01 Art.93 aclara que las obligaciones son elementos del ejercicio. No debe convertir la corrección del presupuesto en una exigencia de obtener un crédito real o ejecutar físicamente instalaciones futuras. Para el hito corresponden supuestos identificados, cantidades defendibles, condiciones de la oferta y simulaciones coherentes. Un cálculo no equivale a un ensayo medido ni una autorización pendiente a una autorización obtenida.

El commit solo cambia `outputs/informe3-integral/`; no actualiza bitácoras individuales en `Investigacion/`. Sus notas «para A-6» ayudan, pero falta asociarlas al integrante responsable. Esta auditoría agrega su propio [registro para A-6](/home/axeler8/Escritorio/audIT/outputs/auditoria-informe3-47f7e7b/REGISTRO-PARA-A6.md), sin certificar revisión humana ajena.

**Cierre:** separar expediente interno y propuesta; declarar «supuesto de presupuesto» o «escenario condicionado» donde sea necesario, sin presentarlos como hechos medidos; actualizar la declaración/bitácora del responsable y registrar la revisión humana efectivamente realizada.

## 4. Qué sí quedó comprobado y debe conservarse

- **Base histórica:** reproducción separada de 57 cierres, deuda y línea. Diferencia máxima de caja frente a valores guardados: menor a CLP 0,00002. Se confirma giro de CLP 44.999.999,54 en M9, devolución M10 y amortización bancaria M21.
- **Economía original:** costo neto CLP 7.984.400.845,22; venta CLP 9.796.810.853,03; margen EBITDA/ingresos 18,50 %. VAN CLP 1.235.043.315,78 y TIR mensual 83,6613236 %, reproducidos sobre Fila A M1–M56 con M0 = 0. No se atribuyen automáticamente esos indicadores a la variante externalizada.
- **Tasa:** 80 % × 0,9 % mensual + 20 % × [(1 + 20 % anual supuesto)^(1/12) − 1] = 1,02618941 % mensual. El 20 % anual de socios es un supuesto que necesita justificación; no es la tasa ordenada por E-24.
- **Contrato:** 12 hitos en sus meses E-25, reparto 60/40 y 36 facturaciones de operación M21–M56. El cobro de operación llega hasta M57; la base distingue esa cola. Fuentes: FEP01 · E-25 · p.74 y Aclaraciones §§3–4.
- **Instalación:** 182 montajes = 10 pilotos + 172 externos, incluidos 34 comodatos. Cuadran 910 h-persona y CLP 16.258.666,67 de costo interno referencial. Las 210 balizas y sus 52,5 h se mantienen aparte. No se acreditó disponibilidad efectiva de vehículos, viajes o puestos por los cupos simulados.
- **Caja de activación:** el script vuelve a producir CLP 7.867.985 de capital adicional en M9, CLP 6.294.388 de banco y CLP 1.573.597 de socios, 313 registros y 224 comprobaciones de cierre. El mínimo simulado es CLP 10.000.003,78 en M13. Las 313 filas de saldo coinciden con el CSV guardado al centavo. Esto verifica el cálculo bajo sus hipótesis, no las fechas de cobro o la posibilidad de diferir reservas.
- **SLA:** 15 + 30 + 180 = 225 minutos; con recuperación de proveedor de 240 minutos, el total es 285 y excede cuatro horas. Los casos distinguen correctamente ambos resultados. El turno de un mes de 31 días reproduce 930 h. No acredita cobertura anual, ausentismo o recuperación real. FEP01 · Artículo 78.2 · p.40.
- **Criterios prudentes:** conservar la separación Fila A/Fila C, la exclusión del hardware adquirido por Curimón, los beneficios de Curimón separados de cobros de audIT y la identificación como pendientes de beneficios sin respaldo.

Pruebas: [reproducción e inventario](/home/axeler8/Escritorio/audIT/outputs/auditoria-informe3-47f7e7b/evidencia.json), [simulaciones verificadas](/home/axeler8/Escritorio/audIT/outputs/auditoria-informe3-47f7e7b/pruebas-simulacion.json).

## 5. Plan de cierre en orden de dependencia

| Prioridad | Acción concreta | Responsable funcional | Prueba de cierre |
|---|---|---|---|
| P0 | Fijar corte/base y conciliar las fuentes económicas y el Art.46 entre `main` y rama de cierre | D1/D2 | Manifiesto único; fuentes y artefactos identificados sin confundir versiones |
| P0 | Resolver instalación por lote y nómina sustituida/retenida, incluyendo costos/logística del servicio | D2/D4, revisión D1 | Matriz de horas y costos que alimente el modelo; servicio termina por lote; Art.73 tratado |
| P0 | Modelar soporte fijo, refuerzo y demanda decreciente con criterios medibles | D2/D3/D4 | Horas × costo por perfil y tramo; SLA cubierto; reducción justificada |
| P0 | Integrar costos, financiamiento y escenarios mediante fórmulas, eliminando resúmenes congelados | D2, validación D1 | Pruebas de mutación se propagan a caja, mínimos y gráficos; indicadores afectados actualizan |
| P1 | Dimensionar capital con el costo corregido, holgura defendida y atraso H5 a precio fijo | D1/D2 | 56 cierres base positivos sin línea; deuda conciliada; estrés y condiciones explícitos |
| P1 | Regenerar los tres gráficos y vistas principales en UF; marcar crédito, aporte y amortización | D1/D2 | PDF/Excel/láminas concilian para el mismo escenario |
| P2 | Actualizar ficha, índice, folios, matriz Art.46, declaraciones y A-6 | D1 y cada responsable | Paquete legible, corporativo y trazable; revisión humana registrada por quien la hizo |

Los responsables son roles de gobernanza del repositorio, no asignaciones individuales inventadas. No hay una pauta específica verificada que permita convertir esta revisión del Informe 3 en una nota; no se utilizan ponderaciones del Informe 2.

## 6. Registro de verificación y límites

- Git: `status`, `show`, `diff`, `log`, `merge-base`, ramas y `ls-remote` en lectura. Se verificó íntegramente el alcance de 38 archivos del commit y se compararon fuentes relevantes con su corte de generación.
- Bases: consultas por secciones T-22 (contenido del Informe 3, id 247), E-24 (253), E-25 (255), E-26 (256), Arts.46, 57, 73, 78.2 y 93; restricciones del caso y calendario; Aclaraciones y apartados pertinentes de Comunicados 09/10. Algunos encabezados de formularios tienen IDs sin contenido, por eso se usaron las secciones continuadas. No se consultó el corpus completo.
- Archivos: extracción de todas las páginas de los tres PDF del nuevo paquete; inventario de las 38/42 hojas, fórmulas, valores guardados, errores, objetos y validaciones; texto de las 9/10 láminas y sus gráficos XML. Inspección visual dirigida a PDF pp.24–27 y láminas nuevas 8/10. No se afirma QA visual exhaustivo de toda la oferta. Un problema de sustitución tipográfica en Poppler no se elevó a hallazgo: el render alternativo de MuPDF mostró correctamente la p.24.
- Pruebas: caja/deuda base e indicadores reproducidos con un cálculo separado; ejecución de funciones de tesorería/activación y cotejo de las 313 filas del CSV; recálculo completo y dos mutaciones en copias mediante LibreOffice Calc/UNO. No se abrió Microsoft Excel ni se acredita comportamiento específico de ese programa.
- Linear: inventario paginado del proyecto Entrega 3 con archivados: **37 tickets, 28 Done, 6 In Progress y 3 Backlog**; las consultas de comentarios devuelven **112**, sin páginas pendientes. Coincide con el conteo del trabajo auditado. El contenido se revisó por muestreo de las últimas evidencias y con atención a AUD-15/20/34. No se confunde Done con cierre económico: AUD-20 sigue documentando condiciones pendientes y AUD-13 está en Backlog. Evidencia: [linear-verificado.json](/home/axeler8/Escritorio/audIT/outputs/auditoria-informe3-47f7e7b/linear-verificado.json).
- Art.46: se inspeccionó la matriz de 68 filas del corte utilizado y la divergencia con la rama posterior. No se reauditaron exhaustivamente los cierres técnicos de las 68 observaciones contra todos los subdocumentos. Los conteos de respuestas «incorporadas» de la IA no se certifican aquí como cierres independientes.
- Prototipo: se comprobó el enlace presente en PDF p.13; no se repitió la navegación interactiva ni se cronometró una exposición. El último commit no cambia ese prototipo. El audio original no fue aportado: las marcas y citas provienen de la transcripción recibida.
- Productos de esta sesión: solo la carpeta `outputs/auditoria-informe3-47f7e7b/`. Los scripts `inspeccionar.py`, `probar_copias.py` y `recalcular_uno.py` permiten repetir el inventario y las pruebas. Copias recalculadas y renders están en `/tmp/audit-informe3-*`; no son entregables. Las fuentes y el registro A-6 están dentro de esta carpeta interna.

**Decisión sugerida al equipo:** conservar la evidencia económica que pasó las pruebas y utilizar los hallazgos AI3-01 a AI3-07 como lista de corrección. Cerrar primero el modelo y después la presentación. La transcripción da respaldo suficiente para priorizar esas acciones; no hace falta rehacer todo desde cero.
