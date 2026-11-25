# PMBOK 08 — Gestión de la calidad

## 1. Qué significa calidad

Calidad es el grado en que un conjunto de características inherentes cumple los requisitos.

No significa “lo más caro”, “lo más sofisticado” ni “sin ningún defecto imaginable”. Un producto de alta calidad satisface de manera consistente los requisitos y es adecuado para su uso.

### Calidad versus grado

- **Calidad:** cumplimiento de requisitos.
- **Grado:** categoría asignada a productos con el mismo uso funcional, pero distintas características técnicas.

Un teléfono básico puede ser de grado bajo y alta calidad si cumple perfectamente sus especificaciones. Un teléfono premium con fallas frecuentes es de grado alto y baja calidad.

En SaludConecta, una versión inicial con pocas funciones puede ser de menor grado, pero debe cumplir seguridad, exactitud y rendimiento comprometidos.

---

## 2. Ideas que suelen confundirse

### Prevención versus inspección

- **Prevención:** evitar que el defecto se produzca. Ejemplo: estándares de código, capacitación, diseño seguro.
- **Inspección:** encontrar el defecto antes de entregar. Ejemplo: revisión o prueba.

Prevenir suele ser menos costoso que corregir después, pero no elimina la necesidad de verificar resultados.

### Muestreo por atributos versus variables

- **Atributos:** el resultado cumple/no cumple o tiene/no tiene defecto.
- **Variables:** se mide en una escala continua, como 1,8 segundos de respuesta.

### Tolerancias versus límites de control

- **Tolerancia o especificación:** rango de resultados aceptables para el cliente o requisito.
- **Límite de control:** frontera estadística del comportamiento estable de un proceso.

Un proceso puede estar bajo control estadístico y aun producir resultados fuera de especificación: es estable, pero incapaz. También puede cumplir temporalmente la especificación y estar fuera de control por una causa especial.

### Exactitud versus precisión

- **Exactitud:** cercanía al valor correcto.
- **Precisión:** resultados cercanos entre sí.

Un proceso puede ser muy preciso pero consistentemente equivocado.

---

## 3. Los tres procesos del capítulo 8

| Proceso | En qué se concentra | Pregunta |
|---|---|---|
| 8.1 Planificar la gestión de la calidad | Estándares, métricas y actividades | ¿Qué significa calidad y cómo la lograremos? |
| 8.2 Gestionar la calidad | Procesos, auditorías y mejora | ¿Nuestros procesos son adecuados y se están usando? |
| 8.3 Controlar la calidad | Resultados y entregables | ¿El producto realmente cumple? |

Una forma de recordarlo:

```text
Planificar = definir la vara
Gestionar = mejorar cómo trabajamos
Controlar = medir lo producido
```

---

## 4. Planificar la gestión de la calidad

Se identifican los requisitos y estándares relevantes y se documenta cómo se demostrará su cumplimiento.

### Preguntas que debe responder el plan

- ¿Qué estándares legales, organizacionales o técnicos aplican?
- ¿Qué métricas se usarán y cuál es su objetivo?
- ¿Qué revisiones, pruebas y auditorías se harán?
- ¿Quién es responsable?
- ¿Qué herramientas, ambientes y datos se requieren?
- ¿Cómo se informarán defectos y no conformidades?
- ¿Qué costo de calidad se aceptará?

### Técnicas relevantes

- juicio de expertos;
- recopilación de datos mediante entrevistas, lluvia de ideas y benchmarking;
- análisis costo-beneficio;
- análisis del costo de la calidad;
- toma de decisiones multicriterio;
- diagramas de flujo, modelos lógicos, matrices y mapas mentales;
- planificación de pruebas e inspecciones;
- reuniones.

### Benchmarking

Compara prácticas o resultados con proyectos internos o externos para identificar niveles alcanzables y mejoras.

Es útil cuando no se sabe qué objetivo es razonable. No conviene copiar una métrica sin considerar que otra empresa puede tener distinto producto, volumen o riesgo.

### Análisis costo-beneficio

Compara el beneficio esperado de una actividad de calidad con su costo.

Ejemplo: automatizar regresión cuesta $5 millones, pero se espera evitar $9 millones de retrabajo y reducir dos semanas. Es favorable si los supuestos son creíbles.

---

## 5. Costo de la calidad, COQ

El costo de calidad incluye lo invertido para conformidad y lo perdido por no conformidad.

| Grupo | Tipo | Ejemplos |
|---|---|---|
| Conformidad | Prevención | Capacitación, estándares, diseño, automatización preventiva |
| Conformidad | Evaluación | Pruebas, inspecciones, auditorías, revisión |
| No conformidad | Falla interna | Retrabajo y defectos encontrados antes de entregar |
| No conformidad | Falla externa | Soporte, garantías, multas, pérdida de reputación después de entregar |

La idea no es gastar infinitamente en pruebas, sino encontrar un equilibrio. Normalmente es preferible mover esfuerzo desde fallas externas hacia prevención y evaluación temprana.

Ejemplo:

- prevenir un defecto de privacidad durante diseño cuesta 10 horas;
- detectarlo en pruebas puede costar 80 horas;
- descubrirlo en producción puede implicar cientos de horas, notificación legal y daño reputacional.

---

## 6. Métricas de calidad

Una métrica debe ser operacional: debe decir qué se mide, cómo, con qué unidad y cuál es el objetivo.

| Necesidad | Métrica útil | Criterio ejemplo |
|---|---|---|
| Rendimiento | Percentil 95 del tiempo de respuesta | ≤ 2 s con 500 usuarios concurrentes |
| Confiabilidad | Disponibilidad mensual | ≥ 99,5 % |
| Defectos | Densidad de defectos | ≤ 0,4 defectos críticos por módulo |
| Eficacia de pruebas | Defectos escapados | ≤ 2 % de defectos detectados tras liberar |
| Cobertura | Cobertura de requisitos | 100 % de requisitos críticos con prueba |
| Aceptación | Casos de aceptación aprobados | 100 % críticos y ≥ 95 % total |
| Reproceso | Horas de retrabajo | ≤ 8 % del esfuerzo mensual |

“El sistema debe ser rápido” no es una métrica. “El 95 % de consultas responde en máximo dos segundos bajo 500 usuarios” sí puede probarse.

### Plan de calidad de SaludConecta

| Objetivo | Métrica | Método | Momento | Responsable |
|---|---|---|---|---|
| Evitar exposición de datos | Hallazgos críticos de seguridad | Prueba y revisión | Antes de cada liberación | Encargado seguridad |
| Responder oportunamente | P95 de latencia | Prueba de carga | Fin de integración | Líder técnico |
| Asegurar trazabilidad | Requisitos críticos con caso de prueba | Revisión de matriz | Semanal | QA |
| Lograr aceptación | Casos UAT aprobados | Prueba de usuario | Antes del cierre | Dueño de producto |

---

## 7. Gestionar la calidad

Gestionar la calidad convierte el plan en actividades ejecutables y examina si los procesos son adecuados. Tiene orientación de **aseguramiento, aprendizaje y mejora**.

### Actividades frecuentes

- auditorías de calidad;
- análisis de procesos;
- diseño para X: confiabilidad, seguridad, mantenibilidad, usabilidad, etc.;
- resolución estructurada de problemas;
- análisis de causa raíz;
- mejora de procesos;
- preparación de informes de calidad.

### Auditoría

Una auditoría revisa si las actividades cumplen políticas, procedimientos y procesos definidos, y busca buenas prácticas o brechas.

No es lo mismo que probar el producto. Una auditoría puede comprobar que el equipo aplica revisión de código; la prueba comprueba si una función se comporta como debe.

### Diseño para X

Se incorporan atributos desde el diseño, por ejemplo:

- seguridad;
- confiabilidad;
- mantenibilidad;
- facilidad de prueba;
- usabilidad;
- disponibilidad.

Es mejor diseñar la seguridad desde el inicio que intentar “agregarla” al final mediante pruebas.

### Resolución de problemas y causa raíz

Secuencia útil:

1. definir el problema con datos;
2. distinguir síntomas de causas;
3. generar causas posibles;
4. verificar la causa raíz;
5. diseñar y ejecutar solución;
6. comprobar eficacia.

Aplicar una solución al síntoma puede reducir el problema temporalmente, pero permitir su repetición.

### Salidas importantes

- informes de calidad;
- documentos de prueba y evaluación;
- solicitudes de cambio;
- actualizaciones al plan y documentos;
- mejoras recomendadas.

---

## 8. Controlar la calidad

Controlar la calidad monitorea y registra resultados de actividades de calidad para evaluar desempeño y asegurar que las salidas sean completas, correctas y adecuadas.

### Herramientas y técnicas frecuentes

- listas de verificación;
- hojas de verificación;
- muestreo estadístico;
- cuestionarios y encuestas;
- revisión de desempeño;
- análisis de causa raíz;
- inspección;
- pruebas/evaluaciones del producto;
- diagramas y gráficos.

### Lista de verificación versus hoja de verificación

- **Checklist:** recuerda elementos que deben comprobarse.
- **Check sheet:** formulario estructurado para contar y clasificar datos observados.

Ejemplo: una checklist pregunta si se revisó autenticación; una check sheet registra cuántos defectos de autenticación aparecieron por versión.

### Muestreo estadístico

Se inspecciona una parte representativa en vez del 100 %.

Es conveniente cuando inspeccionar todo es costoso o destructivo. No conviene para una condición crítica donde un solo incumplimiento es inaceptable, salvo que la norma y el riesgo permitan muestreo.

### Inspección y prueba

- **Inspección:** examina si un resultado cumple estándares; puede ser visual, documental o técnica.
- **Prueba:** ejecuta el producto o componente bajo condiciones definidas para evaluar su comportamiento.

### Salidas clave

- mediciones de control de calidad;
- entregables verificados;
- información de desempeño;
- solicitudes de cambio;
- actualizaciones.

Un entregable que pasa Controlar la Calidad queda **verificado**. Luego, Validar el Alcance busca la **aceptación formal** del cliente.

---

## 9. Las siete herramientas básicas de calidad

### 9.1 Diagrama causa–efecto o Ishikawa

Organiza causas posibles de un problema. Es útil antes de decidir una solución.

Para latencia alta se pueden explorar categorías como personas, proceso, plataforma, datos, red y medición.

### 9.2 Diagrama de flujo

Representa pasos, decisiones y recorridos. Ayuda a detectar cuellos de botella, retrabajo y puntos de control.

### 9.3 Hoja de verificación

Recoge datos de manera uniforme. Es especialmente útil antes de elaborar histogramas o Pareto.

### 9.4 Diagrama de Pareto

Ordena categorías de mayor a menor frecuencia o impacto y ayuda a concentrarse en las “pocas causas vitales”.

No prueba causalidad. La categoría más frecuente no siempre es la de mayor severidad.

### 9.5 Histograma

Muestra la distribución de datos. Permite observar forma, dispersión, concentración y valores extremos.

### 9.6 Gráfico de control

Muestra el comportamiento de un proceso a través del tiempo con línea central y límites de control.

- variación común: inherente al sistema;
- variación especial: señal no habitual que debe investigarse.

Una señal puede ser un punto fuera de límites o un patrón no aleatorio. Los límites de control se calculan a partir del proceso; no son lo mismo que requisitos del cliente.

### 9.7 Diagrama de dispersión

Muestra posible relación entre dos variables, como complejidad de módulo y defectos.

Correlación no demuestra causalidad. Puede orientar una investigación, no cerrarla.

---

## 10. Integración con alcance

Ésta es una comparación clave para el control:

| Proceso | Quién mira principalmente | Qué pregunta | Resultado |
|---|---|---|---|
| Gestionar la Calidad | Equipo/procesos | ¿Trabajamos con procesos adecuados? | Mejora e informes |
| Controlar la Calidad | Equipo técnico/QA | ¿El entregable cumple especificaciones? | Entregable verificado |
| Validar el Alcance | Cliente/patrocinador | ¿Acepta formalmente el entregable? | Entregable aceptado |

Un producto puede superar pruebas técnicas y no ser aceptado porque no responde a la necesidad acordada. También puede gustarle al usuario, pero no cumplir un requisito legal; por eso se necesitan ambos controles.

---

## 11. Ejemplo de decisión

SaludConecta registra 100 defectos:

- 52 por validaciones de datos;
- 21 por integración;
- 12 por permisos;
- 9 por interfaz;
- 6 por documentación.

Pareto sugiere comenzar por validaciones de datos, que representan 52 %. El equipo usa Ishikawa y descubre que las reglas están duplicadas en cinco módulos. La respuesta adecuada no es solo corregir 52 defectos: también centralizar reglas, agregar pruebas automatizadas y actualizar el estándar de diseño.

Aquí se combinan:

- **Controlar Calidad:** medir y clasificar defectos;
- **Gestionar Calidad:** corregir la causa del proceso/diseño;
- **Control Integrado de Cambios:** aprobar cambios relevantes a arquitectura o línea base.

---

## 12. Errores típicos de control

1. Confundir alta calidad con muchas funcionalidades.
2. Definir métricas subjetivas como “bueno” o “rápido”.
3. Dejar toda la calidad para las pruebas finales.
4. Confundir auditoría de proceso con prueba del producto.
5. Confundir límite de control con especificación.
6. Interpretar correlación como causalidad.
7. Corregir defectos sin investigar causas recurrentes.
8. Confundir entregable verificado con entregable aceptado.
9. Pensar que prevención elimina toda inspección.
10. Tratar los costos de fallas externas como inevitables.

---

## 13. Autoevaluación

1. ¿Cómo puede un producto de grado bajo tener alta calidad?
2. Da un ejemplo de prevención y uno de evaluación en SaludConecta.
3. ¿Qué diferencia existe entre tolerancia y límite de control?
4. Clasifica capacitación, prueba, retrabajo y garantía dentro del COQ.
5. Convierte “el sistema debe ser rápido” en una métrica verificable.
6. ¿Qué diferencia hay entre Gestionar y Controlar la Calidad?
7. ¿Para qué usarías Pareto y para qué Ishikawa?
8. ¿Por qué un proceso estable puede producir resultados inaceptables?
9. ¿Qué significa que un entregable esté verificado pero no aceptado?
10. ¿Cuándo sería peligroso usar muestreo?

