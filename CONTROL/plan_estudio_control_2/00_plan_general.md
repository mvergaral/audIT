# Plan general de estudio - Control 2

## Caso transversal: PagoAndes

PagoAndes es una plataforma para que ciudadanos paguen cuentas municipales. Tiene portal web, aplicación para funcionarios, integración con bancos, notificaciones y base de datos de pagos.

Condiciones del caso:

- 500 usuarios concurrentes.
- Disponibilidad exigida: 99,9 % mensual.
- RTO: 15 minutos.
- RPO: 0.
- Plazo: 6 meses.
- Presupuesto fijo.
- La pasarela de pagos es un proveedor externo.

Durante el estudio debes actuar como jefe de proyecto: definir, estimar, planificar, controlar calidad, gestionar riesgos y contratar servicios.

## Calendario recomendado

| Día | Tema principal | Producto que debes completar |
|---|---|---|
| Jueves | Arquitectura y calidad | Diseño lógico y requisitos medibles |
| Viernes | Requisitos, alcance, EDT y cronograma | EDT y red de actividades |
| Sábado | Estimación, riesgos y adquisiciones | Estimación completa y ficha de proveedor |
| Domingo | Integración y simulacro | Prueba completa sin apuntes |
| Lunes | Repaso final | Fórmulas, conceptos confundibles y errores |

## Método de estudio

Para cada concepto responde:

1. ¿Qué significa?
2. ¿Cómo se aplica o calcula?
3. ¿Cuándo conviene usarlo?
4. ¿Qué alternativa podría confundirse con él?

No estudies solamente leyendo. Después de cada sección cierra el documento e intenta explicar PagoAndes con tus propias palabras.

## Fórmulas imprescindibles

```text
UUCP = UAW + UUCW
UCP = UUCP × TCF × EF
E = UCP × CF
Esfuerzo total = E / 0,40
VME = Probabilidad × Impacto monetario
PUE = Energía total / Energía TI
DCiE = Energía TI / Energía total
```

## Prioridad si queda poco tiempo

1. Puntos de Casos de Uso.
2. Ruta crítica, EDT y holguras.
3. Riesgos y VME.
4. Calidad versus validación del alcance.
5. RTO, RPO, PUE y DCiE.
6. Adquisiciones y contratos.
7. Arquitecturas y patrones.
