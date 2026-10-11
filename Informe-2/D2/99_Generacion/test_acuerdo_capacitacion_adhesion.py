"""Controles de la malla y casos de borde del acuerdo de conciliación."""
import unittest
from acuerdo_capacitacion_adhesion import calcular_red, leer_red, contar_firmados, ROOT


class AcuerdoTest(unittest.TestCase):
    def test_adelanto_y_holguras_sin_cambiar_termino(self):
        red = calcular_red(leer_red())
        self.assertEqual((red['A13']['ES'], red['A13']['EF']), (182, 222))
        self.assertEqual((red['A13']['HT'], red['A13']['HL']), (38, 18))
        self.assertEqual(red['A06']['HL'], 24)
        self.assertEqual(red['A25']['EF'], 420)
        self.assertEqual(sum(v['HT'] == 0 for v in red.values()), 13)

    def test_material_tardio_impide_iniciar_antes_de_disponibilidad(self):
        red = calcular_red(leer_red(), disponibilidad=195)
        self.assertEqual(red['G13']['ES'], 195)
        self.assertEqual(red['A13']['ES'], 195)
        self.assertEqual(red['A13']['EF'], 235)
        self.assertEqual(red['A15']['ES'], 240)

    def test_atraso_agota_holgura_y_demora_marcha_blanca(self):
        red = calcular_red(leer_red(), disponibilidad=205)
        self.assertEqual(red['A13']['EF'], 245)
        self.assertEqual(red['A15']['ES'], 245)

    def test_firma_no_equivale_a_activacion_o_consentimiento(self):
        record = dict(rut='RUT-FICTICIO-01', poblacion_inicial=True, modalidad='datos',
                      firma_mandante=True, firma_representante=True, representante_autorizado=True,
                      vigente=True, registrado='2027-10-31', firma='2027-10-31',
                      instalado=False, activado=False, consentimiento_conductor=False)
        self.assertEqual(contar_firmados([record, dict(record, modalidad='completa')]), 1)
        for key in ('vigente','firma_mandante','firma_representante','representante_autorizado','poblacion_inicial'):
            self.assertEqual(contar_firmados([dict(record, **{key:False})]), 0, key)
        self.assertEqual(contar_firmados([dict(record, registrado='2027-11-01')]),0)
        self.assertEqual(contar_firmados([dict(record, firma='2027-11-01')]),0)
        self.assertEqual(contar_firmados([dict(record, revocado=True)]),0)
        self.assertLess(59/148, .4)
        self.assertGreaterEqual(60/148, .4)


if __name__ == '__main__':
    unittest.main()
