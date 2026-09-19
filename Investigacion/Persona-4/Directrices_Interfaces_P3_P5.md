# Directrices Obligatorias de Interfaz y Coordinación Cruzada (Anti-C9)
## Requerimientos Financieros y Técnicos para Persona 3 y Persona 5

**Asignatura:** Taller de Formulación de Proyectos Informáticos (ICI-5444) · Escuela de Informática, PUCV  
**Empresa Asignada:** AudIT (Empresa 10)  
**Tema de Investigación:** TI-12 · *Cumplimiento normativo en proyectos TIC: Ley 21.719, Ley 21.663 (ANCI) y marco internacional*  
**Caso de Estudio:** Caso 10 — *Transportes Curimón S.A.*  
**Emisor:** Persona 4 (*Compliance Cost Modeler & Financial Impact Analyst*)  
**Destinatarios:** Persona 3 (*Marco Internacional, GRC e ISO 27001*) y Persona 5 (*Arquitectura Técnica & Caso 10*)  
**Fecha de Congelamiento:** 16 de Septiembre de 2026  
**Propósito:** Establecer los límites, supuestos y partidas presupuestarias congeladas que P3 y P5 **deben acatar e integrar obligatoriamente** en sus respectivos capítulos, blindando al equipo AudIT contra penalizaciones por incongruencia cruzada bajo el Comunicado 9.

---

```
┌──────────────────────────────────────────────────────────────────────────────┐
│                    PRINCIPIO GENERAL DE BLINDAJE ANTI-C9                     │
├──────────────────────────────────────────────────────────────────────────────┤
│ "Ningún integrante del equipo puede diseñar, dimensionar o recomendar        │
│ componentes técnicos, plataformas de software o calendarios de certificación │
│ que contradigan o no cuenten con respaldo en el Modelo Financiero de P4".   │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

# SECCIÓN 1: REQUERIMIENTOS E INTERFACES PARA PERSONA 3
### (Marco Internacional, Gobierno, Riesgo y Cumplimiento - GRC, y Certificación ISO/IEC 27001:2022)

Persona 3 debe leer, aplicar y respetar taxativamente los siguientes requerimientos en la redacción de su capítulo:

### 1.1 Volumetría Operativa del Caso que P3 debe Considerar
Toda evaluación comparativa y recomendación técnica de herramientas GRC debe realizarse considerando la escala real de Transportes Curimón S.A.:
* **374 camiones activos** con emisión continua de telemetría y georreferenciación GPS (60,4% de flota subcontratada).
* **454 conductores registrados** en total: 196 de planta y **258 externos subcontratados**.
* **148 empresas transportistas terceras** que requieren gestión automatizada de acuerdos DPA.
* **Horizonte Contractual:** **56 meses** (20 meses de implementación en Etapas 1 y 2, más 36 meses de operación).
* **Tránsito Internacional:** ~1.900 viajes anuales a Mendoza, Argentina (transferencia internacional de datos).

### 1.2 Imposición sobre Selección y Cuadro Comparativo de Plataformas GRC
Para evitar incongruencias con el presupuesto ya modelado por Persona 4:
1. **Herramientas Obligatorias en la Comparativa:** En su cuadro comparativo de plataformas GRC ($\ge 8$ herramientas evaluadas según el estándar de la cátedra), Persona 3 **debe incluir obligatoriamente a OneTrust y Vanta**.
2. **Plataforma Seleccionada / Recomendada:**
   * La recomendación técnica final de P3 debe apuntar a una solución que encaje en el **techo financiero presupuestado por P4 de USD 11.500 a USD 18.000 anuales** (equivalente a ~290 UF a 420 UF anuales con paridades al 16/09/2026).
   * **Línea Base Presupuestaria de P4:**
     * *Escenario Base / Corporativo:* **OneTrust Privacy Automation** cotizado en **USD 18.000 / año** (SaaS Cloud para transporte y logística).
     * *Escenario Pyme / Sensibilidad:* **Vanta Trust Platform** cotizado en **USD 11.500 / año**.
   * *Prohibición Anti-C9:* P3 **no puede recomendar como solución definitiva** herramientas enterprise de alto coste como ServiceNow GRC Enterprise o MetricStream cuyos aranceles de entrada superen los USD 50.000 anuales, ya que destruiría la viabilidad económica del proyecto licitado.
3. **Módulos Funcionales que P3 debe justificar en la herramienta:**
   * Mapeo automatizado de flujos de datos y generación de Registros de Actividades de Tratamiento (RAT, Art. 28 Ley 21.719).
   * Portal de gestión de derechos ARCO para conductores y clientes.
   * Repositorio y trazabilidad de consentimientos digitales de los 258 conductores externos.
   * Gestión del ciclo de vida de proveedores y contratos DPA para los 148 transportistas.

### 1.3 Calendario e Hitos de Certificación ISO/IEC 27001:2022
Persona 3 debe armonizar su propuesta metodológica de SGSI con el flujo de caja contractual a 56 meses establecido por P4:
1. **Hito de Auditoría de Certificación Inicial (Fases 1 y 2):**
   * Debe ubicarse temporalmente en el **Mes 18** (hacia el cierre de la Etapa 2 de implementación del sistema, previo a la entrada en operación comercial plena en el Mes 21).
   * **Presupuesto Asignado por P4:** **380 UF** (~$15.558.000 CLP al 16/09/2026), respaldado en cotizaciones formales de organismos acreditados en Chile (BSI Group / Bureau Veritas / SGS).
2. **Auditorías de Seguimiento / Vigilancia Anual:**
   * Deben programarse en los **Años 3, 4 y 5 de operación (Meses 30, 42 y 54)**.
   * **Presupuesto Asignado por P4:** **110 UF anuales** (~$4.500.000 CLP al 16/09/2026 por auditoría anual de vigilancia).
   * *Prohibición Anti-C9:* P3 no puede indicar que la empresa se certifica en el Mes 3 de inicio del proyecto (inviable técnica y documentalmente) ni proponer auditorías semestrales externas que no estén financiadas.

### 1.4 Resumen de Partidas Congeladas para P3

| Concepto / Entregable P3 | Parámetro Financiero Fijado por P4 | Impacto en Capítulo de P3 |
| :--- | :---: | :--- |
| **Suscripción Plataforma GRC** | USD 18.000 / año (OneTrust) | Incluir en tabla comparativa y justificar adecuación a Curimón. |
| **Certificación Inicial ISO 27001** | 380 UF (Mes 18) | Fijar hito en cronograma de implantación del SGSI. |
| **Vigilancia Anual ISO 27001** | 110 UF / año (Años 3, 4 y 5) | Contemplar en plan de mantenimiento continuo del SGSI. |

---

# SECCIÓN 2: REQUERIMIENTOS E INTERFACES PARA PERSONA 5
### (Arquitectura Técnica, Flujos de Datos, Controles de Seguridad y Caso Curimón S.A.)

Persona 5 debe leer, aplicar y respetar taxativamente los siguientes requerimientos en la elaboración de sus diagramas y especificaciones:

### 2.1 Volumetría Operativa Inmutable del Caso 10
Persona 5 es el responsable de caracterizar los flujos de datos y diseñar la arquitectura técnica de Curimón S.A. Sus modelos deben procesar exactamente:
* **374 camiones activos:** Cada vehículo genera telemetría de ruta, velocidad, frenado y geolocalización satelital continua cada 30 segundos. Al estar asociados a un conductor identificable, constituyen **datos personales protegidos**.
* **454 conductores registrados:**
  * **196 conductores propios (planta):** Amparados en relación laboral directa y contrato de trabajo (fines de seguridad en ruta y control operacional).
  * **258 conductores externos subcontratados:** Pertenecen a terceras empresas. Su monitoreo continuo fuera del horario de servicio constituye intromisión ilegítima. Exigen **base de licitud explícita, consentimiento digital informado y botón de desactivación de tracking al terminar la jornada de carga**.
* **148 empresas transportistas subcontratadas:** Cada una requiere anexos contractuales de Encargado de Tratamiento (*Data Processing Agreement - DPA*).
* **Flujo Transfronterizo a Mendoza:** ~1.900 cruces internacionales al año a través del paso Los Libertadores. P5 debe diagramar el cruce de datos telemáticos hacia servidores o receptores en Argentina, lo que activa el régimen de transferencia internacional (Art. 38 Ley 21.719).

### 2.2 Regla de Oro Anti-C9: Correspondencia Biunívoca 1:1
```
┌──────────────────────────────────────────────────────────────────────────────┐
│ "Todo componente técnico, servidor, base de datos o módulo de seguridad      │
│ que P5 dibuje en su arquitectura técnica DEBE tener una celda presupuestaria │
│ explícita en el TCO de P4. Cero componentes huérfanos".                      │
└──────────────────────────────────────────────────────────────────────────────┘
```

### 2.3 Partidas Presupuestarias Técnicas Asignadas y Límites de Diseño
Persona 4 ya ha valorizado y reservado el presupuesto para la infraestructura de seguridad. P5 debe ceñirse a estos límites tecnológicos:

1. **Cifrado a Nivel de Campo en Base de Datos (Exigencia RT-11.10 de las Bases Técnicas):**
   * **Presupuesto CAPEX Asignado por P4:** **120 UF** (~$4.913.000 CLP al 16/09/2026) para consultoría de implementación, configuración de esquemas y llaves criptográficas.
   * **Diseño Exigido a P5:** Debe implementar cifrado de columnas sensibles (identidad conductores externos, remuneraciones/tarifas de transportistas y coordenadas satelitales) en reposo y tránsito sobre base de datos relacional/series de tiempo (PostgreSQL / TimescaleDB).
   * **Gestión de Llaves (KMS):** P5 debe apoyarse en un servicio KMS gestionado en la nube (AWS KMS, Google Cloud KMS o Azure Key Vault).
   * *Prohibición Anti-C9:* P5 **no debe diseñar ni requerir servidores criptográficos físicos dedicados on-premise (HSM físico)** en la sala de servidores de San Bernardo (RT-06.01), ya que un appliance HSM de hardware cuesta entre USD 30.000 y USD 60.000 y **no está financiado** en el proyecto.
2. **Módulo Digital de Gestión de Consentimiento Móvil (Art. 12 Ley 21.719):**
   * **Presupuesto CAPEX Asignado por P4:** **45 UF** (~$1.842.000 CLP al 16/09/2026) para desarrollo e integración en la app móvil.
   * **Diseño Exigido a P5:** P5 debe diagramar en el flujo móvil del conductor una pantalla obligatoria de consentimiento previo al encendido del GPS del camión, con registro de timestamp, IP y versión de términos aceptados.
3. **Plataforma GRC e Integración de Evidencias:**
   * **Presupuesto Asignado por P4:** **1.355 UF a 56 meses** (licenciamiento SaaS gestionado).
   * **Diseño Exigido a P5:** P5 debe dibujar la plataforma GRC (OneTrust / Vanta) conectada vía API o webhook con la base de datos de Curimón para alimentar automáticamente el Registro de Actividades de Tratamiento (RAT).
4. **Roles Técnicos de Soporte y Operación:**
   * CISO / Encargado de Seguridad TI (dedicación presupuestada: 48 h/mes en implantación y 24 h/mes en operación).
   * DPO Fraccional (dedicación presupuestada: 40 h/mes en implantación y 24 h/mes en operación).
   * Analista QA / Cumplimiento (dedicación presupuestada: 64 h/mes en implantación y 16 h/mes en operación).

### 2.4 Resumen de Partidas Congeladas para P5

| Componente Técnico en Arquitectura P5 | Partida Financiera P4 | Especificación Tecnológica Obligatoria |
| :--- | :---: | :--- |
| **Cifrado RT-11.10 en BD** | 120 UF CAPEX | Cifrado a nivel de campo con Cloud KMS (sin HSM on-premise). |
| **Módulo Consentimiento Móvil** | 45 UF CAPEX | Componente en la app de conductores para los 258 externos. |
| **SaaS GRC (OneTrust / Vanta)** | 1.355 UF TCO | Nodo SaaS en nube conectado por API para auditoría continua. |
| **Seguridad Perimetral / SOC** | Cubierto en CISO E-26 | Procedimiento de reporte ANCI CSIRT en menos de 3 horas. |

---

## 3. Mecanismo de Validación Cruzada Previa a la Entrega Final

Antes de que Persona 1 ensamble el informe maestro el Día 5:
1. Persona 3 debe cotejar su tabla comparativa de herramientas con la Tabla de Precios (Entregable 3) de Persona 4.
2. Persona 5 debe revisar su diagrama de arquitectura junto con Persona 4 para verificar celda por celda que no exista ningún componente huérfano ni omisión de costos.
3. Ambos integrantes deben firmar la conformidad en la bitácora interna de trabajo.
