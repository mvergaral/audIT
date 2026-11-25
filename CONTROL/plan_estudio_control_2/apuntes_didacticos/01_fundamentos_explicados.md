# Fundamentos explicados: arquitectura, calidad y requisitos

## 1. Arquitectura: la decisión antes de programar

La arquitectura responde: **¿cuáles son las partes importantes del sistema, cómo se relacionan y dónde se ejecutan?**

No es lo mismo que diseño detallado. El diseño detallado explica cómo se implementa un módulo por dentro. La infraestructura describe equipos y redes. La arquitectura conecta las necesidades del negocio con una estructura técnica.

En PagoAndes, las decisiones arquitectónicas incluyen:

- separar pagos, usuarios, reportes y notificaciones;
- decidir cómo conversar con el banco;
- decidir cómo evitar que una caída del banco derribe todo el sistema;
- decidir dónde guardar y replicar las transacciones;
- decidir cómo soportar 500 usuarios.

Una mala decisión temprana es cara porque se propaga a código, pruebas, servidores y contratos.

## 2. Arquitectura lógica y física

### Lógica

Describe módulos, capas, componentes e interfaces:

```text
Portal ciudadano → Servicio de pagos → Base de datos
                                ↘ Integración bancaria
```

### Física

Describe máquinas, redes y ubicación:

```text
Internet → Firewall → Balanceador → Servidor app 1
                              ↘ Servidor app 2
                                    ↓
                            Base primaria + réplica
```

La frase “módulo de pagos” es lógica. “Dos servidores de aplicación detrás de un balanceador” es física.

## 3. Elegir arquitectura con criterio

### Monolito

Todo se despliega como una unidad.

Es buena opción si el equipo es pequeño, el plazo es corto, la carga es conocida y se necesita simplicidad operativa. No es inferior por definición.

### Capas

Separa presentación, negocio y datos. Suele ser una buena opción empresarial porque facilita mantenimiento, pruebas y separación de responsabilidades.

### Microservicios

Separan servicios desplegables. Convienen si pagos necesita escalar aparte, si distintos equipos despliegan a ritmos diferentes o si hay requisitos de seguridad muy distintos.

No convienen solo por moda: requieren monitoreo, automatización, redes, trazas distribuidas y mayor coordinación.

### Comunicación síncrona y asíncrona

- Síncrona: se espera la respuesta. Conviene cuando el ciudadano necesita saber inmediatamente si el pago fue aprobado.
- Asíncrona: se envía un mensaje y se continúa. Conviene para correo, reportes o procesos largos.

## 4. Calidad: no es una frase bonita

La calidad debe poder medirse. “El sistema será rápido” no permite decidir si cumple.

La plantilla útil es:

> Ante [estímulo], en [condición], el sistema [respuesta], medida mediante [métrica y valor].

Ejemplo:

> Con 500 usuarios concurrentes, el 95 % de las consultas de saldo debe responder en menos de 2 segundos.

El requisito tiene condición, respuesta, métrica y umbral. Por eso puede convertirse en una prueba.

## 5. ISO/IEC 25010:2023

| Característica | Qué pregunta | PagoAndes |
|---|---|---|
| Idoneidad funcional | ¿Hace lo que debe? | Registrar y conciliar pagos |
| Eficiencia de desempeño | ¿Responde bien? | Menos de 2 segundos |
| Compatibilidad | ¿Convive con otros? | API bancaria |
| Capacidad de interacción | ¿Es usable y accesible? | Pago desde móvil |
| Fiabilidad | ¿Funciona y se recupera? | 99,9 % disponible |
| Seguridad | ¿Protege datos y operaciones? | Cifrado y bitácora |
| Mantenibilidad | ¿Es fácil cambiarlo? | Módulos desacoplados |
| Flexibilidad | ¿Se adapta y escala? | Agregar nuevos bancos |
| Seguridad operacional | ¿Limita el daño ante fallas? | Bloqueo de operaciones sospechosas |

No memorices solo los nombres. Relaciona cada característica con una decisión arquitectónica y una métrica.

## 6. RTO y RPO

- **RTO:** tiempo máximo para recuperar el servicio.
- **RPO:** cantidad máxima de información que se puede perder.

PagoAndes exige RTO de 15 minutos y RPO 0.

RPO 0 significa que una transacción confirmada no puede perderse. Una réplica asíncrona podría quedar atrasada algunos segundos, por lo que no garantiza RPO 0. Una replicación sincrónica es más apropiada, aunque aumenta latencia y complejidad.

Activo-activo puede recuperar más rápido, pero cuesta más y exige resolver conflictos. Activo-pasivo es más simple, pero el cambio de sitio puede tardar.

## 7. Requisitos y alcance

Tipos importantes:

- funcional: qué hace el sistema;
- no funcional: bajo qué condiciones opera;
- transición: migración, capacitación y puesta en marcha;
- de calidad: cómo se verifica un entregable.

Incorrecto:

> El sistema manejará adecuadamente los errores.

Correcto:

> Si la pasarela no responde en 10 segundos, el pago queda pendiente, se reintenta tres veces y se informa al ciudadano.

### Tres conceptos que suelen confundirse

- Controlar calidad: el equipo prueba e inspecciona el entregable.
- Validar alcance: el cliente acepta formalmente el entregable.
- Controlar alcance: se verifica que se entregue lo incluido y no se agregue trabajo no aprobado.

## Practica guiada

1. Redacta un requisito medible de rendimiento.
2. Redacta uno de seguridad.
3. Decide si usarías comunicación síncrona para autorizar un pago y asíncrona para enviar un correo. Justifica.
4. Explica por qué RPO 0 no se satisface con un respaldo diario.
