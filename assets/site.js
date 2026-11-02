/* #LeKo – gemeinsame Logik: Header, Mobil-Menü, Impressum-Modal, Jahreszahl, Einblenden, Akkordeons */
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
})();
