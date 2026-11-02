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

# ═══ Kennst du das? ═══
SPIEGEL = [
    'Es ist 23 Uhr. Die Wohnung ist still. Deine Kinder schlafen woanders – und du weißt nicht, wohin mit dir.',
    'Du willst kein Mitleid. Aber manchmal wärst du froh, wenn irgendwer einfach fragt: <em style="color:var(--gold);font-style:italic">»Wie geht’s dir – wirklich?«</em>',
    'Du kämpfst für deine Kinder. Aber das System erklärt dir die Spielregeln nicht.',
    'Du funktionierst. Jeden Tag. Aber tief drinnen weißt du: So war das nicht geplant.',
]
spiegel_html = ''.join(f'\n    <div class="mirror-item" data-reveal><p>{s}</p></div>' for s in SPIEGEL)

# ═══ 5 Säulen (je eine Full-Screen-Sektion, abwechselnd links/rechts) ═══
SAEULEN = [
    ('Orientierung', '🧭', '#C9A84C', 'Der Vater sein, den du dir selbst gewünscht hättest.',
     'Auch nach einer Trennung, auch wenn das System gegen dich arbeitet – LeKo gibt dir den Kompass, der in keiner Schule gelehrt wurde. Orientierung für deinen Weg als Mann, als Vater, als Mensch.'),
    ('Gemeinschaft', '👥', '#D9DDE3', 'Männer, die zuhören, ohne zu urteilen.',
     'Und die da sind, wenn es zählt. In unserer Community findest du Menschen, die denselben Weg gehen – ehrlich, direkt, ohne Performance. Keine Couch, kein Therapeut. Einfach echte Männer.'),
    ('Stärke', '💪', '#C87533', 'Ein starker Körper ist das Fundament.',
     'Gemeinsame Trainings, Events und körperliche Herausforderungen – weil Stärke nicht nur im Kopf entsteht. Wir bewegen uns gemeinsam. Weil Männer, die sich gemeinsam fordern, sich gegenseitig tragen.'),
    ('Resilienz', '🔥', '#B4553A', 'Nicht brechen, sondern wachsen.',
     'Mentale Stärke, Klarheit und Haltung – nicht als Theorie, sondern als Praxis. LeKo gibt dir Werkzeuge, die auch dann funktionieren, wenn es wirklich schwer wird. Weil Resilienz kein Ziel ist, sondern eine tägliche Entscheidung.'),
    ('Verantwortung', '⚡', '#3DA5FF', 'KI und digitale Werkzeuge verstehen und nutzen, statt abgehängt zu werden.',
     'Die Welt verändert sich schneller als je zuvor. Wir zeigen dir, wie du die neuen Werkzeuge für dich und deine Familie nutzt – statt dich von ihnen überwältigen zu lassen.'),
]
saeulen_html = ''.join(
    f'\n  <section class="saeule-section" style="--akzent:{farbe}" aria-labelledby="saeule-{n}">'
    f'\n    <div class="saeule-visual" data-reveal><div class="saeule-icon" aria-hidden="true">{icon}</div></div>'
    f'\n    <div class="saeule-text" data-reveal data-reveal-delay="120"><span class="saeule-label">Säule {n + 1:02d} · {name}</span>'
    f'<h2 id="saeule-{n}">{head}</h2><p>{txt}</p></div>\n  </section>'
    for n, (name, icon, farbe, head, txt) in enumerate(SAEULEN))

# ═══ Väter-App (Handy in der Mitte, Features strahlen per Linie aus · Handy-Bildschirm: Karten) ═══
APP_BADGES = [  # (Platz für die Linien, CSS-Position, Emoji, Titel) – 2 links, 2 rechts, 1 unten Mitte
    ('links', 'badge-top-left', '⚖️', 'Rechtliche Orientierung'),
    ('links', 'badge-mid-left', '👥', 'Väter-Community'),
    ('rechts', 'badge-top-right', '👨‍⚖️', 'Fachliche Kontakte'),
    ('rechts', 'badge-mid-right', '🏋️', 'Sport &amp; Events'),
    ('unten', 'badge-bottom-center', '📅', 'Kalender &amp; Kinderzeit'),
]
KETTE = '<svg class="kette-linie" aria-hidden="true"><line class="app-bahn" x1="50%" y1="0" x2="50%" y2="100%"/><line class="app-strom" x1="50%" y1="0" x2="50%" y2="100%"/></svg>'
BADGE_INFO = {  # Pop-up je Badge: (Modal-ID, Text, Vorteil)
    'Rechtliche Orientierung': ('badge-recht',
        'Obsorge, Besuchsrecht, Unterhalt – endlich in verständlicher Sprache erklärt. Kein Juristendeutsch, kein Eigeninteresse. Du bekommst klare Informationen, damit du in Gesprächen mit Anwälten und vor Gericht vorbereitet bist.',
        'Du weißt, welche Rechte du als Vater hast – bevor du zum ersten Mal vor dem Richter sitzt.'),
    'Väter-Community': ('badge-community',
        'Männer, die verstehen, was du durchmachst – ohne Mitleid, ohne Urteil. In der #LeKo Community findest du echte Väter in ähnlichen Situationen. Direkter Austausch, gegenseitige Unterstützung, keine Performance.',
        'Du bist nicht mehr allein mit dem, was dich nachts wachhält.'),
    'Kalender &amp; Kinderzeit': ('badge-kalender',
        'Deine Zeit mit den Kindern dokumentieren und planen – strukturiert und nachvollziehbar. Halte fest, wann du deine Kinder siehst, und behalte den Überblick über Übergaben, Termine und besondere Momente.',
        'Im Zweifelsfall hast du schwarz auf weiß, wie viel Zeit du wirklich mit deinen Kindern verbracht hast.'),
    'Fachliche Kontakte': ('badge-kontakte',
        'Experten aus unserem Netzwerk, die auf die Situation von Trennungsvätern spezialisiert sind: Familienanwälte, Mediatoren, Psychologen. Kein Rätselraten, wem du vertrauen kannst.',
        'Du sparst Zeit, Geld und Nerven – weil du sofort den richtigen Ansprechpartner findest.'),
    'Sport &amp; Events': ('badge-sport',
        'Gemeinsam aktiv sein – Stammtische, Sport-Challenges, Ausflüge und Events mit anderen Vätern. Raus aus der Wohnung, rein ins Leben. Bewegung als Ventil und Gemeinschaft als Kraftquelle.',
        'Du baust echte Verbindungen auf – nicht nur online, sondern im echten Leben.'),
}
badge_dialoge = ''.join(f'''
<dialog class="modal" id="{BADGE_INFO[h][0]}" aria-labelledby="{BADGE_INFO[h][0]}-titel">
  <button class="schliessen" type="button" data-schliessen aria-label="Schließen">×</button>
  <div class="modal-innen">
    <p class="eyebrow">{e} Feature</p>
    <h2 id="{BADGE_INFO[h][0]}-titel">{h}</h2>
    <p>{BADGE_INFO[h][1]}</p>
    <p class="modal-vorteil">Dein Vorteil: {BADGE_INFO[h][2]}</p>
  </div>
</dialog>
''' for _, _, e, h in sorted(APP_BADGES, key=lambda b: list(BADGE_INFO).index(b[3])))
app_badges = ''.join(f'\n      <li class="app-badge {pos}" data-platz="{s}" data-reveal data-modal="{BADGE_INFO[h][0]}" tabindex="0" role="button" aria-haspopup="dialog">{KETTE}<span class="ab-icon" aria-hidden="true">{e}</span>{h}</li>'
                     for s, pos, e, h in APP_BADGES)  # KETTE: senkrechte Linie nach oben, nur auf dem Handy sichtbar

# ═══ Haltung (2×2) ═══
I.update({
    'h_herz':      '<path d="M12 10.2c-1.3-1.8-4.3-1.5-4.3.9 0 1.8 2.3 3.4 4.3 4.7 2-1.3 4.3-2.9 4.3-4.7 0-2.4-3-2.7-4.3-.9z"/><path d="M2.5 15.5l3.3-.6a4 4 0 0 1 3 .7l1.5 1.1h3.5a1.3 1.3 0 0 1 0 2.6H10"/><path d="M2.5 21.5h9.2l6.9-3.8a1.4 1.4 0 0 0-1.3-2.5l-3.4 1.6"/>',
    'h_richtung':  '<circle cx="12" cy="12" r="9.5"/><path d="M15.8 8.2l-2.3 5.3-5.3 2.3 2.3-5.3z"/><path d="M12 2.5v2M12 19.5v2M2.5 12h2M19.5 12h2"/>',
    'h_wegweiser': '<path d="M12 2.5v19M8.5 21.5h7"/><path d="M12 5h6.5l2.5 2.5-2.5 2.5H12"/><path d="M12 12.5H5.5L3 15l2.5 2.5H12"/>',
})
HALTUNG = [
    ('h_herz', 'Gemeinnützig', 'Wir arbeiten nicht für Profit. Für Menschen.'),
    ('leute', 'Respekt ohne Urteil', 'Kein Raum für Urteile, Verurteilung oder Überlegenheit.'),
    ('h_richtung', 'Unabhängig', 'Keine Finanzierung durch staatliche Institutionen.'),
    ('h_wegweiser', 'Kein Therapie-Ersatz', 'Wir sind Gemeinschaft, keine Therapeuten. Profis empfehlen wir immer gerne weiter.'),
]
haltung_html = ''.join(
    f'\n      <div data-reveal data-reveal-delay="{n * 100}"><article class="haltung-karte">'
    f'<div class="hk-icon" aria-hidden="true">{ico(I[k], "1.2")}</div><h3>{h}</h3><p>{txt}</p></article></div>'
    for n, (k, h, txt) in enumerate(HALTUNG))

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
    links = [('saeulen', 'Säulen'), ('app', 'Väter-App'), ('haltung', 'Haltung'), ('faq', 'FAQ'), ('mitglied', 'Kontakt')]
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
    <span>© <span data-jahr>2026</span> Lebenskompass – ZVR 1346040358</span>
    <nav aria-label="Rechtliches"><button type="button" data-modal="impressum">Impressum</button><span aria-hidden="true">·</span>{ds_link}</nav>
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
INDEX_JS = (HIER / 'index.js').read_text()

index = f'''<!DOCTYPE html>
<html lang="de-AT">
<head>
{KOPF_META}
<title>LeKo – Lebenskompass | Männer-Community Österreich &amp; Deutschland</title>
<meta name="description" content="LeKo ist die Gemeinschaft für Männer zwischen 25 und 50, die Orientierung, Stärke und echte Verbindung suchen – als Väter, als Persönlichkeit, als Teil einer Community, die hält was sie verspricht. Österreich und Deutschland.">
<meta name="robots" content="index, follow">
<link rel="canonical" href="https://prinz03.github.io/leko-website/">
<meta property="og:title" content="LeKo – Stärker werden. Nicht allein.">
<meta property="og:description" content="Männer-Community für Orientierung, Gemeinschaft und Stärke. Überall in Österreich und Deutschland.">
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

<!-- ═══ 1 · HERO (ruhig: nur Text und Licht) ═══ -->
<section class="hero-outer" id="top">
  <div class="hero-inner">
    <div class="hero-licht" aria-hidden="true"></div>
    <div class="hero-text">
      <p class="hero-pre auftritt" style="--d:.3s">Für Männer. Ohne Ausrede.</p>
      <h1 class="hero-h1">
        <span class="h1-weiss auftritt" style="--d:.55s">Stärker werden.</span>
        <span class="h1-gold auftritt" style="--d:.85s">Nicht allein.</span>
      </h1>
      <p class="hero-sub auftritt" style="--d:1.1s">LeKo ist die Community für Männer, die ihr Leben selbst in die Hand nehmen – als Väter, als Persönlichkeiten, als Teil einer Gemeinschaft, die hält was sie verspricht.</p>
      <div class="hero-ctas auftritt" style="--d:1.25s">
        <a href="#mitglied" class="btn btn-gold btn-gross">Jetzt Mitglied werden <span class="pfeil" aria-hidden="true">→</span></a>
      </div>
    </div>
  </div>
</section>

<!-- ═══ 2 · KENNST DU DAS? (wie ein Freund, nicht wie Marketing) ═══ -->
<section class="mirror-section" id="problem" aria-labelledby="mirror-titel">
  <h2 class="mirror-label" id="mirror-titel" data-reveal>Kennst du das?</h2>{spiegel_html}
  <p class="mirror-bridge" data-reveal>Dann bist du hier richtig.</p>
</section>

<!-- ═══ 3 · 5 SÄULEN (Full-Screen-Feature-Sektionen) ═══ -->
<div class="saeulen" id="saeulen">
  <header class="saeulen-intro wrap" data-reveal>
    <p class="eyebrow-gold">Die 5 Säulen von #LeKo</p>
    <h2>Jede Säule trägt. <em>Gemeinsam tragen wir dich.</em></h2>
  </header>
  <div class="saeulen-liste">{saeulen_html}
  </div>
</div>

<!-- ═══ 4 · VÄTER-APP (Handy mit echtem App-Screen, Features per Strom-Linie verbunden) ═══ -->
<section class="app" id="app" aria-labelledby="app-titel">
  <div class="wrap app-kopf" data-reveal>
    <p class="eyebrow-gold">Die #LeKo Väter-App</p>
    <h2 id="app-titel">Die App für Väter<br>in Trennung.<br><em>Dokumentieren. Vernetzt. Nie allein.</em></h2>
    <span class="badge">Bald verfügbar</span>
  </div>
  <div class="app-buehne" id="app-buehne">
    <svg class="app-linien" id="app-linien" aria-hidden="true"></svg>
    <ul class="app-badges" aria-label="Funktionen der App">{app_badges}
    </ul>
    <div class="app-geraet" id="app-geraet">
      <img class="app-mockup" src="assets/img/iphone-mockup.png" width="603" height="1200" alt="" loading="lazy" decoding="async">
      <video class="app-screen-bild" autoplay loop muted playsinline src="assets/video/kompass-demo.mp4" aria-label="Demo der KOMPASS-App"></video>
      <span class="app-koerper" id="app-koerper" aria-hidden="true"></span>
    </div>
  </div>
</section>

<!-- ═══ 5 · HALTUNG (2×2) ═══ -->
<section class="haltung" id="haltung" aria-labelledby="haltung-titel">
  <div class="wrap">
    <header class="haltung-kopf" data-reveal>
      <h2 id="haltung-titel">Unsere Haltung</h2>
      <p class="lead">Was uns trägt — und was uns unterscheidet.</p>
    </header>
    <div class="haltung-grid">{haltung_html}
    </div>
  </div>
</section>

<!-- ═══ 6 · FAQ ═══ -->
<section class="faq" id="faq" aria-labelledby="faq-titel">
  <div class="wrap schmal">
    <header class="faq-kopf" data-reveal>
      <p class="eyebrow-gold">Fragen</p>
      <h2 id="faq-titel">Ehrliche <em>Antworten.</em></h2>
    </header>
    <div class="akk" data-reveal>{faq_html}
    </div>
  </div>
</section>

<!-- ═══ 7 · CTA ═══ -->
<section class="cta" id="mitglied" aria-labelledby="cta-titel">
  <div class="wrap cta-inner" data-reveal>
    <h2 id="cta-titel">Bereit, den nächsten Schritt <em>zu gehen?</em></h2>
    <p class="lead">LeKo ist kein Verein für später. LeKo ist für jetzt.</p>
    <a href="mailto:leko.verein@gmail.com?subject=Mitgliedschaft%20%23LeKo" class="btn btn-gold btn-gross">Jetzt Mitglied werden <span class="pfeil" aria-hidden="true">→</span></a>
    <p class="cta-klein"><a href="mailto:leko.verein@gmail.com">leko.verein@gmail.com</a></p>
  </div>
</section>

</main>

{fuss('<a href="datenschutz.html" target="_blank" rel="noopener">Datenschutz</a>')}
{badge_dialoge}
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
.ds h1 em{{font-style:normal;background:var(--gold-verlauf);-webkit-background-clip:text;background-clip:text;color:transparent}}
.ds .lead{{margin-bottom:40px}}
.privacy{{color:var(--text-2);font-size:1rem}}
.privacy h3{{color:var(--white);font-size:1.35rem;margin:40px 0 10px;padding-top:24px;border-top:1px solid var(--linie)}}
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
