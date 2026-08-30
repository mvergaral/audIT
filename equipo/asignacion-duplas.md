# Asignación de duplas — Trabajo de investigación ICI-5444

Caso 10 · Transporte de Carga · TFEP-01/2026
Registrado el 30 de agosto de 2026.

Los porcentajes son la ponderación del **Informe 1** según la tabla de
`FEP01 · p.67 · Ponderación de la evaluación técnica`
(`./tools/buscar.py -v 172`).

## D1 — Empresa y problema · 19 % · Carlos + Naomi

Subdocumentos 1 (4 %) y 2 (11 %), más el ítem Transversal (4 %).

**Carlos** es literalmente la descripción del subdocumento 2: comprender el problema,
identificar afectados y sostenerlo con números. El Capítulo 7 del caso son cuatro
tablas de indicadores y el Capítulo 8 son diez entrevistas contradictorias; ese
trabajo es suyo.

**Naomi** toma el Formulario T-6, el mapa de actores y —esto es lo importante— la
custodia del 4 % transversal: índice, foliación, formato, APA, nomenclatura del
archivo. Dijo formato, y ese ítem se pierde entero por descuido, no por incapacidad.

## D2 — Esquema de solución y alcance · 21 % · Ignacio C + Matías

Subdocumento 3 (21 %).

El subdocumento 3 es catálogo de requerimientos funcionales y no funcionales trazable
al origen: es toma de requerimientos pura, que es lo de **Ignacio C**. Además el plan
de adhesión de los 148 transportistas es un problema de "qué le ofrezco a alguien para
que me dé un dato", que se piensa mejor desde UX que desde arquitectura.

**Matías** como comodín absorbe el volumen: son 26 decisiones pendientes que hay que
declarar como supuestos.

## D3 — Arquitectura lógica y datos · 27 % · Marcel + Martín

Subdocumentos 4.1 (16 %) y 5 (11 %). Es la dupla con más peso, pero también la que
menos páginas de especificación escribe.

Reparto interno explícito para que **Martín no toque una base de datos**:

- **Marcel**: modelo de dominio, motor y paradigma de persistencia, transaccionalidad,
  migración de las ≈6.000 vigencias, política de retención (RT-05.10).
- **Martín**: capas y módulos de la arquitectura lógica, capa de integración y de
  servicios de negocio, y toda la capa analítica —RT-05.25 a RT-05.30, separación
  transaccional/analítico, tableros con drill-down hasta la transacción de origen—.
  Eso es BI, y el caso lo necesita para el costo por kilómetro por ruta, que hoy no
  existe.

## D4 — Arquitectura física e infraestructura · 16 % · Ignacio V + Alonso

Subdocumento 4.2 (16 %). Es el ítem con más volumen de especificación del informe,
por eso lleva dos personas técnicas aunque valga 16 %.

- **Ignacio V**: dispositivo a bordo (374 unidades, condiciones de cabina, ciclo de
  vida), data center primario y secundario, y la arquitectura de seguridad física.
  La sala de San Bernardo de 26 m² no cumple el Capítulo 6 transversal; ese hallazgo
  es suyo.
- **Alonso**: tabla de emplazamiento nube/on-premise componente por componente,
  enlaces redundantes en los cuatro terminales regionales, ancho de banda por sitio
  y el costo mensual de datos móviles de la flota.

## Innovaciones (subdocumentos 13-14, 17 %)

Reasignadas según quién quedó dónde.

| Tipo | Dupla | Por qué |
| --- | --- | --- |
| 1 · Producto o servicio | D2 | Portal del transportista — Ignacio C |
| 5 · UX / sostenibilidad | D2 | Interfaz operable con guantes y sin interacción en marcha — Ignacio C |
| 4 · Modelo de negocio | D1 | Quién paga el dispositivo, incentivos por adhesión — Carlos con los números |
| 3 · Tecnológica / arquitectura | D3 | Operación desconectada 72 h, unificación de las tres plataformas GPS |
| 2 · Proceso | D4 | Despliegue camión por camión, actualización remota del parque |

## Comprobación de cobertura

19 + 21 + 27 + 16 = **83 %**, y el 17 % restante es justamente Innovaciones, que se
reparte en la tabla de arriba. La asignación cubre el 100 % del Informe 1 sin
solapamientos.

## Advertencia sobre los informes 2 y 3

Estos pesos son los del **Informe 1**. En la misma tabla las ponderaciones cambian
bastante después, así que la carga entre duplas no se mantiene:

| Subdoc. | Informe 1 | Informe 2 | Final |
| --- | --- | --- | --- |
| 3 · Esquema de solución (D2) | 21 % | 12 % | 10 % |
| 4.1 · Arquitectura lógica (D3) | 16 % | 7 % | 5 % |
| 4.2 · Arquitectura física (D4) | 16 % | 1 % | 10 % |
| 5 · Modelo de datos (D3) | 11 % | 6 % | 5 % |
| 2 · Comprensión del problema (D1) | 11 % | 6 % | 4 % |

En el Informe 2 aparecen ítems que hoy no tienen dueño: metodologías (8 %), plan de
trabajo y EDT (15 %), plan de riesgos (10 %) y plan de calidad (8 %) — 41 % del
Informe 2 sin asignar.
