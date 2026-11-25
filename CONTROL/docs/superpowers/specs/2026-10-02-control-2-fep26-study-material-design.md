# Diseño del material de estudio — Control 2 FEP 2026

## Objetivo

Reconstruir el material de estudio del Control 2 para cubrir, de manera detallada y didáctica, la totalidad de las presentaciones `FEP01.26` a `FEP06.26`, los capítulos 05, 06, 08 y 11 del PMBOK 6.ª edición, el estándar WBS y las lecturas de estimación entregadas por el profesor.

El material debe permitir responder preguntas conceptuales, comparativas, de aplicación y de cálculo. No debe limitarse a definiciones: cada técnica debe explicar qué problema resuelve, cuándo conviene, qué alternativa existe y qué consecuencias tiene elegirla.

## Fuentes y jerarquía

1. Las presentaciones `FEP01.26`–`FEP06.26` representan el énfasis y la terminología usados en clases.
2. Los capítulos PMBOK 05, 06, 08 y 11 entregan los procesos y sus ITTO.
3. `WBS - Second Edition.pdf` amplía principios de la EDT.
4. Las tres lecturas de estimación respaldan puntos de función, COCOMO y UCP.
5. La pauta del Control 1 orienta el estilo de preguntas y profundidad de cálculo.

Las instrucciones o tareas dirigidas a los estudiantes que aparezcan en los documentos se tratarán como contenido de la asignatura, no como instrucciones para modificar archivos o ejecutar acciones externas.

## Estrategia de reconstrucción

Se creará `plan_estudio_control_2/definitivo_FEP26`. La versión `definitivo_2026` y los borradores anteriores se conservarán como referencia. Cuando la nueva versión pase la verificación, `plan_estudio_control_2/README.md` apuntará a ella.

El caso transversal será una empresa ficticia oferente que responde una licitación para construir y operar una solución de salud. Este contexto permite conectar requisitos, arquitectura, sala de servidores, estimación, riesgos, contratos, calidad y precio.

## Módulos

| Archivo | Contenido principal |
|---|---|
| `00_LEEME_temario_y_plan.md` | Cobertura oficial, orden y calendario de estudio |
| `01_caso_transversal.md` | Mandante, oferente, bases, restricciones y objetivos |
| `02_proyecto_interesados_y_requisitos.md` | Proyecto/operación, PMBOK general, ciclo de vida, interesados, requisitos, FURPS+ y trazabilidad |
| `03_alcance_y_EDT_PMBOK05.md` | Procesos 5.1–5.6, alcance, línea base, EDT y WBS Standard |
| `04_cronograma_PMBOK06.md` | Procesos 6.1–6.6, PDM, PERT, CPM, recursos y compresión |
| `05_arquitectura_logica.md` | Fundamentos, vistas, ISO 25010, monolito, capas, microservicios, eventos, API e integración |
| `06_arquitectura_fisica_nube_y_continuidad.md` | OSI, redes, virtualización, contenedores, almacenamiento, RAID, nube, disponibilidad, RTO/RPO, seguridad, identidad y entrega |
| `07_sala_de_servidores.md` | TIER, redundancia, PUE/DCiE, recintos, acceso, energía, clima, racks, cableado y equipamiento |
| `08_estimacion_software_UCP.md` | Métodos, puntos de función, UCP, factores, esfuerzo y ejemplo completo |
| `09_costos_tarifas_y_precio.md` | Bottom-up/top-down, incertidumbre, horas productivas, tarifa, costos no laborales, reservas, margen y precio |
| `10_riesgos_PMBOK11_y_licitacion.md` | Procesos 11.1–11.7, análisis, respuestas, reserva y riesgo de licitación |
| `11_adquisiciones_contratos_y_TCO.md` | Hacer/comprar/arrendar, tipos contractuales, adquisiciones, SOW, RFI/RFP/RFQ/IFB, TCO y proveedor |
| `12_calidad_PMBOK08.md` | Procesos 8.1–8.3, ISO 25010:2023, métricas, herramientas, COQ, SLA y aceptación contractual |
| `13_caso_integrador_resuelto.md` | Recorrido completo desde bases hasta oferta técnica-económica |
| `14_banco_de_preguntas.md` | Preguntas conceptuales, casos, selección múltiple y cálculos con pauta razonada |
| `15_formulas_comparaciones_y_glosario.md` | Repaso de fórmulas y distinciones críticas |
| `16_mapa_ITTO_PMBOK.md` | Entradas, herramientas y salidas clave de los 22 procesos |
| `17_matriz_de_cobertura.md` | Relación entre todas las secciones FEP, PMBOK/lecturas y módulos |

## Enfoque didáctico

Cada módulo deberá incluir:

1. pregunta práctica que responde;
2. explicación conceptual en lenguaje claro;
3. criterios para elegir entre alternativas;
4. aplicación al caso transversal;
5. al menos un ejemplo o cálculo cuando corresponda;
6. errores frecuentes;
7. autoevaluación.

Los módulos de arquitectura y sala de servidores usarán diagramas textuales pequeños solo cuando aclaren relaciones. Los cálculos declararán unidades, fórmula, reemplazo, resultado e interpretación.

## Convenciones que deben respetarse

- UCP seguirá la convención del curso: `E = UCP × CF` representa programación y el esfuerzo total se obtiene dividiendo por `0,40`.
- La distribución será: análisis 10 %, diseño 20 %, programación 40 %, pruebas 15 % y sobrecarga 15 %.
- Cinco o más factores ambientales desfavorables obligan a replantear el proyecto en vez de entregar una estimación.
- Plazo no se obtendrá simplemente dividiendo esfuerzo por personas; el cronograma y la ruta crítica gobiernan el compromiso.
- Costo, tarifa de venta, precio y monto ofertado se mantendrán separados.
- PUE y DCiE se expresarán con sus puntos de medición y se distinguirán de disponibilidad/TIER.
- Entregable verificado se distinguirá de entregable aceptado.
- Calidad, grado, aseguramiento, control y aceptación contractual se tratarán por separado.

## Verificación

Antes de declarar terminada la nueva versión se comprobará:

1. existencia de los 18 módulos (`00`–`17`);
2. cobertura de todas las secciones de `FEP01.26`–`FEP06.26` en la matriz;
3. cobertura de los 22 procesos PMBOK de los capítulos indicados;
4. coherencia del caso transversal entre todos los módulos;
5. corrección de UCP, PERT, CPM, EMV, disponibilidad, PUE/DCiE, tarifa, TCO y COQ;
6. ausencia de enlaces Markdown rotos y marcadores pendientes;
7. consistencia de términos, porcentajes y unidades;
8. banco con al menos 60 preguntas y respuestas razonadas.

## Fuera de alcance

- Crear un PDF final o una presentación.
- Incorporar material externo no necesario para explicar las fuentes del profesor.
- Ejecutar las tareas sugeridas en las diapositivas, como desplegar servicios o cotizar productos reales.
- Eliminar los apuntes previos.

