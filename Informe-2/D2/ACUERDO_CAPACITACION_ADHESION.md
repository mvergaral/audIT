# Acuerdo de capacitación y adhesión — 11 de octubre de 2026

## Capacitación

A13 mantiene 40 días hábiles y comienza diez días antes del término de A09,
con A06 como predecesora y disponibilidad obligatoria de G13. G13 corresponde
a la entrega probada y congelada de la versión de entrenamiento en PREPROD,
datos ficticios y material por perfil, incluida en A09 al cierre del sprint 7.
D3 debe identificar las funciones certificadas que habilitan los diez días
iniciales de familiarización. La certificación no se presume ejecutada.

Los treinta días restantes cubren los flujos completos, evaluaciones y el
complemento de cambios del sprint 8 antes de marcha blanca, dentro de la
duración total. Turnos y relevos protegen la operación. Si falta G13, se
registra el atraso, se retrasa A13 y se actualiza el riesgo.

CPM recalculado: A13 ES 182, EF 222, LS 220, LF 260, HT 38 y HL 18.
A06 conserva HT 62 y pasa a HL 24. El proyecto termina en el día 420.
Son 25 actividades y un hito de liberación de duración cero, no un paquete EDT nuevo.
La escala de 20 días hábiles por mes es la convención de T-15; no convierte esos
días en fechas laborales exactas ni reemplaza el calendario contractual.

## Adhesión

Denominador fijo: 148 transportistas de la población inicial del Caso. Una
vez por RUT, con anexo firmado por mandante y representante autorizado,
vigente, no revocado y registrado al corte. Contar las modalidades completa
y de datos. Corte de M9: 31 de octubre de 2027 bajo SA-01 (M1 febrero de 2027).
El 40 % es 59,2: se requieren al menos 60; con 59 o menos se activa el refuerzo.
Mantener metas de 104 en M16 y 134 en M21. Instalación, activación técnica y
consentimientos de conductores se controlan por separado; la firma del
transportista no sustituye esos consentimientos.

## Simulación y fuente de riesgos pendiente

El equipo reportó 82,3 % de inicio oportuno de ambas marchas blancas y 14,1 %
de atraso de la primera por A13 sin adelanto; con el adelanto, 92,1 % y 0,1 %,
respectivamente. **Son resultados reportados, no verificados en este checkout.**
No se incorporan como probabilidades acreditadas de S8 ni como resultado de
un nuevo Monte Carlo ejecutado aquí.

Faltan el código y catálogo integrado de D4, distribuciones, correlaciones,
número de corridas, semilla, definición de inicio oportuno y tratamiento de
indisponibilidad de G13. La entrada determinista está reproducida en
`03_Apoyo/CPM_acuerdo_capacitacion.json`. D4 debe recalcular con esta misma
planificación y conservar evidencia antes de reemplazar cifras en S8.

En este checkout S8 era una plantilla y no había T-16 propio de S8. Se
incorporaron las condiciones comunes y un T-16 parcial con códigos AC-CAP
y AC-ADH, con cuantificación pendiente. No sustituyen ni renumeran los
riesgos del catálogo original ausente. El riesgo R-28 y la validación del
documento completo en 90 segundos siguen pendientes de esa integración.

El uso de IA se declara en los subdocumentos afectados. La revisión humana
y asociación a la bitácora A-6 del responsable siguen pendientes.
