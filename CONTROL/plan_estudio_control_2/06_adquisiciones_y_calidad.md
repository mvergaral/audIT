# Adquisiciones y calidad

## 1. Qué son las adquisiciones

Adquirir significa comprar o contratar productos y servicios fuera del equipo del proyecto.

En PagoAndes se podrían adquirir:

- pasarela bancaria;
- infraestructura en la nube;
- servicio de mensajería;
- certificados digitales;
- soporte especializado.

## 2. Construir o comprar

### Comprar o contratar conviene cuando:

- el proveedor ya tiene certificaciones;
- el componente es estándar;
- desarrollarlo internamente demora demasiado;
- el riesgo regulatorio es alto;
- se necesita soporte especializado.

### Construir conviene cuando:

- el componente es estratégico y diferenciador;
- no existe un producto adecuado;
- se necesita control total;
- el costo de dependencia sería mayor que el costo de desarrollo.

Para PagoAndes conviene contratar la conexión bancaria, pero construir la lógica propia de conciliación y reportes. Así se aprovecha la especialización del proveedor sin entregar todo el control del negocio.

## 3. Riesgos de un proveedor

Contratar una pasarela puede reducir el riesgo técnico, pero crea:

- dependencia;
- riesgo de indisponibilidad;
- cambios de API;
- aumento de precios;
- problemas de salida;
- riesgo de seguridad o privacidad.

Por eso una adquisición debe incluir criterios medibles y un plan de salida.

## 4. Qué debe contener el contrato

- alcance exacto;
- entregables;
- fechas;
- criterios de aceptación;
- disponibilidad;
- tiempo de respuesta;
- soporte;
- penalizaciones;
- seguridad;
- propiedad de datos;
- respaldos;
- continuidad;
- procedimiento de término y migración.

Una frase como “disponibilidad permanente” es ambigua. Debe convertirse en “99,9 % mensual, excluyendo ventanas de mantenimiento informadas con cinco días de anticipación”.

## 5. Calidad: planificar, asegurar y controlar

- Planificar calidad: definir estándares, métricas y criterios.
- Asegurar calidad: revisar el proceso y verificar que se trabaja conforme al plan.
- Controlar calidad: inspeccionar y probar el producto.
- Validar alcance: obtener aceptación formal del cliente.

Ejemplo:

1. Se define que todos los pagos deben tener prueba automatizada.
2. Se audita que el equipo esté ejecutando esas pruebas.
3. Se ejecutan las pruebas y se registran defectos.
4. El cliente firma la recepción del módulo.

## 6. Criterios de aceptación

Un criterio debe ser objetivo:

> Con 500 usuarios concurrentes, el 95 % de las consultas debe responder en menos de 2 segundos.

Debe poder verificarse mediante una prueba, medición o inspección.

## Ejercicios

1. Redacta cinco cláusulas para contratar la pasarela bancaria.
2. Enumera dos riesgos residuales de contratarla.
3. Escribe tres criterios de aceptación para PagoAndes.
4. Explica la diferencia entre asegurar calidad y controlar calidad.
