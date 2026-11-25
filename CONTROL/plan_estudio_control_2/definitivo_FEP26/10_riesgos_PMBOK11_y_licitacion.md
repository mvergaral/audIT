# PMBOK 11 — Gestión de los riesgos

## 1. Qué es un riesgo

Un riesgo es un evento o condición incierta que, si ocurre, tiene un efecto positivo o negativo sobre uno o más objetivos del proyecto.

Tres ideas son esenciales:

1. **Es incierto:** si ya ocurrió, es un problema o incidente, no un riesgo futuro.
2. **Tiene una causa y una consecuencia:** no basta escribir “retraso”.
3. **Puede ser amenaza u oportunidad:** riesgo no significa exclusivamente peligro.

Ejemplo bien redactado:

> Debido a que el laboratorio aún no congela la versión de su API (**causa**), podría cambiar el contrato durante el desarrollo (**evento**), provocando retrabajo y retraso en la integración (**efecto**).

“La API es mala” no es una formulación útil: mezcla opinión con un problema poco medible.

---

## 2. Riesgo individual y riesgo global

- **Riesgo individual:** evento o condición incierta específica.
- **Riesgo general del proyecto:** efecto de la incertidumbre total sobre el proyecto completo, incluidas fuentes que no se capturan como eventos aislados.

SaludConecta puede tener riesgos individuales pequeños, pero un riesgo global alto por requisitos inestables, tecnología nueva y fecha regulatoria rígida.

### Actitud frente al riesgo

| Concepto | Pregunta |
|---|---|
| Apetito | ¿Cuánta incertidumbre estamos dispuestos a perseguir o aceptar para obtener valor? |
| Tolerancia | ¿Qué variación general puede soportar la organización? |
| Umbral | ¿Desde qué valor se requiere actuar o escalar? |

Ejemplo: la organización puede aceptar hasta cinco días de variación; sobre ese umbral, el riesgo se eleva al comité.

---

## 3. Los siete procesos del capítulo 11

| Proceso | Pregunta principal | Resultado característico |
|---|---|---|
| 11.1 Planificar la gestión de riesgos | ¿Cómo gestionaremos el riesgo? | Plan de gestión de riesgos |
| 11.2 Identificar los riesgos | ¿Qué incertidumbres existen? | Registro e informe de riesgos iniciales |
| 11.3 Análisis cualitativo | ¿Cuáles requieren más atención? | Priorización actualizada |
| 11.4 Análisis cuantitativo | ¿Qué efecto numérico conjunto podrían tener? | Exposición y probabilidades cuantificadas |
| 11.5 Planificar respuestas | ¿Qué haremos frente a cada riesgo prioritario? | Respuestas, dueños y reservas |
| 11.6 Implementar respuestas | ¿Se están ejecutando las acciones acordadas? | Acciones realizadas y cambios |
| 11.7 Monitorear los riesgos | ¿Cambió la exposición y aparecieron riesgos nuevos? | Estado, tendencias y efectividad |

Los procesos son iterativos. Identificar riesgos una sola vez al inicio es insuficiente.

---

## 4. Planificar la gestión de los riesgos

El plan establece el enfoque antes de evaluar riesgos particulares. Suele definir:

- metodología y herramientas;
- funciones y responsabilidades;
- presupuesto y calendario de actividades de riesgo;
- categorías mediante una RBS;
- escalas de probabilidad e impacto;
- matriz de probabilidad e impacto;
- umbrales de las partes interesadas;
- formatos de informes y seguimiento.

### Estructura de desglose de riesgos, RBS

Ejemplo para SaludConecta:

```text
1. Técnicos
   1.1 Integración
   1.2 Seguridad
   1.3 Rendimiento
2. Gestión
   2.1 Estimación
   2.2 Recursos
3. Comerciales
   3.1 Proveedores
   3.2 Contratos
4. Externos
   4.1 Regulación
   4.2 Disponibilidad del laboratorio
```

La RBS ayuda a buscar sistemáticamente. No garantiza que todos los riesgos estén en la lista.

---

## 5. Identificar los riesgos

### Fuentes y técnicas

- revisión de documentos, supuestos y restricciones;
- entrevistas y talleres;
- lluvia de ideas;
- listas de verificación y listas de estímulo;
- análisis de causa raíz;
- análisis FODA;
- revisión de lecciones aprendidas;
- análisis de interfaces y dependencias.

### ¿Cuándo conviene cada técnica?

| Técnica | Es útil cuando | Precaución |
|---|---|---|
| Lista de verificación | Hay experiencia repetida | Puede impedir pensar en riesgos nuevos |
| Entrevista | El conocimiento está distribuido entre expertos | Sesgo del entrevistado |
| Taller | Se necesitan perspectivas cruzadas | Requiere facilitación |
| Causa raíz | Varios síntomas parecen relacionados | No confundir causa con evento |
| FODA | Se busca conectar contexto interno y externo | Puede quedarse demasiado general |

### Registro e informe de riesgos

El **registro** contiene riesgos individuales: descripción, categoría, causas, respuestas potenciales, dueño y estado. El **informe de riesgos** resume el riesgo general y la distribución, tendencias y exposición agregada.

Ejemplo inicial:

| ID | Riesgo | Categoría | Dueño |
|---|---|---|---|
| R1 | Cambio de API causa retrabajo | Técnico/externo | Líder integración |
| R2 | Datos de prueba contienen información sensible | Seguridad | Encargado seguridad |
| R3 | Automatización reduce tiempo de regresión | Oportunidad técnica | Líder QA |

El dueño del riesgo vigila y coordina; el dueño de una respuesta puede ejecutar una acción específica.

---

## 6. Análisis cualitativo

Su objetivo es priorizar rápidamente los riesgos individuales para decidir cuáles requieren respuesta o análisis cuantitativo.

### Matriz de probabilidad e impacto

Ejemplo numérico simple:

```text
Exposición = probabilidad × impacto
```

Si la probabilidad de cambio de API es 0,6 y el impacto de costo es $20 millones:

```text
Exposición monetaria simple = 0,6 × $20.000.000 = $12.000.000
```

En análisis cualitativo también pueden usarse escalas ordinales como 1 a 5. La organización define qué combinaciones son bajas, medias o altas.

> Multiplicar escalas ordinales sirve para priorizar bajo reglas definidas, pero no convierte automáticamente el resultado en dinero ni en una probabilidad real.

### Otros criterios de priorización

- calidad de los datos;
- urgencia: cuánto tiempo queda para responder;
- proximidad: cuándo podría ocurrir;
- latencia o dormancia: cuánto tarda en sentirse el efecto;
- detectabilidad;
- manejabilidad y controlabilidad;
- conectividad con otros riesgos;
- impacto estratégico;
- propincuidad: cuánto preocupa a los interesados.

Un riesgo de impacto alto pero muy detectable y controlable puede requerir un tratamiento distinto de otro menos visible que se materializa sin advertencia.

### Ejemplo de matriz para SaludConecta

Escala 1 a 5:

| Riesgo | Prob. | Impacto | Puntaje | Prioridad |
|---|---:|---:|---:|---|
| R1 Cambio de API | 4 | 5 | 20 | Alta |
| R2 Fuga de datos de prueba | 2 | 5 | 10 | Alta por umbral de seguridad |
| R3 Automatizar regresión | 3 | 4 | 12 | Oportunidad alta |
| R4 Ausencia breve de analista | 2 | 2 | 4 | Baja |

R2 demuestra que el puntaje no sustituye el criterio: seguridad puede tener un umbral especial que obliga a tratarlo aunque la probabilidad sea menor.

---

## 7. Análisis cuantitativo

No todos los proyectos lo requieren con la misma profundidad. Conviene cuando el proyecto es grande, complejo, estratégico o necesita responder preguntas como:

- ¿Cuál es la probabilidad de terminar antes de ocho meses?
- ¿Qué reserva de costo entrega un 80 % de confianza?
- ¿Qué variable explica mayor parte de la incertidumbre?

### Valor monetario esperado, EMV

```text
EMV = probabilidad × impacto monetario
```

Las amenazas usan impacto negativo; las oportunidades, positivo.

Ejemplo:

- 40 % de probabilidad de perder $15 millones: `0,40 × -15 = -$6 millones`.
- 30 % de probabilidad de ahorrar $10 millones: `0,30 × 10 = +$3 millones`.
- EMV neto: `-$3 millones`.

El EMV no significa que el proyecto perderá exactamente $3 millones. Es un valor esperado útil para decisiones repetidas o para combinar ramas.

### Árbol de decisiones

Supón dos opciones para la integración:

**Opción A: construir directamente**

- 60 % de éxito: costo $8 millones;
- 40 % de falla: costo total $28 millones por retrabajo.

```text
Costo esperado A = 0,60×8 + 0,40×28 = $16 millones
```

**Opción B: hacer prototipo**

- prototipo cuesta $4 millones;
- luego 85 % de éxito con $8 millones adicionales;
- 15 % de falla con $28 millones adicionales.

```text
Costo esperado B = 4 + 0,85×8 + 0,15×28
Costo esperado B = $15 millones
```

Por valor esperado, B es preferible. Además entrega aprendizaje anticipado. Sin embargo, la decisión también debe considerar plazo y tolerancia al peor caso.

### Simulación Monte Carlo

Se asignan distribuciones a duraciones o costos y se ejecutan miles de combinaciones. El resultado puede indicar:

- P50: 50 % de probabilidad de terminar antes de una fecha;
- P80: 80 % de probabilidad;
- rango de costo probable.

P80 suele ser un compromiso más conservador que P50.

### Análisis de sensibilidad

Muestra qué incertidumbres afectan más el resultado. Un diagrama de tornado ordena variables por influencia y ayuda a concentrar las respuestas donde agregan más valor.

---

## 8. Planificar las respuestas

Una respuesta debe ser apropiada, viable, costo-efectiva, acordada y asignada a una persona.

### Estrategias para amenazas

| Estrategia | Qué significa | Ejemplo |
|---|---|---|
| Escalar | Está fuera de la autoridad o alcance del proyecto | Elevar cambio regulatorio al portafolio |
| Evitar | Eliminar la amenaza o su causa | Quitar una tecnología experimental del diseño |
| Transferir | Pasar la responsabilidad financiera a un tercero | Seguro o contrato con garantía |
| Mitigar | Reducir probabilidad o impacto | Prototipar la API temprano |
| Aceptar | Reconocer sin acción preventiva, quizá con reserva | Aceptar una demora menor y definir contingencia |

Transferir no elimina el riesgo; cambia quién asume parte de su impacto. La reputación del proyecto puede seguir afectada.

### Estrategias para oportunidades

| Estrategia | Qué significa | Ejemplo |
|---|---|---|
| Escalar | La oportunidad excede al proyecto | Proponer reutilizar la plataforma en toda la empresa |
| Explotar | Asegurar que ocurra | Asignar al mejor especialista a automatización |
| Compartir | Asociarse con quien puede capturarla | Acuerdo con proveedor experto |
| Mejorar | Aumentar probabilidad o beneficio | Financiar una prueba temprana de automatización |
| Aceptar | Aprovechar si ocurre, sin invertir antes | Usar capacidad liberada si aparece |

### Respuestas contingentes, residuales y secundarios

- **Plan de contingencia:** se ejecuta si ocurre un disparador.
- **Plan de reserva o fallback:** se usa si la respuesta principal no funciona.
- **Riesgo residual:** permanece después de responder.
- **Riesgo secundario:** aparece como consecuencia de la respuesta.

Ejemplo: para mitigar R1 se crea un adaptador desacoplado. Riesgo residual: cambios semánticos aún requieren trabajo. Riesgo secundario: el adaptador agrega complejidad de mantenimiento.

---

## 9. Implementar y monitorear respuestas

Planificar una mitigación que nunca se ejecuta no cambia la exposición. Implementar respuestas verifica responsables, recursos, fechas y acciones reales.

Monitorear incluye:

- revisar riesgos existentes;
- identificar riesgos nuevos;
- cerrar riesgos obsoletos;
- verificar disparadores;
- auditar eficacia de respuestas;
- analizar reservas;
- observar tendencias del riesgo general;
- actualizar registro e informe.

### Ejemplo de seguimiento

| Riesgo | Respuesta | Disparador | Estado |
|---|---|---|---|
| R1 Cambio de API | Prototipo + adaptador | Nueva versión publicada | Mitigación en curso |
| R2 Datos sensibles | Anonimización automática | Dato real detectado | Prueba aprobada |
| R3 Automatización | Ejecutar piloto | Cobertura supera 60 % | Oportunidad capturada parcialmente |

---

## 10. Riesgo versus problema versus supuesto

| Concepto | Ejemplo | Gestión |
|---|---|---|
| Riesgo | La API podría cambiar | Analizar y responder |
| Problema | La API cambió ayer | Resolver y controlar impacto |
| Supuesto | La API estará disponible en octubre | Validar y registrar; puede originar riesgo |
| Restricción | Debe salir antes del 30 de noviembre | Incorporar a planificación |

Un supuesto incierto puede transformarse en una descripción de riesgo: “Si la API no está disponible en octubre, la integración podría retrasarse”.

---

## 11. Errores típicos de control

1. Escribir efectos vagos como si fueran riesgos: “retraso”, “mala calidad”.
2. Registrar un hecho consumado como riesgo futuro.
3. Analizar solo amenazas y olvidar oportunidades.
4. Priorizar exclusivamente con un puntaje, ignorando umbrales especiales.
5. Confundir transferir con eliminar.
6. Definir “monitorear” como respuesta para todos los riesgos.
7. No asignar dueño ni fecha a la respuesta.
8. Guardar reserva sin relacionarla con incertidumbre.
9. Cerrar un riesgo sin revisar riesgos residuales y secundarios.

---

## 12. Autoevaluación

1. Redacta un riesgo de SaludConecta usando causa–evento–efecto.
2. ¿Qué diferencia existe entre riesgo individual y riesgo general?
3. ¿Por qué una lista de verificación no basta para identificar riesgos?
4. ¿Cuándo un riesgo de puntaje medio podría tratarse como alto?
5. Calcula el EMV de una amenaza con 25 % de probabilidad e impacto de $40 millones.
6. ¿Qué diferencia hay entre mitigar, transferir y aceptar?
7. ¿Qué estrategia de oportunidad intenta asegurar que esta ocurra?
8. Da un ejemplo de riesgo secundario producido por una mitigación.
9. ¿Cuál es la diferencia entre contingencia y fallback?
10. ¿Por qué el proceso de riesgos continúa durante todo el proyecto?

---

## 13. Riesgo específico de una licitación

En una licitación se decide alcance, arquitectura, plazo y precio con la peor información del proyecto. La ventana de consultas se cierra y el error queda congelado en el contrato.

La respuesta temprana puede ser:

1. preguntar en el foro;
2. visitar/medir;
3. declarar un supuesto;
4. escribir una exclusión;
5. rediseñar;
6. aumentar reserva/precio;
7. no ofertar.

Una consulta útil cita la base, transcribe el punto ambiguo, explica las interpretaciones y formula una pregunta cerrada. “Favor aclarar” transfiere poco conocimiento.

### Cuándo no ofertar

Señales: exposición mayor al margen, responsabilidad ilimitada, plazo físicamente imposible, alcance esencial indeterminado, dependencia sin acceso, multa desproporcionada o condición que la empresa no puede acreditar.

## 14. De riesgo a solución

La clase exige cinco eslabones:

```text
riesgo → decisión → lugar de la solución → etapa → evidencia
```

Ejemplo:

| Riesgo | Decisión | Lugar | Etapa | Evidencia |
|---|---|---|---|---|
| API sin contrato estable | consultar + adaptador | requisito/arquitectura | propuesta e implementación | respuesta oficial, componente y actividad EDT |
| datos de migración inciertos | supuesto + perfilamiento | alcance/plan | propuesta | exclusión, 80 h y línea de precio |

Prueba inversa: todo componente inusual debe tener requisito, riesgo o decisión que lo justifique.

## 15. Cuatro etapas de respuesta

- **Propuesta:** consulta, supuesto, exclusión, precio o no ofertar.
- **Implementación:** prototipo, diseño, prueba y adquisición.
- **Implantación:** piloto, marcha blanca, reversa y capacitación.
- **Operación:** monitoreo, continuidad, SLA y soporte.

Actuar antes suele ser más barato. Una consulta puede costar casi cero; reparar en operación puede incluir multa y reputación.

## 16. Ficha y gobierno

Una ficha completa incluye ID, causa-evento-efecto, categoría, probabilidad, impacto, exposición, marco temporal, dueño, estrategia, acción/costo, disparador, contingencia y residual.

El capítulo de propuesta debe resumir enfoque, riesgo general, riesgos principales, trazabilidad, supuestos/exclusiones, reserva y gobierno. El registro completo va como anexo.

Gobierno define frecuencia, asistentes, umbral de escalamiento, informe y liberación de reservas. Declarar un riesgo sin respuesta debilita; declarar riesgo con decisión demuestra comprensión y justifica precio.
