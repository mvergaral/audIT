# Hoja de fórmulas, decisiones y confusiones frecuentes

Usa esta hoja para el repaso final. No sustituye los capítulos: resume relaciones que debes poder explicar.

---

## 1. Mapa global del proyecto

```text
Necesidad
  ↓
Requisito verificable
  ↓
Alcance del producto y del proyecto
  ↓
EDT + diccionario = línea base del alcance
  ↓
Actividades + dependencias + duraciones
  ↓
Cronograma y línea base
  ↓
Ejecución con gestión de riesgos y calidad
  ↓
Entregable verificado
  ↓
Entregable aceptado
```

La estimación alimenta esfuerzo, duración y costo; los riesgos y la calidad atraviesan todo el recorrido.

---

## 2. Fórmulas de cronograma

### Tres valores

```text
Triangular = (O + M + P) / 3
Beta/PERT = (O + 4M + P) / 6
Desviación aproximada = (P - O) / 6
```

### Ruta crítica

```text
EF = ES + duración
LS = LF - duración
Holgura total = LS - ES = LF - EF
```

Con la convención de comenzar en tiempo 0. En una prueba que utilice días 1, 2, 3, conserva la convención de forma consistente.

La ruta crítica es la ruta de mayor duración de la red y normalmente tiene holgura total cero.

---

## 3. Fórmulas UCP

```text
UAW  = Σ(actores × peso)
UUCW = Σ(casos de uso × peso)
UUCP = UAW + UUCW

TCF = 0,6 + 0,01 × TFactor
EF  = 1,4 - 0,03 × EFactor

UCP = UUCP × TCF × EF
Programación = UCP × HH/UCP
Total del ciclo = Programación / 0,40
```

### Pesos de actores

| Simple | Medio | Complejo |
|---:|---:|---:|
| 1 | 2 | 3 |

### Pesos de casos de uso

| 1–3 transacciones | 4–7 | 8 o más |
|---:|---:|---:|
| 5 | 10 | 15 |

### Distribución del curso

| Análisis | Diseño | Programación | Pruebas | Sobrecarga |
|---:|---:|---:|---:|---:|
| 10 % | 20 % | 40 % | 15 % | 15 % |

### Conversión a duración y costo

```text
Capacidad efectiva mensual = personas × HH/mes × disponibilidad
Duración simplificada = esfuerzo total / capacidad efectiva mensual
Costo = esfuerzo × tarifa por hora
```

La duración simplificada no reemplaza la red: supone que el esfuerzo se puede distribuir de forma compatible con las dependencias.

---

## 4. Fórmulas de riesgo

```text
EMV = probabilidad × impacto monetario
EMV neto = Σ EMV de amenazas y oportunidades
```

- amenaza: impacto negativo;
- oportunidad: impacto positivo.

En escalas cualitativas puede usarse `P × I` para priorizar, pero el resultado no es automáticamente dinero ni una probabilidad científica.

---

## 5. Comparaciones que suelen aparecer

### Alcance

| A | B | Diferencia esencial |
|---|---|---|
| Alcance del producto | Alcance del proyecto | Características del producto vs trabajo para producirlo |
| Requisito | Entregable | Necesidad documentada vs resultado producido |
| EDT | Cronograma | Qué trabajo existe vs cuándo y en qué orden se ejecuta |
| Paquete de trabajo | Actividad | Componente gestionable de alcance vs acción temporal |
| Verificar calidad | Validar alcance | Cumplimiento técnico vs aceptación formal |

### Cronograma

| A | B | Diferencia esencial |
|---|---|---|
| Esfuerzo | Duración | Trabajo humano vs tiempo calendario |
| Lead | Lag | Adelantar sucesora vs imponer espera |
| Nivelación | Suavizamiento | Puede mover fecha/ruta vs usa holgura disponible |
| Crashing | Fast tracking | Agregar recursos/costo vs superponer y aumentar riesgo |
| Hito | Actividad | Evento de duración cero vs trabajo con duración |

### Estimación

| A | B | Diferencia esencial |
|---|---|---|
| Top-down | Bottom-up | Total temprano distribuido vs componentes detallados sumados |
| Analogía | Paramétrica | Comparación con caso similar vs relación matemática calibrada |
| Punto de función | UCP | Funciones de usuario/datos vs actores y casos de uso |
| Tamaño | Esfuerzo | Magnitud funcional vs trabajo requerido |

### Riesgos

| A | B | Diferencia esencial |
|---|---|---|
| Riesgo | Problema | Puede ocurrir vs ya ocurrió |
| Mitigar | Evitar | Reducir exposición vs eliminar amenaza/causa |
| Transferir | Escalar | Pasar responsabilidad a tercero vs elevar fuera del proyecto |
| Residual | Secundario | Permanece después de responder vs nace por la respuesta |
| Contingencia | Fallback | Se activa al ocurrir riesgo vs alternativa si la primera respuesta falla |
| Explotar | Mejorar | Garantizar oportunidad vs aumentar probabilidad/beneficio |

### Calidad

| A | B | Diferencia esencial |
|---|---|---|
| Calidad | Grado | Cumplimiento vs categoría de prestaciones |
| Prevención | Inspección | Evitar defecto vs detectarlo |
| Atributo | Variable | Cumple/no cumple vs medición continua |
| Tolerancia | Límite de control | Exigencia del cliente vs estabilidad estadística |
| Auditoría | Prueba | Revisa proceso vs evalúa producto |
| Verificado | Aceptado | Cumple especificación vs cliente aprueba formalmente |

---

## 6. Cómo elegir una técnica

### “Necesito estimar muy temprano”

Usa analogía, expertos y rangos. No inventes detalle para aparentar precisión.

### “Tengo una EDT estable y detallada”

Usa estimación ascendente y compárala con datos históricos.

### “Tengo casos de uso consistentes”

UCP puede convertir actores/casos en tamaño y luego en esfuerzo.

### “No sé qué riesgo atender primero”

Usa análisis cualitativo con P/I, umbrales, urgencia y calidad de datos. Aplica cuantitativo a decisiones de alto impacto cuando se justifique.

### “Tengo muchas categorías de defectos”

Pareto ayuda a priorizar; Ishikawa y causa raíz ayudan a entender por qué.

### “El proceso cambia de forma extraña en el tiempo”

Usa gráfico de control para buscar causas especiales.

### “Necesito reducir la fecha”

Analiza ruta crítica. Crashing compra tiempo con costo; fast tracking compra tiempo con riesgo. Comprimir una tarea con holgura puede no servir.

---

## 7. Palabras clave para reconocer el proceso

| Si el enunciado habla de… | Piensa primero en… |
|---|---|
| Necesidades de interesados | Recopilar Requisitos |
| Límites, exclusiones y aceptación | Definir el Alcance |
| Descomposición orientada a entregables | Crear la EDT |
| Firma o aceptación del cliente | Validar el Alcance |
| Desviación de alcance | Controlar el Alcance |
| Acciones concretas desde paquetes | Definir Actividades |
| Predecesoras y sucesoras | Secuenciar Actividades |
| O, M y P | Estimar Duraciones |
| Ruta crítica o nivelación | Desarrollar Cronograma |
| Tendencias y pronóstico temporal | Controlar Cronograma |
| Categorías y matriz P/I | Planificar Riesgos |
| Causa–evento–efecto | Identificar Riesgos |
| Prioridad | Análisis Cualitativo |
| Monte Carlo, EMV, tornado | Análisis Cuantitativo |
| Mitigar/explotar | Planificar Respuestas |
| Ejecutar mitigación | Implementar Respuestas |
| Auditorías de riesgo y reservas | Monitorear Riesgos |
| Métricas, estándares y COQ | Planificar Calidad |
| Auditoría, proceso y mejora | Gestionar Calidad |
| Inspección, prueba y entregable verificado | Controlar Calidad |

---

## 8. Plantillas para responder

### Pregunta conceptual

> X es… Se diferencia de Y porque… En el caso se usaría cuando… Es preferible a Y si…

### Pregunta de decisión

> Primero identificaría… Luego aplicaría… porque… La alternativa propuesta no es conveniente debido a… El resultado esperado sería…

### Pregunta de cálculo

1. escribir fórmula;
2. reemplazar valores con unidades;
3. calcular sin redondear prematuramente;
4. interpretar el resultado;
5. declarar supuesto o limitación.

### Pregunta de riesgo

> Debido a [causa], podría ocurrir [evento], provocando [efecto]. Su prioridad es… La respuesta elegida es… porque… El dueño y disparador son…

---

## 9. Control mental de 20 segundos

Antes de entregar una respuesta, revisa:

- ¿Contesté la decisión y no solo definí?
- ¿Expliqué por qué esta técnica es adecuada?
- ¿Separé esfuerzo, duración y costo?
- ¿Diferencié verificación técnica de aceptación?
- ¿Nombré amenaza u oportunidad correctamente?
- ¿Usé unidades en el cálculo?
- ¿Declaré el supuesto más importante?

---

## 10. Arquitectura, disponibilidad y sala

```text
Disponibilidad en serie = A1 × A2 × ... × An
Indisponibilidad = 1 − disponibilidad
Caída anual aproximada = indisponibilidad × 365 × 24 h

PUE = energía total / energía TI
DCiE = energía TI / energía total = 1/PUE

potencia de diseño = carga TI × (1 + holgura)
U de diseño = U requeridas / ocupación objetivo
racks = techo(U de diseño / U útiles)
```

| No confundir | Diferencia |
|---|---|
| TIER / SLA | infraestructura certificable vs compromiso del servicio |
| disponibilidad / continuidad | estar operativo vs recuperarse |
| RAID / backup | redundancia local vs copia recuperable |
| RTO / RPO | tiempo de recuperación vs pérdida temporal de datos |
| VM / contenedor | SO completo vs kernel compartido |
| OAuth / OIDC | autorización delegada vs autenticación |

## 11. Costos, contratos y adquisiciones

```text
horas productivas = horas nominales × % productivo
costo directo/h = costo empresa mensual / horas productivas
tarifa = costo directo + gastos generales + margen según base declarada

TCO = adquisición + implantación + integración + operación
      + soporte + renovación + administración + salida − valor residual

PTA = costo objetivo + (precio tope − precio objetivo)
      / participación del comprador

puntaje ponderado = Σ(peso × nota normalizada)
```

| No confundir | Diferencia |
|---|---|
| costo / tarifa / precio / monto | gasto / unidad vendida / venta neta / total formulario |
| CAPEX / OPEX | inversión activable vs gasto recurrente |
| contingencia / gestión / margen | riesgo conocido / desconocido / utilidad |
| RFI / RFP / RFQ / IFB | explorar / proponer / cotizar / ofertar formalmente |
| hacer / comprar / arrendar | construir / adquirir activo / consumir servicio |

## 12. Calidad contractual

```text
requisito → métrica → prueba → aceptación → hito → pago
COQ = prevención + evaluación + falla interna + falla externa
```

Calidad es cumplimiento; grado es cantidad/categoría de prestaciones. Controlar Calidad verifica; Validar Alcance obtiene aceptación. SLA debe contener indicador, objetivo, ventana, exclusiones y consecuencia.

## 13. Glosario adicional

| Sigla | Significado |
|---|---|
| ADR | registro de decisión arquitectónica |
| API | interfaz de programación |
| CAPEX/OPEX | inversión/gasto operativo |
| CI/CD | integración y entrega/despliegue continuos |
| DCiE | eficiencia TI respecto del total |
| DMZ | segmento para servicios expuestos |
| IOPS | operaciones de entrada/salida por segundo |
| PDU | distribución eléctrica del rack |
| PUE | energía total dividida por energía TI |
| RTO/RPO | tiempo/punto objetivo de recuperación |
| SLI/SLO/SLA | indicador/objetivo/acuerdo de servicio |
| TCO | costo total de propiedad |
| UPS | alimentación ininterrumpida |
