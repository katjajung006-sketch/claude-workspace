# Capture

> Schnell eine Notiz, Idee oder Aufgabe in inbox/ speichern — ohne Ablenkung, ohne Struktur-Overhead.

## Variablen

notiz: $ARGUMENTS (der Inhalt der Notiz — Idee, Aufgabe, Link, Gedanke, etc.)

---

## Anweisungen

1. **Stelle sicher, dass `inbox/` existiert:**
   ```
   mkdir -p inbox
   ```

2. **Erstelle eine neue Notiz-Datei** in `inbox/` mit diesem Dateinamen:
   - Format: `YYYY-MM-DD-HH-MM-{kurzname}.md`
   - Datum und Uhrzeit: aktuell (2026-05-23, aktuelle Uhrzeit aus Systemzeit schätzen falls unbekannt)
   - `{kurzname}`: 2–4 Wörter aus dem Notiz-Inhalt, in Kebab-Case, ohne Sonderzeichen
   - Beispiel: `2026-05-23-14-30-idee-fuer-newsletter.md`

3. **Inhalt der Notiz-Datei:**

```markdown
# {Kurzname als Titel}

**Erfasst:** {Datum und Uhrzeit}

---

{notiz — exakt so wie eingegeben, ohne Umformulierung}

---

*Erstellt mit /capture*
```

4. **Bestätige kurz**, welche Datei erstellt wurde:
   ```
   Notiz gespeichert: inbox/YYYY-MM-DD-HH-MM-{kurzname}.md
   ```

---

## Hinweise

- Kein Nachfragen, kein Umstrukturieren — einfach speichern
- Die Notiz bleibt in `inbox/` bis der User sie weiterverarbeitet (z.B. in einen Plan überführt, zu outputs/ verschiebt oder löscht)
- Bei leerem $ARGUMENTS: den User nach dem Inhalt der Notiz fragen
