# Cierre de corrección económica del Informe 3

La entrega está en `outputs/informe3-corregido/entrega/`. El ZIP se construye con una lista explícita de documentos para excluir borradores, bitácoras y respaldos de trabajo. Los archivos de esta corrección son locales, sin commit ni publicación remota.

Origen: repositorio local `47f7e7b1717e531fcbed6a171b6ed2023a1552e6`, libro económico de referencia `c9a6515` y tabla técnica del corte `c948a69`. Se preservaron los originales. El paquete nuevo se genera en un directorio aislado y usa la clase oficial sin editar sus directorios protegidos. El adaptador del verificador amplía la detección de fuentes a esa raíz externa y usa la fecha del driver. No elimina comprobaciones.

| Corrección | Cambio aplicado | Evidencia |
|---|---|---|
| PROF-01 | Cuadros y gráficos principales UF, cuadros formales CLP/UF/USD | PDF, cuatro gráficos nativos en Excel y cuatro en PowerPoint, con conversiones E-24 |
| PROF-02 | Capital base CLP 730 millones, cero línea, piso CLP 20 millones y cota antes de cobros; siete escenarios a precio fijo | Flujo de Caja, Control de entrega, Sensibilidad, Escenarios corregidos y pruebas de recálculo |
| PROF-03 | Compras y puesta en marcha por mes; dotación según capacidad y demanda | Costos, Dotación por perfil y gráfico de egresos M1–M56 |
| PROF-04 | Cobertura fija, cierres temporales y reducción de carga variable por madurez | Contrato de soporte, Soporte por perfil, Personal y condiciones de reducción en el informe |
| PROF-05 | Préstamo, socios, interés, comisión y pago explícitos | Financiamiento, Flujo de Caja, gráfico de desembolso y amortización M21 |
| PROF-06 | Diez pilotos internos y 172 montajes externos M7–M9; descuento de 401 h 20 min internas sustituidas | Instalación por lote y Dotación por perfil. Servicio neto CLP 10.984.533 frente a CLP 6.421.333 de trabajo sustituido |

Las seis correcciones están incorporadas al presupuesto y a su exposición. Las condiciones de contratación, financiación y validación operativa se identifican como tales. No se presentan como acuerdos ya firmados. La base conserva costo neto CLP 6.906.281.106, venta CLP 8.473.964.547, margen EBITDA 18,5% y VAN CLP 1.076.600.979. Las nuevas condiciones de liquidez no se confunden con la aprobación de financiación real.

La planilla anterior identificada tiene capital CLP 274.452.748, préstamo CLP 219.562.198,40 y socios CLP 54.890.549,60. Su orden de magnitud concuerda con las referencias orales de préstamo de 210–250 millones y socios cercanos a 50 millones. Esto permite conciliar las cifras históricas, sin certificar cuál archivo se proyectó efectivamente ante el profesor. La nueva estructura de 584 millones de banco y 146 millones de socios se declara como cambio y se justifica por la cota conservadora de liquidez.

El estrés combinado sin facilidad tiene déficit mensual incluso agotando la línea. La facilidad presupuestada de CLP 420m cubre las pruebas combinadas con reserva M12 y anticipada M9. Las pruebas de atraso simple o choque de 5% sin esa facilidad pueden tener cierre positivo y cota previa a cobros negativa; esa exposición se muestra expresamente. No se declara cubierto todo estrés posible.

Comprobaciones: recálculo completo con Calc y cero celdas de fórmula con error; 19.418 fórmulas; 40 hojas; rótulos y orden de RESUMEN conservados; cero vínculos externos; cuatro cambios de entrada en copias en memoria. El verificador formal mide los PDF, comprueba cifras y referencias y contrasta 34 celdas contra partidas.csv. La presentación tiene diez láminas y pasa validación de paquete, geometría, fuentes, tres tablas y cuatro gráficos editables con datos embebidos. Se revisó también su exportación con LibreOffice, sin afirmar ejecución en Microsoft PowerPoint.

La advertencia de estilo del verificador corresponde principalmente a rangos de páginas/meses escritos con guion y a signos de puntuación del texto heredado. No quedan incumplimientos formales. Las raíces múltiples de TIR de escenarios no convencionales se documentan en `revision/resultados.json`; no se escoge la más alta para justificar la oferta.

La navegación del prototipo se comprobó a nivel de interfaz. No se acreditó SLA productivo ni duración real de exposición. Los68 estados técnicos anteriores se preservan y no se convierten en cierres ficticios. Ignacio Cuevas y Martín Cevallos figuran en las adendas internas A-6 por indicación del usuario, con asistencia alta de IA y sin una firma o revisión humana inventada. Revisar `LEEME-ANTES-DE-ENVIAR.md` antes del envío.
