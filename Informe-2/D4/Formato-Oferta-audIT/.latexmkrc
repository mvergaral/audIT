# Compilación con LuaLaTeX desde la raíz del proyecto.
# Las herramientas de herramientas/ usan este mismo archivo.
$pdf_mode = 4;              # lualatex
$lualatex = 'lualatex -interaction=nonstopmode -halt-on-error -file-line-error %O %S';
$bibtex_use = 1.5;          # biber solo si hay citas
$recorder = 1;              # dependencias reales desde el .fls
$max_repeat = 6;

use Cwd;
my $raiz = getcwd();
$ENV{'TEXINPUTS'} = join(':', "$raiz/estilo//", "$raiz/fuentes//", "$raiz/temas//",
                              "$raiz/portadas//", "$raiz/formularios//",
                              "$raiz/configuracion//", "$raiz//", '') ;
$ENV{'BIBINPUTS'} = "$raiz/referencias//:";
