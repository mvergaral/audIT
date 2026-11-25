from pathlib import Path
O=Path(__file__).resolve().parent;B=O/'fuentes'
p=B/'subdocumentos/01-empresa/contenido.tex';t=p.read_text(encoding='utf-8')
anchor=r'\subsection{Comités institucionales de gobierno y cadencias de decisión}'
policy=r'''\subsection{Subrogancia de la conducción corporativa durante M1--M20}\label{sec:1-subrogancia}

La dedicación contractual del Jefe de Proyecto no se comparte con la administración ordinaria de la sociedad. El instrumento societario simulado incorporado en el Sobre N.º 1, pieza de poderes de representación, encarga esa conducción a la apoderada corporativa identificada como ACC-TFEP-02 en el registro de accionistas. La \tabref{1-subrogancias} separa las competencias delegadas de la dirección del contrato.

\begin{tabla}[ancho=completo]{Cobertura de funciones corporativas durante la implementación}{1-subrogancias}{L{43mm} L{47mm} X}
Función & Responsable de cobertura & Límite y evidencia \\ \midrule
Administración ordinaria y obligaciones societarias & Apoderada corporativa ACC-TFEP-02 & Poder simulado y reporte a la Junta de Accionistas. \\
Contratos y representación fuera del proyecto & Apoderada corporativa ACC-TFEP-02 & Actos de administración ordinaria dentro del poder; actos extraordinarios requieren acuerdo de Junta. \\
Estrategia, distribución de resultados y actos extraordinarios & Junta de Accionistas & Acta societaria del órgano de propietarios. \\
Dirección y representación de TFEP-01/2026 & Jefe de Proyecto y representante legal nominado & Conserva su dedicación contractual y las atribuciones de aceptación y escalamiento de esta oferta. \\
\end{tabla}

La subrogancia se radica en el órgano de propietarios y no añade un puesto a los 22 profesionales de planta ni utiliza las horas contratadas del Jefe de Proyecto. La delimitación de la \tabref{1-subrogancias} evita contar dos veces su disponibilidad: los poderes societarios delegados no habilitan a modificar alcance, hitos o precio del contrato al margen de sus órganos de gobierno.

'''
assert anchor in t
if r'\label{sec:1-subrogancia}' not in t:t=t.replace(anchor,policy+anchor)
p.write_text(t,encoding='utf-8')
p=B/'administrativo/piezas.tex';t=p.read_text(encoding='utf-8')
needle=r'\label{adm:poderes-fin}'
delegation=r'''\par\medskip
\textbf{Subrogancia corporativa del escenario, acuerdo de Junta del 25-11-2026.} Durante M1--M20, Elena Valenzuela Río (ACC-TFEP-02, accionista del 25\,\%) ejerce como apoderada de la administración ordinaria y de la representación de actos ajenos al contrato TFEP-01/2026, informando a la Junta de Accionistas. Los actos extraordinarios requieren acuerdo de Junta. Alejandro Hermosilla Díaz conserva la representación y dirección del proyecto con su dedicación contractual. La función societaria de la accionista no constituye un puesto adicional de la plantilla de 22 profesionales ni utiliza horas del Jefe de Proyecto. Esta delimitación forma parte del instrumento simulado del ejercicio y se refleja en S1, tabla de subrogancias.

'''
assert needle in t
if 'Subrogancia corporativa del escenario' not in t:t=t.replace(needle,delegation+needle)
p.write_text(t,encoding='utf-8')
p=B/'anexos/observaciones-informe3.tex';t=p.read_text(encoding='utf-8')
lines=t.splitlines()
for i,line in enumerate(lines):
    if r'\observacion[sub=1]{EMP-02}' in line:
        prefix=line.split('}{',2)
        # Los primeros dos argumentos se preservan con un parser de grupos.
        s=line.index('{EMP-02}');args=[];j=s
        while j<len(line):
            if line[j]!='{':j+=1;continue
            dep=1;k=j+1
            while dep:
                if line[k]=='{' and line[k-1]!='\\':dep+=1
                elif line[k]=='}' and line[k-1]!='\\':dep-=1
                k+=1
            args.append(line[j+1:k-1]);j=k
        assert len(args)==4
        lines[i]=line[:s]+'{'+args[0]+'}{'+args[1]+'}{Se incorpora una matriz de subrogancias de la conducción corporativa y un poder societario simulado coherente con la nómina de accionistas. La apoderada corporativa ACC-TFEP-02 cubre administración ordinaria y actos ajenos al proyecto; el Jefe de Proyecto conserva su dedicación contractual sin doble cómputo.}{S1 sección de subrogancia y tabla 1-subrogancias; Sobre N.º 1, instrumento de poderes. Estado: Incorporada documentalmente en el escenario simulado}'
p.write_text('\n'.join(lines)+'\n',encoding='utf-8')
print('Subrogancia corporativa documentada en S1, poder simulado y EMP-02; precio y plantilla intactos.')
