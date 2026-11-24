# Resultado de S3 y T-12

Se actualizó S3 y el Formulario T-12 en el worktree cierre-entrega-3. La planilla 3.2 entregada se usó en modo lectura. La compilación y la foliación del paquete quedan a cargo del controlador de la integración para evitar ejecución simultánea de MiKTeX.

## Cambios y localizadores

| Hallazgo | Localizador verificable | Resultado |
| --- | --- | --- |
| D2 05, ALC-01 | S3, Resumen Ejecutivo, Supuestos del alcance y tabla «Montaje inicial de equipos a bordo por terminal y mes contractual», etiqueta `tab:3-montaje`. T-12, SA-01. | Cuatro cortes 10, 60, 60 y 52, acumulados 10, 70, 130 y 182. Piloto interno, lotes externos, control de cambios y sensibilidad para faltantes. Fechas civiles ilustrativas y E-25 en meses contractuales. |
| D2 06, PLA-13 | S3, «Balizas y lectores de portería», etiqueta `sec:3-balizas-lectores`. | 210 balizas base de M7 a M9, 70 por mes, 15 minutos por unidad y 52,5 h totales. Cinco lectores de M5 a M6, uno por terminal y 10 h totales. La reserva de 14 balizas por terminal y mes es una pauta propuesta sujeta al padrón. Se conservan 21 balizas y 19 equipos a bordo para reposición. |
| D2 04 | S3, «Operación», etiqueta `sec:3-operacion`. | Mesa N1 con seis agentes y un FTE de suplencias, proveedor presencial desde M19 y 80 h internas de supervisión desde M21. Tres visitas correctivas y dos rondas regionales al mes como provisión de capacidad. Verificación de capacidad, rutas, stock y ventanas por D2 y D4, con SLA vigente. |
| D2 10, ALC-03 | T-12.8 a T-12.10, etiquetas `tab:t12-transversales`, `tab:t12-caso` y `tab:t12-administrativas`. S3, «Catálogo priorizado», etiqueta `sec:3-catalogo`. | 374 filas transversales, 27 parámetros del Caso y 13 filas de cruce administrativo. El estado es documental. En FEP02 se consignan 19 «Cumple en diseño», 77 «Parcial» y 278 «No acreditado». En FEP03 se consignan 5 «Cumple en diseño» y 22 «Parcial». Los códigos sin componente o antecedente verificable conservan ese estado. |
| D2 10, ALC-04 | T-12.2, fichas RF-003, RF-014 y RNF-005. Referencias CP-INT-03, CP-SYS-05, CP-HW-14, CP-HW-11, CP-PERF-05, CP-UNIT-16 y CP-HW-04 de T-17. T-16, R-28. | Se distinguen compromiso, evidencia de diseño y ensayo previsto. Adhesión, autorización del fabricante y homologación del retorno satelital siguen como dependencias. |
| D2 11, ALC-02 | S3, «Reversión y conciliación del corte», etiqueta `sec:3-reversion`. T-18, `tab:t18-reversion`. T-17, `sec:9-cp-sys-20`. | Se conserva el procedimiento local, se añade recuperación A/B frente a reinstalación presencial y se documentan preservación, reenvío con deduplicación y conciliación. El ensayo queda previsto antes de cada paso a producción. |
| ALC-05 y ALC-06 | T-12.1 a T-12.10 y cuerpo de S3. | Prefijo propio para las tablas del formulario y remisiones actualizadas. S3 se redacta como oferta autónoma. La presentación y numeración del PDF quedan por comprobar después de compilar. |

## Archivos y verificaciones

- `contenido.tex`, `formularios/T-12.tex`, `formularios/cumplimiento-bases.tex`, `formularios/T-12.md` y `compilar_final.py` bajo `subdocumentos/03-solucion/`.
- Cotejo de la hoja «Instalación por lote» por terminal y mes y de 14 parámetros de la planilla congelada. Se verificaron 42 códigos propios en las matrices de S3/S7 y T-17, 414 filas individuales de bases iguales en TeX y Markdown, 58 etiquetas existentes y los 64 códigos de prueba citados.
- El Markdown usa los números de sección calculados desde las fuentes. El LaTeX recupera el folio si dispone de auxiliares vigentes del expediente. La ausencia de esos auxiliares conserva el título de sección, sin atribuir un folio a otro corte.
- El wrapper acepta `--fuentes`, `--auxiliares` y `--aux-t17`. Se verificaron su sintaxis y ayuda. La compilación escribe salidas aisladas bajo `03-solucion/preparacion-final/` y deja el folio global para el ensamblado.
- Permanecen pendientes las comprobaciones de ejecución, los respaldos fuera del alcance de S3 para los requisitos sin acreditar y la revisión independiente. En Art. 46 corresponde distinguir la incorporación de la matriz de la acreditación pendiente de sus filas.
