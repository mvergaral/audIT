# Entregable 3: Banco Pedagógico de Preguntas Avanzadas (6 Preguntas · 20%)

**Asignatura:** ICI-5444 · Taller de Formulación de Proyectos Informáticos (PUCV)  
**Empresa N.º 10:** audIT Soluciones de Software SpA · **Tema:** TI-12  
**Caso:** Caso 10 — Transportes Curimón S.A.  
**Rol:** Persona 6 (*Assessment & Knowledge Verification Lead*)  
**Dificultad:** Avanzada (20% del total exigido por las Indicaciones FEP00.3.26)  
**Nivel de Autoría:** Nivel 0 (100% Humano · Formulario A-6)

---

## 1\. Criterio Pedagógico del Bloque Avanzado

El bloque avanzado evalúa los niveles 5 y 6 de la Taxonomía de Bloom (**Evaluar** y **Sintetizar/Crear**). Su objetivo es someter al estudiante a dilemas complejos de ingeniería, trade-offs de arquitectura, modelación microeconómica de la seguridad y colisiones normativas:

1.  **Soberanía del dato y extraterritorialidad:** Impacto de la US CLOUD Act sobre nubes públicas estadounidenses y su mitigación técnica con cifrado gestionado por el cliente (BYOK/HYOK).
2.  **Estructura del costo total de propiedad (TCO):** Racionalidad económica del cumplimiento, identificando la sensibilidad del costo en horas profesionales frente a las licencias de software.
3.  **Mecanismos criptográficos avanzados:** Resolución del conflicto entre retención probatoria obligatoria de 6 años y el derecho de supresión mediante *borrado criptográfico (crypto-shredding)*.
4.  **Resiliencia ante incertidumbre legislativa:** Justificación técnica de por qué una postergación de la Ley 21.719 no autoriza a desmantelar los controles de ciberseguridad.
5.  **Gobernanza de decisiones algorítmicas:** Análisis comparado profundo entre el artículo 8 bis de la Ley 21.719 y el artículo 22 del RGPD ante perfilamiento automatizado.
6.  **Optimización cuantitativa de la ciberseguridad:** Aplicación del marco matemático de Gordon-Loeb sobre la cota óptima de gasto racional ($\le 37\%$).

La distribución de formatos en este bloque es: **2 Selección Múltiple, 2 Verdadero o Falso, 1 Completar y 1 Respuesta Corta**.

---

## 2\. Cuestionario de Evaluación

1.  Dado que la infraestructura cloud seleccionada es Microsoft Azure (proveedor domiciliado en EE.UU.), ¿qué salvaguarda técnica previene que Microsoft pueda entregar la telemetría sensible de Curimón en texto plano ante una orden judicial federal bajo la US CLOUD Act?  
    a) Contratar el servicio de cifrado estándar en reposo con claves administradas automáticamente por Microsoft (SSE con claves de plataforma).  
    b) Alojar los datos en máquinas virtuales aisladas sin conexión a Internet pública ni puertos de administración remota abiertos.  
    c) Implementar cifrado a nivel de campo con claves maestras custodiadas exclusivamente por Curimón en un HSM bajo esquema BYOK / HYOK.  
    d) Suscribir una cláusula contractual que someta cualquier requerimiento judicial extranjero a los tribunales ordinarios de Santiago.
    
2.  En el modelo TCO a 56 meses formulado para el cumplimiento normativo de Curimón (8.375,4 UF), la partida presupuestaria que introduce la mayor variabilidad y riesgo financiero es el costo de adquisición de licencias de software y servidores en la nube.  
    a) Verdadero  
    b) Falso
    
3.  La técnica criptográfica que permite satisfacer el derecho de supresión de un conductor (Art. 8 ter de la Ley 21.719) sin corromper la integridad referencial de las bases de datos de despachos ni infringir los plazos de retención tributaria de 6 años se denomina \_\_\_\_\_\_\_\_ .
    
4.  Si el Congreso Nacional promulga la postergación de la Ley 21.719 hasta diciembre de 2027 (Boletín 18.623-07), ¿por qué audIT no puede rebajar el presupuesto de ciberseguridad ni desmantelar los controles planificados para el primer año de operación de Curimón?
    
5.  Al comparar la Ley 21.719 de Chile con el RGPD europeo respecto a la toma de decisiones basada en tratamientos automatizados y perfilamiento algorítmico:  
    a) La ley chilena prohíbe de manera absoluta cualquier algoritmo en relaciones laborales, mientras que el RGPD lo admite siempre que cuente con autorización sindical previa.  
    b) Ambos cuerpos legales reconocen el derecho del titular a no quedar sujeto a decisiones exclusivamente automatizadas, facultándolo a exigir intervención humana y a conocer los criterios del modelo.  
    c) El RGPD faculta la impugnación de decisiones algorítmicas solo en el sector público, mientras que la normativa chilena limita este derecho exclusivamente al comercio electrónico.  
    d) La legislación chilena exige una auditoría judicial previa al despliegue de cualquier algoritmo, mientras que el RGPD solo contempla sanciones indemnizatorias a posteriori.
    
6.  De acuerdo con el modelo microeconómico de Gordon-Loeb aplicado en el análisis de inversión del proyecto, el gasto óptimo y racional en medidas de ciberseguridad para proteger la plataforma de Curimón no debe superar teóricamente un tercio (≈37%) de la pérdida económica esperada ante una vulneración.  
    a) Verdadero  
    b) Falso
    

---

## 3\. Formulario de Respuestas y Justificaciones (Pauta de Evaluación)

| N.º | Pregunta Resumida | Formato | Respuesta Correcta | Justificación Técnica y Fundamento Legal |
| --- | --- | --- | --- | --- |
| **1** | Mitigación técnica frente a la US CLOUD Act en Azure | Selección | **c) Implementar cifrado a nivel de campo con claves maestras en HSM (esquema BYOK / HYOK).** | La US CLOUD Act faculta a autoridades estadounidenses a exigir datos a empresas bajo su jurisdicción sin importar la sede del datacenter. Si el cliente retiene las llaves en su propio HSM, el proveedor cloud solo puede entregar datos cifrados matemáticamente indescifrables. |
| **2** | Partida de mayor sensibilidad financiera en el TCO | V / F | **b) Falso.** | Las licencias GRC y cómputo cloud representan partidas fijas y predecibles ($<30\%$). Más del 70% del TCO (8.375,4 UF) corresponde a tarifas horarias de perfiles expertos de alta renta (CISO a 2,0 UF/h, DPO y Asesor Legal), donde cualquier atraso operativo genera desviaciones severas. |
| **3** | Mecanismo criptográfico: derecho de supresión vs retención legal | Completar | **borrado criptográfico (o crypto-shredding)** | Se destruye la llave simétrica específica del conductor en Azure Key Vault. Los datos personales del chofer se vuelven irrecuperables de forma irreversible (cumpliendo el Art. 8 ter), conservando intacta la integridad referencial de los fletes históricos para fiscalizaciones del SII y de la DT (6 años). |
| **4** | Efecto de una eventual prórroga legislativa de la Ley 21.719 | Corta | **La Ley 21.663 de Ciberseguridad sigue vigente (servicio esencial) y las Bases Técnicas (RT-11.05/10) exigen ISO 27001 por contrato.** | La prórroga legal solo posterga la exigibilidad de sanciones de la APDP, pero no extingue las obligaciones de ciberseguridad de la ANCI ni anula los compromisos contractuales asumidos con el cliente mandante en la licitación. |
| **5** | Decisiones automatizadas: Ley 21.719 vs RGPD europeo | Selección | **b) Ambos cuerpos legales reconocen el derecho del titular a no quedar sujeto a decisiones exclusivamente automatizadas.** | El Art. 8 bis de la Ley 21.719 incorporó las garantías del Art. 22 del RGPD: las personas tienen derecho a no quedar supeditadas a valoraciones algorítmicas puras que produzcan efectos jurídicos significativos, pudiendo exigir revisión humana y explicabilidad del modelo. |
| **6** | Límite superior del modelo Gordon-Loeb (cota 37%) | V / F | **a) Verdadero.** | Gordon y Loeb (2002) demostraron formalmente que, debido a la ley de rendimientos marginales decrecientes de las tecnologías defensivas, el gasto óptimo en seguridad tiene como cota superior analítica $1/e \approx 36,79\%$ de la pérdida esperada por un incidente. Invertir más allá de ese límite destruye valor económico. |