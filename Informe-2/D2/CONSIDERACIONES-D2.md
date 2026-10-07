# Consideraciones de D2 para los demás equipos

Informe 2. D2 entregó S3 y Formulario T-12, S7 y Formularios T-14, T-15 y T-18, filas 37 a 52 de la
tabla del Art. 46 e innovaciones 1 y 4 (S13 y T-19). Todo en `recursos/Formato-Oferta-audIT/`.

## Decisiones que afectan a toda la oferta

| Decisión | Valor | Dónde está |
|---|---|---|
| Inicio del contrato | Mes 1 = febrero de 2027 (supuesto SA-01). Es el único inicio que deja los meses 16 y 21 fuera de dic–abr | S3 3.2.6, T-12 |
| Calendario | Mes 16 = mayo 2028, mes 21 = octubre 2028, mes 56 = septiembre 2031. La marcha blanca E1 (feb–abr 2028) cae siempre en temporada de fruta | S3 3.1, S7 7.3.2 |
| Sistema de gestión de 2013 | Sustitución función por función tras capa anticorrupción. Asignación, control de viaje y liquidación en el mes 16. Órdenes y tarifas a clientes en el mes 21. Solo consulta hasta el mes 24 | S3 3.2.4 |
| Documento electrónico sin cobertura | Siempre lo emite el sistema contable: emisión anticipada desde la orden, o datos enviados por el satélite del equipo audIT y folio de vuelta. Ningún equipo emite | S3 3.4.2 |
| Costo antes de la renegociación de 2027 | Estudio de costo por ruta y contrato en el mes 6 (EDT 2.5). El costeo por viaje entra en producción en el mes 16 | S3 3.2.1 |
| Montaje a bordo | Flota propia en los meses 6 a 9 (piloto de 10 en el mes 6). Terceros adheridos desde el mes 7. Pausa en los meses 11 a 15. Reanuda en los meses 16 a 18 | S7 7.3.3 |
| Nombres canónicos de componentes | Los seis contextos de S4 4.1.3: Planificación y tráfico, Flota y activos, Personas y cumplimiento, Telemetría y geocercas, Operación de fletes, Liquidación y costeo | S3 3.3.1 |
| Comités | Los de S6: Comité Ejecutivo, Comité de Proyecto, Comité de Arquitectura, Comité de Operación | S3, S7 |
| EDT | 13 elementos y 54 paquetes. Usar estos códigos en cualquier referencia a la EDT | S7 7.1, T-14 |
| Dotación | 14 → 24 → 30 → 33 → 37 (peak, meses 13 a 17) → 30 → 26 → 16 en operación | S7 7.2.2, T-15 |
| Horas hombre | 93.760 en la implementación y 92.160 en la operación. Solo en el T-15 | T-15 |
| Prioridad de requerimientos | 1 (falla deja salir un camión o pierde prueba), 2 (sostiene criterio o restricción), 3 (optimiza) | S3 3.2.8, T-12 |
| Códigos de origen | CA-nn (criterio Cap. 18), R-nn (restricción Cap. 10), DP-nn (decisión del 16.1), RN-nn (regla de negocio), SA-nn (supuesto de alcance) | T-12, glosario |

EDT de primer nivel: 1 Gestión, 2 Levantamiento y diseño, 3 Plataforma, 4 Equipo a bordo,
5 Servicios Etapa 1 (5.1 a 5.6 = los seis contextos, 5.7 portal del transportista), 6 Integraciones,
7 Datos y migración, 8 Servicios Etapa 2, 9 Adhesión, 10 Calidad y pruebas, 11 Implantación,
12 Innovaciones (12.1 a 12.5, una por innovación), 13 Operación.

## Pendientes por equipo

### D3 (S4, S5, S6, innovación 2)
- S4 llama varias veces «sistema contable de 2013» al sistema de gestión de transporte de 2013. Son sistemas distintos (Caso, cap. 5, p. 12).
- La tabla de inventario de S4 (4.1, `tab:4-inventario`) usa nombres distintos de los seis contextos («Despacho y asignación», «Gestión documental», «Tarifas y liquidación»).
- S4 no tiene todavía el ADR del sistema de 2013 que promete la fila 60 del Art. 46. Debe registrar la misma decisión de S3 3.2.4.
- S4 remite el mecanismo del documento sin cobertura a su sección 4.1, que aún no lo trae. Debe reflejar la decisión de S3 3.4.2.
- S6 dice «marcha blanca de 60 días» en ambas etapas. El Art. 17.1 fija 3 meses (E1) y 2 meses (E2).
- S6 dice que audIT compra «148 computadores y 34 CANclick» en los meses 1 y 2. El hardware lo compra el mandante (Caso, cap. 11) y el T-11 declara 182 equipos.
- S6 cita «SLA 99,5 %». El Art. 78.2 exige 99,9 % para lo crítico.
- Ficha T-19 de la innovación 2: piloto en el mes 4 y flota completa en el mes 8. El plan dice meses 6 y 9. Sus códigos EDT deben pasar a 12.2 y a los paquetes 4.1 y 4.2.

### D4 (S4 física, S8, innovación 3)
- En la malla del T-15 (`7-malla`), la actividad A18 «Escalamiento telemático e instalación progresiva a bordo» (días 240 a 360) se interpretó en S7 así: meses 13 a 15, integración por plataforma sin tocar camiones. Meses 16 a 18, montaje físico. Conviene ajustar su descripción para que no parezca montaje en temporada de fruta.
- La figura `figuras/13-innovaciones/cartera.png` probablemente tiene el nombre antiguo de la innovación 1. Ahora se llama «Expediente verificable del transportista».
- Ficha T-19 de la innovación 3: sus códigos EDT deben pasar a 12.3 y a los paquetes 4.2 y 5.2. Meses de montaje coherentes con S7: 6 a 10, y 16 a 18.
- S8: la red de riesgos puede tomar las actividades y holguras de S7 7.3.1 y los supuestos SA-01 a SA-08 de S3. El SA-08 (apagado 2G y 3G) ya remite a S8.

### D1 (S9, T-17, innovación 5, consolidación del Art. 46)
- El T-17 usa códigos EDT provisionales (`EDT-3.1`, `EDT-2.3`…). La correspondencia ya está en el T-12, campo de componente de cada requerimiento. Los casos de prueba CP-… de D1 se citan allí tal cual.
- Las filas generales 01, 08, 09 y 12 del Art. 46 nombran a S3. Su respuesta debe apuntar a las nuevas secciones (T-12 adjunto, sin títulos seguidos de tabla, sin pendientes internos).
- Ficha T-19 de la innovación 5: sus códigos EDT deben pasar a 12.5 y a los paquetes 4.1 y 5.1.
- Ventanas de prueba de S9: pruebas integrales en los meses 10 a 12 (A12), certificación E2 en los meses 17 y 18 (A22), pruebas de DR en junio y noviembre de cada año de operación.

### Todos
- Las declaraciones de IA de S3, S7 y S13 tienen `\marcador{...}` en la columna de revisión humana. Hay que llenarlas después de revisar, nunca antes.
- No se ha compilado S3, S7 ni S13. Falta instalar `texlive-luatex` (`sudo pacman -S --needed texlive-luatex`). Revisar al compilar que las figuras TikZ (EDT, Gantt, esquema conceptual) quepan en la página y que su letra sea de 9 pt o más.
