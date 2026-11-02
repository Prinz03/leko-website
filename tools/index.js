(function () {
  'use strict';
  var ruhig = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // ── Hero (sticky): Vorzeile, Unterzeile und Buttons treten zuerst zurück, die Headline zuletzt – das Licht wird stärker ──
  var hero = document.querySelector('.hero-outer');
  if (!hero) return;
  var pre = hero.querySelector('.hero-pre'), h1 = hero.querySelector('.hero-h1'), pfeil = hero.querySelector('.scroll-pfeil');
  var unten = hero.querySelectorAll('.hero-sub, .hero-ctas');
  function bis(p, start, ende) { return Math.max(0, Math.min(1, (p - start) / (ende - start))); }
  var geplant = false;
  function inszenieren() {
    geplant = false;
    var weg = hero.offsetHeight - window.innerHeight;
    var p = Math.max(0, Math.min(1, -hero.getBoundingClientRect().top / (weg || 1)));
    if (pfeil) pfeil.style.opacity = 1 - bis(p, 0, 0.1);
    if (ruhig) return;
    hero.style.setProperty('--p', p.toFixed(3));
    var a = bis(p, 0, 0.3), b = bis(p, 0, 0.2), c = bis(p, 0.6, 0.9);
    if (pre) { pre.style.opacity = 1 - a; pre.style.transform = 'translateY(' + (-20 * a).toFixed(1) + 'px)'; }
    unten.forEach(function (el) {
      el.style.opacity = 1 - b; el.style.transform = 'translateY(' + (20 * b).toFixed(1) + 'px)';
      el.style.pointerEvents = b > 0.9 ? 'none' : '';
    });
    if (h1) { h1.style.opacity = 1 - c; h1.style.transform = 'scale(' + (1 - 0.06 * c).toFixed(3) + ')'; }
  }
  window.addEventListener('scroll', function () { if (!geplant) { geplant = true; requestAnimationFrame(inszenieren); } }, { passive: true });
  window.addEventListener('resize', inszenieren);
  inszenieren();
})();
