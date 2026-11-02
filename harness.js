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
    // Al retroceder se salta directo al estado final, sin reproducir la animación.
    const backward = time < lastTarget;
    if (reduced || backward || document.documentElement.dataset.qa === 'true') {
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
    } else if (c.position.slideIndex > 0) {
      // Vuelve a la lámina anterior ya con todas sus revelaciones hechas.
      const idx = c.position.slideIndex - 1;
      const anterior = c.slidesOf(c.position.sequenceId)[idx];
      c.resumeSlide(idx, Math.max(0, (anterior?.fragments.length ?? 1) - 1));
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
