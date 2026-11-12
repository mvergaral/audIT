# Borrador de precios (tareas 4.1 y 4.4)

Consulta: 2026-11-07. Precios netos salvo que se indique. Conversión del Formulario E-24 (FEP01, p. 73):
USD $900, EUR $1.000, UF $40.000, IVA 19 %. Archivo de trabajo, no es entregable.

| Fila T-11 | Equipo | Precio | Moneda | IVA | Tramo | Fuente | Nota |
|---|---|---|---|---|---|---|---|
| 1 y 2 | iWave G26I, IW-G26ISA-512-08G-MIW-XM-12-EM-LI1BXX-D | 454,31 | EUR | Neto (549,72 con IVA español) | 1 unidad, sin tramos | https://www.digikey.es/en/products/detail/iwave-global/IW-G26ISA-512-08G-MIW-XM-12-EM-LI1BXX-D/24374937 | Sin stock, plazo de fábrica 4 semanas |
| 3 | Iridium Edge | 359,00 | USD | Minorista EE. UU. | 1 unidad | https://satphonestore.com/products/iridium-edge | Ground Control no publica precio de equipo |
| 3 | Plan SBD bajo (GC-SBD-5KB-1) | 15,75 al mes | USD | No indica | 5.000 bytes al mes, exceso 3,15 por 1.000 bytes, activación 26,25, 12 meses | https://www.groundcontrol.com/products/iridium/short-burst-data-range/short-burst-data-plans/ | Servicio del mandante (D4-135 b) |
| 3 | Plan SBD medio (GC-SBD-25KB-1) | 36,75 al mes | USD | No indica | 25.000 bytes al mes, exceso 1,68 por 1.000 bytes, activación 31,50, 12 meses | igual | |
| 4 | Technoton CANCrocodile | 47,00 | EUR | No indica | 1, 3, 5 o 10 piezas, cotización desde 10 | https://e-shop.jv-technoton.com/product/cancrocodile/ | Tienda oficial. Salida CAN J1939/21 sin alterar, solo escucha. DHL a Chile desde €48. D4-138 (b) |
| 4 alt. | Teltonika ECAN02 | 15,84 a 17,34 | EUR | Neto | 1 unidad | https://shop.ascend.de/en/products/teltonika-telematics-ecan02-can-ecan02000001 | Descartado en D4-138: compatibilidad con terceros no verificada |
| 5 | GAO RFID lector DESFire IP66 RS485 | sin precio | | | | https://gaorfid.com/?p=19299 | Equivalente con precio: GeoVision IP66 13,56 MHz a USD 83,99 (https://www.ipsecuritydepot.com/geovision-55-rk352-100-gv-reader-13-56mhz-ip66/55-rk352-100/), sin RS485 confirmado |
| 6 | Tarjeta MIFARE DESFire EV3 4K | 1,35 | EUR | Por confirmar | 200 a 799 unidades (1,25 desde 800) | https://rfid.it/en/rfid-iso-cards-hf/1701-mifare-desfire-ev3-4k.html | |
| 7 y 8 | Teltonika EYE Sensor BTSMP1 | 19,99 | EUR | Neto | 10 o más | https://store.comet.bg/en/Catalogue/Product/47075/ | Un vendedor marca un código como fin de vida con reemplazo de firmware nuevo |
| 9 | AAEON ICS-6280A-A10-00 (reemplaza al Karbon 430, D4-138 a) | 523,61 | EUR | Por confirmar | 1 unidad | https://www.texim-europe.com/product/ICS-6280A-A10-00-AAE (precio del resultado de búsqueda, la página no abrió por certificado). Ficha: https://www.aaeon.com/en/p/din-rail-industrial-grade-network-appliances-ics-6280 | RAM, SSD, consumo y ciclo de vida por confirmar. HSSL indica 1 a 3 semanas |
| 9 ant. | OnLogic Karbon 430 | descontinuado | | | | https://www.onlogic.com/k430/ | Garantía 2 años. El K410 también está descontinuado. La línea vigente Karbon 520 parte en USD 2.997 (https://www.notebookcheck.net/Onlogic-readies-hybrid-cooling-rugged-Karbon-524-mini-PCs-with-Intel-Ultra-Core-100H-CPUs-and-Nvidia-SFF-Ada-GPUs.1109626.0.html) |
| 10 | Teltonika RUTX50 | 422,00 | EUR | Neto (510,62 con IVA 21 %) | 1 unidad | https://nasstore.eu/toode/teltonika-industrial-5g-router-rutx50 | |
| 11 | Teltonika TSW202 | 108,00 | EUR | Neto (130,68 con IVA 21 %) | 1 unidad | https://nasstore.eu/?p=15915 | |
| 14 | Fortinet FortiAP 234G | 1.157,00 | USD | Sin impuesto | 1 unidad, MSRP 1.497 | https://www.shi.com/product/49812984/Fortinet-FortiAP-234G | FortiCare aparte |
| 15 | Minew G1 | 78,00 | USD | No indica | 1 unidad (72 desde 100) | https://www.digikey.com.br/en/products/detail/minew/G1/26776367 | Vendedor del mercado de DigiKey |
| 16 | Dell PowerEdge R360 | 5.549,00 | USD | Sin impuesto | Configuración de entrada | https://www.dell.com/en-us/shop/ipovw/poweredge-R360 | Falta ajustar a la configuración del T-11 |
| 17 | Fortinet FortiGate 90G | 2.190,00 | USD | Sin impuesto | 1 unidad, MSRP 3.307 | https://www.publicsector.shidirect.com/product/46531574/Fortinet-FortiGate-90G | FortiCare aparte. Falta el segundo adaptador |
| 18 | Fortinet FortiSwitch 124F-POE | 1.030,00 | USD | Sin impuesto | 1 unidad, MSRP 1.458 | https://www.shi.com/product/41741169/Fortinet-FortiSwitch-124F-POE | Una sola fuente (RT-08.04 abierto) |
| 12 | Mean Well SDR-120-24, fuente DIN 24 V 120 W (referencia para el bus de 98 W (2 × 40 W del ICS-6280 más 18 W del RUTX50)) | 51,87 | EUR | Neto | 1 unidad (48,76 desde 20) | https://www.alimentatorishop.com/en/power-supplies-din-guide/sdr-120-meanwell-din-rail-power-supply-120w-input-88-264vac-voltages-12v-24v-48v | 2 por gabinete. Precio de referencia de un equivalente (D4-137 c) |
| 12 | Mean Well SDR-120-48, fuente DIN 48 V 120 W (bus de 64 W) | 57,40 | EUR | Neto | 1 unidad (53,96 desde 20) | igual | 2 por gabinete. Precio de referencia de un equivalente |
| 12 | Mean Well DRDN20-24 y DRDN20-48, módulo de redundancia | 21,20 | EUR | Neto | 1 unidad | https://elmark-automation.com/shop/mean-well/moduly-redundantne | 1 de cada uno por gabinete |
| 13 | APC Smart-UPS SRT1000XLI | 1.078,99 | EUR | Neto (1.305,58 con IVA español) | 1 unidad | https://bechtle.com/es-en/finder/product-family/apc-smart-ups-srt-system--376--f (ficha 4355988) | Galador 1.111,69 y e-nitiative 1.063,25 netos |
| 14 | Fortinet GPI-145, inyector PoE 802.3bt de 60 W | 300,00 | USD | Precio de lista | 1 unidad (descuentos hasta 239,21) | https://gov.connection.com/product/fortinet-1-port-gigabit-poe-power-injector/gpi-145/41597558 | El GPI-130 es 802.3at y no alcanza los 28 W del T-11 |
| 17 | Fortinet SP-FG60E-PDC-5, adaptador de CA (pack de 5, sirve a 60E, 90G y 91G) | 381,04 | USD | Sin impuesto | Pack de 5 | https://www.cdw.com/product/fortinet-power-adapter/6081868 | Segundo adaptador de los dos FortiGate (D4-130) |
| 19 | APC Smart-UPS SRT3000RMXLI | 5.278,00 | USD | Sin impuesto | 1 unidad, MSRP 6.995 | https://www.shi.com/product/31329371/Smart-Ups-Srt-3000Va-Rm-230V | CDW 4.741,99 |
| 19 | APC SRT96RMBP, batería externa | 1.447,99 | USD | Sin impuesto | 1 unidad | https://www.cdw.com/product/apc-smart-ups-srt-96v-3kva-rm-battery-pack/3895533 | |
| 20 | Vertiv Liebert Mini-Mate2 MMD12E | sin precio | | | | https://www.vertiv.com/en-us/products-catalog/thermal-management/room-cooling/mmd12e-3.55kw | Vertiv vende por revendedor. Sin equivalente con precio en USD o EUR |
| 21 | Xtralis VESDA VLF-250-00 | 2.381,00 | USD | Sin impuesto | 1 unidad | https://firealarm.com/?p=45838 | Un vendedor ofrece excedente nuevo a 1.795 |
| 22 | Kidde FK-5-1-12 para la sala | sin precio | | | | Solo kits de rack en libras | Sin equivalente con precio en USD o EUR |
| 23 | Extintor de CO2 de 5 kg | 79,95 | EUR | Con IVA de Portugal (23 %), neto 65,00 | 1 unidad | https://www.chlengenharia.pt/en/compra/5kg-co2-extinguisher-630048 | Precio de referencia de un equivalente |
| 24 | Suprema FaceStation F2 FSF2-ODB | 2.605,54 | USD | No indica | 1 unidad | https://titansecuritysupply.com/product/fsf2-odb-suprema-face-station-f2-em-mifare-fingerprint | |
| 25 | Axis M3215-LVE | 835,00 | USD | Sin impuesto | 1 unidad | https://www.shi.com/product/45220713/M3215-LVE | |
| 26 | Axis S3008 Mk II 4 TB | 903,99 | EUR | Neto (1.111,91 con IVA de Portugal) | 1 unidad | https://www.bechtle.com/pt-en/shop/axis-s3008-mk-ii-recorder-8ch-4tb--4814387--p | |
| 27 | Vertiv Liebert LT460 con cable de 20 pies | 1.142,44 | USD | Sin impuesto | 1 kit | https://www.kele.com/product/leak/leak-detection/liebert/lt460 | Un vendedor lo marca descontinuado |
| 28 | Himoinsa HYW-8 T5 insonorizado | 9.750,00 | EUR | Neto | 1 unidad | https://www.truck1.ie/buy/construction-machinery/generator-sets/himoinsa | Aviso de concesionario, 2026. La versión abierta cuesta 7.378 en SEV |
| 29 | APC NetShelter SX 24U AR3104 | 2.256,00 | USD | Sin impuesto | 1 unidad, MSRP 3.045 | https://www.publicsector.shidirect.com/product/18131183/APC-NetShelter-SX-Rack | |
