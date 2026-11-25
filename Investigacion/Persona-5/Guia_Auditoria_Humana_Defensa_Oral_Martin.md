# Guía de Auditoría Humana y Defensa Oral para Martín (Persona 5)
## Trabajo de Investigación TI-12 · Caso 10: Transportes Curimón S.A.
**Rol:** Persona 5 (*Compliance Architecture Designer & Case Integrator*)  
**Responsable:** Martín  
**Objetivo:** Instrucciones precisas para auditar personalmente el trabajo (Nivel 0 de IA) y defender oralmente ante la comisión evaluadora sin vacilaciones.

---

## 1. Dónde y Qué Debes Auditar Tú como Humano (Nivel 0 Estricto)

El **Comunicado 9** y la **Sección 6.1 de las Indicaciones del Curso** establecen que el docente puede interrogarte oralmente sobre el contenido técnico para verificar que no fue un volcado de IA no comprendido.

Debes leer y validar personalmente los siguientes 5 puntos en los documentos de `Investigacion/Persona-5/`:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│              LOS 5 PUNTOS CRÍTICOS QUE DEBES DOMINAR ORALMENTE              │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. ¿Quién es Responsable y quién Encargado? (Art. 15 bis Ley 21.719)        │
│ 2. ¿Por qué los 258 choferes externos exigen consentimiento y los 196 no?   │
│ 3. ¿Cuáles son los plazos perentorios ante el CSIRT Nacional? (Ley 21.663)  │
│ 4. ¿Por qué la réplica en EE.UU. exige Cláusulas Contractuales Tipo (SCC)?  │
│ 5. ¿Por qué no usamos servidores HSM físicos en San Bernardo?               │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Balotario de Preguntas Difíciles del Profesor y Respuestas Auditadas

### Pregunta 1: «¿Quién responde legal y económicamente ante la Agencia si se filtran las coordenadas GPS de un conductor en su plataforma?»
* **Tu Respuesta Clave:**
  > «**Transportes Curimón S.A. es el Responsable del tratamiento** según el Artículo 15 bis de la Ley N.º 21.719, porque es quien determina los fines comerciales del servicio y la necesidad de monitoreo. **audIT actúa únicamente como Encargado del tratamiento**, operando el software y la nube bajo contrato vinculante (DPA). Curimón responde directamente ante la Agencia y los titulares, sin perjuicio de que Curimón pueda repetir contra audIT si demostrara que nosotros vulneramos las cláusulas de seguridad estipuladas en el DPA.»

### Pregunta 2: «Ustedes tienen 454 conductores. ¿Por qué tratan de forma distinta a los 196 de planta frente a los 258 externos?»
* **Tu Respuesta Clave:**
  > «Porque la relación jurídica es completamente distinta:
  > - Los **196 conductores propios** tienen contrato de trabajo con Curimón. El tratamiento de su geolocalización y jornada se funda en la obligación legal del empleador bajo el **Artículo 25 bis del Código del Trabajo** (no requieren consentimiento individual, Dictamen Ord. 569/2024 de la Dirección del Trabajo).
  > - Los **258 conductores externos** pertenecen a 148 pymes subcontratadas. Curimón no tiene subordinación jurídica sobre ellos. Monitorearlos sin una base legal propia violaría el Artículo 12 de la Ley 21.719. Por eso desarrollamos en la app móvil un **Módulo de Consentimiento Previo, Informado y Revocable**, con una salvaguarda técnica en el firmware del camión: al finalizar el flete comercial, el tracking satelital se apaga para no invadir su vida privada.»

### Pregunta 3: «Si Curimón sufre un ransomware o un ataque que bota la torre de control 24/7, ¿a quién le tienen que avisar y en qué plazo?»
* **Tu Respuesta Clave:**
  > «Se activa un protocolo tripartito perentorio:
  > 1. Al **CSIRT Nacional de la ANCI** (Ley N.º 21.663, Art. 14 y D.S. 295): alerta temprana obligatoria en **menos de 3 horas**, actualización a las **72 horas** e informe técnico final en **15 días**.
  > 2. A la **Agencia de Protección de Datos Personales** (Art. 14 sexies Ley 21.719): notificación sin dilaciones indebidas si se comprometieron datos sensibles de conductores o clientes.
  > 3. Al **Mandante (Curimón S.A.)**: por contrato de licitación, alerta en un máximo de **2 horas** ante caída de servicio crítico (RT-11.18) y en **24 horas** ante brechas de datos (RT-11.19).»

### Pregunta 4: «Ustedes dicen que los datos viven en Azure Chile Central. Entonces, ¿por qué declaran transferencias internacionales de datos?»
* **Tu Respuesta Clave:**
  > «Por dos requerimientos fácticos del caso:
  > 1. **La réplica secundaria de desastres (RT-07.02):** San Bernardo no puede ser sitio secundario porque comparte el riesgo sísmico con Santiago. La réplica pasiva asíncrona se despliega en **Azure East US 2 (Virginia, EE.UU.)**. Como EE.UU. no es un país con legislación equivalente universal, legalizamos el flujo mediante **Cláusulas Contractuales Tipo (SCC)** bajo el Artículo 28 de la Ley 21.719, complementado con cifrado ciego (las llaves maestras nunca salen de Chile).
  > 2. **El corredor a Mendoza (~1.900 viajes anuales):** Al cruzar el paso Los Libertadores, los camiones transmiten desde territorio argentino. La transferencia se ampara en el Artículo 27 letra b (ejecución de contrato internacional de transporte) y en la **Ley N.º 25.326 de Argentina**, país que cuenta con adecuación formal ante la Unión Europea.»

### Pregunta 5: «¿Por qué en su arquitectura técnica no pusieron servidores criptográficos físicos (appliance HSM) en la sala de San Bernardo?»
* **Tu Respuesta Clave:**
  > «Por consistencia técnica y financiera con Persona 4:
  > 1. **Condición de sitio (RT-06.01):** La sala de San Bernardo tiene apenas 26 m², split doméstico y UPS de 20 minutos; incumple las normas para alojar infraestructura física de alta criticidad sin obras civiles mayores.
  > 2. **Costo inútil:** Un appliance HSM físico cuesta entre USD 30.000 y USD 60.000 y no está financiado en el TCO de la propuesta. En su lugar, utilizamos **Azure Key Vault Managed HSM** en Azure Chile Central (certificado FIPS 140-2 Nivel 3 gestionado en la nube), que cumple el requisito RT-11.10 y cuesta exactamente lo que Persona 4 presupuestó en el modelo de costos.»

---

## 3. Declaración de Uso de IA para el Formulario A-6 (Tu Sección)

Cuando completes tu fila en el **Formulario A-6 del Anexo de IA**, debes consignar exactamente lo siguiente:

| Campo Formulario A-6 | Lo que debes registrar tú (Martín) |
| :--- | :--- |
| **Sección del Trabajo** | Sección 3.1: Arquitectura de Cumplimiento Técnico-Legal y Vinculación con el Caso 10 |
| **Nivel Declarado (0-3)** | **Nivel 2** |
| **Herramienta y Versión** | Claude 3.5 Sonnet / Gemini (Antigravity v2.0) |
| **Uso Efectivo Declarado** | Generación de sintaxis base para diagramas Mermaid y estructuración de tablas comparativas a partir de especificaciones humanas directas. |
| **Autoría Humana (Nivel 0)** | Diseño de la arquitectura de cumplimiento, delimitación de la frontera Responsable/Encargado, elección de Azure Chile Central frente a AWS, y la lógica de protección de los 258 choferes externos. |
| **Evidencia Adjunta** | Historial de commits en el repositorio Git de la carpeta `Investigacion/Persona-5/` y registro de prompts en el Anexo B. |
