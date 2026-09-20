# Apertura y Cierre: Cumplimiento Normativo Aplicado al Proyecto TIC de Transportes Curimón S.A.
## Trabajo TI-12 · Empresa Consultora AudIT · Caso 10

**Autor responsable:** Persona 1 (*Lead Editor & System Integrator*)
**Extensión objetivo:** 1,5 a 2 páginas útiles
**Estado:** borrador editorial sujeto a reescritura humana en las secciones restringidas por el punto 6.1

---

## Resumen ejecutivo

El proyecto informático para Transportes Curimón S.A. debe cumplir exigencias de protección de datos personales, ciberseguridad, gestión de proveedores y continuidad operacional que afectan directamente su arquitectura y presupuesto. La operación considera 374 camiones, 454 conductores, 148 empresas transportistas y 84 clientes corporativos. La plataforma trata geolocalización, telemetría, jornadas, datos contractuales y antecedentes comerciales, por lo que las obligaciones de las leyes N.º 21.719 y N.º 21.663 no pueden abordarse como un anexo jurídico independiente del diseño del sistema.

El análisis de AudIT traduce las obligaciones normativas en actividades, roles, plazos y partidas de costo. La aplicación al Caso 10 exige distinguir a Transportes Curimón como responsable del tratamiento y a AudIT y sus proveedores tecnológicos como encargados; mantener un registro de actividades de tratamiento; evaluar el impacto del monitoreo continuo; establecer controles de privacidad y seguridad desde el diseño; regular transferencias internacionales; y disponer de capacidades formales de respuesta a incidentes. Estas medidas deben reflejarse en la EDT, la carta Gantt, los criterios de aceptación y el flujo de caja.

El marco internacional y las normas técnicas complementan el cumplimiento chileno. El RGPD, NIS2, el Reglamento Europeo de IA y el Reglamento de Ciberresiliencia sirven como referencia cuando existe software exportado, proveedores globales o transferencias internacionales. ISO/IEC 27001:2022, ISO/IEC 27701, ISO/IEC 42001:2023 y NIST CSF 2.0 permiten convertir principios generales en controles auditables y sostener un modelo de mejora continua.

La principal decisión de gobierno consiste en adoptar una matriz integrada que conecte cada obligación con su aplicación fáctica, control, responsable, plazo, evidencia y costo. Así, el cumplimiento deja de ser una declaración formal y se convierte en una capacidad operacional financiada y verificable.

---

## Introducción

Los proyectos TIC que procesan datos personales y sostienen operaciones críticas deben incorporar el cumplimiento desde su formulación. Una solución técnicamente funcional puede resultar inviable si carece de base de licitud, no delimita responsabilidades con proveedores, no contempla incidentes de ciberseguridad o subestima el costo de auditorías y roles especializados.

El tema TI-12 exige determinar qué obligaciones legales concretas recaen sobre un proyecto desarrollado o explotado en Chile. La Ley N.º 21.719 actualiza el régimen de protección de datos personales y obliga a revisar bases de licitud, datos sensibles, derechos de los titulares, portabilidad, seguridad, responsabilidad y sanciones. La Ley N.º 21.663 estructura el marco nacional de ciberseguridad mediante la ANCI y el CSIRT Nacional, distinguiendo servicios esenciales y operadores de importancia vital y estableciendo deberes de seguridad y reporte.

La aplicación se realiza sobre el Caso 10, Transportes Curimón S.A. El sistema licitado centraliza información operacional de una flota distribuida y relaciona datos de conductores propios y externos con rutas, jornadas y telemetría. También integra a transportistas subcontratados, clientes y proveedores cloud. Esta realidad permite evaluar obligaciones que no serían visibles en un análisis normativo abstracto: monitoreo de trabajadores y terceros, contratos de encargo, cifrado de información, transferencias internacionales, continuidad y respuesta a incidentes.

El objetivo del informe es vincular el marco legal y técnico con decisiones concretas del proyecto. Para ello se estudian las normas nacionales e internacionales, se comparan organismos, estándares y herramientas de apoyo, y se construye una matriz que asigna actividades, responsables, plazos y partidas de costo. El resultado debe ser consistente con la arquitectura de cumplimiento y el modelo económico del proyecto.

### Delimitación del aporte propio

> **Sección de autoría humana obligatoria.** La ficha entrega la Ley 21.719, la Ley 21.663, el marco internacional, normas certificables y herramientas de apoyo como piso mínimo. Persona 1 debe reescribir este párrafo después de confirmar cuáles alternativas adicionales investigó el equipo, qué evidencia contradictoria encontró y qué recomendación final está dispuesto a defender. El aporte esperado es la aplicación verificable al Caso 10 mediante la cadena norma → obligación → actividad → rol → plazo → costo, más las ampliaciones reales incorporadas por P2 y P3.

---

## Síntesis de integración con el Caso 10

La coherencia global del informe se sostiene sobre cuatro decisiones. Primero, el marco chileno define las obligaciones y su vigencia. Segundo, el marco internacional y las normas técnicas aportan criterios de comparación y madurez. Tercero, la arquitectura incorpora controles concretos de privacidad, seguridad, transferencias y respuesta a incidentes. Cuarto, el modelo económico financia cada control y evita componentes técnicos sin partida presupuestaria.

La matriz de obligaciones constituye el artefacto integrador. Una fila válida no termina en la norma: debe identificar el hecho del Caso 10 que activa la obligación, la acción requerida, el rol responsable, el plazo normativo u operativo, la evidencia de cumplimiento y el costo asociado. Esta estructura permite comprobar si la propuesta técnico-económica internaliza los costos de cumplimiento o los deja como riesgos no financiados.

---

## Conclusiones y recomendaciones estratégicas

> **Sección de autoría humana obligatoria.** El siguiente contenido es una pauta de contraste. Persona 1 debe redactar la versión final únicamente después de recibir los hallazgos verificados de P2-P5.

Los antecedentes del Caso 10 muestran que privacidad y ciberseguridad son dimensiones inseparables del proyecto. La geolocalización y telemetría asociadas a conductores requieren bases de licitud, minimización, seguridad, retención controlada y atención de derechos. Al mismo tiempo, la continuidad de la torre de control y la exposición a incidentes justifican controles de seguridad, responsabilidades formales y protocolos de reporte.

La propuesta debe evitar dos extremos: limitarse a declaraciones generales de cumplimiento o sobredimensionar controles sin relación con el riesgo y el presupuesto. La alternativa defendible es un programa proporcional, trazable y financiado, respaldado por una matriz de obligaciones y por el calce uno a uno entre arquitectura y costos.

Recomendaciones que deben confirmarse con evidencia final:

1. Incorporar la matriz de obligaciones como instrumento de gobierno del proyecto y actualizarla ante cambios regulatorios o técnicos.
2. Ejecutar privacidad y seguridad desde el diseño, incluyendo registro de tratamientos, evaluación de impacto, contratos con encargados y gestión de incidentes.
3. Mantener correspondencia uno a uno entre controles arquitectónicos, roles, hitos de la EDT y partidas presupuestarias.
4. Priorizar fuentes oficiales y verificar la vigencia de cada norma a la fecha de entrega.
5. Adoptar estándares internacionales como mecanismos de implementación y evidencia, sin presentarlos erróneamente como leyes chilenas obligatorias.

Antes de incorporar este cierre, Persona 1 debe verificar que ninguna recomendación introduzca herramientas, cifras o decisiones ausentes del cuerpo del informe.
