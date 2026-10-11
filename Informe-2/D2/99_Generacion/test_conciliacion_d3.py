import json
import subprocess
import sys
import unittest
from pathlib import Path


GENERACION = Path(__file__).resolve().parent
SALIDA = GENERACION / "salida_temporal"


class ConciliacionD3Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        subprocess.run(
            [sys.executable, str(GENERACION / "generar_plan_detallado.py")],
            check=True,
            cwd=GENERACION,
        )
        cls.plan = json.loads(
            (SALIDA / "plan_detallado.json").read_text(encoding="utf-8")
        )

    def test_innovacion_2_usa_calendario_conciliado(self):
        paquete = next(
            p for p in self.plan["paquetes"] if p["codigo"] == "12.2"
        )
        self.assertEqual(paquete["ventanas"], [[6, 9], [16, 18]])

    def test_innovacion_2_traza_paquetes_tecnicos(self):
        paquete = next(
            p for p in self.plan["paquetes"] if p["codigo"] == "12.2"
        )
        self.assertEqual(paquete["paquetes_relacionados"], ["4.1", "4.2"])

    def test_no_conserva_alerta_m4_m8(self):
        html = (SALIDA / "EDT_Gantt_Proyecto_Completo.html").read_text(
            encoding="utf-8"
        )
        self.assertNotIn("piloto en M4", html)
        self.assertIn("piloto de 10 camiones en M6", html)


if __name__ == "__main__":
    unittest.main()
