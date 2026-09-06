# Resumen de avances de D2

Fecha: 6 de septiembre de 2026.

Integrantes: Ignacio C. y Matías V. Fuente de reparto:
[plan de trabajo D2 v2](plan-trabajo-d2-v2.md).

## Resumen ejecutivo

Se prepararon once de los doce entregables del plan, dos instrumentos de coordinación
entre duplas y un desarrollo específico de la decisión D-01. Los dos entregables que
cierran el Informe 1 son el Subdocumento 3 consolidado y las dos fichas T-19 de las
innovaciones tipo 1 y tipo 4. Ninguno se considera ratificado por el equipo ni aprobado
por el CLIENTE.

El catálogo contiene 42 requisitos de solución: 28 funcionales y 14 no funcionales.
Se documentaron relaciones con los 29 criterios de aceptación y las 14 restricciones
del caso. Esa cobertura de referencias no demuestra por sí sola cumplimiento técnico.

## Entregables del plan

| Código | Entregable | Avance | Pendiente |
|---|---|---|---|
| D2-01 | [Registro de decisiones](registro-decisiones-d2.md) | 26 decisiones documentadas como propuestas | Fundamentación, ratificación y validaciones; D-10, D-14, D-19 y D-21 siguen abiertas |
| D2-02 | [Catálogo RF/RNF](catalogo-requisitos-d2.md) | 28 RF y 14 RNF con origen, etapa y verificación | Completar detalle normativo, metas y revisión cruzada |
| D2-03 | [Matriz de trazabilidad](matriz-trazabilidad-d2.md) | 42 requisitos vinculados a capacidades, componentes y pruebas | Validar relaciones y resolver componentes ausentes con D3/D4 |
| D2-04 | [Esquema de solución](subdoc3-esquema-solucion.md) | Principio de solución, coherencia problema-solución y nueve capacidades | Lectura cruzada con D1, D3 y D4 |
| D2-05 | [Alcance por etapas](alcance-etapas-d2.md) | E1/E2, dependencias, entradas, salidas y exclusiones | Ratificar distribución y compromisos con Matías y el equipo |
| D2-06 | [Plan de adhesión](subdoc3-esquema-solucion.md) | Capítulo 5 del subdocumento 3, con las doce materias exigidas por el plan | Validación jurídica del anexo y ratificación de metas |
| D2-07 | [Criterios de aceptación](criterios-aceptacion-d2.md) | 29 criterios, medición y metas propuestas | Sustentar metas y validar viabilidad; no tratarlas como exigencias textuales |
| D2-08 | [T-12 preliminar](formulario-t12-preliminar-d2.md) | 42 filas y las cinco columnas oficiales | Inventario textual aplicable completo y referencias definitivas; todas las filas pendientes de verificación |
| D2-09 | [Innovación tipo 1](fichas-t19-d2.md) | Ficha T-19 con los siete elementos del Artículo 29° y la delimitación frente a CA-21 y CA-29 | Verificar las referencias APA en su fuente oficial |
| D2-10 | [Innovación tipo 4](fichas-t19-d2.md) | Ficha T-19 con los siete elementos, comodato, ventana de consentimiento y financiamiento del incentivo | Cotizar las partidas de inversión declaradas |
| D2-11 | [Subdocumento 3 consolidado](subdoc3-esquema-solucion.md) | Once capítulos, con justificación del reparto por etapas y declaración de supuestos | Lectura cruzada y numeración definitiva de secciones |
| D2-12 | Presentación | Bloques definidos en el plan | Diapositivas, reparto y ensayo |

## Coordinación con otras duplas

Se revisaron los análisis de D1, arquitectura lógica y datos de D3 e infraestructura
de D4 para recuperar propuestas existentes y evitar diseñar sin considerar su trabajo.

- [Inventario de referencias RT](inventario-requisitos-equipo.md): 180 identificadores
  citados, de los cuales 173 tienen subnúmero y 7 son referencias generales de capítulo.
- [Matriz consolidada del equipo](../matriz-consolidada-requisitos.md): 19 bloques
  y 24 asignaciones dupla-bloque al contar responsabilidades compartidas.
- Se incorporó el apartado de verificación por grupo. No se marcó ninguna aprobación
  en nombre de las duplas.

Los conteos son de identificadores citados, no de obligaciones normativas exhaustivas.
No se suman directamente a los 42 RF/RNF. FEP02 y FEP03 pueden compartir un código
con textos diferentes; debe verificarse fuente, texto y aplicabilidad antes de cerrar
el T-12. Citar un rango tampoco demuestra desarrollo de cada requisito intermedio.

## Depuración realizada

- Corregido el conteo anterior de 172 códigos y 8 capítulos: son 173 y 7.
- Corregido el resumen de asignaciones de la matriz consolidada.
- Retirada la falsa ausencia de RT-06.15 y las conclusiones basadas solo en huecos de numeración.
- Cruces RF/RNF con RT identificados como hipótesis pendientes de contraste.
- Emisiones alineadas como propuesta: base y metodología E1, cálculo productivo completo E2.
- RF-014 corregido para exigir documento conforme antes del movimiento, no mera emisión posterior.
- Separado el parámetro del caso para costeo en 24 horas del versionado propuesto por D2.
- Retiradas las declaraciones de cumplimiento del T-12: 42 filas pendientes de verificación.
- Cerrada la cifra de contratos bajo costo. Son 3, equivalentes al 31 % del ingreso, y 2 se
  renegocian en 2027 (FEP03 · Sección 7.3 · p.15 y Sección 13.2 · p.27).
- Retirados los guiones largos de los documentos de la dupla, sustituidos por punto o coma.
- Corregido el recuento de estados de las 26 decisiones: 3 completas, 19 parciales y 4 abiertas.

## Decisión D-01 desarrollada

Documento: [Jornada de conductores externos](decision-01-jornada-externa.md).

Se compararon cuatro alternativas: declaración única, tacógrafo único, integración
exclusiva con el empleador y expediente por persona con varias fuentes.

La recomendación es preparar un expediente por conductor y evaluar identidad,
cobertura temporal, procedencia, vigencia y coherencia antes del despacho. Una
declaración firmada o un tacógrafo aislado no acreditan automáticamente toda la jornada.

| Situación | Tratamiento propuesto |
|---|---|
| Evidencia suficiente y jornada disponible | Permitir tras verificar las demás condiciones |
| Jornada insuficiente | Bloquear, reprogramar o sustituir al conductor por uno habilitado |
| Evidencia ausente, vencida o contradictoria | Bloquear hasta resolver con respaldo admisible |
| Fuente externa caída | Usar expediente local únicamente si su vigencia y suficiencia están validadas |
| Corrección posterior | Conservar original, registrar nueva versión y revisar efectos operacionales |

Incluye flujo, riesgos, contingencias, pruebas y verificación por D1/D2/D3/D4 y revisión
jurídica. No constituye dictamen legal ni decisión ratificada. No se admite que un
override operacional supla jornada insuficiente o falta de acreditación.

## Bloqueos principales

1. Acreditación legal de jornada externa, firma e identidad del conductor.
2. Alcance físico sobre flota de terceros y viabilidad de la operación mixta.
3. Adhesión, propiedad, financiamiento y retiro de dispositivos.
4. Interfaces reales del sistema contable y contingencia tributaria offline.
5. Acceso autorizado a telemetría y tacógrafos por fabricante/modelo.
6. Consentimiento granular, retención obligatoria y revocación.
7. Geocercas, lugares seguros y aceptación comercial de evidencias.
8. Componentes ausentes y contradicciones técnicas señaladas a D3/D4.

## Verificación realizada y límites

Se comprobaron conteos y presencia de identificadores en catálogo, trazabilidad,
criterios y T-12. Se ejecutó control de formato con Git. Las comprobaciones no son
pruebas de una solución implementada, certificaciones ni revisión normativa exhaustiva.
No se encontró un Acta de Respuestas a Consultas en los documentos revisados; las
consultas no se trataron como respuestas del CLIENTE.

## Próximas acciones

1. Ignacio y Matías revisan D-01; D3/D4 validan implementación y se coordina revisión jurídica.
2. Reparto de innovaciones zanjado el 6 de septiembre. D2 lleva los tipos 1 y 4, D1 el
   tipo 5, D3 el tipo 3 y D4 el tipo 2. `equipo/asignacion-duplas.md` quedó corregido.
3. Matías lidera D-02/D-05 y el plan de adhesión; D4 aporta despliegue y flota mixta.
4. Completar D-10, D-14, D-19 y D-21 sin dejar sus soluciones implícitas.
5. Cada dupla verifica sus bloques y documenta correcciones y evidencia.
6. Completar el inventario normativo y la trazabilidad antes de declarar cumplimiento.
7. Verificar las referencias APA de ambas fichas en su fuente oficial, con fecha de consulta.
8. Preparar las diapositivas de los dos bloques de presentación, que se exponen entre el
   14 y el 25 de septiembre.

## Uso de asistencia de IA

Se utilizó asistencia de IA para investigación de documentos, propuestas iniciales,
matrices, depuración y redacción de estos borradores. El equipo debe revisar fuentes,
exactitud y originalidad, y registrar el uso en el Formulario A-6 conforme a FEP01,
artículo 13.5. La asistencia no sustituye la responsabilidad ni la verificación humana.
