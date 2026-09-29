# Guía para Asistentes IA (Claude / Antigravity)

Trabajo del ramo ICI-5444 (PUCV). Caso 10, **Transporte de Carga**, licitación ficticia
TFEP-01/2026 para la empresa **Transportes Curimón S.A.**, postulando bajo la empresa
consultora **audIT Soluciones Tecnológicas SpA**.

El hito actual es la **Entrega del Informe 2**, fijada para el **05 de octubre de 2026**
(Formulario T-20, FEP01 p.65).

El repositorio no es de software aplicativo: el código en `tools/` existe para consultar
las bases y procesar planillas. El producto central son los informes técnicos y económicos.

## Regla principal: no leer el corpus completo

Los documentos de las bases suman ~100.000 tokens. **Nunca los leas enteros ni los
adjuntes.** Para cualquier consulta, empieza por:

```bash
./tools/buscar.py "términos de la consulta"
```

Cuesta ~330 tokens y devuelve extractos con su cita. Para ver una sección completa
(~380 tokens):

```bash
./tools/buscar.py -v A:45      # por artículo
./tools/buscar.py -v 221       # por id de sección
```

Solo si de verdad hace falta más contexto, abre el `.md` con `sed -n '1200,1260p'`.
Leer un `.md` completo son 30.000 tokens y casi nunca se justifica.

Los PDF originales **no están en el repo** y no debes intentar leerlos aunque
aparezcan localmente: son escaneos de 88 MB sin capa de texto.

Otras opciones útiles: `-o` (cualquiera de las palabras), `-p` (frase literal),
`-f FEP01|FEP02|FEP03` (un documento), `-l` (mapa por capítulos, ~750 tokens).

## Cómo citar

Cada resultado trae documento, página, tipo y número. Cita así: `FEP01 · Artículo 35°
· p.24`. Los `.md` llevan marcadores `<!-- ===== página N / M ===== -->` que
corresponden a la página del PDF original, verificable contra el documento impreso.

## Qué hay dónde

| Directorio / Archivo | Propósito y Contenido |
|---|---|
| `Informe-1/` | Entregables y consolidados del Informe 1 (D1 a D4, consultas, anexos) |
| `Informe-2/` | Espacio activo de la Entrega 2 (`plan_maestro_consolidado_entrega_2.md`, borradores S6–S9) |
| `Investigacion/` | Trabajo de investigación individual TI-12 (Persona 1 a 8, bitácoras A-6 y consolidados) |
| `texto/` | Bases de licitación (`FEP01`, `FEP02`, `FEP03`), `Comunicado_09.md`, `Comunicado_10.md`, DB `secciones.db` |
| `tools/` | Herramientas de consulta (`buscar.py`), exportador (`consultas_xlsx.py`) y OCR |
| `recursos/` | Identidad corporativa, logos, plantillas LaTeX y portadas |

## Directrices Críticas de Entrega (Comunicados 09 y 10)

1. **Régimen de Ficción de Licitación (Art. 46 Obs. 12 / Comunicado 10):**
   Queda terminantemente prohibido consignar nombres reales de integrantes o referencias
   académicas en los documentos de la propuesta técnica. La autoría se formaliza
   exclusivamente mediante códigos de dupla (`D1`, `D2`, `D3`, `D4`) y roles corporativos.

2. **Estructura Técnica Obligatoria (Comunicado 10):**
   Los subdocumentos deben contener análisis, síntesis y justificación de ingeniería.
   Los inventarios exhaustivos van en sus respectivos Formularios `T-xx`. Prohibido
   incluir bitácoras personales, diarios de trabajo o prosa inflada en la propuesta.

3. **Uso de IA y Bitácoras A-6 (Comunicado 09):**
   Todo uso sustancial de IA debe registrarse con transparencia y asociarse a la bitácora
   individual A-6 del integrante responsable en `Investigacion/`. A partir del Informe 2,
   la detección de contenido generado no declarado o indicios de IA (alucinaciones
   normativas, prosa vacía) acarrea sanciones severas sobre el capítulo evaluado.

## Ponderaciones Técnicas de la Entrega 2

La tabla de evaluación técnica está en `FEP01 p.66` (`./tools/buscar.py -v 221`). Los pesos
cambian entre informes. En el **Informe 2**, los pesos son:

| Subdocumento | Nombre / Foco | Peso Informe 2 |
|:---:|---|:---:|
| **S7** | Plan de trabajo, EDT, Cronograma (Forms T-14, T-15, T-18) | **15 %** |
| **S3** | Esquema de solución y alcance (Formulario T-12) | **12 %** |
| **S4.2** | Arquitectura física, Data Center y Hardware (Form T-11) | **11 %** |
| **S8** | Plan de riesgos (Formulario T-16 - AMFE) | **10 %** |
| **S13** | Innovaciones (Formulario T-19) | **10 %** |
| **S6** | Metodologías de gestión y desarrollo (Forms T-9, T-10) | **8 %** |
| **S9** | Plan de calidad y pruebas (Forms T-13, T-17) | **8 %** |
| **S4.1** | Arquitectura lógica e integraciones | **7 %** |
| **S2** | Resumen Ejecutivo y comprensión del problema | **6 %** |
| **S5** | Modelo y gestión de datos | **6 %** |
| **S1** | Presentación empresa y experiencia (Form T-6) | **3 %** |
| **Transversal** | Formalidad y cumplimiento de instrucciones | **3 %** |
| **TOTAL** | Evaluación Técnica | **100 %** |

Al razonar sobre prioridades o esfuerzo, especifica siempre a qué informe corresponde
el porcentaje.

## Gobernanza por Duplas (Entrega 2)

El avance se articula en dos frentes simultáneos (ver `Informe-2/plan_maestro_consolidado_entrega_2.md`):
- **D1 (QA & Gobernanza):** Frente A: S1, S2, Form T-6. Frente B: S9, Form T-13, Form T-17.
- **D2 (PMO & Requerimientos):** Frente A: S3, Form T-12. Frente B: S7, Forms T-14, T-15, T-18.
- **D3 (DevSecOps & Software/Datos):** Frente A: S4.1, S5. Frente B: S6, Forms T-9, T-10, Ficha T-19.
- **D4 (Infraestructura, IoT & Riesgos):** Frente A: S4.2/4.3, Form T-11. Frente B: S8, Form T-16, Ficha T-19.

## Herramientas de Soporte

- `tools/buscar.py` — índice FTS5 en memoria para buscar en las bases sin consumir contexto.
- `tools/consultas_xlsx.py` — genera la planilla oficial de consultas desde `Informe-1/D2/`.
- `tools/pdf_ocr.sh` y `tools/page_to_md.py` — canal de reconstrucción de bases desde PDF original.

## Convenciones

- Todo en español, incluidos comentarios y mensajes de commit.
- Los porcentajes y cifras del caso se citan con su fuente; no los repitas de memoria
  sin verificarlos con `buscar.py`.
