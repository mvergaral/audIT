# Aviso de D4 a D1: audIT EdgeHub y el Subdocumento 1

07-10-2026. El Informe 2 se entrega el 12-10.

## Qué decidió D4

La observación 96 de la revisión del Informe 1 dice que «el producto propio audIT EdgeHub se invoca sin
definirlo en ningún subdocumento». D4 la responde igual que la tabla del equipo: audIT EdgeHub es el
software de borde de audIT y se define en el Subdocumento 1. La innovación 5 (13.5) lo nombra como el
software del equipo a bordo que especifica el Subdocumento 4 en 4.2.2 (decisión D4-86).

Para cerrar la marca que quedó en 13.5 necesitamos que nos confirmen en qué sección del S1 queda definido.
En su borrador está en 1.1.3.

## Lo que choca entre su S1 y el S4

Revisamos `Informe-2/d1/subdocumento_01_empresa_adaptado.md` (versión del 04-10). Hay seis puntos que no
coinciden con el S4 ni con el Caso. El Comunicado 10, sección 7.1 c), toma las contradicciones entre
subdocumentos como indicio de IA, y la sanción es el subdocumento completo en cero. Afecta al S1 y al S4.

| Línea del borrador | Qué dice el S1 | Qué dicen el S4 y las bases |
|---|---|---|
| 314 | Pinzas CANclick en «87 camiones propios sin telemetría previa» y en 34 subcontratados, 121 pasarelas nuevas | Los 148 camiones propios ya tienen dispositivo. Solo 34 subcontratados no tienen ninguno (Caso, numeral 2.2, p.6, y numeral 14.1, p.29: «340 de 374»). audIT instala su equipo en los 148 propios y en esos 34, 182 en total (D4-01) |
| 89, 314, 338 y 346 | Acopladores inductivos CANclick | El S4 usa el lector sin contacto CANCrocodile de Technoton conectado al CAN del equipo (D4-43) |
| 52 a 58 | EdgeHub como pasarela con memoria eMMC de 8 GB | El equipo a bordo es el iWave G26I. Los 8 GB son su configuración mínima, derivada de un uso de unos 2,4 GB (S4 4.2.2, D4-24 y D4-34). EdgeHub tendría que quedar como el software que corre en el G26I |
| 58 | Unos 40 MB en 288 horas | El S4 calcula 38,4 MB para el búfer de 288 horas (3,2 MB por cada 72 h con fotos, por 4 y por 3 de seguridad) |
| 314 | «192 integrados por API» | El Caso dice que hay «accesos de solo consulta en dos de ellos» y que «una de las tres plataformas ni siquiera permite exportar» (p.34). El S4 los trata como integración de datos, sin intervenir los equipos (restricción 3) |
| 90, 314, 339 y 346 | Sondas PT100 en las 44 ramplas de frío | La innovación 3 (13.3, D4-55) mide la temperatura de los semirremolques refrigerados con balizas Bluetooth. Si el S1 pone otro sensor, son dos soluciones distintas para lo mismo |

También conviene usar un solo nombre. El borrador dice «audIT EdgeHub v2.4 Enterprise», «audIT EdgeHub
v2.4 Enterprise Embedded», «audIT EdgeHub v2.4» y «EdgeHub». El Comunicado 10 pide terminología idéntica
en toda la oferta. En el S13 usamos «audIT EdgeHub».

## Lo de D1 que sigue abierto en los documentos de D4

- 13.5: la sección del S1 que define audIT EdgeHub.
- 13.5 y ficha 5 del T-19: la partida del flujo de caja de la Oferta Económica donde se refleja la
  innovación 5 (observación 97).
- Tabla del Art. 46, fila 97: la misma partida.

El texto de 13.5 que está hoy en el formato es el del Informe 1, sin lo que sancionó la revisión. Su
borrador `formulario_t19_tipo5_innovacion.md` (30-09) también usa EdgeHub. Si van a reemplazar 13.5 o la
ficha 5 con ese borrador, avísennos para dejar la innovación alineada con el S4.

## Cambios del 05-10 en las partes de D4 que hay que revisar

El commit `f59f7bd` (05-10) cambió archivos de la carpeta de D4, y esos cambios pasaron al formato del
equipo en `recursos/Formato-Oferta-audIT/`, que es el que se entrega. Varios contradicen el Caso o dicen
que algo está en la oferta cuando no está. El Comunicado 10 (7.1 c y d) trata las dos cosas como indicio
de IA, con el subdocumento completo en cero.

| Dónde (en `recursos/`) | Qué dice | Problema |
|---|---|---|
| S4, `contenido.tex` línea 736 | Los 192 camiones de terceros «se integran mediante conectores y adaptadores API REST/Webhook» | El Caso dice que hay «accesos de solo consulta en dos de ellos» y que una plataforma «ni siquiera permite exportar» (p.34) |
| S4, líneas 613 y 1160 | Concurrencia de 380 sesiones | No sale del Caso. D4 usaba 350, derivado en el Informe 1 |
| S4, línea 1279 | «Memoria de cálculo… según estándares ASHRAE TC 9.9 y TIA» | Esas normas no están en Referencias ni se usaron en el cálculo |
| S13, línea 303 | Las balizas «fueron evaluadas en el modelado de amenazas STRIDE de la sección 4.1» | El S4 no tiene ese modelado ni menciona las balizas. Es una referencia a contenido inexistente |
| S13, línea 261 | Balizas en los paquetes EDT 3.4 y 4.4 | En el T-14 de D2, el 3.4 es la sala de San Bernardo. D2 asigna la innovación 3 a 12.3, 4.2 y 5.2 |
| Art. 46, filas 53 a 63, 68, 75, 76, 80, 89, 91 y 97 | «Se incorpora: [texto del marcador]» | Afirma que se agregó contenido que no está en el documento |
| Declaraciones de IA del S4 y del S13 | Secciones de D4 bajadas de «Alto» a «Medio», con la revisión firmada por un integrante de D1 con su nombre completo | El texto lo redactó la IA, así que «Medio» declara de menos. Además el plan del equipo prohíbe nombres reales |

D4 dejó corregido todo esto en su propio formato (`Formato-Oferta-audIT/` local), con las innovaciones 1
y 4 de D2, la innovación 5 de D1 (con su madurez TRL 6 y su partida del flujo de caja) y los códigos EDT
de D2. Para la entrega del 12-10 hay que decidir en conjunto qué versión se lleva a `recursos/`.
