# ManyChat — Auto-DM-Funnel & Konnektor-Entscheidung

Stand: 2026-06-08

## Was ManyChat bei Katja ist

ManyChat steuert die **Instagram-Auto-DMs**: Jemand kommentiert ein Keyword unter einem Reel → bekommt automatisch eine DM mit dem Freebie-Link. Verbindet also Instagram-Kommentar → Freebie → Landingpage → systeme.io.

- **Account:** @yoga.statt.funktionieren, **Free-Plan** (Limit 25 Kontakte), 1 verbundener Kanal (Instagram).
- **Kein MCP/API-Connector** für ManyChat vorhanden → Bedienung läuft über die **Claude-Chrome-Extension** (eingeloggte Browser-Session) oder über copy-fertige Texte, die Katja einfügt.

## Aktueller Flow (gebaut 2026-06-08)

- **Trigger:** Kommentar mit Keyword **CHECK** unter dem Reel „Ruhe kommt nicht von selbst".
- **Öffentliche Antwort** unter dem Kommentar (3 rotierende deutsche Varianten).
- **Opening-DM** → Button „Schick mir den Check".
- **Link-DM** → Button „Funktionsmodus-Check" → `https://check.katjajung.com`.
- **Status:** DRAFT / Off (bewusst noch nicht live).
- E-Mail-Abfrage/Follow-up im DM sind ManyChat-Pro-Funktionen → aus. E-Mail wird erst auf der Landingpage über systeme.io geholt.

> **Keyword-Konsistenz:** Der Trigger hört auf **CHECK**. Alle Freebie-CTAs in Content (Reels/Karussells/Stories) müssen darum CHECK sagen — nicht „ANKOMMEN" (das stand in älteren Skills). Sonst feuert der Auto-DM nicht.

## Entscheidung: Konnektor = Stufe 2 (nicht jetzt)

**Jetzt:** Browser-Weg. Flows bauen wir gemeinsam in der ManyChat-Oberfläche — ganz ohne Konnektor. Für Katjas Start (0 Kontakte, Free-Plan) reicht das voll.

**Stufe 2 (später):** Eigenen MCP-Server um die **ManyChat-API** bauen. Voraussetzung: **ManyChat Pro** (die API ist Pro-only — „Get API Key" ist im Free-Plan mit UPGRADE gesperrt, bestätigt unter Settings → Extensions → API).

**Sinnvoller Auslöser für Stufe 2:** „Freebie läuft, Volumen kommt rein, ich gehe auf Pro und will systeme.io ↔ ManyChat verbinden." Dann lokalen MCP-Server bauen (läuft auf Katjas Mac, wie der Instagram-Späher in `scripts/instagram-watch/`).

### Was ein Konnektor (mit Pro) könnte
1. **Kontakte lesen & durchsuchen** — wer ist drin, nach Tag/Feld/Name filtern, Anzahl pro Segment.
2. **Tags & Felder setzen** — z. B. alle Freebie-Holer mit `freebie-check` taggen → saubere Segmente.
3. **Bestehende Flows per Befehl auslösen** — einen schon gebauten Flow gezielt an Kontakt/Segment schicken.
4. **Direkt-Nachrichten / Broadcasts senden** — an Kontakt oder Segment. **Aber** nur im Instagram-24-h-Fenster nach letzter Reaktion (oder mit zugelassenen Message-Tags) — kein „an alle Follower jederzeit".
5. **systeme.io ↔ ManyChat koppeln** — Opt-in auf der Landingpage ↔ Tag in ManyChat synchron halten (für Katja der wertvollste Teil).

### Was ein Konnektor NICHT kann
- Flows / Keyword-Trigger / Auto-Antworten **bauen oder ändern** → nur Browser (wie heute).
- Instagrams 24-h-Messaging-Fenster aushebeln.
- Analysen jenseits dessen, was die API hergibt.

## Technischer Ansatz (wenn Stufe 2 kommt)
- Lokaler MCP-Server (Python/Node) auf Katjas Mac, hält den ManyChat-API-Key.
- Pattern wie `scripts/instagram-watch/`: Secrets in gitignored `config.json`, nie committen.
- Tools mappen auf die ManyChat-API: Subscriber lesen/suchen, Tags/Felder setzen, Flow auslösen (sendFlow), Nachricht senden (sendContent).
