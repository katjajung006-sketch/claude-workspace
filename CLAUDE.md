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

Liest `context/` und `CLAUDE.md`, zeigt einen kompakten Status-Block: wer der User ist, aktueller Fokus, offene Pläne, Inbox-Einträge, verfügbare Commands.

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

**Zweck:** Reel im Open-Loop-Format — einfache Yoga-Haltung zeigen, Neugier-Text im Reel, Auflösung erst in der Caption. Contentsäule: Yoga ohne Leistungsdruck.

- `/reel-yoga` → Claude wählt Haltung selbst
- `/reel-yoga Kindhaltung` → Haltung selbst vorgeben

Output: Reel-Hook · Reelcover (Kicker „3-MINUTEN-ÜBUNG" fest + variabler Neugier-Zusatz) · Haltung & Filmhinweis · Caption (6-teilig) · CTA · 5 Hashtags · Story-Sequenz · DM-Antwort (wenn Keyword/DM)
Wirkung jeder Haltung wird vorher geprüft (wahr, in Katjas Sprache, ohne Fachbegriffe).
Einheitliche Cover-Vorlagen in Canva gespeichert → Specs & Links in `reference/reelcover-yoga.md`.
Hauptziel: Speichern · kalter bis warmer Traffic

### /reel-spiegel [thema]

**Zweck:** Minimalistisches Spiegel-Reel — ruhiges Video, der Text trägt alles. Ziel: sofortige Wiedererkennung („Das bin ich.") bei Frauen 40+. Contentsäule: Der Körper im Funktionsmodus.

- `/reel-spiegel` → Claude wählt den Winkel selbst aus dem Soulclient-Profil
- `/reel-spiegel Ruhe fühlt sich fremd an` → Winkel selbst vorgeben

Output: Text im Video (Hook-Titel + 3–5 Punkte + Schlusssatz) · Thumbnail-Hook · Caption (Hook → Spiegel → Erkenntnis+Brücke → CTA) · 5 Hashtags · Story-Sequenz · DM-Antwort (wenn Keyword/DM)
Format: Listen-Hook (KEINE Grundformel-Pflicht) · stille Erkenntnis · kalter Traffic · Problem-Bewusstsein
Hauptziel: Speichern · Teilen · Folgen

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
- Mo: Wahrer Satz + Spür-Check (Poll) · Di: Mini-Körperimpuls + Anstoß (Recycling) · Mi: Leiser Take · Do: Mini-Körperimpuls + Frage-Box · Fr: Wahrer Satz + Einladung (Freebie) · Sa: Behind-the-Scenes + Spür-Check · So: Wahrer Satz + Einladung (Telegram/Audio-Teaser)

Eingebaute Regeln (aus Marktrecherche): ein Story-Run = ein Ziel · Polls max. 2–3×/Woche · kurz halten, Bestes zuerst · abends 18–22 Uhr posten · Link-Disziplin (Freebie → Opt-in/Bio · Angebot „10-Minuten-Rückkehr" → `10-minuten-rueckkehr.katjajung.com`, **nie zur Kasse**, 7-€-Tripwire nie öffentlich). Volle Format-Bausteine (A–H) + Pipeline in `.claude/commands/story-woche.md`.

### /story [typ | typ anzahl]

**Zweck:** Ein einzelner Story-Post für zwischendurch — der spontane Bruder von `/story-woche`. Copy-fertig: Frame-Text, Sticker, B-Roll-Hinweis, Link wo nötig.

- `/story satz` → Wahrer Satz · `/story check` → Spür-Check (Umfrage) · `/story impuls` → Mini-Körperimpuls · `/story take` → Leiser Take · `/story frage` → Frage-Box · `/story anstoss` → Reel/Karussell teilen · `/story einladung` → Funnel (Freebie/Telegram/Angebot) · `/story bts` → Behind-the-Scenes
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

---

## Content-Ablage (Notion)

Katjas fertiger Content wird in ihrer Notion-Datenbank **„Feed"** gesammelt — ihr bestehender Content-Kalender, den sie so behalten will.

- **Wann:** Sobald Katja ein Content-Piece ausdrücklich abnimmt („passt so" / „perfekt") — nie ungefragt.
- **Wohin:** Datenbank „Feed" auf der Notion-Seite „yoga.statt.funktionieren", `data_source_id` `33a8aca2-e91e-81af-8577-000b691410f4`. Anlegen via `notion-create-pages` mit `parent: {type: data_source_id, ...}`.
- **Feld-Mapping:** Titel/Überschrift (Thema) · Format (Reels/Carousel/Post/Video/IG Live) · Thumbnail-Hook (Cover-Text) · Content Säule · Erstellt = `__YES__` · Gepostet + Datum/Tag leer (plant Katja selbst) · kompletter Content im Seiteninhalt.
- **Content-Säulen (in Notion gepflegt):** „Yoga ohne Leistungsdruck" · „Der Körper im Funktionsmodus".
- **Hinweis:** Der Reelcover-Kicker „3-MINUTEN-ÜBUNG" gehört nur zu `/reel-yoga`, nicht zu anderen Reel-Formaten.

**Zweite Datenbank — „Story Highlights & Stories"** (auf derselben Seite „yoga.statt.funktionieren", `data_source_id` `150c2b99-75fe-4478-94c4-ed52407136ae`): Bibliothek für Instagram Story Highlights und einzelne Stories. Spalten: Highlight/Story (Titel) · Typ (Highlight / Story (Einzel)) · Status · Content-Säule (+ „Orientierung / Account") · Slides · CTA/Link-Sticker · Reihenfolge · Notiz. Slide-Texte stehen copy-fertig im Seiteninhalt (Quote-Blöcke). Die 7 Highlights (Starte hier · Über mich · Funktionsmodus · Yoga 40+ · 3-Minuten-Yoga · Wahre Sätze · Angebot) liegen dort fertig. Stories nur ablegen, wenn Katja sie ausdrücklich abnimmt.

Details im Memory: `notion_content_workflow.md`.

---

## Live-Funnel & Hosting

Die Verkaufs-/Landingpages liegen als statisches HTML im Workspace und werden auf **Cloudflare Pages** gehostet (umgezogen von Netlify, weil das Netlify-Konto wegen Credit-Limit pausiert wurde).

- `netlify-deploy/` — **Quelldateien** (Name historisch): `index.html` (Landingpage), `angebot.html` (€7-Tripwire-Verkaufsseite), `kurs.html` (öffentliche €17-Kursseite), `optin.html`, `katja.jpg`. Änderungen hier vornehmen.
- `cloudflare-deploy/check/` und `cloudflare-deploy/kurs/` — **Deploy-Ordner** für die zwei Cloudflare-Pages-Projekte. Vor jedem Deploy aus `netlify-deploy/` synchronisieren.
- `reference/cloudflare-config.md` — Token, Account-ID, Projektnamen, Deploy-Befehle, DNS-Einträge. **Single Source of Truth fürs Deployen.**

Live-Domains: `check.katjajung.com` (Landingpage + €7-Seite) und `10-minuten-rueckkehr.katjajung.com` (€17-Kursseite). Bezahlung/Kurse/E-Mail-Marketing laufen weiterhin über **systeme.io** — Cloudflare ist nur die Anzeige-Hülle, die Kauf-Buttons verlinken auf systeme.io-Bezahlseiten (`minikurs1` = 7 € exklusiv am Freebie-Weg, `17minikurs1` = 17 € öffentlich).

## Instagram-Späher (täglicher Wettbewerber-Bot)

Automatisierter Bot in `scripts/instagram-watch/`, der täglich die drei wichtigsten
Wettbewerber-Accounts (@entspannungsstudio_anila · @yes.you.are_ · @julia.physioglueck)
auf neue Reels/Posts prüft und Katja per Telegram benachrichtigt.

- **Lauf:** `launchd` täglich um 18:00 auf Katjas Mac (`com.katja.instagram-watch.plist`).
- **Abruf:** Instagram-Daten über **Apify** (Gratis-Kontingent). Anonymes Scrapen blockt
  Instagram inzwischen (403) — Apify ist der zuverlässige Weg ohne Account-Risiko.
- **Analyse:** Wenn das **Claude Code CLI** installiert ist, analysiert Claude jeden neuen
  Beitrag durch Katjas Strategie/Marke (gratis übers Abo). Sonst saubere Liste als Fallback.
- **State:** `state.json` merkt bekannte Beiträge → nur echte Neuigkeiten werden gemeldet.
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

## Notizen

- Kontext minimal aber ausreichend halten — kein Bloat
- Pläne in `plans/` mit datierten Dateinamen für die Historie
- Outputs nach Typ/Zweck in `outputs/` organisiert
- Referenzmaterialien in `reference/` zur Wiederverwendung
