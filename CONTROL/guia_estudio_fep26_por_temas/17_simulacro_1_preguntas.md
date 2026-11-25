# Simulacro 1 - Control integral FEP26

Responde primero sin revisar los apuntes. Después compara con la pauta razonada. En preguntas abiertas, una respuesta sólida debe contener **concepto + aplicación + justificación**.

---

# Parte A — Selección múltiple

## 1

¿Cuál elemento forma parte de la línea base del alcance?

A. Lista de actividades, cronograma y costos  
B. Declaración del alcance, EDT y diccionario de la EDT  
C. Registro de riesgos e informe de calidad  
D. Acta de constitución y caso de negocio

## 2

El cliente pide una nueva función después de aprobar el alcance. ¿Qué debe hacerse primero?

A. Agregarla si el equipo cree que puede terminarla  
B. Rechazarla porque la línea base nunca puede cambiar  
C. Registrar y analizar la solicitud mediante el proceso de cambios  
D. Modificar la EDT para calcular su costo

## 3

¿Cuál afirmación describe mejor la regla del 100 %?

A. Todo paquete debe durar menos de 100 horas  
B. La EDT contiene el 100 % del trabajo del proyecto, incluido el de gestión  
C. Cada entregable debe estar terminado antes de iniciar otro  
D. El presupuesto debe estar asignado en un 100 % al inicio

## 4

¿Cuál es un ejemplo de relación inicio–inicio?

A. Las pruebas comienzan cuando termina el desarrollo  
B. La documentación comienza cuando comienza el desarrollo  
C. La revisión termina cuando comienza la liberación  
D. La capacitación termina cuando termina el despliegue

## 5

Una actividad tiene ES = 5, EF = 9, LS = 7 y LF = 11. Su holgura total es:

A. 2  
B. 4  
C. 7  
D. 11

## 6

¿Qué técnica puede alargar el cronograma al resolver sobreasignaciones?

A. Suavizamiento de recursos  
B. Nivelación de recursos  
C. Fast tracking  
D. Análisis de Pareto

## 7

El jefe decide comenzar pruebas antes de terminar todo el desarrollo para recuperar tiempo. Esto es:

A. Intensificación  
B. Transferencia  
C. Ejecución rápida  
D. Nivelación

## 8

En UCP, un actor humano que usa una interfaz gráfica normalmente es:

A. Simple, peso 1  
B. Medio, peso 2  
C. Complejo, peso 3  
D. Complejo, peso 15

## 9

Un caso de uso con seis transacciones se clasifica, según la lectura del curso, como:

A. Simple, peso 5  
B. Medio, peso 10  
C. Complejo, peso 15  
D. No se puede estimar

## 10

Si la estimación de programación es 2.000 HH y programación representa 40 % del ciclo de vida, el esfuerzo total es:

A. 800 HH  
B. 2.000 HH  
C. 4.000 HH  
D. 5.000 HH

## 11

“La API cambió ayer y el conector ya no funciona” corresponde principalmente a:

A. Riesgo  
B. Problema actual  
C. Oportunidad  
D. Supuesto

## 12

¿Qué estrategia de amenaza reduce probabilidad o impacto sin eliminar necesariamente la causa?

A. Explotar  
B. Transferir  
C. Mitigar  
D. Mejorar

## 13

¿Qué estrategia de oportunidad busca garantizar que ocurra?

A. Aceptar  
B. Explotar  
C. Compartir  
D. Mitigar

## 14

¿Cuál corresponde a costo de falla externa?

A. Capacitación preventiva  
B. Revisión de diseño  
C. Retrabajo antes de liberar  
D. Multa por defecto descubierto en producción

## 15

Un gráfico muestra un proceso estable dentro de sus límites de control, pero todas las mediciones superan el máximo exigido por el cliente. La interpretación correcta es:

A. El proceso está bajo control y es capaz  
B. El producto tiene alta calidad porque no hay puntos fuera de control  
C. El proceso es estable, pero no cumple la especificación  
D. Los límites de control deben reemplazarse por los del cliente

## 16

¿Qué proceso produce entregables verificados?

A. Gestionar la Calidad  
B. Controlar la Calidad  
C. Validar el Alcance  
D. Recopilar Requisitos

---

# Parte B — Respuesta breve

## 17

Explica la diferencia entre alcance del producto y alcance del proyecto usando SaludConecta.

## 18

¿Por qué la EDT no debe confundirse con el cronograma?

## 19

¿En qué se diferencian un paquete de trabajo, una cuenta de control y un paquete de planificación?

## 20

Compara estimación análoga y estimación ascendente. Indica cuándo usarías cada una.

## 21

Explica por qué esfuerzo y duración no son equivalentes.

## 22

Redacta correctamente un riesgo usando causa–evento–efecto.

## 23

¿Qué diferencia existe entre un riesgo residual y uno secundario?

## 24

Compara prevención, evaluación, falla interna y falla externa con un ejemplo de cada una.

## 25

Explica la diferencia entre Gestionar la Calidad, Controlar la Calidad y Validar el Alcance.

## 26

¿Por qué un diagrama de Pareto no reemplaza un análisis de causa raíz?

---

# Parte C — Cálculos

## 27. Tres valores

Una actividad tiene O = 5, M = 8 y P = 17 días.

a. Calcula la duración triangular.  
b. Calcula la duración beta/PERT.  
c. Calcula la desviación estándar aproximada.

## 28. Ruta crítica

| Actividad | Duración | Predecesora |
|---|---:|---|
| A | 2 | — |
| B | 5 | A |
| C | 3 | A |
| D | 4 | B |
| E | 6 | C |
| F | 2 | D, E |

Calcula la duración y la ruta crítica.

## 29. UCP básico

Un proyecto posee:

- 2 actores simples, 2 medios y 3 complejos;
- 3 casos de uso simples, 4 medios y 2 complejos;
- TCF = 1,00;
- EF = 0,90.

Calcula UAW, UUCW, UUCP y UCP.

## 30. Esfuerzo UCP

Usando el resultado de la pregunta 29 y un factor de 20 HH/UCP:

a. calcula esfuerzo de programación;  
b. calcula esfuerzo total si programación es 40 %;  
c. calcula duración simplificada con 5 personas, 160 HH/mes y 75 % de disponibilidad.

## 31. EMV

Un proyecto tiene:

- amenaza A: 30 % de probabilidad de perder $20 millones;
- amenaza B: 10 % de probabilidad de perder $50 millones;
- oportunidad C: 40 % de probabilidad de ahorrar $15 millones.

Calcula el EMV neto.

## 32. Pareto

Se observan 200 defectos:

- validación de datos: 90;
- integración: 50;
- interfaz: 30;
- permisos: 20;
- documentación: 10.

¿Qué porcentaje representan las dos primeras categorías y qué decisión inicial sugiere el análisis?

---

# Parte D — Casos de aplicación

## 33. Solicitud de cambio

El patrocinador solicita una aplicación móvil durante la ejecución y exige conservar fecha y presupuesto. Explica cómo actuarías y qué áreas analizarías.

## 34. Atraso y compresión

Una actividad no crítica tiene cinco días de holgura. El proyecto está tres días atrasado por una actividad crítica. El gerente propone pagar horas extra en la actividad no crítica. Evalúa la propuesta y recomienda una alternativa.

## 35. Calidad y aceptación

El módulo aprobó todas las pruebas técnicas, pero la directora clínica se niega a aceptarlo porque el flujo no coincide con el proceso acordado. ¿Existe contradicción? Explica los procesos involucrados.

## 36. Riesgo versus problema

El proveedor avisó que el ambiente de prueba no estará disponible este mes. En el registro figuraba como riesgo y existía un simulador como contingencia. ¿Qué debe hacer el equipo ahora?

---

