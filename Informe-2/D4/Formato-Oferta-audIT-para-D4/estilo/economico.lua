-- ===========================================================================
--  economico.lua
--  Cálculo de montos de los documentos económicos. Lo usa economico.sty.
--
--  Regla de cálculo, una sola para todos los documentos:
--    - Todo monto se lleva a pesos chilenos enteros (CLP), con el tipo de
--      cambio de configuracion/economico.tex (Formulario E-24).
--    - UF y USD se obtienen de ese valor en CLP y se redondean a dos
--      decimales, la mitad hacia arriba. Se calcula con enteros, sin coma
--      flotante, para que el mismo dato dé siempre la misma cifra.
--    - El IVA se calcula sobre el neto en CLP y se redondea al peso. Las
--      sumas se hacen en CLP. Cada suma se convierte después a UF y USD.
--
--  Cada cifra impresa queda anotada en el .aux (\audit@cifraeco) para el
--  verificador. Cada monto y cada tabla generada quedan además, en texto
--  plano, en <documento>.eco.json junto al .aux: de ahí salen el Markdown y
--  el DOCX, que así no vuelven a calcular nada.
-- ===========================================================================
audit_eco = audit_eco or {}
local E = audit_eco

E.tc = {}            -- código -> pesos por unidad (entero)
E.orden_tc = {}      -- códigos en el orden de la configuración
E.nombres = {}       -- código -> nombre
E.iva = 19           -- porcentaje
E.fecha_tc = ""      -- fecha de referencia del tipo de cambio (\FechaTipoCambio)
E.parametros = {}    -- otros parámetros del E-24
E.partidas = {}      -- clave -> registro
E.orden = {}
E.cargado = {}
E.hitos = {}
E.rangos, E.orden_rangos, E.tarifas = {}, {}, {}
-- lo que se exporta para el Markdown
E.exp = { cifras = {}, tablas = {}, pendientes = {} }

local function err(msg)
  tex.error("Documento económico: " .. msg)
end

-- Todo lo que Lua devuelve a TeX se lee con @ como letra (\protected@write,
-- \@auxout). Con las categorías del documento, \protected@write se leería
-- como el prefijo \protected seguido de «@write».
local cct = luatexbase.registernumber("catcodetable@atletter")
local function sp(s)
  tex.sprint(cct, s)
end

-- --------------------------------------------------------------------------
--  Números
-- --------------------------------------------------------------------------
-- Lee "1234", "1,25" o "1.25" como fracción (numerador, 10^decimales).
-- No acepta separadores de miles: «1.234» sería ambiguo.
function E.leer_numero(s)
  s = (s or ""):gsub("%s", "")
  if s == "" then return nil end
  local neg = false
  if s:sub(1, 1) == "-" then neg = true; s = s:sub(2) end
  local ent, dec = s:match("^(%d+)[,.](%d+)$")
  if not ent then ent = s:match("^(%d+)$"); dec = "" end
  if not ent then
    return nil, "«" .. s .. "» no es un número (sin separador de miles, decimales con coma o punto)"
  end
  local den = math.tointeger(10 ^ #dec)
  local num = math.tointeger(tonumber(ent .. dec))
  if neg then num = -num end
  return num, den
end

-- a / b redondeado a entero, la mitad hacia arriba (en valor absoluto)
local function div_red(a, b)
  if b < 0 then a, b = -a, -b end
  if a >= 0 then return (2 * a + b) // (2 * b) end
  return -((2 * (-a) + b) // (2 * b))
end
E.div_red = div_red

-- valor en `moneda` (fracción num/den) -> pesos enteros
function E.a_clp(num, den, moneda)
  local tc = (moneda == "CLP") and 1 or E.tc[moneda]
  if not tc then err("moneda desconocida «" .. tostring(moneda) .. "»"); return 0 end
  return div_red(num * tc, den)
end

-- pesos -> centésimos de la moneda
function E.centesimos(clp, moneda)
  return div_red(clp * 100, E.tc[moneda])
end

-- Formato chileno: miles con punto, decimales con coma
local function miles(n)
  local r = tostring(n):reverse():gsub("(%d%d%d)", "%1."):reverse()
  return (r:gsub("^%.", ""))
end
function E.fmt_entero(n)
  if n < 0 then return "-" .. miles(-n) end
  return miles(n)
end
function E.fmt_cent(c)
  local neg = c < 0
  if neg then c = -c end
  return (neg and "-" or "") .. miles(c // 100) .. "," .. string.format("%02d", c % 100)
end
function E.fmt_decimal(s)
  return (tostring(s):gsub("%.", ","))
end

-- Las tres cifras de un monto en pesos
function E.tres(clp)
  return {
    CLP = "CLP " .. E.fmt_entero(clp),
    UF  = "UF " .. E.fmt_cent(E.centesimos(clp, "UF")),
    USD = "USD " .. E.fmt_cent(E.centesimos(clp, "USD")),
  }
end
local function solo_numero(t) return (t:gsub("^%a+ ", "")) end

-- --------------------------------------------------------------------------
--  Salida a TeX, registro en el .aux y exportación
-- --------------------------------------------------------------------------
local function tex_escape(s)
  return (s:gsub("([%%&#_%$])", "\\%1"))
end
E.tex_escape = tex_escape

-- Cifra impresa: queda en el .aux para el verificador. Se escribe al
-- despachar la página, como una etiqueta.
local function anotar(clave, tres, pesos)
  sp(string.format("\\protected@write\\@auxout{}{\\string\\audit@cifraeco{%s}{%s}{%s}{%s}{%s}}",
    clave, tres.CLP or "", tres.UF or "", tres.USD or "", pesos or ""))
end
local function anotar_iva(clave, neto, iva, total, afecto)
  sp(string.format("\\protected@write\\@auxout{}{\\string\\audit@ivaeco{%s}{%d}{%d}{%d}{%s}}",
    clave, neto, iva, total, afecto))
end

-- Texto de un monto: CLP · UF · USD, sin cortes dentro de cada cifra
local function nb(x) return (x:gsub(" ", "~")) end
local function texto_tres(tres)
  return nb(tres.CLP) .. "\\enspace\\textperiodcentered\\enspace " .. nb(tres.UF)
    .. "\\enspace\\textperiodcentered\\enspace " .. nb(tres.USD)
end
local function plano_tres(tres)
  return tres.CLP .. " · " .. tres.UF .. " · " .. tres.USD
end

local function por_completar(texto)
  return "\\marcador{" .. tex_escape(texto) .. "}"
end

-- Tabla en construcción: cada fila va a TeX (\AgregarFila) y, en texto
-- plano, a la exportación
local actual = nil
function E.empezar_tabla(etiqueta)
  actual = { etiqueta = etiqueta, filas = {} }
end
function E.terminar_tabla(cabecera)
  if actual then
    actual.cabecera = {}
    for c in (cabecera .. "|"):gmatch("([^|]*)|") do actual.cabecera[#actual.cabecera + 1] = c end
    E.exp.tablas[actual.etiqueta] = actual
  end
  actual = nil
end
-- modo "pegada": la fila no se separa de la anterior en un salto de página
-- (las filas UF y USD de una partida van con su fila CLP). modo "filete":
-- la fila abre una partida y lleva el filete fino que la separa de la
-- anterior. Las tablas de montos ponen sus propios filetes: el que el
-- constructor pone entre todas las filas es un punto de corte de página.
local function fila(tex_celdas, md_celdas, modo)
  local pre = (modo == "pegada" and "\\nopagebreak ") or (modo == "filete" and "\\audit@filetefila ") or ""
  sp("\\AgregarFila{" .. pre .. table.concat(tex_celdas, " & ") .. " \\\\}")
  if actual then actual.filas[#actual.filas + 1] = md_celdas or tex_celdas end
end

-- Exportación para el Markdown y el DOCX, al final de la compilación
local function json(v)
  local t = type(v)
  if t == "string" then
    return '"' .. v:gsub('[%c"\\]', function(c)
      return string.format("\\u%04x", c:byte())
    end) .. '"'
  elseif t == "number" then
    return tostring(v)
  elseif t == "table" then
    if #v > 0 or next(v) == nil then
      local r = {}
      for _, x in ipairs(v) do r[#r + 1] = json(x) end
      return "[" .. table.concat(r, ",") .. "]"
    end
    local r, claves = {}, {}
    for k in pairs(v) do claves[#claves + 1] = k end
    table.sort(claves)
    for _, k in ipairs(claves) do r[#r + 1] = json(k) .. ":" .. json(v[k]) end
    return "{" .. table.concat(r, ",") .. "}"
  end
  return "null"
end
function E.guardar()
  local dir = os.getenv("TEXMF_OUTPUT_DIRECTORY") or status.output_directory
  local ruta = ((dir and dir ~= "") and (dir .. "/") or "") .. tex.jobname .. ".eco.json"
  local f = io.open(ruta, "w")
  if not f then return end
  f:write(json(E.exp), "\n")
  f:close()
end

-- --------------------------------------------------------------------------
--  Configuración
-- --------------------------------------------------------------------------
function E.tipo_cambio(codigo, nombre, pesos)
  if not E.tc[codigo] then E.orden_tc[#E.orden_tc + 1] = codigo end
  E.tc[codigo] = math.tointeger(tonumber(pesos))
  E.nombres[codigo] = nombre
end
function E.parametro(indicador, valor)
  E.parametros[#E.parametros + 1] = { indicador = indicador, valor = (valor:gsub("\\%%", "%%")) }
end
function E.parametro_monto(indicador, pesos)
  E.parametros[#E.parametros + 1] = { indicador = indicador, pesos = math.tointeger(tonumber(pesos)) }
end
function E.hito(h, etapa, mes, pct, desc)
  E.hitos[#E.hitos + 1] = { h = h, etapa = tonumber(etapa), mes = mes, pct = tonumber(pct), desc = desc }
end
function E.rango(perfil, cmin, cmax, tmin, tmax)
  E.rangos[perfil] = { tonumber(cmin), tonumber(cmax), tonumber(tmin), tonumber(tmax), cmin, cmax, tmin, tmax }
  E.orden_rangos[#E.orden_rangos + 1] = perfil
end

-- --------------------------------------------------------------------------
--  Montos sueltos
-- --------------------------------------------------------------------------
-- \monto[moneda]{valor}
function E.monto(moneda, valor)
  local num, den = E.leer_numero(valor)
  if not num then err(den or "falta el valor del monto"); return end
  local clave = "monto " .. moneda .. " " .. valor
  local clp = E.a_clp(num, den, moneda)
  local tres = E.tres(clp)
  anotar(clave, tres, tostring(clp))
  E.exp.cifras[clave] = plano_tres(tres)
  sp(texto_tres(tres))
end

-- --------------------------------------------------------------------------
--  Partidas: economico/datos/partidas.csv
--  clave;concepto;moneda;valor;iva;planilla
-- --------------------------------------------------------------------------
local function partir(linea)
  local campos = {}
  for c in (linea .. ";"):gmatch("([^;]*);") do
    campos[#campos + 1] = (c:gsub("^%s+", ""):gsub("%s+$", ""))
  end
  return campos
end

-- Se pueden cargar varios archivos: la muestra antepone el suyo. Si una
-- clave ya existe, gana el archivo cargado primero.
function E.cargar(ruta)
  if E.cargado[ruta] then return end
  E.cargado[ruta] = true
  local f = io.open(ruta, "r")
  if not f then return end
  local n, propias = 0, {}
  for linea in f:lines() do
    n = n + 1
    linea = linea:gsub("\r$", "")
    if n > 1 and linea:match("%S") and not linea:match("^%s*#") then
      local c = partir(linea)
      local clave = c[1]
      if propias[clave] then err("partida repetida «" .. clave .. "» en " .. ruta) end
      propias[clave] = true
      if not E.partidas[clave] then
        local p = { clave = clave, concepto = c[2] or "", moneda = (c[3] and c[3] ~= "" and c[3]) or "CLP",
                    valor = c[4] or "", iva = (c[5] or "si"):lower() ~= "no",
                    planilla = c[6] or "" }
        if p.valor:sub(1, 1) == "=" then
          p.suma = {}
          for k in p.valor:sub(2):gmatch("[^+%s]+") do p.suma[#p.suma + 1] = k end
        elseif p.valor ~= "" then
          local num, den = E.leer_numero(p.valor)
          if not num then err("partida «" .. clave .. "»: " .. den) else p.num, p.den = num, den end
        end
        E.partidas[clave] = p
        E.orden[#E.orden + 1] = clave
      end
    end
  end
  f:close()
end

-- Valor neto en pesos de una partida, o nil si está por completar
function E.neto(clave, pila)
  local p = E.partidas[clave]
  if not p then err("no existe la partida «" .. clave .. "» en partidas.csv"); return nil end
  pila = pila or {}
  if pila[clave] then err("la suma de «" .. clave .. "» se incluye a sí misma"); return nil end
  if p.suma then
    pila[clave] = true
    local total = 0
    for _, k in ipairs(p.suma) do
      local v = E.neto(k, pila)
      if v == nil then pila[clave] = nil; return nil end
      total = total + v
    end
    pila[clave] = nil
    return total
  end
  if not p.num then return nil end
  return E.a_clp(p.num, p.den, p.moneda)
end

function E.iva_de(clp)
  return div_red(clp * E.iva, 100)
end

-- \montoPartida{clave}
function E.monto_partida(clave)
  local p = E.partidas[clave]
  if not p then err("no existe la partida «" .. clave .. "» en partidas.csv"); return end
  local v = E.neto(clave)
  if v == nil then
    E.exp.pendientes["partida " .. clave] = p.concepto
    sp(por_completar("monto por completar: " .. p.concepto))
    return
  end
  local tres = E.tres(v)
  anotar("partida " .. clave, tres, tostring(v))
  E.exp.cifras["partida " .. clave] = plano_tres(tres)
  sp(texto_tres(tres))
end

-- --------------------------------------------------------------------------
--  Tablas
-- --------------------------------------------------------------------------
local MONEDAS = { "CLP", "UF", "USD" }

-- Neto, IVA y total de cada partida en las tres monedas y total general
-- (Artículo 51.2). con_total = false omite el total general.
function E.filas_montos(etiqueta, lista, con_total)
  E.empezar_tabla(etiqueta)
  local claves = {}
  for k in lista:gmatch("[^,%s]+") do claves[#claves + 1] = k end
  local sneto, siva, completas, n = 0, 0, true, 0
  for _, clave in ipairs(claves) do
    local p = E.partidas[clave]
    if not p then err("no existe la partida «" .. clave .. "» en partidas.csv"); return end
    n = n + 1
    local v = E.neto(clave)
    local concepto = tex_escape(p.concepto)
    local abre = n > 1 and "filete" or nil
    if v == nil then
      completas = false
      fila({ tostring(n), concepto, "CLP", por_completar("por completar"), "", "" },
           { tostring(n), p.concepto, "CLP", "[por completar]", "", "" }, abre)
      fila({ "", "", "UF", "", "", "" }, nil, "pegada")
      fila({ "", "", "USD", "", "", "" }, nil, "pegada")
    else
      local iva = p.iva and E.iva_de(v) or 0
      local tot = v + iva
      sneto, siva = sneto + v, siva + iva
      local a, b, c = E.tres(v), E.tres(iva), E.tres(tot)
      anotar("neto " .. clave, a, tostring(v))
      if p.iva then anotar("iva " .. clave, b, tostring(iva)) end
      anotar("total " .. clave, c, tostring(tot))
      anotar_iva(clave, v, iva, tot, p.iva and "si" or "no")
      for i, m in ipairs(MONEDAS) do
        local celdas = { i == 1 and tostring(n) or "", i == 1 and concepto or "", m,
          solo_numero(a[m]), p.iva and solo_numero(b[m]) or (i == 1 and "no aplica" or ""),
          solo_numero(c[m]) }
        local md = { celdas[1], i == 1 and p.concepto or "", m, celdas[4], celdas[5], celdas[6] }
        fila(celdas, md, i > 1 and "pegada" or abre)
      end
    end
  end
  if con_total then
    if completas and n > 0 then
      local stot = sneto + siva
      local a, b, c = E.tres(sneto), E.tres(siva), E.tres(stot)
      anotar("neto total general " .. etiqueta, a, tostring(sneto))
      anotar("iva total general " .. etiqueta, b, tostring(siva))
      anotar("total total general " .. etiqueta, c, tostring(stot))
      anotar_iva("total general " .. etiqueta, sneto, siva, stot, "suma")
      for i, m in ipairs(MONEDAS) do
        fila({ "", i == 1 and "\\textbf{Total general}" or "", m, "\\textbf{" .. solo_numero(a[m]) .. "}",
               "\\textbf{" .. solo_numero(b[m]) .. "}", "\\textbf{" .. solo_numero(c[m]) .. "}" },
             { "", i == 1 and "**Total general**" or "", m, "**" .. solo_numero(a[m]) .. "**",
               "**" .. solo_numero(b[m]) .. "**", "**" .. solo_numero(c[m]) .. "**" },
             i > 1 and "pegada" or "filete")
      end
    else
      fila({ "", "\\textbf{Total general}", "CLP", por_completar("por completar"), "", "" },
           { "", "**Total general**", "CLP", "[por completar]", "", "" }, "filete")
    end
  end
end

-- Hitos de pago del E-25 sobre el valor de la implementación
function E.filas_hitos(clave)
  E.empezar_tabla("hitos-e25")
  local suma = 0
  for _, x in ipairs(E.hitos) do suma = suma + x.pct end
  if suma ~= 100 then err("los hitos del Formulario E-25 suman " .. suma .. " %, no 100 %") end
  if not E.partidas[clave] then err("no existe la partida «" .. clave .. "» en partidas.csv"); return end
  local base = E.neto(clave)
  local etapa, sub = nil, 0
  local function montos(pct, negrita)
    if not base then return { "", "", "" }, { "", "", "" } end
    local clp = div_red(base * pct, 100)
    local t = E.tres(clp)
    local tx, md = {}, {}
    for _, m in ipairs(MONEDAS) do
      tx[#tx + 1] = negrita and ("\\textbf{" .. solo_numero(t[m]) .. "}") or solo_numero(t[m])
      md[#md + 1] = negrita and ("**" .. solo_numero(t[m]) .. "**") or solo_numero(t[m])
    end
    return tx, md, t, clp
  end
  local function subtotal(e, pct)
    local tx, md, t, clp = montos(pct, true)
    if t then anotar("subtotal etapa " .. e, t, tostring(clp)) end
    fila({ "", "\\textbf{Subtotal Etapa " .. e .. "}", "", "\\textbf{" .. pct .. "~\\%}", tx[1], tx[2], tx[3] },
         { "", "**Subtotal Etapa " .. e .. "**", "", "**" .. pct .. " %**", md[1], md[2], md[3] })
  end
  for i, x in ipairs(E.hitos) do
    if etapa and x.etapa ~= etapa then subtotal(etapa, sub); sub = 0 end
    etapa = x.etapa
    sub = sub + x.pct
    local tx, md, t, clp = montos(x.pct, false)
    if t then anotar("hito " .. x.h, t, tostring(clp)) end
    if not base and i == 1 then
      tx[1] = por_completar("con el valor de la implementación")
      md[1] = "[con el valor de la implementación]"
    end
    fila({ x.h, tex_escape(x.desc), x.mes, x.pct .. "~\\%", tx[1], tx[2], tx[3] },
         { x.h, x.desc, x.mes, x.pct .. " %", md[1], md[2], md[3] })
  end
  if etapa then subtotal(etapa, sub) end
end

-- Tipos de cambio y parámetros del E-24
function E.filas_parametros()
  E.empezar_tabla("parametros-e24")
  for _, codigo in ipairs(E.orden_tc) do
    local clp = "CLP " .. E.fmt_entero(E.tc[codigo])
    anotar("tipo de cambio " .. codigo, { CLP = clp }, tostring(E.tc[codigo]))
    fila({ tex_escape(E.nombres[codigo]) .. " (" .. codigo .. ")", "1~" .. codigo .. " = " .. nb(clp) },
         { E.nombres[codigo] .. " (" .. codigo .. ")", "1 " .. codigo .. " = " .. clp })
  end
  fila({ "Impuesto al Valor Agregado", E.iva .. "~\\%" }, { "Impuesto al Valor Agregado", E.iva .. " %" })
  for _, p in ipairs(E.parametros) do
    if p.pesos then
      local t = E.tres(p.pesos)
      anotar("parametro " .. p.indicador, t, tostring(p.pesos))
      fila({ tex_escape(p.indicador), texto_tres(t) }, { p.indicador, plano_tres(t) })
    else
      fila({ tex_escape(p.indicador), tex_escape(p.valor) }, { p.indicador, p.valor })
    end
  end
  if E.fecha_tc ~= "" then
    fila({ "Fecha de referencia del tipo de cambio", tex_escape(E.fecha_tc) },
         { "Fecha de referencia del tipo de cambio", E.fecha_tc })
  else
    fila({ "Fecha de referencia del tipo de cambio", por_completar("fecha de referencia, Formulario E-21, 1.1") },
         { "Fecha de referencia del tipo de cambio", "[fecha de referencia, Formulario E-21, 1.1]" })
  end
end

-- Rangos del E-26 y tarifas ofertadas (economico/datos/tarifas.csv:
-- perfil;costo;tarifa, en UF por hora)
function E.cargar_tarifas(ruta)
  if E.cargado[ruta] then return end
  E.cargado[ruta] = true
  local f = io.open(ruta, "r")
  if not f then return end
  local n = 0
  for linea in f:lines() do
    n = n + 1
    linea = linea:gsub("\r$", "")
    if n > 1 and linea:match("%S") and not linea:match("^%s*#") then
      local c = partir(linea)
      if not E.tarifas[c[1]] then E.tarifas[c[1]] = { costo = c[2] or "", tarifa = c[3] or "" } end
    end
  end
  f:close()
end

local function valor_uf(s)
  local num, den = E.leer_numero(s)
  if not num then return nil end
  return num / den
end

function E.filas_tarifas()
  E.empezar_tabla("tarifas-e26")
  for _, perfil in ipairs(E.orden_rangos) do
    local r = E.rangos[perfil]
    local t = E.tarifas[perfil] or { costo = "", tarifa = "" }
    local rc = "UF " .. E.fmt_decimal(r[5]) .. " a " .. E.fmt_decimal(r[6])
    local rt = "UF " .. E.fmt_decimal(r[7]) .. " a " .. E.fmt_decimal(r[8])
    anotar("rango costo " .. perfil, { UF = "UF " .. E.fmt_decimal(r[5]) }, "")
    anotar("rango tarifa " .. perfil, { UF = "UF " .. E.fmt_decimal(r[7]) }, "")
    local tx = { tex_escape(perfil), nb(rc), "", nb(rt), "" }
    local md = { perfil, rc, "", rt, "" }
    for i, campo in ipairs({ "costo", "tarifa" }) do
      local v = valor_uf(t[campo])
      local col = i == 1 and 3 or 5
      if v then
        local lo, hi = r[i == 1 and 1 or 3], r[i == 1 and 2 or 4]
        if v < lo - 1e-9 or v > hi + 1e-9 then
          err(campo .. " de «" .. perfil .. "», UF " .. t[campo] .. ", fuera del rango del Formulario E-26")
        end
        local cifra = "UF " .. E.fmt_decimal((t[campo]:gsub("%s", "")))
        anotar(campo .. " " .. perfil, { UF = cifra }, "")
        tx[col], md[col] = nb(cifra), cifra
      else
        tx[col], md[col] = por_completar("por completar"), "[por completar]"
      end
    end
    fila(tx, md)
  end
  for perfil, _ in pairs(E.tarifas) do
    if not E.rangos[perfil] then
      sp("\\PackageWarning{economico}{El perfil «" .. tex_escape(perfil) .. "» no está en el "
        .. "Formulario E-26. Declararlo en la hoja de tarifas del modelo financiero con un rango coherente}")
    end
  end
end

return E
