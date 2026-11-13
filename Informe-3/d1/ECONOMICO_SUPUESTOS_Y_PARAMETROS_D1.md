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
     * *Fiel Cumplimiento (Art. 36):* USD 1.000.000 (\$900.000.000 CLP), boleta bancaria con vigencia Meses 1 a 68 (comisión bancaria del 1,2 % anual devengada semestralmente a \$5.400.000 CLP/semestre; Resp: Gerente de Finanzas).
     * *Correcto Funcionamiento (Art. 37):* 5 % del valor de implementación ($V_{\text{impl}}$), vigencia 24 meses (Meses 21 a 45), comisión anual del 1,5 % (Resp: Gerente de Finanzas).
   * **Pólizas de Seguros (Art. 38):**
     * *Responsabilidad Civil (UF 20.000):* Prima anual de UF 65/año (\$2.600.000/año en Meses 1, 13, 25, 37, 49; total \$13.000.000 CLP; Resp: Encargado de Riesgos).
     * *Ciberriesgo y Datos (UF 20.000):* Cobertura de notificación, forense y restitución, prima anual de UF 75/año (\$3.000.000/año en Meses 1, 13, 25, 37, 49; total \$15.000.000 CLP; Resp: CISO y Finanzas).
     * *Todo Riesgo de Equipos:* 0,8 % anual sobre reposición de activos en faena (~CLP 1.200.000/año; Resp: Logística).
     * *Accidentes del Trabajo (Ley 16.744):* 0,93 % sobre remuneraciones imponibles directas de audIT (Resp: RRHH).
   * **Gastos Notariales y Escrow:**
     * *Notaría y Contratación (Art. 68):* Arancel notarial único de UF 30 (\$1.200.000 CLP) en Mes 1 (Resp: Legal).
     * *Custodia de Fuentes Escrow (Art. 84.6):* Depósito semestral de software ante tercero independiente, alta de UF 25 (\$1.000.000 CLP en M6) más canon semestral de UF 15 (\$600.000 CLP en M12, M18, M24, M30, M36, M42, M48, M54; total \$5.800.000 CLP; Resp: Arquitecto de Software y Oficial de Cumplimiento).
   * **Tratamiento de Caja Post-Operación (Meses 57 a 68) y Cobro de M56:**
     * *Salida Efectiva de Caja en M56 (\$13.800.000 CLP):* Para respetar el horizonte de 56 meses sin abrir columnas artificiales, el desembolso bancario de extensión de la garantía de fiel cumplimiento (\$10.800.000 CLP) y la prima única del endoso *tail coverage* de ciberriesgo (\$3.000.000 CLP) se programan como salidas efectivas de caja en el **Mes 56**.
     * *Cero Duplicación de Costos:* Al computarse como salida efectiva en M56, **no se realiza provisión contable recurrente mes a mes** en los gastos operacionales de M21 a M55, garantizando que el costo se compute una sola vez en el horizonte del proyecto.
     * *Calce con el cobro de la última mensualidad.* Según E-25, el servicio de M55 se cobra en M56 y el de M56 se cobra en M57. Registrar la última mensualidad como cuenta por cobrar al cierre de M56 y calcular la liquidez con los cobros efectivos. Para el escenario base de VAN/TIR, usar los flujos efectivos de M1–M56. Como sensibilidad del VAN, presentar por separado el valor en M56 de la cuenta por cobrar de M57, descontada un período con la tasa mensual del escenario.

2. **Justificación Matemática de la Tasa de Descuento (`AUD-7` / Tarea 1.3)**:
   * **Supuesto de Costo de Capital Propio ($K_e$):** Fijado formalmente en **20,0 % anual compuesto** conforme a la política corporativa de audIT y a la Nota Explicativa oficial (Sección 3), equivalente a un **1,531 % mensual** ($1{,}530947\% = (1 + 0{,}20)^{1/12} - 1$).
   * **Distinción Conceptual Crítica:** Se corrige tajantemente la equiparación entre margen operacional EBITDA y tasa de retorno:
     * El *Margen EBITDA ($\text{EBITDA}/\text{Ventas} \le 20\%$)* es una métrica de margen sobre facturación regulada en E-24.
     * La *Tasa Interna de Retorno (TIR)* o costo de capital ($K_e$) mide el rendimiento por unidad de capital invertido en el tiempo. Un proyecto con margen EBITDA de 19 % puede tener una TIR muy distinta según su perfil de capex y cobros de hitos.
   * **WACC Mensual antes de impuestos:** **1,026 % mensual** ($1{,}02619\%$), producto de ponderar 80 % de deuda bancaria al 0,9 % mensual y 20 % de capital propio al 1,531 % mensual ($0{,}80 \times 0{,}900\% + 0{,}20 \times 1{,}530947\%$).
   * **WACC Anual equivalente:** **13,03 % anual** ($(1 + 0{,}0102619)^{12} - 1$).
   * **Regla del VAN y M0:** Se calcula exclusivamente sobre el Flujo Libre (Fila A) sin deducir intereses. Dado que las obras y desembolsos arrancan en M1, $F_0 = 0$ y la función `=VNA(B_tasa; Flujo_M1_M56)` reporta directamente el valor actual neto.

3. **Explicación de Beneficios Económicos para el Mandante (`AUD-9` / Tarea 1.5)**:
   * **Tipo 1:** Valorización pendiente.
   * **Tipo 2:** Beneficio monetario de Curimón pendiente de acreditar. Caso base prudente CLP 0 y sensibilidad provisional CLP 90.000.000 en M21–M56. Validar oportunidades elegibles, visitas y minutos evitados, costos unitarios y pagador. Las horas de instalación liberadas corresponden a audIT.
   * **Tipo 3:** El kilometraje real cumple el criterio 26. Se retiran CLP 75.000.000 de la valorización incremental a 36 meses. Caso base prudente CLP 0 (D4-149). Se mantiene CLP 60.000.000 a 36 meses como sensibilidad térmica provisional. El beneficio del acople queda pendiente de cuantificar. Los CLP 135.000.000 del cálculo original quedan como antecedente histórico porque incluían kilometraje.
   * **Tipo 4:** CLP 120.700.000 brutos/año (CLP 340.000.000 × 71 % × 50 % supuesto) y CLP 362.100.000 brutos en 36 meses a régimen. Neto de Curimón pendiente del reparto con transportistas.
   * **Tipo 5:** CLP 238.320.000 en 36 meses como escenario, sujeto a calibración en marcha blanca.
   * **Consolidación:** El total neto queda pendiente de validación. El recupero bruto y las sensibilidades se muestran por separado y los beneficios de Curimón se mantienen fuera de los ingresos de audIT.

4. **Valorización Completa de la Innovación 5 (`AUD-11` / Tarea 1.7 / `INN-05`)**:
   * **Cumplimiento del Artículo 50.2 (Sobre Técnico vs. Sobre Económico):** En el Formulario T-19 (Ficha 5) se han suprimido todos los valores monetarios en CLP y tarifas horarias, remitiendo formalmente su valorización al Sobre N.º 3 (Oferta Económica).
   * **Inversión Incremental audIT (`innovacion-5-inversion`):** **\$13.000.000 CLP netos**:
     * 300 HH de desarrollo algorítmico y síntesis vocal en audIT EdgeHub (M4–M9) a **\$30.000 CLP/HH (costo perfil Profesional Sénior según Formulario E-26)** = \$9.000.000 CLP.
     * 5 talleres ergonómicos presenciales en los terminales oficiales de Curimón: **San Bernardo, Antofagasta, Talca, Los Ángeles y Puerto Montt** (M4) a \$440.000 CLP c/u = \$2.200.000 CLP.
     * 60 HH de calibración ergonómica y pruebas de carga mental NASA-TLX en marcha blanca (M13–M15) a **\$30.000 CLP/HH (costo perfil Especialista Ergonómico Sénior según E-26)** = \$1.800.000 CLP.
   * **Costo Operacional Incremental audIT (`innovacion-5-costo`):** **\$10.080.000 CLP netos** (10 HH/mes de soporte algorítmico y auditorías semestrales de privacidad a \$28.000 CLP/HH = \$280.000 CLP/mes durante los 36 meses de operación, Meses 21 a 56).
   * **Beneficio Proyectado Curimón (`innovacion-5-beneficio`):** **\$238.320.000 CLP acumulados en 36 meses** (\$79.440.000 CLP/año):
     * *Combustible:* 24.000 viajes nocturnos/año (hipótesis 25 % de 96.000) $\times$ 6,4 km evitados / 2,5 km/l = 61.440 l/año $\times$ \$1.000 CLP/l (precio mayorista ENAP) = **\$61.440.000 CLP/año** (\$184.320.000 CLP en 36 meses).
     * *Mitigación de Siniestralidad Nocturna:* Identificada formalmente como **Supuesto de Escenario de Ingeniería** con 0,48 siniestros evitados/año (1 cada 50.000 viajes nocturnos), calibrada contra el piso de estadísticas de **CONASET** y reportes de fatiga de **ACHS/SUSESO**.
     * *Respaldo del Costo por Incidente Evitado (\$37.500.000 CLP):* Identificado formalmente como **Supuesto de Escenario de Costo Integral**, respaldado en la **Guía de Costos de Siniestralidad AACH (POL 1 2013 0034 CMF)** (deducible UF 350 = \$14M) y estudios de **ChileTransporte AG / CNTC** (lucro cesante de 12 días = \$9M + rescate de grúa pesada y reparaciones menores = \$6,5M + multas contractuales y transbordo = \$8M). Multiplicado por 0,48 incidentes/año arroja **\$18.000.000 CLP/año** (\$54.000.000 CLP en 36 meses).
     * *Instrucción de Carga para D2:* La clave **`innovacion-5-beneficio`** corresponde a los **\$238.320.000 CLP en 36 meses**. Los \$18.000.000 CLP anuales corresponden únicamente al componente de siniestralidad.

5. **Presupuesto Detallado de Calidad y Capacitación (`AUD-10` / Tarea 1.6)**:
   * **Naturaleza de los Precios:** Todos los precios corresponden a **Estimaciones Paramétricas de Ingeniería basadas en benchmarks del mercado nacional a octubre de 2026** (DICTUC, CESMEC, IDIEM, consultoras de ciberseguridad ofensiva, E-Class y OTECs SENCE).
   * **Terminales Oficiales en Partida 7 (A13):** 15 jornadas presenciales distribuidas en los cinco terminales oficiales de Curimón: **San Bernardo, Antofagasta, Talca, Los Ángeles y Puerto Montt** (Caso 10, §2.3, p. 8).
   * **Calendario de Pagos Conciliado (50 % Anticipo / 50 % Contra Informe):**
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

### Conducción y validación de CP-SEC-05 en G13

**Estimación de ingeniería del 12-11-2026: 8 h del Líder de Seguridad**, correspondiente al Encargado de Seguridad de la Información del equipo, para una campaña del caso CP-SEC-05 con variante conectada y sin enlace. Se planifican en **M10, antes de liberar G13 en el día hábil contractual 182**, con candidato, configuración y datos identificados. Son horas de personas, no ocho horas de ejecución continua ni resultados de una prueba ya realizada.

| Actividad del Líder de Seguridad | Horas | Mes y paquete | Resultado previsto |
|---|---:|---|---|
| Preparar la ejecución: revisar protocolo, alcances de los permisos y conservación; verificar versión/configuración congeladas, datos ficticios, relojes y condiciones de observación. | 2 | M10 · 10.1, salida G13 | Lista de entrada y guion aprobables antes de iniciar. |
| Conducir las variantes con y sin enlace; ordenar la revocación por el actor autorizado, comprobar rechazo al actor ajeno y observar el cese de acceso y de captura para la finalidad revocada. | 2 | M10 · 10.1, salida G13 | Registro de ejecución, tiempos y anomalías con el equipo instrumentado. |
| Validar la evidencia: correlacionar permiso y tiempos de portal/equipo/log/SQLite; verificar el límite de cinco minutos, la continuidad del tratamiento con base independiente y la identidad/huella de la evidencia previa retenida. | 3 | M10 · 10.1, salida G13 | Dictamen trazable de cumplimiento o defecto; la ausencia de transmisión no basta. |
| Cerrar el expediente del caso: emitir veredicto y registrar defectos, responsables y resultado de la revisión para la decisión de G13. | 1 | M10 · 10.1, salida G13 | Informe del caso y remisión al Líder de Calidad y Pruebas. |
| **Total** | **8** | **M10 · 10.1 / G13** | **Una asignación interna, contada una sola vez.** |

**Imputación:** 10.1 es el paquete de pruebas de sistema e integración de T-14 y ya contempla actividad durante A09. G13 identifica la salida que usa la evidencia; no es otro paquete al que cobrar las mismas 8 h. La ejecución y su revisión deben terminar antes de esa puerta, sin esperar a A12, que comienza en el día 192. La estimación supone que D3 entrega agente e instrumentación listos y que D4 monta/opera el banco; correcciones de software y una nueva campaña por un fallo requieren reestimación de la actividad afectada.

**Cobertura presupuestaria verificable:** T-15 ya asigna 6.400 h al elemento 10, pero no individualiza en su texto estas 8 h del perfil de Seguridad en M10. Por tanto, se registra una asignación objetivo **dentro de 10.1**, con cobertura por perfil pendiente de comprobar; no se afirma que exista holgura ni que deban contratarse ocho horas nuevas. D2 debe individualizar la cobertura existente y conciliar cualquier ejecución común ya estimada para G13, incluidas las 16 h de Seguridad de REV-S7-02 del catálogo D3. La preparación/corrección de construcción y la conducción/revisión del ensayo tienen resultados propios; si alguna tarea o ejecución es la misma, se imputa una sola vez.

**Cruce de la reserva:** las 8 h de D1 y las 7 h de D4 suman **15 h-persona** de conducción/validación y banco/corrida. Frente a las 16 h condicionales informadas por D2 queda una diferencia nominal de 1 h, que no acredita disponibilidad ni cobertura por perfil. La composición previa de la reserva (QA 8 h, Software 4 h y Firmware 4 h) debe conciliarse con **Seguridad 8 h, Técnico 5 h y Operación/SRE 2 h**; no se suman ambas composiciones. Las 72 h de preparación del agente D3 permanecen en 4.1/A11, M6–M9, y sus 8 h de QA M9 conservan el cruce separado con CP-HW-03. No se agregan a esta corrida ni a las 6.008 h de A09.

**Costo interno atribuible de referencia:** correspondencia con el perfil **Encargado de Seguridad TI** de E-26, costo 0,8–1,4 UF/h. Con la UF contractual de CLP 40.000 de E-24, el punto medio es 1,1 UF/h = CLP 44.000/h: **8 h × CLP 44.000 = CLP 352.000**, rango CLP 256.000–448.000. Es una referencia de personal, no una cotización ni tarifa de venta. No se aplica IVA automáticamente como factura externa. El costo adicional se obtiene sólo por las horas no cubiertas del mismo perfil y mes; no se suma a los CLP 53.750.000 de compras/servicios de calidad y capacitación ni a remuneraciones ya presupuestadas.

**Fuentes de alcance y calendario:** catálogo T-17 oficial, CP-SEC-05; S6, «Puerta de salida G13 y funciones de sprint 7»; T-14, 10.1; T-15, A09/G13/A12 y elemento 10. **Fuentes de valoración:** FEP01 · E-24 · p.73 y E-26 · p.76. Las 8 h y su desglose son una estimación de planificación adoptada para este insumo, no una duración medida ni una confirmación de cobertura financiera.

---

## 2. Instrucciones de Coordinación para la Dupla 2 (D2)

Para la integración de la planilla común y del calendario mensual de caja:
1. En la hoja `Parámetros`, asociar la celda de tasa de descuento a la fórmula exacta del WACC (`1,026 % mensual`), vinculando `B_tasa` a las celdas de deuda (80 % a 0,9 %) y socios (20 % a 1,531 %).
2. En la hoja `Gastos Administrativos / Overhead`, incorporar las partidas de garantías contractuales (Art. 36 y 37), seguros (Art. 38), gastos notariales (Art. 68), software escrow (Art. 84.6) y registrar en el **Mes 56** la salida efectiva de caja de \$13.800.000 CLP (prepago de extensión de fiel cumplimiento y póliza de cola de ciberriesgo para M57–M68), sin duplicar provisiones mensuales en M21 a M55.
3. En la hoja `Flujo de Caja Financiado`, calcular la liquidez de M56 con los cobros efectivos y el pago de garantías y seguros de ese mes. Registrar el cobro de la última mensualidad en M57 en la conciliación de cierre y verificar si se requiere financiamiento puente.
4. En la hoja `Costos`, cargar los desembolsos de las Partidas 1 a 4 y 6 a 8 de Calidad y Capacitación (\$37.250.000 CLP) y de la Innovación 5 (\$13.000.000 CLP) según sus calendarios mensuales específicos en la fase de implementación (Meses 4 a 19), respetando el esquema 50/50 de anticipos e informes.
5. En la sección de Operación de la hoja `Costos`, cargar los pentests y reinducciones (\$2,0M en M29, M41, M53 y \$3,5M en M30, M42, M54) y los \$280.000 mensuales de soporte técnico de la Innovación 5 (Meses 21 a 56).
6. En la hoja `Innovaciones`, vincular las claves `innovacion-5-inversion` (\$13.000.000 CLP), `innovacion-5-costo` (\$10.080.000 CLP) e `innovacion-5-beneficio` (**\$238.320.000 CLP** acumulados en 36 meses).
