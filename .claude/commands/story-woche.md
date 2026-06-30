# Story-Woche

> Komplette Wochen-Produktion für Instagram-Stories: 7 Tage (Montag–Sonntag) fertige, copy-fertige Story-Frames — Text, Sticker, B-Roll-Hinweis, Link wo nötig. Einmal laufen lassen (z. B. Sonntagabend), ganze Woche fertig. **Katja ist sichtbar** (Foto/Video/Gesicht/Stimme); B-Roll + Text-Overlay sind ein zusätzliches Frame-Format, kein Ersatz für ihre Präsenz — nie „faceless" annehmen.

Läuft auf Zuruf, nicht automatisch. Inhalte wählt Claude selbst — **frisch je Lauf, nie wiederholt, immer spezifisch** (nie generisch).

**Das tragende Prinzip: 70/30.** 5 Tage verkaufsorientiert (echte Verkaufsstory-Vorlagen) + 2 Tage reine Verbindung. Die Verkaufstage orientieren sich IMMER an den ausgearbeiteten **Verkaufsstory-Vorlagen** (`reference/stories-verkaufen.md` + Notion-DB „Verkaufs-Stories"). Struktur der Vorlagen bleibt — **der Inhalt wird jede Woche komplett neu geschrieben** (nie zweimal derselbe Mythos, dieselbe Q&A usw.).

---

## Variablen

eingabe: $ARGUMENTS  *(optional — z. B. „ohne harten pitch" oder „start am dienstag"; sonst Standard-Woche)*

---

## Was am Ende rauskommt

- **7 Tage** (Mo–So): **5 Verkaufstage** (je eine Verkaufsstory-Vorlage im vollen Format) + **2 Verbindungstage** (kein Verkauf).
- Pro Frame: **Text** (fertig zum Tippen/Overlay), **Sticker-Anweisung**, kurzer **B-Roll-/Hintergrund-Hinweis**, an Verkaufstagen der **richtige Link / das Keyword**.
- Komplett frischer Inhalt: neuer Mythos, neue Q&A, neuer BTS-Moment, neue persönliche Story usw. — nichts aus der Vorwoche, auch nicht leicht umformuliert.
- An Keyword-Tagen die passende **DM-Antwort** mitliefern.
- Kurzer Wochen-Überblick am Ende (Tag → Format → Ziel/Angebot).

---

## Schritt 0 — Kontext laden (Pflicht, jeder Lauf)

Lies zuerst, damit Stimme, Nische und Verkaufslogik sitzen:
- `context/soulclient.md` — die funktionierende Frau 40+ (das „Wer")
- `reference/zielgruppe-workbook.md` — **das „Was löse ich / was will sie / gelebter Wunschzustand"** (Quelle für Hooks, Mythen, Winkel — über morgens/mittendrin/abends, nicht nur abends)
- `reference/stories-verkaufen.md` — **das Verkaufsstory-System: die Vorlagen-Strukturen + Ton-Regeln fürs Verkaufen** (das „Wie verkaufe ich")
- `context/brand-voice.md` — Tonalität, Power-Words, **verbotene Wörter**, Satzrhythmus
- `reference/story-aufbau.md` — was eine gute Story trägt (Abbruch-Kurve, Frame-1-Regel, Sticker-Hebel, DM-vor-Link)
- `reference/persoenlicher-content.md` — die 6 Türen + Leitplanken für die menschliche Schicht
- Notion-DB **„Verkaufs-Stories"** (`data_source_id` `29fc89c3-46e1-4145-bcea-9fdce5244392`) — die fertigen Vorlagen je Typ als Struktur-Referenz (Inhalt NICHT kopieren, neu schreiben)
- `~/.claude/projects/-Users-katjajung-claude-workspace-vorlage/memory/feedback_content_niche.md` — Nische
- `~/.claude/projects/-Users-katjajung-claude-workspace-vorlage/memory/feedback_no_generic.md` — nichts darf generisch klingen
- `~/.claude/projects/-Users-katjajung-claude-workspace-vorlage/memory/feedback_tageszeit_abwechslung.md` — Tageszeit rotieren, auch 3–5-Min-Auszeiten tagsüber
- `~/.claude/projects/-Users-katjajung-claude-workspace-vorlage/memory/feedback_cta_passend_freebie.md` — welches Freebie wann + abwechseln
- `~/.claude/projects/-Users-katjajung-claude-workspace-vorlage/memory/project_freebie_inventory.md` — welches Freebie/Angebot live ist (Links/Keywords)
- `~/.claude/projects/-Users-katjajung-claude-workspace-vorlage/memory/feedback_content_story_dm.md` — DM-Antwort, wo Keyword-Mechanik
- `outputs/story-woche/verlauf.md` — **was die letzten Wochen schon dran war** (welches Format auf welchem Tag, welche Mythos-/Q&A-/Story-Themen, welche Angebote, Sticker, Tageszeiten, Winkel, persönliche Türen). Existiert die Datei nicht → erster Lauf, neu anlegen. **Die letzten 2–3 Einträge lesen und bewusst ANDERS bauen** (siehe Rotations-Regel).

**Harte Leitplanken (nicht verhandelbar):**
- Nur **Funktionsmodus** + **einfache Yoga-/Atemimpulse**. NIEMALS „Nervensystem", „Vagusnerv", „Regulation", Fachsprache.
- Verbotene Marken-Wörter: High Performance, Disziplin, Challenge, Transformation, Selbstoptimierung, Selfcare, „du musst nur", „Zeit für dich nehmen" u. Ä. **Auch nicht per Verneinung.**
- Verkaufs-Ton (aus `reference/stories-verkaufen.md`): **Mechanismus nutzen, kein Hype.** Raus: „🔥 BRANDNEU", „krasseste Erkenntnis", FOMO-Countdown ohne echte Deadline. Rein: Wiedererkennung + ruhiger Konter, klare Ansage, DM-Weg, Versprechen immer gespürt-körperlich, nie Leistung. Mehr Verkaufs-Zug ist gewollt, Hype nicht.
- **Kein Satz darf nach KI klingen.** Keine Floskeln, kein gleichförmiger Rhythmus, keine „Das ist nicht X, sondern Y"-Masche.
- **Einfache, normale Alltagssprache.** So, wie Katja zu einer Freundin spricht. Test je Satz: Würde sie das genau so laut sagen?
- Geduzt. Kein Emoji im Frame-Text, außer Katja gibt eines vor (Emojis nur in Sticker-/Hinweis-Zeilen).
- Kein Caption-Verweis, kein „Link in der Caption" (Stories haben keine Caption) — CTAs über Keyword/Link-Sticker.

---

## Die Wochenstruktur — 70/30

**5 Verkaufstage + 2 Verbindungstage.** Verteilung so, dass es nie monoton wird:

- **Max. 2 Verkaufstage am Stück** — die 2 Verbindungstage brechen die Woche auf (z. B. Verbindung auf Mi + Sa, oder Di + Sa … die Platzierung jede Woche variieren).
- **Höchstens 1–2 harte Pitches pro Woche** (klarer Produkt-CTA). Die restlichen Verkaufstage sind **weich**: Wert/Erkennung mit sanftem CTA. Zwei harte Produkt-Pitches **nie an aufeinanderfolgenden Tagen**.
- **Angebote durchwechseln:** alle 4 Freebies (RESET · 3MINUTEN · NACHTRUHE · Funktionsmodus-Check) + das Produkt (10-Minuten-Rückkehr). **Kein Keyword zweimal in derselben Woche.** Über Wochen hinweg fair rotieren.
- **Telegram-Gruppe** zählt NICHT als echter Verkaufstag (kein Pitch) — kann aber als weiche Community-Einladung auf einem der Verbindungstage vorkommen.

Die **Tag→Format-Zuordnung wechselt jede Woche** — die Woche startet NICHT immer mit demselben Format (nicht jeden Montag Mythos). Siehe Rotations-Regel.

---

## Die 5 Verkaufstage — Vorlagen-Pool

Jeder Verkaufstag nutzt **eine** dieser ausgearbeiteten Vorlagen im **vollen Format** (Struktur aus `reference/stories-verkaufen.md` / Notion-DB). **Pro Woche 5 verschiedene auswählen**, Tag-Zuordnung rotieren:

1. **Mythos aufdecken** — Ansprechen (Umfrage) → Fakt/kippen → Beweis → was ohne den Mythos geht → CTA
2. **Fragen & Antworten + Mini-Impuls** — Fragesticker → Frage + Mini-Impuls (echter Mehrwert) → warum es wirkt → Beweis/Herausforderung → CTA
3. **Behind the Scenes** — Opener/Tagesablauf → Problem beschreiben → konkretisieren / wie ich arbeite → Ansprache + CTA
4. **Persönliche Story** — Opener → wie es vorher war → Wendepunkt → wie es heute ist → CTA (trägt zugleich die menschliche Schicht)
5. **1-teilige Verkaufs-Story** — kurz, 1–2 Frames: Hook am konkreten Moment → CTA
6. **Erzähl-Bogen** — Slide 1 (Umfrage) → Wendepunkt → neuer Weg → CTA („fast aufgegeben" / „alles probiert" / „was niemand sah" / „nie getraut")
7. **Fallstudie** — Thema/Umfrage → Vorher → Herausforderung → Ergebnis (echter Screenshot) → ohne-Aufwand → CTA. **Nur einsetzen, wenn ein echtes Kunden-Ergebnis vorliegt** — sonst auslassen, nichts erfinden.

**Struktur bleibt, Inhalt jede Woche neu:** Nie denselben Mythos, dieselbe Q&A-Frage, denselben BTS-Moment, dieselbe persönliche Story wie in den letzten Wochen (laut `verlauf.md`). Jede Woche neues Thema/neuer Winkel aus `reference/zielgruppe-workbook.md`.

---

## Die 2 Verbindungstage — Pool (kein Verkauf, auch rotieren)

Reine Beziehung/Interaktion, **kein CTA**, kein Keyword. **Auch hier abwechseln** — nicht immer This-or-that + Quiz:

- **This-or-that** („Wie kommst DU am ehesten runter?")
- **Echtes Leben + Quiz** (kleiner privater Moment + leichtes Quiz)
- **Frage in die Runde** (offene Frage-Box, leicht aus dem Alltag beantwortbar)
- **Stimmungs-Slider** (Emoji-/Skala-Slider, „Wie voll ist dein Akku gerade?")
- **Kleiner BTS-privat-Moment** (Tochter, Spaziergang, Buch, langsamer Morgen) → warme Reaktion
- **Lieblingsding/Moment teilen** + Foto-Antwort-Sticker
- **Telegram-Community-Einladung** (weich, als Beziehung, kein Verkaufsdruck)

Pro Woche **zwei verschiedene** wählen, nie dieselben zwei wie zuletzt.

---

## Rotations-Regel (das Herz gegen Langeweile — nicht verhandelbar)

Jede Woche muss sich **komplett anders anfühlen** als die Vorwoche. Vor dem Bauen `verlauf.md` lesen und bewusst variieren:

1. **Tag→Format-Zuordnung** — welches Verkaufsformat auf welchem Tag liegt, jede Woche anders. **Die Woche startet nie zweimal mit demselben Format.**
2. **Welche 5 Verkaufsformate** — über Wochen durch den Pool rotieren, nicht jede Woche dieselben 5.
3. **Inhalt jeder Vorlage neu** — neuer Mythos (anderes Thema), neue Q&A-Frage + anderer Mini-Impuls, neuer BTS-Moment, neue persönliche Story / anderer Erzähl-Bogen. Struktur bleibt, Text wird komplett neu geschrieben. Nie ein Thema aus den letzten 2–3 Wochen.
4. **Angebot/Keyword** — alle Freebies + Produkt durchwechseln, kein Keyword 2× in der Woche, über Wochen fair verteilen.
5. **Verbindungstage** — zwei andere Formate als zuletzt.
6. **Sticker** — Umfrage, Quiz, This-or-that, Frage-Box, Emoji-Slider, Skala-Slider, Link, „Frag mich was", Foto-Antwort durchwechseln. **Polls/Umfragen/This-or-that max. 2–3×/Woche.** Nie dieselbe Sticker-Art jeden Tag.
7. **Tageszeit** — morgens / Vormittag / Mittag (3-Min-Auszeit!) / Nachmittag / Feierabend / abends über die Woche verteilen; nicht jede Woche dasselbe Muster, nicht alles auf den Abend.
8. **Winkel/Moment** — aus `reference/zielgruppe-workbook.md`, je Tag ein anderer konkreter Alltagsmoment.

**Test vor dem Abschicken:** Würde Katja denken „das hatte ich letzte Woche so ähnlich"? Wenn ja → neu. Am Ende alle Picks in `verlauf.md` festhalten.

---

## Angebote, Keywords & Links (richtig verlinken)

- **Produkt — 10-Minuten-Rückkehr (17 €):** Keyword **RÜCKKEHR** (manueller DM) oder Link-Sticker `10-minuten-rueckkehr.katjajung.com`. **NIE zur Kasse.** 7-€-Tripwire bleibt Freebie-exklusiv, kommt NICHT in Stories.
- **Freebies (Auto-DM):** Erkennung/Funktionsmodus → **7ZEICHEN** (bzw. **CHECK**, solange 7ZEICHEN nicht live) · kurze Spür-Übung tagsüber → **3MINUTEN** · Abend/Feierabend abschalten → **RESET** · Einschlafen/Kopf-aus → **NACHTRUHE**.
- **Timing (Stand 2026-06-27):** Die Auto-DM-Flows für RESET, 3MINUTEN, NACHTRUHE, 7ZEICHEN gehen **ab 28.06.** live. Davor diese Keywords nicht nutzen → Funktionsmodus-Tag auf **CHECK** (läuft schon) ziehen, andere Freebie-Tage auf RÜCKKEHR/Link. Beim Lauf kurz gegen `project_freebie_inventory.md` prüfen, was live ist.
- **Nie zwei Keywords in einer Story** (ManyChat-Flow). Keyword im Post exakt zum Trigger.
- **DM-Antwort:** Bei Keyword-Mechanik je Tag eine kurze, warme DM-Antwort mitliefern (Begrüßung → Link → ein ehrlicher Satz). Nie generisch.

---

## Menschliche Schicht (die Frau hinter der Marke)

Persönliches ist keine eigene Story, sondern läuft **durch die Woche** mit — vor allem über den **Persönliche-Story-Verkaufstag** und die **Verbindungstage**, dazu kleine persönliche Sätze, wo sie passen. Quelle: `reference/persoenlicher-content.md` (die 6 Türen).

- Über die Woche **verschiedene Türen** anklingen lassen (ehrlicher Zwischenstand · eigene Rückkehr in den Körper · die Ausbildung · echtes Leben · das Warum · Gesicht & Stimme), rotierend, nie dasselbe Häppchen wie zuletzt.
- **Pflicht — zurück zu ihr:** Jeder persönliche Moment endet bei der Soul-Client („… und vielleicht kennst du das auch"), nie reines Tagebuch, kein Oversharing, keine Guru-Story.
- Nicht erzwungen-formelhaft auf alle 7 Tage stempeln — dort einbauen, wo es echt wirkt, und die Türen über die Wochen variieren.

---

## Story-Mechanik (aus der Marktrecherche — fest eingebaut)

- **Ein Tag = ein Ziel.** An Verkaufstagen nie mehrere Angebote mischen. Eine Handlung.
- **Kurz halten, Bestes zuerst.** Pro Tag selten mehr als 4 Frames (Verkaufsformate 4–5 Frames, Verbindung 1–2). Frame 1 entscheidet, ob jemand bleibt.
- **Interaktion ist der Hebel:** jeden Tag genau ein klares Interaktions- oder Bindungs-Element (Sticker/CTA). Niedrigschwellige Sticker (Emoji-Slider) bringen früh Antworten → Algo-Schub.
- **Ein bewusster Weiterleitungs-Moment pro Woche** (Sends sind ein Top-Signal) — „Schick das einer Frau, die gerade auch nur funktioniert."
- **Katjas Bildwelt:** ein Mix aus Frames mit ihr (Foto/Video/Gesicht/Stimme) und ruhiger B-Roll + Text-Overlay — sie ist sichtbar, B-Roll ist Ergänzung, nicht Ersatz. Katjas Sandbeige/Creme-Welt (#D8C7B2 / #F4EFE7), Tageslicht, ruhige Settings.
- **Posten am besten abends 18–22 Uhr** (die Feierabend-Frau). Hinweis am Ende einmal mitgeben.

---

## Spezifisch statt generisch — der wichtigste Test

Jeder Frame muss an einem **konkreten, schmalen Moment** der Soul-Client hängen.
- Generisch (verboten): „Gönn dir Ruhe", „Selbstfürsorge ist wichtig", „Atme tief durch".
- Spezifisch (so): „Der Moment im Auto, in dem du kurz nicht aussteigen willst.", „Mittags zwischen zwei Terminen, und du merkst, du hast seit Stunden nicht durchgeatmet."
- Vor dem Schreiben gegen die Soul-Client halten: Würde **sie** beim Durchtippen kurz innehalten und denken „das bin ich"? Wenn nicht — verwerfen.

---

## Ausgabe-Format

Pro Tag ein klarer Block — Verkaufs- oder Verbindungstag gekennzeichnet, mit Format, Tageszeit und (an Verkaufstagen) Angebot:

```
### MONTAG · 🟢 Verkauf · Mythos · morgens → RESET (Freebie)

**Frame 1 — Ansprechen**
[Frame-Text, copy-fertig]
🟫 Hintergrund: [B-Roll-Hinweis]
🎯 Sticker: Umfrage — „[Option A]" / „[Option B]"

**Frame 2 — Fakt**
[Frame-Text]
…
**Frame 5 — CTA**
[Frame-Text]
🔗 Link-Sticker: [URL]  /  Keyword: „RESET"
```

An Verkaufstagen mit Keyword die **DM-Antwort** separat darunter. Verbindungstage mit `⚪ Verbindung` kennzeichnen.

**Am Ende des ganzen Laufs:** Wochen-Überblick (Tabelle Tag → Format → Ziel/Angebot) + Verteilungs-Check (5/2, max. 2 Verkauf am Stück, Pitches nicht nebeneinander, kein Keyword doppelt) + Hinweis „Am besten abends 18–22 Uhr posten."

**Verlauf festhalten (Pflicht):** Neuen Eintrag **oben** in `outputs/story-woche/verlauf.md` (Datei anlegen, falls nicht vorhanden) — mit Lauf-Datum und je einer Zeile: **Tag→Format-Zuordnung**, **Verkaufsstory-Themen** (welcher Mythos/welche Q&A/welcher BTS-Moment/welche Story-Tür/welcher Erzähl-Bogen), **Angebote/Keywords**, **Verbindungs-Formate**, **Sticker-Arten**, **Tageszeiten**, **Winkel/Momente**, **persönliche Türen**. Kurz, stichpunktartig — nur damit der nächste Lauf weiß, was zu meiden ist und was anders sein muss.

**Danach:** kurz fragen, ob ein Tag angepasst werden soll.

---

## Nicht tun

- **Nicht** nach Notion ablegen, außer Katja nimmt ausdrücklich ab („passt so" / „perfekt"). Dann in die DB „Story Highlights & Stories" (`150c2b99-75fe-4478-94c4-ed52407136ae`) als **EINE Seite pro Woche**: Titel „Story-Woche TT.–TT.MM.JJJJ", Typ „Story (Einzel)", Status „Fertig". Alle 7 Tage Mo→So untereinander als **ganz normaler Text** (Tag-Überschrift + Frame-Text + 🟫/🎯/🔗-Hinweise). **NIE** 7 Einzel-Zeilen, **NIE** als Tabelle (echte Zeilenumbrüche). Connector kann nicht löschen → Aufräumen macht Katja. Details: Memory `feedback_story_woche_notion_format`.
- **Nicht** denselben Mythos / dieselbe Q&A / denselben BTS-Moment / dieselbe Story wie in den letzten Wochen (laut `verlauf.md`) — Struktur bleibt, Inhalt IMMER neu.
- **Nicht** die Woche zweimal mit demselben Format starten; **nicht** dieselbe Tag→Format-Zuordnung wie zuletzt.
- **Nicht** mehr als 1–2 harte Produkt-Pitches/Woche, **nie** zwei nebeneinander. **Nicht** mehr als 2–3 Polls/Woche. **Nicht** zwei Angebote in einen Tag.
- **Nicht** das Angebot falsch verlinken (Freebie → Auto-DM-Keyword/Opt-in · Produkt → Verkaufsseite, nie Kasse · 7-€-Tripwire nie öffentlich). **Nicht** ein Keyword nutzen, dessen Flow noch nicht live ist.
- **Nicht** vergessen, am Ende den Verlauf-Eintrag zu schreiben.
- **Nicht** generisch, nicht belehrend, nicht antreibend, kein Hype.
