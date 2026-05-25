# Zielgruppe

> Arbeitet mit dem Soulclient-Profil — entweder analysiert der Skill ein Thema aus Sicht der Zielgruppe (für Content), oder er hilft, ein neues Insight zu dokumentieren und in `context/soulclient.md` einzupflegen.

## Variablen

eingabe: $ARGUMENTS

---

## Schritt 1 — Kontext laden

Lies zuerst:
- `context/soulclient.md`
- `context/brand-voice.md`

---

## Schritt 2 — Modus bestimmen

**Wenn $ARGUMENTS leer ist:**
Frage kurz:
> „Thema analysieren (z.B. `/zielgruppe Feierabend-Erschöpfung`) oder neues Insight dokumentieren (`/zielgruppe update`)?"

---

**Wenn $ARGUMENTS = `update` (oder: „neu", „insight", „ergänzen"):**
→ Modus B ausführen (Profil aktualisieren)

**In allen anderen Fällen:**
→ Modus A ausführen (Thema analysieren)

---

## Modus A — Thema analysieren

**Zweck:** Ein Thema durch die Augen der Zielgruppe sehen — für Content, Captions, Hooks, Reels.

Thema: `$ARGUMENTS`

Liefere folgende Abschnitte — kompakt, präzise, in der Sprache der Zielgruppe:

---

### Wie sie über dieses Thema spricht

Die rohen Sätze, die sie im Alltag sagt oder denkt. Nicht paraphrasiert — so nah wie möglich an ihrer Stimme.

Beispiel-Format:
- „Ich bin einfach müde, aber ich kann nicht aufhören."
- „Ich weiß nicht mal mehr, was ich eigentlich brauche."
- 4–6 Sätze in ihrer Stimme

---

### Was sie wirklich fühlt (unter der Oberfläche)

Was steckt hinter dem, was sie sagt? Welche Schicht liegt darunter?
Nicht analysieren — benennen. 2–3 Sätze.

---

### Ihr größter Widerstand zu diesem Thema

Was hält sie davon ab, sich damit zu beschäftigen oder etwas zu ändern?
Konkret, nicht abstrakt.

---

### Was sie sich wünscht (aber nicht so sagen würde)

Die tiefere Sehnsucht hinter dem Thema — in ihrer Alltagssprache.

---

### Trigger-Sätze für Content

3–5 Eröffnungssätze (Hook-Qualität), die sie sofort erkennen lässt: „Das bin ich."
Kurz. Direkt. Kein Erklären.

Format:
- „Du machst weiter. Weil aufhören sich nicht erlaubt anfühlt."
- „Dein Körper hat dich heute dreimal gefragt. Du hast dreimal nicht geantwortet."

---

### Content-Winkel (Ideen für Posts / Reels)

3–4 konkrete Ideen, wie dieses Thema als Reel, Carousel oder Caption umgesetzt werden kann.
Immer mit Blick auf: Was hilft ihr, sich zu erkennen — nicht, was bringt Reichweite?

---

## Modus B — Profil aktualisieren

**Zweck:** Ein neues Insight über die Zielgruppe festhalten und in `context/soulclient.md` einpflegen.

Führe durch diese Schritte:

1. **Frage:** „Was hast du beobachtet, gehört oder erfahren — über eine konkrete Frau, eine Reaktion, eine Aussage, ein Muster?"
   → Warte auf Antwort.

2. **Verarbeiten:** Formuliere das Insight klar und zeige Katja, wie du es einordnest:
   - Zu welchem bestehenden Abschnitt in `soulclient.md` passt es?
   - Ist es eine Ergänzung, eine Präzisierung, oder etwas Neues?

3. **Zeige den Eintrag** — exakt so, wie er in `soulclient.md` stehen würde. Warte auf Freigabe.

4. **Erst nach Freigabe:** Trage das Insight in den passenden Abschnitt in `context/soulclient.md` ein. Kein neuer Abschnitt, wenn es in einen bestehenden passt.

5. **Bestätige kurz:** Wo genau wurde was ergänzt.

---

## Stilregel für alle Outputs

- Sprache der Zielgruppe: nah, konkret, alltagstauglich — nie psychologisierend
- Kein KI-Klang, keine Floskeln, kein gleichförmiger Rhythmus
- Verbotene Wörter aus `brand-voice.md` beachten
- Kurze Sätze. Pausen. Wirkung durch Erkennen — nicht durch Erklären.
