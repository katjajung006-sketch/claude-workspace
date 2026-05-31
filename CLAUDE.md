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

Output je Reel: Reel-Text · Thumbnail-Hook (Reelcover) · Caption · B-Roll · 5 passende Hashtags
Format: Kalter bis warmer Traffic · Wiedererkennung · körpernahe Wahrheit · leise Autorität

### /reel-yoga [haltung]

**Zweck:** Reel im Open-Loop-Format — einfache Yoga-Haltung zeigen, Neugier-Text im Reel, Auflösung erst in der Caption. Contentsäule: Yoga ohne Leistungsdruck.

- `/reel-yoga` → Claude wählt Haltung selbst
- `/reel-yoga Kindhaltung` → Haltung selbst vorgeben

Output: Reel-Hook · Reelcover (Kicker „3-MINUTEN-ÜBUNG" fest + variabler Neugier-Zusatz) · Haltung & Filmhinweis · Caption (6-teilig) · CTA · 5 Hashtags
Wirkung jeder Haltung wird vorher geprüft (wahr, in Katjas Sprache, ohne Fachbegriffe).
Einheitliche Cover-Vorlagen in Canva gespeichert → Specs & Links in `reference/reelcover-yoga.md`.
Hauptziel: Speichern · kalter bis warmer Traffic

### /zielgruppe [thema | update]

**Zweck:** Mit dem Soulclient-Profil arbeiten — entweder ein Thema aus Sicht der Zielgruppe analysieren oder ein neues Insight dokumentieren.

- `/zielgruppe Feierabend-Erschöpfung` → Analyse: Sprache, innere Sätze, Widerstände, Trigger-Sätze und Content-Winkel für dieses Thema
- `/zielgruppe update` → Profil-Update: neues Insight dokumentieren und in `context/soulclient.md` einpflegen

Liest automatisch `context/soulclient.md` und `context/brand-voice.md` als Grundlage.

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

## Live-Funnel & Hosting

Die Verkaufs-/Landingpages liegen als statisches HTML im Workspace und werden auf **Cloudflare Pages** gehostet (umgezogen von Netlify, weil das Netlify-Konto wegen Credit-Limit pausiert wurde).

- `netlify-deploy/` — **Quelldateien** (Name historisch): `index.html` (Landingpage), `angebot.html` (€7-Tripwire-Verkaufsseite), `kurs.html` (öffentliche €17-Kursseite), `optin.html`, `katja.jpg`. Änderungen hier vornehmen.
- `cloudflare-deploy/check/` und `cloudflare-deploy/kurs/` — **Deploy-Ordner** für die zwei Cloudflare-Pages-Projekte. Vor jedem Deploy aus `netlify-deploy/` synchronisieren.
- `reference/cloudflare-config.md` — Token, Account-ID, Projektnamen, Deploy-Befehle, DNS-Einträge. **Single Source of Truth fürs Deployen.**

Live-Domains: `check.katjajung.com` (Landingpage + €7-Seite) und `10-minuten-rueckkehr.katjajung.com` (€17-Kursseite). Bezahlung/Kurse/E-Mail-Marketing laufen weiterhin über **systeme.io** — Cloudflare ist nur die Anzeige-Hülle, die Kauf-Buttons verlinken auf systeme.io-Bezahlseiten (`minikurs1` = 7 € exklusiv am Freebie-Weg, `17minikurs1` = 17 € öffentlich).

## Notizen

- Kontext minimal aber ausreichend halten — kein Bloat
- Pläne in `plans/` mit datierten Dateinamen für die Historie
- Outputs nach Typ/Zweck in `outputs/` organisiert
- Referenzmaterialien in `reference/` zur Wiederverwendung
