# Solicitud de ajuste acotado de S5: clasificación de evidencia de jornada

Documento interno de coordinación D1 → D3. No integrar a la oferta técnica.
Fecha: 10 de octubre de 2026.

## Motivo y alcance

El plan maestro asigna S5 y su diccionario de datos a D3. Se solicita alinear su clasificación con S3, «Evidencia de jornada y veredicto de asignación» y con los oráculos de S9/T-17. No se solicita modificar S3 ni rediseñar el modelo completo de S5. D1 ya incorpora el contraste de esta interfaz a sus criterios de aceptación.

La versión compilada de S5, §5.1.5, Tabla 5.6, presenta seis niveles instrumentales: separa CAN y portería como niveles y ubica DECL_JUR en nivel 6. La Tabla 5.7 define nivel_cascada como un ENUM de seis niveles instrumentales. S3 utiliza niveles 1–5, reserva 0 al registro voluntario y trata la ausencia de fuente como estado distinto. Así, una atestación puede recibir códigos diferentes en arquitectura, datos y pruebas.

## Cambio solicitado

1. Sustituir la prelación y descripción de la Tabla 5.6 por el contrato canónico:

| Nivel | Evidencia | Condición de interpretación |
| --- | --- | --- |
| 1 | Tacógrafo digital descargado | Preservar original e identidad; aplicar controles de validez |
| 2 | Equipo a bordo con conductor identificado | No equiparar dato del vehículo a identidad personal ausente |
| 3 | Telemetría de fábrica, sólo lectura | Respetar permisos y cobertura efectiva |
| 4 | Reposo del camión, sin coordenadas | No acredita por sí solo el descanso personal |
| 5 | Atestación firmada del transportista | Asignación con marca y responsabilidad registrada, según S3 |
| 0 | Registro voluntario del conductor | Beneficio; nunca requisito ni veredicto |

2. Separar en el diccionario origen instrumental, nivel canónico, modalidad de adhesión y veredicto. Conservar códigos de origen útiles (CAN, GPS, portería, etc.) como fuentes, sin convertirlos en nuevos escalones. Un evento de portería puede complementar trazabilidad; no crea automáticamente un nivel de descanso. CAN instalado y telemetría de fábrica no son categorías intercambiables.
3. Ajustar el dominio de nivel_cascada en la Tabla 5.7 y en los anexos: 1–5 para la cascada; 0 exclusivamente voluntario. Ausencia de evidencia, código desconocido y evidencia inválida deben tener estados explícitos distintos de nivel 0. Definir nulabilidad y restricciones sin forzar valores ficticios en fuentes que carezcan de velocidad, odómetro o coordenadas.
4. Conservar las reglas de modalidad de S3: modalidad de datos exige atestación firmada que complemente el reposo; sin adhesión, la validación documental necesita atestación firmada para habilitar asignación con marca. La falta de fuente bloquea, con excepción únicamente según RN-04. Un incumplimiento legal bloquea siempre; el nivel 0 no cambia el resultado.
5. Revisar referencias, diagramas y diccionario que repitan la escala anterior. Preservar identidad, originales, huellas, rectificación auditable, custodia y retención. Si hay registros ya codificados, documentar la migración explícita del origen a nivel; no renumerarlos silenciosamente.

## Criterio de cierre

Entregar S5 y sus anexos corregidos, con una tabla de correspondencia origen → nivel → condición → veredicto. Cotejarla con S3 y con los casos CP-SYS-05 y CP-UAT-09 de T-17, incluidos los niveles 0 y 5, modalidad de datos, ausencia de atestación y bloqueo legal. Cualquier código que cambie el significado o el veredicto impide aceptar la integración.

La profundidad esperada es localizada: tabla de cascada, dominio del atributo, restricciones y referencias dependientes. Si la interfaz de implementación ya existe, debe corregirse también su contrato y mapeo. Este archivo constituye una solicitud; S5 permanece sin modificar por D1.
