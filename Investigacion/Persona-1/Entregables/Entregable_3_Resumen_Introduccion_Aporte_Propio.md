# Entregable 3: Resumen, Introducción y Aporte Propio

## Restricción de autoría

El punto 6.1 de las indicaciones exige autoría humana para el párrafo de aporte propio y la discusión crítica. Este documento organiza los insumos, pero Persona 1 debe redactar la versión entregable con su propio razonamiento y conservar historial de cambios.

## Ficha de insumos para el resumen ejecutivo

Insumos validados para la versión final:

| Elemento | Respuesta validada |
| :--- | :--- |
| Problema concreto del Caso 10 | Descontrol de flota de 374 camiones, datos dispersos en planillas y falta de trazabilidad en zonas sin cobertura. |
| Principal obligación bajo Ley 21.719 | Licitud de tratamiento de datos de conductores, acuerdos de encargo (Art. 15 bis) y Registro de Actividades de Tratamiento (RAT). |
| Principal obligación bajo Ley 21.663 | Reporte obligatorio de incidentes de ciberseguridad al CSIRT Nacional en $\le 3\text{ h}$ bajo D.S. 295/2024. |
| Hallazgo internacional más relevante | Aplicabilidad de la Ley argentina 25.326 por tránsito a Mendoza y uso preventivo de Cláusulas Contractuales Tipo para réplica en East US 2. |
| Control técnico determinante | Cifrado de campo (RT-11.10) con 686 llaves en Azure Key Vault Managed HSM y almacenamiento local cifrado. |
| Impacto económico principal | TCO de cumplimiento de 8.375,4 UF netas, equivalente al 3,9% del contrato, con RoSI mayor a +250%. |
| Recomendación del grupo | Despliegue por fases: contratos/consentimientos, plataforma Azure con cifrado y CSIRT, y certificación ISO 27001 con seguro de ciberriesgo. |

## Estructura recomendada del resumen

1. Contexto y problema en dos oraciones.
2. Alcance normativo estudiado.
3. Aplicación a Curimón.
4. Hallazgo principal.
5. Recomendación comprometida.

## Estructura recomendada de la introducción

1. Relevancia del cumplimiento en proyectos TIC.
2. Objetivo exigido por la ficha TI-12.
3. Descripción breve del Caso 10 y por qué activa obligaciones.
4. Método de investigación: fuentes oficiales, comparación, matriz y costeo.
5. Párrafo final de aporte propio.

## Pauta humana para el aporte propio

El párrafo final debe responder sin vaguedades:

- ¿Qué contenidos provienen literalmente de la ficha?
- ¿Qué dos o más alternativas añadió el grupo en cada lista que decía “otros”?
- ¿Qué subtema propio se incorporó?
- ¿Qué aplicación concreta se hizo al Caso 10?
- ¿Qué comparación, medición o prueba realizó el equipo?
- ¿Qué recomendación está dispuesto a defender?

### Redacción manual

**Resumen Ejecutivo:**  
Transportes Curimón administra una flota de 374 camiones, 454 conductores (196 propios y 258 externos), 148 transportistas subcontratados y 84 clientes corporativos bajo un contrato licitado a 56 meses con operaciones entre la frontera de Chile y Argentina, es decir, hacia Mendoza. Históricamente, la operación sufría de falta de visibilidad y control sobre sus unidades, con datos de telemetría y jornadas dispersos en planillas informales, lo que impedía costear tramos reales y configuraba un riesgo real ante el nuevo marco regulatorio chileno. El presente trabajo estructura el programa integral de cumplimiento normativo (TI-12) para el proyecto, articulando la Ley N.º 21.719 sobre Protección de Datos Personales (sanciones de hasta 20.000 UTM o 4% de ventas), la Ley N.º 21.663 de Ciberseguridad (notificación obligatoria al CSIRT Nacional en $\le 3\text{ h}$ bajo D.S. 295/2024) y la Ley N.º 25.326 argentina para el tránsito internacional. Se descartó el uso de banda ancha satelital en toda la flota porque era una opción elevada en el precio, adoptándose una arquitectura de conectividad por capas: telemetría por celular como principal, almacenamiento local cifrado y satélite transaccional de respaldo, convergiendo en una vista operacional unificada. La solución se despliega en Azure Chile Central con réplica en East US 2 (bajo Cláusulas Contractuales Tipo), cifrado de campo (RT-11.10) con 686 claves individuales en Azure Key Vault Managed HSM y gobierno GRC. El presupuesto de cumplimiento asciende a 8.375,4 UF netas, representando el 3,9% del contrato de licitación y asegurando un RoSI mayor a +250%.

**Párrafo de Delimitación del Aporte Propio:**  
En cumplimiento del Punto 4 de las Indicaciones, AudIT delimita su aporte propio frente a la Ficha TI-12: mientras la ficha suministró el marco conceptual general de las Leyes 21.719 y 21.663, los estándares ISO 27001/27701/42001 y las herramientas base de mercado, el grupo aportó:
1. La incorporación obligatoria de la Ley argentina 25.326 por el paso fronterizo a Mendoza y del marco de atestación SOC 2 Type II para los 84 clientes.
2. La integración del Dictamen DT N.º 569/2018 para regular el monitoreo mediante GPS.
3. La evaluación de Eramba y Osano como herramientas GRC de aporte propio para ponderar el esquema On-Premise vs. SaaS.
4. La formulación de una solución de conectividad por capas con almacenamiento local cifrado que resuelve el descontrol de flota descartando la banda ancha satelital por sobrecosto.
5. El diseño de aislamiento criptográfico de 686 llaves HSM (RT-11.10).
6. La modelación formal del TCO de 8.375,4 UF conciliado con los aranceles E-26 y el límite de inversión de Gordon-Loeb.

## Control de calidad

- [x] El resumen no contiene citas ni cifras no verificadas.
- [x] El aporte propio menciona contribuciones reales, no intenciones.
- [x] Curimón aparece como caso de aplicación y TI-12 como tema principal.
- [x] No se promete contenido inexistente en el cuerpo.
- [x] Persona 1 puede reconstruir oralmente el razonamiento.
