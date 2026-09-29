# Guía para Asistentes IA

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

Cada resultado trae documento, página, tipo y número. Cita así: `FEP01 · Artículo 35° · p.24`. Los `.md` llevan marcadores `<!-- ===== página N / M ===== -->` que
corresponden a la página del PDF original, verificable contra el documento impreso.

## Qué hay dónde

| Directorio / Archivo | Propósito y Contenido                                                                                                  |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| `Informe-1/`       | Entregables, consolidados y plantilla histórica del Informe 1                                                          |
| `Informe-2/`       | Espacio activo de la Entrega 2 (`plan_maestro_consolidado_entrega_2.md`, borradores S6–S9)                           |
| `Investigacion/`   | Trabajo de investigación individual TI-12 (Persona 1 a 8, bitácoras A-6 y consolidados)                               |
| `texto/`           | Bases de licitación (`FEP01`, `FEP02`, `FEP03`), `Comunicado_09.md`, `Comunicado_10.md`, DB `secciones.db`          |
| `tools/`           | Herramientas de consulta (`buscar.py`), exportador (`consultas_xlsx.py`) y OCR                                      |
| `recursos/`        | Identidad corporativa, logos, plantillas LaTeX y portadas                                                               |
| `Formato-Oferta-audIT/` | **Nuevo formato LaTeX oficial de la oferta** (reemplaza a Plantilla-audIT). Ver `GUIA.md` y `LEEME-EQUIPO.md`  |

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

|     Subdocumento     | Nombre / Foco                                             | Peso Informe 2 |
| :-------------------: | --------------------------------------------------------- | :-------------: |
|     **S7**     | Plan de trabajo, EDT, Cronograma (Forms T-14, T-15, T-18) | **15 %** |
|     **S3**     | Esquema de solución y alcance (Formulario T-12)          | **12 %** |
|    **S4.2**    | Arquitectura física, Data Center y Hardware (Form T-11)  | **11 %** |
|     **S8**     | Plan de riesgos (Formulario T-16 - AMFE)                  | **10 %** |
|     **S13**     | Innovaciones (Formulario T-19)                            | **10 %** |
|     **S6**     | Metodologías de gestión y desarrollo (Forms T-9, T-10)  |  **8 %**  |
|     **S9**     | Plan de calidad y pruebas (Forms T-13, T-17)              |  **8 %**  |
|    **S4.1**    | Arquitectura lógica e integraciones                      |  **7 %**  |
|     **S2**     | Resumen Ejecutivo y comprensión del problema             |  **6 %**  |
|     **S5**     | Modelo y gestión de datos                                |  **6 %**  |
|     **S1**     | Presentación empresa y experiencia (Form T-6)            |  **3 %**  |
| **Transversal** | Formalidad y cumplimiento de instrucciones                |  **3 %**  |
|    **TOTAL**    | Evaluación Técnica                                      | **100 %** |

Al razonar sobre prioridades o esfuerzo, especifica siempre a qué informe corresponde
el porcentaje.

## Gobernanza por Duplas (Entrega 2)

El avance se articula en dos frentes simultáneos (ver `Informe-2/plan_maestro_consolidado_entrega_2.md`):

- **D1 (QA & Gobernanza):** Frente A: S1, S2, Form T-6. Frente B: S9, Form T-13, Form T-17.
- **D2 (PMO & Requerimientos):** Frente A: S3, Form T-12. Frente B: S7, Forms T-14, T-15, T-18.
- **D3 (DevSecOps & Software/Datos):** Frente A: S4.1, S5. Frente B: S6, Forms T-9, T-10, Ficha T-19.
- **D4 (Infraestructura, IoT & Riesgos):** Frente A: S4.2/4.3, Form T-11. Frente B: S8, Form T-16, Ficha T-19.

## Formato Oficial de la Oferta (LaTeX) — Formato-Oferta-audIT

El formato oficial de entrega de la propuesta técnica reside en `Formato-Oferta-audIT/` (enlazado a `recursos/Formato-Oferta-audIT/`). Reemplaza a la plantilla anterior y cuenta con una suite automatizada de compilación y verificación de bases.

### Directiva Obligatoria para Asistentes IA
Antes de generar o modificar cualquier archivo LaTeX, **el asistente DEBE leer completamente `Formato-Oferta-audIT/LEEME-EQUIPO.md` y consultar `Formato-Oferta-audIT/GUIA.md`**. No asumas comandos ni estructuras LaTeX estándar sin verificar la clase `audit-oferta.cls`.

### Reglas de Trabajo y Gobernanza en LaTeX
1. **Aislamiento por Dupla:** Cada dupla edita **únicamente** su carpeta en `Formato-Oferta-audIT/subdocumentos/NN-nombre/` (`contenido.tex`, `meta.tex`, `formularios/`). Queda **estrictamente prohibido** modificar `estilo/`, `configuracion/`, `portadas/`, `temas/` o `herramientas/`.
2. **Prefijo Único de Etiquetas:** Toda etiqueta de sección, tabla o figura debe llevar el prefijo del subdocumento para evitar colisiones: `\label{sec:NN-...}`, `\label{tab:NN-...}`, `\label{fig:NN-...}`.
3. **Citas Semánticas a las Bases (No son Bibliografía):**
   - Bases Administrativas: `\art{40.1}{26}`
   - Bases Técnicas Transversales: `\transv{numeral 2.1}{6}`
   - Bases Técnicas del Caso: `\caso{numeral 14.1}{29}` o `\caso{RT-09.01}{32}`
   - Formularios: `\form{T-7}{57}`
   - **Nunca** agregar artículos de las bases a `referencias/referencias.bib`. Las fuentes externas reales (normas ISO, leyes, papers) van en `referencias/referencias.bib` y se citan con `\parencite{clave}` o `\textcite{clave}` (norma APA 7).
4. **Reglas Estructurales Obligatorias (Auditadas por `verificar.py`):**
   - Después de un título va **siempre** un párrafo. Nunca una tabla o figura directamente.
   - Toda tabla y figura debe citarse en el texto **antes** de que aparezca, usando `\tabref{...}` o `\figref{...}`.
   - Después de una tabla debe incluirse la conclusión o síntesis que se extrae de ella.
   - Prohibido llamar a tablas del cuerpo «Formulario T-NN»; los formularios reales se imprimen al final desde `formularios/`.
   - Lo que esté pendiente se marca con `\marcador{descripción}` (aviso en informes, error en entrega final).
5. **Filtro de Residuos Prohibidos:**
   El verificador rechaza palabras no corporativas o prohibidas por el Comunicado 10:
   - Prohibido: `«duplas»`, `«Escuela»`, `«horas hombre»` (salvo en Formulario T-15), o nombres reales de estudiantes.
6. **Dispositivos de Venta Corporativa:**
   - Resumen de apertura: `\begin{resumenApertura} ... \begin{recibe} \item ... \end{recibe} \end{resumenApertura}`.
   - Compromisos medibles: `\begin{compromiso}[metrica=..., verifica=..., fuente=...] ... \end{compromiso}`.
   - Decisiones técnicas: `\decision{titulo=..., decide=..., descarta=..., criterio=..., fuente=...}`.
   - Requisitos trazados: `\req{RT-XX.YY}` o `\reqMargen{RT-XX.YY}`.
   - Cifras con fuente: `\cifra{340 de 374}{Caso, numeral 14.1, p. 29}` o `\cifraMargen{...}{...}{...}`.
7. **Tabla de Observaciones (Artículo 46):**
   Las 100 observaciones del Informe 1 se incorporan en `Formato-Oferta-audIT/anexos/observaciones-informe1.tex`.

### Comandos de Compilación y Verificación (desde `Formato-Oferta-audIT/`)
```bash
./herramientas/preparar.sh                      # Configura entorno y PyMuPDF (una vez)
python3 herramientas/compilar.py muestra        # Compila muestra para revisar render
python3 herramientas/compilar.py subdocs NN     # Compila únicamente el subdocumento NN (ej: 04)
python3 herramientas/compilar.py subdocs        # Compila todos los subdocumentos de la instancia
python3 herramientas/verificar.py               # Ejecuta las 21 verificaciones de bases y formato
```

## Herramientas de Soporte

- `tools/buscar.py` — índice FTS5 en memoria para buscar en las bases sin consumir contexto.
- `tools/consultas_xlsx.py` — genera la planilla oficial de consultas desde `Informe-1/D2/`.
- `tools/pdf_ocr.sh` y `tools/page_to_md.py` — canal de reconstrucción de bases desde PDF original.

## Convenciones

- Todo en español, incluidos comentarios y mensajes de commit.
- Los porcentajes y cifras del caso se citan con su fuente; no los repitas de memoria
  sin verificarlos con `buscar.py`.
