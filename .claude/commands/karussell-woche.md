# Karussell-Woche

> Komplette Wochen-Produktion: 7 fertige Instagram-Karussells, editierbar in Canva, je mit Caption als Kommentar, abgelegt im Ordner „erstellte Karussells". Der feste Freitags-Output. Themen wählt Claude selbst — nach Trend + Soul Client, immer spezifisch, nie generisch.

Dieser Command ist der **eine feste Weg**. Nicht neu designen, nicht das Format hinterfragen. Katja hat den Look final freigegeben (2026-06-03: „perfekt, das passt"). Wenn etwas am Look geändert werden soll, sagt Katja das ausdrücklich — sonst läuft exakt diese Vorlage.

---

## Was am Ende rauskommt

- **7 Karussells**, je 7–9 Slides (Foto-Cover + 5–7 Inhalts-Slides + Foto-Schluss).
- Jedes als **editierbares Canva-Design** (echter Text, Foto + Zahl als Elemente), abgelegt im Ordner **„erstellte Karussells"** (`FAHLiWIgZvA`).
- Je Karussell die **Caption inkl. Hashtags als Canva-Kommentar** am Design.
- Temporäres Hosting danach wieder gelöscht, lokales Staging aufgeräumt.
- Katja kurz benachrichtigt, dass die Woche fertig liegt.

---

## Schritt 0 — Kontext laden (Pflicht, jeder Lauf)

Lies zuerst, damit Stimme und Nische sitzen:
- `context/soulclient.md` — die funktionierende Frau 40+ (für Themenwahl + Sprache)
- `context/brand-voice.md` — Tonalität, Power-Words, **verbotene Wörter**, Satzrhythmus
- `~/.claude/projects/-Users-katjajung-claude-workspace-vorlage/memory/project_karussell_design_system.md` — dieses Design-System + bekannte Import-Tücken
- `~/.claude/projects/-Users-katjajung-claude-workspace-vorlage/memory/feedback_content_niche.md` — Nische
- `~/.claude/projects/-Users-katjajung-claude-workspace-vorlage/memory/feedback_no_generic.md` — nichts darf generisch klingen

**Harte Leitplanken (nicht verhandelbar):**
- Nur **Funktionsmodus** + **einfache Yoga-/Atemimpulse**. NIEMALS „Nervensystem", „Vagusnerv", „Regulation", „Perimenopause", Fachsprache.
- Verbotene Marken-Wörter: High Performance, Disziplin, Challenge, Transformation u. Ä. (siehe brand-voice).
- **Übungen anfängerinnen-tauglich:** Leitet ein Karussell eine konkrete Übung/Haltung an, vollständig erklären (Ausgangshaltung + genaue Bewegung + Atemrichtung + Wiederholung/Dauer), sodass eine absolute Anfängerin es allein nachmacht. Keine Pose-Namen ohne Erklärung. Kanon: `reference/somatic-yoga.md`.
- **Kein Satz darf nach KI klingen.** Kein „Das ist nicht X, sondern Y" als Masche, keine Floskeln, kein gleichförmiger Rhythmus.
- **Nichts Generisches.** Siehe Schritt 1.

---

## Schritt 1 — 7 Themen wählen (Trend + Soul Client)

**Quellen für den Trend-Blick (in dieser Reihenfolge, so weit verfügbar):**
1. **Wettbewerber-Späher:** `scripts/instagram-watch/state.json` — was die drei Accounts (@entspannungsstudio_anila, @yes.you.are_, @julia.physioglueck) zuletzt gepostet haben. Themen, die dort gerade laufen, als Resonanz-Signal nehmen — **nie kopieren**, sondern in Katjas Nische + Stimme übersetzen.
2. **Eigene Top-Performer:** frühere `outputs/karussell/KARUSSELLS.md`-Stände / was gut lief. Bewährte Winkel variieren, nicht wiederholen.
3. **Live-Web:** kurze `WebSearch` nach aktuellen Themen rund um Frauen 40+, Erschöpfung im Alltag, stilles Yoga, „immer funktionieren". Saison/Datum mitdenken (z. B. Jahresanfang, dunkle Monate, Ferien-Ende).

**Auswahl-Regeln:**
- **Mix beider Säulen:** „Der Körper im Funktionsmodus" + „Yoga ohne Leistungsdruck". Grob 4/3 oder 3/4, nicht alles eine Säule.
- **Pro Karussell ein Ziel** (Speichern als Default; Teilen; Telegram-Gruppe „Zurück zu dir"; Freebie „5 Tage zurück in deinen Körper"). Höchstens 1–2 mit Freebie/Telegram-CTA pro Woche, der Rest Speichern/Teilen.
- **Keine Wiederholung** von Themen der Vorwoche (vorigen KARUSSELLS.md-Stand prüfen, falls noch da).

**Spezifisch statt generisch — der wichtigste Test.** Jedes Thema muss an einem **konkreten, schmalen Moment** aus dem Leben der Soul-Client hängen, nicht an einem breiten Begriff.
- Generisch (verboten): „Stress abbauen", „Selbstfürsorge", „Zur Ruhe kommen", „5 Tipps für mehr Gelassenheit".
- Spezifisch (so): „Warum du abends erschöpft bist, obwohl du ‚nichts' geschafft hast", „7 stille Zeichen, dass du nur noch funktionierst", „Der Moment im Auto, in dem du kurz nicht aussteigen willst".
- Vor dem Schreiben jedes Thema gegen den Soul-Client halten: Würde **sie** beim Scrollen kurz innehalten und denken „das bin ich"? Wenn nicht — verwerfen.

---

## Schritt 2 — Inhalte schreiben (Brand Voice)

Für jedes der 7 Karussells genau diese Felder füllen (Struktur wie in `outputs/karussell/build.py`, Liste `CAROUSELS`):

```python
{
    "slug": "NN-kurz-sprechend",          # 01.. 07, kebab-case
    "eyebrow": PILLAR_FUNKTION | PILLAR_YOGA,
    "cover": {"hook": "...", "sub": "..."},   # Hook = der starke erste Satz; sub = ruhiger Zweizeiler
    "content": ["...", "...", ...],            # 5–7 Zeilen, je 1 kurzer Satz/Gedanke; die große Zahl = laufender Index
    "close": {"relief": "...", "cta": "..."},  # relief = emotionaler Schlusssatz; cta = passend zum Ziel
}
```

Schreib-Regeln:
- **Cover-Hook:** kurz, körpernah, trifft sofort — ein echter Scroll-Stopper, kein netter Satz. Aus der **Nische-Hook-Palette** bauen (`reference/hook-formel.md` → „Nische": Widerspruch · Das Unausgesprochene · Erkennung/Spiegel · Insider · Listen-Hook; **keine Confession**, die ist persönlich-exklusiv), ≥ 2 Mechanismen + Auflöse-Test. Über die 7 Karussells die Form variieren, nicht 7× dieselbe. Keine Frage als Hook, außer sie sitzt.
- **Inhalts-Slides:** EIN Gedanke pro Slide, ruhig, in Libre-Baskerville-Länge (max. ~2 kurze Sätze). Die durchnummerierte Zahl ist Gestaltung, kein Aufzähl-Zwang — der Text trägt.
- **Schluss:** `relief` = entlastender, wahrer Satz (kein Motivations-Spruch). `cta` passend zum Ziel; **Interaktions-Frage gehört NICHT auf die Schluss-Slide, sondern in die Caption.**
- **Caption je Karussell** (für KARUSSELLS.md + Canva-Kommentar): 3 kurze Absätze + Interaktions-/CTA-Zeile, dann 5 Hashtags. Hashtags aus dem etablierten Set mischen: #funktionsmodus #yogastattfunktionieren #zurückzudir #erschöpfung #frauenab40 #selbstübergehen #atemübung #yogaamabend #loslassen #atempause — passend zum Thema, nicht stur dieselben fünf.

Wenn ein Satz nach Vorlage/KI klingt: neu schreiben. Lieber roh und wahr als glatt.

---

## Schritt 3 — Dateien aktualisieren

- `outputs/karussell/build.py`: die `CAROUSELS`-Liste **komplett ersetzen** durch die 7 neuen. `PILLAR_FUNKTION`/`PILLAR_YOGA`/`HANDLE` bleiben.
- `outputs/karussell/KARUSSELLS.md`: neu schreiben — pro Karussell Überschrift, Säule · Ziel · Slide-Zahl · Ordner-Slug, dann **Caption + Hashtags**.

---

## Schritt 4 — Gebackene Hintergründe sicherstellen

Cover/Schluss nutzen EIN flaches Bild mit eingebackenem Gradient (`cover_bg.png` / `close_bg.png`) — **kein separater `.scrim`-Layer**, sonst verdeckt Canva beim PDF-Import das Foto.

- Liegen `outputs/karussell/cover_bg.png` und `close_bg.png` schon vor und `katja.jpg` ist unverändert → **nichts tun**, wiederverwenden.
- Wenn `katja.jpg` getauscht wurde → `python3 outputs/karussell/bake_photo.py` einmal laufen lassen (rendert beide neu).

---

## Schritt 5 — Editierbare PDFs rendern

```bash
python3 outputs/karussell/build_pdf.py
```

Erzeugt je Karussell `outputs/karussell/_pdf/<slug>.pdf` — mehrseitig, **echter Text** (1080×1350), Foto fest in Cover/Schluss eingebacken. (Headless-Chrome `--print-to-pdf`, `@page{size:1080px 1350px}`.)

---

## Schritt 6 — Temporär hosten (Cloudflare Pages)

`import-design-from-url` braucht eine **öffentliche HTTPS-URL**. Eigenes, isoliertes Wegwerf-Projekt — **NICHT** die Live-Funnel-Projekte (`katjajung-check`, `kurs-10-minuten-rueckkehr`) anfassen.

```bash
# Token + Account-ID aus reference/secrets.local.md (gitignored, NIE committen/pushen):
export CLOUDFLARE_API_TOKEN=<aus secrets.local.md>
export CLOUDFLARE_ACCOUNT_ID=<aus secrets.local.md>

npx --yes wrangler@latest pages project create karussell-import-temp --production-branch=main
npx --yes wrangler@latest pages deploy outputs/karussell/_pdf --project-name=karussell-import-temp --branch=main --commit-dirty=true
```

Aus der Deploy-Ausgabe die `https://<...>.karussell-import-temp.pages.dev`-Basis-URL nehmen. PDF-URL je Karussell = `<basis>/<slug>.pdf`. Kurz einen Treffer mit `curl -sI` prüfen (200).

---

## Schritt 7 — Nach Canva importieren (7×)

Für jedes Karussell:
- `import-design-from-url` mit `url = <basis>/<slug>.pdf`, `name = "<Karussell-Titel>"`, `intended_design_type = "instagram_post"`.
- Design-ID merken.

---

## Schritt 8 — Verifizieren

Pro Design einmal `get-design-thumbnail` (oder `start-editing-transaction`) prüfen:
- **Cover zeigt das Foto** (nicht nur Espresso-Fläche). Wenn nein → Hintergrund-Backen / `.scrim` checken (Schritt 4) und neu importieren.
- **Inhalts-Slides:** Text + große Zahl vorhanden.

**Bekannte Tücke:** Der PDF-Import verschmilzt auf einzelnen Inhalts-Slides die große Zahl und den Absatz zu **einem** Textfeld (Canva-Nähe-Heuristik) → Zahl dann nicht einzeln verschiebbar. Trat in Charge 1 (2026-06-03) bei 2 von ~45 Slides auf. Aktueller Stand: hinnehmbar, Katja kann es in Sekunden trennen. **Wenn diese Automatik in der Testphase mehrfach nervt → robusten Fix umsetzen (PPTX-Import via `python-pptx`: explizite, nie verschmelzende Textboxen; oder Zahl im PDF klar separieren).** Nicht ungefragt das ganze Format umbauen.

---

## Schritt 9 — Ablegen + Caption als Kommentar

Pro Design:
- `move-item-to-folder` → Ziel-Ordner `FAHLiWIgZvA` („erstellte Karussells", im Hauptordner „Karussells" `FAHLiUSMhec`).
- `comment-on-design` → die Caption inkl. Hashtags dieses Karussells (Text aus KARUSSELLS.md).

---

## Schritt 10 — Aufräumen

```bash
npx --yes wrangler@latest pages project delete karussell-import-temp --yes
rm -rf outputs/karussell/_pdf
```

Brand-Kit zur Sicherheit: `yoga.statt.funktionieren` = `kAHKM5Z5cP0`.

---

## Schritt 11 — Katja benachrichtigen

Kurze Nachricht: „7 Karussells für die Woche liegen in Canva → Ordner ‚erstellte Karussells', Captions als Kommentar dran. Themen: <7 Titel in einer Zeile>."
- Wenn ein Telegram-Weg verfügbar ist (`scripts/instagram-watch/config.json` Token), gern als Telegram-Ping. Sonst als Text-Antwort im Lauf.

---

## Nicht tun

- **Nicht** nach Notion „Feed" archivieren — nur wenn Katja ein Stück ausdrücklich abnimmt („passt so" / „perfekt").
- **Nicht** `secrets.local.md` oder `config.json` committen/pushen.
- **Nicht** die Live-Funnel-Cloudflare-Projekte anfassen.
- **Nicht** das Design-System ändern oder Themen vorab zur Freigabe vorlegen (läuft autonom; Katja gibt zwischendurch Feedback).
