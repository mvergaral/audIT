# Arquitectura lógica de software

## 1. Por qué importa en una oferta

La arquitectura describe los elementos estructurales del sistema, sus responsabilidades y relaciones. Son decisiones tempranas, difíciles de revertir, que determinan alcance, esfuerzo, infraestructura, riesgos y calidad.

No es un diagrama vistoso ni una lista de productos. Debe permitir defender:

- qué módulos se construirán;
- cómo colaboran;
- dónde están las fronteras;
- qué atributos de calidad justifican la estructura;
- qué se compra o integra;
- qué consecuencias y costos tiene la decisión.

## 2. Vistas y niveles

Una sola vista no responde todo:

- **Contexto:** sistema, usuarios y externos.
- **Contenedores:** aplicaciones, servicios, bases y canales.
- **Componentes:** responsabilidades internas relevantes.
- **Despliegue/física:** nodos, redes y ambientes.
- **Escenarios:** cómo se comporta frente a casos significativos.

El modelo 4+1 de Kruchten organiza vistas lógica, desarrollo, procesos, física y escenarios. C4 ofrece contexto, contenedores, componentes y código. Se elige según la pregunta; un diagrama de clases no reemplaza la arquitectura de despliegue.

## 3. Atributos de calidad como motor

ISO/IEC 25010:2023 organiza nueve características: adecuación funcional, eficiencia de desempeño, compatibilidad, capacidad de interacción, fiabilidad, seguridad, mantenibilidad, flexibilidad y seguridad operacional.

No basta nombrarlas. Un escenario de calidad tiene:

```text
Fuente → estímulo → condición → componente → respuesta → métrica
```

Ejemplo: “Durante hora punta, 500 usuarios consultan resultados; el portal responde con P95 ≤ 2 s sin errores superiores a 1 %”.

## 4. Registro de decisión arquitectónica, ADR

Un ADR documenta:

1. contexto y problema;
2. alternativas;
3. criterios;
4. decisión;
5. consecuencias positivas y negativas.

Ejemplo: elegir monolito modular en vez de microservicios porque el equipo es pequeño y el plazo corto. Se gana simplicidad operativa; se acepta menor independencia de despliegue.

## 5. Estilos principales

### Monolito

Una unidad desplegable concentra funcionalidad.

**Conviene:** alcance moderado, equipo pequeño, dominio todavía cambiante y necesidad de entregar rápido.

**Ventajas:** despliegue, pruebas y transacciones simples.  
**Riesgos:** acoplamiento y crecimiento desordenado.

Un **monolito modular** mantiene fronteras internas claras y puede evolucionar; no equivale a “código mezclado”.

### Arquitectura en capas

Separa presentación, aplicación/negocio y datos. Reduce dependencias directas y facilita pruebas.

Conviene en sistemas de información clásicos. Falla cuando todas las capas se convierten en pasos obligatorios sin sentido o cuando lógica de negocio termina en la interfaz/base.

### Cliente-servidor, tres y N capas

Cliente-servidor separa consumidor y servicio. Tres capas añade presentación, lógica y datos; N capas agrega responsabilidades como integración, seguridad o servicios.

No confundir capa lógica con nodo físico: varias capas pueden ejecutarse en una máquina o una capa en muchos nodos.

### Microservicios

Servicios autónomos alineados a capacidades de negocio, con despliegue y datos suficientemente independientes.

**Conviene:** dominio comprendido, equipos independientes, escalado desigual y alta madurez operativa.

**Costo:** red, observabilidad, seguridad, versionado, consistencia, pruebas y operación distribuida. Para seis personas y ocho meses, elegir microservicios solo “porque escalan” probablemente aumenta riesgo.

### Arquitectura orientada a eventos

Productores publican eventos y consumidores reaccionan. Reduce acoplamiento temporal y absorbe picos.

**Conviene:** notificaciones, integración asincrónica, auditoría y procesos desacoplados.  
**Riesgos:** duplicados, orden, trazabilidad, consistencia eventual y reintentos.

Se necesita idempotencia: procesar dos veces el mismo evento no debe duplicar efectos.

## 6. Comparación para SaludConecta

| Criterio | Monolito modular | Microservicios | Eventos |
|---|---:|---:|---:|
| Velocidad inicial | Alta | Baja | Media |
| Complejidad operativa | Baja | Alta | Alta |
| Independencia de despliegue | Media | Alta | Media/alta |
| Transacciones consistentes | Simple | Difícil | Eventual |
| Equipo pequeño | Adecuado | Generalmente excesivo | Solo en puntos útiles |

Decisión razonable: monolito modular para núcleo, adaptadores separados para integraciones y mensajería para notificaciones. No hay obligación de elegir un único estilo para todo.

## 7. API e integración

### REST

Modela recursos sobre HTTP. Debe definir contratos, autenticación, versionado, códigos de estado, paginación, idempotencia y errores. OpenAPI documenta el contrato.

### API Gateway

Punto de entrada para enrutamiento, autenticación, límites y observabilidad. Ayuda con múltiples servicios, pero puede transformarse en punto único de falla o concentrar lógica indebida.

### Resiliencia

- timeout: no esperar indefinidamente;
- reintento con backoff: repetir fallas transitorias;
- circuit breaker: dejar de invocar un servicio caído;
- bulkhead: aislar recursos para que una falla no consuma todo;
- fallback: respuesta degradada;
- idempotencia: reintentar sin duplicar efectos.

Reintentar sin límite empeora una caída. Cada patrón resuelve un modo de falla específico.

### Integración síncrona o asíncrona

| Síncrona | Asíncrona |
|---|---|
| Respuesta inmediata | Desacopla tiempo |
| Flujo simple | Tolera indisponibilidad temporal |
| Dependencia directa | Requiere colas, seguimiento y compensación |

Consultar saldo para confirmar pago suele ser síncrono; enviar notificación puede ser asíncrono.

## 8. Datos distribuidos

Una base compartida simplifica consistencia, pero acopla módulos. Bases por servicio aumentan autonomía, pero exigen integración y consistencia eventual.

Una **saga** coordina transacciones distribuidas mediante pasos y compensaciones. No “deshace” necesariamente el mundo real; ejecuta una acción compensatoria, como anular una reserva.

## 9. Trazabilidad arquitectónica

| Requisito/riesgo | Decisión | Evidencia |
|---|---|---|
| P95 ≤ 2 s | caché + prueba de carga | diagrama y plan de pruebas |
| API inestable | adaptador + contrato versionado | componente, actividad y riesgo |
| auditoría | eventos inmutables | módulo y criterio de aceptación |

## 10. Errores frecuentes

1. Elegir microservicios por moda.
2. Dibujar productos comerciales en vez de responsabilidades.
3. Omitir integraciones y fronteras.
4. No declarar consecuencias negativas.
5. Confundir arquitectura lógica con física.
6. Prometer calidad sin escenario ni métrica.
7. Agregar un bus/API Gateway como respuesta universal.

## 11. Autoevaluación

1. ¿Por qué un monolito modular puede ser mejor que microservicios?
2. ¿Cuándo usarías eventos en SaludConecta?
3. Escribe un ADR resumido para la integración de laboratorio.
4. ¿Qué diferencia hay entre capa y nodo?
5. ¿Qué problema resuelven circuit breaker e idempotencia?
6. Redacta un escenario de calidad completo.

