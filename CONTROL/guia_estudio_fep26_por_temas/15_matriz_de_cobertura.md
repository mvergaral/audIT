# Matriz de cobertura de las fuentes

Esta matriz sirve para comprobar dónde estudiar cada sección. “Cubierto” significa que el apunte explica el concepto; no que reproduzca literalmente las diapositivas.

## FEP01.26 — Introducción a Arquitectura de Software

| Sección de la presentación | Apunte | Cobertura |
|---|---|---|
| 1 Fundamentos | `05` | concepto, vistas, ADR, atributos/ISO 25010 |
| 2 Arquitectura lógica | `05` | monolito, capas, microservicios, eventos, API e integración |
| 3 Arquitectura física | `06`, `07` | OSI, topología, VM/contenedores, RAID y dimensionamiento |
| 4 Nube | `06` | características, IaaS/PaaS/SaaS, regiones, serverless y comparación |
| 5 Atributos de calidad | `06`, `12` | escalabilidad, disponibilidad, rendimiento, SLI/SLO/SLA |
| 6 Continuidad | `06` | activo-pasivo/activo-activo, RTO/RPO, replicación y respaldos |
| 7 Seguridad | `06` | defensa en profundidad, red, datos y monitoreo |
| 8 Identidad y sesión | `06` | LDAP/AD, SAML, OAuth, OIDC, JWT y sesión |
| 9 Entrega | `06` | ambientes, CI/CD y despliegues |
| 10 Tendencias | `05`, `06`, `09` | plataforma, datos, IA, FinOps y sostenibilidad como decisiones justificadas |
| 11 Propuesta | `13` | trazabilidad requisito-arquitectura-costo y comparación de alternativas |

## FEP02.26 — Requisitos, Alcance, Planificación y EDT

| Sección | Apunte | Cobertura |
|---|---|---|
| 1 Proyecto | `02` | proyecto/operación, PMBOK, ciclo de vida, triple restricción e interesados |
| 2 Requisitos | `02` | tipos, FURPS+, elicitación, especificación y trazabilidad |
| 3 Alcance | `03` | seis procesos, alcance producto/proyecto, enunciado y cambios |
| 4 EDT | `03` | regla 100 %, descomposición, paquetes y diccionario |
| 5 Cronograma | `04` | seis procesos, red, PERT, CPM, recursos y compresión |
| 6 Estimación y costo | `08`, `09` | técnicas, incertidumbre, tarifas, insumos, reservas y margen |

## FEP03.26 — Estimación de Software

| Sección | Apunte | Cobertura |
|---|---|---|
| 1 Medir tamaño | `08` | tamaño, esfuerzo, plazo, costo y métodos |
| 2 Punto Función | `08` | EI/EO/EQ/ILF/EIF, UFP, factores y FP |
| 3 Punto Caso de Uso | `08` | actores, transacciones, UAW/UUCW/UUCP |
| 4 Factores | `08` | TCF, EF, pesos e interpretación |
| 5 Tamaño a esfuerzo | `08`, `09` | CF, distribución, plazo, tarifa y precio |
| 6 Ejemplo completo | `08`, `13` | cálculo paso a paso y uso en propuesta |
| 7 Glosario | `15` | siglas y distinciones |

## FEP04.26 — Gestión de los Riesgos

| Sección | Apunte | Cobertura |
|---|---|---|
| 1 Qué es riesgo | `10` | incertidumbre/riesgo/problema, amenaza/oportunidad y exposición |
| 2 Proceso | `10`, `16` | siete procesos, plan, RBS, registro e informe |
| 3 Identificar | `10` | técnicas, bases, supuestos y causa-evento-efecto |
| 4 Analizar | `10` | cualitativo, EMV, árbol, PERT/simulación y sensibilidad |
| 5 Responder | `10` | estrategias, costo, residual/secundario y contingencia |
| 6 Licitación | `10` | consultas, supuestos, exclusiones y decisión de ofertar |
| 7 Riesgo a solución | `10`, `13` | trazabilidad a alcance, arquitectura, EDT y precio |
| 8 Declarar y etapa | `10` | ficha, propuesta/implementación/implantación/operación y gobierno |
| 9 Propuesta | `10`, `13` | estructura, reserva y evaluación |

## FEP05.26 — Sala de Servidores

| Bloque | Apunte | Cobertura |
|---|---|---|
| 1 Datacenter | `07` | cuatro servicios, TIER, redundancia y PUE/DCiE |
| 2 Recintos | `07` | principios y trece recintos |
| 3 Distribución | `07` | escalas, esquemas, holguras y justificación |
| 4 Seguridad | `07` | líneas de acceso, mantrap, antipassback, CCTV, sensores y extinción |
| 5 Energía/clima | `07` | cadena, UPS, baterías, generador, calor y pasillos |
| 6 Rack/cableado | `07` | U, elevación, PDU, topología, etiquetado y certificación |
| 7 Equipamiento | `07` | formatos, VM/contenedores, clúster y almacenamiento |
| 8 Caso LATIOS | `07`, `13` | aplicación de criterios a ficha técnica/caso |
| 9 Propuesta | `07`, `13`, `15` | parámetros, glosario y números verificables |

## FEP06.26 — Contratos, Adquisiciones y Calidad

| Sección | Apunte | Cobertura |
|---|---|---|
| 1 Adquisiciones | `11` | familias, hacer/comprar/arrendar y formas de pago |
| 2 Contratos | `11` | modelos, distribución del riesgo, FPIF/PTA y cláusulas |
| 3 Proceso | `11` | procesos PMBOK, SOW, RFI/RFP/RFQ/IFB y evaluación |
| 4 Economía | `09`, `11` | TCO, CAPEX/OPEX, dependencia, salida y precio |
| 5 Calidad | `12` | calidad/grado, producto/proceso, ISO 25010 y requisitos |
| 6 Aseguramiento | `12` | tres procesos, plan, niveles y herramientas |
| 7 Costo de calidad | `12` | prevención, evaluación, fallas y costo óptimo |
| 8 Cruce contractual | `11`, `12` | aceptación, SLA, multas, recepción, garantía y pagos |
| 9 Propuesta | `13` | efecto en estimación, planificación, riesgo y estrategia |

## PMBOK y lecturas

| Fuente | Apunte |
|---|---|
| PMBOK capítulo 05 | `03`, `16` |
| PMBOK capítulo 06 | `04`, `16` |
| PMBOK capítulo 08 | `12`, `16` |
| PMBOK capítulo 11 | `10`, `16` |
| WBS Second Edition | `03` |
| Lecturas 1–3 de estimación | `08`, `09` |
| Pauta Control 1 | `14` y estilo de ejercicios en `03`, `04`, `08`, `10` |

## Control de cobertura

- FEP01: 11/11 secciones.
- FEP02: 6/6 secciones.
- FEP03: 7/7 secciones.
- FEP04: 9/9 secciones.
- FEP05: 9/9 bloques.
- FEP06: 9/9 secciones.
- PMBOK: 22/22 procesos en `16`.

