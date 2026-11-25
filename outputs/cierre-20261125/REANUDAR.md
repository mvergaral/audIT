# Reanudar el cierre de la oferta final audIT

**Punto de pausa solicitado por el usuario el 25-11-2026, aproximadamente a las 13:21 de America/Santiago. La compilación global fue interrumpida y la oferta NO está declarada lista ni enviada.**

Leer primero este archivo y `ESTADO-EJECUCION.json`; después el plan en `docs/superpowers/plans/2026-11-25-cierre-entrega-final.md`. La base de las fuentes es `c140209`. Este checkpoint conserva las correcciones dentro de `outputs/cierre-20261125/fuentes/`; no se aplicaron al formato original ni se incorporaron cambios locales ajenos.

## Instrucciones confirmadas por el usuario

- Plazo confirmado: **25-11-2026 a las 14:00 de Chile**. Si se retoma después, confirmar el nuevo contexto de entrega sin asumir prórroga.
- **Ignacio Cuevas** sigue siendo el responsable real de revisión y firma del cierre D2/A-6. No hay confirmación de revisión efectuada.
- **Carlos Abarza** es el responsable de entregar los tres sobres y preparar el Sobre 1 físico.
- No existen respaldos administrativos reales en el repositorio. El usuario confirmó la autorización docente para piezas simuladas bajo Art. 93.
- Todos los emisores de esas piezas deben ser inequívocamente ficticios, incluyendo certificadora, auditores, aliados regionales y clientes de T-6. Bureau Veritas y Nexia deben sustituirse.
- El **video está listo según el usuario**, quien compartirá su enlace. Falta recibirlo e incorporarlo/verificarlo; no generar otro video.
- No se autorizó envío, publicación ni contacto con otras personas desde herramientas.

## Trabajo realizado

1. Snapshot del corte y cambios locales: `evidencia/linea-base.json` y `snapshot.json`. Se recuperaron 683 archivos, incluidos insumos D2 ocultos por sparse checkout.
2. Correcciones en copia aislada de fuentes, conservando precio, XLSX, malla y simulación. Los informes de revisión cotejaron 56 insumos económicos/planificación sin cambios.
3. Sobre 1 ampliado con **25 piezas simuladas autónomas**: identidad, RUT, vigencia, patente, constitución, poderes, accionistas, antecedentes tributarios/comerciales/laborales, capacidad bancaria, estados financieros 2023–2025, cartas, convenios, ISO y garantía. Fuentes: `fuentes/sobre1-antecedentes.tex` y `fuentes/administrativo/piezas.tex`.
4. A-2 completo, A-4 con alcance corregido, A-5 con inicio/término por pieza y A-6 con responsabilidad/confidencialidad y uso de Codex. No se atribuyó una revisión humana inexistente.
5. Última compilación administrativa concluida: **37 páginas**. Un ejemplar se conserva como `documentos/PROVISIONAL_Sobre1_20261125.pdf`. La última corrida administrativa posterior fue interrumpida: revisar las modificaciones finales de fecha/suscripción del poder y de A-6 antes de liberar.
6. Los cinco indicadores financieros están conciliados: liquidez 2,14; prueba ácida 1,88; leverage 0,38 al cierre; ROE 18,5 % sobre patrimonio promedio y ROA 12,8 % sobre activos promedio. Los balances cuadran en los tres ejercicios. Ver informe independiente.
7. Emisores ficticios y contactos `.example` conciliados entre S1, T-6, Anexo 1.A y Sobre 1. Mapa en `evidencia/emisores-ficticios.json`.
8. Subrogancia de gobierno corporativo incorporada en S1 y poder simulado: accionista ACC-TFEP-02, funciones societarias separadas del proyecto, conservando 22 profesionales de planta y dedicación del JP. El último ajuste fecha el poder consolidado al 25-11 y mueve su suscripción al final; falta cotejar PDF recompilado.
9. Diccionario independiente S5 agregado al flujo de integración; anexos S1/S2/S5 pasan al correlativo global. S2 ahora incluye sus seis supuestos en Anexo 2.F.
10. Nombres personales de integrantes reemplazados por roles corporativos en la propuesta técnica; identidad original preservada en el corte Git y evidencia. Declaración explícita de esta intervención y revisión final pendiente en los capítulos.
11. T-14/T-15/T-18 incluyen declaración IA propia y tabla con `\filasUsoIA`. Hubo un error de `titletoc` al usar `\section*` fuera del formulario: se corrigió al cierre `\audit@titulocierre` usado por T-11. **Verificar compilación de esos tres formularios antes de otra corrida larga.**
12. CP-PERF-03/CP-INT-25 parametrizados para el sitio secundario admisible; criterio GPS de plataforma sin exportación explícitamente no conforme si falta evidencia. SA-01/R-21 distingue escenario civil de fecha contractual. R-17 conserva riesgo alto y H4/H7/H12 sin margen, H11 protegido por A23.
13. Art. 46: 74 IDs únicos; conteo y localizadores corregidos, riesgo total 36, EMP-02 vinculado a nueva subrogancia, GEN-05 pendiente de revisión humana y RIE-05 parcial. No hay base para declarar todas las filas cerradas.
14. Sobre 3 revisado: cinco archivos del ZIP coinciden con sus hashes; 37 partidas conciliadas, 32.661 fórmulas y cero errores según evidencia y huella del recálculo anterior. No se modificó el modelo ni precio. Ver `informes/economico-plazo.md` y JSON.
15. Sitio y assets públicos respondieron 200. Tiene demostración integrada, pero identidad publicada distinta de la oferta. No se acreditó navegación completa, WCAG ni permanencia. El video fue declarado listo por el usuario; enlace pendiente.

## Estado exacto de la compilación

- MiKTeX funciona fuera del sandbox. LuaLaTeX y biber están instalados; Perl existe en `C:/Program Files/Git/usr/bin`, aunque el flujo final evita latexmk por problemas de escapado/rutas.
- `compilar_directo.py` reutiliza el integrador oficial de la copia y ejecuta LuaLaTeX/biber mediante archivos de entrada literales. El PDF administrativo ya compiló correctamente.
- Primera corrida técnica completó muchos PDF, pero falló en los tres encabezados IA de T-14/T-15/T-18. Se corrigieron sus fuentes.
- Segunda corrida global fue **detenida a petición del usuario durante la primera vuelta**. No hay manifiesto global final estabilizado ni ZIP técnico validado.
- Los auxiliares y PDF parciales permanecen localmente en `fuentes/salida/aux/final/`; no se suben para evitar confundirlos con finales. El estado de resultados se conserva en `evidencia/compilacion-checkpoint.json`.
- El compilador calcula hashes de fuentes y de auxiliares externos congelados. Al finalizar hay que verificar que las referencias cruzadas apunten a los folios definitivos: un cambio de páginas puede requerir una pasada adicional con los `.aux` finales congelados.

## Qué falta, en orden

1. Recuperar dependencias si se retoma desde otro clon: `python -X utf8 outputs/cierre-20261125/restaurar_contexto.py`. Solo completa archivos faltantes desde `c140209`; conserva las correcciones versionadas.
2. No volver a ejecutar `preparar.py`, `corregir.py`, `conciliar.py` ni los scripts de edición sobre las fuentes ya corregidas: varios no son idempotentes y podrían duplicar anexos o declaraciones. Son registro de lo aplicado.
3. Probar T-14/T-15/T-18 corregidos; luego ejecutar `compilar_directo.py` desde esta carpeta con permisos para MiKTeX. Terminar todas las vueltas y confirmar 31 PDF: SUBDOC00, 14 capítulos, 13 formularios y tres anexos independientes.
4. Ejecutar `python -X utf8 compilar_directo.py admin` y `python -X utf8 auditar_administrativo.py`. Verificar A-6 nuevo, poder fechado/suscrito al 25-11 y A-5/folio financiero 21. Si cambia el folio, actualizar S1 y T-6 antes de congelar.
5. Ejecutar `python -X utf8 verificar_final.py`. Es el verificador oficial con compatibilidad Windows y lectura correcta de la columna de fuente incrustada de `pdffonts`. **Este runner todavía no se ejecutó sobre un técnico final.** Conservar resultados crudos y dictaminar los hallazgos sin ocultarlos.
6. Inspeccionar los PDF finales: cinco láminas físicas S4, anexos S1/S2/S5, nuevas declaraciones IA, índices T-17, CP-PERF-03/INT-25 y tabla Art. 46. Los renders administrativos anteriores están en `revision/` solo localmente.
7. RIE-05 sigue parcial: hay costo estimado R-24 de CLP 3 millones y umbrales calculados, pero faltan pérdidas/frecuencias antes/después y costos incrementales por respuesta. No transformar ordinales de exposición en probabilidades ni presentar la reserva como costo por respuesta. Ver `informes/rie05-calculos.md/.json`.
8. Obtener enlace del video y comprobar acceso. Corregir con el responsable del sitio la razón social publicada «audIT Soluciones Tecnológicas de Misión Crítica S.A.» a «audIT Soluciones Tecnológicas SpA». No publicar cambios sin instrucción.
9. Obtener revisión humana del corte final por Ignacio Cuevas y responsables de cada bloque; completar el A-6 consolidado y las firmas que correspondan. El nombramiento de responsables y las suscripciones ficticias no acreditan esa revisión.
10. Armar tres ZIP oficiales, extraerlos a carpetas nuevas y cotejar inventario, CRC y SHA-256. Reutilizar los cinco económicos verificados si no cambiaron. No incluir temporales ni duplicar el Art. 46, que va dentro de SUBDOC00.
11. Carlos prepara el Sobre 1 físico, foliado y firmado, con respaldo digital, y presenta los tres sobres simultáneamente. Registrar recepción. Nada fue enviado.

## Archivos oficiales previstos

- `SOBRE1_AUDIT_ANTECEDENTES_OFERENTE_20261125.ZIP`
- `SOBRE2_AUDIT_OFERTA_TECNICA_20261125.ZIP`
- `SOBRE3_AUDIT_OFERTA_ECONOMICA_20261125.ZIP`

## Decisiones tomadas durante la ejecución

- Trabajar sobre copia aislada para preservar el checkout y sus cambios anteriores.
- Aplicar compatibilidad Windows y anexos en esa copia, sin modificar carpetas protegidas del formato original.
- Preservar precio, modelo y malla; describir sus límites y condiciones futuras sin inventar resultados.
- Generar documentación administrativa ficticia tras la autorización explícita del usuario, con emisores inconfundibles y contactos `.example`.
- Cubrir la subrogancia societaria mediante el órgano de propietarios, sin añadir un puesto de plantilla ni consumir horas del JP. La revisión humana debe ratificar esta propuesta del escenario.
- Mantener abiertas las revisiones humanas, el cálculo RIE-05 y las comprobaciones no realizadas.
- No abrir material privado de Drive tras el rechazo automático. El usuario aportará el enlace autorizado del video.

La reanudación debe partir de estos archivos, no rehacer la búsqueda histórica ni volver a generar las piezas ya escritas.
