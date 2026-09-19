# Directrices de Validación Cruzada: Persona 5 (Martín) vs. Persona 4
## Acta de Calce Biunívoco 1:1 y Blindaje Anti-Comunicado 9
**Asignatura:** Taller de Formulación de Proyectos Informáticos (ICI-5444)  
**Empresa Asignada:** audIT (Empresa 10)  
**Tema:** TI-12 · *Cumplimiento normativo en proyectos TIC*  
**Caso:** Caso 10 · *Transportes Curimón S.A.*  
**Emisor:** Martín (Persona 5 · *Arquitectura & Caso*)  
**Contraparte:** Persona 4 (*Modelo Económico & TCO*)  

---

## 1. Principio Rector de Calce Biunívoco

El **Comunicado 9 (Indicio c)** sanciona con puntaje cero las propuestas donde un capítulo técnico describa tecnologías, componentes o procesos que luego no se reflejen en los costos o que contradigan a otro subdocumento.

Para dar cumplimiento irrestricto a esta exigencia, la presente acta verifica que **cada elemento diseñado por Persona 5 cuenta con una celda presupuestaria asignada en el modelo de Persona 4, y que ninguna partida presupuestaria carece de justificación técnica:**

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       CALCE TÉCNICO-ECONÓMICO 1:1                           │
│                                                                             │
│  Componente en Arquitectura (P5)      Partida Presupuestaria (P4)          │
│  ───────────────────────────────      ───────────────────────────          │
│  • Cifrado FLE RT-11.10         <───> C-02: Cifrado en BD (120 UF)          │
│  • Módulo Consentimiento Móvil  <───> C-01: UX/UI App (45 UF)               │
│  • 148 Contratos DPA            <───> C-03: Asesor Legal (95 UF)            │
│  • EIPD / DPIA Flota 374 GPS    <───> C-04: EIPD DPO/Legal (80 UF)          │
│  • Cláusulas SCC Mendoza        <───> C-05: SCC Transfronterizo (35 UF)     │
│  • Azure Key Vault HSM          <───> Gestión Claves HSM E-24               │
│  • Notificación CSIRT < 3 h     <───> Retainer CISO E-26 (O-03)             │
│  • Supervisión RAT y ARCO       <───> Retainer DPO E-26 (O-02)              │
│  • CERO COMPONENTES HUÉRFANOS   <───> CERO GASTOS NO JUSTIFICADOS           │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Matriz Detallada de Trazabilidad Cruzada

| # | Elemento Diseñado por Persona 5 | Especificación Técnica (P5) | Partida Presupuestaria en P4 | Valor Asignado P4 | Estado de Calce |
| :---: | :--- | :--- | :--- | :---: | :---: |
| 1 | **Módulo Consentimiento Móvil** | Pantalla digital en `audIT Mobile` para los 258 choferes externos; registro de timestamp y revocación. | **C-01:** Consultoría diseño UX/UI e integración en app móvil (EDT 2.4). | 45,0 UF | **CALCE 1:1** ✅ |
| 2 | **Cifrado de Campo FLE (RT-11.10)** | Cifrado cliente AES-256-GCM sobre PostgreSQL 16; una llave por titular para borrado criptográfico. | **C-02:** Consultoría arquitectura de cifrado y esquemas de llaves (EDT 3.4). | 120,0 UF | **CALCE 1:1** ✅ |
| 3 | **Contratos DPA con 148 Transportistas** | Estandarización y firma de acuerdos de encargo (Art. 15 bis) para delimitar responsabilidad de Curimón. | **C-03:** Asesor Legal TIC (47,5 horas a 2,0 UF/h según E-26). | 95,0 UF | **CALCE 1:1** ✅ |
| 4 | **EIPD / DPIA Flota Masiva** | Evaluación de impacto sobre 374 camiones GPS y modelo algorítmico de fatiga (Art. 15 ter). | **C-04:** Asesor Legal (30h) + DPO (10h) según Formulario E-26. | 80,0 UF | **CALCE 1:1** ✅ |
| 5 | **Cláusulas Transfronterizas SCC** | Adopción de Cláusulas Contractuales Tipo para réplica Azure East US 2 y cruces a Mendoza (~1.900/a). | **C-05:** Asesor Legal Especializado TIC (17,5 horas a 2,0 UF/h). | 35,0 UF | **CALCE 1:1** ✅ |
| 6 | **Oficial de Seguridad (CISO 24/7)** | Conducción de la mesa de respuesta a ciberincidentes y reporte CSIRT $\le 3\text{ h}$ (Ley 21.663, Art. 14). | **O-03:** Retainer mensual CISO E-26 (Línea 2479: 24 h/mes a 2,0 UF/h). | 2.688,0 UF | **CALCE 1:1** ✅ |
| 7 | **Delegado de Privacidad (DPO)** | Gestión del RAT, resolución de derechos ARCO de conductores y auditoría del Art. 8 bis. | **O-02:** Retainer mensual DPO E-26 (Proxy JP L2467: 18 h/mes a 2,0 UF/h). | 2.016,0 UF | **CALCE 1:1** ✅ |
| 8 | **Gestión Criptográfica Cloud HSM** | Bóveda FIPS 140-2 Nivel 3 en Azure Chile Central (sin hardware HSM físico on-premise en San Bernardo). | **Infraestructura Nube / Claves:** Servicio Azure Key Vault Managed HSM. | Financiado P4 | **CALCE 1:1** ✅ |

---

## 3. Conformidad Formal Anti-Comunicado 9

Se certifica que:
1. Persona 5 **no incluye AWS**, respetando la decisión unificada de Microsoft Azure en Chile Central.
2. Persona 5 **no dibuja appliances HSM físicos** en San Bernardo, respetando las limitaciones del recinto de 26 m² (RT-06.01) y el presupuesto del TCO.
3. Todas las cifras de población son exactamente las del Caso: **374 camiones, 454 conductores (196 propios / 258 externos), 148 transportistas, 84 clientes y ~1.900 viajes a Mendoza**.
