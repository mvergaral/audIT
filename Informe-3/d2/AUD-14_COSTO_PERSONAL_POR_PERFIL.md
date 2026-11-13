# AUD-14 · Costo de personal por perfil y actividad

## Implementación base, EDT 5 a 8

El reparto de D3 suma **36.800 h** ya consideradas en T-15. Esta valorización preliminar aplica los límites de la columna de costo de E-26 a las horas propuestas y usa CLP 40.000 por UF según E-24. Los importes son costo interno de referencia. La selección de costos por perfil y la asignación mensual quedan pendientes de validación de D2.

| Perfil E-26 | EDT 5 (h) | EDT 6 (h) | EDT 7 (h) | EDT 8 (h) | Total (h) | Costo (CLP/h) | Subtotal bruto (CLP) |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Arquitecto Senior | 320 | 160 | 160 | 240 | 880 | 32.000–56.000 | 28.160.000–49.280.000 |
| Jefe de Desarrollo | 640 | 320 | 160 | 400 | 1.520 | 28.000–56.000 | 42.560.000–85.120.000 |
| Ingeniero Senior (Software) | 5.920 | 2.720 | 320 | 2.400 | 11.360 | 24.000–32.000 | 272.640.000–363.520.000 |
| Ingeniero Senior (Frontend/Móvil) | 4.000 | 320 | 160 | 1.600 | 6.080 | 24.000–32.000 | 145.920.000–194.560.000 |
| Encargado de Seguridad TI | 640 | 320 | 320 | 400 | 1.680 | 32.000–56.000 | 53.760.000–94.080.000 |
| Ingeniero de Datos | 1.600 | 1.280 | 2.400 | 1.200 | 6.480 | 24.000–40.000 | 155.520.000–259.200.000 |
| Analista QA Senior | 3.200 | 960 | 960 | 1.280 | 6.400 | 16.000–24.000 | 102.400.000–153.600.000 |
| Ingeniero DevOps / SRE | 1.280 | 320 | 320 | 480 | 2.400 | 24.000–40.000 | 57.600.000–96.000.000 |
| **Total** | 17.600 | 6.400 | 4.800 | 8.000 | **36.800** | | **858.560.000–1.295.360.000** |

| Actividad | Horas | Costo bruto de referencia (CLP) |
| --- | ---: | ---: |
| EDT 5 · Servicios de la Etapa 1 y portal base | 17.600 | 407.040.000–599.040.000 |
| EDT 6 · Integraciones | 6.400 | 151.040.000–229.120.000 |
| EDT 7 · Datos y migración | 4.800 | 112.000.000–183.040.000 |
| EDT 8 · Servicios de la Etapa 2 | 8.000 | 188.480.000–284.160.000 |

Cálculo por perfil y actividad = horas propuestas × costo horario. Los totales por perfil y por actividad representan el mismo costo. Integrar estas horas una vez en personal y validar sus meses de devengo antes de distribuirlas al flujo.

## Costos horarios y distribución mensual de referencia

Se verificó que los ocho costos horarios elegidos estén dentro de la columna de costo de E-26. Para Software y Frontend/Móvil se propone extender a EDT 5 a 8 los CLP 30.000/h usados en el expediente. Para los demás perfiles se usa el punto medio de E-26 como supuesto de planificación. La verificación confirma conformidad con el rango. D2 todavía debe ratificar estos costos para el presupuesto.

| Perfil | Arquitectura | Liderazgo | Software | Frontend/Móvil | Seguridad | Datos | QA | SRE |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Costo de referencia (CLP/h) | 44.000 | 42.000 | 30.000 | 30.000 | 44.000 | 32.000 | 20.000 | 32.000 |

Se conserva el total de horas por perfil y elemento EDT de D3. La distribución de referencia reparte las horas de cada elemento en proporción al número de subpaquetes activos de T-14 por mes, con igual peso para los subpaquetes. Los redondeos a horas enteras se asignan por mayor residuo y, en empate, al mes más temprano. Para EDT 5 y 8, las ventanas coinciden dentro de cada elemento y el reparto equivale a distribuir sus horas uniformemente. En EDT 6, el tramo M16–M24 corresponde solo a 6.5. En EDT 7 se consideran las ventanas específicas de 7.1, 7.2 y 7.3. Los pesos son un supuesto para construir una primera curva de demanda.

| Mes | Arquitectura | Liderazgo | Software | Frontend/Móvil | Seguridad | Datos | QA | SRE | Total (h) | Costo (CLP) |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| M4 | 7 | 7 | 14 | 7 | 14 | 100 | 40 | 14 | 203 | 6.296.000 |
| M5 | 7 | 7 | 14 | 7 | 14 | 100 | 40 | 14 | 203 | 6.296.000 |
| M6 | 112 | 204 | 1.693 | 876 | 224 | 841 | 926 | 352 | 5.228 | 157.118.000 |
| M7 | 112 | 203 | 1.693 | 875 | 223 | 841 | 926 | 351 | 5.224 | 156.970.000 |
| M8 | 112 | 203 | 1.693 | 875 | 223 | 841 | 926 | 351 | 5.224 | 156.970.000 |
| M9 | 112 | 203 | 1.693 | 875 | 223 | 841 | 925 | 351 | 5.223 | 156.950.000 |
| M10 | 77 | 141 | 1.211 | 813 | 155 | 520 | 720 | 283 | 3.920 | 116.946.000 |
| M11 | 7 | 7 | 14 | 7 | 14 | 100 | 40 | 14 | 203 | 6.296.000 |
| M12 | 7 | 7 | 13 | 7 | 13 | 100 | 40 | 13 | 200 | 6.190.000 |
| M13 | 40 | 67 | 400 | 267 | 67 | 200 | 214 | 80 | 1.335 | 40.772.000 |
| M14 | 40 | 67 | 400 | 267 | 67 | 200 | 214 | 80 | 1.335 | 40.772.000 |
| M15 | 40 | 67 | 400 | 267 | 67 | 200 | 213 | 80 | 1.334 | 40.752.000 |
| M16 | 46 | 78 | 494 | 278 | 78 | 244 | 246 | 91 | 1.555 | 47.532.000 |
| M17 | 46 | 77 | 494 | 277 | 77 | 244 | 246 | 91 | 1.552 | 47.416.000 |
| M18 | 46 | 77 | 494 | 277 | 77 | 244 | 246 | 91 | 1.552 | 47.416.000 |
| M19 | 12 | 18 | 107 | 18 | 24 | 144 | 73 | 24 | 420 | 12.926.000 |
| M20 | 12 | 18 | 107 | 18 | 24 | 144 | 73 | 24 | 420 | 12.926.000 |
| M21 | 12 | 18 | 107 | 18 | 24 | 144 | 73 | 24 | 420 | 12.926.000 |
| M22 | 11 | 17 | 107 | 17 | 24 | 144 | 73 | 24 | 417 | 12.810.000 |
| M23 | 11 | 17 | 106 | 17 | 24 | 144 | 73 | 24 | 416 | 12.780.000 |
| M24 | 11 | 17 | 106 | 17 | 24 | 144 | 73 | 24 | 416 | 12.780.000 |
| **Total** | 880 | 1.520 | 11.360 | 6.080 | 1.680 | 6.480 | 6.400 | 2.400 | **36.800** | **1.111.840.000** |

**Sobrecarga global en M6–M9.** Solo EDT 5 a 8 demandan 5.228, 5.224, 5.224 y 5.223 h, frente a las 4.800 h mensuales de todo el proyecto en T-15. El exceso mínimo es de 1.699 h antes de incorporar otros elementos EDT. El reparto por ventanas sirve para localizar el conflicto. Para nivelarlo, D2 debe estimar la carga de los subpaquetes y verificar cuáles pueden desplazarse sin afectar los hitos.

**Conflicto por perfil en M13–M15.** La distribución de EDT 8 demanda 400 h/mes de Software y 267 h/mes de Frontend/Móvil en esos tres meses. T-15 reserva en E2 160 h/mes para cada uno de esos roles. D2 debe revisar qué tareas puede asumir el equipo full-stack y qué demanda debe redistribuir. Tampoco se ha conciliado la carga de los demás elementos EDT ni las horas de innovación con la disponibilidad de cada perfil.

**Cierres M21–M24.** La curva de demanda deja 1.669 h (51.296.000 CLP de referencia) en 6.5 y 7.2 después del cierre de la curva de implementación de T-15 en M20. Se mantienen identificadas en este subtotal para conservar la trazabilidad con D3. Antes de integrarlas al flujo, D2 debe asignarlas a capacidad de operación o reprogramarlas y conciliar su costo con el presupuesto base.

Fuente de ventanas: [T-14, elementos 5 a 8](https://github.com/mvergaral/audIT/blob/4da4195/recursos/Formato-Oferta-audIT/subdocumentos/07-plan-trabajo/formularios/T-14.tex#L44). Fuente de capacidad: [T-15, asignación por escuadra](https://github.com/mvergaral/audIT/blob/4da4195/recursos/Formato-Oferta-audIT/subdocumentos/07-plan-trabajo/formularios/T-15.tex#L105).

## Desglose preliminar por subpaquete, M6–M9

D3 entrega horas por elemento y perfil. La tabla conserva el reparto mensual anterior y divide cada elemento entre sus subpaquetes activos según el mismo supuesto de igual peso. Las diferencias de una hora distribuyen los residuos del redondeo. El desglose sirve para preparar la revisión con los responsables de Desarrollo, Integración y Datos.

| Subpaquete | Actividad | M6 (h) | M7 (h) | M8 (h) | M9 (h) | Total (h) |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| 5.1 | Personas y cumplimiento | 503 | 503 | 503 | 503 | 2.012 |
| 5.2 | Flota y activos | 503 | 503 | 503 | 503 | 2.012 |
| 5.3 | Planificación y tráfico | 503 | 503 | 503 | 503 | 2.012 |
| 5.4 | Telemetría y geocercas | 503 | 503 | 503 | 503 | 2.012 |
| 5.5 | Operación de fletes | 503 | 503 | 503 | 503 | 2.012 |
| 5.6 | Liquidación y costeo | 503 | 503 | 503 | 503 | 2.012 |
| 5.7 | Portal del transportista | 502 | 502 | 502 | 502 | 2.008 |
| **EDT 5** | | **3.520** | **3.520** | **3.520** | **3.520** | **14.080** |
| 6.1 | Interfaz contable | 222 | 221 | 221 | 221 | 885 |
| 6.2 | Plataformas de posicionamiento | 222 | 221 | 221 | 221 | 885 |
| 6.3 | Telemetría de fábrica y tacógrafos | 222 | 221 | 221 | 221 | 885 |
| 6.4 | Combustible, peaje y taller | 221 | 221 | 221 | 220 | 883 |
| 6.5 | Capa anticorrupción y retiro del legado | 221 | 220 | 220 | 220 | 881 |
| **EDT 6** | | **1.108** | **1.104** | **1.104** | **1.103** | **4.419** |
| 7.1 | Migración de vigencias | 200 | 200 | 200 | 200 | 800 |
| 7.2 | Migración histórica | 200 | 200 | 200 | 200 | 800 |
| 7.3 | Repositorio analítico | 200 | 200 | 200 | 200 | 800 |
| **EDT 7** | | **600** | **600** | **600** | **600** | **2.400** |
| **Demanda parcial** | | **5.228** | **5.224** | **5.224** | **5.223** | **20.899** |
| Capacidad global de T-15 | | 4.800 | 4.800 | 4.800 | 4.800 | 19.200 |
| **Exceso mínimo** | | **428** | **424** | **424** | **423** | **1.699** |

### Opciones para revisar la carga

- **7.3, repositorio analítico:** la ventana de T-14 empieza en M4. Revisar qué tareas de diseño y preparación pueden adelantarse a M4–M5 y cuáles dependen de A07 o de los datos de A09. Aun si se adelantaran las 800 h asignadas a 7.3 en M6–M9, quedaría un exceso mínimo de 899 h en ese tramo.
- **5.1–5.7, servicios de Etapa 1:** validar en qué sprint se entrega cada componente y qué trabajo puede quedar en M10 antes de H4. La demanda parcial en M10 es de 3.920 h frente a 5.280 h globales. La diferencia de 1.360 h debe conciliarse con las demás actividades, la disponibilidad por perfil y la fecha efectiva de A09.
- **6.1–6.5 y 7.1:** conservar las ventanas de integración y verificación documental. La ventana posterior de 6.5 corresponde al retiro del legado. Cualquier traslado de trabajo desde M6–M9 requiere identificar que se trata de alcance de retiro y que cabe en la carga del mes de destino.

D2 debe pedir a Desarrollo, Integración y Datos horas por perfil y subpaquete, con hitos o dependencias que fijen su mes. Priorizar 7.3 y las entregas de A09, que son las primeras opciones para comprobar cuánto trabajo puede adelantarse o concentrarse al cierre de la ventana.

Fuentes: [T-14, ventanas de los subpaquetes 5.1–7.3](https://github.com/mvergaral/audIT/blob/4da4195/recursos/Formato-Oferta-audIT/subdocumentos/07-plan-trabajo/formularios/T-14.tex#L44) · [T-15, capacidad mensual](https://github.com/mvergaral/audIT/blob/4da4195/recursos/Formato-Oferta-audIT/subdocumentos/07-plan-trabajo/formularios/T-15.tex#L36) · [T-15, dependencias de A08–A10](https://github.com/mvergaral/audIT/blob/4da4195/recursos/Formato-Oferta-audIT/subdocumentos/07-plan-trabajo/formularios/T-15.tex#L200).

### Verificación contra A05, A07, A09 y G13

| Opción | Resultado del cruce | Dato para decidir |
| --- | --- | --- |
| Adelantar trabajo de 7.3 a M4–M5 | T-14 abre la ventana de 7.3 en M4 y lo vincula a A09. La red de T-15 fija H2 (arquitectura y modelo de datos) en el día hábil 76 y H3 (ambientes y observabilidad) en el 112. A09 empieza después de H3. Solo se considera candidato el trabajo preparatorio que pueda ejecutarse con los insumos disponibles antes de H3. | Datos debe indicar qué diseño, contratos de datos o especificación de pruebas pueden adelantarse, con horas por perfil y dependencia de H2. Construcción y pruebas que requieran los ambientes se mantienen después de H3. |
| Concentrar trabajo de A09 en M10 | T-15 fija G13 al día 182 y H4 al día 192. S6 exige que G13 congele en PREPROD los flujos de acceso/privacidad, asignación, jornada, alerta y conectividad. Solo se puede evaluar para el sprint 8 trabajo que no sea necesario para liberar esos flujos, con entrega y pruebas antes de H4. | Desarrollo debe identificar las tareas del sprint 8, horas por perfil y carga ya comprometida en ese sprint. |

Con el reparto actual, EDT 5 y 6 consumen 18.499 de las 19.200 h globales de M6–M9. Quedarían como máximo 701 h para EDT 7 y el resto del proyecto. Adelantar 800 h de 7.3 sigue siendo un límite hipotético. La diferencia mensual de 1.360 h en M10 tampoco acredita capacidad en el sprint 8, porque incluye el mes completo y otros frentes. Con los documentos disponibles no se puede confirmar un traslado de horas concreto. Se conserva la curva como diagnóstico hasta obtener el desglose de las tareas y su carga por perfil.

Fuentes: [T-15, red de precedencias e hitos](https://github.com/mvergaral/audIT/blob/4da4195/recursos/Formato-Oferta-audIT/subdocumentos/07-plan-trabajo/formularios/T-15.tex#L198) · [S6, alcance y condiciones de G13](https://github.com/mvergaral/audIT/blob/4da4195/recursos/Formato-Oferta-audIT/subdocumentos/06-metodologias/contenido.tex#L221).

### Respuesta de D3 · Reservas de 7.3 y sprint 8

D3 entregó dos reservas dentro de las horas ya presupuestadas. La primera identifica la preparación de 7.3 que puede realizarse sin los ambientes de H3. La segunda identifica las tareas de cierre de A09 entre G13 y H4. El cruce mantiene los totales de 4.800 h de EDT 7 y 17.600 h de EDT 5.

| Perfil | 7.3 M4 (h) | 7.3 M5 (h) | A09 sprint 8 (h) |
| --- | ---: | ---: | ---: |
| Arquitectura | 16 | 8 | 16 |
| Liderazgo | 8 | 8 | 32 |
| Software | 8 | 16 | 240 |
| Frontend/Móvil | 0 | 0 | 160 |
| Seguridad | 16 | 8 | 32 |
| Datos | 48 | 96 | 80 |
| QA | 16 | 32 | 160 |
| SRE | 16 | 24 | 80 |
| **Total** | **128** | **192** | **800** |

**Cruce con la curva de AUD-14.** La curva ya asigna 203 h a 7.3 en cada uno de M4 y M5 y 3.520 h de A09 a M10. Las reservas de D3 identifican parte de esas cargas, por lo que no se descuentan automáticamente 1.120 h del exceso de M6–M9. La comparación sí detecta cambios por perfil. Frente a la curva, M4 requiere reservar 9 h más de Arquitectura, 1 h más de Liderazgo, 2 h más de Seguridad y 2 h más de SRE. M5 requiere 1 h más de Arquitectura, 1 h más de Liderazgo, 2 h más de Software y 10 h más de SRE. D2 debe conciliar esos cambios con la carga de los mismos perfiles y ubicar el resto de 7.3.

**Sprint 8.** Las 800 h incluyen el cierre de costeo, liquidación y consultas del portal, la regresión de construcción y la entrega de H4. En 10 días hábiles equivalen a 10 jornadas completas de diez días, entre ellas 3 personas de Software, 2 de Frontend/Móvil y 2 de QA. D2 debe comprobar la capacidad neta por perfil en esa ventana y ubicar las 16.800 h restantes de A09. La versión de capacitación de G13 y la certificación independiente de A12/H5 mantienen sus propias condiciones.

Fuente: D3, «Respuesta a D2: preparación de 7.3 y cierre de A09», 12 de noviembre de 2026.

### Capacidad de A09 por sprint

La siguiente tabla resta la reserva de D3 para el sprint 8 de las horas por perfil de EDT 5. El promedio de los siete sprints anteriores sirve para medir demanda hasta contar con estimaciones por incremento.

| Perfil | EDT 5 (h) | Sprints 1–7 (h) | Promedio por sprint 1–7 (h) | Sprint 8 (h) | Personas mínimas en sprint 8, a 80 h brutas |
| --- | ---: | ---: | ---: | ---: | ---: |
| Arquitectura | 320 | 304 | 43,4 | 16 | 1 |
| Liderazgo | 640 | 608 | 86,9 | 32 | 1 |
| Software | 5.920 | 5.680 | 811,4 | 240 | 3 |
| Frontend/Móvil | 4.000 | 3.840 | 548,6 | 160 | 2 |
| Seguridad | 640 | 608 | 86,9 | 32 | 1 |
| Datos | 1.600 | 1.520 | 217,1 | 80 | 1 |
| QA | 3.200 | 3.040 | 434,3 | 160 | 2 |
| SRE | 1.280 | 1.200 | 171,4 | 80 | 1 |
| **Total** | **17.600** | **16.800** | **2.400** | **800** | |

**Sprints 1–7, días 112–182.** Con meses contractuales de 20 días, quedan 68 días en M6–M9 con 30 personas y 2 días en M10 con 33. El techo bruto de todo el proyecto es **16.848 h** (68 × 30 × 8 + 2 × 33 × 8). Si se calendarizaran las **16.800 h** restantes de EDT 5 íntegramente en esos sprints, quedarían solo **48 h brutas para todos los demás frentes**. A08 y A10 también se ejecutan en esta ventana. El supuesto de concentrar toda esa carga en A09 requiere revisar qué incluyen las horas de EDT 5, su calendario y la dotación. Dividirlas entre siete sprints no resuelve la concurrencia.

**Sprint 8, días 182–192.** Las 800 h equivalen a 10 personas a jornada completa en bruto. Software, Frontend/Móvil y QA requieren al menos 3, 2 y 2 personas respectivamente a 80 h por persona. Si las 800 h representaran esfuerzo neto de historias, incluso con foco 1 y sin ausencias ni guardias el factor 0,85 de T-10 dejaría un máximo de 68 h netas por persona. Los mínimos por separado subirían a 4 de Software, 3 de Frontend/Móvil y 3 de QA. Para comprobar el escenario real, D2 debe distinguir horas brutas de esfuerzo neto y obtener disponibilidad del equipo y foco de E1 para esos diez días. T-10 explicita 0,70 para E2.

**Conciliación para AUD-14.** Revisar con D3 qué horas de EDT 5 corresponden a ejecución de historias de A09 y cuáles son dedicaciones presupuestadas en otro momento dentro del mismo elemento. Luego conciliar las horas de los siete incrementos de T-10 con las tareas simultáneas de A08/A10 y con la capacidad por persona del sprint 8. Conservar G13 y H4 como límites de la propuesta.

Fuentes: [T-15, dotación mensual y mes contractual](https://github.com/mvergaral/audIT/blob/4da4195/recursos/Formato-Oferta-audIT/subdocumentos/07-plan-trabajo/formularios/T-15.tex#L25) · [T-15, A08–A10 y G13](https://github.com/mvergaral/audIT/blob/4da4195/recursos/Formato-Oferta-audIT/subdocumentos/07-plan-trabajo/formularios/T-15.tex#L200) · [T-10, incrementos y capacidad neta](https://github.com/mvergaral/audIT/blob/4da4195/recursos/Formato-Oferta-audIT/subdocumentos/06-metodologias/formularios/T-10.tex#L71).

### Cruce con la matriz de D3 para A09-1 a A09-7

D3 ubica las 16.800 h completas en los siete primeros sprints, con 2.400 h en cada uno, y mantiene las 800 h de A09-8. El cruce verifica las sumas por sprint y perfil. Para convertir la matriz a meses se prorratean linealmente las horas de cada perfil según los días hábiles del sprint que caen en cada mes. El resultado sustituye la distribución uniforme anterior de EDT 5 para analizar capacidad. Los costos horarios y el total presupuestado por perfil se conservan.

| Mes | Arquitectura | Liderazgo | Software | Frontend/Móvil | Seguridad | Datos | QA | SRE | EDT 5 (h) |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| M6 | 51,2 | 76,8 | 716,8 | 358,4 | 89,6 | 192 | 281,6 | 153,6 | 1.920 |
| M7 | 99,2 | 177,6 | 1.854,4 | 953,6 | 166,4 | 448 | 774,4 | 326,4 | 4.800 |
| M8 | 81,6 | 176 | 1.707,2 | 1.100,8 | 160 | 400 | 854,4 | 320 | 4.800 |
| M9 | 65,6 | 161,6 | 1.292,8 | 1.292,8 | 172,8 | 432 | 1.020,8 | 361,6 | 4.800 |
| M10 | 22,4 | 48 | 348,8 | 294,4 | 51,2 | 128 | 268,8 | 118,4 | 1.280 |
| **Total** | **320** | **640** | **5.920** | **4.000** | **640** | **1.600** | **3.200** | **1.280** | **17.600** |

| Mes | EDT 5 actualizado (h) | EDT 6 y 7, curva preliminar (h) | Demanda parcial (h) | Capacidad global T-15 (h) | Exceso parcial (h) |
| --- | ---: | ---: | ---: | ---: | ---: |
| M6 | 1.920 | 1.708 | 3.628 | 4.800 | 0 |
| M7 | 4.800 | 1.704 | 6.504 | 4.800 | 1.704 |
| M8 | 4.800 | 1.704 | 6.504 | 4.800 | 1.704 |
| M9 | 4.800 | 1.703 | 6.503 | 4.800 | 1.703 |
| M10 | 1.280 | 400 | 1.680 | 5.280 | 0 |

El exceso mensual de la demanda parcial se concentra ahora en M7–M9 y suma **5.111 h** con las estimaciones actuales de EDT 6 y 7. Las diferencias de M6 y M10 corresponden a meses completos y requieren verificar fechas, perfiles y otros frentes antes de usarlas. En la ventana exacta hasta G13 el cruce anterior sigue dejando 48 h brutas para el resto del proyecto. A08, A10 y A11 se ejecutan en paralelo.

La siguiente revisión conjunta debe cuantificar qué esfuerzo es necesario en cada incremento y comprobar si se solapa con partidas de integración, datos, QA independiente o implantación. Si el esfuerzo se confirma, comparar dotación adicional por perfil con una reprogramación compatible con G13 y H4 antes de fijar el flujo. La matriz acredita el reparto presupuestario y deja pendiente la nivelación.

Fuente: D3, «Desglose preliminar de EDT 5 por sprint y perfil», 12 de noviembre de 2026.

### Escenario con la revisión de D3 por tareas en A09-2 a A09-6

D3 reestimó Software, Frontend/Móvil y QA de construcción para los sprints 2–6. El catálogo identifica 3.056 h frente a las 9.104 h de la matriz previa. La diferencia de 6.048 h queda pendiente de conciliar con el alcance y el presupuesto. El escenario sustituye solo esas columnas y conserva las demás horas como supuestos. El subtotal condicional de EDT 5 es 11.552 h, incluido el sprint 8.

| Mes | EDT 5 en escenario parcial (h) | EDT 6 y 7, curva preliminar (h) | Demanda parcial (h) | Capacidad global T-15 (h) | Exceso parcial (h) |
| --- | ---: | ---: | ---: | ---: | ---: |
| M6 | 1.920 | 1.708 | 3.628 | 4.800 | 0 |
| M7 | 2.737,6 | 1.704 | 4.441,6 | 4.800 | 0 |
| M8 | 2.291,2 | 1.704 | 3.995,2 | 4.800 | 0 |
| M9 | 3.323,2 | 1.703 | 5.026,2 | 4.800 | 226,2 |
| M10 | 1.280 | 400 | 1.680 | 5.280 | 0 |

Se aplica el mismo prorrateo por días hábiles del cruce anterior. El exceso parcial pasa de 5.111 h a 226,2 h en M9 bajo este escenario. La comparación aún excluye otros frentes y usa dotación agregada. El sprint 7 conserva 2.400 h provisionales, de las cuales 1.920 h caen en M9 con este prorrateo. D2 debe revisar primero ese sprint por su impacto en M9 y G13. El cruce debe incluir las pruebas de sistema e integración de 10.1 que correspondan durante A09, además de verificar la carga por perfil y los paquetes que cubren los trabajos excluidos de la aplicación. Mantener este escenario como diagnóstico hasta conciliarlo con T-15 y el presupuesto común.

Fuente: D3, «Revisión de Software, Frontend y QA en los sprints 2–6», 12 de noviembre de 2026.

### Sprint 7 · Trabajo y pruebas requeridos para G13

| Trabajo de cierre | Evidencia para G13 | Imputación a conciliar |
| --- | --- | --- |
| Acceso, privacidad y permisos del transportista | Acceso permitido y rechazo auditado, con concesión y revocación verificadas. Casos CP-SEC-04/05. | EDT 5 cubre el incremento aplicativo. Cruzar con 3.2 para controles de plataforma y con EDT 10 para la ejecución transversal. |
| Asignación elegible, jornada y descanso | Reserva válida, bloqueo de asignación inválida y motivo de decisión registrado. CP-UNIT-01/02, CP-SYS-01/05 y CP-INT-03. | Los sprints 1–3 ya contienen identidad, jornada y asignación. En el sprint 7 identificar integración en PREPROD, regresión y correcciones concretas. |
| Alerta de conducción | Caso sintético de 4 h 15 min y área segura a 35 min, con aviso antes de cinco horas. CP-UNIT-18. | Identificar en EDT 5 la parte aplicativa y conciliar con 4.1 la prueba física CP-HW-06. |
| Conectividad intermitente | Reinicio y reenvío doble con evento íntegro y sin duplicados. CP-UNIT-23. | Conciliar el consumo de eventos de EDT 5 con 4.1 y la prueba física CP-HW-03. |
| Congelamiento del candidato y material | Versión, configuración y digest de PREPROD, datos ficticios, evidencia de ejecución, acta y material por perfil. | EDT 5 cubre la entrega técnica. La impartición y evaluación de la capacitación corresponden a A13. |

**Límite parcial en M9.** Sin las 1.920 h prorrateadas del sprint 7, EDT 5–7 suman 3.106,2 h en ese mes. Quedan como máximo 1.693,8 h para el sprint 7 y los demás frentes que aún faltan incorporar. Si se mantiene el prorrateo de 8 días de 10, el máximo matemático para el sprint completo sería **2.117,25 h**, frente a las **2.400 h** de la bolsa preliminar. La diferencia de **282,75 h** mide el ajuste mínimo de ese escenario si se modifica únicamente el sprint 7. La capacidad real será menor cuando se añadan las demás actividades de M9.

Para nivelar, D2 debe identificar por cada fila el trabajo ya entregado en sprints anteriores, las correcciones o integraciones pendientes, el perfil ejecutor y las horas para obtener la evidencia. Las pruebas requeridas y el congelamiento deben completarse antes de G13. La revisión debe evitar cargar dos veces la preparación de un mismo caso y conservar las ejecuciones que correspondan a cada nivel y ambiente.

Fuentes: [T-10, alcance de A09-7](https://github.com/mvergaral/audIT/blob/4da4195/recursos/Formato-Oferta-audIT/subdocumentos/06-metodologias/formularios/T-10.tex#L79) · [S6, cinco flujos y evidencia de G13](https://github.com/mvergaral/audIT/blob/4da4195/recursos/Formato-Oferta-audIT/subdocumentos/06-metodologias/contenido.tex#L221) · [T-17, trazabilidad de pruebas](https://github.com/mvergaral/audIT/blob/4da4195/recursos/Formato-Oferta-audIT/subdocumentos/09-calidad/formularios/trazabilidad-T-17.tex#L27).

#### Conciliación interna D2 · Acceso, jornada y asignación

| Flujo | Trabajo previsto antes del sprint 7 | Trabajo que corresponde identificar en el candidato G13 |
| --- | --- | --- |
| Acceso por rol y privacidad | A09-1 incluye maestros, permisos y roles (RF-005/RF-022). La estimación de A09-1 aún está agregada por perfil. | Probar en PREPROD el acceso por rol, la denegación y el registro de concesión/revocación. Identificar los ajustes de adhesión o consentimiento que correspondan a RF-026. |
| Jornada y descanso | REV-S2-01 (144 h) recibe y vincula evidencia; REV-S2-02 (192 h) implementa atestación externa y sus errores. | Ejecutar escenarios de jornada y descanso sobre el candidato, verificar la decisión y su motivo y estimar correcciones concretas. |
| Asignación elegible | REV-S3-01 (224 h) implementa el veredicto; REV-S3-02 (176 h) distingue modalidades; REV-S3-03 (192 h) controla la confirmación y concurrencia. | Probar reserva válida y bloqueos con evidencia de jornada y activos en el candidato integrado. Presupuestar ejecución y correcciones donde correspondan. |

Las cinco tareas detalladas de los sprints 2 y 3 suman **928 h** de Software, Frontend/Móvil y QA ya identificadas en el escenario parcial. Esas horas sirven para delimitar la construcción previa. La bolsa de 2.400 h del sprint 7 carece de detalle por tarea para determinar cuánto de ese trabajo contiene. El ajuste se calcula al estimar integración, regresión, correcciones y evidencia de G13 por perfil, junto con alerta, conectividad y congelamiento. Las ejecuciones transversales deben conciliarse con 10.1.

Fuente: D3, «Revisión de Software, Frontend y QA en los sprints 2–6», tareas REV-S2-01/02 y REV-S3-01/02/03. [T-10, incrementos A09](https://github.com/mvergaral/audIT/blob/4da4195/recursos/Formato-Oferta-audIT/subdocumentos/06-metodologias/formularios/T-10.tex#L73) · [S6, criterios de G13](https://github.com/mvergaral/audIT/blob/4da4195/recursos/Formato-Oferta-audIT/subdocumentos/06-metodologias/contenido.tex#L221).

#### Estimación preliminar de D2 para el sprint 7

Se propone una estimación de asignación técnica en bloques de 8 h. Supone que acceso, asignación y jornada llegan implementados desde los sprints 1–3, que la aplicación de flota y consumo de eventos del sprint 4 está disponible, y que PREPROD, datos de prueba y contratos están disponibles para el candidato. Cada fila de flujo incluye la prueba focalizada y sus ajustes previstos. La regresión conjunta cubre interacciones entre flujos. Los bloques son estimaciones de D2 para revisión, sujetas a confirmar el alcance pendiente y la disponibilidad.

| Tarea | Alcance | Arq. | Líder | Software | Frontend | Seguridad | Datos | QA | SRE | Total (h) |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Adhesión y consentimientos (RF-026) | Completar flujo y validar concesión/revocación en el candidato | 8 | 8 | 64 | 56 | 16 | 0 | 32 | 0 | 184 |
| Acceso y privacidad | Integrar configuración de roles, ejecutar casos y corregir defectos del candidato | 0 | 0 | 16 | 8 | 16 | 0 | 16 | 8 | 64 |
| Asignación, jornada y descanso | Integrar datos y flujos, ejecutar escenarios y corregir defectos del candidato | 8 | 0 | 32 | 16 | 0 | 16 | 24 | 0 | 96 |
| Alerta de conducción (RF-027) | Completar comportamiento aplicativo y verificar el escenario de alerta | 8 | 0 | 40 | 24 | 0 | 0 | 24 | 8 | 104 |
| Conectividad intermitente | Verificar reinicio, reenvío e idempotencia en PREPROD | 0 | 0 | 24 | 8 | 0 | 8 | 24 | 16 | 80 |
| Regresión del candidato | Ejecutar regresión conjunta y corregir defectos entre flujos | 0 | 8 | 40 | 24 | 8 | 8 | 40 | 8 | 136 |
| Congelamiento y evidencia | Preparar datos y material técnico, registrar versión, configuración, acta y digest | 8 | 16 | 8 | 8 | 0 | 8 | 16 | 16 | 80 |
| **Total (h)** | | **32** | **32** | **224** | **144** | **40** | **40** | **176** | **56** | **744** |

El costo interno referencial es **CLP 22.144.000** con las tarifas de este documento. Si se usa esta estimación en el escenario parcial y se mantiene el prorrateo de 8 de los 10 días en M9, entran **595,2 h** de este sprint en M9. La demanda parcial de EDT 5–7 en ese mes baja a **3.701,4 h**, con una diferencia de **1.098,6 h** respecto de la capacidad global de T-15. Esa diferencia aún debe cubrir las demás actividades de M9 y conciliarse por perfil.

Las 224 h de Software, 144 h de Frontend y 176 h de QA requieren, como mínimo bruto a 80 h por persona en diez días, 3, 2 y 3 personas respectivamente. D2 debe revisar el calendario real por persona, las asignaciones simultáneas y el tratamiento de capacidad neta de T-10. Mantener identificadas la ejecución transversal de 10.1, las pruebas físicas de 4.1 y la impartición de A13. Validar la cobertura del catálogo antes de incorporar esta estimación al presupuesto común.

### Consolidación de carga de M9

Se toma el escenario de 744 h para el sprint 7 y se incorporan las partidas de M9 que tienen una estimación mensual identificable. El cruce mide demanda de personal. La imputación económica de las innovaciones se concilia en sus respectivas fichas.

| Trabajo en M9 | Horas para el cruce | Respaldo y condición |
| --- | ---: | --- |
| EDT 5–7 | 3.701,4 | Escenario parcial de A09, integraciones y datos de este documento. Incluye la parte de M9 del sprint 7. |
| EDT 4.2, montaje a bordo | 260 | Referencia de 52 altas × 5 h-persona. Incluye 138 h 40 min de Técnico instalador y 121 h 20 min de Analista de implantación. Conciliar con agenda y carga del piloto A11. |
| EDT 12.1, expediente | 144 | JSON de D3. Software 64 h, Frontend/Móvil 24 h, Seguridad 16 h, Datos 16 h y QA 24 h. |
| EDT 12.2, programación de patio | 32 | JSON de D3. Software 8 h, QA 16 h y SRE 8 h. |
| **Demanda identificada** | **4.137,4** | |
| Capacidad global T-15 | 4.800 | 30 personas × 160 h en M9. |
| **Diferencia para las partidas pendientes** | **662,6** | Antes de completar las actividades restantes y la disponibilidad por perfil. |

El cruce incorpora **40 h de QA de innovaciones** y **72 h de Software de innovaciones**, además de la carga de construcción incluida en EDT 5. D2 debe comprobar si coinciden en fechas y personas con las pruebas y entregas de A09.

| Partida pendiente | Comprobación de D2 para M9 |
| --- | --- |
| EDT 10.1, pruebas de sistema e integración | T-14 vincula 10.1 con A09 y A12, entre otras actividades. En M9 registrar solo las ejecuciones transversales de A09 que tengan una ventana y un responsable identificados. Distinguirlas de las pruebas focalizadas y la regresión de construcción ya consideradas para G13. A12 empieza en el día hábil 192, en M10. Falta asignar horas por ejecución y perfil para M9. |
| Equipamiento y terreno | Confirmar qué carga adicional de A11 queda fuera de los montajes ya considerados, incluidas homologación, balizas y presencia de terreno. La programación de 52 altas se mantiene como referencia. |
| Capacitación y adopción | A13 empieza con G13, día 182, en M10. En M9 conciliar el material técnico de G13 ya incluido en A09 y revisar si existe trabajo preparatorio separado de implantación con carga propia. |
| Innovaciones y gestión | Identificar la carga de M9 para 12.4 y 12.5, los demás trabajos simultáneos y sus perfiles. D1 informa 300 h de desarrollo para la innovación 5 en M4–M9 sin distribuirlas por mes en el insumo revisado. |

Fuentes: [T-14, paquetes 10.1, 11.1 y 12](https://github.com/mvergaral/audIT/blob/4da4195/recursos/Formato-Oferta-audIT/subdocumentos/07-plan-trabajo/formularios/T-14.tex#L67) · [T-15, secuencia A09–A13](https://github.com/mvergaral/audIT/blob/4da4195/recursos/Formato-Oferta-audIT/subdocumentos/07-plan-trabajo/formularios/T-15.tex#L202) · [JSON D3](https://github.com/mvergaral/audIT/blob/993fa514357085fb75b79a329de0e5c278507233/Informe-3/d3/datos/presupuesto_d3.json) · [Respaldo de montajes base](APORTE_ECONOMICO_INNOVACIONES_1_Y_4.md) · [Aporte de D1](https://github.com/mvergaral/audIT/blob/993fa514357085fb75b79a329de0e5c278507233/Informe-3/d1/ECONOMICO_SUPUESTOS_Y_PARAMETROS_D1.md).

#### Estimación preliminar de M9 para pruebas transversales de 10.1

D2 propone reservar horas para cinco bloques de ejecución sobre interfaces y componentes integrados. T-17 proporciona los casos. La agrupación en M9 y las horas son supuestos de planificación de D2. Se requiere que las interfaces y los datos de prueba estén disponibles dentro del mes. La reserva cubre preparación de la ejecución integrada, ejecución, evidencia y una repetición ordinaria. Las correcciones de código se concilian con las partidas de construcción o integración que ya las cubran.

| Bloque | Ejecución propuesta | QA (h) | Software (h) | Datos (h) | SRE (h) | Total (h) |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| Interfaz con TMS 2013 | CP-INT-05/06, probar conector y enrutamiento con el adaptador de integración | 16 | 8 | 8 | 8 | 40 |
| Posicionamiento de terceros | CP-INT-07/08, verificar normalización y accesos en la interfaz habilitada | 16 | 8 | 8 | 8 | 40 |
| Visita, espera y conformidad | CP-SYS-03/04 y CP-INT-20, ejecutar recorrido integrado con geocerca y entrega | 24 | 16 | 0 | 8 | 48 |
| Despacho con documento contable | CP-SYS-06, verificar el bloqueo con documento y datos provenientes de la interfaz | 24 | 8 | 0 | 8 | 40 |
| Vigencias documentales | CP-SYS-08, verificar el bloqueo usando el padrón de prueba conciliado | 16 | 8 | 8 | 0 | 32 |
| **Total** | | **96** | **48** | **24** | **32** | **200** |

La ejecución de vigencias usa el padrón conciliado y comprueba el bloqueo de extremo a extremo. El candidato G13 ya incluye escenarios de asignación y jornada con datos ficticios. Si ambos registros corresponden a una misma ejecución, descontar el esfuerzo compartido una vez identificados caso, datos y ambiente. Aplicar el mismo control a las pruebas del adaptador que ya estén previstas en A10. A12 mantiene su ventana a partir de M10.

Si se incorporan las 200 h completas, la carga parcial de M9 llega a **4.337,4 h** y quedan **462,6 h** hasta la capacidad global. El bloque representa **CLP 5.152.000** de costo interno referencial para 10.1 con los valores de AUD-14. Su imputación se concilia con el presupuesto existente del elemento 10. D2 debe validar el calendario de pruebas y la disponibilidad de QA, Software, Datos y SRE. El saldo global sigue sujeto a la carga de terreno, implantación, gestión e innovaciones pendientes.

Fuentes: [T-14, paquete 10.1](https://github.com/mvergaral/audIT/blob/4da4195/recursos/Formato-Oferta-audIT/subdocumentos/07-plan-trabajo/formularios/T-14.tex#L67) · [T-17, catálogo de pruebas de integración y sistema](https://github.com/mvergaral/audIT/blob/4da4195/recursos/Formato-Oferta-audIT/subdocumentos/09-calidad/formularios/catalogo-T-17.tex#L809).

#### Homologación y trabajo en terreno de M9

T-15 sitúa el final temprano de A11 en el día hábil 172, dentro de M9. T-14 mantiene en 4.1 las pruebas físicas del equipo a bordo y en 4.2 los montajes. Las **260 h de los 52 montajes** ya incluyen instalación y preparación de banco. Para la homologación de terceros, S4 prevé clasificar equipos y plataformas contra su estándar en Etapa 1. La verificación de intercambio de datos de terceros ya tiene una reserva en 10.1 (CP-INT-07/08). Cualquier revisión de terreno de 4.3 se registra cuando exista una visita o equipo identificado y se concilia con A10 y 10.1.

D2 propone un escenario para **un ciclo de cierre de A11** en M9. La cantidad de ciclos y las horas son supuestos pendientes de validar con el calendario del piloto y las familias de equipos. Las pruebas se ejecutan sobre el equipo físico y su evidencia se concilia con T-17.

| Trabajo de cierre de A11 | Firmware (h) | QA (h) | Telecomunicaciones y campo (h) | Total (h) |
| --- | ---: | ---: | ---: | ---: |
| Preparar el equipo de prueba y comprobar lectura pasiva del bus (CP-HW-04) | 8 | 0 | 8 | 16 |
| Lanzar y comprobar el ensayo de desconexión y recuperación (CP-HW-03) | 8 | 8 | 0 | 16 |
| Ejecutar la prueba física de alerta y bloqueo de interacción en marcha (CP-HW-06) | 8 | 0 | 8 | 16 |
| Conciliar evidencia, cerrar incidencias del piloto y registrar acta técnica | 0 | 8 | 8 | 16 |
| **Total de referencia** | **24** | **16** | **24** | **64** |

El ensayo de 72 h se calendariza como duración transcurrida. La fila contempla dedicación de preparación, comprobación y registro. Revisar si alguna ejecución ya fue completada o está presupuestada en A11 o en calidad antes de incorporar la reserva.

Para las **balizas de semirremolque**, D4 estima 15 minutos-persona por unidad y una ventana M6–M10 y M16–M18. Las 210 unidades base equivalen a 52,5 h en total. En M9 se aplica **0,25 h × balizas programadas en el mes** cuando se confirme la agenda. La cantidad de balizas se obtiene del calendario de semirremolques.

Con la reserva completa de 10.1 y el escenario de 64 h de A11, M9 suma **4.401,4 h** y la diferencia respecto a T-15 es **398,6 h antes de balizas y otros pendientes**. Para cerrar terreno, confirmar las familias que requieren pruebas, las visitas de clasificación de terceros, el número de balizas en M9 y los turnos de campo. Las horas se concilian con los presupuestos base de equipamiento y calidad.

Fuentes: [T-14, paquetes 4.1–4.3](https://github.com/mvergaral/audIT/blob/4da4195/recursos/Formato-Oferta-audIT/subdocumentos/07-plan-trabajo/formularios/T-14.tex#L41) · [T-15, A11](https://github.com/mvergaral/audIT/blob/4da4195/recursos/Formato-Oferta-audIT/subdocumentos/07-plan-trabajo/formularios/T-15.tex#L204) · [S4, estándar de homologación](https://github.com/mvergaral/audIT/blob/4da4195/recursos/Formato-Oferta-audIT/subdocumentos/04-arquitectura/contenido.tex#L978) · [T-17, trazabilidad de pruebas físicas](https://github.com/mvergaral/audIT/blob/4da4195/recursos/Formato-Oferta-audIT/subdocumentos/09-calidad/formularios/trazabilidad-T-17.tex#L32) · [D4, equipos y calendario](https://github.com/mvergaral/audIT/blob/993fa514357085fb75b79a329de0e5c278507233/Informe-3/d4/4.1-presupuesto-equipos.md) · [Estimación de intervenciones en terreno](APORTE_ECONOMICO_INNOVACIONES_1_Y_4.md).

#### Escenario de M9 para innovaciones 4 y 5

Para 12.4, S13 sitúa la construcción de la ventana de transmisión y la consola de permisos entre M6 y M10. D2 propone una reserva de M9 para trabajo específico del comodato, condicionada a que las interfaces base estén listas. La estimación excluye los montajes base y la implementación general de adhesión, permisos y liquidación de EDT 5. El cálculo del reparto monetario de esperas requiere confirmar la regla y su mes de implementación.

| Trabajo de 12.4 propuesto en M9 | Firmware (h) | Software (h) | Frontend (h) | QA (h) | Total (h) |
| --- | ---: | ---: | ---: | ---: | ---: |
| Integrar la ventana del viaje con la transmisión del equipo y probar los límites | 16 | 8 | 0 | 8 | 32 |
| Mostrar y verificar en la consola la ventana efectiva, su vigencia y el efecto de la revocación | 0 | 8 | 16 | 16 | 40 |
| Probar la consistencia entre asignación, ventana autorizada y eventos registrados | 0 | 8 | 0 | 16 | 24 |
| **Reserva preliminar 12.4** | **16** | **24** | **16** | **40** | **96** |

Las horas de 12.4 son una estimación de D2. La primera fila prueba los límites del equipo. La tercera comprueba la trazabilidad entre servicios y registros. Antes de adoptar el escenario, conciliar casos y ejecuciones con el equipo a bordo (4.1), el trabajo de permisos de A09/G13 y las pruebas transversales de 10.1. La reserva queda sujeta a la disponibilidad y al alcance pendiente real en M9.

Para **12.5**, D1 estima 300 h de desarrollo algorítmico y síntesis vocal entre M4 y M9 a CLP 30.000/h. El escenario usa un reparto uniforme de **50 h en M9** (CLP 1.500.000 de costo atribuido). La dedicación mensual efectiva requiere el calendario de D1. Los talleres de M4 y la calibración de M13–M15 tienen sus propias ventanas.

Con estas dos reservas, la carga parcial de M9 pasa de **4.401,4 a 4.547,4 h**. La diferencia con la capacidad de T-15 queda en **252,6 h** antes de balizas, visitas de clasificación, preparación de implantación, gestión y demás carga por identificar. Registrar ambas reservas como escenarios de capacidad hasta aprobar su imputación por perfil y mes.

Fuentes: [S13, ventana y consola de la innovación 4](https://github.com/mvergaral/audIT/blob/4da4195/recursos/Formato-Oferta-audIT/subdocumentos/13-innovaciones/contenido.tex#L369) · [T-14, paquetes 12.4 y 12.5](https://github.com/mvergaral/audIT/blob/4da4195/recursos/Formato-Oferta-audIT/subdocumentos/07-plan-trabajo/formularios/T-14.tex#L77) · [D1, valorización de innovación 5](https://github.com/mvergaral/audIT/blob/993fa514357085fb75b79a329de0e5c278507233/Informe-3/d1/ECONOMICO_SUPUESTOS_Y_PARAMETROS_D1.md#L56).

#### Balizas, visitas, implantación y gestión en M9

| Partida | Carga de referencia o dato pendiente |
| --- | --- |
| Balizas | Como escenario, repartir las 210 balizas base en proporción a los 182 montajes de camión. Las 52 altas de M9 representan 60 balizas y **15 h-persona**. La cantidad efectiva depende de la agenda de semirremolques, que tiene su propia ventana. |
| Visitas de clasificación | 4.3 y S4 requieren identificar y clasificar equipos de terceros. Registrar solo las visitas de M9 que exijan presencia en terreno, con horas de intervención y traslado por perfil. Conciliar las pruebas de interfaz ya contempladas en A10/10.1 y las visitas que coincidan con el montaje base. Sigue pendiente la cantidad y duración. |
| Implantación y capacitación | La actividad A13 empieza en M10. El material técnico de G13 ya está en la estimación de A09. Las horas de coordinación de terminales, preparación de turnos u otras tareas previas se incorporan si se identifica su actividad en M9. |
| Gestión de proyecto | T-15 asigna **9.600 h** al elemento 1 de implementación y T-14 prevé dirección e informes en M9. Falta el reparto efectivo por mes y perfil. Para sensibilidad, una distribución uniforme en los 20 meses de la curva de implementación asigna **480 h** a M9. |

| Escenario | Carga M9 (h) | Saldo frente a 4.800 h |
| --- | ---: | ---: |
| Parcial anterior | 4.547,4 | 252,6 |
| Con 60 balizas como referencia | 4.562,4 | 237,6 |
| Con balizas y reparto uniforme de gestión | 5.042,4 | −242,4 |

Con la referencia de balizas, **gestión, visitas y preparación de implantación deben sumar como máximo 237,6 h** para caber en la capacidad global, antes de incorporar otros pendientes. Las 480 h de gestión muestran la sensibilidad del mes al reparto de esa partida. Para decidir si hay sobrecarga, D2 debe obtener primero la dedicación de gestión en M9 y después confirmar la agenda de terminales. Los perfiles de terreno deben revisarse por turno y terminal.

Fuentes: [T-14, gestión y comunicaciones](https://github.com/mvergaral/audIT/blob/4da4195/recursos/Formato-Oferta-audIT/subdocumentos/07-plan-trabajo/formularios/T-14.tex#L29) · [T-15, horas de implementación por EDT](https://github.com/mvergaral/audIT/blob/4da4195/recursos/Formato-Oferta-audIT/subdocumentos/07-plan-trabajo/formularios/T-15.tex#L54) · [D4, ventana de balizas](https://github.com/mvergaral/audIT/blob/993fa514357085fb75b79a329de0e5c278507233/Informe-3/d4/4.1-presupuesto-equipos.md#L183) · [Montajes base y duración por baliza](APORTE_ECONOMICO_INNOVACIONES_1_Y_4.md).

#### Dedicación de gestión identificada en M9

S6 establece dedicación exclusiva del **Jefe de Proyecto durante la implementación**, a cargo de línea base, cambios, riesgos y seguimiento. Con el mes contractual de T-15, D2 reserva **160 h de dedicación nominal** para ese rol en M9. El seguimiento semanal y el Comité de Proyecto quincenal forman parte de esa dedicación. Al consolidar por EDT, verificar si alguna actividad del jefe ya está imputada a otro elemento y contar cada hora una vez.

S1 identifica tres analistas PMO. La asignación explícita de tres FTE que figura en T-15 corresponde a M13–M15. Para M9 queda pendiente distribuir la dedicación de PMO por actividad y verificar si alguna parte ya está recogida como liderazgo o coordinación en EDT 5–7. El Líder de Desarrollo del insumo de D3 y el Jefe de Proyecto son roles distintos.

| Cruce nominal | Horas de M9 |
| --- | ---: |
| Escenario parcial con balizas | 4.562,4 |
| Jefe de Proyecto a dedicación exclusiva | 160 |
| **Demanda identificada bajo este escenario** | **4.722,4** |
| **Diferencia frente a capacidad global de T-15** | **77,6** |

Esas 77,6 h deben cubrir conjuntamente la dedicación adicional de PMO, visitas, preparación de implantación y otras partidas pendientes. Como prueba de sensibilidad, **80 h adicionales de PMO** llevarían el escenario a 4.802,4 h, un exceso de 2,4 h antes de terreno e implantación. Las 80 h ilustran media jornada mensual. D2 debe revisar primero el plan de asignación de los analistas de PMO en M9 y cruzarlo con las actividades ya contabilizadas.

Fuentes: [S6, dedicación exclusiva y gobernanza](https://github.com/mvergaral/audIT/blob/4da4195/recursos/Formato-Oferta-audIT/subdocumentos/06-metodologias/contenido.tex#L69) · [S1, equipo de PMO](https://github.com/mvergaral/audIT/blob/4da4195/recursos/Formato-Oferta-audIT/subdocumentos/01-empresa/contenido.tex#L158) · [T-15, capacidad nominal y asignación de M13–M15](https://github.com/mvergaral/audIT/blob/4da4195/recursos/Formato-Oferta-audIT/subdocumentos/07-plan-trabajo/formularios/T-15.tex#L105).

#### Reserva preliminar de PMO en M9

S1 asigna a PMO el control de la EDT, el seguimiento del Gantt y la coordinación documental. S6 establece seguimiento semanal y Comité de Proyecto quincenal. D2 propone estimar el trabajo de un analista en horas-persona, con cuatro ciclos semanales y dos quincenales durante el mes contractual. Las duraciones son supuestos de planificación de D2.

| Actividad de PMO | Criterio | Horas M9 |
| --- | --- | ---: |
| Preparar el seguimiento semanal, registrar acuerdos y actualizar acciones | 4 ciclos × 3 h | 12 |
| Consolidar el informe y el acta del Comité de Proyecto | 2 ciclos × 6 h | 12 |
| Actualizar el Gantt, la carga por EDT y los compromisos de A08, A09, A10 y A11 | 4 cortes × 4 h | 16 |
| Mantener el registro de riesgos, cambios y decisiones | 4 cortes × 3 h | 12 |
| Consolidar dependencias y trazabilidad documental para la entrega de G13 | 1 bloque de cierre × 12 h | 12 |
| **Reserva de PMO** | | **64** |

El Jefe de Proyecto conserva la conducción de reuniones y decisiones dentro de sus 160 h. La reserva de PMO cubre preparación, registro y seguimiento documental. Para el cierre de G13, conciliar estas 12 h con las tareas de congelamiento y evidencia de A09: PMO consolida y controla el expediente de entrega, mientras ingeniería y QA preparan los artefactos y evidencias técnicas. La reserva tampoco incorpora la coordinación técnica ya imputada al Líder de Desarrollo en EDT 5–7.

Con las 64 h completas, el escenario de M9 llega a **4.786,4 h** y quedan **13,6 h** frente al total de T-15. Ese saldo debe cubrir visitas, preparación de implantación y demás pendientes. Las 64 h equivalen al 40 % de un mes-persona nominal. Para confirmar que caben, D2 debe identificar el analista y comprobar sus otras asignaciones. La reserva no se incorpora como costo adicional a las 9.600 h de gestión de T-15 mientras se concilia su imputación.

Fuentes: [S1, funciones de PMO](https://github.com/mvergaral/audIT/blob/4da4195/recursos/Formato-Oferta-audIT/subdocumentos/01-empresa/contenido.tex#L158) · [S6, cadencias de gobernanza](https://github.com/mvergaral/audIT/blob/4da4195/recursos/Formato-Oferta-audIT/subdocumentos/06-metodologias/contenido.tex#L90) · [T-15, horas por elemento EDT](https://github.com/mvergaral/audIT/blob/4da4195/recursos/Formato-Oferta-audIT/subdocumentos/07-plan-trabajo/formularios/T-15.tex#L54).

#### Preparación de terminales y visitas de clasificación

D2 propone **20 h de Analista de Implantación** para preparar los cinco terminales antes de A13. La reserva supone una coordinación remota por terminal y se limita a la preparación operativa. Debe conciliarse con las tareas ya presupuestadas de agenda de montaje y con el material técnico de G13.

| Actividad de preparación | Horas por terminal | Horas para cinco terminales |
| --- | ---: | ---: |
| Confirmar contraparte, turnos y perfiles que participarán en la capacitación | 2 | 10 |
| Verificar lugar, acceso y disponibilidad de recursos para las sesiones | 1 | 5 |
| Consolidar agenda y registrar confirmaciones y pendientes | 1 | 5 |
| **Reserva de implantación** | **4** | **20** |

Para **4.3**, revisar primero qué equipos de terceros pueden clasificarse con fichas y evidencia de la plataforma, y cuáles requieren inspección física. La reserva presencial se calcula con horas de inspección y traslado por persona. Como sensibilidad, una visita adicional de dos horas con dos personas agrega **4 h-persona**, antes de traslados. Cinco visitas de ese tipo sumarían **20 h-persona**. El número, duración y dotación de las visitas son supuestos para probar el impacto.

| Escenario de M9 | Carga (h) | Saldo frente a 4.800 h |
| --- | ---: | ---: |
| Parcial anterior, con PMO | 4.786,4 | 13,6 |
| Con preparación de los cinco terminales | 4.806,4 | −6,4 |
| Con preparación y cinco visitas adicionales, antes de traslados | 4.826,4 | −26,4 |

D2 debe comprobar con la agenda de implantación cuáles de las confirmaciones ya están incluidas y qué tareas pueden hacerse al inicio de M10. G13 está en el día hábil 182, por lo que quedan dos días hábiles de M10 antes del inicio previsto de A13. Trasladar horas a esa ventana requiere validar los turnos y la disponibilidad de los analistas. Si la preparación debe quedar íntegra en M9, el escenario exige liberar al menos 6,4 h más las visitas efectivas y demás pendientes.

Fuentes: [S7, cinco terminales y dotación de implantación](https://github.com/mvergaral/audIT/blob/4da4195/recursos/Formato-Oferta-audIT/subdocumentos/07-plan-trabajo/contenido.tex#L276) · [T-15, G13 y comienzo de A13](https://github.com/mvergaral/audIT/blob/4da4195/recursos/Formato-Oferta-audIT/subdocumentos/07-plan-trabajo/formularios/T-15.tex#L206) · [S4, clasificación de equipos de terceros](https://github.com/mvergaral/audIT/blob/4da4195/recursos/Formato-Oferta-audIT/subdocumentos/04-arquitectura/contenido.tex#L978).

#### Ajuste propuesto para la preparación antes de G13

| Ventana | Trabajo de Implantación | Horas-persona |
| --- | --- | ---: |
| M9 | Confirmar contraparte, turnos y participantes para los cinco terminales. | 10 |
| M10, primer día hábil antes de G13 | Verificar acceso, lugar y recursos. Reservar 1 h por terminal. | 5 |
| M10, segundo día hábil antes de G13 | Cerrar la agenda y registrar confirmaciones. Reservar 1 h por terminal y completar antes de G13. | 5 |
| **Total** | | **20** |

El ajuste deja M9 en **4.796,4 h**, con **3,6 h** frente al techo de T-15, antes de cualquier visita presencial y otros pendientes. M10 recibe 10 h de Analista de Implantación. D2 debe asignar 5 h por día y comprobar que el segundo bloque termine antes de G13. Las confirmaciones que dependan de disponibilidad de terminal deben levantarse en M9.

Para 4.3, usar primero las fichas del equipo y la evidencia de la plataforma. Registrar como excepción los equipos cuya clasificación requiera inspección física, con terminal, fecha, perfiles, intervención y traslado. Una visita adicional de 4 h-persona en M9 dejaría el escenario en 4.800,4 h antes del traslado. Calendarizar esas visitas en una ventana con disponibilidad acreditada o revisar la carga de M9 antes de darla por nivelada.

#### Capacidad por perfil en M9

La carga de A09 se obtiene con los últimos dos días del sprint 5, los diez del sprint 6 y los primeros ocho del sprint 7. Se usan los tres perfiles revisados por D3 en los sprints 5 y 6, las asignaciones preliminares de los demás perfiles y las 744 h de D2 para el sprint 7. Para EDT 6 y 7 se conserva su reparto mensual preliminar. La columna de otros trabajos suma las reservas de innovaciones 1, 2 y 4, 10.1 y el cierre de A11 según el perfil aplicable.

| Perfil | A09 (h) | EDT 6–7 (h) | Otros trabajos (h) | Demanda M9 (h) | Equivalente a 160 h | Personas mínimas con dedicación de hasta 160 h al perfil |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Software sénior | 505,6 | 509 | 144 | **1.158,6** | 7,24 | 8 |
| Frontend/Móvil | 328 | 75 | 40 | **443** | 2,77 | 3 |
| QA | 323,2 | 285 | 192 | **800,2** | 5,00 | 6 |
| Datos | 272 | 521 | 40 | **833** | 5,21 | 6 |
| SRE | 252,8 | 95 | 40 | **387,8** | 2,42 | 3 |

Las 50 h de la innovación 5 se conservan en la carga global con perfil específico por confirmar. Los mínimos por perfil son cotas brutas. Una misma persona puede cubrir más de un perfil si tiene las competencias y la suma de sus asignaciones cabe en su calendario. T-15 indica 30 personas para todo M9. La asignación detallada por escuadra corresponde a M13–M15. Para validar M9 hace falta el cuadro de personas y turnos, empezando por Software, QA y Datos. También se debe resolver qué ejecuciones de 10.1 coinciden con A10, G13 o A11 antes de cerrar sus horas.

Para la preparación de terminales, S7 prevé siete analistas de Implantación desde M10. D2 debe identificar quién cubre cada bloque de 5 h antes de G13 y comprobar sus asignaciones simultáneas. La dotación prevista permite identificar el equipo responsable. La confirmación requiere una asignación para esos dos días.

Fuentes: [T-15, dotación mensual](https://github.com/mvergaral/audIT/blob/4da4195/recursos/Formato-Oferta-audIT/subdocumentos/07-plan-trabajo/formularios/T-15.tex#L36) · [T-15, alcance de la tabla por rol](https://github.com/mvergaral/audIT/blob/4da4195/recursos/Formato-Oferta-audIT/subdocumentos/07-plan-trabajo/formularios/T-15.tex#L99) · [S7, dotación de implantación](https://github.com/mvergaral/audIT/blob/4da4195/recursos/Formato-Oferta-audIT/subdocumentos/07-plan-trabajo/contenido.tex#L276).

#### Cruce semanal de Software, QA y Datos en M9

M9 comprende los días hábiles 160 a 180 de la red, contando cada tramo como fin menos inicio. La carga de A09 se prorratea por los días de cada sprint. Las demás horas tienen mes de referencia, pero no un reparto semanal completo.

| Semana de M9 | Tramo de la red | Sprints de A09 | Software (h) | QA (h) | Datos (h) |
| --- | --- | --- | ---: | ---: | ---: |
| 1 | 160–165 | 2 días del sprint 5 y 3 del sprint 6 | 136 | 76 | 100 |
| 2 | 165–170 | 5 días del sprint 6 | 136 | 76 | 100 |
| 3 | 170–175 | 2 días del sprint 6 y 3 del sprint 7 | 121,6 | 83,2 | 52 |
| 4 | 175–180 | 5 días del sprint 7 | 112 | 88 | 20 |
| **A09 en M9** | | | **505,6** | **323,2** | **272** |
| **Horas con semana pendiente** | | EDT 6–7, innovaciones, 10.1 y A11 según perfil | **653** | **477** | **561** |
| **Demanda mensual identificada** | | | **1.158,6** | **800,2** | **833** |

En las fechas tempranas de T-15, A08 y A11 terminan el día 172, durante la semana 3. A10 termina el día 178, durante la semana 4. Estas fechas permiten priorizar la asignación semanal, pero las horas de EDT 6 y 7 incluyen más trabajo que A10 y A08 respectivamente. Se requiere identificar el subpaquete antes de trasladar su carga. Las pruebas transversales de 10.1 deben ubicarse tras la entrega de la interfaz y los datos que usan. El sprint 7 continúa dos días en M10 antes de G13.

Como prueba de sensibilidad, si las horas con semana pendiente se distribuyeran en cuatro partes iguales, se obtendrían los siguientes mínimos brutos. El supuesto sirve para localizar posibles picos y todavía debe contrastarse con precedencias y personas.

| Semana | Software (h / personas mínimas) | QA (h / personas mínimas) | Datos (h / personas mínimas) |
| --- | ---: | ---: | ---: |
| 1 | 299,25 / 8 | 195,25 / 5 | 240,25 / 7 |
| 2 | 299,25 / 8 | 195,25 / 5 | 240,25 / 7 |
| 3 | 284,85 / 8 | 202,45 / 6 | 192,25 / 5 |
| 4 | 275,25 / 7 | 207,25 / 6 | 160,25 / 5 |

Los mínimos dividen por 40 h brutas por persona y redondean hacia arriba. Para validar el cruce, D2 debe registrar persona, perfil, semana, horas disponibles y horas ya comprometidas. Revisar primero Datos antes del cierre temprano de A08 y QA en las semanas 3–4, cuando coinciden G13 y las pruebas integradas. Comprobar Software desde la semana 1 por la concurrencia de A09 y A10. La dotación mensual de 30 personas sigue siendo el techo agregado.

Fuente de ventanas: [T-15, red de A08, A09, A10, A11 y G13](https://github.com/mvergaral/audIT/blob/4da4195/recursos/Formato-Oferta-audIT/subdocumentos/07-plan-trabajo/formularios/T-15.tex#L200).

##### Propuesta semanal para Datos

Las 833 h de Datos identificadas en M9 se componen de 272 h de A09, 221 h de EDT 6, 300 h de EDT 7, 16 h del expediente verificable y 24 h de pruebas transversales. Para probar un calendario, D2 divide las 300 h de EDT 7 en tres bloques iguales para 7.1–7.3. Se ubica el bloque de 7.1 antes del cierre temprano de A08 en el día 172. El reparto de las 221 h de EDT 6 usa como referencia la ventana de A10 hasta el día 178 y requiere confirmar el subpaquete de cada ejecución.

| Semana de M9 | A09 | EDT 6 | 7.1 Vigencias | 7.2 Históricos y 7.3 Repositorio | Expediente | 10.1 | Total (h) | Mínimo bruto a 40 h/persona |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 100 | 61 | 42 | 50 | 0 | 0 | **253** | 7 |
| 2 | 100 | 61 | 42 | 50 | 16 | 0 | **269** | 7 |
| 3 | 52 | 62 | 16 | 50 | 0 | 0 | **180** | 5 |
| 4 | 20 | 37 | 0 | 50 | 0 | 24 | **131** | 4 |
| **Total** | **272** | **221** | **100** | **200** | **16** | **24** | **833** | |

La semana 2 concentra la mayor demanda. Si hubiera seis personas con 40 h brutas disponibles para Datos, faltarían 13 h en la semana 1 y 29 h en la semana 2. Un ajuste para probar es trasladar esas 42 h de 7.2/7.3 a semanas posteriores de M9. Las ventanas de T-14 lo permiten a nivel de paquete, sujeto a verificar sus dependencias y responsables. Si parte de ese trabajo alimenta A09 o el expediente, se conserva su precedencia y se revisa la dotación.

Las 16 h del expediente se ubican provisionalmente en la semana 2. Las 24 h de 10.1 se reservan en la semana 4 y se ejecutan según la disponibilidad de las interfaces y del padrón conciliado. Si una prueba depende del cierre de A10, su ventana es desde el día 178 y debe revisarse por día. S1 declara un Líder de Datos al 100 % durante implementación. Esa dedicación permite identificar al responsable de la coordinación y debe cruzarse con su carga de liderazgo antes de contarla como ejecución de ingeniería. Los demás perfiles de Datos requieren asignación nominal.

Fuentes: [S1, dedicación del Líder de Datos](https://github.com/mvergaral/audIT/blob/4da4195/recursos/Formato-Oferta-audIT/subdocumentos/01-empresa/contenido.tex#L187) · [T-14, paquetes 7.1–7.3](https://github.com/mvergaral/audIT/blob/4da4195/recursos/Formato-Oferta-audIT/subdocumentos/07-plan-trabajo/formularios/T-14.tex#L56) · [T-15, cierres tempranos](https://github.com/mvergaral/audIT/blob/4da4195/recursos/Formato-Oferta-audIT/subdocumentos/07-plan-trabajo/formularios/T-15.tex#L201).

##### Escenario ajustado de Datos y primera asignación de Software y QA

Para Datos, el escenario mueve 13 h de la semana 1 y 29 h de la semana 2 a la semana 3, dentro de 7.2/7.3. Se mantiene la carga de vigencias antes del día 172. Antes de adoptar el ajuste, identificar las tareas de históricos o repositorio que no sean insumo de un incremento, prueba o entrega anterior.

Para Software y QA, D2 usa un reparto proporcional dentro de los 18 días de M9 anteriores al cierre temprano de A10 como primera referencia para la carga agregada de EDT 6–7. El reparto se debe sustituir por el calendario de cada paquete, ya que EDT 7 también incluye trabajos con otras ventanas. Las reservas de innovaciones y pruebas se asignan por semana en la tabla. Los números son una propuesta de demanda, con personas todavía por confirmar.

| Perfil y trabajo | Semana 1 (h) | Semana 2 (h) | Semana 3 (h) | Semana 4 (h) | M9 (h) |
| --- | ---: | ---: | ---: | ---: | ---: |
| **Datos, escenario ajustado** | **240** | **240** | **222** | **131** | **833** |
| Software · A09 | 136 | 136 | 121,6 | 112 | 505,6 |
| Software · EDT 6–7 | 141 | 141 | 142 | 85 | 509 |
| Software · Innovaciones 1, 2 y 4 | 0 | 40 | 44 | 12 | 96 |
| Software · Pruebas 10.1 | 0 | 0 | 0 | 48 | 48 |
| **Software total** | **277** | **317** | **307,6** | **257** | **1.158,6** |
| QA · A09 | 76 | 76 | 83,2 | 88 | 323,2 |
| QA · EDT 6–7 | 79 | 79 | 79 | 48 | 285 |
| QA · Innovaciones 1, 2 y 4 | 0 | 16 | 40 | 24 | 80 |
| QA · Cierre A11 | 0 | 0 | 16 | 0 | 16 |
| QA · Pruebas 10.1 | 0 | 0 | 32 | 64 | 96 |
| **QA total** | **155** | **171** | **250,2** | **224** | **800,2** |

- **Datos:** seis personas a 40 h brutas cubrirían las dos primeras semanas con 240 h exactas. La semana 3 quedaría en 222 h después del traslado. Validar qué tareas se desplazan y quién las ejecuta.
- **Software:** la semana 2 exige 317 h. Ocho personas a 40 h dejarían 3 h brutas esa semana. Confirmar la dotación y la disponibilidad real, especialmente mientras coinciden A09 y A10.
- **QA:** con seis personas a 40 h, la semana 3 supera el techo en 10,2 h. Como variante, trasladar 16 h de 10.1 a la semana 4 dejaría QA en **234,2 h en la semana 3 y 240 h en la semana 4**. Identificar una ejecución que pueda moverse sin afectar A11, G13 ni la entrega de A10. Los casos que dependan del cierre temprano de A10 deben revisarse por día desde el 178.

La demanda mensual de los tres perfiles permanece en 2.791,8 h en ambos escenarios. D2 debe cruzar la propuesta con el calendario por persona, sus tareas en otros perfiles y las ausencias. La capacidad bruta deja poco margen en las semanas señaladas.

##### Validación de disponibilidad · Software, semana 2 de M9

La demanda de referencia es **317 h**: 136 h de A09, 141 h de EDT 6–7 y 40 h de las innovaciones 1 y 2. La siguiente distribución prueba si esa carga cabe aritméticamente en ocho jornadas de 40 h. Cada puesto representa una asignación por confirmar. La carga de EDT 6–7 requiere identificar el subpaquete y los perfiles compatibles antes de reservar personas.

| Puesto por confirmar | A09 (h) | EDT 6–7 (h) | Innovaciones 1 y 2 (h) | Total (h) | Margen bruto (h) |
| --- | ---: | ---: | ---: | ---: | ---: |
| 1 | 40 | 0 | 0 | 40 | 0 |
| 2 | 40 | 0 | 0 | 40 | 0 |
| 3 | 40 | 0 | 0 | 40 | 0 |
| 4 | 16 | 24 | 0 | 40 | 0 |
| 5 | 0 | 40 | 0 | 40 | 0 |
| 6 | 0 | 40 | 0 | 40 | 0 |
| 7 | 0 | 37 | 0 | 37 | 3 |
| 8 | 0 | 0 | 40 | 40 | 0 |
| **Total** | **136** | **141** | **40** | **317** | **3** |

T-15 permite comprobar el techo mensual de 30 personas, pero los insumos revisados carecen de una asignación nominal por perfil para esta semana. Para cada puesto, D2 debe registrar persona, actividad concreta, horas disponibles para el contrato y compromisos simultáneos. El puesto 4 requiere comprobar ambas competencias y el calendario. El puesto 8 debe separar las dos innovaciones y verificar que el mismo perfil pueda asumirlas.

El umbral de confirmación es **317 h efectivamente asignables a estos tres bloques**. Con siete personas a tiempo completo faltarían 37 h. Con ocho personas y una jornada de ausencia de 8 h faltarían 5 h, incluso antes de descontar otros compromisos. Si hay déficit, identificar primero qué horas de EDT 6–7 corresponden a trabajo con ventana flexible, conservando las dependencias de A09 y A10. Las horas de la tabla son dedicaciones brutas presupuestadas. El esfuerzo neto de historias se comprueba con la regla de T-10.

Fuentes: [T-15, dotación de M6–M9](https://github.com/mvergaral/audIT/blob/4da4195/recursos/Formato-Oferta-audIT/subdocumentos/07-plan-trabajo/formularios/T-15.tex#L36) · [T-10, regla de capacidad neta](https://github.com/mvergaral/audIT/blob/4da4195/recursos/Formato-Oferta-audIT/subdocumentos/06-metodologias/formularios/T-10.tex#L88).

##### Candidatos para Software · Semana 2 de M9

S1 declara tres ingenieros de software sénior en planta, sin identificarlos por nombre en la nómina revisada. T-15 identifica dos puestos full-stack de refuerzo en M13–M15. Su incorporación en M9 requiere confirmar fecha de alta, competencias y capacidad disponible. El cuadro vincula perfiles candidatos con los puestos de la propuesta anterior.

| Puesto | Persona o perfil candidato | Trabajo de referencia | Horas objetivo | Validación pendiente |
| --- | --- | --- | ---: | --- |
| 1 | Ingeniero de software sénior de planta 1 | A09 | 40 | Nombre y dedicación de la semana. |
| 2 | Ingeniero de software sénior de planta 2 | A09 | 40 | Nombre y dedicación de la semana. |
| 3 | Ingeniero de software sénior de planta 3 | A09 | 40 | Nombre, dedicación y asignación a Curimón. |
| 4 | Por identificar, software con experiencia en integración | A09 y EDT 6–7 | 40 | Competencias para ambos bloques y calendario. |
| 5 | Desarrollador full-stack de refuerzo 1, candidato condicionado | EDT 6–7 | 40 | Incorporación en M9 y aptitud para el subpaquete concreto. |
| 6 | Desarrollador full-stack de refuerzo 2, candidato condicionado | EDT 6–7 | 40 | Incorporación en M9 y aptitud para el subpaquete concreto. |
| 7 | Por identificar, software con experiencia en integración | EDT 6–7 | 37 | Nombre, competencias y otras asignaciones. |
| 8 | Por identificar, software para los paquetes 12.1 y 12.2 | Innovaciones 1 y 2 | 40 | Nombre, competencias y posibilidad de cubrir ambos paquetes. |
| **Total requerido** | | | **317** | |

Si los tres profesionales de planta y los dos refuerzos estuvieran disponibles y fueran compatibles con el trabajo, aportarían como máximo **200 h**, dejando **117 h** por cubrir. El escenario de planta solamente aportaría como máximo **120 h**, dejando **197 h**. Antes de contar a un profesional de Datos, Frontend, Firmware o Liderazgo como apoyo, verificar que pueda asumir la tarea específica y descontar la dedicación de su perfil original. La disponibilidad nominal de M9 sigue pendiente para los ocho puestos.

Fuentes: [S1, composición de las células de Software](https://github.com/mvergaral/audIT/blob/4da4195/recursos/Formato-Oferta-audIT/subdocumentos/01-empresa/contenido.tex#L167) · [T-15, refuerzos de M13–M15](https://github.com/mvergaral/audIT/blob/4da4195/recursos/Formato-Oferta-audIT/subdocumentos/07-plan-trabajo/formularios/T-15.tex#L115).

##### Alcance de la redistribución con cinco candidatos

La curva mensual de Software en M9 atribuye 469 h a EDT 6 y 40 h a EDT 7. Son cifras del reparto preliminar por ventanas. En la semana 2 se habían agrupado 141 h de ambos elementos. Aun si las 40 h mensuales de EDT 7 estuvieran todas en esa semana y pudieran trasladarse, quedarían **77 h** de la brecha de 117 h por cubrir. Esa es una cota optimista. El trabajo de integración que alimenta A09, las pruebas de 10.1 o el cierre de A10 requiere comprobar precedencias antes de moverse.

Las cuatro semanas de M9 demandan 277, 317, 307,6 y 257 h de Software. Si los mismos cinco candidatos aportaran 40 h por semana, su capacidad mensual sería de 800 h frente a 1.158,6 h de demanda. **La brecha mensual sería de 358,6 h**. Redistribuir horas entre semanas no elimina ese faltante mensual. Mantener abiertos dos datos para decidir: capacidad confirmada de Software en M9 y desglose de EDT 6/7 por tarea, perfil y fecha. Si se confirma el escenario de cinco personas, comparar refuerzo, reducción de esfuerzo sustentada por tareas o traslado a otro mes permitido antes de adoptar el presupuesto.

## Expediente verificable, EDT 12.1

Las 480 h de implementación están desglosadas por perfil y mes en el JSON de D3 y valorizadas en el [respaldo de AUD-21](APORTE_ECONOMICO_INNOVACIONES_1_Y_4.md). La referencia de CLP 30.000/h para Software y Frontend/Móvil corresponde a esas 224 h del expediente. Para extenderla a otros paquetes se requiere validación de D2.

D3 propone imputar las 480 h dentro de las 2.560 h de Innovaciones de T-15. En marcha blanca, conciliar los bloques de Software, Frontend/Móvil, QA y SRE con la carga de E1/A15. En M16–M20 queda pendiente estimar la dedicación de soporte por perfil y mes. Desde M21, las 12 h/mes propuestas requieren verificar disponibilidad de los mismos perfiles en 13.2 y 13.4 antes de valorizar un déficit.

## Conciliación D2/D3 · Innovaciones 1 y 2

| Mes | Expediente 12.1 (h) | Programación de patio 12.2 (h) | Demanda conjunta (h) |
| --- | ---: | ---: | ---: |
| M4 | 24 | 80 | 104 |
| M5 | 0 | 168 | 168 |
| M6 | 0 | 128 | 128 |
| M7 | 0 | 56 | 56 |
| M8 | 144 | 24 | 168 |
| M9 | 144 | 32 | 176 |
| M10 | 104 | 0 | 104 |
| M13 | 40 | 0 | 40 |
| M14 | 8 | 0 | 8 |
| M15 | 16 | 0 | 16 |
| M16 | 0 | 40 | 40 |
| M17 | 0 | 8 | 8 |
| M18 | 0 | 24 | 24 |
| **Total** | **480** | **560** | **1.040** |

D2 puede usar el JSON de D3 como base de demanda por perfil y mes. Las 1.040 h se proponen dentro de las 2.560 h del elemento 12, con 1.520 h de reserva agregada para conciliar con 12.3–12.5. La suficiencia por perfil depende de la carga simultánea. En M9 ya se incluyeron las 176 h de 12.1/12.2 en el escenario de capacidad.

| Paquete de operación | Demanda mensual conjunta | Meses | Comprobación |
| --- | --- | --- | --- |
| 13.2 | SRE 10 h y Seguridad 4 h | M21–M56 | 14 h/mes dentro de las 640 h nominales del paquete. Identificar capacidad libre de cada perfil después de las otras asignaciones. |
| 13.4 | Software 8 h, Datos 2 h y QA 4 h | M21–M56 | 14 h/mes dentro de las 640 h nominales del paquete. Identificar capacidad libre de cada perfil después de las otras asignaciones. |

Se conservan las **28 h en M21** para ambos servicios y se registra por separado cualquier esfuerzo de aceptación o traspaso de H12. Si el mismo perfil absorbe cierres de 6.5 o 7.2 en M21–M24, descontar primero esas asignaciones de su capacidad disponible. Para M16–M20, el [respaldo de AUD-21](APORTE_ECONOMICO_INNOVACIONES_1_Y_4.md) identifica las actividades candidatas de estabilización y producción de Etapa 1. Queda por asignar horas y responsables, especialmente en M18. El déficit de personal de cada perfil y mes se calcula como el máximo entre cero y la demanda menos la capacidad que D2 acredite.

**Costos de referencia propuestos para 12.2.** Adoptar para el escenario de D2 los puntos medios de E-26 que usó D3: Arquitectura y Seguridad CLP 44.000/h, Software y Frontend/Móvil CLP 28.000/h, Datos y SRE CLP 32.000/h, y QA CLP 20.000/h. Las 560 h de implementación equivalen a **CLP 16.576.000** de costo atribuido de referencia, sujeto a ratificación. El costo de CLP 30.000/h acordado para las 224 h de Software y Frontend de 12.1 conserva ese alcance. Las 6.048 h de diferencia de los sprints 2–6 quedan pendientes de conciliación. La revisión de los sprints 1 y 7 y de los demás perfiles sigue abierta.

Fuente: [D3, esfuerzo por perfil y conciliaciones](https://github.com/mvergaral/audIT/blob/df2313894b2644f856ac66525788b310a72c17a0/Informe-3/d3/3.1-esfuerzo-perfiles.md) · [D3, JSON mensual](https://github.com/mvergaral/audIT/blob/df2313894b2644f856ac66525788b310a72c17a0/Informe-3/d3/datos/presupuesto_d3.json).

### Concurrencia de cierres e innovaciones en M21–M24

El reparto preliminar de 6.5 (retiro del legado) y 7.2 (cierre de históricos) ubica 1.669 h después de M20. Para comprobar la concurrencia, se suman por perfil esas horas y las 28 h mensuales de las innovaciones 1 y 2. La suma mide demanda. La imputación de los cierres a paquetes y el costo incremental requieren validación.

| Demanda en horas | M21 | M22 | M23 | M24 |
| --- | ---: | ---: | ---: | ---: |
| SRE | 34 | 34 | 34 | 34 |
| Seguridad | 28 | 28 | 28 | 28 |
| Software | 115 | 115 | 114 | 114 |
| Datos | 146 | 146 | 146 | 146 |
| QA | 77 | 77 | 77 | 77 |
| Arquitectura, Liderazgo y Frontend/Móvil, solo cierres | 48 | 45 | 45 | 45 |
| **Total conjunto** | **448** | **445** | **444** | **444** |

Como prueba de capacidad, si todos los cierres de los cinco perfiles compartidos se atendieran en los mismos paquetes que las innovaciones, 13.2 tendría que reservar **62 h/mes** para SRE y Seguridad, y 13.4 **338 h/mes en M21–M22** y **337 h/mes en M23–M24** para Software, Datos y QA. Frente a 640 h nominales por paquete, quedarían 578 h en 13.2 y 302–303 h en 13.4 para su trabajo habitual. Estas diferencias son agregadas y dependen de la imputación de los cierres. Por ejemplo, en M21 la demanda combinada de Datos por sí sola sería 146 h, antes del resto de sus funciones.

D2 debe verificar la tarea de cierre, mes, paquete y persona responsable, y descontar la carga habitual y la guardia antes de reservar capacidad para las innovaciones. En M21 se conservan las 28 h nominales. Si hay trabajo de aceptación o traspaso H12, identificarlo aparte y comprobar si ya está incluido en su actividad. El déficit queda pendiente hasta contar con esa información. Las horas de cierre se contabilizan una vez, en la asignación aprobada.

Fuentes: [T-14, retiro del legado e históricos](https://github.com/mvergaral/audIT/blob/4da4195/recursos/Formato-Oferta-audIT/subdocumentos/07-plan-trabajo/formularios/T-14.tex#L55) · [T-15, horas de continuidad operacional](https://github.com/mvergaral/audIT/blob/4da4195/recursos/Formato-Oferta-audIT/subdocumentos/07-plan-trabajo/formularios/T-15.tex#L80).

## Revisión de cobertura de EDT 5 · Propuesta de 6.008 h

El catálogo publicado por D3 contiene **66 actividades, ocho sprints y ocho perfiles**. El JSON suma **6.008 h** y referencia los 22 RF de entrega de Etapa 1 identificados en T-12. Incluye la integración y evidencia de los cinco flujos de G13, el candidato de H4 y los trabajos de apoyo de Arquitectura, Liderazgo, Seguridad, Datos y SRE. La revisión conserva las 744 h del sprint 7 preparadas por D2 y las 800 h de cierre del sprint 8.

| Cruce de cobertura | Comprobación antes de adoptar el total |
| --- | --- |
| RNF-006 · Emisión contable e idempotencia | RF-014 está en el catálogo. Confirmar con 6.1/10.1 qué tarea verifica reintentos con el adaptador integrado y un solo documento por viaje. |
| RNF-011 · Convivencia con el TMS anterior | Confirmar el esfuerzo de enrutamiento y convivencia en 6.5/11.2 y la ejecución integrada correspondiente. Registrar en A09 únicamente cualquier ajuste aplicativo que quede sin cobertura. |
| RNF-014 · Revocación y retención | El catálogo incluye revocación e invalidación de caché en S1. Comprobar dónde se prueba que la revocación detiene la captura futura y conserva la evidencia obligatoria, cruzando 4.1, los controles de datos y la aplicación. |
| Calidad de etapa y otras dependencias | Verificar las filas de esfuerzo de 10.1–10.3 para pruebas transversales y aceptación, de 4.1/6 para equipo físico y adaptadores, y de 11.1 para impartición de capacitación. Contabilizar una sola vez la ejecución común de G13 y 10.1. |

Los puntos anteriores son comprobaciones de cobertura entre paquetes. Antes de estimar un adicional, identificar si la actividad ya está incluida y en qué paquete. La recomendación de D2 es usar **6.008 h como estimación técnica candidata** de EDT 5, comprobar esas interfaces y llevar a acuerdo el total y la dotación antes de actualizar T-15 y el presupuesto. Las **11.592 h** de diferencia respecto de las 17.600 h vigentes quedan pendientes de conciliación.

En M9, el nuevo catálogo sitúa **1.459,2 h de A09**, frente a **1.998,4 h** del escenario parcial anterior. Al sustituir solo A09, el escenario de M9 baja de 4.796,4 a **4.257,2 h**, con una diferencia global de **542,8 h** frente a T-15. Las horas de A09 de Software, Frontend/Móvil y QA en M9 permanecen iguales. Por eso la brecha de Software de la semana 2 sigue abierta bajo la dotación de cinco candidatos y requiere el desglose de EDT 6–7 y la disponibilidad real por perfil.

Fuentes: [D3, catálogo por actividad y perfil](https://github.com/mvergaral/audIT/blob/0712c7f/Informe-3/d3/datos/estimacion_edt5.json) · [D3, fronteras de alcance y calendario](https://github.com/mvergaral/audIT/blob/0712c7f/Informe-3/d3/3.1-esfuerzo-perfiles.md) · [T-12, requisitos de la solución](https://github.com/mvergaral/audIT/blob/0712c7f/recursos/Formato-Oferta-audIT/subdocumentos/03-solucion/formularios/T-12.tex).

### Resultado del cruce de los tres requisitos transversales

| Requisito | Cobertura identificada | Acción para cerrar la conciliación |
| --- | --- | --- |
| **RNF-006 · Un documento por viaje** | REV-S6-02/03 cubren la solicitud y presentación en la aplicación. El adaptador pertenece a 6.1. CP-INT-11/12 cubren emisor único e idempotencia. CP-INT-12 verifica la misma clave tras una pérdida de respuesta y exige un solo documento en ERP y base transaccional. | Identificar la ejecución del caso con el adaptador integrado en el calendario de 10.1. Revisar si cabe en el bloque contable ya reservado de M9. El ensayo de idempotencia y el bloqueo de despacho CP-SYS-06 son verificaciones distintas. |
| **RNF-011 · Convivencia con el TMS anterior** | 6.5 cubre la capa anticorrupción y el retiro del legado. CP-INT-05/06 cubren captura y enrutamiento. La trazabilidad de T-17 ubica en 11.2 la comprobación durante la convivencia: repetir la misma orden por ambas rutas, conservar un solo viaje y mantener los bloqueos. | Asignar la ejecución de convivencia al calendario de 11.2 y conciliar su evidencia con 10.1 y 6.5. Verificar que la ejecución de marcha blanca compruebe el flujo completo, además de las pruebas de componente. |
| **RNF-014 / RN-10 · Revocación y conservación** | REV-S1-02 cubre revocación aplicativa e invalidación de caché. 12.4 cubre ventana del equipo y consola. CP-SEC-05 comprueba el cese de captura en los servicios y señala que la evidencia obligatoria se conserva. CP-SEC-08 comprueba integridad de los originales. | Unificar el actor de CP-SEC-05: el paso principal menciona al conductor y la variante exige al propietario o titular autorizado. Hacer explícito en el procedimiento integrado el cese de captura futura en el equipo a bordo dentro de cinco minutos y la conservación de la evidencia previa tras esa misma revocación. Incluir la denegación auditada al usuario ajeno. |

Para el último punto, D2 propone una **reserva condicional de 16 h-persona en 10.1** para completar el procedimiento y ejecutar una variante integrada: 8 h de QA, 4 h de Software y 4 h de Firmware. Se supone un equipo de prueba disponible, evidencia previa y los mecanismos de revocación implementados. Conciliarla primero con la reserva de 12.4 y con G13. Si se comparte la misma ejecución, se cuenta una vez. Si el ensayo revela un cambio de código, estimarlo en el paquete que lo ejecuta.

El cruce identifica cobertura de construcción para los tres puntos y deja pendientes la asignación horaria de las pruebas y la corrección del procedimiento de revocación. Las **6.008 h de EDT 5** quedan como estimación técnica candidata. La reserva condicional de pruebas corresponde a 10.1 y debe conciliarse antes de incorporarla al presupuesto de calidad.

Fuentes: [T-17, trazabilidad de los tres RNF](https://github.com/mvergaral/audIT/blob/0712c7f/recursos/Formato-Oferta-audIT/subdocumentos/09-calidad/formularios/trazabilidad-T-17.tex#L39) · [T-17, idempotencia contable](https://github.com/mvergaral/audIT/blob/0712c7f/recursos/Formato-Oferta-audIT/subdocumentos/09-calidad/formularios/catalogo-T-17.tex#L980) · [T-17, revocación](https://github.com/mvergaral/audIT/blob/0712c7f/recursos/Formato-Oferta-audIT/subdocumentos/09-calidad/formularios/catalogo-T-17.tex#L2330) · [T-12, RN-10](https://github.com/mvergaral/audIT/blob/0712c7f/recursos/Formato-Oferta-audIT/subdocumentos/03-solucion/formularios/T-12.tex#L598).

### Calendario de pruebas para la conciliación de EDT 5

Las ventanas siguientes usan días hábiles de la red de T-15. Son reservas propuestas de D2. Calidad e Implantación deben confirmar responsable, ambiente y disponibilidad antes de fijarlas.

| Frente | Ventana propuesta | Responsable previsto | Entrega y condición |
| --- | --- | --- | --- |
| **10.1 · Emisión contable sin duplicados (CP-INT-11/12)** | **M10, días 183–187**, dentro de A09 y antes de H4 (día 192). | Líder de Calidad y Pruebas, con el responsable del adaptador 6.1. | Con el adaptador disponible, ejecutar el reintento tras pérdida de respuesta y conciliar solicitud, documento y folio entre ERP y aplicación. Incorporar el resultado al candidato H4. Si la interfaz no está lista, elevar el impacto en H4 y confirmar con Calidad qué ejecución corresponde a A12. |
| **11.2 · Convivencia con el TMS anterior** | **M13, días 240–245**, al inicio de A15. Repetición en marcha blanca si se corrigen defectos y evidencia cerrada antes de H7. | Líder de Implantación, con Integración y Calidad. | Con la configuración de convivencia habilitada, cursar la misma orden por ambas rutas y verificar un solo viaje y la vigencia de los bloqueos. Adjuntar al acta la configuración, el resultado y las incidencias. Usar CP-INT-05/06 como antecedentes técnicos. |
| **10.1 / 12.4 · Revocación y conservación** | **Antes de G13 (día 182)** si se comparte la ejecución del candidato. Si se requiere una ejecución adicional y Calidad confirma que la prueba mínima de G13 sigue cubierta, proponer la variante ampliada en **A12, desde el día 192 y antes de H5**. | Líder de Calidad y Pruebas, con Software y Firmware. | Confirmar el actor autorizado y verificar el cese de captura futura en cinco minutos y la conservación de evidencia en la misma ejecución. Mantener las 16 h como reserva condicional hasta decidir si el ensayo se comparte. |

La reserva contable de M9 corresponde al bloqueo de despacho CP-SYS-06. El calendario ubica la comprobación integrada de idempotencia en M10 y deja pendiente confirmar sus horas en 10.1. En M9 se mantienen las pruebas del conector TMS de 10.1. La comprobación de convivencia de M13 se imputa en 11.2 y reutiliza la evidencia técnica cuando sea válida para ese escenario. Las pruebas se registran por ejecución y paquete para conciliar horas antes de adoptar la estimación de EDT 5.

Fuentes: [T-14, paquetes 10.1 y 11.2](https://github.com/mvergaral/audIT/blob/0712c7f/recursos/Formato-Oferta-audIT/subdocumentos/07-plan-trabajo/formularios/T-14.tex#L67) · [T-15, precedencias y ventanas](https://github.com/mvergaral/audIT/blob/0712c7f/recursos/Formato-Oferta-audIT/subdocumentos/07-plan-trabajo/formularios/T-15.tex#L203) · [T-17, trazabilidad de ensayos](https://github.com/mvergaral/audIT/blob/0712c7f/recursos/Formato-Oferta-audIT/subdocumentos/09-calidad/formularios/trazabilidad-T-17.tex#L39).

#### Responsables del calendario de pruebas

| Prueba | Responsable de la propuesta técnica | Coordinación interna de la entrega | Insumo que debe confirmar cada frente |
| --- | --- | --- | --- |
| Emisión contable sin duplicados, 10.1 / 6.1 | Líder de Calidad y Pruebas. El Líder de Integración entrega el adaptador de 6.1. | **D1** para QA y **D3** para la interfaz. **D2** registra la ventana y concilia las horas. | D1 confirma caso, ejecutor y evidencia. D3 confirma disponibilidad del adaptador y del ambiente de integración antes de H4. |
| Convivencia con el TMS anterior, 11.2 / 6.5 | Líder de Implantación. El Líder de Integración entrega la configuración de convivencia y Calidad valida la evidencia. | **D2** coordina la ventana y el acta. **D3** prepara el enrutamiento de 6.5. **D1** revisa la prueba y su evidencia. | D2 confirma el responsable operativo de la marcha blanca y la ventana. D3 confirma configuración y datos de prueba. D1 confirma el criterio de aceptación. |
| Revocación y conservación, 10.1 / 12.4 / 4.1 | Líder de Calidad y Pruebas para el ensayo integrado. Líder Funcional para 12.4 e Ingeniero de firmware para 4.1. | **D1** coordina el caso. **D2** concilia 12.4 y la reserva. **D3** aporta aplicación y permisos. **D4** aporta equipo a bordo y firmware. | D1 confirma el actor autorizado y si una sola ejecución cubre G13 y 12.4. D3 y D4 confirman las partes de aplicación y equipo que intervienen. |

La asignación por rol se basa en T-14. S1 nomina a Claudia Navarrete Rivas para Calidad y Pruebas. La asignación por dupla corresponde a la coordinación académica de los aportes. El ejecutor individual, el ambiente y la disponibilidad de cada ventana se confirman con el equipo responsable.

Fuentes: [T-14, responsables de los paquetes](https://github.com/mvergaral/audIT/blob/0712c7f/recursos/Formato-Oferta-audIT/subdocumentos/07-plan-trabajo/formularios/T-14.tex#L41) · [S1, rol nominado de Calidad](https://github.com/mvergaral/audIT/blob/0712c7f/recursos/Formato-Oferta-audIT/subdocumentos/01-empresa/contenido.tex#L181) · [Linear, organización por dupla](https://linear.app/audit-fep/document/guia-de-tareas-duplas-y-dependencias-entrega-3-d3076fd48ae7).

#### Acuerdo D1–D2 sobre CP-SEC-05

D1 confirma que el actor de revocación será el **titular autorizado del camión**, conforme a RF-022. Se propone una sola ejecución: registrar evidencia previa, revocar el permiso, comprobar que el acceso cubierto cesa en un máximo de cinco minutos y verificar que la evidencia de conservación obligatoria sigue íntegra.

**RN-10 de T-12** exige también que la revocación detenga la captura futura en el equipo audIT en no más de cinco minutos. El entorno de CP-SEC-05 figura como Staging AKS / Módulo de Privacidad. Para acreditar RN-10 en la misma corrida, D4 debe confirmar que el equipo a bordo de prueba puede conectarse al entorno y que se puede observar su registro de captura o búfer local. El cese de acceso en la aplicación y el cese de captura en el equipo se registran como dos resultados.

| Evidencia de la corrida | Comprobación |
| --- | --- |
| Antes de revocar | Con un permiso vigente y una ventana de viaje que permanezca abierta durante la prueba, comprobar que el equipo registra posiciones, que el acceso autorizado funciona y que existe una muestra de evidencia previa identificada. |
| Después de revocar | Registrar la hora de revocación y verificar, con marcas de tiempo comparables, que el acceso cubierto cesa y que el equipo deja de registrar nuevas posiciones cubiertas dentro de cinco minutos. Conservar evidencia del equipo además de la del backend. |
| Conservación y autorización | Comprobar la integridad de la muestra previa. Ejecutar también la denegación auditada para el usuario ajeno prevista en la variante de CP-SEC-05. |

Las **16 h de 10.1** siguen como reserva condicional. D1 confirma el criterio de aceptación, D3 la observación en la aplicación y D4 la observación en el equipo. Si el entorno permite verificar ambos ceses y la conservación en la misma corrida, retirar la reserva para la ejecución adicional. Si falta la observación del equipo, conservar la reserva y programar la variante física en la ventana acordada con Calidad. Este acuerdo se registra en AUD-14 para la actualización posterior del procedimiento en T-17.

Fuentes: respuesta de D1 compartida con D2. [T-12, RN-10](https://github.com/mvergaral/audIT/blob/0712c7f/recursos/Formato-Oferta-audIT/subdocumentos/03-solucion/formularios/T-12.tex#L598) · [T-17, CP-SEC-05 y entorno](https://github.com/mvergaral/audIT/blob/0712c7f/recursos/Formato-Oferta-audIT/subdocumentos/09-calidad/formularios/catalogo-T-17.tex#L2330) · [S13, ventana de transmisión y búfer](https://github.com/mvergaral/audIT/blob/0712c7f/recursos/Formato-Oferta-audIT/subdocumentos/13-innovaciones/contenido.tex#L369).

**Respuesta de D4.** D4 coincide con el actor autorizado y propone una sola corrida para comprobar el cese de acceso y la conservación de evidencia. La confirmación del entorno queda pendiente: D4 debe indicar si el equipo de prueba puede conectarse a Staging AKS y si, en esa misma corrida, se puede observar un registro local de captura o del búfer con marcas de tiempo. RN-10 de T-12 es la fuente del cese de captura a bordo. Mantener las 16 h de 10.1 como reserva condicional hasta resolver ese punto.

**Propuesta de equipo de D1.** D1 ajustará CP-SEC-05 para comprobar en la misma corrida el cese de captura en un máximo de cinco minutos y la conservación íntegra de la evidencia previa. Propone un **iWave G26I de banco**. D4 debe confirmar disponibilidad, conexión a Staging y qué registro local con marcas de tiempo permite verificar la última captura. Si el banco permite obtener esa evidencia junto con las comprobaciones de la aplicación, retirar las 16 h reservadas para una ejecución adicional.

#### CP-SEC-05 · Corrida de banco propuesta y supuestos

D4 confirmó que se puede usar en banco la unidad de prueba **iWave G26I** con el Iridium Edge y los lectores, registrada en el IoT Hub de **PREPROD**. Propuso sincronizar los relojes GNSS y UTC, conservar copias de la bandeja SQLite y cruzarlas con el evento de revocación y Log Analytics. D1 propuso que el actor sea el titular autorizado del camión. La corrida se planifica antes de G13, con RF-022 disponible en PREPROD y una ventana de viaje que siga abierta durante el ensayo.

| Punto | Estado para la planificación |
| --- | --- |
| Cese de captura local | **Supuesto pendiente de D3:** al aplicar la nueva versión del permiso, el equipo deja de registrar nuevas posiciones cubiertas dentro de cinco minutos desde la revocación, según RN-10. Los registros obligatorios de jornada conservan su tratamiento propio. |
| Evidencia del equipo | **Supuesto pendiente de comprobar en banco:** SQLite u otro registro local conserva marcas de tiempo de las capturas, incluidas las posiciones ya enviadas o retiradas de la bandeja. Comparar el último registro de captura con la hora de revocación. Si la bandeja solo muestra mensajes pendientes, obtener el registro local que permita observar la captura. |
| Evidencia de aplicación y conservación | **Resultado esperado:** vincular el evento de auditoría de revocación, la versión aplicada en el equipo, el cese de emisión y acceso en PREPROD y la integridad de la muestra previa de conservación obligatoria. Registrar por separado captura, transmisión y acceso. |
| Variante sin enlace | **Variante propuesta:** revocar mientras el equipo está desconectado y verificar que al reconectarse comprueba la versión del permiso antes de transmitir. El resultado de esta variante se registra por separado del cese de captura con el equipo conectado. |
| Terceros con GPS propio | **Alcance diferenciado:** verificar revocación en la ingesta y el portal para los 192 terceros que conservan su equipo. La evidencia local del iWave corresponde al equipo de audIT. |

El escenario de una sola corrida se usa para planificar. **Las 16 h de 10.1 permanecen como reserva condicional** hasta verificar que la misma ejecución permite acreditar el cese de captura local, el cese de acceso y la conservación de evidencia. D1 conduce la definición del caso con Seguridad. D4 aporta equipo y registros de banco. D3 queda pendiente de confirmar el comportamiento de la aplicación y del registro local.

Fuentes: respuestas de D1 y D4 compartidas con D2. [T-12, RN-10](https://github.com/mvergaral/audIT/blob/0712c7f/recursos/Formato-Oferta-audIT/subdocumentos/03-solucion/formularios/T-12.tex#L598) · [S5, revocación y versión del permiso](https://github.com/mvergaral/audIT/blob/0712c7f/recursos/Formato-Oferta-audIT/subdocumentos/05-datos/contenido.tex#L112) · [D4, PREPROD e IoT Hub](https://github.com/mvergaral/audIT/blob/0712c7f/Informe-3/d4/4.2-nube-conectividad.md).

### Revisión de la propuesta de cierre de D3

| Bloque | Base propuesta para conciliar | Condición pendiente |
| --- | --- | --- |
| EDT 5 | **6.008 h** como estimación técnica candidata. Las reservas de cobertura se imputan a sus paquetes propietarios: 104 h a 6.1, 120 h a 6.5 y 128 h a 7.3, dentro de EDT 6–7. | Verificar cobertura del resto de los paquetes y acordar el cambio de las 17.600 h vigentes. Las 11.592 h de diferencia requieren conciliación de presupuesto y dotación. |
| Pruebas | 24 h de convivencia en 11.2/M13 y 40 h de retención, integridad y restauración en 10.1/A12/M11, dentro de sus presupuestos. Conciliar los bloques de 10.1 ya estimados para contable y TMS. | Mantener identificada la prueba de revocación de G13 y RN-10. Las 40 h de M11 cubren un alcance de recuperación y no resuelven por sí solas la observación del cese de captura en el equipo. La reserva de 16 h sigue condicional a la respuesta de D4. |
| Innovaciones 1 y 2 | 480 h en 12.1 y 560 h en 12.2, dentro de las 2.560 h de EDT 12. | Validar disponibilidad por perfil y mes y conciliar el saldo de 1.520 h con 12.3–12.5. |
| Continuidad M16–M20 | **60 h** del expediente: 6 h/mes de SRE, 4 h/mes de Software y 2 h/mes de Seguridad. A21 en M16–M17 y subactividad de soporte E1 en M18–M20. | Identificar los ejecutores y la cobertura de base, especialmente en M18. La subactividad se propone bajo 11.4 y no aumenta la duración contractual de A21. |
| Cierres M21–M24 | **879 h** en 6.5 y **790 h** en 7.2. La demanda de Datos es 44 h/mes para 6.5 y 100 h/mes para 7.2. | Confirmar el calendario y el paquete de ejecución. Datos suma 146 h/mes con las innovaciones, antes de su carga habitual. |
| Operación M21–M56 | **14 h/mes por paquete** de innovaciones. Para M21–M24, D3 propone 62 h/mes en 13.2 y **386, 383, 382 y 382 h** en 13.4 al asignarle también los cierres de Arquitectura, Liderazgo y Frontend/Móvil. | Verificar si 13.4 cubre esos tres perfiles además de Software, Datos y QA. La diferencia nominal de 254–258 h en 13.4 debe cubrir su trabajo habitual. Las 28 h se mantienen en M21. El esfuerzo de H12 se imputa a su propia actividad. |

Las reservas de 6.1, 6.5 y 7.3 detallan horas ya contenidas en la curva. En M9 suman 32, 16 y 24 h respectivamente. Su asignación requiere sustituir las fracciones del reparto preliminar de EDT 6–7 que correspondan a esas tareas.

Para comparar el presupuesto, se propone **CLP 177.472.000** de costo atribuido a A09 si D2 ratifica sus referencias de EDT base, incluida la tarifa de CLP 30.000/h para Software y Frontend. A puntos medios de E-26, el mismo esfuerzo equivale a **CLP 170.512.000**. Las 560 h de 12.2 conservan el escenario de puntos medios, por **CLP 16.576.000**.

Los tres bloques de continuidad, cierres y operación totalizan **2.737 h**. Los **CLP 84.360.000** de D3 corresponden al escenario en que esas horas requieren financiamiento adicional en su totalidad. La decisión se toma por perfil y mes, descontando la cobertura base que pueda acreditarse. Antes de modificar T-14, S7, T-15 o el modelo, registrar el escenario elegido y su aprobación.

Fuente: D3, «Propuesta de cierre para confirmar con D2», 12 de noviembre de 2026.

#### Capacidad de Datos en M21–M24

La propuesta de D3 requiere **146 h/mes de Datos**: 44 h de 6.5, 100 h de 7.2 y 2 h de mantenimiento de innovaciones. S1 compromete al Líder de Datos al 50 % durante la operación, equivalente a **80 h/mes nominales**. Esa dedicación corresponde al contrato y cubre funciones de liderazgo. Para imputarla a estas tareas se requiere verificar que sean compatibles con el perfil y descontar sus demás compromisos.

| Cobertura acreditada en el perfil Datos | Déficit de referencia por mes | Costo adicional de referencia M21–M24 a CLP 32.000/h |
| --- | ---: | ---: |
| 146 h/mes disponibles en el equipo de operación | 0 h | CLP 0 |
| 80 h/mes disponibles para las tres tareas | 66 h | CLP 8.448.000 |
| 0 h/mes acreditadas para estas tareas en el escenario sin cobertura | 146 h | CLP 18.688.000 |

Los tres casos son escenarios. T-15 informa 640 h/mes agregadas en 13.4. Falta identificar quién cubre la ejecución de históricos, integración y mantenimiento, y cuánto puede aportar el Líder de Datos después de sus otras responsabilidades. Priorizar la asignación de las 100 h/mes de históricos de 7.2 y comprobar después la concurrencia con 6.5. Mantener el costo incremental sin aprobar hasta acreditar la capacidad disponible por persona.

Fuentes: [S1, dedicación contractual del Líder de Datos](https://github.com/mvergaral/audIT/blob/0712c7f/recursos/Formato-Oferta-audIT/subdocumentos/01-empresa/contenido.tex#L187) · [T-15, capacidad nominal de operación](https://github.com/mvergaral/audIT/blob/0712c7f/recursos/Formato-Oferta-audIT/subdocumentos/07-plan-trabajo/formularios/T-15.tex#L80).

##### Asignación propuesta para validar Datos en operación

| Bloque mensual M21–M24 | Horas | Responsable del entregable | Ejecutor propuesto |
| --- | ---: | --- | --- |
| 7.2 · Conciliación y cierre de históricos | 100 | Líder de Datos | Ingeniero de Datos de operación. El Líder de Datos valida entregables y podría asumir parte del trabajo si su dedicación y competencias lo permiten. |
| 6.5 · Conciliación para retiro del TMS anterior | 44 | Líder de Integración | Ingeniero de Datos con acceso a históricos y al flujo de órdenes, coordinado con Integración. |
| 12.2 · Mantenimiento de calidad de entradas | 2 | Líder de Desarrollo, coordinado con Operación | Ingeniero de Datos de 13.4. |
| **Total de ejecución por confirmar** | **146** | | |

Primera opción: reservar las 146 h/mes en un puesto de Ingeniería de Datos de operación. Si ese puesto tiene 160 h nominales, quedan **14 h/mes** para sus demás tareas. Segunda opción: distribuir la ejecución entre el equipo y refuerzo según el déficit. Como prueba de sensibilidad, si se acreditaran 80 h del Líder de Datos para 7.2, quedarían **20 h de históricos + 44 h de retiro + 2 h de mantenimiento**, o **66 h/mes** de ejecución a cubrir. Las 80 h son su dedicación contractual total y requieren descontar las demás funciones de liderazgo. T-15 identifica roles de ingeniería de Datos en M13–M15. Su continuidad en 13.4 durante M21–M24 se debe confirmar por separado.

El orden de validación es identificar el puesto que ejecuta 7.2, registrar su capacidad por mes después de la carga habitual y luego asignar 6.5 y las 2 h de 12.2. La aprobación del costo incremental queda pendiente de ese cruce.

## Validaciones pendientes

- Confirmar las correspondencias con E-26 y seleccionar costos horarios respaldados para el presupuesto de personal.
- Nivelar las horas de EDT 5 a 8 por perfil y mes, considerando los demás compromisos de T-15. Conciliar los cierres de EDT 6.5 y 7.2 hasta M24 con el término de la curva de implementación en M20 y asignar el esfuerzo una sola vez.
- Incorporar los perfiles y actividades que faltan del presupuesto total, incluidos los aportes de calidad y capacitación de D1 y las actividades de terreno. La tabla cubre únicamente los cuatro elementos EDT que D3 desglosó.
- Registrar esta valorización como insumo de AUD-15 una vez validada la asignación. Para AUD-21, llevar al flujo solo las horas adicionales confirmadas.

Fuentes: FEP01 · Formularios E-24 (p. 73) y E-26 (p. 76). [JSON de D3, commit 993fa51](https://github.com/mvergaral/audIT/blob/993fa514357085fb75b79a329de0e5c278507233/Informe-3/d3/datos/presupuesto_d3.json) · [AUD-24](https://linear.app/audit-fep/issue/AUD-24) · [AUD-14](https://linear.app/audit-fep/issue/AUD-14).
