# Formulario T-18. Cronograma maestro Gantt y red PERT/CPM

**Estado:** borrador de hitos y dependencias; fechas y holguras pendientes de validar.  
**Vínculo:** Subdocumento 7, sección 7.3.

## Red lógica preliminar

| ID | Actividad / hito | Predecesoras | Entregable / salida | Calendario y duración |
|:---|:---|:---|:---|:---|
| M0 | Inicio y línea base | Contrato / acta de inicio | Planes, EDT y gobernanza aprobados | Por confirmar en Bases |
| A | Requisitos, diseño e interfaces | M0 | Baseline T-12 y diseños aprobados | Estimar con T-14 |
| B | Ambientes y plataforma base | M0 | Ambientes, accesos, seguridad y observabilidad | Estimar con D3/D4 |
| C | Construcción Etapa 1 | A, B | Capacidades funcionales integradas | Estimar por paquetes |
| D | Equipamiento y habilitación de flota | A, logística de equipos | Unidades preparadas/instaladas y trazadas | Estimar con D4 y terminales |
| E | Migración y reconciliación | A, acceso a datos, componentes habilitados | Datos aceptados y excepciones documentadas | Estimar con dueño de datos |
| F | Pruebas de integración y sistema | C, D, E, tooling QA | Informes de pruebas y defectos tratados | H4 / D1-D3-D4 |
| G | UAT en cinco terminales | F, disponibilidad de usuarios | Actas UAT por terminal | H4 / contraparte |
| H | Aceptación y producción Etapa 1 | G, criterios contractuales | Acta de aceptación y liberación | Mes contractual por conciliar |
| I | Marcha blanca de 60 días | H, soporte preparado | Registros de operación y salida | Fechas por confirmar |
| J | Construcción e integración Etapa 2 | A, decisiones aprobadas | Innovaciones/capacidades integradas | Duración por estimar |
| K | Pruebas y aceptación Etapa 2 | J, tooling QA | Evidencia y acta de aceptación | Hitos por confirmar |
| L | Producción Etapa 2 | K | Liberación y estabilización | Mes contractual por conciliar |
| Z | Transferencia y cierre | H, I, L, obligaciones operativas | Actas y documentación final | Plazo total por verificar |

## Cálculo PERT/CPM pendiente

Las relaciones lógicas son preliminares. Duraciones, fechas tempranas/tardías, holgura total/libre y ruta crítica se calculan cuando se conozcan el plazo contractual, calendario laboral, restricciones de precedencia, disponibilidad del mandante y asignación de recursos T-15. No se declara ruta crítica en este borrador.

## H4 hacia D1

Para cerrar H4 se debe acordar calendario con D1, D3, D4 y Curimón para: pruebas de integración, carga, seguridad, resiliencia y recuperación; UAT en San Bernardo, Valparaíso, Concepción, Antofagasta y Puerto Montt; marcha blanca de 60 días; y criterios de entrada/salida. Este formulario aún no comunica un calendario aprobado ni reemplaza el acuse de entrega del handshake.
