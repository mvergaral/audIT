# Módulo 4 - Riesgos, adquisiciones y calidad

## 1. Gestión de riesgos

Un riesgo es un evento incierto que puede afectar positiva o negativamente objetivos de alcance, plazo, costo o calidad.

### Proceso

1. Identificar.
2. Analizar cualitativamente.
3. Analizar cuantitativamente si corresponde.
4. Planificar respuestas.
5. Implementar respuestas.
6. Monitorear y actualizar.

### Causa, evento y efecto

“Mala calidad de datos” suele ser un efecto. Hay que preguntar qué evento lo produce: duplicados, campos vacíos, códigos inconsistentes o volumen mayor al supuesto.

## 2. Análisis cualitativo

```text
Exposición = Probabilidad × Impacto
```

Una escala posible:

- crítica: P×I ≥ 0,40;
- alta: 0,20–0,40;
- media: 0,08–0,20;
- baja: <0,08.

Un riesgo con probabilidad alta y bajo impacto puede requerir menos atención que uno poco probable pero catastrófico.

## 3. Análisis cuantitativo y VME

```text
VME = Probabilidad × Impacto monetario
Reserva de contingencia = Σ VME
```

Ejemplo: 50 % y $8.000.000 producen $4.000.000 de VME.

El VME es valor esperado, no una predicción exacta de gasto.

## 4. Respuestas

Para amenazas: evitar, transferir, mitigar, aceptar o escalar.

Para oportunidades: explotar, compartir, mejorar, aceptar o escalar.

### Residual y secundario

- Residual: queda después de responder.
- Secundario: nace como consecuencia de la respuesta.

Ejemplo: contratar una pasarela transfiere parte del riesgo técnico, pero crea dependencia del proveedor.

## 5. Riesgos de licitación

Frases peligrosas de bases técnicas:

- “todo lo necesario para el correcto funcionamiento”;
- “a satisfacción del mandante”;
- “disponibilidad permanente”;
- “migración de información histórica” sin volumen ni calidad;
- “según requiera la contraparte”.

Respuesta profesional:

- consultar;
- declarar supuestos con número, plazo y consecuencia;
- excluir explícitamente lo que no se cotiza;
- convertir aceptación en criterios medibles;
- asignar responsable y acción.

## 6. Adquisiciones

Adquirir es contratar fuera del equipo. En PagoAndes puede incluir pasarela bancaria, nube, SMS, certificados y soporte.

### Comprar versus construir

Comprar conviene si el servicio es estándar, certificado o requiere una especialización que no tiene el equipo. Construir conviene si es diferenciador, estratégico o exige control total.

### Contrato

Debe definir alcance, entregables, plazos, criterios de aceptación, SLA, soporte, seguridad, datos, multas, garantías y salida.

Una garantía puede inmovilizar dinero durante todo el contrato. Un seguro transfiere un impacto económico. No son lo mismo.

## 7. Calidad

### Planificar calidad

Define estándares, métricas, pruebas, responsables y criterios de aceptación.

### Asegurar calidad

Evalúa el proceso: auditorías, revisiones, cumplimiento de prácticas y trazabilidad.

### Controlar calidad

Evalúa el producto: pruebas, inspección y medición de defectos.

### Validar alcance

El cliente acepta formalmente el entregable.

## 8. Trazabilidad

```text
Requisito → componente → prueba → resultado → aceptación
```

Si el diagrama promete una métrica de calidad, la EDT debe incluir la actividad para probarla y el presupuesto debe incluir sus horas.

## Preguntas de control relacionadas

7. Costo con horas nominales.
8–9. Riesgos y licitación.
13. VME.
Todas las preguntas nuevas de calidad y adquisiciones del Control 2.
