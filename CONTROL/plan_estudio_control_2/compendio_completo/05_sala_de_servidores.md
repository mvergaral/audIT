# Módulo 5 - Sala de servidores, redes y continuidad

## 1. Qué se dimensiona

La sala debe sostener equipos TI, refrigeración, energía, redes, almacenamiento y continuidad. No basta con sumar servidores.

## 2. Carga TI, PUE y DCiE

```text
PUE = Energía total del recinto / Energía TI
DCiE = Energía TI / Energía total del recinto
```

Si el recinto consume 50.000 kWh y TI consume 40.000:

```text
PUE = 1,25
DCiE = 80 %
```

PUE cercano a 1 es más eficiente. DCiE alto es mejor.

## 3. Racks y potencia

Para 6 racks de 4 kW:

```text
Carga TI = 6×4 = 24 kW
```

Si la UPS usa 25 % de margen:

```text
UPS = 24×1,25 = 30 kW
```

Con PUE 1,6:

```text
Potencia del sitio = 24×1,6 = 38,4 kW
```

Con generador dimensionado con 40 % adicional:

```text
Generador = 38,4×1,4 = 53,76 kW
```

El margen de UPS se aplica a TI. El PUE convierte TI en consumo total.

## 4. Refrigeración y densidad

La potencia eléctrica de los equipos TI termina casi completamente como calor. Si una propuesta declara 26 kW por rack y pretende refrigerar solo con aire, hay que cuestionar si la densidad supera el límite práctico del sistema.

El confinamiento de pasillo frío mejora el flujo de aire, pero no elimina el límite térmico de los equipos ni la necesidad de capacidad de refrigeración.

## 5. UPS y generador

- UPS: mantiene energía durante interrupciones breves y permite apagado o transferencia.
- Generador: sostiene operación durante cortes prolongados.
- PDU: distribuye energía a los equipos.

La UPS no reemplaza al generador y el generador no corrige problemas de calidad eléctrica por sí solo.

## 6. Redes y modelo OSI

El modelo OSI ayuda a localizar fallas:

1. Física: cables y señales.
2. Enlace: tramas y MAC.
3. Red: IP y enrutamiento.
4. Transporte: TCP/UDP y puertos.
5. Sesión.
6. Presentación: formato y cifrado.
7. Aplicación: HTTP, DNS, SMTP, etc.

Una falla de cable no se resuelve cambiando una API. Una falla de puerto no se diagnostica igual que una falla de aplicación.

## 7. Almacenamiento y RAID

- RAID 0: rendimiento, sin redundancia.
- RAID 1: espejo, tolera la pérdida de un disco del par.
- RAID 5: paridad distribuida, tolera un disco, penaliza escrituras.
- RAID 6: doble paridad, tolera dos discos.
- RAID 10: espejo más distribución, buen rendimiento y redundancia, mayor costo de capacidad.

RAID no es respaldo: protege contra fallas de discos, no contra borrado, corrupción o ransomware.

## 8. Continuidad

- Activo-activo: ambos sitios atienden.
- Activo-pasivo: uno espera.
- Respaldo: permite restaurar, pero tiene un RPO según frecuencia.

RPO 0 exige que una escritura confirmada esté protegida sin esperar a un respaldo diario. RTO corto exige practicar la recuperación, no solo comprar equipos.

## Preguntas de control relacionadas

2. RTO/RPO.
10. PUE/DCiE.
11. Densidad térmica.
12. Disponibilidad compuesta.
16. UPS, PUE y generador.
