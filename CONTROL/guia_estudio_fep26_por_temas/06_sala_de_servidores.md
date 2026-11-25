# Sala de servidores

## 1. Qué se diseña realmente

El curso no pide construir un datacenter de cientos de racks: pide justificar una sala de aproximadamente 1 a 12 gabinetes dentro de un edificio existente.

Debe garantizar continuamente:

1. energía acondicionada y respaldada;
2. clima controlado;
3. conectividad por caminos adecuados;
4. seguridad física;
5. monitoreo con responsables y procedimientos.

El orden práctico de diseño y presupuesto es energía → clima → conectividad → equipamiento.

## 2. TIER, disponibilidad y redundancia

TIER expresa características de infraestructura y mantenibilidad. No se “hereda” automáticamente: alojar un servidor en un proveedor TIER III no convierte en TIER III un servicio cuya sucursal tiene un enlace único.

| Nivel | Idea práctica |
|---|---|
| TIER I | camino único, sin redundancia |
| TIER II | componentes redundantes |
| TIER III | mantenimiento concurrente |
| TIER IV | tolerancia a fallas |

Un “nueve” adicional reduce mucho la caída permitida, pero aumenta costo. El nivel debe responder a impacto de negocio, no a prestigio.

### Notación de redundancia

| Configuración | Significado | Uso |
|---|---|---|
| N | capacidad exacta requerida | no crítico |
| N+1 | un componente adicional | sala típica |
| 2N | dos sistemas completos | misión crítica |
| 2(N+1) | dos sistemas con reserva | máxima exigencia |

La redundancia también debe ser de trayecto. Dos UPS que dependen del mismo tablero y ducto pueden fallar juntos.

## 3. PUE y DCiE

```text
PUE = energía total de la instalación / energía de equipos TI
DCiE = energía TI / energía total = 1 / PUE
```

Ejemplo: instalación consume 68.000 kWh y TI 40.000 kWh.

```text
PUE = 68.000 / 40.000 = 1,70
DCiE = 40.000 / 68.000 = 0,5882 = 58,82 %
```

PUE ideal se acerca a 1, pero 1 real no existe porque clima, UPS, luz y pérdidas consumen energía. Para que sea auditable se deben declarar puntos y período de medición.

Cómo mejorarlo: confinamiento de pasillos, tapas ciegas, sellado de pasos, temperatura adecuada, equipos eficientes y medición. PUE no mide disponibilidad ni calidad del software.

## 4. Principios para distribuir recintos

1. separar por función;
2. separar por acceso;
3. separar por riesgo: agua, combustible, hidrógeno y fuego lejos del cómputo;
4. minimizar visitas a la sala blanca.

Tres líneas de acceso pueden ir desde guardia/visitas, pasando por zona técnica, hasta sala blanca. Baños o tuberías no deben compartir muro o piso superior riesgoso.

### Trece recintos de referencia

| Recinto | Función |
|---|---|
| Sala de servidores | racks de cómputo, red y almacenamiento |
| NOC/monitoreo | alarmas, consola y bitácora |
| Climatización | equipos de precisión |
| Extinción | cilindros y tablero de agente limpio |
| Acceso/custodia | credenciales, visitas y CCTV |
| UPS y baterías | respaldo eléctrico |
| Generador | autonomía prolongada y combustible |
| Acometida de comunicaciones | llegada de operadores |
| Acometida eléctrica | empalme, tablero y transferencia |
| Taller | reparación fuera de sala blanca |
| Bodega | repuestos e insumos |
| Reuniones | coordinación/auditoría |
| Baños/servicios | fuera del perímetro técnico |

No siempre caben todos separados. Si se fusionan, se declara el riesgo aceptado; por ejemplo, taller y bodega aumentan circulación y partículas.

## 5. Distribución de racks

Se evalúa que la elección esté justificada, no que exista un plano universal.

- una fila: sala pequeña, simple, menor escalabilidad;
- filas enfrentadas: facilita pasillo frío/caliente;
- perímetro: acceso sencillo, peor control de aire;
- pods/confinamiento: eficiencia alta, mayor costo.

Holguras de referencia del material: alrededor de 1,2 m al frente y 0,9 m atrás, ajustadas a equipos, puertas y norma aplicable.

## 6. Seguridad, acceso y monitoreo

Capas:

1. guardia y credencial en edificio;
2. tarjeta por perfil en zona técnica;
3. tarjeta + biometría y esclusa en sala;
4. cerradura del rack.

- **Mantrap/esclusa:** segunda puerta no abre hasta cerrar la primera.
- **Antipassback:** una credencial no vuelve a entrar sin registrar salida.
- externos entran acompañados;
- accesos y tareas quedan en bitácora.

Sensores: humo temprano/VESDA, temperatura, humedad, agua, apertura, energía y gases relevantes. Una alarma necesita destinatario, canal, tiempo de respuesta y procedimiento. “Hay sensor” sin operación 24/7 no constituye control.

La extinción con agente limpio evita agua sobre electrónica, pero exige diseño certificado y seguridad humana: algunos agentes desplazan oxígeno o requieren evacuación.

## 7. Cadena eléctrica

```text
Red → tablero → ATS/TTA → UPS → PDU A/B → fuentes dobles → equipo
```

| Eslabón | Función | Protección típica |
|---|---|---|
| Empalme | suministro | generador/doble alimentador |
| Tablero | protección y reparto | selectividad/termografía |
| ATS | conmuta red-generador | prueba con carga |
| UPS | filtra y sostiene sin corte | N+1 y bypass |
| PDU | distribuye por rack | A/B por caminos distintos |
| Fuente | alimenta servidor | fuentes dobles |

### UPS, baterías y generador

- UPS on-line doble conversión es la opción apropiada para la sala.
- batería determina minutos de autonomía; tiene vida útil, ventilación y peso.
- generador toma carga después de segundos y debe alimentar también climatización.
- si ambos fallan, debe existir apagado ordenado.

Dimensionamiento simplificado:

```text
potencia de diseño = carga TI × (1 + holgura)
```

La capacidad real debe considerar factor de potencia, eficiencia, arranque y clima.

## 8. Climatización

La potencia eléctrica consumida por TI termina casi completamente como calor. Una carga TI de 26 kW exige retirar aproximadamente esa carga térmica, más pérdidas y holgura.

Buenas prácticas:

- pasillo frío frente a tomas y caliente en descargas;
- confinamiento para evitar mezcla;
- tapas ciegas en U libres;
- cableado que no bloquee aire;
- clima de precisión N+1 si la criticidad lo exige;
- monitoreo en toma de aire, no solo en muro.

Rango de referencia de la presentación: 18–27 °C y 40–60 % HR, sujeto al diseño y recomendaciones vigentes. Enfriar demasiado aumenta costo y puede causar condensación.

## 9. Rack y unidades U

Una U mide 44,45 mm. Gabinetes comunes son 42U/45U. Se deja alrededor de 20 % libre para crecimiento, flujo y maniobra.

Distribución típica:

```text
arriba: patch panels
zona alta: switches/firewall
centro: servidores
abajo: almacenamiento pesado
costados: PDU A y B
vacíos: tapas ciegas
```

El gabinete debe tener profundidad suficiente, anclaje, puertas practicables, rieles, organizadores y potencia declarada. Blade/HCI concentran densidad: ahorran U, pero exigen más kW y clima.

### Cuántos racks

```text
U requeridas = Σ U de equipos + organizadores + paneles
U de diseño = U requeridas / ocupación objetivo
racks = techo(U de diseño / U útiles por rack)
```

Además se limita por kW/rack y peso; disponer de U libres no significa disponer de energía/clima.

## 10. Cableado

- datos y energía en bandejas separadas; cruces a 90°;
- identificación en ambos extremos;
- radio de curvatura de fibra;
- certificación con informe;
- planilla/DCIM actualizada.

Topología TIA-942: ENI (entrada), MDA (principal), HDA/ZDA (horizontal/zona) y EDA (equipo). ToR instala switch por rack; EoR al final de fila. ToR acorta cables y aumenta equipos; EoR centraliza y alarga tendidos.

## 11. Equipamiento

- torre: pequeñas oficinas, no opción normal de sala;
- rack 1U/2U/4U: estándar;
- blade: densidad y chasis compartido;
- HCI: cómputo, almacenamiento y virtualización integrados.

Dimensionar CPU, RAM, disco/IOPS, red, fuentes dobles y licenciamiento. Tres nodos es mínimo frecuente para clúster con quórum y mantenimiento, pero debe comprobarse capacidad N+1.

DAS/NAS/SAN se eligen por patrón; HDD para capacidad/respaldo, SSD para uso general y NVMe para IOPS altos.

## 12. Ficha técnica de SaludConecta

| Parámetro | Propuesta de estudio |
|---|---|
| Sala | 32 m² útiles + recintos de apoyo |
| Racks | 6×42U, máximo 70 % inicial |
| Potencia | 3 kW promedio; carga TI 22 kW con holgura |
| UPS | doble conversión N+1, bypass, 10 min |
| Generador | 12 h, incluye clima |
| Clima | capacidad N+1 y pasillos confinados |
| PUE de diseño | 1,7, medido tablero general/PDU |
| Disponibilidad | objetivo de servicio 99,5 % |
| Enlaces | dos operadores y trayectos diferentes |
| Continuidad | RTO 4 h, RPO 1 h |

No se debe afirmar “TIER III” sin demostrar todos los requisitos y alcance de certificación.

## 13. Errores y autoevaluación

Errores: comprar servidores antes de diseñar energía/clima, redundancia sin caminos independientes, PUE sin puntos de medición, sensores sin respuesta, racks saturados, confundir UPS con generador y omitir operación/licencias.

1. Calcula PUE y DCiE con 90 MWh totales y 54 MWh TI.
2. ¿Por qué dos UPS pueden no constituir 2N?
3. ¿Qué fusionarías si solo hay 45 m² y qué riesgo aceptas?
4. Explica la secuencia de un corte eléctrico.
5. ¿Por qué blade puede empeorar la climatización?
6. ¿Qué parámetros debe declarar una ficha verificable?

