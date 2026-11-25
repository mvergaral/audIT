# Caso integrador resuelto — Proyecto SaludConecta

Este documento muestra cómo se conectan alcance, EDT, cronograma, estimación, riesgos y calidad. La finalidad no es memorizar esta empresa, sino aprender una forma de razonar frente a un caso nuevo.

---

## 1. Enunciado

La empresa ficticia **Red Salud Austral** encarga el proyecto **SaludConecta**, una plataforma para consultar resultados de laboratorio, enviar alertas clínicas y administrar permisos de acceso.

Condiciones iniciales:

- plazo solicitado: 8 meses;
- presupuesto: $180 millones;
- equipo inicialmente disponible: 6 personas;
- 120.000 registros deberán migrarse;
- debe integrarse con una API del laboratorio que aún puede cambiar;
- los datos son sensibles;
- el cliente exige respuesta rápida y trazabilidad de requisitos;
- la aprobación final la realiza la directora clínica.

---

## 2. Primera decisión: convertir necesidades en requisitos verificables

### Necesidades vagas

- “Que sea seguro”.
- “Que responda rápido”.
- “Que los resultados sean confiables”.

### Requisitos mejorados

| ID | Requisito | Criterio verificable |
|---|---|---|
| RQ-01 | Solo personal autorizado podrá consultar resultados | Pruebas de roles sin accesos indebidos críticos |
| RQ-02 | Las consultas deben responder oportunamente | P95 ≤ 2 s con 500 usuarios concurrentes |
| RQ-03 | Todo acceso a un resultado quedará auditado | 100 % de operaciones críticas genera registro íntegro |
| RQ-04 | Se migrarán 120.000 registros | 100 % procesado y ≥ 99,9 % conciliado automáticamente |
| RQ-05 | Se intercambiarán resultados con el laboratorio | Casos de integración críticos aprobados |

### ¿Por qué hacerlo antes de la EDT?

Si “seguridad” queda como una aspiración general, el equipo puede olvidar trabajo de autenticación, cifrado, auditoría, pruebas y revisión. Los requisitos verificables permiten definir alcance, trabajo y calidad.

---

## 3. Matriz de trazabilidad

| Requisito | Entregable EDT | Caso de prueba | Riesgo relacionado | Responsable |
|---|---|---|---|---|
| RQ-01 | 1.3 Seguridad y accesos | CP-SEC-01 | R2 Datos expuestos | Líder seguridad |
| RQ-02 | 1.2 Portal clínico | CP-PERF-01 | R4 Capacidad insuficiente | Líder técnico |
| RQ-03 | 1.3 Seguridad y accesos | CP-AUD-01 | R2 Datos expuestos | Líder seguridad |
| RQ-04 | 1.5 Migración | CP-MIG-01 | R5 Mala calidad de datos | Líder datos |
| RQ-05 | 1.4 Integración laboratorio | CP-INT-01 | R1 Cambio de API | Líder integración |

La matriz permite seguir la cadena:

```text
Necesidad → requisito → entregable → prueba → aceptación
```

Si cambia RQ-05, se pueden localizar rápidamente la parte de la EDT, las pruebas y el riesgo afectados.

---

## 4. Declaración de alcance

### Incluye

- portal web clínico;
- autenticación por roles;
- auditoría de accesos;
- integración con un laboratorio;
- migración de 120.000 registros;
- pruebas, capacitación y despliegue inicial.

### Excluye

- aplicación móvil nativa;
- integración con otros laboratorios;
- renovación de infraestructura física;
- operación permanente de mesa de ayuda después del período de estabilización.

### Criterios de aceptación

- requisitos críticos aprobados;
- cero vulnerabilidades críticas abiertas;
- rendimiento objetivo alcanzado;
- conciliación de migración cumplida;
- aceptación formal de la directora clínica.

### Supuestos y restricciones

- supuesto: el laboratorio entregará ambiente de prueba en el mes 2;
- restricción: presupuesto máximo de $180 millones;
- restricción: fecha regulatoria dentro de 8 meses;
- supuesto: seis integrantes estarán disponibles al 80 %.

Un supuesto no validado puede originar un riesgo. La fecha y el presupuesto limitan el plan, pero no cambian mágicamente el esfuerzo requerido.

---

## 5. EDT orientada a entregables

```text
1.0 SaludConecta
├── 1.1 Gestión del proyecto
│   ├── 1.1.1 Planes y líneas base
│   └── 1.1.2 Seguimiento y cierre
├── 1.2 Portal clínico
│   ├── 1.2.1 Consulta de pacientes
│   ├── 1.2.2 Visualización de resultados
│   └── 1.2.3 Alertas clínicas
├── 1.3 Seguridad y accesos
│   ├── 1.3.1 Gestión de identidad y roles
│   └── 1.3.2 Auditoría de accesos
├── 1.4 Integración con laboratorio
│   ├── 1.4.1 Contrato de interfaz
│   ├── 1.4.2 Conector
│   └── 1.4.3 Integración validada
├── 1.5 Migración de datos
│   ├── 1.5.1 Datos depurados
│   ├── 1.5.2 Migración piloto
│   └── 1.5.3 Migración conciliada
├── 1.6 Calidad y aceptación
│   ├── 1.6.1 Evidencias de prueba
│   └── 1.6.2 Entregables aceptados
└── 1.7 Transición
    ├── 1.7.1 Usuarios capacitados
    └── 1.7.2 Solución desplegada
```

### Comprobación de la regla del 100 %

La EDT incorpora trabajo de producto y de gestión. Incluye pruebas, migración, capacitación y cierre; no solo programación. Cada nivel inferior representa el 100 % de su elemento padre sin duplicaciones deliberadas.

### Diccionario de un paquete de trabajo

**Código:** 1.4.2  
**Nombre:** Conector de laboratorio  
**Descripción:** componente que recibe y transforma resultados mediante la interfaz aprobada.  
**Incluye:** autenticación técnica, transformación, manejo de errores y registros.  
**Excluye:** modificación del sistema del laboratorio.  
**Criterio de aceptación:** 100 % de casos críticos de contrato y reintento aprobados.  
**Responsable:** líder de integración.  
**Supuesto:** disponibilidad del ambiente externo.  
**Estimación:** 480 horas-persona.  
**Hito asociado:** integración técnica validada.

La EDT no muestra cuándo ocurrirá ese trabajo. Para eso se derivan actividades.

---

## 6. De paquete de trabajo a cronograma

Para simplificar el caso, se representa una porción del proyecto:

| ID | Actividad | Duración | Predecesora |
|---|---|---:|---|
| A | Confirmar requisitos | 3 días | — |
| B | Diseñar arquitectura | 2 días | A |
| C | Prototipar experiencia clínica | 4 días | A |
| D | Desarrollar servicio backend | 5 días | B |
| E | Desarrollar portal | 4 días | B, C |
| F | Integrar portal y servicios | 3 días | D, E |
| G | Ejecutar aceptación | 2 días | F |

Rutas relevantes:

```text
A-B-D-F-G = 3+2+5+3+2, pero F espera también a E
A-C-E-F-G = 3+4+4+3+2 = 16 días
```

La ruta crítica es `A-C-E-F-G` y dura 16 días. B y D disponen de un día de holgura en esta red.

### Decisión ante un atraso

Si C se retrasa dos días, se atrasa la fecha final salvo que:

- se reduzca duración de una actividad crítica mediante intensificación;
- se superponga trabajo mediante ejecución rápida, aceptando más riesgo;
- se reduzca alcance con aprobación;
- se cambie la fecha mediante control integrado de cambios.

Agregar una persona a D no resolvería el problema si D sigue sin gobernar la fecha final.

---

## 7. Estimación por puntos de caso de uso

### Tamaño

- UAW = 16;
- UUCW = 115;
- UUCP = 131;
- TFactor = 38 → TCF = 0,98;
- EFactor = 20 → EF = 0,80.

```text
UCP = 131 × 0,98 × 0,80 = 102,704
```

Con tres factores ambientales desfavorables se usa el valor académico de 28 HH/UCP:

```text
Programación = 102,704 × 28 = 2.875,712 HH
Total = 2.875,712 / 0,40 = 7.189,28 HH
```

### Revisión de factibilidad

Capacidad efectiva:

```text
6 personas × 160 HH/mes × 80 % = 768 HH/mes
```

Duración simplificada:

```text
7.189,28 / 768 = 9,36 meses
```

Costo, con $30.000 por hora:

```text
7.189,28 × $30.000 = $215.678.400
```

### Conclusión profesional

La solicitud de 8 meses y $180 millones no es consistente con esta estimación y estos supuestos. Antes de comprometerse, el director debe:

1. validar el tamaño mediante estimación ascendente y expertos;
2. revisar productividad y tarifas reales;
3. priorizar alcance;
4. evaluar recursos y secuencia;
5. presentar alternativas con consecuencias explícitas.

No debe reemplazar 28 por un factor menor solo para “hacer calzar” el proyecto.

---

## 8. Gestión de riesgos

### Registro priorizado

| ID | Riesgo causa–evento–efecto | P | I | Respuesta | Dueño | Disparador |
|---|---|---:|---:|---|---|---|
| R1 | Como la API no está congelada, podría cambiar y causar retrabajo | 4 | 5 | Mitigar: prototipo + adaptador | Líder integración | Nueva versión de contrato |
| R2 | Por usar datos sensibles, una copia podría exponerse y provocar sanción | 2 | 5 | Evitar/mitigar: datos sintéticos y anonimización | Seguridad | Dato real detectado |
| R3 | Si automatización funciona, podría reducir regresión y adelantar entregas | 3 | 4 | Mejorar: piloto temprano | QA | Cobertura > 60 % |
| R4 | Por capacidad limitada, el tiempo de respuesta podría superar 2 s | 3 | 4 | Mitigar: prueba de carga temprana | Líder técnico | P95 > 1,7 s en piloto |
| R5 | Debido a datos históricos inconsistentes, la conciliación podría fallar | 4 | 4 | Mitigar: perfilamiento y migración piloto | Líder datos | Error > 0,1 % |

### Reserva de contingencia

Si R1 tiene 60 % de probabilidad y un impacto estimado de $20 millones:

```text
EMV R1 = 0,60 × $20 millones = $12 millones
```

Este cálculo ayuda a discutir reserva, pero no obliga a reservar exactamente $12 millones sin considerar correlaciones, otros riesgos y política de la organización.

---

## 9. Gestión de calidad

### Plan y métricas

| Requisito | Métrica | Actividad preventiva | Control | Criterio |
|---|---|---|---|---|
| Seguridad | Vulnerabilidades críticas | Modelado de amenazas y estándar seguro | Prueba de penetración | 0 críticas abiertas |
| Rendimiento | P95 de respuesta | Diseño de caché y revisión | Prueba de carga | ≤ 2 s |
| Migración | Tasa de conciliación | Perfilamiento y reglas de limpieza | Comparación origen/destino | ≥ 99,9 % automática y 100 % resuelta |
| Trazabilidad | Requisitos críticos cubiertos | Matriz mantenida | Auditoría de matriz | 100 % |
| Integración | Casos críticos aprobados | Contrato y simulador | Prueba de contrato | 100 % críticos |

### Flujo de verificación y aceptación

1. El equipo ejecuta pruebas: **Controlar la Calidad**.
2. Si cumple, el entregable queda **verificado**.
3. La directora clínica revisa los criterios: **Validar el Alcance**.
4. Si está conforme, el entregable queda **aceptado**.

Una firma del desarrollador no sustituye la aceptación del cliente; la aceptación tampoco sustituye una prueba regulatoria obligatoria.

---

## 10. Cambio integrado: nueva aplicación móvil

En el mes 3, el patrocinador solicita una aplicación móvil nativa “sin mover la fecha”.

### Respuesta incorrecta

> “Sí, la agregamos y después vemos cómo recuperar el tiempo”.

### Respuesta profesional

1. Registrar la solicitud.
2. Analizar impacto en requisitos y trazabilidad.
3. Actualizar alternativas de EDT y estimación.
4. Evaluar cronograma, ruta crítica y recursos.
5. Identificar riesgos nuevos.
6. definir métricas y pruebas móviles.
7. Presentar alternativas al órgano autorizado:
   - agregar alcance y presupuesto;
   - agregar alcance y extender fecha;
   - intercambiar alcance de menor prioridad;
   - rechazar o postergar a otra fase.
8. Solo después de aprobar, actualizar líneas base y documentos.

Esto evita la corrupción silenciosa del alcance y mantiene coherencia entre las áreas.

---

## 11. Cómo responder un caso en el control

Usa esta estructura breve:

1. **Identifica el problema:** “Existe una solicitud fuera de la línea base”.
2. **Nombra el proceso o concepto:** “Debe pasar por control integrado de cambios”.
3. **Aplica al caso:** “Se analiza su efecto en EDT, cronograma, costo, riesgos y calidad”.
4. **Justifica la elección:** “Agregarla de inmediato impediría medir la desviación y podría comprometer seguridad y fecha”.
5. **Indica la salida o decisión:** “El comité aprueba, rechaza o posterga; luego se actualizan líneas base si corresponde”.

Una respuesta completa no se limita a definir un término: explica qué decisión tomar y por qué otra alternativa sería menos adecuada.

---

## 12. Preguntas para rehacer el caso sin mirar

1. ¿Qué información falta para convertir “confiable” en un requisito?
2. ¿Por qué las pruebas y la gestión del proyecto deben aparecer en la EDT?
3. ¿Qué actividad comprimirías primero en la red y por qué?
4. ¿Qué supuesto de capacidad afecta la conversión de esfuerzo a duración?
5. ¿Qué harías si la estimación por expertos fuera 5 meses y UCP entregara 9,36?
6. ¿Por qué R2 puede tratarse como alto aunque su probabilidad sea 2 de 5?
7. ¿Cuál es la diferencia entre el prototipo de R1 como mitigación y el prototipo como estimación?
8. ¿Qué proceso entrega el producto verificado y cuál entrega el producto aceptado?
9. ¿Qué cambios produce una aplicación móvil en cada área del caso?
10. Escribe una recomendación ejecutiva de cinco líneas para el patrocinador.

