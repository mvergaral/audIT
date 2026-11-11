# Paquete Económico y Financiero de Dupla 1 (Informe 3)

**Proyecto:** Licitación TFEP-01-2026 · Caso 10 · Transportes Curimón S.A.  
**Autoría:** Dupla 1 (Evaluación Financiera, Beneficios y Consolidación Documental).  
**Destinatarios:** Dupla 2 (Integración de Planilla, Flujo y Curva S), Dupla 3, Dupla 4 y Mesa de Coordinación.  
**Estado:** Formalizado y verificado conforme a Bases Administrativas (FEP01.26), Formularios E-21 a E-26, T-22 y Aclaraciones Oficiales del Art. 44.1.

---

## 1. Resumen Ejecutivo del Paquete D1

En cumplimiento del rol asignado a la Dupla 1 en la planificación del Informe 3 y en el proyecto oficial de Linear (`AudIT_Fep`), este documento consolida los cuatro componentes financieros bajo la titularidad técnica de D1:

1. **Supuestos de Precio, Margen y Financiamiento (`AUD-5` / Tarea 1.1)**:
   * Rentabilidad objetivo del proyecto fijada en **18,5 % a 19,0 % EBITDA**, garantizando estricta subordinación al tope legal del **20,0 % EBITDA** sobre ingresos netos normado en E-24 y aclarado oficialmente en Art. 44.1.
   * Criterio de precios: $P_{\text{neto}} = C_{\text{total}} / (1 - m)$, con firmeza de precios en implementación (M1–M21) y reajustabilidad por IPC en operación (M21–M56).
   * Horizonte de evaluación estricto de **56 meses**.
   * Separación entre el **Flujo Libre del Proyecto (Fila A)** para VAN/TIR y el **Flujo de Caja Financiado (Fila C)** para liquidez acumulada y Curva S.
   * Restricción bloqueante de liquidez: el cupo de la línea de crédito al 3,0 % mensual nunca debe superar los **\$50.000.000 CLP**.

2. **Justificación Matemática de la Tasa de Descuento (`AUD-7` / Tarea 1.3)**:
   * **WACC Mensual antes de impuestos:** **1,026 % mensual** ($1{,}02619\%$), producto de ponderar 80 % de deuda bancaria al 0,9 % mensual y 20 % de capital propio al 1,531 % mensual (equivalencia compuesta de la rentabilidad anual del 20 %: $(1 + 0{,}20)^{1/12} - 1$).
   * **WACC Anual equivalente:** **13,03 % anual**.
   * Prevención de error: **no** utilizar el 20 % como tasa de corte (conlleva VAN $\le 0$) ni dividir linealmente por 12.
   * Consistencia: flujos mensuales se descuentan con la tasa mensual de 1,026 %; la TIR obtenida en Excel es mensual y se anualiza mediante $(1 + \text{TIR})^{12} - 1$.

3. **Explicación de Beneficios Económicos para el Mandante (`AUD-9` / Tarea 1.5)**:
   * Cuantificación rigurosa de ahorros operacionales para Transportes Curimón S.A. por un total acumulado de **\$823.320.000 CLP en los 36 meses de operación**:
     * \$238.320.000 CLP por ahorro de diésel (61.440 l/año) y reducción de siniestros nocturnos (Innovación 5).
     * \$360.000.000 CLP por recuperación de sobreestadías hoy objetadas en faenas (Innovación 4).
     * \$135.000.000 CLP por mantención preventiva de semirremolques por km real y cadena de frío (Innovación 3).
     * \$90.000.000 CLP por reducción de tiempos muertos en patio (Innovación 2).
   * Separación categórica (Art. 50.2): estos ahorros pertenecen al cliente y **no** se registran como cobro o ingreso de audIT.

4. **Valorización Completa de la Innovación 5 (`AUD-11` / Tarea 1.7 / `INN-05`)**:
   * **Inversión adicional audIT (`innovacion-5-inversion`):** **\$13.000.000 CLP** (300 HH de desarrollo algorítmico en M4–M9, 5 talleres ergonómicos en terminales en M4 y 60 HH de calibración en M13–M15).
   * **Costo operacional incremental audIT (`innovacion-5-costo`):** **\$10.080.000 CLP** (10 HH/mes de soporte y privacidad durante los 36 meses de operación a \$280.000/mes).
   * **Beneficio directo Curimón (`innovacion-5-beneficio`):** **\$238.320.000 CLP** en 36 meses (\$79.440.000 CLP/año).
   * Claves cargadas formalmente en `partidas.csv` y Ficha 5 de Formulario T-19.

5. **Presupuesto de Calidad y Capacitación (`AUD-10` / Tarea 1.6)**:
   * **Inversión en Implementación:** **\$37.250.000 CLP**, desglosada en:
     * Ensayos físicos y ambientales de laboratorio externo: \$5.000.000 CLP (homologación IP67, IEC 60529 en M5) + \$7.000.000 CLP (cámara climática y vibración SAE J1455 en M6–M7) + \$3.500.000 CLP (banco HIL e instrumental bus CAN en M4–M10).
     * Auditorías externas independientes de seguridad ofensiva (Pentest): \$9.000.000 CLP (M12 para H5 y M18 para H10).
     * Programa de capacitación presencial y plataforma LMS: \$4.000.000 CLP (LMS y diseño instruccional) + \$5.250.000 CLP (talleres en 5 terminales A13 en M11–M12) + \$3.500.000 CLP (capacitación Etapa 2 A23 en M18–M19).
   * **Gasto de Operación (36 meses):** **\$16.500.000 CLP**, desglosada en:
     * 3 auditorías anuales de penetración recurrentes en producción (M30, M42, M54): \$12.000.000 CLP.
     * Plan continuo de reinducción y rotación de conductores/operadores: \$4.500.000 CLP.
   * Total Contrato Calidad y Capacitación: **\$53.750.000 CLP**. Herramientas CI/CD (SonarQube, k6, ZAP) costeadas en D3 para evitar duplicación.

---

## 2. Instrucciones de Coordinación para la Dupla 2 (D2)

Para la integración de la planilla común y del calendario mensual de caja:
1. En la hoja `Parámetros`, asociar la celda de tasa de descuento a la fórmula exacta del WACC (`1,026 % mensual`), vinculando `B_tasa` a las celdas de deuda (80 % a 0,9 %) y socios (20 % a 1,531 %).
2. En la hoja `Flujo de Caja`:
   * Calcular el **VAN** aplicando `=VNA(Parametros!B_tasa; FlujoProyecto_M1_M56) + FlujoProyecto_M0` sobre la fila del **Flujo Libre del Proyecto (Fila A)**, sin deducir intereses bancarios.
   * La **TIR** sobre la Fila A reportará la tasa mensual. La TIR anualizada debe formularse como `=(1+TIR_mensual)^12-1`.
   * Modelar el servicio de la deuda (intereses al 0,9 % y amortización) y de la línea de crédito (al 3,0 %) en la sección de financiamiento (Fila B) para obtener el **Flujo Neto Financiado (Fila C)**.
   * Graficar la **Curva S** acumulando costos operativos más intereses devengados frente a la facturación de hitos y pagos mensuales, auditando que la línea de crédito nunca exceda los \$50.000.000 CLP.
3. Incorporar los \$13.000.000 de inversión de Innovación 5 en el presupuesto de inversión (M4–M15) y los \$280.000 mensuales en costos de operación técnica (M21–M56).
4. Cargar en la hoja `Costos` las partidas de Calidad y Capacitación de D1: \$37.250.000 en Inversión (ensayos IP67/SAE, pentest y talleres) y \$16.500.000 en Operación (pentest anual y reinducción).
