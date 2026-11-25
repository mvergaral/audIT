# Adquisiciones, contratos y costo total de propiedad

## 1. Adquirir es una decisión de arquitectura

Adquirir es obtener de un tercero un bien, servicio o resultado que el proyecto decide no producir. Cambia arquitectura, riesgo, flujo de caja, conocimiento y salida; no es un trámite posterior.

## 2. Nueve familias TIC

1. infraestructura física;
2. nube IaaS/PaaS;
3. software de base;
4. software de aplicación;
5. servicios profesionales;
6. soporte y mantención;
7. conectividad;
8. datos/contenidos;
9. personas, formación y certificación.

Cada familia usa métricas, garantías y riesgos distintos. Comprar hardware no se evalúa como contratar desarrollo.

## 3. Hacer, comprar o arrendar

| Hacer | Comprar | Arrendar/servicio |
|---|---|---|
| núcleo diferenciador | problema estándar resuelto | demanda variable o evitar CAPEX |
| conserva conocimiento/control | parametrización y fabricante | operación delegada |
| costo y plazo de construir | riesgo de brecha/licencia | dependencia y costo de salida |

Se decide mediante criterios ponderados y TCO a horizonte declarado, no por preferencia tecnológica.

### Formas de pagar

- perpetua: pago inicial + mantención;
- suscripción: pago periódico por acceso;
- consumo: pago por uso real.

La misma solución cambia CAPEX/OPEX y riesgo de continuidad. SaaS deja de estar disponible si se deja de pagar; una licencia perpetua puede seguir, pero queda obsoleta sin soporte.

## 4. Contrato y distribución del riesgo

El contrato define obligaciones, entregables, precio, pago, aceptación, cambio, propiedad, responsabilidad y cierre.

### Precio fijo

Precio acordado por alcance. El proveedor absorbe sobrecostos si el alcance estaba claro. Conviene con requisitos estables; exige exclusiones y control de cambios.

Variantes: fijo firme, reajustable, con incentivo.

### Costos reembolsables

Cliente paga costos permitidos más honorario. Adecuado a alcance incierto; el comprador asume más riesgo y necesita control/auditoría.

Variantes:

- **CPFF:** costo más honorario fijo; el honorario no crece con cada peso gastado.
- **CPIF:** costo más incentivo por cumplir metas.
- **CPAF:** costo más honorario por evaluación de desempeño.
- **CPPC:** costo más porcentaje del costo; es especialmente problemático porque el honorario aumenta cuando el proveedor gasta más y suele estar restringido.

### Tiempo y materiales

Tarifa por tiempo y unidades. Híbrido útil cuando no se conoce toda la cantidad; debe tener topes y reglas para no quedar abierto.

## 5. Incentivo FPIF y PTA

En precio fijo con incentivo se comparten desviaciones hasta un techo. Conceptos:

- costo objetivo;
- ganancia objetivo;
- precio objetivo;
- proporción de reparto comprador/vendedor;
- precio tope.

```text
PTA = costo objetivo + (precio tope − precio objetivo) / participación del comprador
```

Sobre el PTA, cada peso adicional de costo recae efectivamente en el vendedor porque el precio ya alcanzará el tope.

Ejemplo: costo objetivo 80, ganancia objetivo 10, precio objetivo 90, techo 110 y reparto comprador 70 %:

```text
PTA = 80 + (110−90)/0,70 = 108,57
```

## 6. Cláusulas que afectan margen

- alcance, supuestos y exclusiones;
- forma e hitos de pago;
- aceptación tácita o plazo para observar;
- multas y límite de responsabilidad;
- SLA y descuentos;
- garantía y soporte;
- propiedad intelectual y reutilización;
- confidencialidad/datos;
- reajuste y moneda;
- término anticipado y transición/salida.

La propiedad intelectual puede impedir reutilizar componentes y destruir margen futuro. Una multa máxima superior al margen obliga a rediseñar plazo/precio o no ofertar.

## 7. Procesos de adquisiciones PMBOK

1. **Planificar:** qué adquirir, cómo, cuándo, criterios, contrato y SOW.
2. **Efectuar:** solicitar, evaluar y seleccionar vendedor.
3. **Controlar:** desempeño, cambios, reclamaciones, pagos y cierre.

### SOW

El enunciado del trabajo describe alcance adquirido, entregables, estándares, lugar, plazo, aceptación y datos. Ambigüedad aquí se transforma en conflicto contractual.

### Documentos de mercado

| Documento | Propósito |
|---|---|
| RFI | conocer mercado/capacidades |
| RFP | solicitar propuesta de solución |
| RFQ | solicitar cotización comparable |
| IFB | invitar oferta formal con especificación cerrada |

No se piden en el mismo momento: RFI explora; RFQ compara algo suficientemente definido.

## 8. Evaluación ponderada

```text
puntaje total = Σ(peso criterio × nota normalizada)
```

Ejemplo:

| Criterio | Peso | A | B |
|---|---:|---:|---:|
| Técnico | 45 % | 90 | 80 |
| Precio | 30 % | 70 | 95 |
| Experiencia | 15 % | 85 | 75 |
| Plazo | 10 % | 80 | 90 |

```text
A = 0,45×90 + 0,30×70 + 0,15×85 + 0,10×80 = 82,25
B = 0,45×80 + 0,30×95 + 0,15×75 + 0,10×90 = 84,75
```

B gana aunque A tenga mejor nota técnica. Los pesos son una decisión estratégica, no matemática neutral.

### Marco chileno mencionado en clases

La presentación sitúa la contratación pública bajo la Ley 19.886, su modernización y el reglamento DS 661. Para el control importa reconocer que procedimiento, garantías, criterios y plazos provienen de las bases y del marco aplicable. En una compra real se debe consultar siempre la versión vigente, no apuntes antiguos.

## 9. TCO, CAPEX y OPEX

```text
TCO = adquisición + implantación + integración + operación
      + soporte + renovación + administración + salida − valor residual
```

**CAPEX:** inversión en activo. **OPEX:** gasto recurrente. Comparar solo precio inicial favorece falsamente la compra barata.

### Punto de equilibrio

Compra: costo inicial 30 + operación 6/año. SaaS: 14/año.

```text
30 + 6t = 14t
t = 3,75 años
```

Antes de 3,75 años SaaS cuesta menos; después, compra cuesta menos bajo estos supuestos. Falta valorar riesgo, obsolescencia y salida.

## 10. Dependencia y salida

Vendor lock-in aumenta cuando se usan formatos propietarios, servicios exclusivos, datos difíciles de extraer o conocimiento externo.

Mitigaciones: estándares, exportación, documentación, transferencia, propiedad de datos, asistencia de salida, límites de alza y prueba de migración.

Salir también cuesta: extracción, transformación, doble operación, nuevo proveedor, pruebas y término contractual.

## 11. Aplicación a SaludConecta

- hacer: núcleo clínico y reglas diferenciadoras;
- comprar: componente de firma/certificación si está estandarizado;
- arrendar: notificaciones y capacidad nube variable;
- contrato fijo para entregables bien definidos;
- T&M con tope para diagnóstico de sistema legado incierto;
- cláusula de aceptación en 10 días hábiles;
- SLA trazado a arquitectura y soporte;
- plan de salida para datos y nube.

## 12. Errores y autoevaluación

Errores: pedir tres cotizaciones sin decisión make/buy, elegir por precio inicial, omitir administración del proveedor, no costear salida, aceptar SLA que arquitectura no soporta y comprar por usuario sin revisar métrica real.

1. ¿Cuándo preferirías RFI en vez de RFQ?
2. ¿Quién asume más riesgo en precio fijo?
3. Calcula PTA para un FPIF inventado.
4. ¿Por qué SaaS no es solo una decisión financiera?
5. Construye un TCO a tres años para dos alternativas.
6. Explica cómo una cláusula de aceptación afecta cronograma y caja.
