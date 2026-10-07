# Formulario T-13

**Contenido exigido:** Niveles y tipos de prueba conforme a ISO/IEC/IEEE 29119. — Apartado 1, folio 5

**Contenido exigido:** Ambientes y datos de prueba. — Apartado 2, folio 5

**Contenido exigido:** Criterios de entrada y de salida. — Apartado 3, folio 5

**Contenido exigido:** Automatización de pruebas. — Apartado 4, folio 6

**Contenido exigido:** Calendario de las pruebas de carga, resiliencia, recuperación ante desastres y seguridad ofensiva. — Apartado 5, folio 6

### Niveles y tipos de prueba conforme a ISO/IEC/IEEE 29119.

Se aplica planificación, seguimiento, diseño, preparación, ejecución y cierre de los procesos de prueba (ISO/IEC/IEEE, 2021). La estructura de nueve campos del catálogo es una convención de audIT. Se diseñan 25 casos unitarios, 25 de integración, 20 de sistema, 12 de rendimiento y 8 de seguridad, 15 de hardware/HIL y 15 UAT: 120 identificadores únicos. Unitarias contrastan reglas/oráculos; integración valida esquemas e idempotencia; sistema verifica flujos completos; no funcionales miden carga, seguridad y recuperación; HIL utiliza dispositivos homologados; UAT comprueba tareas con contraparte. Véase sección 9.2.

### Ambientes y datos de prueba.

CI utiliza dobles y fixtures sintéticos; QA integra contratos; staging reproduce configuración/carga; HIL conserva modelo, firmware, señales y permisos; UAT usa terminales y usuarios designados con autorización. Producción se utiliza solo en ejercicio autorizado, con respaldo y reversión. Se versionan entradas, semilla/reloj, oráculo y manifiesto. No se atribuyen marcas o API ensayadas al parque existente sin homologación. Datos operacionales requieren acceso autorizado y minimización. Véase sección 9.2.1.

### Criterios de entrada y de salida.

Entrada: versión/configuración y ambiente identificados, requisito/caso/criterio fijados, datos y permisos disponibles, observabilidad y reversión verificadas. Salida: todos los criterios aplicables cumplidos, reporte reproducible y defectos relacionados, sin críticos/altos para cierre de marcha blanca. Se aplican los mínimos de sección 9.3.6; cuatro semanas sostenidas y las seis condiciones acumulativas de sección 9.3.5 gobiernan aceptación. Un promedio o cobertura de código no reemplaza otro criterio.

### Automatización de pruebas.

Cada cambio ejecuta compilación, pruebas unitarias y regresión; contratos e integración se ejecutan contra dobles versionados y en QA. Cobertura de lógica de negocio mínima de 70 % es bloqueante; 80 % es objetivo adicional. Análisis estático/dependencias y pruebas de autorización acompañan cada promoción; el resultado se conserva por versión. Carga, cortes de enlace y recuperación requieren script, manifiesto y cronómetro; HIL/UAT conservan las verificaciones manuales que no puede suplir un pipeline. Un fallo bloquea promoción y dispara corrección/reevaluación; una excepción no rebaja mínimos contractuales. Véase sección 9.2.3.

### Calendario de las pruebas de carga, resiliencia, recuperación ante desastres y seguridad ofensiva.

Construcción E1: A09/A10/A11; certificación E1 A12, M12/H5, con informes separados de las cuatro familias y UAT. Marcha blanca A15, M13--M15; producción A19, M16/H7. Construcción E2 A20 y certificación A22, M18/H10, incluyendo regresión E1 y las cuatro familias. Marcha blanca A24, M19--M20; aceptación final A25, M21/H12. DR y seguridad ofensiva requieren autorización previa y reversión; las ventanas contractuales no se desplazan por ensayos. Resiliencia y DR se repiten semestralmente en operación; intrusión anual y antes de producción por tercero independiente, con informe íntegro y remediación. Se realizan dos ensayos de migración antes de la definitiva (FEP02, 20.1, pp. 34--35; RT-11.20, p. 24). Véase sección 9.3.2.
