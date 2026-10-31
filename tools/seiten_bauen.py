"""Erzeugt index.html und datenschutz.html für die #LeKo-Website (Geometrie wird hier berechnet).

Aufruf aus dem Repo:  python3 tools/seiten_bauen.py
Quellen: tools/index.css, tools/index.js, tools/datenschutz-inhalt.html – Ausgabe ins Repo-Hauptverzeichnis.
"""
import math, pathlib, sys

HIER = pathlib.Path(__file__).resolve().parent
ZIEL = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else HIER.parent
DS_INHALT = (pathlib.Path(sys.argv[2]) if len(sys.argv) > 2 else HIER / 'datenschutz-inhalt.html').read_text()
C = 200  # Kompass-Mitte im viewBox 0 0 400 400


def pol(r, grad, c=C):
    a = math.radians(grad)
    return round(c + r * math.sin(a), 2), round(c - r * math.cos(a), 2)


def ico(d, w='1.6'):
    return (f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{w}" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{d}</svg>')


I = {
    'stern':     '<path d="M12 3l2.6 5.6 6 .7-4.5 4.1 1.2 6L12 16.4 6.7 19.4l1.2-6L3.4 9.3l6-.7z"/>',
    'hantel':    '<path d="M6 7v10M18 7v10M3 10v4M21 10v4M6 12h12"/>',
    'leute':     '<circle cx="9" cy="8" r="3"/><circle cx="17" cy="9" r="2.5"/><path d="M3 20c0-3.3 2.7-6 6-6s6 2.7 6 6M15 14.5c3 0 6 1.8 6 5.5"/>',
    'vater':     '<circle cx="8" cy="6" r="2.5"/><circle cx="16.5" cy="10" r="1.8"/><path d="M4 21v-6a4 4 0 0 1 8 0v6M14 21v-4a2.5 2.5 0 0 1 5 0v4"/>',
    'chip':      '<rect x="5" y="5" width="14" height="14" rx="2"/><path d="M9 1v4M15 1v4M9 19v4M15 19v4M1 9h4M1 15h4M19 9h4M19 15h4M9 9h6v6H9z"/>',
    'waage':     '<path d="M12 3v18M7 21h10M5 7h14"/><path d="M5 7l-3 6a3 3 0 0 0 6 0z"/><path d="M19 7l-3 6a3 3 0 0 0 6 0z"/>',
    'kalender':  '<rect x="3.5" y="5" width="17" height="15" rx="2"/><path d="M3.5 10h17M8 3v4M16 3v4"/>',
    'kontakt':   '<path d="M4 5h16v14H4z"/><circle cx="10" cy="11" r="2.4"/><path d="M6.5 16.5c.5-1.8 1.8-2.8 3.5-2.8s3 1 3.5 2.8M15 10h3M15 13h3"/>',
    'jarvis':    '<path d="M4 5h16v11H9l-5 4z"/><path d="M12 8.2l.9 1.9 2 .3-1.5 1.4.4 2-1.8-1-1.8 1 .4-2-1.5-1.4 2-.3z"/>',
    'pokal':     '<path d="M8 4h8v4a4 4 0 0 1-8 0z"/><path d="M8 6H5a3 3 0 0 0 3 4M16 6h3a3 3 0 0 1-3 4M12 12v4M9 20h6"/>',
    'protokoll': '<path d="M7 3h7l4 4v14H7z"/><path d="M14 3v4h4"/><path d="M10 12.5h5M10 16h5"/>',
    'pfeil-ab':  '<path d="M6 9l6 6 6-6"/>',
}

MINI_KOMPASS = ('<svg class="mini-kompass" viewBox="0 0 60 60" aria-hidden="true"><circle cx="30" cy="30" r="28" fill="none" stroke="#c9a84c" stroke-width="1"/>'
                '<circle cx="30" cy="30" r="21" fill="none" stroke="#c9a84c" stroke-opacity=".35" stroke-dasharray="1.5 3"/>'
                '<polygon points="30,8 34,30 30,30" fill="#c9a84c"/><polygon points="30,8 26,30 30,30" fill="#e2c97e"/>'
                '<polygon points="30,52 34,30 30,30" fill="#6e5620"/><polygon points="30,52 26,30 30,30" fill="#a8862a"/>'
                '<circle cx="30" cy="30" r="3" fill="#c9a84c"/></svg>')

# ═══ Säulen ═══
SAEULEN = [
    ('stern', 'Resilienz &amp; Persönlichkeit', 'Mentale Stärke, Klarheit und Haltung. Nicht brechen, sondern wachsen. In Bildungsseminaren und Gesprächen geht es um Selbstführung, den Umgang mit Druck und innere Stabilität – damit du auch in stürmischen Zeiten Kurs hältst.'),
    ('hantel', 'Sport &amp; Bewegung', 'Ein starker Körper ist das Fundament. Gemeinsame Trainings und Events, vom lockeren Lauf bis zur echten Herausforderung. Jeder startet dort, wo er gerade steht – es geht um Weiterkommen, nicht um Höchstleistung.'),
    ('leute', 'Gemeinschaft', 'Männer, die zuhören, ohne zu urteilen. Und die da sind, wenn es zählt. Bei unseren Treffen, in der Telegram-Community und überall dort, wo einer den anderen braucht.'),
    ('vater', 'Vaterschaft &amp; Neuanfang', 'Der Vater sein, den du dir selbst gewünscht hättest. Auch nach einer Trennung. Austausch mit Männern in ähnlicher Lage und Orientierung, wenn der Alltag plötzlich ein anderer ist.'),
    ('chip', 'Neue Technologien', 'KI und digitale Werkzeuge verstehen und nutzen, statt abgehängt zu werden. Wir erklären verständlich und praxisnah – ohne Fachchinesisch.'),
]
R_NETZ = 38
pos = [(round(50 + R_NETZ * math.cos(math.radians(-90 + 72 * n)), 2), round(50 + R_NETZ * math.sin(math.radians(-90 + 72 * n)), 2)) for n in range(5)]
FLOAT = ['3s', '3.5s', '4s', '4.5s', '5s']
linien = ''.join(
    f'<path class="netz-linie" id="nl-{n}" data-linie="{n}" d="M50 50L{x} {y}"/>'
    f'<circle class="energie" r=".9"><animateMotion dur="2.4s" begin="{-n * .45:.2f}s" repeatCount="indefinite"><mpath href="#nl-{n}"/></animateMotion></circle>'
    for n, (x, y) in enumerate(pos))
knoten = ''.join(
    f'\n      <button class="knoten" type="button" data-saeule="{n}" style="--x:{x}%;--y:{y}%;--f:{FLOAT[n]}" aria-haspopup="dialog">'
    f'{ico(I[k])}<span class="knoten-nr" aria-hidden="true">{n + 1}</span><span class="knoten-name">{t}</span></button>'
    for n, ((k, t, _), (x, y)) in enumerate(zip(SAEULEN, pos)))
saeulen_liste = ''.join(
    f'\n      <div class="akk-item"><button class="akk-frage" type="button" aria-expanded="false" aria-controls="sl-{n}">'
    f'<span class="akk-ico">{ico(I[k])}</span><span class="akk-titel"><small>Säule {n + 1}</small>{t}</span><span class="chevron">{ico(I["pfeil-ab"], "2")}</span></button>'
    f'<div class="akk-antwort" id="sl-{n}" role="region"><p>{txt}</p></div></div>'
    for n, (k, t, txt) in enumerate(SAEULEN))
saeulen_js = ',\n    '.join("{ titel: '" + t.replace('&amp;', '&') + "', text: '" + txt + "' }" for _, t, txt in SAEULEN)

# ═══ App ═══
FEATURES_L = [('waage', 'Rechtliche Orientierung', 'Obsorge, Besuchsrecht, Unterhalt — klar erklärt nach österreichischem Recht.'),
              ('leute', 'Väter-Community', 'Männer, die wirklich verstehen, was du durchmachst. Kein Ratschlag — echte Erfahrung.'),
              ('kalender', 'Kalender &amp; Kinderzeit', 'Plane Wochenenden und Ferien mit System. Damit du nichts verpasst.')]
FEATURES_R = [('kontakt', 'Fachliche Kontakte', 'Direkter Zugang zu Familienrechts-Experten in Österreich.'),
              ('jarvis', 'Jarvis Vereinsassistent', 'KI-gestützte Antworten, Protokolle und Erinnerungen im Telegram.'),
              ('pokal', 'Sportevents &amp; Mitglieder', 'Gemeinsame Aktivitäten und ein exklusiver Bereich nur für Mitglieder.')]
BFLOAT = ['4.2s', '5s', '4.6s', '5.4s', '4.4s', '4.8s']


def bubbles(liste, start):
    return ''.join(
        f'\n        <div class="bubble" data-bubble="{start + n}" style="--f:{BFLOAT[start + n]};--fv:{-(start + n) * .7:.1f}s">'
        f'<span class="b-ico">{ico(I[k])}</span><div><b><span class="b-nr">{start + n + 1:02d}</span>{t}</b><p>{txt}</p></div></div>'
        for n, (k, t, txt) in enumerate(liste))


MINI = [('kalender', 'Kalender', 'Sa · Kinderzeit'), ('leute', 'Community', '12 neue Beiträge'),
        ('protokoll', 'Protokoll', 'Entwurf gespeichert'), ('kontakt', 'Kontakte', 'Fachleute in der Nähe')]
mini_karten = ''.join(f'\n              <div class="mini">{ico(I[k], "1.7")}<b>{h}</b><small>{u}</small></div>' for k, h, u in MINI)

FAQ = [
    ('Muss ich sportlich sein?', 'Nein. Jeder startet dort, wo er gerade steht. Es geht um Weiterkommen, nicht um Höchstleistung.'),
    ('Kann ich erst schnuppern?', 'Ja. Komm zu einem offenen Treffen und lern uns kennen, ganz ohne Verpflichtung.'),
    ('Für wen ist #LeKo gedacht?', 'Für Männer zwischen 25 und 50, die mehr Klarheit, Stärke und echte Gemeinschaft wollen – ob Single, Partner, Vater oder im Neuanfang.'),
    ('Was kosten die Seminare?', 'Für Bildungsseminare gibt es einen Förderbeitrag, den wir bei jedem Termin transparent angeben. Der Verein ist gemeinnützig und arbeitet nicht gewinnorientiert.'),
    ('Wie werde ich Mitglied?', 'Über einen Aufnahmeantrag. Das Präsidium entscheidet über die Aufnahme. Die Mitgliedschaft läuft ein Jahr und verlängert sich automatisch; du kannst jederzeit schriftlich kündigen.'),
]
faq_html = ''.join(
    f'\n      <div class="akk-item"><button class="akk-frage" type="button" aria-expanded="false" aria-controls="faq-{n}">'
    f'<span class="akk-titel">{q}</span><span class="chevron">{ico(I["pfeil-ab"], "2")}</span></button>'
    f'<div class="akk-antwort" id="faq-{n}" role="region"><p>{a}</p></div></div>'
    for n, (q, a) in enumerate(FAQ, 1))


# ═══ Gemeinsame Teile ═══
def kopf(vor):
    links = [('saeulen', 'Säulen'), ('app', 'Väter-App'), ('haltung', 'Haltung'), ('faq', 'FAQ'), ('kontakt', 'Kontakt')]
    li = ''.join(f'<li><a href="{vor}#{a}">{n}</a></li>' for a, n in links)
    sl = ''.join(f'\n    <a href="{vor}#{a}">{n}</a>' for a, n in links)
    return f'''<header class="kopf" id="kopf">
  <div class="wrap">
    <a href="{vor}#top" class="marke"><img src="assets/logo/logo-128x128.png" alt="" width="36" height="36">#LeKo</a>
    <ul class="kopf-links">{li}</ul>
    <a href="{vor}#mitglied" class="btn btn-gold kopf-cta"><span class="lang">Jetzt&nbsp;</span>Mitglied werden</a>
    <button class="burger" id="burger" type="button" aria-label="Menü öffnen" aria-expanded="false" aria-controls="schublade"><span></span></button>
  </div>
  <nav class="schublade" id="schublade" aria-label="Mobile Navigation">{sl}
  </nav>
</header>'''


def fuss(ds_link):
    return f'''<footer class="fuss">
  <div class="wrap">
    <span>© 2026 Lebenskompass – ZVR 1346040358</span>
    <nav aria-label="Rechtliches"><button type="button" data-modal="impressum">Impressum</button><span aria-hidden="true">|</span>{ds_link}</nav>
  </div>
</footer>

<dialog class="modal" id="impressum" aria-labelledby="impressum-titel">
  <button class="schliessen" type="button" data-schliessen aria-label="Schließen">×</button>
  <div class="modal-innen">
    <p class="eyebrow">Impressum</p>
    <h2 id="impressum-titel">#LeKo</h2>
    <p><strong>Lebenskompass – Bildungsverein zur Förderung gesunder Bewegung, Resilienz, Persönlichkeitsentwicklung und Integration von neuen Technologien</strong></p>
    <p>Tirolerweg 11, 9073 Klagenfurt am Wörthersee, Österreich<br>ZVR-Zahl: 1346040358</p>
    <p>Vertreten durch: Markus Prinz (Präsident)<br>E-Mail: <a href="mailto:leko.verein@gmail.com">leko.verein@gmail.com</a></p>
    <p>Gemeinnütziger Verein im Sinne der §§ 34 ff BAO.</p>
  </div>
</dialog>'''


KOPF_META = '''<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="theme-color" content="#080808">
<link rel="icon" type="image/png" sizes="128x128" href="assets/logo/logo-128x128.png">
<link rel="apple-touch-icon" href="assets/logo/logo-256x256.png">
<link rel="stylesheet" href="assets/fonts/fonts.css">
<link rel="stylesheet" href="assets/site.css">'''

INDEX_CSS = (HIER / 'index.css').read_text()
INDEX_JS = (HIER / 'index.js').read_text().replace('/*SAEULEN*/', saeulen_js)

index = f'''<!DOCTYPE html>
<html lang="de-AT">
<head>
{KOPF_META}
<title>#LeKo – Stärker werden. Nicht allein.</title>
<meta name="description" content="#LeKo ist die Gemeinschaft für Männer von 25 bis 50 in Kärnten: Bildungsseminare, Bewegung, Resilienz und echte Bruderschaft. Gemeinnützig aus Klagenfurt.">
<meta property="og:title" content="#LeKo – Stärker werden. Nicht allein.">
<meta property="og:description" content="Bildungsseminare, Bewegung und Männer, auf die du zählen kannst. Gemeinnützig aus Klagenfurt.">
<meta property="og:image" content="https://prinz03.github.io/leko-website/assets/logo/logo-512x512.png">
<meta property="og:url" content="https://prinz03.github.io/leko-website/">
<meta property="og:type" content="website">
<meta property="og:locale" content="de_AT">
<style>
{INDEX_CSS}</style>
</head>
<body>
<a class="skip" href="#inhalt">Zum Inhalt springen</a>

{kopf('')}

<main id="inhalt">

<!-- ═══ 1 · HERO (Scroll-Kompass) ═══ -->
<section class="hero-outer" id="top">
  <div class="hero-sticky">

    <div class="hero-content wrap">
      <p class="eyebrow auftritt" style="--d:.5s">Es ist an der Zeit, Deinen Kompass neu auszurichten.</p>
      <h1><span class="auftritt" style="--d:.8s">Stärker werden.</span><span class="gold-kursiv auftritt" style="--d:1.1s">Nicht allein.</span></h1>
      <p class="lead auftritt" style="--d:1.25s">#LeKo ist die Gemeinschaft für Männer von 25 bis 50 in Kärnten: Bildungsseminare, Bewegung und Brüder, auf die du zählen kannst.</p>
      <div class="knoepfe auftritt" style="--d:1.4s">
        <a href="#mitglied" class="btn btn-gold">Jetzt Mitglied werden <span class="pfeil" aria-hidden="true">→</span></a>
        <a href="#kontakt" class="btn btn-dunkel">Unverbindlich kennenlernen</a>
      </div>
    </div>

    <div class="scroll-indicator" aria-hidden="true">↓</div>

  </div>
</section>

<!-- ═══ BRÜCKE ═══ -->
<section class="bruecke-section">
  <div class="bruecke-inner">
    <p class="bruecke-text">Du bist nicht allein damit.</p>
    <p class="bruecke-text bruecke-text--sub">Es ist nicht zu spät.</p>
  </div>
</section>

<!-- ═══ 2 · KENNST DU DAS (Sticky Cards) ═══ -->
<section class="kennst-outer" id="kennst-du-das" aria-label="Kennst du das?">
  <div class="kennst-sticky">
    <div class="haltung-label">Kennst du das?</div>
    <div class="kennst-progress">
      <div class="kennst-progress-bar" id="kennstBar"></div>
    </div>

    <div class="kennst-card" data-index="0">
      <div class="kennst-card-inner">
        <span class="kennst-nummer">01</span>
        <h3>Du willst mehr —<br>weißt aber nicht wie.</h3>
        <p>Du spürst, dass da noch mehr in dir steckt. Aber der Alltag holt dich immer wieder ein. Und du weißt nicht, wo du anfangen sollst.</p>
      </div>
    </div>

    <div class="kennst-card" data-index="1">
      <div class="kennst-card-inner">
        <span class="kennst-nummer">02</span>
        <h3>Du fühlst dich<br>allein damit.</h3>
        <p>In deinem Umfeld redet niemand über solche Dinge. Also hältst du es für dich. Dabei bräuchtest du genau jetzt jemanden, der zuhört.</p>
      </div>
    </div>

    <div class="kennst-card" data-index="2">
      <div class="kennst-card-inner">
        <span class="kennst-nummer">03</span>
        <h3>Der innere Kompass<br>zeigt kein Nord.</h3>
        <p>Entscheidungen fallen schwer. Du weißt nicht, was wirklich zu dir passt — und was du nur glaubst, tun zu müssen.</p>
      </div>
    </div>

    <div class="kennst-card" data-index="3">
      <div class="kennst-card-inner">
        <span class="kennst-nummer">04</span>
        <h3>Du bist bereit.<br>Aber es fehlt der Rahmen.</h3>
        <p>Du willst wachsen, Verantwortung übernehmen, Gleichgesinnte finden. Was fehlt, ist eine Gemeinschaft, die das mit dir trägt.</p>
      </div>
    </div>
  </div>
</section>

<!-- ═══ 3 · 5 SÄULEN ═══ -->
<section class="sektion saeulen" id="saeulen" aria-labelledby="saeulen-titel">
  <div class="wrap">
    <div class="kopfzeile ein">
      <p class="eyebrow">Was wir tun</p>
      <h2 id="saeulen-titel">Die 5 Säulen von <em>#LeKo</em></h2>
      <p class="lead">Jede Säule ist ein Bereich, in dem wir dich fördern und fordern. <span class="nur-gross">Klick auf eine Säule.</span></p>
    </div>
    <div class="netz ein" id="netz">
      <svg class="netz-linien" viewBox="0 0 100 100" aria-hidden="true">{linien}</svg>
      <div class="vereinssiegel" id="saulenChip" aria-hidden="true">
        <div class="siegel-glow"></div>
        <svg class="siegel-svg" viewBox="0 0 160 160" xmlns="http://www.w3.org/2000/svg">
          <circle cx="80" cy="80" r="76" fill="none" stroke="#c9a84c" stroke-width="1.5" opacity="0.6"/>
          <circle cx="80" cy="80" r="68" fill="none" stroke="#c9a84c" stroke-width="0.5" opacity="0.3"/>
          <path id="kreisTextPfad" d="M80,80 m-63,0 a63,63 0 1,1 126,0 a63,63 0 1,1 -126,0" fill="none"/>
          <text font-family="Playfair Display,serif" font-size="9.5" fill="#c9a84c" letter-spacing="3.5" opacity="0.85"><textPath href="#kreisTextPfad" startOffset="8%">VEREIN LEBENSKOMPASS · ÖSTERREICH ·</textPath></text>
          <circle cx="80" cy="80" r="54" fill="#0f0e08" stroke="#c9a84c" stroke-width="1" opacity="0.5"/>
          <circle cx="80" cy="58" r="9" fill="none" stroke="#c9a84c" stroke-width="1.5"/>
          <path d="M65,90 Q80,76 95,90" fill="none" stroke="#c9a84c" stroke-width="1.5" stroke-linecap="round"/>
          <circle cx="57" cy="62" r="7" fill="none" stroke="#c9a84c" stroke-width="1.2" opacity="0.7"/>
          <path d="M46,90 Q57,79 68,90" fill="none" stroke="#c9a84c" stroke-width="1.2" stroke-linecap="round" opacity="0.7"/>
          <circle cx="103" cy="62" r="7" fill="none" stroke="#c9a84c" stroke-width="1.2" opacity="0.7"/>
          <path d="M92,90 Q103,79 114,90" fill="none" stroke="#c9a84c" stroke-width="1.2" stroke-linecap="round" opacity="0.7"/>
          <path d="M64,66 Q80,56 96,66" fill="none" stroke="#c9a84c" stroke-width="0.8" stroke-dasharray="2,3" opacity="0.45"/>
          <text x="80" y="116" text-anchor="middle" font-family="Playfair Display,serif" font-size="8.5" fill="#c9a84c" letter-spacing="3" opacity="0.8">LEBENSKOMPASS</text>
          <line x1="55" y1="108" x2="105" y2="108" stroke="#c9a84c" stroke-width="0.5" opacity="0.4"/>
          <circle cx="80" cy="27" r="2" fill="#c9a84c" opacity="0.6"/>
          <circle cx="80" cy="133" r="2" fill="#c9a84c" opacity="0.6"/>
          <circle cx="27" cy="80" r="2" fill="#c9a84c" opacity="0.6"/>
          <circle cx="133" cy="80" r="2" fill="#c9a84c" opacity="0.6"/>
        </svg>
      </div>{knoten}
    </div>
    <div class="saeulen-liste">{saeulen_liste}
    </div>
  </div>
</section>

<dialog class="modal" id="saeule-panel" aria-labelledby="saeule-titel">
  <button class="schliessen" type="button" data-schliessen aria-label="Schließen">×</button>
  <div class="modal-innen">
    <div class="panel-kopf"><span class="panel-ico" id="saeule-ico"></span><div><p class="eyebrow" id="saeule-nr"></p><h2 id="saeule-titel"></h2></div></div>
    <p id="saeule-text"></p>
  </div>
</dialog>

<!-- ═══ 4 · VÄTER-APP ═══ -->
<section class="sektion app" id="app" aria-labelledby="app-titel">
  <div class="wrap">
    <div class="kopfzeile ein">
      <span class="badge">Bald verfügbar</span>
      <h2 id="app-titel">Die #LeKo <em>Väter-App</em></h2>
      <p class="lead">Für Väter in Trennungssituationen und für jeden Mann, der Orientierung sucht: verständliche Infos, Rückhalt und eine echte Community.</p>
    </div>
    <div class="app-buehne" id="app-buehne">
      <svg class="app-linien" id="app-linien" aria-hidden="true"></svg>
      <div class="bubbles links">{bubbles(FEATURES_L, 0)}
      </div>
      <div class="handy-stage" aria-hidden="true">
        <div class="handy" id="handy">
          <span class="notch"></span>
          <div class="screen">
            <div class="screen-kopf"><b>#LeKo App</b>{MINI_KOMPASS.replace('mini-kompass', 'screen-logo')}</div>
            <p class="screen-gruss">Willkommen zurück</p>
            <div class="mini-grid">{mini_karten}
            </div>
            <div class="mini breit">{ico(I['stern'], '1.7')}<div><b>Nächstes Treffen</b><small>Do · 19:00 · Klagenfurt</small></div></div>
            <div class="tabbar"><i></i><i></i><i></i><i></i></div>
          </div>
        </div>
      </div>
      <div class="bubbles rechts">{bubbles(FEATURES_R, 3)}
      </div>
    </div>
  </div>
</section>

<!-- ═══ 5 · HALTUNG (2×2) ═══ -->
<section class="haltung-section" id="haltung" aria-labelledby="haltung-titel">
  <div class="haltung-container">
    <div class="haltung-heading-block">
      <h2 class="haltung-heading" id="haltung-titel">Unsere Haltung</h2>
      <p class="haltung-sub">Was uns trägt — und was uns unterscheidet.</p>
    </div>
    <div class="haltung-grid">
      <div class="haltung-karte">
        <div class="haltung-karte-icon" aria-hidden="true">◈</div>
        <h3>Gemeinnützig</h3>
        <p>Wir handeln ohne Gewinnabsicht. Alles, was wir aufbauen, dient dem Verein — nicht einzelnen Personen. Jeder Beitrag fließt zurück in die Gemeinschaft.</p>
      </div>
      <div class="haltung-karte">
        <div class="haltung-karte-icon" aria-hidden="true">◈</div>
        <h3>Respekt</h3>
        <p>Jede Geschichte verdient Gehör. Bei uns gibt es keine falschen Gefühle, keine unreifen Fragen. Wer sich zeigt, wird gesehen — ohne Wertung.</p>
      </div>
      <div class="haltung-karte">
        <div class="haltung-karte-icon" aria-hidden="true">◈</div>
        <h3>Unabhängig</h3>
        <p>Keine Partei, keine Doktrin, keine Ideologie. Wir sind ein Ort für Menschen — nicht für Meinungen. Deine Richtung bestimmst du selbst.</p>
      </div>
      <div class="haltung-karte">
        <div class="haltung-karte-icon" aria-hidden="true">◈</div>
        <h3>Kein Therapie-Ersatz</h3>
        <p>Wir bieten Gemeinschaft und Orientierung. Wer professionelle Hilfe braucht, wird von uns ermutigt, sie zu suchen — nicht aufgehalten.</p>
      </div>
    </div>
    <div class="krisen-box">
      <p class="krisen-title">Notfall? Diese Nummern helfen sofort</p>
      <div class="krisen-nummern">
        <a href="tel:142">142 — Telefonseelsorge</a>
        <a href="tel:144">144 — Rettung</a>
        <a href="tel:133">133 — Polizei</a>
      </div>
    </div>
  </div>
</section>

<!-- ═══ 6 · MITGLIED WERDEN ═══ -->
<section class="sektion mitglied" id="mitglied" aria-labelledby="mitglied-titel">
  <div class="wrap">
    <div class="mitglied-block ein">
      <p class="eyebrow">Mitgliedschaft</p>
      <h2 id="mitglied-titel">Bereit, deinen Kompass <em>neu auszurichten?</em></h2>
      <p class="lead">Jahresbeitrag, automatische Verlängerung, jederzeit schriftlich kündbar.</p>
      <ul class="vorteile">
        <li>Zugang zu allen Bildungsseminaren</li>
        <li>Mitglied der Telegram-Community</li>
        <li>#LeKo App (Väter-Bereich)</li>
        <li>Sportevents &amp; gemeinsame Aktivitäten</li>
        <li>Persönliches Erstgespräch mit Markus Prinz</li>
        <li>Zugang zum Übergabeprotokoll-System</li>
      </ul>
      {MINI_KOMPASS}
      <div class="knoepfe">
        <a href="mailto:leko.verein@gmail.com?subject=Mitgliedschaft%20%23LeKo" class="btn btn-gold">Jetzt Mitglied werden <span class="pfeil" aria-hidden="true">→</span></a>
        <a href="#kontakt" class="btn btn-dunkel">Unverbindlich kennenlernen</a>
      </div>
    </div>
  </div>
</section>

<!-- ═══ 7 · FAQ ═══ -->
<section class="sektion faq" id="faq" aria-labelledby="faq-titel">
  <div class="wrap schmal">
    <div class="kopfzeile ein">
      <p class="eyebrow">Fragen</p>
      <h2 id="faq-titel">Ehrliche <em>Antworten.</em></h2>
    </div>
    <div class="akk ein">{faq_html}
    </div>
  </div>
</section>

<!-- ═══ 8 · KONTAKT ═══ -->
<section class="sektion kontakt" id="kontakt" aria-labelledby="kontakt-titel">
  <div class="wrap schmal">
    <div class="ein">
      <p class="eyebrow">Kontakt</p>
      <h2 id="kontakt-titel">Schreib <em>uns.</em></h2>
      <a class="mail" href="mailto:leko.verein@gmail.com">leko.verein@gmail.com</a>
      <p class="lead">Wir melden uns so schnell wie möglich.</p>
      <a href="#mitglied" class="btn btn-gold">Jetzt Mitglied werden <span class="pfeil" aria-hidden="true">→</span></a>
    </div>
  </div>
</section>

</main>

{fuss('<a href="datenschutz.html" target="_blank" rel="noopener">Datenschutz</a>')}

<script src="assets/site.js"></script>
<script>
{INDEX_JS}</script>
</body>
</html>
'''

datenschutz = f'''<!DOCTYPE html>
<html lang="de-AT">
<head>
{KOPF_META}
<title>Datenschutzerklärung – #LeKo</title>
<meta name="description" content="Datenschutzerklärung des Vereins Lebenskompass (#LeKo), Klagenfurt am Wörthersee.">
<style>
.ds{{padding:calc(var(--nav-h) + 72px) 0 100px}}
.ds .wrap{{max-width:820px}}
.ds h1{{font-size:clamp(2.4rem,7vw,4.2rem);margin:14px 0 22px}}
.ds h1 em{{font-style:italic;color:var(--gold)}}
.ds .lead{{margin-bottom:40px}}
.privacy{{color:var(--text-2);font-size:1rem}}
.privacy h3{{font-family:var(--serif);color:var(--white);font-size:1.35rem;margin:40px 0 10px;padding-top:24px;border-top:1px solid var(--linie)}}
.privacy p{{margin-bottom:12px;overflow-wrap:anywhere}}
.privacy ul{{margin:0 0 12px 1.2rem}}
.privacy li{{margin-bottom:6px}}
.privacy strong{{color:var(--white);font-weight:600}}
.privacy a{{color:var(--gold)}}
.stand{{margin-top:36px;font-size:.85rem;color:var(--text-2)}}
.zurueck{{margin-top:40px}}
</style>
</head>
<body>
<a class="skip" href="#inhalt">Zum Inhalt springen</a>

{kopf('index.html')}

<main id="inhalt" class="ds">
  <div class="wrap">
    <p class="eyebrow">Datenschutz</p>
    <h1>Datenschutz<em>erklärung</em></h1>
    <p class="lead">Der Schutz deiner Daten ist uns wichtig. Wir verarbeiten personenbezogene Daten nur auf Grundlage der Datenschutz-Grundverordnung (DSGVO) und des österreichischen Datenschutzgesetzes (DSG). Hier erfährst du, welche Daten das sind und welche Rechte du hast.</p>
    <div class="privacy">
{DS_INHALT}
    </div>
    <p class="stand">Stand: Oktober 2026</p>
    <a href="index.html" class="btn btn-dunkel zurueck">← Zur Startseite</a>
  </div>
</main>

{fuss('<a href="datenschutz.html" aria-current="page">Datenschutz</a>')}

<script src="assets/site.js"></script>
</body>
</html>
'''

(ZIEL / 'index.html').write_text(index)
(ZIEL / 'datenschutz.html').write_text(datenschutz)
print('index.html', len(index), 'Zeichen · datenschutz.html', len(datenschutz), 'Zeichen')
