/* Adaptador reutilizable: navegación oculta sobre el controlador HyperFrames. */
(() => {
  const deck = document.querySelector('hyperframes-slideshow');
  const player = document.querySelector('hyperframes-player');
  if (location.protocol === 'file:') {
    player.iframeElement.srcdoc = JSON.parse(document.getElementById('embedded-composition').textContent);
  } else {
    player.setAttribute('src','composition/index.html');
  }
  let movement;
  let lastTarget = 1;
  const originalSeek = player.seek.bind(player);
  player.seek = (time) => {
    const frame = player.iframeElement;
    const win = frame?.contentWindow;
    const timeline = win?.__hfMasterTimeline;
    const previous = timeline?.time() ?? time;
    movement?.kill();
    originalSeek(time);
    if (!timeline || !win.__hfSetTime) return;
    const reduced = matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (reduced || document.documentElement.dataset.qa === 'true') {
      win.__hfSetTime(time);
    } else {
      const sameScene = Math.floor(lastTarget / 10) === Math.floor(time / 10);
      const from = sameScene ? previous : Math.floor(time / 10) * 10;
      win.__hfSetTime(from);
      movement = win.gsap.to(timeline, {time, duration: sameScene ? 1 : 1.05, ease: 'power2.inOut', onUpdate: () => win.__hfSetTime(timeline.time())});
    }
    lastTarget = time;
    document.body.dataset.target = String(time);
  };
  function next() { deck.controller?.next(); }
  function previous() {
    const c = deck.controller;
    if (!c) return;
    if (c.position.fragmentIndex > 0) {
      c.resumeSlide(c.position.slideIndex, c.position.fragmentIndex - 1);
    } else {
      c.prev();
    }
  }
  const surface = document.getElementById('surface');
  // Salta a una lámina del respaldo (R1, R2…).
  function goBackup(n) {
    const c = deck.controller;
    if (!c) return;
    if (c.position.sequenceId !== 'respaldo') c.enterBranch('respaldo');
    setTimeout(() => c.goToSlide(Math.max(0, Math.min(n - 1, c.show.slides.length - 1))), 30);
  }
  let idleTimer;
  surface.addEventListener('mousemove', () => {
    surface.classList.remove('idle');
    clearTimeout(idleTimer);
    idleTimer = setTimeout(() => surface.classList.add('idle'), 4000);
  });
  surface.addEventListener('click', () => { next(); deck.focus({preventScroll:true}); });
  surface.addEventListener('contextmenu', e => { e.preventDefault(); previous(); });
  // En el respaldo, un número seguido de Enter salta a esa lámina (R1, R2…).
  let typed = '';
  let typedTimer;
  window.addEventListener('keydown', e => {
    if (e.ctrlKey || e.altKey || e.metaKey || /INPUT|TEXTAREA/.test(e.target.tagName)) return;
    const c = deck.controller;
    if (!c) return;
    if (/^[0-9]$/.test(e.key)) {
      typed += e.key;
      clearTimeout(typedTimer);
      typedTimer = setTimeout(() => { typed = ''; }, 2500);
      e.preventDefault(); e.stopImmediatePropagation();
      return;
    }
    if (e.key === 'Enter' && typed) {
      const n = Number(typed);
      typed = '';
      goBackup(n);
      e.preventDefault(); e.stopImmediatePropagation();
      return;
    }
    const actions = {
      ArrowRight: next, ' ':next, Enter:next, PageDown:next,
      ArrowLeft:previous, Backspace:previous, PageUp:previous,
      Home:()=>c.goToSlide(0), End:()=>c.goToSlide(c.show.slides.length-1),
      b:()=>c.enterBranch('respaldo'), B:()=>c.enterBranch('respaldo'),
      Escape:()=>c.backToMain(),
      f:()=>{if(document.fullscreenElement)document.exitFullscreen();else document.documentElement.requestFullscreen().catch(()=>{});},
      F:()=>{if(document.fullscreenElement)document.exitFullscreen();else document.documentElement.requestFullscreen().catch(()=>{});}
    };
    if (actions[e.key]) { e.preventDefault(); e.stopImmediatePropagation(); actions[e.key](); }
  },true);
  deck.focus({preventScroll:true});
  window.auditDeck = {get controller(){return deck.controller;}, get player(){return player;}};
})();

/* Temporizador independiente de la navegación. */
(() => {
  const box = document.createElement('div');
  box.id = 'audit-timer';
  box.style.cssText = 'position:fixed;left:12px;bottom:10px;z-index:2147483647;display:flex;align-items:center;gap:6px;padding:4px 7px;border:1px solid #dce4e7;border-radius:6px;background:rgba(255,255,255,.94);color:#123448;font:600 12px system-ui,sans-serif;font-variant-numeric:tabular-nums;box-shadow:0 1px 4px #0001';
  box.innerHTML = '<span aria-label="Tiempo transcurrido">00:00</span><span style="opacity:.55;font-size:10px">/ 15:00</span><button type="button" title="Iniciar o pausar" aria-label="Iniciar">▶</button><button type="button" title="Reiniciar" aria-label="Reiniciar">↻</button>';
  const [clock] = box.querySelectorAll('span');
  const [toggle, reset] = box.querySelectorAll('button');
  for (const b of [toggle,reset]) b.style.cssText='border:0;background:transparent;color:inherit;cursor:pointer;padding:2px;font:inherit;line-height:1';
  let elapsed=0, started=null;
  const total=900000;
  function paint(){
    const ms=Math.min(total,elapsed+(started===null?0:performance.now()-started));
    const sec=Math.floor(ms/1000);
    clock.textContent=String(Math.floor(sec/60)).padStart(2,'0')+':'+String(sec%60).padStart(2,'0');
    box.style.color=sec>=900?'#a13437':sec>=780?'#a65e00':'#123448';
    if(ms>=total){elapsed=total;started=null;}
    toggle.textContent=started===null?'▶':'Ⅱ';
    toggle.setAttribute('aria-label',started===null?'Iniciar o continuar':'Pausar');
    toggle.disabled=elapsed>=total;
  }
  toggle.addEventListener('click',()=>{if(started===null){if(elapsed<total)started=performance.now();}else{elapsed=Math.min(total,elapsed+performance.now()-started);started=null;}paint();document.querySelector('hyperframes-slideshow')?.focus({preventScroll:true});});
  reset.addEventListener('click',()=>{elapsed=0;started=null;paint();document.querySelector('hyperframes-slideshow')?.focus({preventScroll:true});});
  for(const event of ['click','pointerdown','contextmenu'])box.addEventListener(event,e=>e.stopPropagation());
  document.body.appendChild(box);paint();setInterval(paint,200);
})();
