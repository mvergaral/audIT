# Verificación Aritmética del Modelo Económico de Persona 4

## TI-12 · audIT (Empresa N.º 10) · Caso 10, Transportes Curimón S.A.

**Verificador:** Matías V. (Persona 8)
**Documento auditado:** `Persona-4/Subdocumento_Persona_4_Consolidado_Definitivo.md`
**Fecha:** 21 de septiembre de 2026
**Método:** recálculo íntegro de las tablas y de los indicadores derivados, y ejecución
del script `modelo_costos.py` transcrito en el §7 del propio documento.

> A diferencia del fact-checking de fuentes, esta verificación **sí es concluyente**: opera
> sobre datos que ya están en el repositorio y no requiere consultar nada externo.

---

## 1. Lo que cuadra

La tabla de flujo de desembolso del §3.2 es **exacta en las tres direcciones**: las diez
partidas suman su total de fila, las cinco columnas suman su total de columna, y ambos
caminos convergen en 8.375,40 UF sin diferencia alguna.

| Verificación | Resultado |
| :--- | :--- |
| Suma de las 10 filas | 8.375,40 UF ✓ |
| Suma de las 5 columnas (1.678,0 + 1.531,0 + 2.156,7 + 1.780,7 + 1.229,0) | 8.375,40 UF ✓ |
| Conversión a pesos: 8.375,4 × 40.000 | $335.016.000 ✓ |
| Conversión a dólares: 335.016.000 / 900 | USD 372.240 ✓ |
| Las 10 conversiones a CLP fila por fila | 10 de 10 exactas ✓ |
| Puente de conciliación §3.3: 4.768,4 + 3.607,0 | 8.375,40 UF ✓ |
| Desagregados: 120 + 725,4 = 845,4 · 2.016 + 310 = 2.326 · 891 + 390 = 1.281 | ✓ |
| Escenario HSM §4.1: 8.375,4 − 725,4 + 2.680,6 | 10.330,6 UF ✓ |
| Umbral de indiferencia: 8.375,4 / 55.000 | 15,23 % ✓ |
| Cota de Gordon-Loeb: 1/e | 36,79 %, coherente con el «≤ 37 %» ✓ |
| 20.000 UTM × $70.000 / 40.000 | 35.000 UF ✓ |
| 10.000 UTM × $70.000 / 40.000 | 17.500 UF ✓ |
| Tarifas de rol: DPO 18 h/mes y CISO 24 h/mes a 2,00 UF/h, en los cinco tramos | ✓ exactas |

**El script del §7 corre y reproduce el TCO al centavo: 8.375,40 UF.** Eso es trabajo de
ingeniería verificable y es la mejor defensa posible frente al Comunicado 9. Conviene
decirlo en la exposición.

---

## 2. Hallazgo A-01 · El tramo 3 dura 16 meses y tres partidas lo cobran como 12

La cabecera de la tabla define los tramos: **1-12, 13-20, 21-36, 37-48, 49-56**, que suman
56 meses. El tercero, «Meses 21 a 36 (Año 3)», dura **16 meses**, no 12.

Las partidas basadas en dedicación —DPO y CISO— respetan esa duración: 16 × 36 = 576 UF
y 16 × 48 = 768 UF, ambas correctas. Pero **tres partidas de tarifa periódica cobran ese
tramo como si durase 12 meses**:

| Partida | Tarifa declarada en el documento | Tramo 3 declarado | Equivale a | 16 meses serían | Faltan |
| :--- | :--- | :---: | :---: | :---: | :---: |
| Cifrado Azure Key Vault | 686 claves × USD 1/mes = 15,435 UF/mes | 185,20 UF | 12,00 meses | 246,96 UF | **61,76 UF** |
| Póliza Chubb | 90 UF/año = 7,50 UF/mes | 90,00 UF | 12,00 meses | 120,00 UF | **30,00 UF** |
| SaaS GRC | 60 UF/año = 5,00 UF/mes | 60,00 UF | 12,00 meses | 80,00 UF | **20,00 UF** |
| | | | | **Total** | **111,76 UF** |

Con la corrección, el TCO sería **8.487,16 UF** ($339.486.400 CLP): un **+1,33 %**.

### Corroboración independiente

La fila del SaaS GRC totaliza **255,00 UF**. Si el tramo 3 se cobrara por sus 16 meses,
la fila totalizaría **280,00 UF** — que es **exactamente la cifra que el propio Persona 4
usa en otros dos lugares**: en `Entregable_1_Matriz_Obligaciones.md` (fila 138, «280,00 UF
· $11.200.000 CLP») y en la matriz de sensibilidad del §4.2 («Escenario Base · 280,00 UF ·
CISO Assistant Pro»).

Es decir: el documento ya contiene la cifra correcta en dos sitios, y el flujo de caja
arrastra la de 12 meses. Eso descarta que sea una decisión deliberada de prorrateo y lo
identifica como arrastre de una versión anterior del modelo.

> **Nota metodológica.** El script del §7 **sí** distribuye estas partidas sobre 16 meses
> (`90.0 / 16`, `112.5 / 16`, `85.0 / 16`), lo que confirma que el tramo es de 16 meses.
> El script divide los totales declarados, de modo que reproduce fielmente la tabla; lo
> que no cuadra es el total de la fila frente a su propia tarifa unitaria.

---

## 3. Hallazgo A-02 · El script no reproduce el VAN declarado

El §7 afirma que el script «reproduce el 100 % de las tablas y cifras de este documento».
Ejecutado sin modificación alguna:

```
Total TCO:           8,375.40 UF  ($335,016,000 CLP)     <- coincide con el texto
VAN Costo (0.9% m):  6,559.64 UF  ($262,385,649 CLP)     <- el texto declara 6.582,3 UF
```

Diferencia: **22,66 UF**. El TCO coincide exactamente; el VAN no.

Es la misma variable que ya arrastraba discrepancias. Los valores que circulan en el
repositorio son ahora **cuatro**:

| Valor | Dónde |
| :--- | :--- |
| **6.582,3 UF** | Texto del §3.3 del definitivo y `Bitacora_A6_Persona_4` |
| **6.559,64 UF** | Salida del script del §7 **del mismo documento** |
| **5.757,68 UF** | `Entregable_2`, `Entregable_4`, `.tex`, `README` |
| **6.537,13 UF** | Citado en `PENDIENTES_…md`; ya no aparece en ningún archivo |

**Acción:** Persona 4 corre el script, toma la cifra que produce y la escribe en el texto,
o corrige el script si la distribución mensual que asume no es la que quiso modelar. Lo
que no puede quedar es un documento que afirme reproducir una cifra que su propio código
no produce: es exactamente el indicio b del Comunicado 9, «cifras que no puedan seguirse
hasta un cálculo mostrado».

---

## 4. Hallazgo A-03 · El RoSI declarado no sale de la fórmula mostrada

El §5 escribe la fórmula completa y su resultado:

$$\text{RoSI} = \frac{(55.000 \times 0,85) - 8.375,4}{8.375,4} \times 100\% = \mathbf{459{,}68\%}$$

Recalculado: (46.750 − 8.375,4) / 8.375,4 = 38.374,6 / 8.375,4 = **458,18 %**.

Diferencia: **1,5 puntos porcentuales**. La fórmula y los tres números están a la vista,
de modo que el error se detecta con una calculadora. Es el caso más simple de corregir y
el más fácil de que lo encuentre el evaluador.

---

## 5. Hallazgo A-04 · La base de la proporcionalidad no tiene fuente

El §3.3 afirma que el TCO «representa aproximadamente un **3,9 %** del presupuesto total
estimado para la licitación (estimada en ~215.000 UF a 56 meses)».

La aritmética es correcta: 8.375,4 / 215.000 = 3,90 %. **El problema es el denominador.**
Búsqueda sobre las tres bases (FEP01, FEP02, FEP03) con `tools/buscar.py`: no hay monto
total publicado. Tampoco está declarado como estimación propia con su método.

Lo mismo con el «rango 3 %–5 % de la industria logística» de la frase siguiente, que no
lleva fuente.

**Acción:** o se aporta la fuente, o se declara como estimación propia explicando cómo se
construyó, o se retira el párrafo. La primera opción es la mejor: el §4 de las Indicaciones
valora explícitamente «mediciones o pruebas realizadas por el equipo».

---

## 6. Aclaración sobre Azure Key Vault

Una observación anterior de esta auditoría señalaba «tres cifras para la misma partida».
**Corresponde precisar:** no son tres cifras contradictorias sino dos alcances distintos
más un residuo:

| Cifra | Qué es |
| :--- | :--- |
| **725,4 UF** | Solo las 686 claves, a USD 1/clave/mes. Correcta |
| **845,4 UF** | Las claves más 120 UF de ingeniería de cifrado. Correcta; es la fila 5 del §3.1 |
| **0,00 UF marginal** | Versión antigua, en `Subdocumento_Persona_4_Consolidado.md` y su README, donde se presumía absorbido en el tier CSP. **Superada** |

Persona 5 cita 845,4 UF en su declaración A-6, que **coincide** con el documento
definitivo. No hay contradicción entre P4 y P5 en esta partida. Lo que sí queda en pie es
el conflicto de arquitectura del hallazgo H-07: Key Vault **Premium** frente a Managed
**HSM**.

---

## 7. Resumen

| # | Hallazgo | Efecto | Esfuerzo |
| :-: | :--- | :--- | :--- |
| **A-01** | Tramo 3 cobrado como 12 meses en tres partidas | TCO +111,76 UF (+1,33 %) | Recalcular tres celdas y los totales |
| **A-02** | El script no reproduce el VAN del texto | 22,66 UF de diferencia | Correr el script y copiar la cifra |
| **A-03** | RoSI 459,68 % frente a 458,18 % calculado | 1,5 pp | Una línea |
| **A-04** | Base de 215.000 UF sin fuente | El 3,9 % no es rastreable | Fuente, declaración o retiro |

Ninguno de los cuatro invalida el modelo. Los cuatro son del tipo que el Comunicado 9
describe en su letra b, y los cuatro se cierran en una sesión de trabajo.

**El modelo tiene fondo real**: cuadra en tres direcciones, tiene un script que lo
reproduce y sus tarifas de rol son exactas contra el Formulario E-26. Lo que falta es la
pasada final de consistencia.

---

**Firma del verificador:** ______________________  **Fecha:** ____________

---

## Anexo · Estado tras la aplicación de los hallazgos (21-09-2026)

| Hallazgo | Estado |
| :--- | :--- |
| **A-01** Tramo 3 cobrado como 12 meses | **Aplicado.** Key Vault 725,4 → 787,16 UF · Chubb 390,0 → 420,0 UF · GRC 255,0 → 280,0 UF. TCO 8.375,40 → **8.492,16 UF** ($339.686.400 CLP · USD 377.429) |
| **A-02** El script no reproducía el VAN | **Aplicado.** Actualizadas las tres tarifas en `modelo_costos.py`; el script vuelve a reproducir el TCO al centavo y entrega **VAN = 6.651,24 UF**, que es la cifra que ahora figura en el texto |
| **A-03** RoSI 459,68 % | **Aplicado.** Recalculado sobre la base vigente: **450,51 %** |
| **A-04** Base de 215.000 UF sin fuente | **Abierto.** La proporción se actualizó a 3,95 %, pero el denominador sigue sin respaldo |

Indicadores recalculados sobre 8.492,16 UF: puente de conciliación 4.855,16 + 3.637,0;
$p^* = 15,44\,\%$; alternativa Managed HSM 10.385,6 UF; matriz de sensibilidad del §4.2
reanclada en 8.018,96 / 8.492,16 / 8.965,36 UF con banda de ±5,57 % y cuadrantes asimétricos
en ±3,92 %.

La tabla de flujo vuelve a cuadrar en las tres direcciones: las diez filas suman 8.492,16 UF,
las cinco columnas suman 8.492,16 UF y ambos caminos coinciden.

**Propagación:** la cifra se actualizó en Persona 1 (subdocumento, Entregables 3 y 4 y guía
de defensa), Persona 6 (banco avanzado, subdocumento y `.tex`) y el manual operativo de
Persona 4.
