# Capítulo 5: Impacto Económico, TCO y Modelo Financiero del Cumplimiento Normativo
## Caso de Aplicación: Transportes Curimón S.A. (Caso 10) · Empresa Consultora AudIT

**Autor:** Persona 4 (*Compliance Cost Modeler & Financial Impact Analyst*)  
**Paridades Contractuales Oficiales E-24:** 1 UF = $40.000 CLP · 1 USD = $900 CLP · 1 EUR = $1.000 CLP · 1 UTM = $70.000 CLP · Tasa Descuento: 0,9% mensual (11,351% EA)

---

### 5.1 Enfoque Metodológico de Ingeniería Económica y Delimitación del Caso
El dimensionamiento financiero del cumplimiento normativo para **Transportes Curimón S.A.** traduce las exigencias de la **Ley N° 21.719** (Protección de Datos Personales, que reforma sustantivamente la Ley N° 19.628), la **Ley N° 21.663** (Marco de Ciberseguridad), la doctrina vinculante de la Dirección del Trabajo y la norma **ISO/IEC 27001:2022** en un presupuesto riguroso de Costo Total de Propiedad (*Total Cost of Ownership* - TCO).

El modelo abarca el ciclo contractual íntegro de **56 meses** estipulado en las Bases Técnicas (`FEP03.10`, Art. 17), estructurado en **Etapa 1 de Implementación** (Meses 1-12), **Etapa 2 de Pruebas y Certificación** (Meses 13-20) y **Etapa 3 de Operación Continua** (Meses 21-56, equivalente a 36 meses de operación en régimen). Toda formulación cuantitativa se gobierna bajo la volumetría inmutable del caso: **374 camiones** (340 con GPS previo en 3 plataformas dispares y 34 subcontratados integrados mediante app móvil), **454 conductores** (196 de planta protegidos por Dictámenes DT Ord. N° 569/020 y Ord. N° 2328/130 que consagran el derecho a la desconexión del GPS fuera de jornada, y 258 externos subcontratados sujetos a consentimiento explícito en RT-16.30), **148 transportistas subcontratados** (62 pymes con DPA marco y 86 dueños-choferes con anexos simplificados), **84 clientes corporativos** (acceso telemático restringido RT-16.09 y notificación en <2h/<24h RT-11.18/19) y **~1.900 cruces anuales a Mendoza (Argentina)** con cláusulas SCC transfronterizas (RT-05.23). Todas las tarifas se sujetan a las bandas oficiales del **Formulario E-26** (`FEP01.26`, Art. 13.5), garantizando trazabilidad absoluta mediante auditoría humana directa sobre fuentes primarias oficiales y aranceles de mercado vigentes.

---

### 5.2 Matriz Sintética de Obligaciones Normativas y Valorización de Cumplimiento
La siguiente matriz condensa la traducción operativa de los requerimientos legales en actividades de ingeniería, asociando roles responsables E-26, plazos normativos, hitos operativos y costos de inversión (CAPEX) y operación (OPEX):

| ID | Mandato Normativo, Vigencia & Art. Exacto | Aplicación Fáctica al Caso Curimón S.A. | Solución Técnica AudIT y Rol E-26 | Plazo Normativo & Hito Operativo | Naturaleza & Costo (UF / CLP) |
| :---: | :--- | :--- | :--- | :--- | :---: |
| **OB-01** | **Ley N° 21.719 (inc. Art. 3° bis y sust. Arts. 12-13 Ley 19.628)**<br>*(DO 13/12/2024 · Vacatio 24m: rige 01/12/2026 · BCN: 16/09/2026)* | 258 choferes externos sin vínculo laboral requieren base de licitud explícita y revocable. | Módulo de Consentimiento Móvil (RT-17.01). Analista Diseñador (20h) + QA (15h) + DPO (5h). | Ex ante al inicio del tratamiento (Art. 12 Ley 19.628) / Hito: Mes 12 | **CAPEX: 45,0 UF**<br>($1.800.000 CLP) |
| **OB-02** | **Ley N° 21.719 (inc. Arts. 3° sexies y 14 bis Ley 19.628)**<br>*(DO 13/12/2024 · Vacatio 24m: rige 01/12/2026 · BCN: 16/09/2026)* | Cifrado mandatorio RT-11.10 de choferes externos, tarifas de 148 pymes y telemetría. | Cifrado a nivel de campo en BD PostgreSQL con Azure Key Vault (Chile Central). CISO (40h) + Arq. (20h). | Principio de seguridad desde el diseño y por defecto (Art. 14 bis) / Hito: Meses 6-12 | **CAPEX: 120,0 UF**<br>($4.800.000 CLP) |
| **OB-03** | **Ley N° 21.719 (inc. Art. 14 ter Ley 19.628)**<br>*(DO 13/12/2024 · Vacatio 24m: rige 01/12/2026 · BCN: 16/09/2026)* | Inventario de datos hoy dispersos en 4 Excel; trazabilidad de accesos clientes (RT-16.09). | RAT con revisiones semestrales en CISO Assistant Pro. DPO (15h/año: 15 UF E1, 10 UF E2, 45 UF E3 = 70 UF en 56m). | Actualización semestral permanente (Art. 14 ter) / Hito: Continuo (56 meses) | **OPEX: 70,0 UF**<br>($2.800.000 CLP) |
| **OB-04** | **Ley N° 21.719 (inc. Art. 15 ter Ley 19.628)**<br>*(DO 13/12/2024 · Vacatio 24m: rige 01/12/2026 · BCN: 16/09/2026)* | Monitoreo continuo GPS cada 30 segundos sobre flota íntegra de 374 unidades. | Evaluación de Impacto en Protección de Datos (EIPD / DPIA). Asesor Legal (30h) + DPO (10h). | Previo al tratamiento masivo y de alto riesgo (Art. 15 ter) / Hito: Mes 10 | **CAPEX: 80,0 UF**<br>($3.200.000 CLP) |
| **OB-05** | **Ley N° 21.719 (inc. Art. 48 Ley 19.628)**<br>*(DO 13/12/2024 · Vacatio 24m: rige 01/12/2026 · BCN: 16/09/2026)* | Obligación de DPO autónomo con reporte a Directorio y canal de atención de derechos ARCO. | Retainer DPO Fraccional amortizado (18 h/mes a 2,0 UF/h). Proxy Jefe de Proyecto E-26. | Vacatio legis 24 meses (Diciembre 2026, Art. 48) / Hito: Vigencia permanente 56 meses | **OPEX: 2.016,0 UF**<br>($80.640.000 CLP) |
| **OB-06** | **Ley N° 21.719 (sust. Arts. 25 y 26 Ley 19.628)**<br>*(DO 13/12/2024 · Vacatio 24m: rige 01/12/2026 · BCN: 16/09/2026)* | 148 transportistas subcontratados tratan datos de tracking y despacho sin acuerdos legales. | Estandarización y firma de contratos DPA marco y anexos chofer-dueño. Asesor Legal (47,5h). | Previo a la transferencia a encargados (Arts. 25 y 26) / Hito: Meses 3-8 | **CAPEX: 95,0 UF**<br>($3.800.000 CLP) |
| **OB-07** | **Ley N° 21.719 (inc. Arts. 26 bis a 26 quáter Ley 19.628)**<br>*(DO 13/12/2024 · Vacatio 24m: rige 01/12/2026 · BCN: 16/09/2026)* | ~1.900 viajes anuales a Mendoza configuran transferencia internacional transfronteriza. | Cláusulas Contractuales Tipo (SCC) Chile-Argentina (RT-05.23). Asesor Legal TIC (17,5h). | Previo a flujo transfronterizo (Arts. 26 bis a 26 quáter) / Hito: Mes 12 | **CAPEX: 35,0 UF**<br>($1.400.000 CLP) |
| **OB-08** | **Ley N° 21.663 Marco de Ciberseguridad, Arts. 5, 8, 9 y 25**<br>*(DO 08/04/2024 · Plenamente vigente · BCN: 16/09/2026)* | Flota 24/7/365 (RT-10.05). Deber de reporte perentorio al CSIRT Nacional en menos de 3 horas. | Retainer CISO 24/7 y mesa de triaje ante ciberincidentes (24 h/mes a 2,0 UF/h). CISO E-26. | Plazo perentorio < 3 horas notificación preliminar CSIRT (Art. 9 Ley 21.663 y D.S. N° 295/2024) / Hito: Guardia 24/7 | **OPEX: 2.688,0 UF**<br>($107.520.000 CLP) |
| **OB-09** | **ISO/IEC 27001:2022 (Cláusulas 4-10)**<br>*(Estándar vigente internacional / INN Chile · Verificación: 16/09/2026)* | Exigencia de licitación de certificar el SGSI para resiliencia de torre de control y nube. | Certificación externa Fases 1+2 (Mes 18) y 3 vigilancias anuales (Años 3-5). BSI / SGS Chile. | Exigencia contractual bases / Hito: Mes 18 (Certif.) y Años 3-5 (Vigilancia) | **CAPEX: 387,5 UF**<br>**OPEX: 337,5 UF** |
| **OB-10** | **Ley N° 21.719 (inc. Art. 49 Ley 19.628)**<br>*(DO 13/12/2024 · Vacatio 24m: rige 01/12/2026 · BCN: 16/09/2026)* | Blindaje patrimonial para mitigar multas de hasta 20.000 UTM ante fallas de seguridad. | 4 auditorías anuales del Modelo de Prevención de Infracciones. DPO (20h) + QA (20h) por ciclo. | Anual para conservar atenuante calificada de responsabilidad (Art. 49) / Hito: Meses 20, 32, 44 y 56 | **OPEX: 240,0 UF**<br>($9.600.000 CLP) |
| **OB-11** | **Ley N° 21.719 (inc. Art. 8° bis Ley 19.628)**<br>*(DO 13/12/2024 · Vacatio 24m: rige 01/12/2026 · BCN: 16/09/2026)* | Algoritmo telemático de fatiga en cabina con suspensión/bloqueo de despacho en ruta. | Protocolo de explicabilidad algorítmica y revisión humana de decisiones automatizadas. | Ex ante a producción / Hito: Mes 11 (Diseño) y operación continua | **OPEX: 0,00 UF marginal**<br>*(Absorbido en Retainer DPO OB-05)* |
| **OB-12** | **Ley N° 21.719 (mod. Arts. 2° g y 16 Ley 19.628)**<br>*(DO 13/12/2024 · Vacatio 24m: rige 01/12/2026 · BCN: 16/09/2026)* | Enrolamiento biométrico facial/dactilar de 454 choferes en app móvil y cabina. | Consentimiento explícito reforzado para biometría y alternativa no biométrica por credencial. | Previo al enrolamiento / Hito: Mes 8 | **CAPEX: 0,00 UF marginal**<br>*(Embebido en App Móvil OB-01)* |
| **OB-13** | **Bases Técnicas FEP02 (Cláusulas RT-11.18 y RT-11.19)**<br>*(Exigencia contractual directa · Vigencia desde adjudicación)* | Aviso contractual perentorio a 84 clientes corporativos ante incidentes críticos y brechas. | Protocolo de escalamiento multicanal (<2h incidentes críticos, <24h brechas de privacidad). | Contractual perentorio: <2h y <24h / Hito: Mes 12 y guardia continua | **OPEX: 0,00 UF marginal**<br>*(Absorbido en Guardia CISO OB-08)* |
| **SUB** | **SUBTOTAL MATRIZ** | **Suma Directa de Obligaciones Normativas Básicas** | **13 Obligaciones de Cumplimiento Técnico-Legal** | **56 Meses de Contrato** | **6.114,0 UF** ($244.560.000 CLP) |

---

### 5.3 Modelo Presupuestario TCO a 56 Meses y Flujo de Caja Consolidado
El presupuesto maestro consolidado asciende a **7.705,0 UF ($308.200.000 CLP)**, integrando al subtotal de la matriz los componentes de infraestructura transversal GRC, transferencia de riesgo y soporte continuo:

| Categoría de Costo | Partida Presupuestaria / Código TCO | Etapa 1 (M 1-12) | Etapa 2 (M 13-20) | Etapa 3 (M 21-56) | Total TCO (UF) | Total TCO (CLP) | % TCO |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **CAPEX (Inversión)** | C-01 a C-05: Ingeniería, Cifrado, EIPD, DPAs y Mendoza | 375,0 UF | 0,0 UF | 0,0 UF | **375,0 UF** | $15.000.000 | 4,87% |
| | C-06: Certificación Inicial ISO/IEC 27001:2022 (Fases 1+2) | 0,0 UF | 387,5 UF | 0,0 UF | **387,5 UF** | $15.500.000 | 5,03% |
| **SUBTOTAL CAPEX** | **Gastos de Capital de Implementación y Certificación** | **375,0 UF** | **387,5 UF** | **0,0 UF** | **762,5 UF** | **$30.500.000** | **9,90%** |
| **OPEX (Operación)** | O-01: Actualización Semestral RAT (Art. 14 ter) | 15,0 UF | 10,0 UF | 45,0 UF | **70,0 UF** | $2.800.000 | 0,91% |
| | O-02: Retainer Mensual DPO Fraccional E-26 (36 UF/mes) | 432,0 UF | 288,0 UF | 1.296,0 UF | **2.016,0 UF** | $80.640.000 | 26,16% |
| | O-03: Retainer CISO 24/7 y Reporte ANCI 3h (48 UF/mes) | 576,0 UF | 384,0 UF | 1.728,0 UF | **2.688,0 UF** | $107.520.000 | 34,89% |
| | O-04: Auditorías Anuales de Vigilancia ISO 27001 (BSI/SGS) | 0,0 UF | 0,0 UF | 337,5 UF | **337,5 UF** | $13.500.000 | 4,38% |
| | O-05: Modelo Prevención Infracciones Art. 49 (4 ciclos) | 0,0 UF | 60,0 UF | 180,0 UF | **240,0 UF** | $9.600.000 | 3,11% |
| | O-06: Suscripción SaaS GRC CISO Assistant Pro Cloud | 60,0 UF | 40,0 UF | 180,0 UF | **280,0 UF** | $11.200.000 | 3,63% |
| | O-07: Póliza Corporativa Cyber Insurance (Chubb Seguros) | 90,0 UF | 60,0 UF | 270,0 UF | **420,0 UF** | $16.800.000 | 5,45% |
| | O-08: Fondo de Reserva para Contingencias Legales | 50,0 UF | 30,0 UF | 90,0 UF | **170,0 UF** | $6.800.000 | 2,21% |
| | O-09: Soporte Operativo QA (516 UF), App (135 UF) y Legal (70 UF) | 12,0 UF | 148,0 UF | 561,0 UF | **721,0 UF** | $28.840.000 | 9,36% |
| **SUBTOTAL OPEX** | **Costos Recurrentes de Operación (56 Meses)** | **1.235,0 UF** | **1.020,0 UF** | **4.687,5 UF** | **6.942,5 UF** | **$277.700.000** | **90,10%** |
| **TOTAL TCO** | **Presupuesto Integral de Cumplimiento AudIT** | **1.610,0 UF** | **1.407,5 UF** | **4.687,5 UF** | **7.705,0 UF** | **$308.200.000** | **100,00%** |

*Puente de Conciliación:* $\text{Total TCO} = 6.114,0\text{ UF (Obligaciones Directas)} + [280,0\text{ (GRC)} + 420,0\text{ (Seguro)} + 170,0\text{ (Reserva)} + 721,0\text{ (Soporte QA/Legal)}] = \mathbf{7.705,0\text{ UF}}$. La inversión en cumplimiento representa un **3,6% del presupuesto global del proyecto licitado**, plenamente alineado con benchmarks de la industria logística.

| Flujo Desembolsos Calendario (A1-A5) | Año 1 (M 1-12) | Año 2 (M 13-24) | Año 3 (M 25-36) | Año 4 (M 37-48) | Año 5 (M 49-56 / 8m) | Total TCO (56M) | Total Moneda Local (CLP) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Inversión de Capital (CAPEX)** | 375,0 UF | 387,5 UF | 0,0 UF | 0,0 UF | 0,0 UF | **762,5 UF** | $30.500.000 CLP |
| **Gasto Operacional (OPEX)** | 1.235,0 UF | 1.540,83 UF | 1.562,50 UF | 1.562,50 UF | 1.041,67 UF | **6.942,5 UF** | $277.700.000 CLP |
| **Flujo Anual Total (UF)** | **1.610,0 UF** | **1.928,33 UF** | **1.562,50 UF** | **1.562,50 UF** | **1.041,67 UF** | **7.705,0 UF** | **$308.200.000 CLP** |
| **Flujo Anual Total (CLP)** | $64.400.000 | $77.133.333 | $62.500.000 | $62.500.000 | $41.666.667 | **$308.200.000** | **100,00%** |

*Evaluación Financiera y Valor Esperado (Flujo de Desembolso Puro):* Al ser un flujo puro de egresos donde las multas evitadas no son ingresos de caja reinvertibles, la TIR no es matemáticamente aplicable al flujo aislado. Actualizando los desembolsos calendario a la tasa contractual de licitación $i = 0,9\%$ mensual ($r = 11,351\%$ anual efectivo E-24), el Valor Actual Neto del costo es $\text{VAN}_{\text{costo}} = \mathbf{5.757,68\text{ UF}}$ ($230.307.200 CLP). Frente a una exposición punitiva multicuerpo de 55.000,00 UF ($2.200.000.000 CLP), el umbral de indiferencia es $p^* = 7.705,0 / 55.000,0 = \mathbf{14,01\%\text{ a 56 meses}} \implies \mathbf{2,80\%\text{ anual calendario}}$ ($\mathbf{2,09\%\text{ anual}}$ sobre $\text{VAN}_{\text{costo}}$). Superada esa probabilidad mínima, el valor esperado del daño excede el TCO total, blindando el VAN global del proyecto.

---

### 5.4 Matriz Consolidada de Tarifas, Metadatos Arancelarios y Benchmark Salarial
En estricto cumplimiento del Formulario E-26 (`FEP01.26`, Art. 13.5) y cotizaciones de mercado vigentes (Chile 2025/2026), se unifican las tarifas de perfiles profesionales y las cotizaciones externas de software, certificación y seguros:

| Perfil / Insumo Técnico | Clasificación / Proveedor | Banda E-26 / Tarifa Base | Tarifa Homologada | Captura / Respaldo Oficial | Justificación Técnica y Régimen Contractual |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **Oficial de Seguridad (CISO)** | Encargado Seg. TI (E-26 L2479) | 1,5 – 2,5 UF/h | **2,00 UF/h** ($80.000) | 16/09/2026 · Chile · Robert Half | Dirección guardia pasiva 24/7 y reporte ANCI < 3h (Ley 21.663, Art. 9 y D.S. N° 295/2024). Margen 42,8%. |
| **Delegado de Privacidad (DPO)** | Jefe de Proyecto Proxy (L2467) | 1,5 – 3,0 UF/h | **2,00 UF/h** ($80.000) | 16/09/2026 · Chile · Michael Page | Autonomía técnica y reporte a Directorio (Art. 48 Ley 21.719). Margen 39,5%. |
| **Analista QA y Cumplimiento** | Analista QA Experto (L2484) | 0,8 – 1,0 UF/h | **1,00 UF/h** ($40.000) | 16/09/2026 · Chile · Hays IT | Control de evidencias documentales, logs y auditorías Art. 49. Margen 37,1%. |
| **Asesor Legal Externo TIC** | Perfil Especializado (L2488) | 2,0 – 4,0 UF/h | **2,00 UF/h** ($80.000) | 16/09/2026 · Chile · Col. Abogados | Redacción 148 DPAs, EIPD y cláusulas transfronterizas Mendoza. Margen 38,0%. |
| **CISO Assistant Pro Cloud** | Norad Security (SaaS Cloud GRC)| EUR 2.400/año (60,0 UF/a) | **60,00 UF/año** (5,00 UF/m) | 16/09/2026 · ciso-assistant.com | Reemplazo eficiente de OneTrust (ahorro 1.075 UF). Módulos RAT, ISO 27001 y ANCI. |
| **Certificación ISO 27001** | BSI Group / SGS Chile | $15.500.000 / $4.500.000 | **387,5 UF** / **112,5 UF/a** | 28/08/2026 · Chile · bsigroup.com | Certificación inicial Fases 1+2 Mes 18 (14 días-auditor según directriz IAF MD 5) y 3 vigilancias anuales. |
| **Póliza Cyber Insurance** | Chubb Seguros Chile S.A. | Prima anual corporativa | **90,00 UF/año** (7,5 UF/m) | 16/09/2026 · Chile · chubb.com | Cobertura agregada 50.000 UF (ransomware, forense DFIR y multas regulatorias). |
| **Azure Key Vault** | Microsoft Azure Inc. | Tier Estándar HSM Cloud | **0,00 UF/mes** (Marginal) | 16/09/2026 · Azure Chile Central | Región: Chile Central. 100% absorbido en créditos y tiers CSP provistos por P5. |

*Nota de Arquitectura y Regularización:* CISO Assistant Pro Cloud (EUR 2.400/año = 60,0 UF/año) reduce en 1.075 UF el sobrecosto de suites cerradas, garantizando interoperabilidad con Persona 3. Azure Key Vault opera en la región Azure Chile Central sin costo marginal para cumplimiento (0,00 UF), coordinado 1:1 con la arquitectura cloud de Persona 5 mediante Envelope Encryption (KEK maestra protegida y DEKs locales), descartando el sobrecosto prescindible de un clúster dedicado Managed HSM (52,56 UF/mes = 2.680,6 UF a 51 meses).

---

### 5.5 Sensibilidad Bidimensional, RoSI y Absorción del Riesgo Sancionatorio
Para evaluar la estabilidad financiera ante fluctuaciones del mercado, se modeló una matriz de sensibilidad bidimensional combinando la tarifa y dedicación del **DPO ($V_1$, $\pm 20\%$)** y el licenciamiento de la **Plataforma GRC ($V_2$, $\pm 25\%$)**:

| Escenario de Sensibilidad | DPO Retainer ($V_1$) | Plataforma SaaS GRC ($V_2$) | TCO Final (UF) | TCO Final (CLP) | Variación vs Base |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Escenario Optimista (-20% / -25%)** | 1.612,80 UF (DPO 1,60 UF/h) | 210,00 UF (GRC con desc. multianual) | **7.231,80 UF** | $289.272.000 CLP | **$-6,14\%$** ($-473,20$ UF) |
| **Escenario Base (Línea Central)** | **2.016,00 UF (DPO 2,00 UF/h)** | **280,00 UF (CISO Assistant Pro)** | **7.705,00 UF** | **$308.200.000 CLP** | **Baseline (0,00%)** |
| **Escenario Pesimista (+20% / +25%)** | 2.419,20 UF (DPO 2,40 UF/h) | 350,00 UF (GRC con módulos extra) | **8.178,20 UF** | $327.128.000 CLP | **$+6,14\%$** ($+473,20$ UF) |

La variación máxima simétrica de **$\pm 6,14\%$** confirma que las partidas base invariables (5.409,00 UF, 70,20% del TCO) blindan contractualmente a Curimón S.A. Asimismo, los cuadrantes asimétricos cruzados confirman la estabilidad del modelo: el Escenario Asimétrico A (DPO +20% / GRC -25%) resulta en un TCO de 8.038,20 UF (+4,32%), mientras que el Escenario Asimétrico B (DPO -20% / GRC +25%) sitúa el TCO en 7.371,80 UF (-4,32%), demostrando que las variaciones inversas se amortiguan mutuamente sin amenazar la viabilidad económica.

#### Modelado del Retorno sobre la Inversión en Seguridad (RoSI) y Regla de Gordon-Loeb
Bajo el marco normativo chileno, una contingencia severa en Curimón S.A. expone a la empresa a: **Multa Gravísima Ley N° 21.719 (Art. 46)** de hasta 20.000 UTM ($35.000,00\text{ UF}$ = \$1.400.000.000 CLP) y **Sanción ANCI Ley N° 21.663 (Título VII)** de hasta 10.000 UTM ($17.500,00\text{ UF}$), mitigables hasta un 70% mediante la atenuante del Art. 49.

Aplicando la formulación estandarizada de ingeniería económica:
$$\text{RoSI}_1 = \frac{(35.000,00\text{ UF} \times 0,85) - 7.705,00\text{ UF}}{7.705,00\text{ UF}} \times 100\% = \frac{29.750,00 - 7.705,00}{7.705,00} \times 100\% = \mathbf{286,11\%}\quad(\mathbf{416,70\%}\text{ sobre }\text{VAN}_{\text{costo}})$$

En un escenario de contingencia integral multicuerpo (datos, ciberseguridad y costos forenses por 55.000,00 UF = \$2.200M CLP mitigados al 90%), el retorno alcanza $\mathbf{RoSI}_2 = \mathbf{542,44\%}$ ($\mathbf{759,72\%}$ sobre $\text{VAN}_{\text{costo}}$).

De acuerdo con el modelo económico de **Gordon y Loeb (2002)**, la inversión óptima en ciberseguridad se acota a un techo del $37\%$ de la pérdida esperada:
$$\text{Presupuesto Óptimo} \le 0,37 \times \text{Pérdida Esperada} = 0,37 \times 55.000,00\text{ UF} = \mathbf{20.350,00\text{ UF}}$$
El costo total del programa AudIT (**7.705,0 UF**) representa solo el **$14,01\%$ de la exposición patrimonial agregada** y apenas el **$22,01\%$ del valor de una sola multa gravísima máxima ($35.000\text{ UF}$)**, situándose holgadamente bajo la cota de sobreinversión. Con una probabilidad de indiferencia de solo **2,80% anual** ($2,09\%$ anual sobre $\text{VAN}_{\text{costo}}$) frente al riesgo multicuerpo, el programa de cumplimiento de AudIT constituye una decisión de alta racionalidad financiera y blindaje patrimonial para Transportes Curimón S.A.
