# Módulo 2 - Requisitos, alcance, EDT y cronogramas

## 1. Requisitos

Un requisito debe describir una necesidad o condición verificable, no imponer innecesariamente una tecnología.

### Tipos

- Negocio: objetivo de la organización.
- Interesado: necesidad de una persona o grupo.
- Funcional: qué debe hacer el producto.
- No funcional: rendimiento, seguridad, disponibilidad, usabilidad.
- Transición: migración, capacitación, conversión y marcha blanca.
- Proyecto: hitos, plazo y restricciones contractuales.
- Calidad: criterio de aceptación de un entregable.

### ERS

La Especificación de Requisitos de Software define requisitos funcionales, no funcionales, restricciones e interfaces. No debe incluir el “cómo” detallado, algoritmos o tecnologías si existen varias soluciones válidas.

Un enunciado “deberá manejar adecuadamente los errores” es deficiente: usa un verbo ambiguo y no tiene umbral. Debe transformarse en una condición medible.

## 2. Alcance

Alcance es todo el trabajo necesario y solo ese trabajo.

- Validar alcance: cliente acepta el entregable.
- Controlar alcance: se evita entregar de más o de menos.
- Controlar calidad: se comprueba que el producto cumple requisitos y estándares.

La triple restricción conecta alcance, tiempo y costo. Si se fijan dos, el tercero queda condicionado. Calidad, riesgos y recursos también se ven afectados.

## 3. EDT / WBS

La EDT descompone el alcance en entregables y paquetes de trabajo:

```text
1. PagoAndes
   1.1 Requisitos
   1.2 Arquitectura
   1.3 Desarrollo
   1.4 Integración bancaria
   1.5 Pruebas
   1.6 Capacitación
   1.7 Puesta en marcha
```

Regla del 100 %: la suma de los hijos representa todo el trabajo del padre.

Regla 8/80: un paquete de trabajo suele durar entre 8 y 80 horas. Un paquete de 200 horas es demasiado grande para controlar.

Las flechas de precedencia pertenecen al cronograma, no son obligatorias para que exista una EDT. El primer nivel puede organizarse por fases, siempre que la descomposición sea completa y controlable.

## 4. Dependencias

- Obligatoria: impuesta por lógica física o contractual.
- Discrecional: decisión del equipo; puede cambiarse con justificación.
- Externa: depende de un proveedor, cliente, autoridad o tercero.

Para acortar un proyecto sin recursos adicionales se pueden revisar dependencias discrecionales. No se debe romper una dependencia obligatoria.

## 5. PDM y relaciones

- FS (Fin-Inicio): B empieza cuando A termina.
- SS (Inicio-Inicio): B empieza cuando A empieza, con posible retraso.
- FF (Fin-Fin): B termina cuando A termina.
- SF (Fin-Inicio inversa): poco usada.

Un retraso positivo agrega espera. Un adelanto permite comenzar antes de que termine completamente la predecesora.

## 6. CPM y ruta crítica

La ruta crítica es el camino de mayor duración y sus actividades tienen holgura cero.

Ejemplo:

| Actividad | Duración | Predecesoras |
|---|---:|---|
| A | 4 | - |
| B | 3 | A |
| C | 8 | B |
| D | 5 | B |
| E | 4 | C, D |
| F | 2 | E |

Rutas:

```text
A-B-C-E-F = 21 días
A-B-D-E-F = 18 días
```

La ruta crítica es A-B-C-E-F. D tiene 3 días de holgura.

## 7. PERT

Cuando una duración es incierta:

```text
tE triangular = (O + M + P) / 3
tE PERT beta  = (O + 4M + P) / 6
σ = (P − O) / 6
```

PERT da más peso al valor más probable. Se puede planificar internamente con P50 y comprometer externamente un percentil más conservador, como P80, si el riesgo lo exige.

## 8. Costos y horas

Esfuerzo no es plazo. Costo no es precio de venta.

Para costo directo:

```text
Costo = horas-hombre × tarifa
```

Las horas nominales de contrato no son necesariamente horas productivas. Si se calcula tarifa mensual usando todas las horas nominales, se puede subestimar el costo real porque existen feriados, reuniones, permisos y tiempos no productivos.

## Preguntas de control relacionadas

3. Requisitos ambiguos.
4. EDT.
5. Dependencias discrecionales.
7. Horas nominales y costo.
14. CPM y holgura.
15. PDM con SS, FS, FF y retrasos.
