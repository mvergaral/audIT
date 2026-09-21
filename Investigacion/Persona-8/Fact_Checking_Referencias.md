# Fact-Checking de Fuentes y Referencias

## TI-12 · audIT (Empresa N.º 10) · Caso 10, Transportes Curimón S.A.

**Verificador:** Matías V. (Persona 8)
**Nivel de uso de IA declarado:** **Nivel 0.** Cada fila se cierra abriendo la fuente.
**Estado:** inventario levantado el 21-09-2026. **Verificación pendiente.**

> **Alcance.** 92 URL distintas en 46 dominios, más las referencias bibliográficas sin
> enlace. Este documento **no verifica**: clasifica y prioriza, para que la verificación
> humana no tenga que releer el corpus completo.

> [!CAUTION]
> **Qué exige el §6.1 de las Indicaciones.** «La producción de cifras, citas o
> referencias: estas se obtienen de la fuente, no del modelo». Y el §6: «Una referencia
> inexistente o una cifra sin respaldo **se evalúa como error grave**». Una referencia no
> queda validada porque suene plausible: queda validada cuando alguien abrió la página.

---

## 1. Prioridad 1 — Referencias con forma de fuente no verificada

> Todas son de Persona 4. **No están declaradas inexistentes**: están señaladas porque
> presentan alguno de los patrones que obligan a comprobarlas antes del despacho.

### 1.1 Dos autores distintos para la misma fuente

| Dónde | Qué dice |
| :--- | :--- |
| `Entregable_3`, ref. 8 | «**Intuitem Technologies.** (2026). *CISO Assistant Pro Enterprise Pricing and Packaging Guide*. Lyon / Cloud SaaS» |
| `Entregable_4`, ref. 6 | «**CISO Assistant / Norad Security.** (2026). *CISO Assistant Pro Cloud: GRC Metrics, SOC 2 Type II Certification and Commercial Cloud Pricing*» |

El mismo producto, dos editores. **«Norad Security» no aparece en ninguna otra parte del
corpus.** Una de las dos atribuciones es falsa; puede que ambas.

**Qué verificar:** quién publica CISO Assistant, en qué dominio, y si existe un documento
de precios con ese título. El repositorio que se cita
(`github.com/intuitem/ciso-assistant-community`) es comprobable en un minuto.

### 1.2 Precio citado de un proveedor que no publica precios

| | |
| :--- | :--- |
| **Persona 3 verificó** el 20-09-2026 que Vanta **no publica precios**: «No, solo por cotización» (`Subdocumento_P3`, §3.2, fila Vanta). Ese hallazgo es uno de los criterios ponderados de su matriz |
| **Persona 4 cita** «*Vanta Trust Management Platform **Pricing** and SOC 2 / ISO 27001 Automation Catalog*» (`E-3`, ref. 11) y consigna **USD 11.500 / año** (`E-3`, PR-08), atribuido a «Vanta Inc. (Cotización Oficial Cloud)» |

Dos capítulos del mismo informe afirman cosas opuestas sobre el mismo proveedor, y uno
de ellos lleva una cifra al modelo económico. El §5 es explícito: «*Cuando un proveedor
no publica precios, corresponde declararlo expresamente («solo por cotización») en lugar
de citar cifras de terceros sin verificar*».

**Qué verificar:** abrir `vanta.com/pricing`. Si no hay cifra publicada, la cifra se
retira o se reetiqueta como estimación propia declarada.

### 1.3 Títulos que describen una página, no un documento

| Ref. | Título citado | Problema |
| :---: | :--- | :--- |
| `E-3` 9 | «*Azure Key Vault Official Pricing Documentation for South America / Chile Central Region*» | Azure no publica un documento así; publica una calculadora. El §5 pide producto, moneda, región y fecha de consulta, no un título inventado para la página |
| `E-3` 6 | «**BSI Group Chile.** *Propuesta Económica y Tarifario Referencial […] ISO/IEC 27001:2022*» | Una propuesta económica es un documento privado. Si Persona 4 la tiene, se adjunta; si no, es «solo por cotización» |
| `E-3` 7 | «**SGS Chile Ltda.** *Esquema de Tarifas de Auditoría de Sistemas de Gestión*» | Igual que la anterior |
| `E-3` 5 | «**Colegio de Abogados de Chile A.G.** *Arancel Referencial de Honorarios Profesionales*» | El arancel referencial del Colegio de Abogados **fue derogado**. Verificar que exista una edición 2024/2025 antes de sostener la cifra |
| `E-4` 5 | «**ENISA.** (2022). *Cybersecurity and return on investment*» | ENISA publica sobre ROSI, pero hay que confirmar que ese título y ese año existan |

> **Correcta y verificable:** `E-4` ref. 4, Sonnenreich, Albanese & Stout (2006), *Return
> on Security Investment (ROSI)*, JRPIT 38(1). Es una fuente real y localizable. Sirve de
> patrón de cómo deben quedar las demás.

### 1.4 Una referencia que no es una referencia

`E-3`, ref. 12 funde **CMF + Banco Central + SII** en una sola entrada titulada
«*Indicadores Económicos Oficiales de la República de Chile al 16 de septiembre de
2026*», sin URL ni documento. Son tres organismos y tres cifras distintas (UF, USD, UTM);
necesitan tres entradas con su fecha de consulta.

---

## 2. Prioridad 1 — Marcador residual en la bibliografía

Las bibliografías de Persona 4 citan **rutas del sistema de archivos del repositorio**:

```
Archivo local: `Proyecto/Informe/repo/texto/FEP01_26_Bases_Administrativas_TFEP_01_2026_3.md`
Archivo local: `Proyecto/Informe/repo/texto/FEP03_10_26_Caso_10_Transporte_de_Carga_Bases_Tecnicas_del_Caso.md`
```

| Archivo | Línea |
| :--- | :---: |
| `Entregable_2_Modelo_TCO.md` | 376, 377 |
| `Entregable_3_Tabla_Precios_Metadatos.md` | 257, 258 |
| `Entregable_4_Analisis_Sensibilidad.md` | 199 |
| `Entregable_1_Matriz_Obligaciones.md` | 169 |
| `Manual_Operativo_Persona_4.md` | 410, 413 |

Es un marcador residual de trabajo (Comunicado 9, letra d). Las Bases se citan por su
código —FEP01.26, FEP03.10.26—, nunca por su ruta en el disco.

---

## 3. Prioridad 2 — Contradicción verificable entre capítulos

### 3.1 El dictamen de la Dirección del Trabajo sobre GPS tiene cuatro numeraciones

| Forma citada | Apariciones | Dónde |
| :--- | :---: | :--- |
| `Ord. N° 569/020` | 10 | P4, P5 |
| `Dictamen DT 569/2018` | 5 | P4, P6 |
| `Ord. 569/2024` | 1 | P5, `Subdocumento`, §59 |
| `Ord. N° 569/2018 **y** N° 569/020`, como si fueran **dos** dictámenes distintos | 1 | P4 |

La numeración de la Dirección del Trabajo es «Ord. N° 569/020»: número de oficio y
correlativo, **el año no va en el número**. Las formas `569/2018` y `569/2024` no
respetan ese formato.

Es una línea de aporte propio del grupo —la doctrina laboral sobre monitoreo GPS de
conductores— y sostiene el trato diferenciado de los 196 choferes de planta. Que aparezca
con cuatro numeraciones es verificable en segundos contra `dt.gob.cl`.

**Qué verificar:** el número y el año correctos en el buscador de dictámenes de la DT, y
unificarlos. Igual para `Ord. 2328/130`, que aparece 8 veces sin variantes pero tampoco
fue verificado.

### 3.2 ISO/IEC 27001:2022 enlazada a la ficha de otra norma

`Subdocumento_P3`, tabla de referencias, filas 6 y 7: **las dos** apuntan a
`iso.org/standard/27701`. La 27001 tiene su propia ficha.

---

## 4. Prioridad 2 — Capítulo sin bibliografía

**Persona 5 no tiene lista de referencias.** El capítulo cita a lo largo del texto la Ley
21.719 con sus artículos, la Ley 21.663, el Art. 25 bis del Código del Trabajo, el
Dictamen 569, la **Ley N° 21.377 «No Chat»**, el **D.S. N° 298**, la **Ley 25.326**
argentina y las Cláusulas Contractuales Tipo — **sin una sola URL ni entrada
bibliográfica**.

Dos de esas normas no aparecen en ningún otro capítulo y, por tanto, nadie más las
verificó: la **Ley 21.377** y el **D.S. 298**. Van como filas nuevas de la tabla de
vigencias.

---

## 5. Prioridad 3 — Admisibilidad de las fuentes (§5)

El §5 clasifica las fuentes en tres categorías. El corpus usa dominios de las tres:

| Categoría | Dominios presentes | Situación |
| :--- | :--- | :--- |
| **Preferentes** | `bcn.cl`, `diariooficial.interior.gob.cl`, `eur-lex.europa.eu`, `iso.org`, `anci.gob.cl`, `cmfchile.cl`, `senado.cl`, `camara.cl`, `sii.cl`, `bcentral.cl` | Correctas. Son la mayoría |
| **Admisibles con declaración expresa** | `dlapiperdataprotection.com`, `fpf.org`, `carey.cl`, `anguitaosorio.cl`, `alejandrobarros.com`, `roberthalf.cl`, `michaelpage.cl` | **Persona 2 las declara correctamente** con su marca `[S]`. Donde Persona 4 las usa para sostener una cifra, falta la declaración de muestra y metodología que pide el §5 |
| **No admisibles como primarias** | `vlex.cl`, `lexlatin.com`, `diarioconstitucional.cl`, `iura.cl`, `retailfinanciero.org` | Agregadores. Solo pueden acompañar a la fuente original, nunca sustituirla |

**Qué verificar:** que ninguna afirmación dependa **únicamente** de un dominio de la
tercera fila. Persona 2 ya lo hizo en su capítulo; falta el de Persona 4.

---

## 6. URL de dominio desnudo usadas como fuente de una cifra

Diecisiete referencias apuntan a la raíz del sitio (`https://www.roberthalf.cl`,
`https://azure.microsoft.com`, `https://www.chubb.com/cl-es/`) y no a la página del dato.
Un dominio no respalda una cifra: el §5 exige producto, moneda, región y fecha de
consulta, y eso vive en una página concreta.

| Archivo | Líneas |
| :--- | :--- |
| `Entregable_3_Tabla_Precios_Metadatos.md` | 40-45 |
| `Manual_Operativo_Persona_4.md` | 337-341, 419-424 |

---

## 7. Orden de trabajo sugerido

| # | Qué | Tiempo estimado | Por qué primero |
| :-: | :--- | :---: | :--- |
| 1 | Las 6 referencias de la §1 de este documento | 20 min | Una referencia inexistente es «error grave» por el §6 |
| 2 | `vanta.com/pricing` y la cifra de USD 11.500 | 5 min | Contradice a un capítulo del propio informe |
| 3 | El dictamen 569 en `dt.gob.cl` | 10 min | Es la línea de aporte propio del grupo |
| 4 | Las rutas `Archivo local:` | 5 min | Marcador residual, eliminación directa |
| 5 | Ley 21.377 y D.S. 298 (P5) | 10 min | Nadie más las verificó |
| 6 | Las 17 URL de dominio desnudo | 30 min | Cada una sostiene una cifra del modelo económico |
| 7 | El enlace de ISO 27001 | 1 min | |

---

## 8. Declaración de cierre

> Completar al terminar:

Se verificaron ____ de 92 URL y ____ de ____ referencias bibliográficas, entre el ____ y
el ____ de septiembre de 2026. Las referencias que no pudieron confirmarse en su fuente
fueron **retiradas del informe**, no reetiquetadas. Las cifras cuyo respaldo resultó ser
un dominio sin página específica fueron **declaradas como estimación propia** o retiradas,
conforme al §5 de las Indicaciones.

**Firma del verificador:** ______________________  **Fecha:** ____________
