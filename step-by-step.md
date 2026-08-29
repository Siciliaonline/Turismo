# Sizilien Tourismus Führer - Dokumentation mit Sphinx und GitHub Pages (29.Aug.26.v1)

#### Guide:

- https://www.sphinx-doc.org/en/master/
- https://sphinx-rtd-theme.readthedocs.io/en/stable/

**Vergleichbare Beispiele:**

- https://docs.sunfounder.com/en/latest/ 
- https://docs.ros.org/en/humble/index.html

**Tutorial:**

- https://www.youtube.com/watch?v=wPzC1ZTVoJY

---

Diese Anleitung beschreibt, wie du eine Tourismus-Dokumentationswebseite über Sizilien mit dem Sphinx-Layout Read the Docs erstellst, die Quelldateien in GitHub verwaltest und die fertige HTML-Seite kostenlos über GitHub Pages veröffentlichst.

Die Anleitung ist für Windows, Linux und macOS geeignet. Die Befehle funktionieren überwiegend in PowerShell, Windows Terminal oder einer Unix-Shell.

## 1. Ziel und Ergebnis

Am Ende besitzt du:

- ein GitHub-Repository mit deinen Dokumentationsquellen,
- eine Sphinx-Projektstruktur für Sizilien,
- das Layout `sphinx_rtd_theme` mit Provinz-Navigation,
- Markdown-Unterstützung über `myst-parser`,
- Kapitel für alle 9 sizilianischen Provinzen (Agrigento, Caltanissetta, Catania, Enna, Messina, Palermo, Ragusa, Siracusa, Trapani),
- Attraktionen, Gastronomie und Events pro Stadt,
- Bilder und Download-Dateien,
- einen automatischen GitHub-Actions-Workflow,
- eine kostenlose Webseite unter einer GitHub-Pages-Adresse.

Die Adresse hat typischerweise dieses Format:

```text
https://DEIN-BENUTZERNAME.github.io/turismo/
```

Eine eigene Domain ist nicht erforderlich.

## 2. Benötigte Software

Installiere zunächst:

1. Git: https://git-scm.com/downloads
2. Python 3: https://www.python.org/downloads/
3. Einen Editor, zum Beispiel Visual Studio Code: https://code.visualstudio.com/
4. Ein GitHub-Konto: https://github.com/

Prüfe die Installation:

```bash
git --version
python --version
```

Auf manchen Linux-Systemen lautet der Python-Befehl `python3`:

```bash
python3 --version
```

Unter Windows sollte Python beim Installieren mit der Option `Add Python to PATH` zum Suchpfad hinzugefügt werden.

## 3. GitHub-Repository erstellen

Melde dich bei GitHub an und erstelle ein neues Repository.

Beispiel:

```text
Name: turismo
Sichtbarkeit: Public
README: optional
.gitignore: Python
Lizenz: nach Bedarf
```

Für ein öffentliches Tourismus-Handbuch ist `Public` die beste Wahl. Kopiere die HTTPS-Adresse des Repositorys. Sie sieht ungefähr so aus:

```text
https://github.com/DEIN-BENUTZERNAME/turismo.git
```

## 4. Lokales Arbeitsverzeichnis erstellen

Erstelle einen Ordner und klone das Repository:

```bash
git clone https://github.com/DEIN-BENUTZERNAME/turismo.git
cd turismo
```

Wenn das Repository leer ist, kannst du auch direkt in einem neuen Ordner arbeiten:

```bash
mkdir turismo
cd turismo
git init
git branch -M main
git remote add origin https://github.com/DEIN-BENUTZERNAME/turismo.git
```

## 5. Python-virtuelle Umgebung einrichten

Eine virtuelle Umgebung verhindert, dass die Sphinx-Pakete andere Python-Projekte beeinflussen.

### Windows PowerShell

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

Falls PowerShell die Aktivierung blockiert, kann einmalig folgender Befehl erforderlich sein:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

Danach erneut:

```powershell
.venv\Scripts\Activate.ps1
```

### Windows Eingabeaufforderung

```bat
python -m venv .venv
.venv\Scripts\activate.bat
```

### Linux oder macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Eine aktivierte Umgebung ist meistens an `(.venv)` am Anfang der Eingabezeile zu erkennen.

## 6. Sphinx und Erweiterungen installieren

Installiere Sphinx, das Read-the-Docs-Theme und den Markdown-Parser:

```bash
python -m pip install --upgrade pip
python -m pip install sphinx sphinx-rtd-theme myst-parser
```

Für eine reproduzierbare Umgebung speicherst du die Pakete:

```bash
mkdir docs
python -m pip freeze > docs/requirements.txt
```

Eine bewusst minimale `docs/requirements.txt` ist meist übersichtlicher:

```text
sphinx
sphinx-rtd-theme
myst-parser
```

## 7. Sphinx-Projekt erzeugen

Erstelle ein Sphinx-Projekt im Ordner `docs`:

```bash
sphinx-quickstart docs
```

Beantworte die Fragen beispielsweise so:

```text
Separate source and build directories: yes
Project name: Sizilien Tourismus Führer
Author name: Dein Name
Project release: 1.0
Project language: de
```

Bei einer getrennten Struktur liegen die Quellen danach normalerweise unter:

```text
docs/source/
```

und die erzeugten Dateien unter:

```text
docs/build/
```

## 8. Empfohlene technische Struktur

Eine sinnvolle Struktur für die Sizilien-Dokumentation mit allen 9 Provinzen ist:

```text
turismo/
│
├── .github/
│   └── workflows/
│       └── sphinx.yml
│
├── docs/
│   ├── requirements.txt
│   ├── Makefile
│   ├── make.bat
│   │
│   ├── source/
│   │   ├── conf.py
│   │   ├── index.rst
│   │   │
│   │   ├── _static/
│   │   │   ├── custom.css
│   │   │   └── images/
│   │   │       ├── agrigento/
│   │   │       ├── caltanissetta/
│   │   │       ├── catania/
│   │   │       ├── enna/
│   │   │       ├── messina/
│   │   │       ├── palermo/
│   │   │       ├── ragusa/
│   │   │       ├── siracusa/
│   │   │       └── trapani/
│   │   │
│   │   ├── _templates/
│   │   │
│   │   ├── downloads/
│   │   │   └── karten/ (optional)
│   │   │
│   │   ├── provinzen/
│   │   │   ├── agrigento/
│   │   │   │   ├── index.rst
│   │   │   │   ├── agrigento-stadt.md
│   │   │   │   ├── mondello.md
│   │   │   │   ├── porto-empedocle.md
│   │   │   │   ├── sciacca.md
│   │   │   │   └── weitere_orte.md
│   │   │   │
│   │   │   ├── caltanissetta/
│   │   │   │   └── index.rst (Placeholder)
│   │   │   │
│   │   │   ├── catania/
│   │   │   │   └── index.rst (Placeholder)
│   │   │   │
│   │   │   ├── enna/
│   │   │   │   └── index.rst (Placeholder)
│   │   │   │
│   │   │   ├── messina/
│   │   │   │   └── index.rst (Placeholder)
│   │   │   │
│   │   │   ├── palermo/
│   │   │   │   └── index.rst (Placeholder)
│   │   │   │
│   │   │   ├── ragusa/
│   │   │   │   └── index.rst (Placeholder)
│   │   │   │
│   │   │   ├── siracusa/
│   │   │   │   └── index.rst (Placeholder)
│   │   │   │
│   │   │   └── trapani/
│   │   │       └── index.rst (Placeholder)
│   │   │
│   │   └── events/
│   │       └── jahreskalender.md
│   │
│   └── build/
│       └── html/
│
├── .gitignore
├── README.md
└── LICENSE
```

Der Ordner `docs/build/` enthält generierte Dateien und wird nicht in GitHub gespeichert. Die Quelldateien befinden sich in `docs/source/`.

## 9. Konfiguration in conf.py

Öffne:

```text
docs/source/conf.py
```

Verwende folgende Konfiguration für das Turismo-Projekt:

```python
from datetime import datetime

project = "Sizilien Tourismus Führer"
author = "Dein Name"
year = datetime.now().year
copyright = f"{year}, {author}"
release = "1.0"

extensions = [
    "myst_parser",
]

templates_path = ["_templates"]
exclude_patterns = []

language = "de"

html_theme = "sphinx_rtd_theme"
html_title = "Sizilien Tourismus Führer"
html_static_path = ["_static"]
# html_logo = "_static/images/logo.png"  # Später hinzufügen
# html_favicon = "_static/images/favicon.ico"  # Später hinzufügen

html_theme_options = {
    "navigation_depth": 3,
    "collapse_navigation": False,
    "sticky_navigation": True,
    "includehidden": True,
}

html_css_files = [
    "custom.css",
]
```

Die `navigation_depth: 3` ermöglicht es, Provinzen und ihre Sub-Seiten (Städte) in der Navigation anzuzeigen.

## 10. Startseite mit reStructuredText

Öffne:

```text
docs/source/index.rst
```

Ersetze den Inhalt durch:

```rst
Sizilien Tourismus Führer
=========================

Willkommen zum umfassenden Tourismus-Handbuch für die italienische Insel Sizilien.

Diese Webseite dokumentiert die neun Provinzen und ihre wichtigsten Städte, 
Sehenswürdigkeiten, lokale Gastronomie und regionale Veranstaltungen.

.. note::

   Die Dokumentation wird kontinuierlich erweitert. Die Provinz Agrigento ist 
   derzeit vollständig dokumentiert. Weitere Provinzen werden in Kürze hinzugefügt.

Provinzen Siziliens
-------------------

.. toctree::
   :maxdepth: 2
   :caption: Provinzen:

   provinzen/agrigento/index
   provinzen/caltanissetta/index
   provinzen/catania/index
   provinzen/enna/index
   provinzen/messina/index
   provinzen/palermo/index
   provinzen/ragusa/index
   provinzen/siracusa/index
   provinzen/trapani/index

Weitere Bereiche
----------------

.. toctree::
   :maxdepth: 1
   :caption: Zusätzlich:

   events/jahreskalender

* :ref:`genindex`
* :ref:`search`
```

## 11. Agrigento - Vollständig ausgearbeitete Provinz

Erstelle die Datei:

```text
docs/source/provinzen/agrigento/index.rst
```

Mit folgendem Inhalt:

```rst
Agrigento
=========

Die Provinz Agrigento liegt im Südwesten Siziliens und ist bekannt für das 
weltberühmte Tal der Tempel (Valle dei Templi), eines der bedeutendsten 
archäologischen Stätten des antiken Griechenlands außerhalb von Griechenland.

.. toctree::
   :maxdepth: 2

   agrigento-stadt
   mondello
   porto-empedocle
   sciacca
   weitere_orte

Überblick
---------

- **Hauptstadt:** Agrigento
- **Größte Sehenswürdigkeit:** Tal der Tempel (UNESCO-Weltkulturerbe)
- **Fläche:** 3.544 km²
- **Bevölkerung:** ca. 430.000 Einwohner
- **Klima:** Mediterran, heiße Sommer, milde Winter
```

Erstelle:

```text
docs/source/provinzen/agrigento/agrigento-stadt.md
```

```markdown
# Agrigento-Stadt

Agrigento ist die Hauptstadt der gleichnamigen Provinz und eine der ältesten Städte Europas.

## Überblick

Die Stadt liegt auf einem Hügel und bietet atemberaubende Ausblicke über das 
Tal der Tempel. Mit etwa 60.000 Einwohnern ist sie das Zentrum der Region.

## Tal der Tempel (Valle dei Templi)

Das Tal der Tempel ist die Hauptattraktion Agritentos und zählt zum 
UNESCO-Weltkulturerbe.

### Wichtigste Tempel

- **Tempel der Concordia** - einer der besterhaltenen griechischen Tempel
- **Tempel des Dioskuren** - auch als Tempel der Zwillinge bekannt
- **Tempel des Olympischen Zeus** - einst der größte Tempel der antiken Welt
- **Tempel der Hera** - östlichster Tempel der Anlage

### Öffnungszeiten

- täglich 8:30 - 19:00 Uhr
- Letzter Einlass: 18:00 Uhr

### Eintritt

- Erwachsene: ca. 10 EUR
- Ermäßigt: ca. 5 EUR

## Altstadt (Centro Storico)

Die Altstadt liegt oberhalb des Tempeltals und ist geprägt von barocken 
Kirchen und engen, verwundenen Gassen.

### Sehenswürdigkeiten

- **Kathedrale von San Gerlando** - monumentale Kirche im barocken Stil
- **Kirche von Santo Spirito** - gotische Architektur
- **Palazzo Politi** - prächtige Adelsvilla

## Lokale Gastronomie

Die sizilianische Küche Agritentos ist von arabischen, normannischen und 
italienischen Einflüssen geprägt.

### Typische Gerichte

- **Arancini** - gefüllte Reisbällchen
- **Pasta alla Norma** - Pasta mit Auberginen und Tomaten
- **Granita con Brioche** - Eissorbet mit süßlichem Brötchen (zum Frühstück)
- **Caponata** - süß-saure Gemüsemischung
- **Fritto Misto** - gemischte Fischspezialitäten

### Empfehlenswerte Restaurants

- [Restaurant-Name hinzufügen]
- [Restaurant-Name hinzufügen]

## Praktische Informationen

- **Anfahrt:** Bus, Auto oder Zugverbindung nach Agrigento-Zentrum
- **Beste Reisezeit:** April-Juni und September-Oktober
- **Sprache:** Italienisch, einige Englischsprachler in touristischen Bereichen
```

Erstelle:

```text
docs/source/provinzen/agrigento/mondello.md
```

```markdown
# Mondello

Mondello ist eine malerische Küstenstadt in der Provinz Agrigento mit 
wunderschönen Stränden und einer entspannten Atmosphäre.

## Überblick

Die Stadt liegt etwa 25 km südlich von Agrigento und ist bekannt für ihre 
traumhaften Sandstrände und das kristallklare Mittelmeer.

## Strände

### Spiaggia di Mondello

Der Hauptstrand erstreckt sich über mehrere Kilometer und bietet:
- Feiner, heller Sand
- Flaches, seichtes Wasser (ideal für Familien)
- Zahlreiche Strandlokale (Chiringuitos)
- Wassersportmöglichkeiten

### Weitere Strände

- **Spiaggia di Porto** - südlich des Hauptstrandes
- **Cala Bianca** - versteckter, weniger überlaufener Strand

## Wassersport

- Windsurfen
- Kitesurfen
- Schnorcheln
- Bootstouren

## Lokale Gastronomie

Die Küche Mondellos ist geprägt von frischen Meeresfrüchten.

- **Pasta al Riccio di Mare** - Pasta mit Seeigel
- **Fritto di Pesce** - gemischte Fischspezialitäten
- **Orata alla Griglia** - gegrillte Dorade

## Praktische Informationen

- **Anfahrt:** Auto oder lokale Busverbindungen
- **Beste Reisezeit:** Juni-September
- **Übernachtung:** Kleine Hotels und Ferienhäuser
```

Erstelle Platzhalter-Dateien:

```text
docs/source/provinzen/agrigento/porto-empedocle.md
docs/source/provinzen/agrigento/sciacca.md
docs/source/provinzen/agrigento/weitere_orte.md
```

```markdown
# [Ortname]

Weitere Informationen folgen in Kürze.
```

## 12. Platzhalter für weitere Provinzen

Erstelle für jede der verbleibenden 8 Provinzen eine Datei:

```text
docs/source/provinzen/[PROVINZ]/index.rst
```

Beispiel für Caltanissetta:

```rst
Caltanissetta
=============

Die Provinz Caltanissetta liegt im Herzen Siziliens.

.. note::

   Diese Provinz wird in Kürze vollständig dokumentiert. 
   Weitere Informationen folgen bald.

Coming Soon - Inhalt wird hinzugefügt.
```

Wiederhole dies für: caltanissetta, catania, enna, messina, palermo, ragusa, siracusa, trapani

## 13. Event-Kalender erstellen

Erstelle:

```text
docs/source/events/jahreskalender.md
```

```markdown
# Jahreskalender - Events und Veranstaltungen in Sizilien

Dieser Kalender zeigt die wichtigsten Veranstaltungen und Feste 
in den Provinzen Siziliens über das Jahr verteilt.

## Januar

### Epiphanie-Prozessionen
- **Provinz:** Palermo, Agrigento
- **Datum:** 6. Januar
- **Beschreibung:** Traditionelle Prozessionen mit historischen Kostümen

## Februar

### Karneval
- **Provinz:** Palermo, Messina
- **Datum:** Variiert (ca. 2 Wochen vor Ostern)
- **Beschreibung:** Bunte Umzüge mit Karnevalsgruppen und lokalen Masken

## März

### Ostern
- **Provinz:** Alle Provinzen
- **Datum:** Variiert
- **Beschreibung:** Religiöse Prozessionen und Messen

## April

### Blütenzeit
- **Provinz:** Agrigento, Ragusa
- **Datum:** Ganzmonatig
- **Beschreibung:** Wanderungen durch blühende Mandelbäume und Zitronenhaine

## Mai

### Festa di San Giorgio (Ragusa)
- **Provinz:** Ragusa
- **Datum:** 29. Mai
- **Beschreibung:** Spektakuläre Prozession mit dramatischen Treppen

## Juni bis September

### Sommerfeste und Konzerte
- **Provinz:** Alle Provinzen
- **Datum:** Variiert
- **Beschreibung:** Musik- und Kulturfestivals in Küstenstädten

## Oktober bis November

### Weinlese und Traubenfeste
- **Provinz:** Trapani, Agrigento
- **Datum:** Variiert
- **Beschreibung:** Traditionelle Ernte- und Weinfeste

## Dezember

### Weihnachtsmärkte
- **Provinz:** Alle größeren Städte
- **Datum:** Dezember
- **Beschreibung:** Traditionelle Weihnachtsmärkte und Dekoration

*Weitere regionale Feste werden bei der Fertigstellung der einzelnen Provinzen ergänzt.*
```

## 14. Lokalen HTML-Build durchführen

Aktiviere deine virtuelle Umgebung und führe aus:

```bash
sphinx-build -b html docs/source docs/build/html
```

Die fertige Startseite liegt anschließend hier:

```text
docs/build/html/index.html
```

Öffne sie direkt im Browser oder starte einen lokalen Server:

```bash
python -m http.server 8000 --directory docs/build/html
```

Öffne danach:

```text
http://localhost:8000
```

## 15. Sphinx-Warnungen kontrollieren

Während des Builds meldet Sphinx fehlende Seiten und andere Probleme:

```bash
sphinx-build -W -b html docs/source docs/build/html
```

`-W` behandelt Warnungen als Fehler.

## 16. `.gitignore` erstellen

Im Hauptverzeichnis:

```text
.venv/
__pycache__/
*.pyc
docs/build/
.vscode/
.idea/
.DS_Store
Thumbs.db
```

## 17. `README.md` erstellen

```markdown
# Sizilien Tourismus Führer

Dokumentation der neun Provinzen Siziliens mit Informationen zu Attraktionen, Gastronomie und Events.

## Status

- ✅ Agrigento: Vollständig
- ⏳ Weitere Provinzen: Geplant

## Lokal bauen

python -m pip install -r docs/requirements.txt
sphinx-build -b html docs/source docs/build/html
```

## 18. Dateien zu Git hinzufügen

```bash
git add .
git commit -m "Initiale Sphinx-Dokumentation für Sizilien Turismo"
git push -u origin main
```

## 19. GitHub Pages aktivieren

1. Repository Settings öffnen
2. Pages auswählen
3. Quelle auf "GitHub Actions" setzen

## 20. Checkliste

### Vorbereitung
- [ ] Git installiert
- [ ] Python installiert
- [ ] GitHub-Repository erstellt
- [ ] Virtuelle Umgebung erstellt

### Sphinx-Setup
- [ ] Sphinx installiert
- [ ] Theme und Parser installiert
- [ ] conf.py konfiguriert
- [ ] index.rst mit allen Provinzen

### Agrigento - Vollständig
- [ ] index.rst
- [ ] agrigento-stadt.md
- [ ] mondello.md
- [ ] Placeholder für weitere Orte

### Weitere Provinzen
- [ ] 8x Placeholder index.rst

### Veröffentlichung
- [ ] .gitignore
- [ ] README.md
- [ ] GitHub-Actions-Workflow
- [ ] GitHub Pages aktiviert
- [ ] Webseite online
