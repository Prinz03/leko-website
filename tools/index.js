(function () {
  'use strict';
  var ruhig = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var NS = 'http://www.w3.org/2000/svg';

  // ── Hero: Scroll-Pfeil blendet beim ersten Scrollen aus ──
  var hinweis = document.querySelector('.scroll-indicator');
  if (hinweis) {
    var pfeilAus = function () { hinweis.style.opacity = Math.max(0, 1 - window.scrollY / (window.innerHeight * 0.3)); };
    window.addEventListener('scroll', pfeilAus, { passive: true });
    pfeilAus();
  }

  // ── Sticky Cards: Kennst du das? (Karte wechselt mit dem Scroll-Fortschritt) ──
  function stickyKarten(aussenSel, kartenSel, balkenId) {
    var aussen = document.querySelector(aussenSel), karten = document.querySelectorAll(kartenSel), balken = document.getElementById(balkenId);
    if (!aussen || !karten.length) return;
    function update() {
      var gescrollt = -aussen.getBoundingClientRect().top;
      var gesamt = aussen.offsetHeight - window.innerHeight;
      var p = Math.max(0, Math.min(1, gescrollt / gesamt));
      var idx = Math.min(Math.floor(p * karten.length), karten.length - 1);
      karten.forEach(function (k, i) { k.classList.toggle('active', i === idx); });
      if (balken) balken.style.width = ((idx + 1) / karten.length * 100) + '%';
    }
    window.addEventListener('scroll', update, { passive: true });
    window.addEventListener('resize', update);
    update();
  }
  stickyKarten('.kennst-outer', '.kennst-card', 'kennstBar');

  // Säulen: Karte hervorheben lässt die passende Säule im Tempel aufleuchten
  document.querySelectorAll('.saeule-karte').forEach(function (karte) {
    var saeule = document.querySelector('.saeule[data-nr="' + karte.dataset.nr + '"]');
    if (!saeule) return;
    function an() { saeule.classList.add('aktiv'); }
    function aus() { saeule.classList.remove('aktiv'); }
    karte.addEventListener('mouseenter', an); karte.addEventListener('mouseleave', aus);
    karte.addEventListener('focus', an); karte.addEventListener('blur', aus);
    karte.addEventListener('click', function () {
      var war = saeule.classList.contains('fest');
      document.querySelectorAll('.saeule.fest').forEach(function (s) { s.classList.remove('fest'); });
      saeule.classList.toggle('fest', !war);
    });
  });

  // App: geschwungene Linien von jeder Feature-Bubble zum Handy, mit wanderndem Energie-Punkt
  var buehne = document.getElementById('app-buehne'), svg = document.getElementById('app-linien'), handy = document.getElementById('handy');
  function linienZeichnen() {
    svg.textContent = '';
    if (getComputedStyle(svg).display === 'none') return;
    var b0 = buehne.getBoundingClientRect(), h = handy.getBoundingClientRect(), zaehler = { l: 0, r: 0 };
    svg.setAttribute('viewBox', '0 0 ' + b0.width + ' ' + b0.height);
    document.querySelectorAll('.bubble').forEach(function (b, n) {
      var r = b.getBoundingClientRect(), links = r.right <= h.left, k = zaehler[links ? 'l' : 'r']++;
      var x1 = (links ? r.right : r.left) - b0.left, y1 = r.top + r.height / 2 - b0.top;
      var x2 = (links ? h.left : h.right) - b0.left, y2 = h.top - b0.top + h.height * (0.3 + 0.2 * k);
      var mx = (x1 + x2) / 2;
      var pfad = document.createElementNS(NS, 'path');
      pfad.setAttribute('d', 'M' + x1 + ' ' + y1 + 'C' + mx + ' ' + y1 + ' ' + mx + ' ' + y2 + ' ' + x2 + ' ' + y2);
      pfad.setAttribute('class', 'app-bahn'); pfad.id = 'app-bahn-' + n;
      svg.appendChild(pfad);
      var punkt = document.createElementNS(NS, 'circle');
      punkt.setAttribute('class', 'app-funke'); punkt.setAttribute('r', '3.5');
      if (ruhig) { punkt.setAttribute('cx', x2); punkt.setAttribute('cy', y2); }
      else {
        var lauf = document.createElementNS(NS, 'animateMotion');
        lauf.setAttribute('dur', (2.6 + n * 0.2).toFixed(1) + 's'); lauf.setAttribute('begin', (-n * 0.5).toFixed(1) + 's'); lauf.setAttribute('repeatCount', 'indefinite');
        var mp = document.createElementNS(NS, 'mpath'); mp.setAttribute('href', '#app-bahn-' + n);
        lauf.appendChild(mp); punkt.appendChild(lauf);
      }
      svg.appendChild(punkt);
    });
  }
  document.querySelectorAll('.bubble').forEach(function (b) {
    var n = b.dataset.bubble;
    b.addEventListener('mouseenter', function () { var p = document.getElementById('app-bahn-' + n); if (p) p.classList.add('hell'); });
    b.addEventListener('mouseleave', function () { var p = document.getElementById('app-bahn-' + n); if (p) p.classList.remove('hell'); });
  });
  linienZeichnen();
  if ('ResizeObserver' in window) new ResizeObserver(linienZeichnen).observe(buehne);
  window.addEventListener('load', linienZeichnen);
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(linienZeichnen);
  buehne.addEventListener('transitionend', function (e) { if (e.target === buehne) linienZeichnen(); });
})();
