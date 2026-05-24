# Plan

> Einen ausführlichen Projektplan erstellen und in `plans/` ablegen. Für Projekte, Initiativen und Vorhaben — nicht nur Workspace-Änderungen (dafür: /create-plan).

## Variablen

projekt: $ARGUMENTS (beschreibe das Projekt oder Vorhaben, für das du einen Plan brauchst)

---

## Anweisungen

- **WICHTIG:** Du erstellst einen PLAN, keine Implementierung. Denke gründlich nach, stelle ggf. Rückfragen, dann schreibe ein vollständiges Plan-Dokument.
- Falls $ARGUMENTS leer ist oder zu wenig Information enthält: stelle gezielte Rückfragen (Ziel, Zeitrahmen, Ressourcen, Kontext), bevor du anfängst.
- Lies `context/` um den User, seine Rolle und aktuellen Fokus zu verstehen — der Plan soll dazu passen.
- Erstelle den Plan in `plans/` mit Dateiname: `YYYY-MM-DD-{projektname}.md`
  - Datum: heute (2026-05-23)
  - `{projektname}`: kurzer Kebab-Case-Name des Projekts

---

## Plan-Format

```markdown
# Plan: {Projekttitel}

**Erstellt:** {YYYY-MM-DD}
**Status:** Entwurf
**Projekt:** {einzeilige Beschreibung}
**Zeitrahmen:** {falls bekannt, sonst "offen"}

---

## Ziel

{Was soll am Ende erreicht sein? Konkret und messbar, 2–4 Sätze.}

## Hintergrund & Kontext

{Warum dieses Projekt? Was ist der Ausgangspunkt? Welche Einschränkungen oder Rahmenbedingungen gibt es?}

---

## Phasen & Aufgaben

### Phase 1: {Name}

**Ziel dieser Phase:** {was wird hier erreicht}
**Zeitrahmen:** {Dauer oder Zeitraum, falls bekannt}

- [ ] {Aufgabe}
- [ ] {Aufgabe}
- [ ] {Aufgabe}

**Ergebnis:** {was liegt am Ende dieser Phase vor}

---

### Phase 2: {Name}

**Ziel dieser Phase:** {was wird hier erreicht}
**Zeitrahmen:** {Dauer oder Zeitraum, falls bekannt}

- [ ] {Aufgabe}
- [ ] {Aufgabe}

**Ergebnis:** {was liegt am Ende dieser Phase vor}

---

{Weitere Phasen nach Bedarf}

---

## Ressourcen & Abhängigkeiten

| Was | Beschreibung | Status |
| --- | ------------ | ------ |
| {Ressource/Tool/Person} | {wofür gebraucht} | {verfügbar / offen} |

---

## Risiken & Unbekannte

| Risiko | Wahrscheinlichkeit | Gegenmaßnahme |
| ------ | ------------------ | ------------- |
| {Risiko} | hoch/mittel/niedrig | {wie damit umgehen} |

---

## Erfolgskriterien

Das Projekt ist abgeschlossen, wenn:

1. {messbares Kriterium}
2. {messbares Kriterium}
3. {messbares Kriterium}

---

## Nächste Schritte

Die unmittelbar nächsten Aktionen:

1. **Jetzt:** {was sofort getan werden kann}
2. **Diese Woche:** {was kurzfristig ansteht}
3. **Offen:** {was noch geklärt werden muss}

---

## Notizen

{Weitere Überlegungen, Ideen, Fragen}
```

---

## Qualitätsstandards

- Phasen und Aufgaben müssen konkret und umsetzbar sein — keine generischen Floskeln
- Zeitrahmen angeben, wenn der User sie erwähnt hat
- Risiken ehrlich einschätzen, auch wenn unbequem
- Den Plan an die Realität des Users anpassen (Rolle, Ressourcen, Kontext aus `context/`)

---

## Bericht

Nach Erstellung:

1. Kurze Zusammenfassung des Plans (3–5 Sätze)
2. Offene Fragen, die vor dem Start geklärt werden sollten
3. Pfad zur Plan-Datei: `plans/YYYY-MM-DD-{projektname}.md`
4. Hinweis auf unmittelbar nächste Schritte
