// ── Väter-App: Linien vom Handy-Körper zu jedem Feature-Badge, mit laufendem Strom ──
(function () {
  'use strict';
  var NS = 'http://www.w3.org/2000/svg';
  var buehne = document.getElementById('app-buehne'), svg = document.getElementById('app-linien'), geraet = document.getElementById('app-koerper');
  if (!buehne || !svg || !geraet) return;
  function zeichnen() {
    svg.textContent = '';
    if (getComputedStyle(svg).display === 'none') return;
    var b = buehne.getBoundingClientRect(), g = geraet.getBoundingClientRect();
    svg.setAttribute('viewBox', '0 0 ' + b.width + ' ' + b.height);
    var zaehler = { links: 0, rechts: 0, unten: 0 };
    buehne.querySelectorAll('.app-badge').forEach(function (badge) {
      var r = badge.getBoundingClientRect(), platz = badge.dataset.platz, k = zaehler[platz]++, d;
      if (platz === 'unten') {
        // senkrecht: Oberkante des Badges → Unterkante des Handys
        var xu = r.left + r.width / 2 - b.left, y1u = r.top - b.top, y2u = g.bottom - b.top, my = (y1u + y2u) / 2;
        d = 'M' + xu + ' ' + y1u + 'C' + xu + ' ' + my + ' ' + xu + ' ' + my + ' ' + xu + ' ' + y2u;
      } else {
        var links = platz === 'links';
        var x1 = (links ? r.right : r.left) - b.left, y1 = r.top + r.height / 2 - b.top;
        var x2 = (links ? g.left : g.right) - b.left, y2 = g.top - b.top + g.height * (0.3 + 0.4 * k);
        var mx = (x1 + x2) / 2;
        d = 'M' + x1 + ' ' + y1 + 'C' + mx + ' ' + y1 + ' ' + mx + ' ' + y2 + ' ' + x2 + ' ' + y2;
      }
      ['app-bahn', 'app-strom'].forEach(function (klasse, i) {
        var pfad = document.createElementNS(NS, 'path');
        pfad.setAttribute('d', d); pfad.setAttribute('class', klasse);
        if (i) pfad.style.animationDelay = (-(k * 0.4 + { links: 0, rechts: 0.2, unten: 0.6 }[platz])).toFixed(1) + 's';
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
