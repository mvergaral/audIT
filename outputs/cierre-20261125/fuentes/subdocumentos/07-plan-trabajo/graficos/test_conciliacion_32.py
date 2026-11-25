"""Comprueba el puente mensual entre presupuesto, tareas y capacidad interna."""
import unittest
from conciliar_32 import construir, PLANILLA, calcular_red
from pathlib import Path
import json


class Conciliacion(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.d = construir(PLANILLA)

    def test_esfuerzo_total_y_mensual_se_conserva(self):
        self.assertAlmostEqual(sum(x['horas'] for x in self.d['asignaciones'] if x['mes']<=20),99626.6666666667)
        self.assertAlmostEqual(sum(x['horas'] for x in self.d['asignaciones'] if x['mes']>=21),84606)
        for original in self.d['capacidad']:
            actual=sum(x['horas'] for x in self.d['asignaciones'] if (x['mes'],x['perfil'])==(original['mes'],original['perfil']))
            self.assertAlmostEqual(actual,original['horas'],places=6)

    def test_no_costo_ni_horas_negativas_o_paquetes_ajenos(self):
        for a in self.d['asignaciones']:
            self.assertGreaterEqual(a['horas'],0)
            self.assertIn(a['paquete'],self.d['paquetes'])
        self.assertEqual(set(self.d['paquetes']),{a['paquete'] for a in self.d['asignaciones']})

    def test_montaje_preserva_inventario_y_terminales(self):
        self.assertEqual(sum(x['kits'] for x in self.d['montaje']),182)
        self.assertEqual({x['mes'] for x in self.d['montaje']},{6,7,8,9})
        self.assertEqual(len({x['terminal'] for x in self.d['montaje']}),5)

    def test_operacion_conserva_suplencias_y_campo(self):
        a=self.d['asignaciones']
        self.assertEqual(sum(x['horas'] for x in a if x['paquete']=='13.1'),40320)
        self.assertEqual(sum(x['horas'] for x in a if x['paquete']=='13.3'),2880)

    def test_red_respeta_dependencias_hitos_y_limites(self):
        p=Path(__file__).parent/'red-3.2.json'
        nodes=calcular_red(json.loads(p.read_text(encoding='utf-8'))['nodos'])
        by={n['id']:n for n in nodes}
        for n in nodes:
            self.assertGreaterEqual(n['HT'],0,n['id'])
            self.assertGreaterEqual(n['HL'],0,n['id'])
            if 'limite' in n:self.assertLessEqual(n['EF'],n['limite'],n['id'])
            for pred in n['predecesoras']:
                v=by[pred['id']]['EF' if pred['tipo']=='FS' else 'ES']+pred.get('lag',0)
                self.assertGreaterEqual(n['ES'],v,n['id'])
        for h,m in {'H1':2,'H2':4,'H3':6,'H4':10,'H5':12,'H6':13,'H7':16,'H8':14,'H9':17,'H10':18,'H11':19,'H12':21}.items():
            d=by[h]['EF']
            self.assertTrue((m-1)*20 <= d <= m*20,(h,d))
        self.assertEqual(by['H6']['ES'],240)
        self.assertEqual(by['H11']['ES'],360)

    def test_reservas_directas_y_cierre_no_se_pierden(self):
        a=self.d['asignaciones']
        self.assertEqual(sum(x['horas'] for x in a if x['mes']>=21 and x['paquete'] in ['6.5','7.2']),1669)
        self.assertEqual(sum(x['horas'] for x in a if x['tarea'].startswith('Guardia de puesta')),960)
        self.assertAlmostEqual(sum(x['horas'] for x in a if x['tarea']=='Banco y configuración de kits'),182*20/60)
        self.assertAlmostEqual(sum(x['horas'] for x in a if x['tarea']=='Integración prueba y recepción de cada kit'),182*140/60)
        self.assertAlmostEqual(sum(x['horas'] for x in a if x['tarea']=='Montaje de balizas base'),210*15/60)
        self.assertTrue(all(x['paquete']=='12.3' for x in a if x['tarea']=='Montaje de balizas base'))
        self.assertAlmostEqual(sum(x['horas'] for x in a if x['tarea']=='Piloto a bordo'),10*140/60)

    def test_toda_asignacion_tiene_ventana_activa(self):
        nodes=calcular_red(json.loads((Path(__file__).parent/'red-3.2.json').read_text(encoding='utf-8'))['nodos'])
        for a in self.d['asignaciones']:
            self.assertTrue(any(a['paquete'] in n['edt'] and n['duracion']>0 and n['ES']<a['mes']*20 and n['EF']>(a['mes']-1)*20 for n in nodes),str(a))


if __name__=='__main__':
    unittest.main()
