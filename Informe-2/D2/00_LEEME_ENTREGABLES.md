# Entregables D2 — EDT y carta Gantt del proyecto completo

**Empieza abriendo `00_ABRIR_ENTREGABLES.html` en tu navegador.** Reúne el árbol completo de la EDT, las 13 secciones de detalle, ambas cartas Gantt, la trazabilidad y las observaciones pendientes.

## Archivos para incorporar al informe

**Actualización del 11 de octubre de 2026:** para impresión y anexos de S7, usar
`03_Apoyo/Laminas_EDT_Gantt_PERT.pdf`: vistas generales, detalles de los 54 paquetes,
Gantt M1–M24/M1–M56 y ambos PERT. Las láminas son vectoriales, con texto mínimo
de 10 puntos en origen. Los PDF individuales están en
`recursos/Formato-Oferta-audIT/subdocumentos/07-plan-trabajo/graficos/` y S7 los referencia.
La verificación de escala y referencias en el PDF oficial queda pendiente de compilarlo:
el entorno Windows actual presenta errores de acceso/configuración de MiKTeX y de
interpretación de la orden de compilación. El cuaderno de láminas es material de revisión,
sin sustituir el documento oficial con folios y firmas.

Para regenerar estas láminas, ejecutar
`python Informe-2/d2/99_Generacion/generar_laminas_impresion.py` después de actualizar
los datos del plan detallado. Usa la red CPM conciliada: A13 inicia en el día 182, condicionada a G13,
con 40 días de duración. Adhesión: al menos 60 de 148 iniciales al corte de M9.
La verificación de Monte Carlo con la fuente de D4 sigue pendiente. La fuente económica mantiene pendiente
la valorización incremental de la innovación 2, sin duplicar T-11.

| Entregable | Carpeta | Uso recomendado |
|---|---|---|
| EDT completa: árbol de 13 áreas y 54 paquetes | `01_EDT/01_Completa/` | Vista general o anexo amplio. El SVG conserva la calidad al ampliar; el PNG permite insertarlo como imagen. |
| EDT seccionada: 13 láminas de detalle | `01_EDT/02_Seccionada/` | Insertar las secciones en el cuerpo del informe para leer entregables, aceptación y responsables. Cada lámina tiene SVG y PNG con el mismo nombre. |
| Gantt de implementación y retiro del legado, M1–M24 | `02_Gantt/01_Graficos/Gantt_Implementacion_M01-M24` | Detalle de implementación, marchas blancas y convivencia con el sistema anterior. Disponible en SVG y PNG. |
| Gantt completa, M1–M56 | `02_Gantt/01_Graficos/Gantt_Completa_M01-M56` | Horizonte contractual completo, incluyendo 36 meses de operación. Disponible en SVG y PNG. |

La EDT completa y la seccionada representan **los mismos 54 paquetes**. No se suman como alcances distintos. Los códigos se mantienen iguales en la EDT, el diccionario y las barras de la Gantt.

## Fuentes editables

En `01_EDT/03_Editables/`:

- **`EDT_Completa_y_Seccionada.drawio`**: archivo principal de diagrams.net. Primera pestaña: árbol completo; siguientes 13 pestañas: secciones de detalle.
- `EDT_Completa.drawio`: únicamente el árbol completo.
- `EDT_Seccionada.drawio`: únicamente las 13 secciones.

En `02_Gantt/02_Editables/`:

- `Gantt_Completa_M01-M56.mmd`: fuente Mermaid de todo el horizonte.
- `Gantt_Implementacion_M01-M24.mmd`: fuente Mermaid del detalle de implementación.

Para diagrams.net: **Archivo → Abrir desde → Dispositivo** y seleccionar el `.drawio`. Para Mermaid Chart: copiar el contenido del `.mmd` en el editor. Las fuentes Mermaid usan febrero de 2027 como ancla provisional; las imágenes SVG/PNG muestran meses contractuales relativos.

## Material de apoyo

`03_Apoyo/` contiene:

- `Diccionario_EDT.csv`: código, nombre, entregable, aceptación, responsable, referencia a red, origen de ventana y requisitos asociados.
- `Red_Actividades_y_Holguras.csv`: 25 actividades y el hito G13 del T-15, precedencias, duración y holguras en días hábiles.

Estos archivos complementan los gráficos y facilitan su revisión.

## Versiones anteriores y generación

- `90_Archivo/01_Borradores_anteriores/`: borradores Markdown históricos. No constituyen la fuente oficial de esta versión.
- `90_Archivo/02_Vistas_anteriores/`: gráficos, vistas y fuentes anteriores conservados para consulta. **No usar para armar el informe actual.**
- `99_Generacion/`: scripts y datos para reproducir los entregables. No son documentos de entrega.

Para regenerar: ejecutar `python Informe-2/d2/99_Generacion/actualizar_entregables.py` desde la raíz del repositorio, y luego `exportar_png.cjs` con Node y el paquete Sharp disponible.

## Estado y fuentes

Versión detallada basada en los **T-14, T-15, T-18, T-19 y T-12 oficiales** del repositorio. La vista HTML explica las discrepancias de montaje, referencias EDT de innovaciones y criterios de autonomía que requieren conciliación antes de aprobar la línea base. Las ventanas de pruebas son una propuesta mensual derivada del T-15.

El árbol general es extenso: usar las láminas seccionadas para mantener la legibilidad en páginas de tamaño normal. La red CPM del T-15 se presenta como información de apoyo; las barras por paquete no representan una nueva red CPM calculada.
