$ErrorActionPreference = 'Stop'
$root = (Get-Location).Path
$inputDir = Join-Path $root 'Informe-3/d2'
$out = Join-Path $root 'Informe-3/AUDIT-Informe3-Modelo-Economico.xlsx'
$excel = New-Object -ComObject Excel.Application
$excel.DisplayAlerts = $false
$excel.Visible = $false
function Add-Sheet($name) {
    $sheet = $book.Worksheets.Add([Type]::Missing, $book.Worksheets.Item($book.Worksheets.Count))
    $sheet.Name = $name
    return $sheet
}
function Set-Row($sheet, $row, $values) {
    for ($i=0; $i -lt $values.Count; $i++) {
        $cell = $sheet.Cells.Item($row,$i+1)
        $v = $values[$i]
        if ($v -is [string] -and $v.StartsWith('=')) { $cell.Formula = $v }
        elseif ($null -ne $v) { $cell.Value2 = $v }
    }
}
function Header($sheet,$range) {
    $r = $sheet.Range($range)
    $r.Font.Bold = $true
    $r.Font.Color = 16777215
    $r.Interior.Color = 6373678
}
try {
    $source = $excel.Workbooks.Open((Join-Path $inputDir 'D2_MODELO_TRABAJO_OFERTA_D2.xlsx'),0,$true)
    $book = $excel.Workbooks.Open((Join-Path $inputDir 'D2_RESUMEN_MANDANTE_OFERTA_D2.xlsx'),0,$true)
    $excel.Calculation = -4135
    $keep = @('RESUMEN','PARÁMETROS','COSTOS DE OPERACION','TARIFAS DE OPERACION','FLUJO DE CAJA NETO','FLUJO DE CAJA COMPLETO','PCUESFUERZO')
    for ($i=$book.Worksheets.Count; $i -ge 1; $i--) {
        $sheet = $book.Worksheets.Item($i)
        if ($sheet.Name -notin $keep) { $sheet.Delete() | Out-Null }
        elseif ($sheet.Name -ne 'RESUMEN') { $sheet.Cells.Clear() | Out-Null }
    }
    $targets = @{}
    foreach ($original in $source.Worksheets) {
        $name = $original.Name
        $targets[$name] = if ($name -eq 'Parámetros') { Add-Sheet 'Parámetros D2' } else { Add-Sheet $name }
    }
    foreach ($original in $source.Worksheets) {
        $name = $original.Name
        $target = $targets[$name]
        $range = $original.UsedRange
        $dest = $target.Range($target.Cells.Item(1,1),$target.Cells.Item($range.Rows.Count,$range.Columns.Count))
        $dest.Value2 = $range.Value2
        $formulas = $range.Formula
        for ($i=1; $i -le $range.Rows.Count; $i++) {
            for ($j=1; $j -le $range.Columns.Count; $j++) {
                $v = $formulas[$i,$j]
                if ($v -is [string] -and $v.StartsWith('=')) {
                    if ($name -eq 'Indicadores' -and $i -eq 7 -and $j -eq 2) { continue }
                    $dest.Cells.Item($i,$j).Formula = ($v -replace "(?:'Parámetros'|Parámetros)!", "'Parámetros D2'!")
                }
            }
        }
        Header $target ($target.Range($target.Cells.Item(1,1),$target.Cells.Item(1,$range.Columns.Count)).Address(0,0))
        $target.UsedRange.Columns.AutoFit() | Out-Null
    }

    $p = $book.Worksheets.Item('Parámetros D2')
    Set-Row $p 19 @('USD en CLP',900)
    Set-Row $p 20 @('EUR en CLP',1000)
    Set-Row $p 21 @('UF en CLP',40000)
    Set-Row $p 22 @('Reserva D4',152699775)
    Set-Row $p 23 @('Mes de desembolso de reserva en sensibilidad',12)
    Set-Row $p 24 @('Shock de costo',0.05)
    Set-Row $p 25 @('Shock de ingreso',-0.05)
    Set-Row $p 26 @('IVA adicional calibración por mes',114000)
    Set-Row $p 27 @('Capital inicial adicional en escenario H5 y reserva',400000000,'Supuesto aprobado por D1. 80 % banco y 20 % socios en M1. Disponibilidad y comisiones pendientes.')
    Set-Row $p 28 @('Seriedad de oferta, escenario preoperacional',2812500)
    Set-Row $p 29 @('Cierre de coberturas M56',13800000)
    Set-Row $p 30 @('Activar reserva en estrés combinado',1)
    Set-Row $p 31 @('Primer mes de atraso de H5 en estrés',13)
    foreach ($cfg in @(@('B2',2,0,0.2),@('B4',2,0,10000000000),@('B12',1,0,1),@('B13',1,12,13),@('B23',1,1,56),@('B24:B25',2,-1,1),@('B27',2,0,10000000000),@('B30',1,0,1))) {
        $r = $p.Range($cfg[0])
        $r.Validation.Add([int]$cfg[1],1,1,[double]$cfg[2],[double]$cfg[3])
        $r.Locked = $false
        $r.Interior.Color = 14277081
    }
    $fx = $book.Worksheets.Item('PARÁMETROS')
    Set-Row $fx 1 @('Conversiones del Resumen')
    $fx.Range('B4').Formula = "='Parámetros D2'!B19"
    $fx.Range('B5').Formula = "='Parámetros D2'!B20"
    $fx.Range('B6').Formula = "='Parámetros D2'!B21"
    $admin = Add-Sheet 'Gastos Administrativos'
    Set-Row $admin 1 @('Partida','Mes de pago','Neto CLP','Fuente','Criterio')
    $n=2
    foreach ($item in (Import-Csv (Join-Path $inputDir 'AUD-16_CALENDARIO_ADMIN_D1.csv') -Encoding UTF8)) {
        Set-Row $admin $n @($item.id,[int]$item.mes_caja,[double]$item.importe_clp_neto,$item.fuente,$item.criterio)
        $n++
    }
    $admin.Range("C2:C$($n-1)").Locked = $false
    Set-Row $admin ($n+1) @('Cierre de coberturas',56,"='Parámetros D2'!B29",'D1, salida en M56','Extensión de garantía y cola de ciberriesgo')
    Set-Row $admin ($n+3) @('Overhead','Pendiente',$null,'D1/D2','Conciliar gerencia, administración, contabilidad y legal con RRHH y R-24.')
    Set-Row $admin ($n+4) @('Seriedad de oferta','Sensibilidad',"='Parámetros D2'!B28",'D1','Escenario preoperacional separado.')
    Set-Row $admin ($n+5) @('Todo riesgo y accidentes del trabajo','Pendiente',$null,'D1/D2','Confirmar base asegurable y evitar duplicar cargas en tarifa integral.')
    $cost = $book.Worksheets.Item('Costos')
    for ($i=2; $i -le 57; $i++) {
        $f = ('=SUMIF(''Gastos Administrativos''!$B$2:$B${0},A{1},''Gastos Administrativos''!$C$2:$C${0})' -f ($n-1),$i)
        try { $cost.Range("E$i").Formula = $f } catch { throw "Costos E${i}: $f | $($_.Exception.Message)" }
        $cost.Range("F$i").Formula = ('=SUMIF(''Gastos Administrativos''!B{0},A{1},''Gastos Administrativos''!C{0})' -f ($n+1),$i)
    }
    $bridge=Add-Sheet 'PUENTE D2'
    Set-Row $bridge 1 @('Grupo','Costo CLP','Costo UF','Venta UF')
    Set-Row $bridge 2 @('Implementación RRHH','=SUM(Costos!G2:G21)')
    Set-Row $bridge 3 @('Implementación bloque D4','=SUM(Costos!B2:B21)')
    Set-Row $bridge 4 @('Implementación calidad','=SUM(Costos!D2:D21)')
    Set-Row $bridge 5 @('Implementación otros servicios','=SUM(Costos!I2:I21,Costos!J2:J57)-SUM(B2:B4)')
    Set-Row $bridge 6 @('Operación RRHH','=SUM(Costos!G22:G57)')
    Set-Row $bridge 7 @('Operación servicios','=SUM(Costos!I22:I57)-B6')
    Set-Row $bridge 9 @('La distribución por componente sigue las fórmulas de la plantilla. La garantía se atribuye a implementación y se paga en M21.')
    for ($i=2;$i -le 7;$i++) {
        $bridge.Range("C$i").Formula = ('=B{0}/''Parámetros D2''!$B$21' -f $i)
        $bridge.Range("D$i").Formula = if ($i -lt 6) { ('=C{0}*''Parámetros D2''!$B$14/SUM($B$2:$B$5)' -f $i) } elseif ($i -eq 6) { "='Parámetros D2'!B15*'Parámetros D2'!B16/'Parámetros D2'!B21-C7" } else { '=C7' }
    }
    $c = $book.Worksheets.Item('COSTOS DE OPERACION')
    $t = $book.Worksheets.Item('TARIFAS DE OPERACION')
    foreach ($pair in @(@('V35',2),@('V45',4),@('AL35',6))) {
        $c.Range($pair[0]).Formula = "='PUENTE D2'!C$($pair[1])"
        $t.Range($pair[0]).Formula = "='PUENTE D2'!D$($pair[1])"
    }
    $t.Range('B47').Formula = "='Parámetros D2'!B14/SUM('PUENTE D2'!B2:B5)-1"
    $net = $book.Worksheets.Item('FLUJO DE CAJA NETO')
    $net.Range('C33').Formula = "=-'PUENTE D2'!C3"
    $net.Range('B35').Formula = "=-'PUENTE D2'!C5"
    $net.Range('O35').Formula = "=-'PUENTE D2'!C7"
    $complete = $book.Worksheets.Item('FLUJO DE CAJA COMPLETO')
    $complete.Range('B23').Formula = '=Indicadores!B2'
    $complete.Range('B26').Formula = '=Indicadores!B3'
    $pcu = $book.Worksheets.Item('PCUESFUERZO')
    foreach ($address in @('I164','N39','N52','N55')) { $pcu.Range($address).Value2 = 'Pendiente de conciliación PCU' }
    $flow = $book.Worksheets.Item('Flujo de Caja')
    $income = Add-Sheet 'Ingresos'
    Set-Row $income 1 @('Mes','Hito','Fracción','Variable neto CLP','Facturación neta CLP','Cobro neto CLP')
    for ($i=2;$i -le 58;$i++) {
        foreach ($col in @('A','B','C','D','E','F')) {
            $income.Range("$col$i").Formula = ('=IF(''Flujo de Caja''!{0}{1}="","",''Flujo de Caja''!{0}{1})' -f $col,$i)
        }
    }
    $fin = Add-Sheet 'Financiamiento'
    Set-Row $fin 1 @('Mes','Capital inicial','Aporte propio','Crédito inicial','Interés banco','Interés línea','Giro línea','Pago línea','Saldo línea','Pago banco','Saldo banco','Caja acumulada')
    for ($i=2;$i -le 58;$i++) {
        Set-Row $fin $i @("='Flujo de Caja'!A$i",('=IF(A{0}=MIN($A$2:$A$58),''Parámetros D2''!B4,0)' -f $i),("=B$i-D$i"),('=B{0}*''Parámetros D2''!B5' -f $i),"='Flujo de Caja'!P$i","='Flujo de Caja'!Q$i","='Flujo de Caja'!R$i","='Flujo de Caja'!S$i","='Flujo de Caja'!T$i","='Flujo de Caja'!U$i","='Flujo de Caja'!V$i","='Flujo de Caja'!W$i")
    }
    $ind = $book.Worksheets.Item('Indicadores')
    $ind.Range('B7').Formula = '=SUMPRODUCT(--(COUNTIF(Proveedores!A2:A281,Proveedores!A2:A281)>1))'
    $ind.Range('C3').Value2 = 'Fila A M1–M56. Caso base consolidado.'
    Set-Row $ind 9 @('Estado','Avance consolidado','Ver decisiones y respaldos pendientes en Resumen Ejecutivo.')
    Set-Row $ind 10 @('Margen sobre ventas','=1-SUM(Costos!K2:K57)/SUM(Ingresos!E2:E57)','La plantilla conserva utilidad sobre costo en RESUMEN.')
    Set-Row $ind 11 @('TIR anual efectiva','=(1+B3)^''Parámetros D2''!B18-1','Equivalencia matemática. Presentar con el VAN y la TIR mensual.')
    Set-Row $ind 12 @('Venta neta de equilibrio nominal','=SUM(Costos!K2:K57)','Costos netos del escenario fijados. Umbral EBITDA cero sin intereses ni IVA.')
    Set-Row $ind 13 @('Venta neta de equilibrio VAN cero','=NPV(''Parámetros D2''!B10,Costos!K2:K57)/NPV(''Parámetros D2''!B10,Ingresos!F2:F57)*SUM(Ingresos!E2:E57)','Escala de cobros constante y calendario base. Se conserva M57 fuera del VAN base.')
    $sens=Add-Sheet 'Sensibilidad'
    Set-Row $sens 1 @('Escenario','VAN CLP','TIR mensual','Caja mínima','Uso máximo de línea','Déficit sin cubrir','Criterio')
    Set-Row $sens 2 @('Base','=Indicadores!B2','=Indicadores!B3','=Indicadores!B6','=Indicadores!B5','=MAX(0,-D2)','Caso de oferta con cobro H5 en M12.')
    Set-Row $sens 3 @('Aumento de costos','=NPV(''Parámetros D2''!B10,B11:B66)','=IRR(B11:B66,Indicadores!B3)',$null,$null,$null,'Precio fijo. Variación aplicada a costos netos.')
    Set-Row $sens 4 @('Caída de cobros','=NPV(''Parámetros D2''!B10,C11:C66)','=IRR(C11:C66,Indicadores!B3)',$null,$null,$null,'Calendario fijo. Variación aplicada a cobros netos.')
    Set-Row $sens 5 @('H5 en M13','=NPV(''Parámetros D2''!B10,D11:D66)','=IRR(D11:D66,Indicadores!B3)','=MIN(F11:F66)','=MAX(G11:G66)','=MAX(0,-D5)','Precio fijo. Mantiene la facturación contractual en M12.')
    Set-Row $sens 6 @('Estrés combinado','=NPV(''Parámetros D2''!B10,H11:H66)','=IRR(H11:H66,Indicadores!B3)','=MIN(J11:J66)','=MAX(K11:K66)','=MAX(0,-D6)','H5, reserva, IVA de calibración sin crédito. Refuerzo incluido en base.')
    Set-Row $sens 7 @('Mes de caja mínima en estrés','=INDEX(A11:A66,MATCH(D6,J11:J66,0))')
    Set-Row $sens 8 @('Seriedad de oferta en M0','=Indicadores!B2-''Parámetros D2''!B28')
    Set-Row $sens 10 @('Mes','Fila A: costos','Fila A: cobros','Fila A: H5','IVA neto H5','Caja H5','Línea H5','Fila A: estrés','IVA neto estrés','Caja estrés','Línea estrés','Saldo banco H5','Saldo banco estrés','Caja antes de línea H5','Caja antes de línea estrés','Fila A descontada acumulada')
    for ($i=11;$i -le 66;$i++) {
        $r=$i-9
        $prev=$i-1
        $delta=('(IF(A{0}=''Parámetros D2''!B31,1,0)-IF(A{0}=''Parámetros D2''!B13,1,0))*SUMIF(''Flujo de Caja''!$B$2:$B$57,"H5",''Flujo de Caja''!$C$2:$C$57)*''Parámetros D2''!B14' -f $i)
        Set-Row $sens $i @("='Flujo de Caja'!A$r",('=Ingresos!F{0}-Costos!K{0}*(1+''Parámetros D2''!B24)' -f $r),('=Ingresos!F{0}*(1+''Parámetros D2''!B25)-Costos!K{0}' -f $r),("='Flujo de Caja'!H$r+$delta"),('=''Flujo de Caja''!O{0}+(D{1}-''Flujo de Caja''!H{0})*''Parámetros D2''!B11*''Parámetros D2''!B12' -f $r,$i),$null,$null,('=D{0}-IF(A{0}=''Parámetros D2''!B23,''Parámetros D2''!B22*''Parámetros D2''!B30,0)' -f $i),('=E{0}-IF(COUNTIF(''INN-5 Costos''!$A$3:$A$5,A{0}),''Parámetros D2''!B26*''Parámetros D2''!B12,0)' -f $i))
        foreach ($scenario in @(@('D','E','F','G','L','N',$false),@('H','I','J','K','M','O',$true))) {
            $free,$tax,$cash,$line,$loan,$before,$extra=$scenario
            $initial = if ($extra) { "('Parámetros D2'!B4+'Parámetros D2'!B27)" } else { "'Parámetros D2'!B4" }
            $oldLine = if ($i -eq 11) { '0' } else { "$line$prev" }
            $oldLoan = if ($i -eq 11) { '0' } else { "$loan$prev" }
            $oldCash = if ($i -eq 11) { $initial } else { "$cash$prev" }
            $loanStart = if ($i -eq 11) { "$initial*'Parámetros D2'!B5" } else { $oldLoan }
            $sens.Range("$before$i").Formula = "=$oldCash+$free$i+$tax$i-$oldLine*'Parámetros D2'!B7-$oldLoan*'Parámetros D2'!B6"
            $sens.Range("$line$i").Formula = "=MIN('Parámetros D2'!B8,MAX(0,$oldLine-$before$i))"
            $sens.Range("$loan$i").Formula = "=$loanStart-IF(A$i>='Parámetros D2'!B17,MIN($loanStart,MAX(0,$before$i-$oldLine+$line$i)),0)"
            $sens.Range("$cash$i").Formula = "=$before$i-$oldLine+$line$i-($loanStart-$loan$i)"
        }
        $prior = if ($i -eq 11) { '0' } else { "P$prev" }
        $sens.Range("P$i").Formula = ('={0}+''Flujo de Caja''!H{1}/(1+''Parámetros D2''!B10)^A{2}' -f $prior,$r,$i)
    }
    Set-Row $ind 14 @('Recuperación descontada sostenida','=IF(Sensibilidad!P66<0,"Sin recuperación",IF(COUNTIF(Sensibilidad!P11:P66,"<0")=0,MIN(Sensibilidad!A11:A66),LOOKUP(2,1/(Sensibilidad!P11:P66<0),Sensibilidad!A11:A66)+1))','Primer mes tras el último saldo descontado acumulado negativo.')
    $hardware=Add-Sheet 'Hardware del mandante'
    Set-Row $hardware 1 @('N.º','Grupo','Ref. T-11','Modelo de referencia','Cantidad','Precio original','Unitario CLP','Neto CLP','IVA','Mes','Fuente','Observación')
    $n=2
    $section=$false
    foreach ($l in (Get-Content (Join-Path $root 'Informe-3/d4/4.1-presupuesto-equipos.md') -Encoding UTF8)) {
        if ($l -match '^## 5[ .]') { $section=$true }
        elseif ($section -and $l -match '^## ') { break }
        if ($section -and $l -match '^\|\s*\d+\s*\|') {
            $parts = $l.Trim().Substring(1,$l.Trim().Length-2).Split('|').Trim()
            if ($parts.Count -ne 12) { continue }
            foreach ($idx in @(0,4,6,7,9)) { if ($parts[$idx] -match '^[0-9.]+$') { $parts[$idx] = $parts[$idx].Replace('.','') } }
            $v = [object[]]$parts
            foreach ($idx in @(0,4,6,7,9)) { if ($v[$idx] -match '^\d+$') { $v[$idx]=[double]$v[$idx] } }
            if ($v[4] -is [double] -and $v[6] -is [double]) { $v[7]="=E$n*G$n" }
            Set-Row $hardware $n $v
            $n++
        }
    }
    if ($n -eq 2) { throw 'No se identificó el inventario D4' }
    Set-Row $hardware ($n+1) @('Total referencial',$null,$null,$null,$null,$null,$null,("=SUM(H2:H"+($n-1)+")"),$null,$null,'D4 4.1 · precios 2026-11-07','Fuera de caja audIT.')
    $summary = Add-Sheet 'Resumen Ejecutivo'
    Set-Row $summary 1 @('audIT · Transportes Curimón · Informe 3','Avance económico')
    Set-Row $summary 2 @('Costo neto CLP','=RESUMEN!C8')
    Set-Row $summary 3 @('Venta neta CLP','=RESUMEN!H8')
    Set-Row $summary 4 @('Margen sobre ventas','=Indicadores!B10')
    Set-Row $summary 5 @('VAN M0–M56 CLP','=Indicadores!B2')
    Set-Row $summary 6 @('TIR mensual','=Indicadores!B3')
    Set-Row $summary 7 @('Déficit H5 en M13 CLP','=Sensibilidad!F5')
    Set-Row $summary 8 @('Déficit estrés combinado CLP','=Sensibilidad!F6')
    Set-Row $summary 10 @('Versión de insumos','OFERTA_D2 · c601503. Corte GitHub 8c950fa.')
    Set-Row $summary 11 @('Financiamiento','D1 aprobó modelar CLP 400 millones adicionales en el escenario combinado. Disponibilidad y comisiones pendientes.')
    Set-Row $summary 12 @('Margen de la plantilla','Rentabilidad Nominal en RESUMEN divide utilidad por costo.')
    Set-Row $summary 13 @('Filas B29 y B30 de RESUMEN','La plantilla invierte las referencias costo/venta. Para el cotejo usar C8 y H8.')
    Set-Row $summary 14 @('IVA','Base conserva el criterio publicado. Confirmar IVA y crédito fiscal por proveedor.')
    Set-Row $summary 15 @('Innovaciones','Completar atribución, beneficio neto de Curimón y cobertura de horas con cada responsable.')
    Set-Row $summary 16 @('Administración','Confirmar overhead incremental, bases asegurables y partidas de garantías.')
    Set-Row $summary 17 @('Capacidad','D2 debe acreditar capacidad efectiva y refuerzos. PCU pendiente de conciliación.')
    Set-Row $summary 18 @('Compras del mandante','Inventario informativo. Energía y combustible requieren confirmación del pagador.')
    $curva=$book.Worksheets.Item('Curva S')
    $chart=$curva.ChartObjects().Add(340,24,660,320).Chart
    $chart.ChartType=4
    $chart.SetSourceData($curva.Range('A1:D57'))
    foreach ($line in $chart.SeriesCollection()) { $line.XValues = $curva.Range('A2:A57') }
    $chart.HasTitle=$true
    $chart.ChartTitle.Text='Curva S mensual · CLP'
    foreach ($sheet in $book.Worksheets) {
        if ($sheet.Name -in $keep) { continue }
        $sheet.UsedRange.Columns.AutoFit() | Out-Null
        foreach ($column in $sheet.UsedRange.Columns) { if ($column.ColumnWidth -gt 62) { $column.ColumnWidth=62; $column.WrapText=$true } }
        $sheet.UsedRange.Rows.AutoFit() | Out-Null
    }
    foreach ($address in @('B3','B10:B11')) { $ind.Range($address).NumberFormat='0.00%' }
    $sens.Range('C2:C6').NumberFormat='0.00%'
    foreach ($address in @('B4','B6')) { $summary.Range($address).NumberFormat='0.00%' }
    foreach ($address in @('B2:B3','B5','B7:B8')) { $summary.Range($address).NumberFormat='#,##0' }
    foreach ($name in @('Costos','Flujo de Caja','Indicadores','Curva S','Ingresos','Financiamiento','Sensibilidad','Gastos Administrativos','Parámetros D2','PUENTE D2','Resumen Ejecutivo')) {
        $book.Worksheets.Item($name).Protect()
    }
    foreach ($name in @('PARÁMETROS','COSTOS DE OPERACION','TARIFAS DE OPERACION','FLUJO DE CAJA NETO','FLUJO DE CAJA COMPLETO','PCUESFUERZO')) {
        $book.Worksheets.Item($name).Visible=0
    }
    $excel.Calculation=-4105
    $excel.CalculateFullRebuild()
    $checks=@(@('RESUMEN','C8',7984400845.222496),@('RESUMEN','H8',9796810853.033737),@('RESUMEN','G21',1235043315.7805276),@('RESUMEN','G22',0.8366132363093755),@('Sensibilidad','F5',155747160.3787424),@('Sensibilidad','F6',0),@('Hardware del mandante',"H$($n+1)",225384199))
    foreach ($check in $checks) {
        $actual = $book.Worksheets.Item($check[0]).Range($check[1]).Value2
        if ($actual -isnot [double] -or [math]::Abs($actual - $check[2]) -gt 1) { throw "$($check[0]) $($check[1]): $actual esperado $($check[2])" }
        Write-Output "$($check[0]) $($check[1]) = $actual"
    }
    $summary.Activate()
    $book.SaveAs($out,51)
    Write-Output $out
} finally {
    $excel.DisplayAlerts = $false
    if ($book) { $book.Close($false) }
    if ($source) { $source.Close($false) }
    $excel.Quit()
}
