# Correcciones de fuente del Sobre 1

Se editó únicamente `fuentes/sobre1-antecedentes.tex` en la copia aislada. El PDF de referencia sigue siendo el ejemplar cotejado en `administrativo.md`.

| Apartado | Cambio |
| --- | --- |
| Carátula y folio | Pie identificado como Sobre N.º 1 mediante `\textoPie` local al documento. Las configuraciones de firma se vaciaron localmente y los campos visibles quedaron disponibles para firma. |
| A-1 y antecedentes legales | Referencia oficial a p.49, firma propia del formulario y nómina de respaldos requeridos. |
| Antecedentes financieros y laborales | Nómina de instrumentos por incorporar. Monto de Fiel Cumplimiento de USD 1.000.000 y Correcto Funcionamiento de 5 % del valor total de la fase de implementación. FEP01 arts. 36 y 37, pp.23–24. |
| A-2 a A-4 | Siete declaraciones del A-2 conforme a FEP01 p.50. A-3 con reserva mediante `\Needspace` y bloque indivisible para declaración y firma. A-4 cubre al equipo propuesto, conforme a FEP01 p.52. Se retiraron las leyendas de autorización notarial simulada y se identificó su espacio. |
| A-5 | Índice único al inicio con número, documento, folios de inicio y término por `\pageref` y observación. Distingue formularios, nóminas y ficha de requisitos. |
| A-6 | Consolidado por sección, herramienta y finalidad. El estado de revisión queda sujeto a acreditación. Se eliminó la atribución a integrantes en este sobre y se incorporaron responsabilidad por exactitud, originalidad y coherencia técnica y la cláusula de confidencialidad del modelo, para revisión y suscripción del representante legal. |
| Habilitantes y garantía | Se señalaron los instrumentos por incorporar. Se retiraron el número de serie, fecha de emisión y banco del supuesto ejemplar y la declaración de cumplimiento íntegro. La ficha conserva glosa, plazo, monto y exigencia de original. |

## Control de fuente

Se cotejó el cambio con `git diff --no-index --check` y se verificaron el balance de llaves, el anidamiento de entornos, los siete numerales del A-2 y las 22 referencias de folio frente a 21 etiquetas únicas. Queda por comprobar con la compilación y extracción del PDF que todos los folios resuelvan, que la declaración y firma del A-3 permanezcan juntas y que el pie quede correcto en todas las páginas.

## Registro interno de pendientes

- Ignacio Cuevas es el revisor designado para D2/A-6. La revisión del corte final y su acreditación siguen pendientes.
- Carlos Abarza es el responsable de la entrega física y electrónica simultánea del 25-11-2026 a las 14:00, hora de Santiago. Su designación no acredita la revisión, las firmas ni la ejecución de la entrega.
- Faltan las piezas legales, financieras y habilitantes, el original de la boleta o sustitución expresamente autorizada para la simulación y las firmas y formalidades aplicables. El índice se debe reconciliar con el ejemplar completo antes de escanearlo y formar el respaldo digital.
- Se conservó la URL del sitio web declarada en el A-1. La eventual sustitución por una URL corporativa requiere un dato aprobado.
