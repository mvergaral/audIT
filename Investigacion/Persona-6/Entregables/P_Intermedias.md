# Entregable 2: Banco Pedagógico de Preguntas Intermedias (12 Preguntas · 40%)
**Asignatura:** ICI-5444 · Taller de Formulación de Proyectos Informáticos (PUCV)  
**Empresa N.º 10:** audIT Soluciones de Software SpA · **Tema:** TI-12  
**Caso:** Caso 10 — Transportes Curimón S.A.  
**Rol:** Persona 6 (*Assessment & Knowledge Verification Lead*)  
**Dificultad:** Intermedia (40% del total exigido por las Indicaciones FEP00.3.26)  
**Nivel de Autoría:** Nivel 0 (100% Humano · Formulario A-6)

---

## 1. Criterio Pedagógico del Bloque Intermedio

El bloque intermedio evalúa los niveles 3 y 4 de la Taxonomía de Bloom (**Aplicar** y **Analizar**). Su propósito es verificar la capacidad de traducir regulaciones técnicas y legales abstractas a las condiciones operacionales del Caso 10 (Transportes Curimón S.A.):
1. **Delimitación de roles jurídicos y contractuales:** Distinción práctica entre Curimón (Responsable) y audIT/Azure (Encargados bajo DPA).
2. **Arquitectura y limitaciones de infraestructura cloud:** Imposibilidad de redundancia nativa GZRS en Azure Chile Central y necesidad de replicación gestionada hacia East US 2.
3. **Doctrina laboral y telemetría:** Restricciones de la Dirección del Trabajo (Dictamen 569/2018) sobre el uso del GPS en la flota de 374 camiones.
4. **Gobierno de decisiones automatizadas:** Salvaguardas exigidas por el Art. 8 bis de la Ley 21.719 ante el algoritmo de fatiga y despacho.
5. **Cumplimiento de bases técnicas contractuales:** SLAs de aviso a clientes en menos de 2 horas (RT-11.18) y cifrado de campo con HSM (RT-11.10).
6. **Mapeo cruzado GRC y operaciones transfronterizas:** Reutilización de controles y aplicación territorial de la Ley 25.326 en el tramo Santiago--Mendoza.

La distribución de formatos en este bloque es: **3 Selección Múltiple, 3 Verdadero o Falso, 3 Completar y 3 Respuesta Corta**.

---

## 2. Cuestionario de Evaluación

1. En la operación del Caso 10 de Transportes Curimón, ¿qué roles jurídicos asumen la empresa de transporte y el proveedor audIT respecto al tratamiento de datos y telemetría de los 454 choferes bajo la Ley 21.719?  
   a) Curimón actúa como encargado del tratamiento y audIT asume la calidad de responsable principal de las bases de datos.  
   b) Ambas partes operan como corresponsables solidarios directos ante la APDP sin mediar contrato de mandato.  
   c) Curimón es el responsable del tratamiento y audIT actúa exclusivamente como encargado del tratamiento bajo instrucciones.  
   d) audIT es calificado como un simple proveedor de infraestructura física exento de obligaciones de tratamiento de datos.

2. En el despliegue cloud propuesto para Curimón sobre Microsoft Azure, la réplica de datos entre la región primaria (Chile Central) y el sitio secundario de contingencia (East US 2) puede implementarse habilitando almacenamiento geo-redundante nativo con zonas (GZRS).  
   a) Verdadero  
   b) Falso

3. El Dictamen Ordinario N.º 569/2018 de la Dirección del Trabajo prohíbe taxativamente que los dispositivos de posicionamiento satelital (GPS) a bordo de la flota vehicular se utilicen como mecanismos directos de control de ________ laboral.

4. Si el módulo analítico de fatiga de Curimón bloquea automáticamente a un conductor para un despacho minero por considerar que presenta signos de somnolencia, ¿qué garantías específicas le confiere el Art. 8 bis de la Ley 21.719?  
   *[Espacio para respuesta breve]*

5. Considerando el cronograma a 56 meses del proyecto de Curimón, ¿en qué momento debe ejecutarse formalmente la Evaluación de Impacto en la Protección de Datos (EIPD / DPIA) sobre el sistema telemático de cabina?  
   a) Durante las pruebas integradas de carga en la Etapa 2, inmediatamente antes del despliegue en producción.  
   b) En la fase de arquitectura y diseño conceptual durante la Etapa 1, de manera previa al inicio del tratamiento de telemetría masiva.  
   c) En el mes 21 de operación, una vez consolidada la línea base de los primeros 100 camiones en ruta.  
   d) Solo en caso de que ocurra una filtración de seguridad de datos personales que deba ser reportada a la autoridad.

6. A diferencia del RGPD de la Unión Europea, la Ley Marco de Ciberseguridad de Chile (Ley 21.663) estructura sus multas exclusivamente en Unidades Tributarias Mensuales (UTM), sin considerar un porcentaje sobre los ingresos anuales de la empresa infractora.  
   a) Verdadero  
   b) Falso

7. Si un Operador de Importancia Vital (OIV) experimenta un incidente de ciberseguridad que provoca la interrupción efectiva de su servicio esencial, la Ley 21.663 reduce el plazo de envío de la actualización intermedia al CSIRT Nacional de 72 a ________ horas corridas.

8. ¿Por qué el módulo telemático de detección de fatiga y despacho automatizado de Curimón clasificaría como sistema de «Alto Riesgo» según el Reglamento de IA de la Unión Europea (Reglamento UE 2024/1689)?  
   *[Espacio para respuesta breve]*

9. De acuerdo con las Bases Técnicas del Caso 10 de Curimón, ¿cuál es el plazo máximo contractual fijado en el requerimiento RT-11.18 para que audIT notifique a la contraparte ante un incidente de ciberseguridad calificado como crítico?  
   a) Máximo 2 horas.  
   b) Máximo 6 horas.  
   c) Máximo 12 horas.  
   d) Máximo 24 horas.

10. Cuando un camión de Transportes Curimón cruza la frontera y opera en el tramo internacional hacia Mendoza, la telemetría capturada en ruta y el tratamiento de datos de los choferes en territorio trasandino quedan alcanzados por la Ley 25.326 de la República Argentina.  
    a) Verdadero  
    b) Falso

11. Para cumplir el requerimiento RT-11.10 de las Bases Técnicas, la plataforma de audIT debe asegurar que las llaves criptográficas utilizadas para el cifrado a nivel de campo se resguarden en un módulo de seguridad de hardware denominado ________ (o por su sigla en inglés).

12. ¿Cuál es la principal justificación técnica y económica para incorporar una plataforma de software GRC (como CISO Assistant) frente al uso tradicional de hojas de cálculo en el proyecto de Curimón?  
    *[Espacio para respuesta breve]*

---

## 3. Formulario de Respuestas y Justificaciones (Pauta de Evaluación)

| N.º | Pregunta Resumida | Formato | Respuesta Correcta | Justificación Técnica y Fundamento Legal |
| :---: | :--- | :---: | :--- | :--- |
| **1** | Roles jurídicos de Curimón y audIT bajo Ley 21.719 | Selección | **c) Curimón es responsable del tratamiento y audIT actúa exclusivamente como encargado del tratamiento.** | Curimón determina fines y medios del negocio logístico (responsable). audIT procesa y aloja la telemetría por cuenta de la mandante siguiendo sus instrucciones contractuales (encargado, Art. 15 bis), formalizado a través de un Acuerdo de Procesamiento de Datos (DPA). |
| **2** | Disponibilidad de almacenamiento GZRS nativo en Azure Chile Central | V / F | **b) Falso.** | Azure Chile Central carece de «región emparejada» (*paired region*) en la topología global de Microsoft. La sincronización hacia East US 2 debe gestionarse a nivel de aplicación y motor de base de datos con transferencias internacionales controladas bajo SCC. |
| **3** | Restricción del GPS según Dictamen DT 569/2018 | Completar | **asistencia y jornada (o jornada laboral)** | La doctrina laboral chilena dictamina que la geolocalización continua es un medio técnico para la seguridad física de la carga y la gestión logística vial, pero no constituye un mecanismo lícito para fiscalizar pausas, descansos o registrar el inicio/término de la jornada de trabajo. |
| **4** | Garantías del Art. 8 bis Ley 21.719 ante algoritmo de fatiga | Corta | **Derecho a ser informado de la decisión automatizada, conocer los criterios del modelo e impugnar exigiendo revisión humana.** | El Art. 8 bis prohíbe que las personas queden sujetas a decisiones puramente algorítmicas que impacten negativamente sus condiciones laborales sin una instancia efectiva de explicación y contradicción humana. |
| **5** | Momento de ejecución de la EIPD / DPIA en el proyecto | Selección | **b) En la fase de arquitectura y diseño conceptual durante la Etapa 1, previo al tratamiento masivo.** | Por mandato del Art. 15 ter de la Ley 21.719 y el principio de Privacy by Design, la EIPD debe ser preventiva. Analizar los riesgos de 454 choferes en la Etapa 1 permite incorporar controles técnicos (cifrado, consentimiento granular) en el diseño de software antes de capturar datos reales. |
| **6** | Estructura de sanciones en la Ley 21.663 vs RGPD | V / F | **a) Verdadero.** | El Art. 40 de la Ley 21.663 tasa las infracciones exclusivamente en UTM (hasta 20.000 UTM generales y hasta 40.000 UTM si se trata de un OIV reincidente), sin incorporar la figura del porcentaje de facturación que sí utilizan el RGPD y la Ley 21.719 de datos personales. |
| **7** | Plazo agravado de reporte al CSIRT para OIV con servicio interrumpido | Completar | **24** | El Art. 9 de la Ley 21.663 establece un procedimiento agravado de notificación para OIV cuando hay afectación a la continuidad operacional: se mantiene la alerta temprana en 3 horas, pero la actualización técnica se reduce de 72 a 24 horas corridas. |
| **8** | Calificación del módulo de fatiga como Alto Riesgo en la UE | Corta | **El Anexo III numeral 4 del AI Act cataloga como alto riesgo los sistemas de IA de supervisión laboral y asignación de turnos.** | El monitoreo continuo de conductores y la inferencia algorítmica sobre su capacidad física impactan directamente en sus derechos laborales y su seguridad personal, requiriendo gobernanza, trazabilidad y supervisión humana. |
| **9** | Plazo contractual RT-11.18 para avisar incidente crítico al cliente | Selección | **a) Máximo 2 horas.** | El requerimiento contractual RT-11.18 impone un estándar privado más exigente que la alerta temprana de la Ley 21.663 (3 horas), obligando a audIT a notificar formalmente a Curimón en un plazo no superior a 2 horas desde la confirmación de la criticidad del evento. |
| **10** | Aplicación territorial de ley de datos argentina en tramo a Mendoza | V / F | **a) Verdadero.** | Por el principio universal de territorialidad de la ley, cualquier tratamiento o captura de datos personales efectuada en territorio argentino se rige por su propia legislación (Ley 25.326), quedando bajo la fiscalización de la Agencia de Acceso a la Información Pública (AAIP). |
| **11** | Custodia de claves de cifrado de campo bajo RT-11.10 | Completar | **HSM (Hardware Security Module)** | El almacenamiento de claves maestras en un dispositivo HSM certificado (mínimo FIPS 140-2 Nivel 3) garantiza que las claves no residan en texto plano en la memoria del servidor de aplicaciones ni queden expuestas al proveedor del servicio cloud. |
| **12** | Justificación técnica de software GRC frente a planillas | Corta | **Permite mapeo cruzado de controles, acreditando una sola evidencia para ISO 27001, Ley 21.663, Ley 21.719 y RGPD.** | Centralizar la trazabilidad y la gestión de evidencias normativas en una única plataforma evita redundancias operacionales y disminuye drásticamente el costo de horas profesionales de auditoría presupuestadas en el TCO del proyecto. |
