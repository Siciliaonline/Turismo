# Anleitung: Inhalte zur Tourismo-Dokumentation hinzufügen

## Webseite pflegen und erweitern

Die Dokumentationsseiten werden in `docs/source/` gepflegt. Der Ordner `docs/build/` enthält automatisch erzeugte HTML-Dateien und sollte nicht manuell bearbeitet werden.

## Bestehende Seite ändern

Öffne die passende Quelldatei, zum Beispiel:

```text
docs/source/provinzen/agrigento/agrigento-stadt.md
```

Bearbeite den Inhalt in Markdown und baue die Webseite lokal:

```bash
source .venv/bin/activate
make -C docs html-all
```

Starte einen lokalen Server zur Vorschau:

```bash
python -m http.server 8000 --directory docs/build/html
```

Öffne dann `http://localhost:8000` im Browser.

## Eine neue Stadt zu Agrigento hinzufügen

Beispiel: Du möchtest die Stadt "Sciacca" ausarbeiten.

1. **Erstelle die Markdown-Datei:**

```text
docs/source/provinzen/agrigento/sciacca.md
```

2. **Schreibe den Inhalt mit Struktur:**

```markdown
# Sciacca

Kurzbeschreibung der Stadt.

## Überblick

Allgemeine Informationen.

## Sehenswürdigkeiten

- Attraktion 1
- Attraktion 2

## Lokale Gastronomie

- Gericht 1
- Gericht 2

## Praktische Informationen

- Anfahrt
- Beste Reisezeit
```

3. **Registriere die neue Seite in der Navigation:**

Öffne `docs/source/provinzen/agrigento/index.rst` und ergänze:

```rst
.. toctree::
   :maxdepth: 2

   agrigento-stadt
   mondello
   sciacca
```

4. **Baue die Dokumentation lokal:**

```bash
make -C docs html-all
```

Die neue Seite sollte jetzt in der Navigation sichtbar sein.

## Eine neue Provinz mit Platzhaltern starten

Um eine neue Provinz wie Palermo vorzubereiten:

1. **Erstelle den Ordner:**

```text
docs/source/provinzen/palermo/
```

2. **Erstelle index.rst:**

```rst
Palermo
=======

Die Provinz Palermo ist die bevölkerungsreichste Siziliens und kulturelles Zentrum der Insel.

.. note::

   Diese Provinz wird derzeit dokumentiert. Weitere Informationen folgen bald.

.. toctree::
   :maxdepth: 2

   palermo-stadt
```

3. **Erstelle erste Seite mit Platzhalter:**

```text
docs/source/provinzen/palermo/palermo-stadt.md
```

```markdown
# Palermo-Stadt

Weitere Informationen folgen in Kürze.
```

## Bilder hinzufügen

1. Lege Bilder nach Provinz ab:

```text
docs/source/_static/images/agrigento/
docs/source/_static/images/palermo/
```

2. Binde Bilder in Markdown ein:

```markdown
![Tal der Tempel](_static/images/agrigento/tempeltale.jpg)

*Bildunterschrift mit Kontext*
```

## Veranstaltungen zum Jahreskalender hinzufügen

Öffne `docs/source/events/jahreskalender.md` und ergänze Events:

```markdown
## Juli

### Volksfest XY
- **Provinz:** Palermo
- **Datum:** 15. Juli
- **Beschreibung:** Traditionelles Sommerfest mit Musik und Tanz
```

## Wichtige Regeln

- **Dateinamen:** Keine Umlaute oder Leerzeichen (z.B. `agrigento-stadt.md`, nicht `Agrigento Stadt.md`)
- **Groß-/Kleinschreibung:** Konsistent halten, besonders in `toctree` Einträgen
- **Markdown vs. reStructuredText:** 
  - Inhalte: `.md` (Markdown)
  - Navigation: `.rst` (reStructuredText)
- **Links:** Relativ zu `docs/source/` verwenden

## Änderungen veröffentlichen

```bash
git add docs/source
git commit -m "Agrigento: Sciacca-Seite hinzugefügt"
git push origin main
```

Der GitHub-Actions-Workflow baut automatisch die Webseite neu und veröffentlicht sie auf GitHub Pages.

## Fehlersuche

### Seite nicht in Navigation sichtbar

- Prüfe, dass der Dateiname in `toctree` korrekt ist
- Achte auf Groß-/Kleinschreibung
- Stelle sicher, dass die Datei existiert

### Bilder nicht angezeigt

- Bilder müssen in `docs/source/_static/images/` liegen
- Pfad im Markdown muss relativ sein: `_static/images/agrigento/bild.jpg`
- Dateinamen dürfen keine Leerzeichen enthalten

### Build schlägt fehl

```bash
make -C docs html-all SPHINXOPTS=-W
```

Die `-W` Option behandelt Warnungen als Fehler und zeigt problematische Links.
