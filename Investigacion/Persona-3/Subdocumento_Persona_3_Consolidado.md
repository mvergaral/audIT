# Subdocumento Persona 3 · Marco internacional, normas técnicas y herramientas de apoyo


## 1. Marco internacional aplicable al proyecto

### 1.1 Apertura

El proyecto de Transportes Curimón S.A. se ejecuta en Chile, pero su cadena de obligaciones no termina en la
frontera. Tres situaciones lo internacionalizan. La primera es la ruta Antofagasta a Puerto Montt con cruce a
Mendoza, que mueve datos de conductores y de carga a un tercer país. La segunda es la elección de Azure Chile
Central como región primaria y Azure East US 2 como réplica, que traslada copias fuera del territorio nacional.
La tercera es que el mandante exige controles de las familias ISO/IEC 27001 y 27002 en el requisito RT-11.05,
es decir, importa un estándar internacional al pliego mismo de la licitación.

De ahí que el marco europeo no aparezca aquí como referencia académica sino por dos vías concretas. Una es
directa, cuando la norma europea se aplica por sí misma. La otra es indirecta, cuando la norma europea opera
como patrón de diseño de la regulación chilena, como ocurre con la Ley 21.719 respecto del RGPD.

### 1.2 Tabla de vigencias


| Norma | Identificador | Estado a septiembre de 2026 | Fecha crítica siguiente | Aplicabilidad a Curimón |
| :--- | :--- | :--- | :--- | :--- |
| RGPD | Reglamento (UE) 2016/679 | Aplicable desde el 25-05-2018 | Sin hito pendiente | Indirecta. Modelo de la Ley 21.719 y exigencia contractual probable de clientes con matriz europea |
| Directiva NIS2 | Directiva (UE) 2022/2555 | Plazo de transposición vencido el 17-10-2024. Varios Estados siguen en procedimiento de infracción | Depende de cada Estado miembro | Indirecta. Referente del diseño de la Ley 21.663 y de su régimen de reporte |
| Reglamento de IA | Reglamento (UE) 2024/1689, modificado por el Reglamento (UE) 2026/1744 | Prohibiciones y alfabetización desde el 02-02-2025. Transparencia del art. 50 desde el 02-08-2026. Alto riesgo del Anexo III aplazado | 02-12-2027 (Anexo III) y 02-08-2028 (Anexo I) | Indirecta hoy. Relevante si el modelo predictivo de fatiga se ofreciera en la UE |
| Reglamento de Ciberresiliencia | Reglamento (UE) 2024/2847 | Obligaciones de reporte del art. 14 aplicables desde el 11-09-2026 | 11-12-2027 aplicación completa | Indirecta. Afecta a los fabricantes de los componentes telemáticos que Curimón incorpore |


### 1.3 Lectura comparada Chile frente a la Unión Europea

| Dimensión | Unión Europea | Chile | Consecuencia para el proyecto |
| :--- | :--- | :--- | :--- |
| Plazo de notificación de brechas | 72 horas al supervisor (RGPD art. 33) | «Sin dilaciones indebidas» (Ley 21.719, art. 14 sexies) | El informe no puede afirmar que Chile exige 72 horas. Las Bases sí fijan 2 h y 24 h al cliente en RT-11.18 y RT-11.19, que es una obligación contractual, no legal |
| Decisiones automatizadas | RGPD art. 22 | Ley 21.719, art. 8 bis | El bloqueo automático del despacho cae en este supuesto y arrastra EIPD del art. 15 ter |
| Reporte de incidentes de ciberseguridad | NIS2, 24 h de alerta temprana | Ley 21.663 y su reglamento | Curimón queda obligado por ser servicio esencial de transporte terrestre aunque no figure como OIV |
| Transferencia internacional | Capítulo V del RGPD, decisiones de adecuación y cláusulas tipo | Ley 21.719, arts. 27 y 28 | La Agencia aún no publica cláusulas modelo. La réplica en East US 2 y el cruce a Mendoza quedan sin instrumento estándar disponible |


#### 1.4 Análisis de la asimetría normativa

 La falta de cláusulas del modelo chileno crea un riesgo critico a la continuidad operativa de Curimon, lo que puede resultar en plazos extendidos ya que los contratos ya firmados con el proveedor de nube y con los transportistas externos deben rehacerse,aumento de costo al tener que redactar clausulas propias y someterlas a revisión legal y problemas de arquitectura al tener plataformas internacionales y nacionales como Azure Chile Central.
 Mientras no existan cláusulas modelo nacionales, la propuesta incorpora cláusulas contractuales basadas en el capítulo V del RGPD como diseño de preferencia, declarando expresamente que se trata de un instrumento provisorio, y reserva en el presupuesto las horas de revisión legal para su reemplazo.

---

## 2. Normas técnicas certificables

### 2.1 Las cuatro de la ficha

| Norma | Objeto | Certificable | Nota de vigencia |
| :--- | :--- | :---: | :--- |
| ISO/IEC 27001:2022 | Sistema de gestión de seguridad de la información | Sí | El plazo de transición desde la edición 2013 venció en octubre de 2025. Toda certificación vigente está en la edición 2022 |
| ISO/IEC 27701:2025 | Sistema de gestión de privacidad (PIMS) | Sí | **Cambio estructural.** La edición 2025 la convierte en norma autónoma. Ya no requiere un SGSI 27001 previo como sí exigía la edición 2019 |
| ISO/IEC 42001:2023 | Sistema de gestión de inteligencia artificial | Sí | Vigente. Aplicable al modelo predictivo de fatiga y al bloqueo automático de despacho |
| NIST CSF 2.0 | Marco de gestión de ciberseguridad | No certificable | Publicado en 2024. Incorpora la función Govern. Se usa como marco de madurez, no como sello |

**Por qué el cambio de la 27701 importa al costeo.** Bajo la edición 2019 la ruta de privacidad certificable
obligaba a pagar antes una certificación 27001 completa. Bajo la edición 2025 la privacidad puede certificarse
por separado. Eso abre una alternativa de secuenciación que el modelo de costos de P4 debe poder evaluar, en
lugar de asumir una sola ruta. La consecuencia práctica es que la partida de certificación deja de ser un
número único y pasa a ser una decisión de camino.

### 2.2 Dos marcos adicionales de aporte propio

La ficha cierra su lista con «y otros que el grupo debe identificar». El punto 4 de las Indicaciones obliga a
agregar al menos dos alternativas y a justificar qué aportan. El grupo incorpora las siguientes.

**a) Ley argentina 25.326 de Protección de los Datos Personales.**
Justificación de pertinencia: el Caso 10 contempla cruce fronterizo a Mendoza. Ningún otro marco de la ficha
cubre el tratamiento de datos que ocurre del lado argentino de la operación. Es el único marco adicional que
es obligatorio y no voluntario para este caso concreto.

**b) SOC 2 Type II (AICPA, TSC 2017 con revisiones posteriores).**
Justificación de pertinencia: es el informe de aseguramiento que con más frecuencia exigen los clientes
corporativos en contratos de servicios tecnológicos. Curimón atiende a 84 empresas cliente. A diferencia de ISO
27001, no certifica un sistema de gestión sino la operación efectiva de controles durante un periodo observado,
lo que lo hace complementario y no sustituto.


#### Justificación del aporte
El grupo evaluó cinco marcos adicionales y decidió incorporar dos. La Ley argentina 25.326 entra porque el Caso 10 contempla operación con cruce a Mendoza, y ninguno de los marcos de la ficha alcanza el tratamiento de datos que ocurre del lado argentino de esa ruta. Es el único marco adicional que resulta obligatorio y no voluntario para Curimón. El informe SOC 2 Type II entra por una razón distinta. Curimón atiende a 84 empresas cliente, y el aseguramiento que esos clientes exigen en contratos de servicios no es una certificación de sistema de gestión sino un informe sobre la operación efectiva de controles durante un periodo. Si el grupo se hubiera limitado a la ficha, el informe habría descrito un proyecto sin jurisdicción argentina y sin el mecanismo contractual que sus propios clientes le van a pedir.

### 2.3 Costo de certificación

Ninguna de las certificadoras que operan en Chile publica precio de lista para auditoría de certificación. El
régimen aplicable es **«solo por cotización»** conforme al punto 5 de las Indicaciones, y así debe declararse.
Lo que sí se documenta es la estructura del costo, que tiene cuatro componentes separables.

| Componente | Naturaleza | Fuente a usar | Régimen |
| :--- | :--- | :--- | :--- |
| Compra del texto de la norma | Precio publicado | Tienda oficial de ISO o del INN | Precio de lista CHF 155.00 (181,021.40 Peso chileno)|
| Consultoría de implantación | Horas profesionales | Formulario E-26, perfil a declarar por P4 | Rango UF/h del E-26 |
| Auditoría de certificación (etapas 1 y 2) | Servicio de organismo acreditado | Cotización a BSI, Bureau Veritas, SGS, AENOR Chile, TÜV | Solo por cotización |
| Mantención (vigilancia anual y recertificación a 3 años) | Servicio recurrente | Misma cotización | Solo por cotización |



---

## 3. Comparativa de herramientas GRC y de apoyo al cumplimiento

### 3.1 Universo evaluado

Ocho plataformas analizadas y una descartada con declaración expresa. Las seis primeras provienen de la
lista de la ficha. Las dos últimas son aporte propio del grupo.

| # | Herramienta | Categoría funcional | Modelo de despliegue | Origen |
| :-: | :--- | :--- | :--- | :--- |
| 1 | OneTrust | Privacidad, consentimiento y GRC integrado | SaaS | Ficha |
| 2 | Vanta | Automatización de cumplimiento y evidencia continua | SaaS | Ficha |
| 3 | Drata | Automatización de cumplimiento y evidencia continua | SaaS | Ficha |
| 4 | BigID | Descubrimiento y clasificación de datos personales | SaaS e instalable | Ficha |
| 5 | Microsoft Purview Compliance Manager | Cumplimiento dentro del ecosistema Microsoft 365 y Azure | SaaS | Ficha |
| 6 | Securiti.ai | Gobierno de datos y privacidad con foco en IA | SaaS | Ficha |
| 7 | **Osano** | Gestión de consentimiento y privacidad para organizaciones medianas | SaaS | **Aporte propio** |
| 8 | **Eramba** | GRC de código abierto, autoalojable | Autoalojado | **Aporte propio** |


**Por qué estas dos de aporte propio.** Osano cubre un tramo de mercado que las seis de la ficha no atienden,
el de la organización mediana que necesita consentimiento y no una suite completa. Eramba introduce la única
alternativa autoalojada del conjunto, lo que permite que la comparación incluya el eje construir frente a
comprar y no solo la elección entre proveedores SaaS. Sin ella, la comparativa habría tenido un sesgo de
categoría.

### 3.2 Ficha de datos por herramienta (columnas objetivas)



| Herramienta | Cubre Ley 21.719 con plantilla propia | Cubre ISO 27001 / 27701 / 42001 | Descubrimiento de datos | Consentimiento | Precio publicado | URL oficial consultada | Fecha consulta |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- | :---: |
| OneTrust | No | Sí | Sí | Sí | No, solo por cotización  | https://www.onetrust.com/pricing/#accordion-b4d6a3b6f6-accordionitem_2 | 20-09-2026 |
| Vanta | No | Sí | Parcial | No | No, solo por cotización | https://www.vanta.com/pricing | 20-09-2026 |
| Drata | No | Sí | Parcial | No | No, solo por cotización (Demo) | https://drata.com/contact-sales | 20-09-2026 |
| BigID | No | Sí | Sí | Parcial | No, solo por cotización (Demo) | https://home.bigid.com/demo | 20-09-2026 |
| Microsoft Purview | No | Sí | Sí | No | Sí, por plan de licenciamiento | https://azure.microsoft.com/es-mx/pricing/details/purview/ | 20-09-2026 |
| Securiti.ai | No | Sí | Sí | Sí | No, solo por cotización (Demo) | https://securiti.ai/request-demo/ | 20-09-2026 |
| Osano | No | Sí | Parcial | Sí | No, solo por cotización (Demo) | https://www.osano.com/plans | 20-09-2026 |
| Eramba | No | Sí | No | No | Sí, edición comunitaria y suscripción | https://www.eramba.org/get-started-grc | 20-09-2026 |



### 3.3 Criterios, ponderación y análisis



#### 3.3.1 Criterios ponderados (los que sí distinguen)
 
| Criterio | Peso | Por qué pesa lo que pesa | De dónde sale el dato |
| :--- | :---: | :--- | :--- |
| Descubrimiento de datos personales | 25 % | Curimón no tiene inventario de tratamientos. Sin esto, el registro de actividades se levanta a mano sobre la base operativa completa | Columna «Descubrimiento de datos» |
| Gestión de consentimiento | 20 % | 258 conductores externos y 148 transportistas generan solicitudes de acceso y supresión que alguien debe resolver en plazo | Columna «Consentimiento» |
| Transparencia del precio | 25 % | El punto 5 de las Indicaciones impide llevar al flujo de caja una cifra no verificable. Solo 2 de 8 publican precio real | Columna «Precio publicado» |
| Encaje con la arquitectura comprometida | 20 % | La propuesta ya fijó Azure y Key Vault con HSM en el Informe 1. Una herramienta nativa del mismo ecosistema reduce costo de integración | Modelo de despliegue y región declarada por el proveedor |
| Esfuerzo de operación | 10 % | La única autoalojada del conjunto es Eramba. Ahí el esfuerzo de operación es el criterio que decide si conviene frente a comprar SaaS | Inferido del modelo de despliegue; no figura como columna en la ficha del §3.2 |
 
Suma: 100 %. La ponderación es una decisión del equipo y admite revisión: si se asume que toda contratación
pasará igualmente por cotización, el 25 % de transparencia del precio pierde poder discriminante y se traslada
al encaje con la arquitectura, que es el criterio de mayor efecto económico en este caso.

#### 3.3.2 Matriz de puntuación
 
Escala 1 a 5. Regla de conversión: Sí = 5, Parcial o «Demo» = 3, No = 1. Precio: publicado = 5, solo
cotización = 1 (sin matices, porque el punto 5 trata ambos casos igual: si no hay precio de lista, no hay
precio de lista).
 
| Herramienta | Descubr. 25 % | Consent. 20 % | Precio 25 % | Encaje Azure 20 % | Operación 10 % | **Total ponderado** |
| :--- | :-: | :-: | :-: | :-: | :-: | :-: |
| OneTrust | 5 | 5 | 1 | 1 | 3 | **3,05** |
| Vanta | 3 | 1 | 1 | 1 | 3 | **1,75** |
| Drata | 3 | 1 | 1 | 1 | 3 | **1,75** |
| BigID | 5 | 3 | 1 | 1 | 3 | **2,55** |
| **Microsoft Purview** | 5 | 1 | **5** | **5** | 4 | **3,70** |
| Securiti.ai | 5 | 5 | 1 | 1 | 3 | **3,05** |
| Osano | 3 | 5 | 1 | 1 | 4 | **2,65** |
| Eramba | 1 | 1 | **5** | 1 | 1 | **1,60** |

---

## 4. Cierre del subdocumento

En este capítulo se crean tres puntos que se deben abordar. La licencia anual de la herramienta recomendada, las horas de revisión legal para las cláusulas de transferencia internacional, y la auditoría de certificación ISO/IEC 27001:2022 con su mantención a tres años. Las dos últimas se rigen por cotización, de modo que ingresan al flujo de caja como supuesto declarado.

---

## Referencias que P3 aporta a la bibliografía común

Formato APA 7. P3 entrega a P1 la entrada completa de cada fuente que cite, con DOI cuando exista.

| # | Fuente | Tipo | Estado |
| :-: | :--- | :--- | :--- |
| 1 | Reglamento (UE) 2016/679 (RGPD), EUR-Lex | Texto legal oficial | https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:32016R0679 enlace CELEX |
| 2 | Directiva (UE) 2022/2555 (NIS2), EUR-Lex | Texto legal oficial | https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:32022L2555 enlace CELEX |
| 3 | Reglamento (UE) 2024/1689 (IA), EUR-Lex | Texto legal oficial | https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:32024R1689 enlace CELEX |
| 4 | Reglamento (UE) 2026/1744 (Ómnibus digital sobre IA), DOUE Serie L, 24-07-2026, CELEX 32026R1744 | Texto legal oficial | https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:32026R1744 enlace CELEX |
| 5 | Reglamento (UE) 2024/2847 (Ciberresiliencia), EUR-Lex | Texto legal oficial | https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:32024R2847 enlace CELEX |
| 6 | ISO/IEC 27001:2022 | Norma técnica | https://www.iso.org/standard/27001 Ficha oficial en iso.org |
| 7 | ISO/IEC 27701:2025 | Norma técnica | https://www.iso.org/standard/27701 Ficha oficial en iso.org |
| 8 | ISO/IEC 42001:2023 | Norma técnica | https://www.iso.org/standard/42001 Ficha oficial en iso.org |
| 9 | NIST Cybersecurity Framework 2.0 | Marco oficial | nist.gov, DOI del NIST CSWP 29 |
| 10 | Ley 25.326 de la República Argentina | Texto legal oficial | InfoLEG |
| 11 | Comisión Europea, página oficial de reporte del CRA | Documentación oficial | digital-strategy.ec.europa.eu |
