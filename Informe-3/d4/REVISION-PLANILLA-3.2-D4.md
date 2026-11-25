# Revisión de D4 a la planilla 3.2

| Dato | Valor |
|---|---|
| Fecha | 2026-11-15 |
| Revisa | D4 (infraestructura, IoT y riesgos) |
| Rama | `codex/cierre-entrega-3` |
| Commits revisados | `b4cc116` (planilla 3.2 y scripts) y `aab0dba` (adenda A-6) |
| Archivo | `outputs/3.2/Entrega-3.2/INFORME3_AUDIT_PLANILLA_3.2_20261115.xlsx` |
| Hojas leídas | Feedback 3.2, Parámetros corrección, Contrato de soporte, Soporte por perfil, Instalación por lote |
| Decisión de D4 | D4-160 en `Informe-2/D4/DECISIONES-D4.md` |
| Para | D2 (planilla y T-15) y D1 (S1 y red regional) |

La rama no modifica archivos de D4. El único subdocumento que toca es `03-solucion/contenido.tex`.

## 1. Resumen

- Los supuestos de D4 en C78–C89 son correctos o se pueden aceptar con condiciones.
- La 3.2 cambia el modelo de operación y deja cinco contradicciones con el T-15 y con S10, S11, S12, T-8 y S14. El Comunicado 10, §7.1, pone en 0 un subdocumento si contradice a otro.
- D4 no cambia sus subdocumentos hasta que D2 decida el T-15. Después los ajusta en un solo paso.

## 2. Validación de los parámetros de D4

### 2.1 Correctos

| Celda | Valor | Fuente de D4 | Resultado |
|---|---|---|---|
| B63 | 182 kits | 4.1, T-11 fila 1 | Correcto. 148 propios y 34 de terceros sin equipo |
| B67, B68, B69 | 8, 7, 7 | T-11 fila 2 | Correcto. Juegos por crecimiento en M24, M36 y M48 |
| B79 | 19 | 4.1 fila 19 | Correcto. La nota «172 más 19» calza porque 4.1 cuenta aparte los 10 del piloto |
| B80 | 21 | T-11, balizas | Correcto |
| B87, B88 | 1 y 3.331.927,28 | 4.3 | Correcto. Prepago en M13, M25, M37 y M49, el último por 8 meses. El total es el de 4.3 |
| B85, B86 | 160 h SRE y 80 h Software | Sin fuente D4 | Razonable como mínimo. H7 (M16) es el paso más exigente: entra toda la flota, se reconectan los equipos y parte la mesa |

Los refuerzos de B85 y B86 son horas por encima del T-15. D2 debe reflejarlas en el T-15 o rotularlas como contingencia.

### 2.2 Aceptables con condiciones

**B78, 80 h internas de campo en operación (0,5 FTE)**
- Alcanzan para stock, garantías con el fabricante, coordinación del proveedor, recepción de cada intervención y hoja de vida de los equipos.
- Condición 1. El proveedor debe hacer en sus rondas la revisión preventiva de gabinetes y equipos a bordo. Hoy esa tarea está en el paquete 13.3 (`subdocumentos/11-planes-operacion/contenido.tex`, línea 120).
- Condición 2. FEP02, numeral 8.4, p. 19, exige atención 24x7 en sitio y resolución en 4 h para el hardware crítico de San Bernardo y de los terminales. Las rondas programadas no cubren eso. Falta una partida de llamados de urgencia en el contrato del proveedor.

**B81 y B82, 2 visitas correctivas y 2 rondas regionales al mes**
- Sirven como base para diagnóstico y reinstalación.
- Falta el crecimiento concentrado: 8 kits en M24, 7 en M36 y 7 en M48, más 35 balizas (T-11). Con 140 min por kit (B6), esos meses superan las 2 visitas. Proponemos lotes en esos tres meses, igual que los lotes de montaje.
- Falta la renovación de 40 tractocamiones entre 2030 y 2032 (Caso, RT-02.12, p. 31). Cada camión renovado obliga a desmontar el equipo y montarlo en el nuevo. Con el mes 1 en febrero de 2027, eso da cerca de un traslado al mes desde M36.
- Con 2 rondas, cada uno de los cuatro terminales regionales se visita cada dos meses aproximadamente. Funciona solo con equipos de reposición en el terminal y visitas a pedido.

**Mesa de nivel 1 interna**
- De acuerdo. Calza con el S10.

## 3. Contradicciones con el T-15 y los subdocumentos

| N.º | Planilla 3.2 | Documento que contradice | Dónde |
|---|---|---|---|
| 1 | Montaje externo M7–M9 (B59 = 1) | S12 dice que la instalación no se subcontrata. T-8 no tiene proveedor de montaje. 4.4 de D4 y S1 de D1 la declaran interna | `12-equipo/contenido.tex` línea 227. `12-equipo/formularios/T-8.tex`. `Informe-3/d4/4.4-proveedores-clave.md` línea 23 |
| 2 | Los 182 kits se montan en M6–M9 (B37–B42) y el técnico interno sale en M10 (B83) | T-14 monta en los meses 6 a 10 y 16 a 18. S4 y 4.1 detienen el montaje en M11–M15 y lo retoman en M16–M18 por los terceros que adhieren después | `07-plan-trabajo/formularios/T-14.tex` línea 42. `04-arquitectura/contenido.tex` líneas 970–974. `Informe-3/d4/4.1-presupuesto-equipos.md` línea 190 |
| 3 | Paquete 13.3 con 80 h internas (Contrato de soporte B7) | T-15 da 2 personas y 320 h. S10, S11, S12, T-8 y S14 cuentan 16 personas en operación | `07-plan-trabajo/formularios/T-15.tex` línea 87. `10-operacion/contenido.tex` línea 75. `12-equipo/contenido.tex` línea 143. `12-equipo/formularios/T-8.tex` línea 53. `14-ventajas/contenido.tex` líneas 152, 179 y 185 |
| 4 | Escalones de madurez (B70 = 1, B13–B15): el 13.4 baja de 640 h a 560, 480 y 400 desde M25, M33 y M45 | T-15 dice que la operación es constante durante los 36 meses. S11 usa justo esas 320 h variables para la bolsa evolutiva (224 h) y la deuda técnica (96 h). Con los escalones, la bolsa de 2.688 h al año no cabe | `07-plan-trabajo/formularios/T-15.tex` línea 81. `11-planes-operacion/contenido.tex` líneas 45, 49 y 51 |
| 5 | Mesa de nivel 1 con 960 h más 160 h de suplencias, 7 FTE (Contrato de soporte) | T-15 y S10 dicen 6 personas y 960 h | `07-plan-trabajo/formularios/T-15.tex` línea 85. `10-operacion/contenido.tex` línea 181 |

Las rutas de `subdocumentos/` son relativas a `recursos/Formato-Oferta-audIT/` en `main`.

## 4. Propuesta para D1 y D2

- Que el proveedor externo de campo sean los cuatro centros técnicos aliados de la red regional que nombra el S1.
- Así se cubren las urgencias de 4 h en los terminales.
- Además, la fila de esos centros en el T-8 deja de decir «Sin partida propia» (`12-equipo/formularios/T-8.tex` línea 84) y toma el porcentaje del servicio de campo externo.

## 5. Qué se necesita de cada dupla

**D2**
- Decidir si el T-15 adopta el modelo de la 3.2: 13.3 a 0,5 FTE con proveedor externo, escalones de madurez en 13.4 y mesa de 7 FTE. La otra opción es que la planilla vuelva al T-15.
- Agregar a la planilla un lote de montaje en M16–M18, o confirmar con el T-14 que no hace falta.
- Agregar lotes de crecimiento en M24, M36 y M48, los traslados por renovación desde M36 y una partida de llamados de urgencia.
- Reflejar los refuerzos B85 y B86 en el T-15 o rotularlos como contingencia.

**D1**
- Decidir si el S1 pasa el montaje y el campo a proveedor externo.
- Responder la propuesta de la sección 4 sobre la red regional.

**D4**
- Con la decisión de D2, ajustar S10, S11, S12, T-8 y S14 en un solo paso: quién monta, el paquete 13.3, la capacidad del 13.4, la bolsa evolutiva y el porcentaje del proveedor de campo.
