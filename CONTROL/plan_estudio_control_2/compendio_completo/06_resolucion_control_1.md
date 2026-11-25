# Resolución completa del Control 1 del CamScanner

Este documento usa el control escaneado como checklist. Las letras corresponden a las alternativas visibles en el PDF.

## 1. ISO/IEC 25010:2023

**Respuesta: d.**

La versión 2023 organiza nueve características. Entre los cambios importantes aparecen:

- capacidad de interacción en lugar de la antigua usabilidad;
- flexibilidad en lugar de portabilidad como característica amplia;
- seguridad operacional como característica nueva.

No es correcto decir que conserva simplemente las ocho características de 2011 ni que es un modelo de proceso equivalente a CMMI o ISO 9001.

## 2. RTO y RPO

**Respuesta: a.**

RTO de 15 minutos significa que el servicio debe recuperarse en máximo 15 minutos. RPO igual a cero significa que no se puede perder información confirmada.

Para RPO 0 se necesita replicación sincrónica. Como además el RTO es corto, una arquitectura activo-activo o un sitio caliente es más coherente que un respaldo diario o un sitio frío.

## 3. Requisito no verificable

**Respuesta: c.**

“Manejar adecuadamente” es ambiguo y “errores de comunicación” no tiene umbral, tiempo ni resultado observable. Un requisito debe poder probarse.

Una redacción mejor sería:

> Si el servicio externo no responde en 10 segundos, el sistema registra el evento, reintenta tres veces y muestra un estado pendiente.

## 4. EDT y paquetes de trabajo

**Respuesta: c.**

El primer nivel por fases puede ser válido. Las precedencias pertenecen al cronograma y pueden modelarse después. El problema es el paquete de 200 horas, que supera la regla práctica 8/80 y es demasiado grande para controlarlo como unidad.

La EDT debe cumplir la regla del 100 %: sus hijos representan todo el trabajo del padre.

## 5. Acelerar el plazo sin recursos

**Respuesta: e.**

Las dependencias discrecionales son elegidas por el equipo y pueden revisarse. Las obligatorias dependen de la lógica del trabajo; las externas dependen de terceros.

Por eso no se puede negociar una dependencia interna simplemente con un comité, ni cambiar una dependencia obligatoria sin cambiar la solución. Lo correcto es revisar las dependencias discrecionales.

## 6. Interpretación de EF = 1,05

**Respuesta: b.**

El factor ambiental se calcula como:

```text
EF = 1,4 − 0,03×Σ
```

EF = 1 representa un ambiente neutro. EF = 1,05 es desfavorable: aumenta el esfuerzo estimado en comparación con un ambiente neutro.

EF menor que 1 sería favorable.

## 7. Costo calculado con horas nominales

**Respuesta: d.**

Las horas nominales incluyen horas contractuales, pero no todas son productivas. Existen feriados, reuniones, permisos, coordinación, capacitación y tiempos de espera.

Si se divide el costo mensual por todas las horas nominales, se subestima el costo real de cada hora productiva aproximadamente en el porcentaje de horas no productivas.

No se está sobreestimando el costo: se está usando un denominador demasiado grande.

## 8. Transacción crítica de una licitación

**Respuesta: c.**

La ventana de consultas es crítica porque es el último momento formal para aclarar ambigüedades de las bases antes de comprometer precio, alcance y plazo.

Una consulta puede revelar que:

- la disponibilidad exigida era mayor;
- la migración tenía más datos;
- existían sistemas externos no mencionados;
- el criterio de aceptación era subjetivo.

Descubrirlo después de ofertar convierte una incertidumbre en un costo asumido por el proveedor.

## 9. Deducible y atraso de la aseguradora

**Respuesta: b.**

El deducible queda como parte del impacto que la empresa debe asumir: es riesgo residual.

La posibilidad de que la aseguradora se demore introduce un riesgo nuevo derivado de la respuesta de transferir el riesgo: es riesgo secundario.

No son reserva de contingencia y reserva de gestión, porque la pregunta habla de efectos de contratar el seguro.

## 10. PUE y DCiE

**Respuesta: e.**

```text
PUE = energía total / energía TI
PUE = 50.000 / 40.000 = 1,25
```

```text
DCiE = energía TI / energía total
DCiE = 40.000 / 50.000 = 0,80 = 80 %
```

Por tanto, la afirmación que indica PUE 1,25 y DCiE 80 % es correcta. PUE 1,0 es un límite ideal: no es razonable alcanzarlo en una instalación real porque siempre existen pérdidas y consumo de refrigeración.

## 11. Densidad térmica del rack

**Respuesta: a.**

Una carga de 26 kW por rack es muy alta para refrigeración convencional por aire. El confinamiento de pasillo frío mejora la circulación, pero no crea capacidad térmica adicional.

La observación correcta es que la densidad declarada excede el límite práctico aproximado de ese esquema y exige una solución de refrigeración acorde.

## 12. Disponibilidad de componentes en serie

**Respuesta: c.**

En una cadena en serie, todos los componentes deben funcionar:

```text
Disponibilidad = 0,9995 × 0,9990 × 0,9995
Disponibilidad ≈ 0,9980 = 99,80 %
```

Caída mensual aproximada en 30 días:

```text
30×24×60 = 43.200 minutos
43.200×(1−0,9980) ≈ 86,35 minutos
```

El mínimo exigido de 99,9 % permite aproximadamente 43,20 minutos, por lo que 99,80 % no cumple.

No se promedian las disponibilidades: en serie se multiplican.

## 13. Valor monetario esperado

**Respuesta: a.**

```text
VME = Σ(probabilidad × impacto)
```

Con los seis riesgos:

```text
0,50×8.000.000 = 4.000.000
0,40×5.000.000 = 2.000.000
0,30×6.000.000 = 1.800.000
0,25×4.000.000 = 1.000.000
0,20×7.000.000 = 1.400.000
0,60×3.000.000 = 1.800.000
```

```text
VME total = 12.000.000
Porcentaje = 12.000.000 / 240.000.000 = 0,05 = 5 %
```

## 14. Duración y holgura de E

**Respuesta: d.**

Rutas principales:

```text
A-C-F-H = 4+5+4+5 = 18 días
A-D-G-H = 4+6+3+5 = 18 días
B-D-G-H = 3+6+3+5 = 17 días
B-E-G-H = 3+2+3+5 = 13 días
```

La duración total es 18 días. Las dos primeras son críticas.

Para E:

- termina temprano en el día 5;
- puede terminar hasta el día 10 sin retrasar G;
- por tanto, su holgura es 5 días.

## 15. Relaciones con retraso y extensión

**Respuesta: c.**

La actividad B se extiende de 8 a 10 semanas. Al ser predecesora de C y D, el cambio se propaga:

- C depende del inicio de B con un retraso de 2 semanas;
- D espera el fin de B;
- E espera el fin de D y el fin de C, con su retraso de una semana;
- F debe terminar junto con E.

El camino que controla la fecha final termina en la semana 23. La holgura existente no alcanza para absorber toda la extensión de B.

La clave es respetar el tipo de relación: no todas las dependencias son Fin-Inicio.

## 16. Carga TI, UPS, sitio y generador

**Respuesta: b.**

Hay 6 racks de 4 kW:

```text
Carga TI = 6×4 = 24 kW
```

UPS con 25 % de margen:

```text
UPS = 24×1,25 = 30 kW
```

PUE de 1,6:

```text
Potencia del sitio = 24×1,6 = 38,40 kW
```

Generador con 40 % adicional:

```text
Generador = 38,40×1,40 = 53,76 kW
```

## 17. Esfuerzo total de SmartGrid Andes

**Respuesta: d. 9.450 horas-hombre.**

### Actores

```text
UAW = 5×1 + 3×2 + 9×3 = 38
```

### Casos de uso

La clasificación de los casos del enunciado da:

- 3 simples;
- 6 medios;
- 4 complejos.

```text
UUCW = 3×5 + 6×10 + 4×15 = 135
UUCP = 38 + 135 = 173
```

Factores:

```text
TCF = 1,15
EF = 0,95
UCP = 173×1,15×0,95 ≈ 189
```

Esfuerzo de programación:

```text
E = 189×20 = 3.780 HH
```

Como programación es el 40 %:

```text
Esfuerzo total = 3.780/0,40 = 9.450 HH
```

La trampa es elegir 3.780, que es solo programación, no el total.

## 18. Plazo y presupuesto de SmartGrid Andes

**Respuesta: a.**

Capacidad del equipo:

```text
6×160×10 = 9.600 HH
```

Duración necesaria:

```text
9.450/(6×160) = 9,84375 meses
```

Cabe dentro de los 10 meses.

Costo:

```text
9.450×55 = USD 519.750
```

Presupuesto máximo:

```text
519.750−480.000 = USD 39.750 sobre el presupuesto
```

La situación correcta es: cumple el plazo, pero excede el presupuesto.
