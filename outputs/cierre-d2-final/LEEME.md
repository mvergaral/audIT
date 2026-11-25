# Entrega de D2 para revisión

Empezar por CIERRE-D2.md. Las decisiones comerciales aceptadas y los controles están en evidencia/.

El paquete D2_PARA_REVISION_20261125.zip contiene 11 archivos: seis PDF técnicos y cinco económicos. No incluye el Sobre 1 ni el resto del Sobre 2. No es una oferta enviada ni firmada. El PDF es la referencia de foliación del sobre económico; los DOCX deben revisarse en Word/LibreOffice según su propia paginación.

Para reproducir la generación: integrar las fuentes y datos del ZIP sobre el corte de repositorio indicado en evidencia/linea-base.json, ejecutar preparar_fuentes.py para crear la copia aislada y luego compilar_d2.py y compilar_economico.py, incorporar las curvas y normalizar los DOCX con completar_docx.py y verificar con verificar_corte.py. El paso de fuente residual en S7 conserva texto y píxeles. Los runners usan la copia aislada fuentes/ y no modifican estilos o configuración compartidos. compilar_d2.py requiere MiKTeX y biber disponibles; los scripts de documentos usan el runtime indicado por Codex.

No ejecutar los generadores iniciales de contenido sobre fuentes revisadas sin revisar su efecto. Los manifiestos técnico y económico tienen nombres separados. Los auxiliares y renders no se entregan.
