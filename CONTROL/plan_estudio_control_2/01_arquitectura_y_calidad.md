# Arquitectura y calidad

## 1. Qué es arquitectura

La arquitectura define los elementos principales del sistema y sus relaciones:

- módulos;
- responsabilidades;
- integraciones;
- flujo de datos y control;
- protocolos;
- ubicación en hardware.

No es lo mismo que diseño detallado ni que infraestructura. La arquitectura decide la estructura general; el diseño explica cómo se implementa internamente; la infraestructura muestra sobre qué equipos y redes se ejecuta.

## 2. Arquitectura lógica y física

### Lógica

Organiza el software: módulos, capas, servicios e interfaces. No depende de marcas específicas de servidores.

### Física

Organiza la ejecución: servidores, redes, almacenamiento, zonas, respaldos y ubicaciones.

### En PagoAndes

```text
Portal web / app
        ↓
Servicios de negocio
        ↓
Base de datos de pagos
        ↓
Capa de integración bancaria
```

La arquitectura lógica dice que existe una capa de pagos. La arquitectura física dice que esa capa se ejecuta en dos instancias detrás de un balanceador.

## 3. Cuándo elegir cada estilo

### Monolito

Conviene cuando el equipo es pequeño, el plazo es corto, la carga es conocida y la operación debe ser simple.

No conviene si partes del sistema necesitan escalar de forma independiente o si varios equipos deben desplegar por separado.

### Capas

Conviene para sistemas empresariales con responsabilidades relativamente claras. Facilita mantenimiento y pruebas.

### Microservicios

Convienen cuando hay módulos con escalamiento, ciclos de despliegue, equipos o requisitos de seguridad diferentes.

No se justifican solamente porque sean modernos. Aumentan redes, monitoreo, despliegues y problemas de consistencia.

### Eventos

Convienen cuando el proceso es asíncrono, largo o debe desacoplarse. Por ejemplo, enviar una notificación después de confirmar un pago.

No son ideales si el usuario necesita una respuesta inmediata y simple.

## 4. ISO/IEC 25010:2023

Las nueve características son:

1. Idoneidad funcional.
2. Eficiencia de desempeño.
3. Compatibilidad.
4. Capacidad de interacción.
5. Fiabilidad.
6. Seguridad.
7. Mantenibilidad.
8. Flexibilidad.
9. Seguridad operacional.

### Ejemplos en PagoAndes

- Rendimiento: 95 % de los pagos responde en menos de 2 segundos.
- Disponibilidad: 99,9 % mensual.
- Seguridad: datos personales cifrados y accesos registrados.
- Escalabilidad: soportar el doble de usuarios agregando instancias.
- Recuperabilidad: recuperación en máximo 15 minutos.

Una frase como “el sistema será rápido” es una intención. Un requisito de calidad debe tener condición, respuesta, métrica y valor.

## 5. RTO, RPO y disponibilidad

- RTO: tiempo máximo para recuperar el servicio.
- RPO: punto máximo de pérdida de datos aceptable.

Si RPO = 0, la replicación debe ser sincrónica: el dato se confirma en ambos sitios antes de terminar la operación.

Si solo se exigiera RPO de 30 minutos, podría bastar replicación asíncrona, que suele ser más simple y rápida, aceptando perder como máximo 30 minutos de información.

## Ejercicios

1. Escribe tres requisitos de calidad medibles para PagoAndes.
2. Explica por qué usarías capas antes que microservicios.
3. Una base técnica exige RTO de 10 minutos y RPO de 0. Propón una solución y justifícala.
4. Clasifica: disponibilidad, seguridad, rendimiento, mantenibilidad y escalabilidad.
