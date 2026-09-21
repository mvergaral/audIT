# Entregable 4: Conclusiones y Recomendaciones Estratégicas

## Restricción de autoría

Las conclusiones y recomendaciones deben ser de autoría humana. Este entregable es una matriz de síntesis para que Persona 1 construya el cierre después de recibir resultados definitivos.

## Matriz de síntesis previa

| Dimensión | Hallazgo validado | Interpretación humana |
| :--- | :--- | :--- |
| Ley 21.719 | Exige base de licitud, acuerdos de encargo, RAT y contempla sanciones de hasta 20.000 UTM o 4% de ventas. | El rastreo de choferes no puede tratarse como solo un tema técnico: necesita respaldo legal y contractual. |
| Ley 21.663 | Obliga a reportar incidentes al CSIRT Nacional en $\le 3\text{ h}$ bajo D.S. 295/2024. | La operación debe tener alertas y responsables definidos; no basta con reaccionar manualmente después del incidente. |
| Marco internacional | El cruce a Mendoza activa la Ley argentina 25.326 y la réplica East US 2 exige cláusulas contractuales preventivas. | La solución debe funcionar legalmente en Chile y también cuando los datos cruzan frontera o se respaldan fuera del país. |
| Herramientas GRC | CISO Assistant Pro y Purview permiten gestionar RAT, evidencias y seguimiento de cumplimiento. | La herramienta elegida debe ser defendible por costo y utilidad, no solo por reputación de mercado. |
| Impacto económico | El cumplimiento cuesta 8.375,4 UF netas, equivalente al 3,9% del contrato, con RoSI mayor a +250%. | El costo es alto, pero es proporcional frente al tamaño de la licitación y al riesgo de multas. |
| Arquitectura | La solución usa Azure Chile Central, réplica East US 2, cifrado RT-11.10, 686 claves HSM y conectividad por capas. | La arquitectura resuelve el problema operacional sin pagar satélite masivo en toda la flota. |

## Estructura de conclusión

1. Responder al objetivo del trabajo, no repetir la introducción.
2. Explicar la relación entre privacidad, ciberseguridad y gobierno del proyecto.
3. Identificar la brecha más importante encontrada en el Caso 10.
4. Explicar el efecto en arquitectura, cronograma y presupuesto.
5. Cerrar con una recomendación priorizada y defendible.

## Prueba de derivación

Cada oración del cierre debe clasificarse como:

- **Resultado:** proviene de evidencia desarrollada en el cuerpo.
- **Interpretación:** lectura humana explícita de esos resultados.
- **Recomendación:** decisión propuesta por el grupo con fundamento.

Si una oración no puede clasificarse o no tiene antecedente, debe eliminarse.

## Conclusiones - redacción manual

1. **El cumplimiento es necesario para operar:** La investigación dejó en claro que cumplir con las leyes no es solo un trámite legal o papeleo, sino algo indispensable para que el proyecto funcione en la práctica. Si no se cuenta con bases legales claras o no se avisa a tiempo de incidentes, Curimón se arriesga a multas muy graves que pueden llegar a 20.000 UTM por datos personales o 40.000 UTM por ciberseguridad.
2. **Solución a la desorganización de datos:** El problema de fondo en Curimón era que la información de los camiones y choferes estaba repartida en planillas Excel sin ningún orden ni seguridad. La propuesta de conectar la flota por capas y unificarla en una sola vista resuelve este desorden de raíz, asegurando que los datos viajen protegidos y que no se pierda información en las zonas sin señal.
3. **Inversión justificada:** Gastar **8.375,4 UF netas** ($\text{VAN}_{\text{costo}} = \mathbf{6.582,3\text{ UF}}$) representa apenas el 3,9% de lo que cuesta toda la licitación. Con solo un 2,80% de probabilidad al año de recibir una fiscalización con sanción, el plan de seguridad ya se paga completamente solo, logrando un retorno sobre la inversión (RoSI) superior al $+250\%$.

## Recomendaciones - redacción manual

1. **Fase 1 · Ordenar contratos y permisos (Meses 1 a 4):** Lo primero es firmar los contratos de encargo con los 148 transportistas externos y pedir el consentimiento en la app a los 258 choferes subcontratados. Además, se debe armar el registro de datos (RAT) antes de activar el rastreo masivo por GPS.
2. **Fase 2 · Montar la plataforma y el enlace de seguridad (Meses 5 a 12):** Desplegar los sistemas en Azure Chile Central, configurar las 686 claves en Key Vault para cifrar los datos de cada transportista y dejar listo el canal de alertas para avisarle al CSIRT Nacional en menos de 3 horas si ocurre un ataque.
3. **Fase 3 · Certificación formal y respaldo final (Meses 13 a 20):** Hacer la auditoría externa para certificar la norma ISO/IEC 27001:2022 con una empresa acreditada y contratar el seguro de ciberriesgo con Chubb, dejando el proyecto completamente respaldado frente a los 84 clientes corporativos.
