# Guion oral · Revisión 2 · cinco expositores

**Duración prevista:** 14:29 de exposición + 0:31 de margen, seguidos por 15 minutos de preguntas. Es una pauta para ensayar, no una medición de duración. Expositor 1–5 identifica la distribución interna; la presentación corporativa conserva roles y códigos.

| Voz | Diapositivas | Tramo previsto | Tema |
| --- | --- | --- | --- |
| Expositor 1 | 1–7 | 0:00–3:28 | Problema, correcciones y arquitectura lógica |
| Expositor 2 | 8–11 | 3:28–5:53 | Arquitectura física, datos y desconexión |
| Expositor 3 | 12–15 | 5:53–7:51 | EDT, diccionario y cobertura |
| Expositor 4 | 16–19 | 7:51–10:56 | Red, G13, transición y capacidad |
| Expositor 5 | 20–26 | 10:56–14:29 | Riesgos, reservas y cierre |

Las indicaciones entre **[corchetes]** son para ensayar; no se pronuncian. Los relevos siguen la tabla. Los separadores introducen actos. La lámina 3 expone las correcciones; sus marcas de observación y R10 amplían la evidencia cuando se requiera. Las cifras de desempeño y riesgo conservan su condición de diseño o estimación.

## Expositor 1 · 0:00–3:28

**Diapositiva 1 · Portada · 15 s**

«Buenos días. Presentamos la segunda revisión de nuestra propuesta para Transportes Curimón. Revisaremos las correcciones del primer informe, los riesgos de la solución y del proyecto, y cómo la EDT y los hitos gobiernan la ejecución.»

**Diapositiva 2 · Salida segura · 25 s**

«Partimos de una decisión operacional: un viaje no debe liberarse solo porque el camión esté listo. La salida exige tres evidencias vigentes: conductor habilitado, vehículo conforme y documento íntegro disponible en cabina. [Revelar cada control.] Si alguna falla, la orden queda bloqueada. Ese es el problema que organiza el resto de la solución.»

**Diapositiva 3 · Cambios principales del Informe 2 · 40 s**

«Seleccionamos cinco cambios principales respecto del primer informe. [Requisitos y arquitectura.] El catálogo ahora traza 42 requisitos hasta pruebas diseñadas, y la arquitectura define esquema, capas y equipos. [Revelar legado y capacidad.] Resolvimos el futuro del sistema de 2013 mediante sustitución gradual y consulta hasta M24. También derivamos la memoria y la capacidad de reconexión. [Revelar innovaciones.] Reformulamos las innovaciones 2 y 3 y entregamos las cinco fichas. La matriz del Artículo 46 conserva el detalle. Las pruebas siguen pendientes de ejecución. Ahora profundizamos en la solución.»

Referencia para preguntas: observaciones 01/38/45/48, S3 §3.2.8 y T-12/T-17; 37/53/64/65, S3 §3.3 y S4 §§4.1.3/4.2 con T-11; 43, S3 §3.2.4; 73/74, S4 §§4.2.2/4.2.8 y CP-PERF-02; 88–91, S13 §§13.2–13.3 y T-19. Se priorizaron decisiones de alcance, viabilidad y verificación. La selección no acredita cierre de las 100 observaciones. La innovación 2 programa intervenciones por oportunidad de patio y la 3 conecta el semirremolque. El ERP contable se conserva como emisor tributario; M16 y M21 marcan la sustitución por funciones del sistema de gestión.

**Diapositiva 4 · Separador: Qué construimos · 3 s**

[Transición de acto: avanzar al terminar la frase anterior.]

**Diapositiva 5 · Contexto y tres planos · 40 s**

«[Nube.] El núcleo vive en Chile Central, en tres zonas; Brazil South queda para recuperación. [Sitios.] San Bernardo sostiene la torre y la integración con el contable, único emisor. Cada terminal tiene dos nodos y respaldo 5G. [Flota.] Los 182 camiones audIT conviven con 192 de terceros que conservan sus equipos; acceder a sus datos exige autorización y factibilidad por proveedor. [Componentes.] Son 39: 24 en la región primaria, uno en la secundaria y 14 fuera de la nube.»

**Diapositiva 6 · Arquitectura lógica · 45 s**

«Recorrer la pila. [Capas.] Portales Next.js y app Flutter; Front Door como borde público; API Management; seis contextos de negocio en AKS sobre .NET; IoT Hub y Event Hubs para ingesta; y persistencia según cada dato. [Transversales.] Entra ID y Key Vault aportan seguridad, Azure Monitor observabilidad. [Contextos.] Cada contexto decide sobre su negocio y sus datos: Planificación pregunta a Personas y Flota. Sus nombres coinciden con los paquetes 5.1 a 5.6 de la EDT.»

**Diapositiva 7 · Verificación en 30 s · 40 s**

«Seguir una petición real por la pila. [Solicitud.] La torre pide asignar conductor, tracto, semirremolque y carga. [Invariantes.] Planificación evalúa en paralelo tres condiciones y pregunta a quien es dueño de cada dato: Personas, Flota y el documento del contable. Una causa legal bloquea siempre, y el rechazo explica por qué. [Presupuesto.] El Caso da 30 segundos: dos para identidad, ocho para las tres evaluaciones en paralelo, ocho para reservar y confirmar, cuatro para veredicto y auditoría, tres para responder, y cinco de margen. [Cierre.] Ojo: es un reparto de diseño, todavía sin medición.»

## Expositor 2 · 3:28–5:53

**Diapositiva 8 · Arquitectura física · 40 s**

«[Nube.] Chile Central concentra producción; el esquema identifica sus dos redes. Brazil South es recuperación: RPO de 15 minutos y RTO de cuatro horas. [Enlaces.] El camión llega por LTE o Iridium a IoT Hub de Chile Central. San Bernardo usa ExpressRoute de 100 Mbit/s y VPN; terminales, enlace fijo y 5G. [Energía.] Fuentes y adaptadores A/B en circuitos distintos en San Bernardo. Cada terminal tiene dos fuentes y un módulo por cada bus de 24 y 48 V: UPS más otro circuito del tablero. [Cierre.] El mandante compra el hardware de T-11. Los cinco ambientes se construyen desde el mismo código.»

**Diapositiva 9 · El camión · 35 s**

«[Equipo.] El iWave G26I ejecuta Linux y conserva datos localmente. [Periféricos.] CANCrocodile lee sin cortar el arnés, sujeto a autorización y homologación. MIFARE identifica al conductor detenido. Iridium cubre la falta de señal y la baliza identifica el semirremolque. [Memoria.] La observación 73 se responde derivando 2.374 MB; la configuración mínima elegida es de 8 GB. El búfer de 288 horas ocupa 38,4 MB y cubre el escenario de cierre fronterizo.»

**Diapositiva 10 · Datos · 35 s**

«[Dominios.] PostgreSQL confirma asignaciones; SQLite captura a bordo; TimescaleDB conserva telemetría. La caché nunca habilita con una copia vieja. Documentos y auditoría quedan inmutables y la analítica se separa del despacho. [Volumen.] Se dimensionan 96 mil viajes y cerca de 120 millones de posiciones al año. [Migración.] Las aproximadamente seis mil vigencias requieren verificación documental individual y respaldo custodiado. El hash comprueba integridad; nada en cuarentena habilita despacho.»

**Diapositiva 11 · Sin enlace · 35 s**

«[Autoridad.] Una asignación nueva requiere estado autoritativo en Azure. El documento tributario lo emite únicamente el contable de San Bernardo, mediante la integración. [Autonomía.] San Bernardo y terminales sostienen 24 horas de funciones locales. El camión conserva 72 horas como mínimo contractual y 288 por diseño. [Reconexión.] Los lotes se deduplican y se liberan con acuse duradero. CP-PERF-02 define la prueba con 300 camiones tras 72 horas, incluyendo transferencia, persistencia y conciliación. Su ejecución sigue pendiente.»

## Expositor 3 · 5:53–7:51

En el Informe 2, S7 pesa 15 %. Señalar el árbol y los criterios, sin recitar los 54 paquetes.

**Diapositiva 12 · Separador: Cómo lo ejecutamos · 3 s**

[Transición de acto: avanzar al terminar la frase anterior.]

**Diapositiva 13 · EDT, niveles 0 y 1 · 35 s**

«La EDT parte de una plataforma de control de jornada, flota y viaje. [Primer nivel.] Se divide en trece elementos orientados a entregables. [Paquetes.] Contiene 54 paquetes estimables y asignables: servicios, integraciones, datos, calidad, implantación, innovaciones y operación. [Cobertura.] La regla del 100 % exige que los hijos cubran el trabajo del padre sin vacíos ni doble conteo. La aceptación de cada paquete se concreta en T-14.»

**Diapositiva 14 · EDT, nivel 2 · 40 s**

«[Árbol completo.] Los 54 paquetes conectan construcción y operación. Los seis contextos corresponden a 5.1 Personas, 5.2 Flota, 5.3 Planificación y 5.4 a 5.6 Telemetría, Fletes y Costeo. El portal ocupa 5.7. [Trazabilidad.] Las cinco innovaciones se ubican en 12.1 a 12.5 y conservan sus fichas T-19. La adhesión tiene paquetes, responsable y riesgo propios. El elemento 11 produce las evidencias de capacitación, marcha blanca, aceptación y traspaso.»

**Diapositiva 15 · Diccionario y regla del 100 % · 40 s**

«Tomemos el paquete 11.2 del T-14. [Entregable.] Marcha blanca y paso a producción E1. Se acepta con las seis condiciones del Artículo 17.3 en H6 y H7. [Responsable.] El Líder de Implantación responde por A15 y A19, meses 13 a 16. [Traza.] La observación 48 conecta RNF-011, paquete 11.2 y casos CP-INT-05 y CP-SYS-05. La cobertura se contrasta con 42 requisitos, seis contextos, cinco innovaciones y las once exigencias del Caso.»

## Expositor 4 · 7:51–10:56

**Diapositiva 16 · Carta Gantt y dependencias · 65 s**

«[Barras.] La red tiene 25 actividades y G13, del día cero al 420. [Dependencias.] A12 espera migración, construcción, integraciones y piloto. El adelanto A09 hacia G13 y A13 es de diez días, condicionado a una versión lista. [Ruta.] Trece actividades críticas incluyen A14 y A23. Sin consumir reservas, un atraso se propaga; el siguiente ejemplo muestra cómo cambia ese resultado al usarlas. [Hitos.] Los rombos indican posición planificada. Los porcentajes redondeados miden cumplimiento del límite contractual en Monte Carlo de S8. A12 se planifica al día 226, pero su 96,2 % corresponde al límite 240. La holgura interna no cambia ese límite.»

**Diapositiva 17 · ¿Y si A09 se atrasa? · 40 s**

«Este escenario es determinista, sin nueva simulación. [Atraso.] Diez días adicionales en A09 llevan su término al día 202: H4 queda dos días tarde. A12 termina el 236 y A14 baja de 14 a cuatro días. [Resultado.] H5 y el inicio fijo de H6 se conservan en el límite 240. A13 termina el 232, ocho días antes. Consumir la reserva protege la marcha blanca, sin corregir el incumplimiento de H4. El consumo superior al 50 % activa R-16 y el hito tardío permanece bajo R-17.»

**Diapositiva 18 · Paquete 11.1 y G13 · 35 s**

«Un ejemplo es el paquete 11.1, capacitación operacional. Su entregable es la capacitación de torre, terminales y conductores. Se acepta con G13 disponible antes de A13 y con los usuarios certificados. [Seguir la secuencia.] G13 requiere una versión probada en PREPROD, datos ficticios y material por perfil antes de iniciar A13. A13 contempla 40 días hábiles: diez de familiarización y treinta de práctica y evaluación. Si G13 no está aceptada, la capacitación no comienza. La reserva A14 protege la red, pero no elimina esta precedencia.»

**Diapositiva 19 · Transición en dos etapas · 45 s**

«[Etapas.] E1 entra a marcha blanca en M13–M15 y a producción en M16; E2 hace marcha blanca M19–M20 y se acepta en M21. [Capacidad.] En M13–M15 son 37 personas: 21 de planta y 16 de refuerzo. La capacidad se divide en 21,5 FTE E1, 14,1 E2 y 1,4 de coordinación. Seguridad e Integración son dos roles distintos de un FTE: cada uno aporta 0,4 a E1, 0,4 a E2 y 0,2 a coordinación. [Legado.] Se sustituye por funciones en M16 y M21, conserva consulta hasta M24 y el contable sigue como emisor. La operación continúa hasta M56.»

Para preguntas de capacidad: T-15 separa ambos roles y deja 1,4 FTE total de coordinación entre siete roles compartidos; no se suma otra vez a la dotación. En M19–M20, S7 prevé 26 personas; 16 integran operación desde M21.

## Expositor 5 · 10:56–14:29

**Diapositiva 20 · Separador: Cómo lo protegemos · 3 s**

[Transición de acto: avanzar al terminar la frase anterior.]

**Diapositiva 21 · Mapa de calor P×I · 45 s**

«Partir por el panorama completo. [Mapa.] Probabilidad por impacto, de 1 a 5; el color sigue la escala del S8. [Riesgos.] Los 28 riesgos del T-16 en su celda inicial: la mayoría se concentra en exposición media; siete quedan en alta, y uno, el R-06, llega a 15. [Antes y después.] Después de mitigar, ninguno queda en alta. [Cierre.] Las categorías: técnicos, contrapartes, gestión, ciberseguridad y continuidad. Lo residual es una estimación, no una medición.»

**Diapositiva 22 · Riesgos de exposición alta · 45 s**

«[Riesgos altos.] R-06 se evita usando Managed Redis desde el diseño. R-11 exige al menos 60 de los 148 transportistas al corte M9; con 59 o menos se refuerza la adhesión. [Seguridad.] R-23 trata el portal expuesto. Para R-24, la réplica en Brazil South exige base de licitud, aprobación y cláusulas firmadas antes de H2. [Operación.] Se agregan la marcha blanca en temporada, el bloqueo indebido y R-28. Las exposiciones posteriores a mitigar son estimadas.»

**Diapositiva 23 · Corbatín de R-28 · 45 s**

«[Evento.] El documento completo no vuelve a cabina en 90 segundos. [Controles.] Sin LTE se utiliza Iridium. Si la carga se conoce solo en terreno, se solicita al contable por satélite; la preemisión sirve cuando ya se conoce antes. Un documento grande se fragmenta y reensambla; las pérdidas requieren acuse íntegro y reintentos dentro del plazo. El ensayo M3 comprueba esas barreras con el peor documento. [Respuesta.] Sin documento conforme no hay salida. Si el ensayo falla, se revisa el diseño antes de operar ese camino. El AMFE contiene diez modos con NPR estimado bajo 50.»

**Diapositiva 24 · Reservas y holguras · 50 s**

«[Reservas.] A14 aporta 14 días y A23 diez. S7 usa PERT por cadenas: 97,9 % y 97,6 %, con 95,6 % conjunto. [Red completa.] S8 incorpora rutas convergentes y capacitación en diez mil corridas: H6 alcanza 96,2 %, H11 95,5 % y ambas fechas se cumplen en 92,1 %. Son modelos distintos; para hablar de la red completa se usa este último. [Control.] Una reserva bajo la mitad, con más de la mitad de cadena pendiente, se eleva al Comité. Las holguras de las rutas no críticas absorben variaciones dentro del plan, pero no permiten mover los hitos contractuales.»

Fuente: S7 §7.3.1 para PERT por cadenas y S8, simulación de cronograma, para la red completa. El 95,6 % y el 92,1 % no son resultados intercambiables. No se modifica el LaTeX de esas fuentes.

**Diapositiva 25 · Tres compromisos · 20 s**

«Proponemos una arquitectura híbrida, 54 paquetes verificables y 28 riesgos tratados. Las reservas protegen la ejecución. Los 120 casos de prueba están diseñados y su ejecución corresponde a la fase contractual. Gracias.»

**Diapositiva 26 · Preguntas · 5 s**

«Gracias. Abrimos las preguntas y la discusión.»

[En preguntas, B abre respaldos; número y Enter seleccionan R1–R21; Escape vuelve al punto de la exposición.]

## Ensayo y preguntas

Ensayar con cronómetro, cinco relevos y revelaciones; repetir en el proyector disponible. La pauta deja 31 segundos de margen. Recortar ejemplos secundarios si es necesario, conservando condiciones y unidades. Las pruebas T-17 están diseñadas, no ejecutadas. Las exposiciones residuales y probabilidades son estimaciones del modelo. Los meses son contractuales y febrero de 2027 es el supuesto de calendario.

Para responder: conclusión, evidencia y localizador del informe. El respaldo conserva calendarios por innovación, los seis pasos de reversión y los criterios completos del diccionario. La presentación no acredita por sí sola cierre de las 100 observaciones ni resultados de campo.
