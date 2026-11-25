# Sala de servidores, continuidad y eficiencia energética

## 1. PUE y DCiE

```text
PUE = Energía total del recinto / Energía de equipos TI
DCiE = Energía de equipos TI / Energía total del recinto
```

Si el recinto consume 50.000 kWh y los equipos TI consumen 40.000 kWh:

```text
PUE = 50.000 / 40.000 = 1,25
DCiE = 40.000 / 50.000 = 0,80 = 80 %
```

Un PUE más cercano a 1 es mejor. Un DCiE más alto es mejor.

## 2. Carga TI, UPS y generador

Si hay 6 racks de 4 kW:

```text
Carga TI = 6 × 4 = 24 kW
```

Si la UPS requiere un margen de diseño de 25 %:

```text
UPS = 24 × 1,25 = 30 kW
```

Si el PUE es 1,6:

```text
Potencia del sitio = 24 × 1,6 = 38,4 kW
```

Si el generador se dimensiona con 40 % adicional:

```text
Generador = 38,4 × 1,4 = 53,76 kW
```

No multipliques el margen de UPS sobre la potencia total del sitio: la UPS protege la carga TI.

## 3. Continuidad

- Activo-activo: ambos sitios procesan tráfico. Mayor disponibilidad, pero mayor complejidad y costo.
- Activo-pasivo: un sitio atiende y otro espera. Es más simple y barato, pero el cambio puede demorar.
- Respaldo: permite recuperar datos, pero no necesariamente cumple RTO corto.

Para RTO de 15 minutos y RPO 0, PagoAndes necesita una solución de continuidad más exigente que un respaldo diario.

## Ejercicios

1. Calcula PUE y DCiE con 80.000 kWh totales y 60.000 kWh TI.
2. Dimensiona UPS y generador para 10 racks de 5 kW, PUE 1,5 y margen de generador de 30 %.
3. Explica por qué un respaldo diario no cumple RPO = 0.
