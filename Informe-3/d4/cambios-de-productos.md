# Cambios de productos para el Informe 3

Fecha: 2026-11-07. Referencia: Formulario T-11 del Informe 2 (`audIT/recursos/Formato-Oferta-audIT/salida/informe2/`).
El cambio de modelo (Karbon 430 a AAEON ICS-6280A-A10-00) quedó aplicado el 2026-11-11 en las figuras, el S4 y el T-11 (D4-142). Los demás siguen sin aplicar y quedan para las correcciones del Informe 3.

## Cambio de modelo

- Fila 9, computador de terminal (8 unidades): OnLogic Karbon 430 pasa a AAEON ICS-6280A-A10-00.
  Motivo: el Karbon 430 figura como descontinuado y su garantía es de 2 años, lo que choca con el
  criterio de vigencia de 56 meses (FEP02, numeral 1.6, p. 5). El AAEON usa el mismo Atom x6425E, va
  en riel DIN, opera de −40 a +75 °C y tiene doble entrada de 9 a 48 V. Según su ficha viene sin RAM ni
  SSD y AAEON no publica su consumo: el cálculo toma 40 W por equipo (adaptador del fabricante), y el
  gabinete pasa de 152 a 162 W y la UPS de 83 a 78 minutos. Garantía de 2 años extensible. (D4-138 a y D4-142)

## Modelo genérico que pasa a un producto concreto

- Fila 12, fuentes redundantes de gabinete: «fuentes de riel DIN de 24 V y de 48 V con módulo de
  redundancia» pasa a Mean Well SDR-120-24 y SDR-120-48 (120 W), con módulos Mean Well DRDN20-24 y
  DRDN20-48. Dimensionado sobre los 98 W del bus de 24 V (2 × 40 W del ICS-6280 más 18 W del RUTX50) y los 64 W del bus de 48 V del S4 §4.2.8.
  (D4-137 c)
- Fila 14, inyector del punto de acceso: «inyector 802.3bt» sin modelo pasa a Fortinet GPI-145
  (802.3bt, 60 W). El GPI-130 se descartó porque es 802.3at y no alcanza los 28 W del FortiAP 234G.
- Fila 17, segundo adaptador del FortiGate 90G: sin modelo pasa a Fortinet SP-FG60E-PDC-5 (pack de 5
  adaptadores, compatible con 60E, 90G y 91G). (D4-130)
- Fila 23, extintor portátil: «extintor de dióxido de carbono» pasa a extintor de CO2 de 5 kg como
  referencia de precio. (D4-137 c)
- Fila 29, rack: «rack cerrado de 24 unidades» pasa a APC NetShelter SX 24U AR3104 como referencia de
  precio.

## El modelo no cambia, pero se presupuesta con un equivalente

- Fila 5, lector de tarjeta del conductor: el GAO RFID MIFARE DESFire se mantiene en el T-11 y se
  presupuesta con el precio de un lector GeoVision IP66 de 13,56 MHz, porque GAO no publica precio.
  Falta confirmar RS485 en el equivalente. (D4-137 c)
- Fila 16, servidor: el Dell PowerEdge R360 se mantiene y se presupuesta con su configuración de
  entrada. Falta ajustar procesador, memoria, discos y segunda fuente. (D4-141 d)

## Cambio de cantidad

- Fila 2, crecimiento de la flota propia: 22 iWave G26I solos pasan a 22 juegos completos (G26I,
  Iridium Edge, Technoton CANCrocodile y lector GAO RFID). Sin los periféricos esos camiones no
  cumplen el diseño a bordo. (D4-141 b)
- Repuestos de sala y de gabinete, que el T-11 no trae: se agrega una unidad de cada equipo crítico,
  que compra el mandante y se guarda en San Bernardo (FEP02, numeral 8.4, p. 19). (D4-141 c)
  - Dell PowerEdge R360: 1
  - Fortinet FortiGate 90G: 1
  - Fortinet FortiSwitch 124F-POE: 1
  - APC SRT3000RMXLI: 1
  - AAEON ICS-6280A-A10-00: 1
  - Teltonika RUTX50: 1
  - Teltonika TSW202: 1
  - APC SRT1000XLI: 1
  - Mean Well SDR-120-24: 1
  - Mean Well SDR-120-48: 1
- Unidades de prueba antes de la compra masiva, que paga audIT (FEP02, RT-08.15, p. 19): una de cada
  dispositivo de terreno (G26I, Edge, CANCrocodile, lector GAO, baliza EYE, AAEON, RUTX50, TSW202,
  FortiAP 234G y Minew G1). (D4-135 e)

## Cambio propuesto y revertido

- Fila 4, lector CAN sin contacto: Technoton CANCrocodile pasaba a Teltonika ECAN02 (D4-137 b), y
  vuelve a CANCrocodile (D4-138 b). Motivo: no se pudo verificar que el ECAN02 funcione con el iWave
  G26I, y el CANCrocodile sí tiene precio público (€47,00 en la tienda oficial de Technoton). Queda el
  riesgo de proveedor único con sede en Belarús.

## Sin cambio, con aviso

- Filas 7 y 8, baliza Teltonika EYE Sensor BTSMP1: un vendedor marca un código como fin de vida, con
  reemplazo de firmware nuevo. Hay que pedir el código vigente al comprar.
- Fila 18, FortiSwitch 124F-POE: sigue con una sola fuente. Continúa abierto el RT-08.04 de D4-130.
- Filas 20 y 22, clima Vertiv Mini-Mate2 y extinción Kidde FK-5-1-12: sin cambio de modelo, pero sin
  precio público. Necesitan cotización.
