# Conciliación de respaldos de personal, gastos e infraestructura

Corte GitHub 8c950fa y planilla consolidada en la rama de cierre. Las partidas de este registro conservan sus importes vigentes hasta recibir evidencia que justifique un ajuste.

## D1, D2 y D3 · Personal y CP-SEC-05

Linear acepta la coordinación nominal para la entrega. La ficha de reservas de AUD-14 y la matriz INN-5 de AUD-15 conservan vacíos los campos de ejecutor, aceptación y horas netas acreditadas. El Excel consolidado tiene 40 cruces de capacidad y ninguno registra horas disponibles acreditadas.

| Partida | Mes y base de cálculo | Neto CLP | Estado |
|---|---|---:|---|
| Seguridad/SRE | M9 | 1.108.000 | Cupo presupuestado |
| Datos/QA | M21–M24, 2.852.000 por mes | 11.408.000 | Cupos presupuestados |
| INN-5 desarrollo | M4–M9, 50 h/mes × 30.000 | 9.000.000 | Refuerzo nominal |
| INN-5 soporte | M21–M56, 10 h/mes × 28.000 | 10.080.000 | Refuerzo nominal |
| **Total de refuerzos** | Hoja Refuerzo presupuestado | **31.596.000** | Conservar hasta acreditar cobertura interna |

INN-5 concilia en importes con D1. La inversión de CLP 13.000.000 se compone de CLP 9.000.000 de desarrollo, CLP 2.200.000 de talleres M4 y CLP 1.800.000 de calibración M13–M15. La operación de CLP 10.080.000 corresponde al soporte. La aceptación por ejecutor y el IVA de la calibración siguen pendientes.

| Preparación CP-SEC-05, 4.1/A11 | Horas por perfil | Total |
|---|---|---:|
| M6 | Arquitectura 4, Software 8, Seguridad 4 | 16 |
| M7 | Software 16, QA 8 | 24 |
| M8 | Software 8, QA 4, SRE 4 | 16 |
| M9 | Software 4, QA 8, SRE 4 | 16 |
| **Total** | Demanda documentada fuera de A09 | **72** |

La preparación tiene un costo atribuible de referencia de CLP 2.016.000. Se requiere identificar la fila de nómina, ejecutor y horas netas por perfil y mes. Las 8 h QA de M9 podrían coincidir con CP-HW-03. Descontarlas exige comprobar que es la misma ejecución. La campaña G13 cuenta con 15 h estimadas de D1 y D4 dentro de una reserva condicional de 16 h en 10.1. Esa campaña se concilia por separado.

[Reserva AUD-14](https://linear.app/audit-fep/issue/AUD-14) · [Refuerzo y cobertura INN-5 AUD-15](https://linear.app/audit-fep/issue/AUD-15) · [Detalle de preparación](https://github.com/mvergaral/audIT/blob/8c950fa/Informe-3/d2/AUD-14_COSTO_PERSONAL_POR_PERFIL.md#L723) · [Calidad AUD-10](https://linear.app/audit-fep/issue/AUD-10)

## D1, D2 y D4 · IVA, garantías y overhead

| Partida | Tratamiento comprobado | Evidencia pendiente |
|---|---|---|
| LTE a bordo y ExpressRoute | CLP 14.432.400 de IVA referencial en la caja base, en el mes del servicio. Crédito fiscal modelado en cero. | Cotización, emisor, receptor, documento, fecha de pago y crédito aplicable. |
| Hardware inicial audIT y SIM 5G | CLP 21.828.338 de IVA referencial en el registro D4. | Canal, base de internación, factura y mes efectivo. |
| Azure/Entra, Iridium, soporte, reposición, R-24 y disposición final | Registro mensual con netos y canales de referencia. | Emisor, receptor, base afecta, impuesto, pago y eventual crédito. |
| GitLab, SonarQube y firma | Netos presupuestados e IVA referencial. | Facturación, titularidad, pago y crédito aplicable. |
| Calibración INN-5 | CLP 1.800.000 netos. Sensibilidad de CLP 114.000 de IVA mensual en M13–M15. | Régimen y documento del prestador. |
| Fiel cumplimiento, RC, ciberriesgo, notaría y custodia | CLP 85.400.000 calendarizados. CLP 13.800.000 adicionales en M56 por extensión y cola, imputados una vez. | Condiciones de póliza, base, prorrateos y pago. |
| Garantía de correcto funcionamiento | 0,15 % sobre precio de implementación, con desembolso estimado en M21. | Condiciones y fecha de constitución. |
| Seriedad de oferta | CLP 2.812.500 de referencia. Sensibilidad preoperacional en M0. | Comisión, exigibilidad y fecha. |
| Todo riesgo, accidentes y overhead | Criterios preliminares documentados. | Base asegurable y mapa de importes ya incluidos en RRHH o R-24. |

La hoja Proveedores totaliza CLP 69.374.046 en su columna referencial. Ese total tiene una cobertura distinta de la caja base. Para cerrar por partida se requiere identificar pagador, emisor, receptor, neto, IVA, mes efectivo y crédito recuperable, y conciliar los importes existentes antes de moverlos al flujo.

[AUD-16](https://linear.app/audit-fep/issue/AUD-16) · [Detalle mensual IVA D4](d2/AUD-16_IVA_PROVEEDORES_D4.csv) · [Calendario administrativo](d2/AUD-16_CALENDARIO_ADMIN_D1.csv) · [Criterios administrativos](d2/AUD-16_GASTOS_ADMINISTRATIVOS.md)

## D4 · Pagadores y precios estimados

| Partida | Base que usa el expediente | Evidencia pendiente |
|---|---|---|
| Hardware de campo y red | Mandante según Aclaraciones §9. | Verificar canal y costo puesto en destino antes de contratar. |
| Infraestructura local, instalación, Azure y conectividad | audIT según reparto actualizado de D4. | Confirmar condiciones comerciales y responsabilidades de cada contrato. |
| Energía de sala/gabinetes y combustible | Mandante según decisión interna D4-143 b. El propio D4 señala que falta base expresa. | Aclaración del mandante o decisión de presupuestarlo en audIT, con consumo, tarifa y calendario. |
| Clima de precisión | Dos unidades estimadas a USD 12.000 cada una. | Cotización con instalación, alcance y entrega. |
| Extinción | Una solución estimada a USD 15.000. | Cotización dimensionada y condiciones de instalación. |
| LTE M2M | CLP 28.260.000 netos de referencia. | Oferta por operador, líneas, cobertura, IVA y pago. |
| Circuito ExpressRoute | CLP 47.700.000 netos de referencia. | Oferta del operador, SLA, IVA y plazo. El puerto Microsoft se presupuesta en Azure. |

[AUD-39](https://linear.app/audit-fep/issue/AUD-39) · [Reparto D4](d4/4.8-compras-audit-y-mandante.md) · [Presupuesto de equipos](d4/4.1-presupuesto-equipos.md) · [Nube y conectividad](d4/4.2-nube-conectividad.md) · [Aclaraciones §9](../texto/Aclaraciones_Informe_3.md)
