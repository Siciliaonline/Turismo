# Sizilien Tourismus Führer

Umfassende Dokumentation der neun Provinzen Siziliens mit Informationen zu Sehenswürdigkeiten, Gastronomie und Veranstaltungen.

Die veröffentlichte Dokumentation ist über GitHub Pages erreichbar.

## Status

- ✅ Agrigento: Vollständig dokumentiert
- ⏳ Caltanissetta, Catania, Enna, Messina, Palermo, Ragusa, Siracusa, Trapani: In Planung

## Provinzen

1. **Agrigento** - Tal der Tempel und antike Stätten
2. **Caltanissetta** - Zentrum Siziliens
3. **Catania** - Lavalandschaften des Ätna
4. **Enna** - Bergregion mit mittelalterlichen Städten
5. **Messina** - Straße zwischen Sizilien und Kalabrien
6. **Palermo** - Hauptstadt und kulturelles Zentrum
7. **Ragusa** - Barocke Architektur und UNESCO-Stätten
8. **Siracusa** - Antike griechische Kolonien
9. **Trapani** - Salzgärten und westliche Küste

## Lokal bauen

Virtuelle Umgebung aktivieren und Abhängigkeiten installieren:

```bash
source .venv/bin/activate
python -m pip install -r docs/requirements.txt
```

HTML-Dokumentation erzeugen (Italienisch als Standardsprache):

```bash
make -C docs html-all
```

Lokalen Webserver starten:

```bash
python -m http.server 8000 --directory docs/build/html
```

Die Dokumentation ist dann unter `http://localhost:8000` erreichbar. Die
Sprachen liegen unter `/` (Italiano), `/en/` (English) und `/de/` (Deutsch).
