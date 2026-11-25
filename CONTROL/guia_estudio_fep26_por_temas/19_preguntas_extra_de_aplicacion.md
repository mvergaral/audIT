> Estas preguntas incluyen respuestas orientativas junto a cada enunciado. Úsalas como repaso guiado: intenta responder antes de leer la solución.

# Preguntas extra de aplicación por tema

## 37. Arquitectura

¿Por qué arquitectura no es simplemente dibujar cajas?  
**Respuesta:** porque documenta decisiones estructurales, responsabilidades, relaciones y consecuencias que determinan calidad, costo y riesgo. Un diagrama sin justificación no permite evaluar alternativas.

## 38. Monolito o microservicios

NexoSalud tiene seis personas y ocho meses. ¿Qué elegirías?  
**Respuesta:** normalmente monolito modular, por menor costo operativo y coordinación. Microservicios se justifican si existen dominios/equipos independientes o escalado desigual que compensen red, observabilidad y despliegue distribuido.

## 39. Eventos

¿Para qué parte de SaludConecta usarías arquitectura orientada a eventos?  
**Respuesta:** notificaciones y auditoría, donde se tolera asincronía y conviene desacoplar. Deben manejarse duplicados, orden, idempotencia y seguimiento.

## 40. Resiliencia

Compara timeout, reintento y circuit breaker.  
**Respuesta:** timeout limita espera; reintento repite una falla transitoria con backoff; circuit breaker deja de invocar un servicio persistentemente fallido. Reintentar sin límite puede agravar una caída.

## 41. Lógica y física

¿Cuál es la diferencia entre una capa y un nodo?  
**Respuesta:** capa es separación lógica de responsabilidad; nodo es ubicación de ejecución. Varias capas pueden compartir nodo y una capa puede desplegarse en varios.

## 42. Disponibilidad

Dos componentes en serie tienen 99,9 % y 99,5 %. Calcula disponibilidad.  
**Respuesta:** `0,999×0,995 = 0,994005 = 99,4005 %`; el sistema no alcanza 99,5 %.

## 43. RAID

¿Por qué RAID 6 no reemplaza un respaldo?  
**Respuesta:** tolera falla de hasta dos discos, pero replica borrado, corrupción, malware y error humano. El respaldo conserva una copia recuperable separada.

## 44. Nube

¿Cuándo PaaS sería mejor que IaaS?  
**Respuesta:** cuando se prioriza desarrollar y delegar SO/plataforma. IaaS conviene si se necesita control especial, software legado o configuración que PaaS no permite.

## 45. Continuidad

Un servicio tiene RTO 4 h y RPO 1 h. Interpreta.  
**Respuesta:** debe volver en máximo cuatro horas y recuperar datos hasta un punto no anterior a una hora antes del incidente.

## 46. Identidad

¿Por qué OAuth 2.0 no equivale a autenticación?  
**Respuesta:** OAuth delega autorización. OpenID Connect añade identidad/autenticación; JWT es solo un formato posible de token.

## 47. Entrega

Compara blue-green y canary.  
**Respuesta:** blue-green mantiene dos ambientes y cambia todo el tráfico, con reversa rápida y costo alto; canary expone gradualmente y requiere observabilidad para decidir expansión/reversa.

## 48. TIER

¿Un servidor en un datacenter TIER III garantiza servicio TIER III?  
**Respuesta:** no. Enlaces, aplicación, dependencias y operación pueden ser puntos únicos; TIER describe infraestructura dentro de un alcance.

## 49. Redundancia

¿Por qué dos UPS no son necesariamente 2N?  
**Respuesta:** pueden compartir tablero, ducto, ATS o PDU. 2N exige dos sistemas completos y caminos independientes.

## 50. PUE/DCiE

Energía total 90 MWh y TI 54 MWh. Calcula.  
**Respuesta:** `PUE=90/54=1,667`; `DCiE=54/90=60 %`. Deben declararse puntos y período de medición.

## 51. Recintos

¿Por qué separar baterías de la sala blanca?  
**Respuesta:** peso, ventilación y posible hidrógeno/energía almacenada constituyen riesgos distintos y requieren acceso/mantenimiento propios.

## 52. Corte eléctrico

Describe la secuencia.  
**Respuesta:** UPS sostiene sin corte; ATS arranca/transfiere al generador; generador sostiene TI y clima. Si falla o se agota, monitoreo activa apagado ordenado antes de perder batería.

## 53. Racks

Hay 210U de equipos, 42U por rack y ocupación objetivo 70 %. ¿Cuántos racks?  
**Respuesta:** capacidad útil/rack `42×0,70=29,4U`; `210/29,4=7,14`, por lo tanto 8 racks, sujeto además a kW y peso.

## 54. Tarifa

Costo empresa $2.400.000, 180 h, 75 % productivo, GG 18 % y margen 12 % sobre costo.  
**Respuesta:** horas 135; directo $17.777,78; con GG $20.977,78; tarifa con margen $23.495,11/h.

## 55. Incertidumbre

¿Por qué no se debe comunicar una estimación temprana como cifra exacta?  
**Respuesta:** faltan requisitos/diseño y el cono es ancho. Debe darse rango, supuestos y fecha, refinándolo con aprendizaje.

## 56. Reservas

Compara contingencia, reserva de gestión y margen.  
**Respuesta:** contingencia cubre riesgos identificados dentro de línea base; gestión cubre desconocido fuera de línea base; margen es utilidad en el precio.

## 57. Hacer/comprar/arrendar

¿Qué elegirías para notificaciones variables?  
**Respuesta:** arrendar servicio por uso puede evitar infraestructura y absorber variación; hay que evaluar TCO, privacidad, SLA y salida.

## 58. Tipo de contrato

¿Quién asume más riesgo de costo en precio fijo?  
**Respuesta:** proveedor, si alcance está definido. Con ambigüedad, habrá conflicto/cambios; por eso debe aclarar supuestos y exclusiones.

## 59. PTA

Costo objetivo 80, ganancia 10, techo 110, reparto comprador 70 %.  
**Respuesta:** precio objetivo 90; `PTA=80+(110−90)/0,70=108,57`.

## 60. Documentos

¿Cuándo usar RFI y cuándo RFQ?  
**Respuesta:** RFI explora mercado y capacidades; RFQ pide precio comparable cuando especificación/cantidad ya están definidas.

## 61. TCO

Compra cuesta 30 inicial + 6/año; SaaS 14/año. Punto de equilibrio.  
**Respuesta:** `30+6t=14t`; `t=3,75 años`. Después se comparan riesgos, obsolescencia y salida.

## 62. ISO 25010:2023

Menciona cuatro características relevantes para SaludConecta y justifica.  
**Respuesta:** seguridad por datos clínicos; fiabilidad por continuidad; eficiencia por atención; interacción por usuarios diversos. También aplican mantenibilidad y compatibilidad.

## 63. Requisito de calidad

Reescribe “debe ser seguro”.  
**Respuesta ejemplo:** “Antes de recepción, una prueba independiente no detectará vulnerabilidades críticas abiertas y el 100 % de accesos clínicos quedará auditado”.

## 64. Cadena contractual

Explica `requisito → métrica → prueba → aceptación → hito → pago`.  
**Respuesta:** convierte una expectativa en obligación verificable. Si falta un eslabón, puede ser imposible demostrar incumplimiento o vincularlo a recepción/pago.
