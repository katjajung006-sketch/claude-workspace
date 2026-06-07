# Karussell-Woche

> Komplette Wochen-Produktion: 7 fertige Instagram-Karussells, editierbar in Canva, je mit Caption als Kommentar, abgelegt in einem Ziel-Ordner. Themen wählt Claude selbst — nach Trend + Zielgruppe, immer spezifisch, nie generisch.

Dieser Command ist **ein fester Weg**, kein Vorschlag zum Umbauen bei jedem Lauf. Das Design-System (Schriften, Farben, Layout) steckt in den Render-Skripten — wer es ändern will, ändert die Skripte bewusst, nicht den Befehl.

> **Vor dem ersten Lauf einrichten** — überall, wo `[...]` steht, deinen eigenen Wert eintragen:
> - `[@DEINHANDLE]` — dein Instagram-Handle (steht auch oben in `build.py`).
> - `[DEIN-CANVA-ZIELORDNER-ID]` — Canva-Ordner, in den die Designs gelegt werden.
> - `[DEIN-CLOUDFLARE-TEMP-PROJEKT]` — Name eines **Wegwerf**-Cloudflare-Pages-Projekts nur fürs Hosten.
> - `[PFAD-ZU-DEINEN-KONTEXT-DATEIEN]` — deine Zielgruppen-/Brand-Voice-Notizen.
> - `[DEINE NISCHE]`, `[DEINE VERBOTENEN WÖRTER]`, `[DEINE STAMM-HASHTAGS]` — siehe Schritt 0/1.

---

## Was am Ende rauskommt

- **7 Karussells**, je 7–9 Slides (Foto-Cover + 5–7 Inhalts-Slides + Foto-Schluss).
- Jedes als **editierbares Canva-Design** (echter Text, Foto + Zahl als Elemente), abgelegt im Ziel-Ordner `[DEIN-CANVA-ZIELORDNER-ID]`.
- Je Karussell die **Caption inkl. Hashtags als Canva-Kommentar** am Design.
- Temporäres Hosting danach wieder gelöscht, lokales Staging aufgeräumt.
- Kurze Abschluss-Nachricht, dass die Woche fertig liegt.

---

## Schritt 0 — Kontext laden (Pflicht, jeder Lauf)

Lies zuerst, damit Stimme und Nische sitzen:
- `[PFAD-ZU-DEINEN-KONTEXT-DATEIEN]` — wer deine Zielgruppe ist (für Themenwahl + Sprache).
- deine Brand-Voice-Notizen — Tonalität, Power-Words, **verbotene Wörter**, Satzrhythmus.

**Harte Leitplanken (anpassen an deine Marke):**
- Bleib in `[DEINE NISCHE]`. Keine Fachsprache, die deine Zielgruppe nicht selbst benutzt.
- Verbotene Wörter: `[DEINE VERBOTENEN WÖRTER]` (z. B. Marketing-Phrasen, die nicht zu deiner Stimme passen).
- **Kein Satz darf nach KI klingen.** Keine Floskeln, kein „Das ist nicht X, sondern Y" als Masche, kein gleichförmiger Rhythmus.
- **Nichts Generisches.** Siehe Schritt 1.

---

## Schritt 1 — 7 Themen wählen (Trend + Zielgruppe)

**Quellen für den Trend-Blick (so weit verfügbar):**
1. *(optional)* Ein Wettbewerber-/Trend-Tracker, falls du einen hast — was in deiner Nische gerade läuft, als Resonanz-Signal nehmen. **Nie kopieren**, sondern in deine Stimme übersetzen.
2. Eigene Top-Performer: was bei dir bisher gut lief. Bewährte Winkel variieren, nicht wiederholen.
3. Live-Web: kurze `WebSearch` nach aktuellen Themen deiner Zielgruppe. Saison/Datum mitdenken.

**Auswahl-Regeln:**
- **Mix deiner Content-Säulen** — nicht alle 7 zum selben Unterthema.
- **Pro Karussell ein Ziel** (Speichern als Default; Teilen; ein konkreter CTA wie Freebie/Gruppe). Höchstens 1–2 mit hartem CTA pro Woche, der Rest Speichern/Teilen.
- **Keine Wiederholung** von Themen der Vorwoche (vorigen `KARUSSELLS.md`-Stand prüfen, falls vorhanden).

**Spezifisch statt generisch — der wichtigste Test.** Jedes Thema muss an einem **konkreten, schmalen Moment** aus dem Leben deiner Zielperson hängen, nicht an einem breiten Begriff.
- Generisch (verboten): „Stress abbauen", „5 Tipps für mehr Gelassenheit".
- Spezifisch (so): „Warum du abends erschöpft bist, obwohl du ‚nichts' geschafft hast".
- Vor dem Schreiben jedes Thema gegen deine Zielperson halten: Würde **sie** beim Scrollen kurz innehalten und denken „das bin ich"? Wenn nicht — verwerfen.

---

## Schritt 2 — Inhalte schreiben (Brand Voice)

Für jedes der 7 Karussells genau diese Felder füllen (Struktur wie in `scripts/karussell/build.py`, Liste `CAROUSELS`):

```python
{
    "slug": "NN-kurz-sprechend",          # 01.. 07, kebab-case
    "eyebrow": PILLAR_A | PILLAR_B,        # deine Content-Säule
    "cover": {"hook": "...", "sub": "..."},   # Hook = der starke erste Satz; sub = ruhiger Zweizeiler
    "content": ["...", "...", ...],            # 5–7 Zeilen, je 1 kurzer Gedanke; die große Zahl = laufender Index
    "close": {"relief": "...", "cta": "..."},  # relief = emotionaler Schlusssatz; cta = passend zum Ziel
}
```

Schreib-Regeln:
- **Cover-Hook:** kurz, konkret, trifft sofort. Keine Frage als Hook, außer sie sitzt.
- **Inhalts-Slides:** EIN Gedanke pro Slide, ruhig, max. ~2 kurze Sätze. Die durchnummerierte Zahl ist Gestaltung, kein Aufzähl-Zwang — der Text trägt.
- **Schluss:** `relief` = entlastender, wahrer Satz (kein Motivations-Spruch). `cta` passend zum Ziel; **Interaktions-Frage gehört NICHT auf die Schluss-Slide, sondern in die Caption.**
- **Caption je Karussell** (für `KARUSSELLS.md` + Canva-Kommentar): 3 kurze Absätze + Interaktions-/CTA-Zeile, dann 5 Hashtags aus deinem Set `[DEINE STAMM-HASHTAGS]` — passend zum Thema, nicht stur dieselben fünf.

Wenn ein Satz nach Vorlage/KI klingt: neu schreiben. Lieber roh und wahr als glatt.

---

## Schritt 3 — Dateien aktualisieren

- `scripts/karussell/build.py`: die `CAROUSELS`-Liste **komplett ersetzen** durch die 7 neuen. `PILLAR_*`/`HANDLE` bleiben.
- `scripts/karussell/KARUSSELLS.md`: neu schreiben — pro Karussell Überschrift, Säule · Ziel · Slide-Zahl · Slug, dann **Caption + Hashtags**.

---

## Schritt 4 — Gebackene Hintergründe sicherstellen

Cover/Schluss nutzen EIN flaches Bild mit eingebackenem Gradient (`cover_bg.png` / `close_bg.png`) — **kein separater `.scrim`-Layer**, sonst verdeckt Canva beim PDF-Import das Foto.

- Liegen `cover_bg.png` und `close_bg.png` schon vor und `photo.jpg` ist unverändert → **nichts tun**, wiederverwenden.
- Wenn `photo.jpg` getauscht wurde → `python3 scripts/karussell/bake_photo.py` einmal laufen lassen (rendert beide neu).

---

## Schritt 5 — Editierbare PDFs rendern

```bash
python3 scripts/karussell/build_pdf.py
```

Erzeugt je Karussell `scripts/karussell/_pdf/<slug>.pdf` — mehrseitig, **echter Text** (1080×1350), Foto fest in Cover/Schluss eingebacken. (Headless-Chrome `--print-to-pdf`, `@page{size:1080px 1350px}`.)

---

## Schritt 6 — Temporär hosten (Cloudflare Pages)

`import-design-from-url` braucht eine **öffentliche HTTPS-URL**. Eigenes, isoliertes Wegwerf-Projekt — **NICHT** deine Live-Projekte anfassen.

```bash
# Token + Account-ID aus deiner lokalen, gitignorierten Secret-Datei — NIE committen/pushen:
export CLOUDFLARE_API_TOKEN=<dein Token>
export CLOUDFLARE_ACCOUNT_ID=<deine Account-ID>

npx --yes wrangler@latest pages project create [DEIN-CLOUDFLARE-TEMP-PROJEKT] --production-branch=main
npx --yes wrangler@latest pages deploy scripts/karussell/_pdf --project-name=[DEIN-CLOUDFLARE-TEMP-PROJEKT] --branch=main --commit-dirty=true
```

Aus der Deploy-Ausgabe die `https://<...>.[DEIN-CLOUDFLARE-TEMP-PROJEKT].pages.dev`-Basis-URL nehmen. PDF-URL je Karussell = `<basis>/<slug>.pdf`. Kurz einen Treffer mit `curl -sI` prüfen (200).

> Alternative ohne Cloudflare: jeder Dienst, der die PDFs unter einer öffentlichen HTTPS-URL ausliefert (z. B. ein anderer statischer Host). Wichtig ist nur die erreichbare `.pdf`-URL.

---

## Schritt 7 — Nach Canva importieren (7×)

Für jedes Karussell:
- `import-design-from-url` mit `url = <basis>/<slug>.pdf`, `name = "<Karussell-Titel>"`, `intended_design_type = "instagram_post"`.
- Design-ID merken.

---

## Schritt 8 — Verifizieren

Pro Design einmal `get-design-thumbnail` (oder `start-editing-transaction`) prüfen:
- **Cover zeigt das Foto** (nicht nur Farbfläche). Wenn nein → Hintergrund-Backen / `.scrim` checken (Schritt 4) und neu importieren.
- **Inhalts-Slides:** Text + große Zahl vorhanden.

**Bekannte Tücke:** Der PDF-Import verschmilzt auf einzelnen Inhalts-Slides die große Zahl und den Absatz manchmal zu **einem** Textfeld (Canva-Nähe-Heuristik) → Zahl dann nicht einzeln verschiebbar. Meist nur 1–2 Slides, in Sekunden manuell trennbar. Wenn es dauerhaft nervt → robuster Fix via PPTX-Import (`python-pptx`, explizite Textboxen) oder Zahl im PDF klar separieren. Nicht ungefragt das ganze Format umbauen.

---

## Schritt 9 — Ablegen + Caption als Kommentar

Pro Design:
- `move-item-to-folder` → Ziel-Ordner `[DEIN-CANVA-ZIELORDNER-ID]`.
- `comment-on-design` → die Caption inkl. Hashtags dieses Karussells (Text aus `KARUSSELLS.md`).

---

## Schritt 10 — Aufräumen

```bash
npx --yes wrangler@latest pages project delete [DEIN-CLOUDFLARE-TEMP-PROJEKT] --yes
rm -rf scripts/karussell/_pdf
```

*(Optional: dein Canva-Brand-Kit-ID `[DEIN-BRAND-KIT-ID]` zur Sicherheit notieren.)*

---

## Schritt 11 — Benachrichtigen

Kurze Nachricht: „7 Karussells für die Woche liegen in Canva → Ziel-Ordner, Captions als Kommentar dran. Themen: <7 Titel in einer Zeile>."

---

## Nicht tun

- **Nicht** deine Secret-Datei committen/pushen.
- **Nicht** deine Live-Hosting-Projekte anfassen — nur das Wegwerf-Temp-Projekt.
- **Nicht** das Design-System ändern oder Themen vorab zur Freigabe vorlegen (läuft autonom; Feedback kommt zwischendurch).

---

## Voraussetzungen (siehe README)

- Python 3 + Google Chrome (für Headless-Rendering).
- Canva-MCP in Claude Code verbunden (für `import-design-from-url`, `move-item-to-folder`, `comment-on-design`).
- Cloudflare-Account + `wrangler` (oder ein anderer öffentlicher HTTPS-Host).
- Eigenes Foto als `scripts/karussell/photo.jpg`.
