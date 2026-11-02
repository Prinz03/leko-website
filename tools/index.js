(function () {
  'use strict';

  // ── Hero (sticky über 400vh): Headline tritt zurück → Handy fliegt ein (30–60 %) → 5 App-Screens wechseln (60–100 %) ──
  var hero = document.querySelector('.hero-outer');
  if (!hero) return;
  var text = hero.querySelector('.hero-text'), phone = hero.querySelector('.phone-frame'), pfeil = hero.querySelector('.scroll-pfeil');
  var screens = hero.querySelectorAll('.app-screen'), punkte = hero.querySelectorAll('.phone-punkte i');
  function bis(p, start, ende) { return Math.max(0, Math.min(1, (p - start) / (ende - start))); }
  var geplant = false, aktiv = -1;
  function inszenieren() {
    geplant = false;
    var weg = hero.offsetHeight - window.innerHeight;
    var prog = Math.max(0, Math.min(1, -hero.getBoundingClientRect().top / (weg || 1)));
    hero.style.setProperty('--p', prog.toFixed(3));
    if (pfeil) pfeil.style.opacity = 1 - bis(prog, 0, 0.08);
    var aus = bis(prog, 0.18, 0.32);
    if (text) {
      text.style.opacity = 1 - aus;
      text.style.transform = 'translateY(' + (-40 * aus).toFixed(1) + 'px)';
      text.style.pointerEvents = aus > 0.5 ? 'none' : '';
    }
    var ein = bis(prog, 0.3, 0.6);
    if (phone) {
      phone.style.opacity = ein;
      phone.style.transform = 'translateY(' + ((1 - ein) * 120).toFixed(1) + 'px)';
    }
    var s = prog > 0.6 ? Math.min(screens.length - 1, Math.floor((prog - 0.6) / 0.4 * screens.length)) : 0;
    if (s !== aktiv) {
      aktiv = s;
      screens.forEach(function (el, i) { el.classList.toggle('active', i === s); });
      punkte.forEach(function (el, i) { el.classList.toggle('an', i === s); });
    }
  }
  window.addEventListener('scroll', function () { if (!geplant) { geplant = true; requestAnimationFrame(inszenieren); } }, { passive: true });
  window.addEventListener('resize', inszenieren);
  inszenieren();
})();
