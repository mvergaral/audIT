$ErrorActionPreference = 'Stop'

$projectRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
Push-Location $projectRoot
try {
    $env:TEXINPUTS = 'comun//;'

    xelatex -interaction=nonstopmode -halt-on-error -output-directory=build main.tex
    biber build/main
    xelatex -interaction=nonstopmode -halt-on-error -output-directory=build main.tex
    xelatex -interaction=nonstopmode -halt-on-error -output-directory=build main.tex

    if (-not (Test-Path -LiteralPath 'build\main.pdf')) {
        throw 'La compilacion termino sin generar build\main.pdf.'
    }

    Write-Output "PDF generado: $projectRoot\build\main.pdf"
}
finally {
    Pop-Location
}
