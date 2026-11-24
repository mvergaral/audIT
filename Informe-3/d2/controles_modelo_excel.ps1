# Controles compartidos por la regeneración y la actualización del consolidado.
function Set-ControlesModelo($book, $excel) {
    $excel.Calculation = -4135
    $p = $book.Worksheets.Item('Parámetros D2')
    $flow = $book.Worksheets.Item('Flujo de Caja')
    $cost = $book.Worksheets.Item('Costos')
    $vendors = $book.Worksheets.Item('Proveedores')
    $detail = $book.Worksheets.Item('Detalle proveedores D4')
    $sens = $book.Worksheets.Item('Sensibilidad')
    $adjust = $book.Worksheets.Item('Ajustes de operación')
    $fin = $book.Worksheets.Item('Financiamiento')
    $admin = $book.Worksheets.Item('Gastos Administrativos')
    $summary = $book.Worksheets.Item('Resumen Ejecutivo')
    $ind = $book.Worksheets.Item('Indicadores')
    $personal = $book.Worksheets.Item('Personal')
    $capacity = $book.Worksheets.Item('Capacidad por perfil')
    $benefits = $book.Worksheets.Item('Beneficios Curimón')
    $innov = $book.Worksheets.Item('Innovaciones')
    $protected = @($p,$flow,$cost,$vendors,$detail,$sens,$adjust,$fin,$admin,$summary,$ind,$personal,$capacity,$benefits,$innov)
    foreach ($sheet in $protected) { $sheet.Unprotect(); $sheet.Cells.Locked = $true }
    $entryRows = @(35..39) + @(42..46) + @(49..51)
    $existingEntries = @{}
    foreach ($row in $entryRows) { $existingEntries[$row] = $p.Range("B$row").Value2 }
    $existingAlternative = $p.Range('B54').Value2

    function Sheet($name) {
        try { $s = $book.Worksheets.Item($name) } catch {
            $s = $book.Worksheets.Add([Type]::Missing, $book.Worksheets.Item($book.Worksheets.Count))
            $s.Name = $name
        }
        $s.Unprotect()
        $s.Cells.Locked = $true
        return $s
    }
    function Fill($sheet, $address, $formula) {
        $range = $sheet.Range($address)
        $range.Cells.Item(1,1).Formula = $formula
        $range.FillDown() | Out-Null
    }
    function Validation($sheet,$address,[int]$kind,[int]$op,$first,$second) {
        $r = $sheet.Range($address)
        $r.Validation.Delete()
        if ($kind -eq 7) {
            $scratch = $sheet.Range('ZZ1')
            # FormulaLocal obtiene los nombres y separadores del Excel que está ejecutándose.
            $scratch.Formula = $first
            $local = $scratch.FormulaLocal
            $scratch.ClearContents() | Out-Null
            $r.Validation.Add(7,1,1,$local)
        } elseif ($null -eq $second) {
            $r.Validation.Add($kind,1,$op,$first)
        } else {
            $r.Validation.Add($kind,1,$op,$first,$second)
        }
        $r.Validation.IgnoreBlank = $false
        $r.Validation.ShowError = $true
        $r.Validation.ErrorTitle = 'Valor fuera de rango'
        $r.Validation.ErrorMessage = 'Revisa el rango y las condiciones de esta entrada.'
        $r.Locked = $false
        $r.Interior.Color = 13562367
    }
    function TextInput($sheet,$address) {
        Validation $sheet $address 6 1 0 500
    }
    function Nonnegative($sheet,$address) {
        Validation $sheet $address 2 7 0 $null
    }
    function MonthInput($sheet,$address) {
        Validation $sheet $address 1 1 1 56
    }
    function Toggle($sheet,$address) {
        Validation $sheet $address 1 1 0 1
    }
    function Rate($sheet,$address) {
        Validation $sheet $address 2 1 0 1
    }
    function ExtraHeader($sheet,$address,$labels) {
        for ($index=0; $index -lt $labels.Count; $index++) {
            $sheet.Range($address).Cells.Item(1,$index+1).Value2 = $labels[$index]
        }
        Header $sheet $address
        $sheet.Range($address).ColumnWidth = 25
        $sheet.Range($address).WrapText = $true
        $sheet.Range($address).RowHeight = 33
    }

    $p.Range('B2:B47').Validation.Delete()
    $p.Range('C4').Value2 = 'Supuesto de caja. Acreditar capital, plazo, crédito y aporte antes de cierre.'
    $p.Range('C12').Value2 = 'IVA de caja estimado de LTE y ExpressRoute. El crédito exige respaldo separado.'
    $p.Range('C27').Value2 = 'Supuesto autorizado para simulación. Disponibilidad, tasa, giro, aporte y comisión por acreditar.'
    Set-Row $p 35 @('Mes de desembolso capital base',1,'Supuesto. Aplicar las fechas acreditadas por banco y socios.')
    Set-Row $p 36 @('Mes de desembolso refuerzo H5',1,'Supuesto de estrés, confirmación pendiente.')
    Set-Row $p 37 @('Comprar saldo CP-SEC-05 en estrés',0,'0: sin compra. 1: compra las horas por cubrir al costo de referencia.')
    Set-Row $p 38 @('Meta interna de caja CLP',10000000,'Criterio D1 para M12. Se contrasta en el mes indicado.')
    Set-Row $p 39 @('Mes de comprobación de meta',12,'Meta interna de D1.')
    Set-Row $p 40 @('Conciliación neta D4 en M56',-1,'AUD-16 / AUD-17. Ajuste único de redondeo para reproducir el total mensual del corte.')
    Set-Row $p 41 @('Semilla numérica de TIR',0.8,'Semilla de convergencia del escenario base. Sin efecto sobre los flujos.')
    Set-Row $p 42 @('Comisión bancaria adicional base',0,'CLP. Supuesto hasta confirmar términos del crédito inicial.')
    Set-Row $p 43 @('Mes comisión bancaria base',1,'Supuesto. Confirmar calendario de tesorería.')
    Set-Row $p 44 @('Fracción bancaria del refuerzo',0.8,'Escenario 80/20 de E-24. Registrar aporte por separado en Financiamiento.')
    Set-Row $p 45 @('Tasa bancaria mensual del refuerzo',0.009,'Supuesto E-24. Reemplazar con la tasa del instrumento confirmado.')
    Set-Row $p 46 @('Tasa de reserva D4',0.1,'AUD-16 / D4 4.7. No hay cuantificación validada por riesgo.')
    $h5Calendar = Import-Csv (Join-Path $PSScriptRoot 'AUD-18_CALENDARIO_INGRESOS_E25.csv') |
        Where-Object id_evento -eq 'H5'
    $h5Period = [datetime]::ParseExact($h5Calendar.periodo_hito_o_servicio,'yyyy-MM-dd',[Globalization.CultureInfo]::InvariantCulture)
    $h5LastDay = $h5Period.AddMonths(1).AddDays(-1)
    Set-Row $p 48 @('Periodo contractual H5',$h5Period.ToOADate(),'E-25 y calendario AUD-18. M12.')
    Set-Row $p 49 @('Recepción prevista de factura válida',$h5LastDay.ToOADate(),'Supuesto al cierre de M12. Factura emitida al firmar el acta. Confirmar ambas fechas.')
    Set-Row $p 50 @('Plazo propuesto, días corridos',15,'Desde recepción de factura válida. Sujeto a aceptación de la contraparte.')
    Set-Row $p 51 @('Plazo alternativo, días corridos',30,'Sensibilidad con el mismo punto de partida.')
    Set-Row $p 52 @('Abono estimado con plazo propuesto','=IF(AND(ISNUMBER(B49),ISNUMBER(B50)),B49+B50,"")')
    Set-Row $p 53 @('Abono estimado con plazo alternativo','=IF(AND(ISNUMBER(B49),ISNUMBER(B51)),B49+B51,"")')
    Set-Row $p 54 @('Usar plazo alternativo en tesorería',0,'0: plazo propuesto. 1: plazo alternativo. Recalcula los dos escenarios de caja en Sensibilidad.')
    Set-Row $p 55 @('Abono estimado del escenario','=IF(B54=1,B53,B52)')
    Set-Row $p 56 @('Mes contractual de facturación H5',[double]$h5Calendar.mes_hito_o_servicio,'E-25 y calendario AUD-18.')
    if ($null -ne $existingAlternative) { $p.Range('B54').Value2 = [double]$existingAlternative }
    foreach ($row in $entryRows) {
        $value = $existingEntries[$row]
        if ($null -ne $value) { $p.Range("B$row").Value2 = [double]$value }
    }
    $p.Range('B22').Formula = '=ROUND(SUM(Costos!B2:B57)*B46,0)'
    $p.Range('C22').Value2 = 'Tasa de reserva D4 × costos D4 audIT. Se carga en sensibilidad.'
    $p.Range('B26').Formula = "=ROUND('INN-5 Costos'!E3*B11,0)"
    $p.Range('C26').Value2 = 'IVA potencial mensual de calibración. Fuente INN-5 Costos. Se carga solo en estrés.'
    Validation $p 'B2' 2 1 0 0.2
    foreach ($address in @('B4','B27','B33','B38','B42')) { Nonnegative $p $address }
    foreach ($address in @('B12','B30','B37')) { Toggle $p $address }
    foreach ($address in @('B23','B34:B36','B39','B43')) { MonthInput $p $address }
    Validation $p 'B13' 1 1 12 56
    Validation $p 'B49' 7 1 '=AND(ISNUMBER(B49),INT(B49)=B49,B49>=B48,B49+MAX(B50:B51)<=EOMONTH(B48,MAX(''Flujo de Caja''!$A$2:$A$57)-B56))' $null
    Validation $p 'B50:B51' 7 1 '=AND(ISNUMBER(B50),INT(B50)=B50,B50>=0,ISNUMBER($B$49),$B$49+B50<=EOMONTH($B$48,MAX(''Flujo de Caja''!$A$2:$A$57)-$B$56))' $null
    Toggle $p 'B54'
    Set-Row $p 31 @('Mes de cobro H5 en tesorería','=IF(ISNUMBER(B55),B56+(YEAR(B55)-YEAR(B48))*B18+MONTH(B55)-MONTH(B48),"")','Calculado desde la fecha de recepción y el plazo seleccionado.')
    $p.Range('A13').Value2 = 'Mes de cobro H5 en comparador de oferta'
    foreach ($range in @('B48:B49','B52:B53','B55')) { $p.Range($range).NumberFormat = 'dd/mm/yyyy' }
    $p.Range('A48:C56').WrapText = $true
    $p.Range('A48:C56').RowHeight = 30
    Validation $p 'B24' 2 1 0 1
    Validation $p 'B25' 2 1 -1 0
    Validation $p 'B44' 2 1 0 0.8
    Rate $p 'B45:B46'
    $p.Range('B45:B46').NumberFormat = '0.00%'
    $p.Range('B44').NumberFormat = '0.00%'
    $p.Range('C35:C46').WrapText = $true
    $p.Range('A35:A46').WrapText = $true
    $p.Range('A35:C46').RowHeight = 29

    $adjust.Range('B22:C57').Validation.Delete()
    Validation $adjust 'B22:B57' 7 1 '=AND(ISNUMBER(B22),B22>=0,C22<=MensualidadBase+B22)' $null
    Validation $adjust 'C22:C57' 7 1 '=AND(ISNUMBER(C22),C22>=0,C22<=MensualidadBase+B22)' $null
    TextInput $adjust 'D22:D57'
    Set-Row $adjust 1 @('Mes de servicio','Variable CLP','Descuento CLP','Fuente','Control de entrada')
    Header $adjust 'E1'
    $adjust.Range('E:E').ColumnWidth = 42
    Fill $adjust 'E22:E57' '=IF(AND(ISNUMBER(B22),B22>=0,ISNUMBER(C22),C22>=0,C22<=MensualidadBase+B22),"OK","Revisar variable o descuento")'
    $adjust.Range('A59').Value2 = 'Editar M21–M56 y registrar fuente. Un ajuste inválido queda excluido y se señala en el Resumen Ejecutivo.'
    Fill $flow 'D2:D58' '=SUMIFS(''Ajustes de operación''!$B$2:$B$57,''Ajustes de operación''!$A$2:$A$57,A2,''Ajustes de operación''!$E$2:$E$57,"OK")-SUMIFS(''Ajustes de operación''!$C$2:$C$57,''Ajustes de operación''!$A$2:$A$57,A2,''Ajustes de operación''!$E$2:$E$57,"OK")'
    Fill $flow 'E2:E58' '=C2*''Parámetros D2''!$B$14+IF(AND(A2>=''Parámetros D2''!$B$17,A2<''Parámetros D2''!$B$17+''Parámetros D2''!$B$16),MAX(0,''Parámetros D2''!$B$15+D2),0)'
    Fill $flow 'F2:F58' '=IF(B2="H5",0,C2*''Parámetros D2''!$B$14)+IF(A2=''Parámetros D2''!$B$13,SUMIF($B$2:$B$58,"H5",$C$2:$C$58)*''Parámetros D2''!$B$14,0)+IF(AND(A2-''Parámetros D2''!$B$32>=''Parámetros D2''!$B$17,A2-''Parámetros D2''!$B$32<''Parámetros D2''!$B$17+''Parámetros D2''!$B$16),MAX(0,''Parámetros D2''!$B$15+SUMIF($A$2:$A$58,A2-''Parámetros D2''!$B$32,$D$2:$D$58)),0)'

    $master = Sheet 'Cuadro maestro'
    $master.Range('A19:J23').UnMerge()
    Set-Row $master 1 @('Fase','Componente','Costo CLP','Venta de escenario CLP','Margen','Costo UF','Venta UF','Costo USD','Venta USD','Criterio')
    Header $master 'A1:J1'
    $groups = @(
        @('Personal','G','Dotación y refuerzos'),
        @('Infraestructura y servicios','B','Detalle D4, pagador audIT'),
        @('Licencias','C','GitLab y SonarQube'),
        @('Calidad y capacitación','D','Calendario de campañas'),
        @('Firma automática','L','Firma incluida en el flujo'),
        @('Otros confirmados','H','Incluye talleres y calibración INN-5'),
        @('Administración','E','Calendario administrativo'),
        @('Cierre','F','Extensión de coberturas'))
    $r = 2
    foreach ($phase in @(@('Implementación',2,21),@('Operación',22,57))) {
        $name,$start,$end = $phase
        foreach ($group in $groups) {
            $label,$col,$reason = $group
            Set-Row $master $r @($name,$label,('=SUM(Costos!{0}{1}:{0}{2})' -f $col,$start,$end),$null,$null,$null,$null,$null,$null,$reason)
            $r++
        }
        if ($name -eq 'Implementación') {
            Set-Row $master $r @($name,'Garantía correcto funcionamiento','=SUM(Costos!J2:J57)',$null,$null,$null,$null,$null,$null,'Costo de implementación pagado en M21')
            $r++
        }
    }
    Fill $master 'D2:D10' '=IF(SUM($C$2:$C$10)=0,0,C2/SUM($C$2:$C$10)*SUMPRODUCT(--(Ingresos!$B$2:$B$58<>""),Ingresos!$C$2:$C$58)*''Parámetros D2''!$B$14)'
    $master.Range('D11').Formula = '=IF(RESUMEN!$H$7=0,0,MAX(0,SUM(Ingresos!$E$2:$E$58)-SUM($D$2:$D$10))*(RESUMEN!$H$7-SUM($C$12:$C$18))/RESUMEN!$H$7)'
    Fill $master 'D12:D18' '=IF(RESUMEN!$H$7=0,0,MAX(0,SUM(Ingresos!$E$2:$E$58)-SUM($D$2:$D$10))*C12/RESUMEN!$H$7)'
    Fill $master 'E2:E18' '=IF(D2=0,"",(D2-C2)/D2)'
    Fill $master 'F2:F18' '=C2/''Parámetros D2''!$B$21'
    Fill $master 'G2:G18' '=D2/''Parámetros D2''!$B$21'
    Fill $master 'H2:H18' '=C2/''Parámetros D2''!$B$19'
    Fill $master 'I2:I18' '=D2/''Parámetros D2''!$B$19'
    Set-Row $master 19 @('Total',$null,'=SUM(C2:C18)','=SUM(D2:D18)','=IF(D19=0,"",(D19-C19)/D19)','=SUM(F2:F18)','=SUM(G2:G18)','=SUM(H2:H18)','=SUM(I2:I18)')
    Set-Row $master 20 @('Diferencia de control',$null,'=C19-RESUMEN!C8','=D19-SUM(Ingresos!E2:E58)')
    Set-Row $master 21 @('Plantilla contractual RESUMEN',$null,'=RESUMEN!C8','=RESUMEN!H8')
    Set-Row $master 22 @('Venta de escenario menos plantilla',$null,$null,'=D19-D21')
    $master.Range('D22').Formula = '=ROUND(D19-D21,2)'
    Set-Row $master 23 @('La facturación efectiva de operación se asigna en proporción a la venta contractual de cada componente. Los montos son netos.')
    $master.Range('C2:D22').NumberFormat = '#,##0'
    $master.Range('E2:E19').NumberFormat = '0.00%'
    $master.Range('F2:I19').NumberFormat = '#,##0.00'
    $master.Range('A:A').ColumnWidth = 33
    $master.Range('B:B').ColumnWidth = 33
    $master.Range('C:I').ColumnWidth = 20
    $master.Range('J:J').ColumnWidth = 43
    $master.Range('A1:J1').WrapText = $true
    $master.Range('A1:J1').RowHeight = 29
    $master.Range('A19:J22').Font.Bold = $true
    $master.Protect()

    # H e I preservan pago y crédito con respaldo y su propio mes. K conserva el supuesto.
    ExtraHeader $detail 'K1:M1' @('IVA de caja estimado','Documento/receptor y pago','Documento y periodo de crédito')
    Fill $detail 'K2:K379' '=IF(OR(C2="Circuito de operador ExpressRoute",C2="LTE a bordo"),ROUND(E2*''Parámetros D2''!$B$11,0),"")'
    $detail.Range('H1').Value2 = 'IVA efectivo CLP'
    $detail.Range('I1').Value2 = 'Crédito fiscal CLP'
    Validation $detail 'H2:H379' 7 1 '=OR(H2="",AND(ISNUMBER(H2),H2>=0,L2<>"",ISNUMBER(P2),P2>=1,P2<=57,INT(P2)=P2))' $null
    Validation $detail 'I2:I379' 7 1 '=OR(I2="",AND(ISNUMBER(I2),I2>=0,M2<>"",ISNUMBER(Q2),Q2>=1,Q2<=57,INT(Q2)=Q2))' $null
    Validation $detail 'L2:L379' 7 1 '=OR(H2="",L2<>"")' $null
    Validation $detail 'M2:M379' 7 1 '=OR(I2="",M2<>"")' $null
    Validation $detail 'P2:P379' 1 1 1 57
    Validation $detail 'Q2:Q379' 1 1 1 57
    $detail.Range('A381').Value2 = 'Ingresar respaldo, mes efectivo y luego importe. El mes presupuestado permanece en A. Un pago válido reemplaza el supuesto de la partida.'
    Fill $detail 'N2:N379' '=IF(AND(ISNUMBER(H2),H2>=0,L2<>"",ISNUMBER(P2),P2>=1,P2<=57,INT(P2)=P2),H2,"")'
    Fill $detail 'O2:O379' '=IF(AND(ISNUMBER(I2),I2>=0,M2<>"",ISNUMBER(Q2),Q2>=1,Q2<=57,INT(Q2)=Q2),I2,"")'
    Fill $detail 'R2:R379' '=IF(ISNUMBER(N2),0,IF(ISNUMBER(K2),K2,0))'
    ExtraHeader $detail 'N1:R1' @('IVA efectivo válido','Crédito válido','Mes de pago efectivo','Mes de crédito','Estimación de caja usada')
    $detail.Range('K2:K379').NumberFormat = '#,##0'
    $detail.Range('N2:O379').NumberFormat = '#,##0'
    $vendors.Range('G1').Value2 = 'IVA usado en caja'
    $vendors.Range('H1').Value2 = 'Crédito usado en caja'
    for ($month=1; $month -le 56; $month++) {
        $r = 2+5*($month-1)
        foreach ($v in @($r,($r+3))) {
            $vCrit = "'Detalle proveedores D4'!`$A`$2:`$A`$379,B$v,'Detalle proveedores D4'!`$B`$2:`$B`$379,D$v"
            $vendors.Range("G$v").Formula = ('=SUMIFS(''Detalle proveedores D4''!$R$2:$R$379,{0})+SUMIFS(''Detalle proveedores D4''!$N$2:$N$379,''Detalle proveedores D4''!$P$2:$P$379,B{1},''Detalle proveedores D4''!$B$2:$B$379,D{1})' -f $vCrit,$v)
            $vendors.Range("H$v").Formula = ('=SUMIFS(''Detalle proveedores D4''!$O$2:$O$379,''Detalle proveedores D4''!$Q$2:$Q$379,B{0},''Detalle proveedores D4''!$B$2:$B$379,D{0})' -f $v)
        }
        $vendors.Range("G$($r+4)").ClearContents() | Out-Null
        $vendors.Range("H$($r+4)").ClearContents() | Out-Null
        $vendors.Range("I$($r+1)").Formula = ('=ROUND(E{0}*''Parámetros D2''!$B$11,0)' -f ($r+1))
    }
    $vendors.Range('E277').Formula = $vendors.Range('E277').Formula -replace '-1$',"+'Parámetros D2'!`$B`$40"
    $vendors.Range('G2:I281').NumberFormat = '#,##0'
    $vendors.Range('G2:I281').Interior.Pattern = -4142
    Fill $flow 'K2:K58' '=SUMIFS(Proveedores!$G$2:$G$281,Proveedores!$B$2:$B$281,A2,Proveedores!$D$2:$D$281,"audIT")'
    Fill $flow 'L2:L58' '=SUMIFS(Proveedores!$H$2:$H$281,Proveedores!$B$2:$B$281,A2,Proveedores!$D$2:$D$281,"audIT")'
    $flow.Range('K58').Formula = '=SUMIFS(''Detalle proveedores D4''!$N$2:$N$379,''Detalle proveedores D4''!$P$2:$P$379,A58,''Detalle proveedores D4''!$B$2:$B$379,"audIT")'
    $flow.Range('L58').Formula = '=SUMIFS(''Detalle proveedores D4''!$O$2:$O$379,''Detalle proveedores D4''!$Q$2:$Q$379,A58,''Detalle proveedores D4''!$B$2:$B$379,"audIT")'
    $tax = Sheet 'Conciliación IVA'
    Set-Row $tax 1 @('Mes','IVA ref. audIT','IVA usado caja audIT','Crédito fiscal audIT','IVA ref. Curimón','IVA caja estimado LTE y ExpressRoute','IVA efectivo D4 audIT con respaldo','IVA ref. licencias','IVA potencial calibración','IVA efectivo D4 Curimón con respaldo','Crédito D4 Curimón con respaldo')
    Header $tax 'A1:K1'
    Fill $tax 'A2:A58' '=''Flujo de Caja''!A2'
    Fill $tax 'B2:B58' '=SUMIFS(Proveedores!$I$2:$I$281,Proveedores!$B$2:$B$281,A2,Proveedores!$D$2:$D$281,"audIT")'
    Fill $tax 'C2:C58' '=''Flujo de Caja''!K2*''Parámetros D2''!$B$12'
    Fill $tax 'D2:D58' '=''Flujo de Caja''!L2*''Parámetros D2''!$B$12'
    Fill $tax 'E2:E58' '=SUMIFS(Proveedores!$I$2:$I$281,Proveedores!$B$2:$B$281,A2,Proveedores!$D$2:$D$281,"Curimón")'
    Fill $tax 'F2:F58' '=SUMIFS(''Detalle proveedores D4''!$R$2:$R$379,''Detalle proveedores D4''!$A$2:$A$379,A2,''Detalle proveedores D4''!$B$2:$B$379,"audIT")'
    Fill $tax 'G2:G58' '=SUMIFS(''Detalle proveedores D4''!$N$2:$N$379,''Detalle proveedores D4''!$P$2:$P$379,A2,''Detalle proveedores D4''!$B$2:$B$379,"audIT")'
    Fill $tax 'H2:H58' '=SUMIFS(Proveedores!$I$2:$I$281,Proveedores!$B$2:$B$281,A2,Proveedores!$C$2:$C$281,"Licencias D3")'
    Fill $tax 'I2:I58' '=IF(COUNTIF(''INN-5 Costos''!$A$3:$A$5,A2),''Parámetros D2''!$B$26,0)'
    Fill $tax 'J2:J58' '=SUMIFS(''Detalle proveedores D4''!$N$2:$N$379,''Detalle proveedores D4''!$P$2:$P$379,A2,''Detalle proveedores D4''!$B$2:$B$379,"Curimón")'
    Fill $tax 'K2:K58' '=SUMIFS(''Detalle proveedores D4''!$O$2:$O$379,''Detalle proveedores D4''!$Q$2:$Q$379,A2,''Detalle proveedores D4''!$B$2:$B$379,"Curimón")'
    $tax.Range('A59').Value2 = 'Total'
    foreach ($col in @('B','C','D','E','F','G','H','I','J','K')) {
        $tax.Range("${col}59").Formula = "=SUM(${col}2:${col}58)"
    }
    $tax.Range('A60').Value2 = 'Los importes de referencia, estimación de caja, pago efectivo y crédito fiscal tienen respaldo y bases distintos.'
    $tax.Range('A61').Value2 = 'Las referencias audIT incluyen licencias. El IVA potencial de calibración se carga en el estrés combinado.'
    $tax.Range('B:K').ColumnWidth = 22
    $tax.Range('A1:K1').WrapText = $true
    $tax.Range('A1:K1').RowHeight = 42
    $tax.Range('B2:K59').NumberFormat = '#,##0'
    $tax.Protect()

    $purchases = Sheet 'Adquisiciones'
    $sourcePath = Join-Path $PSScriptRoot '../d4/4.5-matriz-adquisiciones.md'
    $matrix = Get-Content -LiteralPath $sourcePath -Encoding UTF8 -Raw
    $calendar = ($matrix -split '(?m)^## 2\. Orden, pago y disponibilidad para hitos\s*\r?\n',2)[1]
    $calendar = ($calendar -split '(?m)^## 3\. Estrategia',2)[0]
    $purchaseRows = @([regex]::Matches($calendar,'(?m)^\| (A-\d{2}[^|]+) \| ([^|]+) \| ([^|]+) \| ([^|]+) \|\s*$'))
    if ($purchaseRows.Count -ne 8) { throw 'No se encontraron las ocho filas del calendario crítico de D4.' }
    Set-Row $purchases 1 @('Partida y pagador','Orden y pago previstos','Recepción y aceptación requeridas','Condición o alternativa','Mes de orden efectiva','Mes de recepción efectiva','Mes de puesta en servicio','Respaldo')
    Header $purchases 'A1:H1'
    for ($index=0; $index -lt $purchaseRows.Count; $index++) {
        $row = $index+2
        $fields = @($purchaseRows[$index].Groups | Select-Object -Skip 1 | ForEach-Object { $_.Value.Trim() })
        Set-Row $purchases $row $fields
    }
    $purchases.Range('A11').Value2 = 'Fuente: Informe-3/d4/4.5-matriz-adquisiciones.md, §2. Registrar orden, recepción y puesta en servicio con su respaldo.'
    $purchases.Range('A12').Value2 = 'Los meses presupuestados se concilian en Proveedores y Hardware del mandante. Esta hoja registra dependencias y fechas confirmadas.'
    MonthInput $purchases 'E2:G9'
    TextInput $purchases 'H2:H9'
    $purchases.Range('A:A').ColumnWidth = 28
    $purchases.Range('B:D').ColumnWidth = 48
    $purchases.Range('E:G').ColumnWidth = 16
    $purchases.Range('H:H').ColumnWidth = 30
    $purchases.Range('A1:H9').WrapText = $true
    $purchases.Range('A1:H1').RowHeight = 30
    $purchases.Range('A2:H9').Rows.AutoFit() | Out-Null
    $purchases.Protect()

    for ($r=2; $r -le 31; $r++) {
        $criterion = $admin.Range("E$r").Value2
        if ($criterion -match '900\.000\.000.*?(\d+)/12$') {
            if ($null -eq $admin.Range("F$r").Value2) { $admin.Range("F$r").Value2 = [double]900000000 }
            if ($null -eq $admin.Range("G$r").Value2) { $admin.Range("G$r").Value2 = 0.012 }
            if ($null -eq $admin.Range("H$r").Value2) { $admin.Range("H$r").Value2 = [double]$Matches[1] }
            $admin.Range("C$r").Formula = ('=F{0}*G{0}*H{0}/''Parámetros D2''!$B$18' -f $r)
            Rate $admin "G$r"
            Validation $admin "H$r" 1 1 1 56
            $admin.Range("G$r").NumberFormat = '0.00%'
        } elseif ($criterion -match '(\d+) UF') {
            if ($null -eq $admin.Range("F$r").Value2) { $admin.Range("F$r").Value2 = [double]$Matches[1] }
            $admin.Range("G$r").Formula = "='Parámetros D2'!`$B`$21"
            $admin.Range("C$r").Formula = "=F$r*G$r"
        }
    }
    ExtraHeader $admin 'F1:H1' @('Base o cantidad','Tasa o valor unitario','Meses de cobertura')
    MonthInput $admin 'B2:B31'
    Nonnegative $admin 'F2:F31'
    $extras = Sheet 'Gastos por acreditar'
    Set-Row $extras 1 @('Mes','kW sala','kW gabinetes','Horas de referencia sala','CLP/kWh','Horas de grupo de respaldo','L/h grupo','CLP/L','Pagador energía','Pagador combustible','Evidencia energía','Evidencia combustible','Energía audIT CLP','Combustible audIT CLP','Overhead adicional CLP','Seguros adicionales CLP','Evidencia administración','Administración adicional CLP','Estado','Horas de grupo de pruebas','Horas mensuales de sala')
    Header $extras 'A1:U1'
    for ($mes=1; $mes -le 56; $mes++) {
        $extras.Range("A$($mes+1)").Value2 = [double]$mes
    }
    Set-Row $extras 59 @('Parámetro','Valor','Fuente o supuesto')
    Header $extras 'A59:C59'
    Set-Row $extras 60 @('Inicio referencial sala',6,'H3/A07. Confirmar instalación y fecha de energización.')
    Set-Row $extras 61 @('Carga estimada sala kW',1.944,'S4 §4.2.6, balance de cargas. Confirmar medición y alcance de sala.')
    Set-Row $extras 62 @('Consumo de grupo a plena carga L/h',2.68,'S4 §4.2.6, referencia de diseño.')
    Set-Row $extras 63 @('Horas de red de referencia',720,'Mes referencial de 30 días. Registrar consumo o tarifa aplicable.')
    Set-Row $extras 65 @('Las celdas de desembolso se calculan si se asigna pagador, se ingresa el supuesto completo y se documenta su referencia.')
    Set-Row $extras 66 @('Administración registra solo el diferencial tras cobertura de RRHH, R-24, pólizas y garantías ya presupuestadas. El escenario no altera la venta base.')
    Fill $extras 'B2:B57' '=IF(A2>=$B$60,$B$61,0)'
    Fill $extras 'D2:D57' '=IF(A2>=$B$60,$B$63,0)'
    Fill $extras 'G2:G57' '=$B$62'
    Fill $extras 'M2:M57' '=IF(AND(I2="audIT",K2<>"",COUNT(C2,E2)=2,MIN(C2,E2)>=0),(B2*MAX(0,IF(ISNUMBER(U2),U2,D2)-SUM(F2))+C2*IF(ISNUMBER(U2),U2,D2))*E2,0)'
    Fill $extras 'N2:N57' '=IF(AND(J2="audIT",L2<>"",COUNT(F2,H2)=2,MIN(F2,H2)>=0,SUM(F2,T2)<=744),SUM(F2,T2)*G2*H2,0)'
    Fill $extras 'R2:R57' '=IF(AND(Q2<>"",COUNT(O2:P2)=2,MIN(O2:P2)>=0),SUM(O2:P2),0)'
    Fill $extras 'S2:S57' '=IF(AND(K2<>"",L2<>"",Q2<>"",OR(I2="Curimón",AND(I2="audIT",COUNT(C2,E2)=2)),OR(J2="Curimón",AND(J2="audIT",COUNT(F2,H2)=2)),COUNT(O2:P2)=2),"Revisar respaldo","Por cuantificar o acreditar")'
    MonthInput $extras 'B60'
    Nonnegative $extras 'B61:B62'
    Validation $extras 'B63' 1 1 0 744
    foreach ($a in @('C2:C57','E2:E57','H2:H57','O2:P57')) { Nonnegative $extras $a }
    Validation $extras 'F2:F57' 7 1 '=OR(F2="",AND(ISNUMBER(F2),F2>=0,F2<=IF(ISNUMBER(U2),U2,D2),SUM(F2,T2)<=744))' $null
    Validation $extras 'T2:T57' 7 1 '=OR(T2="",AND(ISNUMBER(T2),T2>=0,SUM(F2,T2)<=744))' $null
    Validation $extras 'U2:U57' 7 1 '=OR(U2="",AND(ISNUMBER(U2),U2>=0,U2<=744,SUM(F2)<=U2))' $null
    Validation $extras 'I2:I57' 7 1 '=OR(I2="",I2="audIT",I2="Curimón")' $null
    Validation $extras 'J2:J57' 7 1 '=OR(J2="",J2="audIT",J2="Curimón")' $null
    foreach ($a in @('K2:L57','Q2:Q57')) { TextInput $extras $a }
    $extras.Range('A:A').ColumnWidth = 10
    $extras.Range('B:U').ColumnWidth = 19
    $extras.Range('K:L').ColumnWidth = 24
    $extras.Range('Q:Q').ColumnWidth = 24
    $extras.Range('S:S').ColumnWidth = 31
    $extras.Range('A1:U1').WrapText = $true
    $extras.Range('A1:U1').RowHeight = 33
    $extras.Range('C2:H57').NumberFormat = '#,##0.00'
    $extras.Range('M2:R57').NumberFormat = '#,##0'
    $extras.Protect()
    ExtraHeader $cost 'M1:Q1' @('Inversión T-22','Operación T-22','Administración T-22','RRHH T-22','Control de naturaleza')
    Fill $cost 'M2:M57' '=ROUND(SUMIFS(''Detalle proveedores D4''!$E$2:$E$379,''Detalle proveedores D4''!$A$2:$A$379,A2,''Detalle proveedores D4''!$B$2:$B$379,"audIT",''Detalle proveedores D4''!$C$2:$C$379,"Equipos")+SUMIFS(''Detalle proveedores D4''!$E$2:$E$379,''Detalle proveedores D4''!$A$2:$A$379,A2,''Detalle proveedores D4''!$B$2:$B$379,"audIT",''Detalle proveedores D4''!$C$2:$C$379,"Unidades de prueba"),0)'
    Fill $cost 'N2:N57' '=B2+C2+D2+H2+L2-M2-(O2-E2-F2-J2)'
    Fill $cost 'O2:O57' '=E2+F2+J2+SUMIFS(''Detalle proveedores D4''!$E$2:$E$379,''Detalle proveedores D4''!$A$2:$A$379,A2,''Detalle proveedores D4''!$B$2:$B$379,"audIT",''Detalle proveedores D4''!$C$2:$C$379,"Asesoría legal R-24")'
    Fill $cost 'P2:P57' '=G2'
    Fill $cost 'Q2:Q57' '=SUM(M2:P2)-K2'
    $cost.Range('A59').Value2 = 'Total por naturaleza T-22'
    foreach ($col in @('M','N','O','P','Q')) { $cost.Range("${col}59").Formula = "=SUM(${col}2:${col}57)" }
    $cost.Range('M2:Q59').NumberFormat = '#,##0'
    $cost.Range('A61').Value2 = 'M21 incluye garantía de implementación. La imputación de las 1.669 h de cierres 13.2/13.4 en M21–M24 queda por acreditar con T-15, PCU y nómina.'
    $capacity.Range('H1').Value2 = 'Ajuste incremental neto de cupos base'
    $capacity.Range('H1').WrapText = $true
    $capacity.Range('H1').RowHeight = 33
    foreach ($a in @('D2:D41','F2:F41')) { Nonnegative $capacity $a }
    TextInput $capacity 'I2:I41'
    Validation $capacity 'H2:H41' 7 1 '=OR(H2="",AND(ISNUMBER(H2),H2>=0,I2<>""))' $null
    $personal.Range('A66').Value2 = 'Datos/QA M21–M24: CLP 2.852.000/mes y soporte INN-5: CLP 280.000/mes ya incluidos en Refuerzo presupuestado.'
    for ($r=2; $r -le 57; $r++) {
        $personal.Range("C$r").Formula = ('=SUMIF(''Refuerzo presupuestado''!$A$2:$A$48,A{0},''Refuerzo presupuestado''!$E$2:$E$48)' -f $r)
    }
    Fill $personal 'D2:D57' '=SUM(B2:C2)+SUMIFS(''Capacidad por perfil''!$H$2:$H$41,''Capacidad por perfil''!$A$2:$A$41,A2,''Capacidad por perfil''!$I$2:$I$41,"<>")'

    $cp = Sheet 'CP-SEC-05'
    Set-Row $cp 1 @('Mes','Semana','Perfil / puesto','Horas requeridas','Tarifa ref. CLP/h','Ejecutor','Horas reservadas','Horas compartidas','Evidencia de cobertura','Horas por cubrir','Compra neta estimada')
    Header $cp 'A1:K1'
    $rows = @(Import-Csv (Join-Path $PSScriptRoot 'AUD-14_RESERVAS_CP-SEC-05.csv') -Delimiter ';' -Encoding UTF8 |
        Where-Object { $_.id -match '^\d+$' } | Select-Object -First 11)
    $rates = @{
        'Arquitecto de Solución' = 44000
        'Oficial de Seguridad' = 44000
        'Software A11' = 28000
        'QA A11' = 20000
        'Líder de Operación/SRE' = 32000
    }
    $r=2
    foreach ($entry in $rows) {
        Set-Row $cp $r @([double]$entry.mes.TrimStart('M'),$entry.semana_propuesta,$entry.puesto_propuesto,
            [double]$entry.horas_requeridas,[double]$rates[$entry.puesto_propuesto])
        $r++
    }
    Fill $cp 'J2:J12' '=MAX(0,D2-IF(AND(F2<>"",I2<>""),MIN(D2,SUM(G2:H2)),0))'
    Fill $cp 'K2:K12' '=J2*E2'
    Set-Row $cp 13 @('Total',$null,$null,'=SUM(D2:D12)',$null,$null,$null,$null,$null,'=SUM(J2:J12)','=SUM(K2:K12)')
    $cp.Range('A15').Value2 = 'AUD-14_RESERVAS_CP-SEC-05.csv / E-26 puntos medios. Acreditar las horas antes de reducir el saldo de compra.'
    $cp.Range('A16').Value2 = 'La compra se registra una vez en Sensibilidad. El presupuesto base conserva el refuerzo comprometido.'
    Nonnegative $cp 'E2:E12'
    TextInput $cp 'F2:F12'
    TextInput $cp 'I2:I12'
    Validation $cp 'G2:G12' 7 1 '=OR(G2="",AND(ISNUMBER(G2),G2>=0,SUM(G2:H2)<=D2,F2<>"",I2<>""))' $null
    Validation $cp 'H2:H12' 7 1 '=OR(H2="",AND(ISNUMBER(H2),H2>=0,SUM(G2:H2)<=D2,F2<>"",I2<>""))' $null
    $cp.Range('A:B').ColumnWidth = 10
    $cp.Range('C:C').ColumnWidth = 26
    $cp.Range('D:K').ColumnWidth = 19
    $cp.Range('I:I').ColumnWidth = 35
    $cp.Range('A1:K1').WrapText = $true
    $cp.Range('A1:K1').RowHeight = 32
    $cp.Range('K2:K13').NumberFormat = '#,##0'
    $cp.Protect()

    Set-Row $innov 19 @('Innovación','Partida','Referencia CLP','Mes o ventana','Tratamiento')
    Set-Row $innov 20 @(2,'Desarrollo',16576000,'Implementación EDT 12.2','Atribución de nómina. Cobertura por acreditar.')
    Set-Row $innov 21 @(2,'Operación',16992000,'M21–M56','Atribución de nómina. Solo se agrega brecha acreditada.')
    Set-Row $innov 22 @(3,'Integración y montaje',5700000,'M6–M10 y M16–M18','Estimado. Conciliar imputación en EDT y compras.')
    Set-Row $innov 23 @(3,'Operación',4032000,'M21–M56','Estimado. Confirmar cobertura en nómina.')
    Set-Row $innov 24 @(5,'Inversión y soporte','=SUM(''INN-5 Costos''!E2:E5)+SUMIF(''Refuerzo presupuestado''!B2:B48,"INN-5*",''Refuerzo presupuestado''!E2:E48)','M4–M9, M13–M15 y M21–M56','Desarrollo y soporte en refuerzos. Talleres y calibración en INN-5 Costos.')
    Header $innov 'A19:E19'
    $innov.Range('C20:C24').NumberFormat = '#,##0'
    Set-Row $innov 27 @('Mes','Innovación','Actividad incremental','Pagador','Cantidad','Tarifa neta CLP','Costo ya cubierto CLP','Evidencia y criterio de imputación','Costo bruto','Diferencial neto')
    Header $innov 'A27:J27'
    MonthInput $innov 'A28:A83'
    Validation $innov 'B28:B83' 1 1 1 5
    TextInput $innov 'C28:C83'
    Validation $innov 'D28:D83' 7 1 '=OR(D28="",D28="audIT",D28="Curimón")' $null
    Nonnegative $innov 'E28:G83'
    TextInput $innov 'H28:H83'
    Fill $innov 'I28:I83' '=IF(AND(ISNUMBER(A28),ISNUMBER(B28),C28<>"",OR(D28="audIT",D28="Curimón"),COUNT(E28:G28)=3,MIN(E28:G28)>=0,H28<>""),E28*F28,"")'
    Fill $innov 'J28:J83' '=IF(ISNUMBER(I28),MAX(0,I28-G28),"")'
    $innov.Range('A85').Value2 = 'Escenario de costo incremental. Registrar solo partidas adicionales con fuente. Cargar en costo ya cubierto lo incluido en nómina, compras o refuerzos.'
    $innov.Range('A86').Value2 = 'Sensibilidad carga el diferencial de audIT. El diferencial de Curimón queda en esta hoja y puede usarse para calcular el beneficio neto por innovación.'
    $innov.Range('A27:J27').WrapText = $true
    $innov.Range('A27:J27').RowHeight = 29
    $innov.Range('F:G').ColumnWidth = 19
    $innov.Range('H:H').ColumnWidth = 34
    $innov.Range('I:J').ColumnWidth = 19
    $innov.Range('F28:G83').NumberFormat = '#,##0'
    $innov.Range('I28:J83').NumberFormat = '#,##0'

    Set-Row $benefits 8 @('Innovación','Base de medición','Unidad','Condición')
    Set-Row $benefits 9 @('INN-1','Preparación y verificación de expedientes','Minutos por expediente','Medir tiempo y evitar solape con INN-4')
    Set-Row $benefits 10 @('INN-2','Visitas y tiempo de preparación evitados','Visitas y minutos','Validar línea base y piloto')
    Set-Row $benefits 11 @('INN-3','Acoples y eventos térmicos','Eventos por clase','Kilometraje corresponde al criterio 26')
    Set-Row $benefits 12 @('INN-5','Consumo y siniestralidad','Litros y eventos','Medir con línea base y viajes elegibles')
    Set-Row $benefits 14 @('INN-4 · Recupero bruto de referencia a 36 meses','=Innovaciones!C9*''Parámetros D2''!B16/''Parámetros D2''!B18',$null,'El neto depende del reparto, los costos y la adopción.')
    Set-Row $benefits 17 @('Innovación','Métrica','Unidades evitadas al mes','Valor por unidad CLP','Adopción','Costos y reparto mensual CLP','Beneficio neto mensual CLP','Evidencia')
    $benefitRows = @(
        @('INN-1','Minutos de preparación y verificación evitados'),
        @('INN-2','Visitas adicionales evitadas y pagadas por Curimón'),
        @('INN-2','Minutos de Curimón sin solapamiento con las visitas'),
        @('INN-3','Eventos de acople evitados o resueltos'),
        @('INN-3','Eventos térmicos evitados o resueltos'),
        @('INN-5','Litros de combustible evitados'),
        @('INN-5','Eventos de siniestralidad evitados'))
    for ($i=0; $i -lt $benefitRows.Count; $i++) { Set-Row $benefits ($i+18) $benefitRows[$i] }
    Fill $benefits 'G18:G24' '=IF(AND(COUNT(C18:F18)=4,H18<>"",MIN(C18:F18)>=0,E18<=1),C18*D18*E18-F18,"")'
    Set-Row $benefits 26 @('Ingresar la medición y su fuente para valorizar el beneficio de Curimón. Los resultados quedan fuera de Ingresos audIT.')
    Set-Row $benefits 28 @('INN-4 · Escenario mensual a régimen')
    Set-Row $benefits 29 @('Bruto mensual CLP','Adopción','Reparto a terceros','Costo incremental Curimón CLP','Neto mensual CLP','Evidencia','Alcance')
    $benefits.Range('A30').Formula = '=Innovaciones!C9/''Parámetros D2''!B18'
    $benefits.Range('E30').Formula = '=IF(AND(COUNT(B30:D30)=3,F30<>"",MIN(B30:D30)>=0,MAX(B30:C30)<=1),A30*B30*(1-C30)-D30,"")'
    $benefits.Range('G30').Value2 = 'Ingresar costos y reparto acreditados.'
    foreach ($a in @('A8:D8','A17:H17','A29:G29')) { Header $benefits $a }
    $benefits.Range('B:B').ColumnWidth = 42
    $benefits.Range('C:H').ColumnWidth = 28
    $benefits.Range('A17:H24').WrapText = $true
    $benefits.Range('A17:H24').RowHeight = 32
    $benefits.Range('A29:G30').WrapText = $true
    $benefits.Range('A29:G30').RowHeight = 32
    $benefits.Range('E18:E24').NumberFormat = '0.00%'
    $benefits.Range('B30:C30').NumberFormat = '0.00%'
    $benefits.Range('G18:G24').NumberFormat = '#,##0'

    ExtraHeader $fin 'M1:S1' @('Comisión base','Refuerzo total (estrés)','Refuerzo banco','Refuerzo socios','Comisión estrés','Saldo banco base en estrés','Saldo banco refuerzo en estrés')
    Fill $fin 'B2:B58' '=IF(A2=''Parámetros D2''!$B$35,''Parámetros D2''!$B$4,0)'
    Fill $fin 'M2:M58' '=IF(A2=''Parámetros D2''!$B$43,''Parámetros D2''!$B$42,0)'
    Fill $fin 'N2:N58' '=IF(A2=''Parámetros D2''!$B$36,''Parámetros D2''!$B$27,0)'
    Fill $fin 'O2:O58' '=N2*''Parámetros D2''!$B$44'
    Fill $fin 'P2:P58' '=N2-O2'
    Fill $fin 'Q2:Q58' '=IF(A2=''Parámetros D2''!$B$34,''Parámetros D2''!$B$33,0)'
    $fin.Range('D2').Formula = "=B2*'Parámetros D2'!`$B`$5"
    $fin.Range('D2:D58').FillDown() | Out-Null
    for ($r=2; $r -le 58; $r++) {
        $previous = $r-1
        $bank = if ($r -eq 2) { '0' } else { "V$previous" }
        $line = if ($r -eq 2) { '0' } else { "T$previous" }
        $cash = if ($r -eq 2) { '0' } else { "W$previous" }
        $available = "($cash+H$r+O$r+Financiamiento!B$r-P$r-Q$r-Financiamiento!M$r)"
        $debt = "($bank+Financiamiento!D$r)"
        $flow.Range("R$r").Formula = "=MAX(0,MIN('Parámetros D2'!`$B`$8-$line,-$available))"
        $flow.Range("S$r").Formula = "=MIN($line,MAX(0,$available))"
        $flow.Range("U$r").Formula = "=IF(A$r>='Parámetros D2'!`$B`$17,MIN($debt,MAX(0,$available+R$r-S$r)),0)"
        $flow.Range("V$r").Formula = "=$debt-U$r"
        $flow.Range("W$r").Formula = "=$available+R$r-S$r-U$r"
    }
    $fin.Range('R58:S58').ClearContents() | Out-Null
    Fill $fin 'R2:R57' '=Sensibilidad!R11'
    Fill $fin 'S2:S57' '=Sensibilidad!S11'
    Set-Row $fin 60 @('Evidencia para acreditar','Referencia verificable','Estado')
    Header $fin 'A60:C60'
    $terms = @(
        'H5 · acta, factura y fecha de pago',
        'Capital base · carta de crédito, condiciones y giro',
        'Capital base · compromiso y fecha de aporte',
        'Refuerzo · carta de crédito, condiciones y giro',
        'Refuerzo · compromiso y fecha de aporte',
        'Línea · disponibilidad, tope, condiciones y fecha',
        'Comisiones y garantías de ambos créditos',
        'Calendario intramensual de cobros, pagos y giros')
    for ($i=0; $i -lt $terms.Count; $i++) { $fin.Range("A$($i+61)").Value2 = $terms[$i] }
    TextInput $fin 'B61:B68'
    Fill $fin 'C61:C68' '=IF(B61="","Por acreditar","Referencia ingresada para revisión")'
    $fin.Range('A60:C68').WrapText = $true
    $fin.Range('A60:C68').RowHeight = 42
    $fin.Range('B2:S58').NumberFormat = '#,##0'

    ExtraHeader $sens 'Q10:V10' @('Compra CP-SEC-05 CLP','Saldo de crédito base','Saldo de crédito adicional','Egresos previos al cobro','Caja mínima por orden adverso','Línea residual al inicio')
    ExtraHeader $sens 'W10:X10' @('Gastos adicionales CLP','Innovación incremental audIT')
    Fill $sens 'W11:W66' '=SUMIF(''Gastos por acreditar''!$A$2:$A$57,A11,''Gastos por acreditar''!$M$2:$M$57)+SUMIF(''Gastos por acreditar''!$A$2:$A$57,A11,''Gastos por acreditar''!$N$2:$N$57)+SUMIF(''Gastos por acreditar''!$A$2:$A$57,A11,''Gastos por acreditar''!$R$2:$R$57)'
    Fill $sens 'X11:X66' '=SUMIFS(Innovaciones!$J$28:$J$83,Innovaciones!$A$28:$A$83,A11,Innovaciones!$D$28:$D$83,"audIT")'
    Fill $sens 'Q11:Q66' '=SUMIF(''CP-SEC-05''!$A$2:$A$12,A11,''CP-SEC-05''!$K$2:$K$12)*''Parámetros D2''!$B$37'
    Fill $sens 'H11:H66' '=D11-IF(A11=''Parámetros D2''!$B$23,''Parámetros D2''!$B$22*''Parámetros D2''!$B$30,0)-Q11-W11-X11'
    for ($i=11; $i -le 66; $i++) {
        $frow = $i-9
        $prev = $i-1
        $baseCash = if ($i -eq 11) { '0' } else { "F$prev" }
        $baseLine = if ($i -eq 11) { '0' } else { "G$prev" }
        $baseDebt = if ($i -eq 11) { '0' } else { "L$prev" }
        $stressCash = if ($i -eq 11) { '0' } else { "J$prev" }
        $stressLine = if ($i -eq 11) { '0' } else { "K$prev" }
        $stressDebt = if ($i -eq 11) { '0' } else { "R$prev" }
        $stressExtra = if ($i -eq 11) { '0' } else { "S$prev" }
        $startBase = "($baseDebt+Financiamiento!D$frow)"
        $startStress = "($stressDebt+Financiamiento!D$frow)"
        $startExtra = "($stressExtra+Financiamiento!O$frow)"
        $bankRate = "'Parámetros D2'!`$B`$6"
        $lineRate = "'Parámetros D2'!`$B`$7"
        $extraRate = "'Parámetros D2'!`$B`$45"
        $limit = "'Parámetros D2'!`$B`$8"
        $payStart = "'Parámetros D2'!`$B`$17"
        $sens.Range("N$i").Formula = "=$baseCash+Financiamiento!B$frow+D$i+E$i-$baseLine*$lineRate-$baseDebt*$bankRate-Financiamiento!M$frow"
        $sens.Range("G$i").Formula = "=MIN($limit,MAX(0,$baseLine-N$i))"
        $sens.Range("L$i").Formula = "=$startBase-IF(A$i>=$payStart,MIN($startBase,MAX(0,N$i-$baseLine+G$i)),0)"
        $sens.Range("F$i").Formula = "=N$i-$baseLine+G$i-($startBase-L$i)"
        $sens.Range("O$i").Formula = "=$stressCash+Financiamiento!B$frow+Financiamiento!N$frow+H$i+I$i-$stressLine*$lineRate-$stressDebt*$bankRate-$stressExtra*$extraRate-Financiamiento!M$frow-Financiamiento!Q$frow"
        $sens.Range("K$i").Formula = "=MIN($limit,MAX(0,$stressLine-O$i))"
        $sens.Range("R$i").Formula = "=$startStress-IF(A$i>=$payStart,MIN($startStress,MAX(0,O$i-$stressLine+K$i)),0)"
        $sens.Range("S$i").Formula = "=$startExtra-IF(A$i>=$payStart,MIN($startExtra,MAX(0,O$i-$stressLine+K$i-($startStress-R$i))),0)"
        $sens.Range("M$i").Formula = "=R$i+S$i"
        $sens.Range("J$i").Formula = "=O$i-$stressLine+K$i-($startStress-R$i)-($startExtra-S$i)"
        $sens.Range("T$i").Formula = "=-H$i+D$i+'Flujo de Caja'!G$frow+('Flujo de Caja'!J$frow+(D$i-'Flujo de Caja'!H$frow)*'Parámetros D2'!`$B`$11)*'Parámetros D2'!`$B`$12-I$i+$stressLine*$lineRate+$stressDebt*$bankRate+$stressExtra*$extraRate+Financiamiento!M$frow+Financiamiento!Q$frow"
        $sens.Range("V$i").Formula = "=MAX(0,$limit-$stressLine)"
        $sens.Range("U$i").Formula = "=$stressCash-T$i+V$i"
    }
    $sens.Range('B3').Formula = "=NPV('Parámetros D2'!B10,B11:B66)"
    $sens.Range('A2').Value2 = 'Comparador de oferta'
    $sens.Range('G2').Formula = '="Cobro H5 en M"&''Parámetros D2''!B13&" en el comparador."'
    $sens.Range('A5').Formula = '=IF(ISNUMBER(''Parámetros D2''!B31),"Tesorería · H5 en M"&''Parámetros D2''!B31,"Tesorería · sin fecha para H5")'
    $sens.Range('G5').Value2 = 'El devengo se mantiene en M12 para aislar el plazo de cobro. Si cambia el mes del acta, revisar facturación e IVA.'
    $sens.Range('C5').Formula = '=IFERROR(IRR(D11:D66,''Parámetros D2''!B41),"Sin convergencia")'
    $sens.Range('C6').Formula = '=IFERROR(IRR(H11:H66,''Parámetros D2''!B41),"Sin convergencia")'
    $sens.Range('G6').Value2 = 'H5, reserva y calibración sin crédito. Incluye comisiones, horas y gastos adicionales según entradas.'
    Set-Row $sens 9 @('Meta de caja CLP',"='Parámetros D2'!B38","=INDEX(J11:J66,MATCH('Parámetros D2'!B39,A11:A66,0))-B9",'Holgura de caja en el mes meta')
    Set-Row $sens 68 @('Caja mínima con egresos antes de ingresos','=MIN(U11:U66)','=INDEX(A11:A66,MATCH(B68,U11:U66,0))')
    $sens.Range('A69').Value2 = 'Cota conservadora con línea residual de apertura. Cobros, crédito y aporte del mes se ubican al final. Confirmar disponibilidad y fechas reales.'
    $sens.Range('A70').Value2 = 'Se amortiza primero el crédito base y luego el refuerzo en el escenario combinado. Confirmar la prelación contractual.'
    Set-Row $sens 72 @('Cierre mensual de tesorería','Sin refuerzo ni reserva','Con refuerzo y estrés')
    Header $sens 'A72:C72'
    Set-Row $sens 73 @('Caja M12 CLP','=F22','=J22')
    Set-Row $sens 74 @('Caja M13 CLP','=F23','=J23')
    Set-Row $sens 75 @('Caja M14 CLP','=F24','=J24')
    $sens.Range('B73:C75').NumberFormat = '#,##0'
    $sens.Range('B9:C9').NumberFormat = '#,##0'
    $sens.Range('Q11:X66').NumberFormat = '#,##0'
    $sens.Range('B68').NumberFormat = '#,##0'
    $sens.Range('A68').WrapText = $true
    $sens.Range('A68').RowHeight = 32

    $ind.Range('B3').Formula = '=IFERROR(IRR(''Flujo de Caja''!H2:H57,''Parámetros D2''!B41),"Sin convergencia")'
    $ind.Range('B10').Formula = '=IF(SUM(Ingresos!E2:E58)>0,1-SUM(Costos!K2:K57)/SUM(Ingresos!E2:E58),"Sin venta")'
    Set-Row $summary 3 @('Venta neta de escenario CLP','=''Cuadro maestro''!D19')
    Set-Row $summary 11 @('Financiamiento','Capital y refuerzo son hipótesis de caja. Revisar condiciones, fechas, comisiones y referencias en Financiamiento.')
    Set-Row $summary 14 @('IVA','LTE y ExpressRoute en el escenario de caja. Ver pagador, respaldo y crédito fiscal en Conciliación IVA.')
    Set-Row $summary 18 @('Cuadro maestro','La venta de escenario concilia con Ingresos. La referencia contractual se conserva en RESUMEN.')
    Set-Row $summary 19 @('Ajustes de operación','Registrar variable y descuento en el mes de servicio. M56 se cobra en M57.')
    Set-Row $summary 7 @('Déficit de tesorería por plazo H5 CLP','=Sensibilidad!F5')
    Set-Row $summary 20 @('Caja mínima del estrés CLP','=Sensibilidad!D6')
    Set-Row $summary 21 @('Holgura frente a la meta CLP','=Sensibilidad!C9')
    Set-Row $summary 22 @('Venta contractual neta CLP','=''Cuadro maestro''!D21')
    Set-Row $summary 23 @('Venta de escenario menos contractual','=''Cuadro maestro''!D22')
    Set-Row $summary 24 @('Ajustes de operación por corregir','=COUNTIF(''Ajustes de operación''!E22:E57,"Revisar*")')
    Set-Row $summary 25 @('Caja mínima por orden adverso','=Sensibilidad!B68')
    Set-Row $summary 26 @('Cobro H5 previsto en tesorería','=''Parámetros D2''!B55')
    $summary.Range('B26').NumberFormat = 'dd/mm/yyyy'
    $summary.Range('B20:B25').NumberFormat = '#,##0'
    $summary.Range('A18:A25').ColumnWidth = 42
    $summary.Range('B11:B19').WrapText = $true
    $summary.Range('A11:B19').RowHeight = 30

    $curva = $book.Worksheets.Item('Curva S')
    $curva.Unprotect()
    $curva.Cells.Locked = $true
    $chart = $curva.ChartObjects(1).Chart
    $series = $chart.SeriesCollection()
    for ($i = $series.Count; $i -ge 1; $i--) {
        $line = $series.Item($i)
        if ($line.Formula -match '\$A\$2:\$A\$57,\d+\)$' -or ($series.Count -eq 4 -and $line.Name -eq 'Mes')) { $line.Delete() | Out-Null; continue }
        $line.XValues = $curva.Range('A2:A57')
        $line.Smooth = $false
    }
    if ($chart.SeriesCollection().Count -ne 3) { throw 'La Curva S debe tener tres series.' }
    $curva.Protect()

    foreach ($range in @('C18:D24','F18:F24','D30')) { Nonnegative $benefits $range }
    foreach ($range in @('E18:E24','B30:C30')) { Rate $benefits $range }
    foreach ($range in @('H18:H24','F30')) { TextInput $benefits $range }
    MonthInput $innov 'A13'
    Validation $innov 'B13:C13' 1 7 0 $null
    foreach ($name in @('RESUMEN','PARÁMETROS','COSTOS DE OPERACION','TARIFAS DE OPERACION','FLUJO DE CAJA NETO','FLUJO DE CAJA COMPLETO','PCUESFUERZO','Dedicación D3','Refuerzo presupuestado','INN-5 Costos','Hardware del mandante','PUENTE D2','Ingresos')) {
        $sheet = $book.Worksheets.Item($name)
        $sheet.Unprotect()
        $sheet.Cells.Locked = $true
        $sheet.Protect()
    }
    foreach ($sheet in $protected) { $sheet.Protect() }
    foreach ($name in @('Escenarios de caja','Cotejo D1')) { $book.Worksheets.Item($name).Visible = 0 }
    $excel.Calculation = -4105
    $excel.CalculateFullRebuild()
}
