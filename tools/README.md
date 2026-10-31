# tools/ – Generator für die #LeKo-Website

`index.html` und `datenschutz.html` werden aus diesen Dateien erzeugt – **nicht direkt in den HTML-Dateien ändern**, sonst geht die Änderung beim nächsten Bauen verloren.

| Datei | Inhalt |
|---|---|
| `seiten_bauen.py` | Seitenaufbau, Texte, berechnete Geometrie (Kompass-Striche, Säulen-Fünfeck) |
| `index.css` | Gestaltung nur der Startseite (wird inline eingesetzt) |
| `index.js` | Skript nur der Startseite (Scroll-Kompass, Sticky Cards, Säulen-Panel, App-Linien) |
| `datenschutz-inhalt.html` | Text der Datenschutzerklärung |

Gemeinsames für beide Seiten liegt in `assets/site.css`, `assets/site.js` und `assets/fonts/fonts.css` und wird direkt bearbeitet.

## Bauen

```bash
python3 tools/seiten_bauen.py
```

Nur Python 3, keine weiteren Pakete. Danach die Seite im Browser prüfen, dann committen.

🤖 Erstellt mit KI-Unterstützung | LeKo Vereins-Jarvis
