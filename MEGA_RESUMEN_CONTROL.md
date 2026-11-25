# MEGA RESUMEN — CONTROL 1 FEP (17:00)

> Todo lo que necesitas para hoy, en un solo lugar. Incluye la **estructura oficial**, los **5 temas** y los **2 casos reales resueltos** del control anterior (2025) con su pauta.
> Regla de oro del profe: **tenlo ORDENADO para que, cuando te pidan "cambiar una variable", solo cambies esa casilla, vuelvas a sumar y salga el número.**

---

# 0 · QUÉ ENTRA Y CÓMO SE PUNTÚA (aviso oficial)

**18 ítems · 225 puntos · 60 min · solo calculadora simple.**

| Tipo de ítem | Cant. | Puntaje | % |
|---|---|---|---|
| Alternativas de materia | 11 | 99 | 44% |
| Alternativas con desarrollo | 7 | 126 | 56% |

| Tema | Ítems | Puntaje | % |
|---|---|---|---|
| Arquitectura de Software | 3 | 36 | 16% |
| Requisitos, Alcance, Planificación y EDT | 5 | 63 | 28% |
| Estimación de Software | 4 | 54 | 24% |
| Gestión de los Riesgos | 3 | 36 | 16% |
| Sala de Servidores | 3 | 36 | 16% |

**Lectura clave**: el bloque más pesado es *Requisitos/Alcance/EDT* (28%), y el más "calculable" es *Estimación* (24%). Las "alternativas con desarrollo" son donde cae el cálculo de puntos de casos de uso.

---

# TEMA 1 · ARQUITECTURA DE SOFTWARE (3 ítems)

## 1.1 Lógica vs Física (cae seguro)

| | Arquitectura LÓGICA | Arquitectura FÍSICA |
|---|---|---|
| Organiza | el **software** (módulos, componentes, capas, servicios) | la **ejecución** (nodos, servidores, redes, almacenamiento) |
| Muestra | interfaces, integraciones, flujo de información | dónde se despliega cada componente lógico |
| Depende de | nada tecnológico (independiente del proveedor) | tecnología concreta, capacidad, ubicación |
| Artefacto | diagrama de componentes / contexto / módulos | diagrama de despliegue / topología de red |

> "Un diagrama de clases NO es arquitectura lógica, y una lista de servidores NO es arquitectura física." El puente entre ambas es una **tabla de correspondencia**: *"el módulo Facturación (lógico) se despliega en el clúster de apps, 2 instancias de 4 vCPU/8 GB (físico)"*.

## 1.2 Estilos arquitectónicos (saber qué es cada uno)

| Estilo | Idea en una frase |
|---|---|
| **Monolítico** | Todo el código acoplado en un solo paquete desplegable. |
| **Cliente-servidor** | Un cliente pide, un servidor responde. La forma más antigua de distribuido. |
| **En capas (3/N)** | Presentación, lógica de negocio y datos separadas en niveles. |
| **Microservicios** | Servicios pequeños, autónomos, desplegables por separado, que se comunican por API. |
| **Basado en eventos** | Componentes desacoplados que publican/consumen eventos vía un intermediario. |
| **Serverless** | Funciones que se ejecutan por evento, sin administrar servidores; se paga por uso. |

**Monolito — ventajas**: simplicidad inicial, depuración directa, menos latencia (llamadas en memoria), transacciones simples, menor costo. **Desventajas**: escalamiento limitado (se replica todo), acoplamiento fuerte, despliegues riesgosos, tecnología única, conflictos en equipos grandes.

## 1.3 Atributos de calidad (ISO/IEC 25010 — 9 características)

Idoneidad funcional · **Eficiencia de desempeño** · Compatibilidad · Capacidad de interacción (antes usabilidad) · **Fiabilidad** (disponibilidad, tolerancia a fallos) · **Seguridad** · **Mantenibilidad** · Flexibilidad (escalabilidad, antes portabilidad) · Seguridad operacional.

**Los 5 que "se compran y se venden"** (aparecen en las bases y se pagan):

| Atributo | Se mide en | Impacto en costo |
|---|---|---|
| Rendimiento | p95 de respuesta, transacciones/seg | Medio |
| **Disponibilidad** | uptime (99,5 / 99,9 / 99,99%) | **Alto** |
| Escalabilidad | usuarios concurrentes sin degradación | Medio |
| **Seguridad** | controles + resultados de pruebas | **Alto** |
| Mantenibilidad | tiempo de reparación, esfuerzo de cambio | se paga después |

> Regla práctica: **cada "nueve" adicional de disponibilidad multiplica complejidad y costo**. No comprometas 99,99% si el caso no lo exige.

## 1.4 Cómo se escribe un atributo (igual que un requisito)

❌ "El sistema será rápido / disponible / seguro / escalable." · ✅ "El 95% de las consultas responde en < 2 s con 500 usuarios concurrentes." / "99,9% de disponibilidad mensual en horario hábil."

**ADR (Architecture Decision Record)**: cada decisión se documenta como *contexto → alternativas → decisión → consecuencias*. "Una arquitectura no es un dibujo: es un conjunto de decisiones con consecuencias. 3 o 4 ADR bien escritos sostienen todo el capítulo."

---

# TEMA 2 · REQUISITOS, ALCANCE, PLANIFICACIÓN Y EDT (5 ítems)

## 2.1 Proyecto vs Operación · PMBOK

- **Proyecto** = temporal + resultado único. **Operación** = continua + repetitiva.
- PMBOK: **5 grupos** (Inicio, Planificación, Ejecución, Monitoreo y control, Cierre) · **10 áreas** · **49 procesos**. → *Los grupos NO son fases: se solapan.*
- **Triple restricción**: Alcance ↔ Tiempo ↔ Costo. Fijas dos, el tercero se obliga.

## 2.2 Requisitos

- Requisito = necesidad/condición que debe cumplir el sistema (IEEE 610.12). *El "cómo" es diseño, no requisito.*
- **Funcional** (qué hace) vs **No funcional** (bajo qué condiciones). → **Sin número, no es requisito: es intención.** ("rápido" ❌ / "p95 < 2 s con 500 usuarios" ✅)
- 4 actividades: **Extraer → Analizar → Especificar → Verificar** (ciclo).
- **FURPS+**: Funcionalidad, Usabilidad, Reliability, Performance, Soporte (+ implementación, interfaz, operaciones, empaquetado, legales).
- **SMART** (redactar): Specific, Measurable, Achievable, Result-oriented, Time-bound.
- **MoSCoW** (priorizar): Must, Should, Could, Won't.
- Buena ERS: no ambigua · completa · concisa · verificable · consistente · modificable · trazable · priorizada.

## 2.3 Alcance

- **Alcance del producto** (qué tendrá → lo valida el usuario) vs **alcance del proyecto** (todo el trabajo → lo aprueba el patrocinador).
- **Supuesto** = doy por cierto SIN verificar. **Restricción** = limitación CONOCIDA. ("Un supuesto no declarado es un riesgo asumido gratis.")
- **Scope creep** = el CLIENTE pide de a poquito (→ control de cambios). **Gold plating** = el PROVEEDOR regala funciones (→ entregar exactamente lo pedido).
- **Línea base del alcance** = enunciado del alcance + EDT + diccionario de la EDT. Solo cambia por control de cambios.

## 2.4 La EDT (WBS)

- Desglosar el trabajo en pedazos hasta poder estimar cada uno. El último nivel manejable = **paquete de trabajo**.
- **Regla del 100%**: los hijos suman exactamente el 100% del padre (menos = trabajo huérfano; más = duplicado).
- **Regla 8/80**: un paquete de trabajo dura entre 8 y 80 horas.
- **La EDT NO tiene fechas ni secuencia** (eso es el cronograma). Confundirlas es el error más frecuente.
- **RACI**: Responsible (ejecuta) · Accountable (aprueba, **uno solo**) · Consulted · Informed.

## 2.5 Cronograma

- **Esfuerzo ≠ Duración**: esfuerzo = horas-hombre (no cambia al sumar gente); duración = tiempo calendario. ("9 embarazadas no hacen un bebé en 1 mes.")
- **PERT (beta)**: `tE = (O + 4M + P) / 6` · desviación `σ = (P − O) / 6` · ±2σ = 95,45%.

## 2.6 Dependencias — PDM (¡lo que preguntaste!)

El método de diagramación por precedencia (PDM) enlaza cada actividad con su predecesora mediante **4 relaciones**. Se leen **siempre desde la predecesora hacia la sucesora**, y la sigla nombra primero el extremo de la predecesora.

| Sigla | Nombre | Regla | Ejemplo |
|---|---|---|---|
| **FS** | Fin → Inicio | B no empieza hasta que A **termine** | no se prueba (I) sin haber construido (G). **La más usada.** |
| **SS** | Inicio → Inicio | B no empieza hasta que A **empiece** | la migración empieza cuando empieza la integración. |
| **FF** | Fin → Fin | B no **termina** hasta que A termine | la documentación cierra cuando cierra la marcha blanca. |
| **SF** | Inicio → Fin | B no termina hasta que A **empiece** | el sistema viejo se apaga cuando el nuevo arranca. **La menos usada.** |

**Tip de control**: "¿cuál es la mejor dependencia para X?" → casi siempre **FS**. SF es la rara.

**Adelanto (lead) y retraso (lag)**: modificadores de la relación. Lead = anticipar la sucesora (signo **−**). Lag = espera (signo **+**). *"El lag es espera, no trabajo: no consume horas pero sí ocupa días del plazo."*

**Tipos de dependencia por origen**:
- **Obligatorias** (lógica dura): legal/contrato/naturaleza. No se alteran.
- **Discrecionales** (lógica blanda): mejores prácticas. **Solo estas se pueden reordenar para acortar.**
- **Externas**: dependen de terceros (se documentan como supuestos).
- **Internas**: bajo control del equipo.

**Ruta crítica**: camino más largo del diagrama de red; sus actividades tienen **holgura cero**. Holgura = inicio tardío − inicio temprano. (Recorres hacia adelante: inicio temprano = máx de finales tempranos; hacia atrás: final tardío = mín de inicios tardíos.)

**Compresión**: **Crashing** = más recursos → sube COSTO. **Fast-tracking** = paralelizar → sube RIESGO.

---

# TEMA 3 · ESTIMACIÓN DE SOFTWARE (4 ítems) ← LO MÁS IMPORTANTE

## 3.1 La cadena (no saltes eslabones)

**Tamaño → Esfuerzo → Plazo → Costo** (4 cosas distintas).

| Eslabón | Mide | Unidad |
|---|---|---|
| Tamaño | cuánta funcionalidad | PF / UCP |
| Esfuerzo | cuánto trabajo | horas |
| Plazo | cuánto calendario | semanas |
| Costo | cuánta plata | pesos |

## 3.2 Punto Función (Albrecht) — breve

5 categorías: **ILF** (interno 7/10/15), **EIF** (externo 5/7/10), **EI** (entrada 3/4/6), **EO** (salida CON cálculo 4/5/7), **EQ** (consulta SIN cálculo 3/4/6).
`FP = UFP × TCF`, con `TCF = 0,65 + 0,01 × Σ(14 factores)`.
**Trampa**: EO vs EQ → si el dato salió calculado/derivado es EO; si sale tal cual, EQ.

## 3.3 Punto de Casos de Uso (Karner) — LA RECETA

**Las 5 fórmulas, en orden** (memoriza: "suma, ajusta técnico, ajusta ambiente, multiplica, convierte"):

1. `UUCP = UAW + UUCW`
2. `TCF = 0,6 + 0,01 × Σ(peso × valor)`  ← habla del SISTEMA
3. `EF = 1,4 − 0,03 × Σ(peso × valor)`    ← habla del EQUIPO
4. `UCP = UUCP × TCF × EF`
5. `E = UCP × CF` (programación = 40%) → `Esfuerzo total = E ÷ 0,40` **(Lectura B del curso)**

### 3.3.1 Actores (UAW)
- Simple (otro sistema, API) = **1**
- Medio (protocolo/texto) = **2**
- Complejo (persona con GUI) = **3**

> Un actor es un **ROL**, no una persona: 5.000 vecinos = un solo actor "Vecino" (3 pts).

### 3.3.2 Casos de uso (UUCW) — por nº de transacciones
- Simple (1–3 transacciones) = **5**
- Medio (4–7) = **10**
- Complejo (8+) = **15**

> **Transacción** = viaje de ida y vuelta usuario↔sistema que termina cuando el sistema queda esperando el siguiente estímulo.

### 3.3.3 Pesos de los FACTORES TÉCNICOS (TCF) — tabla que DEBES tener a mano

| # | Factor técnico | Peso |
|---|---|---|
| T1 | Sistema distribuido | **2** |
| T2 | Rendimiento / tiempo de respuesta | 1 |
| T3 | Eficiencia del usuario final | 1 |
| T4 | Procesamiento interno complejo | 1 |
| T5 | Reutilización | 1 |
| T6 | Facilidad de instalación | **0,5** |
| T7 | Facilidad de uso | **0,5** |
| T8 | Portabilidad | **2** |
| T9 | Modificabilidad | 1 |
| T10 | Concurrencia | 1 |
| T11 | Seguridad | 1 |
| T12 | Acceso de terceros / integración | 1 |
| T13 | Entrenamiento especial | 1 |

> **Solo 4 pesos distintos de 1**: T1 y T8 valen **2**; T6 y T7 valen **0,5**. Todo lo demás vale 1. Cada valor va de 0 a 5.

### 3.3.4 Pesos de los FACTORES DE AMBIENTE (EF) — tabla que DEBES tener a mano

| # | Factor ambiental | Peso |
|---|---|---|
| E1 | Familiaridad con el proceso/modelo | **1,5** |
| E2 | Experiencia en la aplicación/dominio | **0,5** |
| E3 | Experiencia en orientación a objetos | 1 |
| E4 | Capacidad del analista líder | **0,5** |
| E5 | Motivación | 1 |
| E6 | Requisitos estables | **2** |
| E7 | Personal a tiempo parcial | **−1** |
| E8 | Dificultad del lenguaje | **−1** |

> **E7 y E8 tienen peso NEGATIVO (−1)**: un valor alto ahí es MALO (sube el esfuerzo). Cada valor va de 0 a 5 (3 = medio).

### 3.3.5 Factor de conversión (CF) — cuentas los "desfavorables"

1. Cuenta cuántos **E1–E6** valen **menos que 3**.
2. Cuenta cuántos **E7–E8** valen **más que 3**.
3. Suma (0 a 8) y aplica:

| Desfavorables | CF |
|---|---|
| **2 o menos** | **20 h/UCP** |
| **3 o 4** | **28 h/UCP** (+40%) |
| **5 o más** | **No se estima: se replantea** |

> El CF es el parámetro más sensible de todo el método: **20 → 28 sube el esfuerzo 40%** sin tocar una línea de alcance.

### 3.3.6 Distribución del esfuerzo
Análisis **10%** · Diseño **20%** · **Programación 40%** · Pruebas **15%** · Sobrecarga **15%**.
→ *"Programar es menos de la mitad del trabajo."*

---

## 3.4 EJEMPLO 1 RESUELTO — MediSys (Control 2025, Caso 1)

### Datos
- **Actores**: 3 APIs (simple) + 2 protocolos (medio) + 8 GUI (complejo).
- **15 casos de uso**: 1 simple, 5 medios, 9 complejos.
- **T**: T1=5, T2=4, T3=3, T4=5, T5=4, T6=2, T7=2, T8=4, T9=3, T10=5, T11=5, T12=4, T13=3.
- **E**: E1=2, E2=3, E3=2, E4=3, E5=3, E6=2, E7=3, E8=4.

### Paso a paso
```
UAW  = 3×1 + 2×2 + 8×3  = 3 + 4 + 24     = 31
UUCW = 1×5 + 5×10 + 9×15 = 5 + 50 + 135  = 190
UUCP = 31 + 190                          = 221

TCF:  SUMA = 5×2 + 4×1 + 3×1 + 5×1 + 4×1 + 2×0,5 + 2×0,5 + 4×2 + 3×1 + 5×1 + 5×1 + 4×1 + 3×1
            = 10 + 4 + 3 + 5 + 4 + 1 + 1 + 8 + 3 + 5 + 5 + 4 + 3
            = 56
      TCF  = 0,6 + 0,01×56               = 1,16

EF:   SUMA = 2×1,5 + 3×0,5 + 2×1 + 3×0,5 + 3×1 + 2×2 + 3×(−1) + 4×(−1)
            = 3 + 1,5 + 2 + 1,5 + 3 + 4 − 3 − 4
            = 8
      EF   = 1,4 − 0,03×8                = 1,16

UCP  = 221 × 1,16 × 1,16                = 297

Desfavorables: E1–E6 <3 → E1(2),E3(2),E6(2) = 3 ; E7–E8 >3 → E8(4) = 1 ; total = 4
CF   = 28 HH

E (programación) = 297 × 28             = 8.316 HH
Esfuerzo total   = 8.316 ÷ 0,40         = 20.790 HH
```

### La pregunta de "cambio de variable" (pregunta 7)
*"Si se optimiza el equipo mejorando E1 a 4, E3 a 4 y E5 a 5, ¿nuevo esfuerzo total?"*

**NO rehagas todo. Solo cambia esas casillas de la tabla de EF y vuelve a sumar:**

```
EF nueva:
E1: 2→4  → 4×1,5 = 6   (antes 3)
E3: 2→4  → 4×1   = 4   (antes 2)
E5: 3→5  → 5×1   = 5   (antes 3)
SUMA nueva = 6 + 1,5 + 4 + 1,5 + 5 + 4 − 3 − 4 = 15
EF  = 1,4 − 0,03×15 = 0,95

UCP = 221 × 1,16 × 0,95 = 244      ← TCF (1,16) NO cambia

Desfavorables nuevas: E1–E6 <3 → solo E6(2) = 1 ; E7–E8 >3 → E8(4) = 1 ; total = 2
CF  = 20 HH                         ← ¡el CF también baja!

E   = 244 × 20 = 4.880 HH
Total = 4.880 ÷ 0,40 = 12.200 HH
```

> **Lección clave**: al mejorar los factores E, cambian **dos cosas a la vez** — el EF (baja el UCP) **y** el CF (baja 28→20). El profe te hace el "cambio de variable" precisamente para ver si recuerdas volver a contar los desfavorables.

---

## 3.5 EJEMPLO 2 RESUELTO — AeroControl (Control 2025, Caso 2)

### Datos
- **Actores**: 4 APIs (simple) + 5 protocolos (medio) + 12 GUI (complejo).
- **25 casos de uso**: 0 simples, 5 medios, 20 complejos.
- **T**: T1=5, T2=5, T3=4, T4=5, T5=3, T6=1, T7=2, T8=5, T9=4, T10=5, T11=5, T12=3, T13=4.
- **E base**: E1=2, E2=1, E3=3, E4=2, E5=3, E6=1, E7=4, E8=3.
- **E optimizado**: E1=4, E2=4, E3=5, E4=5, E5=5, E6=3, E7=1, E8=2.

### Paso a paso (escenario base)
```
UAW  = 4×1 + 5×2 + 12×3 = 4 + 10 + 36    = 50
UUCW = 0×5 + 5×10 + 20×15 = 0 + 50 + 300 = 350
UUCP = 50 + 350                          = 400

TCF:  SUMA = 5×2 + 5×1 + 4×1 + 5×1 + 3×1 + 1×0,5 + 2×0,5 + 5×2 + 4×1 + 5×1 + 5×1 + 3×1 + 4×1
            = 10 + 5 + 4 + 5 + 3 + 0,5 + 1 + 10 + 4 + 5 + 5 + 3 + 4
            = 59,5
      TCF  = 0,6 + 0,01×59,5 = 1,195

EF base:
      SUMA = 2×1,5 + 1×0,5 + 3×1 + 2×0,5 + 3×1 + 1×2 + 4×(−1) + 3×(−1)
           = 3 + 0,5 + 3 + 1 + 3 + 2 − 4 − 3 = 5,5
      EF   = 1,4 − 0,03×5,5 = 1,235

UCP  = 400 × 1,195 × 1,235 = 590
CF   = 28 HH
E    = 590 × 28 = 16.520 HH      → Total = 41.300 HH
```

> **Nota de borde (importante)**: el escenario base de AeroControl cuenta con 5 factores desfavorables (E1, E2, E4, E6 < 3 y E7 > 3), lo que según la diapositiva sería "replantear". El profe, en la pauta 2025, igual usó **CF = 28**. Conclusión práctica: aplica la regla **estricta** (≥5 → replantear), pero si la alternativa solo ofrece 20 o 28, usa 28 en el borde. Cuando cambies los E, **vuelve a contar desfavorables**: en el optimizado bajan a 2 → CF = 20.

### Escenario optimizado (cambio de variable de TODOS los E)
```
EF opt:
      SUMA = 4×1,5 + 4×0,5 + 5×1 + 5×0,5 + 5×1 + 3×2 + 1×(−1) + 2×(−1)
           = 6 + 2 + 5 + 2,5 + 5 + 6 − 1 − 2 = 23,5
      EF   = 1,4 − 0,03×23,5 = 0,695

UCP(O) = 400 × 1,195 × 0,695 = 332
CF(O)  = 20 HH
E(O)   = 332 × 20 = 6.640 HH    → Total = 16.600 HH
```

### Preguntas comparativas que cayeron (patrón)
- **Reducción % del EF** = (1,235 − 0,695) / 1,235 = **44%**.
- **Reducción de esfuerzo** = 16.520 − 6.640 = **9.880 HH** (o 41.300 − 16.600 = 24.700 total).
- **Impacto de bajar T10 y T11 de 5 a 3**: quita (2+2)=4 a la SUMA del TCF → TCF 1,195 → 1,155 → ahorra **544 HH**.
- **Costo a USD 75/HH**: base 16.520×75 = **USD 1.239.000**; optimizado 6.640×75 = **USD 498.000**; ahorro 741.000 → la capacitación se justifica si cuesta menos de ese ahorro.

---

## 3.6 Los 6 errores que el profe descuenta

1. **Saltarse la cadena** (requisitos → precio directo).
2. **No declarar la lectura A/B** (E es total vs E es solo programación → diferencia 2,5×).
3. **No contar los desfavorables** para el CF (usan 20 "por costumbre").
4. **Usar 28 sin justificar** (falta el 40% de esfuerzo de más).
5. **Dividir horas por dotación** y creer que eso es el plazo (el plazo sale del cronograma).
6. **5 o más desfavorables y estimar igual** → el método dice "replantear" (vender al costo).

---

# TEMA 4 · GESTIÓN DE RIESGOS (3 ítems)

## 4.1 Las 3 palabras
- **Incertidumbre** = no sé (materia prima).
- **Riesgo** = evento INCIERTO con efecto (se gestiona con respuesta + reserva). *Todavía no pasa.*
- **Problema** = ya pasó (acción correctiva).

> Si puedes poner el verbo en pasado, NO es riesgo.

**Amenaza** (negativo) vs **Oportunidad** (positivo). Las oportunidades son la única forma legítima de bajar precio sin bajar alcance.

## 4.2 La fórmula estrella
**Exposición = Probabilidad × Impacto** (`E = P × I`).
**VME (Valor Monetario Esperado) = Probabilidad × Impacto (en $)**. → **Reserva de contingencia = Σ VME** de los riesgos aceptados.

## 4.3 Cómo se escribe un riesgo bien
> **"Dado que** \<causa cierta\> **entonces puede que** \<evento incierto\> **teniendo como consecuencia** \<efecto en un objetivo\>."

- "El equipo no tiene experiencia" = **CAUSA** (hecho, sin probabilidad). "…puede que el desarrollo demore 4 semanas" = **RIESGO**.

## 4.4 Las 5 estrategias ante AMENAZAS (¡la pregunta que mencionaste!)

| Estrategia | Qué hace | Ejemplo |
|---|---|---|
| **Escalar** | lo manda arriba (fuera de mi control) | normativa corporativa |
| **Evitar (eliminar)** | cambio el diseño para que NO exista | excluyo la integración |
| **Transferir** | se lo paso a un tercero (pago prima) | subcontrato al que mantiene el legado |
| **Mitigar** | bajo P o I (sin eliminar) | prueba de concepto temprana |
| **Aceptar** | reconozco y reservo (activo) o solo observo (pasivo) | riesgo de certificación |

*Mnemotecnia: "**E**n **E**l **T**rabajo **M**e **A**poyo" (Escalar–Evitar–Transferir–Mitigar–Aceptar).*

**Oportunidades**: escalar · **explotar** · compartir · **mejorar** · aceptar.

**Para elegir (2 preguntas)**: (1) ¿quién controla el riesgo? → nosotros: evitar/mitigar · tercero: transferir · nadie: escalar. (2) ¿la respuesta cuesta menos que el ahorro? → si no, aceptar.

## 4.5 Riesgo residual, secundario, disparador
- **Residual** = lo que queda DESPUÉS de la respuesta (se financia).
- **Secundario** = riesgo NUEVO que crea tu propia respuesta.
- **Disparador** = señal que activa el plan de contingencia.

## 4.6 Las 5 palancas de la licitación
**Consultar → Suponer → Excluir → Rediseñar → No ofertar.** (Un riesgo que no produjo ninguna de estas 5 = no fue gestionado, fue "mencionado".)

## 4.7 La escalera de costo (de más barato a más caro)
Consulta (gratis) → Supuesto → Exclusión → Decisión de arquitectura → Prueba de concepto → Reserva → Rehacer → Reparar en producción (carísimo).
*"Gestionar el riesgo = bajarlo de peldaño."*

---

# TEMA 5 · SALA DE SERVIDORES (3 ítems)

## 5.1 Redundancia (la letra lo dice todo)

| Config | Qué significa | Si falla un componente |
|---|---|---|
| **N** | justo lo necesario, sin repuesto | el servicio se cae |
| **N+1** | un repuesto | el repuesto asume; no hay caída |
| **2N** | dos sistemas completos e independientes | el segundo sigue solo (TIER IV) |
| **2(N+1)** | dos, cada uno con repuesto | se puede fallar y mantener a la vez |

> "Ojo con el trayecto: de poco sirve un segundo UPS si ambos alimentan el mismo tablero por el mismo ducto. **La redundancia también es de camino** — se verifica siguiendo el cable."

## 5.2 TIER (ANSI/TIA-942 / Uptime Institute) — la tabla que hay que memorizar

| | TIER I | TIER II | TIER III | TIER IV |
|---|---|---|---|---|
| Caminos de distribución | Uno | Uno | 1 activo + 1 alternativo | 2 activos |
| Componentes redundantes | No | N+1 | N+1 | 2(N+1) |
| Mantenimiento sin caída | No | No | Sí | Sí |
| Tolera falla imprevista | No | No | Parcialmente | Sí |
| Disponibilidad máx. | 99,671% | 99,741% | 99,982% | 99,995% |
| **Caída/año** | **≈28,8 h** | **≈22,7 h** | **≈1,6 h** | **≈0,4 h** |

> "El TIER no se hereda del proveedor: si tu servidor está en un datacenter TIER III pero el enlace de la sucursal es único, tu disponibilidad NO es TIER III."

## 5.3 PUE (Power Usage Effectiveness)

`PUE = Energía total de la instalación / Energía de los equipos TI`
- **Numerador** = todo (medido en el medidor de la eléctrica: servidores, red, storage, refrigeración, luz, pérdidas del UPS).
- **Denominador** = solo equipos TI (medido en las PDU).
- Ejemplo canónico: 50.000 kWh totales / 40.000 kWh TI = **PUE 1,25**.
- `DCiE = energía TI / energía total` (la misma cuenta al revés; en el ejemplo, 80%).
- **PUE 1,0 no existe**. Mientras más cerca de 1, mejor. Promedio mundial 2025 ≈ **1,54** (2007 era 2,5).

**Cómo se baja el PUE (ordenado por impacto)**: (1) confinar el pasillo frío + paneles ciegos en cada U vacía → (2) evitar recirculación (sellar piso técnico, tapar huecos) → (3) refrigeración de mejor tecnología (velocidad variable, free cooling) → (4) fuentes/luz/parásitos → (5) medir periódicamente.

## 5.4 Orden del diseño (y del presupuesto)
**Energía → Clima → Red → Servidores** (en ese orden). "Primero energía, después clima, después red, y solo entonces los servidores."

---

# DECÁLOGO FINAL (repaso de 2 minutos antes de entrar)

1. Proyecto = temporal + único. PMBOK: 5 grupos (no fases) · 10 áreas · 49 procesos.
2. Requisito sin número = intención. "Rápido" ❌ / "p95 < 2 s" ✅.
3. Alcance = decidir qué NO se hace. Scope creep (cliente) ≠ gold plating (proveedor).
4. EDT: regla 100% + 8/80 + **sin secuencia**. RACI: la "A" es única.
5. Dependencias: **FS (la normal), SS, FF, SF (la rara)**. Solo las discrecionales se reordenan.
6. Tamaño → Esfuerzo → Plazo → Costo. Esfuerzo ≠ duración. PERT = (O+4M+P)/6.
7. **UCP**: UUCP=UAW+UUCW · TCF=0,6+0,01Σ · EF=1,4−0,03Σ · UCP=UUCP×TCF×EF · E=UCP×CF · **total = E÷0,40**.
8. Pesos: actores 1/2/3 · CU 5/10/15 · **T1,T8=2; T6,T7=0,5** · **E6=2, E1=1,5, E2=E4=0,5, E7=E8=−1**. CF: ≤2→20, 3-4→28, ≥5→replantear.
9. Al cambiar un factor E: re-suma el EF **y vuelve a contar los desfavorables** (el CF puede cambiar).
10. Riesgo (puede pasar) ≠ problema (pasó). Exposición=P×I. Amenazas: **escalar/evitar/transferir/mitigar/aceptar**. TIER IV = 99,995% ≈ 0,4 h/año. PUE ≈ energía total / energía TI.

---

**Cómo estudiar en el tiempo que queda**: memoriza las dos tablas de pesos (T y E) y la receta de UCP → haz de nuevo los 2 ejemplos resueltos a mano con calculadora → practica el "cambio de variable" cambiando un solo E → repasa las 4 dependencias y los 4 TIER.
