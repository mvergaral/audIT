# Arquitectura física, nube, continuidad y entrega

## 1. De la lógica al despliegue

La arquitectura física ubica componentes lógicos en infraestructura: redes, balanceadores, servidores, contenedores, almacenamiento, seguridad y respaldos. El diagrama lógico dice “qué colabora”; el físico dice “dónde corre y por qué puede cumplir”.

## 2. Modelo OSI aplicado

| Capa | Pregunta práctica | Ejemplos |
|---|---|---|
| 7 Aplicación | ¿Qué protocolo usa la aplicación? | HTTP, DNS, SMTP |
| 6 Presentación | ¿Cómo se representa/cifra? | TLS, formatos |
| 5 Sesión | ¿Cómo se mantiene diálogo? | sesiones/tokens |
| 4 Transporte | ¿Puerto y confiabilidad? | TCP/UDP |
| 3 Red | ¿Cómo se enruta? | IP, router, firewall L3 |
| 2 Enlace | ¿Cómo circula localmente? | Ethernet, VLAN, switch |
| 1 Física | ¿Qué medio transporta? | cobre, fibra, radio |

Sirve para ubicar fallas y controles. “La red está caída” es insuficiente: puede fallar DNS, TLS, ruta, VLAN o fibra.

## 3. Topología on-premise

```text
Internet
  ↓
Firewall/WAF → DMZ → balanceador → aplicaciones
                                  ↓
                             servicios internos
                                  ↓
                         base de datos/almacenamiento
                                  ↓
                              respaldo aislado
```

La DMZ aloja servicios expuestos sin abrir acceso directo a la red interna. La segmentación reduce movimiento lateral. Dos equipos no dan alta disponibilidad si comparten energía, enlace o configuración defectuosa.

## 4. Dimensionamiento

Cadena defendible:

```text
usuarios → concurrencia → transacciones/s → consumo unitario → capacidad → holgura
```

Se declaran CPU, RAM, datos a horizonte, IOPS, ancho de banda y crecimiento. “Servidor potente” no es dimensionamiento.

### Virtualización y contenedores

- **VM:** incluye sistema operativo; mayor aislamiento y sobrecarga.
- **Contenedor:** comparte kernel; arranque rápido y densidad mayor.
- **Orquestador:** programa, recupera y escala contenedores.
- **Hipervisor tipo 1:** ejecuta directamente sobre hardware; apropiado para producción.

Contenedores pueden correr dentro de VM. Elegirlos no elimina nodos, almacenamiento, red ni operación.

### Quórum

Los sistemas de consenso suelen usar cantidad impar. Con tres nodos, dos forman mayoría; con dos, perder uno impide distinguir falla de partición. Tres nodos no garantizan capacidad si un nodo no soporta la carga restante.

## 5. Almacenamiento y RAID

- **DAS:** conectado directamente; simple y local.
- **NAS:** archivos por red; compartición sencilla.
- **SAN:** bloques por red; alto desempeño y complejidad.

| RAID | Idea | Capacidad útil aproximada | Tolerancia |
|---|---|---|---|
| 0 | distribución sin redundancia | `n×disco` | ninguna |
| 1 | espejo | 50 % | un disco por espejo |
| 5 | paridad simple | `(n−1)×disco` | un disco |
| 6 | doble paridad | `(n−2)×disco` | dos discos |
| 10 | espejos distribuidos | 50 % | depende de pares |

RAID mejora disponibilidad local; **no es respaldo** porque replica borrado, corrupción o ransomware.

## 6. Nube

Cinco características: autoservicio, acceso por red, recursos compartidos, elasticidad y servicio medido.

| Modelo | Cliente gestiona | Proveedor gestiona | Conviene cuando |
|---|---|---|---|
| IaaS | SO, middleware y aplicación | hardware/virtualización | se necesita control |
| PaaS | aplicación y datos | plataforma y base | se prioriza desarrollo |
| SaaS | configuración/uso | solución completa | problema estándar |

Despliegue puede ser público, privado, híbrido o multicloud. Región es zona geográfica; una región contiene zonas de disponibilidad separadas.

### Serverless

El proveedor administra servidores y cobra por uso. Conviene en eventos, carga variable o tareas breves. Riesgos: arranque en frío, límites, dependencia y costos impredecibles a alto volumen.

### On-premise versus nube

No se decide por modernidad:

| Criterio | On-premise | Nube |
|---|---|---|
| Inversión | CAPEX alto | OPEX/consumo |
| Elasticidad | Lenta | Alta |
| Control físico | Alto | Delegado |
| Operación | Propia | Compartida |
| Salida | Activos quedan | Migración puede ser costosa |

## 7. Rendimiento, escalabilidad y disponibilidad

- escalado vertical: máquina mayor;
- horizontal: más instancias;
- elasticidad: ajustar automáticamente;
- disponibilidad: porcentaje utilizable;
- rendimiento: tiempo/capacidad bajo carga.

Disponibilidad en serie:

```text
A_total = A1 × A2 × ... × An
```

Dos componentes de 99,9 % en serie producen `0,999² = 99,8001 %`, no 99,9 %.

### SLI, SLO y SLA

- **SLI:** indicador medido, por ejemplo disponibilidad observada.
- **SLO:** objetivo interno, por ejemplo 99,7 %.
- **SLA:** compromiso contractual con medición, exclusiones y compensación, por ejemplo 99,5 %.

Conviene operar con SLO más exigente que SLA para tener margen.

## 8. Continuidad

- **RTO:** tiempo máximo para recuperar servicio.
- **RPO:** pérdida máxima de datos expresada en tiempo.

RTO de 4 h no significa respaldo cada 4 h. RPO de 1 h exige copias o replicación capaces de perder como máximo una hora.

| Diseño | Ventaja | Costo/riesgo |
|---|---|---|
| Activo-pasivo | operación más simple | capacidad ociosa y conmutación |
| Activo-activo | aprovecha sitios y reduce interrupción | conflictos y complejidad |

Replicación síncrona protege RPO pero añade latencia; asíncrona tolera distancia y puede perder cambios recientes.

### Respaldos

Completo, incremental y diferencial responden a costo/tiempo distintos. Una política debe declarar frecuencia, retención, ubicación, cifrado, inmutabilidad y pruebas de restauración. Un respaldo nunca restaurado es una esperanza, no evidencia.

## 9. Seguridad e identidad

Defensa en profundidad combina segmentación, firewall/WAF, endurecimiento, cifrado, gestión de secretos, mínimo privilegio, monitoreo y respuesta.

- autenticación: quién eres;
- autorización: qué puedes hacer;
- sesión: cómo se mantiene el estado.

| Tecnología | Uso principal |
|---|---|
| LDAP/Active Directory | directorio corporativo |
| SAML 2.0 | federación empresarial |
| OAuth 2.0 | delegación/autorización |
| OpenID Connect | autenticación sobre OAuth 2.0 |
| JWT | formato de token, no protocolo de autenticación por sí solo |

Token autocontenido escala bien, pero revocarlo es más difícil; sesión de servidor facilita revocación, pero exige almacenamiento compartido al escalar.

## 10. Ambientes y CI/CD

- desarrollo: cambio frecuente y datos sintéticos;
- QA: pruebas integradas;
- preproducción: semejante a producción;
- producción: servicio real y controles estrictos.

CI integra y prueba cada cambio. CD automatiza entrega/despliegue bajo controles. Estrategias:

- **blue-green:** dos ambientes, cambio rápido y costo duplicado;
- **canary:** exposición gradual y observabilidad exigente;
- **rolling:** reemplazo progresivo;
- **feature flags:** separan despliegue de activación.

Infraestructura como código hace repetible el ambiente. Datos reales no deben copiarse a QA sin anonimización.

## 11. Decisión SaludConecta

Una alternativa híbrida:

- identidad e integración local por restricciones del mandante;
- portal y APIs en nube administrada;
- respaldo inmutable en ubicación separada;
- enlace/VPN redundante;
- activo-pasivo para base crítica según RTO/RPO;
- ambientes separados y despliegue blue-green.

Debe compararse con operación totalmente local mediante TCO, seguridad, capacidad y dependencia.

## 11.1 Tendencias: cuándo son decisión y no moda

- **Platform engineering:** estandariza despliegues para varios equipos; puede ser excesiva para uno pequeño.
- **IaC/GitOps:** infraestructura declarada y cambios auditables; exige secretos protegidos.
- **Service mesh:** control y telemetría entre muchos servicios; agrega complejidad.
- **Edge:** procesa cerca de la fuente cuando latencia o conectividad lo justifican.
- **Datos e IA:** requieren calidad, seguridad y costo por uso evaluados.
- **FinOps:** etiquetas, presupuestos y responsabilidad sobre gasto nube.
- **Sostenibilidad:** reduce energía y sobredimensionamiento.

La innovación defendible resuelve un requisito y tiene impacto estimado. Si solo agrega un nombre moderno, aumenta costo y riesgo.

Para datos personales se debe considerar el marco indicado en clases, incluida la Ley 21.719, y verificar vigencia y aplicación antes de una oferta real.

## 12. Errores frecuentes y autoevaluación

Errores: confundir RAID con backup, prometer SLA del proveedor como propio, sumar disponibilidades, elegir dos nodos para quórum, omitir costo de salida, usar JWT sin estrategia de revocación y llamar CI/CD a copiar archivos manualmente.

1. ¿Por qué dos servidores pueden seguir formando un punto único de falla?
2. Calcula disponibilidad de tres componentes de 99,9 % en serie.
3. ¿Cuándo elegirías PaaS en vez de IaaS?
4. Diferencia RTO y RPO con un incidente.
5. ¿Por qué RAID 6 no reemplaza un respaldo?
6. Compara blue-green y canary.
