# CONTROL N.º 1 — SIN RESPUESTAS

**Taller de Formulación de Proyectos / ICI5444-1**  
**Fecha original:** 8 de septiembre de 2025  
**Duración:** 60 minutos  
**Profesor:** Antonio Moya Villegas

**Nombre:** ________________________________________________

## Instrucciones

- Todas las preguntas son de alternativas con desarrollo.
- Debes marcar una alternativa y justificar matemáticamente tu respuesta.
- Este documento replica el control antiguo, pero elimina la pauta, los cálculos y las respuestas.

---

# Caso 1: Sistema Integrado de Gestión Hospitalaria "MediSys"

La empresa TechHealth Solutions ha sido contratada para desarrollar un sistema integrado de gestión hospitalaria llamado **MediSys** para una red de cinco hospitales. El análisis preliminar ha identificado los siguientes componentes.

## Actores del sistema

- **Actores simples (API):** 3 sistemas externos: laboratorio, farmacia y facturación.
- **Actores medios (protocolo):** 2 sistemas: radiología DICOM y mensajería HL7.
- **Actores complejos (GUI):** 8 usuarios: médicos, enfermeras, administrativos, pacientes, farmacéuticos, laboratoristas, radiólogos y directivos.

## Casos de uso identificados

### Módulo Pacientes: 6 casos de uso

- Registro de paciente: 8 transacciones.
- Admisión hospitalaria: 12 transacciones.
- Historia clínica: 15 transacciones.
- Agendamiento de citas: 6 transacciones.
- Alta médica: 10 transacciones.
- Consulta de expediente: 4 transacciones.

### Módulo Médico: 5 casos de uso

- Diagnóstico: 9 transacciones.
- Prescripción: 7 transacciones.
- Orden de exámenes: 5 transacciones.
- Cirugías: 14 transacciones.
- Interconsultas: 6 transacciones.

### Módulo Administrativo: 4 casos de uso

- Facturación: 11 transacciones.
- Gestión de camas: 8 transacciones.
- Reportes gerenciales: 13 transacciones.
- Auditoría: 3 transacciones.

## Factores técnicos evaluados

`T1=5, T2=4, T3=3, T4=5, T5=4, T6=2, T7=2, T8=4, T9=3, T10=5, T11=5, T12=4, T13=3`

Recuerda que los pesos de **T1 y T8 son 2**, mientras que los pesos de **T6 y T7 son 0,5**. Los restantes tienen peso 1.

## Factores ambientales evaluados

`E1(1,5)=2, E2(0,5)=3, E3(1)=2, E4(0,5)=3, E5(1)=3, E6(2)=2, E7(-1)=3, E8(-1)=4`

---

## 1. UUCP

Calcule el valor exacto de **UUCP** (Puntos de Casos de Uso sin ajustar) para el sistema MediSys.

- A) 285
- B) 290
- C) 295
- D) 300
- E) Ninguna de las anteriores

**Desarrollo:**

______________________________________________________________________________

______________________________________________________________________________

______________________________________________________________________________

## 2. Factor de Complejidad Técnica

Determine el Factor de Complejidad Técnica del proyecto.

`TCF = 0,6 + 0,01 × Σ`

- A) 1,045
- B) 1,055
- C) 1,065
- D) 1,075
- E) Ninguna de las anteriores

**Desarrollo:**

______________________________________________________________________________

______________________________________________________________________________

______________________________________________________________________________

## 3. Factor de Ambiente

Calcule el Factor de Ambiente del sistema.

`EF = 1,4 − 0,03 × Σ`

- A) 0,845
- B) 0,875
- C) 0,905
- D) 0,935
- E) Ninguna de las anteriores

**Desarrollo:**

______________________________________________________________________________

______________________________________________________________________________

______________________________________________________________________________

## 4. UCP ajustado

¿Cuál es el valor de **UCP** (Puntos de Casos de Uso ajustados)?

- A) 248,73
- B) 254,82
- C) 260,91
- D) 267,00
- E) Ninguna de las anteriores

**Desarrollo:**

______________________________________________________________________________

______________________________________________________________________________

______________________________________________________________________________

## 5. Factor de Conversión

Determine el Factor de Conversión (**CF**) apropiado según los criterios de riesgo del proyecto.

- A) 20 horas-hombre/UCP
- B) 24 horas-hombre/UCP
- C) 28 horas-hombre/UCP
- D) 32 horas-hombre/UCP
- E) Proyecto no viable

**Desarrollo:**

______________________________________________________________________________

______________________________________________________________________________

______________________________________________________________________________

## 6. Factibilidad

Si el proyecto debe completarse en 6 meses con un equipo de 8 desarrolladores trabajando 160 horas al mes cada uno, ¿es factible según la estimación? Considere solo programación como el 40% del total.

- A) Sí, sobran 832 horas.
- B) Sí, sobran 375 horas.
- C) Sí, ajustado con 96 horas de margen.
- D) No, faltan 384 horas.
- E) Ninguna de las anteriores.

**Desarrollo:**

______________________________________________________________________________

______________________________________________________________________________

______________________________________________________________________________

## 7. Cambio de variables ambientales

Si se optimiza el equipo mejorando **E1 a 4, E3 a 4 y E5 a 5**, ¿cuál sería el nuevo esfuerzo total del proyecto en horas-hombre?

- A) 5.846
- B) 6.234
- C) 6.622
- D) 7.010
- E) Ninguna de las anteriores

**Desarrollo:**

______________________________________________________________________________

______________________________________________________________________________

______________________________________________________________________________

______________________________________________________________________________

---

# Caso 2: Sistema de Gestión Aeroportuaria Internacional "AeroControl"

El Consorcio Aeroportuario Internacional ha contratado a su empresa para desarrollar **AeroControl**, un sistema crítico de gestión aeroportuaria que integrará las operaciones de tres aeropuertos internacionales con un tráfico promedio de 500 vuelos diarios cada uno.

## Actores identificados

### APIs — actores simples: 4 sistemas

- Sistema meteorológico mundial.
- Base de datos de aeronaves ICAO.
- Sistema de reservas Amadeus.
- API de control de tráfico aéreo.

### Protocolos — actores medios: 5 sistemas

- SITA Type B Messaging.
- ACARS para comunicación con aeronaves.
- Protocolo radar ADS-B.
- Sistema ILS (Instrument Landing System).
- Protocolo AFTN de mensajería aeronáutica.

### Interfaces GUI — actores complejos: 12 usuarios

- Controladores aéreos de torre.
- Controladores de aproximación.
- Supervisores de operaciones.
- Personal de handling.
- Agentes de check-in.
- Personal de seguridad.
- Bomberos aeroportuarios.
- Personal de mantenimiento de pistas.
- Gestores de slots.
- Autoridades aeronáuticas.
- Pilotos (briefing).
- Pasajeros (información).

## Módulos y casos de uso

### Módulo Control Aéreo

- Gestión de aproximación: 18 transacciones.
- Control de torre: 22 transacciones.
- Gestión de pistas: 16 transacciones.
- Vectorización de aeronaves: 14 transacciones.
- Emergencias aéreas: 25 transacciones.

### Módulo Operaciones Tierra

- Asignación de gates: 11 transacciones.
- Handling de equipaje: 13 transacciones.
- Aprovisionamiento de combustible: 9 transacciones.
- Catering y limpieza: 7 transacciones.
- Push-back y remolque: 6 transacciones.
- Procedimientos de de-icing: 8 transacciones.

### Módulo Seguridad

- Control de accesos: 8 transacciones.
- Screening de pasajeros: 10 transacciones.
- Vigilancia perimetral: 14 transacciones.
- Gestión de incidentes: 17 transacciones.
- Auditoría de seguridad: 5 transacciones.

### Módulo Pasajeros

- Check-in múltiple: 9 transacciones.
- Control de inmigración: 11 transacciones.
- Información de vuelos: 4 transacciones.
- Gestión de conexiones: 13 transacciones.
- Servicios especiales: 7 transacciones.

### Módulo Gestión de Slots

- Asignación de slots: 15 transacciones.
- Optimización de capacidad: 19 transacciones.
- Gestión de delays: 12 transacciones.
- Coordinación CFMU: 10 transacciones.

## Factores técnicos

- T1=5: sistema altamente distribuido.
- T2=5: tiempo de respuesta crítico, menor a 1 segundo.
- T3=4: eficiencia de usuario crítica.
- T4=5: procesamiento complejo en tiempo real.
- T5=3: reutilización moderada.
- T6=1: instalación muy compleja.
- T7=2: usabilidad especializada.
- T8=5: portabilidad multiplataforma.
- T9=4: alta modificabilidad.
- T10=5: concurrencia masiva.
- T11=5: seguridad de nivel militar.
- T12=3: integración con terceros.
- T13=4: entrenamiento especializado.

## Factores ambientales — escenario base

- E1=2: familiaridad media-baja con el modelo.
- E2=1: poca experiencia en aviación.
- E3=3: experiencia media en orientación a objetos.
- E4=2: analista líder junior.
- E5=3: motivación media.
- E6=1: requisitos muy volátiles.
- E7=4: 30% del personal trabaja a tiempo parcial.
- E8=3: lenguaje de complejidad media.

## Factores ambientales — escenario optimizado

`E1=4, E2=4, E3=5, E4=5, E5=5, E6=3, E7=1, E8=2`

---

## 8. Comparación de escenarios

Analice comparativamente el escenario base y el escenario optimizado del equipo de desarrollo.

I. La reducción porcentual del Factor de Ambiente (EF) entre ambos escenarios es mayor al 36%.

II. El diferencial de productividad medido en UCP/persona-mes mejora en un factor superior a 1,57.

III. La reducción del esfuerzo total supera las 8.500 horas-hombre considerando el factor de conversión ajustado por riesgo.

- A) Solo I y II.
- B) Solo II y III.
- C) Solo I y III.
- D) Todas las afirmaciones son correctas.
- E) Ninguna afirmación es correcta.

**Desarrollo:**

______________________________________________________________________________

______________________________________________________________________________

______________________________________________________________________________

______________________________________________________________________________

## 9. Clasificación de casos de uso

Considerando la clasificación de casos de uso por transacciones, analice las siguientes afirmaciones:

I. El sistema tiene exactamente 8 casos de uso simples.

II. El módulo de Control Aéreo aporta 75 puntos al Factor de Peso de los Casos de Uso sin ajustar (UUCW).

III. La relación entre casos complejos y medios es 3,2.

- A) Solo I.
- B) Solo II.
- C) Solo III.
- D) I y III.
- E) Ninguna de las anteriores.

**Desarrollo:**

______________________________________________________________________________

______________________________________________________________________________

______________________________________________________________________________

## 10. Cálculo de Puntos de Casos de Uso

Analice las siguientes afirmaciones:

I. El Factor de Peso de los Actores sin ajustar (UAW) total es 50.

II. El Factor de Peso de los Casos de Uso sin ajustar (UUCW) está entre 350 y 400.

III. Los Puntos de Casos de Uso sin ajustar (UUCP) superan los 420 puntos.

- A) Solo I.
- B) Solo II.
- C) I y II.
- D) II y III.
- E) Todas son correctas.

**Desarrollo:**

______________________________________________________________________________

______________________________________________________________________________

______________________________________________________________________________

## 11. Complejidad de integración

Analice las siguientes afirmaciones:

I. Los 9 sistemas externos aportan 17 puntos al UAW.

II. Agregar un actor API aumenta el UUCP en menos del 1%.

III. La integración representa el mayor riesgo técnico del proyecto.

- A) Solo I.
- B) Solo II.
- C) I y II.
- D) Todas las afirmaciones son correctas.
- E) Ninguna afirmación es correcta.

**Desarrollo:**

______________________________________________________________________________

______________________________________________________________________________

______________________________________________________________________________

## 12. Impacto de la concurrencia y la seguridad

Analice las siguientes afirmaciones:

I. T10 y T11 en valor 5 agregan 0,10 al TCF.

II. Reducir ambos factores a 3 ahorraría más de 500 horas-hombre.

III. Son los factores técnicos de mayor peso en el sistema.

- A) Solo I.
- B) Solo II.
- C) I y II.
- D) I y III.
- E) II y III.

**Desarrollo:**

______________________________________________________________________________

______________________________________________________________________________

______________________________________________________________________________

## 13. Viabilidad económica

Analice la viabilidad económica del proyecto considerando un costo de **USD 75 por hora-hombre**.

I. Con el escenario base (equipo actual), el costo total del proyecto supera USD 1,19 millones.

II. El escenario optimizado (equipo capacitado) reduce el costo a menos de USD 550.000.

III. La inversión en capacitación del equipo se justifica si cuesta menos de USD 400.000.

- A) Solo I es correcta.
- B) I y III son correctas.
- C) I y II son correctas.
- D) Todas las afirmaciones son correctas.
- E) Ninguna afirmación es correcta.

**Desarrollo:**

______________________________________________________________________________

______________________________________________________________________________

______________________________________________________________________________

______________________________________________________________________________

---

# Hoja de respuestas

| Pregunta | Respuesta |
|---:|:---:|
| 1 | |
| 2 | |
| 3 | |
| 4 | |
| 5 | |
| 6 | |
| 7 | |
| 8 | |
| 9 | |
| 10 | |
| 11 | |
| 12 | |
| 13 | |
