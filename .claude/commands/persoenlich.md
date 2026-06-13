# Persönlich — die Frau hinter der Marke (Feed)

> Baut ein persönliches **Feed-Piece** — Reel ODER Karussell — aus einer der 6 Türen. Ziel: Follower lernen Katja als Mensch kennen, ohne dass die Nische verwässert. Holt Inhalt, Stimme und Leitplanken aus `reference/persoenlicher-content.md`, die Format-Struktur aus den bestehenden Reel-/Karussell-Skills — kein Doppeln.

## Variablen

eingabe: $ARGUMENTS  *(optional — z. B. „warum", „karussell ausbildung", „reel zwischenstand", oder ein freies Thema)*

---

## Schritt 1 — Kontext laden (Pflicht)

Lies zuerst:
- `reference/persoenlicher-content.md` — **die 6 Türen, Leitplanken, die Regel „zurück zu ihr", CTA-Logik, Rhythmus.** Das ist die Quelle für diesen Skill.
- `context/soulclient.md` — die funktionierende Frau 40+ (damit der Anschluss zu ihr sitzt)
- `context/brand-voice.md` — Tonalität, Power-Words, **verbotene Wörter**, Satzrhythmus
- `context/founder-story.md` — für Tür 5 (Das Warum) die echten Sätze/Momente
- `context/personal-info.md` — echte Lebens-Details (Job bis 14:30, Tochter 25, alleine, Morgen-Routine) für Tür 1/2/4
- `outputs/story-woche/verlauf.md` (Abschnitt „Persönliche Tür") — welche Tür zuletzt schon in Stories lief, damit Feed + Stories nicht dieselbe Tür gleichzeitig spielen

Memory mitnehmen: `feedback_no_generic`, `feedback_einfach_verstaendlich`, `feedback_hook_kalter_traffic`, `feedback_caption_kurz_am_hook`, `feedback_cta_passend_freebie`, `feedback_reel_kein_caption_verweis_cta`, `feedback_notion_alt_hooks`.

---

## Schritt 2 — Tür + Format bestimmen

**Tür erkennen** (aus $ARGUMENTS, sonst Claude wählt — rotierend, nicht zuletzt verwendete Tür):
- `zwischenstand` / `job` / `ehrlich` → **Tür 1** Der ehrliche Zwischenstand
- `körper` / `rückkehr` / `morgen` / `routine` → **Tür 2** Eigene Rückkehr in den Körper
- `ausbildung` / `lernen` → **Tür 3** Die Ausbildung
- `leben` / `alltag` / `tochter` / `feierabend` → **Tür 4** Das echte Leben drumherum
- `warum` / `geschichte` / `story` → **Tür 5** Das Warum (in Häppchen)
- `gesicht` / `stimme` / `audio` → **Tür 6** Gesicht & Stimme
- Freies Thema → die passendste Tür wählen und kurz benennen.

**Format erkennen** (`reel` / `karussell` in $ARGUMENTS, sonst Default je Tür):
| Tür | Default-Format |
|---|---|
| 1 Zwischenstand | Reel |
| 2 Rückkehr Körper | Reel |
| 3 Ausbildung | Karussell |
| 4 Echtes Leben | Reel |
| 5 Das Warum | Reel (Karussell als starke Alternative) |
| 6 Gesicht & Stimme | Reel mit Gesicht — **Hinweis:** Tür 6 lebt eigentlich in Stories. Im Feed nur bauen, wenn ausdrücklich ein Gesicht-/Stimme-Reel gewollt ist. Sonst auf `/story persoenlich` verweisen. |

Katja kann beides vorgeben: `/persoenlich karussell warum`.

---

## Schritt 3 — Bauen

### Wenn Reel
Folge der **Output-Struktur aus `.claude/commands/reel.md`** (Reel-Text · Thumbnail-Hook/Reelcover · Caption · B-Roll · 5 Hashtags · Story-Sequenz · DM-Antwort wenn nötig) — **mit diesen Abweichungen für persönlichen Content:**
- **KEINE Grundformel-Pflicht.** Die 4 Grundformeln aus `reel.md` gelten nur fürs Funktionsmodus-Erkennungs-Format. Hier trägt ein **persönlicher Hook** aus der gewählten Tür (ihre Wahrheit, ihr Moment) — siehe Beispiel-Winkel in `reference/persoenlicher-content.md`. Der Hook muss trotzdem ein Scroll-Stopper sein (erste 1–2 Sek., sofort klar worum's geht — Memory `feedback_hook_kalter_traffic`).
- **Reel-Text:** 3 Beats, ehrlicher Ich-Einstieg statt Klammersatz. Faceless möglich (ruhige B-Roll), Gesicht optional.
- **Caption:** nicht mit derselben Zeile wie das Reel starten; kurz und am Hook bleiben; endet bei ihr (die „zurück zu ihr"-Regel). Kein Yoga-Verkaufsabsatz.
- Kein On-Screen-CTA, kein „steht in der Caption" (Memory `feedback_reel_kein_caption_verweis_cta`).

### Wenn Karussell
Folge der **Slide-/Output-Struktur aus `.claude/commands/karussell-einstieg.md`** (Cover-Hook → Aufbau → Erkenntnis → CTA · Caption · 5 Hashtags · Story-Sequenz), aber **als persönliche Erzählung** statt Teach: Tür 5 = Geschichte über Slides, Tür 3 = „was ich gerade lerne". Kein Freebie-Zwang, kein ANKOMMEN-CTA per Default.

### Für beide Formate (Pflicht)
- **Zurück zu ihr** am Ende — nie reines Tagebuch.
- Leitplanken aus `reference/persoenlicher-content.md`: kein Oversharing, keine perfekte Guru-Story, leise Wahrheit, einfache Alltagssprache.
- Kommt eine Übung/Haltung vor: anfängerinnen-tauglich erklären (Ausgangshaltung + genaue Bewegung + Atemrichtung + feste Wiederholung; Kanon `reference/somatic-yoga.md`).

### CTA bewusst wählen
Persönlicher Content baut Beziehung, nicht Funnel (siehe `reference/persoenlicher-content.md` → CTA-Logik):
- Default: leiser **Folgen**-Grund („bleib hier / folg mir, wenn du auch leise rauswillst — ohne dich noch mehr zu optimieren") oder ein Reaktions-/Frage-Sticker in den Stories.
- **Kein reflexhaftes „Speichern".** Freebie-CTA nur ausnahmsweise und ganz leise.

---

## Schritt 3.5 — Alt-Hooks (Pflicht)

Immer **2 alternative Hooks** zum finalen mitliefern („zum Tauschen") — für die Notion-Ablage und zum Vergleichen (Memory `feedback_notion_alt_hooks`).

---

## Ausgabe-Format

```
ERKANNTE TÜR: [Nr + Name] · FORMAT: [Reel / Karussell]

— dann die vollständigen Outputs des gewählten Formats —
(Reel: Reel-Text · Reelcover · Caption · B-Roll · 5 Hashtags · Story-Sequenz · DM-Antwort wenn nötig)
(Karussell: Slides · Caption · 5 Hashtags · Story-Sequenz · DM-Antwort wenn nötig)

ALT-HOOKS (zum Tauschen):
1. [Alternative 1]
2. [Alternative 2]
```

Nach der Ausgabe: kurz fragen, ob Tür, Hook, Format oder Caption angepasst werden sollen.

---

## Notion (nur auf Abnahme)

Erst wenn Katja abnimmt („passt so" / „perfekt") → in DB „Feed" (`33a8aca2-e91e-81af-8577-000b691410f4`), wie aller Feed-Content (Memory `notion_content_workflow`). Content-Säule = nächstliegende (meist „Der Körper im Funktionsmodus"). **Die 2 Alt-Hooks mit in die Seite.** Nie ungefragt ablegen.

---

## Nicht tun

- **Nicht** die Funktionsmodus-Grundformeln als Hook erzwingen — das ist hier das falsche Format.
- **Nicht** reines Tagebuch ohne Anschluss zur Soul-Client.
- **Nicht** die perfekte „ich hab's gelöst"-Story — sie ist noch unterwegs, das ist der Vorsprung.
- **Nicht** Oversharing, nicht Details über Dritte ohne deren Okay.
- **Nicht** reflexhaft „Speichern" als CTA, **nicht** ungefragt ein Freebie pushen.
- **Nicht** nach KI klingen, **nicht** generisch, **nicht** poetisch/verkopft.
