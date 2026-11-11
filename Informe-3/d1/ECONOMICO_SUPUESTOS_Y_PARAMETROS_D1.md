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
     * 300 HH de desarrollo algorítmico y síntesis vocal en audIT EdgeHub (M4–M9) a \$30.000 CLP/HH = \$9.000.000 CLP.
     * 5 talleres ergonómicos presenciales en terminales (M4) a \$440.000 CLP c/u = \$2.200.000 CLP.
     * 60 HH de calibración ergonómica y pruebas de carga mental NASA-TLX en marcha blanca (M13–M15) a \$30.000 CLP/HH = \$1.800.000 CLP.
   * **Costo Operacional Incremental audIT (`innovacion-5-costo`):** **\$10.080.000 CLP netos** (10 HH/mes de soporte algorítmico y privacidad a \$28.000 CLP/HH = \$280.000 CLP/mes durante los 36 meses de operación, Meses 21 a 56).
   * **Beneficio Proyectado Curimón (`innovacion-5-beneficio`):** **\$238.320.000 CLP** (\$79.440.000 CLP/año):
     * *Combustible:* 24.000 viajes nocturnos/año (25 % de 96.000 viajes) $\times$ 6,4 km evitados / 2,5 km/l = 61.440 l/año $\times$ \$1.000 CLP/l (precio mayorista ENAP) = **\$61.440.000 CLP/año**.
     * *Mitigación de Siniestralidad Nocturna:* 0,48 siniestros evitados/año (1 cada 50.000 viajes nocturnos) $\times$ costo medio respaldado de **\$37.500.000 CLP por siniestro carretero menor evitado** (deducible de seguro UF 350 = \$14M + lucro cesante 12 días = \$9M + rescate de grúa y reparaciones menores = \$6,5M + multas contractuales y transbordo = \$8M) = **\$18.000.000 CLP/año**.

5. **Presupuesto Detallado de Calidad y Capacitación (`AUD-10` / Tarea 1.6)**:
   * **Inversión en Implementación (Capex):** **\$37.250.000 CLP netos**:
     * *P1. Homologación IP67 (IEC 60529 / CP-HW-08):* 2 campañas a \$2.500.000 = \$5.000.000 CLP (DICTUC/CESMEC, 14-oct-2026; pago en Mes 5).
     * *P2. Ensayos SAE J1455 térmico y vibración (CP-HW-07):* 2 campañas a \$3.500.000 = \$7.000.000 CLP (IDIEM U. de Chile, 16-oct-2026; pagos en Mes 6 y Mes 7).
     * *P3. Arriendo banco HIL e instrumental bus CAN (CP-HW-04):* 7 meses a \$500.000/mes = \$3.500.000 CLP (Vector/Kvaser Chile, 08-oct-2026; pagos Meses 4 a 10).
     * *P4. Pentest externo independiente E1 y E2 (FEP02 §20.1):* 2 auditorías a \$4.500.000 = \$9.000.000 CLP (Dreamlab Technologies, 18-oct-2026; pagos en Mes 12 y Mes 18).
     * *P6. Plataforma LMS y diseño instruccional (A13):* 1 paquete llave en mano = \$4.000.000 CLP (E-Class Formación, 20-oct-2026; pagos en Mes 10 y Mes 11).
     * *P7. Talleres presenciales en 5 terminales (A13):* 15 jornadas a \$350.000/jornada = \$5.250.000 CLP (LogisTrain OTEC, 22-oct-2026; pagos en Mes 11 y Mes 12).
     * *P8. Capacitación complementaria Etapa 2 (A23):* 10 jornadas a \$350.000/jornada = \$3.500.000 CLP (LogisTrain OTEC, 22-oct-2026; pagos en Mes 18 y Mes 19).
   * **Gasto de Operación Directo (Opex, 36 meses):** **\$16.500.000 CLP netos**:
     * *P5. Pentest recurrente anual en producción:* 3 auditorías anuales a \$4.000.000 = \$12.000.000 CLP (Dreamlab Technologies; pagos en Mes 30, Mes 42 y Mes 54).
     * *P9. Plan de reinducción continua y soporte LMS:* 3 anualidades a \$1.500.000 = \$4.500.000 CLP (E-Class Formación; pagos en Mes 30, Mes 42 y Mes 54).
   * **Total Calidad y Capacitación:** **\$53.750.000 CLP**. Las herramientas CI/CD (SonarQube, k6, ZAP) son costeadas por D3 (AUD-25).

---

## 2. Instrucciones de Coordinación para la Dupla 2 (D2)

Para la integración de la planilla común y del calendario mensual de caja:
1. En la hoja `Parámetros`, asociar la celda de tasa de descuento a la fórmula exacta del WACC (`1,026 % mensual`), vinculando `B_tasa` a las celdas de deuda (80 % a 0,9 %) y socios (20 % a 1,531 %).
2. En la hoja `Gastos Administrativos / Overhead`, incorporar las partidas de garantías contractuales (Art. 36 y 37), seguros (Art. 38), gastos notariales (Art. 68) y software escrow (Art. 84.6) conforme al desglose de AUD-5.
3. En la hoja `Financiamiento`, modelar el servicio de la deuda (intereses al 0,9 % y amortización) y de la línea de crédito (al 3,0 %) en la Fila B para obtener el **Flujo Neto Financiado (Fila C)** y graficar la **Curva S**, auditando que la línea de crédito nunca supere el cupo máximo de \$50.000.000 CLP.
4. En la hoja `Costos`, cargar los desembolsos de las Partidas 1 a 4 y 6 a 8 de Calidad y Capacitación (\$37.250.000 CLP) y de la Innovación 5 (\$13.000.000 CLP) según sus calendarios mensuales específicos en la fase de implementación (Meses 4 a 19).
5. En la sección de Operación de la hoja `Costos`, cargar los pentests y reinducciones (\$5.500.000 en M30, M42 y M54) y los \$280.000 mensuales de soporte técnico de la Innovación 5 (Meses 21 a 56).
6. En la hoja `Innovaciones`, vincular las claves `innovacion-5-inversion`, `innovacion-5-costo` e `innovacion-5-beneficio` con sus notas de respaldo metodológico paramétrico.
