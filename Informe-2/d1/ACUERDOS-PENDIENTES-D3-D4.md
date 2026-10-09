# Acuerdos pendientes entre D3 y D4

Registro interno de coordinación — 09-10-2026. No forma parte de la oferta.

Antes de cerrar la integración, D3 y D4 deben conciliar estos puntos y dejar una única versión vigente:

| Tema | Diferencia o problema | Acuerdo requerido |
|---|---|---|
| Carga concurrente | S4 de D4 utiliza 350 usuarios; S4 compartido y pruebas D1 utilizan 380. Las cargas de estrés resultantes son 525 y 570 | Justificar la concurrencia con poblaciones y supuestos, acordar un perfil y comunicarlo a D1 |
| Equipo a bordo | S6 de D3 menciona 148 computadores y 34 CANclick; el diseño físico contempla 182 iWave G26I y lectores CANCrocodile | Unificar cantidades, componentes, responsable de adquisición y calendario con S7 de D2 |
| Datos de terceros | S4 compartido presume REST/Webhook para 192 camiones; el Caso limita permisos y exportación de las plataformas | Definir mecanismos autorizados por proveedor, restricciones y contingencias sin prometer interfaces no acreditadas |
| Calendario y disponibilidad | S6 mantiene marchas blancas de 60 días en ambas etapas y presenta 99,5 % como SLA contractual general | Reflejar E1 M13–M15, E2 M19–M20 y disponibilidad de 99,9 % para servicios críticos; conciliar con D2 |
| Evidencia de arquitectura y seguridad | S4 atribuye cálculos a ASHRAE/TIA; innovación 3 de S13 afirma evaluación STRIDE en S4 sin contenido identificado | Incorporar el análisis y sustento correspondientes o corregir las afirmaciones y referencias |

D3 debe además precisar su definición de terminado: el pipeline pide cobertura de ramas ≥80 %, pero la definición dice «cobertura ≥80 %» sin indicar qué mide. D1 distingue líneas de lógica de negocio ≥70 % y ramas ≥80 %.

Una vez acordados los parámetros, D1 comprobará si S9/T-13/T-17 requieren ajustes y actualizará las respuestas Art. 46 con la evidencia recibida. Las seis correcciones de EdgeHub ya están incorporadas en S1; su definición está en §1.1.3.
