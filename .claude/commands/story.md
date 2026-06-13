# Story

> Ein einzelner Instagram-Story-Post für zwischendurch — copy-fertig: Frame-Text, Sticker, B-Roll-Hinweis, Link wo nötig. Der spontane Bruder von `/story-woche` (dort liegt der volle Format-Katalog und die Story-Mechanik). Faceless: B-Roll + Text-Overlay.

---

## Variablen

eingabe: $ARGUMENTS

---

## Schritt 1 — Kontext laden

Lies zuerst:
- `context/soulclient.md`
- `context/brand-voice.md`
- `reference/story-aufbau.md` — **was eine gute Story trägt** (Abbruch-Kurve, Frame-1-Regel, Sticker-Hebel, DM-vor-Link) + Zielgruppen-Übersetzung (müde Abend-Frau 40+). Grundlage für jeden Frame.
- `reference/persoenlicher-content.md` — **nur bei Typ `persoenlich`/`bts`:** die 6 Türen + Leitplanken (zurück zu ihr, kein Oversharing, keine Guru-Story).
- `outputs/story-woche/verlauf.md` — **was zuletzt schon dran war** (gemeinsamer Verlauf mit `/story-woche`). Die letzten Einträge lesen und **nicht wiederholen** — besonders das Körperthema bei `impuls`, den Winkel bei `satz`/`take`. Existiert die Datei nicht: erster Lauf, neu anlegen.
- `~/.claude/projects/-Users-katjajung-claude-workspace-vorlage/memory/project_freebie_inventory.md` (für korrekte Links bei Einladungen)

Volle Format-Definitionen, Story-Mechanik und Link-Disziplin stehen in `.claude/commands/story-woche.md` (Bausteine A–H). Hier nur die Kurzfassung zum Auswählen.

**Variation:** Den gewählten Typ inhaltlich frisch halten gegenüber den letzten Verlauf-Einträgen — kein Körperthema, kein wahrer Satz, kein Take doppelt (auch nicht leicht umformuliert). Bei mehreren Varianten (`satz 3`) untereinander klar verschieden.

---

## Schritt 2 — Typ bestimmen

**Wenn $ARGUMENTS leer:** Frage kurz nach dem Typ:
> `satz` · `check` · `impuls` · `take` · `frage` · `anstoss` · `einladung` · `bts` · `persoenlich`

**Eingaben erkennen:**
- `satz` / `wahrersatz` → **A** Wahrer Satz (1 Frame, Slider/Teilen)
- `check` / `poll` / `umfrage` / `spür` → **B** Spür-Check (1 Frame, This-or-That-Umfrage)
- `impuls` / `körper` → **C** Mini-Körperimpuls (2–3 Frames, Mikro-Übung)
- `take` / `klartext` → **D** Leiser Take (1–2 Frames, Frage-Sticker)
- `frage` / `box` → **E** Frage-Box (1 Frame, offene Frage)
- `anstoss` / `recycling` / `teilen` → **F** Anstoß (Reel/Karussell als Story teilen)
- `einladung` / `freebie` / `angebot` / `telegram` → **G** Einladung (2–3 Frames, EIN Ziel, Link-Sticker)
- `bts` / `aufbau` / `persoenlich` / `persönlich` / `tür` → **H** Persönliche Tür (1–2 Frames) — **eine der 6 Türen** aus `reference/persoenlicher-content.md` wählen (rotierend gegen den Verlauf-Abschnitt „Persönliche Tür"; nicht die zuletzt genutzte). Pflicht: endet bei ihr, kein Tagebuch, kein Oversharing.

**Zahl dahinter** (z. B. `satz 3`): so viele Varianten erstellen.

---

## Schritt 3 — Erstellen

Den gewählten Baustein exakt nach der Definition in `story-woche.md` schreiben. Frischer, spezifischer Inhalt — nichts Generisches, an einem konkreten Moment der Soul-Client.

**Bei G (Einladung) die Link-Disziplin einhalten:**
- Freebie „Funktionsmodus-Check" → Opt-in-Seite / „Link in meiner Bio".
- Angebot „10-Minuten-Rückkehr" (17 €) → Link-Sticker „Ich will zurück zu mir" → `10-minuten-rueckkehr.katjajung.com` (**nie zur Kasse**, 7-€-Tripwire nie öffentlich).
- Telegram-Gruppe „Zurück zu dir" → Einladung in die kostenlose Community.
- Bei Keyword-Mechanik („Schreib mir ANKOMMEN") eine kurze, warme DM-Antwort mitliefern.

---

## Ausgabe-Format

```
**Story — [Typ]**

**Frame 1**
[Frame-Text, copy-fertig]
🟫 Hintergrund: [B-Roll-/Flächen-Hinweis]
🎯 Sticker: [Sticker-Anweisung]

(weitere Frames bei C/D/G)
```

Bei Einladung mit Keyword: DM-Antwort separat darunter.

**Verlauf festhalten:** Bei Typen mit rotierbarem Inhalt (`impuls`, `satz`, `take`, `check`, `frage`, `bts`, `persoenlich`) **eine kurze Zeile** in die Liste „Einzel-Stories (laufend)" in `outputs/story-woche/verlauf.md` anfügen — Datum · Typ · Kernthema (z. B. „2026-06-12 · impuls · Füße"). Nur eine Zeile, kein voller Block. Bei `persoenlich`/`bts` zusätzlich die genutzte Tür oben im Abschnitt „Persönliche Tür" vermerken (für die Rotation). Bei reinem `anstoss`/`einladung` ohne neues Thema entfällt der Eintrag.

**Nach der Ausgabe:** kurz fragen, ob Anpassungen gewünscht sind.

---

## Stilregeln

- Brand Voice aus `brand-voice.md`. Nur Funktionsmodus + einfache Yoga-/Atemimpulse. NIE „Nervensystem"/Fachsprache.
- Verbotene Wörter (Disziplin/Selbstoptimierung/Selfcare/„du musst nur" …) — **auch nicht per Verneinung**; direkt positiv formulieren (z. B. „mehr Druck"). Außerdem: immer einfache, normale Alltagssprache, nicht poetisch/verkopft.
- Kein KI-Klang, keine Floskeln, kein gleichförmiger Rhythmus. Geduzt.
- Kein Emoji im Frame-Text (nur in Sticker-/Hinweis-Zeilen). Einladend, erinnernd, körpernah — nie belehrend oder antreibend.
- Polls sparsam (max. 2–3/Woche im Gesamtbild). Ein Story-Run = ein Ziel.
- **Übungen/Körperimpulse IMMER aus Sicht der absoluten Anfängerin erklären** (Frau, die noch nie Yoga/Körperarbeit gemacht hat). Pflicht je Übung: **Ausgangshaltung** (wo, wie sitzt/liegt/steht sie) + **genaue Bewegung** (wohin, wie weit, welche Richtung) + **Atemrichtung** (ein-/ausatmen) + **Wiederholung**. Keine Fachbegriffe, keine Pose-Namen ohne Erklärung. Sie muss es allein mit dem Text richtig machen können (volle Erklär-Regel in `story-woche.md`, Baustein C).
