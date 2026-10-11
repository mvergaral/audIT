import unittest
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

    def test_enlaza_edt_publicada_por_d2(self):
        self.assertIn(
            "../../Informe-2/D2/01_EDT/01_Completa/EDT_Completa.png",
            self.texto,
        )

    def test_enlaza_gantt_publicada_por_d2(self):
        self.assertIn(
            "../../Informe-2/D2/02_Gantt/01_Graficos/"
            "Gantt_Completa_M01-M56.png",
            self.texto,
        )

    def test_no_conserva_figuras_tikz(self):
        self.assertNotIn(r"\begin{tikzpicture}", self.texto)
        self.assertNotIn(r"\begin{figuraNativa}", self.texto)


if __name__ == "__main__":
    unittest.main()
