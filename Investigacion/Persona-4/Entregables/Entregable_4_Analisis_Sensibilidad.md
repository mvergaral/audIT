# Entregable 4: Análisis de Sensibilidad Bidimensional y Modelado RoSI
## Evaluación de Riesgo Financiero, Retorno de la Inversión en Seguridad y Absorción Sancionatoria

**Asignatura:** Taller de Formulación de Proyectos Informáticos (ICI-5444) · Escuela de Informática, PUCV  
**Empresa Consultora:** AudIT (Empresa 10)  
**Tema de Investigación:** TI-12 · *Cumplimiento normativo en proyectos TIC: Ley 21.719, Ley 21.663 (ANCI) y marco internacional*  
**Proyecto de Aplicación:** Caso 10 — *Transportes Curimón S.A.* (Código `FEP03.10`)  
**Rol Responsable:** Persona 4 (*Compliance Cost Modeler & Financial Impact Analyst*)  
**Estado:** Versión Definitiva 1.0 — Auditada y con Verificación Matemática en KaTeX  
**Paridades Oficiales Inmutables de Conversión (Septiembre 2026):**  
* **1 UF = $40.942,74 CLP** (Comisión para el Mercado Financiero / Servicio de Impuestos Internos)  
* **1 USD = $954,28 CLP** (Banco Central de Chile, Dólar Observado)  
* **1 UTM = $71.721 CLP** (Servicio de Impuestos Internos)  

---

## 1. Presentación y Fundamento Metodológico

El presente documento expone la evaluación de riesgo cuantitativo del presupuesto de cumplimiento normativo para **Transportes Curimón S.A.** ante variaciones de mercado e incertidumbres operacionales durante el horizonte contractual de **56 meses**. 

Para garantizar la estabilidad del flujo de caja corporativo y blindar las decisiones de inversión, este estudio aborda dos análisis complementarios:
1. **Análisis de Sensibilidad Bidimensional ($3 \times 3$):** Evalúa el impacto simultáneo sobre el TCO consolidado al someter a estrés las dos partidas de mayor peso e incertidumbre: el servicio profesional del **Delegado de Protección de Datos ($V_1$, DPO Retainer)** y el licenciamiento de la **Plataforma de Gobernanza, Riesgo y Cumplimiento ($V_2$, SaaS GRC)**.
2. **Modelado de Retorno sobre la Inversión en Seguridad (*Return on Security Investment* - RoSI):** Cuantifica la rentabilidad económica de implementar el programa de cumplimiento integral de AudIT frente a la exposición al régimen sancionatorio de la **Ley N° 21.719** (hasta 20.000 UTM), la **Ley N° 21.663** (hasta 10.000 UTM) y el valor atenuante del **Modelo de Prevención de Infracciones (Art. 49)**.

---

## 2. Definición de Variables y Rangos de Incertidumbre

De acuerdo con la estructura del presupuesto maestro de 8.765,0 UF, el costo consolidado se descompone en partidas fijas parametrizadas y dos variables críticas:

$$\text{TCO Total} = \text{Partidas Base Invariables} + V_1 + V_2$$

Donde:
* **Partidas Base Invariables:** Corresponden a los 755,0 UF de CAPEX directo (Módulo de Consentimiento 45 UF, Cifrado RT-11.10 120 UF, EIPD 80 UF, DPAs 95 UF, Mendoza 35 UF, Certificación Inicial ISO 27001 Mes 18 380 UF) más las partidas operacionales fijadas por contrato (CISO 2.688 UF, Vigilancia ISO 330 UF, Modelo Art. 49 240 UF, Ciberseguro 420 UF, Fondo de Reserva 170 UF, RAT 70 UF y Soporte QA/Legal 721 UF):
  $$\text{Partidas Base Invariables} = 8.765,0 - 2.016,0 - 1.355,0 = \mathbf{5.394,0\text{ UF}}\quad(220.845.139\text{ CLP})$$
* **Variable 1 ($V_1$ — DPO Retainer a 56 Meses):**
  * *Escenario Base:* Retainer mensual amortizado de 36,0 UF/mes (18 h/mes $\times$ 2,0 UF/h). Total = **2.016,0 UF** ($82.540.564 CLP).
  * *Variación Baja ($-20\%$):* Reducción de $-20\%$ sobre la tarifa base de 2,00 UF/h (tarifa horaria efectiva de 1,60 UF/h). Total = $2.016,0 \times 0,80 = \mathbf{1.612,80\text{ UF (DPO 1,60 UF/h)}}$ ($66.032.451 CLP).
  * *Variación Alta ($+20\%$):* Mayor conflictividad de privacidad con conductores externos o incremento tarifario (+20%, tarifa efectiva 2,40 UF/h). Total = $2.016,0 \times 1,20 = \mathbf{2.419,20\text{ UF (DPO 2,40 UF/h)}}$ ($99.048.677 CLP).
* **Variable 2 ($V_2$ — Suscripción Plataforma SaaS GRC a 56 Meses):**
  * *Escenario Base:* OneTrust Privacy Automation Cloud paquetizado corporativo por 56 meses. Total = **1.355,00 UF** ($55.477.413 CLP).
  * *Variación Baja ($-25\%$):* Adopción de plataforma GRC en tier Pyme (*Vanta Trust Platform* cotizada a USD 11.500/año). Total = $1.355,0 \times 0,75 = \mathbf{1.016,25\text{ UF}}$ ($41.608.060 CLP).
  * *Variación Alta ($+25\%$):* Expansión modular enterprise para auditoría continua de telemetría y geocercas complejas. Total = $1.355,0 \times 1,25 = \mathbf{1.693,75\text{ UF}}$ ($69.346.766 CLP).

---

## 3. Matriz Bidimensional de 9 Escenarios de Sensibilidad

La siguiente tabla presenta la combinación exhaustiva de las 9 posibilidades resultantes, calculando para cada celda el TCO consolidado en UF y CLP, junto con la desviación porcentual frente a la línea base:

| Identificador de Escenario | Condición $V_1$ (DPO Retainer) | Condición $V_2$ (Plataforma GRC) | TCO Total (UF) | TCO Total (CLP) | Variación Absoluta vs Base (UF) | Variación Porcentual (%) | Categorización de Riesgo |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| **ESC-01** | **Bajo (-20%):** 1.612,80 UF (DPO 1,60 UF/h) | **Bajo (-25%):** 1.016,25 UF | **8.023,05 UF** | $328.485.674 | $-741,95$ UF | **$-8,46\%$** | Ultra-Optimista |
| **ESC-02** | **Bajo (-20%):** 1.612,80 UF (DPO 1,60 UF/h) | **Base (0%):** 1.355,00 UF | **8.361,80 UF** | $342.355.003 | $-403,20$ UF | **$-4,60\%$** | Favorable Moderado |
| **ESC-03** | **Bajo (-20%):** 1.612,80 UF (DPO 1,60 UF/h) | **Alto (+25%):** 1.693,75 UF | **8.700,55 UF** | $356.224.333 | $-64,45$ UF | **$-0,74\%$** | Compensado Bajo |
| **ESC-04** | **Base (0%):** 2.016,00 UF (DPO 2,00 UF/h) | **Bajo (-25%):** 1.016,25 UF | **8.426,25 UF** | $345.000.787 | $-338,75$ UF | **$-3,86\%$** | Tecnológico Ágil |
| **ESC-05** | **Base (0%):** 2.016,00 UF (DPO 2,00 UF/h) | **Base (0%):** 1.355,00 UF | **8.765,00 UF** | **$358.863.116** | **0,00 UF** | **Baseline (0,00%)** | **LÍNEA BASE AUDIT** |
| **ESC-06** | **Base (0%):** 2.016,00 UF (DPO 2,00 UF/h) | **Alto (+25%):** 1.693,75 UF | **9.103,75 UF** | $372.725.446 | $+338,75$ UF | **$+3,86\%$** | Expansión Cloud |
| **ESC-07** | **Alto (+20%):** 2.419,20 UF (DPO 2,40 UF/h) | **Bajo (-25%):** 1.016,25 UF | **8.829,45 UF** | $361.501.899 | $+64,45$ UF | **$+0,74\%$** | Compensado Alto |
| **ESC-08** | **Alto (+20%):** 2.419,20 UF (DPO 2,40 UF/h) | **Base (0%):** 1.355,00 UF | **9.168,20 UF** | $375.371.229 | $+403,20$ UF | **$+4,60\%$** | Sobrecarga Legal |
| **ESC-09** | **Alto (+20%):** 2.419,20 UF (DPO 2,40 UF/h) | **Alto (+25%):** 1.693,75 UF | **9.506,95 UF** | $389.241.558 | $+741,95$ UF | **$+8,46\%$** | Ultra-Pesimista |

### Grilla Matricial de Sensibilidad (TCO en UF)

$$\begin{array}{c|ccc}
\text{DPO } (V_1) \;\backslash\; \text{GRC } (V_2) & \text{Bajo } (-25\%) & \text{Base } (0\%) & \text{Alto } (+25\%) \\
\hline
\text{Bajo } (-20\%) & 8.023,05\text{ UF} & 8.361,80\text{ UF} & 8.700,55\text{ UF} \\
\text{Base } (0\%) & 8.426,25\text{ UF} & \mathbf{8.765,00\text{ UF}} & 9.103,75\text{ UF} \\
\text{Alto } (+20\%) & 8.829,45\text{ UF} & 9.168,20\text{ UF} & 9.506,95\text{ UF}
\end{array}$$

### Conclusiones del Análisis de Sensibilidad:
1. **Simetría y Alta Estabilidad:** La oscilación presupuestaria máxima es estrictamente simétrica de **$\pm 8,46\%$** ($\pm 741,95$ UF $\approx \pm \$30,38$ millones CLP), fluctuando entre **8.023,05 UF y 9.506,95 UF**.
2. **Efecto Amortiguador de la Estructura Contractual:** Las partidas base invariables (5.394,0 UF) representan el **61,5% del TCO**, lo que garantiza que contingencias operacionales en honorarios o licencias no desestabilicen el balance financiero del proyecto licitado.
3. **Efecto de Compensación Cruzada (ESC-03 y ESC-07):** En escenarios mixtos donde una variable sube y la otra baja, la variación neta sobre el presupuesto global es inferior al **1,0%** ($\pm 64,45$ UF), confirmando la resiliencia del modelo económico de AudIT.

---

## 4. Cuantificación del Régimen Sancionatorio Aplicable

Para evaluar la pertinencia económica de la inversión en cumplimiento, es imperativo contrastar el costo TCO frente al marco punitivo vigente en Chile a septiembre de 2026:

### 4.1 Régimen Punitivo de la Ley N° 21.719 (Protección de Datos Personales)
La reforma a la Ley N° 19.628 introduce tres tramos sancionatorios pecuniarios expresados en Unidades Tributarias Mensuales (UTM), calculadas a la paridad oficial de **$1\text{ UTM} = \$71.721\text{ CLP}$** y **$1\text{ UF} = \$40.942,74\text{ CLP}$**:

1. **Infracciones Leves (Art. 44):** Multas de hasta **5.000 UTM**.
   $$\text{Multa Leve Máxima} = 5.000 \times 71.721\text{ CLP} = 358.605.000\text{ CLP} \equiv \mathbf{8.758,70\text{ UF}}$$
2. **Infracciones Graves (Art. 45):** Multas de hasta **10.000 UTM**.
   $$\text{Multa Grave Máxima} = 10.000 \times 71.721\text{ CLP} = 717.210.000\text{ CLP} \equiv \mathbf{17.517,42\text{ UF}}$$
3. **Infracciones Gravísimas (Art. 46):** Multas de hasta **20.000 UTM**.
   $$\text{Multa Gravísima Máxima} = 20.000 \times 71.721\text{ CLP} = 1.434.420.000\text{ CLP} \equiv \mathbf{35.034,84\text{ UF}}$$

### 4.2 Régimen Sancionatorio de la Ley N° 21.663 (Marco de Ciberseguridad / ANCI)
Para Operadores de Importancia Vital (OIV) y prestadores de servicios esenciales, el incumplimiento de la obligación de notificación de incidentes dentro de las 3 horas (Art. 14) o la inobservancia de medidas técnicas de seguridad faculta a la Agencia Nacional de Ciberseguridad (ANCI) a aplicar sanciones de hasta:
$$\text{Multa ANCI Máxima} = 10.000\text{ UTM} = 717.210.000\text{ CLP} \equiv \mathbf{17.517,42\text{ UF}}$$

### 4.3 La Atenuante Calificada del Artículo 49 (Modelo de Prevención de Infracciones)
El Artículo 49 de la Ley N° 19.628 reformada establece que la adopción eficaz y certificación de un **Modelo de Prevención de Infracciones** constituye una **circunstancia atenuante muy calificada** de responsabilidad administrativa:
* Permite a la Agencia de Protección de Datos **rebajar la cuantía de la sanción pecuniaria entre un 50% y un 70%**.
* En faltas no intencionales derivadas de errores técnicos fortuitos, faculta a sustituir la multa por una amonestación escrita condicionada a la ejecución de un plan de cumplimiento.
* **Impacto Económico Directo:** Sobre una multa gravísima de 20.000 UTM (35.034,84 UF), la atenuante del Art. 49 representa una **mitigación económica directa de entre 17.517,42 UF y 24.524,39 UF** (\$717M a \$1.004M CLP de ahorro patrimonial).

---

## 5. Modelado del Retorno sobre la Inversión en Seguridad (RoSI)

### 5.1 Formulación Matemática Estándar de Ingeniería de Ciberseguridad
El modelo RoSI evalúa cuantitativamente la conveniencia económica de una inversión defensiva, relacionando el riesgo monetario mitigado frente al costo total de propiedad:

$$\text{RoSI} = \frac{\Delta\text{ALE} - \text{Costo Solución (TCO)}}{\text{Costo Solución (TCO)}} \times 100\%$$

Donde:
* $\Delta\text{ALE}$ representa la reducción en la Pérdida Anualizada Esperada (*Annualized Loss Expectancy*):
  $$\Delta\text{ALE} = \text{ALE}_{\text{sin controles}} - \text{ALE}_{\text{con controles}} = (\text{Exposición de Riesgo Base} \times \text{ARO}) \times \text{Eficacia de Mitigación } (E_m)$$
* $\text{ARO}$ (*Annualized Rate of Occurrence*): Tasa anual estimada de fiscalizaciones o incidentes de fuga de datos en operaciones logísticas desreguladas ($\sim 0,35$ incidentes/año).
* $E_m$ (*Eficacia de Mitigación*): Porcentaje de absorción y reducción de probabilidad conferido por el SGSI ISO 27001, cifrado RT-11.10 y gobernanza OneTrust ($E_m \ge 85\%$).

### 5.2 Escenarios de Evaluación del RoSI a 56 Meses (Horizonte Completo)

Considerando la exposición de riesgo acumulada durante los 56 meses de contrato, el RoSI se evalúa tanto respecto al presupuesto nominal (**TCO = 8.765,00 UF**) como al valor actualizado intertemporal de los egresos (**$\text{VAN}_{\text{costo}} = 6.759,38\text{ UF}$ a $r = 10\%$**):

#### Escenario RoSI 1: Exposición Exclusiva a Multa Gravísima Ley 21.719 (20.000 UTM)
* Exposición Bruta por Sanción Máxima: $35.034,84\text{ UF}$ (\$1.434.420.000 CLP).
* Eficacia Combinada de Controles Técnicos y Modelo Art. 49 ($E_m$): $85\%$.
* Riesgo Mitigado ($\Delta\text{ALE}_{56M}$):
  $$\Delta\text{ALE}_{56M} = 35.034,84\text{ UF} \times 0,85 = \mathbf{29.779,61\text{ UF}}\quad(1.219.256.402\text{ CLP})$$
* Retorno sobre TCO Nominal (8.765,00 UF):
  $$\text{RoSI}_1(\text{TCO}) = \frac{29.779,61 - 8.765,00}{8.765,00} \times 100\% = \mathbf{239,76\%}$$
* Retorno sobre Costo Actualizado ($\text{VAN}_{\text{costo}} = 6.759,38\text{ UF}$):
  $$\text{RoSI}_1(\text{VAN}) = \frac{29.779,61 - 6.759,38}{6.759,38} \times 100\% = \mathbf{340,57\%}$$

#### Escenario RoSI 2: Exposición Integral Multicuerpo (Ley 21.719 + Ley 21.663 + Costos Forenses)
En una eventualidad de ransomware en la torre de control con secuestro de telemetría de 374 camiones y exposición no reportada al CSIRT:
* Sanción Gravísima Protección de Datos: 20.000 UTM ($35.034,84$ UF).
* Sanción Grave Ley Marco Ciberseguridad ANCI: 10.000 UTM ($17.517,42$ UF).
* Costos Operacionales de Remediación Forense DFIR y Notificación: $2.500,00$ UF.
* **Exposición Total de Riesgo Agregado:**
  $$\text{Riesgo Total} = 35.034,84 + 17.517,42 + 2.500,00 = \mathbf{55.052,26\text{ UF}}\quad(2.254.041.528\text{ CLP})$$
* Eficacia de Mitigación con ISO 27001 + Póliza Chubb + DPO/CISO Retainer ($E_m$): $90\%$.
* Riesgo Mitigado:
  $$\Delta\text{ALE}_{\text{Integral}} = 55.052,26\text{ UF} \times 0,90 = \mathbf{49.547,03\text{ UF}}\quad(2.028.588.647\text{ CLP})$$
* Retorno sobre TCO Nominal (8.765,00 UF):
  $$\text{RoSI}_2(\text{TCO}) = \frac{49.547,03 - 8.765,00}{8.765,00} \times 100\% = \mathbf{465,28\%}$$
* Retorno sobre Costo Actualizado ($\text{VAN}_{\text{costo}} = 6.759,38\text{ UF}$):
  $$\text{RoSI}_2(\text{VAN}) = \frac{49.547,03 - 6.759,38}{6.759,38} \times 100\% = \mathbf{633,01\%}$$

### 5.3 Análisis de Valor Esperado y Umbral de Indiferencia Probabilística ($p^*$)

> [!IMPORTANT]
> **Fundamentación Teórica de Inversión Defensiva (Sin Falacia TIR):**  
> Al no existir ingresos de caja generados por el cumplimiento legal, no corresponde aplicar la Tasa Interna de Retorno (TIR). La rentabilidad defensiva se fundamenta probabilísticamente mediante el **Valor Esperado del Daño ($E[\text{Pérdida}]$)**.

Frente a la exposición punitiva multicuerpo de **55.052,26 UF**, el valor esperado de la contingencia para una probabilidad acumulada $p$ durante los 56 meses se formaliza como:
$$E[\text{Pérdida Sin Cumplimiento}] = p \times 55.052,26\text{ UF}$$

El punto de equilibrio o **probabilidad de indiferencia ($p^*$)** donde el costo del programa iguala el daño esperado es:
$$p^* = \frac{\text{TCO Total}}{\text{Sanción Multicuerpo}} = \frac{8.765,00\text{ UF}}{55.052,26\text{ UF}} = \mathbf{15,92\%\text{ a 56 meses}} \implies \mathbf{3,18\%\text{ anual}}$$

Si la probabilidad anual de sufrir una fiscalización con sanción grave/gravísima supera apenas el **3,18% anual** (o **2,46% anual** considerando $\text{VAN}_{\text{costo}} = 6.759,38\text{ UF}$), la pérdida económica esperada excede íntegramente el presupuesto del proyecto, acreditando que la inversión de AudIT no es un gasto discrecional, sino un escudo financiero indispensable.

---

## 6. Cuadro Comparativo: Inversión en Cumplimiento vs. Techo de Multas

La siguiente tabla resume la relación costo-beneficio del proyecto para la Gerencia General de Transportes Curimón S.A.:

| Dimensión Financiera / Contingencia | Monto en Moneda Legal (CLP) | Monto en Unidades de Fomento (UF) | % de Equivalencia frente al TCO AudIT (8.765 UF) | Dictamen de Decisión Económica |
| :--- | :---: | :---: | :---: | :--- |
| **Inversión TCO Total AudIT (56 Meses)** | **$358.863.116 CLP** | **8.765,00 UF** | **100,0% (Base de Comparación)** | Inversión programada en 56 meses. |
| **Una Sola Multa Leve Ley 21.719 (5.000 UTM)** | $358.605.000 CLP | 8.758,70 UF | **99,9%** | Una sola falta leve equivale al presupuesto total. |
| **Una Sola Multa Grave Ley 21.719 (10.000 UTM)** | $717.210.000 CLP | 17.517,42 UF | **199,9%** | El costo de una multa duplica el presupuesto. |
| **Una Sola Multa Gravísima Ley 21.719 (20.000 UTM)**| **$1.434.420.000 CLP** | **35.034,84 UF** | **399,7%** | El TCO completo representa solo el 25% de la multa. |
| **Sanción Máxima ANCI Ley 21.663 (10.000 UTM)** | $717.210.000 CLP | 17.517,42 UF | **199,9%** | Supera ampliamente la inversión de cumplimiento. |
| **Exposición Consolidada Multicuerpo + DFIR** | $2.254.041.528 CLP | 55.052,26 UF | **628,1%** | Riesgo patrimonial devastador sin defensas. |

$$\text{Conclusión Clave: } \mathbf{\text{TCO Total (8.765,0 UF)}} = \mathbf{0,250} \times \mathbf{\text{Multa Gravísima Máxima (35.034,84 UF)}}$$

---

## 7. Dictamen Financiero Final

Desde la perspectiva de la teoría de decisiones financieras y gestión del riesgo operacional:
1. **Racionalidad Económica Indiscutible:** La implementación del modelo de cumplimiento propuesto por AudIT no genera un gasto suntuario, sino un mecanismo de **cobertura patrimonial activa** que exhibe un retorno proyectado de entre **239,8% y 465,3% (RoSI)**.
2. **Blindaje de Flujo de Caja:** La variación del TCO en la simulación bidimensional ($\pm 8,46\%$) demuestra que el presupuesto está sólidamente blindado contra fluctuaciones del mercado de software y honorarios profesionales.
3. **Aseguramiento Contractual:** Cumplir con las cláusulas técnicas RT-11.10 y certificar ISO 27001 en el Mes 18 permite a Curimón S.A. defender sus contratos corporativos con las 84 empresas clientes, evitando rescisiones indemnizatorias de alto impacto.

---

## 8. Bibliografía y Referencias de Respaldo

1. **Biblioteca del Congreso Nacional de Chile (BCN).** (2024). *Ley N° 21.719: Regula la protección y el tratamiento de los datos personales y crea la Agencia de Protección de Datos Personales*. Diario Oficial, 13 de diciembre de 2024.
2. **Biblioteca del Congreso Nacional de Chile (BCN).** (2024). *Ley N° 21.663: Ley Marco de Ciberseguridad e Infraestructura Crítica de la Información*. Diario Oficial, 8 de abril de 2024.
3. **Sonnenreich, W., Albanese, J., & Stout, B.** (2006). *Return on Security Investment (ROSI) - A Practical Quantitative Model*. Journal of Research and Practice in Information Technology, 38(1), 45-56.
4. **ENISA (European Union Agency for Cybersecurity).** (2022). *Cybersecurity and return on investment: Measuring the economic impact of security controls*. Atenas, Grecia.
5. **Comisión para el Mercado Financiero (CMF) & Servicio de Impuestos Internos (SII).** (2026). *Indicadores Económicos Oficiales: UF ($40.942,74 CLP), Dólar ($954,28 CLP) y UTM ($71.721 CLP) al 16 de septiembre de 2026*.
