# Módulo 1 - Arquitectura, calidad, continuidad y entrega

## 1. Qué es arquitectura de software

La arquitectura es el diseño de más alto nivel: identifica elementos importantes, responsabilidades, relaciones, flujos de datos, protocolos y ubicación de los componentes.

No es:

- un diagrama de clases detallado;
- una lista de servidores sin relación con el software;
- una elección de tecnología por moda.

La arquitectura toma decisiones costosas de cambiar. En PagoAndes, escoger una base de datos centralizada, una arquitectura distribuida o una integración síncrona afectará desarrollo, pruebas, operación y precio.

## 2. Vistas 4+1

| Vista | Pregunta | Público |
|---|---|---|
| Lógica | ¿Cómo se divide el sistema? | Analistas y usuarios |
| Proceso | ¿Qué corre en paralelo y cómo se coordina? | Integradores |
| Desarrollo | ¿Cómo se organiza el código y los equipos? | Desarrollo |
| Física | ¿Dónde se ejecuta cada componente? | Operaciones |
| Escenarios | ¿Cómo atraviesa un caso las otras vistas? | Todos |

Un escenario crítico de PagoAndes, como “confirmar pago”, debe poder trazarse desde el usuario hasta la integración bancaria, base de datos y respuesta.

## 3. Arquitectura lógica versus física

### Lógica

```text
Portal ciudadano → Servicios de negocio → Datos
                               ↘ Integración bancaria
```

### Física

```text
Internet → WAF → Balanceador → App 1 / App 2
                            → BD primaria / réplica
```

La lógica organiza el software. La física organiza servidores, redes, almacenamiento, capacidad, ubicación y redundancia.

## 4. Estilos y cuándo usarlos

### Monolito

Una unidad de despliegue. Conviene para equipos pequeños, plazo corto, carga conocida y baja complejidad operativa.

### Monolito modular

Un despliegue, pero con fronteras claras entre módulos. Es un buen punto medio: mantiene operación simple y permite extraer un módulo después.

### Capas / n-capas

Separa presentación, negocio, datos e integración. Es apropiada para aplicaciones empresariales porque facilita mantenimiento y escalamiento por niveles.

### Cliente-servidor

Un cliente solicita y un servidor responde. Es común en sistemas heredados, pero los clientes pesados pueden ser difíciles de actualizar y escalar.

### Microservicios

Servicios autónomos y desplegables por separado. Convienen cuando hay escalamiento independiente, equipos autónomos, ciclos de despliegue distintos o tecnologías diferentes. No convienen solo por moda: exigen DevOps, observabilidad, redes y manejo de consistencia.

### Eventos

Componentes publican y consumen eventos. Conviene para procesos largos, desacoplados o que deben sobrevivir a una caída temporal del consumidor. Exige manejar orden, duplicados, reintentos e idempotencia.

### Serverless

Funciones ejecutadas por evento sin administrar servidores. Conviene para cargas intermitentes y pequeñas, pero hay que revisar latencia, dependencia del proveedor y costos variables.

## 5. Atributos de calidad ISO/IEC 25010:2023

1. Idoneidad funcional.
2. Eficiencia de desempeño.
3. Compatibilidad.
4. Capacidad de interacción.
5. Fiabilidad.
6. Seguridad.
7. Mantenibilidad.
8. Flexibilidad.
9. Seguridad operacional.

El modelo 2023 no es simplemente la versión 2011 con redacción actualizada: cambia la organización y agrega seguridad operacional como característica.

### Calidad debe ser medible

Incorrecto: “el sistema será rápido”.

Correcto: “Con 500 usuarios concurrentes, el 95 % de las consultas responde en menos de 2 segundos”.

Plantilla:

```text
Ante [estímulo], en [condición], el sistema [respuesta],
medida mediante [métrica y valor].
```

## 6. Disponibilidad, RTO y RPO

Disponibilidad es el porcentaje de tiempo en que el servicio está operativo.

- RTO: tiempo máximo para recuperar el servicio.
- RPO: cantidad máxima de datos que se puede perder.

RTO de 15 minutos no significa que no se pierdan datos. RPO 0 significa que no se puede perder ninguna transacción confirmada.

### Replicación

- Sincrónica: confirma el dato en ambos sitios; apropiada para RPO 0, pero agrega latencia.
- Asíncrona: replica después; suele ser más rápida y barata, pero puede perder los últimos datos.

### Activo-activo y activo-pasivo

- Activo-activo: ambos sitios procesan. Mejor recuperación, mayor complejidad.
- Activo-pasivo: uno espera. Menor costo, pero el cambio puede tardar.

## 7. Seguridad y operación

Una solución expuesta a internet necesita, según el caso:

- segmentación de red;
- firewall y WAF;
- cifrado en tránsito y reposo;
- gestión de identidad;
- bitácora auditable;
- pruebas de intrusión;
- recuperación ante incidentes.

La seguridad operacional busca limitar el daño cuando algo falla: bloqueo, modo degradado, límites y procedimientos de reversa.

## 8. Nube y entrega

- IaaS: se arriendan máquinas y redes.
- PaaS: se usa una plataforma administrada.
- SaaS: se consume una aplicación completa.

Ambientes típicos:

```text
Desarrollo → QA → Preproducción → Producción
```

La separación permite probar antes de afectar usuarios. CI/CD automatiza construcción, pruebas y despliegue, pero no elimina la necesidad de criterios de aceptación.

## Preguntas de control relacionadas

1. ISO/IEC 25010.
2. RTO/RPO.
3. Requisitos no verificables.
10. PUE/DCiE.
11. Densidad térmica.
12. Disponibilidad compuesta.
16. UPS, PUE y generador.
