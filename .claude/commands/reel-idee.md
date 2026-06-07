# Reel-Idee — aus deiner Idee zum fertigen Reel

> Du kommst mit einer Idee oder einem Hook, ich prüfe und schärfe den Hook und baue daraus das komplette, postfertige Reel — automatisch im passenden Format (Der Körper im Funktionsmodus *oder* Yoga ohne Leistungsdruck). Der Hook ist dein Ausgangspunkt, nicht meiner.

## Variablen

idee: $ARGUMENTS

---

## Schritt 1 — Kontext laden

Lies zuerst:
- `context/soulclient.md`
- `context/brand-voice.md`

Das passende Format-Dokument liest du in Schritt 2, sobald die Säule feststeht.

---

## Schritt 2 — Idee aufnehmen & Format erkennen

**Wenn $ARGUMENTS leer:** Frag nach Katjas Idee oder Hook. Beispiele, was reinkommen kann:
- Ein fertiger Hook („Viele Frauen halten Erschöpfung für normal …")
- Eine grobe Idee ohne Hook („irgendwas zu: abends nicht abschalten können")
- Eine Haltung/Übung mit Winkel („Beine an der Wand, aber der Hook fehlt mir noch")

**Format automatisch erkennen** — welche Content-Säule trägt diese Idee?

- **Yoga ohne Leistungsdruck** → wenn die Idee eine konkrete Haltung, Übung oder Körperaktion enthält *oder* nach Open-Loop klingt („3 Minuten …", „mach das …", „bleib so liegen …"). Dann gilt das Open-Loop-Format aus `.claude/commands/reel-yoga.md`.
- **Der Körper im Funktionsmodus** → wenn die Idee ein Erkennungs-/Awareness-Thema ist (Müdigkeit, für andere da sein, nicht abschalten, Gereiztheit, sich selbst übergehen). Dann gilt das Funktionsmodus-Format aus `.claude/commands/reel.md`.

**Sag in einem Satz, welches Format du erkannt hast** — damit Katja korrigieren kann, falls du danebenliegst. Bei Unklarheit: den besseren Fit wählen, kurz begründen, weitermachen (sie kann umsteuern).

**Dann das erkannte Format-Dokument vollständig lesen** — es ist die Single Source of Truth für Hook-Mechanik, Caption-Struktur, Reelcover, B-Roll/Haltung, Hashtags, Story und DM:
- Funktionsmodus → `.claude/commands/reel.md`
- Yoga → `.claude/commands/reel-yoga.md`

---

## Schritt 3 — Hook-Check (das Herzstück)

Bevor irgendetwas gebaut wird: Katjas Hook ehrlich prüfen — gegen die Mechanik des erkannten Formats.

- **Funktionsmodus-Format:** Der Hook muss über eine der vier Grundformeln + einen Klammersatz tragen (siehe `reel.md`). Maßstab: sofortige Wiedererkennung, körpernahe Wahrheit, der Klammersatz als emotionaler Stich.
- **Yoga-Format:** Der Hook muss Open-Loop sein — Neugier öffnen, die Auflösung NICHT im Reel verraten (siehe `reel-yoga.md`).

**Ehrlich urteilen, nicht schmeicheln.** Drei mögliche Ausgänge:

1. **Hook ist schon stark** → bestätigen, höchstens minimal nachschärfen (ein Wort, ein Rhythmus). Sagen, warum er trägt.
2. **Hook ist gut, aber verbesserbar** → 2–3 geschärfte Varianten geben, eine empfehlen, **kurz begründen warum** (welche Formel/Mechanik sie stärker macht).
3. **Hook trifft noch nicht** → in 1–2 Sätzen sagen, was fehlt (z. B. „verrät die Auflösung schon" / „keine Wiedererkennung, zu abstrakt"), dann bessere Optionen liefern.

**Wenn Katja nur eine Idee ohne Hook gegeben hat:** Hook von Grund auf bauen — mit den Formeln/Prinzipien des erkannten Formats, 2–3 Varianten, eine empfohlen.

Am Ende von Schritt 3 steht **ein finaler Hook fest** (klar markiert). Dieser Hook ist ab jetzt gesetzt — das ganze Reel wird um ihn herum gebaut. Wenn mehrere Varianten zur Wahl stehen, baust du das Reel mit der empfohlenen — Katja kann nachher tauschen.

---

## Schritt 3.5 — Nur bei Yoga: Wirkung der Haltung prüfen (PFLICHT)

Wenn das erkannte Format Yoga ist: vor dem Schreiben die echte Wirkung der Haltung prüfen — genau wie in `reel-yoga.md` (Schritt 2.5) beschrieben.

- Nur wahre Resultate, nichts erfinden, nichts übertreiben (im Zweifel kurz per WebSearch prüfen).
- Keine Fachbegriffe (kein Parasympathikus, Cortisol, Lymphfluss, Asana). In Katjas Sprache übersetzen: runterkommen · Kopf wird leiser · Körper darf aus dem Funktionsmodus aussteigen.
- Beine nach oben (Beine an der Wand, Figur-4 liegend) → Beine werden **leichter**. Savasana am Boden → Beine werden schwer. Nicht verwechseln.

---

## Schritt 4 — Das komplette Reel bauen

Jetzt das vollständige, postfertige Reel um den finalen Hook bauen — **exakt nach der Struktur des erkannten Format-Dokuments**. Alle Outputs, die das jeweilige Format liefert:

- **Reel-Text / Reel-Hook** (On-Screen) — der finale Hook aus Schritt 3
- **Reelcover** (Thumbnail-Hook; bei Yoga mit festem Kicker „3-MINUTEN-ÜBUNG")
- **Haltung & Filmhinweis** (Yoga) *bzw.* **B-Roll-Vorschlag** (Funktionsmodus)
- **Caption** (volle Struktur des jeweiligen Formats — beginnt NIE mit demselben Satz wie das Reel)
- **5 Hashtags** (auf dieses Reel zugeschnitten, keine generischen Mega-Tags)
- **Story-Sequenz** (immer, 3–5 kurze Stories, die zum Reel führen)
- **DM-Antwort** (nur wenn der Post eine DM-/Keyword-Mechanik nutzt — sonst weglassen)

Die genauen Bausteine, Beispiele und Stilregeln je Output stehen im gelesenen Format-Dokument — dort nachschlagen, nicht hier dupliziert.

---

## Ausgabe-Format

Zuerst der Hook-Check, dann das fertige Reel:

```
---
ERKANNTES FORMAT

[Funktionsmodus | Yoga ohne Leistungsdruck] — [ein Satz, warum]

---
HOOK-CHECK

Urteil: [stark bestätigt | geschärft | neu gebaut]
[kurze ehrliche Einschätzung von Katjas Hook + warum]

Finaler Hook: [der gesetzte Hook]
[ggf. 1–2 Alternativen zum Tauschen]

---
```

Danach das vollständige Reel im Ausgabe-Format des erkannten Formats (siehe `reel.md` bzw. `reel-yoga.md`): Reel-Text · Reelcover · Haltung/Filmhinweis bzw. B-Roll · Caption · Hashtags · Story-Sequenz · DM-Antwort (wenn nötig).

Nach der Ausgabe: kurz fragen, ob Hook, Caption oder ein anderer Teil angepasst werden soll — oder ob eine der Hook-Alternativen rein soll.

---

## Stilregeln

- Der Hook ist Katjas Ausgangspunkt — respektier ihre Idee, schärfe sie, ersetz sie nur, wenn sie wirklich nicht trägt (und sag dann warum).
- Beim Hook-Check ehrlich sein, nicht nett. Eine geschärfte Variante hilft mehr als ein „passt schon".
- Brand Voice aus `brand-voice.md` strikt einhalten · nichts Generisches · kein KI-Klang.
- Verbotene Wörter: High Performance · Glow up · Selbstoptimierung · Hustle · Disziplin · Challenge · Transformation in X Tagen · Workout · (Yoga-Jargon/Physiologie-Begriffe).
- Yoga und Atem als Rückweg — nicht als weitere Leistung.
- Freebie-CTAs nur ehrlich auf den aktuellen Freebie-Bestand zuschneiden (siehe Memory `project_freebie_inventory.md`).
