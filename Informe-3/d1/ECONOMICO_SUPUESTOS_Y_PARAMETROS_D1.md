# Paquete Económico y Financiero de Dupla 1 (Informe 3)

**Proyecto:** Licitación TFEP-01-2026 · Caso 10 · Transportes Curimón S.A.  
**Autoría:** Dupla 1 (Evaluación Financiera, Beneficios y Consolidación Documental).  
**Destinatarios:** Dupla 2 (Integración de Planilla, Flujo y Curva S), Dupla 3, Dupla 4 y Mesa de Coordinación.  
**Estado:** Formalizado y verificado conforme a Bases Administrativas (FEP01.26), Formularios E-21 a E-26, T-22 y Aclaraciones Oficiales del Art. 44.1.

---

## 1. Resumen Ejecutivo del Paquete D1

En cumplimiento del rol asignado a la Dupla 1 en la planificación del Informe 3 y en el proyecto oficial de Linear (`AudIT_Fep`), este documento consolida los cinco componentes financieros bajo la titularidad técnica de D1:

1. **Supuestos de Precio, Margen, Financiamiento, Garantías y Seguros (`AUD-5` / Tarea 1.1)**:
   * **Rentabilidad y Precios:** Rentabilidad objetivo del proyecto fijada en **18,5 % a 19,0 % EBITDA**, garantizando subordinación al tope legal del **20,0 % EBITDA** sobre ingresos netos normado en E-24 y aclarado oficialmente en Art. 44.1. Fórmula de precio: $P_{\text{neto}} = C_{\text{total}} / (1 - m)$.
   * **Separación de Flujos:** Flujo Libre del Proyecto (Fila A) para VAN y TIR; Flujo de Caja Financiado (Fila C) para liquidez acumulada y Curva S. Restricción bloqueante: la línea de crédito al 3,0 % mensual nunca debe superar los **\$50.000.000 CLP**.
   * **Garantías Contractuales:**
     * *Seriedad de la Oferta (Art. 35):* USD 500.000 (\$450.000.000 CLP), boleta bancaria a la vista en Valparaíso (comisión de 1,5 % anual en 5 meses = \$2.812.500 CLP preoperacional; Resp: Gerente de Finanzas).
     * *Fiel Cumplimiento (Art. 36):* USD 1.000.000 (\$900.000.000 CLP), boleta bancaria con vigencia Meses 1 a 68 (comisión bancaria del 1,2 % anual devengada semestralmente a \$5.400.000 CLP/semestre, totalizando \$50.400.000 CLP en 56 meses; Resp: Gerente de Finanzas).
     * *Correcto Funcionamiento (Art. 37):* 5 % del valor de implementación ($V_{\text{impl}}$), vigencia 24 meses (Meses 21 a 45), comisión anual del 1,5 % (Resp: Gerente de Finanzas).
   * **Pólizas de Seguros (Art. 38):**
     * *Responsabilidad Civil (UF 20.000):* Prima anual de UF 65/año (\$2.600.000/año en Meses 1, 13, 25, 37, 49; total \$13.000.000 CLP; Resp: Encargado de Riesgos).
     * *Ciberriesgo y Datos (UF 20.000):* Cobertura de notificación, forense y restitución, prima anual de UF 75/año (\$3.000.000/año en Meses 1, 13, 25, 37, 49; total \$15.000.000 CLP; Resp: CISO y Finanzas).
     * *Todo Riesgo de Equipos:* 0,8 % anual sobre reposición de activos en faena (~CLP 1.200.000/año; Resp: Logística).
     * *Accidentes del Trabajo (Ley 16.744):* 0,93 % sobre remuneraciones imponibles directas de audIT (Resp: RRHH).
   * **Gastos Notariales y Escrow:**
     * *Notaría y Contratación (Art. 68):* Arancel notarial único de UF 30 (\$1.200.000 CLP) en Mes 1 (Resp: Legal).
     * *Custodia de Fuentes Escrow (Art. 84.6):* Depósito semestral de software ante tercero independiente, alta de UF 25 (\$1.000.000 CLP en M6) más canon semestral de UF 15 (\$600.000 CLP en M12, M18, M24, M30, M36, M42, M48, M54; total \$5.800.000 CLP; Resp: Arquitecto de Software y Oficial de Cumplimiento).
   * **Tratamiento Financiero de Post-Operación (Meses 57 a 68):**
     * Dado que el horizonte normativo de evaluación de E-24 está acotado estrictamente a **56 meses**, los costos de la garantía de fiel cumplimiento (\$10.800.000 CLP) y del seguro de ciberriesgo (\$3.000.000 CLP) para los meses 57 a 68 (**total de \$13.800.000 CLP**) se imputan íntegramente dentro del flujo de los 56 meses. Se financian mediante prepago de endoso de cola (*run-off / tail coverage*) en el **Mes 49** y provisión mensualizada de comisiones bancarias durante la operación (M21–M56) liquidada en el **Mes 56**, garantizando que el precio comercial ofertado cubra el 100 % de los compromisos legales postcontractuales.

2. **Justificación Matemática de la Tasa de Descuento (`AUD-7` / Tarea 1.3)**:
   * **Supuesto de Costo de Capital Propio ($K_e$):** Fijado formalmente en **20,0 % anual compuesto** conforme a la política corporativa de audIT y a la Nota Explicativa oficial (Sección 3), equivalente a un **1,531 % mensual** ($1{,}530947\% = (1 + 0{,}20)^{1/12} - 1$).
   * **Distinción Conceptual Crítica:** Se corrige tajantemente la equiparación entre margen operacional EBITDA y tasa de retorno:
     * El *Margen EBITDA ($\text{EBITDA}/\text{Ventas} \le 20\%$)* es una métrica de margen sobre facturación regulada en E-24.
     * La *Tasa Interna de Retorno (TIR)* o costo de capital ($K_e$) mide el rendimiento por unidad de capital invertido en el tiempo. Un proyecto con margen EBITDA de 19 % puede tener una TIR muy distinta según su perfil de capex y cobros de hitos.
   * **WACC Mensual antes de impuestos:** **1,026 % mensual** ($1{,}02619\%$), producto de ponderar 80 % de deuda bancaria al 0,9 % mensual y 20 % de capital propio al 1,531 % mensual ($0{,}80 \times 0{,}900\% + 0{,}20 \times 1{,}530947\%$).
   * **WACC Anual equivalente:** **13,03 % anual** ($(1 + 0{,}0102619)^{12} - 1$).
   * **Regla del VAN:** Se calcula exclusivamente sobre el Flujo Libre (Fila A) sin intereses. Descontar al WACC de 1,026 % mensual genera un VAN positivo que agrega valor neto por encima del costo efectivo de las fuentes de capital.

3. **Explicación de Beneficios Económicos para el Mandante (`AUD-9` / Tarea 1.5)**:
   * **Cuadro Resumen y Calificación Metodológica Dual:**
     * *Beneficios Consolidados de Ingeniería (Innovaciones 2, 3 y 4):* **\$585.000.000 CLP** en 36 meses (\$195.000.000 CLP/año), desglosados en:
       * \$360.000.000 CLP por recuperación de sobreestadías hoy objetadas en faenas (Innovación 4).
       * \$135.000.000 CLP por mantención preventiva de semirremolques por km real y cadena de frío (Innovación 3).
       * \$90.000.000 CLP por reducción de tiempos muertos en patio (Innovación 2).
     * *Proyección bajo Hipótesis Paramétrica de Ingeniería (Innovación 5):* **\$238.320.000 CLP** en 36 meses (\$79.440.000 CLP/año), sujeta a contraste y calibración empírica en marcha blanca (M13–M15) con el TMS 2013 y a integración económica por D2.
     * **TOTAL GLOBAL PROYECTADO PARA CURIMÓN:** **\$823.320.000 CLP en los 36 meses** (\$274.440.000 CLP/año). Al presentar este total se preserva explícitamente su naturaleza dual (base consolidada de \$585M + hipótesis proyectada de \$238,32M).
   * **Separación de Flujos (Art. 50.2):** Estos beneficios pertenecen íntegramente a Curimón y no representan cobro ni ingreso de audIT.

4. **Valorización Completa de la Innovación 5 (`AUD-11` / Tarea 1.7 / `INN-05`)**:
   * **Inversión Incremental audIT (`innovacion-5-inversion`):** **\$13.000.000 CLP netos**:
     * 300 HH de desarrollo algorítmico y síntesis vocal en audIT EdgeHub (M4–M9) a **\$30.000 CLP/HH (costo perfil Profesional Sénior según Formulario E-26)** = \$9.000.000 CLP.
     * 5 talleres ergonómicos presenciales en terminales (M4) a \$440.000 CLP c/u = \$2.200.000 CLP.
     * 60 HH de calibración ergonómica y pruebas de carga mental NASA-TLX en marcha blanca (M13–M15) a **\$30.000 CLP/HH (costo perfil Especialista Ergonómico Sénior según E-26)** = \$1.800.000 CLP.
   * **Costo Operacional Incremental audIT (`innovacion-5-costo`):** **\$10.080.000 CLP netos** (10 HH/mes de soporte algorítmico y privacidad a \$28.000 CLP/HH = \$280.000 CLP/mes durante los 36 meses de operación, Meses 21 a 56).
   * **Beneficio Proyectado Curimón (`innovacion-5-beneficio`):** **\$238.320.000 CLP** (\$79.440.000 CLP/año):
     * *Combustible:* 24.000 viajes nocturnos/año (hipótesis 25 % de 96.000) $\times$ 6,4 km evitados / 2,5 km/l = 61.440 l/año $\times$ \$1.000 CLP/l (precio mayorista ENAP) = **\$61.440.000 CLP/año**.
     * *Mitigación de Siniestralidad Nocturna:* Identificada formalmente como **Supuesto de Escenario de Ingeniería** con 0,48 siniestros evitados/año (1 cada 50.000 viajes nocturnos), calibrada contra el piso conservador de estadísticas de siniestralidad vial de **CONASET** y reportes de fatiga de **ACHS/SUSESO**.
     * *Respaldo del Costo por Incidente Evitado (\$37.500.000 CLP):* Identificado formalmente como **Supuesto de Escenario de Costo Integral**, respaldado analíticamente en la **Guía de Costos de Siniestralidad AACH (POL 1 2013 0034 CMF)** (deducible de flota pesada UF 350 = \$14M) y estudios de **ChileTransporte AG / CNTC** (lucro cesante de 12 días a \$750k/día = \$9M + rescate de grúa pesada y reparaciones menores bajo deducible = \$6,5M + multas contractuales y transbordo = \$8M). Multiplicado por 0,48 incidentes/año arroja exactamente **\$18.000.000 CLP/año** de beneficio referencial de escenario para el cliente, quedando sujeto a contraste en marcha blanca e integración económica en el flujo por parte de D2.

5. **Presupuesto Detallado de Calidad y Capacitación (`AUD-10` / Tarea 1.6)**:
   * **Naturaleza de los Precios:** Todos los precios corresponden a **Estimaciones Paramétricas de Ingeniería basadas en benchmarks del mercado nacional a octubre de 2026** (DICTUC, CESMEC, IDIEM, consultoras de ciberseguridad ofensiva, E-Class y OTECs SENCE).
   * **Calendario de Pagos Estrictamente Conciliado:** La totalidad de los servicios externos y cursos de capacitación se concilian con la regla contractual de **50 % anticipo a la orden de servicio y 50 % contra recepción conforme del informe técnico final o acta de capacitación**:
     * *Mes 4:* Anticipo IP67 (\$2,5M) + arriendo CAN/HIL (\$500k) = **\$3.000.000 CLP**.
     * *Mes 5:* Informe final IP67 (\$2,5M) + Anticipo SAE Campaña 1 (\$1,75M) + arriendo CAN/HIL (\$500k) = **\$4.750.000 CLP**.
     * *Mes 6:* Informe SAE Campaña 1 (\$1,75M) + Anticipo SAE Campaña 2 (\$1,75M) + arriendo CAN/HIL (\$500k) = **\$4.000.000 CLP**.
     * *Mes 7:* Informe SAE Campaña 2 (\$1,75M) + arriendo CAN/HIL (\$500k) = **\$2.250.000 CLP**.
     * *Meses 8 y 9:* Arriendo CAN/HIL = **\$500.000 CLP/mes**.
     * *Mes 10:* Arriendo CAN/HIL (\$500k) + Anticipo LMS y contenidos (\$2,0M) = **\$2.500.000 CLP**.
     * *Mes 11:* Entrega LMS (\$2,0M) + Anticipo Pentest E1 (\$2,25M) + Anticipo Talleres A13 (\$2,625M) = **\$6.875.000 CLP**.
     * *Mes 12:* Informe Pentest E1 para H5 (\$2,25M) + Actas Talleres A13 (\$2,625M) = **\$4.875.000 CLP**.
     * *Mes 17:* Anticipo Pentest E2 (\$2,25M) = **\$2.250.000 CLP**.
     * *Mes 18:* Informe Pentest E2 para H10 (\$2,25M) + Anticipo Capacitación E2 A23 (\$1,75M) = **\$4.000.000 CLP**.
     * *Mes 19:* Actas Capacitación E2 A23 (\$1,75M) = **\$1.750.000 CLP**.
     * *Total Capex Implementación (Meses 1 a 21):* **\$37.250.000 CLP**.
     * *Fase de Operación (Meses 21 a 56):* Pentest anual (50 % anticipo en M29, M41, M53 de \$2,0M; 50 % informe en M30, M42, M54 de \$2,0M) más anualidad de reinducción (\$1,5M en M30, M42, M54). Total Opex = **\$16.500.000 CLP**.
   * **Total Calidad y Capacitación:** **\$53.750.000 CLP**.

---

## 2. Instrucciones de Coordinación para la Dupla 2 (D2)

Para la integración de la planilla común y del calendario mensual de caja:
1. En la hoja `Parámetros`, asociar la celda de tasa de descuento a la fórmula exacta del WACC (`1,026 % mensual`), vinculando `B_tasa` a las celdas de deuda (80 % a 0,9 %) y socios (20 % a 1,531 %).
2. En la hoja `Gastos Administrativos / Overhead`, incorporar las partidas de garantías contractuales (Art. 36 y 37), seguros (Art. 38), gastos notariales (Art. 68), software escrow (Art. 84.6) y la provisión/prepago de los meses postcontractuales M57–M68 (\$13.800.000 CLP) conforme al desglose de AUD-5.
3. En la hoja `Financiamiento`, modelar el servicio de la deuda (intereses al 0,9 % y amortización) y de la línea de crédito (al 3,0 %) en la Fila B para obtener el **Flujo Neto Financiado (Fila C)** y graficar la **Curva S**, auditando que la línea de crédito nunca supere el cupo máximo de \$50.000.000 CLP.
4. En la hoja `Costos`, cargar los desembolsos de las Partidas 1 a 4 y 6 a 8 de Calidad y Capacitación (\$37.250.000 CLP) y de la Innovación 5 (\$13.000.000 CLP) según sus calendarios mensuales específicos en la fase de implementación (Meses 4 a 19), respetando el esquema 50/50 de devengo.
5. En la sección de Operación de la hoja `Costos`, cargar los pentests y reinducciones (\$2,0M en M29, M41, M53 y \$3,5M en M30, M42, M54) y los \$280.000 mensuales de soporte técnico de la Innovación 5 (Meses 21 a 56).
6. En la hoja `Innovaciones`, vincular las claves `innovacion-5-inversion`, `innovacion-5-costo` e `innovacion-5-beneficio` con sus notas de respaldo metodológico paramétrico.
