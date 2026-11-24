# Revisión de consistencia de D2 con la entrega 3.2

Fecha de revisión: 24 de noviembre de 2026.

**S3 y S7 todavía no representan una misma línea base técnica y económica con la planilla 3.2.** Las diferencias principales están en horas y dotación, montaje por terminal, servicio de campo y continuidad operacional. Los ajustes locales mejoran la descripción de las innovaciones y la reversión, pero conservan las curvas antiguas y no están reflejados en los PDF versionados.

Esta revisión identifica **14 hallazgos**, con evidencia y criterio de cierre. Es un informe interno de revisión; no integra la propuesta ni sustituye la bitácora A-6.

## Versiones y alcance

La referencia económica es `outputs/3.2/Entrega-3.2/INFORME3_AUDIT_PLANILLA_3.2_20261115.xlsx`, extraída de `origin/codex/cierre-entrega-3`, commit `a59b9d2a809184b136396e4a61617ebe70f52821`. SHA-256: `7976df5e54cad827b688e9c35a9918631e984b961526f5901a5a25c55fd3247e`.

Se toma esta planilla como la versión entregada indicada por el usuario. El repositorio acredita su contenido, pero no se revisó un comprobante externo de envío.

El contraste abarca S3, T-12 y su matriz; S7, sus anexos gráficos activos, T-14, T-15 y T-18; las observaciones del Art. 46 correspondientes a S3/S7; y las hojas de la planilla relacionadas con estos compromisos. También se revisaron los cambios sin confirmar en `tmp/cierre-entrega-3`.

Hay tres estados que deben distinguirse:

| Estado | Situación observada |
| --- | --- |
| Rama remota | Contiene la planilla 3.2 y las modificaciones posteriores de D1. Es la referencia congelada de esta revisión. |
| `main` local | T-12 y las fuentes principales de S7/T-14/T-15/T-18 coinciden con la rama remota. El párrafo de reversión de S3 difiere. |
| Worktree `tmp/cierre-entrega-3` | Rama local en `c9a6515`, 17 commits atrás del remoto, con cambios sin confirmar en S3, S7 y formularios. T-12 coincide con el remoto. |

No se cambiaron fuentes de la oferta, la planilla, los PDF ni la rama de trabajo. Los archivos bajo `fuentes/` son una copia de consulta del commit remoto.

## Comparación cuantitativa

Las horas de la planilla son **horas internas contratadas**: columna I de `Dotación por perfil`, M1–M20, y columna G de `Soporte por perfil`, M21–M56. Incluyen refuerzos y cierres de la planilla; excluyen el esfuerzo externo que se paga como servicio. Por tanto, las diferencias requieren un puente por tarea, rol y modalidad; no deben corregirse sustituyendo un total sin revisar su composición.

| Magnitud | S7 y T-15 actuales | Planilla 3.2 | Diferencia o consecuencia |
| --- | ---: | ---: | --- |
| Horas de implementación M1–M20 | 93.760 | 99.626,67 | +5.866,67 h internas |
| Pico de implementación | 37 personas/FTE, M13–M17 | 39,230625 FTE equivalentes, M7 | Cambia el máximo y su mes. No permite inferir por sí solo personas físicas. |
| H6/M13 y H7/M16 | 5.920 h/mes | 6.160 h/mes | +240 h en cada mes |
| Horas de operación M21–M56 | 92.160 | 84.606 | −7.554 h internas; además hay servicio externo |
| M21 | 2.560 h | 2.853 h | +293 h, con refuerzos y cierre |
| M22–M24 | 2.560 h/mes | 2.611 h/mes | +51 h/mes |
| M25–M32 | 2.560 h/mes | 2.400 h/mes | 15 FTE equivalentes |
| M33–M44 | 2.560 h/mes | 2.320 h/mes | 14,5 FTE equivalentes |
| M45–M56 | 2.560 h/mes | 2.240 h/mes | 14 FTE equivalentes |
| Mesa N1 | 6 personas, 960 h/mes | 6 agentes + 1 FTE de suplencias, 1.120 h/mes | Falta declarar la reserva en T-15 |
| Campo en operación | 2 personas, 320 h/mes | 80 h/mes internas + visitas y rondas externas | Cambian capacidad, ejecutor y costos |
| Equipos acumulados M9 | 164 | 182 | +18 equipos en el escenario económico |
| Equipos acumulados M18 | 179 | 182 desde M9 | Los calendarios no son equivalentes |

El detalle de los 56 meses está en [comparacion-mensual.csv](datos/comparacion-mensual.csv). Los resultados verificables y las versiones comparadas están en [evidencia-verificada.json](datos/evidencia-verificada.json).

## Hallazgos que afectan el compromiso técnico

### D2 01 Horas y pico de implementación desactualizados

**Prioridad alta.** S7 `contenido.tex`, líneas 196–214, y T-15, líneas 16–71, conservan 93.760 h y un pico de 37 en M13–M17. La suma independiente de `Dotación por perfil!I2:I381` es 99.626,67 h. El máximo mensual es M7, con 6.276,9 h, equivalente a 39,230625 FTE. En M13 y M16 hay 6.160 h, equivalentes a 38,5 FTE.

La diferencia permanece en el worktree local y en el PDF de T-15, páginas 4–5. Actualizar la curva, el resumen de S7 y la distribución por etapa/paquete. Separar dotación base, horas adicionales, horas de montaje sustituidas y contratación externa. Cierre: los meses, etapas y paquetes concilian con la planilla sin doble imputación.

### D2 02 La operación se presenta constante y la planilla usa madurez

**Prioridad alta.** T-15, líneas 78–98, declara 16 personas y 2.560 h mensuales constantes durante 36 meses. La planilla activa `Parámetros corrección!B70=1`, con factores de carga variable de 100 %, 75 %, 50 % y 25 % en B12:B15. `Soporte por perfil` muestra las horas por tramo de la tabla anterior.

S7/T-15 deben distinguir cobertura fija, bolsa variable, cierre M21–M24 y refuerzos de producción. Declarar las condiciones de reducción ya previstas en C70: dos meses sin P1, backlog menor que 10 y demanda dentro de capacidad. Cierre: la disminución de esfuerzo no modifica el SLA ofertado y existe capacidad explícita si no se cumplen las condiciones de reducción.

### D2 03 Falta el FTE de suplencias de mesa N1

**Prioridad alta.** T-15, tabla `t15-operacion`, asigna 960 h/mes a EDT13.1. `Contrato de soporte!B2+B13` suma 1.120 h/mes: seis agentes más un FTE de suplencias y picos. La diferencia contractual es 160 h/mes y 5.760 h en 36 meses.

Incorporar esa reserva y su uso en la tabla y justificación de turnos. Cierre: EDT13.1 concilia a 40.320 h internas en M21–M56 y distingue puestos atendidos de dotación de reemplazo.

### D2 04 Campo pasa de dos personas a supervisión interna y servicio externo

**Prioridad alta.** T-15 compromete dos personas y 320 h/mes para EDT13.3. La 3.2 asigna `Contrato de soporte!B7=80` h internas mensuales, tres visitas correctivas mensuales y dos rondas regionales, con reposiciones y costos externos en `Detalle proveedores D4`, filas 380–426.

`Parámetros corrección!B83=19` fija la salida del técnico de implementación desde M19; la coordinación interna de operación reaparece desde M21 y no equivale a una cuadrilla de terreno. Actualizar roles, responsables, ventanas y escalamiento en S7/T-14/T-15/T-18. Cierre: la capacidad y los traslados del proveedor permiten atender los cinco terminales bajo el SLA, con validación D2/D4 de los supuestos B78:B83.

### D2 05 Dos calendarios de montaje incompatibles

**Prioridad alta.** S3, líneas 945–960, y S7, tabla `7-cobertura`, prevén 10 equipos en M6, 164 acumulados en M9 y 179 en M18. T-14/EDT4.2 y T-18 conservan montaje en M6–M10 y M16–M18. La Gantt activa de plataforma representa esas dos ventanas.

La 3.2 presupuesta 10 pilotos en M6 y 172 montajes externos en M7–M9, repartidos 60/60/52: termina los 182 en M9 y el control B18 indica cero costo de montaje posterior a M9. `Conciliación técnica` ya muestra la diferencia de cobertura; no constituye su resolución.

Para alinear la oferta a la 3.2, justificar disponibilidad de kits, adhesión, paso por terminal y capacidad para completar el escenario temprano. Si esa ejecución no es viable, se necesita una versión económica corregida con montaje, activaciones, comunicaciones e IVA según las ventanas reales. Cierre: una sola curva mensual compartida por S3, S7, formularios, anexos y planilla.

### D2 06 Balizas y lectores sin programación física equivalente

**Prioridad alta.** La 3.2 separa 210 balizas base, 21 de reposición, cinco lectores de portería y 19 equipos a bordo de reposición. B53:B56 asigna 15 min por baliza, montaje en tres meses y dos horas por lector. Son 52,5 h para balizas base y 10 h para lectores.

T-14/EDT12.3 y el cruce local de T-15 aluden a balizas y lectores, pero no detallan una programación por sitio, rendimiento, ejecutor y stock que concilie con estas cantidades. El anexo Art. 46 mantiene PLA-13 pendiente. Cierre: incorporar actividades identificables y reservas, distinguiendo alta inicial, reposición y prueba. No sumar el stock como montaje inicial.

### D2 07 Refuerzos de producción y cierre M21 a M24 fuera de la curva técnica

**Prioridad alta.** B85:B86 presupuestan 160 h SRE y 80 h Software en H6, H7, H11 y H12. La operación incluye además cierre de integraciones/migración: en M21, 66 h de Datos, 37 h de QA, 12 h de Arquitectura y 18 h de Frontend; en los meses siguientes persisten las horas de cierre correspondientes.

T-14 admite EDT6.5/7.2 hasta M24, pero la malla T-15 termina en A25/H12 y no individualiza una estabilización de Etapa 2 que concilie ese esfuerzo. El anexo registra PLA-14 pendiente. Cierre: asignar tarea, responsable, período y capacidad a refuerzos y cierre, separando aceptación H12 de actividades posteriores y evitando sumar nuevamente horas que ya están costeadas.

### D2 08 Innovaciones con alcance anterior en T 14 y anexos

**Prioridad media.** El T-14 remoto y `graficos/ajustes-paquetes.json` conservan «Semirremolque conectado», incluyen kilometraje dentro de la innovación 3 y llaman a la innovación 5 «Bienestar del conductor y descanso en parador seguro». La hoja `Innovaciones`, fila 4, limita INN-3 a acople y registro térmico y ubica el kilometraje en alcance base.

El T-14 local ya corrige esos puntos y explicita preparación M4–M5 para EDT12.2 y talleres M4 para EDT12.5. Es un avance que debe preservarse. Falta propagarlo al JSON que alimenta las figuras, a la EDT/Gantt y a los PDF. Cierre: mismo entregable, aceptación y meses en T-14, T-15, T-19, figuras y atribución económica; separar alcance base de incremento por innovación.

### D2 09 La red sigue sin desagregar los paquetes que gobiernan recursos

**Prioridad alta.** El T-14 contiene 54 paquetes, pero la red mantiene 25 actividades agregadas. A09 y A20 concentran construcción; EDT2.5 aparece «fuera de la red» y EDT7.2 no tiene un nodo propio. El cambio local de A18 describe integración M13–M15 y montaje M16–M18, pero mantiene un solo nodo de 120 días y 40 de holgura.

La tabla local de cruce mejora la identificación de entregables, pero no calcula holgura por tramo ni demuestra la nivelación por perfil. Cierre: desagregar donde haya dependencias o recursos distintos y recalcular precedencias, holguras y ruta crítica; conciliar las tareas resultantes con la 3.2. Corresponde a los pendientes PLA-03 a PLA-08 y PLA-11, según su alcance específico.

### D2 10 T 12 tiene cobertura interna de códigos y mantiene pendientes de cumplimiento

**Prioridad alta para el cierre de la oferta.** Se comprobaron 42 códigos únicos: 28 RF y 14 RNF. Todos aparecen en `trazabilidad-secciones.tex` y `trazabilidad-aceptacion.tex`. Eso acredita cobertura de los códigos propios en esas matrices.

No equivale a una fila de cumplimiento por cada RT de las bases. El anexo mantiene ALC-03 pendiente. Además, RF-003 declara «Sí» pese a depender de adhesión o atestación, y ALC-04 pide distinguir compromiso, evidencia disponible y verificación futura también para RNF-005 y RF-014. Cierre: completar la matriz individual de RT y los estados de evidencia sin atribuir a pruebas futuras resultados ya acreditados. Esta revisión no certifica cumplimiento normativo integral.

### D2 11 Reversión con estados distintos entre remoto local y anexo

**Prioridad media.** El S3 remoto ya remite a T-18/CP-SYS-20, pero mantiene una garantía absoluta de cero pérdida vinculada al buffer. T-18 remoto conserva un párrafo simplificado sobre reinstalación de imagen en el siguiente paso por terminal.

El worktree local mejora ambos textos: añade deduplicación, preservación y conciliación de registros, y distingue retorno A/B de recuperación presencial. El anexo ALC-02 todavía señala que el enlace explícito en S3 está pendiente. Cierre: consolidar la redacción local con el procedimiento y la prueba, comprobar referencias y actualizar el estado del anexo con evidencia. La descripción del procedimiento no demuestra que el ensayo se haya ejecutado.

## Hallazgos de versión y paquete

### D2 12 Los PDF preparados no incluyen las mejoras locales

**Prioridad alta.** El PDF de T-14 aún contiene las denominaciones y criterios anteriores de EDT12.3/12.5; el PDF de T-15 conserva 93.760/92.160 h y la malla agregada. La Gantt de plataforma mantiene montaje M6–M10 y M16–M18. Las diferencias económicas están, por tanto, en los entregables preparados y no solo en comentarios de fuente.

`ARCHIVOS-VIGENTES.md` identifica `S7_Integrado_Revision.pdf` y `preparacion-final/` como documentos vigentes, aunque las fuentes locales ya avanzaron respecto de ellos. Los PDF inspeccionados contienen 46 páginas de S7 y 9/10/6 páginas de T-14/T-15/T-18. Cierre: una vez resuelta la conciliación, regenerar fuentes derivadas, figuras, PDF y manifiesto; revisar contenido exportado y foliación. No basta con que la portada diga versión 3.0 y 25-11-2026.

### D2 13 La propia planilla contiene descripciones heredadas

**Prioridad media.** Los valores y fórmulas vigentes usan B83=19, pero `Feedback 3.2!C7` dice que el técnico sale en M10. `Conciliación técnica!C17` conserva 160 h/mes para M18–M20, mientras `Dotación por perfil` elimina el FTE del técnico desde M19. `Soporte por perfil!J7` sigue describiendo «Dos perfiles» aunque G7 contiene 80 h.

El README de regeneración también conserva una descripción inicial de salida en M10. Cierre: corregir las explicaciones y conciliaciones para que describan los parámetros y fórmulas efectivos. Para esta revisión prevalecen B83 y las horas efectivamente calculadas; no se propone cambiar la planilla entregada durante una revisión de consistencia.

### D2 14 Los respaldos económicos generales no concilian con la 3.2

**Prioridad alta si se incorporan al paquete.** `economico/datos/partidas.csv`, líneas 21–22 y 67–73, conserva venta de implementación CLP 4.618.802.815, venta de operación CLP 5.178.008.038, costos totales CLP 7.984.400.845 y facilidad adicional de CLP 400 millones.

La planilla 3.2 presenta costo CLP 6.820.207.480,34, venta de implementación CLP 4.477.563.339,07, mensualidad CLP 108.077.483,27 por 36 meses y facilidad contingente CLP 420 millones. El README `v32/REGENERAR.md` advierte expresamente que los PDF y presentación de la 3.1 no forman un paquete coherente con esta planilla.

Cierre: identificar qué respaldos son históricos y cuáles acompañarán a la oferta; actualizar los vigentes desde la línea base elegida y comprobar E-21/E-24/E-25/E-26 y narrativa económica con sus responsables. No trasladar a la 3.2 conclusiones de caja de los respaldos antiguos de AUD-14/AUD-15 sin repetir el cálculo pertinente.

## Estado del anexo de observaciones

El anexo `observaciones-informe3.tex` remoto contiene 20 observaciones asignadas a S3/S7: **2 incorporadas, 5 parciales y 13 pendientes**. Son estados declarados en ese archivo; no nuevas calificaciones del revisor.

| Grupo | Incorporadas | Parciales | Pendientes |
| --- | --- | --- | --- |
| S3/T-12 | — | ALC-02 | ALC-01, ALC-03, ALC-04, ALC-05, ALC-06 |
| S7/formularios | PLA-02, PLA-09 | PLA-01, PLA-03, PLA-07, PLA-11 | PLA-04, PLA-05, PLA-06, PLA-08, PLA-10, PLA-12, PLA-13, PLA-14 |

Además de las brechas económicas descritas, esos pendientes incluyen inicio contractual frente a calendario civil, numeración de tablas T-12, redacción autónoma de S3, disponibilidad de usuarios durante temporada de fruta, cierres sucesivos de Los Libertadores y contenido de la Gantt en T-14. Deben conservar su estado hasta comprobar el cambio y su localizador. No se revalidaron aquí todas las exigencias de las bases asociadas a esas observaciones.

## Orden de corrección propuesto

1. **Consolidar el punto de partida de D2.** Preservar los cambios locales y compararlos con el remoto antes de integrar. Conservar la planilla entregada como referencia identificada.
2. **Resolver montaje y servicio de campo con D4.** Son decisiones que cambian calendario, capacidad y pagos. Fijar quién ejecuta cada intervención, en qué terminal y con qué condiciones de adhesión/stock.
3. **Conciliar T-15 con la 3.2.** Preparar el puente mensual de horas base, adicionales, sustituidas y externas. Repartir por tarea, paquete, rol y etapa; actualizar mesa N1, operación y madurez.
4. **Actualizar la red y el relato técnico.** Reflejar las decisiones en S3/S7, T-12/T-14/T-15/T-18, innovaciones y estabilización M21–M24; recalcular las holguras afectadas.
5. **Regenerar anexos y salidas.** Actualizar JSON de gráficos, EDT, Gantt, PDF, manifiestos y referencias. Contrastar los documentos exportados con las fuentes consolidadas.
6. **Cerrar el expediente.** Actualizar Art. 46 por evidencia, registrar este uso de IA en la A-6 del responsable y realizar el cotejo final con el paquete económico que se enviará.

## Comprobaciones y límites de la revisión

Se leyeron valores almacenados y fórmulas de la planilla sin modificarla ni recalcularla. La suma independiente confirmó los totales de horas, la curva mensual, 42 requerimientos únicos, 54 paquetes y cobertura de los códigos propios en ambas matrices. No se encontraron celdas Excel de tipo error en los valores almacenados. Esto no certifica equivalencia de recálculo entre Excel y LibreOffice; el README de la 3.2 mantiene pendiente esa comprobación.

Se extrajo texto de los PDF vigentes de S7 y sus formularios/anexos activos, y se inspeccionaron visualmente la Gantt de plataforma y la página 5 de T-15 para confirmar las diferencias descritas. No se hizo una certificación visual de todas las páginas ni una nueva compilación LaTeX.

La verificación se reproduce con `scripts/verificar_revision.py` usando Python y openpyxl en modo de lectura. `datos/evidencia-verificada.json` conserva el commit, hash, totales y estados comparados. Las correcciones propuestas requieren aplicarse y verificarse en una intervención posterior; esta entrega es la revisión solicitada.
