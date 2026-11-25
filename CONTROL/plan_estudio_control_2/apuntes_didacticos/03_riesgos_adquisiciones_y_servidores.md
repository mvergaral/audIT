# Riesgos, adquisiciones y sala de servidores

## 1. Riesgos: una forma de pensar

Un riesgo es un evento incierto que puede afectar los objetivos. Para analizarlo separa:

- causa: por qué podría ocurrir;
- evento de riesgo: qué podría ocurrir;
- efecto: qué consecuencia tendría;
- respuesta: qué harás antes o después.

Ejemplo PagoAndes:

- causa: la API bancaria está poco documentada;
- riesgo: el proveedor cambia la API durante el desarrollo;
- efecto: integración atrasada y costo adicional;
- respuesta: prueba de concepto, adaptador y cláusula contractual.

## 2. VME y respuestas

```text
VME = Probabilidad × Impacto monetario
```

Con 30 % y $5.000.000:

```text
VME = 0,30 × 5.000.000 = $1.500.000
```

Respuestas a amenazas:

- evitar: cambiar el plan para eliminar la amenaza;
- mitigar: reducir probabilidad o impacto;
- transferir: contratar, asegurar o garantizar;
- aceptar: monitorear y reservar dinero;
- escalar: subir la decisión a una autoridad superior.

### Residual y secundario

Si contratas una pasarela, queda un riesgo residual de indisponibilidad. Al mismo tiempo aparece un riesgo secundario de dependencia del proveedor.

Agregar más personas no siempre es una mitigación. Si no conoces una interfaz, una prueba de concepto entrega información; más personas solo pueden aumentar coordinación.

## 3. Adquisiciones: construir o comprar

Comprar conviene si el proveedor ya tiene certificaciones, conexiones, soporte y experiencia que costaría mucho desarrollar.

Construir conviene si el componente es diferenciador, estratégico o necesita control especial sobre datos y evolución.

Para PagoAndes:

- comprar la conexión bancaria puede ser razonable;
- construir la conciliación interna puede proteger el conocimiento del negocio;
- el contrato debe permitir cambiar de proveedor.

## 4. Qué debe decir el contrato

No basta con “el proveedor debe entregar un servicio de calidad”. Debe definir:

- alcance;
- entregables;
- fechas;
- criterios de aceptación;
- disponibilidad;
- tiempo de respuesta;
- soporte;
- seguridad;
- respaldo;
- propiedad y portabilidad de datos;
- aviso previo de cambios;
- penalizaciones;
- procedimiento de salida.

“Disponibilidad permanente” no es verificable. “99,9 % mensual, con mantenimiento avisado con cinco días de anticipación” sí.

## 5. Calidad: cuatro procesos distintos

### Planificar calidad

Definir estándares, métricas, pruebas, responsables y criterios antes de construir.

### Asegurar calidad

Evaluar el proceso. Por ejemplo, revisar que cada requisito tenga una prueba asociada.

### Controlar calidad

Evaluar el producto. Por ejemplo, ejecutar una prueba de carga y registrar defectos.

### Validar alcance

El cliente acepta formalmente el entregable.

Secuencia completa:

```text
Requisito → prueba definida → prueba ejecutada → resultado → aceptación del cliente
```

## 6. Sala de servidores

```text
PUE = Energía total / Energía TI
DCiE = Energía TI / Energía total
```

Para 6 racks de 4 kW:

```text
Carga TI = 6 × 4 = 24 kW
UPS con 25 % = 24 × 1,25 = 30 kW
Sitio con PUE 1,6 = 24 × 1,6 = 38,4 kW
Generador con 40 % = 38,4 × 1,4 = 53,76 kW
```

El margen de UPS se aplica a la carga TI. El PUE convierte carga TI en potencia total del sitio.

## 7. Continuidad

- Activo-activo: ambos sitios trabajan; más disponibilidad y más complejidad.
- Activo-pasivo: uno trabaja y otro espera; menor costo, pero recuperación más dependiente del cambio.
- Respaldo diario: sirve para recuperar datos, pero no cumple RPO 0.

Con RTO 15 minutos y RPO 0, PagoAndes necesita replicación continua y un procedimiento de recuperación probado.

## Ejercicios

1. Identifica causa, riesgo y efecto de una mala calidad de datos.
2. Redacta tres cláusulas para la pasarela.
3. Escribe una actividad de aseguramiento y una de control de calidad.
4. Dimensiona UPS y generador para 10 racks de 5 kW, PUE 1,5 y margen de generador de 30 %.
