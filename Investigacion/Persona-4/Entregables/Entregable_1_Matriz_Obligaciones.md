# Entregable 1: Matriz de Obligaciones Aplicables al Caso 10 (Curimón S.A.)
## Modelado de Requerimientos Normativos y Valorización de Cumplimiento

**Asignatura:** Taller de Formulación de Proyectos Informáticos (ICI-5444) · Escuela de Informática, PUCV  
**Empresa Consultora:** AudIT (Empresa 10)  
**Tema de Investigación:** TI-12 · *Cumplimiento normativo en proyectos TIC: Ley 21.719, Ley 21.663 (ANCI) y marco internacional*  
**Proyecto de Aplicación:** Caso 10 — *Transportes Curimón S.A.*  
**Rol Responsable:** Persona 4 (*Compliance Cost Modeler & Financial Impact Analyst*)  
**Estado:** Versión Definitiva 2.1 — 13 Obligaciones Fácticas del Caso 10, Delimitación Laboral DT y Conciliación E-24 / TCO 7.705,0 UF  
**Paridades Oficiales Contractuales (Formulario E-24 / Bases Administrativas FEP01.26, Art. 9.3) (8):**  
* **1 UF = $40.000 CLP** (Fijo contractual licitación) (8)  
* **1 USD = $900 CLP** (Fijo contractual licitación · Factor: $1\text{ USD} = 0,0225\text{ UF}$) (8)  
* **1 EUR = $1.000 CLP** (Fijo contractual licitación · Factor: $1\text{ EUR} = 0,0250\text{ UF}$) (8)  
* **Tasa de Evaluación Económica Contractual:** $i = 0,9\%\text{ mensual}$ ($11,35\%\text{ efectivo anual}$, crédito de consumo E-24)  
* **1 UTM = $70.000 CLP** (Referencia tributaria contractual) (8)  

---

## 1. Presentación y Enfoque Metodológico

Esta matriz traduce el marco normativo aplicable al Caso 10 —*Ley N° 21.719 (1) que reforma estructuralmente la Ley N° 19.628 sobre Protección de Datos Personales (2), Ley N° 21.663 Marco de Ciberseguridad (4), doctrina vinculante de la Dirección del Trabajo (10)(11) y la norma ISO/IEC 27001:2022 (7)*— en un plan riguroso de ingeniería económica y técnica.

El modelo opera como un **puente metodológico** entre dos realidades:
1. **La Realidad Fáctica y Restricciones del Caso 10 (5):** Extraída directamente de las Bases Técnicas de la Licitación (`FEP03.10` y `FEP02.26`), considerando la volumetría inmutable de **374 camiones** (340 con GPS previo y 34 subcontratados sin dispositivo), **454 conductores** (196 propios y 258 externos subcontratados), **148 transportistas** (personas naturales y pymes de 1 a 4 camiones), **84 clientes corporativos**, flujos internacionales a Mendoza (~1.900 cruces/año) y las cláusulas técnicas obligatorias (**RT-11.10, RT-11.18, RT-11.19, RT-16.09, RT-16.30, RT-17.01 y RT-22.04**).
2. **La Propuesta de Ingeniería de Cumplimiento de AudIT:** Solución tecnológica y presupuestaria que da respuesta a las brechas del caso, estructurada bajo las bandas tarifarias oficiales del **Formulario E-26** (`FEP01.26`, Art. 13.5) (6) y respaldada en estudios de mercado (9), proyectada en el horizonte contractual de **56 meses** (Meses 1 a 12: Etapa 1; Meses 13 a 20: Etapa 2; Meses 21 a 56: Operación continua) (5).

### 1.1 Delimitación Laboral y Doctrina de la Dirección del Trabajo (196 Choferes Propios vs. 258 Externos)

El diagnóstico de los 454 choferes exige una delimitación jurídica estricta para evitar contingencias laborales y de privacidad:
* **196 Conductores Propios (Trabajadores Dependientes):** Sujetos al Código del Trabajo y a la doctrina vinculante de la Dirección del Trabajo (**Dictámenes DT Ord. N° 569/020 y Ord. N° 2328/130**) (10)(11). La georreferenciación GPS y la telemetría sólo son jurídicamente lícitas durante la **jornada laboral pactada** y para fines de coordinación logística y seguridad en ruta. Queda estrictamente prohibido el monitoreo en tiempos de descanso, permisos, feriados o fuera de turno, consagrando el **derecho a la desconexión digital e intimidad**. La arquitectura técnica de AudIT implementa el corte automático de telemetría fuera de servicio.
* **258 Conductores Externos (Subcontratados / Tercerizados):** Pertenecen a los 148 transportistas independientes. No existe vínculo de subordinación con Curimón S.A., por lo que su tratamiento telemático se rige bajo la Ley N° 21.719 (Arts. 12 y 13 Ley 19.628), requiriendo consentimiento explícito, granular e informado en la App móvil (OB-01, OB-12) y convenios DPA con sus empleadores (OB-06).

### 1.2 Principio Contable de No Doble Imputación (Eliminación de Doble Cobro CAPEX/OPEX)

Para erradicar cualquier observación de doble cobro entre partidas de desarrollo inicial y costos operacionales recurrentes:
* **Retainers Mensuales Ininterrumpidos (OPEX):** El DPO (36,0 UF/mes = 2.016,0 UF) y el CISO (48,0 UF/mes = 2.688,0 UF) inician funciones desde el **Mes 1**. Bajo el esquema de tarifa plana amortizada (*blended retainer fee*), absorben las labores de gobernanza continua, supervisión del diseño regulatorio, revisión del algoritmo de fatiga (OB-11), protocolos biométricos (OB-12) y guardia de respuesta ante incidentes (OB-08, OB-13).
* **Inversión Inicial Específica (CAPEX):** Se circunscribe a desarrollos de software singulares (App consentimiento), configuración de infraestructura criptográfica, honorarios legales externos por productos cerrados (EIPD, DPA, transferencias internacionales) y la auditoría arancelaria inicial ISO 27001 con organismo acreditado (BSI/SGS). Existe una separación contable nítida y estricta entre CAPEX y OPEX.

> [!NOTE]
> **Nota de Técnica Legislativa y Estado de Vigencia Oficial al 16/09/2026 (1)(2)(3)(4)(7)(10)(11):**  
> * **Ley N° 21.719 (reforma estructural a la Ley N° 19.628) (1)(2):** Promulgada y publicada en el Diario Oficial el 13 de diciembre de 2024 (Boletín N° 11.144-07). Cuenta con **vigencia diferida (*vacatio legis* de 24 meses)**, entrando en régimen general el **13 de diciembre de 2026**. Verificación oficial en BCN al 16 de septiembre de 2026. Los artículos citados corresponden al texto refundido y reformado de la Ley N° 19.628.
> * **Ley N° 21.663 (Marco de Ciberseguridad) (4):** Publicada en el Diario Oficial el 8 de abril de 2024. Se encuentra **plenamente vigente**, con fiscalización y reporte activo al CSIRT Nacional / ANCI. Verificación BCN al 16 de septiembre de 2026.
> * **Norma ISO/IEC 27001:2022 (7):** Estándar internacional plenamente vigente, adoptado por el Instituto Nacional de Normalización (INN Chile). Verificación al 16 de septiembre de 2026.

---

## 2. Matriz Consolidada de Obligaciones Normativas (13 Requerimientos Caso 10)

| ID | Cuerpo Normativo, Estado de Vigencia & Art. Exacto | Obligación Concreta | Aplicación Operativa al Caso Curimón S.A. (Diagnóstico Fáctico) | Actividad de Cumplimiento Requerida (Propuesta Técnica AudIT) | Rol Responsable (E-26 / Proxy) (6) | Plazo Normativo & Hito Operativo | Naturaleza & Costo Estimado (UF y CLP) (8) |
| :---: | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **OB-01** | **Ley N° 21.719 (que incorpora el Art. 3° bis y sustituye los Arts. 12-13 de la Ley N° 19.628)** (1)(2)<br>*(DO 13/12/2024 · Vigencia diferida: vacatio legis 24 meses, rige 13/12/2026 · BCN: 16/09/2026)* | Base de licitud para tratamiento de datos personales y consentimiento informado. | **RT-11.10 y RT-22.04 (5):** 258 conductores externos subcontratados no son trabajadores de Curimón. Su monitoreo GPS continuo exige consentimiento explícito y verificable. | Desarrollo e integración del Módulo Digital de Consentimiento en la App Móvil del Conductor (RT-17.01) con firma electrónica y botón de revocación (RT-16.30) (5). | Analista Diseñador Experto (20h) + Analista QA Experto (15h) + DPO Proxy (5h) (6) | Ex ante al inicio del tratamiento (Art. 12 Ley 19.628) / Hito: Mes 12 | **CAPEX:** **45,0 UF**<br>($1.800.000 CLP) (8) |
| **OB-02** | **Ley N° 21.719 (que incorpora los Arts. 3° sexies y 14 bis a la Ley N° 19.628)** (1)(2)<br>*(DO 13/12/2024 · Vigencia diferida: vacatio legis 24 meses, rige 13/12/2026 · BCN: 16/09/2026)* | Principio de seguridad de los datos: medidas técnicas de cifrado en reposo y tránsito. | **RT-11.10 (5):** Cifrado a nivel de campo obligatorio para datos personales de 258 conductores externos, georreferenciación en tiempo real y tarifas comerciales de 148 transportistas. | Implementación de cifrado a nivel de campo en PostgreSQL/TimescaleDB en reposo y tránsito, con llaves gestionadas en Azure Key Vault (Microsoft Azure Chile Central). | Encargado de Seguridad TI (CISO) + Arquitecto Experto (Especialista Cloud Azure) (6) | Principio de seguridad desde el diseño y por defecto (Art. 14 bis) / Hito: Meses 6-12 | **CAPEX:** **120,0 UF**<br>($4.800.000 CLP) (8) |
| **OB-03** | **Ley N° 21.719 (que incorpora el Art. 14 ter a la Ley N° 19.628)** (1)(2)<br>*(DO 13/12/2024 · Vigencia diferida: vacatio legis 24 meses, rige 13/12/2026 · BCN: 16/09/2026)* | Registro de Actividades de Tratamiento (RAT) y trazabilidad de accesos. | **RT-05.15 y RT-16.09 (5):** Datos hoy dispersos en 4 planillas Excel. Obligatoriedad de auditar qué cliente accede a la posición de camiones y bajo qué autorización. | Levantamiento de inventario de datos de 454 conductores y 84 clientes; parametrización y actualización continua del RAT en plataforma GRC (CISO Assistant Pro) con revisiones semestrales (15 UF en E1, 10 UF en E2 y 45 UF en E3 = 70,0 UF total en 56 meses). | DPO (Proxy Jefe de Proyecto E-26) (6) | Actualización semestral permanente (Art. 14 ter) / Hito: Continuo (56 meses) | **OPEX:** **70,0 UF** (56 meses)<br>*(15 UF/año amortizado)*<br>($2.800.000 CLP) (8) |
| **OB-04** | **Ley N° 21.719 (que incorpora el Art. 15 ter a la Ley N° 19.628)** (1)(2)<br>*(DO 13/12/2024 · Vigencia diferida: vacatio legis 24 meses, rige 13/12/2026 · BCN: 16/09/2026)* | Evaluación de Impacto en la Protección de Datos (EIPD / DPIA). | Flota total de 374 unidades: 340 con GPS en 3 plataformas dispares y 34 camiones subcontratados sin dispositivo integrados vía App Móvil (RT-17.01) (5). Tratamiento masivo y continuo de localización satelital. | Redacción técnica de la EIPD inicial: mapa de riesgos de invasión a la privacidad, análisis de proporcionalidad y plan de mitigación técnica. | Asesor Legal Externo TIC + DPO Proxy (6)(9) | Previo al tratamiento masivo y de alto riesgo (Art. 15 ter) / Hito: Mes 10 | **CAPEX:** **80,0 UF**<br>($3.200.000 CLP) (8) |
| **OB-05** | **Ley N° 21.719 (que incorpora el Art. 48 a la Ley N° 19.628)** (1)(2)<br>*(DO 13/12/2024 · Vigencia diferida: vacatio legis 24 meses, rige 13/12/2026 · BCN: 16/09/2026)* | Nombramiento formal del Delegado de Protección de Datos (DPO). | Curimón procesa datos de localización masiva y transfronteriza, requiriendo interlocución formal e independiente ante la futura Agencia (APDP) (1)(5). | Designación formal del DPO fraccional con reporte directo al Directorio, atención a derechos ARCO y supervisión continua de cumplimiento bajo tarifa retainer. | DPO (Proxy Jefe de Proyecto E-26) (6)(9) | Vacatio legis 24 meses (Diciembre 2026, Art. 48) / Hito: Vigencia permanente 56 meses | **OPEX:** **36,0 UF/mes**<br>($1.440.000 CLP/mes) (8) |
| **OB-06** | **Ley N° 21.719 (que sustituye los Arts. 25 y 26 de la Ley N° 19.628)** (1)(2)<br>*(DO 13/12/2024 · Vigencia diferida: vacatio legis 24 meses, rige 13/12/2026 · BCN: 16/09/2026)* | Formalización de contratos de Encargado de Tratamiento (*DPA*). | 148 transportistas subcontratados (empresas y personas naturales dueños-choferes) gestionan camiones y datos de localización sin acuerdos de privacidad (5). | Redacción y formalización de convenios DPA diferenciados: contratos marco corporativos para personas jurídicas y anexos simplificados de adhesión para personas naturales. | Asesor Legal Especializado en TIC (6)(9) | Previo a la transferencia a encargados (Arts. 25 y 26) / Hito: Meses 3-8 | **CAPEX:** **95,0 UF**<br>($3.800.000 CLP) (8) |
| **OB-07** | **Ley N° 21.719 (que incorpora los Arts. 26 bis a 26 quáter a la Ley N° 19.628)** (1)(2)<br>*(DO 13/12/2024 · Vigencia diferida: vacatio legis 24 meses, rige 13/12/2026 · BCN: 16/09/2026)* | Régimen de Transferencia Internacional de Datos Personales. | **RT-05.23 (5):** ~1.900 cruces internacionales al año a través del paso Los Libertadores hacia Mendoza (Argentina) con flujo de datos de flota y choferes. | Redacción y suscripción de Cláusulas Contractuales Tipo (SCC) transfronterizas Chile-Argentina y verificación de idoneidad regulatoria. | Asesor Legal Especializado en TIC (6)(9) | Previo a flujo transfronterizo (Arts. 26 bis a 26 quáter) / Hito: Mes 12 | **CAPEX:** **35,0 UF**<br>($1.400.000 CLP) (8) |
| **OB-08** | **Ley N° 21.663 Marco de Ciberseguridad, Arts. 5, 8, 9 y 25** (4)<br>*(DO 08/04/2024 · Plenamente vigente · BCN: 16/09/2026)* | Deber de reporte de ciberincidentes y notificación en menos de 3 horas. | Operación logística crítica (flota rueda 24/7/365, RT-10.05) (5). Exposición de la torre de control a incidentes de indisponibilidad o ransomware. | Protocolo de triaje técnico de incidentes, mesa de escalamiento y enlace formal 24/7 de reporte al CSIRT Nacional en menos de 3 horas bajo guardia CISO E-26 (4). | Encargado de Seguridad TI (CISO E-26) (6) | Plazo perentorio < 3 horas notificación preliminar CSIRT (Art. 9 Ley 21.663 y D.S. N° 295/2024) / Hito: Guardia 24/7 | **OPEX:** **48,0 UF/mes**<br>($1.920.000 CLP/mes) (8) |
| **OB-09** | **ISO/IEC 27001:2022 (Cláusulas 4-10)** (7)<br>*(Estándar vigente internacional / INN Chile · Verificación: 16/09/2026)* | Certificación del Sistema de Gestión de Seguridad de la Información (SGSI). | Exigencia de licitación para garantizar ciberresiliencia del servicio de transporte y blindar la infraestructura en nube (5). | Auditoría externa de certificación inicial (Fases 1 y 2 con BSI/SGS) y auditorías anuales de mantenimiento en los Años 3, 4 y 5 (7)(9). | Organismo Certificador Acreditado (BSI / SGS) (7) | Exigencia contractual bases / Hito: Mes 18 (Certif.) y Años 3-5 (Vigilancia) | **CAPEX:** **387,50 UF** (Certif. $15.500.000 CLP)<br>**OPEX:** **112,50 UF/año** (Vig. $4.500.000 CLP/año) (8) |
| **OB-10** | **Ley N° 21.719 (que incorpora el Art. 49 a la Ley N° 19.628)** (1)(2)<br>*(DO 13/12/2024 · Vigencia diferida: vacatio legis 24 meses, rige 13/12/2026 · BCN: 16/09/2026)* | Modelo de Prevención de Infracciones (Atenuante de Responsabilidad). | Blindaje patrimonial de Curimón para reducir o eximir sanciones de hasta 20.000 UTM (1.400 millones CLP) ante filtraciones o fallas fortuitas (1)(8). | Cuatro auditorías anuales de mantenimiento del modelo de prevención ejecutadas al cierre de implementación (Mes 20) y en operación (Meses 32, 44 y 56 de contrato) (5). | DPO + Analista QA Experto (E-26) (6) | Anual para conservar atenuante calificada de responsabilidad (Art. 49) / Hito: Meses 20, 32, 44 y 56 | **OPEX:** **60,0 UF/año**<br>($2.400.000 CLP/año) (8) |
| **OB-11** | **Ley N° 21.719 (que incorpora el Art. 8° bis a la Ley N° 19.628)** (1)(2)<br>*(DO 13/12/2024 · Vigencia diferida: vacatio legis 24 meses, rige 13/12/2026 · BCN: 16/09/2026)* | Decisiones individuales automatizadas y modelo de fatiga. | **RT-10.05 y Caso 10 (5):** Algoritmo telemático de fatiga y comportamiento en cabina con capacidad de bloqueo o suspensión de despacho. La ley prohíbe decisiones automatizadas con efectos jurídicos adversos sin derecho a revisión humana. | Procedimiento mandatorio de explicación algorítmica, impugnación y revisión humana del bloqueo de despacho; protocolo de doble check por jefatura de tráfico y DPO. | DPO Proxy + Analista QA Experto + Operaciones Curimón (6) | Ex ante a producción (Art. 8 bis) / Hito: Mes 11 (Diseño) y operación 56 meses | **OPEX:** **0,00 UF marginal**<br>*(Absorbido en retainers DPO OB-05 y QA continuo)* (8) |
| **OB-12** | **Ley N° 21.719 (que modifica Arts. 2° letra g y 16 de la Ley N° 19.628)** (1)(2)<br>*(DO 13/12/2024 · Vigencia diferida: vacatio legis 24 meses, rige 13/12/2026 · BCN: 16/09/2026)* | Tratamiento de datos sensibles y biometría de conductores. | **RT-17.01 y Caso 10 (5):** Enrolamiento biométrico facial o dactilar de 454 choferes en app móvil y sensores de cabina. Los datos biométricos constituyen categoría sensible. | Protocolo de consentimiento expreso reforzado para biometría; habilitación obligatoria de alternativa no biométrica (credencial digital/PIN) y borrado seguro de plantillas. | DPO Proxy + Analista Diseñador Experto (E-26) (6) | Previo al enrolamiento de conductores / Hito: Mes 8 | **CAPEX:** **0,00 UF marginal**<br>*(Alcance funcional embebido en App OB-01 y DPO OB-05)* (8) |
| **OB-13** | **Bases Técnicas FEP02 (RT-11.18 y RT-11.19)** (5)<br>*(Exigencia contractual directa · Vigencia desde adjudicación · BCN/PUCV: 16/09/2026)* | Aviso contractual perentorio a clientes corporativos (<2h y <24h). | **RT-11.18 y RT-11.19 (5):** Obligación contractual de notificar a los 84 clientes corporativos incidentes críticos en < 2 horas y brechas de seguridad/privacidad en < 24 horas. | Protocolo de escalamiento multicanal (API B2B, SMS y correo seguro) integrado a torre de control y despacho de reportes preliminares bajo guardia 24/7/365. | Encargado de Seguridad TI (CISO E-26) + Mesa de Ayuda AudIT (6) | Contractual perentorio: < 2h crítico, < 24h brechas / Hito: Mes 12 y guardia 24/7 | **OPEX:** **0,00 UF marginal**<br>*(Absorbido en guardia 24/7 CISO OB-08 y mesa de ayuda AudIT)* (8) |

---

## 3. Memoria de Cálculo Detallada por Partida

Para garantizar absoluta trazabilidad y rigor técnico sin ruptura de ficción, a continuación se transparenta la fórmula de cálculo de cada partida en base a horas y tarifas oficiales del Formulario E-26 (6) y paridades oficiales (8):

### 3.1 Partidas de Inversión Inicial (CAPEX — Meses 1 a 20)

* **OB-01 (Módulo de Consentimiento Móvil — 45,0 UF):**
  $$\text{Costo} = (20\text{ h Analista Diseñador Experto} \times 1,0\text{ UF/h}) + (15\text{ h Analista QA Experto} \times 1,0\text{ UF/h}) + (5\text{ h DPO} \times 2,0\text{ UF/h}) = 20 + 15 + 10 = \mathbf{45,0\text{ UF}}\quad(\$1.800.000\text{ CLP})$$
* **OB-02 (Cifrado RT-11.10 en Base de Datos y Telemetría — 120,0 UF):**
  $$\text{Costo} = (40\text{ h Encargado Seguridad TI} \times 2,0\text{ UF/h}) + (20\text{ h Arquitecto Experto Cloud Azure} \times 2,0\text{ UF/h}) = 80 + 40 = \mathbf{120,0\text{ UF}}\quad(\$4.800.000\text{ CLP})$$
  *(Nota: El consumo criptográfico recurrente de Azure Key Vault en Azure Chile Central es 100% absorbido por el tier CSP de AudIT / P5, costo marginal 0,00 UF).*
* **OB-04 (Elaboración formal EIPD/DPIA — 80,0 UF):**
  $$\text{Costo} = (30\text{ h Asesor Legal TIC} \times 2,0\text{ UF/h}) + (10\text{ h DPO Proxy} \times 2,0\text{ UF/h}) = 60 + 20 = \mathbf{80,0\text{ UF}}\quad(\$3.200.000\text{ CLP})$$
* **OB-06 (Estandarización 148 Contratos DPA — 95,0 UF):**
  $$\text{Costo} = 47,5\text{ h Asesor Legal TIC} \times 2,0\text{ UF/h} = \mathbf{95,0\text{ UF}}\quad(\$3.800.000\text{ CLP})$$
  *(Promedio de ~19 minutos de dedicación legal por transportista mediante contrato marco tipificado).*
* **OB-07 (Protocolo Transferencia Internacional Mendoza — 35,0 UF):**
  $$\text{Costo} = 17,5\text{ h Asesor Legal TIC} \times 2,0\text{ UF/h} = \mathbf{35,0\text{ UF}}\quad(\$1.400.000\text{ CLP})$$
* **OB-09 (Auditoría Externa Inicial ISO 27001 Fases 1+2 — 387,50 UF):**
  Cotización corporativa de organismo acreditado en Chile (BSI Group / SGS) (7)(9): $15.500.000 CLP netos en Mes 18 dividido por $40.000 CLP/UF contractual E-24 = **387,50 UF** ($15.500.000 CLP) (8).
* **OB-12 (Protocolo de Datos Sensibles y Biometría de Conductores — 0,00 UF marginal):**
  El diseño de interfaces para consentimiento biométrico y provisión de alternativa no biométrica se encuentra absorbido íntegramente dentro del alcance funcional del desarrollo del Módulo Digital de Consentimiento (**OB-01**, 45,0 UF) y la supervisión del DPO (**OB-05**). Costo marginal incremental: **0,00 UF** ($0 CLP).

$$\mathbf{Total\;CAPEX\;Matriz} = 45,0 + 120,0 + 80,0 + 95,0 + 35,0 + 387,50 + 0,00 = \mathbf{762,50\;UF}\quad(\$30.500.000\text{ CLP})$$

---

### 3.2 Partidas Operacionales Recurrentes (OPEX — Proyectadas a 56 Meses)

> [!TIP]
> **Esquema Contractual de Tarifa Plana Amortizada (*Blended Retainer Fee*) y Absorción Continua:**  
> Para los roles de DPO (OB-05) y CISO (OB-08), el modelo financiero aplica una **tarifa plana mensual amortizada** a lo largo de los 56 meses. Esta modalidad contractual estabiliza el flujo de caja del cliente Transportes Curimón S.A., absorbiendo en los primeros 20 meses la mayor carga de ingeniería regulatoria, redacción de políticas, supervisión de algoritmos de fatiga (OB-11) y protocolos biométricos (OB-12), manteniendo en régimen operacional la guardia pasiva 24/7 y la atención de incidentes a clientes (OB-13) y a la ANCI (OB-08) sin cobros adicionales ni duplicidades.

* **OB-03 (Actualización Continua del RAT — 70,0 UF en 56 meses):**
  Revisiones semestrales sistemáticas de inventario en plataforma GRC CISO Assistant Pro (DPO a 2,0 UF/h): 15,0 UF en Etapa 1 (Meses 1-12, 7,5h/semestre), 10,0 UF en Etapa 2 (Meses 13-20, 5,0h) y 45,0 UF en Etapa 3 (Meses 21-56, 36 meses a 15 UF/año) = **70,0 UF total en 56 meses** ($2.800.000 CLP).
* **OB-05 (DPO Fraccional E-26 — Retainer 36 UF/mes):**
  $$18\text{ h/mes DPO} \times 2,0\text{ UF/h} = 36\text{ UF mensuales} \rightarrow 36 \times 56\text{ meses} = \mathbf{2.016,0\;UF}\quad(\$80.640.000\text{ CLP})$$
* **OB-08 (CISO TI Protocolo Reporte ANCI — Retainer 48 UF/mes):**
  $$24\text{ h/mes Encargado Seguridad TI} \times 2,0\text{ UF/h} = 48\text{ UF mensuales} \rightarrow 48 \times 56\text{ meses} = \mathbf{2.688,0\;UF}\quad(\$107.520.000\text{ CLP})$$
* **OB-09 (Auditorías Anuales de Vigilancia ISO 27001 — 112,50 UF/año):**
  Auditorías de seguimiento en Años 3, 4 y 5 de contrato (3 ciclos de $4.500.000 CLP/año = 112,50 UF/año a paridad E-24) (7): $112,50 \times 3 = \mathbf{337,50\;UF}\quad(\$13.500.000\text{ CLP})$.
* **OB-10 (Modelo Prevención Infracciones Art. 49 — 60 UF por auditoría):**
  $$20\text{ h DPO} \times 2,0\text{ UF/h} + 20\text{ h QA} \times 1,0\text{ UF/h} = 60\text{ UF por ciclo} \rightarrow 60 \times 4\text{ auditorías (Meses 20, 32, 44 y 56)} = \mathbf{240,0\;UF}\quad(\$9.600.000\text{ CLP})$$
* **OB-11 (Revisión Humana de Decisiones Automatizadas de Fatiga — 0,00 UF marginal):**
  Protocolo de impugnación y revisión humana del bloqueo de despacho por fatiga. Las labores técnicas y operacionales son absorbidas íntegramente en el retainer del DPO (**OB-05**, 36 UF/mes) y la bolsa de QA continuo del proyecto. Costo marginal incremental: **0,00 UF** ($0 CLP).
* **OB-13 (Protocolo de Aviso Perentorio a Clientes <2h / <24h RT-11.18 y RT-11.19 — 0,00 UF marginal):**
  Canal y protocolo de notificación perentoria a los 84 clientes corporativos ante incidentes críticos y brechas. Cubierto al 100% bajo la guardia 24/7/365 del CISO (**OB-08**, 48 UF/mes) y el servicio de mesa de ayuda central de AudIT. Costo marginal incremental: **0,00 UF** ($0 CLP).

$$\mathbf{Total\;OPEX\;Matriz\;a\;56\;Meses} = 70,0 + 2.016,0 + 2.688,0 + 337,50 + 240,0 + 0,00 + 0,00 = \mathbf{5.351,50\;UF}\quad(\$214.060.000\text{ CLP})$$

---

## 4. Resumen Consolidado y Conciliación Hacia el TCO Global (7.705,0 UF)

### 4.1 Subtotal Directo de la Matriz de Obligaciones

| Clasificación Presupuestaria | Total en Unidades de Fomento (UF) | Total en Pesos Chilenos (CLP) (8) | % del Total Matriz |
| :--- | :---: | :---: | :---: |
| **Inversión Inicial (CAPEX Directo — 7 partidas)** | **762,50 UF** | $30.500.000 CLP | 12,47% |
| **Operación Continua (OPEX Directo 56 Meses — 7 partidas)** | **5.351,50 UF** | $214.060.000 CLP | 87,53% |
| **SUBTOTAL DIRECTO 13 OBLIGACIONES** | **6.114,00 UF** | **$244.560.000 CLP** | **100,00%** |

---

### 4.2 Tabla de Conciliación Presupuestaria Analítica (Puente Matriz $\rightarrow$ TCO a 56 Meses)

Conforme a las exigencias del **Comunicado 9 (punto b)** y el **Principio de No Doble Imputación**, a continuación se desglosa la conciliación exacta entre el subtotal de la matriz de obligaciones y el presupuesto consolidado del **Entregable 2 (TCO a 56 Meses)**:

| Partida Presupuestaria Consolidada | Origen y Justificación Metodológica | Monto Total (UF) | Monto Total (CLP E-24) (8) |
| :--- | :--- | :---: | :---: |
| **1. Subtotal de 13 Obligaciones Directas (Matriz)** | Suma consolidada de las 13 obligaciones normativas (OB-01 a OB-13): CAPEX 762,50 UF + OPEX 5.351,50 UF. | **6.114,00 UF** | $244.560.000 CLP |
| **2. Plataforma SaaS GRC (CISO Assistant Pro Enterprise)** | Suscripción SaaS Pro a 56 meses (€2.400/año = 60 UF/año auditada en Azure Chile Central) para RAT, incidentes ANCI y DPA. Ahorro de 1.075 UF vs OneTrust. | **280,00 UF** | $11.200.000 CLP |
| **3. Mantenimiento y Soporte Módulo Consentimiento** | Soporte técnico y adaptaciones evolutivas en App Móvil (30 UF/año en operación continua, Meses 13 a 56). | **135,00 UF** | $5.400.000 CLP |
| **4. Soporte Continuo QA y Asesoría Legal Complementaria** | Analista QA continuo (816 UF menos 80 UF de OB-10 = 736 UF a 1,0 UF/h) + bolsa horas legales externas para peritajes (120 UF menos contingencias). | **586,00 UF** | $23.440.000 CLP |
| **5. Póliza de Ciberriesgo (*Cyber Insurance*)** | Cobertura financiera ante incidentes de ciberseguridad o filtración (Chubb Seguros Chile, $3,6M CLP/año = 90 UF/año). | **420,00 UF** | $16.800.000 CLP |
| **6. Fondo de Contingencia Legal y Remediación** | Fondo de reserva para controversias ante la Agencia y peritajes forenses urgentes. | **170,00 UF** | $6.800.000 CLP |
| **TOTAL TCO CUMPLIMIENTO CONSOLIDADO (56 MESES)** | **Presupuesto Integral del Modelo Económico (Entregable 2)** | **7.705,00 UF** | **$308.200.000 CLP** |

$$\text{Comprobación Presupuestaria Consolidada: } \text{CAPEX } (762,50\text{ UF}) + \text{OPEX } (5.351,50 + 1.591,00 = 6.942,50\text{ UF}) = \mathbf{7.705,00\text{ UF}}\quad(\Delta = 0,000\text{ UF})$$

---

## 5. Checklist de Verificación de Incongruencias (Anti-C9)

- [x] **P1 (Presupuesto de Páginas):** Matriz estructurada en formato tabular compacto de 13 obligaciones, optimizada para ocupar $\le 0,70$ páginas en el informe técnico final.
- [x] **P2 (Marco Legal Chile):** Plazos respetan la *vacatio legis* de la Ley 21.719 (vigencia plena 13 de diciembre de 2026, 24 meses tras DO 13/12/2024) (1)(2); actividades en meses 1 a 20 son de diseño, adecuación contractual e ingeniería previa a la fiscalización de la Agencia. Se integra la doctrina laboral DT (Ord. 569/020 y Ord. 2328/130) para 196 choferes contratados (10)(11).
- [x] **P3 (Marco Internacional / ISO):** Hito de certificación ISO 27001 fijado exactamente en Mes 18 (387,50 UF) y vigilancias anuales de 112,50 UF en años 3, 4 y 5 de contrato (337,50 UF total) (7).
- [x] **P4 (Modelo Económico y Cero Doble Cobro):** Se eliminan cobros duplicados explicitando la absorción en los retainers continuos de DPO y CISO (Mes 1 a 56) de las obligaciones OB-11 y OB-13, y en OB-01 para OB-12. Total TCO: 7.705,00 UF ($308.200.000 CLP).
- [x] **P5 (Arquitectura Técnica):** Cifrado RT-11.10 y Módulo de Consentimiento móvil valorizados en 120 UF y 45 UF respectivamente (5), calzando 1:1 con la arquitectura en Azure Chile Central (Azure Key Vault absorbido al 100% en tier CSP AudIT). Notificaciones contractuales RT-11.18 y RT-11.19 cubiertas bajo guardia CISO 24/7.
- [x] **P6 (Banco de Preguntas):** Cifras oficiales congeladas (TCO 7.705,0 UF, Matriz 6.114,0 UF, multas hasta 20.000 UTM = $1.400M CLP) disponibles para la redacción de alternativas del cuestionario.
- [x] **P7 (Presentación Ejecutiva):** Valores consolidados de CAPEX (762,5 UF), OPEX (6.942,5 UF) y TCO (7.705,0 UF) homologados para los gráficos de las láminas de defensa.
- [x] **P8 (Auditor QA / Datos Reales):** Todas las tarifas provienen del Formulario E-26 (6) y las conversiones se realizan a 1 UF = $40.000 CLP (8).

---

## 6. Bibliografía y Fuentes Primarias Verificables

(1) **Biblioteca del Congreso Nacional de Chile (BCN).** (2024). *Ley N° 21.719: Regula la protección y el tratamiento de los datos personales y crea la Agencia de Protección de Datos Personales*. Publicada en el Diario Oficial el 13 de diciembre de 2024. Texto oficial disponible en: [https://www.bcn.cl/leychile/navegar?idNorma=1209272](https://www.bcn.cl/leychile/navegar?idNorma=1209272).  
(2) **Biblioteca del Congreso Nacional de Chile (BCN).** (1999, texto consolidado y reformado por la Ley N° 21.719). *Ley N° 19.628: Sobre Protección de la Vida Privada*. Texto oficial actualizado disponible en: [https://www.bcn.cl/leychile/navegar?idNorma=141599](https://www.bcn.cl/leychile/navegar?idNorma=141599).  
(3) **Cámara de Diputadas y Diputados de Chile.** (2017-2024). *Historia de la Ley N° 21.719: Tramitación del Proyecto de Ley que regula la protección y el tratamiento de los datos personales y crea la Agencia de Protección de Datos Personales (Boletín N° 11.144-07)*. Disponible en: [https://www.camara.cl/legislacion/ProyectosDeLey/tramitacion.aspx?prmID=11666](https://www.camara.cl/legislacion/ProyectosDeLey/tramitacion.aspx?prmID=11666).  
(4) **Biblioteca del Congreso Nacional de Chile (BCN).** (2024). *Ley N° 21.663: Ley Marco de Ciberseguridad e Infraestructura Crítica de la Información*. Publicada en el Diario Oficial el 8 de abril de 2024. Texto oficial disponible en: [https://www.bcn.cl/leychile/navegar?idNorma=1202434](https://www.bcn.cl/leychile/navegar?idNorma=1202434).  
(5) **Escuela de Informática, Pontificia Universidad Católica de Valparaíso (PUCV).** (2026). *Bases Técnicas del Caso 10: Transportes Curimón S.A. (Código FEP03.10)* y *Bases Técnicas Transversales (Código FEP02.26, Cláusulas RT-11.18 y RT-11.19)*. Asignatura: Taller de Formulación y Evaluación de Proyectos Informáticos (ICI-5444).  
(6) **Escuela de Informática, Pontificia Universidad Católica de Valparaíso (PUCV).** (2026). *Bases Administrativas de la Licitación: Formulario E-24 (Paridades de Evaluación Económica) y Formulario E-26 (Rango de Valores Aceptados para Perfiles Profesionales, Art. 13.5)*. Asignatura: Taller de Formulación y Evaluación de Proyectos Informáticos (ICI-5444). Archivo local en repositorio: `Proyecto/Informe/repo/texto/FEP01_26_Bases_Administrativas_TFEP_01_2026_3.md`.  
(7) **Organización Internacional de Normalización (ISO) / Instituto Nacional de Normalización (INN Chile).** (2022). *ISO/IEC 27001:2022: Information security, cybersecurity and privacy protection — Information security management systems — Requirements*. Ginebra, Suiza.  
(8) **Escuela de Informática, PUCV / Comisión para el Mercado Financiero (CMF).** (2026). *Formulario E-24: Paridades de Conversión Contractuales Oficiales para Evaluación Económica (1 UF = $40.000 CLP, 1 USD = $900 CLP, 1 EUR = $1.000 CLP, 1 UTM = $70.000 CLP)*.  
(9) **Robert Half Chile & Michael Page Chile.** (2025/2026). *Guía Salarial 2025/2026 y Estudio de Remuneraciones en Tecnología, Ciberseguridad, Riesgo y Cumplimiento Normativo*. Santiago, Chile.  
(10) **Dirección del Trabajo de Chile (DT).** (2020). *Dictamen Ordinario N° 569/020: Mecanismos de control audiovisual y geolocalización (GPS) en el ámbito laboral y límites del poder de dirección del empleador*. Santiago, Chile. Disponible en portal oficial DT.  
(11) **Dirección del Trabajo de Chile (DT).** (2018). *Dictamen Ordinario N° 2328/130: Tratamiento de datos personales y biométricos de trabajadores, proporcionalidad y derecho a la desconexión e intimidad*. Santiago, Chile. Disponible en portal oficial DT.
