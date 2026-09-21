# Apertura y Cierre: Cumplimiento Normativo Aplicado al Proyecto TIC de Transportes Curimón S.A.
## Trabajo TI-12 · Empresa Consultora AudIT · Caso 10

**Autor responsable:** Persona 1 (*Lead Editor & System Integrator* — Ignacio C.)  
**Extensión objetivo:** 1,5 a 2 páginas útiles  
**Estado:** versión con redacción humana en secciones restringidas por el punto 6.1

---

## Resumen ejecutivo

Transportes Curimón administra una flota de 374 camiones, 454 conductores (196 propios y 258 externos), 148 transportistas subcontratados y 84 clientes corporativos bajo un contrato licitado a 56 meses con operaciones entre la frontera de Chile y Argentina, es decir, hacia Mendoza. Históricamente, la operación sufría de falta de visibilidad y control sobre sus unidades, con datos de telemetría y jornadas dispersos en planillas informales, lo que impedía costear tramos reales y configuraba un riesgo real ante el nuevo marco regulatorio chileno. El presente trabajo estructura el programa integral de cumplimiento normativo (TI-12) para el proyecto, articulando la Ley N.º 21.719 sobre Protección de Datos Personales (sanciones de hasta 20.000 UTM o 4% de ventas), la Ley N.º 21.663 de Ciberseguridad (notificación obligatoria al CSIRT Nacional en $\le 3\text{ h}$ bajo D.S. 295/2024) y la Ley N.º 25.326 argentina para el tránsito internacional. Se descartó el uso de banda ancha satelital en toda la flota porque era una opción elevada en el precio, adoptándose una arquitectura de conectividad por capas: telemetría por celular como principal, almacenamiento local cifrado y satélite transaccional de respaldo, convergiendo en una vista operacional unificada. La solución se despliega en Azure Chile Central con réplica en East US 2 (bajo Cláusulas Contractuales Tipo), cifrado de campo (RT-11.10) con 686 claves individuales en Azure Key Vault Managed HSM y gobierno GRC. El presupuesto de cumplimiento asciende a 8.375,4 UF netas, representando el 3,9% del contrato de licitación y asegurando un RoSI mayor a +250%.

---

## Introducción

Un proyecto TIC no se puede evaluar solo por si la plataforma funciona o no. Cuando maneja datos personales y sostiene una operación crítica, como ocurre en Transportes Curimón, también debe demostrar que cumple con la ley desde el inicio. Si no existe una base legal clara, si los proveedores no tienen responsabilidades definidas o si no hay un plan para responder ante incidentes, una buena solución técnica igual puede transformarse en un riesgo para la empresa.

El tema TI-12 pide identificar qué obligaciones legales afectan a un proyecto desarrollado o utilizado en Chile. Para este caso, las dos normas principales son la Ley N.º 21.719, que actualiza la protección de datos personales, y la Ley N.º 21.663, que organiza el marco nacional de ciberseguridad mediante la ANCI y el CSIRT Nacional. En términos prácticos, esto obliga a revisar la licitud del tratamiento de datos, la seguridad de la información, los derechos de los titulares, las responsabilidades de cada actor y los plazos de reporte ante incidentes.

La aplicación se realiza sobre el Caso 10, Transportes Curimón S.A. El sistema licitado busca ordenar la información de una flota distribuida, vinculando datos de conductores propios y externos con rutas, jornadas y telemetría. Además, participan transportistas subcontratados, clientes corporativos y proveedores cloud. Por eso, el análisis no puede quedarse en una revisión general de leyes: debe aterrizarse en temas concretos como monitoreo por GPS, contratos de encargo, cifrado, transferencias internacionales, continuidad operacional y respuesta ante incidentes.

El objetivo del informe es conectar el marco legal y técnico con decisiones concretas del proyecto. Para eso se revisan normas nacionales e internacionales, organismos, estándares y herramientas de apoyo, y luego se ordena todo en una matriz con actividades, responsables, plazos, evidencias y costos. La idea final es que el cumplimiento no quede como una declaración general, sino como una parte real de la arquitectura, el presupuesto y la ejecución del proyecto.

### Delimitación del aporte propio

En cumplimiento del Punto 4 de las Indicaciones, AudIT delimita su aporte propio frente a la Ficha TI-12: mientras la ficha suministró el marco conceptual general de las Leyes 21.719 y 21.663, los estándares ISO 27001/27701/42001 y las herramientas base de mercado, el grupo aportó:

1. La incorporación obligatoria de la Ley argentina 25.326 por el paso fronterizo a Mendoza y del marco de atestación SOC 2 Type II para los 84 clientes.
2. La integración del Dictamen DT N.º 569/2018 para regular el monitoreo mediante GPS.
3. La evaluación de Eramba y Osano como herramientas GRC de aporte propio para ponderar el esquema On-Premise vs. SaaS.
4. La formulación de una solución de conectividad por capas con almacenamiento local cifrado que resuelve el descontrol de flota descartando la banda ancha satelital por sobrecosto.
5. El diseño de aislamiento criptográfico de 686 llaves HSM (RT-11.10).
6. La modelación formal del TCO de 8.375,4 UF conciliado con los aranceles E-26 y el límite de inversión de Gordon-Loeb.

---

## Síntesis de integración con el Caso 10

La conexión entre el marco regulatorio y la operación real de Transportes Curimón S.A. demostró que las exigencias legales no admiten una revisión superficial. Al cruzar el marco normativo (P2 y P3), el presupuesto (P4) y la arquitectura tecnológica (P5), aparecen tres relaciones importantes:

Primero, el régimen de corresponsabilidad del Art. 15 bis de la Ley N.º 21.719 obliga a distinguir operativamente entre los 196 conductores propios (amparados en el contrato de trabajo y el Dictamen DT 569/2018) y los 258 conductores dependientes de 148 transportistas subcontratados. Para estos últimos, la licitud del rastreo telemático exige acuerdos de encargo (DPA) específicos y cláusulas de consentimiento expreso en la aplicación móvil antes de liberar turnos.

Segundo, la falta de una Agencia de Protección de Datos constituida y de Cláusulas Contractuales Tipo oficiales en Chile genera una zona gris respecto a la réplica de contingencia en Azure East US 2 y el tránsito a Mendoza. AudIT aborda esta brecha usando de forma preventiva las Cláusulas Tipo del RGPD europeo (Capítulo V) y dejando consideradas en el TCO horas de asesoría legal para ajustarlas cuando la autoridad emita directrices.

Tercero, cada control técnico exigido por las bases queda conectado con una partida concreta del presupuesto: el cifrado de base de datos a nivel de campo (RT-11.10) se cubre con Azure Key Vault (725,4 UF), la gestión del RAT se apoya en la plataforma GRC CISO Assistant Pro (255 UF) y el cumplimiento de ISO/IEC 27001 se respalda con consultoría E-26 y auditoría externa acreditada (387,5 UF). Así se evita proponer controles sin costo asociado o gastos sin justificación normativa.

---

## Conclusiones y recomendaciones estratégicas

### Conclusiones

1. **El cumplimiento es necesario para operar:** La investigación dejó en claro que cumplir con las leyes no es solo un trámite legal o papeleo, sino algo indispensable para que el proyecto funcione en la práctica. Si no se cuenta con bases legales claras o no se avisa a tiempo de incidentes, Curimón se arriesga a multas muy graves que pueden llegar a 20.000 UTM por datos personales o 40.000 UTM por ciberseguridad.
2. **Solución a la desorganización de datos:** El problema de fondo en Curimón era que la información de los camiones y choferes estaba repartida en planillas Excel sin ningún orden ni seguridad. La propuesta de conectar la flota por capas y unificarla en una sola vista resuelve este desorden de raíz, asegurando que los datos viajen protegidos y que no se pierda información en las zonas sin señal.
3. **Inversión justificada:** Gastar **8.375,4 UF netas** ($\text{VAN}_{\text{costo}} = \mathbf{6.582,3\text{ UF}}$) representa apenas el 3,9% de lo que cuesta toda la licitación. Con solo un 2,80% de probabilidad al año de recibir una fiscalización con sanción, el plan de seguridad ya se paga completamente solo, logrando un retorno sobre la inversión (RoSI) superior al $+250\%$.

### Recomendaciones estratégicas priorizadas

1. **Fase 1 · Ordenar contratos y permisos (Meses 1 a 4):** Lo primero es firmar los contratos de encargo con los 148 transportistas externos y pedir el consentimiento en la app a los 258 choferes subcontratados. Además, se debe armar el registro de datos (RAT) antes de activar el rastreo masivo por GPS.
2. **Fase 2 · Montar la plataforma y el enlace de seguridad (Meses 5 a 12):** Desplegar los sistemas en Azure Chile Central, configurar las 686 claves en Key Vault para cifrar los datos de cada transportista y dejar listo el canal de alertas para avisarle al CSIRT Nacional en menos de 3 horas si ocurre un ataque.
3. **Fase 3 · Certificación formal y respaldo final (Meses 13 a 20):** Hacer la auditoría externa para certificar la norma ISO/IEC 27001:2022 con una empresa acreditada y contratar el seguro de ciberriesgo con Chubb, dejando el proyecto completamente respaldado frente a los 84 clientes corporativos.
