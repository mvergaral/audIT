# Avance de la Dupla 1 — Informe 2

**Actualización:** 6 de octubre de 2026  
**Responsable del resumen:** Ignacio Cuevas

## Avances realizados

- Se revisaron las fuentes de S1 y S2 y se creó la bibliografía compartida en `recursos/Formato-Oferta-audIT/referencias/referencias.bib`.
- Se conectaron las citas de S1/S2 con la bibliografía. Las 17 claves citadas existen en el archivo y no tienen duplicados.
- En S1 se corrigió la mención de NIST SP 800-207 y se añadieron referencias para NIST CSF 2.0, ISO/IEC 20000-1 y Ley 19.628.
- Se precisó que ISO 27001 sigue en auditoría Fase 2 con Bureau Veritas y que la entrega del certificado está comprometida para el Mes 1, conforme al Art. 34.1.
- Se ajustó la referencia a la Ley 21.719: su entrada en vigor indicada es el 1 de diciembre de 2026. Hay que confirmar la fecha efectiva de entrega de la oferta para cerrar su aplicabilidad.
- Se actualizó la matriz del Art. 46 en sus versiones Markdown y LaTeX. La tabla conserva las 100 observaciones; las observaciones 05 y 28 reflejan que la bibliografía ya está creada y que aún faltan cotejos transversales.
- Se había corregido también una contradicción en el anexo de certificación ISO 27001: no se presenta como emitida o aprobada mientras la Fase 2 esté en curso.

## Archivos principales modificados

- `recursos/Formato-Oferta-audIT/referencias/referencias.bib`
- `recursos/Formato-Oferta-audIT/subdocumentos/01-empresa/contenido.tex`
- `recursos/Formato-Oferta-audIT/subdocumentos/02-problema/contenido.tex`
- `Informe-2/d1/Tabla-Art46-Informe2.md`
- `recursos/Formato-Oferta-audIT/anexos/observaciones-informe1.tex`
- `Informe-2/d1/subdocumento_01_anexos.md`

## Pendientes

1. **Imágenes de S2:** siguen pendientes. Al incorporarlas, verificar que no presenten las 288 horas como requisito; la exigencia mínima acordada es 72 horas y la figura debe tener datos trazables.
2. **S9:** completar el calendario cuando estén los hitos y paquetes de D2 (H4), las confirmaciones de integración de D3 (H2) y el dimensionamiento de pruebas de D4 (H3).
3. **Cotejo transversal:** revisar autorías, referencias y respuestas del Art. 46 de S3 y S13 con sus responsables.
4. **Validación legal:** confirmar la fecha de entrega y la aplicabilidad de las disposiciones citadas en S1/S2 antes de cerrar la oferta.
5. **Compilación y PDF:** falta integrar/configurar el paquete común de la plantilla y compilar para hacer revisión visual final. En el checkout disponible no está el proyecto común completo ni hay PDFs finales.

## Comprobaciones realizadas

- 17 claves de cita de S1/S2 cotejadas contra la bibliografía: sin claves faltantes ni duplicadas.
- 100 observaciones presentes en la tabla LaTeX del Art. 46.
- `git diff --check`: sin errores de formato; Git solo informó avisos de conversión de finales de línea.

**Estado:** avance documental de S1/S2 y matriz realizado; imágenes, coordinación entre duplas, revisión legal y compilación final siguen abiertos.
