# Costos, tarifas y precio ofertado

## 1. La cadena completa

```text
paquete EDT → horas por perfil → costo directo → gastos generales
→ contingencia/insumos → costo total → margen → precio de venta
→ impuestos → monto ofertado
```

Cada cifra debe rastrearse hasta alcance. Un monto global sin desagregación no puede defenderse ni controlarse.

## 2. Ascendente y descendente

| Bottom-up | Top-down |
|---|---|
| estima cada paquete y suma | parte de un total y reparte |
| requiere EDT madura | requiere referencia/presupuesto |
| trazable y costosa | rápida y menos defendible |
| oferta definitiva | filtro preliminar |

Top-down sirve para decidir si vale la pena ofertar. Bottom-up sirve para fijar el compromiso. Compararlas ayuda a detectar inconsistencias.

## 3. Cono de incertidumbre

Una idea temprana puede desviarse mucho más que una estimación basada en requisitos y diseño. La clase usa como referencia rangos que se estrechan aproximadamente desde 0,25×–4× en idea, 0,5×–2× con requisitos, 0,67×–1,5× con diseño y 0,8×–1,25× durante construcción.

No es una ley para inflar precio; explica por qué una licitación fija compromisos cuando todavía existe incertidumbre y por qué hacen falta supuestos, exclusiones y contingencia.

## 4. Horas nominales versus productivas

Ejemplo de la clase:

```text
costo empresa mensual = $2.000.000
horas nominales = 180
productividad = 80 %
horas productivas = 180 × 0,80 = 144 h
costo directo/h = 2.000.000 / 144 = $13.888,89
```

Usar 180 h daría $11.111,11/h y subestimaría 20 %. Feriados, vacaciones, licencias, capacitación, preventa y tareas internas existen aunque no se facturen al proyecto.

Con 20 % de gastos generales y 15 % de margen sobre costo total:

```text
gastos generales = 13.888,89 × 0,20 = 2.777,78
costo total/h = 16.666,67
margen = 16.666,67 × 0,15 = 2.500
tarifa de venta/h = $19.166,67 ≈ $19.180 según redondeo de clase
```

El porcentaje de margen debe indicar su base. “15 %” sobre costo no equivale a margen del 15 % sobre venta.

## 5. Costos que no son horas

- licencias y suscripciones;
- nube, almacenamiento, respaldo y tráfico;
- servidores, red, UPS, clima y racks;
- certificaciones y pruebas externas;
- viajes/viáticos;
- capacitación y documentación;
- garantías y seguros;
- operación y soporte;
- reajuste, moneda e inflación.

La boleta de garantía inmoviliza capacidad financiera. Un servicio en dólares crea riesgo cambiario si el precio al cliente queda fijo en pesos.

## 6. Reservas y margen

| Concepto | Cubre | Ubicación | Autoridad |
|---|---|---|---|
| Contingencia | riesgos identificados | línea base de costos | jefe de proyecto según reglas |
| Reserva de gestión | trabajo desconocido dentro del marco | fuera de línea base, dentro presupuesto | dirección/patrocinador |
| Margen | utilidad esperada | precio de venta | no es fondo de proyecto |

```text
presupuesto = línea base de costos + reserva de gestión
precio = costo total vendido + margen
monto ofertado = precio + impuestos aplicables
```

Usar margen para pagar un riesgo no “usa una reserva”: convierte utilidad en pérdida.

## 7. Contingencia por riesgos

Puede apoyarse en EMV:

```text
EMV = probabilidad × impacto
```

Ejemplo: 40 % de una pérdida de $10 millones aporta $4 millones de exposición. Sumar EMV orienta la reserva, pero debe considerar correlación, respuesta y confianza.

## 8. Costo versus venta

- costo: lo que la empresa gasta;
- tarifa: precio de una unidad vendida;
- precio: lo cobrado antes de impuestos;
- monto ofertado: cifra final del formulario;
- valor: beneficio percibido por el cliente.

Una estimación UCP entrega esfuerzo; no entrega automáticamente plazo ni precio. Plazo viene del cronograma; precio, de tarifa, insumos, riesgo y estrategia comercial.

## 9. Ejemplo SaludConecta

Supón 7.200 HH distribuidas:

| Perfil/insumo | Cantidad | Tarifa/costo | Subtotal |
|---|---:|---:|---:|
| Horas profesionales | 7.200 h | $19.180 | $138.096.000 |
| Nube y licencias | — | — | $14.000.000 |
| Hardware/instalación | — | — | $18.000.000 |
| Contingencia | — | — | $9.000.000 |
| **Costo/precio base** | | | **$179.096.000** |

Ya supera el presupuesto de $180 millones antes de algunos impuestos y operación prolongada. La respuesta profesional es revisar alcance, arquitectura, tarifa, adquisiciones y riesgo, no borrar horas.

## 10. Errores frecuentes

1. Dividir sueldo por horas nominales.
2. Omitir gestión, QA, ambientes y garantía.
3. Confundir contingencia con margen.
4. Cotizar nube por un mes y vender 24 meses.
5. Omitir moneda/reajuste.
6. Pasar de requisitos a precio sin tamaño/esfuerzo.
7. reducir estimación para coincidir con presupuesto.

## 11. Autoevaluación

1. Calcula tarifa con $2,4 millones/mes, 180 h, 75 % productivo, 18 % GG y 12 % margen sobre costo.
2. ¿Por qué top-down sirve para no ofertar, pero no para defender una oferta final?
3. Clasifica contingencia, reserva de gestión y margen.
4. Enumera cinco costos no laborales de SaludConecta.
5. Explica por qué precio y costo no son sinónimos.

