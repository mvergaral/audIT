# PMBOK 05 - Gestión del Alcance y EDT/WBS

## 1. Idea central

Gestionar el alcance significa garantizar que el proyecto incluya **todo el trabajo requerido y únicamente el trabajo requerido**.

Hay dos alcances:

- **Alcance del producto:** características y funciones del producto.
- **Alcance del proyecto:** trabajo que debe realizarse para entregar el producto.

En SaludConecta, “videoconsulta con receta electrónica” es alcance del producto. Analizar, diseñar, programar, probar, capacitar y desplegar esa funcionalidad pertenece al alcance del proyecto.

## 2. Mapa de procesos

```text
5.1 Planificar la Gestión del Alcance
        ↓
5.2 Recopilar Requisitos
        ↓
5.3 Definir el Alcance
        ↓
5.4 Crear la EDT/WBS
        ↓
5.5 Validar el Alcance
5.6 Controlar el Alcance
```

## 3. 5.1 Planificar la Gestión del Alcance

Define cómo se hará el trabajo de alcance.

### Salidas principales

- Plan de gestión del alcance.
- Plan de gestión de los requisitos.

### Preguntas que responde

- ¿Cómo se definirá y aprobará el alcance?
- ¿Cómo se creará y mantendrá la EDT?
- ¿Cómo se aceptarán entregables?
- ¿Cómo se controlarán cambios?
- ¿Cómo se documentarán y priorizarán requisitos?

No produce todavía el alcance detallado. Define el procedimiento para gestionarlo.

## 4. 5.2 Recopilar Requisitos

Determina, documenta y gestiona necesidades de interesados.

### Técnicas y cuándo usarlas

| Técnica | Conviene cuando | Limitación |
|---|---|---|
| Entrevista | Se necesita profundidad individual | Puede reflejar sesgos personales |
| Grupo focal | Interesa explorar percepciones de un grupo | Puede dominar una voz fuerte |
| Taller facilitado | Hay áreas con intereses distintos | Requiere buena facilitación |
| Encuesta | Hay muchos interesados dispersos | Entrega menos profundidad |
| Observación | El usuario no logra explicar su trabajo | Consume tiempo y depende del contexto |
| Prototipo | El requisito visual o interactivo es incierto | Puede confundirse con producto terminado |
| Benchmarking | Se quiere comparar con buenas prácticas | Lo que funciona afuera puede no encajar |
| Diagrama de contexto | Se deben aclarar fronteras e interfaces | No reemplaza el detalle de requisitos |

### Salidas

- Documentación de requisitos.
- Matriz de trazabilidad de requisitos.

### Matriz de trazabilidad

Conecta cada requisito con su origen, objetivo, entregable, prueba y estado.

```text
REQ-014 → Tesorería → Conciliación → Módulo Pagos → Prueba CP-27 → Aprobado
```

Sirve para detectar requisitos sin prueba, trabajo sin requisito y cambios que afectan varios entregables.

## 5. 5.3 Definir el Alcance

Convierte requisitos seleccionados en una descripción detallada del proyecto y producto.

### Enunciado del alcance

Debe contener, según el caso:

- descripción del alcance del producto;
- entregables;
- criterios de aceptación;
- exclusiones;
- restricciones;
- supuestos.

### Ejemplo didáctico

Mala definición:

> Integrar SaludConecta con los sistemas del cliente.

Buena definición:

> Integrar con el laboratorio Alfa mediante su API REST documentada, considerando hasta diez operaciones. Otros laboratorios quedan fuera de la primera etapa.

La segunda permite estimar y controlar cambios.

### Las once preguntas de formulación de la clase

| Etapa | Preguntas | Qué determinan |
|---|---|---|
| Identificación | qué, por qué, para qué, a quiénes | naturaleza, objetivos, beneficios y destinatarios |
| Alternativas | cuánto, cómo, dónde | metas/tamaño, solución y localización |
| Evaluación | con qué, quiénes | recursos, financiamiento, organización y perfiles |
| Programación | cuándo | orden, prioridad y control temporal |
| Selección | cuál | alternativa elegida y criterios |

La tecnología responde principalmente el “cómo”; las otras diez preguntas impiden resolver con tecnología un problema mal formulado.

### Diagrama de contexto

Muestra el sistema dentro de una frontera y, fuera, personas, procesos, equipos y sistemas externos. Cada flecha es una interfaz que debe especificarse, proveerse o construirse, probarse y cotizarse. Lo externo no se construye, pero puede generar trabajo y riesgo.

## 6. 5.4 Crear la EDT/WBS

La EDT es una descomposición jerárquica orientada a entregables del trabajo total del proyecto.

### Ejemplo

```text
1. SaludConecta
   1.1 Dirección del proyecto
   1.2 Requisitos aprobados
   1.3 Portal de pacientes
       1.3.1 Registro
       1.3.2 Agenda
       1.3.3 Videoconsulta
   1.4 Aplicación administrativa
   1.5 Integraciones
       1.5.1 Laboratorio
       1.5.2 Pagos
   1.6 Migración de datos
   1.7 Pruebas y aceptación
   1.8 Capacitación y puesta en marcha
```

### Regla del 100 %

La EDT debe incluir 100 % del trabajo definido por el alcance, incluido trabajo de dirección. Cada nivel hijo representa 100 % del padre, sin duplicaciones.

### Paquete de trabajo

Es el nivel suficientemente bajo para estimar, asignar, presupuestar y controlar. No existe una profundidad universal: se descompone hasta que el trabajo sea manejable.

### Cuenta de control y paquete de planificación

- **Cuenta de control:** punto donde alcance, costo y cronograma se integran para medir desempeño.
- **Paquete de planificación:** trabajo futuro conocido, pero aún sin detalle suficiente para convertirlo en paquete de trabajo.

### Diccionario de la EDT

Describe cada elemento: código, alcance, responsable, hitos, criterios de aceptación, supuestos, recursos y referencias.

### Línea base del alcance

Está formada por:

1. Enunciado del alcance aprobado.
2. EDT/WBS aprobada.
3. Diccionario de la EDT/WBS.

## 7. WBS Standard - principios importantes

- Orientación a entregables, no a una simple lista de tareas.
- La EDT no reemplaza el cronograma.
- Los elementos no tienen que llegar todos al mismo nivel.
- Puede representarse como árbol, esquema numerado o tabla.
- Debe facilitar estimación, asignación de responsabilidad, control de cambios y reporte.
- Debe evitar solapamientos, porque producen doble conteo.

## 8. 5.5 Validar el Alcance

Formaliza la aceptación de entregables completados.

Entrada clave: **entregables verificados**, provenientes de Controlar la Calidad.

Salida clave: **entregables aceptados** o solicitudes de cambio.

### Distinción fundamental

```text
Controlar Calidad: ¿está correcto?
Validar Alcance: ¿el cliente lo acepta?
```

Un módulo puede pasar todas las pruebas y aun requerir la firma del cliente.

## 9. 5.6 Controlar el Alcance

Monitorea el estado del alcance y gestiona cambios a la línea base.

### Corrupción del alcance

Ocurre cuando se agrega funcionalidad sin aprobación formal. Puede parecer “ayudar al cliente”, pero consume tiempo y presupuesto no autorizados.

### Análisis de variación

Compara desempeño real contra línea base para decidir si se necesita acción correctiva o solicitud de cambio.

## 10. Predictivo versus adaptativo

En un enfoque predictivo, el alcance se define temprano y cambia mediante control integrado. En un enfoque adaptativo, requisitos y alcance detallado se refinan por iteración, con participación continua del cliente.

La gestión del alcance sigue existiendo en ambos; cambia la frecuencia y el artefacto utilizado.

## 11. Errores típicos de control

- Confundir EDT con cronograma.
- Descomponer solo el trabajo técnico y olvidar gestión, pruebas y capacitación.
- Crear paquetes tan grandes que no puedan controlarse.
- Usar actividades como estructura principal sin identificar entregables.
- Validar alcance antes de verificar calidad.
- Agregar cambios sin actualizar la línea base.

## 12. Autoevaluación

1. ¿Qué documentos forman la línea base del alcance?
2. ¿Por qué la matriz de trazabilidad reduce omisiones?
3. ¿Cuál es la diferencia entre paquete de trabajo y cuenta de control?
4. ¿Por qué una EDT no debe contener flechas de precedencia como elemento esencial?
5. ¿Qué ocurre primero: Controlar Calidad o Validar Alcance?
