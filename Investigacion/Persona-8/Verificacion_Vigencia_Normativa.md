# Verificación Documentada del Estado de Vigencia de las Normas Citadas

## TI-12 · audIT (Empresa N.º 10) · Caso 10, Transportes Curimón S.A.

**Verificador:** Matías V. (Persona 8)
**Nivel de uso de IA declarado:** **Nivel 0.** Cada fila se abre y se lee en su fuente
oficial. Ninguna celda se completa con conocimiento de modelo ni con fuente secundaria.
**Fecha de corte del informe:** 20 de septiembre de 2026 (acordada con Persona 1, DC-08).

> **Por qué este documento.** La ficha TI-12 exige, como entregable propio y nombrado,
> la «verificación documentada del estado de vigencia de cada norma citada, con la fuente
> oficial y la fecha de consulta». El punto 5 de las Indicaciones añade que **una cifra o
> una referencia sin fecha no se considera válida**.

---

## Cómo se completa

1. **Abrir la URL de la columna «Fuente oficial»** y leer el encabezado de vigencia. No
   vale un buscador, un blog ni un agregador: el punto 5 los declara no admisibles como
   fuente primaria.
2. **Anotar la fecha en que se abrió**, en formato `DD-MM-AAAA`. Es la fecha de consulta,
   no la de hoy por defecto.
3. **Marcar el estado** con uno de los cinco valores de la leyenda.
4. Si la fuente **no permite confirmar** el dato, dejar `[NV]` y escribir en
   observaciones qué se buscó y por qué no se encontró. Una ausencia declarada vale;
   una afirmación sin respaldo, no.

### Leyenda de estados

| Marca | Significado |
| :---: | :--- |
| **V** | Vigente y plenamente exigible a la fecha de corte |
| **VL** | Publicada pero en *vacatio legis*: aún no exigible. Indicar la fecha en que lo será |
| **VP** | Vigencia parcial o escalonada. Indicar qué tramo rige y desde cuándo |
| **T** | En tramitación. No es norma todavía |
| **D** | Derogada o sustituida. Indicar por qué norma |
| **[NV]** | No verificado. Declarado como tal, con constancia de la búsqueda |

---

## 1. Normativa chilena

*Fuentes oficiales: Biblioteca del Congreso Nacional (`bcn.cl/leychile`) y Diario Oficial
(`diariooficial.interior.gob.cl`). Persona 2 dejó fijados los `idNorma` en su*
`Entregable_6_Declaracion_Exhaustividad_Bitacora.md`*, lo que evita la búsqueda por texto.*

| # | Norma | Materia | Estado | Fecha D.O. | Fuente oficial (URL) | Fecha consulta | Observaciones |
| :-: | :--- | :--- | :---: | :---: | :--- | :---: | :--- |
| 1 | **Ley N° 21.719** | Protección y tratamiento de datos personales | | | `bcn.cl/leychile/navegar?idNorma=1209272` | | Verificar el **Art. primero transitorio**. P2 verificó vigencia el **01-12-2026**, no el 13-12-2026 (H-10) |
| 2 | **Ley N° 21.663** | Marco de ciberseguridad (ANCI, CSIRT) | | | `bcn.cl/leychile/navegar?idNorma=1202434` | | Vigencia **escalonada**: tramo general 01-01-2025, tramo diferido (Arts. 5, 8, 9 y Título VII) 01-03-2025. Marcar **VP** |
| 3 | **D.S. N° 295/2024**, Min. Interior | Reglamento de reporte de incidentes (3/72/15) | | | | | Confirmar que los plazos 3 h / 72 h / 7 d / 15 d están **en el reglamento** y no en la ley. P2 declaró este punto `[NV]` |
| 4 | **Ley N° 19.628** | Protección de la vida privada | | | | | Reformada por la 21.719. Precisar qué rige **hoy** y qué queda sustituido desde el 01-12-2026 |
| 5 | **Ley N° 21.180** | Transformación digital del Estado | | | | | Exigida por la ficha TI-12 |
| 6 | **Ley N° 20.285** | Acceso a la información pública | | | | | `[NV]` en P2. Fecha D.O. sin confirmar |
| 7 | **Ley N° 21.096** | Consagra el derecho a la protección de datos personales | | | | | `[NV]` en P2 |
| 8 | **Ley N° 21.459** | Delitos informáticos (Convenio de Budapest) | | | | | `[NV]` en P2. Citada por P6 en el cuestionario |
| 9 | **Ley N° 21.521** | Fintech | | | | | `[NV]` en P2 |
| 10 | **Ley N° 21.680** | Registro de Deuda Consolidada | | | | | `[NV]` en P2. Falta además el número de NCG que la operativiza |
| 11 | **Ley N° 21.659** | — | | | | | `[NV]` en P2 |
| 12 | **Instructivo Presidencial N° 8** | Ciberseguridad | | | | | `[NV]` en P2 |
| 13 | **Reglamento de Ciberseguridad de la Defensa** | — | | | | | `[NV]` en P2 |
| 14 | **D.S. N° 285/2024 o N° 295/2024** | Calificación de OIV | | | | | **Errata declarada.** P2 (`Entregable_5:127`) señala que la fila 18 cita el D.S. 285/2024, número que no aparece en ninguna otra parte. Verificar cuál es, o **retirar la cita** |
| 15 | **Dictamen DT Ord. N° 569/2018** y **N° 569/020** | Monitoreo GPS de conductores | | | `dt.gob.cl` | | Línea de aporte propio del grupo. Confirmar numeración exacta: aparecen dos formas distintas en el corpus |
| 16 | **Art. 25 bis, Código del Trabajo** | Jornada de choferes | | | | | Base del trato diferenciado de los 196 choferes de planta (P5) |

---

## 2. Organismos

| # | Organismo | Estado a la fecha de corte | Fuente oficial (URL) | Fecha consulta | Observaciones |
| :-: | :--- | :--- | :--- | :---: | :--- |
| 17 | **Agencia de Protección de Datos Personales** | | | | P2 sostiene que **no está constituida** al 20-09-2026. Confirmar si hubo designación del Consejo |
| 18 | **ANCI** | | `anci.gob.cl` | | Verificar si Curimón figura en la nómina de OIV. P2 lo dejó `[NV]` |
| 19 | **CSIRT Nacional** | | | | Confirmar el canal formal de notificación vigente |
| 20 | **Consejo para la Transparencia** | | | | Citado por P2 como acervo comparable |

---

## 3. Normativa internacional

*Fuente oficial: EUR-Lex (`eur-lex.europa.eu`). Persona 3 descargó los textos CELEX y
están en* `Persona-3/Entregables/`*, lo que permite verificar sin conexión.*

| # | Norma | Identificador | Estado | Fuente oficial (URL) | Fecha consulta | Observaciones |
| :-: | :--- | :--- | :---: | :--- | :---: | :--- |
| 21 | **RGPD** | Reglamento (UE) 2016/679 | | `eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:32016R0679` | | Aplicable desde el 25-05-2018 según P3 |
| 22 | **Directiva NIS2** | Directiva (UE) 2022/2555 | | `…CELEX:32022L2555` | | Plazo de transposición vencido el 17-10-2024 |
| 23 | **Reglamento de IA** | Reglamento (UE) 2024/1689 | | `…CELEX:32024R1689` | | Aplicación escalonada. Marcar **VP** e indicar los tramos |
| 24 | **Ómnibus digital sobre IA** | Reglamento (UE) 2026/1744 | | `…CELEX:32026R1744` | | Modifica al anterior. **Norma reciente: verificar con especial cuidado** |
| 25 | **Reglamento de Ciberresiliencia** | Reglamento (UE) 2024/2847 | | `…CELEX:32024R2847` | | Reporte del art. 14 desde el 11-09-2026 según P3 |
| 26 | **Ley 25.326 (Argentina)** | Protección de datos personales | | InfoLEG | | Tramo internacional a Mendoza (P5) |
| 27 | **Convenio 108+ (CETS 223)** | Consejo de Europa | | `coe.int` → **Treaty Office** | | **P2 no pudo verificar si Chile adhirió.** Si no consta, redactar «no consta que Chile haya adherido», nunca «Chile no adhirió» |

---

## 4. Normas técnicas

*Fuente oficial: `iso.org` y `nist.gov`. Para las ISO basta la ficha pública de la norma;
no se requiere el texto, que es de pago.*

| # | Norma | Estado | Fuente oficial (URL) | Fecha consulta | Observaciones |
| :-: | :--- | :---: | :--- | :---: | :--- |
| 28 | **ISO/IEC 27001:2022** | | `iso.org/standard/27001` | | **P3 la enlazó a `/standard/27701`, que es otra norma.** Corregir el enlace en su tabla de referencias |
| 29 | **ISO/IEC 27701** | | `iso.org/standard/27701` | | P3 la cita como **:2025**. Confirmar el año de edición vigente |
| 30 | **ISO/IEC 42001:2023** | | `iso.org/standard/42001` | | |
| 31 | **NIST Cybersecurity Framework 2.0** | | `nist.gov` (NIST CSWP 29) | | Verificar el DOI |

---

## 5. Precios y cotizaciones

*El punto 5 de las Indicaciones exige que toda cifra indique **producto, moneda, región,
fecha de consulta** y si es precio de lista o cotización; y que cuando el proveedor no
publica precios se declare «solo por cotización» en lugar de citar cifras de terceros.*

| # | Ítem | Proveedor | Cifra declarada en el informe | ¿Precio de lista o cotización? | URL oficial | Fecha consulta | Verificado |
| :-: | :--- | :--- | :--- | :---: | :--- | :---: | :---: |
| 32 | Key Vault Premium | Microsoft Azure | USD 1 / clave / mes | | `azure.microsoft.com/pricing/details/key-vault/` | | **Tres cifras distintas en el corpus (H-06)** |
| 33 | Managed HSM B1 | Microsoft Azure | USD 3,20 / h | | | | Alternativa descartada por P4 pero especificada por P5 (H-07) |
| 34 | CISO Assistant Pro | Intuitem | EUR 2.400 / año | | | | **Herramienta no evaluada por P3 (H-03)** |
| 35 | Microsoft Purview | Microsoft | Por plan de licenciamiento | | `azure.microsoft.com/pricing/details/purview/` | | Recomendada por P3 |
| 36 | Auditoría ISO 27001 | BSI / SGS Chile | 387,5 UF | | | | ¿Cotización formal o estimación? |
| 37 | Póliza de ciberseguridad | Chubb | 90 UF / año | | | | |
| 38 | **Presupuesto total de la licitación** | — | «~215.000 UF» | | — | | **No localizado en FEP01, FEP02 ni FEP03 (H-06).** De esta cifra se deriva el 3,9 % de proporcionalidad |

---

## 6. Declaración de cierre

> Completar al terminar el barrido:

Se verificaron ____ de 38 filas contra su fuente oficial entre el ____ y el ____ de
septiembre de 2026. Quedan ____ filas marcadas `[NV]`, declaradas como tales con
constancia de la búsqueda realizada. Las citas correspondientes a filas `[NV]` fueron
**retiradas del informe o reformuladas sin numeral**, según lo acordado con Persona 1.

**Firma del verificador:** ______________________  **Fecha:** ____________
