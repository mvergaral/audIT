# Proyecto, interesados y requisitos

## 1. Proyecto versus operación

Un **proyecto** es temporal y crea un resultado único. Una **operación** es continua y repetitiva.

| Dimensión | Proyecto | Operación |
|---|---|---|
| Duración | Inicio y fin | Continua |
| Resultado | Único | Repetitivo |
| Equipo | Se forma y disuelve | Estructura permanente |
| Presupuesto | Acotado al proyecto | Recurrente |

Construir SaludConecta es proyecto; prestar soporte por 24 meses es operación contratada. La transición entre ambos debe aparecer en alcance, EDT, costo y aceptación.

Los proyectos nacen por demanda, estrategia, solicitud de cliente, obligación legal, avance tecnológico o problema existente.

## 2. PMBOK como marco

PMBOK no es una metodología cerrada: es un cuerpo de buenas prácticas que se adapta al proyecto.

### Cinco grupos de procesos

- **Inicio:** autoriza y reconoce interesados.
- **Planificación:** define objetivos, alcance y curso de acción.
- **Ejecución:** realiza el trabajo.
- **Monitoreo y control:** compara, pronostica y gestiona cambios.
- **Cierre:** completa formalmente proyecto, fase o contrato.

No son fases cronológicas. Pueden repetirse y solaparse dentro de cada fase.

### Diez áreas de conocimiento

Integración, alcance, cronograma, costos, calidad, recursos, comunicaciones, riesgos, adquisiciones e interesados. El control se concentra en alcance, cronograma, calidad y riesgos, pero las presentaciones conectan también costos y adquisiciones.

## 3. Ciclos de vida

| Predictivo | Adaptativo | Híbrido |
|---|---|---|
| Alcance detallado temprano | Alcance se refina por iteración | Mezcla ambos |
| Cambios formales | Repriorización frecuente | Gobierno según componente |
| Adecuado a precio fijo y requisitos estables | Adecuado a alta volatilidad | Integraciones/hardware predictivos y software iterativo |

Una licitación a suma alzada suele exigir marco predictivo porque alcance, precio y plazo se comprometen. El desarrollo interno puede usar iteraciones, pero eso no elimina obligaciones contractuales.

## 4. Triple restricción ampliada

Alcance, tiempo y costo se afectan mutuamente; calidad, riesgo y recursos también cambian. Si las bases fijan plazo y presupuesto, no queda libertad infinita: hay que negociar alcance, productividad, riesgo o viabilidad.

Aceptar una aplicación móvil “sin cambiar nada” no es flexibilidad; es una inconsistencia que debe analizarse.

## 5. Plan para la dirección

Integra planes subsidiarios y líneas base. Las líneas base principales son alcance, cronograma y costos; solo cambian mediante solicitud aprobada.

Una línea base no es la última versión editada, sino la versión aprobada contra la cual se mide desempeño.

## 6. Interesados

Un interesado puede afectar o verse afectado por el proyecto. Ejemplos:

- patrocinador: financia y resuelve decisiones de alto nivel;
- directora clínica: acepta entregables;
- médicos y administrativos: usuarios;
- pacientes: afectados por experiencia y privacidad;
- laboratorio: dependencia externa;
- regulador: impone obligaciones;
- NexoSalud: proveedor que asume margen y riesgo contractual.

### Matriz poder–interés

| Poder/interés | Tratamiento |
|---|---|
| Alto/alto | Gestionar de cerca |
| Alto/bajo | Mantener satisfecho |
| Bajo/alto | Mantener informado |
| Bajo/bajo | Monitorear |

No se trata de “comunicar más” a todos, sino de involucrarlos de forma adecuada.

## 7. Documentos de una licitación

- **Bases administrativas:** reglas, garantías, multas, evaluación y contrato.
- **Bases técnicas:** necesidad, requisitos, entregables y niveles de servicio.
- **Anexos/formularios:** formatos obligatorios de oferta.
- **Consultas y respuestas:** pueden aclarar o modificar la interpretación de las bases.
- **Oferta técnica/económica:** compromiso del oferente.

Una respuesta oficial posterior puede obligar a recalcular alcance y precio.

## 8. Qué es un requisito

Un requisito expresa una capacidad o condición necesaria. No es una solución prematura ni una frase aspiracional.

“Usar Kubernetes” es diseño, salvo que exista una restricción explícita. “Soportar recuperación automática ante falla de un nodo” expresa la necesidad verificable.

### Tipos útiles

- negocio;
- interesados;
- solución funcional;
- solución no funcional;
- transición;
- proyecto/calidad.

### Funcionales y no funcionales

Funcional: qué hace el sistema. No funcional: cómo debe comportarse o qué restricción cumple.

FURPS+ ayuda a buscar no funcionales:

| Letra | Área | Ejemplo |
|---|---|---|
| F | Funcionalidad | Roles y reglas clínicas |
| U | Usabilidad | Completar reserva en menos de tres minutos |
| R | Confiabilidad | Disponibilidad y recuperación |
| P | Rendimiento | P95 de respuesta ≤ 2 s |
| S | Soportabilidad | Mantenibilidad, prueba, documentación |
| + | Restricciones | Seguridad, plataforma, interfaz, ley |

## 9. Desarrollo y gestión de requisitos

1. **Elicitar:** descubrir necesidades.
2. **Analizar:** resolver conflictos, priorizar y modelar.
3. **Especificar:** escribir de forma clara y verificable.
4. **Validar:** confirmar que representa la necesidad real.
5. **Gestionar:** versionar, trazar y controlar cambios.

### Técnicas y elección

| Técnica | Conviene cuando | Limitación |
|---|---|---|
| Entrevista | Conocimiento profundo en pocas personas | Sesgo y tiempo |
| Taller | Hay conflictos entre áreas | Requiere facilitación |
| Observación | El trabajo real difiere del procedimiento | Puede alterar conducta |
| Encuesta | Muchos participantes | Poca profundidad |
| Prototipo | La interfaz es difícil de verbalizar | Puede confundirse con producto terminado |
| Análisis documental | Existen normas/bases/procesos | Documentos pueden estar obsoletos |

## 10. Cómo escribir un requisito verificable

Una plantilla práctica contiene:

```text
Sujeto + comportamiento/atributo + condición + valor medible + método de verificación
```

Malo: “El sistema será rápido y seguro”.

Mejor:

> Bajo 500 usuarios concurrentes, el percentil 95 de las consultas clínicas será ≤ 2 segundos, medido mediante prueba de carga en preproducción.

Características: necesario, singular, claro, factible, verificable, trazable, consistente y priorizado.

## 11. Matriz de trazabilidad

| ID | Origen | Requisito | Diseño/EDT | Prueba | Aceptación |
|---|---|---|---|---|---|
| RQ-01 | Base técnica 4.2 | P95 ≤ 2 s | Balanceo + 1.2 | PR-CAR-01 | Hito 4 |
| RQ-02 | Ley/cliente | Acceso por roles | Identidad + 1.3 | PR-SEC-03 | Hito 3 |

Sirve para analizar cambios y demostrar cobertura. No es un inventario decorativo.

## 12. Errores frecuentes

1. Confundir necesidad con tecnología.
2. Usar “adecuado”, “rápido” o “fácil” sin métrica.
3. Olvidar transición, datos, operación y capacitación.
4. Basarse solo en lo que dice el patrocinador e ignorar usuarios.
5. Aprobar requisitos sin criterio de verificación.
6. Cambiar la especificación sin analizar impacto.

## 13. Autoevaluación

1. ¿Por qué los grupos de procesos no son fases?
2. ¿Qué combinación de ciclo de vida usarías para software más compra de hardware?
3. Clasifica cinco interesados de SaludConecta por poder/interés.
4. Convierte “debe ser fácil” en requisito verificable.
5. ¿Cuándo usarías observación en vez de entrevista?
6. ¿Por qué una respuesta del foro puede cambiar el precio?
7. Traza un requisito desde la base hasta el pago.

