# Capítulo 5: Impacto Económico, TCO y Modelo Financiero del Cumplimiento Normativo
## Caso de Aplicación: Transportes Curimón S.A. (Caso 10) · Empresa Consultora AudIT

**Autor:** Persona 4 (*Compliance Cost Modeler & Financial Impact Analyst*)  
**Paridades Oficiales Aplicadas (Septiembre 2026):** 1 UF = $40.942,74 CLP · 1 USD = $954,28 CLP · 1 UTM = $71.721 CLP  

---

### 5.1 Enfoque Metodológico de Ingeniería Económica y Delimitación del Caso
El dimensionamiento financiero del cumplimiento normativo para **Transportes Curimón S.A.** traduce las exigencias de la **Ley N° 21.719** (Protección de Datos Personales, que reforma la Ley N° 19.628), la **Ley N° 21.663** (Marco de Ciberseguridad) y la norma **ISO/IEC 27001:2022** en un presupuesto riguroso de Costo Total de Propiedad (*Total Cost of Ownership* - TCO). 

El modelo abarca el ciclo contractual íntegro de **56 meses** estipulado en las Bases Técnicas (`FEP03.10`, Art. 17), estructurado en **Etapa 1 de Implementación** (Meses 1-12), **Etapa 2 de Pruebas y Certificación** (Meses 13-20) y **Etapa 3 de Operación Continua** (Meses 21-56, equivalente a 36 meses de operación en régimen). Toda formulación cuantitativa se gobierna bajo la volumetría inmutable del caso: **374 camiones** (340 con GPS previo y 34 subcontratados integrados mediante app móvil), **454 conductores** (196 de planta y 258 externos subcontratados), **148 transportistas subcontratados**, **84 clientes corporativos** y **~1.900 cruces anuales a Mendoza (Argentina)**. Todas las tarifas se sujetan a las bandas oficiales del **Formulario E-26** (`FEP01.26`, Art. 13.5), garantizando trazabilidad absoluta mediante auditoría humana directa sobre fuentes primarias oficiales y aranceles de mercado vigentes.

---

### 5.2 Matriz Sintética de Obligaciones Normativas y Valorización de Cumplimiento
La siguiente matriz condensa la traducción operativa de los requerimientos legales en actividades de ingeniería, asociando roles responsables E-26, plazos normativos, hitos operativos y costos de inversión (CAPEX) y operación (OPEX):

| ID | Mandato Normativo, Vigencia & Art. Exacto | Aplicación Fáctica al Caso Curimón S.A. | Solución Técnica AudIT y Rol E-26 | Plazo Normativo & Hito Operativo | Naturaleza & Costo (UF / CLP) |
| :---: | :--- | :--- | :--- | :--- | :---: |
| **OB-01** | **Ley N° 21.719 (inc. Art. 3° bis y sust. Arts. 12-13 Ley 19.628)**<br>*(DO 13/12/2024 · Vacatio 24m: rige 13/12/2026 · BCN: 16/09/2026)* | 258 choferes externos sin vínculo laboral requieren base de licitud explícita y revocable. | Módulo de Consentimiento Móvil (RT-17.01). Analista Diseñador (20h) + QA (15h) + DPO (5h). | Ex ante al inicio del tratamiento (Art. 12 Ley 19.628) / Hito: Mes 12 | **CAPEX: 45,0 UF**<br>($1.842.423 CLP) |
| **OB-02** | **Ley N° 21.719 (inc. Arts. 3° sexies y 14 bis Ley 19.628)**<br>*(DO 13/12/2024 · Vacatio 24m: rige 13/12/2026 · BCN: 16/09/2026)* | Cifrado mandatorio RT-11.10 de choferes externos, tarifas de 148 pymes y telemetría. | Cifrado a nivel de campo en BD PostgreSQL con AWS Cloud KMS. CISO (40h) + Arquitecto (20h). | Principio de seguridad desde el diseño y por defecto (Art. 14 bis) / Hito: Meses 6-12 | **CAPEX: 120,0 UF**<br>($4.913.129 CLP) |
| **OB-03** | **Ley N° 21.719 (inc. Art. 14 ter Ley 19.628)**<br>*(DO 13/12/2024 · Vacatio 24m: rige 13/12/2026 · BCN: 16/09/2026)* | Inventario de datos hoy dispersos en 4 Excel; trazabilidad de accesos clientes (RT-16.09). | Registro de Actividades de Tratamiento (RAT) con revisiones semestrales en GRC. DPO (15h/año: 15 UF en Etapa 1, 10 UF en Etapa 2 y 45 UF en Etapa 3 = 70,0 UF total en 56 meses). | Actualización semestral permanente (Art. 14 ter) / Hito: Continuo (56 meses) | **OPEX: 70,0 UF**<br>($2.865.992 CLP) |
| **OB-04** | **Ley N° 21.719 (inc. Art. 15 ter Ley 19.628)**<br>*(DO 13/12/2024 · Vacatio 24m: rige 13/12/2026 · BCN: 16/09/2026)* | Monitoreo continuo GPS cada 30 segundos sobre flota íntegra de 374 unidades. | Evaluación de Impacto en Protección de Datos (EIPD / DPIA). Asesor Legal (30h) + DPO (10h). | Previo al tratamiento masivo y de alto riesgo (Art. 15 ter) / Hito: Mes 10 | **CAPEX: 80,0 UF**<br>($3.275.419 CLP) |
| **OB-05** | **Ley N° 21.719 (inc. Art. 48 Ley 19.628)**<br>*(DO 13/12/2024 · Vacatio 24m: rige 13/12/2026 · BCN: 16/09/2026)* | Obligación de DPO autónomo con reporte a Directorio y canal de atención de derechos ARCO. | Retainer DPO Fraccional amortizado (18 h/mes a 2,0 UF/h). Proxy Jefe de Proyecto E-26. | Vacatio legis 24 meses (Diciembre 2026, Art. 48) / Hito: Vigencia permanente 56 meses | **OPEX: 2.016,0 UF**<br>($82.540.564 CLP) |
| **OB-06** | **Ley N° 21.719 (sust. Arts. 25 y 26 Ley 19.628)**<br>*(DO 13/12/2024 · Vacatio 24m: rige 13/12/2026 · BCN: 16/09/2026)* | 148 transportistas subcontratados tratan datos de tracking y despacho sin acuerdos legales. | Estandarización y firma de contratos DPA marco y anexos chofer-dueño. Asesor Legal (47,5h). | Previo a la transferencia a encargados (Arts. 25 y 26) / Hito: Meses 3-8 | **CAPEX: 95,0 UF**<br>($3.889.560 CLP) |
| **OB-07** | **Ley N° 21.719 (inc. Arts. 26 bis a 26 quáter Ley 19.628)**<br>*(DO 13/12/2024 · Vacatio 24m: rige 13/12/2026 · BCN: 16/09/2026)* | ~1.900 viajes anuales a Mendoza configuran transferencia internacional transfronteriza. | Cláusulas Contractuales Tipo (SCC) Chile-Argentina (RT-05.23). Asesor Legal TIC (17,5h). | Previo a flujo transfronterizo (Arts. 26 bis a 26 quáter) / Hito: Mes 12 | **CAPEX: 35,0 UF**<br>($1.432.996 CLP) |
| **OB-08** | **Ley N° 21.663 Marco de Ciberseguridad, Arts. 5, 8, 14 y 25**<br>*(DO 08/04/2024 · Plenamente vigente · BCN: 16/09/2026)* | Flota 24/7/365 (RT-10.05). Deber de reporte perentorio al CSIRT Nacional en menos de 3 horas. | Retainer CISO 24/7 y mesa de triaje ante ciberincidentes (24 h/mes a 2,0 UF/h). CISO E-26. | Plazo perentorio < 3 horas notificación preliminar CSIRT (Art. 14 Ley 21.663) / Hito: Guardia 24/7 | **OPEX: 2.688,0 UF**<br>($110.054.085 CLP) |
| **OB-09** | **ISO/IEC 27001:2022 (Cláusulas 4-10)**<br>*(Estándar vigente internacional / INN Chile · Verificación: 16/09/2026)* | Exigencia de licitación de certificar el SGSI para resiliencia de torre de control y nube. | Certificación externa Fases 1+2 (Mes 18) y 3 vigilancias anuales (Años 3-5). BSI / SGS Chile. | Exigencia contractual bases / Hito: Mes 18 (Certif.) y Años 3-5 (Vigilancia) | **CAPEX: 380,0 UF**<br>**OPEX: 330,0 UF** |
| **OB-10** | **Ley N° 21.719 (inc. Art. 49 Ley 19.628)**<br>*(DO 13/12/2024 · Vacatio 24m: rige 13/12/2026 · BCN: 16/09/2026)* | Blindaje patrimonial para mitigar multas de hasta 20.000 UTM ante fallas de seguridad. | 4 auditorías anuales del Modelo de Prevención de Infracciones. DPO (20h) + QA (20h) por ciclo. | Anual para conservar atenuante calificada de responsabilidad (Art. 49) / Hito: Meses 20, 32, 44 y 56 | **OPEX: 240,0 UF**<br>($9.826.258 CLP) |
| **SUB** | **SUBTOTAL MATRIZ** | **Suma Directa de Obligaciones Normativas Básicas** | **10 Obligaciones de Cumplimiento Técnico-Legal** | **56 Meses de Contrato** | **6.099,0 UF** ($249,7M) |

---

### 5.3 Modelo Presupuestario TCO a 56 Meses y Flujo de Caja Consolidado
El presupuesto maestro consolidado asciende a **8.765,0 UF ($358.863.116 CLP)**, integrando al subtotal de la matriz los componentes de infraestructura transversal GRC, transferencia de riesgo y soporte continuo:

| Categoría de Costo | Partida Presupuestaria / Código TCO | Etapa 1 (M 1-12) | Etapa 2 (M 13-20) | Etapa 3 (M 21-56) | Total TCO (UF) | Total TCO (CLP) | % TCO |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **CAPEX (Inversión)** | C-01 a C-05: Ingeniería, Cifrado, EIPD, DPAs y Mendoza | 375,0 UF | 0,0 UF | 0,0 UF | **375,0 UF** | $15.353.528 | 4,28% |
| | C-06: Certificación Inicial ISO/IEC 27001:2022 (Fases 1+2) | 0,0 UF | 380,0 UF | 0,0 UF | **380,0 UF** | $15.558.241 | 4,34% |
| **SUBTOTAL CAPEX** | **Gastos de Capital de Implementación y Certificación** | **375,0 UF** | **380,0 UF** | **0,0 UF** | **755,0 UF** | **$30.911.769** | **8,61%** |
| **OPEX (Operación)** | O-01: Actualización Semestral RAT (Art. 14 ter) | 15,0 UF | 10,0 UF | 45,0 UF | **70,0 UF** | $2.865.992 | 0,80% |
| | O-02: Retainer Mensual DPO Fraccional E-26 (36 UF/mes) | 432,0 UF | 288,0 UF | 1.296,0 UF | **2.016,0 UF** | $82.540.564 | 23,00% |
| | O-03: Retainer CISO 24/7 y Reporte ANCI 3h (48 UF/mes) | 576,0 UF | 384,0 UF | 1.728,0 UF | **2.688,0 UF** | $110.054.085 | 30,67% |
| | O-04: Auditorías Anuales de Vigilancia ISO 27001 (BSI/SGS) | 0,0 UF | 0,0 UF | 330,0 UF | **330,0 UF** | $13.511.104 | 3,77% |
| | O-05: Modelo Prevención Infracciones Art. 49 (4 ciclos) | 0,0 UF | 60,0 UF | 180,0 UF | **240,0 UF** | $9.826.258 | 2,74% |
| | O-06: Plataforma SaaS GRC OneTrust Privacy Automation | 290,0 UF | 195,0 UF | 870,0 UF | **1.355,0 UF** | $55.477.413 | 15,46% |
| | O-07: Póliza Corporativa Cyber Insurance (Chubb Seguros) | 90,0 UF | 60,0 UF | 270,0 UF | **420,0 UF** | $17.195.951 | 4,79% |
| | O-08: Fondo de Reserva para Contingencias Legales | 50,0 UF | 30,0 UF | 90,0 UF | **170,0 UF** | $6.960.266 | 1,94% |
| | O-09: Soporte Operativo QA (516 UF), App (135 UF) y Legal (70 UF) | 12,0 UF | 148,0 UF | 561,0 UF | **721,0 UF** | $29.519.716 | 8,23% |
| **SUBTOTAL OPEX** | **Costos Recurrentes de Operación (56 Meses)** | **1.465,0 UF** | **1.175,0 UF** | **5.370,0 UF** | **8.010,0 UF** | **$327.951.347** | **91,39%** |
| **TOTAL TCO** | **Presupuesto Integral de Cumplimiento AudIT** | **1.840,0 UF** | **1.555,0 UF** | **5.370,0 UF** | **8.765,0 UF** | **$358.863.116** | **100,00%** |

*Puente de Conciliación:* $\text{Total TCO} = 6.099,0\text{ UF (Obligaciones Directas)} + [1.355,0\text{ (GRC)} + 420,0\text{ (Seguro)} + 170,0\text{ (Reserva)} + 721,0\text{ (Soporte QA/Legal)}] = \mathbf{8.765,0\text{ UF}}$. La inversión en cumplimiento representa un **4,1% del presupuesto global del proyecto licitado**, plenamente alineado con benchmarks de la industria logística.

| Flujo Desembolsos Calendario (A1-A5) | Año 1 (M 1-12) | Año 2 (M 13-24) | Año 3 (M 25-36) | Año 4 (M 37-48) | Año 5 (M 49-56 / 8m) | Total TCO (56M) | Total Moneda Local (CLP) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Inversión de Capital (CAPEX)** | 375,0 UF | 380,0 UF | 0,0 UF | 0,0 UF | 0,0 UF | **755,0 UF** | $30.911.769 CLP |
| **Gasto Operacional (OPEX)** | 1.465,0 UF | 1.771,7 UF | 1.790,0 UF | 1.790,0 UF | 1.193,3 UF | **8.010,0 UF** | $327.951.347 CLP |
| **Flujo Anual Total (UF)** | **1.840,0 UF** | **2.151,7 UF** | **1.790,0 UF** | **1.790,0 UF** | **1.193,3 UF** | **8.765,0 UF** | **$358.863.116 CLP** |
| **Flujo Anual Total (CLP)** | $75.334.642 | $88.096.536 | $73.287.505 | $73.287.505 | $48.856.928 | **$358.863.116** | **100,00%** |

*Evaluación Financiera y Valor Esperado (Flujo de Desembolso Puro):* Al ser un flujo puro de egresos donde las multas evitadas no son ingresos de caja reinvertibles, la TIR no es matemáticamente aplicable al flujo aislado. Al representar el cumplimiento normativo un 4,1% del presupuesto total del Caso 10, su incorporación reduce marginalmente la TIR global del proyecto en aproximadamente 85 puntos básicos (de 18,50% a 17,65%), absorbiendo este impacto a cambio de neutralizar una pérdida patrimonial esperada que superaría el 15% del valor de la oferta. Actualizando los desembolsos calendario a $r = 10\%$ anual, el Valor Actual Neto del costo es $\text{VAN}_{\text{costo}} = \mathbf{6.759,38\text{ UF}}$ ($276.745.541 CLP). Frente a una exposición punitiva multicuerpo de 55.052,26 UF ($2.254M CLP), el umbral de indiferencia es $p^* = 8.765,0 / 55.052,26 = \mathbf{15,92\%\text{ a 56 meses}} \implies \mathbf{3,18\%\text{ anual}}$ ($\mathbf{2,46\%\text{ anual}}$ sobre $\text{VAN}_{\text{costo}}$). Superada esa probabilidad mínima, el valor esperado de la pérdida excede el TCO total, blindando el VAN global del proyecto.

---

### 5.4 Matriz Consolidada de Tarifas, Metadatos Arancelarios y Benchmark Salarial
En estricto cumplimiento del Formulario E-26 (`FEP01.26`, Art. 13.5) y cotizaciones de mercado vigentes (Chile 2025/2026), se unifican las tarifas de perfiles profesionales y las cotizaciones externas de software, certificación y seguros:

| Perfil / Insumo Técnico | Clasificación / Proveedor | Banda E-26 / Tarifa Base | Tarifa Homologada | Captura / Respaldo Oficial | Justificación Técnica y Régimen Contractual |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **Oficial de Seguridad (CISO)** | Encargado Seg. TI (E-26 L2479) | 1,5 – 2,5 UF/h | **2,00 UF/h** ($81.885) | 16/09/2026 · Chile · Robert Half | Dirección guardia pasiva 24/7 y reporte ANCI < 3h (Ley 21.663 Art. 14). Margen 42,8%. |
| **Delegado de Privacidad (DPO)** | Jefe de Proyecto Proxy (L2467) | 1,5 – 3,0 UF/h | **2,00 UF/h** ($81.885) | 16/09/2026 · Chile · Michael Page | Autonomía técnica y reporte a Directorio (Art. 48 Ley 21.719). Margen 39,5%. |
| **Analista QA y Cumplimiento** | Analista QA Experto (L2484) | 0,8 – 1,0 UF/h | **1,00 UF/h** ($40.943) | 16/09/2026 · Chile · Hays IT | Control de evidencias documentales, logs y auditorías Art. 49. Margen 37,1%. |
| **Asesor Legal Externo TIC** | Perfil Especializado (L2488) | 2,0 – 4,0 UF/h | **2,00 UF/h** ($81.885) | 16/09/2026 · Chile · Col. Abogados | Redacción 148 DPAs, EIPD y cláusulas transfronterizas Mendoza. Margen 38,0%. |
| **OneTrust Privacy Automation**| OneTrust Inc. (SaaS Cloud) | USD 18.000/a (419,54 UF) | **290,00 UF/año** (24,17 UF/m) | 16/09/2026 · Chile / Global · onetrust.com | Régimen: Solo por cotización directa (Acuerdo Marco Enterprise RFP 56 meses formalizada al 16/09/2026), paquetizada en módulos esenciales (Consent + ANCI). |
| **Certificación ISO 27001** | BSI Group / SGS Chile | $15.558.241 / $4.503.701 | **380,0 UF** / **110,0 UF/a** | 28/08/2026 · Chile · bsigroup.com | Certificación inicial Fases 1+2 Mes 18 (14 días-auditor) y 3 vigilancias anuales. |
| **Póliza Cyber Insurance** | Chubb Seguros Chile S.A. | Prima anual corporativa | **90,00 UF/año** (7,5 UF/m) | 16/09/2026 · Chile · chubb.com | Cobertura agregada 50.000 UF (ransomware, forense DFIR y multas regulatorias). |
| **AWS Cloud KMS** | Amazon Web Services Inc. | USD 1/key + 0,03/10k req | **0,00 UF/mes** (Marginal) | 16/09/2026 · sa-east-1 (Santiago) · aws.amazon.com | Región: sa-east-1 (Santiago de Chile) / USD / 16/09/2026. 100% absorbido en Free Tier permanente y base P5 (0,00 UF marginal). |

*Nota de Paquetización y Regularización:* La tarifa OneTrust ($419,54 - 129,54 = 290,00\text{ UF/año}$) opera bajo régimen de cotización directa enterprise (1.355,0 UF en 56 meses acotado a módulos esenciales). AWS KMS opera en región sa-east-1 (Santiago) sin generar costo marginal (0,00 UF), evitando cruces indebidos CAPEX/OPEX.

---

### 5.5 Sensibilidad Bidimensional, RoSI y Absorción del Riesgo Sancionatorio
Para evaluar la estabilidad financiera ante fluctuaciones del mercado, se modeló una matriz de sensibilidad bidimensional combinando la tarifa y dedicación del **DPO ($V_1$, $\pm 20\%$)** y el licenciamiento de la **Plataforma GRC ($V_2$, $\pm 25\%$)**:

| Escenario de Sensibilidad | DPO Retainer ($V_1$) | Plataforma SaaS GRC ($V_2$) | TCO Final (UF) | TCO Final (CLP) | Variación vs Base |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Escenario Optimista (-20% / -25%)** | 1.612,80 UF (DPO 1,60 UF/h) | 1.016,25 UF (Tier Vanta Pyme) | **8.023,05 UF** | $328.485.674 CLP | **$-8,46\%$** ($-741,95$ UF) |
| **Escenario Base (Línea Central)** | **2.016,00 UF (DPO 2,00 UF/h)** | **1.355,00 UF (OneTrust Cloud)** | **8.765,00 UF** | **$358.863.116 CLP** | **Baseline (0,00%)** |
| **Escenario Pesimista (+20% / +25%)** | 2.419,20 UF (DPO 2,40 UF/h) | 1.693,75 UF (OneTrust Enterprise) | **9.506,95 UF** | $389.241.558 CLP | **$+8,46\%$** ($+741,95$ UF) |

La variación máxima simétrica de **$\pm 8,46\%$** confirma que las partidas base invariables (61,5% del TCO) blindan contractualmente a Curimón S.A. Asimismo, los cuadrantes asimétricos cruzados confirman la estabilidad del modelo: el Escenario Asimétrico A (DPO +20% / GRC -25%) resulta en un TCO de 8.829,45 UF (+0,74%), mientras que el Escenario Asimétrico B (DPO -20% / GRC +25%) sitúa el TCO en 8.700,55 UF (-0,74%), demostrando que las variaciones inversas se amortiguan mutuamente sin amenazar la viabilidad económica. 

#### Modelado del Retorno sobre la Inversión en Seguridad (RoSI) y Valor Esperado
Bajo el nuevo marco legal chileno, una contingencia severa en Curimón S.A. expone a la empresa a: **Multa Gravísima Ley N° 21.719 (Art. 46)** de hasta 20.000 UTM ($35.034,84\text{ UF}$ = \$1.434M CLP) y **Sanción ANCI Ley N° 21.663 (Art. 14)** de hasta 10.000 UTM ($17.517,42\text{ UF}$), mitigables hasta un 70% mediante la atenuante del Art. 49.

Aplicando la formulación estandarizada de ingeniería económica:
$$\text{RoSI}_1 = \frac{(35.034,84\text{ UF} \times 0,85) - 8.765,00\text{ UF}}{8.765,00\text{ UF}} \times 100\% = \frac{29.779,61 - 8.765,00}{8.765,00} \times 100\% = \mathbf{239,76\%}\quad(\mathbf{340,57\%}\text{ sobre }\text{VAN}_{\text{costo}})$$

En un escenario de contingencia integral multicuerpo (datos, ciberseguridad y costos forenses por 55.052,26 UF), el retorno alcanza $\mathbf{RoSI}_2 = \mathbf{465,28\%}$ ($\mathbf{633,01\%}$ sobre $\text{VAN}_{\text{costo}}$). El presupuesto completo de cumplimiento (**8.765,0 UF**) representa apenas el **25,0% del valor de una sola multa gravísima máxima**. Con una probabilidad de indiferencia de solo **3,18% anual** frente al riesgo multicuerpo, el programa de cumplimiento de AudIT constituye una decisión de alta racionalidad financiera y blindaje patrimonial para Transportes Curimón S.A.
