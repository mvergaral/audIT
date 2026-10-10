"""Subdocumento 6: Metodologías de Gestión y Desarrollo de Software.

Implementa los dos diagramas oficiales de gestión y calidad del software:
  - 6-1-hitos: Gobernanza temporal, fases contractuales (56 meses) y marchas blancas.
  - 6-2-pipeline: Pipeline DevSecOps unificado en GitLab CI, quality gates y SLSA.
"""
import os
import sys

from comun import Figura, ancho, ROJO, LINEA, BORDE, BORDE_FICHA, GRIS_CLARO, SUBRED

C6 = "06-metodologias"


def figura_6_1_hitos():
    """Gobernanza temporal del proyecto y articulación de fases contractuales."""
    f = Figura("6-1-hitos", C6, "V", alto=520)

    # Encabezado temático
    f.grupo(8, 8, 406, 52, "Gobernanza temporal del proyecto y articulación de hitos", rx=5, peso=600)
    f.texto(16, 32, "Marco híbrido: Control contractual PMBOK + Scrum en iteraciones de 2 semanas.", 9)
    f.texto(16, 44, "Duración total: 56 meses (FEP01 Art. 17 y FEP03 Art. 17).", 9, peso=600)

    # Escala de Meses (Línea de tiempo)
    f.grupo(16, 68, 390, 36, "Escala temporal del contrato (Meses 1 al 56)", rx=4, tam=9, peso=600)
    marcas = [("M1-12", 40), ("M13-15", 110), ("M16-18", 185), ("M19-20", 255), ("M21-56", 345)]
    for txt, cx in marcas:
        f.texto(cx, 92, txt, 9, peso=600, anc="middle")

    # Bloque Etapa 1
    f.grupo(16, 114, 390, 80, "Etapa 1: Implementación del Núcleo y Flota Propia", rx=4)
    # Fases E1
    f.rect(24, 136, 120, 46, relleno="#F8F9FA", rx=3)
    f.texto(84, 154, "Desarrollo Núcleo", 9, peso=600, anc="middle")
    f.texto(84, 168, "Meses 1 al 12", 9, anc="middle")

    f.rect(150, 136, 76, 46, relleno="#FFFFFF", rx=3)
    f.texto(188, 154, "Marcha blanca", 9, peso=600, anc="middle")
    f.texto(188, 168, "M13 a M15", 9, anc="middle")

    f.rect(232, 136, 164, 46, relleno="#F8F9FA", rx=3)
    f.texto(314, 154, "Operación en Régimen Etapa 1", 9, peso=600, anc="middle")
    f.texto(314, 168, "Desde Mes 16 hasta Mes 56", 9, anc="middle")

    # Bloque Etapa 2
    f.grupo(16, 204, 390, 80, "Etapa 2: Integraciones Extendidas y Transportistas Terceros", rx=4)
    # Fases E2
    f.rect(150, 226, 92, 46, relleno="#F8F9FA", rx=3)
    f.texto(196, 244, "Desarrollo E2", 9, peso=600, anc="middle")
    f.texto(196, 258, "Meses 13 al 18", 9, anc="middle")

    f.rect(248, 226, 68, 46, relleno="#FFFFFF", rx=3)
    f.texto(282, 244, "Marcha blanca", 9, peso=600, anc="middle")
    f.texto(282, 258, "M19 a M20", 9, anc="middle")

    f.rect(322, 226, 74, 46, relleno="#F8F9FA", rx=3)
    f.texto(359, 244, "Régimen Total", 9, peso=600, anc="middle")
    f.texto(359, 258, "M21 a M56", 9, anc="middle")

    # Frentes simultáneos destacados
    f.grupo(16, 294, 390, 96, "Articulación de frentes simultáneos de trabajo", rx=5, relleno="#F8F9FA")
    f.texto(26, 324, "• Ventana M13-15: Soporte/adopción de Etapa 1 en marcha blanca convive con el", 9)
    f.texto(26, 338, "  desarrollo de Etapa 2 (asignaciones de recursos y perfiles segregados).", 9)
    f.texto(26, 354, "• Ventana M19-20: Producción en régimen de Etapa 1 opera en paralelo con la marcha", 9)
    f.texto(26, 368, "  blanca de Etapa 2, compartiendo la fuente maestra y el bus de eventos común.", 9)
    f.texto(26, 382, "• Sprints de software: Iteraciones de dos semanas sincronizadas con comités quincenales.", 9, peso=600)

    # Puertas de salida (Quality Gates contractuales)
    f.grupo(8, 400, 406, 114, "Criterios de salida y aceptación formal (Quality Gates)", rx=5)
    f.marcador(26, 424, 1)
    f.texto(38, 426, "Aceptación formal suscrita por la contraparte técnica de Transportes Curimón S.A.", 9)
    f.marcador(26, 444, 2)
    f.texto(38, 446, "Migración y conciliación del 100 % de las 6.000 vigencias documentales sin inconsistencias.", 9)
    f.marcador(26, 464, 3)
    f.texto(38, 466, "Cero defectos críticos (Severidad 1) abiertos en el sistema de gestión de incidentes.", 9)
    f.marcador(26, 484, 4)
    f.texto(38, 486, "Prueba de recuperación ante desastres (DR) ejecutada exitosamente con RPO < 15 min.", 9, peso=600)

    return f.guardar()


def figura_6_2_pipeline():
    """Pipeline DevSecOps unificado en GitLab CI y puertas de calidad."""
    f = Figura("6-2-pipeline", C6, "V", alto=520)

    # Encabezado temático
    f.grupo(8, 8, 406, 52, "Pipeline DevSecOps unificado en GitLab CI Enterprise", rx=5, peso=600)
    f.texto(16, 32, "Integración y entrega continua con puertas de calidad bloqueantes automáticas.", 9)
    f.texto(16, 44, "Revisión por pares independiente: el autor no cuenta como revisor (Art. 4.3).", 9, peso=600)

    # 5 Fases del pipeline horizontal
    fases = [
        ("1. Merge Request", "RF trazable T-12", 16, 68, 76),
        ("2. Pruebas Unit.", "PyTest >= 80 %", 96, 68, 76),
        ("3. SAST / Calidad", "SonarQube 'A'", 176, 68, 76),
        ("4. Contenedores", "Trivy 0 CVEs", 256, 68, 76),
        ("5. Firma / SBOM", "Cosign SLSA 3", 336, 68, 70),
    ]

    for tit, sub, x, y, w in fases:
        f.grupo(x, y, w, 44, tit, rx=4, tam=9, peso=600)
        f.texto(x + w / 2, y + 36, sub, 9, anc="middle")

    # Flechas entre fases
    f.linea([(92, 90), (96, 90)])
    f.linea([(172, 90), (176, 90)])
    f.linea([(252, 90), (256, 90)])
    f.linea([(332, 90), (336, 90)])

    # Ficha del artefacto inmutable
    f.ficha(211, 126, "Artefacto único inmutable: Promoción del mismo digest SHA-256 (sin reconstrucción)", tam=9, peso=600)

    # Ambientes de Promoción Progresiva
    f.grupo(16, 146, 390, 88, "Ambientes de promoción progresiva en Azure Kubernetes Service (AKS)", rx=5)

    ambientes = [
        ("DEV", "Datos sintéticos", 24, 170, 84),
        ("QA", "Pruebas de carga", 118, 170, 86),
        ("PREPROD", "Staging y seguridad", 212, 170, 94),
        ("PROD", "Canario / Blue-Green", 314, 170, 84),
    ]

    for nom, desc, x, y, w in ambientes:
        f.rect(x, y, w, 48, relleno="#FFFFFF", rx=3)
        f.texto(x + w / 2, y + 20, nom, 9, peso=600, anc="middle")
        f.texto(x + w / 2, y + 36, desc, 9, anc="middle")

    # Flechas entre ambientes
    f.linea([(108, 194), (118, 194)])
    f.linea([(204, 194), (212, 194)])
    f.linea([(306, 194), (314, 194)])

    # Mecanismos de Reversión y Rollback
    f.grupo(16, 244, 390, 126, "Mecanismo de reversión segura y resiliencia de datos", rx=5, relleno="#F8F9FA")
    f.texto(26, 274, "• Detección automática: Si un SLI de latencia o error falla en PROD tras el despliegue,", 9)
    f.texto(26, 288, "  el cluster ejecuta rollback automático a la versión previa estable en < 60 s.", 9)
    f.texto(26, 302, "• Reversión de datos: Migraciones de base de datos diseñadas con scripts reversibles", 9)
    f.texto(26, 316, "  (expand/contract). Las nuevas columnas admiten nulos durante el período de prueba.", 9)
    f.texto(26, 330, "• Preservación de eventos: El bus Kafka/Event Hubs retiene los eventos no procesados,", 9)
    f.texto(26, 344, "  garantizando que ningún ping telemático o viaje se pierda durante la reversión.", 9)
    f.texto(26, 358, "• Aislamiento DR: Las pruebas de recuperación operan en suscripción independiente.", 9, peso=600)

    # Bloque inferior: Políticas y Gobernanza
    f.grupo(8, 380, 406, 132, "Políticas de seguridad DevSecOps y cumplimiento SLSA Nivel 3", rx=5)
    f.marcador(26, 404, 1)
    f.texto(38, 406, "Prohibición de modificaciones manuales en consola; infraestructura 100 % como código (IaC).", 9)
    f.marcador(26, 426, 2)
    f.texto(38, 428, "Escaneo obligatorio de dependencias de terceros; bloqueo ante vulnerabilidades CVE críticas.", 9)
    f.marcador(26, 448, 3)
    f.texto(38, 450, "Generación obligatoria de SBOM (Software Bill of Materials) en formato CycloneDX firmado.", 9)
    f.marcador(26, 470, 4)
    f.texto(38, 472, "Trazabilidad completa: cada imagen en producción se vincula al commit y al autor en GitLab.", 9)
    f.marcador(26, 492, 5)
    f.texto(38, 494, "Dos revisores de código obligatorios para aprobar cualquier fusión hacia la rama principal.", 9, peso=600)

    return f.guardar()


FIGURAS = [figura_6_1_hitos, figura_6_2_pipeline]
