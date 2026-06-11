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
- `outputs/story-woche/verlauf.md` — **was zuletzt schon dran war** (gemeinsamer Verlauf mit `/story-woche`). Die letzten Einträge lesen und **nicht wiederholen** — besonders das Körperthema bei `impuls`, den Winkel bei `satz`/`take`. Existiert die Datei nicht: erster Lauf, neu anlegen.
- `~/.claude/projects/-Users-katjajung-claude-workspace-vorlage/memory/project_freebie_inventory.md` (für korrekte Links bei Einladungen)

Volle Format-Definitionen, Story-Mechanik und Link-Disziplin stehen in `.claude/commands/story-woche.md` (Bausteine A–H). Hier nur die Kurzfassung zum Auswählen.

**Variation:** Den gewählten Typ inhaltlich frisch halten gegenüber den letzten Verlauf-Einträgen — kein Körperthema, kein wahrer Satz, kein Take doppelt (auch nicht leicht umformuliert). Bei mehreren Varianten (`satz 3`) untereinander klar verschieden.

---

## Schritt 2 — Typ bestimmen

**Wenn $ARGUMENTS leer:** Frage kurz nach dem Typ:
> `satz` · `check` · `impuls` · `take` · `frage` · `anstoss` · `einladung` · `bts`

**Eingaben erkennen:**
- `satz` / `wahrersatz` → **A** Wahrer Satz (1 Frame, Slider/Teilen)
- `check` / `poll` / `umfrage` / `spür` → **B** Spür-Check (1 Frame, This-or-That-Umfrage)
- `impuls` / `körper` → **C** Mini-Körperimpuls (2–3 Frames, Mikro-Übung)
- `take` / `klartext` → **D** Leiser Take (1–2 Frames, Frage-Sticker)
- `frage` / `box` → **E** Frage-Box (1 Frame, offene Frage)
- `anstoss` / `recycling` / `teilen` → **F** Anstoß (Reel/Karussell als Story teilen)
- `einladung` / `freebie` / `angebot` / `telegram` → **G** Einladung (2–3 Frames, EIN Ziel, Link-Sticker)
- `bts` / `aufbau` → **H** Behind-the-Scenes (1–2 Frames)

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

**Verlauf festhalten:** Bei Typen mit rotierbarem Inhalt (`impuls`, `satz`, `take`, `check`, `frage`, `bts`) **eine kurze Zeile** in die Liste „Einzel-Stories (laufend)" in `outputs/story-woche/verlauf.md` anfügen — Datum · Typ · Kernthema (z. B. „2026-06-12 · impuls · Füße"). Nur eine Zeile, kein voller Block. Bei reinem `anstoss`/`einladung` ohne neues Thema entfällt der Eintrag.

**Nach der Ausgabe:** kurz fragen, ob Anpassungen gewünscht sind.

---

## Stilregeln

- Brand Voice aus `brand-voice.md`. Nur Funktionsmodus + einfache Yoga-/Atemimpulse. NIE „Nervensystem"/Fachsprache.
- Verbotene Wörter (Disziplin/Selbstoptimierung/Selfcare/„du musst nur" …) — außer Disziplin in Verneinung.
- Kein KI-Klang, keine Floskeln, kein gleichförmiger Rhythmus. Geduzt.
- Kein Emoji im Frame-Text (nur in Sticker-/Hinweis-Zeilen). Einladend, erinnernd, körpernah — nie belehrend oder antreibend.
- Polls sparsam (max. 2–3/Woche im Gesamtbild). Ein Story-Run = ein Ziel.
