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

// ── Väter-App: Linien vom Handy zu jedem Feature-Badge, mit laufendem Strom ──
(function () {
  'use strict';
  var NS = 'http://www.w3.org/2000/svg';
  var buehne = document.getElementById('app-buehne'), svg = document.getElementById('app-linien'), geraet = document.getElementById('app-geraet');
  if (!buehne || !svg || !geraet) return;
  function zeichnen() {
    svg.textContent = '';
    if (getComputedStyle(svg).display === 'none') return;
    var b = buehne.getBoundingClientRect(), g = geraet.getBoundingClientRect();
    svg.setAttribute('viewBox', '0 0 ' + b.width + ' ' + b.height);
    var zaehler = { l: 0, r: 0 };
    buehne.querySelectorAll('.app-badge').forEach(function (badge) {
      var r = badge.getBoundingClientRect(), links = r.right <= g.left, k = zaehler[links ? 'l' : 'r']++;
      var x1 = (links ? r.right : r.left) - b.left, y1 = r.top + r.height / 2 - b.top;
      var x2 = (links ? g.left : g.right) - b.left, y2 = g.top - b.top + g.height * (links ? 0.3 + 0.2 * k : 0.38 + 0.24 * k);
      var mx = (x1 + x2) / 2, d = 'M' + x1 + ' ' + y1 + 'C' + mx + ' ' + y1 + ' ' + mx + ' ' + y2 + ' ' + x2 + ' ' + y2;
      ['app-bahn', 'app-strom'].forEach(function (klasse, i) {
        var pfad = document.createElementNS(NS, 'path');
        pfad.setAttribute('d', d); pfad.setAttribute('class', klasse);
        if (i) pfad.style.animationDelay = (-(k * 0.4 + (links ? 0 : 0.2))).toFixed(1) + 's';
        svg.appendChild(pfad);
      });
    });
  }
  zeichnen();
  if ('ResizeObserver' in window) new ResizeObserver(zeichnen).observe(buehne);
  window.addEventListener('load', zeichnen);
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(zeichnen);
  buehne.addEventListener('transitionend', zeichnen);
})();
