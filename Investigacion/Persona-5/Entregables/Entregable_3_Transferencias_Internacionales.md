# Entregable 3: Transferencias Internacionales de Datos y Selección de Región Cloud
## Licitación TFEP-01/2026 · Caso 10: Transportes Curimón S.A. · Empresa Consultora audIT
**Tema de Investigación:** TI-12 · *Cumplimiento normativo en proyectos TIC: Ley 21.719, Ley 21.663 (ANCI) y marco internacional*  
**Autor:** Martín (Persona 5 · *Compliance Architecture Designer & Case Integrator*)  
**Fecha:** Septiembre de 2026  
**Estado:** Versión Definitiva 1.0 — Auditada con Trazabilidad al Caso 10 y al Informe 1

---

## 1. Marco Jurídico Aplicable a Flujos Transfronterizos

El **Artículo 27 de la Ley N.º 21.719** establece como regla general que la transferencia internacional de datos personales solo procede cuando el receptor se encuentra en un país que proporcione niveles adecuados de protección o cuando se otorguen garantías contractuales idóneas.

En la operación de **Transportes Curimón S.A.** se identifican dos vectores transfronterizos distintos que exigen soluciones técnicas y contractuales diferenciadas:
1. **Vector Cloud (Infraestructura de Misión Crítica):** Almacenamiento primario en Chile y replicación pasiva de contingencia en Estados Unidos.
2. **Vector Terrestre Operacional (Corredor Bioceánico):** Tránsito de tractocamiones chilenos hacia Mendoza (Argentina) a través del paso Los Libertadores.

---

## 2. Vector 1: Arquitectura de Nube y Residencia de Datos

### 2.1 Justificación de la Región Primaria: Microsoft Azure Chile Central
Conforme a los requerimientos **RT-03.01 y RT-03.02 de las Bases Técnicas Transversales**, el adjudicatario debe declarar la nube pública y garantizar presencia de región en Chile o Sudamérica con arquitectura multi-zona de disponibilidad.

* **Sede de Tratamiento:** La región **Azure Chile Central** (desplegada en la Región Metropolitana de Santiago) aloja el núcleo transaccional en PostgreSQL 16 Multi-AZ, la base de telemetría TimescaleDB y los microservicios de despacho en Azure Kubernetes Service (AKS).
* **Beneficio Regulatorio:** Los datos personales de los 454 conductores, habilitaciones y registros de clientes se mantienen bajo jurisdicción territorial chilena durante la operación normal, garantizando plena residencia local del dato y cumplimiento inmediato del principio de soberanía del dato sin requerir salvaguardas transfronterizas complejas en régimen diario.

### 2.2 Réplica Secundaria de Recuperación ante Desastres: Azure East US 2
El requisito **RT-07.02** exige que el sitio secundario se encuentre a distancia suficiente para no compartir el evento de fuerza mayor o desastre natural que afecte al sitio principal (riesgo sísmico mayor en la cuenca central chilena). La sala de servidores de San Bernardo (26 m², climatización doméstica, UPS de 20 min) no califica como sitio de respaldo geográfico conforme a los umbrales de RTO $\le 4\text{ h}$ y RPO $\le 15\text{ min}$ (RT-07.09 y RT-07.13).

* **Destino de la Replicación Asíncrona:** Región **Azure East US 2** (Virginia, Estados Unidos).
* **Mecanismo de Legalidad (Art. 28 Ley 21.719):** Dado que Estados Unidos no cuenta con una ley federal omnibus declarada como "país adecuado" por la APDP, la transferencia se legaliza mediante **Cláusulas Contractuales Tipo (SCC / CCT)** suscritas entre Curimón S.A., audIT y Microsoft Corporation, incorporando:
  1. Cláusula de no acceso estatal injustificado y deber de notificación ante requerimientos judiciales foráneos.
  2. Cifrado a nivel de campo (RT-11.10) con llaves maestras custodiadas exclusivamente en el HSM de Chile Central; los datos transferidos a East US 2 viajan y descansan en estado permanentemente cifrado, de modo que el operador de infraestructura en EE.UU. carece de capacidad técnica de descifrado (cifrado ciego).

---

## 3. Vector 2: Operación Logística Internacional a Mendoza (Argentina)

El Caso 10 documenta **~1.900 cruces internacionales al año** a través del paso fronterizo Los Libertadores hacia la provincia de Mendoza. Durante este tramo internacional, los camiones continúan emitiendo eventos de telemetría y geolocalización satelital.

### 3.1 Armonización Jurídica con la Ley N.º 25.326 de Argentina
* **Nivel de Adecuación:** La República Argentina cuenta con decisión de adecuación de la Comisión Europea desde el año 2003 (Decisión 2003/490/CE), ratificada bajo los estándares del RGPD. Su marco legal (**Ley N.º 25.326 de Protección de Datos Personales**) reconoce principios equivalentes a la Ley N.º 21.719 chilena (consentimiento, finalidad, seguridad y derechos ARCO).
* **Base de Transferencia:** La transferencia califica bajo el **Artículo 27 letra b) de la Ley N.º 21.719** (transferencia necesaria para la ejecución de un contrato de transporte internacional entre el titular/transportista y el responsable).

### 3.2 Salvaguardas Técnicas en Cabina y Red Celular Extranjera
1. **Roaming Celular y Sincronización Diferida:** La unidad embarcada con memoria de 8 GB almacena atómicamente en SQLite WAL toda la cinemática en territorio argentino. Al ingresar a zonas de sombra celular en alta montaña (hasta 12 días por cierres climáticos invernales, RT-10.05), el registro no se interrumpe ni se descarta.
2. **Homologación de Datos de Hoja de Ruta:** La transmisión de manifiestos y documentos electrónicos de transporte (MIC/DTA) hacia aduanas o clientes en Argentina se realiza vía canales seguros TLS 1.3 con validación de hash SHA-256 de conformidad con el estándar MERCOSUR de transporte internacional terrestre.

---

## 4. Cuadro Comparativo de Proveedores Cloud frente al Cumplimiento TI-12

| Proveedor Cloud | Región Primaria en Chile | Modelo de HSM Dedicado en Chile | Cumplimiento ISO/IEC 27018 | Compatibilidad Caso Curimón |
| :--- | :--- | :--- | :---: | :--- |
| **Microsoft Azure (Seleccionado)** | **Chile Central** (Santiago, 3 Zonas Multi-AZ operativas) | **Azure Key Vault Premium** (claves RSA respaldadas por HSM, región local) | **Sí** (Acreditado auditoría BSI) | **Óptima:** Coherente 100% con Subdoc 4 y Subdoc 5 de audIT. |
| **Amazon Web Services (AWS)** | Local Zone Santiago / sa-east-1 (São Paulo) | CloudHSM (solo en Brasil; KMS multitenant en Chile) | Sí (Acreditado) | Subóptima: Requiere transferir llaves maestras a Brasil o EE.UU. |
| **Google Cloud Platform (GCP)** | southamerica-west1 (Santiago, 3 Zonas) | Cloud KMS / Cloud HSM local | Sí (Acreditado) | Descartada: Mayor costo en enlace privado ExpressRoute vs terminales. |
