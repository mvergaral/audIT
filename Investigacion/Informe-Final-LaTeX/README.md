# Informe Final TI-12 en LaTeX

Carpeta de ensamblaje del informe final de AudIT para el Caso 10, Transportes Curimón S.A.

## Propósito

Esta carpeta separa el informe final de los borradores individuales de P1-P8. La clase y los estilos se copiaron desde `AUDIT/recursos/Plantilla-audIT/comun/` para que el ensamblaje pueda evolucionar sin modificar la plantilla original.

La fuente consolidada es `../INFORME-MAESTRO.md`. Su versión LaTeX generada queda en `contenido/informe_maestro.tex` y `main.tex` compila ese fragmento directamente.

## Estructura

- `main.tex`: punto de entrada único del informe.
- `contenido/`: capítulos que recibirán el texto consolidado de P1-P8.
- `contenido/informe_maestro.tex`: conversión LaTeX del informe maestro ensamblado.
- `comun/`: clase, estilos y configuración LaTeX del formato audIT.
- `referencias.bib`: bibliografía compartida, pendiente de revisión final con P8.
- `assets/figuras/`: diagramas y figuras aprobadas para insertar.
- `assets/tablas/`: archivos auxiliares de tablas, si se necesitan.
- `build/`: salida de compilación y archivos intermedios. No editar manualmente.

## Orden de ensamblaje

1. P1: resumen, introducción, integración, conclusiones y recomendaciones.
2. P2: marco normativo chileno, vigencia y organismos.
3. P3: marco internacional, normas técnicas y herramientas GRC.
4. P4: obligaciones costeadas, TCO, precios y sensibilidad.
5. P5: arquitectura, privacidad desde el diseño y transferencias.
6. P6: cuestionario y anexos de preguntas.
7. P7: presentación alineada con el informe.
8. P8: auditoría de fuentes, declaración de IA y control final.

## Compilación

Desde esta carpeta, con una distribución LaTeX instalada, en Windows se puede ejecutar:

```bash
powershell -ExecutionPolicy Bypass -File build.ps1
```

El script usa `pdflatex` y `biber` directamente, por lo que no requiere Perl. Si se desea compilar manualmente:

```bash
set TEXINPUTS=comun//;
pdflatex -interaction=nonstopmode -output-directory=build main.tex
biber build/main
pdflatex -interaction=nonstopmode -output-directory=build main.tex
pdflatex -interaction=nonstopmode -output-directory=build main.tex
```

El PDF final quedará en `build/main.pdf`.

## Regenerar desde el informe maestro

Cuando se actualice `../INFORME-MAESTRO.md`, regenerar el fragmento antes de compilar:

```bash
pandoc ../INFORME-MAESTRO.md --from markdown+tex_math_dollars --to latex --wrap=none --output contenido/informe_maestro.tex
```

La plantilla puede emitir advertencias de sustitución de tamaños tipográficos. No son errores de compilación. La bibliografía aparecerá vacía hasta que P8 consolide `referencias.bib` y se incorporen citas al contenido.

## Regla de ensamblaje

No copiar texto al informe final sin validar su responsable, fuente, cifra, versión y compatibilidad con los demás capítulos. Los capítulos iniciales contienen marcadores `TODO` deliberados hasta que P8 cierre la auditoría.
