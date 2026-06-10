# Instagram-Späher

Täglicher Bot, der die wichtigsten Wettbewerber-Accounts auf neue
Reels/Posts prüft, sie (falls Claude CLI installiert ist) durch Katjas
Strategie/Marke analysiert und das Ergebnis per Telegram schickt.

**Beobachtete Accounts:** @entspannungsstudio_anila · @jasmin.bachman · @kerstin.huber.steinhorst · @nadine_weiland_yoga
(änderbar in `config.json`)

---

## Wie es funktioniert

1. `launchd` startet täglich um 18:00 `run.sh` → `watch.py`.
2. `watch.py` holt über **Apify** die neuesten Beiträge je Account.
3. Es vergleicht mit `state.json` (was schon bekannt war) → nur **neue** Beiträge zählen.
4. **Analyse:** Wenn das Claude Code CLI vorhanden ist, schreibt Claude eine kurze
   Analyse pro Beitrag (Hook, was funktioniert, was du mitnimmst).
   Sonst gibt's eine saubere Liste mit Link, Format und Zahlen.
5. Versand per **Telegram**.
6. Jede gesendete Nachricht wird zusätzlich lokal mitgeschrieben:
   `sent/JJJJ-MM-TT.txt` (mehrere Läufe am Tag werden mit Zeitstempel angehängt).
   So lässt sich jederzeit nachlesen, was verschickt wurde — gitignored.

Am ersten Lauf wird nur der aktuelle Stand gespeichert (kein Beitrags-Flut) — ab dem
nächsten Tag kommen echte Neuigkeiten.

---

## Einrichtung (einmalig, ~10 Min)

### 1. Apify-Token holen (Instagram-Abruf, gratis)
1. Auf https://apify.com kostenlos registrieren.
2. Links auf **Settings → Integrations → API tokens**.
3. Token kopieren.
4. In `config.json` bei `apify_token` einsetzen.

Das Gratis-Kontingent (5 $ Plattform-Guthaben/Monat) reicht für 3 Accounts/Tag locker.

### 2. Telegram-Bot erstellen (Versand, gratis)
1. In Telegram **@BotFather** öffnen → `/newbot` → Namen vergeben.
2. BotFather gibt dir einen **Token** (Form `123456:ABC-...`). → in `config.json` bei
   `telegram_bot_token` einsetzen.
3. Öffne deinen neuen Bot in Telegram und schick ihm **irgendeine Nachricht** ("hallo").
4. Im Terminal:
   ```
   cd scripts/instagram-watch
   python3 get_chat_id.py
   ```
   Die angezeigte Zahl bei `telegram_chat_id` in `config.json` eintragen.

### 3. (Optional, für die Analyse) Claude Code CLI installieren
Ohne dieses CLI bekommst du eine saubere Beitrags-Liste. Mit ihm die volle Analyse —
kostenlos über dein Claude-Abo.
```
npm install -g @anthropic-ai/claude-code
claude         # einmal starten und mit deinem Claude-Account einloggen
```

### 4. Testlauf
```
cd scripts/instagram-watch
python3 watch.py
```
Beim ersten Mal: Telegram-Nachricht "Späher eingerichtet …". Läuft das, weiter zu Schritt 5.

### 5. Täglichen Lauf aktivieren (launchd)
```
cp scripts/instagram-watch/com.katja.instagram-watch.plist ~/Library/LaunchAgents/
launchctl load ~/Library/LaunchAgents/com.katja.instagram-watch.plist
```
Fertig. Der Bot meldet sich ab jetzt täglich um 18:00.

**Uhrzeit ändern:** `Hour`/`Minute` in der plist anpassen, dann
`launchctl unload …` und wieder `load`.
**Abschalten:** `launchctl unload ~/Library/LaunchAgents/com.katja.instagram-watch.plist`

---

## Dateien
| Datei | Zweck |
|---|---|
| `watch.py` | Hauptskript (Abruf, Vergleich, Analyse, Versand) |
| `config.json` | Tokens & Accounts — **gitignored**, nie committen |
| `config.example.json` | Vorlage zum Kopieren |
| `get_chat_id.py` | Telegram chat_id ermitteln |
| `run.sh` | Wrapper für launchd (setzt PATH) |
| `com.katja.instagram-watch.plist` | Zeitplan für launchd |
| `state.json` | gemerkte Beiträge — wird automatisch angelegt, gitignored |
| `sent/JJJJ-MM-TT.txt` | Kopie jeder gesendeten Telegram-Nachricht, gitignored |
| `watch.log` / `launchd.*.log` | Protokolle, gitignored |

---

## Fehlersuche
- **Nichts kommt an:** `cat scripts/instagram-watch/watch.log` ansehen.
- **Apify-Fehler:** Token prüfen, Apify-Guthaben checken (apify.com → Billing).
- **Keine Analyse, nur Liste:** Claude CLI ist nicht installiert/eingeloggt (Schritt 3).
- **Mac war um 18:00 aus:** launchd holt den Lauf beim nächsten Aufwachen nach.

## Spätere Upgrades
- **Läuft nur, wenn der Mac an ist.** Wenn das stört: auf einen Cloud-Lauf umstellen
  (Apify-Scheduler oder ein kleiner Server). Apify-Abruf, Analyse-Prompt und
  Telegram-Versand bleiben identisch.
