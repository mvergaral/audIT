# Filas de D4 para el anexo del Art. 46 (oferta final)

| Dato | Valor |
|---|---|
| Fecha | 2026-11-24 |
| De | D4 (S4.2/S4.3, S8, S13 y T-11, T-16, T-19) |
| Para | D1, que mantiene `anexos/observaciones-informe3.tex` |
| Base | Revisión final del Informe 2 y anexo regenerado en `main` (5011546), con el cierre de D3 (84dbc21) |
| Estado de los cambios | Subidos a `main` (D4-161 y D4-162) |

Cada fila trae el texto de respuesta y de sección y estado, listo para reemplazar el que hoy dice «Pendiente». ARQ-01 y ARQ-02 son de la parte 4.1 (D3) y no van aquí.

## Generales

**GEN-06** · T-11 sin declaración propia
- Respuesta: El T-11 cierra con sus Referencias y su Declaración de uso de IA propias. El T-16 y el T-19 también traen su declaración.
- Sección y estado: Formularios T-11, T-16 y T-19. Estado: Incorporada (bloque S4/S8/S13). T-14, T-15 y T-18 quedan a cargo de D2.

**GEN-05** · S8 con uso alto de IA y revisión concentrada
- Respuesta: La declaración del S8 nombra a tres revisores por sección y dice qué verificó cada uno, incluida la regla de la simulación sobre la malla conciliada.
- Sección y estado: Declaración de IA del S8. Estado: Incorporada para el S8.

## Arquitectura física (S4.2, S4.3 y T-11)

**ARQ-03** · Mesa de ayuda sin dimensionar
- Respuesta: El S4 resume el dimensionamiento: 576 contactos al mes con Erlang C, dos agentes en el relevo de madrugada y uno el resto del día, 851 horas cubiertas por seis agentes más una jornada de suplencias (siete en total), y el campo con media jornada interna más un proveedor externo. El cálculo completo y su sensibilidad están en el S10.
- Sección y estado: S4 §4.2, dimensionamiento, y S10 §10.3. Estado: Incorporada.

**ARQ-04** · Alcance del ExpressRoute a Chile Central
- Respuesta: Se nombran los proveedores de Santiago (Cirion, Equinix y PitChile). Se exige confirmación escrita antes de contratar y la conmutación a la VPN se prueba en la Etapa 1. Si el circuito no llega, se contrata Premium o dos VPN por rutas distintas. Queda como R-33 en el T-16.
- Sección y estado: S4 §4.2, enlaces, y T-16 R-33. Estado: Incorporada.

**ARQ-05** · Datos personales en Brazil South
- Respuesta: Antes del H2, Curimón valida con una asesoría legal externa el instrumento contractual con garantías adecuadas de los artículos 27 letra b) y 28 de la Ley N.º 21.719. Mientras tanto, Brazil South solo recibe artefactos técnicos y datos sintéticos, y los datos personales quedan en Chile Central con alta disponibilidad entre zonas: réplica sincrónica, sin pérdida de datos confirmados y conmutación de 60 a 120 s (fuente Microsoft). Cubre una zona y no la región completa. Si no hay vía habilitante, se selecciona y ensaya un sitio secundario admisible (RPO hasta 15 min, RTO hasta 4 h, RT-07.04), y el H7 exige ese ensayo con acta (R-24).
- Sección y estado: S4 §4.3 (texto conjunto con D3, que responde ARQ-01 y ARQ-02), S8/T-16 R-24 y T-8. Estado: Incorporada (la vía habilitante se acredita antes del H2).

**ARQ-06** · Numeración y fuentes del T-11
- Respuesta: Las tablas del T-11 se numeran T-11.n. El formulario trae sus Referencias y su ficha de fabricante por fila.
- Sección y estado: Formulario T-11. Estado: Incorporada.

**ARQ-07** · Brechas declaradas
- Respuesta: Una tabla da, para cada una de las cinco brechas, el dato que falta, la prueba o consulta con su plazo y la contingencia. La autonomía ofertada (288 h del G26I y la prueba de 72 h) queda separada del producto satelital del Informe 1.
- Sección y estado: S4 §4.2, supuestos y brechas, y T-16 R-04 y R-08. Estado: Incorporada.

**ARQ-08** · Autoridad tributaria en la Figura 4.13
- Respuesta: La autoridad tributaria queda fuera del sitio. La línea al sistema contable lleva el rótulo «Internet del emisor», y el texto explica que el emisor se comunica por su propio enlace y que la capa anticorrupción solo le pide la emisión.
- Sección y estado: S4 §4.2, Figura 4.13. Estado: Incorporada.

## Riesgos (S8 y T-16)

**RIE-01** · Riesgos internos y R-06
- Respuesta: Cada riesgo declara su origen (mandante, terceros o audIT) y R-06 salió del registro activo. Son 35 riesgos: 17 de terceros, 12 de audIT y 6 del mandante.
- Sección y estado: S8 §8.1 y T-16. Estado: Incorporada.

**RIE-02** · Convivencia y retiro del sistema de 2013
- Respuesta: Queda como R-29, con retiro por función en M16, M21 y M24, conciliación diaria, reversión probada y acta del mandante. Su contingencia está en el S8.
- Sección y estado: S8 §8.2 y T-16 R-29. Estado: Incorporada.

**RIE-03** · Adopción de las innovaciones 1 y 2
- Respuesta: R-30 (9 a 6) y R-31 (6 a 4), conciliados con las fichas 1 y 2 del T-19.
- Sección y estado: S8, T-16 y T-19. Estado: Incorporada.

**RIE-04** · Árbol de fallas sin cuantificar
- Respuesta: Se fija el protocolo de conteo sobre unas 16.000 asignaciones del paralelo M13–M14, con intervalo binomial del 95 % y la regla del tres cuando no hay eventos.
- Sección y estado: S8 §8.2, árbol de fallas. Estado: Incorporada.

**RIE-05** · Razón de retorno
- Respuesta: Se define la razón de retorno de cada respuesta material como pérdida esperada evitada sobre costo, valorizada con las multas del Art. 80. Los montos van en el Sobre N.º 3.
- Sección y estado: S8 §8.3. Estado: Incorporada.

**RIE-06** · R-17 aceptado con atraso de H1 y H2
- Respuesta: Sobre la malla conciliada, H4, H7, H11 y H12 quedan sin margen. R-17 pasa a exposición alta, con umbrales, escalamiento, recuperación con refuerzo y contingencia de entrega con alcance comprometido y acta. La malla se ajusta antes del H1 y la simulación se vuelve a correr. No se publican probabilidades de la red anterior.
- Sección y estado: S8 §8.2 y §8.3 y T-16 R-17. Estado: Incorporada (nueva simulación sujeta al ajuste de la malla con D2).

**RIE-07** · Numeración repetida entre S8 y T-16
- Respuesta: Las tablas del T-16 se numeran T-16.n y el S8 remite a ellas por su número propio.
- Sección y estado: S8 y T-16. Estado: Incorporada.

**RIE-08** · Desconexión física y mitigación de R-14
- Respuesta: Nuevo R-35, desconexión física de antena, CAN o alimentación por un conductor externo, con exposición 12 a 8 y contingencia. Su detección es el equipo sin reporte en un tramo con cobertura, más sellos revisados en terminal, bloqueo de la siguiente asignación y la cláusula del anexo. R-14 se apoya ahora en el anexo de adhesión y en el incentivo de comodato de la innovación 4.
- Sección y estado: S8 §8.2 y T-16 R-14, R-22 y R-35. Estado: Incorporada.

**Nota sin observación propia** · Calendario de instalación
- Nota para D1: S4, S12, S13, T-19 y R-19/R-31 del T-16 ya dicen que los 182 equipos se montan entre M6 y M9 y que en M17–M19 solo se valida y se repone por excepción, igual que el S7.

**PLA-10 / PLA-12** (bloque S7/S8)
- Respuesta: R-32 cubre la disponibilidad de usuarios en la temporada de fruta. R-34 cubre los cierres de Los Libertadores sobre las ventanas fijas del piloto y de los lotes (días 112 a 180), eligiendo camiones que no cruzan la frontera y reemplazando dentro del mismo lote.
- Sección y estado: S8 §8.2 y T-16 R-32 y R-34. Estado: Incorporada en el S8. La parte de S7 y T-18 es de D2.

## Innovaciones (S13 y T-19)

**INN-01** · Innovación 2 con TRL 2 y línea base sin medir
- Respuesta: La ficha fija la línea base en el piloto de M6, el método de medición, los umbrales (preparación inútil −20 %, primer intento ≥ 95 %, sustitución ≤ 30 min) y la decisión del Comité al cierre de M6, con sustitución si no se acredita. El beneficio base queda en cero.
- Sección y estado: S13 §13.2 y ficha 2 del T-19. Estado: Incorporada.

**INN-02** · Kilometraje en la innovación 3
- Respuesta: El kilometraje queda como alcance base del criterio 26. La innovación 3 se renombra «Acople verificado y registro térmico del semirremolque», igual que el paquete 12.3 del T-14.
- Sección y estado: S13 §13.3 y ficha 3 del T-19. Estado: Incorporada.

**INN-03** · Catálogo de paradores en la innovación 5
- Respuesta: El catálogo es alcance base del criterio 28 y no se imputa a la innovación. La innovación 5 queda como «Anticipación circadiana y aviso no punitivo de descanso», igual que el paquete 12.5 del T-14.
- Sección y estado: S13 §13.5 y ficha 5 del T-19. Estado: Incorporada.

**INN-04** · Riesgo residual de las fichas
- Respuesta: Cada ficha declara su exposición inicial y residual, enlazada al T-16: R-30 (9 a 6), R-31 (6 a 4), R-22 (8 a 4), R-11 (12 a 8) y R-14 (9 a 6). La innovación 5 tiene un plan adicional con disparadores: adherencia bajo 70 % en M14 o NASA-TLX sobre 35 puntos.
- Sección y estado: S13 y T-19, fichas 1 a 5. Estado: Incorporada.

**INN-05** · Base y magnitud de los beneficios
- Respuesta: El S13 explica el tratamiento de la planilla 3.2: beneficio cero en el escenario base para las innovaciones 2 y 3, valor pendiente de los datos de la Etapa 1 para la 1 y la 5, y recupero bruto referencial de la 4, que es de Curimón y no se suma a la venta. Cada ficha fija el indicador físico que se mide en el piloto.
- Sección y estado: S13, introducción y fichas. Estado: Incorporada.
