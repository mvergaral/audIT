# Capítulo 3.1: Arquitectura de Cumplimiento Técnico-Legal y Vinculación con el Caso Curimón S.A.
## Licitación TFEP-01/2026 · Caso 10: Transportes Curimón S.A. · Empresa Consultora audIT
**Tema de Investigación:** TI-12 · *Cumplimiento normativo en proyectos TIC: Ley 21.719, Ley 21.663 (ANCI) y marco internacional*  
**Autor:** Martín (Persona 5 · *Compliance Architecture Designer & Case Integrator*)  
**Extensión Estimada:** 2,5 páginas útiles (~1.400 palabras) · Formato de Integración para Informe Final

---

### 1. Delimitación de Fronteras de Responsabilidad y Modelo Multicapa

La implantación de una plataforma digital de misión crítica para **Transportes Curimón S.A.** (Caso 10) exige traducir los mandatos de la **Ley N.º 21.719** sobre Protección de Datos Personales y de la **Ley N.º 21.663** (Marco de Ciberseguridad) en una arquitectura técnica verificable. El diseño parte de la frontera jurídica formal fijada por el **Artículo 15 bis de la Ley N.º 21.719**:

* **Responsable del Tratamiento:** Transportes Curimón S.A., persona jurídica titular de la operación de transporte, custodia la base de datos de sus 454 conductores, 148 transportistas subcontratados y 84 clientes corporativos, fijando las finalidades operacionales de despacho, seguridad y liquidación.
* **Encargado del Tratamiento:** audIT Soluciones de Software SpA y Microsoft Azure procesan los datos exclusivamente bajo instrucciones formales mediante un Acuerdo de Procesamiento de Datos (*Data Processing Agreement* - DPA). audIT provee la lógica de aplicación, mientras que Azure suministra la infraestructura segura en la nube bajo certificación ISO/IEC 27018.

```
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│                   MAPA DE ARQUITECTURA DE CUMPLIMIENTO (CASO CURIMÓN S.A.)                  │
├─────────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                             │
│  [1. TITULARES Y ACTIVOS]                                                                   │
│   • 196 Conductores Propios  ──────┐                                                        │
│   • 258 Conductores Externos ──────┤ (App audIT Mobile: Consentimiento previo Art. 12)       │
│   • 148 Pymes Transportistas ──────┤ (Portal Web: Secretos comerciales y tarifas cifradas)  │
│   • 374 Camiones en Ruta     ──────┴─► [2. INGESTA: Dispositivo Cabina 8 GB SQLite WAL]     │
│                                                   │                                         │
│                                                   │ (TLS 1.3 / Protocol Buffers diferido)   │
│                                                   ▼                                         │
│  [3. FRONTERA DEL ENCARGADO: Microsoft Azure Chile Central]                                 │
│   ┌──────────────────────────────────────────────────────────────────────────────────────┐  │
│   │ Azure API Management (mTLS, WAF, Cuotas reconexión masiva)                           │  │
│   ├──────────────────────────────────────────┬───────────────────────────────────────────┤  │
│   │ LÓGICA DE NEGOCIO Y GOBERNANZA           │ CRIPTOGRAFÍA Y DATOS (RT-11.10)           │  │
│   │ • Servicio Jornada (Art. 25 bis DT)      │ • Azure Key Vault Premium (claves RSA/HSM) │  │
│   │ • Despacho Bloqueante (<= 30 s RT-09.01) │ • Cifrado de Campo FLE (AES-256-GCM)      │  │
│   │ • Módulo RAT y Derechos ARCO (GRC)       │ • Llave individual por Titular (Borrado)  │  │
│   │ • Revisión Humana Despacho (Art. 8 bis)  │ • Repositorio Inmutable WORM (SHA-256)    │  │
│   └──────────────────────────────────────────┴───────────────────────────────────────────┘  │
│                    │                                              │                         │
│                    │ (Replicación DR Asíncrona)                   │ (Notificaciones Ley)    │
│                    ▼                                              ▼                         │
│  [4. DESTINOS TRANSFRONTERIZOS]              [5. CANALES PERENTORIOS DE REPORTE]            │
│   • Azure East US 2 (Virginia, EE.UU.)        • CSIRT Nacional: <= 3 h / 72 h / 15 d        │
│     (Cláusulas Contractuales Tipo - SCC)        (Ley N.º 21.663 Art. 9 y D.S. 295)         │
│   • Tramo Internacional a Mendoza             • Agencia Protección Datos: Sin dilación      │
│     (~1.900 viajes/año, Ley 25.326 Arg.)        (Ley N.º 21.719 Art. 14 sexies)            │
│                                               • Curimón: <= 2 h crítico / 24 h brecha       │
└─────────────────────────────────────────────────────────────────────────────────────────────┘
```

*Explicación Integral de la Arquitectura:* La figura ilustra el ciclo de vida del dato desde su captura en terreno hasta su persistencia y fiscalización. En el borde izquierdo, los titulares interactúan mediante terminales diferenciados: la aplicación móvil recaba el consentimiento explícito de los 258 choferes externos antes de iniciar el flete, mientras que la unidad telemática de cabina almacena la cinemática en un búfer SQLite WAL de 8 GB con autonomía de hasta 288 horas (12 días, RT-10.05). La información ingresa a la región **Azure Chile Central** bajo terminación mTLS y protección WAF. En el núcleo transaccional, los datos sensibles no se guardan en texto plano: el requisito **RT-11.10** se satisface mediante Cifrado a Nivel de Campo (FLE) respaldado por **Azure Key Vault Premium**, asignando una clave simétrica por titular para garantizar el derecho a la supresión y borrado criptográfico (Art. 7) y al bloqueo temporal (Art. 8 ter). Ante contingencias, la arquitectura activa canales diferenciados: replicación cifrada hacia **Azure East US 2** mediante Cláusulas Contractuales Tipo, y reporte perentorio de ciberincidentes al **CSIRT Nacional en menos de 3 horas** (Ley N.º 21.663, Art. 9 y D.S. N.º 295/2024).

---

### 2. Privacidad por Arquitectura (PbD) y Derechos de los Titulares

En conformidad con el **principio de seguridad (Art. 3° letra f) y el deber de medidas de seguridad del Art. 14 quinquies de la Ley N.º 21.719**, el sistema implementa la privacidad desde el diseño mediante cuatro instrumentos operativos:

1. **Tratamiento Diferenciado de Choferes (196 Propios vs. 258 Externos):** Para la dotación propia de Curimón, la base de licitud radica en la ejecución del contrato de trabajo y el cumplimiento del **Artículo 25 bis del Código del Trabajo** (control de fatiga y descansos, amparado en el Dictamen Ord. 569/2024 de la Dirección del Trabajo). Para los 258 conductores externos de pymes subcontratadas, el rastreo continuo fuera de servicio constituiría una vulneración grave; por ello, la app móvil exige **consentimiento previo y explícito (Art. 12)** y el firmware a bordo desactiva el streaming satelital inmediatamente después de confirmada la entrega en destino.
2. **Evaluación de Impacto (EIPD / DPIA - Art. 15 ter):** Al monitorear en tiempo real a 374 tractocamiones cada 30 segundos a lo largo de 41 millones de kilómetros anuales, se configura un tratamiento masivo de alto riesgo. La EIPD formalizada en la Etapa 1 introduce el **enclavamiento cinético de pantalla** (conforme a la Ley N.º 21.377 "No Chat", bloqueando la interfaz táctil con $v > 0\text{ km/h}$) y el aislamiento de datos de conducción agresiva frente a fines disciplinarios directos.
3. **Supervisión Humana ante Bloqueos Automatizados (Art. 8 bis):** La verificación bloqueante del despacho (RT-09.01) evalúa de forma algorítmica las invariantes de jornada, vigencias mecánicas y sustancias peligrosas (D.S. N.º 298) en $\le 30$ segundos. Para cumplir con la garantía del Art. 8 bis, el sistema prohíbe el rechazo opaco: ante un bloqueo, la plataforma genera un documento con la causal específica y habilita un flujo de **revisión humana inmediata** a cargo de la torre de programación 24/7.
4. **Registro de Actividades de Tratamiento (RAT - Art. 14 ter):** Erradica las 4 planillas Excel y ~6.000 vigencias manuales actuales mediante un catálogo automatizado en la herramienta GRC, aplicando políticas de retención legales inalterables: 5 años para jornadas laborales, 6 años para documentos tributarios (SII) y 2 años en línea para telemetría cruda (Capítulo 15 del Caso).

---

### 3. Transferencias Internacionales de Datos y Selección de Nube

El análisis de flujos transfronterizos bajo los **Artículos 27 y 28 de la Ley N.º 21.719** resuelve dos necesidades críticas de Curimón S.A.:

* **Sede Primaria y Réplica de Desastres (Vector Cloud):** La elección de **Microsoft Azure Chile Central** (Santiago) asegura la residencia territorial de los datos y el cumplimiento de RT-03.01. Sin embargo, para satisfacer el requisito **RT-07.02** (sitio secundario geográficamente desvinculado del riesgo sísmico de la cuenca central con RTO $\le 4\text{ h}$ y RPO $\le 15\text{ min}$), la réplica pasiva se ubica en **Azure East US 2 (Virginia, EE.UU.)**. La legalidad de este traspaso se asegura mediante **Cláusulas Contractuales Tipo (SCC)** suscritas entre Curimón, audIT y Microsoft, complementadas con cifrado ciego: las llaves maestras residen exclusivamente en el HSM chileno, impidiendo el acceso a datos en claro por autoridades o terceros en destino.
* **Tránsito Terrestre Internacional a Mendoza (Vector Terrestre):** Los **~1.900 viajes anuales** por el paso Los Libertadores activan el régimen de exportación transfronteriza. Este flujo se ampara en el **Artículo 27 letra b)** (necesidad contractual de transporte internacional) y en la **Ley N.º 25.326 de Argentina**, país que cuenta con declaración de adecuación formal por la Unión Europea. La unidad embarcada con 8 GB absorbe interrupciones de señal en alta montaña de hasta 12 días (RT-10.05) sin pérdida de integridad probatoria.

---

### 4. Vínculo con la Propuesta Técnico-Económica (Caso Curimón S.A.)

Dando estricto cumplimiento a la **Ficha Oficial TI-12**, el cumplimiento normativo deja de ser un costo oculto y se formaliza como una partida estructural de la propuesta:

1. **Trazabilidad con la Estructura de Desglose de Trabajo (EDT):**
   * *EDT 1.3:* Elaboración y validación del RAT corporativo en OpenMetadata (Meses 1-4).
   * *EDT 2.4:* Desarrollo del Módulo de Consentimiento Móvil y Enclavamiento Cinético en `audIT Mobile` (Meses 4-7).
   * *EDT 3.4:* Implementación del Cifrado a Nivel de Campo FLE con Azure Key Vault HSM (Meses 3-6).
   * *EDT 7.2:* Marcha blanca operacional con conductores reales, EIPD y pruebas de reporte CSIRT $\le 3\text{ h}$ (Meses 13-15).
2. **Hitos Contractuales en la Carta Gantt:**
   * *Mes 4 (H2):* RAT formalizado y consentimientos digitales iniciales.
   * *Mes 6 (H3):* Cifrado RT-11.10 operativo y contratos DPA suscritos con las 148 pymes transportistas.
   * *Mes 12 (H5):* Aprobación definitiva de la EIPD y formalización de Cláusulas Contractuales Tipo para Mendoza y EE.UU.
   * *Mes 20:* Certificación de conformidad del SGSI (ISO/IEC 27001 Fases 1+2) previo al paso a producción comercial (Mes 21).
3. **Calce con Perfiles del Formulario E-26:** Las actividades se valorizan con precisión biunívoca en el presupuesto de Persona 4, asignando roles auditados del Formulario E-26: CISO (Encargado Seguridad TI, Línea 2479 a 2,0 UF/h), DPO (Proxy Jefe de Proyecto, Línea 2467 a 2,0 UF/h), Analista QA y Cumplimiento (Línea 2484 a 1,0 UF/h) y Asesor Legal TIC (Línea 2488 a 2,0 UF/h).
4. **Respaldo de Criterios de Aceptación:** Garantiza el **Criterio 4** (cadena inalterable de custodia SHA-256 en WORM), el **Criterio 11** (recupero de \$241,4 millones en sobreestadías objetadas mediante geocercas satelitales auditadas) y el requisito **RF-014** (emisión de Documentos Electrónicos de Transporte sin cobertura celular).
