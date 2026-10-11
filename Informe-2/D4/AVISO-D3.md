# Aviso de la dupla 4 a la dupla 3: integración de su 4.1 al Subdocumento 4

Fecha: 11 de octubre de 2026. Afecta a `subdocumento_04_1_arquitectura_logica.md` (commit eef2475), a su S5 y a su S6.

La dupla 4 integró al Subdocumento 4 del formato su versión de la arquitectura lógica, que se sobrepone a
la anterior. No se tocó ningún archivo de la dupla 3. Se pide revisar los cambios de abajo y corregir lo
que corresponda en sus archivos, para que el S4, el S5 y el S6 digan lo mismo.

## Lo que se cambió al integrar y por qué

1. **Versiones del 4.1.1.** «.NET 8 LTS / Go 1.22+» con soporte hasta noviembre de 2026 no cumple el
   FEP02, numeral 1.6, p.5, que pide soporte vigente y hoja de ruta por los 56 meses. Además, Go 1.22 ya no
   tiene soporte. La tabla quedó así:
   - .NET 10 LTS, con soporte hasta el 14-11-2028;
   - Go 1.27, porque Go mantiene sus dos versiones mayores más recientes;
   - PostgreSQL 16, con soporte hasta el 09-11-2028;
   - para los tres, un plan de actualización dentro del contrato.

   Fuentes: dotnet.microsoft.com, go.dev y postgresql.org, consultados el 2026-10-10.
2. **Caché.** Azure Managed Redis se usa desde la Etapa 1, y no como una transición desde un «SKU de origen
   por confirmar». La solución es nueva, Microsoft retira Enterprise el 31-03-2027 y Basic, Standard y
   Premium el 30-09-2028, y recomienda migrar sin esperar. Azure Managed Redis está en Chile Central y en
   Brazil South según la API de precios de Azure. **Hay que alinear el S5** (5.2 y 5.4), que todavía habla
   de una migración programada.
3. **Concurrencia.** Se adopta 380 sesiones, 570 en estrés, y se quitó la nota «D3 y D4 deben acordar».
   La 4.2 de la dupla 4 ya usa 380.
4. **Respuestas del Art. 46.** Las respuestas 53 a 63 de su tabla decían «no se acredita en este lote» y
   «su cierre requiere examen». Se reescribieron apuntando a la sección del S4 donde quedó resuelta cada
   observación. La 65 decía «Apache Kafka en clúster Strimzi sobre AKS», pero su 4.1.1 dice Event Hubs.
   Quedó Event Hubs con protocolo Kafka.
5. **Secuencias.** Las tres figuras 4-3, 4-4 y 4-6 se usan en una copia corregida, en
   `D4/graficos-v2/fuente/s4_secuencias.py`, con estos cambios:
   - sin título dentro de la figura;
   - «sistema contable» en lugar de «ERP 2013», porque el Caso (cap. 5, p.12) separa el sistema de gestión
     de 2013 del sistema contable;
   - el presupuesto de la tabla 4-presupuesto (10, 450 y 200 ms, bajo 2 s), en lugar de «25 s + 5 s»;
   - sin «el token autoriza el arranque del motor» ni «inmovilización», porque el bus del vehículo es de
     solo lectura (restricción 6).
6. **Citas.** RT-26.07 está en la p.45 del FEP02, no en la 44. RT-13.08 está en la p.33 del Caso, no en la
   32. WCAG está en el Art. 4.3, p.6, del FEP01.
7. **Tablas.** Las de tipo «concepto y descripción» (capas, contextos, campos del error, piezas de la capa
   anticorrupción, parámetros de la telemetría) siguen como texto, porque el Comunicado 10, sección 5.2, no
   las acepta en el cuerpo. El contenido es el suyo.
8. **Frases sin respaldo.** Se quitaron «cero detenciones de flota en faenas mineras o agrícolas» y el
   nivel «FIPS 140-2 Nivel 3» de Key Vault Premium, que no se pudo verificar.

## Lo que queda de su lado

- Declarar en el S4 la herramienta y el nivel de IA del texto del Informe 1 (filas 4.1 a 4.1.19) y firmar
  su revisión humana, también la de 4.1.20 y 4.1.21 (OpenAI Codex).
- **S6, línea 146.** Habla de tres suscripciones (Desarrollo, Pruebas/Staging y Producción). El S4 tiene
  cinco ambientes, cada uno en su suscripción: desarrollo, QA, preproducción, producción y recuperación.
- **S6, línea 193.** La declaración de IA trae un nombre real con cargo. El Comunicado 10 lo prohíbe: la
  autoría va solo por código de dupla.
- **Filas 73 y 74 de su tabla.** Recalculan el almacenamiento y la reconexión con otras cifras (2.400 MiB,
  71.400 paquetes en 11,9 min). Son de la parte física de la dupla 4, que mantiene sus cálculos aprobados:
  2.374 MB y 57.600 mensajes en 9,6 min. Si tienen una observación al cálculo, conviene revisarla juntos.

## Integración de la versión del 11 de octubre (commit f86e240)

La dupla 4 integró al Subdocumento 4 la versión nueva completa, con sus 26 subsecciones. El punto 5 de
arriba ya no aplica: el S4 usa ahora su presupuesto de 25 s más 5 s y sus figuras nuevas. Al integrar se
cambió lo siguiente, sin tocar sus archivos:

1. **Figuras.** Las secuencias 4-3, 4-4, 4-6 y 4-7 y el documento sin cobertura se usan desde una copia en
   `D4/graficos-v2/fuente/s4_secuencias.py`, sin el título interno (lo da la leyenda) y sin punto y coma en
   las notas. LogicaCapas se usa tal cual.
2. **Notas de trabajo.** Se quitaron la fila «S4.2 de D4 mantiene 350 (525 en estrés)» de la tabla 4.19, que
   ya no es cierta (la 4.2 usa 380 y 570), y las menciones a duplas en fuentes de figuras y en 4.1.1.
3. **Citas.** RT-05.29 está en la p.32 del Caso. El numeral 16.1 del Caso son las decisiones de diseño
   pendientes, así que no respalda la compatibilidad del equipo con la carga (tabla 4.9). El Art. 4.3 del
   FEP01 está en la p.6. RT-26.07 sigue en la p.45 del FEP02.
4. **Tablas.** La de campos del rechazo (4.11) pasó a texto. Las demás quedaron con una frase por celda.
5. **Parte física.** Para que calce con su 4.1, la 4.3.2 ya no dice que el terminal asigna con la copia local:
   sin enlace, el viaje nuevo lo asigna la torre en el sistema central. El S8 sumó el riesgo R-28 (retorno
   satelital del documento sobre 90 s), que es el acuerdo pendiente entre D2, D3 y D4.

