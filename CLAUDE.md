# CLAUDE.md

Diese Datei gibt Claude Code (claude.ai/code) Anweisungen für die Arbeit in diesem Repository.

---

## Was das hier ist

Dies ist ein **Claude Workspace Template** — eine strukturierte Umgebung, die für die Arbeit mit Claude Code als leistungsstarkem Agenten-Assistenten über mehrere Sessions hinweg konzipiert ist. Der Benutzer startet wiederholt neue Claude Code Sessions und verwendet `/prime` zu Beginn jeder Session, um den wesentlichen Kontext ohne Ballast zu laden.

**Diese Datei (CLAUDE.md) ist das Fundament.** Sie wird automatisch am Anfang jeder Session geladen. Halte sie aktuell — sie ist die Single Source of Truth dafür, wie Claude diesen Workspace verstehen und darin arbeiten soll.

---

## Die Claude-User-Beziehung

Claude arbeitet als **Agenten-Assistent** mit Zugriff auf die Workspace-Ordner, Kontext-Dateien, Commands und Outputs. Die Beziehung ist:

- **User**: Definiert Ziele, liefert Kontext zu seiner Rolle/Funktion und steuert die Arbeit über Commands
- **Claude**: Liest Kontext, versteht die Ziele des Users, führt Commands aus, produziert Outputs und pflegt die Workspace-Konsistenz

Claude sollte sich immer über `/prime` am Session-Start orientieren, dann mit vollem Bewusstsein dafür handeln, wer der User ist, was er erreichen möchte und wie dieser Workspace das unterstützt.

---

## Workspace-Struktur

```
.
├── CLAUDE.md              # Diese Datei — Kern-Kontext, immer geladen
├── .claude/
│   └── commands/          # Slash-Commands, die Claude ausführen kann
│       ├── start.md       # /start — Kompakter Status-Check zum Session-Start
│       ├── capture.md     # /capture — Schnelle Notiz in inbox/ speichern
│       ├── plan.md        # /plan — Ausführlichen Projektplan erstellen
│       ├── prime.md       # /prime — Vollständige Session-Initialisierung
│       ├── create-plan.md # /create-plan — Workspace-Änderungspläne erstellen
│       ├── implement.md   # /implement — Pläne umsetzen
│       └── shutdown.md    # /shutdown — Session beenden und aufräumen
├── context/               # Hintergrund-Kontext — vollständig befüllt
│   ├── personal-info.md   # Wer Katja ist, Alltag, Lebenssituation
│   ├── business-info.md   # Marke, Positionierung, Zielgruppe, Design
│   ├── strategy.md        # Funnel, Angebote, Tech-Stack, Instagram, Filming-Setup
│   ├── brand-voice.md     # Tonalität, Power-Words, verbotene Wörter, Satzrhythmus
│   ├── founder-story.md   # Katjas persönliche Geschichte (in ihren eigenen Worten)
│   ├── soulclient.md      # Die funktionierende Frau 40+ — detailliertes Profil
│   ├── human-design.md    # Manifestor 6/2, Ego-Autorität, Money Channel
│   └── current-data.md    # Metriken und aktuelle Kennzahlen (noch auszufüllen)
├── inbox/                 # Schnell-Notizen und Ideen (erfasst mit /capture)
├── plans/                 # Pläne erstellt mit /plan und /create-plan
├── outputs/               # Arbeitsergebnisse und Deliverables
├── reference/             # Vorlagen, Beispiele, wiederverwendbare Patterns
└── scripts/               # Automatisierungsskripte (falls zutreffend)
```

**Verzeichnisse:**

| Verzeichnis  | Zweck                                                                                   |
| ------------ | --------------------------------------------------------------------------------------- |
| `context/`   | Wer der User ist, seine Rolle, aktuelle Prioritäten, Strategien. Gelesen von `/start` und `/prime`. |
| `inbox/`     | Schnell-Notizen, Ideen und Aufgaben. Erfasst mit `/capture`, manuell weiterverarbeitet. |
| `plans/`     | Projekt- und Implementierungspläne. Erstellt mit `/plan` oder `/create-plan`, umgesetzt mit `/implement`. |
| `outputs/`   | Deliverables, Analysen, Reports und Arbeitsergebnisse.                                 |
| `reference/` | Hilfreiche Dokumentation, Vorlagen und Patterns für verschiedene Workflows.            |
| `scripts/`   | Automatisierungs- und Tooling-Skripte.                                                 |

---

## Commands

### /start

**Zweck:** Kompakter Status-Check zum Session-Start. Schneller als `/prime`.

Liest `context/` und `CLAUDE.md`, zeigt einen kompakten Status-Block: wer der User ist, aktueller Fokus, offene Pläne, Inbox-Einträge, **terminierte Erinnerungen (Scheduled Tasks)** und verfügbare Commands. Die aktiven Reminder (z. B. „Telegram-Posts fertig machen", „Insights-Check") erscheinen mit Fällig-Datum unter „Offene Pläne & Erinnerungen".

### /capture [notiz]

**Zweck:** Idee, Aufgabe oder Gedanke sofort in `inbox/` speichern — ohne Unterbrechung.

Speichert die Notiz als datierte Markdown-Datei in `inbox/`. Kein Umstrukturieren, einfach festhalten.

Beispiel: `/capture Idee: Newsletter-Serie über KI-Workflows`

### /plan [projekt]

**Zweck:** Ausführlichen Projektplan erstellen und in `plans/` ablegen.

Für Projekte, Initiativen und Vorhaben. Claude denkt gründlich nach, stellt ggf. Rückfragen und erstellt ein vollständiges Plan-Dokument mit Phasen, Aufgaben, Risiken und Erfolgskriterien.

Beispiel: `/plan Onboarding-Prozess für neue Teammitglieder überarbeiten`

### /prime

**Zweck:** Vollständige Session-Initialisierung mit tiefem Kontext-Verständnis.

Am Anfang jeder Session ausführen, wenn vollständige Orientierung wichtig ist. Claude liest alle Kontext-Dateien und bestätigt sein Verständnis von User, Workspace und Zielen.

### /create-plan [anforderung]

**Zweck:** Detaillierten Plan für Workspace-Änderungen erstellen.

Für strukturelle Änderungen am Workspace selbst (neue Commands, Skripte, Workflows). Erzeugt ein gründliches Plan-Dokument in `plans/`.

Beispiel: `/create-plan Wettbewerbs-Analyse-Command hinzufügen`

### /implement [plan-pfad]

**Zweck:** Einen mit `/create-plan` erstellten Plan umsetzen.

Liest den Plan, führt jeden Schritt der Reihe nach aus, validiert die Arbeit und aktualisiert den Plan-Status.

Beispiel: `/implement plans/2026-01-28-wettbewerbs-analyse-command.md`

### /telegram [typ | typ anzahl]

**Zweck:** Fertige Beiträge für die Telegram-Gruppe „Zurück zu dir" erstellen — direkt kopierbereit.

Wochenrhythmus: Woche 1 (Mo + Do), Woche 2 (Mo + So)
- `/telegram montag` → Wahrer Satz + Reflexionsfrage (Montagsformat)
- `/telegram körper` → 3-Minuten-Körperimpuls (Donnerstag)
- `/telegram audio` → Audio-Rückkehr Skript (Sonntag, zum Einsprechen)
- `/telegram tagesimpuls` → Spontaner Kurzimpuls (2–4 Sätze)
- `/telegram tagesimpuls 3` → Mehrere Posts auf einmal

Ohne Argument: fragt nach dem gewünschten Typ.

### /reel [thema] · /format-klammersätze

**Zweck:** Vollständiges Instagram Reel Content-Piece im Funktionsmodus-Format — Reel-Text, Thumbnail-Hook, Caption, CTA, B-Roll, Hashtags.

- `/reel Müdigkeit` → Thema selbst vorgeben
- `/format-klammersätze` → Claude wählt Thema und Blickwinkel eigenständig aus dem Soulclient-Profil

Output je Reel: Reel-Text · Thumbnail-Hook (Reelcover) · Caption · B-Roll · 5 passende Hashtags · Story-Sequenz · DM-Antwort (wenn Keyword/DM)
Format: Kalter bis warmer Traffic · Wiedererkennung · körpernahe Wahrheit · leise Autorität

### /reel-idee [idee | hook]

**Zweck:** Du kommst mit einer eigenen Idee oder einem fertigen Hook — Claude prüft/schärft den Hook und baut daraus das komplette, postfertige Reel. Der Hook ist dein Ausgangspunkt, nicht Claudes. Erkennt automatisch die passende Content-Säule.

- `/reel-idee Viele Frauen halten Erschöpfung für normal …` → fertigen Hook reingeben
- `/reel-idee irgendwas zu: abends nicht abschalten können` → grobe Idee, Claude baut den Hook
- `/reel-idee Beine an der Wand` → Haltung/Übung vorgeben

Ablauf: Format automatisch erkennen (Funktionsmodus *oder* Yoga ohne Leistungsdruck) → **Hook-Check** (stark bestätigen / schärfen mit Varianten + Begründung / neu bauen) → komplettes Reel um den finalen Hook bauen, exakt nach dem erkannten Format.
Output: Erkanntes Format · Hook-Check (Urteil + finaler Hook + ggf. Alternativen) · dann alle Reel-Outputs des Formats (Reel-Text · Reelcover · Haltung & Filmhinweis bzw. B-Roll · Caption · 5 Hashtags · Story-Sequenz · DM-Antwort wenn Keyword/DM).
Nutzt `reel.md` (Funktionsmodus) bzw. `reel-yoga.md` (Yoga) als Single Source of Truth für die Formatstruktur — kein Doppeln.

### /reel-yoga [haltung]

**Zweck:** Reel im Open-Loop-Format — einfache Yoga-Haltung zeigen, On-Screen-Text in 3 Beats (Situations-Anker → Haltung + Zeit → offener Spür-Satz), Auflösung erst in der Caption. Contentsäule: Yoga ohne Leistungsdruck.

- `/reel-yoga` → Claude wählt Haltung selbst
- `/reel-yoga Kindhaltung` → Haltung selbst vorgeben

Output: Reel-Text (3 Beats, ~10–12 Sek) · Reelcover (Neugier-Hook groß als Blickfang + „3 MIN" als kleines, frei verschiebbares Eck-Badge; trägt den Situations-Anker — neu seit 2026-06-16) · Haltung & Filmhinweis · Caption (6-teilig) · CTA · 5 Hashtags · Story-Sequenz · DM-Antwort (wenn Keyword/DM)
Wirkung jeder Haltung wird vorher geprüft (wahr, in Katjas Sprache, ohne Fachbegriffe). Pflicht-Schritt Situations-Anker: jedes Reel hängt an EINEM konkreten Soulclient-Moment — trägt Hook, Cover und Weiterleitungs-Wirkung. Kein Caption-Verweis im Video, CTAs nur in der Caption. Freebie-CTA: je Reel das passende der vier Freebies wählen und über Pieces hinweg abwechseln — **3MINUTEN** (3-Minuten-Körpercheck) bei kurzem Übungs-/Spür-Fokus tagsüber · **RESET** (5-Minuten-Körper-Reset) bei Abend-/Feierabend-/Abschalten-Fokus · **NACHTRUHE** (Einschlaf-Freebie „Wenn der Kopf nicht ausmacht") bei Einschlaf-/im-Bett-/„Kopf macht nicht aus"-Fokus · **CHECK** (Funktionsmodus-Check) bei Erkennen-/Funktionsmodus-Fokus; nie zwei Keywords in einem Post mischen (ManyChat-Flow). RESET- und NACHTRUHE-Flow müssen noch gebaut werden (Stand 2026-06-22).
Einheitliche Cover-Vorlagen in Canva gespeichert → Specs & Links in `reference/reelcover-yoga.md`.
Hook-Grundregel & Formel (was viral lief, ~90k): `reference/hook-formel.md` — Hook immer am konkreten, wiedererkennbaren Moment (sie kennt ihr Problem), nie „du merkst es nicht"-Diagnose. Gilt für beide Yoga-Reel-Skills.
Hauptziel: Speichern · kalter bis warmer Traffic

### /reel-yoga-wirkung [haltung]

**Zweck:** Yoga-Reel wie `/reel-yoga`, aber **ergebnis-geführter** Einstieg — der Hook startet mit der spürbaren Wirkung statt mit dem Problem/Situations-Moment. Danach gleicher Open Loop (Auflösung in der Caption). Contentsäule: Yoga ohne Leistungsdruck.

- `/reel-yoga-wirkung` → Claude wählt Haltung selbst
- `/reel-yoga-wirkung Liegende Drehung` → Haltung vorgeben

**A/B-Test-Schwester von `/reel-yoga`** (eingerichtet 2026-06-12): Beide laufen gegeneinander, um zu sehen, welcher Einstieg die Zielgruppe besser stoppt. Der EINZIGE Unterschied ist der Hook-Ansatz — `/reel-yoga` öffnet mit dem Problem (sie erkennt sich), `/reel-yoga-wirkung` mit dem Ergebnis (sie will wissen, was sie davon hat). Cover, Caption-Aufbau, Hashtags, Story und die CTA-/Freebie-Logik (je Reel das passende der vier Freebies wählen und abwechseln — 3MINUTEN, RESET, NACHTRUHE oder CHECK) bleiben parallel.
Hook-Pool ergebnis-geführt (Insider/Advocacy · Autorität · Tempo · Machbarkeit), z. B. „Ich wünschte, mehr Frauen wüssten, dass …" · „Wenn ich dir nur eine Übung zeigen dürfte …" · „Du machst diese eine Übung drei Minuten, und …". Eingebaute Leitplanken: versprochenes Ergebnis ist immer gespürt-körperlich, nie Leistung/Optimierung (schützt vor Transformations-Sound); kein Körperteil als Schlagzeile, wenn es nach Schmerz klingt (über den Zustand führen). Gut für Test-Reels, um die Hooks durchzutesten.
Output identisch zu `/reel-yoga`.

### /reel-spiegel [thema]

**Zweck:** Minimalistisches Spiegel-Reel — ruhiges Video, der Text trägt alles. Ziel: sofortige Wiedererkennung („Das bin ich.") bei Frauen 40+. Contentsäule: Der Körper im Funktionsmodus.

- `/reel-spiegel` → Claude wählt den Winkel selbst aus dem Soulclient-Profil
- `/reel-spiegel Ruhe fühlt sich fremd an` → Winkel selbst vorgeben

Output: Text im Video (Hook-Titel + 3–5 Punkte + Schlusssatz) · Thumbnail-Hook · Caption (Hook → Spiegel → **leise Wendung, kein Yoga-Erklärteil** → CTA) · 5 Hashtags · Story-Sequenz · DM-Antwort (wenn Keyword/DM)
Format: Listen-Hook (KEINE Grundformel-Pflicht) · stille Erkenntnis · kalter Traffic · Problem-Bewusstsein
Eingebaute Regeln (2026-06-12 geschärft): Hook-Schärfer „… und du merkst/hörst es nicht" (über *Hören*, nicht „merken") · ist die Liste aus inneren Sätzen, schließt der Video-Text mit dem EINEN Satz, den sie sich nie sagt · Schlusssatz nie als Analyse/Vorwurf über sie · Caption ohne Yoga-Verkaufsabsatz, wirkt durch Erkennen · keine sich selbst widersprechenden Sätze (kleiner erster Schritt = die Veränderung selbst) · Speichern als Hauptziel, optional EIN Freebie-CTA dazu (Spür-/Rückkehr-Auflösung → 3MINUTEN, Abend-/Feierabend-Auflösung → RESET, Einschlaf-/Nacht-Auflösung → NACHTRUHE, reine Erkennung → CHECK).
Hauptziel: Speichern · Teilen · Folgen

### /persoenlich [tür | format | thema]

**Zweck:** Persönliches Feed-Piece — **Reel ODER Karussell** — aus einer der 6 „Türen", damit Follower Katja als Mensch kennenlernen, ohne dass die Nische verwässert. Persönliches ist die menschliche Schicht UNTER den zwei Content-Säulen, keine dritte Säule.

- `/persoenlich` → Claude wählt Tür (rotierend) + passendes Format
- `/persoenlich warum` → Tür vorgeben (Das Warum — Gründungsgeschichte in Häppchen)
- `/persoenlich karussell ausbildung` → Format + Tür vorgeben

Die 6 Türen: (1) Ehrlicher Zwischenstand · (2) Eigene Rückkehr in den Körper · (3) Die Ausbildung · (4) Echtes Leben drumherum · (5) Das Warum · (6) Gesicht & Stimme. Nutzt `reference/persoenlicher-content.md` als Single Source of Truth (Türen, Leitplanken, CTA-Logik) und die bestehenden `reel.md`/Karussell-Skills nur fürs Format-Gerüst — kein Doppeln. Pflicht-Regel: jeder Post endet bei der Soul-Client („… und vielleicht kennst du das auch"), nie Tagebuch; CTA bewusst (default leiser Folgen-Grund, kein reflexhaftes Speichern, Freebie nur ausnahmsweise). Output inkl. 2 Alt-Hooks zum Tauschen.

### /zielgruppe [thema | update]

**Zweck:** Mit dem Soulclient-Profil arbeiten — entweder ein Thema aus Sicht der Zielgruppe analysieren oder ein neues Insight dokumentieren.

- `/zielgruppe Feierabend-Erschöpfung` → Analyse: Sprache, innere Sätze, Widerstände, Trigger-Sätze und Content-Winkel für dieses Thema
- `/zielgruppe update` → Profil-Update: neues Insight dokumentieren und in `context/soulclient.md` einpflegen

Liest automatisch `context/soulclient.md` und `context/brand-voice.md` als Grundlage.

### /karussell-uebung [übung | anlass]

**Zweck:** Tutorial-Karussell im „All of it in the Post"-Format — eine kleine, konkrete Yoga-, Atem- oder Körperübung, die komplett im Post funktioniert. Reines Content-Piece (Text), kein Rendering. Contentsäule: Yoga ohne Leistungsdruck.

- `/karussell-uebung` → Claude wählt Anlass + Übung selbst aus dem Soulclient-Profil
- `/karussell-uebung Beine an der Wand` → Übung selbst vorgeben
- `/karussell-uebung Feierabend-Erschöpfung` → Anlass vorgeben, Claude wählt passende Übung

Output: Carousel-Slides (7–9, Hook → Einordnung → Schritt-für-Schritt → Zusammenfassung → CTA) · 3 Hook-Varianten · Caption (eigener Hook → Spiegelung → Erkenntnis → Bezug zum Karussell → CTA) · 5 Hashtags · Story-Sequenz · DM-Antwort (wenn Keyword/DM) · optional Design-Hinweise pro Slide.
Format: warmer (auch kalter) Traffic · Lösungsbewusstsein · konkreter, machbarer Einstieg ohne Leistungsdruck. Wirkung jeder Übung wird vorher geprüft (wahr, in Katjas Sprache, ohne Fachbegriffe).
Hauptziel: Speichern + Freebie holen.

### /karussell-einstieg [thema | winkel]

**Zweck:** Teach-Karussell „Teach + Freebie" — erkennen → körperlich verstehen → kleiner nächster Schritt. Zeigt Frauen 40+, dass Yoga kein weiterer To-do-Punkt ist, sondern der erste Moment am Tag, in dem sie wieder bei sich ankommen. Reines Content-Piece (Text), Rendern optional. Contentsäule: Yoga ohne Leistungsdruck.

- `/karussell-einstieg` → Claude wählt den Teach-Winkel selbst
- `/karussell-einstieg Warum du nicht beweglich sein musst` → Winkel vorgeben

Output: Carousel-Slides (6–9, Hook → Problem schärfen → Teach-Teil → tiefe Erkenntnis → Freebie-Brücke → CTA) · Caption (eigene Hook → Spiegelung → Learning → Reframe → Freebie-Brücke → Kommentar-CTA) · Kommentar-CTA · 5 Hashtags · Story-Sequenz · DM-Antwort (wenn Keyword/DM).
Format: kalter + warmer Traffic · Problem- bis Lösungsbewusstsein · Yoga als Tür, nicht als Lösungsversprechen.
Hauptziel: **Kommentar fürs Freebie (Keyword ANKOMMEN)**. Abgrenzung zu `/karussell-uebung` (eine Übung, Speichern) ist im Skill dokumentiert.

### /karussell-woche

**Zweck:** Komplette Wochen-Produktion — 7 fertige Instagram-Karussells, editierbar in Canva, je mit Caption als Kommentar, abgelegt im Ordner „erstellte Karussells" (`FAHLiWIgZvA`).

Claude wählt die 7 Themen **selbst** (Trend via Instagram-Späher + WebSearch + eigene Top-Performer, vor allem nach Soul Client), schreibt in Brand Voice, rendert über die bewährte HTML→PDF-Pipeline (Foto fest eingebacken), hostet temporär auf Cloudflare, importiert als editierbare Canva-Designs, legt sie ab und kommentiert die Captions. Immer exakt diese Vorlage — nicht neu designen. Vollständige Schritt-für-Schritt-Pipeline in `.claude/commands/karussell-woche.md`.

**Läuft auf Zuruf, nicht automatisch.** Katja meldet sich, wenn sie die Karussells erstellt haben will — dann `/karussell-woche` ausführen. (Eine frühere Freitags-/Donnerstags-Automatik wurde auf Katjas Wunsch am 2026-06-04 wieder entfernt.)

### /story-woche [optional: anpassung]

**Zweck:** Komplette Wochen-Produktion für **tägliche Instagram-Stories** — 7 Tage (Mo–So) copy-fertige Frames: Text, Sticker, B-Roll-Hinweis, Link wo nötig. Einmal laufen lassen (z. B. Sonntagabend), ganze Woche fertig. Faceless: B-Roll + Text-Overlay, kein In-die-Kamera-Sprechen nötig.

Claude wählt die Inhalte **selbst** (frisch je Lauf, nie wiederholt, immer spezifisch), nach festem Rhythmus, der an Katjas Telegram-Tage andockt:
- Mo: Wahrer Satz + Spür-Check (Poll) · Di: Mini-Körperimpuls + Anstoß (Recycling) · Mi: Leiser Take · Do: Mini-Körperimpuls + Frage-Box · Fr: persönl. Einstieg (Tür 5) → Einladung (Freebie) · Sa: Spür-Check · So: persönl. Einstieg (Tür 5) → Einladung (Telegram; Audio-Teaser nur jeden 2. Sonntag im 14-Tage-Telegram-Rhythmus, sonst Verweis auf Montags-Post — siehe Memory `feedback_story_sonntag_telegram_rhythmus`)
- **Persönlicher Moment an ALLEN 7 Tagen (fest im Skill hinterlegt, kommt automatisch):** Mo/Di/Mi/Do/Sa je eine der 5 Alltags-Türen (1, 2, 3, 4, 6 — rotierend, alle 5/Woche); Fr + So Tür 5 (Das Warum) als Einstieg, der in den Funnel überleitet. So sind alle 6 Türen jede Woche in der Story. Details im Abschnitt „Persönlicher Content".

Eingebaute Regeln (aus Marktrecherche): ein Story-Run = ein Ziel · Polls max. 2–3×/Woche · kurz halten, Bestes zuerst · abends 18–22 Uhr posten · Link-Disziplin (Freebie → Opt-in/Bio · Angebot „10-Minuten-Rückkehr" → `10-minuten-rueckkehr.katjajung.com`, **nie zur Kasse**, 7-€-Tripwire nie öffentlich). Volle Format-Bausteine (A–H) + Pipeline in `.claude/commands/story-woche.md`.
Geschärft 2026-06-12: verbotene Wörter nie per Verneinung (auch „nicht mehr Disziplin" raus → „mehr Druck") · Körperimpuls-Frame-1 führt über den Zustand, nie über einen Körperteil als Schlagzeile · Wahrer Satz rotiert die Form (Vielleicht-Paar / leise Frage / stiller Spiegel-Satz), nie 3× dieselbe/Woche · Frame 1 trägt täglich einen Slider (zählt nicht als Poll, Algo-Schub) · 1 bewusster Weiterleitungs-Moment/Woche (Sends) · Mittwochs-Take endet immer auf DM-Öffner.

### /story [typ | typ anzahl]

**Zweck:** Ein einzelner Story-Post für zwischendurch — der spontane Bruder von `/story-woche`. Copy-fertig: Frame-Text, Sticker, B-Roll-Hinweis, Link wo nötig.

- `/story satz` → Wahrer Satz · `/story check` → Spür-Check (Umfrage) · `/story impuls` → Mini-Körperimpuls · `/story take` → Leiser Take · `/story frage` → Frage-Box · `/story anstoss` → Reel/Karussell teilen · `/story einladung` → Funnel (Freebie/Telegram/Angebot) · `/story bts` → Behind-the-Scenes · `/story persoenlich` → Persönliche Tür (1 von 6)
- `/story satz 3` → mehrere Varianten · ohne Argument: fragt nach dem Typ

### /shutdown

**Zweck:** Session sauber beenden — Workspace scannen, aufräumen, alles auf den neuesten Stand bringen.

Prüft alle Verzeichnisse auf veraltete oder temporäre Dateien, aktualisiert CLAUDE.md und context/, committed und pusht Änderungen, liefert einen Abschluss-Report.

---

## Kritische Anweisung: Diese Datei pflegen

**Wann immer Claude Änderungen am Workspace macht, MUSS Claude prüfen, ob CLAUDE.md aktualisiert werden muss.**

Nach jeder Änderung — ob Commands, Skripte, Workflows oder Strukturänderungen — frage:

1. Fügt diese Änderung neue Funktionalität hinzu, die Benutzer kennen müssen?
2. Ändert sie die oben dokumentierte Workspace-Struktur?
3. Sollte ein neuer Command aufgelistet werden?
4. Braucht context/ neue Dateien dafür?

Falls ja, aktualisiere die entsprechenden Abschnitte. Diese Datei muss immer den aktuellen Zustand des Workspace widerspiegeln, damit zukünftige Sessions genauen Kontext haben.

**Beispiele für Änderungen, die CLAUDE.md-Updates erfordern:**

- Neuen Slash-Command hinzufügen → im Commands-Abschnitt ergänzen
- Neuen Output-Typ erstellen → in Workspace-Struktur dokumentieren oder Abschnitt erstellen
- Skript hinzufügen → Zweck und Verwendung dokumentieren
- Workflow-Patterns ändern → entsprechende Dokumentation aktualisieren

---

## Für Benutzer, die dieses Template herunterladen

Um diesen Workspace an deine eigenen Bedürfnisse anzupassen, fülle deine Kontext-Dokumente in `context/` aus und passe sie nach Bedarf an. Verwende dann `/create-plan` zum Planen und `/implement` zum Umsetzen struktureller Änderungen. So bleibt alles synchron — besonders CLAUDE.md, die immer den aktuellen Zustand des Workspace widerspiegeln muss.

---

## Session-Workflow

1. **Start**: `/start` für kompakten Status-Check, oder `/prime` für vollständige Orientierung
2. **Erfassen**: `/capture` für schnelle Notizen und Ideen zwischendurch
3. **Planen**: `/plan` für Projekte und Vorhaben, `/create-plan` für Workspace-Änderungen
4. **Umsetzen**: `/implement` zum Ausführen von Workspace-Plänen
5. **Beenden**: `/shutdown` zum Aufräumen, Aktualisieren und sauberen Abschluss
6. **Pflegen**: Claude aktualisiert CLAUDE.md und context/ während sich der Workspace weiterentwickelt

---

## Schreibweise — Grundregel für alle Outputs

Kein Text klingt nach KI. Nicht bei Content, nicht bei Antworten, nicht in Plänen.

Nie: „Hier ist, womit…" — „Das ist nicht X, sondern Y" — „Zusammenfassend lässt sich sagen" — „in der Tat" — „durchaus" — „es ist wichtig zu betonen" — maschinell gleichförmiger Rhythmus — Floskeln ohne Substanz.

Jeder Satz ist eine Entscheidung, kein generiertes Muster.

**Immer einfache, normale Alltagssprache — nicht poetisch, nicht verkopft.** Gilt für ALLES, was wir erstellen (Reels, Karussells, Stories, Captions, E-Mails, Telegram, Antworten). So schreiben, wie Katja zu einer Freundin spricht. NICHT „dein Atem ist den ganzen Tag oben geblieben" → SONDERN „du hast den ganzen Tag kaum richtig durchgeatmet". Lieber schlicht und klar als schön. Test je Satz: Würde sie das genau so laut zu jemandem sagen?

---

## Somatic Yoga — Methode hinter allem Content

Katja macht eine **Somatic-Yoga-Lehrerausbildung** (deutsch, komplett online, self-paced: 200h-Basis/RYT-200 + Somatic-60h-Spezialisierung; bewusst nicht die klassische Yogalehrer-Ausbildung). Somatic Yoga = **spüren statt leisten** — langsame, kleine, von innen geführte Bewegungen, Körperehrlichkeit statt Performance. Passt deckungsgleich zur Marke „raus aus dem Funktionsmodus, zurück in den Körper".

- **Bei allem Content** (Reels, Karussells, Stories, Captions, Telegram, E-Mails) aus `reference/somatic-yoga.md` schöpfen — Single Source of Truth: Prinzipien, typische Übungen, Fachbegriff→Alltagssprache-Tabelle.
- **Sprach-Regel:** Die Methode ist im Kern Nervensystem-Arbeit — im Content aber NIE Fachsprache (kein „Nervensystem", „Vagus", „somatisch" als Schlagwort). Tiefe intern, Sprache körpernah. Verstärkt die bestehende Nischen-Leitplanke.

---

## Persönlicher Content (die Frau hinter der Marke)

Damit Katja als Mensch sichtbar wird, ohne die Nische zu verwässern, gibt es ein festes Persönlich-System (eingerichtet 2026-06-13). **Persönliches ist keine dritte Content-Säule, sondern die menschliche Schicht UNTER den beiden Säulen** — Katja als lebender Beweis für „raus aus dem Funktionsmodus" (Human Design Linie 6 / Role Model). Dosiert und energieschonend (Linie 2 / Hermit).

- **Single Source of Truth:** `reference/persoenlicher-content.md` — die 6 Türen, Leitplanken (immer „zurück zu ihr", kein Oversharing, keine Guru-Story), CTA-Logik (Beziehung statt Funnel) und Rhythmus/Format-Verteilung. Alle Persönlich-Skills lesen daraus.
- **Die 6 Türen:** (1) Ehrlicher Zwischenstand · (2) Eigene Rückkehr in den Körper · (3) Die Ausbildung · (4) Echtes Leben drumherum · (5) Das Warum (in Häppchen) · (6) Gesicht & Stimme.
- **Stories (jeden Tag):** `/story-woche` baut an ALLEN 7 Tagen einen kleinen persönlichen Moment ein (fest hinterlegt, kommt automatisch). Mo/Di/Mi/Do/Sa = je eine der 5 Alltags-Türen (1, 2, 3, 4, 6 — Zuordnung rotiert wöchentlich); Fr + So = Tür 5 (Das Warum) als Einstieg in den Funnel. Spontan zusätzlich über `/story persoenlich`. Getrackt in `outputs/story-woche/verlauf.md` (Abschnitt „Persönliche Türen").
- **Feed (1×/Woche):** Tür 5 (Das Warum / Geschichte) als Reel oder Karussell über `/persoenlich` — ~1 von 7 Feed-Posts, das Grid bleibt Nische-dominiert.
- **Variation:** Jedes Mal ein anderer Moment/Häppchen; Tür 5 über Story (Fr/So) + Feed nie doppelt. Tag→Tür-Zuordnung der 5 Alltags-Türen wöchentlich variieren.

## Content-Ablage (Notion)

Katjas fertiger Content wird in ihrer Notion-Datenbank **„Feed"** gesammelt — ihr bestehender Content-Kalender, den sie so behalten will.

- **Wann:** Sobald Katja ein Content-Piece ausdrücklich abnimmt („passt so" / „perfekt") — nie ungefragt.
- **Wohin:** Datenbank „Feed" auf der Notion-Seite „yoga.statt.funktionieren", `data_source_id` `33a8aca2-e91e-81af-8577-000b691410f4`. Anlegen via `notion-create-pages` mit `parent: {type: data_source_id, ...}`.
- **Feld-Mapping:** Titel/Überschrift (Thema) · Format (Reels/Carousel/Post/Video/IG Live) · Thumbnail-Hook (Cover-Text) · Content Säule · Erstellt = `__YES__` · Gepostet + Datum/Tag leer (plant Katja selbst) · kompletter Content im Seiteninhalt.
- **Immer mitablegen:** Im Seiteninhalt **immer die zwei Alternativ-Hooks** („zum Tauschen") mit aufnehmen — nicht nur den finalen Hook (Katja-Wunsch 2026-06-13, gilt dauerhaft). Außerdem den CTA pro Piece **bewusst** wählen, nie reflexhaft „Speichern" als Default.
- **Content-Säulen (in Notion gepflegt):** „Yoga ohne Leistungsdruck" · „Der Körper im Funktionsmodus".
- **Hinweis:** Das Reelcover der Yoga-Serie (`/reel-yoga` + `/reel-yoga-wirkung`) zeigt seit 2026-06-16 den großen Neugier-Hook als Blickfang + „3 MIN" als kleines, frei verschiebbares Eck-Badge (ersetzt den alten fixen Kicker „3-MINUTEN-ÜBUNG"). Zwei Varianten (Foto+Verlauf · einfarbig), Canva-Vorlage `DAHMwUMzKLg` im Ordner „Reelcover" — Details in `reference/reelcover-yoga.md`. Gehört nur zu diesen Yoga-Reels, nicht zu anderen Reel-Formaten.

**Zweite Datenbank — „Story Highlights & Stories"** (auf derselben Seite „yoga.statt.funktionieren", `data_source_id` `150c2b99-75fe-4478-94c4-ed52407136ae`): Bibliothek für Instagram Story Highlights und einzelne Stories. Spalten: Highlight/Story (Titel) · Typ (Highlight / Story (Einzel)) · Status · Content-Säule (+ „Orientierung / Account") · Slides · CTA/Link-Sticker · Reihenfolge · Notiz. Slide-Texte stehen copy-fertig im Seiteninhalt (Quote-Blöcke). Die 7 Highlights (Starte hier · Über mich · Funktionsmodus · Yoga 40+ · 3-Minuten-Yoga · Wahre Sätze · Angebot) liegen dort fertig. Stories nur ablegen, wenn Katja sie ausdrücklich abnimmt.

**Dritte Datenbank — „Telegram — Zurück zu dir"** (auf derselben Seite „yoga.statt.funktionieren", `data_source_id` `d8b65105-7f91-4a53-971c-2e8c395e3e64`, angelegt 2026-06-13): Sammlung der fertigen Telegram-Posts für die Gruppe „Zurück zu dir". Spalten: Titel · Typ (Wahrer Satz / Körperimpuls / Audio-Rückkehr / Tagesimpuls) · Woche (Woche 1 / Woche 2 / Spontan) · Tag (Montag / Donnerstag / Sonntag / Spontan) · Status (Entwurf / Fertig / Gepostet) · Gepostet am (Datum, leer — plant Katja selbst). Der komplette Post steht copy-fertig im Seiteninhalt als Code-Block (Code-Block = exakte Zeilenumbrüche + 1-Klick-Kopieren); bei der Audio-Rückkehr Titel und Skript als zwei getrennte Code-Blöcke. **Hier KEINE Alternativ-Hooks** — die Alt-Hook-Regel gilt nur für Feed-Content (Reels/Karussells), Telegram-Posts haben keinen Hook-Mechanismus. Telegram-Content immer in DIESE DB, nie in „Feed". Ablegen nur, wenn Katja den Post ausdrücklich abnimmt (Katja-Wunsch 2026-06-13: jeden abgenommenen Telegram-Post direkt hier einfügen).

Details im Memory: `notion_content_workflow.md`.

---

## Live-Funnel & Hosting

Die Verkaufs-/Landingpages liegen als statisches HTML im Workspace und werden auf **Cloudflare Pages** gehostet (umgezogen von Netlify, weil das Netlify-Konto wegen Credit-Limit pausiert wurde).

- `website-quelle/` — **Quelldateien**: `index.html` (Landingpage), `angebot.html` (€7-Tripwire-Verkaufsseite), `kurs.html` (öffentliche €17-Kursseite), `optin.html`, `katja.jpg`. Änderungen hier vornehmen. (Früher `netlify-deploy/` — umbenannt 2026-06-22, weil der alte Name verwirrte; es geht nichts zu Netlify, das ist nur der Quell-Ordner für den Cloudflare-Deploy.)
- `cloudflare-deploy/check/` und `cloudflare-deploy/kurs/` — **Deploy-Ordner** für die zwei Cloudflare-Pages-Projekte. Vor jedem Deploy aus `website-quelle/` synchronisieren.
- `reference/cloudflare-config.md` — Token, Account-ID, Projektnamen, Deploy-Befehle, DNS-Einträge. **Single Source of Truth fürs Deployen.**

Live-Domains: `check.katjajung.com` (Landingpage + €7-Seite) und `10-minuten-rueckkehr.katjajung.com` (€17-Kursseite). Bezahlung/Kurse/E-Mail-Marketing laufen weiterhin über **systeme.io** — Cloudflare ist nur die Anzeige-Hülle, die Kauf-Buttons verlinken auf systeme.io-Bezahlseiten (`minikurs1` = 7 € exklusiv am Freebie-Weg, `17minikurs1` = 17 € öffentlich).

## ManyChat (Auto-DM-Funnel)

ManyChat steuert die **Instagram-Auto-DMs**: Kommentar mit Keyword **CHECK** unter einem Reel → automatische DM mit Freebie-Link (`check.katjajung.com`). Verbindet Instagram-Kommentar → Freebie → Landingpage → systeme.io.

- **Account:** @yoga.statt.funktionieren, **Free-Plan** (Limit 25 Kontakte). Kein MCP/API-Connector → Bedienung über die **Claude-Chrome-Extension** (eingeloggte Session) oder copy-fertige Texte.
- **Flows (Stand 2026-06-22):**
  - **„Auto-DM Funktionsmodus-Check"** — Keyword **CHECK** → Opening-DM → Link-DM `check.katjajung.com`. **LIVE** auf dem Reel „Der Körper sagt selten laut Nein…".
  - **„Auto-DM 3MINUTEN (Körpercheck)"** — Keyword **3MINUTEN** → Opening-DM → Link-DM mit Google-Drive-Link (3-Minuten-Körpercheck, Direkt-Lieferung) + Telegram-Button. Status **DRAFT/Off**, Trigger-Post bei Bedarf aufs Promo-Reel setzen.
  - **„Auto-DM RESET (5-Minuten-Körper-Reset)"** — Keyword **RESET** → Link-DM mit Google-Drive-Link (`docs.google.com/document/d/1e4bbzXMVQ3ZuNh8GfTPEkFQr9bD93lwCmf18ksXiIoA`, Direkt-Lieferung) + Telegram-Button. **NOCH NICHT GEBAUT (Stand 2026-06-22)** — muss noch angelegt werden, bevor RESET als Keyword-CTA live gehen darf.
  - **„Auto-DM NACHTRUHE (Einschlaf-Freebie)"** — Keyword **NACHTRUHE** → Link-DM mit Google-Drive-Link (`docs.google.com/document/d/1EKkAjrlYFzq_cMwmse97t558lXxV9T3-JYyNGXjBNbY`, Direkt-Lieferung Einschlaf-Freebie „Wenn der Kopf nicht ausmacht") + Telegram-Button. **NOCH NICHT GEBAUT (Stand 2026-06-22)** — wird im ManyChat-Komplett-Setup am 28.06. gebaut, bevor NACHTRUHE als Keyword-CTA live gehen darf.
- **Keyword-Konsistenz (jetzt pro Freebie):** Erkennungs-/Funktionsmodus-Content → **CHECK** · kurzer Übungs-/Spür-Content tagsüber → **3MINUTEN** · Abend-/Feierabend-/Abschalten-Content → **RESET** · Einschlaf-/im-Bett-/„Kopf macht abends nicht aus"-Content → **NACHTRUHE**. Über Pieces/Stories hinweg bewusst abwechseln. Keyword im Post muss exakt zum jeweiligen Trigger passen. Keywords distinktiv halten (siehe Memory `project_manychat_keyword_strategy`). **Gotcha:** Archiviertes/neu hochgeladenes Reel bricht den Trigger („Post not found") → neu zuweisen; Trigger-Schalter muss ON sein.
- **Konnektor = Stufe 2:** Eigener MCP-Server um die ManyChat-API erst bei **Pro** (API ist Pro-only) + Volumen, v. a. für systeme.io-Sync. Jetzt nicht nötig — Browser-Weg reicht.
- **Details & Konnektor-Fähigkeiten:** `reference/manychat-konnektor.md`.

## Instagram-Späher (täglicher Wettbewerber-Bot)

Automatisierter Bot in `scripts/instagram-watch/`, der täglich die wichtigsten
Wettbewerber-Accounts (@entspannungsstudio_anila · @jasmin.bachman · @kerstin.huber.steinhorst · @nadine_weiland_yoga)
auf neue Reels/Posts prüft und Katja per Telegram benachrichtigt.

- **Lauf:** `launchd` täglich um 18:00 auf Katjas Mac (`com.katja.instagram-watch.plist`).
- **Abruf:** Instagram-Daten über **Apify** (Gratis-Kontingent). Anonymes Scrapen blockt
  Instagram inzwischen (403) — Apify ist der zuverlässige Weg ohne Account-Risiko.
- **Analyse:** Wenn das **Claude Code CLI** installiert ist, analysiert Claude jeden neuen
  Beitrag durch Katjas Strategie/Marke (gratis übers Abo). Sonst saubere Liste als Fallback.
- **State:** `state.json` merkt bekannte Beiträge → nur echte Neuigkeiten werden gemeldet.
- **Mitschrift:** Jede gesendete Telegram-Nachricht wird zusätzlich lokal gesichert in `scripts/instagram-watch/sent/JJJJ-MM-TT.txt` (gitignored) — so kann Claude jederzeit nachlesen/vorlesen, was der Späher verschickt hat.
- **Übersicht:** Die Hauptnachricht listet am Ende ALLE geprüften Accounts mit Vermerk (✅ x neu · ➖ nichts Neues · ⚠️ Abruf gescheitert).
- **Secrets:** `config.json` (Apify- + Telegram-Token) ist gitignored, nie committen.
- **Setup & Details:** `scripts/instagram-watch/README.md`.

## Karussell-Wochen-Produktion (auf Zuruf)

Katjas wöchentliche Instagram-Karussells erstellt Claude **auf Zuruf** — Katja meldet sich, wenn sie sie haben will (keine automatische Terminierung; eine frühere Freitags-/Donnerstags-Automatik wurde am 2026-06-04 auf ihren Wunsch entfernt).

- **Auslöser:** `/karussell-woche` (oder Katja bittet darum). Ablauf folgt exakt `.claude/commands/karussell-woche.md` — 7 Themen autonom nach Trend + Soul Client (immer spezifisch, nie generisch), Inhalte in Brand Voice, HTML→PDF rendern (Foto eingebacken), temporär auf Cloudflare hosten, als editierbare Canva-Designs importieren, in Ordner „erstellte Karussells" (`FAHLiWIgZvA`) ablegen, Captions als Kommentar, temp-Hosting löschen.
- **Produktionsbausteine:** `outputs/karussell/build.py` (Inhalt `CAROUSELS` + PNG-Renderer), `build_pdf.py` (editierbare PDFs), `bake_photo.py` (Gradient ins Foto backen → `cover_bg.png`/`close_bg.png`), `KARUSSELLS.md` (Captions). Design-System-Details + bekannte Import-Tücken im Memory `project_karussell_design_system.md`.

## Instagram Story-Highlight-Cover

Die 7 Highlight-Cover für @yoga.statt.funktionieren sind gebaut (2026-06-05). Look: **nur Strichsymbol (Espresso #3A2D28) auf vollflächigem Sandbeige #D8C7B2, kein Wort**, 1080×1920, Symbol mittig (Instagram stanzt den runden Kreis selbst aus → ganzes Bild gefüllt).

- **Produktion:** `outputs/highlight-covers/gen_final.py` (HTML/CSS → headless Chrome → einzelne PNGs + 7-seitiges PDF). PNGs in `outputs/highlight-covers/final/`.
- **Canva:** editierbares Design `DAHLvN6rajc` im Ordner „Highlight-Cover" (`FAHLvJtAYGI`). Pipeline = wie Karussells (PDF → temp Cloudflare → `import-design-from-url` als `your_story` → in Ordner verschieben → temp löschen).
- **Doku:** `reference/highlight-cover.md` (Symbol-Zuordnung je Highlight, Pipeline für neue/​geänderte Cover). Highlights-Liste lebt in der Notion-DB „Story Highlights & Stories".

## Instagram Story-Vorlagen (Canva)

Editierbares Story-Vorlagen-Set, eine Vorlage je Story-Typ (Wahrer Satz · Spür-Check · Mini-Impuls · Leiser Take · Frage-Box · Einladung · Behind-the-Scenes), gebaut 2026-06-11. Marken-Optik (Sandbeige/Creme, Libre Baskerville + DM Sans), 1080×1920. Katja tippt nur den Text rein; Sticker setzt sie in Instagram.

- **Produktion:** `outputs/story-vorlagen/build.py` (HTML/CSS → headless Chrome → Preview-PNGs + 7-seitiges PDF). Pipeline wie Highlight-Cover/Karussell (PDF → temp Cloudflare → `import-design-from-url` als `your_story` → in Ordner → temp löschen).
- **Canva:** Design „Story-Vorlagen — yoga.statt.funktionieren" `DAHMRwHPwjc` im Ordner „Story-Vorlagen" `FAHMR5OZJJI`.
- **Doku:** `reference/story-vorlagen.md`. Grundlagen für guten Story-Aufbau (Recherche) + Zielgruppen-Übersetzung: `reference/story-aufbau.md` (von `/story` + `/story-woche` mitgelesen).
- **Variation:** `/story` und `/story-woche` teilen sich `outputs/story-woche/verlauf.md` — vor jedem Lauf lesen (nicht wiederholen), nach jedem Lauf eintragen. Erzwingt frische Körperthemen/Sätze über Wochen hinweg.
- **Erklär-Regel für Übungen:** Jede Übung/Haltung in JEDEM Format anfängerinnen-tauglich (Ausgangshaltung + genaue Bewegung + Atemrichtung + Wiederholung). Kanon in `reference/somatic-yoga.md`, verankert in allen Übungs-Skills.

## CTA-Bibliothek

Pro Reel-Ziel eine fertige CTA-Vorlage in Brand Voice — zum Rauspicken beim Content-Bau (recherchiert + festgelegt 2026-06-08). Jeweils gleich aufgebaut: Kernregel · CTAs nach Mechanismus · Platzierung · Tabu. Liegt doppelt — als Markdown in `reference/` und als Notion-Unterseite der Seite „yoga.statt.funktionieren".

- **Folgen** → `reference/folgen-ctas.md` — Regel: Grund statt Bitte („bleib hier, wenn…"), Identität/Zugehörigkeit am stärksten.
- **Speichern** → `reference/speichern-ctas.md` — Regel: wiederkehrender Zukunftsmoment („für die Abende, an denen…").
- **Kommentar/Keyword** → `reference/kommentar-keyword-ctas.md` — Keyword immer **CHECK** (Funnel), plus Erkennungs-Kommentar fürs Engagement.

## Notizen

- Kontext minimal aber ausreichend halten — kein Bloat
- Pläne in `plans/` mit datierten Dateinamen für die Historie
- Outputs nach Typ/Zweck in `outputs/` organisiert
- Referenzmaterialien in `reference/` zur Wiederverwendung
