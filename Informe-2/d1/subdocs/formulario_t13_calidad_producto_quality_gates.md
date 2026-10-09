# Formulario T-13

**Niveles y tipos de prueba conforme a ISO/IEC/IEEE 29119..**  \hyperref[sec:9-t13-1]{Apartado 1}, folio \pageref{sec:9-t13-1}

**Ambientes y datos de prueba..**  \hyperref[sec:9-t13-2]{Apartado 2}, folio \pageref{sec:9-t13-2}

**Criterios de entrada y de salida..**  \hyperref[sec:9-t13-3]{Apartado 3}, folio \pageref{sec:9-t13-3}

**Automatización de pruebas..**  \hyperref[sec:9-t13-4]{Apartado 4}, folio \pageref{sec:9-t13-4}

**Calendario de las pruebas de carga, resiliencia, recuperación ante desastres y seguridad ofensiva..**  \hyperref[sec:9-t13-5]{Apartado 5}, folio \pageref{sec:9-t13-5}

### 9.0.1 Niveles y tipos de prueba conforme a ISO/IEC/IEEE 29119.

Se aplica planificación, seguimiento, diseño, preparación, ejecución y cierre de los procesos de prueba (ISO/IEC/IEEE, 2021). La estructura de nueve campos del catálogo es una convención de audIT. Se diseñan 25 casos unitarios, 25 de integración, 20 de sistema, 12 de rendimiento y 8 de seguridad, 15 de hardware/HIL y 15 UAT: 120 identificadores únicos. Unitarias contrastan reglas/oráculos; integración valida esquemas e idempotencia; sistema verifica flujos completos; no funcionales miden carga, seguridad y recuperación; HIL utiliza dispositivos homologados; UAT comprueba tareas con contraparte. Véase sección 9.2.

### 9.0.2 Ambientes y datos de prueba.

CI utiliza dobles y fixtures sintéticos; QA integra contratos; staging reproduce configuración/carga; HIL conserva modelo, firmware, señales y permisos; UAT usa terminales y usuarios designados con autorización. Producción se utiliza solo en ejercicio autorizado, con respaldo y reversión. Se versionan entradas, semilla/reloj, oráculo y manifiesto. No se atribuyen marcas o API ensayadas al parque existente sin homologación. Datos operacionales requieren acceso autorizado y minimización. Véase sección 9.2.1.

La homologación física utiliza iWave G26I con audIT EdgeHub, lector CAN sin contacto Technoton CANCrocodile y las balizas Bluetooth de la innovación 3. Se distinguen los 182 equipos previstos de los 192 terceros con dispositivos existentes: sus plataformas requieren acceso autorizado y no se presume API ni exportación disponible. El catálogo T-17 verifica lectura, integridad, datos ausentes, antigüedad y conciliación, sin atribuir al parque real el resultado de dobles sintéticos. Para frío, rango y precisión provienen del modelo y la homologación; no se trasladan especificaciones de sondas PT100.

### 9.0.3 Criterios de entrada y de salida.

Entrada: versión/configuración y ambiente identificados, requisito/caso/criterio fijados, datos y permisos disponibles, observabilidad y reversión verificadas. Salida: todos los criterios aplicables cumplidos, reporte reproducible y defectos relacionados, sin críticos/altos para cierre de marcha blanca. Se aplican los mínimos de sección 9.3.6; cuatro semanas sostenidas y las seis condiciones acumulativas de sección 9.3.5 gobiernan aceptación. Un promedio o cobertura de código no reemplaza otro criterio.

Los controles siguientes complementan los criterios contractuales de S9 §9.3.6. La Tabla 13.1 relaciona umbral, método y evidencia; los controles físicos son compromisos de homologación de la configuración ofertada, no certificaciones ya obtenidas. audIT provee o contrata el banco y los instrumentos, sin presumir infraestructura del mandante.

*Tabla 13.1. Controles bloqueantes de software y homologación física*

| Control | Umbral y alcance | Método y caso | Evidencia de salida |
|---|---|---|---|
| Cobertura | Líneas de negocio ≥70 % contractual; ramas ≥80 % adicional | GitLab Runner y reporte compatible con SonarQube; catálogo unitario CP-UNIT-01–25 | Versión, numeradores, denominadores, exclusiones y cero pruebas fallidas |
| Complejidad | ≤15 por función de negocio, compromiso audIT | SonarQube y revisión de descomposición; S9 §9.1.1 | Reporte estático y cierre de funciones fuera de límite |
| Vulnerabilidades | Cero críticas o altas abiertas en el artefacto promovido | SonarQube, Trivy y OWASP ZAP; CP-SEC-01–08 según alcance | Informes ligados a huella, reevaluación y SBOM |
| Lectura CAN pasiva | Pérdida <0,1 %; cero tramas transmitidas por audIT | CANoe y analizador independiente; CP-HW-04 | Contadores, captura, autorización y mapa de señales |
| Energía en reposo | <50 mA tras 30 min, compromiso audIT | Instrumento de corriente sobre conjunto alimentado; CP-HW-05 | Serie de corriente, tensión, duración y configuración de periféricos |
| Ambiente térmico y vibración | Operación entre −20 °C y +70 °C; perfil SAE J1455 aprobado para montaje | Cámara y mesa de vibración; CP-HW-07 | Protocolo identificado, certificado de calibración e informe funcional |
| Protección exterior | IP67 del conjunto expuesto: gabinete, conectores y cableado exterior | Laboratorio y procedimiento IEC 60529; CP-HW-08 | Configuración de montaje, informe de polvo/agua y verificación funcional |
| Actualización de firmware | Solo detenido en terminal autorizado; recuperación A/B sin pérdida | Control de ubicación/estado y fallos de imagen/energía; CP-SYS-20 y CP-HW-09 | Rechazos fuera de ventana, huellas, arranque, reversión y conciliación |

Cada informe conserva la versión del procedimiento, modelo, montaje y calibración aplicables. Una ficha de fabricante o un resultado sobre otro montaje no sustituye la homologación del conjunto. Un fallo impide liberar ese equipo o incremento hasta su corrección y reevaluación. El perfil térmico y vibratorio se documenta antes del ensayo; los números de un fixture no se atribuyen a una cláusula normativa sin respaldo.

### 9.0.4 Automatización de pruebas.

Cada cambio ejecuta compilación, pruebas unitarias y regresión; contratos e integración se ejecutan contra dobles versionados y en QA. La cobertura automatizada de líneas ejecutables de lógica de negocio ≥70 % es el mínimo contractual bloqueante (RT-04.11); la cobertura de ramas ≥80 % es un compromiso adicional bloqueante de audIT, coherente con S6 Tabla 6.3. Se calculan líneas cubiertas/líneas ejecutables y ramas cubiertas/ramas instrumentadas por separado, con módulos y exclusiones justificadas; no se incluyen dependencias o código generado para elevar el resultado. Análisis estático/dependencias y pruebas de autorización acompañan cada promoción; el resultado se conserva por versión. Carga, cortes de enlace y recuperación requieren script, manifiesto y cronómetro; HIL/UAT conservan las verificaciones manuales que no puede suplir un pipeline. Un fallo bloquea promoción y dispara corrección/reevaluación; una excepción no rebaja mínimos contractuales ni los gates adicionales bloqueantes comprometidos. Véase sección 9.2.3.

### 9.0.5 Calendario de las pruebas de carga, resiliencia, recuperación ante desastres y seguridad ofensiva.

El perfil de carga común es 380 sesiones nominales (80 internas, 150 conductores, 50 transportistas y 100 clientes) y 570 en estrés (120, 225, 75 y 150 respectivamente). Son hipótesis conservadoras de S4, no mediciones del Caso; CP-PERF-01 preserva esa mezcla y comprueba los umbrales contractuales a 1,5 veces el peak. Un cambio de perfil exige actualizar S9 y T-17 antes de ensayar.

Construcción E1: A09/A10/A11; certificación E1 A12, M12/H5, con informes separados de las cuatro familias y UAT. Marcha blanca A15, M13--M15; producción A19, M16/H7. Construcción E2 A20 y certificación A22, M18/H10, incluyendo regresión E1 y las cuatro familias. Marcha blanca A24, M19--M20; aceptación final A25, M21/H12. DR y seguridad ofensiva requieren autorización previa y reversión; las ventanas contractuales no se desplazan por ensayos. Resiliencia y DR se repiten semestralmente en operación; intrusión anual y antes de producción por tercero independiente, con informe íntegro y remediación. Se realizan dos ensayos de migración antes de la definitiva (FEP02, 20.1, pp. 34--35; RT-11.20, p. 24). Véase sección 9.3.2.
