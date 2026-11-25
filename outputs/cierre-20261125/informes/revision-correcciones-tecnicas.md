# Revisión de las correcciones técnicas

Cotejo de fuentes y registros de cambio del corte 25-11-2026. Los veredictos corresponden a las fuentes inspeccionadas mientras se regeneraban los PDF.

## Cumplimiento de las correcciones técnicas

**Veredicto: cumple las correcciones de fuente prioritarias en el segundo cotejo.** El paquete conserva las 74 observaciones, incorpora los supuestos al anexo S2 y corrige R-21 y el alcance geográfico de dos ensayos. El segundo cotejo comprobó las tres respuestas corregidas y las tres tablas nuevas de declaración.

| Comprobación | Resultado |
| --- | --- |
| Sintaxis e inventario Art. 46 | Las 74 llamadas preservan su orden e IDs únicos. Cada una tiene prefijo `[sub=N]` coherente con su grupo y cuatro grupos de argumentos balanceados, incluidos comandos con llaves anidadas. La cabecera ya dice 74. La completitud frente al documento de revisión original sigue por acreditar. |
| Respuestas de Art. 46 | El diff contra `evidencia/antes-conciliacion/` cambió RIE-01, RIE-02 y RIE-06. El selector inicial de `conciliar.py` buscaba el patrón `}{ID}`, mientras la fila tiene `]{ID}`. En la primera pasada quedaron intactas tres respuestas sin respaldo suficiente. En el segundo cotejo, GEN-05, EMP-02 y RIE-05 ya aparecen en estado parcial con la falta correspondiente. |
| Anexo S2 y S8/T-16 | La sección 2.F contiene SUP-01 a SUP-06 y expresa que las comprobaciones corresponden a ejecución. R-21 separa SA-01 del inicio contractual y modifica su disparador. R-17 mantiene exposición alta mientras su reducción residual sigue como objetivo de mitigación. RIE-01 refleja los 36 riesgos con reparto 17/13/6. RIE-02 exige ensayo y acta posteriores. |
| Formularios S7 | T-14, T-15 y T-18 reconocen que la revisión final está pendiente. En la primera pasada sus bloques sólo acumulaban la fila con `\usoIA`. En el segundo cotejo, los tres archivos ya contienen tabla y `\filasUsoIA`; conservar el pendiente de revisión y verificar su salida impresa. |
| Emisores ficticios | Los tres archivos del registro incorporan Certificadora Simulada Horizonte TFEP, Auditores Simulados Faro TFEP y la nomenclatura ficticia de clientes y centros. Los contactos T-6 usan `.example` y se retiraron los móviles reales de referencia. El código CSH-EXP-2026-CL-8921 coincide en S1 y Anexo 1.A. Conciliar cartas, páginas, fechas, alcances y expedientes contra el Sobre 1 cuando esté ensamblado. |
| Precio y malla | Comparé los SHA-256 de 56 insumos del snapshot seleccionados por alcance económico, de planificación y de simulación. Coinciden todos. El diff de T-14, T-15 y T-18 contra los respaldos de conciliación se limita a los bloques de declaración. |

## Calidad de las correcciones técnicas

**Veredicto: fuentes prioritarias corregidas, liberación pendiente de verificación.** Los reparos iniciales de las tres filas y declaraciones se subsanaron en fuente. El expediente y los PDF finales siguen por verificar.

- **DR.** CP-INT-25 y CP-PERF-03 ya apuntan al sitio secundario admisible de R-24. CP-INT-25 conserva «Staging Azure Multi-Region», y CP-PERF-03 sigue prescribiendo AKS, PostgreSQL/TimescaleDB y Azure Front Door. Mientras la alternativa sigue por seleccionar, parametrizar el entorno y el runbook por las capacidades homologadas. CP-INT-25 verifica consistencia a 60 segundos y fija un límite de 120 segundos sin distinguir inspección intermedia de aceptación; precisar el momento del veredicto.
- **Estados y localizadores pendientes.** GEN-01 llama «anexo independiente» a la tabla ubicada en SUBDOC00. ARQ-08 conserva el rótulo abreviado de otra figura. CAL-07 exige ingesta real de las tres plataformas, pero SA-03 mantiene una sin exportación. ALC-03 conserva el estado parcial correctamente; exige decidir los artefactos de oferta y localizar los obligatorios. RIE-06 explicita H11/A23 y la continuidad de la simulación, pero conviene decir «incorporada la respuesta de diseño, exposición alta vigente» y evitar prometer un ajuste de malla como resultado.
- **Rastreo del corte.** Las divergencias de hash en `cambios.json` para T-16, catálogo T-17 y Art. 46 tienen etapas posteriores identificables. `compilar.py` también tuvo una etapa posterior. El hash de S1 en `conciliacion-cambios.json` queda sucedido por la normalización de emisores. Emitir los hashes finales de compilación y vincularlos con los registros anteriores.
- **Maquetación y concordancia.** Verificar en los PDF regenerados la presencia de S5 independiente, los folios de todos los anexos, los seis SUP en S2, la impresión efectiva de los seis campos en cada formulario, las páginas de las fichas DR y los nuevos folios del Artículo 46. Las revisiones humanas, actas de contrato y firmas conservan sus propios requisitos de evidencia.



