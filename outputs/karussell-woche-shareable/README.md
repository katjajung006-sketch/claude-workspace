# Karussell-Woche — teilbarer Skill für Claude Code

Ein Slash-Command für Claude Code, der eine **komplette Wochenladung Instagram-Karussells** produziert: 7 Karussells, je 7–9 Slides, als **editierbare Canva-Designs**, jeweils mit Caption als Kommentar am Design.

Diese Version ist anonymisiert — überall, wo `[...]` steht, trägst du deine eigenen Werte ein. Das Design (Foto-Cover → ruhige Text-Slides mit grosser Zahl → Foto-Schluss) ist als funktionierende Vorlage dabei; Farben und Schriften kannst du anpassen.

---

## Wie es funktioniert (Kurzfassung)

1. Claude wählt 7 Themen für deine Zielgruppe und schreibt die Texte in deiner Stimme.
2. Ein Python-Skript rendert jedes Karussell als **mehrseitiges PDF mit echtem Text** (Headless-Chrome).
3. Die PDFs werden kurz öffentlich gehostet (Cloudflare Pages o. Ä.).
4. Claude importiert jedes PDF über den **Canva-MCP** als editierbares Design, legt es in einen Ordner und hängt die Caption als Kommentar dran.
5. Temporäres Hosting wird wieder gelöscht.

Der „Trick" dabei: Canva kann PDFs als **bearbeitbare** Designs importieren (Text bleibt Text). Das Foto wird mit seinem Verlauf zu *einem* flachen Bild „gebacken", damit Canva es beim Import nicht verdeckt.

---

## Voraussetzungen

| Was | Wofür | Hinweis |
|---|---|---|
| **Claude Code** | führt den Command aus | Desktop/CLI/IDE |
| **Python 3** | Rendering-Skripte | keine externen Pakete nötig |
| **Google Chrome** | Headless-Rendering (PNG/PDF) | Pfad ggf. in den Skripten anpassen |
| **Canva-MCP** in Claude Code verbunden | Import/Ablage/Kommentar | siehe Canva-MCP-Doku |
| **Cloudflare-Account + `wrangler`** | PDFs kurz öffentlich hosten | oder ein anderer öffentlicher HTTPS-Host |
| **Eigenes Foto** | Cover-/Schluss-Slide | als `photo.jpg` |

> Kein Cloudflare? Jeder Dienst geht, der die PDFs unter einer öffentlichen `https://.../<slug>.pdf`-URL ausliefert. Canvas `import-design-from-url` braucht nur die erreichbare Datei.

---

## Einrichten (einmalig)

1. **Command installieren**
   `command/karussell-woche.md` in deinen Claude-Code-Command-Ordner kopieren:
   - projektweit: `<dein-projekt>/.claude/commands/karussell-woche.md`
   - oder global: `~/.claude/commands/karussell-woche.md`
   Danach steht `/karussell-woche` zur Verfügung.

2. **Skripte ablegen**
   Den Ordner `scripts/karussell/` so in dein Projekt übernehmen, dass die Pfade im Command passen (Standard: `scripts/karussell/`). Wenn du sie woanders hinlegst, die Pfade in `karussell-woche.md` entsprechend ändern.

3. **Foto hinterlegen**
   Dein Hochformat-Foto als `scripts/karussell/photo.jpg` ablegen, dann einmal:
   ```bash
   python3 scripts/karussell/bake_photo.py
   ```
   Das erzeugt `cover_bg.png` und `close_bg.png`. (Die Platzhalter-Datei `photo.PLATZHALTER.txt` kannst du danach löschen.)

4. **`build.py` anpassen** (oben im Datei-Kopf):
   - `HANDLE` = dein Instagram-Name.
   - `PILLAR_A` / `PILLAR_B` = deine Content-Säulen.
   - `CHROME` = Chrome-Pfad, falls nicht macOS.
   - optional Farben/Schriften im `HEAD`-Block.

5. **Platzhalter im Command füllen** — in `karussell-woche.md`:
   - `[@DEINHANDLE]`, `[DEINE NISCHE]`, `[DEINE VERBOTENEN WÖRTER]`, `[DEINE STAMM-HASHTAGS]`
   - `[PFAD-ZU-DEINEN-KONTEXT-DATEIEN]` — deine Zielgruppen-/Brand-Voice-Notizen
   - `[DEIN-CANVA-ZIELORDNER-ID]` — Canva-Ordner-ID, in den die Designs gelegt werden
   - `[DEIN-CLOUDFLARE-TEMP-PROJEKT]` — Name eines Wegwerf-Cloudflare-Projekts
   - `[DEIN-BRAND-KIT-ID]` — optional

6. **Secrets lokal halten**
   Cloudflare-Token + Account-ID nur in einer lokalen, **gitignorierten** Datei oder als Umgebungsvariable. Nie committen.

---

## Benutzen

In Claude Code:
```
/karussell-woche
```
Claude arbeitet die Schritte aus `karussell-woche.md` ab: Themen wählen → Texte schreiben → `build_pdf.py` → hosten → 7× nach Canva importieren → ablegen → Captions als Kommentar → aufräumen → kurze Abschluss-Meldung.

Manuell testen (ohne Claude), nur das Rendering:
```bash
python3 scripts/karussell/build.py       # PNG-Vorschau je Slide
python3 scripts/karussell/build_pdf.py   # editierbare PDFs in scripts/karussell/_pdf/
```

---

## Dateien in diesem Bundle

```
karussell-woche-shareable/
├── README.md                         ← diese Datei
├── command/
│   └── karussell-woche.md            ← der Slash-Command (→ .claude/commands/)
└── scripts/karussell/
    ├── build.py                      ← Inhalt (CAROUSELS) + PNG-Vorschau-Renderer
    ├── build_pdf.py                  ← editierbare PDFs fürs Canva-Import
    ├── bake_photo.py                 ← Foto + Verlauf zu cover_bg/close_bg backen
    ├── KARUSSELLS.md                 ← Captions-Vorlage
    └── photo.PLATZHALTER.txt         ← Hinweis: hier dein photo.jpg ablegen
```

---

## Anpassen

- **Anderer Look:** Farben (`--sand`, `--cream`, `--clay`, `--espresso`) und Schriften (Google-Fonts-Link) stehen im `HEAD`-Block von `build.py` **und** `build_pdf.py` — an beiden Stellen gleich halten. Verlauf-Werte zusätzlich in `bake_photo.py`.
- **Anderes Format:** Slide-Grösse `1080×1350` (4:5) ist an mehreren Stellen gesetzt (`.slide`, `@page`, `--window-size`, `bake_photo.py`). Alle gemeinsam ändern.
- **Anderer Host statt Canva/Cloudflare:** nur Schritt 6/7 im Command betreffen das — solange am Ende editierbare Designs im Zielordner liegen, ist der Weg dorthin austauschbar.

---

## Bekannte Tücke

Beim PDF-Import verschmilzt Canva auf einzelnen Inhalts-Slides die grosse Zahl und den Textabsatz manchmal zu **einem** Textfeld (Nähe-Heuristik). Betrifft meist nur 1–2 Slides pro Woche und ist in Sekunden manuell trennbar. Wenn es dauerhaft stört: über PPTX (`python-pptx`, explizite Textboxen) importieren statt PDF.
