# Entregable 4: Índice Temático y Matriz de Distribución Multidimensional
**Asignatura:** ICI-5444 · Taller de Formulación de Proyectos Informáticos (PUCV)  
**Empresa N.º 10:** audIT Soluciones de Software SpA · **Tema:** TI-12  
**Caso:** Caso 10 — Transportes Curimón S.A.  
**Rol:** Persona 6 (*Assessment & Knowledge Verification Lead*)  

---

## 1. Matriz Cruzada de las 30 Preguntas (Tabla de Control Integral)

La siguiente tabla refleja exactamente los registros que se compilan de forma automática en el informe final a través de la macro `\indiceTematico` programada en `informe-ti12.sty`:

| N.º | Sección del Informe | Dificultad | Formato | Nivel Bloom | Subtema Oficial TI-12 |
| :---: | :--- | :---: | :---: | :---: | :--- |
| **P01** | 1.3 Ley 21.663 y ANCI | Básica | Selección múltiple | Recordar | Ley 21.663 y ciberseguridad |
| **P02** | 1.2 Ley 21.719 | Básica | Verdadero o Falso | Comprender | Ley 21.719 y datos personales |
| **P03** | 1.2 Ley 21.719 | Básica | Completar | Recordar | Ley 21.719 y datos personales |
| **P04** | 1.1 Estado de vigencia | Básica | Respuesta corta | Comprender | Verificación de vigencia |
| **P05** | 1.8 Normas certificables | Básica | Selección múltiple | Comprender | Normas técnicas certificables |
| **P06** | 1.4 Normativa complementaria | Básica | Verdadero o Falso | Recordar | Normativa chilena complementaria |
| **P07** | 1.7 Marco internacional | Básica | Completar | Recordar | Marco internacional (RGPD) |
| **P08** | 1.3 Ley 21.663 y ANCI | Básica | Respuesta corta | Comprender | Ley 21.663 y ciberseguridad |
| **P09** | 2.2 Herramientas GRC | Básica | Selección múltiple | Recordar | Herramientas de apoyo GRC |
| **P10** | 1.6 Transferencias internacionales | Básica | Verdadero o Falso | Comprender | Transferencias internacionales |
| **P11** | 1.8 Normas certificables | Básica | Completar | Recordar | Normas técnicas certificables |
| **P12** | 1.2 Ley 21.719 | Básica | Respuesta corta | Comprender | Ley 21.719 y datos personales |
| **P13** | 1.2 Ley 21.719 | Intermedia | Selección múltiple | Analizar | Ley 21.719 y Caso Curimón |
| **P14** | 3.1 Arquitectura | Intermedia | Verdadero o Falso | Aplicar | Arquitectura de cumplimiento |
| **P15** | 1.4 Normativa complementaria | Intermedia | Completar | Aplicar | Normativa laboral y GPS |
| **P16** | 3.2 Matriz de obligaciones | Intermedia | Respuesta corta | Analizar | Decisiones automatizadas |
| **P17** | 1.5 Privacidad desde el diseño | Intermedia | Selección múltiple | Aplicar | Privacidad desde el diseño |
| **P18** | 2.1 Marcos normativos | Intermedia | Verdadero o Falso | Analizar | Comparación de marcos |
| **P19** | 1.3 Ley 21.663 y ANCI | Intermedia | Completar | Analizar | Ley 21.663 y OIV |
| **P20** | 1.7 Marco internacional | Intermedia | Respuesta corta | Analizar | Marco internacional (IA Act) |
| **P21** | 3.2 Matriz de obligaciones | Intermedia | Selección múltiple | Aplicar | Matriz de obligaciones y SLAs |
| **P22** | 1.6 Transferencias internacionales | Intermedia | Verdadero o Falso | Aplicar | Transferencias (Mendoza) |
| **P23** | 3.2 Matriz de obligaciones | Intermedia | Completar | Aplicar | Seguridad técnica y cifrado |
| **P24** | 2.2 Herramientas GRC | Intermedia | Respuesta corta | Analizar | Herramientas de apoyo GRC |
| **P25** | 1.6 Transferencias internacionales | Avanzada | Selección múltiple | Evaluar | Nube y US CLOUD Act |
| **P26** | 3.3 Impacto económico | Avanzada | Verdadero o Falso | Evaluar | Modelo TCO y roles E-26 |
| **P27** | 3.1 Arquitectura | Avanzada | Completar | Sintetizar | Borrado criptográfico |
| **P28** | 4. Tendencias | Avanzada | Respuesta corta | Evaluar | Tendencias y prórrogas |
| **P29** | 2.1 Marcos normativos | Avanzada | Selección múltiple | Sintetizar | Comparación Chile vs. UE |
| **P30** | 3.3 Impacto económico | Avanzada | Verdadero o Falso | Evaluar | Modelo Gordon-Loeb |

---

## 2. Cobertura de Subtemas Obligatorios de la Ficha TI-12

Conforme a la Sección 3 de las Indicaciones y las directrices de `Division.md`, el cuestionario garantiza una presencia mínima proporcional en cada uno de los subtemas del informe:

```
┌──────────────────────────────────────────────────────────────────────────────────┐
│                   DISTRIBUCIÓN DE PREGUNTAS POR SUBTEMA TI-12                    │
├────────────────────────────────────────────────────┬───────────┬─────────────────┤
│ Subtema Oficial de la Ficha TI-12                  │ Preguntas │ N.º Preguntas   │
├────────────────────────────────────────────────────┼───────────┼─────────────────┤
│ 1. Ley 21.719 (Protección de Datos Personales)     │     6     │ P02, P03, P12,  │
│                                                    │           │ P13, P16, P17   │
│ 2. Ley 21.663 (Marco de Ciberseguridad y ANCI)     │     5     │ P01, P08, P18,  │
│                                                    │           │ P19, P28        │
│ 3. Privacidad y Seguridad desde el Diseño          │     5     │ P06, P14, P15,  │
│                                                    │           │ P23, P27        │
│ 4. Transferencias Internacionales y Región Cloud   │     4     │ P10, P21, P22,  │
│                                                    │           │ P25             │
│ 5. Marco Internacional (RGPD, NIS2, IA Act, CRA)   │     4     │ P07, P20, P24,  │
│                                                    │           │ P29             │
│ 6. Normas Certificables y Herramientas GRC         │     6     │ P04, P05, P09,  │
│                                                    │           │ P11, P26, P30   │
├────────────────────────────────────────────────────┼───────────┼─────────────────┤
│ TOTAL DE PREGUNTAS DEL CUESTIONARIO                │    30     │ Cobertura 100%  │
└────────────────────────────────────────────────────┴───────────┴─────────────────┘
```

---

## 3. Matriz de Cobertura por Secciones del Informe

Para verificar que no exista ninguna sección del informe huérfana de evaluación:

* **1.1 Estado de vigencia:** 1 pregunta (P04).
* **1.2 Ley 21.719:** 4 preguntas (P02, P03, P12, P13).
* **1.3 Ley 21.663 y ANCI:** 3 preguntas (P01, P08, P19).
* **1.4 Normativa complementaria:** 2 preguntas (P06, P15).
* **1.5 Privacidad desde el diseño:** 1 pregunta (P17).
* **1.6 Transferencias internacionales:** 3 preguntas (P10, P22, P25).
* **1.7 Marco internacional:** 2 preguntas (P07, P20).
* **1.8 Normas certificables:** 2 preguntas (P05, P11).
* **2.1 Marcos normativos:** 2 preguntas (P18, P29).
* **2.2 Herramientas GRC:** 2 preguntas (P09, P24).
* **3.1 Arquitectura:** 2 preguntas (P14, P27).
* **3.2 Matriz de obligaciones:** 3 preguntas (P16, P21, P23).
* **3.3 Impacto económico:** 2 preguntas (P26, P30).
* **4. Tendencias:** 1 pregunta (P28).

**Total:** 30 preguntas repartidas a lo largo de los 14 capítulos y subcapítulos sustantivos del informe de investigación.
