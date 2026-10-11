# Consideraciones de D2 para los demás equipos

Informe 2. D2 entregó S3 y Formulario T-12, S7 y Formularios T-14, T-15 y T-18, filas 37 a 52 de la
tabla del Art. 46 e innovaciones 1 y 4 (S13 y T-19). Todo en `recursos/Formato-Oferta-audIT/`.

## Conciliación vigente solicitada a D2 — 11 de octubre de 2026

Los siguientes puntos son el registro histórico de conciliación. El acuerdo posterior de capacitación y adhesión está en `ACUERDO_CAPACITACION_ADHESION.md`; sus decisiones sustituyen los pendientes de definición de los puntos 2 y 3. Este registro actualiza la coordinación; no acredita que los cambios estén incorporados ni que las comprobaciones técnicas estén aprobadas.

| Punto | Acción y alcance | Evidencia de cierre |
|---|---|---|
| 1. Documento en cabina | Corregir S3 y T-12: el retorno satelital debe entregar la representación completa y conforme del documento en cabina, no solamente el folio. Mantener al sistema contable como emisor. Conciliar con S4 y el riesgo R-28 de S8 incorporados por D4. | S3/T-12/S4/S8 coherentes; comprobación integral de los 90 segundos documentada. Hasta contar con ella, la factibilidad permanece pendiente. |
| 2. Capacitación y red | Acordar con D4 una sola planificación: S8 adelanta la capacitación 10 días respecto del término de la construcción, mientras T-15 inicia A13 después de A09. No presentar ambas como una misma línea base. | Relación de precedencia y eventual desfase explícitos; malla, fechas, holguras, ruta crítica, Gantt/PERT y simulación recalculados con el mismo supuesto. Actualizar los resultados de S7/S8 que dependan de él. |
| 3. Refuerzo de adhesión | Conciliar con D1/D4 el umbral: D4 usa menos de 42 transportistas firmados y las pruebas de D1 menos de 60. Definir el universo que constituye el denominador del 40 %, la fecha de corte, qué cuenta como firmado y la regla de redondeo. | Una fórmula y un umbral comunes en riesgos y pruebas. No elegir 42 o 60 sin justificar el denominador. |
| 4. Legibilidad y archivos | Incorporar vista general y detalles de EDT/Gantt con letra de al menos 9 puntos en el tamaño final de impresión. Actualizar en S7 el texto que aún describe la EDT anterior y resolver los archivos faltantes de los PERT. | PDF revisado a escala final; texto coherente con la EDT vigente; ambos PERT generados y referencias resueltas en una compilación reproducible. La existencia del SVG no acredita la disponibilidad del PDF requerido. |
| 5. Innovación 2 | Recuperar en S13/T-19 la programación dinámica de intervenciones por oportunidad de patio. El diseño y calendario acordados siguen vigentes: piloto de 10 camiones en M6, montaje propio M6–M9 con flota propia completa en M9, terceros adheridos desde M7, pausa M11–M15 y continuación M16–M18. La integración de D4 no sustituye este acuerdo por la versión antigua. | S13/T-19 coherentes con EDT 12.2, paquetes 4.1/4.2 y calendario de S7; comprobar que las fuentes de generación no vuelvan a introducir la versión anterior. |

La **valorización incremental de la innovación 2 permanece pendiente en la fuente económica**. Debe identificar los costos adicionales de planificador, integración, homologación y operación, evitando duplicar el equipamiento contractual ya incluido en T-11. No dar por cerrado el costo con la sola corrección de S13/T-19.

El uso de IA en esta conciliación debe asociarse a la bitácora A-6 del responsable. La revisión humana y el cierre de cada evidencia permanecen pendientes; no se atribuye una revisión a una persona sin confirmación.

### Avance documental del 11 de octubre de 2026

- S3 y T-12 actualizados: representación completa y conforme en cabina, bloqueo de salida sin ella y comprobación integral de los 90 segundos pendiente, vinculada a S4/R-28.
- S13/T-19 ya contenían el diseño por oportunidad de patio en el checkout revisado. Se explicitó la flota propia completa en M9 y se conservó el calendario acordado. La valorización incremental sigue pendiente en la fuente económica.
- S7 actualizado: descripción de la EDT vigente, vistas generales y detalles vectoriales de EDT/Gantt, y PDF disponibles de ambos PERT. Las 44 láminas de revisión están en `03_Apoyo/Laminas_EDT_Gantt_PERT.pdf`, con IBM Plex Sans incrustada y texto mínimo de 10 puntos en origen. Los archivos fuente de figuras se incluyen expresamente en el repositorio para evitar PERT faltantes en otro checkout.
- Once controles documentales y de cálculo automatizados pasan. La compilación oficial y la medición de escala en el PDF de S7 siguen pendientes: MiKTeX reporta acceso denegado/configuración incompleta y la orden presenta problemas de interpretación en Windows. El verificador general no puede evaluar los PDF oficiales que no se generaron. El cuaderno de revisión no sustituye la oferta con folios y firmas.
- Acuerdo ejecutado: A13 en días 182–222, HT 38 y HL 18; A06 HL 24; término día 420. G13 condiciona el inicio a PREPROD/material listo al cierre del sprint 7; complemento del sprint 8 dentro de los 40 días. Adhesión: 60 de 148 iniciales al corte de M9, RUT único, ambas modalidades y anexo firmado, vigente, no revocado y registrado. S3/T-12, S8/T-16 parcial y pruebas de D1 actualizados. Pendientes: definir con D3 funciones certificadas, integrar catálogo original de D4 y verificar Monte Carlo; 82,3 %, 14,1 %, 92,1 % y 0,1 % son resultados reportados, no verificados aquí.

## Decisiones que afectan a toda la oferta

| Decisión | Valor | Dónde está |
|---|---|---|
| Inicio del contrato | Mes 1 = febrero de 2027 (supuesto SA-01). Es el único inicio que deja los meses 16 y 21 fuera de dic–abr | S3 3.2.6, T-12 |
| Calendario | Mes 16 = mayo 2028, mes 21 = octubre 2028, mes 56 = septiembre 2031. La marcha blanca E1 (feb–abr 2028) cae siempre en temporada de fruta | S3 3.1, S7 7.3.2 |
| Sistema de gestión de 2013 | Sustitución función por función tras capa anticorrupción. Asignación, control de viaje y liquidación en el mes 16. Órdenes y tarifas a clientes en el mes 21. Solo consulta hasta el mes 24 | S3 3.2.4 |
| Documento electrónico sin cobertura | Siempre lo emite el sistema contable: emisión anticipada desde la orden, o envío satelital de datos y retorno de la representación completa y conforme a cabina. Comprobación integral de los 90 segundos pendiente; corregir S3/T-12 conforme al punto 1 | S3 3.4.2, T-12; conciliación con S4/S8 R-28 |
| Costo antes de la renegociación de 2027 | Estudio de costo por ruta y contrato en el mes 6 (EDT 2.5). El costeo por viaje entra en producción en el mes 16 | S3 3.2.1 |
| Montaje a bordo | Flota propia en los meses 6 a 9 (piloto de 10 en el mes 6). Terceros adheridos desde el mes 7. Pausa en los meses 11 a 15. Reanuda en los meses 16 a 18 | S7 7.3.3 |
| Nombres canónicos de componentes | Los seis contextos de S4 4.1.3: Planificación y tráfico, Flota y activos, Personas y cumplimiento, Telemetría y geocercas, Operación de fletes, Liquidación y costeo | S3 3.3.1 |
| Comités | Los de S6: Comité Ejecutivo, Comité de Proyecto, Comité de Arquitectura, Comité de Operación | S3, S7 |
| EDT | 13 elementos y 54 paquetes. Usar estos códigos en cualquier referencia a la EDT | S7 7.1, T-14 |
| Dotación | 14 → 24 → 30 → 33 → 37 (peak, meses 13 a 17) → 30 → 26 → 16 en operación | S7 7.2.2, T-15 |
| Horas hombre | 93.760 en la implementación y 92.160 en la operación. Solo en el T-15 | T-15 |
| Prioridad de requerimientos | 1 (falla deja salir un camión o pierde prueba), 2 (sostiene criterio o restricción), 3 (optimiza) | S3 3.2.8, T-12 |
| Códigos de origen | CA-nn (criterio Cap. 18), R-nn (restricción Cap. 10), DP-nn (decisión del 16.1), RN-nn (regla de negocio), SA-nn (supuesto de alcance) | T-12, glosario |

EDT de primer nivel: 1 Gestión, 2 Levantamiento y diseño, 3 Plataforma, 4 Equipo a bordo,
5 Servicios Etapa 1 (5.1 a 5.6 = los seis contextos, 5.7 portal del transportista), 6 Integraciones,
7 Datos y migración, 8 Servicios Etapa 2, 9 Adhesión, 10 Calidad y pruebas, 11 Implantación,
12 Innovaciones (12.1 a 12.5, una por innovación), 13 Operación.

## Pendientes por equipo

### D3 (S4, S5, S6, innovación 2)
- S4 llama varias veces «sistema contable de 2013» al sistema de gestión de transporte de 2013. Son sistemas distintos (Caso, cap. 5, p. 12).
- La tabla de inventario de S4 (4.1, `tab:4-inventario`) usa nombres distintos de los seis contextos («Despacho y asignación», «Gestión documental», «Tarifas y liquidación»).
- S4 no tiene todavía el ADR del sistema de 2013 que promete la fila 60 del Art. 46. Debe registrar la misma decisión de S3 3.2.4.
- S4 remite el mecanismo del documento sin cobertura a su sección 4.1, que aún no lo trae. Debe reflejar la decisión de S3 3.4.2.
- S6 dice «marcha blanca de 60 días» en ambas etapas. El Art. 17.1 fija 3 meses (E1) y 2 meses (E2).
- S6 dice que audIT compra «148 computadores y 34 CANclick» en los meses 1 y 2. El hardware lo compra el mandante (Caso, cap. 11) y el T-11 declara 182 equipos.
- S6 cita «SLA 99,5 %». El Art. 78.2 exige 99,9 % para lo crítico.
- Ficha T-19 de la innovación 2: D2 adopta piloto de 10 camiones en M6, montaje propio M6–M9, terceros adheridos desde M7, pausa M11–M15 y continuación M16–M18. La planificación la ubica en EDT 12.2 y la relaciona con los paquetes 4.1 y 4.2. D3 debe reflejar este acuerdo en su ficha consolidada.
- Documento sin cobertura: exigir la representación completa y conforme que vuelve a cabina; quedan pendientes su tamaño máximo y la comprobación integral de los 90 s, en coordinación con D3/D4 y R-28 de S8. D2 mantiene al sistema contable como emisor fiscal.
- Innovación 2: quedan pendientes los costos incrementales del planificador, integración, homologación y operación. La valorización no debe duplicar el stock contractual de T-11 ni presentar ahorros medidos sin línea base.

### D4 (S4 física, S8, innovación 3)
- En la malla del T-15 (`7-malla`), la actividad A18 «Escalamiento telemático e instalación progresiva a bordo» (días 240 a 360) se interpretó en S7 así: meses 13 a 15, integración por plataforma sin tocar camiones. Meses 16 a 18, montaje físico. Conviene ajustar su descripción para que no parezca montaje en temporada de fruta.
- La figura `figuras/13-innovaciones/cartera.png` probablemente tiene el nombre antiguo de la innovación 1. Ahora se llama «Expediente verificable del transportista».
- Ficha T-19 de la innovación 3: sus códigos EDT deben pasar a 12.3 y a los paquetes 4.2 y 5.2. Meses de montaje coherentes con S7: 6 a 10, y 16 a 18.
- S8: la red de riesgos puede tomar las actividades y holguras de S7 7.3.1 y los supuestos SA-01 a SA-08 de S3. El SA-08 (apagado 2G y 3G) ya remite a S8.

### D1 (S9, T-17, innovación 5, consolidación del Art. 46)
- El T-17 usa códigos EDT provisionales (`EDT-3.1`, `EDT-2.3`…). La correspondencia ya está en el T-12, campo de componente de cada requerimiento. Los casos de prueba CP-… de D1 se citan allí tal cual.
- Las filas generales 01, 08, 09 y 12 del Art. 46 nombran a S3. Su respuesta debe apuntar a las nuevas secciones (T-12 adjunto, sin títulos seguidos de tabla, sin pendientes internos).
- Ficha T-19 de la innovación 5: sus códigos EDT deben pasar a 12.5 y a los paquetes 4.1 y 5.1.
- Ventanas de prueba de S9: pruebas integrales en los meses 10 a 12 (A12), certificación E2 en los meses 17 y 18 (A22), pruebas de DR en junio y noviembre de cada año de operación.

### Compilación (resultado del 07-10-2026)

- Compilan S1, S2, S3, S4, S5, S7, S8, S9 y S13 con todos sus formularios. **S6 no compila**: `06-metodologias/contenido.tex` usa `\audIT`, que la clase no define (línea 8 y siguientes). Mientras falle, S7 queda con dos referencias sin resolver (`sec:6-gestion-pmbok` y `sec:6-gestion-ceremonias`) y `compilar.py subdocs` no copia ningún PDF a `salida/`.
- Nota histórica, sustituida el 11-10-2026: los PERT que utilizaba S7 estaban ignorados por git. S7 ahora usa los PDF de `subdocumentos/07-plan-trabajo/graficos/`, incluidos mediante una excepción local de `.gitignore` y reproducibles con `Informe-2/d2/99_Generacion/generar_laminas_impresion.py`. El procedimiento anterior era:
  `rsvg-convert -f pdf -o figuras/07-plan-trabajo/pert-etapa1.pdf figuras/07-plan-trabajo/pert-etapa1.svg` (y lo mismo con `pert-etapa2`).
  Para que salgan en IBM Plex, enlazar las fuentes una vez:
  `mkdir -p ~/.local/share/fonts/ibm-plex && ln -sf /usr/share/texmf-dist/fonts/opentype/ibm/plex/*.otf ~/.local/share/fonts/ibm-plex/ && fc-cache -f`.
- `verificar.py` se cae si existe `salida/informe2/manifiesto-s1-s2.json` (D1) y no están sus PDF de anexos. Sin ese manifiesto, el resultado es: cumple todo salvo el punto 8 (referencias a S6) y los avisos de siempre (punto y coma del código TikZ, marcadores de revisión humana).
- Paquetes de Arch necesarios: `texlive-binextra`, `texlive-fontsextra` y `texlive-luatex`.

### Todos
- Las declaraciones de IA de S3, S7 y S13 tienen `\marcador{...}` en la columna de revisión humana. Hay que llenarlas después de revisar, nunca antes.
- Las figuras 3.4 (cascada) y 7.4 (Gantt) quedan en página propia con espacio libre. Revisarlo al armar la versión final.
