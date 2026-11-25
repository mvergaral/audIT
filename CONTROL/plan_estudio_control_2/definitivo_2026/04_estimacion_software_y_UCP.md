# Estimación de proyectos de software y puntos de caso de uso

## 1. Estimar no es adivinar

Una estimación es una predicción fundamentada en información incompleta. Su propósito es apoyar decisiones de alcance, presupuesto, plazo, capacidad y riesgo.

Una buena estimación debe declarar:

- qué se está estimando: tamaño, esfuerzo, duración o costo;
- método utilizado;
- supuestos y exclusiones;
- datos históricos o parámetros;
- rango de incertidumbre;
- fecha y responsable de la estimación.

### Cuatro conceptos que no deben mezclarse

| Concepto | Ejemplo |
|---|---|
| Tamaño | 103 puntos de caso de uso |
| Esfuerzo | 2.884 horas-persona |
| Duración | 7,5 meses |
| Costo | $86.520.000 |

Pasar de uno a otro requiere factores de productividad, capacidad, calendarios y tarifas. Por eso, decir “el sistema tiene 100 puntos, entonces dura 100 días” no tiene fundamento.

---

## 2. Familias de métodos de estimación

### 2.1 Juicio de expertos

Una o más personas estiman usando experiencia en proyectos semejantes.

**Conviene cuando:** la tecnología o dominio son especializados y todavía hay pocos datos cuantificables.

**Ventaja:** incorpora contexto que un modelo puede omitir.

**Riesgo:** anclaje, presión política, exceso de confianza o dependencia de una sola persona.

**Cómo mejorarlo:** usar Delphi o Wideband Delphi: varias personas estiman, explican diferencias y vuelven a estimar sin forzar una falsa unanimidad.

### 2.2 Estimación por analogía

Compara el proyecto con proyectos históricos similares y ajusta sus diferencias.

**Conviene cuando:** se necesita una aproximación temprana y existe un repositorio de proyectos realmente comparables.

**Es mejor que un modelo complejo** cuando los datos son escasos pero hay un caso histórico muy parecido.

**No conviene** copiar el valor de un proyecto que solo se parece superficialmente: misma cantidad de pantallas no significa misma integración, seguridad o calidad.

### 2.3 Estimación paramétrica o algorítmica

Usa relaciones matemáticas calibradas, por ejemplo:

```text
Esfuerzo = tamaño × productividad
```

o modelos como COCOMO, que relacionan tamaño y factores de costo.

**Conviene cuando:** existen mediciones consistentes y un parámetro con relación estable.

**Ventaja:** es repetible y permite análisis de sensibilidad.

**Riesgo:** una fórmula precisa aplicada a datos malos produce una respuesta precisamente equivocada.

### 2.4 Estimación descendente y ascendente

- **Top-down:** estima el proyecto completo y distribuye el valor. Es rápida y útil al inicio.
- **Bottom-up:** estima paquetes de trabajo o actividades y luego suma. Es más trazable cuando la EDT está detallada.

Bottom-up suele ser más defendible en planificación detallada, pero también puede omitir trabajo transversal si la EDT no cumple la regla del 100 %.

### 2.5 Descomposición

Divide un problema grande en componentes estimables. Puede aplicarse al producto —módulos, funciones o casos de uso— o al trabajo —paquetes de la EDT y actividades—.

Su fortaleza es obligar a reconocer partes olvidadas. Su debilidad es que una mala descomposición transmite sus omisiones a la suma final.

### 2.6 Puntos de función

Miden funcionalidad desde la perspectiva del usuario y no dependen directamente del lenguaje de programación.

Se consideran cinco tipos:

| Tipo | Sigla | Idea |
|---|---|---|
| Entrada externa | EI | Datos entran para mantener información o controlar el sistema |
| Salida externa | EO | Información sale con procesamiento o cálculo |
| Consulta externa | EQ | Entrada/salida simple sin procesamiento significativo |
| Archivo lógico interno | ILF | Datos lógicos mantenidos por la aplicación |
| Archivo de interfaz externo | EIF | Datos usados, pero mantenidos por otra aplicación |

Cada función se clasifica por complejidad y recibe un peso. Se obtiene un total no ajustado y, según la variante, se aplica un factor basado en características generales.

**Conviene cuando:** los requisitos funcionales están suficientemente definidos y se desea comparar productividad entre tecnologías.

**Limitación:** clasificar correctamente exige experiencia y puede ser pesado para estimaciones muy tempranas.

### 2.7 COCOMO

COCOMO estima esfuerzo a partir del tamaño del software y factores que influyen en el costo. COCOMO 81 se apoyaba principalmente en líneas de código; COCOMO II fue diseñado para prácticas modernas, reutilización y distintos niveles de información.

**Conviene cuando:** hay una medida de tamaño razonable y parámetros calibrados para el contexto.

**No conviene** tratar los coeficientes publicados como una ley universal. La productividad de una organización, sus herramientas y su dominio pueden ser muy diferentes.

### 2.8 Puntos de caso de uso, UCP

El método UCP estima tamaño a partir de actores y casos de uso, ajustándolo por factores técnicos y ambientales.

**Conviene cuando:** los casos de uso son el artefacto principal de requisitos y tienen un nivel de detalle consistente.

**No conviene cuando:** unos casos de uso describen tres pasos y otros contienen cincuenta a distinto nivel de abstracción; el conteo resultará engañoso.

---

## 3. Método de puntos de caso de uso paso a paso

La ruta de cálculo es:

```text
Actores → casos de uso → UUCP → factor técnico → factor ambiental → UCP → esfuerzo
```

### Paso 1: peso no ajustado de actores, UAW

| Actor | Criterio típico | Peso |
|---|---|---:|
| Simple | Otro sistema mediante API definida | 1 |
| Medio | Otro sistema mediante protocolo o interacción textual | 2 |
| Complejo | Persona mediante interfaz gráfica | 3 |

```text
UAW = suma(cantidad de actores × peso)
```

No se pondera por “importancia política”. Se pondera por la complejidad de interacción que usa el método.

### Paso 2: peso no ajustado de casos de uso, UUCW

Según la convención usada en las lecturas del curso:

| Caso de uso | Transacciones | Peso |
|---|---:|---:|
| Simple | 1 a 3 | 5 |
| Medio | 4 a 7 | 10 |
| Complejo | 8 o más | 15 |

```text
UUCW = suma(cantidad de casos de uso × peso)
```

Una transacción es un conjunto significativo de acciones que produce una respuesta observable; no es cada clic de la interfaz.

### Paso 3: puntos no ajustados

```text
UUCP = UAW + UUCW
```

### Paso 4: factor de complejidad técnica, TCF

Cada factor técnico recibe una influencia de 0 a 5. Esa influencia se multiplica por su peso.

| Factor | Descripción abreviada | Peso |
|---|---|---:|
| T1 | Sistema distribuido | 2 |
| T2 | Objetivos de rendimiento | 1 |
| T3 | Eficiencia del usuario final | 1 |
| T4 | Procesamiento interno complejo | 1 |
| T5 | Reutilización | 1 |
| T6 | Facilidad de instalación | 0,5 |
| T7 | Facilidad de uso | 0,5 |
| T8 | Portabilidad | 2 |
| T9 | Facilidad de cambio | 1 |
| T10 | Concurrencia | 1 |
| T11 | Seguridad especial | 1 |
| T12 | Acceso directo de terceros | 1 |
| T13 | Capacitación especial | 1 |

Si `TFactor` es la suma ponderada:

```text
TCF = 0,6 + 0,01 × TFactor
```

### Paso 5: factor ambiental, EF

También se evalúa cada factor de 0 a 5.

| Factor | Descripción abreviada | Peso |
|---|---|---:|
| E1 | Familiaridad con el proceso | 1,5 |
| E2 | Experiencia en la aplicación | 0,5 |
| E3 | Experiencia orientada a objetos | 1 |
| E4 | Capacidad del analista líder | 0,5 |
| E5 | Motivación | 1 |
| E6 | Requisitos estables | 2 |
| E7 | Personal de tiempo parcial | -1 |
| E8 | Lenguaje difícil | -1 |

Si `EFactor` es la suma ponderada:

```text
EF = 1,4 - 0,03 × EFactor
```

Los pesos negativos de E7 y E8 son intencionales. Una valoración alta en factores desfavorables reduce la suma ponderada y, mediante la fórmula, aumenta el factor ambiental y el tamaño ajustado.

### Paso 6: puntos de caso de uso ajustados

```text
UCP = UUCP × TCF × EF
```

### Paso 7: factor de conversión y esfuerzo

La lectura del curso propone examinar factores ambientales desfavorables. Como regla práctica del material:

| Cantidad de factores desfavorables | Conversión orientativa |
|---:|---:|
| 0 a 2 | 20 horas-persona/UCP |
| 3 a 4 | 28 horas-persona/UCP |
| 5 o más | Conviene replantear el proyecto |

```text
Esfuerzo de programación = UCP × factor de conversión
```

El factor de conversión ideal debe calibrarse con datos de la propia organización. Usar 20 o 28 sin validar es una aproximación académica, no una garantía contractual.

---

## 4. Ejemplo completo: SaludConecta

### 4.1 Actores

El equipo identifica:

- 4 actores simples: servicios con API definida;
- 3 actores medios: sistemas legados mediante protocolo;
- 2 actores complejos: médico y administrativo mediante interfaz gráfica.

```text
UAW = 4×1 + 3×2 + 2×3
UAW = 4 + 6 + 6 = 16
```

### 4.2 Casos de uso

- 4 simples;
- 5 medios;
- 3 complejos.

```text
UUCW = 4×5 + 5×10 + 3×15
UUCW = 20 + 50 + 45 = 115
```

```text
UUCP = 16 + 115 = 131
```

### 4.3 Ajuste técnico

Después de ponderar los 13 factores, el equipo obtiene `TFactor = 38`.

```text
TCF = 0,6 + 0,01×38 = 0,98
```

### 4.4 Ajuste ambiental

La suma ponderada ambiental es `EFactor = 20`.

```text
EF = 1,4 - 0,03×20 = 0,80
```

### 4.5 Tamaño ajustado

```text
UCP = 131 × 0,98 × 0,80
UCP = 102,704 ≈ 102,70
```

### 4.6 Esfuerzo

Hay tres factores ambientales desfavorables, por lo que se usa 28 horas-persona/UCP.

```text
Esfuerzo de programación = 102,704 × 28
Esfuerzo de programación = 2.875,712 horas-persona
```

Se puede redondear a **2.876 horas-persona**, pero conviene redondear al final y conservar decimales durante el cálculo.

### 4.7 Esfuerzo total del ciclo de vida

La lectura distribuye el esfuerzo de esta forma:

| Actividad | Porcentaje |
|---|---:|
| Requisitos | 10 % |
| Análisis y diseño | 20 % |
| Programación | 40 % |
| Pruebas | 15 % |
| Integración/implementación | 15 % |

Si 2.875,712 horas corresponden al 40 %:

```text
Esfuerzo total = 2.875,712 / 0,40
Esfuerzo total = 7.189,28 horas-persona
```

Distribución:

| Actividad | Horas aproximadas |
|---|---:|
| Requisitos | 718,93 |
| Análisis y diseño | 1.437,86 |
| Programación | 2.875,71 |
| Pruebas | 1.078,39 |
| Integración/implementación | 1.078,39 |
| **Total** | **7.189,28** |

### 4.8 De esfuerzo a duración

Con seis personas y 160 horas nominales por mes:

```text
Capacidad nominal mensual = 6 × 160 = 960 horas-persona/mes
Duración ideal = 7.189,28 / 960 = 7,49 meses
```

Pero esa duración supone, de forma poco realista, disponibilidad total, paralelización perfecta y cero interrupciones. Si solo el 80 % del tiempo es productivo para el proyecto:

```text
Capacidad efectiva = 960 × 0,80 = 768 horas-persona/mes
Duración aproximada = 7.189,28 / 768 = 9,36 meses
```

Este resultado revela un problema: el caso exige ocho meses. Las opciones son revisar alcance, productividad, secuencia, recursos, fecha o supuestos. **No corresponde reducir arbitrariamente la estimación para que coincida con la fecha deseada.**

### 4.9 De esfuerzo a costo

Si la tarifa promedio cargada es $30.000 por hora-persona:

```text
Costo de trabajo = 7.189,28 × $30.000
Costo de trabajo = $215.678.400
```

El presupuesto de $180 millones no alcanza para ese escenario. Esto no demuestra que el modelo sea infalible; demuestra que hay una inconsistencia que debe analizarse antes de comprometer el proyecto.

---

## 5. ¿Qué método elegir?

| Situación | Método inicial recomendable | Motivo |
|---|---|---|
| Solo existe una idea general | Analogía + expertos + rango | No hay detalle suficiente para un cálculo fino |
| Existe una EDT detallada | Bottom-up | Permite rastrear cada estimación al trabajo |
| Existen casos de uso consistentes | UCP | Usa artefactos ya disponibles y ajusta contexto |
| Requisitos funcionales estables | Puntos de función | Mide funcionalidad de forma independiente de tecnología |
| Hay muchos proyectos históricos medidos | Paramétrico calibrado | Aprovecha productividad real de la organización |
| Tecnología nueva y alta incertidumbre | Tres valores + prototipo + reserva | Explicita incertidumbre y obtiene aprendizaje |

La práctica más sólida es **triangular métodos**: por ejemplo, UCP + estimación ascendente + juicio de expertos. Si dan resultados muy distintos, no se promedian a ciegas; se investiga qué supuesto explica la diferencia.

---

## 6. Incertidumbre, precisión y compromiso

Una estimación temprana debe presentarse como rango. A medida que se aclara alcance y se obtienen datos, el rango puede estrecharse.

Ejemplo:

```text
Estimación inicial: 7 a 11 meses
Después del prototipo: 8 a 9,5 meses
Compromiso aprobado: 9 meses + reserva definida
```

Agregar decimales no crea exactitud. “9,36 meses” es el resultado del modelo; para una decisión conviene comunicar supuestos y un rango.

---

## 7. Errores típicos de control

1. **Confundir tamaño con esfuerzo.** Los UCP no son horas.
2. **Confundir esfuerzo con duración.** La duración depende de recursos, secuencia y calendarios.
3. **Contar clics como transacciones.** Se deben contar intercambios significativos.
4. **Clasificar actores por relevancia.** Se clasifican por mecanismo de interacción.
5. **Aplicar 20 HH/UCP siempre.** El factor depende de las condiciones ambientales y, en la vida real, de la calibración histórica.
6. **Olvidar que programación representa 40 %.** Si se pide esfuerzo total, no se entrega solo programación.
7. **Redondear en cada paso.** Puede acumular errores.
8. **Ajustar la cifra para obedecer al presupuesto.** El presupuesto es una restricción, no evidencia de esfuerzo.
9. **Usar un modelo sin declarar supuestos.** La cifra deja de ser defendible.

---

## 8. Autoevaluación

1. Explica la diferencia entre tamaño, esfuerzo, duración y costo.
2. ¿Por qué una estimación bottom-up puede ser más precisa, pero no necesariamente correcta?
3. ¿Cuándo preferirías analogía en lugar de UCP?
4. ¿Qué representan EI, EO, EQ, ILF y EIF?
5. ¿Por qué UCP requiere casos de uso escritos al mismo nivel?
6. Un actor humano que usa una interfaz gráfica, ¿qué peso recibe?
7. Un caso de uso de seis transacciones, ¿qué peso recibe?
8. Si UUCP = 90, TCF = 1,05 y EF = 0,90, calcula UCP.
9. Si UCP = 85 y corresponde usar 28 HH/UCP, calcula programación y esfuerzo total con la distribución del curso.
10. ¿Qué decisión tomarías si tres métodos producen 4, 7 y 9 meses?

