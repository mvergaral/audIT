# Aclaraciones de Bases Administrativas (Art. 44.1)

**Estimados:**

Las siguientes aclaraciones se emiten conforme al **Art. 44.1 de las Bases Administrativas**. Rigen para todas las empresas y forman parte integrante de las Bases. Al final se adjunta una nota explicativa sobre rentabilidad, tasa de descuento, VAN y Curva S.

---

## 1. Alcance del Informe 3

### a) Preparación de la Oferta Económica
El Informe 3 corresponde a la preparación de la Oferta Económica. **No se debe volver a presentar la Propuesta Técnica ni el contenido de los Informes 1 y 2.**

El Informe 3 debe contener:
* Proveedores clave de la solución.
* Adquisiciones clave.
* Curva S del proyecto.
* Análisis de costos de la solución.
* VAN y TIR.
* Valorización de las cinco innovaciones en el flujo de caja.
* Planilla de cálculo.

> **Alcance según Formulario E-21:**
> * El Informe 3 constituye un avance del **E-21 – Entregable 2** (análisis económico-financiero, el "documento de costos frente a venta") y del **E-21 – Entregable 3** (modelo financiero).
> * El **E-21 – Entregable 1** (la propuesta económica formal) se presenta únicamente en el **Sobre N° 3**.
>
> *Trazabilidad:* Los valores del Informe 3 deben derivar de las cantidades declaradas en los Informes 1 y 2: dotación, horas hombre, EDT y arquitectura (Art. 57.2). **Cualquier costo que no se pueda rastrear hasta la propuesta técnica será observado.**

---

### b) Requisitos adicionales
* **Tabla de trazabilidad (Art. 46):** Formato `observación – respuesta – sección modificada` respecto a las observaciones del Informe 2. Puede ser breve y debe adjuntarse como anexo.
* **Avance del prototipo interactivo:** Disponible a través de un enlace navegable para su revisión. Durante la presentación basta una navegación rápida dentro de los 15 minutos de exposición.
* *Nota:* El Formulario E-21 completo (Entregables 1, 2 y 3) solo se exige en la Oferta Económica final.

---

### c) Uso de la plantilla
La planilla entregada es una guía. Cada empresa puede agregar, modificar o eliminar hojas, salvo las restricciones indicadas en el [Punto 5](#5-estructura-de-la-planilla). El "cumplimiento de la plantilla proporcionada" del Formulario E-21 se entenderá como el respeto irrestricto de esas condiciones mínimas.

---

## 2. Prototipo interactivo
Con el Informe 3 basta con entregar un **avance**. La versión completa, con el alcance mínimo del numeral 25.2 y los requisitos RT-25.06 a RT-25.09, se entrega junto con la propuesta final.

---

## 3. Horizonte de evaluación
**Sí, deben extender el modelo según el Excel.** Rige el horizonte de **56 meses** del Formulario E-24 y del Art. 17:

* **Etapa 1:** Meses 1 a 16.
* **Etapa 2:** Meses 13 a 21.
* **Operación (36 meses):** Meses 21 a 56.

> *Nota:* La estructura referencial de 20 + 16 meses de la plantilla es meramente un ejemplo ilustrativo y no aplica.

---

## 4. Hitos de pago
**Sí, deben reemplazar los hitos de la plantilla por los 12 hitos del Formulario E-25 (H1 a H12)**, respetando sus porcentajes y meses:
* **60 %** en la Etapa 1.
* **40 %** en la Etapa 2 (ambos sobre el valor de la implementación).
* **Operación:** Se factura en **36 pagos mensuales** (meses 21 al 56). No puede anticiparse ni prorratearse en la implementación.

---

## 5. Estructura de la planilla
Se permite agregar todas las hojas requeridas, siempre que se cumplan las siguientes condiciones mínimas:

1. **Hoja Resumen Intocable:** No modificar la hoja *Resumen*. Deben mantenerse sus filas, rótulos y orden, ya que constituye la base estandarizada de comparación entre ofertas.
2. **Hojas mínimas obligatorias:**
   * **Del Formulario E-21:** *Resumen Ejecutivo*, *Parámetros*, *Curva S*, *Costos*, *Ingresos*, *Flujo de Caja* e *Indicadores*.
   * **Proveedores (T-22):** Sumada al gasto de operación.
   * **Sensibilidad:** (E-21, numeral 2.2).
   * **Innovaciones:** (E-21, numeral 2.7).
   * **Financiamiento.**
3. **Curva S graficada:** De carácter mensual, abarcando los 56 meses (ver nota explicativa, sección 6).
4. **Flujo de caja mensual:** Detallado con el total del mes y el monto acumulado (T-22).
5. **Formulación íntegra:** Todo debe calcularse mediante fórmulas directas que permitan rastrear el origen de cada dato. **No se aceptarán valores fijos digitados en celdas de resultado ni constantes incrustadas dentro de las fórmulas.** Todos los supuestos deben residir en la hoja *Parámetros* o en hojas de entrada claramente identificadas.

---

## 6. Gastos administrativos
Debe crearse una hoja dedicada a gastos administrativos que alimente la hoja *Costos*, incluyendo como mínimo:

* **Overhead empresarial:** Gerencia, administración, contabilidad y legal (E-21, 2.1).
* **Costo financiero de garantías:** Seriedad de la oferta, fiel cumplimiento y correcto funcionamiento (Art. 35 a 37).
* **Seguros:** (Art. 38).
* **Gastos notariales y de contratación:** (Art. 68).
* **Custodia de fuentes ante terceros:** (Art. 84.6).

> Cada ítem debe declarar explícitamente su criterio de cálculo. Los intereses de financiamiento **no** son gastos administrativos: deben registrarse en la hoja de *Financiamiento*.

---

## 7. Rentabilidad máxima
* **Tope máximo:** **20 %** aplicable al proyecto completo (no por ítem individual).
* **Métrica:** $\text{EBITDA} / \text{Ingresos netos}$ (sin impuestos y sin IVA).
* Cada componente puede tener un margen diferente siempre que se declare (E-21, 2.1) y el consolidado no sobrepase el 20 %. El 40 % de la plantilla no aplica (ver nota explicativa, sección 2).

---

## 8. Tasa de descuento
Cada empresa debe construir su tasa de descuento utilizando la estructura de financiamiento del Formulario E-24 (deuda y capital propio), antes de impuestos y expresada en términos mensuales, justificando su composición (E-21, 2.2). **Debe ser estrictamente menor al 20 %.** La tasa del 1,92 % anual de la plantilla no aplica (ver nota explicativa, secciones 3 y 4).

---

## 9. Hardware que adquiere el cliente

### Exclusión del flujo
El hardware adquirido por el cliente **no va en el flujo de caja** (dispositivos de campo, instrumentación de planta y recepción, equipamiento de red, medidores y sensores).

### Hoja informativa requerida
Debe detallarse en una hoja informativa separada (no vinculada a la suma del flujo) con:
* Especificación técnica.
* Marca y modelo de referencia.
* Cantidad requerida.
* Costo estimado (conforme al Cap. 11 de Bases Técnicas y Art. 14.2 de Bases Administrativas).

### Ítems que SÍ van en el flujo:
* Instalación, configuración e integración del hardware ejecutada por el proponente.
* Infraestructura on-premise de la solución (servidores, almacenamiento, gabinetes) provista por el proponente según el Art. 14.2.

---

## 10. Exigencias técnicas de la planilla
Las exigencias del Formulario E-21 entran en vigencia a partir del Informe 3:
* Validación de datos en celdas de entrada.
* Protección de fórmulas críticas.
* Documentación de supuestos en cada hoja.
* Ausencia absoluta de valores fijos (*hardcoded*) dentro de las fórmulas.

> **Importante (Art. 40):** Si se protegen hojas con contraseña, esta debe declararse expresamente dentro del informe. De lo contrario, el archivo no será revisado.

---
---

# Nota explicativa: Rentabilidad, Tasa de Descuento, VAN y Curva S

### 1. La idea conceptual
* **Rentabilidad máxima:** Es el límite de ganancia tolerado para la empresa; lo fija el cliente o las condiciones del mercado.
* **Tasa de descuento:** Es el costo del capital con el que la empresa financia el proyecto; la calcula el proponente.
* **Regla de viabilidad:** El proyecto es conveniente si rinde más de lo que cuesta el capital, pero sin superar el tope establecido:

$$\text{Costo del dinero (tasa de descuento)} < \text{Rentabilidad del proyecto} \le 20\%$$

* **Analogía:** Si se adquiere un crédito al 13 % para levantar un negocio, este debe generar más del 13 % para ser rentable. Si además el cliente fija que la ganancia no puede superar el 20 %, el rango admisible de rendimiento es estrictamente entre el 13 % y el 20 %.

---

### 2. Rentabilidad máxima

$$\text{EBITDA} = \text{Ingresos netos (sin IVA)} - \text{Costos operativos del proyecto}$$

* Los costos operativos contemplan: equipo humano, proveedores, servicios de nube, licencias, overhead y gastos administrativos. **No se restan impuestos ni intereses bancarios.**

| Componente | Caso A | Caso B |
| :--- | :---: | :---: |
| **Ingresos netos** (facturación neta) | \$1.000 | \$1.000 |
| **Costos del proyecto** | \$800 | \$780 |
| **EBITDA** | \$200 | \$220 |
| **Rentabilidad** ($\text{EBITDA} / \text{Ingresos}$) | **20 % ✔** | **22 % ✘** |

> *En el Caso B se supera el límite normado; en ese escenario es imperativo reducir el precio de venta.*

---

### 3. Tasa de descuento
Conforme al Formulario E-24, el financiamiento se compone de:
1. **80 % Deuda bancaria:** Tasa del 0,9 % mensual.
2. **20 % Capital propio (socios):** Rentabilidad exigida por riesgo, con un tope de 20 % anual.

Cálculo del costo promedio ponderado de capital (por cada \$100 de financiamiento mensual):

| Fuente | Monto (\$) | Costo mensual | Costo en \$ |
| :--- | :---: | :---: | :---: |
| **Banco** | 80 | 0,900 % | 0,72 |
| **Socios** (20 % anual convertida) | 20 | 1,531 % | 0,31 |
| **Total** | **100** | — | **1,03** |

$$\text{Tasa ponderada mensual} \approx 1,03\% \quad (\approx 13\% \text{ anual})$$

#### Conversión de tasa anual a efectiva mensual
No debe dividirse linealmente entre 12 ($20\% / 12 = 1,667\%$ es incorrecto). Debido a la capitalización periódica, debe aplicarse la equivalencia compuesta:

$$(1 + i_{\text{anual}})^{1/12} - 1 = (1 + 0,20)^{1/12} - 1 \approx 1,531\%$$

*Fórmula en Excel:* `=(1+20%)^(1/12)-1`

---

### 4. Por qué NO usar el 20 % como tasa de descuento
Si se invierten \$100 en el período 0 y se perciben \$120 al cabo de un año, el proyecto rinde exactamente el 20 % permitido:

| Tasa de descuento aplicada | Valor presente de los \$120 | VAN resultante | Interpretación |
| :---: | :---: | :---: | :--- |
| **13 %** | $120 / 1,13 = 106,2$ | **+6,2** | **Favorable:** Rinde por encima del costo de capital. |
| **20 %** | $120 / 1,20 = 100,0$ | **0,0** | Indiferente: no agrega valor. |

> Si se asume el 20 % como tasa de corte, el proyecto óptimo tendrá $\text{VAN} = 0$, y cualquier desviación conllevará un $\text{VAN}$ negativo.

---

### 5. Comparativa: Dos flujos para dos propósitos

| Criterio | Flujo del Proyecto | Flujo de Caja Financiado |
| :--- | :--- | :--- |
| **Pregunta central** | ¿El negocio en sí mismo es rentable? | ¿Existe liquidez disponible en cuenta cada mes? |
| **Componentes** | Ingresos (hitos/operación), costos e inversiones operativas. | Flujo del proyecto $+$ desembolsos de deuda, aportes, líneas de crédito, intereses y amortizaciones. |
| **Aplicación** | Cálculo de **VAN y TIR**. | Seguimiento mensual acumulado (**T-22**) y **Curva S**. |

#### Demostración numérica (cifras en millones de pesos):
* *Supuestos:* Financiamiento en mes 1 (\$160 banco / \$40 socios). Crédito cobra 0,9 % mensual desde mes 2. Déficits cubiertos con línea de crédito al 3 % mensual (tope máximo de \$50.000.000 según E-24).

| Ítem | Mes 1 | Mes 2 | Mes 3 |
| :--- | :---: | :---: | :---: |
| Ingresos por hito | 0 | 0 | 250 |
| Costos del período | −100 | −100 | −20 |
| **A. Flujo del Proyecto** | **−100** | **−100** | **+230** |
| Crédito bancario ingresado (80 %) | +160 | 0 | 0 |
| Aporte de socios ingresado (20 %) | +40 | 0 | 0 |
| Intereses del crédito (0,9 % s/ 160) | 0 | −1,44 | −1,44 |
| Amortización de capital del crédito | 0 | 0 | −160 |
| Giro línea de crédito | 0 | +1,44 | 0 |
| Intereses línea de crédito (3 %) | 0 | 0 | −0,04 |
| Amortización línea de crédito | 0 | 0 | −1,44 |
| **B. Financiamiento neto** | **+200** | **0** | **−162,92** |
| **C. Flujo Neto de Caja (A + B)** | **+100** | **−100** | **+67,08** |
| **Saldo Acumulado en Caja** | **100** | **0** | **67,08** |

* **Lectura operativa:**
  * **Mes 1:** Ingresan \$200 de capital inicial frente a \$100 de egresos. Cierre de caja en +\$100.
  * **Mes 2:** Costos por \$100 más \$1,44 de interés. Como la caja previa era de \$100, se genera un déficit de \$1,44 cubierto mediante línea de crédito.
  * **Mes 3:** Ingresa pago de hito (\$250), cancelando capital e intereses de la línea de crédito y amortizando la deuda bancaria principal.
  * **Regla de control:** El **VAN y TIR** provienen exclusivamente de la **Fila A**. La **Curva S y la liquidez** proceden de la **Fila C**.
  * Si el saldo deudor de la línea sobrepasa el límite de \$50.000.000, la estructura no es financieramente viable y requiere reprogramación de desembolsos o mayor capital inicial.

---

### 6. Qué representa la Curva S
La Curva S (E-21, 2.3) ilustra la evolución acumulada mensual de tres variables:

1. **Costos acumulados:** Suma acumulada de costos operativos más intereses devengados (deuda bancaria y línea de crédito). La amortización de pasivos no representa costo operativo, por lo que no se adiciona.
   *(En el ejemplo: 100 $\rightarrow$ 201,44 $\rightarrow$ 222,92).*
2. **Ingresos acumulados:** Suma progresiva de facturación por hitos de desarrollo (E-25) y mensualidades de operación.
   *(En el ejemplo: 0 $\rightarrow$ 0 $\rightarrow$ 250).*
3. **Saldo de caja acumulado:** Trayectoria de la Fila C. El valle de esta curva expone la máxima necesidad de línea de crédito.
   *(En el ejemplo: 100 $\rightarrow$ 0 $\rightarrow$ 67,08).*

---

### 7. Errores comunes que serán motivo de observación
1. **Adoptar el 20 % como tasa de corte:** Conlleva invariablemente a un VAN nulo o negativo.
2. **Dividir linealmente la tasa anual entre 12:** Debe emplearse capitalización compuesta: `=(1+TasaAnual)^(1/12)-1`.
3. **Duplicar el cómputo de intereses en el VAN:** El VAN se evalúa sobre el flujo libre del proyecto sin descontar intereses, dado que estos ya van ponderados dentro de la tasa de descuento. Los intereses se imputan únicamente en el flujo financiero y en la Curva S.
4. **Incorporar montos con IVA en el flujo:** Todas las evaluaciones deben formularse estrictamente en valores netos.
5. **Inconsistencia de periodicidad en tasas:** A flujos mensuales corresponden tasas efectivas mensuales. La TIR resultante de Excel será mensual; para anualizarla utilícese `=(1+TIR)^12-1`.
6. **Saldos negativos de caja sin soporte de línea:** Cualquier saldo negativo debe respaldarse con la línea de crédito respetando el tope de \$50.000.000.
7. **Parámetros numéricos quemados dentro de fórmulas:** La tasa y demás supuestos deben residir en la hoja *Parámetros* y ser llamados por celda vinculada (ej.: `=VNA(Parametros!B5; ...)`).