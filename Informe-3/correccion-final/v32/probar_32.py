"""Prueba de propagación de la planilla 3.2 en copias recalculadas con LibreOffice.

Uso: /usr/bin/python3 probar_32.py PLANILLA.xlsx DIRECTORIO_TEMPORAL
Apaga cada interruptor de la 3.2 y comprueba que el resultado se mueve en la dirección esperada.
"""
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lo  # noqa: E402

CASOS = [
    ('madurez apagada', {'B70': 0}, 'costo', '>'),
    ('montaje sin sustitución', {'B59': 0}, 'costo', '>'),
    ('campo interno 320 h', {'B78': 320}, 'costo', '>'),
    ('amortización bullet M21', {'B84': 0}, 'interes_banco', '>'),
    ('soporte mensual (mismo total salvo comisión)', {'B87': 0}, 'costo', '≈'),
]


def main(planilla, tmp):
    py = os.environ.get('AUDIT_PYTHON', 'python3')
    ind = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'indicadores.py')
    leer = lambda p: eval(subprocess.run([py, '-I', '-c', (
        'import sys,contextlib,io; sys.path.insert(0,%r)\nimport indicadores\n'
        'with contextlib.redirect_stdout(io.StringIO()): r=indicadores.resumen(%r)\nprint(repr(r))'
    ) % (os.path.dirname(ind), p)], capture_output=True, text=True, check=True).stdout)
    base = leer(planilla)
    desk = lo.connect()
    fallas = 0
    for nombre, cambios, clave, signo in CASOS:
        doc = lo.open_doc(desk, planilla)
        pc = doc.Sheets.getByName('Parámetros corrección')
        pc.unprotect('')
        for ref, val in cambios.items():
            pc.getCellRangeByName(ref).setValue(val)
        doc.calculateAll()
        out = os.path.join(tmp, nombre.replace(' ', '_') + '.xlsx')
        lo.save_xlsx(doc, out)
        doc.close(True)
        r = leer(out)
        ok = {'>': r[clave] > base[clave] + 1, '≈': abs(r[clave] - base[clave]) < 1e5}[signo]
        ok = ok and r['celdas_error'] == 0 and r['identidad_max'] < 1
        fallas += not ok
        print(f"{'OK ' if ok else 'FALLA'} {nombre:28} {clave}: {base[clave]/1e6:,.2f} -> {r[clave]/1e6:,.2f} M"
              f" | margen {r['margen']:.2%} | errores {r['celdas_error']}")
    lo.close(desk)
    sys.exit(1 if fallas else 0)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
