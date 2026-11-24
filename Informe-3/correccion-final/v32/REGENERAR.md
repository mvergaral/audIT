# Regeneración de la planilla 3.2

Reemplaza los pasos de Codex (`@oai/artifact-tool`) por LibreOffice con UNO. Parte de la planilla 3.1 publicada y aplica los cambios en tres fases. Las fórmulas se escriben en sintaxis de Calc. Gráficos, validaciones y protección se conservan.

Requisitos: LibreOffice con `uno` disponible en el Python del sistema (`/usr/bin/python3`) y un Python con openpyxl para los scripts de lectura (`AUDIT_PYTHON`). `LO_PERFIL` fija el perfil temporal de LibreOffice.

```bash
cd Informe-3/correccion-final/v32
export AUDIT_PYTHON=/ruta/a/python-con-openpyxl LO_PERFIL=/tmp/lo-perfil-audit LO_PUERTO=2202
export LO_EJECUTABLE=/usr/bin/libreoffice  # ajustar a la instalación local; por defecto se usa soffice
T=../../../outputs/3.2/trabajo; E=../../../outputs/3.2/Entrega-3.2
mkdir -p "$T" "$E"
git show origin/main:outputs/3.1/Entrega-3.1/INFORME3_AUDIT_PLANILLA_20261115.xlsx > $T/base-3.1.xlsx
/usr/bin/python3 aplicar_costos.py $T/base-3.1.xlsx $T/paso-a.xlsx
/usr/bin/python3 aplicar_financiamiento.py $T/paso-a.xlsx $T/paso-b.xlsx
/usr/bin/python3 aplicar_registro.py $T/paso-b.xlsx $T/paso-c.xlsx
/usr/bin/python3 aplicar_controles.py $T/paso-c.xlsx $E/INFORME3_AUDIT_PLANILLA_3.2_20261115.xlsx
$AUDIT_PYTHON -I indicadores.py $E/INFORME3_AUDIT_PLANILLA_3.2_20261115.xlsx --meses
/usr/bin/python3 probar_32.py $E/INFORME3_AUDIT_PLANILLA_3.2_20261115.xlsx /tmp
/usr/bin/python3 probar_controles.py $E/INFORME3_AUDIT_PLANILLA_3.2_20261115.xlsx
```

| Script | Cambios |
|---|---|
| `aplicar_costos.py` | Madurez en base (B70), montaje sustituido (B59), salida del técnico en M10, campo externo por visita (filas 380-426 de Detalle proveedores D4), prepago anual de soporte, refuerzos de puesta en producción. Parámetros nuevos B78-B88. |
| `aplicar_financiamiento.py` | Precio por margen objetivo (B62 = 0), hoja Amortización calculada con `simular_amortizacion.py`, pago bancario por calendario (B84, B89), línea de los escenarios ante faltante previo a cobros, déficit residual contra cero. |
| `aplicar_registro.py` | Hoja Feedback 3.2 con resultados como fórmulas. |
| `aplicar_controles.py` | Entradas B78:B92 desbloqueadas y validadas. Prepagos programados desde B89:B91 con remanente derivado del principal. Salida mensual exacta del técnico por B83, leyendas de los cinco gráficos y controles de regresión. |

La comprobación en Microsoft Excel sigue pendiente. Recalcular el archivo y contrastar indicadores y controles con LibreOffice; una apertura sin errores no demuestra equivalencia de cálculo. Las TIR de escenarios sin convergencia se muestran como «Revisar raíces».

## Revisión de parámetros y alcance de entrega

B90 conserva el primer prepago propuesto de CLP 320 millones y B91 el mes 18 para liquidar el remanente. Son entradas de planificación explícitas: Excel recalcula el principal restante y los flujos al modificar B89:B91 o el capital. No ejecuta el optimizador de Python para elegir otro calendario. Revalidar caja y cota antes de cobros después de cualquier cambio. B83 admite M10–M21, la ventana de salida del técnico durante o al cierre de implementación; su FTE de referencia está en B92.

Las regresiones comprueban que el caso base conserva sus cifras, que B89 mueve el primer pago, que un capital distinto actualiza el principal programado y que retrasar la salida del técnico conserva su nómina hasta el mes elegido. Las fórmulas siguen protegidas sin contraseña y las nuevas entradas admiten edición y validación. Las leyendas de los cinco gráficos se vinculan a las cabeceras reales de sus series; no a la celda común RESUMEN!A1.

La carpeta `Entrega-3.2` contiene la planilla. Los PDF y la presentación de `Entrega-3.1` son versiones anteriores y no integran un paquete económico coherente con esta planilla: deben actualizarse antes de enviarlos juntos. La comprobación en Microsoft Excel sigue pendiente; requiere forzar el recálculo y contrastar controles e indicadores, además de abrir el archivo. Los supuestos de campo y guardias de B78:B92 requieren la validación de D2/D4.
