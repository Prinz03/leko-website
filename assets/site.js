/* #LeKo – gemeinsame Logik: Header, Mobil-Menü, Impressum-Modal, Jahreszahl, Einblenden, Akkordeons, Väter-App */
(function () {
  'use strict';

  // Header: transparent → Glas-Leiste beim Scrollen
  var kopf = document.getElementById('kopf');
  function kopfZustand() { kopf.classList.toggle('solid', window.scrollY > 24); }
  kopfZustand();
  window.addEventListener('scroll', kopfZustand, { passive: true });

  // Mobil-Menü
  var burger = document.getElementById('burger');
  function menue(auf) {
    kopf.classList.toggle('offen', auf);
    burger.setAttribute('aria-expanded', String(auf));
    burger.setAttribute('aria-label', auf ? 'Menü schließen' : 'Menü öffnen');
    document.body.style.overflow = auf ? 'hidden' : '';
  }
  burger.addEventListener('click', function () { menue(!kopf.classList.contains('offen')); });
  document.querySelectorAll('.schublade a').forEach(function (a) { a.addEventListener('click', function () { menue(false); }); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') menue(false); });

  // Modale Fenster (Impressum): öffnen per data-modal, schließen per × oder Klick daneben
  document.querySelectorAll('[data-modal]').forEach(function (k) {
    k.addEventListener('click', function () {
      var d = document.getElementById(k.getAttribute('data-modal'));
      if (d && d.showModal) d.showModal();
    });
  });
  document.querySelectorAll('dialog.modal').forEach(function (d) {
    d.addEventListener('click', function (e) { if (e.target === d || e.target.closest('[data-schliessen]')) d.close(); });
  });

  // Jahreszahl im Footer
  document.querySelectorAll('[data-jahr]').forEach(function (el) { el.textContent = new Date().getFullYear(); });

  // Einblenden beim Scrollen: alles mit data-reveal gleitet sanft herein (optional versetzt per data-reveal-delay in ms)
  if ('IntersectionObserver' in window) {
    var beob = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('revealed'); beob.unobserve(e.target); } });
    }, { threshold: 0.15 });
    document.querySelectorAll('[data-reveal]').forEach(function (el) {
      el.style.opacity = '0';
      el.style.transform = 'translateY(30px)';
      el.style.transition = 'opacity .7s ease, transform .7s ease';
      if (el.dataset.revealDelay) el.style.transitionDelay = el.dataset.revealDelay + 'ms';
      beob.observe(el);
    });
  }

  // Akkordeons mit weicher Höhenanimation (FAQ)
  document.querySelectorAll('.akk-frage').forEach(function (knopf) {
    knopf.addEventListener('click', function () {
      var item = knopf.closest('.akk-item'), antwort = item.querySelector('.akk-antwort');
      var auf = !item.classList.contains('offen');
      antwort.style.height = antwort.scrollHeight + 'px';
      if (auf) {
        antwort.addEventListener('transitionend', function fertig() {
          if (item.classList.contains('offen')) antwort.style.height = 'auto';
          antwort.removeEventListener('transitionend', fertig);
        });
      } else {
        void antwort.offsetHeight;
        antwort.style.height = '0px';
      }
      item.classList.toggle('offen', auf);
      knopf.setAttribute('aria-expanded', String(auf));
    });
  });

  // Väter-App (Desktop): Handy steht, die Features wechseln mit dem Scroll-Fortschritt
  (function initAppScroll() {
    var outer = document.querySelector('.app-sticky-outer'), schritte = document.querySelectorAll('.app-schritt');
    var handy = document.querySelector('.app-handy'), titel = document.querySelector('.handy-aktiv-titel'), text = document.querySelector('.handy-aktiv-text');
    var punkte = document.querySelectorAll('.handy-punkte i');
    if (!outer || !schritte.length) return;
    var daten = Array.prototype.map.call(schritte, function (s) {
      return { titel: s.querySelector('h3').textContent, text: s.querySelector('p').textContent };
    });
    var aktuell = -1, glimmen;
    function update() {
      var weg = outer.offsetHeight - window.innerHeight;
      var prog = weg > 0 ? Math.max(0, Math.min(1, -outer.getBoundingClientRect().top / weg)) : 0;
      var schritt = Math.min(schritte.length - 1, Math.floor(prog * schritte.length));
      if (schritt === aktuell) return;
      aktuell = schritt;
      schritte.forEach(function (s, i) { s.classList.toggle('aktiv', i === schritt); });
      punkte.forEach(function (p, i) { p.classList.toggle('an', i === schritt); });
      if (titel) titel.textContent = daten[schritt].titel;
      if (text) text.textContent = daten[schritt].text;
      if (handy) {  // kurzes Aufglühen beim Wechsel
        handy.classList.add('glueht');
        clearTimeout(glimmen);
        glimmen = setTimeout(function () { handy.classList.remove('glueht'); }, 400);
      }
    }
    window.addEventListener('scroll', update, { passive: true });
    window.addEventListener('resize', update);
    update();
  })();
})();
