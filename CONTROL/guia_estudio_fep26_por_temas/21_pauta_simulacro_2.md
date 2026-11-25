# Pauta razonada del Simulacro 2

Utiliza esta pauta solo después de responder una sección completa del banco. Una respuesta sólida debe incluir **concepto, aplicación al caso y conclusión**.

Banco correspondiente: `18_banco_acotado_profesor_sin_respuestas.md`.

---

# Parte A - Selección múltiple

## Resumen de respuestas

```text
1B  2D  3C  4E  5A  6C
7B  8E  9D  10C 11A 12D
13C 14B 15E 16A 17D 18C
19A 20D 21B 22E 23C 24A
```

## Capítulo 5

### 1. B

**Recopilar Requisitos** produce la documentación de requisitos y la matriz de trazabilidad. La opción A corresponde a Planificar la Gestión del Alcance; C atribuye la matriz al proceso equivocado; D mezcla la línea base con una salida anterior. Por eso “todas” tampoco puede ser correcta.

### 2. D

La línea base del alcance está formada por el **enunciado del alcance aprobado, la EDT y el diccionario de la EDT**. Los requisitos y su trazabilidad son documentos esenciales, pero no integran esa línea base. Las líneas base de cronograma y costos pertenecen a otras áreas.

### 3. C

Un **paquete de planificación** contiene trabajo conocido dentro de una cuenta de control que aún no puede descomponerse en paquetes de trabajo. No debe llamarse actividad porque todavía no corresponde al nivel operativo del cronograma, ni paquete de trabajo si aún no es estimable y gestionable con suficiente detalle.

### 4. E

Las tres afirmaciones expresan la regla del 100 %: todo el trabajo requerido, cobertura completa del padre por sus hijos y exclusión del trabajo que no pertenece al alcance. También debe incluirse el trabajo de gestión, aunque no produzca funcionalidad del producto.

### 5. A

Un resultado técnicamente conforme puede convertirse en **entregable verificado**, pero la aceptación pertenece a Validar el Alcance. Como el flujo omitido estaba aprobado, no corresponde eliminarlo automáticamente ni aceptar el módulo; se debe rastrear y corregir la no conformidad.

### 6. C

La petición debe documentarse y someterse al proceso de control de cambios. Antes de aprobarla no se modifica la línea base, no se agrega silenciosamente a la EDT y tampoco se rechaza solo porque exista una línea base: una línea base puede cambiar, pero únicamente de forma controlada.

---

## Capítulo 6

### 7. B

La condición está relacionada con el **inicio** de ambas actividades y contiene un retraso de tres días: `SS+3`. Una relación FS tomaría como referencia el término del despliegue y una FF regularía fechas de término.

### 8. E

Se redujo el **lag** de cinco a dos unidades. Esto no reduce por sí mismo la duración de B ni convierte la relación en SS. El cambio solo es válido si la espera original era discrecional o si la nueva espera continúa respetando la restricción que la originó.

### 9. D

```text
Holgura = LS-ES = 11-8 = 3 días
Holgura = LF-EF = 17-14 = 3 días
```

Que las duraciones temprana y tardía coincidan no significa holgura cero; toda actividad conserva la misma duración al desplazarse.

### 10. C

Superponer trabajo originalmente secuencial por una dependencia discrecional es **fast tracking o ejecución rápida**. No requiere necesariamente recursos adicionales, pero aumenta el riesgo de cambios y retrabajo. Debe evaluarse sobre la ruta crítica para que pueda reducir la fecha final.

### 11. A

El ajuste permanece dentro de la holgura y no cambia la ruta crítica ni la fecha del proyecto: es **suavizamiento de recursos**. La nivelación puede superar la holgura y modificar el cronograma; fast tracking superpone trabajo y crashing incorpora recursos o costo.

### 12. D

Al acortar solo una de dos rutas críticas, la otra puede continuar con la duración original y seguir determinando el término. Por eso el proyecto podría no acortarse. Siempre se debe recalcular la red: no se puede repartir automáticamente la reducción ni crear holgura en la ruta no intervenida.

---

## Capítulo 8

### 13. C

**Grado** representa la categoría o cantidad de prestaciones; **calidad** representa cumplimiento de requisitos. Un producto básico puede ser de bajo grado y alta calidad. Un producto avanzado puede tener alto grado y baja calidad si incumple sus especificaciones.

### 14. B

Auditar y mejorar el proceso utilizado para producir resultados corresponde a **Gestionar la Calidad**. Planificar define estándares y métricas; Controlar la Calidad mide resultados o entregables concretos; Validar el Alcance obtiene aceptación formal.

### 15. E

La secuencia correcta es:

```text
Capacitación       -> prevención
Inspección         -> evaluación
Retrabajo previo   -> falla interna
Garantía posterior -> falla externa
```

### 16. A

Prevención y evaluación son costos de **conformidad**. Eliminar prevención puede parecer un ahorro inmediato, pero puede incrementar defectos, retrabajo y fallas externas. Esto no significa que toda evaluación deba desaparecer: prevención y detección cumplen funciones diferentes.

### 17. D

Los límites de control describen la estabilidad estadística del proceso; los límites de especificación describen lo que exige el cliente. Un proceso puede ser estable alrededor de un promedio inaceptable y, por tanto, no ser capaz de cumplir la especificación.

### 18. C

La inspección y reinspección pertenecen a **Controlar la Calidad** y son costos de evaluación. La corrección de defectos antes de liberar es falla interna. Después de la reinspección puede existir un entregable verificado, pero todavía falta la aceptación formal mediante Validar el Alcance.

---

## Capítulo 11

### 19. A

La secuencia es:

```text
Planificar -> Identificar -> Cualitativo -> Cuantitativo
-> Planificar respuestas -> Implementar respuestas -> Monitorear
```

El análisis cuantitativo puede no ser necesario en todos los proyectos, pero cuando se realiza se apoya en riesgos previamente identificados y priorizados.

### 20. D

La póliza **transfiere** contractualmente una parte del impacto financiero. No elimina la causa ni reduce necesariamente la probabilidad. Tampoco equivale a aceptación activa, porque en esta última el proyecto conserva la exposición y prepara una respuesta o reserva propia.

### 21. B

**Explotar** busca asegurar que la oportunidad ocurra. Mejorar aumenta su probabilidad o impacto sin garantizarla; compartir asigna parte de su aprovechamiento a un tercero; escalar se usa cuando está fuera de la autoridad o alcance del proyecto.

### 22. E

La exposición que permanece después de responder es **riesgo residual**. La incompatibilidad creada por la propia respuesta es un **riesgo secundario**. Ambos deben documentarse y recibir propietario y tratamiento apropiados.

### 23. C

La contingencia cubre riesgos identificados y forma parte de la línea base de costos. La reserva de gestión cubre trabajo imprevisto o desconocido, queda fuera de la línea base, pero forma parte del presupuesto total del proyecto.

### 24. A

```text
EMV(X) = 0,60x18 + 0,40x(-6)
       = 10,8 - 2,4
       = $8,4 millones

EMV(Y) = 0,80x12 + 0,20x(-3)
       = 9,6 - 0,6
       = $9,0 millones
```

Y supera a X en **$0,6 millones de valor esperado**. La selección por EMV no elimina la necesidad de considerar tolerancia al riesgo.

---

# Parte B - Desarrollo y cálculo

## 25. Procesos, salidas y aceptación

### a. Procesos y salidas centrales

| Orden | Proceso | Salida central |
|---:|---|---|
| 1 | Planificar la Gestión del Alcance | Plan de gestión del alcance y plan de gestión de requisitos |
| 2 | Recopilar Requisitos | Documentación de requisitos y matriz de trazabilidad |
| 3 | Definir el Alcance | Enunciado del alcance del proyecto |
| 4 | Crear la EDT | Línea base del alcance |
| 5 | Validar el Alcance | Entregables aceptados |
| 6 | Controlar el Alcance | Información de desempeño y solicitudes de cambio |

No es necesario recitar todas las actualizaciones de planes y documentos para explicar la finalidad de cada proceso.

### b. Recorrido de aceptación

```text
Trabajo ejecutado
    -> entregable terminado
    -> Controlar la Calidad
    -> entregable verificado
    -> Validar el Alcance
    -> entregable aceptado
```

Controlar la Calidad comprueba conformidad técnica y criterios medibles. Validar el Alcance obtiene aceptación formal del cliente o patrocinador. Normalmente el control técnico ocurre antes de presentar el resultado para aceptación, aunque ambos procesos pueden coordinarse de manera iterativa.

### c. Grabación solicitada

Se debe registrar la solicitud, analizar efectos sobre alcance, EDT, cronograma, costos, calidad y riesgos, y someterla a la autoridad de cambios. Antes de aprobarla no se deben modificar la línea base del alcance, la línea base del cronograma ni la de costos. Si se aprueba, se actualizan los documentos afectados y se comunica la decisión.

---

## 26. Diagnóstico de una EDT

### a. Elementos potencialmente válidos

Usar fases del ciclo de vida como primer nivel puede ser válido si cada fase se descompone en entregables y, en conjunto, la EDT representa el 100 % del alcance. No existe obligación de que el primer nivel utilice una única estructura universal.

### b. Errores

- Las flechas de precedencia pertenecen al diagrama de red del cronograma, no a la EDT.
- Llamar “actividad” a todo componente inferior mezcla el alcance con el cronograma.
- Detenerse siempre en 200 horas es un criterio rígido. La descomposición debe continuar hasta que el trabajo sea estimable, asignable y controlable.
- Con reportes quincenales, 200 horas equivalen aproximadamente a cinco semanas de una persona a tiempo completo, lo que dificulta observar objetivamente el avance dentro de cada ciclo de control.
- Excluir la gestión deja trabajo real fuera del alcance representado.

### c. Vocabulario

- **Cuenta de control:** punto donde se integran alcance, cronograma y costo para medir desempeño.
- **Paquete de planificación:** trabajo conocido pero todavía no detallado en paquetes ejecutables.
- **Paquete de trabajo:** nivel inferior de la EDT donde el trabajo puede estimarse, asignarse y controlarse.
- **Actividad:** acción del cronograma necesaria para completar un paquete de trabajo.

### d. Regla vulnerada

Excluir la gestión vulnera la **regla del 100 %**, porque la EDT debe incluir todo el trabajo requerido para completar y administrar el proyecto.

---

## 27. Red con relaciones mixtas

### a. Cálculo original

Se utiliza tiempo cero como inicio:

| Actividad | Cálculo | Inicio temprano | Fin temprano |
|---|---|---:|---:|
| A | Inicio | 0 | 4 |
| B | FS con A | 4 | 10 |
| C | SS+2 con B | 6 | 13 |
| D | FS con B | 10 | 15 |
| E | `max(EF_C, EF_D+1)` | 16 | 20 |
| F | FF con E | 17 | 20 |
| G | FS con E | 20 | 22 |

Para F, la relación FF exige que termine cuando termina E. Como F dura tres semanas, debe comenzar en la semana 17.

### b. Duración y secuencia controladora

El proyecto termina en la semana **22**. La secuencia que controla el término es:

```text
A -> B -> D -> espera de 1 semana -> E -> G
```

La rama de C termina antes de la fecha impuesta por D más el retraso. F termina en la semana 20 y no controla el fin global.

### c. B aumenta a ocho semanas

El inicio de B permanece en 4, pero ahora termina en 12:

| Actividad | Inicio temprano | Fin temprano |
|---|---:|---:|
| A | 0 | 4 |
| B | 4 | 12 |
| C | 6 | 13 |
| D | 12 | 17 |
| E | `max(13,17+1)=18` | 18 | 22 |
| F | 19 | 22 |
| G | 22 | 24 |

### d. Efecto diferente

C depende del **inicio** de B mediante SS+2. Como B sigue comenzando en la semana 4, C continúa comenzando en la 6. D depende del **término** de B mediante FS, por lo que se desplaza dos semanas.

### e. Conclusión

El proyecto termina en la **semana 24**. El aumento de dos semanas no es absorbido porque afecta la secuencia que controla la fecha final.

---

## 28. Holguras y optimización de recursos

### a. Red original

Recorrido hacia adelante:

| Actividad | ES | EF |
|---|---:|---:|
| A | 0 | 3 |
| B | 3 | 9 |
| C | 3 | 8 |
| D | 9 | 13 |
| E | 8 | 15 |
| F | 15 | 17 |

Rutas:

```text
A-B-D-F = 3+6+4+2 = 15 días
A-C-E-F = 3+5+7+2 = 17 días
```

Recorrido hacia atrás y holguras:

| Actividad | LS | LF | Holgura |
|---|---:|---:|---:|
| A | 0 | 3 | 0 |
| B | 5 | 11 | 2 |
| C | 3 | 8 | 0 |
| D | 11 | 15 | 2 |
| E | 8 | 15 | 0 |
| F | 15 | 17 | 0 |

Duración: **17 días**. Ruta crítica: **A-C-E-F**.

### b. Primero C y luego B

```text
A: 0-3
C: 3-8
B: 8-14
E: 8-15
D: 14-18
F: 18-20
```

El proyecto termina en el día **20**.

### c. Primero B y luego C

```text
A: 0-3
B: 3-9
D: 9-13
C: 9-14
E: 14-21
F: 21-23
```

El proyecto termina en el día **23**.

### d. Decisión de nivelación

Conviene ejecutar **C antes que B**, porque produce una fecha final de 20 días en vez de 23. Es nivelación, no suavizamiento, porque resolver la restricción del recurso supera la holgura disponible y modifica la fecha final y la estructura crítica del cronograma.

### e. Compresión

- **Fast tracking:** superpone actividades cuya secuencia sea discrecional; aumenta riesgo y retrabajo.
- **Crashing:** incorpora recursos o costo para reducir duraciones; debe compararse costo versus reducción lograda.

Se evalúan en las actividades o dependencias que controlen la nueva fecha final. Comprimir una rama con holgura sin afectar la secuencia crítica no acortará el proyecto.

---

## 29. Costo de la calidad y grado

### a. Clasificación

| Costo | Clasificación |
|---|---|
| Capacitación, $2 M | Prevención |
| Inspecciones, $3 M | Evaluación |
| Retrabajo previo, $4 M | Falla interna |
| Garantías, $6 M | Falla externa |

### b. Totales

```text
Conformidad = prevención + evaluación
            = 2 + 3
            = $5 millones

No conformidad = falla interna + falla externa
               = 4 + 6
               = $10 millones

Costo total de la calidad = 5 + 10
                           = $15 millones
```

### c. Interpretación

La mayor carga está en no conformidad, especialmente en fallas externas. Una inversión selectiva en prevención -mejores prácticas, capacitación, automatización temprana o diseño robusto- podría reducir retrabajos y garantías. No se concluye automáticamente que toda inspección deba eliminarse.

### d. Calidad y grado

Ser de categoría básica indica **bajo grado**, no baja calidad. Si cumple consistentemente todos sus requisitos, puede ser un producto de bajo grado y alta calidad.

---

## 30. Los tres procesos y la aceptación

### a. Asociación

| Evento | Proceso |
|---:|---|
| 1 | Planificar la Gestión de la Calidad: define métricas y tolerancias |
| 2 | Gestionar la Calidad: audita y mejora procesos |
| 3 | Controlar la Calidad: mide un resultado y detecta incumplimiento |
| 4 | Controlar la Calidad: verifica el resultado corregido |
| 5 | Validar el Alcance: obtiene aceptación formal; pertenece al capítulo 5 |

### b. Verificación y aceptación

Después del evento 4 existe evidencia para considerar el entregable **verificado** respecto de esa métrica. Después del evento 5 se convierte en **aceptado** formalmente por el cliente.

### c. Estabilidad y capacidad

Un proceso puede presentar variación predecible dentro de sus límites de control y, aun así, estar centrado sobre 4,8 segundos. Ser estable no significa que el promedio y la dispersión estén dentro de la especificación máxima de 3 segundos.

### d. Retrabajo

La corrección antes de entregar es un costo de **falla interna**. Las pruebas y reinspecciones corresponden a evaluación.

---

## 31. Árbol de decisión

### a. Representación

```text
Decisión
├── Alternativa A
│   ├── 65 % -> +$18 M
│   └── 35 % -> -$12 M
└── Alternativa B
    ├── 85 % -> +$11 M
    └── 15 % -> -$5 M
```

### b. Valores esperados

```text
EMV(A) = 0,65x18 + 0,35x(-12)
       = 11,70 - 4,20
       = $7,50 millones

EMV(B) = 0,85x11 + 0,15x(-5)
       = 9,35 - 0,75
       = $8,60 millones
```

### c. Selección

Según EMV se recomienda **B**:

```text
Diferencia = 8,60 - 7,50 = $1,10 millones
```

### d. Tolerancia al riesgo

El EMV representa un promedio de muchos escenarios equivalentes, no una garantía para una decisión única. La organización también puede considerar capacidad de absorber pérdidas, apetito de riesgo, restricciones estratégicas y consecuencias no monetarias. En este caso B, además de mayor EMV, presenta una pérdida potencial menor.

---

## 32. Respuestas y reservas

### a. EMV

```text
R1 = 0,25x(-12) = -$3 millones
R2 = 0,10x(-20) = -$2 millones
O1 = 0,40x(+5)  = +$2 millones

EMV neto = -3 - 2 + 2
          = -$3 millones
```

### b. Reservas y presupuesto

La política exige sumar los EMV negativos sin descontar oportunidades:

```text
Contingencia = 3 + 2
             = $5 millones

Línea base de costos = 100 + 5
                     = $105 millones

Reserva de gestión = 10 % de 105
                   = $10,5 millones

Presupuesto total = 105 + 10,5
                  = $115,5 millones
```

### c. Residual y secundario

- La exposición menor que permanece después de transferir R2 es **riesgo residual**.
- El posible rechazo de la aseguradora introducido por la póliza es **riesgo secundario**.

### d. Procesos

- Diseñar la transferencia y demás acciones: **Planificar la Respuesta a los Riesgos**.
- Contratar la póliza y ejecutar las acciones: **Implementar la Respuesta a los Riesgos**.
- Seguir exposiciones, comprobar eficacia y detectar cambios: **Monitorear los Riesgos**.

### e. Conclusión

La contingencia se asocia a riesgos identificados y forma parte de la línea base de costos. La reserva de gestión cubre trabajo imprevisto, queda fuera de la línea base y completa el presupuesto. Fusionarlas ocultaría la causa y la autoridad de uso de los fondos.

---

# Lista de revisión para autocorrección

Antes de considerar correcta una respuesta de desarrollo, verifica:

- ¿Nombraste el concepto o proceso exacto?
- ¿Mostraste la fórmula antes del resultado?
- ¿Incluiste unidades y decimales solicitados?
- ¿Elegiste el máximo o mínimo correcto en la red?
- ¿Diferenciaste entregable verificado de aceptado?
- ¿Separaste calidad de grado y estabilidad de capacidad?
- ¿Usaste signo negativo para amenazas y positivo para oportunidades?
- ¿Terminaste con una conclusión que responde exactamente lo preguntado?

