(function () {
  'use strict';
  var ruhig = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var NS = 'http://www.w3.org/2000/svg';

  // ── Inszenierung beim Scrollen: Headline weicht dem Kompass, Brücken-Satz leuchtet Zeile für Zeile auf ──
  var hinweis = document.querySelector('.scroll-indicator');
  var heroAussen = document.querySelector('.hero-outer'), bruecke = document.querySelector('.bruecke-section');
  var heroText = document.querySelector('.hero-content'), kompass = document.querySelector('.hero-kompass');
  var zeilen = bruecke ? bruecke.querySelectorAll('.bruecken-satz span') : [];
  function fortschritt(el) {
    var weg = el.offsetHeight - window.innerHeight;
    return Math.max(0, Math.min(1, -el.getBoundingClientRect().top / (weg || 1)));
  }
  var geplant = false;
  function inszenieren() {
    geplant = false;
    if (hinweis) hinweis.style.opacity = Math.max(0, 1 - window.scrollY / (window.innerHeight * 0.3));
    if (ruhig) return;
    if (heroAussen) {
      // ab 40 % des Hero-Wegs: Headline tritt zurück, Kompass blendet ein; ab 60 % dreht sich die Nadel
      var prog = fortschritt(heroAussen), kProg = Math.max(0, Math.min(1, (prog - 0.4) / 0.45));
      heroAussen.style.setProperty('--p', prog.toFixed(3));
      if (kompass) {
        kompass.classList.toggle('sichtbar', prog > 0.4);
        kompass.style.setProperty('--winkel', (Math.max(0, Math.min(1, (prog - 0.6) / 0.25)) * 15).toFixed(2) + 'deg');
      }
      if (heroText) {
        heroText.style.opacity = Math.max(0, 1 - kProg * 2);
        heroText.style.transform = 'translateY(' + (-kProg * 40).toFixed(1) + 'px)';
      }
    }
    if (bruecke) {
      var q = fortschritt(bruecke);
      zeilen.forEach(function (z, i) { z.style.setProperty('--l', Math.max(0, Math.min(1, (q - i * 0.35) / 0.4)).toFixed(3)); });
    }
  }
  window.addEventListener('scroll', function () { if (!geplant) { geplant = true; requestAnimationFrame(inszenieren); } }, { passive: true });
  window.addEventListener('resize', inszenieren);
  inszenieren();

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
})();
