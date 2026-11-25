# Registro de cambios y justificación técnica de D3

## audIT Soluciones Tecnológicas SpA · Licitación TFEP-01/2026 · Caso 10, Transportes Curimón S.A.

**Revisión de D3 del 24 de noviembre de 2026.** La revisión en `codex/cierre-entrega-3` cubre S4.1, S5 y su anexo, S6 y los formularios T-9/T-10, S13.2 y la ficha 2 de T-19. Los ajustes de software y continuidad se incorporaron en los archivos compartidos S4 y T-11.

**Línea base de la revisión.** Se partió del commit `a59b9d2` y de la Entrega 3.2 con el ajuste `8a7d35c`. La revisión de integración tomó como referencia `5011546` en `main` y la conciliación de S3, S7 y T-14/T-15/T-18 que incorporó D2. Se usó el anexo del Art. 46 para localizar las observaciones y la planilla publicada para cotejar recursos, plazos y costos. [Planilla 3.2](../../outputs/3.2/Entrega-3.2/INFORME3_AUDIT_PLANILLA_3.2_20261115.xlsx) · [Anexo del Art. 46](../../recursos/Formato-Oferta-audIT/salida/final-por-subdocumento/AUDIT-Anexo-Art46-Resolucion-Observaciones.pdf)

**Resultado de compilación.** Nueve PDF verificados, con 244 páginas en total. Codex asistió la conciliación, la redacción, los diagramas y la verificación formal. La validación humana queda pendiente.

## 1. Arquitectura lógica y Formulario T-11

Fuentes modificadas en `subdocumentos/04-arquitectura/`, con apoyo de los generadores de D3 para publicar las figuras.

| Área o archivo | Qué se cambió | Por qué se cambió |
|---|---|---|
| `contenido.tex` y `formularios/T-11.tex` · Versiones | Se especificaron Flutter 3.50.0, React 19.3.0, Next.js 16.x LTS y Go 1.27.4. Se incorporaron fuentes de los fabricantes y criterios para fijar parches y actualizar versiones. | ARQ-01 y ARQ-06 requerían respaldo verificable, vigencia del soporte y consistencia entre el diseño y la ficha de componentes. [Flutter](https://docs.flutter.dev/release/release-notes) · [React](https://react.dev/versions) · [Next.js](https://nextjs.org/support-policy) · [Go](https://go.dev/doc/devel/release) |
| `contenido.tex` · Registro de ADR | Se identificó el estado propuesto de cada uno de los ocho ADR, con alternativas, criterio y verificación. El registro distingue la fecha de propuesta, la aprobación por acta y la fecha efectiva. | ARQ-02 pedía estado por decisión. La aprobación debe corresponder al acta de cada ADR. |
| `contenido.tex` · Dimensionamiento de soporte | Se especificaron seis agentes regulares de Mesa N1 y un equivalente para suplencias y picos. Campo conserva 80 h internas de coordinación al mes en operación y el proveedor atiende por visita. La transición a atención externa comienza en M19. | ARQ-03 pedía dimensionar la mesa y el soporte. La planilla 3.2 detalla la cobertura en `Mesa de ayuda`, `Contrato de soporte` B2, B7 y B13 y `Parámetros corrección` B78:B83. |
| `contenido.tex` · Evidencia de jornada y continuidad | Se explicitó el contraste con la cascada de evidencia de S5 antes de asignar a un conductor sin rastro instrumental. La réplica personal en el sitio secundario quedó condicionada a validación jurídica antes de H2. | ARQ-07 exige identificar el dato faltante y su contingencia. ARQ-05 requiere respaldo de la vía de transferencia y ensayo de recuperación para H7. |
| `contenido.tex` y `s4_secuencias.py` · Figura 4.10 | El costo se versiona por viaje y la liquidación mensual se agrupa por beneficiario y detalla tramo y asignación ejecutada. La secuencia conserva el acuse contable y agrega la regla de un cargo base por tramo. | Evitar doble liquidación ante reasignación y reflejar en S4.1 la regla de datos incorporada en S5 por DAT-05. |
| `contenido.tex` y `publicar_graficos.py` · Figuras 4.2, 4.3, 4.5, 4.6, 4.9 y 4.11 | Se publicaron versiones vectoriales de los seis diagramas de contextos, resiliencia, integraciones, capa anticorrupción, analítica y modelo táctico. | La revisión visual confirmó el montaje en PDF y el verificador midió 9 pt efectivos, el mínimo del Art. 40.4. |
| `formularios/T-11.tex` · Numeración y referencias | La tabla principal pasó a identificarse como T-11.1. La ficha incluye sus referencias técnicas y su declaración de uso de IA en el propio PDF. | ARQ-06 observaba la numeración coincidente con S4 y la remisión de las fuentes al capítulo. |

## 2. Modelo de datos y diccionario independiente

Fuentes modificadas en `subdocumentos/05-datos/`, con la versión editable de la Figura 5.1 en `Informe-2/D3/graficos/`.

| Área o archivo | Qué se cambió | Por qué se cambió |
|---|---|---|
| `contenido.tex`, `anexos.tex` y Figura 5.1 | Se separaron titular del equipo, empleador del conductor y beneficiario de liquidación. El detalle vincula la asignación ejecutada y el tramo. Una reasignación previa conserva el tramo, un relevo en ruta abre otro y una rectificación referencia el cargo original mediante un ajuste. | DAT-05 señalaba que una sola identidad cubría tres roles y que la clave por viaje permitía duplicar cobros. El cargo base queda restringido a uno por tramo. |
| `anexos.tex` · Diccionario y capacidad | Se publicó el diccionario en un PDF independiente. Los atributos, restricciones y supuestos de tamaño quedaron en el anexo y el cuerpo conservó el análisis del modelo. | DAT-01 pedía separar el diccionario. DAT-02 pedía llevar la explicación extensa al texto y reservar las celdas para comparar datos. |
| `contenido.tex` · Calidad y disponibilidad | Se alineó la disponibilidad mensual con S4 y S10, con 99,9 % para servicios críticos y 99,5 % para los servicios de criticidad alta definidos en S10. La medición toma la transacción completa por servicio y excluye ventanas aprobadas. | DAT-04 pedía que datos y arquitectura usaran el mismo perímetro de medición. Calidad aún debe aplicar el criterio por servicio en T-17. |
| `contenido.tex` · Privacidad y recuperación | Se documentó la vía contractual propuesta para transferir datos personales. Mientras se valida antes de H2, los ensayos en Brazil South usan datos sintéticos y artefactos técnicos. | ARQ-05 vincula la réplica internacional con R-24 y el ensayo de recuperación de H7. La 3.2 provisiona asesoría legal y nube en `Detalle proveedores D4`. |
| `declaracion-ia.tex` · Cierre | Se recompuso la declaración de IA y se verificó su última página. | DAT-03 observaba una página de continuación con encabezado y sin filas. |

## 3. Metodología y formularios T-9 y T-10

Fuentes modificadas en `subdocumentos/06-metodologias/`.

| Área o archivo | Qué se cambió | Por qué se cambió |
|---|---|---|
| `contenido.tex` y `formularios/T-9.tex` · Gobierno y comunicaciones | Se cruzaron los trece actores de S2 con información, emisor, destinatario, frecuencia, canal y escalamiento. Se precisaron las atribuciones del titular y suplente funcionales que Curimón designará por acta. La nueva matriz quedó como Tabla 6.A y la tabla DevSecOps conservó el número 6.3. | MET-01, MET-02 y MET-03 pedían ampliar la cobertura, formalizar decisiones y dar contenido propio a T-9. S9 y T-13 ya hacen referencia a la Tabla 6.3. |
| `contenido.tex` y `formularios/T-9.tex` · Adhesión | Se asignaron al Líder Funcional el anexo de adhesión, enrolamiento, control mensual por RUT y escalamiento de los 148 transportistas iniciales. Se definió el refuerzo con 59 o menos adhesiones en M9 y se incorporaron al reporte de T-9 los indicadores y denominadores de S3, distinguiendo adhesión, consentimiento, montaje y activación. | MET-08 pedía incorporar la adhesión al método siguiendo los paquetes EDT 9.1 a 9.3 de S7 y T-14. |
| `formularios/T-10.tex` · Sprints A09 y A20 | Ocho sprints A09 y cinco A20 quedaron con requisitos, incremento, dependencias, pruebas, perfil revisor y criterio de salida. A09-7 entrega el candidato en d180. G13 se libera en d182 tras el ensayo G13-Q y la práctica comienza en d192. Los candidatos de A09-8 y A20-5 pasan a las revisiones de H4 y H9. | MET-03 y MET-04 pedían un plan de incrementos utilizable, enlazado a T-12, T-17 y los hitos de S7/S9. La nivelación por perfil depende de T-15. |
| `contenido.tex` y `formularios/T-10.tex` · Deuda técnica | Se incorporó el carril Kanban de deuda a EDT 13.4. Software comparte con mejoras 160, 120, 80 y 40 h variables por mes a partir de M21, M25, M33 y M45, respectivamente. | MET-05 pedía identificar paquete y capacidad durante la operación. Las horas provienen de `Soporte por perfil` y las reservas que comparten bolsa se descuentan según T-15. |
| `formularios/T-10.tex` · Cierre M21–M24 | Se registraron 1.669 h ya contratadas, con 879 h en EDT 6.5 y 790 h en EDT 7.2. Se acepta en el plan la reserva de 69 h en Gestión de Servicio según S7, condicionada a validar el titular y la cobertura en H1. | El desglose del CSV vigente de D3 coincide con T-15. La condición de H1 conserva la cobertura de SLA, cambios y guardias. [Evidencia de D2](../../output/auditoria-d2-32/INDEX.md) |
| `contenido.tex` y `formularios/T-10.tex` · DevSecOps | Se identificaron GitLab Premium Self-Managed y SonarQube Server Developer Edition como suscripciones separadas del cómputo. Se citó la documentación de ramas protegidas de GitLab para el flujo de integración. | MET-06 pedía una fuente relacionada con la práctica. MET-07 pedía alinear la metodología con la arquitectura. La 3.2 registra las suscripciones en el bloque `Licencias D3` de `Proveedores`. [Documentación de ramas protegidas](https://docs.gitlab.com/user/project/repository/branches/protected/) |

Los pagos de GitLab figuran en M1, M13, M25, M37 y M49, y los de SonarQube en M4, M16, M28, M40 y M52. El presupuesto neto conjunto de referencia es CLP 38.032.600. El período y el precio de SonarQube se mantienen como supuesto comercial de la 3.2. La valorización se presenta en el Sobre N.º 3.

## 4. Innovación 2 y ficha 2 de T-19

Fuentes modificadas en `subdocumentos/13-innovaciones/`.

| Área o archivo | Qué se cambió | Por qué se cambió |
|---|---|---|
| `contenido.tex` y `formularios/T-19.tex` · Piloto y lotes | Se especificaron diez kits en el piloto interno de San Bernardo en M6 y lotes externos de 60, 60 y 52 kits en M7, M8 y M9 en cinco terminales. El escenario de S7 acumula 182 en M9. Cada orden se libera con adhesión aplicable, stock, ventana y reserva del proveedor. Los desvíos se reprograman con las activaciones y el efecto en caja. | El nuevo S7 y T-18 coinciden con la hoja `Instalación por lote` y `Parámetros corrección` B6:B8. Se retiraron de S13.2 y T-19 los 164 montajes y la ventana física de M16 a M18 del cronograma anterior. |
| `contenido.tex` y `formularios/T-19.tex` · Alcance y recursos | Se imputaron planificador, tablero, integración y homologación a EDT 12.2. La 3.2 considera 560 h de implementación y 576 h de operación dentro del presupuesto de personal. | Mantener el alcance del presupuesto de `Innovaciones` y `Atribución innovaciones` y tramitar capacidad adicional mediante control de cambios. |
| `contenido.tex` y `formularios/T-19.tex` · Métricas y madurez | Se conservó TRL 2. Para el piloto se definieron una muestra mínima de 20 intervenciones elegibles, metas de 20 % menos preparación inútil y 95 % de validación al primer intento. Se mide el recambio modular hasta 30 min y se comprueba por separado la referencia de montaje integral de 140 min en CP-UAT-02. | INN-01 e INN-05 pedían un método de medición y base para atribuir el beneficio. El escenario económico base mantiene el beneficio monetario sin reconocer hasta contar con resultados del piloto. |

## 5. Anexo del Art. 46 y archivos verificados

| Archivo o grupo | Qué se cambió | Por qué se cambió |
|---|---|---|
| `anexos/observaciones-informe3.tex` y anexo PDF | Se actualizaron las respuestas, localizadores y estados de las observaciones pertinentes a D3. El PDF central conserva los 74 identificadores del conjunto. | Permitir el cotejo entre la observación original y el cambio en su documento. |
| PDF y Markdown de S4, S5, S6 y S13 | Se recompilaron con la regla común incorporada en `624575f`. El anexo central conserva las respuestas de D2 para ALC/PLA y las actualizaciones de D3. | GEN-01 concentra la resolución en el anexo central y preserva el índice de cada subdocumento. |

| PDF final | Páginas | Resultado o alcance |
|---|---:|---|
| [AUDIT-Subdocumento4.pdf](../../recursos/Formato-Oferta-audIT/salida/final-por-subdocumento/AUDIT-Subdocumento4.pdf) | 85 | S4.1 con las seis figuras vectoriales a 9 pt efectivos. S4.2 conserva el incumplimiento del plano físico. |
| [AUDIT-Formulario-T-11.pdf](../../recursos/Formato-Oferta-audIT/salida/final-por-subdocumento/AUDIT-Formulario-T-11.pdf) | 20 | Tabla T-11.1 y referencias técnicas en el formulario. |
| [AUDIT-Subdocumento5.pdf](../../recursos/Formato-Oferta-audIT/salida/final-por-subdocumento/AUDIT-Subdocumento5.pdf) | 30 | Figura 5.1 a 9 pt efectivos. Cierre de la declaración de IA comprobado. |
| [AUDIT-Subdocumento5-Anexos.pdf](../../recursos/Formato-Oferta-audIT/salida/final-por-subdocumento/AUDIT-Subdocumento5-Anexos.pdf) | 41 | Diccionario de datos en archivo independiente. |
| [AUDIT-Subdocumento6.pdf](../../recursos/Formato-Oferta-audIT/salida/final-por-subdocumento/AUDIT-Subdocumento6.pdf) | 20 | Matriz de comunicación, metodología y herramientas. |
| [AUDIT-Formulario-T-9.pdf](../../recursos/Formato-Oferta-audIT/salida/final-por-subdocumento/AUDIT-Formulario-T-9.pdf) | 4 | Gobierno, comunicaciones y adhesión. |
| [AUDIT-Formulario-T-10.pdf](../../recursos/Formato-Oferta-audIT/salida/final-por-subdocumento/AUDIT-Formulario-T-10.pdf) | 5 | Trece sprints, pruebas y criterios de salida. |
| [AUDIT-Subdocumento13.pdf](../../recursos/Formato-Oferta-audIT/salida/final-por-subdocumento/AUDIT-Subdocumento13.pdf) | 26 | S13.2 con recursos y método de medición. |
| [AUDIT-Formulario-T-19.pdf](../../recursos/Formato-Oferta-audIT/salida/final-por-subdocumento/AUDIT-Formulario-T-19.pdf) | 13 | Ficha 2 con el método y criterios de decisión del piloto. |

El verificador evaluó 21 puntos. Confirmó folios correlativos por archivo, fuentes incrustadas y referencias resueltas. Reportó un incumplimiento de letra en `fisica-completa.pdf` de S4.2, con 4,38 pt efectivos, y dos avisos sobre citas a tablas de formularios y puntuación. [Resultado de la verificación](../../recursos/Formato-Oferta-audIT/salida/verificacion-final-por-subdocumento-d3.md)

## 6. Pendientes compartidos para el armado final

| Frente | Pendiente |
|---|---|
| Infraestructura y Calidad | Confirmar factibilidad de ExpressRoute y la alternativa con S8/T-16. Corregir en S4.2 el emplazamiento y enlace de la autoridad tributaria de ARQ-08, y redistribuir el plano para alcanzar 9 pt. Acreditar la vía jurídica y el ensayo de recuperación de R-24 para H7. |
| PMO y responsables de la planilla | Validar la adhesión, el stock y las ventanas por terminal del escenario de 182 montajes acumulados en M9. Alinear las glosas de `Feedback 3.2` P5 y `Conciliación técnica` fila 17 con la fecha vigente de transición en `Parámetros corrección` B83, M19. |
| PMO y Calidad | Confirmar en H1 la cobertura de las 69 h de conducción técnica. Nivelar la capacidad por sprint con T-15 y S11. Incorporar a T-17 las variantes de reasignación y verificar que los ensayos SLA usen el perímetro de S10. Medir la línea base y el beneficio de la innovación 2 en el piloto de M6. |
| Integración de la oferta | Regenerar S9 con la tabla de observaciones en el anexo central. Conciliar la foliación general del sobre durante el ensamblaje. |
