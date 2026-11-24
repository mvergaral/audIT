"""Genera un teleprompter HTML autónomo con el texto hablado de GUION.md."""
import html
import json
import re
import sys

md_path, out_path = sys.argv[1:3]
md = open(md_path, encoding="utf-8").read()

def inline(t):
    t = html.escape(t, quote=False)
    return re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)

def bloques(cuerpo):
    """Convierte las líneas '> ...' en párrafos y listas."""
    partes, lista = [], []
    for linea in cuerpo.splitlines():
        if not linea.startswith(">"):
            continue
        t = linea[1:].strip()
        if t.startswith("- "):
            lista.append(f"<li>{inline(t[2:])}</li>")
            continue
        if lista:
            partes.append("<ul>" + "".join(lista) + "</ul>")
            lista = []
        if t:
            partes.append(f"<p>{inline(t)}</p>")
    if lista:
        partes.append("<ul>" + "".join(lista) + "</ul>")
    return "".join(partes)

secciones = re.split(r"^## ", md, flags=re.M)[1:]
completa, corta = [], []
for s in secciones:
    titulo, _, cuerpo = s.partition("\n")
    m = re.match(r"Diapositiva (\d) · (.+?) \((.+?)\)", titulo)
    if m:
        completa.append({"n": m.group(1), "tema": m.group(2), "t": m.group(3), "html": bloques(cuerpo)})
    elif titulo.startswith("Versión corta"):
        # La versión corta usa las diapositivas 2 y 3
        ps = re.findall(r"^> (.+)$", cuerpo, flags=re.M)
        corta = [{"n": "2", "tema": "Resultado", "t": "", "html": f"<p>{inline(ps[0])}</p>"},
                 {"n": "3", "tema": "Curva S", "t": "", "html": "".join(f"<p>{inline(p)}</p>" for p in ps[1:])}]

datos = json.dumps({"completa": completa, "corta": corta}, ensure_ascii=False)

pagina = r"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover" />
<title>Teleprompter · Curva S y resultado</title>
<style>
  @font-face { font-family: AuditSans; font-weight: 100 500; src: url('assets/fonts/AuditSans-Regular.woff2'); }
  @font-face { font-family: AuditSans; font-weight: 600 900; src: url('assets/fonts/AuditSans-Bold.woff2'); }
  :root { --fondo:#0b1720; --texto:#f2f6f8; --tenue:#8fa6b3; --acento:#5fc3d3; --ambar:#f2b75b; --tam:56px; --ancho:1100px; }
  * { box-sizing: border-box; margin: 0; padding: 0; }
  html, body { height: 100%; background: var(--fondo); color: var(--texto);
    font-family: AuditSans, "Liberation Sans", system-ui, sans-serif; overflow: hidden; }
  #scroll { position: fixed; inset: 0; overflow-y: scroll; scrollbar-width: none; }
  #scroll::-webkit-scrollbar { display: none; }
  #texto { max-width: var(--ancho); margin: 0 auto; padding: 45vh 48px 80vh; font-size: var(--tam); line-height: 1.45; }
  body.espejo #texto { transform: scaleX(-1); }
  #texto p { margin-bottom: 0.8em; }
  #texto ul { margin: 0 0 0.8em 1.1em; }
  #texto li { margin-bottom: 0.5em; }
  #texto strong { color: var(--acento); }
  .marca { display: flex; align-items: baseline; gap: 0.5em; margin: 1.2em 0 0.7em; padding-top: 0.6em;
    border-top: 3px solid #23404f; font-size: 0.5em; font-weight: 800; letter-spacing: .08em;
    text-transform: uppercase; color: var(--ambar); }
  .marca .n { font-size: 1.6em; }
  .marca .t { margin-left: auto; color: var(--tenue); letter-spacing: 0; }
  .fin { text-align: center; color: var(--tenue); font-size: 0.6em; margin-top: 2em; }
  /* Línea de lectura */
  #guia { position: fixed; left: 0; right: 0; top: 33vh; height: 0; pointer-events: none;
    border-top: 2px solid rgba(242,183,91,.55); }
  #guia::before, #guia::after { content: "▶"; position: absolute; top: -0.72em; font-size: 28px; color: var(--ambar); }
  #guia::before { left: 10px; } #guia::after { right: 10px; transform: scaleX(-1); }
  .velo { position: fixed; left: 0; right: 0; pointer-events: none; }
  #velo-sup { top: 0; height: 22vh; background: linear-gradient(var(--fondo), transparent); }
  #velo-inf { bottom: 0; height: 30vh; background: linear-gradient(transparent, var(--fondo)); }
  /* Barra de estado */
  #hud { position: fixed; left: 0; right: 0; bottom: 0; display: flex; flex-wrap: wrap; gap: 8px 22px; align-items: center;
    padding: 10px 18px; background: rgba(5,12,17,.88); color: var(--tenue); font-size: 17px; transition: opacity .3s; }
  #hud b { color: var(--texto); }
  #hud.oculto { opacity: 0; }
  #hud .estado { color: var(--ambar); font-weight: 800; }
  #hud button { font: inherit; color: var(--texto); background: #18303d; border: 1px solid #2c4a5a; border-radius: 8px;
    padding: 6px 12px; cursor: pointer; }
  #hud .ayuda { margin-left: auto; font-size: 14px; }
  #tiempo.pasado { color: #ff8f8f; }
  @media (max-width: 700px) { #texto { padding-left: 20px; padding-right: 20px; } #hud .ayuda { display: none; } }
</style>
</head>
<body>
<div id="scroll"><div id="texto"></div></div>
<div class="velo" id="velo-sup"></div><div class="velo" id="velo-inf"></div>
<div id="guia"></div>
<div id="hud">
  <span class="estado" id="estado">EN PAUSA</span>
  <span>Diapositiva <b id="dia">1</b></span>
  <span>Tiempo <b id="tiempo">0:00</b> / <span id="meta">10:00</span></span>
  <span>Velocidad <b id="vel">3</b></span>
  <button id="b-play">▶︎ / ❚❚</button>
  <button id="b-menos">− vel</button><button id="b-mas">+ vel</button>
  <button id="b-ant">◀ dia</button><button id="b-sig">dia ▶</button>
  <button id="b-modo">Versión corta</button>
  <span class="ayuda">Espacio: iniciar · ↑↓ velocidad · ←→ diapositiva · + − letra · M espejo · C versión · R inicio · F pantalla completa</span>
</div>
<script>
const DATOS = __DATOS__;
const $ = (id) => document.getElementById(id);
const scroller = $('scroll'), texto = $('texto');
// Preferencias del lector (solo en este navegador)
const pref = (() => { try { return JSON.parse(localStorage.getItem('prompter') || '{}'); } catch (e) { return {}; } })();
const guardar = () => { try { localStorage.setItem('prompter', JSON.stringify(pref)); } catch (e) {} };
let vel = pref.vel || 3, tam = pref.tam || 56, modo = 'completa';
let corriendo = false, ultimo = null, transcurrido = 0, resto = 0, temporizador = null;

function render() {
  const secs = DATOS[modo];
  texto.innerHTML = secs.map((s) =>
    `<section data-n="${s.n}"><div class="marca"><span class="n">${s.n}</span><span>${s.tema}</span>` +
    `<span class="t">${s.t}</span></div>${s.html}</section>`).join('') +
    '<div class="fin">— Fin · Quedamos atentos a sus preguntas —</div>';
  $('meta').textContent = modo === 'completa' ? '10:00' : '2:00';
  $('b-modo').textContent = modo === 'completa' ? 'Versión corta' : 'Versión completa';
  scroller.scrollTop = 0; transcurrido = 0; pintarTiempo(); actualizarDia();
}
function aplicar() {
  document.documentElement.style.setProperty('--tam', tam + 'px');
  $('vel').textContent = vel; pref.vel = vel; pref.tam = tam; guardar();
}
// Velocidad 1–10. Con letra de 56 px en pantalla de 1920, la velocidad 3 lee el guion completo en ~10 min.
const pxs = () => (8 + vel * 6.5) * tam / 56;
function paso(t) {
  if (!corriendo) return;
  if (ultimo !== null) {
    resto += pxs() * (t - ultimo) / 1000;
    const entero = Math.floor(resto);
    if (entero) { scroller.scrollTop += entero; resto -= entero; }
  }
  ultimo = t;
  requestAnimationFrame(paso);
}
function alternar() {
  corriendo = !corriendo; ultimo = null;
  $('estado').textContent = corriendo ? 'LEYENDO' : 'EN PAUSA';
  if (corriendo) {
    requestAnimationFrame(paso);
    temporizador = setInterval(() => { transcurrido++; pintarTiempo(); }, 1000);
  } else clearInterval(temporizador);
}
function pintarTiempo() {
  const m = Math.floor(transcurrido / 60), s = String(transcurrido % 60).padStart(2, '0');
  $('tiempo').textContent = `${m}:${s}`;
  $('tiempo').classList.toggle('pasado', transcurrido > (modo === 'completa' ? 600 : 120));
}
const secciones = () => Array.from(texto.querySelectorAll('section'));
const lineaLectura = () => scroller.scrollTop + innerHeight * 0.33;
function actualizarDia() {
  let actual = secciones()[0];
  for (const s of secciones()) if (s.offsetTop <= lineaLectura() + 4) actual = s;
  if (actual) $('dia').textContent = actual.dataset.n;
}
function irA(sec) { if (sec) scroller.scrollTop = sec.offsetTop - innerHeight * 0.33 + 2; }
function saltar(delta) {
  const ss = secciones(), y = lineaLectura();
  let i = ss.findIndex((s) => s.offsetTop > y + 4) - 1;
  if (i < -1) i = ss.length - 1;
  irA(ss[Math.max(0, Math.min(ss.length - 1, i + delta))]);
}
scroller.addEventListener('scroll', actualizarDia);
addEventListener('keydown', (e) => {
  const k = e.key;
  if (k === ' ') { e.preventDefault(); alternar(); }
  else if (k === 'ArrowUp') { e.preventDefault(); vel = Math.min(10, vel + 1); aplicar(); }
  else if (k === 'ArrowDown') { e.preventDefault(); vel = Math.max(1, vel - 1); aplicar(); }
  else if (k === 'ArrowRight' || k === 'PageDown') { e.preventDefault(); saltar(1); }
  else if (k === 'ArrowLeft' || k === 'PageUp') { e.preventDefault(); saltar(-1); }
  else if (k === '+' || k === '=') { tam = Math.min(110, tam + 4); aplicar(); }
  else if (k === '-') { tam = Math.max(28, tam - 4); aplicar(); }
  else if (k === 'm' || k === 'M') document.body.classList.toggle('espejo');
  else if (k === 'c' || k === 'C') { modo = modo === 'completa' ? 'corta' : 'completa'; render(); }
  else if (k === 'r' || k === 'R') { scroller.scrollTop = 0; transcurrido = 0; pintarTiempo(); }
  else if (k === 'h' || k === 'H') $('hud').classList.toggle('oculto');
  else if (k === 'f' || k === 'F') {
    if (!document.fullscreenElement) document.documentElement.requestFullscreen().catch(() => {});
    else document.exitFullscreen();
  } else if (/^[1-5]$/.test(k)) irA(secciones().find((s) => s.dataset.n === k));
});
$('b-play').onclick = alternar;
$('b-mas').onclick = () => { vel = Math.min(10, vel + 1); aplicar(); };
$('b-menos').onclick = () => { vel = Math.max(1, vel - 1); aplicar(); };
$('b-ant').onclick = () => saltar(-1);
$('b-sig').onclick = () => saltar(1);
$('b-modo').onclick = () => { modo = modo === 'completa' ? 'corta' : 'completa'; render(); };
// Tocar el texto en celular o tablet pausa y reanuda
scroller.addEventListener('click', alternar);
// Evita que Espacio vuelva a activar el último botón pulsado
document.querySelectorAll('#hud button').forEach((b) => b.addEventListener('click', () => b.blur()));
aplicar(); render();
</script>
</body>
</html>
"""
open(out_path, "w", encoding="utf-8").write(pagina.replace("__DATOS__", datos))
print("ok", len(completa), "secciones,", len(corta), "en versión corta")
