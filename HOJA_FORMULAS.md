# HOJA DE FÓRMULAS Y SIGLAS — Repaso rápido

---

## TEMA 1 — PLANIFICACIÓN

### PERT / Tres valores
- Triangular: `tE = (O + M + P) / 3`
- Beta (PERT): `tE = (O + 4·M + P) / 6`
- Desviación: `σ = (P − O) / 6`
- Intervalos: **±1σ = 68,26% · ±2σ = 95,45% · ±3σ = 99,73%**

### Duración vs esfuerzo
- `Duración = Esfuerzo / (personas × horas por día)`

### Reglas de la EDT
- **Regla del 100%**: Σ hijos = 100% del padre.
- **Regla 8/80**: un paquete de trabajo dura entre 8 y 80 horas.

---

## TEMA 2 — ESTIMACIÓN

### Punto Función (Albrecht)
- `FP = UFP × TCF`
- `TCF = 0,65 + 0,01 × ΣFi` (14 factores, rango 0,65–1,35)

### Punto de Casos de Uso (Karner)
- `UUCP = UAW + UUCW`
- `TCF = 0,6 + 0,01 × Σ(peso × valor)`
- `EF = 1,4 − 0,03 × Σ(peso × valor)`
- `UCP = UUCP × TCF × EF`
- `E = UCP × CF`
- **Lectura B (curso)**: `Esfuerzo total = E ÷ 0,40`

### Pesos
- **Actores (UAW)**: simple 1 · medio 2 · complejo 3
- **Casos de uso (UUCW)**: simple (1–3 trans) 5 · medio (4–7) 10 · complejo (8+) 15

### Factor de conversión (CF) — factores desfavorables
- **≤ 2 → 20 h/UCP**
- **3–4 → 28 h/UCP**
- **≥ 5 → replantear el proyecto**

### Distribución del esfuerzo
- Análisis 10% · Diseño 20% · **Programación 40%** · Pruebas 15% · Sobrecarga 15%

---

## TEMA 3 — RIESGOS

### Fórmulas
- **Exposición = Probabilidad × Impacto**
- **VME = Probabilidad × Impacto** (en dinero)
- **Reserva de contingencia = Σ VME** de los riesgos cuantificados

### Zonas de exposición
- Crítica: P×I ≥ 0,40
- Alta: 0,20 – 0,40
- Media: 0,08 – 0,20
- Baja: < 0,08

### Cronograma (percentiles)
- Comprometer **P80**, planificar internamente **P50**.

---

## SIGLAS

### Planificación
- **PMBOK**: guía de fundamentos para la dirección de proyectos
- **PMI**: Project Management Institute
- **IEEE 610.12**: definición estándar de requisito
- **ERS**: Especificación de Requisitos del Software
- **FURPS+**: Funcionalidad, Usabilidad, Reliability, Performance, Soporte (+ implementación, interfaz, operaciones, empaquetado, legales)
- **SMART**: Specific, Measurable, Achievable, Result, Time
- **MoSCoW**: Must, Should, Could, Won't
- **EDT / WBS**: Estructura de Desglose del Trabajo
- **RACI**: Responsible, Accountable, Consulted, Informed
- **PDM**: método de diagramación por precedencia
- **CPM**: método de la ruta crítica
- **PERT**: estimación por tres valores
- **O / M / P**: optimista / más probable / pesimista

### Estimación
- **PF / FP**: punto función / function points
- **UFP**: puntos función sin ajustar
- **ILF / EIF**: archivo lógico interno / de interfaz externo
- **EI / EO / EQ**: entrada / salida / consulta externa
- **UAW**: peso de actores sin ajustar
- **UUCW**: peso de casos de uso sin ajustar
- **UUCP**: puntos de casos de uso sin ajustar
- **TCF**: factor de complejidad técnica
- **EF**: factor de ambiente
- **UCP**: puntos de casos de uso ajustados
- **CF**: factor de conversión (horas por punto)

### Riesgos
- **VME**: valor monetario esperado
- **RBS**: estructura de desglose de riesgos
- **P × I × E**: probabilidad, impacto, exposición
- **RTO / RPO**: tiempo / punto objetivo de recuperación

---

## FRASES CLAVE (último repaso)

- "Sin número, no es requisito: es una intención."
- "Lo que no se excluye por escrito se presume incluido."
- "Un supuesto no declarado es un riesgo asumido gratis."
- "Esfuerzo no es plazo; costo no es venta."
- "Programar es menos de la mitad del trabajo."
- "EF bajo = bueno."
- "Un riesgo que no cambió nada no fue gestionado: fue mencionado."
- "Gestionar el riesgo = bajarlo de peldaño."
