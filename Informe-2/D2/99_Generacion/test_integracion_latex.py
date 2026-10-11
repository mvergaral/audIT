import unittest
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
CONTENIDO = (
    ROOT
    / "recursos"
    / "Formato-Oferta-audIT"
    / "subdocumentos"
    / "07-plan-trabajo"
    / "contenido.tex"
)


class IntegracionLatexTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.texto = CONTENIDO.read_text(encoding="utf-8")

    def test_enlaza_edt_general_vectorial(self):
        self.assertIn(
            "subdocumentos/07-plan-trabajo/graficos/edt-general.pdf",
            self.texto,
        )

    def test_enlaza_gantt_general_vectorial(self):
        self.assertIn(
            "subdocumentos/07-plan-trabajo/graficos/gantt-general.pdf",
            self.texto,
        )

    def test_no_conserva_figuras_tikz(self):
        self.assertNotIn(r"\begin{tikzpicture}", self.texto)
        self.assertNotIn(r"\begin{figuraNativa}", self.texto)

    def test_archivos_graficos_disponibles_y_etiquetas_unicas(self):
        base = ROOT / 'recursos/Formato-Oferta-audIT'
        entries = re.findall(r'\\(?:anexoGrafico|figuraHorizontal)\{([^}]+)\}\{[^}]+\}\{([^}]+)\}', self.texto)
        labels = [label for _, label in entries]
        self.assertEqual(len(labels), len(set(labels)))
        for path, label in entries:
            self.assertTrue((base / path).is_file(), path)
            self.assertIn(r'\figref{' + label + '}', self.texto)


if __name__ == "__main__":
    unittest.main()
