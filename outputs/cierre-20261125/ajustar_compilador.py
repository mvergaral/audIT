from pathlib import Path
p=Path(__file__).resolve().parent/'fuentes/herramientas/compilar.py'
t=p.read_text(encoding='utf-8')
old='"-jobname=" + self.nombre, "-usepretex=" + pre]'
assert old in t
t=t.replace(old,'"-jobname=" + self.nombre]')
old='        cmd.append(self.fuente)'
assert old in t
t=t.replace(old,'''        # En Windows el shell de Perl consume las barras de -usepretex.
        # Un archivo envoltorio conserva literalmente el mismo preámbulo.
        wrapper = os.path.join(self.auxdir, self.nombre + "-entrada.tex")
        with open(wrapper, "w", encoding="utf-8") as w:
            w.write(pre + "\\n" + r"\\input{" + self.fuente.replace(os.sep, "/") + "}\\n")
        cmd.append(wrapper)''')
p.write_text(t,encoding='utf-8')
print('Corregida frontera Python/Perl/TeX mediante archivo de entrada literal.')
