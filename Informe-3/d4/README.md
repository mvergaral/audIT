# Informe 3 · Aporte de D4 (infraestructura, proveedores y adquisiciones)

Tareas de D4 del proyecto de Linear de la entrega 3, P-AUD-1 (AUD-32 a AUD-41). Versión del 2026-11-11.
Cada tarea tiene su archivo, con el mismo contenido que su adjunto en Linear.

## Tareas

| Código | Linear | Tarea | Archivo | Estado en Linear |
|---|---|---|---|---|
| 4.1 | AUD-32 | Presupuestar equipos, repuestos, instalación e infraestructura | `4.1-presupuesto-equipos.md` | In Progress, espera 4.4 |
| 4.2 | AUD-33 | Calcular nube, conectividad y alojamiento | `4.2-nube-conectividad.md` | In Progress, espera 3.6 de D3 |
| 4.3 | AUD-34 | Calcular mantenimiento, reposiciones y operación técnica | `4.3-mantencion-operacion.md` | In Progress |
| 4.4 | AUD-35 | Identificar y justificar proveedores clave | `4.4-proveedores-clave.md` | In Progress, espera 3.5 de D3 |
| 4.5 | AUD-36 | Consolidar matriz de adquisiciones | `4.5-matriz-adquisiciones.md` | In Progress, espera 3.4 de D3 |
| 4.6 | AUD-37 | Entregar calendario de compras y contrataciones a D2 | `4.6-calendario-compras.md` | In Progress |
| 4.7 | AUD-38 | Valorizar respuestas a riesgos y contingencias | `4.7-riesgos-contingencias.md` | In Progress |
| 4.8 | AUD-39 | Distinguir compras de audIT y del cliente | `4.8-compras-audit-y-mandante.md` | Done |
| 4.9 | AUD-40 | Valorizar innovación 3 | `4.9-innovacion-3.md` | In Progress |
| 4.10 | AUD-41 | Redactar explicación de costos y adquisiciones | `4.10-explicacion-costos-adquisiciones.md` | In Progress |

Archivos de apoyo:

| Archivo | Contenido |
|---|---|
| `art46-respuestas-D4.md` | Respuestas de D4 a la revisión del Informe 2, para el anexo del Art. 46 (`../AUDIT-Anexo-Art46-Informe3-Revision-Independiente.md`) |
| `_borrador-precios.md` | Cada precio de hardware con su fuente, URL y fecha de consulta (2026-11-07) |
| `cambios-de-productos.md` | Cambios de producto frente al T-11 del Informe 2 |
| `calculo/` | Scripts que producen todas las cifras, sus salidas `.out` y los precios de Azure consultados en la API pública (`calculo/azure_precios/`, 2026-11-11) |

## Resultado

| Concepto | Neto en pesos, 56 meses |
|---|---|
| Infraestructura on-premise y unidades de prueba (4.1) | 111.326.621 |
| Azure (4.2) | 750.165.482 |
| Conectividad (4.2) | 396.869.362 |
| Soporte y mantención (4.3) | 152.371.182 |
| Asesoría legal R-24 y reserva de contingencia (4.7) | 144.373.265 |
| **Total de D4 en el flujo de audIT** | **1.555.105.912** |
| Hardware que compra el mandante, hoja informativa fuera del flujo (4.1) | 225.384.199 |

Innovación 3 (4.9): inversión $5.700.000, costo $4.032.000 y beneficio $135.000.000 (cifra de D1).

## Bases del reparto

- El mandante compra el hardware de campo y de red, que va en una hoja informativa fuera del flujo.
  audIT paga la infraestructura on-premise, la instalación, la nube y la conectividad (aclaraciones del
  Informe 3, §9, en `../../texto/Aclaraciones_Informe_3.md`).
- Valores netos, al tipo de cambio del Formulario E-24: USD $900 y EUR $1.000.
- Lo que no tiene precio público está estimado y marcado «estimado».
- Las decisiones están en `../../Informe-2/D4/DECISIONES-D4.md`, D4-134 a D4-146.

## Cómo volver a calcular

Desde `calculo/`, con Python 3:

```
python3 presupuesto_41.py > presupuesto_41.out
python3 nube_42.py > nube_42.out
python3 mantencion_contingencia.py > mantencion_contingencia.out
python3 calendario_46.py > calendario_46.out
```

`azure_api.py` vuelve a consultar la API pública de precios de Azure y guarda la respuesta en
`azure_precios/`.
