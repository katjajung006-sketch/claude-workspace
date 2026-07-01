# Start

> Workspace-Kontext laden und kompakten Status anzeigen. Schnellerer Einstieg als /prime — fokussiert auf aktuellen Stand statt vollständiger Orientierung.

## Ausführen

```
ls context/
ls plans/
ls outputs/
ls inbox/ 2>/dev/null || echo "(inbox/ leer oder nicht vorhanden)"
```

## Lesen

CLAUDE.md
./context

**Außerdem jeden `inbox/`-Eintrag kurz öffnen** und auf den Status/Fällig-Vermerk prüfen. Offene Erinnerungen leben dort, nicht nur in `plans/`. Achte je Datei auf:
- `Status:` (offen / wartet / erledigt …)
- `Fällig:` bzw. ein Datum → mit dem heutigen Datum vergleichen (überfällig, fällig bald, oder noch Zeit)

**Außerdem die terminierten Erinnerungen (Scheduled Tasks) abrufen** — die zeitgesteuerten Reminder leben NICHT in `inbox/`, sondern im Scheduler. Dafür das Tool `mcp__scheduled-tasks__list_scheduled_tasks` aufrufen (ist ein deferred Tool → ggf. vorher per ToolSearch laden). Nur Einträge mit `enabled: true` zählen; deaktivierte ignorieren. Je Eintrag `description` + `fireAt`/`nextRunAt` nehmen und das Datum mit heute vergleichen (überfällig / fällig in X Tagen). Diese Reminder gehören mit in „Offene Pläne & Erinnerungen".

## Status-Ausgabe

Nach dem Lesen liefere einen kompakten Status-Block — kein Fließtext, nur das Wesentliche:

```
## Workspace-Status

**Wer du bist:** <eine Zeile — Rolle und Kontext des Users>
**Aktueller Fokus:** <was gerade im Vordergrund steht, laut context/>
**Offene Pläne & Erinnerungen:** <alle noch offenen Vorhaben — aus plans/ (Status "Entwurf"/"In Arbeit"), offene inbox/-Einträge mit Status offen/wartet UND alle aktiven terminierten Erinnerungen (Scheduled Tasks, enabled). Je Eintrag: Titel + Fällig-Hinweis relativ zu heute (z. B. "fällig ab 19.06., noch 8 Tage" / "am 25.06., in 5 Tagen" / "überfällig" / "auf später verschoben"). Die terminierten Reminder immer mit auflisten. "Keine" nur, wenn wirklich nichts offen ist.>
**Letzte Outputs:** <die 3 neuesten Dateien in outputs/, oder "Keine">
**Inbox:** <Anzahl Einträge in inbox/ gesamt + kurze Beschreibung, oder "Leer">

**Verfügbare Commands:** /start · /capture · /plan · /create-plan · /implement · /shutdown · /prime · /zielgruppe · /telegram · /reel · /format-klammersätze · /reel-idee · /reel-yoga · /reel-yoga-wirkung · /reel-stille · /reel-spiegel · /persoenlich · /karussell-uebung · /karussell-einstieg · /karussell-woche · /story · /story-woche

**Bereit.** Was möchtest du heute angehen?
```

Halte es kurz — Richtwert ~15 Zeilen, plus je eine Zeile pro offener Erinnerung. Kein Willkommenstext, keine Erklärungen. Direkt zum Status.
