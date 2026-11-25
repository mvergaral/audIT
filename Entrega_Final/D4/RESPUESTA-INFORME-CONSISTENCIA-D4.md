# Respuesta de D4 al informe de consistencia contra la entrega 3.2

| Dato | Valor |
|---|---|
| Fecha | 2026-11-25 |
| Informe | `INFORME_CONSISTENCIA_ENTREGA3_VS_SUBDOCS.md` (54 hallazgos) |
| Alcance | Solo los hallazgos de archivos de D4: S4.2 y 4.3, T-11, S8, T-16, S10, S11, S12, T-8, S13, T-19 y S14 |
| Fuente usada | Modelo final de D2 `economico/planilla/AUDIT_ModeloFinanciero_3_20261125.xlsx` (mismo valor de contrato que la 3.2), malla de D2, S1 de D1 y bases con `tools/buscar.py` |
| Decisión | D4-163 |
| Estado | Escrito en el formato local de D4, en revisión antes de pasar al repo |

Cada hallazgo se comprobó contra la fuente antes de corregirlo. Tres no se aplicaron tal como venían, y la tabla dice por qué.

## Aplicados

| ID | Dónde | Qué se hizo |
|---|---|---|
| CRIT-03 | S4 §4.2.1 | El párrafo separa lo que compra el mandante (equipo a bordo, tarjetas EV3 4K, balizas, RUTX50, TSW202, FortiAP con GPI-145, Minew G1, FortiGate y FortiSwitch) de lo que provee audIT (AAEON, fuentes DIN, UPS, R360, climas, VESDA, Kidde, extintores, Suprema, Axis, detector de agua, racks y grupo electrógeno), igual que la columna «Adquiere» del T-11 y la hoja «Hardware del mandante» |
| CRIT-05 | Declaraciones de S4 y T-11 | Las filas de D3 con «Responsable D3» o «Pendiente de validación» quedan con los revisores de D4. Las filas de D4 ya no citan la planilla 3.2, los informes anteriores ni códigos ARQ-0x. El texto del S4 ya no cita «observación 71, 73 y 75 del Informe 1» ni el Informe 1 en el Novec y el plano de sala |
| CRIT-08 | S10 §10.5 | El libro del terminal sin enlace dice al menos 24 horas, el mayor entre las 12 del RT-03.10 del Caso y las 24 del Art. 16.4 |
| CRIT-09 | S11 §11.5 | El ejercicio de octubre opera el terminal al menos 24 horas sin enlace, con la misma cita |
| CRIT-10 | S11 §11.1 | La tabla del 13.4 suma una fila de refuerzo de 103 horas y da 743 en M21–M24, con nota de 823 en M21. El texto declara 226 horas de datos y 197 de pruebas, con los refuerzos de 66 y 37 |
| CRIT-11 | Declaración del S13 | Igual que CRIT-05, y sin las referencias a INN-02, INN-05 ni al Informe 1 |
| MAY-05 | T-11 | Las filas 57, 60, 62 y 63 remiten a las filas 16, 17 y 18, 15 y 14 |
| MAY-06 | S4 §4.2.7 y T-11 fila 18 | El FortiSwitch tiene una sola fuente. La redundancia está en el par, uno por circuito, más el repuesto. Si el diseño exige doble fuente por chasis, se cambia el modelo antes de la compra del mes 3 |
| MAY-07 | S4 §4.2.3 | Las filas 32 a 78 del T-11 son 47 componentes: 32 en la región primaria, 1 en Brazil South y 14 fuera de la nube |
| MAY-15 | S8 y T-16 R-36 | R-36 suma la autorización previa y escrita del mandante y el control del tope del 40 % del Art. 73.1 con el T-8. El técnico de campo de audIT respalda hasta el mes 18 |
| MAY-16 | S8 y T-16 | Nuevo R-37, escalones de madurez del soporte (6 a 4, audIT), con disparador dos meses antes de cada escalón. El H5 entra a la vigilancia de R-17 como el escenario de caja más exigente del Sobre N.º 3. Son 36 riesgos |
| MAY-18 | S10 §10.4 | Base de 1.280 horas, refuerzos de M21–M24 y escalones de 1.200, 1.120 y 1.040 horas |
| MAY-19 | S11, resumen | Dos pruebas reales de recuperación al año, seis en 36 meses, y dos ejercicios de resiliencia al año con cuatro escenarios |
| MAY-20 | S11 §11.2 | La deuda técnica toma 72, 48 y 24 horas al mes por tramo, el 30 % de la parte variable |
| MAY-21 | T-8 | Implantación, Integración y Funcional van en los meses 3 a 20, como la dotación por perfil |
| MAY-22 | T-8 y S12 | El equipo clave en operación queda igual que el S1 de D1: Arquitecto con 45 horas de cierre en M21–M24 y apoyo a demanda, y Líder de Calidad con 50 %. Las 480 horas al mes se mantienen y cada rol se asocia a su línea del presupuesto |
| MAY-23 | S13 introducción e innovación 1 | Ninguna innovación tiene beneficio monetario base ni cobro incremental. El personal va en la dotación del contrato y el único egreso de la 1 es la firma electrónica desde el mes 13 |
| MAY-24 | S13 innovación 4 y ficha 4 | Sin partida propia ni costo incremental. Los 34 comodatos son parte de los 182 equipos base. El recupero es bruto, referencial y de Curimón |
| MAY-25 | S13 innovación 5 y ficha 5 | Desarrollo y soporte en la dotación. El único egreso son los talleres del mes 4 y la calibración externa de M13–M15 |
| MAY-26 | S14 §14.2 | 1.520 horas reservadas en la implementación y 3.032 en 56 meses, en vez de 2.560 |
| MEN-03 | S4 §4.3.1 | audIT se hace cargo desde el mes 4 de unos 50 litros al mes de combustible de pruebas y unos 3.000 kWh al mes de energía de sala y gabinetes |
| MEN-04 | T-11 filas 6, 8, 14 y 17 | MIFARE DESFire EV3 4K, balizas 12, 12 y 11 en los meses 24, 36 y 48, inyector GPI-145 y pack SP-FG60E-PDC-5 |
| MEN-07 | S8 | Sin «Informe 2» ni «planilla económica 3.2» |
| MEN-12 | S10 §10.3 | La mesa programa 930 horas en un mes de 31 días con 30 de reserva, más las 160 de suplencias, y cita el Sobre N.º 3 |
| MEN-13 | Declaración del S10 | Siete personas del paquete 13.1 |
| MEN-14 | S11 §11.4 | Los usuarios de GitLab siguen la dotación de operación, que baja de 15 a 14 personas |
| MEN-15 | T-8 | El servicio de ergonomía incluye la calibración de M13–M15 |
| MEN-16 | T-8 | Los comentarios del archivo ya no tienen montos |
| MEN-17 | S14 §14.1 | Beneficios operacionales sin beneficio monetario base ni cobro incremental |

## Aplicados con otra solución

| ID | Qué pedía | Qué se hizo y por qué |
|---|---|---|
| CRIT-04 | Regenerar `04-arquitectura/contenido.md` | El espejo `.md` lo mantiene D3 con un formato propio. Se regenera desde el S4 compilado después de esta corrección, sin cambiar la parte 4.1 de D3 |
| MAY-04 | Cambiar «meses 17 a 19» por «16 a 18» | No se cambió. La malla de D2 y el T-14 ponen A21-PATIO en los días 320 a 380, es decir M17 a M19. Se agregó lo que sí pedía: el técnico de campo cubre hasta el mes 18 y desde el 19 el campo es externo, y la media jornada son 80 horas al mes |
| MEN-07 (R-26) | Cambiar el reenvío de 72 horas por el búfer de 288 | No se cambió el número. El S4 dice que el equipo conserva lo ya enviado durante 72 horas, y el búfer de 288 horas es lo que todavía no se envía. R-26 ahora lo dice así |

## Pedido del prompt maestro

| Pedido | Qué se hizo |
|---|---|
| Corregir la figura ilegible del S4 | La vista completa (4,38 pt) pasa a cinco láminas a 9 pt: San Bernardo en dos, la nube, terminales y contrapartes, y la flota. Las conexiones entre láminas llevan el mismo número en las dos. Guion `D4/graficos-v2/fuente/fisica_laminas.py` |
| Revisar riesgos frente a la malla vigente | R-17 y el S8 dicen lo mismo que el S7: H4, H7 y H12 sin margen y H11 con A23. D2 reprodujo la simulación |
| Proveedores | R-36 con Art. 73.1 y técnico hasta M18 |
| Calendario de montaje | 182 equipos en M9, M17–M19 sin montajes iniciales, ya corregido en D4-162. D2 corrigió C83 y A17 de su planilla |

## Fuera del alcance de D4

Los hallazgos de S1, S2, S3, S5, S6, S7, S9, T-6, T-12, T-13, T-14, T-15, T-17 y T-18 son de otras duplas y no se tocaron.
