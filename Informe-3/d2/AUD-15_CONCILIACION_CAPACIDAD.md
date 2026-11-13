# AUD-15 · Conciliación de demanda y dotación

**Corte de demanda:** publicación D3 `4070a7e`. **Estado:** conciliación aritmética y de imputación para D2, con asignación individual pendiente. T-15 expresa capacidad contractual nominal en horas-persona. Para cerrar la nivelación se requiere el saldo disponible de cada ejecutor después de sus otras asignaciones, en las fechas de cada tarea.

## M9 · Construcción, pruebas y terreno

La demanda D3 de **3.354,2 h** se reconstruye con **1.459,2 h** de A09, **1.703 h** de EDT 6–8, **144 h** de 12.1, **32 h** de 12.2 y **16 h** de preparación del agente en 4.1/A11. Esta lectura reemplaza las filas equivalentes del escenario anterior de AUD-14. Las **6.008 h** de A09 en el catálogo completo sustituyen la estimación de trabajo de **17.600 h** del elemento 5 para el alcance revisado. La diferencia de **11.592 h** requiere una decisión de nivelación y presupuesto antes de modificar la dotación o la nómina. [Matriz publicada](https://github.com/mvergaral/audIT/blob/4070a7e/Informe-3/d3/datos/dedicacion_mensual_d3.csv) · [Aporte D3](https://github.com/mvergaral/audIT/blob/4070a7e/Informe-3/d3/APORTE_COSTOS_SOFTWARE_DATOS.md).

| Perfil D3 | Demanda M9 (h) | FTE nominales a 160 h |
| --- | ---: | ---: |
| Arquitectura | 92,8 | 0,5800 |
| Liderazgo de Desarrollo | 139 | 0,8688 |
| Software | 1.090,6 | 6,8163 |
| Frontend/Móvil | 427 | 2,6688 |
| Seguridad | 170,2 | 1,0638 |
| Datos | 597,8 | 3,7363 |
| QA | 656,2 | 4,1013 |
| SRE | 180,6 | 1,1288 |
| **Total** | **3.354,2** | **20,9638** |

T-15 consigna **30 personas × 160 h = 4.800 h** en M9. La diferencia con la demanda parcial D3 es **1.445,8 h** para el resto del proyecto. S1 compromete un Oficial de Seguridad y un Líder de Operaciones al 100 % en implementación. Aun dedicando por entero a cada uno a las tareas del perfil respectivo, faltarían **10,2 h de Seguridad** y **20,6 h de SRE** para cubrir solo D3 con esos dos puestos. Las cifras son mínimos para ese supuesto de asignación y pueden cubrirse con otros ejecutores compatibles si se acredita su disponibilidad. Los **597,8 h de Datos** y **656,2 h de QA** también requieren combinar ejecución técnica y liderazgo con ejecutores identificados. El desglose por rol de T-15 está fechado en M13–M15. Para M9 corresponde obtener la nómina por persona o código, rol, actividad, fechas y jornada reservada. [T-15, curva y asignación por rol](https://github.com/mvergaral/audIT/blob/0712c7f/recursos/Formato-Oferta-audIT/subdocumentos/07-plan-trabajo/formularios/T-15.tex#L34) · [S1, dedicaciones](https://github.com/mvergaral/audIT/blob/0712c7f/recursos/Formato-Oferta-audIT/subdocumentos/01-empresa/contenido.tex#L185).

Como sensibilidad de carga, sumar a la matriz D3 los bloques restantes identificados en AUD-14 antes de ajustar coincidencias y confirmar fechas.

| Bloque de AUD-14 fuera del total publicado D3 | Horas M9 | Condición para adoptarlo |
| --- | ---: | --- |
| Montaje a bordo 4.2 | 260 | 52 altas de referencia, sujetas a agenda. |
| Pruebas transversales 10.1 | 200 | Confirmar ventana y casos propios frente a pruebas de A09/A10. |
| Cierre de A11 | 64 | Confirmar un ciclo. Cruzar 8 h de QA de CP-HW-03 con las 8 h de QA del agente ya en D3. |
| 12.4 | 96 | Verificar ejecución propia frente a 4.1, A09 y 10.1. |
| 12.5 | 50 | Prorrateo de 300 h en seis meses, sujeto a calendario D1. |
| Balizas | 15 | Escenario de 60 unidades × 0,25 h. |
| Jefe de Proyecto y PMO | 224 | 160 h de dedicación nominal y 64 h de reserva PMO. Cruzar cierre documental con G13. |
| Preparación de terminales | 20 | Verificar alcance propio frente a agenda de montajes. |
| **Subtotal de sensibilidad** | **929** | Antes de conciliar coincidencias. |

La suma bruta de este escenario es **4.283,2 h**. La diferencia de **516,8 h** frente a T-15 precede a las visitas de clasificación y demás cargas pendientes. Por perfil, con solo los bloques técnicos desglosados de 10.1, A11 y 12.4, las demandas brutas suben a **1.162,6 h de Software, 443 h de Frontend, 621,8 h de Datos, 808,2 h de QA y 212,6 h de SRE**. Asignar primero las tareas con fecha condicionada por A11 y G13, validar las coincidencias por caso, candidato, ambiente y evidencia, y registrar el déficit residual por perfil y semana. [AUD-14, reservas y escenarios M9](AUD-14_COSTO_PERSONAL_POR_PERFIL.md#consolidación-de-carga-de-m9).

## M21–M24 · Cierres y operación

T-14 mantiene los cierres de **6.5** y **7.2** hasta M24. La demanda de **1.669 h** se compone de **879 h** de 6.5 y **790 h** de 7.2 dentro de los presupuestos de **6.400 h de EDT 6** y **4.800 h de EDT 7**. D3 propone ejecutar los cierres con recursos de 13.2 y 13.4, que también reciben 14 h por paquete y mes de mantenimiento de innovaciones. H12 tiene su propia actividad en 11.3. Cada hora de cierre lleva su EDT de alcance y su paquete de ejecución para imputarse una vez. [T-14, ventanas y responsables](https://github.com/mvergaral/audIT/blob/0712c7f/recursos/Formato-Oferta-audIT/subdocumentos/07-plan-trabajo/formularios/T-14.tex#L51) · [Reglas de la matriz D3](https://github.com/mvergaral/audIT/blob/4070a7e/Informe-3/d3/datos/conciliacion_presupuesto.json).

| Mes | Cierres 6.5 + 7.2 | Innovaciones | Demanda total | 13.2 demanda / diferencia hasta 640 h | 13.4 demanda / diferencia hasta 640 h |
| --- | ---: | ---: | ---: | ---: | ---: |
| M21 | 420 | 28 | **448** | 62 / 578 | 386 / 254 |
| M22 | 417 | 28 | **445** | 62 / 578 | 383 / 257 |
| M23 | 416 | 28 | **444** | 62 / 578 | 382 / 258 |
| M24 | 416 | 28 | **444** | 62 / 578 | 382 / 258 |
| **Total** | **1.669** | **112** | **1.781** | **248 / 2.312** | **1.533 / 1.027** |

T-15 asigna **640 h mensuales** a cada paquete y **2.560 h mensuales** a toda la operación. Las diferencias anteriores deben cubrir la operación habitual y la guardia 24×7 antes de asignar horas a los cierres. En 13.2, la demanda es **28 h de Seguridad y 34 h de SRE** al mes. En 13.4 hay **146 h de Datos y 77 h de QA** al mes, además de Software, Arquitectura, Liderazgo y Frontend. S1 compromete **80 h nominales de Líder de Datos** y **40 h nominales de Líder de Calidad** en operación. Por eso, aun imputándoles todas esas horas, restan **66 h mensuales de Datos** y **37 h mensuales de QA** por asignar a ejecutores compatibles. Debe verificarse qué dedicación de ambos líderes puede reservarse luego de sus responsabilidades habituales. [T-15, continuidad operacional](https://github.com/mvergaral/audIT/blob/0712c7f/recursos/Formato-Oferta-audIT/subdocumentos/07-plan-trabajo/formularios/T-15.tex#L80) · [S1, dedicaciones](https://github.com/mvergaral/audIT/blob/0712c7f/recursos/Formato-Oferta-audIT/subdocumentos/01-empresa/contenido.tex#L185).

Para Datos, registrar **100 h/mes** de conciliación histórica en 7.2, **44 h/mes** de retiro del TMS anterior en 6.5 y **2 h/mes** de mantenimiento. Identificar ingeniería de Datos en 13.4 y reservar las horas junto con los responsables de 7.2 y 6.5. Si se confirma un puesto nominal de 160 h para ejecutar las tres tareas, quedan 14 h/mes para sus demás trabajos. Si se confirman únicamente 80 h/mes compatibles y disponibles, el déficit sería de **264 h en cuatro meses**, equivalentes a **CLP 8.448.000** a CLP 32.000/h. Con 0 h de cobertura el escenario de referencia sería **584 h y CLP 18.688.000**. La brecha de personal y su efecto presupuestario se calculan tras acreditar disponibilidad, imputación y costo marginal. [AUD-14, capacidad de Datos y ejecutores propuestos](AUD-14_COSTO_PERSONAL_POR_PERFIL.md#capacidad-de-datos-en-m21m24).

## CP-SEC-05 · Agente y campaña de G13

| Imputación | Ventana | Horas | Conciliación |
| --- | --- | ---: | --- |
| D3, agente 4.1/A11 | M6–M9 | 72 | La matriz contiene 16, 24, 16 y 16 h respectivamente. En M9 son 4 de Software, 8 de QA y 4 de SRE. Mantener separadas de A09. Cruzar el QA con CP-HW-03 por ejecución y evidencia. |
| D1, Seguridad 10.1 | M10, antes de G13 | 8 | Conducción y validación. Cruzar con las 16 h de Seguridad de REV-S7-02 y conservar una sola imputación si coinciden las tareas. |
| D4, banco 10.1 | M10, antes de G13 | 7 | 5 h de Técnico y 2 h de Operación/SRE en la campaña compartida. |
| Reserva condicional 10.1 | M10, antes de G13 | 16 | Las dos asignaciones de campaña totalizan 15 h. Queda 1 h de diferencia nominal. La composición previa de 8 QA, 4 Software y 4 Firmware se sustituye al aprobar el desglose definitivo. |

La reserva sigue condicionada a capacidad acreditada por perfil y a ejecutar el caso sobre el iWave G26I en PREPROD con el candidato y la instrumentación identificados. G13 se libera en el día hábil 182 (M10). A12 comienza en el día 192. En la variante conectada, registrar por separado revocación, cese de captura local dentro de cinco minutos, cese de transmisión y acceso, denegación al actor ajeno e integridad de la evidencia previa. En la variante sin enlace, observar la verificación del permiso antes de transmitir al reconectar y registrar por separado la evidencia local. El costo atribuible de las 8 h de Seguridad es **CLP 352.000** a CLP 44.000/h según el punto medio E-26 con la UF contractual de E-24. Su aplicación como incremento depende del cruce con la asignación base de 10.1. [D1, conducción y valoración](../d1/ECONOMICO_SUPUESTOS_Y_PARAMETROS_D1.md#conducción-y-validación-de-cp-sec-05-en-g13) · [AUD-14, cruce D4 y D3](AUD-14_COSTO_PERSONAL_POR_PERFIL.md#cp-sec-05--confirmación-de-d4-y-cruce-de-las-horas) · [T-15, secuencia A09/G13/A12](https://github.com/mvergaral/audIT/blob/0712c7f/recursos/Formato-Oferta-audIT/subdocumentos/07-plan-trabajo/formularios/T-15.tex#L202).

## Comprobación reproducible

Desde la raíz del repositorio, obtener los totales de la versión publicada. El CSV usa punto decimal.

```powershell
$demanda = git show 4070a7e:Informe-3/d3/datos/dedicacion_mensual_d3.csv | ConvertFrom-Csv
$demanda | Where-Object mes -eq 9 | Group-Object bloque | ForEach-Object {
    [pscustomobject]@{ Bloque = $_.Name; Horas = ($_.Group.horas_solicitadas | Measure-Object -Sum).Sum }
}
$demanda | Where-Object { [int]$_.mes -in (21..24) } | Group-Object mes,paquete_ejecucion | ForEach-Object {
    [pscustomobject]@{ MesPaquete = $_.Name; Horas = ($_.Group.horas_solicitadas | Measure-Object -Sum).Sum }
}
$demanda | Where-Object bloque -eq agente_cp_sec_05 | Group-Object mes | ForEach-Object {
    [pscustomobject]@{ Mes = $_.Name; Horas = ($_.Group.horas_solicitadas | Measure-Object -Sum).Sum }
}
```

Para cada perfil, mes y ventana crítica, sumar la demanda con coincidencias conciliadas. Sumar la capacidad de ejecutores acreditados y restar sus otras asignaciones, incluidas guardias. El déficit es el máximo entre cero y demanda menos capacidad disponible. Con un déficit acreditado, registrar ejecutor de refuerzo o reprogramación compatible con el hito y valorizar únicamente el efecto que corresponda en la nómina o contratación. Las horas agregadas de T-15 permiten controlar el total y los paquetes. La evidencia de cierre es el calendario de asignaciones aceptado por D2, con responsables y cobertura por perfil.
