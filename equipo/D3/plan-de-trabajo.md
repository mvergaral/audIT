# Plan de Trabajo - D3 (Marcel y Martín)
**Informe 1** - Fecha de entrega: Lunes 21 de septiembre de 2026

## 1. Alcance General (D3)
Nuestra dupla tiene el mayor peso en el Informe 1, sumando un **27%** de los requisitos obligatorios, más la responsabilidad conjunta de formular la **Innovación Tipo 3 (17% del Informe 1, compartido en la cartera)**.
- **Subdocumento 4.1 (16%)**: Arquitectura lógica y esquema de la solución.
- **Subdocumento 5 (11%)**: Modelo y gestión de datos.
- **Subdocumento 13 (Innovación Tipo 3)**: Formulario T-19 sobre "Operación desconectada 72 h y unificación de las tres plataformas GPS".
---

## 2. Responsabilidades por Integrante

### Martín (Arquitectura Lógica y Capa Analítica)
**Foco:** Definir cómo se estructuran los módulos de software, integraciones, y la inteligencia de negocio (BI), asegurando resiliencia extrema.

**Tareas Específicas:**
1. **Arquitectura Lógica y Resiliencia (Subdocumento 4.1):** 
   - Diseñar esquema híbrido obligatorio (Nube pública multi-zona + on-premise), abarcando 8 capas (RT-02.01).
   - Aplicar estándar ISO/IEC/IEEE 42010 (5 vistas) y mantener el Registro de Decisiones de Arquitectura (ADR).
   - Capa de aplicación **100% stateless** (sin estado).
   - Patrones de resiliencia obligatorios: Time-outs explícitos (prohibidas llamadas remotas sin timeout), reintento exponencial, cortacircuitos e idempotencia en escrituras.
2. **Integración e Interoperabilidad:**
   - Diseñar la Capa Anticorrupción para aislar el ERP 2013 contable y mensajería asíncrona ("entrega al menos una vez") para desacoplar procesos.
   - Documentar APIs síncronas en OpenAPI 3.1 y asíncronas en AsyncAPI 2.6. Autenticación M2M vía OAuth 2.1 o mTLS.
   - Diseñar API unificada para extraer la telemetría inactiva de 61 tractocamiones propios e ingestar TAGs/combustible.
3. **Capa Analítica (RT-05.25 a RT-05.30):**
   - **Separación absoluta** entre almacenamiento transaccional y analítico.
   - **Cálculo de Costo por Kilómetro:** Debe resolverse para la **Etapa 1** (crítico antes de renegociar contratos en 2027). Latencia analítica ≤ 24 horas manejando componentes con desfase (ej. combustible a 40 días).
   - Definir supuesto para estimar costo real de camiones subcontratados donde solo se conoce la tarifa.
   - Diseñar herramienta de autoservicio con modelo semántico documentado para que Finanzas cree sus propios reportes.

### Marcel (Persistencia, Migración y Retención)
**Foco:** Persistencia auditable, saneamiento de datos heredados y cumplimiento estricto de seguridad legal.

**Tareas Específicas:**
1. **Modelo de Dominio y Persistencia (Subdocumento 5):**
   - Justificar el motor de persistencia frente al Teorema CAP. Presentar diccionario de datos con sensibilidades.
   - **Auditoría inalterable** (incluso para admins) registrando valores antes/después de cada modificación.
   - **Esquema de Respaldo 3-2-1-1-0:** Copias inmutables, RTO 4h, RPO 15min. Cifrado en reposo/tránsito (TLS 1.3).
   - **Seguridad (Ley N° 21.719):** Cifrado a nivel de campo obligatorio para localización, jornada, tarifas y datos de los 258 conductores subcontratados. Anonimización verificable en Dev/QA.
2. **Migración de Datos y Saneamiento:**
   - Migración de ≈6.000 vigencias exigiendo **verificación documental obligatoria** por cada una.
   - Plan de migración con reglas de transformación y al menos **2 ensayos completos** en Preproducción con conciliación cuantitativa final.
3. **Política de Retención (RT-05.10):**
   - Siniestros (10 años), Liquidaciones/DTE (6 años), Jornada/Peligrosas (5 años), Tiempos en cliente (3 años), Telemetría en línea (2 años y agregación posterior).
   - Planificar exportación en formatos abiertos para reversibilidad al término del contrato.

---

## 3. Trabajo Conjunto (Innovación Tipo 3)
**Foco:** Completar el **Formulario T-19** y asegurar su trazabilidad en la Arquitectura Lógica.
- **Tema:** *Operación desconectada 72 h y unificación de 3 plataformas GPS.*
- **Elementos requeridos en T-19:** Justificación del problema, tecnología con nivel de madurez citado en **APA 7.ª ed.**, impacto económico preliminar y mitigación de riesgos.
- **Diseño de la Operación Desconectada:**
  - Declarar explícitamente qué funciones **NO** estarán disponibles offline y el procedimiento manual de contingencia.
  - Diseñar la emisión en sombra del Documento de Transporte Electrónico (DTE).
  - Justificar tipo de app móvil (nativa/híbrida) frente al uso offline, estimando consumo de batería/datos.
  - Soportar reconexión masiva simultánea sin pérdida de integridad en max 20 min por camión, con bitácora determinista de resolución de conflictos. Hardware on-premise crítico debe declarar RAID (tolerancia falla 1 disco).
- **Unificación GPS:**
  - Unificar 3 proveedores (uno de los cuales no exporta datos) sin reemplazar el hardware externo e integrar 34 camiones sin GPS. Considerar que la instalación a bordo se hace camión a camión según su paso por el terminal (cada 6 a 30 días).

---

## 4. Hitos y Próximos Pasos Inmediatos
1. **Levantamiento Fino:** Cruzar las restricciones de infraestructura (San Bernardo, camiones externos) con definiciones lógicas y persistencia.
2. **Consolidación de Arquitectura:** Martín define las cajas, Marcel define cómo los datos viven dentro y fluyen entre ellas.
3. **Redacción y Cruce:** Armar los documentos de los Subdocumentos 4.1 y 5 asegurando coherencia absoluta.
4. **Formulario T-19:** Cerrar la ficha de la innovación antes de la consolidación final.
5. **Preparación de la Defensa (Art. 45):** Ambos integrantes deben dominar todos los temas de la dupla. El mandante exige 15 min de exposición y se reserva el derecho de *designar quién expone cada sección* sin previo aviso.

