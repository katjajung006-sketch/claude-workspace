# Persönlich — die Frau hinter der Marke (Feed)

> Baut ein persönliches **Feed-Piece** — Reel ODER Karussell — aus **Tür 5 (Deine Geschichte / Das Warum)**. Das ist die EINZIGE Tür fürs Feed: nur deine Geschichte ist stark genug, um im Grid zu stoppen. Die anderen 5 Türen sind Story-Material und laufen über `/story persoenlich` + `/story-woche`. Ziel: Follower lernen Katja als Mensch kennen, ohne dass die Nische verwässert. Holt Inhalt, Stimme und Leitplanken aus `reference/persoenlicher-content.md`, die Format-Struktur aus den bestehenden Reel-/Karussell-Skills — kein Doppeln.

## Variablen

eingabe: $ARGUMENTS  *(optional — `reel` / `karussell` fürs Format, dazu optional ein Häppchen/Winkel der Geschichte, z. B. „reel wendepunkt" oder „karussell von außen sah alles gut aus")*

---

## Schritt 1 — Kontext laden (Pflicht)

Lies zuerst:
- `reference/persoenlicher-content.md` — **Leitplanken, die Regel „zurück zu ihr", CTA-Logik, Positionierung (du bist RAUS).** Tür 5 + die Feed-Logik stehen dort. Das ist die Quelle für diesen Skill.
- `context/founder-story.md` — **die Hauptquelle:** die echten Sätze/Momente deiner Geschichte. Daraus kommt das Häppchen.
- `context/soulclient.md` — die funktionierende Frau 40+ (damit der Anschluss zu ihr sitzt)
- `context/brand-voice.md` — Tonalität, Power-Words, **verbotene Wörter**, Satzrhythmus
- `context/personal-info.md` — echte Lebens-Details (Job bis 14:30, Tochter 25, alleine, Morgen-Routine), falls für die Geschichte gebraucht
- `outputs/story-woche/verlauf.md` (Abschnitt „Persönliche Türen") + die Notion-DB „Feed" — welches Tür-5-Häppchen zuletzt schon lief (Story Fr/So **und** Feed), damit sich **kein Geschichts-Häppchen wiederholt**.

Memory mitnehmen: `feedback_katja_ist_raus`, `feedback_nicht_faceless`, `feedback_persoenlich_reel_tuer5`, `feedback_no_generic`, `feedback_einfach_verstaendlich`, `feedback_hook_kalter_traffic`, `feedback_caption_kurz_am_hook`, `feedback_cta_passend_freebie`, `feedback_reel_kein_caption_verweis_cta`, `feedback_notion_alt_hooks`, `feedback_alt_hooks_immer`.

---

## Schritt 2 — Format + Häppchen bestimmen

**Tür ist immer Tür 5 (Deine Geschichte).** Keine andere Tür wählen — die leben in den Stories. Wenn Katja nach einer Alltags-Tür (ehrlicher Zwischenstand, Rückkehr in den Körper, echtes Leben, Stimme/Audio) für ein Feed-Stück fragt: **nicht als Feed-Piece bauen**, sondern auf `/story persoenlich` bzw. `/story-woche` verweisen. (Bringt eine Ausbildungs-/Yoga-Erkenntnis echten Lehr-Wert, ist das kein persönliches Stück, sondern normaler Nische-Content → `/karussell-einstieg` oder `/karussell-uebung`.)

**Format erkennen** (aus $ARGUMENTS):
- `reel` → Reel (Default, wenn nichts genannt ist)
- `karussell` → Karussell (Geschichte über Slides — starke Alternative, gut für einen längeren Bogen)

**Häppchen wählen:** Deine Geschichte ist nicht ein Monolog, sondern wird **getropft** — ein Moment/Winkel pro Piece. Aus `context/founder-story.md` ein Häppchen ziehen, das **anders ist als zuletzt** (Feed + Story Fr/So abgleichen, siehe Verlauf + Notion). Beispiele für Winkel: der Wendepunkt · „von außen sah alles gut aus" · „ich dachte, ich brauch mehr Durchhalten" · der erste kleine Schritt raus · was sie heute draußen hält.

**Wochen-Rhythmus:** Tür 5 als Feed-Piece läuft **1× pro Woche**. Da sie zusätzlich an Fr/So als Story-Einstieg vorkommt, hier immer ein **anderes Häppchen** als zuletzt in den Stories.

---

## Schritt 3 — Bauen

### Wenn Reel
Folge der **Output-Struktur aus `.claude/commands/reel.md`** (Reel-Text · Thumbnail-Hook/Reelcover · Caption · B-Roll · 5 Hashtags · Story-Sequenz · DM-Antwort wenn nötig) — **mit diesen Abweichungen für persönlichen Content:**
- **KEINE Grundformel-Pflicht.** Die 4 Grundformeln aus `reel.md` gelten nur fürs Funktionsmodus-Erkennungs-Format. Hier trägt ein **persönlicher Hook** aus der Geschichte (ihre Wahrheit, ihr Moment).
- **Hook = psychologischer Auslöser, kein netter Satz (Pflicht — `reference/hook-formel.md` + Memory `feedback_starker_hook`):** Jeder Hook trägt **≥ 2 von 3 Mechanismen** (Neugier-Lücke · Pattern Interrupt · emotionale Erkennung) und besteht den **Auflöse-Test**: Kann man ihn lesen, „ja stimmt" denken und weiterscrollen → schwach, neu bauen. Muss man weiterschauen, um die Spannung aufzulösen → stark. Konkret schlägt vage (Zahl/Bild/gefühlter Moment), Reiz ganz vorne (~1 Sek). Negativbeispiel: „Halb drei. Ich komm aus dem Büro." — wahr, aber kein Stopper.
- **Hook sichtbar machen (Pflicht, Katja-Wunsch 2026-06-30):** Den Hook **als Zeile 1 klar kennzeichnen** („HOOK (Zeile 1, der Stopper):"). Beide Reel-Versionen starten mit genau dieser Hook-Zeile; die 2 Alt-Hooks unten **ersetzen ebendiese Zeile 1** (zum Tauschen). Nicht den Hook unmarkiert im Fließtext verstecken — Katja muss auf einen Blick sehen, was der Scroll-Stopper ist.
- **IMMER ZWEI FORMAT-VARIANTEN liefern** (Katja-Wunsch 2026-06-30, Pflicht) — Katja wählt je nach Zeit/Energie spontan:
  - **Variante A — Text im Reel:** der Text trägt das Video auch stumm. Knappe, lesbare On-Screen-Beats (kurz, schnell produzierbar — Katjas Notfall-/Stresstag-Variante). Katja ist trotzdem im Bild (B-Roll mit ihr), Text als Overlay.
  - **Variante B — Voiceover:** Katja spricht den Text als Voiceover ein (warm, persönlich, baut Vertrauen), sie ist im Bild, **Untertitel laufen mit** (viele schauen stumm). Der Text darf hier flüssiger/voller sein — so, wie sie ihn laut sagen würde.
  Beide starten mit **demselben Hook als Zeile 1**. Ehrlicher Ich-Einstieg statt Klammersatz; keine feste Beat-Zahl (die „3 Beats" gelten nur fürs Funktionsmodus-Reel). **Katja ist immer im Bild** — nie „faceless". (Talking Head / direkt in die Kamera ist ein späterer Schritt, noch nicht Standard.)
- **Positionierung (Pflicht):** Katja **ist raus** aus dem Funktionsmodus und führt von der anderen Seite — glaubwürdig, weil sie es gelebt hat UND sich ihren Weg täglich hält (Yoga, Atmen, Pausen). **Nie „ich bin selbst noch nicht raus / noch mittendrin"** (Memory `feedback_katja_ist_raus`).
- **Caption:** nicht mit derselben Zeile wie das Reel starten; kurz und am Hook bleiben; endet bei ihr (die „zurück zu ihr"-Regel). Kein Yoga-Verkaufsabsatz.
- Kein On-Screen-CTA, kein „steht in der Caption" (Memory `feedback_reel_kein_caption_verweis_cta`).

### Wenn Karussell
Folge der **Slide-/Output-Struktur aus `.claude/commands/karussell-einstieg.md`** (Cover-Hook → Aufbau → Erkenntnis → CTA · Caption · 5 Hashtags · Story-Sequenz), aber **als persönliche Erzählung** statt Teach: deine Geschichte über die Slides, Häppchen für Häppchen, mit einer leisen Wendung/Erkenntnis hinten. Kein Freebie-Zwang, kein ANKOMMEN-CTA per Default. Gleiche Positionierung (du bist raus) und „zurück zu ihr" am Ende.

### Für beide Formate (Pflicht)
- **Zurück zu ihr** am Ende — nie reines Tagebuch.
- Leitplanken aus `reference/persoenlicher-content.md`: kein Oversharing, keine abgehobene Guru-Story, leise Wahrheit, einfache Alltagssprache.
- **Tochter kommt nicht vor** (Memory `feedback_tochter_kein_content`).

### CTA bewusst wählen
Persönlicher Content baut Beziehung, nicht Funnel (siehe `reference/persoenlicher-content.md` → CTA-Logik):
- Default: leiser **Folgen**-Grund („bleib hier / folg mir, wenn du auch leise rauswillst — ohne dich noch mehr zu optimieren").
- **Kein reflexhaftes „Speichern".** Freebie-CTA nur ausnahmsweise und ganz leise.

---

## Schritt 3.5 — Die 3 Hooks = die 3 Formen (Pflicht)

Immer **3 Hooks** liefern (1 Haupt als Zeile 1 + 2 Alt zum Tauschen) — und die **3 nutzen je eine der drei Formen** (Katja-System 2026-06-30, `reference/hook-formel.md` + Memory `feedback_starker_hook`):

1. **Confession** — ehrliche, überraschende, konkrete Beichte, **IMMER mit einer Zahl/konkreten Größe** (Jahre, Häufigkeit, Anzahl) — Pflicht für diese Form.
2. **Widerspruch** — zwei Dinge hart nebeneinander, die nicht zusammenpassen (Pattern Interrupt).
3. **Das Unausgesprochene** — was keiner sagt, die unbequeme Wahrheit; **Einstieg variieren, nicht immer „Keiner sagt dir…"** (z. B. „Niemand warnt dich, dass…", „Worüber keiner spricht: …", „Das, was mir keiner gesagt hat: …").

Jeder der 3 trägt ≥ 2 Mechanismen und besteht den Auflöse-Test. **Beim Ausgeben jeden Hook mit seiner Form labeln** (Confession / Widerspruch / Unausgesprochenes), damit Katja den Mechanismus sieht. Nie 3× dieselbe Form oder derselbe Opener. Die 2 nicht gewählten kommen als Alt-Hooks mit in die Notion-Ablage (`feedback_notion_alt_hooks`, `feedback_alt_hooks_immer`).

---

## Ausgabe-Format

```
TÜR 5 (Deine Geschichte) · FORMAT: [Reel / Karussell] · HÄPPCHEN: [kurzer Winkel]

— dann die vollständigen Outputs des gewählten Formats —
(Reel: HOOK (Zeile 1) · Variante A Text im Reel · Variante B Voiceover (+ Untertitel) · Reelcover · Caption · B-Roll · 5 Hashtags · Story-Sequenz · DM-Antwort wenn nötig)
(Karussell: Slides · Caption · 5 Hashtags · Story-Sequenz · DM-Antwort wenn nötig)

DIE 3 HOOKS (je eine Form, ersetzen Zeile 1 zum Tauschen):
1. [Confession] …
2. [Widerspruch] …
3. [Das Unausgesprochene] …
(Haupt-Hook = einer der drei, oben als Zeile 1 gesetzt)
```

Nach der Ausgabe: kurz fragen, ob Hook, Format, Häppchen oder Caption angepasst werden sollen.

---

## Notion (nur auf Abnahme)

Erst wenn Katja abnimmt („passt so" / „perfekt") → in DB „Feed" (`33a8aca2-e91e-81af-8577-000b691410f4`), wie aller Feed-Content (Memory `notion_content_workflow`). **Content-Säule = „Persönlich"** (die eigene Säule existiert jetzt). **Die 2 Alt-Hooks mit in die Seite.** Nie ungefragt ablegen.

---

## Nicht tun

- **Nicht** eine andere Tür als Tür 5 fürs Feed bauen — die anderen 5 Türen sind Stories (`/story persoenlich`, `/story-woche`).
- **Nicht** die Funktionsmodus-Grundformeln als Hook erzwingen — das ist hier das falsche Format.
- **Nicht** reines Tagebuch ohne Anschluss zur Soul-Client.
- **Nicht** „ich bin selbst noch nicht raus / noch mittendrin" — FALSCH und widerspricht dem Coachen/Verkaufen. Katja IST raus aus dem Funktionsmodus; sie führt von der anderen Seite und hält sich ihren Weg täglich (Yoga, Atmen, Pausen). Glaubwürdig durch gelebte Erfahrung, nicht durch Noch-Feststecken. Genauso wenig die abgehobene „bei mir ist alles für immer perfekt"-Guru-Story.
- **Nicht** „faceless" annehmen — Katja ist im Bild.
- **Nicht** Oversharing, nicht Details über Dritte ohne deren Okay.
- **Nicht** reflexhaft „Speichern" als CTA, **nicht** ungefragt ein Freebie pushen.
- **Nicht** nach KI klingen, **nicht** generisch, **nicht** poetisch/verkopft.
