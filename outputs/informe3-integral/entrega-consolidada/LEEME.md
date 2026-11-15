# Paquete consolidado · Informe 3

**TFEP-01/2026 · Simulación académica · 14 de noviembre de 2026**

Se usó el corte auditado c9a6515652c3357ea684bf0bb9338b7c4ec028fd. El addendum del PDF y las últimas láminas documentan la revisión. Las nuevas hojas de Excel incluyen fechas, movimientos, fórmulas de saldo, mínimos por mes, anexos y referencias de instalación y soporte. El cuerpo original de la oferta conserva los escenarios históricos. Las fuentes y cambios en curso de la rama de cierre se preservaron. [Corte de origen](https://github.com/mvergaral/audIT/commit/c9a6515652c3357ea684bf0bb9338b7c4ec028fd)

## Cierre de tesorería

- Se comprobaron los 56 cierres mensuales de las tres variantes de financiación y la continuidad hasta M57. En los nueve meses críticos se conciliaron 36 combinaciones de escenario y mes, incluidas las pruebas con H6 retrasado. El piso se cumple en las secuencias simuladas. En M1 la prueba parte del capital abonado antes de los egresos.
- Se incorporaron los tres anexos académicos aprobados. Se conserva el hito contractual H5 en M12. Se simula el pago a 15 días en M13 y a 30 días en M14, manteniendo el importe.
- Si H5 pasa a marzo y H6 pasa al 17 de febrero, la alternativa consiste en diferir CLP 19.510.000 de la reserva D4 de enero al 17 de febrero, después del cobro de H6. La caja queda en CLP 10.003.606,27 después del IVA y antes del abono del 17. El diferimiento depende de que la reserva admita el cambio de fecha. Si la reserva ya está comprometida, se necesitan al menos CLP 19.506.394 disponibles antes del IVA del 16 para alcanzar el piso, con nueva comprobación si el atraso alcanza el pago siguiente.
- Los días y horas utilizados son supuestos de tesorería. La comprobación intramensual abarca M1, M9, M10, M12, M13, M14, M15, M16 y M21. Las hipótesis sobre cobros de H4, H6, H7, H8 y H12 requieren revisión si se usa el flujo fuera de este ejercicio.

## Trazabilidad técnica que sigue abierta

La revisión complementaria concilia la agenda simulada de 182 montajes, la cotización por 172 montajes tras el piloto, el efecto de IVA en M9, el refuerzo temporal por rol y las pruebas de atención y recuperación. [Anexo técnico D1/D2](Cierre-tecnico-D1-D2.md)

- **Instalación.** Se conciliaron 182 kits, 910 horas-persona y CLP 16.258.667 de referencia por mes y rol. El comparador de externalización para sustituir únicamente el montaje del técnico a bordo es CLP 37.333 por equipo. D2/D4 aún requieren agenda por terminal, resultados del piloto, cotización, autorización escrita y cruce con las filas de nómina que se sustituirían. Las 210 balizas se registran aparte, con 52,5 horas-persona y perfil por confirmar. [AUD-15](https://linear.app/audit-fep/issue/AUD-15) · [AUD-21](https://linear.app/audit-fep/issue/AUD-21) · [Referencia de D2](https://github.com/mvergaral/audIT/blob/c9a6515/Informe-3/d2/APORTE_ECONOMICO_INNOVACIONES_1_Y_4.md)
- **Soporte.** Se identificaron las 2.560 horas mensuales de T-15 por actividad de continuidad y el contrato estimado de fabricante de CLP 3.331.927 mensuales desde M13. La disminución de CLP 2.852.000 en nómina global desde M25 queda a nivel agregado. Falta vincularla a roles, volumen de atención, horas reforzadas y cobertura SLA. [T-15](https://github.com/mvergaral/audIT/blob/c9a6515/recursos/Formato-Oferta-audIT/subdocumentos/07-plan-trabajo/formularios/T-15.tex) · [AUD-34](https://linear.app/audit-fep/issue/AUD-34)

**Registro de IA para A-6.** Se usó IA para preparar anexos simulados, calcular secuencias de caja, reconstruir referencias de instalación y soporte y preparar las copias consolidadas. La revisión humana debe registrarla quien la realice.
