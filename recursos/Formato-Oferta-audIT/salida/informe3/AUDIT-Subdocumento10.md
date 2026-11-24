# Subdocumento 10. Servicios de operación y niveles de servicio

audIT, Empresa N.º 10. Licitación TFEP-01/2026, Caso 10 Transporte de Carga. Oferta Técnica, Sobre N.º 2. Propuesta final. Archivo AUDIT-Subdocumento10.pdf.

## 10 Servicios de operación y niveles de servicio

> **Resumen de apertura.**
>
> Este subdocumento define cómo audIT opera el servicio entre los meses 21 y 56: quién atiende, en qué
> horario, con qué tiempos y cómo se mide. La flota rueda a toda hora, así que la atención es 24x7x365
> para todo contacto, y todo incidente que impida asignar un viaje, emitir un documento de transporte o
> recibir una emergencia es de severidad crítica (Caso, RT-21.06, p. 34). La mesa de servicio se dimensiona
> con el modelo Erlang C sobre 576 contactos al mes.
>
> **Qué recibe Transportes Curimón S.A.**
> - Una mesa de servicio 24x7x365 con un canal único de registro y cuatro niveles de atención, desde un centro de operaciones en Santiago.
> - Los niveles de servicio del FEP01, Artículo 78, p. 40 con una fórmula de medición única, abierta en tiempo real y exportable.
> - Un informe mensual de nivel de servicio dentro de los primeros cinco días hábiles de cada mes.
> - Libros de operación ejecutables por el personal de Curimón y una base de conocimiento mantenida durante todo el contrato.

La operación empieza en el mes 21, con la Etapa 2 en producción, y dura 36 meses. La mesa de servicio
existe desde el mes 16, porque desde ese mes un incidente que impida asignar ya es crítico, pero entre
los meses 16 y 20 la atiende la escuadra de estabilización con más personas (Subdocumento 7). Este
subdocumento describe el régimen estable. La sección 10.1 fija el modelo de soporte, la 10.2 los
niveles de servicio y cómo se miden, la 10.3 el tamaño de la mesa, la 10.4 los acuerdos internos y con
proveedores que sostienen esos niveles, la 10.5 los libros de operación y el conocimiento, y la 10.6 la
observabilidad que hace posible medir todo lo anterior.

## 10.1 Modelo de soporte

El modelo sigue las prácticas de ITIL 4 que una operación de este tamaño necesita: mesa de servicio,
gestión de incidentes, gestión de problemas, habilitación de cambios, gestión de niveles de servicio,
monitoreo y eventos, y gestión del conocimiento (AXELOS, 2019). El sistema de gestión del
servicio se alinea con la norma ISO/IEC 20000-1 (iso20000_1, ), que audIT ya usa en su
gobierno interno (Subdocumento 1). La Figura 10.1 muestra cómo viaja un contacto por los cuatro
niveles que define FEP02, numeral 21.3, p. 36.

\begin{figuraNativa}[!ht]{Niveles de atención, condición de escalamiento y equipo que atiende cada nivel}{10-niveles}
\begin{tikzpicture}[x=1mm,y=1mm,
  caja/.style={draw=audit-marino,line width=0.6pt,fill=white,rounded corners=2pt,align=center,
               text width=38mm,minimum height=16mm,inner sep=2pt,
               font=\sffamily\fontsize{9.5bp}{11bp}\selectfont\color{audit-tinta}},
  nota/.style={align=center,font=\sffamily\fontsize{9.5bp}{11bp}\selectfont\color{audit-tinta}},
  flecha/.style={-latex,line width=0.6pt,draw=audit-marino}]
  \node[caja,fill=audit-gris-claro] (u) at (0,0) {Conductores, torre, terminales, taller, transportistas y clientes};
  \node[caja] (n1) at (53,0) {**Nivel 1**  Mesa de servicio 24x7  paquete 13.1, 6 personas};
  \node[caja] (n2) at (106,0) {**Nivel 2**  Plataforma y aplicaciones  13.2 y 13.4, guardia 24x7};
  \node[caja,fill=audit-gris-claro] (m) at (106,30) {Monitoreo y alertas de la plataforma};
  \node[caja] (n3) at (106,-32) {**Nivel 3**  Desarrollo, datos  y arquitectura};
  \node[caja] (n4) at (53,-32) {**Nivel 4**  Fabricantes  y proveedores};
  \draw[flecha] (u) -- node[above,nota]{canal  único} (n1);
  \draw[flecha] (n1) -- node[above,nota]{sin  solución} (n2);
  \draw[flecha] (m) -- node[right,nota]{incidente  directo} (n2);
  \draw[flecha] (n2) -- node[right,nota]{cambio  de código} (n3);
  \draw[flecha] (n3) -- node[above,nota]{falla de  producto} (n4);
  \node[nota,align=left,anchor=north] at (0,-24) {Crítico: respuesta en  15 min y resolución en 4 h.  El nivel 1 resuelve el 70 %  en el primer contacto.};
\end{tikzpicture}
\end{figuraNativa}

El nivel 1 es la mesa de servicio del paquete 13.1. Recibe todo contacto, lo registra con número de
ticket y severidad, lo resuelve con la base de conocimiento cuando puede y, si no, lo deriva. Su meta es
resolver en el primer contacto al menos el 70 % de los casos, como exige FEP02, RT-21.06, p. 36. El
nivel 2 son los ingenieros de plataforma y de aplicaciones de los paquetes 13.2 y 13.4, que se turnan
en la guardia primaria y secundaria de ocho personas que justifica el Subdocumento 7. El nivel 3 reúne
a quienes construyeron el software y el diseño: desarrollo, datos y arquitectura. El nivel 4 son los
fabricantes y proveedores, y gestionarlo es responsabilidad de audIT sin que eso lo exima frente al
mandante (FEP02, numeral 21.3, p. 37). Los incidentes que detecta el monitoreo entran directo al nivel 2,
sin pasar por la mesa.

El centro de operaciones que pide FEP02, RT-21.01, p. 35 es el Centro de Operaciones Técnicas de audIT en
Santiago (Subdocumento 1). Atiende las 24 horas todos los días del año, con dos agentes en el relevo de
madrugada y uno en el resto del día, más la guardia de ingeniería. El gerente de servicio dedicado que
pide FEP02, RT-21.02, p. 35 es el Líder de Operación / SRE, Felipe Morales Cárdenas, que tiene dedicación
completa durante la operación (Subdocumento 12). El paquete 13.3 cubre el ciclo de vida del equipo a
bordo y los traslados a los cinco terminales, que están a más de 2.500 km entre sus extremos
(Caso, RT-21.16, p. 34). Los traslados van incluidos en la oferta, como exige el mismo requisito.

Los canales son un teléfono único, el portal de la mesa con autoservicio, un botón de ayuda en la
aplicación del conductor y el correo. Todos llegan al mismo registro, con número de ticket, severidad y
seguimiento hasta el cierre, como pide FEP02, RT-21.15, p. 37. El horario es 24x7x365 para todas las
severidades, más que el mínimo de 8:00 a 20:00 en días hábiles de FEP02, RT-21.07, p. 36, porque el Caso
lo exige sin excepción (Caso, RT-21.06, p. 34). Un ticket se cierra con la confirmación de la persona que lo
abrió o, si no responde, a los tres días hábiles de la solución, plazo que se declara conforme a
FEP02, RT-21.17, p. 37.

El escalamiento tiene dos ejes. El funcional pasa el ticket al nivel siguiente cuando el actual no puede
resolverlo, y el jerárquico avisa a quien decide según la severidad. Un incidente crítico se informa en
el acto al gerente de servicio y a la contraparte técnica de Curimón, y si a la hora no tiene solución
en curso, al Jefe de Proyecto. Un incidente alto se informa al gerente de servicio dentro de la hora.
Los medios y bajos siguen el flujo funcional.

## 10.2 Indicadores y niveles de servicio

La severidad sigue las cuatro clases del FEP01, Artículo 78.1, p. 40, con la regla del Caso para la crítica. Es
crítico todo incidente que impida asignar un viaje, emitir un documento de transporte o recibir un
evento de emergencia (Caso, RT-21.06, p. 34), y toda brecha que comprometa datos. Es alto un incidente que
degrada un proceso con alternativa costosa, como la posición al cliente con más de dos minutos de
atraso, el portal del transportista caído o un terminal sin enlace. Medio es una función no crítica con
alternativa, y bajo una consulta o un defecto menor.

audIT compromete los tiempos del FEP01, Artículo 78.2, p. 40 para cada severidad: respuesta en 15 minutos, 1 hora, 4
horas y 8 horas, y resolución en 4, 8, 24 y 48 horas, de la crítica a la baja. El informe de causa raíz
se entrega en 5 días hábiles para los críticos y en 10 para los altos. Todas las severidades se
atienden 24x7x365, también la media y la baja, que el artículo admite en horario hábil.

**Disponibilidad.**  La disponibilidad mínima mensual es 99,9 % para los servicios críticos y
99,5 % para los altos (FEP01, Artículo 78.2, p. 40). Los servicios críticos son cuatro: la asignación con
verificación bloqueante, la emisión del documento de transporte, la recepción de eventos de emergencia y
la ingesta de telemetría. Los altos son la publicación de posición al cliente, los portales del cliente
y del transportista y la liquidación. Un minuto cuenta como indisponible cuando la transacción sintética
del servicio falla en dos sondeos seguidos desde dos ubicaciones distintas, o cuando falla más del 5 %
de las transacciones reales de ese minuto. La disponibilidad del mes es
\[
D = 1 - \frac{\text{minutos indisponibles fuera de ventanas aprobadas}}{\text{minutos del mes}} .
\]
Con 30,4 días, el 99,9 % admite 43,8 minutos de indisponibilidad al mes y el 99,5 %, 3,6 horas. Las
ventanas de mantención aprobadas no cuentan, y las excedidas o no aprobadas sí (FEP01, Artículo 79.4, p. 41). Los
Subdocumentos 4, 5 y 9 usan esta misma definición: la disponibilidad se mide sobre la transacción de
negocio de extremo a extremo y no se deduce de la alta disponibilidad de un componente.

> **Compromiso C-01.** audIT mantiene cada mes la disponibilidad de los servicios críticos y altos medida con la fórmula de esta sección.
>
> Métrica: 99,9 % mensual en los cuatro servicios críticos y 99,5 % en los altos. Se verifica en: Informe mensual de nivel de servicio y medición propia del mandante. Fuente: FEP01, Artículo 78.2, p. 40 y Caso, RT-21.06, p. 34.

**Indicadores adicionales.**  audIT compromete también los del FEP01, Artículo 78.3, p. 40. El tiempo de
respuesta de la transacción crítica se mide en el percentil 95 contra los umbrales del
Caso, RT-09.01, p. 32: 30 segundos para asignar, 90 para emitir el documento, 15 para la emergencia y dos
minutos para la posición. El tiempo medio de restauración de los incidentes críticos no supera 4 horas
al mes. Los cambios fallidos no pasan del 5 % de los despliegues del mes. La prueba semestral de
recuperación cumple el RPO de 15 minutos y el RTO de 4 horas. No queda ninguna vulnerabilidad crítica
abierta fuera del plazo del FEP01, Artículo 21.1, p. 15. Una misma causa raíz no se repite más de una vez por
trimestre. La satisfacción con la mesa es 4,0 o más en escala de 1 a 5. La mesa cumple además lo de
FEP02, RT-21.06, p. 36: 80 % de los contactos atendidos antes de 20 segundos, 70 % resueltos en el
primer contacto y abandono de 5 % o menos.

La medición corre sobre la plataforma de observabilidad de la sección 10.6, con datos en tiempo real y
exportables para el mandante (FEP01, Artículo 79.1, p. 40), que puede medir por su cuenta (FEP01, Artículo 79.3, p. 41). El informe
mensual llega dentro de los cinco primeros días hábiles con cada indicador, los incidentes, sus causas
y el plan de acción (FEP01, Artículo 79.2, p. 40), y trae el análisis de tendencia que pide FEP02, RT-21.09, p. 36.

## 10.3 Dimensionamiento de la mesa de servicio

FEP02, RT-21.14, p. 36 pide dimensionar la mesa con teoría de colas o el modelo Erlang C a partir del
volumen de contactos del Caso, y el Caso, numeral 14.2, p. 30 pide estimar ese volumen y declararlo como
supuesto, separando personal interno, conductores y transportistas. El cálculo usa las poblaciones a
tres años del Caso, numeral 14.1, p. 29: 390 personas propias con acceso, 520 conductores, 175
transportistas y 100 clientes. Los contactos por persona al mes son un supuesto de audIT, porque el
Caso no los da: 0,4 del personal propio, 0,5 de los conductores, 0,8 de los transportistas y 0,2 de los
clientes. Los transportistas consultan más porque tratan con el portal, la liquidación y los permisos
de sus datos. El resultado son 576 contactos al mes, unos 19 al día.

Los contactos no llegan parejos. El supuesto reparte el 35 % en el relevo de madrugada, entre las 4:00
y las 8:00, cuando los conductores toman el camión en los terminales, el 55 % entre las 8:00 y las
20:00, y el 10 % en la noche. La hora punta de cada franja trae 1,5 veces su promedio. Cada contacto
de nivel 1 ocupa 8 minutos entre conversación y registro, y una persona espera en promedio 2 minutos
antes de colgar. La Tabla 10.1 da el resultado por franja en la hora punta.

**Tabla 10.1.** Nivel de servicio de la mesa por franja en la hora punta, con el modelo Erlang C

| Franja | Contactos por hora | Agentes | Esperan | Antes de 20 s | Abandono |
|---|---|---|---|---|---|
| Relevo de madrugada, 4:00 a 8:00 | 2,49 | 2 | 4,7 % | 95,6 % | 3,3 % |
| Día, 8:00 a 20:00, solo con la mesa | 1,30 | 1 | 17,4 % | 83,2 % | 14,4 % |
| Día, con desborde del nivel 2 | 1,30 | 2 | 1,4 % | 98,7 % | 1,0 % |
| Noche, 20:00 a 4:00 | 0,36 | 1 | 4,7 % | 95,4 % | 3,8 % |

*Fuente: elaboración propia con el guion de dimensionamiento de audIT. Umbrales de FEP02, RT-21.06, p. 36.*

La tabla muestra que un agente basta de noche, que el relevo necesita dos y que de día un agente solo
cumple los 20 segundos pero no el abandono, porque con 8 minutos por contacto quien espera suele
esperar más de lo que tolera. Por eso de día un ingeniero de nivel 2 de turno toma los contactos que
llegan con el agente ocupado. Ese desborde ocupa poco tiempo, porque solo uno de cada seis contactos del
día encuentra al agente ocupado.

Los puestos dedicados son uno durante las 24 horas y un segundo en el relevo de madrugada. Suman 851
horas al mes, que las seis personas del paquete 13.1, con 960 horas, cubren con un 11 % para
vacaciones, licencias y capacitación. Es la misma dotación del Formulario T-15.

El volumen de contactos es un supuesto, así que importa saber qué pasa si el real es mayor. La
Figura 10.2 muestra el abandono en la hora punta de cada franja cuando el volumen sube
hasta tres veces el supuesto, con la dotación de la Tabla 10.1.

\begin{figuraNativa}[!ht]{Abandono en la hora punta de cada franja según el volumen de contactos frente al supuesto}{10-sensibilidad}
\begin{tikzpicture}[x=1mm,y=1mm,
  t/.style={font=\sffamily\fontsize{9.5bp}{11bp}\selectfont\color{audit-tinta}},
  serie/.style={line width=1.1pt}]
  \foreach \v in {0,5,10,15,20,25} {
    \draw[audit-gris-claro,line width=0.4pt] (0,2*\v) -- (90,2*\v);
    \node[t,anchor=east] at (-1.5,2*\v) {\v %};
  }
  \draw[audit-filete,line width=0.6pt] (0,0) -- (90,0);
  \foreach \x/\l in {0/{1,0},22.5/{1,5},45/{2,0},67.5/{2,5},90/{3,0}} {
    \draw[audit-filete] (\x,0) -- (\x,-1.2);
    \node[t,anchor=north] at (\x,-1.6) {\l};
  }
  \node[t,anchor=north] at (45,-7) {Volumen de contactos, en veces el supuesto};
  \draw[audit-marino,line width=0.8pt,dash pattern=on 3pt off 2pt] (0,10) -- (90,10);
  \node[t,anchor=west] at (91,9.5) {Límite, 5 %};
  \draw[serie,audit-marino] (0,6.6) -- (22.5,14.4) -- (45,24.8) -- (67.5,37.6) -- (90,52.8);
  \node[t,anchor=west] at (91,52.8) {Madrugada, 2 agentes};
  \draw[serie,audit-turquesa] (0,7.6) -- (22.5,11.6) -- (45,15.4) -- (67.5,19.4) -- (90,23.4);
  \node[t,anchor=west] at (91,23.4) {Noche, 1 agente};
  \draw[serie,audit-tinta,dash pattern=on 1pt off 1.5pt] (0,2.0) -- (22.5,4.2) -- (45,7.2) -- (67.5,11.2) -- (90,15.8);
  \node[t,anchor=west] at (91,16.2) {Día, 2 con desborde};
\end{tikzpicture}
\end{figuraNativa}

La franja que primero se resiente es el relevo de madrugada. Con 1,5 veces el volumen, sus dos agentes
dejan un abandono de 7,2 %, sobre el límite de 5 %, y la noche llega a 5,8 %. El día aguanta más
porque tiene el desborde del nivel 2: con el doble del volumen sigue en 95,2 % antes de 20 segundos y
3,6 % de abandono. En todos los casos basta un agente más en la franja que falla. Con el doble del
volumen, un tercer agente de madrugada baja el abandono a 2,0 % y un segundo agente de noche lo deja en
0,3 %. Con 2,5 veces, el tercero de madrugada lo deja en 3,7 %. Entre los meses 16 y 20, cuando el uso
recién empieza y las consultas pueden llegar a 2,5 veces el supuesto, ese agente extra lo pone la
escuadra de estabilización del Subdocumento 7. Después el supuesto se revisa cada trimestre con el
volumen real, y se agrega un puesto en la franja que supere el 4 % de abandono dos meses seguidos.

El 30 % de los contactos que el nivel 1 no resuelve son unos 170 tickets al mes para el nivel 2, a los
que se suman los incidentes que abre el monitoreo. Los ocho ingenieros de los paquetes 13.2 y 13.4 los
atienden dentro de sus 1.280 horas mensuales, junto con la guardia y la mantención del Subdocumento 11.
En los meses 21 a 24 el paquete 13.2 dedica además unas 62 horas al mes, de seguridad y de plataforma,
a cerrar los paquetes 6.5 y 7.2 de la EDT, y le quedan cerca de 578 para la guardia y los tickets. El
Subdocumento 11 muestra cómo se reparte en esos meses la capacidad del paquete 13.4.

## 10.4 Acuerdos operacionales y contratos de apoyo

Un nivel de servicio externo solo se cumple si los plazos internos y los de los proveedores caben dentro
de él. Por eso cada acuerdo operacional entre niveles de audIT, y cada contrato de apoyo con un tercero,
se fija restando desde el plazo del FEP01, Artículo 78.2, p. 40.

Para un incidente crítico, la mesa registra y deriva en 5 minutos, y el ingeniero de guardia reconoce el
incidente en 10, de modo que la respuesta queda dentro de los 15 minutos. El nivel 3 se suma dentro de
30 minutos si la guardia lo pide, y el diagnóstico y la contención se buscan en la primera hora, para
dejar tiempo de solución dentro de las 4 horas. Para un incidente alto, la guardia reconoce en 30
minutos y el nivel 3 entra en 2 horas. El borrador de la causa raíz de un crítico está en 3 días hábiles,
y la revisión con el mandante cierra el plazo de 5. Los acuerdos se revisan cada mes con el informe de
nivel de servicio, y el que se incumple dos meses seguidos se corrige en el plan de acción.

Los contratos de apoyo son los de los proveedores clave del Sobre N.º 3. El soporte de Azure llega por la
condición de Microsoft CSP de audIT. El hardware crítico de San Bernardo y de los terminales debe tener
atención 24x7 y resolución en 4 horas (FEP02, numeral 8.4, p. 19). audIT lo cumple con los contratos de
soporte de los fabricantes y con los equipos de reposición que quedan en cada sitio: primero se cambia
el equipo y después se diagnostica el que falló. El tiempo de aire satelital lo da Ground Control y los planes de datos un operador móvil
elegido tras medir la cobertura. El circuito ExpressRoute tiene su proveedor en Santiago. Cuando un
proveedor no controla su plazo, como la red móvil en una zona de sombra, la continuidad no depende de
él: el equipo a bordo guarda 288 horas y los eventos críticos salen por satélite (Subdocumento 4).

La seguridad de la operación también tiene plazos fijos. Una vulnerabilidad se corrige en 7 días
corridos si es crítica, en 15 si es alta y en 30 si es media, contados desde su publicación
(FEP01, Artículo 21.1, p. 15). Una empresa independiente hace cada año una prueba de penetración, en junio y julio de
los meses 29 y 30, 41 y 42, y 53 y 54, y sus hallazgos entran al mismo flujo con esos plazos. El código
fuente, además de estar en el repositorio del mandante en cada liberación, se deposita cada seis meses
ante un agente de custodia independiente, como exige el FEP01, Artículo 84.6, p. 43. Los dos servicios son contratos
de apoyo de audIT y aparecen en el Formulario T-8.

## 10.5 Libros de operación y conocimiento

Cada alerta de la plataforma y cada procedimiento recurrente tiene su libro de operación: qué se
observa, cómo se confirma, qué se hace y cómo se vuelve atrás. Los primeros son los procedimientos que
el Subdocumento 4 ya declara: la conmutación a Brazil South y su vuelta, el paso de ExpressRoute a la
VPN, el terminal sin enlace durante 12 horas, la reconexión masiva tras una zona de sombra, la rotación
de certificados de los equipos y la actualización del equipo a bordo en el terminal. Los libros se
escriben en español, en formato editable, se versionan en el repositorio del mandante y son de su
propiedad (FEP02, RT-22.03, p. 38). Se prueban con el personal de Curimón antes de traspasarlos, porque
FEP02, RT-21.04, p. 35 exige que ese personal pueda ejecutarlos.

La base de conocimiento crece con cada ticket. Cuando un caso se resuelve, el agente registra la solución
o mejora el artículo que usó, y cada mes se revisan los artículos más consultados y los que no
resolvieron. Así el centro de soporte aprende de la operación, como pide FEP02, RT-21.10, p. 36, y la
base lleva métricas de uso y de utilidad percibida durante todo el contrato (FEP02, RT-22.08, p. 38). El
análisis mensual de tendencia de los tickets alimenta la gestión de problemas: un tipo de contacto que
crece se convierte en un problema con causa raíz, y su corrección pasa a la mantención del
Subdocumento 11.

El conocimiento también pasa a las personas de Curimón. Durante la operación audIT hace al menos dos
jornadas anuales de actualización y capacita sin costo al personal nuevo del mandante
(FEP02, RT-22.06, p. 38). Las jornadas caen en mayo y en octubre, fuera de la temporada de fruta, y el
programa anual de reinducción que audIT contrata cubre su preparación y su material. La versión de
entrenamiento con datos ficticios que el Subdocumento 6 prepara para la capacitación inicial se mantiene
en preproducción durante todo el contrato, para que el personal nuevo practique sin riesgo, que es lo
que valora FEP02, RT-22.09, p. 38. En los seis meses siguientes al paso a producción de la Etapa 2, del
mes 21 al 26, el equipo de audIT acompaña además al área de tecnología de Curimón en la operación diaria
(FEP02, RT-22.07, p. 38).

La automatización avanza por etapas. Un procedimiento que se ejecuta a mano más de cuatro veces al mes
pasa a un guion que el ingeniero lanza, y cuando el guion funciona sin intervención durante tres meses
pasa a ejecutarse solo ante la alerta. Los primeros candidatos son agregar unidades de IoT Hub cuando
el uso supera el 75 % de la cuota, reiniciar un consumidor de Event Hubs detenido y volver a enrolar el
certificado de un equipo a bordo. El avance se mide con el trabajo manual repetitivo del Subdocumento
11.

## 10.6 Observabilidad de extremo a extremo

La plataforma de observabilidad es la del Subdocumento 4: Azure Monitor, Log Analytics y Application
Insights, con una instrumentación única de trazas, métricas y registros, y retención de 12 meses en línea
y 24 en archivo. Cada mensaje del equipo a bordo lleva un identificador que lo sigue por IoT Hub, Event
Hubs, el servicio que lo procesa y la base que lo guarda. Así un evento de jornada que llegó tarde se
puede seguir desde la cabina hasta la torre.

Los cuatro servicios críticos tienen una transacción sintética que corre cada minuto desde dos
ubicaciones, y es la que mide la disponibilidad de la sección 10.2. Las alertas no se disparan por
umbrales fijos de cada componente sino por el consumo del presupuesto de error de cada servicio
(Beyer et al., 2016). Si en una hora se consume el 2 % del presupuesto del mes, se llama a la guardia,
y si en seis horas se consume el 5 %, se abre un ticket. Con 43,8 minutos de presupuesto al mes, el
primer umbral salta con menos de un minuto de caída real.

La correlación agrupa las alertas por la topología: región, servicio y componente. Si cae el circuito
ExpressRoute, la conmutación a la VPN es esperada y se registra como un solo incidente, no como una
alerta por cada servicio que tardó un minuto. La detección también es proactiva. El monitoreo de la
flota avisa cuando un camión que debía reportar no reporta, cuando un equipo pierde el satélite o cuando
un terminal pasa a su enlace de respaldo, antes de que alguien llame a la mesa. Es lo que pide el
análisis de modos de falla del Formulario T-16, que identificó la detección tardía como el punto débil
del equipo a bordo.

Los tableros de indicadores y de soporte están abiertos para el mandante según su rol, como pide
FEP02, RT-21.13, p. 36: la gerencia ve los niveles de servicio, la contraparte técnica los incidentes y
las tendencias, y el área de tecnología de Curimón el detalle de cada componente.

## Referencias

AXELOS. (2019). *ITIL Foundation: ITIL 4 Edition*. TSO.

Beyer, B., Jones, C., Petoff, J. y Murphy, N. R. (Eds.). (2016). *Site Reliability Engineering: How Google Runs Production Systems*. O'Reilly Media. https://sre.google/sre-book/being-on-call/

International Organization for Standardization. (2018). *Information technology --- Service management --- Part 1: Service management system requirements*. https://www.iso.org/standard/70636.html

Transportes Curimón S.A. (2026). *Bases administrativas para la preparación de la propuesta: Licitación Pública Internacional N.º TFEP-01/2026* (Documento FEP01).

Transportes Curimón S.A. (2026). *Bases técnicas del Caso 10, Transporte de Carga: Licitación Pública Internacional N.º TFEP-01/2026* (Documento FEP03).

Transportes Curimón S.A. (2026). *Bases técnicas transversales para la preparación de la propuesta: Licitación Pública Internacional N.º TFEP-01/2026* (Documento FEP02).

## Declaración de uso de IA

Conforme al Comunicado 10, sección 7.2, cada sección de este subdocumento y cada formulario asociado declara la herramienta de inteligencia artificial generativa usada, su finalidad, el nivel de uso en texto y en diagramas según la escala oficial de esa sección, y quién revisó y qué verificó. Esta declaración se consolida en el Formulario A-6.

| Sección | Herramienta | Finalidad del uso | Nivel en texto | Nivel en diagramas | Revisión humana (quién y qué verificó) |
|---|---|---|---|---|---|
| Introducción y 10.1 | Claude Opus 5.5 en Claude Code | Redacción inicial del modelo de soporte desde las bases, el Formulario T-15 y el Subdocumento 7, y diagrama de niveles dibujado en TikZ desde el modelo definido por el equipo | Alto | Medio | Naomi Núñez, Líder de Calidad, e Ignacio Vera y Marcel Gutiérrez, Arquitectos de Solución: niveles, centro de operaciones, gerente de servicio, canales, horario y escalamiento frente a FEP02, capítulo 21, y al Caso. |
| 10.2 | Claude Opus 5.5 en Claude Code | Redacción inicial de la severidad, los niveles de servicio y la fórmula única de disponibilidad, conciliada con los Subdocumentos 4, 5 y 9 | Alto | Ninguno | Naomi Núñez, Líder de Calidad, e Ignacio Vera y Marcel Gutiérrez, Arquitectos de Solución: valores del Artículo 78, servicios críticos y altos, fórmula y su coherencia con los otros subdocumentos. |
| 10.3 | Claude Opus 5.5 en Claude Code | Guion del modelo Erlang C con supuestos declarados, cálculo de sensibilidad al volumen, gráfico dibujado en TikZ con sus resultados y redacción inicial del dimensionamiento, con la conciliación de capacidad del Informe 3 | Alto | Medio | Naomi Núñez, Líder de Calidad, e Ignacio Vera y Marcel Gutiérrez, Arquitectos de Solución: supuestos de volumen, cálculo reproducible, lectura del gráfico, coherencia con las seis personas del Formulario T-15 y horas del paquete 13.2 en los meses 21 a 24. |
| 10.4 a 10.6 | Claude Opus 5.5 en Claude Code | Redacción inicial de los acuerdos internos y con proveedores, la seguridad de la operación, los libros, el conocimiento, la capacitación y la observabilidad desde el Subdocumento 4, las bases y el calendario de calidad y capacitación del Informe 3 | Alto | Ninguno | Naomi Núñez, Líder de Calidad, e Ignacio Vera y Marcel Gutiérrez, Arquitectos de Solución: plazos internos dentro del Artículo 78, plazos del Artículo 21.1, meses de la prueba de penetración y del depósito de fuentes, jornadas del RT-22.06 y procedimientos frente al Subdocumento 4. |
