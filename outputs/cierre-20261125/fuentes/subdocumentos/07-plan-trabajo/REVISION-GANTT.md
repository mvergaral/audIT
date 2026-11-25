# Revisión de la carta Gantt - v3, 2 de noviembre de 2026

Estado actualizado: preparación para propuesta final, versión 3.0, 25-11-2026. Ignacio Cuevas confirmó la revisión de EDT v2 y Gantt v3; el registro nominal está en REGISTRO-PARA-A6.md. Los cierres actuales se detallan en PENDIENTES-ENTREGA-FINAL.md. Las notas siguientes conservan el historial de revisión y no sustituyen ese estado.

Registro interno de trabajo; no se incluye en la propuesta técnica.

## Resultado

- PDF para revisión: `graficos/Gantt_Completa_Revisada.pdf` (12 páginas).
- Páginas individuales y manifiesto: `graficos/revisada/`.
- S7 referencia las nuevas páginas; se retiraron sus referencias a los nueve detalles repetidos M1-M56.
- Los PDF anteriores se conservan como material previo, sin referencias desde la sección vigente.

## Cambios

1. Panorama contractual con trece elementos EDT e hitos principales.
2. Red CPM: 25 actividades, G13, HT, enlaces críticos, adelanto FS-10 y fechas fijas H6/H11.
3. Siete detalles por frentes, con los 50 paquetes de implementación, sin división arbitraria cada seis filas.
4. Tabla de doce hitos: día planificado, límite, mes y margen. H6/H11 son inicios fijos.
5. Lámina de G13, reservas y control de fechas, sin atribuir probabilidades al gráfico.
6. Operación: cuatro paquetes M21-M56. Incluye aclaración de inicio y fin de M21.
7. Marcha blanca y aceptación diferenciadas; ventanas de innovaciones numeradas sin inventar nombres de fases.
8. Rombo = posición planificada; trazo ocre = límite contractual en los detalles. HT de actividad y margen de hito se distinguen.

## Datos y verificaciones

El generador verifica las 26 filas de red contra el T-15 vigente: duraciones, precedencias, fechas tempranas/tardías, holguras y criticidad. Además recalcula CPM con relaciones FS y FS-10 y contrasta todos los resultados. Verifica 54 códigos contra T-14, cobertura única por detalle y los doce meses de hitos contra `configuracion/economico.tex`. La versión de esa fuente se registra con SHA-256.

La extracción de E-25 p.74 devuelve el encabezado sin la tabla: la coincidencia con el catálogo económico del proyecto no acredita cotejo directo de la tabla original. Sigue pendiente la revisión humana de esa fuente.

Los PDF independientes tienen letra mínima de 12 pt en origen, sin texto fuera de página. A un ancho de 257,4 mm la escala teórica deja unos 10,4 pt; la medida definitiva requiere el PDF oficial compilado.

## Regeneración

Desde la raíz del repositorio:

`python -X utf8 recursos/Formato-Oferta-audIT/subdocumentos/07-plan-trabajo/graficos/generar_gantt_revisada.py`

Los generadores anteriores están archivados en `version-anterior/2026-11-02/`; el punto de entrada vigente es `generar_gantt_revisada.py`. No regenerar las Gantt vigentes con el generador histórico de láminas de D2: también reemplaza el bloque controlado de S7 con la estructura antigua. La revisión se limita al subdocumento 07 y no modifica esa herramienta externa.

## Integración compilada y pendientes

- PDF integrado tras la revisión de EDT: 46 páginas. Las doce láminas Gantt ocupan los folios/páginas PDF 32-43; la EDT ocupa 23-31. La versión previa de 61 páginas se conserva en `version-anterior/2026-11-02/informes/`.
- Compilación directa con LuaLaTeX: tres pasadas correctas; Biber correcto. Se obtuvieron las etiquetas reales de S3, S4 y S6 en compilaciones temporales para resolver referencias externas. El PDF integrado no contiene referencias `??`.
- Las doce figuras tienen letra mínima efectiva medida de 10,424 pt al insertarse en la plantilla, por encima de 9 pt. Se revisaron folios, orientación y contenido de las doce páginas.
- Las fuentes oficiales IBM Plex se descargan de CTAN a una carpeta local de compilación. MiKTeX resolvió los paquetes faltantes. No se modificaron los estilos ni la configuración de la plantilla.
- Comando reproducible desde la raíz: `python -X utf8 recursos/Formato-Oferta-audIT/subdocumentos/07-plan-trabajo/graficos/compilar_revision.py`. El primer uso necesita conexión para las fuentes/paquetes, MiKTeX con LuaLaTeX y Biber; los siguientes reutilizan las dependencias locales. No usa el `latexmk` cuyo manejo de argumentos falla en este Windows.
- Auxiliares, fuentes descargadas y logs: `graficos/revisada/compilacion/`, excluidos del versionado y retirados tras la revisión. El próximo build los regenerará. Ver `graficos/revisada/verificacion-integracion.json` para las comprobaciones.
- Esta es una copia integrada de revisión con el formato oficial; no sustituye el empaquetado completo de la entrega ni la aprobación humana.
- Pendientes de contenido: cotejo directo de E-25, revisión humana y asociación a la bitácora A-6 del responsable. La declaración de IA conserva ese pendiente sin atribuir una aprobación no realizada.

## Registro de asistencia IA para A-6

Herramienta: OpenAI Codex. Trabajo: conciliación documental y recálculo CPM, crítica de la versión previa, reorganización del anexo, generación vectorial, actualización de referencias y revisión visual. Se añadió una declaración específica en `declaracion-ia.tex` con revisión humana pendiente. Este registro debe asociarse a la bitácora A-6 del integrante responsable; no sustituye su revisión ni atribuye aprobación humana.

## Orden de archivos antes del push

Las versiones reemplazadas están en `version-anterior/2026-11-02/`, con `movimientos.json` y un LEEME. Se conservaron EDT y PERT activos. El generador vigente contiene sus propios rótulos y no depende de los scripts archivados. Los auxiliares y fuentes locales de compilación están excluidos por `graficos/.gitignore`. Los cachés `.codex-cache`, `tmp` y `debug.log` se excluyen del versionado sin borrar contenido local.
