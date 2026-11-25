# Requisitos, alcance, EDT y cronograma

## 1. Tipos de requisitos

| Tipo | Qué describe | Ejemplo en PagoAndes |
|---|---|---|
| Negocio | Necesidad de la organización | Reducir pagos presenciales |
| Interesado | Necesidad de un grupo | El tesorero necesita reportes |
| Funcional | Qué hace el sistema | Registrar un pago |
| No funcional | Condición del sistema | Responder en menos de 2 segundos |
| Transición | Paso del estado antiguo al nuevo | Migrar pagos históricos |
| Proyecto | Restricción del proyecto | Terminar en 6 meses |
| Calidad | Criterio para aceptar un entregable | 99,9 % de disponibilidad |

## 2. Requisito verificable

Deficiente:

> El sistema debe manejar adecuadamente los errores.

Mejor:

> Si la pasarela no responde en 10 segundos, el sistema registra el pago como pendiente, reintenta tres veces y notifica al usuario.

La palabra “adecuadamente”, sin umbral, no permite verificar ni aceptar el requisito.

## 3. Alcance y calidad

- Validar alcance: el cliente acepta formalmente el entregable.
- Controlar calidad: el equipo verifica requisitos, estándares y pruebas.
- Controlar alcance: se evita entregar trabajo adicional o dejar trabajo fuera.

Ejemplo: el equipo prueba el módulo de pagos; eso es control de calidad. El cliente firma que lo recibe; eso es validación del alcance.

## 4. EDT

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

Reglas:

- La suma de los hijos representa el 100 % del padre.
- Un paquete de trabajo debería durar entre 8 y 80 horas.
- La EDT representa trabajo y entregables, no solo departamentos.

## 5. Dependencias

- Obligatoria: impuesta por la naturaleza del trabajo.
- Discrecional: elegida por el equipo; puede cambiarse con justificación.
- Externa: depende de una persona, proveedor u organización externa.

Para acortar un proyecto sin agregar recursos, conviene revisar dependencias discrecionales. No se debe romper una dependencia obligatoria.

## 6. Ruta crítica y holgura

La ruta crítica es la secuencia de actividades con holgura cero. Si una actividad crítica se atrasa, se atrasa el proyecto.

Procedimiento:

1. Calcular inicio y término temprano.
2. Calcular inicio y término tardío desde el final hacia atrás.
3. Calcular holgura.
4. Marcar las actividades con holgura cero.

Una actividad no crítica puede atrasarse hasta su holgura sin mover la fecha final.

## Ejercicio

Usa estas actividades:

| Actividad | Duración | Predecesoras |
|---|---:|---|
| A Requisitos | 4 días | - |
| B Arquitectura | 3 días | A |
| C Desarrollo | 8 días | B |
| D Integración bancaria | 5 días | B |
| E Pruebas | 4 días | C, D |
| F Capacitación | 2 días | E |

Calcula duración total, rutas posibles, ruta crítica y holgura de D.
