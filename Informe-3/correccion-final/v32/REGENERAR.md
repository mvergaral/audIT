# Regeneración de la planilla 3.2

Reemplaza los pasos de Codex (`@oai/artifact-tool`) por LibreOffice con UNO. Parte de la planilla 3.1 publicada y aplica los cambios en tres fases. Las fórmulas se escriben en sintaxis de Calc. Gráficos, validaciones y protección se conservan.

Requisitos: LibreOffice con `uno` disponible en el Python del sistema (`/usr/bin/python3`) y un Python con openpyxl para los scripts de lectura (`AUDIT_PYTHON`). `LO_PERFIL` fija el perfil temporal de LibreOffice.

```bash
cd Informe-3/correccion-final/v32
export AUDIT_PYTHON=/ruta/a/python-con-openpyxl LO_PERFIL=/tmp/lo-perfil-audit
T=../../../outputs/3.2/trabajo; E=../../../outputs/3.2/Entrega-3.2
git show origin/main:outputs/3.1/Entrega-3.1/INFORME3_AUDIT_PLANILLA_20261115.xlsx > $T/base-3.1.xlsx
/usr/bin/python3 aplicar_costos.py $T/base-3.1.xlsx $T/paso-a.xlsx
/usr/bin/python3 aplicar_financiamiento.py $T/paso-a.xlsx $T/paso-b.xlsx
/usr/bin/python3 aplicar_registro.py $T/paso-b.xlsx $E/INFORME3_AUDIT_PLANILLA_3.2_20261115.xlsx
$AUDIT_PYTHON -I indicadores.py $E/INFORME3_AUDIT_PLANILLA_3.2_20261115.xlsx --meses
/usr/bin/python3 probar_32.py $E/INFORME3_AUDIT_PLANILLA_3.2_20261115.xlsx /tmp
```

| Script | Cambios |
|---|---|
| `aplicar_costos.py` | Madurez en base (B70), montaje sustituido (B59), salida del técnico en M10, campo externo por visita (filas 380-426 de Detalle proveedores D4), prepago anual de soporte, refuerzos de puesta en producción. Parámetros nuevos B78-B88. |
| `aplicar_financiamiento.py` | Precio por margen objetivo (B62 = 0), hoja Amortización calculada con `simular_amortizacion.py`, pago bancario por calendario (B84, B89), línea de los escenarios ante faltante previo a cobros, déficit residual contra cero. |
| `aplicar_registro.py` | Hoja Feedback 3.2 con resultados como fórmulas. |

Abrir el archivo final una vez en Excel para confirmar el recálculo: LibreOffice reproduce la 3.1 salvo cuatro TIR de escenarios sin convergencia, que quedan como «Revisar raíces».
