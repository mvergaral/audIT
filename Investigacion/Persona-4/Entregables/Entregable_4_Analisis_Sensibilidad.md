# Entregable 4: Análisis de Sensibilidad Bidimensional y Modelado RoSI
## Evaluación de Riesgo Financiero, Retorno de la Inversión en Seguridad y Absorción Sancionatoria

**Asignatura:** Taller de Formulación de Proyectos Informáticos (ICI-5444) · Escuela de Informática, PUCV  
**Empresa Consultora:** AudIT (Empresa 10)  
**Tema de Investigación:** TI-12 · *Cumplimiento normativo en proyectos TIC: Ley 21.719, Ley 21.663 (ANCI) y marco internacional*  
**Proyecto de Aplicación:** Caso 10 — *Transportes Curimón S.A.* (Código `FEP03.10`)  
**Rol Responsable:** Persona 4 (*Compliance Cost Modeler & Financial Impact Analyst*)  
**Estado:** Versión Definitiva 2.0 — Auditada y con Verificación Matemática en KaTeX  
**Paridades Contractuales Oficiales de Conversión (Formulario E-24 / Bases de Licitación FEP01.26):**  
* **1 UF = $40.000 CLP** (Fijo contractual de evaluación de la licitación)  
* **1 USD = $900 CLP** (Factor contractual de conversión: $0,0225\text{ UF/USD}$)  
* **1 EUR = $1.000 CLP** (Factor contractual de conversión: $0,0250\text{ UF/EUR}$)  
* **1 UTM = $70.000 CLP** (Referencia tributaria contractual: $1,75\text{ UF/UTM}$)  
* **Tasa de Descuento Contractual:** $i = 0,9\%\text{ mensual}$ ($11,351\%\text{ efectivo anual}$, Formulario E-24, crédito de consumo / evaluación financiera)  

---

## 1. Presentación y Fundamento Metodológico

El presente documento expone la evaluación de riesgo cuantitativo del presupuesto de cumplimiento normativo para **Transportes Curimón S.A.** ante variaciones de mercado e incertidumbres operacionales durante el horizonte contractual de **56 meses**. 

Para garantizar la estabilidad del flujo de caja corporativo y blindar las decisiones de inversión, este estudio aborda dos análisis complementarios:
1. **Análisis de Sensibilidad Bidimensional ($3 \times 3$):** Evalúa el impacto simultáneo sobre el TCO consolidado al someter a estrés las dos partidas de mayor variabilidad e incertidumbre: el servicio profesional del **Delegado de Protección de Datos ($V_1$, DPO Retainer)** y el licenciamiento de la **Plataforma de Gobernanza, Riesgo y Cumplimiento ($V_2$, SaaS GRC CISO Assistant Pro Cloud)**.
2. **Modelado de Retorno sobre la Inversión en Seguridad (*Return on Security Investment* - RoSI):** Cuantifica la rentabilidad económica de implementar el programa de cumplimiento integral de AudIT frente a la exposición al régimen sancionatorio de la **Ley N° 21.719** (hasta 20.000 UTM), la **Ley N° 21.663** (hasta 10.000 UTM) y el valor atenuante del **Modelo de Prevención de Infracciones (Art. 49)**.

---

## 2. Definición de Variables y Rangos de Incertidumbre

De acuerdo con la estructura del presupuesto maestro optimizado de **7.705,00 UF ($308.200.000 CLP)**, el costo consolidado se descompone en partidas fijas parametrizadas y dos variables críticas:

$$\text{TCO Total} = \text{Partidas Base Invariables} + V_1 + V_2$$

Donde:
* **Partidas Base Invariables:** Corresponden a los 762,50 UF de CAPEX directo (C-01 Consentimiento Móvil 45 UF, C-02 Cifrado Azure Key Vault 120 UF, C-03 EIPD 80 UF, C-04 DPAs 95 UF, C-05 Mendoza 35 UF, C-06 Certificación Inicial ISO 27001 Mes 18 387,50 UF) más las partidas operacionales fijadas por contrato (CISO 2.688 UF, Vigilancia ISO 337,50 UF, Modelo Art. 49 240 UF, Ciberseguro Chubb 420 UF, Fondo de Reserva 170 UF, RAT 70 UF y Soporte QA/Legal 721 UF):
  $$\text{Partidas Base Invariables} = 7.705,00 - 2.016,00 - 280,00 = \mathbf{5.409,00\text{ UF}}\quad(216.360.000\text{ CLP})$$
  *(Representan un sólido **70,20% del TCO Total**, lo que provee una alta inercia de estabilidad financiera al proyecto)*.
* **Variable 1 ($V_1$ — DPO Retainer a 56 Meses):**
  * *Escenario Base:* Retainer mensual amortizado de 36,00 UF/mes (18 h/mes $\times$ 2,00 UF/h). Total = **2.016,00 UF** ($80.640.000 CLP).
  * *Variación Baja ($-20\%$):* Reducción de $-20\%$ por economías de escala y automatización (tarifa efectiva de 1,60 UF/h o abono de 28,80 UF/mes). Total = $2.016,00 \times 0,80 = \mathbf{1.612,80\text{ UF}}$ ($64.512.000 CLP). Variación: $-403,20$ UF.
  * *Variación Alta ($+20\%$):* Mayor conflictividad de privacidad con conductores externos o incremento en horas de litigación (+20%, tarifa efectiva 2,40 UF/h o abono de 43,20 UF/mes). Total = $2.016,00 \times 1,20 = \mathbf{2.419,20\text{ UF}}$ ($96.768.000 CLP). Variación: $+403,20$ UF.
* **Variable 2 ($V_2$ — Suscripción Plataforma SaaS GRC CISO Assistant Pro Cloud a 56 Meses):**
  * *Escenario Base:* Suscripción corporativa cloud (€2.400/año = 60,00 UF/año base = 5,00 UF/mes). Total = **280,00 UF** ($11.200.000 CLP).
  * *Variación Baja ($-25\%$):* Descuento adicional por pago plurianual anticipado (-25%, 45,00 UF/año o 3,75 UF/mes). Total = $280,00 \times 0,75 = \mathbf{210,00\text{ UF}}$ ($8.400.000 CLP). Variación: $-70,00$ UF.
  * *Variación Alta ($+25\%$):* Expansión modular para telemetría avanzada y geocercas en tiempo real (+25%, 75,00 UF/año o 6,25 UF/mes). Total = $280,00 \times 1,25 = \mathbf{350,00\text{ UF}}$ ($14.000.000 CLP). Variación: $+70,00$ UF.

---

## 3. Matriz Bidimensional de 9 Escenarios de Sensibilidad

La siguiente tabla presenta la combinación exhaustiva de las 9 posibilidades resultantes, calculando para cada celda el TCO consolidado en UF y CLP, junto con la desviación porcentual frente a la línea base:

| Identificador de Escenario | Condición $V_1$ (DPO Retainer) | Condición $V_2$ (Plataforma GRC) | TCO Total (UF) | TCO Total (CLP) | Variación Absoluta vs Base (UF) | Variación Porcentual (%) | Categorización de Riesgo |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| **ESC-01** | **Bajo (-20%):** 1.612,80 UF (DPO 1,60 UF/h) | **Bajo (-25%):** 210,00 UF | **7.231,80 UF** | $289.272.000 | $-473,20$ UF | **$-6,14\%$** | Ultra-Optimista |
| **ESC-02** | **Bajo (-20%):** 1.612,80 UF (DPO 1,60 UF/h) | **Base (0%):** 280,00 UF | **7.301,80 UF** | $292.072.000 | $-403,20$ UF | **$-5,23\%$** | Favorable Moderado |
| **ESC-03** | **Bajo (-20%):** 1.612,80 UF (DPO 1,60 UF/h) | **Alto (+25%):** 350,00 UF | **7.371,80 UF** | $294.872.000 | $-333,20$ UF | **$-4,32\%$** | Asimétrico B (Compensado) |
| **ESC-04** | **Base (0%):** 2.016,00 UF (DPO 2,00 UF/h) | **Bajo (-25%):** 210,00 UF | **7.635,00 UF** | $305.400.000 | $-70,00$ UF | **$-0,91\%$** | Eficiencia SaaS |
| **ESC-05** | **Base (0%):** 2.016,00 UF (DPO 2,00 UF/h) | **Base (0%):** 280,00 UF | **7.705,00 UF** | **$308.200.000** | **0,00 UF** | **Baseline (0,00%)** | **LÍNEA BASE AUDIT** |
| **ESC-06** | **Base (0%):** 2.016,00 UF (DPO 2,00 UF/h) | **Alto (+25%):** 350,00 UF | **7.775,00 UF** | $311.000.000 | $+70,00$ UF | **$+0,91\%$** | Expansión Cloud |
| **ESC-07** | **Alto (+20%):** 2.419,20 UF (DPO 2,40 UF/h) | **Bajo (-25%):** 210,00 UF | **8.038,20 UF** | $321.528.000 | $+333,20$ UF | **$+4,32\%$** | Asimétrico A (Compensado) |
| **ESC-08** | **Alto (+20%):** 2.419,20 UF (DPO 2,40 UF/h) | **Base (0%):** 280,00 UF | **8.108,20 UF** | $324.328.000 | $+403,20$ UF | **$+5,23\%$** | Sobrecarga Legal |
| **ESC-09** | **Alto (+20%):** 2.419,20 UF (DPO 2,40 UF/h) | **Alto (+25%):** 350,00 UF | **8.178,20 UF** | $327.128.000 | $+473,20$ UF | **$+6,14\%$** | Ultra-Pesimista |

### Grilla Matricial de Sensibilidad (TCO en UF)

$$\begin{array}{c|ccc}
\text{DPO } (V_1) \;\backslash\; \text{GRC } (V_2) & \text{Bajo } (-25\%) & \text{Base } (0\%) & \text{Alto } (+25\%) \\
\hline
\text{Bajo } (-20\%) & 7.231,80\text{ UF} & 7.301,80\text{ UF} & 7.371,80\text{ UF} \\
\text{Base } (0\%) & 7.635,00\text{ UF} & \mathbf{7.705,00\text{ UF}} & 7.775,00\text{ UF} \\
\text{Alto } (+20\%) & 8.038,20\text{ UF} & 8.108,20\text{ UF} & 8.178,20\text{ UF}
\end{array}$$

### Conclusiones del Análisis de Sensibilidad:
1. **Simetría y Rango de Incertidumbre Muy Estrecho:** La oscilación presupuestaria máxima es estrictamente simétrica de **$\pm 6,14\%$** ($\pm 473,20$ UF $\approx \pm \$18,93$ millones CLP), fluctuando en una banda de entre **7.231,80 UF y 8.178,20 UF**. La sustitución eficiente de OneTrust por CISO Assistant Pro redujo la exposición a variabilidad desde $\pm 8,46\%$ a solo $\pm 6,14\%$.
2. **Elevada Resiliencia por Partidas Invariables:** Las partidas base invariables (5.409,00 UF) representan el **70,20% del TCO Total**, garantizando que cualquier fluctuación en licenciamiento o asesoría jurídica tenga un impacto acotado y manejable sobre las finanzas de Curimón S.A.
3. **Efecto de Compensación Cruzada (ESC-03 y ESC-07):** En los cuadrantes asimétricos cruzados, el efecto combinado amortigua los sobrecostos, limitando el desvío neto a un moderado $\pm 4,32\%$ ($\pm 333,20$ UF).

---

## 4. Cuantificación del Régimen Sancionatorio Aplicable

Para evaluar la pertinencia económica de la inversión en cumplimiento, es imperativo contrastar el costo TCO frente al marco punitivo vigente en Chile bajo las paridades contractuales del Formulario E-24 ($1\text{ UTM} = \$70.000\text{ CLP}$ y $1\text{ UF} = \$40.000\text{ CLP}$, factor: $1,75\text{ UF/UTM}$):

### 4.1 Régimen Punitivo de la Ley N° 21.719 (Protección de Datos Personales)
La reforma a la Ley N° 19.628 introduce tres tramos sancionatorios pecuniarios expresados en Unidades Tributarias Mensuales (UTM):

1. **Infracciones Leves (Art. 44):** Multas de hasta **5.000 UTM**.
   $$\text{Multa Leve Máxima} = 5.000 \times 1,75\text{ UF/UTM} = \mathbf{8.750,00\text{ UF}}\quad(350.000.000\text{ CLP})$$
2. **Infracciones Graves (Art. 45):** Multas de hasta **10.000 UTM**.
   $$\text{Multa Grave Máxima} = 10.000 \times 1,75\text{ UF/UTM} = \mathbf{17.500,00\text{ UF}}\quad(700.000.000\text{ CLP})$$
3. **Infracciones Gravísimas (Art. 46):** Multas de hasta **20.000 UTM**.
   $$\text{Multa Gravísima Máxima} = 20.000 \times 1,75\text{ UF/UTM} = \mathbf{35.000,00\text{ UF}}\quad(1.400.000.000\text{ CLP})$$

### 4.2 Régimen Sancionatorio de la Ley N° 21.663 (Marco de Ciberseguridad / ANCI)
Para Operadores de Importancia Vital (OIV) y prestadores de servicios esenciales, el incumplimiento de la obligación de notificación de incidentes dentro de las 3 horas (Art. 9 de la Ley N° 21.663 y D.S. N° 295/2024) o la inobservancia de medidas técnicas de seguridad faculta a la Agencia Nacional de Ciberseguridad (ANCI) a aplicar sanciones de hasta:
$$\text{Multa ANCI Máxima} = 10.000\text{ UTM} = 10.000 \times 1,75\text{ UF/UTM} = \mathbf{17.500,00\text{ UF}}\quad(700.000.000\text{ CLP})$$

### 4.3 La Atenuante Calificada del Artículo 49 (Modelo de Prevención de Infracciones)
El Artículo 49 de la Ley N° 19.628 reformada establece que la adopción eficaz y auditoría continua de un **Modelo de Prevención de Infracciones** constituye una **circunstancia atenuante muy calificada** de responsabilidad administrativa:
* Permite a la Agencia de Protección de Datos **rebajar la cuantía de la sanción pecuniaria entre un 50% y un 70%**.
* En faltas no intencionales derivadas de incidentes técnicos imprevistos, faculta a sustituir la multa por una amonestación escrita sujeta a un plan de subsanación.
* **Impacto Económico Directo:** Sobre una multa gravísima de 20.000 UTM (35.000,00 UF), la atenuante del Art. 49 representa una **mitigación económica directa de entre 17.500,00 UF y 24.500,00 UF** (\$700M a \$980M CLP de ahorro patrimonial neto).

---

## 5. Modelado del Retorno sobre la Inversión en Seguridad (RoSI)

### 5.1 Formulación Matemática Estándar de Ingeniería de Ciberseguridad
El modelo RoSI evalúa cuantitativamente la conveniencia económica de una inversión defensiva, relacionando el riesgo monetario mitigado frente al costo total de propiedad:

$$\text{RoSI} = \frac{\Delta\text{ALE} - \text{Costo Solución (TCO)}}{\text{Costo Solución (TCO)}} \times 100\%$$

Donde:
* $\Delta\text{ALE}$ representa la reducción en la Pérdida Anualizada Esperada (*Annualized Loss Expectancy*):
  $$\Delta\text{ALE} = \text{ALE}_{\text{sin controles}} - \text{ALE}_{\text{con controles}} = (\text{Exposición de Riesgo Base} \times \text{ARO}) \times \text{Eficacia de Mitigación } (E_m)$$
* $\text{ARO}$ (*Annualized Rate of Occurrence*): Tasa anual estimada de fiscalizaciones o incidentes de fuga de datos en flotas de transporte telemático ($\sim 0,35$ eventos/año).
* $E_m$ (*Eficacia de Mitigación*): Porcentaje de absorción y reducción de probabilidad conferido por la certificación ISO 27001, cifrado Azure RT-11.10 y gobernanza CISO Assistant ($E_m \ge 85\%$).

### 5.2 Escenarios de Evaluación del RoSI a 56 Meses (Horizonte Completo)

Considerando la exposición de riesgo acumulada durante los 56 meses de contrato, el RoSI se evalúa tanto respecto al presupuesto nominal (**TCO = 7.705,00 UF**) como al valor actualizado intertemporal de los desembolsos (**$\text{VAN}_{\text{costo}} = 5.757,68\text{ UF}$ a $r = 11,351\%$ anual**):

#### Escenario RoSI 1: Exposición Exclusiva a Multa Gravísima Ley 21.719 (20.000 UTM)
* Exposición Bruta por Sanción Máxima: $35.000,00\text{ UF}$ (\$1.400.000.000 CLP).
* Eficacia Combinada de Controles Técnicos y Modelo Art. 49 ($E_m$): $85\%$.
* Riesgo Mitigado ($\Delta\text{ALE}_{56M}$):
  $$\Delta\text{ALE}_{56M} = 35.000,00\text{ UF} \times 0,85 = \mathbf{29.750,00\text{ UF}}\quad(1.190.000.000\text{ CLP})$$
* Retorno sobre TCO Nominal (7.705,00 UF):
  $$\text{RoSI}_1(\text{TCO}) = \frac{29.750,00 - 7.705,00}{7.705,00} \times 100\% = \mathbf{286,11\%}$$
* Retorno sobre Costo Actualizado ($\text{VAN}_{\text{costo}} = 5.757,68\text{ UF}$):
  $$\text{RoSI}_1(\text{VAN}) = \frac{29.750,00 - 5.757,68}{5.757,68} \times 100\% = \mathbf{416,70\%}$$

#### Escenario RoSI 2: Exposición Integral Multicuerpo (Ley 21.719 + Ley 21.663 + Costos Forenses DFIR)
En una eventualidad de ciberincidente severo en la torre de control con secuestro de telemetría de 374 camiones y reporte deficiente al CSIRT:
* Sanción Gravísima Protección de Datos: 20.000 UTM ($35.000,00$ UF).
* Sanción Grave Ley Marco Ciberseguridad ANCI: 10.000 UTM ($17.500,00$ UF).
* Costos Operacionales de Remediación Forense DFIR y Peritajes: $2.500,00$ UF.
* **Exposición Total de Riesgo Agregado:**
  $$\text{Riesgo Total} = 35.000,00 + 17.500,00 + 2.500,00 = \mathbf{55.000,00\text{ UF}}\quad(2.200.000.000\text{ CLP})$$
* Eficacia de Mitigación con ISO 27001 + Póliza Chubb + DPO/CISO Retainer ($E_m$): $90\%$.
* Riesgo Mitigado:
  $$\Delta\text{ALE}_{\text{Integral}} = 55.000,00\text{ UF} \times 0,90 = \mathbf{49.500,00\text{ UF}}\quad(1.980.000.000\text{ CLP})$$
* Retorno sobre TCO Nominal (7.705,00 UF):
  $$\text{RoSI}_2(\text{TCO}) = \frac{49.500,00 - 7.705,00}{7.705,00} \times 100\% = \mathbf{542,44\%}$$
* Retorno sobre Costo Actualizado ($\text{VAN}_{\text{costo}} = 5.757,68\text{ UF}$):
  $$\text{RoSI}_2(\text{VAN}) = \frac{49.500,00 - 5.757,68}{5.757,68} \times 100\% = \mathbf{759,72\%}$$

### 5.3 Análisis de Valor Esperado y Umbral de Indiferencia Probabilística ($p^*$)

> [!IMPORTANT]
> **Fundamentación Teórica de Inversión Defensiva (Sin Falacia TIR):**  
> Al tratarse de una estructura de desembolsos puros destinada a mitigar contingencias regulatorias y operacionales catastróficas, no corresponde calcular una Tasa Interna de Retorno (TIR). La justificación económica se sustenta en la teoría de decisiones bajo riesgo mediante el **Valor Esperado del Daño ($E[\text{Pérdida}]$)**.

Frente a la exposición punitiva multicuerpo de **55.000,00 UF ($2.200.000.000 CLP)**, el valor esperado de la contingencia para una probabilidad acumulada $p$ durante los 56 meses se define como:
$$E[\text{Pérdida Sin Cumplimiento}] = p \times 55.000,00\text{ UF}$$

El umbral o **probabilidad de indiferencia ($p^*$)** donde el costo total del TCO iguala al daño esperado es:
$$p^* = \frac{\text{TCO Total}}{\text{Sanción Multicuerpo}} = \frac{7.705,00\text{ UF}}{55.000,00\text{ UF}} = \mathbf{14,01\%\text{ acumulada a 56 meses}} \implies \mathbf{2,80\%\text{ anual calendario}}$$
$$(\text{o } 14,01\% / 4,6667\text{ años} = \mathbf{3,00\%\text{ anualizado sobre el horizonte real de 56 meses}})$$

Bajo la actualización intertemporal ($\text{VAN}_{\text{costo}} = 5.757,68\text{ UF}$), el umbral de indiferencia resulta aún menor:
$$p^*_{\text{VAN}} = \frac{5.757,68\text{ UF}}{55.000,00\text{ UF}} = \mathbf{10,47\%\text{ a 56 meses}} \implies \mathbf{2,09\%\text{ anual}}$$

Si la probabilidad anual de sufrir una fiscalización sancionatoria grave supera un exiguo **2,80% anual**, la pérdida económica esperada supera el 100% del presupuesto de cumplimiento, demostrando la alta conveniencia y rentabilidad defensiva del programa de AudIT.

---

## 6. Cuadro Comparativo: Inversión en Cumplimiento vs. Techo de Multas

La siguiente tabla resume la relación costo-beneficio del proyecto bajo las paridades fijas contractuales E-24:

| Dimensión Financiera / Contingencia | Monto en CLP ($40.000 CLP/UF) | Monto en UF | % de Equivalencia frente al TCO AudIT (7.705 UF) | Dictamen de Decisión Económica |
| :--- | :---: | :---: | :---: | :--- |
| **Inversión TCO Total AudIT (56 Meses)** | **$308.200.000 CLP** | **7.705,00 UF** | **100,0% (Base de Comparación)** | Inversión programada en 56 meses. |
| **Una Sola Multa Leve Ley 21.719 (5.000 UTM)** | $350.000.000 CLP | 8.750,00 UF | **113,6%** | Una sola falta leve ya supera el presupuesto total. |
| **Una Sola Multa Grave Ley 21.719 (10.000 UTM)** | $700.000.000 CLP | 17.500,00 UF | **227,1%** | El costo de una multa duplica el presupuesto. |
| **Una Sola Multa Gravísima Ley 21.719 (20.000 UTM)**| **$1.400.000.000 CLP** | **35.000,00 UF** | **454,3%** | El TCO completo representa solo el 22,01% de la multa. |
| **Sanción Máxima ANCI Ley 21.663 (10.000 UTM)** | $700.000.000 CLP | 17.500,00 UF | **227,1%** | Supera ampliamente la inversión en cumplimiento. |
| **Exposición Consolidada Multicuerpo + DFIR** | $2.200.000.000 CLP | 55.000,00 UF | **713,8%** | Riesgo patrimonial devastador sin defensas. |

$$\text{Conclusión Clave: } \mathbf{\text{TCO Total (7.705,00 UF)}} = \mathbf{0,2201} \times \mathbf{\text{Multa Gravísima Máxima (35.000,00 UF)}}$$

---

## 7. Dictamen Financiero Final

Desde la perspectiva de la ingeniería financiera y gestión del riesgo operacional:
1. **Racionalidad Económica Concluyente:** El plan de cumplimiento de AudIT exhibe un retorno defensivo proyectado de entre **286,1% y 542,4% (RoSI)**, garantizando que cada peso invertido en ciberseguridad y protección de datos ahorra entre 2,8 y 5,4 veces su valor en pérdidas patrimoniales directas.
2. **Estabilidad Presupuestaria:** La oscilación del TCO en la simulación bidimensional ($\pm 6,14\%$) acredita que el presupuesto está sólidamente protegido frente a contingencias tarifarias o tecnológicas.
3. **Blindaje de la Operación Comercial:** El aseguramiento técnico (RT-11.10) y la certificación ISO 27001 en el Mes 18 blindan los contratos logísticos con las 84 empresas clientes de Curimón S.A., evitando la pérdida de licitaciones y garantizando continuidad operacional continua (24/7/365).

---

## 8. Bibliografía y Referencias de Respaldo

1. **Escuela de Informática, PUCV.** (2026). *Bases Administrativas de la Licitación: Formulario E-24 (Paridades Contractuales y Evaluación Económica) y Formulario E-26 (Rango de Valores Aceptados para Perfiles Profesionales, Código FEP01.26, Arts. 9.3 y 13.5)*. Archivo: `FEP01_26_Bases_Administrativas_TFEP_01_2026_3.md`.
2. **Biblioteca del Congreso Nacional de Chile (BCN).** (2024). *Ley N° 21.719: Regula la protección y el tratamiento de los datos personales y crea la Agencia de Protección de Datos Personales*. Diario Oficial, 13 de diciembre de 2024.
3. **Biblioteca del Congreso Nacional de Chile (BCN).** (2024). *Ley N° 21.663: Ley Marco de Ciberseguridad e Infraestructura Crítica de la Información*. Diario Oficial, 8 de abril de 2024.
4. **Sonnenreich, W., Albanese, J., & Stout, B.** (2006). *Return on Security Investment (ROSI) - A Practical Quantitative Model*. Journal of Research and Practice in Information Technology, 38(1), 45-56.
5. **ENISA (European Union Agency for Cybersecurity).** (2022). *Cybersecurity and return on investment: Measuring the economic impact of security controls*. Atenas, Grecia.
6. **CISO Assistant / Norad Security.** (2026). *CISO Assistant Pro Cloud: GRC Metrics, SOC 2 Type II Certification and Commercial Cloud Pricing*.
