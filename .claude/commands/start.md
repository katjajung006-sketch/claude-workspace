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

## Status-Ausgabe

Nach dem Lesen liefere einen kompakten Status-Block — kein Fließtext, nur das Wesentliche:

```
## Workspace-Status

**Wer du bist:** <eine Zeile — Rolle und Kontext des Users>
**Aktueller Fokus:** <was gerade im Vordergrund steht, laut context/>
**Offene Pläne:** <Pläne in plans/ mit Status "Entwurf" oder "In Arbeit", oder "Keine">
**Letzte Outputs:** <die 3 neuesten Dateien in outputs/, oder "Keine">
**Inbox:** <Anzahl und kurze Beschreibung der Einträge in inbox/, oder "Leer">

**Verfügbare Commands:** /start · /capture · /plan · /create-plan · /implement · /shutdown · /prime

**Bereit.** Was möchtest du heute angehen?
```

Halte es kurz — maximal 15 Zeilen. Kein Willkommenstext, keine Erklärungen. Direkt zum Status.
