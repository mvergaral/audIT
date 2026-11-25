# Gestión de riesgos

## 1. Qué es un riesgo

Un riesgo es un evento incierto que, si ocurre, afecta positiva o negativamente los objetivos del proyecto.

- Amenaza: efecto negativo.
- Oportunidad: efecto positivo.

No confundas:

- Causa: condición que origina el riesgo.
- Riesgo: evento incierto.
- Efecto: consecuencia.
- Problema: evento que ya ocurrió.

## 2. Exposición y VME

```text
Exposición = Probabilidad × Impacto
VME = Probabilidad × Impacto monetario
```

Ejemplo:

```text
Probabilidad = 40 %
Impacto = $3.000.000
VME = 0,40 × 3.000.000 = $1.200.000
```

La reserva de contingencia puede calcularse sumando los VME de los riesgos cuantificados.

## 3. Respuestas a amenazas

- Evitar: eliminar la causa o cambiar el plan.
- Transferir: pasar el impacto a un tercero mediante contrato o seguro.
- Mitigar: reducir probabilidad o impacto.
- Aceptar: no realizar una acción preventiva; se monitorea o se reserva dinero.
- Escalar: llevar la decisión a un nivel superior.

Para PagoAndes, ante el riesgo “la pasarela cambia su API”:

- Mitigar: construir un adaptador y hacer pruebas tempranas.
- Transferir parcialmente: exigir aviso contractual y soporte del proveedor.
- Aceptar: mantener una reserva para cambios menores.

Agregar más personas no siempre mitiga el riesgo. Si el problema es una interfaz desconocida, una prueba de concepto es más útil que aumentar el equipo.

## 4. Riesgos residuales y secundarios

- Residual: el riesgo que permanece después de responder.
- Secundario: un riesgo nuevo producido por la respuesta.

Ejemplo: contratar un proveedor reduce el riesgo técnico, pero crea dependencia y riesgo de indisponibilidad del proveedor.

## 5. Riesgos y calidad

La mala calidad de datos, criterios de aceptación ambiguos y pruebas tardías son riesgos del proyecto.

Respuestas útiles:

- perfilamiento temprano de datos;
- prueba de concepto;
- prueba de carga;
- prueba de intrusión;
- criterios de aceptación medibles;
- revisión de riesgos durante todo el proyecto.

## Ejercicios

1. Calcula el VME de tres riesgos de PagoAndes.
2. Elige una respuesta para cada riesgo y explica por qué.
3. Identifica un riesgo residual y uno secundario.
4. Explica por qué “aumentar el equipo” no siempre reduce un riesgo.
